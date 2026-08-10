# Formal Search and Citation-Chain Record, v0.7.0

**Author:** Mark Julius Banasihan

**Retrieval date:** 9 August 2026

**Publication cutoff:** 9 August 2026
**Status:** Machine retrieval complete within declared index limits; author screening remains open

## Result

The frozen Semantic Scholar search returned 184 records across eight query families. Full token paging was used for every direct query. Backward and forward chain requests returned 2,482 records for fourteen resolved seeds. The L12 DOI returned `404` for both Semantic Scholar chain endpoints. After deduplication, the combined pool contains 2,431 records.

The numbers describe index retrieval. They do not establish that every record is eligible, accessible, or substantively relevant. They also do not establish that the literature is exhausted.

## Direct-search completion

| Query | Executed Semantic Scholar syntax | Returned records | Pages |
|---|---|---:|---:|
| F01 | `"meaningful human control" +(evidence \| assessment \| operationalization \| assurance)` | 75 | 1 |
| F02 | `"effective human oversight" +(evidence \| performance \| audit \| evaluation \| compliance)` | 24 | 1 |
| F03 | `("human oversight" \| "human control") +("incident reconstruction" \| "accident reconstruction")` | 1 | 1 |
| F04 | `("formal authority" \| "human authority") +("practical control" \| override \| intervention \| contestability) +(automation \| "artificial intelligence" \| autonomous)` | 13 | 1 |
| F05 | `("AI incident" \| "algorithmic incident") +(reconstruction \| provenance \| "chain of custody" \| "missing evidence")` | 1 | 1 |
| F06 | `("assurance case" \| "assurance audit") +("human control" \| "human oversight")` | 2 | 1 |
| F07 | `("claim evidence" \| "chain of evidence") +("human control" \| "human oversight")` | 2 | 1 |
| F08 | `(indeterminate \| missingness) +("human oversight" \| "meaningful human control")` | 66 | 1 |

## Citation-chain completion

| Seed | Semantic Scholar identifier | References returned | Citations returned | Retrieval state |
|---|---|---:|---:|---|
| L01 | `DOI:10.3389/frobt.2018.00015` | 95 | 445 | Complete within index response |
| L02 | `DOI:10.1007/s43681-022-00167-3` | 110 | 99 | Complete within index response |
| L04 | `DOI:10.1007/s11948-025-00554-z` | 69 | 4 | Complete within index response |
| L06 | `DOI:10.1007/s43681-026-01147-7` | 58 | 3 | Complete within index response |
| L10 | `DOI:10.1016/j.clsr.2022.105681` | 151 | 216 | Complete within index response |
| L12 | `DOI:10.1609/aies.v8i1.36596` | 0 | 0 | Unresolved by Semantic Scholar; both endpoints returned `404` |
| L14 | `DOI:10.1007/s43681-022-00178-0` | 75 | 83 | Complete within index response |
| L15 | `DOI:10.1016/j.ress.2025.111311` | 0 | 21 | Complete index response; no references returned |
| L16 | `DOI:10.1016/S0022-4375(02)00032-4` | 0 | 301 | Complete index response; no references returned |
| L17 | `DOI:10.1111/risa.13850` | 212 | 76 | Complete within index response |
| L24 | `ARXIV:2605.26340` | 34 | 3 | Complete within index response |
| L25 | `DOI:10.1007/s11023-024-09701-0` | 113 | 50 | Complete within index response |
| L26 | `DOI:10.1007/978-3-032-07132-3_11` | 24 | 5 | Complete within index response |
| L27 | `DOI:10.1145/3630106.3658957` | 104 | 44 | Complete within index response |
| L28 | `ARXIV:2605.16278` | 87 | 0 | Complete index response; no citations returned |

## Cross-index check

Crossref resolved 22 of 25 DOI-bearing retained proposals. The unresolved records are two DataCite-issued arXiv identifiers and the Dagstuhl report DOI. Their official source records remain available. This is a metadata coverage difference.

OpenAlex resolved 13 of the 15 frozen seeds. It also resolved L12 and returned zero backward and forward links, which confirms that a record can resolve in one index while supplying no usable citation chain. The two arXiv seeds, L24 and L28, did not resolve through the tested OpenAlex URL form. Reference and citation counts differ between Semantic Scholar and OpenAlex for the resolved seeds. The repository treats those counts as dated index observations.

## Screening state

The [screening proposals](formal-search-screening-v0.7.0.md) classify all 2,431 records through a reproducible triage rule. The output proposes 12 close records, retains 13 records already present in the working matrix, marks 77 records for author attention because both control and evidence terms appear, and preserves 1,087 inaccessible records whose metadata lacks an abstract.

These are AI-assisted proposals. They cannot be used as final author screening decisions. The contribution statement remains bounded until Mark Julius Banasihan confirms the close set and reviews any exclusion capable of defeating the integration claim.

## Coverage limits

- Semantic Scholar supplied the controlling full-chain record. “Complete” means every page returned by that index, not every citation that exists.
- Scopus and Web of Science were not searched because authenticated access was not available in this environment.
- The Harvard library interface could not be reached because its host did not resolve in the controlled browser session.
- The machine triage cannot judge an inaccessible record's substantive overlap.
- Three records in the retrieved pool have indexed publication dates after the cutoff and are excluded from this review version.
- Citation indexes merge, omit, and split versions differently. Counts will change after the recorded retrieval time.

## Reproducibility files

- [`data/formal-search-v0.7.0.json`](data/formal-search-v0.7.0.json) preserves requests and returned metadata.
- [`data/formal-screening-proposals-v0.7.0.json`](data/formal-screening-proposals-v0.7.0.json) preserves one proposal for every deduplicated record.
- [`data/author-screening-queue-v0.7.0.csv`](data/author-screening-queue-v0.7.0.csv) isolates the 89 records that need an author decision.
- [`data/formal-metadata-verification-v0.7.0.json`](data/formal-metadata-verification-v0.7.0.json) preserves the Crossref and OpenAlex checks.
- [`../scripts/run_formal_literature_search.py`](../scripts/run_formal_literature_search.py) executes the frozen queries and chains.
- [`../scripts/propose_formal_search_screening.py`](../scripts/propose_formal_search_screening.py) generates reversible triage proposals.
- [`../scripts/verify_formal_search_metadata.py`](../scripts/verify_formal_search_metadata.py) repeats the metadata and coverage checks.
