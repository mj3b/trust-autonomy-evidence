# arXiv Preprint Candidate, v0.14.0

This directory contains the first repository-controlled preprint package for *From Formal Authority to Practical Human Control* by Mark Julius Banasihan.

## Package map

| File | Purpose |
|---|---|
| [`main.tex`](main.tex) | Self-contained article source generated from the reader manuscript. The source archive places this file at archive root. |
| [`preprint-v0.14.0.pdf`](preprint-v0.14.0.pdf) | Canonical 25-page color PDF with a professional single-column body, black text, dark navy navigation, and journal-style tables. |
| [`overleaf-compiled-v0.14.0.pdf`](overleaf-compiled-v0.14.0.pdf) | Approved 25-page Overleaf output, byte-identical to the canonical preprint and visually inspected on 14 representative text, table, figure, and References pages. |
| [`overleaf-compile-receipt.json`](overleaf-compile-receipt.json) | Records the project, source and output hashes, page count, compiler result, warnings, visual checks, and claim boundary. |
| [`arxiv-source-v0.14.0.zip`](arxiv-source-v0.14.0.zip) | Deterministic upload archive containing `main.tex`, ten figure PNGs, and `00README.XXX`. |
| [`source-manifest.json`](source-manifest.json) | SHA-256, byte size, and archive path for every upload member. |
| [`figures-bw-manifest.json`](figures-bw-manifest.json) | Source and output hashes for ten retained grayscale alternatives. |
| [`figures-bw/`](figures-bw/) | Grayscale publication alternatives for print and accessibility checks; the color figures remain the preprint sources. |
| [`metadata.yaml`](metadata.yaml) | Proposed title, authorship, abstract, categories, comments, and unresolved submission fields. |
| [`00README.XXX`](00README.XXX) | arXiv compiler note included in the source archive. |

## Build path

1. [`manuscript.md`](../manuscript.md) preserves Pandoc citation identifiers.
2. [`references.bib`](../references.bib) supplies checked citation metadata.
3. [`manuscript-reader.md`](../manuscript-reader.md) resolves citations into readable author-year links.
4. [`build_arxiv_monochrome_figures.py`](../../scripts/build_arxiv_monochrome_figures.py) preserves ten grayscale alternatives and records their source and output hashes.
5. [`build_arxiv_preprint.py`](../../scripts/build_arxiv_preprint.py) generates professional single-column `main.tex` from the repository manuscript, dark navy palette, journal tables, and original color figures.
6. [`build_arxiv_source_archive.py`](../../scripts/build_arxiv_source_archive.py) creates the deterministic Overleaf and arXiv upload archive and source manifest.
7. The archive was imported into the private [Overleaf project](https://www.overleaf.com/project/6a7e1b42384861803d9c9825), where it compiled to 25 pages with zero errors, one TeX command-compatibility warning, and no overfull or underfull box notice.
8. The approved Overleaf PDF was synchronized to `preprint-v0.14.0.pdf`; the two files are byte-identical.
9. Placement checks confirm that all ten figures and seven tables appear before References.
10. [`validate_arxiv_package.py`](../../scripts/validate_arxiv_package.py) checks identity, abstract length, single-column structure, table style, palette markers, grayscale-alternative lineage, color-figure references, archive membership, manifest hashes, all 17 display locations, and both PDF records.

The LaTeX source uses a professional single-column long-form article layout adapted from the structural approach of the Yale arXiv Paper Template, with all Yale branding, logo, and affiliation removed. The implementation remains an independent `article` source and carries no Yale endorsement. Captions appear above tables. Dark navy headings, labels, headers, links, and horizontal rules provide navigation; black body text and light gray-blue header rows keep the page restrained. Letter, symbol, and pattern labels preserve figure meaning without color. The layout has no vertical table rules or full cell grid. Major-section float barriers keep displays with the relevant argument and before References. Overleaf compiled the source archive to the canonical 25-page PDF with zero errors, one TeX command-compatibility warning, and no overfull or underfull box notice. The author must still inspect arXiv's compiled PDF before submission.

## Evidence controls

The package depends on the v0.14 proposition-review ledger, 32-claim Chain-of-Evidence map, five evidence-fitness dimensions, dependency closure, human-review attestation, 33 mutation controls, CoE Integrity Audit, repository validation, and release manifest. Six close sources remain quarantined, and RS-DQ-004 has zero source-content permission.

## Author decisions still required

- confirm public affiliation wording and corresponding email;
- select the arXiv license;
- confirm `cs.CY` as the primary category and whether `cs.HC` should be a cross-list;
- obtain endorsement if arXiv requests it;
- confirm the applicable ethics or human-subjects determination language;
- inspect arXiv's generated PDF and metadata before selecting Submit;
- add the version DOI after the GitHub release is archived by Zenodo.

Repository validation cannot make these author and platform decisions.
