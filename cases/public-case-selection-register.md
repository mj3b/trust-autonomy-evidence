# Public Case Selection Register

## Freeze state

**Protocol:** [`public-case-reconstruction-protocol.md`](../protocols/public-case-reconstruction-protocol.md)

**Evidence cutoff:** 6 August 2026 at 23:59:59 UTC

**Screening state:** Complete. The first eligible case in each stratum was selected after five AI Incident Database candidates were screened.

**Freeze commit:** [`180ddda1d70f0ee36faaf8875e839bbc99cbbec2`](https://github.com/mj3b/trust-autonomy-evidence/commit/180ddda1d70f0ee36faaf8875e839bbc99cbbec2)

Candidate discovery, screening, and source acquisition began after the freeze commit was recorded. The earlier empty state remains available in the freeze commit and establishes that case outcomes were unknown when the selection procedure was published.

## Candidate collections

| Collection | Frozen input | Retrieval date | SHA-256 | Search result |
|---|---|---|---|---|
| AI Incident Database weekly snapshot | `backup-20260803110541.tar.bz2`; 1,607 incident records and 7,452 report records | 7 August 2026 | `97fe770b0e92730c98fbb05bca8f9e2df6803f0f386d94404a19a7677d70f240` | 828 candidates matched at least one frozen term |
| OECD AI Incidents and Hazards Monitor export | `incidents (1).xlsx`; first 100 rows exposed by the frozen 18-term query | 7 August 2026 | `741bcde4c920a0501589637368831c6242641738a176588312b24056fc27207e` | 100 exported candidates; date-range probes found no result before 2020 |

The machine-readable search output is preserved in [`candidate-search-output.json`](data/candidate-search-output.json). The OECD interface reported about 3,635 matches and limited an export to 100 visible rows. Separate frozen-query probes returned zero records for 1900 through 2019. Because all three selections were filled by AI Incident Database events dated before 2020, the interface limit could not change which candidates were selected.

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
| 1 | AIID-27 | Incident 27 and its linked reports | 26 September 1983 | Pre-action intervention | INCLUDE-PRE | A machine-based warning system inferred an attack; the duty officer received the alert before escalation, challenged it using contextual and ground-radar evidence, and reported a false alarm. At least two eligible reports support the bounded sequence. | [`TAE-PUB-001`](TAE-PUB-001-oko-1983/) |
| 2 | AIID-42 | Incident 42 and its linked reports | 3 April 1996 | None | EX-SOURCE | The frozen term `chatbot` appears only in a generic administrative record about converting the database, not in an event source. The remaining material does not supply two independent reports of a bounded autonomous action. | None |
| 3 | AIID-79 | Incident 79 and its linked reports | 16 March 1999 | None | EX-BOUNDARY | The frozen term `assistant` appears in a source author's job title. The event concerns a population-level formula applied over time and lacks one bounded action sequence that can be reconstructed under the protocol. | None |
| 4 | AIID-444 | Incident 444 and its linked reports | 22 March 2003 | Authority without practical force | INCLUDE-FORCE | Patriot operators held formal engagement authority, while a compressed decision window, training to trust the system, incomplete communications, limited air-picture access, and identification gaps made effective challenge infeasible. | [`TAE-PUB-002`](TAE-PUB-002-patriot-zg710-2003/) |
| 5 | AIID-445 | Incident 445 and its linked reports | 2 April 2003 | Incomplete or conflicting evidence | INCLUDE-GAP | Public sources establish the detection, command correlation, launch order, engagement, and loss. The full inquiry, logs, displays, and classified technical report are unavailable, so the misclassification mechanism and feasible intervention options remain indeterminate. | [`TAE-PUB-003`](TAE-PUB-003-patriot-fa18-2003/) |

## Selected cases

| Stratum | Candidate ID | Selection order | Packet manifest | Assessment state |
|---|---|---:|---|---|
| Pre-action intervention | AIID-27 | 1 | [`packet-manifest.json`](TAE-PUB-001-oko-1983/packet-manifest.json) | Bounded intervention proposition supported |
| Incomplete or conflicting evidence | AIID-445 | 5 | [`packet-manifest.json`](TAE-PUB-003-patriot-fa18-2003/packet-manifest.json) | Sequence supported; cause and intervention feasibility indeterminate |
| Authority without practical force | AIID-444 | 4 | [`packet-manifest.json`](TAE-PUB-002-patriot-zg710-2003/packet-manifest.json) | Formal authority supported; practical-force chain unsupported |

## Update rule

Append candidates in screening order. Preserve excluded and replaced candidates. A pull request that adds or changes a candidate must include the frozen collection hashes, search output, decision code, and effect on the three selected strata.
