# Trust Evidence Register

## Decision rule

Every trust claim should identify the object of reliance, the action being permitted, the conditions under which reliance is justified, and the records an independent reviewer can inspect.

## Evidence grades

| Grade | Meaning | Examples |
|---|---|---|
| A | Independently verified in an operational setting across multiple cases | External field study, repeated audit, deployment outcomes, completed remediation |
| B | Independently assessed in a bounded study or adopted into an institutional process | Blinded scoring, external replication, accepted institutional governance artifact |
| C | Executable and reproducible within a published artifact | Tests, schemas, fixtures, validation scripts, integrity checks |
| D | Specified and traceable | Published method, definitions, claim register, mappings, version history |
| E | Asserted without inspectable support | Policy promises or impact claims without records |

The grade applies to a defined claim. A system, repository, institution, or researcher does not receive one permanent grade.

## Twelve evidence propositions

| Proposition | Minimum useful evidence | Stronger evidence | Failure signal |
|---|---|---|---|
| Identity is known | Agent, model, version, deployer, and owner identifiers | Cryptographic attribution and verified supply-chain records | Shared accounts or unidentified automated actors |
| Scope is bounded | Intended task, environment, and prohibited actions | Enforced permissions and sandbox tests | Broad tools with policy-only restrictions |
| Capability is measured | Results on relevant tasks | Human-calibrated, adversarial, repeated, and domain-specific evaluation | Benchmark selected after results are known |
| Reliability is characterized | Success and failure rates | Conditional failure distribution, confidence intervals, and drift monitoring | One aggregate score hides severe failure modes |
| Uncertainty is usable | Declared uncertainty or abstention behavior | Calibration evidence tied to decision thresholds | Fluent output is treated as calibrated confidence |
| Evidence is sufficiently complete | Source manifest and known gaps | Independent completeness review and inaccessible-source register | Missing data is silently treated as absence |
| Monitoring covers the pipeline | Fraction of actions observed | Stage-by-stage survival, false negatives, escalation rate, and detection delay | A flag rate is reported without downstream handling |
| Human authority has force | Named person with stop, reject, modify, or escalate power | Records of exercised intervention under realistic conditions | Review occurs after irreversible execution |
| Integrity is preserved | Timestamped logs and change history | Signed receipts, protected telemetry, and independent custody | Mutable logs remain under sole deployer control |
| Decisions are reconstructable | Question, evidence, alternatives, authority, outcome, and obligations | Independent reconstruction from contemporaneous records | Rationale is created after the outcome |
| Harm can be corrected | Appeal, rollback, and incident procedures | Measured recovery, completed remediation, and affected-person evidence | Correction exists only in policy text |
| Governance changes under evidence | Review cadence and update conditions | Documented control changes after failures and external findings | Repeated failures leave thresholds unchanged |

## How trust is earned

Evidence becomes more persuasive when producing it exposes the claimant to a meaningful possibility of failure.

| Trust mechanism | Observable behavior | Inspectable evidence |
|---|---|---|
| Competence | Another person can understand and run the method | Specifications, schemas, examples, installation results, clean-room implementation |
| Reliability | Results remain stable across declared conditions | Repeated cases, failure distributions, uncertainty intervals, boundary tests |
| Candor | Adverse findings and unresolved questions remain public | Negative-results register, publication blockers, retractions, corrections |
| Constraint acceptance | Failed gates limit action or claims | Records of delay, escalation, rejection, stopping, or reduced scope |
| Independence | People outside the claimant's control test the proposition | Preregistration, blinded review, external replication, qualified audit |
| Accountability | Decisions and repair obligations remain reconstructable | Named authority, contemporaneous records, appeals, remediation closure |
| Learning | Contradictory evidence changes the method | Issue-to-revision-to-retest history across releases |
| Institutional responsibility | A body can question, revise, or reject the proposal | Meeting records, reviewed contributions, decisions, dissent, accepted revisions |

External replication, disclosed failures, stopped actions, and completed repairs carry greater evidentiary weight because the claimant cannot fully control their result.

## Claims the register cannot support alone

The register does not establish that a system is safe, a decision is correct, a person understood the evidence, an institution will exercise authority, a recorded fact is true, or a governance requirement has been satisfied. Each conclusion requires evidence from the relevant decision and context.

