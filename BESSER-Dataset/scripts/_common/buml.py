"""Locating, fingerprinting, loading and walking a model's BUML source. Only
`load_buml()` / `load_domain_model()` need `besser` (the `.venv-puml`
interpreter); it is imported inside them, so everything else works from any
venv.
"""
from __future__ import annotations

import ast
import hashlib
import importlib.util
import sys
import uuid
from pathlib import Path

OLD_GLOB = "*_BUML_model.py"
NEW_GLOB = "*_buml.py"


def find_buml_file(model_dir: Path) -> Path | None:
    """The model's BUML source file -- older models use `*_BUML_model.py`,
    newer ones `*_buml.py`."""
    matches = list(model_dir.glob(OLD_GLOB)) or list(model_dir.glob(NEW_GLOB))
    return matches[0] if matches else None


PUML_MODEL_NAME_PREFIX = "' model: "


def puml_digest(model_dir: Path) -> str | None:
    """SHA-256 of the model's `.puml` (line endings normalized), or None if it
    has none. `buml_to_puml.py` sorts every collection, so two models with the
    same diagram always get the same digest, even when their generated
    python_code.py differs in ordering. The `' model: <name>` header line is
    skipped, matching `buml_fingerprint`, which ignores the DomainModel's
    random name."""
    pumls = sorted(model_dir.glob("*.puml"))
    if not pumls:
        return None
    lines = pumls[0].read_text(encoding="utf-8").replace("\r\n", "\n").split("\n")
    kept = "\n".join(line for line in lines if not line.startswith(PUML_MODEL_NAME_PREFIX))
    return hashlib.sha256(kept.encode("utf-8")).hexdigest()


class _CanonicalBuml(ast.NodeTransformer):
    """Removes the only differences found between copies of one model:
    set-literal item order (Python prints sets in arbitrary order) and the
    DomainModel's own name (a random UUID or Eclipse ID per copy)."""

    def visit_Set(self, node: ast.Set) -> ast.Set:
        self.generic_visit(node)
        node.elts.sort(key=ast.unparse)
        return node

    def visit_Call(self, node: ast.Call) -> ast.Call:
        self.generic_visit(node)
        if isinstance(node.func, ast.Name) and node.func.id == "DomainModel":
            node.keywords = [k for k in node.keywords if k.arg != "name"]
        return node


ROOT_CALLS = {"DomainModel", "Project"}


def binding_name(statement) -> str | None:
    """The variable a top-level `name = ...` / `name: T = ...` binds, or None."""
    targets = [statement.target] if isinstance(statement, ast.AnnAssign) else getattr(statement, "targets", [])
    names = [t.id for t in targets if isinstance(t, ast.Name)]
    return names[0] if names else None


def dead_statements(tree: ast.Module) -> set[int]:
    """Indexes of top-level `name = ...` statements whose value can't reach
    the model: nothing reads that binding before it is overwritten, or ever
    (followed transitively from the roots -- DomainModel/Project bindings and
    every non-binding statement such as `X.methods = {...}`). The source
    dataset has these for overloaded methods: the same variable is assigned
    twice and only the binding read by `X.methods` ends up in the model."""
    latest: dict[str, int] = {}
    reads: dict[int, set[int]] = {}
    roots = []
    for i, statement in enumerate(tree.body):
        if isinstance(statement, (ast.Import, ast.ImportFrom)):
            continue
        value = getattr(statement, "value", None)
        reads[i] = {latest[n.id] for n in ast.walk(value) if isinstance(n, ast.Name) and n.id in latest} if value else set()
        name = binding_name(statement)
        is_root = isinstance(value, ast.Call) and isinstance(value.func, ast.Name) and value.func.id in ROOT_CALLS
        if name is None or is_root:
            roots.append(i)
        if name is not None:
            latest[name] = i
    live, stack = set(), list(roots)
    while stack:
        i = stack.pop()
        if i not in live:
            live.add(i)
            stack.extend(reads.get(i, ()))
    return {i for i in reads if i not in live}


class _ResolveReads(ast.NodeTransformer):
    """Rewrites every variable read to the token of the binding it resolves to."""

    def __init__(self, current: dict[str, str]):
        self.current = current

    def visit_Name(self, node: ast.Name) -> ast.Name:
        if isinstance(node.ctx, ast.Load) and node.id in self.current:
            return ast.copy_location(ast.Name(id=self.current[node.id], ctx=ast.Load()), node)
        return node


def buml_fingerprint(file_path: Path) -> tuple[str, bool]:
    """(SHA-256 of the original BUML source in canonical form, whether
    statement order had to be kept). The source is parsed as Python and:
      - set items are sorted and the DomainModel's `name=` is removed
        (_CanonicalBuml); comments and formatting are dropped by the parser;
      - statements that never reach the model are dropped (dead_statements:
        overwritten overloaded-method definitions);
      - every binding is renamed after its own content (`name@<hash of its
        value>`) and every read is rewritten to the binding it resolves to.
        The source reuses variable names (overloads; an attribute and an
        association both called `FoodItem_Food`), and this makes each
        statement mean the same thing wherever it stands;
      - statements are then sorted. Only if one property (`X.attributes`) is
        still assigned twice -- the last assignment wins -- is order kept.
    Two files get the same fingerprint only if the models they build have the
    same classes, attributes, methods, enumerations, generalizations,
    associations and constraints, role names and multiplicities included."""
    tree = _CanonicalBuml().visit(ast.parse(file_path.read_text(encoding="utf-8")))
    dead = dead_statements(tree)
    current: dict[str, str] = {}
    statements = []
    for i, statement in enumerate(tree.body):
        if i in dead:
            continue
        name = binding_name(statement)
        statement = _ResolveReads(current).visit(statement)
        if name is not None and getattr(statement, "value", None) is not None:
            token = f"{name}@{hashlib.sha256(ast.unparse(statement.value).encode('utf-8')).hexdigest()[:16]}"
            targets = [statement.target] if isinstance(statement, ast.AnnAssign) else statement.targets
            for target in targets:
                if isinstance(target, ast.Name) and target.id == name:
                    target.id = token
            current[name] = token
        statements.append(statement)
    property_targets = [ast.unparse(t) for statement in statements
                        for t in ([statement.target] if isinstance(statement, ast.AnnAssign)
                                  else getattr(statement, "targets", []))
                        if isinstance(t, ast.Attribute)]
    order_kept = len(property_targets) != len(set(property_targets))
    texts = [ast.unparse(statement) for statement in statements]
    if not order_kept:
        texts.sort()
    return hashlib.sha256("\n".join(texts).encode("utf-8")).hexdigest(), order_kept


def load_buml(file_path: Path):
    """(DomainModel, Project or None). Executes the BUML source under a
    unique throwaway module name (so models loaded in the same worker process
    never collide). The DomainModel is a top-level one, or else the first
    model of a Project; the Project carries the project name, owner and
    metadata description."""
    from besser.BUML.metamodel.project import Project
    from besser.BUML.metamodel.structural import DomainModel

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
    values = list(vars(module).values())
    project = next((v for v in values if isinstance(v, Project)), None)
    model = next((v for v in values if isinstance(v, DomainModel)), None)
    if model is None and project is not None and project.models:
        model = project.models[0]
    if model is None:
        raise ValueError(f"No DomainModel found in {file_path}")
    return model, project


def load_domain_model(file_path: Path) -> DomainModel:
    return load_buml(file_path)[0]


def type_name(value) -> str:
    return value.name if hasattr(value, "name") else str(value)


def ordered_ends(association):
    """Deterministic (end1, end2): association.ends is a set, so list order
    varies between runs under hash randomization."""
    ends = list(getattr(association, "ends", []))
    if len(ends) != 2:
        return None

    def end_key(end):
        multiplicity = getattr(end, "multiplicity", None)
        return (
            type_name(getattr(end, "type", "")),
            str(getattr(end, "name", "")),
            str(getattr(multiplicity, "min", "")),
            str(getattr(multiplicity, "max", "")),
            bool(getattr(end, "is_navigable", False)),
            bool(getattr(end, "is_composite", False)),
            bool(getattr(end, "is_aggregation", False)),
        )

    ordered = sorted(ends, key=end_key)
    return ordered[0], ordered[1]
