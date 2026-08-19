# Paper Workspace

This directory develops a methods and comparative-case paper from the repository's frozen public-case evidence. Version 0.16.0 rebuilds the explanation, formalizes the event-control decision rule, and derives one unresolved and two failing case-level results without changing the released case states. The v0.14.0 proposition gate remains controlling for source use: five sources have one bounded manuscript permission each, two remain background-only, and six are quarantined. Released case packets, assessments, and manifests remain the controlling research record.

**PR #11 merge commit:** [`a2a8db7a5a63fe09a2cdb48cb648c013c0d110ec`](https://github.com/mj3b/trust-autonomy-evidence/commit/a2a8db7a5a63fe09a2cdb48cb648c013c0d110ec)

**Base commit:** [`acd9333d55b33f4031c058d21f9662cdb7d47c6f`](https://github.com/mj3b/trust-autonomy-evidence/commit/acd9333d55b33f4031c058d21f9662cdb7d47c6f)

**Research question**

> How can a frozen, evidence-traceable assessment procedure represent formal human authority, practical human control, and unresolved evidence in a bounded public incident record?

## Paper map

| File | Short description |
|---|---|
| [`paper-charter.md`](paper-charter.md) | Fixes the paper type, question, contribution, audience, and claim boundary. |
| [`revision-plan-v0.16.0.md`](revision-plan-v0.16.0.md) | Freezes the reader-first rebuild, formal decision rules, terminology changes, open evidence gates, and rejection conditions. |
| [`manuscript.md`](manuscript.md) | Preserves the auditable manuscript source with Pandoc citation identifiers. |
| [`manuscript-reader.md`](manuscript-reader.md) | Presents the same manuscript with clickable author-year citations and a rendered reference list for GitHub readers. |
| [`manuscript-pressure-test-v0.8.0.md`](manuscript-pressure-test-v0.8.0.md) | Records citation, count, claim, coding-stability, ethics, and submission-gate findings and their resolutions. |
| [`review-record-v0.8.0.md`](review-record-v0.8.0.md) | Records author authorization, reviewed additions, support decisions, and the publication boundary. |
| [`tables.md`](tables.md) | Preserves exact assessment states, search counts, correction history, captions, and interpretation notes. |
| [`tables/manuscript-tables.tex`](tables/manuscript-tables.tex) | Provides journal-ready `booktabs` fragments with three horizontal rules and no vertical rules. |
| [`literature-matrix.md`](literature-matrix.md) | Relates 60 working sources to the proposed contribution and its boundaries. |
| [`literature-search-log.md`](literature-search-log.md) | Records discovery queries, dates, retained candidates, and search limits. |
| [`formal-literature-search-protocol-v0.7.0.md`](formal-literature-search-protocol-v0.7.0.md) | Freezes the formal search, screening, deduplication, and citation-chain rules before retrieval. |
| [`formal-citation-chain-v0.7.0.md`](formal-citation-chain-v0.7.0.md) | Reports the eight direct queries, fifteen seed chains, second-index checks, errors, and coverage limits. |
| [`formal-search-screening-v0.7.0.md`](formal-search-screening-v0.7.0.md) | Summarizes preliminary machine triage and the author-confirmation gate. |
| [`data/author-screening-queue-v0.7.0.csv`](data/author-screening-queue-v0.7.0.csv) | Presents the 12 close-source proposals and 77 attention records for author decisions and notes. |
| [`data/author-screening-decisions-v0.8.0.csv`](data/author-screening-decisions-v0.8.0.csv) | Preserves the blank decision ledger at the v0.8 checkpoint. |
| [`data/author-screening-gate-v0.8.0.json`](data/author-screening-gate-v0.8.0.json) | Preserves the open 89-record gate state published at the v0.8 checkpoint. |
| [`data/author-screening-decisions-v0.9.0.csv`](data/author-screening-decisions-v0.9.0.csv) | Records all 89 author decisions, rationales, review bases, source locators, and the AI-assistance disclosure. |
| [`data/author-screening-gate-v0.9.0.json`](data/author-screening-gate-v0.9.0.json) | Records the closed author gate and final decision counts used by Figure 5 and the v0.9 audit. |
| [`review-record-v0.9.0.md`](review-record-v0.9.0.md) | Records author accountability for the final screening state and its publication boundary. |
| [`author-screening-completion-gate.md`](author-screening-completion-gate.md) | Shows completed and open author decisions and defines when final search-flow language becomes eligible. |
| [`next-evidence-gates-v0.10.0.md`](next-evidence-gates-v0.10.0.md) | Reports the full-text, inaccessible-record, authenticated-interface, and independence gate states. |
| [`data/close-source-full-text-gate-v0.10.0.csv`](data/close-source-full-text-gate-v0.10.0.csv) | Records one full-text state for each of the 27 retained-close sources. |
| [`data/inaccessible-record-retrieval-v0.10.0.csv`](data/inaccessible-record-retrieval-v0.10.0.csv) | Receives retrieval outcomes and author decisions for the frozen 1,087-record inaccessible population. |
| [`inaccessible-risk-sample-v0.11.0.md`](inaccessible-risk-sample-v0.11.0.md) | Explains why the 284-record sample was frozen before retrieval and defines its interpretation boundary. |
| [`data/inaccessible-risk-sample-v0.11.0.csv`](data/inaccessible-risk-sample-v0.11.0.csv) | Records the 284 selected records with strata, digests, ranks, origins, and source metadata. |
| [`data/inaccessible-risk-sample-v0.11.0.json`](data/inaccessible-risk-sample-v0.11.0.json) | Stores the population hash, seed, allocation method, counts, sample hash, and claim boundary. |
| [`direct-query-retrieval-tranche-v0.11.0.md`](direct-query-retrieval-tranche-v0.11.0.md) | Reports five retrieval outcomes, four screening decisions, one open review, and the effect on the paper. |
| [`data/direct-query-retrieval-evidence-v0.11.0.json`](data/direct-query-retrieval-evidence-v0.11.0.json) | Preserves the checked routes, locators, review bases, source observations, decisions, assistance, and limits. |
| [`forward-citation-retrieval-tranche-v0.12.0.md`](forward-citation-retrieval-tranche-v0.12.0.md) | Reports 102 retrieval outcomes, 71 open author decisions, access limits, duplicates, and the next gate. |
| [`data/forward-citation-retrieval-evidence-v0.12.0.json`](data/forward-citation-retrieval-evidence-v0.12.0.json) | Preserves the route, outcome, source observation, review basis, assistance, and claim limit for every selected forward citation. |
| [`data/forward-citation-author-review-queue-v0.12.0.csv`](data/forward-citation-author-review-queue-v0.12.0.csv) | Holds the 71 recovered-content records with blank author decisions and no claim permission. |
| [`forward-citation-author-screening-protocol-v0.13.0.md`](forward-citation-author-screening-protocol-v0.13.0.md) | Freezes the order, permitted decisions, evidence rule, assistance boundary, and completion conditions before screening. |
| [`data/forward-citation-author-screening-decisions-v0.13.0.csv`](data/forward-citation-author-screening-decisions-v0.13.0.csv) | Records all 71 decisions, mechanism-specific rationales, review bases, source locators, ownership, assistance, and claim permissions. |
| [`data/forward-citation-author-screening-v0.13.0.json`](data/forward-citation-author-screening-v0.13.0.json) | Stores the frozen input hash, recomputed decision counts, zero-permission rule, and interpretation limits. |
| [`forward-citation-author-screening-v0.13.0.md`](forward-citation-author-screening-v0.13.0.md) | Reports the closed screening gate and the separate proposition-review boundary. |
| [`forward-citation-proposition-review-protocol-v0.14.0.md`](forward-citation-proposition-review-protocol-v0.14.0.md) | Freezes proposition-level locators, fitness decisions, permission states, limitations, reversal conditions, and completion rules. |
| [`data/forward-citation-proposition-review-v0.14.0.csv`](data/forward-citation-proposition-review-v0.14.0.csv) | Records all 13 source decisions, corrected identities, exact propositions, locators, fitness states, limits, and disclosures. |
| [`data/forward-citation-proposition-review-v0.14.0.json`](data/forward-citation-proposition-review-v0.14.0.json) | Stores the 5 manuscript-use, 2 background-only, and 6 quarantined composition. |
| [`forward-citation-proposition-review-v0.14.0.md`](forward-citation-proposition-review-v0.14.0.md) | Explains the permitted propositions, corrected identities, controls, and remaining boundary. |
| [`data/direct-query-resolution-v0.14.0.json`](data/direct-query-resolution-v0.14.0.json) | Closes RS-DQ-004 for screening while preserving zero source-content permission. |
| [`preprint-readiness-v0.14.0.md`](preprint-readiness-v0.14.0.md) | Separates completed evidence gates from author and arXiv submission decisions. |
| [`arxiv/`](arxiv/) | Preserves the historical v0.14.0 arXiv-format source, 25-page PDF, archive, metadata, and placement receipt. |
| [`preprints/`](preprints/) | Contains the v0.16.0 single-column LaTeX source, deterministic archive, 30-page compiled review PDF, metadata, and compile receipt. |
| [`../evidence/human-review-attestation-v0.11.0.json`](../evidence/human-review-attestation-v0.11.0.json) | Records author review of the five direct-query states and six added claims, with AI-assistance limits. |
| [`../evidence/human-review-attestation-v0.12.0.json`](../evidence/human-review-attestation-v0.12.0.json) | Records the 102-record workflow boundary and states that 71 source reviews remain pending. |
| [`../evidence/human-review-attestation-v0.13.0.json`](../evidence/human-review-attestation-v0.13.0.json) | Records author authorization, AI assistance, decision accountability, 71 completed decisions, and zero manuscript claim permissions. |
| [`../evidence/human-review-attestation-v0.14.0.json`](../evidence/human-review-attestation-v0.14.0.json) | Records author authorization and accountability for the proposition, direct-query, claim, audit, and preprint workflow. |
| [`../evidence/claim-evidence-map.json`](../evidence/claim-evidence-map.json) | Maps 40 material claims to exact evidence, fitness decisions, dependencies, limits, and reversal conditions. |
| [`../audits/v0.13.0/audit-report.md`](../audits/v0.13.0/audit-report.md) | Reports the 28-claim audit, 26 detected controls, four exceptions, and the proposition-review boundary. |
| [`../audits/v0.14.0/audit-report.md`](../audits/v0.14.0/audit-report.md) | Reports the 32-claim audit, 33 detected controls, five bounded source permissions, and four open exceptions. |
| [`../audits/v0.16.0/audit-report.md`](../audits/v0.16.0/audit-report.md) | Reports the 40-claim audit, 39 detected controls, and the remaining independent-validity and coverage exceptions. |
| [`data/authenticated-interface-searches-v0.10.0.csv`](data/authenticated-interface-searches-v0.10.0.csv) | Tracks the five authenticated and disciplinary-interface searches. |
| [`citation-chain-log-v0.6.0.md`](citation-chain-log-v0.6.0.md) | Records the index-based citation sample and its limits. |
| [`literature-support-audit-v0.6.0.md`](literature-support-audit-v0.6.0.md) | Preserves the 16-proposition audit for the earlier introduction and related-work draft. |
| [`literature-support-audit-v0.6.0.json`](literature-support-audit-v0.6.0.json) | Preserves the earlier manuscript locators and checked bibliography keys. |
| [`literature-support-audit-v0.7.0.md`](literature-support-audit-v0.7.0.md) | Explains the 21-proposition support audit for the full v0.4 draft. |
| [`literature-support-audit-v0.7.0.json`](literature-support-audit-v0.7.0.json) | Maps current material literature propositions to checked keys, review bases, and scope notes. |
| [`novelty-audit.md`](novelty-audit.md) | Tests the proposed contribution against the closest prior work located so far. |
| [`references.bib`](references.bib) | Stores checked citation metadata for the working literature set. |
| [`claim-evidence-register.md`](claim-evidence-register.md) | Maps planned manuscript claims to repository evidence and excluded interpretations. |
| [`submission-notes.md`](submission-notes.md) | Records authorship, disclosure, venue, and preprint decisions that remain open. |
| [`review-record-pr11.md`](review-record-pr11.md) | Records the pressure test of PR #11, its resolutions, and the remaining paper blocker. |
| [`claim-crosswalk.md`](claim-crosswalk.md) | Connects paper claims to the executable v0.6 gates and drafting consequences. |
| [`scientistone-artifact-pressure-test.md`](scientistone-artifact-pressure-test.md) | Records how ScientistOne constrains originality and changes evidence, run-type, and method-code controls. |

## Working rule

A manuscript statement is not treated as a supported research claim merely because it appears in the draft. Material claims must identify their source in the claim-evidence register and preserve the repository's distinctions among observation, source claim, assessor inference, and unresolved evidence.

If the manuscript conflicts with a frozen packet or released assessment, the released artifact controls until a documented protocol and release process changes it.

A released assessment label records what the published procedure produced. It does not establish independent validity. The [PR #11 review record](review-record-pr11.md) preserves the Oko mismatch and its v0.6 resolution through reclassification.

The [claim crosswalk](claim-crosswalk.md) and [v0.14 audit](../audits/v0.14.0/audit-report.md) make that boundary executable. A failed or indeterminate evidence-fitness, support, or dependency gate prevents the affected claim from entering a conclusion. The formal open-index search, selected-index citation chains, 89-record author queue, 27-source initial full-text gate, 71-record forward screen, 13-source proposition review, and five-record direct-query screen are complete within declared limits. The [v0.10 protocol](../protocols/search-coverage-and-full-text-protocol-v0.10.0.md) controls the 1,087-record recovery population and five authenticated or disciplinary interfaces. The 284-record residual-risk sample is frozen. Its forward-citation stratum has 102 retrieval outcomes and 71 screening decisions. Five sources have bounded proposition permission, two remain background-only, and six are quarantined. The proposed cross-domain mechanism remains conclusion-ineligible. Independent assessment, 980 retrieval outcomes, the 177-record backward-reference stratum, authenticated interfaces, and venue-specific ethics guidance remain open.
