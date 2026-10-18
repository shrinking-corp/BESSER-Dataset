#!/usr/bin/env python3
"""Self-test of the two checks the benchmark dataset relies on: the duplicate
detector (`_common.buml.buml_fingerprint`, used by `select_unique_models.py`)
and the PUML losslessness verifier (`verify_puml_conversion.py`). A check
that can't fail proves nothing (cf. the 2026-10-18 mutation-score false
positive), so this tries to fool both. Read-only on the dataset: mutated
copies live in a temporary folder only.

1. **Fingerprint vs. real changes and vs. noise** (seeded sample of real
   models, plus every model in the dataset that uses a construct too rare
   for the sample to hit: OCL constraints, explicit navigability). Each BUML *mutation* changes something the model contains (a
   name, type, multiplicity, flag, element, constraint, metadata) and must
   change the fingerprint. Each *noise* operation changes only what carries
   no meaning (set order, the model's random name, the order of independent
   statements, formatting) and must not. Every mutated file is also loaded
   with besser: a mutation must change the loaded model, noise must not --
   otherwise the test case itself is wrong and is reported as such. A
   mutation that changes the fingerprint but not the besser facts exposes a
   blind spot of the verifier's fact extraction.
2. **Verifier vs. corrupted PUML** (same sample). The unmodified PUML must be
   lossless; each corruption (deleted or altered line, flipped flag, bogus
   class) must be reported.
3. **Independent grouping** (every model in --models-file). Models are
   grouped a second time by the facts of the model besser builds -- separate
   code from the AST fingerprint -- and both groupings must be identical.

Usage:
    python scripts/selftest_conversion_checks.py [--models-file reports/usable_models.txt]
        [--sample-size 300] [--seed 42] [--workers N] [--dataset-dir PATH] [--reports-dir PATH]
"""
from __future__ import annotations

import argparse
import ast
import concurrent.futures
import datetime
import hashlib
import random
import re
import sys
import tempfile
from collections import Counter
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from _common.buml import binding_name, buml_fingerprint, dead_statements, find_buml_file, load_buml  # noqa: E402
from _common.io import add_common_io_args, read_model_names  # noqa: E402
from _common.report import write_reports  # noqa: E402
from verify_puml_conversion import model_facts, puml_facts, source_literal_check  # noqa: E402

RARE_CONSTRUCT_MARKERS = ("Constraint(", "is_navigable=")
PRIMITIVE_TYPES = ["StringType", "IntegerType", "FloatType", "BooleanType", "DateType",
                   "TimeType", "DateTimeType", "TimeDeltaType", "AnyType"]


# --- BUML mutations: each must change the model ------------------------------------------------

def _live_calls(tree: ast.Module, func: str) -> list[ast.Call]:
    dead = dead_statements(tree)
    return [node for i, statement in enumerate(tree.body) if i not in dead
            for node in ast.walk(statement)
            if isinstance(node, ast.Call) and isinstance(node.func, ast.Name) and node.func.id == func]


def _keyword(call: ast.Call, arg: str):
    return next((k for k in call.keywords if k.arg == arg), None)


def _rename(func: str, arg: str):
    def mutate(tree, rng):
        calls = [c for c in _live_calls(tree, func)
                 if (k := _keyword(c, arg)) is not None and isinstance(k.value, ast.Constant)
                 and isinstance(k.value.value, str) and k.value.value]
        if not calls:
            return False
        k = _keyword(rng.choice(calls), arg)
        k.value = ast.Constant(k.value.value + "_mut")
        return True
    return mutate


def _change_multiplicity(tree, rng):
    calls = [c for c in _live_calls(tree, "Multiplicity")
             if len(c.args) == 2 and isinstance(c.args[1], ast.Constant) and isinstance(c.args[1].value, int)]
    if not calls:
        return False
    call = rng.choice(calls)
    call.args[1] = ast.Constant(1 if call.args[1].value == 9999 else call.args[1].value + 1)
    return True


def _flip_flag(func: str, arg: str, default: bool, only_association_ends: bool = False):
    """Flips the flag; where it is absent (= `default`), adds the opposite
    value -- adding the default itself would change nothing."""
    def mutate(tree, rng):
        calls = _live_calls(tree, func)
        if only_association_ends:
            calls = [c for c in calls if _keyword(c, "multiplicity") is not None]
        if not calls:
            return False
        call = rng.choice(calls)
        k = _keyword(call, arg)
        if k is None:
            call.keywords.append(ast.keyword(arg=arg, value=ast.Constant(not default)))
        else:
            current = k.value.value if isinstance(k.value, ast.Constant) else default
            k.value = ast.Constant(not current)
        return True
    return mutate


def _change_attribute_type(tree, rng):
    calls = [c for c in _live_calls(tree, "Property")
             if (k := _keyword(c, "type")) is not None and isinstance(k.value, ast.Name) and k.value.id in PRIMITIVE_TYPES]
    if not calls:
        return False
    k = _keyword(rng.choice(calls), "type")
    k.value = ast.Name(id=rng.choice([t for t in PRIMITIVE_TYPES if t != k.value.id]), ctx=ast.Load())
    return True


def _remove_from_attributes(tree, rng):
    dead = dead_statements(tree)
    sets = [s.value for i, s in enumerate(tree.body) if i not in dead and isinstance(s, ast.Assign)
            and any(isinstance(t, ast.Attribute) and t.attr == "attributes" for t in s.targets)
            and isinstance(s.value, ast.Set) and s.value.elts]
    if not sets:
        return False
    target = rng.choice(sets)
    target.elts.pop(rng.randrange(len(target.elts)))
    if not target.elts:
        # `{}` would be a dict; an empty set has to be spelled set()
        for s in tree.body:
            if isinstance(s, ast.Assign) and s.value is target:
                s.value = ast.Call(func=ast.Name(id="set", ctx=ast.Load()), args=[], keywords=[])
    return True


def _remove_from_domain_model(arg: str):
    def mutate(tree, rng):
        sets = [k.value for c in _live_calls(tree, "DomainModel")
                if (k := _keyword(c, arg)) is not None and isinstance(k.value, ast.Set) and len(k.value.elts) > 1]
        if not sets:
            return False
        target = rng.choice(sets)
        target.elts.pop(rng.randrange(len(target.elts)))
        return True
    return mutate


BUML_MUTATIONS = {
    "rename class": _rename("Class", "name"),
    "rename attribute/role": _rename("Property", "name"),
    "rename method": _rename("Method", "name"),
    "rename parameter": _rename("Parameter", "name"),
    "rename enum literal": _rename("EnumerationLiteral", "name"),
    "rename enumeration": _rename("Enumeration", "name"),
    "rename association": _rename("BinaryAssociation", "name"),
    "edit OCL expression": _rename("Constraint", "expression"),
    "edit project owner": _rename("Project", "owner"),
    "edit project name": _rename("Project", "name"),
    "edit description": _rename("Metadata", "description"),
    "change multiplicity": _change_multiplicity,
    "flip abstract": _flip_flag("Class", "is_abstract", default=False),
    "flip composite": _flip_flag("Property", "is_composite", default=False, only_association_ends=True),
    "flip navigable": _flip_flag("Property", "is_navigable", default=True, only_association_ends=True),
    "change attribute type": _change_attribute_type,
    "remove attribute": _remove_from_attributes,
    "remove association": _remove_from_domain_model("associations"),
    "remove generalization": _remove_from_domain_model("generalizations"),
    "remove type": _remove_from_domain_model("types"),
}


# --- BUML noise: each must leave the model unchanged -------------------------------------------

def _shuffle_sets(tree, rng):
    sets = [n for n in ast.walk(tree) if isinstance(n, ast.Set) and len(n.elts) > 1]
    for node in sets:
        rng.shuffle(node.elts)
    return bool(sets)


def _rename_model(tree, rng):
    calls = [c for c in ast.walk(tree) if isinstance(c, ast.Call) and isinstance(c.func, ast.Name)
             and c.func.id == "DomainModel" and _keyword(c, "name") is not None]
    for call in calls:
        _keyword(call, "name").value = ast.Constant(f"_{rng.getrandbits(64):016x}")
    return bool(calls)


def _reads(statement) -> set[str]:
    return {n.id for n in ast.walk(statement) if isinstance(n, ast.Name) and isinstance(n.ctx, ast.Load)}


def _property_targets(statement) -> set[str]:
    targets = getattr(statement, "targets", [])
    return {ast.unparse(t) for t in targets if isinstance(t, ast.Attribute)}


def _swap_independent_statements(tree, rng):
    """Random swaps of adjacent statements that can't affect each other: neither
    reads or rebinds what the other binds, and they don't assign the same
    property -- so which binding every read sees is unchanged."""
    body = tree.body
    swapped = 0
    for _ in range(len(body) * 4):
        i = rng.randrange(len(body) - 1) if len(body) > 1 else 0
        a, b = body[i], body[i + 1] if i + 1 < len(body) else None
        if b is None or isinstance(a, (ast.Import, ast.ImportFrom)) or isinstance(b, (ast.Import, ast.ImportFrom)):
            continue
        bound_a, bound_b = binding_name(a), binding_name(b)
        if bound_a is not None and (bound_a in _reads(b) or bound_a == bound_b):
            continue
        if bound_b is not None and bound_b in _reads(a):
            continue
        if _property_targets(a) & _property_targets(b):
            continue
        if (_property_targets(a) and bound_b and bound_b in _reads(a)) or (_property_targets(b) and bound_a and bound_a in _reads(b)):
            continue
        body[i], body[i + 1] = b, a
        swapped += 1
    return swapped > 0


def _reformat(tree, rng):
    return True  # writing the tree back with ast.unparse already drops comments and reformats


BUML_NOISE = {
    "shuffle set items": _shuffle_sets,
    "change model's random name": _rename_model,
    "reorder independent statements": _swap_independent_statements,
    "reformat / drop comments": _reformat,
}


# --- PUML corruptions: each must be reported by the verifier -----------------------------------

ASSOC_LINE = re.compile(r'^\S+ "[^"]*" [*o]?--[*o]? "[^"]*" \S+')
ATTRIBUTE_LINE = re.compile(r"^  [+\-#~] \S+ : ")
METHOD_LINE = re.compile(r"^  [+\-#~] \S+\(")


def _lines_matching(lines, predicate):
    return [i for i, line in enumerate(lines) if predicate(line)]


def _puml_delete(predicate):
    def corrupt(lines, rng):
        idx = _lines_matching(lines, predicate)
        if not idx:
            return None
        out = list(lines)
        del out[rng.choice(idx)]
        return out
    return corrupt


def _puml_edit(predicate, edit):
    def corrupt(lines, rng):
        idx = _lines_matching(lines, predicate)
        if not idx:
            return None
        out = list(lines)
        i = rng.choice(idx)
        changed = edit(out[i])
        if changed == out[i]:
            return None
        out[i] = changed
        return out
    return corrupt


def _edit_role(line):
    return re.sub(r'"(\S+) ', lambda m: f'"{m.group(1)}_mut ', line, count=1)


def _edit_multiplicity(line):
    return re.sub(r"(\d+)\.\.(\d+)", lambda m: f"{m.group(1)}..{int(m.group(2)) + 1}", line, count=1)


def _flip_composition(line):
    if "*--" in line and "--*" not in line:
        return line.replace("*--", "--*", 1)
    if "--*" in line:
        return line.replace("--*", "--", 1)
    return line.replace(" -- ", " *-- ", 1)


PUML_CORRUPTIONS = {
    "delete association": _puml_delete(lambda l: bool(ASSOC_LINE.match(l))),
    "delete attribute": _puml_delete(lambda l: bool(ATTRIBUTE_LINE.match(l)) and "(" not in l),
    "delete method": _puml_delete(lambda l: bool(METHOD_LINE.match(l))),
    "delete enum literal": _puml_delete(lambda l: bool(re.match(r"^  \S+$", l))),
    "delete generalization": _puml_delete(lambda l: "<|--" in l),
    "delete constraint": _puml_delete(lambda l: l.startswith("  constraint ")),
    "delete project header": _puml_delete(lambda l: l.startswith("' project: ")),
    "change role name": _puml_edit(lambda l: bool(ASSOC_LINE.match(l)), _edit_role),
    "change multiplicity": _puml_edit(lambda l: bool(ASSOC_LINE.match(l)), _edit_multiplicity),
    "change attribute type": _puml_edit(lambda l: bool(ATTRIBUTE_LINE.match(l)) and "(" not in l,
                                        lambda l: l + "_mut"),
    "change parameter": _puml_edit(lambda l: bool(METHOD_LINE.match(l)) and "()" not in l,
                                   lambda l: l.replace("(", "(x", 1)),
    "flip abstract": _puml_edit(lambda l: l.startswith(("class ", "abstract class ")),
                                lambda l: l[len("abstract "):] if l.startswith("abstract ") else "abstract " + l),
    "flip composition": _puml_edit(lambda l: bool(ASSOC_LINE.match(l)), _flip_composition),
    "drop {not navigable}": _puml_edit(lambda l: "{not navigable}" in l, lambda l: l.replace(" {not navigable}", "", 1)),
    "change model name": _puml_edit(lambda l: l.startswith("' model: "), lambda l: l + "_mut"),
    "add bogus class": lambda lines, rng: lines[:-1] + ["class Bogus_mut {", "}"] + lines[-1:],
}


# --- per-model worker -----------------------------------------------------------------------

def _facts_key(facts: Counter) -> str:
    """Hash of a model's facts without its own (random) name."""
    items = sorted((repr(k), v) for k, v in facts.items() if k[0] != "model")
    return hashlib.sha256(repr(items).encode("utf-8")).hexdigest()


def group_keys(model_dir: Path) -> dict:
    buml = find_buml_file(model_dir)
    try:
        fingerprint, _ = buml_fingerprint(buml)
        model, project = load_buml(buml)
        return {"model": model_dir.name, "fingerprint": fingerprint, "facts": _facts_key(model_facts(model, project))}
    except Exception as exc:  # noqa: BLE001
        return {"model": model_dir.name, "error": f"{type(exc).__name__}: {exc}"}


def _fingerprint_and_facts(tree: ast.Module, workdir: Path, label: str) -> tuple[str, str]:
    path = workdir / f"{label}.py"
    path.write_text(ast.unparse(tree), encoding="utf-8")
    fingerprint, _ = buml_fingerprint(path)
    model, project = load_buml(path)
    return fingerprint, _facts_key(model_facts(model, project))


def selftest_model(task: tuple[Path, int]) -> dict:
    model_dir, seed = task
    rng = random.Random(f"{seed}:{model_dir.name}")
    buml = find_buml_file(model_dir)
    source = buml.read_text(encoding="utf-8")
    out = {"model": model_dir.name, "buml": [], "puml": [], "error": None}
    try:
        base_fp, _ = buml_fingerprint(buml)
        model, project = load_buml(buml)
        base_facts = _facts_key(model_facts(model, project))
        with tempfile.TemporaryDirectory() as tmp:
            workdir = Path(tmp)
            for kind, operations, expect_change in (("mutation", BUML_MUTATIONS, True), ("noise", BUML_NOISE, False)):
                for name, operation in operations.items():
                    tree = ast.parse(source)
                    if not operation(tree, rng):
                        continue
                    ast.fix_missing_locations(tree)
                    try:
                        fp, facts = _fingerprint_and_facts(tree, workdir, re.sub(r"\W", "_", name))
                    except Exception as exc:  # noqa: BLE001 -- a mutation can make the model invalid
                        out["buml"].append({"kind": kind, "name": name, "outcome": "invalid_model",
                                            "detail": f"{type(exc).__name__}: {exc}"[:200]})
                        continue
                    fp_changed, facts_changed = fp != base_fp, facts != base_facts
                    if facts_changed != expect_change:
                        outcome = "bad_test_case"   # the operation didn't do what it claims
                    elif fp_changed == expect_change:
                        outcome = "ok"
                    else:
                        outcome = "FINGERPRINT_FOOLED"
                    out["buml"].append({"kind": kind, "name": name, "outcome": outcome})

        puml_path = sorted(model_dir.glob("*.puml"))[0]
        puml_text = puml_path.read_text(encoding="utf-8")
        expected = model_facts(model, project)

        def reported(text: str) -> bool:
            actual = puml_facts(text)
            missing_literals, _ = source_literal_check(source, text)
            return bool(expected - actual or actual - expected or missing_literals)

        out["puml"].append({"name": "unmodified PUML", "outcome": "VERIFIER_FALSE_ALARM" if reported(puml_text) else "ok"})
        lines = puml_text.split("\n")
        for name, corrupt in PUML_CORRUPTIONS.items():
            corrupted = corrupt(lines, rng)
            if corrupted is None:
                continue
            out["puml"].append({"name": name, "outcome": "ok" if reported("\n".join(corrupted)) else "VERIFIER_FOOLED"})
    except Exception as exc:  # noqa: BLE001
        out["error"] = f"{type(exc).__name__}: {exc}"
    return out


def tally(entries: list[dict], key: str = "name") -> dict:
    table: dict[str, Counter] = {}
    for e in entries:
        table.setdefault(e[key], Counter())[e["outcome"]] += 1
    return {name: dict(counts) for name, counts in sorted(table.items())}


def compare_groupings(keys: list[dict]) -> dict:
    by_fp: dict[str, set[str]] = {}
    by_facts: dict[str, set[str]] = {}
    for k in keys:
        if "error" in k:
            continue
        by_fp.setdefault(k["fingerprint"], set()).add(k["model"])
        by_facts.setdefault(k["facts"], set()).add(k["model"])
    facts_of = {k["model"]: k["facts"] for k in keys if "error" not in k}
    fp_of = {k["model"]: k["fingerprint"] for k in keys if "error" not in k}
    over = [sorted(g) for g in by_fp.values() if len({facts_of[m] for m in g}) > 1]
    under = [sorted(g) for g in by_facts.values() if len({fp_of[m] for m in g}) > 1]
    return {
        "models": len(fp_of),
        "errors": [k for k in keys if "error" in k],
        "groups_by_fingerprint": len(by_fp),
        "groups_by_besser_model": len(by_facts),
        "fingerprint_merged_different_models": over[:20],
        "fingerprint_split_identical_models": under[:20],
        "identical": not over and not under,
    }


def render_markdown_report(report: dict) -> str:
    lines = [
        "# Self-test of the duplicate detector and the PUML verifier",
        "",
        f"Generated: {report['generated_at']} · sample {report['sample_size']} models, seed {report['seed']}",
        "",
        f"**Verdict: {'PASS' if report['passed'] else 'FAIL'}** "
        f"(fingerprint fooled {report['fingerprint_fooled']}×, verifier fooled {report['verifier_fooled']}×, "
        f"verifier false alarms {report['verifier_false_alarms']}, bad test cases {report['bad_test_cases']}, "
        f"groupings identical: {report['grouping']['identical']})",
        "",
        f"Never exercised: {', '.join(report['untested_operations']) or 'none'}. "
        f"Models added for rare constructs: {len(report['rare_construct_models'])}.",
        "",
        "## 1. Fingerprint: real changes must change it, noise must not",
        "",
        "`ok` = behaved correctly · `FINGERPRINT_FOOLED` = failed · `bad_test_case` = besser says the operation "
        "didn't do what it claims (not counted either way) · `invalid_model` = the mutated file no longer loads.",
        "",
        "| Operation | Outcomes |",
        "|---|---|",
    ]
    for name, counts in report["buml_tally"].items():
        lines.append(f"| {name} | {', '.join(f'{k}: {v}' for k, v in sorted(counts.items()))} |")
    lines += ["", "## 2. Verifier: corrupted PUML must be reported, the real PUML must pass", "",
              "| Corruption | Outcomes |", "|---|---|"]
    for name, counts in report["puml_tally"].items():
        lines.append(f"| {name} | {', '.join(f'{k}: {v}' for k, v in sorted(counts.items()))} |")
    g = report["grouping"]
    lines += [
        "",
        "## 3. Independent grouping (besser-built model vs. AST fingerprint)",
        "",
        f"- Models: {g['models']} (errors: {len(g['errors'])})",
        f"- Groups by fingerprint: {g['groups_by_fingerprint']} · by besser-built model: {g['groups_by_besser_model']}",
        f"- Fingerprint merged models besser builds differently: {len(g['fingerprint_merged_different_models'])}",
        f"- Fingerprint split models besser builds identically: {len(g['fingerprint_split_identical_models'])}",
        "",
        "Full detail: see the accompanying `.json`.",
    ]
    return "\n".join(lines) + "\n"


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    add_common_io_args(parser, __file__)
    parser.add_argument("--models-file", type=Path, default=None, help="Default: reports/usable_models.txt")
    parser.add_argument("--sample-size", type=int, default=300)
    parser.add_argument("--seed", type=int, default=42)
    parser.add_argument("--workers", type=int, default=4)
    parser.add_argument("--report-name", default="conversion_checks_selftest")
    args = parser.parse_args()

    names = read_model_names(args.models_file or args.reports_dir / "usable_models.txt")
    model_dirs = [args.dataset_dir / n for n in names]
    sample = random.Random(args.seed).sample(model_dirs, min(args.sample_size, len(model_dirs)))
    # Constructs too rare for a random sample to hit are tested on every model that has them.
    rare = sorted(d for d in args.dataset_dir.iterdir() if d.is_dir() and d not in set(sample)
                  and (buml := find_buml_file(d)) is not None
                  and any(marker in buml.read_text(encoding="utf-8") for marker in RARE_CONSTRUCT_MARKERS))
    sample += rare
    print(f"Sample: {len(sample) - len(rare)} random + {len(rare)} models with rare constructs "
          f"({', '.join(RARE_CONSTRUCT_MARKERS)})")

    with concurrent.futures.ProcessPoolExecutor(max_workers=args.workers) as executor:
        print(f"1+2: mutation/noise/corruption tests on {len(sample)} sampled models...")
        results = list(executor.map(selftest_model, [(d, args.seed) for d in sample], chunksize=4))
        print(f"3: grouping all {len(model_dirs)} models a second time by the besser-built model...")
        keys = list(executor.map(group_keys, model_dirs, chunksize=20))

    buml_entries = [e for r in results for e in r["buml"]]
    puml_entries = [e for r in results for e in r["puml"]]
    grouping = compare_groupings(keys)
    report = {
        "generated_at": datetime.datetime.now(datetime.timezone.utc).isoformat(),
        "sample_size": len(sample),
        "rare_construct_models": [d.name for d in rare],
        "seed": args.seed,
        "fingerprint_fooled": sum(e["outcome"] == "FINGERPRINT_FOOLED" for e in buml_entries),
        "verifier_fooled": sum(e["outcome"] == "VERIFIER_FOOLED" for e in puml_entries),
        "verifier_false_alarms": sum(e["outcome"] == "VERIFIER_FALSE_ALARM" for e in puml_entries),
        "bad_test_cases": sum(e["outcome"] == "bad_test_case" for e in buml_entries),
        "buml_tally": tally(buml_entries),
        "puml_tally": tally(puml_entries),
        "grouping": grouping,
        "model_errors": [{"model": r["model"], "error": r["error"]} for r in results if r["error"]],
        "failures": [{"model": r["model"], **e} for r in results for e in r["buml"] + r["puml"]
                     if e["outcome"] in ("FINGERPRINT_FOOLED", "VERIFIER_FOOLED", "VERIFIER_FALSE_ALARM")],
    }
    all_operations = {**{n: "BUML" for n in list(BUML_MUTATIONS) + list(BUML_NOISE)},
                      **{n: "PUML" for n in list(PUML_CORRUPTIONS) + ["unmodified PUML"]}}
    tallies = {"BUML": report["buml_tally"], "PUML": report["puml_tally"]}
    report["untested_operations"] = sorted(f"{side} {name}" for name, side in all_operations.items()
                                           if not tallies[side].get(name, {}).get("ok"))
    report["passed"] = (report["fingerprint_fooled"] == 0 and report["verifier_fooled"] == 0
                        and report["verifier_false_alarms"] == 0 and report["bad_test_cases"] == 0
                        and not report["untested_operations"] and grouping["identical"]
                        and not report["model_errors"] and not grouping["errors"])
    json_path, md_path = write_reports(args.reports_dir, args.report_name, report, render_markdown_report(report))

    print(f"\nVerdict: {'PASS' if report['passed'] else 'FAIL'}")
    if report["untested_operations"]:
        print(f"  never exercised (no model in the sample allowed it): {report['untested_operations']}")
    if report["model_errors"]:
        print(f"  model errors: {report['model_errors'][:3]}")
    print(f"  fingerprint fooled: {report['fingerprint_fooled']}, verifier fooled: {report['verifier_fooled']}, "
          f"verifier false alarms: {report['verifier_false_alarms']}, bad test cases: {report['bad_test_cases']}")
    print(f"  groupings identical: {grouping['identical']} ({grouping['groups_by_fingerprint']} by fingerprint, "
          f"{grouping['groups_by_besser_model']} by besser-built model, {len(grouping['errors'])} errors)")
    for name, counts in report["buml_tally"].items():
        print(f"  BUML {name:32} {counts}")
    for name, counts in report["puml_tally"].items():
        print(f"  PUML {name:32} {counts}")
    print(f"Report written to {json_path} and {md_path}")


if __name__ == "__main__":
    main()
