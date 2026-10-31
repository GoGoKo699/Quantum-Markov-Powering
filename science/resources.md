# Query, gate, workspace, and precision resources

The lower and upper bounds charge calls to the explicitly supplied one-step row unitary. They do not assign unit cost to an independently supplied powered row oracle.

Let $`n=\log_2N`$, $`m=\log_2M=4n`$, and define

```math
k=\lceil\sqrt N\rceil,
\qquad
q_\psi=2k+1,
\qquad
q_\pi=3q_\psi.
```

## Query account

All counts below include inverses and controlled calls. The constructive bounds are worst-case caps, with no unbounded postselection loop.

| Task | Constructive query cap | Worst-case lower bound |
|---|---:|---:|
| Prepare the stationary quantum sample | $`q_\pi`$ | $`\Omega(\sqrt N)`$ |
| Clean row preparation for the squared chain | $`q_\pi`$ | $`\Omega(\sqrt N)`$ |
| Stationary reflection | $`2q_\pi`$ | $`\Omega(\sqrt N)`$ |
| Squared-chain Szegedy reflection | $`2q_\pi`$ | $`\Omega(\sqrt N)`$ |
| Normalization-one flat-discriminant block encoding for the squared chain | $`2q_\pi`$ | $`\Omega(\sqrt N)`$ |

The table holds for the base family and the [two-state product family](early-reversibility.md). Lower bounds use error $`10^{-3}`$; the upper circuits can be compiled to any prescribed positive error without increasing these query caps.

Each supplied row call reduces to one ordinary evaluation query. Conversely, each evaluation query in the upper construction is implemented as $`U_fA^\dagger`$ and costs one row call plus known gates. All calls made during instance-dependent preprocessing are included. Precomputing only quantities determined by $`N`$, the product parameter $`T`$, and the requested accuracy uses no queries to $`f`$.

The $`\Theta(\sqrt N)`$ tightness statement is for the supplied row-unitary model. Only a lower-bound transfer is asserted for a model supplied exclusively with one-step Szegedy reflections.

## Known gates and workspace

The explicit known unitary $`A`$ and its inverse use $`O(n+m^2)`$ elementary gates, including decomposed controlled rotations, with $`O(n+m)`$ reusable ancillary qubits. This cost must be paid when simulating an evaluation query from a supplied row query.

The exact-amplification circuits use known zero-state and uniform-state reflections. Multi-controlled phase operations can be implemented using $`O(n+m)`$ elementary reversible gates and $`O(n+m)`$ clean reusable ancillas. Controlled versions preserve these polynomial bounds.

For any of the five tasks, if its query cap is $`Q=O(\sqrt N)`$, a conservative bound for the number of additional gates in the ideal known-angle model is

```math
G=O\!\left(Q(n+m)^2\right)=O(Qn^2).
```

The total quantum register width is $`O(n+m)=O(n)`$, including source and endpoint registers where required, index-erasure workspace, dummy registers for the oracle interface, amplification flags, and scratch space for controlled operations. The product family adds only a constant number of quantum bits. The parameter $`T`$ is a known classical integer, rather than a quantum input register.

The known gate parameters are uniformly computable. The prefix probabilities for $`W_\chi`$, the amplitude-dilution angle, and the two-state transition angles depend only on the stated classical parameters. They require no table indexed by the $`M`$ possible output labels and no QRAM.

## Finite gate precision

Exact known-angle gates are a query-model idealization. They are not assigned free infinite precision in the finite-gate resource statement.

Fix a finite inverse-closed universal gate set with standard efficient synthesis, and let $`\varepsilon>0`$ be the desired operator error for the complete task circuit. Synthesize each of its at most $`G`$ known elementary gates to operator error at most $`\varepsilon/G`$, after including a harmless constant margin for any decomposition overhead. Exact oracle calls remain exact in this model.

A telescoping product estimate gives

```math
\|\widehat C-C\|
\le
\sum_{j=1}^{G}\|\widehat G_j-G_j\|
\le\varepsilon.
```

The estimate applies to complete unitaries, so it is sufficient for clean row isometries, clean-ancilla reflections, and block encodings. It also bounds the trace distance of their state outputs.

The final rotation descriptions therefore require

```math
p=O\!\left(\log\frac G\varepsilon\right)
=
O\!\left(\log Q+\log n+\log\frac1\varepsilon\right)
```

bits of accuracy. Classical evaluation of the angle formulas can use additional $`O(n+\log T)`$ guard bits. Its cost is polynomial in these bit lengths per required gate parameter.

For example, [Solovay–Kitaev synthesis](../references/related-work.md#gate-synthesis) supplies a finite-gate implementation with

```math
O\!\left(
G\,\operatorname{poly}\!\left(\log\frac G\varepsilon\right)
\right)
```

nonoracle gates and the same $`Q`$ queries. More efficient single-qubit compilers can improve this gate overhead without changing the query statement. Known angles can be compiled classically, so their precision descriptions do not require an additional quantum data-loading memory.

For fixed task error and $`Q=\Theta(\sqrt N)`$, $`\log Q=\Theta(n)`$. The displayed uniform error guarantee uses per-gate accuracy $`O(\varepsilon/G)`$, whose bit budget grows with $`n`$. This is a sufficient precision budget accounting for accumulation over the exponential-in-$`n`$ query circuit.

If the supplied row oracle is itself implemented approximately, an additional per-call error $`\zeta`$ contributes at most $`Q\zeta`$ to the same hybrid estimate. Keeping the total error at $`\varepsilon`$ requires an appropriate budget, for example $`\zeta=O(\varepsilon/Q)`$. This describes an implementation requirement; the lower-bound oracle model grants exact access.

## Lower-bound reduction resources

The reductions use at most $`32`$ fresh attempts, each invoking the proposed primitive once. The slowest accepted branch has probability greater than $`0.187`$ and conditional image-state fidelity greater than $`63/64-0.0054`$. The bounded repetition gives final fidelity greater than $`0.977`$ and at most $`32Q`$ evaluation queries.

The added measurements and state preparations are known operations on $`O(n+m)`$ qubits per attempt. This is a bounded-query algorithm, not an expected-query or unbounded-postselection reduction. The exact constants and the connection to the source's squared-fidelity error convention are proved in [the lower bounds](lower-bounds.md#bounded-repetition-and-the-sources-error-convention).

## Classical and coherent resources answer different tasks

A classical stationary sample uses at most one evaluation query for both constructed families, by starting the hidden coordinate uniformly and sampling the known slow bit uniformly. A coherent purification of that classical sampling circuit is equally cheap if its history registers may remain entangled with the endpoint.

The hard task requires a designated endpoint register in the pure square-root state, or one of the stated operators. Scalar expectation-estimation algorithms can sometimes use the cheap purification directly. No conclusion about their complexity follows merely from the cost of cleaning the endpoint state.

