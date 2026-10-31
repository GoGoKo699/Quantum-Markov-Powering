# From Childs's quantum algorithms notes to coherent Markov powering

A classical simulation can run a Markov chain for two steps and keep only the final state. A quantum circuit can do that too, if the required output is a classical sample. The additional task in this project is to produce a **pure state whose amplitudes are the positive square roots of the endpoint probabilities**, with intermediate information removed coherently. The difference between these tasks is the starting point for the result.

This bridge connects one educational source to the project's definitions and proofs. It supplies the probability calculations and reductions that are specific to this project, while identifying the research theorem used for the lower bound. The [learning overview](README.md) and [milestone map](milestones.md) organize the same material into a shared reading route.

## Selected source

**Andrew M. Childs, _Lecture Notes on Quantum Algorithms_, version dated 17 April 2025.**

- [Official source page](https://www.cs.umd.edu/~amchilds/qa/)
- [Official PDF](https://www.cs.umd.edu/~amchilds/qa/qa.pdf)
- Bibliography key: `Childs2025Notes`

The date is the date printed on the verified PDF's title page. Page numbers below are the notes' **printed page numbers**, not a PDF viewer's file-page counter. The official PDF URL may later serve a revised version; the section names and date identify the version used here. The route uses selected sections, rather than requiring the whole notes.

## Reading route

| Part of the notes | Printed pages | Use in this project |
|---|---:|---|
| §§1.1–1.2, “Quantum data” and “Quantum circuits” | 1–2 | Amplitude vectors, registers, unitary circuits, and computational-basis measurement. The endpoint mixed-state calculation below is supplied locally. |
| §1.3, “Universal gate sets”; §1.4, “Reversible computation” | 2–3 | Operator-norm approximation, reversible function evaluation, and the role of retained computational history. |
| Chapter 2, “Efficient universality of quantum circuits,” especially §2.1, “Subadditivity of errors” | 7–10; §2.1 on 7 | Why precision must be budgeted across a circuit. The project's gate and workspace accounting is in [resources](../science/resources.md). |
| §18.1, “Discrete-time quantum walk”; §18.2, “How to quantize a Markov chain” | 81–82 | From a row-state isometry to a reflection and a walk unitary. The stochastic-matrix convention needs the translation below. |
| §18.3, “Spectrum of the quantum walk,” including Theorem 18.1 | 83–84 | The spectral relation between an available walk and its encoded discriminant. This does not supply an oracle for a powered chain. |
| §19.3, “Amplitude amplification and quantum counting” | 88–89 | The square-root improvement in amplifying a known success event. The exact amplification construction used here is detailed separately in the project's upper bound. |
| §§21.1–21.2, “Quantum query complexity” and “Quantum queries” | 97–98 | A query is a call to a specified input-dependent operation; known gates are a separate resource. |
| Chapter 23, “The quantum adversary method” | 109–114 | Background on query lower bounds. The noncoherent index-erasure theorem used here is an imported research result, not a theorem proved in this chapter. |
| §29.1, “Block encoding”; §§29.2–29.3, “Quantum signal processing” and “Qubitization” | 143–147 | Representing a matrix as a unitary block and applying spectral transformations to the matrix actually encoded. |

Stationarity, total-variation mixing, warm starts, conditional Markov bridges, and the particular index-erasure reduction are defined in the project. The notes' quantum-walk constructions provide tools for those arguments; the project does not attribute all of these probability notions or its conclusions to the notes.

## Notation and access

For a probability distribution $`p`$ on a finite set, this project writes its positive-amplitude quantum sample as

```math
|p\rangle=\sum_x\sqrt{p(x)}\,|x\rangle.
```

Measurement in the basis labeled by $`x`$ returns $`x`$ with probability $`p(x)`$. A distribution and its quantum sample are different mathematical objects: the distribution does not specify how the pure state is prepared or whether unobserved registers remain correlated with it.

There are several notation changes between the notes and the project.

| Childs's notation or convention | Project convention and interpretation |
|---|---|
| Column-stochastic transition matrix: $`P_{kj}`$ is the probability to move from $`j`$ to $`k`$ | Row-stochastic matrix: $`P(x,y)`$ is the probability to move from $`x`$ to $`y`$. The two matrices are transposes. |
| $`T`$, the isometry embedding a state label and its transition amplitudes | $`V_P`$, the clean row-state isometry |
| $`\Pi=TT^\dagger`$ in Chapter 18 | The quantum projector $`V_PV_P^\dagger`$ on a subspace of two registers |
| $`U=S(2\Pi-I)`$ in Chapter 18 | The walk unitary $`S R_P`$, with $`S`$ swapping the two state registers |
| $`D_{jk}=\sqrt{P_{jk}P_{kj}}`$ | The flat discriminant $`D(P)`$; this symmetric matrix is unchanged by transposing the transition matrix |

In particular, the project's classical matrix $`\Pi_f=\mathbf1\pi_f`$, whose every row is the stationary distribution, is **not** Childs's doubled-space projector $`\Pi`$. The project's supplied unitary $`U_f`$ prepares a row; it is **not** the walk unitary denoted by $`U`$ in Chapter 18.

The query model also matters. An unknown injection $`f:[N]\to[M]`$, with $`[L]=\{0,\ldots,L-1\}`$, is supplied through

```math
O_f|x,w\rangle=|x,w\oplus f(x)\rangle.
```

The XOR keeps the operation reversible. Evaluating it on a uniform superposition gives

```math
\frac1{\sqrt N}\sum_x|x\rangle|f(x)\rangle.
```

It does not immediately give the image state $`N^{-1/2}\sum_x|f(x)\rangle`$: the input label is still present and correlated with the output.

The [model](../science/model.md) supplies one fully specified row-preparation unitary, its actual inverse, and charged controlled calls. In the [construction](../science/construction.md#the-full-unitary-completion),

```math
U_f=O_f A,\qquad U_f^\dagger=A^\dagger O_f,
\qquad O_f=U_f A^\dagger,
```

where $`A`$ is a known preparation circuit. These identities hold as full unitaries, not only on one initialized input. Thus either oracle can simulate the other with one query and known gates. The construction accounts for controls, work registers, and finite gate precision; it assumes no free QRAM or precomputed description of the unknown image.

## From a classical sampler to a coherent oracle

Let $`P`$ be a row-stochastic matrix. Classical two-step probabilities add over intermediate states:

```math
(P^2)_{xy}=\sum_z P_{xz}P_{zy}.
```

Two coherent row queries instead produce a state of the form

```math
|x\rangle
\sum_{z,y}\sqrt{P_{xz}P_{zy}}\,|z\rangle|y\rangle.
```

Measuring only the endpoint $`y`$ gives the correct two-step probability. A clean powered row requires the different state

```math
|x\rangle
\sum_y\sqrt{(P^2)_{xy}}\,|y\rangle|0\rangle_{\mathrm{work}}.
```

The first expression keeps a record of which intermediate state led to each endpoint. Removing that record while preserving all endpoint amplitudes is an extra coherent operation.

Childs's §1.4 explains why computational history can obstruct interference and how inverse circuits can uncompute suitable scratch registers. Applying an inverse here without further structure generally undoes part of the desired endpoint computation as well. The endpoint is not ordinarily enough information to reconstruct the particular intermediate branch. A quantum circuit may discard the history, but the remaining endpoint can then be a mixed state. The following example makes this distinction explicit without requiring a general theory of quantum channels.

## A complete small example

Take $`N=2`$, $`M=4`$, and $`f(0)=0,\ f(1)=2`$. **These dimensions are a teaching example, outside the lower-bound family's requirements $`N\ge4`$ and $`M=N^4`$.** They establish no asymptotic lower bound.

A chain state is a pair $`(x,y)`$ with $`x\in\{0,1\}`$ and $`y\in\{0,1,2,3\}`$. To take one step, draw a fresh first coordinate uniformly and draw the second coordinate from

```math
K_0=\frac18(5,1,1,1),
\qquad
K_1=\frac18(1,1,5,1).
```

Thus $`P((x,y),(z,w))=K_x(w)/2`$. The old second coordinate is unused. After the first step, the first coordinate is uniform, so the final second coordinate after the next step has distribution

```math
q=\frac{K_0+K_1}{2}=\frac18(3,1,3,1).
```

The final first coordinate is another independent uniform draw. Consequently every row of $`P^2`$ is $`\pi(a,b)=q(b)/2`$. This distribution is stationary: if the first coordinate is uniform, one further step produces the same pair of marginal distributions.

The relevant row states and desired endpoint quantum sample are

```math
\begin{aligned}
|\chi_0\rangle
&=\frac{\sqrt5|0\rangle+|1\rangle+|2\rangle+|3\rangle}{\sqrt8},\\
|\chi_2\rangle
&=\frac{|0\rangle+|1\rangle+\sqrt5|2\rangle+|3\rangle}{\sqrt8},\\
|q\rangle
&=\frac{\sqrt3|0\rangle+|1\rangle+\sqrt3|2\rangle+|3\rangle}{\sqrt8}.
\end{aligned}
```

For a fixed initial state, the two-query history contains the following factor involving the intermediate first coordinate $`z`$ and the final second coordinate $`b`$:

```math
\frac{|0\rangle_z|\chi_0\rangle_b
+|1\rangle_z|\chi_2\rangle_b}{\sqrt2}.
```

The other newly created registers factor from this expression: the intermediate second coordinate has the initial row's state, and the final first coordinate is uniform. Ignoring $`z`$ leaves the weighted average of the two endpoint pure-state projectors,

```math
\rho_b=\frac12|\chi_0\rangle\langle\chi_0|
+\frac12|\chi_2\rangle\langle\chi_2|.
```

The diagonal of $`\rho_b`$ is exactly $`q`$. Therefore computational-basis measurements cannot distinguish this output from $`|q\rangle`$. Its coherence is different: the matrix entry between labels $`0`$ and $`2`$ is $`\sqrt5/8`$, whereas that entry in $`|q\rangle\langle q|`$ is $`3/8`$.

This difference has a direct measurement consequence. For the known vector

```math
|-_{02}\rangle=\frac{|0\rangle-|2\rangle}{\sqrt2},
```

the two probabilities are

```math
\langle-_{02}|\rho_b|-_{02}\rangle
=\frac{3-\sqrt5}{8}>0,
\qquad
|\langle-_{02}|q\rangle|^2=0.
```

The history retains information about which image label received the larger amplitude. Discarding that record removes the interference needed for the pure positive-amplitude endpoint state. This is the concrete step that ordinary marginalization does not implement.

## From reflections to the query separation

### What the walk construction supplies

For any row-stochastic $`P`$, the map

```math
V_P|x\rangle=|x\rangle\sum_y\sqrt{P_{xy}}\,|y\rangle
```

is an isometry. Each row state is normalized, and distinct source labels make the images orthogonal. With $`S`$ swapping the two registers, the Chapter 18 construction becomes

```math
R_P=2V_PV_P^\dagger-I,\qquad
W_P=S R_P,\qquad
V_P^\dagger S V_P=D(P).
```

These equations connect a clean row circuit to a reflection, walk, and discriminant encoding. If a row unitary is available, its inverse and a known reflection about initialized work can implement the row-subspace reflection. This is a circuit construction from an available resource.

Theorem 18.1 relates the spectrum of this walk to that of $`D(P)`$. For a general nonreversible chain it does **not** identify the positive stationary quantum sample as a unit-eigenvalue eigenvector of the flat discriminant. Reversibility supplies that additional identification. Indeed, the hard one-step chain below has a stationary distribution but $`\|D(P_f)\|<1`$; its two-step discriminant has eigenvalue one. Availability and spectral analysis of the powered object are separate questions.

### The family used by the theorem

Now use the actual asymptotic family: $`N=2^n\ge4`$, $`M=N^4`$, and an unknown injection $`f:[N]\to[M]`$. Define

```math
K_x(w)=\frac12\mathbf1_{\{w=f(x)\}}+\frac1{2M},
\qquad
P_f((x,y),(z,w))=\frac1N K_x(w).
```

Every transition has positive probability. The same averaging calculation as in the toy example gives

```math
P_f^2=\mathbf1\pi_f,\qquad
\pi_f(z,w)=\frac1Nq_f(w),\qquad
q_f(w)=\frac1{2M}+
\frac{\mathbf1_{\{w\in\mathrm{im}f\}}}{2N}.
```

The chain therefore reaches stationarity in exactly two steps from every initial state. A single supplied row query still costs one evaluation of $`f`$, because it only has to prepare a known background state translated by $`f(x)`$.

The stationary quantum sample is $`|u_N\rangle|q_f\rangle`$, where $`|u_L\rangle=L^{-1/2}\sum_{x\in[L]}|x\rangle`$. Define the unknown image state and a known ratio by

```math
|\psi_f\rangle=\frac1{\sqrt N}\sum_x|f(x)\rangle,
\qquad s=\frac NM.
```

Direct comparison of amplitudes inside and outside the image gives

```math
|q_f\rangle=c|\psi_f\rangle+d|u_M\rangle,
\qquad
c=\frac{\sqrt{1+s}-\sqrt s}{\sqrt2},
\quad d=\frac1{\sqrt2}.
```

This identity explains why coherent stationarity contains information beyond an ordinary stationary sample.

### Where the lower bound enters

Let $`H=I-|u_M\rangle\langle u_M|`$ be a known projector. Since $`\langle u_M|\psi_f\rangle=\sqrt s`$,

```math
H|q_f\rangle=c\bigl(|\psi_f\rangle-\sqrt s\,|u_M\rangle\bigr).
```

This outcome has constant probability. Its normalized state has squared overlap $`1-s`$ with $`|\psi_f\rangle`$, which is at least $`63/64`$ for this family. A sufficiently accurate stationary quantum sample would consequently yield a bounded-error image state using only constant additional overhead.

The required hardness statement is **Lindzey and Rosmanis's noncoherent index-erasure theorem**, identified precisely in [the inherited theorem section](../science/lower-bounds.md#inherited-hardness-theorem) and [related work](../references/related-work.md#index-erasure). For injective functions with sufficiently large output range, it gives an $`\Omega(\sqrt N)`$ quantum query lower bound for producing the image state even when arbitrary function-dependent garbage is allowed. The range $`M=N^4`$ satisfies its hypothesis. Childs's adversary-method chapter is useful background, but this specific research theorem is an additional proof dependency.

The [local reductions](../science/lower-bounds.md) transfer that theorem to five targets: a stationary quantum sample, a clean two-step row, its Szegedy row reflection, a stationary-state reflection, and a normalization-one block encoding of $`D(P_f^2)`$. The operator lower bounds require their own reductions; they do not follow merely because one possible state-preparation implementation is expensive.

For example, put $`|\omega\rangle=|u_N\rangle|u_M\rangle`$ and $`\alpha=\langle\pi_f|\omega\rangle`$. Its known warm overlap obeys $`\alpha^2\ge1/2`$. A stationary reflection gives

```math
(I\otimes H)(2|\pi_f\rangle\langle\pi_f|-I)|\omega\rangle
=2\alpha|u_N\rangle H|q_f\rangle.
```

Thus one reflection followed by a known measurement already exposes the same hard image component with constant probability. Since every powered row is $`|\pi_f\rangle`$, the ideal powered row reflection is $`I\otimes(2|\pi_f\rangle\langle\pi_f|-I)`$, so the argument also applies directly to it.

The [full proof](../science/lower-bounds.md#bounded-repetition-and-the-sources-error-convention) keeps the inherited theorem's fidelity convention and bounds the repetition count. The main result uses fixed target error $`10^{-3}`$, with trace-distance error for states and uniform operator guarantees for clean oracle tasks; this bridge is not substituting exact-state intuition for those error estimates.

### Why the square-root upper bound matches

One evaluation prepares $`N^{-1/2}\sum_x|x,f(x)\rangle`$. Projecting the index register onto its known uniform state gives

```math
\bigl(|u_N\rangle\langle u_N|\otimes I\bigr)
\frac1{\sqrt N}\sum_x|x,f(x)\rangle
=\frac1{\sqrt N}|u_N\rangle|\psi_f\rangle.
```

The success probability is exactly $`1/N`$. Amplitude amplification raises it to constant probability in $`O(\sqrt N)`$ queries. For clean reusable unitaries, the project uses known-probability exact amplification, with explicitly chosen dilution and phases, to return ancillary registers to their required states. Section 19.3 provides the amplification viewpoint; the precise exact construction is spelled out in [upper bounds](../science/upper-bounds.md#exact-amplification-with-an-explicit-query-cap), using the primary amplitude-amplification result cited in [related work](../references/related-work.md#amplitude-amplification).

A further controlled linear combination of the image state and the known uniform state prepares $`|q_f\rangle`$ with constant additional amplification overhead. Conjugation by this clean preparation supplies the reflection and block-encoding targets. This establishes matching $`\Theta(\sqrt N)`$ query complexity in the stated row-unitary model. It is not a matching upper bound in a weaker reflection-only input model. Gate synthesis, ancillary cleanup, and precision remain part of the [resource account](../science/resources.md).

## What powers and what does not

Section 29.1 describes a block encoding: a matrix appears as a specified block of a larger unitary. In the project's normalization-one case,

```math
(\langle0|_{\mathrm{anc}}\otimes I)\,
U\,(|0\rangle_{\mathrm{anc}}\otimes I)=D.
```

More generally the block can be $`D/\alpha`$; the normalization $`\alpha`$ affects the algorithm's success and cost. Projecting the ancillas is an operation with a success probability, not a free way to apply $`D`$ as a unitary.

Block-encoding products and polynomial transformations act on the matrix actually encoded. Starting with $`D(P)`$ therefore gives ways to access $`D(P)^j`$. In general this is a different matrix from

```math
D(P^j)_{xy}=\sqrt{(P^j)_{xy}(P^j)_{yx}}.
```

The source of the difference can be read directly from paths. Let $`H_j`$ coherently retain all $`j`$ transitions, and let $`\mathsf R_j`$ reverse all path registers. Then

```math
H_j^\dagger\mathsf R_jH_j=D(P)^j.
```

For fixed endpoints, let $`b_{xy}(h)`$ be the conditional probability of an internal path $`h`$, and let $`\bar b_{yx}(h)`$ be the conditional probability of the reversed path from $`y`$ to $`x`$, also using the same kernel $`P`$. The [path expansion](../science/bridge-composition.md#2-whole-path-compression) gives

```math
[D(P)^j]_{xy}
=D(P^j)_{xy}
\sum_h\sqrt{b_{xy}(h)\bar b_{yx}(h)}.
```

The sum is the affinity of two probability distributions, so it lies between zero and one. The quantum compression compares compatible individual paths before adding them; the powered kernel first adds path probabilities. Equality requires the relevant conditional bridge distributions to agree.

This is not only a possible small approximation issue. For the hard family,

```math
\|D(P_f^2)-D(P_f)^2\|\ge\frac{135}{256}.
```

The [construction](../science/construction.md#a-constant-operator-gap-between-the-two-quantum-powers) proves this constant operator-norm gap. For a strictly positive kernel, the [two-step converse](../science/bridge-composition.md#3-an-exact-converse-at-two-steps) further proves that equality $`D(P^2)=D(P)^2`$ holds exactly when the kernel is reversible. The positivity hypothesis matters.

There is a valid alternative matrix whose powers do compose:

```math
\mathcal D(P)=\mathrm{diag}(\sqrt\pi)\,P\,
\mathrm{diag}(\sqrt\pi)^{-1},
\qquad
\mathcal D(P)^j=\mathcal D(P^j).
```

This identity is an ordinary similarity transformation for a positive stationary law. For nonreversible chains, implementing it by forward and time-reversed row access is an additional input model. The stochastic reverse kernel is

```math
P^\star(y,x)=\frac{\pi(x)P(x,y)}{\pi(y)}.
```

It describes a conditional distribution under stationarity. It is different from the inverse of a row-preparation unitary, which reverses a specified circuit on its registers. In the hard family, a clean reverse row itself contains the hard $`|q_f\rangle`$ factor, whereas $`U_f^\dagger`$ costs one query. The [reverse-access derivation](../science/construction.md#stochastic-time-reversal-is-an-additional-resource) makes this distinction explicit. The conditional spectral results discussed in [interpretation](../science/interpretation.md) remain conditional on their supplied coherent operations.

## A positive bridge compiler

The history calculation also identifies a sufficient extra resource. Regrouping the path registers by source and endpoint yields

```math
H_j|x\rangle
=|x\rangle\sum_y\sqrt{(P^j)_{xy}}\,
|y\rangle|\beta_{xy}\rangle,
\qquad
|\beta_{xy}\rangle=\sum_h\sqrt{b_{xy}(h)}\,|h\rangle.
```

Suppose a source-and-endpoint-controlled full unitary prepares each of these conditional bridge states, with their specified phases and clean work:

```math
B_j|x,y\rangle|0\rangle
=|x,y\rangle|\beta_{xy}\rangle.
```

Then applying $`B_j^\dagger`$ to the history unprepares the bridge and leaves a clean powered row. If the bridge operation costs $`g_j`$, the compiled forward operation costs $`j`$ base row queries plus $`g_j`$. The inverse and controls must be supported and charged as well. This is the [positive compiler theorem](../science/bridge-composition.md#5-a-compiler-from-conditional-bridge-unpreparation); it specifies the missing operation rather than treating it as free.

Approximation needs a coherent promise. The [error theorem](../science/bridge-composition.md#6-approximation-that-composes-coherently) assumes a uniform vector-norm error at most $`\delta`$ for the phase-fixed conditional bridge states, including all retained work. It obtains one fixed exact clean-row completion within operator norm $`\delta`$ of the actual compiled unitary, with the same guarantee for its inverse and controls. Replacing $`q`$ such calls then contributes at most $`q\delta`$ to the final vector error. Fidelity alone would miss endpoint-dependent phases, which can spoil interference between different endpoints.

A separate [affinity criterion](../science/bridge-composition.md#4-a-quantitative-block-encoding-criterion) says that uniformly high forward/reversed bridge affinity makes the cheap history compression close to $`D(P^j)`$ in operator norm. That criterion concerns the encoded matrix. It does not, by itself, clean the endpoint row.

## Scope and evidence

The pieces have distinct provenance.

| Kind of input | Role |
|---|---|
| Background in the selected Childs notes | Registers and amplitudes, reversible evaluation, query accounting, walk reflections, spectral mapping, amplitude amplification, block encodings, and circuit approximation. |
| Local definitions and derivations in this repository | The positive two-step chain and its full oracle completion; reduction of its coherent targets to index erasure; explicit matching constructions; the reverse-row and norm-gap calculations; the conditional-bridge identity, compiler, and error theorem; the early-reversibility product. |
| Imported primary research results | Lindzey–Rosmanis noncoherent index-erasure hardness, exact amplitude amplification, and the other explicitly cited implementation tools. Their assumptions are preserved in the [source index](../references/source-index.md) and [related work](../references/related-work.md). |

The result concerns specified coherent primitives. An ordinary stationary sample for this family is cheap: choose either a uniform output label or the image of a uniformly sampled input, each with probability one half, and independently draw the first coordinate uniformly. Scalar expectation-estimation methods may also retain history. Neither task requires the clean stationary quantum sample.

The [early-reversibility product](../science/early-reversibility.md) tensors the hard chain with a known two-state chain that flips with probability $`1/T`$. The square of the product is already exactly reversible, while worst-case classical mixing takes $`\Theta(T)`$ steps. Choosing $`N=2^n`$ and $`T=n\ge4`$ gives mixing of order $`n`$ but coherent target complexity of order $`2^{n/2}`$. The hard cost is the endpoint-coherence requirement: it persists despite favorable powered spectral properties and a known uniform state with squared stationary overlap at least one half.

That example does not establish a product lower bound multiplying the hard cost by the slow factor's mixing cost, and the uniform warm source already has the slow coordinate stationary. Its purpose is to show why early reversibility alone does not bound the cost of constructing the coherent powered operations from the original forward oracle.

The [main theorem](../science/model.md#main-theorem) fixes the access and error guarantees; the linked science files contain the proofs. The [verification notes](../verification/README.md) explain the finite-dimensional checks and their limits. Those checks support the identities and numerical implementations, while the imported query lower bound and the local reductions establish the asymptotic separation.
