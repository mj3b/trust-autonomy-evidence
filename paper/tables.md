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

## Table 3. Formal search and final screening state

| Stage | Record class | Count | Status |
|---|---|---:|---|
| Retrieval | Direct queries | 184 | Complete for the declared open-index queries |
| Retrieval | Citation chains | 2,482 | Fourteen of fifteen seed chains resolved |
| Pooling | Combined records | 2,666 | Before deduplication |
| Pooling | Deduplicated records | 2,431 | Unit for screening |
| Final screening | Retain close | 27 | Confirmed close set |
| Final screening | Retain background | 45 | Thirteen prior records plus 32 author-confirmed records |
| Final screening | Exclude single component | 10 | Relevant component without the tested combination |
| Final screening | Exclude topic | 1,259 | Outside the review question |
| Final screening | Inaccessible | 1,087 | Abstract absent; substantive screening unresolved |
| Final screening | Outside cutoff | 3 | Published after the cutoff |
| Author gate | Completed queue | 89 | All queued decisions recorded |

*Note.* The six final screening classes sum to 2,431. Mark Julius Banasihan is the decision owner for the 89-record queue, with disclosed AI assistance. The 1,087 inaccessible records and authenticated database searching remain separate coverage limits.

## Table 4. Proposal-to-author decision changes

| Proposed class | Records | Retain close | Retain background | Exclude topic | Exclude single component |
|---|---:|---:|---:|---:|---:|
| Retain close | 12 | 12 | 0 | 0 | 0 |
| Author attention | 77 | 15 | 32 | 20 | 10 |
| Total author queue | 89 | 27 | 32 | 20 | 10 |

*Note.* The author confirmed all 12 proposed close records. The 77 attention records produced 15 additional close sources and 32 background sources. These decisions close the declared author gate. They do not resolve the inaccessible-record or authenticated-database gates.

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
| Figure 5 and Tables 3 and 4 | Retrieval counts, final author decisions, and the closed 89-record author gate | A completed systematic review or universal originality |
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
