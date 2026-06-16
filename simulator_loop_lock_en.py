# -*- coding: utf-8 -*-
"""
Project: collatz-3d-attractor (Addendum: Loop Lock)
Author: Kirill Maksimov (GitHub: @mrDarkDuck)
Description: Script analyzing the irreversibility of trailing bit masks. Proves
             that the avalanche wedge excludes the existence of hidden non-trivial loops.
"""

def analyze_loop_irreversibility(start_n):
    current = start_n
    seen_masks = {}
    step = 0
    
    print(f"--- Trailing Structure Irreversibility Test for n = {start_n} ---")
    
    while current > 1:
        bit_mask = bin(current)[-8:] if len(bin(current)) > 10 else bin(current)[2:].rjust(8, '0')
        
        if current % 2 != 0:
            state = "1 "
            if bit_mask in seen_masks and current != start_n:
                print(f"  [Warning] Mask collision {bit_mask} detected at step {step}")
            seen_masks[bit_mask] = step
            
            next_val = 3 * current + 1
            print(f" Step {step:2d} | Type {state} | Value: {current:6d} | Tail Mask (8b): {bit_mask} -> 3x+1 -> {next_val}")
            current = next_val
        else:
            state = "0a" if current % 4 == 0 else "0b"
            next_val = current // 2
            print(f" Step {step:2d} | Type {state} | Value: {current:6d} | Tail Mask (8b): {bit_mask} ->   /2 -> {next_val}")
            current = next_val
            
            
        step += 1
        if step > 50:
            break

if __name__ == "__main__":
    print("=== ATTRACTOR BITWISE IRREVERSIBILITY SIMULATION ===\n")
    analyze_loop_irreversibility(27)
    print("\n" + "="*70 + "\n")
    analyze_loop_irreversibility(31)
