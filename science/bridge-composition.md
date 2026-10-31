# Bridge conditions for coherent Markov powering

This note separates two useful constructions. Retaining a quantum walk's complete history gives a cheap compression of a power of the one-step flat discriminant. Erasing a conditional history gives a clean row oracle for a power of the transition matrix. The second operation requires an additional coherent resource, whose cost and approximation guarantees are stated explicitly below.

## 1. Conventions and access

Let $`P`$ be a row-stochastic matrix on a finite set $`\Omega`$. Its flat discriminant is

```math
D(P)_{xy}=\sqrt{P_{xy}P_{yx}}.
```

The available row oracle is one specified source-controlled unitary $`U_P`$ satisfying

```math
U_P|x\rangle|0\rangle
=|x\rangle\sum_y\sqrt{P_{xy}}\,|y\rangle.
```

All phases in this promise are fixed. Calls to its actual inverse, and any controlled calls used by an algorithm, are charged. Source control means that the oracle preserves the source register on every input, including inputs outside the initialized-ancilla subspace.

Applying the row oracle successively to fresh registers constructs a history isometry with $`j`$ row-oracle calls:

```math
H_j|x_0\rangle
=\sum_{x_1,\ldots,x_j}
\sqrt{\prod_{k=0}^{j-1}P_{x_kx_{k+1}}}
\,|x_0,x_1,\ldots,x_j\rangle.
```

The circuit implementing this isometry is a full unitary, with the remaining registers initialized to zero. Its inverse is the reverse circuit using the same row-oracle completion.

## 2. Whole-path compression

Let $`\mathsf R_j`$ reverse the order of all $`j+1`$ path registers. Direct expansion gives

```math
H_j^\dagger\mathsf R_jH_j=D(P)^j.
```

Indeed, an entry of this compression sums, over paths from $`x`$ to $`y`$, the geometric mean of that path's probability and the probability of the reversed path under the same kernel. It is therefore the ordinary matrix product of $`j`$ copies of $`D(P)`$.

To compare this with $`D(P^j)`$, fix endpoints with $`(P^j)_{xy}(P^j)_{yx}>0`$. For an internal path $`h=(x_1,\ldots,x_{j-1})`$, define

```math
b_{xy}(h)
=\frac{P_{xx_1}P_{x_1x_2}\cdots P_{x_{j-1}y}}{(P^j)_{xy}},
\qquad
\bar b_{yx}(h)
=\frac{P_{yx_{j-1}}\cdots P_{x_2x_1}P_{x_1x}}{(P^j)_{yx}}.
```

These are the conditional forward bridge distribution and the reversed conditional bridge distribution, both formed from $`P`$. Their Bhattacharyya affinity is

```math
\mathcal B^{(j)}_{xy}
=\sum_h\sqrt{b_{xy}(h)\bar b_{yx}(h)}.
```

Consequently,

```math
[D(P)^j]_{xy}
=D(P^j)_{xy}\,\mathcal B^{(j)}_{xy},
\qquad 0\le\mathcal B^{(j)}_{xy}\le1.
```

If the discriminant entry is zero, both sides are zero; set the corresponding affinity to one by convention. Equality of a nonzero entry holds precisely when the two bridge distributions agree. The identity and its equality criterion follow from path expansion and the equality condition in Cauchy–Schwarz. They are elementary probability and linear-algebra facts.

This formula concerns the flat discriminant. The curved discriminant using an independently supplied time-reversed kernel has different access requirements; its stationary-weight factors telescope under multiplication.

## 3. An exact converse at two steps

**Proposition.** If every entry of $`P`$ is strictly positive, the following statements are equivalent:

1. $`D(P^2)=D(P)^2`$.
2. All forward and reversed conditional two-step bridges agree.
3. $`P`$ satisfies detailed balance with respect to a positive stationary distribution.

Under these conditions, $`D(P^j)=D(P)^j`$ for every positive integer $`j`$.

**Proof.** The bridge identity proves the equivalence of the first two statements. Put $`r_{xy}=P_{xy}/P_{yx}`$. Bridge equality says

```math
\frac{P_{xz}P_{zy}}{P_{yz}P_{zx}}
=\frac{(P^2)_{xy}}{(P^2)_{yx}}
\quad\text{for every }x,y,z.
```

The choice $`z=x`$ is permitted by strict positivity and makes the right side equal to $`r_{xy}`$. Hence

```math
r_{xz}r_{zy}=r_{xy}.
```

Fix a reference state $`o`$ and let $`a_x=r_{ox}`$. Taking $`z=o`$ gives $`r_{xy}=a_y/a_x`$. Thus $`\pi_x=a_x/\sum_z a_z`$ satisfies $`\pi_xP_{xy}=\pi_yP_{yx}`$. Detailed balance also implies stationarity. Conversely, for a reversible kernel,

```math
D(P)=\operatorname{diag}(\sqrt\pi)\,P\,
\operatorname{diag}(\sqrt\pi)^{-1}.
```

The same relation holds for every power of $`P`$, proving the converse and the last assertion.

Strict positivity is substantive. For a lazy directed five-cycle, $`P=(I+C)/2`$, both $`D(P)^2`$ and $`D(P^2)`$ equal $`I/4`$, although the chain is irreducible, aperiodic and nonreversible. Sparse supports can prevent the two-step comparison from detecting circulation.

## 4. A quantitative block-encoding criterion

**Proposition.** Suppose every relevant conditional bridge affinity obeys

```math
\mathcal B^{(j)}_{xy}\ge1-\varepsilon.
```

Then

```math
\bigl\|D(P^j)-D(P)^j\bigr\|
\le\varepsilon\,\|D(P^j)\|
\le\varepsilon.
```

**Proof.** Write $`A=D(P^j)`$ and $`E=A-D(P)^j`$. These are symmetric matrices, and entrywise $`0\le E\le\varepsilon A`$. For any vector $`v`$,

```math
|v^\dagger Ev|
\le |v|^\top E|v|
\le\varepsilon |v|^\top A|v|
\le\varepsilon\|A\|\,\|v\|^2.
```

For any row-stochastic kernel $`R`$, the inequality

```math
2\sqrt{R_{xy}R_{yx}}\,|v_x|\,|v_y|
\le R_{xy}|v_x|^2+R_{yx}|v_y|^2
```

implies $`\|D(R)\|\le1`$. Apply it to $`R=P^j`$.

Thus the cheap history circuit supplies an approximate normalized block encoding of $`D(P^j)`$ whenever the stated uniform bridge promise is available. This conclusion concerns the operator encoded by the history circuit; it does not assert that its endpoint row amplitudes have been cleaned. Verifying the bridge promise can itself be costly. A subsequent spectral algorithm must charge the approximation accuracy it needs relative to its own gap and error parameters.

## 5. A compiler from conditional bridge unpreparation

For $`(P^j)_{xy}>0`$, let

```math
|\beta_{xy}\rangle
=\sum_h\sqrt{b_{xy}(h)}\,|h\rangle.
```

Assume a single source-and-endpoint-controlled unitary $`B_j`$ is available with the phase-fixed promise

```math
B_j|x,y\rangle|0\rangle
=|x,y\rangle|\beta_{xy}\rangle.
```

Additional work registers may be included, but their required final state is also fixed to zero. The cost of producing this unitary, its controls and its inverse is part of the input model. No bridge samples, endpoint-conditioned advice or random-access data structure are supplied for free.

Regrouping the history registers gives

```math
H_j|x\rangle
=|x\rangle\sum_y\sqrt{(P^j)_{xy}}
\,|y\rangle|\beta_{xy}\rangle.
```

Applying $`B_j^\dagger`$ therefore yields

```math
|x\rangle\sum_y\sqrt{(P^j)_{xy}}
\,|y\rangle|0\rangle.
```

The full circuit $`U_j=B_j^\dagger\mathsf H_j`$, where $`\mathsf H_j`$ is the unitary history circuit, is one consistent clean-row completion. Its inverse is exactly $`\mathsf H_j^\dagger B_j`$. Its forward cost is $`j`$ calls to the base row oracle plus the charged bridge-unpreparation cost. The inverse has the corresponding reverse cost.

This gives a sufficient extra resource for clean endpoint powering. In the hard family developed in this project, a sufficiently accurate two-step bridge compiler must inherit the index-erasure query lower bound, since it would otherwise prepare the hard clean stationary state cheaply.

## 6. Approximation that composes coherently

Suppose the implementation is a source-and-endpoint-controlled full unitary $`\widetilde B_j`$ with

```math
\sup_{x,y:(P^j)_{xy}>0}
\bigl\|\widetilde B_{j,xy}|0\rangle
-|\beta_{xy}\rangle\bigr\|\le\delta.
```

This is a vector-norm statement with the specified positive-amplitude phase, including clean work registers. Pure-state fidelity or closeness after discarding work registers does not provide this promise.

Let $`\widetilde U_j=\widetilde B_j^\dagger\mathsf H_j`$ be the actual compiled full unitary. For each source $`x`$, its initialized-input column differs from the ideal clean powered-row column by at most $`\delta`$: the squared error is

```math
\sum_y(P^j)_{xy}
\bigl\|\widetilde B_{j,xy}^\dagger
|\beta_{xy}\rangle-|0\rangle\bigr\|^2
\le\delta^2.
```

The orthogonal source and endpoint labels prevent errors from accumulating across distinct endpoints. If $`J`$ initializes the ancillary registers and $`V_j`$ is the ideal clean row isometry, then

```math
\|\widetilde U_jJ-V_j\|\le\delta.
```

This is an operator-norm bound, so it holds for every coherent source superposition entangled with an arbitrary reference register. For the corresponding isometric channels, it implies an unhalved diamond-norm error at most $`2\delta`$.

### One fixed exact completion, including its inverse

The previous statement can be strengthened without asserting closeness to an arbitrarily selected oracle completion.

**Lemma.** There is one exact, source-controlled clean-row completion $`U_j^{\mathrm{exact}}`$ such that

```math
\|\widetilde U_j-U_j^{\mathrm{exact}}\|\le\delta,
\qquad
\|\widetilde U_j^\dagger-(U_j^{\mathrm{exact}})^\dagger\|\le\delta.
```

**Proof.** Work independently in each preserved source block. Let $`a`$ be the actual initialized-input output and $`b`$ its required clean-row vector. Both are unit vectors. Set $`z=\langle a|b\rangle`$, $`s=\sqrt{1-|z|^2}`$, and, when $`s>0`$, $`e=(b-za)/s`$. On the span with orthonormal basis $`(a,e)`$, the matrix

```math
R=\begin{pmatrix}z&-s\\s&\overline z\end{pmatrix}
```

is unitary, sends $`a`$ to $`b`$, and satisfies

```math
\|R-I\|=\sqrt{2-2\operatorname{Re}z}=\|a-b\|.
```

Extend it by the identity on the orthogonal complement. When $`s=0`$, use the phase $`z`$ on $`a`$ and the identity elsewhere. The direct sum of these correcting rotations, multiplied on the left of $`\widetilde U_j`$, is the claimed exact completion. Its distance is the maximum column error over source blocks. Taking adjoints preserves that distance.

This exact comparison unitary is fixed once the compiled circuit and kernel are fixed. It works simultaneously for every input, every reference, and every later choice of forward, inverse or controlled calls. A circuit making at most $`q`$ such calls has vector error at most $`q\delta`$, or channel diamond-norm error at most $`2q\delta`$, relative to this same completion. This follows from the usual telescoping hybrid bound. The comparison unitary's existence does not provide a free implementation of its correcting rotations.

Two exact row completions can agree on all initialized columns and still be distance two apart on other inputs. Consequently the lemma does not establish closeness to a separately prescribed full completion. An algorithm using only the clean-row promise must be correct for the allowed completion, or explicitly use the construction just given.

### Why phases and retained work matter

For a uniform two-state kernel, each two-step conditional bridge is the same uniform vector. A putative bridge preparer can prepare that vector with an endpoint-dependent phase $`(-1)^y`$. Every bridge density matrix and fidelity is then exactly correct, but unpreparation changes the clean endpoint state from $`|+\rangle`$ to $`|-\rangle`$. The endpoint fidelity becomes zero. This is why a phase-fixed coherent-unitary guarantee is necessary.

## 7. Verification and scope

The accompanying NumPy checks independently compare enumerated paths, matrix powers, bridge affinities and complete finite-dimensional circuits. They include reversible and nonreversible controls, the sparse-support converse counterexample, source-reference inputs, full inverses, a fixed exact completion, and an endpoint-dependent phase failure.

The checks support the algebra and circuit implementation at finite size. They do not establish the inherited asymptotic query lower bound. The relevant primary references for the surrounding access models and lower-bound mechanism are:

- Claudon, Piquemal and Monmarché, [*Quantum speedup for nonreversible Markov chains*](https://doi.org/10.1038/s41467-025-65761-5), with [arXiv version 2](https://arxiv.org/abs/2501.05868v2).
- Lindzey and Rosmanis, [*A tight lower bound for non-coherent index erasure*](https://www.rintonpress.com/xxqic22/qic-22-78/0594-0626.pdf), *Quantum Information and Computation* **22**, 594–626 (2022).
