# From Formal Authority to Practical Human Control

## A traceable method for reconstructing human control in automated decisions

> **Reader edition.** This file converts the manuscript's Pandoc citation keys into clickable author-year citations. The [auditable source](manuscript.md) preserves the citation keys, and [references.bib](references.bib) preserves the checked metadata.

**Author:** Mark Julius Banasihan  
**ORCID:** [0009-0001-8121-2878](https://orcid.org/0009-0001-8121-2878)  
**Affiliation:** Independent Researcher, Node & Norm, United States  
**Student status:** ALB candidate in Extension Studies, Harvard University  
**Correspondence:** institutional and personal addresses recorded in the venue package  
**Status:** Proposition-reviewed Preprints.org working manuscript, v0.15.0 candidate

This research was conducted independently through Node & Norm. It was not sponsored, supervised, or endorsed by Harvard University and does not represent the University's views.

## Abstract

Institutions often treat a named reviewer or approval step as evidence that an automated system remains under human control. That inference can fail when the person lacks timely information, comprehension, authority, an opportunity to challenge the system, or the ability to affect the outcome. This paper develops a frozen, evidence-traceable procedure for representing formal authority, practical control, and unresolved evidence in bounded public incident records. Before case screening, the protocol fixed the evidence cutoff, candidate collections, eligibility rules, screening order, selection strata, and missing-data treatment. Three versioned historical case packets record claim-level provenance, categorical evidence states, and a chain from information access through effect. A frozen reanalysis changed six Oko pre-action stages from supported to partially supported. The current assessments record partial support across those Oko stages, supported authority with unsupported practical conditions in Patriot ZG710, and supported authority with unresolved conditions in the Patriot F/A-18C case. An open-index search produced 2,431 deduplicated records. Author screening and forward-citation review yielded five bounded source propositions for manuscript use, two background-only sources, and six quarantined sources. The contribution is a governance-specific integration with a visible correction path. Institutions claiming human control bear an ethical burden to preserve evidence of practical force because unsupported attribution can obscure responsibility and exposure to harm. Three retrospective, single-assessor cases supply no population estimate, causal validation, independent-reliability result, or transfer claim for current learned systems.

**Keywords:** human oversight; meaningful human control; AI governance; incident reconstruction; assurance

## Resolved evidence decision

`PAPER-BLOCKER-01` identified a mismatch between Oko's released v0.3 supported states and the protocol's direct-and-contemporaneous evidence rule. The [v0.6 adjudication protocol](../protocols/oko-evidence-adjudication-v0.6.0.md) was frozen before reassessment. The resulting [change ledger](../assessments/v0.6.0/oko-change-ledger.json) records six transitions to partially supported and preserves v0.3.0 as release history. Missing contemporaneous records remain a limitation.

## 1. Introduction

### 1.1 The institutional problem

An approval step proves that an institution assigned a role. It does not show that the person received the relevant information, understood the system's limits, could challenge the proposed action in time, exercised that authority, or changed the outcome. A human-control claim therefore contains several empirical propositions that a signature or job title cannot establish by itself.

Human-factors research explains the mechanism. Automation can leave people responsible for rare or abnormal conditions after routine system operation has reduced their preparation for those conditions ([Bainbridge, 1983](https://doi.org/10.1016/0005-1098(83)90046-8)). Situation awareness and intervention performance depend on what the person can perceive, understand, and project under the operating conditions ([Endsley, 2017](https://doi.org/10.1177/0018720816681350)). Trust affects reliance through the interaction of the person, system, task, and context ([Lee & See, 2004](https://doi.org/10.1518/hfes.46.1.50_30392)). Formal authority can remain intact as these operational conditions deteriorate.

The same problem appears in policy. Green finds that government rules often require human oversight without establishing that the designated people can perform the intended review ([Green, 2022](https://doi.org/10.1016/j.clsr.2022.105681)). Zhu et al. separate AI operative agency from human evaluative agency and identify verification, contestation, and substitution as oversight mechanisms ([Zhu et al., 2026](https://doi.org/10.1007/s43681-026-01147-7)). These accounts direct attention to a documentary question: what evidence would justify reliance on an institutional claim that human authority had practical force in one consequential decision?

### 1.2 Research gap

Five research streams answer parts of that question. Meaningful-human-control scholarship defines moral, design, and institutional conditions for control ([Santoni de Sio & van den Hoven, 2018](https://doi.org/10.3389/frobt.2018.00015); [Siebert et al., 2023](https://doi.org/10.1007/s43681-022-00167-3); [Davidovic, 2023](https://doi.org/10.3389/fdata.2022.1017677); [Calvert, 2025](https://doi.org/10.1007/s11948-025-00554-z)). Human-factors research explains why monitoring, comprehension, and timely intervention can fail ([Bainbridge, 1983](https://doi.org/10.1016/0005-1098(83)90046-8); [Lee & See, 2004](https://doi.org/10.1518/hfes.46.1.50_30392); [Endsley, 2017](https://doi.org/10.1177/0018720816681350)). Oversight research identifies causal power, epistemic access, preparedness, intention, human learning, and institutional design as conditions for effectiveness ([Sterz et al., 2024](https://doi.org/10.1145/3630106.3659051); [Te'eni et al., 2025](https://doi.org/10.1007/s00146-025-02401-y); [Laux, 2024](https://doi.org/10.1007/s00146-023-01777-z); [Baum & Laux, 2026](https://doi.org/10.48550/arXiv.2603.19213)). Incident research specifies causal factors, reporting structures, and information needs ([McGregor, 2021](https://doi.org/10.1609/aaai.v35i17.17817); [Macrae, 2022](https://doi.org/10.1111/risa.13850); [Ezell et al., 2025](https://doi.org/10.1609/aies.v8i1.36596); [Paeth et al., 2025](https://doi.org/10.1609/aaai.v39i28.35163); [Wei & Heim, 2026](https://doi.org/10.1609/aaai.v40i44.41139)). Assurance and traceability research connects claims to evidence, assumptions, uncertainty, validation rules, and provenance ([Burr & Leslie, 2023](https://doi.org/10.1007/s43681-022-00178-0); [Paterson et al., 2025](https://doi.org/10.1016/j.ress.2025.111311); [Meng et al., 2026](https://doi.org/10.48550/arXiv.2605.26340); [Moghaddam, 2026](https://doi.org/10.48550/arXiv.2604.04103)).

The closest prior work sharply limits the present claim. Sterz et al. define effective oversight through sufficient causal power, suitable epistemic access, self-control, and fitting intentions ([Sterz et al., 2024](https://doi.org/10.1145/3630106.3659051)). Verdiesen, Santoni de Sio, and Dignum place oversight across technical, sociotechnical, and governance layers ([Verdiesen et al., 2021](https://doi.org/10.1007/s11023-020-09532-9)). Laux treats overseer competence and incentives as institutional-design problems ([Laux, 2024](https://doi.org/10.1007/s00146-023-01777-z)). Almada connects human intervention to the information and system conditions needed for contestability ([Almada, 2019](https://doi.org/10.1145/3322640.3326699)). Douer and Meyer show that causal responsibility can diverge from assigned human functions ([Douer & Meyer, 2020](https://doi.org/10.1109/TASE.2020.2965466)).

Prior methods also cover reconstruction and evidence. Dekker reconstructs human contributions inside an event sequence while controlling hindsight ([Dekker, 2002](https://doi.org/10.1016/S0022-4375(02)00032-4)). Pittaras and McGregor classify possible failure causes from incomplete open-source AI incidents ([Pittaras & McGregor, 2023](https://ceur-ws.org/Vol-3381/17.pdf)). ScientistOne supplies claim-level evidence chains and post-hoc integrity checks ([Meng et al., 2026](https://doi.org/10.48550/arXiv.2605.26340)). Moghaddam proposes evidence-linked formal argument graphs with deterministic validation and provenance ([Moghaddam, 2026](https://doi.org/10.48550/arXiv.2604.04103)). Alhalangy joins selective human review to a structured case-level audit trail in a synthetic institutional study ([Alhalangy, 2026](https://doi.org/10.3390/info17070694)). Recent close sources go further: Bahidika applies oversight tiers to public AI Incident Database records ([Bahidika, 2026](https://doi.org/10.14569/IJACSA.2026.0170502)), LaPosta publishes a runnable decision-chain protocol ([LaPosta, 2026](https://doi.org/10.1609/aaaiss.v8i1.42543)), Niazi, Hassani, and Lee define a versioned assurance case with a practical-override trace ([Niazi et al., 2026](https://doi.org/10.3390/automation7030096)), and Surve, Shabtai, and Elovici declare an audit-evidence method with a retrospective Cruise application ([Surve et al., 2026](https://doi.org/10.48550/arXiv.2606.21276)).

The remaining contribution is one governance-specific integration: protocol fixation before case screening, a visible selection and stopping path, versioned public evidence packets, categorical missingness, a chain from information access through effect, claim-specific evidence fitness, conclusion dependency closure, versioned correction, and executable artifact checks. The formal search records 2,431 deduplicated records and preserves the limits created by inaccessible abstracts, one unresolved citation seed, and unavailable authenticated databases. The paper therefore states a bounded integration claim. Universal originality remains outside the evidence.

### 1.3 Research question and contribution

> How can a frozen, evidence-traceable assessment procedure represent formal human authority, practical human control, and unresolved evidence in a bounded public incident record?

The paper proposes a documentary assessment procedure. It defines a bounded action sequence, fixes the case-selection and missing-data rules, assembles a versioned evidence packet, assigns provenance to material statements, and evaluates six pre-action conditions: access, comprehension, authority, feasible challenge, exercised challenge, and effect. An explicit indeterminate state prevents missing records from becoming negative factual findings. A correction ledger preserves earlier outputs when a later adjudication changes a state.

The three cases demonstrate that procedure under contrastive evidence conditions. They do not test prevalence, classification accuracy, independent reliability, causal effects, or transfer to current learned systems. The institutional output is a proposed record set that a reviewer would need before relying on a practical-control claim. The ethical proposition is narrower: an institution that represents a decision as human-controlled should preserve evidence capable of testing whether the assigned authority had practical force.

### 1.4 Paper structure

Section 2 locates the procedure in meaningful-human-control, human-factors, oversight, incident-analysis, reconstruction, and assurance research. Section 3 defines the frozen method, artifact controls, literature search, and transfer boundary. Section 4 reports the released assessment and search results. Sections 5 through 7 separate interpretation, limitations, and proposed institutional record requirements.

## 2. Related work

### 2.1 Meaningful human control

Santoni de Sio and van den Hoven define meaningful human control through tracking and tracing. System behavior must respond to relevant human reasons, and human actors must be able to understand their role and bear responsibility ([Santoni de Sio & van den Hoven, 2018](https://doi.org/10.3389/frobt.2018.00015)). This account makes human presence insufficient because control depends on the relation among system behavior, human reasons, and identifiable responsibility.

Later work moves the concept toward institutional and engineering use. Siebert et al. propose actionable properties that align ability, authority, and responsibility ([Siebert et al., 2023](https://doi.org/10.1007/s43681-022-00167-3)). Davidovic argues that designers must first state the purpose served by human control ([Davidovic, 2023](https://doi.org/10.3389/fdata.2022.1017677)). Calvert places proximal intervention inside a wider system of distal control across design, deployment, and governance ([Calvert, 2025](https://doi.org/10.1007/s11948-025-00554-z)). Verdiesen, Santoni de Sio, and Dignum divide control across technical, sociotechnical, and governance layers ([Verdiesen et al., 2021](https://doi.org/10.1007/s11023-020-09532-9)). Tsamados, Floridi, and Taddeo compare supervisory control with human-machine teaming for foundation-model systems ([Tsamados et al., 2025](https://doi.org/10.1007/s43681-024-00489-4)). Zhu et al. frame oversight as human evaluative agency expressed through verification, steering, contestation, and substitution ([Zhu et al., 2026](https://doi.org/10.1007/s43681-026-01147-7)).

The present paper uses these sources to define the proposition being assessed. It does not offer a new philosophical account of meaningful human control.

### 2.2 Human oversight and the automation problem

Bainbridge shows how automation transfers rare, abnormal, and difficult work to people after routine operation has weakened the practice needed for that work ([Bainbridge, 1983](https://doi.org/10.1016/0005-1098(83)90046-8)). Endsley connects autonomous-system performance to situation awareness, monitoring, workload, trust, and out-of-the-loop degradation ([Endsley, 2017](https://doi.org/10.1177/0018720816681350)). Lee and See model appropriate reliance as a relation among the person, automation, task, and environment ([Lee & See, 2004](https://doi.org/10.1518/hfes.46.1.50_30392)). Together, these mechanisms explain how nominal oversight can lose practical force.

Human response to algorithmic advice is conditional. Alon-Barkat and Busuioc find both automation bias and selective adherence across experimental public-sector decisions ([Alon-Barkat & Busuioc, 2023](https://doi.org/10.1093/jopart/muac007)). Langer, Baum, and Schlicker separate the ability to detect error from a person's response tendency ([Langer et al., 2024](https://doi.org/10.1007/s11023-024-09701-0)). Haselager et al. propose a counterargument prompt that supports questioning of medical decision-support advice ([Haselager et al., 2023](https://doi.org/10.1017/S0963180122000718)). Dhanorkar, Passi, and Vorvoreanu identify a priori control, co-planning, real-time monitoring, and post hoc review in interviews with 17 experienced developers who use software agents ([Dhanorkar et al., 2026](https://doi.org/10.1145/3805689.3812402)).

Two retained empirical sources expose different gaps between assigned oversight and practical effect. In a secondary analysis of 99 Tesla-user interviews, Suryana et al. report that perceived safety sometimes coexisted with failures to track driver reasons; takeover readiness and prior reliable experience also shaped perception ([Suryana et al., 2024](https://doi.org/10.48550/arXiv.2402.08080)). The study concerns reported perception in partial driving automation and does not observe incident-control outcomes. In a 28-participant sandbox study, Li et al. report task-completion rates of 83.3 percent under direct manipulation and 61.9 percent under text guidance; delayed responses and difficult error correction also made intervention effects harder for participants to assess ([Li et al., 2025](https://doi.org/10.1109/CAI64502.2025.00121)). The sample, tasks, model, and single qualitative coder limit transfer. Together, the studies support a mechanism claim: perceived control and formal feedback access can remain separate from demonstrated intervention effect.

Effectiveness also depends on causal and institutional conditions. Sterz et al. identify causal power, epistemic access, self-control, and fitting intentions ([Sterz et al., 2024](https://doi.org/10.1145/3630106.3659051)). Baum and Laux distinguish constitutive human participation from corrective oversight and require genuine preparedness and capacity for the latter ([Baum & Laux, 2026](https://doi.org/10.48550/arXiv.2603.19213)). Te'eni, Yahav, and Schwartz treat continual human learning as a condition for stable and adaptive control ([Te'eni et al., 2025](https://doi.org/10.1007/s00146-025-02401-y)). Laux proposes institutional safeguards that anticipate fallible competence and incentives ([Laux, 2024](https://doi.org/10.1007/s00146-023-01777-z)). Green's policy analysis reaches a related implication: oversight rules need evidence that people can perform the assigned review ([Green, 2022](https://doi.org/10.1016/j.clsr.2022.105681)). The present method converts these constructs into documentary questions about information, comprehension, authority, feasibility, action, and effect.

Design and governance research also show why those conditions depend on system architecture. Van der Waa et al. use human-agent team patterns to make allocation timing, sufficient understanding, halt or resume capability, and handover conditions explicit ([van der Waa et al., 2020](https://doi.org/10.1007/978-3-030-49183-3_16)). Kolt argues that monitoring and detailed records can reduce information asymmetry and support intervention, while speed, opacity, and irreversible action can make conventional oversight ineffective ([Kolt, 2025](https://arxiv.org/abs/2501.07913)). The first source offers conceptual design patterns and the second offers legal analysis. Neither supplies a field estimate of effective control.

### 2.3 AI incident analysis and missing records

The AI Incident Database was created to provide a shared record of real-world failures and support learning across incidents ([McGregor, 2021](https://doi.org/10.1609/aaai.v35i17.17817)). Its reports remain public-source records with changing coverage and varying detail. Pittaras and McGregor respond to that constraint through expert classification of goals, technologies, and possible technical failure causes ([Pittaras & McGregor, 2023](https://ceur-ws.org/Vol-3381/17.pdf)). Paeth et al. show that incident reports contain structural ambiguity and unavoidable epistemic uncertainty ([Paeth et al., 2025](https://doi.org/10.1609/aaai.v39i28.35163)). These limits support an explicit indeterminate state.

Macrae demonstrates that public investigative reports can support systematic analysis of sociotechnical failure in an autonomous system ([Macrae, 2022](https://doi.org/10.1111/risa.13850)). Ezell, Roberts-Gaal, and Chan specify system, contextual, cognitive, access, tool, log, and documentation information needed to investigate AI-agent incidents ([Ezell et al., 2025](https://doi.org/10.1609/aies.v8i1.36596)). Wei and Heim locate those information needs inside institutional reporting systems and post-reporting action ([Wei & Heim, 2026](https://doi.org/10.1609/aaai.v40i44.41139)). The present method applies a narrower question to each packet: which records support a claim that assigned human authority could affect the bounded action?

### 2.4 Reconstruction, forensics, and assurance

Dekker treats accident reconstruction as recovery of what people could know and why their actions made sense inside the unfolding event ([Dekker, 2002](https://doi.org/10.1016/S0022-4375(02)00032-4)). This approach guards against hindsight and unsupported counterfactual blame. McDermid identifies time, knowledge independent of the automated system, and practiced skill as conditions for effective intervention ([McDermid, 2019](https://www.york.ac.uk/assuring-autonomy/news/blog/human-control-ai-autonomy/)). These works closely anticipate the procedure's reconstruction logic and feasible-challenge stage.

Reconstruction output also depends on the analytic frame and the available record. Zhang, Jing, and Sun assigned separate teams to apply HFACS, AcciMap, and STAMP to the same official report of the Tianjin Port fire and explosion ([Zhang et al., 2018](https://doi.org/10.1007/s11668-018-0534-1)). The methods produced different factor sets, and the authors state that missing report detail can hide material factors. One accident, analyst reconciliation, and dependence on one official report prevent treating the comparison as a validation against event truth. The study supports the narrower rule used here: method choice and source completeness must remain visible when a public-record reconstruction is interpreted.

Argument-based assurance asks whether evidence justifies a stated claim under explicit assumptions and uncertainty. Burr and Leslie extend that structure to ethical and social claims ([Burr & Leslie, 2023](https://doi.org/10.1007/s43681-022-00178-0)). AMLAS applies it to machine-learning safety across development and deployment ([Paterson et al., 2025](https://doi.org/10.1016/j.ress.2025.111311)). Lam et al. define scope, criteria, evidence, and reporting for assurance audits of algorithmic systems ([Lam et al., 2024](https://doi.org/10.1145/3630106.3658957)). The present procedure borrows this claim-evidence discipline for retrospective assessment. It issues no safety case for Oko or Patriot.

Recent forensic work provides closer technical neighbors. Leung et al. reconstruct changing AI system state for insurance claims ([Leung et al., 2026](https://arxiv.org/abs/2606.03777)). Ledjaki et al. preserve and replay prompt-level evidence through a chain-of-custody design ([Ledjaki et al., 2026](https://doi.org/10.1145/3774905.3795469)). These papers constrain the contribution to the specific combination of practical human control, public case selection, categorical missingness, and executable repository checks.

ScientistOne supplies a closer architecture for research verifiability. Its Chain-of-Evidence framework requires claims to trace to evidence, and its post-hoc audit checks scores, specification violations, references, and method-code alignment ([Meng et al., 2026](https://doi.org/10.48550/arXiv.2605.26340)). Moghaddam's argument graphs treat each AI-assisted step as a claim that must pass evidence and reasoning constraints before entering an official record ([Moghaddam, 2026](https://doi.org/10.48550/arXiv.2604.04103)). Alhalangy integrates prediction, explanation, selective review, and an audit trail into a synthetic institutional decision pathway ([Alhalangy, 2026](https://doi.org/10.3390/info17070694)). Lee, Yoon, and Lee position oversight authority, record duties, and auditability in the pre-design governance decision ([Lee et al., 2026](https://doi.org/10.3390/systems14070849)). These sources establish prior work for traceability, evidence-linked argument, and prospective record design. The present adaptation applies five evidence-fitness dimensions and dependency closure to retrospective public-case claims. Independent review has yet to test those judgments.

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

**Table 1. Assessment-state decision rules.**

| State | Code | Decision rule |
|---|:---:|---|
| Supported | S | Direct, contemporaneous evidence satisfies the stage definition. |
| Partially supported | P | Some required elements are present and a material gap remains. |
| Unsupported | U | Available evidence contradicts the stage or shows that the condition was absent. |
| Indeterminate | I | The packet lacks enough evidence to decide. |
| Outside scope | O | The stage does not apply within the declared case boundary, with a written reason. |

*Note.* A missing record produces an indeterminate state unless the protocol or case design establishes that the record should exist. The states are categorical. No numeric distance or aggregate score is assigned.

### 3.8 Missing evidence and inference

Missing public evidence produces an indeterminate state unless the packet establishes that a required record should exist and eligible evidence shows the condition was absent. This rule blocks a common inference error in retrospective work: converting an unavailable log, display, inquiry, or internal record into a finding that the underlying condition failed. The report separates what a source states, what a preserved record directly shows, what the assessor infers, and what remains unresolved.

### 3.9 Artifact and consistency controls

Repository checks validate schemas, packet hashes, selection invariants, cross-case interactions, derived figure data, release manifests, and prespecified mutations. These checks reproduce declared transformations and detect internal contradictions. They do not reproduce the assessor's historical judgments.

The v0.6 Chain-of-Evidence adaptation maps each material claim to exact locators, records a human support attestation, and tests directness, contemporaneity, independence, completeness, and publication authority. A dependency graph controls which claims may enter a conclusion. The integrity audit adapts ScientistOne's score verification, specification-violation, reference-verification, and method-code-alignment checks, then adds evidence-fitness and dependency-closure checks. A separate literature-support register maps material manuscript sentences to checked references.

### 3.10 Formal literature search

A v0.7 protocol fixed eight query families, inclusion rules, screening states, deduplication, fifteen citation seeds, and a contribution rejection test before retrieval. Semantic Scholar served as the controlling reproducible index. Every direct-search token and every returned citation page were retrieved. Crossref checked DOI metadata, while OpenAlex compared seed coverage. Publisher, proceedings, preprint, and institutional pages were used to verify the close set.

AI assistance assigned preliminary triage proposals. Mark Julius Banasihan reviewed the initial 89-record queue and remains accountable for every recorded decision. A separate frozen protocol governed AI-assisted screening of 71 recovered forward citations under his authorization. A v0.14 proposition protocol then required a stable locator, exact passage, bounded proposition, five-dimension fitness decision, limitation, reversal condition, and permission state for each of the 13 close sources. Five received bounded manuscript permission, two remain background-only, and six are quarantined. A direct-query overlay closed the fifth screening decision while preserving zero source-content permission. An abstract-only record supports only a bounded description of the source's declared purpose or model. A wider substantive claim requires checked full text and a stable proposition locator. Authenticated Scopus or Web of Science access and several disciplinary interfaces remain open.

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

**Table 2. Practical-control states across three public cases.**

| Stage | Oko, 1983 | Patriot ZG710, 2003 | Patriot F/A-18C, 2003 |
|---|:---:|:---:|:---:|
| Access before action | P | P | P |
| Comprehension | P | U | I |
| Formal authority | P | S | S |
| Feasible challenge | P | U | I |
| Exercised challenge | P | U | I |
| Protective effect | P | U | U |
| Correction | O | O | O |
| Repair | O | U | U |
| Institutional reform | P | S | S |

*Note.* S = supported; P = partially supported; U = unsupported; I = indeterminate; O = outside scope. The table reports 27 item-level findings. It supplies no frequency, causal, or population estimate.

### 4.6 Decision paths and trust-evidence states

Figure 3 traces each bounded sequence from machine output through human and institutional action. Its relative spacing reflects the absence of a defensible common time scale. Figure 4 reports the twelve trust-evidence propositions by case. The categorical states are kept separate because the protocol defines no validated aggregation rule.

**Figure 3. Decision paths from machine output through institutional response.** Each row preserves the order of documented machine, human, and institutional actions. Horizontal spacing separates stages for reading and does not encode a common elapsed-time scale. The figure exposes where intervention occurred, failed, or remains unresolved. It supplies no causal-effect estimate.

**Figure 4. Trust-evidence states across three public cases.** The matrix reports twelve proposition-level evidence states for each packet. Supported, partially supported, unsupported, indeterminate, and outside-scope states remain categorical. The display shows where the record is strong, adverse, incomplete, or irrelevant. It supplies no combined trust score or case ranking.

### 4.7 Integrity and correction results

The v0.14 integrity audit maps 32 material repository claims. The versioned Oko correction closes the prior protocol-consistency and dependency failure within the declared procedure. The completed 89-record and 71-record ledgers make their screening counts eligible within bounded workflow scopes. The 13-source proposition ledger makes five source propositions eligible only at their recorded scope and locators. Independent validity, 980 retrieval outcomes, the 177-record backward-reference stratum, and authenticated-database coverage remain outside the completed evidence base. Thirty-three negative controls confirm that the audit detects prespecified corruptions. Six Oko adjudication mutations test state, evidence, and dependency records. These results show internal contract behavior. They establish no external validity.

**Figure A1. Mutation-response matrix.** Each prespecified corruption is paired with the control expected to detect it. A detected mutation shows that the committed check responded to that injected error. It does not estimate sensitivity to unknown mistakes.

**Figure A2. Reproducibility lineage.** The upper lane traces the research record from frozen collections to the release archive. The lower lane traces the figure pipeline from plot inputs to integrity checking. The labeled connector runs from Assessments to Plot inputs because recorded assessment states become inputs to the figure builder. The diagram shows which transformations can be repeated from preserved artifacts and where human judgment remains necessary. Artifact lineage supplies no independent reproduction of the research conclusions.

**Figure A3. Claim-evidence integrity.** The matrix shows the five evidence gates and conclusion eligibility for twenty mapped claims. Independent validity and search-coverage limits remain visible. It assigns no numeric score.

**Figure A4. Versioned correction of the Oko assessment.** All six pre-action stages move from supported in v0.3.0 to partially supported in v0.6.0. The packet remained fixed. The frozen evidence rule required the correction, and the change supplies no new historical evidence.

**Table A1. Oko correction record.**

| Stage | v0.3.0 | v0.6.0 | Material gap recorded in v0.6.0 |
|---|:---:|:---:|---|
| Access before action | S | P | No contemporaneous delivery, interface, or command record was located. |
| Comprehension | S | P | No contemporaneous reasoning, review, or explanation record was located. |
| Formal authority | S | P | No contemporaneous delegation or command-procedure record was located. |
| Feasible challenge | S | P | No contemporaneous timing or operating record was located. |
| Exercised challenge | S | P | No contemporaneous decision or communication log was located. |
| Protective effect | S | P | No contemporaneous linked action, stop, or escalation record was located. |

*Note.* The v0.6.0 adjudication applied a protocol frozen before reassessment and admitted no new historical source.

### 4.8 Formal search result

The eight Semantic Scholar queries returned 184 records. Fourteen resolved seed chains returned 2,482 reference and citation records. L12 returned `404` for both chain endpoints. The combined pool contains 2,431 deduplicated records. The frozen machine pass proposed 12 close records and placed 77 records in an attention queue. Author review confirmed all 12 proposed close records. The 77 attention records produced 15 additional close sources, 32 background sources, 20 topic exclusions, and 10 single-component exclusions. The final full-pool state therefore contains 27 close records, 45 background records, 1,259 topic exclusions, 10 single-component exclusions, 1,087 inaccessible records, and three records outside the publication cutoff.

Crossref resolved 22 of 25 DOI-bearing retained proposals. OpenAlex resolved thirteen of fifteen citation seeds, including an L12 record with zero indexed links. Different reference and citation counts across indexes show that chain coverage depends on the selected index. The completed author queue supports a declared closest-work analysis and a bounded integration statement. The inaccessible records and open database searches prevent a universal originality or systematic-coverage claim.

**Figure 5. Formal search retrieval and final screening state.** The left panel traces 184 direct-query records and 2,482 citation-chain records through pooling and deduplication. The right panel reports the six final screening classes on a logarithmic count axis. Blue points identify the 27 close and 45 background records. The annotation records closure of all 89 author decisions. The 1,087 inaccessible records remain a separate coverage limit.

**Table 3. Formal search and final screening state.**

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

**Table 4. Proposal-to-author decision changes.**

| Proposed class | Records | Retain close | Retain background | Exclude topic | Exclude single component |
|---|---:|---:|---:|---:|---:|
| Retain close | 12 | 12 | 0 | 0 | 0 |
| Author attention | 77 | 15 | 32 | 20 | 10 |
| Total author queue | 89 | 27 | 32 | 20 | 10 |

*Note.* The author confirmed all 12 proposed close records. The 77 attention records produced 15 additional close sources and 32 background sources. These decisions close the declared author gate. They do not resolve the inaccessible-record or authenticated-database gates.

#### 4.8.1 Forward-citation risk-sample update

The frozen 102-record forward-citation stratum produced 34 full-text recoveries, 37 abstract recoveries, 26 metadata-only outcomes, three duplicates, and two unavailable outcomes. All 71 records with recovered content received an author-authorized, AI-assisted screening decision under a protocol fixed before those decisions. Thirteen records entered close-source review, 22 entered background review, 11 were excluded as single-component sources, and 25 were excluded as off-topic. Screening decided corpus membership and granted no proposition permission. The later v0.14 proposition review gave five bounded propositions manuscript permission, retained two sources as background-only, and quarantined six because exact text or required support remained unresolved.

Across the 1,087-record recovery population, the population ledger contains 107 retrieval outcomes. All 76 recovered-content records have a screening decision after a v0.14 overlay closed RS-DQ-004 as close on title, metadata, and a verified publisher-PDF route. Its unreadable text layer and unresolved author identity preserve zero proposition permission. The unresolved retrieval class contains 980 records without an outcome, 26 metadata-only records, two unavailable records, and three reconciled duplicates. These categories preserve the 2,431-record denominator without treating access failure or duplicate detection as a topic exclusion.

**Table 5. Residual-risk retrieval and screening checkpoint.**

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

The six pre-action propositions produce eighteen categorical findings across the three selected packets. Oko contains six partially supported findings. ZG710 contains one supported, one partially supported, and four unsupported findings. F/A-18C contains one supported, one partially supported, one unsupported, and three indeterminate findings. These counts describe the assessment output. They assign no distance among states and no aggregate control score.

**Figure 6. Evidence boundaries across six pre-action practical-control stages.** Each horizontal bar contains the six findings for one case. Partial support records some supporting evidence with a material gap. Indeterminate records insufficient evidence for a decision. Unsupported records evidence against the condition or evidence that the condition was absent. The display makes the public-record constraint visible and supplies no missingness rate, reliability estimate, or case ranking.

**Table A3. Availability of coding-stability evidence.**

| Test condition | Oko, 1983 | Patriot ZG710, 2003 | Patriot F/A-18C, 2003 |
|---|:---:|:---:|:---:|
| A second coding exists | Yes | No | No |
| The same source packet was used | Yes | NA | NA |
| The same evidence rule was used | No | NA | NA |
| Comparable pre-action stages | 6 | 0 | 0 |
| Unchanged classifications | 0 | NA | NA |
| Changed classifications | 6 | NA | NA |
| Independent second assessor | No | No | No |
| Reliability claim eligible | No | No | No |

*Note.* Oko's six changes arose when the direct-and-contemporaneous rule was applied to the frozen packet. The comparison records a correction under a changed classification rule. It cannot estimate intra-rater stability or inter-rater reliability. The two Patriot cases have one released coding each.

## 5. Discussion

### 5.1 Formal authority and practical force

Formal authority answers one question: who was permitted to approve, reject, modify, stop, or escalate? Practical control asks whether that permission had causal force in the bounded decision. Causal force depends on a connected chain. The person must receive relevant information, interpret it, retain intervention rights, have a feasible opportunity to act, exercise judgment, and affect execution. A break at any required stage makes the wider practical-force conclusion ineligible under this protocol.

The cross-case result illustrates the mechanism. Both Patriot packets support formal authority. ZG710 records absent practical conditions in the available evidence, while F/A-18C leaves several conditions unresolved. Oko's retrospective accounts support the reported sequence only partially under the direct-and-contemporaneous rule. The figure therefore turns “human in the loop” into testable documentary propositions.

### 5.2 The evidentiary function of an indeterminate state

Public incident records are shaped by classification, litigation, institutional disclosure, journalism, preservation, and time. A missing operator display or inquiry file can block a judgment about comprehension or feasibility. It cannot establish that the operator lacked comprehension or opportunity. The indeterminate state holds that boundary. It also makes the missing record visible as a research result and a recordkeeping requirement.

### 5.3 Records institutions would need

An institution seeking to substantiate practical control should preserve the information shown to the reviewer, timestamps, system state, uncertainty and known gaps, independent evidence, authority, available interventions, action taken, execution changes, and downstream effect. These records let an investigator test the chain after an incident and let an assurance team test it before deployment. Their presence supports inspectability. Safe, lawful, or beneficial outcomes require separate evidence.

### 5.4 Relationship to prior research

The method operationalizes established constructs at the level of a public evidence packet. Tracking, tracing, epistemic access, causal power, institutional design, and contestability define what control may require ([Santoni de Sio & van den Hoven, 2018](https://doi.org/10.3389/frobt.2018.00015); [Sterz et al., 2024](https://doi.org/10.1145/3630106.3659051); [Laux, 2024](https://doi.org/10.1007/s00146-023-01777-z); [Almada, 2019](https://doi.org/10.1145/3322640.3326699)). Human-factors research explains why monitoring and challenge can fail ([Bainbridge, 1983](https://doi.org/10.1016/0005-1098(83)90046-8); [Endsley, 2017](https://doi.org/10.1177/0018720816681350)). Incident analysis identifies the records needed to reconstruct an event ([Ezell et al., 2025](https://doi.org/10.1609/aies.v8i1.36596); [Macrae, 2022](https://doi.org/10.1111/risa.13850)). Assurance and evidence-chain methods structure the path from proposition to evidence and conclusion ([Burr & Leslie, 2023](https://doi.org/10.1007/s43681-022-00178-0); [Meng et al., 2026](https://doi.org/10.48550/arXiv.2605.26340); [Moghaddam, 2026](https://doi.org/10.48550/arXiv.2604.04103)). Recent close work already supplies AI-incident oversight tiers, runnable decision-chain protocols, versioned assurance cases, and architecture-aware audit evidence ([Bahidika, 2026](https://doi.org/10.14569/IJACSA.2026.0170502); [LaPosta, 2026](https://doi.org/10.1609/aaaiss.v8i1.42543); [Niazi et al., 2026](https://doi.org/10.3390/automation7030096); [Surve et al., 2026](https://doi.org/10.48550/arXiv.2606.21276)). The remaining contribution concerns the declared combination of a frozen selection path, public case packets, categorical missingness, correction history, evidence fitness, and conclusion closure.

### 5.5 Use for current AI governance

Contemporary systems can share the mechanisms tested here even when their architecture differs. Agentic software may compress review time, distribute actions across tools, obscure intermediate system state, or leave a reviewer with nominal stop authority. Dhanorkar, Passi, and Vorvoreanu show that developers already perform several forms of agent oversight work ([Dhanorkar et al., 2026](https://doi.org/10.1145/3805689.3812402)). Alhalangy and Lee, Yoon, and Lee show how escalation and record duties can enter prospective governance design ([Alhalangy, 2026](https://doi.org/10.3390/info17070694); [Lee et al., 2026](https://doi.org/10.3390/systems14070849)). Future work can apply the frozen chain to contemporary agent traces, appeals, high-stakes recommendations, and tool-mediated actions. Each application requires a new protocol and evidence boundary.

### 5.6 Ethical burden of proof

Human-control language can distribute responsibility, reassure affected people, and justify deployment. Those functions create an ethical burden of proof. An institution should preserve evidence capable of testing the practical-control chain when it represents a consequential system as human-controlled. The burden concerns the institution's claim and records. It does not presume individual fault.

This position follows from the risk of nominal oversight. A role assignment can place responsibility on a person who lacks information, capacity, opportunity, or causal power ([Green, 2022](https://doi.org/10.1016/j.clsr.2022.105681); [Sterz et al., 2024](https://doi.org/10.1145/3630106.3659051); [Douer & Meyer, 2020](https://doi.org/10.1109/TASE.2020.2965466)). Institutional design should anticipate human fallibility and incentives ([Laux, 2024](https://doi.org/10.1007/s00146-023-01777-z)). The proposed record set lets affected people, investigators, and oversight bodies examine whether responsibility was attached to practical authority. It guarantees no safe or just outcome.

## 6. Limitations

The design has several limits. The three strata were defined around the headline contrasts, and screening stopped after five candidates. The selected set demonstrates the procedure under those anticipated conditions. It estimates no prevalence and provides no independent classification test. Two cases concern one system family and operating period. Oko and Patriot differ materially from present learned systems.

The evidence is retrospective and public. Classified material, internal logs, complete displays, and some inquiry records were unavailable. Some cited content remains remote-only. Oko relies on later participant accounts and lacks a located contemporaneous command record. Source agreement can reflect shared dependence on an earlier account. Packet hashes prove preservation of stored bytes and do not prove source truth.

One assessor designed and applied the method. The study supplies no inter-rater reliability, construct-validity estimate, causal effect, safety effect, legal-sufficiency judgment, or outcome comparison. Artifact tests detect internal inconsistency and prespecified corruption. They do not validate historical interpretation.

The formal search used open indexes and official source pages. Author review closed the 89-record decision queue, the 71-record recovered forward-citation queue, the 13-source proposition gate, and the fifth direct-query screening decision. Another 980 records lack a retrieval outcome, and authenticated Scopus or Web of Science, IEEE Xplore, ACM Digital Library, PhilPapers, and HeinOnline or an equivalent legal index remain open. Five forward sources have one bounded proposition permission each, two remain background-only, and six are quarantined. RS-DQ-004 has zero source-content permission. The contribution language is therefore bounded to the declared search and reviewed source set.

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

## Version relationship and integrity status

The v0.14.0 preprint was archived on Zenodo under the version DOI [10.5281/zenodo.21926005](https://doi.org/10.5281/zenodo.21926005). This v0.15.0 candidate identifies that earlier record, supplies venue-required author and disclosure metadata, replaces the pending archive reference with the issued DOI, and preserves the same research question, case assessments, quantitative counts, and bounded conclusions. The repository's version history remains the authority for changes to data, claims, code, figures, and audit results.

The v0.14.0 integrity audit mapped 32 material claims to evidence, applied 33 controlled mutations, and detected all 33 corrupted conditions. These results test whether declared repository controls respond to seeded errors. They do not establish the truth of every historical claim, independent assessor agreement, population validity, or transfer to present AI systems.

## Data and materials availability

The repository, versioned releases, packets, assessments, figure data, audit outputs, search files, manuscript tables, and release manifests are available at [github.com/mj3b/trust-autonomy-evidence](https://github.com/mj3b/trust-autonomy-evidence). The v0.6.0 evidence archive has the version DOI [10.5281/zenodo.21865007](https://doi.org/10.5281/zenodo.21865007). The repository's all-versions DOI is [10.5281/zenodo.21841127](https://doi.org/10.5281/zenodo.21841127). The v0.14.0 preprint, including the proposition ledger, corrected source identities, 32-claim audit, 33 mutation controls, LaTeX source, and review PDF, has the version DOI [10.5281/zenodo.21926005](https://doi.org/10.5281/zenodo.21926005).

## Ethics and publication authority

The study uses public records and contains no participant recruitment, intervention, or direct interaction with living individuals. The repository preserves eligible public-domain and openly licensed material, cites proprietary sources through metadata and limited paraphrase, and excludes personal, confidential, institutionally restricted, and security-sensitive material under the frozen protocol. No institutional determination about human-subjects review has been obtained. The author must check Harvard and venue requirements before submission and must not describe the study as exempt without the applicable determination.

## Author contributions

Mark Julius Banasihan: Conceptualization, methodology, investigation, data curation, software, validation, visualization, writing of the original draft, review and editing, project administration, and accountable authorship.

## AI-assistance disclosure

Generative AI tools assisted with literature discovery, metadata organization, preliminary screening proposals, decision-ledger preparation, draft development, code generation, figure and consistency checks, and language revision. AI outputs did not approve claims or evidence states. Mark Julius Banasihan defined the research question and protocols, reviewed and approved the 89 screening decisions, approved the evidence and assessment decisions, verified the sources used for claims, controlled the repository releases, and remains responsible for the analysis, interpretations, errors, and submitted text. Claim-level evidence mapping, evidence-fitness checks, controlled mutations, reference verification, and method-code alignment checks were applied to the released research artifacts. These controls test declared consistency and error response; they do not replace independent peer review.

## Conflicts of Interest

The author declares no conflicts of interest.

## References

- Abdalilah Alhalangy. (2026). [Operationalizing Accountable AI Through Traceable Governance Architecture for Institutional Decision Support](https://doi.org/10.3390/info17070694). *Information*, 17(7), 694.
- Marco Almada. (2019). [Human Intervention in Automated Decision-Making: Toward the Construction of Contestable Systems](https://doi.org/10.1145/3322640.3326699). *Proceedings of the Seventeenth International Conference on Artificial Intelligence and Law*, 2-11.
- Saar Alon-Barkat and Madalina Busuioc. (2023). [Human-AI Interactions in Public Sector Decision Making: Automation Bias and Selective Adherence to Algorithmic Advice](https://doi.org/10.1093/jopart/muac007). *Journal of Public Administration Research and Theory*, 33(1), 153-169.
- Ornella Bahidika. (2026). [Agentic Accountability: ``The Buck Stops Where?'' Ethical Frameworks for Human Oversight of Autonomous AI Systems](https://doi.org/10.14569/IJACSA.2026.0170502). *International Journal of Advanced Computer Science and Applications*.
- Lisanne Bainbridge. (1983). [Ironies of Automation](https://doi.org/10.1016/0005-1098(83)90046-8). *Automatica*, 19(6), 775-779.
- Kevin Baum and Johann Laux. (2026). [Constitutive vs. Corrective: A Causal Taxonomy of Human Runtime Involvement in AI Systems](https://doi.org/10.48550/arXiv.2603.19213).
- Christopher Burr and David Leslie. (2023). [Ethical Assurance: A Practical Approach to the Responsible Design, Development, and Deployment of Data-Driven Technologies](https://doi.org/10.1007/s43681-022-00178-0). *AI and Ethics*, 3(1), 73-98.
- Simeon C. Calvert. (2025). [Principles and Framework for the Operationalisation of Meaningful Human Control over Autonomous Systems](https://doi.org/10.1007/s11948-025-00554-z). *Science and Engineering Ethics*, 31(5), 27.
- Jovana Davidovic. (2023). [On the Purpose of Meaningful Human Control of AI](https://doi.org/10.3389/fdata.2022.1017677). *Frontiers in Big Data*, 5, 1017677.
- Sidney W. A. Dekker. (2002). [Reconstructing Human Contributions to Accidents: The New View on Error and Performance](https://doi.org/10.1016/S0022-4375(02)00032-4). *Journal of Safety Research*, 33(3), 371-385.
- Shipi Dhanorkar, Samir Passi, and Mihaela Vorvoreanu. (2026). [Human Oversight of Agentic Systems in Practice: Examining the Oversight Work, Challenges, and Heuristics of Developers Using Software Agents](https://doi.org/10.1145/3805689.3812402). *Proceedings of the 2026 ACM Conference on Fairness, Accountability, and Transparency*.
- Nir Douer and Joachim Meyer. (2020). [The Responsibility Quantification Model of Human Interaction With Automation](https://doi.org/10.1109/TASE.2020.2965466). *IEEE Transactions on Automation Science and Engineering*, 17(2), 1044-1060.
- Mica R. Endsley. (2017). [From Here to Autonomy: Lessons Learned from Human-Automation Research](https://doi.org/10.1177/0018720816681350). *Human Factors*, 59(1), 5-27.
- Carson Ezell, Xavier Roberts-Gaal, and Alan Chan. (2025). [Incident Analysis for AI Agents](https://doi.org/10.1609/aies.v8i1.36596). *Proceedings of the AAAI/ACM Conference on AI, Ethics, and Society*, 8(1), 865-878.
- Ben Green. (2022). [The Flaws of Policies Requiring Human Oversight of Government Algorithms](https://doi.org/10.1016/j.clsr.2022.105681). *Computer Law & Security Review*, 45, 105681.
- Pim Haselager, Hanna Schraffenberger, Serge Thill, Simon Fischer, Pablo Lanillos, Sebastiaan van de Groes, and Miranda van Hooff. (2023). [Reflection Machines: Supporting Effective Human Oversight Over Medical Decision Support Systems](https://doi.org/10.1017/S0963180122000718). *Cambridge Quarterly of Healthcare Ethics*, 32(4), 552-567.
- Noam Kolt. (2025). [Governing AI Agents](https://arxiv.org/abs/2501.07913).
- Paul LaPosta. (2026). [Conflict as Telemetry for Illegible AI: Governing LLM Agent Workflows](https://doi.org/10.1609/aaaiss.v8i1.42543). *AAAI Spring Symposia*.
- Khoa Lam, Benjamin Lange, Borhane Blili-Hamelin, Jovana Davidovic, Shea Brown, and Ali Hasan. (2024). [A Framework for Assurance Audits of Algorithmic Systems](https://doi.org/10.1145/3630106.3658957). *Proceedings of the 2024 ACM Conference on Fairness, Accountability, and Transparency*, 1078-1092.
- Markus Langer, Kevin Baum, and Nadine Schlicker. (2024). [Effective Human Oversight of AI-Based Systems: A Signal Detection Perspective on the Detection of Inaccurate and Unfair Outputs](https://doi.org/10.1007/s11023-024-09701-0). *Minds and Machines*, 35(1).
- Johann Laux. (2024). [Institutionalised Distrust and Human Oversight of Artificial Intelligence: Towards a Democratic Design of AI Governance Under the European Union AI Act](https://doi.org/10.1007/s00146-023-01777-z). *AI & Society*, 39(6), 2853-2866.
- Lidaw Fabrice Ledjaki, Yuan-Chen Chang, Mohamed Loutis, and Esma Aimeur. (2026). [Prompt Scene Investigation: Uncovering the Evidence in LLMs](https://doi.org/10.1145/3774905.3795469). *Companion Proceedings of the ACM Web Conference 2026*, 284-290.
- John D. Lee and Katrina A. See. (2004). [Trust in Automation: Designing for Appropriate Reliance](https://doi.org/10.1518/hfes.46.1.50_30392). *Human Factors*, 46(1), 50-80.
- Hyun-Kyung Lee, Cheolhee Yoon, and Bong Gyou Lee. (2026). [Operationalising Human-Centred AI Governance Under the EU AI Act: A Governance Framework for Human Oversight and Data Accountability](https://doi.org/10.3390/systems14070849). *Systems*, 14(7), 849.
- Alex Leung, Rex Zhang, Kentaroh Toyoda, and SiewMei Loh. (2026). [From Control Boundary to Insurance Claim: Reconstructing AI-Mediated Losses Through the CER Framework](https://arxiv.org/abs/2606.03777).
- Wangfan Li, Athish Venkatachalam, Jackson Bowen, and Carlos Toxtli-Hernandez. (2025). [Human Oversight over Autonomous Task Execution in Sandbox Environments](https://doi.org/10.1109/CAI64502.2025.00121). *2025 IEEE Conference on Artificial Intelligence*, 663-668.
- Carl Macrae. (2022). [Learning from the Failure of Autonomous and Intelligent Systems: Accidents, Safety, and Sociotechnical Sources of Risk](https://doi.org/10.1111/risa.13850). *Risk Analysis*, 42(9), 1999-2025.
- John A. McDermid. (2019). [Human Control of AI and Autonomy: The Art of the Possible](https://www.york.ac.uk/assuring-autonomy/news/blog/human-control-ai-autonomy/). *Centre for Assuring Autonomy, University of York*.
- Sean McGregor. (2021). [Preventing Repeated Real World AI Failures by Cataloging Incidents: The AI Incident Database](https://doi.org/10.1609/aaai.v35i17.17817). *Proceedings of the AAAI Conference on Artificial Intelligence*, 35(17), 15458-15463.
- Rui Meng, Bhavana Dalvi Mishra, Jiefeng Chen, Chun-Liang Li, Palash Goyal, Mihir Parmar, Yiwen Song, Yale Song, Rajarishi Sinha, Parthasarathy Ranganathan, Burak Gokturk, Jinsung Yoon, and Tomas Pfister. (2026). [ScientistOne: Towards Human-Level Autonomous Research via Chain-of-Evidence](https://doi.org/10.48550/arXiv.2605.26340).
- Mahyar Tourchi Moghaddam. (2026). [Compliance-by-Construction Argument Graphs: Using Generative AI to Produce Evidence-Linked Formal Arguments for Certification-Grade Accountability](https://doi.org/10.48550/arXiv.2604.04103).
- M. Niazi, Hossein Hassani, and Madison Lee. (2026). [Rights-Based AI in Cyber-Physical Systems: A Governance Framework for Socio-Technical Resilience and Trust](https://doi.org/10.3390/automation7030096). *Automation*, 7(3), 96.
- Kevin Paeth, Daniel Atherton, Nikiforos Pittaras, Heather Frase, and Sean McGregor. (2025). [Lessons for Editors of AI Incidents from the AI Incident Database](https://doi.org/10.1609/aaai.v39i28.35163). *Proceedings of the AAAI Conference on Artificial Intelligence*, 39(28), 28946-28953.
- Colin Paterson, Richard David Hawkins, Chiara Picardi, Yan Jia, Radu Calinescu, and Ibrahim Habli. (2025). [Safety Assurance of Machine Learning for Autonomous Systems](https://doi.org/10.1016/j.ress.2025.111311). *Reliability Engineering & System Safety*, 264(Part A), 111311.
- Nikiforos Pittaras and Sean McGregor. (2023). [A Taxonomic System for Failure Cause Analysis of Open Source AI Incidents](https://ceur-ws.org/Vol-3381/17.pdf). *Proceedings of the Workshop on Artificial Intelligence Safety 2023*, 3381.
- Filippo Santoni de Sio and Jeroen van den Hoven. (2018). [Meaningful Human Control over Autonomous Systems: A Philosophical Account](https://doi.org/10.3389/frobt.2018.00015). *Frontiers in Robotics and AI*, 5, 15.
- Luciano Cavalcante Siebert, Maria Luce Lupetti, Evgeni Aizenberg, Niek Beckers, Arkady Zgonnikov, Herman Veluwenkamp, David Abbink, Elisa Giaccardi, Geert-Jan Houben, Catholijn M. Jonker, Jeroen van den Hoven, Deborah Forster, and Reginald L. Lagendijk. (2023). [Meaningful Human Control: Actionable Properties for AI System Development](https://doi.org/10.1007/s43681-022-00167-3). *AI and Ethics*, 3, 241-255.
- Sarah Sterz, Kevin Baum, Sebastian Biewer, Holger Hermanns, Anne Lauber-Ronsberg, Philip Meinel, and Markus Langer. (2024). [On the Quest for Effectiveness in Human Oversight: Interdisciplinary Perspectives](https://doi.org/10.1145/3630106.3659051). *Proceedings of the 2024 ACM Conference on Fairness, Accountability, and Transparency*, 2495-2507.
- Priyanka Surve, Asaf Shabtai, and Yuval Elovici. (2026). [CEDAR-42001: From ISO/IEC 42001 Conformity to Architecture-Aware, Audit-Visible Assurance Posture for AI Cyber-Physical Systems](https://doi.org/10.48550/arXiv.2606.21276).
- Lucas Elbert Suryana, Sina Nordhoff, Simeon C. Calvert, Arkady Zgonnikov, and Bart van Arem. (2024). [User Perception of Partially Automated Driving Systems: A Meaningful Human Control Perspective on the Perception among Tesla Users](https://doi.org/10.48550/arXiv.2402.08080).
- Dov Te'eni, Inbal Yahav, and David Schwartz. (2025). [What It Takes to Control AI by Design: Human Learning](https://doi.org/10.1007/s00146-025-02401-y). *AI & Society*.
- Andreas Tsamados, Luciano Floridi, and Mariarosaria Taddeo. (2025). [Human Control of AI Systems: From Supervision to Teaming](https://doi.org/10.1007/s43681-024-00489-4). *AI and Ethics*, 5(2), 1535-1548.
- Ilse Verdiesen, Filippo Santoni de Sio, and Virginia Dignum. (2021). [Accountability and Control Over Autonomous Weapon Systems: A Framework for Comprehensive Human Oversight](https://doi.org/10.1007/s11023-020-09532-9). *Minds and Machines*, 31, 137-163.
- Kevin Wei and Lennart Heim. (2026). [Designing Incident Reporting Systems for Harms from General-Purpose AI](https://doi.org/10.1609/aaai.v40i44.41139). *Proceedings of the AAAI Conference on Artificial Intelligence*, 40(44), 38016-38029.
- Yuyuan Zhang, Limin Jing, and Chengyang Sun. (2018). [Systems-Based Analysis of China-Tianjin Port Fire and Explosion: A Comparison of HFACS, AcciMap, and STAMP](https://doi.org/10.1007/s11668-018-0534-1). *Journal of Failure Analysis and Prevention*, 18(6), 1386-1400.
- Liming Zhu, Qinghua Lu, Ming Ding, Sung Une Lee, and Chen Wang. (2026). [Designing Meaningful Human Oversight in AI](https://doi.org/10.1007/s43681-026-01147-7). *AI and Ethics*, 6, 286.
- Jasper van der Waa, Jurriaan van Diggelen, Luciano Cavalcante Siebert, Mark Neerincx, and Catholijn Jonker. (2020). [Allocation of Moral Decision-Making in Human-Agent Teams: A Pattern Approach](https://doi.org/10.1007/978-3-030-49183-3_16). *Engineering Psychology and Cognitive Ergonomics. Cognition and Design*, 203-220.
