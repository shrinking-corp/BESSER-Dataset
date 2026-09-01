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
import concurrent.futures
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

TEST_FILENAME = "test_hypothesis.py"
SOURCE_MODULE = "python_code"
DEFAULT_TIMEOUT = 120


def find_model_dirs(dataset_dir: Path, models_file: Path | None, limit: int | None) -> list[Path]:
    if models_file:
        names = [l.strip() for l in models_file.read_text().splitlines() if l.strip()]
        dirs = [dataset_dir / name for name in names]
    else:
        dirs = sorted(p for p in dataset_dir.iterdir() if p.is_dir())
    if limit:
        dirs = dirs[:limit]
    return dirs


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
        cov_summary = json.loads(cov_json_path.read_text())
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
        "## Breakdown by status",
        "",
        "| Status | Count |",
        "|---|---|",
    ]
    for status, count in sorted(report["by_status"].items(), key=lambda kv: -kv[1]):
        lines.append(f"| {status} | {count} |")
    lines += ["", "Full per-model detail: see `coverage_prototype_report.json`."]
    return "\n".join(l for l in lines if l is not None) + "\n"


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--dataset-dir", type=Path,
        default=Path(__file__).resolve().parent.parent / "Dataset",
    )
    parser.add_argument(
        "--reports-dir", type=Path,
        default=Path(__file__).resolve().parent.parent / "reports",
    )
    parser.add_argument("--models-file", type=Path, default=None, help="File with one model dir name per line")
    parser.add_argument("--report-name", type=str, default="coverage_prototype_report")
    parser.add_argument("--workers", type=int, default=8)
    parser.add_argument("--timeout", type=int, default=DEFAULT_TIMEOUT)
    parser.add_argument("--limit", type=int, default=None)
    args = parser.parse_args()

    model_dirs = find_model_dirs(args.dataset_dir, args.models_file, args.limit)
    total = len(model_dirs)
    hypothesis_home = tempfile.mkdtemp(prefix="besser_hypothesis_db_")
    scratch_dir = tempfile.mkdtemp(prefix="besser_coverage_scratch_")
    print(f"Measuring coverage for {total} models with {args.workers} workers...")

    results: list[dict] = []
    done = 0
    try:
        with concurrent.futures.ProcessPoolExecutor(max_workers=args.workers) as executor:
            futures = {
                executor.submit(validate_model, model_dir, args.timeout, hypothesis_home, scratch_dir): model_dir
                for model_dir in model_dirs
            }
            for future in concurrent.futures.as_completed(futures):
                model_dir = futures[future]
                try:
                    result = future.result()
                except Exception as exc:
                    result = {
                        "model": model_dir.name, "status": "error", "error_message": str(exc),
                        "duration_s": None, "percent_covered": None, "num_statements": None,
                        "covered_lines": None, "missing_lines": None, "returncode": None,
                    }
                results.append(result)
                done += 1
                if done % 25 == 0 or done == total:
                    print(f"  {done}/{total} processed...")
    finally:
        shutil.rmtree(hypothesis_home, ignore_errors=True)
        shutil.rmtree(scratch_dir, ignore_errors=True)

    report = build_report(results)
    args.reports_dir.mkdir(parents=True, exist_ok=True)
    json_path = args.reports_dir / f"{args.report_name}.json"
    json_path.write_text(json.dumps(report, indent=2) + "\n")
    md_path = args.reports_dir / f"{args.report_name}.md"
    md_path.write_text(render_markdown_report(report))

    print()
    print(f"Measured: {report['measured_count']}/{report['total_models']}")
    print(f"Avg coverage: {report['avg_percent_covered']}%")
    print(f"Duration p50/p90/max: {report['duration_stats_s']['p50']}/{report['duration_stats_s']['p90']}/{report['duration_stats_s']['max']}s")
    print(f"Report written to {json_path} and {md_path}")


if __name__ == "__main__":
    main()
