#!/usr/bin/env python3
"""Measure `python_code.py` coverage achieved by each half of `test_hypothesis.py`.

Every generated `test_hypothesis.py` has two kinds of tests:

- **Structural tests** (`SECTION 1 — STRUCTURAL TESTS`): reflection-based
  checks (`inspect.isabstract`, constructor signature, property presence).
  Never decorated with `@given`.
- **Hypothesis-strategy tests** (`HYPOTHESIS STRATEGIES` section): the
  `@given`-based property tests (instantiation, setters) built from the
  `st.builds(...)` strategies defined in that section.

Hypothesis's pytest plugin auto-applies the `hypothesis` marker to every
`@given` test, so the two groups can be selected cheaply with `-m hypothesis`
/ `-m "not hypothesis"` -- no need to parse test node ids out of the file
(confirmed against `Dataset/model_1`: 9 `-m hypothesis` / 23 `-m "not
hypothesis"`, matching an independent AST-based count of `@given`
decorators).

For each model this script runs pytest+coverage twice (once per group) and
reports three numbers:

- `structural_percent_covered` -- raw line coverage from the structural-only
  run. Never adjusted; the user wants the full component count here.
- `hypothesis_percent_covered_raw` -- raw line coverage from the
  hypothesis-only run, same denominator (total statements in
  `python_code.py`) as above.
- `hypothesis_percent_covered_implemented` -- the same hypothesis-only run,
  but with statements belonging to "empty" methods excluded from both the
  numerator and the denominator. An "empty" method is a function/method
  whose entire body is a single `pass` statement (confirmed empirically:
  every non-`__init__`/non-property method sampled across 300 random models
  that has no real logic takes exactly this shape -- these are the
  generated `Operation`s from PROMPT.md's "907/9082 models fail because of
  empty pass-body operations" finding). Getters/setters and `__init__`
  always contain at least one real statement, so they're never excluded by
  this rule.

This is a PROTOTYPE script (see PROMPT.md / user request 2026-09-02): it
does NOT write into each model's code_metadata.json by default. Pass
--write-metadata to opt into that once the prototype numbers have been
reviewed and approved for a full-dataset run.

Usage:
    python scripts/validate_coverage_split.py --models-file PATH [--workers N]
                                                [--timeout SECONDS] [--dataset-dir PATH]
"""
from __future__ import annotations

import argparse
import ast
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
CODE_FILENAME = "python_code.py"
SOURCE_MODULE = "python_code"
METADATA_FILENAME = "code_metadata.json"
METADATA_KEY = "coverage_by_section_validation"
DEFAULT_TIMEOUT = 120


def load_cache(cache_path: Path) -> dict[str, dict]:
    """Read a JSONL cache of previously-completed results, keyed by model name.

    Tolerates a truncated last line (e.g. the process was killed mid-write)
    by skipping any line that fails to parse.
    """
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


def find_empty_method_lines(python_code_path: Path) -> tuple[set[int], int]:
    """Return (line numbers of `pass`-only-body functions, count of such functions).

    Walks every FunctionDef/AsyncFunctionDef in the module (methods and
    top-level functions alike). A function counts as "empty" only when its
    body is *exactly* one `pass` statement -- no docstring, no other code.
    """
    tree = ast.parse(python_code_path.read_text())
    empty_lines: set[int] = set()
    count = 0
    for node in ast.walk(tree):
        if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)):
            if len(node.body) == 1 and isinstance(node.body[0], ast.Pass):
                empty_lines.add(node.body[0].lineno)
                count += 1
    return empty_lines, count


def run_pytest_coverage(
    model_dir: Path, marker_expr: str, timeout: int, hypothesis_home: str,
    scratch_dir: str, tag: str,
) -> dict:
    """Run pytest against a marker-selected subset of test_hypothesis.py with coverage."""
    cov_json_path = Path(scratch_dir) / f"{model_dir.name}.{tag}.cov.json"
    cov_data_path = Path(scratch_dir) / f"{model_dir.name}.{tag}.coverage"

    result = {
        "status": "unknown",
        "returncode": None,
        "duration_s": None,
        "num_statements": None,
        "covered_lines": None,
        "missing_lines": None,
        "percent_covered": None,
        "executed_lines": None,
        "missing_lines_list": None,
        "tests_selected": None,
        "error_message": None,
    }

    env = dict(os.environ)
    env["PYTHONDONTWRITEBYTECODE"] = "1"
    env["HYPOTHESIS_STORAGE_DIRECTORY"] = hypothesis_home
    env["COVERAGE_FILE"] = str(cov_data_path)

    start = time.monotonic()
    try:
        proc = subprocess.run(
            [
                sys.executable, "-m", "pytest", TEST_FILENAME,
                "-m", marker_expr,
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

    tail_lines = [l for l in (proc.stdout or "").strip().splitlines() if l.strip()]
    last_line = tail_lines[-1] if tail_lines else ""
    result["tests_selected"] = last_line

    if proc.returncode == 5:
        # No tests matched this marker (e.g. a model with zero @given tests).
        result["status"] = "no_tests_selected"
        cov_json_path.unlink(missing_ok=True)
        return result

    if not cov_json_path.is_file():
        result["status"] = "no_coverage_data"
        result["error_message"] = last_line or (proc.stderr or "").strip()[-500:]
        return result

    try:
        cov_summary = json.loads(cov_json_path.read_text())
        file_data = cov_summary["files"][CODE_FILENAME]
        totals = file_data["summary"]
        result["num_statements"] = totals["num_statements"]
        result["covered_lines"] = totals["covered_lines"]
        result["missing_lines"] = totals["missing_lines"]
        result["percent_covered"] = round(totals["percent_covered"], 2)
        result["executed_lines"] = file_data["executed_lines"]
        result["missing_lines_list"] = file_data["missing_lines"]
        result["status"] = "measured" if proc.returncode == 0 else "measured_with_test_failures"
    except (KeyError, json.JSONDecodeError) as exc:
        result["status"] = "parse_error"
        result["error_message"] = str(exc)
    finally:
        cov_json_path.unlink(missing_ok=True)

    return result


def adjust_for_empty_methods(hyp_result: dict, empty_lines: set[int]) -> dict:
    """Recompute hyp_result's coverage percentage with empty-method lines excluded."""
    adjusted = {
        "num_statements": None,
        "covered_lines": None,
        "percent_covered": None,
        "empty_lines_excluded": None,
    }
    if hyp_result["status"] not in ("measured", "measured_with_test_failures"):
        return adjusted

    executed = set(hyp_result["executed_lines"] or [])
    missing = set(hyp_result["missing_lines_list"] or [])
    all_statement_lines = executed | missing

    excluded = empty_lines & all_statement_lines
    adjusted_total = len(all_statement_lines) - len(excluded)
    adjusted_covered = len(executed - excluded)

    adjusted["num_statements"] = adjusted_total
    adjusted["covered_lines"] = adjusted_covered
    adjusted["percent_covered"] = (
        round(100.0 * adjusted_covered / adjusted_total, 2) if adjusted_total > 0 else None
    )
    adjusted["empty_lines_excluded"] = len(excluded)
    return adjusted


def strip_line_lists(result: dict) -> dict:
    """Drop the raw executed/missing line arrays before writing to the report (keep it small)."""
    trimmed = dict(result)
    trimmed.pop("executed_lines", None)
    trimmed.pop("missing_lines_list", None)
    return trimmed


def validate_model(model_dir: Path, timeout: int, hypothesis_home: str, scratch_dir: str) -> dict:
    checked_at = datetime.datetime.now(datetime.timezone.utc).isoformat()
    result = {
        "model": model_dir.name,
        "checked_at": checked_at,
        "python_version": platform.python_version(),
        "status": "missing_file",
        "empty_method_count": None,
        "structural": None,
        "hypothesis_raw": None,
        "hypothesis_implemented_only": None,
        "error_message": None,
    }

    test_path = model_dir / TEST_FILENAME
    code_path = model_dir / CODE_FILENAME
    if not test_path.is_file():
        result["error_message"] = f"{TEST_FILENAME} not found in {model_dir.name}"
        return result
    if not code_path.is_file():
        result["error_message"] = f"{CODE_FILENAME} not found in {model_dir.name}"
        return result

    try:
        empty_lines, empty_count = find_empty_method_lines(code_path)
    except SyntaxError as exc:
        result["status"] = "code_parse_error"
        result["error_message"] = str(exc)
        return result

    result["empty_method_count"] = empty_count

    structural = run_pytest_coverage(
        model_dir, "not hypothesis", timeout, hypothesis_home, scratch_dir, "structural"
    )
    hyp = run_pytest_coverage(
        model_dir, "hypothesis", timeout, hypothesis_home, scratch_dir, "hypothesis"
    )
    hyp_adjusted = adjust_for_empty_methods(hyp, empty_lines)

    result["structural"] = strip_line_lists(structural)
    result["hypothesis_raw"] = strip_line_lists(hyp)
    result["hypothesis_implemented_only"] = hyp_adjusted
    result["status"] = "measured"
    return result


def build_report(results: list[dict]) -> dict:
    total = len(results)
    by_status: dict[str, int] = {}
    for r in results:
        by_status[r["status"]] = by_status.get(r["status"], 0) + 1

    def pct_values(key_path):
        vals = []
        for r in results:
            node = r
            for key in key_path:
                node = node.get(key) if isinstance(node, dict) else None
                if node is None:
                    break
            if node is not None:
                vals.append(node)
        return vals

    structural_pcts = pct_values(["structural", "percent_covered"])
    hyp_raw_pcts = pct_values(["hypothesis_raw", "percent_covered"])
    hyp_impl_pcts = pct_values(["hypothesis_implemented_only", "percent_covered"])

    def avg(vals):
        return round(sum(vals) / len(vals), 2) if vals else None

    return {
        "generated_at": datetime.datetime.now(datetime.timezone.utc).isoformat(),
        "total_models": total,
        "by_status": by_status,
        "avg_structural_percent_covered": avg(structural_pcts),
        "avg_hypothesis_percent_covered_raw": avg(hyp_raw_pcts),
        "avg_hypothesis_percent_covered_implemented": avg(hyp_impl_pcts),
        "measured_structural_count": len(structural_pcts),
        "measured_hypothesis_raw_count": len(hyp_raw_pcts),
        "measured_hypothesis_implemented_count": len(hyp_impl_pcts),
        "results": results,
    }


def render_markdown_report(report: dict) -> str:
    lines = [
        "# Coverage-by-section Prototype Report",
        "",
        f"Generated: {report['generated_at']}",
        "",
        f"- **Total models checked:** {report['total_models']}",
        f"- **Avg structural coverage:** {report['avg_structural_percent_covered']}% "
        f"({report['measured_structural_count']} measured)",
        f"- **Avg hypothesis coverage (raw):** {report['avg_hypothesis_percent_covered_raw']}% "
        f"({report['measured_hypothesis_raw_count']} measured)",
        f"- **Avg hypothesis coverage (implemented-only):** "
        f"{report['avg_hypothesis_percent_covered_implemented']}% "
        f"({report['measured_hypothesis_implemented_count']} measured)",
        "",
        "## Breakdown by status",
        "",
        "| Status | Count |",
        "|---|---|",
    ]
    for status, count in sorted(report["by_status"].items(), key=lambda kv: -kv[1]):
        lines.append(f"| {status} | {count} |")
    lines += [
        "",
        "## Per-model detail",
        "",
        "| Model | Empty methods | Structural % | Hypothesis % (raw) | Hypothesis % (implemented) |",
        "|---|---|---|---|---|",
    ]
    for r in report["results"]:
        struct_pct = (r.get("structural") or {}).get("percent_covered")
        hyp_raw_pct = (r.get("hypothesis_raw") or {}).get("percent_covered")
        hyp_impl_pct = (r.get("hypothesis_implemented_only") or {}).get("percent_covered")
        lines.append(
            f"| {r['model']} | {r.get('empty_method_count')} | {struct_pct} | {hyp_raw_pct} | {hyp_impl_pct} |"
        )
    lines += ["", "Full per-model detail: see `coverage_split_prototype_report.json`."]
    return "\n".join(lines) + "\n"


def write_metadata(model_dir: Path, result: dict) -> bool:
    metadata_path = model_dir / METADATA_FILENAME
    if not metadata_path.is_file():
        return False
    try:
        metadata = json.loads(metadata_path.read_text())
    except json.JSONDecodeError:
        return False
    metadata[METADATA_KEY] = {
        "checked_at": result["checked_at"],
        "python_version": result["python_version"],
        "empty_method_count": result["empty_method_count"],
        "structural_percent_covered": (result.get("structural") or {}).get("percent_covered"),
        "hypothesis_percent_covered_raw": (result.get("hypothesis_raw") or {}).get("percent_covered"),
        "hypothesis_percent_covered_implemented": (result.get("hypothesis_implemented_only") or {}).get("percent_covered"),
    }
    metadata_path.write_text(json.dumps(metadata, indent=2) + "\n")
    return True


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument(
        "--dataset-dir", type=Path,
        default=Path(__file__).resolve().parent.parent / "Dataset",
    )
    parser.add_argument(
        "--reports-dir", type=Path,
        default=Path(__file__).resolve().parent.parent / "reports",
    )
    parser.add_argument("--models-file", type=Path, default=None, help="File with one model dir name per line")
    parser.add_argument("--report-name", type=str, default="coverage_split_prototype_report")
    parser.add_argument("--workers", type=int, default=8)
    parser.add_argument("--timeout", type=int, default=DEFAULT_TIMEOUT)
    parser.add_argument("--limit", type=int, default=None)
    parser.add_argument("--fresh", action="store_true",
                         help="Ignore any existing cache and recompute every model")
    parser.add_argument("--write-metadata", action="store_true",
                         help="Also write results into each model's code_metadata.json "
                              "(off by default -- this is a prototype script)")
    args = parser.parse_args()

    args.reports_dir.mkdir(parents=True, exist_ok=True)
    cache_path = args.reports_dir / f"{args.report_name}.cache.jsonl"

    cached_results: dict[str, dict] = {} if args.fresh else load_cache(cache_path)
    if args.fresh and cache_path.is_file():
        cache_path.unlink()

    all_model_dirs = find_model_dirs(args.dataset_dir, args.models_file, args.limit)
    total = len(all_model_dirs)
    model_dirs = [d for d in all_model_dirs if d.name not in cached_results]
    skipped = total - len(model_dirs)

    hypothesis_home = tempfile.mkdtemp(prefix="besser_hypothesis_db_")
    scratch_dir = tempfile.mkdtemp(prefix="besser_coverage_split_scratch_")
    print(f"Measuring split coverage for {total} models with {args.workers} workers...")
    if skipped:
        print(f"Resuming from cache: {skipped}/{total} already done, {len(model_dirs)} remaining "
              f"(pass --fresh to ignore the cache and recompute everything)")

    results: list[dict] = list(cached_results.values())
    done = skipped
    cache_file = cache_path.open("a")
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
                        "empty_method_count": None, "structural": None,
                        "hypothesis_raw": None, "hypothesis_implemented_only": None,
                    }
                results.append(result)
                cache_file.write(json.dumps(result) + "\n")
                cache_file.flush()
                done += 1
                if done % 25 == 0 or done == total:
                    print(f"  {done}/{total} processed...")
    finally:
        cache_file.close()
        shutil.rmtree(hypothesis_home, ignore_errors=True)
        shutil.rmtree(scratch_dir, ignore_errors=True)

    if args.write_metadata:
        written = 0
        for result in results:
            if result["status"] == "measured":
                model_dir = args.dataset_dir / result["model"]
                if write_metadata(model_dir, result):
                    written += 1
        print(f"Wrote {METADATA_KEY} into {written}/{len(results)} models' code_metadata.json")

    report = build_report(results)
    args.reports_dir.mkdir(parents=True, exist_ok=True)
    json_path = args.reports_dir / f"{args.report_name}.json"
    json_path.write_text(json.dumps(report, indent=2) + "\n")
    md_path = args.reports_dir / f"{args.report_name}.md"
    md_path.write_text(render_markdown_report(report))

    print()
    print(f"Measured: structural={report['measured_structural_count']}, "
          f"hyp_raw={report['measured_hypothesis_raw_count']}, "
          f"hyp_implemented={report['measured_hypothesis_implemented_count']} / {report['total_models']}")
    print(f"Avg structural coverage: {report['avg_structural_percent_covered']}%")
    print(f"Avg hypothesis coverage (raw): {report['avg_hypothesis_percent_covered_raw']}%")
    print(f"Avg hypothesis coverage (implemented-only): {report['avg_hypothesis_percent_covered_implemented']}%")
    print(f"Report written to {json_path} and {md_path}")


if __name__ == "__main__":
    main()
