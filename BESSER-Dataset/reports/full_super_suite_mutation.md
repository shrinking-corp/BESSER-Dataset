# Property-Scoped Mutation Testing Report (cosmic-ray, capped)

Generated: 2026-10-19T21:15:17.313650+00:00

Scope: only @property getters and @x.setter setters -- see validate_mutation_properties.py's docstring. Not comparable to validate_mutation.py's whole-file mutation_prototype_report.

- **Total models checked:** 5264
- **Measured successfully:** 5264
- **Average mutation score (killed/run):** 0.7561
- **Average share of whole-file mutants that are in properties:** 0.9747
- **Total mutants in-file (uncapped) across sample:** 1765103
- **Total mutants in-properties (uncapped) across sample:** 1713375
- **Total mutants actually run (post-cap):** 190966
- **Kills that were only a per-mutant timeout:** 54 (in 39 measured models)

## Per-model duration (init+exec, seconds)

- p50: 81.78
- p90: 217.89
- p99: 851.19
- max: 2688.204
- total (sum, sample only): 654509.8

## Breakdown by status

| Status | Count |
|---|---|
| measured | 5264 |

Full per-model detail: see `mutation_properties_report.json`.
