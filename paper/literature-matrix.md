# Core Literature Matrix

## Review question

Which prior work most closely addresses the distinction between formal human authority and evidence of practical human control in a reconstructable automated decision?

## Status

The initial 15-source set was checked against publisher pages, DOI records, conference proceedings, or institutional repositories on 8 August 2026. The PR #11 pressure test added eight near-neighbors that constrain the proposed contribution. The v0.5 review adds ScientistOne as a close prior architecture for claim traceability and integrity audit. Metadata has been checked for those additions. Full-text review remains incomplete where the [novelty audit](novelty-audit.md) says so. This matrix is a structured seed, not a systematic review.

| ID | Stream and source | What it contributes | Relationship to this paper | Boundary or difference |
|---|---|---|---|---|
| L01 | Meaningful human control: [Santoni de Sio and van den Hoven (2018)](https://doi.org/10.3389/frobt.2018.00015) | Defines tracking and tracing conditions for meaningful human control. | Supplies the philosophical basis for distinguishing control from mere human presence. | Does not provide a frozen retrospective evidence-reconstruction procedure. |
| L02 | Operational properties: [Siebert et al. (2023)](https://doi.org/10.1007/s43681-022-00167-3) | Proposes four actionable system properties, including alignment among ability, authority, and responsibility. | Closely supports the paper's practical-force mechanism. | Uses design properties and illustrative scenarios; it does not analyze public incident packets. |
| L03 | Institutional purpose: [Davidovic (2023)](https://doi.org/10.3389/fdata.2022.1017677) | Argues that the purpose of human control must be stated before institutional design follows. | Requires this paper to state the decision served by the control test. | Provides a normative purpose analysis and no evidence assessment. |
| L04 | Operational framework: [Calvert (2025)](https://doi.org/10.1007/s11948-025-00554-z) | Proposes domain-neutral principles and a framework for operationalizing meaningful human control. | Helps position the control chain against a wider system of proximal and distal control. | Does not test claims against a versioned public-case evidence procedure. |
| L05 | Supervision and teaming: [Tsamados, Floridi, and Taddeo (2025)](https://doi.org/10.1007/s43681-024-00489-4) | Compares supervisory control with human-machine teaming for contemporary AI. | Frames the limits of exclusive human supervision and possible future applications. | Does not reconstruct whether practical control existed in historical incidents. |
| L06 | Layered agency: [Zhu et al. (2026)](https://doi.org/10.1007/s43681-026-01147-7) | Distinguishes AI operative agency from human evaluative agency and proposes oversight mechanisms. | Closely relates verification, contestation, and substitution to practical control. | Remains design-oriented and calls for empirical testing under organizational conditions. |
| L07 | Human factors: [Bainbridge (1983)](https://doi.org/10.1016/0005-1098(83)90046-8) | Explains why automation can leave people responsible for rare tasks for which automation has made them less prepared. | Provides the classic mechanism behind ineffective fallback authority. | Predates modern AI and does not supply an AI governance assessment method. |
| L08 | Trust and reliance: [Lee and See (2004)](https://doi.org/10.1518/hfes.46.1.50_30392) | Connects trust, context, automation characteristics, and appropriate reliance. | Supports treating trust as a relation grounded in evidence. | Reviews reliance behavior and does not test institutional proof of control. |
| L09 | Situation awareness: [Endsley (2017)](https://doi.org/10.1177/0018720816681350) | Synthesizes out-of-the-loop performance, monitoring, trust, and situation-awareness problems. | Supports the access, comprehension, and feasible-challenge stages. | Addresses human-autonomy interaction broadly and does not provide case-packet provenance. |
| L10 | Oversight policy: [Green (2022)](https://doi.org/10.1016/j.clsr.2022.105681) | Finds that many government oversight policies assume people can perform the intended review and proposes institutional justification. | Directly supports the paper's decision problem and its focus on evidence behind oversight claims. | Surveys policy and prior evidence without reconstructing a declared control chain. |
| L11 | Human processing of advice: [Alon-Barkat and Busuioc (2023)](https://doi.org/10.1093/jopart/muac007) | Tests automation bias and selective adherence across three experiments. | Prevents the paper from treating human deference as a universal or simple mechanism. | Experimental advice-taking differs from retrospective high-velocity incident reconstruction. |
| L12 | Agent incident analysis: [Ezell, Roberts-Gaal, and Chan (2025)](https://doi.org/10.1609/aies.v8i1.36596) | Identifies system, contextual, and cognitive factors plus the records needed to investigate agent incidents. | Supplies a direct bridge between incident causes and required evidence. | Centers AI agents and information requirements, not practical human control as the assessed proposition. |
| L13 | Incident uncertainty: [Paeth et al. (2025)](https://doi.org/10.1609/aaai.v39i28.35163) | Documents structural ambiguity and unavoidable epistemic uncertainty in AI incident reporting. | Supports explicit indeterminate states and restrained interpretation of incident databases. | Studies incident editing and taxonomy without a versioned case-reconstruction procedure. |
| L14 | Ethical assurance: [Burr and Leslie (2023)](https://doi.org/10.1007/s43681-022-00178-0) | Extends argument-based assurance to ethical, social, and legal claims. | Supports linking institutional claims to structured arguments and inspectable evidence. | Covers lifecycle assurance broadly and does not isolate one human-control mechanism. |
| L15 | ML safety assurance: [Paterson et al. (2025)](https://doi.org/10.1016/j.ress.2025.111311) | Develops AMLAS as a process for constructing evidence-backed ML safety cases. | Supplies assurance logic, artifact discipline, assumptions, and uncertainty treatment. | Assures development and deployment of ML components; public-incident reconstruction is outside its scope. |

## Pressure-test additions

| ID | Stream and source | What it contributes | Relationship to this paper | Boundary or difference |
|---|---|---|---|---|
| L16 | Human accident reconstruction: [Dekker (2002)](https://doi.org/10.1016/S0022-4375(02)00032-4) | Develops a method for reconstructing human contributions inside the event sequence and warns against hindsight-driven counterfactual judgments. | Directly constrains any claim that traceable reconstruction of human action is new. | Does not operationalize a formal-authority-to-effect evidence chain for AI governance. |
| L17 | Sociotechnical AI failure analysis: [Macrae (2022)](https://doi.org/10.1111/risa.13850) | Systematically analyzes public investigative reports on the Uber automated-driving fatality and develops five sociotechnical risk domains. | Demonstrates that public-report reconstruction of autonomous-system failure already supports method development. | Analyzes sociotechnical sources of risk, not documentary support for practical human control. |
| L18 | Human-control assurance: [McDermid (2019)](https://www.york.ac.uk/assuring-autonomy/news/blog/human-control-ai-autonomy/) | Connects effective intervention to time, independent knowledge, skills, and assurance. | Closely anticipates several conditions in the practical-control chain. | Supplies design and assurance guidance without a frozen retrospective case procedure. |
| L19 | Open-source AI incident classification: [Pittaras and McGregor (2023)](https://ceur-ws.org/Vol-3381/17.pdf) | Classifies goals, methods, technologies, and possible failure causes from incomplete public incident reports. | Shows that expert classification under open-source uncertainty is established in AI-incident research. | Targets technical failure causes and taxonomy development, not human-control propositions. |
| L20 | AI incident-reporting design: [Wei and Heim (2026)](https://doi.org/10.1609/aaai.v40i44.41139) | Compares nine safety-sector reporting systems and defines institutional design choices for general-purpose AI incident reporting. | Supports the paper's proposed recordkeeping implications and reporting context. | Designs reporting systems without reconstructing practical control in individual incidents. |
| L21 | AI-loss evidence reconstruction: [Leung et al. (2026)](https://arxiv.org/abs/2606.03777) | Introduces control boundary, evidence reconstruction, and insurance response for agentic AI losses using public examples. | Shares the language of control boundaries, reconstructed state, and claim-grade evidence. | Centers insurance recovery and current generative or agentic systems. Human practical control is not its assessed chain. |
| L22 | LLM prompt forensics: [Ledjaki et al. (2026)](https://doi.org/10.1145/3774905.3795469) | Proposes tamper-resistant prompt identifiers, replay, investigation, and chain-of-custody records for LLM incidents. | Constrains claims about originality in evidence preservation, replay, and forensic traceability. | Focuses on prompt traces and model behavior, not institutional human authority. |
| L23 | AI incident infrastructure: [McGregor (2021)](https://doi.org/10.1609/aaai.v35i17.17817) | Defines the AI Incident Database as shared infrastructure for collecting and learning from public failures. | Supplies the origin and limits of the candidate collection used by this repository. | Catalogs incidents without making claim-level practical-control assessments. |
| L24 | Autonomous research verifiability: [Meng et al. (2026)](https://doi.org/10.48550/arXiv.2605.26340) and [generated artifacts](https://github.com/scientist-one/generated-artifacts) | Defines Chain-of-Evidence, ScientistOne, and four uniform post-hoc integrity checks; publishes generated papers and solution code. | Directly constrains originality claims for claim traceability, evidence-preserving workflows, score and reference verification, and method-code alignment. | Studies autonomous research outputs. It does not assess practical human control, claim-specific historical evidence fitness, or conclusion dependency closure in public governance cases. |

## Provisional synthesis

The literature establishes five propositions relevant to the manuscript:

1. Human presence or formal authority is not sufficient for meaningful control.
2. Practical control depends on system design, human ability, information, context, and institutional arrangements.
3. Human performance under automation is conditional and can degrade when oversight becomes rare, compressed, or poorly supported.
4. Incident analysis requires records capable of testing alternative causal explanations.
5. Assurance claims require structured arguments, traceable evidence, assumptions, and uncertainty.

The proposed paper's remaining contribution is narrower than PR #11 stated. Prior work already supplies control conditions, retrospective reconstruction, public AI-incident analysis, assurance logic, evidence reconstruction, forensic traceability, claim-level evidence chains, and post-hoc integrity checks. The unresolved hypothesis concerns a governance-specific combination: a protocol fixed before screening, a preserved selection path, versioned public evidence packets, categorical missingness, a declared chain from information access through effect, claim-specific evidence fitness, and conclusion dependency closure.

## Search expansion required

Before a novelty claim is permitted, expand the review across:

- Scopus or Web of Science;
- IEEE Xplore and ACM Digital Library;
- PhilPapers;
- HeinOnline or an equivalent legal database;
- backward references from L01, L02, L04, L06, L10, L12, L14, and L15;
- forward citations to those same sources;
- terms combining `meaningful human control`, `human oversight`, `incident reconstruction`, `assurance case`, `formal authority`, `practical control`, `contestability`, `override`, and `evidence traceability`.

Record databases, dates, complete search strings, duplicate treatment, inclusion decisions, and inaccessible results.

The [literature search log](literature-search-log.md) records the open-web pilot. The [novelty audit](novelty-audit.md) defines the current rejection test and the work that remains.
