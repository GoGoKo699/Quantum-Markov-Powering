# Verification of clean Markov powering

Run the deterministic checks with Python and NumPy:

```bash
python verification/verify_markov_powering.py --output verification/results.json
```

The script needs no network connection and no data files. It exits nonzero if any check fails and writes a machine-readable report when `--output` is supplied. The recorded run used Python 3.12.14 and NumPy 2.3.5. The absolute numerical tolerance is `2e-11`; the random seed is fixed in the source.

## Claims covered

| Check | Risk it addresses |
| --- | --- |
| Full one-query completion | Constructs the known prefix-controlled background preparation and verifies the entire resulting unitary, its inverse identity and initialized positive-amplitude rows. An entangled reference is included. A different completion with the same row promise is distance two away. |
| Exact index erasure and LCU | Executes the diluted Grover construction, full preparation and inverse, coherent linear combination, and final cleanup. Checks vector phases and every garbage register. A deliberately wrong controlled-branch phase fails. |
| Bounded-error postselection | Checks success-probability continuity and explicit conditional trace-distance bounds for pure and mixed perturbations. |
| Base and product chains | Checks exact two-step mixing, one-step mixing from the uniform warm start, two-warmness, powered reversibility and product spectra. Measures the flat-composition discrepancy and compares it to an independent Rayleigh/norm witness. |
| Bridge identity | Compares direct history compression, independently computed matrix powers and enumerated conditional bridge affinities. Includes reversible, nonreversible and sparse-support controls. |
| Coherent compiler | Tests a single approximate full bridge unitary and its inverse, coherent source-reference inputs, one fixed exact completion, and forward/inverse composition with intervening source mixing. A phase-blind bridge guarantee can give zero endpoint fidelity. |

The finite diagnostics use several domain/range sizes. They test identities and circuits, not the inherited asymptotic query lower bound.

| Diagnostic | Dimensions | Relation to the asymptotic family |
| --- | --- | --- |
| Full oracle, base chain and product spectra | $`N=2,M=16`$ | Obeys $`M=N^4`$ algebraically, but is below the main theorem's stated $`N\ge4`$ range. Used only as a small matrix diagnostic. |
| Exact amplification and LCU | $`(N,M)=(2,16),(4,32),(8,128)`$ | The latter two do not obey $`M=N^4`$. The exact circuit identities apply to these injective-function instances as well. |
| Postselection perturbations | $`N=4,M=64`$ | Does not obey $`M=N^4`$. Tests the general trace-distance inequalities and projection formula. |
| Bridge identities and compiler | Three-state kernels; a five-state sparse control | General Markov examples, independent of the injection-family lower bound. |

In particular, the displayed finite-size flat-composition norm is not evidence that a finite instance satisfies an asymptotic complexity theorem. The lower bound follows from the analytic reduction on the growing family $`M=N^4`$ and the cited index-erasure theorem.

The amplitude-amplification checks use the constructive proof's explicit cap $`k=\lceil\sqrt N\rceil`$. The code conjugates the uniform-index good subspace by Hadamards so that the good index becomes the computational zero state. After the final index cleanup, this gives the same full preparation unitary. Query counts $`2k+1`$ and $`3(2k+1)`$ are included in the report.

## Explicit postselection constants

Use trace distance $`T(\rho,\sigma)=\tfrac12\|\rho-\sigma\|_1`$. Let a projection succeed with ideal probability $`p>0`$ and actual probability $`q`$, where $`T(\rho,\sigma)\le\epsilon<p`$. Then

```math
|p-q|\le\epsilon,
\qquad
T(\rho\mid\mathrm{success},\sigma\mid\mathrm{success})
\le\frac{\epsilon}{p}.
```

For completeness, let $`A=\Pi\rho\Pi`$ and $`B=\Pi\sigma\Pi`$. The measurement channel retaining the successful block and a single failure flag gives

```math
\|A-B\|_1+|p-q|\le2\epsilon.
```

Writing $`A/q-B/p=(A-B)/p+(1/q-1/p)A`$ proves the displayed conditional bound.

In the stationary-qsample reduction, $`p\ge7/32`$, and the ideal projected state has trace distance $`\sqrt{N/M}`$ from the index-erasure target. Thus the successful approximate output has trace distance at most

```math
\sqrt{N/M}+\frac{32}{7}\epsilon.
```

For $`M=N^4`$, $`N\ge16`$ and $`\epsilon\le10^{-3}`$, this is at most $`1/64+4/875<0.0202`$. Each attempt succeeds with probability at least $`871/4000`$. Thirty-two charged independent attempts leave failure probability at most $`e^{-871/125}<0.001`$; producing an arbitrary state after total failure therefore gives an unconditional trace error below $`0.022`$, and hence squared fidelity above $`0.978`$. This makes the small constant-error reduction explicit in the asymptotic range. The main lower-bound proof uses a direct fidelity estimate to cover all $`N\ge4`$. The asymptotic index-erasure theorem, rather than numerical checks, supplies the lower bound.

## Recorded findings

The complete values are in `results.json`. The finite-size hard chain gives

```math
\|D(P^2)-D(P)^2\|\simeq0.2966006261.
```

Its independent contraction lower bound is approximately `0.2815792395`, and the stationary-vector Rayleigh witness is approximately `0.2860345922`. This confirms an operator-level discrepancy rather than merely a mismatch between two implementations of the same formula.

For the positive three-state nonreversible control, the two-step flat discrepancy is approximately `0.4324317265`; the uniform bridge-affinity norm bound is approximately `0.5317028930`. Reversible controls agree to floating-point precision. The lazy directed five-cycle shows why strict positivity is needed for the two-step converse.

The exact index-erasure and LCU constructions return the required vector, including all cleared registers and its relative phase, within `7e-15` in the recorded examples. For the approximate bridge compiler, the largest bridge error is approximately `0.11178`, the distance to the constructed exact full-unitary completion is approximately `0.07417`, and the source-reference error is approximately `0.05931`. These illustrate the uniform bound proved in the bridge-composition note.

## Limits

These checks are targeted finite-dimensional safeguards. They do not establish asymptotic optimality, replace the index-erasure lower-bound proof, establish practical gate counts, or certify novelty. Exact real rotations and square roots are represented in floating-point arithmetic here; a finite gate-synthesis analysis must charge its own precision. The script deliberately tests failure modes involving oracle completion, phase control, retained work and sparse support because those can change the mathematical claim.
