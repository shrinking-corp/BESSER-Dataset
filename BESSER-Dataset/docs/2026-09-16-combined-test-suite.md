<!--
  AI-GENERATED DOCUMENT
  Generated/modified by: Claude Code (VS Code extension)
  Model used:            Claude Sonnet 5 (claude-sonnet-5)
  Generated at:          2026-09-17
-->

> **AI marking** — This document was generated/modified by **Claude Code (VS Code extension)**,
> using **Claude Sonnet 5** (`claude-sonnet-5`), generated at **2026-09-17**.
> Interpretation is AI-authored and has not been independently reviewed.

# The combined test suite: `test_combined.py`

**Status:** generated dataset-wide (8,368/8,368); coverage and whole-file
mutation measured, property-scoped mutation and class coverage pending as of
this writing.
**Related:** [`DECISIONS.md`](DECISIONS.md) — same-day entries;
[`2026-09-10-structural-test-generation.md`](2026-09-10-structural-test-generation.md)
for `test_structural_full.py`'s own design.

---

## What "combined" means, and what it deliberately isn't

The goal is a single, real `test_combined.py` file per model containing
both `test_hypothesis.py`'s (the dataset's original suite) and
`test_structural_full.py`'s (this session's suite) tests — **not** two
files handed to one `pytest` invocation. The distinction matters for
reproducibility and for the tooling: a real merged file is something every
downstream script (coverage, mutation, class coverage) can point at with
the exact same `--test-file` mechanism already built for the other two
suites, with no special-casing anywhere.

`scripts/generate_combined_tests.py` builds it by literal text
concatenation of the two files' source, run through two safety passes
first (below), plus a name-collision pass.

## Bug 1: module-level variable name collisions (safe, verified, not fixed)

Both generators independently define same-named module-level variables for
some classes — confirmed on `model_1`: both define `{ClassName}_strategy`
Hypothesis strategy variables and a `safe_text` helper, under the identical
name. This does **not** need fixing: Python executes module-level code
top-to-bottom, and neither file's lines are ever interleaved with the
other's (one file's content is placed fully before the other's), so each
file's own `@given(instance=X_strategy)` decorator always captures that
same file's own assignment, made immediately above it — the other file's
later reassignment of the same name only affects that other file's own,
later decorators. Verified empirically on `model_1`: running the combined
file gives exactly 32 (old) + 17 (new) = 49 passed, matching a clean sum.

## Bug 2: test function name collisions (fixed)

A genuinely different, worse problem: if both files define `def test_X(...)`
with the *identical* name, Python just rebinds `test_X` to whichever
definition executes second — no error, and pytest (which collects test
items by introspecting the already-executed module's namespace) only ever
sees the survivor. The other generator's test for that class is silently
and permanently dropped, not merely shadowed for part of the file.

Confirmed via a full-dataset AST scan (comparing top-level test-function
names between the real files directly, not inferred from one sample):
**439/9,017 models (4.9%) have at least one genuine collision**, always the
pattern `test_{ClassName}_instantiation` — both generators independently
produce this exact name for at least some classes, with no
generator-specific suffix.

**Fix**, `disambiguate_test_names()`: every top-level `test_*` function in
the OLD suite is renamed with a `test_hyp_` infix (`test_X` →
`test_hyp_X`) before concatenation — AST-located by exact line number, then
a line-anchored text substitution, not a blind find/replace, so a name that
happens to also appear in a string or comment elsewhere is never touched.
Keeps pytest's `test_*` discovery working, and guarantees the full name can
never collide with anything `test_structural_full.py` generates —
structurally, not just for the 439 currently-observed cases. Re-verified on
`model_10000019` (a real colliding model): 88 (old) + 35 (new) = 123 tests,
combined file collects exactly 123.

## Bug 3: semantic duplication (the actual point of "combined") — fixed

Avoiding name collisions isn't the same as avoiding testing the same thing
twice under two different names — the user's explicit ask once the first
two fixes landed: *"if both files test the same thing, we should keep only
one test."* Two deterministic, AST-structural rules in
`find_redundant_old_tests()` — matched by test-body *shape*, never by test
name, so the rules hold regardless of the two generators' different naming
conventions (old suite lowercases every name; new suite preserves case):

1. **Exact duplicate.** A test whose entire body is exactly
   `assert isinstance(<param>, ClassName)`. Both generators independently
   produce this per class — confirmed: old suite's
   `test_petrinet_token_instantiation` and new suite's
   `test_petrinet_Token_instantiation` are structurally identical, just
   differently cased, which is *why this never showed up in the Bug 2 name
   collision scan* — casing hides it as a string collision, but it's the
   exact same check for the exact same class, happening for essentially
   every class in every model. If both suites have one for a class, the OLD
   suite's copy is dropped.
2. **Subsumption.** OLD suite's `assert hasattr(ClassName, "attr")`
   existence-check (confirmed shape: `test_petrinet_node_has_name` — checks
   `hasattr` then walks the MRO to confirm the descriptor is a `property`)
   is dropped when the NEW suite has a `_value_roundtrip` test for the same
   (class, attribute) — since round-tripping an actual value strictly
   proves more than checking a descriptor merely exists.

No other test type is touched — OLD suite's `_is_not_abstract`/
`_constructor_exists`/`_constructor_args` and NEW suite's `_isa_`/
`_assoc_..._link_reassign_clear` have no counterpart in the other file.

**Verified on both smoke models:**
- `model_1`: 32 + 17 − 9 (removed) = 40; pytest collects and passes exactly 40.
- `model_10000019`: 88 + 35 − 27 = 96, matches exactly; `test_secret_instantiation`
  now appears exactly once (the old suite's redundant copy removed before
  the rename step even needed to run for it).

**Full-dataset generation: 8,368/8,368, zero errors.** Dedup removed
**360,308** redundant old-suite tests across 8,367/8,368 models — averaging
~43 per model, confirming this class of duplication is pervasive across
the whole dataset, not an edge case.

## Combined-suite measurement results and timeout handling

### Coverage (`combined_coverage_validation`)

First pass on `usable_models.txt` (8,368): 8,133 measured, 233 timeout, 2
`no_coverage_data`.

**The 2 `no_coverage_data` were a real, separate bug**, not new: models
`model_10001897`/`model_10001985` (the "Factura" pair from the original
BUML→PUML conversion fix batch — see
[`2026-09-10-buml-to-puml-conversion.md`](2026-09-10-buml-to-puml-conversion.md)).
Their on-disk `test_structural_full.py` was generated by an earlier version
of `generate_structural_tests.py`, before `resolve_code_name()` existed —
the actual generated class is `Facturas` (the code generator pluralizes
it), not `Factura` as BUML declares. Confirmed by regenerating with the
current script: it correctly resolves `Facturas` now. Fixed by regenerating
`test_structural_full.py` → `test_combined.py` → re-measuring for both
models; both now `measured`.

**The 233 timeouts were escalated the same way as `old_suite_unmeasurable`**
(180s, 8 workers): 218 recovered, 15 still timing out. Spot-checked
`model_100203` (1,080 tests) standalone: finishes in 88.81s with ~0% CPU
load — same unseeded-Hypothesis-search-variance class as before, not a new
bug. Only 4/15 overlap with the already-known old-suite stragglers, so
mostly a distinct (if same-cause) set — the combined file is simply
bigger/slower than either suite alone, pushing some borderline models over
the batch-run timeout that weren't affected running each suite separately.
**Decision: exclude these 15 too**, under a new `combined_suite_unmeasurable`
reason. Master exclusion list: **729** models (was 714).
`reports/usable_models.txt`: **8,353** (was 8,368).

### Mutation, whole-file (`combined_mutation_validation`)

Run on the updated 8,353-model `usable_models.txt`: 8,283 measured, **70
timeout** — at cosmic-ray's default 900s overall-timeout per model.

**Different, more tractable root cause than the coverage timeouts.**
Mutation testing reruns the *entire* suite once per mutant (up to 40,
capped); a *surviving* mutant runs to completion every time (only killed
mutants benefit from `-x` fail-fast). Spot-checked `model_10000802`: 446
tests, 29.34s baseline. At the combined suite's ~43% average kill rate,
roughly 57% of 40 mutants each run the full 29.34s (≈670s) plus the killed
~43% at a shorter fail-fast time (≈250s) — landing right around the 900s
ceiling. That ceiling was sized for smaller, single-suite runs; the
combined suite's baseline runtime is naturally larger (roughly the sum of
both suites, minus dedup), so the same fixed timeout is now exceeded by a
meaningfully larger fraction of models. Consistent with the comparison:
old suite alone had 27 such timeouts, new suite alone had **zero**,
combined has 70 — and only 2/70 overlap with the old-suite stragglers, 0/70
with the coverage-timeout exclusions — a new, distinct group.

**Why this isn't being treated as unfixable like the coverage timeouts**:
the coverage timeouts were genuine unpredictable variance (the identical
file finished in wildly different times across repeated runs) where more
time wasn't reliably going to help. Here the cost is fairly predictable
(~N × baseline runtime), so proportionally more headroom should resolve
most of them.

**Retried at `--overall-timeout 1800` (double default): 53/70 recovered, 17
still timing out.** Confirms the diagnosis: among the 53 that completed,
p90/p99 duration was already 1,823-1,839s — right at the new ceiling,
median 1,331.78s (22 min/model). These 17 are the most extreme tail of the
dataset; recoverable with a much larger timeout (~1hr+ per model) but not
worth that cost for 17/8,353 models. **Excluded** under
`combined_suite_unmeasurable` rather than retried further — bringing that
reason's total to 32 (15 coverage + 17 mutation). Master exclusion list:
**746** models. `reports/usable_models.txt`: **8,336**.

## Reproduction

```bash
python scripts/generate_combined_tests.py --models-file reports/usable_models.txt --workers 24
python scripts/validate_coverage_structural.py --models-file reports/usable_models.txt --test-file test_combined.py --report-name combined_coverage_report --workers 24 --write-metadata
python scripts/validate_mutation.py --models-file reports/usable_models.txt --test-file test_combined.py --report-name combined_mutation_report --workers 24 --write-metadata
```
