# v0.9.0 Chain-of-Evidence Audit Plan

## Objective

Test whether the twenty declared claims in `TAE-COE-V0.9.0` resolve to the cited artifacts, retain intact file evidence, pass claim-specific fitness judgments, and obey dependency and conclusion gates.

## Added scope

The v0.9.0 increment replaces the open author-screening checkpoint with 89 accountable author decisions. It tests the closed gate, final screening counts, final Figure 5 data, and the retained coverage limits.

## Checks

1. Recompute declared values from JSON and CSV evidence.
2. Validate the claim map, lineage record, mutation suite, and audit result against their schemas.
3. Resolve every file, heading, text marker, JSON pointer, and CSV cell.
4. Verify paired method and implementation markers.
5. Recompute evidence fitness, dependency closure, and conclusion eligibility.
6. Inject fourteen controlled corruptions into in-memory copies and confirm that the expected checks detect them.

## Decision rule

A required failed or indeterminate gate prevents conclusion eligibility. A published exception preserves a bounded repository claim only when the affected conclusion stays outside the eligible claim set.

## Declared limits

The audit supplies an internal integrity result. It supplies no independent reliability, field-validity, originality, systematic-review, or outcome-effectiveness finding.
