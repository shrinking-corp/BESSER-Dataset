#!/usr/bin/env python3
"""Assign every benchmark model a difficulty bucket and a train/test side,
stratified by bucket. Read-only on the dataset: writes only reports.

1. **Buckets.** The official `difficulty_score` (0-100, from
   `compute_difficulty_score.py`) is cut into 10 buckets of width 10:
   0-10, 10-20, ..., 90-100 (a score of exactly 100 goes into 90-100).
2. **Duplicate groups (safety net).** Models with byte-identical `.puml`
   files are one benchmark task; splitting them across train and test would
   leak the test set into training. The default input,
   `reports/unique_models.txt` (`select_unique_models.py`), already holds
   one model per diagram, so this should find none. Any it does find (e.g.
   when given `usable_models.txt`) go to one side as a whole.
3. **Stratified split.** Within each bucket the groups are shuffled with a
   per-bucket RNG seeded from `--seed` and the bucket, then taken into the test
   set until it holds `round(bucket size * (1 - train ratio))` models; every
   bucket with at least two groups gets at least `--min-test-per-bucket` test
   models. Because each bucket's order is fixed by the seed, a smaller test
   ratio always gives a subset of a larger one's test set.

`--require-file` (repeatable) drops models missing a file the benchmark needs,
e.g. `test_super_suite.py` (a model without a green super suite has nothing
to test against). Every dropped model is listed in the report.

Writes `<output-name>.json/.md` (parameters, per-bucket counts, duplicate
groups, dropped models, one row per model) and `<output-name>_train.txt` /
`<output-name>_test.txt` (one model per line, usable as --models-file).

Usage:
    python scripts/make_benchmark_split.py --train-ratio R
        [--models-file reports/unique_models.txt] [--seed 42]
        [--min-test-per-bucket 1] [--require-file NAME ...]
        [--dataset-dir PATH] [--reports-dir PATH] [--output-name benchmark_split]
"""
from __future__ import annotations

import argparse
import datetime
import random
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from _common.buml import puml_digest  # noqa: E402
from _common.io import add_common_io_args, iter_measured_models, read_model_names  # noqa: E402
from _common.report import write_reports  # noqa: E402

BUCKET_WIDTH = 10
BUCKET_COUNT = 10
BUCKET_LABELS = [f"{i * BUCKET_WIDTH}-{(i + 1) * BUCKET_WIDTH}" for i in range(BUCKET_COUNT)]


def bucket_index(score: float) -> int:
    return min(max(int(score // BUCKET_WIDTH), 0), BUCKET_COUNT - 1)


def load_candidates(dataset_dir: Path, names: list[str], required_files: list[str]) -> tuple[list[dict], dict]:
    """One row per model that has a difficulty score, a PUML file and every
    required file; everything else is returned in `dropped` by reason."""
    wanted = set(names)
    scores = {name: float(data["difficulty_score"])
              for name, _path, data in iter_measured_models(dataset_dir, wanted) if "difficulty_score" in data}
    dropped: dict[str, list[str]] = {"no_difficulty_score": [], "no_puml": []}
    dropped.update({f"missing_{f}": [] for f in required_files})
    rows = []
    for name in sorted(wanted):
        model_dir = dataset_dir / name
        if name not in scores:
            dropped["no_difficulty_score"].append(name)
            continue
        missing = [f for f in required_files if not (model_dir / f).is_file()]
        if missing:
            dropped[f"missing_{missing[0]}"].append(name)
            continue
        digest = puml_digest(model_dir)
        if digest is None:
            dropped["no_puml"].append(name)
            continue
        rows.append({"model": name, "difficulty_score": scores[name], "puml_sha256": digest})
    return rows, dropped


def group_duplicates(rows: list[dict]) -> list[list[dict]]:
    """Models with identical PUML content, as groups sorted by model name;
    a group's bucket is its first member's (identical diagrams normally share
    a score, and any that don't are reported)."""
    by_hash: dict[str, list[dict]] = {}
    for row in rows:
        by_hash.setdefault(row["puml_sha256"], []).append(row)
    groups = [sorted(members, key=lambda r: r["model"]) for members in by_hash.values()]
    return sorted(groups, key=lambda g: g[0]["model"])


def split_bucket(groups: list[list[dict]], train_ratio: float, min_test: int, seed: int, bucket: int) -> tuple[list, list]:
    """(train groups, test groups). Test takes groups from the front of the
    seeded order until it reaches its target; the last group always stays in
    train, so neither side of a bucket with two or more groups is empty."""
    order = list(groups)
    random.Random(f"{seed}:{bucket}").shuffle(order)
    if len(order) < 2:
        return order, []
    target = max(round(sum(len(g) for g in order) * (1.0 - train_ratio)), min_test)
    test, train, taken = [], [], 0
    for group in order[:-1]:
        if taken < target:
            test.append(group)
            taken += len(group)
        else:
            train.append(group)
    train.append(order[-1])
    return train, test


def render_markdown_report(report: dict) -> str:
    p = report["parameters"]
    lines = [
        "# Benchmark train/test split",
        "",
        f"Generated: {report['generated_at']}",
        "",
        f"- **Models file:** `{p['models_file']}` · **train ratio:** {p['train_ratio']} · **seed:** {p['seed']} · "
        f"**min test per bucket:** {p['min_test_per_bucket']} · **required files:** {', '.join(p['required_files']) or 'none'}",
        f"- **Models split:** {report['models_split']} (train {report['train_count']}, test {report['test_count']}, "
        f"actual test share {report['actual_test_share'] * 100:.2f}%)",
        f"- **Duplicate PUML groups:** {report['duplicate_group_count']} groups covering "
        f"{report['models_in_duplicate_groups']} models, each kept on one side",
        "",
        "## Per bucket",
        "",
        "| Difficulty | Models | Groups | Train | Test | Test share |",
        "|---|---:|---:|---:|---:|---:|",
    ]
    for b in report["buckets"]:
        share = f"{b['test'] / b['models'] * 100:.1f}%" if b["models"] else "–"
        lines.append(f"| {b['bucket']} | {b['models']} | {b['groups']} | {b['train']} | {b['test']} | {share} |")
    dropped = {k: v for k, v in report["dropped"].items() if v}
    lines += ["", "## Dropped models", ""]
    if dropped:
        lines += [f"- **{reason}:** {len(models)}" for reason, models in dropped.items()]
    else:
        lines.append("None.")
    if report["groups_with_mixed_buckets"]:
        lines += ["", f"**Note:** {len(report['groups_with_mixed_buckets'])} duplicate groups have members in "
                  "different buckets; each was placed by its first member (see the `.json`)."]
    lines += ["", "Per-model assignment: see the accompanying `.json` and the `_train.txt` / `_test.txt` lists."]
    return "\n".join(lines) + "\n"


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    add_common_io_args(parser, __file__)
    parser.add_argument("--models-file", type=Path, default=None,
                         help="Models to split (default: reports/unique_models.txt)")
    parser.add_argument("--train-ratio", type=float, required=True,
                         help="Share of each bucket that goes to train, e.g. 0.8 (no default on purpose)")
    parser.add_argument("--seed", type=int, default=42)
    parser.add_argument("--min-test-per-bucket", type=int, default=1)
    parser.add_argument("--require-file", action="append", default=[],
                         help="Drop models missing this file (repeatable), e.g. test_super_suite.py")
    parser.add_argument("--output-name", default="benchmark_split")
    args = parser.parse_args()
    if not 0.0 < args.train_ratio < 1.0:
        parser.error("--train-ratio must be between 0 and 1")

    models_file = args.models_file or args.reports_dir / "unique_models.txt"
    names = read_model_names(models_file)
    rows, dropped = load_candidates(args.dataset_dir, names, args.require_file)
    print(f"{len(rows)}/{len(names)} models eligible "
          f"({', '.join(f'{k}: {len(v)}' for k, v in dropped.items() if v) or 'none dropped'})")

    groups = group_duplicates(rows)
    by_bucket: dict[int, list[list[dict]]] = {i: [] for i in range(BUCKET_COUNT)}
    mixed = []
    for group in groups:
        buckets = {bucket_index(r["difficulty_score"]) for r in group}
        if len(buckets) > 1:
            mixed.append([r["model"] for r in group])
        by_bucket[bucket_index(group[0]["difficulty_score"])].append(group)

    assignments, bucket_rows = [], []
    for i in range(BUCKET_COUNT):
        train, test = split_bucket(by_bucket[i], args.train_ratio, args.min_test_per_bucket, args.seed, i)
        for side, side_groups in (("train", train), ("test", test)):
            for group in side_groups:
                for r in group:
                    assignments.append({
                        "model": r["model"], "difficulty_score": r["difficulty_score"],
                        "bucket": BUCKET_LABELS[i], "split": side,
                        "puml_group": group[0]["model"], "puml_sha256": r["puml_sha256"],
                    })
        bucket_rows.append({
            "bucket": BUCKET_LABELS[i],
            "models": sum(len(g) for g in by_bucket[i]),
            "groups": len(by_bucket[i]),
            "train": sum(len(g) for g in train),
            "test": sum(len(g) for g in test),
        })
        b = bucket_rows[-1]
        print(f"  {b['bucket']:>6}: {b['models']:5} models ({b['groups']} groups) -> train {b['train']}, test {b['test']}")
    assignments.sort(key=lambda a: a["model"])

    train_names = [a["model"] for a in assignments if a["split"] == "train"]
    test_names = [a["model"] for a in assignments if a["split"] == "test"]
    duplicate_groups = [[r["model"] for r in g] for g in groups if len(g) > 1]
    report = {
        "generated_at": datetime.datetime.now(datetime.timezone.utc).isoformat(),
        "parameters": {
            "models_file": str(models_file), "train_ratio": args.train_ratio, "seed": args.seed,
            "min_test_per_bucket": args.min_test_per_bucket, "required_files": args.require_file,
            "bucket_width": BUCKET_WIDTH, "bucket_labels": BUCKET_LABELS,
        },
        "models_in_file": len(names),
        "models_split": len(assignments),
        "train_count": len(train_names),
        "test_count": len(test_names),
        "actual_test_share": len(test_names) / len(assignments) if assignments else 0.0,
        "duplicate_group_count": len(duplicate_groups),
        "models_in_duplicate_groups": sum(len(g) for g in duplicate_groups),
        "duplicate_groups": duplicate_groups,
        "groups_with_mixed_buckets": mixed,
        "buckets": bucket_rows,
        "dropped": dropped,
        "assignments": assignments,
    }
    json_path, md_path = write_reports(args.reports_dir, args.output_name, report, render_markdown_report(report))
    for side, side_names in (("train", train_names), ("test", test_names)):
        (args.reports_dir / f"{args.output_name}_{side}.txt").write_text(
            "".join(f"{n}\n" for n in side_names), encoding="utf-8")

    print(f"\nTrain {len(train_names)} / test {len(test_names)} "
          f"({report['actual_test_share'] * 100:.2f}% test); "
          f"{len(duplicate_groups)} duplicate PUML groups kept together")
    print(f"Report written to {json_path} and {md_path}")


if __name__ == "__main__":
    main()
