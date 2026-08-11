# Literature Search Log

## Purpose

This log records the searches used to test whether the proposed paper duplicates an existing combination of meaningful human control, retrospective incident reconstruction, public evidence packets, explicit missingness, claim-level provenance, and executable artifact checks.

## Current scope

The 8 through 10 August 2026 sessions used exact-phrase queries, publisher pages, proceedings pages, institutional repositories, preprint records, Crossref, OpenAlex, and a frozen Semantic Scholar search. The formal search retrieved every page returned for eight query families and every returned citation page for fourteen resolved seeds. Mark Julius Banasihan completed the 89-record author queue. The search still falls short of a multidisciplinary systematic review because authenticated Scopus or Web of Science access, several disciplinary interfaces, and inaccessible-record review remain open.

## Formal v0.7 search

| ID | Date | Search surface | Query or operation | Result |
|---|---|---|---|---|
| F01--F08 | 2026-08-09 | Semantic Scholar Academic Graph bulk API | Eight frozen query families recorded in the [protocol](formal-literature-search-protocol-v0.7.0.md) | 184 records; every returned token page preserved. |
| C01 | 2026-08-09 | Semantic Scholar Academic Graph citations API | Backward and forward chains for 15 frozen seeds | 2,482 chain records for 14 resolved seeds; L12 returned `404` on both endpoints. |
| D01 | 2026-08-09 | Repository deduplication | DOI, then title and year | 2,431 deduplicated records in the combined pool. |
| S01 | 2026-08-09 | Reproducible machine triage | Six protocol decisions plus an outside-cutoff state | 12 `retain-close`, 13 `retain-background`, 77 author-attention records, 1,239 topic exclusions, 1,087 inaccessible records, and 3 outside-cutoff records proposed. These are not final author decisions. |
| V01 | 2026-08-09 | Crossref REST API | DOI lookup for 25 DOI-bearing retained proposals | 22 resolved; three DataCite or Dagstuhl records did not resolve through Crossref. |
| V02 | 2026-08-09 | OpenAlex Works API | Coverage comparison for 15 frozen citation seeds | 13 resolved; L12 resolved with zero indexed links; two arXiv URL-form seeds did not resolve. |
| I01 | 2026-08-09 | ACM proceedings, arXiv, Springer, MDPI, Oxford repository, Dagstuhl | Exact-title and DOI checks for proposed close sources | Verified publisher, proceedings, preprint, or institutional records for L29 through L41. |
| I02 | 2026-08-09 | Harvard library interface | Interface access attempt | Host did not resolve in the controlled browser session; no search result was claimed. |
| A01 | 2026-08-10 | Frozen 89-record author queue | Author review of 12 proposed close and 77 attention records | 27 retain close, 32 retain background, 20 exclude topic, and 10 exclude single component. All decisions record a rationale, review basis, source locator, author, date, and assistance disclosure. |
| R01 | 2026-08-11 | Frozen forward-citation risk stratum | DOI, publisher, repository, proceedings, and preserved-index routes for 102 selected records | 34 full-text, 37 abstract, 26 metadata-only, 3 duplicate, and 2 unavailable outcomes. Seventy-one recovered-content records await author decisions and have no claim permission. |

The [formal chain record](formal-citation-chain-v0.7.0.md) reports query strings, counts, errors, and coverage limits. The [screening proposal file](formal-search-screening-v0.7.0.md) separates machine triage from author judgment.

## Discovery queries

| ID | Date | Search surface | Query | Retained result or decision |
|---|---|---|---|---|
| Q01 | 2026-08-08 | Open web | `"meaningful human control" "incident" reconstruction autonomous systems` | Retained McDermid (2019); confirmed Tsamados et al. (2025) uses historical automation incidents as motivation. |
| Q02 | 2026-08-08 | Open web | `"human oversight" "incident analysis" artificial intelligence` | Confirmed Ezell et al. (2025) and located adjacent incident-reporting work. |
| Q03 | 2026-08-08 | Open web | `"human control" "assurance case" AI` | Retained McDermid (2019); confirmed overlap with assurance-case reasoning. |
| Q04 | 2026-08-08 | Open web | `"formal authority" "human control" automation` | No exact prior use of the paper's formal-authority and practical-control pairing was located. |
| Q05 | 2026-08-08 | Open web | `AI incident reconstruction method public records paper` | Retained Leung et al. (2026), Ledjaki et al. (2026), and Wei and Heim (2026). |
| Q06 | 2026-08-08 | Open web | `artificial intelligence incident investigation framework causal reconstruction paper` | Confirmed incident-analysis and public-report method overlap; no identical human-control chain was located. |
| Q07 | 2026-08-08 | Open web | `"formal authority" "practical human control"` | No exact match was located. This absence is not evidence of novelty. |
| Q08 | 2026-08-08 | Open web | `"immutable evidence" "meaningful human control" incident` | No work combining those exact terms was located. The paper has removed the overbroad word `immutable` for remote-only source content. |
| Q09 | 2026-08-08 | Open web | `"indeterminate" "human oversight" AI incident reconstruction` | Located related uses of indeterminacy, without the same retrospective evidence-state procedure. |
| Q10 | 2026-08-08 | Open web | `"claim-level provenance" AI incident` | Located adjacent provenance systems. No result used claim-level provenance to assess practical human control in a public incident packet. |
| Q11 | 2026-08-08 | Publisher and index pages | Exact titles and DOI strings for eight pressure-test additions | Metadata checked for L16 through L23. Full-text review status is recorded in the novelty audit. |
| Q12 | 2026-08-09 | arXiv and public GitHub artifacts | `Chain-of-Evidence ScientistOne integrity audit method code alignment` | Retained Meng et al. (2026) as L24 and inspected the public generated-papers and solution-code repository. |
| Q13 | 2026-08-09 | Open web and Crossref | `effective human oversight AI evidence performance testing` | Retained L25 and L26. |
| Q14 | 2026-08-09 | ACM and Crossref | `algorithmic assurance audit framework evidence criteria` | Retained L27. |
| Q15 | 2026-08-09 | arXiv | `effective human oversight framework architecture process documentation` | Retained L28. |
| Q16 | 2026-08-09 | OpenAlex | DOI searches for 12 declared seed works | Recorded index identifiers and counts in the [citation-chain log](citation-chain-log-v0.6.0.md). |
| Q17 | 2026-08-09 | OpenAlex | Forward-citation samples for L01, L02, L10, L14, and L16 | Inspected five highly cited returned titles per seed. No sampled title disclosed the complete method combination. The sample cannot support a novelty finding. |
| Q18 | 2026-08-09 | Semantic Scholar, ACM proceedings, Springer, Oxford repository, Dagstuhl, arXiv, and MDPI | Exact-title and DOI review of the formal-search close set | Added L29 through L41 and narrowed the integration language. |

## Inclusion rule

A result enters the working matrix when it addresses at least one of these functions:

1. defines conditions for meaningful or effective human control;
2. reconstructs human action or sociotechnical failure from retrospective records;
3. analyzes public AI incidents under missing or uncertain evidence;
4. specifies evidence preservation, chain of custody, replay, or claim-grade proof;
5. develops assurance arguments for AI or autonomous systems;
6. designs institutional incident reporting or recordkeeping;
7. preserves claim-level evidence chains or audits references, scores, specifications, and method-code alignment.

Search results that only used the same words for unrelated technical tasks were excluded. Commercial control products, unsourced commentary, and papers about AI-assisted physical crash reconstruction were not treated as near-neighbors.

## Remaining contribution gate

The open-index retrieval, selected Semantic Scholar citation chains, and 89-record author queue are complete within recorded index limits. The recovery ledger now records 107 of 1,087 inaccessible-record outcomes. Seventy-one recovered forward citations await author screening, and 980 population records still lack an outcome. Scopus or Web of Science, IEEE Xplore, ACM Digital Library, PhilPapers, and HeinOnline or an equivalent legal index remain open. The manuscript may state its bounded integration and may not state a novelty finding.
