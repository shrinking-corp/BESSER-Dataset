#!/usr/bin/env python3
"""Export the PCA and article difficulty scores into flat CSV files Excel can
open directly, for building box-and-whisker and (manually faked) violin
charts. Read-only: does not write anything into `model_metadata.json`.

Written `;`-delimited with `,` as the decimal separator (European-locale
Excel default) -- with a plain `,`-delimited/`.`-decimal CSV, a
comma-as-decimal Excel install treats each number as text (or truncates it
to an integer at the first `.`) instead of parsing it as a float.

Writes three files into --reports-dir:

  difficulty_scores_raw.csv
      One row per measured model: model, difficulty_score,
      difficulty_score_article, difficulty_score_article_capped_100.
      Feed the numeric columns into Excel's native Box and Whisker chart
      (Insert > Insert Statistic Chart > Box and Whisker) -- select the
      score columns with headers, but NOT the `model` column (it would be
      read as a grouping category, and since every model name is unique
      there'd be nothing to group, producing one lone point per "box").
      The 4th column is the article score CAPPED (clipped) at 100 --
      min(difficulty_score_article, 100) -- deliberately NOT min-max
      rescaled: capping only pulls in the extreme tail above 100 (a small
      number of models; the article score is unbounded, up to ~931 in this
      dataset) while leaving every other model's value untouched, so the
      bulk of the distribution's real shape/spread is preserved for
      comparison against the PCA score's native [0, 100] axis. A full
      min-max rescale was tried first and rejected: it compresses the
      entire non-outlier bulk of the distribution into a sliver near 0
      (since one ~932-class model dominates the observed max), which is
      far less informative than capping. This does NOT change the real,
      unbounded difficulty_score_article value anywhere else (report,
      model_metadata.json) -- it exists only for this chart comparison.

  difficulty_scores_pca_violin_bins.csv
  difficulty_scores_article_violin_bins.csv
      A histogram of each score (default 40 bins), with both a raw count
      and a mirrored +/- pair of columns already computed -- Excel has no
      native violin chart, but a *horizontal, stacked* bar chart built from
      the neg/pos columns (bars pointing left and right from a center line,
      one row per bin) produces the same shape. Columns: bin_center, count,
      density, neg_count, neg_density. The article version bins the
      capped-at-100 values (same reasoning as above) -- models above 100
      all land in the top bin. Each file bins its own score over its own
      range -- NOT comparable side by side on one shared axis (see below).

  difficulty_scores_pyramid_bins.csv
      One row per integer score from 0 to 100 inclusive (101 rows). Each
      score is rounded to the nearest whole number, then counted. Exactly
      3 columns, nothing else: score (0-100), pca_count (how many models
      round to this PCA score), article_count (how many models round to
      this article-capped score). No sign tricks, no extra columns --
      build whatever chart layout you want from these two plain counts.

Usage:
    python scripts/export_difficulty_scores_for_excel.py
        [--dataset-dir PATH] [--reports-dir PATH] [--bins N]
"""
from __future__ import annotations

import argparse
import csv
import json
from pathlib import Path

import numpy as np

METADATA_FILENAME = "model_metadata.json"


def de(value: float, decimals: int) -> str:
    """Format a float with `,` as the decimal separator, for a comma-decimal
    Excel locale."""
    return f"{value:.{decimals}f}".replace(".", ",")


def load_scores(dataset_dir: Path) -> tuple[list[str], list[float], list[float]]:
    models, pca, article = [], [], []
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
            continue
        models.append(d.name)
        pca.append(float(data["difficulty_score"]))
        article.append(float(data["difficulty_score_article"]))
    return models, pca, article


def write_violin_bins(path: Path, values: np.ndarray, bins: int) -> None:
    counts, edges = np.histogram(values, bins=bins)
    centers = (edges[:-1] + edges[1:]) / 2.0
    bin_width = edges[1] - edges[0]
    total = counts.sum()
    with path.open("w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f, delimiter=";")
        writer.writerow(["bin_center", "count", "density", "neg_count", "neg_density"])
        for center, count in zip(centers, counts):
            density = count / (total * bin_width) if total and bin_width else 0.0
            writer.writerow([de(center, 4), int(count), de(density, 6), -int(count), de(-density, 6)])


def write_pyramid_bins(path: Path, pca_values: np.ndarray, article_values: np.ndarray, scale_max: int) -> None:
    """One row per integer score 0..scale_max: how many models round to
    that score, for each of the two score columns. Exactly 3 plain columns:
    score, pca_count, article_count."""
    pca_rounded = np.clip(np.round(pca_values), 0, scale_max).astype(int)
    article_rounded = np.clip(np.round(article_values), 0, scale_max).astype(int)
    pca_counts = np.bincount(pca_rounded, minlength=scale_max + 1)
    article_counts = np.bincount(article_rounded, minlength=scale_max + 1)
    with path.open("w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f, delimiter=";")
        writer.writerow(["score", "pca_count", "article_count"])
        for score in range(scale_max + 1):
            writer.writerow([score, int(pca_counts[score]), int(article_counts[score])])


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--dataset-dir", type=Path, default=Path(__file__).resolve().parent.parent / "Dataset")
    parser.add_argument("--reports-dir", type=Path, default=Path(__file__).resolve().parent.parent / "reports")
    parser.add_argument("--bins", type=int, default=40)
    args = parser.parse_args()

    models, pca, article = load_scores(args.dataset_dir)
    print(f"Loaded {len(models)} measured models with both scores")

    args.reports_dir.mkdir(parents=True, exist_ok=True)

    article_arr = np.array(article)
    article_capped = np.minimum(article_arr, 100.0)
    n_capped = int((article_arr > 100.0).sum())

    raw_path = args.reports_dir / "difficulty_scores_raw.csv"
    with raw_path.open("w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f, delimiter=";")
        writer.writerow([
            "model", "difficulty_score", "difficulty_score_article",
            "difficulty_score_article_capped_100",
        ])
        for m, p, a, a_cap in zip(models, pca, article, article_capped):
            writer.writerow([m, de(p, 6), de(a, 6), de(float(a_cap), 6)])
    print(f"Wrote {raw_path} ({n_capped}/{len(models)} models capped at 100)")

    pca_bins_path = args.reports_dir / "difficulty_scores_pca_violin_bins.csv"
    write_violin_bins(pca_bins_path, np.array(pca), args.bins)
    print(f"Wrote {pca_bins_path}")

    article_bins_path = args.reports_dir / "difficulty_scores_article_violin_bins.csv"
    write_violin_bins(article_bins_path, article_capped, args.bins)
    print(f"Wrote {article_bins_path} (binned on capped values)")

    pyramid_path = args.reports_dir / "difficulty_scores_pyramid_bins.csv"
    write_pyramid_bins(pyramid_path, np.array(pca), article_capped, scale_max=100)
    print(f"Wrote {pyramid_path} (101 rows, integer scores 0-100)")


if __name__ == "__main__":
    main()
