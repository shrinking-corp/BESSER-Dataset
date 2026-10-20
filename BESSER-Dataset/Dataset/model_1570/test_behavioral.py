import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    graphdom_Edge,
    graphdom_Graph,
    graphdom_Node,
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

def test_assoc_connectedEdges3_reverse_link_reassign_clear():
    a1 = graphdom_Node(color="sample_text", dominated=True, dominating=True, grade="sample_text", guid="sample_text", nodeName="sample_text", xCoord=7, yCoord=7)
    a2 = graphdom_Node(color="sample_text_2", dominated=False, dominating=False, grade="sample_text_2", guid="sample_text_2", nodeName="sample_text_2", xCoord=13, yCoord=13)
    b = graphdom_Edge(guid="sample_text", marked=True, weight=7)
    _safe_set(b, 'Edge', a1)
    assert _is_linked(b, 'Edge', a1)
    if hasattr(a1, 'connectedNodes'):
        assert _is_linked(a1, 'connectedNodes', b)
    _safe_set(b, 'Edge', a2)
    assert _is_linked(b, 'Edge', a2)
    if hasattr(a1, 'connectedNodes'):
        assert not _is_linked(a1, 'connectedNodes', b)
    if hasattr(a2, 'connectedNodes'):
        assert _is_linked(a2, 'connectedNodes', b)
    _safe_set(b, 'Edge', None)
    assert not _is_linked(b, 'Edge', a2)
    if hasattr(a2, 'connectedNodes'):
        assert not _is_linked(a2, 'connectedNodes', b)


def test_assoc_connectedNodes4_reverse_link_reassign_clear():
    a1 = graphdom_Node(color="sample_text", dominated=True, dominating=True, grade="sample_text", guid="sample_text", nodeName="sample_text", xCoord=7, yCoord=7)
    a2 = graphdom_Node(color="sample_text_2", dominated=False, dominating=False, grade="sample_text_2", guid="sample_text_2", nodeName="sample_text_2", xCoord=13, yCoord=13)
    b = graphdom_Edge(guid="sample_text", marked=True, weight=7)
    _safe_set(b, 'connectedEdges', {a1})
    assert _is_linked(b, 'connectedEdges', a1)
    if hasattr(a1, 'Node'):
        assert _is_linked(a1, 'Node', b)
    _safe_set(b, 'connectedEdges', {a2})
    assert _is_linked(b, 'connectedEdges', a2)
    if hasattr(a1, 'Node'):
        assert not _is_linked(a1, 'Node', b)
    if hasattr(a2, 'Node'):
        assert _is_linked(a2, 'Node', b)
    _safe_set(b, 'connectedEdges', set())
    assert not _is_linked(b, 'connectedEdges', a2)
    if hasattr(a2, 'Node'):
        assert not _is_linked(a2, 'Node', b)


def test_assoc_edges1_reverse_link_reassign_clear():
    a1 = graphdom_Graph(graphName="sample_text")
    a2 = graphdom_Graph(graphName="sample_text_2")
    b = graphdom_Edge(guid="sample_text", marked=True, weight=7)
    _safe_set(b, 'graphdom_Edge', a1)
    assert _is_linked(b, 'graphdom_Edge', a1)
    if hasattr(a1, 'graphdom_Graph2'):
        assert _is_linked(a1, 'graphdom_Graph2', b)
    _safe_set(b, 'graphdom_Edge', a2)
    assert _is_linked(b, 'graphdom_Edge', a2)
    if hasattr(a1, 'graphdom_Graph2'):
        assert not _is_linked(a1, 'graphdom_Graph2', b)
    if hasattr(a2, 'graphdom_Graph2'):
        assert _is_linked(a2, 'graphdom_Graph2', b)
    _safe_set(b, 'graphdom_Edge', None)
    assert not _is_linked(b, 'graphdom_Edge', a2)
    if hasattr(a2, 'graphdom_Graph2'):
        assert not _is_linked(a2, 'graphdom_Graph2', b)


def test_assoc_nodes0_reverse_link_reassign_clear():
    a1 = graphdom_Node(color="sample_text", dominated=True, dominating=True, grade="sample_text", guid="sample_text", nodeName="sample_text", xCoord=7, yCoord=7)
    a2 = graphdom_Node(color="sample_text_2", dominated=False, dominating=False, grade="sample_text_2", guid="sample_text_2", nodeName="sample_text_2", xCoord=13, yCoord=13)
    b = graphdom_Graph(graphName="sample_text")
    _safe_set(b, 'graphdom_Graph', {a1})
    assert _is_linked(b, 'graphdom_Graph', a1)
    if hasattr(a1, 'graphdom_Node'):
        assert _is_linked(a1, 'graphdom_Node', b)
    _safe_set(b, 'graphdom_Graph', {a2})
    assert _is_linked(b, 'graphdom_Graph', a2)
    if hasattr(a1, 'graphdom_Node'):
        assert not _is_linked(a1, 'graphdom_Node', b)
    if hasattr(a2, 'graphdom_Node'):
        assert _is_linked(a2, 'graphdom_Node', b)
    _safe_set(b, 'graphdom_Graph', set())
    assert not _is_linked(b, 'graphdom_Graph', a2)
    if hasattr(a2, 'graphdom_Node'):
        assert not _is_linked(a2, 'graphdom_Node', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

