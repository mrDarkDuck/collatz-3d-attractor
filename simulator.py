import sys

def analyze_any_number_3d():
    print("=" * 65)
    print(" INTERACTIVE 3D COLLATZ CONJECTURE SIMULATOR")
    print("=" * 65)
    
    # 1. Requesting user input
    try:
        user_input = input("Enter any natural number to launch: ").strip()
        if not user_input:
            print("Error: Input cannot be empty.")
            return
        n = int(user_input)
        if n <= 0:
            print("Error: The number must be strictly greater than 0.")
            return
    except ValueError:
        print("Error: Please enter a valid integer without letters or spaces.")
        return

    start_number = n
    print(f"\n[Launch] Number {start_number} enters the outer orbit of the shell...\n")
    print(f"{'Step':<5} | {'Current Number':<20} | {'3D Attribute':<15} | {'Spatial Trajectory Action'}")
    print("-" * 90)

    step = 0
    count_1 = 0
    count_0a = 0
    count_0b = 0
    mgl_captures = 0  # Counter for instant interceptions by super-evenness

    # Variable to track the previous step state
    was_growth_last_step = False

    # 2. Main cycle of the attribute rotation
    while n != 1:
        if n % 2 != 0:
            # Odd attribute 1 (Growth Impulse)
            type_str = "1 (Odd)"
            action = "💥 Growth 3n+1 -> Upward Impulse"
            count_1 += 1
            next_n = 3 * n + 1
            was_growth_last_step = True
        else:
            # Even attribute
            if n % 4 == 0:
                type_str = "0a (Super-Even)"
                # Checking if the growth curve instantly hit this chute
                if was_growth_last_step:
                    action = "⚡ TRAP! Growth instantly intercepted by super-evenness"
                    mgl_captures += 1
                else:
                    action = "🟩 Compression -> Sliding down the chute (Z-axis)"
                count_0a += 1
            else:
                type_str = "0b (Semi-Even)"
                action = "🔵 Dive along Y-axis -> Inward spiral turn"
                count_0b += 1
            
            next_n = n // 2
            was_growth_last_step = False

        # Formatting output for ultra-large numbers
        display_num = str(n) if len(str(n)) <= 18 else str(n)[:15] + "..."
        print(f"{step:<5} | {display_num:<20} | {type_str:<15} | {action}")
        
        n = next_n
        step += 1

    # Final assembly point at the core
    print(f"{step:<5} | {1:<20} | 1 (Odd)        | 🏁 ATTRACTOR REACHED (Vortex Center)")
    count_1 += 1

    # 3. Final logical report and theory validation
    print("=" * 90)
    print(f" LOGICAL SUMMARY REPORT FOR NUMBER: {start_number}")
    print("=" * 90)
    print(f"• Total trajectory descent length: {step} steps.")
    print(f"• Deep compression cascades (Green '0a'): {count_0a}")
    print(f"• Blue axis spatial turns (Blue '0b'): {count_0b}")
    print(f"• Instant growth interceptions by super-evenness: {mgl_captures} times.")
    
    if count_1 > 1:
        capture_rate = (mgl_captures / (count_1 - 1)) * 100
        print(f"• Super-evenness trap efficiency: {capture_rate:.1f}% of growth steps cut off instantly.")
    
    total_deletions = count_0a + count_0b
    print(f"• Balance of forces: {count_1} growth impulses vs {total_deletions} division steps.")
    
    # Main conclusion based on powers of two
    print(f"• Outcome: Number collapsed into binary framework and pulled by gravity to point (0,0,0).")
    print("=" * 90)

if __name__ == "__main__":
    analyze_any_number_3d()
