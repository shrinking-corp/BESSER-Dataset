# PCA difficulty score: evidence report

Generated: 2026-10-18T21:19:53.916782+00:00

- **Models used:** 5264 (models file: `reports\unique_models.txt`, 0 no_logic-only models excluded)
- **Official score (PC1+PC2) vs. article, Spearman:** +0.9165

## 1. How many components to keep

Retained by Kaiser (eigenvalue > 1): **3** · broken stick: **1** · parallel analysis (100 random runs, seed 42, 95th pct): **3**

| Component | Eigenvalue | Variance | Scree drop | Kaiser | Broken stick (expected) | Parallel p95 (random) |
|---|---:|---:|---:|:-:|---:|---:|
| PC1 | 5.364 | 48.76% | 3.862 | ✓ | ✓ (27.45%) | ✓ (1.089) |
| PC2 | 1.502 | 13.65% | 0.376 | ✓ | ✗ (18.36%) | ✓ (1.068) |
| PC3 | 1.126 | 10.24% | 0.237 | ✓ | ✗ (13.82%) | ✓ (1.049) |
| PC4 | 0.889 | 8.08% | 0.239 | ✗ | ✗ (10.79%) | ✗ (1.036) |
| PC5 | 0.650 | 5.91% | 0.082 | ✗ | ✗ (8.51%) | ✗ (1.020) |
| PC6 | 0.568 | 5.16% | 0.236 | ✗ | ✗ (6.70%) | ✗ (1.008) |
| PC7 | 0.332 | 3.02% | 0.059 | ✗ | ✗ (5.18%) | ✗ (0.995) |
| PC8 | 0.273 | 2.48% | 0.148 | ✗ | ✗ (3.88%) | ✗ (0.984) |
| PC9 | 0.125 | 1.14% | 0.024 | ✗ | ✗ (2.75%) | ✗ (0.972) |
| PC10 | 0.101 | 0.92% | 0.031 | ✗ | ✗ (1.74%) | ✗ (0.960) |
| PC11 | 0.070 | 0.64% | – | ✗ | ✗ (0.83%) | ✗ (0.944) |

## 2. Component sweep vs. the article formula

| Components | Cumulative variance | Spearman | Pearson | Score range |
|---|---:|---:|---:|---|
| PC1..PC1 | 48.76% | +0.9164 | +0.7477 | 0.00–100.00 |
| PC1..PC2 | 62.42% | +0.9165 | +0.7403 | 0.42–94.95 |
| PC1..PC3 | 72.65% | +0.9036 | +0.7206 | 3.78–93.24 |
| PC1..PC4 | 80.73% | +0.9030 | +0.7238 | 5.01–91.25 |
| PC1..PC5 | 86.65% | +0.9088 | +0.7282 | 5.44–88.58 |
| PC1..PC6 | 91.81% | +0.9143 | +0.7289 | 5.22–87.04 |
| PC1..PC7 | 94.83% | +0.9199 | +0.7313 | 6.50–87.09 |
| PC1..PC8 | 97.30% | +0.9236 | +0.7341 | 6.39–85.23 |
| PC1..PC9 | 98.44% | +0.9245 | +0.7346 | 6.32–84.52 |
| PC1..PC10 | 99.36% | +0.9255 | +0.7350 | 6.46–84.54 |
| PC1..PC11 | 100.00% | +0.9246 | +0.7341 | 6.44–84.10 |

## 3. Extremes check (is the component a real style axis?)

### PC2 (13.65% variance)

Overall mean PC1: -0.000

| Group | Size | Mean PC1 | Mean score |
|---|---:|---:|---:|
| Bottom 10 | 10 | +1.040 | -3.456 |
| Top 10 | 10 | +0.706 | +5.139 |
| Bottom 5% | 263 | +1.039 | -2.062 |
| Top 5% | 263 | -0.379 | +3.029 |

Both extreme groups above average PC1: **yes** · both tails: **no**

### PC3 (10.24% variance)

Overall mean PC1: -0.000

| Group | Size | Mean PC1 | Mean score |
|---|---:|---:|---:|
| Bottom 10 | 10 | +3.567 | -4.214 |
| Top 10 | 10 | +5.429 | +3.637 |
| Bottom 5% | 263 | +2.340 | -2.505 |
| Top 5% | 263 | +2.663 | +2.289 |

Both extreme groups above average PC1: **yes** · both tails: **yes**

## 4. Clamped vs. unclamped (PC1+PC2)

Spearman change without the clip: -0.00038; 6 models above 100, 1 below 0 (max 107.20).

## 5. Exclusion sensitivity (PC1+PC2)

- Base set (n=5264): Spearman +0.9165
- Also without 992 zero-has_logic models (n=4825): Spearman +0.9217

## 6. What adding PC3 would do (PC1+PC2 vs. PC1+PC2+PC3)

- Rank agreement between the two scores (Spearman): **+0.9883**
- Score change: median |change| 1.73, 90th pct 5.21, largest rise +11.22, largest fall -11.97
- Models changing 10-point bucket: 1230 (23.4%), 4 by two or more
- Mean change, models with methods: -1.28 (n=699); without: -0.74

| Bucket | PC1+PC2 | PC1+PC2+PC3 |
|---|---:|---:|
| 0-10 | 363 | 274 |
| 10-20 | 1239 | 1427 |
| 20-30 | 1294 | 1286 |
| 30-40 | 1002 | 1024 |
| 40-50 | 647 | 537 |
| 50-60 | 336 | 352 |
| 60-70 | 188 | 235 |
| 70-80 | 127 | 102 |
| 80-90 | 59 | 23 |
| 90-100 | 9 | 4 |

**Biggest risers**

| Model | PC1+PC2 | +PC3 | Change | Classes | Enums | Methods |
|---|---:|---:|---:|---:|---:|---:|
| model_4314 | 20.38 | 31.60 | +11.22 | 5 | 4 | 0 |
| model_2793 | 22.82 | 33.69 | +10.88 | 4 | 5 | 0 |
| model_730 | 16.98 | 27.70 | +10.72 | 3 | 2 | 2 |
| model_4902 | 28.99 | 39.00 | +10.00 | 5 | 3 | 0 |
| model_4436 | 30.64 | 40.41 | +9.77 | 8 | 5 | 0 |
| model_4490 | 34.92 | 44.09 | +9.17 | 23 | 6 | 0 |
| model_2794 | 35.49 | 44.58 | +9.09 | 7 | 5 | 0 |
| model_2971 | 4.98 | 13.87 | +8.90 | 1 | 1 | 0 |
| model_3521 | 4.98 | 13.87 | +8.90 | 1 | 1 | 0 |
| model_2972 | 4.98 | 13.87 | +8.90 | 1 | 1 | 0 |
| model_4435 | 38.50 | 47.17 | +8.67 | 10 | 6 | 0 |
| model_100510 | 39.28 | 47.84 | +8.56 | 15 | 7 | 0 |
| model_3408 | 39.32 | 47.87 | +8.55 | 10 | 5 | 0 |
| model_3448 | 20.84 | 29.31 | +8.47 | 5 | 3 | 0 |
| model_100424 | 40.08 | 48.52 | +8.44 | 37 | 8 | 0 |

**Biggest fallers**

| Model | PC1+PC2 | +PC3 | Change | Classes | Enums | Methods |
|---|---:|---:|---:|---:|---:|---:|
| model_944 | 85.18 | 73.21 | -11.97 | 276 | 12 | 6 |
| model_943 | 85.19 | 73.23 | -11.97 | 275 | 12 | 6 |
| model_939 | 84.90 | 73.10 | -11.80 | 271 | 11 | 6 |
| model_941 | 84.89 | 73.10 | -11.79 | 272 | 11 | 6 |
| model_942 | 85.12 | 73.35 | -11.77 | 272 | 12 | 6 |
| model_940 | 85.13 | 73.36 | -11.77 | 271 | 12 | 6 |
| model_938 | 85.11 | 73.34 | -11.77 | 272 | 12 | 6 |
| model_937 | 85.13 | 73.36 | -11.77 | 271 | 12 | 6 |
| model_94 | 82.79 | 71.14 | -11.65 | 152 | 6 | 37 |
| model_4612 | 80.05 | 68.77 | -11.28 | 236 | 7 | 12 |
| model_4614 | 79.94 | 68.68 | -11.26 | 237 | 7 | 12 |
| model_4615 | 79.96 | 68.70 | -11.26 | 235 | 7 | 12 |
| model_4616 | 80.13 | 69.11 | -11.02 | 238 | 8 | 14 |
| model_1943 | 84.35 | 73.42 | -10.93 | 341 | 7 | 0 |
| model_4613 | 80.41 | 69.48 | -10.92 | 238 | 8 | 12 |

Full per-model detail: see the accompanying `.json` report.
