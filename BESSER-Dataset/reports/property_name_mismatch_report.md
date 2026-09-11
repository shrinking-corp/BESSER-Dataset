# Property Setter/Deleter Name-Mismatch Audit

Generated: 2026-09-10T20:22:22.527612+00:00

Read-only audit for `@X.setter`/`@X.deleter` decorators whose decorated function isn't actually named X -- a silent defect that doesn't prevent loading, so nothing else in this pipeline would otherwise catch it. See the script's docstring for the confirmed real-world example this was built to hunt for.

- **Total models checked:** 9082
- **Models with at least one mismatch:** 2
- **Total mismatches found:** 2

## Breakdown by status

| Status | Count |
|---|---|
| checked | 9082 |

## Models with mismatches

| Model | Class | Expected | Actual def name | Kind | Line |
|---|---|---|---|---|---|
| model_10001058 | result | class2 | class1 | setter | 1000 |
| model_2881 | express_Reference | self1 | self | setter | 860 |

Full per-model detail: see the accompanying `.json` report.
