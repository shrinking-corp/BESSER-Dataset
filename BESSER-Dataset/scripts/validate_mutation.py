#!/usr/bin/env python3
"""Measure mutation score of `test_hypothesis.py` against `python_code.py`.

Uses cosmic-ray (not mutmut): a manual comparison on a sample model found
that mutmut structurally cannot mutate `@property`/`@x.setter`-decorated
methods (its trampoline mechanism breaks on decorators, not a config
limitation) -- and this dataset's bidirectional-association logic lives
almost entirely in property setters, not `__init__`. cosmic-ray mutates
that code too, at the cost of a full test-suite subprocess run per mutant
(no coverage-guided/test-impact skipping), so mutant counts are capped per
model (--max-mutants) to bound cost. See docs/DECISIONS.md.

IMPORTANT SAFETY NOTE: cosmic-ray mutates the target file **in place on
disk** and only reverts it after each mutant's test run completes. If the
process is interrupted (killed, crashes, OOM) mid-mutant, the file is left
mutated on disk. An earlier version of this script ran cosmic-ray directly
against `Dataset/<model>/python_code.py` and a `pkill` mid-run left 8
models' `python_code.py` permanently mutated until caught via `git status`
and restored with `git checkout --`. To make that class of bug impossible,
this script NEVER runs cosmic-ray against the real dataset directory: for
each model it copies just `python_code.py` + `test_hypothesis.py` (the only
two files test_hypothesis.py ever imports -- verified across a sample) into
a throwaway scratch directory, runs cosmic-ray there, and discards the
scratch directory afterward. The real `Dataset/` tree is opened read-only.

For each model:
  1. Copy python_code.py + test_hypothesis.py into a fresh scratch dir.
  2. Write a cr-config.toml + cr-session.sqlite there.
  3. `cosmic-ray init` to enumerate all possible mutants.
  4. If more than --max-mutants were generated, randomly downsample the
     `mutation_specs`/`work_items` rows in the session sqlite db (seeded by
     model name, so it's reproducible) before any test execution happens.
  5. `cosmic-ray exec` to run the (capped) mutants.
  6. Read `work_results` from the session db for kill/survive/other counts.
  7. Delete the whole scratch dir.

This is a PROTOTYPE script (see PROMPT.md): it does NOT write into each
model's code_metadata.json by default, only into an aggregate report under
reports/. Pass --write-metadata to also merge each measured model's result
into its code_metadata.json under a "mutation_validation" key (same
convention as validate_tests.py / validate_coverage_split.py: the file must
already exist, and only that one key is touched -- written in a single pass
after the whole run finishes, so an interrupted run never leaves partial
metadata).

A long run (the 250-model prototype sample took ~7 CPU-hours summed) is a
real candidate for getting killed partway -- machine reboot, SSH drop, Ctrl-C
-- and the aggregate report is only written at the very end, so without
caching an interrupted run loses all of its progress. To avoid that, every
model's result is appended as one line to a `<report-name>.cache.jsonl` file
in --reports-dir *as soon as that model finishes* (not batched). On startup,
any model already present in that cache file is skipped and its cached
result is reused for the final aggregate report; pass --fresh to ignore an
existing cache and recompute everything.

Usage:
    python scripts/validate_mutation.py --models-file PATH [--workers N]
        [--max-mutants N] [--per-mutant-timeout SECONDS]
        [--overall-timeout SECONDS] [--dataset-dir PATH] [--fresh]
        [--write-metadata]
"""
from __future__ import annotations

import argparse
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

TEST_FILENAME = "test_hypothesis.py"
SOURCE_FILENAME = "python_code.py"
CONFIG_FILENAME = "cr-config.toml"
SESSION_FILENAME = "cr-session.sqlite"
METADATA_FILENAME = "code_metadata.json"
METADATA_KEY = "mutation_validation"
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

    exec cost is ~= baseline test-suite runtime x mutants run, and mutants
    run is capped at the same --max-mutants for nearly every model, so file
    size is a free proxy for baseline runtime (measured: p50 exec is 73s,
    max is 850s for the same 40-mutant cap). Submitting the slowest models
    first (LPT scheduling) keeps a handful of them from landing at the tail
    of the run with most workers already idle.
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

    # Work entirely in a scratch copy -- cosmic-ray mutates its target file
    # in place on disk and only reverts it after each mutant's run. Never
    # point it at the real, git-tracked dataset directory (see module
    # docstring: an interruption mid-mutant previously corrupted 8 models'
    # python_code.py this way until caught by `git status` and restored).
    scratch_dir = Path(tempfile.mkdtemp(prefix=f"cr_{model_dir.name}_", dir=scratch_root))
    try:
        shutil.copy2(source_path, scratch_dir / SOURCE_FILENAME)
        shutil.copy2(test_path, scratch_dir / TEST_FILENAME)

        config_path = scratch_dir / CONFIG_FILENAME
        session_path = scratch_dir / SESSION_FILENAME
        # test-command needs two levels of backslash-safety on Windows, where
        # sys.executable is a backslash path:
        #  1. cosmic-ray itself parses this value with shlex.split() in POSIX
        #     mode (cosmic_ray/testing.py) before exec'ing it, which treats
        #     backslash as an escape character and mangles the path.
        #  2. our own TOML *double*-quoted strings do the same at load time.
        # Forward slashes are inert to both, and Windows' CreateProcess accepts
        # them in an executable path just fine, so normalize to those; the
        # double quotes around the path guard against a hypothetical space in
        # it (harmless if absent), and the TOML *literal* (single-quoted)
        # string around the whole value stops TOML from re-interpreting them.
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
    """Merge this model's mutation result into its code_metadata.json under METADATA_KEY.

    Requires the file to already exist (written by validate_python_code.py,
    the first validator to run against every model) -- same convention as
    validate_tests.py / validate_coverage_split.py: never create it here,
    and never touch any key but our own.
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

    return {
        "generated_at": datetime.datetime.now(datetime.timezone.utc).isoformat(),
        "total_models": total,
        "by_status": by_status,
        "measured_count": len(measured),
        "avg_mutation_score": round(sum(r["mutation_score"] for r in measured) / len(measured), 4) if measured else None,
        "total_mutants_generated_sum": sum(r["total_mutants_generated"] or 0 for r in results),
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
        "# Mutation Testing Prototype Report (cosmic-ray, capped)",
        "",
        f"Generated: {report['generated_at']}",
        "",
        f"- **Total models checked:** {report['total_models']}",
        f"- **Measured successfully:** {report['measured_count']}",
        f"- **Average mutation score (killed/run):** {report['avg_mutation_score']}" if report['avg_mutation_score'] is not None else "",
        f"- **Total mutants generated (uncapped) across sample:** {report['total_mutants_generated_sum']}",
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
    lines += ["", "Full per-model detail: see `mutation_prototype_report.json`."]
    return "\n".join(l for l in lines if l is not None) + "\n"


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--dataset-dir", type=Path,
        default=Path(__file__).resolve().parent.parent / "Dataset",
    )
    parser.add_argument(
        "--reports-dir", type=Path,
        default=Path(__file__).resolve().parent.parent / "reports",
    )
    parser.add_argument("--models-file", type=Path, default=None)
    parser.add_argument("--report-name", type=str, default="mutation_prototype_report")
    parser.add_argument("--workers", type=int, default=8)
    parser.add_argument("--max-mutants", type=int, default=DEFAULT_MAX_MUTANTS)
    parser.add_argument("--per-mutant-timeout", type=float, default=DEFAULT_PER_MUTANT_TIMEOUT)
    parser.add_argument("--overall-timeout", type=int, default=DEFAULT_OVERALL_TIMEOUT)
    parser.add_argument("--limit", type=int, default=None)
    parser.add_argument("--fresh", action="store_true",
                         help="Ignore any existing cache and recompute every model")
    parser.add_argument("--write-metadata", action="store_true",
                         help="Also write results into each model's code_metadata.json "
                              "(off by default -- this is a prototype script)")
    args = parser.parse_args()

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

    hypothesis_home = tempfile.mkdtemp(prefix="besser_hypothesis_db_mut_")
    scratch_root = tempfile.mkdtemp(prefix="besser_cosmicray_scratch_")
    print(f"Running capped mutation testing for {total} models with {args.workers} workers "
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
                        "mutation_score": None, "total_mutants_generated": None, "mutants_run": None,
                        "killed": None, "survived": None, "other_outcomes": {},
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
    print(f"Avg mutation score: {report['avg_mutation_score']}")
    print(f"Duration p50/p90/max: {report['duration_stats_s']['p50']}/{report['duration_stats_s']['p90']}/{report['duration_stats_s']['max']}s")
    print(f"Report written to {json_path} and {md_path}")


if __name__ == "__main__":
    main()
