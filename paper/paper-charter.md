# Paper Charter

## Decision problem

Institutions often treat a named human reviewer, approval step, or override power as evidence that a system remains under human control. That inference is not justified when the person lacks timely information, comprehension, authority, a feasible opportunity to challenge the system, or the ability to affect the outcome.

The paper must help an institutional decision-maker decide what evidence is required before a claim of human control deserves reliance.

## Research question

> How can a frozen, evidence-traceable assessment procedure represent formal human authority, practical human control, and unresolved evidence in a bounded public incident record?

### Subquestions

1. Which links in the pre-action control chain are supported, unsupported, or indeterminate in each packet?
2. Does formal authority coincide with evidence of feasible challenge, exercised challenge, and effect?
3. What records are needed to reconstruct those propositions without converting missing evidence into a factual failure?
4. Which conclusions remain outside the design because the cases are retrospective, purposefully selected, and single-assessor?

## Paper type

A methods demonstration with a comparative reconstruction of three purposefully selected public cases.

It is not a prevalence study, causal evaluation, system ranking, legal-responsibility analysis, or independent-reliability study.

## Proposed contribution

The paper contributes a documented and executable procedure for testing whether a human-control claim has evidentiary support in a bounded decision record. The procedure combines:

1. a declared decision boundary;
2. a protocol frozen before candidate screening;
3. a preserved selection and stopping path;
4. claim-level provenance;
5. categorical supported, partially supported, unsupported, indeterminate, and outside-scope states;
6. a practical-control chain connecting access, comprehension, authority, feasibility, exercise, and effect;
7. machine-readable assessments, packet hashes, and executable consistency checks.

## Provisional central claim

The current assessment set applies v0.6.0 to Oko and preserves the v0.3.0 Patriot assessments. Oko records partial support across access, comprehension, authority, feasible challenge, exercised challenge, and effect. ZG710 records supported authority with several practical-control conditions unsupported. F/A-18C records supported authority with several conditions indeterminate because public records are missing.

These states demonstrate how the procedure represents three contrastive evidence conditions. The selection strata anticipated those contrasts, so the cases do not independently establish discriminative validity.

The v0.6 adjudication resolves the Oko protocol mismatch through reclassification under the existing direct-and-contemporaneous rule. The adjudication protocol was frozen before the reassessment, the evidence universe remained fixed, and each transition is recorded in a machine-readable ledger. The decision preserves v0.3.0 and leaves the missing contemporaneous record visible.

## Novelty hypothesis

A targeted search identified prior work on meaningful human control, human-automation performance, retrospective reconstruction, public AI-incident analysis, assurance cases, AI-loss reconstruction, prompt forensics, Chain-of-Evidence, and post-hoc research-integrity audit. Broad claims to originality in any one of these areas are rejected.

The narrower novelty hypothesis concerns a governance-specific combination: a protocol fixed before screening, a preserved selection path, versioned public evidence packets, explicit indeterminate states, a declared chain from access through effect, claim-specific evidence fitness, dependency closure, and executable checks over the published artifacts.

This is a provisional hypothesis. The paper must not claim novelty until backward citation review, forward citation review, and a documented database search are complete.

## Evidence base

The manuscript derives its case findings from:

- the [public-case reconstruction protocol](../protocols/public-case-reconstruction-protocol.md);
- the [selection register](../cases/public-case-selection-register.md);
- three versioned [public-case packets](../cases/), with hashes for preserved files and source metadata for remote-only materials;
- the [cross-case report](../reports/public-case-reconstruction-v0.3.0.md);
- the [figure methods and captions](../reports/figure-methods.md);
- the released machine-readable assessments, manifests, and repository checks.

## Intended readers

- AI governance and policy researchers;
- assurance and audit practitioners;
- safety and human-factors researchers;
- institutional decision-makers responsible for consequential AI-supported decisions;
- developers and deployers responsible for preserving review and incident records.

## Claim boundary

The paper may claim that the published method produced traceable, bounded assessment states for the three packets.

It may not claim:

- population frequency, prevalence, or effect size;
- causal effectiveness of human intervention;
- independent reviewer agreement;
- general safety or reliability of Oko or Patriot;
- equivalence between historical systems and current learned systems;
- legal responsibility, compliance, or moral culpability;
- improved institutional outcomes;
- independent validation of the method's ability to discriminate among case types;
- immutable preservation of source content that remains remote-only;
- contemporaneous historical support for Oko beyond the evidence in the frozen packet.

## Completion gates

A manuscript is ready for public preprint review only when:

1. every material empirical claim appears in the claim-evidence register;
2. every bibliographic entry has been checked against a publisher, DOI record, or institutional repository;
3. the literature search and citation-chaining procedure are documented;
4. the Oko decision and each assessment transition remain traceable to the frozen v0.6 adjudication;
5. all nine figures rebuild and both repository validators pass;
6. the version-specific data and code archive is cited;
7. the single-assessor design and AI-assisted workflow are disclosed;
8. the abstract, results, and conclusion use the same claim boundary.

## Authorship and assistance

Mark Julius Banasihan is the accountable human author for this working paper. Final author name, affiliation, and acknowledgments must be confirmed before submission. AI tools may assist with search, organization, drafting, formatting, and consistency checks. They are not authors and cannot accept responsibility for the paper's claims. The manuscript will disclose material AI assistance according to the selected venue's rules.

## Change rule

This working charter includes its v0.1 foundation and each later material decision. A change to the research question, unit of analysis, case set, assessment states, or claim boundary must be recorded in branch history before the affected drafting continues.

## Decision history

On 8 August 2026, the PR #11 pressure test changed the question from whether the method can distinguish the three states to how the method represents them. The contrastive selection strata anticipate the headline differences, which prevents the three selected cases from serving as an independent test of discriminative validity. The case set, unit of analysis, released assessment states, and frozen packets remain unchanged.

On 9 August 2026, the v0.6 adjudication resolved `PAPER-BLOCKER-01` by applying the existing evidence rule to the frozen Oko packet. Six practical-control stages changed from supported to partially supported in a new assessment. The v0.3.0 record remains unchanged. A sentence-level support audit closed the current literature-support exception; systematic novelty searching remains open.
