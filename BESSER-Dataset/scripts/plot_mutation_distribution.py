#!/usr/bin/env python3
"""Plot a histogram of the real per-model mutation ratio against the fitted
Beta(alpha, beta) continuous distribution, and show it on screen.

Refits the Beta distribution inline (via fit_mutation_distribution.py),
so the plot always reflects the same run as the fit -- not a separately
saved fit-report that could go stale.

Usage:
    python scripts/plot_mutation_distribution.py --report PATH
        [--score-field mutation_score] [--bins N] [--save PATH]
"""
from __future__ import annotations

import argparse
import sys
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parent))
from fit_mutation_distribution import (  # noqa: E402
    beta_pdf, fit_beta_method_of_moments, ks_statistic_vs_beta, load_scores,
)


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--report", type=Path, required=True)
    parser.add_argument("--score-field", default="mutation_score")
    parser.add_argument("--bins", type=int, default=40)
    parser.add_argument("--save", type=Path, default=None, help="Also save the figure to this path (e.g. reports/charts/mutation_ratio_fit.png)")
    args = parser.parse_args()

    scores = load_scores(args.report, args.score_field)
    alpha, beta = fit_beta_method_of_moments(scores)
    d_stat = ks_statistic_vs_beta(scores, alpha, beta)

    fig, ax = plt.subplots(figsize=(9, 6))
    ax.hist(scores, bins=args.bins, range=(0.0, 1.0), density=True,
            color="#4C72B0", alpha=0.75, edgecolor="white", label=f"Real data (n={len(scores)})")

    x = np.linspace(1e-4, 1 - 1e-4, 1000)
    ax.plot(x, beta_pdf(x, alpha, beta), color="#C44E52", linewidth=2.5,
            label=f"Fitted Beta($\\alpha$={alpha:.2f}, $\\beta$={beta:.2f})\nKS D={d_stat:.3f}")

    ax.set_xlabel("Mutation ratio")
    ax.set_ylabel("Density")
    ax.set_title(f"Mutation ratio distribution vs. fitted Beta\n{args.report.name}")
    ax.legend()
    fig.tight_layout()

    if args.save:
        args.save.parent.mkdir(parents=True, exist_ok=True)
        fig.savefig(args.save, dpi=150)
        print(f"Saved to {args.save}")

    plt.show()


if __name__ == "__main__":
    main()
