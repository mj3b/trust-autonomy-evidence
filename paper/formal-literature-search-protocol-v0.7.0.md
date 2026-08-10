# Formal Literature Search Protocol, v0.7.0

**Author:** Mark Julius Banasihan  
**Protocol date:** 9 August 2026  
**Status:** Frozen before retrieval  
**Repository base:** `v0.6.0`, commit `cccd272f7ef471ca5a4bcd4c1f7ee4ec18e49e85`

## Decision served

The paper cannot state a defensible contribution until a reproducible search tests whether prior work already supplies the same method. This protocol fixes the search and screening rules before new records are inspected.

The review asks:

> Does prior work disclose a method that joins protocol fixation before screening, visible case selection, versioned public evidence packets, categorical missingness, a practical-human-control chain, claim-specific evidence fitness, conclusion dependency closure, versioned correction, and executable artifact checks?

The search tests substantial equivalence. Different terminology does not protect the contribution claim when the underlying mechanism is the same.

## Search cutoff and eligible record types

The publication cutoff is 9 August 2026. Eligible records include journal articles, conference papers, scholarly books or chapters, standards, institutional research reports, and preprints. A record must have an English title and abstract or accessible English full text for substantive screening.

News, marketing pages, course materials, unsourced commentary, and records without enough content to judge relevance are excluded. An inaccessible scholarly record remains in the log with an `inaccessible` decision.

## Search surfaces

The reproducible indexed search uses:

1. Semantic Scholar Academic Graph bulk search for title and abstract retrieval;
2. Crossref REST API for DOI and bibliographic verification;
3. OpenAlex for forward and backward citation comparison when an indexed seed is present.

The disciplinary interface check covers ACM Digital Library, IEEE Xplore, PhilPapers, and HeinOnline or Harvard HOLLIS. Scopus and Web of Science are recorded separately when authenticated access is available. Interface results are logged with the exact query, displayed result count, access condition, and screening decision.

Coverage differs across indexes. Agreement among indexes increases retrieval confidence. It does not prove that the search found every relevant work.

## Frozen query families

The executable search preserves the exact API syntax. The conceptual families are:

| ID | Search concepts |
|---|---|
| F01 | `"meaningful human control"` with evidence, assessment, operation, or assurance |
| F02 | `"effective human oversight"` with evidence, performance, audit, evaluation, or compliance |
| F03 | human oversight with incident or accident reconstruction |
| F04 | formal or human authority with practical control, override, intervention, or contestability in automated systems |
| F05 | AI or algorithmic incidents with reconstruction, provenance, chain of custody, or missing evidence |
| F06 | assurance cases or assurance audits with human control or oversight |
| F07 | claim-evidence or chain-of-evidence methods with human control or oversight |
| F08 | indeterminate states or missingness in human-control and oversight assessment |

No relevance-ranked stopping rule is allowed inside a returned query set. The search retrieves every record supplied by the API for each frozen query through its continuation token. Rate limits, service failures, and index caps are recorded.

## Deduplication

Records are deduplicated in this order:

1. normalized DOI;
2. normalized title plus publication year;
3. normalized title when one index omits the year;
4. manual review of preprint and published-version pairs.

The published version controls when its content matches the preprint. Both identifiers remain in the record when version history affects interpretation.

## Screening rules

Title and abstract screening assigns one of six decisions:

- `retain-close`: overlaps at least two listed method elements or directly threatens the integration claim;
- `retain-background`: supplies a material construct, mechanism, or method already used by the paper;
- `exclude-single-component`: covers one familiar component without changing the paper's contribution boundary;
- `exclude-topic`: concerns another subject despite term overlap;
- `exclude-record-type`: fails the eligible record rule;
- `inaccessible`: available metadata cannot support a substantive decision.

Full-text review is required before a new source can support a manuscript claim that exceeds its abstract. Abstract-only records may support a bounded statement about the source's declared purpose, model, or result.

## Citation chaining

Backward references and forward citations will be retrieved for these fifteen seeds:

`L01`, `L02`, `L04`, `L06`, `L10`, `L12`, `L14`, `L15`, `L16`, `L17`, `L24`, `L25`, `L26`, `L27`, and `L28`.

The machine record retains every reference and citation returned by the selected index. Screening uses the same six decisions. A missing index record, truncated citation set, or inaccessible source is recorded as a coverage limit.

## Contribution decision rule

The integration claim fails when one prior method supplies all nine tested elements or supplies a substantially equivalent mechanism. Partial overlap narrows the paper's language and must enter the literature matrix.

The search can support a bounded contribution statement when:

1. every frozen query completed or has a recorded access failure;
2. duplicates and screening decisions are preserved;
3. all fifteen seed chains completed within declared index limits;
4. every `retain-close` record received abstract or full-text review;
5. the novelty audit explains the closest remaining neighbor;
6. the manuscript uses contribution language consistent with the recorded search limits.

This protocol cannot establish universal originality. It can show that a declared search did or did not locate a substantially equivalent method by the cutoff date.

## Authorship and assistance

Mark Julius Banasihan owns the search decisions, source interpretations, and manuscript claims. AI assistance may retrieve metadata, normalize records, propose screening candidates, and check consistency. The machine-generated candidate set is evidence for review activity. It is not a human judgment and cannot close the contribution decision by itself.
