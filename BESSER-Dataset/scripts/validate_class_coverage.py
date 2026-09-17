#!/usr/bin/env python3
"""Class coverage: of every class that actually exists in `python_code.py`
(per tree-sitter's `code_structure.json`), how many got at least one PASSING
test?

Denominator: tree-sitter's class list -- independent of the BUML model and
of this project's own test generator, so it isn't affected by either's
name-resolution quirks (e.g. the "#"-character bug in generate_structural_tests.py).

Numerator: a class counts as covered if any test in the target file that
PASSED (per pytest's --junit-xml output) references that class name, either
as a direct constructor call (`ClassName(...)`) or as an isinstance check
(`isinstance(x, ClassName)`, including the tuple form). Reference detection
is a single AST walk per test function; a class referenced by an ERRORED,
FAILED, or SKIPPED test does not count -- the test ran and didn't establish
anything trustworthy about that class.

Usage:
    python scripts/validate_class_coverage.py --models-file PATH [--workers N]
        [--dataset-dir PATH] [--reports-dir PATH] [--report-name NAME]
        [--timeout SECONDS] [--limit N] [--fresh] [--write-metadata]
        [--test-file NAME] [--metadata-key KEY]

By default measures test_structural_full.py, writing class_coverage_validation.
Pass --test-file test_hypothesis.py to measure the original suite instead
(auto-derives --metadata-key class_coverage_validation_hypothesis).
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
import xml.etree.ElementTree as ET
from pathlib import Path

CODE_STRUCTURE_FILENAME = "code_structure.json"
METADATA_FILENAME = "code_metadata.json"
DEFAULT_TIMEOUT = 60

# Overridable via --test-file/--metadata-key; see validate_coverage_structural.py
# for why this reads from env vars rather than a plain module constant
# (ProcessPoolExecutor workers on Windows re-import this file fresh via 'spawn').
TEST_FILENAME = os.environ.get("VALIDATE_CLASS_COVERAGE_TEST_FILENAME", "test_structural_full.py")
METADATA_KEY = os.environ.get("VALIDATE_CLASS_COVERAGE_METADATA_KEY", "class_coverage_validation")
TEST_FILE_METADATA_KEYS = {
    "test_structural_full.py": "class_coverage_validation",
    "test_hypothesis.py": "class_coverage_validation_hypothesis",
    "test_combined.py": "combined_class_coverage_validation",
}


def find_model_dirs(dataset_dir: Path, models_file: Path | None, limit: int | None) -> list[Path]:
    if models_file:
        names = [l.strip() for l in models_file.read_text().splitlines() if l.strip()]
        dirs = [dataset_dir / name for name in names]
    else:
        dirs = sorted(p for p in dataset_dir.iterdir() if p.is_dir())
    if limit:
        dirs = dirs[:limit]
    return dirs


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


def real_class_names(code_structure_path: Path) -> list[str]:
    data = json.loads(code_structure_path.read_text(encoding="utf-8"))
    return [c["name"] for c in data.get("classes", [])]


def _referenced_class_names(call: ast.Call, known: set[str]) -> set[str]:
    """Class names `call` references, if it's a constructor call or an
    isinstance()/issubclass() check against one or more known names."""
    found: set[str] = set()
    func = call.func
    if isinstance(func, ast.Name) and func.id in known:
        found.add(func.id)
    if isinstance(func, ast.Name) and func.id in ("isinstance", "issubclass") and len(call.args) >= 2:
        target = call.args[1]
        candidates = target.elts if isinstance(target, (ast.Tuple, ast.List)) else [target]
        for c in candidates:
            if isinstance(c, ast.Name) and c.id in known:
                found.add(c.id)
    return found


def class_references_by_test(test_source_path: Path, known_classes: list[str]) -> dict[str, set[str]]:
    """test function name -> set of known class names it references."""
    known = set(known_classes)
    tree = ast.parse(test_source_path.read_text(encoding="utf-8"))
    result: dict[str, set[str]] = {}
    for node in ast.walk(tree):
        if not isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)):
            continue
        if not node.name.startswith("test_"):
            continue
        refs: set[str] = set()
        for sub in ast.walk(node):
            if isinstance(sub, ast.Call):
                refs |= _referenced_class_names(sub, known)
        result[node.name] = refs
    return result


def parse_junit_pass(junit_path: Path) -> dict[str, bool]:
    """test name -> True if it passed (no failure/error/skip child)."""
    tree = ET.parse(junit_path)
    outcomes: dict[str, bool] = {}
    for testcase in tree.iter("testcase"):
        name = testcase.get("name", "")
        passed = (
            testcase.find("failure") is None
            and testcase.find("error") is None
            and testcase.find("skipped") is None
        )
        outcomes[name] = passed
    return outcomes


def validate_model(model_dir: Path, timeout: int, hypothesis_home: str, scratch_dir: str) -> dict:
    checked_at = datetime.datetime.now(datetime.timezone.utc).isoformat()
    result = {
        "model": model_dir.name,
        "checked_at": checked_at,
        "python_version": platform.python_version(),
        "status": "missing_file",
        "total_classes": None,
        "covered_classes": None,
        "class_coverage_percent": None,
        "covered_class_names": None,
        "uncovered_class_names": None,
        "error_message": None,
    }

    cs_path = model_dir / CODE_STRUCTURE_FILENAME
    test_path = model_dir / TEST_FILENAME
    if not cs_path.is_file():
        result["error_message"] = f"{CODE_STRUCTURE_FILENAME} not found"
        return result
    if not test_path.is_file():
        result["error_message"] = f"{TEST_FILENAME} not found"
        return result

    try:
        classes = real_class_names(cs_path)
    except Exception as exc:
        result["status"] = "code_structure_parse_error"
        result["error_message"] = str(exc)
        return result

    result["total_classes"] = len(classes)
    if not classes:
        result["status"] = "empty_model"
        result["covered_classes"] = 0
        result["class_coverage_percent"] = None
        result["covered_class_names"] = []
        result["uncovered_class_names"] = []
        return result

    try:
        refs_by_test = class_references_by_test(test_path, classes)
    except SyntaxError as exc:
        result["status"] = "test_file_parse_error"
        result["error_message"] = str(exc)
        return result

    junit_path = Path(scratch_dir) / f"{model_dir.name}.junit.xml"
    env = dict(os.environ)
    env["PYTHONDONTWRITEBYTECODE"] = "1"
    env["HYPOTHESIS_STORAGE_DIRECTORY"] = hypothesis_home
    try:
        proc = subprocess.run(
            [sys.executable, "-m", "pytest", TEST_FILENAME,
             f"--junit-xml={junit_path}", "-q", "-p", "no:cacheprovider", "--no-header"],
            cwd=str(model_dir), capture_output=True, text=True, timeout=timeout, env=env,
        )
    except subprocess.TimeoutExpired:
        result["status"] = "timeout"
        result["error_message"] = f"Execution exceeded {timeout}s"
        return result

    if not junit_path.is_file():
        result["status"] = "no_test_data"
        tail = (proc.stdout or "").strip().splitlines()
        result["error_message"] = tail[-1] if tail else (proc.stderr or "").strip()[-500:]
        return result

    try:
        passed_by_test = parse_junit_pass(junit_path)
    except ET.ParseError as exc:
        result["status"] = "parse_error"
        result["error_message"] = str(exc)
        return result
    finally:
        junit_path.unlink(missing_ok=True)

    covered: set[str] = set()
    for test_name, refs in refs_by_test.items():
        if not refs:
            continue
        # pytest's testcase name is the bare function name for non-parametrized
        # tests; match on suffix to tolerate a parametrize-id suffix if present.
        test_passed = passed_by_test.get(test_name)
        if test_passed is None:
            test_passed = next((v for k, v in passed_by_test.items() if k.startswith(test_name)), None)
        if test_passed:
            covered |= refs

    covered_names = sorted(c for c in classes if c in covered)
    uncovered_names = sorted(c for c in classes if c not in covered)
    result["status"] = "measured"
    result["covered_classes"] = len(covered_names)
    result["class_coverage_percent"] = round(len(covered_names) / len(classes) * 100, 2)
    result["covered_class_names"] = covered_names
    result["uncovered_class_names"] = uncovered_names
    return result


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
        "status": result["status"],
        "total_classes": result["total_classes"],
        "covered_classes": result["covered_classes"],
        "class_coverage_percent": result["class_coverage_percent"],
        "uncovered_class_names": result["uncovered_class_names"],
    }
    metadata_path.write_text(json.dumps(metadata, indent=2) + "\n")
    return True


def build_report(results: list[dict]) -> dict:
    total = len(results)
    by_status: dict[str, int] = {}
    for r in results:
        by_status[r["status"]] = by_status.get(r["status"], 0) + 1
    measured = [r for r in results if r["status"] == "measured"]
    percents = [r["class_coverage_percent"] for r in measured if r["class_coverage_percent"] is not None]
    return {
        "generated_at": datetime.datetime.now(datetime.timezone.utc).isoformat(),
        "test_file": TEST_FILENAME,
        "total_models": total,
        "by_status": by_status,
        "measured_count": len(measured),
        "avg_class_coverage_percent": round(sum(percents) / len(percents), 2) if percents else None,
        "results": results,
    }


def render_markdown_report(report: dict) -> str:
    lines = [
        "# Class Coverage Report",
        "",
        f"Generated: {report['generated_at']}",
        f"Test file measured: `{report['test_file']}`",
        "",
        "Of every class that actually exists in python_code.py (per tree-sitter's "
        "code_structure.json), what fraction got at least one passing test "
        "(a constructor call or isinstance() check inside a test that passed)?",
        "",
        f"- **Total models:** {report['total_models']}",
        f"- **Measured:** {report['measured_count']}",
        f"- **Avg class coverage:** {report['avg_class_coverage_percent']}%",
        "",
        "## Breakdown by status",
        "",
        "| Status | Count |",
        "|---|---|",
    ]
    for status, count in sorted(report["by_status"].items(), key=lambda kv: -kv[1]):
        lines.append(f"| {status} | {count} |")
    lines += ["", "Full per-model detail, including uncovered class names: see the accompanying `.json` report."]
    return "\n".join(lines) + "\n"


def main() -> None:
    global TEST_FILENAME, METADATA_KEY
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--dataset-dir", type=Path, default=Path(__file__).resolve().parent.parent / "Dataset")
    parser.add_argument("--reports-dir", type=Path, default=Path(__file__).resolve().parent.parent / "reports")
    parser.add_argument("--models-file", type=Path, default=None)
    parser.add_argument("--report-name", type=str, default="class_coverage_report")
    parser.add_argument("--workers", type=int, default=8)
    parser.add_argument("--timeout", type=int, default=DEFAULT_TIMEOUT)
    parser.add_argument("--limit", type=int, default=None)
    parser.add_argument("--fresh", action="store_true", help="Ignore any existing cache and recompute every model")
    parser.add_argument("--write-metadata", action="store_true",
                         help="Also write results into each model's code_metadata.json")
    parser.add_argument("--test-file", type=str, default=None,
                         help=f"Measure class coverage of this test file instead of the default "
                              f"({TEST_FILENAME!r}) -- e.g. test_hypothesis.py")
    parser.add_argument("--metadata-key", type=str, default=None,
                         help="Override the code_metadata.json key results are written under "
                              "(default: derived from --test-file, see TEST_FILE_METADATA_KEYS)")
    args = parser.parse_args()

    if args.test_file:
        TEST_FILENAME = args.test_file
    if args.metadata_key:
        METADATA_KEY = args.metadata_key
    elif args.test_file:
        if args.test_file not in TEST_FILE_METADATA_KEYS:
            parser.error(
                f"--test-file {args.test_file!r} has no known default metadata key -- "
                f"pass --metadata-key explicitly (known test files: {sorted(TEST_FILE_METADATA_KEYS)})"
            )
        METADATA_KEY = TEST_FILE_METADATA_KEYS[args.test_file]
    os.environ["VALIDATE_CLASS_COVERAGE_TEST_FILENAME"] = TEST_FILENAME
    os.environ["VALIDATE_CLASS_COVERAGE_METADATA_KEY"] = METADATA_KEY
    print(f"Test file: {TEST_FILENAME}  |  metadata key: {METADATA_KEY}")

    args.reports_dir.mkdir(parents=True, exist_ok=True)
    cache_path = args.reports_dir / f"{args.report_name}.cache.jsonl"

    cached_results: dict[str, dict] = {} if args.fresh else load_cache(cache_path)
    if args.fresh and cache_path.is_file():
        cache_path.unlink()

    all_model_dirs = find_model_dirs(args.dataset_dir, args.models_file, args.limit)
    total = len(all_model_dirs)
    model_dirs = [d for d in all_model_dirs if d.name not in cached_results]
    skipped = total - len(model_dirs)

    hypothesis_home = tempfile.mkdtemp(prefix="besser_hypothesis_db_classcov_")
    scratch_dir = tempfile.mkdtemp(prefix="besser_classcov_scratch_")
    print(f"Measuring class coverage for {total} models with {args.workers} workers...")
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
                        "total_classes": None, "covered_classes": None, "class_coverage_percent": None,
                        "covered_class_names": None, "uncovered_class_names": None,
                    }
                results.append(result)
                cache_file.write(json.dumps(result) + "\n")
                cache_file.flush()
                done += 1
                if done % 500 == 0 or done == total:
                    print(f"  {done}/{total} processed", flush=True)
    finally:
        cache_file.close()
        shutil.rmtree(hypothesis_home, ignore_errors=True)
        shutil.rmtree(scratch_dir, ignore_errors=True)

    if args.write_metadata:
        written = 0
        for result in results:
            if result["status"] in ("measured", "empty_model"):
                model_dir = args.dataset_dir / result["model"]
                if write_metadata(model_dir, result):
                    written += 1
        print(f"Wrote {METADATA_KEY} into {written}/{len(results)} models' code_metadata.json")

    report = build_report(results)
    json_path = args.reports_dir / f"{args.report_name}.json"
    json_path.write_text(json.dumps(report, indent=2) + "\n")
    md_path = args.reports_dir / f"{args.report_name}.md"
    md_path.write_text(render_markdown_report(report))

    print()
    print(f"Measured: {report['measured_count']}/{report['total_models']}")
    print(f"Avg class coverage: {report['avg_class_coverage_percent']}%")
    print(f"Report written to {json_path} and {md_path}")


if __name__ == "__main__":
    main()
