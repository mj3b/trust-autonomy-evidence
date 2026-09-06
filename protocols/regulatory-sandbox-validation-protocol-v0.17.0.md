# Prospective Regulatory Sandbox Validation Protocol

**Version:** 0.17.0 draft
**Decision owner:** Mark Julius Banasihan
**Status:** Protocol candidate; freeze commit and sandbox partner remain open

## Research problem

The historical cases show what can and cannot be reconstructed from surviving public records. They cannot establish whether the six-stage method works when evidence is collected before and during a contemporary automated decision. A prospective sandbox study addresses that limit by fixing the assessment rule before the observed outcomes and capturing the intervention path as it occurs.

## Research question

> Can a preregistered six-stage evidence protocol distinguish assigned oversight from practical human control in a contemporary automated decision while preserving missing evidence, timing, intervention, and execution records?

## Pre-study freeze

Before any study run, freeze and hash:

1. the system and decision boundary;
2. the oversight role and intervention rights;
3. the six required event-level stages;
4. the five evidence states and case-level decision rule;
5. the timing-margin definitions;
6. the data-retention and redaction rules;
7. the planned conditions and stopping rule;
8. the analysis code and expected output schema.

The freeze prevents the researcher from changing the decision rule after observing which condition passes or fails.

## Six required stages

The protocol uses the current practical-control construct without renaming or reordering its required fields:

1. information access;
2. comprehension capacity;
3. intervention authority;
4. intervention feasibility;
5. exercised judgment;
6. execution propagation.

Each stage receives one state: supported, partially supported, unsupported, indeterminate, or outside scope. Outside scope cannot remove a conceptually required event-level stage.

## Minimum evidence capture

| Stage | Required record | Prospective test |
|---|---|---|
| Information access | Timestamped interface state and delivered evidence | Verify what the overseer could see before irreversible commitment |
| Comprehension capacity | Training basis, limitation disclosure, and task-specific comprehension check | Test whether the overseer can interpret output, uncertainty, and alternatives under study conditions |
| Intervention authority | Role delegation and tested controls | Verify that approve, reject, modify, stop, and escalation rights work before the study |
| Intervention feasibility | Workload, latency, staffing, and complete timing inputs | Calculate the proposed timing margin and record channel failures |
| Exercised judgment | Contemporaneous decision, challenge, or intervention record | Distinguish active judgment from automatic confirmation |
| Execution propagation | Linked downstream state or action record | Verify that the intervention changed execution or a binding obligation |

## Study conditions

The first application should contain at least three prespecified conditions:

1. a control path with sufficient information, time, and functioning intervention rights;
2. a degraded path with one known constraint, such as compressed time or incomplete system-limit information;
3. a missing-record path used to confirm that the method returns unresolved instead of converting absence into failure.

These conditions test the procedure's response to known differences. They do not estimate real-world prevalence.

## Timing measure

For each run with complete timestamps:

\[
M_t=(t_{commit}-t_{access})-(t_{interpret}+t_{decide}+t_{transmit}+t_{propagate}).
\]

A nonnegative margin is necessary for feasibility under this proposed measure. A functioning intervention channel is also required. Missing inputs produce an indeterminate timing result.

Here, $t_{commit}$ and $t_{access}$ are event timestamps. The terms $t_{interpret}$, $t_{decide}$, $t_{transmit}$, and $t_{propagate}$ are elapsed durations under the notation inherited from v0.16.0. The data dictionary must identify each field as a timestamp or duration and express every value in a common unit. A later manuscript revision may rename the duration terms with a $d$ prefix for dimensional clarity without changing the arithmetic.

## Assessment and independence

The accountable author may perform the first protocol rehearsal and artifact check. That solo run can show whether the study package is executable and internally consistent. It cannot establish inter-rater reliability or independent validity.

The first reliability study should use a blinded second assessor who receives the frozen protocol, redacted evidence packet, and classification form without the author's case labels. Disagreement should remain visible at the stage level. Any consensus state must preserve both original decisions and the adjudication rationale.

## Validation ladder

The evidence claim should expand only after the corresponding study phase is complete:

1. **Controlled conformance and executability:** apply the procedure to prespecified conditions with known differences. This tests whether the procedure returns the expected state and whether the artifact pipeline runs. It does not establish construct validity.
2. **Reliability:** use a blinded second assessor and preserve both initial classifications. Freeze the sample, missing-data treatment, adjudication rule, and an appropriate stage-level reliability statistic before labeled outcomes are visible.
3. **Construct and criterion validity:** sample from the intended systems, tasks, and operating conditions. Compare the six-stage results with preregistered hypotheses and an external criterion that was not produced from the same stage labels.
4. **Institutional outcomes:** examine whether measured practical control is associated with correction, harm prevention, accountability, or other defined outcomes. Report associations unless the study design supports a causal effect.

This sequence prevents a successful software rehearsal or a high assessor-agreement score from being presented as evidence that the construct predicts meaningful institutional outcomes.

## Ethics, privacy, and study authority

Before participant recruitment or operational-data collection, record the applicable research-ethics or institutional-review determination, sandbox authority, lawful processing and publication authority, consent or waiver basis, and the data minimization, redaction, security, retention, and deletion plan. A solo synthetic rehearsal requires a recorded determination that it uses no participant data or protected operational records.

Stop the study if the required authority, ethics determination, consent basis, or data protections are absent. The protocol and empty schemas may remain public while restricted evidence stays withheld under a declared access rule.

## Required outputs

Publish, subject to sandbox, privacy, security, and legal restrictions:

- preregistration and protocol hash;
- system and decision boundary;
- redacted evidence packet and source manifest;
- stage-level assessment ledger;
- timing inputs and calculation state;
- case-level pass, fail, or unresolved result;
- assessor disagreement and adjudication record;
- claim-evidence map and evidence-fitness decisions;
- integrity-audit result and controlled-mutation response;
- missing, withheld, deleted, and inaccessible records;
- correction ledger and version manifest.
- ethics or institutional-review determination and data-authority record, or a documented determination that each is inapplicable.

## Rejection and stopping rules

Stop the run and withhold a case-level conclusion when the decision boundary changes, required logs cannot be lawfully preserved, the required ethics or data authority is absent, the intervention controls fail before the planned task, or the protocol is changed after outcome visibility. Record the stopped run and its reason. Do not replace it silently.

## Interpretation boundary

A successful protocol rehearsal establishes internal executability. A prospective case result remains specific to its system, task, people, interface, timing, and organizational setting. Claims about legal compliance, safety, fairness, improved outcomes, reliability, and general transfer require separate evidence.
