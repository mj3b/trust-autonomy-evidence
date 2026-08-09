# ScientistOne Artifact Pressure Test

## Decision for this paper

ScientistOne narrows the manuscript's contribution. Chain-of-Evidence, evidence-preserving research workflows, and post-hoc integrity auditing are established prior architecture. This paper may study their application to practical-human-control reconstruction and its added evidence-fitness and dependency-closure rules. It may not present claim traceability itself as an original contribution.

## Findings carried into v0.5

| Artifact finding | Repository response | Paper consequence |
|---|---|---|
| A result label can hide whether a value is one run, a selected result, or a mean. | Every numeric evidence item receives an explicit run type. | Describe the unit behind every reported value. |
| Failed or superseded work can affect the interpretation of a successful result. | Failed, excluded, and post-hoc evidence remain permitted evidence types. | Preserve negative method history when it bears on a claim. |
| A reference can resolve while its content fails to support the sentence. | Path resolution and human support review are separate gates. | Do not treat a valid citation as entailment. |
| A method description can differ from released code. | Method and implementation evidence are paired and tested. | State the implemented procedure, then identify deviations. |
| Artifact availability can exceed independent verifiability. | `remote_only`, `pending`, and verified integrity states remain distinct. | Limit reproducibility language to preserved artifacts and transformations. |
| The 75-paper integrity audit and six-task generalization evaluation have different scopes. | Audit unit and sample appear in each result. | Do not merge findings across units or denominators. |

## Examples requiring source-level caution

The public artifact repository supports closer review of Parameter Golf, unweighted SVD, AI4Code, unsupported multi-seed language, and Cloudcast verification. These examples motivate v0.5 controls. They are not findings about this repository and do not establish that ScientistOne generally succeeds or fails.

## Open verification

The paper and generated-artifacts repository were inspected as prior architecture and as a source of integrity-test examples. Full reproduction of the ScientistOne system and every reported task remains outside this project's scope.
