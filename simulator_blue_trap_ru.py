# -*- coding: utf-8 -*-
"""
Проект: collatz-3d-attractor (Аддендум: Синий Капкан)
Автор: Кирилл Максимов (GitHub: @mrDarkDuck)
Описание: Автономный скрипт для верификации фрактального деления 
          чисел типа 0b (4k+2) по глубине погружения на оси Y.
"""

def analyze_blue_trap(max_n):
    # Словарь для подсчета количества чисел на каждой глубине
    depth_counts = {}
    # Словарь для хранения первых примеров траекторий
    examples = {}
    
    total_0b = 0
    
    for n in range(2, max_n + 1, 2):
        if n % 4 != 2:
            continue  # Строго анализируем только числа типа 0b
            
        total_0b += 1
        current = n
        dives = 0
        path = []
        
        while True:
            # Шаг 1: Деление на 2 (Переход 0b -> 1)
            current = current // 2
            path.append(f"1({current})")
            
            # Шаг 2: Шаг Коллатца 3x+1
            current = 3 * current + 1
            
            if current % 4 == 0:
                path.append(f"0a({current})")
                dives += 1
                break  # Число вылетело на стабильный зеленый каркас
            elif current % 4 == 2:
                path.append(f"0b({current})")
                dives += 1  # Число уходит на следующий виток торнадо
        
        # Фиксируем статистику глубины
        depth_counts[dives] = depth_counts.get(dives, 0) + 1
        
        # Сохраняем первые 2 примера для каждой глубины
        if dives not in examples:
            examples[dives] = []
        if len(examples[dives]) < 2:
            examples[dives].append((n, path))
            
    return total_0b, depth_counts, examples

if __name__ == "__main__":
    LIMIT = 100000
    print(f"=== АНАЛИЗ СИНЕГО КАПКАНА (Диапазон до {LIMIT}) ===")
    
    total_0b, counts, examples = analyze_blue_trap(LIMIT)
    print(f"Всего обнаружено чисел типа 0b (4k+2): {total_0b}\n")
    
    print("Распределение чисел по глубине витков торнадо (ось Y):")
    for depth in sorted(counts.keys()):
        qty = counts[depth]
        percentage = (qty / total_0b) * 100
        print(f"  Глубина d={depth}: {qty} шт. ({percentage:.3f}%)")
        
    print("\nПримеры траекторий для каждой глубины:")
    for depth in sorted(examples.keys()):
        print(f"\n Глубина d={depth} (Остаток n ≡ {2**(depth+1)-2} mod {2**(depth+2)}):")
        for n, path in examples[depth]:
            path_str = " -> ".join(path)
            print(f"    n = {n:3d} | Старт(0b) -> {path_str}")
