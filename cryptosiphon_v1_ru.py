import sys
import locale

# Remove Python's limit on integer string conversion for arbitrary-precision math
# Снимаем ограничение Python на количество знаков в числе для длинной арифметики
sys.set_int_max_str_digits(100000)

# Localization dictionary / Словарь локализации
LOCALIZATION = {
    "ru": {
        "start": "1. Исходный текст: '{text}'\n",
        "cipher": "2. Шифротекст (Гигантская координата Z аттрактора):\n{cipher}\n",
        "key_size": "3. Размер приватного траекторного ключа (бит): {size}",
        "key_frag": "   Фрагмент лога вакантных мест фаз: {frag}...\n",
        "decrypt": "4. Результат дешифровки зеркального мира: '{text}'",
        "err_decrypt": "[Ошибка дешифровки: Крах топологического сифона]",
        "err_route": "[Крах сифона]: Обнаружен поддельный или поврежденный маршрут ключа!"
    },
    "en": {
        "start": "1. Original text: '{text}'\n",
        "cipher": "2. Ciphertext (Massive Z-coordinate of the attractor):\n{cipher}\n",
        "key_size": "3. Private trajectory key size (bits): {size}",
        "key_frag": "   Vacant space phase log fragment: {frag}...\n",
        "decrypt": "4. Mirror world decryption result: '{text}'",
        "err_decrypt": "[Decryption Error: Topological Siphon Collapse]",
        "err_route": "[Siphon Collapse]: Fake or corrupted key trajectory detected!"
    }
}

# Automatically detect system language / Автоматически определяем язык системы
try:
    sys_lang = locale.getdefaultlocale()[0][:2].lower()
except Exception:
    sys_lang = "en"

LANG = LOCALIZATION.get(sys_lang, LOCALIZATION["en"])


class TopologicalSiphonCipher:
    def __init__(self, steps=111):
        """
        Initialize the cipher. steps = avalanche depth (111 steps = number 27 resonance).
        Инициализация шифратора. steps — глубина лавинного разгона (111 шагов = резонанс числа 27).
        """
        self.steps = steps

    def _text_to_int(self, text: str) -> int:
        """Convert text string to a single massive bitwise passport // Перевод текста в битовый паспорт"""
        encoded_bytes = text.encode('utf-8')
        return int.from_bytes(encoded_bytes, byteorder='big')

    def _int_to_text(self, number: int) -> str:
        """Convert bitwise passport back to text // Перевод битового паспорта обратно в текст"""
        try:
            byte_length = (number.bit_length() + 7) // 8
            decoded_bytes = number.to_bytes(byte_length, byteorder='big')
            return decoded_bytes.decode('utf-8')
        except Exception:
            return LANG["err_decrypt"]

    def encrypt(self, plain_text: str) -> dict:
        """
        Forward path (Avalanche wedge). Encrypts text into a chaotic spatial coordinate.
        Прямой ход (Лавинный клин). Превращает текст в хаотичную пространственную координату.
        """
        n = self._text_to_int(plain_text)
        
        # Guarantee that the seed number is odd to force launch the avalanche
        # Гарантируем, что стартовое число нечетное, чтобы активировать лавину
        padding_bit = 0
        if n % 2 == 0:
            n = (n << 1) + 1
            padding_bit = 1
            
        trajectory_log = []
        current = n
        
        # Process the number through the siphon to generate carry wave chaos
        # Прогоняем число через сифон для генерации carry wave хаоса
        for _ in range(self.steps):
            if current % 2 != 0:
                # Avalanche wedge: T(n) = (n << 1) + n + 1 (3n + 1 equivalent)
                # Лавинный клин: T(n) = (n << 1) + n + 1 (эквивалент 3n + 1)
                current = (current << 1) + current + 1
                trajectory_log.append(1) # Phase 1: Avalanche
            else:
                # Blue dive: division by 2
                # Синий нырок: деление на 2
                current = current // 2
                trajectory_log.append(0) # Phase 0: Dissipation
                
        return {
            "ciphertext": current,
            "private_key_path": trajectory_log,
            "padding_bit": padding_bit
        }

    def decrypt(self, cipher_data: dict) -> str:
        """
        Reverse path (Mirror operator). Unwinds the spiral using the vacant phase map.
        Обратный ход (Зеркальный оператор). Разворачивает спираль на основе карты фаз.
        """
        current = cipher_data["ciphertext"]
        path = cipher_data["private_key_path"]
        padding_bit = cipher_data["padding_bit"]
        
        # Unwind strictly backward from the edge of the inverse tree
        # Идем строго обратно по фазовому логу с конца обратного дерева
        for phase in reversed(path):
            if phase == 0:
                # Reverse blue dive: restore parity by multiplying by 2
                # Обратный синий нырок: восстанавливаем четность умножением на 2
                current = current * 2
            else:
                # Reverse mirror avalanche wedge: (n - 1) / 3 with route integrity check
                # Обратный лавинный клин: (n - 1) / 3 с проверкой целостности маршрута
                if (current - 1) % 3 != 0:
                    raise ValueError(LANG["err_route"])
                current = (current - 1) // 3
                
        # Remove padding bit if it was applied // Снимаем паддинг, если он был
        if padding_bit == 1:
            current = current >> 1
            
        return self._int_to_text(current)


# ==========================================
# PROTOTYPE VALIDATION RUN / ДЕМОНСТРАЦИЯ
# ==========================================
if __name__ == "__main__":
    # Test secret dataset (Multilingual demonstration)
    # Тестовый секретный текст (Двуязычная демонстрация)
    secret_data = "mrDarkDuck. collatz-3d-attractor v4.0.0. Sealed / Проект запечатан."
    
    print(LANG["start"].format(text=secret_data))
    
    # Initialize the Topological Siphon engine
    # Инициализируем движок «Топологического сифона»
    siphon = TopologicalSiphonCipher(steps=111)
    
    # Execute forward encryption path // Запускаем шифрование
    encrypted_packet = siphon.encrypt(secret_data)
    
    print(LANG["cipher"].format(cipher=encrypted_packet['ciphertext']))
    print(LANG["key_size"].format(size=len(encrypted_packet['private_key_path'])))
    print(LANG["key_frag"].format(frag=encrypted_packet['private_key_path'][:20]))
    
    # Execute reverse mirror decryption path // Запускаем дешифровку
    decrypted_data = siphon.decrypt(encrypted_packet)
    
    print(LANG["decrypt"].format(text=decrypted_data))
