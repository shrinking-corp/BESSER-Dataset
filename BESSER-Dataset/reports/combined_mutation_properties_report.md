# Property-Scoped Mutation Testing Report (cosmic-ray, capped)

Generated: 2026-09-17T17:55:00.206850+00:00

Scope: only @property getters and @x.setter setters -- see validate_mutation_properties.py's docstring. Not comparable to validate_mutation.py's whole-file mutation_prototype_report.

- **Total models checked:** 8336
- **Measured successfully:** 8284
- **Average mutation score (killed/run):** 0.4382
- **Average share of whole-file mutants that are in properties:** 0.974
- **Total mutants in-file (uncapped) across sample:** 2558737
- **Total mutants in-properties (uncapped) across sample:** 2482009
- **Total mutants actually run (post-cap):** 294661

## Per-model duration (init+exec, seconds)

- p50: 88.11
- p90: 212.48
- p99: 557.73
- max: 916.642
- total (sum, sample only): 977262.95

## Breakdown by status

| Status | Count |
|---|---|
| measured | 8258 |
| timeout | 38 |
| exec_error | 27 |
| error | 12 |
| init_error | 1 |

Full per-model detail: see `mutation_properties_report.json`.
