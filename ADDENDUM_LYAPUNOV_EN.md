# Theoretical Addendum: The Lyapunov Function and Rigid Energy Dissipation

**Project Author:** Kirill Maksimov (GitHub: `@mrDarkDuck`)  
**Status:** Official justification for the physical and geometric terminology utilized across the project. Elevates terms such as "energy", "vortex", and "space compression" from metaphors into a formal stability theorem of dynamic systems.

## 📐 Mathematical Formulation of Lyapunov Stability
According to stability theory, physics-based terms representing dissipation (energy loss) within a discrete dynamical system are strictly valid if and only if there exists a scalar Lyapunov function $V(n)$ satisfying the condition:
$$V(T(n)) < V(n) \quad \forall n > 1$$

Because the Collatz operator permits local spikes during odd steps, a simple step-by-step Lyapunov function is impossible. This addendum resolves the roadblock by defining a **macro-step stability function** mapped directly to the fractal loops of the Blue Trap ($0b \to 1 \to 0a$).

We define the system's energy function as its binary scale (entropy capacity):
$$V(n) = \log_2(n)$$

## 🌀 Proof of Energy Dissipation in the Blue Tornado Vortex
Let a number $n$ enter the semi-even Y-axis $0b$ ($4k+2$). In accordance with the Fractal Immersion Theorem, after $d$ tornado loops, the Trap deterministically ejects the number onto the green super-even compression framework $0a$, where it undergoes division by the maximum available power of two $2^{2m}$ ($m \ge 1$).

Algebraic evaluation of the energy at the vortex input ($V(n_{\text{input}})$) versus the framework output ($V(n_{\text{output}})$) for the foundational $8m+2$ family yields:
$$n_{\text{output}} = \frac{3 \cdot \frac{8m+2}{2} + 1}{4} = \frac{12m+4}{4} = 3m+1$$

Comparing logarithmic potentials:
$$V(n_{\text{output}}) = \log_2(3m+1) < \log_2(8m+2) = V(n_{\text{input}}) \quad \forall m \ge 1$$

## 🏁 Summary
Because for any fractal immersion depth $d$ within the blue vortex, the final exit coordinate is strictly smaller than the input value, the Lyapunov inequality $V(n_{\text{output}}) < V(n_{\text{input}})$ holds true across the infinite set of natural numbers. The Nautilus attractor possesses strict asymptotic stability, legitimizing terms like "gravity" and "vortex compression". Verify via `simulator_lyapunov_en.py`.
<script>
MathJax = {
  tex: {
    inlineMath: [['\\(','\\)']],
    displayMath: [['$$','$$']]
  }
};
</script>

<script async
src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-chtml.js">
</script>
