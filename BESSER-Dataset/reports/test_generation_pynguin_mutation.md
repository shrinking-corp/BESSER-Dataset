# Property-Scoped Mutation Testing Report (cosmic-ray, capped)

Generated: 2026-10-01T22:37:08.981848+00:00

Scope: only @property getters and @x.setter setters -- see validate_mutation_properties.py's docstring. Not comparable to validate_mutation.py's whole-file mutation_prototype_report.

- **Total models checked:** 200
- **Measured successfully:** 192
- **Average mutation score (killed/run):** 0.2775
- **Average share of whole-file mutants that are in properties:** 0.9731
- **Total mutants in-file (uncapped) across sample:** 204506
- **Total mutants in-properties (uncapped) across sample:** 197686
- **Total mutants actually run (post-cap):** 7615

## Per-model duration (init+exec, seconds)

- p50: 58.09
- p90: 155.39
- p99: 217.03
- max: 222.21800000000002
- total (sum, sample only): 14971.35

## Breakdown by status

| Status | Count |
|---|---|
| measured | 192 |
| missing_file | 8 |

Full per-model detail: see `mutation_properties_report.json`.
