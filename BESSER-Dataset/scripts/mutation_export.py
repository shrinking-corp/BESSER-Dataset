"""Shared helper: export full detail of SURVIVED mutants from a cosmic-ray
session db before the scratch copy holding it is discarded.

`validate_mutation.py`/`validate_mutation_properties.py` only ever read a
*count* of survived mutants out of the session sqlite db (see their
`read_results()`) -- enough for a mutation score, but nothing to act on.
the LLM-driven track of the test-generation comparison needs the actual mutant detail:
which line, which operator, what the diff looked like. cosmic-ray keeps
exactly that (`mutation_specs` + `work_results.diff`, see
`cosmic_ray/work_db.py`), but only inside the session db, which lives in a
scratch copy deleted right after each model finishes.

This module supplies one function, called from `validate_model()` in both
scripts, in the same worker process, before their `finally: shutil.rmtree(...)`
discards the scratch copy.
"""
from __future__ import annotations

import json
import sqlite3
from pathlib import Path


def export_surviving_mutants(
    session_path: Path, export_dir: Path, model_name: str, test_filename: str,
) -> int:
    """Write `<export_dir>/<model_name>.json` with every SURVIVED mutant's
    detail for this model (module, line range, operator, args, and the
    unified diff cosmic-ray recorded for that specific mutant).

    Returns how many mutants were exported. Writes no file at all when 0
    (nothing survived, or nothing had a result yet -- e.g. a timed-out run).
    """
    con = sqlite3.connect(str(session_path))
    try:
        cur = con.cursor()
        cur.execute(
            """
            SELECT ms.job_id, ms.module_path, ms.operator_name, ms.operator_args,
                   ms.occurrence, ms.start_pos_row, ms.start_pos_col,
                   ms.end_pos_row, ms.end_pos_col, ms.definition_name,
                   wr.diff
            FROM mutation_specs ms
            JOIN work_results wr ON wr.job_id = ms.job_id
            WHERE wr.test_outcome = 'SURVIVED'
            """
        )
        rows = cur.fetchall()
    finally:
        con.close()

    if not rows:
        return 0

    mutants = []
    for (job_id, module_path, operator_name, operator_args, occurrence,
         start_row, start_col, end_row, end_col, definition_name, diff) in rows:
        try:
            args = json.loads(operator_args) if operator_args else None
        except json.JSONDecodeError:
            args = operator_args
        mutants.append({
            "job_id": job_id,
            "module_path": module_path,
            "operator_name": operator_name,
            "operator_args": args,
            "occurrence": occurrence,
            "start_pos": [start_row, start_col],
            "end_pos": [end_row, end_col],
            "definition_name": definition_name,
            "diff": diff,
        })

    export_dir.mkdir(parents=True, exist_ok=True)
    payload = {
        "model": model_name,
        "test_file": test_filename,
        "survived_count": len(mutants),
        "mutants": mutants,
    }
    (export_dir / f"{model_name}.json").write_text(json.dumps(payload, indent=2) + "\n")
    return len(mutants)
