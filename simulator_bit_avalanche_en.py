# -*- coding: utf-8 -*-
"""
Project: collatz-3d-attractor (Addendum: Avalanche Wedge)
Author: Kirill Maksimov (GitHub: @mrDarkDuck)
Description: Script visualizing the bit carry wave during the 3x+1 operation.
             Demonstrates how the chaotic tail of a number is destroyed.
"""

def analyze_bit_avalanche(n):
    if n % 2 == 0:
        return "Error: This method applies only to odd numbers (type 1)."
        
    x = n
    two_x = x << 1  # Bitwise shift left (multiply by 2)
    three_x = two_x + x
    result = three_x + 1
    
    # Binary formatting with right alignment
    max_len = len(bin(result)[2:]) + 2
    
    str_x = bin(x)[2:].rjust(max_len, '.')
    str_two_x = bin(two_x)[2:].rjust(max_len, '.')
    str_res = bin(result)[2:].rjust(max_len, '.')
    
    # Count trailing zeros (degree of super-evenness)
    trailing_zeros = len(str_res) - len(str_res.rstrip('0'))
    
    print(f"--- Analysis for n = {n} ---")
    print(f"       x:  {str_x}  (Original Odd)")
    print(f"     2x:  {str_two_x}  (Shifted by 1 bit)")
    print(f" + 1 (total 3x+1):")
    print(f" Result: {str_res}  (Trailing zeros: {trailing_zeros})")
    
    # State classification based on our ternary logic
    if result % 4 == 0:
        print(f" Status: Surfacing onto the green framework 0a (divisible by {2**trailing_zeros})")
    else:
        print(f" Status: Forced into the blue tornado loop 0b")
    print("-" * (max_len + 30))

if __name__ == "__main__":
    print("=== BIT AVALANCHE SIMULATION (EXAMPLES) ===\n")
    test_numbers = [7, 27, 85, 127]
    for num in test_numbers:
        analyze_bit_avalanche(num)
