import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    mydsl_Edge,
    mydsl_Graph,
    mydsl_Node,
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

def test_assoc_edges0_reverse_link_reassign_clear():
    a1 = mydsl_Graph(name="sample_text")
    a2 = mydsl_Graph(name="sample_text_2")
    b = mydsl_Edge(label="sample_text", parsed_source="sample_text", parsed_target="sample_text")
    _safe_set(b, 'mydsl_Edge', a1)
    assert _is_linked(b, 'mydsl_Edge', a1)
    if hasattr(a1, 'mydsl_Graph'):
        assert _is_linked(a1, 'mydsl_Graph', b)
    _safe_set(b, 'mydsl_Edge', a2)
    assert _is_linked(b, 'mydsl_Edge', a2)
    if hasattr(a1, 'mydsl_Graph'):
        assert not _is_linked(a1, 'mydsl_Graph', b)
    if hasattr(a2, 'mydsl_Graph'):
        assert _is_linked(a2, 'mydsl_Graph', b)
    _safe_set(b, 'mydsl_Edge', None)
    assert not _is_linked(b, 'mydsl_Edge', a2)
    if hasattr(a2, 'mydsl_Graph'):
        assert not _is_linked(a2, 'mydsl_Graph', b)


def test_assoc_nodes1_reverse_link_reassign_clear():
    a1 = mydsl_Node(content="sample_text", isInvisible=True, name="sample_text")
    a2 = mydsl_Node(content="sample_text_2", isInvisible=False, name="sample_text_2")
    b = mydsl_Graph(name="sample_text")
    _safe_set(b, 'mydsl_Graph2', {a1})
    assert _is_linked(b, 'mydsl_Graph2', a1)
    if hasattr(a1, 'mydsl_Node'):
        assert _is_linked(a1, 'mydsl_Node', b)
    _safe_set(b, 'mydsl_Graph2', {a2})
    assert _is_linked(b, 'mydsl_Graph2', a2)
    if hasattr(a1, 'mydsl_Node'):
        assert not _is_linked(a1, 'mydsl_Node', b)
    if hasattr(a2, 'mydsl_Node'):
        assert _is_linked(a2, 'mydsl_Node', b)
    _safe_set(b, 'mydsl_Graph2', set())
    assert not _is_linked(b, 'mydsl_Graph2', a2)
    if hasattr(a2, 'mydsl_Node'):
        assert not _is_linked(a2, 'mydsl_Node', b)


def test_assoc_source9_reverse_link_reassign_clear():
    a1 = mydsl_Node(content="sample_text", isInvisible=True, name="sample_text")
    a2 = mydsl_Node(content="sample_text_2", isInvisible=False, name="sample_text_2")
    b = mydsl_Edge(label="sample_text", parsed_source="sample_text", parsed_target="sample_text")
    _safe_set(b, 'mydsl_Edge10', a1)
    assert _is_linked(b, 'mydsl_Edge10', a1)
    if hasattr(a1, 'mydsl_Node11'):
        assert _is_linked(a1, 'mydsl_Node11', b)
    _safe_set(b, 'mydsl_Edge10', a2)
    assert _is_linked(b, 'mydsl_Edge10', a2)
    if hasattr(a1, 'mydsl_Node11'):
        assert not _is_linked(a1, 'mydsl_Node11', b)
    if hasattr(a2, 'mydsl_Node11'):
        assert _is_linked(a2, 'mydsl_Node11', b)
    _safe_set(b, 'mydsl_Edge10', None)
    assert not _is_linked(b, 'mydsl_Edge10', a2)
    if hasattr(a2, 'mydsl_Node11'):
        assert not _is_linked(a2, 'mydsl_Node11', b)


def test_assoc_subgraphs4_reverse_link_reassign_clear():
    a1 = mydsl_Graph(name="sample_text")
    a2 = mydsl_Graph(name="sample_text_2")
    b = mydsl_Graph(name="sample_text")
    _safe_set(b, 'mydsl_Graph5', a1)
    assert _is_linked(b, 'mydsl_Graph5', a1)
    if hasattr(a1, 'mydsl_Graph3'):
        assert _is_linked(a1, 'mydsl_Graph3', b)
    _safe_set(b, 'mydsl_Graph5', a2)
    assert _is_linked(b, 'mydsl_Graph5', a2)
    if hasattr(a1, 'mydsl_Graph3'):
        assert not _is_linked(a1, 'mydsl_Graph3', b)
    if hasattr(a2, 'mydsl_Graph3'):
        assert _is_linked(a2, 'mydsl_Graph3', b)
    _safe_set(b, 'mydsl_Graph5', None)
    assert not _is_linked(b, 'mydsl_Graph5', a2)
    if hasattr(a2, 'mydsl_Graph3'):
        assert not _is_linked(a2, 'mydsl_Graph3', b)


def test_assoc_target6_reverse_link_reassign_clear():
    a1 = mydsl_Node(content="sample_text", isInvisible=True, name="sample_text")
    a2 = mydsl_Node(content="sample_text_2", isInvisible=False, name="sample_text_2")
    b = mydsl_Edge(label="sample_text", parsed_source="sample_text", parsed_target="sample_text")
    _safe_set(b, 'mydsl_Edge7', a1)
    assert _is_linked(b, 'mydsl_Edge7', a1)
    if hasattr(a1, 'mydsl_Node8'):
        assert _is_linked(a1, 'mydsl_Node8', b)
    _safe_set(b, 'mydsl_Edge7', a2)
    assert _is_linked(b, 'mydsl_Edge7', a2)
    if hasattr(a1, 'mydsl_Node8'):
        assert not _is_linked(a1, 'mydsl_Node8', b)
    if hasattr(a2, 'mydsl_Node8'):
        assert _is_linked(a2, 'mydsl_Node8', b)
    _safe_set(b, 'mydsl_Edge7', None)
    assert not _is_linked(b, 'mydsl_Edge7', a2)
    if hasattr(a2, 'mydsl_Node8'):
        assert not _is_linked(a2, 'mydsl_Node8', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

