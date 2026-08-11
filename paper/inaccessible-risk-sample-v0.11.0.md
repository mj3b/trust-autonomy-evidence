# Inaccessible-Record Residual-Risk Sample, v0.11.0

**Status:** `FROZEN_BEFORE_RETRIEVAL`  
**Decision owner:** Mark Julius Banasihan  
**Selection date:** 2026-08-11  
**Controlling protocol:** [`protocols/search-coverage-and-full-text-protocol-v0.10.0.md`](../protocols/search-coverage-and-full-text-protocol-v0.10.0.md)

**Assistance disclosure:** Codex drafted the builder and records, computed the deterministic selection, and ran consistency checks under author authorization. Mark Julius Banasihan remains responsible for retrieval, screening, interpretation, and manuscript claims.

## Decision

Sample membership can become outcome-dependent when it is chosen after retrieval begins. This checkpoint fixes the 284 selected records while all 1,087 records remain unresolved. Later retrieval outcomes cannot change membership.

## Population and allocation

The source population is the 1,087 records classified as `inaccessible` in [`formal-screening-proposals-v0.7.0.json`](data/formal-screening-proposals-v0.7.0.json). Each record receives one primary stratum using the frozen order: forward citation, backward reference, then direct query.

| Primary stratum | Population | Selected |
|---|---:|---:|
| forward-citation | 391 | 102 |
| backward-reference | 679 | 177 |
| direct-query | 17 | 5 |
| **Total** | **1,087** | **284** |

The allocation uses Hamilton largest-remainder apportionment. Integer ties follow the declared stratum order. This rounding rule was recorded before any sampled retrieval outcome.

## Reproduction rule

Within each stratum, records are ordered by the SHA-256 digest of `TAE-v0.10-risk-sample|record_key`. The lowest digests enter the sample until the stratum allocation is met. [`inaccessible-risk-sample-v0.11.0.csv`](data/inaccessible-risk-sample-v0.11.0.csv) records the digest, rank, origin set, and source metadata for every selected record.

The executable builder checks the 1,087-record population, primary-stratum assignment, proportional allocation, digest order, selected keys, and exact CSV and JSON bytes.

## Evidence boundary

This checkpoint establishes deterministic sample membership and selection lineage. It supplies no retrieval, screening, prevalence, exhaustive-coverage, or originality result. Sampled records still require the lawful retrieval procedure and author decision recorded in [`inaccessible-record-retrieval-v0.10.0.csv`](data/inaccessible-record-retrieval-v0.10.0.csv).
