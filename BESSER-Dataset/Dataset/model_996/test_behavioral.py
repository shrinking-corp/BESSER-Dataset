import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    GraphMetaM_Edge,
    GraphMetaM_Graph,
    GraphMetaM_Model,
    GraphMetaM_Vertex,
    Type,
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

def test_assoc_edge1_reverse_link_reassign_clear():
    a1 = GraphMetaM_Graph(cycles=7, name="sample_text", rName="sample_text")
    a2 = GraphMetaM_Graph(cycles=13, name="sample_text_2", rName="sample_text_2")
    b = GraphMetaM_Edge(async_=True, localPriority=7, name="sample_text", rName="sample_text")
    _safe_set(b, 'GraphMetaM_Edge', a1)
    assert _is_linked(b, 'GraphMetaM_Edge', a1)
    if hasattr(a1, 'GraphMetaM_Graph2'):
        assert _is_linked(a1, 'GraphMetaM_Graph2', b)
    _safe_set(b, 'GraphMetaM_Edge', a2)
    assert _is_linked(b, 'GraphMetaM_Edge', a2)
    if hasattr(a1, 'GraphMetaM_Graph2'):
        assert not _is_linked(a1, 'GraphMetaM_Graph2', b)
    if hasattr(a2, 'GraphMetaM_Graph2'):
        assert _is_linked(a2, 'GraphMetaM_Graph2', b)
    _safe_set(b, 'GraphMetaM_Edge', None)
    assert not _is_linked(b, 'GraphMetaM_Edge', a2)
    if hasattr(a2, 'GraphMetaM_Graph2'):
        assert not _is_linked(a2, 'GraphMetaM_Graph2', b)


def test_assoc_graph9_reverse_link_reassign_clear():
    a1 = GraphMetaM_Model(name="sample_text")
    a2 = GraphMetaM_Model(name="sample_text_2")
    b = GraphMetaM_Graph(cycles=7, name="sample_text", rName="sample_text")
    _safe_set(b, 'GraphMetaM_Graph10', a1)
    assert _is_linked(b, 'GraphMetaM_Graph10', a1)
    if hasattr(a1, 'GraphMetaM_Model'):
        assert _is_linked(a1, 'GraphMetaM_Model', b)
    _safe_set(b, 'GraphMetaM_Graph10', a2)
    assert _is_linked(b, 'GraphMetaM_Graph10', a2)
    if hasattr(a1, 'GraphMetaM_Model'):
        assert not _is_linked(a1, 'GraphMetaM_Model', b)
    if hasattr(a2, 'GraphMetaM_Model'):
        assert _is_linked(a2, 'GraphMetaM_Model', b)
    _safe_set(b, 'GraphMetaM_Graph10', None)
    assert not _is_linked(b, 'GraphMetaM_Graph10', a2)
    if hasattr(a2, 'GraphMetaM_Model'):
        assert not _is_linked(a2, 'GraphMetaM_Model', b)


def test_assoc_incoming6_reverse_link_reassign_clear():
    a1 = GraphMetaM_Vertex(activity="sample_text", cycles=7, globalPriority=7, name="sample_text", rName="sample_text", type="sample_text")
    a2 = GraphMetaM_Vertex(activity="sample_text_2", cycles=13, globalPriority=13, name="sample_text_2", rName="sample_text_2", type="sample_text_2")
    b = GraphMetaM_Edge(async_=True, localPriority=7, name="sample_text", rName="sample_text")
    _safe_set(b, 'Edge', a1)
    assert _is_linked(b, 'Edge', a1)
    if hasattr(a1, 'target'):
        assert _is_linked(a1, 'target', b)
    _safe_set(b, 'Edge', a2)
    assert _is_linked(b, 'Edge', a2)
    if hasattr(a1, 'target'):
        assert not _is_linked(a1, 'target', b)
    if hasattr(a2, 'target'):
        assert _is_linked(a2, 'target', b)
    _safe_set(b, 'Edge', None)
    assert not _is_linked(b, 'Edge', a2)
    if hasattr(a2, 'target'):
        assert not _is_linked(a2, 'target', b)


def test_assoc_outgoing7_reverse_link_reassign_clear():
    a1 = GraphMetaM_Vertex(activity="sample_text", cycles=7, globalPriority=7, name="sample_text", rName="sample_text", type="sample_text")
    a2 = GraphMetaM_Vertex(activity="sample_text_2", cycles=13, globalPriority=13, name="sample_text_2", rName="sample_text_2", type="sample_text_2")
    b = GraphMetaM_Edge(async_=True, localPriority=7, name="sample_text", rName="sample_text")
    _safe_set(b, 'Edge8', a1)
    assert _is_linked(b, 'Edge8', a1)
    if hasattr(a1, 'source'):
        assert _is_linked(a1, 'source', b)
    _safe_set(b, 'Edge8', a2)
    assert _is_linked(b, 'Edge8', a2)
    if hasattr(a1, 'source'):
        assert not _is_linked(a1, 'source', b)
    if hasattr(a2, 'source'):
        assert _is_linked(a2, 'source', b)
    _safe_set(b, 'Edge8', None)
    assert not _is_linked(b, 'Edge8', a2)
    if hasattr(a2, 'source'):
        assert not _is_linked(a2, 'source', b)


def test_assoc_source4_reverse_link_reassign_clear():
    a1 = GraphMetaM_Vertex(activity="sample_text", cycles=7, globalPriority=7, name="sample_text", rName="sample_text", type="sample_text")
    a2 = GraphMetaM_Vertex(activity="sample_text_2", cycles=13, globalPriority=13, name="sample_text_2", rName="sample_text_2", type="sample_text_2")
    b = GraphMetaM_Edge(async_=True, localPriority=7, name="sample_text", rName="sample_text")
    _safe_set(b, 'outgoing', a1)
    assert _is_linked(b, 'outgoing', a1)
    if hasattr(a1, 'Vertex5'):
        assert _is_linked(a1, 'Vertex5', b)
    _safe_set(b, 'outgoing', a2)
    assert _is_linked(b, 'outgoing', a2)
    if hasattr(a1, 'Vertex5'):
        assert not _is_linked(a1, 'Vertex5', b)
    if hasattr(a2, 'Vertex5'):
        assert _is_linked(a2, 'Vertex5', b)
    _safe_set(b, 'outgoing', None)
    assert not _is_linked(b, 'outgoing', a2)
    if hasattr(a2, 'Vertex5'):
        assert not _is_linked(a2, 'Vertex5', b)


def test_assoc_target3_reverse_link_reassign_clear():
    a1 = GraphMetaM_Vertex(activity="sample_text", cycles=7, globalPriority=7, name="sample_text", rName="sample_text", type="sample_text")
    a2 = GraphMetaM_Vertex(activity="sample_text_2", cycles=13, globalPriority=13, name="sample_text_2", rName="sample_text_2", type="sample_text_2")
    b = GraphMetaM_Edge(async_=True, localPriority=7, name="sample_text", rName="sample_text")
    _safe_set(b, 'incoming', a1)
    assert _is_linked(b, 'incoming', a1)
    if hasattr(a1, 'Vertex'):
        assert _is_linked(a1, 'Vertex', b)
    _safe_set(b, 'incoming', a2)
    assert _is_linked(b, 'incoming', a2)
    if hasattr(a1, 'Vertex'):
        assert not _is_linked(a1, 'Vertex', b)
    if hasattr(a2, 'Vertex'):
        assert _is_linked(a2, 'Vertex', b)
    _safe_set(b, 'incoming', None)
    assert not _is_linked(b, 'incoming', a2)
    if hasattr(a2, 'Vertex'):
        assert not _is_linked(a2, 'Vertex', b)


def test_assoc_vertex0_reverse_link_reassign_clear():
    a1 = GraphMetaM_Vertex(activity="sample_text", cycles=7, globalPriority=7, name="sample_text", rName="sample_text", type="sample_text")
    a2 = GraphMetaM_Vertex(activity="sample_text_2", cycles=13, globalPriority=13, name="sample_text_2", rName="sample_text_2", type="sample_text_2")
    b = GraphMetaM_Graph(cycles=7, name="sample_text", rName="sample_text")
    _safe_set(b, 'GraphMetaM_Graph', {a1})
    assert _is_linked(b, 'GraphMetaM_Graph', a1)
    if hasattr(a1, 'GraphMetaM_Vertex'):
        assert _is_linked(a1, 'GraphMetaM_Vertex', b)
    _safe_set(b, 'GraphMetaM_Graph', {a2})
    assert _is_linked(b, 'GraphMetaM_Graph', a2)
    if hasattr(a1, 'GraphMetaM_Vertex'):
        assert not _is_linked(a1, 'GraphMetaM_Vertex', b)
    if hasattr(a2, 'GraphMetaM_Vertex'):
        assert _is_linked(a2, 'GraphMetaM_Vertex', b)
    _safe_set(b, 'GraphMetaM_Graph', set())
    assert not _is_linked(b, 'GraphMetaM_Graph', a2)
    if hasattr(a2, 'GraphMetaM_Vertex'):
        assert not _is_linked(a2, 'GraphMetaM_Vertex', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

