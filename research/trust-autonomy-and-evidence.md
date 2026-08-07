# Trust, Autonomy, and Evidence

## Research question

An institution that says it trusts an AI system has left the evaluative claim incomplete. The claim must specify what or whom the institution relies on, which action the reliance permits, the conditions governing that permission, the consequences of failure, and the evidence available for review.

This project uses the following question:

> **What evidence justifies reliance on an autonomous AI system, and what evidence shows that institutional authority can still detect, interrupt, correct, and repair its actions?**

## Four objects of reliance

| Object | Reliance claim | Evidence required | Category error |
|---|---|---|---|
| AI agent | The agent can perform a defined task within specified conditions | Capability, reliability, failure distribution, security, and calibration evidence | Treating average benchmark performance as permission to act in every case |
| Oversight process | The control process can detect and stop unacceptable actions | Coverage, detection, escalation, intervention, and response-time evidence | Treating the presence of a monitor or reviewer as proof that the pipeline works |
| Institution | The organization will govern the system consistently and repair harm | Named authority, incentives, decision records, incident response, appeal, and remediation evidence | Treating policy publication as evidence of practice |
| Assessor | The assessor's conclusions are competent, candid, and reproducible | Traceable methods, disclosed failures, independent checking, correction history, and bounded claims | Treating credentials or publication as proof that a claim is valid |

The objects interact without becoming interchangeable. A capable agent can operate inside a weak institution. An effective oversight process can constrain a bounded class of agent failures. A qualified assessor may conclude that the evidence supports no deployment decision.

## Trustworthiness, trust, and justified reliance

- **Trustworthiness** refers to properties that make reliance defensible. NIST includes validity and reliability, safety, security and resilience, accountability and transparency, explainability and interpretability, privacy, and fairness with harmful bias managed.
- **Trust** is a person's willingness to accept vulnerability based on expectations about another actor or system.
- **Reliance** is observable behavior, such as delegating a task, accepting a recommendation, allowing an action, or reducing supervision.
- **Justified reliance** exists when the reliance decision matches the evidence, stakes, context, and demonstrated limits.
- **Calibration** is the relationship between believed trustworthiness and demonstrated trustworthiness. Excessive belief can produce misuse; insufficient belief can produce disuse.

Lee and See's 2004 review frames appropriate reliance as the design objective because people must decide whether to depend on automation without complete understanding. NIST adds a governance condition: validity and reliability form a base, while context determines which additional characteristics and thresholds matter.

## Autonomy profile

Autonomy has multiple dimensions. A system may have wide permissions and short tasks, narrow permissions and long tasks, or high impact with frequent review. A governance assessment should record at least six variables.

| Variable | Question | Evidence |
|---|---|---|
| Goal scope | How broadly can the agent interpret or revise its objective? | System instructions, planning rules, permitted subgoals, and evaluation tasks |
| Action authority | Which tools, accounts, data, environments, or funds can it use? | Permission manifests, identity records, capability tokens, and access logs |
| Temporal horizon | How difficult a task can it complete without assistance? | Human-calibrated task evaluations, success curves, retries, and uncertainty intervals |
| Impact radius | How many people, systems, or irreversible commitments can one action affect? | Dependency maps, transaction limits, propagation records, and blast-radius analysis |
| Oversight distance | How much can occur before review or intervention? | Review frequency, monitor coverage, detection delay, queue behavior, and stop latency |
| Reversibility | Can an authorized person undo the action and repair its effects? | Rollback tests, appeal procedures, compensation records, and recovery time |

METR's time horizon measures task difficulty using the time a skilled human needs for the task. It does not measure the agent's wall-clock operating duration and does not cover every form of intellectual work. GovAI's code-inspection work adds impact and oversight attributes. These limitations make a single autonomy score insufficient for selecting a governance response.

## Trust evidence ladder

Evidence can be ranked by how directly it supports a defined reliance claim.

### Level 0: Assertion

Mission statements, policy promises, self-descriptions, model confidence, and vendor claims identify propositions that require testing.

### Level 1: Design evidence

Specifications, schemas, permission models, review procedures, safety cases, and escalation rules establish intended behavior.

### Level 2: Executable evidence

Schema validation, deterministic tests, access-control tests, rollback tests, tamper detection, and monitor-pipeline tests establish behavior for included conditions and fixtures.

### Level 3: Empirical evaluation

Representative task results, adversarial testing, calibration curves, failure distributions, subgroup analysis, monitor recall, and intervention latency estimate performance under declared test conditions.

### Level 4: Independent evaluation

External replication, third-party audit, blinded scoring, red-team assessment, and secure access to non-public records reduce the author's control over evidence selection and interpretation.

### Level 5: Operational evidence

Production logs, sampled decision records, incident rates, override outcomes, false-negative investigations, drift measures, appeals, and repairs show performance within an institution and use context.

### Level 6: Longitudinal accountability

Repeated audits, disclosed failures, corrective-action closure, policy revisions after incidents, performance across system updates, and evidence that leaders accepted costly constraints show whether behavior persists as systems and incentives change.

Higher levels add support to a claim. They do not cure weaknesses at lower levels. Operational success without reconstructable design may resist audit. Sound design without field evidence leaves effectiveness unresolved.

## Practical human control

Practical control is a chain. Evidence from one stage cannot establish the entire chain.

1. **Access:** The human received relevant evidence before the decision or irreversible action.
2. **Comprehension:** The human could interpret the output, limitations, uncertainty, and alternatives.
3. **Authority:** The person held explicit power to approve, reject, modify, stop, or escalate.
4. **Feasibility:** Time, staffing, information, and institutional protection made exercise possible.
5. **Exercise:** Contemporaneous records show intervention, independent reasoning, or departure from the system recommendation.
6. **Effect:** The intervention altered execution or downstream obligations.
7. **Correction:** Affected people or authorized actors could contest and revise the decision.
8. **Repair:** A named actor could remediate qualifying harm.
9. **Reform:** Evidence from the case could change the decision architecture.

Article 14 of the EU AI Act connects oversight measures to risk, autonomy, and context. Assigned persons must have competence, training, and authority; understand system limits and automation bias; interpret outputs; and disregard, override, reverse, or interrupt output where appropriate. These requirements supply a legal reference point. Evidence from a particular deployment remains necessary to assess whether oversight had practical force.

## Minimum evidence package for one autonomous decision

An independent assessor should receive a bounded package containing:

- system, model, version, owner, deployer, and agent identity;
- task, goal, environment, tool, permission, and prohibited-action scope;
- relevant capability evaluation and known failure distribution;
- decision question, available evidence, uncertainty, and alternatives;
- named authority and delegation basis;
- event and action logs with timestamps and integrity information;
- monitor coverage, alert path, review outcome, and detection delay;
- intervention, override, stop, or escalation record;
- final action and downstream propagation;
- appeal, correction, repair, and reassessment records;
- declared missing evidence and inaccessible sources;
- independent reviewer findings and disagreement record.

This package may support a bounded assurance proposition:

> The available contemporaneous records show that a named human authority received the relevant alert before irreversible execution, reviewed the underlying evidence, exercised stop authority, and caused the action to be withheld.

The proposition does not establish general system safety, sound human reasoning, truthful source evidence, or equivalent control in another context.

## Research contribution

The proposed contribution is an evidence architecture for calibrated reliance under increasing autonomy. Its credibility depends on independent application, operational cases, negative findings, and visible revision when evidence contradicts the model.

