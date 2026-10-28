#!/usr/bin/env python3
"""Build the benchmarking-ready copy of the dataset from a split made by
`make_benchmark_split.py`. The research `Dataset/` is only read, never
changed; the copy is what the benchmarking repo clones.

**What goes in is configured in `benchmark_export.toml`** (repo root), not
in this script:
  - per-model files (optionally only some top-level keys of a JSON file),
  - values copied into each model's manifest entry,
  - repo files shipped once (e.g. scripts the benchmark runs on generated code).
Add or remove an item there; the pre-check, manifest.json and README follow
it. The file itself documents the fields.

Layout:

    <output-dir>/
      manifest.json           split parameters, buckets, source commit, the
                              export config, and one entry per model
      README.md               generated from the config
      train.txt, test.txt     the model names on each side
      benchmark_export.toml   the config this export was made with
      train/<model>/ and test/<model>/   the configured per-model files
      <shared files>          wherever the config puts them

Everything is checked before anything is written: a model missing a
required file (or a required JSON key) aborts the export with the full list,
so a copy is never half-built. Optional files are exported where present
and listed per model under `absent` otherwise.

Usage:
    python scripts/export_benchmark_dataset.py --output-dir PATH
        [--config benchmark_export.toml] [--split-report reports/benchmark_split.json]
        [--dataset-dir PATH] [--force]
"""
from __future__ import annotations

import argparse
import datetime
import json
import shutil
import subprocess
import sys
import tomllib
from dataclasses import asdict, dataclass
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from _common.buml import find_buml_file  # noqa: E402
from _common.io import add_common_io_args  # noqa: E402

CONFIG_FILENAME = "benchmark_export.toml"
IGNORED = shutil.ignore_patterns("__pycache__", ".hypothesis", ".coverage", ".pytest_cache")
ENTRY_KEYS = {"model", "split", "bucket", "difficulty_score", "path", "files", "absent"}


@dataclass(frozen=True)
class ModelFile:
    name: str
    source: str
    required: bool = True
    keys: tuple[str, ...] | None = None
    description: str = ""


@dataclass(frozen=True)
class ManifestField:
    name: str
    source: str
    key: str


@dataclass(frozen=True)
class SharedFile:
    name: str
    source: str
    description: str = ""


@dataclass(frozen=True)
class ExportConfig:
    model_files: list[ModelFile]
    manifest_fields: list[ManifestField]
    shared_files: list[SharedFile]


def load_config(path: Path) -> ExportConfig:
    """Parses and validates the export config; any mistake is a ValueError
    naming the section, before a single model is looked at."""
    data = tomllib.loads(path.read_text(encoding="utf-8"))
    sections = {"model_files": ModelFile, "manifest_fields": ManifestField, "shared_files": SharedFile}
    unknown = set(data) - set(sections)
    if unknown:
        raise ValueError(f"{path.name}: unknown sections {sorted(unknown)} (known: {sorted(sections)})")
    parsed = {}
    for section, cls in sections.items():
        items = []
        for i, item in enumerate(data.get(section, [])):
            if "keys" in item:
                item = {**item, "keys": tuple(item["keys"])}
            try:
                items.append(cls(**item))
            except TypeError as e:
                raise ValueError(f"{path.name}: [[{section}]] #{i + 1}: {e}") from None
        names = [it.name for it in items]
        duplicates = sorted({n for n in names if names.count(n) > 1})
        if duplicates:
            raise ValueError(f"{path.name}: [[{section}]] names used twice: {duplicates}")
        parsed[section] = items
    clashes = sorted({f.name for f in parsed["manifest_fields"]} & ENTRY_KEYS)
    if clashes:
        raise ValueError(f"{path.name}: [[manifest_fields]] names {clashes} are already manifest entry keys")
    if not parsed["model_files"]:
        raise ValueError(f"{path.name}: no [[model_files]] configured")
    return ExportConfig(**parsed)


def locate(model_dir: Path, source: str) -> Path | None:
    if source == "@puml":
        pumls = sorted(model_dir.glob("*.puml"))
        return pumls[0] if pumls else None
    if source == "@buml":
        return find_buml_file(model_dir)
    path = model_dir / source
    return path if path.exists() else None


def read_json(path: Path) -> dict | None:
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError, UnicodeDecodeError):
        return None
    return data if isinstance(data, dict) else None


def dotted(data: dict | None, key: str):
    for part in key.split("."):
        if not isinstance(data, dict) or part not in data:
            return None
        data = data[part]
    return data


def plan_model(model_dir: Path, config: ExportConfig) -> tuple[list, list[str], list[str], dict]:
    """(copy actions, problems, absent optional files, manifest field values)
    for one model. An action is (exported name, source path, filtered JSON
    payload or None)."""
    actions, problems, absent = [], [], []
    for item in config.model_files:
        path = locate(model_dir, item.source)
        if path is None:
            (problems if item.required else absent).append(item.name)
            continue
        if item.keys is None:
            actions.append((item.name, path, None))
            continue
        data = read_json(path)
        if data is None:
            (problems if item.required else absent).append(f"{item.name} (unreadable JSON)")
            continue
        selected = {k: data[k] for k in item.keys if k in data}
        missing_keys = [k for k in item.keys if k not in data]
        if item.required and missing_keys:
            problems.append(f"{item.name} (keys {missing_keys} missing in {path.name})")
        elif not selected:
            absent.append(item.name)
        else:
            actions.append((item.name, path, selected))
    cache: dict[str, dict | None] = {}
    fields = {}
    for field in config.manifest_fields:
        if field.source not in cache:
            path = model_dir / field.source
            cache[field.source] = read_json(path) if path.is_file() else None
        fields[field.name] = dotted(cache[field.source], field.key)
    return actions, problems, absent, fields


def copy_path(source: Path, target: Path) -> None:
    target.parent.mkdir(parents=True, exist_ok=True)
    if source.is_dir():
        shutil.copytree(source, target, ignore=IGNORED)
    else:
        shutil.copy2(source, target)


def source_commit(repo_root: Path) -> str | None:
    try:
        result = subprocess.run(["git", "rev-parse", "HEAD"], cwd=repo_root, capture_output=True, text=True, timeout=10)
    except (OSError, subprocess.SubprocessError):
        return None
    if result.returncode != 0:
        return None
    return result.stdout.strip() or None


def render_readme(manifest: dict, config: ExportConfig) -> str:
    counts = manifest["counts"]
    lines = [
        "# Benchmark dataset",
        "",
        f"Exported {manifest['exported_at']} from the BESSER dataset repo"
        + (f" (commit `{manifest['source_commit']}`)" if manifest["source_commit"] else "") + ".",
        f"{counts['train']} train and {counts['test']} test models, stratified by difficulty bucket "
        f"(train ratio {manifest['split']['train_ratio']}, seed {manifest['split']['seed']}). "
        "Each model is a distinct model of the source dataset: copies of the same original BUML "
        "model were removed before the split.",
        "",
        "Each `train/<model>/` and `test/<model>/` folder holds:",
        "",
    ]
    for item in config.model_files:
        optional = "" if item.required else " (optional: not every model has it, see `absent` in the manifest)"
        lines.append(f"- `{item.name}` -- {item.description or item.source}{optional}")
    if config.shared_files:
        lines += ["", "Shared files:", ""]
        lines += [f"- `{s.name}` -- {s.description or s.source}" for s in config.shared_files]
    extra = [f.name for f in config.manifest_fields]
    lines += [
        "",
        "`train.txt` / `test.txt` list the models on each side. `manifest.json` lists every model "
        "with its split, difficulty bucket, difficulty score, folder path"
        + (f", {', '.join(f'`{n}`' for n in extra)}" if extra else "")
        + " and the original file names; it also records the split parameters and this export's config "
        "(`benchmark_export.toml`).",
        "",
    ]
    return "\n".join(lines)


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    add_common_io_args(parser, __file__)
    repo_root = Path(__file__).resolve().parent.parent
    parser.add_argument("--output-dir", type=Path, required=True)
    parser.add_argument("--config", type=Path, default=repo_root / CONFIG_FILENAME)
    parser.add_argument("--split-report", type=Path, default=None,
                        help="Default: <reports-dir>/benchmark_split.json")
    parser.add_argument("--force", action="store_true", help="Replace an existing, non-empty output directory")
    args = parser.parse_args()

    dataset_dir = args.dataset_dir.resolve()
    output_dir = args.output_dir.resolve()
    if output_dir == dataset_dir or dataset_dir in output_dir.parents or output_dir in dataset_dir.parents:
        parser.error("--output-dir must be outside the dataset directory")
    if output_dir.exists() and any(output_dir.iterdir()) and not args.force:
        parser.error(f"{output_dir} is not empty (pass --force to replace it)")
    try:
        config = load_config(args.config)
    except (OSError, ValueError, tomllib.TOMLDecodeError) as e:
        parser.error(f"export config: {e}")

    split_path = args.split_report or args.reports_dir / "benchmark_split.json"
    split = json.loads(split_path.read_text(encoding="utf-8"))
    assignments = split["assignments"]

    plan, problems = [], []
    for a in assignments:
        actions, model_problems, absent, fields = plan_model(dataset_dir / a["model"], config)
        if model_problems:
            problems.append(f"{a['model']}: missing {', '.join(model_problems)}")
        plan.append((a, actions, absent, fields))
    for shared in config.shared_files:
        if not (repo_root / shared.source).exists():
            problems.append(f"shared file {shared.name}: {shared.source} not found in the repo")
    if problems:
        print(f"Export aborted, {len(problems)} problems:")
        for line in problems[:50]:
            print(f"  {line}")
        if len(problems) > 50:
            print(f"  ... and {len(problems) - 50} more")
        sys.exit(1)

    if output_dir.exists():
        shutil.rmtree(output_dir)
    output_dir.mkdir(parents=True)
    entries = []
    for a, actions, absent, fields in plan:
        target = output_dir / a["split"] / a["model"]
        target.mkdir(parents=True)
        for name, source, payload in actions:
            if payload is None:
                copy_path(source, target / name)
            else:
                (target / name).write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
        entries.append({
            "model": a["model"], "split": a["split"], "bucket": a["bucket"],
            "difficulty_score": a["difficulty_score"],
            "path": f"{a['split']}/{a['model']}",
            **fields,
            "files": {name: source.name for name, source, _payload in actions},
            "absent": absent,
        })
    for shared in config.shared_files:
        copy_path(repo_root / shared.source, output_dir / shared.name)
    shutil.copy2(args.config, output_dir / CONFIG_FILENAME)
    for side in ("train", "test"):
        names = sorted(e["model"] for e in entries if e["split"] == side)
        (output_dir / f"{side}.txt").write_text("".join(f"{n}\n" for n in names), encoding="utf-8")

    manifest = {
        "exported_at": datetime.datetime.now(datetime.timezone.utc).isoformat(),
        "source_commit": source_commit(repo_root),
        "split_report": str(split_path),
        "split": split["parameters"],
        "counts": {"train": sum(e["split"] == "train" for e in entries),
                   "test": sum(e["split"] == "test" for e in entries)},
        "buckets": split["buckets"],
        "export_config": asdict(config),
        "models": entries,
    }
    (output_dir / "manifest.json").write_text(json.dumps(manifest, indent=2) + "\n", encoding="utf-8")
    (output_dir / "README.md").write_text(render_readme(manifest, config), encoding="utf-8")
    absent_total = sum(len(e["absent"]) for e in entries)
    print(f"Exported {len(entries)} models ({manifest['counts']['train']} train, "
          f"{manifest['counts']['test']} test) to {output_dir}"
          + (f"; {absent_total} optional files absent (see manifest)" if absent_total else ""))


if __name__ == "__main__":
    main()
