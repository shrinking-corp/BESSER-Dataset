# Property-Scoped Mutation Testing Report (cosmic-ray, capped)

Generated: 2026-09-17T19:47:36.121782+00:00

Scope: only @property getters and @x.setter setters -- see validate_mutation_properties.py's docstring. Not comparable to validate_mutation.py's whole-file mutation_prototype_report.

- **Total models checked:** 2
- **Measured successfully:** 2
- **Average mutation score (killed/run):** 1.0
- **Average share of whole-file mutants that are in properties:** 0.9753
- **Total mutants in-file (uncapped) across sample:** 5922
- **Total mutants in-properties (uncapped) across sample:** 5778
- **Total mutants actually run (post-cap):** 80

## Per-model duration (init+exec, seconds)

- p50: 144.58
- p90: 144.58
- p99: 144.58
- max: 144.578
- total (sum, sample only): 271.05

## Breakdown by status

| Status | Count |
|---|---|
| measured | 2 |

Full per-model detail: see `mutation_properties_report.json`.
