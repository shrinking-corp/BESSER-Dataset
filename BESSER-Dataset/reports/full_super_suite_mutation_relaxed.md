# Property-Scoped Mutation Testing Report (cosmic-ray, capped)

Generated: 2026-10-21T08:26:37.011412+00:00

Scope: only @property getters and @x.setter setters -- see validate_mutation_properties.py's docstring. Not comparable to validate_mutation.py's whole-file mutation_prototype_report.

- **Total models checked:** 407
- **Measured successfully:** 407
- **Average mutation score (killed/run):** 0.8064
- **Average share of whole-file mutants that are in properties:** 0.9722
- **Total mutants in-file (uncapped) across sample:** 282449
- **Total mutants in-properties (uncapped) across sample:** 273499
- **Total mutants actually run (post-cap):** 15480
- **Kills that were only a per-mutant timeout:** 11 (in 10 measured models)

## Per-model duration (init+exec, seconds)

- p50: 126.52
- p90: 486.27
- p99: 1426.69
- max: 2511.624
- total (sum, sample only): 88702.6

## Breakdown by status

| Status | Count |
|---|---|
| measured | 407 |

Full per-model detail: see `mutation_properties_report.json`.
