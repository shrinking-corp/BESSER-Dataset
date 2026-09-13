"""Extract class-diagram-relevant structure (classes, methods, attributes,
inheritance, decorators, ...) from a Python source file using tree-sitter.

The `.scm` files in `scripts/queries/` locate the CST (concrete syntax tree)
nodes we care about -- class definitions, function/method definitions, and
attribute assignments. This module resolves the relationships between those
nodes (which class owns which method/attribute, which decorators apply to
which definition) using tree-sitter's field/parent API directly, since that
is far simpler than trying to express nesting and "nearest enclosing
definition" logic inside the query language itself.

Relationships between classes (associations/aggregation/composition) are
deliberately out of scope for this extractor -- see the project discussion
that scoped this down to classes/methods/attributes/inheritance first.

Requires `tree-sitter` and `tree-sitter-python` (see the project venv note
at the top of generate_code_structure.py).
"""
from __future__ import annotations

from pathlib import Path

from tree_sitter import Language, Node, Parser, Query, QueryCursor
import tree_sitter_python as tspython

QUERIES_DIR = Path(__file__).resolve().parent / "queries"
PY_LANGUAGE = Language(tspython.language())

ENUM_BASE_NAMES = {"Enum", "IntEnum", "StrEnum", "Flag", "IntFlag"}
ABSTRACT_BASE_NAMES = {"ABC"}
ABSTRACT_METHOD_DECORATORS = {"abstractmethod", "abstractproperty"}


def _load_query(filename: str) -> Query:
    return Query(PY_LANGUAGE, (QUERIES_DIR / filename).read_text())


CLASSES_QUERY = _load_query("classes.scm")
FUNCTIONS_QUERY = _load_query("functions.scm")
ATTRIBUTES_QUERY = _load_query("attributes.scm")


def _text(src: bytes, node: Node | None) -> str | None:
    if node is None:
        return None
    return src[node.start_byte:node.end_byte].decode("utf-8", errors="replace")


def _decorators_of(node: Node, src: bytes) -> list[str]:
    """Decorator names on `node`, e.g. ['property'] or ['dataclass'].

    A decorated definition is wrapped one level up in a `decorated_definition`
    node (the class/function node itself has no decorator field), so this
    looks at the parent rather than at `node`.
    """
    parent = node.parent
    if parent is None or parent.type != "decorated_definition":
        return []
    names = []
    for child in parent.children:
        if child.type != "decorator":
            continue
        # A decorator's children are `@` followed by an identifier, an
        # attribute (`a.b`), or a call (`a.b(...)`) -- take the text minus
        # the leading `@` and, for a call, minus the argument list.
        expr = child.children[1] if len(child.children) > 1 else child
        text = _text(src, expr)
        names.append(text.split("(", 1)[0].strip() if text else "")
    return names


def _visibility(name: str) -> str:
    if name.startswith("__") and name.endswith("__"):
        return "public"  # dunder methods (__init__, __eq__, ...) are part of the public API
    if name.startswith("__"):
        return "private"
    if name.startswith("_"):
        return "protected"
    return "public"


def _docstring_of(body: Node, src: bytes) -> str | None:
    if body.child_count == 0:
        return None
    first = body.children[0]
    if first.type != "expression_statement" or first.child_count == 0:
        return None
    string_node = first.children[0]
    if string_node.type != "string":
        return None
    text = _text(src, string_node)
    return text.strip("'\" \n") if text else None


def _base_names(superclasses: Node | None, src: bytes) -> list[str]:
    """Names from a class's `superclasses: (argument_list)` field.

    Only plain names are resolved (`Base`, `module.Base`); a metaclass
    keyword argument (`metaclass=ABCMeta`) or a call is kept as raw text so
    nothing is silently dropped.
    """
    if superclasses is None:
        return []
    names = []
    for child in superclasses.children:
        if child.type in ("(", ")", ","):
            continue
        if child.type == "identifier":
            names.append(_text(src, child))
        elif child.type == "attribute":
            names.append(_text(src, child))
        else:
            names.append(_text(src, child))  # keyword_argument, call, etc. -- kept as-is
    return [n for n in names if n]


def _nearest_enclosing_definition(node: Node) -> Node | None:
    """Walk up from `node` to the nearest class_definition or
    function_definition ancestor (skipping decorated_definition wrappers).

    This is how a method is told apart from a top-level function, and how a
    method's owning class is found, regardless of how deeply the definition
    is nested inside if/for/try blocks.
    """
    current = node.parent
    while current is not None:
        if current.type in ("class_definition", "function_definition"):
            return current
        current = current.parent
    return None


def _parse_parameters(parameters: Node, src: bytes) -> list[dict]:
    params = []
    for child in parameters.children:
        if child.type in ("(", ")", ",", "*", "/"):
            continue
        if child.type == "identifier":
            params.append({"name": _text(src, child), "type": None, "default": None})
        elif child.type == "typed_parameter":
            # unnamed identifier child + `type:` field
            name_node = next((c for c in child.children if c.type == "identifier"), None)
            params.append({
                "name": _text(src, name_node),
                "type": _text(src, child.child_by_field_name("type")),
                "default": None,
            })
        elif child.type == "default_parameter":
            params.append({
                "name": _text(src, child.child_by_field_name("name")),
                "type": None,
                "default": _text(src, child.child_by_field_name("value")),
            })
        elif child.type == "typed_default_parameter":
            params.append({
                "name": _text(src, child.child_by_field_name("name")),
                "type": _text(src, child.child_by_field_name("type")),
                "default": _text(src, child.child_by_field_name("value")),
            })
        elif child.type == "list_splat_pattern":
            params.append({"name": f"*{_text(src, child.children[-1])}", "type": None, "default": None})
        elif child.type == "dictionary_splat_pattern":
            params.append({"name": f"**{_text(src, child.children[-1])}", "type": None, "default": None})
    return params


def extract_module_structure(source: str) -> dict:
    """Parse `source` (a Python file's text) and return its class-diagram
    structure: module-level functions plus classes with their bases,
    decorators, modifiers, attributes, and methods.
    """
    src = source.encode("utf-8")
    parser = Parser(PY_LANGUAGE)
    tree = parser.parse(src)
    root = tree.root_node

    class_matches = QueryCursor(CLASSES_QUERY).matches(root)
    class_nodes = [m[1]["class.def"][0] for m in class_matches]

    function_matches = QueryCursor(FUNCTIONS_QUERY).matches(root)
    function_nodes = [m[1]["function.def"][0] for m in function_matches]

    attribute_matches = QueryCursor(ATTRIBUTES_QUERY).matches(root)

    classes_by_id: dict[int, dict] = {}
    class_node_by_id: dict[int, Node] = {}
    for node in class_nodes:
        name = _text(src, node.child_by_field_name("name"))
        bases = _base_names(node.child_by_field_name("superclasses"), src)
        decorators = _decorators_of(node, src)
        classes_by_id[node.id] = {
            "name": name,
            "line_start": node.start_point[0] + 1,
            "line_end": node.end_point[0] + 1,
            "bases": bases,
            "decorators": decorators,
            "is_abstract": bool(ABSTRACT_BASE_NAMES & set(bases)),  # refined below once methods are known
            "is_enum": bool(ENUM_BASE_NAMES & set(bases)),
            "is_dataclass": "dataclass" in decorators,
            "docstring": _docstring_of(node.child_by_field_name("body"), src),
            "attributes": [],
            "methods": [],
        }
        class_node_by_id[node.id] = node

    module_functions = []
    methods_by_class_id: dict[int, list[dict]] = {cid: [] for cid in classes_by_id}
    init_method_node_by_class_id: dict[int, Node] = {}

    for node in function_nodes:
        name = _text(src, node.child_by_field_name("name"))
        decorators = _decorators_of(node, src)
        params = _parse_parameters(node.child_by_field_name("parameters"), src)
        method_info = {
            "name": name,
            "visibility": _visibility(name),
            "decorators": decorators,
            "is_static": "staticmethod" in decorators,
            "is_classmethod": "classmethod" in decorators,
            "is_abstract": bool(ABSTRACT_METHOD_DECORATORS & set(decorators)),
            "parameters": params,
            "return_type": _text(src, node.child_by_field_name("return_type")),
            "docstring": _docstring_of(node.child_by_field_name("body"), src),
            "line_start": node.start_point[0] + 1,
            "line_end": node.end_point[0] + 1,
        }

        owner = _nearest_enclosing_definition(node)
        if owner is not None and owner.type == "class_definition" and owner.id in classes_by_id:
            methods_by_class_id[owner.id].append(method_info)
            if name == "__init__":
                init_method_node_by_class_id[owner.id] = node
        elif owner is None:
            module_functions.append(method_info)
        # else: a function nested inside another function -- out of scope, skipped

    attributes_by_class_id: dict[int, list[dict]] = {cid: [] for cid in classes_by_id}
    for pattern_index, captures in attribute_matches:
        name = _text(src, captures["attribute.name"][0])
        attr_type = _text(src, captures.get("attribute.type", [None])[0])
        value = _text(src, captures.get("attribute.value", [None])[0])
        line = captures["attribute.assignment"][0].start_point[0] + 1

        if "attribute.owner" in captures:
            # class-body assignment: owning class captured directly by the query
            owner_id = captures["attribute.owner"][0].id
            if owner_id in attributes_by_class_id:
                attributes_by_class_id[owner_id].append({
                    "name": name, "type": attr_type, "default": value,
                    "visibility": _visibility(name), "is_class_var": True, "line": line,
                })
        else:
            # self.x = ... -- only keep the ones inside __init__ (see attributes.scm)
            assignment_node = captures["attribute.assignment"][0]
            enclosing_method = _nearest_enclosing_definition(assignment_node)
            if enclosing_method is None or _text(src, enclosing_method.child_by_field_name("name")) != "__init__":
                continue
            owner_class = _nearest_enclosing_definition(enclosing_method)
            if owner_class is not None and owner_class.id in attributes_by_class_id:
                attributes_by_class_id[owner_class.id].append({
                    "name": name, "type": attr_type, "default": value,
                    "visibility": _visibility(name), "is_class_var": False, "line": line,
                })

    classes = []
    for node in class_nodes:
        info = classes_by_id[node.id]
        methods = methods_by_class_id[node.id]
        info["is_abstract"] = info["is_abstract"] or any(m["is_abstract"] for m in methods)
        info["methods"] = methods
        info["attributes"] = attributes_by_class_id[node.id]
        classes.append(info)

    return {
        "has_error": root.has_error,  # true if tree-sitter's error-recovery kicked in
        "functions": module_functions,
        "classes": classes,
    }
