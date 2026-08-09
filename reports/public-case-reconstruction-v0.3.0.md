# Public-Case Reconstruction Report, v0.3.0

## Result

Three cases selected under a frozen protocol produce three distinct conclusions about human control and evidence sufficiency.

1. In the 1983 Oko warning incident, a named duty officer received an alert before escalation, challenged it using contextual and ground-radar evidence, reported a false alarm, and affected the decision path.
2. In the 2003 Patriot engagement of RAF Tornado ZG710, operators held formal launch authority. A compressed decision window, incomplete information, system-centered training, and the division of work between people and automation prevented that authority from functioning as an effective challenge.
3. In the 2003 Patriot engagement of a U.S. Navy F/A-18C, public evidence establishes the main action sequence and resulting loss. Missing inquiry records, logs, displays, and technical details prevent a finding about the misclassification mechanism or feasible intervention options.

These findings support the repository's central distinction: assigned human authority and practical human control are separate propositions. They also show why an assessment needs an explicit indeterminate state. Missing records can prevent a conclusion even when the outcome is known.

## Method

The [public-case protocol](../protocols/public-case-reconstruction-protocol.md) fixed the evidence cutoff, two candidate collections, search vocabulary, screening order, eligibility rules, selection strata, and source-packet contract before candidate screening. The freeze is recorded in the [selection register](../cases/public-case-selection-register.md).

The AI Incident Database snapshot contained 1,607 incidents and 7,452 reports. Whole-token and whole-phrase matching produced 828 candidates. The OECD query produced about 3,635 matches, while the interface exported 100 visible rows. Date-range probes found no OECD result before 2020. The three strata were filled by AI Incident Database events dated 1983 and 2003, so the OECD export limit did not affect selection.

Screening stopped after five candidates:

| Order | Candidate | Decision |
|---:|---|---|
| 1 | AIID-27 | Selected for pre-action intervention |
| 2 | AIID-42 | Excluded because the matching term appeared only in an administrative record |
| 3 | AIID-79 | Excluded because the matching term appeared in a job title and no bounded action sequence was present |
| 4 | AIID-444 | Selected for authority without practical force |
| 5 | AIID-445 | Selected for incomplete or conflicting evidence |

Each packet contains a narrative report, source manifest, machine-readable assessment, and SHA-256 packet manifest.

## Cross-case comparison

| Mechanism | Oko | Tornado ZG710 | F/A-18C |
|---|---|---|---|
| Access before action | Supported | Partially supported | Partially supported |
| Comprehension | Supported | Unsupported | Indeterminate |
| Formal authority | Supported | Supported | Supported |
| Feasible challenge | Supported | Unsupported | Indeterminate |
| Exercised challenge | Supported | Unsupported | Indeterminate |
| Protective effect | Supported | Unsupported | Unsupported |
| Evidence completeness | Unsupported | Partially supported | Unsupported |
| Reconstructability | Partially supported | Partially supported | Partially supported |

### Practical force

The Oko case contains public evidence for each pre-action control link through effect. Its limits concern source completeness and counterfactual claims about later decision-makers.

The Tornado case shows why authority alone is insufficient. A crew can possess formal discretion while lacking the time, context, independent evidence, and preparation needed to use it. The failed interaction, rather than the presence of one missing control, explains the practical-control result.

The F/A-18C case supports a weaker conclusion. A human order is reported and the engagement occurred, yet public evidence cannot resolve comprehension, feasibility, or exercised challenge. Assigning a precise causal failure would exceed the record.

### Evidence sufficiency

The packets distinguish four provenance states:

- `direct_record` for an official record or a source containing a participant's direct account;
- `source_claim` for a proposition reported by an eligible source;
- `assessor_inference` for a classification derived from cited evidence;
- `unresolved` when eligible public evidence does not justify a determination.

This distinction prevents source authority from transferring automatically to every assessment claim. It also prevents a documented outcome from becoming evidence for a complete causal explanation.

## Interaction test

The three packets exercise a conjunctive practical-control rule:

- TAE-PUB-001 supports access, authority, feasibility, exercise, and effect.
- TAE-PUB-002 supports formal authority while feasibility, exercise, and effect are unsupported.
- TAE-PUB-003 supports formal authority while feasibility and exercise remain indeterminate and effect is unsupported.

Repository validation checks these relations. A later edit that turns formal authority into a sufficient control finding, or converts missing evidence into a negative factual claim, will fail the interaction check.

## Claim boundary

The result establishes that the published procedure selects cases deterministically from the preserved search output and produces traceable, bounded assessments for those cases. It does not establish:

- inter-rater reliability;
- population frequency or effect size;
- causal effectiveness of the evidence architecture;
- the general safety or reliability of Oko or Patriot;
- equivalence between historical knowledge-based systems and current learned systems;
- legal responsibility, compliance, or moral culpability;
- improved institutional outcomes.

The same author designed the framework, performed the screening, assembled the packets, and made the assessments. Frozen inputs, hashes, schemas, and executable checks reduce discretionary drift and expose the work to audit. They do not supply independent judgment.

## Next evidence gate

The next material test is a preregistered clean-room reconstruction or independent application using these public packets. If external participation remains unavailable, the repository can still advance through new frozen case families, adversarial source perturbations, and prospective simulated decisions. Claims about independent reliability must remain unresolved until independent evidence exists.
