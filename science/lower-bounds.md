# Lower bounds from noncoherent index erasure

The lower bound allows arbitrary final garbage. Its obstruction is therefore not an artificial requirement that the algorithm clean every work register. It is the requirement that a designated output register contain the stationary quantum sample, or that an implemented operator be accurate on all required inputs.

We first prove one reduction for the base family. [Early reversibility](early-reversibility.md) transfers it to the slow product without changing the constants.

## Inherited hardness theorem

For an injection $`f:[N]\to[M]`$, index erasure asks for

```math
|\psi_f\rangle=N^{-1/2}\sum_{x\in[N]}|f(x)\rangle.
```

The [Lindzey–Rosmanis theorem](../references/related-work.md#index-erasure), Theorem 1 in the journal article (Theorem 1.1 in arXiv v3), gives bounded-error quantum query complexity $`\Theta(\sqrt N)`$ in the noncoherent state-generation model when $`M\ge N^{3+\kappa}`$ for a fixed $`\kappa>0`$. Our choice $`M=N^4`$ satisfies this hypothesis.

The noncoherent error criterion is a lower bound on the designated output's fidelity with the target, with arbitrary ancillary state allowed. Measurements and mixed outputs can be purified, retaining their records in ancillary registers. The reduction below produces target fidelity greater than $`0.977`$ using a bounded maximum number of queries, so it lies within the small constant-error regime of that theorem.

The supplied row oracle, its inverse, and controlled versions each use one standard evaluation query, as proved in [the construction](construction.md#controlled-calls-do-not-strengthen-the-lower-bound-model). It therefore suffices to convert each proposed coherent Markov primitive into index erasure with constant overhead.

## A common projection that reveals the image state

Use the decomposition from [the stationary state](construction.md#the-stationary-quantum-sample-and-its-known-warm-state):

```math
|q_f\rangle=c|\psi_f\rangle+d|u\rangle,
\qquad
s=N^{-3},
\qquad
\langle u|\psi_f\rangle=\sqrt s.
```

The known projector

```math
H=I-|u\rangle\langle u|
```

removes the uniform component. Implement this two-outcome measurement by applying Hadamards, coherently marking the all-zero string in a single flag, measuring only that flag, and undoing the marking and Hadamards. Accept the nonzero outcome; the endpoint basis label is not measured. On the accepted outcome,

```math
H|q_f\rangle
=
c\bigl(|\psi_f\rangle-\sqrt s\,|u\rangle\bigr)
=
\sqrt v\,|\psi_f^\perp\rangle,
```

where

```math
|\psi_f^\perp\rangle
=
\frac{|\psi_f\rangle-\sqrt s\,|u\rangle}{\sqrt{1-s}},
\qquad
v=c^2(1-s).
```

The accepted state has target fidelity

```math
|\langle\psi_f|\psi_f^\perp\rangle|^2=1-s\ge\frac{63}{64}.
```

For $`N\ge4`$, $`\sqrt s\le1/8`$ and

```math
c\ge\frac{7}{8\sqrt2},
\qquad
v\ge
\frac{49}{128}\frac{63}{64}
=
\frac{3087}{8192}
=:v_0
>0.376.
```

The acceptance probability is bounded below independently of the injection and of $`N`$.

## State preparation and clean powered rows

Suppose the designated stationary-state output has trace distance at most $`\delta=10^{-3}`$ from $`|\pi_f\rangle`$. Discard its first coordinate and all work registers, obtaining a state $`\rho`$ within trace distance $`\delta`$ of $`|q_f\rangle\langle q_f|`$.

After measuring $`H`$, let $`p`$ be the acceptance probability. Trace-distance control of measurement probabilities gives

```math
v-\delta\le p\le v+\delta.
```

The unnormalized accepted state's overlap with the desired image projector obeys

```math
\langle\psi_f|H\rho H|\psi_f\rangle
\ge v(1-s)-\delta.
```

Indeed, $`H|\psi_f\rangle\langle\psi_f|H`$ is an effect between zero and the identity. The conditional fidelity is consequently at least

```math
\frac{v(1-s)-\delta}{v+\delta}
=
1-s-\frac{\delta(2-s)}{v+\delta}
\ge
\frac{63}{64}-\frac{2\delta}{v_0}
>
\frac{63}{64}-0.0054.
```

Here $`p>0.375`$. Clean row preparation for $`P_f^2`$ reduces immediately to this task: initialize any fixed source, apply the proposed powered row oracle, and retain its endpoint. Every exact row of $`P_f^2`$ is $`\pi_f`$. A vector-isometry error $`\delta`$ implies output trace distance at most $`\delta`$.

## A normalization-one block encoding of the powered discriminant

Suppose the zero-ancilla block $`B`$ satisfies

```math
\|B-D(P_f^2)\|\le\delta,
\qquad
D(P_f^2)=|\pi_f\rangle\langle\pi_f|.
```

Apply the block encoding to the known input $`|\omega\rangle=|u_N\rangle|u_M\rangle`$, accept the zero block ancilla, and then accept the $`H`$ outcome on the second state coordinate.

The ideal accepted vector is

```math
(I\otimes H)
|\pi_f\rangle\langle\pi_f|\omega\rangle
=
\alpha\sqrt v\,|u_N\rangle|\psi_f^\perp\rangle.
```

Its norm is $`a=\alpha\sqrt v`$, with

```math
a^2\ge\frac{v_0}{2}>0.188.
```

The actual accepted vector differs from it by at most $`\delta`$ in Euclidean norm. Its acceptance probability is therefore at least $`(a-\delta)^2>0.187`$.

For completeness, if nonzero vectors $`x,y`$ satisfy $`\|x-y\|\le\delta`$ and $`\|y\|=a`$, then

```math
\left\|
\frac{x}{\|x\|}-\frac{y}{a}
\right\|
\le
\frac{2\delta}{a}.
```

This follows by adding and subtracting $`x/a`$ and using $`|\|x\|-a|\le\delta`$. The trace distance between the corresponding normalized pure states is no larger. In the present reduction it is below $`0.0047`$. A target-projector measurement consequently shows that the accepted output has fidelity at least

```math
\frac{63}{64}-0.0047
>
\frac{63}{64}-0.0054
```

with $`|\psi_f\rangle`$ after discarding the first coordinate.

This argument uses the normalization-one signal amplitude. It does not assume that applying a block encoding automatically prepares its encoded projector's eigenstate with unit success probability.

## Stationary reflection

Let

```math
R_{\pi_f}=2|\pi_f\rangle\langle\pi_f|-I.
```

Apply a proposed implementation to the same known state $`|\omega\rangle`$, then accept $`H`$ on the second coordinate. Because $`H|u_M\rangle=0`$,

```math
(I\otimes H)R_{\pi_f}|\omega\rangle
=
2\alpha\sqrt v\,|u_N\rangle|\psi_f^\perp\rangle.
```

The ideal success probability is $`4\alpha^2v\ge2v_0>0.753`$. If auxiliary registers are used in the implementation, also accept their prescribed zero outcome. The clean-ancilla operator error from [the model](model.md#quantum-primitives-and-error-conventions) bounds the accepted-vector error by $`\delta`$.

The preceding normalized-vector estimate gives still better constants than in the block-encoding reduction. In particular, success exceeds $`0.187`$ and conditional target fidelity exceeds $`63/64-0.0054`$.

Only one ordinary invocation of the synthesized reflection is used in each attempt. Controlled access to that synthesized reflection is unnecessary. A common global phase is immaterial to this state-generation reduction.

## Direct powered Szegedy reflection

For the base family,

```math
V_{P_f^2}|s\rangle=|s\rangle|\pi_f\rangle,
\qquad
R_{P_f^2}=I\otimes R_{\pi_f}.
```

Initializing an arbitrary fixed source therefore turns an implementation of $`R_{P_f^2}`$ into an implementation of $`R_{\pi_f}`$ with the same initialized-ancilla operator error. This proves hardness of the powered row-subspace reflection directly. It is not a lower bound only for one chosen method of constructing that reflection.

For the product chain, [the corresponding invariant subspace](early-reversibility.md#the-powered-szegedy-reflection-is-hard-directly) uses a known row state of the two-state factor and gives the same conclusion.

## Bounded repetition and the source's error convention

Every reduction above has, in each fresh attempt,

```math
p_{\rm accept}>0.187,
\qquad
F_{\rm conditional}>
\frac{63}{64}-0.0054.
```

Run at most $`32`$ independent attempts, retain the first accepted output, and output an arbitrary fixed state if all attempts fail. Then

```math
p_{\rm fail}<(1-0.187)^{32}<0.002
```

and the final designated output satisfies

```math
F_{\psi_f}>
(1-0.002)\left(\frac{63}{64}-0.0054\right)
=
0.97701705
>
0.977.
```

Thus the index-erasure error in the squared-fidelity convention is less than $`0.023`$, in particular less than $`0.03`$. The query budget is at most $`32Q`$ if the proposed Markov task uses at most $`Q`$ row queries. Deferred measurements and inactive branches can be implemented with the controlled evaluations already covered by the access equivalence.

The lower bound therefore forces $`Q=\Omega(\sqrt N)`$ for each task. A separately heralded state-generation primitive with a fixed positive success probability also gives an $`\Omega(\sqrt N)`$ bound by increasing the constant repetition cap; the displayed $`32`$-attempt constants apply to the unconditional error conventions used in the main theorem.

## What the lower bound does and does not identify

All function-dependent garbage is allowed in the stationary state-generation task. The lower bound is for worst-case injections, rather than for every particular efficiently described function. The Markov state space has $`NM=N^5`$ states; no optimal exponent in that dimension is asserted.

If an algorithm receives only $`R_{P_f}`$ and controlled versions, simulate each with $`U_f`$, a known zero-endpoint reflection, and $`U_f^\dagger`$. Two row queries per reflection preserve the lower bound. The [matching upper bounds](upper-bounds.md) are stated for row-unitary access, not for this restricted reflection-only interface.

