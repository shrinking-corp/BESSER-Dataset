<!--
  AI-GENERATED DOCUMENT
  Generated/modified by: Claude Code (VS Code extension)
  Model used:            Claude Sonnet 5 (claude-sonnet-5)
  Generated at:          2026-09-10
-->

> **AI marking** — This document was generated/modified by **Claude Code (VS Code extension)**,
> using **Claude Sonnet 5** (`claude-sonnet-5`), generated at **2026-09-10**.
> Interpretation is AI-authored and has not been independently reviewed.

# Master exclusion list

**Status:** built and current — `logic_validation` was re-run after this
session's 18 `python_code.py` fixes landed, so the counts below reflect the
fixed state (no known staleness).
**Related:** [`DECISIONS.md`](DECISIONS.md) — "Models with no testable logic"
(the `logic_validation` key), "`model_1339` / `model_1950`: excluded, not
fixable with available tools", and "Property-name mismatches: 2 models
excluded, not fixable without breaking ground truth"

---

## What it combines

Three independent classifications of "models not usable for the
coverage/mutation experiments," for different reasons:

- **`logic_validation.usable == false`** (631 models, all `no_logic` — 0
  `syntax_error`, `missing_file`, or `empty_file` after the re-run; the 12
  `syntax_error` and 1 `missing_file` models from the original 644-model
  count were exactly the ones this session fixed, see
  [`2026-09-10-structural-test-generation.md`](2026-09-10-structural-test-generation.md))
  — static AST classification, catching models with no executable code at
  all.
- **`model_1339` / `model_1950`** (2 models — their `python_code.py`
  genuinely has real logic per static analysis) — excluded for an unrelated
  reason: their `test_hypothesis.py` is broken, and besser's own
  `PythonGenerator` raises a *new*
  `SyntaxError: non-default argument follows default argument` when
  regeneration is attempted. No available fix on either side.
- **`model_10001058` / `model_2881`** (2 models — found by
  `scripts/check_property_name_mismatches.py`) — a `@X.setter`/`@X.deleter`
  decorated function whose name doesn't match `X` (e.g. `@class2.setter`
  decorating a function named `class1`). This silently creates a phantom
  duplicate property under the wrong name instead of a working setter on the
  intended attribute (`instance.class2 = ...` raises `AttributeError`;
  `instance.class1 = ...` — the accidental byproduct — works).
  `test_hypothesis.py` for both models already asserts against the buggy
  name, so renaming to fix it would break currently-passing ground truth;
  marked and excluded instead, matching the "mark, don't delete/patch when
  the alternative breaks something else" policy applied to `logic_validation`.

`reports/excluded_models_master.json` / `.txt` union all three (**635 models
total**), tagging each with its `reason_source` (`logic_validation` /
`test_infra_unfixable` / `property_name_mismatch`) so a consumer can apply
any subset of these policies without re-deriving the list. The complement —
**8,447 usable models** — is in `reports/usable_models.txt`, meant as a
`--models-file` input to scope expensive dataset-wide runs (mutation testing
in particular) away from models with nothing meaningful, or nothing
trustworthy, to measure.

## Reproduction

```bash
python scripts/validate_logic.py --write-metadata
# then rebuild reports/excluded_models_master.{json,txt} and reports/usable_models.txt
# from the refreshed logic_validation_report.json
```
