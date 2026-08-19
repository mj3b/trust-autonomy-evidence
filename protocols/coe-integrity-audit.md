# Chain-of-Evidence Integrity Audit

**Protocol origin:** 0.5.0

**Current audit scope:** `TAE-COE-V0.16.0`

**Decision served:** whether a material claim may enter a conclusion in this repository or its working paper

## Problem

A citation, file path, or hash establishes a connection. It does not establish that the connected evidence supports the claim, fits the claim's evidentiary demands, or closes every dependency behind a conclusion. This protocol tests those separate propositions.

## Unit of analysis

The unit is one declared claim in [`evidence/claim-evidence-map.json`](../evidence/claim-evidence-map.json). The current audit covers the 40 claims listed in that map. Other repository sentences remain outside this audit unless a later release adds them.

## Standing application rule

Exploratory notes may remain outside the claim map while their status is explicit. A data point, source observation, figure, finding, or release statement must enter the claim map before it supports a material conclusion. The five gates then apply. A changed artifact requires a rebuilt map and audit. A failed or indeterminate required gate remains visible and blocks the affected conclusion.

## Five gates

A claim receives a separate state for each gate:

1. **Traceability:** every declared evidence item resolves to an existing artifact and exact locator.
2. **Integrity:** a preserved hash or release manifest can detect a changed artifact. Remote-only and pending items remain indeterminate.
3. **Support:** a recorded human review attests that the evidence supports the bounded claim. An automated path check cannot supply this judgment.
4. **Evidence fitness:** the evidence is assessed for directness, contemporaneity, independence, completeness, and publication authority. A dimension may be outside scope when the claim does not require it.
5. **Dependency closure:** every declared prerequisite exists and is eligible for the proposed conclusion.

The allowed states are `pass`, `fail`, `indeterminate`, and `outside_scope`. Missing evidence does not become a negative factual finding.

## Evidence-fitness rule

The five dimensions answer different questions:

| Dimension | Question |
|---|---|
| Directness | Does the artifact bear directly on the proposition? |
| Contemporaneity | Was the evidence produced close enough to the event for this claim? |
| Independence | Does the claim require corroboration that is independent of the focal source or system? |
| Completeness | Does the record contain the material evidence needed for the claim's stated scope? |
| Publication authority | Does the source have an identified basis for publishing the asserted information? |

One failed required dimension makes evidence fitness fail. One indeterminate required dimension makes fitness indeterminate when no dimension fails. The rationale must explain why each dimension is required or outside scope.

## Conclusion-eligibility rule

A claim is eligible for use in a conclusion only when:

- its status is `supported`;
- traceability, integrity, support, evidence fitness, and dependency closure pass;
- every declared dependency is eligible; and
- no unresolved exception blocks the intended scope.

A failed or indeterminate required gate prevents conclusion use. The underlying observation may still be reported with its state and limitation.

## Four integrity checks adapted from CoE Integrity Audit

The executable audit applies four checks described by the ScientistOne artifact, plus one repository-specific closure check:

1. **Score verification:** compare declared numeric or categorical values with their exact source locations and preserve run type.
2. **Specification violation:** test the schemas, status rules, bounded-language declarations, and conclusion-eligibility rule.
3. **Reference verification:** resolve artifact paths and locators, then report missing human support review separately.
4. **Method-code alignment:** connect a methodological requirement to the implementation marker that enforces it.
5. **Evidence fitness and dependency closure:** recompute fitness and block conclusions whose required evidence or dependencies fail.

The names of the first four checks are adapted from ScientistOne. Their implementation and the fifth check are repository-specific. This adaptation does not claim authorship of the general Chain-of-Evidence architecture.

## Run-type rule

Numerical evidence must state whether it represents an individual run, selected run, best run, multi-run mean, failed run, excluded run, or post-hoc ablation. `not_applicable` is permitted for non-run evidence. Failed and excluded evidence remains preserved when it affects interpretation.

## Bounded-language rule

The terms `all`, `always`, `required`, `consistently`, `proves`, `guarantees`, and `state of the art` require an explicit scope justification in the claim map. The audit tests declarations in the map. It does not yet scan every prose sentence.

## Negative controls

The audit applies controlled corruptions to in-memory copies of the released claim map. The source files remain unchanged. Each control must be detected by its prespecified check:

- numeric mismatch;
- missing reference;
- removed support review;
- failed fitness dimension;
- removed method marker;
- unresolved dependency;
- stale hash;
- mislabelled run type; and
- unsupported bounded term.

A control that escapes detection fails the audit.

## Oko negative case

`PAPER-C04` and `TAE-C25` preserve `PAPER-BLOCKER-01`. Retrospective participant accounts trace to the released Oko packet and can support bounded claims about those accounts. The present record does not satisfy the practical-control protocol's requirement for contemporaneous evidence behind the stronger claim that all released `supported` states meet that rule. Contemporaneity therefore fails for that claim, and dependent conclusions remain ineligible.

## Audit authority

The executable checks establish internal contract behavior and artifact consistency. Mark Julius Banasihan remains the human reviewer of record for the declared support judgments. AI assistance is recorded in the research activity log. No independent assessor has reproduced the judgments.

## Current outputs

- [`audits/v0.16.0/audit-results.json`](../audits/v0.16.0/audit-results.json)
- [`audits/v0.16.0/audit-report.md`](../audits/v0.16.0/audit-report.md)
- [`audits/v0.16.0/audit-plan.md`](../audits/v0.16.0/audit-plan.md)
- [`audits/v0.16.0/exceptions.md`](../audits/v0.16.0/exceptions.md)
- [`evidence/human-review-attestation-v0.16.0.json`](../evidence/human-review-attestation-v0.16.0.json)
- [`fixtures/coe-audit-mutations.json`](../fixtures/coe-audit-mutations.json)

The v0.14.0 audit and attestation remain available in their versioned directories as historical records.

## Claim boundary

Passing the audit means the committed controls behaved as declared for the mapped claim set. It supplies no independent reliability estimate, source-truth determination, field-validity finding, or proof that an institution will make a better decision.
