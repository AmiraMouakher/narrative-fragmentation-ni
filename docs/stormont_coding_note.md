# Coding note: Stormont Executive suspension dummy

This note documents the coding rule and boundary decisions for the
`stormont_suspended` variable used in the robustness analyses
(`notebooks/03_robustness_analyses.ipynb`). The variable serves as a
media-independent, administrative-record measure of institutional breakdown,
addressing the common-source endogeneity concern raised in peer review.

## Coding rule

A month is coded **1 (suspended)** if a functioning power-sharing Executive
was absent for the **majority of calendar days** of that month, and **0**
otherwise.

A "functioning power-sharing Executive" is defined functionally: a First
Minister and deputy First Minister jointly in office. Under the Northern
Ireland Act 1998, these offices are interdependent (the resignation of one
removes the other), and their vacancy prevents the Executive Committee from
meeting and from taking cross-cutting, significant, or controversial
decisions. This functional criterion — rather than the formal presence of
individual departmental ministers — captures the institutional-collapse
dimension of political instability that the measure is intended to represent.

The majority-of-days threshold for boundary months is simple, symmetric, and
non-discretionary, consistent with standard practice for coding sub-monthly
events into monthly panels.

## Application

| Period | Coding | Rationale |
|---|---|---|
| Sept–Oct 2015 | 0 | The McGuigan-crisis episode (rolling DUP ministerial resignations; the First Minister "stepping aside" 10 Sept – 20 Oct 2015) was an acute political crisis, but the institutions never formally collapsed: the Assembly sat, the Executive existed, and the episode was resolved by the Fresh Start Agreement (17 Nov 2015). Coding it as suspension would require a qualitative dysfunction threshold, undermining the administrative-record character of the variable. The security dimension of this episode is captured by the PSNI index. |
| Jan 2017 | 1 | Deputy First Minister Martin McGuinness resigned on 9 January 2017; under the 1998 Act the joint office fell when Sinn Féin declined to renominate (16 January). The Executive was absent for the majority of the month and politically defunct from 9 January. |
| Feb 2017 – Dec 2019 | 1 | No Executive in office. |
| Jan 2020 | 0 | Executive restored on 11 January 2020 under the New Decade, New Approach agreement; functioning for 21 of 31 days. |
| Feb 2020 – Jan 2022 | 0 | Executive in office. |
| Feb 2022 | 1 | First Minister Paul Givan resigned on 3 February 2022, automatically removing the deputy First Minister. Remaining ministers continued only in a caretaker capacity: without FM/dFM, the Executive Committee could not meet and could not take significant, controversial, or cross-cutting decisions (including a budget). By the functional criterion, the power-sharing core collapsed on 3 February 2022. |
| Mar 2022 – Jan 2024 | 1 | No functioning Executive. The formal departure of caretaker ministers on 28 October 2022 (expiry of the statutory Executive-formation period) is a legal artefact and does not mark a change in Executive functionality. |
| Feb 2024 | 0 | Executive restored on 3 February 2024 (First Minister Michelle O'Neill, deputy First Minister Emma Little-Pengelly); functioning for 26 of 29 days. |

Main specification: suspended months = January 2017 – December 2019 and
February 2022 – January 2024.

## Sensitivity variants

Two alternative boundary codings are estimated in the notebook
(`point2_stormont_sensitivity.csv`):

1. **Inclusive boundaries** — transition months coded as suspended
   (January 2020 = 1; February 2024 = 1).
2. **Caretaker period as functioning** — a strictly legal reading in which the
   second suspension begins only in November 2022, after caretaker ministers
   left office on 28 October 2022.

The inclusive variant changes two months; the caretaker variant changes nine months (February–October 2022). Evaluate the estimated sensitivity rather than assuming negligible changes.

## Sources

All dates are matters of public administrative record: resignation of the
deputy First Minister (9 January 2017); restoration under New Decade, New
Approach (11 January 2020); resignation of the First Minister (3 February
2022); departure of caretaker ministers at the expiry of the statutory period
(28 October 2022); restoration of the Executive (3 February 2024). Statutory
framework: Northern Ireland Act 1998 (joint nature of the FM/dFM offices;
Executive Committee functions); Northern Ireland (Executive Formation etc)
Act 2022 (extension of formation periods and caretaker arrangements).
