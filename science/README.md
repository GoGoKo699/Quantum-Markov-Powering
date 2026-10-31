# Scientific overview

Classical temporal coarse-graining replaces a transition matrix $`P`$ by $`P^j`$. The corresponding quantum operation is not obtained simply by keeping a coherent record of $`j`$ transitions: a clean endpoint state must combine the amplitudes of all paths with the same endpoint. This project makes the cost of that operation explicit.

The central example is a strictly positive chain whose classical state is exactly stationary after two steps. Its supplied one-step clean row unitary costs one injection-evaluation query. Preparing its stationary quantum sample, or implementing its clean squared-chain row and associated operators, nevertheless costs $`\Theta(\sqrt N)`$ queries at fixed small error. A known slow factor puts the same obstruction in an early-reversibility regime. A conditional-bridge construction then states an additional coherent resource sufficient for clean powering.

## The connected account

| Page | Question answered |
| --- | --- |
| [Model and theorem](model.md) | What is supplied, what output is requested, and what exact query claim is proved? |
| [Construction](construction.md) | How can one clean transition be easy while two classical steps mix exactly? |
| [Lower bounds](lower-bounds.md) | How do states, reflections, and normalized encodings each solve noncoherent index erasure? |
| [Matching upper bounds](upper-bounds.md) | How does a bounded exact-amplification circuit prepare the target and its clean operators? |
| [Resources](resources.md) | What do controls, inverses, gates, ancillas, and finite precision cost? |
| [Early reversibility](early-reversibility.md) | Why do a favorable powered spectrum and a constant warm overlap leave the access obstruction intact? |
| [Bridge composition](bridge-composition.md) | What does a retained trajectory actually encode, and what extra coherent access erases it? |
| [Interpretation](interpretation.md) | Which inference about powered spectral methods changes, and which sampling tasks and prior theorems remain unaffected? |

Read the first five pages for the complete theorem and proof. The final three connect the theorem to composition, spectral methods, and operational scope. [Related work](../references/related-work.md) identifies inherited ingredients and neighboring access models; the [source index](../references/source-index.md) records the checked versions and locations.

## Logical dependencies

The only asymptotic lower-bound input is the published noncoherent index-erasure theorem. The explicit Markov construction and constant-overhead reductions transfer it to each requested primitive. The constructive upper bound uses known-probability amplitude amplification with a full workspace account. The slow product preserves those costs through explicit embeddings.

The bridge identity follows independently from expanding paths and applying Cauchy–Schwarz. Its exact two-step converse requires strict positivity. The approximate compiler requires a single phase-fixed, source-and-endpoint-controlled bridge unitary; fidelity of isolated bridge density matrices is insufficient. These are sufficient conditions and exact identities, not a universal characterization of all possible powering algorithms.

## Reproducibility and limits

The [verification suite](../verification/README.md) checks the finite circuit identities and their relevant failure modes. It does not replace the analytical lower bound. The full science distinguishes ordinary samples, retained-history purifications, clean square-root states, and operator implementations. Those outputs are not interchangeable in a query comparison.
