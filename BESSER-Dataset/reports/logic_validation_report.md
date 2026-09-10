# Logic Validation Report (static, AST-based)

Generated: 2026-09-10T16:10:49.106723+00:00

- **Total models checked:** 9082
- **Usable (contain testable logic):** 8438
- **Excluded (no testable logic / unreadable):** 644
- **Usable rate:** 92.91%

## Breakdown by status

| Status | Usable | Count |
|---|---|---|
| has_logic | yes | 8438 |
| no_logic | no | 630 |
| syntax_error | no | 12 |
| missing_file | no | 1 |
| empty_file | no | 1 |

## Logic present in the usable models

| Metric | Total |
|---|---|
| Classes | 246183 |
| Statements inside method bodies | 2663997 |
| ...of which introduce control flow | 1025107 |
| Operations (B-UML methods) | 19596 |
| ...of which are `pass` stubs | 19596 |

**1037** usable models have at least one operation and *every* one of them is a `pass` stub. These are still usable (their property setters carry real association logic) but their operations contribute nothing to a mutation score -- see `all_operations_stubbed` in each model's metadata.

Excluded models are listed one per line in `excluded_models_no_logic.txt`.
Full per-model detail: see `logic_validation_report.json` and each model's `code_metadata.json`.
