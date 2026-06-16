# -*- coding: utf-8 -*-
"""
Project: collatz-3d-attractor (Blue Trap Addendum)
Author: Kirill Maksimov (GitHub: @mrDarkDuck)
Description: Autonomous script verifying the fractal distribution of 
             0b-type numbers (4k+2) along the Y-axis depth.
"""

def analyze_blue_trap(max_n):
    depth_counts = {}
    examples = {}
    total_0b = 0
    
    for n in range(2, max_n + 1, 2):
        if n % 4 != 2:
            continue  # Strictly analyze 0b-type numbers (4k+2)
            
        total_0b += 1
        current = n
        dives = 0
        path = []
        
        while True:
            # Step 1: Divide by 2 (Transition 0b -> 1)
            current = current // 2
            path.append(f"1({current})")
            
            # Step 2: Collatz Step 3x+1
            current = 3 * current + 1
            
            if current % 4 == 0:
                path.append(f"0a({current})")
                dives += 1
                break  # Truncated by the stable green framework
            elif current % 4 == 2:
                path.append(f"0b({current})")
                dives += 1  # Forced into the next tornado loop
        
        depth_counts[dives] = depth_counts.get(dives, 0) + 1
        
        if dives not in examples:
            examples[dives] = []
        if len(examples[dives]) < 2:
            examples[dives].append((n, path))
            
    return total_0b, depth_counts, examples

if __name__ == "__main__":
    LIMIT = 100000
    print(f"=== BLUE TRAP ANALYSIS (Range up to {LIMIT}) ===")
    
    total_0b, counts, examples = analyze_blue_trap(LIMIT)
    print(f"Total 0b-type numbers (4k+2) found: {total_0b}\n")
    
    print("Distribution of numbers by tornado loop depth (Y-axis):")
    for depth in sorted(counts.keys()):
        qty = counts[depth]
        percentage = (qty / total_0b) * 100
        print(f"  Depth d={depth}: {qty} pcs ({percentage:.3f}%)")
        
    print("\nTrajectory Examples for Each Depth Level:")
    for depth in sorted(examples.keys()):
        print(f"\n Depth d={depth} (Remainder n ≡ {2**(depth+1)-2} mod {2**(depth+2)}):")
        for n, path in examples[depth]:
            path_str = " -> ".join(path)
            print(f"    n = {n:3d} | Start(0b) -> {path_str}")
