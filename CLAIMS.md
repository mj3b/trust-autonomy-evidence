# Claims Register

This register separates demonstrated repository properties from research propositions.

| ID | Claim | Present evidence | Status | Update condition |
|---|---|---|---|---|
| TAE-C01 | The repository defines five separate concepts: trust, trustworthiness, reliance, justified reliance, and calibration | Published definitions in the research brief | Demonstrated as an artifact property | A release removes or merges a definition |
| TAE-C02 | The repository defines autonomy using six variables | Published autonomy profile | Demonstrated as an artifact property | A release changes the profile |
| TAE-C03 | The evidence ladder contains seven levels with declared examples and boundaries | Published evidence ladder | Demonstrated as an artifact property | A release changes the ladder |
| TAE-C04 | The trust evidence register contains twelve propositions | Published register | Demonstrated as an artifact property | A release changes the register |
| TAE-C05 | The practical human control test contains nine documentary stages | Published protocol | Demonstrated as an artifact property | A release changes the protocol |
| TAE-C06 | Independent reviewers can apply the autonomy profile consistently | No eligible study | Unresolved | Prespecified multi-reviewer evidence satisfies the review protocol |
| TAE-C07 | Independent reviewers can apply the practical human control test consistently | No eligible study for this repository version | Unresolved | Prespecified multi-case evidence satisfies the review protocol |
| TAE-C08 | The model identifies material omissions in real decision evidence | No prospective case series | Unresolved | Predefined case evaluation records omission detection and reviewer agreement |
| TAE-C09 | Failed evidence conditions alter institutional action | No prospective intervention study | Unresolved | Contemporaneous records show a failed condition caused delay, escalation, rejection, or stopping |
| TAE-C10 | Use of the architecture improves safety, accountability, decision quality, or harm repair | No comparative outcome evidence | Unresolved | A suitable comparative design supports a bounded outcome claim |
| TAE-C11 | The architecture satisfies any legal, regulatory, certification, or normative requirement | No qualified determination | Outside current claim scope | A qualified authority assesses a defined version in a defined context |
| TAE-C12 | All 12 v0.2.0 synthetic cases conform to the published input schemas | Executable schema validation in the solo-validation suite | Demonstrated for committed fixtures | A fixture or schema change fails validation |
| TAE-C13 | The v0.2.0 assessment contract reproduces all 252 prespecified oracle determinations | Generated results and executable oracle comparison | Demonstrated for committed fixtures | Any assessment differs from the sealed oracle |
| TAE-C14 | All 12 v0.2.0 mutation tests produce exactly their prespecified classification deltas | Executable before-and-after comparison | Demonstrated for committed mutations | Any additional, missing, or incorrect delta occurs |
| TAE-C15 | Case title, reported outcome, and impact-radius mutations leave trust and practical-control assessments invariant under the current contract | Three executable invariance tests | Demonstrated for included mutations | Any assessment changes under an invariant mutation |
| TAE-C16 | The v0.2.0 suite establishes independent reliability or operational effectiveness | Author-designed rules, fixtures, and oracle only | Unsupported | Eligible independent or operational evidence satisfies a prespecified protocol |

## Interpretation rule

Artifact-property claims establish what the repository contains and how included procedures behave. Empirical claims require observations outside the author's construction of the artifact. Operational and outcome claims require evidence from the relevant institution and deployment context.
