# v0.6.0 Claim-Evidence Figure Methods

## Result

Figure A3 converts the machine-readable v0.6 integrity-audit result into a categorical claim-gate matrix. It adds no evidence judgment and changes no claim state.

## Formal caption

**Figure A3. Evidence fitness determines conclusion eligibility.** The matrix displays five gate states and one conclusion-eligibility decision for 15 material claims declared in v0.6.0. Every mapped claim passes traceability. The versioned Oko correction closes the prior evidence-fitness and dependency failure within the declared procedure. The independent-validity claim remains ineligible. Letter labels preserve the states without relying on color. The figure assigns no numeric score.

## Transformation

The builder reads `audits/v0.6.0/audit-results.json`, preserves the five categorical gate states, converts the boolean eligibility field into `eligible` or `blocked`, and writes one row per claim to `figures/data/fig-a3-claim-evidence-integrity.csv`.

The v0.6 figure manifest records the builder, specification, claim map, audit result, derived data, SVG, and PNG. The validator rebuilds the CSV exactly, checks image structure and dimensions, and verifies the committed manifest hashes.

## Interpretation boundary

The matrix shows whether the committed v0.6 contract permits a mapped claim to support a conclusion. It supplies no aggregate trust score, source-truth determination, independent reliability estimate, field-validity result, or originality finding.
