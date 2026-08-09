# v0.5.0 Integrity Audit Plan

## Decision

The release may be described as claim-traceable only if the mapped claim set validates, every negative control is detected, open exceptions remain visible, and blocked claims cannot enter a conclusion.

## Prespecified scope

The audit covers the claims enumerated in `evidence/claim-evidence-map.json`. It tests the paper's case-selection, case-state, Oko contemporaneity, artifact-validation, bounded-conclusion, and limitation claims together with the v0.5 method claims.

## Tests

| Gate | Pass condition |
|---|---|
| Schema | Claim map, lineage, mutation suite, and results validate against their schemas. |
| Traceability | Every path and locator resolves. |
| Integrity | Every required local artifact has a verifiable hash or appears in a preserved release manifest. |
| Support | A human support attestation is recorded, or the claim remains indeterminate. |
| Fitness | Every required fitness dimension passes; failures and indeterminate states remain visible. |
| Closure | A conclusion is eligible only when its own gates and every dependency pass. |
| Controls | All nine prespecified corruptions are detected by the expected check. |
| Paper | The independent paper-workspace validator passes. |

## Expected exceptions

- `COE-EX-01`: the Oko contemporaneity mismatch blocks protocol-consistency claims and dependent paper conclusions.
- `COE-EX-02`: sentence-level support review for the complete literature discussion remains unfinished.
- `COE-EX-03`: no independent assessor has reproduced the support and fitness judgments.

These exceptions produce `PASS_WITH_EXCEPTIONS` when the controls pass. An escaped negative control, broken artifact, undeclared dependency, or incorrectly eligible blocked claim produces `FAIL`.

## Preservation rule

The audit operates on copies for negative controls. It does not change the frozen v0.3.0 case assessments or the v0.4.0 figures.
