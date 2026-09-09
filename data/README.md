# Data inventory

The author-supplied frozen CSV extracts and PSNI workbook are bundled. `psni_monthly(1).csv` was renamed to `psni_monthly.csv` without modifying its contents. Checksums and coverage are recorded in `docs/data_manifest.json`.

| Filename | Required columns / purpose |
| --- | --- |
| `events_monthly_northern_ireland.csv` | `month`, `violence`, `repression`, `security`, `total_events`, `elite_coop`, `elite_conflict` |
| `kg_theme_counts_northern_ireland.csv` | `month`, `theme`, `mentions` |
| `kg_theme_counts_northern_ireland_STRICT.csv` | `month`, `theme`, `mentions`; stricter geographic filter |
| `psni_monthly.csv` | `month`, `psni_shootings`, `psni_bombings`, `psni_para_shootings`, `psni_para_assaults`, `psni_s41_arrests` |
| `March 2026 Accompanying excel spreadsheet for Security website ONLINE 14.05.2026a2.xls` | Workbook read by notebook 01, only needed to regenerate PSNI CSV |

Use month-start ISO dates. The Events and PSNI panels should have one row per month. GKG has theme-count rows per month. Check missing months, duplicates, nonnegative counts and study coverage before analysis.

GDELT queries are in notebooks 02 and 03. PSNI source: https://www.psni.police.uk/official-statistics/security-situation-statistics . The workbook release/date above is recorded in the supplied extraction notebook and is included as supplied.

The original README described a June 2026 snapshot, and the supplied files are now recorded with hashes. When adding them, record extraction dates, query versions, row counts, date coverage, SHA-256 hashes and redistribution terms. The manuscript calls the dataset version 2.1 while the original README calls it 2.0; reconcile this terminology against the actual GDELT tables used.

The supplied embedding CSV is also included. Regression reference outputs are in `results/reference/`; reruns write to `results/`. Bundled data are included by Git; review source terms before public redistribution. Do not substitute synthetic inputs and describe the resulting outputs as paper results.
