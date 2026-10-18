"""Shared I/O helpers: reading --models-file / python_code.py text safely,
and resolving which model directories a run should process.
"""
from __future__ import annotations

import argparse
import json
from collections.abc import Iterator
from pathlib import Path

MODEL_METADATA_FILENAME = "model_metadata.json"


def read_text_robust(path: Path) -> str:
    """Reads a text file regardless of which BOM (if any) Windows wrote --
    confirmed real (2026-10-12): PowerShell's `echo >` defaults to UTF-16LE
    with BOM, `Out-File -Encoding utf8` defaults to UTF-8 WITH BOM (neither
    matches plain `.read_text()`'s assumption) -- `encoding="utf-8-sig"`
    alone only covers the UTF-8 case, not UTF-16, so a `--models-file`
    created with plain `echo` silently corrupts the first model name AND
    throws off line-splitting entirely (one line becomes several, since
    UTF-16 is 2 bytes/char). Sniffs the actual BOM bytes rather than
    guessing from one case."""
    raw = path.read_bytes()
    if raw.startswith(b"\xff\xfe") or raw.startswith(b"\xfe\xff"):
        return raw.decode("utf-16")
    if raw.startswith(b"\xef\xbb\xbf"):
        return raw.decode("utf-8-sig")
    return raw.decode("utf-8")


def read_model_names(models_file: Path) -> list[str]:
    """Model names from a --models-file, one per line, blank lines ignored."""
    return [l.strip() for l in read_text_robust(models_file).splitlines() if l.strip()]


def find_model_dirs(dataset_dir: Path, models_file: Path | None, limit: int | None) -> list[Path]:
    """Resolves the list of model directories to process: explicit
    --models-file (one model name per line) if given, else every
    subdirectory of dataset_dir, sorted. --limit (if given) is applied
    last, after either source."""
    if models_file:
        dirs = [dataset_dir / name for name in read_model_names(models_file)]
    else:
        dirs = sorted(p for p in dataset_dir.iterdir() if p.is_dir())
    if limit:
        dirs = dirs[:limit]
    return dirs


def iter_measured_models(dataset_dir: Path, only: set[str] | None = None) -> Iterator[tuple[str, Path, dict]]:
    """Yields (model_name, model_metadata_path, parsed_metadata) for every
    model whose `model_metadata.json` has status "measured" (restricted to
    `only` if given), sorted by model name -- a fixed order, which the
    difficulty-score PCA needs for determinism (directory-listing order isn't
    guaranteed stable). Missing or unparseable metadata files are skipped.
    Callers that later rewrite the file should reuse the yielded dict instead
    of re-reading it."""
    for model_dir in sorted(dataset_dir.iterdir(), key=lambda p: p.name):
        if only is not None and model_dir.name not in only:
            continue
        path = model_dir / MODEL_METADATA_FILENAME
        if not path.is_file():
            continue
        try:
            data = json.loads(path.read_text(encoding="utf-8"))
        except (json.JSONDecodeError, UnicodeDecodeError):
            continue
        if data.get("status") == "measured":
            yield model_dir.name, path, data


def update_json_key(path: Path, key: str, payload: object) -> bool:
    """Sets one top-level `key` in an existing JSON file (a model's
    code_metadata.json / model_metadata.json), leaving every other key
    untouched. Never creates the file -- returns False if it's missing or
    unreadable. Explicit UTF-8 both ways: the Windows locale default can fail
    on non-ASCII text inside stored error messages, which used to be able to
    crash a run at the very end, after every result was computed."""
    if not path.is_file():
        return False
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except (json.JSONDecodeError, UnicodeDecodeError):
        return False
    data[key] = payload
    path.write_text(json.dumps(data, indent=2) + "\n", encoding="utf-8")
    return True


def add_common_io_args(parser: argparse.ArgumentParser, script_file: str) -> None:
    """Adds the --dataset-dir/--reports-dir pair nearly every script here
    shares, defaulting relative to the repo root (two directories up from
    the calling script, i.e. scripts/<script_file>'s own parent.parent).
    Pass __file__ from the caller as script_file."""
    repo_root = Path(script_file).resolve().parent.parent
    parser.add_argument("--dataset-dir", type=Path, default=repo_root / "Dataset")
    parser.add_argument("--reports-dir", type=Path, default=repo_root / "reports")
