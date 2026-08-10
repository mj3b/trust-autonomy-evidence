# v0.8.0 Chain-of-Evidence Audit Plan

## Objective

Test whether the twenty declared claims in `TAE-COE-V0.8.0` resolve to the cited artifacts, retain intact file evidence, pass claim-specific fitness judgments, and obey dependency and conclusion gates.

## Added scope

The v0.8.0 increment adds five claims covering the reader manuscript, Figure 6, Table A3, the author-screening checkpoint, and the blocked final screening conclusion.

## Checks

1. Recompute declared values from JSON and CSV evidence.
2. validate the claim map, lineage record, mutation suite, and audit result against their schemas.
3. resolve every file, heading, text marker, JSON pointer, and CSV cell.
4. verify paired method and implementation markers.
5. recompute evidence fitness, dependency closure, and conclusion eligibility.
6. inject fourteen controlled corruptions into in-memory copies and confirm that the expected checks detect them.

## Decision rule

A required failed or indeterminate gate prevents conclusion eligibility. A published exception may preserve a bounded repository claim, but it cannot convert an unsupported research conclusion into a supported one.

## Declared limits

The audit supplies an internal integrity result. It supplies no independent reliability, field-validity, originality, systematic-review, or outcome-effectiveness finding.
