# Chain-of-Evidence Adaptation

## Source architecture

The v0.5.0 method adapts three ideas described in the ScientistOne paper and public artifact repository:

1. Chain-of-Evidence connects each claim to inspectable evidence.
2. ScientistOne preserves those connections through research stages.
3. CoE Integrity Audit tests score verification, specification violations, references, and method-code alignment after an artifact has been produced.

These ideas constrain the originality claim for this repository. Claim traceability and post-hoc integrity checking are prior work. The contribution tested here is a domain adaptation that adds claim-specific evidence fitness, dependency closure, explicit indeterminate states, human support attestations, and preservation of failed evidence for public governance reconstruction.

## Repository adaptation

The adaptation separates five questions that can otherwise collapse into one broad trust statement:

| Question | Stored evidence |
|---|---|
| Can a reader locate the artifact? | path and exact locator |
| Can a changed artifact be detected? | hash or release-manifest state |
| Does the artifact support the sentence? | human support-review attestation |
| Is that evidence fit for this claim? | five evidence-fitness dimensions |
| May the claim support a conclusion? | dependency closure and eligibility |

The method uses W3C PROV-O-compatible concepts for agents, activities, entities, and relations. It does not claim full PROV-O serialization or RO-Crate conformance. A later release may add a formal research-object package.

## ScientistOne artifact pressure test

The public generated-artifacts repository changes how the paper should use the ScientistOne results. It makes source-level checking possible and exposes several distinctions that summary prose can hide:

- the Parameter Golf score is exact for the recorded artifact, while the reported final size is a mean;
- failed unweighted SVD work must remain visible when describing method exploration;
- an unsupported five-seed statement cannot support a repeatability claim;
- AI4Code method descriptions must align with the released code;
- Cloudcast claims remain constrained where independent verification is unavailable; and
- the audit of 75 papers and evaluation across six generalization tasks have different units and scopes.

The repository therefore requires run-type labels and retains failed, excluded, and post-hoc evidence. It does not import ScientistOne's reported findings as evidence about the quality of this repository.

## Evidence and inference

**Observation:** ScientistOne and its artifact repository publish a claim-traceability architecture, an autonomous research system, and a four-part post-hoc integrity audit.

**Inference:** Those materials provide a strong prior architecture for v0.5 and narrow this repository's defensible contribution to its governance-specific implementation and extensions.

**Uncertainty:** This adaptation has not been reviewed by the ScientistOne authors. The audit labels and reported examples require continuing verification against the paper, preserved files, and any later versions.

## Use boundary

The v0.5 audit can detect broken references, changed values, missing attestations, failed fitness dimensions, method-code mismatches, open dependencies, stale hashes, run-type errors, and unsupported bounded terms in its declared test set. It cannot decide source truth or replace qualified human review.
