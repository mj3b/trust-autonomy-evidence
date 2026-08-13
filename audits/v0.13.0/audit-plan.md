# v0.13.0 Chain-of-Evidence Audit Plan

## Objective

Test whether the twenty-eight claims declared in `TAE-COE-V0.13.0` resolve to exact evidence, retain intact files, pass claim-specific fitness judgments, and obey support and conclusion gates.

## Added scope

The v0.13.0 increment closes the frozen 71-record forward-citation screening gate. The audit tests the queue hash, ordered membership, decision counts, required rationales and disclosures, population-ledger agreement, decision ownership, and zero-permission rule. Screening can support a bounded corpus-composition claim. It cannot support a manuscript proposition from a retained source.

## Checks

1. Recompute the 102 retrieval outcomes and 71 screening decisions from their evidence records.
2. Validate the claim map, lineage record, mutation suite, and audit result against their schemas.
3. Resolve every file, heading, text marker, JSON pointer, and CSV record.
4. Verify the protocol and implementation markers for the forward-citation screening gate.
5. Recompute evidence fitness, dependency closure, support state, and conclusion eligibility.
6. Confirm that every retained source remains in `none-until-proposition-review` and every exclusion remains in `none-excluded`.
7. Run twenty-six controlled corruptions and confirm that their expected checks detect them.

## Decision rule

A required failed or indeterminate gate prevents conclusion eligibility. `PAPER-C33` and `PAPER-C34` may enter conclusions only as bounded statements about retrieval and screening workflow state. No source proposition enters the manuscript from those claims.

Version 0.13.0 may be released only if all twenty-eight claims resolve as declared, all twenty-six negative controls are detected, the four open exceptions remain visible, and `PAPER-C32` remains conclusion-ineligible.

## Preservation rule

The v0.12 tag preserves the prior 27-claim map and open screening boundary. The v0.13 builder reconstructs the prior claim set, replaces the forward-retrieval claim with its reviewed state, and appends `PAPER-C34`. Earlier tagged audit outputs remain release history.

## Declared limits

The audit supplies an internal integrity result. It supplies no independent reliability, field-validity, originality, systematic-review, institutional-transfer, source-truth, or outcome-effectiveness finding.
