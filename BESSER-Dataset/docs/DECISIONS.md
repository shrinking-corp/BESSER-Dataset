# Decisions & findings log — coverage / mutation testing evaluation

Running log of non-trivial findings and decisions made while evaluating test
coverage and mutation testing for the dataset (see `PROMPT.md`). Newest
entries at the top. Each entry should stand alone enough to explain *why* a
decision was made, so we can backtrack later without re-deriving it.

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
