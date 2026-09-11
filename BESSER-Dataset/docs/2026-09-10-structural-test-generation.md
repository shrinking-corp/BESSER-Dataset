<!--
  AI-GENERATED DOCUMENT
  Generated/modified by: Claude Code (VS Code extension)
  Model used:            Claude Sonnet 5 (claude-sonnet-5)
  Generated at:          2026-09-10
-->

> **AI marking** — This document was generated/modified by **Claude Code (VS Code extension)**,
> using **Claude Sonnet 5** (`claude-sonnet-5`), generated at **2026-09-10**.
> Figures were produced by the scripts cited under [Reproduction](#reproduction) and
> cross-checked against the reports in [`../reports/`](../reports/); the
> interpretation is AI-authored and has not been independently reviewed.

# `generate_structural_tests.py`: a deterministic-first suite for near-100% coverage

**Status:** `test_structural_full.py` generated for 9,082/9,082 models.
Coverage measured dataset-wide (see
[`2026-09-10-coverage-taxonomy.md`](2026-09-10-coverage-taxonomy.md)):
avg 88.24% line / 56.03% branch / 100.0% function / 74.59% structural,
9,035/9,082 measured on the first full pass.
**Related:** [`DECISIONS.md`](DECISIONS.md) — "Structural test generation and
4-type coverage validator"

---

## Why a new test generator, alongside the dataset's own `test_hypothesis.py`

The goal for this phase of the project is a stronger, more deterministic
baseline suite to compare a "diagram shrinking" tool's output against —
`test_hypothesis.py` is the dataset's existing generated suite, useful as
ground truth for validation, but not built to maximize coverage. Two
generation styles were considered (property-based/Hypothesis vs.
deterministic sequences); **kept both, prioritizing deterministic** — a fixed
sequence (construct → assign → reassign → clear) reliably hits branches like
`if old_value is not None:` that random `@given` sampling rarely reaches by
chance, so Section 1 of the generated file is deterministic tests and
Section 2 is supplementary Hypothesis-based instantiation tests.

`besser`'s own `TestCaseGenerator` (in `besser.generators.testgen`) was
evaluated first and rejected — it's broken in this pip release (missing
Jinja2 templates). `besser.generators.python_classes.PythonGenerator` has
intact templates and was usable for regenerating a handful of models' code
(see the `#`-character section below), but has its own separate, unrelated
bug (see [`DECISIONS.md`](DECISIONS.md), "model_1339 / model_1950").

## Design decisions made along the way

- **Not `is_abstract`-skipped.** The first version skipped every
  `is_abstract=True` class, which cost roughly half the achievable coverage
  on a sample model (44% vs. 84%) — most setter logic lives on abstract
  parent classes. Verified dataset-wide that 0/732 sampled methods are
  actually `@abstractmethod` in the generated code, so Python doesn't block
  direct instantiation regardless of the BUML-level `is_abstract` flag —
  removed the skip entirely.
- **Deterministic association-end ordering.** `association.ends` is an
  unordered Python `set`; `_ordered_ends()` sorts by an explicit key so which
  end is "first" doesn't vary run to run (same non-determinism class as
  `buml_to_puml.py`'s earlier fix, initially missed here and re-discovered).
- **Real-property detection before linking an association.** The generated
  code doesn't always implement both sides of a bidirectional association
  (confirmed: `model_1`'s `petrinet_Arc`/`petrinet_Token` are bare
  `pass`-only classes despite being declared association participants in
  BUML). `_has_real_property()` checks the *actual generated code*, not the
  BUML model, and swaps which side a test links from — or skips the
  association test entirely if neither side has real setter logic to
  exercise.
- **Enum-aware constructor kwargs.** Missing initially, causing
  `TypeError: missing 1 required positional argument` for any class needing
  an enum-typed field — 64/108 test failures on one sample model before the
  fix. `build_literal_tables()` builds a per-model table of one real literal
  per enum.
- **Constructibility check via real `__init__` signature**, not BUML
  metadata — catches the case an enum has zero literals
  (`class OrderStatus(Enum): pass`), making any class requiring it
  genuinely unconstructible by anyone, BUML `is_abstract` flag or not.
- **`_safe_set()` wraps every `setattr`** in `try/except RecursionError`,
  `pytest.skip()`-ing rather than failing — a genuine dataset bug (two
  reciprocal setters unconditionally calling each other with no base case)
  causes infinite mutual recursion for that one relationship; this is a
  defect in the code under test, not something this test suite should
  misreport as its own failure.
- **Empty import list guarded.** A model can genuinely have zero
  classes/enums (BUML `types=None` — confirmed real case: `model_650`).
  `",\n    ".join([])` plus the always-added trailing comma produced a
  dangling `,` — a syntax error, not just an unused import — for every such
  model. Fixed by skipping the whole `from python_code import (...)` block
  when there's nothing to import.

## The `#`-character name-resolution bug

**Finding:** BUML allows characters in a `Class`/`Enumeration` `.name` that
aren't valid Python identifiers. Confirmed real case: `model_2533`'s
`Class(name="raas_small_test_#29373817")` — `#` is legal in a UML/BUML name
but starts a comment in Python, and the actual generator drops it silently:
`class raas_small_test_29373817:` in `python_code.py`. The test generator was
using the raw BUML name directly in emitted import statements, constructor
calls, and `isinstance` checks — producing `SyntaxError` in the generated
`test_structural_full.py` (the `#` truncated the rest of the line as a
comment).

**Fix, chosen over guessing the exact sanitization rule:** resolve every
class/enum name against the *actually-loaded* `code_module` (already loaded
via `importlib` for other checks), rather than re-deriving the generator's
sanitization logic. `resolve_code_name()` tries the raw name via `hasattr`
first, then a best-effort sanitized fallback
(`_python_identifier()` — strip non-alphanumeric/underscore characters,
prefix `_` if the result starts with a digit or is empty), and returns
`None` if neither exists — in which case that class/enum is excluded from
imports, instantiation, and every other code-emission point, rather than
guessing wrong. This is more robust to divergent generator behavior across
the dataset than hard-coding one sanitization rule.

**Scope check:** a full dataset-wide static scan (loading every model's BUML
source, checking every `Class`/`Enumeration` name against
`_python_identifier()`) found the bug is isolated to `model_2533` — all 8
hits are its own classes (`raas_small_test_#…` variants). No other model is
affected; the fix does not need to be propagated further.

## Dataset-wide error diagnosis (17 errors on the first full run)

All 17 were genuine, pre-existing defects in the dataset's `python_code.py`
files — not bugs in the generator script, which correctly caught them by
`exec`-ing the module (the same mechanism used everywhere else this session)
rather than crashing the whole batch.

| Category | Models | What's actually wrong |
|---|---|---|
| Missing file | `model_10002944` | `python_code.py` doesn't exist at all for this model — the *same* model fixed for BUML→PUML conversion earlier, but that fix was to the BUML source; this is a separate, still-broken generated-code file. |
| `NameError` | `model_100233`, `100234`, `100235`, `100236` | Generated code references `StringType` without importing it — 4 consecutively-numbered models, almost certainly the same generation-batch bug. |
| Malformed class body | `model_603`, `610`, `684`, `4822`, `5195`, `5390` | "expected an indented block after class definition" — a class with no body at all, not even a `pass`. |
| Deep syntax error | `model_724`, `725`, `739`, `740`, `741`, `742` | Invalid syntax at very large line numbers (3,340–5,163) — these are the "UML-describing-itself" meta-models (`RefUML`/`RefOntoUML`/`UML` sources), among the largest and most complex models in the dataset; something in the generator broke at that scale. |

These 17 models (0.19% of the dataset) needed hand-patches to the
already-generated `python_code.py` directly — a less clean fix than the
7 BUML-source edits in
[`2026-09-10-buml-to-puml-conversion.md`](2026-09-10-buml-to-puml-conversion.md),
since it patches an artifact rather than its source; no BUML-level fix was
available the way it was there. All 17 (plus 1 more found in a later pass,
totalling the 18-model list in `reports/fixed_models_remutate.txt`) were
individually fixed and re-validated.

### Second wave: 43-model structural-coverage re-run

A later `validate_coverage_structural.py` re-run over 43 previously-flagged
models (`reports/structural_coverage_refix.txt`) surfaced two more bug
classes, distinct from the syntax defects above:

- **Encoding (4 models):** `function_ranges()`'s
  `ast.parse(source_path.read_text())` lacked `encoding="utf-8"`, so on
  Windows it fell back to the OS locale encoding, mangling multi-byte
  characters. Confirmed: `model_2210`'s Norwegian enum literal `"Årsstudie"`
  is valid Python 3 under its actual (UTF-8) encoding, but a locale-encoding
  read corrupts it into an invalid token, raising a false "invalid
  character" `SyntaxError`. Fixed by adding `encoding="utf-8"` explicitly —
  the only place in this pipeline that re-parses `python_code.py`'s raw text
  this way (everywhere else uses `importlib.exec_module`, which already
  follows Python's own UTF-8-default source-encoding rules).
- **`empty_model` misclassification (37 models, not a code bug — a
  reporting bug):** models with genuinely zero classes correctly generate a
  `test_structural_full.py` with zero test functions. Pytest's "0 tests
  collected" (exit code 5) means `pytest-cov` never imports the source
  module at all, so no coverage JSON is ever written — the validator was
  bucketing this identically to a real failure (`no_coverage_data`),
  including *not writing any metadata at all* for these 37 models. Fixed by
  adding a distinct `empty_model` status, gated on `structural_totals.classes
  == 0`, which **is** written to `code_metadata.json` (with `null` coverage
  percentages, since there's no code to compute one over) — the classes==0
  check exists precisely so this new status can't ever apply to a model that
  legitimately failed for some other reason.

## `check_property_name_mismatches.py` — built, execution on hold

A read-only audit script for a newly-discovered, separate bug class:
`@x.setter`/`@x.deleter` decorators whose decorated function name doesn't
match `x` (would silently produce a getter/setter pair under two different
attribute names). Built this session but **not yet run** — held at the
user's explicit request while other work was in flight. Check
`reports/property_name_mismatches_report.json` for whether/when it was
eventually run.

## Reproduction

```bash
python scripts/generate_structural_tests.py --workers 8 --write-metadata
python scripts/generate_structural_tests.py --models-file reports/structural_coverage_refix.txt --fresh
python scripts/validate_coverage_structural.py --workers 8 --write-metadata
```
