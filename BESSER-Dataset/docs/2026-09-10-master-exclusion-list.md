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

**Status:** built and current — last updated 2026-09-17.
**Related:** [`DECISIONS.md`](DECISIONS.md) — "Models with no testable logic"
(the `logic_validation` key), "`model_1339` / `model_1950`: excluded, not
fixable with available tools", "Property-name mismatches: 2 models excluded,
not fixable without breaking ground truth", "Old-suite-unmeasurable models
excluded (79)", and the 2026-09-16/17 combined-test-suite entries.

## At a glance

| `reason_source` | Count | One-line reason |
|---|---|---|
| `logic_validation` | 631 | No executable logic in `python_code.py` at all (static AST check) |
| `old_suite_unmeasurable` | 79 | `test_hypothesis.py` can't be measured: 52 persistent timeouts (Hypothesis-search variance) + 27 hard collection errors |
| `combined_suite_unmeasurable` | 32 | `test_combined.py` can't be measured: 15 coverage timeouts + 17 mutation timeouts, same variance/scale root causes, only surfaced once the two suites were combined |
| `property_name_mismatch` | 2 | `@X.setter` name doesn't match `X` — silent phantom-property bug, unfixable without breaking ground truth |
| `test_infra_unfixable` | 2 | `test_hypothesis.py` broken AND besser's own generator errors on regeneration |
| **Total excluded** | **746** | |
| **Usable** (`reports/usable_models.txt`) | **8,336** | out of 9,082 |

---

## What it combines

Five independent classifications of "models not usable for the
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

- **79 models, `old_suite_unmeasurable`** (added 2026-09-15) — couldn't get a
  reliable `test_hypothesis.py` coverage measurement no matter how the run was
  tuned. Two distinct sub-causes:
  - **52 persistent timeouts.** Not infinite loops — manually confirmed on
    multiple sample models (e.g. `model_100063`, 788 tests) that the *same*
    file finishes in 20-45s on some standalone runs and doesn't finish in
    300s on others, with ~0% CPU load throughout (ruling out contention).
    Root cause: unseeded Hypothesis search occasionally lands on an
    expensive input combination. Tried three escalating attempts (60s/8
    workers → 180s/8 workers → 300s/3 workers, each getting progressively
    more of these to complete) before accepting this as inherent variance,
    not a fixable performance issue — retrying further has diminishing
    returns.
  - **27 `no_coverage_data`** — `test_hypothesis.py` fails to even *collect*
    against these models, e.g. a hard `SyntaxError` from `from` (a reserved
    Python keyword) used as a keyword argument name. A real, pre-existing
    defect in the ground-truth test file itself, not something introduced or
    fixable by this session's work.
- **32 models, `combined_suite_unmeasurable`** (added 2026-09-16/17, once
  `test_combined.py` existed) — the same two failure classes as
  `old_suite_unmeasurable`, but only surfacing once the two suites were
  merged into one larger file, since a bigger baseline runtime makes both
  failure modes more likely to cross a fixed timeout:
  - **15 coverage timeouts.** Escalated once (180s/8 workers): 218/233
    recovered, these 15 didn't. Spot-checked `model_100203` (1,080 tests)
    standalone: finishes in 88.81s with ~0% CPU load — same Hypothesis-
    variance class as above, not a new bug.
  - **17 mutation timeouts.** Mutation reruns the whole suite once per
    mutant (up to 40); root cause here is arithmetic, not variance —
    baseline runtime × up to 40 reruns approaches cosmic-ray's 900s
    overall-timeout for a suite this size. Escalated once to 1800s: 53/70
    recovered; among those, p90/p99 duration was already 1823-1839s, right
    at the new ceiling — these 17 are simply the most extreme tail.
    Recoverable with a much larger timeout, but not worth the per-model
    cost (some approaching an hour) for 17/8,353 models.

`reports/excluded_models_master.json` / `.txt` union all five (**746 models
total**), tagging each with its `reason_source` (`logic_validation` /
`test_infra_unfixable` / `property_name_mismatch` / `old_suite_unmeasurable` /
`combined_suite_unmeasurable`) so a consumer can apply any subset of these
policies without re-deriving the list. The complement — **8,336 usable
models** — is in `reports/usable_models.txt`, meant as a `--models-file`
input to scope expensive dataset-wide runs (mutation testing in particular)
away from models with nothing meaningful, or nothing trustworthy, to
measure.

## Reproduction

```bash
python scripts/validate_logic.py --write-metadata
# then rebuild reports/excluded_models_master.{json,txt} and reports/usable_models.txt
# from the refreshed logic_validation_report.json
```
