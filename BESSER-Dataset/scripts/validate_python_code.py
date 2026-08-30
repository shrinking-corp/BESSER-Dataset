#!/usr/bin/env python3
"""Validate that each model's generated `python_code.py` compiles and runs cleanly.

For every model directory under `Dataset/`, this script executes the model's
`python_code.py` in an isolated subprocess to check that it is syntactically
valid (compilable) and that it runs to completion without raising an
exception (runnable). The result is written into a `code_metadata.json` file
alongside the model's other artifacts, and an aggregate report is written to
`reports/`.

Usage:
    python scripts/validate_python_code.py [--workers N] [--timeout SECONDS]
                                            [--dataset-dir PATH] [--limit N]

Each model's `code_metadata.json` gets (or has updated) a top-level
"python_code_validation" key:

    {
      "python_code_validation": {
        "file": "python_code.py",
        "checked_at": "2026-08-30T12:00:00+00:00",
        "python_version": "3.13.5",
        "status": "pass",            # pass | syntax_error | runtime_error | timeout | missing_file
        "compiles": true,
        "runs": true,
        "returncode": 0,
        "error_type": null,
        "error_message": null
      }
    }

Existing keys in code_metadata.json (if any) are preserved; only the
"python_code_validation" key is added/overwritten.
"""
from __future__ import annotations

import argparse
import concurrent.futures
import datetime
import json
import platform
import subprocess
import sys
from pathlib import Path

CODE_FILENAME = "python_code.py"
METADATA_FILENAME = "code_metadata.json"
DEFAULT_TIMEOUT = 20
SYNTAX_ERROR_TYPES = {"SyntaxError", "IndentationError", "TabError"}


def find_model_dirs(dataset_dir: Path) -> list[Path]:
    return sorted(p for p in dataset_dir.iterdir() if p.is_dir())


def parse_traceback(stderr: str) -> tuple[str | None, str | None]:
    """Extract (error_type, error_message) from a Python traceback's last line."""
    lines = [l for l in stderr.strip().splitlines() if l.strip()]
    if not lines:
        return None, None
    last = lines[-1]
    if ":" in last:
        etype, _, msg = last.partition(":")
        etype = etype.strip()
        # Guard against grabbing a non-exception line (e.g. a file path)
        if etype.replace("_", "").isalnum():
            return etype, msg.strip()
    return None, last.strip()


def validate_model(model_dir: Path, timeout: int) -> dict:
    code_path = model_dir / CODE_FILENAME
    checked_at = datetime.datetime.now(datetime.timezone.utc).isoformat()
    python_version = platform.python_version()

    result = {
        "file": CODE_FILENAME,
        "checked_at": checked_at,
        "python_version": python_version,
        "status": "missing_file",
        "compiles": False,
        "runs": False,
        "returncode": None,
        "error_type": None,
        "error_message": None,
    }

    if not code_path.is_file():
        result["error_message"] = f"{CODE_FILENAME} not found in {model_dir.name}"
        return {"model": model_dir.name, **result}

    try:
        proc = subprocess.run(
            [sys.executable, CODE_FILENAME],
            cwd=str(model_dir),
            capture_output=True,
            text=True,
            timeout=timeout,
        )
    except subprocess.TimeoutExpired:
        result["status"] = "timeout"
        result["error_type"] = "TimeoutExpired"
        result["error_message"] = f"Execution exceeded {timeout}s"
        return {"model": model_dir.name, **result}

    result["returncode"] = proc.returncode

    if proc.returncode == 0:
        result["status"] = "pass"
        result["compiles"] = True
        result["runs"] = True
        return {"model": model_dir.name, **result}

    error_type, error_message = parse_traceback(proc.stderr)
    result["error_type"] = error_type
    result["error_message"] = error_message

    if error_type in SYNTAX_ERROR_TYPES:
        result["status"] = "syntax_error"
        result["compiles"] = False
        result["runs"] = False
    else:
        result["status"] = "runtime_error"
        result["compiles"] = True
        result["runs"] = False

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
    data["python_code_validation"] = entry

    metadata_path.write_text(json.dumps(data, indent=2) + "\n")


def build_report(results: list[dict]) -> dict:
    total = len(results)
    by_status: dict[str, int] = {}
    by_error_type: dict[str, int] = {}
    failing_models = []

    for r in results:
        by_status[r["status"]] = by_status.get(r["status"], 0) + 1
        if r["status"] != "pass":
            failing_models.append(
                {
                    "model": r["model"],
                    "status": r["status"],
                    "error_type": r["error_type"],
                    "error_message": r["error_message"],
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
        "by_status": by_status,
        "by_error_type": dict(sorted(by_error_type.items(), key=lambda kv: -kv[1])),
        "failing_models": sorted(failing_models, key=lambda m: m["model"]),
    }


def render_markdown_report(report: dict) -> str:
    lines = [
        "# Python Code Validation Report",
        "",
        f"Generated: {report['generated_at']}",
        "",
        f"- **Total models checked:** {report['total_models']}",
        f"- **Passed (compiles & runs):** {report['passed']}",
        f"- **Failed:** {report['failed']}",
        f"- **Pass rate:** {report['pass_rate'] * 100:.2f}%" if report["pass_rate"] is not None else "- **Pass rate:** n/a",
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

    lines += ["", f"Full per-model detail: see `python_code_validation_report.json` "
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
    print(f"Validating {total} models from {args.dataset_dir} with {args.workers} workers...")

    results: list[dict] = []
    done = 0
    with concurrent.futures.ProcessPoolExecutor(max_workers=args.workers) as executor:
        futures = {
            executor.submit(validate_model, model_dir, args.timeout): model_dir
            for model_dir in model_dirs
        }
        for future in concurrent.futures.as_completed(futures):
            model_dir = futures[future]
            try:
                result = future.result()
            except Exception as exc:  # defensive: worker-side crash
                result = {
                    "model": model_dir.name,
                    "file": CODE_FILENAME,
                    "checked_at": datetime.datetime.now(datetime.timezone.utc).isoformat(),
                    "python_version": platform.python_version(),
                    "status": "runtime_error",
                    "compiles": False,
                    "runs": False,
                    "returncode": None,
                    "error_type": type(exc).__name__,
                    "error_message": str(exc),
                }
            write_model_metadata(model_dir, result)
            results.append(result)
            done += 1
            if done % 500 == 0 or done == total:
                print(f"  {done}/{total} processed...")

    report = build_report(results)
    args.reports_dir.mkdir(parents=True, exist_ok=True)

    json_path = args.reports_dir / "python_code_validation_report.json"
    json_path.write_text(json.dumps(report, indent=2) + "\n")

    md_path = args.reports_dir / "python_code_validation_report.md"
    md_path.write_text(render_markdown_report(report))

    print()
    print(f"Passed: {report['passed']}/{report['total_models']} ({(report['pass_rate'] or 0) * 100:.2f}%)")
    print(f"By status: {report['by_status']}")
    print(f"Report written to {json_path} and {md_path}")


if __name__ == "__main__":
    main()