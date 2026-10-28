# The BESSER benchmark dataset: what was done, found and decided

One document for the whole project, September to October 2026. It replaces
reading the dated explainers in `docs/` one by one; each section says where
the detail lives. Where an older document gives a different number, the
number here is the current one (section 12 lists what was superseded and why).

## In short

- **Goal.** Turn the BESSER B-UML dataset into a clean benchmark for a
  separate project that shrinks UML class diagrams (PlantUML) and asks an LLM
  to generate Python code from the original and the shrunk diagram. This repo
  provides the data only. The shrinking, the comparison and the iteration
  live in the benchmarking repo; the LLM calls live in the code-agent repo.
- **Data.** 9,082 source models → 8,336 usable → **5,264 unique**. Each has a
  lossless PlantUML diagram, the reference Python implementation, a test
  suite that passes on it, structural metadata and a difficulty score.
- **Test suite.** Built from the dataset's own tests plus three generators of
  ours. Property-scoped mutation score **75.61%**, against **35.60%** for the
  dataset's original tests: **+40.01 points, 4,640 models better, 0 worse.**
  The gain grows with difficulty, from +30 to +61 points.
- **Difficulty.** A 0-100 score from PCA over 11 structural counts (PC1+PC2,
  62% of variance), agreeing with the reference paper's formula at Spearman
  0.92. Ten 10-point buckets drive a stratified train/test split.
- **Open.** The train ratio and the hand-over details are with the
  benchmarking side (`docs/handout.md`). Everything else is done.

---

## 1. The three repositories

| Repository | Owns |
|---|---|
| **BESSER-Dataset** (this one) | the models, their diagrams, reference code, test suites, metadata, difficulty score, split and export |
| benchmarking | iterating over the export, PSO-driven shrinking of the PUML (tuning genetic-algorithm and Kruskal parameters), running the suites on generated code, comparing |
| code agent | the LLM calls and the prompts |

This repo deliberately contains no iterator, no shrinking and no prompts. Its
output is an export folder (section 9) that the benchmarking repo can clone
and iterate over.

## 2. The source dataset

The BESSER B-UML dataset: 9,082 models derived from ModelSet, which collects
Ecore metamodels scraped from GitHub. Each model folder holds the BUML model
(BESSER's Python modelling format), generated `python_code.py`, a generated
pytest + Hypothesis suite `test_hypothesis.py`, a textual description, an
image, a Java rendering, a category label and `model_path.txt` (the source
file in ModelSet).

What the first validation runs found:
- `python_code.py` compiles and runs for 9,064 of 9,082 (99.80%).
- `test_hypothesis.py` passes for 8,027 (88.38%). Of the 1,055 failures, 919
  are `AssertionError`, and 918 of those trace to one cause, below.
- **No operation in the dataset has a body.** All 19,768 BUML operations, in
  the 1,037 models that declare any, are generated as `# TODO: Implement` +
  `pass` (8,878 in 699 models of the 5,264 unique ones). The dataset's own tests deliberately fail on such stubs
  ("`..._changes_state`, FAIL if empty"), which is where the 918 failures
  come from. Consequence for everything below: every piece of real logic in
  the reference code is in property setters (bidirectional association
  bookkeeping), and that is what mutation testing measures.
- **The dataset's own tests are weak.** Most only check
  `isinstance(instance, Class)`. On `model_1`, all 13 constructor mutants
  survived because no test checked that a constructor argument landed.

Detail: `docs/2026-09-10-zero-implemented-operations.md`, DECISIONS
2026-09-01.

## 3. Which models are usable: 9,082 → 8,336

Models are **marked, not deleted**: the dataset is a published artifact with
external model IDs, and the excluded models are findings in their own right.
`reports/excluded_models_master.json` tags each with its reason:

| Reason | Models | What it means |
|---|---:|---|
| `logic_validation` | 631 | No executable statement anywhere in `python_code.py` (every class `pass`). Coverage is a trivial 100% and there are zero mutants. Detected statically; agreed 19/19 with cosmic-ray's zero-mutant models. |
| `old_suite_unmeasurable` | 79 | The dataset's suite can't be measured: 52 persistent timeouts from unseeded Hypothesis search, 27 that don't even collect (e.g. `from` used as a keyword argument) |
| `combined_suite_unmeasurable` | 32 | Same causes once the suites were merged: 15 coverage timeouts, 17 mutation timeouts even at 1,800 s |
| `property_name_mismatch` | 2 | `@X.setter` on a function named `Y` creates a phantom property; the dataset's tests already assert the wrong name |
| `test_infra_unfixable` | 2 | Broken tests, and besser's own generator emits invalid Python on regeneration |
| **Excluded** | **746** | |
| **Usable** (`reports/usable_models.txt`) | **8,336** | |

The BUML-to-PUML conversion also surfaced 7 BUML source bugs (name
collisions, undefined variables, hyphens in names), fixed in the BUML so all
9,082 convert. Detail: `docs/2026-09-10-master-exclusion-list.md`,
`docs/2026-09-10-buml-to-puml-conversion.md`.

## 4. Copies removed: 8,336 → 5,264

**Finding.** 37% of the usable models are copies of another model. The same
Ecore file sits in many GitHub repositories, so ModelSet holds it many times,
and the `model_1000xxxx` batch (no `model_path.txt`) is 60% copies, with five
groups of 158-200. A copy is the same benchmark task again: it multiplies LLM
and compute cost, weights one diagram many times in every average and in the
PCA fit, and could leak between train and test.

**How copies are identified** (`select_unique_models.py`,
`_common.buml.buml_fingerprint`). On the original BUML, not on anything we
generated, ignoring exactly three meaningless differences:
1. the order of items in set literals
2. statement order and comments
3. the model's own `name=`, a random ID per copy

Everything else must match: classes, attributes, types, methods,
enumerations, generalizations, associations, role names, multiplicities,
constraints. Two subtleties in the source had to be handled:
- **Overloaded methods** are defined by assigning one variable twice, and
  only the last definition reaches the model. Sorting statements would hide
  which one, so dead statements are dropped and every binding is renamed
  after its content before sorting.
- **Variable names are reused** across elements (one name for an attribute
  and an association).

**Verified three ways.** The BUML fingerprint, the lossless PUML (section 5)
and an independent grouping by the model besser builds all give the same
5,264 groups, model for model. Within a group, `python_code.py` is identical
up to ordering in 1,014 of 1,018 groups. The other 4 differ only in how
besser's generator renamed an attribute called `property`, which depends on
set order.

**Decision.** One representative per group (alphabetically first):
**5,264 unique models**, 3,072 copies in 1,018 groups.
`reports/unique_models.txt` replaced `usable_models.txt` for every later
step.

**Only exact copies are removed.** Forks with one extra attribute or a
renamed class are different models: a different diagram, different code,
a different task. Any similarity threshold would be our own arbitrary choice,
while exact copies are a property of the source anyone can check.

**Why it was found late.** Every validator works on one model at a time.
Copies were noticed on 2026-09-29 (by method-count signature) and removed
from the 200-model sample, but never counted dataset-wide. Code-level hashes
miss them because the copies' code differs in ordering. The sample was
checked afterwards: all 200 are representatives, so its results stand.

Detail: DECISIONS 2026-10-18 (two entries).

## 5. The PlantUML diagram (the benchmark input)

`buml_to_puml.py` writes one `.puml` per model. It is sorted throughout, so
identical models give identical files, and it is **lossless**: everything
any BUML model in the dataset specifies is written out.
- **Elements:** classes (abstract or not), attributes with types,
  operations with typed parameters and return types, enumerations, and
  generalizations.
- **Associations:** role names and multiplicities on both ends, composition
  on either or both ends, `{not navigable}` ends.
- **Constraints:** OCL constraints as notes (418 in 31 models).
- **Metadata:** model, project, owner and description as `'` comments.

This was not the case at first. Role names were missing. They are the
attribute names every association test uses, so code generated from the old
PUML could never have passed those tests, and the benchmark comparison would
have been broken from the start. OCL constraints, the metadata, navigability
and two-sided composition were missing too. After finding gaps one by one,
the conversion was made complete by construction and verified on every
model:

- `verify_puml_conversion.py`, three checks per model:
  1. Every BUML construct used is one the converter handles.
  2. Round trip: the PUML is parsed back and compared, fact by fact, with
     the model besser loads.
  3. Every string literal in the BUML source appears in the PUML.

  Result: **9,082/9,082 lossless.**
- `selftest_conversion_checks.py` mutation-tests the checks themselves on
  300 random models plus all 32 models with rare constructs:
  - 24 kinds of real BUML change must change the fingerprint, and 4 kinds of
    noise must not.
  - 17 kinds of PUML corruption must be reported by the verifier.

  Result: **every one exercised, 0 fooled, 0 false alarms.**

The format, with real examples, is in `docs/handout.md` section 3. Since the
benchmarking repo's shrinker parses this format, its changes (role names,
`*--*`, `{not navigable}`, constraint notes, `'` comments) are listed there
for them.

## 6. Structural metadata and the difficulty score

**`model_metadata.json`** holds counts read from the BUML model, independent
of the generated code: classes, abstract classes, enumerations and literals,
attributes, methods, generalizations, associations, compositions, many-valued
association ends and attribute type diversity. `associations` was redefined
to exclude compositions, so the relationship counts no longer overlap.
Aggregation and association classes never occur in the dataset.

**The reference paper's formula** (Cheng et al., "Large Language Models for
UML Class Diagram Modeling", *Appl. Sci.* 2026, 16, 6540) is
`D = 0.3571·C + 0.4082·R + 0.2347·A`: classes, relationships, attributes;
readability term dropped, weights rescaled. It is calibrated on 30 textbook
exercises with at most 13 classes, and it has two problems at this
dataset's scale:
- **It is unbounded.** It uses raw counts, unnormalized by design.
  `model_2023` (932 classes) scores 931, about 67 times the paper's own
  average "hard" exercise.
- **It is blind to some structure.** It ignores enumerations, methods and
  types, so `model_3616` (344 enumerations, 1,223 literals) scores 0.

**Our score** (`compute_difficulty_score.py`):
1. log1p of 11 counts, z-scored, PCA on the correlation matrix (deterministic).
2. PC1 (all loadings positive: overall size) plus |PC2| (a style contrast
   between attribute-rich flat models and deep hierarchies; its sign is
   arbitrary, hence the absolute value).
3. Each is clipped to its 1st-99th percentile and rescaled to a point budget
   proportional to its variance.
4. The two are summed, so the score lies in 0-100 by construction.

**Final fit, on the 5,264 unique models:**

| | PC1 | PC2 | PC3 |
|---|---:|---:|---:|
| Variance explained | 48.8% | 13.7% | 10.2% |
| Points in the score | 78.1 | 21.9 | – |
| Spearman with the article, PC1..PCk | 0.9164 | 0.9165 | 0.9036 |

**Why PC1+PC2.** Retention tests disagree: Kaiser and parallel analysis
keep 3 components, broken stick keeps 1.
- PC2 is a real, interpretable second axis. Its extremes are above-average
  models, not small ones drifting there. It costs nothing in agreement with
  the article (0.9164 → 0.9165).
- PC3 was measured directly (experiment 6). It barely changes the ranking
  (Spearman 0.988 with PC1+PC2), but it moves 23.4% of models one bucket. It
  lifts small enumeration-heavy models by up to 11 points and drops the
  largest models by about 12. Models with methods fall more than models
  without. For a code-generation difficulty measure that is noise, so PC3
  stays out.

Retention tests say how many components carry signal, not which ones serve
a given purpose. The choice is a measured one and is reported as such.

**Independent evidence the score means something:** the dataset's own tests
cover hard models worst (baseline mutation score 0.39 in the easiest bucket,
0.23 in the hardest; section 8).

**Buckets** (10 points each, 0-10 … 90-100):
363 / 1,239 / 1,294 / 1,002 / 647 / 336 / 188 / 127 / 59 / 9.

Detail: `docs/2026-09-28-explainer-pca-difficulty-score.md`, DECISIONS
2026-10-18 (PCA entry), `experiment_difficulty_score_pca.py` and its report.

## 7. Measuring test quality

### Tools

- **Coverage:** coverage.py + pytest-cov. There is no serious alternative.
- **Mutation:** cosmic-ray, not mutmut. mutmut skips every decorated
  function by design, so it can't mutate `@property` getters and setters,
  which is where all of this dataset's logic is. On `model_1`, mutmut found
  13 mutants (all in `__init__`) and cosmic-ray found 135. mutatest and
  mutpy are unmaintained.
- **The score used throughout: property-scoped mutation**
  (`validate_mutation_properties.py`). Only mutants inside property getters
  and setters, which are about 97% of all mutants anyway. Each model is
  capped at 40 mutants, drawn by a seeded sample.

### Pitfalls found in the measurement itself

Each of these would have produced wrong numbers without any error showing:

| Problem | Effect | Fix |
|---|---|---|
| cosmic-ray mutates the file **in place** and reverts afterwards | A killed run left 8 dataset files mutated (caught in `git status`) | It always runs on a scratch copy |
| The mutant cap sampled **positions** in an unordered SQL result | The "seeded" sample differed between runs (27 of 40 mutants on `model_1`); no historical per-model score was reproducible | Sort mutants by content before sampling: identical sets across runs |
| Unseeded Hypothesis | Run-to-run noise and random timeouts | `--hypothesis-seed 0` for every comparison run (a convention; nothing records it) |
| **A suite that fails on the unmutated code "kills" every mutant** | Fake perfect scores. 155 of 200 sample suites failed unmutated; the published 92.66% was really 77.55% (section 8) | A baseline guard: the suite must pass unmutated first, or the model gets `baseline_failed` and no score. And every suite is made green before measuring. |
| A per-mutant timeout counts as a **kill** | Load could inflate scores without anyone seeing it | Timeout kills are counted (`killed_by_timeout`) and reported; the worst case (all of them survived) is shown next to the real number |
| Caches keyed only by report name | A second run with another test file silently reused the first run's results | Each cached result records its test file; mismatches are recomputed |
| Failed models cached as done | Retries meant new report names and manual merges | Timeouts and errors are retried automatically under the same report |

DECISIONS 2026-09-01, 2026-10-01 (`cap_mutants`), 2026-10-17, 2026-10-18 and
2026-10-20 have the details.

## 8. Building the test suite

### The path

1. **Structural generator** (`generate_structural_tests.py` →
   `test_structural_full.py`). Deterministic tests of attributes,
   constructors, generalizations and associations (link → reassign →
   clear), driven by the BUML. It checks the actual code for which side of
   an association has a real setter, because the generated code often
   implements only one side (in `model_1`, 5 of 7 classes are bare stubs).
   On its own it covers more code than the dataset's tests but kills fewer
   mutants, because coverage and mutation score answer different questions.
2. **Combined suite** (`generate_combined_tests.py` → `test_combined.py`).
   The dataset's tests (renamed `test_hyp_…` to avoid silent name clashes,
   which hit 4.9% of models) plus ours. Old tests that ours duplicate or
   strictly subsume are dropped: 360,308 of them.
3. **Which test generators help.** Compared on a 200-model sample,
   stratified equally across 7 buckets of logic-bearing method counts:
   - **Pynguin:** dropped. Its assertions are `isinstance`-only on this
     code, and it scored far below the baseline.
   - **UTBotPython:** dropped. It has no native-Windows path (Docker, Linux,
     Python 3.9), and it is the same tool family as CrossHair.
   - **CrossHair** (symbolic execution) helps. It can't target properties
     at all, only operations and constructors.
   - **Behavioral tests (ours).** A surviving mutant on `model_1` showed
     that tests drove each association only from one end. The new
     generator drives it from both ends independently.
   - **Stub doubles (ours).** Mutants behind a link to a stub class looked
     unkillable, because the stub never has the attribute the real side
     checks for. A test can attach that attribute itself first (a standard
     test double), and these mutants turned out killable after all.
     `model_1`: 35% → 95%.
4. **Super suite** (`generate_super_suite.py` → `test_super_suite.py`):
   combined + behavioral + CrossHair in one file. Merging, rather than
   choosing one generator, keeps the "never worse" property: CrossHair alone
   helped 72 models and hurt 65 (in the early, unguarded measurement), but
   merged it only adds.

### The false positive, and green suites

The first sample result, 92.66% vs 50.85%, was inflated. 155 of 200 super
suites failed on the unmutated code, which scores every mutant as killed.
There were four causes:
1. Our stub-double tests asserted the wrong shape for collection ends.
2. CrossHair tested Python's own `Enum` internals.
3. CrossHair used `datetime` without importing it.
4. The dataset's empty-method checks fail on the stub operations. These sit
   in the baseline too.

The fix:
- The baseline guard (section 7).
- Fixed generators.
- **Green suites.** Every test that fails on the reference is removed and
  listed, the same way for the baseline. A test that fails on the reference
  can't judge generated code either, so this is also what the benchmark
  needs.

The honest sample result: **77.55% vs 34.52%, +43.03 points, 188 better,
0 worse.**

### The stub-assertion fix

While writing the handout we found 3,371 CrossHair tests in 407 models that
asserted what an empty stub operation returns (`== None`), while the PUML
declares, e.g., `: str`. Code that implements the operation as declared
would fail them. The sanitizer now turns such an assertion into a bare call,
which still fails if the operation is missing or takes other arguments.
Mutation scores for the 407 models are unchanged (0.8064 before and after),
as expected, since only properties are mutated.

### Final result: all 5,264 unique models

All suites rebuilt and remeasured (`docs/RUNBOOK-full-regeneration.md`):
- **Behavioral:** 66,543 tests.
- **CrossHair:** tests for 4,106 of the 5,064 non-sample models. The other
  958 have only property classes. 17.7% of classes got tests within the
  300 s per-model cap.
- **Super suite:** 1,023,139 tests.
- **Green baseline** (`test_combined_green.py`): 931,579 tests.
- **Green:** 5,264/5,264 for both. Removed tests: 6,250 in 650 models (super
  suite) and 6,210 in 649 (baseline), almost all the dataset's empty-method
  checks.
- **Mutation:** 40 mutants per model, seed 0, the same 190,966 mutants in
  both runs, 0 `baseline_failed`.

| Bucket | Models | Baseline | Super suite | Lift (pts) | Better / worse / same |
|---|---:|---:|---:|---:|---|
| 0-10 | 363 | 0.394 | 0.696 | +30.1 | 237 / 0 / 126 |
| 10-20 | 1,239 | 0.385 | 0.764 | +37.9 | 1,096 / 0 / 143 |
| 20-30 | 1,294 | 0.379 | 0.744 | +36.5 | 1,112 / 0 / 182 |
| 30-40 | 1,002 | 0.352 | 0.741 | +38.8 | 880 / 0 / 122 |
| 40-50 | 647 | 0.319 | 0.765 | +44.5 | 611 / 0 / 36 |
| 50-60 | 336 | 0.296 | 0.800 | +50.4 | 326 / 0 / 10 |
| 60-70 | 188 | 0.265 | 0.812 | +54.7 | 185 / 0 / 3 |
| 70-80 | 127 | 0.298 | 0.818 | +52.0 | 125 / 0 / 2 |
| 80-90 | 59 | 0.261 | 0.833 | +57.1 | 59 / 0 / 0 |
| 90-100 | 9 | 0.231 | 0.842 | +61.1 | 9 / 0 / 0 |
| **All** | **5,264** | **0.356** | **0.756** | **+40.01** | **4,640 / 0 / 624** |

- The original tests get weaker as models get harder; the super suite gets
  stronger. The lift doubles from the easiest to the hardest bucket.
- **Timeout kills:** 54 (super suite) and 44 (baseline) out of 190,966
  mutants each. Counting all of them as survived gives +40.00 points.
- **Unchanged models** are mostly small models with nothing for the new
  generators to add (126 of 363 in the easiest bucket).
- The sample showed +43.03 points. It over-represents logic-heavy models,
  which gain more. **Report the full-dataset number.**

Reports: `reports/full_mutation_comparison.*`,
`reports/super_suite_relaxed_check.*`. Detail: DECISIONS 2026-10-20 and
2026-10-21, `docs/2026-10-11-explainer-test-generation-comparison.md`.

## 9. The hand-over to the benchmarking side

- **Export** (`export_benchmark_dataset.py`, driven by
  `benchmark_export.toml`). It writes `train/<model>/` and `test/<model>/`
  with `model.puml`, `model_buml.py`, `python_code.py`,
  `test_super_suite.py`, `code_structure.json` (tree-sitter structure of the
  reference), `model_metadata.json` and `test_suite_quality.json` (the two
  mutation results). It also writes `manifest.json`, a README,
  `train.txt`/`test.txt` and a copy of the config. Adding or removing a file,
  a JSON key, a manifest field or a shared script is a config change, not a
  code change. The export refuses to write inside the dataset or over a
  non-empty folder. Tested on the 200 sample.
- **Split** (`make_benchmark_split.py`). Stratified by bucket, seed 42, at
  least one test model per bucket (test = max(round(n·(1−ratio)), 1)). The
  ratio is not chosen yet; per-bucket train/test counts for 90/10 … 50/50
  are in `docs/split-ratio-options.md` and the handout.
- **What generated code must look like.** The suite tests the reference
  generator's API, so the code agent must produce the same shape:
  - same class names; enumerations as `Enum` subclasses
  - every class instantiable (no `@abstractmethod`, even for abstract classes)
  - attributes as required constructor keywords, association ends as
    optional ones, many-valued ends as sets
  - a `@property` with a setter for everything
  - association setters that keep both ends consistent
  - operations that don't raise

  Run with Python 3.11, pytest 9.1.1, hypothesis 6.167.1,
  `--hypothesis-seed=0`. Score a model by its pass rate, since suite sizes
  vary widely: median 90 tests, P90 481, maximum 4,137
  (`reports/test_count_distribution.md`).
- **Pilot sample** (`select_pilot_sample.py` → `reports/pilot_sample.txt`,
  shipped as `pilot.txt`). 100 models, 10 per bucket (all 9 of 90-100, 11
  of 80-90), avoiding the 200 test-generation sample where possible (3
  overlap, all in 90-100). They
  let the benchmarking side try the whole pipeline before a full run. They
  overlap train and test on purpose.
- **The seed is per test, not one shared stream.** Checked in the
  Hypothesis source (`core.py`, `get_random_for_wrapped_test`): with
  `--hypothesis-seed`, every `@given` test gets a fresh `Random(seed)`, and
  the example database is switched off. Running tests or models in another
  order therefore gives the same examples. What can still change them: the
  test's strategies (`st.builds(Class)` reads the generated class's type
  hints), the Hypothesis version, and a 200 ms per-example deadline under
  heavy load. So the runs on original and shrunk code see identical inputs.
  **Open:** one missing class fails the whole suite at import. Full answer:
  `docs/2026-10-28-hypothesis-seed-and-comparable-test-runs.md`.
- **Open with them:** `docs/handout.md` section 7 (ratio, a reference
  runner, whether to ship `python_code.py`, where the export lives, more
  data, the PUML parser).

## 10. Defects found in the source dataset

For anyone using or maintaining the BESSER dataset:
- **No operation is implemented** (19,768 stubs), and the dataset's own
  tests fail on the stubs.
- **Many generated classes are bare stubs** even when the model declares
  them in associations, so one side of a bidirectional link is never
  maintained.
- **Abstract is not implemented consistently.** Some abstract classes derive
  from `ABC`, others are plain classes. No abstract methods were found
  (0 of 732 sampled methods), so every class can be instantiated.
- **Overloaded operations collapse to one.** They are written as two
  assignments to one variable, so only the last survives. Variable names
  are also reused across elements.
- **Names that clash with Python** (`property`, `self`) are renamed
  inconsistently. One `Factura` became `Facturas`. One attribute (`Fecha`,
  `model_10001897`) is missing from the code. One class is split in two
  (`model_10001985`).
- **Phantom properties:** in 2 models a setter has the wrong name.
- **Invalid generated tests:** 27 suites don't collect.
- **besser's `PythonGenerator`** emits invalid parameter order for 2 models;
  its `TestCaseGenerator` is broken in the pip release.
- **Copies:** 37% of usable models; labels (`category.txt`, README titles)
  differ between copies of one model.
- **7 BUML source bugs** that blocked conversion (fixed in the BUML).
- **1,732 string literals in 222 models** sit in definitions that never reach
  the model.

## 11. Lessons on method

- **Check the instrument before trusting the number.** Three of the
  project's largest corrections were measurement bugs, not data: fake kills
  from failing suites, a seeded sample that wasn't reproducible, and a cache
  that reused another test file's results. A one-line check (does the suite
  pass unmutated? does the same seed give the same mutants?) would have
  caught each.
- **Verify on every shape, not one example.** The stub-double rule was
  checked on one model whose links all happened to be single-valued; it was
  wrong for collections. The PUML was believed complete until a third gap
  appeared, after which it was proved complete on all 9,082 models.
- **Compare like with like.** Tool scores on their own subsets looked better
  than they were; each was re-compared with the baseline on the same models.
- **Count across models, not only within.** Every validator looked at one
  model at a time, which is why 37% copies went unnoticed for weeks.
- **Windows specifics:**
  - Read text as UTF-8 and sniff the BOM: PowerShell writes UTF-16 or
    UTF-8-with-BOM.
  - Call tools as `python -m tool`. Renaming a venv silently breaks its
    `.exe` wrappers.
  - Never install test tools into the measurement venv. One install
    downgraded pytest.

## 12. Numbers that were superseded

| Old figure | Where it appeared | Current | Why it changed |
|---|---|---|---|
| Super suite 92.66%, baseline 50.85% (+41.81) | 2026-10-12 presentation, early explainer | 77.55% / 34.52% (+43.03) on the sample; **75.61% / 35.60% (+40.01)** on all 5,264 | Suites failing unmutated; then the full run |
| Super suite 77.59%, CrossHair 64.24%, behavioral 59.89%, Pynguin 27.75% | test-generation comparison | not remeasured | Same unguarded measurement; only the qualitative ranking stands |
| September full-dataset mutation averages (~40-44%) | coverage/mutation reports | superseded by the green, guarded full run | Unguarded, unseeded, copy-weighted, non-reproducible sampling |
| PCA fits on 9,082 / 8,451 / 8,336 models (Spearman 0.894 / 0.879 / 0.874) | `reports/difficulty_score_report.md`, presentation | **0.9165** on 5,264 | Copies weighted the fit; PC2's apparent cost in agreement came from the copies |
| Difficulty distribution (mean 33.0, 0-10 bucket 156 models) | presentation, distribution report | buckets as in section 6 | Refit on the unique set |
| ~940 models with failing empty-method checks | DECISIONS 2026-10-18 | **650** (super suite) / 649 (baseline) | Counted with copies |
| 992 models with no logic-bearing method, 640,217 methods classified | method-logic classification | **439** models (8.34%); **427,336** methods (2.24% no_logic, 71.73% trivial, 26.03% has_logic) | Counted with copies (8,336); recount on the 5,264 (`reports/method_logic_summary.md`) |
| 19,768 stub operations in 1,037 models | zero-operations explainer | **8,878** operations in **699** models, all stubs | Counted on all 9,082 with copies; same recount |
| 4 CrossHair syntax-error models | 2026-10-11 | handled by the sanitizer; 110 invalid outputs skipped in the full run | Full run |

## 13. Where to find things

**Docs** (`docs/`):

| File | What |
|---|---|
| `DECISIONS.md` | the running log, newest first; the source for everything here |
| `handout.md` | for the benchmarking side: export, PUML format, how to run the suite, open questions |
| `RUNBOOK-full-regeneration.md` | the full pipeline in order, with commands and costs |
| `split-ratio-options.md` | train/test per bucket for each ratio |
| `2026-09-10-*` | exclusions, PUML conversion, zero operations, structural tests, coverage taxonomy, mutation scope |
| `2026-09-16-*` | the combined suite; tree-sitter fidelity and class coverage |
| `2026-09-28-explainer-*` | the PCA score, empty models and mutation score, tree-sitter vs model |
| `2026-10-11-explainer-test-generation-comparison.md` | the generator comparison and the false positive |
| `2026-10-12-presentation-*` | questions on the difficulty score and mutation work (pre-dedup numbers) |
| `2026-10-28-hypothesis-seed-and-comparable-test-runs.md` | why seeded runs on original and shrunk code see identical inputs; the import risk |

**Scripts** (`scripts/`, shared helpers in `scripts/_common/`):

| Step | Scripts |
|---|---|
| Validate the source | `validate_python_code.py`, `validate_tests.py`, `validate_logic.py`, `check_property_name_mismatches.py`, `classify_method_logic.py` |
| Diagram and identity | `buml_to_puml.py`, `verify_puml_conversion.py`, `selftest_conversion_checks.py`, `select_unique_models.py` |
| Metadata and difficulty | `generate_model_metadata.py`, `generate_code_structure.py` / `extract_structure.py` (tree-sitter), `compute_difficulty_score.py`, `compute_article_difficulty_score.py`, `compare_difficulty_scores.py`, `difficulty_score_distribution.py`, `experiment_difficulty_score_pca.py` |
| Fidelity of the generated code | `validate_generator_fidelity.py`, `validate_generator_fidelity_names.py` |
| Tests | `generate_structural_tests.py`, `generate_combined_tests.py`, `generate_behavioral_tests.py`, `generate_crosshair_tests.py`, `generate_pynguin_tests.py`, `generate_super_suite.py`, `make_green_suite.py` |
| Measurement | `validate_coverage*.py`, `validate_class_coverage.py`, `validate_mutation.py`, `validate_mutation_properties.py`, `mutation_export.py`, `compare_mutation_runs.py`, `select_test_generation_sample.py`, `test_count_distribution.py`, `summarize_method_logic.py` |
| Benchmark | `make_benchmark_split.py`, `select_pilot_sample.py`, `export_benchmark_dataset.py` (+ `benchmark_export.toml`), `check_pipeline_status.py` |

**Key lists and reports** (`reports/`): `unique_models.txt` (the 5,264),
`usable_models.txt` (the 8,336), `excluded_models_master.*`,
`unique_models_report.*`, `full_*` (the final regeneration),
`difficulty_score_pca_experiment_report.*`,
`conversion_checks_selftest.*`.

**Environments:**
- `.venv`: Python 3.11.9, pytest 9.1.1, hypothesis 6.167.1, cosmic-ray.
  Measurement and most scripts.
- `.venv-puml`: besser. Anything that loads BUML.
- `.venv-testgen`: CrossHair and Pynguin.
- `.venv-treesitter`: not present on this machine. Only needed if
  `code_structure.json` is regenerated.
