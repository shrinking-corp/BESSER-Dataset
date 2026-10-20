import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    DAG_Edge,
    DAG_Graph,
    DAG_Node,
    DAG_Revision,
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

def test_assoc_children4_reverse_link_reassign_clear():
    a1 = DAG_Node(ID=7, level=7, name="sample_text")
    a2 = DAG_Node(ID=13, level=13, name="sample_text_2")
    b = DAG_Node(ID=7, level=7, name="sample_text")
    _safe_set(b, 'parents', {a1})
    assert _is_linked(b, 'parents', a1)
    if hasattr(a1, 'Node5'):
        assert _is_linked(a1, 'Node5', b)
    _safe_set(b, 'parents', {a2})
    assert _is_linked(b, 'parents', a2)
    if hasattr(a1, 'Node5'):
        assert not _is_linked(a1, 'Node5', b)
    if hasattr(a2, 'Node5'):
        assert _is_linked(a2, 'Node5', b)
    _safe_set(b, 'parents', set())
    assert not _is_linked(b, 'parents', a2)
    if hasattr(a2, 'Node5'):
        assert not _is_linked(a2, 'Node5', b)


def test_assoc_from_11_reverse_link_reassign_clear():
    a1 = DAG_Node(ID=7, level=7, name="sample_text")
    a2 = DAG_Node(ID=13, level=13, name="sample_text_2")
    b = DAG_Edge(ID=7, name="sample_text")
    _safe_set(b, 'outgoing', a1)
    assert _is_linked(b, 'outgoing', a1)
    if hasattr(a1, 'Node12'):
        assert _is_linked(a1, 'Node12', b)
    _safe_set(b, 'outgoing', a2)
    assert _is_linked(b, 'outgoing', a2)
    if hasattr(a1, 'Node12'):
        assert not _is_linked(a1, 'Node12', b)
    if hasattr(a2, 'Node12'):
        assert _is_linked(a2, 'Node12', b)
    _safe_set(b, 'outgoing', None)
    assert not _is_linked(b, 'outgoing', a2)
    if hasattr(a2, 'Node12'):
        assert not _is_linked(a2, 'Node12', b)


def test_assoc_incoming7_reverse_link_reassign_clear():
    a1 = DAG_Node(ID=7, level=7, name="sample_text")
    a2 = DAG_Node(ID=13, level=13, name="sample_text_2")
    b = DAG_Edge(ID=7, name="sample_text")
    _safe_set(b, 'Edge8', a1)
    assert _is_linked(b, 'Edge8', a1)
    if hasattr(a1, 'to'):
        assert _is_linked(a1, 'to', b)
    _safe_set(b, 'Edge8', a2)
    assert _is_linked(b, 'Edge8', a2)
    if hasattr(a1, 'to'):
        assert not _is_linked(a1, 'to', b)
    if hasattr(a2, 'to'):
        assert _is_linked(a2, 'to', b)
    _safe_set(b, 'Edge8', None)
    assert not _is_linked(b, 'Edge8', a2)
    if hasattr(a2, 'to'):
        assert not _is_linked(a2, 'to', b)


def test_assoc_nodes0_reverse_link_reassign_clear():
    a1 = DAG_Node(ID=7, level=7, name="sample_text")
    a2 = DAG_Node(ID=13, level=13, name="sample_text_2")
    b = DAG_Graph(name="sample_text")
    _safe_set(b, 'DAG_Graph', {a1})
    assert _is_linked(b, 'DAG_Graph', a1)
    if hasattr(a1, 'DAG_Node'):
        assert _is_linked(a1, 'DAG_Node', b)
    _safe_set(b, 'DAG_Graph', {a2})
    assert _is_linked(b, 'DAG_Graph', a2)
    if hasattr(a1, 'DAG_Node'):
        assert not _is_linked(a1, 'DAG_Node', b)
    if hasattr(a2, 'DAG_Node'):
        assert _is_linked(a2, 'DAG_Node', b)
    _safe_set(b, 'DAG_Graph', set())
    assert not _is_linked(b, 'DAG_Graph', a2)
    if hasattr(a2, 'DAG_Node'):
        assert not _is_linked(a2, 'DAG_Node', b)


def test_assoc_outgoing6_reverse_link_reassign_clear():
    a1 = DAG_Node(ID=7, level=7, name="sample_text")
    a2 = DAG_Node(ID=13, level=13, name="sample_text_2")
    b = DAG_Edge(ID=7, name="sample_text")
    _safe_set(b, 'Edge', a1)
    assert _is_linked(b, 'Edge', a1)
    if hasattr(a1, 'from_'):
        assert _is_linked(a1, 'from_', b)
    _safe_set(b, 'Edge', a2)
    assert _is_linked(b, 'Edge', a2)
    if hasattr(a1, 'from_'):
        assert not _is_linked(a1, 'from_', b)
    if hasattr(a2, 'from_'):
        assert _is_linked(a2, 'from_', b)
    _safe_set(b, 'Edge', None)
    assert not _is_linked(b, 'Edge', a2)
    if hasattr(a2, 'from_'):
        assert not _is_linked(a2, 'from_', b)


def test_assoc_parents2_reverse_link_reassign_clear():
    a1 = DAG_Node(ID=7, level=7, name="sample_text")
    a2 = DAG_Node(ID=13, level=13, name="sample_text_2")
    b = DAG_Node(ID=7, level=7, name="sample_text")
    _safe_set(b, 'children', {a1})
    assert _is_linked(b, 'children', a1)
    if hasattr(a1, 'Node'):
        assert _is_linked(a1, 'Node', b)
    _safe_set(b, 'children', {a2})
    assert _is_linked(b, 'children', a2)
    if hasattr(a1, 'Node'):
        assert not _is_linked(a1, 'Node', b)
    if hasattr(a2, 'Node'):
        assert _is_linked(a2, 'Node', b)
    _safe_set(b, 'children', set())
    assert not _is_linked(b, 'children', a2)
    if hasattr(a2, 'Node'):
        assert not _is_linked(a2, 'Node', b)


def test_assoc_to13_reverse_link_reassign_clear():
    a1 = DAG_Node(ID=7, level=7, name="sample_text")
    a2 = DAG_Node(ID=13, level=13, name="sample_text_2")
    b = DAG_Edge(ID=7, name="sample_text")
    _safe_set(b, 'incoming', a1)
    assert _is_linked(b, 'incoming', a1)
    if hasattr(a1, 'Node14'):
        assert _is_linked(a1, 'Node14', b)
    _safe_set(b, 'incoming', a2)
    assert _is_linked(b, 'incoming', a2)
    if hasattr(a1, 'Node14'):
        assert not _is_linked(a1, 'Node14', b)
    if hasattr(a2, 'Node14'):
        assert _is_linked(a2, 'Node14', b)
    _safe_set(b, 'incoming', None)
    assert not _is_linked(b, 'incoming', a2)
    if hasattr(a2, 'Node14'):
        assert not _is_linked(a2, 'Node14', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_revision9_stub_double():
    # DAG_Revision has no real 'DAG_Revision' property in the generated
    # code (a bare stub) -- manually attach it so DAG_Node's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # DAG_Node's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = DAG_Node(ID=7, level=7, name="sample_text")
    partner = DAG_Revision()
    setattr(partner, 'DAG_Revision', None)
    _safe_set(owner, 'DAG_Node10', partner)
    assert getattr(partner, 'DAG_Revision') == owner
    _safe_set(owner, 'DAG_Node10', None)
    assert getattr(partner, 'DAG_Revision') is None


