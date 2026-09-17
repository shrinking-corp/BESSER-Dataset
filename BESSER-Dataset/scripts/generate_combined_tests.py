#!/usr/bin/env python3
"""Generate `test_combined.py` per model: the literal concatenation of
`test_hypothesis.py` (the dataset's original suite) and `test_structural_full.py`
(this session's deterministic-first suite), as one real file -- not two files
fed to a single pytest invocation.

Why concatenation is safe despite real name collisions between the two
generators' output:

- **Module-level variables** (confirmed on model_1: both independently
  define `{ClassName}_strategy` Hypothesis strategy variables AND a
  `safe_text` helper with the identical name) -- Python executes
  module-level code top-to-bottom. Each `@given(instance=X_strategy)`
  decorator captures whatever `X_strategy` currently is at the moment the
  decorator line executes -- which, since the two files' lines are never
  interleaved (this script places one file's content fully before the
  other's), is always that SAME file's own assignment, made immediately
  above it. The other file's later reassignment of the same name only takes
  effect for that other file's own subsequent decorators. Verified
  empirically (see docs/DECISIONS.md) by running the combined file against
  model_1 and confirming identical pass/fail counts to running each file
  separately.
- **Test function names** -- a genuinely different problem, NOT covered by
  the above reasoning: if both files define `def test_X(...)` with the
  identical name, Python just rebinds `test_X` to whichever definition runs
  second -- no error, and pytest (which collects test items by introspecting
  the already-executed module's namespace) only ever sees the survivor. The
  other generator's test for that class is silently dropped, not merely
  shadowed for part of the file. Confirmed this actually happens: both
  generators independently produce a `test_{ClassName}_instantiation`
  function for at least some classes, with no generator-specific suffix --
  439/9,017 models (4.9%) have at least one such collision, checked via AST
  across the full dataset. Fixed in `disambiguate_test_names()`: every
  top-level `test_*` function in the OLD suite is renamed with a `test_hyp_`
  infix before concatenation (keeps pytest's `test_*` discovery working,
  guarantees the name can never collide with anything the new suite
  generates -- structurally, not just for the 439 currently-observed cases).

No import deduplication is attempted -- duplicate imports (both files
import pytest, hypothesis, overlapping names from python_code, etc.) are
functionally harmless in Python (re-importing rebinds to the same objects),
and deduplicating them correctly would require resolving import-order
subtleties for no behavioral benefit.

Usage:
    python scripts/generate_combined_tests.py --models-file PATH [--workers N]
        [--dataset-dir PATH] [--reports-dir PATH] [--report-name NAME]
        [--limit N] [--fresh]
"""
from __future__ import annotations

import argparse
import ast
import concurrent.futures
import datetime
import json
import platform
from pathlib import Path

OLD_TEST_FILENAME = "test_hypothesis.py"
NEW_TEST_FILENAME = "test_structural_full.py"
COMBINED_FILENAME = "test_combined.py"


def find_model_dirs(dataset_dir: Path, models_file: Path | None, limit: int | None) -> list[Path]:
    if models_file:
        names = [l.strip() for l in models_file.read_text().splitlines() if l.strip()]
        dirs = [dataset_dir / name for name in names]
    else:
        dirs = sorted(p for p in dataset_dir.iterdir() if p.is_dir())
    if limit:
        dirs = dirs[:limit]
    return dirs


def load_cache(cache_path: Path) -> dict[str, dict]:
    cached: dict[str, dict] = {}
    if not cache_path.is_file():
        return cached
    with cache_path.open("r") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            try:
                result = json.loads(line)
            except json.JSONDecodeError:
                continue
            cached[result["model"]] = result
    return cached


def _pure_instantiation_class(node: ast.FunctionDef | ast.AsyncFunctionDef) -> str | None:
    """The class name if this test's ENTIRE body is exactly one
    `assert isinstance(<param>, ClassName)` statement -- both generators
    independently produce a test in exactly this shape per class (confirmed
    on model_1: old suite's `test_petrinet_token_instantiation` and new
    suite's `test_petrinet_Token_instantiation` are structurally identical,
    just under different casing, which is WHY name-based matching can't find
    this overlap -- only ~4.9% of these happen to collide as strings). Body
    structure is the only reliable, generator-agnostic signature.
    """
    if len(node.body) != 1:
        return None
    stmt = node.body[0]
    if not isinstance(stmt, ast.Assert):
        return None
    test = stmt.test
    if not (isinstance(test, ast.Call) and isinstance(test.func, ast.Name) and test.func.id == "isinstance"):
        return None
    if len(test.args) < 2 or not isinstance(test.args[1], ast.Name):
        return None
    return test.args[1].id


def _hasattr_check_target(node: ast.FunctionDef | ast.AsyncFunctionDef) -> tuple[str, str] | None:
    """(class_name, attr_name) if this function's FIRST statement is
    `assert hasattr(ClassName, "attr")` -- the dataset's original generator's
    attribute-existence-check pattern (confirmed on model_1:
    `test_petrinet_node_has_name`). Matching only the first statement, not
    the whole body, is deliberate: it's the part of the pattern that
    reliably identifies intent even if later statements in the body vary."""
    if not node.body:
        return None
    stmt = node.body[0]
    if not isinstance(stmt, ast.Assert):
        return None
    test = stmt.test
    if not (isinstance(test, ast.Call) and isinstance(test.func, ast.Name) and test.func.id == "hasattr"):
        return None
    if len(test.args) < 2:
        return None
    cls_arg, attr_arg = test.args[0], test.args[1]
    if not isinstance(cls_arg, ast.Name):
        return None
    if not (isinstance(attr_arg, ast.Constant) and isinstance(attr_arg.value, str)):
        return None
    return cls_arg.id, attr_arg.value


def _value_roundtrip_target(node: ast.FunctionDef | ast.AsyncFunctionDef) -> tuple[str, str] | None:
    """(class_name, attr_name) if this is one of generate_structural_tests.py's
    own `_value_roundtrip` tests: first statement `instance = ClassName(...)`,
    second statement `assert instance.ATTR == ...`. This is our own
    generator's exact, known shape (see generate_tests() in
    generate_structural_tests.py) -- matched structurally here rather than
    by the test's own name string, for the same reason as the two functions
    above: robust regardless of exactly how the name was formed."""
    if len(node.body) < 2:
        return None
    first, second = node.body[0], node.body[1]
    if not (isinstance(first, ast.Assign) and len(first.targets) == 1 and isinstance(first.targets[0], ast.Name)):
        return None
    instance_name = first.targets[0].id
    call = first.value
    if not (isinstance(call, ast.Call) and isinstance(call.func, ast.Name)):
        return None
    class_name = call.func.id
    if not isinstance(second, ast.Assert):
        return None
    cmp = second.test
    if not (isinstance(cmp, ast.Compare) and len(cmp.ops) == 1 and isinstance(cmp.ops[0], ast.Eq)):
        return None
    left = cmp.left
    if not (isinstance(left, ast.Attribute) and isinstance(left.value, ast.Name) and left.value.id == instance_name):
        return None
    return class_name, left.attr


def find_redundant_old_tests(old_tree: ast.Module, new_tree: ast.Module) -> set[str]:
    """Names of OLD-suite top-level test functions to drop because the NEW
    suite already tests the exact same thing, or something strictly
    stronger, for the same (class[, attribute]).

    Two deterministic, structural (not name-based) rules -- see the three
    matcher functions above for exactly what each pattern requires:
      1. Exact duplicate: both suites have a "pure instantiation" test
         (construct + isinstance, nothing else) for the same class. Drop the
         OLD suite's copy, keep the NEW suite's.
      2. Subsumption: OLD suite has an attribute-existence check
         (`hasattr` + property-descriptor check) for (class, attr), and NEW
         suite has a `_value_roundtrip` test for the SAME (class, attr) --
         which additionally proves the actual value round-trips correctly,
         strictly more than existence alone. Drop the OLD suite's copy.

    No other test type is touched -- OLD suite's `_is_not_abstract`/
    `_constructor_exists`/`_constructor_args` and NEW suite's `_isa_`/
    `_assoc_..._link_reassign_clear` have no counterpart in the other file
    and are always kept as-is.
    """
    new_instantiation_classes: set[str] = set()
    new_roundtrip_targets: set[tuple[str, str]] = set()
    for node in new_tree.body:
        if not isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)):
            continue
        cls = _pure_instantiation_class(node)
        if cls:
            new_instantiation_classes.add(cls)
        rt = _value_roundtrip_target(node)
        if rt:
            new_roundtrip_targets.add(rt)

    to_remove: set[str] = set()
    for node in old_tree.body:
        if not isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)):
            continue
        cls = _pure_instantiation_class(node)
        if cls and cls in new_instantiation_classes:
            to_remove.add(node.name)
            continue
        ha = _hasattr_check_target(node)
        if ha and ha in new_roundtrip_targets:
            to_remove.add(node.name)
    return to_remove


def _decorator_start_line(node: ast.FunctionDef | ast.AsyncFunctionDef) -> int:
    if node.decorator_list:
        return node.decorator_list[0].lineno
    return node.lineno


def remove_functions(source: str, names_to_remove: set[str]) -> str:
    """Excise the named top-level functions (decorator lines included) by
    line range. Leaves everything else -- including any now-unused
    Hypothesis strategy variable the removed test's `@given` referenced --
    untouched: harmless dead code, not worth the extra complexity/risk of
    trying to detect "unused" correctly."""
    if not names_to_remove:
        return source
    tree = ast.parse(source)
    lines = source.splitlines(keepends=True)
    remove_line_idxs: set[int] = set()
    for node in tree.body:
        if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)) and node.name in names_to_remove:
            start = _decorator_start_line(node) - 1
            end = node.end_lineno
            remove_line_idxs.update(range(start, end))
    return "".join(line for i, line in enumerate(lines) if i not in remove_line_idxs)


def disambiguate_test_names(source: str) -> str:
    """Rename every top-level `def test_X(...)` to `def test_hyp_X(...)`.

    Both generators independently converged on the exact same name for at
    least some classes' instantiation test -- `test_{ClassName}_instantiation`
    -- confirmed dataset-wide: 439/9,017 models have at least one genuine
    collision (checked via AST, comparing top-level test-function names
    between the two files directly). A naive concatenation would let
    whichever definition comes last silently win (Python just rebinds the
    name; no error), permanently losing the other generator's test for that
    class with no visible failure anywhere.

    Renaming with a `test_hyp_` infix (not just a `test_` suffix) keeps
    pytest's default `test_*` discovery working, while guaranteeing the full
    name can never collide with anything test_structural_full.py generates
    -- not just the 439 currently-observed cases, but structurally, since
    that generator never produces a `test_hyp_*` name.

    AST-located (exact lineno of each top-level test function), then
    line-anchored text substitution -- not a blind global find/replace --
    so a name that happens to also appear elsewhere (a string, a comment)
    is never touched, only the actual `def` line.
    """
    tree = ast.parse(source)
    lines = source.splitlines(keepends=True)
    for node in tree.body:
        if not isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)):
            continue
        if not node.name.startswith("test_"):
            continue
        old_def = f"def {node.name}("
        new_def = f"def test_hyp_{node.name[len('test_'):]}("
        idx = node.lineno - 1
        if old_def in lines[idx]:
            lines[idx] = lines[idx].replace(old_def, new_def, 1)
    return "".join(lines)


def combine_tests(old_source: str, new_source: str) -> tuple[str, int]:
    """Returns (combined_source, count_of_old_suite_tests_dropped_as_redundant)."""
    old_tree = ast.parse(old_source)
    new_tree = ast.parse(new_source)
    redundant = find_redundant_old_tests(old_tree, new_tree)
    old_source = remove_functions(old_source, redundant)
    old_source = disambiguate_test_names(old_source)
    combined = (
        "# =============================================================================\n"
        "# This file is a generated concatenation of two independent test suites --\n"
        "# see scripts/generate_combined_tests.py for why simple concatenation is safe\n"
        "# despite both generators using the same naming convention for some helpers,\n"
        "# and for the deterministic rules used to drop old-suite tests the new suite\n"
        "# already covers equally or more thoroughly.\n"
        "# =============================================================================\n"
        "\n"
        "# ----- SECTION A: test_hypothesis.py (original generated suite) -----\n"
        f"{old_source}\n"
        "\n"
        "# ----- SECTION B: test_structural_full.py (deterministic-first suite) -----\n"
        f"{new_source}\n"
    )
    return combined, len(redundant)


def generate_model(model_dir: Path) -> dict:
    checked_at = datetime.datetime.now(datetime.timezone.utc).isoformat()
    result = {
        "model": model_dir.name,
        "checked_at": checked_at,
        "python_version": platform.python_version(),
        "status": "missing_file",
        "error_message": None,
        "old_tests_removed_as_redundant": None,
    }

    old_path = model_dir / OLD_TEST_FILENAME
    new_path = model_dir / NEW_TEST_FILENAME
    if not old_path.is_file():
        result["error_message"] = f"{OLD_TEST_FILENAME} not found"
        return result
    if not new_path.is_file():
        result["error_message"] = f"{NEW_TEST_FILENAME} not found"
        return result

    try:
        old_source = old_path.read_text(encoding="utf-8")
        new_source = new_path.read_text(encoding="utf-8")
        combined, removed_count = combine_tests(old_source, new_source)
        (model_dir / COMBINED_FILENAME).write_text(combined, encoding="utf-8")
        result["status"] = "generated"
        result["old_tests_removed_as_redundant"] = removed_count
    except Exception as exc:
        result["status"] = "error"
        result["error_message"] = str(exc)
    return result


def build_report(results: list[dict]) -> dict:
    total = len(results)
    by_status: dict[str, int] = {}
    for r in results:
        by_status[r["status"]] = by_status.get(r["status"], 0) + 1
    generated = [r for r in results if r["status"] == "generated"]
    removed_counts = [r["old_tests_removed_as_redundant"] for r in generated
                       if r["old_tests_removed_as_redundant"] is not None]
    return {
        "generated_at": datetime.datetime.now(datetime.timezone.utc).isoformat(),
        "total_models": total,
        "by_status": by_status,
        "generated_count": len(generated),
        "total_old_tests_removed_as_redundant": sum(removed_counts),
        "models_with_a_removal": sum(1 for c in removed_counts if c > 0),
        "results": results,
    }


def render_markdown_report(report: dict) -> str:
    lines = [
        "# Combined Test Generation Report",
        "",
        f"Generated: {report['generated_at']}",
        "",
        f"- **Total models:** {report['total_models']}",
        f"- **Generated:** {report['generated_count']}",
        f"- **Old-suite tests dropped as redundant (exact duplicate or subsumed by a "
        f"stronger new-suite test):** {report['total_old_tests_removed_as_redundant']} "
        f"across {report['models_with_a_removal']} models",
        "",
        "## Breakdown by status",
        "",
        "| Status | Count |",
        "|---|---|",
    ]
    for status, count in sorted(report["by_status"].items(), key=lambda kv: -kv[1]):
        lines.append(f"| {status} | {count} |")
    lines += ["", "Full per-model detail: see the accompanying `.json` report."]
    return "\n".join(lines) + "\n"


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--dataset-dir", type=Path, default=Path(__file__).resolve().parent.parent / "Dataset")
    parser.add_argument("--reports-dir", type=Path, default=Path(__file__).resolve().parent.parent / "reports")
    parser.add_argument("--models-file", type=Path, default=None)
    parser.add_argument("--report-name", type=str, default="combined_tests_report")
    parser.add_argument("--workers", type=int, default=8)
    parser.add_argument("--limit", type=int, default=None)
    parser.add_argument("--fresh", action="store_true", help="Ignore any existing cache and recompute every model")
    args = parser.parse_args()

    args.reports_dir.mkdir(parents=True, exist_ok=True)
    cache_path = args.reports_dir / f"{args.report_name}.cache.jsonl"

    cached_results: dict[str, dict] = {} if args.fresh else load_cache(cache_path)
    if args.fresh and cache_path.is_file():
        cache_path.unlink()

    all_model_dirs = find_model_dirs(args.dataset_dir, args.models_file, args.limit)
    total = len(all_model_dirs)
    model_dirs = [d for d in all_model_dirs if d.name not in cached_results]
    skipped = total - len(model_dirs)

    print(f"Generating combined tests for {total} models with {args.workers} workers...")
    if skipped:
        print(f"Resuming from cache: {skipped}/{total} already done, {len(model_dirs)} remaining "
              f"(pass --fresh to ignore the cache and recompute everything)")

    results: list[dict] = list(cached_results.values())
    done = skipped
    cache_file = cache_path.open("a")
    try:
        with concurrent.futures.ProcessPoolExecutor(max_workers=args.workers) as executor:
            futures = {executor.submit(generate_model, model_dir): model_dir for model_dir in model_dirs}
            for future in concurrent.futures.as_completed(futures):
                model_dir = futures[future]
                try:
                    result = future.result()
                except Exception as exc:
                    result = {"model": model_dir.name, "status": "error", "error_message": str(exc)}
                results.append(result)
                cache_file.write(json.dumps(result) + "\n")
                cache_file.flush()
                done += 1
                if done % 500 == 0 or done == total:
                    print(f"  {done}/{total} processed", flush=True)
    finally:
        cache_file.close()

    report = build_report(results)
    json_path = args.reports_dir / f"{args.report_name}.json"
    json_path.write_text(json.dumps(report, indent=2) + "\n")
    md_path = args.reports_dir / f"{args.report_name}.md"
    md_path.write_text(render_markdown_report(report))

    print()
    print(f"Generated: {report['generated_count']}/{report['total_models']}")
    print(f"Report written to {json_path} and {md_path}")


if __name__ == "__main__":
    main()
