# v0.5.0 Chain-of-Evidence Integrity Audit

**Audit date:** 2026-08-09  
**Status:** `PASS_WITH_EXCEPTIONS`  
**Scope:** Fourteen material claims declared in TAE-COE-V0.5.0; complete repository prose and independent validity are outside the audit.

## Decision

The declared v0.5 claim set passes its executable integrity controls with three published exceptions. The result permits bounded artifact and method claims. It does not clear the blocked Oko protocol-consistency conclusion or establish independent reliability.

## Integrity checks

| Check | State | Tested | Passed | Failed | Indeterminate |
|---|---:|---:|---:|---:|---:|
| score_verification | pass | 14 | 14 | 0 | 0 |
| specification_violation | pass | 14 | 14 | 0 | 0 |
| reference_verification | pass | 14 | 14 | 0 | 0 |
| method_code_alignment | pass | 3 | 3 | 0 | 0 |
| evidence_fitness_and_dependency_closure | pass_with_exceptions | 14 | 7 | 7 | 0 |

## Claim gates

| Claim | Traceability | Integrity | Support | Fitness | Closure | Conclusion eligible |
|---|---|---|---|---|---|---|
| PAPER-C02 | pass | pass | pass | pass | pass | yes |
| PAPER-C03 | pass | pass | pass | pass | pass | yes |
| PAPER-C04 | pass | pass | pass | fail | fail | no |
| PAPER-C05 | pass | pass | pass | pass | pass | yes |
| PAPER-C06 | pass | pass | pass | pass | pass | yes |
| PAPER-C07 | pass | pass | pass | pass | pass | yes |
| PAPER-C08 | pass | pass | pass | pass | pass | yes |
| PAPER-C09 | pass | pass | pass | fail | fail | no |
| PAPER-C11 | pass | pass | pass | pass | pass | yes |
| PAPER-C14 | pass | pass | pass | pass | pass | yes |
| TAE-C21 | pass | pass | pass | pass | pass | yes |
| TAE-C23 | pass | pass | pass | fail | outside_scope | no |
| TAE-C24 | pass | pass | pass | pass | fail | no |
| TAE-C25 | pass | pass | pass | pass | fail | no |

## Negative controls

| Control | Expected check | Detected |
|---|---|---|
| COE-NC-01 | score_verification | yes |
| COE-NC-02 | reference_verification | yes |
| COE-NC-03 | reference_verification | yes |
| COE-NC-04 | evidence_fitness_and_dependency_closure | yes |
| COE-NC-05 | method_code_alignment | yes |
| COE-NC-06 | evidence_fitness_and_dependency_closure | yes |
| COE-NC-07 | reference_verification | yes |
| COE-NC-08 | score_verification | yes |
| COE-NC-09 | specification_violation | yes |

All nine controls run on in-memory copies. The committed evidence files remain unchanged.

## Published exceptions

- `COE-EX-01`: Oko contemporaneity blocks the stronger protocol-consistency claim and dependent paper conclusion.
- `COE-EX-02`: complete sentence-level literature support review and systematic searching remain unfinished.
- `COE-EX-03`: no independent assessor has reproduced the support or evidence-fitness judgments.

## Interpretation

A passing control shows that the audit detected the prespecified corruption. It does not show that the underlying source is true. Human support review, claim-specific fitness, and conclusion closure remain separate gates for that reason.

The full machine-readable result is [`audit-results.json`](audit-results.json). The protocol is [`protocols/coe-integrity-audit.md`](../../protocols/coe-integrity-audit.md).
