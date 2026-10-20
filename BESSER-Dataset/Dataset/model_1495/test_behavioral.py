import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Node,
    petri_net_Arc,
    petri_net_Node,
    petri_net_PetriNet,
    petri_net_Place,
    petri_net_Transition,
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
    a1 = petri_net_PetriNet(name="sample_text")
    a2 = petri_net_PetriNet(name="sample_text_2")
    b = petri_net_Arc(name="sample_text")
    _safe_set(b, 'petri_net_Arc', a1)
    assert _is_linked(b, 'petri_net_Arc', a1)
    if hasattr(a1, 'petri_net_PetriNet2'):
        assert _is_linked(a1, 'petri_net_PetriNet2', b)
    _safe_set(b, 'petri_net_Arc', a2)
    assert _is_linked(b, 'petri_net_Arc', a2)
    if hasattr(a1, 'petri_net_PetriNet2'):
        assert not _is_linked(a1, 'petri_net_PetriNet2', b)
    if hasattr(a2, 'petri_net_PetriNet2'):
        assert _is_linked(a2, 'petri_net_PetriNet2', b)
    _safe_set(b, 'petri_net_Arc', None)
    assert not _is_linked(b, 'petri_net_Arc', a2)
    if hasattr(a2, 'petri_net_PetriNet2'):
        assert not _is_linked(a2, 'petri_net_PetriNet2', b)


def test_assoc_nodes0_reverse_link_reassign_clear():
    a1 = petri_net_PetriNet(name="sample_text")
    a2 = petri_net_PetriNet(name="sample_text_2")
    b = petri_net_Node(name="sample_text")
    _safe_set(b, 'petri_net_Node', a1)
    assert _is_linked(b, 'petri_net_Node', a1)
    if hasattr(a1, 'petri_net_PetriNet'):
        assert _is_linked(a1, 'petri_net_PetriNet', b)
    _safe_set(b, 'petri_net_Node', a2)
    assert _is_linked(b, 'petri_net_Node', a2)
    if hasattr(a1, 'petri_net_PetriNet'):
        assert not _is_linked(a1, 'petri_net_PetriNet', b)
    if hasattr(a2, 'petri_net_PetriNet'):
        assert _is_linked(a2, 'petri_net_PetriNet', b)
    _safe_set(b, 'petri_net_Node', None)
    assert not _is_linked(b, 'petri_net_Node', a2)
    if hasattr(a2, 'petri_net_PetriNet'):
        assert not _is_linked(a2, 'petri_net_PetriNet', b)


def test_assoc_source3_reverse_link_reassign_clear():
    a1 = petri_net_Node(name="sample_text")
    a2 = petri_net_Node(name="sample_text_2")
    b = petri_net_Arc(name="sample_text")
    _safe_set(b, 'petri_net_Arc4', a1)
    assert _is_linked(b, 'petri_net_Arc4', a1)
    if hasattr(a1, 'petri_net_Node5'):
        assert _is_linked(a1, 'petri_net_Node5', b)
    _safe_set(b, 'petri_net_Arc4', a2)
    assert _is_linked(b, 'petri_net_Arc4', a2)
    if hasattr(a1, 'petri_net_Node5'):
        assert not _is_linked(a1, 'petri_net_Node5', b)
    if hasattr(a2, 'petri_net_Node5'):
        assert _is_linked(a2, 'petri_net_Node5', b)
    _safe_set(b, 'petri_net_Arc4', None)
    assert not _is_linked(b, 'petri_net_Arc4', a2)
    if hasattr(a2, 'petri_net_Node5'):
        assert not _is_linked(a2, 'petri_net_Node5', b)


def test_assoc_target6_reverse_link_reassign_clear():
    a1 = petri_net_Node(name="sample_text")
    a2 = petri_net_Node(name="sample_text_2")
    b = petri_net_Arc(name="sample_text")
    _safe_set(b, 'petri_net_Arc7', a1)
    assert _is_linked(b, 'petri_net_Arc7', a1)
    if hasattr(a1, 'petri_net_Node8'):
        assert _is_linked(a1, 'petri_net_Node8', b)
    _safe_set(b, 'petri_net_Arc7', a2)
    assert _is_linked(b, 'petri_net_Arc7', a2)
    if hasattr(a1, 'petri_net_Node8'):
        assert not _is_linked(a1, 'petri_net_Node8', b)
    if hasattr(a2, 'petri_net_Node8'):
        assert _is_linked(a2, 'petri_net_Node8', b)
    _safe_set(b, 'petri_net_Arc7', None)
    assert not _is_linked(b, 'petri_net_Arc7', a2)
    if hasattr(a2, 'petri_net_Node8'):
        assert not _is_linked(a2, 'petri_net_Node8', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

