#!/usr/bin/env python3
"""Measure mutation score of `test_hypothesis.py` against ONLY the property
getters/setters in `python_code.py` -- not `__init__`, not plain methods.

This is a SEPARATE, differently-scoped metric from `validate_mutation.py`'s
whole-file mutation score, kept in its own script/report/metadata key so the
existing whole-file results (already computed across all 9,082 models) are
never touched or overwritten. See that script's docstring for the shared
cosmic-ray mechanics (scratch-copy safety, capping, resume/cache); this
docstring only covers what's different here.

Why scope to properties: this dataset's generated code puts almost all of
its real logic in `@property` getters and `@x.setter` setters (bidirectional-
association consistency, `hasattr`/`getattr`/`setattr` chains) -- confirmed
in docs/DECISIONS.md and re-confirmed empirically this session (model_100:
72% of its whole-file mutants already fall inside setters; model_1: 81%).
`__init__` bodies are mostly plain assignment plus the occasional
`is not None` default-value check.

Getters are included too, not just setters, despite every getter body in
this dataset being a trivial `return self.__x` (confirmed across the WHOLE
dataset: 304,554 getters scanned, zero contain anything else). A trivial
getter still has exactly one mutation available to it: cosmic-ray's
`RemoveDecorator` operator can strip the `@property` decorator itself. This
is worth measuring even though it should almost always be killed -- if
`@property` is removed but the paired `@x.setter` isn't (mutants are one
change at a time), `x.setter` immediately raises `AttributeError` at class-
definition time (`.setter` requires `x` to already be a property object),
failing the entire test file to even collect. That near-guaranteed kill
means this particular mutant type won't discriminate much between good and
bad test suites, but it's cheap to include now that the range-detection
machinery below exists, and it costs nothing to leave in.

Implementation note on why decorator lines matter: a mutation removing
`@property` is positioned at the DECORATOR's own line, not the `def` line.
Python's `ast.FunctionDef.lineno` points at `def`, excluding any decorator
lines above it -- so property line ranges here start from
`node.decorator_list[0].lineno`, not `node.lineno`, or `RemoveDecorator`
mutants would fall just outside the recorded range and get misclassified as
"not in a property". Confirmed by hitting exactly this bug while prototyping
against model_1 and model_100 in this session. Also confirmed empirically
that cosmic-ray's own `definition_name` column cannot be used for this
instead: for a decorator-removal mutant it reports the *enclosing class*,
not the method -- and this dataset can have a class and one of its own
properties share the exact same literal name (model_1's `petrinet_Node`
class has a property/setter pair also named `petrinet_Node`), making that
column ambiguous. Line-range matching against the AST sidesteps this
entirely.

The scoping step runs between `cosmic-ray init` and the existing random
--max-mutants capping: first every mutant outside a property's line range is
dropped, then the (now much smaller) survivors are capped exactly as
`validate_mutation.py` already does. A model with no properties at all
(e.g. every class is a bare `pass` stub) naturally falls through to the
`no_mutants` status, same as validate_mutation.py's fully-empty case.

Usage:
    python scripts/validate_mutation_properties.py --models-file PATH [--workers N]
        [--max-mutants N] [--per-mutant-timeout SECONDS]
        [--overall-timeout SECONDS] [--dataset-dir PATH] [--fresh]
        [--write-metadata] [--test-file NAME] [--metadata-key KEY]

By default tests against test_hypothesis.py, writing mutation_validation_properties.
Pass --test-file test_structural_full.py to measure the new structural suite instead
(auto-derives --metadata-key structural_mutation_validation_properties).
"""
from __future__ import annotations

import argparse
import ast
import concurrent.futures
import datetime
import json
import os
import platform
import random
import shutil
import sqlite3
import subprocess
import sys
import tempfile
import time
from pathlib import Path

# Overridable via --test-file/--metadata-key (see main()); read from env
# vars rather than plain module constants because ProcessPoolExecutor
# workers on Windows use 'spawn' and re-import this file fresh in a new
# interpreter -- a `global TEST_FILENAME = ...` mutation in main() (parent
# process only) would never reach them. The parent sets these env vars
# before creating the pool; each worker's own fresh import then picks up
# the same overridden values. See validate_mutation.py for the identical
# pattern.
TEST_FILENAME = os.environ.get("VALIDATE_MUTATION_PROPERTIES_TEST_FILENAME", "test_hypothesis.py")
SOURCE_FILENAME = "python_code.py"
CONFIG_FILENAME = "cr-config.toml"
SESSION_FILENAME = "cr-session.sqlite"
METADATA_FILENAME = "code_metadata.json"
METADATA_KEY = os.environ.get("VALIDATE_MUTATION_PROPERTIES_METADATA_KEY", "mutation_validation_properties")
TEST_FILE_METADATA_KEYS = {
    "test_hypothesis.py": "mutation_validation_properties",
    "test_structural_full.py": "structural_mutation_validation_properties",
}
DEFAULT_MAX_MUTANTS = 40
DEFAULT_PER_MUTANT_TIMEOUT = 90.0
DEFAULT_OVERALL_TIMEOUT = 900  # hard wall-clock cap per model, seconds


def cosmic_ray_executable() -> str:
    """Path to the cosmic-ray console-script installed alongside this interpreter.

    subprocess.run(["cosmic-ray", ...]) resolves that name via PATH, which
    does not include a venv's Scripts/bin directory unless the venv was
    shell-activated -- invoking .venv/Scripts/python.exe directly does not
    add it, and this script is meant to be runnable that way. The
    console-script always installs next to the interpreter that installed
    it, so resolve it from sys.executable instead of trusting PATH. Falls
    back to the bare name (PATH lookup) if not found there.
    """
    name = "cosmic-ray.exe" if platform.system() == "Windows" else "cosmic-ray"
    candidate = Path(sys.executable).parent / name
    return str(candidate) if candidate.is_file() else "cosmic-ray"


def load_cache(cache_path: Path) -> dict[str, dict]:
    """Read a JSONL cache of previously-completed results, keyed by model name.

    Tolerates a truncated last line (e.g. the process was killed mid-write)
    by skipping any line that fails to parse.
    """
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


def find_model_dirs(dataset_dir: Path, models_file: Path | None, limit: int | None) -> list[Path]:
    if models_file:
        names = [l.strip() for l in models_file.read_text().splitlines() if l.strip()]
        dirs = [dataset_dir / name for name in names]
    else:
        dirs = sorted(p for p in dataset_dir.iterdir() if p.is_dir())
    if limit:
        dirs = dirs[:limit]
    return dirs


def sort_longest_first(model_dirs: list[Path]) -> list[Path]:
    """Sort by combined python_code.py + test_hypothesis.py size, descending.

    Same LPT-scheduling rationale as validate_mutation.py: reduces idle-
    worker tail time on a run with highly variable per-model duration.
    """
    def size(model_dir: Path) -> int:
        total = 0
        for name in (SOURCE_FILENAME, TEST_FILENAME):
            try:
                total += (model_dir / name).stat().st_size
            except OSError:
                pass
        return total

    return sorted(model_dirs, key=size, reverse=True)


def property_line_ranges(source_path: Path) -> list[tuple[int, int]]:
    """Line ranges (inclusive) of every @property getter and @x.setter method.

    Each range starts at the DECORATOR's own line, not the `def` line -- see
    module docstring for why that distinction matters for RemoveDecorator
    mutants specifically.
    """
    tree = ast.parse(source_path.read_text())
    ranges: list[tuple[int, int]] = []
    for node in ast.walk(tree):
        if not isinstance(node, ast.FunctionDef):
            continue
        deco_names = [
            d.attr if isinstance(d, ast.Attribute) else getattr(d, "id", None)
            for d in node.decorator_list
        ]
        if "property" in deco_names or "setter" in deco_names:
            start = node.decorator_list[0].lineno if node.decorator_list else node.lineno
            ranges.append((start, node.end_lineno))
    return ranges


def scope_to_properties(session_path: Path, source_path: Path) -> tuple[int, int]:
    """Delete mutation_specs/work_items rows outside property getter/setter ranges.

    Returns (total_in_file, total_in_properties) -- both pre-cap.
    """
    ranges = property_line_ranges(source_path)
    con = sqlite3.connect(str(session_path))
    try:
        cur = con.cursor()
        cur.execute("SELECT job_id, start_pos_row FROM mutation_specs")
        rows = cur.fetchall()
        total_in_file = len(rows)
        drop = [(jid,) for jid, row in rows if not any(lo <= row <= hi for lo, hi in ranges)]
        cur.executemany("DELETE FROM mutation_specs WHERE job_id = ?", drop)
        cur.executemany("DELETE FROM work_items WHERE job_id = ?", drop)
        con.commit()
        return total_in_file, total_in_file - len(drop)
    finally:
        con.close()


def cap_mutants(session_path: Path, max_mutants: int, seed_key: str) -> tuple[int, int]:
    """Randomly downsample mutation_specs/work_items rows in-place. Returns (total, kept)."""
    con = sqlite3.connect(str(session_path))
    try:
        cur = con.cursor()
        cur.execute("SELECT job_id FROM mutation_specs")
        job_ids = [row[0] for row in cur.fetchall()]
        total = len(job_ids)
        if total <= max_mutants:
            return total, total
        rng = random.Random(seed_key)
        keep = set(rng.sample(job_ids, max_mutants))
        drop = [(jid,) for jid in job_ids if jid not in keep]
        cur.executemany("DELETE FROM mutation_specs WHERE job_id = ?", drop)
        cur.executemany("DELETE FROM work_items WHERE job_id = ?", drop)
        con.commit()
        return total, max_mutants
    finally:
        con.close()


def read_results(session_path: Path) -> dict:
    con = sqlite3.connect(str(session_path))
    try:
        cur = con.cursor()
        cur.execute("SELECT test_outcome, COUNT(*) FROM work_results GROUP BY test_outcome")
        outcomes = {(row[0] or "none"): row[1] for row in cur.fetchall()}
        cur.execute("SELECT COUNT(*) FROM work_results")
        total_run = cur.fetchone()[0]
        return {"outcomes": outcomes, "total_run": total_run}
    finally:
        con.close()


def validate_model(
    model_dir: Path,
    max_mutants: int,
    per_mutant_timeout: float,
    overall_timeout: int,
    hypothesis_home: str,
    scratch_root: str,
) -> dict:
    checked_at = datetime.datetime.now(datetime.timezone.utc).isoformat()
    result = {
        "model": model_dir.name,
        "checked_at": checked_at,
        "python_version": platform.python_version(),
        "status": "missing_file",
        "total_mutants_in_file": None,
        "total_mutants_in_properties": None,
        "total_mutants_generated": None,
        "mutants_run": None,
        "killed": None,
        "survived": None,
        "other_outcomes": {},
        "mutation_score": None,
        "init_duration_s": None,
        "exec_duration_s": None,
        "error_message": None,
    }

    source_path = model_dir / SOURCE_FILENAME
    test_path = model_dir / TEST_FILENAME
    if not source_path.is_file() or not test_path.is_file():
        result["error_message"] = f"{SOURCE_FILENAME} or {TEST_FILENAME} not found in {model_dir.name}"
        return result

    # Work entirely in a scratch copy -- same safety rationale as
    # validate_mutation.py: cosmic-ray mutates its target file in place on
    # disk, so it must never point at the real, git-tracked dataset directory.
    scratch_dir = Path(tempfile.mkdtemp(prefix=f"crp_{model_dir.name}_", dir=scratch_root))
    try:
        shutil.copy2(source_path, scratch_dir / SOURCE_FILENAME)
        shutil.copy2(test_path, scratch_dir / TEST_FILENAME)

        config_path = scratch_dir / CONFIG_FILENAME
        session_path = scratch_dir / SESSION_FILENAME
        # See validate_mutation.py for why this needs forward slashes +
        # quoting + a TOML literal string: sys.executable's backslashes get
        # mangled both by TOML's double-quoted-string escaping and by
        # cosmic-ray's own shlex.split() of the test-command on Windows.
        python_exe = Path(sys.executable).as_posix()
        config_text = f"""[cosmic-ray]
module-path = "{SOURCE_FILENAME}"
timeout = {per_mutant_timeout}
excluded-modules = []
test-command = '"{python_exe}" -m pytest {TEST_FILENAME} -x -q -p no:cacheprovider'

[cosmic-ray.distributor]
name = "local"
"""
        config_path.write_text(config_text)

        env = dict(os.environ)
        env["PYTHONDONTWRITEBYTECODE"] = "1"
        env["HYPOTHESIS_STORAGE_DIRECTORY"] = hypothesis_home

        cr_exe = cosmic_ray_executable()
        init_start = time.monotonic()
        init_proc = subprocess.run(
            [cr_exe, "init", CONFIG_FILENAME, SESSION_FILENAME],
            cwd=str(scratch_dir), capture_output=True, text=True,
            timeout=min(overall_timeout, 300), env=env,
        )
        result["init_duration_s"] = round(time.monotonic() - init_start, 3)
        if init_proc.returncode != 0:
            result["status"] = "init_error"
            result["error_message"] = (init_proc.stderr or init_proc.stdout or "").strip()[-1000:]
            return result

        if not session_path.is_file():
            result["status"] = "init_error"
            result["error_message"] = "cosmic-ray init produced no session file"
            return result

        total_in_file, total_in_properties = scope_to_properties(session_path, scratch_dir / SOURCE_FILENAME)
        result["total_mutants_in_file"] = total_in_file
        result["total_mutants_in_properties"] = total_in_properties

        total_generated, kept = cap_mutants(session_path, max_mutants, seed_key=model_dir.name)
        result["total_mutants_generated"] = total_generated

        if kept == 0:
            result["status"] = "no_mutants"
            return result

        exec_start = time.monotonic()
        try:
            exec_proc = subprocess.run(
                [cr_exe, "exec", CONFIG_FILENAME, SESSION_FILENAME],
                cwd=str(scratch_dir), capture_output=True, text=True,
                timeout=overall_timeout, env=env,
            )
        except subprocess.TimeoutExpired:
            result["status"] = "timeout"
            result["exec_duration_s"] = round(time.monotonic() - exec_start, 3)
            result["error_message"] = f"exec exceeded {overall_timeout}s"
            try:
                stats = read_results(session_path)
                result["mutants_run"] = stats["total_run"]
                result["killed"] = stats["outcomes"].get("KILLED", 0)
                result["survived"] = stats["outcomes"].get("SURVIVED", 0)
                result["other_outcomes"] = {k: v for k, v in stats["outcomes"].items() if k not in ("KILLED", "SURVIVED")}
            except Exception:
                pass
            return result

        result["exec_duration_s"] = round(time.monotonic() - exec_start, 3)
        if exec_proc.returncode != 0 and exec_proc.returncode != 1:
            result["status"] = "exec_error"
            result["error_message"] = (exec_proc.stderr or exec_proc.stdout or "").strip()[-1000:]

        stats = read_results(session_path)
        result["mutants_run"] = stats["total_run"]
        result["killed"] = stats["outcomes"].get("KILLED", 0)
        result["survived"] = stats["outcomes"].get("SURVIVED", 0)
        result["other_outcomes"] = {k: v for k, v in stats["outcomes"].items() if k not in ("KILLED", "SURVIVED")}
        if stats["total_run"] > 0:
            result["mutation_score"] = round(result["killed"] / stats["total_run"], 4)

        if result["status"] == "missing_file":
            result["status"] = "measured"
        return result
    except subprocess.TimeoutExpired:
        result["status"] = "timeout"
        result["error_message"] = "init exceeded timeout"
        return result
    except Exception as exc:
        result["status"] = "error"
        result["error_message"] = str(exc)
        return result
    finally:
        shutil.rmtree(scratch_dir, ignore_errors=True)


def write_metadata(model_dir: Path, result: dict) -> bool:
    """Merge this model's result into its code_metadata.json under METADATA_KEY.

    Same convention as validate_mutation.py's write_metadata(): requires the
    file to already exist, never creates it, never touches any other key --
    including validate_mutation.py's own "mutation_validation" key.
    """
    metadata_path = model_dir / METADATA_FILENAME
    if not metadata_path.is_file():
        return False
    try:
        metadata = json.loads(metadata_path.read_text())
    except json.JSONDecodeError:
        return False
    metadata[METADATA_KEY] = {
        "checked_at": result["checked_at"],
        "python_version": result["python_version"],
        "status": result["status"],
        "total_mutants_in_file": result["total_mutants_in_file"],
        "total_mutants_in_properties": result["total_mutants_in_properties"],
        "total_mutants_generated": result["total_mutants_generated"],
        "mutants_run": result["mutants_run"],
        "killed": result["killed"],
        "survived": result["survived"],
        "mutation_score": result["mutation_score"],
    }
    metadata_path.write_text(json.dumps(metadata, indent=2) + "\n")
    return True


def build_report(results: list[dict]) -> dict:
    total = len(results)
    by_status: dict[str, int] = {}
    for r in results:
        by_status[r["status"]] = by_status.get(r["status"], 0) + 1

    measured = [r for r in results if r["mutation_score"] is not None]
    durations = sorted(
        (r.get("init_duration_s") or 0) + (r.get("exec_duration_s") or 0)
        for r in results if r.get("exec_duration_s") is not None
    )

    def pct(vals, p):
        if not vals:
            return None
        idx = min(len(vals) - 1, int(len(vals) * p / 100))
        return round(vals[idx], 2)

    property_shares = [
        r["total_mutants_in_properties"] / r["total_mutants_in_file"]
        for r in results
        if r.get("total_mutants_in_file")
    ]

    return {
        "generated_at": datetime.datetime.now(datetime.timezone.utc).isoformat(),
        "total_models": total,
        "by_status": by_status,
        "measured_count": len(measured),
        "avg_mutation_score": round(sum(r["mutation_score"] for r in measured) / len(measured), 4) if measured else None,
        "avg_property_mutant_share": round(sum(property_shares) / len(property_shares), 4) if property_shares else None,
        "total_mutants_in_file_sum": sum(r["total_mutants_in_file"] or 0 for r in results),
        "total_mutants_in_properties_sum": sum(r["total_mutants_in_properties"] or 0 for r in results),
        "total_mutants_run_sum": sum(r["mutants_run"] or 0 for r in results),
        "duration_stats_s": {
            "p50": pct(durations, 50),
            "p90": pct(durations, 90),
            "p99": pct(durations, 99),
            "max": durations[-1] if durations else None,
            "total": round(sum(durations), 2),
        },
        "results": results,
    }


def render_markdown_report(report: dict) -> str:
    lines = [
        "# Property-Scoped Mutation Testing Report (cosmic-ray, capped)",
        "",
        f"Generated: {report['generated_at']}",
        "",
        "Scope: only @property getters and @x.setter setters -- see "
        "validate_mutation_properties.py's docstring. Not comparable to "
        "validate_mutation.py's whole-file mutation_prototype_report.",
        "",
        f"- **Total models checked:** {report['total_models']}",
        f"- **Measured successfully:** {report['measured_count']}",
        f"- **Average mutation score (killed/run):** {report['avg_mutation_score']}" if report['avg_mutation_score'] is not None else "",
        f"- **Average share of whole-file mutants that are in properties:** {report['avg_property_mutant_share']}" if report['avg_property_mutant_share'] is not None else "",
        f"- **Total mutants in-file (uncapped) across sample:** {report['total_mutants_in_file_sum']}",
        f"- **Total mutants in-properties (uncapped) across sample:** {report['total_mutants_in_properties_sum']}",
        f"- **Total mutants actually run (post-cap):** {report['total_mutants_run_sum']}",
        "",
        "## Per-model duration (init+exec, seconds)",
        "",
        f"- p50: {report['duration_stats_s']['p50']}",
        f"- p90: {report['duration_stats_s']['p90']}",
        f"- p99: {report['duration_stats_s']['p99']}",
        f"- max: {report['duration_stats_s']['max']}",
        f"- total (sum, sample only): {report['duration_stats_s']['total']}",
        "",
        "## Breakdown by status",
        "",
        "| Status | Count |",
        "|---|---|",
    ]
    for status, count in sorted(report["by_status"].items(), key=lambda kv: -kv[1]):
        lines.append(f"| {status} | {count} |")
    lines += ["", "Full per-model detail: see `mutation_properties_report.json`."]
    return "\n".join(l for l in lines if l is not None) + "\n"


def main() -> None:
    global TEST_FILENAME, METADATA_KEY
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
    parser.add_argument("--report-name", type=str, default="mutation_properties_report")
    parser.add_argument("--workers", type=int, default=8)
    parser.add_argument("--max-mutants", type=int, default=DEFAULT_MAX_MUTANTS)
    parser.add_argument("--per-mutant-timeout", type=float, default=DEFAULT_PER_MUTANT_TIMEOUT)
    parser.add_argument("--overall-timeout", type=int, default=DEFAULT_OVERALL_TIMEOUT)
    parser.add_argument("--limit", type=int, default=None)
    parser.add_argument("--fresh", action="store_true",
                         help="Ignore any existing cache and recompute every model")
    parser.add_argument("--write-metadata", action="store_true",
                         help="Also write results into each model's code_metadata.json "
                              "under the 'mutation_validation_properties' key "
                              "(off by default; never touches validate_mutation.py's "
                              "'mutation_validation' key)")
    parser.add_argument("--test-file", type=str, default=None,
                         help=f"Run mutants against this test file instead of the default "
                              f"({TEST_FILENAME!r}) -- e.g. test_structural_full.py")
    parser.add_argument("--metadata-key", type=str, default=None,
                         help="Override the code_metadata.json key results are written under "
                              "(default: derived from --test-file, see TEST_FILE_METADATA_KEYS)")
    args = parser.parse_args()

    if args.test_file:
        TEST_FILENAME = args.test_file
    if args.metadata_key:
        METADATA_KEY = args.metadata_key
    elif args.test_file:
        if args.test_file not in TEST_FILE_METADATA_KEYS:
            parser.error(
                f"--test-file {args.test_file!r} has no known default metadata key -- "
                f"pass --metadata-key explicitly (known test files: "
                f"{sorted(TEST_FILE_METADATA_KEYS)})"
            )
        METADATA_KEY = TEST_FILE_METADATA_KEYS[args.test_file]
    os.environ["VALIDATE_MUTATION_PROPERTIES_TEST_FILENAME"] = TEST_FILENAME
    os.environ["VALIDATE_MUTATION_PROPERTIES_METADATA_KEY"] = METADATA_KEY
    print(f"Test file: {TEST_FILENAME}  |  metadata key: {METADATA_KEY}")

    args.reports_dir.mkdir(parents=True, exist_ok=True)
    cache_path = args.reports_dir / f"{args.report_name}.cache.jsonl"

    cached_results: dict[str, dict] = {} if args.fresh else load_cache(cache_path)
    if args.fresh and cache_path.is_file():
        cache_path.unlink()

    all_model_dirs = find_model_dirs(args.dataset_dir, args.models_file, args.limit)
    total = len(all_model_dirs)
    model_dirs = [d for d in all_model_dirs if d.name not in cached_results]
    model_dirs = sort_longest_first(model_dirs)
    skipped = total - len(model_dirs)

    hypothesis_home = tempfile.mkdtemp(prefix="besser_hypothesis_db_mutprop_")
    scratch_root = tempfile.mkdtemp(prefix="besser_cosmicray_scratch_prop_")
    print(f"Running property-scoped mutation testing for {total} models with {args.workers} workers "
          f"(cap={args.max_mutants} mutants/model)...")
    if skipped:
        print(f"Resuming from cache: {skipped}/{total} already done, {len(model_dirs)} remaining "
              f"(pass --fresh to ignore the cache and recompute everything)")
    print(f"(scratch copies under {scratch_root} -- dataset directory is never mutated in place)")

    results: list[dict] = list(cached_results.values())
    done = skipped
    cache_file = cache_path.open("a")
    try:
        with concurrent.futures.ProcessPoolExecutor(max_workers=args.workers) as executor:
            futures = {
                executor.submit(
                    validate_model, model_dir, args.max_mutants,
                    args.per_mutant_timeout, args.overall_timeout, hypothesis_home, scratch_root,
                ): model_dir
                for model_dir in model_dirs
            }
            for future in concurrent.futures.as_completed(futures):
                model_dir = futures[future]
                try:
                    result = future.result()
                except Exception as exc:
                    result = {
                        "model": model_dir.name, "status": "error", "error_message": str(exc),
                        "mutation_score": None, "total_mutants_in_file": None,
                        "total_mutants_in_properties": None, "total_mutants_generated": None,
                        "mutants_run": None, "killed": None, "survived": None, "other_outcomes": {},
                        "init_duration_s": None, "exec_duration_s": None,
                    }
                results.append(result)
                cache_file.write(json.dumps(result) + "\n")
                cache_file.flush()
                done += 1
                print(f"  {done}/{total}: {model_dir.name} -> {result['status']}"
                      + (f" ({result['killed']}/{result['mutants_run']} killed)" if result.get("mutants_run") else ""),
                      flush=True)
    finally:
        cache_file.close()
        shutil.rmtree(hypothesis_home, ignore_errors=True)
        shutil.rmtree(scratch_root, ignore_errors=True)

    if args.write_metadata:
        written = 0
        for result in results:
            if result["status"] == "measured":
                model_dir = args.dataset_dir / result["model"]
                if write_metadata(model_dir, result):
                    written += 1
        print(f"Wrote {METADATA_KEY} into {written}/{len(results)} models' code_metadata.json")

    report = build_report(results)
    args.reports_dir.mkdir(parents=True, exist_ok=True)
    json_path = args.reports_dir / f"{args.report_name}.json"
    json_path.write_text(json.dumps(report, indent=2) + "\n")
    md_path = args.reports_dir / f"{args.report_name}.md"
    md_path.write_text(render_markdown_report(report))

    print()
    print(f"Measured: {report['measured_count']}/{report['total_models']}")
    print(f"Avg mutation score (properties only): {report['avg_mutation_score']}")
    print(f"Avg share of file's mutants that are in properties: {report['avg_property_mutant_share']}")
    print(f"Duration p50/p90/max: {report['duration_stats_s']['p50']}/{report['duration_stats_s']['p90']}/{report['duration_stats_s']['max']}s")
    print(f"Report written to {json_path} and {md_path}")


if __name__ == "__main__":
    main()
