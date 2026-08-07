# Solo Validation Report, v0.2.0

## Decision

The v0.2.0 assessment contract produced the expected result for all 252 prespecified case determinations and all 12 mutation tests. This result demonstrates deterministic behavior for the committed synthetic fixtures and declared mutation properties.

## Test surface

| Measure | Result |
|---|---:|
| Synthetic cases | 12 |
| Trust-evidence determinations | 144 |
| Practical-control determinations | 108 |
| Oracle comparisons | 252 |
| Mutation tests | 12 |
| Expected mutation deltas | 11 |
| Invariance tests | 3 |
| Failures | 0 |

## Properties exercised

The suite tests positive, partial, indeterminate, unsupported, and outside-scope assessment states. It separates formal authority from feasible intervention, pre-action access from post-action notification, process evidence from outcome, integrity from truth, correction from reform, and autonomy profile changes from evidence-assessment changes.

The mutation suite tests eleven expected classification changes and three invariance conditions. Title, reported outcome, and impact-radius changes leave the trust and practical-control assessments unchanged under the current contract. Impact radius remains visible in the autonomy profile.

## Reproduction

```bash
python analysis/run_solo_validation.py --check
```

The command validates the JSON Schemas, verifies the sealed artifact hashes, evaluates every case, compares each determination with the committed oracle, applies every mutation, and confirms that the generated result and report are current.

## Claim boundary

The author designed the constructs, fixtures, rules, and oracle. Exact agreement therefore establishes internal artifact behavior. It does not estimate inter-rater reliability, independent usability, population validity, operational effectiveness, legal sufficiency, or outcome improvement.

The next evidence step available without volunteer reviewers is reconstruction of prespecified public cases using contemporaneous source packets and a published source-selection rule.
