# Method Logic Classification Report (static, AST-based)

Generated: 2026-09-29T20:06:46.742160+00:00

Every method in every model's `python_code.py` classified as `no_logic` (empty/stub body), `trivial` (plain assignment/return/getter/setter, no branching or computation of any value), or `has_logic` (a loop, multi-branch conditional, `try`, `match`, comprehension, or arithmetic/boolean computation).

- **Total models:** 8336
- **Measured:** 8336

## Breakdown by status

| Status | Count |
|---|---|
| measured | 8336 |

## Method counts across all measured models

| Category | Methods | Share of methods | Models with ≥1 such method | Share of models |
|---|---|---|---|---|
| no_logic | 14256 | 2.23% | 947 | 11.36% |
| trivial | 461776 | 72.13% | 8336 | 100.00% |
| has_logic | 164185 | 25.65% | 7344 | 88.10% |
| **Total methods** | **640217** | | | |

**7344** models have at least one `has_logic` method (Phase 4's sample should be drawn from these). **992** measured models have none at all -- every method is either a stub or a plain assignment/getter/setter, so no test-generation library targeting logic would have anything to work with there.

## Per-model distribution: how many has_logic methods does a model have?

| has_logic methods | Models | Share |
|---|---|---|
| 0 | 992 | 11.9% |
| 1-5 | 1629 | 19.54% |
| 6-10 | 1691 | 20.29% |
| 11-20 | 1649 | 19.78% |
| 21-50 | 1686 | 20.23% |
| 51-100 | 483 | 5.79% |
| 101-200 | 158 | 1.9% |
| 200+ | 48 | 0.58% |

Mean has_logic methods/model: **19.7** (median **10.0**). Mean total methods/model: **76.8** (median **43.0**).

## Per-model distribution: how many methods does a model have in total?

| Total methods | Models | Share |
|---|---|---|
| 0 | 0 | 0.0% |
| 1-10 | 957 | 11.48% |
| 11-25 | 1682 | 20.18% |
| 26-50 | 1926 | 23.1% |
| 51-100 | 2162 | 25.94% |
| 101-200 | 924 | 11.08% |
| 201-500 | 574 | 6.89% |
| 500+ | 111 | 1.33% |

Among the **992** models with zero `has_logic` methods, average total method count is **13.85** (median **6.0**, max **162**) -- these are consistently small models, not large models that merely happen to lack complex logic.

## Top 50 models by has_logic method count

| Model | has_logic methods | Total methods |
|---|---|---|
| model_1933 | 589 | 1672 |
| model_5063 | 528 | 1258 |
| model_455 | 370 | 961 |
| model_456 | 370 | 961 |
| model_452 | 363 | 909 |
| model_453 | 363 | 909 |
| model_5149 | 362 | 1104 |
| model_5150 | 362 | 1104 |
| model_10041 | 351 | 884 |
| model_450 | 351 | 884 |
| model_451 | 351 | 884 |
| model_2456 | 336 | 896 |
| model_5058 | 330 | 886 |
| model_5059 | 330 | 886 |
| model_5060 | 330 | 886 |
| model_5061 | 326 | 876 |
| model_1929 | 311 | 875 |
| model_1930 | 311 | 875 |
| model_5062 | 310 | 826 |
| model_457 | 309 | 777 |
| model_1125 | 301 | 895 |
| model_2457 | 297 | 842 |
| model_2458 | 297 | 842 |
| model_1148 | 283 | 817 |
| model_2455 | 274 | 710 |
| model_3992 | 265 | 764 |
| model_3993 | 265 | 764 |
| model_3987 | 257 | 784 |
| model_3988 | 257 | 784 |
| model_3986 | 255 | 780 |
| model_3260 | 253 | 687 |
| model_3261 | 253 | 687 |
| model_2898 | 249 | 1039 |
| model_2845 | 246 | 748 |
| model_4849 | 245 | 747 |
| model_4850 | 245 | 747 |
| model_5064 | 233 | 625 |
| model_116 | 227 | 613 |
| model_713 | 226 | 671 |
| model_714 | 226 | 671 |
| model_1838 | 224 | 750 |
| model_3087 | 224 | 678 |
| model_3088 | 223 | 1016 |
| model_2864 | 218 | 544 |
| model_2621 | 205 | 805 |
| model_3266 | 204 | 566 |
| model_3267 | 204 | 566 |
| model_3268 | 204 | 566 |
| model_711 | 197 | 608 |
| model_712 | 197 | 608 |

Per-model totals (no_logic/trivial/has_logic counts): see `method_logic_classification_report.json`. Full per-method detail (which specific methods are has_logic) is written into each model's own `code_metadata.json` under the `method_logic_classification` key, not duplicated in this aggregate report.
