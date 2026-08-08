# Trust, Autonomy, and Evidence

[![Status: Working Research](https://img.shields.io/badge/status-working%20research-5b6cff)](RESEARCH_STATUS.md)
[![Version: 0.4.0](https://img.shields.io/github/v/release/mj3b/trust-autonomy-evidence?display_name=tag&label=release)](https://github.com/mj3b/trust-autonomy-evidence/releases)
[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.21841127.svg)](https://doi.org/10.5281/zenodo.21841127)
[![Validation](https://github.com/mj3b/trust-autonomy-evidence/actions/workflows/validate.yml/badge.svg)](https://github.com/mj3b/trust-autonomy-evidence/actions/workflows/validate.yml)
[![License: Apache 2.0](https://img.shields.io/badge/license-Apache%202.0-green)](LICENSE)
[![ORCID](https://img.shields.io/badge/ORCID-0009--0001--8121--2878-brightgreen)](https://orcid.org/0009-0001-8121-2878)

## The problem

Institutions increasingly allow AI systems to recommend, plan, communicate, or act across consequential workflows. Claims that these systems are trusted, trustworthy, or subject to human control often leave the evidentiary test unspecified.

This repository asks:

> **What evidence justifies reliance on an autonomous AI system, and what evidence shows that institutional authority can still detect, interrupt, correct, and repair its actions?**

The project develops an evidence architecture for bounded reliance. It identifies the object of reliance, the action being permitted, the governing conditions, and the records an independent reviewer would need to inspect.

## Current contribution

[Version 0.4.0](https://github.com/mj3b/trust-autonomy-evidence/releases) contributes nine connected artifacts:

1. A conceptual model separating trust, trustworthiness, reliance, justified reliance, and calibration.
2. A six-variable autonomy profile covering goal scope, action authority, temporal horizon, impact radius, oversight distance, and reversibility.
3. A seven-level evidence ladder from assertion through longitudinal accountability.
4. A documentary test for practical human control across access, comprehension, authority, feasibility, exercise, effect, correction, repair, and reform.
5. A solo-validation suite containing 12 synthetic cases, 252 prespecified determinations, 12 mutation tests, three invariance tests, and sealed oracle artifacts.
6. A frozen public-case selection protocol with preserved candidate inputs, search output, exclusions, and selection decisions.
7. Three public evidence packets covering a successful pre-action intervention, formal authority without practical force, and an action sequence whose cause remains indeterminate.
8. A frozen research agenda focused on practical authority, evidence sufficiency, and interacting control conditions.
9. A publication figure set containing four main figures, two appendix figures, six derived data tables, formal captions, reading guides, and artifact-integrity checks.

All 252 determinations and 12 mutation tests pass under the committed contract. The v0.4.0 repository validator also checks source references, packet hashes, frozen selection invariants, three cross-case control interactions, exact figure data, and figure-artifact integrity. These results establish repeatable behavior and traceable bounded assessments for the included artifacts. They do not establish independent reliability, field validity, institutional effectiveness, or improved outcomes.

The v0.4.0 publication package derives from the committed v0.3.0 and v0.2.0 artifacts. Each image has a derived CSV, an SVG for paper production, a PNG preview, a formal caption, and an explicit interpretation boundary. The package changes no earlier case finding.

## Featured figure

Figure 2 compares whether assigned human authority became practical control in three historical cases.

[![Practical-control chain across three public cases](figures/generated/fig-2-practical-control-chain.png)](figures/generated/fig-2-practical-control-chain.svg)

### What the figure tells us

The featured figure asks a simple question: **Could the designated human actually change what the system did?**

All three cases gave a human formal authority. The outcomes differed because authority was only one link in a longer chain:

1. Did the person receive the relevant information?
2. Could they understand it?
3. Did they have authority to intervene?
4. Was intervention realistically possible in the available time?
5. Did they intervene?
6. Did the intervention change the outcome?

In the released v0.3.0 assessment, the 1983 Oko chain is classified as intact. Retrospective participant accounts report that Stanislav Petrov received the warning, questioned it, had time and authority to act, and prevented the warning from driving further escalation.

In the Patriot ZG710 case, a human authorized the engagement. The evidence indicates weak comprehension and no feasible or exercised challenge before launch. Formal authority therefore produced no protective effect.

In the F/A-18C case, the public record confirms human authority and some access to information. Missing records prevent conclusions about what operators saw, understood, or could have done in time. The purple cells mean “we do not know.” Orange cells record evidence that a condition failed.

The later reforms shown in both Patriot cases indicate institutional learning. They could not repair the losses already caused.

The central lesson is that placing a human “in the loop” does not establish meaningful control. Institutions need evidence that the entire chain works: timely information, comprehension, authority, opportunity, intervention, and effect.

The released figure derives this pattern from the [27 plotted states](figures/data/fig-2-practical-control-chain.csv). Authority is classified as supported in all three cases. A protective effect appears only in Oko, where the other five pre-action links are also classified as supported. The [figure methods](reports/figure-methods.md#derivation-of-the-central-lesson) preserve the formal derivation.

The paper-stage [PR #11 pressure test](paper/review-record-pr11.md) identified a protocol-consistency question. Oko's supporting records are retrospective, and the practical-control protocol defines a supported state through direct, contemporaneous evidence. Until a versioned resolution addresses that mismatch, read the green Oko cells as released assessment states, not as proof that the classifications satisfy every protocol requirement.

The figure shows this pattern across three historical cases. It supplies no estimate of how often these failures occur and no prediction of performance in current AI systems.

The [publication figure set](figures/) contains the remaining main figures, both appendix figures, their derived data, and plain-language reading guides.

## Repository map

| Path | Purpose |
| --- | --- |
| [`README.md`](README.md) | States the research question, current result, reading order, and validation commands. |
| [`RESEARCH_STATUS.md`](RESEARCH_STATUS.md) | Records the release state, completed artifacts, active work, and open empirical questions. |
| [`CLAIMS.md`](CLAIMS.md) | Lists each proposition with its evidence, confidence, limits, and reversal conditions. |
| [`LIMITATIONS.md`](LIMITATIONS.md) | Names validity threats and conclusions outside the current evidence. |
| [`SOURCES.md`](SOURCES.md) | Records the standards, papers, and public repositories used by the project. |
| [`CITATION.cff`](CITATION.cff) | Provides machine-readable authorship, release, license, and DOI metadata. |
| [`CHANGELOG.md`](CHANGELOG.md) | Tracks material changes to concepts, protocols, claims, and evidence requirements. |
| [`CONTRIBUTING.md`](CONTRIBUTING.md) and [`GOVERNANCE.md`](GOVERNANCE.md) | Define contribution evidence, review rules, decision authority, and change records. |
| [`research/`](research/) | Contains the main conceptual paper on justified reliance, autonomy, and practical control. |
| [`research/frozen-research-agenda.md`](research/frozen-research-agenda.md) | Freezes three research topics and one project question for the next public-case cycle. |
| [`paper/`](paper/) | Develops the methods paper, claim register, literature audit, review record, references, and publication decisions. |
| [`evidence/`](evidence/) | Contains the trust evidence register that converts reliance claims into inspectable records. |
| [`protocols/`](protocols/) | Defines solo validation, independent review, and practical-control assessment procedures. |
| [`protocols/public-case-reconstruction-protocol.md`](protocols/public-case-reconstruction-protocol.md) | Freezes the source cutoff, candidate pools, eligibility rules, screening order, and reconstruction procedure before case selection. |
| [`cases/`](cases/) | Publishes three case packets, their provenance manifests, assessments, hashes, and admissibility requirements. |
| [`cases/public-case-selection-register.md`](cases/public-case-selection-register.md) | Preserves the frozen collection hashes and every inclusion or exclusion in screening order. |
| [`cases/data/candidate-search-output.json`](cases/data/candidate-search-output.json) | Preserves the deterministic search result from the two candidate collections without redistributing article text. |
| [`schemas/`](schemas/) | Contains seven JSON Schemas defining synthetic and public-case assessment contracts. |
| [`fixtures/`](fixtures/) | Contains 12 synthetic cases and the controlled mutation suite. |
| [`oracles/`](oracles/) | Stores prespecified expected decisions and the SHA-256 manifest that seals them. |
| [`analysis/`](analysis/) | Implements the deterministic assessment logic and solo-validation runner. |
| [`assessments/`](assessments/) | Stores generated machine-readable assessment results. |
| [`reports/`](reports/) | Publishes the solo-validation and three-case reconstruction results with explicit claim boundaries. |
| [`figures/`](figures/) | Publishes four main figures, two appendix figures, their derived data, plotting specifications, and plain-language reading guides. |
| [`reports/figure-methods.md`](reports/figure-methods.md) | Records formal captions, transformations, missingness treatment, and prohibited interpretations for the figure set. |
| [`scripts/`](scripts/) | Contains candidate-search, packet-sealing, release-manifest, and repository-validation utilities. |
| [`release/`](release/) | Seals the v0.3.0 case artifacts and v0.4.0 publication package with SHA-256 digests. |
| [`mappings/`](mappings/) | Relates this work to GDI, HIT, CDFI, and CDCF governance artifacts. |
| [`.github/`](.github/) | Defines automated validation, the pull-request checklist, and structured issue forms. |
| [`requirements-dev.txt`](requirements-dev.txt) and [`LICENSE`](LICENSE) | Pin the validation dependency and state the Apache-2.0 license. |

## How to read the repository

Start with [Trust, Autonomy, and Evidence](research/trust-autonomy-and-evidence.md). Use the [Trust Evidence Register](evidence/trust-evidence-register.md) to translate a reliance claim into inspectable evidence. Read the [public-case report](reports/public-case-reconstruction-v0.3.0.md), [CLAIMS.md](CLAIMS.md), and [LIMITATIONS.md](LIMITATIONS.md) before applying the model.

The four protocols define solo validation, public-case reconstruction, practical-control assessment, and future independent evaluation. The public-case selection register must record its freeze commit before candidate screening begins. The mapping files show how this project relates to existing public artifacts without transferring claims among them.

## Repository validation

Install the pinned development dependency and run the validator with Python 3.10 or later:

```bash
python -m pip install -r requirements-dev.txt
python scripts/validate_repository.py
```

The repository validator checks required release files, internal Markdown links, version alignment, duplicate claim identifiers, exclusion of private candidacy language, JSON Schema conformance, source references, sealed packet and release hashes, selection invariants, three public-case interactions, 252 oracle comparisons, 12 mutation tests, and figure data and artifact integrity. The paper validator checks the manuscript workspace, author identity, question alignment, bibliography structure, version DOI, and open blocker record. Successful runs end with `repository validation: PASS` and `paper validation: PASS`.

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

Version 0.4.0 is released through GitHub and the repository's Zenodo integration. Its version-specific DOI is [10.5281/zenodo.21844706](https://doi.org/10.5281/zenodo.21844706).

> Banasihan, M. J. (2026). *Trust, Autonomy, and Evidence* (Version v0.4.0) [Computer software]. Zenodo.

The all-versions DOI, [10.5281/zenodo.21841127](https://doi.org/10.5281/zenodo.21841127), resolves to the newest archived version. Machine-readable metadata in [CITATION.cff](CITATION.cff) points to the exact v0.4.0 archive. The v0.3.0 case release remains available at [10.5281/zenodo.21843843](https://doi.org/10.5281/zenodo.21843843).

## Author

Mark Julius Banasihan is an independent applied researcher studying decision authority, human influence, evaluation, and assurance in AI-mediated institutional systems.

[GitHub](https://github.com/mj3b) | [ORCID](https://orcid.org/0009-0001-8121-2878)
