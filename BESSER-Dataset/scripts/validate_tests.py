#!/usr/bin/env python3
"""Validate that each model's `test_hypothesis.py` collects and passes under pytest.

For every model directory under `Dataset/`, this script runs

    pytest test_hypothesis.py

in an isolated subprocess (cwd = the model directory, so `from python_code
import ...` resolves the sibling `python_code.py`). It records whether the
test module could even be collected (i.e. `python_code.py` imports cleanly
and the test file itself is syntactically valid) and, if so, how many of its
tests passed/failed/errored. The result is written into each model's
`code_metadata.json` under a new "test_validation" key, alongside the
"python_code_validation" key written by `validate_python_code.py`.

This complements validate_python_code.py: that script only checks the
generated model code runs standalone; this one checks that the accompanying
generated test suite actually exercises that code successfully.

Usage:
    python scripts/validate_tests.py [--workers N] [--timeout SECONDS]
                                      [--dataset-dir PATH] [--limit N]

Each model's `code_metadata.json` gets (or has updated) a top-level
"test_validation" key:

    {
      "test_validation": {
        "file": "test_hypothesis.py",
        "checked_at": "2026-08-30T12:00:00+00:00",
        "python_version": "3.13.5",
        "status": "pass",   # pass | test_failures | collection_error |
                             # no_tests_collected | timeout | missing_file | error
        "returncode": 0,
        "collected": 32,
        "passed": 32,
        "failed": 0,
        "errors": 0,
        "skipped": 0,
        "error_type": null,
        "error_message": null,
        "failing_tests": []
      }
    }

Existing keys in code_metadata.json (if any) are preserved; only the
"test_validation" key is added/overwritten.

To avoid littering the dataset with `.pytest_cache` / `.hypothesis`
directories in every one of the ~9000 model folders, pytest's cache plugin
is disabled and Hypothesis's example database is redirected to a shared
temp directory for the duration of the run (removed automatically after).
"""
from __future__ import annotations

import argparse
import concurrent.futures
import datetime
import json
import os
import platform
import re
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

TEST_FILENAME = "test_hypothesis.py"
METADATA_FILENAME = "code_metadata.json"
DEFAULT_TIMEOUT = 60

SUMMARY_COUNT_RE = re.compile(
    r"(\d+)\s+(passed|failed|errors?|skipped|xfailed|xpassed)"
)
FAILED_LINE_RE = re.compile(r"^(?:FAILED|ERROR)\s+(\S+)(?:\s+-\s+(.*))?$")
TRACEBACK_LINE_RE = re.compile(r"^E\s+([A-Za-z_][A-Za-z0-9_.]*)\s*:\s*(.*)$")


def find_model_dirs(dataset_dir: Path) -> list[Path]:
    return sorted(p for p in dataset_dir.iterdir() if p.is_dir())


def parse_counts(stdout: str) -> dict:
    """Parse the final pytest summary line, e.g. "3 failed, 12 passed in 1.2s".

    Only the last non-empty line is considered: pytest may print an
    "Interrupted: N error(s) during collection" banner immediately above it,
    which matches the same count pattern and would otherwise be double-counted.
    """
    counts = {"passed": 0, "failed": 0, "errors": 0, "skipped": 0, "xfailed": 0, "xpassed": 0}
    lines = [l for l in stdout.strip().splitlines() if l.strip()]
    if not lines:
        return counts
    last_line = lines[-1]
    for match in SUMMARY_COUNT_RE.finditer(last_line):
        n = int(match.group(1))
        key = match.group(2)
        if key == "error":
            key = "errors"
        counts[key] = counts.get(key, 0) + n
    return counts


def parse_failure_detail(stdout: str) -> tuple[str | None, str | None, list[str]]:
    """Extract (error_type, error_message, failing_test_names) from pytest output.

    Prefers the full "E   <Type>: <message>" lines from the traceback body
    over the short-summary "FAILED ... - <Type>: <message>" line, because
    pytest truncates the latter to fit its summary width (e.g. "AssertionError...")
    when stdout isn't a tty, which would otherwise clip real messages.
    """
    failing_tests = []
    last_dash_msg: str | None = None
    for line in stdout.splitlines():
        m = FAILED_LINE_RE.match(line.strip())
        if m:
            failing_tests.append(m.group(1))
            if m.group(2):
                last_dash_msg = m.group(2)

    error_type = None
    error_message = None
    for line in stdout.splitlines():
        m = TRACEBACK_LINE_RE.match(line.rstrip())
        if m:
            error_type, error_message = m.group(1), m.group(2).strip()

    if error_type is None and last_dash_msg:
        if ":" in last_dash_msg:
            etype, _, msg = last_dash_msg.partition(":")
            etype = etype.strip()
            if etype.replace("_", "").isalnum():
                error_type, error_message = etype, msg.strip()
        if error_type is None:
            error_message = last_dash_msg

    if error_type is None and error_message is None:
        lines = [l for l in stdout.strip().splitlines() if l.strip()]
        if lines:
            error_message = lines[-1].strip()

    return error_type, error_message, failing_tests


def validate_model(model_dir: Path, timeout: int, hypothesis_home: str) -> dict:
    test_path = model_dir / TEST_FILENAME
    checked_at = datetime.datetime.now(datetime.timezone.utc).isoformat()
    python_version = platform.python_version()

    result = {
        "file": TEST_FILENAME,
        "checked_at": checked_at,
        "python_version": python_version,
        "status": "missing_file",
        "returncode": None,
        "collected": 0,
        "passed": 0,
        "failed": 0,
        "errors": 0,
        "skipped": 0,
        "error_type": None,
        "error_message": None,
        "failing_tests": [],
    }

    if not test_path.is_file():
        result["error_message"] = f"{TEST_FILENAME} not found in {model_dir.name}"
        return {"model": model_dir.name, **result}

    env = dict(os.environ)
    env["PYTHONDONTWRITEBYTECODE"] = "1"
    env["HYPOTHESIS_STORAGE_DIRECTORY"] = hypothesis_home

    try:
        proc = subprocess.run(
            [
                sys.executable, "-m", "pytest", TEST_FILENAME,
                "-q", "-p", "no:cacheprovider", "--tb=line", "--no-header",
            ],
            cwd=str(model_dir),
            capture_output=True,
            text=True,
            timeout=timeout,
            env=env,
        )
    except subprocess.TimeoutExpired:
        result["status"] = "timeout"
        result["error_type"] = "TimeoutExpired"
        result["error_message"] = f"Execution exceeded {timeout}s"
        return {"model": model_dir.name, **result}

    result["returncode"] = proc.returncode
    stdout = proc.stdout or ""

    counts = parse_counts(stdout)
    result["passed"] = counts["passed"]
    result["failed"] = counts["failed"]
    result["errors"] = counts["errors"]
    result["skipped"] = counts["skipped"] + counts["xfailed"] + counts["xpassed"]
    result["collected"] = sum(counts.values())

    if proc.returncode == 0:
        result["status"] = "pass"
        return {"model": model_dir.name, **result}

    error_type, error_message, failing_tests = parse_failure_detail(stdout)
    result["error_type"] = error_type
    result["error_message"] = error_message
    result["failing_tests"] = failing_tests[:10]

    if proc.returncode == 5:
        result["status"] = "no_tests_collected"
    elif proc.returncode == 2:
        result["status"] = "collection_error"
    elif proc.returncode == 1:
        result["status"] = "test_failures"
    else:
        result["status"] = "error"
        if error_message is None:
            error_message = (proc.stderr or "").strip().splitlines()[-1] if proc.stderr else None
            result["error_message"] = error_message

    return {"model": model_dir.name, **result}


def write_model_metadata(model_dir: Path, validation: dict) -> None:
    metadata_path = model_dir / METADATA_FILENAME
    data = {}
    if metadata_path.is_file():
        try:
            data = json.loads(metadata_path.read_text())
        except (json.JSONDecodeError, OSError):
            data = {}

    entry = {k: v for k, v in validation.items() if k != "model"}
    data["test_validation"] = entry

    metadata_path.write_text(json.dumps(data, indent=2) + "\n")


def build_report(results: list[dict]) -> dict:
    total = len(results)
    by_status: dict[str, int] = {}
    by_error_type: dict[str, int] = {}
    failing_models = []
    total_tests_collected = 0
    total_tests_passed = 0
    total_tests_failed = 0
    total_tests_errored = 0

    for r in results:
        by_status[r["status"]] = by_status.get(r["status"], 0) + 1
        total_tests_collected += r.get("collected", 0) or 0
        total_tests_passed += r.get("passed", 0) or 0
        total_tests_failed += r.get("failed", 0) or 0
        total_tests_errored += r.get("errors", 0) or 0
        if r["status"] != "pass":
            failing_models.append(
                {
                    "model": r["model"],
                    "status": r["status"],
                    "returncode": r["returncode"],
                    "error_type": r["error_type"],
                    "error_message": r["error_message"],
                    "failed": r["failed"],
                    "errors": r["errors"],
                    "failing_tests": r["failing_tests"],
                }
            )
            if r["error_type"]:
                by_error_type[r["error_type"]] = by_error_type.get(r["error_type"], 0) + 1

    passed = by_status.get("pass", 0)
    return {
        "generated_at": datetime.datetime.now(datetime.timezone.utc).isoformat(),
        "total_models": total,
        "passed": passed,
        "failed": total - passed,
        "pass_rate": round(passed / total, 4) if total else None,
        "total_tests_collected": total_tests_collected,
        "total_tests_passed": total_tests_passed,
        "total_tests_failed": total_tests_failed,
        "total_tests_errored": total_tests_errored,
        "by_status": by_status,
        "by_error_type": dict(sorted(by_error_type.items(), key=lambda kv: -kv[1])),
        "failing_models": sorted(failing_models, key=lambda m: m["model"]),
    }


def render_markdown_report(report: dict) -> str:
    lines = [
        "# Test Suite Validation Report",
        "",
        f"Generated: {report['generated_at']}",
        "",
        f"- **Total models checked:** {report['total_models']}",
        f"- **Models with fully passing test suite:** {report['passed']}",
        f"- **Models with a failing/broken test suite:** {report['failed']}",
        f"- **Model pass rate:** {report['pass_rate'] * 100:.2f}%" if report["pass_rate"] is not None else "- **Model pass rate:** n/a",
        "",
        f"- **Total individual tests collected:** {report['total_tests_collected']}",
        f"- **Total individual tests passed:** {report['total_tests_passed']}",
        f"- **Total individual tests failed:** {report['total_tests_failed']}",
        f"- **Total individual tests errored:** {report['total_tests_errored']}",
        "",
        "## Breakdown by status",
        "",
        "| Status | Count |",
        "|---|---|",
    ]
    for status, count in sorted(report["by_status"].items(), key=lambda kv: -kv[1]):
        lines.append(f"| {status} | {count} |")

    if report["by_error_type"]:
        lines += ["", "## Failing models by error type", "", "| Error type | Count |", "|---|---|"]
        for etype, count in report["by_error_type"].items():
            lines.append(f"| {etype} | {count} |")

    lines += ["", f"Full per-model detail: see `test_validation_report.json` "
                   "and each model's `code_metadata.json`."]
    return "\n".join(lines) + "\n"


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--dataset-dir",
        type=Path,
        default=Path(__file__).resolve().parent.parent / "Dataset",
        help="Path to the Dataset directory (default: <repo>/Dataset)",
    )
    parser.add_argument(
        "--reports-dir",
        type=Path,
        default=Path(__file__).resolve().parent.parent / "reports",
        help="Where to write the aggregate report (default: <repo>/reports)",
    )
    parser.add_argument("--workers", type=int, default=8, help="Parallel worker processes")
    parser.add_argument("--timeout", type=int, default=DEFAULT_TIMEOUT, help="Per-model timeout (seconds)")
    parser.add_argument("--limit", type=int, default=None, help="Only process the first N models (for testing)")
    args = parser.parse_args()

    model_dirs = find_model_dirs(args.dataset_dir)
    if args.limit:
        model_dirs = model_dirs[: args.limit]

    total = len(model_dirs)
    hypothesis_home = tempfile.mkdtemp(prefix="besser_hypothesis_db_")
    print(f"Validating {total} test suites from {args.dataset_dir} with {args.workers} workers...")
    print(f"(Hypothesis example database redirected to {hypothesis_home})")

    results: list[dict] = []
    done = 0
    try:
        with concurrent.futures.ProcessPoolExecutor(max_workers=args.workers) as executor:
            futures = {
                executor.submit(validate_model, model_dir, args.timeout, hypothesis_home): model_dir
                for model_dir in model_dirs
            }
            for future in concurrent.futures.as_completed(futures):
                model_dir = futures[future]
                try:
                    result = future.result()
                except Exception as exc:  # defensive: worker-side crash
                    result = {
                        "model": model_dir.name,
                        "file": TEST_FILENAME,
                        "checked_at": datetime.datetime.now(datetime.timezone.utc).isoformat(),
                        "python_version": platform.python_version(),
                        "status": "error",
                        "returncode": None,
                        "collected": 0,
                        "passed": 0,
                        "failed": 0,
                        "errors": 0,
                        "skipped": 0,
                        "error_type": type(exc).__name__,
                        "error_message": str(exc),
                        "failing_tests": [],
                    }
                write_model_metadata(model_dir, result)
                results.append(result)
                done += 1
                if done % 500 == 0 or done == total:
                    print(f"  {done}/{total} processed...")
    finally:
        shutil.rmtree(hypothesis_home, ignore_errors=True)

    report = build_report(results)
    args.reports_dir.mkdir(parents=True, exist_ok=True)

    json_path = args.reports_dir / "test_validation_report.json"
    json_path.write_text(json.dumps(report, indent=2) + "\n")

    md_path = args.reports_dir / "test_validation_report.md"
    md_path.write_text(render_markdown_report(report))

    print()
    print(f"Passed: {report['passed']}/{report['total_models']} ({(report['pass_rate'] or 0) * 100:.2f}%)")
    print(f"By status: {report['by_status']}")
    print(f"Report written to {json_path} and {md_path}")


if __name__ == "__main__":
    main()
