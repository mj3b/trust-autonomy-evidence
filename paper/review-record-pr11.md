# PR #11 Pressure-Test Record

**Review date:** 8 August 2026  
**Reviewed change:** [PR #11](https://github.com/mj3b/trust-autonomy-evidence/pull/11)  
**Merge commit:** [`a2a8db7a5a63fe09a2cdb48cb648c013c0d110ec`](https://github.com/mj3b/trust-autonomy-evidence/commit/a2a8db7a5a63fe09a2cdb48cb648c013c0d110ec)  
**Reviewer of record:** Mark Julius Banasihan, with AI-assisted consistency checking

## Decision

PR #11 established a useful paper workspace and left the frozen evidence artifacts unchanged. Its seven paper files support literature review and manuscript planning. Full empirical drafting remains gated by one unresolved protocol inconsistency.

The GitHub workflow for PR #11 completed successfully. That workflow checked repository artifacts and internal Markdown links. It did not require the paper package, validate BibTeX structure, compare the paper question across files, or test paper claims against protocol definitions.

## Findings

| ID | Severity | Observation | Consequence | Resolution state |
|---|---|---|---|---|
| PT-01 | High | The research question asked whether the procedure can distinguish three states. The selection protocol defined strata around those same contrasts before screening. | The cases demonstrate execution under contrastive conditions. They do not independently validate discriminative performance. | Resolved in the paper charter and manuscript question. |
| PT-02 | High | The practical-control protocol defines `supported` as direct, contemporaneous evidence. Oko's supported states rely on retrospective participant interviews, and the packet reports no located contemporaneous command log or official incident record. | The manuscript cannot describe the released Oko classifications as protocol-consistent on the present record. | Resolved in v0.6.0 through a prereassessment freeze, six reclassifications to partially supported, and a change ledger. |
| PT-03 | Medium | PR #11 described the source packets as immutable. Some relied-on source content is remote-only and has no repository hash. | Immutability applies to preserved files and versioned repository records, not to every underlying source page. | Resolved in paper wording. |
| PT-04 | Medium | PR #11 called the procedure reproducible. The repository has executable checks and one assessor. No independent reconstruction has reproduced the judgments. | The paper may claim traceability, executable checks, and repeatable artifact transformations. Independent reproducibility remains unresolved. | Resolved in paper wording. |
| PT-05 | Medium | The title used `AI-mediated decisions` without stating the functional definition that admitted Oko and Patriot. | A reader could infer architectural equivalence between historical knowledge-based systems and current learned models. | Resolved through an explicit system-inclusion and transfer boundary. |
| PT-06 | Medium | The initial matrix omitted close prior work on human accident reconstruction, public-report analysis of autonomous-system failure, human-control assurance, open-source AI-incident classification, AI-loss reconstruction, and prompt forensics. | The original novelty hypothesis was too broad. | Resolved provisionally through eight additions and a narrower novelty hypothesis. Database searches and citation chaining remain incomplete. |
| PT-07 | Medium | The repository validator did not require any paper file or validate paper metadata. | CI success could coexist with a deleted or internally inconsistent paper workspace. | Resolved through `scripts/validate_paper.py` and the CI workflow. |
| PT-08 | Medium | The repository instructed readers to cite the exact release. `CITATION.cff` contained the all-versions DOI. Zenodo assigns v0.4.0 the version DOI `10.5281/zenodo.21844706`. | A citation generated from the repository could point to the concept record, not the frozen v0.4.0 archive. | Resolved in `CITATION.cff`, the root README, and the manuscript availability section. |
| PT-09 | Low | Two BibTeX journal fields contained a doubled backslash before an ampersand. | Some BibTeX and LaTeX workflows could render or parse the journal names incorrectly. | Resolved. |
| PT-10 | Low | The paper README named the merged PR branch as the continuing working branch. | The workspace map became stale as soon as focused paper work moved to a new branch. | Resolved with a branch-neutral workflow statement and merge provenance. |

## Evidence behind the open blocker

The [practical-control protocol](../protocols/practical-human-control-test.md) requires direct, contemporaneous evidence for a `supported` state. The [Oko report](../cases/TAE-PUB-001-oko-1983/case-report.md) identifies its direct records as retrospective interviews. The [Oko source manifest](../cases/TAE-PUB-001-oko-1983/source-manifest.json) dates those interview sources to 1999 and 2017 and records the absence of contemporaneous Soviet command logs, an official incident record, and an investigation file.

The frozen v0.3.0 assessment remains unchanged. The paper will identify its classifications as released procedure outputs. A future versioned decision must either clarify the admissible meaning of contemporaneous evidence and justify that rule or reclassify the affected Oko stages under the existing definition.

## v0.6.0 resolution

The [adjudication protocol](../protocols/oko-evidence-adjudication-v0.6.0.md) froze the question, evidence universe, stage rules, and dependency rule before reassessment. The [v0.6.0 assessment](../assessments/v0.6.0/TAE-PUB-001-oko-1983.json) classifies all six practical-control stages from access through effect as partially supported. The [change ledger](../assessments/v0.6.0/oko-change-ledger.json) preserves each transition and the hashes of the frozen v0.3.0 inputs. `PAPER-BLOCKER-01` is resolved by reclassification. Missing contemporaneous evidence remains missing.

## Safe drafting boundary

Introduction, related work, method, results, discussion, and conclusion may proceed within the v0.6 claim boundary. The paper may report the current partial states and the version history. It may not claim that contemporaneous records were found, that the historical sequence is independently verified, or that the procedure has independent reliability.
