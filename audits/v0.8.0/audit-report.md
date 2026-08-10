# v0.8.0 Chain-of-Evidence Integrity Audit

**Audit date:** 2026-08-10  
**Status:** `PASS_WITH_EXCEPTIONS`  
**Scope:** Twenty material claims declared in TAE-COE-V0.8.0, including the reader manuscript, Figure 6, Table A3, and the author-screening gate. Independent validity, final author screening, and authenticated database coverage remain outside the completed evidence base.

## Decision

The declared v0.8 claim set passes its executable integrity controls with three published exceptions. The new reader manuscript, Figure 6, Table A3, and author-screening gate resolve to their declared evidence. The open screening gate prevents final literature-screening conclusions. The result permits bounded artifact and method claims and supplies no independent reliability, originality, or completed systematic-search finding.

## Integrity checks

| Check | State | Tested | Passed | Failed | Indeterminate |
|---|---:|---:|---:|---:|---:|
| score_verification | pass | 30 | 30 | 0 | 0 |
| specification_violation | pass | 20 | 20 | 0 | 0 |
| reference_verification | pass | 20 | 20 | 0 | 0 |
| method_code_alignment | pass | 5 | 5 | 0 | 0 |
| evidence_fitness_and_dependency_closure | pass_with_exceptions | 20 | 18 | 2 | 0 |

## Claim gates

| Claim | Traceability | Integrity | Support | Fitness | Closure | Conclusion eligible |
|---|---|---|---|---|---|---|
| PAPER-C02 | pass | pass | pass | pass | pass | yes |
| PAPER-C03 | pass | pass | pass | pass | pass | yes |
| PAPER-C04 | pass | pass | pass | pass | pass | yes |
| PAPER-C05 | pass | pass | pass | pass | pass | yes |
| PAPER-C06 | pass | pass | pass | pass | pass | yes |
| PAPER-C07 | pass | pass | pass | pass | pass | yes |
| PAPER-C08 | pass | pass | pass | pass | pass | yes |
| PAPER-C09 | pass | pass | pass | pass | pass | yes |
| PAPER-C11 | pass | pass | pass | pass | pass | yes |
| PAPER-C14 | pass | pass | pass | pass | pass | yes |
| PAPER-C15 | pass | pass | pass | pass | pass | yes |
| TAE-C21 | pass | pass | pass | pass | pass | yes |
| TAE-C23 | pass | pass | pass | fail | outside_scope | no |
| TAE-C24 | pass | pass | pass | pass | pass | yes |
| TAE-C25 | pass | pass | pass | pass | pass | yes |
| PAPER-C22 | pass | pass | pass | pass | pass | yes |
| PAPER-C23 | pass | pass | pass | pass | pass | yes |
| PAPER-C24 | pass | pass | pass | pass | pass | yes |
| PAPER-C25 | pass | pass | pass | pass | pass | yes |
| PAPER-C26 | pass | pass | pass | fail | pass | no |

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
| COE-NC-10 | score_verification | yes |
| COE-NC-11 | reference_verification | yes |
| COE-NC-12 | reference_verification | yes |
| COE-NC-13 | evidence_fitness_and_dependency_closure | yes |
| COE-NC-14 | method_code_alignment | yes |

All 14 controls run on in-memory copies. The committed evidence files remain unchanged.

## Published exceptions

- `COE-EX-03`: no independent assessor has reproduced the support or evidence-fitness judgments.
- `COE-EX-04`: authenticated database searching, inaccessible-record review, and full citation chaining remain incomplete.
- `COE-EX-05`: all 89 author-screening decisions remain open, so final search-flow conclusions are blocked.

## Interpretation

A passing control shows that the audit detected the prespecified corruption. It does not show that the underlying source is true. Human support review, claim-specific fitness, and conclusion closure remain separate gates for that reason.

The full machine-readable result is [`audit-results.json`](audit-results.json). The protocol is [`protocols/coe-integrity-audit.md`](../../protocols/coe-integrity-audit.md).
