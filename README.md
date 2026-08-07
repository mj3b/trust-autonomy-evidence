# Trust, Autonomy, and Evidence

[![Status: Working Research](https://img.shields.io/badge/status-working%20research-5b6cff)](RESEARCH_STATUS.md)
[![Version: 0.1.0](https://img.shields.io/badge/version-0.1.0-blue)](CHANGELOG.md)
[![Validation](https://github.com/mj3b/trust-autonomy-evidence/actions/workflows/validate.yml/badge.svg)](https://github.com/mj3b/trust-autonomy-evidence/actions/workflows/validate.yml)
[![License: Apache 2.0](https://img.shields.io/badge/license-Apache%202.0-green)](LICENSE)
[![ORCID](https://img.shields.io/badge/ORCID-0009--0001--8121--2878-brightgreen)](https://orcid.org/0009-0001-8121-2878)

## The problem

Institutions increasingly allow AI systems to recommend, plan, communicate, or act across consequential workflows. Claims that these systems are trusted, trustworthy, or subject to human control often leave the evidentiary test unspecified.

This repository asks:

> **What evidence justifies reliance on an autonomous AI system, and what evidence shows that institutional authority can still detect, interrupt, correct, and repair its actions?**

The project develops an evidence architecture for bounded reliance. It identifies the object of reliance, the action being permitted, the governing conditions, and the records an independent reviewer would need to inspect.

## Current contribution

Version 0.1.0 contributes four connected artifacts:

1. A conceptual model separating trust, trustworthiness, reliance, justified reliance, and calibration.
2. A six-variable autonomy profile covering goal scope, action authority, temporal horizon, impact radius, oversight distance, and reversibility.
3. A seven-level evidence ladder from assertion through longitudinal accountability.
4. A documentary test for practical human control across access, comprehension, authority, feasibility, exercise, effect, correction, repair, and reform.

These artifacts organize evidence claims. They have not been validated as predictors of safer decisions or better institutional outcomes.

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
├── LICENSE
├── scripts/
│   └── validate_repository.py
├── research/
│   └── trust-autonomy-and-evidence.md
├── evidence/
│   └── trust-evidence-register.md
├── protocols/
│   ├── independent-review-protocol.md
│   └── practical-human-control-test.md
├── cases/
│   └── README.md
└── mappings/
    ├── governed-decision-intelligence.md
    ├── human-influence-telemetry.md
    ├── cdfi-framework.md
    └── cdcf-governance.md
```

## How to read the repository

Start with [Trust, Autonomy, and Evidence](research/trust-autonomy-and-evidence.md). Use the [Trust Evidence Register](evidence/trust-evidence-register.md) to translate a reliance claim into inspectable evidence. Read [CLAIMS.md](CLAIMS.md) and [LIMITATIONS.md](LIMITATIONS.md) before applying the model.

The two protocols define future evaluation work. The mapping files show how this project relates to existing public artifacts without transferring claims among them.

## Repository validation

Run the dependency-free validator with Python 3.10 or later:

```bash
python scripts/validate_repository.py
```

The validator checks required files, internal Markdown links, version alignment, duplicate claim identifiers, and exclusion of private candidacy language. A successful run ends with `repository validation: PASS`.

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

Contributions should identify the proposition being changed, the evidence supporting the change, the limits of that evidence, and the conditions that would reverse the conclusion. Case material must exclude personal, confidential, and institutionally restricted information unless the contributor has documented authority to publish it.

## Citation

Machine-readable citation metadata appears in [CITATION.cff](CITATION.cff). Cite an archived release once one is available.

## Author

Mark Julius Banasihan is an independent applied researcher studying decision authority, human influence, evaluation, and assurance in AI-mediated institutional systems.

[GitHub](https://github.com/mj3b) | [ORCID](https://orcid.org/0009-0001-8121-2878)
