#!/usr/bin/env python3
"""Convert each model's BUML source into a PlantUML (`.puml`) text file.

Requires `besser` installed (pip install besser) -- NOT the same venv used by
validate_mutation.py: besser pulls in a large, unrelated dependency tree
(Django, FastAPI, Docker, cryptography, ...) and pins pytest<9, so it should
live in its own virtualenv to avoid downgrading pytest for mutation testing.

Two BUML source filename conventions exist across this dataset's generation
batches, confirmed empirically across all 9,082 models (no gaps, no overlap):
- `<domain>_BUML_model.py`  -- 5,990 models
- `<dirname>_buml.py`       -- 3,092 models
Both must be checked, or a third of the dataset is silently skipped.

The conversion logic (load the DomainModel, then emit `.puml` text) is a
close relative of a walker/visitor/iterator implementation from an earlier,
separate repo (shrinking-corp/dataset-with-iterator, BumlToPuml/), kept here
as plain functions instead -- no ABC/visitor/walker classes, just
load_domain_model() + generate_puml(). The one thing carried over verbatim
is *why* every collection gets sorted: BUML's model.types / class.attributes
/ class.methods / association.ends etc. are plain Python sets with no stable
iteration order, so skipping the sorts would make output non-reproducible
between runs on an otherwise-unchanged model. That old repo's compatibility
rewrite for legacy constructor calls (DomainModel(...) etc.) was tested and
found unnecessary against this dataset + besser 7.13.0 -- all 13 sampled
models across both filename conventions loaded cleanly without it.

Output: `<same-stem-as-source>.puml` written next to the BUML source file in
its model directory (matching the sibling repo's own convention).

Usage:
    python scripts/buml_to_puml.py --models-file PATH [--workers N]
        [--dataset-dir PATH] [--reports-dir PATH] [--report-name NAME]
        [--limit N] [--fresh]
"""
from __future__ import annotations

import argparse
import concurrent.futures
import datetime
import importlib.util
import json
import platform
import sys
import time
import uuid
from pathlib import Path

from besser.BUML.metamodel.project import Project
from besser.BUML.metamodel.structural import AssociationClass, BinaryAssociation, Class, DomainModel, Enumeration

OLD_GLOB = "*_BUML_model.py"
NEW_GLOB = "*_buml.py"


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


def find_buml_file(model_dir: Path) -> Path | None:
    matches = list(model_dir.glob(OLD_GLOB)) or list(model_dir.glob(NEW_GLOB))
    return matches[0] if matches else None


def load_domain_model(file_path: Path):
    module_name = f"buml_model_{uuid.uuid4().hex}"
    spec = importlib.util.spec_from_file_location(module_name, str(file_path))
    if spec is None or spec.loader is None:
        raise ValueError(f"Could not load Python module from path: {file_path}")

    module = importlib.util.module_from_spec(spec)
    sys.modules[module_name] = module
    try:
        spec.loader.exec_module(module)
    finally:
        sys.modules.pop(module_name, None)

    for value in vars(module).values():
        if isinstance(value, DomainModel):
            return value
    for value in vars(module).values():
        if isinstance(value, Project) and value.models:
            return value.models[0]

    raise ValueError(f"No DomainModel found in {file_path}")


def _type_name(value) -> str:
    return value.name if hasattr(value, "name") else str(value)


def _visibility_symbol(value) -> str:
    visibility = str(value) if value else "public"
    return "+" if visibility == "public" else "-" if visibility == "private" else "#" if visibility == "protected" else "~"


def _association_symbol(end1, end2) -> str:
    if getattr(end2, "is_composite", False):
        return "*--"
    if getattr(end1, "is_composite", False):
        return "--*"
    if getattr(end2, "is_aggregation", False):
        return "o--"
    if getattr(end1, "is_aggregation", False):
        return "--o"
    if getattr(end1, "is_navigable", False) and not getattr(end2, "is_navigable", False):
        return "<--"
    if getattr(end2, "is_navigable", False) and not getattr(end1, "is_navigable", False):
        return "-->"
    return "--"


def _multiplicity_label(end) -> str:
    multiplicity = getattr(end, "multiplicity", None)
    if multiplicity is None:
        return '""'
    return f'"{getattr(multiplicity, "min", "")}..{getattr(multiplicity, "max", "")}"'


def _ordered_ends(association):
    """Deterministic (end1, end2) pair -- association.ends is an unordered 2-item set."""
    ends = list(getattr(association, "ends", []))
    if len(ends) != 2:
        return None

    def end_key(end):
        multiplicity = getattr(end, "multiplicity", None)
        return (
            _type_name(getattr(end, "type", "")),
            str(getattr(end, "name", "")),
            str(getattr(multiplicity, "min", "")),
            str(getattr(multiplicity, "max", "")),
            bool(getattr(end, "is_navigable", False)),
            bool(getattr(end, "is_composite", False)),
            bool(getattr(end, "is_aggregation", False)),
        )

    ordered = sorted(ends, key=end_key)
    return ordered[0], ordered[1]


def generate_puml(model) -> str:
    lines: list[str] = ["@startuml"]

    types = sorted((t for t in model.types if isinstance(t, (Class, Enumeration))), key=_type_name)

    for model_type in types:
        if isinstance(model_type, Class):
            class_prefix = "abstract class" if model_type.is_abstract else "class"
            lines.append(f"{class_prefix} {model_type.name} {{")

            for attr in sorted(model_type.attributes, key=_type_name):
                attr_type = _type_name(getattr(attr, "type", ""))
                lines.append(f"  {_visibility_symbol(getattr(attr, 'visibility', None))} {attr.name} : {attr_type}")

            for method in sorted(model_type.methods, key=_type_name):
                params = [
                    f"{p.name} : {_type_name(getattr(p, 'type', ''))}"
                    for p in sorted(getattr(method, "parameters", []), key=_type_name)
                ]
                return_type = _type_name(getattr(method, "type", "void")) if getattr(method, "type", None) else "void"
                lines.append(
                    f"  {_visibility_symbol(getattr(method, 'visibility', None))} {method.name}({', '.join(params)}) : {return_type}"
                )

            lines.append("}")
        elif isinstance(model_type, Enumeration):
            lines.append(f"enum {model_type.name} {{")
            for literal in sorted(model_type.literals, key=_type_name):
                lines.append(f"  {literal.name}")
            lines.append("}")

    association_classes = sorted((t for t in types if isinstance(t, AssociationClass)), key=_type_name)
    for assoc_class in association_classes:
        association = getattr(assoc_class, "association", None)
        if association is None:
            continue
        ordered = _ordered_ends(association)
        if ordered is None:
            continue
        end1, end2 = ordered
        lines.append(f"({_type_name(end1.type)}, {_type_name(end2.type)}) .. {assoc_class.name}")

    generalizations = sorted(model.generalizations, key=lambda g: f"{_type_name(g.general)}::{_type_name(g.specific)}")
    for gen in generalizations:
        lines.append(f"{gen.general.name} <|-- {gen.specific.name}")

    binary_associations = sorted(
        (a for a in model.associations if isinstance(a, BinaryAssociation)), key=_type_name
    )
    for assoc in binary_associations:
        ordered = _ordered_ends(assoc)
        if ordered is None:
            continue
        end1, end2 = ordered
        type1_name = _type_name(end1.type)
        type2_name = _type_name(end2.type)
        label1 = _multiplicity_label(end1)
        label2 = _multiplicity_label(end2)
        symbol = _association_symbol(end1, end2)
        assoc_name = str(getattr(assoc, "name", ""))
        if assoc_name:
            lines.append(f"{type1_name} {label1} {symbol} {label2} {type2_name} : {assoc_name}")
        else:
            lines.append(f"{type1_name} {label1} {symbol} {label2} {type2_name}")

    lines.append("@enduml")
    return "\n".join(lines)


def convert_model(model_dir: Path) -> dict:
    checked_at = datetime.datetime.now(datetime.timezone.utc).isoformat()
    result = {
        "model": model_dir.name,
        "checked_at": checked_at,
        "python_version": platform.python_version(),
        "status": "missing_file",
        "buml_source": None,
        "output_file": None,
        "duration_s": None,
        "error_message": None,
    }

    buml_file = find_buml_file(model_dir)
    if buml_file is None:
        result["error_message"] = f"No {OLD_GLOB} or {NEW_GLOB} file found in {model_dir.name}"
        return result
    result["buml_source"] = buml_file.name

    start = time.monotonic()
    try:
        model = load_domain_model(buml_file)
        puml_text = generate_puml(model)
        output_path = buml_file.with_suffix(".puml")
        output_path.write_text(puml_text)
        result["status"] = "converted"
        result["output_file"] = output_path.name
    except Exception as exc:
        result["status"] = "error"
        result["error_message"] = str(exc)
    result["duration_s"] = round(time.monotonic() - start, 3)
    return result


def build_report(results: list[dict]) -> dict:
    total = len(results)
    by_status: dict[str, int] = {}
    for r in results:
        by_status[r["status"]] = by_status.get(r["status"], 0) + 1
    durations = sorted(r["duration_s"] for r in results if r.get("duration_s") is not None)

    def pct(vals, p):
        if not vals:
            return None
        idx = min(len(vals) - 1, int(len(vals) * p / 100))
        return round(vals[idx], 3)

    return {
        "generated_at": datetime.datetime.now(datetime.timezone.utc).isoformat(),
        "total_models": total,
        "by_status": by_status,
        "converted_count": by_status.get("converted", 0),
        "duration_stats_s": {
            "p50": pct(durations, 50),
            "p90": pct(durations, 90),
            "max": durations[-1] if durations else None,
            "total": round(sum(durations), 2),
        },
        "results": results,
    }


def render_markdown_report(report: dict) -> str:
    lines = [
        "# BUML to PUML Conversion Report",
        "",
        f"Generated: {report['generated_at']}",
        "",
        f"- **Total models:** {report['total_models']}",
        f"- **Converted:** {report['converted_count']}",
        f"- **Duration p50/p90/max (s):** {report['duration_stats_s']['p50']}/"
        f"{report['duration_stats_s']['p90']}/{report['duration_stats_s']['max']}",
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
    parser.add_argument(
        "--dataset-dir", type=Path,
        default=Path(__file__).resolve().parent.parent / "Dataset",
    )
    parser.add_argument(
        "--reports-dir", type=Path,
        default=Path(__file__).resolve().parent.parent / "reports",
    )
    parser.add_argument("--models-file", type=Path, default=None)
    parser.add_argument("--report-name", type=str, default="buml_to_puml_report")
    parser.add_argument("--workers", type=int, default=8)
    parser.add_argument("--limit", type=int, default=None)
    parser.add_argument("--fresh", action="store_true",
                         help="Ignore any existing cache and recompute every model")
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

    print(f"Converting {total} models to PUML with {args.workers} workers...")
    if skipped:
        print(f"Resuming from cache: {skipped}/{total} already done, {len(model_dirs)} remaining "
              f"(pass --fresh to ignore the cache and recompute everything)")

    results: list[dict] = list(cached_results.values())
    done = skipped
    cache_file = cache_path.open("a")
    try:
        with concurrent.futures.ProcessPoolExecutor(max_workers=args.workers) as executor:
            futures = {executor.submit(convert_model, model_dir): model_dir for model_dir in model_dirs}
            for future in concurrent.futures.as_completed(futures):
                model_dir = futures[future]
                try:
                    result = future.result()
                except Exception as exc:
                    result = {
                        "model": model_dir.name, "status": "error", "error_message": str(exc),
                        "buml_source": None, "output_file": None, "duration_s": None,
                    }
                results.append(result)
                cache_file.write(json.dumps(result) + "\n")
                cache_file.flush()
                done += 1
                print(f"  {done}/{total}: {model_dir.name} -> {result['status']}", flush=True)
    finally:
        cache_file.close()

    report = build_report(results)
    json_path = args.reports_dir / f"{args.report_name}.json"
    json_path.write_text(json.dumps(report, indent=2) + "\n")
    md_path = args.reports_dir / f"{args.report_name}.md"
    md_path.write_text(render_markdown_report(report))

    print()
    print(f"Converted: {report['converted_count']}/{report['total_models']}")
    print(f"Report written to {json_path} and {md_path}")


if __name__ == "__main__":
    main()
