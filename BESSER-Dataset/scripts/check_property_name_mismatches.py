#!/usr/bin/env python3
"""Audit every model's python_code.py for a specific, silent code-generation
defect: a `@X.setter`-decorated function whose own `def` name doesn't
actually match `X`.

Why this matters: `@X.setter` only works correctly by *convention* -- the
decorator returns a new property object (getter + the new setter), and that
object gets bound to whichever name the immediately-following `def` uses,
which is supposed to be the same `X`. Python does not enforce or even check
this; `@class2.setter\ndef class1(self, value): ...` is completely legal
syntax that silently creates a SEPARATE class attribute named `class1`
instead of attaching the setter to `class2` -- no error, no warning, just
quietly wrong behavior (the property ends up read-only in practice, and an
oddly-named extra attribute appears alongside it).

This is a real, found-in-the-wild defect: confirmed in model_10001058's
`result` class (the same file fixed for a *different*, load-blocking bug --
`docs/DECISIONS.md`-adjacent session notes). That one was found by accident
while reading the file for something else, not because anything was
checking for this pattern. This script exists to find out how many more
exist, dataset-wide, since nothing else in this pipeline would ever surface
one -- it doesn't prevent loading, so the exhaustive load-check every other
script's error-handling relies on (see generate_structural_tests.py) can't
catch it.

This is a READ-ONLY audit. It never modifies any file -- it only reports
findings, so a fix (if any are found and worth fixing) is a separate,
deliberate follow-up, not something this script does automatically.

Usage:
    python scripts/check_property_name_mismatches.py [--models-file PATH]
        [--dataset-dir PATH] [--reports-dir PATH] [--report-name NAME]
        [--limit N]
"""
from __future__ import annotations

import argparse
import ast
import datetime
import json
from pathlib import Path

SOURCE_FILENAME = "python_code.py"


def find_model_dirs(dataset_dir: Path, models_file: Path | None, limit: int | None) -> list[Path]:
    if models_file:
        names = [l.strip() for l in models_file.read_text().splitlines() if l.strip()]
        dirs = [dataset_dir / name for name in names]
    else:
        dirs = sorted(p for p in dataset_dir.iterdir() if p.is_dir())
    if limit:
        dirs = dirs[:limit]
    return dirs


def _decorator_setter_target(decorator: ast.expr) -> str | None:
    """If `decorator` is `<name>.setter` or `<name>.deleter`, return <name>."""
    if (
        isinstance(decorator, ast.Attribute)
        and decorator.attr in ("setter", "deleter")
        and isinstance(decorator.value, ast.Name)
    ):
        return decorator.value.id
    return None


def find_mismatches(source_path: Path) -> list[dict]:
    """Every @X.setter / @X.deleter whose decorated function isn't named X."""
    # encoding="utf-8" is required, not cosmetic: Path.read_text() otherwise
    # falls back to the OS locale encoding (not UTF-8 on Windows), which
    # mangles multi-byte characters and raises a false "invalid character"
    # SyntaxError -- same bug, same 4 models (model_2210/2213/2243/2246), as
    # validate_coverage_structural.py's function_ranges().
    tree = ast.parse(source_path.read_text(encoding="utf-8"))
    mismatches: list[dict] = []

    class _ClassWalker(ast.NodeVisitor):
        def visit_ClassDef(self, node: ast.ClassDef) -> None:
            for item in node.body:
                if not isinstance(item, (ast.FunctionDef, ast.AsyncFunctionDef)):
                    continue
                for deco in item.decorator_list:
                    target = _decorator_setter_target(deco)
                    if target is not None and target != item.name:
                        mismatches.append({
                            "class": node.name,
                            "expected_name": target,
                            "actual_def_name": item.name,
                            "decorator_kind": deco.attr,
                            "lineno": item.lineno,
                        })
            self.generic_visit(node)

    _ClassWalker().visit(tree)
    return mismatches


def check_model(model_dir: Path) -> dict:
    checked_at = datetime.datetime.now(datetime.timezone.utc).isoformat()
    result = {
        "model": model_dir.name,
        "checked_at": checked_at,
        "status": "missing_file",
        "mismatches": [],
        "error_message": None,
    }

    source_path = model_dir / SOURCE_FILENAME
    if not source_path.is_file():
        result["error_message"] = f"{SOURCE_FILENAME} not found"
        return result

    try:
        result["mismatches"] = find_mismatches(source_path)
        result["status"] = "checked"
    except SyntaxError as exc:
        result["status"] = "parse_error"
        result["error_message"] = str(exc)

    return result


def build_report(results: list[dict]) -> dict:
    total = len(results)
    by_status: dict[str, int] = {}
    for r in results:
        by_status[r["status"]] = by_status.get(r["status"], 0) + 1

    models_with_mismatches = [r for r in results if r["mismatches"]]
    total_mismatches = sum(len(r["mismatches"]) for r in results)

    return {
        "generated_at": datetime.datetime.now(datetime.timezone.utc).isoformat(),
        "total_models": total,
        "by_status": by_status,
        "models_with_mismatches": len(models_with_mismatches),
        "total_mismatches": total_mismatches,
        "results": [r for r in results if r["mismatches"] or r["status"] != "checked"],
    }


def render_markdown_report(report: dict) -> str:
    lines = [
        "# Property Setter/Deleter Name-Mismatch Audit",
        "",
        f"Generated: {report['generated_at']}",
        "",
        "Read-only audit for `@X.setter`/`@X.deleter` decorators whose "
        "decorated function isn't actually named X -- a silent defect that "
        "doesn't prevent loading, so nothing else in this pipeline would "
        "otherwise catch it. See the script's docstring for the confirmed "
        "real-world example this was built to hunt for.",
        "",
        f"- **Total models checked:** {report['total_models']}",
        f"- **Models with at least one mismatch:** {report['models_with_mismatches']}",
        f"- **Total mismatches found:** {report['total_mismatches']}",
        "",
        "## Breakdown by status",
        "",
        "| Status | Count |",
        "|---|---|",
    ]
    for status, count in sorted(report["by_status"].items(), key=lambda kv: -kv[1]):
        lines.append(f"| {status} | {count} |")
    lines += [
        "",
        "## Models with mismatches",
        "",
        "| Model | Class | Expected | Actual def name | Kind | Line |",
        "|---|---|---|---|---|---|",
    ]
    for r in report["results"]:
        for m in r["mismatches"]:
            lines.append(
                f"| {r['model']} | {m['class']} | {m['expected_name']} | "
                f"{m['actual_def_name']} | {m['decorator_kind']} | {m['lineno']} |"
            )
    lines += ["", "Full per-model detail: see the accompanying `.json` report."]
    return "\n".join(lines) + "\n"


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument(
        "--dataset-dir", type=Path,
        default=Path(__file__).resolve().parent.parent / "Dataset",
    )
    parser.add_argument(
        "--reports-dir", type=Path,
        default=Path(__file__).resolve().parent.parent / "reports",
    )
    parser.add_argument("--models-file", type=Path, default=None)
    parser.add_argument("--report-name", type=str, default="property_name_mismatch_report")
    parser.add_argument("--limit", type=int, default=None)
    args = parser.parse_args()

    model_dirs = find_model_dirs(args.dataset_dir, args.models_file, args.limit)
    total = len(model_dirs)
    print(f"Scanning {total} models for property setter/deleter name mismatches...")

    results: list[dict] = []
    for i, model_dir in enumerate(model_dirs, start=1):
        result = check_model(model_dir)
        results.append(result)
        if result["mismatches"]:
            print(f"  {i}/{total}: {model_dir.name} -> {len(result['mismatches'])} mismatch(es)", flush=True)
        elif i % 500 == 0 or i == total:
            print(f"  {i}/{total} scanned...", flush=True)

    report = build_report(results)
    args.reports_dir.mkdir(parents=True, exist_ok=True)
    json_path = args.reports_dir / f"{args.report_name}.json"
    json_path.write_text(json.dumps(report, indent=2) + "\n")
    md_path = args.reports_dir / f"{args.report_name}.md"
    md_path.write_text(render_markdown_report(report))

    print()
    print(f"Models with mismatches: {report['models_with_mismatches']}/{report['total_models']}")
    print(f"Total mismatches found: {report['total_mismatches']}")
    print(f"Report written to {json_path} and {md_path}")


if __name__ == "__main__":
    main()
