<!--
  AI-GENERATED DOCUMENT
  Generated/modified by: Visual Studio Claude Code 2.1.236
  Model used:            Claude Opus 5 (claude-opus-5)
  Generated at:          2026-09-10
-->

> **AI marking** — This document was generated/modified by **Visual Studio Claude Code 2.1.236**,
> using **Claude Opus 5** (`claude-opus-5`), generated at **2026-09-10**.
> Figures were produced by the scripts cited under [Reproduction](#reproduction) and
> cross-checked against the existing reports in [`../reports/`](../reports/); the
> interpretation is AI-authored and has not been independently reviewed.

# Zero implemented operations in the B-UML dataset

**Status:** confirmed, dataset-wide (all 9,082 models)
**Discovered:** 2026-09-10, incidental to the no-logic model classification
(`scripts/validate_logic.py`)
**Related:** [`DECISIONS.md`](DECISIONS.md) — entries of 2026-09-10, 2026-09-02 and 2026-09-01

---

## Summary

**Not a single B-UML operation is implemented anywhere in the dataset.**

All **19,768** operations, spread across the **1,037** models that declare any,
have a body consisting of exactly one `pass` statement. There are zero
implemented operation bodies in 9,082 models.

An "operation" here is a B-UML method — the modelling-language equivalent of a
behavioural method on a class, as opposed to an attribute or an association.
In the generated Python they appear as plain methods on a class, distinct from
`__init__`, from `@property` getters and from `@x.setter` setters.

## What the generated code actually looks like

Every stub carries a generator-emitted `# TODO` comment, so this is a
deliberate placeholder rather than an accidental truncation. From
`Dataset/model_100322/python_code.py`:

```python
class pnextensions_pnutils_PnUtils:

    def __init__(self):

        pass
    def layout(self, pnextensions_petriNet):
        # TODO: Implement layout method
        pass
```

The `# TODO: Implement <name> method` marker appears in **1,046** of the 9,082
`python_code.py` files: the 1,037 classified above, plus 9 more that are
`syntax_error` models whose operations could not be counted because the file
does not parse.

## Evidence

| Measure | Value |
|---|---|
| Models in dataset | 9,082 |
| Models declaring ≥ 1 operation | 1,037 |
| Operations declared in total | 19,768 |
| Operations with a real body | **0** |
| Operations that are `pass` stubs | **19,768** (100%) |
| Operations per such model | min 1, median 7, p90 50, max 286 |

Counted by AST, without executing anything: for every `FunctionDef` on a class
that is not `__init__` and carries neither a `@property` nor a `@x.setter`
decorator, the body is checked for being a lone `pass` (also accepting `...` or
a docstring-only body, neither of which occurs in practice).

## Why it matters

### 1. It accounts for essentially every assertion failure in the test suite

The test-validation run found 1,055 of 9,082 models failing, of which **919
fail with `AssertionError`**. Cross-referencing those against the stub-operation
set:

| | Count |
|---|---|
| Models failing with `AssertionError` | 919 |
| ...that have only stubbed operations | **918** |
| ...that do not | 1 |

The single exception is `model_100004`, whose failure has an unrelated cause —
`Literal '' missing in DateVisibleEnum`, an empty-string enum literal, in a
model with no operations at all.

In other words: **the entire `AssertionError` failure class in this dataset is
one bug in the code generator, not 918 separate problems.** The generated
`test_hypothesis.py` asserts that calling an operation changes object state;
the generated `python_code.py` never implements the operation. The tests are
correct and the code is incomplete — the two generators disagree about whether
operation bodies exist.

Note that most stub-operation models still *pass*: of the 1,037, 918 fail with
`AssertionError`, 106 pass outright, 9 time out and 3 have collection errors.
Whether a model fails depends on whether its test generator happened to emit a
state-change assertion for one of its stubs.

### 2. It bounds what mutation testing can ever measure

Mutation testing works by making small semantic changes to code and checking
whether the test suite notices. A `pass` statement has nothing to change — no
operator, no literal, no branch — so operation bodies contribute **zero
mutants**. Every mutation score in this dataset is therefore a score over
association and property-setter logic only, never over behaviour.

This matters when interpreting the prototype's average mutation score of 0.33:
that number describes bidirectional-association consistency code, and says
nothing whatsoever about the behavioural layer of the models, because the
behavioural layer does not exist in code form.

### 3. It makes "implements no logic" ambiguous, deliberately so

Two defensible readings, with very different exclusion sets:

| Reading | Excluded | Encoded as |
|---|---|---|
| No executable statement anywhere in the file | 644 models | `logic_validation.usable == false` |
| No *implemented operation* | +1,037 models | `logic_validation.all_operations_stubbed == true` |

The stricter reading is **not** what `usable: false` encodes. The 1,037
stub-operation models still carry real bidirectional-association logic in their
property setters — genuinely coverable, genuinely mutable — so excluding them
outright would discard measurable code. Both flags are written to every model's
`code_metadata.json`, so either policy can be applied downstream without
re-running anything.

## Recommendation

This is a **generator defect**, not a dataset-curation problem, and it is worth
reporting upstream to the B-UML/BESSER code generator rather than papering over
in the dataset. Two coherent fixes exist, and either would resolve the 918
failures:

1. **Emit operation bodies.** Even a minimal generated body (e.g. assigning to
   the operation's declared return, or raising `NotImplementedError`) would make
   the code honest about its own completeness. `raise NotImplementedError` would
   turn 918 silent assertion failures into an explicit, greppable signal.
2. **Stop generating state-change assertions for unimplemented operations.**
   The test generator can already see that the body is a stub; it should assert
   only what the code claims to do.

Until then, any experiment measuring *behavioural* coverage or mutation score on
this dataset is measuring an empty set, and should say so explicitly.

## Reproduction

```bash
# Full classification, dry run (does not touch the dataset):
python3 scripts/validate_logic.py --workers 8 --reports-dir /tmp/logic-check

# Operation counts, dataset-wide:
python3 - <<'PY'
import json
rep = json.load(open("reports/logic_validation_report.json"))
ops = sum((r["metrics"] or {}).get("operations", 0) for r in rep["results"])
emp = sum((r["metrics"] or {}).get("empty_operations", 0) for r in rep["results"])
print("operations:", ops, "| stubs:", emp, "| implemented:", ops - emp)
PY

# The AssertionError cross-reference:
python3 - <<'PY'
import json
stub = {r["model"] for r in json.load(open("reports/logic_validation_report.json"))["results"]
        if r["all_operations_stubbed"]}
ae = {m["model"] for m in json.load(open("reports/test_validation_report.json"))["failing_models"]
      if m.get("error_type") == "AssertionError"}
print(len(ae), "AssertionError models;", len(ae & stub), "are stub-operation models;",
      len(ae - stub), "are not:", sorted(ae - stub))
PY
```

Sources: [`../reports/logic_validation_report.json`](../reports/logic_validation_report.json),
[`../reports/test_validation_report.json`](../reports/test_validation_report.json),
[`../reports/mutation_prototype_report.json`](../reports/mutation_prototype_report.json).
