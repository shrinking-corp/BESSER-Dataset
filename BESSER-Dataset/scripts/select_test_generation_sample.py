#!/usr/bin/env python3
"""Pick the shared test-generation-comparison sample: one model list used by
both Track A (library-generated tests, us) and Track B (the colleague's LLM
mutation-feedback loop), so "library vs. LLM" is measured on identical models.

Decided 2026-09-29 (see docs/DECISIONS.md): stratify by
`has_logic` method count, not `difficulty_score` -- the two don't always
track together (e.g. model_2023 scores 86.66/100 on difficulty_score but has
zero methods at all), and the whole point of this sample is testing methods
that have real logic, so it must be built around that directly. Allocation
across has_logic buckets is EQUAL (not proportional to the dataset's real
shape): the purpose of this sample is comparing test-generation methods
across complexity levels, not describing the dataset's natural distribution,
so the rare high-has_logic-count buckets get the same representation as the
common low-count ones.

Two steps:

1. **De-duplicate.** Several models share identical (no_logic, trivial,
   has_logic, total_methods) counts -- a strong signal of near-identical
   generated content under different model names (confirmed by eye on a few
   pairs, e.g. model_455/model_456 both 370 has_logic / 961 total). Only one
   representative per duplicate group (the alphabetically-first model name,
   for determinism) is kept in the eligible pool, so the sample isn't
   secretly testing the same code twice.
2. **Bucket + seeded random sample.** Models are assigned to the same
   has_logic buckets `classify_method_logic.py` already reports
   (1-5/6-10/11-20/21-50/51-100/101-200/200+; the "0" bucket is excluded
   entirely -- nothing for either track to target). --sample-size is split
   as evenly as possible across the 7 buckets, then that many models are
   drawn from each bucket's (de-duplicated) pool via a seeded RNG.

Usage:
    python scripts/select_test_generation_sample.py
        [--classification-report reports/method_logic_classification_report.json]
        [--reports-dir reports] [--sample-size 200] [--seed 42]
        [--output-name test_generation_sample]

Writes <output-name>.txt (one model name per line, same format as
usable_models.txt) and <output-name>_report.{json,md} (full methodology
detail: bucket targets vs. actual, duplicate groups dropped, per-model
has_logic/total_methods, for handing to the colleague alongside the list).
"""
from __future__ import annotations

import argparse
import datetime
import json
import random
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from classify_method_logic import _HAS_LOGIC_BUCKET_EDGES, _HAS_LOGIC_BUCKET_LABELS, _bucket  # noqa: E402

# The "0" bucket (no has_logic methods at all) is never eligible for Phase 4.
ELIGIBLE_BUCKET_LABELS = [l for l in _HAS_LOGIC_BUCKET_LABELS if l != "0"]


def load_measured_results(report_path: Path) -> list[dict]:
    data = json.loads(report_path.read_text(encoding="utf-8"))
    return [r for r in data["results"] if r.get("totals")]


def deduplicate(results: list[dict]) -> tuple[list[dict], list[dict]]:
    """Group by (no_logic, trivial, has_logic, total_methods); keep only the
    alphabetically-first model name per group. Returns (kept, dropped)."""
    groups: dict[tuple, list[dict]] = {}
    for r in results:
        t = r["totals"]
        sig = (t["no_logic"], t["trivial"], t["has_logic"], t["total_methods"])
        groups.setdefault(sig, []).append(r)

    kept: list[dict] = []
    dropped: list[dict] = []
    for sig, members in groups.items():
        members_sorted = sorted(members, key=lambda r: r["model"])
        kept.append(members_sorted[0])
        for m in members_sorted[1:]:
            dropped.append({"model": m["model"], "duplicate_of": members_sorted[0]["model"],
                             "shared_signature": {"no_logic": sig[0], "trivial": sig[1],
                                                   "has_logic": sig[2], "total_methods": sig[3]}})
    return kept, dropped


def assign_buckets(results: list[dict]) -> dict[str, list[dict]]:
    buckets: dict[str, list[dict]] = {label: [] for label in ELIGIBLE_BUCKET_LABELS}
    for r in results:
        hl = r["totals"]["has_logic"]
        if hl <= 0:
            continue
        label = _bucket(hl, _HAS_LOGIC_BUCKET_EDGES, _HAS_LOGIC_BUCKET_LABELS)
        buckets[label].append(r)
    return buckets


def bucket_targets(sample_size: int, num_buckets: int) -> list[int]:
    """Split sample_size as evenly as possible across num_buckets, giving
    the +1 remainder to the first buckets in order (deterministic)."""
    base, remainder = divmod(sample_size, num_buckets)
    return [base + 1 if i < remainder else base for i in range(num_buckets)]


def select_sample(buckets: dict[str, list[dict]], targets: dict[str, int], seed: int) -> dict:
    rng = random.Random(seed)
    selected: dict[str, list[dict]] = {}
    shortfalls: dict[str, dict] = {}
    for label in ELIGIBLE_BUCKET_LABELS:
        pool = sorted(buckets[label], key=lambda r: r["model"])
        target = targets[label]
        if len(pool) < target:
            shortfalls[label] = {"target": target, "available": len(pool)}
            selected[label] = pool  # take everything available
        else:
            selected[label] = rng.sample(pool, target)
    return {"selected": selected, "shortfalls": shortfalls}


def build_report(
    all_results: list[dict], kept: list[dict], dropped: list[dict],
    buckets: dict[str, list[dict]], targets: dict[str, int],
    selection: dict, seed: int, sample_size: int,
) -> dict:
    selected = selection["selected"]
    flat_selected = [r for label in ELIGIBLE_BUCKET_LABELS for r in selected[label]]

    return {
        "generated_at": datetime.datetime.now(datetime.timezone.utc).isoformat(),
        "seed": seed,
        "requested_sample_size": sample_size,
        "actual_sample_size": len(flat_selected),
        "total_measured_models": len(all_results),
        "models_with_zero_has_logic_excluded": sum(1 for r in all_results if r["totals"]["has_logic"] == 0),
        "duplicate_groups_found": len({d["duplicate_of"] for d in dropped}),
        "models_dropped_as_duplicates": len(dropped),
        "eligible_pool_after_dedup": sum(len(v) for v in buckets.values()),
        "bucket_summary": [
            {
                "bucket": label,
                "pool_size_after_dedup": len(buckets[label]),
                "target": targets[label],
                "actual_selected": len(selected[label]),
                "shortfall": selection["shortfalls"].get(label),
            }
            for label in ELIGIBLE_BUCKET_LABELS
        ],
        "dropped_duplicates": sorted(dropped, key=lambda d: d["model"]),
        "sample": sorted(
            (
                {"model": r["model"], "bucket": label, "has_logic": r["totals"]["has_logic"],
                 "trivial": r["totals"]["trivial"], "no_logic": r["totals"]["no_logic"],
                 "total_methods": r["totals"]["total_methods"]}
                for label in ELIGIBLE_BUCKET_LABELS for r in selected[label]
            ),
            key=lambda x: x["model"],
        ),
    }


def render_markdown_report(report: dict) -> str:
    lines = [
        "# Test-generation-comparison sample selection report",
        "",
        f"Generated: {report['generated_at']}  |  seed: {report['seed']}",
        "",
        "Shared sample for Track A (library-generated tests) and Track B "
        "(the colleague's LLM mutation-feedback loop) -- both tracks work "
        "against exactly this model list, so results are directly comparable.",
        "",
        f"- **Requested sample size:** {report['requested_sample_size']}",
        f"- **Actual sample size:** {report['actual_sample_size']}",
        f"- **Total measured models (input pool):** {report['total_measured_models']}",
        f"- **Excluded (zero has_logic methods):** {report['models_with_zero_has_logic_excluded']}",
        f"- **Duplicate groups found:** {report['duplicate_groups_found']} "
        f"({report['models_dropped_as_duplicates']} models dropped, one kept per group)",
        f"- **Eligible pool after dedup:** {report['eligible_pool_after_dedup']}",
        "",
        "## Bucket breakdown",
        "",
        "| has_logic bucket | Pool (after dedup) | Target | Selected | Shortfall |",
        "|---|---|---|---|---|",
    ]
    for b in report["bucket_summary"]:
        shortfall = "-" if not b["shortfall"] else f"wanted {b['shortfall']['target']}, only {b['shortfall']['available']} available"
        lines.append(f"| {b['bucket']} | {b['pool_size_after_dedup']} | {b['target']} | {b['actual_selected']} | {shortfall} |")

    lines += [
        "",
        "## Full sample",
        "",
        "| Model | Bucket | has_logic | trivial | no_logic | total_methods |",
        "|---|---|---|---|---|---|",
    ]
    for m in report["sample"]:
        lines.append(f"| {m['model']} | {m['bucket']} | {m['has_logic']} | {m['trivial']} | "
                      f"{m['no_logic']} | {m['total_methods']} |")

    lines += [
        "",
        f"{report['models_dropped_as_duplicates']} models were excluded as exact-duplicate "
        "twins of another model already in the eligible pool (identical no_logic/trivial/"
        "has_logic/total_methods counts) -- see `dropped_duplicates` in the accompanying "
        ".json for the full list and which model each was a duplicate of.",
    ]
    return "\n".join(lines) + "\n"


def main() -> None:
    repo_root = Path(__file__).resolve().parent.parent
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--classification-report", type=Path,
                         default=repo_root / "reports" / "method_logic_classification_report.json")
    parser.add_argument("--reports-dir", type=Path, default=repo_root / "reports")
    parser.add_argument("--sample-size", type=int, default=200)
    parser.add_argument("--seed", type=int, default=42)
    parser.add_argument("--output-name", type=str, default="test_generation_sample")
    args = parser.parse_args()

    print(f"Loading {args.classification_report}...")
    all_results = load_measured_results(args.classification_report)
    print(f"  {len(all_results)} measured models")

    kept, dropped = deduplicate(all_results)
    print(f"De-duplication: {len(dropped)} models dropped as exact duplicates, "
          f"{len(kept)} unique signatures remain")

    buckets = assign_buckets(kept)
    for label in ELIGIBLE_BUCKET_LABELS:
        print(f"  bucket {label:>8}: {len(buckets[label])} models eligible (post-dedup)")

    targets_list = bucket_targets(args.sample_size, len(ELIGIBLE_BUCKET_LABELS))
    targets = dict(zip(ELIGIBLE_BUCKET_LABELS, targets_list))
    print(f"Targets per bucket: {targets}")

    selection = select_sample(buckets, targets, args.seed)
    report = build_report(all_results, kept, dropped, buckets, targets, selection, args.seed, args.sample_size)

    args.reports_dir.mkdir(parents=True, exist_ok=True)
    txt_path = args.reports_dir / f"{args.output_name}.txt"
    txt_path.write_text("".join(f"{m['model']}\n" for m in report["sample"]))
    json_path = args.reports_dir / f"{args.output_name}_report.json"
    json_path.write_text(json.dumps(report, indent=2) + "\n")
    md_path = args.reports_dir / f"{args.output_name}_report.md"
    md_path.write_text(render_markdown_report(report))

    print(f"\nActual sample size: {report['actual_sample_size']}/{report['requested_sample_size']}")
    if any(b["shortfall"] for b in report["bucket_summary"]):
        print("WARNING: one or more buckets had a shortfall -- see the report for detail.")
    print(f"Sample list: {txt_path}")
    print(f"Full report: {json_path} and {md_path}")


if __name__ == "__main__":
    main()
