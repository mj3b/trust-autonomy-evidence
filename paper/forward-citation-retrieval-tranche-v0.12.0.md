# Forward-Citation Retrieval Tranche, v0.12.0

**Status:** `RETRIEVAL_COMPLETE_SCREENING_OPEN`

**Decision owner:** Mark Julius Banasihan

**Retrieval date:** 11 August 2026  
**Frozen source sample:** [`inaccessible-risk-sample-v0.11.0.csv`](data/inaccessible-risk-sample-v0.11.0.csv)

## Problem

The manuscript cannot assess literature-coverage risk while 102 records in the frozen forward-citation stratum lack a recorded retrieval outcome. This tranche resolves that accounting problem. It does not decide which recovered sources belong in the paper.

Selection membership was fixed before retrieval. The pass does not change the three research topics, project question, publication cutoff, public cases, or released assessments.

## Results

| Retrieval outcome | Records | Share of tranche | What the state permits |
|---|---:|---:|---|
| Full text recovered | 34 | 33.3% | Author screening; later proposition-level review if retained |
| Abstract recovered | 37 | 36.3% | Author screening and abstract-bounded description |
| Metadata only | 26 | 25.5% | Identification and access accounting only |
| Duplicate | 3 | 2.9% | Version reconciliation; no separate screening record |
| Unavailable | 2 | 2.0% | Coverage limit only |
| **Total** | **102** | **100.0%** | Retrieval accounting complete |

The retrieval pass recovered source content for 71 records. Those records now form an author queue. Every row begins with no screening decision and no permission to support a manuscript claim.

## What the result establishes

1. Every record in the frozen forward-citation stratum has a dated outcome and locator.
2. Seventy-one records have enough source content for author screening.
3. Twenty-eight records remain limited to metadata or an unavailable state.
4. Three records resolve to duplicate versions and remain visible in the evidence record.

## What the result does not establish

- It does not show that any newly recovered record is close, background, or out of scope.
- It does not show that the paper's contribution is original.
- It does not establish exhaustive coverage of the 1,087-record inaccessible population.
- It does not establish the frequency of close sources in the full population.
- It does not establish independent reliability, field validity, or institutional effects.

## Access findings

Publisher access state and scholarly relevance proved to be separate questions. Several DOI routes exposed readable abstracts. Others ended at purchase pages, security checks, or metadata-only landings. Two title records still yielded too little information to identify and screen the underlying work. These states remain visible because treating an access failure as a topic exclusion would understate uncertainty.

Three records required version reconciliation. Duplicate handling matters because counting a preprint, conference version, and published article as separate findings can inflate apparent coverage without adding independent evidence.

## Evidence path

The [machine-readable evidence record](data/forward-citation-retrieval-evidence-v0.12.0.json) preserves the route, source observation, review basis, assistance disclosure, and claim limit for each selected record. The [author queue](data/forward-citation-author-review-queue-v0.12.0.csv) contains the 71 recovered-content records. The [population ledger](data/inaccessible-record-retrieval-v0.10.0.csv) now records 107 outcomes across the direct-query and forward-citation tranches.

The validator checks frozen membership, count agreement, unique record keys, outcome vocabulary, locator presence, ledger agreement, queue membership, decision ownership, and claim permission. A recovered record without a decision must retain an `OPEN:` note.

## Source limits carried forward

The two direct-query limits remain open. RS-DQ-004 renders as a publisher PDF without a usable text layer in the checked channel. RS-DQ-005 exposes a publisher abstract while the article remains behind purchase or institutional access. The forward pass does not resolve or conceal either limit.

## Next decision

Mark Julius Banasihan must screen the 71 recovered-content records under the frozen v0.7 rules. Only author-retained records may move to the literature matrix. Any source used for a proposition beyond its abstract must then pass the existing full-text and proposition-support controls.
