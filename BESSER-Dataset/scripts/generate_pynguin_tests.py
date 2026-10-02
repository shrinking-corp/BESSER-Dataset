#!/usr/bin/env python3
"""Generate `test_pynguin.py` per model using Pynguin (search-based test
generation), for the library track of the test-generation comparison.

Runs Pynguin in a scratch copy, never the real `Dataset/` tree (Pynguin
executes the module under test with generated inputs -- same scratch-copy
safety convention as `validate_mutation.py`, not specific to Pynguin, but
doubly warranted here since Pynguin's own docs flag this as a reason to
sandbox at all).

Two things found while smoke-testing Pynguin against this dataset's code
(see docs/DECISIONS.md, 2026-10-01) are baked in here, not optional:

1. **`PYNGUIN_DANGER_AWARE=1` is required** -- Pynguin refuses to run
   otherwise, since it executes the module under test with generated
   inputs. Decided (with the user) to run natively rather than inside
   Docker (Pynguin's own recommended isolation): this dataset's generated
   code has shown zero file I/O, network, or subprocess behavior anywhere
   this session.
2. **`--maximum_mutation_time` must be passed explicitly, never left at the
   `-1` ("unlimited") default.** Confirmed empirically: with the default,
   Pynguin's internal `MUTATION_ANALYSIS` assertion-generation pass gets
   starved and every emitted assertion is `isinstance()`-only, the same weak
   pattern already diagnosed in this project's own test suites. Giving it an
   explicit floor (this script defaults to 60s) made Pynguin actually
   produce real value assertions in the smoke test.

Also requires `--pynguin-python` to point at the isolated `.venv-testgen`
interpreter (default: `<repo>/.venv-testgen/Scripts/python.exe`), NOT the
main `.venv` -- installing Pynguin into the main venv was found to silently
downgrade `pytest`/`setuptools`/`Jinja2`/`rich` (see docs/DECISIONS.md), so
Track A tooling is isolated in its own venv.

Each model gets `test_pynguin.py` written into its directory (same
convention as `generate_combined_tests.py`'s `test_combined.py`), plus the
model's own `pynguin_stats.json` sidecar with Pynguin's self-reported
coverage/mutation statistics (NOT the number to trust for the Phase 4
comparison -- that comes from re-running this project's own
`validate_mutation_properties.py` against the generated file, same as every
other suite, so results are apples-to-apples. Pynguin's own numbers are kept
only as a secondary diagnostic).

Usage:
    python scripts/generate_pynguin_tests.py --models-file PATH [--workers N]
        [--dataset-dir PATH] [--reports-dir PATH] [--report-name NAME]
        [--maximum-search-time SECONDS] [--maximum-mutation-time SECONDS]
        [--overall-timeout SECONDS] [--pynguin-python PATH] [--limit N] [--fresh]
"""
from __future__ import annotations

import argparse
import concurrent.futures
import datetime
import json
import os
import platform
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

SOURCE_FILENAME = "python_code.py"
OUTPUT_TEST_FILENAME = "test_pynguin.py"
STATS_SIDECAR_FILENAME = "pynguin_stats.json"
DEFAULT_MAXIMUM_SEARCH_TIME = 60
DEFAULT_MAXIMUM_MUTATION_TIME = 60
DEFAULT_OVERALL_TIMEOUT = 600
# Cached results with one of these statuses are automatically re-attempted
# on the next run under the SAME --report-name, instead of staying
# permanently "done" -- same fix as validate_mutation.py/
# validate_mutation_properties.py (2026-10-01), applied here too after the
# user hit the identical annoyance with this script. "missing_file" is
# excluded: permanent (the model genuinely has no python_code.py), not a
# transient failure a re-run would fix.
RETRIABLE_STATUSES = {"timeout", "no_tests_generated", "error"}

OUTPUT_VARIABLES = [
    "TargetModule", "Coverage", "NumberOfCreatedMutants",
    "NumberOfKilledMutants", "NumberOfTimedOutMutants", "MutationScore",
]


def default_pynguin_python(repo_root: Path) -> Path:
    name = "python.exe" if platform.system() == "Windows" else "python"
    return repo_root / ".venv-testgen" / ("Scripts" if platform.system() == "Windows" else "bin") / name


def load_cache(cache_path: Path) -> dict[str, dict]:
    cached: dict[str, dict] = {}
    if not cache_path.is_file():
        return cached
    with cache_path.open("r") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            try:
                result = json.loads(line)
            except json.JSONDecodeError:
                continue
            cached[result["model"]] = result
    return cached


def find_model_dirs(dataset_dir: Path, models_file: Path | None, limit: int | None) -> list[Path]:
    if models_file:
        names = [l.strip() for l in models_file.read_text().splitlines() if l.strip()]
        dirs = [dataset_dir / name for name in names]
    else:
        dirs = sorted(p for p in dataset_dir.iterdir() if p.is_dir())
    if limit:
        dirs = dirs[:limit]
    return dirs


def parse_statistics_csv(csv_path: Path) -> dict | None:
    """Pynguin writes this CSV with a blank line between the header and the
    data row (confirmed: '"TargetModule",...\\n\\n"python_code",...\\n\\n') --
    filter blank lines out rather than assume row 1 is the data."""
    if not csv_path.is_file():
        return None
    text = csv_path.read_text(encoding="utf-8", errors="replace")
    lines = [l for l in text.splitlines() if l.strip()]
    if len(lines) < 2:
        return None
    header = [h.strip('"') for h in lines[0].split(",")]
    values = [v.strip('"') for v in lines[1].split(",")]
    return dict(zip(header, values))


def generate_model(
    model_dir: Path, pynguin_python: str, maximum_search_time: int,
    maximum_mutation_time: int, overall_timeout: int,
) -> dict:
    checked_at = datetime.datetime.now(datetime.timezone.utc).isoformat()
    result = {
        "model": model_dir.name,
        "checked_at": checked_at,
        "python_version": platform.python_version(),
        "status": "missing_file",
        "tests_written": None,
        "pynguin_stats": None,
        "error_message": None,
    }

    source_path = model_dir / SOURCE_FILENAME
    if not source_path.is_file():
        result["error_message"] = f"{SOURCE_FILENAME} not found"
        return result

    scratch_root = tempfile.mkdtemp(prefix=f"pynguin_{model_dir.name}_")
    try:
        proj_dir = Path(scratch_root) / "proj"
        out_dir = Path(scratch_root) / "out"
        report_dir = Path(scratch_root) / "report"
        proj_dir.mkdir()
        shutil.copy2(source_path, proj_dir / SOURCE_FILENAME)

        env = dict(os.environ)
        env["PYNGUIN_DANGER_AWARE"] = "1"
        env["PYTHONDONTWRITEBYTECODE"] = "1"

        cmd = [
            pynguin_python, "-m", "pynguin",
            "--project_path", str(proj_dir),
            "--module_name", "python_code",
            "--output_path", str(out_dir),
            "--report_dir", str(report_dir),
            "--maximum_search_time", str(maximum_search_time),
            "--maximum_mutation_time", str(maximum_mutation_time),
            "--output_variables", *OUTPUT_VARIABLES,
        ]
        try:
            proc = subprocess.run(
                cmd, capture_output=True, text=True, timeout=overall_timeout, env=env,
            )
        except subprocess.TimeoutExpired:
            result["status"] = "timeout"
            result["error_message"] = f"Pynguin exceeded {overall_timeout}s"
            return result

        stats = parse_statistics_csv(report_dir / "statistics.csv")
        result["pynguin_stats"] = stats

        generated_path = out_dir / "test_python_code.py"
        if not generated_path.is_file():
            result["status"] = "no_tests_generated"
            result["error_message"] = (proc.stderr or proc.stdout or "").strip()[-1000:]
            return result

        # errors="replace": Pynguin's own generated header has been observed
        # to contain a non-UTF-8 byte (its copyright line's en-dash), same
        # class of issue as this project's other encoding="utf-8" reads --
        # never let one bad byte in a cosmetic comment fail the whole model.
        test_text = generated_path.read_text(encoding="utf-8", errors="replace")
        (model_dir / OUTPUT_TEST_FILENAME).write_text(test_text, encoding="utf-8")
        if stats is not None:
            (model_dir / STATS_SIDECAR_FILENAME).write_text(json.dumps(stats, indent=2) + "\n", encoding="utf-8")

        result["status"] = "generated"
        result["tests_written"] = test_text.count("\ndef test_")
        return result
    except Exception as exc:
        result["status"] = "error"
        result["error_message"] = str(exc)
        return result
    finally:
        shutil.rmtree(scratch_root, ignore_errors=True)


def build_report(results: list[dict]) -> dict:
    total = len(results)
    by_status: dict[str, int] = {}
    for r in results:
        by_status[r["status"]] = by_status.get(r["status"], 0) + 1
    generated = [r for r in results if r["status"] == "generated"]

    def _float(stats: dict | None, key: str) -> float | None:
        if not stats or key not in stats:
            return None
        try:
            return float(stats[key])
        except ValueError:
            return None

    self_scores = [v for r in generated if (v := _float(r["pynguin_stats"], "MutationScore")) is not None]
    return {
        "generated_at": datetime.datetime.now(datetime.timezone.utc).isoformat(),
        "total_models": total,
        "by_status": dict(sorted(by_status.items(), key=lambda kv: -kv[1])),
        "generated_count": len(generated),
        "avg_tests_per_model": round(sum(r["tests_written"] or 0 for r in generated) / len(generated), 2) if generated else None,
        "avg_pynguin_self_reported_mutation_score": round(sum(self_scores) / len(self_scores), 4) if self_scores else None,
        "results": results,
    }


def render_markdown_report(report: dict) -> str:
    lines = [
        "# Pynguin Test Generation Report (Phase 4 Track A)",
        "",
        f"Generated: {report['generated_at']}",
        "",
        f"- **Total models:** {report['total_models']}",
        f"- **Generated:** {report['generated_count']}",
        f"- **Avg tests per model:** {report['avg_tests_per_model']}",
        f"- **Avg Pynguin self-reported mutation score:** {report['avg_pynguin_self_reported_mutation_score']} "
        "(diagnostic only -- the real comparison number comes from re-running "
        "validate_mutation_properties.py against test_pynguin.py)",
        "",
        "## Breakdown by status",
        "",
        "| Status | Count |",
        "|---|---|",
    ]
    for status, count in report["by_status"].items():
        lines.append(f"| {status} | {count} |")
    lines += ["", "Full per-model detail: see the accompanying `.json` report."]
    return "\n".join(lines) + "\n"


def main() -> None:
    repo_root = Path(__file__).resolve().parent.parent
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--dataset-dir", type=Path, default=repo_root / "Dataset")
    parser.add_argument("--reports-dir", type=Path, default=repo_root / "reports")
    parser.add_argument("--models-file", type=Path, default=None)
    parser.add_argument("--report-name", type=str, default="pynguin_generation_report")
    parser.add_argument("--workers", type=int, default=4,
                         help="Pynguin is CPU-heavy per model (search + internal mutation "
                              "analysis) -- default kept modest, raise cautiously")
    parser.add_argument("--maximum-search-time", type=int, default=DEFAULT_MAXIMUM_SEARCH_TIME)
    parser.add_argument("--maximum-mutation-time", type=int, default=DEFAULT_MAXIMUM_MUTATION_TIME,
                         help="Never omit/default to -1 -- see module docstring, this starves "
                              "Pynguin's own assertion-generation pass")
    parser.add_argument("--overall-timeout", type=int, default=DEFAULT_OVERALL_TIMEOUT)
    parser.add_argument("--pynguin-python", type=str, default=None,
                         help="Path to the .venv-testgen interpreter Pynguin is installed in "
                              "(default: <repo>/.venv-testgen/Scripts/python.exe)")
    parser.add_argument("--limit", type=int, default=None)
    parser.add_argument("--fresh", action="store_true", help="Ignore any existing cache and recompute every model")
    args = parser.parse_args()

    pynguin_python = args.pynguin_python or str(default_pynguin_python(repo_root))
    if not Path(pynguin_python).is_file():
        parser.error(f"Pynguin interpreter not found at {pynguin_python!r} -- pass --pynguin-python "
                      f"explicitly, or install Pynguin into .venv-testgen first")

    args.reports_dir.mkdir(parents=True, exist_ok=True)
    cache_path = args.reports_dir / f"{args.report_name}.cache.jsonl"
    cached_results_all: dict[str, dict] = {} if args.fresh else load_cache(cache_path)
    if args.fresh and cache_path.is_file():
        cache_path.unlink()
    retriable = {m: r for m, r in cached_results_all.items() if r["status"] in RETRIABLE_STATUSES}
    cached_results = {m: r for m, r in cached_results_all.items() if m not in retriable}

    all_model_dirs = find_model_dirs(args.dataset_dir, args.models_file, args.limit)
    total = len(all_model_dirs)
    model_dirs = [d for d in all_model_dirs if d.name not in cached_results]
    skipped = total - len(model_dirs)

    print(f"Generating Pynguin tests for {total} models with {args.workers} workers "
          f"(search={args.maximum_search_time}s, mutation={args.maximum_mutation_time}s/model)...")
    if skipped:
        print(f"Resuming from cache: {skipped}/{total} already done, {len(model_dirs)} remaining "
              f"(pass --fresh to ignore the cache and recompute everything)")
    if retriable:
        print(f"Auto-retrying {len(retriable)} previously-failed models from the cache -- "
              f"same report, no separate retry run needed")

    results: list[dict] = list(cached_results.values())
    done = skipped
    cache_file = cache_path.open("a")
    try:
        with concurrent.futures.ProcessPoolExecutor(max_workers=args.workers) as executor:
            futures = {
                executor.submit(
                    generate_model, model_dir, pynguin_python,
                    args.maximum_search_time, args.maximum_mutation_time, args.overall_timeout,
                ): model_dir
                for model_dir in model_dirs
            }
            for future in concurrent.futures.as_completed(futures):
                model_dir = futures[future]
                try:
                    result = future.result()
                except Exception as exc:
                    result = {
                        "model": model_dir.name, "status": "error", "error_message": str(exc),
                        "tests_written": None, "pynguin_stats": None,
                    }
                results.append(result)
                cache_file.write(json.dumps(result) + "\n")
                cache_file.flush()
                done += 1
                print(f"  {done}/{total}: {model_dir.name} -> {result['status']}", flush=True)
    finally:
        cache_file.close()

    report = build_report(results)
    json_path = args.reports_dir / f"{args.report_name}.json"
    json_path.write_text(json.dumps(report, indent=2) + "\n")
    md_path = args.reports_dir / f"{args.report_name}.md"
    md_path.write_text(render_markdown_report(report))

    print()
    print(f"Generated: {report['generated_count']}/{report['total_models']}")
    print(f"Report written to {json_path} and {md_path}")


if __name__ == "__main__":
    main()
