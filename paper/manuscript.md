# From Formal Authority to Practical Human Control

## A traceable method for reconstructing human control in automated decisions

**Author:** Mark Julius Banasihan  
**ORCID:** [0009-0001-8121-2878](https://orcid.org/0009-0001-8121-2878)  
**Status:** Methods and results draft, v0.3

## Abstract

Institutions often treat a named human reviewer or approval step as evidence that an automated or autonomous system remains under human control. That inference can fail when the designated person lacks timely information, comprehension, authority, a feasible opportunity to challenge the system, or the ability to affect the outcome. This paper develops a frozen, evidence-traceable procedure for representing formal authority, practical control, and unresolved evidence in bounded public incident records. The protocol fixed the evidence cutoff, candidate collections, search vocabulary, eligibility rules, screening order, three selection strata, and missing-data treatment before candidate screening. It assembled three versioned historical case packets with claim-level provenance, categorical evidence states, and a chain from information access through effect. A preregistered v0.6 adjudication applied the existing direct-and-contemporaneous rule to the Oko packet and reclassified access, comprehension, authority, feasibility, exercise, and effect from supported to partially supported. The current assessment set therefore records partial support across those six Oko stages, supported authority with unsupported practical conditions in ZG710, and supported authority with unresolved practical conditions in F/A-18C. The three contrastive cases demonstrate procedure execution and no independent test of discrimination. The contribution is a traceable, executable evidence procedure with a visible correction path. Three retrospective, single-assessor cases supply no population estimate, causal validation, independent-reliability result, or transfer claim for current learned systems.

## Resolved evidence decision

`PAPER-BLOCKER-01` identified a mismatch between Oko's released v0.3 supported states and the protocol's direct-and-contemporaneous evidence rule. The [v0.6 adjudication protocol](../protocols/oko-evidence-adjudication-v0.6.0.md) was frozen before reassessment. The resulting [change ledger](../assessments/v0.6.0/oko-change-ledger.json) records six transitions to partially supported and preserves v0.3.0 as release history. Missing contemporaneous records remain a limitation.

## 1. Introduction

### 1.1 The institutional problem

An approval step proves that an institution assigned a role. It does not show that the person received the relevant information, understood the system's limits, could challenge the proposed action in time, exercised that authority, or changed the outcome. A human-control claim therefore contains several empirical propositions that a signature or job title cannot establish by itself.

Human-factors research explains the mechanism. Automation can leave people responsible for rare or abnormal conditions after routine system operation has reduced their preparation for those conditions [@bainbridge1983ironies]. Situation awareness and intervention performance depend on what the person can perceive, understand, and project under the operating conditions [@endsley2017autonomy]. Trust affects reliance through the interaction of the person, system, task, and context [@lee2004trust]. Formal authority can remain intact as these operational conditions deteriorate.

The same problem appears in policy. Green finds that government rules often require human oversight without establishing that the designated people can perform the intended review [@green2022flaws]. Zhu et al. separate AI operative agency from human evaluative agency and identify verification, contestation, and substitution as oversight mechanisms [@zhu2026oversight]. These accounts direct attention to a documentary question: what evidence would justify reliance on an institutional claim that human authority had practical force in one consequential decision?

### 1.2 Research gap

Four research streams answer parts of that question. Meaningful-human-control scholarship defines moral, design, and institutional conditions for control [@santoni2018meaningful; @siebert2023meaningful; @davidovic2023purpose; @calvert2025principles]. Human-factors research explains why monitoring, comprehension, and timely intervention can fail [@bainbridge1983ironies; @lee2004trust; @endsley2017autonomy]. Incident research specifies causal factors, reporting structures, and information needs [@mcgregor2021incidents; @macrae2022failure; @ezell2025incident; @paeth2025lessons; @wei2026reporting]. Assurance research connects claims to evidence, assumptions, and uncertainty [@burr2023ethical; @paterson2025safety].

The closest prior work narrows the remaining contribution. Dekker already provides a retrospective method for reconstructing human contributions inside the event sequence and controlling hindsight [@dekker2002reconstructing]. McDermid ties effective intervention to time, independent knowledge, skills, and assurance [@mcdermid2019control]. Pittaras and McGregor classify possible failure causes from incomplete open-source AI incidents [@pittaras2023taxonomic]. Leung et al. join control boundaries, reconstructed state, and claim-grade evidence for agentic AI losses [@leung2026cer]. Ledjaki et al. propose prompt-level chain of custody and replay [@ledjaki2026prompt].

These sources rule out broad originality claims for control conditions, public-record reconstruction, incident evidence, provenance, or assurance. Langer, Baum, and Schlicker separate oversight sensitivity from response tendency [@langer2024signal]. Langer, Lazar, and Baum show why checklist compliance may fail to establish actual oversight performance [@langer2025testing]. Lam et al. formalize assurance audits for algorithmic systems [@lam2024assurance]. Gaube et al. supply a wider architecture, process, and documentation framework for effective human oversight [@gaube2026oversight]. The remaining hypothesis concerns one integration: protocol fixation before screening, a preserved selection path, versioned public evidence packets, explicit missingness, a practical-control chain, versioned correction, and executable artifact checks. The [novelty audit](novelty-audit.md) treats that hypothesis as provisional until institutional database searches and full citation chaining are complete.

### 1.3 Research question and contribution

> How can a frozen, evidence-traceable assessment procedure represent formal human authority, practical human control, and unresolved evidence in a bounded public incident record?

The paper proposes a documentary assessment procedure. It defines a bounded action sequence, fixes the case-selection and missing-data rules, assembles a versioned evidence packet, assigns provenance to material statements, and evaluates six pre-action conditions: access, comprehension, authority, feasible challenge, exercised challenge, and effect. An explicit indeterminate state prevents missing records from becoming negative factual findings.

The three cases demonstrate that procedure under contrastive evidence conditions. They do not test prevalence, classification accuracy, independent reliability, causal effects, or transfer to current learned systems. The institutional output is a proposed record set that a reviewer would need before relying on a practical-control claim.

### 1.4 Paper structure

Section 2 locates the procedure in meaningful-human-control, human-factors, incident-analysis, reconstruction, and assurance research. Section 3 defines the frozen method and its transfer boundary. Section 4 reports the released assessment states and the open protocol-consistency question. Sections 5 through 7 separate interpretation, limitations, and proposed institutional record requirements.

## 2. Related work

### 2.1 Meaningful human control

Santoni de Sio and van den Hoven define meaningful human control through tracking and tracing. System behavior must respond to relevant human reasons, and human actors must be able to understand their role and bear responsibility [@santoni2018meaningful]. This account makes human presence insufficient because control depends on the relation among system behavior, human reasons, and identifiable responsibility.

Later work moves the concept toward institutional and engineering use. Siebert et al. propose actionable properties that align ability, authority, and responsibility [@siebert2023meaningful]. Davidovic argues that designers must first state the purpose served by human control [@davidovic2023purpose]. Calvert places proximal intervention inside a wider system of distal control across design, deployment, and governance [@calvert2025principles]. Tsamados, Floridi, and Taddeo compare supervisory control with human-machine teaming for foundation-model systems [@tsamados2025control]. Zhu et al. frame oversight as human evaluative agency expressed through verification, steering, contestation, and substitution [@zhu2026oversight].

The present paper uses these sources to define the proposition being assessed. It does not offer a new philosophical account of meaningful human control.

### 2.2 Human oversight and the automation problem

Bainbridge shows how automation transfers rare, abnormal, and difficult work to people after routine operation has weakened the practice needed for that work [@bainbridge1983ironies]. Endsley connects autonomous-system performance to situation awareness, monitoring, workload, trust, and out-of-the-loop degradation [@endsley2017autonomy]. Lee and See model appropriate reliance as a relation among the person, automation, task, and environment [@lee2004trust]. Together, these mechanisms explain how nominal oversight can lose practical force.

Human response to algorithmic advice is conditional. Alon-Barkat and Busuioc find both automation bias and selective adherence across experimental public-sector decisions [@alonbarkat2023interactions]. Green's policy analysis reaches an institutional implication: oversight rules need evidence that people can perform the assigned review [@green2022flaws]. The present method converts that implication into separate documentary questions about information, comprehension, authority, feasibility, action, and effect.

### 2.3 AI incident analysis and missing records

The AI Incident Database was created to provide a shared record of real-world failures and support learning across incidents [@mcgregor2021incidents]. Its reports remain public-source records with changing coverage and varying detail. Pittaras and McGregor respond to that constraint through expert classification of goals, technologies, and possible technical failure causes [@pittaras2023taxonomic]. Paeth et al. show that incident reports contain structural ambiguity and unavoidable epistemic uncertainty [@paeth2025lessons]. These limits support an explicit indeterminate state.

Macrae demonstrates that public investigative reports can support systematic analysis of sociotechnical failure in an autonomous system [@macrae2022failure]. Ezell, Roberts-Gaal, and Chan specify system, contextual, cognitive, access, tool, log, and documentation information needed to investigate AI-agent incidents [@ezell2025incident]. Wei and Heim locate those information needs inside institutional reporting systems and post-reporting action [@wei2026reporting]. The present method applies a narrower question to each packet: which records support a claim that assigned human authority could affect the bounded action?

### 2.4 Reconstruction, forensics, and assurance

Dekker treats accident reconstruction as recovery of what people could know and why their actions made sense inside the unfolding event [@dekker2002reconstructing]. This approach guards against hindsight and unsupported counterfactual blame. McDermid identifies time, knowledge independent of the automated system, and practiced skill as conditions for effective intervention [@mcdermid2019control]. These works closely anticipate the procedure's reconstruction logic and feasible-challenge stage.

Argument-based assurance asks whether evidence justifies a stated claim under explicit assumptions and uncertainty. Burr and Leslie extend that structure to ethical and social claims [@burr2023ethical]. AMLAS applies it to machine-learning safety across development and deployment [@paterson2025safety]. The present procedure borrows this claim-evidence discipline for retrospective assessment. It does not issue a safety case for Oko or Patriot.

Recent forensic work provides closer technical neighbors. Leung et al. reconstruct changing AI system state for insurance claims [@leung2026cer]. Ledjaki et al. preserve and replay prompt-level evidence through a chain-of-custody design [@ledjaki2026prompt]. These papers constrain the contribution to the specific combination of practical human control, public case selection, categorical missingness, and executable repository checks.

ScientistOne supplies a closer architecture for research verifiability. Its Chain-of-Evidence framework requires claims to trace to evidence, and its post-hoc audit checks scores, specification violations, references, and method-code alignment [@meng2026scientistone]. This prior work rules out an originality claim for claim traceability or the four audit categories. The present adaptation adds a governance-specific assessment of directness, contemporaneity, independence, completeness, publication authority, and dependency closure. These additions remain method proposals until independent review tests their application.

### 2.5 Synthesis

Existing research supplies theories of control, evidence about oversight performance, retrospective reconstruction methods, public incident-analysis procedures, reporting requirements, assurance logic, and forensic evidence controls. This paper studies one integration of those elements in a frozen public-case procedure.

The contribution is methodological and bounded. It asks how a reader can inspect the path from candidate selection to source packet, provenance label, assessment state, figure, and manuscript claim. The current evidence shows that the procedure can generate that path for three selected packets. It does not show that another assessor would agree, that the categories are valid across domains, or that use of the procedure improves institutional decisions.

## 3. Method

### 3.1 Study design

Describe the work as a retrospective, purposefully selected, single-assessor methods study. Define one bounded AI-mediated decision or action sequence as the unit of analysis.

### 3.2 System inclusion and transfer boundary

Explain the functional, historically neutral AI-system definition used by the frozen protocol. Identify the machine-based inference, recommendation, classification, or decision function in each case. State that Oko and Patriot differ materially from current learned systems and agents. Any present-system application must be justified through shared mechanisms, not category labels.

### 3.3 Protocol freeze and evidence cutoff

Report the freeze commit, evidence cutoff, fixed vocabulary, and rule that screening could begin only after the protocol and empty register reached `main`.

### 3.4 Candidate collections and search

Report the AI Incident Database snapshot, OECD export, preserved hashes, query terms, candidate counts, and interface limitation.

### 3.5 Eligibility, strata, and stopping

Define the six eligibility conditions, exclusions, chronological screening order, three strata, first-eligible rule, and stopping condition.

State that the strata anticipate the three headline contrasts. The case set demonstrates procedure execution under those conditions and does not independently validate discrimination.

**Figure:** Figure 1, frozen selection and stopping.

### 3.6 Versioned evidence packets

Describe the case boundary, chronology, source manifest, missing-evidence record, publication-rights statement, preserved files, remote-only sources, and SHA-256 packet manifest. Limit immutability claims to content that was preserved and hashed.

### 3.7 Assessment contract

Define the autonomy variables, trust-evidence propositions, practical-control stages, categorical states, and provenance labels.

### 3.8 Missing evidence and inference

Explain why missing evidence is indeterminate unless the packet establishes that a required record should exist and is absent. Separate direct record, source claim, assessor inference, and unresolved evidence.

### 3.9 Artifact and consistency controls

Describe schema checks, packet hashes, selection invariants, interaction checks, mutation tests, figure rebuilds, and release manifests. Separate repeatable artifact transformations from independent reproduction of assessment judgments.

Describe the v0.6 Chain-of-Evidence adaptation, including exact locators, integrity states, human support attestations, five evidence-fitness dimensions, dependency closure, run-type labels, and bounded-language declarations. Report the four adapted ScientistOne checks and the repository-specific fitness and closure check. State that the audit covers the declared material claims and a separate sentence-level literature-support register.

### 3.10 Frozen Oko adjudication

Report the adjudication question, frozen evidence universe, cutoff, stage rules, dependency rule, and prereassessment freeze commit. Explain that retrospective testimony directly supports what a participant later reported and does not become a contemporaneous event record. Preserve the v0.3.0 assessment and publish each v0.6 transition in a separate ledger.

**Figure:** Figure A3, claim-evidence integrity matrix.

## 4. Results

### 4.1 Selection result

Report 928 preserved candidate records, five screened candidates, two exclusions, three selections, and the stopping condition. State that 923 candidates remain unscreened and carry no exclusion decision.

### 4.2 Oko, 1983

Report both versions. The v0.3.0 release classified the six stages from access through effect as supported. The frozen v0.6 adjudication classifies all six as partially supported because the packet contains retrospective participant accounts and no located contemporaneous command log or official incident record. The adjudication resolves the protocol mismatch through reclassification. It does not fill the historical record or establish the sole cause of the ultimate outcome.

### 4.3 Patriot ZG710, 2003

Report formal authority, compressed time, incomplete information, system-centered training, challenge infeasibility, engagement, and loss. Do not infer more than the packet supports.

### 4.4 Patriot F/A-18C, 2003

Report the supported detection-to-engagement sequence. Preserve the indeterminate findings created by missing inquiry records, logs, displays, and technical details.

### 4.5 Cross-case practical-control chain

Compare access, comprehension, authority, feasible challenge, exercised challenge, and effect.

**Figure:** Figure 2, practical-control chain.

**Bounded current result:** Authority is partially supported in Oko and supported in both Patriot packets. The remaining links and protective effect receive different states. The comparison reports procedure output under contrastive selection.

### 4.6 Decision paths and trust-evidence states

Use Figure 3 for source-linked chronology and Figure 4 for the 12 trust-evidence propositions. Do not aggregate categorical states into a score.

## 5. Discussion

### 5.1 Formal authority and practical force

Explain why an assigned right to decide does not establish timely access, understanding, feasible challenge, action, or effect.

### 5.2 The evidentiary function of an indeterminate state

Explain how the indeterminate state prevents incomplete public records from becoming negative factual findings.

### 5.3 Records institutions would need

Derive a bounded recordkeeping proposition: institutions seeking to demonstrate practical control should preserve the information shown to the reviewer, timing, system state, independent evidence, authority, available interventions, action taken, and effect.

Distinguish this institutional implication from a finding that such records guarantee safe outcomes.

### 5.4 Relationship to prior research

Explain how the method complements meaningful-human-control theory, human-factors evidence, incident analysis, and assurance cases.

### 5.5 Use for current AI governance

Discuss possible application to contemporary systems as a future research direction. Do not transfer historical case results to present learned systems.

## 6. Limitations

Address purposeful selection, alignment between the strata and headline contrasts, stopping after five screened candidates, two cases from one system family and operating period, retrospective public evidence, source dependence, classified and unavailable records, remote-only source content, the remaining Oko evidence gap, single assessment, no inter-rater evidence, no causal estimate, incomplete institutional database searching, and no present-system transfer claim.

## 7. Institutional implications

State which evidence an assurance team, regulator, deployer, or incident investigator would need to examine before relying on a human-control claim. Treat the list as a proposed assessment requirement, not proof of legal compliance.

## 8. Conclusion

Return to the decision problem. State only that the method produced traceable, bounded distinctions for the three packets and that formal authority alone did not establish practical control within them.

## Data and materials availability

Link the v0.5.0 [Zenodo archive](https://doi.org/10.5281/zenodo.21863464), the versioned GitHub releases, packet index, assessment ledger, figure data, audit outputs, and release manifests. The all-versions DOI is `10.5281/zenodo.21841127`. The exact v0.6.0 DOI will be added after Zenodo archives the GitHub release.

## Ethics and publication authority

Document the use of public records, copyright limits, redaction rules, security-sensitive exclusions, and the basis for any determination about human-subjects review requirements.

## Author contributions

To be completed using the selected venue's taxonomy.

## AI-assistance disclosure

To be completed after selecting a venue. The disclosure must identify material assistance with literature discovery, drafting, formatting, and consistency checking and preserve the human author's responsibility for source verification, analysis, and conclusions.
