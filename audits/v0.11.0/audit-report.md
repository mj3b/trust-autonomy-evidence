# v0.11.0 Chain-of-Evidence Integrity Audit

**Audit date:** 2026-08-11

**Status:** `PASS_WITH_EXCEPTIONS`

**Scope:** Twenty-six material claims declared in TAE-COE-V0.11.0, including the five-record direct-query state, four bounded source descriptions, and one provisional synthesis. Independent validity, 1,082 retrieval outcomes, authenticated database coverage, and institutional transfer remain outside the completed evidence base.

## Decision

The declared v0.11 claim set passes its executable integrity controls with four published exceptions. The five-record tranche count claim and four bounded source descriptions resolve to their declared evidence. The cross-domain synthesis remains conclusion-ineligible because independence and completeness are indeterminate. The result supplies no independent reliability, originality, institutional-transfer, or completed systematic-search finding.

## Integrity checks

| Check | State | Tested | Passed | Failed | Indeterminate |
|---|---:|---:|---:|---:|---:|
| score_verification | pass | 46 | 46 | 0 | 0 |
| specification_violation | pass | 26 | 26 | 0 | 0 |
| reference_verification | pass | 26 | 26 | 0 | 0 |
| method_code_alignment | pass | 6 | 6 | 0 | 0 |
| evidence_fitness_and_dependency_closure | pass_with_exceptions | 26 | 24 | 1 | 1 |

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
| PAPER-C26 | pass | pass | pass | pass | pass | yes |
| PAPER-C27 | pass | pass | pass | pass | pass | yes |
| PAPER-C28 | pass | pass | pass | pass | pass | yes |
| PAPER-C29 | pass | pass | pass | pass | pass | yes |
| PAPER-C30 | pass | pass | pass | pass | pass | yes |
| PAPER-C31 | pass | pass | pass | pass | pass | yes |
| PAPER-C32 | pass | pass | pass | indeterminate | pass | no |

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
| COE-NC-15 | score_verification | yes |
| COE-NC-16 | reference_verification | yes |
| COE-NC-17 | reference_verification | yes |
| COE-NC-18 | evidence_fitness_and_dependency_closure | yes |
| COE-NC-19 | method_code_alignment | yes |
| COE-NC-20 | evidence_fitness_and_dependency_closure | yes |
| COE-NC-21 | reference_verification | yes |
| COE-NC-22 | specification_violation | yes |

All 22 controls run on in-memory copies. The committed evidence files remain unchanged.

## Published exceptions

- `COE-EX-03`: no independent assessor has reproduced the support or evidence-fitness judgments.
- `COE-EX-04`: authenticated database searching, 1,082 retrieval outcomes, and the remaining risk-sample records remain incomplete.
- `COE-EX-06`: RS-DQ-004 remains open because readable text and author identity require resolution; RS-DQ-005 remains restricted to its abstract.
- `COE-EX-07`: PAPER-C32 remains provisional because one model-architecture study cannot establish institutional or public-incident transfer.

## Closed exception

- `COE-EX-05` closed when Mark Julius Banasihan recorded all 89 author decisions and the final search-flow data were rebuilt from the ledger.

## Interpretation

A passing control shows that the audit detected the prespecified corruption. It does not show that the underlying source is true. Human support review, claim-specific fitness, and conclusion closure remain separate gates for that reason.

The full machine-readable result is [`audit-results.json`](audit-results.json). The protocol is [`protocols/coe-integrity-audit.md`](../../protocols/coe-integrity-audit.md).
