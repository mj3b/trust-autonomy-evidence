# Case Studies

Version 0.3.0 retains twelve constructed cases in [`fixtures/synthetic/cases.json`](../fixtures/synthetic/cases.json) and adds three public-case packets selected under a frozen protocol.

The synthetic cases test internal artifact behavior. They are not operational observations and do not represent a sampled decision population.

## Public-case packets

| Packet | Short description | Selection stratum |
|---|---|---|
| [`TAE-PUB-001`](TAE-PUB-001-oko-1983/) | A 1983 Oko false warning in which a duty officer challenged the alert before escalation | Pre-action intervention |
| [`TAE-PUB-002`](TAE-PUB-002-patriot-zg710-2003/) | A 2003 Patriot fratricide in which formal launch authority lacked practical force | Authority without practical force |
| [`TAE-PUB-003`](TAE-PUB-003-patriot-fa18-2003/) | A 2003 Patriot fratricide with a supported sequence and unresolved cause and feasible intervention | Incomplete or conflicting evidence |

Each directory contains a source manifest, machine-readable assessment, narrative report, and SHA-256 packet manifest. [`public-case-packet-index.json`](public-case-packet-index.json) seals the three packet manifests. [`public-case-selection-register.md`](public-case-selection-register.md) preserves the screening path.

A public case enters this directory under the versioned protocol in force. Version 0.3.0 requires a declared decision boundary, source provenance, publication authority, a redaction statement, a missing-evidence register, a protocol version, and limits on interpretation. The three v0.3.0 packets are single-assessor records and contain no independent reviewer result. Contemporaneous evidence varies by packet and must be evaluated at the assessment-state level.

## What this case set can and cannot tell us

The three public cases were purposefully selected under a frozen order and stopping rule to demonstrate the method under contrasting evidence conditions. They show the assessment states produced for documented pre-action intervention, formal authority without practical force, and incomplete or conflicting evidence. Because the strata anticipated these contrasts, the case set does not independently validate discrimination among them.

They do not tell us:

- how often these conditions occur;
- whether these cases represent AI systems generally;
- whether human intervention usually improves outcomes;
- whether historical military systems behave like current learned AI systems.

The cases are retrospective and single-assessor. They do not establish independent reliability, causal effects, outcome improvement, or population representativeness. See the [public-case reconstruction protocol](../protocols/public-case-reconstruction-protocol.md) and [selection register](public-case-selection-register.md) for the governing rules and screening record.

Synthetic or simulated additions must identify which properties are constructed and which conclusions cannot transfer to operational deployments.

## Privacy and authority

Do not publish personal data, confidential records, security-sensitive details, or institutionally restricted material without documented authority. A redacted case must identify how redaction affects the assessment.

