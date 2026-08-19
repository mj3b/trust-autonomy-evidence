# v0.16.0 Chain-of-Evidence Audit Plan

## Objective

Test whether the 40 claims declared in `TAE-COE-V0.16.0` resolve to exact evidence, retain intact files, pass claim-specific fitness judgments, close declared dependencies, and preserve the limits on the new formal and case-level statements.

## Added scope

The v0.16 increment preserves the earlier research record and adds five manuscript claims:

1. the six-stage event-control rule;
2. deterministic case-level results derived from released states;
3. the bounded conclusion that none of the three selected cases passes;
4. a proposed timing-margin measure that is not applied to the historical packets; and
5. the interpretation of the released `effect` field as execution propagation, without a beneficial-outcome or counterfactual-effect claim.

## Checks

1. Validate the claim map, lineage record, mutation suite, and audit result against their schemas.
2. Recompute the three case-level results directly from the released assessment JSON.
3. Confirm that the manuscript, protocol, table register, figures, and LaTeX source use the same six-stage terminology and decision rule.
4. Confirm that the timing equation is labeled as a proposal and that the missing historical timestamps remain visible.
5. Recompute support, evidence fitness, dependency closure, and conclusion eligibility for all 40 claims.
6. Run 39 controlled corruptions and confirm that each prespecified check detects its target failure.
7. Preserve independent review, present-system transfer, open search coverage, venue acceptance, and peer review as external gates.

## Decision rule

The v0.16 claims pass the internal integrity audit only when every new evidence locator resolves, exact case results match the deterministic builder, all claim dependencies close, and every controlled corruption is detected. This decision addresses repository consistency. It does not validate the historical interpretations.

## Preservation rule

Earlier releases, the Zenodo v0.14.0 preprint, and the v0.15.0 venue package remain unchanged release history. Version 0.16.0 records a new formal interpretation of the released states and does not rewrite the underlying case packets.

## Declared limits

The audit supplies an internal integrity result. It supplies no independent reliability, construct validity, source truth, prevalence estimate, causal effect, safety result, legal conclusion, current-system transfer, institutional-effect finding, platform acceptance, or peer review.
