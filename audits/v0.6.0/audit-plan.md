# v0.6.0 Chain-of-Evidence Audit Plan

## Decision

Audit the declared v0.6 material claims after the Oko correction and sentence-level literature review. Reuse the four ScientistOne integrity checks and the repository's evidence-fitness and dependency-closure check.

## Frozen inputs

- `evidence/claim-evidence-map.json`
- `evidence/research-lineage.json`
- `fixtures/coe-audit-mutations.json`
- `schemas/claim-evidence-map.schema.json`
- `schemas/coe-audit-result.schema.json`

## Acceptance rule

All schemas must validate, all locators and expected values must resolve, all exact hashes or release-manifest records must match, declared eligibility must equal computed eligibility, and all nine negative controls must be detected.

Published exceptions do not convert an internal audit into independent validation.
