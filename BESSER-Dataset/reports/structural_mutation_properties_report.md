# Property-Scoped Mutation Testing Report (cosmic-ray, capped)

Generated: 2026-09-16T14:57:52.682762+00:00

Scope: only @property getters and @x.setter setters -- see validate_mutation_properties.py's docstring. Not comparable to validate_mutation.py's whole-file mutation_prototype_report.

- **Total models checked:** 8368
- **Measured successfully:** 8364
- **Average mutation score (killed/run):** 0.3597
- **Average share of whole-file mutants that are in properties:** 0.9739
- **Total mutants in-file (uncapped) across sample:** 2708183
- **Total mutants in-properties (uncapped) across sample:** 2625235
- **Total mutants actually run (post-cap):** 297324

## Per-model duration (init+exec, seconds)

- p50: 77.12
- p90: 106.94
- p99: 195.25
- max: 423.53099999999995
- total (sum, sample only): 662304.82

## Breakdown by status

| Status | Count |
|---|---|
| measured | 8364 |
| error | 4 |

Full per-model detail: see `mutation_properties_report.json`.
