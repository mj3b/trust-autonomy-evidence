# v0.16.0 Manuscript Rebuild Specification

## Decision served

Version 0.16.0 rebuilds the paper so that a first-time reader can answer four questions without consulting the repository:

1. Why can a named reviewer fail to provide practical human control?
2. What evidence would distinguish assigned authority from practical control?
3. Why does each part of the method exist?
4. What institutional error can occur when the evidence is absent?

The revision retains the research question, three released case assessments, formal-search counts, and current claim boundaries. It adds no prevalence, reliability, causal-effect, contemporary-system-transfer, legal-compliance, or institutional-outcome finding.

## Reader and voice rules

The manuscript uses `I` for author decisions, `this study` for the research contribution, `the procedure` for assessment behavior, `the evidence` for support states, and a named institutional actor for governance decisions. Ambiguous first-person plural language is excluded.

Each major method section follows one reasoning sequence:

> problem -> inference error -> control -> evidence requirement -> remaining limit

Plain-language explanation precedes notation. Repository identifiers, full mutation inventories, release mechanics, and hash detail remain in the supplement or repository.

## Terminology decisions

The six event-level stages are:

1. information access;
2. comprehension capacity;
3. intervention authority;
4. intervention feasibility;
5. exercised judgment; and
6. execution propagation.

`Execution propagation` is the manuscript term for the released assessment field named `effect`. The new term describes a linked change in execution. It does not assert a counterfactual causal effect or beneficial outcome.

Comprehension capacity is a required event-level stage in the v0.16 manuscript rule. It concerns observable evidence that the assigned person could interpret the output, limitations, uncertainty, and alternatives. It does not infer a private mental state.

## Formal rules

For case `c` and stage `j`, the state is:

\[
s_{c,j}\in\{S,P,U,I,O\}
\]

where `S` is supported, `P` partially supported, `U` unsupported, `I` indeterminate, and `O` outside scope.

Event-level practical control passes when every required stage is supported. It fails when any required stage is unsupported. It remains unresolved when no required stage is unsupported and at least one is partially supported or indeterminate.

The three nested propositions are:

\[
EventControl=Access\land Comprehension\land Authority\land Feasibility\land Exercise\land Propagation
\]

\[
AccountableControl=EventControl\land Correction\land Repair
\]

\[
LearningControl=AccountableControl\land Reform
\]

For a contemporary record with usable timestamps, intervention-time margin is:

\[
M_t=(t_{commit}-t_{access})-(t_{interpret}+t_{decide}+t_{transmit}+t_{propagate})
\]

The formula is a proposed measurement rule. The historical packets lack the complete timing inputs needed to calculate it.

A material claim is eligible for a conclusion only when traceability, integrity, human support review, evidence fitness, and every declared dependency pass.

## Required manuscript changes

- Replace the abstract with a reader-first statement of problem, method, result, contribution, and limits.
- Replace the internal blocker box with a research-language correction result.
- Explain the reason for every method control before describing its implementation.
- Add a construct-derivation table connecting each stage to prior work, observable evidence, and the error prevented.
- Add the categorical practical-control rule and nested institutional propositions.
- Add the proposed time-feasibility rule and identify its unavailable historical inputs.
- Compare formal authority with the full practical-control result in one table.
- Explain the institutional consequence of pass, fail, unresolved, and outside-scope results.
- State the bounded closest-work finding in plain language.
- Move release mechanics and detailed audit inventories out of the main argument.
- Preserve the case-selection, search-coverage, single-assessor, historical-transfer, and outcome limits.

## Evidence additions that remain open

The following work requires new evidence and therefore remains outside the v0.16 result:

- application to a contemporary learned or agentic system;
- independent second-assessor coding;
- intra-rater stability under an unchanged rule;
- comparison against a role-only baseline across a larger case set;
- component-removal testing on newly assessed cases;
- the remaining 980 retrieval outcomes;
- the 177-record backward-reference stratum;
- authenticated multidisciplinary and disciplinary database searches;
- prevalence, causal-effect, safety-effect, or institutional-outcome estimation.

## Rejection conditions

The rebuild fails when any of these conditions occurs:

- comprehension remains required in prose and optional in the formal event-control rule;
- execution propagation is described as a causal or beneficial outcome without eligible evidence;
- a missing record becomes evidence that a stage failed;
- a three-case count is presented as a population estimate;
- the closest-work statement extends beyond the reviewed source set;
- a formula introduces a score or ranking across categorical evidence states;
- a changed claim lacks an updated evidence map, support review, or dependency decision;
- the compiled PDF separates a formula, table, note, or caption from the section it explains.

