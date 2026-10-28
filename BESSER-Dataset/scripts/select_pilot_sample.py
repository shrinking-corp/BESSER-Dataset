#!/usr/bin/env python3
"""Pick the pilot sample: a small, difficulty-balanced set of models for
trying the benchmark pipeline end to end before a full run. Read-only on the
dataset: writes only reports.

1. **Per bucket.** `--per-bucket` models from each of the 10 difficulty
   buckets of `make_benchmark_split.py` (0-10 ... 90-100), 100 in total by
   default.
2. **Small buckets.** A bucket with fewer models gives all of them, and the
   shortfall is taken from the nearest bucket with models to spare (the
   harder one on a tie). With the 5,264 unique models: all 9 of 90-100,
   11 of 80-90.
3. **Avoided models.** Models in `--avoid-file` (default: the 200-model
   test-generation sample, so the pilot is new models) are taken only when a
   bucket has nothing else left. Every one taken is listed in the report.
4. **Reproducible.** Each bucket is shuffled with an RNG seeded from `--seed`
   and the bucket, as in the split.

The pilot sample is not a third split: it overlaps train and test on
purpose, and the split ignores it.

Writes `<output-name>.txt` (one model per line, usable as --models-file) and
`<output-name>.json/.md` (parameters, per-bucket counts, one row per model).

Usage:
    python scripts/select_pilot_sample.py
        [--models-file reports/unique_models.txt] [--per-bucket 10] [--seed 42]
        [--avoid-file reports/test_generation_sample.txt] [--require-file NAME ...]
        [--dataset-dir PATH] [--reports-dir PATH] [--output-name pilot_sample]
"""
from __future__ import annotations

import argparse
import datetime
import random
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from _common.io import add_common_io_args, read_model_names  # noqa: E402
from _common.report import write_reports  # noqa: E402
from make_benchmark_split import BUCKET_COUNT, BUCKET_LABELS, bucket_index, load_candidates  # noqa: E402


def bucket_quotas(available: list[int], per_bucket: int) -> list[int]:
    """`per_bucket` from each bucket; a small bucket's shortfall is taken one
    model at a time from the nearest bucket with models to spare."""
    quotas = [min(per_bucket, n) for n in available]
    for i in sorted(range(BUCKET_COUNT), reverse=True):
        for _ in range(per_bucket - quotas[i]):
            spare = [j for j in range(BUCKET_COUNT) if available[j] > quotas[j]]
            if not spare:
                return quotas
            quotas[min(spare, key=lambda j: (abs(i - j), -j))] += 1
    return quotas


def pick(rows: list[dict], quota: int, avoid: set[str], seed: int, bucket: int) -> list[dict]:
    order = sorted(rows, key=lambda r: r["model"])
    random.Random(f"{seed}:{bucket}").shuffle(order)
    order.sort(key=lambda r: r["model"] in avoid)
    return sorted(order[:quota], key=lambda r: r["model"])


def render_markdown_report(report: dict) -> str:
    p = report["parameters"]
    lines = [
        "# Pilot sample",
        "",
        f"Generated: {report['generated_at']}",
        "",
        f"- **Models file:** `{p['models_file']}` · **per bucket:** {p['per_bucket']} · **seed:** {p['seed']} · "
        f"**avoided:** `{p['avoid_file']}` · **required files:** {', '.join(p['required_files']) or 'none'}",
        f"- **Picked:** {report['picked_count']} models; {len(report['picked_from_avoid_list'])} of them from the "
        "avoided list (a bucket had nothing else left)",
        "- Overlaps the train/test split on purpose; the split ignores this sample.",
        "",
        "## Per bucket",
        "",
        "| Difficulty | Models | Picked | From the avoided list |",
        "|---|---:|---:|---:|",
    ]
    for b in report["buckets"]:
        lines.append(f"| {b['bucket']} | {b['models']} | {b['picked']} | {b['from_avoid_list']} |")
    lines += ["", "## Models", "", "| Model | Bucket | Difficulty | Avoided |", "|---|---|---:|---|"]
    for r in report["sample"]:
        lines.append(f"| {r['model']} | {r['bucket']} | {r['difficulty_score']:.2f} | {'yes' if r['avoided'] else ''} |")
    return "\n".join(lines) + "\n"


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    add_common_io_args(parser, __file__)
    parser.add_argument("--models-file", type=Path, default=None,
                         help="Models to pick from (default: reports/unique_models.txt)")
    parser.add_argument("--per-bucket", type=int, default=10)
    parser.add_argument("--seed", type=int, default=42)
    parser.add_argument("--avoid-file", type=Path, default=None,
                         help="Models to take only as a last resort (default: reports/test_generation_sample.txt)")
    parser.add_argument("--require-file", action="append", default=[],
                         help="Drop models missing this file (repeatable), e.g. test_super_suite.py")
    parser.add_argument("--output-name", default="pilot_sample")
    args = parser.parse_args()

    models_file = args.models_file or args.reports_dir / "unique_models.txt"
    avoid_file = args.avoid_file or args.reports_dir / "test_generation_sample.txt"
    avoid = set(read_model_names(avoid_file)) if avoid_file.is_file() else set()
    names = read_model_names(models_file)
    rows, dropped = load_candidates(args.dataset_dir, names, args.require_file)
    print(f"{len(rows)}/{len(names)} models eligible "
          f"({', '.join(f'{k}: {len(v)}' for k, v in dropped.items() if v) or 'none dropped'})")

    by_bucket: dict[int, list[dict]] = {i: [] for i in range(BUCKET_COUNT)}
    for r in rows:
        by_bucket[bucket_index(r["difficulty_score"])].append(r)
    quotas = bucket_quotas([len(by_bucket[i]) for i in range(BUCKET_COUNT)], args.per_bucket)

    sample, bucket_rows = [], []
    for i in range(BUCKET_COUNT):
        picked = pick(by_bucket[i], quotas[i], avoid, args.seed, i)
        sample += [{"model": r["model"], "bucket": BUCKET_LABELS[i], "difficulty_score": r["difficulty_score"],
                    "avoided": r["model"] in avoid} for r in picked]
        bucket_rows.append({"bucket": BUCKET_LABELS[i], "models": len(by_bucket[i]), "picked": len(picked),
                            "from_avoid_list": sum(r["model"] in avoid for r in picked)})
        b = bucket_rows[-1]
        print(f"  {b['bucket']:>6}: {b['models']:5} models -> picked {b['picked']}"
              + (f" ({b['from_avoid_list']} from the avoided list)" if b["from_avoid_list"] else ""))
    sample.sort(key=lambda r: r["model"])

    report = {
        "generated_at": datetime.datetime.now(datetime.timezone.utc).isoformat(),
        "parameters": {
            "models_file": str(models_file), "per_bucket": args.per_bucket, "seed": args.seed,
            "avoid_file": str(avoid_file), "required_files": args.require_file, "bucket_labels": BUCKET_LABELS,
        },
        "picked_count": len(sample),
        "picked_from_avoid_list": [r["model"] for r in sample if r["avoided"]],
        "buckets": bucket_rows,
        "dropped": dropped,
        "sample": sample,
    }
    json_path, md_path = write_reports(args.reports_dir, args.output_name, report, render_markdown_report(report))
    txt_path = args.reports_dir / f"{args.output_name}.txt"
    txt_path.write_text("".join(f"{r['model']}\n" for r in sample), encoding="utf-8")
    print(f"\nPicked {len(sample)} models ({len(report['picked_from_avoid_list'])} from the avoided list)")
    print(f"Written to {txt_path}, {json_path} and {md_path}")


if __name__ == "__main__":
    main()
