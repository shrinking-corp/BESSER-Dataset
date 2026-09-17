# Generator Fidelity Report (BUML model vs. generated code)

Generated: 2026-09-16T17:13:38.094408+00:00

Cross-references `model_metadata.json` (what the BUML model declares) against `code_structure.json` (what python_code.py's syntax tree actually has, via tree-sitter). See the script's docstring for which fields are directly comparable vs. reported-only.

- **Total models:** 9082
- **Compared:** 9081
- **Models with a mismatch (classes/abstract_classes/enumerations delta != 0):** 3711 (40.87%)

## Directly-comparable fields

| Field | Compared | Nonzero delta | Avg delta (code - model) |
|---|---|---|---|
| classes | 9081 | 2830 | 0.9947 |
| abstract_classes | 9081 | 1960 | -1.5592 |
| enumerations | 9081 | 1 | -0.0002 |

## Reported-only fields (mismatch EXPECTED, not flagged -- see docstring)

| Field | Compared | Avg delta (code - model) |
|---|---|---|
| attributes | 9081 | 21.2233 |
| methods | 9081 | 75.3186 |

## Breakdown by status

| Status | Count |
|---|---|
| compared | 9081 |
| missing_file | 1 |

Mismatched models listed in the accompanying `.json` report's `mismatched_models`.
