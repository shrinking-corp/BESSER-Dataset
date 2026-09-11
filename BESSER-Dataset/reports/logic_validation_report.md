# Logic Validation Report (static, AST-based)

Generated: 2026-09-10T20:07:32.102696+00:00

- **Total models checked:** 9082
- **Usable (contain testable logic):** 8451
- **Excluded (no testable logic / unreadable):** 631
- **Usable rate:** 93.05%

## Breakdown by status

| Status | Usable | Count |
|---|---|---|
| has_logic | yes | 8451 |
| no_logic | no | 631 |

## Logic present in the usable models

| Metric | Total |
|---|---|
| Classes | 246933 |
| Statements inside method bodies | 2678203 |
| ...of which introduce control flow | 1031235 |
| Operations (B-UML methods) | 20687 |
| ...of which are `pass` stubs | 20687 |

**1046** usable models have at least one operation and *every* one of them is a `pass` stub. These are still usable (their property setters carry real association logic) but their operations contribute nothing to a mutation score -- see `all_operations_stubbed` in each model's metadata.

Excluded models are listed one per line in `excluded_models_no_logic.txt`.
Full per-model detail: see `logic_validation_report.json` and each model's `code_metadata.json`.
