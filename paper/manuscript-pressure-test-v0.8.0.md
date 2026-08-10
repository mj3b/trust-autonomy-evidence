# Manuscript Pressure Test, v0.8.0 Candidate

## Decision

The manuscript supports a bounded methods-demonstration claim. It is not ready for journal submission because author screening, inaccessible-record review, authenticated database coverage, ethics guidance, and venue formatting remain open.

The pressure test examined citation resolution, repository readability, numeric consistency, assessment-state consistency, contribution language, coding-stability evidence, ethics language, and submission gates.

## Findings and resolutions

| ID | Finding | Evidence | Resolution |
|---|---|---|---|
| PT-01 | GitHub displayed raw citation syntax such as `[@bainbridge1983ironies]`. A repository reader could interpret the `@` symbol as a profile reference. | The source manuscript contains Pandoc citation identifiers. GitHub does not run a citation processor. | Added an explanation to the source manuscript and generated `manuscript-reader.md` with clickable author-year citations and a reference list. |
| PT-02 | Citation-identifier resolution passes. | The manuscript uses 38 distinct identifiers. All 38 map to entries in `references.bib`. | Added an executable reader-manuscript check that fails on an unresolved or surviving Pandoc citation. |
| PT-03 | Three bibliography entries remain unused in the current manuscript. | `gaube2026oversight`, `langer2025dagstuhl`, and `langer2025testing` appear in the working bibliography and have no current in-text citation. | Retained them as screened working-set records. They should enter the manuscript only when a sentence relies on them. |
| PT-04 | The manuscript status still identified the document as v0.4. | The repository released v0.7.0 and now contains a v0.8.0 candidate. | Updated the status to a pressure-tested v0.8.0 candidate. |
| PT-05 | The abstract described the literature result more firmly than the screening state allowed. | All 89 author-decision fields are blank, 1,087 records remain inaccessible, and authenticated databases remain open. | Recast the result as a frozen open-index search with provisional triage and placed the two open counts in the abstract. |
| PT-06 | A final search-flow figure is ineligible at the current checkpoint. | The queue contains 12 proposed close records and 77 proposed attention records with zero author decisions. | Preserved Figure 5 as preliminary and added an executable completion gate. The final label becomes eligible only after 89 valid author decisions. |
| PT-07 | The term “evidence missingness” could collapse partial support, indeterminate evidence, and evidence against a condition. | The assessment contract assigns different meanings to P, I, and U. | Added Figure 6 as an evidence-boundary composition. It preserves each state and assigns no missingness rate or aggregate score. |
| PT-08 | The repository had no compact table showing what coding-stability evidence exists. | Oko has two classifications under different evidence rules. Each Patriot case has one released classification. No independent second assessor exists. | Added Table A3. It records the available version comparison and marks reliability claims ineligible. |
| PT-09 | Numeric and state consistency pass. | Retrieval counts reconcile to 2,666 pooled and 2,431 deduplicated records. Preliminary classes sum to 2,431. Table 2 matches all 27 practical-control states. Figure 6 matches all 18 pre-action states. | Preserved the counts and added derived-data validation for Figure 6. |
| PT-10 | The ethics statement remains appropriately unresolved. | No institutional human-subjects determination or venue guidance has been recorded. | Preserved the statement that the author must obtain the applicable guidance before submission. |

## Claims currently eligible

The manuscript can claim that the frozen procedure generated traceable categorical findings for three purposefully selected public packets; separated formal authority from access, comprehension, feasibility, exercise, and effect; preserved indeterminate states; detected prespecified artifact corruptions; and recorded a versioned correction under a frozen evidence rule.

## Claims currently ineligible

The present record cannot support originality, inter-rater reliability, intra-rater stability, construct validity, prevalence, causal effects, institutional effectiveness, legal sufficiency, safety, field transfer, or improved outcomes.

## Submission gates

| Gate | Current state | Closure evidence |
|---|---|---|
| Author screening | Open, 0 of 89 complete | Completed decision and note fields, followed by rebuilt final screening counts |
| Inaccessible records | Open, 1,087 records | Documented retrieval attempts and final accessibility dispositions |
| Authenticated and disciplinary databases | Open | Exported query histories, deduplication results, and retained-source decisions |
| Ethics and publication authority | Open | Applicable Harvard and venue guidance recorded in submission notes |
| Venue package | Open | Anonymous manuscript, formatted tables and figures, declarations, and reporting checklist |
| Reliability evidence | Open | A frozen repeat-coding or independent-coding study with disagreements preserved |

## Next decision

The next research action is author screening. Closing the 89-record gate converts the literature section from provisional triage to a defensible reviewed set and permits the final search-flow figure. Authenticated database searching follows because it tests whether the retained set changes under sources unavailable to the open-index search.
