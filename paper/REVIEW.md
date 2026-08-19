# Review the Current Paper

The current reviewer copy is **v0.16.0**:

**[Open the 30-page review PDF](preprints/preprints-compiled-v0.16.0.pdf)**

This PDF is the version to send to an external reviewer or prospective arXiv endorser. It contains the rebuilt explanation, six-stage event-control rule, three case results, current tables and figures, limitations, and author disclosures.

## For an arXiv endorser

arXiv describes endorsement as a check that the submitter belongs to the relevant research community and that the intended paper fits the subject area. It [does not treat endorsement as peer review](https://info.arxiv.org/help/endorsement.html#what-are-my-responsibilities-as-an-endorser). A prospective endorser can therefore begin with the PDF and this short category-fit summary:

- The paper studies the institutional conditions under which a human can detect, question, interrupt, and alter a consequential automated decision.
- It contributes a reproducible documentary method, deterministic decision rule, public evidence packets, and executable claim-integrity controls.
- Its proposed primary category is `cs.CY` because the research concerns the governance and institutional consequences of computing and automated decision systems.
- The paper declares its limits: three historical, purposively selected, single-assessor cases provide no prevalence, causal-effect, independent-reliability, or present-system transfer estimate.

An endorsement request should include the arXiv endorsement code, this PDF, the author's ORCID, and a concise explanation of subject-area fit. A request for detailed scholarly feedback should be stated separately.

## Version guide

| Location | Meaning | Use for current review? |
|---|---|---|
| [`preprints/preprints-compiled-v0.16.0.pdf`](preprints/preprints-compiled-v0.16.0.pdf) | Current paper | Yes |
| [`preprints/`](preprints/) | Current source, metadata, archive, and compile records | Yes, when source or provenance is relevant |
| [`arxiv/`](arxiv/) | Historical v0.14.0 arXiv-format package | No |
| [`archive/`](archive/) | Retired delivery packages | No |

The paper version and repository version answer different questions. The paper remains v0.16.0 because its claims and results have not changed. Later repository releases organize files, repair metadata, and strengthen validation around that paper.

## Evidence for a deeper review

The PDF is sufficient for a first reading. These records support a closer review:

| Review need | Record |
|---|---|
| See the paper in a browser with clickable references | [`manuscript-reader.md`](manuscript-reader.md) |
| Inspect the formal decision rule and case-level outputs | [`../assessments/event-control-results-v0.16.0.json`](../assessments/event-control-results-v0.16.0.json) |
| Trace material claims to their evidence | [`../evidence/claim-evidence-map.json`](../evidence/claim-evidence-map.json) |
| Inspect the integrity-audit result and exceptions | [`../audits/v0.16.0/audit-report.md`](../audits/v0.16.0/audit-report.md) |
| Review the declared contribution and limits | [`paper-charter.md`](paper-charter.md) |
| Inspect the rebuild decisions | [`revision-plan-v0.16.0.md`](revision-plan-v0.16.0.md) |

## Questions for substantive review

1. Does the six-stage rule measure practical control clearly enough to reproduce?
2. Does each case result follow from the released evidence states without crossing the stated inference boundary?
3. Does the manuscript explain its contribution relative to the closest oversight, incident-reconstruction, and evidence-chain research?
4. Are the institutional implications proportional to three purposively selected historical cases?
5. Which claim requires stronger evidence before journal submission?

The repository controls establish agreement among the declared manuscript, evidence records, formulas, figures, and executable checks. Independent review remains necessary for construct validity, source interpretation, external validity, and general significance.
