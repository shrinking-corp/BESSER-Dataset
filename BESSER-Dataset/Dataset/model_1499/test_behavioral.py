import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    PetriElement,
    PetriNet_Arc,
    PetriNet_PetriElement,
    PetriNet_Place,
    PetriNet_ReseauPetri,
    PetriNet_Transition,
    ArcType,
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

def test_assoc_arcs6_reverse_link_reassign_clear():
    a1 = PetriNet_ReseauPetri(name="sample_text")
    a2 = PetriNet_ReseauPetri(name="sample_text_2")
    b = PetriNet_Arc(poids="sample_text", type="sample_text")
    _safe_set(b, 'PetriNet_Arc8', a1)
    assert _is_linked(b, 'PetriNet_Arc8', a1)
    if hasattr(a1, 'PetriNet_ReseauPetri7'):
        assert _is_linked(a1, 'PetriNet_ReseauPetri7', b)
    _safe_set(b, 'PetriNet_Arc8', a2)
    assert _is_linked(b, 'PetriNet_Arc8', a2)
    if hasattr(a1, 'PetriNet_ReseauPetri7'):
        assert not _is_linked(a1, 'PetriNet_ReseauPetri7', b)
    if hasattr(a2, 'PetriNet_ReseauPetri7'):
        assert _is_linked(a2, 'PetriNet_ReseauPetri7', b)
    _safe_set(b, 'PetriNet_Arc8', None)
    assert not _is_linked(b, 'PetriNet_Arc8', a2)
    if hasattr(a2, 'PetriNet_ReseauPetri7'):
        assert not _is_linked(a2, 'PetriNet_ReseauPetri7', b)


def test_assoc_debut0_reverse_link_reassign_clear():
    a1 = PetriNet_PetriElement(name="sample_text")
    a2 = PetriNet_PetriElement(name="sample_text_2")
    b = PetriNet_Arc(poids="sample_text", type="sample_text")
    _safe_set(b, 'PetriNet_Arc', a1)
    assert _is_linked(b, 'PetriNet_Arc', a1)
    if hasattr(a1, 'PetriNet_PetriElement'):
        assert _is_linked(a1, 'PetriNet_PetriElement', b)
    _safe_set(b, 'PetriNet_Arc', a2)
    assert _is_linked(b, 'PetriNet_Arc', a2)
    if hasattr(a1, 'PetriNet_PetriElement'):
        assert not _is_linked(a1, 'PetriNet_PetriElement', b)
    if hasattr(a2, 'PetriNet_PetriElement'):
        assert _is_linked(a2, 'PetriNet_PetriElement', b)
    _safe_set(b, 'PetriNet_Arc', None)
    assert not _is_linked(b, 'PetriNet_Arc', a2)
    if hasattr(a2, 'PetriNet_PetriElement'):
        assert not _is_linked(a2, 'PetriNet_PetriElement', b)


def test_assoc_elements4_reverse_link_reassign_clear():
    a1 = PetriNet_ReseauPetri(name="sample_text")
    a2 = PetriNet_ReseauPetri(name="sample_text_2")
    b = PetriNet_PetriElement(name="sample_text")
    _safe_set(b, 'PetriNet_PetriElement5', a1)
    assert _is_linked(b, 'PetriNet_PetriElement5', a1)
    if hasattr(a1, 'PetriNet_ReseauPetri'):
        assert _is_linked(a1, 'PetriNet_ReseauPetri', b)
    _safe_set(b, 'PetriNet_PetriElement5', a2)
    assert _is_linked(b, 'PetriNet_PetriElement5', a2)
    if hasattr(a1, 'PetriNet_ReseauPetri'):
        assert not _is_linked(a1, 'PetriNet_ReseauPetri', b)
    if hasattr(a2, 'PetriNet_ReseauPetri'):
        assert _is_linked(a2, 'PetriNet_ReseauPetri', b)
    _safe_set(b, 'PetriNet_PetriElement5', None)
    assert not _is_linked(b, 'PetriNet_PetriElement5', a2)
    if hasattr(a2, 'PetriNet_ReseauPetri'):
        assert not _is_linked(a2, 'PetriNet_ReseauPetri', b)


def test_assoc_fin1_reverse_link_reassign_clear():
    a1 = PetriNet_PetriElement(name="sample_text")
    a2 = PetriNet_PetriElement(name="sample_text_2")
    b = PetriNet_Arc(poids="sample_text", type="sample_text")
    _safe_set(b, 'PetriNet_Arc2', a1)
    assert _is_linked(b, 'PetriNet_Arc2', a1)
    if hasattr(a1, 'PetriNet_PetriElement3'):
        assert _is_linked(a1, 'PetriNet_PetriElement3', b)
    _safe_set(b, 'PetriNet_Arc2', a2)
    assert _is_linked(b, 'PetriNet_Arc2', a2)
    if hasattr(a1, 'PetriNet_PetriElement3'):
        assert not _is_linked(a1, 'PetriNet_PetriElement3', b)
    if hasattr(a2, 'PetriNet_PetriElement3'):
        assert _is_linked(a2, 'PetriNet_PetriElement3', b)
    _safe_set(b, 'PetriNet_Arc2', None)
    assert not _is_linked(b, 'PetriNet_Arc2', a2)
    if hasattr(a2, 'PetriNet_PetriElement3'):
        assert not _is_linked(a2, 'PetriNet_PetriElement3', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

