# v0.11.0 Chain-of-Evidence Audit Plan

## Objective

Test whether the twenty-six claims declared in `TAE-COE-V0.11.0` resolve to exact evidence, retain intact files, pass claim-specific fitness judgments, and obey dependency and conclusion gates.

## Added scope

The v0.11.0 increment adds one direct-query workflow claim, four bounded source-description claims, and one proposed cross-domain mechanism. The audit must keep the proposed mechanism outside the eligible conclusion set while its independence and completeness remain indeterminate.

## Checks

1. Recompute declared values from JSON and CSV evidence.
2. Validate the claim map, lineage record, mutation suite, and audit result against their schemas.
3. Resolve every file, heading, text marker, JSON pointer, and CSV cell.
4. Verify paired method and implementation markers.
5. Recompute evidence fitness, dependency closure, and conclusion eligibility.
6. Verify the recorded human-review attestation against the five direct-query evidence records and six added claims.
7. Inject twenty-two controlled corruptions into in-memory copies and confirm that the expected checks detect them.

## Decision rule

A required failed or indeterminate gate prevents conclusion eligibility. A published exception preserves a bounded claim only when the affected conclusion stays outside the eligible claim set.

Version 0.11.0 may be released only if all twenty-six mapped claims resolve as declared, all twenty-two negative controls are detected, the four exceptions are visible, and `PAPER-C32` remains conclusion-ineligible.

## Preservation rule

The v0.9 claim map and mutation fixture are preserved as named files. The v0.11 builder starts from that preserved map, refreshes hashes for the current evidence paths, and appends the six new claims. Earlier tagged audit outputs remain release history.

## Declared limits

The audit supplies an internal integrity result. It supplies no independent reliability, field-validity, originality, systematic-review, institutional-transfer, or outcome-effectiveness finding.
