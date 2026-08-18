# Preprints.org submission package, v0.15.0

This directory preserves the exact manuscript source, metadata, archive manifest, and later compiled PDF used for the Preprints.org submission candidate.

The package identifies the Zenodo v0.14.0 preprint at [10.5281/zenodo.21926005](https://doi.org/10.5281/zenodo.21926005). The v0.15.0 revision adds venue-required author metadata, an issued prior-version DOI, a version-relationship statement, an expanded integrity-status statement, a venue-aligned AI-assistance disclosure, and the author-confirmed conflicts-of-interest declaration. The title block identifies Mark Julius Banasihan as an independent researcher with Node & Norm and retains both authorized correspondence addresses. A separate author note identifies Node & Norm as the author's independent research initiative, records Harvard University student status, and disclaims University sponsorship or endorsement. The research question, three case assessments, numerical results, and bounded conclusions remain unchanged.

## Repository map

| File | Purpose |
|---|---|
| `main.tex` | Self-contained LaTeX manuscript submitted for compilation. |
| `metadata.yaml` | Author, affiliation, subject, license, DOI, and submission-state record. |
| `preprints-source-v0.15.0.zip` | Deterministic upload archive containing the LaTeX source and ten figures. |
| `source-manifest.json` | SHA-256 lineage for the archive and each member. |
| `preprints-compiled-v0.15.0.pdf` | The 25-page PDF compiled from the exact source archive in a separate Overleaf project. |
| `overleaf-compile-receipt.json` | Records the Overleaf project, source and output hashes, compile result, representative-page review, display locations, and claim boundary. |
| `00README.XXX` | Plain-text compiler and version note included in the archive. |

## Submission gates

1. Completed: the author confirmed the declaration, "The author declares no conflicts of interest," on 2026-08-18.
2. Completed under author authorization: Codex inspected the 25-page Overleaf PDF, including the title page, figures, tables, appendices, and References; the receipt names the reviewer and limits.
3. Open: the author confirms that the Zenodo v0.14.0 relationship is visible to Preprints.org screeners.
4. Completed for the compiled candidate: repository validators and the CoE Integrity Audit pass with declared open exceptions.
5. Open: the exact submitted files and their hashes are recorded before the Submit action.
