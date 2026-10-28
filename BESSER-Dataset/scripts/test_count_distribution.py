#!/usr/bin/env python3
"""Distribution of tests per model for one or more green suites, read from
the reports `generate_super_suite.py` / `make_green_suite.py` wrote
(`tests_after_pruning`). Read-only: writes only reports.

Three tables: summary statistics, a histogram with bins that roughly double
(suite sizes are very skewed), and median / P90 per difficulty bucket (the
buckets of `make_benchmark_split.py`, from each model's `model_metadata.json`).

Usage:
    python scripts/test_count_distribution.py
        [--suite "Super suite=reports/full_super_suite.json"] [--suite ...]
        [--dataset-dir PATH] [--reports-dir PATH] [--output-name test_count_distribution]
"""
from __future__ import annotations

import argparse
import datetime
import json
import statistics
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from _common.io import add_common_io_args, iter_measured_models  # noqa: E402
from _common.report import write_reports  # noqa: E402
from make_benchmark_split import BUCKET_LABELS, bucket_index  # noqa: E402

BINS = [(1, 10), (11, 25), (26, 50), (51, 100), (101, 250), (251, 500),
        (501, 1000), (1001, 2000), (2001, 5000), (5001, None)]
DEFAULT_SUITES = ["Super suite=full_super_suite.json", "Baseline=full_green_test_combined.json"]


def read_counts(path: Path) -> dict[str, int]:
    data = json.loads(path.read_text(encoding="utf-8"))
    return {r["model"]: r["tests_after_pruning"] for r in data["results"]
            if r.get("tests_after_pruning") is not None}


def percentile(values: list[int], p: float) -> int:
    s = sorted(values)
    return s[min(len(s) - 1, round(p / 100 * (len(s) - 1)))]


def summarize(values: list[int]) -> dict:
    return {
        "models": len(values), "total_tests": sum(values), "min": min(values),
        "p10": percentile(values, 10), "p25": percentile(values, 25), "median": statistics.median(values),
        "mean": statistics.mean(values), "p75": percentile(values, 75), "p90": percentile(values, 90),
        "p99": percentile(values, 99), "max": max(values),
    }


def histogram(values: list[int]) -> list[dict]:
    rows = []
    for lo, hi in BINS:
        n = sum(1 for v in values if v >= lo and (hi is None or v <= hi))
        rows.append({"bin": f"{lo:,}+" if hi is None else f"{lo:,}-{hi:,}", "models": n, "share": n / len(values)})
    return rows


def fmt(value: float) -> str:
    """Thousands separators; a median like 383.5 keeps its half."""
    return f"{int(value):,}" if float(value).is_integer() else f"{value:,}"


def render_markdown_report(report: dict) -> str:
    names = list(report["suites"])
    suites = report["suites"]
    lines = ["# Tests per model", "", f"Generated: {report['generated_at']}", ""]
    lines += [f"- **{n}:** `{suites[n]['report']}`" for n in names]
    lines += ["", "## Summary", "", "| | " + " | ".join(names) + " |", "|---|" + "---:|" * len(names)]
    labels = [("models", "Models"), ("total_tests", "Total tests"), ("min", "Min"), ("p10", "P10"),
              ("p25", "P25"), ("median", "Median"), ("mean", "Mean"), ("p75", "P75"), ("p90", "P90"),
              ("p99", "P99"), ("max", "Max")]
    for key, label in labels:
        cells = []
        for n in names:
            v = suites[n]["summary"][key]
            cells.append(f"{v:,.1f}" if key == "mean" else fmt(v))
        lines.append(f"| {label} | " + " | ".join(cells) + " |")
    lines += ["", "## Histogram", "", "| Tests | " + " | ".join(f"{n} models | share" for n in names) + " |",
              "|---|" + "---:|---:|" * len(names)]
    for i, (lo, hi) in enumerate(BINS):
        cells = [f"{suites[n]['histogram'][i]['models']:,} | {suites[n]['histogram'][i]['share']:.1%}" for n in names]
        lines.append(f"| {suites[names[0]]['histogram'][i]['bin']} | " + " | ".join(cells) + " |")
    lines += ["", "## By difficulty bucket", "",
              "| Bucket | Models | " + " | ".join(f"{n} median | {n} P90" for n in names) + " |",
              "|---|---:|" + "---:|---:|" * len(names)]
    for b in report["by_bucket"]:
        cells = [f"{fmt(b[n]['median'])} | {b[n]['p90']:,}" for n in names]
        lines.append(f"| {b['bucket']} | {b['models']:,} | " + " | ".join(cells) + " |")
    return "\n".join(lines) + "\n"


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    add_common_io_args(parser, __file__)
    parser.add_argument("--suite", action="append", default=None,
                         help='"Label=report.json" (repeatable; a bare file name is looked up in --reports-dir). '
                              "Default: the full super suite and the full green baseline")
    parser.add_argument("--output-name", default="test_count_distribution")
    args = parser.parse_args()

    suites = {}
    for spec in args.suite or DEFAULT_SUITES:
        label, _, path = spec.partition("=")
        if not path:
            parser.error(f"--suite {spec!r}: expected Label=path")
        path = Path(path)
        if not path.is_absolute() and not path.exists():
            path = args.reports_dir / path
        suites[label] = {"report": str(path), "counts": read_counts(path)}

    first = next(iter(suites.values()))["counts"]
    scores = {name: data["difficulty_score"] for name, _p, data in iter_measured_models(args.dataset_dir, set(first))
              if "difficulty_score" in data}
    by_bucket = []
    for i, label in enumerate(BUCKET_LABELS):
        models = [m for m in first if m in scores and bucket_index(scores[m]) == i]
        if not models:
            continue
        row = {"bucket": label, "models": len(models)}
        for name, suite in suites.items():
            values = [suite["counts"][m] for m in models if m in suite["counts"]]
            row[name] = {"median": statistics.median(values), "p90": percentile(values, 90)}
        by_bucket.append(row)

    report = {
        "generated_at": datetime.datetime.now(datetime.timezone.utc).isoformat(),
        "suites": {name: {"report": s["report"], "summary": summarize(list(s["counts"].values())),
                          "histogram": histogram(list(s["counts"].values()))} for name, s in suites.items()},
        "models_without_score": sorted(set(first) - set(scores)),
        "by_bucket": by_bucket,
    }
    markdown = render_markdown_report(report)
    json_path, md_path = write_reports(args.reports_dir, args.output_name, report, markdown)
    print(markdown)
    print(f"Report written to {json_path} and {md_path}")


if __name__ == "__main__":
    main()
