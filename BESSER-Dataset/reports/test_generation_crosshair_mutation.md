# Property-Scoped Mutation Testing Report (cosmic-ray, capped)

Generated: 2026-10-01T22:30:28.139072+00:00

Scope: only @property getters and @x.setter setters -- see validate_mutation_properties.py's docstring. Not comparable to validate_mutation.py's whole-file mutation_prototype_report.

- **Total models checked:** 200
- **Measured successfully:** 177
- **Average mutation score (killed/run):** 0.6505
- **Average share of whole-file mutants that are in properties:** 0.9722
- **Total mutants in-file (uncapped) across sample:** 239528
- **Total mutants in-properties (uncapped) across sample:** 231366
- **Total mutants actually run (post-cap):** 7015

## Per-model duration (init+exec, seconds)

- p50: 56.0
- p90: 90.17
- p99: 131.81
- max: 137.219
- total (sum, sample only): 10692.06

## Breakdown by status

| Status | Count |
|---|---|
| measured | 177 |
| missing_file | 23 |

Full per-model detail: see `mutation_properties_report.json`.
