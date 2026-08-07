# Contributing

## Contribution standard

Every contribution must identify:

1. the proposition, protocol, schema, case, or mapping being changed;
2. the evidence supporting the change;
3. the claim that the evidence permits;
4. the claim that remains unsupported;
5. the tests or review conditions affected;
6. the migration effect for existing cases and results.

Changes to prose alone should resolve a defined ambiguity, omission, traceability problem, or interpretation risk.

## Case contributions

A case proposal must include a decision boundary, source manifest, provenance statement, inaccessible-evidence register, publication authority, redaction statement, and expected assessment purpose.

Synthetic cases must declare which properties are constructed. Public and operational cases must separate direct records, source claims, assessor inference, and unresolved uncertainty.

## Contract changes

A change to an assessment state, signal vocabulary, classification rule, schema, oracle, or mutation property requires:

- a new or revised fixture exposing the change;
- regenerated deterministic results;
- an updated oracle manifest when a sealed artifact changes;
- claim and limitation review;
- a changelog entry;
- passing repository validation.

## Validation

```bash
python -m pip install -r requirements-dev.txt
python scripts/validate_repository.py
```

Pull requests should preserve the full validator output and explain every expected result change.

## Sensitive material

Do not submit confidential, personal, security-sensitive, copyrighted, or institutionally restricted records without documented authority. Redaction must identify the assessment fields affected by removed information.

