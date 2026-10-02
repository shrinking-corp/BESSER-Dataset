#!/usr/bin/env python3
"""Write `test_combined_plus_behavioral.py` per model: a literal
concatenation of `test_combined.py` + `test_behavioral.py`, for measuring
the behavioral generator's real effect on mutation score (Phase 4 Stage 1).

Why a plain concatenation is safe here, unlike `generate_combined_tests.py`'s
old+new merge: `test_behavioral.py` is a wholly new category of test
(`test_{assoc}_reverse_link_reassign_clear`) that `generate_structural_tests.py`
never produces, so there is no name collision or semantic-duplication risk
to dedupe against -- every test `generate_behavioral_tests.py` writes is one
`test_combined.py` could not possibly already contain. This is deliberately
a small, interim tool for Stage 1 measurement, not the final "super suite"
merger (Step 3) -- that one needs real AST-based dedup once more than one
approach's results are in and some may overlap.

A model with no `test_behavioral.py` (nothing generated -- e.g. no
association has both ends independently real) is copied through unchanged,
not treated as an error.

Usage:
    python scripts/merge_combined_and_behavioral.py --models-file PATH
        [--workers N] [--dataset-dir PATH] [--reports-dir PATH]
        [--report-name NAME] [--limit N] [--fresh]
"""
from __future__ import annotations

import argparse
import concurrent.futures
import datetime
import json
import platform
from pathlib import Path

COMBINED_FILENAME = "test_combined.py"
BEHAVIORAL_FILENAME = "test_behavioral.py"
OUTPUT_FILENAME = "test_combined_plus_behavioral.py"
# Cached results with one of these statuses are automatically re-attempted
# on the next run under the SAME --report-name -- same fix as
# validate_mutation.py/validate_mutation_properties.py (2026-10-01).
# "missing_combined"/"no_behavioral_tests" are excluded: permanent facts
# (no test_combined.py to merge; or none generated for that model), not
# transient failures a re-run would fix.
RETRIABLE_STATUSES = {"error"}


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


def merge_model(model_dir: Path) -> dict:
    checked_at = datetime.datetime.now(datetime.timezone.utc).isoformat()
    result = {
        "model": model_dir.name,
        "checked_at": checked_at,
        "python_version": platform.python_version(),
        "status": "missing_combined",
        "behavioral_tests_added": 0,
        "error_message": None,
    }
    combined_path = model_dir / COMBINED_FILENAME
    if not combined_path.is_file():
        result["error_message"] = f"{COMBINED_FILENAME} not found"
        return result

    try:
        combined_text = combined_path.read_text(encoding="utf-8")
        behavioral_path = model_dir / BEHAVIORAL_FILENAME
        if behavioral_path.is_file():
            behavioral_text = behavioral_path.read_text(encoding="utf-8")
            merged = combined_text + "\n\n" + behavioral_text
            result["behavioral_tests_added"] = behavioral_text.count("\ndef test_")
            result["status"] = "merged"
        else:
            merged = combined_text
            result["status"] = "no_behavioral_tests"
        (model_dir / OUTPUT_FILENAME).write_text(merged, encoding="utf-8")
    except Exception as exc:
        result["status"] = "error"
        result["error_message"] = str(exc)
    return result


def build_report(results: list[dict]) -> dict:
    total = len(results)
    by_status: dict[str, int] = {}
    for r in results:
        by_status[r["status"]] = by_status.get(r["status"], 0) + 1
    merged = [r for r in results if r["status"] == "merged"]
    return {
        "generated_at": datetime.datetime.now(datetime.timezone.utc).isoformat(),
        "total_models": total,
        "by_status": by_status,
        "models_with_behavioral_tests": len(merged),
        "total_behavioral_tests_added": sum(r["behavioral_tests_added"] for r in merged),
        "results": results,
    }


def render_markdown_report(report: dict) -> str:
    lines = [
        "# Combined + Behavioral Merge Report",
        "",
        f"Generated: {report['generated_at']}",
        "",
        f"- **Total models:** {report['total_models']}",
        f"- **Models with >=1 behavioral test added:** {report['models_with_behavioral_tests']}",
        f"- **Total behavioral tests added across sample:** {report['total_behavioral_tests_added']}",
        "",
        "## Breakdown by status",
        "",
        "| Status | Count |",
        "|---|---|",
    ]
    for status, count in sorted(report["by_status"].items(), key=lambda kv: -kv[1]):
        lines.append(f"| {status} | {count} |")
    lines += ["", f"Output file per model: `{OUTPUT_FILENAME}`. Full per-model detail: see the accompanying `.json` report."]
    return "\n".join(lines) + "\n"


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--dataset-dir", type=Path, default=Path(__file__).resolve().parent.parent / "Dataset")
    parser.add_argument("--reports-dir", type=Path, default=Path(__file__).resolve().parent.parent / "reports")
    parser.add_argument("--models-file", type=Path, default=None)
    parser.add_argument("--report-name", type=str, default="combined_plus_behavioral_report")
    parser.add_argument("--workers", type=int, default=8)
    parser.add_argument("--limit", type=int, default=None)
    parser.add_argument("--fresh", action="store_true", help="Ignore any existing cache and recompute every model")
    args = parser.parse_args()

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

    print(f"Merging combined+behavioral for {total} models with {args.workers} workers...")
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
            futures = {executor.submit(merge_model, model_dir): model_dir for model_dir in model_dirs}
            for future in concurrent.futures.as_completed(futures):
                model_dir = futures[future]
                try:
                    result = future.result()
                except Exception as exc:
                    result = {"model": model_dir.name, "status": "error", "error_message": str(exc), "behavioral_tests_added": 0}
                results.append(result)
                cache_file.write(json.dumps(result) + "\n")
                cache_file.flush()
                done += 1
                if done % 500 == 0 or done == total:
                    print(f"  {done}/{total} processed", flush=True)
    finally:
        cache_file.close()

    report = build_report(results)
    json_path = args.reports_dir / f"{args.report_name}.json"
    json_path.write_text(json.dumps(report, indent=2) + "\n")
    md_path = args.reports_dir / f"{args.report_name}.md"
    md_path.write_text(render_markdown_report(report))

    print()
    print(f"Models with behavioral tests merged in: {report['models_with_behavioral_tests']}/{total}")
    print(f"Report written to {json_path} and {md_path}")


if __name__ == "__main__":
    main()
