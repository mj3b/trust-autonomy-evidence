# From Formal Authority to Practical Human Control

## A traceable method for reconstructing human control in automated decisions

**Author:** Mark Julius Banasihan  
**ORCID:** [0009-0001-8121-2878](https://orcid.org/0009-0001-8121-2878)  
**Status:** Full review draft, v0.4

## Abstract

Institutions often treat a named human reviewer or approval step as evidence that an automated or autonomous system remains under human control. That inference can fail when the designated person lacks timely information, comprehension, authority, a feasible opportunity to challenge the system, or the ability to affect the outcome. This paper develops a frozen, evidence-traceable procedure for representing formal authority, practical control, and unresolved evidence in bounded public incident records. The protocol fixed the evidence cutoff, candidate collections, search vocabulary, eligibility rules, screening order, three selection strata, and missing-data treatment before candidate screening. It assembled three versioned historical case packets with claim-level provenance, categorical evidence states, and a chain from information access through effect. A protocol-frozen v0.6 adjudication applied the existing direct-and-contemporaneous rule to the Oko packet and reclassified access, comprehension, authority, feasibility, exercise, and effect from supported to partially supported. The current assessment set records partial support across those six Oko stages, supported authority with unsupported practical conditions in ZG710, and supported authority with unresolved practical conditions in F/A-18C. A frozen literature search located close work on effective oversight, institutional design, causal human involvement, traceable governance, and evidence-linked argument graphs. That work bounds the contribution to a governance-specific integration with a visible correction path. Institutions claiming human control bear an ethical burden to preserve evidence of practical force because unsupported attribution can obscure responsibility and exposure to harm. Three retrospective, single-assessor cases supply no population estimate, causal validation, independent-reliability result, or transfer claim for current learned systems.

**Keywords:** human oversight; meaningful human control; AI governance; incident reconstruction; assurance

## Resolved evidence decision

`PAPER-BLOCKER-01` identified a mismatch between Oko's released v0.3 supported states and the protocol's direct-and-contemporaneous evidence rule. The [v0.6 adjudication protocol](../protocols/oko-evidence-adjudication-v0.6.0.md) was frozen before reassessment. The resulting [change ledger](../assessments/v0.6.0/oko-change-ledger.json) records six transitions to partially supported and preserves v0.3.0 as release history. Missing contemporaneous records remain a limitation.

## 1. Introduction

### 1.1 The institutional problem

An approval step proves that an institution assigned a role. It does not show that the person received the relevant information, understood the system's limits, could challenge the proposed action in time, exercised that authority, or changed the outcome. A human-control claim therefore contains several empirical propositions that a signature or job title cannot establish by itself.

Human-factors research explains the mechanism. Automation can leave people responsible for rare or abnormal conditions after routine system operation has reduced their preparation for those conditions [@bainbridge1983ironies]. Situation awareness and intervention performance depend on what the person can perceive, understand, and project under the operating conditions [@endsley2017autonomy]. Trust affects reliance through the interaction of the person, system, task, and context [@lee2004trust]. Formal authority can remain intact as these operational conditions deteriorate.

The same problem appears in policy. Green finds that government rules often require human oversight without establishing that the designated people can perform the intended review [@green2022flaws]. Zhu et al. separate AI operative agency from human evaluative agency and identify verification, contestation, and substitution as oversight mechanisms [@zhu2026oversight]. These accounts direct attention to a documentary question: what evidence would justify reliance on an institutional claim that human authority had practical force in one consequential decision?

### 1.2 Research gap

Five research streams answer parts of that question. Meaningful-human-control scholarship defines moral, design, and institutional conditions for control [@santoni2018meaningful; @siebert2023meaningful; @davidovic2023purpose; @calvert2025principles]. Human-factors research explains why monitoring, comprehension, and timely intervention can fail [@bainbridge1983ironies; @lee2004trust; @endsley2017autonomy]. Oversight research identifies causal power, epistemic access, preparedness, intention, human learning, and institutional design as conditions for effectiveness [@sterz2024quest; @teeni2025learning; @laux2024distrust; @baum2026runtime]. Incident research specifies causal factors, reporting structures, and information needs [@mcgregor2021incidents; @macrae2022failure; @ezell2025incident; @paeth2025lessons; @wei2026reporting]. Assurance and traceability research connects claims to evidence, assumptions, uncertainty, validation rules, and provenance [@burr2023ethical; @paterson2025safety; @meng2026scientistone; @moghaddam2026arguments].

The closest prior work sharply limits the present claim. Sterz et al. define effective oversight through sufficient causal power, suitable epistemic access, self-control, and fitting intentions [@sterz2024quest]. Verdiesen, Santoni de Sio, and Dignum place oversight across technical, sociotechnical, and governance layers [@verdiesen2021oversight]. Laux treats overseer competence and incentives as institutional-design problems [@laux2024distrust]. Almada connects human intervention to the information and system conditions needed for contestability [@almada2019intervention]. Douer and Meyer show that causal responsibility can diverge from assigned human functions [@douer2020responsibility].

Prior methods also cover reconstruction and evidence. Dekker reconstructs human contributions inside an event sequence while controlling hindsight [@dekker2002reconstructing]. Pittaras and McGregor classify possible failure causes from incomplete open-source AI incidents [@pittaras2023taxonomic]. ScientistOne supplies claim-level evidence chains and post-hoc integrity checks [@meng2026scientistone]. Moghaddam proposes evidence-linked formal argument graphs with deterministic validation and provenance [@moghaddam2026arguments]. Alhalangy joins selective human review to a structured case-level audit trail in a synthetic institutional study [@alhalangy2026traceable].

The remaining contribution is one governance-specific integration: protocol fixation before case screening, a visible selection and stopping path, versioned public evidence packets, categorical missingness, a chain from information access through effect, claim-specific evidence fitness, conclusion dependency closure, versioned correction, and executable artifact checks. The formal search records 2,431 deduplicated records and preserves the limits created by inaccessible abstracts, one unresolved citation seed, and unavailable authenticated databases. The paper therefore states a bounded integration claim. Universal originality remains outside the evidence.

### 1.3 Research question and contribution

> How can a frozen, evidence-traceable assessment procedure represent formal human authority, practical human control, and unresolved evidence in a bounded public incident record?

The paper proposes a documentary assessment procedure. It defines a bounded action sequence, fixes the case-selection and missing-data rules, assembles a versioned evidence packet, assigns provenance to material statements, and evaluates six pre-action conditions: access, comprehension, authority, feasible challenge, exercised challenge, and effect. An explicit indeterminate state prevents missing records from becoming negative factual findings. A correction ledger preserves earlier outputs when a later adjudication changes a state.

The three cases demonstrate that procedure under contrastive evidence conditions. They do not test prevalence, classification accuracy, independent reliability, causal effects, or transfer to current learned systems. The institutional output is a proposed record set that a reviewer would need before relying on a practical-control claim. The ethical proposition is narrower: an institution that represents a decision as human-controlled should preserve evidence capable of testing whether the assigned authority had practical force.

### 1.4 Paper structure

Section 2 locates the procedure in meaningful-human-control, human-factors, oversight, incident-analysis, reconstruction, and assurance research. Section 3 defines the frozen method, artifact controls, literature search, and transfer boundary. Section 4 reports the released assessment and search results. Sections 5 through 7 separate interpretation, limitations, and proposed institutional record requirements.

## 2. Related work

### 2.1 Meaningful human control

Santoni de Sio and van den Hoven define meaningful human control through tracking and tracing. System behavior must respond to relevant human reasons, and human actors must be able to understand their role and bear responsibility [@santoni2018meaningful]. This account makes human presence insufficient because control depends on the relation among system behavior, human reasons, and identifiable responsibility.

Later work moves the concept toward institutional and engineering use. Siebert et al. propose actionable properties that align ability, authority, and responsibility [@siebert2023meaningful]. Davidovic argues that designers must first state the purpose served by human control [@davidovic2023purpose]. Calvert places proximal intervention inside a wider system of distal control across design, deployment, and governance [@calvert2025principles]. Verdiesen, Santoni de Sio, and Dignum divide control across technical, sociotechnical, and governance layers [@verdiesen2021oversight]. Tsamados, Floridi, and Taddeo compare supervisory control with human-machine teaming for foundation-model systems [@tsamados2025control]. Zhu et al. frame oversight as human evaluative agency expressed through verification, steering, contestation, and substitution [@zhu2026oversight].

The present paper uses these sources to define the proposition being assessed. It does not offer a new philosophical account of meaningful human control.

### 2.2 Human oversight and the automation problem

Bainbridge shows how automation transfers rare, abnormal, and difficult work to people after routine operation has weakened the practice needed for that work [@bainbridge1983ironies]. Endsley connects autonomous-system performance to situation awareness, monitoring, workload, trust, and out-of-the-loop degradation [@endsley2017autonomy]. Lee and See model appropriate reliance as a relation among the person, automation, task, and environment [@lee2004trust]. Together, these mechanisms explain how nominal oversight can lose practical force.

Human response to algorithmic advice is conditional. Alon-Barkat and Busuioc find both automation bias and selective adherence across experimental public-sector decisions [@alonbarkat2023interactions]. Langer, Baum, and Schlicker separate the ability to detect error from a person's response tendency [@langer2024signal]. Haselager et al. propose a counterargument prompt that supports questioning of medical decision-support advice [@haselager2023reflection]. Dhanorkar, Passi, and Vorvoreanu identify a priori control, co-planning, real-time monitoring, and post hoc review in interviews with 17 experienced developers who use software agents [@dhanorkar2026practice].

Effectiveness also depends on causal and institutional conditions. Sterz et al. identify causal power, epistemic access, self-control, and fitting intentions [@sterz2024quest]. Baum and Laux distinguish constitutive human participation from corrective oversight and require genuine preparedness and capacity for the latter [@baum2026runtime]. Te'eni, Yahav, and Schwartz treat continual human learning as a condition for stable and adaptive control [@teeni2025learning]. Laux proposes institutional safeguards that anticipate fallible competence and incentives [@laux2024distrust]. Green's policy analysis reaches a related implication: oversight rules need evidence that people can perform the assigned review [@green2022flaws]. The present method converts these constructs into documentary questions about information, comprehension, authority, feasibility, action, and effect.

### 2.3 AI incident analysis and missing records

The AI Incident Database was created to provide a shared record of real-world failures and support learning across incidents [@mcgregor2021incidents]. Its reports remain public-source records with changing coverage and varying detail. Pittaras and McGregor respond to that constraint through expert classification of goals, technologies, and possible technical failure causes [@pittaras2023taxonomic]. Paeth et al. show that incident reports contain structural ambiguity and unavoidable epistemic uncertainty [@paeth2025lessons]. These limits support an explicit indeterminate state.

Macrae demonstrates that public investigative reports can support systematic analysis of sociotechnical failure in an autonomous system [@macrae2022failure]. Ezell, Roberts-Gaal, and Chan specify system, contextual, cognitive, access, tool, log, and documentation information needed to investigate AI-agent incidents [@ezell2025incident]. Wei and Heim locate those information needs inside institutional reporting systems and post-reporting action [@wei2026reporting]. The present method applies a narrower question to each packet: which records support a claim that assigned human authority could affect the bounded action?

### 2.4 Reconstruction, forensics, and assurance

Dekker treats accident reconstruction as recovery of what people could know and why their actions made sense inside the unfolding event [@dekker2002reconstructing]. This approach guards against hindsight and unsupported counterfactual blame. McDermid identifies time, knowledge independent of the automated system, and practiced skill as conditions for effective intervention [@mcdermid2019control]. These works closely anticipate the procedure's reconstruction logic and feasible-challenge stage.

Argument-based assurance asks whether evidence justifies a stated claim under explicit assumptions and uncertainty. Burr and Leslie extend that structure to ethical and social claims [@burr2023ethical]. AMLAS applies it to machine-learning safety across development and deployment [@paterson2025safety]. Lam et al. define scope, criteria, evidence, and reporting for assurance audits of algorithmic systems [@lam2024assurance]. The present procedure borrows this claim-evidence discipline for retrospective assessment. It issues no safety case for Oko or Patriot.

Recent forensic work provides closer technical neighbors. Leung et al. reconstruct changing AI system state for insurance claims [@leung2026cer]. Ledjaki et al. preserve and replay prompt-level evidence through a chain-of-custody design [@ledjaki2026prompt]. These papers constrain the contribution to the specific combination of practical human control, public case selection, categorical missingness, and executable repository checks.

ScientistOne supplies a closer architecture for research verifiability. Its Chain-of-Evidence framework requires claims to trace to evidence, and its post-hoc audit checks scores, specification violations, references, and method-code alignment [@meng2026scientistone]. Moghaddam's argument graphs treat each AI-assisted step as a claim that must pass evidence and reasoning constraints before entering an official record [@moghaddam2026arguments]. Alhalangy integrates prediction, explanation, selective review, and an audit trail into a synthetic institutional decision pathway [@alhalangy2026traceable]. Lee, Yoon, and Lee position oversight authority, record duties, and auditability in the pre-design governance decision [@lee2026governance]. These sources establish prior work for traceability, evidence-linked argument, and prospective record design. The present adaptation applies five evidence-fitness dimensions and dependency closure to retrospective public-case claims. Independent review has yet to test those judgments.

### 2.5 Synthesis

Existing research supplies theories of control, evidence about oversight performance, causal-role taxonomies, institutional-design principles, retrospective reconstruction methods, public incident-analysis procedures, reporting requirements, assurance logic, claim-evidence architecture, and forensic evidence controls. This paper studies one governance-specific integration of those elements in a frozen public-case procedure.

The contribution is methodological and bounded. It asks how a reader can inspect the path from candidate selection to source packet, provenance label, assessment state, figure, and manuscript claim. The current evidence shows that the procedure can generate that path for three selected packets. It does not show that another assessor would agree, that the categories are valid across domains, or that use of the procedure improves institutional decisions.

## 3. Method

### 3.1 Study design

This is a retrospective, purposefully selected, single-assessor methods study. The unit of analysis is one bounded machine-mediated decision or action sequence. The method assesses documentary support for a practical-control proposition within that boundary. It does not assess personal blame, legal liability, or moral character.

### 3.2 System inclusion and transfer boundary

The frozen protocol used a functional and historically neutral system boundary. A case qualified when an identifiable machine-based system generated an inference, classification, recommendation, communication, decision, or action that affected a person, institution, digital setting, or physical setting. Oko concerns a rule-based early-warning inference. The Patriot cases concern automated detection, tracking, classification, and engagement support. These systems differ materially from present learned models and agents. Transfer therefore depends on shared mechanisms such as time compression, information dependence, intervention rights, and causal effect.

### 3.3 Protocol freeze and evidence cutoff

The public-case protocol and empty selection register reached `main` at commit `180ddda1d70f0ee36faaf8875e839bbc99cbbec2`. The evidence cutoff was 6 August 2026 at 23:59:59 UTC. The protocol fixed the candidate collections, eighteen search terms, six eligibility conditions, exclusion rules, chronological screening order, three strata, first-eligible rule, and missing-data treatment. Candidate screening began after the freeze commit.

### 3.4 Candidate collections and search

The candidate pool came from two public collections. The AI Incident Database snapshot contained 1,607 incidents and 7,452 linked reports; 828 incidents matched at least one frozen term. The OECD AI Incidents and Hazards Monitor interface exposed the first 100 rows returned by the frozen query. The snapshot and export are preserved with SHA-256 hashes in the selection register. The combined search output contains 928 candidate records. The OECD interface reported about 3,635 matches and capped export at 100 visible rows. Date probes found no OECD result before 2020, while all selected cases predated 2020 and came from the AI Incident Database.

### 3.5 Eligibility, strata, and stopping

An eligible case required an identifiable system output or action, a bounded sequence, two reports from different authors or organizations, one primary or official record, lawful citation and analysis, and compliance with the evidence cutoff. The incomplete-evidence stratum allowed two independent secondary reports after a documented unsuccessful search for an official record. Benchmark demonstrations, unbounded performance reports, single-source events, private-evidence dependencies, rights conflicts, duplicates, and post-cutoff evidence were excluded.

Candidates were deduplicated, sorted by event date and collection identifier, and screened until the first eligible case filled each of three strata: pre-action intervention, incomplete or conflicting evidence, and authority without practical force. Screening stopped after five candidates. The strata anticipate the headline contrasts. The case set therefore demonstrates procedure execution under those conditions and supplies no independent discrimination test.

**Figure 1. Frozen selection and stopping.** The figure shows the chronological decisions for the five screened candidates and the point at which all three strata were filled.

### 3.6 Versioned evidence packets

Each selected case packet defines the action boundary and chronology; lists title, issuer, author, dates, URLs, source class, and preservation state; records unavailable evidence; labels material statements; states publication-rights limits; and preserves hashes for locally stored files. Remote-only sources are cited with metadata and retrieval information. The packet manifest proves the bytes preserved in the repository at that version. It makes no claim about later remote content or source truth.

### 3.7 Assessment contract

The assessment contract records six autonomy variables, twelve trust-evidence propositions, and nine practical-control stages. The current paper compares six pre-action stages: access, comprehension, authority, feasibility, exercise, and effect. Every stage receives one categorical state: supported, partially supported, unsupported, indeterminate, or outside scope. Material statements receive one provenance label: direct record, source claim, assessor inference, or unresolved.

A bounded practical-force conclusion requires supported findings for access, authority, feasibility, exercise, and effect. Correction and repair are required for a wider institutional-accountability conclusion. Reform requires longitudinal evidence.

### 3.8 Missing evidence and inference

Missing public evidence produces an indeterminate state unless the packet establishes that a required record should exist and eligible evidence shows the condition was absent. This rule blocks a common inference error in retrospective work: converting an unavailable log, display, inquiry, or internal record into a finding that the underlying condition failed. The report separates what a source states, what a preserved record directly shows, what the assessor infers, and what remains unresolved.

### 3.9 Artifact and consistency controls

Repository checks validate schemas, packet hashes, selection invariants, cross-case interactions, derived figure data, release manifests, and prespecified mutations. These checks reproduce declared transformations and detect internal contradictions. They do not reproduce the assessor's historical judgments.

The v0.6 Chain-of-Evidence adaptation maps each material claim to exact locators, records a human support attestation, and tests directness, contemporaneity, independence, completeness, and publication authority. A dependency graph controls which claims may enter a conclusion. The integrity audit adapts ScientistOne's score verification, specification-violation, reference-verification, and method-code-alignment checks, then adds evidence-fitness and dependency-closure checks. A separate literature-support register maps material manuscript sentences to checked references.

### 3.10 Formal literature search

A v0.7 protocol fixed eight query families, inclusion rules, screening states, deduplication, fifteen citation seeds, and a contribution rejection test before retrieval. Semantic Scholar served as the controlling reproducible index. Every direct-search token and every returned citation page were retrieved. Crossref checked DOI metadata, while OpenAlex compared seed coverage. Publisher, proceedings, preprint, and institutional pages were used to verify the close set.

AI assistance assigned preliminary triage proposals. Mark Julius Banasihan remains the decision owner. An abstract-only record can support a bounded description of the source's declared purpose or model. A wider substantive claim requires checked full text. Authenticated Scopus or Web of Science access and several disciplinary interfaces remain open.

### 3.11 Frozen Oko adjudication

The v0.6 adjudication asked which states follow when the existing definitions are applied to the frozen Oko packet. It admitted no new historical source. The evidence cutoff, packet, six stage questions, state rules, and dependency rule were fixed before reassessment. Retrospective first-person testimony directly supports what a participant later reported. Its publication date prevents it from satisfying the contemporaneous-record requirement for a supported 1983 state. The v0.3.0 assessment remains preserved. A separate ledger records each v0.6 change.

## 4. Results

### 4.1 Selection result

The search preserved 928 candidate records. Five candidates were screened in chronological order. Two were excluded: one lacked two independent reports of a bounded autonomous action, and one lacked a bounded action sequence. AIID-27 filled pre-action intervention, AIID-444 filled authority without practical force, and AIID-445 filled incomplete or conflicting evidence. Screening then stopped. The remaining 923 candidates carry no exclusion decision.

### 4.2 Oko, 1983

The v0.3.0 release classified access, comprehension, authority, feasibility, exercise, and effect as supported. The frozen v0.6 adjudication classifies all six as partially supported. The packet contains retrospective participant accounts and an independent retrospective reconstruction. It contains no located contemporaneous Soviet command log, official incident record, or investigation file. The correction aligns the state labels with the evidence rule and preserves the missing historical record as a limitation. The packet supports a bounded account of what later sources report. It supplies no sole-cause finding for the ultimate outcome.

### 4.3 Patriot ZG710, 2003

The ZG710 packet supports formal engagement authority. It records a decision window of about one minute, incomplete communication, restricted access to the wider air picture, training that emphasized trust in the system, and identification weaknesses. Within the packet, comprehension, feasible challenge, exercised challenge, and protective effect are unsupported. The assessment addresses the practical-control chain. It assigns no individual legal or moral responsibility.

### 4.4 Patriot F/A-18C, 2003

The F/A-18C packet supports the detection-to-engagement sequence and formal authority. The full inquiry, system logs, operator displays, and classified technical report were unavailable. Access is partially supported; comprehension, feasibility, and exercised challenge are indeterminate; effect is unsupported because the engagement proceeded and the aircraft was lost. The unresolved states preserve the difference between a missing public record and evidence that a condition failed.

### 4.5 Cross-case practical-control chain

Figure 2 compares the six pre-action stages. Oko carries partial support across the chain. ZG710 carries supported authority, partial access, and unsupported comprehension, feasibility, exercise, and effect. F/A-18C carries supported authority, partial access, indeterminate comprehension, feasibility, and exercise, and unsupported effect.

**Figure 2. Practical-control chain.** The result shows that assigned authority can coexist with different states for information, understanding, opportunity, action, and effect. The comparison reports the procedure's output for purposefully selected cases. It supplies no frequency estimate.

### 4.6 Decision paths and trust-evidence states

Figure 3 traces each bounded sequence from machine output through human and institutional action. Its relative spacing reflects the absence of a defensible common time scale. Figure 4 reports the twelve trust-evidence propositions by case. The categorical states are kept separate because the protocol defines no validated aggregation rule.

### 4.7 Integrity and correction results

The v0.6 integrity audit maps fifteen material repository claims. Every declared claim passes traceability. The versioned Oko correction closes the prior protocol-consistency and dependency failure within the declared procedure. An independent-validity claim remains ineligible. Nine negative controls confirm that the audit detects prespecified corruptions. Six Oko adjudication mutations test state, evidence, and dependency records. These results show internal contract behavior. They establish no external validity.

**Figure A3. Claim-evidence integrity.** The matrix shows that traceability and conclusion eligibility are separate decisions. It assigns no numeric score.

### 4.8 Formal search result

The eight Semantic Scholar queries returned 184 records. Fourteen resolved seed chains returned 2,482 reference and citation records. L12 returned `404` for both chain endpoints. The combined pool contains 2,431 deduplicated records. Preliminary triage proposes twelve close additions and retains thirteen earlier matrix records found in the pool. Seventy-seven records contain both control and evidence terms and require author attention. Another 1,087 records lack abstracts and remain inaccessible for substantive screening. Three records fall after the publication cutoff.

Crossref resolved 22 of 25 DOI-bearing retained proposals. OpenAlex resolved thirteen of fifteen citation seeds, including an L12 record with zero indexed links. Different reference and citation counts across indexes show that chain coverage depends on the selected index. The search therefore supports a declared closest-work analysis and a bounded integration statement. It does not support universal originality.

## 5. Discussion

### 5.1 Formal authority and practical force

Formal authority answers one question: who was permitted to approve, reject, modify, stop, or escalate? Practical control asks whether that permission had causal force in the bounded decision. Causal force depends on a connected chain. The person must receive relevant information, interpret it, retain intervention rights, have a feasible opportunity to act, exercise judgment, and affect execution. A break at any required stage makes the wider practical-force conclusion ineligible under this protocol.

The cross-case result illustrates the mechanism. Both Patriot packets support formal authority. ZG710 records absent practical conditions in the available evidence, while F/A-18C leaves several conditions unresolved. Oko's retrospective accounts support the reported sequence only partially under the direct-and-contemporaneous rule. The figure therefore turns “human in the loop” into testable documentary propositions.

### 5.2 The evidentiary function of an indeterminate state

Public incident records are shaped by classification, litigation, institutional disclosure, journalism, preservation, and time. A missing operator display or inquiry file can block a judgment about comprehension or feasibility. It cannot establish that the operator lacked comprehension or opportunity. The indeterminate state holds that boundary. It also makes the missing record visible as a research result and a recordkeeping requirement.

### 5.3 Records institutions would need

An institution seeking to substantiate practical control should preserve the information shown to the reviewer, timestamps, system state, uncertainty and known gaps, independent evidence, authority, available interventions, action taken, execution changes, and downstream effect. These records let an investigator test the chain after an incident and let an assurance team test it before deployment. Their presence supports inspectability. Safe, lawful, or beneficial outcomes require separate evidence.

### 5.4 Relationship to prior research

The method operationalizes established constructs at the level of a public evidence packet. Tracking, tracing, epistemic access, causal power, institutional design, and contestability define what control may require [@santoni2018meaningful; @sterz2024quest; @laux2024distrust; @almada2019intervention]. Human-factors research explains why monitoring and challenge can fail [@bainbridge1983ironies; @endsley2017autonomy]. Incident analysis identifies the records needed to reconstruct an event [@ezell2025incident; @macrae2022failure]. Assurance and evidence-chain methods structure the path from proposition to evidence and conclusion [@burr2023ethical; @meng2026scientistone; @moghaddam2026arguments]. The repository joins these functions in one versioned assessment path.

### 5.5 Use for current AI governance

Contemporary systems can share the mechanisms tested here even when their architecture differs. Agentic software may compress review time, distribute actions across tools, obscure intermediate system state, or leave a reviewer with nominal stop authority. Dhanorkar, Passi, and Vorvoreanu show that developers already perform several forms of agent oversight work [@dhanorkar2026practice]. Alhalangy and Lee, Yoon, and Lee show how escalation and record duties can enter prospective governance design [@alhalangy2026traceable; @lee2026governance]. Future work can apply the frozen chain to contemporary agent traces, appeals, high-stakes recommendations, and tool-mediated actions. Each application requires a new protocol and evidence boundary.

### 5.6 Ethical burden of proof

Human-control language can distribute responsibility, reassure affected people, and justify deployment. Those functions create an ethical burden of proof. An institution should preserve evidence capable of testing the practical-control chain when it represents a consequential system as human-controlled. The burden concerns the institution's claim and records. It does not presume individual fault.

This position follows from the risk of nominal oversight. A role assignment can place responsibility on a person who lacks information, capacity, opportunity, or causal power [@green2022flaws; @sterz2024quest; @douer2020responsibility]. Institutional design should anticipate human fallibility and incentives [@laux2024distrust]. The proposed record set lets affected people, investigators, and oversight bodies examine whether responsibility was attached to practical authority. It guarantees no safe or just outcome.

## 6. Limitations

The design has several limits. The three strata were defined around the headline contrasts, and screening stopped after five candidates. The selected set demonstrates the procedure under those anticipated conditions. It estimates no prevalence and provides no independent classification test. Two cases concern one system family and operating period. Oko and Patriot differ materially from present learned systems.

The evidence is retrospective and public. Classified material, internal logs, complete displays, and some inquiry records were unavailable. Some cited content remains remote-only. Oko relies on later participant accounts and lacks a located contemporaneous command record. Source agreement can reflect shared dependence on an earlier account. Packet hashes prove preservation of stored bytes and do not prove source truth.

One assessor designed and applied the method. The study supplies no inter-rater reliability, construct-validity estimate, causal effect, safety effect, legal-sufficiency judgment, or outcome comparison. Artifact tests detect internal inconsistency and prespecified corruption. They do not validate historical interpretation.

The formal search used open indexes and official source pages. Machine triage leaves 77 records for author attention and 1,087 inaccessible records. Authenticated Scopus or Web of Science, IEEE Xplore, ACM Digital Library, PhilPapers, and HeinOnline or an equivalent legal index remain open. The contribution language is therefore bounded to the declared search and reviewed close set.

## 7. Institutional implications

An assurance team, regulator, deployer, or incident investigator can use the practical-control chain as a proposed evidence request. Before relying on a human-control claim, the reviewer should ask for:

1. the exact information and system output shown to the named person;
2. timestamps connecting output, review, action, and irreversible commitment;
3. model or system version, operating state, uncertainty, and known limits;
4. independent information available for challenge;
5. role delegation and tested approve, reject, modify, stop, and escalation rights;
6. staffing, workload, latency, access, and institutional conditions that affected feasibility;
7. the contemporaneous decision, challenge, or escalation record;
8. evidence that the intervention propagated into execution;
9. appeal, correction, repair, and reform records when the claim extends beyond pre-action control;
10. missing, inaccessible, or deleted records and the retention rule that governed them.

This proposed request converts a general assurance statement into inspectable propositions. It proves no legal compliance, safety, fairness, or accountability outcome by itself.

## 8. Conclusion

An institution cannot substantiate practical human control through a named reviewer or approval step alone. The claim requires evidence that the person received and understood relevant information, held authority, could act in time, exercised judgment, and affected execution. This requirement carries an ethical burden of proof when human-control language assigns responsibility or reassures people exposed to a consequential system. The frozen method produced traceable, bounded distinctions across three public packets and exposed where the historical record could not support a finding. Its versioned correction path also showed how a released claim can be narrowed without erasing the earlier record.

The result is a method demonstration. Independent assessors, varied case families, contemporary system traces, and prospective decision studies are needed before the method can support reliability, validity, or institutional-effect claims.

## Data and materials availability

The repository, versioned releases, packets, assessments, figure data, audit outputs, search files, and release manifests are available at [github.com/mj3b/trust-autonomy-evidence](https://github.com/mj3b/trust-autonomy-evidence). The v0.6.0 evidence archive has the version DOI [10.5281/zenodo.21865007](https://doi.org/10.5281/zenodo.21865007). The all-versions DOI is [10.5281/zenodo.21841127](https://doi.org/10.5281/zenodo.21841127). The formal search data and this manuscript remain branch artifacts until a later version-specific archive is released.

## Ethics and publication authority

The study uses public records and contains no participant recruitment, intervention, or direct interaction with living individuals. The repository preserves eligible public-domain and openly licensed material, cites proprietary sources through metadata and limited paraphrase, and excludes personal, confidential, institutionally restricted, and security-sensitive material under the frozen protocol. No institutional determination about human-subjects review has been obtained. The author must check Harvard and venue requirements before submission and must not describe the study as exempt without the applicable determination.

## Author contributions

Mark Julius Banasihan: Conceptualization, methodology, investigation, data curation, software, validation, visualization, writing of the original draft, review and editing, project administration, and accountable authorship. This statement will be mapped to the selected venue's required taxonomy before submission.

## AI-assistance disclosure

Generative AI tools assisted with literature discovery, metadata organization, preliminary screening proposals, draft development, code generation, figure and consistency checks, and language revision. Mark Julius Banasihan defined the research question and protocols, approved the evidence and assessment decisions, verified the sources used for claims, controlled the repository releases, and remains responsible for the analysis, interpretations, errors, and submitted text. The final disclosure will follow the selected venue's current policy.
