"""Shared per-model worker pool with an append-as-you-go JSONL cache.

Every generate_*/validate_* script runs one worker function per model in a
ProcessPoolExecutor and appends each result to `<report-name>.cache.jsonl`
the moment it finishes, so an interrupted multi-hour run loses nothing (see
docs/DECISIONS.md 2026-09-01). That loop used to be copy-pasted into ~21
scripts with subtly different crash handling; it lives here once.

Windows note: workers use 'spawn' and re-import the calling script, so
`worker` must be a module-level function of that script and any per-run
configuration it reads from globals must already be in os.environ before
this is called (see validate_mutation.py's TEST_FILENAME comment).
"""
from __future__ import annotations

import concurrent.futures
import json
from collections.abc import Callable
from pathlib import Path


def run_models(
    worker: Callable[..., dict],
    model_dirs: list[Path],
    *,
    worker_args: tuple = (),
    workers: int,
    cache_path: Path,
    results: list[dict],
    already_done: int = 0,
    total: int | None = None,
    error_fields: dict | None = None,
    describe: Callable[[dict], str] | None = None,
) -> list[dict]:
    """Runs `worker(model_dir, *worker_args)` for every model in `model_dirs`.

    Each result is appended to `results` (pre-seeded by the caller with any
    cached results) and to `cache_path` immediately. A worker that raises is
    recorded as {"model", "status": "error", "error_message"} plus
    `error_fields` (e.g. None-valued metric keys the caller's report code
    expects on every result). Progress: with `describe`, one line per model
    (`n/total: model -> status<describe(result)>`); without it, a line every
    500 models. Returns `results`.
    """
    total = total if total is not None else already_done + len(model_dirs)
    done = already_done
    with cache_path.open("a") as cache_file, \
            concurrent.futures.ProcessPoolExecutor(max_workers=workers) as executor:
        futures = {executor.submit(worker, model_dir, *worker_args): model_dir for model_dir in model_dirs}
        for future in concurrent.futures.as_completed(futures):
            model_dir = futures[future]
            try:
                result = future.result()
            except Exception as exc:
                result = {"model": model_dir.name, "status": "error", "error_message": str(exc),
                          **(error_fields or {})}
            results.append(result)
            cache_file.write(json.dumps(result) + "\n")
            cache_file.flush()
            done += 1
            if describe is not None:
                print(f"  {done}/{total}: {model_dir.name} -> {result['status']}{describe(result)}", flush=True)
            elif done % 500 == 0 or done == total:
                print(f"  {done}/{total} processed", flush=True)
    return results
