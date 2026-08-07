# Publication Figure Set

The figure set converts committed assessments, selection records, mutation results, and artifact lineage into six reproducible graphics. It adds no empirical observation and changes no v0.3.0 case finding.

The figures follow four measurement rules drawn from the repository's use of METR's evaluation discipline: the measured unit appears in each specification, raw categorical states remain visible, uncertainty stays separate from negative findings, and every image has a machine-readable input table.

## Main figures

| Figure | Short description | Files |
|---|---|---|
| Figure 1 | Shows how 928 preserved candidate records produced five screening decisions, three selected cases, two exclusions, and 923 unscreened records under the frozen stopping rule. | [PNG](generated/fig-1-selection-and-stopping.png) · [SVG](generated/fig-1-selection-and-stopping.svg) · [data](data/fig-1-selection-and-stopping.csv) |
| Figure 2 | Compares the nine practical-control propositions across Oko, Patriot ZG710, and Patriot F/A-18C. | [PNG](generated/fig-2-practical-control-chain.png) · [SVG](generated/fig-2-practical-control-chain.svg) · [data](data/fig-2-practical-control-chain.csv) |
| Figure 3 | Places 15 source-linked events in relative order and marks the public evidence gap in the F/A-18C sequence. | [PNG](generated/fig-3-decision-paths.png) · [SVG](generated/fig-3-decision-paths.svg) · [data](data/fig-3-decision-paths.csv) |
| Figure 4 | Compares the 12 trust-evidence propositions across the three public cases. | [PNG](generated/fig-4-trust-evidence-states.png) · [SVG](generated/fig-4-trust-evidence-states.svg) · [data](data/fig-4-trust-evidence-states.csv) |

## Appendix figures

| Figure | Short description | Files |
|---|---|---|
| Figure A1 | Maps all 12 controlled mutations to 11 prespecified state changes and three invariance tests. | [PNG](generated/fig-a1-mutation-response.png) · [SVG](generated/fig-a1-mutation-response.svg) · [data](data/fig-a1-mutation-response.csv) |
| Figure A2 | Traces the research and figure-generation artifacts from frozen collections through repository validation. | [PNG](generated/fig-a2-reproducibility-lineage.png) · [SVG](generated/fig-a2-reproducibility-lineage.svg) · [data](data/fig-a2-reproducibility-lineage.csv) |

## Regeneration

Install the development dependencies and rebuild the full set:

```bash
python -m pip install -r requirements-dev.txt
python analysis/build_figures.py
```

Check whether every committed CSV, PNG, and SVG matches a clean rebuild:

```bash
python analysis/build_figures.py --check
```

The repository validator runs the same freshness check. [Figure methods](../reports/figure-methods.md) records the transformations, captions, and claim boundaries. [The figure register](specifications/figure-register.json) provides a machine-readable specification for each image.

## Use boundary

The three public cases were purposefully selected under a stopping rule. The figures support cross-case description for those packets. They supply no population frequency, effect size, causal estimate, inter-rater reliability result, system ranking, or aggregate trust score.
