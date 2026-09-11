# Property-Scoped Mutation Testing Report (cosmic-ray, capped)

Generated: 2026-09-11T08:23:01.652541+00:00

Scope: only @property getters and @x.setter setters -- see validate_mutation_properties.py's docstring. Not comparable to validate_mutation.py's whole-file mutation_prototype_report.

- **Total models checked:** 8447
- **Measured successfully:** 8417
- **Average mutation score (killed/run):** 0.4104
- **Average share of whole-file mutants that are in properties:** 0.9739
- **Total mutants in-file (uncapped) across sample:** 2849510
- **Total mutants in-properties (uncapped) across sample:** 2762176
- **Total mutants actually run (post-cap):** 300184

## Per-model duration (init+exec, seconds)

- p50: 58.7
- p90: 127.78
- p99: 419.99
- max: 926.937
- total (sum, sample only): 652590.52

## Breakdown by status

| Status | Count |
|---|---|
| measured | 8417 |
| timeout | 26 |
| error | 4 |

Full per-model detail: see `mutation_properties_report.json`.
