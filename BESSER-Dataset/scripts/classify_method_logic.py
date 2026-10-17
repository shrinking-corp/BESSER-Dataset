#!/usr/bin/env python3
"""Classify every method in `python_code.py` by how much real logic it has.

this test-generation comparison, step 1: before spending effort generating tests
that target "real logic", we need to know which methods actually have any.
This generalizes `validate_logic.py`'s whole-model `no_logic` check down to
individual methods, and splits the remainder into `trivial` (plain field
assignment / getters / setters / guarded bidirectional-association setters --
nothing a value-varying test could meaningfully falsify beyond what an
isinstance/hasattr check already does) and `has_logic` (a loop, a multi-branch
or nested conditional, a `try`, a `match`, a comprehension, or an arithmetic/
boolean computation -- something a mutation could actually break in a way
that depends on *which* input value you pick).

Classification rules, in order:

1. **no_logic** -- body is empty/`pass`/`...`/docstring-only (same stub
   detection as `validate_logic.py`).
2. **trivial** -- no loop, no `try`, no `match`, no comprehension/lambda, no
   arithmetic (`BinOp`)/boolean (`BoolOp`) computation anywhere, AND any `if`
   present is a single, non-`elif` guard (e.g. the common bidirectional-
   association pattern `if self._x is not None: self._x._y.remove(self)`),
   AND the body has at most 4 statements total.
3. **has_logic** -- everything else.

This is a static, AST-only heuristic tuned for triage/sampling (Phase 4's
"which methods are worth targeting"), not a formal complexity metric.

Usage:
    python scripts/classify_method_logic.py [--models-file PATH] [--workers N]
        [--dataset-dir PATH] [--reports-dir PATH] [--limit N] [--write-metadata]

Without --write-metadata this only writes the aggregate reports (dry run).

Each model's code_metadata.json gets (or has updated) a top-level
"method_logic_classification" key:

    {
      "method_logic_classification": {
        "checked_at": "...", "python_version": "...",
        "status": "measured",   # measured | missing_file | empty_file | syntax_error
        "totals": {"no_logic": N, "trivial": N, "has_logic": N, "total_methods": N},
        "has_logic_methods": [{"class": "...", "method": "...", "statement_count": N}, ...]
      }
    }
"""
from __future__ import annotations

import argparse
import ast
import concurrent.futures
import datetime
import json
import platform
from pathlib import Path

CODE_FILENAME = "python_code.py"
METADATA_FILENAME = "code_metadata.json"
REPORT_BASENAME = "method_logic_classification_report"

BRANCH_NODES = (ast.For, ast.AsyncFor, ast.While, ast.Try, ast.Match)
COMPUTE_NODES = (ast.BinOp, ast.BoolOp, ast.ListComp, ast.SetComp,
                 ast.DictComp, ast.GeneratorExp, ast.Lambda)
MAX_TRIVIAL_STATEMENTS = 4


def _read_text_robust(path: Path) -> str:
    """Reads a text file regardless of which BOM (if any) Windows wrote --
    confirmed real (2026-10-12): PowerShell's `echo >` defaults to UTF-16LE
    with BOM, `Out-File -Encoding utf8` defaults to UTF-8 WITH BOM (neither
    matches plain `.read_text()`'s assumption) -- `encoding="utf-8-sig"`
    alone only covers the UTF-8 case, not UTF-16, so a `--models-file`
    created with plain `echo` silently corrupts the first model name AND
    throws off line-splitting entirely (one line becomes several, since
    UTF-16 is 2 bytes/char). Sniffs the actual BOM bytes rather than
    guessing from one case."""
    raw = path.read_bytes()
    if raw.startswith(b"\xff\xfe") or raw.startswith(b"\xfe\xff"):
        return raw.decode("utf-16")
    if raw.startswith(b"\xef\xbb\xbf"):
        return raw.decode("utf-8-sig")
    return raw.decode("utf-8")


def find_model_dirs(dataset_dir: Path, models_file: Path | None, limit: int | None) -> list[Path]:
    if models_file:
        names = [l.strip() for l in _read_text_robust(models_file).splitlines() if l.strip()]
        dirs = [dataset_dir / name for name in names]
    else:
        dirs = sorted(p for p in dataset_dir.iterdir() if p.is_dir())
    if limit:
        dirs = dirs[:limit]
    return dirs


def _is_docstring(node: ast.stmt) -> bool:
    return isinstance(node, ast.Expr) and isinstance(node.value, ast.Constant) \
        and isinstance(node.value.value, str)


def _is_stub_body(body: list[ast.stmt]) -> bool:
    meaningful = [n for n in body if not _is_docstring(n)]
    if not meaningful:
        return True
    return all(
        isinstance(n, ast.Pass)
        or (isinstance(n, ast.Expr) and isinstance(n.value, ast.Constant)
            and n.value.value is Ellipsis)
        for n in meaningful
    )


def _count_statements(body: list[ast.stmt]) -> int:
    """Count statements, descending into a single non-elif `if`'s branches."""
    total = 0
    for n in body:
        if _is_docstring(n) or isinstance(n, ast.Pass):
            continue
        total += 1
        if isinstance(n, ast.If) and not n.orelse:
            total += _count_statements(n.body) - 1  # the `if` header already counted
        elif isinstance(n, ast.If) and n.orelse and not _is_elif(n):
            total += _count_statements(n.body) - 1
            total += _count_statements(n.orelse)
    return total


def _is_elif(if_node: ast.If) -> bool:
    """True when `orelse` is itself another `if` (an `elif` chain), not a plain `else`."""
    return len(if_node.orelse) == 1 and isinstance(if_node.orelse[0], ast.If)


def _has_disallowed_node(body: list[ast.stmt]) -> bool:
    """True if anything in `body` (excluding nested function/class defs) rules out `trivial`."""
    for stmt in body:
        for node in ast.walk(stmt):
            if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef, ast.ClassDef)) and node is not stmt:
                continue  # nested defs judged separately, not part of this body's own logic
            if isinstance(node, BRANCH_NODES) or isinstance(node, COMPUTE_NODES):
                return True
            if isinstance(node, ast.If) and _is_elif(node):
                return True
            if isinstance(node, ast.If) and node.orelse and any(
                isinstance(sub, ast.If) for sub in node.orelse
            ):
                return True
    return False


def classify_method_body(body: list[ast.stmt]) -> tuple[str, int]:
    """Returns (category, statement_count) for a single method's body."""
    if _is_stub_body(body):
        return "no_logic", 0

    meaningful = [n for n in body if not _is_docstring(n)]
    stmt_count = _count_statements(meaningful)

    if stmt_count <= MAX_TRIVIAL_STATEMENTS and not _has_disallowed_node(meaningful):
        return "trivial", stmt_count
    return "has_logic", stmt_count


def analyse_source(source: str) -> tuple[list[dict], str | None]:
    """Returns (per-method records, syntax_error_message)."""
    try:
        tree = ast.parse(source)
    except SyntaxError as exc:
        return [], f"{exc.msg} (line {exc.lineno})"

    records: list[dict] = []
    for node in ast.walk(tree):
        if not isinstance(node, ast.ClassDef):
            continue
        for member in node.body:
            if not isinstance(member, (ast.FunctionDef, ast.AsyncFunctionDef)):
                continue
            category, stmt_count = classify_method_body(member.body)
            records.append({
                "class": node.name,
                "method": member.name,
                "category": category,
                "statement_count": stmt_count,
            })
    return records, None


def validate_model(model_dir: Path) -> dict:
    code_path = model_dir / CODE_FILENAME
    result = {
        "model": model_dir.name,
        "checked_at": datetime.datetime.now(datetime.timezone.utc).isoformat(),
        "python_version": platform.python_version(),
        "status": "missing_file",
        "totals": None,
        "methods": None,
        "error_message": None,
    }

    if not code_path.is_file():
        result["error_message"] = f"{CODE_FILENAME} is missing"
        return result

    try:
        source = code_path.read_text(encoding="utf-8", errors="replace")
    except OSError as exc:
        result["error_message"] = f"{CODE_FILENAME} could not be read: {exc}"
        return result

    if not source.strip():
        result["status"] = "empty_file"
        return result

    records, syntax_error = analyse_source(source)
    if syntax_error is not None:
        result["status"] = "syntax_error"
        result["error_message"] = syntax_error
        return result

    totals = {"no_logic": 0, "trivial": 0, "has_logic": 0}
    for r in records:
        totals[r["category"]] += 1
    totals["total_methods"] = len(records)

    result["status"] = "measured"
    result["totals"] = totals
    result["methods"] = records
    return result


def write_model_metadata(model_dir: Path, result: dict) -> None:
    metadata_path = model_dir / METADATA_FILENAME
    data = {}
    if metadata_path.is_file():
        try:
            data = json.loads(metadata_path.read_text())
        except (json.JSONDecodeError, OSError):
            data = {}

    has_logic_methods = [
        {"class": m["class"], "method": m["method"], "statement_count": m["statement_count"]}
        for m in (result["methods"] or []) if m["category"] == "has_logic"
    ]
    data["method_logic_classification"] = {
        "checked_at": result["checked_at"],
        "python_version": result["python_version"],
        "status": result["status"],
        "totals": result["totals"],
        "has_logic_methods": has_logic_methods,
    }
    metadata_path.write_text(json.dumps(data, indent=2) + "\n")


_HAS_LOGIC_BUCKET_EDGES = [0, 5, 10, 20, 50, 100, 200, 10**9]
_HAS_LOGIC_BUCKET_LABELS = ["0", "1-5", "6-10", "11-20", "21-50", "51-100", "101-200", "200+"]
_TOTAL_METHODS_BUCKET_EDGES = [0, 10, 25, 50, 100, 200, 500, 10**9]
_TOTAL_METHODS_BUCKET_LABELS = ["0", "1-10", "11-25", "26-50", "51-100", "101-200", "201-500", "500+"]


def _bucket(n: int, edges: list[int], labels: list[str]) -> str:
    for edge, label in zip(edges, labels):
        if n <= edge:
            return label
    return labels[-1]


def _distribution(values: list[int], edges: list[int], labels: list[str]) -> dict:
    counts = {label: 0 for label in labels}
    for v in values:
        counts[_bucket(v, edges, labels)] += 1
    total = len(values) or 1
    return {
        "counts": counts,
        "percent": {label: round(count / total * 100, 2) for label, count in counts.items()},
    }


def build_report(results: list[dict]) -> dict:
    total = len(results)
    by_status: dict[str, int] = {}
    for r in results:
        by_status[r["status"]] = by_status.get(r["status"], 0) + 1

    measured = [r for r in results if r["status"] == "measured"]
    totals_sum = {"no_logic": 0, "trivial": 0, "has_logic": 0, "total_methods": 0}
    for r in measured:
        for k in totals_sum:
            totals_sum[k] += r["totals"][k]

    per_model_has_logic = sorted(
        ({"model": r["model"], "has_logic_methods": r["totals"]["has_logic"],
          "total_methods": r["totals"]["total_methods"]} for r in measured),
        key=lambda x: -x["has_logic_methods"],
    )
    models_with_has_logic = [m for m in per_model_has_logic if m["has_logic_methods"] > 0]
    models_with_no_has_logic = total - len(models_with_has_logic) - (total - len(measured))

    has_logic_counts = [r["totals"]["has_logic"] for r in measured]
    total_methods_counts = [r["totals"]["total_methods"] for r in measured]
    zero_hl_totals = [r["totals"]["total_methods"] for r in measured if r["totals"]["has_logic"] == 0]
    models_with_category = {
        cat: sum(1 for r in measured if r["totals"][cat] > 0)
        for cat in ("no_logic", "trivial", "has_logic")
    }

    def _mean(vals: list[int]) -> float | None:
        return round(sum(vals) / len(vals), 2) if vals else None

    def _median(vals: list[int]) -> float | None:
        if not vals:
            return None
        s = sorted(vals)
        mid = len(s) // 2
        return float(s[mid]) if len(s) % 2 else (s[mid - 1] + s[mid]) / 2

    return {
        "generated_at": datetime.datetime.now(datetime.timezone.utc).isoformat(),
        "total_models": total,
        "by_status": dict(sorted(by_status.items(), key=lambda kv: -kv[1])),
        "measured_count": len(measured),
        "totals_over_measured_models": totals_sum,
        "share": {
            k: round(totals_sum[k] / totals_sum["total_methods"], 4)
            for k in ("no_logic", "trivial", "has_logic")
        } if totals_sum["total_methods"] else None,
        "models_with_category": models_with_category,
        "models_with_at_least_one_has_logic_method": len(models_with_has_logic),
        "models_with_zero_has_logic_methods": models_with_no_has_logic,
        "per_model_stats": {
            "has_logic_mean": _mean(has_logic_counts),
            "has_logic_median": _median(has_logic_counts),
            "total_methods_mean": _mean(total_methods_counts),
            "total_methods_median": _median(total_methods_counts),
            "zero_has_logic_models_avg_total_methods": _mean(zero_hl_totals),
            "zero_has_logic_models_median_total_methods": _median(zero_hl_totals),
            "zero_has_logic_models_max_total_methods": max(zero_hl_totals) if zero_hl_totals else None,
        },
        "has_logic_count_distribution": _distribution(
            has_logic_counts, _HAS_LOGIC_BUCKET_EDGES, _HAS_LOGIC_BUCKET_LABELS),
        "total_methods_distribution": _distribution(
            total_methods_counts, _TOTAL_METHODS_BUCKET_EDGES, _TOTAL_METHODS_BUCKET_LABELS),
        "top_50_models_by_has_logic_method_count": per_model_has_logic[:50],
        # Deliberately excludes each result's full "methods" list (640k+
        # records dataset-wide) -- it would make this single report file
        # exceed GitHub's 100MB hard push limit for no benefit: the has_logic
        # methods are already written into each model's own code_metadata.json
        # (write_model_metadata()), and nothing downstream reads the full
        # per-method list from this aggregate report, only "totals".
        "results": sorted(
            ({k: v for k, v in r.items() if k != "methods"} for r in results),
            key=lambda r: r["model"],
        ),
    }


def render_markdown_report(report: dict) -> str:
    t = report["totals_over_measured_models"]
    s = report["share"] or {}
    lines = [
        "# Method Logic Classification Report (static, AST-based)",
        "",
        f"Generated: {report['generated_at']}",
        "",
        "Every method in every model's `python_code.py` classified as "
        "`no_logic` (empty/stub body), `trivial` (plain assignment/return/"
        "getter/setter, no branching or computation of any value), or "
        "`has_logic` (a loop, multi-branch conditional, `try`, `match`, "
        "comprehension, or arithmetic/boolean computation).",
        "",
        f"- **Total models:** {report['total_models']}",
        f"- **Measured:** {report['measured_count']}",
        "",
        "## Breakdown by status",
        "",
        "| Status | Count |",
        "|---|---|",
    ]
    for status, count in report["by_status"].items():
        lines.append(f"| {status} | {count} |")

    lines += [
        "",
        "## Method counts across all measured models",
        "",
        "| Category | Methods | Share of methods | Models with ≥1 such method | Share of models |",
        "|---|---|---|---|---|",
    ]
    mwc = report.get("models_with_category") or {}
    measured_n = report["measured_count"] or 1
    for cat in ("no_logic", "trivial", "has_logic"):
        m_count = mwc.get(cat, 0)
        lines.append(
            f"| {cat} | {t[cat]} | {s.get(cat, 0) * 100:.2f}% | {m_count} | "
            f"{m_count / measured_n * 100:.2f}% |"
        )
    lines += [
        f"| **Total methods** | **{t['total_methods']}** | | | |",
        "",
        f"**{report['models_with_at_least_one_has_logic_method']}** models have at least one "
        f"`has_logic` method (Phase 4's sample should be drawn from these). "
        f"**{report['models_with_zero_has_logic_methods']}** measured models have none at all "
        "-- every method is either a stub or a plain assignment/getter/setter, so no test-"
        "generation library targeting logic would have anything to work with there.",
        "",
        "## Per-model distribution: how many has_logic methods does a model have?",
        "",
        "| has_logic methods | Models | Share |",
        "|---|---|---|",
    ]
    hl_dist = report.get("has_logic_count_distribution")
    if hl_dist:
        for label, count in hl_dist["counts"].items():
            lines.append(f"| {label} | {count} | {hl_dist['percent'][label]}% |")
    ps = report.get("per_model_stats") or {}
    lines += [
        "",
        f"Mean has_logic methods/model: **{ps.get('has_logic_mean')}** "
        f"(median **{ps.get('has_logic_median')}**). Mean total methods/model: "
        f"**{ps.get('total_methods_mean')}** (median **{ps.get('total_methods_median')}**).",
        "",
        "## Per-model distribution: how many methods does a model have in total?",
        "",
        "| Total methods | Models | Share |",
        "|---|---|---|",
    ]
    tm_dist = report.get("total_methods_distribution")
    if tm_dist:
        for label, count in tm_dist["counts"].items():
            lines.append(f"| {label} | {count} | {tm_dist['percent'][label]}% |")
    lines += [
        "",
        f"Among the **{report['models_with_zero_has_logic_methods']}** models with zero "
        f"`has_logic` methods, average total method count is "
        f"**{ps.get('zero_has_logic_models_avg_total_methods')}** "
        f"(median **{ps.get('zero_has_logic_models_median_total_methods')}**, max "
        f"**{ps.get('zero_has_logic_models_max_total_methods')}**) -- these are consistently "
        "small models, not large models that merely happen to lack complex logic.",
        "",
        "## Top 50 models by has_logic method count",
        "",
        "| Model | has_logic methods | Total methods |",
        "|---|---|---|",
    ]
    for m in report["top_50_models_by_has_logic_method_count"]:
        lines.append(f"| {m['model']} | {m['has_logic_methods']} | {m['total_methods']} |")

    lines += [
        "",
        f"Per-model totals (no_logic/trivial/has_logic counts): see `{REPORT_BASENAME}.json`. "
        "Full per-method detail (which specific methods are has_logic) is written into each "
        "model's own `code_metadata.json` under the `method_logic_classification` key, not "
        "duplicated in this aggregate report.",
    ]
    return "\n".join(lines) + "\n"


def main() -> None:
    repo_root = Path(__file__).resolve().parent.parent
    parser = argparse.ArgumentParser(description=__doc__,
                                      formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--dataset-dir", type=Path, default=repo_root / "Dataset")
    parser.add_argument("--reports-dir", type=Path, default=repo_root / "reports")
    parser.add_argument("--models-file", type=Path, default=None,
                         help="Optional newline-separated model list (default: every model directory)")
    parser.add_argument("--workers", type=int, default=8)
    parser.add_argument("--limit", type=int, default=None)
    parser.add_argument("--write-metadata", action="store_true",
                         help="Write the method_logic_classification key into each model's "
                              "code_metadata.json (default: report only, dataset untouched)")
    args = parser.parse_args()

    model_dirs = find_model_dirs(args.dataset_dir, args.models_file, args.limit)
    total = len(model_dirs)
    mode = "writing metadata" if args.write_metadata else "dry run (reports only)"
    print(f"Classifying methods in {total} models from {args.dataset_dir} "
          f"with {args.workers} workers -- {mode}...")

    results: list[dict] = []
    with concurrent.futures.ProcessPoolExecutor(max_workers=args.workers) as executor:
        for done, result in enumerate(
            executor.map(validate_model, model_dirs, chunksize=32), start=1
        ):
            results.append(result)
            if done % 1000 == 0 or done == total:
                print(f"  {done}/{total} analysed")

    if args.write_metadata:
        written = 0
        for model_dir, result in zip(model_dirs, results):
            if result["status"] == "measured":
                write_model_metadata(model_dir, result)
                written += 1
        print(f"Wrote method_logic_classification into {written}/{total} code_metadata.json files.")

    report = build_report(results)
    args.reports_dir.mkdir(parents=True, exist_ok=True)
    (args.reports_dir / f"{REPORT_BASENAME}.json").write_text(json.dumps(report, indent=2) + "\n")
    (args.reports_dir / f"{REPORT_BASENAME}.md").write_text(render_markdown_report(report))

    t = report["totals_over_measured_models"]
    print(f"\nMeasured: {report['measured_count']}/{total}")
    print(f"no_logic={t['no_logic']}  trivial={t['trivial']}  has_logic={t['has_logic']}  "
          f"(total_methods={t['total_methods']})")
    print(f"Models with >=1 has_logic method: {report['models_with_at_least_one_has_logic_method']}")
    print(f"\nReports written to {args.reports_dir}")


if __name__ == "__main__":
    main()
