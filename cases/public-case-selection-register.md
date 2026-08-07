# Public Case Selection Register

## Freeze state

**Protocol:** [`public-case-reconstruction-protocol.md`](../protocols/public-case-reconstruction-protocol.md)

**Evidence cutoff:** 6 August 2026 at 23:59:59 UTC

**Screening state:** No candidates screened

**Freeze commit:** To be recorded after the initial protocol reaches `main`

Candidate discovery, screening, and source acquisition begin only after the freeze commit is recorded here. This empty register establishes that the case outcomes were unknown when the selection procedure was published.

## Candidate collections

| Collection | Frozen input | Retrieval date | SHA-256 | Status |
|---|---|---|---|---|
| AI Incident Database weekly snapshot | Pending | Pending | Pending | Not retrieved |
| OECD AI Incidents and Hazards Monitor export | Pending | Pending | Pending | Not retrieved |

## Decision codes

| Code | Meaning |
|---|---|
| INCLUDE-PRE | First eligible pre-action intervention case |
| INCLUDE-GAP | First eligible incomplete or conflicting evidence case |
| INCLUDE-FORCE | First eligible authority-without-practical-force case |
| EX-BENCH | Benchmark, hypothetical scenario, or controlled demonstration |
| EX-BOUNDARY | No bounded reliance decision or action sequence |
| EX-SOURCE | Fewer than two eligible public reports |
| EX-PRIMARY | Required primary or official record unavailable outside the incomplete-evidence stratum |
| EX-PRIVATE | Basic reconstruction requires restricted evidence |
| EX-RIGHTS | Material cannot be cited or preserved lawfully |
| EX-DUPLICATE | Duplicate event, system, deployer, and period |
| EX-CUTOFF | Event or evidence falls outside the frozen cutoff |

## Screening register

| Order | Candidate ID | Collection references | Event date | Provisional stratum | Decision code | Reason | Packet |
|---:|---|---|---|---|---|---|---|

## Selected cases

| Stratum | Candidate ID | Selection order | Packet manifest | Assessment state |
|---|---|---:|---|---|
| Pre-action intervention | Pending | Pending | Pending | Pending |
| Incomplete or conflicting evidence | Pending | Pending | Pending | Pending |
| Authority without practical force | Pending | Pending | Pending | Pending |

## Update rule

Append candidates in screening order. Preserve excluded and replaced candidates. A pull request that adds or changes a candidate must include the frozen collection hashes, search output, decision code, and effect on the three selected strata.
