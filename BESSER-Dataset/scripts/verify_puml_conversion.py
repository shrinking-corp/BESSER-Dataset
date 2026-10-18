#!/usr/bin/env python3
"""Prove that every `.puml` is a lossless conversion of its original BUML
model. Read-only: never changes the dataset; writes only a report.

Three independent checks per model:

1. **Coverage.** The BUML source is parsed (`ast`, not executed) and every
   constructor call, keyword argument and property assignment in it must be
   one `buml_to_puml.py` converts (SUPPORTED_CALLS, SUPPORTED_ASSIGNMENTS --
   the full inventory of the 9,082-model dataset, 2026-10-18). Anything else
   is reported as `unsupported`, so a construct a future model uses can't be
   dropped silently.
2. **Round trip.** The BUML is loaded with besser and turned into a multiset
   of facts (model and project metadata, classes, attributes, methods with
   parameters, enumerations and literals, generalizations, associations with
   both ends' role, multiplicity, composition, aggregation and navigability,
   OCL constraints). The generated `.puml` is parsed back into the same kind
   of facts. A model passes only if both multisets are equal; otherwise the
   missing and extra facts are listed. Any `.puml` line the parser doesn't
   recognize is itself a mismatch.
3. **Source text.** Every string literal passed to a BUML constructor in the
   original file (names, role names, descriptions, owners, OCL expressions)
   must appear in the PUML -- a check that doesn't go through besser, so a
   field besser dropped on load couldn't hide on both sides of check 2.
   Only statements that reach the model count: the source dataset defines
   some overloaded methods by assigning one variable twice, and the
   overwritten definition never reaches the model. Those are listed
   separately as a source-data defect, computed from the statements (what
   reads which binding), not assumed.

besser adds its 9 built-in primitive types to every model's types; they are
the type vocabulary, not model content, and are not expected in the PUML.

Usage:
    python scripts/verify_puml_conversion.py [--models-file PATH] [--workers N]
        [--dataset-dir PATH] [--reports-dir PATH] [--report-name NAME] [--limit N]
"""
from __future__ import annotations

import argparse
import ast
import concurrent.futures
import datetime
import re
import sys
from collections import Counter
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from _common.buml import (  # noqa: E402
    PUML_MODEL_NAME_PREFIX, binding_name, dead_statements, find_buml_file, load_buml, type_name,
)
from _common.io import add_common_io_args, find_model_dirs  # noqa: E402
from _common.report import render_status_table, write_reports  # noqa: E402

SUPPORTED_CALLS = {
    "Class": {"name", "is_abstract"},
    "Property": {"name", "type", "multiplicity", "is_composite", "is_navigable", "is_aggregation", "visibility"},
    "Multiplicity": {"min_multiplicity", "max_multiplicity"},
    "Method": {"name", "parameters", "type", "visibility"},
    "Parameter": {"name", "type"},
    "Enumeration": {"name", "literals"},
    "EnumerationLiteral": {"name"},
    "Generalization": {"general", "specific"},
    "BinaryAssociation": {"name", "ends"},
    "Constraint": {"name", "context", "expression", "language"},
    "DomainModel": {"name", "types", "associations", "generalizations", "constraints", "metadata"},
    "Metadata": {"description"},
    "Project": {"name", "owner", "metadata", "models"},
}
MAX_POSITIONAL = {"Multiplicity": 2}
SUPPORTED_ASSIGNMENTS = {"attributes", "methods"}
BUILTIN_PRIMITIVES = {"str", "int", "float", "bool", "date", "time", "datetime", "timedelta", "any"}
VISIBILITY = {"public": "+", "private": "-", "protected": "#", "package": "~"}
NOT_NAVIGABLE = "{not navigable}"

CLASS_HEADER = re.compile(r"^(abstract class|class) (\S+) \{$")
ENUM_HEADER = re.compile(r"^enum (\S+) \{$")
METHOD = re.compile(r"^  ([+\-#~]) (\S+)\((.*)\) : (.*)$")
ATTRIBUTE = re.compile(r"^  ([+\-#~]) (\S+) : (.*)$")
LITERAL = re.compile(r"^  (\S+)$")
GENERALIZATION = re.compile(r"^(\S+) <\|-- (\S+)$")
ASSOCIATION = re.compile(r'^(\S+) "([^"]*)" ([*o]?)--([*o]?) "([^"]*)" (\S+)(?: : (.*))?$')
ASSOCIATION_CLASS = re.compile(r"^\((\S+), (\S+)\) \.\. (\S+)$")
NOTE_HEADER = re.compile(r"^note top of (\S+)$")
CONSTRAINT = re.compile(r"^  constraint (\S+) \((.*?)\): (.*)$")
HEADER = {"' model description: ": "model_description", "' project: ": "project",
          "' owner: ": "owner", "' description: ": "description"}
UNESCAPE = re.compile(r"\\(\\|n|r)")


def _unescape(text: str) -> str:
    return UNESCAPE.sub(lambda m: {"\\": "\\", "n": "\n", "r": "\r"}[m.group(1)], text)


def unsupported_constructs(source: str) -> list[str]:
    found = set()
    tree = ast.parse(source)
    for statement in tree.body:
        if not isinstance(statement, (ast.ImportFrom, ast.Import, ast.Assign, ast.AnnAssign)):
            found.add(f"statement {type(statement).__name__}")
        targets = [statement.target] if isinstance(statement, ast.AnnAssign) else getattr(statement, "targets", [])
        for target in targets:
            if isinstance(target, ast.Attribute) and target.attr not in SUPPORTED_ASSIGNMENTS:
                found.add(f"assignment .{target.attr}")
    for node in ast.walk(tree):
        if not isinstance(node, ast.Call):
            continue
        name = node.func.id if isinstance(node.func, ast.Name) else ast.unparse(node.func)
        if name not in SUPPORTED_CALLS:
            found.add(f"call {name}")
            continue
        for keyword in node.keywords:
            if keyword.arg not in SUPPORTED_CALLS[name]:
                found.add(f"{name}({keyword.arg}=)")
        if len(node.args) > MAX_POSITIONAL.get(name, 0):
            found.add(f"{name}(positional)")
    return sorted(found)


def _string_literals(node) -> list[tuple[str, str, str]]:
    found = []
    for call in ast.walk(node):
        if isinstance(call, ast.Call) and isinstance(call.func, ast.Name) and call.func.id in SUPPORTED_CALLS:
            for keyword in call.keywords:
                value = keyword.value
                if isinstance(value, ast.Constant) and isinstance(value.value, str) and value.value:
                    found.append((call.func.id, keyword.arg, value.value))
    return found


def source_literal_check(source: str, puml_text: str) -> tuple[list[str], list[str]]:
    """(missing, dead). Every string literal passed to a BUML constructor in a
    statement that reaches the model (names, role names, descriptions,
    owners, OCL expressions) must appear in the PUML, raw or in its escaped
    one-line form -- tying the PUML to the source text, independently of how
    besser loads it. Literals in dead statements (see dead_statements) are
    returned separately: they are a defect of the source dataset, and the
    model itself doesn't contain them."""
    tree = ast.parse(source)
    dead = dead_statements(tree)
    missing, dead_literals = [], []
    for i, statement in enumerate(tree.body):
        for call, arg, text in _string_literals(statement):
            label = f"{call}({arg}={text[:80]!r})"
            if i in dead:
                dead_literals.append(f"{binding_name(statement)}: {label}")
                continue
            escaped = text.replace("\\", "\\\\").replace("\r", "\\r").replace("\n", "\\n")
            if text not in puml_text and escaped not in puml_text:
                missing.append(label)
    return missing, dead_literals


def _visibility(element) -> str:
    value = getattr(element, "visibility", None)
    return VISIBILITY.get(str(value) if value else "public", "~")


def _end_fact(end) -> tuple:
    multiplicity = getattr(end, "multiplicity", None)
    return (type_name(end.type), str(getattr(end, "name", "") or ""),
            str(getattr(multiplicity, "min", "")) if multiplicity else "",
            str(getattr(multiplicity, "max", "")) if multiplicity else "",
            bool(getattr(end, "is_composite", False)), bool(getattr(end, "is_aggregation", False)),
            bool(getattr(end, "is_navigable", True)))


def model_facts(model, project) -> Counter:
    """besser adds its 9 built-in primitive types to every DomainModel's types
    by itself (no BUML file defines them), so those are the type vocabulary,
    not model content; any other primitive type would be reported."""
    from besser.BUML.metamodel.structural import (
        AssociationClass, BinaryAssociation, Class, Enumeration, PrimitiveDataType,
    )

    facts = Counter([("model", str(model.name))])
    model_metadata = getattr(model, "metadata", None)
    if model_metadata is not None and getattr(model_metadata, "description", None):
        facts[("model_description", str(model_metadata.description))] += 1
    if project is not None:
        facts[("project", str(project.name))] += 1
        if getattr(project, "owner", None):
            facts[("owner", str(project.owner))] += 1
        project_metadata = getattr(project, "metadata", None)
        if project_metadata is not None and getattr(project_metadata, "description", None):
            facts[("description", str(project_metadata.description))] += 1
    for t in model.types:
        if isinstance(t, Class):
            facts[("class", t.name, bool(t.is_abstract))] += 1
            for a in t.attributes:
                facts[("attribute", t.name, a.name, _visibility(a), type_name(getattr(a, "type", "")))] += 1
            for m in t.methods:
                params = tuple(sorted(f"{p.name} : {type_name(getattr(p, 'type', ''))}"
                                      for p in getattr(m, "parameters", [])))
                ret = type_name(m.type) if getattr(m, "type", None) else "void"
                facts[("method", t.name, m.name, _visibility(m), params, ret)] += 1
            if isinstance(t, AssociationClass) and getattr(t, "association", None) is not None:
                ends = sorted(type_name(e.type) for e in t.association.ends)
                facts[("association_class", t.name, tuple(ends))] += 1
        elif isinstance(t, Enumeration):
            facts[("enum", t.name)] += 1
            for literal in t.literals:
                facts[("literal", t.name, literal.name)] += 1
        elif isinstance(t, PrimitiveDataType) and t.name in BUILTIN_PRIMITIVES:
            continue
        else:
            facts[("unsupported_type", type(t).__name__, type_name(t))] += 1
    for g in model.generalizations:
        facts[("generalization", g.general.name, g.specific.name)] += 1
    for assoc in model.associations:
        if isinstance(assoc, BinaryAssociation):
            facts[("association", str(assoc.name or ""), tuple(sorted(_end_fact(e) for e in assoc.ends)))] += 1
        else:
            facts[("unsupported_association", type(assoc).__name__, str(assoc.name))] += 1
    for c in getattr(model, "constraints", None) or []:
        facts[("constraint", type_name(c.context), c.name, str(c.language), str(c.expression))] += 1
    return facts


def _parse_end_label(label: str, type_: str, decoration: str) -> tuple:
    navigable = True
    if label.endswith(NOT_NAVIGABLE):
        navigable = False
        label = label[: -len(NOT_NAVIGABLE)].rstrip()
    tokens = label.split(" ") if label else []
    bounds = tokens[-1] if tokens and ".." in tokens[-1] else ""
    role = " ".join(tokens[:-1] if bounds else tokens)
    low, high = bounds.split("..", 1) if bounds else ("", "")
    return (type_, role, low, high, decoration == "*", decoration == "o", navigable)


def puml_facts(text: str) -> Counter:
    facts: Counter = Counter()
    current_class = current_enum = note_context = None
    for line in text.replace("\r\n", "\n").split("\n"):
        if line in ("@startuml", "@enduml", ""):
            continue
        if line.startswith(PUML_MODEL_NAME_PREFIX):
            facts[("model", _unescape(line[len(PUML_MODEL_NAME_PREFIX):]))] += 1
            continue
        header = next((key for prefix, key in HEADER.items() if line.startswith(prefix)), None)
        if header:
            prefix = next(p for p, k in HEADER.items() if k == header)
            facts[(header, _unescape(line[len(prefix):]))] += 1
            continue
        if note_context is not None:
            if line == "end note":
                note_context = None
            elif m := CONSTRAINT.match(line):
                facts[("constraint", note_context, m.group(1), m.group(2), _unescape(m.group(3)))] += 1
            else:
                facts[("unparsed_line", line)] += 1
            continue
        if line == "}":
            current_class = current_enum = None
            continue
        if current_class is not None:
            if m := METHOD.match(line):
                params = tuple(p for p in m.group(3).split(", ") if p)
                facts[("method", current_class, m.group(2), m.group(1), params, m.group(4))] += 1
            elif m := ATTRIBUTE.match(line):
                facts[("attribute", current_class, m.group(2), m.group(1), m.group(3))] += 1
            else:
                facts[("unparsed_line", line)] += 1
            continue
        if current_enum is not None:
            if m := LITERAL.match(line):
                facts[("literal", current_enum, m.group(1))] += 1
            else:
                facts[("unparsed_line", line)] += 1
            continue
        if m := CLASS_HEADER.match(line):
            current_class = m.group(2)
            facts[("class", current_class, m.group(1) == "abstract class")] += 1
        elif m := ENUM_HEADER.match(line):
            current_enum = m.group(1)
            facts[("enum", current_enum)] += 1
        elif m := GENERALIZATION.match(line):
            facts[("generalization", m.group(1), m.group(2))] += 1
        elif m := ASSOCIATION.match(line):
            type1, label1, left, right, label2, type2, name = m.groups()
            end1 = _parse_end_label(label1, type1, right)  # end1's composition is drawn on the right
            end2 = _parse_end_label(label2, type2, left)
            facts[("association", name or "", tuple(sorted([end1, end2])))] += 1
        elif m := ASSOCIATION_CLASS.match(line):
            facts[("association_class", m.group(3), tuple(sorted([m.group(1), m.group(2)])))] += 1
        elif m := NOTE_HEADER.match(line):
            note_context = m.group(1)
        else:
            facts[("unparsed_line", line)] += 1
    return facts


def verify_model(model_dir: Path) -> dict:
    result = {"model": model_dir.name, "status": "error", "unsupported": [], "missing": [], "extra": [],
              "missing_count": 0, "extra_count": 0, "source_literals_missing": [],
              "source_dead_definitions": [], "source_dead_definition_count": 0, "error_message": None}
    buml = find_buml_file(model_dir)
    pumls = sorted(model_dir.glob("*.puml"))
    if buml is None:
        result["status"] = "no_buml"
        return result
    if not pumls:
        result["status"] = "no_puml"
        return result
    try:
        source = buml.read_text(encoding="utf-8")
        puml_text = pumls[0].read_text(encoding="utf-8")
        result["unsupported"] = unsupported_constructs(source)
        literals_missing, dead_literals = source_literal_check(source, puml_text)
        result["source_literals_missing"] = literals_missing[:20]
        result["source_dead_definitions"] = dead_literals[:20]
        result["source_dead_definition_count"] = len(dead_literals)
        model, project = load_buml(buml)
        expected = model_facts(model, project)
        actual = puml_facts(puml_text)
    except Exception as exc:  # noqa: BLE001 -- recorded per model, the run goes on
        result["error_message"] = f"{type(exc).__name__}: {exc}"
        return result
    missing, extra = expected - actual, actual - expected
    result["missing_count"], result["extra_count"] = sum(missing.values()), sum(extra.values())
    result["missing"] = [repr(f) for f in list(missing.elements())[:20]]
    result["extra"] = [repr(f) for f in list(extra.elements())[:20]]
    if result["unsupported"]:
        result["status"] = "unsupported"
    elif missing or extra or result["source_literals_missing"]:
        result["status"] = "mismatch"
    else:
        result["status"] = "lossless"
    return result


def build_report(results: list[dict]) -> dict:
    by_status = Counter(r["status"] for r in results)
    fact_kinds = Counter()
    for r in results:
        for f in r["missing"]:
            fact_kinds["missing " + f.split(",")[0].strip("(' ")] += 1
        for f in r["extra"]:
            fact_kinds["extra " + f.split(",")[0].strip("(' ")] += 1
        for f in r["source_literals_missing"]:
            fact_kinds["source literal missing " + f.split("=")[0]] += 1
    return {
        "generated_at": datetime.datetime.now(datetime.timezone.utc).isoformat(),
        "total_models": len(results),
        "lossless_count": by_status.get("lossless", 0),
        "by_status": dict(by_status),
        "unsupported_constructs": sorted({c for r in results for c in r["unsupported"]}),
        "differing_fact_kinds": dict(fact_kinds.most_common()),
        "source_dead_definitions": {
            "models": sum(1 for r in results if r["source_dead_definition_count"]),
            "literals": sum(r["source_dead_definition_count"] for r in results),
            "per_model": {r["model"]: r["source_dead_definitions"]
                          for r in sorted(results, key=lambda r: r["model"]) if r["source_dead_definitions"]},
        },
        "not_lossless": sorted((r for r in results if r["status"] != "lossless"), key=lambda r: r["model"]),
    }


def render_markdown_report(report: dict) -> str:
    lines = [
        "# PUML conversion: losslessness check",
        "",
        f"Generated: {report['generated_at']}",
        "",
        f"- **Models checked:** {report['total_models']}",
        f"- **Lossless (every BUML fact in the PUML, nothing extra):** {report['lossless_count']}",
        f"- **Unsupported BUML constructs found:** {', '.join(report['unsupported_constructs']) or 'none'}",
        "",
    ]
    lines += render_status_table(report["by_status"])
    dead = report["source_dead_definitions"]
    lines += [
        "",
        "## Source definitions that never reach the model (defect of the source dataset)",
        "",
        f"{dead['literals']} string literals in {dead['models']} models sit in BUML statements whose value is "
        "never read before being overwritten, or never read at all (overloaded methods assigned to the same "
        "variable twice). The model loaded from the BUML doesn't contain them, so the PUML can't either; "
        "they are not counted as conversion losses.",
        "",
    ]
    for model, examples in list(dead["per_model"].items())[:15]:
        lines.append(f"- **{model}:** {'; '.join(examples[:3])}")
    if report["differing_fact_kinds"]:
        lines += ["", "## Kinds of differing facts (first 20 per model)", "", "| Kind | Count |", "|---|---:|"]
        lines += [f"| {kind} | {count} |" for kind, count in report["differing_fact_kinds"].items()]
    if report["not_lossless"]:
        lines += ["", "## First models that are not lossless", ""]
        for r in report["not_lossless"][:25]:
            detail = r["error_message"] or "; ".join(
                r["unsupported"] + r["missing"][:3] + r["extra"][:3] + r["source_literals_missing"][:3])
            lines.append(f"- **{r['model']}** ({r['status']}): {detail[:300]}")
    lines += ["", "Full per-model detail: see the accompanying `.json` report."]
    return "\n".join(lines) + "\n"


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    add_common_io_args(parser, __file__)
    parser.add_argument("--models-file", type=Path, help="Default: every model directory in the dataset")
    parser.add_argument("--workers", type=int, default=4)
    parser.add_argument("--limit", type=int)
    parser.add_argument("--report-name", default="puml_conversion_report")
    args = parser.parse_args()

    model_dirs = find_model_dirs(args.dataset_dir, args.models_file, args.limit)
    print(f"Verifying {len(model_dirs)} models with {args.workers} workers...")
    with concurrent.futures.ProcessPoolExecutor(max_workers=args.workers) as executor:
        results = list(executor.map(verify_model, model_dirs, chunksize=20))

    report = build_report(results)
    json_path, md_path = write_reports(args.reports_dir, args.report_name, report, render_markdown_report(report))
    print(f"Lossless: {report['lossless_count']}/{report['total_models']}  {report['by_status']}")
    if report["unsupported_constructs"]:
        print(f"Unsupported BUML constructs: {report['unsupported_constructs']}")
    dead = report["source_dead_definitions"]
    print(f"Source definitions that never reach the model (dataset defect, not a loss): "
          f"{dead['literals']} literals in {dead['models']} models")
    for kind, count in list(report["differing_fact_kinds"].items())[:10]:
        print(f"  {kind}: {count}")
    print(f"Report written to {json_path} and {md_path}")


if __name__ == "__main__":
    main()
