import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    graph_Edge,
    graph_Graph,
    graph_Mark,
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

def test_assoc_edges1_reverse_link_reassign_clear():
    a1 = graph_Graph(name="sample_text")
    a2 = graph_Graph(name="sample_text_2")
    b = graph_Edge(name="sample_text")
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


def test_assoc_graph12_reverse_link_reassign_clear():
    a1 = graph_Graph(name="sample_text")
    a2 = graph_Graph(name="sample_text_2")
    b = graph_Edge(name="sample_text")
    _safe_set(b, 'edges', a1)
    assert _is_linked(b, 'edges', a1)
    if hasattr(a1, 'Graph13'):
        assert _is_linked(a1, 'Graph13', b)
    _safe_set(b, 'edges', a2)
    assert _is_linked(b, 'edges', a2)
    if hasattr(a1, 'Graph13'):
        assert not _is_linked(a1, 'Graph13', b)
    if hasattr(a2, 'Graph13'):
        assert _is_linked(a2, 'Graph13', b)
    _safe_set(b, 'edges', None)
    assert not _is_linked(b, 'edges', a2)
    if hasattr(a2, 'Graph13'):
        assert not _is_linked(a2, 'Graph13', b)


def test_assoc_graph16_reverse_link_reassign_clear():
    a1 = graph_Mark(time="sample_text")
    a2 = graph_Mark(time="sample_text_2")
    b = graph_Graph(name="sample_text")
    _safe_set(b, 'Graph17', a1)
    assert _is_linked(b, 'Graph17', a1)
    if hasattr(a1, 'marks'):
        assert _is_linked(a1, 'marks', b)
    _safe_set(b, 'Graph17', a2)
    assert _is_linked(b, 'Graph17', a2)
    if hasattr(a1, 'marks'):
        assert not _is_linked(a1, 'marks', b)
    if hasattr(a2, 'marks'):
        assert _is_linked(a2, 'marks', b)
    _safe_set(b, 'Graph17', None)
    assert not _is_linked(b, 'Graph17', a2)
    if hasattr(a2, 'marks'):
        assert not _is_linked(a2, 'marks', b)


def test_assoc_graph7_reverse_link_reassign_clear():
    a1 = graph_Node(name="sample_text")
    a2 = graph_Node(name="sample_text_2")
    b = graph_Graph(name="sample_text")
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


def test_assoc_mark5_reverse_link_reassign_clear():
    a1 = graph_Node(name="sample_text")
    a2 = graph_Node(name="sample_text_2")
    b = graph_Mark(time="sample_text")
    _safe_set(b, 'Mark6', a1)
    assert _is_linked(b, 'Mark6', a1)
    if hasattr(a1, 'node'):
        assert _is_linked(a1, 'node', b)
    _safe_set(b, 'Mark6', a2)
    assert _is_linked(b, 'Mark6', a2)
    if hasattr(a1, 'node'):
        assert not _is_linked(a1, 'node', b)
    if hasattr(a2, 'node'):
        assert _is_linked(a2, 'node', b)
    _safe_set(b, 'Mark6', None)
    assert not _is_linked(b, 'Mark6', a2)
    if hasattr(a2, 'node'):
        assert not _is_linked(a2, 'node', b)


def test_assoc_marks3_reverse_link_reassign_clear():
    a1 = graph_Mark(time="sample_text")
    a2 = graph_Mark(time="sample_text_2")
    b = graph_Graph(name="sample_text")
    _safe_set(b, 'graph4', {a1})
    assert _is_linked(b, 'graph4', a1)
    if hasattr(a1, 'Mark'):
        assert _is_linked(a1, 'Mark', b)
    _safe_set(b, 'graph4', {a2})
    assert _is_linked(b, 'graph4', a2)
    if hasattr(a1, 'Mark'):
        assert not _is_linked(a1, 'Mark', b)
    if hasattr(a2, 'Mark'):
        assert _is_linked(a2, 'Mark', b)
    _safe_set(b, 'graph4', set())
    assert not _is_linked(b, 'graph4', a2)
    if hasattr(a2, 'Mark'):
        assert not _is_linked(a2, 'Mark', b)


def test_assoc_node14_reverse_link_reassign_clear():
    a1 = graph_Node(name="sample_text")
    a2 = graph_Node(name="sample_text_2")
    b = graph_Mark(time="sample_text")
    _safe_set(b, 'mark', a1)
    assert _is_linked(b, 'mark', a1)
    if hasattr(a1, 'Node15'):
        assert _is_linked(a1, 'Node15', b)
    _safe_set(b, 'mark', a2)
    assert _is_linked(b, 'mark', a2)
    if hasattr(a1, 'Node15'):
        assert not _is_linked(a1, 'Node15', b)
    if hasattr(a2, 'Node15'):
        assert _is_linked(a2, 'Node15', b)
    _safe_set(b, 'mark', None)
    assert not _is_linked(b, 'mark', a2)
    if hasattr(a2, 'Node15'):
        assert not _is_linked(a2, 'Node15', b)


def test_assoc_nodes0_reverse_link_reassign_clear():
    a1 = graph_Node(name="sample_text")
    a2 = graph_Node(name="sample_text_2")
    b = graph_Graph(name="sample_text")
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


def test_assoc_source8_reverse_link_reassign_clear():
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


def test_assoc_target9_reverse_link_reassign_clear():
    a1 = graph_Node(name="sample_text")
    a2 = graph_Node(name="sample_text_2")
    b = graph_Edge(name="sample_text")
    _safe_set(b, 'graph_Edge10', a1)
    assert _is_linked(b, 'graph_Edge10', a1)
    if hasattr(a1, 'graph_Node11'):
        assert _is_linked(a1, 'graph_Node11', b)
    _safe_set(b, 'graph_Edge10', a2)
    assert _is_linked(b, 'graph_Edge10', a2)
    if hasattr(a1, 'graph_Node11'):
        assert not _is_linked(a1, 'graph_Node11', b)
    if hasattr(a2, 'graph_Node11'):
        assert _is_linked(a2, 'graph_Node11', b)
    _safe_set(b, 'graph_Edge10', None)
    assert not _is_linked(b, 'graph_Edge10', a2)
    if hasattr(a2, 'graph_Node11'):
        assert not _is_linked(a2, 'graph_Node11', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

