#!/usr/bin/env python3
"""The evidence behind the PCA difficulty score's design: how it compares to
the reference paper's `difficulty_score_article`, and why only PC1+PC2 are
used. Read-only -- never writes into `model_metadata.json` or changes the
official `difficulty_score`. Fits the same PCA as `compute_difficulty_score.py`
on the same model set (pass the same `--models-file` to both).

1. **Component retention**: how many components the standard rules keep --
   Kaiser (eigenvalue > 1), the broken-stick model, and Horn's parallel
   analysis (keep a component only while its eigenvalue beats the 95th
   percentile of the same PCA on random normal data of identical shape,
   `--parallel-iterations` runs, fixed `--seed`). Also the scree drops.
2. **Component sweep**: the combined score built from PC1 alone, PC1+PC2, ...
   up to all components, each compared to the article score (Spearman and
   Pearson). PC1 is kept signed; every later component enters as |value|
   (its eigenvector sign is arbitrary, see compute_difficulty_score.py);
   point budgets are variance-proportional among the included components.
3. **Extremes check** (formerly `diagnose_pc2_extremes.py`) for each of
   `--extremes-components` (default PC2 and PC3): the top/bottom
   `--extremes-n` models and the top/bottom `--tail-pct`% by raw component
   score, with their PC1 and raw-field averages. If both ends sit above the
   average PC1, the component separates two kinds of *large* models (a real
   style axis) rather than small models drifting to one end by default.
4. **Clamped vs. unclamped**: PC1+PC2 with and without the 1st/99th
   percentile clip -- how many models would leave 0-100, and whether rank
   agreement with the article changes.
5. **Exclusion sensitivity**: PC1+PC2 refit after also removing the models
   with zero `has_logic` methods (`classify_method_logic.py`), to show
   whether logic-less-but-working models move the result.
6. **PC3 impact**: what adding PC3 would actually do to the score -- rank
   agreement between PC1+PC2 and PC1+PC2+PC3, how far scores move, how many
   models change 10-point difficulty bucket, the biggest risers and fallers
   with their structure, and whether models with methods move differently.
   This is the evidence for keeping PC1+PC2 although Kaiser and parallel
   analysis retain 3 components (docs/DECISIONS.md, 2026-10-18).

Models whose methods are all empty stubs (`no_logic` in
`logic_validation_report.json`) are always excluded; they are already outside
`reports/usable_models.txt`.

Usage:
    python scripts/experiment_difficulty_score_pca.py [--models-file PATH]
        [--dataset-dir PATH] [--reports-dir PATH] [--max-components N]
        [--parallel-iterations N] [--seed N] [--extremes-components 2,3]
        [--extremes-n N] [--tail-pct P] [--top-movers N]
"""
from __future__ import annotations

import argparse
import datetime
import json
import sys
from pathlib import Path

import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parent))
from _common.io import add_common_io_args, iter_measured_models, read_model_names  # noqa: E402
from _common.report import write_reports  # noqa: E402
from compute_difficulty_score import FIELDS, compute_pca, component_vector, project  # noqa: E402
from compare_difficulty_scores import pearson, spearman  # noqa: E402

LOGIC_VALIDATION_REPORT = "logic_validation_report.json"
METHOD_LOGIC_REPORT = "method_logic_classification_report.json"
REPORT_NAME = "difficulty_score_pca_experiment_report"


def load_no_logic_only_models(reports_dir: Path) -> set[str]:
    path = reports_dir / LOGIC_VALIDATION_REPORT
    data = json.loads(path.read_text(encoding="utf-8"))
    return {r["model"] for r in data["results"] if r.get("status") == "no_logic"}


def load_zero_has_logic_models(reports_dir: Path) -> set[str]:
    """Models with zero has_logic-classified methods (only trivial getters/
    setters), per `classify_method_logic.py`. Disjoint from the no_logic set:
    the classification only ran on usable models."""
    path = reports_dir / METHOD_LOGIC_REPORT
    data = json.loads(path.read_text(encoding="utf-8"))
    return {r["model"] for r in data["results"] if r["totals"].get("has_logic", 0) == 0}


def load_models(dataset_dir: Path, only: set[str] | None, excluded: set[str]) -> tuple[list[str], np.ndarray, np.ndarray]:
    """(model names, raw FIELDS matrix, article scores) in one pass. Models
    without a `difficulty_score_article` yet are skipped, same guard as
    compare_difficulty_scores.py."""
    models: list[str] = []
    rows: list[list[float]] = []
    article: list[float] = []
    for name, _path, data in iter_measured_models(dataset_dir, only):
        if name in excluded or "difficulty_score_article" not in data:
            continue
        models.append(name)
        rows.append([float(data.get(f) or 0) for f in FIELDS])
        article.append(float(data["difficulty_score_article"]))
    return models, np.array(rows, dtype=np.float64), np.array(article, dtype=np.float64)


def rescale(raw_scores: np.ndarray, low_pct: float, high_pct: float, budget: float, clamp: bool) -> np.ndarray:
    """Percentile-derived lo/hi, linearly mapped onto [0, budget]. With
    clamp=False a model beyond the band lands below 0 or above `budget`."""
    lo = float(np.percentile(raw_scores, low_pct))
    hi = float(np.percentile(raw_scores, high_pct))
    if hi == lo:
        return np.zeros_like(raw_scores)
    if clamp:
        raw_scores = np.clip(raw_scores, lo, hi)
    return (raw_scores - lo) / (hi - lo) * budget


def combined_score_for_components(
    raw_matrix: np.ndarray, fit: dict, component_indices: list[int],
    low_pct: float, high_pct: float, scale_max: float, clamp: bool,
) -> np.ndarray:
    variances = [fit["all_components"][i]["variance_explained"] for i in component_indices]
    total_variance = sum(variances)
    total_points = np.zeros(raw_matrix.shape[0], dtype=np.float64)
    for i, variance in zip(component_indices, variances):
        raw_scores = project(raw_matrix, fit, component_vector(fit, i))
        if i != 0:
            raw_scores = np.abs(raw_scores)
        total_points += rescale(raw_scores, low_pct, high_pct, scale_max * variance / total_variance, clamp)
    return total_points


def leading_count(passes: list[bool]) -> int:
    """How many components pass from PC1 onward before the first failure --
    retention rules keep a leading run, not scattered components."""
    count = 0
    for ok in passes:
        if not ok:
            break
        count += 1
    return count


def component_retention(fit: dict, n_models: int, iterations: int, seed: int) -> dict:
    eigenvalues = np.array(fit["all_eigenvalues"])
    p = len(eigenvalues)
    shares = eigenvalues / eigenvalues.sum()
    broken_stick = np.array([sum(1.0 / i for i in range(k, p + 1)) / p for k in range(1, p + 1)])

    rng = np.random.default_rng(seed)
    random_eigenvalues = np.empty((iterations, p))
    for it in range(iterations):
        noise = rng.standard_normal((n_models, p))
        random_eigenvalues[it] = np.sort(np.linalg.eigvalsh(np.corrcoef(noise, rowvar=False)))[::-1]
    pa_mean = random_eigenvalues.mean(axis=0)
    pa_p95 = np.percentile(random_eigenvalues, 95, axis=0)

    kaiser_pass = [bool(e > 1.0) for e in eigenvalues]
    broken_stick_pass = [bool(s > b) for s, b in zip(shares, broken_stick)]
    parallel_pass = [bool(e > t) for e, t in zip(eigenvalues, pa_p95)]
    components = [
        {
            "component": f"PC{k + 1}",
            "eigenvalue": float(eigenvalues[k]),
            "variance_explained": float(shares[k]),
            "scree_drop_to_next": float(eigenvalues[k] - eigenvalues[k + 1]) if k + 1 < p else None,
            "kaiser_pass": kaiser_pass[k],
            "broken_stick_expected_share": float(broken_stick[k]),
            "broken_stick_pass": broken_stick_pass[k],
            "parallel_random_mean": float(pa_mean[k]),
            "parallel_random_p95": float(pa_p95[k]),
            "parallel_pass": parallel_pass[k],
        }
        for k in range(p)
    ]
    return {
        "parallel_iterations": iterations,
        "seed": seed,
        "retained_kaiser": leading_count(kaiser_pass),
        "retained_broken_stick": leading_count(broken_stick_pass),
        "retained_parallel_analysis": leading_count(parallel_pass),
        "components": components,
    }


def extremes_check(models: list[str], raw_matrix: np.ndarray, fit: dict, index: int, n: int, tail_pct: float) -> dict:
    pc1_scores = project(raw_matrix, fit, component_vector(fit, 0))
    scores = project(raw_matrix, fit, component_vector(fit, index))
    order = np.argsort(scores)
    n_tail = max(1, round(len(models) * tail_pct / 100.0))

    def group(idx: np.ndarray, with_members: bool) -> dict:
        summary = {
            "size": int(len(idx)),
            "mean_pc1": float(pc1_scores[idx].mean()),
            "mean_component_score": float(scores[idx].mean()),
            "mean_fields": {f: float(raw_matrix[idx, j].mean()) for j, f in enumerate(FIELDS)},
        }
        if with_members:
            summary["members"] = [
                {"model": models[i], "pc1": float(pc1_scores[i]), "score": float(scores[i]),
                 "fields": {f: float(raw_matrix[i, j]) for j, f in enumerate(FIELDS)}}
                for i in idx
            ]
        return summary

    groups = {
        "bottom_n": group(order[:n], True),
        "top_n": group(order[-n:][::-1], True),
        "bottom_tail": group(order[:n_tail], False),
        "top_tail": group(order[-n_tail:], False),
    }
    overall_pc1 = float(pc1_scores.mean())
    loadings = fit["all_components"][index]["loadings"]
    return {
        "component": f"PC{index + 1}",
        "variance_explained": fit["all_components"][index]["variance_explained"],
        "loadings": loadings,
        "overall_mean_pc1": overall_pc1,
        "extremes_n": n,
        "tail_pct": tail_pct,
        **groups,
        "both_extremes_above_mean_pc1": bool(groups["bottom_n"]["mean_pc1"] > overall_pc1
                                             and groups["top_n"]["mean_pc1"] > overall_pc1),
        "both_tails_above_mean_pc1": bool(groups["bottom_tail"]["mean_pc1"] > overall_pc1
                                          and groups["top_tail"]["mean_pc1"] > overall_pc1),
    }


def pc3_impact(models: list[str], raw_matrix: np.ndarray, two: np.ndarray, three: np.ndarray, top: int) -> dict:
    """Official PC1+PC2 score vs. the same score with PC3 added."""
    delta = three - two
    bucket_two = np.minimum((two // 10).astype(int), 9)
    bucket_three = np.minimum((three // 10).astype(int), 9)
    jumps = np.abs(bucket_three - bucket_two)
    has_methods = raw_matrix[:, FIELDS.index("methods")] > 0

    def movers(order: np.ndarray) -> list[dict]:
        return [
            {"model": models[i], "score_pc1_pc2": float(two[i]), "score_pc1_pc2_pc3": float(three[i]),
             "change": float(delta[i]), "fields": {f: float(raw_matrix[i, j]) for j, f in enumerate(FIELDS)}}
            for i in order[:top]
        ]

    return {
        "spearman_between_scores": spearman(two, three),
        "mean_change": float(delta.mean()),
        "median_abs_change": float(np.median(np.abs(delta))),
        "p90_abs_change": float(np.percentile(np.abs(delta), 90)),
        "max_rise": float(delta.max()),
        "max_fall": float(delta.min()),
        "bucket_changed_count": int((jumps > 0).sum()),
        "bucket_changed_pct": float((jumps > 0).mean() * 100),
        "bucket_changed_by_two_or_more": int((jumps >= 2).sum()),
        "bucket_counts_pc1_pc2": [int((bucket_two == b).sum()) for b in range(10)],
        "bucket_counts_pc1_pc2_pc3": [int((bucket_three == b).sum()) for b in range(10)],
        "mean_change_models_with_methods": float(delta[has_methods].mean()) if has_methods.any() else None,
        "mean_change_models_without_methods": float(delta[~has_methods].mean()) if (~has_methods).any() else None,
        "models_with_methods": int(has_methods.sum()),
        "biggest_risers": movers(np.argsort(delta)[::-1]),
        "biggest_fallers": movers(np.argsort(delta)),
    }


def render_markdown_report(report: dict) -> str:
    retention = report["component_retention"]
    lines = [
        "# PCA difficulty score: evidence report",
        "",
        f"Generated: {report['generated_at']}",
        "",
        f"- **Models used:** {report['models_used']} "
        f"(models file: `{report['models_file'] or 'all measured'}`, "
        f"{report['models_excluded_no_logic_only']} no_logic-only models excluded)",
        f"- **Official score (PC1+PC2) vs. article, Spearman:** {report['unclamped_experiment']['spearman_clamped_vs_article']:+.4f}",
        "",
        "## 1. How many components to keep",
        "",
        f"Retained by Kaiser (eigenvalue > 1): **{retention['retained_kaiser']}** · "
        f"broken stick: **{retention['retained_broken_stick']}** · "
        f"parallel analysis ({retention['parallel_iterations']} random runs, seed {retention['seed']}, 95th pct): "
        f"**{retention['retained_parallel_analysis']}**",
        "",
        "| Component | Eigenvalue | Variance | Scree drop | Kaiser | Broken stick (expected) | Parallel p95 (random) |",
        "|---|---:|---:|---:|:-:|---:|---:|",
    ]
    for c in retention["components"]:
        drop = f"{c['scree_drop_to_next']:.3f}" if c["scree_drop_to_next"] is not None else "–"
        lines.append(
            f"| {c['component']} | {c['eigenvalue']:.3f} | {c['variance_explained'] * 100:.2f}% | {drop} | "
            f"{'✓' if c['kaiser_pass'] else '✗'} | {'✓' if c['broken_stick_pass'] else '✗'} "
            f"({c['broken_stick_expected_share'] * 100:.2f}%) | "
            f"{'✓' if c['parallel_pass'] else '✗'} ({c['parallel_random_p95']:.3f}) |"
        )
    lines += [
        "",
        "## 2. Component sweep vs. the article formula",
        "",
        "| Components | Cumulative variance | Spearman | Pearson | Score range |",
        "|---|---:|---:|---:|---|",
    ]
    for s in report["component_sweep"]:
        lines.append(
            f"| PC1..PC{s['components_included']} | {s['cumulative_variance_explained'] * 100:.2f}% | "
            f"{s['spearman_vs_article']:+.4f} | {s['pearson_vs_article']:+.4f} | "
            f"{s['score_min']:.2f}–{s['score_max']:.2f} |"
        )
    lines += ["", "## 3. Extremes check (is the component a real style axis?)", ""]
    for e in report["extremes_check"]:
        lines += [
            f"### {e['component']} ({e['variance_explained'] * 100:.2f}% variance)",
            "",
            f"Overall mean PC1: {e['overall_mean_pc1']:+.3f}",
            "",
            "| Group | Size | Mean PC1 | Mean score |",
            "|---|---:|---:|---:|",
        ]
        for key, label in [("bottom_n", f"Bottom {e['extremes_n']}"), ("top_n", f"Top {e['extremes_n']}"),
                           ("bottom_tail", f"Bottom {e['tail_pct']:g}%"), ("top_tail", f"Top {e['tail_pct']:g}%")]:
            g = e[key]
            lines.append(f"| {label} | {g['size']} | {g['mean_pc1']:+.3f} | {g['mean_component_score']:+.3f} |")
        lines += [
            "",
            f"Both extreme groups above average PC1: **{'yes' if e['both_extremes_above_mean_pc1'] else 'no'}** · "
            f"both tails: **{'yes' if e['both_tails_above_mean_pc1'] else 'no'}**",
            "",
        ]
    unclamped = report["unclamped_experiment"]
    exclusion = report["wider_exclusion_experiment"]
    lines += [
        "## 4. Clamped vs. unclamped (PC1+PC2)",
        "",
        f"Spearman change without the clip: {unclamped['spearman_delta']:+.5f}; "
        f"{unclamped['models_over_cap_count']} models above 100, {unclamped['models_under_cap_count']} below 0 "
        f"(max {unclamped['unclamped_score_max']:.2f}).",
        "",
        "## 5. Exclusion sensitivity (PC1+PC2)",
        "",
        f"- Base set (n={exclusion['narrower_exclusion']['models_used']}): "
        f"Spearman {exclusion['narrower_exclusion']['spearman_vs_article']:+.4f}",
        f"- Also without {exclusion['zero_has_logic_models_count']} zero-has_logic models "
        f"(n={exclusion['wider_exclusion']['models_used']}): "
        f"Spearman {exclusion['wider_exclusion']['spearman_vs_article']:+.4f}",
        "",
    ]
    impact = report["pc3_impact"]
    lines += [
        "## 6. What adding PC3 would do (PC1+PC2 vs. PC1+PC2+PC3)",
        "",
        f"- Rank agreement between the two scores (Spearman): **{impact['spearman_between_scores']:+.4f}**",
        f"- Score change: median |change| {impact['median_abs_change']:.2f}, 90th pct {impact['p90_abs_change']:.2f}, "
        f"largest rise {impact['max_rise']:+.2f}, largest fall {impact['max_fall']:+.2f}",
        f"- Models changing 10-point bucket: {impact['bucket_changed_count']} ({impact['bucket_changed_pct']:.1f}%), "
        f"{impact['bucket_changed_by_two_or_more']} by two or more",
        f"- Mean change, models with methods: {impact['mean_change_models_with_methods']:+.2f} "
        f"(n={impact['models_with_methods']}); without: {impact['mean_change_models_without_methods']:+.2f}",
        "",
        "| Bucket | PC1+PC2 | PC1+PC2+PC3 |",
        "|---|---:|---:|",
    ]
    for b, (c2, c3) in enumerate(zip(impact["bucket_counts_pc1_pc2"], impact["bucket_counts_pc1_pc2_pc3"])):
        lines.append(f"| {b * 10}-{b * 10 + 10} | {c2} | {c3} |")
    for key, label in [("biggest_risers", "Biggest risers"), ("biggest_fallers", "Biggest fallers")]:
        lines += [
            "",
            f"**{label}**",
            "",
            "| Model | PC1+PC2 | +PC3 | Change | Classes | Enums | Methods |",
            "|---|---:|---:|---:|---:|---:|---:|",
        ]
        for m in impact[key]:
            f = m["fields"]
            lines.append(f"| {m['model']} | {m['score_pc1_pc2']:.2f} | {m['score_pc1_pc2_pc3']:.2f} | "
                         f"{m['change']:+.2f} | {f['classes']:.0f} | {f['enumerations']:.0f} | {f['methods']:.0f} |")
    lines += ["", "Full per-model detail: see the accompanying `.json` report."]
    return "\n".join(lines) + "\n"


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    add_common_io_args(parser, __file__)
    parser.add_argument("--models-file", type=Path, help="Fit only these models (e.g. reports/usable_models.txt)")
    parser.add_argument("--low-percentile", type=float, default=1.0)
    parser.add_argument("--high-percentile", type=float, default=99.0)
    parser.add_argument("--scale-max", type=float, default=100.0)
    parser.add_argument("--max-components", type=int, default=11)
    parser.add_argument("--parallel-iterations", type=int, default=100)
    parser.add_argument("--seed", type=int, default=42)
    parser.add_argument("--extremes-components", default="2,3",
                         help="Comma-separated component numbers for the extremes check")
    parser.add_argument("--extremes-n", type=int, default=10)
    parser.add_argument("--tail-pct", type=float, default=5.0)
    parser.add_argument("--top-movers", type=int, default=15)
    args = parser.parse_args()

    only = set(read_model_names(args.models_file)) if args.models_file else None
    excluded = load_no_logic_only_models(args.reports_dir)
    excluded_in_set = len(excluded if only is None else excluded & only)
    models, raw_matrix, article_scores = load_models(args.dataset_dir, only, excluded)
    print(f"Loaded {len(models)} measured models ({excluded_in_set} no_logic-only excluded)")

    fit = compute_pca(raw_matrix)
    n_components = min(args.max_components, len(fit["all_components"]))

    print("\n--- 1: component retention ---")
    retention = component_retention(fit, len(models), args.parallel_iterations, args.seed)
    for c in retention["components"]:
        print(f"  {c['component']:>4}: eigenvalue={c['eigenvalue']:.3f}  variance={c['variance_explained'] * 100:5.2f}%  "
              f"kaiser={'Y' if c['kaiser_pass'] else 'n'}  broken_stick={'Y' if c['broken_stick_pass'] else 'n'}  "
              f"parallel={'Y' if c['parallel_pass'] else 'n'} (random p95 {c['parallel_random_p95']:.3f})")
    print(f"  Retained: Kaiser {retention['retained_kaiser']}, broken stick {retention['retained_broken_stick']}, "
          f"parallel analysis {retention['retained_parallel_analysis']}")

    print("\n--- 2: component sweep (PC1..PCk vs. article) ---")
    sweep_results = []
    for k in range(1, n_components + 1):
        indices = list(range(k))
        combined = combined_score_for_components(
            raw_matrix, fit, indices, args.low_percentile, args.high_percentile, args.scale_max, clamp=True,
        )
        cumulative_variance = fit["all_components"][k - 1]["cumulative_variance_explained"]
        sweep_results.append({
            "components_included": k,
            "component_labels": [fit["all_components"][i]["component"] for i in indices],
            "cumulative_variance_explained": cumulative_variance,
            "spearman_vs_article": spearman(combined, article_scores),
            "pearson_vs_article": pearson(combined, article_scores),
            "score_min": float(combined.min()),
            "score_max": float(combined.max()),
        })
        s = sweep_results[-1]
        print(f"  PC1..PC{k}: cum.variance={cumulative_variance * 100:5.2f}%  "
              f"spearman={s['spearman_vs_article']:+.4f}  pearson={s['pearson_vs_article']:+.4f}")

    print("\n--- 3: extremes check ---")
    extremes = []
    for number in (int(x) for x in args.extremes_components.split(",") if x.strip()):
        e = extremes_check(models, raw_matrix, fit, number - 1, args.extremes_n, args.tail_pct)
        extremes.append(e)
        print(f"  {e['component']}: mean PC1 bottom-{args.extremes_n}={e['bottom_n']['mean_pc1']:+.3f}  "
              f"top-{args.extremes_n}={e['top_n']['mean_pc1']:+.3f}  "
              f"bottom-{args.tail_pct:g}%={e['bottom_tail']['mean_pc1']:+.3f}  "
              f"top-{args.tail_pct:g}%={e['top_tail']['mean_pc1']:+.3f}  (overall {e['overall_mean_pc1']:+.3f})")

    print("\n--- 4: PC1+PC2, clamped vs. unclamped ---")
    clamped = combined_score_for_components(
        raw_matrix, fit, [0, 1], args.low_percentile, args.high_percentile, args.scale_max, clamp=True,
    )
    unclamped = combined_score_for_components(
        raw_matrix, fit, [0, 1], args.low_percentile, args.high_percentile, args.scale_max, clamp=False,
    )
    r_spearman_clamped = spearman(clamped, article_scores)
    r_spearman_unclamped = spearman(unclamped, article_scores)
    frac = unclamped / args.scale_max
    over, under = frac > 1.0, frac < 0.0
    n_over, n_under = int(over.sum()), int(under.sum())
    print(f"  Clamped spearman={r_spearman_clamped:+.4f}, unclamped={r_spearman_unclamped:+.4f}; "
          f"{n_over} above / {n_under} below the 0-{args.scale_max:.0f} scale")

    def capped(mask: np.ndarray, descending: bool) -> list[dict]:
        rows = [{"model": models[i], "unclamped_score": float(unclamped[i]), "fraction_of_scale": float(frac[i])}
                for i in np.where(mask)[0]]
        return sorted(rows, key=lambda x: -x["fraction_of_scale"] if descending else x["fraction_of_scale"])

    print("\n--- 5: exclusion sensitivity ---")
    zero_has_logic = load_zero_has_logic_models(args.reports_dir)
    models_wide, raw_matrix_wide, article_scores_wide = load_models(args.dataset_dir, only, excluded | zero_has_logic)
    combined_wide = combined_score_for_components(
        raw_matrix_wide, compute_pca(raw_matrix_wide), [0, 1],
        args.low_percentile, args.high_percentile, args.scale_max, clamp=True,
    )

    def stats(n_models: int, score: np.ndarray, r: float) -> dict:
        return {"models_used": n_models, "spearman_vs_article": r, "mean": float(score.mean()),
                "median": float(np.median(score)), "min": float(score.min()), "max": float(score.max())}

    narrower_stats = stats(len(models), clamped, r_spearman_clamped)
    wider_stats = stats(len(models_wide), combined_wide, spearman(combined_wide, article_scores_wide))
    print(f"  Base (n={narrower_stats['models_used']}): spearman={narrower_stats['spearman_vs_article']:+.4f}; "
          f"without zero-has_logic (n={wider_stats['models_used']}): spearman={wider_stats['spearman_vs_article']:+.4f}")

    print("\n--- 6: PC3 impact ---")
    with_pc3 = combined_score_for_components(
        raw_matrix, fit, [0, 1, 2], args.low_percentile, args.high_percentile, args.scale_max, clamp=True,
    )
    impact = pc3_impact(models, raw_matrix, clamped, with_pc3, args.top_movers)
    print(f"  Spearman(PC1+PC2, PC1+PC2+PC3)={impact['spearman_between_scores']:+.4f}  "
          f"median |change|={impact['median_abs_change']:.2f}  "
          f"bucket changed: {impact['bucket_changed_count']} ({impact['bucket_changed_pct']:.1f}%)  "
          f"methods vs none: {impact['mean_change_models_with_methods']:+.2f} / "
          f"{impact['mean_change_models_without_methods']:+.2f}")

    report = {
        "generated_at": datetime.datetime.now(datetime.timezone.utc).isoformat(),
        "models_file": str(args.models_file) if args.models_file else None,
        "models_used": len(models),
        "models_excluded_no_logic_only": excluded_in_set,
        "rescale_low_percentile": args.low_percentile,
        "rescale_high_percentile": args.high_percentile,
        "scale_max": args.scale_max,
        "component_retention": retention,
        "component_sweep": sweep_results,
        "extremes_check": extremes,
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
            "models_over_cap": capped(over, descending=True),
            "models_under_cap": capped(under, descending=False),
        },
        "wider_exclusion_experiment": {
            "zero_has_logic_models_count": len(zero_has_logic),
            "narrower_exclusion": narrower_stats,
            "wider_exclusion": wider_stats,
        },
        "pc3_impact": impact,
    }
    json_path, md_path = write_reports(args.reports_dir, REPORT_NAME, report, render_markdown_report(report))
    print(f"\nReport written to {json_path} and {md_path}")


if __name__ == "__main__":
    main()
