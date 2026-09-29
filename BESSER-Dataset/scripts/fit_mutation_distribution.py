#!/usr/bin/env python3
"""Fit a continuous probability distribution to this dataset's per-model
mutation ratio (mutation score), and report goodness of fit.

Why Beta(alpha, beta): mutation ratio is bounded to [0, 1] by definition
(killed/run), which already rules out unbounded distributions (normal,
exponential, ...) as a faithful model -- Beta is the standard continuous
distribution with support exactly [0, 1]. This dataset's mutation-score
distribution is also known to be bimodal (see reports/summary_report.md:
"a large mass near 0%... and a second mass near 100%... comparatively
little in between") -- a Beta distribution is U-shaped (mass piled at both
boundaries) exactly when both alpha < 1 and beta < 1, which is the shape
to expect fitting this data, not a coincidence-hunting choice.

Fit method: method of moments (closed-form from the sample mean/variance),
not MLE -- this project has no scipy installed, and MLE for Beta requires
solving a digamma-based equation numerically (needs scipy.special.digamma
or an equivalent root-finder). Method of moments is a standard, valid,
fully deterministic closed-form alternative:
    common = mean*(1-mean)/variance - 1
    alpha  = mean * common
    beta   = (1-mean) * common
(Undefined / not a valid Beta fit if variance >= mean*(1-mean); the script
reports this explicitly rather than silently producing nonsense parameters.)

Goodness of fit: a Kolmogorov-Smirnov style statistic (max absolute gap
between the empirical CDF and the fitted Beta's CDF), computed without
scipy via a self-contained regularized incomplete beta function
(continued-fraction method, the standard non-scipy way to compute it --
see `regularized_incomplete_beta()` below). Smaller D = better fit;
there's no scipy.stats.kstest p-value here (that needs the KS
distribution's CDF, a separate special function), but D itself is a
standard, interpretable, comparable-across-fits number.

Usage:
    python scripts/fit_mutation_distribution.py --report PATH
        [--score-field mutation_score] [--reports-dir PATH]
"""
from __future__ import annotations

import argparse
import json
import math
from pathlib import Path

import numpy as np


def load_scores(report_path: Path, score_field: str) -> np.ndarray:
    data = json.loads(report_path.read_text(encoding="utf-8"))
    results = data.get("results")
    if results is None:
        raise ValueError(f"{report_path} has no top-level 'results' list -- wrong report file?")
    scores = [r[score_field] for r in results if r.get(score_field) is not None]
    if not scores:
        raise ValueError(f"No non-null '{score_field}' values found in {report_path}")
    return np.array(scores, dtype=np.float64)


def fit_beta_method_of_moments(scores: np.ndarray) -> tuple[float, float]:
    mean = float(scores.mean())
    var = float(scores.var(ddof=0))
    max_var = mean * (1.0 - mean)
    if var >= max_var:
        raise ValueError(
            f"Sample variance ({var:.6f}) >= mean*(1-mean) ({max_var:.6f}) -- "
            f"no valid Beta distribution has this mean and variance (Beta's "
            f"variance is always < mean*(1-mean)). The data is more spread "
            f"out than any Beta shape can represent; a Beta fit is not "
            f"appropriate for this sample."
        )
    common = mean * (1.0 - mean) / var - 1.0
    alpha = mean * common
    beta = (1.0 - mean) * common
    return alpha, beta


def log_beta_function(a: float, b: float) -> float:
    """log(B(a, b)) via lgamma, for numerically stable PDF evaluation
    (B(a,b) itself can be astronomically small/large for the alpha/beta
    values this data tends to produce)."""
    return math.lgamma(a) + math.lgamma(b) - math.lgamma(a + b)


def beta_pdf(x: np.ndarray, a: float, b: float) -> np.ndarray:
    log_norm = -log_beta_function(a, b)
    with np.errstate(divide="ignore"):
        log_pdf = log_norm + (a - 1.0) * np.log(x) + (b - 1.0) * np.log1p(-x)
    return np.exp(log_pdf)


def _betacf(x: float, a: float, b: float, max_iter: int = 200, eps: float = 1e-12) -> float:
    """Continued-fraction evaluation for the incomplete beta function,
    the standard algorithm (Numerical Recipes' betacf) for computing the
    regularized incomplete beta function without scipy."""
    qab = a + b
    qap = a + 1.0
    qam = a - 1.0
    c = 1.0
    d = 1.0 - qab * x / qap
    if abs(d) < eps:
        d = eps
    d = 1.0 / d
    h = d
    for m in range(1, max_iter + 1):
        m2 = 2 * m
        aa = m * (b - m) * x / ((qam + m2) * (a + m2))
        d = 1.0 + aa * d
        if abs(d) < eps:
            d = eps
        c = 1.0 + aa / c
        if abs(c) < eps:
            c = eps
        d = 1.0 / d
        h *= d * c
        aa = -(a + m) * (qab + m) * x / ((a + m2) * (qap + m2))
        d = 1.0 + aa * d
        if abs(d) < eps:
            d = eps
        c = 1.0 + aa / c
        if abs(c) < eps:
            c = eps
        d = 1.0 / d
        delta = d * c
        h *= delta
        if abs(delta - 1.0) < eps:
            break
    return h


def regularized_incomplete_beta(x: float, a: float, b: float) -> float:
    """I_x(a, b) -- the Beta(a, b) CDF at x. Pure-Python continued-fraction
    implementation (no scipy). x must be in [0, 1]."""
    if x <= 0.0:
        return 0.0
    if x >= 1.0:
        return 1.0
    log_front = a * math.log(x) + b * math.log1p(-x) - log_beta_function(a, b)
    front = math.exp(log_front)
    if x < (a + 1.0) / (a + b + 2.0):
        return front * _betacf(x, a, b) / a
    return 1.0 - front * _betacf(1.0 - x, b, a) / b


def ks_statistic_vs_beta(scores: np.ndarray, alpha: float, beta: float) -> float:
    """Kolmogorov-Smirnov D statistic: max gap between the empirical CDF
    and the fitted Beta's CDF, evaluated at every data point (the only
    points where the empirical CDF can jump, so the max is exact there)."""
    sorted_scores = np.sort(scores)
    n = len(sorted_scores)
    empirical_upper = np.arange(1, n + 1) / n
    empirical_lower = np.arange(0, n) / n
    fitted = np.array([regularized_incomplete_beta(x, alpha, beta) for x in sorted_scores])
    gaps = np.maximum(np.abs(fitted - empirical_upper), np.abs(fitted - empirical_lower))
    return float(gaps.max())


def sample_beta(alpha: float, beta: float, n: int, seed: int) -> np.ndarray:
    """Draw n samples from the fitted Beta(alpha, beta) -- numpy's own Beta
    sampler, seeded for determinism/reproducibility."""
    rng = np.random.default_rng(seed)
    return rng.beta(alpha, beta, size=n)


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--report", type=Path, required=True,
                         help="Path to a mutation report JSON with a top-level 'results' list "
                              "(e.g. reports/mutation_full_dataset_report.json or "
                              "reports/combined_mutation_properties_report_final.json)")
    parser.add_argument("--score-field", default="mutation_score")
    parser.add_argument("--reports-dir", type=Path, default=Path(__file__).resolve().parent.parent / "reports")
    parser.add_argument("--sample-n", type=int, default=0,
                         help="If >0, also draw this many samples from the fitted distribution "
                              "and print their mean/variance as a sanity check")
    parser.add_argument("--seed", type=int, default=42)
    args = parser.parse_args()

    scores = load_scores(args.report, args.score_field)
    print(f"Loaded {len(scores)} mutation scores from {args.report}")
    print(f"Sample mean: {scores.mean():.6f}   Sample variance: {scores.var(ddof=0):.6f}")
    print(f"Sample min/max: [{scores.min():.6f}, {scores.max():.6f}]")

    alpha, beta = fit_beta_method_of_moments(scores)
    print(f"\nFitted Beta(alpha={alpha:.4f}, beta={beta:.4f})")
    print(f"  Shape: {'U-shaped (bimodal, mass at both ends)' if alpha < 1 and beta < 1 else 'unimodal' if alpha > 1 and beta > 1 else 'monotonic (mass concentrated at one end)'}")

    beta_mean = alpha / (alpha + beta)
    beta_var = (alpha * beta) / ((alpha + beta) ** 2 * (alpha + beta + 1))
    print(f"  Theoretical mean/variance of this fit: {beta_mean:.6f} / {beta_var:.6f} "
          f"(sanity check against sample: {scores.mean():.6f} / {scores.var(ddof=0):.6f})")

    d_stat = ks_statistic_vs_beta(scores, alpha, beta)
    print(f"\nKolmogorov-Smirnov D statistic vs. fitted Beta: {d_stat:.6f}")
    print("  (smaller = better fit; D is the max gap between the empirical and fitted CDFs)")

    print(f"\nPDF (paste-ready): f(x) = x^{alpha:.4f}-1 * (1-x)^{beta:.4f}-1 / B({alpha:.4f}, {beta:.4f})")
    print(f"  where B(a,b) = exp(lgamma(a) + lgamma(b) - lgamma(a+b)) = "
          f"{math.exp(log_beta_function(alpha, beta)):.6e}")

    result = {
        "report_source": str(args.report),
        "score_field": args.score_field,
        "n": len(scores),
        "sample_mean": float(scores.mean()),
        "sample_variance": float(scores.var(ddof=0)),
        "sample_min": float(scores.min()),
        "sample_max": float(scores.max()),
        "fit_method": "method_of_moments",
        "beta_alpha": alpha,
        "beta_beta": beta,
        "beta_theoretical_mean": beta_mean,
        "beta_theoretical_variance": beta_var,
        "ks_statistic": d_stat,
    }

    if args.sample_n > 0:
        drawn = sample_beta(alpha, beta, args.sample_n, args.seed)
        print(f"\n{args.sample_n} samples drawn from the fitted distribution (seed={args.seed}):")
        print(f"  mean={drawn.mean():.6f}  variance={drawn.var(ddof=0):.6f}")
        result["sample_draw_n"] = args.sample_n
        result["sample_draw_seed"] = args.seed
        result["sample_draw_mean"] = float(drawn.mean())
        result["sample_draw_variance"] = float(drawn.var(ddof=0))

    args.reports_dir.mkdir(parents=True, exist_ok=True)
    out_path = args.reports_dir / "mutation_ratio_distribution_report.json"
    out_path.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(f"\nReport written to {out_path}")


if __name__ == "__main__":
    main()
