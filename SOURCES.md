# Source Register

The source register identifies the contribution each source makes to the model. Inclusion does not imply endorsement of every claim in the source.

| Source | Contribution used in this repository |
|---|---|
| [NIST AI RMF: Trustworthiness Characteristics](https://airc.nist.gov/airmf-resources/airmf/3-sec-characteristics/) | Defines multiple context-sensitive characteristics of trustworthy AI and treats validity and reliability as foundational |
| [NIST AI RMF Core](https://airc.nist.gov/airmf-resources/airmf/5-sec-core/) | Connects governance to documented validity, residual risk, safe failure, monitoring, and system limits |
| [Lee and See, Trust in Automation](https://pubmed.ncbi.nlm.nih.gov/15151155/) | Frames appropriate reliance and calibration as design objectives for human use of automation |
| [European Union Artificial Intelligence Act, Article 14](https://eur-lex.europa.eu/eli/reg/2024/1689/oj?locale=en) | Connects oversight to competence, authority, interpretation, override, reversal, interruption, autonomy, risk, and context |
| [GovAI, Measuring AI Agent Autonomy](https://www.governance.ai/research-paper/measuring-ai-agent-autonomy-towards-a-scalable-approach-with-code-inspection) | Develops code-inspection methods and identifies impact and oversight attributes |
| [GovAI, Visibility into AI Agents](https://www.governance.ai/research-paper/visibility-into-ai-agents) | Identifies agent identifiers, activity logs, and real-time monitoring as governance infrastructure |
| [GovAI, Evaluating Offline Monitoring](https://www.governance.ai/research-paper/evaluating-offline-monitoring-of-internal-ai-agents) | Extends monitor evaluation across coverage, filtering, human review, escalation, and detection delay |
| [GovAI, Incident Analysis for AI Agents](https://www.governance.ai/research-paper/incident-analysis-for-ai-agents) | Connects incident reconstruction to system, contextual, cognitive, access, tool, log, and documentation evidence |
| [GovAI, Frontier AI Auditing](https://www.governance.ai/research-paper/frontier-ai-auditing-toward-rigorous-third-party-assessment-of-safety-and-security-practices-at-leading-ai-companies) | Defines organization-level audit needs, qualified assessors, assurance levels, and secure access to non-public evidence |
| [GovAI, ASPIRE](https://www.governance.ai/research-paper/towards-publicly-accountable-frontier-llms) | Defines conditions for external scrutiny through access, searching attitude, proportionality, independence, resources, and expertise |
| [METR, Measuring AI Ability to Complete Long Tasks](https://metr.org/time-horizons/) | Defines task difficulty using human completion time and documents domain and interpretation limits |
| [Anthropic Responsible Scaling Policy](https://www.anthropic.com/responsible-scaling-policy) | Provides an example of capability thresholds, safeguards, risk reports, external review, monitoring, incidents, and revision |
| [OpenAI Preparedness Framework](https://cdn.openai.com/pdf/18a02b5d-6b67-4cec-ab64-68cdfbddebcd/preparedness-framework-v2.pdf) | Provides an example of capability tracking, safeguard evaluation, risk thresholds, and deployment decision processes |
| [ScientistOne: Towards Human-Level Autonomous Research via Chain-of-Evidence](https://doi.org/10.48550/arXiv.2605.26340) | Supplies the prior architecture for claim traceability and four CoE Integrity Audit checks adapted in v0.5.0 and carried through the v0.14 source, manuscript, preprint, audit, and release path |
| [ScientistOne generated artifacts](https://github.com/scientist-one/generated-artifacts) | Makes generated papers and solution code available for source-level checks of scores, references, run types, and method-code alignment |
| [Langer, Baum, and Schlicker, Effective Human Oversight](https://doi.org/10.1007/s11023-024-09701-0) | Separates oversight sensitivity from response tendency and identifies task, system, and person factors |
| [Langer, Lazar, and Baum, Testing Human Oversight Compliance](https://doi.org/10.1007/978-3-032-07132-3_11) | Explains limits of checklist compliance and context-sensitive empirical oversight testing |
| [Lam et al., Assurance Audits of Algorithmic Systems](https://doi.org/10.1145/3630106.3658957) | Supplies a criterion-audit framework, external assurance model, scope discipline, and audit reporting structure |
| [Gaube et al., Keeping an Eye on AI](https://doi.org/10.48550/arXiv.2605.16278) | Supplies a broad effective-oversight definition, architecture, process model, and documentation template |

## Public-case sources

| Source | Contribution used in this repository |
|---|---|
| [OECD explanatory memorandum on the updated definition of an AI system](https://doi.org/10.1787/623da898-en) | Supplies a functional definition covering machine-based inference, predictions, recommendations, decisions, and knowledge-based approaches |
| [AI Incident Database snapshots](https://incidentdatabase.ai/research/snapshots/) | Supplies the first frozen candidate collection and incident-report relationships |
| [OECD AI Incidents and Hazards Monitor methodology](https://oecd.ai/en/incidents-methodology) | Supplies the second candidate collection's scope and inclusion method |
| [Chatham House, Too Close for Comfort](https://www.chathamhouse.org/sites/default/files/field/field_document/20140428TooCloseforComfortNuclearUseLewisWilliamsPelopidasAghlani.pdf) | Reconstructs the Oko warning chain and preserves uncertainty about higher-level counterfactual decisions |
| [UK Ministry of Defence, RAF Tornado ZG710 accident summary](https://assets.publishing.service.gov.uk/media/5a78e39b40f0b62b22cbd9a5/maas03_02_tornado_zg710_22mar03.pdf) | Supplies the primary public record for the classification, decision window, information gaps, launch, and loss |
| [U.S. Defense Science Board, Patriot System Performance](https://www.govinfo.gov/content/pkg/GOVPUB-D-PURL-LPS66633/pdf/GOVPUB-D-PURL-LPS66633.pdf) | Supplies official system-level findings about identification, situational awareness, automatic operation, operator control, and missing causal evidence |
| [U.S. Army Research Laboratory, Looking Back at 20 Years of MANPRINT on Patriot](https://www.govinfo.gov/content/pkg/GOVPUB-D101-PURL-gpo58824/pdf/GOVPUB-D101-PURL-gpo58824.pdf) | Supplies human-systems findings about automation bias, training, vigilance, residual operator roles, and reform |
| [U.S. Air Force, Friendly fire incidents will be investigated](https://www.af.mil/News/Article-Display/Article/139557/friendly-fire-incidents-will-be-investigated/) | Supplies a contemporaneous official record of the F/A-18C incident and investigation scope |
| [Washington Post, Investigation Finds U.S. Missiles Downed Navy Jet](https://www.washingtonpost.com/archive/politics/2004/12/11/investigation-finds-us-missiles-downed-navy-jet/323e76f1-31d5-49c1-a27a-df9f389b0532/) | Reports the Central Command sequence and the public summary's unexplained causal gap |

## Adjacent public artifacts

| Artifact | Relationship |
|---|---|
| [Governed Decision Intelligence](https://github.com/mj3b/governed-decision-intelligence) | Defines records for evidence, authority, alternatives, uncertainty, escalation, and downstream obligations |
| [Human Influence Telemetry](https://github.com/mj3b/human-influence-telemetry) | Defines a documentary assessment of whether formal human authority retained practical force |
| [CDFI Framework](https://github.com/mj3b/cdfi-framework) | Supplies an evaluation-governance case involving reliability gates and bounded publication claims |
| [CDCF Foundation Governance Frameworks](https://github.com/CatholicOS/foundation-docs) | Supplies an institutional governance context involving project vetting and human accountability criteria |
