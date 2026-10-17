#!/usr/bin/env python3
"""Two experiments on top of `compute_difficulty_score.py`'s PCA fit, both
read-only -- neither writes into `model_metadata.json` or changes the
official `difficulty_score`:

1. **Component sweep**: instead of only ever combining PC1+PC2, build the
   combined score from PC1 alone, then PC1+PC2, PC1+PC2+PC3, ... up to all
   11 components, and report the Spearman correlation against
   `difficulty_score_article` for each -- does agreement with the reference
   formula improve, worsen, or plateau as more axes of variation are added?
   PC1 is kept signed (every loading positive by construction, so "higher
   = bigger" is well-defined); every component beyond PC1 is folded in via
   its absolute value, same reasoning as `compute_difficulty_score.py`'s
   PC2 handling -- an eigenvector's sign is arbitrary whenever its loadings
   don't all share one sign, which holds for PC2..PC11 too, not just PC2.
   Each included component's point budget is variance-proportional among
   the included set (not a fixed share), same formula as the 2-component
   case, generalized.

2. **Unclamped variant**: the official score clips each component's raw
   projection to its 1st/99th percentile band *before* rescaling into its
   point budget, specifically so one extreme outlier model can't single-
   handedly stretch the 0-100 scale for everyone else. This re-runs the
   PC1+PC2 combination WITHOUT that clip -- same percentile-derived lo/hi
   bounds, but outliers beyond them now land below 0 or above their budget
   instead of being pinned to it -- to answer two things: how many models
   would that affect, and does removing the clip change rank agreement
   with the article formula (clipping creates ties at the boundary that
   could shift Spearman either way).

Excludes models with only `no_logic` methods (per `logic_validation_report.json`'s
`status == "no_logic"` -- the ~631 fully-empty-stub models), since those
describe no real structure to rank by difficulty at all. This is a
difference from the official `compute_difficulty_score.py`, which does not
apply this exclusion -- see `checklist.md` for why that's flagged as a gap
there, not here.

3. **Wider exclusion comparison**: the 631 fully-empty models above are a
   narrower set than the ~992 models that have zero `has_logic` methods
   but are NOT fully empty (they still have real, working `trivial`
   methods -- getters/setters -- just nothing with actual logic; counted
   by `classify_method_logic.py` among the already-usable 8,336 models,
   so this set doesn't overlap with the 631 at all). This experiment
   re-runs the official PC1+PC2 combination with BOTH exclusion sets
   (631-only vs. 631+992) and reports Spearman-vs-article plus basic score
   stats for each, to answer directly: does also excluding the
   logic-less-but-functioning models change anything.

Usage:
    python scripts/experiment_difficulty_score_pca.py [--dataset-dir PATH]
        [--reports-dir PATH] [--max-components N]
"""
from __future__ import annotations

import argparse
import datetime
import json
import sys
from pathlib import Path

import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parent))
from compute_difficulty_score import (  # noqa: E402
    FIELDS, METADATA_FILENAME, compute_pca, component_vector, project,
)
from compare_difficulty_scores import pearson, rankdata, spearman  # noqa: E402

LOGIC_VALIDATION_REPORT = "logic_validation_report.json"
METHOD_LOGIC_REPORT = "method_logic_classification_report.json"


def load_no_logic_only_models(reports_dir: Path) -> set[str]:
    path = reports_dir / LOGIC_VALIDATION_REPORT
    data = json.loads(path.read_text(encoding="utf-8"))
    return {r["model"] for r in data["results"] if r.get("status") == "no_logic"}


def load_zero_has_logic_models(reports_dir: Path) -> set[str]:
    """Models with zero has_logic-classified methods, per
    `classify_method_logic.py`'s dataset-wide run -- a DIFFERENT, disjoint
    set from `load_no_logic_only_models()`'s 631: that one is fully-empty
    stub models excluded before this classification ever ran; this one is
    drawn only from the already-usable 8,336, so none of the 631 appear
    here at all."""
    path = reports_dir / METHOD_LOGIC_REPORT
    data = json.loads(path.read_text(encoding="utf-8"))
    return {r["model"] for r in data["results"] if r["totals"].get("has_logic", 0) == 0}


def load_raw_matrix_excluding(dataset_dir: Path, excluded: set[str]) -> tuple[list[str], np.ndarray]:
    """Same as compute_difficulty_score.py's load_raw_matrix(), plus skipping
    any model in `excluded` -- kept as a separate function (not a flag on
    the original) so the official script's behavior is untouched."""
    models: list[str] = []
    rows: list[list[float]] = []
    for d in sorted(dataset_dir.iterdir(), key=lambda p: p.name):
        if d.name in excluded:
            continue
        p = d / METADATA_FILENAME
        if not p.is_file():
            continue
        try:
            data = json.loads(p.read_text(encoding="utf-8"))
        except json.JSONDecodeError:
            continue
        if data.get("status") != "measured":
            continue
        row = [float(data.get(f) or 0) for f in FIELDS]
        models.append(d.name)
        rows.append(row)
    return models, np.array(rows, dtype=np.float64)


def load_article_scores(dataset_dir: Path, models: list[str]) -> np.ndarray:
    scores = []
    for name in models:
        p = dataset_dir / name / METADATA_FILENAME
        data = json.loads(p.read_text(encoding="utf-8"))
        scores.append(float(data["difficulty_score_article"]))
    return np.array(scores, dtype=np.float64)


def rescale_clamped(raw_scores: np.ndarray, low_pct: float, high_pct: float, budget: float) -> np.ndarray:
    lo = float(np.percentile(raw_scores, low_pct))
    hi = float(np.percentile(raw_scores, high_pct))
    if hi == lo:
        return np.zeros_like(raw_scores)
    clipped = np.clip(raw_scores, lo, hi)
    return (clipped - lo) / (hi - lo) * budget


def rescale_unclamped(raw_scores: np.ndarray, low_pct: float, high_pct: float, budget: float) -> np.ndarray:
    """Same percentile-derived lo/hi as rescale_clamped(), but no np.clip --
    a model beyond the percentile band lands below 0 or above `budget`
    instead of being pinned to it."""
    lo = float(np.percentile(raw_scores, low_pct))
    hi = float(np.percentile(raw_scores, high_pct))
    if hi == lo:
        return np.zeros_like(raw_scores)
    return (raw_scores - lo) / (hi - lo) * budget


def combined_score_for_components(
    raw_matrix: np.ndarray, fit: dict, component_indices: list[int],
    low_pct: float, high_pct: float, scale_max: float, clamp: bool,
) -> np.ndarray:
    """PC1 (index 0) kept signed; every other included component folded in
    via |value| (arbitrary eigenvector sign otherwise -- same reasoning as
    the official script's PC2 handling, generalized to PC3..PC11). Each
    component's point budget is variance-proportional among exactly the
    included set."""
    variances = [fit["all_components"][i]["variance_explained"] for i in component_indices]
    total_variance = sum(variances)
    rescale_fn = rescale_clamped if clamp else rescale_unclamped

    total_points = np.zeros(raw_matrix.shape[0], dtype=np.float64)
    for i, variance in zip(component_indices, variances):
        vector = component_vector(fit, i)
        raw_scores = project(raw_matrix, fit, vector)
        if i != 0:
            raw_scores = np.abs(raw_scores)
        budget = scale_max * variance / total_variance
        total_points += rescale_fn(raw_scores, low_pct, high_pct, budget)
    return total_points


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--dataset-dir", type=Path, default=Path(__file__).resolve().parent.parent / "Dataset")
    parser.add_argument("--reports-dir", type=Path, default=Path(__file__).resolve().parent.parent / "reports")
    parser.add_argument("--low-percentile", type=float, default=1.0)
    parser.add_argument("--high-percentile", type=float, default=99.0)
    parser.add_argument("--scale-max", type=float, default=100.0)
    parser.add_argument("--max-components", type=int, default=11)
    args = parser.parse_args()

    excluded = load_no_logic_only_models(args.reports_dir)
    print(f"Excluding {len(excluded)} no_logic-only models (per {LOGIC_VALIDATION_REPORT})")

    models, raw_matrix = load_raw_matrix_excluding(args.dataset_dir, excluded)
    print(f"Loaded {len(models)} measured, non-excluded models")

    fit = compute_pca(raw_matrix)
    article_scores = load_article_scores(args.dataset_dir, models)

    n_components = min(args.max_components, len(fit["all_components"]))

    print("\n--- Experiment 1: component sweep (cumulative PC1..PCk, clamped) ---")
    sweep_results = []
    for k in range(1, n_components + 1):
        indices = list(range(k))
        combined = combined_score_for_components(
            raw_matrix, fit, indices, args.low_percentile, args.high_percentile, args.scale_max, clamp=True,
        )
        r_spearman = spearman(combined, article_scores)
        r_pearson = pearson(combined, article_scores)
        cumulative_variance = fit["all_components"][k - 1]["cumulative_variance_explained"]
        sweep_results.append({
            "components_included": k,
            "component_labels": [fit["all_components"][i]["component"] for i in indices],
            "cumulative_variance_explained": cumulative_variance,
            "spearman_vs_article": r_spearman,
            "pearson_vs_article": r_pearson,
            "score_min": float(combined.min()),
            "score_max": float(combined.max()),
        })
        print(f"  PC1..PC{k}: cum.variance={cumulative_variance*100:5.2f}%  "
              f"spearman={r_spearman:+.4f}  pearson={r_pearson:+.4f}  "
              f"range=[{combined.min():.2f}, {combined.max():.2f}]")

    print("\n--- Experiment 2: PC1+PC2, clamped vs. unclamped ---")
    official_indices = [0, 1]
    clamped = combined_score_for_components(
        raw_matrix, fit, official_indices, args.low_percentile, args.high_percentile, args.scale_max, clamp=True,
    )
    unclamped = combined_score_for_components(
        raw_matrix, fit, official_indices, args.low_percentile, args.high_percentile, args.scale_max, clamp=False,
    )
    r_spearman_clamped = spearman(clamped, article_scores)
    r_spearman_unclamped = spearman(unclamped, article_scores)
    frac = unclamped / args.scale_max
    over = frac > 1.0
    under = frac < 0.0
    n_over = int(over.sum())
    n_under = int(under.sum())
    print(f"  Clamped:   spearman={r_spearman_clamped:+.4f}  range=[{clamped.min():.2f}, {clamped.max():.2f}]")
    print(f"  Unclamped: spearman={r_spearman_unclamped:+.4f}  range=[{unclamped.min():.2f}, {unclamped.max():.2f}]")
    print(f"  Models exceeding the normal 0-{args.scale_max:.0f} cap (unclamped, as a fraction of scale): "
          f"{n_over} above 1.0, {n_under} below 0.0, out of {len(models)} "
          f"({(n_over + n_under) / len(models) * 100:.2f}% total)")

    over_models = sorted(
        ({"model": models[i], "unclamped_score": float(unclamped[i]), "fraction_of_scale": float(frac[i])}
         for i in np.where(over)[0]),
        key=lambda x: -x["fraction_of_scale"],
    )
    under_models = sorted(
        ({"model": models[i], "unclamped_score": float(unclamped[i]), "fraction_of_scale": float(frac[i])}
         for i in np.where(under)[0]),
        key=lambda x: x["fraction_of_scale"],
    )

    print("\n--- Experiment 3: narrower (631) vs wider (631+992) exclusion, PC1+PC2 ---")
    zero_has_logic = load_zero_has_logic_models(args.reports_dir)
    wider_excluded = excluded | zero_has_logic
    print(f"  Narrower: {len(excluded)} excluded (fully-empty stub models only)")
    print(f"  Wider: {len(wider_excluded)} excluded (+{len(zero_has_logic)} zero-has_logic-but-functioning models)")

    models_wide, raw_matrix_wide = load_raw_matrix_excluding(args.dataset_dir, wider_excluded)
    fit_wide = compute_pca(raw_matrix_wide)
    article_scores_wide = load_article_scores(args.dataset_dir, models_wide)
    combined_wide = combined_score_for_components(
        raw_matrix_wide, fit_wide, [0, 1], args.low_percentile, args.high_percentile, args.scale_max, clamp=True,
    )
    r_spearman_wide = spearman(combined_wide, article_scores_wide)

    narrower_stats = {
        "models_used": len(models), "spearman_vs_article": r_spearman_clamped,
        "mean": float(clamped.mean()), "median": float(np.median(clamped)),
        "min": float(clamped.min()), "max": float(clamped.max()),
    }
    wider_stats = {
        "models_used": len(models_wide), "spearman_vs_article": r_spearman_wide,
        "mean": float(combined_wide.mean()), "median": float(np.median(combined_wide)),
        "min": float(combined_wide.min()), "max": float(combined_wide.max()),
    }
    print(f"  Narrower (n={narrower_stats['models_used']}): spearman={narrower_stats['spearman_vs_article']:+.4f}  "
          f"mean={narrower_stats['mean']:.2f}  median={narrower_stats['median']:.2f}")
    print(f"  Wider    (n={wider_stats['models_used']}): spearman={wider_stats['spearman_vs_article']:+.4f}  "
          f"mean={wider_stats['mean']:.2f}  median={wider_stats['median']:.2f}")

    report = {
        "generated_at": datetime.datetime.now(datetime.timezone.utc).isoformat(),
        "models_used": len(models),
        "models_excluded_no_logic_only": len(excluded),
        "wider_exclusion_experiment": {
            "zero_has_logic_models_count": len(zero_has_logic),
            "narrower_exclusion": narrower_stats,
            "wider_exclusion": wider_stats,
        },
        "rescale_low_percentile": args.low_percentile,
        "rescale_high_percentile": args.high_percentile,
        "scale_max": args.scale_max,
        "component_sweep": sweep_results,
        "unclamped_experiment": {
            "spearman_clamped_vs_article": r_spearman_clamped,
            "spearman_unclamped_vs_article": r_spearman_unclamped,
            "spearman_delta": r_spearman_unclamped - r_spearman_clamped,
            "clamped_score_min": float(clamped.min()),
            "clamped_score_max": float(clamped.max()),
            "unclamped_score_min": float(unclamped.min()),
            "unclamped_score_max": float(unclamped.max()),
            "models_over_cap_count": n_over,
            "models_under_cap_count": n_under,
            "models_over_cap_pct": round(n_over / len(models) * 100, 4),
            "models_under_cap_pct": round(n_under / len(models) * 100, 4),
            "models_over_cap": over_models,
            "models_under_cap": under_models,
        },
    }
    args.reports_dir.mkdir(parents=True, exist_ok=True)
    report_path = args.reports_dir / "difficulty_score_pca_experiment_report.json"
    report_path.write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")
    print(f"\nReport written to {report_path}")


if __name__ == "__main__":
    main()
