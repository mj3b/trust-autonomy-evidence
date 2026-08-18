# Forward-Citation Proposition Review Protocol, v0.14.0

**Decision owner:** Mark Julius Banasihan  
**Review date:** 2026-08-13  
**Input:** the 13 records classified `retain-close` in the frozen v0.13 forward-citation ledger

## Problem

Screening establishes that a source is close to the research question. It does not establish that a specific sentence is supported by that source. This review places a proposition-level gate between corpus membership and manuscript use.

## Review unit

The unit is one retained source and one bounded proposition. Each source receives:

1. a verified identity and stable locator;
2. a declared review basis;
3. a bounded proposition or an explicit reason why none is permitted;
4. exact page, section, or abstract locators;
5. a five-dimension evidence-fitness decision;
6. a manuscript-use decision;
7. a limitation and reversal condition; and
8. an AI-assistance disclosure with human decision ownership.

## Review states

| State | Meaning | Claim permission |
|---|---|---|
| `manuscript-use` | Inspectable text supports a bounded proposition and every required fitness dimension passes. | The stated proposition may enter the manuscript with its locator and limitation. |
| `background-only` | The source is relevant, but it adds context without supporting a material manuscript proposition in this cycle. | Background description only. |
| `quarantined` | Exact full text, source identity, proposition support, or a required fitness dimension is unresolved. | No manuscript claim permission. |

An abstract may support a description of the abstract's declared purpose. It may not support a proposition that requires methods, results, limitations, or page-level context.

## Evidence-fitness rule

The review records directness, contemporaneity, independence, completeness, and publication authority. `outside_scope` is allowed only when the proposition does not require that dimension. One failed or indeterminate required dimension blocks manuscript use.

The source need not be contemporaneous with this paper's historical cases when it supports a method, a present-day oversight mechanism, or a design pattern. The rationale must identify that scope.

## ScientistOne-inspired lineage rule

Every permitted proposition must trace through this sequence:

`source locator -> inspected passage -> proposition review row -> bibliography record -> manuscript sentence -> claim map -> integrity audit -> release manifest`

If any link changes, the proposition and dependent conclusion return to review.

## Completion conditions

The gate closes only when:

- all 13 frozen source identifiers appear exactly once and in their frozen order;
- every row has a stable locator, review basis, decision, rationale, fitness states, limitation, owner, date, and disclosure;
- only inspectable proposition-level records receive `manuscript-use`;
- manuscript-use propositions resolve to exact page, section, or abstract locators;
- the five permitted citations resolve in `references.bib` and the manuscript;
- quarantined records receive no claim permission;
- the direct-query overlay records a terminal decision without altering the v0.11 released artifact;
- the claim map, lineage, mutation suite, audit, paper validator, repository validator, and release manifest agree.

## Decision boundary

Closing this gate shows that the retained-source propositions were reviewed under the declared procedure. It supplies no independent source verification, systematic-search completion, inter-assessor agreement, originality finding, prevalence estimate, or institutional-effect result.
