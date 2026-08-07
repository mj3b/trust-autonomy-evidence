# Case Studies

Version 0.3.0 retains twelve constructed cases in [`fixtures/synthetic/cases.json`](../fixtures/synthetic/cases.json) and adds three public-case packets selected under a frozen protocol.

The synthetic cases test internal artifact behavior. They are not operational observations and do not represent a sampled decision population.

## Public-case packets

| Packet | Short description | Selection stratum |
|---|---|---|
| [`TAE-PUB-001`](TAE-PUB-001-oko-1983/) | A 1983 Oko false warning in which a duty officer challenged the alert before escalation | Pre-action intervention |
| [`TAE-PUB-002`](TAE-PUB-002-patriot-zg710-2003/) | A 2003 Patriot fratricide in which formal launch authority lacked practical force | Authority without practical force |
| [`TAE-PUB-003`](TAE-PUB-003-patriot-fa18-2003/) | A 2003 Patriot fratricide whose public record supports the sequence while leaving cause and feasible intervention unresolved | Incomplete or conflicting evidence |

Each directory contains a source manifest, machine-readable assessment, narrative report, and SHA-256 packet manifest. [`public-case-packet-index.json`](public-case-packet-index.json) seals the three packet manifests. [`public-case-selection-register.md`](public-case-selection-register.md) preserves the screening path.

A case may enter this directory when it contains a declared decision boundary, contemporaneous records, source provenance, publication authority, redaction statement, missing-evidence register, protocol version, independent reviewer results, and limits on interpretation.

These public cases are retrospective and single-assessor. They do not establish independent reliability or represent a sampled decision population. Synthetic or simulated additions must identify which properties are constructed and which conclusions cannot transfer to operational deployments.

## Privacy and authority

Do not publish personal data, confidential records, security-sensitive details, or institutionally restricted material without documented authority. A redacted case must identify how redaction affects the assessment.
