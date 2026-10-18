#!/usr/bin/env python3
"""Extract class-diagram structure (classes, methods, attributes,
inheritance, decorators) from each model's `python_code.py` via
tree-sitter, and write it to a new `code_structure.json` file per model.

Requires `tree-sitter` and `tree-sitter-python` -- these are a separate,
lightweight dependency from `besser` (used by generate_model_metadata.py)
and the pytest/hypothesis/mutation stack (used by the validate_*.py
scripts), so install them into their own venv:

    python3 -m venv .venv-treesitter
    .venv-treesitter/bin/pip install tree-sitter tree-sitter-python
    .venv-treesitter/bin/python scripts/generate_code_structure.py ...

This is deliberately a NEW, self-contained per-model file, not another key
merged into code_metadata.json or model_metadata.json:
- model_metadata.json holds structural counts read off the BUML *model*
  (the diagram) via the besser library -- independent of the generated code.
- code_metadata.json holds *validation* results about python_code.py
  (compiles, passes tests, coverage, mutation score, logic_validation's
  aggregate counts).
- code_structure.json (this script) holds the actual per-class/method/
  attribute *structure* read directly off python_code.py's syntax tree --
  the class-diagram-shaped detail that logic_validation's counts summarize
  but don't preserve (e.g. it has no per-attribute type/visibility, no
  parameter lists, no base-class names).

Relationships between classes (associations/aggregation/composition) are
deliberately out of scope for now -- see extract_structure.py's docstring.

Because tree-sitter is error-tolerant (unlike `ast.parse`, it never raises on
malformed input -- it recovers around the broken part and parses the rest),
this can produce a structure for files that validate_logic.py's AST-based
pass marks as `syntax_error`; check each result's `has_error` flag before
trusting it fully.

Usage:
    python scripts/generate_code_structure.py [--workers N]
        [--dataset-dir PATH] [--reports-dir PATH] [--report-name NAME]
        [--limit N] [--models-file PATH] [--fresh]
"""
from __future__ import annotations

import argparse
import datetime
import json
import platform
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from _common.cache import load_cache, partition_cache  # noqa: E402
from _common.io import add_common_io_args, find_model_dirs  # noqa: E402
from _common.pool import run_models  # noqa: E402
from _common.report import render_status_table, write_reports  # noqa: E402
from extract_structure import extract_module_structure  # noqa: E402

CODE_FILENAME = "python_code.py"
STRUCTURE_FILENAME = "code_structure.json"
RETRIABLE_STATUSES = frozenset({"error"})


def process_model(model_dir: Path) -> dict:
    checked_at = datetime.datetime.now(datetime.timezone.utc).isoformat()
    result = {
        "model": model_dir.name,
        "checked_at": checked_at,
        "python_version": platform.python_version(),
        "status": "missing_file",
        "has_error": None,
        "counts": None,
        "error_message": None,
    }

    code_path = model_dir / CODE_FILENAME
    if not code_path.is_file():
        result["error_message"] = f"{CODE_FILENAME} not found in {model_dir.name}"
        return result

    try:
        source = code_path.read_text(encoding="utf-8", errors="replace")
        structure = extract_module_structure(source)
    except Exception as exc:
        result["status"] = "error"
        result["error_message"] = str(exc)
        return result

    result["status"] = "extracted"
    result["has_error"] = structure["has_error"]
    result["counts"] = {
        "classes": len(structure["classes"]),
        "module_functions": len(structure["functions"]),
        "attributes": sum(len(c["attributes"]) for c in structure["classes"]),
        "methods": sum(len(c["methods"]) for c in structure["classes"]),
        "abstract_classes": sum(1 for c in structure["classes"] if c["is_abstract"]),
        "enum_classes": sum(1 for c in structure["classes"] if c["is_enum"]),
        "dataclasses": sum(1 for c in structure["classes"] if c["is_dataclass"]),
    }

    payload = {
        "generated_at": checked_at,
        "python_version": result["python_version"],
        "source_file": CODE_FILENAME,
        "has_error": structure["has_error"],
        "functions": structure["functions"],
        "classes": structure["classes"],
    }
    (model_dir / STRUCTURE_FILENAME).write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
    return result


def build_report(results: list[dict]) -> dict:
    total = len(results)
    by_status: dict[str, int] = {}
    for r in results:
        by_status[r["status"]] = by_status.get(r["status"], 0) + 1

    measured = [r["counts"] for r in results if r.get("counts") is not None]
    parse_errors = sum(1 for r in results if r.get("has_error"))

    def total_of(field):
        return sum(c[field] for c in measured)

    fields = ["classes", "module_functions", "attributes", "methods",
              "abstract_classes", "enum_classes", "dataclasses"]

    return {
        "generated_at": datetime.datetime.now(datetime.timezone.utc).isoformat(),
        "total_models": total,
        "by_status": by_status,
        "extracted_count": len(measured),
        "models_with_parse_errors": parse_errors,
        "sums": {field: total_of(field) for field in fields} if measured else {},
        "results": results,
    }


def render_markdown_report(report: dict) -> str:
    lines = [
        "# Code Structure Extraction Report",
        "",
        f"Generated: {report['generated_at']}",
        "",
        f"- **Total models:** {report['total_models']}",
        f"- **Extracted:** {report['extracted_count']}",
        f"- **Models with tree-sitter parse errors (partial extraction):** {report['models_with_parse_errors']}",
        "",
        "## Totals over extracted models",
        "",
        "| Field | Total |",
        "|---|---|",
    ]
    for field, value in report["sums"].items():
        lines.append(f"| {field} | {value} |")
    lines.append("")
    lines += render_status_table(report["by_status"])
    lines += ["", "Full per-model detail: see the accompanying `.json` report and each model's `code_structure.json`."]
    return "\n".join(lines) + "\n"


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    add_common_io_args(parser, __file__)
    parser.add_argument("--models-file", type=Path, default=None)
    parser.add_argument("--report-name", type=str, default="code_structure_report")
    parser.add_argument("--workers", type=int, default=8)
    parser.add_argument("--limit", type=int, default=None)
    parser.add_argument("--fresh", action="store_true",
                         help="Ignore any existing cache and recompute every model")
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

    print(f"Extracting code structure for {total} models with {args.workers} workers...")
    if skipped:
        print(f"Resuming from cache: {skipped}/{total} already done, {len(model_dirs)} remaining "
              f"(pass --fresh to ignore the cache and recompute everything)")
    if retriable:
        print(f"Auto-retrying {len(retriable)} previously-failed models from the cache")

    results = run_models(process_model, model_dirs, workers=args.workers, cache_path=cache_path,
                         results=list(cached_results.values()), already_done=skipped, total=total,
                         error_fields={"has_error": None, "counts": None})

    report = build_report(results)
    json_path, md_path = write_reports(args.reports_dir, args.report_name, report, render_markdown_report(report))

    print()
    print(f"Extracted: {report['extracted_count']}/{report['total_models']}")
    print(f"Report written to {json_path} and {md_path}")


if __name__ == "__main__":
    main()
