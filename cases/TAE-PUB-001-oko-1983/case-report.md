# TAE-PUB-001: Oko False Launch Warning

## Decision

On 26 September 1983, the Oko warning system indicated that the United States had launched five intercontinental ballistic missiles. Duty officer Stanislav Petrov treated the signal as a false alarm and reported that judgment before the warning advanced as a confirmed attack.

This packet supports a bounded proposition about practical human control. Petrov received the output, understood its consequence, could challenge it, exercised that authority, and affected the decision path. The available evidence does not establish what senior Soviet leaders would otherwise have done.

## Boundary

The sequence begins when Oko classified incoming missiles and ends when Petrov reported the alert as false before escalation to a retaliatory launch decision. Later publicity and honors fall outside the boundary.

## Chronology

| Stage | Reconstructed event | Evidence | Provenance |
|---|---|---|---|
| Signal | Oko displayed a launch warning, followed by additional missile indications. | O2, O3, O4 | `source_claim` |
| Context check | Petrov compared the warning with the limited scale of the reported attack and the absence of confirmation from ground radar. | O2, O3, O4 | `direct_record` from retrospective interviews |
| Intervention | Petrov classified the warning as false and communicated that judgment to superiors. | O2, O3, O4 | `direct_record` from retrospective interviews |
| Effect | This warning did not advance as a confirmed attack report within the reconstructed chain. | O2, O3 | `source_claim` |
| Mechanism | Reflected sunlight on high-altitude clouds is reported as the source of the satellite error. | O2, O3 | `source_claim` |

## Search record

| Evidence class | Located | Boundary effect |
|---|---|---|
| System record | System name, warning function, and reported error mechanism | Supports functional identity; does not establish configuration or reliability |
| Context record | Retrospective accounts of the alert and command setting | Supports the main sequence |
| Access record | Reports of display access and ground-radar cross-checking | Supports access with incomplete monitoring coverage |
| Tool record | Public descriptions of Oko's satellite warning function | Supports functional classification under O5 |
| Log record | No public contemporaneous command log located | Prevents complete reconstruction and integrity testing |
| Documentation record | Independent reconstruction and primary interviews | Supports the bounded proposition with retrospective-source limits |

## Provenance ledger

| Statement | Classification | Evidence |
|---|---|---|
| Petrov received and rejected the alert before escalation. | `source_claim` supported by interview-derived records | O2, O3, O4 |
| The available sequence satisfies access, comprehension, authority, feasibility, exercise, and effect. | `assessor_inference` | O2, O3, O4 |
| Oko falls within the selected functional AI-system definition. | `assessor_inference` | O2, O3, O5 |
| A retaliatory launch would otherwise have occurred. | `unresolved` | No eligible public record |
| The official Soviet record corroborates the interviews. | `unresolved` | Official record unavailable |

## Assessment

The autonomy profile is narrow goal scope, recommendation authority, a single-step horizon, public impact, pre-action oversight, and partial reversibility. The full machine-readable determination appears in [`assessment.json`](assessment.json).

Practical control is supported through effect. Trust evidence remains weaker: reliability and uncertainty evidence are unsupported, record completeness is unsupported, and integrity is indeterminate.

## Supported proposition

A named duty officer received the Oko alert before escalation, challenged it with contextual and ground-radar evidence, classified it as false, and communicated that classification before the warning advanced to a retaliatory launch decision.

## Excluded conclusions

- The public record does not establish that senior Soviet leaders would otherwise have ordered a retaliatory launch.
- The public record does not support the counterfactual claim that one person saved the world.
- One successful intervention does not establish general system reliability, safety, or institutional effectiveness.

## Rights and missing evidence

The packet contains source metadata, short paraphrases, and original assessment. It does not redistribute copyrighted reports. Soviet command logs, the official incident record, and the investigation file were not located in a public archive. See [`source-manifest.json`](source-manifest.json) for provenance and preservation details.
