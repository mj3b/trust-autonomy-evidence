# v0.15.0 Chain-of-Evidence Integrity Audit

**Audit date:** 2026-08-18

**Status:** `PASS_WITH_EXCEPTIONS`

**Scope:** Thirty-five material claims declared in TAE-COE-V0.15.0, including the closed v0.14 research claims, the Zenodo prior-version trace, independent Node & Norm author metadata, a specific Harvard University student-status note, and an open final-submission gate. Independent validity, 980 retrieval outcomes, authenticated database coverage, the 177-record backward-reference stratum, institutional transfer, platform acceptance, and peer review remain outside the completed evidence base.

## Decision

The declared v0.15 claim set preserves the v0.14 research gates and adds two supported venue-provenance claims. The final-submission claim remains ineligible because conflict confirmation, compiled-PDF inspection, upload review, and exact submitted-file hashes are open. All 33 controlled corruptions remain detected. The result supplies no independent reliability, originality, institutional-transfer, platform-acceptance, peer-review, or completed systematic-search finding.

## Integrity checks

| Check | State | Tested | Passed | Failed | Indeterminate |
|---|---:|---:|---:|---:|---:|
| score_verification | pass | 74 | 74 | 0 | 0 |
| specification_violation | pass | 35 | 35 | 0 | 0 |
| reference_verification | pass_with_exceptions | 35 | 34 | 0 | 1 |
| method_code_alignment | pass | 10 | 10 | 0 | 0 |
| evidence_fitness_and_dependency_closure | pass_with_exceptions | 35 | 32 | 1 | 2 |

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
| PAPER-C33 | pass | pass | pass | pass | pass | yes |
| PAPER-C34 | pass | pass | pass | pass | pass | yes |
| PAPER-C35 | pass | pass | pass | pass | pass | yes |
| PAPER-C36 | pass | pass | pass | pass | pass | yes |
| PAPER-C37 | pass | pass | pass | pass | pass | yes |
| PAPER-C38 | pass | pass | pass | pass | pass | yes |
| PAPER-C39 | pass | pass | pass | pass | pass | yes |
| PAPER-C40 | pass | pass | pass | pass | pass | yes |
| PAPER-C41 | pass | pass | indeterminate | indeterminate | pass | no |

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
| COE-NC-23 | score_verification | yes |
| COE-NC-24 | reference_verification | yes |
| COE-NC-25 | evidence_fitness_and_dependency_closure | yes |
| COE-NC-26 | method_code_alignment | yes |
| COE-NC-27 | score_verification | yes |
| COE-NC-28 | reference_verification | yes |
| COE-NC-29 | reference_verification | yes |
| COE-NC-30 | evidence_fitness_and_dependency_closure | yes |
| COE-NC-31 | method_code_alignment | yes |
| COE-NC-32 | evidence_fitness_and_dependency_closure | yes |
| COE-NC-33 | reference_verification | yes |

All 33 controls run on in-memory copies. The committed evidence files remain unchanged.

## Published exceptions

- `COE-EX-03`: no independent assessor has reproduced the support or evidence-fitness judgments.
- `COE-EX-04`: authenticated database searching, 980 retrieval outcomes, and the 177-record backward-reference stratum remain incomplete.
- `COE-EX-06`: RS-DQ-004 is closed for screening, yet readable text and author identity remain unresolved; RS-DQ-005 remains restricted to its abstract.
- `COE-EX-07`: PAPER-C32 remains provisional because one model-architecture study cannot establish institutional or public-incident transfer.
- `COE-EX-10`: PAPER-C41 remains provisional until the author confirms the conflict declaration, inspects the compiled v0.15 PDF, reviews the Preprints.org upload, and freezes the submitted-file hashes.

## Closed exception

- `COE-EX-05` closed when Mark Julius Banasihan recorded all 89 author decisions and the final search-flow data were rebuilt from the ledger.
- `COE-EX-08` closed when all 71 recovered forward-citation records received an author-authorized, AI-assisted screening decision and their claim permissions remained closed.
- `COE-EX-09` closed when all 13 close forward-citation sources received a proposition decision, five bounded permissions entered the manuscript, and six unresolved records remained quarantined.

## Interpretation

A passing control shows that the audit detected the prespecified corruption. It does not show that the underlying source is true. Human support review, claim-specific fitness, and conclusion closure remain separate gates for that reason.

The full machine-readable result is [`audit-results.json`](audit-results.json). The protocol is [`protocols/coe-integrity-audit.md`](../../protocols/coe-integrity-audit.md).
