# Manuscript Tables

These tables preserve exact states and counts behind the figures. The submission version should use three horizontal rules, no vertical rules, concise column labels, and a note below each table. The Markdown copies support repository reading. The [`booktabs` fragments](tables/manuscript-tables.tex) support journal typesetting.

## Table 1. Assessment-state decision rules

| State | Code | Decision rule |
|---|:---:|---|
| Supported | S | Direct, contemporaneous evidence satisfies the stage definition. |
| Partially supported | P | Some required elements are present and a material gap remains. |
| Unsupported | U | Available evidence contradicts the stage or shows that the condition was absent. |
| Indeterminate | I | The packet lacks enough evidence to decide. |
| Outside scope | O | The stage does not apply within the declared case boundary, with a written reason. |

*Note.* A missing record produces an indeterminate state unless the protocol or case design establishes that the record should exist. The states are categorical. No numeric distance or aggregate score is assigned.

## Table 2. Practical-control states across three public cases

| Stage | Oko, 1983 | Patriot ZG710, 2003 | Patriot F/A-18C, 2003 |
|---|:---:|:---:|:---:|
| Access before action | P | P | P |
| Comprehension | P | U | I |
| Formal authority | P | S | S |
| Feasible challenge | P | U | I |
| Exercised challenge | P | U | I |
| Protective effect | P | U | U |
| Correction | O | O | O |
| Repair | O | U | U |
| Institutional reform | P | S | S |

*Note.* S = supported; P = partially supported; U = unsupported; I = indeterminate; O = outside scope. The table reports 27 item-level findings from three purposefully selected cases. It supplies no frequency, causal, or population estimate.

## Table 3. Formal search and preliminary screening

| Stage | Record class | Count | Status |
|---|---|---:|---|
| Retrieval | Direct queries | 184 | Complete for the declared open-index queries |
| Retrieval | Citation chains | 2,482 | Fourteen of fifteen seed chains resolved |
| Pooling | Combined records | 2,666 | Before deduplication |
| Pooling | Deduplicated records | 2,431 | Unit for preliminary triage |
| Preliminary triage | Retain close | 12 | Author decision required |
| Preliminary triage | Retain background | 13 | Proposed background set |
| Preliminary triage | Attention records | 77 | Author decision required |
| Preliminary triage | Exclude topic | 1,239 | AI-assisted proposal |
| Preliminary triage | Inaccessible | 1,087 | Substantive screening unresolved |
| Preliminary triage | Outside cutoff | 3 | Published after the cutoff |
| Author gate | Open queue | 89 | Twelve close plus 77 attention records |

*Note.* The six preliminary triage classes sum to 2,431. The decisions are AI-assisted proposals. The 89-record author gate remains open. Authenticated database searching also remains open.

## Table A1. Versioned correction of the Oko assessment

| Stage | v0.3.0 | v0.6.0 | Material gap recorded in v0.6.0 |
|---|:---:|:---:|---|
| Access before action | S | P | No contemporaneous delivery, interface, or command record was located. |
| Comprehension | S | P | No contemporaneous reasoning, review, or explanation record was located. |
| Formal authority | S | P | No contemporaneous delegation or command-procedure record was located. |
| Feasible challenge | S | P | No contemporaneous timing or operating record was located. |
| Exercised challenge | S | P | No contemporaneous decision or communication log was located. |
| Protective effect | S | P | No contemporaneous linked action, stop, or escalation record was located. |

*Note.* The packet remained fixed. The v0.6.0 adjudication applied a protocol frozen before reassessment and admitted no new historical source. The correction records a change in evidence classification.

## Table A2. Figure and table interpretation boundaries

| Display | Directly reports | Does not establish |
|---|---|---|
| Figure 1 | Frozen selection order and stopping counts | Prevalence or representativeness |
| Figure 2 and Table 2 | Item-level practical-control states | A causal effect or aggregate control score |
| Figure 3 | Relative event order and public record gaps | A common elapsed-time scale |
| Figure 4 | Item-level trust-evidence states | A system ranking or aggregate trust score |
| Figure 5 and Table 3 | Retrieval counts, triage proposals, and the open author gate | A completed systematic review or universal originality |
| Figure 6 | Counts of four evidence states across six pre-action stages per case | A missingness rate, aggregate control score, reliability estimate, or case ranking |
| Figure A1 | Prespecified mutation responses | Independent reviewer agreement or field validity |
| Figure A2 | Artifact lineage and integrity checks | Source truth or completeness |
| Figure A3 | Claim gates and conclusion eligibility | Source truth, independent reliability, or a claim ranking |
| Figure A4 and Table A1 | A versioned evidence-classification correction | New historical evidence or an error-rate estimate |

*Note.* Each figure has a machine-readable CSV. The figure specifications and methods report the unit of analysis, transformation, supported claim, and prohibited interpretation.

## Table A3. Availability of coding-stability evidence

| Test condition | Oko, 1983 | Patriot ZG710, 2003 | Patriot F/A-18C, 2003 |
|---|:---:|:---:|:---:|
| A second coding exists | Yes | No | No |
| The same source packet was used | Yes | NA | NA |
| The same evidence rule was used | No | NA | NA |
| Comparable pre-action stages | 6 | 0 | 0 |
| Unchanged classifications | 0 | NA | NA |
| Changed classifications | 6 | NA | NA |
| Independent second assessor | No | No | No |
| Reliability claim eligible | No | No | No |

*Note.* Oko's six changes arose when the direct-and-contemporaneous rule was applied to the frozen packet. The comparison records a correction under a changed classification rule. It cannot estimate intra-rater stability or inter-rater reliability. The two Patriot cases have one released coding each.
