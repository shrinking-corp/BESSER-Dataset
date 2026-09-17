# Property-Scoped Mutation Testing Report (cosmic-ray, capped)

Generated: 2026-09-16T15:31:15.389117+00:00

Scope: only @property getters and @x.setter setters -- see validate_mutation_properties.py's docstring. Not comparable to validate_mutation.py's whole-file mutation_prototype_report.

- **Total models checked:** 4
- **Measured successfully:** 4
- **Average mutation score (killed/run):** 0.35
- **Average share of whole-file mutants that are in properties:** 0.9682
- **Total mutants in-file (uncapped) across sample:** 2330
- **Total mutants in-properties (uncapped) across sample:** 2262
- **Total mutants actually run (post-cap):** 160

## Per-model duration (init+exec, seconds)

- p50: 40.08
- p90: 43.22
- p99: 43.22
- max: 43.218
- total (sum, sample only): 148.47

## Breakdown by status

| Status | Count |
|---|---|
| measured | 4 |

Full per-model detail: see `mutation_properties_report.json`.
