# Property-Scoped Mutation Testing Report (cosmic-ray, capped)

Generated: 2026-09-17T19:23:49.251292+00:00

Scope: only @property getters and @x.setter setters -- see validate_mutation_properties.py's docstring. Not comparable to validate_mutation.py's whole-file mutation_prototype_report.

- **Total models checked:** 38
- **Measured successfully:** 38
- **Average mutation score (killed/run):** 0.4789
- **Average share of whole-file mutants that are in properties:** 0.9735
- **Total mutants in-file (uncapped) across sample:** 58648
- **Total mutants in-properties (uncapped) across sample:** 56580
- **Total mutants actually run (post-cap):** 1520

## Per-model duration (init+exec, seconds)

- p50: 1146.3
- p90: 1413.25
- p99: 1806.3
- max: 1806.2959999999998
- total (sum, sample only): 43035.44

## Breakdown by status

| Status | Count |
|---|---|
| measured | 38 |

Full per-model detail: see `mutation_properties_report.json`.
