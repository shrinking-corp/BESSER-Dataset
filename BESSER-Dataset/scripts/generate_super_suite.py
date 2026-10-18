#!/usr/bin/env python3
"""Write `test_super_suite.py` per model: `test_combined.py` (old+new,
already deduped) + `test_behavioral.py` + `test_crosshair.py`, merged into
one file and pruned to its green subset -- the fixed per-model test oracle.

Merge steps:
1. CrossHair's output is sanitized first (`_common/crosshair.py`): invalid
   syntax skipped, tests of Python's own `Enum` internals dropped, and
   `datetime.<x>` module references rewritten to a private alias so they
   can't collide with the `datetime` class the other two parts import.
2. The parts are concatenated. Repeated top-level test names are renamed
   (`_common/green.py::make_test_names_unique`) -- Python keeps only the last
   definition of a name, so duplicates would otherwise silently never run.
3. The merged suite is run once on the unmutated python_code.py and every
   failing test is removed (`_common/green.py::make_green`), then re-run
   until green. A test that fails on the original code makes cosmic-ray
   count every mutant as killed, so it can't be part of a valid oracle --
   this was the cause of the inflated 92.66% result (see docs/DECISIONS.md
   2026-10-17). Removed tests are listed per model in the report.

Only a green suite is written. A model whose suite can't be made green
(collection error, timeout, no tests left) gets no `test_super_suite.py` --
any stale one from an earlier run is deleted, so a mutation run can never
pick up a broken leftover.

Needs pytest + hypothesis, i.e. the main `.venv`.

Usage:
    python scripts/generate_super_suite.py --models-file PATH
        [--workers N] [--dataset-dir PATH] [--reports-dir PATH]
        [--report-name NAME] [--limit N] [--fresh]
        [--hypothesis-seed N] [--timeout SECONDS]
"""
from __future__ import annotations

import argparse
import datetime
import platform
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from _common.cache import load_cache, partition_cache  # noqa: E402
from _common.crosshair import sanitize_crosshair_tests  # noqa: E402
from _common.green import describe_green_result, make_green, make_test_names_unique  # noqa: E402
from _common.io import add_common_io_args, find_model_dirs  # noqa: E402
from _common.pool import run_models  # noqa: E402
from _common.report import render_status_table, write_reports  # noqa: E402

COMBINED_FILENAME = "test_combined.py"
BEHAVIORAL_FILENAME = "test_behavioral.py"
CROSSHAIR_FILENAME = "test_crosshair.py"
OUTPUT_FILENAME = "test_super_suite.py"
DEFAULT_TIMEOUT = 360
# "error"/"timeout" are execution-environment failures, retried on a plain
# re-run under the same --report-name. "missing_combined"/"collection_error"/
# "no_tests"/"not_green" are deterministic facts about the inputs.
RETRIABLE_STATUSES = frozenset({"error", "timeout"})


def _count_tests(source: str) -> int:
    return source.count("\ndef test_") + (1 if source.startswith("def test_") else 0)


def merge_model(model_dir: Path, hypothesis_seed: int | None, timeout: float) -> dict:
    checked_at = datetime.datetime.now(datetime.timezone.utc).isoformat()
    result = {
        "model": model_dir.name,
        "checked_at": checked_at,
        "python_version": platform.python_version(),
        "status": "missing_combined",
        "behavioral_tests_added": 0,
        "crosshair_tests_added": 0,
        "crosshair_skipped_invalid_syntax": False,
        "crosshair_stdlib_tests_dropped": 0,
        "duplicate_test_names_renamed": 0,
        "tests_before_pruning": None,
        "tests_after_pruning": None,
        "removed_tests": [],
        "error_message": None,
    }
    output_path = model_dir / OUTPUT_FILENAME
    combined_path = model_dir / COMBINED_FILENAME
    if not combined_path.is_file():
        result["error_message"] = f"{COMBINED_FILENAME} not found"
        output_path.unlink(missing_ok=True)
        return result

    try:
        parts = [combined_path.read_text(encoding="utf-8")]

        behavioral_path = model_dir / BEHAVIORAL_FILENAME
        if behavioral_path.is_file():
            behavioral_text = behavioral_path.read_text(encoding="utf-8")
            parts.append(behavioral_text)
            result["behavioral_tests_added"] = _count_tests(behavioral_text)

        crosshair_path = model_dir / CROSSHAIR_FILENAME
        if crosshair_path.is_file():
            crosshair_text, dropped = sanitize_crosshair_tests(crosshair_path.read_text(encoding="utf-8"))
            if crosshair_text is None:
                result["crosshair_skipped_invalid_syntax"] = True
            else:
                result["crosshair_stdlib_tests_dropped"] = len(dropped)
                parts.append(crosshair_text)
                result["crosshair_tests_added"] = _count_tests(crosshair_text)

        merged, result["duplicate_test_names_renamed"] = make_test_names_unique("\n\n".join(parts) + "\n")
        green = make_green(merged, model_dir, OUTPUT_FILENAME, hypothesis_seed, timeout)
        result["tests_before_pruning"] = green["tests_before"]
        result["tests_after_pruning"] = green["tests_after"]
        result["removed_tests"] = green["removed"]
        result["error_message"] = green["error_message"]
        result["status"] = green["status"]
        if green["status"] == "green":
            output_path.write_text(green["source"], encoding="utf-8")
        else:
            output_path.unlink(missing_ok=True)
    except Exception as exc:
        result["status"] = "error"
        result["error_message"] = str(exc)
    return result


def build_report(results: list[dict]) -> dict:
    by_status: dict[str, int] = {}
    for r in results:
        by_status[r["status"]] = by_status.get(r["status"], 0) + 1
    green = [r for r in results if r["status"] == "green"]
    skipped_crosshair = [r for r in results if r.get("crosshair_skipped_invalid_syntax")]
    return {
        "generated_at": datetime.datetime.now(datetime.timezone.utc).isoformat(),
        "total_models": len(results),
        "by_status": by_status,
        "green_count": len(green),
        "total_tests_after_pruning": sum(r["tests_after_pruning"] or 0 for r in green),
        "models_with_removed_tests": sum(1 for r in green if r.get("removed_tests")),
        "total_tests_removed": sum(len(r.get("removed_tests") or []) for r in results),
        "total_crosshair_stdlib_tests_dropped": sum(r.get("crosshair_stdlib_tests_dropped") or 0 for r in results),
        "total_duplicate_test_names_renamed": sum(r.get("duplicate_test_names_renamed") or 0 for r in results),
        "crosshair_skipped_invalid_syntax_models": [r["model"] for r in skipped_crosshair],
        "results": results,
    }


def render_markdown_report(report: dict) -> str:
    lines = [
        "# Super Suite Report (merged + pruned to green)",
        "",
        f"Generated: {report['generated_at']}",
        "",
        f"- **Total models:** {report['total_models']}",
        f"- **Green suites written:** {report['green_count']} "
        f"({report['total_tests_after_pruning']} tests total)",
        f"- **Tests removed for failing on unmutated code:** {report['total_tests_removed']} "
        f"(in {report['models_with_removed_tests']} green models)",
        f"- **CrossHair tests of stdlib internals dropped:** {report['total_crosshair_stdlib_tests_dropped']}",
        f"- **Duplicate test names renamed (would otherwise never run):** "
        f"{report['total_duplicate_test_names_renamed']}",
        f"- **Models with CrossHair skipped for invalid syntax:** "
        f"{', '.join(report['crosshair_skipped_invalid_syntax_models']) or 'none'}",
        "",
    ]
    lines += render_status_table(report["by_status"])
    lines += ["", f"Output file per model: `{OUTPUT_FILENAME}`. Removed tests and reasons per model: "
                  "see the accompanying `.json` report."]
    return "\n".join(lines) + "\n"


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    add_common_io_args(parser, __file__)
    parser.add_argument("--models-file", type=Path, default=None)
    parser.add_argument("--report-name", type=str, default="super_suite_report")
    parser.add_argument("--workers", type=int, default=8)
    parser.add_argument("--limit", type=int, default=None)
    parser.add_argument("--fresh", action="store_true", help="Ignore any existing cache and recompute every model")
    parser.add_argument("--hypothesis-seed", type=int, default=0,
                         help="Seed for the unmutated pruning run -- use the same seed as the mutation run")
    parser.add_argument("--timeout", type=float, default=DEFAULT_TIMEOUT,
                         help="Wall-clock cap for one unmutated run of a model's merged suite, seconds")
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

    print(f"Building green super suites for {total} models with {args.workers} workers "
          f"(hypothesis seed={args.hypothesis_seed}, timeout={args.timeout}s)...")
    if skipped:
        print(f"Resuming from cache: {skipped}/{total} already done, {len(model_dirs)} remaining "
              f"(pass --fresh to ignore the cache and recompute everything)")
    if retriable:
        print(f"Auto-retrying {len(retriable)} previously-failed models from the cache -- "
              f"same report, no separate retry run needed")

    results = run_models(
        merge_model, model_dirs, worker_args=(args.hypothesis_seed, args.timeout),
        workers=args.workers, cache_path=cache_path, results=list(cached_results.values()),
        already_done=skipped, total=total, describe=describe_green_result,
    )

    report = build_report(results)
    json_path, md_path = write_reports(args.reports_dir, args.report_name, report, render_markdown_report(report))

    print()
    print(f"Green: {report['green_count']}/{report['total_models']}  |  "
          f"tests removed: {report['total_tests_removed']}")
    print(f"Report written to {json_path} and {md_path}")


if __name__ == "__main__":
    main()
