# Next session: evaluate test coverage & mutation testing for the dataset

## Context

This repo (`BESSER-Dataset`) contains ~9,082 model directories under `Dataset/`
(e.g. `Dataset/model_1/`). Each model directory has, among other files:

- `python_code.py` — a generated Python implementation of a B-UML model
  (classes, properties, bidirectional associations, operations).
- `test_hypothesis.py` — a generated pytest + Hypothesis test suite that
  imports from `python_code.py` and exercises the generated classes
  (structural checks + `@given`-based property tests).
- `code_metadata.json` — per-model metadata, now including:
  - `python_code_validation` — from `scripts/validate_python_code.py`:
    does `python_code.py` compile and run standalone?
  - `test_validation` — from `scripts/validate_tests.py`: does
    `test_hypothesis.py` collect and pass under pytest?
- `metadata.txt`, `category.txt`, `model_path.txt`, `README.md`,
  `textualDescription.txt`, an `image.gv.png`, and a `Java/` folder with a
  Java rendering of the same model.

Two prior sessions already built dataset-wide validators, both following the
same shape (subprocess-per-model, parallel workers, results merged into
`code_metadata.json`, aggregate report under `reports/`):

- `scripts/validate_python_code.py` → `reports/python_code_validation_report.{json,md}`
  — 9,064/9,082 (99.80%) of `python_code.py` files compile & run cleanly.
- `scripts/validate_tests.py` → `reports/test_validation_report.{json,md}`
  — 8,027/9,082 (88.38%) of `test_hypothesis.py` suites fully pass.
  **Key finding:** of the 1,055 failing models, 919 fail with
  `AssertionError`, and 907 of those are because the generated model code has
  operations with empty/stubbed bodies (just `pass`) that the paired
  generated test asserts should change object state. This is a real gap in
  the generated code, not flaky tests — keep it in mind below, since methods
  with empty bodies are trivially "coverable" but not meaningfully mutable.

Read both report `.md` files before starting — they contain the full picture
of what currently passes/fails and why.

## The task

The user wants to know, for each model's test suite:

1. **Test coverage** — how much of `python_code.py` does `test_hypothesis.py`
   actually exercise (line/branch coverage)?
2. **Mutation score** — of the code that *is* covered, how much of it is
   actually meaningfully tested (does the suite catch semantic changes), as
   opposed to just executing lines without asserting anything about them?

**Before writing any large-scale script or running anything across the full
9,082 models**, research current Python tooling for both measurements and
present the user with a short comparison + a concrete recommendation. Do not
unilaterally pick a tool and run it dataset-wide — this is an explicit
ask-then-build task.

### Coverage

`coverage.py` (with `pytest-cov` for pytest integration) is the standard
choice and there isn't much real competition here — but verify current
version/maintenance status before assuming.

### Mutation testing — shortlist to verify and compare

These were reasonable options as of this writing; re-check PyPI/GitHub for
current maintenance status, since mutation-testing tooling in Python churns:

- **`mutmut`** — actively maintained, simple CLI, coverage-guided mutant
  skipping (won't waste time mutating uncovered lines), reasonable pytest
  integration.
- **`cosmic-ray`** — powerful and configurable, supports distributed
  execution, but has heavier per-project setup (a session/config file plus a
  sqlite results DB per run) — likely more overhead than needed for running
  against thousands of tiny independent single-file projects.
- **`mutatest`** — lightweight, AST-based, minimal configuration, built for
  quick single-package runs. Check whether it's still maintained; it hasn't
  always kept pace with newer Python versions.
- **`mutpy`** — largely unmaintained last time this was checked; likely skip
  unless the others don't pan out.

Weigh these specifically against this dataset's shape, not in the abstract:

- ~9,082 **independent, single-module** projects (one `python_code.py` +
  one `test_hypothesis.py` each), not one big codebase — whichever tool
  handles "many small isolated runs" most cheaply (low per-invocation
  overhead, no persistent session DB you have to manage per model) wins.
- Full-suite pytest runtime already ranges from well under 1s to ~60s+ per
  model (the largest `test_hypothesis.py` is 23,501 lines, in
  `model_2583`), and the full single-pass test-validation run across all
  9,082 models took on the order of an hour even without mutation testing.
  Mutation testing reruns the test suite once per surviving mutant, so a
  full-dataset run could easily be one or two orders of magnitude more
  expensive — budget and sampling strategy need to be part of the proposal
  to the user, not an afterthought.
- Hypothesis's `@given` tests are stochastic (default `max_examples=50`);
  for reproducible mutation scoring you likely want a fixed
  `HYPOTHESIS_SEED` or a `derandomize` profile so a mutant isn't
  "killed" or "survives" depending on random luck between runs.
- Many models have operations with empty (`pass`) bodies (see above) —
  decide how/whether to treat mutants in those bodies (there's nothing
  meaningful to mutate in a `pass` statement), so raw mutation scores may
  need to be reported alongside "coverable statements" counts to be
  interpretable.

### Suggested deliverable for this session

1. Confirm current state of the shortlisted libraries (versions, last
   release, open issues around Python 3.13 support), and add/drop
   candidates as warranted.
2. Present a short comparison table to the user and **recommend one tool**
   (coverage is basically decided; mutation testing is the real choice).
3. Get the user's go-ahead on the tool *and* on scope (e.g. "run on a
   sample of N models first" vs. "full dataset") before building anything
   that touches all 9,082 directories.
4. Once approved, prototype on a small sample (~20-50 models spanning small
   and large test suites) exactly like `scripts/validate_tests.py` was
   prototyped before its full run — measure real per-model timing before
   committing to a full-dataset design.
5. If/when scaled up, follow the existing pattern: a new
   `scripts/validate_coverage.py` and/or `scripts/validate_mutation.py`,
   subprocess-per-model, parallel workers, results merged into each model's
   `code_metadata.json` under new keys (e.g. `coverage_validation`,
   `mutation_validation`), plus an aggregate report under `reports/`.

## Environment / gotchas learned last session (avoid re-discovering these)

- Python 3.13.5, pytest 9.0.3 preinstalled; `hypothesis` was **not**
  preinstalled — `pip install hypothesis` was required to run the existing
  test suites at all. Coverage/mutation tools will need the same treatment.
- 8 physical cores available locally.
- Running pytest per model creates `.pytest_cache/` and Hypothesis creates
  `.hypothesis/` in the model's cwd unless suppressed. Use
  `-p no:cacheprovider` for pytest's cache, and set the
  `HYPOTHESIS_STORAGE_DIRECTORY` env var to a shared temp dir (cleaned up
  after the run) to keep Hypothesis's example database out of the dataset.
  `.pytest_cache/`, `.hypothesis/`, `__pycache__/`, and `*.pyc` are now
  gitignored as a backstop, but avoiding creating them in the first place is
  cleaner. Coverage tools have their own equivalent artifacts (`.coverage`,
  `htmlcov/`, mutation tools' own cache/DB files) — apply the same
  redirect-or-suppress treatment and gitignore anything that can't be
  avoided.
- `PYTHONDONTWRITEBYTECODE=1` avoids `__pycache__` littering from imports.
- **Don't launch a long parallel job via a heredoc passed to `python3 -`
  (stdin script) if it uses `multiprocessing`/`ProcessPoolExecutor`** — on
  macOS, the spawn start method re-imports `__main__` from its file path,
  and `<stdin>` isn't a real file, so every worker crashes immediately.
  Write the job to a real `.py` file and run that instead.
- **Don't background a long job by embedding `nohup ... &` inside the
  command string you pass to a `run_in_background` shell call** — the
  harness considers the *launcher* command finished the moment the shell
  returns (immediately, since `&` detaches), not when the actual work
  finishes, so you'll get a premature "completed" notification while the
  real process is still running. Instead, run the actual long command
  directly in the foreground of a `run_in_background: true` call (no manual
  `nohup`/`&`), so the harness tracks the real process and notifies you
  when it actually exits.
- When parsing pytest's stdout for summary counts, only parse the **last
  non-empty line** — a preceding `"Interrupted: N error(s) during
  collection"` banner line matches the same `"<N> <word>"` pattern and will
  double-count if you scan the last few lines instead of just the last one.
- Pytest truncates long assertion messages in its one-line `FAILED ... -
  <message>` summary format when stdout isn't a tty. Prefer parsing the
  full `E   <Type>: <message>` line(s) from the traceback body over the
  short-summary dash-message for readable error text.
