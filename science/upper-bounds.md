# Matching constructive upper bounds

The lower bound is tight in the supplied row-unitary model. This page gives a deterministic circuit with a bounded number of queries, including the clean state preparation needed for operator implementations. Exactness is first stated with ideal known-angle gates; [finite gate synthesis](resources.md#finite-gate-precision) supplies uniform operator approximations without increasing the query count.

The ingredients are inherited [exact amplitude amplification with known success probability](../references/related-work.md#amplitude-amplification) and a coherent combination of two prepared states. We spell out the construction to identify every query, auxiliary register, and success amplitude.

## Preparing the image state cleanly

An evaluation query is available as $`O_f=U_fA^\dagger`$. On an $`n`$-qubit index register $`I`$ and an $`m`$-qubit target $`W`$, define

```math
L_f=O_f^{I,W}(H_I^{\otimes n}\otimes I_W).
```

Dummy registers needed to match the supplied row-oracle interface return unchanged after the evaluation simulation. Then

```math
L_f|0^n,0^m\rangle
=
\frac1{\sqrt N}\sum_x|x,f(x)\rangle.
```

The known projection of $`I`$ onto $`|u_N\rangle`$ has success probability exactly $`1/N`$ and accepted vector

```math
(|u_N\rangle\langle u_N|\otimes I)
L_f|0,0\rangle
=
\frac1{\sqrt N}|u_N\rangle|\psi_f\rangle.
```

This gives a coherent preparation procedure with a known success amplitude. It does not yet allow the index register to be discarded.

### Exact amplification with an explicit query cap

Choose the integer

```math
k=\lceil\sqrt N\rceil,
\qquad
\vartheta=\frac{\pi}{4k+2},
\qquad
r=N\sin^2\vartheta.
```

Since $`k\ge\sqrt N`$ and $`\pi<4`$, $`0\lt r\le1`$. Prepare a dilution flag $`C`$ with probability $`r`$ of being one, independently of $`L_f`$. Let $`\mathcal A_f`$ be this preparation together with $`L_f`$, and declare the good subspace to be

```math
C=1
\quad\hbox{and}\quad
I=|u_N\rangle.
```

Its success probability is exactly $`\sin^2\vartheta`$. The normalized good state is $`|1\rangle_C|u_N\rangle_I|\psi_f\rangle_W`$.

Let $`S_0=I-2|0\rangle\langle0|`$ on the initialized preparation registers and let $`S_{\rm good}=I-2\Pi_{\rm good}`$. The amplitude-amplification iterate is

```math
G=-\mathcal A_f S_0\mathcal A_f^\dagger S_{\rm good}.
```

Both reflections other than the applications of $`\mathcal A_f`$ are known. In the two-dimensional good/bad subspace, $`G`$ advances the angle by $`2\vartheta`$. Therefore

```math
G^k\mathcal A_f|0\rangle
=
|1\rangle_C|u_N\rangle_I|\psi_f\rangle_W,
```

because $`(2k+1)\vartheta=\pi/2`$. Flip $`C`$ and apply Hadamards to $`I`$ to return both to zero. This gives a clean preparation unitary $`W_\psi`$ for the image state.

The exact query count is

```math
q_\psi=2k+1
=
2\lceil\sqrt N\rceil+1
\le2\sqrt N+3.
```

The inverse and controlled versions of this explicitly known circuit have the same query count. The known global phases in the amplification expression are included when constructing a controlled version, so that no relative phase is lost in the next step.

## Preparing the stationary sample

From [the construction](construction.md#the-stationary-quantum-sample-and-its-known-warm-state),

```math
|q_f\rangle=c|\psi_f\rangle+d|u_M\rangle,
\qquad
c=\frac{\sqrt{1+s}-\sqrt s}{\sqrt2},
\qquad
d=\frac1{\sqrt2},
\qquad
s=N^{-3}.
```

Let $`\ell=c+d`$. Since $`0\lt c\le1/\sqrt2`$,

```math
1<\ell\le\sqrt2.
```

The left inequality follows, for example, from $`N\ge4`$ and $`c\ge7/(8\sqrt2)`$. The target state has unit norm, including the known overlap $`\langle u_M|\psi_f\rangle=\sqrt s`$.

Prepare a flag $`F`$ in

```math
|a\rangle
=
\sqrt{\frac c\ell}|0\rangle
+
\sqrt{\frac d\ell}|1\rangle.
```

Conditioned on $`F`$, prepare either $`|\psi_f\rangle`$ using $`W_\psi`$ or $`|u_M\rangle`$ using Hadamards. Both branches return the same work registers to zero. Undo the preparation of $`|a\rangle`$. The zero-flag block of the resulting unitary $`B_f`$ is

```math
(\langle0|_F\otimes I)B_f|0\rangle
=
\frac{c|\psi_f\rangle+d|u_M\rangle}{\ell}
=
\frac{|q_f\rangle}{\ell},
```

with all other work registers zero on that accepted branch. Its success probability is $`1/\ell^2\ge1/2`$, known independently of the injection.

Add a second flag whose probability of being one is $`\ell^2/4`$. Declaring success to mean that this flag is one and $`F`$ is zero makes the combined success probability exactly $`1/4`$. One amplitude-amplification iteration then makes success certain, because $`3\arcsin(1/2)=\pi/2`$. Reset the known flags.

The resulting unitary $`W_q`$ prepares $`|q_f\rangle`$ cleanly. It uses two forward applications and one inverse application of the combined preparation, hence at most

```math
q_q=3q_\psi
```

evaluation queries, or the same number of supplied row queries. Adding a uniform $`n`$-qubit state produces a clean unitary $`W_\pi`$ for

```math
|\pi_f\rangle=|u_N\rangle|q_f\rangle,
\qquad
q_\pi=3(2\lceil\sqrt N\rceil+1).
```

No repetition until success or unbounded stopping time is used.

## Obtaining the five primitives

Let the work register of $`W_\pi`$ be included explicitly, so that

```math
W_\pi|0\rangle_{\rm state}|0\rangle_{\rm work}
=
|\pi_f\rangle_{\rm state}|0\rangle_{\rm work}.
```

### Stationary sample and clean powered row

Applying $`W_\pi`$ prepares the stationary quantum sample with $`q_\pi`$ queries. Since every row of $`P_f^2`$ is $`\pi_f`$, a powered row unitary can preserve its source and apply $`W_\pi`$ to fresh endpoint and work registers. This uses $`q_\pi`$ queries and is a clean row implementation uniformly over all source superpositions.

### Stationary and powered Szegedy reflections

Conjugating the all-zero reflection gives

```math
\mathcal R_\pi
=
W_\pi(2|0\rangle\langle0|-I)W_\pi^\dagger.
```

This is a reflection on the full state-and-work space. On the initialized-work subspace it acts exactly as $`R_{\pi_f}=2|\pi_f\rangle\langle\pi_f|-I`$ and returns the work register to zero. Its query count is $`2q_\pi`$.

For the base chain, $`R_{P_f^2}=I\otimes R_{\pi_f}`$, so the same count suffices. More generally, if $`\mathcal U_2`$ is the powered row preparation with clean work, conjugate

```math
2I_{\rm source}\otimes
|0\rangle\langle0|_{\rm endpoint,work}
-I
```

by $`\mathcal U_2`$. Its restriction to zero work is the desired row-subspace reflection. The endpoint and work registers must both be included in the zero projector; reflecting only a subset of the preparation workspace would not justify the stated operator.

### Normalization-one flat-discriminant block encoding

Let $`S`$ swap source and endpoint while leaving the work register alone. The unitary

```math
\mathcal B_2=\mathcal U_2^\dagger S\mathcal U_2
```

has, between zero endpoint-and-work embeddings, the block

```math
V_{P_f^2}^\dagger S V_{P_f^2}
=
D(P_f^2).
```

This is an exact normalization-one block encoding, using $`2q_\pi`$ queries. It is also Hermitian because $`S`$ is Hermitian.

The same constructions apply to [the slow product](early-reversibility.md): prepare its known one-qubit powered row in addition to $`|\pi_f\rangle`$. The known factor costs no function queries.

## Uniform approximation of the operators

The exact circuits specify complete unitary algorithms with explicit ancillary registers. Approximate every known gate in the entire chosen circuit so that the product of the approximating gates differs from the ideal product by at most $`\varepsilon`$ in operator norm. The resulting clean row and reflection implementations satisfy the initialized-ancilla error definitions in [the model](model.md#quantum-primitives-and-error-conventions); taking a block cannot increase the error.

Equivalently, if a state-preparation unitary is approximated to operator error $`\eta`$, conjugating a known reflection incurs at most $`2\eta`$ error. A row-isometry approximation of size $`\eta`$ changes the compressed swap block by at most $`2\eta`$. Additional known-gate errors must be included in that budget.

This is why the construction provides operator approximations, not just high fidelity on the single initial state used in its preparation proof. The finite-gate count and precision required for the full circuit are given next in [resources](resources.md).

