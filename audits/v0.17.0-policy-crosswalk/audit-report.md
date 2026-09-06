# v0.17.0 Policy Crosswalk Chain-of-Evidence Audit

**Audit date:** 2026-09-05

**Status:** `PASS_WITH_EXCEPTIONS`

**Scope:** Five bounded claims governing the targeted policy and standards crosswalk, the proposed EU AI Act regulatory-sandbox validation protocol, and their v0.17.0 manuscript use. The v0.16.0 historical findings remain unchanged.

## Decision

The audit confirms that five bounded claims resolve to the eight-record official-source ledger, the policy crosswalk, the sandbox protocol, the v0.17.0 manuscript section, the author attestation, and the validator. Nine in-memory mutations test numeric agreement, source resolution, manuscript integration, file integrity, evidence fitness, method-code alignment, dependency closure, and scope control. The historical case results and the v0.16.0 manuscript claim map remain unchanged.

## Integrity checks

| Check | State | Tested | Passed | Failed | Indeterminate |
|---|---:|---:|---:|---:|---:|
| score_verification | pass | 1 | 1 | 0 | 0 |
| specification_violation | pass | 5 | 5 | 0 | 0 |
| reference_verification | pass | 5 | 5 | 0 | 0 |
| method_code_alignment | pass | 1 | 1 | 0 | 0 |
| evidence_fitness_and_dependency_closure | pass | 5 | 5 | 0 | 0 |

## Claim gates

| Claim | Traceability | Integrity | Support | Fitness | Closure | Conclusion eligible |
|---|---|---|---|---|---|---|
| PAPER-C47 | pass | pass | pass | pass | pass | yes |
| PAPER-C48 | pass | pass | pass | pass | pass | yes |
| PAPER-C49 | pass | pass | pass | pass | pass | yes |
| PAPER-C50 | pass | pass | pass | pass | pass | yes |
| PAPER-C51 | pass | pass | pass | pass | pass | yes |

## Negative controls

| Control | Expected check | Detected |
|---|---|---|
| COE-NC-01 | score_verification | yes |
| COE-NC-02 | reference_verification | yes |
| COE-NC-03 | reference_verification | yes |
| COE-NC-04 | evidence_fitness_and_dependency_closure | yes |
| COE-NC-05 | method_code_alignment | yes |
| COE-NC-06 | evidence_fitness_and_dependency_closure | yes |
| COE-NC-07 | specification_violation | yes |
| COE-NC-08 | reference_verification | yes |
| COE-NC-09 | reference_verification | yes |

## Published exceptions

- `COE-EX-12`: the review is targeted to named provisions and official summaries and supplies no complete legal analysis, compliance finding, or ISO conformity assessment.
- `COE-EX-13`: no sandbox authority, system provider, participant group, or independent assessor has applied the proposed protocol.

## Interpretation

A detected mutation shows that the named control responded to a prespecified corruption. It supplies no evidence that the legal summary is complete or that the prospective method will work in a field setting. Those conclusions remain blocked by the published exceptions.
