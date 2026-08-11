# v0.12.0 Chain-of-Evidence Audit Plan

## Objective

Test whether the twenty-seven claims declared in `TAE-COE-V0.12.0` resolve to exact evidence, retain intact files, pass claim-specific fitness judgments, and obey support and conclusion gates.

## Added scope

The v0.12.0 increment adds one numerical workflow claim for the 102-record forward-citation tranche. The audit must keep that claim outside the eligible conclusion set while author review of its routes and outcomes remains pending. It must also keep all 71 recovered sources outside manuscript claims until screening decisions are recorded.

## Checks

1. Recompute declared values from the retrieval evidence and queue.
2. Validate the claim map, lineage record, mutation suite, and audit result against their schemas.
3. Resolve every file, heading, text marker, JSON pointer, and CSV record.
4. Verify the method and implementation markers for the forward-citation workflow.
5. Recompute evidence fitness, dependency closure, support state, and conclusion eligibility.
6. Verify that pending source review produces an indeterminate support gate for `PAPER-C33`.
7. Run the twenty-two existing controlled corruptions and confirm that their expected checks detect them.

## Decision rule

A required failed or indeterminate gate prevents conclusion eligibility. A published exception may preserve a review checkpoint when the affected claim remains ineligible and the open author queue grants no claim permission.

Version 0.12.0 may be released only if all twenty-seven claims resolve as declared, all twenty-two negative controls are detected, the five exceptions are visible, and `PAPER-C32` and `PAPER-C33` remain conclusion-ineligible.

## Preservation rule

The v0.11 release manifest preserves the prior 26-claim map and audit outputs by hash. The v0.12 builder reconstructs that claim set, refreshes current-file hashes, and appends `PAPER-C33`. Earlier tagged audit outputs remain release history.

## Declared limits

The audit supplies an internal integrity result. It supplies no independent reliability, field-validity, originality, systematic-review, institutional-transfer, or outcome-effectiveness finding.
