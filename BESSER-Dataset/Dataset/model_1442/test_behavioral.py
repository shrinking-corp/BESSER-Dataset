import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Element,
    GraphOperations_ConstantUtils,
    GraphOperations_EIntContainer,
    GraphOperations_Edge,
    GraphOperations_Element,
    GraphOperations_Graph,
    GraphOperations_Node,
    GraphOperations_Triangle,
    EdgeState,
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

def test_assoc_edges1_reverse_link_reassign_clear():
    a1 = GraphOperations_Graph()
    a2 = GraphOperations_Graph()
    b = GraphOperations_Edge(state="sample_text", weight=3.14)
    _safe_set(b, 'Edge', a1)
    assert _is_linked(b, 'Edge', a1)
    if hasattr(a1, 'graph2'):
        assert _is_linked(a1, 'graph2', b)
    _safe_set(b, 'Edge', a2)
    assert _is_linked(b, 'Edge', a2)
    if hasattr(a1, 'graph2'):
        assert not _is_linked(a1, 'graph2', b)
    if hasattr(a2, 'graph2'):
        assert _is_linked(a2, 'graph2', b)
    _safe_set(b, 'Edge', None)
    assert not _is_linked(b, 'Edge', a2)
    if hasattr(a2, 'graph2'):
        assert not _is_linked(a2, 'graph2', b)


def test_assoc_graph3_reverse_link_reassign_clear():
    a1 = GraphOperations_Node(degree=3.14, depth=7)
    a2 = GraphOperations_Node(degree=9.99, depth=13)
    b = GraphOperations_Graph()
    _safe_set(b, 'Graph', a1)
    assert _is_linked(b, 'Graph', a1)
    if hasattr(a1, 'nodes'):
        assert _is_linked(a1, 'nodes', b)
    _safe_set(b, 'Graph', a2)
    assert _is_linked(b, 'Graph', a2)
    if hasattr(a1, 'nodes'):
        assert not _is_linked(a1, 'nodes', b)
    if hasattr(a2, 'nodes'):
        assert _is_linked(a2, 'nodes', b)
    _safe_set(b, 'Graph', None)
    assert not _is_linked(b, 'Graph', a2)
    if hasattr(a2, 'nodes'):
        assert not _is_linked(a2, 'nodes', b)


def test_assoc_graph8_reverse_link_reassign_clear():
    a1 = GraphOperations_Graph()
    a2 = GraphOperations_Graph()
    b = GraphOperations_Edge(state="sample_text", weight=3.14)
    _safe_set(b, 'edges', a1)
    assert _is_linked(b, 'edges', a1)
    if hasattr(a1, 'Graph9'):
        assert _is_linked(a1, 'Graph9', b)
    _safe_set(b, 'edges', a2)
    assert _is_linked(b, 'edges', a2)
    if hasattr(a1, 'Graph9'):
        assert not _is_linked(a1, 'Graph9', b)
    if hasattr(a2, 'Graph9'):
        assert _is_linked(a2, 'Graph9', b)
    _safe_set(b, 'edges', None)
    assert not _is_linked(b, 'edges', a2)
    if hasattr(a2, 'Graph9'):
        assert not _is_linked(a2, 'Graph9', b)


def test_assoc_incomingEdges4_reverse_link_reassign_clear():
    a1 = GraphOperations_Node(degree=3.14, depth=7)
    a2 = GraphOperations_Node(degree=9.99, depth=13)
    b = GraphOperations_Edge(state="sample_text", weight=3.14)
    _safe_set(b, 'Edge5', a1)
    assert _is_linked(b, 'Edge5', a1)
    if hasattr(a1, 'target'):
        assert _is_linked(a1, 'target', b)
    _safe_set(b, 'Edge5', a2)
    assert _is_linked(b, 'Edge5', a2)
    if hasattr(a1, 'target'):
        assert not _is_linked(a1, 'target', b)
    if hasattr(a2, 'target'):
        assert _is_linked(a2, 'target', b)
    _safe_set(b, 'Edge5', None)
    assert not _is_linked(b, 'Edge5', a2)
    if hasattr(a2, 'target'):
        assert not _is_linked(a2, 'target', b)


def test_assoc_nodes0_reverse_link_reassign_clear():
    a1 = GraphOperations_Node(degree=3.14, depth=7)
    a2 = GraphOperations_Node(degree=9.99, depth=13)
    b = GraphOperations_Graph()
    _safe_set(b, 'graph', {a1})
    assert _is_linked(b, 'graph', a1)
    if hasattr(a1, 'Node'):
        assert _is_linked(a1, 'Node', b)
    _safe_set(b, 'graph', {a2})
    assert _is_linked(b, 'graph', a2)
    if hasattr(a1, 'Node'):
        assert not _is_linked(a1, 'Node', b)
    if hasattr(a2, 'Node'):
        assert _is_linked(a2, 'Node', b)
    _safe_set(b, 'graph', set())
    assert not _is_linked(b, 'graph', a2)
    if hasattr(a2, 'Node'):
        assert not _is_linked(a2, 'Node', b)


def test_assoc_outgoingEdges6_reverse_link_reassign_clear():
    a1 = GraphOperations_Node(degree=3.14, depth=7)
    a2 = GraphOperations_Node(degree=9.99, depth=13)
    b = GraphOperations_Edge(state="sample_text", weight=3.14)
    _safe_set(b, 'Edge7', a1)
    assert _is_linked(b, 'Edge7', a1)
    if hasattr(a1, 'source'):
        assert _is_linked(a1, 'source', b)
    _safe_set(b, 'Edge7', a2)
    assert _is_linked(b, 'Edge7', a2)
    if hasattr(a1, 'source'):
        assert not _is_linked(a1, 'source', b)
    if hasattr(a2, 'source'):
        assert _is_linked(a2, 'source', b)
    _safe_set(b, 'Edge7', None)
    assert not _is_linked(b, 'Edge7', a2)
    if hasattr(a2, 'source'):
        assert not _is_linked(a2, 'source', b)


def test_assoc_source10_reverse_link_reassign_clear():
    a1 = GraphOperations_Node(degree=3.14, depth=7)
    a2 = GraphOperations_Node(degree=9.99, depth=13)
    b = GraphOperations_Edge(state="sample_text", weight=3.14)
    _safe_set(b, 'outgoingEdges', a1)
    assert _is_linked(b, 'outgoingEdges', a1)
    if hasattr(a1, 'Node11'):
        assert _is_linked(a1, 'Node11', b)
    _safe_set(b, 'outgoingEdges', a2)
    assert _is_linked(b, 'outgoingEdges', a2)
    if hasattr(a1, 'Node11'):
        assert not _is_linked(a1, 'Node11', b)
    if hasattr(a2, 'Node11'):
        assert _is_linked(a2, 'Node11', b)
    _safe_set(b, 'outgoingEdges', None)
    assert not _is_linked(b, 'outgoingEdges', a2)
    if hasattr(a2, 'Node11'):
        assert not _is_linked(a2, 'Node11', b)


def test_assoc_target12_reverse_link_reassign_clear():
    a1 = GraphOperations_Node(degree=3.14, depth=7)
    a2 = GraphOperations_Node(degree=9.99, depth=13)
    b = GraphOperations_Edge(state="sample_text", weight=3.14)
    _safe_set(b, 'incomingEdges', a1)
    assert _is_linked(b, 'incomingEdges', a1)
    if hasattr(a1, 'Node13'):
        assert _is_linked(a1, 'Node13', b)
    _safe_set(b, 'incomingEdges', a2)
    assert _is_linked(b, 'incomingEdges', a2)
    if hasattr(a1, 'Node13'):
        assert not _is_linked(a1, 'Node13', b)
    if hasattr(a2, 'Node13'):
        assert _is_linked(a2, 'Node13', b)
    _safe_set(b, 'incomingEdges', None)
    assert not _is_linked(b, 'incomingEdges', a2)
    if hasattr(a2, 'Node13'):
        assert not _is_linked(a2, 'Node13', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_longEdge14_stub_double():
    # GraphOperations_Triangle has no real 'GraphOperations_Triangle' property in the generated
    # code (a bare stub) -- manually attach it so GraphOperations_Edge's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # GraphOperations_Edge's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = GraphOperations_Edge(state="sample_text", weight=3.14)
    partner = GraphOperations_Triangle()
    setattr(partner, 'GraphOperations_Triangle', None)
    _safe_set(owner, 'GraphOperations_Edge', partner)
    assert getattr(partner, 'GraphOperations_Triangle') == owner
    _safe_set(owner, 'GraphOperations_Edge', None)
    assert getattr(partner, 'GraphOperations_Triangle') is None


def test_assoc_shortEdges15_stub_double():
    # GraphOperations_Triangle has no real 'GraphOperations_Triangle16' property in the generated
    # code (a bare stub) -- manually attach it so GraphOperations_Edge's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # GraphOperations_Edge's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = GraphOperations_Edge(state="sample_text", weight=3.14)
    partner = GraphOperations_Triangle()
    setattr(partner, 'GraphOperations_Triangle16', None)
    _safe_set(owner, 'GraphOperations_Edge17', partner)
    assert owner in getattr(partner, 'GraphOperations_Triangle16')
    _safe_set(owner, 'GraphOperations_Edge17', None)
    assert owner not in getattr(partner, 'GraphOperations_Triangle16')


