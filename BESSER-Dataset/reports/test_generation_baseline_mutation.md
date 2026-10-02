# Property-Scoped Mutation Testing Report (cosmic-ray, capped)

Generated: 2026-10-01T20:54:04.124990+00:00

Scope: only @property getters and @x.setter setters -- see validate_mutation_properties.py's docstring. Not comparable to validate_mutation.py's whole-file mutation_prototype_report.

- **Total models checked:** 200
- **Measured successfully:** 200
- **Average mutation score (killed/run):** 0.5085
- **Average share of whole-file mutants that are in properties:** 0.9724
- **Total mutants in-file (uncapped) across sample:** 249630
- **Total mutants in-properties (uncapped) across sample:** 241036
- **Total mutants actually run (post-cap):** 7935

## Per-model duration (init+exec, seconds)

- p50: 147.0
- p90: 721.14
- p99: 1020.53
- max: 1057.5149999999999
- total (sum, sample only): 52190.93

## Breakdown by status

| Status | Count |
|---|---|
| measured | 200 |

Full per-model detail: see `mutation_properties_report.json`.
