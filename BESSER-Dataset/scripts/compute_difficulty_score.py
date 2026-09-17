#!/usr/bin/env python3
"""Compute a per-model structural difficulty score via PCA over
`model_metadata.json`'s structural counts, and write it into each model's
`model_metadata.json`.

Methodology (see docs/DECISIONS.md for the full discussion this implements):

1. **Variables**: 11 of `model_metadata.json`'s 14 structural fields --
   `classes`, `attributes`, `associations`, `composition`, `generalizations`,
   `abstract_classes`, `enumerations`, `enumeration_literals`, `methods`,
   `many_valued_association_ends`, `attribute_type_diversity`. The other 3
   (`association_classes`, `abstract_methods`, `aggregation`) are confirmed
   true constants (std=0) across all 9,082 models -- not a judgment call
   that they're "irrelevant", a hard requirement, since standardizing a
   true constant divides by zero. Every included field has genuine variance
   and is weighted by PCA itself, not hand-picked. (Inheritance depth was
   also considered and dropped -- confirmed near-degenerate, not a true
   constant but 99.9% of models fall into just two of its three observed
   values, essentially redundant with `generalizations`.)
2. **Log1p transform** on every raw count before standardizing -- dampens
   the influence of this dataset's extreme outliers (a few "UML describing
   itself" meta-models with thousands of classes vs. a median of roughly a
   dozen) while preserving relative ordering all the way through the
   extremes, unlike percentile clipping applied at this stage.
3. **Standardize** (z-score) each log-transformed column across the full
   measured dataset (not just `usable_models.txt` -- this score describes
   the *diagram's* structural complexity, independent of whether the
   generated code/tests happen to work, so models excluded from test
   validation for unrelated reasons still get a real score here).
4. **PCA**: eigendecompose the resulting correlation matrix
   (`numpy.linalg.eigh`, deterministic for a real symmetric matrix -- no
   randomness anywhere in this pipeline). The first principal component's
   loadings are the weights; no one hand-picks A/B/C/D. PCA's sign is
   arbitrary, so it's fixed deterministically here: loadings are flipped if
   their sum is negative, so higher score always means more complex.
5. **Two components combined, not just PC1.** PC1 alone (48.54% variance
   explained) only captures "how much structure overall" -- PC2 (14.80%) is
   a real, different axis: a *contrast* between data-schema-heavy models
   (high `attribute_type_diversity`/`attributes`) and hierarchy-heavy ones
   (high `generalizations`/`abstract_classes`/`composition`), not a
   magnitude. Verified empirically (not assumed) that this axis reflects a
   real second kind of complexity, not just size, before including it:
   checked the models at both extremes of PC2 and confirmed both groups
   score *above* the dataset's average PC1 (0.732 and 1.398 vs. an overall
   mean of 0.000) -- i.e. both a "189-class, 157-generalization,
   zero-attribute" model and a "58-class, 79-attribute, zero-generalization"
   model are genuinely large, just built in opposite architectural styles.
   Neither extreme is a small/trivial model drifting there by default.
6. **PC2 is folded in via its absolute value, not its signed value --
   this is a hard requirement, not a style choice.** An eigenvector's sign
   is mathematically arbitrary (undefined up to a flip) whenever its
   loadings don't all share one sign, which is exactly PC2's case (unlike
   PC1, where every loading being positive means either valid sign choice
   gives the same real-world meaning: "more = more"). Using signed PC2
   directly -- or any monotonic shift of it -- would make the final score
   depend on which arbitrary sign convention this code happens to apply,
   with zero connection to the actual models: flip the sign-fixing rule's
   `<` to `>` and every model currently rewarded by PC2 would instead be
   penalized, and vice versa, though nothing about any model changed.
   `|PC2|` (and only a symmetric function like it) is invariant to that
   arbitrary choice, which is why it's the only sound option here -- it
   reads as "how far this model sits from a balanced blend of the two
   styles, in either direction," never "which style is harder."
7. **Weights are variance-proportional between PC1 and PC2**, not an
   arbitrary split (e.g. not a flat 50/50): PC1 gets
   `scale_max * var(PC1) / (var(PC1) + var(PC2))` points and PC2 gets the
   rest -- roughly 76.6/23.4 for a scale_max of 100, computed from the
   actual eigenvalues each run, never hardcoded, so the split reflects how
   much of the dataset's real variation each axis actually accounts for.
8. **Each component rescaled independently** to its own point budget via
   percentile clipping (1st/99th by default) then linear min-max -- PC1's
   raw (signed) scores for its budget, `|PC2|`'s (always non-negative)
   scores for its budget. The two point totals are summed for the final
   score, which is bounded to [0, scale_max] by construction (each addend
   is already clipped to its own non-negative sub-range).

Writes `difficulty_score` (0-100, the final bounded PC1+PC2 combined score),
plus `difficulty_score_pc1_points`/`difficulty_score_pc2_points` (each
component's own contribution, for transparency -- e.g. "this model's
difficulty comes mostly from size, or mostly from structural
distinctiveness"), and the unbounded, *signed* raw projections
`difficulty_score_pc1_raw`/`difficulty_score_pc2_raw` (signed, even though
only `|PC2 raw|` feeds the score -- the sign tells you *which* style a
model leans toward, useful context the final number alone doesn't carry)
into every measured model's `model_metadata.json`. Also writes a reference
report (`reports/difficulty_score_report.json`) with the exact loadings for
every component, per-field log1p means/stds, and variance explained, so the
same formula can be reproduced or applied to a new model without
recomputing PCA from scratch.

Usage:
    python scripts/compute_difficulty_score.py [--dataset-dir PATH]
        [--reports-dir PATH] [--low-percentile P] [--high-percentile P]
        [--scale-max N] [--dry-run]
"""
from __future__ import annotations

import argparse
import datetime
import json
from pathlib import Path

import numpy as np

FIELDS = [
    "classes", "attributes", "associations", "composition", "generalizations",
    "abstract_classes", "enumerations", "enumeration_literals", "methods",
    "many_valued_association_ends", "attribute_type_diversity",
]
EXCLUDED_CONSTANT_FIELDS = ["association_classes", "abstract_methods", "aggregation"]
# Considered and dropped: inheritance depth -- confirmed near-degenerate
# (4,700/9,082 models at depth 0, 4,373 at depth 1, only 9 ever reaching
# depth 2), essentially redundant with `generalizations`. See
# docs/DECISIONS.md, 2026-09-17 entry.
METADATA_FILENAME = "model_metadata.json"


def load_raw_matrix(dataset_dir: Path) -> tuple[list[str], np.ndarray]:
    """Every measured model's raw FIELDS values, in a stable (sorted-by-name)
    order -- determinism requires a fixed row order, not directory-listing
    order (which some filesystems don't guarantee is stable)."""
    models: list[str] = []
    rows: list[list[float]] = []
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
        row = [float(data.get(f) or 0) for f in FIELDS]
        models.append(d.name)
        rows.append(row)
    return models, np.array(rows, dtype=np.float64)


def compute_pca(raw_matrix: np.ndarray) -> dict:
    """Returns the fitted transform: log1p means/stds, PC1 loadings, and
    diagnostics (variance explained, all eigenvalues) -- everything needed
    to reproduce the raw score for any model without redoing PCA."""
    log_matrix = np.log1p(raw_matrix)
    means = log_matrix.mean(axis=0)
    stds = log_matrix.std(axis=0, ddof=0)
    if np.any(stds == 0):
        zero_fields = [f for f, s in zip(FIELDS, stds) if s == 0]
        raise ValueError(
            f"Field(s) {zero_fields} have zero variance in this dataset (even "
            f"after log1p) -- PCA standardization would divide by zero. Remove "
            f"them from FIELDS before running."
        )
    standardized = (log_matrix - means) / stds

    corr = np.corrcoef(standardized, rowvar=False)
    eigenvalues, eigenvectors = np.linalg.eigh(corr)  # ascending order, deterministic
    order = np.argsort(eigenvalues)[::-1]
    eigenvalues = eigenvalues[order]
    eigenvectors = eigenvectors[:, order]

    pc1 = eigenvectors[:, 0].copy()
    if pc1.sum() < 0:  # deterministic sign convention: higher score = more complex
        pc1 = -pc1

    # Full component breakdown (PC1..PCn), not just PC1 -- so a single run
    # shows the complete picture (what each axis of variation looks like,
    # not just the dominant one) rather than needing a separate ad-hoc pass
    # per component. Sign-fixed the same way as PC1 for readability, though
    # for anything past PC1 "higher = harder" isn't implied by the sign.
    all_components = []
    total_var = eigenvalues.sum()
    for i in range(len(eigenvalues)):
        vec = eigenvectors[:, i].copy()
        if vec.sum() < 0:
            vec = -vec
        all_components.append({
            "component": f"PC{i+1}",
            "variance_explained": float(eigenvalues[i] / total_var),
            "cumulative_variance_explained": float(eigenvalues[: i + 1].sum() / total_var),
            "loadings": dict(zip(FIELDS, vec.tolist())),
        })

    variance_explained = float(eigenvalues[0] / eigenvalues.sum())
    return {
        "pc1_loadings": dict(zip(FIELDS, pc1.tolist())),
        "log1p_means": dict(zip(FIELDS, means.tolist())),
        "log1p_stds": dict(zip(FIELDS, stds.tolist())),
        "variance_explained_by_pc1": variance_explained,
        "all_eigenvalues": eigenvalues.tolist(),
        "all_components": all_components,
        "_pc1_vector": pc1,
        "_means_vector": means,
        "_stds_vector": stds,
    }


def component_vector(fit: dict, index: int) -> np.ndarray:
    """The loadings for the component at `index` (0 = PC1, 1 = PC2, ...) as
    a plain array in FIELDS order."""
    return np.array([fit["all_components"][index]["loadings"][f] for f in FIELDS])


def project(raw_matrix: np.ndarray, fit: dict, vector: np.ndarray) -> np.ndarray:
    """Every model's raw (signed, unbounded) score on the component defined
    by `vector` -- same log1p+standardize transform regardless of which
    component, since standardization is fit once on the whole dataset, not
    per-component."""
    log_matrix = np.log1p(raw_matrix)
    standardized = (log_matrix - fit["_means_vector"]) / fit["_stds_vector"]
    return standardized @ vector


def rescale(raw_scores: np.ndarray, low_pct: float, high_pct: float, scale_max: float) -> tuple[np.ndarray, float, float]:
    lo = float(np.percentile(raw_scores, low_pct))
    hi = float(np.percentile(raw_scores, high_pct))
    if hi == lo:
        return np.zeros_like(raw_scores), lo, hi
    clipped = np.clip(raw_scores, lo, hi)
    scaled = (clipped - lo) / (hi - lo) * scale_max
    return scaled, lo, hi


def compute_combined_score(
    pc1_scores: np.ndarray, pc2_scores: np.ndarray,
    pc1_variance: float, pc2_variance: float,
    low_pct: float, high_pct: float, scale_max: float,
) -> dict:
    """PC1 (signed, "how big") + |PC2| (unsigned, "how far from a balanced
    blend of styles") combined into one 0-scale_max score, each weighted by
    its own share of the variance the two together explain -- see the
    module docstring (points 5-8) for why PC2 must be unsigned and why the
    weights are variance-proportional, not an arbitrary split."""
    total_variance = pc1_variance + pc2_variance
    pc1_budget = scale_max * pc1_variance / total_variance
    pc2_budget = scale_max * pc2_variance / total_variance

    pc1_points, pc1_lo, pc1_hi = rescale(pc1_scores, low_pct, high_pct, pc1_budget)
    pc2_abs_scores = np.abs(pc2_scores)
    pc2_points, pc2_lo, pc2_hi = rescale(pc2_abs_scores, low_pct, high_pct, pc2_budget)

    return {
        "combined_score": pc1_points + pc2_points,
        "pc1_points": pc1_points,
        "pc2_points": pc2_points,
        "pc1_budget": pc1_budget,
        "pc2_budget": pc2_budget,
        "pc1_clip_bounds": (pc1_lo, pc1_hi),
        "pc2_abs_clip_bounds": (pc2_lo, pc2_hi),
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--dataset-dir", type=Path, default=Path(__file__).resolve().parent.parent / "Dataset")
    parser.add_argument("--reports-dir", type=Path, default=Path(__file__).resolve().parent.parent / "reports")
    parser.add_argument("--low-percentile", type=float, default=1.0)
    parser.add_argument("--high-percentile", type=float, default=99.0)
    parser.add_argument("--scale-max", type=float, default=100.0)
    parser.add_argument("--dry-run", action="store_true",
                         help="Compute and report everything, but don't write into model_metadata.json files")
    args = parser.parse_args()

    print(f"Loading structural counts for fields: {FIELDS}")
    models, raw_matrix = load_raw_matrix(args.dataset_dir)
    print(f"Loaded {len(models)} measured models")

    fit = compute_pca(raw_matrix)

    print("\nVariance explained by each component:")
    for comp in fit["all_components"]:
        print(f"  {comp['component']}: {comp['variance_explained']*100:5.2f}%  "
              f"(cumulative: {comp['cumulative_variance_explained']*100:5.2f}%)")

    print("\nLoadings by component (rows=fields, cols=PC1..PCn):")
    header = "  " + f"{'field':24}" + "".join(f"{c['component']:>9}" for c in fit["all_components"])
    print(header)
    for field in FIELDS:
        row = "  " + f"{field:24}" + "".join(f"{c['loadings'][field]:+9.4f}" for c in fit["all_components"])
        print(row)

    pc1_scores = project(raw_matrix, fit, fit["_pc1_vector"])
    pc2_vector = component_vector(fit, 1)
    pc2_scores = project(raw_matrix, fit, pc2_vector)
    pc1_variance = fit["all_components"][0]["variance_explained"]
    pc2_variance = fit["all_components"][1]["variance_explained"]

    combo = compute_combined_score(
        pc1_scores, pc2_scores, pc1_variance, pc2_variance,
        args.low_percentile, args.high_percentile, args.scale_max,
    )
    combined_scores = combo["combined_score"]

    print(f"\nPC1/PC2 point budgets (variance-proportional, out of scale_max={args.scale_max}):")
    print(f"  PC1 (\"how big\"):                {combo['pc1_budget']:.4f} points "
          f"(variance share {pc1_variance/(pc1_variance+pc2_variance)*100:.2f}%)")
    print(f"  PC2 (\"how far from balanced style\"): {combo['pc2_budget']:.4f} points "
          f"(variance share {pc2_variance/(pc1_variance+pc2_variance)*100:.2f}%)")
    print(f"\nPC1 raw score range: [{pc1_scores.min():.4f}, {pc1_scores.max():.4f}]"
          f"  clip bounds: {combo['pc1_clip_bounds']}")
    print(f"|PC2| raw score range: [{np.abs(pc2_scores).min():.4f}, {np.abs(pc2_scores).max():.4f}]"
          f"  clip bounds: {combo['pc2_abs_clip_bounds']}")
    print(f"\nCombined final score range: [{combined_scores.min()}, {combined_scores.max()}] "
          f"(scale 0-{args.scale_max})")

    if not args.dry_run:
        written = 0
        for i, name in enumerate(models):
            path = args.dataset_dir / name / METADATA_FILENAME
            try:
                data = json.loads(path.read_text(encoding="utf-8"))
            except (OSError, json.JSONDecodeError):
                continue
            # Kept at full float precision, deliberately not rounded.
            data["difficulty_score"] = float(combined_scores[i])
            data["difficulty_score_pc1_points"] = float(combo["pc1_points"][i])
            data["difficulty_score_pc2_points"] = float(combo["pc2_points"][i])
            data["difficulty_score_pc1_raw"] = float(pc1_scores[i])
            data["difficulty_score_pc2_raw"] = float(pc2_scores[i])
            path.write_text(json.dumps(data, indent=2) + "\n", encoding="utf-8")
            written += 1
        print(f"\nWrote difficulty_score into {written}/{len(models)} models' model_metadata.json")
    else:
        print("\n--dry-run: nothing written to model_metadata.json files")

    report = {
        "generated_at": datetime.datetime.now(datetime.timezone.utc).isoformat(),
        "fields_used": FIELDS,
        "fields_excluded_true_constants": EXCLUDED_CONSTANT_FIELDS,
        "models_used_for_pca": len(models),
        "all_components": fit["all_components"],
        "log1p_means": fit["log1p_means"],
        "log1p_stds": fit["log1p_stds"],
        "pc1_variance_explained": pc1_variance,
        "pc2_variance_explained": pc2_variance,
        "pc1_budget": combo["pc1_budget"],
        "pc2_budget": combo["pc2_budget"],
        "pc1_clip_bounds_raw": list(combo["pc1_clip_bounds"]),
        "pc2_abs_clip_bounds_raw": list(combo["pc2_abs_clip_bounds"]),
        "rescale_low_percentile": args.low_percentile,
        "rescale_high_percentile": args.high_percentile,
        "scale_max": args.scale_max,
        "pc1_raw_score_min": float(pc1_scores.min()),
        "pc1_raw_score_max": float(pc1_scores.max()),
        "pc2_raw_score_min": float(pc2_scores.min()),
        "pc2_raw_score_max": float(pc2_scores.max()),
        "final_score_min": float(combined_scores.min()),
        "final_score_max": float(combined_scores.max()),
        "dry_run": args.dry_run,
    }
    args.reports_dir.mkdir(parents=True, exist_ok=True)
    report_path = args.reports_dir / "difficulty_score_report.json"
    report_path.write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")
    print(f"Report written to {report_path}")


if __name__ == "__main__":
    main()
