# Manuscript Tables

These tables preserve exact states and counts behind the figures. The submission version should use three horizontal rules, no vertical rules, concise column labels, and a note below each table. The Markdown copies support repository reading. The [`booktabs` fragments](tables/manuscript-tables.tex) support journal typesetting.

## Table 1. Derivation of the event-level practical-control chain

| Stage | Prior construct | Why it is required | Minimum supporting record | Error prevented |
|---|---|---|---|---|
| Information access | Epistemic access and situation awareness | Judgment cannot act on information the person never received | Timestamped delivery, interface, or access record | Treating post-action notice as review |
| Comprehension capacity | Situation awareness and competent oversight | Delivery alone does not show that the person could interpret the information | Training, explanation, test, or contemporaneous reasoning record | Treating visibility as understanding |
| Intervention authority | Causal power and contestability | A person cannot control a decision without a right to change it | Delegation, procedure, or permission record | Treating responsibility as permission |
| Intervention feasibility | Preparedness, workload, and temporal opportunity | A formal right can be unusable under actual conditions | Timing, staffing, access, latency, or workload record | Treating theoretical authority as usable authority |
| Exercised judgment | Verification, contestation, and substitution | Available control says nothing about whether judgment occurred | Contemporaneous approve, reject, modify, stop, or escalate record | Inferring action from role assignment |
| Execution propagation | Causal contribution and decision-chain effect | A decision that never reaches execution cannot control the bounded event | Linked system or institutional record showing execution changed | Inferring operational effect from an unexecuted judgment |

*Note.* The released assessment JSON uses the field name `effect` for execution propagation. The manuscript term avoids implying that the change was beneficial or that it caused the final outcome.

## Table 2. Assessment-state decision rules

| State | Code | Decision rule |
|---|:---:|---|
| Supported | S | Direct, contemporaneous evidence satisfies the stage definition. |
| Partially supported | P | Some required elements are present and a material gap remains. |
| Unsupported | U | Available evidence contradicts the stage or shows that the condition was absent. |
| Indeterminate | I | The packet lacks enough evidence to decide. |
| Outside scope | O | The stage does not apply within the declared case boundary, with a written reason. |

*Note.* A missing record produces an indeterminate state unless the protocol or case design establishes that the record should exist. The states are categorical. No numeric distance or aggregate score is assigned.

## Table 3. Practical-control states across three public cases

| Stage | Oko, 1983 | Patriot ZG710, 2003 | Patriot F/A-18C, 2003 |
|---|:---:|:---:|:---:|
| Information access | P | P | P |
| Comprehension capacity | P | U | I |
| Intervention authority | P | S | S |
| Intervention feasibility | P | U | I |
| Exercised judgment | P | U | I |
| Execution propagation | P | U | U |
| Correction | O | O | O |
| Repair | O | U | U |
| Institutional reform | P | S | S |

*Note.* S = supported; P = partially supported; U = unsupported; I = indeterminate; O = outside scope. The first six rows determine the event-control result. Correction, repair, and institutional reform describe post-event response and do not alter that result. The table reports 27 item-level findings from three purposefully selected cases and supplies no frequency, causal, or population estimate.

## Table 4. Formal authority compared with event-level practical control

| Case | Authority state | Complete event-control result | Why |
|---|:---:|:---:|---|
| Oko, 1983 | P | Unresolved | All six required stages are partially supported; none reaches the direct-and-contemporaneous threshold. |
| Patriot ZG710, 2003 | S | Fail | Comprehension, feasibility, exercised judgment, and execution propagation are unsupported. |
| Patriot F/A-18C, 2003 | S | Fail | Execution propagation is unsupported; comprehension, feasibility, and exercised judgment are indeterminate. |

*Note.* A supported authority state establishes one required condition. It cannot substitute for the other five conditions. These results are derived from the released categorical states under the v0.16.0 decision rule.

## Table 5. Formal search and final screening state

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

## Table 6. Proposal-to-author decision changes

| Proposed class | Records | Retain close | Retain background | Exclude topic | Exclude single component |
|---|---:|---:|---:|---:|---:|
| Retain close | 12 | 12 | 0 | 0 | 0 |
| Author attention | 77 | 15 | 32 | 20 | 10 |
| Total author queue | 89 | 27 | 32 | 20 | 10 |

*Note.* The author confirmed all 12 proposed close records. The 77 attention records produced 15 additional close sources and 32 background sources. These decisions close the declared author gate. They do not resolve the inaccessible-record or authenticated-database gates.

## Table 7. Residual-risk retrieval and screening checkpoint

| Scope | State | Count | Claim boundary |
|---|---|---:|---|
| Forward-citation stratum | Retrieval outcomes recorded | 102 | Complete for the frozen stratum |
| Forward-citation stratum | Recovered content | 71 | Eligible for screening |
| Forward-citation stratum | Screening decisions | 71 | 13 close, 22 background, 11 single-component, 25 topic |
| Forward-citation stratum | Proposition permissions | 5 | Each permission is limited to one locator-bounded proposition |
| Forward-citation stratum | Background-only or quarantined | 8 | Two background-only; six quarantined |
| Direct-query stratum | Screening decisions | 5 of 5 | Screening closed; RS-DQ-004 has zero proposition permission |
| Recovery population | Retrieval outcomes | 107 of 1,087 | 980 retrieval outcomes remain open |
| Recovery population | Recovered-content decisions | 76 of 76 | All recovered content has a screening decision |

*Note.* These counts describe the frozen recovery workflow and the v0.14 proposition-review overlay. They supply no close-source prevalence estimate for the 1,087-record population because 980 retrieval outcomes remain open. Proposition permission is narrower than source inclusion and does not establish generalizability.

## Table A1. Versioned correction of the Oko assessment

| Stage | v0.3.0 | v0.6.0 | Material gap recorded in v0.6.0 |
|---|:---:|:---:|---|
| Information access | S | P | No contemporaneous delivery, interface, or command record was located. |
| Comprehension capacity | S | P | No contemporaneous reasoning, review, or explanation record was located. |
| Intervention authority | S | P | No contemporaneous delegation or command-procedure record was located. |
| Intervention feasibility | S | P | No contemporaneous timing or operating record was located. |
| Exercised judgment | S | P | No contemporaneous decision or communication log was located. |
| Execution propagation | S | P | No contemporaneous linked action, stop, or escalation record was located. |

*Note.* The packet remained fixed. The v0.6.0 adjudication applied a protocol frozen before reassessment and admitted no new historical source. The correction records a change in evidence classification.

## Table A2. Figure and table interpretation boundaries

| Display | Directly reports | Does not establish |
|---|---|---|
| Figure 1 | Frozen selection order and stopping counts | Prevalence or representativeness |
| Figure 2 and Tables 3 and 4 | Item-level practical-control states and derived case-level results | A causal effect, beneficial outcome, or aggregate control score |
| Figure 3 | Relative event order and public record gaps | A common elapsed-time scale |
| Figure 4 | Item-level trust-evidence states | A system ranking or aggregate trust score |
| Figure 5 and Tables 5 and 6 | Retrieval counts, final author decisions, and the closed 89-record author gate | A completed systematic review or universal originality |
| Figure 6 | Counts of four evidence states across six event-level stages per case | A missingness rate, aggregate control score, reliability estimate, or case ranking |
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
| Comparable event-level stages | 6 | 0 | 0 |
| Unchanged classifications | 0 | NA | NA |
| Changed classifications | 6 | NA | NA |
| Independent second assessor | No | No | No |
| Reliability claim eligible | No | No | No |

*Note.* Oko's six changes arose when the direct-and-contemporaneous rule was applied to the frozen packet. The comparison records a correction under a changed classification rule. It cannot estimate intra-rater stability or inter-rater reliability. The two Patriot cases have one released coding each.
