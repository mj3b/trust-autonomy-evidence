# Publication Figure Set

The figure set converts committed assessments, selection records, mutation results, artifact lineage, and the v0.6.0 integrity audit into seven reproducible graphics. The current main figures incorporate the v0.6 Oko adjudication and preserve the v0.3 Patriot assessments.

The figures follow four measurement rules drawn from the repository's use of METR's evaluation discipline: the measured unit appears in each specification, raw categorical states remain visible, uncertainty stays separate from negative findings, and every image has a machine-readable input table.

## Main figures

| Figure | Short description | Files |
|---|---|---|
| Figure 1 | Shows how 928 preserved candidate records produced five screening decisions, three selected cases, two exclusions, and 923 unscreened records under the frozen stopping rule. | [PNG](generated/fig-1-selection-and-stopping.png) · [SVG](generated/fig-1-selection-and-stopping.svg) · [data](data/fig-1-selection-and-stopping.csv) |
| Figure 2 | Compares the nine practical-control propositions across Oko, Patriot ZG710, and Patriot F/A-18C. | [PNG](generated/fig-2-practical-control-chain.png) · [SVG](generated/fig-2-practical-control-chain.svg) · [data](data/fig-2-practical-control-chain.csv) |
| Figure 3 | Places 15 source-linked events in relative order and marks the public evidence gap in the F/A-18C sequence. | [PNG](generated/fig-3-decision-paths.png) · [SVG](generated/fig-3-decision-paths.svg) · [data](data/fig-3-decision-paths.csv) |
| Figure 4 | Compares the 12 trust-evidence propositions across the three public cases. | [PNG](generated/fig-4-trust-evidence-states.png) · [SVG](generated/fig-4-trust-evidence-states.svg) · [data](data/fig-4-trust-evidence-states.csv) |

## Appendix figures

| Figure | Short description | Files |
|---|---|---|
| Figure A1 | Maps all 12 controlled mutations to 11 prespecified state changes and three invariance tests. | [PNG](generated/fig-a1-mutation-response.png) · [SVG](generated/fig-a1-mutation-response.svg) · [data](data/fig-a1-mutation-response.csv) |
| Figure A2 | Traces the research and figure-generation artifacts from frozen collections through repository validation. | [PNG](generated/fig-a2-reproducibility-lineage.png) · [SVG](generated/fig-a2-reproducibility-lineage.svg) · [data](data/fig-a2-reproducibility-lineage.csv) |
| Figure A3 | Shows five claim gates and conclusion eligibility for the material v0.6 claims. | [PNG](generated/fig-a3-claim-evidence-integrity.png) · [SVG](generated/fig-a3-claim-evidence-integrity.svg) · [data](data/fig-a3-claim-evidence-integrity.csv) |

## How to read the figures

Each reading guide separates four steps: what the figure directly shows, how the comparison supports an inference, what conclusion follows, and where the evidence ends. Categorical states are findings about declared propositions. They are not numeric scores.

### Figure 1. Frozen selection and stopping

The figure directly shows 928 preserved candidate records, five completed screening decisions, three selected cases, two exclusions, and 923 unscreened records. The procedure stopped when the three prespecified strata were filled. No decision was assigned to the 923 records that remained.

The counts support a procedural conclusion: the published cases follow the frozen order and stopping rule. They do not support a conclusion about the prevalence of eligible cases because almost all preserved records were left unscreened.

### Figure 2. Practical-control chain

The figure directly shows 27 categorical findings: nine practical-control conditions across three cases. Oko records partial support for access, comprehension, authority, feasibility, exercise, and effect. ZG710 records supported authority alongside unsupported comprehension, feasibility, exercise, and effect. F/A-18C records supported authority, partially supported access, an unsupported effect, and unresolved comprehension, feasibility, and exercise.

Authority evidence is present in every column, with partial support in Oko and support in both Patriot packets. The remaining pre-action conditions vary. This pattern supports a bounded method claim: each practical-control stage requires its own evidence. The figure does not estimate the causal contribution of any condition.

### Figure 3. Reconstructed decision paths

The figure directly shows five source-linked events in each case. Oko contains a documented human challenge before escalation. ZG710 contains an approximately one-minute decision window followed by authorization, engagement, and loss. F/A-18C contains detection, correlation, an engagement order, launch, and loss. Timing and display evidence remain incomplete.

The ordered events show where a human judgment entered each sequence and where the public record stops supporting further reconstruction. Horizontal position records order only. It supplies no common elapsed-time scale.

### Figure 4. Trust-evidence states

The figure directly shows 36 categorical findings: 12 trust-evidence propositions across three cases. Conditional reliability and calibrated uncertainty are unsupported in every packet. Record integrity is indeterminate in every packet. Evidence completeness is unsupported or partially supported.

Those shared gaps limit the reliance claims that the packets can support. The matrix permits proposition-level comparison. It supplies no aggregate trust score, system ranking, or claim that one system is generally trustworthy.

### Figure A1. Mutation-response map

The figure directly shows that 11 prespecified state changes occurred and three declared invariance conditions remained unchanged across 12 controlled mutation tests. The observed responses match the committed oracle.

The result shows that the assessment code follows its declared rules for the included synthetic fixtures. The author designed the fixtures, code, mutations, and oracle, so the result supplies no independent-reviewer agreement or field-validity estimate.

### Figure A2. Reproducibility lineage

The figure directly shows the path from frozen collections through candidate selection, case packets, assessments, derived tables, rendered figures, and integrity checks. File hashes and the manifest can detect a changed committed input or artifact.

This lineage supports reconstruction of how each plotted state was produced. It establishes ordering and file integrity. It makes no claim that a source is true, complete, or sufficient for an institutional decision.

### Figure A3. Claim-evidence integrity

The figure directly shows five evidence gates and one conclusion-eligibility state for each material v0.6 claim. Every claim passes traceability. `PAPER-C04` now passes because the v0.6 assessment fits the declared evidence rule and preserves the partial state. `PAPER-C09` passes dependency closure. The independent-assessment and database-search limits remain published exceptions.

The matrix separates a working evidence link from evidence that fits the proposed conclusion. Purple cells preserve indeterminate states and gray cells preserve outside-scope or ineligible states. The figure calculates no aggregate trust score and supplies no source-truth or independent-reliability finding.

## Regeneration

Install the development dependencies and rebuild the full set:

```bash
python -m pip install -r requirements-dev.txt
python analysis/build_figures.py
python scripts/run_coe_integrity_audit.py
python analysis/build_claim_evidence_figure.py
```

Check exact equality for the six derived CSV files, verify the structure and dimensions of the PNG and SVG files, and confirm the recorded hashes for all 18 committed artifacts:

```bash
python analysis/build_figures.py --check
python scripts/run_coe_integrity_audit.py --check
python analysis/build_claim_evidence_figure.py --check
```

The repository validator runs the same data and artifact-integrity checks. Image renderer bytes can vary by operating system even when the plotted data and dimensions remain unchanged. [Figure methods](../reports/figure-methods.md) records the transformations, captions, and claim boundaries. [The figure register](specifications/figure-register.json) describes Figures 1 through A2. [The v0.6 specification](specifications/claim-evidence-integrity.json) describes Figure A3. Versioned manifests record byte counts and SHA-256 hashes.

## Use boundary

The three public cases were purposefully selected under a stopping rule. The figures support cross-case description for those packets. They supply no population frequency, effect size, causal estimate, inter-rater reliability result, system ranking, or aggregate trust score.
