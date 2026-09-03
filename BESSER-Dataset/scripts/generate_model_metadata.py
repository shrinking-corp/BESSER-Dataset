#!/usr/bin/env python3
"""Compute structural counts (classes, relations, etc.) from each model's BUML source
and write them to a new `model_metadata.json` file per model.

Requires `besser` installed (pip install besser) -- use a separate venv from
validate_mutation.py's; see buml_to_puml.py's docstring for why.

This is deliberately a NEW, self-contained per-model file, not another key
merged into code_metadata.json: code_metadata.json holds *validation*
results about python_code.py/test_hypothesis.py (compiles, passes tests,
coverage, mutation score); this is structural facts read directly off the
BUML *model* (the diagram), independent of whether the generated code even
compiles. Existing code_metadata.json keys are never touched by this script.

Field meanings:
- classes: every Class instance in the model, INCLUDING association classes
  (AssociationClass is a Class subtype in this metamodel -- confirmed via
  its MRO -- so excluding it would just be an undercount, not a more
  "correct" count). abstract_classes/association_classes are subset counts
  of that same total, not separate exclusive buckets.
- model.types also always contains 9 auto-injected PrimitiveDataType entries
  (int, str, bool, date, ...) regardless of whether the model uses them --
  confirmed empirically (a model with 7 explicit classes had len(model.types)
  == 16). Every count here explicitly isinstance()-filters those out.
- associations / aggregation / composition: BinaryAssociation is the only
  concrete Association subtype this metamodel defines (no NAryAssociation
  exists at all). Composition and aggregation are not separate relationship
  classes -- they're flags (is_composite / is_aggregation) on an
  association's Property ends, so classifying an association just means
  inspecting both ends' flags (composite takes priority if both are set,
  matching the PUML arrow-symbol priority used elsewhere in this dataset's
  tooling). Association *end order* doesn't matter for counting (only for
  rendering an arrow direction), so no ordering/sorting is needed here.
- Checked and confirmed UNUSED anywhere in this 9,082-model dataset (grepped
  every raw BUML source file for actual constructor calls, not just name
  matches): GeneralizationSet, NAryAssociation, Realization, Dependency,
  Package. Not included as fields -- there's nothing to count.
- OCL Constraint(...) exists in 31/9,082 models but was deliberately left
  out: it's not a relation between elements (it's a rule attached to one
  class), and at 0.3% prevalence it would be a near-constant-zero column.
- "class variables" (a Python-code-level distinction between a class-body
  assignment and a self.x = ... in __init__) has NO representation in
  BUML's metamodel at all -- Property (attributes' only concept) has no
  static/instance flag, confirmed directly from its constructor signature.
  Not recoverable from the model; deliberately out of scope here.
- "interfaces": BUML has no Interface class in its metamodel whatsoever, at
  any level -- not a scoping choice, there is nothing to read. Any
  interface-like distinction the original (pre-BUML) Ecore models may have
  had was lost in translation; every interface-like thing is indistinguishable
  from Class(is_abstract=True) in this metamodel. Not included as a
  separate field for the same reason.

Usage:
    python scripts/generate_model_metadata.py --models-file PATH [--workers N]
        [--dataset-dir PATH] [--reports-dir PATH] [--report-name NAME]
        [--limit N] [--fresh]
"""
from __future__ import annotations

import argparse
import concurrent.futures
import datetime
import importlib.metadata
import importlib.util
import json
import platform
import sys
import uuid
from pathlib import Path

from besser.BUML.metamodel.project import Project
from besser.BUML.metamodel.structural import AssociationClass, BinaryAssociation, Class, DomainModel, Enumeration

OLD_GLOB = "*_BUML_model.py"
NEW_GLOB = "*_buml.py"
METADATA_FILENAME = "model_metadata.json"


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


def compute_structure(model) -> dict:
    classes = [t for t in model.types if isinstance(t, Class)]
    enumerations = [t for t in model.types if isinstance(t, Enumeration)]
    binary_associations = [a for a in model.associations if isinstance(a, BinaryAssociation)]

    composition = 0
    aggregation = 0
    for assoc in binary_associations:
        ends = list(getattr(assoc, "ends", []))
        if any(getattr(e, "is_composite", False) for e in ends):
            composition += 1
        elif any(getattr(e, "is_aggregation", False) for e in ends):
            aggregation += 1

    return {
        "classes": len(classes),
        "abstract_classes": sum(1 for c in classes if c.is_abstract),
        "association_classes": sum(1 for c in classes if isinstance(c, AssociationClass)),
        "enumerations": len(enumerations),
        "enumeration_literals": sum(len(e.literals) for e in enumerations),
        "attributes": sum(len(c.attributes) for c in classes),
        "methods": sum(len(c.methods) for c in classes),
        "abstract_methods": sum(1 for c in classes for m in c.methods if getattr(m, "is_abstract", False)),
        "generalizations": len(model.generalizations),
        "associations": len(binary_associations),
        "aggregation": aggregation,
        "composition": composition,
    }


BESSER_VERSION = importlib.metadata.version("besser")


def process_model(model_dir: Path) -> dict:
    checked_at = datetime.datetime.now(datetime.timezone.utc).isoformat()
    result = {
        "model": model_dir.name,
        "checked_at": checked_at,
        "besser_version": BESSER_VERSION,
        "python_version": platform.python_version(),
        "status": "missing_file",
        "buml_source": None,
        "structure": None,
        "error_message": None,
    }

    buml_file = find_buml_file(model_dir)
    if buml_file is None:
        result["error_message"] = f"No {OLD_GLOB} or {NEW_GLOB} file found in {model_dir.name}"
        return result
    result["buml_source"] = buml_file.name

    try:
        model = load_domain_model(buml_file)
        result["structure"] = compute_structure(model)
        result["status"] = "measured"
    except Exception as exc:
        result["status"] = "error"
        result["error_message"] = str(exc)
        return result

    metadata_path = model_dir / METADATA_FILENAME
    payload = {
        "generated_at": result["checked_at"],
        "besser_version": result["besser_version"],
        "python_version": result["python_version"],
        "status": result["status"],
        "buml_source": result["buml_source"],
        **result["structure"],
    }
    metadata_path.write_text(json.dumps(payload, indent=2) + "\n")
    return result


def build_report(results: list[dict]) -> dict:
    total = len(results)
    by_status: dict[str, int] = {}
    for r in results:
        by_status[r["status"]] = by_status.get(r["status"], 0) + 1

    measured = [r["structure"] for r in results if r.get("structure") is not None]

    def avg(field):
        vals = [s[field] for s in measured]
        return round(sum(vals) / len(vals), 2) if vals else None

    fields = [
        "classes", "abstract_classes", "association_classes", "enumerations",
        "enumeration_literals", "attributes", "methods", "abstract_methods",
        "generalizations", "associations", "aggregation", "composition",
    ]

    return {
        "generated_at": datetime.datetime.now(datetime.timezone.utc).isoformat(),
        "total_models": total,
        "by_status": by_status,
        "measured_count": len(measured),
        "averages": {field: avg(field) for field in fields},
        "sums": {field: sum(s[field] for s in measured) for field in fields} if measured else {},
        "results": results,
    }


def render_markdown_report(report: dict) -> str:
    lines = [
        "# Model Structure Metadata Report",
        "",
        f"Generated: {report['generated_at']}",
        "",
        f"- **Total models:** {report['total_models']}",
        f"- **Measured:** {report['measured_count']}",
        "",
        "## Averages per model",
        "",
        "| Field | Average |",
        "|---|---|",
    ]
    for field, value in report["averages"].items():
        lines.append(f"| {field} | {value} |")
    lines += [
        "",
        "## Breakdown by status",
        "",
        "| Status | Count |",
        "|---|---|",
    ]
    for status, count in sorted(report["by_status"].items(), key=lambda kv: -kv[1]):
        lines.append(f"| {status} | {count} |")
    lines += ["", "Full per-model detail: see the accompanying `.json` report and each model's `model_metadata.json`."]
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
    parser.add_argument("--report-name", type=str, default="model_metadata_report")
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

    print(f"Computing model structure metadata for {total} models with {args.workers} workers...")
    if skipped:
        print(f"Resuming from cache: {skipped}/{total} already done, {len(model_dirs)} remaining "
              f"(pass --fresh to ignore the cache and recompute everything)")

    results: list[dict] = list(cached_results.values())
    done = skipped
    cache_file = cache_path.open("a")
    try:
        with concurrent.futures.ProcessPoolExecutor(max_workers=args.workers) as executor:
            futures = {executor.submit(process_model, model_dir): model_dir for model_dir in model_dirs}
            for future in concurrent.futures.as_completed(futures):
                model_dir = futures[future]
                try:
                    result = future.result()
                except Exception as exc:
                    result = {
                        "model": model_dir.name, "status": "error", "error_message": str(exc),
                        "buml_source": None, "structure": None,
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
    print(f"Measured: {report['measured_count']}/{report['total_models']}")
    print(f"Report written to {json_path} and {md_path}")


if __name__ == "__main__":
    main()
