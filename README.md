# Quantum Markov Powering

**When does a cheap one-step quantum transition remain cheap after two classical steps?** This project gives an explicit family for which classical mixing is complete after two steps, yet implementing the clean quantum transition of the squared chain costs substantially more than implementing one step.

For an injection $`f:[N]\to[M]`$ with $`N=2^n\ge4`$ and $`M=N^4`$, the chain is

```math
P_f((x,y),(z,w))
=\frac1N\left(\frac12\mathbf1_{\{w=f(x)\}}+\frac1{2M}\right).
```

It has full support and satisfies $`P_f^2=\mathbf1\pi_f`$. Its specified clean one-step row unitary, inverse, and controlled versions each use one ordinary evaluation of $`f`$. At fixed error $`10^{-3}`$, clean access to the square instead has tight worst-case query complexity $`\Theta(\sqrt N)`$.

The external lower-bound ingredient is [Lindzey and Rosmanis's noncoherent index-erasure theorem](references/related-work.md#index-erasure). The contribution developed here is its explicit Markov-chain embedding, reductions covering the relevant quantum operators, matching constructions, and the resulting account of coherent powering costs.

## Principal results

| Resource or property | Established result |
| --- | --- |
| Clean one-step row oracle | One evaluation query, with an explicit full unitary completion |
| Classical mixing | Exact stationarity after two steps from every source |
| Ordinary stationary sample | At most one evaluation query from a known uniform source |
| Stationary quantum sample and clean squared-chain row | $`\Theta(\sqrt N)`$ queries, allowing arbitrary final garbage for the state-output task |
| Stationary reflection and squared-chain Szegedy reflection | $`\Theta(\sqrt N)`$ queries under the stated clean-ancilla operator error |
| Normalization-one encoding of the squared-chain flat discriminant | $`\Theta(\sqrt N)`$ queries |
| Known warm source | Classical density bounded by twice stationarity; squared coherent overlap at least $`1/2`$ |

The [main theorem](science/model.md#main-theorem) fixes the supplied oracle, controls, accuracy conventions, and scope. The tight bounds use row-unitary access and its inverse; only the lower-bound transfer is asserted for reflection-only access. The [resource account](science/resources.md) charges known gates, workspace, precision, and all function-dependent preprocessing.

A [known two-state product](science/early-reversibility.md) makes exact reversibility occur after two steps while worst-case mixing takes $`\Theta(n)`$ steps on a $`5n+1`$-qubit state register. The coherent tasks still require $`\Theta(2^{n/2})`$ queries. The slow factor is independent and removable; this is an obstruction to a generic spectral-only implementation guarantee.

## What permits coherent powering?

Keeping every intermediate state produces a valid coherent trajectory. Its whole-path reversal compresses to $`D(P)^j`$, where $`D(P)_{xy}=\sqrt{P_{xy}P_{yx}}`$. The required flat discriminant for the powered chain is $`D(P^j)`$. These matrices differ by the overlap of forward and reversed conditional path distributions.

The [bridge analysis](science/bridge-composition.md) proves the exact identity, a uniform-affinity approximation bound, and a sufficient construction: a charged, phase-fixed coherent preparation of the conditional bridge can be inverted to erase the path. Its vector-error guarantee extends to coherent source inputs, one consistent full unitary completion, and later inverse or controlled calls. The bridge oracle's implementation cost is an additional resource.

## Reading routes

Start with the [scientific overview](science/README.md), or choose a direct route:

- **Understand the result:** [model and theorem](science/model.md) → [construction](science/construction.md) → [interpretation](science/interpretation.md).
- **Check the proof:** [lower bounds](science/lower-bounds.md) → [matching upper bounds](science/upper-bounds.md) → [resources](science/resources.md).
- **Study composition:** [early reversibility](science/early-reversibility.md) → [bridge conditions](science/bridge-composition.md).
- **Check attribution:** [related work](references/related-work.md), [versioned source index](references/source-index.md), and [BibTeX](references/references.bib).
- **Reproduce the finite checks:** [verification guide](verification/README.md) and [recorded results](verification/results.json).

The [LLM reading guide](llms.txt) maps questions to the authoritative pages.

## Reproduction

The deterministic finite checks use Python 3.12 and NumPy. From the repository root:

```bash
python -m pip install -r verification/requirements.txt
python verification/verify_markov_powering.py --output verification/results.json
```

The six checks cover full oracle completions, exact amplification and cleanup, postselection, chain spectra, path identities, and the approximate bridge compiler. They include negative controls for incorrect phases and oracle-completion assumptions. Small circuit examples verify the algebra; the asymptotic query lower bound comes from the cited theorem and the analytical reduction.

## Interpretation and boundaries

A pure square-root sample of a distribution is a stronger output than one classical draw. Ordinary samples and coherent sampling circuits retaining their history remain cheap in this family. Scalar amplitude estimation may use those circuits directly. The result therefore does not imply an advantage or disadvantage for every Monte Carlo task.

The conditional spectral guarantees of [Claudon, Piquemal, and Monmarché](references/related-work.md#nonreversible-spectral-methods) remain valid when their powered-kernel walk is supplied. Instantiating such a method from a one-step oracle must also charge the cost of implementing that powered walk. Access to a circuit's inverse is different from access to the stationary time-reversed Markov kernel. The [interpretation](science/interpretation.md) explains these distinctions and the prior-work comparison.

## Purpose and contact

This repository serves as a record of the work and a guide for the author’s self-directed learning. For discussion or potential collaboration, please contact Ruge Lin at [gogoko699@gmail.com](mailto:gogoko699@gmail.com).

## License

[MIT](LICENSE).
