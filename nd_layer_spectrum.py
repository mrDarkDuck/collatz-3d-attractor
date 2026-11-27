#!/usr/bin/env python3
"""
Addendum VII Verification Script:
Phase-Space Quantization (Nd-Layers), Inter-Layer Transition Spectrum (Delta k),
and the 2-Adic Mersenne Ascent Limit (2^m - 1).

Repository: collatz-3d-attractor
"""

import math
import random
from collections import Counter


def get_nd_layer(x: int) -> int:
    """Returns the dyadic Nd-layer index k = floor(log2(x))."""
    return x.bit_length() - 1


def get_ternary_state(x: int) -> str:
    """Classifies integer into O (Odd), E_0b (Semi-Even), or E_0a (Super-Even)."""
    if x & 1:
        return "O"
    return "E_0a" if (x & 3) == 0 else "E_0b"


def compressed_step(x: int) -> tuple[int, int]:
    """
    Performs one compressed cycle (O -> O'):
    Applies 3x + 1 and divides by 2^v until the next odd integer is reached.
    Returns (next_odd, divisions_count).
    """
    val = 3 * x + 1
    v = (val & -val).bit_length() - 1
    return val >> v, v


def verify_scale_invariance(layers: list[int] = [10, 50, 256, 1024], samples: int = 50_000):
    """Verifies that state densities (O: 50%, E_0b: 25%, E_0a: 25%) are invariant across Nd-layers."""
    print("=" * 72)
    print("1. SCALE INVARIANCE ACROSS Nd-LAYERS (THEOREM 1)")
    print("=" * 72)
    print(f"{'Layer k':<12} | {'O (Odd) %':<14} | {'E_0b (Semi) %':<16} | {'E_0a (Super) %':<16}")
    print("-" * 72)

    for k in layers:
        counts = Counter()
        for _ in range(samples):
            # Random integer strictly inside [2^k, 2^(k+1))
            x = (1 << k) | random.getrandbits(k)
            counts[get_ternary_state(x)] += 1

        p_o = counts["O"] / samples * 100
        p_0b = counts["E_0b"] / samples * 100
        p_0a = counts["E_0a"] / samples * 100
        print(f"k = {k:<8} | {p_o:>11.2f}%   | {p_0b:>13.2f}%   | {p_0a:>13.2f}%")
    print()


def analyze_transition_spectrum(samples: int = 100_000, bit_length: int = 512) -> dict[int, float]:
    """Computes empirical vs. theoretical Delta k distribution for compressed O -> O' cycles."""
    print("=" * 72)
    print(f"2. INTER-LAYER TRANSITION SPECTRUM (Delta k) | N = {samples:,}, {bit_length}-bit")
    print("=" * 72)

    transitions = Counter()
    total_drift = 0

    for _ in range(samples):
        # Random odd number in layer k = bit_length - 1
        x = (1 << (bit_length - 1)) | random.getrandbits(bit_length - 1) | 1
        k_start = get_nd_layer(x)
        x_next, _ = compressed_step(x)
        k_end = get_nd_layer(x_next)

        dk = k_end - k_start
        transitions[dk] += 1
        total_drift += dk

    print(f"{'Delta k':<10} | {'Empirical %':<14} | {'Theoretical %':<15} | {'Abs Error':<10}")
    print("-" * 72)

    empirical_pct = {}
    for dk in sorted(transitions.keys(), reverse=True):
        emp = transitions[dk] / samples * 100
        empirical_pct[dk] = emp

        if dk in (1, 0):
            theo = (1 / 3) * 100
        elif dk <= -1:
            theo = (1 / (3 * (2 ** abs(dk)))) * 100
        else:
            theo = 0.0

        if dk >= -8:
            print(f"{dk:+10d} | {emp:>11.2f}%   | {theo:>12.2f}%   | {abs(emp - theo):>8.2f}%")

    mean_drift = total_drift / samples
    print("-" * 72)
    print(f"Discrete Grid Drift E[Delta k]: {mean_drift:.5f} (Theoretical: -0.33333)")
    print(f"Continuous Log2 Drift:          {math.log2(3) - 2:.5f} layers/cycle\n")
    return empirical_pct


def analyze_mersenne_ascent(m_values: list[int] = [5, 10, 20, 50, 100]) -> tuple[list[int], list[int]]:
    """Simulates the 2-adic bit-fuel burn for Mersenne numbers 2^m - 1."""
    print("=" * 72)
    print("3. MERSENNE ASCENT LIMIT (2^m - 1) & BIT-FUEL CONSERVATION")
    print("=" * 72)
    print(f"{'Number':<12} | {'k_start':<8} | {'Streak':<8} | {'k_peak':<8} | {'Gain':<8} | {'Break dk':<8}")
    print("-" * 72)

    example_layers = []
    example_deltas = []

    for m in m_values:
        x = (1 << m) - 1
        k_start = get_nd_layer(x)
        k_curr = k_start
        deltas = []
        layers_trace = [k_start]

        # Run m compressed steps (m-1 ascent steps + 1 break step)
        for _ in range(m):
            x, _ = compressed_step(x)
            k_next = get_nd_layer(x)
            deltas.append(k_next - k_curr)
            layers_trace.append(k_next)
            k_curr = k_next

        k_peak = max(layers_trace)
        break_dk = deltas[-1]

        if m == 20:
            example_layers = layers_trace
            example_deltas = deltas

        print(
            f"2^{m:<3}- 1   | {k_start:<8} | {m - 1:<8} | {k_peak:<8} | "
            f"{k_peak - k_start:+8d} | {break_dk:+8d}"
        )

    print("-" * 72)
    print(f"Rhythm for 2^20 - 1: {example_deltas}\n")
    return example_layers, example_deltas


def export_plots(spectrum: dict[int, float], mersenne_layers: list[int]):
    """Generates PNG charts for the repository if matplotlib is available."""
    try:
        import matplotlib.pyplot as plt
    except ImportError:
        print("[Info] matplotlib not installed — skipping PNG chart generation.")
        return

    # Plot 1: Transition Spectrum
    dks = sorted([k for k in spectrum.keys() if k >= -7])
    emp_vals = [spectrum[k] for k in dks]
    theo_vals = [
        (1 / 3) * 100 if k in (0, 1) else (1 / (3 * (2 ** abs(k)))) * 100
        for k in dks
    ]

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(13, 5))

    x_pos = range(len(dks))
    ax1.bar([p - 0.18 for p in x_pos], emp_vals, width=0.36, label="Empirical (512-bit)", color="#2b5c8f")
    ax1.bar([p + 0.18 for p in x_pos], theo_vals, width=0.36, label="Theoretical Model", color="#d95f02", alpha=0.85)
    ax1.set_xticks(list(x_pos))
    ax1.set_xticklabels([f"{k:+d}" if k != 0 else "0" for k in dks])
    ax1.set_xlabel("Inter-Layer Shift (Δk)")
    ax1.set_ylabel("Probability (%)")
    ax1.set_title("Nd-Layer Transition Spectrum (O → O')")
    ax1.grid(axis="y", linestyle="--", alpha=0.4)
    ax1.legend()

    # Plot 2: Mersenne Ascent Ladder (2^20 - 1)
    steps = list(range(len(mersenne_layers)))
    ax2.plot(steps[:-1], mersenne_layers[:-1], marker="o", color="#1b9e77", linewidth=2, label="Ascent Phase (m-1 steps)")
    ax2.plot(steps[-2:], mersenne_layers[-2:], marker="x", markersize=9, color="#e7298a", linewidth=2, linestyle="--", label="Super-Even Break (E_0a)")
    ax2.set_xlabel("Compressed Cycle Step")
    ax2.set_ylabel("Nd-Layer Index (k)")
    ax2.set_title("Mersenne Bit-Fuel Burn: 2^20 - 1")
    ax2.grid(True, linestyle="--", alpha=0.4)
    ax2.legend()

    plt.tight_layout()
    output_file = "nd_layer_spectrum_verification.png"
    plt.savefig(output_file, dpi=150)
    print(f"[Saved] Visualization exported to '{output_file}'")


if __name__ == "__main__":
    random.seed(42)
    verify_scale_invariance()
    spectrum_data = analyze_transition_spectrum(samples=100_000, bit_length=512)
    m20_layers, _ = analyze_mersenne_ascent()
    export_plots(spectrum_data, m20_layers)
