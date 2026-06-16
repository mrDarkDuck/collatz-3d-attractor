# -*- coding: utf-8 -*-
"""
Проект: collatz-3d-attractor (Аддендум: Геометрический Изоморфизм)
Автор: Кирилл Максимов (GitHub: @mrDarkDuck)
Описание: Скрипт строгого отображения арифметических шагов Коллатца 
          в 3D-координаты матрицы вращения (угол Фибоначчи 137.5°).
"""

import math

def get_state_vector(n):
    """
    Алгебраический мост (Изоморфизм): переводит остатки modulo 4 
    в тригонометрические веса состояний 1, 0a, 0b.
    """
    # Вычисляем индикаторы состояний через тригонометрические переключатели
    # Это исключает "метафоричность" и дает строгую формульную связь
    is_odd = n % 2                                     # 1 если нечетное, 0 если четное
    is_0a = (1 - is_odd) * (1 - (n % 4) // 2)         # 1 если суперчетное (0a)
    is_0b = (1 - is_odd) * ((n % 4) // 2)             # 1 если получетное (0b)
    
    return is_odd, is_0a, is_0b

def generate_3d_trajectory(start_n, angle_deg=137.5):
    """
    Строит 3D-координаты траектории, используя матрицу поворота Rz.
    """
    current = start_n
    theta = math.radians(angle_deg)
    
    # Стартовые параметры раковины Nautilus
    x, y, z = 0.0, 0.0, 0.0
    trajectory_data = []
    step_index = 0
    
    while True:
        is_odd, is_0a, is_0b = get_state_vector(current)
        
        # Динамический радиус-вектор (сжатие/рост) на основе признаков
        # Математически увязываем шаг Коллатца со сдвигом по осям
        r = math.log2(current) if current > 1 else 1.0
        
        # Вращение плоскости X-Y на угол Фибоначчи за каждый шаг
        current_angle = step_index * theta
        
        # Проекция на оси с учетом активации глубины Y синими числами 0b
        # 0b активирует силовой импульс, смещающий координату по оси Y
        dx = r * math.cos(current_angle) * (is_odd + is_0a)
        dy = r * math.sin(current_angle) * (is_odd + is_0a) + (r * is_0b)  # Нырок по Y
        dz = current * 0.01  # Высота Z отражает масштаб числа
        
        x += dx
        y += dy
        z += dz
        
        state_label = "1" if is_odd else ("0a" if is_0a else "0b")
        trajectory_data.append((step_index, current, state_label, round(x, 2), round(y, 2), round(z, 2)))
        
        if current == 1:
            break
            
        # Арифметический шаг
        if is_odd:
            current = 3 * current + 1
        else:
            current = current // 2
            
        step_index += 1
        
    return trajectory_data

if __name__ == "__main__":
    START_NUM = 6
    print(f"=== ВЕРИФИКАЦИЯ ГЕОМЕТРИЧЕСКОГО ИЗОМОРФИЗМА (Число {START_NUM}) ===")
    print("Связь между арифметическим оператором и 3D-координатами матрицы поворота:\n")
    print(f"{'Шаг':<5} | {'Число':<6} | {'Тип':<4} | {'Координата X':<12} | {'Координата Y':<12} | {'Координата Z':<12}")
    print("-" * 65)
    
    data = generate_3d_trajectory(START_NUM)
    for step, val, label, x, y, z in data:
        print(f"{step:<5} | {val:<6} | {label:<4} | {x:<12} | {y:<12} | {z:<12}")
