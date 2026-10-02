# Test-Generation Comparison Report (Stage 1)

*Generated 2026-10-02. Compares four approaches to raising mutation score on a
200-model sample, stratified by `has_logic` method count (see
`reports/test_generation_sample_report.md` for the sampling methodology):
our existing baseline (`test_combined.py`), two third-party libraries
(Pynguin, CrossHair), and a new, purpose-built generator (behavioral tests).
Every score in this report comes from this project's own
`validate_mutation_properties.py` (cosmic-ray, property-scoped, 40-mutant
cap, fixed Hypothesis seed), never a tool's self-reported number — so every
column is measured exactly the same way. Methodology notes:
`docs/DECISIONS.md` (2026-10-01/02 entries).*

## At a glance

| Approach | How it was generated | Models with ≥1 test | Measured how |
|---|---|---|---|
| **Baseline** | Existing `test_hypothesis.py` + `test_structural_full.py`, merged | 200/200 | Standalone |
| **Behavioral** | New: `scripts/generate_behavioral_tests.py`, merged into baseline | 153/200 | Baseline + addition |
| **Pynguin** | Search-based generation (`scripts/generate_pynguin_tests.py`) | 191/200 | Standalone (replaces baseline) |
| **CrossHair** | Symbolic execution (`scripts/generate_crosshair_tests.py`) | 177/200 | Standalone (replaces baseline) |

**Headline finding:** Behavioral and CrossHair both genuinely raise mutation
score on a fair comparison; Pynguin does not. See "Recommendation" below.

---

## 1. Why this comparison exists

Mutation score across every suite measured in this project has been stuck in
the 35–51% range. Earlier diagnosis (`docs/DECISIONS.md`, 2026-09-17/18 and
2026-10-01) found the root cause is mostly **weak assertions** — tests that
check an object was constructed with the right *type*, not that its values
or its bidirectional-association invariants actually hold — concentrated in
this dataset's dominant code pattern (property getter/setter pairs
maintaining two-way links between objects). This comparison tests four ways
to address that: two established third-party test-generation libraries, and
one small, purpose-built generator targeting the exact gap a real
surviving-mutant investigation found (see the "Real surviving-mutant
diagnosis on model_1" entry in `docs/DECISIONS.md`).

---

## 2. Headline results: raw standalone averages

| Approach | Measured | Avg mutation score |
|---|---:|---:|
| Baseline | 200/200 | 50.85% |
| Behavioral (baseline + addition) | 200/200 | **59.89%** |
| Pynguin (standalone) | 192/200 | 27.75% |
| CrossHair (standalone) | 177/200 | 65.05% |

Pynguin and CrossHair's rows are **not directly comparable to baseline's
full-200 figure** — they're standalone scores measured only on the subset
of models each tool could generate anything for at all (192 and 177
respectively, not 200). Comparing 65.05% directly against 50.85% would be
comparing two different populations of models, not a fair test of either
tool. Section 3 fixes this.

---

## 3. The fair comparison: same subset, both sides

For each tool, baseline's score is recomputed restricted to **exactly the
same models** that tool succeeded on — this is the real test of "does this
approach's output beat what we already have," not "does this tool's best
case beat our overall average."

| | Pynguin (192-model subset) | CrossHair (177-model subset) |
|---|---:|---:|
| Baseline, same models | 51.54% | 52.12% |
| Tool standalone, same models | 27.75% | **65.05%** |
| **Delta** | **−23.79 pts** | **+12.93 pts** |

**Pynguin loses badly, even on its own best-case subset.** Confirms the
root-cause diagnosis directly: Pynguin's default assertion generation
produces `isinstance()`-only checks on this dataset's property-heavy code
(see `docs/DECISIONS.md`, 2026-10-01, "Pynguin installed and smoke-tested"),
which is strictly weaker than what the existing baseline already does.

**CrossHair genuinely wins**, by a wide margin, on a fair head-to-head —
real evidence that symbolic execution produces a stronger test suite than
this project's current generator, on the subset of models where it can run
at all (one with ≥1 class that isn't purely property-only — see Section 5).

---

## 4. Per-model behavior: Behavioral never hurts, CrossHair is a mixed bag

Averages can hide a lot. Looking at how many *individual* models got
better, worse, or stayed the same tells a sharper story:

| | Improved | Worsened | Unchanged | Total |
|---|---:|---:|---:|---:|
| **Behavioral** vs. baseline | **110 (55.0%)** | **0 (0.0%)** | 90 (45.0%) | 200 |
| **CrossHair** vs. baseline (same subset) | 72 (40.7%) | 65 (36.7%) | 40 (22.6%) | 177 |

**Behavioral is monotonic — it never once made a model's score worse**,
across all 200 models. This follows directly from how it's measured: it's
an *addition* to the baseline, not a replacement, so the only possible
outcomes are "adds a test that kills an extra mutant" (improves) or "adds
nothing / adds a test that doesn't change the outcome" (unchanged). Among
the 110 models it did improve, the average gain was a substantial **+16.4
points**.

**CrossHair, measured standalone, is a real mixed bag per model** — on 65 of
177 models (36.7%), replacing the baseline with CrossHair's output actually
*lowers* mutation score, even though the overall average is higher. This is
the direct consequence of measuring it as a full replacement rather than an
addition: CrossHair's suite doesn't know what the baseline already tests, so
on some models it simply tests different (sometimes fewer, sometimes less
effective) things. This is the central argument for merging CrossHair into
the baseline rather than using it standalone (see Recommendation).

---

## 5. Generation reliability and coverage

Not every tool could produce output for every model:

| Approach | Generated for | No output at all | Why |
|---|---:|---:|---|
| Behavioral | 153/200 (76.5%) | 47/200 (23.5%) | No binary association in the model has *both* ends independently implementing a real `@property` setter — nothing for this generator to target. |
| Pynguin | 191/200 (95.5%) | 9/200 (4.5%) | Timeouts on the largest/most-complex models (277–1,016 total methods vs. a dataset median of ~43) — confirmed these are genuinely the hardest cases, not a bug. |
| CrossHair | 177/200 (88.5%) | 23/200 (11.5%) | No class in the model has its own `__init__` *and* isn't purely property-only — CrossHair's target resolution cannot reach `@property`-only classes at all (a hard capability gap, not a tuning issue — see `docs/DECISIONS.md`, 2026-10-01). |

Average tests generated, per model that got ≥1:

| Approach | Avg tests/model (generated subset) |
|---|---:|
| Behavioral | 25.8 (median 5.5; up to 224 on association-heavy models) |
| Pynguin | 27.9 |
| CrossHair | 24.9 |

---

## 6. Performance

Median (p50) / 90th-percentile (p90) / max wall-clock time per model,
property-scoped mutation measurement only (generation time not included —
Pynguin/CrossHair generation is a separate, one-time cost per model):

| Approach | p50 | p90 | max |
|---|---:|---:|---:|
| Baseline | 147.0s | 721.1s | 1,057.5s |
| Behavioral | 105.6s | 777.9s | 1,537.6s |
| Pynguin | 58.1s | 155.4s | 222.2s |
| CrossHair | 56.0s | 90.2s | 137.2s |

Pynguin's and CrossHair's own *measurement* runtimes are faster than
baseline's largely because their test suites are smaller/narrower (no
Hypothesis-driven `@given` tests with many examples per run); this isn't a
reflection of the tools' own generation cost, which is separate and, for
CrossHair in particular, was the reason per-class invocation (not
whole-file) was needed in the first place (see `docs/DECISIONS.md`).

---

## 7. Recommendation

**Combine Behavioral and CrossHair into the eventual super suite; drop
Pynguin.**

- **Behavioral**: deterministic, fully explainable (the exact mechanism was
  traced to a specific surviving mutant before being built), applies
  broadly (76.5% of models get ≥1 test), monotonically safe (never lowers a
  model's score), and cheap to run (pure AST analysis and code generation,
  no external tool, no SMT solving). Clear keep.
- **CrossHair**: the strongest raw per-model effect (+12.93 pts on a fair
  comparison) of any approach tested, real evidence symbolic execution
  reaches mutants the current generator misses. But it only covers 88.5% of
  models and, measured standalone, actively hurts over a third of the
  models it does cover — the fix is to **merge it into baseline the same
  way Behavioral was** (not yet done — see Open Items) rather than use it
  as a wholesale replacement, which should convert its real per-model
  wins into pure upside without the standalone downside.
- **Pynguin**: drop. Loses by −23.79 points even on its own best-case
  subset, with a root cause (weak, isinstance-only default assertions on
  this dataset's property-heavy code) that's architectural, not a tuning
  problem — already tested explicit `--maximum_mutation_time` budgets with
  only marginal, inconsistent improvement (see `docs/DECISIONS.md`,
  2026-10-01, "Pynguin installed and smoke-tested").

This isn't a forced choice between approaches — Behavioral and CrossHair
target different parts of the problem (bidirectional-association guard
logic vs. whatever CrossHair's symbolic execution happens to reach) and are
not mutually exclusive. The plan going forward is to combine whichever
approach(es) actually help into one final "super suite," which this result
directly supports doing for both of them.

---

## 8. Open items, not yet done

- **CrossHair has not been measured merged-with-baseline** — only
  standalone. Given Section 4's finding that standalone CrossHair actively
  hurts 36.7% of the models it covers, this is the single most important
  next measurement: does `baseline + CrossHair`'s tests (same treatment
  Behavioral got) convert CrossHair's real per-model wins into pure
  upside, the way the standalone-vs-additive comparison predicts it should?
- **A real, non-zero floor of unkillable (equivalent) mutants exists** in
  this dataset from asymmetric stub associations (one side of a
  bidirectional link is a bare `class X: pass`) — confirmed directly via
  surviving-mutant inspection on `model_1`. No approach tested here, or any
  conceivable test-writing approach, can close that gap. Worth keeping in
  mind when judging how close to 100% any future combined score could
  realistically get.
- **This is Stage 1 only.** Track B (the colleague's LLM-driven mutation-
  feedback loop) is still pending, not expected soon. This report will be
  re-run as a 5-way comparison once his results exist.
- **The reproducibility fixes behind these numbers are new, from this same
  investigation** — the `cap_mutants()` row-order bug (every prior mutation
  score in this project, not just this comparison, was affected whenever
  capping applied) and the venv-rename-breaks-console-scripts bug (CrossHair
  specifically). Both are fixed and verified; see `docs/DECISIONS.md`,
  2026-10-01.

---

## Source reports

| Report | Scope | Files |
|---|---|---|
| Sample selection | 200/9,082 | `test_generation_sample.{txt,report.json,report.md}` |
| Baseline mutation | 200 sample | `test_generation_baseline_mutation.{json,md}` |
| Behavioral generation | 200 sample | `behavioral_tests_report.{json,md}` |
| Behavioral+baseline merge | 200 sample | `combined_plus_behavioral_report.{json,md}` |
| Behavioral mutation | 200 sample | `test_generation_behavioral_mutation.{json,md}` |
| Pynguin generation | 200 sample | `pynguin_generation_report.{json,md}` (summary `.json` may lag the cache after late retries — `.cache.jsonl` is authoritative) |
| Pynguin mutation | 200 sample | `test_generation_pynguin_mutation.{json,md}` |
| CrossHair generation | 200 sample | `crosshair_generation_report.{json,md}` |
| CrossHair mutation | 200 sample | `test_generation_crosshair_mutation.{json,md}` |

See `docs/DECISIONS.md` (2026-10-01/02 entries) for the full methodology
discussion, including why `--hypothesis-seed` and the `cap_mutants()` fix
were necessary for these numbers to be trustworthy at all, and the full
surviving-mutant trace that motivated building the Behavioral generator.
