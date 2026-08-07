# Public Case Reconstruction Protocol

## Decision

Public records can test whether the assessment contract remains usable when the author does not control the underlying event, source coverage, or missing evidence. They cannot establish inter-rater reliability, operational effectiveness, or the truth of every source claim.

This protocol freezes the selection and reconstruction procedure before any candidate case is screened. Case screening may begin only after the commit that first adds this protocol and the empty selection register reaches the repository's `main` branch.

## Research question

Can the v0.2.0 autonomy profile, trust evidence register, and practical human control test produce traceable, bounded findings from public evidence created outside this project?

## Evidence cutoff

Eligible evidence must have been publicly available by **6 August 2026 at 23:59:59 UTC**. A later archive copy may preserve an eligible source. Information first published after the cutoff remains outside the frozen reconstruction packet and may be analyzed in a later protocol version.

## Unit of analysis

One case represents a bounded AI-mediated decision or action sequence. The boundary must identify:

- the AI system or agent;
- the actor that developed, deployed, or operated it;
- the task, recommendation, communication, or action in scope;
- the relevant period;
- the human or institutional authority, when publicly identifiable;
- the consequence or obligation that makes reliance material.

Several reports about the same action sequence form one case. A continuing deployment may produce separate cases when the decision authority, system version, action, or institutional response changes.

## Candidate sources

The candidate pool will be constructed from two public incident collections:

1. the first [AI Incident Database weekly snapshot](https://incidentdatabase.ai/research/snapshots) retrieved after this protocol reaches `main`, filtered to reports published by the evidence cutoff;
2. the [OECD AI Incidents and Hazards Monitor](https://oecd.ai/en/incidents) records available at screening, filtered to events and supporting reports published by the evidence cutoff.

The OECD monitor uses news aggregation and model-assisted classification and states that it does not independently verify every third-party report. The AI Incident Database accepts contributed reports and preserves changing incident records. These collections identify candidates. Their classifications do not count as proof of a Trust, Autonomy, and Evidence proposition.

The [GovAI incident analysis framework](https://www.governance.ai/research-paper/incident-analysis-for-ai-agents) supplies a source-search checklist covering system, contextual, cognitive, access, tool, log, and documentation evidence. It is not a candidate catalog.

## Fixed search vocabulary

Apply these case-insensitive terms to titles, summaries, and report text in each candidate collection:

`agent`, `autonomous`, `assistant`, `copilot`, `chatbot`, `tool use`, `computer use`, `browser`, `operator`, `automated decision`, `automated action`, `human review`, `human oversight`, `override`, `intervention`, `appeal`, `rollback`, and `incident response`.

Preserve the exported results, collection version or retrieval date, query implementation, and SHA-256 hash. Record query failures and inaccessible fields.

## Eligibility

A candidate is eligible when all of these conditions hold:

1. An identifiable AI system generated a recommendation, communication, plan, tool call, decision, or action that affected a person, institution, digital environment, or physical environment.
2. The case contains a bounded action sequence that can be separated from general product performance.
3. At least two public reports describe the sequence, and the reports are issued by different authors or organizations.
4. At least one report is a primary or official record, such as an operator statement, regulator or court record, public incident report, technical postmortem, repository issue, disclosed trace, or institutional decision record.
5. The available material permits citation and analysis without publishing personal, confidential, security-sensitive, or institutionally restricted information.
6. The event and the included evidence satisfy the frozen cutoff.

The incomplete-evidence stratum may admit a candidate supported by two independent secondary reports after a documented search finds no primary or official record. That absence becomes part of the finding.

## Exclusions

Exclude a candidate when:

- it is a benchmark result, hypothetical scenario, or controlled demonstration without an external action or decision;
- the available material identifies a general model failure and no bounded reliance decision;
- only one publisher or one unattributed account supports the sequence;
- the case requires private evidence to establish the basic event boundary;
- the material cannot be cited or preserved lawfully;
- it duplicates a candidate already entered in the register;
- its evidence first became public after the cutoff.

Every screened candidate remains in the selection register with an inclusion decision and reason code.

## Selection order

Deduplicate candidates by event, system, deployer, and period. Sort the resulting pool by event date, then collection identifier. Screen in that order until one eligible case fills each stratum:

1. **Pre-action intervention:** a public record reports that a named authority intervened before commitment and altered execution.
2. **Incomplete or conflicting evidence:** the reports omit a required part of the decision chain or materially disagree about it.
3. **Authority without practical force:** a public record reports formal review or intervention authority and evidence that timing, access, feasibility, or effect defeated it.

The provisional stratum controls selection only. The full assessment may produce any supported, partially supported, unsupported, indeterminate, or outside-scope finding.

Select the first eligible candidate in each stratum. Continue screening after a provisional selection only when source acquisition later shows that an eligibility condition failed. Preserve that failure in the register.

## Source packet

Create one immutable packet for each selected case. Each packet must contain:

- a case boundary and chronology;
- a source manifest with title, issuer, author when available, publication date, retrieval date, URL, archive URL when available, and source class;
- a SHA-256 hash for every preserved file;
- a record of unavailable, removed, paywalled, or inaccessible evidence;
- a provenance label for each material statement: `direct_record`, `source_claim`, `assessor_inference`, or `unresolved`;
- the system, context, access, tool, log, and documentation search record;
- a redaction and publication-rights statement.

Proprietary publications remain cited by metadata and a limited excerpt or paraphrase. The packet must not republish full copyrighted articles.

## Assessment procedure

1. Freeze the source packet and record its manifest hash.
2. Record the repository commit and assessment-contract version.
3. Classify the six autonomy variables with packet citations.
4. Evaluate the twelve trust propositions with packet citations.
5. Evaluate the nine practical-control stages with packet citations.
6. Treat missing evidence as indeterminate unless the case establishes that the record should exist and is absent.
7. Separate source claims from assessor inference.
8. State the narrowest assurance proposition supported by the packet.
9. State conclusions excluded by the evidence.
10. Generate a machine-readable assessment and a human-readable report from the frozen packet.

## Cross-case analysis

The cross-case report will compare where evidence becomes unavailable, contradictory, retrospective, or institutionally ineffective. It will report item-level findings. It will not aggregate the three cases into a general performance rate.

## Protocol deviations

A deviation must be recorded before the affected assessment continues. The record must identify the rule, reason, effect on selection or interpretation, and corrective action. A change to eligibility, search vocabulary, evidence cutoff, selection order, strata, or missing-data treatment requires a new protocol version. Results produced under the earlier version remain unchanged.

## Claim boundary

Completion of three cases can show that the published method produces traceable findings from a bounded public record. The design remains retrospective and single-assessor. It cannot estimate reviewer agreement, causal effects, deployment safety, institutional effectiveness, or outcome improvement.
