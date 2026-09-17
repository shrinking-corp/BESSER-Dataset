# Property-Scoped Mutation Testing Report (cosmic-ray, capped)

Generated: 2026-09-17T19:42:27.914015+00:00

Scope: only @property getters and @x.setter setters -- see validate_mutation_properties.py's docstring. Not comparable to validate_mutation.py's whole-file mutation_prototype_report.

- **Total models checked:** 12
- **Measured successfully:** 12
- **Average mutation score (killed/run):** 0.5604
- **Average share of whole-file mutants that are in properties:** 0.9605
- **Total mutants in-file (uncapped) across sample:** 39614
- **Total mutants in-properties (uncapped) across sample:** 38034
- **Total mutants actually run (post-cap):** 480

## Per-model duration (init+exec, seconds)

- p50: 511.74
- p90: 685.56
- p99: 710.92
- max: 710.9219999999999
- total (sum, sample only): 5572.61

## Breakdown by status

| Status | Count |
|---|---|
| measured | 12 |

Full per-model detail: see `mutation_properties_report.json`.
