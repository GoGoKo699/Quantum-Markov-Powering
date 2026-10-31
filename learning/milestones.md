# Thirty milestones for understanding clean Markov powering

This map follows the scientific question from a single sampling operation to an end-to-end quantum resource statement: when does coherent access to one Markov step supply coherent access to several steps?

The selected educational anchor is Andrew M. Childs's *Lecture Notes on Quantum Algorithms*, edition dated 17 April 2025. [The anchor bridge](anchor.md) supplies the selected sections, notation translation, and the steps connecting those foundations to this project. Section numbers below refer to that edition. The project's row-stochastic convention differs from the notes' column-stochastic convention; use the [notation and access table](anchor.md#notation-and-access) when moving between them.

## Allocation and source roles

| Phase | Milestones | Role in the scientific story |
|---|---|---|
| Background/preliminaries | M01–M12: 12 milestones | Assemble states, retained records, stochastic dynamics, quantum walks, and query/error models into one precise computational contract. |
| Narrative/innovation | M13–M30: 18 milestones | Follow the explicit construction through hardness, matching algorithms, sufficient bridge resources, early reversibility, and the final scope of the result. |

The allocation gives more space to the narrative because the central insight depends on several operations that look similar while providing different outputs and access. The background phase ends by integrating those distinctions into the problem definition. The narrative phase begins with the local transition rule, connects its classical and quantum consequences, and ends with the complete theorem and its limits. The map identifies the load-bearing understanding targets; detailed calculations and specialist lower-bound machinery remain in their canonical sources.

Every milestone inherits the phase named above its group and records a central question, understanding target, dependencies and story role, conceptual connection, and source pointers. “Anchor” always means the single selected Childs source. “Project” points to the canonical scientific account. “Research input” or “Research comparison” identifies primary literature used for a proof or comparison; these papers are distinct from the educational anchor.

## Phase I — Background/preliminaries

### M01 — Probabilities and coherent amplitudes

- **Central question:** What changes when the requested output is a quantum sample of a distribution?
- **Understanding target:** Distinguish an ordinary sampled label, the probability law of that label, and the pure state whose amplitudes are the positive square roots of those probabilities. Explain why measuring that pure state gives the law without making the three objects computationally interchangeable.
- **Dependencies and story role:** This is the local starting point. It supplies the meanings of state, amplitude, and output before any Markov or oracle terminology is introduced.
- **Conceptual connection:** A familiar sampling task acquires an additional coherence requirement when the endpoint must be available as a pure quantum register.
- **Sources:** Anchor: [Childs §§1.1–1.2](anchor.md#reading-route), “Quantum data” and “Quantum circuits.” Project: [notation and input family](../science/model.md#notation-and-input-family) and [ordinary sampling and observables](../science/interpretation.md#ordinary-sampling-and-observables).

### M02 — Joint registers and retained histories

- **Central question:** What happens to the endpoint when the register recording its origin is discarded?
- **Understanding target:** Explain how orthogonal history labels can retain information about an endpoint. Distinguish tracing out those labels from coherently returning them to a common zero state, including why the former can leave a mixed endpoint rather than its quantum sample.
- **Dependencies and story role:** Builds on M01 by moving from one register to joint states. It establishes the physical obstruction that the later oracle separation quantifies.
- **Conceptual connection:** The history that makes a computation reversible can also prevent the interference needed to combine different paths.
- **Sources:** Anchor: [Childs §§1.1 and 1.4](anchor.md#reading-route), for tensor-product registers and reversible computation. Project: [why mixing does not erase quantum history](../science/interpretation.md#why-mixing-does-not-erase-quantum-history). The reduced-state distinction is supplied locally.

### M03 — Uncomputation and complete unitary promises

- **Central question:** What must be specified before reversing or coherently reusing a preparation circuit?
- **Understanding target:** Distinguish a promise about a unitary's initialized-input columns from a specification of its full action. Explain how workspace, source control, and the actual inverse enter a valid uncomputation argument.
- **Dependencies and story role:** Uses M01–M02 to turn the retained-history issue into a circuit question. It prepares the distinction between a legal oracle and a desired isometry.
- **Conceptual connection:** A map that prepares the right state on one input does not, by that fact alone, specify how its inverse acts on other states.
- **Sources:** Anchor: [Childs §§1.2 and 1.4](anchor.md#reading-route). Project: [supplied oracle and charged queries](../science/model.md#supplied-oracle-and-charged-queries) and [one fixed exact completion](../science/bridge-composition.md#one-fixed-exact-completion-including-its-inverse).

### M04 — A query model as a resource statement

- **Central question:** Which operations are paid for in an oracle complexity comparison?
- **Understanding target:** Identify the supplied evaluation or row unitary, permitted inverses and controls, independent known gates, and excluded instance-dependent advice. Understand why a full simulation in both directions is needed before declaring two oracle interfaces equivalent.
- **Dependencies and story role:** Uses M03 to attach a cost to the circuit operations. It establishes the common currency for the later lower and upper bounds.
- **Conceptual connection:** Query complexity measures a specified interface; changing that interface can move computational work into the input.
- **Sources:** Anchor: [Childs §§21.1–21.2](anchor.md#reading-route), “Quantum query complexity” and “Quantum queries.” Project: [supplied oracle and charged queries](../science/model.md#supplied-oracle-and-charged-queries) and [query account](../science/resources.md#query-account).

### M05 — Stochastic rows, paths, and classical powers

- **Central question:** How does a sequence of classical transitions become a powered transition matrix?
- **Understanding target:** Read a stochastic row as a conditional distribution, a path probability as a product, and an endpoint probability as a sum over internal paths. Explain what the matrix power preserves and what information it marginalizes.
- **Dependencies and story role:** Uses the probability side of M01. It introduces the local stochastic object before global stationary or spectral statements.
- **Conceptual connection:** Classical temporal coarse-graining sums probabilities over histories; the desired quantum endpoint amplitudes are square roots of those sums.
- **Sources:** Anchor: [Childs §§18.1–18.2](anchor.md#reading-route), “Discrete-time quantum walk” and “How to quantize a Markov chain.” Project: [notation and input family](../science/model.md#notation-and-input-family) and [history conventions](../science/bridge-composition.md#1-conventions-and-access). Use the project's row convention.

### M06 — Stationarity, detailed balance, and time reversal

- **Central question:** How does reversing a stochastic process differ from undoing its preparation circuit?
- **Understanding target:** Distinguish a stationary law, detailed balance, and the stationary time-reversed conditional law. Explain why the inverse of a forward quantum row unitary is not automatically a row oracle for that reversed Markov kernel.
- **Dependencies and story role:** Combines M03 and M05. It connects a classical symmetry property to the quantum access needed to use it.
- **Conceptual connection:** Circuit reversal undoes amplitudes in a larger space; stochastic reversal changes which classical conditional distribution is requested.
- **Sources:** Anchor: [Childs §§1.4 and 18.2](anchor.md#reading-route), for uncomputation and the walk framework. Project: [stochastic time reversal as an additional resource](../science/construction.md#stochastic-time-reversal-is-an-additional-resource) and [the two discriminants](../science/interpretation.md#the-exact-distinction-between-two-discriminants). The stationary-reversal definitions are given locally.

### M07 — Mixing, spectral structure, and initial overlap

- **Central question:** Which promises about a chain concern its classical dynamics, and which concern a quantum starting state?
- **Understanding target:** Distinguish worst-case total-variation mixing, a powered-chain spectral gap, classical warmness in the stated density-ratio direction, and coherent state overlap. Explain what each controls without treating one promise as an implementation of another.
- **Dependencies and story role:** Builds on M05–M06 and the state distinction in M01. It assembles the promises that will make the hard example classically favorable.
- **Conceptual connection:** A chain may have useful spectral geometry and a readily prepared overlapping state while its target quantum operation remains unavailable.
- **Sources:** Anchor: [Childs §§18.2–18.3](anchor.md#reading-route), for the relation between stochastic and walk spectra. Project: [the product chain](../science/early-reversibility.md#the-product-chain), [its powered spectrum](../science/early-reversibility.md#the-powered-spectrum-is-fully-favorable), and [the known warm state](../science/construction.md#the-stationary-quantum-sample-and-its-known-warm-state). Total-variation and warmness conventions are supplied locally.

### M08 — Quantizing a row with an isometry and reflections

- **Central question:** What quantum objects can a supplied clean row oracle construct?
- **Understanding target:** Relate the row isometry $`V_P`$, its doubled-register subspace, the reflection $`R_P`$, and swap compression $`V_P^\dagger S V_P`$. Translate the notes' walk notation without identifying its walk unitary with the project's row-preparation oracle.
- **Dependencies and story role:** Joins M03–M06. It is the local quantum construction from which the operator tasks are defined.
- **Conceptual connection:** The same row preparation supports both a subspace reflection and a matrix encoding, but these are different requested operations.
- **Sources:** Anchor: [Childs §§18.2–18.3](anchor.md#reading-route) and the [notation translation](anchor.md#notation-and-access). Project: [quantum primitives and error conventions](../science/model.md#quantum-primitives-and-error-conventions).

### M09 — Encoded operators and their composition

- **Central question:** What matrix is obtained when two quantum encodings are multiplied?
- **Understanding target:** Read a block encoding as a specified subblock of a unitary, including its normalization. Distinguish ordinary multiplication of encoded matrices from applying a nonlinear entrywise transform after a classical matrix power.
- **Dependencies and story role:** Uses M04 and M08. It connects the local walk construction to the linear-algebra operations available to an outer quantum algorithm.
- **Conceptual connection:** A valid encoding of $`D(P)^j`$ does not by itself identify the encoded matrix with $`D(P^j)`$.
- **Sources:** Anchor: [Childs §§29.1 and 29.3](anchor.md#reading-route), “Block encoding” and “Qubitization.” Project: [the two discriminants](../science/interpretation.md#the-exact-distinction-between-two-discriminants). Research input: [block-encoding products](../references/related-work.md#block-encoding-products).

### M10 — Amplitude amplification as a controlled use of reflections

- **Central question:** Which resources turn a nonzero success amplitude into a useful preparation algorithm?
- **Understanding target:** Explain the two-reflection geometry of amplitude amplification and identify the actual preparation, its inverse, and the success-subspace reflection. Distinguish knowing an overlap from possessing the operations that amplify it.
- **Dependencies and story role:** Uses M03–M04 and M08. It supplies the constructive tool that will later match the lower bound.
- **Conceptual connection:** Reflections make amplification possible, while constructing the required reflection may itself be the hard computational task.
- **Sources:** Anchor: [Childs §19.3](anchor.md#reading-route), “Amplitude amplification and quantum counting.” Project: [exact amplification with a query cap](../science/upper-bounds.md#exact-amplification-with-an-explicit-query-cap). Research input for exact known-success dilution: [Brassard–Høyer–Mosca–Tapp](../references/related-work.md#amplitude-amplification).

### M11 — Lower bounds for generating a state

- **Central question:** What can a query lower bound prohibit when the output is quantum and arbitrary garbage is allowed?
- **Understanding target:** Distinguish state generation from function decision, and target-register fidelity from a requirement to clean every register. State the imported noncoherent index-erasure task, its large-codomain hypothesis, and why a constant-overhead reduction is enough to transfer its hardness.
- **Dependencies and story role:** Combines M01–M04. It supplies the research-level converse input and the error conventions needed to use it responsibly.
- **Conceptual connection:** The lower bound concerns coherence in the designated output, even when all other registers may depend on the unknown function.
- **Sources:** Anchor: [Childs §§21.1–21.2 and Chapter 23](anchor.md#reading-route), for query models and adversary-method foundations. Project: [inherited hardness theorem](../science/lower-bounds.md#inherited-hardness-theorem) and [error conventions](../science/model.md#quantum-primitives-and-error-conventions). Research input: [Lindzey–Rosmanis](../references/related-work.md#index-erasure); its specialized state-generation theorem is not derived from the lecture notes.

### M12 — The complete computational contract

- **Central question:** What must be fixed before a statement about quantum Markov speedup has a definite meaning?
- **Understanding target:** Integrate the supplied oracle, requested output, accuracy, success convention, initial information, and charged resources into one problem statement. Distinguish ordinary samples, retained-history purifications, clean rows, reflections, and normalized encodings within that statement.
- **Dependencies and story role:** Integrates M01–M11 and closes the background phase. The narrative can now compare algorithms under one contract.
- **Conceptual connection:** A spectral theorem becomes an end-to-end computational claim only after its required interface and output are specified.
- **Sources:** Anchor: [Childs §§18.2, 21.1–21.2, and 29.1](anchor.md#reading-route). Project: [model and theorem](../science/model.md), [what the original oracle supplies](../science/interpretation.md#what-the-original-oracle-supplies), and [query account](../science/resources.md#query-account).

## Phase II — Narrative/innovation

### M13 — Designing the hidden-image transition

- **Central question:** How can a local transition hide a difficult coherent state while remaining easy to sample?
- **Understanding target:** Explain the roles of the unknown injection, the two state coordinates, the uniform fresh coordinate, and the half-uniform background in $`P_f((x,y),(z,w))=K_x(w)/N`$. Identify what each feature contributes to access, positivity, and the eventual stationary law.
- **Dependencies and story role:** Uses M04–M06 and the contract in M12. This is the local mechanism from which the project's claims are derived.
- **Conceptual connection:** The state space retains enough history for a cheap forward transition while allowing classical marginalization to expose the hidden image.
- **Sources:** Anchor: [Childs §§18.2 and 21.2](anchor.md#reading-route). Project: [exact mixing and stationary distribution](../science/construction.md#exact-mixing-and-stationary-distribution) and [notation and input family](../science/model.md#notation-and-input-family).

### M14 — Establishing the legal one-query oracle

- **Central question:** Why is the supplied clean one-step transition a one-query operation?
- **Understanding target:** Follow $`U_f=O_fA`$ as a full unitary completion, including the known prefix preparation of the background. Explain the converse simulation $`O_f=U_fA^\dagger`$ and the invariant-register construction for controlled queries.
- **Dependencies and story role:** Applies M03–M04 to M13. It validates the access premise before any hardness claim relies on it.
- **Conceptual connection:** Explicit completion and control simulations prevent missing work from being hidden in the oracle's unspecified action.
- **Sources:** Anchor: [Childs §§1.4 and 21.2](anchor.md#reading-route). Project: [the full unitary completion](../science/construction.md#the-full-unitary-completion), [known background preparation](../science/construction.md#preparing-the-known-background-state), and [controlled calls](../science/construction.md#controlled-calls-do-not-strengthen-the-lower-bound-model).

### M15 — Exact classical mixing without reversible one-step dynamics

- **Central question:** Why does the second transition remove all dependence on the initial state?
- **Understanding target:** Explain the sum over the fresh intermediate coordinate that gives $`P_f^2=\Pi_f`$. Connect the resulting stationary law, nonreversibility of $`P_f`$, and the inexpensive classical stationary sampler without inferring a clean quantum preparation.
- **Dependencies and story role:** Uses M05–M07 and M13–M14. It establishes the strongest classical features of the example before analyzing its quantum output.
- **Conceptual connection:** Exact loss of classical memory is compatible with a retained coherent record of the path.
- **Sources:** Anchor: [Childs §§18.2–18.3](anchor.md#reading-route), for the walk and spectral setting. Project: [exact mixing and stationary distribution](../science/construction.md#exact-mixing-and-stationary-distribution) and [classical sampling remains easy](../science/construction.md#classical-sampling-remains-easy).

### M16 — The stationary state and the meaning of warm access

- **Central question:** Where is the hidden image encoded in the stationary quantum sample?
- **Understanding target:** Interpret $`|q_f\rangle=c|\psi_f\rangle+d|u_M\rangle`$ and the factorization $`|\pi_f\rangle=|u_N\rangle|q_f\rangle`$. Explain both the constant coherent overlap and the classical bound $`\nu\le2\pi_f`$, keeping the direction of that density-ratio bound explicit.
- **Dependencies and story role:** Combines M01, M07, M10, and M15. It isolates the state structure needed for the lower reduction and rules out a small starting-overlap explanation.
- **Conceptual connection:** A known state may overlap substantially with an unknown target without supplying the target's preparation or reflection.
- **Sources:** Anchor: [Childs §§1.1 and 19.3](anchor.md#reading-route). Project: [stationary quantum sample and warm state](../science/construction.md#the-stationary-quantum-sample-and-its-known-warm-state). Research comparison: [quantum rejection sampling and the ratio direction](../references/related-work.md#quantum-rejection-sampling).

### M17 — Extracting index erasure from the stationary sample

- **Central question:** How does one recover an image-state approximation without knowing which labels lie in the image?
- **Understanding target:** Explain why the known projector orthogonal to $`|u_M\rangle`$ removes the background and preserves almost all of the image state. Understand constant acceptance, the coherent two-outcome measurement, and the bounded repetition that produces fidelity above $`0.977`$.
- **Dependencies and story role:** Applies M02 and M11 to M16. This is the central reduction connecting the constructed state to the inherited lower bound.
- **Conceptual connection:** A known background can be removed coherently even though the unknown image cannot be prepared cheaply.
- **Sources:** Anchor: [Childs §§1.2 and 21.1–21.2](anchor.md#reading-route). Project: [the common projection](../science/lower-bounds.md#a-common-projection-that-reveals-the-image-state), [state preparation](../science/lower-bounds.md#state-preparation-and-clean-powered-rows), and [bounded repetition](../science/lower-bounds.md#bounded-repetition-and-the-sources-error-convention). Research input: [noncoherent index erasure](../references/related-work.md#index-erasure).

### M18 — Transferring hardness to all five coherent primitives

- **Central question:** Why are the powered row, its reflection, and its discriminant encoding computationally consequential outputs?
- **Understanding target:** Trace how a fixed source, a known warm input, or a normalization-one accepted block converts each requested primitive into the state-generation task. Explain the direct identity for the powered Szegedy reflection and why the reflection reduction needs no control of the synthesized reflection.
- **Dependencies and story role:** Combines M08–M12 with M15–M17. It turns one hard state into the full operator-access theorem.
- **Conceptual connection:** An operator implementation is useful on inputs that reveal the encoded hard state, even if the implementation never explicitly calls a stationary-state preparer.
- **Sources:** Anchor: [Childs §§18.2, 19.3, and 29.1](anchor.md#reading-route). Project: [block-encoding reduction](../science/lower-bounds.md#a-normalization-one-block-encoding-of-the-powered-discriminant), [stationary reflection](../science/lower-bounds.md#stationary-reflection), and [direct powered reflection](../science/lower-bounds.md#direct-powered-szegedy-reflection). Research input: [index erasure](../references/related-work.md#index-erasure).

### M19 — Locating the cost in stochastic reverse access

- **Central question:** Could an inexpensive stochastic reverse oracle remove the obstruction under the current input model?
- **Understanding target:** Read the reverse-row factorization into $`|r_w\rangle|q_f\rangle`$ and explain why it already contains the hard target. Distinguish this clean reverse-row lower bound from the readily available circuit inverse and from claims about other reverse interfaces.
- **Dependencies and story role:** Applies M06 and M17 to the explicit oracle in M14. It identifies an additional resource used by a neighboring algorithmic approach.
- **Conceptual connection:** Changing a conditional direction can expose the very marginal whose coherent preparation is hard.
- **Sources:** Anchor: [Childs §§1.4 and 18.2](anchor.md#reading-route). Project: [stochastic time reversal as an additional resource](../science/construction.md#stochastic-time-reversal-is-an-additional-resource) and [the two discriminants](../science/interpretation.md#the-exact-distinction-between-two-discriminants). Research comparison: [nonreversible spectral methods](../references/related-work.md#nonreversible-spectral-methods).

### M20 — An operator witness for the failed power identity

- **Central question:** How large is the discrepancy between powering the flat discriminant and quantizing the classical power?
- **Understanding target:** Explain how the Gram matrix of the row states determines $`\|D(P_f)\|`$, and why $`D(P_f^2)`$ being a unit-norm projector yields a discrepancy at least $`135/256`$. Recognize this as a uniform analytic operator statement, rather than a small numerical example.
- **Dependencies and story role:** Uses M08–M09, M13, and M15. It connects the query separation to an explicit failure of the most immediate matrix-composition substitute.
- **Conceptual connection:** The difference between summing path probabilities and retaining path amplitudes survives exact gates and perfect classical mixing.
- **Sources:** Anchor: [Childs §§18.3 and 29.1](anchor.md#reading-route). Project: [the constant operator gap](../science/construction.md#a-constant-operator-gap-between-the-two-quantum-powers).

### M21 — Reading the bridge-affinity identity

- **Central question:** What does a coherent history circuit actually encode after the whole path is reversed?
- **Understanding target:** Relate path expansion to $`H_j^\dagger\mathsf R_jH_j=D(P)^j`$. Explain how conditioning on endpoints reveals the forward/reversed bridge affinity multiplying each entry of $`D(P^j)`$.
- **Dependencies and story role:** Builds on M02, M05, M09, and M20. It gives the general mechanism behind the explicit operator mismatch.
- **Conceptual connection:** Internal path distinguishability remains visible as a loss of overlap even when the endpoint transition law has favorable symmetry.
- **Sources:** Anchor: [Childs §§18.2–18.3 and 29.1](anchor.md#reading-route). Project: [history conventions](../science/bridge-composition.md#1-conventions-and-access) and [whole-path compression](../science/bridge-composition.md#2-whole-path-compression). Research comparison: [block-encoding products](../references/related-work.md#block-encoding-products).

### M22 — The exact equality criterion and its support assumption

- **Central question:** When does the two-step flat-discriminant identity force reversibility of the original chain?
- **Understanding target:** Connect equality of bridge distributions to the triangle-ratio condition and detailed balance for a strictly positive kernel. Explain why sparse support can prevent this inference, using the directed-cycle counterexample as a boundary of the theorem.
- **Dependencies and story role:** Joins M06 and M21. It identifies the exact structural condition behind equality before considering approximate guarantees.
- **Conceptual connection:** A matrix identity detects circulation only when the required paths are available; positivity is part of the mathematical content.
- **Sources:** Anchor: [Childs §§18.2–18.3](anchor.md#reading-route), for the stochastic/walk framework. Project: [exact two-step converse and counterexample](../science/bridge-composition.md#3-an-exact-converse-at-two-steps).

### M23 — A sufficient promise for approximate discriminant powering

- **Central question:** What additional path information makes the cheap history encoding approximate the desired powered discriminant?
- **Understanding target:** Explain why uniformly high bridge affinity yields an operator-norm error bound. Distinguish an entrywise nonnegative comparison from a positive-semidefinite ordering, and distinguish a good block encoding from a clean endpoint row.
- **Dependencies and story role:** Uses M09 and M21–M22. It turns the general obstruction into a positive, explicitly conditional operator result.
- **Conceptual connection:** Controlling the information retained by paths can repair the encoded matrix without necessarily erasing those paths.
- **Sources:** Anchor: [Childs §29.1](anchor.md#reading-route), for encoding normalization and error. Project: [quantitative block-encoding criterion](../science/bridge-composition.md#4-a-quantitative-block-encoding-criterion) and [the sufficient-resource interpretation](../science/interpretation.md#a-sufficient-additional-resource).

### M24 — Compiling clean powers with a conditional bridge unitary

- **Central question:** What operation actually erases the internal path while preserving endpoint amplitudes?
- **Understanding target:** Regroup the history by its endpoints and identify the normalized conditional bridge state. Explain why the inverse of an endpoint-controlled bridge preparer produces a clean powered row, and include its preparation and unpreparation cost in the resource account.
- **Dependencies and story role:** Applies M03–M05, M14, and M21. It gives a constructive sufficient resource for the stronger clean-row task.
- **Conceptual connection:** The missing operation is coherent conditional unpreparation; classical conditional samples alone do not supply it.
- **Sources:** Anchor: [Childs §1.4](anchor.md#reading-route), for reversible computation and uncomputation. Project: [conditional-bridge compiler](../science/bridge-composition.md#5-a-compiler-from-conditional-bridge-unpreparation). The compiler and its access promise are local project results.

### M25 — Phases, full completions, and reusable approximations

- **Central question:** What accuracy promise makes a bridge compiler safe inside later coherent circuits?
- **Understanding target:** Explain why correct bridge density matrices can still carry harmful endpoint-dependent phases. Relate the phase-fixed controlled-unitary promise to one fixed nearby exact completion, its inverse, and the accumulated error under repeated controlled use; distinguish this from closeness to an independently prescribed completion.
- **Dependencies and story role:** Integrates M02–M04, M12, and M24. It makes the positive compiler an actual reusable oracle statement.
- **Conceptual connection:** Coherent algorithms depend on relative phases and full-unitary behavior beyond the single state being prepared.
- **Sources:** Anchor: [Childs §§1.2–1.4 and 21.2](anchor.md#reading-route). Project: [coherent approximation](../science/bridge-composition.md#6-approximation-that-composes-coherently), [one exact completion](../science/bridge-composition.md#one-fixed-exact-completion-including-its-inverse), and [phase failure](../science/bridge-composition.md#why-phases-and-retained-work-matter).

### M26 — Achieving the matching query upper bound

- **Central question:** How can the hard coherent primitives nevertheless be constructed with order $`\sqrt N`$ queries?
- **Understanding target:** Connect the known $`1/N`$ image-state success probability to exact amplitude dilution, then connect the coherent combination with the uniform state to the stationary sample. Explain the bounded query cap and how clean preparation yields the five primitives when the reflection includes the complete workspace.
- **Dependencies and story role:** Uses M10, M16, M18, and M25. It closes the query-complexity statement with an explicit algorithm instead of an abstract existence claim.
- **Conceptual connection:** The same coherence requirements that create the lower bound determine how a correct upper algorithm must amplify, reset its work, and implement operators.
- **Sources:** Anchor: [Childs §§19.3 and 29.1](anchor.md#reading-route). Project: [matching constructive upper bounds](../science/upper-bounds.md). Research input for exact amplification: [Brassard–Høyer–Mosca–Tapp](../references/related-work.md#amplitude-amplification).

### M27 — Completing the resource and accuracy account

- **Central question:** What costs remain after the number of oracle calls is known?
- **Understanding target:** Relate the query cap to known-gate count, workspace, controls, and finite rotation precision. Explain why a uniform whole-circuit error budget includes $`\log Q`$ when $`Q`$ calls are made, and why this is a sufficient approximation budget rather than a gate-synthesis lower bound.
- **Dependencies and story role:** Integrates M04, M09, M11, M25, and M26. It converts the constructive query statement into a fully specified implementation bound.
- **Conceptual connection:** Small local errors can accumulate through coherent reuse; a pure-state preparation guarantee alone is weaker than the required operator guarantee.
- **Sources:** Anchor: [Childs §§1.3, 21.1, and 29.1](anchor.md#reading-route), including “Universal gate sets.” Project: [resources](../science/resources.md) and [uniform approximation of the operators](../science/upper-bounds.md#uniform-approximation-of-the-operators). Research input: [finite gate synthesis](../references/related-work.md#gate-synthesis).

### M28 — Early reversibility with an independent slow mode

- **Central question:** Can exact reversibility appear long before worst-case mixing while the coherent primitive remains hard?
- **Understanding target:** Explain the product with the known two-state chain, its exact total-variation formula, powered gap, and preserved hard invariant subspaces. Interpret the choice $`T=n`$, $`N=2^n`$, including why the independent slow factor is bypassable and the classical stationary sampler remains cheap.
- **Dependencies and story role:** Combines M07, M15, M18, and M27. It places the access obstruction in the favorable spectral regime relevant to the broader claim.
- **Conceptual connection:** Tensoring a known slow mode changes worst-case mixing without providing the missing coherence for the hidden component.
- **Sources:** Anchor: [Childs §§1.1 and 18.2–18.3](anchor.md#reading-route). Project: [early reversibility](../science/early-reversibility.md), especially [the direct powered reflection](../science/early-reversibility.md#the-powered-szegedy-reflection-is-hard-directly) and [the product's scope](../science/early-reversibility.md#scope-of-the-product-construction).

### M29 — Interpreting a powered-kernel spectral algorithm

- **Central question:** Which end-to-end inference changes once the cost of supplying a powered primitive is exposed?
- **Understanding target:** Read a bound in supplied powered-oracle calls together with the cost of constructing that oracle and its required accuracy. Preserve the distinction between a modular cost product and a universal lower bound, and explain why ordinary sampling, scalar observables, and conditional spectral theorems retain their stated scope.
- **Dependencies and story role:** Integrates M12, M19–M20, and M23–M28. It connects the theorem and its positive conditions to the surrounding algorithmic literature.
- **Conceptual connection:** A transformation of an available encoding and a method of obtaining that encoding are separate scientific claims that must be joined explicitly.
- **Sources:** Anchor: [Childs §§19.3 and 29.1–29.3](anchor.md#reading-route). Project: [reading a powered-kernel bound](../science/interpretation.md#how-to-read-a-powered-kernel-spectral-bound) and [ordinary sampling and observables](../science/interpretation.md#ordinary-sampling-and-observables). Research comparisons: [nonreversible spectral methods](../references/related-work.md#nonreversible-spectral-methods), [quantum fast-forwarding](../references/related-work.md#quantum-fast-forwarding), and [quantized couplings](../references/related-work.md#quantized-couplings).

### M30 — The complete result, its evidence, and its boundary

- **Central question:** What is now established about coherent temporal coarse-graining, and which questions remain separate?
- **Understanding target:** Give a connected account of the legal one-step oracle, favorable classical properties, five matching coherent costs, bridge identity, and sufficient bridge resources. Separate the inherited lower-bound theorem from local deductions, and distinguish analytic proof from finite circuit verification and from claims about applications not covered by the model.
- **Dependencies and story role:** Integrates M01–M29 and closes the narrative phase. It assembles the contribution into one explanation with its assumptions and limitations intact.
- **Conceptual connection:** Efficient coherent composition needs an implementation resource beyond endpoint mixing or powered spectral geometry; the obstruction and the supplied sufficient conditions describe complementary parts of that statement.
- **Sources:** Anchor: [Childs §§21.1–21.2, Chapter 23, and §§29.1–29.3](anchor.md#reading-route). Project: [main theorem](../science/model.md#main-theorem), [logical dependencies](../science/README.md#logical-dependencies), [established scope and open questions](../science/interpretation.md#what-is-established-and-what-remains-open), and [verification limits](../verification/README.md#limits). Research attribution: [related work](../references/related-work.md).

