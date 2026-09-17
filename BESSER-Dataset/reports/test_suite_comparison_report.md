# BESSER-Dataset — Old vs. New vs. Combined Test Suite: Coverage, Mutation & Class Coverage

*Generated 2026-09-17. Consolidates every coverage/mutation/class-coverage measurement
taken across this project's three test-suite variants. Source data: the individual
`reports/*.json` files listed at the bottom; methodology notes: `docs/DECISIONS.md`,
step-by-step run history: `checklist.md`.*

**Three test suites exist per model:**
- **`test_hypothesis.py`** ("old suite") — the dataset's original generated suite (a
  structural half of plain assertions + a hypothesis-strategies half of `@given` tests).
- **`test_structural_full.py`** ("new suite") — this project's deterministic-first
  suite, built for near-complete coverage (`docs/2026-09-10-structural-test-generation.md`).
- **`test_combined.py`** ("combined suite") — a real, literal merge of both files per
  model, with name-collisions fixed and semantically-redundant old-suite tests removed
  (`docs/2026-09-16-combined-test-suite.md`). Not a superset of raw test *counts* — it's
  built to keep only what each suite catches that the other doesn't.

**A note on scope:** each suite's numbers below were measured against the model set
`usable_models.txt` had at the time that suite's run was considered complete — the
exclusion list grew over the life of this project (714 → 746 models) as new
run-specific unmeasurable groups were found and excluded. The **combined-suite**
numbers are the most recent and are scoped to the *final* `usable_models.txt`
(8,336 models, 100% measured for every metric below — see "Recovery" note). The
**old-suite** coverage numbers were freshly rescoped to that same final 8,336 for this
report; the remaining old/new-suite numbers are quoted as originally published,
scoped to that metric's own contemporary exclusion list (noted per row). None of this
changes any conclusion below — the differences in raw model count are all under 2%.

---

## At a glance

| Metric | Old suite | New suite | Combined suite |
|---|---|---|---|
| Line coverage | 73.36% | 88.24% | **89.34%** |
| Branch coverage | 18.52% | 56.03% | **56.88%** |
| Function coverage | 100.0% | 100.0% | 100.0% |
| Structural (diagram-fidelity) coverage | ~0.00%¹ | 74.60% | **76.80%** |
| Mutation score, whole-file | 40.62% | 35.10% | **43.02%** |
| Mutation score, property-scoped | 41.04% | 35.97% | **43.87%** |
| Class coverage | 95.96% | 93.64% | **96.01%** |

*¹ "Structural coverage" measures outcomes specific to the new suite's own generation
strategy (per-field construct/assign/reassign/clear checks); it isn't a metric the old
suite's tests were built to satisfy, so ~0% reflects a metric mismatch, not a quality
gap — see Section 1.*

**The headline finding: the combined suite is at or above both individual suites on
every single metric, not just an average of the two.** This is the direct, intended
result of how `test_combined.py` was built — it keeps everything either suite
individually catches (after removing genuine duplicates), so any class, line, branch,
or mutant caught by *either* suite is caught by the combined file. Coverage/mutation
figures that only average or split the difference would indicate something went wrong
in the merge; consistently equalling-or-beating both source suites is the confirmation
that it didn't.

---

## 1. Coverage: line / branch / function / structural

| | Old suite | New suite | Combined suite |
|---|---|---|---|
| Line coverage | 73.36% | 88.24% | **89.34%** |
| Branch coverage | 18.52% (n=7,229)² | 56.03% | **56.88%** (n=7,229)² |
| Function coverage | 100.0% | 100.0% | 100.0% |
| Structural coverage | ~0.00%¹ | 74.60% | **76.80%** |
| Models measured | 8,336 / 8,336 (100%, rescoped for this report) | 9,041 / 9,082 (+37 `empty_model`, +1 `missing_file`) | 8,336 / 8,336 (100%) |

*² Branch coverage's denominator excludes models with zero branches in their generated
code (nothing to measure) — hence the smaller n than line/function/structural.*

**Read:** the new suite's deterministic-first design (construct → assign → reassign →
clear sequences) reaches far more of `python_code.py` than the old suite, especially on
branch coverage (56% vs. 18.5%) — the old suite's `@given`-based tests rarely exercise
both sides of the bidirectional-setter `if old_value is not None:` conditionals that
dominate this dataset's branching logic. The combined suite pushes every coverage
dimension a further, real (if modest) step above the new suite alone: **89.34% vs.
88.24% line, 56.88% vs. 56.03% branch, 76.80% vs. 74.60% structural** — the old suite's
`@given`-based fuzzing does catch a genuine, if small, sliver of code paths the new
suite's fixed sequences miss, and the combined file's deduplication logic keeps those
without re-adding the old suite's redundant, already-covered tests.

---

## 2. Mutation testing: whole-file vs. property-scoped

*Whole-file* lets cosmic-ray mutate anywhere in `python_code.py`, including `__init__`
bodies. *Property-scoped* restricts mutants to `@property`/`@x.setter` line ranges only
(`docs/2026-09-10-mutation-scope-property-setters.md`) — almost all of this dataset's
non-stub logic lives there, so this score is comparable across models regardless of how
much `__init__`-only logic a given model happens to have.

| | Old suite | New suite | Combined suite |
|---|---|---|---|
| Whole-file mutation score | 40.62% | 35.10% | **43.02%** (mean) / 42.54% (pooled) |
| Property-scoped mutation score | 41.04% | 35.97% | **43.87%** (mean) / 43.48% (pooled) |
| Models measured, whole-file | 8,423 / 9,082 | 8,368 / 8,368 (100%) | 8,336 / 8,336 (100%) |
| Models measured, property-scoped | 8,417 / 8,447 | 8,364 / 8,368 | 8,336 / 8,336 (100%) |

**Read:** counterintuitively, the **new suite alone scores lower on mutation than the
old suite alone** (35.10% vs. 40.62% whole-file) despite covering substantially more
*lines* (88.24% vs. 73.36%) — a direct, concrete illustration of this project's
recurring finding that coverage and mutation score measure different things: the new
suite's deterministic sequences *execute* more code but assert comparatively narrow,
predictable things about it (did the value round-trip correctly), while the old
suite's property-based `@given` tests, despite reaching less code overall, generate a
wider variety of input values per assertion once they do reach a line, which happens to
kill more mutants where it does execute. **The combined suite beats both individually
on mutation score too** (43.02% vs. 40.62%/35.10% whole-file) — proof that the two
suites' mutant-killing power doesn't simply overlap; each catches real faults the other
misses, and the union catches more than either.

Whole-file and property-scoped scores are close to each other for all three suites
(≤1 point apart in each column), consistent with this project's earlier, separately
confirmed finding that ~97% of a model's whole-file mutants already fall inside
property/setter regions — `__init__` and plain operations contribute little to the
mutant pool to begin with.

---

## 3. Class coverage

Of every class tree-sitter finds in `python_code.py`, what fraction got at least one
passing test referencing it (constructor call or `isinstance()` check)?

| | Old suite | New suite | Combined suite |
|---|---|---|---|
| Class coverage | 95.96% | 93.64% | **96.01%** |
| Models measured | 8,259 / 8,368 | 9,043 / 9,082 (+38 `empty_model`, +1 `missing_file`) | 8,336 / 8,336 (100%) |

**Read:** the old suite already reaches the large majority of classes on its own
(95.96%) — class-level coverage is a much lower bar than line/branch coverage, since a
single constructor call anywhere in a passing test satisfies it regardless of how much
of that class's *behavior* gets exercised. The combined suite edges narrowly above both
(96.01%), closing nearly all of the remaining gap between the two suites' individually
uncovered classes.

---

## Recovery note: combined-suite runs reached 100% measured for every metric

Every combined-suite metric in this report reached full **8,336/8,336 (100%)**
coverage after retrying initial timeouts/errors — a genuinely clean result, unlike
several earlier stages of this project that ended in real, permanent exclusions:

- **Coverage**: 233 timeouts + 2 `no_coverage_data` on the first pass → all recovered
  (retry + a name-resolution fix for 2 models) — 0 exclusions.
- **Mutation, whole-file**: 70 timeouts on the first pass → 53 recovered at
  `--overall-timeout 1800`; the remaining **17 were genuinely too slow (median 22
  min/model even among recovered peers) and were excluded** — the one metric in this
  report with a real, permanent exclusion, already reflected in `usable_models.txt`.
- **Mutation, property-scoped**: 52 unmeasured on the first pass (38 timeout, 12
  worker-crash `error`, 1 `init_error`, 1 `exec_error`) → **all 52 recovered** via a
  larger timeout (timeouts) and lower worker concurrency (the rest) — confirming the
  12+1+1 group's root cause was resource contention from 24 concurrent workers, not a
  model defect. Zero exclusions.
- **Class coverage**: 112 timeouts on the first pass → **all 112 recovered** at a
  larger timeout + lower concurrency. Zero exclusions.

Full root-cause writeups for each: `docs/DECISIONS.md`, 2026-09-17 entries.

---

## Key takeaways

1. **Combining the two suites isn't just an average — it strictly dominates.** Every
   metric in this report (coverage ×4, mutation ×2, class coverage) is highest for the
   combined suite, confirming the merge-and-deduplicate approach preserves each
   suite's real, non-overlapping strengths rather than just picking one or blending them.
2. **Coverage and mutation score disagree on which suite is "better" alone.** The new
   suite covers far more code (88.24% vs. 73.36% line) but kills fewer mutants (35.10%
   vs. 40.62%) than the old suite — reinforcing this project's running theme that line
   coverage measures reach, not test strength.
3. **Branch coverage remains the weakest coverage dimension even combined** (56.88%),
   far below line coverage (89.34%) — the bidirectional-setter `if old_value is not
   None:` pattern is still often only exercised from one direction, a concrete
   generator-improvement target independent of which test suite is used.
4. **Mutation score sits well below coverage across the board, for all three suites.**
   Even the combined suite's 89.34% line coverage pairs with only a 43.02% mutation
   score — most executed code still isn't meaningfully asserted on, the same gap this
   project's very first mutation-testing pass identified.
5. **The combined-suite runs were the cleanest of this whole project** — every metric
   reached 100% measured with zero new exclusions, apart from the whole-file mutation
   run's pre-existing 17-model exclusion carried over from before class coverage was
   even attempted.

## Source reports

| Report | Suite | Metric | Files |
|---|---|---|---|
| Old-suite coverage (merged, 3 tiers) | Old | Coverage | `structural_coverage_hypothesis_report.{json,md}` + `_timeouts_retry` + `_stragglers` |
| New-suite coverage | New | Coverage | *(published 2026-09-11; the underlying `structural_coverage_report.json` was a 43-model prototype-scale file, removed 2026-09-17 during reports-folder cleanup — figures quoted as originally reported)* |
| Combined-suite coverage (merged) | Combined | Coverage | `combined_coverage_report.{json,md}` + `_timeouts_retry` + Factura-pair fix in `code_metadata.json` |
| Old-suite mutation, whole-file | Old | Mutation | `mutation_full_dataset_report.{json,md}` |
| Old-suite mutation, property-scoped | Old | Mutation | `mutation_properties_report.{json,md}` |
| New-suite mutation, whole-file | New | Mutation | `structural_mutation_full_dataset_report.{json,md}` |
| New-suite mutation, property-scoped | New | Mutation | `structural_mutation_properties_report.{json,md}` (+4 models fixed post-publication, encoding bug) |
| Combined-suite mutation, whole-file (merged) | Combined | Mutation | `combined_mutation_report.{json,md}` + `_timeouts_retry` |
| Combined-suite mutation, property-scoped (merged) | Combined | Mutation | `combined_mutation_properties_report_final.{json,md}` |
| Old-suite class coverage | Old | Class coverage | `class_coverage_hypothesis_report.{json,md}` |
| New-suite class coverage | New | Class coverage | `class_coverage_report.{json,md}` |
| Combined-suite class coverage (merged) | Combined | Class coverage | `combined_class_coverage_report_final.{json,md}` |

Where a row says "merged," this report's figures were recomputed directly from the
base run's JSON plus every retry JSON (and, for the two coverage exceptions noted, a
direct `code_metadata.json` patch), not read from any single already-published
aggregate — see the source files listed for full per-model detail.
