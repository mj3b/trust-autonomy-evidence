# Trust, Autonomy, and Evidence

[![Status: Working Research](https://img.shields.io/badge/status-working%20research-5b6cff)](RESEARCH_STATUS.md)
[![Version: 0.2.0](https://img.shields.io/badge/version-0.2.0-blue)](CHANGELOG.md)
[![Validation](https://github.com/mj3b/trust-autonomy-evidence/actions/workflows/validate.yml/badge.svg)](https://github.com/mj3b/trust-autonomy-evidence/actions/workflows/validate.yml)
[![License: Apache 2.0](https://img.shields.io/badge/license-Apache%202.0-green)](LICENSE)
[![ORCID](https://img.shields.io/badge/ORCID-0009--0001--8121--2878-brightgreen)](https://orcid.org/0009-0001-8121-2878)

## The problem

Institutions increasingly allow AI systems to recommend, plan, communicate, or act across consequential workflows. Claims that these systems are trusted, trustworthy, or subject to human control often leave the evidentiary test unspecified.

This repository asks:

> **What evidence justifies reliance on an autonomous AI system, and what evidence shows that institutional authority can still detect, interrupt, correct, and repair its actions?**

The project develops an evidence architecture for bounded reliance. It identifies the object of reliance, the action being permitted, the governing conditions, and the records an independent reviewer would need to inspect.

## Current contribution

Version 0.2.0 contributes five connected artifacts:

1. A conceptual model separating trust, trustworthiness, reliance, justified reliance, and calibration.
2. A six-variable autonomy profile covering goal scope, action authority, temporal horizon, impact radius, oversight distance, and reversibility.
3. A seven-level evidence ladder from assertion through longitudinal accountability.
4. A documentary test for practical human control across access, comprehension, authority, feasibility, exercise, effect, correction, repair, and reform.
5. A solo-validation suite containing 12 synthetic cases, 252 prespecified determinations, 12 mutation tests, three invariance tests, and sealed oracle artifacts.

All 252 determinations and 12 mutation tests pass under the committed v0.2.0 contract. The result establishes deterministic behavior for the included fixtures. It does not establish independent reliability, field validity, institutional effectiveness, or improved outcomes.

## Repository map

```text
trust-autonomy-evidence/
├── README.md
├── RESEARCH_STATUS.md
├── CLAIMS.md
├── LIMITATIONS.md
├── SOURCES.md
├── CITATION.cff
├── CHANGELOG.md
├── CONTRIBUTING.md
├── GOVERNANCE.md
├── LICENSE
├── requirements-dev.txt
├── scripts/
│   └── validate_repository.py
├── schemas/
├── fixtures/
├── oracles/
├── assessments/
├── analysis/
├── reports/
├── research/
│   └── trust-autonomy-and-evidence.md
├── evidence/
│   └── trust-evidence-register.md
├── protocols/
│   ├── independent-review-protocol.md
│   ├── practical-human-control-test.md
│   └── solo-validation-protocol.md
├── cases/
│   └── README.md
└── mappings/
    ├── governed-decision-intelligence.md
    ├── human-influence-telemetry.md
    ├── cdfi-framework.md
    └── cdcf-governance.md
```

## How to read the repository

Start with [Trust, Autonomy, and Evidence](research/trust-autonomy-and-evidence.md). Use the [Trust Evidence Register](evidence/trust-evidence-register.md) to translate a reliance claim into inspectable evidence. Read the [solo-validation report](reports/solo-validation-v0.2.0.md), [CLAIMS.md](CLAIMS.md), and [LIMITATIONS.md](LIMITATIONS.md) before applying the model.

The three protocols define solo validation, practical-control assessment, and future independent evaluation. The mapping files show how this project relates to existing public artifacts without transferring claims among them.

## Repository validation

Install the pinned development dependency and run the validator with Python 3.10 or later:

```bash
python -m pip install -r requirements-dev.txt
python scripts/validate_repository.py
```

The validator checks required files, internal Markdown links, version alignment, duplicate claim identifiers, exclusion of private candidacy language, JSON Schema conformance, sealed hashes, 252 oracle comparisons, 12 mutation tests, and generated-output freshness. A successful run ends with `repository validation: PASS`.

## Research boundaries

This repository does not establish that:

- an AI system is generally safe or trustworthy;
- a complete decision record is truthful;
- a reviewer understood the evidence;
- formal human authority had practical force;
- a governance artifact satisfies a legal or normative requirement;
- the proposed evidence architecture improves outcomes.

Each proposition requires evidence from the deployment, institution, decision, and review context in which the claim is made.

## Contribution policy

Contributions should identify the proposition being changed, the evidence supporting the change, the limits of that evidence, and the conditions that would reverse the conclusion. See [CONTRIBUTING.md](CONTRIBUTING.md) and [GOVERNANCE.md](GOVERNANCE.md). Case material must exclude personal, confidential, and institutionally restricted information unless the contributor has documented authority to publish it.

## Citation

Machine-readable citation metadata appears in [CITATION.cff](CITATION.cff). Cite an archived release once one is available.

## Author

Mark Julius Banasihan is an independent applied researcher studying decision authority, human influence, evaluation, and assurance in AI-mediated institutional systems.

[GitHub](https://github.com/mj3b) | [ORCID](https://orcid.org/0009-0001-8121-2878)
