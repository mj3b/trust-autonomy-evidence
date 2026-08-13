# Forward-Citation Author Screening Protocol, v0.13.0

**Status:** `FROZEN_BEFORE_AUTHOR_DECISIONS`

**Decision owner:** Mark Julius Banasihan

**Freeze date:** 11 August 2026

**Input:** the 71 recovered-content records in [`forward-citation-author-review-queue-v0.12.0.csv`](data/forward-citation-author-review-queue-v0.12.0.csv)

## Problem

Retrieval established that 71 forward-citation records expose an abstract or full-text route. It did not establish relevance. The next gate must decide which records could change the manuscript while preventing source discovery from becoming unrecorded claim support.

## Frozen order

Records are reviewed in ascending `sample_id` order. The sequence is divided into five twelve-record batches and one eleven-record batch. Batch boundaries organize the work; they do not change eligibility or decision rules.

## Permitted decisions

| Decision | Required basis | Meaning |
|---|---|---|
| `retain-close` | Source content directly addresses practical human control, evidence sufficiency, public-incident reconstruction, or the paper's combined assessment procedure. | The record can enter close-source review. |
| `retain-background` | Source content supplies a relevant mechanism, concept, domain comparison, or method component. | The record can enter background-source review. |
| `exclude-single-component` | Source content touches one relevant term or component without materially testing the paper's integration claim. | The record remains visible as a screened exclusion. |
| `exclude-topic` | Source content addresses another problem and supplies no material control or evidence mechanism for this paper. | The record remains visible as a topic exclusion. |
| `exclude-outside-cutoff` | The source falls after the frozen publication cutoff. | The record remains visible as a date exclusion. |
| `inaccessible` | The recorded route does not expose enough source content for a screening decision. | Relevance remains unresolved. |

## Evidence rule

An abstract can support a screening decision and an abstract-bounded description of the source's stated purpose or result. A substantive manuscript proposition requires a separate full-text check with a page, section, table, figure, or stable paragraph locator. A full-text route supports screening only until the retained proposition receives that locator-level review.

Every decision records the inspected basis, locator, rationale, decision owner, review date, and assistance disclosure. A rationale must name the source mechanism that controls the decision. Title similarity alone cannot support `retain-close`.

## Claim permission

Screening decides corpus membership. It grants no manuscript proposition permission. Retained records receive `none-until-proposition-review`; excluded records receive `none-excluded`; unresolved records receive `none-unresolved`.

## Assistance and authority

Codex may locate and inspect the recorded source content, summarize the bounded basis, and propose a decision. Mark Julius Banasihan authorized this execution and remains accountable for the decision ledger and any later manuscript use. The record describes the assistance directly; it does not imply independent assessment or unassisted author reading.

## Completion conditions

The gate closes only when all 71 records have one permitted decision, a non-empty rationale, an inspected basis, a source locator, the decision owner, the review date, and a permitted claim state. The validator must recompute membership and decision counts from the ledger. Retained records remain outside manuscript claims until proposition-level review closes their separate support gate.

## Fixed limits

The completed gate will estimate the composition of the frozen 71-record recovered-content queue. It will not establish exhaustive coverage, originality, independent reliability, field validity, or the prevalence of close sources in the full 1,087-record recovery population.
