# Preprints.org submission package, v0.15.0

This directory preserves the exact manuscript source, metadata, archive manifest, and later compiled PDF used for the Preprints.org submission candidate.

The package identifies the Zenodo v0.14.0 preprint at [10.5281/zenodo.21926005](https://doi.org/10.5281/zenodo.21926005). The v0.15.0 revision adds venue-required author metadata, an issued prior-version DOI, a version-relationship statement, an expanded integrity-status statement, a venue-aligned AI-assistance disclosure, and a conflicts-of-interest gate. Node & Norm is the independent research affiliation. Harvard University appears only in an accurate student-status note with an explicit independence disclaimer. The research question, three case assessments, numerical results, and bounded conclusions remain unchanged.

## Repository map

| File | Purpose |
|---|---|
| `main.tex` | Self-contained LaTeX manuscript submitted for compilation. |
| `metadata.yaml` | Author, affiliation, subject, license, DOI, and submission-state record. |
| `preprints-source-v0.15.0.zip` | Deterministic upload archive containing the LaTeX source and ten figures. |
| `source-manifest.json` | SHA-256 lineage for the archive and each member. |
| `00README.XXX` | Plain-text compiler and version note included in the archive. |

## Submission gates

1. The author confirms the conflict-of-interest declaration.
2. The author inspects the compiled PDF.
3. The author confirms that the Zenodo v0.14.0 relationship is visible to Preprints.org screeners.
4. Repository validators and the CoE Integrity Audit pass for the frozen v0.15.0 package.
5. The exact submitted files and their hashes are recorded before the Submit action.
