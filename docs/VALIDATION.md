# Validation performed

- Events: 131 study months present; 63 rows outside the study window.
- Events: duplicate keys = 0
- GKG: 131 study months present; 24177 rows outside the study window.
- GKG: duplicate keys = 0
- Strict GKG: 131 study months present; 24176 rows outside the study window.
- Strict GKG: duplicate keys = 0
- Entropy baseline/strict Pearson r = 0.997657
- Notebook 01 executed fully: extracted PSNI matches supplied CSV; annual shootings check = 18.

Notebooks 02 and 03: static syntax checks passed; not executed end to end because statsmodels and sentence-transformers are unavailable in this runtime. No new statistical results are claimed.

Source coverage requires attention: Events includes historical dates beginning in 1920; GKG extends to July 2026. Keep the 2015-02 to 2025-12 study filter explicit. Each GKG file includes one empty theme per month, dropped by the supplied notebooks. The claimed June 2026 extraction date in the original README is inconsistent with July 2026 observations and needs author correction.
