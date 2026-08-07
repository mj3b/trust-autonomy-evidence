# Repository Governance

## Maintainer

Mark Julius Banasihan is the current maintainer and release authority. The maintainer may accept, revise, defer, or reject a contribution based on evidence traceability, claim discipline, privacy, licensing, security, and compatibility with the declared research scope.

## Decision record

Material changes require a pull request or issue that records:

- the decision being made;
- the affected artifact and claim identifiers;
- supporting and contradicting evidence;
- alternatives considered;
- validation results;
- remaining uncertainty;
- release and migration effects.

## Research contract changes

Changes to schemas, assessment rules, sealed fixtures, oracle answers, or acceptance conditions require a version increment. The changelog must state whether the change corrects an error, clarifies an ambiguity, expands the construct, or changes expected behavior.

Previously published results remain associated with the version that produced them. A later rule cannot silently reinterpret an earlier result.

## Disagreement

Substantive disagreement should remain visible in the issue or pull-request record. Resolution may take the form of a rule revision, an additional case, a competing interpretation, an unresolved status, or a documented scope boundary.

## Release conditions

A numbered release requires:

1. passing repository and solo-suite validation;
2. current claims, limitations, status, citation, and changelog files;
3. synchronized schemas, fixtures, oracle, generated results, and report;
4. a clean public/private boundary;
5. explicit disclosure of unresolved empirical claims.

