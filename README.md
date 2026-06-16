# Collatz Conjecture: 3D Attractor & Ternary Logic Model
![Collatz 3D Tornado Model](collatz_tornado.png)
[switch to rus](https://mrdarkduck.github.io/collatz-3d-attractor/README_RU.html)

**Project Author:** Kirill Maksimov (GitHub: @mrDarkuck)  
**Disclaimer:** I am completely outside the world of advanced mathematics or professional academia. This project represents a look at a 90-year-old puzzle from the perspective of systems logic, binary code, and 3D geometry. It is an outsider's attempt to visualize chaos and turn dry equations into a tangible, physical model.

## 📖 The Story Behind the Concept: From Simple Math to 3D Space

To anyone encountering the Collatz Conjecture, the rules seem elementary: take a number, if it's even, divide by 2; if it's odd, multiply by 3 and add 1. Yet, behind this simplicity lies deterministic chaos. To tame it, the author went through three distinct stages of conceptual evolution:

### Stage 1: Pure Binary Logic (Even / Odd)
First, we completely discarded the magnitude of numbers. We stopped caring how large a number is and focused solely on its state: **Even (0)** or **Odd (1)**. 
Statistically, even and odd numbers are equally split (50/50) across infinity. However, the `3n+1` formula guarantees that every odd number instantly becomes even. Odd states cannot occur consecutively. This means the system is inherently biased toward decay: division by 2 (the downward pull) is mathematically more powerful than the micro-growth of multiplication.

### Stage 2: The "False Growth" Problem and the 2D Graph Deadlock
But when we tried to map this binary graph of 0s and 1s onto a flat 2D plane, we hit a wall. Even numbers (0s) behave fundamentally differently under the hood:
* Some even numbers (like 10) divide by 2 only once and immediately bounce back into an odd state.
* Other even numbers (like 16) can cascade downward, dividing by 2 multiple times in a row, racing toward unity.
On a flat plane, the trajectories tangled, intersected, and turned into an unreadable constellation. It became clear that a 2D model cannot explain why numbers don't escape to infinity.

### Stage 3: The Birth of the Blue Y-Axis and Saving the Binary System
Instead of cluttering the clean binary system (0 and 1) with new artificial math symbols, the author had a breakthrough: **translate this logical uncertainty into spatial geometry**. We differentiated even numbers by their physical behavior in space:
1.  **Green Nodes (0a / Super-Even):** Numbers of the form 4k (4, 8, 12, 16...). They allow multiple divisions by 2. In our shell geometry, they form a rigid flat framework (Z-height and X-width) along which numbers slide down.
2.  **Blue Nodes (0b / Semi-Even):** Numbers of the form 4k+2 (2, 6, 10, 14...). They can only be divided by 2 once. For these nodes, we activated a **third axis — the Y-depth axis**.

**The Core Insight:** Upon hitting a blue `0b` node, the trajectory performs a sharp "dive into the screen" along the Y-axis. This spatial shift breaks the flat graph, warping it into a perfect volumetric nautilus shell. Chaos transforms into a physical gravitational vortex, where the blue Y-axis acts as a mandatory checkpoint, forcing numbers back onto the green rails of deep compression.


## 📌 Overview
This repository contains the materials of a research project proposing a new conceptual approach to the **Collatz Conjecture (3n+1)**. Instead of the classical analysis of arithmetic values, this model translates the problem into the language of symbolic dynamics and 3D topology.

We completely abstract from the magnitude of numbers and reduce the infinite number line to a closed finite automaton with three spatial attributes (tokens): **1 (odd), 0a (super-even, 4k), and 0b (semi-even, 4k+2)**.

> **Important Note:** This work does not claim to be a completed academic proof of the theorem. It is a conceptual geometric model and an empirical tool for trajectory analysis, open for verification, discussion, and development by the community.

---

## 📐 3D Shell Architecture ("The Nautilus Model")
By mapping the state transition graph backwards in time (up the tree of ancestors) using the rules of the Golden Ratio (a twisting step of 137.5°), the system forms a conical logarithmic spiral reminiscent of a sea shell.

*   **Z-Axis (Height):** Fixes discrete time (algorithm steps). The forward trajectory is always directed from top to bottom.
*   **X-Z Plane:** Forms a rigid outer shell framework created by green super-even rails (`0a`).
*   **Y-Axis (Depth):** This additional dimension is activated exclusively by blue semi-even nodes (`0b`). Semi-evenness breaks the flat graph, forcing the trajectory to perform a deterministic "dive inward", spinning the system into a volumetric 3D tornado. The number of loops is strictly quantized by the Fibonacci sequence.

---

## ⚖️ Algebraic Trap of the Semi-Even Axis
The interaction of attributes is strictly deterministic. We have derived the formula for the **Blue Trap**, proving that the semi-even node `0b` has no structural freedom.

Any semi-even number is written as \(4k+2\). Expanding the brackets of the accelerated Collatz step \((3n+1)/2\), we get:
\[\frac{4k+2}{2} = 2k+1 \text{ (Odd '1')} \longrightarrow 3(2k+1)+1 = 6k+3+1 = \mathbf{6k+4}\]

Factoring out the four (\(4 \times (1.5k+1)\)), we algebraically prove that the semi-even node on the next step **always, without a single exception in the Universe, crashes into the green wall of super-evenness `0a`**. There is a mandatory, hard-coded spatial turn: **`0b` \(\to\) `1` \(\to\) `0a`**.

---

## 📊 Computer Simulation Results (Python)
The repository includes a Python simulator that tests the model at extreme scales (including integers up to 92 digits long). Empirical tests fully confirmed the scale invariance of the system:

*   **Super-Evenness Interception (The Interception Rate):** It is algebraically proven that the node `0b` forces a hard turn. On a long distance (a 92-digit titan, 1,955 steps), the law of large numbers confirmed the perfect interlocking of trajectories: **49.8% of all growth steps were instantly intercepted and truncated by the green super-even framework**.
*   **Balance of Forces:** On the same ultra-long distance, **639 growth impulses were recorded against 1,317 steps of division by 2**, which mathematically confirms the continuous dissipation of chaos energy and the contraction of the trajectory to the attractor `(0,0,0)` — the final `4-2-1` loop.

---

## 🏁 The Bottom Line: The Binary Gravity Rule
Computer tests and algebraic logic allow us to formulate the final conclusion of the model:

1.  **Every number in the Universe is just an incomplete power of two (\(2^x\)).** Its trajectory is a binary code cluttered with "noise" from extra ones.
2.  The \(3n+1\) step acts as a **binary vacuum cleaner**. Due to the bit-shift carry wave, it cleans out this noise, turning any number into a super-even one.
3.  Since division by 2 on a long distance dominates multiplication with a massive advantage (**1317 vs 639**), and the super-even trap instantly cuts off half of the growth steps (**49.8%**), numbers physically do not have the spatial clearance to evade compression.

**Conclusion:** The infinity of numbers collapsed into a closed three-color grammar. Every number is doomed to lose energy on the blue axis, fly into the green compression chute, and slide down the binary framework of powers of two to the very bottom of the vortex — to the final unit.

---

## 📂 Repository Structure

All project files are located in the root directory for maximum transparency and direct access to the theoretical and computational foundation of the research:

## 📂 Repository Structure

All project files are located in the root directory for maximum transparency, providing direct access to the theoretical, computational, and visual layers of the research:

* 🌀 [README.md](README.md) — Core manifest, base 3D geometry rules, and project roadmap
* 📄 [LICENSE](LICENSE) — Project open-source license
* 📜 [WHITE_PAPER.md](WHITE_PAPER.md) — Complete popular timeline and synthesis of the independent assault (EN)
* 📘 [MANIFEST_PART2.md](MANIFEST_PART2.md) — Stage 2: Conical Compression Theorem & 1,000-digit Titan test (EN)
* 📗 [THEORY_ERGODICITY_PART3.md](THEORY_ERGODICITY_PART3.md) — Stage 3: Markovian Analytical Proof of the 1:1:1 Stationary State (EN)
* 📙 [THEORY_QUANTUM_PROJECTIONS_PART4.md](THEORY_QUANTUM_PROJECTIONS_PART4.md) — Stage 4: Quantum Cube Projections & 137.5° Matrix Rotation Theory (EN)
* 📕 [MANIFEST_PART5.md](MANIFEST_PART5.md) — Stage 5: Shannon Entropy Loss Invariant (0.138 bits/step) (EN)
* 📓 [MANIFEST_PART6.md](MANIFEST_PART6.md) — Stage 6: 2-adic Topology and the Node 20 Global Highway Hub (EN)
* 📔 [MANIFEST_PART7.md](MANIFEST_PART7.md) — Stage 7: The Avalanche Wedge Law & Non-Invertible Bit Collisions (EN)
* 🚀 [nautilus_3d_viewer_en.html](nautilus_3d_viewer_en.html) — **[LIVE DEMO]** Autonomous HTML5/Canvas 3D interactive viewer (English UI)
* 📐 [collatz_27.obj](collatz_27.obj) — 3D spatial trajectory of number 27 (111 steps, peak value 9232)
* 📐 [collatz_31.obj](collatz_31.obj) — 3D spatial trajectory of number 31 (106 steps, 5 full loops)
* 🖼️ [collatz_tornado.png](collatz_tornado.png) — Attractor render visualization / asset
* ⚙️ [simulator.py](simulator.py) — Python engine computing global retention coefficient and statistics (EN)

- 📑 [ADDENDUM_BLUE_TRAP_EN.md](./ADDENDUM_BLUE_TRAP_EN.md) — Theoretical Addendum: Proof of 2-adic memory and fractal division of the Blue Trap
- ⚙️ [simulator_blue_trap_en.py](./simulator_blue_trap_en.py) — Autonomous verification script for quantum tornado loop quantization along the Y-axis depth (English version)
- 📑 [ADDENDUM_AVALANCHE_EN.md](./ADDENDUM_AVALANCHE_EN.md) — Theoretical Addendum: Proof of bitwise entropy erasure and defense against anomalous trajectories
- ⚙️ [simulator_bit_avalanche_en.py](./simulator_bit_avalanche_en.py) — Visualisation script for the bit carry wave and avalanche entropy collapse (English version)
- 📑 [ADDENDUM_ISOMORPHISM_EN.md](./ADDENDUM_ISOMORPHISM_EN.md) — Theoretical Addendum: Proof of strict algebraic isomorphism of the 3D Nautilus attractor
- ⚙️ [simulator_isomorphism_en.py](./simulator_isomorphism_en.py) — Calculation script for 3D trajectory coordinates based on trigonometric remainder indicators (English version)





[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.20716180.svg)](https://doi.org/10.5281/zenodo.20716180)


## 📄 License
This project is distributed under the open **MIT License**. You are free to use, modify, and develop this geometric model.
