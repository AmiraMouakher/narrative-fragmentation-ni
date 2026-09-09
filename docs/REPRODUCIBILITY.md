# Reproducibility and review notes

## Verified in this packaging pass

Full execution of notebook 01 with exact agreement to the supplied PSNI CSV; study-period coverage and baseline/strict entropy correlation (0.997657); notebook JSON and code-cell Python syntax; portable root discovery; optional extraction defaults; local README links and required file inventory. Stored notebook outputs and execution counters were cleared. The supplied PNG is a reference illustration, not evidence of a successful rerun.

## Not verified

End-to-end execution of notebooks 02 and 03, numerical agreement with the paper, BigQuery extraction, the original package versions, source-data rights, and model-download reproducibility. The required datasets are now bundled. The execution environment lacks statsmodels and sentence-transformers, so full execution was not possible here. Static CI does not certify scientific replication.

## Scientific issues requiring author review

1. **Embedding validation:** notebook 02 builds monthly strings from `kg.groupby("month")["theme"]` and encodes theme labels. It does not independently encode article text. Its output name `monthly_news_text_with_volatility.csv` is retained for compatibility but can be misleading. Supply the actual news-text validation implementation or revise the manuscript claim. No scientific method was silently substituted.
2. **Rank-deficient PSNI local projection:** notebook 03 includes both `shock_l1` and `s_l1`, each equal to the same lagged standardized PSNI series. This duplicates a regressor. The original specification is retained for traceability; remove one copy and rerun the estimates before using the coefficient or standard error in the paper.
3. **Joint tests:** the notebook 03 joint test is a distributed-lag test, not a joint test across all local-projection horizons. Match the manuscript description to what is tested.
4. **Stormont sensitivity:** the caretaker variant changes nine months (February–October 2022), not two or three. The documentation now reflects the implemented periods.
5. **Results summaries:** retained markdown summaries in the notebooks are author-provided historical claims, not regenerated outputs. Recheck them after execution.
6. **Extraction coverage:** supplied queries are not bounded to the study window at SQL level. Later filtering is not an equivalent protection against unnecessary query costs or changing source coverage. Review coverage of each derived series before analysis.

## Packaging changes

- Updated manuscript title to the attached PDF's title.
- Removed automatic mounting and personal Drive paths.
- Defined `BASE` consistently and supported root/notebooks working directories.
- Made strict BigQuery extraction optional and protected existing CSVs.
- Enabled local Application Default Credentials for optional extraction.
- Routed the regenerated dashboard to `figures/`.
- Added Jupyter/validation dependencies and a separate BigQuery dependency file.
- Replaced unsupported claims of bundled data and complete reproducibility.
- Preserved statistical analysis code, including the explicitly documented PSNI issue.

Before a research release: resolve these scientific issues, run every notebook in a clean environment, compare paper tables/figures, and record a validated dependency lockfile.
