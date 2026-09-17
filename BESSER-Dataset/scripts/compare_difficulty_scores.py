#!/usr/bin/env python3
"""Compare the PCA-based `difficulty_score` against the reference paper's
`difficulty_score_article`, for every measured model that has both.

Read-only: does not write anything into `model_metadata.json`. Writes a
comparison report (JSON) with:
  - Pearson correlation (linear agreement) and Spearman rank correlation
    (agreement on *ordering*, robust to the fact the two scores live on
    different scales -- PCA score is bounded [0,100], the article score is
    an unbounded raw-count linear formula).
  - Top-N agreement: how much overlap between "hardest N%" under each score.
  - The models where the two scores disagree most in rank -- useful to
    manually inspect *why* (e.g. a model that's huge on raw class count but
    structurally uniform vs. one that's smaller but PCA-complex on PC2's
    style axis).

Rank correlation is computed by hand (average-rank Spearman) rather than
importing scipy, since only numpy is installed in this project's `.venv`.

Usage:
    python scripts/compare_difficulty_scores.py [--dataset-dir PATH]
        [--reports-dir PATH] [--top-n N] [--top-pct P]
"""
from __future__ import annotations

import argparse
import datetime
import json
from pathlib import Path

import numpy as np

METADATA_FILENAME = "model_metadata.json"


def load_scores(dataset_dir: Path) -> tuple[list[str], np.ndarray, np.ndarray]:
    """Every measured model's name and both difficulty scores, in a stable
    (sorted-by-name) order. Skips any model missing either score (e.g. if
    one script's write step was interrupted partway through)."""
    models: list[str] = []
    pca: list[float] = []
    article: list[float] = []
    skipped = 0
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
        if "difficulty_score" not in data or "difficulty_score_article" not in data:
            skipped += 1
            continue
        models.append(d.name)
        pca.append(float(data["difficulty_score"]))
        article.append(float(data["difficulty_score_article"]))
    if skipped:
        print(f"Skipped {skipped} measured models missing one or both scores")
    return models, np.array(pca, dtype=np.float64), np.array(article, dtype=np.float64)


def rankdata(values: np.ndarray) -> np.ndarray:
    """Average-rank ranking (1-indexed, ties share the mean rank of their
    positions), matching scipy.stats.rankdata's default 'average' method --
    reimplemented here so this doesn't need scipy installed."""
    order = np.argsort(values, kind="mergesort")
    ranks = np.empty(len(values), dtype=np.float64)
    sorted_vals = values[order]

    i = 0
    n = len(values)
    while i < n:
        j = i
        while j + 1 < n and sorted_vals[j + 1] == sorted_vals[i]:
            j += 1
        avg_rank = (i + j) / 2.0 + 1.0
        ranks[order[i : j + 1]] = avg_rank
        i = j + 1
    return ranks


def pearson(a: np.ndarray, b: np.ndarray) -> float:
    return float(np.corrcoef(a, b)[0, 1])


def spearman(a: np.ndarray, b: np.ndarray) -> float:
    return pearson(rankdata(a), rankdata(b))


def top_n_overlap(models: list[str], a: np.ndarray, b: np.ndarray, n: int) -> dict:
    top_a = set(np.array(models)[np.argsort(a)[::-1][:n]])
    top_b = set(np.array(models)[np.argsort(b)[::-1][:n]])
    overlap = top_a & top_b
    return {
        "n": n,
        "overlap_count": len(overlap),
        "overlap_fraction": len(overlap) / n,
        "only_in_pca_top_n": sorted(top_a - top_b),
        "only_in_article_top_n": sorted(top_b - top_a),
    }


def biggest_rank_disagreements(models: list[str], pca: np.ndarray, article: np.ndarray, n: int) -> list[dict]:
    pca_rank_pct = rankdata(pca) / len(pca) * 100.0
    article_rank_pct = rankdata(article) / len(article) * 100.0
    diff = np.abs(pca_rank_pct - article_rank_pct)
    order = np.argsort(diff)[::-1][:n]
    return [
        {
            "model": models[i],
            "pca_score": float(pca[i]),
            "pca_rank_percentile": float(pca_rank_pct[i]),
            "article_score": float(article[i]),
            "article_rank_percentile": float(article_rank_pct[i]),
            "rank_percentile_gap": float(diff[i]),
        }
        for i in order
    ]


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--dataset-dir", type=Path, default=Path(__file__).resolve().parent.parent / "Dataset")
    parser.add_argument("--reports-dir", type=Path, default=Path(__file__).resolve().parent.parent / "reports")
    parser.add_argument("--top-n", type=int, default=15, help="How many biggest rank-disagreement models to list")
    parser.add_argument("--top-pct", type=float, default=10.0, help="Top-N%% overlap to compute (default: top 10%%)")
    args = parser.parse_args()

    models, pca, article = load_scores(args.dataset_dir)
    print(f"Compared {len(models)} models with both scores")

    r_pearson = pearson(pca, article)
    r_spearman = spearman(pca, article)
    print(f"\nPearson correlation (linear agreement):  {r_pearson:+.4f}")
    print(f"Spearman correlation (rank agreement):    {r_spearman:+.4f}")

    n_top = max(1, round(len(models) * args.top_pct / 100.0))
    overlap = top_n_overlap(models, pca, article, n_top)
    print(f"\nTop {args.top_pct}% ({n_top} models) overlap: "
          f"{overlap['overlap_count']}/{n_top} ({overlap['overlap_fraction']*100:.1f}%)")

    disagreements = biggest_rank_disagreements(models, pca, article, args.top_n)
    print(f"\nBiggest rank-percentile disagreements (top {args.top_n}):")
    print(f"  {'model':20} {'pca_score':>10} {'pca_pct':>8} {'article_score':>14} {'art_pct':>8} {'gap':>8}")
    for row in disagreements:
        print(f"  {row['model']:20} {row['pca_score']:10.2f} {row['pca_rank_percentile']:8.2f} "
              f"{row['article_score']:14.2f} {row['article_rank_percentile']:8.2f} {row['rank_percentile_gap']:8.2f}")

    report = {
        "generated_at": datetime.datetime.now(datetime.timezone.utc).isoformat(),
        "models_compared": len(models),
        "pearson_correlation": r_pearson,
        "spearman_correlation": r_spearman,
        "top_pct": args.top_pct,
        "top_n_overlap": overlap,
        "biggest_rank_disagreements": disagreements,
        "pca_score_min": float(pca.min()),
        "pca_score_max": float(pca.max()),
        "article_score_min": float(article.min()),
        "article_score_max": float(article.max()),
    }
    args.reports_dir.mkdir(parents=True, exist_ok=True)
    report_path = args.reports_dir / "difficulty_score_comparison_report.json"
    report_path.write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")
    print(f"\nReport written to {report_path}")


if __name__ == "__main__":
    main()
