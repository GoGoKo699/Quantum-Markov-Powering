# Learning guide

The central question is how to combine two easy quantum transitions into a clean endpoint state. A classical computation can keep an intermediate record and then ignore it. A coherent computation must account for what happens to that record before the endpoint can be used as the desired pure state or quantum operator.

This guide connects the project's theorem to Andrew M. Childs's *Lecture Notes on Quantum Algorithms*, edition dated 17 April 2025, the selected educational anchor.

## The shared map

The [30-milestone map](milestones.md) has two phases:

- **M01–M12 — Background/preliminaries:** states and histories, reversible circuits, stochastic transitions, walk encodings, and the complete access/output/error contract.
- **M13–M30 — Narrative/innovation:** the explicit hard chain, state and operator reductions, bridge conditions, matching construction, resource costs, and the scope of early reversibility.

The [allocation and source roles](milestones.md#allocation-and-source-roles) explain why the project uses 12 background milestones and 18 narrative milestones. Each phase moves from local objects to an integrated account. The map supplies common understanding targets and dependencies; specialist proof details remain in the linked science.

Start with the [anchor bridge](anchor.md), which identifies the relevant Childs sections and supplies a complete small example. The map then places those foundations in the order needed for this project. The [canonical scientific overview](../science/README.md) remains the direct route to the statements and proofs.

## Reading routes

These routes emphasize different questions within the same map. Every milestone names its earlier dependencies and links the relevant canonical argument.

| Reading purpose | Milestone route | Canonical destination |
|---|---|---|
| Follow the complete scientific story | [M01](milestones.md#m01--probabilities-and-coherent-amplitudes) through [M12](milestones.md#m12--the-complete-computational-contract), then [M13](milestones.md#m13--designing-the-hidden-image-transition) through [M30](milestones.md#m30--the-complete-result-its-evidence-and-its-boundary) | [Scientific overview](../science/README.md) |
| Understand the theorem and its matched query cost | [M12](milestones.md#m12--the-complete-computational-contract), M13–M18, then [M26](milestones.md#m26--achieving-the-matching-query-upper-bound)–M27 and M30 | [Model](../science/model.md), [lower bounds](../science/lower-bounds.md), [upper bounds](../science/upper-bounds.md), [resources](../science/resources.md) |
| Understand what retained paths encode and how to clean them | M08–M09, then [M20](milestones.md#m20--an-operator-witness-for-the-failed-power-identity)–M25 and M27 | [Bridge composition](../science/bridge-composition.md) |
| Examine the early-reversibility claim | M05–M09, M15–M20, then [M28](milestones.md#m28--early-reversibility-with-an-independent-slow-mode)–M30 | [Early reversibility](../science/early-reversibility.md) and [interpretation](../science/interpretation.md) |
| Follow the actual circuit and its implementation costs | M03–M04, M10, [M14](milestones.md#m14--establishing-the-legal-one-query-oracle), then M25–M27 | [Oracle completion](../science/construction.md#the-full-unitary-completion), [constructive upper bounds](../science/upper-bounds.md), and [verification](../verification/README.md) |

The source numbers in the map refer to the chosen edition, with the precise headings listed in the [anchor reading route](anchor.md#reading-route). Reading the entire lecture-note collection is unnecessary for following these routes.

## Source roles

| Source type | What it provides |
|---|---|
| **One educational anchor:** [Childs](anchor.md#selected-source) | Quantum data and circuits, reversible computation, walk quantization, amplitude amplification, query models, adversary-method foundations, and block encodings. |
| **Canonical project science:** [science](../science/README.md) | The explicit Markov embedding, all reductions, constructive query caps, analytic operator mismatch, bridge compiler, and the access-model conclusion. Local explanations also supply the project's stationary-distribution, total-variation, and retained-history conventions. |
| **Primary research dependencies and comparisons:** [related work](../references/related-work.md) | The noncoherent index-erasure lower bound; exact known-success amplification; finite gate synthesis; and the access models needed for comparison with other quantum sampling methods. These papers have separate proof and attribution roles. |
| **Finite verification:** [verification](../verification/README.md) | Reproducible checks of concrete matrix and circuit identities, including relevant failure cases. The analytic and imported asymptotic theorems remain the sources of the general claims. |

The specialized noncoherent index-erasure theorem is an imported research result. Childs's query and adversary chapters explain its methodological setting; they do not replace that proof input.

## Notation that matters

The [notation and access bridge](anchor.md#notation-and-access) is part of the reading route. Childs uses column-stochastic transition matrices, while this project uses row-stochastic kernels. The notes' walk unitary is also different from the supplied row-preparation unitary, and the doubled-space projector in the walk construction is different from the project's classical stationary kernel $`\Pi_f`$.

Keeping those objects distinct makes the main question precise: classical powers, coherent history circuits, clean powered rows, and discriminant powers are related operations with different output and access requirements.

## What the guide is meant to make understandable

The explicit example supports a tight query statement for five clean coherent tasks under its stated oracle model. It also admits an inexpensive ordinary stationary sampler. The product example adds slow worst-case mixing through a known independent factor. The bridge results give sufficient additional coherent promises rather than a complete classification of every useful Markov chain.

These distinctions appear throughout the map and are integrated in [M30](milestones.md#m30--the-complete-result-its-evidence-and-its-boundary). They are part of understanding the result itself. The [final scientific interpretation](../science/interpretation.md#what-is-established-and-what-remains-open) states the established conclusion and the remaining questions.

