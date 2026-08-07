# Solo Validation Protocol

## Purpose

This protocol tests declared internal properties of the Trust, Autonomy, and Evidence assessment contract without external reviewers. It evaluates schema conformance, deterministic case classification, response to material evidence changes, and invariance under declared irrelevant changes.

The protocol does not estimate inter-rater reliability, independent usability, field validity, institutional effectiveness, or outcome improvement.

## Frozen materials

Version 0.2.0 freezes these materials before evaluation:

- twelve synthetic cases;
- twelve trust-evidence propositions;
- nine practical-control stages;
- six autonomy variables;
- an explicit classification oracle;
- twelve mutation properties;
- JSON Schemas for inputs and outputs;
- SHA-256 hashes for the case file, mutation file, and oracle.

The oracle manifest prevents silent revision of expected answers after the test runs. A change to any sealed artifact requires a new hash and a changelog entry.

## Assessment states

Each proposition receives one of five states:

- `supported`
- `partially_supported`
- `unsupported`
- `indeterminate`
- `outside_scope`

Missing evidence produces an indeterminate finding unless direct evidence establishes failure. A policy, assigned role, or declared process produces partial support until operational evidence satisfies the stronger condition.

## Case design

The twelve cases exercise:

1. complete pre-action control;
2. design evidence without operational proof;
3. missing evidence;
4. contradicted evidence;
5. formal authority without practical force;
6. post-action notification;
7. mutable records with exercised intervention;
8. successful outcome with weak process evidence;
9. failed outcome with strong process evidence;
10. broad autonomous action without oversight;
11. correction without institutional reform;
12. declared outside-scope stages.

The cases are constructed fixtures. Their distribution does not represent a population of deployed systems or institutional decisions.

## Mutation properties

Each mutation changes one or two declared facts in a base case. The test compares the full assessment before and after the change. It passes only when the complete set of observed classification changes equals the prespecified delta set.

The suite tests material changes involving access timing, authority, integrity, correction, monitoring, evidence completeness, repair, and governance reform. It also tests invariance under changes to case title, reported outcome, and impact radius. Impact radius remains part of the autonomy profile while leaving the evidence findings unchanged.

## Reproduction

Install the pinned development dependency and run:

```bash
python -m pip install -r requirements-dev.txt
python analysis/run_solo_validation.py --check
```

Use `--write` only when intentionally regenerating the committed assessment output and report after changing a source artifact.

## Acceptance rule

The release passes when:

1. every JSON Schema is valid;
2. every case and mutation document conforms to its schema;
3. every sealed artifact matches its recorded SHA-256 hash;
4. all 252 case determinations equal the prespecified oracle;
5. every mutation produces exactly its prespecified assessment deltas;
6. the generated results and report match the committed files;
7. repository validation and CI pass.

Any mismatch blocks the release until the relevant artifact, rule, oracle, claim, or limitation is revised transparently.

## Interpretation

Passing results demonstrate deterministic behavior for included fixtures and declared properties. The same author developed the constructs, rules, cases, and oracle, which creates circularity and confirmation risks. The report therefore supports only internal artifact claims.

Public-case reconstruction can extend the evidence without requiring volunteer reviewers. Such work must freeze the source-selection rule before case selection, preserve inaccessible evidence as a limitation, and avoid treating documentary completeness as proof of truth.
