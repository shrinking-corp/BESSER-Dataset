#!/usr/bin/env python3
"""Export a histogram of the real per-model mutation ratio, plus the fitted
Beta distribution's expected counts on the same bins, into one Excel-ready
CSV -- for a combo chart (bar = real histogram, line = fitted curve).

Refits the Beta distribution inline (via fit_mutation_distribution.py's
functions) rather than reading a separate fit-report file, so the chart
data and the fit are always computed from the same run, never stale.

Written `;`-delimited with `,` as the decimal separator (matches this
project's Excel locale -- see export_difficulty_scores_for_excel.py).

Usage:
    python scripts/export_mutation_distribution_for_excel.py --report PATH
        [--score-field mutation_score] [--bins N] [--reports-dir PATH]
"""
from __future__ import annotations

import argparse
import csv
import sys
from pathlib import Path

import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parent))
from fit_mutation_distribution import (  # noqa: E402
    beta_pdf, fit_beta_method_of_moments, ks_statistic_vs_beta, load_scores,
)


def de(value: float, decimals: int) -> str:
    return f"{value:.{decimals}f}".replace(".", ",")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--report", type=Path, required=True)
    parser.add_argument("--score-field", default="mutation_score")
    parser.add_argument("--bins", type=int, default=40)
    parser.add_argument("--reports-dir", type=Path, default=Path(__file__).resolve().parent.parent / "reports")
    args = parser.parse_args()

    scores = load_scores(args.report, args.score_field)
    alpha, beta = fit_beta_method_of_moments(scores)
    d_stat = ks_statistic_vs_beta(scores, alpha, beta)
    print(f"Loaded {len(scores)} scores from {args.report}")
    print(f"Fitted Beta(alpha={alpha:.4f}, beta={beta:.4f})   KS D={d_stat:.4f}")

    counts, edges = np.histogram(scores, bins=args.bins, range=(0.0, 1.0))
    centers = (edges[:-1] + edges[1:]) / 2.0
    bin_width = edges[1] - edges[0]
    n = len(scores)

    # Expected count per bin under the fitted Beta, on the SAME scale as the
    # real histogram's counts (density * bin_width * n), so both series can
    # share one y-axis in Excel.
    fitted_density = beta_pdf(centers, alpha, beta)
    fitted_counts = fitted_density * bin_width * n

    out_path = args.reports_dir / "mutation_ratio_distribution_bins.csv"
    with out_path.open("w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f, delimiter=";")
        writer.writerow(["bin_center", "count", "fitted_beta_count"])
        for center, count, fitted in zip(centers, counts, fitted_counts):
            writer.writerow([de(float(center), 4), int(count), de(float(fitted), 4)])

    print(f"Wrote {out_path}")
    print("In Excel: select all 3 columns -> Insert Chart -> Combo Chart, "
          "set 'count' as Clustered Column and 'fitted_beta_count' as Line "
          "(check 'fitted_beta_count' does NOT need a secondary axis, since "
          "both are already on the same count scale).")


if __name__ == "__main__":
    main()
