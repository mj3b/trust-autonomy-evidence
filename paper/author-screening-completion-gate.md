# Author Screening Completion Gate

**Status:** OPEN

Mark Julius Banasihan is the recorded decision owner. AI-assisted proposals remain proposals until the v0.8 decision ledger records his decision. The final search-flow figure is eligible only after every queued record has a valid author decision.

## Current state

| Queue component | Records | Author decisions complete | Decisions open |
|---|---:|---:|---:|
| Proposed retain-close | 12 | 0 | 12 |
| Proposed attention | 77 | 0 | 77 |
| Total author gate | 89 | 0 | 89 |

## Completion conditions

1. The v0.8 decision ledger contains one permitted `author_decision` value for every v0.7 queue record.
2. Decisions that depart from the proposal contain a short `author_notes` rationale.
3. Retained close sources receive full-text verification before they support a substantive manuscript claim.
4. The search table and Figure 5 are rebuilt from the author decisions.
5. The manuscript replaces preliminary-screening language with final-screening language only after this gate closes.

## Permitted decisions

`retain-close`, `retain-background`, `exclude-topic`, `exclude-single-component`, `exclude-outside-cutoff`, or `inaccessible`.

## Current boundary

The gate is open. Figure 5 remains a preliminary search-flow figure. The repository can report retrieval and proposal counts; it cannot report final screening counts while 89 author decisions remain open.
