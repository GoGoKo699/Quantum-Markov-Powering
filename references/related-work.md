# Related work and inherited tools

This note identifies the results used by the construction and the nearby models that constrain its interpretation. It records a scoped literature comparison, not an exhaustive priority claim. The [source index](source-index.md) gives versions and reading locations; [interpretation](../science/interpretation.md) states the resulting scope of the separation.

## Index erasure

Nathan Lindzey and Ansis Rosmanis, [*A tight lower bound for non-coherent index erasure*](https://www.rintonpress.com/xxqic22/qic-22-78/0594-0626.pdf), *Quantum Information and Computation* **22**(7–8), 594–626 (2022), [doi:10.26421/QIC22.7-8-3](https://doi.org/10.26421/QIC22.7-8-3).

Theorem 1 is the external lower-bound input. For an injection $`f:[N]\to[M]`$, it gives bounded-error noncoherent query complexity $`\Theta(\sqrt N)`$ for preparing the uniform image state when $`M\ge N^{3+\epsilon}`$ for some fixed $`\epsilon>0`$. Our choice $`M=N^4`$ meets this hypothesis.

The error convention in their §2.2 is essential. If the full final state is $`|\Psi_f\rangle`$ and the desired target-register state is $`|F_f\rangle`$, the noncoherent requirement is

```math
\bigl\|(\langle F_f|\otimes I)|\Psi_f\rangle\bigr\|
=\max_{|g_f\rangle}\mathrm{Re}\langle F_f,g_f|\Psi_f\rangle
\ge\sqrt{1-\epsilon}.
```

Equivalently, the target reduced density matrix $`\rho_f`$ obeys $`\langle F_f|\rho_f|F_f\rangle\ge1-\epsilon`$. The garbage state may depend on $`f`$. Thus a reduction need not clean its work registers, and allowing intermediate measurements does not escape the lower bound after purification. The representation-theoretic index-erasure lower bound is inherited from this paper; the contribution here is the Markov-kernel embedding and the reductions from its clean resources.

## Amplitude amplification

Gilles Brassard, Peter Høyer, Michele Mosca, and Alain Tapp, [*Quantum Amplitude Amplification and Estimation*](https://arxiv.org/abs/quant-ph/0005055), *Contemporary Mathematics* **305**, 53–74 (2002), [doi:10.1090/conm/305/05215](https://doi.org/10.1090/conm/305/05215).

Theorem 4 and the dilution construction immediately preceding it supply exact amplification when the success probability is known. This gives the matching query upper bound from the image-state preparation with success probability $`1/N`$. The proof uses the actual preparation unitary, its inverse, and the success-subspace reflection. Those operations must be charged; an overlap bound alone does not supply them. Section 4 also provides the standard amplitude-estimation primitive relevant to the scalar-observable limitation discussed in [interpretation](../science/interpretation.md#ordinary-sampling-and-observables).

## Gate synthesis

Christopher M. Dawson and Michael A. Nielsen, [*The Solovay–Kitaev algorithm*](https://arxiv.org/abs/quant-ph/0505030v2), *Quantum Information and Computation* **6**(1), 81–95 (2006), [doi:10.26421/QIC6.1-6](https://doi.org/10.26421/QIC6.1-6).

The constructive synthesis result in §§2–4 supports approximating the explicit, known, constant-dimensional rotations used in the preparation and amplification circuits with a number of gates polynomial in the logarithm of inverse precision. It does not provide a method to prepare an arbitrary unknown marginal. The [finite-gate precision account](../science/resources.md#finite-gate-precision) separately budgets gate approximation error over the query algorithm.

## Block-encoding products

András Gilyén, Yuan Su, Guang Hao Low, and Nathan Wiebe, [*Quantum singular value transformation and beyond: exponential improvements for quantum matrix arithmetics*](https://arxiv.org/abs/1806.01838), STOC 2019, 193–204, [doi:10.1145/3313276.3316366](https://doi.org/10.1145/3313276.3316366).

Lemma 53 in the full arXiv paper gives a product construction with separate ancillas: block encodings of $`A`$ and $`B`$ yield an encoding of $`AB`$, with normalization multiplied and the stated errors added after scaling. Consequently an exact normalization-one encoding of $`A`$ gives an encoding of $`A^j`$ using $`j`$ calls. This is an algebraic matrix-product rule. It does not change the matrix being multiplied into an entrywise square-root transform of a classical matrix power.

For the flat discriminant $`D(P)_{xy}=\sqrt{P_{xy}P_{yx}}`$, the distinction is

```math
D(P)^j\ne D(P^j)
```

in general. The project's path-bridge identity makes the missing factor explicit. This distinction also prevents treating a block encoding of a retained-history marginal density matrix as a block encoding of its pure qsample projector.

## Quantum fast-forwarding

Simon Apers and Alain Sarlette, [*Quantum fast-forwarding: Markov chains and graph property testing*](https://ir.cwi.nl/pub/28721/28721.pdf), *Quantum Information and Computation* **19**(3–4), 181–213 (2019), [doi:10.26421/QIC19.3-4-1](https://doi.org/10.26421/QIC19.3-4-1).

Theorem 1 is stated in the setting of a finite reversible chain with an implemented quantum walk. Given an input state $`|v\rangle`$ and reflection access to it, the amplified algorithm prepares an approximation to

```math
\frac{D(P)^t|v\rangle}{\kappa},
\qquad
\kappa=\|D(P)^t|v\rangle\|>0.
```

Its expected cost includes $`O(\kappa^{-1}\sqrt{t\log(1/(\epsilon\kappa))})`$ walk steps and $`O(\kappa^{-1})`$ input-state reflections. Thus input access and output normalization remain substantive resources. See Theorem 1, Algorithm 1, and Theorems 2–3.

This is a normalized linear discriminant-power state, not generally the clean row qsample $`\sum_y\sqrt{P^t(x,y)}|y\rangle`$. For reversible $`P`$, the identity $`D(P^t)=D(P)^t`$ does hold. For generic nonreversible forward access it fails: powering the supplied discriminant therefore does not supply $`D(P^t)`$. This project addresses that latter interface gap. The paper's §4 also distinguishes irreversible transition dynamics from discriminant dynamics; its positive fast-forwarding theorem remains intact.

## Nonreversible spectral methods

Baptiste Claudon, Jean-Philip Piquemal, and Pierre Monmarché, [*Quantum speedup for nonreversible Markov chains*](https://pmc.ncbi.nlm.nih.gov/articles/PMC12663442/), *Nature Communications* **16**, 10732 (2025), [doi:10.1038/s41467-025-65761-5](https://doi.org/10.1038/s41467-025-65761-5).

The final article's Proposition 3 is conditional on access to the Szegedy operator of the kernel being transformed. Corollary 2 explicitly counts uses of the operator for a powered kernel. We preserve both statements. The discussion under “Reversibility on π-average” and “Summary” motivates the separate question of their cost in the original one-step access model. The [version reconciliation](source-index.md#published-supplement-reconciliation) distinguishes the final main-text Hellinger formulation from the supplement's total-variation formulation.

The curved-discriminant branch additionally uses a coherent oracle for the stationary time-reversed kernel. The linear cost of multiplying curved discriminants is compatible with ordinary block-encoding composition. The inverse of the forward preparation circuit is a different resource from access to the reversed Markov kernel. Our lower bound supplies only the former.

## Earlier quantum sampling requirements

Dorit Aharonov and Amnon Ta-Shma, [*Adiabatic Quantum State Generation*](https://www.cs.tau.ac.il/~amnon/Papers/AT.sicomp07.pdf), *SIAM Journal on Computing* **37**(1), 47–82 (2007), [doi:10.1137/060648829](https://doi.org/10.1137/060648829).

Their final-paper Definition 5.1 requires a reversible chain to be sparse and explicit, with efficiently approximable stationary probability ratios, to be “strongly samplable.” Theorem 1.3 in §5.4 uses a slowly varying sequence of such chains and a preparable initial qsample. Remark 5.1 explains why removing the ratio requirement would have consequences for graph-isomorphism qsampling. This is an important antecedent to any claim that classical sampling automatically supplies quantum samples.

Our powered kernel has dense rows whose stationary probabilities encode unknown image membership. It therefore does not satisfy those input assumptions merely because it mixes rapidly or is reversible. The present quantitative separation concerns a supplied clean forward-row oracle, rather than the sparse explicit transition and ratio model of that theorem.

## Quantum rejection sampling

Maris Ozols, Martin Roetteler, and Jérémie Roland, [*Quantum rejection sampling*](https://arxiv.org/abs/1103.2774v4), ITCS 2012, 290–308, [doi:10.1145/2090236.2090261](https://doi.org/10.1145/2090236.2090261). A journal version appeared in *ACM Transactions on Computation Theory* **5**(3) (2013), [doi:10.1145/2493252.2493256](https://doi.org/10.1145/2493252.2493256).

Definitions 2 and 4 specify amplitude conversion on the same labelled component states. In the former, initial and target amplitude vectors are fixed and known; the latter supplies a copy, a reflection, and known relative amplitude ratios. Theorem 1 characterizes the corresponding query cost. Neither model supplies unknown endpoint amplitudes or removes a hidden history register for free.

The warmness convention also matters. Our known source law obeys $`\nu\le2\pi`$. Rejection sampling from $`\nu`$ toward $`\pi`$ would instead use a bound on $`\pi/\nu`$ and access to the required ratios. Here the latter ratio is large on the hidden image. Thus the 2-warm start and constant qsample overlap do not instantiate an inexpensive rejection sampler.

## Quantized couplings

Kristan Temme and Pawel Wocjan, [*Quantized Markov Chain Couplings that Prepare Qsamples*](https://arxiv.org/abs/2504.02651v2), *Quantum* **9**, 1951 (2025), [doi:10.22331/q-2025-12-18-1951](https://doi.org/10.22331/q-2025-12-18-1951).

Lemma 16 and Theorem 18 relate convergence of a constructed quantum channel to classical coalescence. Theorem 20 separately assumes efficient access to random-map images, preimages, seed probabilities, and stationary ratios for implementing the quantized grand coupling. Its sparse implementation cost is part of the access model.

Our common-randomness grand coupling coalesces after two steps. That does not instantiate their implementation theorem: inverse-image information and stationary ratios are not provided by the forward oracle. The clean-output lower bound instead shows that implementing the resulting qsample-producing channel must carry a substantial cost in this restricted model. The example is consistent with both their convergence and implementation results.

## Foundational walk framework

Mario Szegedy, [*Quantum speed-up of Markov chain based algorithms*](https://ieeexplore.ieee.org/document/1366222/), FOCS 2004, 32–41, [doi:10.1109/FOCS.2004.53](https://doi.org/10.1109/FOCS.2004.53), introduced the reflection-based walk framework used here. The related longer preprint is titled [*Spectra of Quantized Walks and a √δε rule*](https://arxiv.org/abs/quant-ph/0401053). The source index distinguishes these titles. Our question concerns construction of the supplied reflection for a coarse-grained kernel; it does not dispute the spectral analysis once that reflection is available.
