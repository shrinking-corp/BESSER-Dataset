#!/usr/bin/env python3
"""Generate `test_crosshair.py` per model using CrossHair (symbolic
execution), for the library track of the test-generation comparison.

Unlike Pynguin, CrossHair's `cover` command does NOT usefully enumerate
every class/function in a whole-file target -- confirmed empirically (see
docs/DECISIONS.md, 2026-10-01): pointing it at a whole module only ever
covered ONE representative method, regardless of time budget (a 300s run
finished on its own in 6s with the identical single result -- not a timeout
problem). The fix found: **invoke CrossHair once per class**, using tree-
sitter's `code_structure.json` (already available full-dataset) as the
class list, since that's independent of this project's own BUML/AST
tooling and reflects what's actually in the generated code.

Per-class invocation is also unreliable on its own, tolerated here rather
than treated as an error:
  - A class with no real `__init__` of its own (only inherited) makes
    CrossHair exit non-zero with "No functions or methods found" --
    confirmed on `model_1`'s `petrinet_Arc`. Skipped, not a failure.
  - A class with ONLY `@property`-decorated methods produces zero test
    output (CrossHair's target lookup cannot resolve a property descriptor
    to a plain callable at all -- confirmed on `model_1`'s `petrinet_Node.name`
    getter, a hard capability gap, not a tuning issue). Skipped, not a
    failure -- this means CrossHair contributes nothing for this dataset's
    getter/setter-heavy bulk, only for classes with real "operation" methods.
  - Each class invocation gets its own timeout; one slow/hanging class does
    not abort the rest of the model's classes.

Per-class outputs (each already valid standalone pytest-style code, with
its own `from python_code import X` lines) are concatenated as-is --
duplicate imports across classes are harmless in Python, same reasoning
`generate_combined_tests.py` already relies on for module-level redefinition
safety.

Usage:
    python scripts/generate_crosshair_tests.py --models-file PATH [--workers N]
        [--dataset-dir PATH] [--reports-dir PATH] [--report-name NAME]
        [--per-class-timeout SECONDS] [--per-condition-timeout SECONDS]
        [--crosshair-python PATH] [--limit N] [--fresh]
"""
from __future__ import annotations

import argparse
import datetime
import json
import os
import platform
import shutil
import subprocess
import sys
import tempfile
import time
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from _common.cache import load_cache, partition_cache  # noqa: E402
from _common.crosshair import sanitize_crosshair_tests  # noqa: E402
from _common.io import add_common_io_args, find_model_dirs  # noqa: E402
from _common.pool import run_models  # noqa: E402
from _common.report import render_status_table, write_reports  # noqa: E402

SOURCE_FILENAME = "python_code.py"
CODE_STRUCTURE_FILENAME = "code_structure.json"
OUTPUT_TEST_FILENAME = "test_crosshair.py"
DEFAULT_PER_CLASS_TIMEOUT = 30
DEFAULT_PER_CONDITION_TIMEOUT = 5.0
# Cached results with one of these statuses are automatically re-attempted
# on the next run under the SAME --report-name -- same fix as
# validate_mutation.py/validate_mutation_properties.py (2026-10-01).
# "missing_file"/"missing_code_structure"/"code_structure_parse_error"/
# "no_classes" are excluded: permanent facts about the model's input data,
# not transient failures a re-run would fix.
RETRIABLE_STATUSES = frozenset({"no_tests_generated", "error"})


def default_crosshair_python(repo_root: Path) -> Path:
    name = "python.exe" if platform.system() == "Windows" else "python"
    return repo_root / ".venv-testgen" / ("Scripts" if platform.system() == "Windows" else "bin") / name


def class_names_from_structure(code_structure_path: Path) -> list[str]:
    data = json.loads(code_structure_path.read_text(encoding="utf-8"))
    return [c["name"] for c in data.get("classes", [])]


def cover_one_class(
    crosshair_python: str, proj_dir: Path, class_name: str,
    per_class_timeout: int, per_condition_timeout: float, env: dict,
) -> dict:
    """Returns {"class": ..., "status": ..., "test_text": str|None, "error_message": ...}.

    Invokes `python -m crosshair`, NOT the `crosshair`/`crosshair.exe`
    console-script wrapper directly. Found 2026-10-01: Windows console-
    script launchers (created by pip/distlib) bake in the venv's absolute
    path at install time -- renaming `.venv-phase4` to `.venv-testgen`
    silently broke `crosshair.exe` (exit 1, no output, no error at all),
    which made a full 200-model batch run report 0 classes covered on
    every single model. `python -m crosshair` has no such dependency on a
    fixed path and is exactly how generate_pynguin_tests.py already invokes
    Pynguin (`-m pynguin`, never a console-script wrapper) -- same fix,
    applied here for the same reason.
    """
    result = {"class": class_name, "status": "error", "test_text": None, "error_message": None}
    try:
        proc = subprocess.run(
            [crosshair_python, "-m", "crosshair", "cover", f"python_code.{class_name}",
             "--example_output_format", "pytest",
             "--per_condition_timeout", str(per_condition_timeout)],
            cwd=str(proj_dir), capture_output=True, text=True, timeout=per_class_timeout, env=env,
        )
    except subprocess.TimeoutExpired:
        result["status"] = "timeout"
        result["error_message"] = f"exceeded {per_class_timeout}s"
        return result

    stdout = (proc.stdout or "").strip()
    if proc.returncode != 0:
        # Confirmed real case: "No functions or methods found" for a class
        # with no own __init__ (only inherited) -- not an error worth
        # surfacing loudly, just means nothing to generate for this class.
        result["status"] = "no_target"
        result["error_message"] = (proc.stderr or stdout or "").strip()[-500:]
        return result

    if not stdout or "def test_" not in stdout:
        # Confirmed real case: a class whose only members are @property
        # getters/setters -- CrossHair's target lookup cannot resolve a
        # property descriptor to a plain callable, so it silently finds
        # nothing. Not an error, just nothing usable for this class.
        result["status"] = "no_coverable_target"
        return result

    result["status"] = "covered"
    result["test_text"] = stdout
    return result


def generate_model(
    model_dir: Path, crosshair_python: str, per_class_timeout: int,
    per_condition_timeout: float, overall_timeout: int,
) -> dict:
    checked_at = datetime.datetime.now(datetime.timezone.utc).isoformat()
    result = {
        "model": model_dir.name,
        "checked_at": checked_at,
        "python_version": platform.python_version(),
        "status": "missing_file",
        "classes_total": None,
        "classes_covered": None,
        "tests_written": None,
        "per_class_status": None,
        "error_message": None,
    }

    source_path = model_dir / SOURCE_FILENAME
    structure_path = model_dir / CODE_STRUCTURE_FILENAME
    if not source_path.is_file():
        result["error_message"] = f"{SOURCE_FILENAME} not found"
        return result
    if not structure_path.is_file():
        result["status"] = "missing_code_structure"
        result["error_message"] = f"{CODE_STRUCTURE_FILENAME} not found"
        return result

    try:
        class_names = class_names_from_structure(structure_path)
    except Exception as exc:
        result["status"] = "code_structure_parse_error"
        result["error_message"] = str(exc)
        return result

    result["classes_total"] = len(class_names)
    if not class_names:
        result["status"] = "no_classes"
        return result

    scratch_root = tempfile.mkdtemp(prefix=f"crosshair_{model_dir.name}_")
    try:
        proj_dir = Path(scratch_root)
        shutil.copy2(source_path, proj_dir / SOURCE_FILENAME)

        env = dict(os.environ)
        env["PYTHONDONTWRITEBYTECODE"] = "1"

        per_class_status: dict[str, str] = {}
        covered_texts: list[str] = []
        stdlib_tests_dropped = 0
        start = time.monotonic()
        for class_name in sorted(class_names):
            if time.monotonic() - start > overall_timeout:
                per_class_status[class_name] = "skipped_overall_timeout"
                continue
            outcome = cover_one_class(crosshair_python, proj_dir, class_name,
                                       per_class_timeout, per_condition_timeout, env)
            per_class_status[class_name] = outcome["status"]
            if outcome["test_text"]:
                sanitized, dropped = sanitize_crosshair_tests(outcome["test_text"])
                if sanitized is None:
                    per_class_status[class_name] = "invalid_syntax"
                    continue
                stdlib_tests_dropped += len(dropped)
                if "def test_" in sanitized:
                    covered_texts.append(sanitized)

        result["per_class_status"] = per_class_status
        result["stdlib_tests_dropped"] = stdlib_tests_dropped
        result["classes_covered"] = sum(1 for s in per_class_status.values() if s == "covered")

        if not covered_texts:
            result["status"] = "no_tests_generated"
            return result

        merged_text = "\n\n".join(covered_texts) + "\n"
        (model_dir / OUTPUT_TEST_FILENAME).write_text(merged_text, encoding="utf-8")
        result["status"] = "generated"
        result["tests_written"] = merged_text.count("\ndef test_") + (1 if merged_text.startswith("def test_") else 0)
        return result
    except Exception as exc:
        result["status"] = "error"
        result["error_message"] = str(exc)
        return result
    finally:
        shutil.rmtree(scratch_root, ignore_errors=True)


def build_report(results: list[dict]) -> dict:
    total = len(results)
    by_status: dict[str, int] = {}
    for r in results:
        by_status[r["status"]] = by_status.get(r["status"], 0) + 1
    generated = [r for r in results if r["status"] == "generated"]

    per_class_status_totals: dict[str, int] = {}
    for r in results:
        for s in (r.get("per_class_status") or {}).values():
            per_class_status_totals[s] = per_class_status_totals.get(s, 0) + 1

    return {
        "generated_at": datetime.datetime.now(datetime.timezone.utc).isoformat(),
        "total_models": total,
        "by_status": dict(sorted(by_status.items(), key=lambda kv: -kv[1])),
        "generated_count": len(generated),
        "avg_tests_per_model": round(sum(r["tests_written"] or 0 for r in generated) / len(generated), 2) if generated else None,
        "total_classes_seen": sum(r["classes_total"] or 0 for r in results),
        "total_classes_covered": sum(r["classes_covered"] or 0 for r in results),
        "per_class_status_totals": dict(sorted(per_class_status_totals.items(), key=lambda kv: -kv[1])),
        "results": results,
    }


def render_markdown_report(report: dict) -> str:
    lines = [
        "# CrossHair Test Generation Report",
        "",
        f"Generated: {report['generated_at']}",
        "",
        f"- **Total models:** {report['total_models']}",
        f"- **Generated (>=1 class covered):** {report['generated_count']}",
        f"- **Avg tests per model (generated only):** {report['avg_tests_per_model']}",
        f"- **Total classes seen:** {report['total_classes_seen']}",
        f"- **Total classes covered:** {report['total_classes_covered']} "
        f"({round(report['total_classes_covered']/report['total_classes_seen']*100, 2) if report['total_classes_seen'] else 0}%)",
        "",
        "## Per-class outcome totals (across all models)",
        "",
        "| Outcome | Count |",
        "|---|---|",
    ]
    for status, count in report["per_class_status_totals"].items():
        lines.append(f"| {status} | {count} |")
    lines.append("")
    lines += render_status_table(report["by_status"])
    lines +=["", "Full per-model, per-class detail: see the accompanying `.json` report."]
    return "\n".join(lines) + "\n"


def main() -> None:
    repo_root = Path(__file__).resolve().parent.parent
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    add_common_io_args(parser, __file__)
    parser.add_argument("--models-file", type=Path, default=None)
    parser.add_argument("--report-name", type=str, default="crosshair_generation_report")
    parser.add_argument("--workers", type=int, default=4)
    parser.add_argument("--per-class-timeout", type=int, default=DEFAULT_PER_CLASS_TIMEOUT)
    parser.add_argument("--per-condition-timeout", type=float, default=DEFAULT_PER_CONDITION_TIMEOUT)
    parser.add_argument("--overall-timeout", type=int, default=300,
                         help="Wall-clock cap across all of one model's classes combined")
    parser.add_argument("--crosshair-python", type=str, default=None,
                         help="Path to the .venv-testgen interpreter crosshair-tool is installed in "
                              "(default: <repo>/.venv-testgen/Scripts/python.exe). Invoked as "
                              "`python -m crosshair`, NOT the crosshair/crosshair.exe console-script "
                              "wrapper -- that wrapper bakes in the venv's absolute path at install "
                              "time and silently breaks if the venv directory is ever renamed/moved "
                              "(confirmed 2026-10-01: exit 1, no output, no error at all).")
    parser.add_argument("--limit", type=int, default=None)
    parser.add_argument("--fresh", action="store_true", help="Ignore any existing cache and recompute everything")
    args = parser.parse_args()

    crosshair_python = args.crosshair_python or str(default_crosshair_python(repo_root))
    if not Path(crosshair_python).is_file():
        parser.error(f"crosshair interpreter not found at {crosshair_python!r} -- pass --crosshair-python "
                      f"explicitly, or install crosshair-tool into .venv-testgen first")

    args.reports_dir.mkdir(parents=True, exist_ok=True)
    cache_path = args.reports_dir / f"{args.report_name}.cache.jsonl"
    cached_results_all: dict[str, dict] = {} if args.fresh else load_cache(cache_path)
    if args.fresh and cache_path.is_file():
        cache_path.unlink()
    cached_results, retriable = partition_cache(cached_results_all, RETRIABLE_STATUSES)

    all_model_dirs = find_model_dirs(args.dataset_dir, args.models_file, args.limit)
    total = len(all_model_dirs)
    model_dirs = [d for d in all_model_dirs if d.name not in cached_results]
    skipped = total - len(model_dirs)

    print(f"Generating CrossHair tests for {total} models with {args.workers} workers "
          f"(per-class timeout={args.per_class_timeout}s, overall cap={args.overall_timeout}s/model)...")
    if skipped:
        print(f"Resuming from cache: {skipped}/{total} already done, {len(model_dirs)} remaining "
              f"(pass --fresh to ignore the cache and recompute everything)")
    if retriable:
        print(f"Auto-retrying {len(retriable)} previously-failed models from the cache -- "
              f"same report, no separate retry run needed")

    results = run_models(
        generate_model, model_dirs,
        worker_args=(crosshair_python, args.per_class_timeout, args.per_condition_timeout, args.overall_timeout),
        workers=args.workers, cache_path=cache_path, results=list(cached_results.values()),
        already_done=skipped, total=total,
        describe=lambda r: f" ({r.get('classes_covered')}/{r.get('classes_total')} classes)",
        error_fields={"classes_total": None, "classes_covered": None, "tests_written": None,
                      "per_class_status": None},
    )

    report = build_report(results)
    json_path, md_path = write_reports(args.reports_dir, args.report_name, report, render_markdown_report(report))

    print()
    print(f"Generated: {report['generated_count']}/{report['total_models']}")
    print(f"Classes covered: {report['total_classes_covered']}/{report['total_classes_seen']}")
    print(f"Report written to {json_path} and {md_path}")


if __name__ == "__main__":
    main()
