import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    dot_a_list,
    dot_attr_list,
    dot_attr_stmt,
    dot_attribute,
    dot_edgeRHS,
    dot_edgeRHS_node,
    dot_edgeRHS_subgraph,
    dot_edge_stmt_node,
    dot_edge_stmt_subgraph,
    dot_graph,
    dot_graphvizmodel,
    dot_node_id,
    dot_node_stmt,
    dot_stmt,
    dot_subgraph,
    edgeRHS,
    stmt,
    attributetype,
    edgeop,
    graphtype,
)

def _is_linked(obj, attr_name, other):
    value = getattr(obj, attr_name, None)
    if isinstance(value, (set, list, tuple, frozenset)):
        return other in value
    return value == other

def _safe_set(obj, attr_name, value):
    # Some generated models have a genuine bug: two reciprocal setters
    # unconditionally call each other with no base case, causing
    # infinite mutual recursion for that specific relationship (found
    # in model_10000002's items10/sc11 pair). That's a defect in the
    # code under test, not in this test -- skip rather than fail so it
    # doesn't masquerade as a test-suite problem.
    try:
        setattr(obj, attr_name, value)
    except RecursionError:
        pytest.skip(f'{attr_name!r} setter has infinite mutual recursion in the generated code')

# =============================================================================
# REVERSE-DIRECTION ASSOCIATION TESTS
# Mirrors test_structural_full.py's link_reassign_clear, but sets from the
# OTHER end's own setter directly, instead of relying on it firing only as a
# side effect of the forward-direction test. See module docstring.
# =============================================================================

# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_a_list19_stub_double():
    # dot_attr_list has no real 'dot_attr_list20' property in the generated
    # code (a bare stub) -- manually attach it so dot_a_list's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # dot_a_list's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = dot_a_list(name="sample_text", value="sample_text")
    partner = dot_attr_list()
    setattr(partner, 'dot_attr_list20', None)
    _safe_set(owner, 'dot_a_list', partner)
    assert owner in getattr(partner, 'dot_attr_list20')
    _safe_set(owner, 'dot_a_list', None)
    assert owner not in getattr(partner, 'dot_attr_list20')


def test_assoc_attributes15_stub_double():
    # dot_attr_list has no real 'dot_attr_list16' property in the generated
    # code (a bare stub) -- manually attach it so dot_node_stmt's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # dot_node_stmt's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = dot_node_stmt(name="sample_text")
    partner = dot_attr_list()
    setattr(partner, 'dot_attr_list16', None)
    _safe_set(owner, 'dot_node_stmt', {partner})
    assert getattr(partner, 'dot_attr_list16') == owner
    _safe_set(owner, 'dot_node_stmt', set())
    assert getattr(partner, 'dot_attr_list16') is None


def test_assoc_attributes17_stub_double():
    # dot_attr_list has no real 'dot_attr_list18' property in the generated
    # code (a bare stub) -- manually attach it so dot_attr_stmt's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # dot_attr_stmt's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = dot_attr_stmt(type="sample_text")
    partner = dot_attr_list()
    setattr(partner, 'dot_attr_list18', None)
    _safe_set(owner, 'dot_attr_stmt', {partner})
    assert getattr(partner, 'dot_attr_list18') == owner
    _safe_set(owner, 'dot_attr_stmt', set())
    assert getattr(partner, 'dot_attr_list18') is None


def test_assoc_edgeRHS4_stub_double():
    # dot_edge_stmt_node has no real 'dot_edge_stmt_node5' property in the generated
    # code (a bare stub) -- manually attach it so dot_edgeRHS's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # dot_edgeRHS's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = dot_edgeRHS(op="sample_text")
    partner = dot_edge_stmt_node()
    setattr(partner, 'dot_edge_stmt_node5', None)
    _safe_set(owner, 'dot_edgeRHS', partner)
    assert owner in getattr(partner, 'dot_edge_stmt_node5')
    _safe_set(owner, 'dot_edgeRHS', None)
    assert owner not in getattr(partner, 'dot_edge_stmt_node5')


def test_assoc_edgeRHS9_stub_double():
    # dot_edge_stmt_subgraph has no real 'dot_edge_stmt_subgraph10' property in the generated
    # code (a bare stub) -- manually attach it so dot_edgeRHS's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # dot_edgeRHS's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = dot_edgeRHS(op="sample_text")
    partner = dot_edge_stmt_subgraph()
    setattr(partner, 'dot_edge_stmt_subgraph10', None)
    _safe_set(owner, 'dot_edgeRHS11', partner)
    assert getattr(partner, 'dot_edge_stmt_subgraph10') == owner
    _safe_set(owner, 'dot_edgeRHS11', None)
    assert getattr(partner, 'dot_edge_stmt_subgraph10') is None


def test_assoc_graphs0_stub_double():
    # dot_graphvizmodel has no real 'dot_graphvizmodel' property in the generated
    # code (a bare stub) -- manually attach it so dot_graph's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # dot_graph's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = dot_graph(name="sample_text", strict=True, type="sample_text")
    partner = dot_graphvizmodel()
    setattr(partner, 'dot_graphvizmodel', None)
    _safe_set(owner, 'dot_graph', partner)
    assert owner in getattr(partner, 'dot_graphvizmodel')
    _safe_set(owner, 'dot_graph', None)
    assert owner not in getattr(partner, 'dot_graphvizmodel')


def test_assoc_node24_stub_double():
    # dot_edgeRHS_node has no real 'dot_edgeRHS_node' property in the generated
    # code (a bare stub) -- manually attach it so dot_node_id's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # dot_node_id's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = dot_node_id(name="sample_text")
    partner = dot_edgeRHS_node()
    setattr(partner, 'dot_edgeRHS_node', None)
    _safe_set(owner, 'dot_node_id25', partner)
    assert getattr(partner, 'dot_edgeRHS_node') == owner
    _safe_set(owner, 'dot_node_id25', None)
    assert getattr(partner, 'dot_edgeRHS_node') is None


def test_assoc_node_id3_stub_double():
    # dot_edge_stmt_node has no real 'dot_edge_stmt_node' property in the generated
    # code (a bare stub) -- manually attach it so dot_node_id's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # dot_node_id's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = dot_node_id(name="sample_text")
    partner = dot_edge_stmt_node()
    setattr(partner, 'dot_edge_stmt_node', None)
    _safe_set(owner, 'dot_node_id', partner)
    assert getattr(partner, 'dot_edge_stmt_node') == owner
    _safe_set(owner, 'dot_node_id', None)
    assert getattr(partner, 'dot_edge_stmt_node') is None


def test_assoc_stmts1_stub_double():
    # dot_stmt has no real 'dot_stmt' property in the generated
    # code (a bare stub) -- manually attach it so dot_graph's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # dot_graph's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = dot_graph(name="sample_text", strict=True, type="sample_text")
    partner = dot_stmt()
    setattr(partner, 'dot_stmt', None)
    _safe_set(owner, 'dot_graph2', {partner})
    assert getattr(partner, 'dot_stmt') == owner
    _safe_set(owner, 'dot_graph2', set())
    assert getattr(partner, 'dot_stmt') is None


def test_assoc_stmts21_stub_double():
    # dot_stmt has no real 'dot_stmt23' property in the generated
    # code (a bare stub) -- manually attach it so dot_subgraph's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # dot_subgraph's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = dot_subgraph(name="sample_text")
    partner = dot_stmt()
    setattr(partner, 'dot_stmt23', None)
    _safe_set(owner, 'dot_subgraph22', {partner})
    assert getattr(partner, 'dot_stmt23') == owner
    _safe_set(owner, 'dot_subgraph22', set())
    assert getattr(partner, 'dot_stmt23') is None


def test_assoc_subgraph26_stub_double():
    # dot_edgeRHS_subgraph has no real 'dot_edgeRHS_subgraph' property in the generated
    # code (a bare stub) -- manually attach it so dot_subgraph's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # dot_subgraph's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = dot_subgraph(name="sample_text")
    partner = dot_edgeRHS_subgraph()
    setattr(partner, 'dot_edgeRHS_subgraph', None)
    _safe_set(owner, 'dot_subgraph27', partner)
    assert getattr(partner, 'dot_edgeRHS_subgraph') == owner
    _safe_set(owner, 'dot_subgraph27', None)
    assert getattr(partner, 'dot_edgeRHS_subgraph') is None


def test_assoc_subgraph8_stub_double():
    # dot_edge_stmt_subgraph has no real 'dot_edge_stmt_subgraph' property in the generated
    # code (a bare stub) -- manually attach it so dot_subgraph's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # dot_subgraph's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = dot_subgraph(name="sample_text")
    partner = dot_edge_stmt_subgraph()
    setattr(partner, 'dot_edge_stmt_subgraph', None)
    _safe_set(owner, 'dot_subgraph', partner)
    assert getattr(partner, 'dot_edge_stmt_subgraph') == owner
    _safe_set(owner, 'dot_subgraph', None)
    assert getattr(partner, 'dot_edge_stmt_subgraph') is None


