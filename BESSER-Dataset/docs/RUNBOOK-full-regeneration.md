# Runbook — full regeneration on the 5,264 unique models

The pipeline validated on the 200-model sample (docs/DECISIONS.md, 2026-10-18),
run on every model in `reports/unique_models.txt`. Run from the repo root in
PowerShell. Every step writes a resumable cache under its `--report-name`:
if a run is interrupted, rerun the same command and it continues.

All report names start with `full_` so the sample's published reports
(`super_suite_report`, `test_generation_super_suite_mutation_v3`, …) are never
overwritten.

`--workers` defaults to 8 (CrossHair: 4). Set it to the machine's cores.

## 0. Before starting

Commit everything first. Afterwards `git status` then shows exactly which
files the regeneration changed.

```powershell
& .\.venv\Scripts\python.exe scripts\check_pipeline_status.py
& .\.venv\Scripts\python.exe _scratch\check_sample_vs_unique.py
```

`check_pipeline_status.py` has to end with `OK -- inputs complete`.
- Expected output counts: `test_structural_full.py` / `test_combined.py`
  present for (almost) every model, and `test_behavioral.py` /
  `test_crosshair.py` / `test_super_suite.py` / `test_combined_green.py` only
  for about the 200 sample models.
- If `test_structural_full.py` or `test_combined.py` show any missing or
  stale models, run step 3 first. Otherwise skip it.

Rerun `check_pipeline_status.py` after each step, adding
`--since <time the step started>`. The step's file must show `written since`
equal to `present`, and `stale` must be 0.

## 1. Difficulty score refit (minutes, no test files needed)

```powershell
& .\.venv\Scripts\python.exe scripts\compute_difficulty_score.py --models-file reports\unique_models.txt
& .\.venv\Scripts\python.exe scripts\experiment_difficulty_score_pca.py --models-file reports\unique_models.txt
& .\.venv\Scripts\python.exe scripts\compare_difficulty_scores.py --models-file reports\unique_models.txt
& .\.venv\Scripts\python.exe scripts\difficulty_score_distribution.py --models-file reports\unique_models.txt
```

- The warning that 3,072 models outside the list keep an old score is
  expected. Those are the copies, and no later step reads them.
- These reports overwrite the 8,336-model versions, which stay in git history.
- Recheck experiment 6 (the PC1+PC2 vs PC1+PC2+PC3 argument) and the
  retention table against the DECISIONS entry.

## 2. Behavioral tests (fixed generator, deterministic)

```powershell
& .\.venv-puml\Scripts\python.exe scripts\generate_behavioral_tests.py --models-file reports\unique_models.txt --report-name full_behavioral_tests
```

## 3. Only if step 0 showed missing/stale structural or combined tests

```powershell
& .\.venv-puml\Scripts\python.exe scripts\generate_structural_tests.py --models-file reports\unique_models.txt --report-name full_structural_tests
& .\.venv\Scripts\python.exe scripts\generate_combined_tests.py --models-file reports\unique_models.txt --report-name full_combined_tests
```

## 4. CrossHair tests (the slow generation step)

The sample models keep the `test_crosshair.py` their published results were
measured with. CrossHair is not deterministic, so regenerating them would
make the +43-point result impossible to reproduce from the files. Every other
model is generated with the same default settings as the sample (per class 30 s,
per condition 5 s, at most 300 s per model).

```powershell
$s = Get-Content reports\test_generation_sample.txt
Get-Content reports\unique_models.txt | ? { $s -notcontains $_ } | Set-Content -Encoding utf8 _scratch\crosshair_todo.txt
& .\.venv\Scripts\python.exe scripts\generate_crosshair_tests.py --models-file _scratch\crosshair_todo.txt --report-name full_crosshair --limit 100
```

Check the pilot's report (`reports\full_crosshair.md`) and how long it took.
Then run the same command without `--limit 100`; it continues from the cache.
- Every rerun also retries all `no_tests_generated` models. That is
  expected for a model whose classes have only properties, and wastes time,
  so don't rerun without a reason.
- Steps 2 and 4 are independent and can run at the same time if the machine
  has the cores.

## 5. Super suite (green, the benchmark's test oracle)

```powershell
& .\.venv\Scripts\python.exe scripts\generate_super_suite.py --models-file reports\unique_models.txt --report-name full_super_suite
```

- A model whose suite can't be made green gets no `test_super_suite.py`, and
  the split drops it later (`--require-file`).
- Note the counts by status, and the number of removed tests, for the write-up.

## 6. Green baseline

```powershell
& .\.venv\Scripts\python.exe scripts\make_green_suite.py --test-file test_combined.py --models-file reports\unique_models.txt --report-name full_green_test_combined
```

## 7. Mutation score: super suite and baseline (the expensive step)

Same settings as the sample: property-scoped, 40 mutants per model,
`--hypothesis-seed 0`, baseline guard on. Pilot first, then the full run
from the cache, then a retry of the timeouts at double the cap (this
recovered all 15 timeouts in the sample).

```powershell
& .\.venv\Scripts\python.exe scripts\validate_mutation_properties.py --models-file reports\unique_models.txt --test-file test_super_suite.py --hypothesis-seed 0 --report-name full_super_suite_mutation --write-metadata --limit 100
```

Then the same command without `--limit 100`, then again with
`--overall-timeout 1800`. The baseline uses the same three runs:

```powershell
& .\.venv\Scripts\python.exe scripts\validate_mutation_properties.py --models-file reports\unique_models.txt --test-file test_combined_green.py --metadata-key combined_green_mutation_validation_properties --hypothesis-seed 0 --report-name full_baseline_green_mutation --write-metadata --limit 100
```

`baseline_failed` should be 0 in both reports, because both suites are green.
If it isn't, stop and look at those models before continuing.

**Run the two mutation jobs one after the other, never alongside each other
or any other heavy job.** cosmic-ray counts a mutant whose test run exceeds
the per-mutant timeout (90 s) as KILLED (`cosmic_ray/testing.py`). On an
overloaded machine a slow run can therefore turn into a fake kill. The
report shows these as "Kills that were only a per-mutant timeout"; if that
number is more than a handful, rerun the affected models on an idle machine.
Keep `--workers` at least two below the core count.

## 8. Split and export (after the train ratio is agreed)

This step only needs step 5 (the super suite), so the export can be handed
over while step 7 is still running. What goes into the export is set in
`benchmark_export.toml`: enable the mutation-score item there once step 7
is done, then export again.

```powershell
& .\.venv\Scripts\python.exe scripts\make_benchmark_split.py --train-ratio <ratio> --require-file test_super_suite.py
& .\.venv\Scripts\python.exe scripts\export_benchmark_dataset.py --output-dir <folder outside Dataset>
```

## Cost estimate (from the sample, rough)

- **Mutation.** The 200 sample models took 57,700 worker-seconds (p50 150 s,
  mean 288 s per model). The sample over-represents large models, so the true
  average is lower. For 5,264 models that is about 220–420 worker-hours per
  suite, i.e. 1–2 days at 8 workers or about 9–18 hours at 24. The baseline
  suite is smaller, so it should be faster.
- **CrossHair.** At most 300 s per model, so at most ~100 hours at 4 workers;
  the pilot gives the real rate.
- The pilots (`--limit 100`) take the first 100 models in list order, not a
  random sample. Use them to confirm a step works and to get a rough rate,
  not as an exact estimate.
