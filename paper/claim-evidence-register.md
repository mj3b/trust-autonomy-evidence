# Manuscript Claim-Evidence Register

## Rule

This register distinguishes planned manuscript claims from the evidence that may support them. A claim remains provisional until the cited source has been checked and the final sentence appears in the manuscript with the same scope.

| ID | Planned claim | Class | Evidence path | Present state | Excluded interpretation |
|---|---|---|---|---|---|
| C01 | Formal human presence or authority does not by itself establish meaningful control. | Literature synthesis | L01, L02, L06, L10 in [`literature-matrix.md`](literature-matrix.md) | Supported as a literature proposition | Human oversight always fails. |
| C02 | The candidate selection rules were fixed before screening, and the first eligible case in each stratum was selected. | Direct repository record | [Protocol](../protocols/public-case-reconstruction-protocol.md); [selection register](../cases/public-case-selection-register.md) | Supported | The case comparison independently validates discrimination among states. |
| C03 | Formal authority is supported in all three public-case assessments. | Cross-case observation | [Cross-case report](../reports/public-case-reconstruction-v0.3.0.md); three packet assessments under [`cases/`](../cases/) | Supported within the packets | Formal authority was equivalent across institutions or system designs. |
| C04 | The released Oko assessment classifies access, comprehension, authority, feasible challenge, exercised challenge, and protective effect as supported. | Packet assessment result | [TAE-PUB-001](../cases/TAE-PUB-001-oko-1983/); [Figure 2 derivation](../reports/figure-methods.md) | Released result; protocol-consistency review required | The classifications satisfy the protocol's contemporaneous-evidence rule, establish the sole cause of the ultimate outcome, or transfer to other systems. |
| C05 | ZG710 supports formal authority. Comprehension, feasible challenge, exercised challenge, and effect are unsupported. | Packet assessment result | [TAE-PUB-002](../cases/TAE-PUB-002-patriot-zg710-2003/); [cross-case report](../reports/public-case-reconstruction-v0.3.0.md) | Supported within the packet | Any individual operator was legally or morally culpable. |
| C06 | The F/A-18C packet supports formal authority. Comprehension, feasible challenge, and exercised challenge remain indeterminate. | Packet assessment result | [TAE-PUB-003](../cases/TAE-PUB-003-patriot-fa18-2003/); [cross-case report](../reports/public-case-reconstruction-v0.3.0.md) | Supported within the packet | The unresolved stages factually failed. |
| C07 | An explicit indeterminate state prevents missing public records from being converted into negative factual findings. | Method inference | [Protocol missing-data rule](../protocols/public-case-reconstruction-protocol.md); C06 | Supported as a method property | The method establishes that the missing records never existed. |
| C08 | The repository checks internal contract behavior, selection invariants, cross-case interactions, figure data, artifact integrity, claim gates, and negative controls. | Direct repository record | [Repository validator](../scripts/validate_repository.py); [CoE audit](../scripts/run_coe_integrity_audit.py); [audit report](../audits/v0.5.0/audit-report.md) | Supported for committed artifacts | Independent reliability, source truth, or field validity. |
| C09 | The method produced traceable, bounded, protocol-consistent assessment states for the three selected packets. | Bounded inference | C02 through C08; [cross-case report](../reports/public-case-reconstruction-v0.3.0.md); [v0.5 crosswalk](claim-crosswalk.md) | Blocked where it depends on C04 | General validity across AI systems or institutions. |
| C10 | Institutions seeking to substantiate practical control should preserve reviewer information, timing, system state, independent evidence, authority, available interventions, action, and effect. | Proposed institutional implication | C03 through C07; L06, L10, L12, L14, L15 | To be argued | Maintaining these records guarantees safe or compliant outcomes. |
| C11 | The case set supplies no prevalence, causal-effect, inter-rater, legal-responsibility, or current-system transfer estimate. | Design limitation | [Cases claim boundary](../cases/README.md); [protocol](../protocols/public-case-reconstruction-protocol.md); [figure methods](../reports/figure-methods.md) | Supported | The cases have no descriptive or methodological value. |
| C12 | Oko and Patriot entered the case set under a functional, historically neutral AI-system definition covering machine-based inference and knowledge-based approaches. | Assessor classification | [OECD definition](https://doi.org/10.1787/623da898-en); [limitations](../LIMITATIONS.md); three packet reports | Supported as the repository's declared inclusion rule | The historical systems are architecturally equivalent to current learned models or agents. |
| C13 | The three strata were defined around pre-action intervention, incomplete evidence, and authority without practical force before screening. | Direct repository record | [Protocol](../protocols/public-case-reconstruction-protocol.md); [selection register](../cases/public-case-selection-register.md) | Supported | The three cases independently test how often the method discovers those contrasts. |
| C14 | The Oko packet contains retrospective participant accounts and no located contemporaneous command log or official incident record. | Direct repository record | [Oko source manifest](../cases/TAE-PUB-001-oko-1983/source-manifest.json); [Oko report](../cases/TAE-PUB-001-oko-1983/case-report.md); [practical-control protocol](../protocols/practical-human-control-test.md) | Supported; resolution open | The released supported states automatically satisfy the written contemporaneity rule. |

## Drafting discipline

- Cite packet evidence for case observations.
- Cite literature for general propositions.
- Label the author's classifications and comparisons as assessor inference.
- Use `indeterminate` when missing evidence blocks a finding.
- Do not use a documented outcome as proof of a complete causal explanation.
- Describe released assessment states as procedure outputs until their validity has been tested independently.
- Preserve `PAPER-BLOCKER-01` until the Oko contemporaneity mismatch receives a versioned resolution.
- Recheck this register whenever the abstract, results, or conclusion changes.
