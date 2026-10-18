#!/usr/bin/env python3
"""Bucket every measured model's official `difficulty_score` (already
computed by `compute_difficulty_score.py`, read here, not recomputed) into
1-point-wide buckets across the full 0-100 range, for a distribution
overview/graph.

Read-only -- does not touch `model_metadata.json`. Excludes models with
only `no_logic` methods (per `logic_validation_report.json`'s
`status == "no_logic"`), same exclusion as `experiment_difficulty_score_pca.py`
and for the same reason: a model with no real structure has nothing
meaningful to rank by difficulty score, and including it would pad the
lowest buckets with scores that don't reflect "this is an easy model" so
much as "this model barely exists."

Usage:
    python scripts/difficulty_score_distribution.py [--models-file PATH]
        [--dataset-dir PATH] [--reports-dir PATH]
"""
from __future__ import annotations

import argparse
import datetime
import json
import math
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from _common.io import add_common_io_args, iter_measured_models, read_model_names  # noqa: E402
from _common.report import write_reports  # noqa: E402

LOGIC_VALIDATION_REPORT = "logic_validation_report.json"


def load_no_logic_only_models(reports_dir: Path) -> set[str]:
    path = reports_dir / LOGIC_VALIDATION_REPORT
    data = json.loads(path.read_text(encoding="utf-8"))
    return {r["model"] for r in data["results"] if r.get("status") == "no_logic"}


def load_scores(dataset_dir: Path, only: set[str] | None, excluded: set[str]) -> list[tuple[str, float]]:
    return [
        (name, float(data["difficulty_score"]))
        for name, _path, data in iter_measured_models(dataset_dir, only)
        if name not in excluded and "difficulty_score" in data
    ]


def bucket_scores(scores: list[tuple[str, float]], scale_max: int = 100) -> list[dict]:
    """1-point-wide buckets [0,1), [1,2), ..., [scale_max-1, scale_max],
    the last bucket closed on both ends so a score exactly at scale_max
    (possible by construction, see compute_difficulty_score.py) isn't
    dropped."""
    counts = [0] * scale_max
    for _, score in scores:
        idx = min(int(math.floor(score)), scale_max - 1)
        idx = max(idx, 0)
        counts[idx] += 1
    total = len(scores)
    buckets = []
    for i, count in enumerate(counts):
        lo, hi = i, i + 1
        buckets.append({
            "range_low": lo,
            "range_high": hi,
            "label": f"{lo}-{hi}",
            "count": count,
            "pct": round(count / total * 100, 4) if total else 0.0,
        })
    return buckets


def render_markdown_report(report: dict) -> str:
    lines = [
        "# Difficulty Score Distribution",
        "",
        f"Generated: {report['generated_at']}",
        "",
        f"- **Models included:** {report['models_included']}",
        f"- **Models excluded (no_logic-only):** {report['models_excluded_no_logic_only']}",
        f"- **Mean:** {report['mean']:.2f}  |  **Median:** {report['median']:.2f}  |  "
        f"**Min:** {report['min']:.2f}  |  **Max:** {report['max']:.2f}",
        "",
        "## Buckets (1-point width, 0-100)",
        "",
        "| Range | Count | % | Bar |",
        "|---|---:|---:|---|",
    ]
    max_count = max((b["count"] for b in report["buckets"]), default=0)
    for b in report["buckets"]:
        bar_len = round(b["count"] / max_count * 40) if max_count else 0
        lines.append(f"| {b['label']} | {b['count']} | {b['pct']:.2f}% | {'#' * bar_len} |")
    return "\n".join(lines) + "\n"


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    add_common_io_args(parser, __file__)
    parser.add_argument("--models-file", type=Path, help="Only these models (e.g. reports/usable_models.txt)")
    args = parser.parse_args()

    excluded = load_no_logic_only_models(args.reports_dir)
    print(f"Excluding {len(excluded)} no_logic-only models (per {LOGIC_VALIDATION_REPORT})")

    only = set(read_model_names(args.models_file)) if args.models_file else None
    scored = load_scores(args.dataset_dir, only, excluded)
    print(f"Loaded {len(scored)} measured, non-excluded models with a difficulty_score")

    values = sorted(s for _, s in scored)
    n = len(values)
    mean = sum(values) / n if n else 0.0
    median = values[n // 2] if n % 2 else (values[n // 2 - 1] + values[n // 2]) / 2 if n else 0.0

    buckets = bucket_scores(scored)

    report = {
        "generated_at": datetime.datetime.now(datetime.timezone.utc).isoformat(),
        "models_included": n,
        "models_excluded_no_logic_only": len(excluded),
        "mean": mean,
        "median": median,
        "min": values[0] if values else None,
        "max": values[-1] if values else None,
        "buckets": buckets,
    }
    json_path, md_path = write_reports(args.reports_dir, "difficulty_score_distribution_report",
                                       report, render_markdown_report(report))

    print(f"Mean: {mean:.2f}  Median: {median:.2f}  Min: {report['min']:.2f}  Max: {report['max']:.2f}")
    print(f"Reports written to {json_path} and {md_path}")


if __name__ == "__main__":
    main()
