# From Formal Authority to Practical Human Control

## A traceable method for reconstructing human control in automated decisions

<!-- SOURCE-CITATION-NOTE-START -->
> **Citation note for repository readers.** Strings such as `[@bainbridge1983ironies]` are Pandoc citation identifiers. Each identifier maps to one checked record in [`references.bib`](references.bib). The [reader edition](manuscript-reader.md) converts them into clickable author-year citations.
<!-- SOURCE-CITATION-NOTE-END -->

**Author:** Mark Julius Banasihan  
**ORCID:** [0009-0001-8121-2878](https://orcid.org/0009-0001-8121-2878)  
**Affiliation:** Independent Researcher, Node & Norm, United States  
**Correspondence:** [mab7898@g.harvard.edu](mailto:mab7898@g.harvard.edu); [markjuliusbanasihan@gmail.com](mailto:markjuliusbanasihan@gmail.com)  
**Status:** Proposition-reviewed working manuscript, v0.16.0 rebuild

## Abstract

Institutions often treat a named reviewer or approval step as proof that an automated decision remained under human control. That proof can fail when the person lacked usable information, comprehension capacity, intervention authority, sufficient time, or an effective path for changing execution. This study asks what evidence an investigator would need to distinguish assigned authority from practical human control in one consequential decision.

The study introduces a frozen, evidence-traceable reconstruction procedure. It preserves case selection, source provenance, missing evidence, assessment changes, and claim dependencies. Six event-level conditions are evaluated separately: information access, comprehension capacity, intervention authority, intervention feasibility, exercised judgment, and execution propagation. Evidence is classified as supported, partially supported, unsupported, or indeterminate, preventing missing records from becoming factual findings.

The procedure was applied to three purposively selected historical cases representing contrasting evidence conditions. Under the direct-and-contemporaneous evidence rule, none supported the complete practical-control conclusion. Reassessment changed all six Oko event-level stages from supported to partially supported. The two Patriot cases retained evidence of formal human authority while producing unsupported or unresolved findings elsewhere in the practical-control chain.

An open-index search produced 2,431 deduplicated records and located prior research addressing each component separately. Within the reviewed source set, no source supplied the complete reconstruction-and-audit procedure. This remains a bounded search result. The three retrospective, single-assessor cases provide no prevalence estimate, independent-reliability result, causal validation, or transfer finding for present learned systems. The study proposes the records institutions should preserve when human control is used to justify deployment, assign responsibility, or explain a consequential automated decision.

**Keywords:** human oversight; meaningful human control; AI governance; incident reconstruction; assurance

## Correction result carried into this study

An earlier Oko assessment classified six event-level stages as supported even though the packet relied on retrospective accounts and lacked contemporaneous command records. I froze a reassessment rule before recoding the case. Applying that rule changed all six stages to partially supported. The earlier assessment remains preserved, and the change ledger records what changed and why. This correction demonstrates one function of the method: a later review can narrow a claim without erasing the research history.

## 1. Introduction

### 1.1 The institutional problem

An approval step identifies who was assigned responsibility. Practical control requires additional evidence: the person received usable information, could interpret the system's output and limits, held intervention rights, had enough time and institutional support to act, exercised judgment, and propagated a change into execution. A signature or job title establishes none of those conditions by itself.

Human-factors research explains the mechanism. Automation can leave people responsible for rare or abnormal conditions after routine system operation has reduced their preparation for those conditions [@bainbridge1983ironies]. Situation awareness and intervention performance depend on what the person can perceive, understand, and project under the operating conditions [@endsley2017autonomy]. Trust affects reliance through the interaction of the person, system, task, and context [@lee2004trust]. Formal authority can remain intact as these operational conditions deteriorate.

The same problem appears in policy. Green finds that government rules often require human oversight without establishing that designated people can perform the intended review [@green2022flaws]. Zhu et al. separate AI operative agency from human evaluative agency and identify verification, contestation, and substitution as oversight mechanisms [@zhu2026oversight]. When an institution uses a human-control claim to justify deployment or assign responsibility, missing evidence can place responsibility on a person who lacked practical power and can preserve a safeguard that never worked. This study therefore asks a documentary question: what evidence would justify reliance on an institutional claim that human authority had practical force in one consequential decision?

### 1.2 Research gap

Five research streams answer parts of that question. Meaningful-human-control scholarship defines moral, design, and institutional conditions for control [@santoni2018meaningful; @siebert2023meaningful; @davidovic2023purpose; @calvert2025principles]. Human-factors research explains why monitoring, comprehension, and timely intervention can fail [@bainbridge1983ironies; @lee2004trust; @endsley2017autonomy]. Oversight research identifies causal power, epistemic access, preparedness, intention, human learning, and institutional design as conditions for effectiveness [@sterz2024quest; @teeni2025learning; @laux2024distrust; @baum2026runtime]. Incident research specifies causal factors, reporting structures, and information needs [@mcgregor2021incidents; @macrae2022failure; @ezell2025incident; @paeth2025lessons; @wei2026reporting]. Assurance and traceability research connects claims to evidence, assumptions, uncertainty, validation rules, and provenance [@burr2023ethical; @paterson2025safety; @meng2026scientistone; @moghaddam2026arguments].

The closest prior work sharply limits the present claim. Sterz et al. define effective oversight through sufficient causal power, suitable epistemic access, self-control, and fitting intentions [@sterz2024quest]. Verdiesen, Santoni de Sio, and Dignum place oversight across technical, sociotechnical, and governance layers [@verdiesen2021oversight]. Laux treats overseer competence and incentives as institutional-design problems [@laux2024distrust]. Almada connects human intervention to the information and system conditions needed for contestability [@almada2019intervention]. Douer and Meyer show that causal responsibility can diverge from assigned human functions [@douer2020responsibility].

Prior methods also cover reconstruction and evidence. Dekker reconstructs human contributions inside an event sequence while controlling hindsight [@dekker2002reconstructing]. Pittaras and McGregor classify possible failure causes from incomplete open-source AI incidents [@pittaras2023taxonomic]. ScientistOne supplies claim-level evidence chains and post-hoc integrity checks [@meng2026scientistone]. Moghaddam proposes evidence-linked formal argument graphs with deterministic validation and provenance [@moghaddam2026arguments]. Alhalangy joins selective human review to a structured case-level audit trail in a synthetic institutional study [@alhalangy2026traceable]. Recent close sources go further: Bahidika applies oversight tiers to public AI Incident Database records [@bahidika2026accountability], LaPosta publishes a runnable decision-chain protocol [@laposta2026conflict], Niazi, Hassani, and Lee define a versioned assurance case with a practical-override trace [@niazi2026rights], and Surve, Shabtai, and Elovici declare an audit-evidence method with a retrospective Cruise application [@surve2026cedar].

Prior research explains the conditions of effective oversight, the reconstruction of human action, the analysis of incomplete incident records, and the connection between claims and evidence. The unresolved problem is procedural. An investigator still needs one method for determining whether a specific institutional claim of human control is supported, contradicted, or unresolved in the surviving record.

This study connects the required steps into one inspectable path. The reader can see how a case was selected, which records entered the packet, what each record supports, where evidence is missing, whether human action propagated into execution, which conclusions depend on those findings, and how a later correction changed the result. Each component prevents a different inference failure. Frozen selection constrains outcome-informed case choice. Categorical missingness protects an unknown condition from becoming a negative factual finding. Evidence fitness prevents citation presence from standing in for adequate support. Dependency closure prevents a conclusion from surviving after a required claim fails. Versioned correction prevents revision from erasing the prior record.

The formal search records 2,431 deduplicated records. Within the sources that received full-text or proposition-level review, no source supplied this complete reconstruction-and-audit procedure. Another 980 retrieval outcomes and several authenticated database searches remain open. The closest-work finding therefore applies only to the reviewed source set.

### 1.3 Research question and contribution

> How can a frozen, evidence-traceable assessment procedure represent formal human authority, practical human control, and unresolved evidence in a bounded public incident record?

The study proposes a documentary assessment procedure. It defines a bounded action sequence, fixes the case-selection and missing-data rules, assembles a versioned evidence packet, assigns provenance to material statements, and evaluates six event-level conditions: information access, comprehension capacity, intervention authority, intervention feasibility, exercised judgment, and execution propagation. An explicit indeterminate state prevents missing records from becoming negative factual findings. A correction ledger preserves earlier outputs when a later adjudication changes a state.

The three cases demonstrate that procedure under contrastive evidence conditions. They do not test prevalence, classification accuracy, independent reliability, causal effects, or transfer to current learned systems. The institutional output is a proposed record set that a reviewer would need before relying on a practical-control claim. The ethical proposition is narrower: an institution that represents a decision as human-controlled should preserve evidence capable of testing whether the assigned authority had practical force.

### 1.4 Paper structure

Section 2 explains which parts of the problem prior research already solves. Section 3 derives the six-stage chain and explains the inference error prevented by each control. Section 4 reports what changed when the procedure was applied to three historical packets. Sections 5 through 7 explain the institutional consequence, evidence limits, and records required to substantiate a human-control claim.

## 2. Related work

### 2.1 Meaningful human control

Santoni de Sio and van den Hoven define meaningful human control through tracking and tracing. System behavior must respond to relevant human reasons, and human actors must be able to understand their role and bear responsibility [@santoni2018meaningful]. This account makes human presence insufficient because control depends on the relation among system behavior, human reasons, and identifiable responsibility.

Later work moves the concept toward institutional and engineering use. Siebert et al. propose actionable properties that align ability, authority, and responsibility [@siebert2023meaningful]. Davidovic argues that designers must first state the purpose served by human control [@davidovic2023purpose]. Calvert places proximal intervention inside a wider system of distal control across design, deployment, and governance [@calvert2025principles]. Verdiesen, Santoni de Sio, and Dignum divide control across technical, sociotechnical, and governance layers [@verdiesen2021oversight]. Tsamados, Floridi, and Taddeo compare supervisory control with human-machine teaming for foundation-model systems [@tsamados2025control]. Zhu et al. frame oversight as human evaluative agency expressed through verification, steering, contestation, and substitution [@zhu2026oversight].

The present paper uses these sources to define the proposition being assessed. It does not offer a new philosophical account of meaningful human control.

### 2.2 Human oversight and the automation problem

Bainbridge shows how automation transfers rare, abnormal, and difficult work to people after routine operation has weakened the practice needed for that work [@bainbridge1983ironies]. Endsley connects autonomous-system performance to situation awareness, monitoring, workload, trust, and out-of-the-loop degradation [@endsley2017autonomy]. Lee and See model appropriate reliance as a relation among the person, automation, task, and environment [@lee2004trust]. Together, these mechanisms explain how nominal oversight can lose practical force.

Human response to algorithmic advice is conditional. Alon-Barkat and Busuioc find both automation bias and selective adherence across experimental public-sector decisions [@alonbarkat2023interactions]. Langer, Baum, and Schlicker separate the ability to detect error from a person's response tendency [@langer2024signal]. Haselager et al. propose a counterargument prompt that supports questioning of medical decision-support advice [@haselager2023reflection]. Dhanorkar, Passi, and Vorvoreanu identify a priori control, co-planning, real-time monitoring, and post hoc review in interviews with 17 experienced developers who use software agents [@dhanorkar2026practice].

Two retained empirical sources expose different gaps between assigned oversight and practical effect. In a secondary analysis of 99 Tesla-user interviews, Suryana et al. report that perceived safety sometimes coexisted with failures to track driver reasons; takeover readiness and prior reliable experience also shaped perception [@suryana2024tesla]. The study concerns reported perception in partial driving automation and does not observe incident-control outcomes. In a 28-participant sandbox study, Li et al. report task-completion rates of 83.3 percent under direct manipulation and 61.9 percent under text guidance; delayed responses and difficult error correction also made intervention effects harder for participants to assess [@li2025sandbox]. The sample, tasks, model, and single qualitative coder limit transfer. Together, the studies support a mechanism claim: perceived control and formal feedback access can remain separate from demonstrated intervention effect.

Effectiveness also depends on causal and institutional conditions. Sterz et al. identify causal power, epistemic access, self-control, and fitting intentions [@sterz2024quest]. Baum and Laux distinguish constitutive human participation from corrective oversight and require genuine preparedness and capacity for the latter [@baum2026runtime]. Te'eni, Yahav, and Schwartz treat continual human learning as a condition for stable and adaptive control [@teeni2025learning]. Laux proposes institutional safeguards that anticipate fallible competence and incentives [@laux2024distrust]. Green's policy analysis reaches a related implication: oversight rules need evidence that people can perform the assigned review [@green2022flaws]. The present method converts these constructs into documentary questions about information, comprehension, authority, feasibility, action, and effect.

Design and governance research also show why those conditions depend on system architecture. Van der Waa et al. use human-agent team patterns to make allocation timing, sufficient understanding, halt or resume capability, and handover conditions explicit [@vanderwaa2020allocation]. Kolt argues that monitoring and detailed records can reduce information asymmetry and support intervention, while speed, opacity, and irreversible action can make conventional oversight ineffective [@kolt2025agents]. The first source offers conceptual design patterns and the second offers legal analysis. Neither supplies a field estimate of effective control.

### 2.3 AI incident analysis and missing records

The AI Incident Database was created to provide a shared record of real-world failures and support learning across incidents [@mcgregor2021incidents]. Its reports remain public-source records with changing coverage and varying detail. Pittaras and McGregor respond to that constraint through expert classification of goals, technologies, and possible technical failure causes [@pittaras2023taxonomic]. Paeth et al. show that incident reports contain structural ambiguity and unavoidable epistemic uncertainty [@paeth2025lessons]. These limits support an explicit indeterminate state.

Macrae demonstrates that public investigative reports can support systematic analysis of sociotechnical failure in an autonomous system [@macrae2022failure]. Ezell, Roberts-Gaal, and Chan specify system, contextual, cognitive, access, tool, log, and documentation information needed to investigate AI-agent incidents [@ezell2025incident]. Wei and Heim locate those information needs inside institutional reporting systems and post-reporting action [@wei2026reporting]. The present method applies a narrower question to each packet: which records support a claim that assigned human authority could affect the bounded action?

### 2.4 Reconstruction, forensics, and assurance

Dekker treats accident reconstruction as recovery of what people could know and why their actions made sense inside the unfolding event [@dekker2002reconstructing]. This approach guards against hindsight and unsupported counterfactual blame. McDermid identifies time, knowledge independent of the automated system, and practiced skill as conditions for effective intervention [@mcdermid2019control]. These works closely anticipate the procedure's reconstruction logic and feasible-challenge stage.

Reconstruction output also depends on the analytic frame and the available record. Zhang, Jing, and Sun assigned separate teams to apply HFACS, AcciMap, and STAMP to the same official report of the Tianjin Port fire and explosion [@zhang2018tianjin]. The methods produced different factor sets, and the authors state that missing report detail can hide material factors. One accident, analyst reconciliation, and dependence on one official report prevent treating the comparison as a validation against event truth. The study supports the narrower rule used here: method choice and source completeness must remain visible when a public-record reconstruction is interpreted.

Argument-based assurance asks whether evidence justifies a stated claim under explicit assumptions and uncertainty. Burr and Leslie extend that structure to ethical and social claims [@burr2023ethical]. AMLAS applies it to machine-learning safety across development and deployment [@paterson2025safety]. Lam et al. define scope, criteria, evidence, and reporting for assurance audits of algorithmic systems [@lam2024assurance]. The present procedure borrows this claim-evidence discipline for retrospective assessment. It issues no safety case for Oko or Patriot.

Recent forensic work provides closer technical neighbors. Leung et al. reconstruct changing AI system state for insurance claims [@leung2026cer]. Ledjaki et al. preserve and replay prompt-level evidence through a chain-of-custody design [@ledjaki2026prompt]. These papers constrain the contribution to the specific combination of practical human control, public case selection, categorical missingness, and executable repository checks.

ScientistOne supplies a closer architecture for research verifiability. Its Chain-of-Evidence framework requires claims to trace to evidence, and its post-hoc audit checks scores, specification violations, references, and method-code alignment [@meng2026scientistone]. Moghaddam's argument graphs treat each AI-assisted step as a claim that must pass evidence and reasoning constraints before entering an official record [@moghaddam2026arguments]. Alhalangy integrates prediction, explanation, selective review, and an audit trail into a synthetic institutional decision pathway [@alhalangy2026traceable]. Lee, Yoon, and Lee position oversight authority, record duties, and auditability in the pre-design governance decision [@lee2026governance]. These sources establish prior work for traceability, evidence-linked argument, and prospective record design. The present adaptation applies five evidence-fitness dimensions and dependency closure to retrospective public-case claims. Independent review has yet to test those judgments.

### 2.5 Synthesis

Existing research supplies theories of control, evidence about oversight performance, causal-role taxonomies, institutional-design principles, retrospective reconstruction methods, public incident-analysis procedures, reporting requirements, assurance logic, claim-evidence architecture, and forensic evidence controls. This paper studies one governance-specific integration of those elements in a frozen public-case procedure.

The contribution is methodological and bounded. It asks how a reader can inspect the path from candidate selection to source packet, provenance label, assessment state, figure, and manuscript claim. The current evidence shows that the procedure can generate that path for three selected packets. It does not show that another assessor would agree, that the categories are valid across domains, or that use of the procedure improves institutional decisions.

## 3. Method

### 3.1 Study design

This is a retrospective, purposively selected, single-assessor methods study. I chose a method demonstration because the first research problem concerns representation: can one public record distinguish assigned authority, practical control, and unresolved evidence without converting missing records into findings? The unit of analysis is one bounded machine-mediated decision or action sequence. The procedure assesses documentary support for a practical-control proposition within that boundary. Personal blame, legal liability, moral character, and population frequency remain outside the study.

### 3.2 System inclusion and transfer boundary

The frozen protocol used a functional and historically neutral system boundary. A case qualified when an identifiable machine-based system generated an inference, classification, recommendation, communication, decision, or action that affected a person, institution, digital setting, or physical setting. Oko concerns a rule-based early-warning inference. The Patriot cases concern automated detection, tracking, classification, and engagement support. These systems differ materially from present learned models and agents. Their value lies in inspectable mechanisms: time compression, information dependence, intervention rights, and the path from human judgment to execution. A future contemporary application must test whether those mechanisms transfer.

### 3.3 Protocol freeze and evidence cutoff

Knowing an outcome can influence case selection and interpretation. I therefore fixed the public-case protocol and empty selection register before screening. They reached `main` at commit `180ddda1d70f0ee36faaf8875e839bbc99cbbec2`. The evidence cutoff was 6 August 2026 at 23:59:59 UTC. The protocol fixed the candidate collections, eighteen search terms, six eligibility conditions, exclusion rules, chronological screening order, three strata, first-eligible rule, and missing-data treatment. The freeze constrains later choice; it supplies no independent protection against bias in the original design.

### 3.4 Candidate collections and search

The candidate pool came from two public collections. The AI Incident Database snapshot contained 1,607 incidents and 7,452 linked reports; 828 incidents matched at least one frozen term. The OECD AI Incidents and Hazards Monitor interface exposed the first 100 rows returned by the frozen query. The snapshot and export are preserved with SHA-256 hashes in the selection register. The combined search output contains 928 candidate records. The OECD interface reported about 3,635 matches and capped export at 100 visible rows. Date probes found no OECD result before 2020, while all selected cases predated 2020 and came from the AI Incident Database.

### 3.5 Eligibility, strata, and stopping

An eligible case required an identifiable system output or action, a bounded sequence, two reports from different authors or organizations, one primary or official record, lawful citation and analysis, and compliance with the evidence cutoff. The incomplete-evidence stratum allowed two independent secondary reports after a documented unsuccessful search for an official record. Benchmark demonstrations, unbounded performance reports, single-source events, private-evidence dependencies, rights conflicts, duplicates, and post-cutoff evidence were excluded.

Candidates were deduplicated, sorted by event date and collection identifier, and screened until the first eligible case filled each of three frozen strata: intervention before irreversible action, incomplete or conflicting evidence, and authority without practical force. The released selection register calls the first stratum `pre-action intervention`; this manuscript uses `event-level control` for the wider six-stage construct. Screening stopped after five candidates. The strata anticipate the headline contrasts. The case set therefore demonstrates procedure execution under those conditions and supplies no independent discrimination test.

**Figure 1. Frozen selection and stopping.** The figure shows the chronological decisions for the five screened candidates and the point at which all three strata were filled.

### 3.6 Versioned evidence packets

A reconstruction can change silently when a source disappears, a file is replaced, or a later account enters the evidence set. Each selected case therefore receives a versioned packet. The packet defines the action boundary and chronology; lists title, issuer, author, dates, URLs, source class, and preservation state; records unavailable evidence; labels material statements; states publication-rights limits; and preserves hashes for locally stored files. Remote-only sources are cited with metadata and retrieval information. The packet manifest proves which bytes the assessment used. It supplies no determination that a source is true.

### 3.7 Construct derivation and assessment contract

The six event-level stages came from a causal question: what must remain true for assigned authority to change execution? The chain begins when the person receives information and ends when an intervention propagates into the system or institutional action. A broken required stage blocks the wider event-control proposition. Table 1 shows how prior constructs become documentary questions and why each stage is needed.

**Table 1. Derivation of the event-level practical-control chain.**

| Stage | Prior construct | Why it enters the chain | Minimum observable evidence | Error prevented |
|---|---|---|---|---|
| Information access | Epistemic access and situation awareness [@sterz2024quest; @endsley2017autonomy] | Judgment cannot act on information the person never received | Timestamped delivery, interface, or access record | Treating post-action information as pre-action review |
| Comprehension capacity | Situation awareness, competence, and system understanding [@endsley2017autonomy; @green2022flaws] | Information has practical value only when the assigned person could interpret the output, limits, uncertainty, and alternatives | Role-appropriate materials plus evidence that they were usable under the operating conditions | Treating exposure to an output as usable understanding |
| Intervention authority | Causal power, delegation, and contestability [@sterz2024quest; @almada2019intervention] | The person needs enforceable rights to approve, reject, modify, stop, or escalate | Named delegation and functioning control rights | Treating an advisory role as decision authority |
| Intervention feasibility | Workload, timing, access, and institutional support [@bainbridge1983ironies; @mcdermid2019control] | Formal rights lose practical force when operating conditions defeat their use | Sufficient time, staffing, access, and response path | Treating ceremonial authority as an available intervention |
| Exercised judgment | Corrective oversight and active review [@baum2026runtime; @green2022flaws] | Assigned authority does not establish that judgment occurred | Contemporaneous decision, challenge, or escalation record | Treating automatic approval as active review |
| Execution propagation | Causal power and intervention effect [@sterz2024quest; @douer2020responsibility] | A changed review record can coexist with unchanged execution | Linked stop, modification, escalation, or downstream state change | Treating a recorded intervention as operationally effective |

The released machine-readable field named `effect` is interpreted here as execution propagation. This wording limits the finding to a linked change in execution. A counterfactual causal effect and a beneficial outcome require separate evidence.

The assessment contract also records six autonomy variables, twelve trust-evidence propositions, and three post-event stages: correction, repair, and reform. Every stage receives one categorical state: supported, partially supported, unsupported, indeterminate, or outside scope. Material statements receive one provenance label: direct record, source claim, assessor inference, or unresolved.

**Table 2. Assessment-state decision rules.**

| State | Code | Decision rule |
|---|:---:|---|
| Supported | S | Direct, contemporaneous evidence satisfies the stage definition. |
| Partially supported | P | Some required elements are present and a material gap remains. |
| Unsupported | U | Available evidence contradicts the stage or shows that the condition was absent. |
| Indeterminate | I | The packet lacks enough evidence to decide. |
| Outside scope | O | The stage does not apply within the declared case boundary, with a written reason. |

*Note.* A missing record produces an indeterminate state unless the protocol or case design establishes that the record should exist. The states are categorical. No numeric distance or aggregate score is assigned.

For case (c) and stage (j), the state is:

\[
s_{c,j}\in\{S,P,U,I,O\}.
\]

Let (R) contain information access, comprehension capacity, intervention authority, intervention feasibility, exercised judgment, and execution propagation. The event-level rule is:

\[
EventControl(c)=
\begin{cases}
FAIL, & \exists j\in R:s_{c,j}=U\\
UNRESOLVED, & \nexists j\in R:s_{c,j}=U\;\land\;\exists j\in R:s_{c,j}\in\{P,I\}\\
PASS, & \forall j\in R:s_{c,j}=S.
\end{cases}
\]

In plain language, one unsupported required stage makes the event-control proposition fail. When no stage is unsupported, a partial or indeterminate stage leaves the proposition unresolved. Every stage must be supported for a pass. The rule assigns no score and creates no ranking among cases.

Event control, institutional accountability, and institutional learning are separate propositions:

\[
EventControl=Access\land Comprehension\land Authority\land Feasibility\land Exercise\land Propagation,
\]

\[
AccountableControl=EventControl\land Correction\land Repair,
\]

\[
LearningControl=AccountableControl\land Reform.
\]

A later correction or reform cannot retroactively establish event-level control. These stages answer what the institution could do after the decision and whether the decision architecture changed.

For a contemporary packet with complete timestamps, the proposed intervention-time margin is:

\[
M_t=(t_{commit}-t_{access})-(t_{interpret}+t_{decide}+t_{transmit}+t_{propagate}).
\]

A nonnegative margin and a functioning intervention channel support timing feasibility. The three historical packets lack the complete timing inputs needed to calculate this measure. The formula defines a future measurement requirement and produces no new historical result.

### 3.8 Missing evidence and inference

Missing public evidence produces an indeterminate state unless the packet establishes that a required record should exist and eligible evidence shows the condition was absent. This rule blocks a common inference error in retrospective work: converting an unavailable log, display, inquiry, or internal record into a finding that the underlying condition failed. Unsupported and indeterminate therefore lead to different institutional conclusions. The first records evidence that a required condition was absent or contradicted. The second records an evidence deficit. The report separates what a source states, what a preserved record directly shows, what the assessor infers, and what remains unresolved.

### 3.9 Artifact and consistency controls

Traceable evidence can still support an overbroad claim, and a correct claim can become inconsistent with its data during revision. Repository checks therefore validate schemas, packet hashes, selection invariants, cross-case interactions, derived figure data, release manifests, and prespecified mutations. These checks reproduce declared transformations and detect internal contradictions. They do not reproduce the assessor's historical judgments.

The Chain-of-Evidence adaptation maps each material claim to exact locators, records a human support attestation, and tests directness, contemporaneity, independence, completeness, and publication authority. A dependency graph controls which claims may enter a conclusion. For material claim (q):

\[
Eligible(q)=Trace(q)\land Integrity(q)\land Support(q)\land Fitness(q)\land\bigwedge_{d\in Dep(q)}Eligible(d).
\]

The formula means that a conclusion cannot remain eligible after a required supporting claim fails or becomes unresolved. The integrity audit adapts ScientistOne's score verification, specification-violation, reference-verification, and method-code-alignment checks, then adds evidence-fitness and dependency-closure checks. A separate literature-support register maps material manuscript sentences to checked references.

### 3.10 Formal literature search

A v0.7 protocol fixed eight query families, inclusion rules, screening states, deduplication, fifteen citation seeds, and a contribution rejection test before retrieval. Semantic Scholar served as the controlling reproducible index. Every direct-search token and every returned citation page were retrieved. Crossref checked DOI metadata, while OpenAlex compared seed coverage. Publisher, proceedings, preprint, and institutional pages were used to verify the close set.

AI assistance assigned preliminary triage proposals. Mark Julius Banasihan reviewed the initial 89-record queue and remains accountable for every recorded decision. A separate frozen protocol governed AI-assisted screening of 71 recovered forward citations under his authorization. A v0.14 proposition protocol then required a stable locator, exact passage, bounded proposition, five-dimension fitness decision, limitation, reversal condition, and permission state for each of the 13 close sources. Five received bounded manuscript permission, two remain background-only, and six are quarantined. A direct-query overlay closed the fifth screening decision while preserving zero source-content permission. An abstract-only record supports only a bounded description of the source's declared purpose or model. A wider substantive claim requires checked full text and a stable proposition locator. Authenticated Scopus or Web of Science access and several disciplinary interfaces remain open.

### 3.11 Frozen Oko adjudication

The Oko correction tests whether a released conclusion can be narrowed without erasing the earlier record. The v0.6 adjudication admitted no new historical source. The evidence cutoff, packet, six stage questions, state rules, and dependency rule were fixed before reassessment. Retrospective first-person testimony directly supports what a participant later reported. Its publication date prevents it from satisfying the contemporaneous-record requirement for a supported 1983 state. The v0.3.0 assessment remains preserved. A separate ledger records each v0.6 change.

## 4. Results

### 4.1 Selection result

The search preserved 928 candidate records. Five candidates were screened in chronological order. Two were excluded: one lacked two independent reports of a bounded autonomous action, and one lacked a bounded action sequence. AIID-27 filled the frozen `pre-action intervention` selection stratum, AIID-444 filled authority without practical force, and AIID-445 filled incomplete or conflicting evidence. Screening then stopped. The remaining 923 candidates carry no exclusion decision.

### 4.2 Oko, 1983

The v0.3.0 release classified information access, comprehension capacity, intervention authority, intervention feasibility, exercised judgment, and execution propagation as supported. The frozen v0.6 adjudication classifies all six as partially supported. The packet contains retrospective participant accounts and an independent retrospective reconstruction. It contains no located contemporaneous Soviet command log, official incident record, or investigation file. The correction aligns the state labels with the evidence rule and preserves the missing historical record as a limitation. Under the categorical event-control rule, Oko remains unresolved because every required stage is partially supported. The packet supports a bounded account of what later sources report. It supplies no sole-cause finding for the ultimate outcome.

### 4.3 Patriot ZG710, 2003

The ZG710 packet supports formal engagement authority. It records a decision window of about one minute, incomplete communication, restricted access to the wider air picture, training that emphasized trust in the system, and identification weaknesses. Within the packet, comprehension capacity, intervention feasibility, exercised judgment, and execution propagation are unsupported. The event-control proposition therefore fails under the categorical rule even though formal authority is supported. The assessment addresses the practical-control chain. It assigns no individual legal or moral responsibility.

### 4.4 Patriot F/A-18C, 2003

The F/A-18C packet supports the detection-to-engagement sequence and formal authority. The full inquiry, system logs, operator displays, and classified technical report were unavailable. Information access is partially supported; comprehension capacity, intervention feasibility, and exercised judgment are indeterminate; execution propagation is unsupported because the engagement proceeded and the aircraft was lost. The event-control proposition fails because one required stage is unsupported. The indeterminate stages separately preserve what the public record cannot resolve.

### 4.5 Cross-case practical-control chain

Figure 2 compares the six event-level stages. Oko carries partial support across the chain. ZG710 carries supported authority, partial access, and unsupported comprehension, feasibility, exercise, and propagation. F/A-18C carries supported authority, partial access, indeterminate comprehension, feasibility, and exercise, and unsupported propagation.

**Figure 2. Practical-control chain.** The first six rows determine the event-control result; the final three record post-event response. Assigned authority can coexist with different states for information, understanding, opportunity, action, and execution propagation. The comparison reports the procedure's output for purposively selected cases and supplies no frequency estimate.

**Table 3. Practical-control states across three public cases.**

| Stage | Oko, 1983 | Patriot ZG710, 2003 | Patriot F/A-18C, 2003 |
|---|:---:|:---:|:---:|
| Information access | P | P | P |
| Comprehension capacity | P | U | I |
| Intervention authority | P | S | S |
| Intervention feasibility | P | U | I |
| Exercised judgment | P | U | I |
| Execution propagation | P | U | U |
| Correction | O | O | O |
| Repair | O | U | U |
| Institutional reform | P | S | S |

*Note.* S = supported; P = partially supported; U = unsupported; I = indeterminate; O = outside scope. The first six rows determine the event-control result. Correction, repair, and institutional reform describe post-event response and do not alter that result. The table reports 27 item-level findings and supplies no frequency, causal, or population estimate.

The formal-authority comparison exposes the decision consequence of the full chain. A role assignment would preserve supported authority in both Patriot cases. The event-level procedure reaches a failing result in both because other required stages are unsupported. Oko remains unresolved because retrospective evidence partially supports each stage and satisfies none at the supported level.

**Table 4. Formal authority compared with event-level practical control.**

| Case | Formal-authority state | Event-control result | Why the wider result differs | Institutional meaning |
|---|:---:|:---:|---|---|
| Oko, 1983 | P | Unresolved | Every required stage is partially supported under the direct-and-contemporaneous rule | The surviving record cannot substantiate the complete practical-control claim |
| Patriot ZG710, 2003 | S | Fail | Comprehension, feasibility, exercise, and propagation are unsupported | Assigned authority lacked documented practical force in the bounded decision |
| Patriot F/A-18C, 2003 | S | Fail | Propagation is unsupported; access is partial; comprehension, feasibility, and exercise remain indeterminate | Formal authority survives while the wider control claim fails and several mechanisms remain unresolved |

*Note.* These three cases were selected to expose contrasting evidence conditions. The two failing results and one unresolved result describe this purposive set. They estimate no population rate.

### 4.6 Decision paths and trust-evidence states

Figure 3 traces each bounded sequence from machine output through human and institutional action. Its relative spacing reflects the absence of a defensible common time scale. Figure 4 reports the twelve trust-evidence propositions by case. The categorical states are kept separate because the protocol defines no validated aggregation rule.

**Figure 3. Decision paths from machine output through institutional response.** Each row preserves the order of documented machine, human, and institutional actions. Horizontal spacing separates stages for reading and does not encode a common elapsed-time scale. The figure exposes where intervention occurred, failed, or remains unresolved. It supplies no causal-effect estimate.

**Figure 4. Trust-evidence states across three public cases.** The matrix reports twelve proposition-level evidence states for each packet. Supported, partially supported, unsupported, indeterminate, and outside-scope states remain categorical. The display shows where the record is strong, adverse, incomplete, or irrelevant. It supplies no combined trust score or case ranking.

### 4.7 Integrity and correction results

The v0.14 integrity audit maps 32 material repository claims. The versioned Oko correction closes the prior protocol-consistency and dependency failure within the declared procedure. The completed 89-record and 71-record ledgers make their screening counts eligible within bounded workflow scopes. The 13-source proposition ledger makes five source propositions eligible only at their recorded scope and locators. Independent validity, 980 retrieval outcomes, the 177-record backward-reference stratum, and authenticated-database coverage remain outside the completed evidence base. Thirty-three negative controls confirm that the audit detects prespecified corruptions. Six Oko adjudication mutations test state, evidence, and dependency records. These results show internal contract behavior. They establish no external validity.

**Figure A1. Mutation-response matrix.** Each prespecified corruption is paired with the control expected to detect it. A detected mutation shows that the committed check responded to that injected error. It does not estimate sensitivity to unknown mistakes.

**Figure A2. Reproducibility lineage.** The upper lane traces the research record from frozen collections to the release archive. The lower lane traces the figure pipeline from plot inputs to integrity checking. The labeled connector runs from Assessments to Plot inputs because recorded assessment states become inputs to the figure builder. The diagram shows which transformations can be repeated from preserved artifacts and where human judgment remains necessary. Artifact lineage supplies no independent reproduction of the research conclusions.

**Figure A3. Claim-evidence integrity.** The matrix shows five evidence gates and conclusion eligibility for forty mapped claims. Independent validity and search-coverage limits remain visible. It assigns no numeric score.

**Figure A4. Versioned correction of the Oko assessment.** All six event-level stages move from supported in v0.3.0 to partially supported in v0.6.0. The packet remained fixed. The frozen evidence rule required the correction, and the change supplies no new historical evidence.

**Table A1. Oko correction record.**

| Stage | v0.3.0 | v0.6.0 | Material gap recorded in v0.6.0 |
|---|:---:|:---:|---|
| Information access | S | P | No contemporaneous delivery, interface, or command record was located. |
| Comprehension capacity | S | P | No contemporaneous reasoning, review, or explanation record was located. |
| Intervention authority | S | P | No contemporaneous delegation or command-procedure record was located. |
| Intervention feasibility | S | P | No contemporaneous timing or operating record was located. |
| Exercised judgment | S | P | No contemporaneous decision or communication log was located. |
| Execution propagation | S | P | No contemporaneous linked action, stop, or escalation record was located. |

*Note.* The v0.6.0 adjudication applied a protocol frozen before reassessment and admitted no new historical source.

### 4.8 Formal search result

The eight Semantic Scholar queries returned 184 records. Fourteen resolved seed chains returned 2,482 reference and citation records. L12 returned `404` for both chain endpoints. The combined pool contains 2,431 deduplicated records. The frozen machine pass proposed 12 close records and placed 77 records in an attention queue. Author review confirmed all 12 proposed close records. The 77 attention records produced 15 additional close sources, 32 background sources, 20 topic exclusions, and 10 single-component exclusions. The final full-pool state therefore contains 27 close records, 45 background records, 1,259 topic exclusions, 10 single-component exclusions, 1,087 inaccessible records, and three records outside the publication cutoff.

Crossref resolved 22 of 25 DOI-bearing retained proposals. OpenAlex resolved thirteen of fifteen citation seeds, including an L12 record with zero indexed links. Different reference and citation counts across indexes show that chain coverage depends on the selected index. The completed author queue supports a declared closest-work analysis and a bounded integration statement. The inaccessible records and open database searches prevent a universal originality or systematic-coverage claim.

**Figure 5. Formal search retrieval and final screening state.** The left panel traces 184 direct-query records and 2,482 citation-chain records through pooling and deduplication. The right panel reports the six final screening classes on a logarithmic count axis. Blue points identify the 27 close and 45 background records. The annotation records closure of all 89 author decisions. The 1,087 inaccessible records remain a separate coverage limit.

**Table 5. Formal search and final screening state.**

| Stage | Record class | Count | Status |
|---|---|---:|---|
| Retrieval | Direct queries | 184 | Complete for the declared open-index queries |
| Retrieval | Citation chains | 2,482 | Fourteen of fifteen seed chains resolved |
| Pooling | Combined records | 2,666 | Before deduplication |
| Pooling | Deduplicated records | 2,431 | Unit for screening |
| Final screening | Retain close | 27 | Confirmed close set |
| Final screening | Retain background | 45 | Thirteen prior records plus 32 author-confirmed records |
| Final screening | Exclude single component | 10 | Relevant component without the tested combination |
| Final screening | Exclude topic | 1,259 | Outside the review question |
| Final screening | Inaccessible | 1,087 | Abstract absent; substantive screening unresolved |
| Final screening | Outside cutoff | 3 | Published after the cutoff |
| Author gate | Completed queue | 89 | All queued decisions recorded |

*Note.* The six final screening classes sum to 2,431. Mark Julius Banasihan is the decision owner for the 89-record queue, with disclosed AI assistance. The 1,087 inaccessible records and authenticated database searching remain separate coverage limits.

**Table 6. Proposal-to-author decision changes.**

| Proposed class | Records | Retain close | Retain background | Exclude topic | Exclude single component |
|---|---:|---:|---:|---:|---:|
| Retain close | 12 | 12 | 0 | 0 | 0 |
| Author attention | 77 | 15 | 32 | 20 | 10 |
| Total author queue | 89 | 27 | 32 | 20 | 10 |

*Note.* The author confirmed all 12 proposed close records. The 77 attention records produced 15 additional close sources and 32 background sources. These decisions close the declared author gate. They do not resolve the inaccessible-record or authenticated-database gates.

#### 4.8.1 Forward-citation risk-sample update

The frozen 102-record forward-citation stratum produced 34 full-text recoveries, 37 abstract recoveries, 26 metadata-only outcomes, three duplicates, and two unavailable outcomes. All 71 records with recovered content received an author-authorized, AI-assisted screening decision under a protocol fixed before those decisions. Thirteen records entered close-source review, 22 entered background review, 11 were excluded as single-component sources, and 25 were excluded as off-topic. Screening decided corpus membership and granted no proposition permission. The later v0.14 proposition review gave five bounded propositions manuscript permission, retained two sources as background-only, and quarantined six because exact text or required support remained unresolved.

Across the 1,087-record recovery population, the population ledger contains 107 retrieval outcomes. All 76 recovered-content records have a screening decision after a v0.14 overlay closed RS-DQ-004 as close on title, metadata, and a verified publisher-PDF route. Its unreadable text layer and unresolved author identity preserve zero proposition permission. The unresolved retrieval class contains 980 records without an outcome, 26 metadata-only records, two unavailable records, and three reconciled duplicates. These categories preserve the 2,431-record denominator without treating access failure or duplicate detection as a topic exclusion.

**Table 7. Residual-risk retrieval and screening checkpoint.**

| Scope | State | Count | Claim boundary |
|---|---|---:|---|
| Forward-citation stratum | Retrieval outcomes recorded | 102 | Complete for the frozen stratum |
| Forward-citation stratum | Recovered content | 71 | Eligible for screening |
| Forward-citation stratum | Screening decisions | 71 | 13 close, 22 background, 11 single-component, 25 topic |
| Forward-citation stratum | Proposition permissions | 5 | Bounded to exact ledger propositions and passage locators |
| Forward-citation stratum | Background-only or quarantined | 8 | Two background-only; six quarantined |
| Direct-query stratum | Screening decisions | 5 of 5 | RS-DQ-004 has zero source-content permission |
| Recovery population | Retrieval outcomes | 107 of 1,087 | 980 retrieval outcomes remain open |
| Recovery population | Recovered-content decisions | 76 of 76 | Screening complete for recovered content |

*Note.* These counts describe the frozen recovery workflow and the v0.14 proposition-review overlay. They supply no close-source prevalence estimate for the 1,087-record population because 980 retrieval outcomes remain open. Proposition permission is narrower than source inclusion and does not establish generalizability.

### 4.9 Evidence boundaries and coding stability

The six event-level propositions produce eighteen categorical findings across the three selected packets. Oko contains six partially supported findings. ZG710 contains one supported, one partially supported, and four unsupported findings. F/A-18C contains one supported, one partially supported, one unsupported, and three indeterminate findings. These counts describe the assessment output. They assign no distance among states and no aggregate control score.

**Figure 6. Evidence boundaries across six event-level practical-control stages.** Each horizontal bar contains the six findings for one case. Partial support records some supporting evidence with a material gap. Indeterminate records insufficient evidence for a decision. Unsupported records evidence against the condition or evidence that the condition was absent. The display makes the public-record constraint visible and supplies no missingness rate, reliability estimate, or case ranking.

**Table A3. Availability of coding-stability evidence.**

| Test condition | Oko, 1983 | Patriot ZG710, 2003 | Patriot F/A-18C, 2003 |
|---|:---:|:---:|:---:|
| A second coding exists | Yes | No | No |
| The same source packet was used | Yes | NA | NA |
| The same evidence rule was used | No | NA | NA |
| Comparable event-level stages | 6 | 0 | 0 |
| Unchanged classifications | 0 | NA | NA |
| Changed classifications | 6 | NA | NA |
| Independent second assessor | No | No | No |
| Reliability claim eligible | No | No | No |

*Note.* Oko's six changes arose when the direct-and-contemporaneous rule was applied to the frozen packet. The comparison records a correction under a changed classification rule. It cannot estimate intra-rater stability or inter-rater reliability. The two Patriot cases have one released coding each.

## 5. Discussion

### 5.1 Formal authority and practical force

Formal authority answers one question: who was permitted to approve, reject, modify, stop, or escalate? Practical control asks whether that permission reached execution in the bounded decision. The path requires usable information, comprehension capacity, intervention rights, a feasible opportunity to act, exercised judgment, and execution propagation. A break at any required stage blocks the wider event-control claim.

The cross-case result shows why the distinction matters. Both Patriot packets support formal authority. Both fail the event-control rule because execution propagation is unsupported, and ZG710 contains three additional unsupported required stages. Oko remains unresolved because retrospective accounts provide partial support without the contemporaneous records required for supported states. A role assignment and practical control therefore produce different documentary conclusions in the same case.

### 5.2 The evidentiary function of an indeterminate state

Public incident records are shaped by classification, litigation, institutional disclosure, journalism, preservation, and time. A missing operator display or inquiry file can block a judgment about comprehension or feasibility. It supplies no evidence that the operator lacked comprehension or opportunity. The indeterminate state preserves that boundary. It also turns the missing record into an explicit result and a recordkeeping requirement. This matters for responsibility: an investigator should not attribute failure to a person when the record cannot establish what information or intervention opportunity the person had.

### 5.3 Consequence of an untested human-control claim

Human-control language can justify deployment, reassure affected people, and assign responsibility after harm. Each use depends on an empirical premise: the designated person had practical power over the decision. When the evidence cannot support that premise, the institution can count an ineffective safeguard as functioning, place responsibility on someone who lacked practical power, or preserve the same failure mechanism in later deployments.

Let `HumanControlClaim(c)` indicate that an institution represents case (c) as human-controlled. The documentary evidence gap is:

\[
EvidenceGap(c)=1[HumanControlClaim(c)=1\land EventControl(c)\neq PASS].
\]

The formula identifies a claim that lacks complete substantiation under the procedure. A failing result records at least one unsupported required condition. An unresolved result records partial or missing evidence without an unsupported required condition. Neither result establishes personal fault, deliberate misrepresentation, legal liability, or an unsafe outcome.

### 5.4 Relationship to prior research

The method operationalizes established constructs at the level of a public evidence packet. Tracking, tracing, epistemic access, causal power, institutional design, and contestability define what control may require [@santoni2018meaningful; @sterz2024quest; @laux2024distrust; @almada2019intervention]. Human-factors research explains why monitoring and challenge can fail [@bainbridge1983ironies; @endsley2017autonomy]. Incident analysis identifies the records needed to reconstruct an event [@ezell2025incident; @macrae2022failure]. Assurance and evidence-chain methods structure the path from proposition to evidence and conclusion [@burr2023ethical; @meng2026scientistone; @moghaddam2026arguments]. Recent close work already supplies AI-incident oversight tiers, runnable decision-chain protocols, versioned assurance cases, and architecture-aware audit evidence [@bahidika2026accountability; @laposta2026conflict; @niazi2026rights; @surve2026cedar].

The contribution lies in what the connected procedure lets an investigator decide. The investigator can distinguish assigned authority from event-level control, evidence of failure from missing evidence, a linked execution change from an outcome claim, and a current conclusion from the earlier version it corrected. Within the reviewed source set, no prior source supplies that complete reconstruction-and-audit path. Open retrieval and authenticated-database gates bound this closest-work finding.

### 5.5 Use for current AI governance

Contemporary systems can share the mechanisms tested here even when their architecture differs. Agentic software may compress review time, distribute actions across tools, obscure intermediate system state, or leave a reviewer with nominal stop authority. Dhanorkar, Passi, and Vorvoreanu show that developers already perform several forms of agent oversight work [@dhanorkar2026practice]. Alhalangy and Lee, Yoon, and Lee show how escalation and record duties can enter prospective governance design [@alhalangy2026traceable; @lee2026governance]. The proposed timing margin and execution-propagation test translate the historical method into measurable requirements for contemporary logs. A new protocol must apply them to a present learned or agentic system before the paper can claim transfer.

### 5.6 Ethical burden of proof

Human-control language can distribute responsibility, reassure affected people, and justify deployment. Those functions create an ethical burden of proof. An institution should preserve evidence capable of testing the practical-control chain when it represents a consequential system as human-controlled. The burden concerns the institution's claim and records. It presumes no individual fault.

This position follows from the risk of nominal oversight. A role assignment can place responsibility on a person who lacks information, capacity, opportunity, or causal power [@green2022flaws; @sterz2024quest; @douer2020responsibility]. Institutional design should anticipate human fallibility and incentives [@laux2024distrust]. The proposed record set lets affected people, investigators, and oversight bodies examine whether responsibility was attached to practical authority. It guarantees no safe or just outcome.

## 6. Limitations

The design has several limits. The three strata were defined around the headline contrasts, and screening stopped after five candidates. The selected set demonstrates the procedure under those anticipated conditions. It estimates no prevalence and provides no independent classification test. Two cases concern one system family and operating period. Oko and Patriot differ materially from present learned systems.

The evidence is retrospective and public. Classified material, internal logs, complete displays, and some inquiry records were unavailable. Some cited content remains remote-only. Oko relies on later participant accounts and lacks a located contemporaneous command record. Source agreement can reflect shared dependence on an earlier account. Packet hashes prove preservation of stored bytes and do not prove source truth.

One assessor designed and applied the method. The study supplies no inter-rater reliability, construct-validity estimate, causal effect, safety effect, legal-sufficiency judgment, or outcome comparison. Artifact tests detect internal inconsistency and prespecified corruption. They do not validate historical interpretation.

The formal search used open indexes and official source pages. Author review closed the 89-record decision queue, the 71-record recovered forward-citation queue, the 13-source proposition gate, and the fifth direct-query screening decision. Another 980 records lack a retrieval outcome, and authenticated Scopus or Web of Science, IEEE Xplore, ACM Digital Library, PhilPapers, and HeinOnline or an equivalent legal index remain open. Five forward sources have one bounded proposition permission each, two remain background-only, and six are quarantined. RS-DQ-004 has zero source-content permission. The contribution language is therefore bounded to the declared search and reviewed source set.

## 7. Institutional implications

An assurance team, regulator, deployer, or incident investigator can use the practical-control chain as a proposed evidence request. The classification determines what the institution may say about the bounded decision.

| Result | Evidentiary meaning | Institutional consequence |
|---|---|---|
| Pass | Every required event-level stage is supported | The available record supports the bounded practical-control claim |
| Fail | At least one required event-level stage is unsupported | The institution should identify the failed condition and avoid relying on practical control as a safeguard for that decision |
| Unresolved | No required stage is unsupported, and at least one is partial or indeterminate | The institution lacks enough evidence to substantiate the complete practical-control claim |
| Outside scope | A separately justified case boundary excludes a nonrequired proposition | The excluded proposition cannot support a conclusion beyond that boundary |

Before relying on a human-control claim, the reviewer should ask for:

1. the exact information and system output shown to the named person;
2. timestamps connecting output, review, action, and irreversible commitment;
3. model or system version, operating state, uncertainty, and known limits;
4. independent information available for challenge;
5. role delegation and tested approve, reject, modify, stop, and escalation rights;
6. staffing, workload, latency, access, and institutional conditions that affected feasibility;
7. the contemporaneous decision, challenge, or escalation record;
8. evidence that the intervention propagated into execution;
9. appeal, correction, repair, and reform records when the claim extends beyond event-level control;
10. missing, inaccessible, or deleted records and the retention rule that governed them.

This proposed request converts a general assurance statement into inspectable propositions. It supplies no legal-compliance, safety, fairness, or accountability-outcome finding by itself.

## 8. Conclusion

An institution substantiates practical human control by showing that the designated person received usable information, had comprehension capacity and intervention authority, could act in time, exercised judgment, and propagated a change into execution. A named reviewer establishes assigned responsibility alone. The additional evidence matters when human-control language justifies deployment, assigns responsibility, or reassures people exposed to a consequential system.

The frozen method converted that broad institutional claim into six testable propositions. Across three purposively selected historical packets, no case passed the complete event-control rule. Oko remained unresolved after six classifications were narrowed to partially supported. Both Patriot cases retained supported formal authority and failed the wider event-control rule. These results demonstrate the documentary distinction; they estimate no population frequency.

The correction history shows why research provenance belongs inside the method. A released conclusion was narrowed, the original record remained visible, and every dependent claim could be reconsidered. Institutions need the same discipline when a human-control claim supports deployment or responsibility allocation.

The result is a method demonstration. Independent assessors, varied case families, contemporary system traces, and prospective decision studies are needed before the method can support reliability, validity, or institutional-effect claims.

## Version relationship and integrity status

The v0.14.0 preprint was archived on Zenodo under the version DOI [10.5281/zenodo.21926005](https://doi.org/10.5281/zenodo.21926005). Version 0.15.0 added venue metadata and submission disclosures. This v0.16.0 working paper rebuilds the explanation and formalizes the event-control decision rule. It preserves the released packet states and search counts, while deriving the previously unstated case-level results: Oko is unresolved, both Patriot cases fail, and no selected case passes. The repository's version history remains the authority for changes to data, claims, code, figures, and audit results.

The v0.14.0 integrity audit mapped 32 material claims to evidence, applied 33 controlled mutations, and detected all 33 corrupted conditions. The v0.16.0 audit extends those controls to the formal rule, its derived case results, the proposed timing measure, and manuscript terminology. These tests ask whether declared repository controls respond to seeded or detectable inconsistencies. They do not establish the truth of every historical claim, independent assessor agreement, population validity, or transfer to present AI systems.

## Data and materials availability

The repository, versioned releases, packets, assessments, figure data, audit outputs, search files, manuscript tables, and release manifests are available at [github.com/mj3b/trust-autonomy-evidence](https://github.com/mj3b/trust-autonomy-evidence). The v0.6.0 evidence archive has the version DOI [10.5281/zenodo.21865007](https://doi.org/10.5281/zenodo.21865007). The repository's all-versions DOI is [10.5281/zenodo.21841127](https://doi.org/10.5281/zenodo.21841127). The v0.14.0 preprint, including the proposition ledger, corrected source identities, 32-claim audit, 33 mutation controls, LaTeX source, and review PDF, has the version DOI [10.5281/zenodo.21926005](https://doi.org/10.5281/zenodo.21926005).

## Ethics and publication authority

The study uses public records and contains no participant recruitment, intervention, or direct interaction with living individuals. The repository preserves eligible public-domain and openly licensed material, cites proprietary sources through metadata and limited paraphrase, and excludes personal, confidential, institutionally restricted, and security-sensitive material under the frozen protocol. No institutional determination about human-subjects review has been obtained. The author must check Harvard and venue requirements before submission and must not describe the study as exempt without the applicable determination.

**Author note.** Node & Norm is the author's independent research initiative. Mark Julius Banasihan is an ALB candidate in Extension Studies at Harvard University. This research was conducted independently through Node & Norm, with no Harvard University sponsorship, supervision, endorsement, or representation.

## Author contributions

Mark Julius Banasihan: Conceptualization, methodology, investigation, data curation, software, validation, visualization, writing of the original draft, review and editing, project administration, and accountable authorship.

## AI-assistance disclosure

Generative AI tools assisted with literature discovery, metadata organization, preliminary screening proposals, decision-ledger preparation, draft development, code generation, figure and consistency checks, and language revision. AI outputs did not approve claims or evidence states. Mark Julius Banasihan defined the research question and protocols, reviewed and approved the 89 screening decisions, approved the evidence and assessment decisions, verified the sources used for claims, controlled the repository releases, and remains responsible for the analysis, interpretations, errors, and submitted text. Claim-level evidence mapping, evidence-fitness checks, controlled mutations, reference verification, and method-code alignment checks were applied to the released research artifacts. These controls test declared consistency and error response; they do not replace independent peer review.

## Conflicts of Interest

The author declares no conflicts of interest.
