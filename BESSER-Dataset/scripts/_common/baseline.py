"""Unmutated-baseline guard for mutation testing.

cosmic-ray counts a mutant as KILLED whenever the test command exits
non-zero. A suite that already fails on the UNMUTATED source therefore
"kills" every mutant and scores a fake 1.0. This happened three separate
times in this project (an invalid CrossHair test file, LLM-written tests
with wrong constructor args, and stub-double tests asserting the wrong
shape for many-valued association ends -- 155/200 sample models, see
docs/DECISIONS.md 2026-10-17), each time from a different generator. The
guard belongs in the measurement step, not in each generator, so no future
generator bug can silently inflate a score again.
"""
from __future__ import annotations

import subprocess
import sys
from pathlib import Path


def check_unmutated_suite(
    scratch_dir: Path,
    test_filename: str,
    env: dict[str, str],
    hypothesis_seed: int | None,
    timeout: float,
) -> tuple[str, str] | None:
    """Runs the exact test command cosmic-ray will use, once, against the
    unmutated source in `scratch_dir`. Returns None if it passes, else
    (status, error_message) with status "timeout" or "baseline_failed"."""
    cmd = [sys.executable, "-m", "pytest", test_filename, "-x", "-q", "-p", "no:cacheprovider"]
    if hypothesis_seed is not None:
        cmd.append(f"--hypothesis-seed={hypothesis_seed}")
    try:
        proc = subprocess.run(
            cmd, cwd=str(scratch_dir), capture_output=True, text=True, timeout=timeout, env=env,
        )
    except subprocess.TimeoutExpired:
        return "timeout", f"unmutated baseline run exceeded {timeout}s"
    if proc.returncode == 0:
        return None
    return "baseline_failed", (proc.stdout or proc.stderr or "").strip()[-1000:]
