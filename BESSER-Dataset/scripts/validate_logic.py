#!/usr/bin/env python3
"""Detect model directories whose `python_code.py` contains no testable logic.

Coverage and mutation testing are both blind to this class of model: a file
made only of `class X: pass` declarations scores **100% line coverage** (every
statement is a class header or a `pass`, and importing the module executes all
of them) and produces **zero mutants** (there is no operator, literal or
branch to mutate). Both metrics therefore look *perfect* precisely where there
is nothing to measure, so neither can be used to find these models -- they have
to be detected statically, from the code itself.

This script parses each model's `python_code.py` with `ast` (no execution) and
classifies it. The result is written into the model's `code_metadata.json`
under a `logic_validation` key, and an aggregate report plus a plain-text
exclusion list are written to `reports/`.

Usage:
    python scripts/validate_logic.py [--write-metadata] [--workers N]
                                     [--dataset-dir PATH] [--reports-dir PATH]
                                     [--limit N]

Without `--write-metadata` the script only writes the reports (dry run), so the
classification can be inspected before it is committed to the dataset.

Each model's `code_metadata.json` gets (or has updated) a top-level
"logic_validation" key:

    {
      "logic_validation": {
        "file": "python_code.py",
        "checked_at": "2026-09-10T12:00:00+00:00",
        "python_version": "3.13.5",
        "status": "no_logic",     # has_logic | no_logic | syntax_error
                                  # | empty_file | missing_file
        "usable": false,          # false => do not use this model for
                                  #          coverage / mutation experiments
        "exclude_reason": "...",  # null when usable
        "all_operations_stubbed": false,
        "metrics": { ... }
      }
    }

Existing keys in code_metadata.json are preserved; only "logic_validation" is
added/overwritten.
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
REPORT_BASENAME = "logic_validation_report"
EXCLUSION_BASENAME = "excluded_models_no_logic.txt"

# Statuses for which `usable` is False.
UNUSABLE_STATUSES = {"no_logic", "syntax_error", "empty_file", "missing_file"}


def find_model_dirs(dataset_dir: Path) -> list[Path]:
    return sorted(p for p in dataset_dir.iterdir() if p.is_dir())


def _decorator_names(node: ast.FunctionDef | ast.AsyncFunctionDef) -> list[str]:
    """Names of a function's decorators, e.g. ['property'] or ['setter']."""
    names = []
    for dec in node.decorator_list:
        if isinstance(dec, ast.Name):
            names.append(dec.id)
        elif isinstance(dec, ast.Attribute):
            names.append(dec.attr)  # `@name.setter` -> "setter"
    return names


def _is_docstring(node: ast.stmt) -> bool:
    return isinstance(node, ast.Expr) and isinstance(node.value, ast.Constant) \
        and isinstance(node.value.value, str)


def _is_stub_body(body: list[ast.stmt]) -> bool:
    """True when a body carries no logic: only `pass`, `...` and/or a docstring.

    The generated code uses a bare `pass` (see docs/DECISIONS.md, 2026-09-02);
    `...` and docstring-only bodies are accepted too so the definition does not
    silently miss a future generator change.
    """
    meaningful = [n for n in body if not _is_docstring(n)]
    if not meaningful:
        return True
    return all(
        isinstance(n, ast.Pass)
        or (isinstance(n, ast.Expr) and isinstance(n.value, ast.Constant)
            and n.value.value is Ellipsis)
        for n in meaningful
    )


# Statements that introduce control flow -- the substrate mutation testing
# actually mutates (conditions, loop bounds, exception paths).
BRANCH_NODES = (ast.If, ast.For, ast.AsyncFor, ast.While, ast.Try,
                ast.IfExp, ast.Assert, ast.Match)


def _is_enum_class(node: ast.ClassDef) -> bool:
    for base in node.bases:
        name = base.id if isinstance(base, ast.Name) else \
            base.attr if isinstance(base, ast.Attribute) else None
        if name in ("Enum", "IntEnum", "StrEnum", "Flag", "IntFlag"):
            return True
    return False


def analyse_source(source: str) -> tuple[ast.Module | None, dict, str | None]:
    """Parse `source` and count its logic-bearing constructs.

    Returns (tree, metrics, syntax_error_message).
    """
    metrics = {
        "classes": 0,
        "empty_classes": 0,       # `class X: pass` -- no members at all
        "enum_classes": 0,
        "init_methods": 0,
        "property_getters": 0,
        "property_setters": 0,
        "operations": 0,          # plain methods == B-UML operations
        "empty_operations": 0,    # operations whose body is just `pass`
        "logic_statements": 0,    # statements inside function bodies, minus stubs
        "branch_statements": 0,   # of those, ones introducing control flow
    }

    try:
        tree = ast.parse(source)
    except SyntaxError as exc:
        return None, metrics, f"{exc.msg} (line {exc.lineno})"

    for node in ast.walk(tree):
        if not isinstance(node, ast.ClassDef):
            continue
        metrics["classes"] += 1
        if _is_enum_class(node):
            metrics["enum_classes"] += 1
        if _is_stub_body(node.body):
            metrics["empty_classes"] += 1
            continue

        for member in node.body:
            if not isinstance(member, (ast.FunctionDef, ast.AsyncFunctionDef)):
                continue
            decorators = _decorator_names(member)
            if member.name == "__init__":
                metrics["init_methods"] += 1
            elif "property" in decorators:
                metrics["property_getters"] += 1
            elif "setter" in decorators:
                metrics["property_setters"] += 1
            else:
                metrics["operations"] += 1
                if _is_stub_body(member.body):
                    metrics["empty_operations"] += 1

            for sub in ast.walk(member):
                if sub is member or not isinstance(sub, ast.stmt):
                    continue
                if isinstance(sub, ast.Pass) or _is_docstring(sub):
                    continue
                metrics["logic_statements"] += 1
            for sub in ast.walk(member):
                if sub is not member and isinstance(sub, BRANCH_NODES):
                    metrics["branch_statements"] += 1

    return tree, metrics, None


def classify(metrics: dict) -> tuple[str, str | None]:
    """Map metrics onto a (status, exclude_reason) pair for a parseable file."""
    if metrics["logic_statements"] == 0:
        if metrics["classes"] == 0:
            reason = (f"{CODE_FILENAME} declares no classes at all "
                      f"(imports/comments only) -- nothing to test")
        elif metrics["empty_classes"] == metrics["classes"]:
            reason = (f"all {metrics['classes']} classes are declaration-only "
                      f"(`class X: pass`) -- no executable statement anywhere")
        else:
            reason = (f"{metrics['classes']} classes but every method body is a "
                      f"stub -- no executable statement anywhere")
        return "no_logic", reason
    return "has_logic", None


def validate_model(model_dir: Path) -> dict:
    code_path = model_dir / CODE_FILENAME
    result = {
        "model": model_dir.name,
        "file": CODE_FILENAME,
        "checked_at": datetime.datetime.now(datetime.timezone.utc).isoformat(),
        "python_version": platform.python_version(),
        "status": "missing_file",
        "usable": False,
        "exclude_reason": f"{CODE_FILENAME} is missing",
        "all_operations_stubbed": False,
        "metrics": None,
    }

    if not code_path.is_file():
        return result

    try:
        source = code_path.read_text(encoding="utf-8", errors="replace")
    except OSError as exc:
        result["status"] = "missing_file"
        result["exclude_reason"] = f"{CODE_FILENAME} could not be read: {exc}"
        return result

    if not source.strip():
        result["status"] = "empty_file"
        result["exclude_reason"] = f"{CODE_FILENAME} is empty"
        return result

    _tree, metrics, syntax_error = analyse_source(source)
    result["metrics"] = metrics

    if syntax_error is not None:
        result["status"] = "syntax_error"
        result["exclude_reason"] = f"{CODE_FILENAME} does not parse: {syntax_error}"
        return result

    status, reason = classify(metrics)
    result["status"] = status
    result["usable"] = status not in UNUSABLE_STATUSES
    result["exclude_reason"] = reason
    result["all_operations_stubbed"] = (
        metrics["operations"] > 0
        and metrics["operations"] == metrics["empty_operations"]
    )
    return result


def write_model_metadata(model_dir: Path, validation: dict) -> None:
    metadata_path = model_dir / METADATA_FILENAME
    data = {}
    if metadata_path.is_file():
        try:
            data = json.loads(metadata_path.read_text())
        except (json.JSONDecodeError, OSError):
            data = {}

    data["logic_validation"] = {k: v for k, v in validation.items() if k != "model"}
    metadata_path.write_text(json.dumps(data, indent=2) + "\n")


def build_report(results: list[dict]) -> dict:
    total = len(results)
    by_status: dict[str, int] = {}
    excluded = []
    for r in results:
        by_status[r["status"]] = by_status.get(r["status"], 0) + 1
        if not r["usable"]:
            excluded.append({
                "model": r["model"],
                "status": r["status"],
                "exclude_reason": r["exclude_reason"],
                "classes": (r["metrics"] or {}).get("classes"),
            })

    usable = total - len(excluded)
    stubbed = [r["model"] for r in results if r["all_operations_stubbed"]]
    measured = [r for r in results if r["metrics"] and r["status"] == "has_logic"]

    return {
        "generated_at": datetime.datetime.now(datetime.timezone.utc).isoformat(),
        "total_models": total,
        "usable": usable,
        "excluded": len(excluded),
        "usable_rate": round(usable / total, 4) if total else None,
        "by_status": dict(sorted(by_status.items(), key=lambda kv: -kv[1])),
        "all_operations_stubbed_count": len(stubbed),
        "totals_over_usable_models": {
            "classes": sum(r["metrics"]["classes"] for r in measured),
            "logic_statements": sum(r["metrics"]["logic_statements"] for r in measured),
            "branch_statements": sum(r["metrics"]["branch_statements"] for r in measured),
            "operations": sum(r["metrics"]["operations"] for r in measured),
            "empty_operations": sum(r["metrics"]["empty_operations"] for r in measured),
        },
        "all_operations_stubbed_models": sorted(stubbed),
        "excluded_models": sorted(excluded, key=lambda m: m["model"]),
        "results": sorted(results, key=lambda r: r["model"]),
    }


def render_markdown_report(report: dict) -> str:
    t = report["totals_over_usable_models"]
    lines = [
        "# Logic Validation Report (static, AST-based)",
        "",
        f"Generated: {report['generated_at']}",
        "",
        f"- **Total models checked:** {report['total_models']}",
        f"- **Usable (contain testable logic):** {report['usable']}",
        f"- **Excluded (no testable logic / unreadable):** {report['excluded']}",
    ]
    if report["usable_rate"] is not None:
        lines.append(f"- **Usable rate:** {report['usable_rate'] * 100:.2f}%")
    lines += [
        "",
        "## Breakdown by status",
        "",
        "| Status | Usable | Count |",
        "|---|---|---|",
    ]
    for status, count in report["by_status"].items():
        lines.append(f"| {status} | {'no' if status in UNUSABLE_STATUSES else 'yes'} | {count} |")

    lines += [
        "",
        "## Logic present in the usable models",
        "",
        "| Metric | Total |",
        "|---|---|",
        f"| Classes | {t['classes']} |",
        f"| Statements inside method bodies | {t['logic_statements']} |",
        f"| ...of which introduce control flow | {t['branch_statements']} |",
        f"| Operations (B-UML methods) | {t['operations']} |",
        f"| ...of which are `pass` stubs | {t['empty_operations']} |",
        "",
        f"**{report['all_operations_stubbed_count']}** usable models have at least one "
        "operation and *every* one of them is a `pass` stub. These are still usable "
        "(their property setters carry real association logic) but their operations "
        "contribute nothing to a mutation score -- see `all_operations_stubbed` in "
        "each model's metadata.",
        "",
        f"Excluded models are listed one per line in `{EXCLUSION_BASENAME}`.",
        f"Full per-model detail: see `{REPORT_BASENAME}.json` and each model's "
        "`code_metadata.json`.",
    ]
    return "\n".join(lines) + "\n"


def main() -> None:
    repo_root = Path(__file__).resolve().parent.parent
    parser = argparse.ArgumentParser(description=__doc__,
                                     formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--dataset-dir", type=Path, default=repo_root / "Dataset",
                        help="Path to the Dataset directory (default: <repo>/Dataset)")
    parser.add_argument("--reports-dir", type=Path, default=repo_root / "reports",
                        help="Where to write the aggregate report (default: <repo>/reports)")
    parser.add_argument("--workers", type=int, default=8, help="Parallel worker processes")
    parser.add_argument("--limit", type=int, default=None,
                        help="Only process the first N models (for testing)")
    parser.add_argument("--write-metadata", action="store_true",
                        help="Write the logic_validation key into each model's "
                             "code_metadata.json (default: report only, dataset untouched)")
    args = parser.parse_args()

    model_dirs = find_model_dirs(args.dataset_dir)
    if args.limit:
        model_dirs = model_dirs[: args.limit]

    total = len(model_dirs)
    mode = "writing metadata" if args.write_metadata else "dry run (reports only)"
    print(f"Analysing {total} models from {args.dataset_dir} "
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
        for model_dir, result in zip(model_dirs, results):
            write_model_metadata(model_dir, result)
        print(f"Wrote logic_validation into {total} code_metadata.json files.")

    report = build_report(results)
    args.reports_dir.mkdir(parents=True, exist_ok=True)
    (args.reports_dir / f"{REPORT_BASENAME}.json").write_text(
        json.dumps(report, indent=2) + "\n")
    (args.reports_dir / f"{REPORT_BASENAME}.md").write_text(
        render_markdown_report(report))
    (args.reports_dir / EXCLUSION_BASENAME).write_text(
        "".join(f"{m['model']}\n" for m in report["excluded_models"]))

    print(f"\nUsable: {report['usable']}/{total} "
          f"({(report['usable_rate'] or 0) * 100:.2f}%)  |  "
          f"Excluded: {report['excluded']}")
    for status, count in report["by_status"].items():
        print(f"  {status:16s} {count}")
    print(f"\nReports written to {args.reports_dir}")


if __name__ == "__main__":
    main()
