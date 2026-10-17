# Generator Fidelity Report, by NAME (BUML model vs. generated code)

Generated: 2026-10-11T18:37:39.844532+00:00

Unlike `generator_fidelity_report` (counts only), this checks whether each specific class/attribute/operation the model declares actually exists in the generated code, by name -- a count match does not imply a name match. See the script's docstring for what counts as a real miss vs. expected, unflagged asymmetry (code-side association accessors / `__init__` / property getters-setters, same reasoning as the count-based report).

- **Total models:** 8336
- **Compared:** 8336
- **Models with >=1 real mismatch:** 2 (0.02%)
- **Models with >=1 missing class:** 1
- **Models with >=1 missing attribute:** 1
- **Models with >=1 missing operation:** 0
- **Total missing classes across dataset:** 1
- **Total missing attributes across dataset:** 1
- **Total missing operations across dataset:** 0

## Breakdown by status

| Status | Count |
|---|---|
| compared | 8336 |

## Top 50 worst models (by total missing classes+attributes+operations)

| Model | Classes missing | Attributes missing | Operations missing | Total |
|---|---|---|---|---|
| model_10001897 | 0 | 1 | 0 | 1 |
| model_10001985 | 1 | 0 | 0 | 1 |

Full per-model, per-class detail (exact missing names): see the accompanying `.json` report.
