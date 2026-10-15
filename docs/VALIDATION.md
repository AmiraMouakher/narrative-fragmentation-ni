# Validation performed

- Events: 131 study months present; 63 rows outside the study window.
- Events: duplicate keys = 0
- GKG: 131 study months present; 24177 rows outside the study window.
- GKG: duplicate keys = 0
- Strict GKG: 131 study months present; 24176 rows outside the study window.
- Strict GKG: duplicate keys = 0
- Entropy baseline/strict Pearson r = 0.997657
- Notebook 01 executed fully: extracted PSNI matches supplied CSV; annual shootings check = 18.

Notebooks 02 and 03: executed end to end on 15 October 2026 with the versions in `requirements-lock.txt` (Python 3.13, numpy 2.1.3, pandas 2.2.3, scipy 1.14.1, statsmodels 0.14.4, scikit-learn 1.5.2, matplotlib 3.9.2). Every statistic reported in the manuscript and its Supplementary Information was compared with the notebook output and reproduces. The semantic-dispersion series was read from the saved `monthly_news_text_with_volatility.csv` (embedding recomputation is optional: `RECOMPUTE_EMBEDDINGS = True` in notebook 02).

Corrections made in this pass: the theme-count trend (notebook 03) is now computed over the study window only (beta = -5.5 themes per month, p = 0.002, Spearman rho = -0.58; previously computed over 138 months including January-July 2026); the semantic-dispersion figure is restricted to the study window; figure labels use the manuscript's terms (violent unrest, state coercion, security mobilization) and conventional significance markers.

Source coverage requires attention: Events includes historical dates beginning in 1920; GKG extends to July 2026. Keep the 2015-02 to 2025-12 study filter explicit. Each GKG file includes one empty theme per month, dropped by the supplied notebooks. The claimed June 2026 extraction date in the original README is inconsistent with July 2026 observations and needs author correction.
