# Oko Evidence Adjudication, v0.6.0

## Decision

The frozen Oko packet partially supports each pre-action practical-control stage through effect. The v0.3.0 assessment classified those six stages as `supported`. The v0.6.0 adjudication changes each one to `partially_supported` because the source packet contains retrospective accounts and no contemporaneous decision record.

This decision resolves `PAPER-BLOCKER-01` through reclassification. It does not supply the missing historical evidence. The v0.3.0 assessment remains preserved as the original procedure output.

## Evidence rule

The [frozen adjudication protocol](../protocols/oko-evidence-adjudication-v0.6.0.md) applies the existing practical-control states without amendment. `Supported` requires direct, contemporaneous evidence satisfying the stage. `Partially supported` applies when the evidence satisfies at least one required element and a material gap remains.

Sources O2 and O4 contain Petrov's later first-person accounts. O3 independently reconstructs the event from later material. None is a contemporaneous 1983 command, interface, timing, decision, or escalation record.

## Stage decisions

| Stage | v0.3.0 | v0.6.0 | What the frozen sources describe | Material gap |
|---|---|---|---|---|
| Access | Supported | Partially supported | Alert receipt and checking of contextual and ground-radar information | No contemporaneous delivery, interface, or command record |
| Comprehension | Supported | Partially supported | Interpretation of the alert, its consequence, and discrepancies | No contemporaneous reasoning, review, or explanation record |
| Authority | Supported | Partially supported | Duty responsibility to classify and report the warning | No contemporaneous delegation or command-procedure record |
| Feasibility | Supported | Partially supported | A decision window and communication path that allowed a false-alarm report | No contemporaneous timing or operating record |
| Exercise | Supported | Partially supported | Challenge to the output and a false-alarm classification | No contemporaneous decision or communication log |
| Effect | Supported | Partially supported | The warning did not advance as a confirmed attack report | No contemporaneous linked action, stop, or escalation record |

The machine-readable [change ledger](../assessments/v0.6.0/oko-change-ledger.json) records the source references, missing element, state transition, frozen artifact hashes, and protocol freeze commit for every row.

## Dependency consequence

The practical-control test requires supported findings for access, authority, feasibility, exercise, and effect before a bounded practical-force conclusion becomes eligible. All five required stages are partially supported in v0.6.0. The paper may report that the retrospective sources describe the chain. It may not state that the packet establishes practical human control through effect under the current evidentiary rule.

## Preserved history

The following v0.3.0 artifacts remain unchanged:

- the Oko case report;
- the Oko source manifest;
- the Oko assessment;
- the Oko packet manifest;
- the public-case packet index;
- the frozen candidate search and selection register.

Version 0.6.0 adds a separate assessment. It does not rewrite the source packet or erase the earlier result.

## Claim boundary

The adjudication establishes internal consistency between the declared evidence rule and the current Oko states. One assessor made the decisions with disclosed AI assistance. The result supplies no new historical corroboration, independent agreement, population estimate, causal estimate, or transfer finding for current learned systems.
