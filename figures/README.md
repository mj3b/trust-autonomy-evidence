# Publication Figure Set

Version 0.9.0 contains six main figures and four appendix figures. Each figure is derived from committed research artifacts and ships with a CSV, PNG, SVG, specification, caption, and interpretation boundary. The case figures use the v0.6 Oko assessment and the preserved v0.3 Patriot assessments.

## Visual standard

The v0.7 design uses journal-width pages, white backgrounds, thin rules, one blue accent, direct labels, and color-independent state codes. Large in-image headlines and source notes were removed. Captions carry the sample, derivation, uncertainty, and prohibited interpretation.

Figures show relationships. The [structured manuscript tables](../paper/tables.md) preserve exact states and counts. [`manuscript-tables.tex`](../paper/tables/manuscript-tables.tex) provides three-rule, no-vertical-rule typesetting fragments for submission.

## Main figures

| Figure | Short description | Files |
|---|---|---|
| Figure 1 | Traces 928 preserved candidates through five decisions, three selections, two exclusions, and the frozen stopping rule. | [PNG](generated/fig-1-selection-and-stopping.png) · [SVG](generated/fig-1-selection-and-stopping.svg) · [data](data/fig-1-selection-and-stopping.csv) |
| Figure 2 | Compares 27 practical-control states across Oko, Patriot ZG710, and Patriot F/A-18C. | [PNG](generated/fig-2-practical-control-chain.png) · [SVG](generated/fig-2-practical-control-chain.svg) · [data](data/fig-2-practical-control-chain.csv) |
| Figure 3 | Places 15 source-linked events in relative order and marks the F/A-18C public record gap. | [PNG](generated/fig-3-decision-paths.png) · [SVG](generated/fig-3-decision-paths.svg) · [data](data/fig-3-decision-paths.csv) |
| Figure 4 | Compares 36 trust-evidence states across the three public cases. | [PNG](generated/fig-4-trust-evidence-states.png) · [SVG](generated/fig-4-trust-evidence-states.svg) · [data](data/fig-4-trust-evidence-states.csv) |
| Figure 5 | Traces the formal literature search and reports the final state after all 89 author decisions. | [PNG](generated/fig-5-formal-search-and-screening.png) · [SVG](generated/fig-5-formal-search-and-screening.svg) · [data](data/fig-5-formal-search-and-screening.csv) |
| Figure 6 | Shows how supported, partial, unsupported, and indeterminate findings compose the six pre-action stages for each case. | [PNG](generated/fig-6-evidence-boundaries.png) · [SVG](generated/fig-6-evidence-boundaries.svg) · [data](data/fig-6-evidence-boundaries.csv) |

## Appendix figures

| Figure | Short description | Files |
|---|---|---|
| Figure A1 | Maps 12 controlled mutations to 11 state changes and three invariance tests. | [PNG](generated/fig-a1-mutation-response.png) · [SVG](generated/fig-a1-mutation-response.svg) · [data](data/fig-a1-mutation-response.csv) |
| Figure A2 | Traces research and figure artifacts from frozen inputs through validation. | [PNG](generated/fig-a2-reproducibility-lineage.png) · [SVG](generated/fig-a2-reproducibility-lineage.svg) · [data](data/fig-a2-reproducibility-lineage.csv) |
| Figure A3 | Shows five claim gates and conclusion eligibility for 20 material claims. | [PNG](generated/fig-a3-claim-evidence-integrity.png) · [SVG](generated/fig-a3-claim-evidence-integrity.svg) · [data](data/fig-a3-claim-evidence-integrity.csv) |
| Figure A4 | Shows the six Oko states corrected between v0.3.0 and v0.6.0. | [PNG](generated/fig-a4-oko-versioned-correction.png) · [SVG](generated/fig-a4-oko-versioned-correction.svg) · [data](data/fig-a4-oko-versioned-correction.csv) |

## Reading guides

### Figure 1. Public-case selection and stopping

The figure shows 928 preserved candidate records, five completed decisions, three selected cases, two exclusions, and 923 unscreened records. Screening stopped when the three prespecified strata were filled. The unscreened records carry no exclusion decision. The counts establish procedure execution and supply no prevalence estimate.

### Figure 2. Practical-control states

Each column contains evidence about a formal human role. The states elsewhere in the chain differ. Oko carries partial support from access through effect. ZG710 carries supported authority alongside unsupported comprehension, feasible challenge, exercised challenge, and effect. F/A-18C carries supported authority and leaves comprehension, feasible challenge, and exercised challenge unresolved.

This pattern supports one bounded conclusion: authority requires a separate evidence path to information, understanding, opportunity, action, and effect. The figure supplies no causal estimate and no claim about how often these states occur.

### Figure 3. Bounded decision paths

The figure shows five source-linked events for each case and identifies where human judgment entered each sequence. Horizontal position records order. It carries no common time scale. The dotted F/A-18C segment marks missing public evidence about timing, displays, report independence, and feasible challenge.

### Figure 4. Trust-evidence states

The figure reports 36 proposition-level findings. Conditional reliability and calibrated uncertainty are unsupported in every packet. Record integrity is indeterminate in every packet. Evidence completeness is unsupported or partial. These gaps limit the reliance claims available from the packets. The figure supplies no system ranking or aggregate trust score.

### Figure 5. Formal search and final screening state

The left panel shows retrieval, pooling, and deduplication. The right panel reports six final screening classes on a declared logarithmic count axis. Blue points identify 27 close and 45 background records. The annotation records 89 of 89 author decisions complete. Another 1,087 records lack abstracts, and authenticated databases remain open. The display supports the final queue result and no completed-review or universal-originality claim.

### Figure 6. Evidence boundaries

Each bar contains six pre-action findings. Oko contains six partially supported findings. ZG710 contains one supported, one partially supported, and four unsupported findings. F/A-18C contains one supported, one partially supported, one unsupported, and three indeterminate findings. Partial support records some evidence with a material gap. Indeterminate records insufficient evidence for a decision. The counts assign no numeric distance among states and supply no missingness rate, reliability estimate, aggregate control score, or case ranking.

### Figure A1. Mutation response

Every observed response matched the committed oracle for the 12 controlled mutations. The author designed the fixtures, code, mutations, and oracle. The result establishes internal contract behavior for those fixtures and supplies no independent-reviewer agreement or field-validity estimate.

### Figure A2. Reproducibility lineage

The upper lane traces the research record. The lower lane traces the figure pipeline. The labeled connector runs from Assessments to Plot inputs because recorded assessment states become inputs to the figure builder. Hashes can detect a changed committed file. This lineage supports reconstruction of the artifact path and makes no source-truth or completeness claim.

### Figure A3. Claim-evidence integrity

Every declared claim passes traceability, integrity, and support review. Final author-screening results are eligible within the declared queue. Independent validity fails evidence fitness and remains ineligible. The matrix separates evidence linkage from conclusion eligibility. It calculates no aggregate score and supplies no independent-reliability finding.

### Figure A4. Oko versioned correction

All six Oko pre-action states move from supported to partially supported. The packet did not change. The v0.6 adjudication applied a stricter rule fixed before reassessment. The figure records a method-driven correction and adds no historical evidence.

## Regeneration

```bash
python analysis/build_figures.py
python analysis/build_claim_evidence_figure.py
python analysis/build_figures.py --check
python analysis/build_claim_evidence_figure.py --check
```

The core builder checks exact equality for nine CSV files, validates 18 rendered files, and verifies the current v0.9 figure manifests. The claim-evidence builder checks one CSV, two rendered files, and its separate v0.9 manifest. Image bytes can vary across operating systems when plotted data and dimensions remain unchanged.

[Figure methods](../reports/figure-methods.md) records the formal captions and transformations. [The figure register](specifications/figure-register.json) describes Figures 1 through A2 and A4. [The claim-evidence specification](specifications/claim-evidence-integrity.json) describes Figure A3.

## Use boundary

The cases were purposefully selected. The figures support description of the committed packets. They supply no population frequency, effect size, causal estimate, inter-rater reliability result, institutional-effectiveness finding, system ranking, or aggregate trust score.
