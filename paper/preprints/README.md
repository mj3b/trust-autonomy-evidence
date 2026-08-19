# Current working paper: v0.16.0

The latest paper is [`preprints-compiled-v0.16.0.pdf`](preprints-compiled-v0.16.0.pdf). This directory preserves its manuscript source, metadata, deterministic archive, and compile receipts.

External reviewers should begin with the [`current-paper review guide`](../REVIEW.md), which separates this package from earlier versions and points to the supporting evidence records.

The package identifies the Zenodo v0.14.0 preprint at [10.5281/zenodo.21926005](https://doi.org/10.5281/zenodo.21926005) and preserves the v0.15.0 venue package as version history. Version 0.16.0 rebuilds the explanation, formalizes the six-stage event-control rule, derives one unresolved and two failing case-level results from the released states, adds a proposed timing margin, and narrows the legacy `effect` field to execution propagation. The title block identifies Mark Julius Banasihan as an independent researcher with Node & Norm and retains both authorized correspondence addresses. A separate author note records Harvard University student status without claiming University sponsorship or endorsement.

## Repository map

| File | Purpose |
|---|---|
| `main.tex` | Self-contained LaTeX working paper. |
| `metadata.yaml` | Author, affiliation, subject, license, DOI, and submission-state record. |
| `preprints-source-v0.16.0.zip` | Deterministic review archive containing the LaTeX source and ten figures. |
| `source-manifest.json` | SHA-256 lineage for the archive and each member. |
| `preprints-compiled-v0.16.0.pdf` | Review PDF compiled from the exact v0.16.0 source archive. |
| `compile-receipt-v0.16.0.json` | Records source and output hashes, the local Tectonic compile result, representative-page review, display locations, and claim boundary. |
| `overleaf-compile-receipt.json` | Records the v0.16.0 XeLaTeX build, downloaded PDF hash, all-page visual review, display locations, and claim boundary. |
| `00README.XXX` | Plain-text compiler and version note included in the archive. |

The retired v0.15.0 PDF, source archive, and Overleaf receipt are stored in [`../archive/v0.15.0/`](../archive/v0.15.0/). The v0.14.0 Zenodo and arXiv-format package remains in [`../arxiv/`](../arxiv/).

## arXiv handoff

If the arXiv submission returns to an editable state, [`preprints-source-v0.16.0.zip`](preprints-source-v0.16.0.zip) is the current source candidate to upload. The author must review arXiv's compiled PDF and current metadata before final submission. The `paper/arxiv/` source package is v0.14.0 history and should not replace the current paper.

## Submission gates

1. Completed: the v0.16.0 manuscript, figures, tables, formal rule, and deterministic result builder agree.
2. Completed: the Chain-of-Evidence map covers 40 claims and all 39 controlled corruptions are detected.
3. Completed: the exact source archive compiled without errors, the log contains no overfull or underfull boxes, and representative pages received a visual placement inspection.
4. Open until author review: Mark Julius Banasihan reviews the full revision and approves any external submission target.
5. Open for stronger research claims: independent assessment, present-system transfer, remaining retrieval, and authenticated database gates.
