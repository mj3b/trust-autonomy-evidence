# v0.15.0 Chain-of-Evidence Audit Plan

## Objective

Test whether the 35 claims declared in `TAE-COE-V0.15.0` resolve to exact evidence, retain intact files, pass claim-specific fitness judgments, close declared dependencies, and keep the Preprints.org submission gate open until every author and platform condition is recorded.

## Added scope

The v0.15 increment preserves all v0.14 research claims and adds three venue claims: the Zenodo v0.14.0 relationship, the author identity and independent Node & Norm affiliation, and final submission readiness.

## Checks

1. Confirm that the Zenodo v0.14.0 DOI agrees across manuscript, venue metadata, and package documentation.
2. Confirm the full author name, ORCID, independent Node & Norm affiliation, Harvard University student-status note, independence disclaimer, and two correspondence addresses.
3. Record the author-confirmed conflict declaration, Overleaf compilation, and authorized visual inspection; preserve upload review and submitted-file hashes as open gates.
4. Validate the claim map, lineage record, mutation suite, and audit result against their schemas.
5. Recompute support, evidence fitness, dependency closure, and conclusion eligibility for all 35 claims.
6. Run 33 controlled corruptions and confirm that each prespecified check detects its target failure.
7. Seal the exact v0.15 source archive and compiled PDF only after author confirmation and visual inspection.

## Decision rule

`PAPER-C41` remains conclusion-ineligible while any final submission gate is open. The author confirmed the conflict declaration on 2026-08-18. Repository integrity does not establish platform acceptance or replace author inspection.

## Preservation rule

The Zenodo v0.14.0 preprint and all earlier repository releases remain unchanged release history. The v0.15 package records its relationship to that history and does not overwrite the prior files.

## Declared limits

The audit supplies an internal integrity result. It supplies no independent reliability, field-validity, originality, systematic-review, source-truth, institutional-transfer, platform-acceptance, peer-review, prevalence, or outcome-effectiveness finding.
