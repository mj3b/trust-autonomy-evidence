# v0.17.0 regulatory-extension review set

This folder preserves the bounded working extension reviewed before its integration into the v0.17.0 manuscript.

| File | Short description |
|---|---|
| [`regulatory-section-review.pdf`](regulatory-section-review.pdf) | Two-page reading copy that explains the institutional gap, the selected policy and standards crosswalk, and the proposed sandbox study. |
| [`regulatory-section.tex`](regulatory-section.tex) | LaTeX source fragment used to prepare the integrated manuscript section. |

The underlying official-source observations and bounded use decisions are recorded in [`../../data/policy-and-standards-source-review-v0.17.0.json`](../../data/policy-and-standards-source-review-v0.17.0.json). Mark Julius Banasihan's accountable inclusion decision is preserved in [`../../../evidence/human-review-attestation-v0.17.0.json`](../../../evidence/human-review-attestation-v0.17.0.json). Independent legal review and field validation remain open.

Rebuild and check the reading copy from the repository root:

```bash
python scripts/build_policy_review_pdf_v0_17_0.py
python scripts/validate_policy_crosswalk_v0_17_0.py
```
