# A strictly positive chain that mixes in two steps

The family is built so that a transition forgets one coordinate while writing the image of the other. A second classical transition therefore removes all dependence on the starting state. The remaining stationary quantum sample contains a uniform superposition of the image of the unknown injection.

Throughout this page, $`N=2^n\ge4`$, $`M=N^4`$, and $`f:[N]\to[M]`$ is injective. Definitions and error conventions are in the [model](model.md).

## Exact mixing and stationary distribution

Define

```math
K_x(w)=\frac12\mathbf1_{\{w=f(x)\}}+\frac1{2M},
\qquad
P_f((x,y),(z,w))=\frac{K_x(w)}N.
```

The coordinate $`z`$ is fresh and uniform. The coordinate $`w`$ is a mixture of $`f(x)`$ and a uniform sample; the old $`y`$ is unused. Every transition probability is at least $`1/(2NM)`$, so the chain is irreducible and aperiodic.

For any source and endpoint,

```math
\begin{aligned}
P_f^2((x,y),(z,w))
&=\sum_{a\in[N],\,b\in[M]}
   \frac{K_x(b)}N\frac{K_a(w)}N\\
&=\frac1N\left(\frac1N\sum_{a\in[N]}K_a(w)\right)\\
&=\frac1N\left(
   \frac1{2M}+
   \frac{\mathbf1_{\{w\in\operatorname{im}f\}}}{2N}
   \right).
\end{aligned}
```

Let

```math
q_f(w)=\frac1{2M}
       +\frac{\mathbf1_{\{w\in\operatorname{im}f\}}}{2N},
\qquad
\pi_f(z,w)=\frac{q_f(w)}N.
```

Thus $`P_f^2=\mathbf1\pi_f=\Pi_f`$. Direct substitution gives $`\pi_f P_f=\pi_f`$. The chain has forgotten its starting state after exactly two steps; the one-step rows still depend on $`x`$.

Every nonstationary eigenvalue is zero, but this does not make $`P_f`$ a reversible kernel. If it were reversible, it would be diagonalizable in the stationary weighted inner product. The equation $`P_f^2=\Pi_f`$ would then force $`P_f=\Pi_f`$, contradicting the dependence of $`K_x`$ on $`x`$. The nontrivial one-step memory is carried by a nilpotent part.

Since every row of $`P_f^2`$ is $`\pi_f`$,

```math
D(P_f^2)_{st}
=\sqrt{\pi_f(t)\pi_f(s)},
\qquad
D(P_f^2)=|\pi_f\rangle\langle\pi_f|.
```

The squared chain is exactly reversible and has an ideal rank-one flat discriminant. These facts alone do not construct its quantum oracle.

## The full unitary completion

For $`a\in[M]`$, define

```math
|\chi_a\rangle
=
\sqrt{\frac12+\frac1{2M}}\,|a\rangle
+
\sqrt{\frac1{2M}}\sum_{w\ne a}|w\rangle.
```

The desired row state is $`|u_N\rangle|\chi_{f(x)}\rangle`$.

Use registers $`(X,Y;Z,W)`$, with $`(X,Y)`$ the retained source. Let $`W_\chi`$ be the fixed, known unitary described below satisfying $`W_\chi|0^m\rangle=|\chi_0\rangle`$, and define

```math
A=H^{\otimes n}_Z\otimes W_{\chi,W},
\qquad
U_f=O_f^{X,W}A.
```

The identity on the source registers is implicit in $`A`$. XOR translation maps $`|\chi_0\rangle`$ to $`|\chi_{f(x)}\rangle`$, since it translates the distinguished basis state and preserves the uniform background. Consequently,

```math
U_f|x,y\rangle|0^n,0^m\rangle
=
|x,y\rangle|u_N\rangle|\chi_{f(x)}\rangle.
```

This formula specifies the entire unitary, not just its action on zero endpoints. It uses exactly one evaluation query and has no function-dependent scratch register to erase. Its inverse is $`A^\dagger O_f^{X,W}`$.

Conversely,

```math
U_fA^\dagger=O_f^{X,W}.
```

Therefore an evaluation query is available from one supplied row query and known gates. Dummy $`Y`$ and $`Z`$ registers can be initialized to zero; the net evaluation operation leaves them unchanged.

### Preparing the known background state

The probability distribution of $`|\chi_0\rangle`$ is a half-weight point mass at the all-zero string plus a half-weight uniform distribution. Let $`a_k`$ be the probability that the first $`k`$ bits are zero:

```math
a_k=\frac{1+2^{-k}}2,
\qquad
0\le k\le m,
\qquad
a_0=1.
```

At position $`k`$, conditional on the previous bits all being zero, prepare the next bit with zero probability $`a_k/a_{k-1}`$. Once a previous bit is one, prepare all remaining bits uniformly. This prefix circuit produces exactly $`|\chi_0\rangle`$ with positive amplitudes.

Using decomposed controlled rotations, it requires $`O(m^2)`$ elementary known gates and $`O(m)`$ reusable ancillary qubits. All angles depend only on $`m`$, and are efficiently computable to any prescribed precision. This is an explicit circuit; there is no table of $`M`$ amplitudes to load. Exactness here is in the known-angle gate model. [Finite gate precision](resources.md#finite-gate-precision) is charged for the complete algorithm.

### Controlled calls do not strengthen the lower-bound model

A controlled XOR evaluation can be implemented with one ordinary evaluation query. Prepare an extra $`m`$-qubit register $`D`$ in $`|u_M\rangle`$. Conditional on the control being zero, swap $`W`$ and $`D`$, apply $`O_f^{X,W}`$, and perform the same conditional swap again.

On the zero-control branch, the oracle acts on $`|u_M\rangle`$ and leaves it invariant. On the one-control branch it acts on the intended target. In both branches $`D`$ returns to $`|u_M\rangle`$ and can be reset by Hadamards. The circuit remains valid on superpositions of the control and source.

Controlled $`A`$ is known, so controlled $`U_f`$ and controlled $`U_f^\dagger`$ each reduce to one ordinary $`O_f`$ query. This proves the claimed query equivalence even for algorithms using controlled calls.

## The stationary quantum sample and its known warm state

Let

```math
s=\frac NM=N^{-3},
\qquad
|\psi_f\rangle=\frac1{\sqrt N}\sum_{x\in[N]}|f(x)\rangle,
\qquad
|u\rangle=|u_M\rangle.
```

Then $`\langle u|\psi_f\rangle=\sqrt s`$, and

```math
|q_f\rangle=c|\psi_f\rangle+d|u\rangle,
\qquad
c=\frac{\sqrt{1+s}-\sqrt s}{\sqrt2},
\qquad
d=\frac1{\sqrt2}.
```

This equality follows by comparing the amplitude on an image element with the amplitude outside the image. In particular,

```math
|\pi_f\rangle=|u_N\rangle|q_f\rangle,
\qquad
\alpha:=\langle u|q_f\rangle=d+c\sqrt s,
\qquad
\alpha^2\ge\frac12.
```

Thus the known state $`|\omega\rangle=|u_N\rangle|u_M\rangle`$ has constant coherent overlap with the target.

There is also a precise classical warm-start statement. If $`\nu`$ is uniform on $`\mathcal X`$, then $`\nu(t)\le2\pi_f(t)`$ for every state $`t`$, because $`\pi_f(t)\ge1/(2NM)`$. This uses the convention that a $`2`$-warm starting distribution is pointwise dominated by twice the stationary distribution. It is not a bound on the reverse density ratio.

## Classical sampling remains easy

A stationary classical sample can be produced by choosing $`z`$ uniformly, choosing a fair coin, and taking $`w`$ either uniform on $`[M]`$ or equal to $`f(x)`$ for a uniform $`x\in[N]`$. At most one evaluation query is used.

Equivalently, beginning from a uniformly random classical source and applying one transition already gives $`\pi_f`$. Beginning from an arbitrary fixed source requires two transitions. These statements are compatible with the coherent lower bound: discarding the source label of a coherent trajectory produces a mixed state, rather than the required square-root superposition of endpoint probabilities.

## Stochastic time reversal is an additional resource

The inverse of the supplied unitary unprepares a coherent forward row. It does not supply a clean row of the stochastic time-reversed chain.

For a stationary kernel, stochastic time reversal is defined by

```math
P_f^\star(t,s)=\frac{\pi_f(s)P_f(s,t)}{\pi_f(t)}.
```

For $`t=(z,w)`$ and $`s=(x,y)`$, substitution gives

```math
P_f^\star((z,w),(x,y))
=
\frac{q_f(y)K_x(w)}{Nq_f(w)}.
```

Define the normalized distribution

```math
r_w(x)=\frac{K_x(w)}{Nq_f(w)},
\qquad
\sum_xr_w(x)=1.
```

The clean reverse-row state therefore factors exactly as

```math
|P_f^\star((z,w),\cdot)\rangle
=
|r_w\rangle|q_f\rangle.
```

A reverse-row preparation on any fixed known source would produce $`|q_f\rangle`$ by discarding its first endpoint coordinate. The [state-preparation reduction](lower-bounds.md#state-preparation-and-clean-powered-rows) consequently gives an $`\Omega(\sqrt N)`$ lower bound for clean stochastic time-reversal access at the stated fixed error. The forward unitary inverse $`U_f^\dagger`$ is already allowed in that lower bound.

This distinguishes two oracle assumptions that are sometimes both called reverse access. Our statement concerns clean reverse rows. It does not infer a lower bound for every alternative interface to the reverse kernel merely from this factorization.

## A constant operator gap between the two quantum powers

The failure of inexpensive clean powering is accompanied by an explicit matrix mismatch. For this family, the difference between $`D(P_f^2)`$ and $`D(P_f)^2`$ has operator norm bounded below by a universal positive constant.

Let $`B`$ be the $`N`$-by-$`M`$ matrix

```math
B_{xw}=\sqrt{K_x(w)}.
```

Its rows are the states $`|\chi_{f(x)}\rangle`$. Injectivity makes every pair of distinct rows have the same inner product

```math
\begin{aligned}
\beta
&=
2\sqrt{\frac12+\frac1{2M}}
 \sqrt{\frac1{2M}}
+\frac{M-2}{2M}\\
&=
\frac12+\frac{\sqrt{M+1}-1}{M}.
\end{aligned}
```

Hence

```math
BB^{\mathsf T}
=
(1-\beta)I_N+\beta\mathbf1\mathbf1^{\mathsf T},
\qquad
\|B\|^2=1+(N-1)\beta.
```

Identify a state vector on $`[N]\times[M]`$ with an $`N`$-by-$`M`$ matrix $`X`$, preserving its norm as the Frobenius norm. The flat discriminant acts as

```math
D(P_f):X\longmapsto\frac1N BX^{\mathsf T}B.
```

The induced norm is at most $`\|B\|^2/N`$. Equality holds: for a leading left/right singular-vector pair $`u,v`$ of $`B`$, the rank-one matrix $`X=uv^{\mathsf T}`$ is an eigenvector of this map with eigenvalue $`\|B\|^2/N`$. Thus

```math
\|D(P_f)\|
=
\frac{1+(N-1)\beta}{N}.
```

For $`M=N^4`$,

```math
\beta\le\frac12+\frac1{N^2},
\qquad
\|D(P_f)\|
\le
\frac12+\frac1{2N}+\frac{N-1}{N^3}
\le\frac{11}{16}
\qquad(N\ge4).
```

Because $`D(P_f)`$ is symmetric, $`\|D(P_f)^2\|=\|D(P_f)\|^2`$. The reverse triangle inequality and $`\|D(P_f^2)\|=1`$ now imply

```math
\boxed{
\|D(P_f^2)-D(P_f)^2\|
\ge
1-\|D(P_f)\|^2
\ge
\frac{135}{256}.
}
```

Moreover $`\|D(P_f)\|\to1/2`$, so this lower bound tends to $`3/4`$. No equality for the limiting mismatch norm is claimed.

A block-encoding product that correctly implements $`D(P_f)^2`$ therefore remains a constant distance from the desired powered flat discriminant. The distinction survives exact gates and exact classical two-step mixing.


