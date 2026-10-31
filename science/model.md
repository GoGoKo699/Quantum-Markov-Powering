# Model and theorem

A stochastic transition and a clean quantum transition are different computational resources. A classical two-step transition may be generated while retaining the intermediate state. A clean quantum transition must combine all paths ending at the same endpoint with their correct square-root amplitudes.

We exhibit strictly positive Markov chains for which this distinction has a tight query cost. The chain mixes exactly in two steps, and its one-step clean row oracle uses one function evaluation. Nevertheless, clean access to its square, the corresponding Szegedy reflection, and the stationary coherent state require order $`\sqrt N`$ one-step queries. The lower bound is a reduction from [noncoherent index erasure](../references/related-work.md#index-erasure). The new statement concerns the cost of composing the Markov access primitive; the index-erasure lower bound itself is inherited.

The [construction](construction.md), [lower bounds](lower-bounds.md), and [matching upper bounds](upper-bounds.md) give the complete argument. The [resource account](resources.md) includes finite gate precision. A [two-state product](early-reversibility.md) places the obstruction in the regime where exact reversibility appears long before worst-case mixing.

## Notation and input family

For powers of two $`N=2^n\ge4`$ and $`M=N^4=2^m`$, identify $`[N]`$ and $`[M]`$ with binary strings of lengths $`n`$ and $`m=4n`$. Here $`[L]=\{0,\ldots,L-1\}`$. An unknown injection $`f:[N]\to[M]`$ is accessed through the standard evaluation oracle

```math
O_f|x,w\rangle=|x,w\mathbin{\oplus}f(x)\rangle.
```

For a probability distribution $`\eta`$, its quantum sample is

```math
|\eta\rangle=\sum_s\sqrt{\eta(s)}\,|s\rangle,
\qquad
|u_L\rangle=L^{-1/2}\sum_{s\in[L]}|s\rangle.
```

Distributions are row vectors, and Markov matrices are row stochastic. The chain state space is $`\mathcal X=[N]\times[M]`$. Its kernel is

```math
K_x(w)=\frac12\mathbf1_{\{w=f(x)\}}+\frac1{2M},
\qquad
P_f((x,y),(z,w))=\frac{K_x(w)}N.
```

We use $`\Pi_f=\mathbf1\pi_f`$ for the classical rank-one stationary kernel. This is distinct from the quantum projector $`|\pi_f\rangle\langle\pi_f|`$.

## Supplied oracle and charged queries

The input is a specified full unitary $`U_f`$ on a source register and an endpoint register, not merely a promise about some of its columns. Its construction is given in [the full unitary completion](construction.md#the-full-unitary-completion). It satisfies

```math
U_f|x,y\rangle|0,0\rangle
=
|x,y\rangle
\sum_{z,w}\sqrt{P_f((x,y),(z,w))}\,|z,w\rangle.
```

One invocation of $`U_f`$, $`U_f^\dagger`$, or a controlled version costs one row-oracle query. Known gates, classical precomputation, workspace, and gate-synthesis accuracy are accounted for separately. The explicit completion uses one $`O_f`$ query, and conversely $`O_f`$ is obtained from one $`U_f`$ query and known gates. Controlled evaluation also uses one ordinary evaluation query with an extra invariant target register. Thus the lower bound uses the ordinary evaluation-query model, without a hidden strengthened oracle.

Algorithms may use arbitrary computation independent of $`f`$, ancillary registers, intermediate measurements, and adaptive control. A query budget bounds the maximum number of oracle calls in any branch. The initial states and advice are independent of $`f`$. No stochastic time-reversal oracle, powered row oracle, stationary state, or data structure containing the image of $`f`$ is included in the input.

Tight upper and lower bounds are stated in this supplied $`U_f,U_f^\dagger`$ model. A lower bound also transfers to algorithms supplied only the one-step Szegedy reflection, since that reflection can be implemented with two row-oracle calls. We do not claim a matching upper bound in the reflection-only model.

## Quantum primitives and error conventions

The clean row isometry of a kernel $`P`$ and its Szegedy row-subspace reflection are

```math
V_P|s\rangle=|s\rangle|P(s,\cdot)\rangle,
\qquad
R_P=2V_PV_P^\dagger-I
=
2\sum_s|s\rangle\langle s|
\otimes|P(s,\cdot)\rangle\langle P(s,\cdot)|-I.
```

The flat discriminant is

```math
D(P)_{st}=\sqrt{P(s,t)P(t,s)}.
```

If $`S`$ swaps the two state registers, then $`D(P)=V_P^\dagger S V_P`$. In particular, it is a real symmetric contraction.

For density operators, trace distance means $`T(\rho,\sigma)=\frac12\|\rho-\sigma\|_1`$. Fidelity to a pure target means the squared quantity $`F_\psi(\rho)=\langle\psi|\rho|\psi\rangle`$.

A state-preparation algorithm succeeds to error $`\delta`$ when its designated output register has trace distance at most $`\delta`$ from the target projector. All other output registers may be arbitrary and may depend on $`f`$.

A clean row implementation approximates the row isometry uniformly over superpositions of source states, with all auxiliary registers initially and finally zero, to vector-operator error at most $`\delta`$. Only this input subspace is prescribed; the algorithm may choose any unitary completion.

For a unitary target $`R`$, a clean-ancilla implementation $`\widehat R`$ has error at most $`\delta`$ when

```math
\|\widehat R J-JR\|\le\delta,
\qquad
J|\varphi\rangle=|\varphi\rangle|0^a\rangle.
```

This is a uniform operator bound on the initialized-ancilla subspace and includes any leakage from that subspace. It also holds for inputs entangled with an external reference. With no auxiliary registers it is ordinary operator-norm error.

A normalization-one block encoding of $`A`$ is a unitary $`\mathcal B`$ with a designated zero-ancilla block

```math
B=(\langle0^a|\otimes I)\mathcal B(|0^a\rangle\otimes I),
\qquad
\|B-A\|\le\delta.
```

Normalization one fixes the signal amplitude used in the lower-bound reduction.

## Main theorem

For the explicit oracle family above, the following statements hold.

1. The chain is strictly positive and nonreversible, and $`P_f^2=\Pi_f`$. Its unique stationary distribution is
   $`\,\pi_f(z,w)=N^{-1}[1/(2M)+\mathbf1_{\{w\in\operatorname{im}f\}}/(2N)]`$.
2. A known uniform coherent state has squared overlap at least $`1/2`$ with $`|\pi_f\rangle`$. The corresponding uniform classical distribution is pointwise bounded by $`2\pi_f`$.
3. At error $`\delta=10^{-3}`$, each of the following tasks has worst-case query complexity $`\Theta(\sqrt N)`$: preparing $`|\pi_f\rangle`$; clean row preparation for $`P_f^2`$; implementing $`R_{P_f^2}`$; implementing $`2|\pi_f\rangle\langle\pi_f|-I`$; and block encoding $`D(P_f^2)`$ with normalization one.
4. The powered flat discriminant is exactly
   $`D(P_f^2)=|\pi_f\rangle\langle\pi_f|`$.
   Its only nonzero eigenvalue is $`1`$.

The lower bound holds for every fixed error at most $`10^{-3}`$. The upper construction is exact with ideal known-angle gates; finite-gate implementations attain any desired positive error with the precision cost in [resources](resources.md).

The theorem concerns clean quantum primitives. A classical stationary sample is available with at most one evaluation of $`f`$, including from a known uniform starting distribution. The construction therefore does not assert a lower bound for ordinary endpoint sampling or for scalar expectation estimation using a coherent circuit that retains its sampling history.

