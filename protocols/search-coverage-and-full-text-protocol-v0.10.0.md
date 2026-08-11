# Search Coverage and Full-Text Verification Protocol, v0.10.0

**Author and decision owner:** Mark Julius Banasihan  
**Protocol date:** 11 August 2026  
**Status:** Frozen before new retrieval and full-text review  
**Source release:** `v0.9.0`

## Decision served

The author-screened manuscript cannot strengthen its contribution language while close sources remain supported only by titles and abstracts and 1,087 retrieved records remain substantively inaccessible. This protocol separates those problems and fixes the next review steps before results are known.

The three frozen research topics and the project question remain unchanged. This cycle tests literature support and coverage. It does not alter the public-case packets or estimate the method's institutional effects.

## Gate 1: retained-close full text

The v0.9 author ledger contains 27 `retain-close` decisions. Eight have a recorded full-text review basis. Nineteen have a `title_and_abstract` basis.

Each retained-close record receives one terminal state:

- `verified`: the inspected full text resolves to a stable locator, and the ledger records reviewer, date, notes, and AI-assistance disclosure;
- `abstract-only-not-used`: the full text remains unavailable and the source is quarantined from manuscript propositions that exceed its abstract;
- `excluded-after-full-text`: full-text inspection shows that the record does not satisfy the close-source rule;
- `inaccessible`: no eligible full text can be obtained after the declared retrieval steps.

`open` is a temporary state. A source passes the full-text gate only in the `verified` state. Verification permits proposition-specific checking. It does not establish that every statement in the source is true or applicable to this paper.

## Gate 2: inaccessible-record recovery

The population is the 1,087 records marked `inaccessible` in `paper/data/formal-screening-proposals-v0.7.0.json`. The released record keys and publication cutoff remain fixed.

Recovery follows this order:

1. resolve the DOI or stable title at the publisher;
2. check Crossref, OpenAlex, and Semantic Scholar for updated abstract or full-text locators;
3. check arXiv, conference proceedings, institutional repositories, and author manuscripts;
4. check Harvard HOLLIS or another lawful library route when ordinary public retrieval fails;
5. preserve the retrieval date, locator, outcome, decision owner, screening decision, and assistance disclosure.

Permitted retrieval outcomes are `abstract-recovered`, `full-text-recovered`, `metadata-only`, `duplicate`, `outside-cutoff`, and `unavailable`. Recovered content receives the v0.7 screening rules. The publication cutoff continues to govern record eligibility even when retrieval occurs later.

## Residual-risk sample

Deterministic recovery applies to the full 1,087-record population. When unresolved records remain, a reproducible risk sample will estimate the chance that the inaccessible set contains additional close sources.

The sample uses these rules:

1. assign each unresolved record to a primary origin stratum in this order: forward citation, backward reference, direct query;
2. select up to 284 records, allocated proportionally across nonempty strata;
3. within each stratum, order records by the SHA-256 digest of `TAE-v0.10-risk-sample|record_key` and select the lowest digests;
4. inspect every sampled record through the lawful retrieval routes above;
5. report stratum counts, recovery rates, close-source yield, and a confidence interval without replacing unavailable observations.

For a finite population of 1,087, a sample of 284 corresponds to an approximate 95% worst-case margin of five percentage points under simple random sampling before nonresponse. The sample measures residual risk. It cannot establish exhaustive coverage. When fewer than 284 records remain unresolved, every remaining record enters the sample.

## Gate 3: authenticated and disciplinary interfaces

The five declared surfaces are:

1. Scopus or Web of Science;
2. ACM Digital Library;
3. IEEE Xplore;
4. PhilPapers;
5. HeinOnline or Harvard HOLLIS.

Each interface uses the eight frozen v0.7 concept families with syntax adapted to that interface. The log preserves the exact query, access condition, search date, displayed result count, exported or screened record count, deduplication result, and author decisions. The search applies no relevance-ranked stopping rule inside a returned query set.

An interface can record `complete`, `access-failure`, or `open`. An access failure documents procedure and leaves the originality exception open. All five interfaces must reach `complete` before authenticated coverage can support closure of that exception.

## Independent-assessment boundary

These three gates are author-controlled and can proceed without volunteer reviewers. They strengthen source support, coverage accounting, and reproducibility. Independent reliability remains a separate open proposition. Internal checks and clean-room software runs cannot convert a single-assessor study into an independent assessment.

## Completion and claim rules

The next manuscript checkpoint requires:

1. zero open records in the 27-source full-text ledger;
2. a recorded retrieval outcome for each of the 1,087 inaccessible records, plus the residual-risk analysis when unavailable records remain;
3. a complete result for each of the five authenticated or disciplinary interfaces;
4. an updated literature matrix, novelty audit, sentence-level support register, claim map, and limitations section;
5. an executable check that blocks substantive use of an unverified full-text source;
6. continued disclosure that independent reliability, field validity, institutional effectiveness, and exhaustive originality remain unresolved unless new evidence closes those propositions.

## Change rule

Any change to the population, sample rule, terminal states, interface set, or claim boundary requires a dated protocol amendment. The amendment must identify the reason, affected records, manuscript effect, and remaining uncertainty.
