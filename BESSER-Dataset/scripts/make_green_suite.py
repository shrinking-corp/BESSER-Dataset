#!/usr/bin/env python3
"""Write `<test-file stem>_green.py` per model: the given test suite with
every test that fails on the unmutated python_code.py removed.

Same rule `generate_super_suite.py` applies to the super suite (see
`_common/green.py` for why a suite must pass on the original code before
any mutation score from it means anything). Use this to put every other
suite in a comparison -- e.g. the `test_combined.py` baseline, or the
dataset's original `test_hypothesis.py` -- on exactly the same footing.
The input file is never modified; a model whose suite can't be made green
gets no output file (any stale one is deleted), and every removed test is
listed in the report with its failure reason.

Needs pytest + hypothesis, i.e. the main `.venv`.

Usage:
    python scripts/make_green_suite.py --test-file test_combined.py
        --models-file PATH [--workers N] [--hypothesis-seed N]
        [--timeout SECONDS] [--report-name NAME] [--limit N] [--fresh]
"""
from __future__ import annotations

import argparse
import datetime
import platform
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from _common.cache import load_cache, partition_cache  # noqa: E402
from _common.green import describe_green_result, make_green, make_test_names_unique  # noqa: E402
from _common.io import add_common_io_args, find_model_dirs  # noqa: E402
from _common.pool import run_models  # noqa: E402
from _common.report import render_status_table, write_reports  # noqa: E402

DEFAULT_TIMEOUT = 360
RETRIABLE_STATUSES = frozenset({"error", "timeout"})


def green_model(model_dir: Path, test_file: str, output_file: str,
                hypothesis_seed: int | None, timeout: float) -> dict:
    result = {
        "model": model_dir.name,
        "test_file": test_file,
        "checked_at": datetime.datetime.now(datetime.timezone.utc).isoformat(),
        "python_version": platform.python_version(),
        "status": "missing_file",
        "duplicate_test_names_renamed": 0,
        "tests_before_pruning": None,
        "tests_after_pruning": None,
        "removed_tests": [],
        "error_message": None,
    }
    input_path = model_dir / test_file
    output_path = model_dir / output_file
    if not input_path.is_file():
        result["error_message"] = f"{test_file} not found"
        output_path.unlink(missing_ok=True)
        return result
    try:
        source, result["duplicate_test_names_renamed"] = make_test_names_unique(
            input_path.read_text(encoding="utf-8"))
    except SyntaxError as exc:
        result["status"] = "collection_error"
        result["error_message"] = f"{exc.msg} (line {exc.lineno})"
        output_path.unlink(missing_ok=True)
        return result
    try:
        green = make_green(source, model_dir, output_file, hypothesis_seed, timeout)
        result["status"] = green["status"]
        result["tests_before_pruning"] = green["tests_before"]
        result["tests_after_pruning"] = green["tests_after"]
        result["removed_tests"] = green["removed"]
        result["error_message"] = green["error_message"]
        if green["status"] == "green":
            output_path.write_text(green["source"], encoding="utf-8")
        else:
            output_path.unlink(missing_ok=True)
    except Exception as exc:
        result["status"] = "error"
        result["error_message"] = str(exc)
    return result


def build_report(results: list[dict], test_file: str, output_file: str) -> dict:
    by_status: dict[str, int] = {}
    for r in results:
        by_status[r["status"]] = by_status.get(r["status"], 0) + 1
    green = [r for r in results if r["status"] == "green"]
    return {
        "generated_at": datetime.datetime.now(datetime.timezone.utc).isoformat(),
        "test_file": test_file,
        "output_file": output_file,
        "total_models": len(results),
        "by_status": by_status,
        "green_count": len(green),
        "models_with_removed_tests": sum(1 for r in green if r.get("removed_tests")),
        "total_tests_removed": sum(len(r.get("removed_tests") or []) for r in results),
        "total_tests_after_pruning": sum(r["tests_after_pruning"] or 0 for r in green),
        "results": results,
    }


def render_markdown_report(report: dict) -> str:
    lines = [
        f"# Green Suite Report: `{report['test_file']}` -> `{report['output_file']}`",
        "",
        f"Generated: {report['generated_at']}",
        "",
        f"- **Total models:** {report['total_models']}",
        f"- **Green suites written:** {report['green_count']} ({report['total_tests_after_pruning']} tests total)",
        f"- **Tests removed for failing on unmutated code:** {report['total_tests_removed']} "
        f"(in {report['models_with_removed_tests']} green models)",
        "",
    ]
    lines += render_status_table(report["by_status"])
    lines += ["", "Removed tests and reasons per model: see the accompanying `.json` report."]
    return "\n".join(lines) + "\n"


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    add_common_io_args(parser, __file__)
    parser.add_argument("--test-file", type=str, required=True, help="e.g. test_combined.py")
    parser.add_argument("--output-file", type=str, default=None,
                         help="Default: <test-file stem>_green.py")
    parser.add_argument("--models-file", type=Path, default=None)
    parser.add_argument("--report-name", type=str, default=None,
                         help="Default: green_<test-file stem>_report")
    parser.add_argument("--workers", type=int, default=8)
    parser.add_argument("--limit", type=int, default=None)
    parser.add_argument("--fresh", action="store_true", help="Ignore any existing cache and recompute every model")
    parser.add_argument("--hypothesis-seed", type=int, default=0,
                         help="Seed for the unmutated run -- use the same seed as the mutation run")
    parser.add_argument("--timeout", type=float, default=DEFAULT_TIMEOUT,
                         help="Wall-clock cap for one unmutated run of a model's suite, seconds")
    args = parser.parse_args()

    stem = Path(args.test_file).stem
    output_file = args.output_file or f"{stem}_green.py"
    report_name = args.report_name or f"green_{stem}_report"

    args.reports_dir.mkdir(parents=True, exist_ok=True)
    cache_path = args.reports_dir / f"{report_name}.cache.jsonl"
    cached_results_all: dict[str, dict] = {} if args.fresh else load_cache(cache_path, expected_test_file=args.test_file)
    if args.fresh and cache_path.is_file():
        cache_path.unlink()
    cached_results, retriable = partition_cache(cached_results_all, RETRIABLE_STATUSES)

    all_model_dirs = find_model_dirs(args.dataset_dir, args.models_file, args.limit)
    total = len(all_model_dirs)
    model_dirs = [d for d in all_model_dirs if d.name not in cached_results]
    skipped = total - len(model_dirs)

    print(f"Pruning {args.test_file} -> {output_file} for {total} models with {args.workers} workers "
          f"(hypothesis seed={args.hypothesis_seed}, timeout={args.timeout}s)...")
    if skipped:
        print(f"Resuming from cache: {skipped}/{total} already done, {len(model_dirs)} remaining "
              f"(pass --fresh to ignore the cache and recompute everything)")
    if retriable:
        print(f"Auto-retrying {len(retriable)} previously-failed models from the cache -- "
              f"same report, no separate retry run needed")

    results = run_models(
        green_model, model_dirs,
        worker_args=(args.test_file, output_file, args.hypothesis_seed, args.timeout),
        workers=args.workers, cache_path=cache_path, results=list(cached_results.values()),
        already_done=skipped, total=total, describe=describe_green_result,
        error_fields={"test_file": args.test_file},
    )

    report = build_report(results, args.test_file, output_file)
    json_path, md_path = write_reports(args.reports_dir, report_name, report, render_markdown_report(report))

    print()
    print(f"Green: {report['green_count']}/{report['total_models']}  |  "
          f"tests removed: {report['total_tests_removed']}")
    print(f"Report written to {json_path} and {md_path}")


if __name__ == "__main__":
    main()
