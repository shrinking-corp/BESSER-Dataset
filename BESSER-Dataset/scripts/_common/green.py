"""Making a per-model test suite "green": every test in it passes on the
unmutated python_code.py.

A mutation score is only meaningful for a suite that passes on the original
code -- a test that fails there "kills" every mutant (cosmic-ray counts any
non-zero exit as KILLED) and the model scores a fake 1.0. On 2026-10-17 this
was found in 118/200 sample suites from four independent causes (CrossHair
stdlib `Enum` tests, a CrossHair `datetime` import bug, a stub-double
generator bug, and the dataset's own `test_hypothesis.py` empty-method checks,
which fail on purpose for every `# TODO: Implement` stub). Fixing each source
individually is necessary but not sufficient -- the next generator can always
introduce a new one -- so every suite that gets mutation-measured, or used as
a benchmarking oracle, is pruned to its green subset here. Removed tests are
always reported, never silently dropped.

Runs pytest exactly the way the mutation validators' cosmic-ray command does:
only python_code.py + the test file, copied into a throwaway scratch dir,
with the same --hypothesis-seed.
"""
from __future__ import annotations

import ast
import os
import re
import shutil
import subprocess
import sys
import tempfile
import xml.etree.ElementTree as ET
from pathlib import Path

SOURCE_FILENAME = "python_code.py"
_PARAM_SUFFIX = re.compile(r"\[.*\]$")


def describe_green_result(result: dict) -> str:
    """Progress-line suffix for a per-model green-suite result."""
    if result["status"] != "green":
        return ""
    return f" ({result.get('tests_after_pruning')} tests, {len(result.get('removed_tests') or [])} removed)"


def make_test_names_unique(source: str) -> tuple[str, int]:
    """Renames repeated top-level `def test_x` to `test_x__2`, `test_x__3`, ...
    Python keeps only the LAST definition of a name, so earlier copies never
    run at all (seen in CrossHair output, e.g. `test_Enum___new__` defined
    several times in one file). Returns (source, renamed_count)."""
    tree = ast.parse(source)
    lines = source.splitlines(keepends=True)
    all_names = {n.name for n in tree.body if isinstance(n, (ast.FunctionDef, ast.AsyncFunctionDef))}
    seen: dict[str, int] = {}
    renamed = 0
    for node in tree.body:
        if not isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)) or not node.name.startswith("test_"):
            continue
        seen[node.name] = seen.get(node.name, 0) + 1
        if seen[node.name] == 1:
            continue
        suffix = seen[node.name]
        new_name = f"{node.name}__{suffix}"
        while new_name in all_names:
            suffix += 1
            new_name = f"{node.name}__{suffix}"
        all_names.add(new_name)
        idx = node.lineno - 1
        lines[idx] = re.sub(rf"\bdef {re.escape(node.name)}\(", f"def {new_name}(", lines[idx], count=1)
        renamed += 1
    return "".join(lines), renamed


def remove_top_level_functions(source: str, names: set[str]) -> str:
    """Drops top-level function definitions (with their decorators) whose
    name is in `names`, leaving every other line untouched."""
    tree = ast.parse(source)
    drop: set[int] = set()
    for node in tree.body:
        if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)) and node.name in names:
            start = min([d.lineno for d in node.decorator_list] + [node.lineno])
            drop.update(range(start - 1, node.end_lineno))
    return "".join(line for i, line in enumerate(source.splitlines(keepends=True)) if i not in drop)


def _parse_junit(junit_path: Path) -> tuple[int, dict[str, str], bool]:
    """(tests_collected, {failing_test_name: reason}, had_collection_error)."""
    total = 0
    failing: dict[str, str] = {}
    collection_error = False
    for case in ET.parse(junit_path).iter("testcase"):
        problem = case.find("failure")
        if problem is None:
            problem = case.find("error")
        if not case.get("classname"):
            # pytest reports a module that fails to import/collect as a
            # testcase with an empty classname -- not an individual test.
            collection_error = collection_error or problem is not None
            continue
        total += 1
        if problem is not None:
            name = _PARAM_SUFFIX.sub("", case.get("name", ""))
            message = (problem.get("message") or problem.tag).splitlines()
            failing.setdefault(name, (message[0] if message else problem.tag)[:200])
    return total, failing, collection_error


def make_green(
    source: str,
    model_dir: Path,
    test_filename: str,
    hypothesis_seed: int | None,
    timeout: float,
    max_rounds: int = 3,
) -> dict:
    """Prunes failing tests from `source` until the suite passes unmutated.

    Returns a dict with "status" (green | no_tests | collection_error |
    not_green | timeout), "source" (the green suite, when green),
    "tests_before", "tests_after", "removed" ([{"test", "reason"}]) and
    "error_message". Removing one failing test can't make another fail, but a
    few rounds are allowed for robustness; a suite still red after that is
    reported as not_green rather than kept.
    """
    result = {
        "status": None, "source": None, "tests_before": None, "tests_after": None,
        "removed": [], "error_message": None,
    }
    scratch = Path(tempfile.mkdtemp(prefix=f"green_{model_dir.name}_"))
    hypothesis_home = tempfile.mkdtemp(prefix="green_hyp_")
    try:
        shutil.copy2(model_dir / SOURCE_FILENAME, scratch / SOURCE_FILENAME)
        env = dict(os.environ)
        env["PYTHONDONTWRITEBYTECODE"] = "1"
        env["HYPOTHESIS_STORAGE_DIRECTORY"] = hypothesis_home
        junit_path = scratch / "junit.xml"
        current = source
        for round_no in range(max_rounds + 1):
            (scratch / test_filename).write_text(current, encoding="utf-8")
            junit_path.unlink(missing_ok=True)
            cmd = [sys.executable, "-m", "pytest", test_filename, "-q", "-p", "no:cacheprovider",
                   f"--junit-xml={junit_path}"]
            if hypothesis_seed is not None:
                cmd.append(f"--hypothesis-seed={hypothesis_seed}")
            try:
                proc = subprocess.run(cmd, cwd=str(scratch), capture_output=True, text=True,
                                      timeout=timeout, env=env)
            except subprocess.TimeoutExpired:
                result["status"] = "timeout"
                result["error_message"] = f"unmutated suite run exceeded {timeout}s"
                return result
            if not junit_path.is_file():
                result["status"] = "collection_error"
                result["error_message"] = (proc.stdout or proc.stderr or "").strip()[-1000:]
                return result

            total, failing, collection_error = _parse_junit(junit_path)
            if result["tests_before"] is None:
                result["tests_before"] = total
            if collection_error:
                result["status"] = "collection_error"
                result["error_message"] = (proc.stdout or proc.stderr or "").strip()[-1000:]
                return result
            if total == 0:
                result["status"] = "no_tests"
                result["tests_after"] = 0
                return result
            if not failing:
                result["status"] = "green"
                result["source"] = current
                result["tests_after"] = total
                return result
            if round_no == max_rounds:
                result["status"] = "not_green"
                result["error_message"] = f"still failing after {max_rounds} pruning rounds: {sorted(failing)[:10]}"
                return result
            result["removed"].extend({"test": name, "reason": reason} for name, reason in sorted(failing.items()))
            current = remove_top_level_functions(current, set(failing))
        return result
    finally:
        shutil.rmtree(scratch, ignore_errors=True)
        shutil.rmtree(hypothesis_home, ignore_errors=True)
