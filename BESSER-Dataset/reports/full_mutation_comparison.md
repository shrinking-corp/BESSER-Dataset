# Mutation runs compared: baseline (A) vs super suite (B)

Generated: 2026-10-20T15:09:46.711854+00:00

- A: `reports\full_baseline_green_mutation.json`
- B: `reports\full_super_suite_mutation.json`
- **Models measured in both:** 5264
- **Mean score:** A 0.356 · B 0.7561 · **lift +40.01 pts**
- **Per model (B vs A):** 4640 improved · 0 worse · 624 unchanged
- **Perfect scores:** A 8 · B 21 · **zero scores:** A 2 · B 0
- **Same number of mutants run per model:** yes, every model
- **Kills that were only a per-mutant timeout:** A 44 · B 54. Counting all of them as survived: A 0.3558 · B 0.7558 · lift +40.00 pts

## By difficulty bucket

| Bucket | Models | A | B | Lift (pts) | Improved | Worse | Unchanged |
|---|---:|---:|---:|---:|---:|---:|---:|
| 0-10 | 363 | 0.3944 | 0.6958 | +30.14 | 237 | 0 | 126 |
| 10-20 | 1239 | 0.3849 | 0.764 | +37.91 | 1096 | 0 | 143 |
| 20-30 | 1294 | 0.3786 | 0.7437 | +36.51 | 1112 | 0 | 182 |
| 30-40 | 1002 | 0.3523 | 0.7405 | +38.82 | 880 | 0 | 122 |
| 40-50 | 647 | 0.3192 | 0.7645 | +44.53 | 611 | 0 | 36 |
| 50-60 | 336 | 0.2959 | 0.7995 | +50.36 | 326 | 0 | 10 |
| 60-70 | 188 | 0.2646 | 0.8117 | +54.71 | 185 | 0 | 3 |
| 70-80 | 127 | 0.2976 | 0.8179 | +52.03 | 125 | 0 | 2 |
| 80-90 | 59 | 0.2612 | 0.8326 | +57.14 | 59 | 0 | 0 |
| 90-100 | 9 | 0.2306 | 0.8417 | +61.11 | 9 | 0 | 0 |

## Largest drops (B below A), top 20

None: no model scores lower in B than in A.

## Models with a timeout kill on either side

| Model | A score | A timeout kills | B score | B timeout kills |
|---|---:|---:|---:|---:|
| model_10000238 | 0.275 | 3 | 0.275 | 3 |
| model_10000974 | 0.525 | 1 | 0.775 | 0 |
| model_10001049 | 0.475 | 1 | 0.625 | 1 |
| model_100148 | 0.3 | 1 | 0.725 | 1 |
| model_100149 | 0.4 | 1 | 0.725 | 2 |
| model_100150 | 0.3 | 0 | 0.65 | 1 |
| model_100151 | 0.5 | 1 | 0.8 | 1 |
| model_100152 | 0.4 | 1 | 0.775 | 1 |
| model_100153 | 0.45 | 1 | 0.75 | 1 |
| model_100174 | 0.25 | 1 | 0.75 | 1 |
| model_100209 | 0.4 | 3 | 0.8 | 3 |
| model_1125 | 0.325 | 0 | 0.75 | 1 |
| model_1148 | 0.45 | 2 | 0.9 | 2 |
| model_1797 | 0.4 | 0 | 0.75 | 1 |
| model_1907 | 0.425 | 1 | 0.775 | 1 |
| model_1929 | 0.35 | 2 | 0.825 | 2 |
| model_1933 | 0.475 | 1 | 0.65 | 1 |
| model_1955 | 0.35 | 1 | 0.675 | 1 |
| model_1959 | 0.35 | 1 | 0.625 | 1 |
| model_2290 | 0.4 | 1 | 0.55 | 1 |
| model_2456 | 0.5 | 1 | 0.8 | 1 |
| model_2617 | 0.475 | 1 | 0.8 | 1 |
| model_2938 | 0.425 | 0 | 0.8 | 1 |
| model_3088 | 0.375 | 1 | 0.85 | 1 |
| model_3260 | 0.275 | 1 | 0.8 | 1 |
| model_3450 | 0.275 | 2 | 0.875 | 2 |
| model_3987 | 0.4 | 1 | 0.9 | 1 |
| model_4340 | 0.4 | 1 | 0.7 | 1 |
| model_455 | 0.3 | 2 | 0.9 | 2 |
| model_4612 | 0.25 | 0 | 0.825 | 1 |
| model_4837 | 0.375 | 1 | 0.825 | 3 |
| model_4841 | 0.35 | 1 | 0.85 | 1 |
| model_4849 | 0.35 | 1 | 0.9 | 1 |
| model_4992 | 0.3 | 2 | 0.85 | 3 |
| model_5064 | 0.25 | 1 | 0.875 | 1 |
| model_5149 | 0.575 | 1 | 0.875 | 3 |
| model_934 | 0.45 | 1 | 0.725 | 1 |
| model_940 | 0.15 | 1 | 0.825 | 1 |
| model_943 | 0.3 | 1 | 0.925 | 1 |
| model_944 | 0.15 | 1 | 0.775 | 1 |
