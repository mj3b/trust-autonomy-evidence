# Author Screening Completion Gate

**Status:** CLOSED

Mark Julius Banasihan is the recorded decision owner. The ledger discloses AI-assisted title-and-abstract screening, the review basis, the source locator, and the author-accountability boundary for every decision. The final search-flow figure is eligible only after every queued record has a valid and traceable decision.

## Current state

| Queue component | Records | Author decisions complete | Decisions open |
|---|---:|---:|---:|
| Proposed retain-close | 12 | 12 | 0 |
| Proposed attention | 77 | 77 | 0 |
| Total author gate | 89 | 89 | 0 |

## Completion conditions

1. The v0.9 decision ledger contains one permitted `author_decision` value for every v0.7 queue record.
2. Decisions that depart from the proposal contain a short `author_notes` rationale.
3. Retained close sources receive full-text verification before they support a substantive manuscript claim.
4. The search table and Figure 5 are rebuilt from the author decisions.
5. The manuscript replaces preliminary-screening language with final-screening language only after this gate closes.

## Permitted decisions

`retain-close`, `retain-background`, `exclude-topic`, `exclude-single-component`, `exclude-outside-cutoff`, or `inaccessible`.

## Current boundary

The gate is closed. Figure 5 may report final author-screening counts. The result remains bounded to the 89-record queue; inaccessible-record review and authenticated-database searching remain separate gates.

## Recorded author decisions

- `exclude-single-component`: 10
- `exclude-topic`: 20
- `retain-background`: 32
- `retain-close`: 27
