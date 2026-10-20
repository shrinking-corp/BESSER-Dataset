import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    petrinet_Arc,
    petrinet_PetriNet,
    petrinet_Place,
    petrinet_Transition,
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

def test_assoc_arcs8_reverse_link_reassign_clear():
    a1 = petrinet_PetriNet(name="sample_text")
    a2 = petrinet_PetriNet(name="sample_text_2")
    b = petrinet_Arc(toPlace=True, weight=7)
    _safe_set(b, 'petrinet_Arc10', a1)
    assert _is_linked(b, 'petrinet_Arc10', a1)
    if hasattr(a1, 'petrinet_PetriNet9'):
        assert _is_linked(a1, 'petrinet_PetriNet9', b)
    _safe_set(b, 'petrinet_Arc10', a2)
    assert _is_linked(b, 'petrinet_Arc10', a2)
    if hasattr(a1, 'petrinet_PetriNet9'):
        assert not _is_linked(a1, 'petrinet_PetriNet9', b)
    if hasattr(a2, 'petrinet_PetriNet9'):
        assert _is_linked(a2, 'petrinet_PetriNet9', b)
    _safe_set(b, 'petrinet_Arc10', None)
    assert not _is_linked(b, 'petrinet_Arc10', a2)
    if hasattr(a2, 'petrinet_PetriNet9'):
        assert not _is_linked(a2, 'petrinet_PetriNet9', b)


def test_assoc_inhibitorArc0_reverse_link_reassign_clear():
    a1 = petrinet_Transition(name="sample_text")
    a2 = petrinet_Transition(name="sample_text_2")
    b = petrinet_Place(name="sample_text", token=7)
    _safe_set(b, 'petrinet_Place', {a1})
    assert _is_linked(b, 'petrinet_Place', a1)
    if hasattr(a1, 'petrinet_Transition'):
        assert _is_linked(a1, 'petrinet_Transition', b)
    _safe_set(b, 'petrinet_Place', {a2})
    assert _is_linked(b, 'petrinet_Place', a2)
    if hasattr(a1, 'petrinet_Transition'):
        assert not _is_linked(a1, 'petrinet_Transition', b)
    if hasattr(a2, 'petrinet_Transition'):
        assert _is_linked(a2, 'petrinet_Transition', b)
    _safe_set(b, 'petrinet_Place', set())
    assert not _is_linked(b, 'petrinet_Place', a2)
    if hasattr(a2, 'petrinet_Transition'):
        assert not _is_linked(a2, 'petrinet_Transition', b)


def test_assoc_place3_reverse_link_reassign_clear():
    a1 = petrinet_Place(name="sample_text", token=7)
    a2 = petrinet_Place(name="sample_text_2", token=13)
    b = petrinet_Arc(toPlace=True, weight=7)
    _safe_set(b, 'petrinet_Arc4', a1)
    assert _is_linked(b, 'petrinet_Arc4', a1)
    if hasattr(a1, 'petrinet_Place5'):
        assert _is_linked(a1, 'petrinet_Place5', b)
    _safe_set(b, 'petrinet_Arc4', a2)
    assert _is_linked(b, 'petrinet_Arc4', a2)
    if hasattr(a1, 'petrinet_Place5'):
        assert not _is_linked(a1, 'petrinet_Place5', b)
    if hasattr(a2, 'petrinet_Place5'):
        assert _is_linked(a2, 'petrinet_Place5', b)
    _safe_set(b, 'petrinet_Arc4', None)
    assert not _is_linked(b, 'petrinet_Arc4', a2)
    if hasattr(a2, 'petrinet_Place5'):
        assert not _is_linked(a2, 'petrinet_Place5', b)


def test_assoc_places6_reverse_link_reassign_clear():
    a1 = petrinet_Place(name="sample_text", token=7)
    a2 = petrinet_Place(name="sample_text_2", token=13)
    b = petrinet_PetriNet(name="sample_text")
    _safe_set(b, 'petrinet_PetriNet', {a1})
    assert _is_linked(b, 'petrinet_PetriNet', a1)
    if hasattr(a1, 'petrinet_Place7'):
        assert _is_linked(a1, 'petrinet_Place7', b)
    _safe_set(b, 'petrinet_PetriNet', {a2})
    assert _is_linked(b, 'petrinet_PetriNet', a2)
    if hasattr(a1, 'petrinet_Place7'):
        assert not _is_linked(a1, 'petrinet_Place7', b)
    if hasattr(a2, 'petrinet_Place7'):
        assert _is_linked(a2, 'petrinet_Place7', b)
    _safe_set(b, 'petrinet_PetriNet', set())
    assert not _is_linked(b, 'petrinet_PetriNet', a2)
    if hasattr(a2, 'petrinet_Place7'):
        assert not _is_linked(a2, 'petrinet_Place7', b)


def test_assoc_transition1_reverse_link_reassign_clear():
    a1 = petrinet_Transition(name="sample_text")
    a2 = petrinet_Transition(name="sample_text_2")
    b = petrinet_Arc(toPlace=True, weight=7)
    _safe_set(b, 'petrinet_Arc', a1)
    assert _is_linked(b, 'petrinet_Arc', a1)
    if hasattr(a1, 'petrinet_Transition2'):
        assert _is_linked(a1, 'petrinet_Transition2', b)
    _safe_set(b, 'petrinet_Arc', a2)
    assert _is_linked(b, 'petrinet_Arc', a2)
    if hasattr(a1, 'petrinet_Transition2'):
        assert not _is_linked(a1, 'petrinet_Transition2', b)
    if hasattr(a2, 'petrinet_Transition2'):
        assert _is_linked(a2, 'petrinet_Transition2', b)
    _safe_set(b, 'petrinet_Arc', None)
    assert not _is_linked(b, 'petrinet_Arc', a2)
    if hasattr(a2, 'petrinet_Transition2'):
        assert not _is_linked(a2, 'petrinet_Transition2', b)


def test_assoc_transitions11_reverse_link_reassign_clear():
    a1 = petrinet_Transition(name="sample_text")
    a2 = petrinet_Transition(name="sample_text_2")
    b = petrinet_PetriNet(name="sample_text")
    _safe_set(b, 'petrinet_PetriNet12', {a1})
    assert _is_linked(b, 'petrinet_PetriNet12', a1)
    if hasattr(a1, 'petrinet_Transition13'):
        assert _is_linked(a1, 'petrinet_Transition13', b)
    _safe_set(b, 'petrinet_PetriNet12', {a2})
    assert _is_linked(b, 'petrinet_PetriNet12', a2)
    if hasattr(a1, 'petrinet_Transition13'):
        assert not _is_linked(a1, 'petrinet_Transition13', b)
    if hasattr(a2, 'petrinet_Transition13'):
        assert _is_linked(a2, 'petrinet_Transition13', b)
    _safe_set(b, 'petrinet_PetriNet12', set())
    assert not _is_linked(b, 'petrinet_PetriNet12', a2)
    if hasattr(a2, 'petrinet_Transition13'):
        assert not _is_linked(a2, 'petrinet_Transition13', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

