#!/usr/bin/env python3
"""Measure line, branch, function, and structural coverage of `python_code.py`
achieved by `test_structural_full.py` (the deterministic-first suite from
generate_structural_tests.py) -- not the dataset's original `test_hypothesis.py`.
Writes results into each model's code_metadata.json under a new
"structural_coverage_validation" key (never touches any other key).

Only 4 of the 6 coverage "types" discussed are measured here -- condition/MC-DC
and full path coverage are deliberately not attempted; see the module-level
NOT_ATTEMPTED note at the bottom of this docstring for why.

Line and branch coverage come straight from coverage.py's own JSON report
(`--cov-branch` enables branch tracking; the JSON's `percent_statements_covered`
and `percent_branches_covered` fields keep these as two separate numbers, not
blended together the way the plain `percent_covered` field is when branch
coverage is on).

Function coverage is NOT taken from coverage.py's own per-function
breakdown: that groups entries by `__qualname__`, which silently MERGES a
`@property` getter and its `@x.setter` into one entry (both are literally
named the same inside the class body) -- confirmed empirically on model_1:
20 real `def` statements via ast, only 12 entries in coverage.py's own
`functions` field. Instead, this script walks python_code.py's AST itself
for every FunctionDef/AsyncFunctionDef's line range, and cross-references
against the JSON report's `executed_lines` list -- a function counts as
covered if ANY of its lines executed.

Structural coverage answers a different question than the first three: not
"how much of the code executed" but "how much of the DIAGRAM's declared
structure got verified by a passing test" -- reusing the same association-
end-to-attribute mapping and constructibility logic as
generate_structural_tests.py, plus that script's own generated test names
(`..._value_roundtrip`, `..._isa_...`, `assoc_..._link_reassign_clear`),
whose pass/fail/skip outcome is read from a `--junit-xml` report. The
denominator is every attribute/generalization/association the BUML model
actually declares (not just the ones a test got generated for), so a class
we couldn't construct (e.g. an empty-enum-typed required field) correctly
counts against the score rather than being quietly excluded.

NOT ATTEMPTED, and why:
- Condition/MC-DC coverage (every boolean sub-expression exercised both
  true and false): no standard, actively-maintained Python tool measures
  this well against arbitrary code, and this dataset's own bidirectional-
  setter conditionals are the main place it would matter -- building a
  reliable custom instrumenter for that, across 9,082 structurally varied
  models, is a much bigger undertaking than the other three metrics for a
  return we don't have evidence is worth it yet.
- Path coverage (every possible route through a function): combinatorially
  explodes even for modest functions with a few independent conditionals
  (2^n paths for n conditions) -- not a realistic target at this dataset's
  scale, and no meaningful partial version of it exists the way "percent of
  lines" or "percent of branches" does.

Usage:
    python scripts/validate_coverage_structural.py --models-file PATH [--workers N]
        [--dataset-dir PATH] [--reports-dir PATH] [--report-name NAME]
        [--timeout SECONDS] [--limit N] [--fresh] [--write-metadata]
        [--test-file NAME] [--metadata-key KEY]

By default measures test_structural_full.py, writing structural_coverage_validation.
Pass --test-file test_hypothesis.py to measure the original suite's line/branch/
function coverage instead (auto-derives --metadata-key
structural_coverage_validation_hypothesis) -- its 'structural' coverage number will
be ~0% regardless, since that sub-metric pattern-matches this generator's own test
names (see TEST_FILE_METADATA_KEYS above).
"""
from __future__ import annotations

import argparse
import ast
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

sys.path.insert(0, str(Path(__file__).resolve().parent))
from _common.buml import NEW_GLOB, OLD_GLOB, find_buml_file, load_domain_model  # noqa: E402
from _common.cache import load_cache, partition_cache  # noqa: E402
from _common.io import add_common_io_args, find_model_dirs, update_json_key  # noqa: E402
from _common.pool import run_models  # noqa: E402
from _common.report import render_status_table, write_reports  # noqa: E402

from besser.BUML.metamodel.structural import BinaryAssociation, Class  # noqa: E402

# Overridable via --test-file/--metadata-key (see main()); read from env
# vars rather than plain module constants because ProcessPoolExecutor
# workers on Windows use 'spawn' and re-import this file fresh in a new
# interpreter -- a `global TEST_FILENAME = ...` mutation in main() (parent
# process only) would never reach them. The parent sets these env vars
# before creating the pool; each worker's own fresh import then picks up
# the same overridden values. See validate_mutation.py for the identical
# pattern.
TEST_FILENAME = os.environ.get("VALIDATE_COVERAGE_STRUCTURAL_TEST_FILENAME", "test_structural_full.py")
SOURCE_MODULE = "python_code"
SOURCE_FILENAME = "python_code.py"
METADATA_FILENAME = "code_metadata.json"
METADATA_KEY = os.environ.get("VALIDATE_COVERAGE_STRUCTURAL_METADATA_KEY", "structural_coverage_validation")
# The 4th coverage type (structural/diagram-fidelity) pattern-matches test
# NAMES this script's own generator produces (..._value_roundtrip, _isa_,
# test_assoc_...) -- it is meaningless against test_hypothesis.py, which
# uses a different naming scheme entirely, and will just come back ~0% for
# every model rather than erroring. Line/branch/function coverage are
# unaffected by which test file runs and remain meaningful either way.
TEST_FILE_METADATA_KEYS = {
    "test_structural_full.py": "structural_coverage_validation",
    "test_hypothesis.py": "structural_coverage_validation_hypothesis",
    "test_combined.py": "combined_coverage_validation",
    "test_super_suite.py": "super_suite_coverage_validation",
}
DEFAULT_TIMEOUT = 60
# Execution-environment failures, not content-driven -- auto-retried under the
# same --report-name (see docs/DECISIONS.md 2026-10-01; this script never got
# that fix until the 2026-10-17 code-review pass found the gap).
RETRIABLE_STATUSES = frozenset({"timeout", "error"})


def structural_totals(model) -> dict:
    classes = [t for t in model.types if isinstance(t, Class)]
    return {
        "classes": len(classes),
        "attributes": sum(len(c.attributes) for c in classes),
        "generalizations": len(model.generalizations),
        "associations": len([a for a in model.associations if isinstance(a, BinaryAssociation)]),
    }


def function_ranges(source_path: Path) -> list[tuple[int, int]]:
    # encoding="utf-8" is required, not cosmetic: Path.read_text() otherwise
    # falls back to the OS locale encoding (not UTF-8 on Windows), which
    # mangles multi-byte characters. Confirmed real case: model_2210 has a
    # Norwegian enum literal "Årsstudie" -- valid Python 3 syntax under
    # UTF-8 (the file's actual encoding) -- that a locale-encoding read
    # corrupts into an invalid token, raising a false "invalid character"
    # SyntaxError. Nothing else in this pipeline re-parses python_code.py's
    # raw text this way (generate_structural_tests.py only imports it via
    # exec_module, which already follows Python's own UTF-8-default source
    # encoding rules), which is why this bug is unique to this script.
    tree = ast.parse(source_path.read_text(encoding="utf-8"))
    return [
        (node.lineno, node.end_lineno)
        for node in ast.walk(tree)
        if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef))
    ]


def parse_junit_outcomes(junit_path: Path) -> dict[str, str]:
    tree = ET.parse(junit_path)
    outcomes: dict[str, str] = {}
    for testcase in tree.iter("testcase"):
        name = testcase.get("name", "")
        if testcase.find("failure") is not None or testcase.find("error") is not None:
            outcomes[name] = "failed"
        elif testcase.find("skipped") is not None:
            outcomes[name] = "skipped"
        else:
            outcomes[name] = "passed"
    return outcomes


def classify_structural_outcomes(outcomes: dict[str, str]) -> dict:
    buckets = {"attributes": {"passed": 0, "skipped": 0, "failed": 0},
               "generalizations": {"passed": 0, "skipped": 0, "failed": 0},
               "associations": {"passed": 0, "skipped": 0, "failed": 0}}
    for name, outcome in outcomes.items():
        if name.endswith("_value_roundtrip"):
            bucket = "attributes"
        elif "_isa_" in name:
            bucket = "generalizations"
        elif name.startswith("test_assoc_"):
            bucket = "associations"
        else:
            continue
        buckets[bucket][outcome] = buckets[bucket].get(outcome, 0) + 1
    return buckets


def validate_model(model_dir: Path, timeout: int, hypothesis_home: str, scratch_dir: str) -> dict:
    checked_at = datetime.datetime.now(datetime.timezone.utc).isoformat()
    result = {
        "model": model_dir.name,
        "test_file": TEST_FILENAME,
        "checked_at": checked_at,
        "python_version": platform.python_version(),
        "status": "missing_file",
        "num_statements": None, "covered_lines": None, "line_percent_covered": None,
        "num_branches": None, "covered_branches": None, "branch_percent_covered": None,
        "total_functions": None, "covered_functions": None, "function_percent_covered": None,
        "structural_totals": None, "structural_outcomes": None, "structural_coverage_percent": None,
        "error_message": None,
    }

    test_path = model_dir / TEST_FILENAME
    code_path = model_dir / SOURCE_FILENAME
    buml_file = find_buml_file(model_dir)
    if not test_path.is_file():
        result["error_message"] = f"{TEST_FILENAME} not found"
        return result
    if not code_path.is_file():
        result["error_message"] = f"{SOURCE_FILENAME} not found"
        return result
    if buml_file is None:
        result["error_message"] = f"No {OLD_GLOB} or {NEW_GLOB} file found"
        return result

    try:
        model = load_domain_model(buml_file)
        totals = structural_totals(model)
    except Exception as exc:
        result["status"] = "buml_load_error"
        result["error_message"] = str(exc)
        return result

    cov_json_path = Path(scratch_dir) / f"{model_dir.name}.cov.json"
    junit_path = Path(scratch_dir) / f"{model_dir.name}.junit.xml"
    cov_data_path = Path(scratch_dir) / f"{model_dir.name}.coverage"

    env = dict(os.environ)
    env["PYTHONDONTWRITEBYTECODE"] = "1"
    env["HYPOTHESIS_STORAGE_DIRECTORY"] = hypothesis_home
    env["COVERAGE_FILE"] = str(cov_data_path)

    try:
        proc = subprocess.run(
            [
                sys.executable, "-m", "pytest", TEST_FILENAME,
                f"--cov={SOURCE_MODULE}", "--cov-branch",
                f"--cov-report=json:{cov_json_path}",
                f"--junit-xml={junit_path}",
                "-q", "-p", "no:cacheprovider", "--no-header",
            ],
            cwd=str(model_dir), capture_output=True, text=True,
            timeout=timeout, env=env,
        )
    except subprocess.TimeoutExpired:
        result["status"] = "timeout"
        result["error_message"] = f"Execution exceeded {timeout}s"
        return result
    finally:
        cov_data_path.unlink(missing_ok=True)

    if not cov_json_path.is_file() or not junit_path.is_file():
        # pytest-cov only emits a coverage JSON when the source module was
        # actually imported by at least one collected test -- with zero
        # tests collected (pytest exit code 5, "no tests ran"), coverage
        # never touches python_code.py at all, so cov_json_path never gets
        # written even though nothing went wrong. Confirmed real case:
        # model_650's python_code.py has zero classes (BUML `types=None`),
        # so generate_structural_tests.py correctly emits a test file with
        # zero test functions -- that's a genuinely-empty model, not a
        # failure, and shouldn't be lumped in with real no_coverage_data
        # cases (a crash, a timeout-adjacent hang, etc.) where something
        # that should have produced data didn't.
        empty_model = totals["classes"] == 0
        result["status"] = "empty_model" if empty_model else "no_coverage_data"
        result["structural_totals"] = totals
        if empty_model:
            result["structural_outcomes"] = {
                "attributes": {"passed": 0, "skipped": 0, "failed": 0},
                "generalizations": {"passed": 0, "skipped": 0, "failed": 0},
                "associations": {"passed": 0, "skipped": 0, "failed": 0},
            }
        else:
            tail = (proc.stdout or "").strip().splitlines()
            result["error_message"] = tail[-1] if tail else (proc.stderr or "").strip()[-500:]
        return result

    try:
        cov_summary = json.loads(cov_json_path.read_text(encoding="utf-8"))
        file_data = cov_summary["files"][SOURCE_FILENAME]
        totals_summary = file_data["summary"]

        result["num_statements"] = totals_summary["num_statements"]
        result["covered_lines"] = totals_summary["covered_lines"]
        result["line_percent_covered"] = round(totals_summary["percent_statements_covered"], 2)
        result["num_branches"] = totals_summary["num_branches"]
        result["covered_branches"] = totals_summary["covered_branches"]
        result["branch_percent_covered"] = (
            round(totals_summary["percent_branches_covered"], 2) if totals_summary["num_branches"] else None
        )

        executed = set(file_data["executed_lines"])
        ranges = function_ranges(code_path)
        covered_funcs = sum(1 for start, end in ranges if any(l in executed for l in range(start, end + 1)))
        result["total_functions"] = len(ranges)
        result["covered_functions"] = covered_funcs
        result["function_percent_covered"] = round(covered_funcs / len(ranges) * 100, 2) if ranges else None

        outcomes = parse_junit_outcomes(junit_path)
        structural_outcomes = classify_structural_outcomes(outcomes)
        result["structural_totals"] = totals
        result["structural_outcomes"] = structural_outcomes
        passed_total = sum(b["passed"] for b in structural_outcomes.values())
        grand_total = totals["attributes"] + totals["generalizations"] + totals["associations"]
        result["structural_coverage_percent"] = round(passed_total / grand_total * 100, 2) if grand_total else None

        result["status"] = "measured"
    except (KeyError, json.JSONDecodeError, ET.ParseError) as exc:
        result["status"] = "parse_error"
        result["error_message"] = str(exc)
    finally:
        cov_json_path.unlink(missing_ok=True)
        junit_path.unlink(missing_ok=True)

    return result


def write_metadata(model_dir: Path, result: dict) -> bool:
    """Merge this model's result into its code_metadata.json under METADATA_KEY.

    Same convention as every other writer in this repo: requires the file to
    already exist, never creates it, never touches any other key.
    """
    return update_json_key(model_dir / METADATA_FILENAME, METADATA_KEY, {
        "checked_at": result["checked_at"],
        "python_version": result["python_version"],
        "status": result["status"],
        "line_percent_covered": result["line_percent_covered"],
        "branch_percent_covered": result["branch_percent_covered"],
        "function_percent_covered": result["function_percent_covered"],
        "structural_coverage_percent": result["structural_coverage_percent"],
        "structural_totals": result["structural_totals"],
        "structural_outcomes": result["structural_outcomes"],
    })


def build_report(results: list[dict]) -> dict:
    total = len(results)
    by_status: dict[str, int] = {}
    for r in results:
        by_status[r["status"]] = by_status.get(r["status"], 0) + 1
    measured = [r for r in results if r["status"] == "measured"]
    empty_model_count = by_status.get("empty_model", 0)

    def avg(field):
        vals = [r[field] for r in measured if r.get(field) is not None]
        return round(sum(vals) / len(vals), 2) if vals else None

    return {
        "generated_at": datetime.datetime.now(datetime.timezone.utc).isoformat(),
        "total_models": total,
        "by_status": by_status,
        "measured_count": len(measured),
        "empty_model_count": empty_model_count,
        "avg_line_percent_covered": avg("line_percent_covered"),
        "avg_branch_percent_covered": avg("branch_percent_covered"),
        "avg_function_percent_covered": avg("function_percent_covered"),
        "avg_structural_coverage_percent": avg("structural_coverage_percent"),
        "results": results,
    }


def render_markdown_report(report: dict) -> str:
    lines = [
        "# Structural-Suite Coverage Report (line / branch / function / structural)",
        "",
        f"Generated: {report['generated_at']}",
        "",
        "Measures test_structural_full.py's coverage of python_code.py -- not "
        "the dataset's original test_hypothesis.py. Condition/MC-DC and path "
        "coverage are deliberately not measured; see the script's docstring.",
        "",
        f"- **Total models:** {report['total_models']}",
        f"- **Measured:** {report['measured_count']}",
        f"- **Empty models (0 classes, correctly 0 tests):** {report['empty_model_count']}",
        f"- **Avg line coverage:** {report['avg_line_percent_covered']}%",
        f"- **Avg branch coverage:** {report['avg_branch_percent_covered']}%",
        f"- **Avg function coverage:** {report['avg_function_percent_covered']}%",
        f"- **Avg structural coverage:** {report['avg_structural_coverage_percent']}%",
        "",
    ]
    lines += render_status_table(report["by_status"])
    lines += ["", "Full per-model detail: see the accompanying `.json` report."]
    return "\n".join(lines) + "\n"


def main() -> None:
    global TEST_FILENAME, METADATA_KEY
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    add_common_io_args(parser, __file__)
    parser.add_argument("--models-file", type=Path, default=None)
    parser.add_argument("--report-name", type=str, default="structural_coverage_report")
    parser.add_argument("--workers", type=int, default=8)
    parser.add_argument("--timeout", type=int, default=DEFAULT_TIMEOUT)
    parser.add_argument("--limit", type=int, default=None)
    parser.add_argument("--fresh", action="store_true",
                         help="Ignore any existing cache and recompute every model")
    parser.add_argument("--write-metadata", action="store_true",
                         help="Also write results into each model's code_metadata.json "
                              "under the 'structural_coverage_validation' key")
    parser.add_argument("--test-file", type=str, default=None,
                         help=f"Measure coverage of this test file instead of the default "
                              f"({TEST_FILENAME!r}) -- e.g. test_hypothesis.py. NOTE: the "
                              f"'structural' coverage type is meaningless for any file other "
                              f"than test_structural_full.py (name-pattern-matches this "
                              f"generator's own test names) -- line/branch/function remain valid.")
    parser.add_argument("--metadata-key", type=str, default=None,
                         help="Override the code_metadata.json key results are written under "
                              "(default: derived from --test-file, see TEST_FILE_METADATA_KEYS)")
    args = parser.parse_args()

    if args.test_file:
        TEST_FILENAME = args.test_file
    if args.metadata_key:
        METADATA_KEY = args.metadata_key
    elif args.test_file in TEST_FILE_METADATA_KEYS:
        METADATA_KEY = TEST_FILE_METADATA_KEYS[args.test_file]
    elif args.test_file and args.write_metadata:
        parser.error(
            f"--test-file {args.test_file!r} has no known default metadata key -- "
            f"pass --metadata-key explicitly with --write-metadata "
            f"(known test files: {sorted(TEST_FILE_METADATA_KEYS)})"
        )
    os.environ["VALIDATE_COVERAGE_STRUCTURAL_TEST_FILENAME"] = TEST_FILENAME
    os.environ["VALIDATE_COVERAGE_STRUCTURAL_METADATA_KEY"] = METADATA_KEY
    print(f"Test file: {TEST_FILENAME}  |  metadata key: {METADATA_KEY}")

    args.reports_dir.mkdir(parents=True, exist_ok=True)
    cache_path = args.reports_dir / f"{args.report_name}.cache.jsonl"

    cached_results_all: dict[str, dict] = {} if args.fresh else load_cache(cache_path, expected_test_file=TEST_FILENAME)
    if args.fresh and cache_path.is_file():
        cache_path.unlink()
    cached_results, retriable = partition_cache(cached_results_all, RETRIABLE_STATUSES)

    all_model_dirs = find_model_dirs(args.dataset_dir, args.models_file, args.limit)
    total = len(all_model_dirs)
    model_dirs = [d for d in all_model_dirs if d.name not in cached_results]
    skipped = total - len(model_dirs)

    hypothesis_home = tempfile.mkdtemp(prefix="besser_hypothesis_db_covstruct_")
    scratch_dir = tempfile.mkdtemp(prefix="besser_covstruct_scratch_")
    print(f"Measuring structural-suite coverage for {total} models with {args.workers} workers...")
    if skipped:
        print(f"Resuming from cache: {skipped}/{total} already done, {len(model_dirs)} remaining "
              f"(pass --fresh to ignore the cache and recompute everything)")
    if retriable:
        print(f"Auto-retrying {len(retriable)} previously-failed models from the cache -- "
              f"same report, no separate retry run needed")

    try:
        results = run_models(
            validate_model, model_dirs, worker_args=(args.timeout, hypothesis_home, scratch_dir),
            workers=args.workers, cache_path=cache_path, results=list(cached_results.values()),
            already_done=skipped, total=total,
            error_fields={"test_file": TEST_FILENAME, "line_percent_covered": None,
                          "branch_percent_covered": None, "function_percent_covered": None,
                          "structural_coverage_percent": None, "structural_totals": None,
                          "structural_outcomes": None},
        )
    finally:
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
    json_path, md_path = write_reports(args.reports_dir, args.report_name, report, render_markdown_report(report))

    print()
    print(f"Measured: {report['measured_count']}/{report['total_models']}")
    print(f"Avg line/branch/function/structural coverage: "
          f"{report['avg_line_percent_covered']}% / {report['avg_branch_percent_covered']}% / "
          f"{report['avg_function_percent_covered']}% / {report['avg_structural_coverage_percent']}%")
    print(f"Report written to {json_path} and {md_path}")


if __name__ == "__main__":
    main()
