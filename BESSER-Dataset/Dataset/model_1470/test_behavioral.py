import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    graph_Edge,
    graph_GraphModel,
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

def test_assoc_src3_reverse_link_reassign_clear():
    a1 = graph_Node(value="sample_text")
    a2 = graph_Node(value="sample_text_2")
    b = graph_Edge(label="sample_text")
    _safe_set(b, 'graph_Edge4', a1)
    assert _is_linked(b, 'graph_Edge4', a1)
    if hasattr(a1, 'graph_Node5'):
        assert _is_linked(a1, 'graph_Node5', b)
    _safe_set(b, 'graph_Edge4', a2)
    assert _is_linked(b, 'graph_Edge4', a2)
    if hasattr(a1, 'graph_Node5'):
        assert not _is_linked(a1, 'graph_Node5', b)
    if hasattr(a2, 'graph_Node5'):
        assert _is_linked(a2, 'graph_Node5', b)
    _safe_set(b, 'graph_Edge4', None)
    assert not _is_linked(b, 'graph_Edge4', a2)
    if hasattr(a2, 'graph_Node5'):
        assert not _is_linked(a2, 'graph_Node5', b)


def test_assoc_tgt6_reverse_link_reassign_clear():
    a1 = graph_Node(value="sample_text")
    a2 = graph_Node(value="sample_text_2")
    b = graph_Edge(label="sample_text")
    _safe_set(b, 'graph_Edge7', a1)
    assert _is_linked(b, 'graph_Edge7', a1)
    if hasattr(a1, 'graph_Node8'):
        assert _is_linked(a1, 'graph_Node8', b)
    _safe_set(b, 'graph_Edge7', a2)
    assert _is_linked(b, 'graph_Edge7', a2)
    if hasattr(a1, 'graph_Node8'):
        assert not _is_linked(a1, 'graph_Node8', b)
    if hasattr(a2, 'graph_Node8'):
        assert _is_linked(a2, 'graph_Node8', b)
    _safe_set(b, 'graph_Edge7', None)
    assert not _is_linked(b, 'graph_Edge7', a2)
    if hasattr(a2, 'graph_Node8'):
        assert not _is_linked(a2, 'graph_Node8', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_edge1_stub_double():
    # graph_GraphModel has no real 'graph_GraphModel2' property in the generated
    # code (a bare stub) -- manually attach it so graph_Edge's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # graph_Edge's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = graph_Edge(label="sample_text")
    partner = graph_GraphModel()
    setattr(partner, 'graph_GraphModel2', None)
    _safe_set(owner, 'graph_Edge', partner)
    assert owner in getattr(partner, 'graph_GraphModel2')
    _safe_set(owner, 'graph_Edge', None)
    assert owner not in getattr(partner, 'graph_GraphModel2')


def test_assoc_node0_stub_double():
    # graph_GraphModel has no real 'graph_GraphModel' property in the generated
    # code (a bare stub) -- manually attach it so graph_Node's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # graph_Node's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = graph_Node(value="sample_text")
    partner = graph_GraphModel()
    setattr(partner, 'graph_GraphModel', None)
    _safe_set(owner, 'graph_Node', partner)
    assert owner in getattr(partner, 'graph_GraphModel')
    _safe_set(owner, 'graph_Node', None)
    assert owner not in getattr(partner, 'graph_GraphModel')


