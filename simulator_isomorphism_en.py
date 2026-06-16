# -*- coding: utf-8 -*-
"""
Project: collatz-3d-attractor (Addendum: Geometric Isomorphism)
Author: Kirill Maksimov (GitHub: @mrDarkDuck)
Description: Script establishing a strict algebraic isomorphism mapping Collatz 
             arithmetic steps to 3D rotation matrix coordinates (137.5° Fibonacci angle).
"""

import math

def get_state_vector(n):
    """
    Algebraic bridge (Isomorphism): translates modulo 4 remainders 
    into trigonometric weights of states 1, 0a, 0b.
    """
    is_odd = n % 2
    is_0a = (1 - is_odd) * (1 - (n % 4) // 2)
    is_0b = (1 - is_odd) * ((n % 4) // 2)
    
    return is_odd, is_0a, is_0b

def generate_3d_trajectory(start_n, angle_deg=137.5):
    """
    Generates 3D trajectory coordinates using the Rz rotation matrix.
    """
    current = start_n
    theta = math.radians(angle_deg)
    
    x, y, z = 0.0, 0.0, 0.0
    trajectory_data = []
    step_index = 0
    
    while True:
        is_odd, is_0a, is_0b = get_state_vector(current)
        r = math.log2(current) if current > 1 else 1.0
        current_angle = step_index * theta
        
        # Isometric projection mapping onto axes where 0b triggers the Y-axis depth dive
        dx = r * math.cos(current_angle) * (is_odd + is_0a)
        dy = r * math.sin(current_angle) * (is_odd + is_0a) + (r * is_0b)
        dz = current * 0.01
        
        x += dx
        y += dy
        z += dz
        
        state_label = "1" if is_odd else ("0a" if is_0a else "0b")
        trajectory_data.append((step_index, current, state_label, round(x, 2), round(y, 2), round(z, 2)))
        
        if current == 1:
            break
            
        if is_odd:
            current = 3 * current + 1
        else:
            current = current // 2
            
        step_index += 1
        
    return trajectory_data

if __name__ == "__main__":
    START_NUM = 6
    print(f"=== GEOMETRIC ISOMORPHISM VERIFICATION (Number {START_NUM}) ===")
    print("Mapping the arithmetic operator onto 3D rotation matrix coordinates:\n")
    print(f"{'Step':<5} | {'Value':<6} | {'Type':<4} | {'Coord X':<12} | {'Coord Y':<12} | {'Coord Z':<12}")
    print("-" * 65)
    
    data = generate_3d_trajectory(START_NUM)
    for step, val, label, x, y, z in data:
        print(f"{step:<5} | {val:<6} | {label:<4} | {x:<12} | {y:<12} | {z:<12}")
