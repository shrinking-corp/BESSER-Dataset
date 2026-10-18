#!/usr/bin/env python3
"""Keep one model per distinct model in the original BUML sources.
Read-only on the dataset.

Found 2026-10-18 while building the benchmark split: the 8,336 usable models
contain thousands of copies of the same model. The copies' BUML files are not
byte-identical, but they differ in exactly three ways that carry no meaning:
  - the order of items inside set literals (`X.attributes={...}`), because
    Python prints sets in arbitrary order;
  - the order of statements and comments;
  - the DomainModel's own `name=`, a random UUID or Eclipse ID per copy.
`_common.buml.buml_fingerprint` parses each original BUML file and ignores
exactly those three; everything else (classes, attributes, methods,
enumerations, generalizations, associations, OCL constraints, role names,
multiplicities) must match. Statements that never reach the model are
dropped first: the source dataset defines overloaded methods by assigning
one variable twice, and only the binding that is read ends up in the model
(`_common.buml.dead_statements`, computed from what reads which binding).
If a variable is still assigned twice after that, statement order changes
the model and is kept for that file. The grouping therefore rests on the original dataset, not on
the PUML this repo generates from it.

The representative of a group is its alphabetically first model name, the
same rule as `select_test_generation_sample.py`. Models without a BUML file,
or whose BUML doesn't parse, are kept and reported.

Two steps:
  1. **BUML** (decides): group by `buml_fingerprint`, keep one per group.
  2. **PUML** (checks): the `.puml` files are generated from the BUML by
     `buml_to_puml.py`, so grouping by PUML must give the same result. A PUML
     group spanning several BUML models means the PUML leaves information
     out (before the 2026-10-18 fix: association role names); a BUML group
     with differing PUML means PUML generation isn't deterministic. Either
     prints a warning with examples -- regenerate the PUML and rerun. The
     model list is written either way, since it rests on step 1 alone.

Writes `<output-name>.txt` (one model per line, the --models-file for every
later step) and `<output-name>_report.json/.md`.

Usage:
    python scripts/select_unique_models.py [--models-file reports/usable_models.txt]
        [--dataset-dir PATH] [--reports-dir PATH] [--output-name unique_models]
"""
from __future__ import annotations

import argparse
import datetime
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from _common.buml import buml_fingerprint, find_buml_file, puml_digest  # noqa: E402
from _common.io import add_common_io_args, read_model_names, read_text_robust  # noqa: E402
from _common.report import write_reports  # noqa: E402


def category(model_dir: Path) -> str | None:
    path = model_dir / "category.txt"
    if not path.is_file():
        return None
    return read_text_robust(path).strip() or None


def puml_cross_check(by_fingerprint: dict[str, list[str]], dataset_dir: Path) -> dict:
    """How the PUML grouping relates to the BUML one."""
    puml_of = {name: puml_digest(dataset_dir / name) for members in by_fingerprint.values() for name in members}
    buml_of = {name: fp for fp, members in by_fingerprint.items() for name in members}
    by_puml: dict[str, list[str]] = {}
    for name, digest in puml_of.items():
        if digest is not None:
            by_puml.setdefault(digest, []).append(name)
    puml_wider = [sorted(members) for members in by_puml.values() if len({buml_of[m] for m in members}) > 1]
    puml_split = [sorted(members) for members in by_fingerprint.values()
                  if len({puml_of[m] for m in members}) > 1]
    return {
        "distinct_by_puml": len(by_puml),
        "models_without_puml": sum(1 for d in puml_of.values() if d is None),
        "puml_groups_spanning_several_buml_groups": sorted(puml_wider),
        "buml_groups_with_differing_puml": sorted(puml_split),
    }


def render_markdown_report(report: dict) -> str:
    sizes: dict[int, int] = {}
    for g in report["duplicate_groups"]:
        sizes[g["size"]] = sizes.get(g["size"], 0) + 1
    check = report["puml_cross_check"]
    lines = [
        "# Unique models (one per distinct BUML model)",
        "",
        f"Generated: {report['generated_at']}",
        "",
        f"- **Input:** `{report['models_file']}`, {report['input_count']} models",
        f"- **Kept:** {report['unique_count']} models",
        f"- **Removed as copies:** {report['removed_count']} models in {len(report['duplicate_groups'])} groups",
        f"- **Kept without comparison** (no BUML file / BUML doesn't parse): "
        f"{len(report['no_buml'])} / {len(report['unparsable_buml'])}",
        "",
        "Copies are identified from the original BUML sources, ignoring only set-item order, "
        "statement order, comments and the model's own random name (see the script's docstring). "
        "Statements that never reach the model (overwritten overloaded-method definitions) are "
        f"dropped first; statement order was still kept for {len(report['order_sensitive_buml'])} models "
        "that assign a variable twice even after that, where order changes the model.",
        "",
        "## Step 1: groups found in the BUML",
        "",
        "### Group sizes",
        "",
        "| Copies of one model | Groups |",
        "|---:|---:|",
    ]
    lines += [f"| {size} | {count} |" for size, count in sorted(sizes.items())]
    lines += [
        "",
        "### Largest groups",
        "",
        "| Representative | Copies | Category |",
        "|---|---:|---|",
    ]
    for g in report["duplicate_groups"][:20]:
        lines.append(f"| {g['representative']} | {g['size']} | {g['category'] or '–'} |")
    wider = check["puml_groups_spanning_several_buml_groups"]
    split = check["buml_groups_with_differing_puml"]
    lines += [
        "",
        "## Step 2: check against the generated PUML",
        "",
        f"**{'Agrees' if not wider and not split else 'Does not agree'}.** "
        f"Distinct by PUML: {check['distinct_by_puml']}, by BUML: {report['unique_count_with_buml']}.",
        "",
        f"- PUML groups spanning several BUML models (information missing from the PUML): {len(wider)}",
        f"- BUML groups whose PUML differs (PUML generation not deterministic): {len(split)}",
    ]
    for label, groups in (("spanning", wider), ("differing", split)):
        for members in groups[:10]:
            lines.append(f"  - {label}: {', '.join(members[:6])}{' …' if len(members) > 6 else ''} ({len(members)} models)")
    lines += ["", "Every group with all its members: see the accompanying `.json`."]
    return "\n".join(lines) + "\n"


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    add_common_io_args(parser, __file__)
    parser.add_argument("--models-file", type=Path, default=None,
                         help="Models to deduplicate (default: reports/usable_models.txt)")
    parser.add_argument("--output-name", default="unique_models")
    args = parser.parse_args()

    models_file = args.models_file or args.reports_dir / "usable_models.txt"
    names = sorted(set(read_model_names(models_file)))
    by_fingerprint: dict[str, list[str]] = {}
    no_buml: list[str] = []
    unparsable: list[dict] = []
    order_sensitive: list[str] = []
    for name in names:
        buml = find_buml_file(args.dataset_dir / name)
        if buml is None:
            no_buml.append(name)
            continue
        try:
            fingerprint, order_kept = buml_fingerprint(buml)
        except (SyntaxError, UnicodeDecodeError) as exc:
            unparsable.append({"model": name, "error": f"{type(exc).__name__}: {exc}"})
            continue
        if order_kept:
            order_sensitive.append(name)
        by_fingerprint.setdefault(fingerprint, []).append(name)

    kept = sorted([members[0] for members in by_fingerprint.values()] + no_buml + [u["model"] for u in unparsable])
    groups = sorted(
        ({"representative": members[0], "size": len(members), "duplicates": members[1:],
          "category": category(args.dataset_dir / members[0]), "buml_fingerprint": fingerprint}
         for fingerprint, members in by_fingerprint.items() if len(members) > 1),
        key=lambda g: (-g["size"], g["representative"]),
    )
    report = {
        "generated_at": datetime.datetime.now(datetime.timezone.utc).isoformat(),
        "models_file": str(models_file),
        "input_count": len(names),
        "unique_count": len(kept),
        "unique_count_with_buml": len(by_fingerprint),
        "removed_count": len(names) - len(kept),
        "no_buml": no_buml,
        "unparsable_buml": unparsable,
        "order_sensitive_buml": order_sensitive,
        "duplicate_groups": groups,
        "puml_cross_check": puml_cross_check(by_fingerprint, args.dataset_dir),
    }
    json_path, md_path = write_reports(args.reports_dir, f"{args.output_name}_report", report,
                                       render_markdown_report(report))
    txt_path = args.reports_dir / f"{args.output_name}.txt"
    txt_path.write_text("".join(f"{n}\n" for n in kept), encoding="utf-8")

    check = report["puml_cross_check"]
    print(f"Step 1 (BUML): {len(names)} models -> {len(kept)} unique ({report['removed_count']} copies removed "
          f"from {len(groups)} groups; {len(no_buml)} without BUML, {len(unparsable)} unparsable, kept; "
          f"statement order kept for {len(order_sensitive)})")
    for g in groups[:5]:
        print(f"  {g['representative']}: {g['size']} copies ({g['category'] or 'no category'})")
    wider = check["puml_groups_spanning_several_buml_groups"]
    split = check["buml_groups_with_differing_puml"]
    print(f"Step 2 (PUML check): {check['distinct_by_puml']} distinct by PUML vs {len(by_fingerprint)} by BUML")
    if wider or split:
        print(f"  WARNING: PUML disagrees with BUML -- {len(wider)} PUML groups span several BUML models, "
              f"{len(split)} BUML groups have differing PUML. Regenerate the PUML (buml_to_puml.py) and rerun.")
        for members in (wider + split)[:5]:
            print(f"    e.g. {', '.join(members[:4])}{' ...' if len(members) > 4 else ''}")
    else:
        print("  OK: PUML agrees with BUML")
    print(f"Model list: {txt_path}")
    print(f"Report written to {json_path} and {md_path}")


if __name__ == "__main__":
    main()
