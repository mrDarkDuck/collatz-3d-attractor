# -*- coding: utf-8 -*-
"""
Проект: collatz-3d-attractor (Аддендум: Лавинный Клин)
Автор: Кирилл Максимов (GitHub: @mrDarkDuck)
Описание: Скрипт для визуализации волны переноса битов при операции 3x+1.
          Показывает, как уничтожается хаотичный хвост числа.
"""

def analyze_bit_avalanche(n):
    if n % 2 == 0:
        return "Ошибка: Метод применим только к нечетным числам (тип 1)."
        
    x = n
    two_x = x << 1  # Сдвиг влево (умножение на 2)
    three_x = two_x + x
    result = three_x + 1
    
    # Форматируем в двоичный вид с выравниванием по правому краю
    max_len = len(bin(result)[2:]) + 2
    
    str_x = bin(x)[2:].rjust(max_len, '.')
    str_two_x = bin(two_x)[2:].rjust(max_len, '.')
    str_res = bin(result)[2:].rjust(max_len, '.')
    
    # Считаем количество завершающих нулей (степень суперчетности)
    trailing_zeros = len(str_res) - len(str_res.rstrip('0'))
    
    print(f"--- Анализ числа n = {n} ---")
    print(f"       x:  {str_x}  (Исходное нечетное)")
    print(f"     2x:  {str_two_x}  (Сдвиг на 1 бит)")
    print(f" + 1 (итого 3x+1):")
    print(f" Результат: {str_res}  (Завершающих нулей: {trailing_zeros})")
    
    # Классификация результата по нашей троичной логике
    if result % 4 == 0:
        print(f" Статус: Всплытие на зеленый каркас 0a (делится на {2**trailing_zeros})")
    else:
        print(f" Статус: Вход в синий виток торнадо 0b")
    print("-" * (max_len + 30))

if __name__ == "__main__":
    print("=== СИМУЛЯЦИЯ БИТОВОЙ ЛАВИНЫ (ПРИМЕРЫ) ===\n")
    # Протестируем несколько чисел, включая «титанов»
    test_numbers = [7, 27, 85, 127]
    for num in test_numbers:
        analyze_bit_avalanche(num)
