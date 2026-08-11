# Direct-Query Retrieval Tranche, v0.11.0

**Status:** `PARTIAL_SCREENING`

**Decision owner:** Mark Julius Banasihan

**Retrieval date:** 11 August 2026
**Frozen source sample:** [`inaccessible-risk-sample-v0.11.0.csv`](data/inaccessible-risk-sample-v0.11.0.csv)

## Decision served

The five direct-query records form the smallest complete stratum in the 284-record residual-risk sample. Reviewing this stratum first tests the lawful retrieval order and evidence ledger before the same procedure reaches 279 citation-chain records.

Selection membership was frozen before these results were known. This tranche changes retrieval and screening evidence. It does not change the sample, three research topics, project question, or public-case assessments.

## Results

| Sample | Source | Recovery | Screening decision | Review basis |
|---|---|---|---|---|
| RS-DQ-001 | Emery, *War by Algorithm* | Full text | `retain-background` | 220-page institutional dissertation |
| RS-DQ-002 | Homayounnejad, *Ensuring Lethal Autonomous Weapon Systems Comply with International Humanitarian Law* | Abstract | `retain-background` | Publisher abstract and stable PDF locator |
| RS-DQ-003 | Zabounidis et al., *Disentangled Concept-Residual Models* | Full text | `retain-background` | 18-page official TMLR paper |
| RS-DQ-004 | *Effective Human Oversight of GenAI-Powered Legal Research Tools* | Full text located | `OPEN` | 20-page publisher PDF rendered; readable text and author metadata require author review |
| RS-DQ-005 | Gielas, *The Loop Is Broken* | Abstract | `retain-close` | Publisher abstract and official issue summary |

All five records now have a lawful retrieval outcome. Four have a bounded screening decision. One remains open because the source can be rendered while its text cannot be inspected through the current retrieval channel. The machine record names B. Mills, and the publisher filename names Jennings. The repository carries that mismatch forward instead of choosing an identity without evidence.

## Findings that affect the paper

### A parallel path can defeat a formal correction

Zabounidis et al. provide a technical analogue for the paper's practical-control question. A person can correct a human-readable concept, yet the output may remain unchanged when an opaque residual path retains the same information. The mechanism supports a general caution: an available intervention has practical force only when it propagates through every path that can determine the outcome. Their experiments concern model architecture. They do not test institutions or public incidents.

### Human performance is now a closer comparison

Gielas directly challenges vague loop labels, centers the cognitive readiness of the operator, proposes a human-in-the-mesh model, and names the Patriot system. This source narrows the paper's contribution language. The repository may describe those declared features from the abstract. Any comparison of detailed mechanisms requires full-text review.

### Legal and historical sources remain background

Homayounnejad connects meaningful human control to international-humanitarian-law precautions for lethal autonomous weapons. Emery traces how algorithmic targeting and quantified risk can distance decision-makers from lethal action. Both help explain why formal assignment and technical precision can fail to establish practical human judgment. Neither inspected source supplies the paper's integrated selection, packet, missingness, correction, evidence-fitness, and executable-check procedure.

## Evidence path

The [machine-readable retrieval evidence](data/direct-query-retrieval-evidence-v0.11.0.json) records each route checked, locator, review basis, source observation, decision, assistance disclosure, and limit. The [population ledger](data/inaccessible-record-retrieval-v0.10.0.csv) records the five outcomes used by the gate report. The validator checks that the two records agree and refuses an unrecognized screening decision.

## Claim boundary

This tranche establishes five retrieval outcomes, four screening decisions, and one new close-source candidate. It does not estimate how many close sources remain among the other 1,082 inaccessible records. It does not close the 284-record residual-risk sample, the five authenticated interfaces, independent reliability, field validity, or institutional effects.

The next bounded action is author reading of RS-DQ-004 and full-text recovery for RS-DQ-005. After those two source-level limits are resolved, the same recorded procedure can move to the 102 forward-citation records.
