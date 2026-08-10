# Figure Methods and Captions

## Result

The v0.8.0 figure package contains six main figures and four appendix figures. It exposes selection, case states, event sequences, formal-search progress, evidence boundaries, mutation responses, artifact lineage, claim gates, and a versioned correction. Every display has a derived CSV and a declared interpretation boundary.

## Design rule

The figure package uses a journal visual system: white background, thin rules, one blue accent, direct labels, compact page dimensions, and state codes carried by shape and text. Titles, source notes, uncertainty, and interpretation appear in captions. The related [table package](../paper/tables.md) uses concise headings, three horizontal rules in its typeset form, no vertical rules, aligned values, and explanatory notes.

The figures report categorical states and counts. They assign no numeric distance among supported, partially supported, unsupported, indeterminate, and outside scope. Figure 5 alone uses a logarithmic axis, which is labeled in the image and caption.

## Inputs and transformations

[`analysis/build_figures.py`](../analysis/build_figures.py) reads committed assessments, selection records, mutation results, event and lineage specifications, formal-search files, and the Oko correction ledger. It writes nine CSV files and eighteen image files. [`analysis/build_claim_evidence_figure.py`](../analysis/build_claim_evidence_figure.py) writes the Figure A3 CSV, PNG, SVG, and manifest from the v0.8 audit result.

The [figure register](../figures/specifications/figure-register.json) records each unit of analysis, sample, inputs, transformation, supported claim, and prohibited interpretation. The builders verify the frozen candidate order, mutation deltas, search totals, and versioned state transitions before rendering.

## Formal captions

### Figure 1. Public-case selection and stopping

The AI Incident Database input contained 1,607 incident records and 7,452 report records, of which 828 matched the frozen vocabulary. The OECD export contributed 100 candidate records. The protocol preserved 928 records, screened the first five AIID candidates in fixed order, selected three cases, excluded two, and stopped when all three prespecified strata were filled. The remaining 923 records were unscreened and carry no exclusion decision. Purposeful stopping supplies no prevalence or representativeness estimate.

### Figure 2. Practical-control states across three public cases

Twenty-seven declared states compare nine practical-control propositions across three purposefully selected public cases. Oko is partially supported across the six stages from access through effect under the v0.6 adjudication. Patriot ZG710 supports authority while comprehension, feasibility, exercise, and effect are unsupported. Patriot F/A-18C supports authority while comprehension, feasibility, and exercise remain indeterminate. S = supported; P = partially supported; U = unsupported; I = indeterminate; O = outside scope. The figure supplies no frequency, effect-size, causal, reliability, or population estimate.

#### Derivation of the central lesson

1. Extract the six pre-action states for each case: access, comprehension, authority, feasibility, exercise, and effect.
2. Compare authority. It is partially supported in Oko and supported in both Patriot packets.
3. Compare the other stages. Oko carries partial support across all six. ZG710 carries partial access and unsupported comprehension, feasibility, exercise, and effect. F/A-18C carries partial access, unresolved comprehension, feasibility, and exercise, and an unsupported effect.
4. Keep unsupported and indeterminate separate. ZG710 contains evidence against several conditions. F/A-18C lacks enough public evidence to decide several conditions.
5. State the bounded inference. Authority evidence does not determine the other practical-control stages in these packets. Each stage needs its own evidence path connecting information, understanding, permission, opportunity, action, and effect.

This comparison does not isolate a causal effect, estimate a population relationship, or assign equal weight to every condition in another setting.

### Figure 3. Bounded decision paths and public evidence gaps

Fifteen source-linked events place five chronology stages for each case in relative order. Oko contains a reported human challenge before escalation. The ZG710 record describes about one minute, incomplete identification evidence, human launch authorization, engagement, and loss. The F/A-18C record supports detection, correlation, a human engagement order, launch, and loss while leaving timing, display state, report independence, and feasible intervention unresolved. Horizontal spacing has no elapsed-time scale.

### Figure 4. Trust-evidence states across three public cases

Thirty-six declared states compare twelve trust-evidence propositions across three purposefully selected cases. Conditional reliability and calibrated uncertainty are unsupported in every packet. Record integrity is indeterminate in every packet. Evidence completeness is unsupported for Oko and F/A-18C and partially supported for ZG710. The figure supports proposition-level comparison and supplies no aggregate trust score or system ranking.

### Figure 5. Formal search retrieval and preliminary screening

Eight Semantic Scholar direct queries returned 184 records. Fourteen resolved seed chains returned 2,482 reference and citation records. The combined pool contained 2,666 records and 2,431 after deduplication. Preliminary AI-assisted triage proposed 12 retain-close, 13 retain-background, 77 attention, 1,239 topic-exclusion, 1,087 inaccessible, and 3 outside-cutoff records. The right panel uses a declared logarithmic count axis. Blue points identify the 89 records in the open author-decision queue. The display records search progress and supplies no completed-review or universal-originality finding.

### Figure 6. Evidence boundaries across six pre-action practical-control stages

Eighteen categorical findings cover six pre-action stages in each of three purposefully selected cases. Oko contains six partially supported findings. ZG710 contains one supported, one partially supported, and four unsupported findings. F/A-18C contains one supported, one partially supported, one unsupported, and three indeterminate findings. The stacked bars preserve the four categories. They assign no numeric distance among states and supply no missingness rate, reliability estimate, aggregate control score, or case ranking.

### Figure A1. Prespecified mutation responses

Twelve controlled mutation tests contain eleven prespecified assessment changes and three invariance conditions. Every expected change appeared, and all three invariance tests preserved the evidence assessments. The author designed the synthetic cases, mutation properties, assessment code, and oracle. The result establishes internal contract behavior for the committed fixtures and supplies no independent-reviewer agreement or field-validity estimate.

### Figure A2. Reproducibility lineage

The research lane traces frozen candidate collections through selection, packets, assessments, and a version archive. The figure lane traces committed inputs through two builders, nine derived CSV files, eighteen rendered files, and integrity checks. Hashes and declared transformations support ordering and file integrity. Source truth and completeness remain separate propositions.

### Figure A3. Claim-evidence integrity and conclusion eligibility

Six categorical decisions report traceability, integrity, support review, evidence fitness, dependency closure, and conclusion eligibility for twenty material claims. Every claim passes traceability, integrity, and support review. The independent-validity and final author-screening claims fail evidence fitness and remain ineligible. The matrix assigns no aggregate score and supplies no source-truth, independent-reliability, or claim-ranking result.

### Figure A4. Versioned correction of the Oko assessment

Six Oko pre-action states move from supported in v0.3.0 to partially supported in v0.6.0. The source packet remained fixed. The v0.6 protocol, frozen before reassessment, required direct and contemporaneous evidence for a supported state. The display records a method-driven correction and supplies no new historical evidence or error-frequency estimate.

## Missingness and uncertainty

Figure 2 and Figure 4 preserve indeterminate states where missing public records prevent a factual finding. Figure 3 uses relative sequence because the packets supply no common time scale. Figure 5 separates inaccessible records and an open author gate from completed decisions. Figure 6 preserves partial, unsupported, and indeterminate findings as separate categories. Figure A4 separates a classification change from a change in source evidence.

## Reproducibility check

`python analysis/build_figures.py --check` rebuilds the nine-figure core set in a temporary directory, compares the derived CSV files exactly, verifies PNG and SVG structure and dimensions, and checks the v0.8 manifests. `python analysis/build_claim_evidence_figure.py --check` performs the parallel check for Figure A3. The main repository validator runs both commands.

## Claim boundary

Three historical cases, including two cases from one system family and period, cannot estimate population frequency, effect size, causal impact, institutional effectiveness, or transfer to current learned systems. The mutation suite tests an author-designed contract. The formal-search triage remains provisional. These figures expose the present evidence and the limits on each inference.
