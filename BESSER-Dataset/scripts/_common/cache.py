"""Shared JSONL-cache-with-resume helpers.

Consolidates two bugs found and fixed independently, inconsistently, in
different scripts over this project's history (see docs/DECISIONS.md):
- 2026-09-16: a cached result can be stale if the same --report-name was
  reused with a different --test-file (load_cache's expected_test_file
  check).
- 2026-10-01: a transient failure ("error"/"timeout"/etc.) should not be
  treated as permanently done -- the next run under the same --report-name
  should retry it automatically (partition_cache's retriable split).
A 2026-10-17 code-review pass found the first fix had reached only 4 of 17
cache-using scripts, and the second only 7 of 17 -- centralizing both here
means every script that adopts load_cache()/partition_cache() gets both
fixes for free, instead of needing yet another rollout pass per bug.
"""
from __future__ import annotations

import json
from pathlib import Path


def load_cache(cache_path: Path, expected_test_file: str | None = None) -> dict[str, dict]:
    """Read a JSONL cache of previously-completed results, keyed by model name.

    Tolerates a truncated last line (e.g. the process was killed mid-write)
    by skipping any line that fails to parse.

    If `expected_test_file` is given, a cached entry recorded against a
    DIFFERENT test file is dropped (forced to recompute) instead of being
    silently reused. Entries written before this field existed (no
    "test_file" key) are trusted as before.
    """
    cached: dict[str, dict] = {}
    stale = 0
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
            recorded_test_file = result.get("test_file")
            if expected_test_file and recorded_test_file and recorded_test_file != expected_test_file:
                stale += 1
                continue
            cached[result["model"]] = result
    if stale:
        print(f"Ignored {stale} cached result(s) recorded against a different --test-file "
              f"than this run ({expected_test_file!r}) -- recomputing them instead of "
              f"silently reusing stale data.")
    return cached


def partition_cache(
    cached: dict[str, dict],
    retriable_statuses: frozenset[str],
) -> tuple[dict[str, dict], dict[str, dict]]:
    """Splits a loaded cache into (done, retriable) by each entry's
    "status" field. Callers should treat `retriable` models as NOT yet
    done (i.e. still feed them to the worker pool) so a re-run under the
    same --report-name automatically retries them -- no separate
    --report-name/manual merge needed. Returns (done, retriable)."""
    retriable = {m: r for m, r in cached.items() if r.get("status") in retriable_statuses}
    done = {m: r for m, r in cached.items() if m not in retriable}
    return done, retriable
