# v0.14.0 Chain-of-Evidence Audit Plan

## Objective

Test whether the 32 claims declared in `TAE-COE-V0.14.0` resolve to exact evidence, retain intact files, pass claim-specific fitness judgments, close declared dependencies, and obey manuscript-permission rules.

## Added scope

The v0.14 increment reviews all 13 forward-citation sources classified close in v0.13. It permits five bounded propositions, retains two sources as background-only, and quarantines six. It also closes RS-DQ-004 for screening while preserving zero source-content permission.

## Checks

1. Recompute the 13 proposition decisions and their 5, 2, and 6 composition.
2. Validate frozen membership, order, required fields, stable locators, passage locators, fitness states, limitations, reversal conditions, and decision ownership.
3. Confirm that the five permitted sources resolve in the bibliography and manuscript.
4. Confirm that quarantined sources and RS-DQ-004 grant no proposition permission.
5. Validate the claim map, lineage record, mutation suite, and audit result against their schemas.
6. Recompute support, evidence fitness, dependency closure, and conclusion eligibility for all 32 claims.
7. Run 33 controlled corruptions and confirm that each prespecified check detects its target failure.
8. Seal every material v0.14 artifact in the release manifest after all other checks pass.

## Decision rule

A required failed or indeterminate gate prevents conclusion eligibility. A source proposition may enter the manuscript only when the review ledger records `manuscript-use`, the exact proposition and passage locator resolve, required fitness states pass, the bibliography and manuscript cite the source, and the author attestation is present.

Version 0.14.0 may be proposed for review only if all 32 claims resolve as declared, all 33 negative controls are detected, open exceptions remain visible, and quarantined sources retain zero proposition permission.

## Preservation rule

The v0.11 direct-query artifact and v0.13 screening artifacts remain unchanged release history. The v0.14 resolution and proposition-review files operate as overlays that preserve those earlier states.

## Declared limits

The audit supplies an internal integrity result. It supplies no independent reliability, field-validity, originality, systematic-review, source-truth, institutional-transfer, prevalence, or outcome-effectiveness finding.
