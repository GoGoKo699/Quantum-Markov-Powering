# Exact reversibility before slow mixing

The base chain has already mixed when its square becomes reversible. A two-state product separates those times while preserving the coherent access obstruction.

The construction is deliberately explicit: a known slow reversible factor is tensored with the hard two-step chain. It tests whether a claimed sufficient spectral condition actually controls the cost of synthesizing the required quantum primitive. It is not a hard classical sampling instance; its stationary distribution can still be sampled with one function evaluation.

## The product chain

Let $`T\ge4`$ be a known integer and define

```math
Q_T=
\begin{pmatrix}
1-1/T&1/T\\
1/T&1-1/T
\end{pmatrix},
\qquad
\lambda=1-\frac2T.
```

The kernel is symmetric, has uniform stationary distribution $`u_2`$, and has eigenvalues $`1`$ and $`\lambda`$. Set

```math
\widetilde P_f=P_f\otimes Q_T,
\qquad
\widetilde\pi_f=\pi_f\otimes u_2.
```

Every entry is strictly positive. The state space has $`2NM`$ elements.

Because $`P_f^t=\Pi_f`$ for every $`t\ge2`$,

```math
\widetilde P_f^{\,t}=\Pi_f\otimes Q_T^t
\qquad(t\ge2).
```

For any starting state $`(x,y,b)`$,

```math
d_{\rm TV}\!\left(
\widetilde P_f^{\,t}((x,y,b),\cdot),
\widetilde\pi_f
\right)
=
\frac{\lambda^t}{2}
\qquad(t\ge2).
```

At time one, the hidden coordinate alone has distance

```math
d_{\rm TV}(K_x,q_f)
=\frac12\left(1-\frac1N\right)
\ge\frac38.
```

Marginalization cannot increase total variation, so no source has reached distance $`1/4`$ at time one. It follows that

```math
\tau_{\rm mix}(1/4)
=
\max\!\left\{
2,\,
\left\lceil
\frac{\log2}{-\log(1-2/T)}
\right\rceil
\right\}
=
\Theta(T).
```

For $`0<\epsilon\le1/4`$, the exact expression replaces $`\log2`$ by $`\log(1/(2\epsilon))`$. The maximum with two is necessary, including at $`T=4`$.

## The powered spectrum is fully favorable

The squared chain is

```math
\widetilde P_f^{\,2}=\Pi_f\otimes Q_T^2.
```

Both factors are reversible with respect to their stationary distributions, so the product is exactly reversible with respect to $`\widetilde\pi_f`$. Its flat discriminant is

```math
D(\widetilde P_f^{\,2})
=
|\pi_f\rangle\langle\pi_f|\otimes Q_T^2.
```

It is strictly positive entrywise, hence primitive. Its only nonzero eigenvalues are $`1`$ and $`\lambda^2`$; its normalized Perron eigenvector is exactly $`|\widetilde\pi_f\rangle`$. The geometric reversibilization of an already reversible kernel is the kernel itself, giving absolute spectral gap

```math
\gamma_{\rm geo}
=
1-\lambda^2
=
\frac{4(T-1)}{T^2}.
```

In particular,

```math
1-
\langle\widetilde\pi_f|
D(\widetilde P_f^{\,2})
|\widetilde\pi_f\rangle
=0.
```

Thus any reversibility-on-stationary-average condition that accepts exact reversibility is satisfied by power two. This statement needs no interpretation of an informal small-error threshold.

The uniform quantum state $`|u_N\rangle|u_M\rangle|u_2\rangle`$ retains squared target overlap $`\alpha^2\ge1/2`$. Its underlying classical distribution remains pointwise dominated by $`2\widetilde\pi_f`$.

## The supplied one-step oracle still costs one query

Use a source $`(x,y,b)`$ and endpoint $`(z,w,c)`$. Let $`W_T`$ prepare

```math
W_T|0\rangle
=
\sqrt{1-1/T}|0\rangle+\sqrt{1/T}|1\rangle,
\qquad
V_T=\mathrm{CNOT}_{b\to c}W_{T,c}.
```

Then the full unitary

```math
\widetilde U_f
=
O_f^{X,W}
\left(
H_Z^{\otimes n}\otimes W_{\chi,W}\otimes V_T
\right)
```

prepares the correct product row. It uses one evaluation query. The parenthesized operation is known and invertible, so the lifted row oracle is again query equivalent to $`O_f`$, including inverse and controlled calls. The known two-state rotations are included in the [gate and precision account](resources.md).

## The powered Szegedy reflection is hard directly

Fix any source $`s=(x,y,b)`$, and prepare the known endpoint-bit state

```math
|r_b\rangle=|Q_T^2(b,\cdot)\rangle.
```

The corresponding powered row is $`|\pi_f\rangle|r_b\rangle`$. For every hidden-coordinate vector $`|v\rangle`$,

```math
R_{\widetilde P_f^{\,2}}
\bigl(|s\rangle|v\rangle|r_b\rangle\bigr)
=
|s\rangle
R_{\pi_f}|v\rangle
|r_b\rangle.
```

Preparing and undoing the fixed source and $`|r_b\rangle`$ uses known gates only. An approximate implementation of the powered Szegedy reflection therefore gives a stationary-reflection implementation for the base family with the same initialized-ancilla operator error.

The [reflection reduction](lower-bounds.md#stationary-reflection) then proves an $`\Omega(\sqrt N)`$ lower bound. The argument does not assume a particular way of building the powered reflection from a row oracle, and does not require control of the synthesized reflection.

## All five costs persist

The other reductions use equally direct restrictions.

- A stationary quantum sample gives $`|\pi_f\rangle`$ by discarding the known two-state factor.
- A clean powered row gives the same hidden state, since its endpoint-bit factor is a known $`|r_b\rangle`$.
- Restricting $`2|\widetilde\pi_f\rangle\langle\widetilde\pi_f|-I`$ to a slow register in $`|u_2\rangle`$ yields $`R_{\pi_f}`$.
- Compressing a block encoding of $`D(\widetilde P_f^{\,2})`$ between known $`|u_2\rangle`$ states gives a normalization-one block encoding of $`|\pi_f\rangle\langle\pi_f|`$, because $`Q_T^2|u_2\rangle=|u_2\rangle`$.

These known embeddings and compressions do not increase the stated error. The lower-bound constants therefore remain unchanged.

For upper bounds, append the appropriate known one-qubit state preparation to $`W_\pi`$, controlled by the retained source bit when constructing a row. Reflection conjugation and compressed swaps then give the remaining operators exactly as in [the constructive upper bounds](upper-bounds.md#obtaining-the-five-primitives). All five tasks have $`\Theta(\sqrt N)`$ query complexity in the supplied row-unitary model.

## Polynomial mixing with exponentially costly coherent powers

Choose

```math
N=2^n,
\qquad
M=2^{4n},
\qquad
T=n,
\qquad
n\ge4.
```

The state register has $`5n+1`$ qubits. The chain mixes in $`\Theta(n)`$ steps from the worst starting state, becomes exactly reversible after at most two steps, and has powered geometric gap

```math
\gamma_{\rm geo}=\frac{4(n-1)}{n^2}.
```

The five coherent tasks nevertheless require and admit $`\Theta(2^{n/2})`$ one-step row queries at the stated fixed accuracy.

A polynomial transformation whose cost is expressed in supplied powered-walk calls remains a valid conditional result. The product family shows why replacing each of those calls by a constant number of original one-step calls requires a separate implementation theorem: the required powered primitive itself can cost exponentially many original queries. The distinction and its relation to [nonreversible spectral methods](../references/related-work.md#nonreversible-spectral-methods) are an access-model issue, not a failure of the spectral transformation under its stated powered access.

## Scope of the product construction

The slow factor is independent and known. Its purpose is to make the spectral condition of early reversibility hold while leaving the coherent preparation task unchanged. This supplies a tensor-product test of whether spectral data alone imply an end-to-end oracle guarantee.

It does not make the best classical stationary sampler slow. Starting the hidden source uniformly and the slow bit uniformly produces a stationary classical sample in one transition. Nor does it obstruct a coherent purification that retains this sampling history. The established separation concerns clean powered quantum access and stationary quantum operators, with all of their input and accuracy requirements stated explicitly.

