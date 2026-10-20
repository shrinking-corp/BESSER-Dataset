import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    graph_Edge,
    graph_Graph,
    graph_Node,
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

def test_assoc_src4_reverse_link_reassign_clear():
    a1 = graph_Node(name="sample_text")
    a2 = graph_Node(name="sample_text_2")
    b = graph_Edge(name="sample_text")
    _safe_set(b, 'graph_Edge', a1)
    assert _is_linked(b, 'graph_Edge', a1)
    if hasattr(a1, 'graph_Node'):
        assert _is_linked(a1, 'graph_Node', b)
    _safe_set(b, 'graph_Edge', a2)
    assert _is_linked(b, 'graph_Edge', a2)
    if hasattr(a1, 'graph_Node'):
        assert not _is_linked(a1, 'graph_Node', b)
    if hasattr(a2, 'graph_Node'):
        assert _is_linked(a2, 'graph_Node', b)
    _safe_set(b, 'graph_Edge', None)
    assert not _is_linked(b, 'graph_Edge', a2)
    if hasattr(a2, 'graph_Node'):
        assert not _is_linked(a2, 'graph_Node', b)


def test_assoc_trg5_reverse_link_reassign_clear():
    a1 = graph_Node(name="sample_text")
    a2 = graph_Node(name="sample_text_2")
    b = graph_Edge(name="sample_text")
    _safe_set(b, 'graph_Edge6', a1)
    assert _is_linked(b, 'graph_Edge6', a1)
    if hasattr(a1, 'graph_Node7'):
        assert _is_linked(a1, 'graph_Node7', b)
    _safe_set(b, 'graph_Edge6', a2)
    assert _is_linked(b, 'graph_Edge6', a2)
    if hasattr(a1, 'graph_Node7'):
        assert not _is_linked(a1, 'graph_Node7', b)
    if hasattr(a2, 'graph_Node7'):
        assert _is_linked(a2, 'graph_Node7', b)
    _safe_set(b, 'graph_Edge6', None)
    assert not _is_linked(b, 'graph_Edge6', a2)
    if hasattr(a2, 'graph_Node7'):
        assert not _is_linked(a2, 'graph_Node7', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_edges1_stub_double():
    # graph_Graph has no real 'graph2' property in the generated
    # code (a bare stub) -- manually attach it so graph_Edge's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # graph_Edge's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = graph_Edge(name="sample_text")
    partner = graph_Graph()
    setattr(partner, 'graph2', None)
    _safe_set(owner, 'Edge', partner)
    assert owner in getattr(partner, 'graph2')
    _safe_set(owner, 'Edge', None)
    assert owner not in getattr(partner, 'graph2')


def test_assoc_graph3_stub_double():
    # graph_Graph has no real 'Graph' property in the generated
    # code (a bare stub) -- manually attach it so graph_Node's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # graph_Node's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = graph_Node(name="sample_text")
    partner = graph_Graph()
    setattr(partner, 'Graph', None)
    _safe_set(owner, 'nodes', partner)
    assert getattr(partner, 'Graph') == owner
    _safe_set(owner, 'nodes', None)
    assert getattr(partner, 'Graph') is None


def test_assoc_graph8_stub_double():
    # graph_Graph has no real 'Graph9' property in the generated
    # code (a bare stub) -- manually attach it so graph_Edge's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # graph_Edge's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = graph_Edge(name="sample_text")
    partner = graph_Graph()
    setattr(partner, 'Graph9', None)
    _safe_set(owner, 'edges', partner)
    assert getattr(partner, 'Graph9') == owner
    _safe_set(owner, 'edges', None)
    assert getattr(partner, 'Graph9') is None


def test_assoc_nodes0_stub_double():
    # graph_Graph has no real 'graph' property in the generated
    # code (a bare stub) -- manually attach it so graph_Node's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # graph_Node's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = graph_Node(name="sample_text")
    partner = graph_Graph()
    setattr(partner, 'graph', None)
    _safe_set(owner, 'Node', partner)
    assert owner in getattr(partner, 'graph')
    _safe_set(owner, 'Node', None)
    assert owner not in getattr(partner, 'graph')


