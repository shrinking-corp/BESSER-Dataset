# Mutation runs compared: before (A) vs relaxed (B)

Generated: 2026-10-21T08:36:36.821332+00:00

- A: `reports\full_super_suite_mutation.json`
- B: `reports\full_super_suite_mutation_relaxed.json`
- **Models measured in both:** 407
- **Mean score:** A 0.8064 · B 0.8064 · **lift +0.00 pts**
- **Per model (B vs A):** 0 improved · 0 worse · 407 unchanged
- **Perfect scores:** A 5 · B 5 · **zero scores:** A 0 · B 0
- **Same number of mutants run per model:** yes, every model
- **Kills that were only a per-mutant timeout:** A 12 · B 11. Counting all of them as survived: A 0.8057 · B 0.8057 · lift +0.00 pts

## By difficulty bucket

| Bucket | Models | A | B | Lift (pts) | Improved | Worse | Unchanged |
|---|---:|---:|---:|---:|---:|---:|---:|
| 0-10 | 13 | 0.6609 | 0.6609 | +0.00 | 0 | 0 | 13 |
| 10-20 | 36 | 0.7674 | 0.7674 | +0.00 | 0 | 0 | 36 |
| 20-30 | 28 | 0.829 | 0.829 | +0.00 | 0 | 0 | 28 |
| 30-40 | 52 | 0.8313 | 0.8313 | +0.00 | 0 | 0 | 52 |
| 40-50 | 57 | 0.8057 | 0.8057 | +0.00 | 0 | 0 | 57 |
| 50-60 | 81 | 0.8049 | 0.8049 | +0.00 | 0 | 0 | 81 |
| 60-70 | 53 | 0.7925 | 0.7925 | +0.00 | 0 | 0 | 53 |
| 70-80 | 47 | 0.8346 | 0.8346 | +0.00 | 0 | 0 | 47 |
| 80-90 | 36 | 0.8326 | 0.8326 | +0.00 | 0 | 0 | 36 |
| 90-100 | 4 | 0.8062 | 0.8062 | +0.00 | 0 | 0 | 4 |

## Largest drops (B below A), top 20

None: no model scores lower in B than in A.

## Models with a timeout kill on either side

| Model | A score | A timeout kills | B score | B timeout kills |
|---|---:|---:|---:|---:|
| model_100148 | 0.725 | 1 | 0.725 | 1 |
| model_100149 | 0.725 | 2 | 0.725 | 2 |
| model_100152 | 0.775 | 1 | 0.775 | 1 |
| model_100153 | 0.75 | 1 | 0.75 | 1 |
| model_1959 | 0.625 | 1 | 0.625 | 0 |
| model_3260 | 0.8 | 1 | 0.8 | 1 |
| model_3987 | 0.9 | 1 | 0.9 | 1 |
| model_4612 | 0.825 | 1 | 0.825 | 1 |
| model_940 | 0.825 | 1 | 0.825 | 1 |
| model_943 | 0.925 | 1 | 0.925 | 1 |
| model_944 | 0.775 | 1 | 0.775 | 1 |
