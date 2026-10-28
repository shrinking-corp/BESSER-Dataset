#!/usr/bin/env python3
"""Recount the method-logic and stub-operation figures on a model list,
from what `classify_method_logic.py` (`method_logic_classification`) and
`validate_logic.py` (`logic_validation`) already wrote into each model's
`code_metadata.json`. Read-only: nothing is reclassified, only summed.

Written to restate figures first counted with copies (on the 8,336 usable
or all 9,082 models) on the 5,264 unique ones: models without a
logic-bearing method, methods per category, stub operations.

Usage:
    python scripts/summarize_method_logic.py
        [--models-file reports/unique_models.txt]
        [--dataset-dir PATH] [--reports-dir PATH] [--output-name method_logic_summary]
"""
from __future__ import annotations

import argparse
import datetime
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from _common.io import add_common_io_args, read_model_names  # noqa: E402
from _common.report import write_reports  # noqa: E402

CATEGORIES = ("no_logic", "trivial", "has_logic")
HAS_LOGIC_BUCKETS = [(0, 0, "0"), (1, 5, "1-5"), (6, 10, "6-10"), (11, 20, "11-20"), (21, 50, "21-50"),
                     (51, 100, "51-100"), (101, 200, "101-200"), (201, None, "200+")]


def has_logic_bucket(n: int) -> str:
    return next(label for lo, hi, label in HAS_LOGIC_BUCKETS if n >= lo and (hi is None or n <= hi))


def render_markdown_report(report: dict) -> str:
    n = report["models"]
    m = report["methods"]
    ops = report["operations"]
    lines = [
        "# Method logic and stub operations",
        "",
        f"Generated: {report['generated_at']}",
        "",
        f"- **Models file:** `{report['models_file']}` · **models:** {n:,} · "
        f"**without metadata:** {len(report['models_without_metadata'])}",
        f"- **Models with no logic-bearing method:** {report['zero_has_logic_models']:,} "
        f"({report['zero_has_logic_models'] / n:.2%})",
        f"- **Models declaring operations:** {ops['models']:,}, with {ops['total']:,} operations, "
        f"{ops['stubs']:,} of them stubs; {ops['models_all_stubbed']:,} models have only stubs",
        "",
        "## Methods by category",
        "",
        "| Category | Methods | Share of methods | Models with at least one |",
        "|---|---:|---:|---:|",
    ]
    for c in CATEGORIES:
        lines.append(f"| {c} | {m[c]:,} | {m[c] / m['total']:.2%} | {report['models_with'][c]:,} |")
    lines.append(f"| **total** | **{m['total']:,}** | | |")
    lines += ["", "## Logic-bearing methods per model", "", "| has_logic methods | Models | Share |", "|---|---:|---:|"]
    for label, count in report["has_logic_distribution"].items():
        lines.append(f"| {label} | {count:,} | {count / n:.2%} |")
    return "\n".join(lines) + "\n"


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    add_common_io_args(parser, __file__)
    parser.add_argument("--models-file", type=Path, default=None,
                         help="Default: reports/unique_models.txt")
    parser.add_argument("--output-name", default="method_logic_summary")
    args = parser.parse_args()

    models_file = args.models_file or args.reports_dir / "unique_models.txt"
    names = read_model_names(models_file)
    methods = {c: 0 for c in CATEGORIES} | {"total": 0}
    models_with = {c: 0 for c in CATEGORIES}
    distribution = {label: 0 for _lo, _hi, label in HAS_LOGIC_BUCKETS}
    operations = {"models": 0, "total": 0, "stubs": 0, "models_all_stubbed": 0}
    zero_has_logic, without_metadata = 0, []

    for name in names:
        path = args.dataset_dir / name / "code_metadata.json"
        try:
            meta = json.loads(path.read_text(encoding="utf-8"))
        except (OSError, json.JSONDecodeError, UnicodeDecodeError):
            without_metadata.append(name)
            continue
        totals = (meta.get("method_logic_classification") or {}).get("totals")
        if totals is None:
            without_metadata.append(name)
            continue
        for c in CATEGORIES:
            methods[c] += totals.get(c, 0)
            models_with[c] += totals.get(c, 0) > 0
        methods["total"] += totals.get("total_methods", 0)
        zero_has_logic += totals.get("has_logic", 0) == 0
        distribution[has_logic_bucket(totals.get("has_logic", 0))] += 1
        logic = meta.get("logic_validation") or {}
        metrics = logic.get("metrics") or {}
        if metrics.get("operations", 0) > 0:
            operations["models"] += 1
            operations["total"] += metrics["operations"]
            operations["stubs"] += metrics.get("empty_operations", 0)
            operations["models_all_stubbed"] += bool(logic.get("all_operations_stubbed"))

    report = {
        "generated_at": datetime.datetime.now(datetime.timezone.utc).isoformat(),
        "models_file": str(models_file),
        "models": len(names) - len(without_metadata),
        "models_without_metadata": without_metadata,
        "zero_has_logic_models": zero_has_logic,
        "methods": methods,
        "models_with": models_with,
        "has_logic_distribution": distribution,
        "operations": operations,
    }
    markdown = render_markdown_report(report)
    json_path, md_path = write_reports(args.reports_dir, args.output_name, report, markdown)
    print(markdown)
    print(f"Report written to {json_path} and {md_path}")


if __name__ == "__main__":
    main()
