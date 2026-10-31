# Primary-source index

Checked 31 October 2026. Locations below identify the claims actually used. The comparison does not certify exhaustive coverage or priority. The bibliography is [references.bib](references.bib).

| Key | Primary source and version | Checked locations | Role |
|---|---|---|---|
| `LindzeyRosmanis2022` | [Final journal PDF](https://www.rintonpress.com/xxqic22/qic-22-78/0594-0626.pdf); QIC 22(7–8), 594–626 (2022). [arXiv v3](https://arxiv.org/abs/1902.07336v3) supplies a versioned alternative. | Journal Theorem 1, §2.2, Corollary 1. The corresponding arXiv main theorem is numbered 1.1. | External noncoherent index-erasure lower bound and its exact error convention. The representation-theoretic proof is inherited. |
| `BrassardEtAl2002` | [Author preprint](https://arxiv.org/abs/quant-ph/0005055), sole arXiv version; published in Contemporary Mathematics 305 (2002). | §2.1, Theorem 4 and preceding dilution construction; §4. | Known-probability amplitude amplification; observable-estimation context. |
| `DawsonNielsen2006` | [arXiv v2](https://arxiv.org/abs/quant-ph/0505030v2); [publisher record](https://www.rintonpress.com/journals/doi/QIC6.1-6.html). | §§2–4. | Finite-gate approximation of the explicit known rotations. |
| `GilyenEtAl2019` | [Full author preprint](https://arxiv.org/abs/1806.01838); STOC 2019 version has a shorter page range. | Full-paper Definition 43 and Lemma 53, §4.4, pp. 46–47. | Encoding convention and ordinary matrix-product composition. |
| `ClaudonEtAl2025` | [Final article](https://pmc.ncbi.nlm.nih.gov/articles/PMC12663442/); Nature Communications 16, 10732 (28 November 2025). [arXiv v2](https://arxiv.org/abs/2501.05868v2) was posted 3 September 2025. | Main Proposition 3; “Reversibility on π-average”; Discussion/Summary; Methods/“Mixed kernels,” Corollary 2. | Closest spectral-method interpretation; supplied powered-kernel access remains explicit. |
| `ClaudonEtAl2025Supplement` | [Published supplement](https://pmc.ncbi.nlm.nih.gov/articles/instance/12663442/bin/41467_2025_65761_MOESM1_ESM.pdf), dated 22 October 2025. | §§II–IV; §IV.B Corollary 5; visible §V.E.5, p. 26. | Reconciliation with the final main text and circuit-access assumptions. |
| `AharonovTaShma2007` | [Final author-hosted journal PDF](https://www.cs.tau.ac.il/~amnon/Papers/AT.sicomp07.pdf); SICOMP 37(1), 47–82 (2007). | §5.3 Definition 5.1; §5.4 Theorem 1.3 and Remark 5.1. | Earlier distinction between classical sampling and quantum state generation; ratio and sparsity assumptions. |
| `OzolsEtAl2012` | [arXiv v4](https://arxiv.org/abs/1103.2774v4), 13 December 2011; ITCS 2012. [Journal-author record](https://research.ibm.com/publications/quantum-rejection-sampling) identifies the 2013 journal extension. | Definitions 2 and 4; Theorem 1 in the versioned preprint. | Amplitude-conversion access and the retained labelled component states. |
| `TemmeWocjan2025` | [arXiv v2](https://arxiv.org/abs/2504.02651v2), 13 December 2025; [Quantum publication](https://quantum-journal.org/papers/q-2025-12-18-1951/), 18 December 2025. | Lemma 16; Theorem 18; §5.5 Theorem 20, p. 20 of the PDF. | Classical coalescence versus implementation of the quantized coupling. |
| `Szegedy2004` | [Final conference record](https://ieeexplore.ieee.org/document/1366222/). Related [longer author preprint](https://arxiv.org/abs/quant-ph/0401053) is titled *Spectra of Quantized Walks and a √δε rule*. | Conference bibliographic record; preprint model and overview. | Attribution of the reflection-based quantum walk framework; not an additional lower-bound input. |
| `ApersSarlette2019` | [Final journal PDF at CWI](https://ir.cwi.nl/pub/28721/28721.pdf), QIC 19(3–4), 181–213 (2019). | Theorem 1 and surrounding formulation, pp. 182–183; §2. | Quantum fast-forwarding acts on powers of the discriminant already encoded. |

## Published supplement reconciliation

The final main text is the controlling reference for Proposition 3 and Corollary 2. The final supplement retains a different, compatible mixing formulation:

| Location | Mixing formulation | Charged operator |
|---|---|---|
| Final main Corollary 2 | Hellinger mixing at $`t=\min\{\tau(\epsilon),\tau^*(\epsilon)\}`$ | Szegedy operator of $`P^t`$ |
| Final supplement §IV.B, Corollary 5, p. 13 | Total-variation mixing, followed by $`\widetilde t=t\lceil\log n\rceil`$ | Szegedy operator of $`P^{\widetilde t}`$ |

Both are conditional powered-oracle statements. This difference changes the mixing-to-spectral estimate, not the need to implement the powered operator. The final supplement's visible p. 26 illustrates a circuit for a particular kinetic walk; it does not establish a general forward-oracle compiler for arbitrary powers.

The PDF text layer near that page contains material absent from the rendered page. The comparison uses the visible page and does not attribute that hidden material to the final paper. The same issue occurs in the arXiv v2 supplement.

### Reproducible supplement provenance

The published supplement was obtained through the official [Europe PMC supplementary-file endpoint](https://www.ebi.ac.uk/europepmc/webservices/rest/PMC12663442/supplementaryFiles), which returns a ZIP for the final article.

- ZIP member: `41467_2025_65761_MOESM1_ESM.pdf`.
- PDF size: 855,140 bytes.
- PDF SHA-256: `e34994ebd0744572ec17a714eef2458e916fd07f9975660847e094bfa7041466`.
- Title-page date: 22 October 2025.
- Compared arXiv supplement: [versioned ancillary PDF](https://arxiv.org/src/2501.05868v2/anc/Markov__SI-rev2.pdf), 853,340 bytes, SHA-256 `3433ef28aabdae2891cc06822e191af5e0b2f1832281dee6b455b076cceca030`, dated 3 September 2025.

The relevant conditional input model was unchanged between these supplement versions. Differences in examples, layout, and bibliography are not used to infer a broader theorem.
