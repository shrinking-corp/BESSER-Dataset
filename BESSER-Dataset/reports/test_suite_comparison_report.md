# BESSER-Dataset — New vs. Original Test Suite: Coverage & Mutation Comparison

*Generated 2026-09-11 (updated same day once the property-scoped mutation run
completed). Consolidates the new deterministic-first test suite's coverage against
the original generated suite's, and compares whole-file vs. property-scoped
mutation scoring on the original suite. Source data: `reports/*.json` and current
`code_metadata.json` per model. Methodology notes: `docs/DECISIONS.md`.*

**Two test suites exist per model:**
- **`test_hypothesis.py`** — the dataset's original generated suite (a structural
  half of plain assertions + a hypothesis-strategies half of `@given` tests).
- **`test_structural_full.py`** — this session's deterministic-first suite, built
  for near-complete coverage (see `docs/2026-09-10-structural-test-generation.md`).

---

## At a glance

| | |
|---|---|
| Old suite — structural-half line coverage | **48.04%** (9,004 / 9,082 measured) |
| Old suite — hypothesis-half line coverage | **75.12%** (8,781 / 9,082 measured) |
| **New suite — line coverage** | **88.24%** (9,041 / 9,082 measured, +37 `empty_model`) |
| New suite — branch coverage | 56.03% |
| New suite — function coverage | 100.00% |
| New suite — structural coverage (diagram-fidelity) | 74.60% |
| Old suite — whole-file mutation score | **40.58%** (8,424 / 9,082 measured) |
| Old suite — property-scoped mutation score | **41.04%** (8,417 / 8,447 measured) |

The new suite's line coverage (88.24%) clears **both halves** of the old suite by a
wide margin — well above the hypothesis half (75.12%) and nearly double the
structural half (48.04%). New-suite mutation testing hasn't run yet (needs the
`--test-file` parameterization discussed but not yet built, to point the existing
mutation scripts at `test_structural_full.py`), so this report only compares
whole-file vs. property-scoped mutation on the *old* suite.

---

## 1. Coverage: old suite vs. new suite

These two coverage measurements answer related but not identical questions, so
they aren't a perfect apples-to-apples comparison — noted explicitly rather than
forced into one number:

- **Old suite (`coverage_split_prototype_report.json`)** splits `test_hypothesis.py`
  into its two *test-style* halves (structural-assertion vs. `@given`-hypothesis) and
  reports each half's own line coverage of `python_code.py` in isolation.
- **New suite (`structural_coverage_validation`, per-model `code_metadata.json`)**
  measures the *whole* `test_structural_full.py` file (it isn't split by style) across
  four distinct coverage types.

| Metric | Old suite | New suite |
|---|---|---|
| Line coverage | 48.04% (structural half) / 75.12% (hypothesis half) | **88.24%** |
| Branch coverage | not measured | 56.03% |
| Function coverage | not measured | 100.00% |
| Structural (diagram-fidelity) coverage | not measured | 74.60% |
| Models measured | 9,004 (structural) / 8,781 (hypothesis) | 9,041 measured + 37 `empty_model` (genuinely 0-class models, correctly excluded) |

**Read:** the new suite's deterministic-first design (construct → assign →
reassign → clear sequences, see `docs/2026-09-10-structural-test-generation.md`)
reaches substantially more of `python_code.py` than either half of the original
suite — even the hypothesis half, which the original report already noted covers
more than its own structural half (property-based fuzzing walks more code per
test than fixed assertions). The new suite adds branch, function, and
diagram-fidelity ("structural") coverage as measurements the old suite never had at
all, at some real cost: branch coverage (56.03%) is markedly lower than line
coverage (88.24%), meaning many of the `if old_value is not None:`-style
conditionals in this dataset's bidirectional-setter logic are still only being
exercised from one direction — a concrete next-improvement target for the
generator, not just a suite-vs-suite difference.

---

## 2. Mutation testing: whole-file vs. property-scoped (old suite only)

Both scores are measured against **`test_hypothesis.py`** (mutation testing hasn't
been re-pointed at the new suite yet). The difference between the two rows is
*which lines of `python_code.py` cosmic-ray is allowed to mutate*, not which test
file runs:

- **Whole-file** (`mutation_validation`) — cosmic-ray may mutate anywhere in
  `python_code.py`, including `__init__` bodies.
- **Property-scoped** (`mutation_validation_properties`) — mutants are restricted
  to `@property`/`@x.setter` line ranges only (decorator lines included); `__init__`
  and plain operations are out of scope by design. See
  `docs/2026-09-10-mutation-scope-property-setters.md` for why (in short: almost
  all of this dataset's non-stub logic lives in property setters, so a score scoped
  to just that region is more comparable across models than one where each
  model's `__init__`-to-setter logic ratio varies).

| | Whole-file | Property-scoped |
|---|---|---|
| Status | complete | complete |
| Models checked | 9,082 | 8,447 (`usable_models.txt` — 631 excluded models never run) |
| Models measured | 8,424 | 8,417 |
| Avg. mutation score | **40.58%** | **41.04%** |
| Total mutants run (post-cap) | 299,920 | 300,184 |
| Total killed | 104,547 | ~123,240 (41.04% of 300,184) |
| Avg. share of whole-file mutants that are property-region | — | **97.39%** |

**Read:** the two scores are nearly identical — 40.58% whole-file vs. 41.04%
property-scoped, less than half a point apart. The reason is now confirmed
directly rather than inferred: on average, **97.39% of a model's whole-file
mutants already fall inside property/setter regions** — `__init__` and plain
operations contribute almost nothing to the mutant pool in the first place
(consistent with "almost all non-stub logic lives in setters"). So scoping to
properties isn't filtering out a competing signal, it's mostly just
confirming what whole-file mutation was already measuring — its real value is
giving every model a score over a *consistently-defined* region (property
logic) rather than one whose composition varies model to model depending on
how much `__init__` logic happens to exist.

---

## Key takeaways

1. **The new suite covers more code than either half of the old one**, by a wide
   margin on line coverage (88.24% vs. 48.04%/75.12%), and adds three coverage
   dimensions (branch, function, structural) the old suite's methodology never
   measured at all.
2. **Branch coverage is the new suite's weakest dimension** (56.03%, vs. 88.24%
   line) — a concrete signal that bidirectional-setter conditionals are still
   often exercised from only one direction, independent of which test suite is
   used.
3. **Scoping mutation to properties barely moves the average** on the old suite
   (40.58% → 41.04%) — confirmed, not provisional: 97.39% of whole-file mutants
   are already in property regions, so `__init__`/operation mutants were never a
   large share of the signal to begin with.
4. **The real open comparison — mutation score of the new suite vs. the old
   one — hasn't been run yet.** That requires parameterizing `validate_mutation.py`
   / `validate_mutation_properties.py` with a `--test-file` option (discussed,
   not yet built) and running both against `test_structural_full.py`.

## Source reports

| Report | Scope | Files |
|---|---|---|
| Old-suite coverage (structural/hypothesis split) | 9,082 (full) | `coverage_split_prototype_report.{json,md}` |
| New-suite coverage (line/branch/function/structural) | 9,082 (full) | `structural_coverage_report.{json,md}` + per-model `code_metadata.json` |
| Old-suite mutation, whole-file | 9,082 (full) | `mutation_full_dataset_report.{json,md}` + per-model `code_metadata.json` |
| Old-suite mutation, property-scoped | 8,447 (`usable_models.txt`), full | `mutation_properties_report.{json,md}` + per-model `code_metadata.json` |

Aggregate averages in this report were recomputed directly from current
`code_metadata.json` files (not the original aggregate JSON reports, which predate
this session's 18/43-model fix batches) except where noted otherwise, so the
whole-file mutation and new-suite coverage figures reflect the dataset's current,
post-fix state.
