# Next Evidence Gates, v0.10.0

**Status:** `OPEN`  
**Decision owner:** Mark Julius Banasihan  
**Source release:** `v0.9.0`

## Decision

The next research cycle addresses support and search coverage before the manuscript makes a stronger contribution claim. The case question and the three frozen topics remain unchanged.

## Gate state

| Gate | Population | Complete | Open | Current state |
|---|---:|---:|---:|---|
| Close-source full-text verification | 27 | 27 terminal | 0 | `CLOSED` |
| Inaccessible-record retrieval | 1087 | 107 | 980 | `OPEN` |
| Authenticated and disciplinary interfaces | 5 | 0 | 5 | `OPEN` |
| Independent assessment | 1 study | 0 | 1 | `OPEN`, outside this cycle |

## Residual-risk sample

The sample is frozen before retrieval with 284 selected records: 102 forward citations, 177 backward references, and 5 direct-query records. Retrieval outcomes are recorded for 107 of 284 sampled records. Recovered content requires screening for 76 records; 75 decisions are recorded and 1 remains open. Frozen membership establishes selection lineage. The current partial result supplies no prevalence, exhaustive-coverage, or originality finding.

## Direct-query tranche

The five-record direct-query stratum has 5 retrieval outcomes, 4 bounded screening decisions, and 1 open decision. One screened record is `retain-close` and remains limited to its abstract until full text is inspected. The [tranche report](direct-query-retrieval-tranche-v0.11.0.md) and [machine-readable evidence record](data/direct-query-retrieval-evidence-v0.11.0.json) preserve the route, basis, decision, and limit for each record.

## Forward-citation tranche

All 102 records in the frozen forward-citation stratum have a retrieval outcome. The pass recovered full text for 34 records and abstracts for 37 records. It recorded 26 metadata-only outcomes, 2 unavailable outcomes, and 3 duplicates. All 71 recovered-content records now have an author-authorized, AI-assisted screening decision: 13 close, 22 background, 11 single-component exclusions, and 25 topic exclusions. Screening closes corpus membership for this tranche. The 13 close sources still require proposition-level review before they can support manuscript claims.

## Claim controls

1. A title-and-abstract review can support a bounded description of a source's declared purpose, model, or result.
2. A proposition that exceeds the abstract requires a verified full-text locator and proposition-specific support check.
3. A risk sample of inaccessible records can estimate residual coverage risk. It cannot establish exhaustive retrieval.
4. An authenticated-interface access failure remains visible and leaves the originality exception open.
5. Internal validation can test reproducibility and corruption detection. It cannot establish independent reliability or field validity.

## Current finding

The 89-decision author gate resolved the original screening queue. The retained-close full-text gate is closed with 22 verified sources, 3 abstract-only sources quarantined from stronger use, 0 exclusions after full-text review, and 2 inaccessible sources. Gate 2 has recorded 107 retrieval outcomes and leaves 980 records unresolved. Its recovered content has 75 decisions and 1 open decision. The 14 close sources recovered through this risk sample remain outside manuscript propositions until their separate source-review gates close.
