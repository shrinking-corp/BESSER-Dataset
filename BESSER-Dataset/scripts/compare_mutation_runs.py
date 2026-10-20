#!/usr/bin/env python3
"""Compare two `validate_mutation_properties.py` reports model by model,
e.g. the green baseline (A) against the super suite (B), or a full run (A)
against an isolated rerun of some of its models (B). Read-only apart from
the report it writes.

Only models measured in both reports are compared. Per model the score
difference is B - A; the report gives:
  - mean score of A and B, the lift (B - A, in points), and how many models
    improved, got worse or stayed the same;
  - perfect (1.0) and zero scores on each side;
  - a check that both runs ran the same number of mutants per model (the
    cap is seeded per model name, so the same suite pair sees the same mutants);
  - kills that were only a per-mutant timeout (`killed_by_timeout`): their
    totals, and the means and lift with those kills counted as survived,
    i.e. the lowest the scores can be if every one of them was fake;
  - everything again per 10-point difficulty bucket (`model_metadata.json`);
  - the largest drops (B below A), and every model with a timeout kill on
    either side.

--write-timeout-models PATH writes the models with a timeout kill in either
report, one per line, for an isolated rerun.

Stdlib only, any venv.

Usage:
    python scripts/compare_mutation_runs.py --a reports/full_baseline_green_mutation.json
        --b reports/full_super_suite_mutation.json [--label-a NAME] [--label-b NAME]
        [--models-file PATH] [--report-name NAME] [--top N]
        [--write-timeout-models PATH] [--dataset-dir PATH] [--reports-dir PATH]
"""
from __future__ import annotations

import argparse
import datetime
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from _common.io import add_common_io_args, iter_measured_models, read_model_names  # noqa: E402
from _common.report import write_reports  # noqa: E402
from make_benchmark_split import BUCKET_LABELS, bucket_index  # noqa: E402


def load_results(path: Path) -> tuple[dict, dict[str, dict]]:
    report = json.loads(path.read_text(encoding="utf-8"))
    return report, {r["model"]: r for r in report["results"]}


def lower_bound(result: dict) -> float:
    """The score with every timeout kill counted as survived."""
    return (result["killed"] - (result.get("killed_by_timeout") or 0)) / result["mutants_run"]


def summarize(pairs: list[tuple[dict, dict]]) -> dict:
    n = len(pairs)
    if not n:
        return {"models": 0}
    diffs = [b["mutation_score"] - a["mutation_score"] for a, b in pairs]
    mean = lambda values: round(sum(values) / n, 4)  # noqa: E731
    mean_a, mean_b = mean([a["mutation_score"] for a, _ in pairs]), mean([b["mutation_score"] for _, b in pairs])
    low_a, low_b = mean([lower_bound(a) for a, _ in pairs]), mean([lower_bound(b) for _, b in pairs])
    return {
        "models": n,
        "mean_a": mean_a,
        "mean_b": mean_b,
        "lift_points": round((mean_b - mean_a) * 100, 2),
        "improved": sum(d > 0 for d in diffs),
        "worse": sum(d < 0 for d in diffs),
        "unchanged": sum(d == 0 for d in diffs),
        "perfect_a": sum(a["mutation_score"] == 1.0 for a, _ in pairs),
        "perfect_b": sum(b["mutation_score"] == 1.0 for _, b in pairs),
        "zero_a": sum(a["mutation_score"] == 0.0 for a, _ in pairs),
        "zero_b": sum(b["mutation_score"] == 0.0 for _, b in pairs),
        "timeout_kills_a": sum(a.get("killed_by_timeout") or 0 for a, _ in pairs),
        "timeout_kills_b": sum(b.get("killed_by_timeout") or 0 for _, b in pairs),
        "lower_bound_mean_a": low_a,
        "lower_bound_mean_b": low_b,
        "lower_bound_lift_points": round((low_b - low_a) * 100, 2),
    }


def render_markdown(report: dict) -> str:
    la, lb = report["label_a"], report["label_b"]
    s = report["overall"]
    lines = [
        f"# Mutation runs compared: {la} (A) vs {lb} (B)",
        "",
        f"Generated: {report['generated_at']}",
        "",
        f"- A: `{report['report_a']}`",
        f"- B: `{report['report_b']}`",
        f"- **Models measured in both:** {s['models']}"
        + (f" (only in A: {len(report['only_in_a'])}, only in B: {len(report['only_in_b'])})"
           if report["only_in_a"] or report["only_in_b"] else ""),
        f"- **Mean score:** A {s['mean_a']} · B {s['mean_b']} · **lift {s['lift_points']:+.2f} pts**",
        f"- **Per model (B vs A):** {s['improved']} improved · {s['worse']} worse · {s['unchanged']} unchanged",
        f"- **Perfect scores:** A {s['perfect_a']} · B {s['perfect_b']} · **zero scores:** A {s['zero_a']} · B {s['zero_b']}",
        f"- **Same number of mutants run per model:** "
        + ("yes, every model" if not report["mutant_count_mismatches"]
           else f"NO, {len(report['mutant_count_mismatches'])} models differ"),
        f"- **Kills that were only a per-mutant timeout:** A {s['timeout_kills_a']} · B {s['timeout_kills_b']}. "
        f"Counting all of them as survived: A {s['lower_bound_mean_a']} · B {s['lower_bound_mean_b']} · "
        f"lift {s['lower_bound_lift_points']:+.2f} pts",
        "",
        "## By difficulty bucket",
        "",
        "| Bucket | Models | A | B | Lift (pts) | Improved | Worse | Unchanged |",
        "|---|---:|---:|---:|---:|---:|---:|---:|",
    ]
    for label, b in report["by_bucket"].items():
        if b["models"]:
            lines.append(f"| {label} | {b['models']} | {b['mean_a']} | {b['mean_b']} | {b['lift_points']:+.2f} "
                         f"| {b['improved']} | {b['worse']} | {b['unchanged']} |")
    if report["no_difficulty_score"]:
        lines.append(f"\n{len(report['no_difficulty_score'])} compared models have no difficulty score "
                     "and appear only in the overall numbers.")
    lines += ["", f"## Largest drops (B below A), top {report['top']}", ""]
    if report["largest_drops"]:
        lines += ["| Model | A | B | Change |", "|---|---:|---:|---:|"]
        lines += [f"| {d['model']} | {d['a']} | {d['b']} | {d['change']:+.4f} |" for d in report["largest_drops"]]
    else:
        lines.append("None: no model scores lower in B than in A.")
    lines += ["", "## Models with a timeout kill on either side", ""]
    if report["timeout_models"]:
        lines += ["| Model | A score | A timeout kills | B score | B timeout kills |", "|---|---:|---:|---:|---:|"]
        lines += [f"| {t['model']} | {t['a']} | {t['timeout_kills_a']} | {t['b']} | {t['timeout_kills_b']} |"
                  for t in report["timeout_models"]]
    else:
        lines.append("None.")
    return "\n".join(lines) + "\n"


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    add_common_io_args(parser, __file__)
    parser.add_argument("--a", type=Path, required=True, help="Report A (e.g. the baseline)")
    parser.add_argument("--b", type=Path, required=True, help="Report B (e.g. the super suite)")
    parser.add_argument("--label-a", default=None, help="Default: A's test file")
    parser.add_argument("--label-b", default=None, help="Default: B's test file")
    parser.add_argument("--models-file", type=Path, default=None, help="Compare only these models")
    parser.add_argument("--report-name", default="mutation_comparison")
    parser.add_argument("--top", type=int, default=20)
    parser.add_argument("--write-timeout-models", type=Path, default=None)
    args = parser.parse_args()

    _report_a, results_a = load_results(args.a)
    _report_b, results_b = load_results(args.b)
    only = set(read_model_names(args.models_file)) if args.models_file else None

    def measured(results: dict[str, dict]) -> set[str]:
        return {m for m, r in results.items() if r.get("mutation_score") is not None and (only is None or m in only)}

    in_a, in_b = measured(results_a), measured(results_b)
    common = sorted(in_a & in_b)
    pairs = [(results_a[m], results_b[m]) for m in common]

    def label(results: dict[str, dict], given: str | None) -> str:
        return given or next((r.get("test_file") for r in results.values() if r.get("test_file")), "?")

    scores = {name: float(data["difficulty_score"])
              for name, _p, data in iter_measured_models(args.dataset_dir, set(common)) if "difficulty_score" in data}
    by_bucket_pairs: dict[str, list] = {label_: [] for label_ in BUCKET_LABELS}
    for m, pair in zip(common, pairs):
        if m in scores:
            by_bucket_pairs[BUCKET_LABELS[bucket_index(scores[m])]].append(pair)

    drops = sorted(((m, a, b) for m, (a, b) in zip(common, pairs) if b["mutation_score"] < a["mutation_score"]),
                   key=lambda t: t[2]["mutation_score"] - t[1]["mutation_score"])
    timeout_models = [m for m, (a, b) in zip(common, pairs) if a.get("killed_by_timeout") or b.get("killed_by_timeout")]

    report = {
        "generated_at": datetime.datetime.now(datetime.timezone.utc).isoformat(),
        "report_a": str(args.a), "report_b": str(args.b),
        "label_a": label(results_a, args.label_a), "label_b": label(results_b, args.label_b),
        "models_file": str(args.models_file) if args.models_file else None,
        "overall": summarize(pairs),
        "by_bucket": {label_: summarize(p) for label_, p in by_bucket_pairs.items()},
        "no_difficulty_score": [m for m in common if m not in scores],
        "only_in_a": sorted(in_a - in_b), "only_in_b": sorted(in_b - in_a),
        "mutant_count_mismatches": [m for m, (a, b) in zip(common, pairs) if a["mutants_run"] != b["mutants_run"]],
        "top": args.top,
        "largest_drops": [{"model": m, "a": a["mutation_score"], "b": b["mutation_score"],
                           "change": round(b["mutation_score"] - a["mutation_score"], 4)}
                          for m, a, b in drops[:args.top]],
        "timeout_models": [{"model": m, "a": results_a[m]["mutation_score"],
                            "timeout_kills_a": results_a[m].get("killed_by_timeout") or 0,
                            "b": results_b[m]["mutation_score"],
                            "timeout_kills_b": results_b[m].get("killed_by_timeout") or 0}
                           for m in timeout_models],
    }
    json_path, md_path = write_reports(args.reports_dir, args.report_name, report, render_markdown(report))
    if args.write_timeout_models:
        args.write_timeout_models.parent.mkdir(parents=True, exist_ok=True)
        args.write_timeout_models.write_text("".join(f"{m}\n" for m in timeout_models), encoding="utf-8")
        print(f"{len(timeout_models)} models with a timeout kill written to {args.write_timeout_models}")

    s = report["overall"]
    print(f"{s['models']} models: A {s['mean_a']} vs B {s['mean_b']} -> lift {s['lift_points']:+.2f} pts "
          f"({s['improved']} improved / {s['worse']} worse / {s['unchanged']} unchanged)")
    print(f"Report written to {json_path} and {md_path}")


if __name__ == "__main__":
    main()
