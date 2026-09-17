#!/usr/bin/env python3
"""One-off diagnostic: what do models at the extreme ends of PC2 actually
look like? Answers the question raised while designing the difficulty
score -- does a strongly negative PC2 represent a genuinely different KIND
of structural complexity (hierarchy/composition-heavy), or is it just
small/sparse models drifting negative because they're below-average on
PC2's larger-magnitude positive-loading fields (attribute_type_diversity,
attributes, associations, enumerations) without having much of the
negative-loading ones (generalizations, abstract_classes, composition)
either?

For the top and bottom N models by raw PC2 score, prints their raw PC1
score (a proxy for "how big/complex overall") and every one of the 11 raw
field values, so the two groups can be compared directly rather than
argued about abstractly.

Read-only: does not write anything, including no changes to
model_metadata.json or any report file -- pure console output.

Usage:
    python scripts/diagnose_pc2_extremes.py [--dataset-dir PATH] [--top-n N]
"""
from __future__ import annotations

import argparse
import sys
from pathlib import Path

import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parent))
import compute_difficulty_score as cds  # noqa: E402


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--dataset-dir", type=Path, default=Path(__file__).resolve().parent.parent / "Dataset")
    parser.add_argument("--top-n", type=int, default=10)
    args = parser.parse_args()

    print(f"Loading structural counts for fields: {cds.FIELDS}")
    models, raw_matrix = cds.load_raw_matrix(args.dataset_dir)
    print(f"Loaded {len(models)} measured models\n")

    fit = cds.compute_pca(raw_matrix)
    log_matrix = np.log1p(raw_matrix)
    standardized = (log_matrix - fit["_means_vector"]) / fit["_stds_vector"]

    pc1_vec = fit["_pc1_vector"]
    pc2_component = fit["all_components"][1]
    pc2_vec = np.array([pc2_component["loadings"][f] for f in cds.FIELDS])

    pc1_scores = standardized @ pc1_vec
    pc2_scores = standardized @ pc2_vec

    print(f"PC2 variance explained: {pc2_component['variance_explained']*100:.2f}%")
    print(f"PC2 loadings: {pc2_component['loadings']}\n")

    order = np.argsort(pc2_scores)
    bottom_idx = order[: args.top_n]   # most negative PC2
    top_idx = order[-args.top_n:][::-1]  # most positive PC2

    def show_group(label, idx_list):
        print(f"\n=== {label} ===")
        print(f"{'model':20} {'PC1':>8} {'PC2':>8}  " + "  ".join(f"{f:>10}" for f in cds.FIELDS))
        for i in idx_list:
            row_vals = "  ".join(f"{raw_matrix[i][j]:10.0f}" for j in range(len(cds.FIELDS)))
            print(f"{models[i]:20} {pc1_scores[i]:8.3f} {pc2_scores[i]:8.3f}  {row_vals}")
        print(f"-- group averages --")
        print(f"{'(avg)':20} {pc1_scores[idx_list].mean():8.3f} {pc2_scores[idx_list].mean():8.3f}  "
              + "  ".join(f"{raw_matrix[idx_list, j].mean():10.2f}" for j in range(len(cds.FIELDS))))

    show_group(f"Bottom {args.top_n} by PC2 (most negative)", bottom_idx)
    show_group(f"Top {args.top_n} by PC2 (most positive)", top_idx)

    # The actual question: does the negative-PC2 group also skew low on PC1
    # (i.e. are they just small/sparse models), or are they substantial on
    # PC1 too (genuinely large, just differently-shaped)?
    print(f"\n=== Summary: is negative PC2 just 'small models', or a real different shape? ===")
    print(f"Overall PC1 mean/std across all models: {pc1_scores.mean():.3f} / {pc1_scores.std():.3f}")
    print(f"Bottom-{args.top_n}-by-PC2 group's PC1 mean: {pc1_scores[bottom_idx].mean():.3f}")
    print(f"Top-{args.top_n}-by-PC2 group's PC1 mean: {pc1_scores[top_idx].mean():.3f}")

    # Broader check, not just the extreme N: correlation between PC1 and PC2
    # across ALL models -- if strongly negative, low-PC1 (small) models
    # systematically have high positive PC2, meaning very negative PC2 is
    # NOT simply "small models" (small models would cluster near positive
    # PC2 in that case, not negative) -- if near zero or positive, no such
    # relationship, and the extreme-group averages above are the real signal.
    corr = float(np.corrcoef(pc1_scores, pc2_scores)[0, 1])
    print(f"\nCorrelation(PC1, PC2) across all {len(models)} models: {corr:+.4f}")
    print("(PC1/PC2 are orthogonal BY CONSTRUCTION over the full dataset, so this "
          "should be ~0 regardless -- the extreme-group comparison above is the "
          "real answer to whether small models specifically drift negative.)")


if __name__ == "__main__":
    main()
