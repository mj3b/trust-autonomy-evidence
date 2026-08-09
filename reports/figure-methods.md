# Figure Methods and Captions

## Result

Six figures expose the observations and transformations behind the repository's public-case and mutation findings. Four figures belong in a paper's main text. Figures A1 and A2 document internal contract behavior and artifact lineage in an appendix.

The figure set is version 0.1.0 and derives from the v0.3.0 public-case release and v0.2.0 solo-validation artifacts. It changes no assessment state, case boundary, source reference, packet hash, or release claim.

## Design rule

METR's time-horizon work defines a measured unit, shows observations, estimates a declared threshold, reports uncertainty, and publishes supporting data and methods. This repository applies the same discipline to categorical evidence. Each image names its unit of analysis, exposes the declared states or counts, preserves indeterminate findings, and ships with a derived CSV.

Supported, partially supported, unsupported, indeterminate, and outside scope remain categorical states. The builder assigns colors and letter codes for display. It assigns no numeric distance, rank, or aggregate score.

## Inputs and transformations

[`analysis/build_figures.py`](../analysis/build_figures.py) reads committed JSON artifacts and three plotting specifications. It writes six CSV files to [`figures/data/`](../figures/data/) and six PNG plus six SVG files to [`figures/generated/`](../figures/generated/).

The three plotting specifications perform narrow transcription tasks:

1. [`selection-decisions.json`](../figures/specifications/selection-decisions.json) extracts the five decisions already recorded in the public-case selection register.
2. [`decision-paths.json`](../figures/specifications/decision-paths.json) extracts five chronology stages and their source references from each case report.
3. [`reproducibility-lineage.json`](../figures/specifications/reproducibility-lineage.json) declares the artifact graph rendered in Figure A2.

The builder checks that the five plotted candidate identifiers match the first five preserved candidates. It also checks that every observed mutation delta equals its prespecified delta before Figure A1 is rendered.

## Formal captions

### Figure 1. Frozen selection and stopping

The AI Incident Database input contained 1,607 incident records and 7,452 report records, of which 828 matched the frozen search vocabulary. The OECD export contributed 100 candidate records, producing 928 preserved candidate records. The protocol screened the first five AIID candidates in fixed order, selected three cases, excluded two, and stopped when all three prespecified strata were filled. The remaining 923 records were unscreened and carry no exclusion decision. Purposeful stopping supplies no prevalence or representativeness estimate.

### Figure 2. Practical-control chain

Twenty-seven declared states compare nine practical-control propositions across three purposefully selected public cases. Formal authority is supported in all three cases. Oko supports the pre-action chain through protective effect. Patriot ZG710 supports authority while comprehension, feasibility, exercise, and effect are unsupported. Patriot F/A-18C supports authority while comprehension, feasibility, and exercise remain indeterminate because the public record omits timing, displays, and complete operator records. Letters identify categorical states: S, supported; PS, partially supported; U, unsupported; I, indeterminate; O, outside scope.

#### Derivation of the central lesson

The central lesson is derived through a declared comparison across the pre-action chain:

1. Extract the six pre-action states for each case: access, comprehension, authority, feasibility, exercise, and effect.
2. Identify the common state. Authority is supported in all three cases.
3. Compare the remaining five states with protective effect. Oko supports all five. ZG710 records partial access and unsupported comprehension, feasibility, exercise, and effect. F/A-18C records partial access, unresolved comprehension, feasibility, and exercise, and an unsupported effect.
4. Preserve unsupported and indeterminate as different findings. ZG710 contains evidence against several conditions. F/A-18C lacks enough public evidence to decide several conditions.
5. State the narrow inference. Formal authority alone does not establish practical control in these packets. Practical control requires an evidence path connecting information, understanding, permission, opportunity, action, and effect.

This derivation compares declared states within three reconstructed cases. It does not isolate a causal effect, estimate a population relationship, or establish that every condition has equal weight in another institutional setting.

### Figure 3. Reconstructed decision paths

Fifteen source-linked events place five bounded chronology stages for each case in relative order. Oko contains a documented human challenge before escalation. The ZG710 record describes about one minute, incomplete identification evidence, human launch authorization, engagement, and loss. The F/A-18C record supports detection, correlation, a human engagement order, launch, and loss while leaving timing, display state, report independence, and feasible intervention unresolved. Horizontal spacing has no elapsed-time scale.

### Figure 4. Trust-evidence states

Thirty-six declared states compare 12 trust-evidence propositions across three purposefully selected public cases. Conditional reliability and calibrated uncertainty are unsupported in every packet. Record integrity is indeterminate in every packet. Evidence completeness is unsupported for Oko and F/A-18C and partially supported for ZG710. The matrix supports bounded comparison of the committed assessments and supplies no aggregate trust score or system ranking.

### Figure A1. Mutation-response map

Twelve controlled mutation tests contain 11 prespecified assessment changes and three invariance conditions. Every expected state change appeared and all three invariant changes left the evidence assessments unchanged. The author designed the synthetic cases, mutation properties, assessment code, and oracle. The result establishes internal contract behavior for the committed fixtures and supplies no estimate of independent reviewer agreement or field validity.

### Figure A2. Reproducibility lineage

The research lane traces frozen candidate collections through fixed search rules, five recorded screening decisions, three source packets, machine-readable assessments, and the v0.3.0 archive. The figure lane traces committed plot inputs through the builder, six derived CSV files, 12 rendered image files, and an integrity check. Hashes and declared transformations support integrity, ordering, and traceability. Source truth and completeness remain separate propositions.


## Missingness and uncertainty

Figure 3 uses relative sequence because the public packets supply no defensible common time scale. The ZG710 packet alone reports an approximate one-minute decision window. Figure 2 preserves indeterminate states where missing public records prevent a factual finding. Figure 4 preserves outside-scope states where the bounded sequence provides no applicable post-action proposition.

## Reproducibility check

`python analysis/build_figures.py --check` rebuilds the figure set in a temporary directory and compares the six derived CSV files exactly with the committed tables. It verifies PNG and SVG structure and dimensions against the rebuild. It also checks the byte count and SHA-256 hash recorded for each of the 18 committed artifacts and each declared input. Image bytes can vary across operating systems because Matplotlib and its font renderer can encode the same plotted data differently. The main repository validator runs this command after schema, packet-hash, selection, interaction, release-manifest, and solo-suite checks.

## Claim boundary

Three historical cases, including two cases from one Patriot system family and operating period, cannot estimate population frequency, effect size, causal impact, institutional effectiveness, or transfer to current learned systems. The mutation suite tests an author-designed contract. These figures expose the present evidence and its limits.
