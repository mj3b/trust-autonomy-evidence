# Formula Register, v0.16.0

The formulas in this project make decision rules inspectable. They do not make the historical evidence more complete or turn categorical judgments into measurements.

Four formulas appear in the compiled v0.16.0 paper. Four additional formulas document supporting repository rules used in the Markdown manuscript or integrity audit. This separation prevents a supporting rule from being mistaken for a published empirical result.

## Formula map

| ID | Question served | Status | Plain-language meaning |
|---|---|---|---|
| `TAE-F01` | What states may a required stage receive? | Compiled paper | Each stage is classified as supported, partially supported, unsupported, indeterminate, or outside scope. The states have no numeric distance. |
| `TAE-F02` | When does a case pass, fail, or remain unresolved? | Compiled paper and executable rule | One unsupported required stage produces a fail. A partial or indeterminate stage produces an unresolved result when no stage fails. Every required stage must be supported for a pass. |
| `TAE-F03` | What conditions compose event-level control? | Supporting repository method | Event-level control requires information access, comprehension, authority, feasibility, exercised judgment, and execution propagation. |
| `TAE-F04` | What additional conditions compose accountable control? | Supporting repository method | Accountable control adds correction and repair to event-level control. |
| `TAE-F05` | What additional condition composes learning control? | Supporting repository method | Learning control adds institutional reform to accountable control. |
| `TAE-F06` | Was there enough time for an intervention to reach execution? | Compiled paper; proposed and uncalculated | The remaining intervention window equals available time minus interpretation, decision, transmission, and propagation time. The historical packets lack the timestamps needed to calculate it. |
| `TAE-F07` | May a mapped claim enter a conclusion? | Supporting repository method and executable rule | A claim requires traceability, integrity, human support review, evidence fitness, and eligible dependencies. |
| `TAE-F08` | Does a human-control representation lack complete documentary support? | Compiled paper; definition only | The indicator is one when an institution represents a case as human-controlled and the event-control result is not a pass. It does not establish fault, deception, liability, or harm. |

## Files

- [`formula-register-v0.16.0.json`](formula-register-v0.16.0.json) records each formula's purpose, source location, implementation path, calculation state, and limits.
- [`formulas-v0.16.0.tex`](formulas-v0.16.0.tex) preserves reusable LaTeX expressions with stable formula identifiers.
- [`../schemas/formula-register.schema.json`](../schemas/formula-register.schema.json) defines the machine-readable contract.

## Use boundary

`TAE-F02` is the only formula in this set that produces the three released case results. `TAE-F07` controls claim eligibility in the integrity audit. The remaining formulas define states, relationships, future measurements, or indicators. None supplies a prevalence estimate, causal effect, reliability result, safety finding, institutional-effectiveness finding, or aggregate trust score.
