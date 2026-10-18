"""Sanitizing CrossHair's generated pytest output.

Three real defects in CrossHair's output, all found 2026-10-11..17 (see
docs/DECISIONS.md), each making a test fail on the UNMUTATED source and so
inflating mutation scores to a fake 1.0:
- invalid syntax: a bare object repr dumped into a set literal;
- tests of Python's own `Enum` internals (`Enum.__new__`,
  `Enum._generate_next_value_`) -- standard library, not model code, and
  matching an exact error message whose wording differs between Python
  versions;
- `datetime.date(...)` used with no `import datetime` -- a NameError on its
  own, and a TypeError once merged next to suites that do
  `from datetime import datetime` (the class shadows the module name).

The module reference is rewritten to a private alias rather than adding a
plain `import datetime`, which would in turn shadow the `datetime` class the
other merged suites rely on. Idempotent: sanitizing already-sanitized output
changes nothing.
"""
from __future__ import annotations

import ast

_MODULE_ALIASES = {"datetime": "_ch_datetime"}
_STDLIB_CLASSES = frozenset({"Enum"})


class _AliasModuleNames(ast.NodeTransformer):
    def visit_Name(self, node: ast.Name) -> ast.Name:
        alias = _MODULE_ALIASES.get(node.id)
        if alias and isinstance(node.ctx, ast.Load):
            return ast.copy_location(ast.Name(id=alias, ctx=node.ctx), node)
        return node


def _references_any(node: ast.AST, names: set[str]) -> bool:
    return any(isinstance(n, ast.Name) and n.id in names for n in ast.walk(node))


def sanitize_crosshair_tests(source: str) -> tuple[str | None, list[str]]:
    """Returns (sanitized_source, dropped_test_names), or (None, []) if
    `source` isn't valid Python at all."""
    try:
        tree = ast.parse(source)
    except SyntaxError:
        return None, []

    stdlib_names = {
        alias.asname or alias.name
        for node in tree.body
        if isinstance(node, ast.ImportFrom) and node.module == "enum"
        for alias in node.names
        if alias.name in _STDLIB_CLASSES
    }
    dropped: list[str] = []
    kept: list[ast.stmt] = []
    for node in tree.body:
        if isinstance(node, ast.FunctionDef) and stdlib_names and _references_any(node, stdlib_names):
            dropped.append(node.name)
            continue
        kept.append(node)
    tree.body = kept
    if stdlib_names and not any(_references_any(n, stdlib_names) for n in kept
                                if not isinstance(n, ast.ImportFrom)):
        tree.body = [n for n in tree.body if not (isinstance(n, ast.ImportFrom) and n.module == "enum")]

    tree = _AliasModuleNames().visit(tree)
    existing_imports = {
        (alias.name, alias.asname)
        for node in tree.body if isinstance(node, ast.Import)
        for alias in node.names
    }
    needed = [
        ast.Import(names=[ast.alias(name=module, asname=alias)])
        for module, alias in sorted(_MODULE_ALIASES.items())
        if _references_any(tree, {alias}) and (module, alias) not in existing_imports
    ]
    tree.body = needed + tree.body
    ast.fix_missing_locations(tree)
    return ast.unparse(tree) + "\n", dropped
