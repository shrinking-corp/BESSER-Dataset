# Decisions & findings log — coverage / mutation testing evaluation

Running log of non-trivial findings and decisions made while evaluating test
coverage and mutation testing for the dataset (see `PROMPT.md`). Newest
entries at the top. Each entry should stand alone enough to explain *why* a
decision was made, so we can backtrack later without re-deriving it.

Entries below from 2026-09-10 onward were written from a second, parallel
Claude Code session (Windows, Claude Sonnet 5) working the same repo
alongside the session that produced the entries below them — expect some
independent convergence on the same underlying script names
(`validate_mutation.py` in particular has fixes from both sessions, for
different, non-overlapping reasons).

---

## 2026-09-29 — Phase 4 sample methodology: stratify by has_logic count, not difficulty_score; equal allocation, size 200

**Superseded decision:** the original Phase 4 plan (checklist.md, first
written 2026-09-28) said the shared Track A/B sample should be "stratified
by `difficulty_score`." Discussed with the user and changed this after
`classify_method_logic.py`'s results made a concrete problem visible:
`difficulty_score` and `has_logic` method count don't always move together.
`model_2023` (the 932-class metamodel used elsewhere as a difficulty-score
example) scores **86.66/100** on `difficulty_score` — one of the hardest
models in the dataset — but has **zero methods at all** (`methods = 0` in
its raw structural fields). It would be a completely useless Phase 4 sample
member despite looking "hard" by the old criterion, because
`difficulty_score` measures overall structural size/style, not "how much
logic exists to break."

**New methodology, decided with the user 2026-09-29:**
- **Stratify by `has_logic` method count** (the same buckets
  `classify_method_logic.py` already reports: 1-5/6-10/11-20/21-50/51-100/
  101-200/200+), since that's what Track A/B actually operate on.
- **Sample size: ~200** — a middle ground between statistical robustness and
  compute/effort cost for both cosmic-ray mutation testing (us) and the
  colleague's manual LLM-loop iterations.
- **Equal allocation across buckets, not proportional to the dataset's real
  shape.** The user's stated purpose is "to determine which method of
  generating tests [to] choose" — a methods comparison, not a description of
  the dataset. Proportional sampling would starve the rare, most-interesting
  high-`has_logic` buckets (51-100/101-200/200+ are only 9.4% of the
  eligible pool combined) of representation exactly where seeing how each
  method scales to complex logic matters most. Split: 1-5→29, 6-10→29,
  11-20→29, 21-50→29, 51-100→28, 101-200→28, 200+→28 (sums to 200).
- **De-duplicate before sampling.** Several models share identical
  `no_logic`/`trivial`/`has_logic`/`total_methods` counts (first noticed in
  the top-50-by-has_logic ranking, e.g. `model_455`/`model_456` both
  370/961) — a strong signal of near-identical generated content under
  different model names. Only one representative per duplicate signature is
  kept in the eligible pool, so the 200-model sample can't secretly contain
  the same code twice.

Built `scripts/select_test_generation_sample.py` implementing this exactly. Verified
against two synthetic fake classification reports (never the real dataset):
3 planted exact-duplicate pairs were correctly detected and dropped, and
bucketing/target-splitting/seeded-sampling produced the exact requested
count with zero duplicates leaking through; a separate test with an
artificially starved bucket correctly fell back to "take everything
available" and reported the shortfall rather than silently under-delivering.
Not yet run against the real dataset (still the user's to run, per standing
process):
```
.venv\Scripts\python.exe scripts\select_test_generation_sample.py --sample-size 200 --seed 42
```

---

## 2026-09-29 — Phase 4 Step 1: per-method logic classification (`classify_method_logic.py`), and the surviving-mutant export prerequisite

**Why:** Phase 4 (raising mutation score, see `checklist.md`) needs to target
test generation at methods that actually *have* logic to break — generating
more tests for a plain getter/setter can't raise mutation score, since there's
nothing value-dependent in it to get wrong. `validate_logic.py` (2026-09-10)
already flags whole *models* with zero logic (`no_logic`, 631 models, every
class a bare `pass`), but that's model-granularity — most usable models are a
mix of stub/trivial/real methods, and Phase 1's whole-file mutation testing
already showed 65%+ mutation scores are achievable, so most of this dataset's
methods must be too simple to fail, not genuinely untested.

**Classification, built in `scripts/classify_method_logic.py`** (AST-only,
same pattern as `validate_logic.py` — parses `python_code.py` once per model,
no execution). Every method in every class gets exactly one label:

1. **`no_logic`** — stub body (`pass`/`...`/docstring only). Reuses
   `validate_logic.py`'s own stub-detection helper, generalized from
   whole-class to per-method.
2. **`trivial`** — at most 4 statements, no loop/`try`/`match`/comprehension/
   `lambda`, no arithmetic (`BinOp`) or boolean (`BoolOp`) computation
   anywhere in the body, and at most one non-`elif` `if` guard. This
   deliberately covers more than plain getters/setters: the dataset's
   near-universal bidirectional-association setter pattern
   (`if self._x is not None: self._x._y.remove(self)` / `self._x = value` /
   `if value is not None: value._y.append(self)`) is still just "set a field
   and keep both sides in sync" — no computed decision, nothing a varied
   input could route down a qualitatively different path — so it's `trivial`
   despite having two `if`s and three statements.
3. **`has_logic`** — everything else: a loop, an `elif`/nested-`else`
   branch, a `try`, a `match`, a comprehension, or arithmetic/boolean
   computation. These are the methods Track A (library-generated tests) and
   Track B (the colleague's LLM track) should actually target.

**Statement counting descends into a single guard's branches** (a 3-line
guarded setter counts as 3 statements, not 1), so the `≤4 statements` rule
doesn't accidentally let a bigger, disguised-as-one-statement block through.
Nested function/class definitions are judged as their own separate methods,
not folded into the parent's complexity count.

**Verified on a synthetic smoke test before handing off** (per the standing
rule: project scripts are never run against the real dataset by the
assistant, only compiled/unit-tested against hand-written code):
`__init__` field assignment and a plain getter → `trivial`; the guarded
bidirectional-association setter → `trivial`; a method with a `for` loop and
arithmetic → `has_logic`; a 3-way `if/elif/else` → `has_logic`; a `pass`
stub → `no_logic`. All five matched the intended rule.

**Run against `usable_models.txt` (8,336 models), `--write-metadata` on.**
Full breakdown (`reports/method_logic_classification_report.{json,md}`),
640,217 methods classified across the dataset:

| Category | Methods | Share of methods | Models with ≥1 such method | Share of models |
|---|---:|---:|---:|---:|
| no_logic | 14,256 | 2.23% | 947 | 11.36% |
| trivial | 461,776 | 72.13% | 8,336 | 100.00% |
| has_logic | 164,185 | 25.65% | 7,344 | 88.10% |

The model-level columns tell a different story than the method-level ones:
**every single measured model (100%) has at least one `trivial` method** —
plain field assignment/getters/setters are universal, not a quirk of some
models — while only **11.36%** of models contain even one fully-empty
`no_logic` stub method (most models' methods all do at least *something*,
even if trivial). **88.10%** of models have at least one `has_logic` method,
which is the Phase 4 sample-eligibility number; the remaining 11.9% (992
models, see below) have none at all.

**This quantifies the mutation-score root cause directly, for the first
time.** Earlier sessions diagnosed *why* mutation score is low (isinstance-
only instantiation tests, fixed/non-varied setter values — see the
2026-09-17/18 discussion below) by reading example test code; this is the
first dataset-wide count of *how much of the code could ever fail a
mutation regardless of test quality*. Only 1 in 4 methods (25.65%) has any
branching, loop, or computed value at all — the remaining 74.35% is
structurally inert (empty stub or plain field assignment/getter/setter), so
no amount of test-writing effort against those methods could move mutation
score. This reframes the mutation-score ceiling: it isn't only a test-
quality problem, it's also that only a quarter of the code is the kind of
code mutation testing can meaningfully discriminate on.

**Per-model spread, from `has_logic_count_distribution` /
`total_methods_distribution` in the report:**

| has_logic methods/model | Models | Share |
|---|---:|---:|
| 0 | 992 | 11.90% |
| 1-5 | 1,629 | 19.54% |
| 6-10 | 1,691 | 20.29% |
| 11-20 | 1,649 | 19.78% |
| 21-50 | 1,686 | 20.23% |
| 51-100 | 483 | 5.79% |
| 101-200 | 158 | 1.90% |
| 200+ | 48 | 0.58% |

Mean 19.70 `has_logic` methods/model, **median only 10** — the distribution
has a long but thin tail (just 2.48% of models clear 100 `has_logic`
methods). **7,344/8,336 models (88.1%)** have at least one `has_logic`
method and are eligible for Phase 4's sample; the **992 (11.9%)** with zero
are consistently small models in their own right (avg 13.85 total methods,
median 6, max 162 — never a large model that just happens to lack complex
logic), so excluding them from the sample loses no large/complex model.

**Side-observation, not pursued further here:** several models in the
top-50-by-`has_logic` ranking form exact-duplicate pairs or triples with
identical has_logic/total-method counts — `model_455`/`model_456` (370/961
each), `model_5149`/`model_5150` (362/1104 each), `model_450`/`model_451`/
`model_10041` (351/884 each), `model_5058`/`model_5059`/`model_5060`
(330/886 each), among others. Consistent with this dataset containing
near-identical generated variants (already known from earlier duplicate-
model observations this session); worth keeping in mind when drawing the
Phase 4 sample so it isn't accidentally padded with near-duplicate twins.

**Shared prerequisite also built: exporting *which* mutants survived, not
just the count.** `validate_mutation.py`/`validate_mutation_properties.py`
only ever read `stats["outcomes"].get("SURVIVED", 0)` — a bare number — from
cosmic-ray's session sqlite db, and that db lives in a scratch copy deleted
right after each model finishes (by design, for dataset safety — see that
script's own docstring). Track B (the colleague's LLM mutation-feedback loop)
needs the actual surviving mutants to show the LLM, not just a count.

Added `scripts/mutation_export.py` (`export_surviving_mutants()`), joining
cosmic-ray's own `mutation_specs` and `work_results` tables
(`cosmic_ray/work_db.py`'s real schema, confirmed by reading the installed
package directly rather than guessing) on `test_outcome = 'SURVIVED'`, and
writing `<dir>/<model>.json` per model with each survivor's module, line
range, operator name+args, `definition_name`, and cosmic-ray's own unified
diff for that specific mutant — everything needed to show a specific broken
test case to an LLM. Wired into both validators as a new, **opt-in**
`--export-surviving-mutants DIR` flag (default off), so every already-
completed full-dataset mutation run stays byte-for-byte unaffected; it only
activates when explicitly passed for the Phase 4 sample run. Verified against
a synthetic sqlite db built to mirror cosmic-ray's real table schema exactly:
correctly exported the one `SURVIVED` row with its full diff, correctly
skipped the `KILLED` row.

---

## 2026-09-28 — Checked: is mutation score inflated by empty/trivial models? Nuanced answer, not a simple yes

**Question raised:** given mutation score is `killed/run`, does the dataset's
~40% average get artificially propped up by empty or near-empty models,
where a handful of trivial mutants get killed easily?

**No inflation from fully-empty models — they're already excluded.**
Cross-referenced `reports/logic_validation_report.json`'s 631 `no_logic`
models (every class is `class X: pass`, confirmed by static AST analysis
back on 2026-09-10) against `reports/usable_models.txt` and
`reports/combined_mutation_properties_report_final.json`: **0/631** appear
in either. They never receive a mutation score at all, so the literal
"empty model scores 100%" concern doesn't occur in this pipeline.

**A real, modest effect among small-but-not-empty models.** Bucketing the
8,336 scored models by how many mutants actually ran (`mutants_run`, capped
at 40):

| mutants_run | n | avg score |
|---|---|---|
| 1-5 | 540 | 50.5% |
| 6-20 | 586 | 45.2% |
| 21-50 (most models, near the cap) | 7,210 | 43.3% |

The smallest ~6.5% of the dataset scores about 7 points higher on average —
real, but small, and confined to a small slice.

**The dominant "near-100%" cluster is NOT these simple models.** The
dataset's mutation score is bimodal (documented in `summary_report.md`);
checked the 906 models scoring exactly 1.0 directly: they ran an average of
**38.9/40** mutants (near the cap, i.e. not small) and have an average
`difficulty_score` of **46.6**, noticeably above a random sample's 32.2. So
the spike at 100% is driven by larger-than-average models whose tests
genuinely catch nearly everything, not by trivial models getting lucky.

**Conclusion:** the ~40% headline average is not inflated by empty models
(excluded) and only marginally affected by very-small ones (~6.5% of the
dataset, +7 points) — the low average is still best explained by the
weak-assertion pattern documented earlier (isinstance-only instantiation
tests, fixed/non-varied setter test values), not by a measurement artifact.
Plain-language writeup with examples:
[`2026-09-28-explainer-empty-models-mutation-score.md`](2026-09-28-explainer-empty-models-mutation-score.md).

## 2026-09-17 — Combined-suite class coverage: all 112 initially-unmeasured models recovered

**Finding:** `validate_class_coverage.py --test-file test_combined.py` (24
workers) left 112/8,336 models at `timeout` on the first pass
(`combined_class_coverage_report.{json,md}`: 8,224 `measured`, avg 96.04%).
Same underlying cause as everywhere else in this session: this script's
default `--timeout` is only 60s (sized for a single pytest run of the old
or new suite alone), and the combined suite's larger baseline runtime
pushes some models past that ceiling.

**Retried at `--timeout 180 --workers 8`** (matching the exact setting that
already worked for the earlier combined-suite *line* coverage run's first
retry tier, 233→218 recovered): **112/112 recovered**, avg class coverage
94.01% for that batch. No further retry tier was needed this time (unlike
line coverage's 15 genuine stragglers) — class coverage's pass/fail
condition (does any passing test reference the class at all) is cheaper to
resolve than the deeper line/branch instrumentation, so fewer models sit at
the genuinely-slow extreme.

**Merged final result** (base + retry,
`combined_class_coverage_report_final.{json,md}`): **8,336/8,336 measured
(100%)**, avg class coverage **96.01%**. Zero exclusions needed for this
metric.

## 2026-09-17 — Combined-suite property-scoped mutation: all 52 initially-unmeasured models recovered — root cause was worker concurrency, not the models

**Finding:** the first pass of `validate_mutation_properties.py --test-file
test_combined.py` (24 workers) left 52/8,336 models unmeasured: 38
`timeout`, 12 `error` (*"A process in the process pool was terminated
abruptly while the future was running or pending"*), 1 `init_error`
(`model_714`), 1 `exec_error` with no recovered score (`model_1955`).
Report: `combined_mutation_properties_report.{json,md}` (8,258 `measured`
outright, avg score 0.4382).

**The 38 timeouts are the same arithmetic-ceiling cause already documented**
for the whole-file mutation run below (combined suite's larger baseline
runtime × up to 40 capped mutants routinely approaches the 900s default
ceiling) — unsurprising here too, since this report's own stats show
property mutants are ~97.4% of a model's whole-file mutant count on
average, i.e. nearly the same cost as the whole-file run.

**The 12 `error` + 1 `init_error` + 1 `exec_error` were a different,
previously-unseen failure mode** — worker processes crashing mid-run rather
than timing out. Retried all three groups at lower concurrency:

| Retry batch | Models | Setting | Result |
|---|---|---|---|
| Timeouts | 38 | `--overall-timeout 1800` | 38/38 recovered, avg score 0.4789 |
| Worker-crash errors | 12 | `--workers 2` | 12/12 recovered, avg score 0.5604 |
| Singletons | 2 | `--workers 2` | 2/2 recovered |

**All three retry batches fully recovered — confirms the root cause was
resource contention from running 24 workers concurrently, not anything
wrong with the models themselves.** Unlike the whole-file mutation run
(which needed a genuine exclusion of 17 models even after retrying at
1800s), property-scoped mutation's smaller mutant cap meant every affected
model finished well within a doubled timeout or reduced concurrency.
**Zero exclusions needed for this metric.**

**Also noted, not investigated further:** 26 of the base run's 27
`exec_error`-labeled records actually had a valid `mutation_score` recovered
despite the status label (only 1, `model_1955`, genuinely lacked one) — a
harmless report-labeling inconsistency in `validate_mutation_properties.py`,
already correctly counted toward "measured successfully" in the base
report's own summary stat.

**Final merged result** (base + all three retries,
`combined_mutation_properties_report_final.{json,md}`): **8,336/8,336
measured (100%)**, average mutation score **0.4387** (mean of per-model
scores) / **0.4348** (pooled killed/run across the full sample).

## 2026-09-17 — Finding: the article formula produces meaningless scores for large models (confirmed, quantified, and sourced against the paper itself)

**The finding:** applying the reference paper's exact difficulty formula
(`D = 0.3571*C + 0.4082*R + 0.2347*A`, raw counts, no normalization -- per
the paper's own methodology, see the entry below) to a genuinely large model
does not just produce a "high" score -- it produces a score with no
interpretable relationship to the paper's own difficulty scale at all.

**Concrete case:** `model_2023` (`fumltracemmNEWFormat_BUML_model.py`, a real
fUML trace metamodel) has `classes=932`, `associations=836`, `composition=292`,
`generalizations=332` (`R = 836+292+332 = 1460`), `attributes=11`. Its
article score:

```
C contribution:  0.3571 * 932  =  332.86  (35.75% of total)
R contribution:  0.4082 * 1460 =  595.92  (63.99% of total)
A contribution:  0.2347 * 11   =    2.58  ( 0.28% of total)
D = 931.36
```

**Why this is "wrong," not just "high":** the paper's own Table 2 reports its
*hard*-difficulty tier average as `C=9.6, R=12.0, A=23.8` (its hardest
textbook exercises). Recomputing `D` for that average with the same
rescaled weights gives `D ≈ 13.9`. `model_2023`'s score of `931.36` is
**~67x** the paper's own definition of an average "hard" exercise -- not
because the model is 67x harder in any meaningful sense, but because `R` and
`C` are raw, unbounded counts and this model has orders of magnitude more
structure than anything the formula was ever calibrated against (the paper's
own dataset tops out at `C=13, R=16`; see the entry below). One relationship
count (`R=1460`) alone contributes more to the score than the paper's entire
average "hard" exercise scores in total.

**Root cause, already confirmed against the paper's text (entry below):**
the paper deliberately never normalizes `C`/`R`/`A` (*"We retain original
raw-data weighting without normalization... primitive numerical features
carry inherent domain semantics"*). That design choice is harmless -- even
reasonable -- for a hand-curated 30-exercise benchmark where every value is
small and roughly comparable in scale. It breaks down completely the moment
the formula is applied to a dataset (like this one) containing models whose
structure spans orders of magnitude, because nothing in the formula limits
how much a single outlier's raw counts can dominate the total.

**Contrast with the PCA score:** the same model scores `86.66` under the
PCA-based `difficulty_score` -- correctly placed near the top of a bounded
`[0, 100]` scale (it *is* one of the hardest models in the dataset), but not
at a value that's mathematically disconnected from every other model's
score the way `931.36` is. This is a direct, concrete illustration of why
`log1p` + standardization + percentile-clip rescaling (PCA score) is
necessary for a dataset at this scale, and why a formula validated on 30
small, uniform-scale exercises cannot be applied unmodified to a dataset
containing real, large-scale structural models without producing scores
that are technically "correct" (faithfully computed) but practically
meaningless for ranking/stratification purposes.

**Practical implication:** any use of `difficulty_score_article` for
stratification, sampling, or ranking across this full dataset should treat
it with this limitation in mind -- it remains useful for relative comparison
among similarly-scaled models, but a handful of large models will dominate
any aggregate statistic (mean, top-N selection, etc.) computed on the raw,
uncapped value. See `scripts/export_difficulty_scores_for_excel.py`'s
`difficulty_score_article_capped_100` column for a cap-based (not rescaled)
mitigation used for chart comparison purposes only.

## 2026-09-17 — Article-formula `difficulty_score_article` computed, and compared against the PCA score

**Formula** (`scripts/compute_article_difficulty_score.py`), reproducing the
reference paper's difficulty score with its FK term dropped (paper's own
weight for it was negligible: 0.02) and the remaining weights rescaled to
sum to 1: `D = 0.3571*C + 0.4082*R + 0.2347*A`, with `C=classes`,
`A=attributes`, and `R = associations + aggregation + composition +
generalizations` (every separate relationship type counted once each, now
that `associations` is mutually exclusive from aggregation/composition --
see the entry above; a paper-specified `dependency` term is omitted since no
`Dependency` class is used anywhere in this dataset's BUML models).
Applied directly to raw counts, no standardization/log-transform/rescaling
-- unlike the PCA score, `D` is intentionally left unbounded, to compare the
paper's formula's real behavior rather than two scores both artificially
squeezed into [0, 100]. Written into `difficulty_score_article` (+
`difficulty_score_article_c/r/a` for transparency) for all 9,082 measured
models. Observed range `[0.00, 931.36]`, mean `27.88`.

**Comparison** (`scripts/compare_difficulty_scores.py`, read-only):
Pearson (linear) correlation `+0.731`, Spearman (rank) correlation `+0.894`
across all 9,082 models -- the two approaches broadly agree on overall
ordering, with meaningfully more agreement on *rank* than on raw linear
value (expected: the article score's raw-count linearity makes it far more
sensitive to a handful of extreme outliers than the log1p+standardized PCA
score is). Top-10%-hardest overlap: 686/908 (75.6%) -- most, but not all, of
what one score calls "hardest" the other does too.

**Where they disagree most, and why (inspected concretely, not just from
the correlation number):**

- **`model_3616`** (`valueSets_BUML_model.py`): 0 classes, 0 attributes, 0
  associations/aggregation/composition/generalizations, but 344
  `enumerations` / 1,223 `enumeration_literals` -- a pure enumeration model.
  PCA score: `41.17` (75th percentile, correctly reflecting substantial
  structure). Article score: `0.00` (0.2nd percentile) -- `C`, `R`, and `A`
  are all zero, so the formula is **structurally blind to enumeration-only
  models**, however large. This is a real gap in the paper's formula for
  this dataset, not a quirk of one model: any model whose complexity lives
  entirely in enumerations scores exactly 0 under the article formula
  regardless of size.
- **`model_10002872`**: 41 classes, 18 associations, but 0 generalizations,
  0 many-valued association ends, `attribute_type_diversity=1` -- a wide,
  structurally flat/uniform model (many similar classes, little relational
  or type richness). Article score: `22.46` (75th percentile -- driven
  almost entirely by the raw class count, `0.3571*41 ≈ 14.6` of it). PCA
  score: `15.32` (9.5th percentile) -- log1p dampens the raw count and
  standardization weighs it against the model's near-total absence on every
  *other* dimension (no inheritance, no type diversity, no multiplicity
  richness), correctly ranking it as structurally simple despite the class
  count. This is the general shape of most of the large rank-disagreements
  observed: **the article formula's raw linear `C`/`R`/`A` cannot
  distinguish "many simple, uniform classes" from "many classes forming a
  genuinely rich structure"; the PCA score can, because it incorporates
  enumerations, methods, type diversity, and multiplicity alongside
  class/attribute/relationship counts, and dampens outlier magnitude via
  log1p instead of scoring it linearly.**

**Takeaway:** the two scores agree well overall (Spearman 0.894), which is
a useful sanity check that the PCA score isn't measuring something
unrelated to the paper's notion of difficulty. But the disagreements are not
noise -- they concentrate in exactly the two places the article formula is
structurally limited (blind to enumerations/methods/type-diversity/
multiplicity entirely; linear in raw counts rather than outlier-robust) and
the PCA score was built to address. Full report:
`reports/difficulty_score_comparison_report.json`.

## 2026-09-17 — PCA-based `difficulty_score` computed and written for all 9,082 models

**Context:** a reference paper scores model difficulty as
`D = w_c*C + w_r*R + w_a*A + w_fk*FK` (Class count, Relationship complexity,
Attribute count, Flesch-Kincaid readability of the requirement text), with
weights `(0.35, 0.4, 0.23, 0.02)`. Two parallel efforts were agreed: (1) our
own PCA-based score, built here, that lets the data itself decide which
structural fields matter and by how much, instead of hand-picking C/R/A/FK;
(2) the paper's exact formula, for a like-for-like comparison (FK dropped as
negligible per the paper's own weight, remaining weights rescaled to sum to
1: `0.3571/0.4082/0.2347` — not yet built, next task).

**Variables (11 of `model_metadata.json`'s 14 structural fields):** `classes`,
`attributes`, `associations`, `composition`, `generalizations`,
`abstract_classes`, `enumerations`, `enumeration_literals`, `methods`,
`many_valued_association_ends`, `attribute_type_diversity`. Excluded:
`association_classes`, `abstract_methods`, `aggregation` — confirmed true
constants (std=0 across all 9,082 models; `aggregation` in particular is
never used anywhere in this dataset), a hard requirement since standardizing
a true constant divides by zero. `inheritance_depth` was also considered,
checked for real variance first (`check_new_metrics_variance.py`), and
dropped as near-degenerate (4,700/9,082 at depth 0, 4,373 at depth 1, only 9
ever reaching depth 2 — effectively redundant with `generalizations`), a
choice rather than a mathematical necessity.

**Two new structural fields added to `generate_model_metadata.py` to feed
this** (verified for real variance before implementing, same discipline as
above): `many_valued_association_ends` (association ends whose multiplicity
max is `*`/unbounded/>1 — avg 9.0/model) and `attribute_type_diversity`
(count of distinct attribute types per model — avg 2.33/model). Same change
also redefined `associations`: was `len(binary_associations)` (an inclusive
superset that double-counted composition/aggregation associations), now
`len(binary_associations) - composition - aggregation` (mutually exclusive
from composition/aggregation) — see the entry directly below this one for
the full rationale; `reports/summary_report.md` and its "~45 relations"
prose were corrected to match (now "~35 relations", avg `associations` 9.56).

**Method** (implemented in `scripts/compute_difficulty_score.py`):
log1p-transform each raw count (dampens outlier influence, e.g. a few
"UML-describing-itself" meta-models with thousands of classes, without
percentile-clipping away the extremes at this stage) → standardize (z-score)
across the full measured dataset → PCA via `numpy.linalg.eigh` on the
correlation matrix (deterministic, no randomness anywhere in the pipeline).
PC1 (48.54% variance explained) is "how much structure overall" — every
loading is positive, so its sign is meaningful and it's used signed. PC2
(14.80%) is a real second axis, a *style contrast* between data-schema-heavy
models (high `attribute_type_diversity`/`attributes`) and hierarchy-heavy
ones (high `generalizations`/`abstract_classes`/`composition`), verified
empirically via `scripts/diagnose_pc2_extremes.py` to reflect real structural
difference rather than small models drifting there by default (both PC2
extremes score *above* the dataset's average PC1: 0.732 and 1.398 vs. an
overall mean of 0.000).

PC2 is folded into the score via **absolute value**, not signed — a hard
requirement, not a style choice: an eigenvector's sign is mathematically
arbitrary whenever its loadings don't all share one sign (PC2's do split,
unlike PC1's), so using signed PC2 (or any monotonic shift of it) would make
the score depend on an arbitrary internal sign-fixing convention with zero
connection to the actual models — only a symmetric function like `|x|` is
invariant to that arbitrary choice. PC1 and PC2 are combined with
**variance-proportional weights** (not an arbitrary 50/50 split): for a
0-100 scale, PC1 gets `100 * var(PC1)/(var(PC1)+var(PC2))` ≈ 76.6 points,
PC2 gets the rest ≈ 23.4, computed from the real eigenvalues each run, never
hardcoded. Each component is independently rescaled (1st/99th percentile
clip, then linear min-max) to its own point budget, and the two totals are
summed — bounded to [0, scale_max] by construction.

**Fields written** (full float precision, no rounding — deliberately, so
downstream stratification/sorting isn't quantized): `difficulty_score`
(the combined 0-100 score), `difficulty_score_pc1_points` /
`difficulty_score_pc2_points` (each component's own contribution, for
transparency), `difficulty_score_pc1_raw` / `difficulty_score_pc2_raw` (the
unbounded signed projections — sign kept even for PC2, as context for which
style a model leans toward, even though only `|PC2 raw|` feeds the score).

**PCA fit scope:** deliberately fit and scored on **all 9,082 measured
models**, not just `usable_models.txt`. Considered and rejected restricting
to usable models: exclusion from `usable_models.txt` is about whether the
*generated code/tests* could be validated (timeouts, unmeasurable mutation
runs, etc.), not about the *diagram's* structural complexity, and is very
plausibly correlated with size/complexity (large models are more prone to
mutation/coverage timeouts) — fitting only on usable models would have cut
off disproportionately many of the largest/most complex models, shrinking
the standardization basis and percentile-clip bounds and silently inflating
everyone else's relative score, while leaving excluded (often "hardest")
models with no score at all.

**Result:** written into `difficulty_score` (+4 supporting fields) for
9,082/9,082 measured models via
`python scripts/compute_difficulty_score.py`. Reference report with full
loadings/means/stds/variance-explained at
`reports/difficulty_score_report.json`, so the formula can be reproduced or
applied to a new model without recomputing PCA from scratch. Score range
observed: `[3.27, 93.55]` (scale 0-100).

**Open follow-up, noted for the article-formula build:** `R` (relationship
complexity) in the paper's formula must sum **all** separate relationship-type
counts now that `associations` is mutually exclusive —
`R = associations + aggregation + composition + generalizations` (+
`dependency`, confirmed always 0 in this dataset; no `Dependency` class is
used anywhere in the BUML models) — not just `associations + generalizations`,
which would silently drop every composition relationship.

**Confirmed against the actual paper (Cheng et al., "Large Language Models
for UML Class Diagram Modeling," *Appl. Sci.* 2026, 16, 6540,
`10.3390/app16136540`, Section 3.1.2 — PDF obtained and read directly, since
MDPI blocks automated fetches):**

- `R`'s definition matches exactly: *"Different relationship types contain
  dependency, association, aggregation, composition, and inheritance."*
- The paper's own text confirms there is **no normalization or capping**:
  *"We retain original raw-data weighting without normalization, as
  primitive numerical features carry inherent domain semantics for UML
  difficulty evaluation."* So `difficulty_score_article`'s unbounded,
  outlier-sensitive behavior (see the entry below) is not a bug in our
  reproduction — it is the paper's formula working exactly as designed.
- The paper's own benchmark is **30 hand-picked textbook exercises** (its
  Table 1), with class counts 4–13, relationship counts 3–16, and attribute
  counts 0–38 — none remotely close to this dataset's largest real models
  (e.g. `model_2023`, 932 classes, 836 associations, 292 composition, 332
  generalizations — an actual fUML trace metamodel). The formula was never
  exercised against anything at that scale in its own paper, so its lack of
  outlier protection was never a problem there; applying it unmodified to a
  9,082-model dataset that includes genuine large-scale specification
  models surfaces exactly the failure mode log1p + standardization was
  built to avoid in our PCA score.

## 2026-09-17 — `model_metadata.json`'s `associations` field redefined: was a superset including aggregation/composition, now mutually exclusive

**Context:** designing a difficulty score (a "relationship complexity"
dimension summing associations + generalizations, per a reference paper's
formula) surfaced that `generate_model_metadata.py`'s `associations` field
was every `BinaryAssociation` regardless of its `is_composite`/
`is_aggregation` flags — i.e. a superset that *already includes* whatever
gets separately counted in `aggregation`/`composition`. Summing
`associations + aggregation + composition` for a "total relationships"
figure would silently double-count every aggregation/composition edge.

**Decision: redefine `associations` in place** (not add a new field
alongside it) so the three fields partition the full `BinaryAssociation` set
with no overlap — `associations` is now the plain (neither-composite-nor-
aggregation) count. Chosen over adding a parallel field because the
inclusive definition being currently undocumented as such made it an
actively misleading number, not just an inconvenient one; a differently-named
field would coexist with, but not fix, that.

**Real consequence: this changes an already-published number.** The
colleague's `summary_report.md` cites "Associations: 19.94" under the old
(inclusive) definition. Since `aggregation` is confirmed 0 for every model
in the dataset (see below), linearity of expectation gives the new
dataset-wide average exactly: 19.94 − 10.38 (composition avg) − 0 = **9.56**
— stated here as an expected value, not yet written into that report, which
should be updated once the actual full-dataset regeneration (below) lands,
so the report always reflects real regenerated data rather than a
derived-in-advance number.

**Incidental confirmation while making this change**: `aggregation` is
exactly 0 for all 9,082 models — `is_aggregation` is apparently never set on
an end without `is_composite` also being set (composite takes priority in
the classification), so in practice this dataset only ever has plain
associations and compositions, never anything classified as aggregation
specifically.

**Verified** on `model_1` (known values: 7 total, 3 composition, 0
aggregation): regenerating with the fixed script gives
`associations: 4` (= 7 − 3 − 0), exactly as expected.

**Full-dataset regeneration needed** (`--fresh --write-metadata`, since
every model's `model_metadata.json` already has old-definition values
that the resumable cache would otherwise skip):
```
python scripts/generate_model_metadata.py --fresh --write-metadata --workers 24
```

## 2026-09-17 — Combined-suite whole-file mutation: 70 models hitting the 900s overall-timeout, arithmetic root cause

**Finding:** running `validate_mutation.py --test-file test_combined.py` on the
8,353-model `usable_models.txt` left 70 models at `timeout` (cosmic-ray's
default 900s overall-timeout per model), vs. 27 for the old suite alone and
**zero** for the new suite alone. Only 2/70 overlap with the already-known
old-suite stragglers and 0/70 with the coverage-timeout exclusions — a new,
distinct group.

**Root cause is arithmetic, not variance** (a genuinely different situation
from the coverage timeouts below): mutation testing reruns the whole suite
once per mutant (up to 40, capped), and a *surviving* mutant always runs to
completion (only killed ones benefit from `-x` fail-fast). Spot-checked
`model_10000802`: 446 tests, 29.34s baseline. At the combined suite's ~43%
average kill rate, ~57% of 40 mutants each running the full 29.34s (≈670s)
plus the killed ~43% at a shorter fail-fast time (≈250s) lands right around
the 900s ceiling — a ceiling sized for smaller, single-suite runs, now
undersized because the combined suite's baseline runtime is naturally
larger. Since the cost is fairly predictable (~N × baseline), unlike the
coverage timeouts' genuine run-to-run variance, more time should reliably
help here rather than just delaying the same outcome.

**Retried at `--overall-timeout 1800` (double default): 53/70 recovered, 17
still timing out.** Confirms the arithmetic diagnosis: among the 53 that
completed, p90/p99 duration was already 1,823-1,839s — right at the new
ceiling, median 1,331.78s (22 minutes/model). These 17 are the most extreme
tail; recoverable with a much larger timeout (~1hr+ per model) but not
worth the cost for 17/8,353 models. **Decision: exclude these 17** under
`combined_suite_unmeasurable` (now 32 total with the 15 coverage timeouts
from the entry below) rather than retry further. Master exclusion list:
**746** models (was 729). `reports/usable_models.txt`: **8,336** (was
8,353). Full writeup in
[`2026-09-16-combined-test-suite.md`](2026-09-16-combined-test-suite.md) and
the at-a-glance table in
[`2026-09-10-master-exclusion-list.md`](2026-09-10-master-exclusion-list.md).

## 2026-09-16 — Combined test suite: `test_combined.py`, deterministic deduplication, and combined-suite results

Built `scripts/generate_combined_tests.py` — a real, merged `test_combined.py`
per model (literal concatenation, not two files fed to one pytest
invocation, per explicit request). Three issues found and handled, in order
of how well-hidden each one was:
1. Module-level variable name collisions (both generators define
   `{ClassName}_strategy`/`safe_text` under identical names) — verified
   harmless given Python's top-to-bottom execution order; no fix needed.
2. Test *function name* collisions (`test_{ClassName}_instantiation` in
   both suites) — 439/9,017 models (4.9%) affected; fixed by renaming every
   old-suite test with a `test_hyp_` infix before concatenation.
3. **Semantic duplication** — the actual point of "combined": two
   deterministic, AST-structural rules (never name-based) drop an old-suite
   test when the new suite already tests the identical thing, or something
   strictly stronger. Removed **360,308** redundant old-suite tests across
   8,367/8,368 models (avg ~43/model) on the full-dataset run.

Combined-suite coverage and whole-file mutation both measured; two more
issues found and fixed/excluded along the way (a stale-generation bug
affecting exactly 2 models, and 15 more `combined_suite_unmeasurable`
timeout exclusions, same root-cause class as `old_suite_unmeasurable`
below). Master exclusion list: **729** models (was 714, before this
session's additions).

Full writeup — every verification step, exact numbers, and the reasoning
behind each fix — in
[`2026-09-16-combined-test-suite.md`](2026-09-16-combined-test-suite.md).

## 2026-09-16 — Tree-sitter-based generator fidelity check and class coverage

Two new scripts built on top of the colleague's tree-sitter extractor
(`scripts/extract_structure.py`/`generate_code_structure.py`, already run
full-dataset into a per-model `code_structure.json`):

- **`scripts/validate_generator_fidelity.py`** — cross-references
  `model_metadata.json` (BUML model) against `code_structure.json` (actual
  code) for the first time. Run: 9,081/9,082 compared, **40.87% mismatch
  rate**. Confirmed root cause on `model_100127`: BUML declares
  `is_abstract=True`, generated code emits a plain class with no `ABC` base
  at all, ever — the generator doesn't implement UML "abstract" as a Python
  concept. Confirms the mechanism behind the earlier "0/732 methods are
  `@abstractmethod`" finding (2026-09-10 structural-test-generation entry).
- **`scripts/validate_class_coverage.py`** — of every class tree-sitter
  finds, what fraction got ≥1 passing test? New suite: 93.64% avg
  (9,043/9,082). Old suite: 95.96% avg (8,259/8,368, 109 timeouts, same
  Hypothesis-variance class as `old_suite_unmeasurable`).

**Process bug found and fixed**: both class-coverage commands were given
the same default `--report-name`, so the second run's cache-resume logic
silently reused the *first* run's results under the new key — every
model's `class_coverage_validation_hypothesis` was a byte-for-byte copy of
the new-suite's data, not a real old-suite measurement. `--test-file`
itself worked fine; nothing tied the cache to which test file was actually
measured. Fixed with a distinct `--report-name`. Not yet fixed at the code
level (the script should probably default its report-name to include the
test-file); noted, not built.

Full writeup in
[`2026-09-16-tree-sitter-fidelity-and-class-coverage.md`](2026-09-16-tree-sitter-fidelity-and-class-coverage.md).

## 2026-09-16 — New-suite mutation testing (whole-file + property-scoped) run to completion

Both mutation types now measured against `test_structural_full.py`,
completing the 2×2 comparison matrix (whole-file/property-scoped ×
old-suite/new-suite):

| | Old suite | New suite (restricted to the same model set) |
|---|---|---|
| Whole-file | 40.0% | 35.1% |
| Property-scoped | 40.49% | 35.97% |

New suite covers more code (line/branch coverage, see the 2026-09-10
structural-test-generation entry) but kills fewer mutants either way it's
scoped — coverage and mutation score answer genuinely different questions.
Property-scoped run hit the same encoding bug as `validate_coverage_structural.py`
and `check_property_name_mismatches.py` before it (`Path.read_text()`
missing `encoding="utf-8"`, same 4 models — `model_2210`/`2213`/`2243`/`2246`)
— this is now the *third* independent occurrence of this exact bug across
different scripts; fixed the same way, in
`validate_mutation_properties.py`'s `property_line_ranges()`.

## 2026-09-15 — Old-suite-unmeasurable models excluded (79)

**Context:** measuring line/branch/function coverage of `test_hypothesis.py`
(closing a gap in `reports/test_suite_comparison_report.md`) left 216 models
timing out at the default 60s. Escalated twice — 180s/8 workers (157 more
measured, 59 still timing out), then 300s/3 workers specifically to rule out
worker-contention as the cause (only 7 more measured, 52 still timing out).

**Diagnosis before accepting the loss:** manually re-ran two sample models
(`model_100063`, `model_1889`) standalone, repeatedly. Same file, wildly
different wall-clock times across attempts (didn't finish in 60s → 44.66s →
20.5s, for the identical test file with identical code) with ~0% measured
CPU load throughout, ruling out both an infinite loop and machine
contention as the cause. Root cause: unseeded Hypothesis search occasionally
draws an expensive input combination for some of this dataset's larger
`@given`-heavy suites — a real characteristic of the test suite, not a bug
in it, and not something retrying with different worker/timeout settings
converges on fixing (the next run could just as easily draw an expensive
seed again). This was actually flagged as a risk in `PROMPT.md` from the
very start of the project ("Hypothesis's `@given` tests are stochastic...
you likely want a fixed `HYPOTHESIS_SEED`") but never acted on.

Separately, the 27 `no_coverage_data` models from the very first pass are a
different, simpler cause: `test_hypothesis.py` fails to even *collect*, e.g.
a hard `SyntaxError` from `from` (a reserved Python keyword) used as a
keyword argument name — a real, pre-existing defect in the untouchable
ground-truth file, unrelated to timeouts.

**Decision:** stop retrying (diminishing returns) and exclude both groups —
52 persistent timeouts + 27 `no_coverage_data` = 79 models — under a new
`old_suite_unmeasurable` reason in the master exclusion list, rather than
leave them in an inconsistent measured/unmeasured limbo across later phases.
Full writeup in
[`2026-09-10-master-exclusion-list.md`](2026-09-10-master-exclusion-list.md).

## 2026-09-10 — Master exclusion list

Unions three independent exclusion reasons into
`reports/excluded_models_master.{json,txt}` (635 models total), tagged by
`reason_source` so any subset of these policies can be applied downstream
without re-deriving the list: `logic_validation.usable == false` (631,
refreshed post-fix, no known staleness — see the 2026-09-10 entry below),
`model_1339`/`model_1950` (test-infra-unfixable, see entry below), and
`model_10001058`/`model_2881` (property-name mismatches, see entry below).
The complement — 8,447 usable models — is in `reports/usable_models.txt`,
for scoping expensive runs (e.g. mutation testing) away from models with
nothing meaningful, or nothing trustworthy, to measure. Details in
[`2026-09-10-master-exclusion-list.md`](2026-09-10-master-exclusion-list.md).

## 2026-09-10 — Property-name mismatches: 2 models excluded, not fixable without breaking ground truth

**Finding:** a `@X.setter`/`@X.deleter`-decorated function whose name
doesn't match `X` doesn't reassign the property named `X` — decorator syntax
`@class2.setter\ndef class1(...)` desugars to `class1 = class2.setter(fn)`,
creating a *new*, separate property under the wrong name while the original
`class2` property is left getter-only. Concretely:
`instance.class2 = "x"` raises `AttributeError: can't set attribute`, while
the accidental byproduct `instance.class1 = "x"` works. Found by a new
read-only audit script, `scripts/check_property_name_mismatches.py`
(AST-based, same `encoding="utf-8"`-on-`read_text()` fix needed as
`validate_coverage_structural.py`'s `function_ranges()` — same 4 false
`parse_error`s on the same 4 models until fixed). Full-dataset run: 2
mismatches across 2 models (`model_10001058`'s `class2`/`class1`,
`model_2881`'s `self1`/`self`).

**Why not fixed:** `test_hypothesis.py` for both models already asserts
against the buggy name (`instance.class1 = ...`, `instance.self = ...`), not
the intended one — the test generator introspects what's actually on the
class, and the buggy setter genuinely works, just under the wrong name.
Renaming the function to match its decorator (the "obvious" fix) would flip
both currently-passing tests to failing, and `test_hypothesis.py` is
off-limits to modify. **Decision:** mark and exclude rather than patch,
consistent with the same policy applied to `logic_validation`.

## 2026-09-10 — `model_1339` / `model_1950`: excluded, not fixable with available tools

**Finding:** both models' `test_hypothesis.py` was already broken
independent of anything this session touched (safe to treat as pre-existing).
Attempting the obvious fix — regenerate `python_code.py` via besser's current
`PythonGenerator` — produces a *new* `SyntaxError:
non-default argument follows default argument`, a real bug in besser's own
template (likely emits association-end constructor parameters in unordered
`set`-iteration order without sorting required-before-optional args first).
Neither the existing test suite nor the regeneration path works for these
two specific models' structure.

**Decision:** mark and exclude, don't attempt further fixes — no BUML-level
edit is available the way there was for the 7 conversion-time bugs in
[`2026-09-10-buml-to-puml-conversion.md`](2026-09-10-buml-to-puml-conversion.md);
this is a defect in besser's generator itself. Neither model appears in the
colleague's `logic_validation` exclusion set (their `python_code.py` does
contain real logic) — this is a distinct exclusion reason, tracked
separately and then unioned into the master exclusion list (see entry
above).

## 2026-09-10 — Structural test generation for near-100% coverage, and a 4-type coverage validator

**User ask:** build a stronger, more deterministic baseline test suite (for
comparing a future diagram-shrinking tool's output against) and measure
coverage of it across as many dimensions as practical — discussed as 6
possible coverage "types," narrowed to 4 after weighing cost against
evidence of value for the other 2.

**New script:** `scripts/generate_structural_tests.py` → per-model
`test_structural_full.py`, deterministic-first (link → reassign → clear
sequences hit branches random `@given` sampling rarely reaches), with a
supplementary Hypothesis-based section kept for breadth. Full writeup of the
design decisions, the real dataset defects found and fixed along the way
(17+ `python_code.py` errors categorized by root cause, an encoding bug, a
BUML-name-vs-Python-identifier mismatch for special characters, and a
coverage-side `no_coverage_data`/`empty_model` misclassification) in
[`2026-09-10-structural-test-generation.md`](2026-09-10-structural-test-generation.md).

**New script:** `scripts/validate_coverage_structural.py` → line, branch,
function (custom AST-based — coverage.py's own per-function grouping merges
`@property` getter/setter pairs), and "structural" coverage (fraction of the
BUML model's true attribute/generalization/association total that a passing
test actually verifies) against `test_structural_full.py`, written to
`structural_coverage_validation`. Full run: 9,035/9,082 measured, avg 88.24%
/ 56.03% / 100.0% / 74.59% (line/branch/function/structural). Rationale for
measuring only 4 of the 6 discussed coverage types (condition/MC-DC and path
coverage deliberately excluded) in
[`2026-09-10-coverage-taxonomy.md`](2026-09-10-coverage-taxonomy.md).

**Incidental audit tool, execution on hold:**
`scripts/check_property_name_mismatches.py` — read-only check for
`@x.setter`/`@x.deleter` decorators whose function name doesn't match `x`.
Built but deliberately not run yet at the user's request; see the structural
test generation writeup for status.

## 2026-09-10 — Property-scoped mutation testing (`validate_mutation_properties.py`)

**User ask:** since almost all of this dataset's non-stub code is
getter/setter logic, build a mutation score scoped to just
`@property`/`@x.setter` regions, as a new, separate metadata key — explicitly
**not** merged into the existing whole-file `validate_mutation.py` /
`mutation_validation`, so already-computed results aren't overwritten.

**Findings, empirically:** getters generate 0 mutants (only `RemoveDecorator`
is possible against a bare `return self.__x`); 49.2% of setters are equally
"trivial" (plain assignment, no relationship logic) — only the
relationship-linked 50.8% (bidirectional `hasattr`/`getattr`/`setattr`
wiring) produce mutants with anything real to kill. Confirms there is no
explicit skip/filter for empty classes or stub methods anywhere in either
mutation script — it's a natural consequence of what cosmic-ray's operators
can act on, not something that needed building. Full table and rationale in
[`2026-09-10-mutation-scope-property-setters.md`](2026-09-10-mutation-scope-property-setters.md).

**Status:** smoke-tested on 3 models; a full 9,082-model `--write-metadata`
run was handed off to run unattended — check
`mutation_validation_properties` in `code_metadata.json` for current
completion status before citing full-dataset numbers.

## 2026-09-10 — BUML → PUML converter and structural `model_metadata.json`

**New script:** `scripts/buml_to_puml.py` — renders a PlantUML diagram from
each model's BUML source. Deliberately plain functions, not a forced
visitor/walker design — the traversal is a single pass over a handful of
known BUML types, so a class-hierarchy abstraction would add indirection
without buying anything.

**New script:** `scripts/generate_model_metadata.py` — a *new*,
separate `model_metadata.json` per model (never touches
`code_metadata.json`) with structural counts read directly from the BUML
model (classes, abstract classes, association classes, enumerations +
literals, attributes, methods, generalizations, associations,
aggregation/composition) — independent of whatever the code generator
produced, useful as ground truth for later comparison work.
**Correction made during design:** `AssociationClass` is a `Class` subtype
(confirmed via MRO) and must be counted in `classes`, not excluded as a
special case — `association_classes` is a subset count, not a separate
bucket.

**7 BUML-source bugs found and fixed** to reach a clean 9,082/9,082
conversion run (name collisions, undefined association variables, a wrong
metamodel-class reference, hyphens in `name=` strings, a blank domain-model
name) — table and per-model detail in
[`2026-09-10-buml-to-puml-conversion.md`](2026-09-10-buml-to-puml-conversion.md).

## 2026-09-10 — Windows-specific fixes to `validate_mutation.py`

The existing `validate_mutation.py` (built in the prior macOS session, entries
below) needed several Windows-only fixes to run at all on this machine —
distinct from, and unrelated to, that session's own fixes to the same file
(in-place mutation / scratch-copy safety, resume/cache):

- `cosmic-ray` resolved via `subprocess.run(["cosmic-ray", ...])` fails
  without the venv's `Scripts` dir on `PATH` (not activated in a subprocess)
  — resolved relative to `sys.executable`'s directory instead.
- `sys.executable`'s Windows backslash path breaks both TOML
  double-quoted-string parsing *and* cosmic-ray's own `shlex.split()` of the
  `test-command` — fixed via forward-slash normalization
  (`Path(...).as_posix()`) plus TOML literal (single-quoted) strings.
- `Path.read_text()` defaults to the OS locale encoding, not UTF-8, on
  Windows — corrupts multi-byte Unicode characters. Fixed with explicit
  `encoding="utf-8"` (the same bug class recurred later in
  `validate_coverage_structural.py`'s `function_ranges()` — see
  [`2026-09-10-structural-test-generation.md`](2026-09-10-structural-test-generation.md)).

Also added: LPT (longest-processing-time) scheduling — sort models by file
size descending before submitting to the worker pool, to reduce idle-worker
tail time — and an opt-in `--write-metadata` flag (single pass at the end,
only for `status == "measured"` results, requires `code_metadata.json` to
already exist).

## 2026-09-10 — Models with no testable logic: detected statically (not from coverage/mutation), and **marked**, not deleted

**User ask:** mark every model that "does not implement any logic" as not-to-be-used,
using best practice (mark vs. delete); and first check whether the metadata already
gathered (coverage / mutation / test validation) is sufficient to identify them.

**Was the existing metadata sufficient? No — and coverage/mutation are actively
the wrong signal here.** Two separate reasons:

1. *Availability:* a sweep of all 9,082 `code_metadata.json` files found exactly
   two keys everywhere — `python_code_validation` and `test_validation`. The
   coverage and mutation numbers only ever existed for prototype samples in
   `reports/` (250 / 231 / 38 models) and were never merged into metadata, so
   there is nothing dataset-wide to filter on.
2. *Validity:* even with a full run they would not work. A file made only of
   `class X: pass` declarations scores **100% line coverage** — importing the
   module executes every one of its statements, because all of them are class
   headers and `pass` — and produces **zero mutants**, because there is no
   operator, literal or branch to mutate. Both metrics look *perfect* exactly
   where there is nothing to measure. Confirmed empirically against the existing
   prototype reports: all 19 such models in the 250-model coverage sample scored
   100.0%.

**Detection method chosen: static AST analysis of `python_code.py`.** No
execution, no test run. Definition of "no logic": zero statements inside any
function/method body, counting neither `pass`/`...` stubs nor docstrings.

**Validated against the mutation ground truth we already had.** Against the
250-model cosmic-ray prototype: the 19 models cosmic-ray generated 0 mutants for
are *exactly* the 19 the static classifier calls unusable — 19/19 agreement, 0
false positives among the 231 models that did produce mutants. Across those 231,
correlation between static statement count and mutants generated is r = 0.995.
The static pass covers all 9,082 models in **~15 seconds**; the 250-model
mutation prototype alone cost ~7 CPU-hours. The cheap static signal reproduces
the expensive dynamic one exactly for this purpose.

**Decision: mark, do not delete.** Reasons, in order of weight:
- The dataset is a published research artifact derived from ModelSet, with
  externally-referenced model ids (`model_path.txt`, the Java renderings, the
  release bundle). Deleting directories breaks those references and silently
  invalidates the two prior validation reports, which are keyed by model name.
- The no-logic models *are a finding* about the B-UML→Python generator (566
  models where every class is a bare `pass`), not noise to be swept away. They
  are the negative examples for any future generator work.
- Marking is reversible and additive; deletion is neither.
- Consumers filter on one predicate, and get the reason for free.

**New script:** `scripts/validate_logic.py`, same shape as the other validators
(`--dataset-dir`/`--reports-dir`/`--workers`/`--limit`), but **defaults to a dry
run** — it only touches `code_metadata.json` when `--write-metadata` is passed,
so the classification can be reviewed before it lands. Adds a `logic_validation`
key per model with `status`, a boolean `usable`, a human-readable
`exclude_reason`, and a `metrics` block (classes, empty classes, enum classes,
init/getter/setter/operation counts, logic statements, branch statements).

**Full run (2026-09-10, `--write-metadata`):** 8,438/9,082 usable (92.91%), 644
excluded — 630 `no_logic`, 12 `syntax_error`, 1 `missing_file`, 1 `empty_file`.
Verified with `git status --porcelain -- Dataset` that exactly 9,082 files
changed and every one of them is a `code_metadata.json`. Reports:
`reports/logic_validation_report.{json,md}` plus a flat
`reports/excluded_models_no_logic.txt` so consumers need not walk 9,082
metadata files.

**Incidental finding, and a significant one: the dataset contains zero
implemented operations.** All **19,768** B-UML operations, across the 1,037
models that declare any, are `pass` stubs — there is not a single implemented
operation body anywhere in the 9,082 models. This is the dataset-wide
generalisation of the 2026-09-01 test-validation finding (907 models failing
because tests assert stubbed operations change state). It also means a stricter
reading of "implements no logic" — *no implemented operations* — would exclude
all 1,037. That is deliberately **not** what `usable: false` encodes: those
models still carry real bidirectional-association logic in their property
setters, which is genuinely coverable and mutable. The stricter reading is
exposed separately as `all_operations_stubbed`, so either exclusion policy can
be applied downstream without a re-run. Written up in full, with the
`AssertionError` cross-reference and an upstream recommendation, in
[`2026-09-10-zero-implemented-operations.md`](2026-09-10-zero-implemented-operations.md).

---

## 2026-09-02 — New metric: coverage split by test section (structural vs. hypothesis), empty-method exclusion

**User ask:** add per-model coverage ratios to metadata, but computed separately
for the two halves of `test_hypothesis.py` (`SECTION 1 — STRUCTURAL TESTS` vs
`HYPOTHESIS STRATEGIES`), and for the hypothesis half only, exclude statements
belonging to "empty" (no-logic) methods from both numerator and denominator so
a trivially-executed `pass` stub doesn't inflate the score.

**Test-group selection:** Hypothesis's pytest plugin auto-applies a `hypothesis`
marker to every `@given` test, so `pytest -m hypothesis` / `-m "not hypothesis"`
cleanly separates the two groups with no need to parse test node ids out of the
file. Verified against `model_1`: 9 `-m hypothesis` / 23 `-m "not hypothesis"`,
matching an independent AST count of `@given` decorators exactly.

**"Empty method" definition (confirmed with user, then verified empirically
across a random sample of 300 models):** a function/method whose entire body
is *exactly one* `pass` statement — no docstring, no other variant (no
`raise NotImplementedError`, no bare `return`) was found anywhere in the
sample. This only ever hits generated `Operation` methods (never `__init__`,
never `@property`/`@x.setter`, which always contain real assignments) — the
same stub-`pass` operations flagged in the 2026-09-01 test-validation entry
below (907/9082 models). Implemented as an AST walk over every
`FunctionDef`/`AsyncFunctionDef`, recording the line number of the lone
`pass` when `len(node.body) == 1 and isinstance(node.body[0], ast.Pass)`.

**Adjustment mechanics:** run pytest+coverage once per group with
`--cov-report=json`, which gives per-file `executed_lines`/`missing_lines`
arrays (not just totals — needed to subtract specific line numbers). For the
hypothesis-only run, the "implemented-only" ratio = drop every empty-method
line from both the executed and the (executed∪missing) sets, then
recompute the percentage. The structural ratio is never adjusted — the user
wants the full structural-component count there.

**New script:** `scripts/validate_coverage_split.py`, same shape as
`validate_coverage.py` (resume/cache, ProcessPoolExecutor, prototype-only —
does not touch `code_metadata.json` unless `--write-metadata` is passed,
which was not used this session). Trial run: 38 models (the first 30 of
`reports/prototype_sample_models.txt`, plus 8 models known to have
stub-operation `AssertionError` failures, added specifically to exercise the
empty-method exclusion path — the first 30 alone happened to contain zero
empty methods). All 38 measured without errors; 2 of the 8 assertion-error
models (`model_100063`, `model_100064`, 72 empty methods each) timed out on
the hypothesis-only run at 120s and were recorded with `status: "timeout"`,
not a crash. Report: `reports/coverage_split_prototype_report.{json,md}`.

**Full run:** user approved the trial numbers and asked for the full
9,082-model `--write-metadata` run. Started locally, but the user then asked
to hand it off to another machine instead (same pattern as the mutation
prototype's compute handoff below) -- stopped the local run after confirming
via `git status --porcelain -- Dataset` that no `code_metadata.json` had been
touched yet (the script only writes metadata in a single pass *after* all
models finish, not incrementally, so an interrupted run never leaves partial
metadata) and no stray process remained. Command for the other machine:
`python3 scripts/validate_coverage_split.py --workers <N> --timeout 120 --write-metadata`
(the 38-model trial cache/report were not committed, so it starts fresh).

## 2026-09-01 — Resume/cache support added to both validator scripts after a real 250-model run risk

**Context:** the 250-model mutation prototype run (on the second, more
capable machine) took ~7 CPU-hours summed across models (p50 75s, p99 462s,
max 852s per model) before this was added. Before this change, both scripts
only wrote their aggregate report at the very end -- a kill/SSH-drop/reboot
partway through, which is a real possibility at that runtime, would have
discarded all progress with no way to resume short of starting over.

**Fix:** both `validate_coverage.py` and `validate_mutation.py` now append
each model's result as one JSON line to `<report-name>.cache.jsonl` in
`reports/` the moment that model finishes (flushed immediately, not
batched). On startup they read that file, skip any model already present,
and merge cached + freshly-computed results into the final report. `--fresh`
ignores an existing cache and recomputes everything.

**Verified:** launched a 6-model mutation run, hard-killed it after 3
completed, confirmed (a) the dataset directory was untouched -- consistent
with the scratch-copy fix above -- and (b) the cache file had exactly those
3 results; reran without `--fresh` and confirmed only the remaining 3 were
computed and the final report merged all 6. Also confirmed `--fresh`
correctly ignores a stale cache (reran with a different `--max-mutants` and
got the new cap applied to a previously-cached model).

## 2026-09-01 — cosmic-ray mutates the target file in place on disk; script now runs it against a scratch copy, never the real dataset

**Finding (caused real, if recovered, dataset corruption this session):**
cosmic-ray's worker mutates the target module **in place on disk**, runs the
test command, then reverts the mutation -- it does not mutate a copy. The
first version of `scripts/validate_mutation.py` pointed cosmic-ray directly
at `Dataset/<model>/python_code.py`. When that run was stopped mid-flight
(`TaskStop` + `pkill`, because the run was too heavy for the local machine —
see below), 8 models were left with a live, unreverted mutation sitting in
their git-tracked `python_code.py` (e.g. `if opp_val == self:` silently
flipped to `if not opp_val == self:` in `model_100015`). Caught immediately
via `git status --porcelain -- Dataset` and restored with `git checkout --`;
nothing was committed.

**Fix:** `validate_model()` now copies only `python_code.py` +
`test_hypothesis.py` (confirmed by grepping a sample of models that
`test_hypothesis.py` never imports anything else local — only stdlib +
hypothesis/pytest) into a fresh `tempfile.mkdtemp()` scratch dir per model,
and runs `cosmic-ray init`/`exec` there. The real `Dataset/` tree is only
ever read, never written. **Verified** by hard-killing (`kill -9`) a live
8-worker run mid-mutation and confirming `git status --porcelain --
Dataset` came back empty afterward (only a harmless leftover scratch dir
under `$TMPDIR` remained, cleaned up manually since the killed process never
reached its own `finally: shutil.rmtree(...)`).

**Process takeaway:** for any tool that mutates files in place with a
revert-after step (as opposed to mutmut, which mutates a separate copy under
`mutants/`), never point it at anything git-tracked directly — always run
against a disposable copy, *especially* once the plan involves killing runs
mid-flight (e.g. to hand heavy compute off to another machine) rather than
always letting them finish cleanly.

## 2026-09-01 — Prototype run moved off this machine: local machine is compute-constrained

**Decision:** the 250-model mutation prototype (cosmic-ray, capped at 40
mutants/model) was started locally, but the user flagged this machine as
weak partway through — `uptime` showed a 1-minute load average of 13.3 with
just 8 parallel workers running. Killing that run is what surfaced the
in-place-mutation bug above. Workflow going forward: validate scripts on a
small sample (~10 models) locally, commit + push, run the actual
sample/full-dataset job on a second, more capable machine, then pull results
back. See the handoff command recorded alongside this entry in the session
notes / commit message.

## 2026-09-01 — Coverage tool: coverage.py + pytest-cov (decided, no real alternative)

- `coverage.py` 7.16.0 (released 2026-08-28), Python 3.10–3.15rc1, actively
  maintained (Ned Batchelder + 263 contributors).
- `pytest-cov` 7.1.0 (released 2026-03-21), actively maintained, wraps
  coverage.py for pytest integration.
- No serious competing library exists in the Python ecosystem for line/branch
  coverage measurement. Not worth further evaluation.

## 2026-09-01 — Mutation tool shortlist: maintenance status re-verified

Checked PyPI/GitHub for each candidate from the prior session's shortlist:

| Tool | Latest release checked | Status |
|---|---|---|
| mutmut | 3.7.0 (2026-07-31) | Actively maintained |
| cosmic-ray | 8.7.0 (PyPI, checked 2026-09-01) | Actively maintained |
| mutatest | 3.1.0 (2022-02) | **Unmaintained** — Snyk flags "Inactive", no release in 3+ years. Dropped. |
| mutpy | last repo update 2024-04 | **Unmaintained** — no active PyPI release cadence. Dropped. |

## 2026-09-01 — mutmut cannot mutate `@property`/`@x.setter` methods (architectural, not configurable)

**Finding:** mutmut's source (`mutmut/mutation/file_mutation.py`, around line
281–291) explicitly skips every decorated function except
`@staticmethod`/`@classmethod`:

> "ignore decorated functions, because [...] @property decorators break the
> trampoline signature assignment (which expects it to be a function)"

This is a hard limitation of mutmut's mutation mechanism (it wraps each
mutated function in a "trampoline" that swaps between original/mutant
implementations at call time — that mechanism can't wrap a property
descriptor), not something exposed via any config flag.

**Why it matters for this dataset specifically:** the generated
`python_code.py` files put essentially all of their non-trivial logic —
bidirectional association consistency (`if opp_val == self`,
`hasattr`/`getattr`/`setattr` chains, `is not None` guards) — inside
`@property` getters and `@x.setter` setters, not in `__init__` bodies or
plain methods. `__init__` just calls the setters.

**Empirical confirmation** (`Dataset/model_1`, manual run, artifacts cleaned
up afterward — not committed):

- mutmut generated **13 mutants total**, confined to the two `__init__`
  methods (`petrinet_Node.__init__`, `petrinet_Petrinet.__init__`). **All 13
  survived** (0% kill rate).
- cosmic-ray, same model, same test suite: **135 mutants** covering
  comparison operators throughout the setter logic. **19/135 killed (14%)**.
- Baseline test suite: 32 tests, 0.52s.

**Decision:** do not use mutmut as primary despite it being cheaper — for
this dataset it would only ever score `__init__` bodies, which is not where
the interesting behavior lives. See next entry for the cost tradeoff this
creates.

## 2026-09-01 — cosmic-ray has no coverage-guided/test-impact mutant skipping — costs ~1 full suite run per mutant

**Finding:** unlike mutmut (which tracks per-function test dependencies and
only reruns tests that actually exercise the mutated function — ~0.2s/mutant
on `model_1`, confirmed via `mutants/mutmut-stats.json`'s
`tests_by_mangled_function_name` / `function_dependencies`), cosmic-ray's
`local` distributor reruns the **entire** test command once per mutant, with
no test-impact analysis. Confirmed empirically: 135 mutants took ~60s wall
time on `model_1`, i.e. ~0.44s/mutant — essentially the full 0.52s baseline
suite runtime per mutant (survived mutants run to completion; only killed
ones benefit from `-x` fail-fast cutting the run short).

**Why it matters for scope:** this dataset already has per-model baseline
suite runtime up to ~60s+ (largest suites), and 9,082 independent models.
Mutation testing at cosmic-ray's per-mutant cost is roughly baseline-runtime
× mutant-count per model — for a model with a 60s suite and, say, 100
mutants, that's ~100 minutes for that one model alone.

**Decision:** use cosmic-ray (for correctness — it isn't blind to setter
logic) but cap mutants per model. cosmic-ray has **no built-in CLI flag** to
limit mutant count, so the cap is implemented by directly deleting rows from
the `mutation_specs`/`work_items` tables in the session sqlite db (written by
`cosmic-ray init`) before running `cosmic-ray exec` — see
`scripts/validate_mutation.py::cap_mutants()`. Sampling is seeded by model
name for reproducibility across reruns.

User approved: **cosmic-ray, capped** (over "mutmut anyway" or "run both and
compare empirically") — see conversation; the property/setter blind spot was
judged disqualifying for mutmut given this dataset's shape, despite the cost
advantage.

## 2026-09-01 — Generated Hypothesis tests often don't assert constructor values, only `isinstance`

**Finding, incidental to the mutmut experiment above:** on `model_1`, the
`@given`-based instantiation tests are shaped like:

```python
@given(instance=petrinet_Node_strategy)
def test_petrinet_node_instantiation(instance):
    assert isinstance(instance, petrinet_Node)
```

They never check that a constructor argument (e.g. `name=`) actually landed
in the resulting object (`instance.name == name`). This is *why* all 13
`__init__`-mutating mutants survived even though they replaced real
assignments with `None` (e.g. `self.name = name` → `self.name = None`) — the
mutation is real and wrong, but nothing in the generated suite would ever
catch it.

**Relationship to the prior session's finding:** the test-validation report
already found 907/9082 models fail because of empty (`pass`-body) generated
*operations* — a gap in the generated *code*. This is a distinct and
additional gap, in the generated *tests*: even where the code is not a stub,
many tests exercise it without asserting anything about its actual effect.
Both should probably be reported side-by-side once mutation scoring is
available dataset-wide, since raw mutation score alone conflates "nothing to
mutate" (empty code) with "mutated but nothing checks it" (shallow tests).

## 2026-09-01 — `__pycache__` must never be blanket-deleted from model directories

**Finding (self-inflicted, caught and fixed same session):** an early
version of `scripts/validate_mutation.py`'s artifact-cleanup step did
`shutil.rmtree(model_dir / "__pycache__")` unconditionally. Some model
directories ship **pre-existing, git-tracked** `.pyc` files (e.g.
`model_10000017/__pycache__/model_10000017_buml.cpython-312.pyc` — Python
3.12 bytecode, likely from a Java/BUML toolchain step, unrelated to pytest's
own bytecode cache which runs under 3.13). A 5-model smoke test briefly
deleted 5 such tracked files; caught via `git status --porcelain -- Dataset`
immediately after and restored with `git checkout --`.

**Fix:** cleanup now only removes `.pytest_cache` and `.hypothesis` (always
safe — those are pytest/Hypothesis's own run-scoped caches, disabled/redirected
where possible in the first place via `-p no:cacheprovider` and
`HYPOTHESIS_STORAGE_DIRECTORY`). `__pycache__` is left alone entirely;
`PYTHONDONTWRITEBYTECODE=1` already prevents new `.pyc` files from being
written during validation runs, so there is nothing of ours to clean up
there.

**Process takeaway:** always run `git status --porcelain -- Dataset` after
any dataset-wide script that does directory cleanup, *before* trusting a
"looks clean" smoke test — a clean stdout doesn't mean the working tree is
unmodified.
