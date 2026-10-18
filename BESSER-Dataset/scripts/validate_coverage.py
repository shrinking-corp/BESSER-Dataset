#!/usr/bin/env python3
"""Measure line coverage of `python_code.py` achieved by `test_hypothesis.py`.

For every model directory given (via --models-file, or all of --dataset-dir
if omitted), this script runs

    pytest --cov=python_code --cov-report=json:<tmp> -q test_hypothesis.py

in an isolated subprocess (cwd = the model directory). It records the
percentage of statements covered, counts of covered/missing lines, and
per-model timing.

This is a PROTOTYPE script (see PROMPT.md): it does NOT write into each
model's code_metadata.json. It only produces an aggregate report under
reports/, so that a partial sample run doesn't leave 9,082 models in an
inconsistent state (some with a coverage_validation key, most without).
That wiring is deferred to a follow-up full-dataset script once timing from
this prototype is reviewed.

Usage:
    python scripts/validate_coverage.py --models-file PATH [--workers N]
                                         [--timeout SECONDS] [--dataset-dir PATH]
"""
from __future__ import annotations

import argparse
import datetime
import json
import os
import platform
import shutil
import subprocess
import sys
import tempfile
import time
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from _common.cache import load_cache, partition_cache  # noqa: E402
from _common.io import add_common_io_args, find_model_dirs  # noqa: E402
from _common.pool import run_models  # noqa: E402
from _common.report import render_status_table, write_reports  # noqa: E402

TEST_FILENAME = "test_hypothesis.py"
SOURCE_MODULE = "python_code"
DEFAULT_TIMEOUT = 120
RETRIABLE_STATUSES = frozenset({"timeout", "error"})


def validate_model(model_dir: Path, timeout: int, hypothesis_home: str, scratch_dir: str) -> dict:
    test_path = model_dir / TEST_FILENAME
    checked_at = datetime.datetime.now(datetime.timezone.utc).isoformat()

    result = {
        "model": model_dir.name,
        "checked_at": checked_at,
        "python_version": platform.python_version(),
        "status": "missing_file",
        "returncode": None,
        "duration_s": None,
        "num_statements": None,
        "covered_lines": None,
        "missing_lines": None,
        "percent_covered": None,
        "error_message": None,
    }

    if not test_path.is_file():
        result["error_message"] = f"{TEST_FILENAME} not found in {model_dir.name}"
        return result

    cov_json_path = Path(scratch_dir) / f"{model_dir.name}.cov.json"
    cov_data_path = Path(scratch_dir) / f"{model_dir.name}.coverage"

    env = dict(os.environ)
    env["PYTHONDONTWRITEBYTECODE"] = "1"
    env["HYPOTHESIS_STORAGE_DIRECTORY"] = hypothesis_home
    env["COVERAGE_FILE"] = str(cov_data_path)

    start = time.monotonic()
    try:
        proc = subprocess.run(
            [
                sys.executable, "-m", "pytest", TEST_FILENAME,
                f"--cov={SOURCE_MODULE}",
                f"--cov-report=json:{cov_json_path}",
                "-q", "-p", "no:cacheprovider", "--no-header",
            ],
            cwd=str(model_dir),
            capture_output=True,
            text=True,
            timeout=timeout,
            env=env,
        )
    except subprocess.TimeoutExpired:
        result["status"] = "timeout"
        result["duration_s"] = round(time.monotonic() - start, 3)
        result["error_message"] = f"Execution exceeded {timeout}s"
        return result
    finally:
        cov_data_path.unlink(missing_ok=True)

    result["duration_s"] = round(time.monotonic() - start, 3)
    result["returncode"] = proc.returncode

    if not cov_json_path.is_file():
        result["status"] = "no_coverage_data"
        tail = (proc.stdout or "").strip().splitlines()
        result["error_message"] = tail[-1] if tail else (proc.stderr or "").strip()[-500:]
        return result

    try:
        cov_summary = json.loads(cov_json_path.read_text(encoding="utf-8"))
        totals = cov_summary["totals"]
        result["num_statements"] = totals["num_statements"]
        result["covered_lines"] = totals["covered_lines"]
        result["missing_lines"] = totals["missing_lines"]
        result["percent_covered"] = round(totals["percent_covered"], 2)
        result["status"] = "measured" if proc.returncode == 0 else "measured_with_test_failures"
    except (KeyError, json.JSONDecodeError) as exc:
        result["status"] = "parse_error"
        result["error_message"] = str(exc)
    finally:
        cov_json_path.unlink(missing_ok=True)

    return result


def build_report(results: list[dict]) -> dict:
    total = len(results)
    by_status: dict[str, int] = {}
    measured = [r for r in results if r["percent_covered"] is not None]
    for r in results:
        by_status[r["status"]] = by_status.get(r["status"], 0) + 1

    durations = sorted(r["duration_s"] for r in results if r["duration_s"] is not None)

    def pct(vals, p):
        if not vals:
            return None
        idx = min(len(vals) - 1, int(len(vals) * p / 100))
        return vals[idx]

    return {
        "generated_at": datetime.datetime.now(datetime.timezone.utc).isoformat(),
        "total_models": total,
        "by_status": by_status,
        "measured_count": len(measured),
        "avg_percent_covered": round(sum(r["percent_covered"] for r in measured) / len(measured), 2) if measured else None,
        "median_percent_covered": pct(sorted(r["percent_covered"] for r in measured), 50),
        "duration_stats_s": {
            "p50": pct(durations, 50),
            "p90": pct(durations, 90),
            "p99": pct(durations, 99),
            "max": durations[-1] if durations else None,
            "total": round(sum(durations), 2),
        },
        "results": results,
    }


def render_markdown_report(report: dict) -> str:
    lines = [
        "# Coverage Prototype Report",
        "",
        f"Generated: {report['generated_at']}",
        "",
        f"- **Total models checked:** {report['total_models']}",
        f"- **Measured successfully:** {report['measured_count']}",
        f"- **Average line coverage:** {report['avg_percent_covered']}%" if report['avg_percent_covered'] is not None else "",
        f"- **Median line coverage:** {report['median_percent_covered']}%" if report['median_percent_covered'] is not None else "",
        "",
        "## Per-model duration (seconds)",
        "",
        f"- p50: {report['duration_stats_s']['p50']}",
        f"- p90: {report['duration_stats_s']['p90']}",
        f"- p99: {report['duration_stats_s']['p99']}",
        f"- max: {report['duration_stats_s']['max']}",
        f"- total (sum, sample only): {report['duration_stats_s']['total']}",
        "",
    ]
    lines += render_status_table(report["by_status"])
    lines += ["", "Full per-model detail: see `coverage_prototype_report.json`."]
    return "\n".join(lines) + "\n"


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    add_common_io_args(parser, __file__)
    parser.add_argument("--models-file", type=Path, default=None, help="File with one model dir name per line")
    parser.add_argument("--report-name", type=str, default="coverage_prototype_report")
    parser.add_argument("--workers", type=int, default=8)
    parser.add_argument("--timeout", type=int, default=DEFAULT_TIMEOUT)
    parser.add_argument("--limit", type=int, default=None)
    parser.add_argument("--fresh", action="store_true",
                         help="Ignore any existing cache and recompute every model")
    args = parser.parse_args()

    args.reports_dir.mkdir(parents=True, exist_ok=True)
    cache_path = args.reports_dir / f"{args.report_name}.cache.jsonl"

    cached_results_all: dict[str, dict] = {} if args.fresh else load_cache(cache_path)
    if args.fresh and cache_path.is_file():
        cache_path.unlink()
    cached_results, retriable = partition_cache(cached_results_all, RETRIABLE_STATUSES)

    all_model_dirs = find_model_dirs(args.dataset_dir, args.models_file, args.limit)
    total = len(all_model_dirs)
    model_dirs = [d for d in all_model_dirs if d.name not in cached_results]
    skipped = total - len(model_dirs)

    hypothesis_home = tempfile.mkdtemp(prefix="besser_hypothesis_db_")
    scratch_dir = tempfile.mkdtemp(prefix="besser_coverage_scratch_")
    print(f"Measuring coverage for {total} models with {args.workers} workers...")
    if skipped:
        print(f"Resuming from cache: {skipped}/{total} already done, {len(model_dirs)} remaining "
              f"(pass --fresh to ignore the cache and recompute everything)")
    if retriable:
        print(f"Auto-retrying {len(retriable)} previously-failed models from the cache")

    try:
        results = run_models(
            validate_model, model_dirs, worker_args=(args.timeout, hypothesis_home, scratch_dir),
            workers=args.workers, cache_path=cache_path, results=list(cached_results.values()),
            already_done=skipped, total=total,
            error_fields={"duration_s": None, "percent_covered": None, "num_statements": None,
                          "covered_lines": None, "missing_lines": None, "returncode": None},
        )
    finally:
        shutil.rmtree(hypothesis_home, ignore_errors=True)
        shutil.rmtree(scratch_dir, ignore_errors=True)

    report = build_report(results)
    json_path, md_path = write_reports(args.reports_dir, args.report_name, report, render_markdown_report(report))

    print()
    print(f"Measured: {report['measured_count']}/{report['total_models']}")
    print(f"Avg coverage: {report['avg_percent_covered']}%")
    print(f"Duration p50/p90/max: {report['duration_stats_s']['p50']}/{report['duration_stats_s']['p90']}/{report['duration_stats_s']['max']}s")
    print(f"Report written to {json_path} and {md_path}")


if __name__ == "__main__":
    main()
