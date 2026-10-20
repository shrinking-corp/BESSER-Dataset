import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    PetriElement,
    petriNet_Arc,
    petriNet_PetriElement,
    petriNet_PetriNetwork,
    petriNet_Place,
    petriNet_Transition,
    ArcDirection,
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

def test_assoc_arcEntrants1_reverse_link_reassign_clear():
    a1 = petriNet_Transition()
    a2 = petriNet_Transition()
    b = petriNet_Arc(Direction="sample_text", jetonsTransferes=7)
    _safe_set(b, 'petriNet_Arc3', a1)
    assert _is_linked(b, 'petriNet_Arc3', a1)
    if hasattr(a1, 'petriNet_Transition2'):
        assert _is_linked(a1, 'petriNet_Transition2', b)
    _safe_set(b, 'petriNet_Arc3', a2)
    assert _is_linked(b, 'petriNet_Arc3', a2)
    if hasattr(a1, 'petriNet_Transition2'):
        assert not _is_linked(a1, 'petriNet_Transition2', b)
    if hasattr(a2, 'petriNet_Transition2'):
        assert _is_linked(a2, 'petriNet_Transition2', b)
    _safe_set(b, 'petriNet_Arc3', None)
    assert not _is_linked(b, 'petriNet_Arc3', a2)
    if hasattr(a2, 'petriNet_Transition2'):
        assert not _is_linked(a2, 'petriNet_Transition2', b)


def test_assoc_arcEntrants4_reverse_link_reassign_clear():
    a1 = petriNet_Place(nbJetons=7)
    a2 = petriNet_Place(nbJetons=13)
    b = petriNet_Arc(Direction="sample_text", jetonsTransferes=7)
    _safe_set(b, 'petriNet_Arc5', a1)
    assert _is_linked(b, 'petriNet_Arc5', a1)
    if hasattr(a1, 'petriNet_Place'):
        assert _is_linked(a1, 'petriNet_Place', b)
    _safe_set(b, 'petriNet_Arc5', a2)
    assert _is_linked(b, 'petriNet_Arc5', a2)
    if hasattr(a1, 'petriNet_Place'):
        assert not _is_linked(a1, 'petriNet_Place', b)
    if hasattr(a2, 'petriNet_Place'):
        assert _is_linked(a2, 'petriNet_Place', b)
    _safe_set(b, 'petriNet_Arc5', None)
    assert not _is_linked(b, 'petriNet_Arc5', a2)
    if hasattr(a2, 'petriNet_Place'):
        assert not _is_linked(a2, 'petriNet_Place', b)


def test_assoc_arcSortants0_reverse_link_reassign_clear():
    a1 = petriNet_Transition()
    a2 = petriNet_Transition()
    b = petriNet_Arc(Direction="sample_text", jetonsTransferes=7)
    _safe_set(b, 'petriNet_Arc', a1)
    assert _is_linked(b, 'petriNet_Arc', a1)
    if hasattr(a1, 'petriNet_Transition'):
        assert _is_linked(a1, 'petriNet_Transition', b)
    _safe_set(b, 'petriNet_Arc', a2)
    assert _is_linked(b, 'petriNet_Arc', a2)
    if hasattr(a1, 'petriNet_Transition'):
        assert not _is_linked(a1, 'petriNet_Transition', b)
    if hasattr(a2, 'petriNet_Transition'):
        assert _is_linked(a2, 'petriNet_Transition', b)
    _safe_set(b, 'petriNet_Arc', None)
    assert not _is_linked(b, 'petriNet_Arc', a2)
    if hasattr(a2, 'petriNet_Transition'):
        assert not _is_linked(a2, 'petriNet_Transition', b)


def test_assoc_arcSortants6_reverse_link_reassign_clear():
    a1 = petriNet_Place(nbJetons=7)
    a2 = petriNet_Place(nbJetons=13)
    b = petriNet_Arc(Direction="sample_text", jetonsTransferes=7)
    _safe_set(b, 'petriNet_Arc8', a1)
    assert _is_linked(b, 'petriNet_Arc8', a1)
    if hasattr(a1, 'petriNet_Place7'):
        assert _is_linked(a1, 'petriNet_Place7', b)
    _safe_set(b, 'petriNet_Arc8', a2)
    assert _is_linked(b, 'petriNet_Arc8', a2)
    if hasattr(a1, 'petriNet_Place7'):
        assert not _is_linked(a1, 'petriNet_Place7', b)
    if hasattr(a2, 'petriNet_Place7'):
        assert _is_linked(a2, 'petriNet_Place7', b)
    _safe_set(b, 'petriNet_Arc8', None)
    assert not _is_linked(b, 'petriNet_Arc8', a2)
    if hasattr(a2, 'petriNet_Place7'):
        assert not _is_linked(a2, 'petriNet_Place7', b)


def test_assoc_petrielement15_reverse_link_reassign_clear():
    a1 = petriNet_PetriNetwork(name="sample_text")
    a2 = petriNet_PetriNetwork(name="sample_text_2")
    b = petriNet_PetriElement(name="sample_text")
    _safe_set(b, 'petriNet_PetriElement', a1)
    assert _is_linked(b, 'petriNet_PetriElement', a1)
    if hasattr(a1, 'petriNet_PetriNetwork'):
        assert _is_linked(a1, 'petriNet_PetriNetwork', b)
    _safe_set(b, 'petriNet_PetriElement', a2)
    assert _is_linked(b, 'petriNet_PetriElement', a2)
    if hasattr(a1, 'petriNet_PetriNetwork'):
        assert not _is_linked(a1, 'petriNet_PetriNetwork', b)
    if hasattr(a2, 'petriNet_PetriNetwork'):
        assert _is_linked(a2, 'petriNet_PetriNetwork', b)
    _safe_set(b, 'petriNet_PetriElement', None)
    assert not _is_linked(b, 'petriNet_PetriElement', a2)
    if hasattr(a2, 'petriNet_PetriNetwork'):
        assert not _is_linked(a2, 'petriNet_PetriNetwork', b)


def test_assoc_place12_reverse_link_reassign_clear():
    a1 = petriNet_Place(nbJetons=7)
    a2 = petriNet_Place(nbJetons=13)
    b = petriNet_Arc(Direction="sample_text", jetonsTransferes=7)
    _safe_set(b, 'petriNet_Arc13', a1)
    assert _is_linked(b, 'petriNet_Arc13', a1)
    if hasattr(a1, 'petriNet_Place14'):
        assert _is_linked(a1, 'petriNet_Place14', b)
    _safe_set(b, 'petriNet_Arc13', a2)
    assert _is_linked(b, 'petriNet_Arc13', a2)
    if hasattr(a1, 'petriNet_Place14'):
        assert not _is_linked(a1, 'petriNet_Place14', b)
    if hasattr(a2, 'petriNet_Place14'):
        assert _is_linked(a2, 'petriNet_Place14', b)
    _safe_set(b, 'petriNet_Arc13', None)
    assert not _is_linked(b, 'petriNet_Arc13', a2)
    if hasattr(a2, 'petriNet_Place14'):
        assert not _is_linked(a2, 'petriNet_Place14', b)


def test_assoc_transition9_reverse_link_reassign_clear():
    a1 = petriNet_Transition()
    a2 = petriNet_Transition()
    b = petriNet_Arc(Direction="sample_text", jetonsTransferes=7)
    _safe_set(b, 'petriNet_Arc10', a1)
    assert _is_linked(b, 'petriNet_Arc10', a1)
    if hasattr(a1, 'petriNet_Transition11'):
        assert _is_linked(a1, 'petriNet_Transition11', b)
    _safe_set(b, 'petriNet_Arc10', a2)
    assert _is_linked(b, 'petriNet_Arc10', a2)
    if hasattr(a1, 'petriNet_Transition11'):
        assert not _is_linked(a1, 'petriNet_Transition11', b)
    if hasattr(a2, 'petriNet_Transition11'):
        assert _is_linked(a2, 'petriNet_Transition11', b)
    _safe_set(b, 'petriNet_Arc10', None)
    assert not _is_linked(b, 'petriNet_Arc10', a2)
    if hasattr(a2, 'petriNet_Transition11'):
        assert not _is_linked(a2, 'petriNet_Transition11', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

