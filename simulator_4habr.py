import sys
import time
import locale
import gc

# Снимаем ограничение Python на конвертацию строк для длинной арифметики
sys.set_int_max_str_digits(100000)

# Криптографические константы Блочного Сифона v5.0.0
BLOCK_SIZE_BYTES = 16  # 16 байт = 128 бит
SIPHON_STEPS = 128     # Жестко фиксированное число шагов сифона (размер ключа = 128 бит)

# ANSI Цветовая разметка терминала
RESET = "\033[0m"
BOLD = "\033[1m"
RED = "\033[31m"
GREEN = "\033[32m"
YELLOW = "\033[33m"
BLUE = "\033[34m"
CYAN = "\033[36m"
MAGENTA = "\033[35m"

LOCALIZATION = {
    "ru": {
        "welcome": f"{BOLD}{CYAN}=== БЛОЧНЫЙ ДЕМОНСТРАЦИОННЫЙ СТЕНД: SIMULATOR_4HABR (v5.0.0) ==={RESET}",
        "prompt_msg": f"{BOLD}Введите текстовое сообщение для шифрования:{RESET}\n> ",
        "err_empty": f"{RED}[Ошибка]: Сообщение не может быть пустым!{RESET}",
        "init_enc": f"\n{YELLOW}[Инициализация]: Разбиение текста на блоки по 128 бит и запуск лавины...{RESET}",
        "block_start": f"{BOLD}{CYAN}\n--- Обработка Блока №{{idx}} ---{RESET}",
        "step_info": f"{CYAN}[Шаг {{step:03d}}] {RESET}Число: {{val}} | {YELLOW}Op: {{op}}{RESET}",
        "enc_res": f"\n{GREEN}=== 1. РЕЗУЛЬТАТ БЛОЧНОГО ШИФРОВАНИЯ ==={RESET}",
        "ciphertext": f"{BOLD}Шифротекст Z (Массив координат аттрактора по блокам):{RESET}\n{MAGENTA}{{cipher}}{RESET}",
        "key_info": f"{BOLD}Размер приватного ключа для каждого блока:{RESET} {SIPHON_STEPS} бит (ЖЕСТКО ФИКСИРОВАН)",
        "key_frag": f"{BOLD}МАССИВ ПРИВАТНЫХ КЛЮЧЕЙ ДЛЯ КОПИРОВАНИЯ (через запятую):{RESET}\n{GREEN}{{frag}}{RESET}",
        "time_op": f"{BLUE}Время выполнения операции: {{t:.6f}} сек.{RESET}",
        "ram_clear": f"\n{RED}[БЕЗОПАСНОСТЬ]: Буфер памяти полностью очищен от исходного текста (del + gc.collect()).{RESET}",
        "prompt_custom_key": f"\n{BOLD}{CYAN}--- ОБРАТНЫЙ ХОД (ПОБЛОЧНЫЙ ДЕШИФРАТОР) ---{RESET}\n{BOLD}Введите массив ключей дешифровки через запятую (или 0 для выхода):{RESET}\n> ",
        "err_invalid_bin": f"{RED}[Ошибка]: Ключи должны состоять только из 0 и 1 и быть длиной {SIPHON_STEPS} бит!{RESET}",
        "err_block_count": f"{RED}[Ошибка]: Количество введенных ключей не совпадает с количеством блоков шифротекста (требуется: {{req}})!{RESET}",
        "init_dec": f"\n{YELLOW}[Инициализация]: Зеркальный оператор восстанавливает блоки из сингулярности...{RESET}",
        "step_dec_info": f"{CYAN}[Шаг дешифровки] {RESET}Число: {{val}} | {BLUE}Op: {{op}}{RESET}",
        "dec_res": f"\n{GREEN}=== 2. РЕЗУЛЬТАТ ОБРАТНОГО ХОДА (ДЕШИФРОВКА УСПЕШНА) ==={RESET}",
        "dec_text": f"{BOLD}Результат поблочной сборки зеркального мира:{RESET}\n'{GREEN}{{text}}{RESET}'",
        "err_collapse": f"{RED}[Крах сифона]: В блоке №{{idx}} обнаружен ложный маршрут ключа! Траектория уничтожена.{RESET}",
        "err_utf8": f"{RED}[Ошибка дешифровки]: Топологический коллапс. Восстановленный массив поврежден.{RESET}",
        "success_msg": f"\n{BOLD}{GREEN}🎉 ПОЗДРАВЛЯЕМ! Все блоки успешно прошли через сифон, исходный текст полностью восстановлен!{RESET}",
        "exit": f"\n{CYAN}Сессия завершена. Блочный проект запечатан.{RESET}"
    },
    "en": {
        "welcome": f"{BOLD}{CYAN}=== BLOCK-BASED DEMO BENCH: SIMULATOR_4HABR (v5.0.0) ==={RESET}",
        "prompt_msg": f"{BOLD}Enter a text message to encrypt:{RESET}\n> ",
        "err_empty": f"{RED}[Error]: Message cannot be empty!{RESET}",
        "init_enc": f"\n{YELLOW}[Initialization]: Splitting text into 128-bit blocks and launching avalanche...{RESET}",
        "block_start": f"{BOLD}{CYAN}\n--- Processing Block №{{idx}} ---{RESET}",
        "step_info": f"{CYAN}[Step {{step:03d}}] {RESET}State: {{val}} | {YELLOW}Op: {{op}}{RESET}",
        "enc_res": f"\n{GREEN}=== 1. BLOCK ENCRYPTION RESULT ==={RESET}",
        "ciphertext": f"{BOLD}Ciphertext Z (Array of attractor coordinates per block):{RESET}\n{MAGENTA}{{cipher}}{RESET}",
        "key_info": f"{BOLD}Private key size for each block:{RESET} {SIPHON_STEPS} bits (STRICTLY FIXED)",
        "key_frag": f"{BOLD}ARRAY OF PRIVATE KEYS FOR COPYING (comma-separated):{RESET}\n{GREEN}{{frag}}{RESET}",
        "time_op": f"{BLUE}Operation execution time: {{t:.6f}} sec.{RESET}",
        "ram_clear": f"\n{RED}[SECURITY]: RAM buffer completely cleared of raw plaintext (del + gc.collect()).{RESET}",
        "prompt_custom_key": f"\n{BOLD}{CYAN}--- REVERSE PATH (BLOCK DECRYPTOR) ---{RESET}\n{BOLD}Enter the array of decryption keys comma-separated (or 0 to exit):{RESET}\n> ",
        "err_invalid_bin": f"{RED}[Error]: Keys must contain only 0 and 1, and be exactly {SIPHON_STEPS} bits long!{RESET}",
        "err_block_count": f"{RED}[Error]: Number of keys provided does not match ciphertext block count (required: {{req}})!{RESET}",
        "init_dec": f"\n{YELLOW}[Initialization]: Mirror operator recovering blocks from origin...{RESET}",
        "step_dec_info": f"{CYAN}[Decryption Step] {RESET}State: {{val}} | {BLUE}Op: {{op}}{RESET}",
        "dec_res": f"\n{GREEN}=== 2. REVERSE PATH RESULT (DECRYPTION SUCCESSFUL) ==={RESET}",
        "dec_text": f"{BOLD}Block-reassembled mirror world decryption result:{RESET}\n'{GREEN}{{text}}{RESET}'",
        "err_collapse": f"{RED}[Siphon Collapse]: Fake key trajectory detected in block №{{idx}}! Route destroyed.{RESET}",
        "err_utf8": f"{RED}[Decryption Error]: Topological collapse. Recovered byte array is corrupted.{RESET}",
        "success_msg": f"\n{BOLD}{GREEN}🎉 CONGRATULATIONS! All blocks successfully passed through the siphon, plaintext restored!{RESET}",
        "exit": f"\n{CYAN}Session finished. Block project sealed.{RESET}"
    }
}

try:
    sys_lang = locale.getdefaultlocale()[:2].lower()
except Exception:
    sys_lang = "en"

LANG = LOCALIZATION.get(sys_lang, LOCALIZATION["en"])

class BlockSiphonEngine:
    def __init__(self):
        self.block_size = BLOCK_SIZE_BYTES
        self.steps = SIPHON_STEPS

    def slice_to_blocks(self, text: str) -> list:
        raw_bytes = bytearray(text.encode('utf-8'))
        # Стандартный криптографический паддинг: добавляем длину паддинга в конец
        padding_len = self.block_size - (len(raw_bytes) % self.block_size)
        raw_bytes.extend([padding_len] * padding_len)
        
        blocks = []
        for i in range(0, len(raw_bytes), self.block_size):
            block_int = int.from_bytes(raw_bytes[i:i+self.block_size], byteorder='big')
            blocks.append(block_int)
        return blocks

    def remove_padding(self, raw_bytes: bytearray) -> bytearray:
        if not raw_bytes:
            return raw_bytes
        padding_len = raw_bytes[-1]
        if 0 < padding_len <= self.block_size:
            # Проверяем валидность паддинга
            if all(b == padding_len for b in raw_bytes[-padding_len:]):
                return raw_bytes[:-padding_len]
        return raw_bytes

    def encrypt_block_interactive(self, n: int, block_idx: int) -> tuple:
        print(LANG["block_start"].format(idx=block_idx))
        
        # Калибровка знака: гарантируем нечетность стартового вектора внутри блока
        padding_bit = 0
        if n % 2 == 0:
            n = (n << 1) + 1
            padding_bit = 1
            
        trajectory_log = []
        current = n
        
        for step in range(1, self.steps + 1):
            if current % 2 != 0:
                op_str = "Avalanche (current << 1) + current + 1"
                current = (current << 1) + current + 1
                trajectory_log.append(1)
            else:
                op_str = "Blue Dive (current // 2)"
                current = current // 2
                trajectory_log.append(0)
                
            val_str = str(current)
            if len(val_str) > 60:
                val_str = val_str[:30] + " ... " + val_str[-30:]
            print(LANG["step_info"].format(step=step, val=val_str, op=op_str))
                
        key_str = "".join(map(str, trajectory_log))
        return current, key_str, padding_bit

    def decrypt_block_interactive(self, ciphertext: int, key_str: str, padding_bit: int, block_idx: int) -> int:
        print(LANG["block_start"].format(idx=block_idx))
        current = ciphertext
        path = [int(c) for c in key_str]
        
        for phase in reversed(path):
            if phase == 0:
                op_str = "Reverse Blue Dive (current * 2)"
                current = current * 2
            else:
                op_str = "Reverse Avalanche ((current - 1) // 3)"
                if (current - 1) % 3 != 0:
                    return "ERR_COLLAPSE"
                current = (current - 1) // 3
                
            val_str = str(current)
            if len(val_str) > 60:
                val_str = val_str[:30] + " ... " + val_str[-30:]
            print(LANG["step_dec_info"].format(val=val_str, op=op_str))
                
        if padding_bit == 1:
            current = current >> 1
            
        return current

def main():
    print(LANG["welcome"])
    engine = BlockSiphonEngine()
    
    # 1. Предложение ввести сообщение
    plain_text = input(LANG["prompt_msg"]).strip()
    if not plain_text:
        print(LANG["err_empty"])
        return
        
    print(LANG["init_enc"])
    t_start = time.perf_counter()
    blocks = engine.slice_to_blocks(plain_text)
    
    cipher_array = []
    keys_array = []
    paddings_array = []
    
    # Поблочное шифрование
    for idx, block_val in enumerate(blocks, 1):
        c_val, k_str, p_bit = engine.encrypt_block_interactive(block_val, idx)
        cipher_array.append(c_val)
        keys_array.append(k_str)
        paddings_array.append(p_bit)
        
    t_end = time.perf_counter()
    
    # 2. Вывод на экран результатов
    true_keys_string = ", ".join(keys_array)
    print(LANG["enc_res"])
    print(LANG["ciphertext"].format(cipher=str(cipher_array)))
    print(LANG["key_info"])
    
    # ЦВЕТОВОЙ АКЦЕНТ: Выделяем важный приватный ключ зеленым цветом в консоли
    print(LANG["key_frag"].format(frag=f"{GREEN}{BOLD}{true_keys_string}{RESET}"))
    print(LANG["time_op"].format(t=t_end - t_start))
    
    # 2.1. Хирургическая очистка исходной памяти
    del plain_text
    del blocks
    gc.collect()
    print(LANG["ram_clear"])
    
    # 3. Вывод на экран предложения ввести ключ (Цикл до успешного ввода)
    while True:
        user_input_keys = input(LANG["prompt_custom_key"]).strip()
        
        # Возможность прервать операцию вручную
        if user_input_keys == "0" or user_input_keys.lower() == "exit":
            break
            
        # Парсим ключи, введенные через запятую
        input_keys_list = [k.strip() for k in user_input_keys.split(",")]
        
        if len(input_keys_list) != len(cipher_array):
            print(LANG["err_block_count"].format(req=len(cipher_array)))
            print("\n------------------------------------------------")
            continue
            
        if not all(all(c in '01' for c in k) and len(k) == SIPHON_STEPS for k in input_keys_list):
            print(LANG["err_invalid_bin"])
            print("\n------------------------------------------------")
            continue
            
        print(LANG["init_dec"])
        t_start = time.perf_counter()
        
        decrypted_blocks_bytes = bytearray()
        collapse_triggered = False
        
        # Поблочная дешифровка
        for idx, c_val in enumerate(cipher_array, 1):
            k_str = input_keys_list[idx - 1]
            p_bit = paddings_array[idx - 1] if k_str == keys_array[idx - 1] else 0
            
            dec_block_numeric = engine.decrypt_block_interactive(c_val, k_str, p_bit, idx)
            
            if dec_block_numeric == "ERR_COLLAPSE":
                print(LANG["err_collapse"].format(idx=idx))
                collapse_triggered = True
                break
                
            try:
                block_bytes = dec_block_numeric.to_bytes(BLOCK_SIZE_BYTES, byteorder='big')
                decrypted_blocks_bytes.extend(block_bytes)
            except Exception:
                print(LANG["err_utf8"])
                collapse_triggered = True
                break
                
        if collapse_triggered:
            print(LANG["time_op"].format(t=time.perf_counter() - t_start))
            print("\n------------------------------------------------")
            continue
            
        final_bytes = engine.remove_padding(decrypted_blocks_bytes)
        
        try:
            decrypted_text = final_bytes.decode('utf-8')
        except Exception:
            print(LANG["err_utf8"])
            print("\n------------------------------------------------")
            continue
            
        t_end = time.perf_counter()
        
        print(LANG["dec_res"])
        print(LANG["dec_text"].format(text=decrypted_text))
        print(LANG["time_op"].format(t=t_end - t_start))
        print(LANG["success_msg"])
        break

    print(LANG["exit"])

if __name__ == "__main__":
    main()
