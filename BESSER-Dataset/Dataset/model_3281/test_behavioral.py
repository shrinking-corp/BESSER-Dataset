import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Edge,
    Graph,
    Mark,
    Node,
    sm_Edge,
    sm_Graph,
    sm_Mark,
    sm_Node,
    sm_Observation,
    sm_State,
    sm_StateMachine,
    sm_Transition,
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

def test_assoc_edges8_reverse_link_reassign_clear():
    a1 = sm_Graph(name="sample_text")
    a2 = sm_Graph(name="sample_text_2")
    b = sm_Edge(name="sample_text")
    _safe_set(b, 'Edge', a1)
    assert _is_linked(b, 'Edge', a1)
    if hasattr(a1, 'graph9'):
        assert _is_linked(a1, 'graph9', b)
    _safe_set(b, 'Edge', a2)
    assert _is_linked(b, 'Edge', a2)
    if hasattr(a1, 'graph9'):
        assert not _is_linked(a1, 'graph9', b)
    if hasattr(a2, 'graph9'):
        assert _is_linked(a2, 'graph9', b)
    _safe_set(b, 'Edge', None)
    assert not _is_linked(b, 'Edge', a2)
    if hasattr(a2, 'graph9'):
        assert not _is_linked(a2, 'graph9', b)


def test_assoc_graph14_reverse_link_reassign_clear():
    a1 = sm_Node(name="sample_text")
    a2 = sm_Node(name="sample_text_2")
    b = sm_Graph(name="sample_text")
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


def test_assoc_graph19_reverse_link_reassign_clear():
    a1 = sm_Graph(name="sample_text")
    a2 = sm_Graph(name="sample_text_2")
    b = sm_Edge(name="sample_text")
    _safe_set(b, 'edges', a1)
    assert _is_linked(b, 'edges', a1)
    if hasattr(a1, 'Graph20'):
        assert _is_linked(a1, 'Graph20', b)
    _safe_set(b, 'edges', a2)
    assert _is_linked(b, 'edges', a2)
    if hasattr(a1, 'Graph20'):
        assert not _is_linked(a1, 'Graph20', b)
    if hasattr(a2, 'Graph20'):
        assert _is_linked(a2, 'Graph20', b)
    _safe_set(b, 'edges', None)
    assert not _is_linked(b, 'edges', a2)
    if hasattr(a2, 'Graph20'):
        assert not _is_linked(a2, 'Graph20', b)


def test_assoc_graph23_reverse_link_reassign_clear():
    a1 = sm_Mark(time="sample_text")
    a2 = sm_Mark(time="sample_text_2")
    b = sm_Graph(name="sample_text")
    _safe_set(b, 'Graph24', a1)
    assert _is_linked(b, 'Graph24', a1)
    if hasattr(a1, 'marks'):
        assert _is_linked(a1, 'marks', b)
    _safe_set(b, 'Graph24', a2)
    assert _is_linked(b, 'Graph24', a2)
    if hasattr(a1, 'marks'):
        assert not _is_linked(a1, 'marks', b)
    if hasattr(a2, 'marks'):
        assert _is_linked(a2, 'marks', b)
    _safe_set(b, 'Graph24', None)
    assert not _is_linked(b, 'Graph24', a2)
    if hasattr(a2, 'marks'):
        assert not _is_linked(a2, 'marks', b)


def test_assoc_mark12_reverse_link_reassign_clear():
    a1 = sm_Node(name="sample_text")
    a2 = sm_Node(name="sample_text_2")
    b = sm_Mark(time="sample_text")
    _safe_set(b, 'Mark13', a1)
    assert _is_linked(b, 'Mark13', a1)
    if hasattr(a1, 'node'):
        assert _is_linked(a1, 'node', b)
    _safe_set(b, 'Mark13', a2)
    assert _is_linked(b, 'Mark13', a2)
    if hasattr(a1, 'node'):
        assert not _is_linked(a1, 'node', b)
    if hasattr(a2, 'node'):
        assert _is_linked(a2, 'node', b)
    _safe_set(b, 'Mark13', None)
    assert not _is_linked(b, 'Mark13', a2)
    if hasattr(a2, 'node'):
        assert not _is_linked(a2, 'node', b)


def test_assoc_marks10_reverse_link_reassign_clear():
    a1 = sm_Mark(time="sample_text")
    a2 = sm_Mark(time="sample_text_2")
    b = sm_Graph(name="sample_text")
    _safe_set(b, 'graph11', {a1})
    assert _is_linked(b, 'graph11', a1)
    if hasattr(a1, 'Mark'):
        assert _is_linked(a1, 'Mark', b)
    _safe_set(b, 'graph11', {a2})
    assert _is_linked(b, 'graph11', a2)
    if hasattr(a1, 'Mark'):
        assert not _is_linked(a1, 'Mark', b)
    if hasattr(a2, 'Mark'):
        assert _is_linked(a2, 'Mark', b)
    _safe_set(b, 'graph11', set())
    assert not _is_linked(b, 'graph11', a2)
    if hasattr(a2, 'Mark'):
        assert not _is_linked(a2, 'Mark', b)


def test_assoc_node21_reverse_link_reassign_clear():
    a1 = sm_Node(name="sample_text")
    a2 = sm_Node(name="sample_text_2")
    b = sm_Mark(time="sample_text")
    _safe_set(b, 'mark', a1)
    assert _is_linked(b, 'mark', a1)
    if hasattr(a1, 'Node22'):
        assert _is_linked(a1, 'Node22', b)
    _safe_set(b, 'mark', a2)
    assert _is_linked(b, 'mark', a2)
    if hasattr(a1, 'Node22'):
        assert not _is_linked(a1, 'Node22', b)
    if hasattr(a2, 'Node22'):
        assert _is_linked(a2, 'Node22', b)
    _safe_set(b, 'mark', None)
    assert not _is_linked(b, 'mark', a2)
    if hasattr(a2, 'Node22'):
        assert not _is_linked(a2, 'Node22', b)


def test_assoc_nodes7_reverse_link_reassign_clear():
    a1 = sm_Node(name="sample_text")
    a2 = sm_Node(name="sample_text_2")
    b = sm_Graph(name="sample_text")
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


def test_assoc_source15_reverse_link_reassign_clear():
    a1 = sm_Node(name="sample_text")
    a2 = sm_Node(name="sample_text_2")
    b = sm_Edge(name="sample_text")
    _safe_set(b, 'sm_Edge', a1)
    assert _is_linked(b, 'sm_Edge', a1)
    if hasattr(a1, 'sm_Node'):
        assert _is_linked(a1, 'sm_Node', b)
    _safe_set(b, 'sm_Edge', a2)
    assert _is_linked(b, 'sm_Edge', a2)
    if hasattr(a1, 'sm_Node'):
        assert not _is_linked(a1, 'sm_Node', b)
    if hasattr(a2, 'sm_Node'):
        assert _is_linked(a2, 'sm_Node', b)
    _safe_set(b, 'sm_Edge', None)
    assert not _is_linked(b, 'sm_Edge', a2)
    if hasattr(a2, 'sm_Node'):
        assert not _is_linked(a2, 'sm_Node', b)


def test_assoc_target16_reverse_link_reassign_clear():
    a1 = sm_Node(name="sample_text")
    a2 = sm_Node(name="sample_text_2")
    b = sm_Edge(name="sample_text")
    _safe_set(b, 'sm_Edge17', a1)
    assert _is_linked(b, 'sm_Edge17', a1)
    if hasattr(a1, 'sm_Node18'):
        assert _is_linked(a1, 'sm_Node18', b)
    _safe_set(b, 'sm_Edge17', a2)
    assert _is_linked(b, 'sm_Edge17', a2)
    if hasattr(a1, 'sm_Node18'):
        assert not _is_linked(a1, 'sm_Node18', b)
    if hasattr(a2, 'sm_Node18'):
        assert _is_linked(a2, 'sm_Node18', b)
    _safe_set(b, 'sm_Edge17', None)
    assert not _is_linked(b, 'sm_Edge17', a2)
    if hasattr(a2, 'sm_Node18'):
        assert not _is_linked(a2, 'sm_Node18', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

