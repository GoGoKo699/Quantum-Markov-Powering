# Interpretation: classical mixing and coherent powering

The construction separates two resources: generating classical endpoints of a Markov process and producing the pure square-root state of their distribution. In the explicit forward-oracle model, a full-support chain can become exactly stationary after two steps while its clean powered-row oracle, stationary qsample, stationary reflection, and normalization-one flat-discriminant block encoding require $`\Theta(\sqrt N)`$ queries at fixed sufficiently small error. The lower bound is inherited through a reduction from noncoherent index erasure; the matching upper bound uses amplitude amplification. See the [main theorem and model](model.md#main-theorem) and the [related-work dependencies](../references/related-work.md).

The significance is an access-model obstruction to a general coherent powering compiler. The construction does not establish a lower bound on ordinary sampling or on every quantum algorithm that uses a Markov chain.

## What the original oracle supplies

For a kernel $`P`$, clean forward-row access means a specified unitary completion of

```math
U_P|x\rangle|0\rangle
=|x\rangle\sum_y\sqrt{P(x,y)}|y\rangle.
```

The input includes its inverse and controlled use. For the constructed family the completion has the explicit form $`U_{P_f}=O_f A`$, where $`A`$ is known and independent of the hidden injection. Consequently the completion neither hides an extra oracle nor grants unexplained information on inputs outside the prepared subspace. Uniform state preparation and the other known rotations have explicitly charged gate implementations. No quantum memory containing a table of transition probabilities is supplied.

Using the oracle twice produces a pure trajectory state,

```math
|x\rangle\sum_{y,z}\sqrt{P(x,y)P(y,z)}|y\rangle|z\rangle.
```

Measuring the endpoint gives exactly the two-step classical law. Discarding the intermediate register generally leaves a mixed state. Producing instead

```math
|x\rangle\sum_z\sqrt{P^2(x,z)}|z\rangle
```

with no endpoint-dependent history is a different transformation. The query lower bound applies even if an algorithm leaves arbitrary additional garbage, provided the target register has the required high fidelity with this pure endpoint state.

## Why mixing does not erase quantum history

For the family on $`[N]\times[M]`$ with $`M=N^4`$,

```math
P_f((x,y),(z,w))
=\frac1N\left(\frac12\mathbf1_{w=f(x)}+\frac1{2M}\right),
\qquad
P_f^2=\mathbf1\pi_f.
```

The stationary law is

```math
\pi_f(z,w)=\frac1N\left(\frac1{2N}\mathbf1_{w\in\operatorname{im}f}
+\frac1{2M}\right).
```

The classical law loses all dependence on the initial state after two steps. The qsample still encodes the unknown image of $`f`$. Removing its known uniform component exposes an approximate uniform image state with constant probability. That is the reduction that imports the index-erasure lower bound.

The uniform law is 2-warm in the convention $`\nu\le2\pi_f`$, and the known uniform qsample has squared overlap at least $`1/2`$ with the target. This rules out a vanishing initial-overlap explanation for the separation. It does not provide the target reflection: obtaining that reflection is one of the hard tasks.

## The exact distinction between two discriminants

Let $`W_\pi=\operatorname{diag}(\pi)`$ and let $`P^*`$ denote the stationary time-reversal. The curved discriminant is

```math
\mathcal D(P)=W_\pi^{1/2}PW_\pi^{-1/2},
\qquad
\mathcal D(P)_{xy}=\sqrt{P(x,y)P^*(y,x)}.
```

It obeys $`\mathcal D(P^j)=\mathcal D(P)^j`$. Given coherent forward and reversed-row access, the corresponding matrix encoding can therefore be composed with linear cost in the power, using ordinary [block-encoding products](../references/related-work.md#block-encoding-products). This remains a valid positive construction.

The forward-only flat discriminant is

```math
D(P)_{xy}=\sqrt{P(x,y)P(y,x)}.
```

Multiplying its encoding gives $`D(P)^j`$. The flat discriminant of the powered chain is $`D(P^j)`$. Their entries differ by a conditional path-overlap factor. In the project's path identity,

```math
[D(P)^j]_{xy}
=D(P^j)_{xy}\,\mathsf F\!\left(B^j_{x\to y},\operatorname{rev}B^j_{y\to x}\right),
```

where $`\mathsf F`$ is the classical Bhattacharyya affinity between the two normalized bridge laws, for endpoints with nonzero transition probabilities. Retaining the trajectory does not make this factor disappear. The explicit family has an [operator-norm discrepancy of at least $`135/256`$](construction.md#a-constant-operator-gap-between-the-two-quantum-powers) already at $`j=2`$.

The availability of $`U_P^\dagger`$ does not supply $`U_{P^*}`$. The former reverses the preparation circuit; the latter prepares a different conditional probability law. Conflating them would change the input model and invalidate the lower-bound comparison.

## How to read a powered-kernel spectral bound

For an implementation using a powered-kernel primitive, write $`C_j(\delta)`$ for the number of original-oracle calls needed to implement that primitive to error $`\delta`$. If an outer spectral transformation makes $`L_j(\eta)`$ calls, a modular implementation must charge

```math
L_j(\eta)\,C_j(\delta),
```

as well as preparation, normalization, and the error budget. A customary sufficient choice is $`\delta=O(\eta/L_j)`$ under a telescoping norm bound. This is cost accounting for a specified composition, not an assertion that every algorithm must follow it or pay this product.

For [Claudon–Piquemal–Monmarché](../references/related-work.md#nonreversible-spectral-methods), the conditional transformation theorems continue to hold. The inference tested here is the stronger one that early reversibility of a power guarantees a cheaper clean reflection when costs are measured in the original forward oracle. That inference needs an independent bound on $`C_j`$. In this family, $`C_2=\Theta(\sqrt N)`$ at fixed error for the relevant clean resources, including the [powered Szegedy row-subspace reflection itself](lower-bounds.md#direct-powered-szegedy-reflection).

## Early reversibility with an independently slow mode

Tensor the hard chain with the known two-state symmetric chain $`Q_T`$ that flips with probability $`1/T`$, for $`T\ge4`$. Then

```math
\widetilde P_f=P_f\otimes Q_T,
\qquad
\widetilde P_f^{\,2}=\Pi_f\otimes Q_T^2,
\qquad
\Pi_f=\mathbf1\pi_f.
```

The square is exactly reversible. Its largest nontrivial eigenvalue is $`(1-2/T)^2`$, giving gap $`4(T-1)/T^2=\Theta(1/T)`$. The worst-case classical mixing time is $`\Theta(T)`$, while the early-reversibility time is at most two. Nevertheless, the clean resources retain their $`\Theta(\sqrt N)`$ query complexity. Taking $`N=2^n`$ and $`T=n\ge4`$ gives clean-resource cost $`\Theta(2^{n/2})`$ while worst-case classical mixing takes $`\Theta(n)`$ steps. This directly separates the structural early-reversibility condition from implementation cost; [the product analysis](early-reversibility.md) gives the details.

Two qualifications are essential. The slow factor is known and independent, so a general algorithm may bypass it; the result is not an $`\Omega(\sqrt{NT})`$ lower bound. Also, the specified uniform source is already stationary on that factor and becomes stationary on the hard factor after one classical step. The warm-start trajectory does not mix slowly. The comparison with $`\Theta(T)`$ is a comparison to worst-case classical mixing, and the clean quantum output task is stronger than drawing one ordinary sample.

## Ordinary sampling and observables

An exact stationary classical sample is inexpensive: draw $`x`$ uniformly, query $`f(x)`$, and use the known fair-coin mixture with a uniform output. The first coordinate is independently uniform. This needs one injection query. A coherent implementation may retain $`x`$ and the mixture coin as history.

For an efficiently evaluable bounded endpoint observable, amplitude estimation can use that retained-history preparation, mark the observable, and uncompute. It does not require a pure stationary qsample on the endpoint alone. The clean-state lower bound therefore does not imply a corresponding $`\sqrt N`$ cost for scalar expectation estimation.

The same distinction applies to couplings. A classically coalescing random-map representation need not have an inexpensive quantization in the supplied oracle model. [Temme–Wocjan's implementation theorem](../references/related-work.md#quantized-couplings) explicitly requires additional access. In our two-step coupling, the required inverse-image and stationary-ratio information can encode the hidden image. Its classical coalescence time alone does not remove the implementation cost.

## A sufficient additional resource

The [conditional-bridge compiler](bridge-composition.md#5-a-compiler-from-conditional-bridge-unpreparation) proves a positive statement. If one can coherently prepare the normalized internal history conditioned on both endpoints, with a fixed positive-amplitude phase, its inverse cleans the history. The powered-row oracle then costs $`j`$ base-row queries plus the explicitly charged bridge-unpreparation cost. This supplied bridge unitary is a sufficient resource; classical conditional samples alone do not provide it.

The [approximation theorem](bridge-composition.md#6-approximation-that-composes-coherently) makes this statement stable under coherent reuse. A uniform phase-fixed bridge-vector error $`\delta`$ gives a compiled full unitary within operator norm $`\delta`$ of one fixed exact clean-row completion, including its inverse. A circuit making $`q`$ forward, inverse, or controlled calls then has vector error at most $`q\delta`$ and unhalved channel diamond-norm error at most $`2q\delta`$. This comparison does not claim closeness to an independently prescribed completion. It requires the coherent unitary promise, not just good bridge density matrices after discarding work.

Separately, uniformly high overlap between forward and reversed bridge laws gives the [approximate discriminant criterion](bridge-composition.md#4-a-quantitative-block-encoding-criterion). This can make the retained-history compression a good block encoding without producing clean endpoint rows. These are distinct sufficient conditions for distinct tasks.

## What is established and what remains open

The established statement is an explicit oracle separation with favorable classical properties and a matching query bound. It proves that clean one-step forward access is not closed under temporal coarse-graining at cost depending only on the number of steps, mixing time, a powered-chain gap, or constant source overlap. It also identifies an independent cost term that must appear when a powered-chain spectral method is instantiated from that access.

The result does not claim that every useful nonreversible chain has this obstruction. The bridge compiler and discriminant criterion above provide explicit sufficient promises. Structured transition formulas, efficiently accessible reverse kernels, known stationary ratios, or accessible inverse images can supply other algorithms. A general characterization of inexpensive clean powering, and the identification of applications where the clean resource is operationally necessary, remain separate questions. The present lower bound does not settle them.
