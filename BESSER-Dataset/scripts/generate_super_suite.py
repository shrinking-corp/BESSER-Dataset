#!/usr/bin/env python3
"""Write `test_super_suite.py` per model: `test_combined.py` (old+new,
already deduped) + `test_behavioral.py` + `test_crosshair.py`, merged into
one real file -- the actual "does combining everything beat each individual
approach" artifact, not just an average of separate scores.

Why plain concatenation is safe for behavioral (same reasoning as
`merge_combined_and_behavioral.py`): `test_behavioral.py` is a wholly new
test category (`test_{assoc}_reverse_link_reassign_clear`) with no
counterpart in `test_combined.py`, so there's no name collision or semantic-
duplication risk to dedupe against.

Why plain concatenation is also safe for CrossHair, checked explicitly
before writing this (not assumed): CrossHair's own naming convention is
`test_{ClassName}___init__` (triple underscore -- `test_` + name +
`___init__`), confirmed via an AST scan across all 177 models that actually
have `test_crosshair.py` -- zero top-level function-name collisions against
that same model's `test_combined.py` or `test_behavioral.py`. No generator
in this project's pipeline happens to produce that exact shape.

**Real bug found during that same scan, handled here**: 4/177 models'
`test_crosshair.py` contain a syntax error -- CrossHair's pytest-output
generator can dump a bare object repr (e.g.
`{<python_code.UML2WithID_Interface object at 0x...>}`) into a set literal
when it can't find a better example value, which isn't valid Python. A
syntactically broken test file fails to even collect under pytest
regardless of which mutation is applied to the source, so cosmic-ray reads
every single mutant as "killed" -- these 4 models' *standalone* CrossHair
mutation score was a fake 1.0, not a real result (confirmed: excluding them
drops the published CrossHair average from 65.05% to 64.24%). Naively
concatenating a broken `test_crosshair.py` into the super suite would make
the WHOLE merged file uncollectable for that model, silently producing
another fake-perfect score -- worse than the standalone case, since it would
also hide whatever `test_combined.py`/`test_behavioral.py` were
contributing. Fixed here by `ast.parse`-validating `test_crosshair.py`
before including it; an invalid file is skipped (not included, not an
error for the whole model) and flagged in the report so it's visible, not
silently inflating anything.

Usage:
    python scripts/generate_super_suite.py --models-file PATH
        [--workers N] [--dataset-dir PATH] [--reports-dir PATH]
        [--report-name NAME] [--limit N] [--fresh]
"""
from __future__ import annotations

import argparse
import ast
import concurrent.futures
import datetime
import json
import platform
from pathlib import Path

COMBINED_FILENAME = "test_combined.py"
BEHAVIORAL_FILENAME = "test_behavioral.py"
CROSSHAIR_FILENAME = "test_crosshair.py"
OUTPUT_FILENAME = "test_super_suite.py"
# Same auto-retry pattern as every other test-generation/merge script in
# this project (2026-10-01 fix) -- a plain re-run under the same
# --report-name picks up just the failed models, no separate retry report.
# "missing_combined" is excluded: a permanent fact (no test_combined.py to
# start from), not a transient failure a re-run would fix.
RETRIABLE_STATUSES = {"error"}


def _read_text_robust(path: Path) -> str:
    """Reads a text file regardless of which BOM (if any) Windows wrote --
    confirmed real (2026-10-12): PowerShell's `echo >` defaults to UTF-16LE
    with BOM, `Out-File -Encoding utf8` defaults to UTF-8 WITH BOM (neither
    matches plain `.read_text()`'s assumption) -- `encoding="utf-8-sig"`
    alone only covers the UTF-8 case, not UTF-16, so a `--models-file`
    created with plain `echo` silently corrupts the first model name AND
    throws off line-splitting entirely (one line becomes several, since
    UTF-16 is 2 bytes/char). Sniffs the actual BOM bytes rather than
    guessing from one case."""
    raw = path.read_bytes()
    if raw.startswith(b"\xff\xfe") or raw.startswith(b"\xfe\xff"):
        return raw.decode("utf-16")
    if raw.startswith(b"\xef\xbb\xbf"):
        return raw.decode("utf-8-sig")
    return raw.decode("utf-8")


def find_model_dirs(dataset_dir: Path, models_file: Path | None, limit: int | None) -> list[Path]:
    if models_file:
        names = [l.strip() for l in _read_text_robust(models_file).splitlines() if l.strip()]
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


def _is_valid_python(source: str) -> bool:
    try:
        ast.parse(source)
        return True
    except SyntaxError:
        return False


def _count_tests(source: str) -> int:
    return source.count("\ndef test_") + (1 if source.startswith("def test_") else 0)


def merge_model(model_dir: Path) -> dict:
    checked_at = datetime.datetime.now(datetime.timezone.utc).isoformat()
    result = {
        "model": model_dir.name,
        "checked_at": checked_at,
        "python_version": platform.python_version(),
        "status": "missing_combined",
        "behavioral_tests_added": 0,
        "crosshair_tests_added": 0,
        "crosshair_skipped_invalid_syntax": False,
        "error_message": None,
    }
    combined_path = model_dir / COMBINED_FILENAME
    if not combined_path.is_file():
        result["error_message"] = f"{COMBINED_FILENAME} not found"
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
            crosshair_text = crosshair_path.read_text(encoding="utf-8")
            if _is_valid_python(crosshair_text):
                parts.append(crosshair_text)
                result["crosshair_tests_added"] = _count_tests(crosshair_text)
            else:
                result["crosshair_skipped_invalid_syntax"] = True

        merged = "\n\n".join(parts) + "\n"
        (model_dir / OUTPUT_FILENAME).write_text(merged, encoding="utf-8")
        result["status"] = "merged"
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
    skipped_crosshair = [r for r in merged if r["crosshair_skipped_invalid_syntax"]]
    return {
        "generated_at": datetime.datetime.now(datetime.timezone.utc).isoformat(),
        "total_models": total,
        "by_status": by_status,
        "merged_count": len(merged),
        "models_with_behavioral_tests": sum(1 for r in merged if r["behavioral_tests_added"] > 0),
        "models_with_crosshair_tests": sum(1 for r in merged if r["crosshair_tests_added"] > 0),
        "total_behavioral_tests_added": sum(r["behavioral_tests_added"] for r in merged),
        "total_crosshair_tests_added": sum(r["crosshair_tests_added"] for r in merged),
        "models_with_crosshair_skipped_invalid_syntax": len(skipped_crosshair),
        "crosshair_skipped_invalid_syntax_models": [r["model"] for r in skipped_crosshair],
        "results": results,
    }


def render_markdown_report(report: dict) -> str:
    lines = [
        "# Super Suite Merge Report",
        "",
        f"Generated: {report['generated_at']}",
        "",
        f"- **Total models:** {report['total_models']}",
        f"- **Merged:** {report['merged_count']}",
        f"- **Models with >=1 behavioral test added:** {report['models_with_behavioral_tests']} "
        f"({report['total_behavioral_tests_added']} tests total)",
        f"- **Models with >=1 CrossHair test added:** {report['models_with_crosshair_tests']} "
        f"({report['total_crosshair_tests_added']} tests total)",
        f"- **Models with CrossHair tests skipped for invalid syntax:** "
        f"{report['models_with_crosshair_skipped_invalid_syntax']} "
        f"({', '.join(report['crosshair_skipped_invalid_syntax_models']) or 'none'})",
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
    parser.add_argument("--report-name", type=str, default="super_suite_report")
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

    print(f"Building super suite for {total} models with {args.workers} workers...")
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
                    result = {
                        "model": model_dir.name, "status": "error", "error_message": str(exc),
                        "behavioral_tests_added": 0, "crosshair_tests_added": 0,
                        "crosshair_skipped_invalid_syntax": False,
                    }
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
    print(f"Merged: {report['merged_count']}/{report['total_models']}")
    print(f"Report written to {json_path} and {md_path}")


if __name__ == "__main__":
    main()
