#!/usr/bin/env python3
"""Compute the reference paper's difficulty-score formula for every measured
model, for a like-for-like comparison against our PCA-based
`difficulty_score` (see `scripts/compute_difficulty_score.py` and
docs/DECISIONS.md, 2026-09-17 entries).

Formula (paper's own weights, FK term dropped and the rest rescaled to sum
to 1 -- see docs/DECISIONS.md for that rescaling):

    D = w_c*C + w_r*R + w_a*A
    w_c = 0.3571   (0.35 / 0.98)
    w_r = 0.4082   (0.40 / 0.98)
    w_a = 0.2347   (0.23 / 0.98)

Where, from `model_metadata.json`:
    C = classes
    A = attributes
    R = associations + aggregation + composition + generalizations
        (relationship complexity -- every separate relationship type in
        this dataset counted once each; `aggregation` is confirmed always 0
        here but included for a correct/complete definition. The paper's R
        also includes "dependency", confirmed always 0 in this dataset --
        no `Dependency` class is used anywhere in the BUML models.)

Unlike the PCA score, C/R/A are NOT standardized or log-transformed here --
this reproduces the paper's formula as specified, applied directly to raw
counts. The result is therefore NOT bounded to any fixed range (a model
with a huge class count has an unbounded D); it is reported as-is, alongside
its own min/max for reference, rather than rescaled to [0, 100] -- rescaling
would be an addition of our own, not part of the paper's formula, and would
get in the way of comparing raw formula behavior against the PCA score.

Read the PCA score's docstring/DECISIONS.md entry for why the PCA score
uses log1p+standardization+PCA instead of raw counts -- that contrast (a
hand-picked linear formula on raw counts vs. a data-driven, scale-robust
composite) is exactly what the comparison is meant to surface.

Usage:
    python scripts/compute_article_difficulty_score.py [--dataset-dir PATH]
        [--reports-dir PATH] [--dry-run]
"""
from __future__ import annotations

import argparse
import datetime
import json
from pathlib import Path

W_C = 0.35 / 0.98
W_R = 0.40 / 0.98
W_A = 0.23 / 0.98

METADATA_FILENAME = "model_metadata.json"


def load_models(dataset_dir: Path) -> list[tuple[str, Path, dict]]:
    """Every measured model's name, metadata path, and parsed metadata, in a
    stable (sorted-by-name) order -- determinism requires a fixed row order."""
    out: list[tuple[str, Path, dict]] = []
    for d in sorted(dataset_dir.iterdir(), key=lambda p: p.name):
        p = d / METADATA_FILENAME
        if not p.is_file():
            continue
        try:
            data = json.loads(p.read_text(encoding="utf-8"))
        except json.JSONDecodeError:
            continue
        if data.get("status") != "measured":
            continue
        out.append((d.name, p, data))
    return out


def compute_car(data: dict) -> tuple[float, float, float]:
    """Returns (C, R, A) for one model's metadata, per the module docstring."""
    c = float(data.get("classes") or 0)
    r = float(
        (data.get("associations") or 0)
        + (data.get("aggregation") or 0)
        + (data.get("composition") or 0)
        + (data.get("generalizations") or 0)
    )
    a = float(data.get("attributes") or 0)
    return c, r, a


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--dataset-dir", type=Path, default=Path(__file__).resolve().parent.parent / "Dataset")
    parser.add_argument("--reports-dir", type=Path, default=Path(__file__).resolve().parent.parent / "reports")
    parser.add_argument("--dry-run", action="store_true",
                         help="Compute and report everything, but don't write into model_metadata.json files")
    args = parser.parse_args()

    entries = load_models(args.dataset_dir)
    print(f"Loaded {len(entries)} measured models")
    print(f"Weights: w_c={W_C:.4f}  w_r={W_R:.4f}  w_a={W_A:.4f}")

    scores = []
    for name, path, data in entries:
        c, r, a = compute_car(data)
        d = W_C * c + W_R * r + W_A * a
        scores.append((name, path, data, c, r, a, d))

    d_values = [s[6] for s in scores]
    print(f"\nD range: [{min(d_values):.4f}, {max(d_values):.4f}]")
    print(f"D mean: {sum(d_values)/len(d_values):.4f}")

    if not args.dry_run:
        written = 0
        for name, path, data, c, r, a, d in scores:
            data["difficulty_score_article"] = d
            data["difficulty_score_article_c"] = c
            data["difficulty_score_article_r"] = r
            data["difficulty_score_article_a"] = a
            path.write_text(json.dumps(data, indent=2) + "\n", encoding="utf-8")
            written += 1
        print(f"\nWrote difficulty_score_article into {written}/{len(scores)} models' model_metadata.json")
    else:
        print("\n--dry-run: nothing written to model_metadata.json files")

    report = {
        "generated_at": datetime.datetime.now(datetime.timezone.utc).isoformat(),
        "formula": "D = w_c*C + w_r*R + w_a*A",
        "weights": {"w_c": W_C, "w_r": W_R, "w_a": W_A},
        "r_definition": "associations + aggregation + composition + generalizations",
        "models_scored": len(scores),
        "d_min": min(d_values),
        "d_max": max(d_values),
        "d_mean": sum(d_values) / len(d_values),
        "dry_run": args.dry_run,
    }
    args.reports_dir.mkdir(parents=True, exist_ok=True)
    report_path = args.reports_dir / "difficulty_score_article_report.json"
    report_path.write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")
    print(f"Report written to {report_path}")


if __name__ == "__main__":
    main()
