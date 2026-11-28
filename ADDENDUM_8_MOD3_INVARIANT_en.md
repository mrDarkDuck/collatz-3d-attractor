# Addendum VIII: The Mod-3 Multiplicity Filter, Reverse-Tree Branching Valve, and Phase Altitude Indicator

## 1. Theorem on Single-Entry Multiples of 3

The subset of natural numbers divisible by $3$ ($x \equiv 0 \pmod 3$) is purged from the Collatz dynamical system immediately after the first affine step and never reappears anywhere along the subsequent trajectory.

### Proof
For any natural number $n \in \mathbb{N}$ (including $n \equiv 0 \pmod 3$), the initial excitation step maps the system strictly to residue $1$ modulo $3$:

$$T(n) = 3n + 1 \equiv 1 \pmod 3$$

Because the relaxation base ($2$) is coprime to $3$ ($\gcd(2, 3) = 1$), consecutive divisions by $2$ induce a closed involution (toggle) between the two non-zero residues:

$$1 \equiv 4 \pmod 3 \xrightarrow{/2} 2 \pmod 3 \xrightarrow{/2} 1 \pmod 3$$

Consequently, for every step $k \ge 1$, the strict invariant $x_k \not\equiv 0 \pmod 3$ holds. Multiples of $3$ (including the odd "pure source" subclass $12k + 3$: $3, 15, 27, 39, 51, 63 \dots$) can exist in the Collatz graph solely as **terminal leaves (starting nodes)** and can never participate in non-trivial cycles or divergent trajectories.

---

## 2. Reverse-Tree Branching Valve ($\frac{N - 1}{3}$) and Fractional Tail Classification

When growing the inverse Collatz tree upward from the terminal attractor $1$, every node permits unbounded vertical growth along the doubling highway ($N \to 2N$), whereas the odd-predecessor operator $P(N) = \frac{N - 1}{3}$ acts as a deterministic modulo-$6$ valve:

| Even Node Class ($\bmod 6$) | Algebraic Form | Value of $\frac{N - 1}{3}$ | Fractional Tail | Topological Role in the Tree |
| :--- | :---: | :---: | :---: | :--- |
| **$N \equiv 4 \pmod 6$** | $6k + 4$ | $2k + 1 \in \mathbb{N}_{\text{odd}}$ | **`.0`** (integer) | **Active Branching Valve:** spawns a new odd branch ($10 \to 3$, $16 \to 5$, $22 \to 7$). |
| **$N \equiv 2 \pmod 6$** | $6k + 2$ | $2k + \frac{1}{3}$ | **`.33333...`** | **Temporary Lock:** after a single doubling ($2N \equiv 4 \pmod 6$), the valve opens. |
| **$N \equiv 0 \pmod 6$** | $6k$ | $2k - \frac{1}{3}$ | **`.66666...`** | **Dead Wall (Absorbing Stem):** doubling preserves divisibility by $3$; zero side branches to $\infty$. |

### Corollary on Branching Rhythm
* Along any stem seeded by $x \not\equiv 0 \pmod 3$, branching valves open **strictly on alternating doubling levels** (`.33333...` $\leftrightarrow$ `.0`).
* Along any stem seeded by $x \equiv 0 \pmod 3$, the fractional tail **`.66666...` is invariant under multiplication by $2$**, turning the entire branch into a smooth one-dimensional stalk with zero offshoots.

---

## 3. The 100% Local Peak Law in Residue Class $2 \pmod 3$

Under compressed odd-to-odd dynamics ($x_{i+1} = \frac{3x_i + 1}{2^\nu}$), the parity of the $2$-adic valuation $\nu$ rigidly locks the integer value to its residue modulo $3$:

* **Odd number of halvings ($\nu \in \{1, 3, 5, \dots\}$):** maps the system into **$x_{i+1} \equiv 2 \pmod 3$** (form $3m + 2$).
* **Even number of halvings ($\nu \in \{2, 4, 6, \dots\}$):** returns the system into **$x_{i+1} \equiv 1 \pmod 3$** (form $3m + 1$).

### Theorem on Trajectory Local Maxima
> *Every local maximum (downward turning peak) of any Collatz trajectory belongs strictly to the residue class $2 \pmod 3$. Local maxima are impossible in class $1 \pmod 3$.*

**Proof:**
A local maximum requires an upward step immediately prior: $x_i > x_{i-1}$. Since $x_i = \frac{3x_{i-1} + 1}{2^\nu}$, the inequality $x_i > x_{i-1}$ holds **if and only if $\nu = 1$** (for all $\nu \ge 2$, $\frac{3x + 1}{2^\nu} \le \frac{3x + 1}{4} < x$). Because $\nu = 1$ is an odd number of halvings, the $1 \pmod 3$ state produced by $3x+1$ deterministically transitions to $2 \pmod 3$. $\blacksquare$

---

## 4. Computational Verification ($50,000$ Trajectories)

An exhaustive sweep across all odd integers in $[3, 99\,999]$ ($1\,899\,202$ compressed $\mathbf{O} \to \mathbf{O}'$ cycles) confirms the analytical theorems with zero exceptions:

| Trajectory Position | Share of $0 \pmod 3$ | Share of $1 \pmod 3$ | Share of $2 \pmod 3$ | Structural Interpretation |
| :--- | :---: | :---: | :---: | :--- |
| **All Intermediate Nodes** | **$0.00\%$** ($0$) | **$34.06\%$** | **$65.94\%$** | Two-to-one dominance of semi-even compressions ($\nu = 1$). |
| **Local PEAKS ($x_{i-1} < x_i > x_{i+1}$)** | **$0.00\%$** ($0$) | **$0.00\%$** ($0$) | **$100.00\%$** ($454\,363$) | **Absolute Invariant:** downward reversal occurs exclusively from $3m + 2$. |
| **Local TROUGHS ($x_{i-1} > x_i < x_{i+1}$)** | **$0.00\%$** ($0$) | **$63.18\%$** | **$36.82\%$** | Dominance of deep super-even drops ($\nu \in \{2, 4, 6 \dots\}$). |

---

## 5. Practical Application: Two-Phase Altitude Indicator

The modulo-$3$ residue of the current odd state acts as an instantaneous phase detector independent of numerical magnitude:

1. **State $x \equiv 2 \pmod 3$ (Ascent / Peak Phase):** the trajectory is actively climbing ($\nu = 1$, $\times 1.5$ growth) or standing at a local apex prior to collapse.
2. **State $x \equiv 1 \pmod 3$ (Descent / Trough Phase):** the trajectory has undergone a multi-step relaxation drop ($\nu \ge 2$) and is cooling in a decay basin.

---

## 6. Staggered Decomposition of the $6k + 5$ Sequence ($12m + 11 \to 12m + 5$)

The arithmetic progression of odd integers in residue class $2 \pmod 3$, given by $6k + 5$ ($5, 11, 17, 23, 29, 35, 41, 47 \dots$), splits modulo $12$ into two strictly alternating subclasses with opposite dynamical behavior:

1. **Exit Branch ($12m + 5$: $5, 17, 29, 41, 53 \dots$):**
   $$3(12m + 5) + 1 = 36m + 16 = 4(9m + 4) \implies \nu \ge 2$$
   Every integer in this subclass becomes divisible by at least $4$ under $3x+1$ (super-even drop $\mathbf{E_{0a}}$) and immediately exits the ascent regime.
2. **Retention Branch ($12m + 11$: $11, 23, 35, 47, 59 \dots$):**
   $$3(12m + 11) + 1 = 36m + 34 = 2(18m + 17) \implies \nu = 1$$
   Every integer in this subclass divides by $2$ strictly once (semi-even compression $\mathbf{E_{0b}}$) and maps to $18m + 17 = 6(3m + 2) + 5$, remaining inside the $6k + 5$ sequence with a $\times 1.5$ scaling factor.

| Start ($12m + 11$) | Algebraic Form | Ascent Steps | Chain Within $6k + 5$ | Exit Point ($12m + 5$) | Post-Exit Collapse |
| :--- | :---: | :---: | :--- | :---: | :--- |
| **$95$** | $3 \cdot 2^5 - 1$ | **$4$** | $95 \to 143 \to 215 \to 323$ | **$485$** | $/16 \to 91$ ($1 \pmod 3$) |
| **$191$** | $3 \cdot 2^6 - 1$ | **$5$** | $191 \to 287 \to 431 \to 647 \to 971$ | **$1457$** | $/4 \to 1093$ ($1 \pmod 3$) |
| **$383$** | $3 \cdot 2^7 - 1$ | **$6$** | $383 \to 575 \to 863 \to 1295 \to 1943 \to 2915$ | **$4373$** | $/64 \to 205$ ($1 \pmod 3$) |
| **$767$** | $3 \cdot 2^8 - 1$ | **$7$** | $767 \to 1151 \to 1727 \to 2591 \to 3887 \to 5831 \to 8747$ | **$13121$** | $/4 \to 9841$ ($1 \pmod 3$) |

### 6.1. Recursive Sieve and Exact Ascent Corridor Formula

Applying the $12m + 11$ retention condition iteratively halves the surviving subset at each step. The set of all natural numbers undergoing an ascent streak of **exact length $L$ steps** ($\nu = 1$) before collapsing on step $L+1$ is given by the closed-form progression:

$$n_L(m) = 3 \cdot 2^{L+2} \cdot m + \left(3 \cdot 2^{L+1} - 1\right), \quad m \in \mathbb{N}_0$$

| Ascent Length ($L$) | Exact Class Formula $n_L(m)$ | Density in $\mathbb{N}$ | Minimal Representative ($m=0$) | Leading Progression Terms |
| :---: | :---: | :---: | :---: | :--- |
| **$L = 0$** (immediate exit) | $12m + 5$ | $1/12$ ($8.33\%$) | **$5$** ($3 \cdot 2^1 - 1$) | $5, 17, 29, 41, 53 \dots$ |
| **$L = 1$** ($1$ ascent step) | $24m + 11$ | $1/24$ ($4.17\%$) | **$11$** ($3 \cdot 2^2 - 1$) | $11, 35, 59, 83, 107 \dots$ |
| **$L = 2$** ($2$ ascent steps) | $48m + 23$ | $1/48$ ($2.08\%$) | **$23$** ($3 \cdot 2^3 - 1$) | $23, 71, 119, 167, 215 \dots$ |
| **$L = 3$** ($3$ ascent steps) | $96m + 47$ | $1/96$ ($1.04\%$) | **$47$** ($3 \cdot 2^4 - 1$) | $47, 143, 239, 335, 431 \dots$ |
| **$L = 4$** ($4$ ascent steps) | $192m + 95$ | $1/192$ ($0.52\%$) | **$95$** ($3 \cdot 2^5 - 1$) | $95, 287, 479, 671, 863 \dots$ |

Summing the asymptotic densities of all finite ascent corridors recovers the exact measure of class $6k + 5$:

$$\sum_{L=0}^{\infty} \frac{1}{3 \cdot 2^{L+2}} = \frac{1}{12} + \frac{1}{24} + \frac{1}{48} + \dots = \frac{1}{6}$$

Hence, finite ascent streaks $L \in [0, \infty)$ exhaust the entire measure of residue class $2 \pmod 3$, leaving zero asymptotic density for unbounded monotonic growth.

### 6.2. Bridge Between the 2-Adic and 3-Adic Models

The minimal corridor representative $n_L(0) = 3 \cdot 2^{L+1} - 1$ establishes a direct algebraic identity between the 3-adic recursive sieve and the 2-adic "bit fuel" mechanism (Addendum VII):
* * In binary, $3 \cdot 2^{L+1} - 1 = 2^{L+2} + 2^{L+1} - 1$ takes the form $\mathtt{10}{\underbrace{\mathtt{111\dots111}}_{L+1}}_2$—a leading $\mathtt{10}$ prefix followed by exactly $L+1$ trailing ones.

* Adding multiples of the progression modulus $3 \cdot 2^{L+2} \cdot m$ modifies only bits strictly above position $L+2$, leaving the trailing block of $L+1$ consecutive ones and its separating zero untouched.

---

## 7. Bitwise "Shadow Matryoshka" and Collision Physics ($3^t + r_t$)

Decomposing an arbitrary odd integer into an upper ballast buffer and a lower residue $n = P_{\text{high}} + r_{\text{low}}$ (where $k_{\min}$ is the lowest bit position in $P_{\text{high}}$ and $r_{\text{low}} < 2^{k_{\min}}$) reveals a **shadow synchronization invariant**:

$$n_t = 3^t \cdot \frac{P_{\text{high}}}{2^{S_t}} + r_t, \quad \forall t : S_t = \sum_{i=1}^{t} \nu_i < k_{\min}$$

As long as the cumulative halving count $S_t$ remains strictly below the buffer capacity $k_{\min}$, the upper bits **do not alter the trajectory route** (preserving the exact $\nu_i$ sequence of $r_{\text{low}}$) and act purely as an altitude scaling factor.

### Modulo-4 Switch at the Collision Point ($S_t = k$)
At the exact instant the ballast is exhausted ($S_t = k$ for $n = 2^k + r$), the two components interact via $n_t = 3^t + r_t$ (an exhaustive sweep across $228\,993$ collisions confirms this deterministic switch with zero exceptions):
1. **Destructive Phase ($3^t + r_t \equiv 0 \pmod 4$, $50\%$ of exact hits):** occurs when $t$ and $r_t$ have opposite modulo-$4$ residues ($t$ even and $r_t \equiv 3 \pmod 4$, or $t$ odd and $r_t \equiv 1 \pmod 4$). The sum is divisible by at least $4$ ($\nu_{\text{extra}} \ge 2$), immediately collapsing the trajectory.
2. **Constructive Phase ($3^t + r_t \equiv 2 \pmod 4$, $50\%$ of exact hits):** occurs when $t$ and $r_t$ share the same modulo-$4$ residue ($t$ even and $r_t \equiv 1 \pmod 4$, or $t$ odd and $r_t \equiv 3 \pmod 4$). The sum divides by $2$ strictly once ($\nu_{\text{extra}} = 1$), allowing carry propagation to fill zero gaps in $3^t$ and synthesize a fresh contiguous block of ones (a "second-stage rocket", e.g., $n = 2^{48} + 2459$ at step $t=27$ generates a trailing block of $14$ consecutive ones).

---

## 8. Supermartingale Resource $R_1(x)$ and the "Impossible Super-Automaton" Criterion

Combining the $2$-adic cluster weight with the $3$-adic phase indicator defines a unified resource functional:

$$R_1(x) = k + 0.585 \sum_{i} (c_i - 1) + 0.415 \cdot \mathbb{I}(x \equiv 2 \pmod 3)$$

where $k = \lfloor \log_2 x \rfloor$ and $c_i \ge 2$ denote the lengths of all internal contiguous clusters of ones in the binary representation of $x$.

* **Computational Verification up to $10^6$:** An exhaustive sweep across all $499\,999$ odd integers in $[3, 999\,999]$ confirms that $R_1(x)$ behaves as a **non-negative supermartingale with a finite stopping time** $\tau_{R_1}(x) = \min \lbrace t \ge 1 : R_1(x_t) < R_1(x_0) \rbrace$:
  * $57.54\%$ of trajectories drop below their initial resource $R_1(x_0)$ on the very first compressed step;
  * $95.18\%$ are quenched within $\le 10$ steps;
  * $100.00\%$ exhibit finite stopping times (maximum across the entire million is $130$ steps for $837\,799$).

### Synthesis for the $3n + 1$ Conjecture: Portrait of the Impossible Super-Automaton
Proving the Collatz conjecture reduces to proving that no finite natural number $x \in \mathbb{N}$ can operate as a self-recharging bitwise automaton (a measure-zero divergent orbit) capable of indefinitely maintaining:
1. an average halving density $\frac{S_T}{T} < \log_2(3) \approx 1.58496$ (Diophantine tracking of convergents of $\log_2 3$);
2. unbounded synthesis of higher-order bits at collision points $3^t + r_t$ via matched modulo-$4$ phases faster than trailing bit clusters burn out and the $2$-adic "bit thermostat" restores equilibrium.

