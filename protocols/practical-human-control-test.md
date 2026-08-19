# Practical Human Control Test

**Current manuscript interpretation:** v0.16.0

## Test proposition

> A claim of event-level practical human control is justified only when contemporaneous evidence shows that a named authority received relevant information before irreversible action, had the demonstrated capacity to understand and challenge it, held feasible intervention power, exercised judgment, and propagated a change into execution when necessary.

The test evaluates documentary support for this proposition in one defined decision. It does not infer private cognition or moral quality from records alone.

## Assessment states

Use one state for each stage:

- **Supported:** the packet contains direct, contemporaneous evidence satisfying the stage definition.
- **Partially supported:** some required elements are present and a material gap remains.
- **Unsupported:** available evidence contradicts the stage or shows the condition was absent.
- **Indeterminate:** the packet lacks enough evidence to decide.
- **Outside scope:** the stage does not apply under the declared case boundary, with a written reason.

Absence of evidence produces an indeterminate state unless the protocol or case design establishes that the missing record should exist.

## Six event-level stages and three post-event stages

The first six rows test whether human judgment could reach execution in the bounded event. The final three rows test what the institution could do after the event. Post-event correction, repair, or reform can show later learning, but it cannot convert failed or unresolved event-level control into a pass.

| Stage | Decision question | Minimum evidence | Stronger evidence | Failure indicator |
|---|---|---|---|---|
| Access | Did the authority receive relevant evidence before commitment or irreversible action? | Timestamped delivery or interface record | Verified access to underlying evidence and known gaps | Evidence arrives after execution |
| Comprehension capacity | Could the authority interpret output, limits, uncertainty, and alternatives? | Role-appropriate materials and evidence that the person could use them under the operating conditions | Independent explanation, challenge, or contemporaneous reasoning record | Approval without usable information about limitations or alternatives |
| Authority | Could the person approve, reject, modify, stop, or escalate? | Named delegation and control rights | Tested access and institutional protection for intervention | Advisory role presented as decision authority |
| Feasibility | Could authority be exercised within operational conditions? | Sufficient time, staffing, access, and response path | Realistic exercise or prior intervention record | Queue, latency, workload, or retaliation risk defeats authority |
| Exercise | Is there evidence of active judgment or intervention? | Contemporaneous decision or review record | Departure from recommendation, challenge, or escalation | Automatic approval or retrospective rationale |
| Execution propagation | Did intervention alter execution or obligations? | Linked action, stop, modification, or escalation event | Verified downstream propagation and enforcement | Decision record changes while execution continues unchanged |
| Correction | Can the decision be contested and revised? | Defined appeal or reassessment path | Completed case with measured response time | Appeal exists without access, authority, or remedy |
| Repair | Can a named actor remediate qualifying harm? | Assigned obligation and available remedy | Completed remediation and affected-person evidence | No owner, resources, deadline, or closure record |
| Reform | Can case evidence change the decision architecture? | Review trigger and change authority | Versioned control revision linked to the case | Repeated failure leaves controls unchanged |

## Decision rule

Report each stage separately. Do not collapse the result into a single score unless a later validated protocol defines and justifies that aggregation.

A bounded claim that a human intervention had event-level practical force requires supported findings for access, comprehension capacity, authority, feasibility, exercise, and execution propagation. An unsupported required stage makes the event-control proposition fail. When no required stage is unsupported, a partially supported or indeterminate required stage leaves the event-control proposition unresolved. `Outside scope` cannot remove a conceptually required event-level stage.

Claims extending to institutional accountability also require supported correction and repair findings. A claim of institutional learning additionally requires supported reform evidence across time.

The released machine-readable assessments through v0.15 use the field name `effect`. Version 0.16 interprets that field as execution propagation. This terminology change does not convert a linked execution record into a counterfactual causal-effect or beneficial-outcome finding.

## Formal representation

For case (c) and stage (j):

\[
s_{c,j}\in\{S,P,U,I,O\}
\]

where the symbols correspond to supported, partially supported, unsupported, indeterminate, and outside scope.

For the required event-stage set (R):

\[
EventControl(c)=
\begin{cases}
FAIL, & \exists j\in R:s_{c,j}=U\\
UNRESOLVED, & \nexists j\in R:s_{c,j}=U\;\land\;\exists j\in R:s_{c,j}\in\{P,I\}\\
PASS, & \forall j\in R:s_{c,j}=S
\end{cases}
\]

The formula exposes the categorical decision rule. It assigns no numerical distance among states and supplies no aggregate control score.

## Proposed timing measure for contemporary records

When a packet contains complete timestamps, the intervention-time margin is:

\[
M_t=(t_{commit}-t_{access})-(t_{interpret}+t_{decide}+t_{transmit}+t_{propagate})
\]

Feasibility requires a nonnegative margin and a functioning intervention channel. Missing timing inputs leave the timing proposition indeterminate. The three released historical packets do not contain the complete inputs needed to calculate this measure.

## Required output

The assessor should publish:

- case and decision boundary;
- repository commit and protocol version;
- evidence citations for every classification;
- missing and inaccessible evidence;
- each stage result;
- reviewer uncertainty and disagreements;
- supported bounded proposition;
- conclusions excluded by the evidence.
