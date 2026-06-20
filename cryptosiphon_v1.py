import sys

# Снимаем ограничение Python на количество знаков в числе для длинной арифметики
sys.set_int_max_str_digits(100000)

class TopologicalSiphonCipher:
    def __init__(self, steps=111):
        """
        Инициализация шифратора.
        steps — количество шагов лавинного разгона (глубина запутывания).
        По умолчанию берем 111 шагов (резонанс числа 27).
        """
        self.steps = steps

    def _text_to_int(self, text: str) -> int:
        """Переводит текст в один гигантский целочисленный битовый паспорт"""
        encoded_bytes = text.encode('utf-8')
        return int.from_bytes(encoded_bytes, byteorder='big')

    def _int_to_text(self, number: int) -> str:
        """Переводит битовый паспорт числа обратно в текст"""
        try:
            byte_length = (number.bit_length() + 7) // 8
            decoded_bytes = number.to_bytes(byte_length, byteorder='big')
            return decoded_bytes.decode('utf-8')
        except Exception:
            return "[Ошибка дешифровки: Крах топологического сифона]"

    def encrypt(self, plain_text: str) -> dict:
        """
        Прямой ход (Шифрование через лавинный клин).
        Превращает текст в хаотичную пространственную координату.
        """
        n = self._text_to_int(plain_text)
        
        # Гарантируем, что стартовое число нечетное, чтобы активировать лавину
        padding_bit = 0
        if n % 2 == 0:
            n = (n << 1) + 1
            padding_bit = 1
            
        trajectory_log = []
        current = n
        
        # Прогоняем число через сифон для генерации carry wave хаоса
        for _ in range(self.steps):
            if current % 2 != 0:
                # Лавинный клин: T(n) = (n << 1) + n + 1 (эквивалент 3n + 1)
                current = (current << 1) + current + 1
                trajectory_log.append(1) # Фиксируем фазу лавины
            else:
                # Синий нырок: деление на 2
                current = current // 2
                trajectory_log.append(0) # Фиксируем фазу диссипации
                
        return {
            "ciphertext": current,
            "private_key_path": trajectory_log,
            "padding_bit": padding_bit
        }

    def decrypt(self, cipher_data: dict) -> str:
        """
        Обратный ход (Дешифровка через зеркальный оператор изнанки).
        Разворачивает спираль на основе траекторного ключа вакантных мест.
        """
        current = cipher_data["ciphertext"]
        path = cipher_data["private_key_path"]
        padding_bit = cipher_data["padding_bit"]
        
        # Идем строго обратно по фазовому логу (с конца обратного дерева)
        for phase in reversed(path):
            if phase == 0:
                # Обратный синий нырок: восстанавливаем четность умножением на 2
                current = current * 2
            else:
                # Обратный зеркальный лавинный клин: (n - 1) / 3
                # Интегрированная ИИ-проверка на целостность и подделку маршрута
                if (current - 1) % 3 != 0:
                    raise ValueError("[Крах сифона]: Обнаружен поддельный или поврежденный маршрут ключа!")
                current = (current - 1) // 3
                
        # Снимаем паддинг, если он был
        if padding_bit == 1:
            current = current >> 1
            
        return self._int_to_text(current)

# ==========================================
# ДЕМОНСТРАЦИЯ РАБОТЫ ПРОТОТИПА v1.0
# ==========================================
if __name__ == "__main__":
    # Исходный секретный манифест
    secret_data = "mrDarkDuck. collatz-3d-attractor v4.0.0. Проект успешно завершен и запечатан."
    
    print(f"1. Исходный текст: '{secret_data}'\n")
    
    # Инициализируем «Топологический сифон»
    siphon = TopologicalSiphonCipher(steps=111)
    
    # Шифруем данные
    encrypted_packet = siphon.encrypt(secret_data)
    
    print(f"2. Шифротекст (Гигантская координата Z аттрактора):\n{encrypted_packet['ciphertext']}\n")
    print(f"3. Размер приватного траекторного ключа (бит): {len(encrypted_packet['private_key_path'])}")
    print(f"   Фрагмент лога вакантных мест фаз: {encrypted_packet['private_key_path'][:20]}...\n")
    
    # Расшифровываем зеркальным оператором
    decrypted_data = siphon.decrypt(encrypted_packet)
    
    print(f"4. Результат дешифровки зеркального мира: '{decrypted_data}'")
