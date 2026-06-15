# Collatz Conjecture: 3D Attractor & Ternary Logic Model
![Collatz 3D Tornado Model](collatz_tornado.png)

**Project Author:** Kirill Maksimov (GitHub: @mrDarkuck)  
**Disclaimer:** I am completely outside the world of advanced mathematics or professional academia. This project represents a look at a 90-year-old puzzle from the perspective of systems logic, binary code, and 3D geometry. It is an outsider's attempt to visualize chaos and turn dry equations into a tangible, physical model.


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
*   `simulator.py` — an interactive Python script for analyzing any ultra-large numbers.
*   `models/collatz_27.obj` — 3D trajectory ("tornado") of the number 27 (111 steps, 5 full loops).
*   `models/collatz_31.obj` — 3D trajectory ("spring") of the number 31 (106 steps, 5 full loops).

## 📄 License
This project is distributed under the open **MIT License**. You are free to use, modify, and develop this geometric model.
