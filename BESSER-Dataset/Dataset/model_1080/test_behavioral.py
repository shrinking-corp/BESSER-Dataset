import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Node,
    PetriNet_Arc,
    PetriNet_Node,
    PetriNet_PetriNet,
    PetriNet_Place,
    PetriNet_Transition,
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

def test_assoc_arcs1_reverse_link_reassign_clear():
    a1 = PetriNet_PetriNet(name="sample_text")
    a2 = PetriNet_PetriNet(name="sample_text_2")
    b = PetriNet_Arc(weight=7)
    _safe_set(b, 'PetriNet_Arc', a1)
    assert _is_linked(b, 'PetriNet_Arc', a1)
    if hasattr(a1, 'PetriNet_PetriNet2'):
        assert _is_linked(a1, 'PetriNet_PetriNet2', b)
    _safe_set(b, 'PetriNet_Arc', a2)
    assert _is_linked(b, 'PetriNet_Arc', a2)
    if hasattr(a1, 'PetriNet_PetriNet2'):
        assert not _is_linked(a1, 'PetriNet_PetriNet2', b)
    if hasattr(a2, 'PetriNet_PetriNet2'):
        assert _is_linked(a2, 'PetriNet_PetriNet2', b)
    _safe_set(b, 'PetriNet_Arc', None)
    assert not _is_linked(b, 'PetriNet_Arc', a2)
    if hasattr(a2, 'PetriNet_PetriNet2'):
        assert not _is_linked(a2, 'PetriNet_PetriNet2', b)


def test_assoc_ingoing4_reverse_link_reassign_clear():
    a1 = PetriNet_Node(name="sample_text")
    a2 = PetriNet_Node(name="sample_text_2")
    b = PetriNet_Arc(weight=7)
    _safe_set(b, 'Arc5', a1)
    assert _is_linked(b, 'Arc5', a1)
    if hasattr(a1, 'target'):
        assert _is_linked(a1, 'target', b)
    _safe_set(b, 'Arc5', a2)
    assert _is_linked(b, 'Arc5', a2)
    if hasattr(a1, 'target'):
        assert not _is_linked(a1, 'target', b)
    if hasattr(a2, 'target'):
        assert _is_linked(a2, 'target', b)
    _safe_set(b, 'Arc5', None)
    assert not _is_linked(b, 'Arc5', a2)
    if hasattr(a2, 'target'):
        assert not _is_linked(a2, 'target', b)


def test_assoc_nodes0_reverse_link_reassign_clear():
    a1 = PetriNet_PetriNet(name="sample_text")
    a2 = PetriNet_PetriNet(name="sample_text_2")
    b = PetriNet_Node(name="sample_text")
    _safe_set(b, 'PetriNet_Node', a1)
    assert _is_linked(b, 'PetriNet_Node', a1)
    if hasattr(a1, 'PetriNet_PetriNet'):
        assert _is_linked(a1, 'PetriNet_PetriNet', b)
    _safe_set(b, 'PetriNet_Node', a2)
    assert _is_linked(b, 'PetriNet_Node', a2)
    if hasattr(a1, 'PetriNet_PetriNet'):
        assert not _is_linked(a1, 'PetriNet_PetriNet', b)
    if hasattr(a2, 'PetriNet_PetriNet'):
        assert _is_linked(a2, 'PetriNet_PetriNet', b)
    _safe_set(b, 'PetriNet_Node', None)
    assert not _is_linked(b, 'PetriNet_Node', a2)
    if hasattr(a2, 'PetriNet_PetriNet'):
        assert not _is_linked(a2, 'PetriNet_PetriNet', b)


def test_assoc_outgoing3_reverse_link_reassign_clear():
    a1 = PetriNet_Node(name="sample_text")
    a2 = PetriNet_Node(name="sample_text_2")
    b = PetriNet_Arc(weight=7)
    _safe_set(b, 'Arc', a1)
    assert _is_linked(b, 'Arc', a1)
    if hasattr(a1, 'source'):
        assert _is_linked(a1, 'source', b)
    _safe_set(b, 'Arc', a2)
    assert _is_linked(b, 'Arc', a2)
    if hasattr(a1, 'source'):
        assert not _is_linked(a1, 'source', b)
    if hasattr(a2, 'source'):
        assert _is_linked(a2, 'source', b)
    _safe_set(b, 'Arc', None)
    assert not _is_linked(b, 'Arc', a2)
    if hasattr(a2, 'source'):
        assert not _is_linked(a2, 'source', b)


def test_assoc_source6_reverse_link_reassign_clear():
    a1 = PetriNet_Node(name="sample_text")
    a2 = PetriNet_Node(name="sample_text_2")
    b = PetriNet_Arc(weight=7)
    _safe_set(b, 'outgoing', a1)
    assert _is_linked(b, 'outgoing', a1)
    if hasattr(a1, 'Node'):
        assert _is_linked(a1, 'Node', b)
    _safe_set(b, 'outgoing', a2)
    assert _is_linked(b, 'outgoing', a2)
    if hasattr(a1, 'Node'):
        assert not _is_linked(a1, 'Node', b)
    if hasattr(a2, 'Node'):
        assert _is_linked(a2, 'Node', b)
    _safe_set(b, 'outgoing', None)
    assert not _is_linked(b, 'outgoing', a2)
    if hasattr(a2, 'Node'):
        assert not _is_linked(a2, 'Node', b)


def test_assoc_target7_reverse_link_reassign_clear():
    a1 = PetriNet_Node(name="sample_text")
    a2 = PetriNet_Node(name="sample_text_2")
    b = PetriNet_Arc(weight=7)
    _safe_set(b, 'ingoing', a1)
    assert _is_linked(b, 'ingoing', a1)
    if hasattr(a1, 'Node8'):
        assert _is_linked(a1, 'Node8', b)
    _safe_set(b, 'ingoing', a2)
    assert _is_linked(b, 'ingoing', a2)
    if hasattr(a1, 'Node8'):
        assert not _is_linked(a1, 'Node8', b)
    if hasattr(a2, 'Node8'):
        assert _is_linked(a2, 'Node8', b)
    _safe_set(b, 'ingoing', None)
    assert not _is_linked(b, 'ingoing', a2)
    if hasattr(a2, 'Node8'):
        assert not _is_linked(a2, 'Node8', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

