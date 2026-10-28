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

## 2026-10-28 — Seeded runs feed identical inputs to original and shrunk code; one missing class fails a whole suite

**Question.** Does the benchmark's run on code from the shrunk diagram see
the same Hypothesis inputs as the run on code from the original diagram?

**Answer: yes**, given the same test file, Python, Hypothesis version and
constructor signatures. Checked in the Hypothesis 6.167.1 source and in all
5,264 suites:
- `--hypothesis-seed` gives every test its own fresh `Random(seed)` and
  turns the example database off, so the order of tests, models and runs
  doesn't matter.
- No suite uses `assume`, `target` or `st.data`, so the code under test
  can't steer the draws.
- The only way generated code changes the inputs is an extra required
  constructor parameter that `st.builds(Class)` then fills from its type
  hint. That code already breaks the API.

**Open.** Every suite imports all model names at module level, so one
missing class fails collection of the whole suite (0 tests run). This
matters if shrinking can drop diagram elements. It was asked of the
benchmarking side; the fix is per-test name lookup in our generator, or
reporting collection errors separately in their runner.

Full write-up: `docs/2026-10-28-hypothesis-seed-and-comparable-test-runs.md`.

**Also this day.**
- Pilot sample (`select_pilot_sample.py`): 100 models, 10 per bucket (all 9
  of 90-100, 11 of 80-90). 3 of them are from the 200-model
  test-generation sample, all in 90-100, which has nothing else.
- Recount on the 5,264 unique models (`summarize_method_logic.py`):
  - 439 models (8.34%) have no logic-bearing method (992 on the 8,336
    with copies).
  - 427,336 methods: 2.24% no_logic, 71.73% trivial, 26.03% has_logic.
  - 8,878 operations in 699 models, every one a stub (19,768 in 1,037 on
    all 9,082).

---

## 2026-10-21 — CrossHair assertions on stub operations rewritten to bare calls; mutation scores unchanged

**Finding** (while writing the benchmarking handout). CrossHair records what an operation returned and asserts it: `assert javaMM_InfixExpression.operatorIsEquality(...) == None`. No BUML model specifies an operation body, so every operation in `python_code.py` is an empty stub (`# TODO: Implement` + `pass`), while the PUML declares `+ operatorIsEquality() : str`. These assertions therefore test the stub, not the diagram: code generated from the PUML that implements the operation as declared would fail them, for both the original and the shrunk diagram. That is noise in exactly the comparison the benchmark makes. Scale: **3,371 tests in 407 of the 5,264 models.** Nothing else in the suite tests operations.

Also checked and harmless: CrossHair passes constructor arguments positionally, while the reference's parameter order comes from BUML's unordered sets. Those tests only assert `__init__(...) == None`, which holds in any order (the setters don't check types); only the parameter count matters.

**Decision.** `_common/crosshair.py` rewrites an assertion on a call of a non-dunder attribute (`==` / `is` anything) to the bare call. The test still fails if the operation is missing or takes different arguments, or if its body raises, but no longer asserts a return value. `__init__(...) == None` checks stay. The rewrite runs when the super suite reads `test_crosshair.py`, so CrossHair was not rerun. Idempotent; checked on `model_10010` (exactly its 2 operation tests relaxed).

**Rerun.**
- `generate_super_suite.py --fresh`: 3,371 assertions relaxed in 407 models; 5,264/5,264 green after the 7 very large models were retried with `--timeout 1200`. Same 1,023,139 tests and 6,250 removed tests as before. `git diff` showed exactly those 407 suites changed.
- Mutation for the 407 models (`full_super_suite_mutation_relaxed`, same settings) compared with the full run (`compare_mutation_runs.py` → `reports/super_suite_relaxed_check.*`): **407 unchanged, 0 improved, 0 worse**, mean 0.8064 both times, same mutants per model. As expected, since the mutation run only mutates properties, never operation bodies. The full-dataset numbers of the entry below stand unchanged.

---

## 2026-10-20 — Full regeneration on the 5,264 unique models: super suite 75.61% vs green baseline 35.60% (+40.01 pts), no model worse

**What was run** (`docs/RUNBOOK-full-regeneration.md`, every model in `reports/unique_models.txt`):
- Behavioral tests regenerated with the fixed generator: 5,264/5,264, 66,543 tests.
- CrossHair for the 5,064 models outside the 200 sample (same settings as the sample: 30 s per class, 5 s per condition, 300 s per model). 4,106 got tests, 958 none (classes with only properties), 0 errors. The sample models kept the CrossHair files their published results were measured with.
- Super suite and green baseline: **5,264/5,264 green** each (super suite 1,023,139 tests, baseline 931,579). The first pass timed out on 8 / 7 very large models because both jobs ran at once; a retry with `--timeout 1200` made them green. The rebuilt suites of the two affected sample models (`model_713`, `model_3260`) are byte-identical to the committed ones. Removed tests: 6,250 in 650 models (super suite) and 6,210 in 649 (baseline), almost all the dataset's own empty-method checks. Dataset-wide this concerns **~650 unique models**, not the "~940" counted with copies. 12 behavioral stub-double tests were also removed (`'Property' object is not callable`).
- Mutation testing, both suites: `validate_mutation_properties.py`, 40 mutants per model, `--hypothesis-seed 0`, baseline guard on, `--workers 24 --overall-timeout 3600`, per-mutant timeout 90 s (default). 5,264/5,264 measured in both, 0 `baseline_failed`, the same 190,966 mutants run (same count per model in both runs).

**Result** (`scripts/compare_mutation_runs.py` → `reports/full_mutation_comparison.*`):

| | Baseline (`test_combined_green`) | Super suite |
|---|---:|---:|
| Mean property mutation score | **35.60%** | **75.61%** |
| Perfect scores | 8 | 21 |
| Zero scores | 2 | 0 |

**Lift +40.01 pts. Per model: 4,640 improved, 0 worse, 624 unchanged.** On the 200-model sample it was +43.03 pts (188 / 0 / 12); the sample over-represents logic-heavy models, which gain more (see below).

By difficulty bucket (refit PC1+PC2 score):

| Bucket | Models | Baseline | Super suite | Lift (pts) | Improved / worse / unchanged |
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

- The original suites get weaker as models get harder (baseline 0.39 → 0.23), while the super suite gets stronger (0.70 → 0.84). The lift therefore grows with difficulty, from +30 to +61 pts. This is also independent evidence that the difficulty score tracks something real: the dataset's own tests cover hard models worst.
- Unchanged models are concentrated in the easy buckets (126 of 363 in 0-10): small models with few or no bidirectional associations and nothing for CrossHair, where the baseline already kills what the super suite kills.

**Timeout kills.** cosmic-ray counts a mutant whose test run exceeds the per-mutant timeout as KILLED (`cosmic_ray/testing.py`); `validate_mutation_properties.py` now counts these separately (`killed_by_timeout`). Baseline 44 in 35 models, super suite 54 in 39, out of 190,966 mutants each. Counting every one of them as survived gives baseline 0.3558, super suite 0.7558, **lift +40.00 pts**, so they don't affect the result. They also sit in the same models with mostly the same counts in both runs (e.g. `model_10000238` 3 / 3, `model_100209` 3 / 3), which fits mutants that really hang (the same mutants are selected in both runs) more than random load. Decided not to rerun them in isolation.

**For the article.** Report the full-dataset numbers (5,264 unique models), not the sample's: 35.60% → 75.61%, +40.01 pts, no model worse, lift rising with difficulty. Mention the worst case with timeout kills counted as survived (+40.00 pts) and that every suite was pruned to tests passing on the original code before measuring (the baseline guard, 0 `baseline_failed`).

---

## 2026-10-18 — Only exact copies are removed; similar models stay

**Question.** Should near-duplicates, such as forks of one metamodel with an extra attribute or a renamed class, also be removed or kept on one side of the train/test split?

**Decision: no.** A model that differs from another in anything the BUML specifies is a different model: a different diagram, different generated code, and a different task for the benchmark. Any similarity threshold would be our arbitrary choice, while "identical apart from set/statement order, comments and the random model name" is a property of the original dataset that anyone can check (`select_unique_models.py`, confirmed by the PUML and the besser-built grouping). The dedup stays at exact copies only: 5,264 models.

**For the article.** If asked about train/test leakage from similar models: the split is stratified by difficulty, exact copies are removed, and similar-but-different models are treated as distinct tasks on purpose.

---

## 2026-10-18 — PUML conversion made lossless, with proof over every model

**Why.** Role names (entry below) were the second piece of information found missing from our PUML by accident; OCL constraints were the third. Finding gaps one example at a time, and claiming "the rest is fine" from a few models, is not defensible: the benchmark's whole comparison runs on the PUML. So the conversion is now complete by construction and verified on all 9,082 models.

**Inventory** (every BUML file in `Dataset/`, all 9,082 parse). Everything the source dataset specifies:
- `Class(name, is_abstract)`
- `Property(name, type, multiplicity, is_composite, is_navigable)` (`is_navigable=False`: 6 ends in 1 model)
- `Method(name, parameters, type)`, `Parameter(name, type)`
- `Enumeration(name, literals)`, `EnumerationLiteral(name)`
- `Generalization(general, specific)`, `BinaryAssociation(name, ends)`
- `Constraint(name, context, expression, language)` (418 in 31 models)
- `DomainModel(name, types, associations, generalizations, constraints, metadata)`
- `Project(name, owner, metadata, models)`, `Metadata(description)`, `Multiplicity(min, max)`
- property assignments `.attributes` / `.methods`

Never used anywhere: visibility, aggregation, `AssociationClass` instances, attribute multiplicities.

**Previously missing from the PUML:**
- OCL constraints
- the model name
- project name, owner and description
- role names (fixed just before)
- navigability, which was only expressible through `<--`/`-->` and not combinable with composition
- composition on both ends of one association

**Now** (`buml_to_puml.py`):
- header comments `' model:` / `' project:` / `' owner:` / `' description:`
- constraints as `note top of <Context>` with `constraint <name> (<language>): <expression>`
- composition as a diamond on either or both sides (`*--`, `--*`, `*--*`)
- `{not navigable}` in the label of a non-navigable end
- free text kept on one line with reversible escaping

**Proof** (`scripts/verify_puml_conversion.py`), three independent checks per model:
1. *Coverage:* every constructor, keyword and property assignment in the BUML source is one the converter handles. A new construct is reported as `unsupported`, never dropped silently.
2. *Round trip:* the model is loaded with besser, the PUML is parsed back, and the two fact multisets must be equal. Every missing or extra fact is listed, and an unrecognized PUML line counts as a mismatch.
3. *Source text:* every string literal given to a BUML constructor in the original file must appear in the PUML. This doesn't go through besser, so a field dropped on load can't hide on both sides of check 2.

**Results.**
- First verifier run: 14/9,082 lossless. Both causes were in the verifier, not the conversion:
  - besser adds its 9 built-in primitive types to every model's types by itself, and the verifier counted them as model content;
  - parameter names from overwritten overloaded-method definitions were demanded although they never reach the model. They are now computed exactly (`_common.buml.dead_statements`) and reported separately.
- After fixing both: **9,082/9,082 lossless**, no unsupported construct. Separately reported source-data defect: 1,732 string literals in 222 models sit in definitions that never reach the model.
- The 6 non-navigable ends (all in `Model_1000000002`) appear one-to-one as `{not navigable}`.

**Can the checks fail?** `scripts/selftest_conversion_checks.py` mutation-tests both checks. It applies about 20 kinds of real BUML change, which must change the fingerprint, and 4 kinds of noise, which must not. besser confirms each case really changed, or didn't change, the model. It applies 16 kinds of PUML corruption, which the verifier must report, and the unmodified PUML must pass. It also groups every usable model a second time by the besser-built model.

First run (300 random models): fingerprint fooled 0×, verifier fooled 0×, 0 false alarms, both groupings identical (5,264 = 5,264). But it had two gaps of its own:
- the navigability mutation added the default value, a no-op reported as 275 `bad_test_case`;
- no sampled model had an OCL constraint, so that path was never exercised.

Fixed: flags absent from the source now get their non-default value; every model using a rare construct (OCL constraints, explicit navigability) is always added to the sample; and the verdict now fails if any operation was never exercised or any test case was bad.

**Final self-test (300 random + 32 rare-construct models, seed 42): PASS.** Every one of the 24 BUML operations and 17 PUML corruptions was exercised; 0 fooled, 0 false alarms, 0 bad test cases; both groupings give 5,264.
- Real BUML changes, each detected every time it applied (count = models where it applied): attribute type 330, multiplicity 302, OCL expression 31, description / project name / owner 332 each, abstract 332, composite 251, navigability 302, removed association 296 / attribute 331 / generalization 167 / type 327, and renamed association 302, attribute or role 332, class 332, enum literal 84, enumeration 112, method 46, parameter 34.
- Noise left the fingerprint unchanged every time: random model name 332, reformat 332, statement reorder 332, set shuffle 329.
- PUML corruptions, each reported every time: bogus class 332, attribute type 331, model name 332, multiplicity 302, parameter 34, role name 302, deleted association 302 / attribute 331 / constraint 31 / enum literal 84 / generalization 175 / method 46 / project header 332, abstract 332, composition 302. Dropping `{not navigable}` was tested once, because only one model has it. The unmodified PUML passed in all 332 models.
- Not counted either way: 51 composite flips and 1 type change made the model invalid, so besser refused to load it.

Report: `reports/conversion_checks_selftest.*`.

---

## 2026-10-18 — PUML association ends now carry role names

`buml_to_puml.py` wrote association ends with multiplicities only (`Account "1..1" -- "0..9999" Order : Account_Order`). The role names, which become the attribute names in the generated code, were missing. Every test of an association uses those names: in `model_10000179`, `cards0`, `hand1`, `hand2` and `hand3` appear 8-16 times each in `test_super_suite.py` and nowhere in the `.puml`. Code generated from that PUML alone could never pass the association tests, whatever its quality, so the benchmark's comparison (original vs. shrunk PUML) would have been broken from the start.
- Each end now reads `"role min..max"`, placed next to the class the end refers to (standard UML): `Hand "cards0 0..9999" -- "hand1 1..1" Card`.
- Method parameters stay sorted by name: in BUML they are a set (`parameters={...}`), so no "real" order exists.
- **This changes the input format the benchmarking repo's PUML shrinker parses**; agreed to change it, to be communicated to the benchmarking side.
- All `.puml` files have to be regenerated.

---

## 2026-10-18 — 37% of the usable models are copies of another model; the pipeline now runs on one model per distinct BUML model

**Finding.** Building the benchmark split showed that the 8,336 usable models hold only **5,235 distinct diagrams**. 4,120 models fall into 1,019 groups with byte-identical `.puml` files.
- 736 of the groups are pairs.
- The model_100000xx-model_10003xxx batch has five groups of 158-200 copies each.
- Checked on the 200-copy "shopping" group: the diagram is identical. The `python_code.py` files (all 200 distinct) and the text descriptions differ only in the order of constructor parameters and listed classes. It is the same model ingested repeatedly, with generator ordering noise, not 200 variants.

**Why it matters.** A copy is the same benchmark task again:
- It multiplies LLM cost and regeneration cost (CrossHair, mutation testing).
- It weights one diagram many times in every dataset-wide average and in the PCA fit, so the loadings lean toward heavily copied diagrams.
- It could leak between train and test if the split ignored it.

Earlier dataset-wide numbers (September coverage/mutation averages, the PCA fits on 9,082 / 8,451 / 8,336 models) were all weighted this way.

**Why it wasn't caught sooner.**
- Every validator in this repo works on one model at a time; none compares models with each other.
- Exact duplicates *were* found on 2026-09-29, by method-count signature, when picking the 200-model sample. They were only removed from that sample and never quantified dataset-wide.
- Code-level hashes would miss them, because the copies' code differs in ordering. Only the sorted `.puml` exposes them, and the PUML became the benchmark's input only with the benchmark design.
- A visible hint was missed: model_3262/3263/3264 had the exact same unclamped difficulty score (105.7679720079053) in the 2026-10-12 clamping experiment.

**Verified on the original BUML, not just our PUML** (all 8,336 usable models):
- Raw BUML bytes show 8,203 "distinct" models, because copies of one model differ in exactly three meaningless ways:
  1. the order of items inside set literals (`Payment.attributes={...}`; Python prints sets in arbitrary order)
  2. statement order and comments
  3. the DomainModel's own `name=`, a fresh random ID per copy (a UUID in 1,216 models, Eclipse-style IDs such as `__gcXQO9YEem…` in others)
- Ignoring only those three, the BUML gives **5,258 distinct models**; the PUML gave 5,235.
- The 23-model gap is 20 PUML groups whose copies differ only in association role names (`owner3` vs `advertiser3`, `aTM0` vs `ATM0`): exactly the information our PUML was dropping (see the PUML entry below).

Where the copies are:

| | Models | Distinct | Copies |
|---|---:|---:|---:|
| `model_1000xxxx` batch | 2,871 | 1,136 | 60% |
| everything else | 5,465 | 4,122 | 25% |

**Where the copies come from, and what differs between them** (every file in every one of the 1,018 groups; `_scratch/analyze_duplicate_groups.py`):
- **Provenance.** 5,990 of the 5,993 models outside the `model_1000xxxx` batch have a `model_path.txt` into ModelSet's raw data (`/modelset/raw-data/repo-ecore-all/data/<github-user>/<repo>/...`). They are Ecore metamodels scraped from GitHub, and the same metamodel file sits in many repositories (e.g. `java.ecore` in `atlanmod/Prefetching_Caching_DSL` and in `martin-fleck/momot`; `Ecore.ecore` vs a `Copy.ecore`). `model_path.txt` differs in 841 groups: same model, different source file. The `model_1000xxxx` batch (3,089 models) has no `model_path.txt`, so its origin is undocumented; its random-UUID / Eclipse IDs fit models saved by many users of one modelling tool.
- **`python_code.py`**: identical in 31 groups and identical up to ordering in 983, i.e. 1,014 of 1,018. Ordering here means the order of classes, methods, statements and constructor parameters.
  - The other 4 groups differ for a real reason: name-clash handling in the source dataset's code generator depends on set order. An attribute `property` (clashing with Python's built-in) became `property1` in one copy and stayed `property` in another (`model_100066/100067`, `model_10001303/10002909`, `model_100086/100089`, `model_100087/100090`).
  - This belongs to the code-vs-BUML name mismatches `validate_generator_fidelity_names.py` measures. The representative keeps one valid variant.
- **BUML**: identical up to the three noise kinds above (set order, statement order, the random model name), consistent with the fingerprint.
- **Generated artifacts differ only by ordering**, as far as inspected (examples checked; the analysis normalizer doesn't cover every case): `test_hypothesis.py` (keyword order in `st.builds(...)`, import order), the Java code, `textualDescription.txt` (class/role order) and the rendered `image.gv.png`.
- **Labels are inconsistent between copies**: `category.txt` differs in 165 groups (`shopping` vs `store`, `database/sql` vs `petrinet`), and the `README.md` title in 314, taken from the source file name (`Java` vs `Java-cdo`, `Ecore` vs `Copy`). `metadata.txt` is identical; its 3 apparent differences are masking artifacts.

**Decision.** New `scripts/select_unique_models.py` writes `reports/unique_models.txt`: one model per distinct **original BUML model**.
- Copies are identified by `_common.buml.buml_fingerprint`: the BUML is parsed as Python, ignoring only the three differences above. Everything else (classes, attributes, methods, enumerations, generalizations, associations, role names, multiplicities) must match.
- The grouping rests on the original dataset, so it holds even for someone who distrusts our PUML generation.
- The PUML grouping is reported alongside as a cross-check (step 2 of the script).

**First real run, and two fixes it caused.** On the regenerated PUML (role names included), step 1 gave 5,258 unique models, but step 2 still disagreed in 7 places:
- *2 PUML groups spanning several BUML models:* the copies differ in **OCL constraints** (e.g. `model_10010` has `Constraint(...)` statements that `model_91` lacks). The PUML has no constraints, so the BUML is right to keep both. This is accepted: the generated code and tests don't use OCL.
- *5 BUML groups with differing PUML:* my fingerprint was wrong. The source dataset defines **overloaded methods by assigning the same variable twice** (`..._m_deltaMinusOne` in `model_100438`/`model_1380`), and only the definition last assigned before `X.methods = {...}` reaches the model. Sorting statements hid which one that is, so two genuinely different models were merged.
  - First fix: keep statement order for files that assign a variable twice. The next run showed this was too conservative: 239 such files, and 36 PUML groups whose copies were left unmerged only because their statements were in a different order.
  - Final fix (`_common.buml.buml_fingerprint`):
    - drop statements that never reach the model (`dead_statements`, computed from which statement reads which binding)
    - rename every binding after its own content (`name@<hash of its value>`) and rewrite every read to the binding it resolves to; the source also reuses one name for an attribute and an association (`FoodItem_Food` in `model_10000436`)
    - sort the statements

    Order is kept only if one property (`X.attributes`) is still assigned twice. Checked on the flagged groups: they now merge, the 200-copy shopping group still merges, and the genuinely different `model_100438`/`model_1380` stay apart.
  - This is also a defect in the source dataset: overloaded operations silently collapse to one, and variable names are reused across elements.
- *Robustness:* `buml_to_puml.py` sorted attributes, methods and associations by name only. Members sharing a name (seen: two `+ defaultValue : str` in one class) would have been ordered by set order. They now sort by (name, full line), which changes nothing where names are unique.

**Final result:** **8,336 usable models → 5,264 unique** (3,072 copies in 1,018 groups, statement order needed for 0 files).
- Step 2: the lossless PUML gives the same 5,264, and the two groupings agree model for model.
- The OCL groups resolved once constraints were added to the PUML.
- A third, independent grouping by the besser-built model (`selftest_conversion_checks.py`) also gives exactly the same 5,264 groups.
- `reports/unique_models.txt` is the list every later step uses.
- The representative is the alphabetically first name, the same rule as `select_test_generation_sample.py`. Every group is listed in `reports/unique_models_report.*`. This list **replaces `usable_models.txt` for every later step**:
- the full regeneration
- `compute_difficulty_score.py` and its proof (`experiment_difficulty_score_pca.py`)
- the comparison and distribution scripts
- the split and the export

**The 200-model test-generation sample is unaffected** (`_scratch/check_sample_vs_unique.py`): all 200 are representatives in `unique_models.txt`, and no two belong to the same group. The 2026-09-29 count-signature dedup used for the sample was stricter than this one, so the +43.03-point result stands on the unique set as published.

This supersedes "pass `reports/usable_models.txt`" in the PCA entry below. `make_benchmark_split.py` defaults to the unique list and keeps its own PUML grouping as a safety net (expected to find 0 groups). The PCA numbers in the entry below were computed on the 8,336 usable models and will move slightly when refit on the unique set during the rerun. The PC1+PC2 argument has to be rechecked then (experiment 6).

---

## 2026-10-18 — PCA evidence completed; PC1+PC2 kept although Kaiser and parallel analysis retain 3 components

**Why.** We need to defend two things to colleagues: how the PCA score compares to the article's formula, and why only PC1+PC2 are used. The second rested on (a) "variance drops off fast" and (b) "PC2 was checked on real models (`diagnose_pc2_extremes.py`), PC3 never was". Neither standard component-retention tests nor a PC3 check had ever been run, and the evidence came from three different model sets (official fit 9,082, experiment 8,451, planned buckets 8,336).

**What changed.** `experiment_difficulty_score_pca.py` is now the single evidence script. It adds component retention (Kaiser, broken stick, Horn's parallel analysis: 100 random-normal runs of identical shape, seed 42, 95th percentile) and the extremes check for PC2 *and* PC3 (top/bottom 10, plus 5% tails), keeps the component sweep, clamping and exclusion experiments, and writes a Markdown report next to the JSON. `compute_difficulty_score.py`, `compare_difficulty_scores.py`, `difficulty_score_distribution.py` and the experiment all take `--models-file`; the rerun passes `reports/usable_models.txt` to all of them, so the fit, the scores, the proof and the buckets describe the same 8,336 models. Run on the old default set (8,451) the script reproduces the previous report's numbers exactly.

**Findings** (8,336 usable models; 8,451 in brackets):

| | PC1 | PC2 | PC3 | PC4 |
|---|---:|---:|---:|---:|
| Eigenvalue | 5.13 (5.27) | 1.71 (1.67) | 1.12 (1.09) | 0.85 (0.81) |
| Variance | 46.7% | 15.5% | 10.2% | 7.7% |
| Random-data 95th pct (parallel analysis) | 1.07 | 1.05 | 1.04 | 1.03 |
| Spearman vs article, PC1..PCk | 0.893 | 0.874 | 0.861 | 0.858 |

- Retained: **Kaiser 3, parallel analysis 3, broken stick 1.** No standard rule picks 2.
- Extremes check, mean PC1 (overall 0): PC2 top/bottom 10 = +0.92 / +0.66, but 5% tails = −0.38 / +0.50. PC3 top/bottom 10 = +5.74 / +3.87, 5% tails = +2.82 / +2.57.
- PC2's positive tail is average-sized, attribute-rich flat models (≈12 classes, 30 attributes, 8 attribute types, no inheritance). Its negative tail is big hierarchies (≈74 classes, 66 generalizations). PC3 contrasts enumeration-heavy large models (≈6.6 enums, 36 literals) with association/method-heavy ones (≈31 associations, 17 methods, no enums).
- Caveat on the extremes check: components driven by fields that are zero for most small models (enums, methods) can only reach their extremes in large models, so passing it is necessary but not sufficient evidence of a "real" axis.

**Consequence.** The written justification "PC3 was never verified" no longer applies, and "the numbers drop off fast" is answered by the formal tests: they say 3. Article agreement falls slightly with every added component (PC2 included), for the reason already given in the explainer: the article measures size only. Three options were weighed: PC1+PC2 (current), PC1+PC2+PC3 (what Kaiser and parallel analysis support), PC1 alone (broken stick; best article agreement; size only). The choice was made on what PC3 actually does to the score, measured below (`experiment_difficulty_score_pca.py`, experiment 6).

**What adding PC3 would actually do** (same fit, 8,336 usable models, PC1+PC2 vs. PC1+PC2+PC3, both clipped and variance-weighted; point budgets 75.0/25.0 vs. 64.5/21.4/14.1):
- Ranking almost unchanged: Spearman between the two scores **0.986**. Median |change| 1.8 points, 90th percentile 5.5, extremes +10.7 / −11.9.
- 25.0% of models change difficulty bucket, all by exactly one bucket. These are mostly models sitting near a bucket boundary.
- The models that rise most are **small and enumeration-heavy** (e.g. `model_4314`: 5 classes, 4 enums, 0 methods, +10.7). The models that fall most are **the largest ones** (271-341 classes, about −12), because PC1's share of the points shrinks from 75 to 64.5. The 80-90 bucket thins from 69 to 26 models.
- Models with methods change the same as models without (−0.95 vs. −1.01). PC3 does **not** in practice raise the weight of methods, despite its +0.30 loading.

**Decision: keep PC1+PC2.** PC3 passes the statistical retention tests, but in practice it changes the score in the wrong direction for a code-generation difficulty measure. It mostly rewards enum count in small models and pulls down the largest models, and it does not give methods more weight.

**Refit on the 5,264 unique models (the final numbers; use these in the article).** The fit above counted copied models many times. Refit with `--models-file reports/unique_models.txt` (`reports/difficulty_score_pca_experiment_report.*`):

| | PC1 | PC2 | PC3 | PC4 |
|---|---:|---:|---:|---:|
| Eigenvalue | 5.36 | 1.50 | 1.13 | 0.89 |
| Variance | 48.8% | 13.7% | 10.2% | 8.1% |
| Random-data 95th pct (parallel analysis) | 1.09 | 1.07 | 1.05 | 1.04 |
| Spearman vs article, PC1..PCk | 0.9164 | 0.9165 | 0.9036 | 0.9030 |

- Retained: unchanged, **Kaiser 3, parallel analysis 3, broken stick 1.** PC1+PC2 explain 62.4%; point budgets 78.1 / 21.9.
- Extremes, mean PC1: PC2 top/bottom 10 = +0.71 / +1.04, 5% tails = −0.38 / +1.04; PC3 top/bottom 10 = +5.43 / +3.57, 5% tails = +2.66 / +2.34. Same pattern as before.
- Adding PC3 (experiment 6): Spearman **0.988** with the PC1+PC2 score; median |change| 1.73, 90th pct 5.21, extremes +11.2 / −12.0; 23.4% of models change bucket (4 of them by two). Risers are again small enum-heavy models (`model_4314`, 5 classes, 4 enums, +11.2), fallers the largest (271-341 classes, −11 to −12). Models with methods now fall *more* than models without (−1.28, n=699, vs −0.74), so PC3 is even further from rewarding methods.
- Without the copies, PC2 costs nothing in article agreement: PC1 alone 0.9164, PC1+PC2 0.9165. On the 8,336 set it cost 0.019; that gap was produced by the copies.
- Clip: 6 models above 100 and 1 below 0 before clipping (max 107.2), Spearman change −0.0004. Without the 992 zero-has_logic models: 0.9217.
- Bucket sizes (PC1+PC2): 363 / 1,239 / 1,294 / 1,002 / 647 / 336 / 188 / 127 / 59 / 9 for 0-10 … 90-100.

**Decision unchanged: PC1+PC2.**

**How to defend it (for the article).** The argument, in order (numbers from the 5,264-model refit):
1. *Why PC1.* It is the dominant component (48.8% of variance) and every loading is positive, so it reads as overall size and complexity.
2. *Why PC2.* It is a second, interpretable axis (data-schema-heavy vs. hierarchy-heavy). Kaiser and parallel analysis both retain it. Its 10 most extreme models on both ends are above-average size. Over its 5% tails, one end is big hierarchies and the other is attribute-rich flat models of slightly below-average size: a real difference in style, not tiny models drifting to one end.
3. *Why not PC3, although the tests also retain it.* Retention rules say how many components carry more than noise; they do not say which ones improve a difficulty score for a given purpose. We therefore measured PC3's effect directly:
   - It barely changes the ranking (Spearman 0.988 with the PC1+PC2 score).
   - Where it does change scores, it moves small enum-heavy models up by up to 11.2 points and the largest models down by about 12.
   - Models with methods fall more than models without, so it does not give methods more weight despite its +0.30 loading.

   That adds noise for our purpose rather than signal. Report the retention tests in full and present PC1+PC2 as a deliberate, measured choice, not as what the tests alone dictate.
4. *Why not PC1 alone.* It captures size only. PC2 adds a real second kind of structure at no cost in article agreement (0.9164 vs 0.9165).
5. *Why variance-proportional weights and |PC2|.* See the 2026-09-28 explainer and the method entry further down: the weights are not hand-chosen, and the sign of PC2 is arbitrary.

---

## 2026-10-18 — Scripts refactored onto a shared `scripts/_common/` package; output verified byte-identical

**Why.** The code review found the same helpers copy-pasted 13-24 times across `scripts/`, and fixes that had only reached some of the copies (the retry-on-error rule reached 7/17 scripts, the stale-cache safeguard 4/17). A fix applied to one copy and not the others is how inconsistent results creep in, so the copies were replaced with one shared implementation each.

**What `_common/` holds.** `io` (BOM-safe text reading, model-list resolution, `--dataset-dir`/`--reports-dir`, merging one key into a model's JSON), `cache` (resumable JSONL cache with the test-file safeguard, retriable-status partitioning), `pool` (the ProcessPoolExecutor loop that appends each result to the cache and records crashes as `error`), `report` (status table, JSON+Markdown report writing in UTF-8), `ast_utils`, `baseline` and `green` (the 2026-10-18 false-positive fixes below), `crosshair` (the CrossHair sanitizer), `buml` (finding/loading a model's BUML source, `type_name`, deterministic `ordered_ends`), `testgen` (the ~15 helpers `generate_structural_tests.py` and `generate_behavioral_tests.py` used to duplicate, plus `buml_to_puml.py`'s third copy of `ordered_ends`). Every script now uses these.

**Bugs fixed along the way.** `validate_coverage_split.py` read `python_code.py` in the Windows default encoding (mis-reported model_2210/2213/2243/2246); `validate_tests.py` recorded a model's last error instead of its first; `validate_logic.py` overwrote the exclusion file even on a partial `--models-file` run; several scripts wrote reports/metadata without `encoding="utf-8"`; `select_test_generation_sample.py` would have crashed with a `NameError` on its final print; `compute_difficulty_score.py` now warns if a field excluded for being constant stops being constant.

**Verification.** A static pass over all 42 script files (compile, undefined names, unused imports): 0 problems. Every module imports under its venv (`.venv`, `.venv-puml`; the two tree-sitter scripts need a `.venv-treesitter` that doesn't exist on this machine yet). `test_structural_full.py`, `test_behavioral.py` and the `.puml` file were regenerated for all 200 sample models into a scratch copy and compared to the dataset: **600/600 byte-identical** -- the refactor changes no output.

---

## 2026-10-18 — The 92.66% super-suite score was a false positive; honest re-measurement: 77.55% vs 34.52% baseline (+43.03 pts)

**What was wrong.** cosmic-ray counts a mutant as KILLED whenever the test command exits non-zero. A suite that already fails on the *unmutated* `python_code.py` therefore "kills" every mutant and the model scores a fake 1.0. Neither mutation validator ever checked that a suite passes unmutated first -- the only such check (`check_baseline_passes()`) lived in the since-deleted LLM pipeline script, never in `validate_mutation.py`/`validate_mutation_properties.py`. Running every sample model's `test_super_suite.py` once, unmutated, showed **155/200 failing**; the v2 report had 157 perfect scores.

**Four independent causes** (found by running each failing suite without `-x` and grouping every failing test):
1. **Stub-double tests asserted the wrong shape** (`generate_behavioral_tests.py`, added 2026-10-12): `assert getattr(partner, attr) == owner` is only right when the stub end holds one object. When it holds a collection the real setter stores `{owner}`, so the test failed on every run. Verified by hand only on `model_1`, whose stub ends happen to all be scalar -- that one check was wrongly treated as covering every shape. A second variant: BUML end names the generator sanitizes (`RDBMS.ecoreTable` -> `RDBMS_ecoreTable`, `model_100170`) were attached to the stub under the raw name, so the setter's `hasattr` guard never saw them.
2. **CrossHair tests of Python's own `Enum` internals** (89/200 models): `Enum.__new__` / `Enum._generate_next_value_` -- standard library, not model code -- matching an exact error message whose wording differs between Python versions.
3. **CrossHair `datetime.date(...)` with no `import datetime`** (~13 models): a `NameError` on its own, a `TypeError` once merged next to suites that `from datetime import datetime` (the class shadows the module name).
4. **The dataset's own `test_hypothesis.py` empty-method checks** (49/200 models): the `..._changes_state` tests deliberately `FAIL if empty` -- every `# TODO: Implement` stub operation fails them on the original code. These are dataset-quality checks, not behavior tests, and they sit in the *baseline* suite, so the baseline (50.85%) was inflated too. Dataset-wide this affects ~940 models (1,046 have stub operations; the 2026-09-01 test validation already reported 1,055 failing original suites), and e.g. `model_298` scored a fake 1.0 in both September full-dataset mutation runs -- those dataset-wide averages are inflated the same way and must be re-measured with the guard below.

**Fixes.**
- **Guard in the measurement step** (`scripts/_common/baseline.py`, used by both mutation validators): the exact test command runs once unmutated before `cosmic-ray init`; if it fails the model gets `baseline_failed`, never a score. Generator-independent, so no future generator bug can inflate a score silently again.
- **Green suites** (`scripts/_common/green.py`): a suite is run unmutated, every failing test is removed and listed in the report, repeated until green; repeated top-level test names are renamed first (Python keeps only the last definition, so duplicates never ran -- 28 found). `generate_super_suite.py` now only writes a green `test_super_suite.py`; `scripts/make_green_suite.py` applies the identical rule to any other suite (`test_combined.py` -> `test_combined_green.py`) so comparisons stay fair. This is also what the benchmarking oracle needs: a test that fails on the reference code can't judge LLM-generated code.
- **Generator fixes, so good tests aren't lost to pruning**: CrossHair output sanitized (`scripts/_common/crosshair.py`: stdlib `Enum` tests dropped, invalid syntax skipped, `datetime` module references aliased) -- applied in `generate_crosshair_tests.py` and on read in `generate_super_suite.py`; stub-double tests now read the partner attribute name and its single-vs-collection shape directly from the real setter's source, and skip rather than guess when it can't be read.

**Honest re-measurement** (200-model sample, `--hypothesis-seed 0`, `validate_mutation_properties.py`, 200/200 green, 200/200 measured, 0 `baseline_failed`):

| | Published | Honest |
|---|---:|---:|
| Baseline (`test_combined` -> `test_combined_green`) | 50.85% | **34.52%** |
| Super suite | 92.66% | **77.55%** |
| Lift | +41.81 pts | **+43.03 pts** |

Per model (super vs baseline, both green): **188 improved, 0 worsened, 12 unchanged**. Perfect scores: baseline 49 -> 0, super suite 157 -> 3. The 441 removed tests are the same dataset empty-method checks in both suites. Reports: `reports/super_suite_report.*`, `reports/green_test_combined_report.*`, `reports/test_generation_super_suite_mutation_v3.*`, `reports/test_generation_baseline_green_mutation.*`. The standalone CrossHair (64.24%) and Behavioral (59.89%) numbers from 2026-10-11 used the same unguarded measurement and are superseded, not re-measured.

---

## 2026-10-17 — BOM-read rollout, stale-cache-by-test-file safeguard, and a non-decision on the mutation-score exclusion filter

**BOM-sniffing fix rolled out to the remaining 17 scripts.** `_read_text_robust()` (sniffs the actual BOM bytes for `--models-file` instead of assuming one encoding -- see the 2026-10-12 entry below for the two different real encodings this already caught) had only been applied to the 4 scripts touched that day. Grepped for the vulnerable `models_file.read_text().splitlines()` pattern across `scripts/`, found 17 more, applied the same helper to all of them: `generate_crosshair_tests.py`, `generate_super_suite.py`, `generate_combined_tests.py`, `generate_pynguin_tests.py`, `validate_coverage.py`, `generate_structural_tests.py`, `validate_class_coverage.py`, `validate_generator_fidelity.py`, `validate_coverage_split.py`, `validate_coverage_structural.py`, `validate_generator_fidelity_names.py`, `generate_model_metadata.py`, `generate_code_structure.py`, `classify_method_logic.py`, `validate_mutation.py`, `buml_to_puml.py`, `check_property_name_mismatches.py`.

**Stale-cache-by-test-file safeguard, built for real instead of left as a "decide later" item.** The 2026-09-16 entry below documented a real incident (two class-coverage runs sharing a `--report-name` but different `--test-file` values, second run silently reusing the first's cached results under its own key) and only worked around it manually (distinct `--report-name` per run), noting the script-level fix as "not yet built." Fixed at the code level this time, in the 4 scripts that actually combine a resumable JSONL cache with `--test-file`: `validate_class_coverage.py`, `validate_coverage_structural.py`, `validate_mutation.py`, `validate_mutation_properties.py`. Each cached result now records which `test_file` produced it; `load_cache()` takes an `expected_test_file` argument and drops (forces recompute of) any cached entry recorded against a different test file, printing how many it dropped, instead of silently trusting it. Entries written before this field existed (no `"test_file"` key) are still trusted, so existing caches aren't invalidated. The other ~14 cache-using scripts don't take `--test-file` at all, so they were never exposed to this failure mode and weren't touched.

**Decided not to build a dedicated "exclude unmeasurable models" script.** `reports/excluded_models_master.json` already records the 111 models with no calculable mutation score (79 `old_suite_unmeasurable` + 32 `combined_suite_unmeasurable`, both timeout-driven, distinct from the 631 `no_logic` models). No current script cross-references mutation score against difficulty score, so there's nothing to wire this into yet, and building a standalone script for a 2-3 line filter nobody calls would be premature. Whenever a future analysis actually needs it: load `excluded_models_master.json`, pull the model names tagged with either of those two reasons, and subtract them from that script's model list inline -- no new script or shared helper needed for this.

---

## 2026-10-12 — "Equivalent" mutants from stub associations turned out to be killable after all

> **Superseded 2026-10-18:** the 92.66% / +41.81 pt results below were a false positive -- the stub-double tests failed on unmutated code for collection-valued stub ends, and nothing checked that. Honest numbers: 77.55% vs 34.52% baseline (+43.03 pts). See the 2026-10-18 entry above. The `model_1` result (35% -> 95%) is genuine.

Reversing a 2026-10-01 conclusion: stub-association mutants (one side of a bidirectional link is a bare `class X: pass` with no real properties, so the generated code's own `hasattr(item, "...")` guard protecting that logic is permanently False) were assumed genuinely unkillable by any test -- "a real, non-zero floor... account for that when judging any track's resulting mutation score." That diagnosis of *why* they survive was correct; the conclusion that nothing could kill them was not.

**Found while debugging why a local-LLM generator-upgrade loop made zero progress on `model_1` across 5 retries** (see the "Local-LLM test-generation experiment" entry below): traced all 26 surviving mutants by hand against the real generated code. ~24/26 sit behind exactly this stub-association pattern (`target`, `petrinet_Node5`, `petrinet_Node9`, `Node`, `petrinet_Petrinet2` -- all point at the bare `petrinet_Arc` stub). This wasn't an LLM or prompting failure; no test, from any technique, can observe a difference inside dead code.

**The fix**: `petrinet_Arc` has no `__slots__`, so nothing stops a *test* from manually `setattr()`-ing the exact attribute name a real implementation would have had, before exercising the real side's setter. This is an ordinary test-double pattern -- standing in for an incomplete collaborator to test the real side's own logic in isolation -- not a fabricated result: the resulting assertion genuinely passes or fails based on real behavior. Hand-traced the exact sequence against `model_1`'s `target` property first to confirm the mutated comparison (`opp_val == self` -> `is not`/`<`/`>`/etc.) would actually be observable this way, before building anything.

**Built as a new deterministic rule in `scripts/generate_behavioral_tests.py`** (not LLM-dependent -- same "diagnose once by hand, hand-write a reliable generator rule" pattern as the original behavioral generator): for each binary association where exactly one side is a stub, construct both sides, manually attach the stub's missing reciprocal attribute, then exercise the real side's setter (assign + clear), asserting the stub's attribute updates correctly both ways.

**Result on `model_1`: 35% (baseline) -> 42.5% (first behavioral fix) -> 95% (38/40 killed, 2 survived).** Confirmed not a false positive the same way the CrossHair/LLM-written-test bugs were: a collection-failure false positive always produces a *uniform* result (every mutant misread as killed identically, i.e. 40/0) -- a genuine 38/2 split is only possible if the suite is actually differentiating between mutants, which means it's really running.

**Confirmed this generalizes well beyond `model_1`**: ran across the full 200-model sample, folded into the super suite -- **92.66% avg, 200/200 measured**. Vs. baseline (50.85%): **+41.81 pt lift**, 142 improved / 0 worsened / 58 unchanged. Vs. the pre-stub-double super suite (77.59%, see the entry below): a further **+15.08 pts**, 55 improved / 0 worsened / 145 unchanged. Zero models worsened in either comparison -- the fix is monotonic at scale, not a `model_1`-specific fluke. Report: `reports/test_generation_super_suite_mutation_v2.{json,md}`.

---

## 2026-10-12 — Local-LLM test-generation experiment (exploratory, via Ollama)

Before handing the colleague's two-stage pipeline off, tried running it locally against `model_1` with a local Ollama model to see what breaks in practice. Real findings, not wasted effort -- several genuine bugs found and fixed along the way:

- **`llama3:8b` too weak for this task.** First just described the code instead of editing it at all (fixed by restating the instruction at the end of the user turn, not just the system prompt -- weaker models weight a system prompt less reliably than something stated right before generation starts). Once it did attempt the task, it wrote fragments with malformed names (`exact_name='constructible'` instead of just `constructible`) and hallucinated code unrelated to anything real in the file.
- **`qwen3-coder:latest` capable, but surfaced real format and safety problems.** Asking for a full-file rewrite caused genuine timeouts (large expected output, compounded by Ollama's default 5-minute keep-alive evicting the model between slow retries) -- fixed by switching from "return the whole file" to a plain-text `<<<ADD>>>`/`<<<REPLACE name>>>`/`<<<DELETE name>>>` ... `<<<END>>>` action format (deliberately not JSON either: embedding multi-line code as a JSON string needs exact escaping of every newline/quote, which a weak model gets wrong far more often than it gets a short literal marker line wrong).
- **A real false-positive mutation score, same bug class as the CrossHair syntax bug.** An LLM-written test called a constructor with the wrong arguments, so it failed unconditionally (not from any mutation) -- `pytest -x` turned that into "every mutant looks killed." Fixed by adding `check_baseline_passes()` to `scripts/generate_llm_improved_tests.py`: the candidate suite must pass UNMUTATED before any mutation score from it is trusted at all; if every model's baseline fails, mutation measurement is skipped entirely that retry and the LLM is shown the real error instead.
- **A duplicate-definition bug in our own `apply_edit_actions()`**: an `ADD` action for a name that already exists would have created a conflicting duplicate top-level definition instead of replacing it (confirmed real -- `qwen3-coder` did this twice for the same helper). Fixed to auto-convert to a replace in that case.
- **The real reason retries stopped helping wasn't the model or the prompt at all** -- see the "equivalent mutants" entry above. Once ~92% of a model's survivors are confirmed unkillable by any test, no amount of retrying moves the score; the deterministic stub-double fix was the right lever, not more prompting.
- **A recurring BOM encoding bug, found twice with two different encodings on two different scripts**: PowerShell's `echo >` defaults to UTF-16LE with BOM, `Out-File -Encoding utf8` defaults to UTF-8 WITH BOM -- neither matches plain `.read_text()`'s assumption, and the UTF-16 case also corrupts line-splitting entirely (one line becomes several, since UTF-16 is 2 bytes/char). Fixed with a shared `_read_text_robust()` helper (sniffs the actual BOM bytes) in `generate_llm_improved_tests.py`, `generate_behavioral_tests.py`, `merge_combined_and_behavioral.py`, and `validate_mutation_properties.py` so far -- `checklist.md` tracks rolling it out to the ~20 other scripts with the same `--models-file` pattern.

---

## 2026-10-11 — Super suite confirmed to beat every individual test-generation approach, not just on average

> **Superseded 2026-10-18:** every score in this entry (baseline 50.85%, super suite 77.59%, CrossHair 64.24%, Behavioral 59.89%) came from suites that were never checked to pass unmutated; several contained tests failing on the original code, which count every mutant as killed. Honest comparison: see the 2026-10-18 entry.

Ran `scripts/generate_super_suite.py` (combined+behavioral+CrossHair, with the invalid-syntax guard from the earlier entry) for real across the 200-model sample, then measured mutation score with `--hypothesis-seed=0` (the now-standing convention) via `validate_mutation_properties.py`.

First pass measured 185/200 (15 timeout); retried at `--overall-timeout 1800` and all 15 recovered, same auto-retry pattern used everywhere else in this project (no manual merge needed, same `--report-name`).

**Final result: 200/200 measured, 77.59% avg.** On the full 200-model set, baseline scores its own already-published 50.85% -- a **+26.74 point lift**, well beyond even CrossHair's standalone best (64.24% on its own, smaller, 173-model subset). Per-model breakdown is the real confirmation this isn't just an average fluke: **123 improved, 0 worsened, 77 unchanged** -- strictly monotonic, now confirmed on the complete sample, not just the 185 that measured on the first pass. Behavioral alone was already known to be monotonic (purely additive); this confirms the property holds even once CrossHair's tests (which were a real mixed bag -- 65 worsened -- when substituted in standalone) are merged alongside rather than swapped in. Report: `reports/test_generation_super_suite_mutation.{json,md}`.

This is now the strongest evidence in the whole comparison for the "combine, don't pick one" recommendation already written up in `reports/test_generation_comparison_report.md`.

---

## 2026-10-11 — Built the colleague's two-stage LLM pipeline (generator upgrade, then per-model tests), pluggable and scratch-safe

Per the redesigned plan (see Step 2/checklist, 2026-10-11): instead of an LLM patching tests for one model at a time, stage 1 edits the *shared* test-generator script using patterns pooled across the sample's surviving mutants (the same kind of improvement as the behavioral generator, but LLM-found instead of hand-found); stage 2 then adds per-model tests on top, once stage 1 has run across the whole sample.

Built two files:
- **`scripts/llm_test_adapter.py`** -- the pluggable interface (`upgrade_generator`, `write_model_specific_tests`). `StubAdapter` is a no-op (no network call, no API key) specifically so every OTHER part of the pipeline can be verified for real without one. `LiteLLMAdapter` is a thin wrapper around `litellm.completion(**kwargs)`, deliberately not exercised against a real model/key from this side -- that's the colleague's own credential and config, not ours to guess at.
- **`scripts/generate_llm_improved_tests.py`** -- the two-stage orchestrator. Every file it writes lives under `--scratch-dir`, never `Dataset/` directly -- enforced unconditionally here (not left to caller discipline), since an LLM-edited generator script is untrusted code by this project's own standard, and running untrusted generated code directly against the live dataset would be a much worse failure mode than the usual case. Reuses the real pipeline throughout, not reimplementations: `generate_structural_tests.py` for regeneration, `generate_combined_tests.py`'s `combine_tests()` for the old+new merge, the same invalid-syntax guard `generate_super_suite.py` uses for CrossHair, and `validate_mutation_properties.py` (with `--hypothesis-seed=0` and `--export-surviving-mutants`, so each retry's prompt is built from THAT retry's own remaining gaps, not stale baseline data) for the real, expensive mutation measurement. The "still open" design questions from the checklist (retry count, per-model-vs-aggregate threshold, whether to afford a full-sample remeasurement every retry) are left as CLI flags with defaults rather than guessed at and hardcoded.

**Verified end-to-end on exactly one named model (`model_1`, never the real dataset)**, stub adapter, `--max-retries 1 --stage 1`: real regeneration -> real suite assembly -> real mutation measurement gave **0.35**, an exact match to `model_1`'s already-known, seed-0-reproducible baseline score. That's a stronger check than "it runs without crashing" -- it confirms the plumbing produces the SAME real number the rest of this project already trusts, not a plausible-looking but wrong one. Stage 2 also verified not to corrupt anything with the stub adapter (0 tests added, candidate file's test count unchanged).

---

## 2026-10-11 — PCA component sweep: more components does not mean better agreement with the article formula

Built `scripts/experiment_difficulty_score_pca.py` to check an implicit assumption behind the official 2-component (PC1+PC2) `difficulty_score`: that using more of the available structure (up to all 11 components) would track the reference paper's formula at least as well. Run dataset-wide (8,451 models, excluding the ~631 no_logic-only models the official score doesn't exclude):

**Spearman-vs-`difficulty_score_article` is not monotonic in component count, and PC1 alone is the best single choice (+0.8960)** -- adding PC2 (the official combination) actually drops it to +0.8791, it keeps dropping through PC3/PC4 (+0.8672/+0.8653), then slowly climbs back to +0.8887 by PC10, never recovering to PC1-alone. Makes sense once stated plainly: the article formula is an unbounded linear combination of raw counts, dominated by sheer size -- exactly what PC1 ("how big") already measures. PC2's axis (data-schema-heavy vs. hierarchy-heavy architectural style, real variation, already documented in `difficulty_score_report.md`) is a *different kind* of complexity the article formula was never designed to reward, so folding it in trades away some rank agreement with that specific reference, even though it's the reason PC2 was included in the first place (capturing a second, genuinely different axis of difficulty the article formula misses entirely). **This isn't a reason to drop PC2** -- the official score's goal was never "maximize agreement with the article formula," it was "capture more than one real kind of structural complexity" -- but it is a concrete number for anyone asking why the two scores don't agree perfectly, and confirms the two scores are measuring deliberately different things, not that either is wrong.

**Second experiment, same script**: removing the percentile clip changes rank agreement negligibly (+0.8791 clamped vs. +0.8790 unclamped, delta -0.0001) -- confirms clipping barely affects *rank*, as expected. But it does real, measurable work on *magnitude*: **13/8,451 models (0.15%) exceed the nominal 0-100 cap once unclamped**, up to 106.2 (`model_2578`); 0 fall below 0.

Full numbers: `reports/difficulty_score_pca_experiment_report.json`. Also built `scripts/difficulty_score_distribution.py` (1-point-bucket histogram of the official score, same exclusion): mean 33.0, median 29.35, min 3.27 (exact match to the official full-dataset min -- a good independent cross-check that the exclusion didn't silently break anything), max 93.55, right-skewed, densest around 15-30.

---

## 2026-10-11 — The 22 tree-sitter-vs-model name mismatches were false positives in our own checker, not a dataset defect

Scoped down from the original idea ("fix the models/code that `validate_generator_fidelity_names.py` flagged") after actually reading the generated code for several of the 22 flagged models, rather than assuming the report was right: **every one of the 22 is a false positive in this project's own name-resolution logic**, not a generator bug, and not a tree-sitter bug. There was nothing in the dataset to fix.

Two confirmed patterns (full detail in `validate_generator_fidelity_names.py`'s own docstring, which was updated alongside the fix):

1. **20/22**: a BUML attribute named `property` or `self` collides with a Python builtin/keyword. The generator disambiguates -- inconsistently across the dataset -- either by keeping the public `@property` accessor's original name while only renaming the internal backing field (`model_116`: `self` -> public getter still `self`, backing field `self_`), or by renaming both ends with the same `+1` suffix (`model_100505`: `self` -> `self1` end-to-end; `model_10001303`: `property` -> `property1` end-to-end). The old checker only ever looked at the code's `attributes` list, never `methods`, and never tried a `+1` suffix -- so it reported "missing" for something that was correctly generated, just filed under a different JSON key or a disambiguated name.
2. **2/22**: the already-known `Factura` -> `Facturas` pluralization, which `generate_structural_tests.py`'s own `resolve_code_name()` already handles but this checker never carried over.

**Fix applied to `scripts/validate_generator_fidelity_names.py`** (no dataset files touched -- manually "fixing" already-correct generated code would have diverged 22 models from their own generator and broken consistency with the rest of the dataset for no reason): `resolve_name_in_set()` now tries, in order, the raw name, the sanitized name, each of those with a `+1` suffix (attributes) or `+s` suffix (classes), and finally a case-insensitive match as a last resort.

**Re-verified against exactly these 22 named models (not a full/sampled dataset run, per standing rule)**: 20/22 now resolve with zero mismatch. The remaining 2 are real, distinct findings, not resolver gaps:
- `model_10001897`: one attribute, `Fecha`, is genuinely absent from the generated code under any name/case tried -- a real (tiny) generator gap.
- `model_10001985`: turns out *not* to be the same kind of case as `model_10001897` despite being documented together as "the Factura pair" since early in the project -- its BUML `Factura` class has no matching class in the code at all, instead splitting into two package/layer-qualified classes (`LogicaPresentacion___Factura_Component`, `Persistencia___Factura_Component`). A structurally different, more complex case, not chased further today.

**Confirmed dataset-wide (8,336/8,336 compared, `--fresh` -- the first attempt silently reused the pre-fix cache, since `"compared"` isn't a retriable status; worth remembering for any future fix to a script with a mature cache)**: mismatch rate drops from 0.26% (22/8,336) to **0.02% (2/8,336)**, and the 2 remaining are exactly the two genuine findings above -- no new false positives, no regressions.

---

## 2026-10-11 — Standing convention: `--hypothesis-seed=0` for every test-generation-comparison mutation run

Writing this down explicitly because it had only ever been agreed in
conversation, not recorded anywhere, which caused a real mix-up: a
super-suite mutation command was handed off and run without the flag before
this was caught.

**The rule**: every mutation measurement that feeds the test-generation
comparison (`reports/test_generation_comparison_report.md` and anything
that extends it -- baseline, Pynguin, CrossHair, Behavioral, the super
suite, and any future approach) uses `--hypothesis-seed=0` on
`validate_mutation_properties.py`, for genuine apples-to-apples
comparability across approaches. Confirmed with the user 2026-10-11: the
4 existing Stage 1 reports (`test_generation_baseline_mutation`,
`_behavioral_mutation`, `_pynguin_mutation`, `_crosshair_mutation`) were
already run this way, so the super suite run joining them must match.

**Why this is worth a flag was easy to miss**: neither the mutation
validators nor their reports store which flags a given run used --
`--hypothesis-seed`'s effect lives entirely inside a per-model cosmic-ray
config file in a scratch directory that gets deleted once that model's run
finishes, so there is no way to verify after the fact whether a past run
was seeded just by inspecting `reports/*.json` or the dataset. If this ever
needs re-confirming, there is no file to check -- only this entry and
whoever ran the commands.

**Scope**: this is specific to the test-generation-comparison sample
(200 models) and whatever supersedes it. The much larger body of
already-published full-dataset mutation scores (old/new/combined suites,
~9,082 models) was measured before this convention existed and is not
retroactively affected -- that's the same already-known
"not reproducible pre-`cap_mutants`-fix" gap tracked separately (see the
"Found and fixed a real bug in cap_mutants()" entry above/below).

---

## 2026-10-11 — Super suite merger built; found a real bug in CrossHair's own output deflating confidence in 4 standalone scores

Built `scripts/generate_super_suite.py`: `test_combined.py` + `test_behavioral.py`
+ `test_crosshair.py` merged into one real `test_super_suite.py` per model,
the actual artifact for "does combining everything beat each individual
approach" (not just averaging separate scores).

**Checked collision risk before writing it, rather than assuming**: an AST
scan across all 177 models that actually have `test_crosshair.py` found
**zero top-level function-name collisions** against that same model's
`test_combined.py`/`test_behavioral.py` — CrossHair's own naming
(`test_{ClassName}___init__`, triple underscore) never matches anything our
own generators produce. Plain concatenation is safe here for the same
reason it was already safe for behavioral (a wholly new test shape with no
counterpart to dedupe against), confirmed rather than inherited by analogy.

**Real bug found during that same scan**: 4/177 models'
(`model_452`, `model_1116`, `model_1185`, `model_3216`) `test_crosshair.py`
is **not valid Python** — CrossHair's `--example_output_format pytest`
can emit a bare object repr (e.g.
`UML2WithID_Component={<python_code.UML2WithID_Interface object at
0x...>}`) into a set literal when it can't find a better example value for
a set-typed argument. A syntactically broken test file fails to even
collect under pytest regardless of which mutation is applied to
`python_code.py`, and neither `validate_mutation.py` nor
`validate_mutation_properties.py` ever checks that the *unmutated* test
file collects before trusting a result — cosmic-ray reads the resulting
non-zero exit code as "killed" for every single mutant, every time.
Confirmed: all 4 models report `mutation_score: 1.0`, `killed: 40/40`,
`survived: 0` — a fake perfect score from a collection failure, not real
test strength. **Corrected published number**: excluding these 4,
`reports/test_generation_comparison_report.md`'s CrossHair standalone
average moves from **65.05% → 64.24%** (177 → 173 models). The headline
conclusion (CrossHair beats baseline) is unaffected, but the number was
inflated.

**Fix applied in `generate_super_suite.py`**: `ast.parse`-validate
`test_crosshair.py` before including it in the merge; an invalid file is
skipped for that model (flagged in the report as
`crosshair_skipped_invalid_syntax`, not silently dropped) rather than
corrupting the whole merged file into another fake-perfect score — which
would have been worse than the standalone case, since it would also mask
whatever `test_combined.py`/`test_behavioral.py` were really contributing.

**Not yet fixed at the root**: `validate_mutation.py`/
`validate_mutation_properties.py` still have no baseline-collection sanity
check for *any* test file, so this exact failure mode could recur for any
future generator with its own syntax edge cases, not just CrossHair. Noted
as a known gap, not scheduled.

**Verified** against a 4-model scratch copy (never the real dataset):
plain combined-only merge (`model_1`), a clean 3-way merge with real
behavioral + CrossHair tests (`model_10000151` — counts matched exactly:
2 behavioral + 2 CrossHair tests added, confirmed independently via
`grep -c '^def test_'`), a 3-way merge where the model's own
`test_behavioral.py` legitimately contains zero tests, just unused helper
functions (`model_10000011` — correctly reported as 0 added, not a bug),
and the invalid-syntax skip case (`model_452` — confirmed the broken
literal is absent from the merged output and the file still parses).

---

## 2026-10-02 — Name-based generator fidelity, run dataset-wide: 99.74% clean, two real patterns found

**Run against the full `usable_models.txt` (8,336 models)**:
`validate_generator_fidelity_names.py` found only **22/8,336 models (0.26%)
with any name-level mismatch** -- 2 missing classes, 20 with a missing
attribute, 0 missing operations. This strongly confirms the generator is
highly faithful **by name** at scale, not just on the 5 hand-picked spot-
checks done when the script was built -- consistent with (and a useful
complement to) the existing count-based fidelity finding that mismatches
there are overwhelmingly the *expected*, documented kind (association
accessors, property pairs), not generation failures.

**Two concrete patterns among the 22, both worth knowing about:**

1. **`model_10001897`/`model_10001985` -- the exact same "Factura" pair
   already documented earlier this project** (the generator renders BUML's
   `Factura` as `Facturas`, confirmed independently back when fixing these
   two models' `test_structural_full.py`). Seeing this name-based check
   reproduce a previously-known defect via a completely different method
   (live-BUML-vs-tree-sitter name comparison, not manual inspection) is a
   good sign the check itself is sound, not just that it finds novel bugs.
2. **17 of the 22 involve a class attribute literally named `property`
   going missing from the generated code** (e.g. `model_10001303`,
   `model_10002412`, `model_10002604`, all with a `Player` class). Not yet
   root-caused, but the name is suggestive: `property` collides with
   Python's own `@property` decorator/builtin, so the generator may be
   silently dropping or mishandling an attribute whose BUML name happens to
   be exactly that reserved-sounding word -- plausible, not yet confirmed,
   and not investigated further here.

---

## 2026-10-02 — Stage 1 results: Pynguin loses, CrossHair genuinely wins (on a fair, same-subset comparison)

**The 200-model Stage 1 measurement finished: baseline, Pynguin, CrossHair,
and Behavioral all measured via the same (now-reproducible, auto-retrying)
`validate_mutation_properties.py` pipeline.** Raw standalone averages:
baseline 50.85% (200/200), behavioral 59.89% (200/200 -- baseline plus the
new association tests, a genuine **+9.0 point lift** over baseline, slightly
better than the single-model `model_1` result found earlier), Pynguin
27.75% (192/200 -- 8 models never got a `test_pynguin.py` at all, the known
largest/most-complex-model generation failures), CrossHair 65.05% (177/200
-- 23 models produced zero tests, no class had a usable non-property-only
target).

**Caught and fixed a real comparison-fairness mistake before drawing any
conclusion.** Pynguin/CrossHair's raw averages are standalone scores on
different, *smaller* subsets than baseline's full-200 average -- comparing
65.05% directly against 50.85% would be comparing different populations of
models, not a fair test of either tool. **Fixed by comparing each tool's
standalone score against baseline's score on that exact same subset**, not
baseline's full-200 figure:

| | Pynguin (192-model subset) | CrossHair (177-model subset) |
|---|---:|---:|
| Baseline, same models | 51.54% | 52.12% |
| Tool standalone | 27.75% | 65.05% |
| **Delta** | **-23.79 pts** | **+12.93 pts** |

**Pynguin is effectively ruled out** as a useful Track A contributor --
loses badly even on its own best-case subset, consistent with everything
already diagnosed about its weak isinstance-only assertions on this
dataset's property-heavy code. **CrossHair genuinely wins**, by a wide
margin, on a fair head-to-head -- real evidence that symbolic execution
produces a stronger test suite than this project's current generator, at
least on the subset of models where it can run at all (one with >=1
class that isn't purely property-only).

**Not yet measured: CrossHair's or Pynguin's *incremental* lift when merged
into `test_combined.py`**, the same treatment Behavioral already got. The
numbers above only show "would this suite work alone," not "does adding it
help" -- the more directly useful question for deciding what to fold into
the eventual super suite. CrossHair is the clear next candidate for that
treatment given today's result; Pynguin likely isn't worth the effort given
how badly it underperforms even standalone.

---

## 2026-10-02 — Built the name-based generator-fidelity check (counts were never enough)

**Flagged 2026-10-01, built today, while mutation measurements ran in the
background.** `validate_generator_fidelity.py` has only ever compared
*counts* between the BUML model and the generated code (e.g. "model says 5
classes, code has 6"). The user pointed out this is a real methodological
gap, not a nice-to-have: two counts can agree while referring to entirely
different, unrelated names. The question that actually matters -- "did the
generator produce *this specific* class/attribute/operation?" -- requires a
name-level check. This also directly anticipates a future need: validating
whether an LLM (Track B, or any future LLM-based generation) produced code
with *all the necessary* classes/methods/attributes. A count match there is
close to meaningless -- an LLM could hallucinate the right number of classes
under the wrong names, or merge/split classes while preserving the total.

**Built `scripts/validate_generator_fidelity_names.py`, a genuinely new
script (not a modification of the count-based one, which stays as-is and
still answers a legitimate, different question).** Key design decision:
`model_metadata.json` turned out to only ever store aggregate counts, never
names (confirmed by inspection) -- so this script reads the **live BUML
model** directly via `besser` (requires `.venv-puml`) instead, reusing
`generate_structural_tests.py`'s own BUML-loading and identifier-
sanitization helpers (`find_buml_file`, `load_domain_model`,
`_python_identifier`) rather than reimplementing already-battle-tested
logic -- in particular the handling of BUML names containing characters
invalid in a Python identifier (e.g. `model_2533`'s `#`), which the real
code generator silently strips and which a naive name-set comparison would
otherwise misreport as a missing class.

For each BUML class, resolves it against `code_structure.json`'s (tree-
sitter) class names trying the raw name then the sanitized form; only a
genuine absence in both counts as missing. For each matched class, checks
every declared attribute/operation name against that class's actual code-
side attributes/methods the same way. Only *missing-from-code* is flagged --
extra code-side attributes/methods (association accessors, `__init__`,
property getters/setters) are expected noise, same reasoning the count-
based script already documented for its own attribute/method counts.

**Verified across 5 spot-checks**, never a full/sampled dataset run (per
standing rule -- the assistant never executes project scripts against the
dataset, only hands off commands): `model_1` and `model_100127` both show
zero mismatch, which is the *correct* result, not a missed bug -- this
check is orthogonal to the already-known abstract-flag defect (that's about
a flag's value, not whether the class exists by name). `model_2533`
confirmed the `#`-sanitization match works with no false-positive "missing"
report. `model_10001`/`model_100017` (real declared operations, not just
the common zero-operations case) resolved correctly with zero false misses.
Also directly unit-tested the resolution helper against a synthetic,
genuinely-absent name to confirm the detection side works, not just the
no-false-positive side.

**Not yet run dataset-wide** -- the 5 spot-checks all came back clean,
which is suggestive but not conclusive at that scale:
```
.venv-puml\Scripts\python.exe scripts\validate_generator_fidelity_names.py --models-file reports\usable_models.txt --workers 8
```

---

## 2026-10-01 — Real surviving-mutant diagnosis on model_1: two distinct causes, neither is "just vary the values"

**Correction, and real diagnosis via actual surviving mutants (not
assumption).** Before building a new "behavioral test" generator (per the
entry below), read `generate_structural_tests.py` in full and found the
premise wrong: it already generates a `link -> reassign -> clear` sequence
per binary association (e.g. `test_assoc_nodes0_link_reassign_clear`),
which already calls a setter with two different real values and checks the
reciprocal side -- i.e. it's already a behavioral, multi-call test, not a
single-snapshot structural one. The earlier claim that a new generator was
needed to add this was based on older context (`test_hypothesis.py`'s known
weaknesses) incorrectly carried over without reading this newer script
first.

Used the newly-built `scripts/mutation_export.py` to get real evidence
instead of guessing again: ran `validate_mutation_properties.py`'s
`validate_model()` directly (smoke-test only, scratch copy, same convention
as the Pynguin/CrossHair checks) against `model_1`'s real `test_combined.py`
with `--export-surviving-mutants`. Result: 40 mutants run, 10 killed, 30
survived (`mutation_score=0.25`, lower than this model's usual score since
property-scoped). Inspected all 30 surviving mutants' diffs directly.
**Every one lives inside a bidirectional-association setter's guard logic**
-- exactly what `link_reassign_clear` is supposed to exercise -- yet they
survive anyway, for two distinct, different reasons:

1. **Genuinely unkillable (equivalent) mutants, not a test gap.**
   `petrinet_Arc` is a bare `class petrinet_Arc: pass` (confirmed via
   `grep`+`Read`) -- zero properties. Setters linking to `petrinet_Arc`-typed
   objects (`target`, `petrinet_Node5`, `petrinet_Node9`) internally check
   `hasattr(item, "Arc")`/`hasattr(item, "petrinet_Arc6")` before doing
   anything observable -- since `petrinet_Arc` instances never have that
   attribute, this is **always False for any possible test**, making the
   comparison mutants inside that branch permanently dead code. No test of
   any kind (library-generated, LLM-generated, or hand-written) could ever
   kill these -- it's a code-generator limitation (an asymmetric
   bidirectional association: one side fully implemented, the reciprocal
   side a stub), not something fixable by writing better tests.
2. **A real, subtle gap: the generated test only triggers a setter from one
   direction, relying on the reciprocal side firing only as a side effect.**
   Traced `test_assoc_nodes0_link_reassign_clear` against the actual code
   line by line: it calls `a.petrinet_Petrinet = {b1}` and relies on that
   setter's own internal code to call `setattr(b1, 'petrinet_Node', a)` as a
   side effect -- it never calls `b1.petrinet_Node = ...` directly. Traced
   the nested execution for the reassignment step: by the time the
   reciprocal setter's own "remove old value" guard runs (triggered
   recursively from inside the outer setter), the *outer* setter has
   already overwritten its own stored collection to the new value -- so the
   specific comparison the surviving mutant touches ends up checking data
   that's already been replaced, making the mutant's effect unobservable in
   this exact call sequence. This is a genuine test blind spot, but the fix
   isn't "vary the literal values" -- it's **calling the setter from both
   ends of an association independently**, not relying on one side's side
   effects to exercise the other.

**Conclusion: no single simple fix (new generator or otherwise) addresses
both causes, and cause 1 isn't fixable by any test at all.** Any future
mutation-score comparison (Track A, Track B, or a new generator) should
expect a real, non-zero floor of unkillable mutants from asymmetric stub
associations -- this should be accounted for when judging "how good" any
approach's resulting mutation score is, not treated as 100% achievable.
Whether a new generator is worth building to address cause 2 specifically
(independent both-ends setter calls) is a decision for the user, not yet
made.

---

## 2026-10-01 — The `.venv-phase4` → `.venv-testgen` rename silently broke `crosshair.exe`, affecting the entire 200-model CrossHair batch run

**User reported every single model came back `no_tests_generated`, 0
classes covered, including models with hundreds of classes** -- a batch-
wide, total failure rather than the occasional per-class skip the smoke
test had shown. Root cause: `generate_crosshair_tests.py` invoked the
`crosshair`/`crosshair.exe` **console-script wrapper** directly (resolved
via `default_crosshair_cli()`, pointing at `.venv-testgen/Scripts/crosshair.exe`).
Windows console-script launchers generated by pip/distlib bake the venv's
**absolute path** into the wrapper at install time -- renaming the venv
directory (`.venv-phase4` -> `.venv-testgen`, done earlier the same day for
unrelated naming-clarity reasons) left the installed `crosshair.exe`
silently broken: confirmed directly, `exit 1, zero stdout, zero stderr` --
no error message of any kind, which is why every model's classes uniformly
failed instead of producing a visible crash.

**Fix: invoke `python -m crosshair` instead of the console-script wrapper,
never a fixed-path `.exe`.** This has no dependency on where the venv
directory happens to live, and is exactly how `generate_pynguin_tests.py`
already invokes Pynguin (`-m pynguin`, never a console-script wrapper) --
same class of fix, same reasoning, just discovered a day later for the
second tool. Removed `default_crosshair_cli()`/`--crosshair-cli` entirely
(no longer has any reason to exist); `--crosshair-python` (already present
for CLI symmetry with the Pynguin script, previously unused) now does the
real work, pointing at the venv's `python.exe` directly.

**Verified the fix restores the original, correct behavior**: re-ran
`generate_model()` against the same scratch copy of `model_1` used in the
original smoke test -- `1/7` classes covered (`petrinet_Petrinet`), byte-
identical to the pre-rename result. **Lesson for the future: renaming any
venv directory this project depends on requires re-verifying every
console-script entry point still works, not just that `python.exe` and
`-m <module>` invocations still function** -- those two are unaffected by
the rename (confirmed directly), only `.exe` wrappers are at risk.

---

## 2026-10-01 — Extended the auto-retry fix to all four generation scripts

**User hit the identical cache-permanence trap on `generate_pynguin_tests.py`**
(191/200 generated, 9 presumably timed-out/errored models stuck in the cache
as permanent failures) right after the mutation-validator fix above was
built -- the same `RETRIABLE_STATUSES` fix just hadn't been applied to the
newer generation scripts yet. Applied the identical pattern to all four:
`generate_pynguin_tests.py` (`{"timeout", "no_tests_generated", "error"}`),
`generate_crosshair_tests.py` (`{"no_tests_generated", "error"}`),
`generate_behavioral_tests.py` (`{"error"}`), and
`merge_combined_and_behavioral.py` (`{"error"}`) -- each excludes its own
permanent/input-data statuses (e.g. `missing_file`, `no_classes`,
`missing_combined`) the same way the validators exclude `missing_file`/
`no_mutants`. Verified each one with a synthetic 2-entry cache (one "good"
status, one "bad"/retriable status), confirming the retriable entry is
correctly excluded from the "done" set while the good one is left alone --
`generate_behavioral_tests.py` needed verifying via `.venv-puml` specifically
(where `besser` lives), the other three via the main `.venv`.

**Practical effect:** every script in the Phase 4 pipeline now self-heals on
a plain re-run (optionally with adjusted timeouts/workers) -- no script in
this project requires a separate `--report-name` + manual merge for a retry
anymore.

---

## 2026-10-01 — Mutation validators now auto-retry failed models under the same report, no more `_retry`/`_error` fragmentation

**User feedback: the established retry pattern (separate `--report-name`
per retry batch, then manually merge into a `_final` report) was "tiresome"
-- too many report files for one logical measurement.** This pattern had
been used repeatedly throughout the project (the 52-model retry, the
112-model retry, etc.) because the cache/resume logic treated ANY cached
result, including a failed one, as permanently "done" -- so simply
re-running the same command never retried a timeout, it just skipped it
forever.

**Fixed at the root in both `validate_mutation.py` and
`validate_mutation_properties.py`.** Added `RETRIABLE_STATUSES = {"timeout",
"error", "init_error", "exec_error"}` -- cached results with one of these
statuses are no longer treated as done. On the next run (same
`--report-name`, same `--models-file`, typically with a higher
`--overall-timeout` or lower `--workers`), already-measured models are
still skipped, but failed ones are automatically re-attempted and their new
result appended to the same cache file -- `load_cache()` already resolves
duplicate lines for one model name by letting the later line win, so this
required no change to the cache format, only to what counts as "skip."
`missing_file` and `no_mutants` are deliberately excluded from
`RETRIABLE_STATUSES` -- those are permanent/legitimate terminal states, not
transient failures a bigger timeout would fix.

**Verified directly** with a synthetic 3-model cache (2 measured, 1
timeout): confirmed the timeout entry is excluded from the "done" set (so
it gets reprocessed) while the two measured ones are correctly left alone,
then confirmed that appending a new successful result for the retried model
makes `load_cache()` report it as measured with the new score, not the old
failure.

**Practical effect:** the test-generation-comparison baseline run (186/200 measured, 14
timeouts at the 900s default) no longer needs a separate retry report --
just re-run the identical command with `--overall-timeout 1800`, and the
same `test_generation_baseline_mutation` report becomes complete in place.

---

## 2026-10-01 — Built and validated `generate_behavioral_tests.py`: +7.5 points mutation score on model_1, reproducibly

**Built the targeted fix for category 2 of the surviving-mutant diagnosis**
(the "both ends independently" gap, not the unkillable stub-class category).
`scripts/generate_behavioral_tests.py` is a copy of
`generate_structural_tests.py` (the original is never modified) trimmed down
to emit *only* the one new kind of test this diagnosis found missing: for
each binary association where **both** ends independently implement a real
`@property` setter (reusing the existing `_has_real_property()` check), one
`test_{assoc}_reverse_link_reassign_clear` test that calls the *other* end's
setter directly -- two different values, reassign, clear -- instead of only
ever observing that side as a side effect of the first end's setter, as
`test_structural_full.py`'s existing forward-direction test does. Writes
`test_behavioral.py` per model. Note: requires the `besser` package, which
lives in `.venv-puml`, not the main `.venv` (same as the original generator
-- found while smoke-testing).

**Smoke-tested end-to-end on a scratch copy of `model_1`** (never the real
dataset): generated exactly 1 test
(`test_assoc_nodes0_reverse_link_reassign_clear`), correctly skipping the
other 5 associations in that model (all link to the `petrinet_Arc` stub,
correctly matching the earlier equivalent-mutant finding -- the generator
doesn't waste a test on something that can't help). Passed standalone (1
test) and merged with the real `test_combined.py` (41 tests, all pass).

**Empirically validated a real, reproducible improvement**, using the now-
fixed, reproducible mutation pipeline (see the `cap_mutants` fix above):
merged the generated test into a scratch copy of `test_combined.py` and
re-ran the identical 40-mutant set (confirmed identical via the content-
sorted cap fix) -- **35% -> 42.5% mutation score (14 -> 17 killed)**, and
the specific mutant originally traced in the diagnosis (line 96) is
confirmed no longer surviving. This is the first concrete, measured,
reproducible evidence in this test-generation comparison that a generator/library approach can
actually move a model's mutation score, not just a traced mechanism in
theory.

**Not yet done:** running this across the full 200-model Stage 1 sample, or
merging its output into `test_combined.py` for a "super suite" (that's Step
3, pending the other three Stage 1 legs too). One model's result (even a
positive one) doesn't establish how much this generalizes -- most models
won't have model_1's specific mix of one real bidirectional association
alongside several stub-linked ones.

---

## 2026-10-01 — Root-caused the run-to-run mutation-score noise: a real bug in `cap_mutants()`, not (mainly) Hypothesis randomness -- fixed in both validators

**Started by testing the "both-ends" fix from the surviving-mutant diagnosis
directly.** Added one hand-written test to a scratch copy of `model_1`'s
`test_combined.py` that calls the `petrinet_Node.petrinet_Node` setter
**directly, from both ends, with two different real values** (rather than
relying on the reciprocal side firing only as a side effect of the other
class's setter, as the existing `link_reassign_clear` test does).
Sanity-checked it passes against the real code first, then re-ran the
cosmic-ray setup with it added: the exact mutant traced in the diagnosis
(`def: petrinet_Node`, line 96, `ReplaceComparisonOperator_IsNot_Is`) was
**confirmed absent from the survivor list** -- the "call both ends
independently" fix mechanism works exactly as diagnosed.

**But the aggregate kill count didn't move in a way that confirmed it,
leading to a much bigger discovery.** Re-running the **completely
unmodified** baseline (no new test, nothing changed) gave three different
kill counts across three separate runs (10, 9, 13 killed out of 40). Initial
hypothesis was Hypothesis's own unseeded `@given` randomness. Tested that
theory directly with `--hypothesis-seed=0` (newly added to both validators,
see below) -- **still got different counts (12, then 13)**, ruling out
Hypothesis alone as the explanation. Tested `PYTHONHASHSEED` next (affects
`set()` iteration order, relevant since this dataset's associations are
set-heavy) -- **also insufficient on its own.**

**Real root cause, found by checking whether `cap_mutants()` even selects
the same mutants twice:** it doesn't. Ran `cosmic-ray init` + the existing
`scope_to_properties()`/`cap_mutants()` pipeline twice, back to back, on the
*identical* source file, and compared the resulting 40-mutant sets by
content (operator + position + occurrence) rather than by `job_id`: **27 of
40 differed between the two runs**, despite `cap_mutants(seed_key=model_name)`
being a fixed seed. Root cause: `cap_mutants()` samples via
`random.Random(seed_key).sample(job_ids, max_mutants)`, which is
**positional** -- it picks indices into whatever order `SELECT job_id FROM
mutation_specs` happens to return, with no `ORDER BY`. Confirmed cosmic-ray
does **not** guarantee that row order is stable across separate `init` runs
on the same file (likely due to its own internal mutant-discovery process,
not something this project controls) -- so the same seed, applied to a
differently-ordered list each time, deterministically picks a *different*
set of mutants. The `seed_key` was never actually making mutant selection
reproducible, for any model, in any run, across this entire project,
whenever capping kicked in (`total_mutants_generated > max_mutants` --
the common case, since the default cap is 40).

**Fix, verified, applied to both `validate_mutation.py` and
`validate_mutation_properties.py`'s `cap_mutants()`:** fetch each mutant's
content (operator, start/end position, occurrence) alongside its `job_id`,
sort by that content *before* building the list `random.sample()` draws
from, so the order is deterministic regardless of whatever order cosmic-ray
happened to insert rows in. Verified directly: the same stable-sort-then-
sample logic produced **identical mutant sets across two separate `init`
runs** (0 differences). Then verified the fix at the `validate_model()`
level: **3 consecutive runs of the real function against `model_1`, with
the fix applied and no Hypothesis seed at all, gave identical results every
time** (14 killed / 26 survived / 0.35 score, all three runs) -- confirming
the `cap_mutants` bug was the dominant cause, not Hypothesis randomness
(`--hypothesis-seed` is still available as a new opt-in flag on both
scripts, since it's cheap insurance and may matter more on models with
heavier property-based test content, but it is not what made this
reproducible here).

**This is a bigger finding than "today's noise" -- it's retroactive.**
Every mutation score this project has ever computed, for every model where
capping applied, was drawn from a non-reproducible random subset of that
model's possible mutants -- not wrong in the sense of being miscounted, but
not the single stable number the `seed_key` mechanism was always intended
to produce. Aggregate statistics across thousands of models are still a
legitimate sample of outcomes and not invalidated by this, but **no
individual historical model score should be treated as exactly
reproducible** if re-measured today. Confirms and sharpens the earlier
"TODO: redo for every model" note -- the full-dataset re-run that was always
going to be needed eventually now has a concrete, verified fix behind it,
not just a seed flag. **Not yet scheduled**; the 200-model test-generation-comparison sample
work going forward uses the fixed scripts, but the existing full-dataset
reports are not being retroactively recomputed as part of this entry.

---

## 2026-10-01 — A 4th Track A approach (behavioral tests), and staging the comparison in two parts

**Reframing, worked out with the user: "structural" vs. "behavioral" tests
is the precise name for the gap Pynguin/CrossHair both hit.**
`generate_structural_tests.py` is not incorrect -- it correctly implements a
**structural** test: construct an object, make one call, check the
resulting snapshot. That's a real, necessary check, and it works. But this
dataset's actual logic (the bidirectional-association setter guard,
`if self._x is not None: self._x._y.remove(self)`) is a **behavioral**
property -- it's defined in terms of what should happen on a state
*transition* (replacing an existing value), which is structurally invisible
to any test that only ever calls the setter once from a fresh instance. No
amount of improving a single-snapshot test (ours, Pynguin's, or CrossHair's)
can reach it; what's needed is a test that calls the setter **twice, with
two different real values**, so the guarded branch actually executes and a
mutation to it becomes observable. This explains, after the fact, exactly
why both Pynguin and CrossHair struggled on this dataset's dominant pattern
today -- they're both fundamentally single-call/return-value-oriented tools.

**Decision: add a 4th Track A approach, not just two.** A new,
purpose-built generator, `scripts/generate_behavioral_tests.py`, will be a
**copy** of `generate_structural_tests.py` (the original is never modified
-- `test_structural_full.py` stays exactly as it is, still correct for what
it checks), producing a new `test_behavioral.py` per model that calls each
bidirectional-association setter twice with two different values. Not yet
built.

**Decision: stage the comparison in two parts, don't wait on Track B.** The
colleague's LLM track isn't expected soon. Rather than block all comparison
work on his timeline, Stage 1 compares the four things fully within this
session's control (baseline `test_combined.py`, Pynguin, CrossHair,
behavioral) first; Stage 2 re-runs the comparison as the real 5-way result
once his results exist. The "library vs. LLM" framing for the thesis still
refers to Stage 2, not Stage 1 alone -- Stage 1 is useful groundwork
(confirms whether any library-side approach helps at all) but isn't the
final answer by itself.

---

## 2026-10-01 — UTBotPython dropped from Track A: no native-Windows path exists

**Decided with the user, same day as the CrossHair property-targeting
findings (see below).** After Pynguin and CrossHair were both smoke-tested
and found to have real, if different, limitations on this dataset's
property-heavy code, investigated whether UTBotPython's actual CLI
component (`utbot-cli-python`, inside the `UnitTestBot/UTBotJava` source
repo -- not just the IntelliJ plugin) could run natively here.

**Finding: no documented native-Windows path exists at all.**
`utbot-cli-python` ships with its own dedicated `Dockerfile`
(`azul/zulu-openjdk:11.0.15` base image, Linux, apt-installed **Python
3.9** specifically -- not this project's 3.11) -- Docker is the only route
the tool's own source provides, not an extra-cautious choice by an academic
competition wrapper (an earlier check of the `UTBotPythonSBFT2024`
competition repo had already surfaced a "Linux + JDK17 + glibc>=2.31"
requirement, which this confirms is inherited from the real tool, not
wrapper-specific over-caution).

**Checked this machine's actual capability before deciding anything:** Java
is already installed (`java -version` → JDK 25 default on PATH, JDK 11 also
present separately -- satisfies the JVM requirement on its own). Docker is
installed (`docker --version` → 29.4.2) but its daemon isn't currently
running (`docker ps` fails to connect to the named pipe).

**Decision: drop UTBotPython, Track A is Pynguin + CrossHair only.**
Weighed starting Docker Desktop and building/running the official image
(technically available) against the realistic payoff: UTBotPython is
fundamentally the same *category* of tool as CrossHair -- symbolic
execution, here combined with fuzzing -- and CrossHair had already hit a
hard structural wall on this exact dataset shape (cannot target `@property`
getters/setters at all, see below). Running a third symbolic-execution-
family tool through an extra Docker+JVM+pinned-Python-3.9 layer for a likely
similar result didn't justify the added setup cost and fragility. This also
supersedes the "three libraries" part of the 2026-10-01 library-choice entry
below -- the reasoning for choosing Pynguin/CrossHair and rejecting the
Hypothesis-based option there still stands.

---

## 2026-10-01 — Pynguin installed and smoke-tested: isolated-venv incident, and a real assertion-budget gotcha

**Incident: installing Pynguin/CrossHair directly into the main `.venv`
silently changed shared dependencies.** `pip install pynguin crosshair-tool`
downgraded `pytest` 9.1.1→8.4.2 and bumped `setuptools` 68.2.2→80.10.2,
`Jinja2` 3.1.2→3.1.6, `rich` 15.0.0→14.3.4. This matters because
`validate_mutation.py`/`validate_mutation_properties.py` invoke `pytest` as
a subprocess for every one of this session's 8,000+ model mutation-testing
runs -- changing it retroactively affects reproducibility of any future
re-run, even though already-saved reports are unaffected. **Fixed:**
uninstalled the new packages, reinstalled the exact prior pinned versions of
the four affected packages, verified via `pip list` that the main venv
matches its pre-incident state exactly. **Going forward:** Track A tooling
lives in a new, separate `.venv-testgen`, never the main `.venv` -- mirrors
the project's existing convention of purpose-specific venvs (`.venv-puml`
already existed for a different purpose). (Separately noted, not caused by
this work: the main venv already had a pre-existing, unrelated dependency
conflict -- a package called `bocl` pins `pytest==7.4.0`/`setuptools==68.2.2`/
etc. and requires a `besser` package that isn't installed at all; this
predates today's session and wasn't introduced or worsened by this fix.)

**Pynguin requires `PYNGUIN_DANGER_AWARE=1` to run at all** -- it executes
the module under test with its generated inputs, and the maintainers'
official recommendation is to run it inside Docker for isolation (the env
var is set automatically there). Decided with the user to run natively
instead and set the var explicitly: this dataset's generated code has shown
zero file I/O, network, or subprocess behavior anywhere across this entire
session (confirmed again on `model_1`: only stdlib `datetime`/`abc`
imports), so the realistic risk is low, though not a hard guarantee the way
Docker isolation would be.

**Real finding: default settings produce isinstance-only assertions on this
dataset's code, same weak pattern as our own generators -- but it's fixable,
not a dead end.** Smoke-tested against a scratch copy of `model_1` (never
the real `Dataset/` tree, same safety convention as the mutation scripts).
With `--maximum_search_time 30` or `90` and the default
`--maximum_mutation_time -1` ("unlimited"), **100% of generated assertions
were `isinstance()` checks** -- zero value assertions, despite Pynguin's
default assertion generator already being `MUTATION_ANALYSIS` (which is
supposed to trace object-attribute/return-value changes across internally-
generated mutants and assert on whatever differs). Root-caused this to two
compounding factors: (1) `model_1` has **zero plain "operation" methods** --
every method is `__init__` or a property getter/setter (confirmed via
`grep`), the same "almost all real logic lives in property setters, not
callable operations" shape documented earlier this project (see the
mutation-score root-cause discussion below); (2) the default `-1` mutation-
time budget appears to get starved by the overall time budget in practice,
rather than genuinely running until done. **Fix: pass
`--maximum_mutation_time` explicitly** (tried `120`) rather than trusting
the default. With that change, Pynguin's internal mutation-analysis pass
measurably ran (236 internally-generated mutants, 35 killed, self-reported
`MutationScore=0.1549` via `--output_variables ... NumberOfCreatedMutants
NumberOfKilledMutants MutationScore` and `--report_dir`), and **one real
value assertion appeared** in the exported test file:
`assert var_3.petrinet_Node == pytest.approx(-2204.94, abs=0.01, rel=0.01)`
(alongside 26 still-isinstance-only ones). Modest yield for a single short
run against one of the dataset's more property-heavy models, but confirms
the mechanism works end-to-end here. **Takeaway for the real Track A sample
run: always pass an explicit `--maximum_mutation_time`, never rely on the
`-1` default.** Per-model time budget for the real 200-model run not yet
decided.

**CrossHair smoke-tested next, same scratch copy of `model_1`: works, but a
different and more awkward limitation than Pynguin's.** `crosshair cover`
produces valid pytest-stub output, but whole-file targeting
(`crosshair cover python_code.py`) only ever covers **one representative
class/method**, never all of them -- tried defaults, `-v
--max_uninteresting_iterations 20`, and `--per_condition_timeout 3`; all
three stopped at exactly 1 test (`petrinet_Petrinet.__init__`), never
reaching the file's other 5 classes. Explicitly ruled out "it just needs
more wall-clock time": a 300-second run with default settings finished on
its own in 6 seconds with the identical single result, so this is how
whole-file targeting behaves, not a budget shortfall. That one assertion is
also useless on its own terms: `assert petrinet_Petrinet.__init__(...) ==
None` is trivially true for any constructor regardless of what it did
internally (`__init__` always returns `None`) -- the same root cause as
Pynguin's weak spot, restated for a different engine: this dataset's logic
lives in property *setters* (state mutation, no return value), and
`cover`'s whole design is built around asserting on function *return
values*. Confirmed class-level targeting is required and still inconsistent:
`crosshair cover python_code.petrinet_Node` (the ABC base class) produced
zero tests, and `crosshair cover python_code.petrinet_Arc` (a different
concrete class) failed outright ("No functions or methods found", exit code
2) -- likely because that class has no `__init__` of its own, only an
inherited one, and CrossHair only examines methods defined directly on the
targeted class. **Integration implication for the real sample run:**
CrossHair probably needs one invocation **per class** (or per `has_logic`
method), not one per model file the way Pynguin works -- a materially
higher invocation count across 200 models, each paying its own process-
startup/SMT-exploration overhead. Not yet tried: targeting a property
*getter* directly, since getters do have a real return value (unlike
setters/`__init__`) and may be the structurally correct way to point
CrossHair at this dataset's code.

**Tried targeting a property getter directly (the structurally "correct"
CrossHair target, since getters DO return a value) -- a hard no, not a
tuning problem.** `crosshair cover python_code.py:21` (the `name` getter's
`def` line, confirmed correct via `grep`) failed outright: "Cannot find a
function or method on line 21." The dotted-path form,
`crosshair cover python_code.petrinet_Node.name`, silently found nothing at
all -- no error, no output. Root cause: CrossHair's target lookup expects a
plain callable; a `@property`-decorated attribute resolves to a descriptor
object through Python's own introspection machinery, not a directly-callable
function, so CrossHair's lookup genuinely cannot see it as a target. This is
a hard capability gap in the tool, not something a longer budget or
different flag would fix.

**Checked whether a Python library exists specifically for getter/setter
round-trip testing** (the user's instinct: Java has OpenPojo/pojo-tester,
which test exactly this pattern via reflection -- surely Python has
something similar?). **Researched and confirmed: no direct equivalent
exists.** `classtools-autocode` *generates* getters/setters, it doesn't test
them; "Sloth Test" builds regression tests from observed real execution
traces, not property round-trips -- neither is actually the same tool
category. The property-based options found earlier (Hypothesis Ghostwriter,
icontract-hypothesis) were already ruled out 2026-10-01 for being "fuzzy."

**Conclusion, combining today's two findings:** neither Pynguin
(isinstance-only on setters) nor CrossHair (can't even target properties) --
nor any known off-the-shelf Python library -- can meaningfully test this
dataset's getter/setter bulk, which is most of its code. The one proven,
actually-available lever for that part remains what was already identified
months ago (see the mutation-score root-cause discussion below): varying
the concrete values `generate_structural_tests.py` uses per setter test,
instead of one hardcoded literal. **This reframes Track A's realistic
scope**: Pynguin/CrossHair are likely to matter for the smaller pool of
models/methods with genuine plain "operations" (actual computed logic), not
the property-heavy bulk every model shares.

UTBotPython not yet tested.

---

## 2026-10-01 — Test-generation comparison: library-track choice: Pynguin, CrossHair, UTBotPython (no Hypothesis-based option)

**Superseded later the same day** — see the "UTBotPython dropped" entry
above (newer entries are at the top of this file): after smoke-testing,
UTBotPython was dropped for lack of any native-Windows path. Track A is
**Pynguin + CrossHair only.** The reasoning below for *why* Pynguin/CrossHair
were chosen, and why the Hypothesis-based option was rejected, still stands
unchanged; only the UTBotPython part of this entry is no longer current.

**Decided with the user and their colleagues.** Track A (the library-
generated-tests side of the library-vs-LLM comparison, see Step 2 below)
will use exactly three tools: **Pynguin, CrossHair, and UTBotPython.** No
optional/control variant is included.

**Why the earlier "strengthened Hypothesis" control was dropped, not just
deprioritized:** the original test-generation-comparison plan (2026-09-28) included an optional
control — re-targeting the Hypothesis property-based library (`@given`,
already used in `test_hypothesis.py`) at `has_logic` methods with real value
assertions instead of `isinstance`-only checks. The user and colleagues
discussed this and rejected it: property-based, randomly-generated-input
testing feels "fuzzy" for the purpose of this specific comparison — they
want tests that exercise a method's actual logic directly, with concrete
inputs and concrete assertions, the way a human would hand-write a test
case. All three chosen tools produce exactly that (plain pytest-style
functions with literal inputs/assertions), unlike Hypothesis's generated
strategies. For the same reason, **Hypothesis Ghostwriter** and
**icontract-hypothesis** (found while researching alternatives, both
effectively free since they only need type hints, no new dependency burden)
were also considered and set aside — both are still property-based/
generated-input in character under the hood, just with a different strategy
source (type hints/contracts instead of manual `@given` annotations).

**Why these three specifically, researched 2026-09-30/10-01** after the
user noted a plain web search for Python test generators surfaces almost
nothing but Pynguin:

- **Pynguin** — search-based (genetic/evolutionary, DynaMOSA algorithm),
  explicitly optimizes for coverage/fault-detection as its fitness function,
  needs no prior knowledge of what's wrong with the code. Reference
  supplied by the user: Lukasczyk, S.; Fraser, G. "Pynguin: Automated Unit
  Test Generation for Python." *ICSE 2022 Companion*.
  [10.1145/3510454.3516829](https://dl.acm.org/doi/10.1145/3510454.3516829).
- **CrossHair** — symbolic execution; finds concrete counterexamples that
  violate an assertion. Directly targets the edge cases (empty string,
  boundary numbers, `None`) already identified as the gap in this dataset's
  existing tests (see the "why is mutation score low" discussion,
  2026-09-17/18 below).
- **UTBotPython** — symbolic execution + feedback-guided ("smart") fuzzing,
  from JetBrains' UnitTestBot project. Chosen as the third candidate because
  it's a genuine, independently-verified peer to Pynguin, not just something
  found on a blog: it was one of only 4 tools in the most recent academic
  head-to-head of Python test generators, SBFT Tool Competition 2024
  (alongside Pynguin, Hypothesis Ghostwriter, and Klara), uses an
  architecturally distinct technique from both Pynguin (search-based) and
  CrossHair (pure symbolic execution, no fuzzing component), and is actively
  maintained. Reference: Eghbali, A. et al. "SBFT Tool Competition 2024 --
  Python Test Case Generation Track." [arXiv:2401.15189](https://arxiv.org/abs/2401.15189);
  repo: [github.com/UnitTestBot](https://github.com/UnitTestBot).
- **Klara ruled out**: also in the SBFT 2024 competition, but its last
  release was 2021 and its own documentation states it doesn't support
  loops or comprehensions — a dealbreaker given how many of this dataset's
  `has_logic` methods involve exactly those constructs.

**Not yet started:** none of the three tools are installed yet. Next step
is checking each one actually runs against this dataset's generated Python
code (version compatibility, whether any can be scoped to specific methods
rather than a whole file) before committing compute time to a full Track A
run on the 200-model sample.

---

## 2026-09-29 — Test-generation comparison sample methodology: stratify by has_logic count, not difficulty_score; equal allocation, size 200

**Superseded decision:** the original test-generation-comparison plan (first
written 2026-09-28) said the shared Track A/B sample should be "stratified
by `difficulty_score`." Discussed with the user and changed this after
`classify_method_logic.py`'s results made a concrete problem visible:
`difficulty_score` and `has_logic` method count don't always move together.
`model_2023` (the 932-class metamodel used elsewhere as a difficulty-score
example) scores **86.66/100** on `difficulty_score` — one of the hardest
models in the dataset — but has **zero methods at all** (`methods = 0` in
its raw structural fields). It would be a completely useless sample
member for this comparison despite looking "hard" by the old criterion, because
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

## 2026-09-29 — Test-generation comparison, step 1: per-method logic classification (`classify_method_logic.py`), and the surviving-mutant export prerequisite

**Why:** this test-generation comparison (raising mutation score) needs to target
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
which is the test-generation-comparison sample-eligibility number; the remaining 11.9% (992
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
method and are eligible for this comparison's sample; the **992 (11.9%)** with zero
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
comparison's sample so it isn't accidentally padded with near-duplicate twins.

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
activates when explicitly passed for this comparison's sample run. Verified against
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
