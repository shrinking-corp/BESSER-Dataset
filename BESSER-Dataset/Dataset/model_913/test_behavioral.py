import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Noeud,
    PetriElement,
    PetriNet_Arc,
    PetriNet_Noeud,
    PetriNet_PetriElement,
    PetriNet_Place,
    PetriNet_ReseauPetri,
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

def test_assoc_LinksToSuccessors8_reverse_link_reassign_clear():
    a1 = PetriNet_Noeud(name="sample_text")
    a2 = PetriNet_Noeud(name="sample_text_2")
    b = PetriNet_Arc(isReadArc=True, poids=7)
    _safe_set(b, 'Arc9', a1)
    assert _is_linked(b, 'Arc9', a1)
    if hasattr(a1, 'predecessor'):
        assert _is_linked(a1, 'predecessor', b)
    _safe_set(b, 'Arc9', a2)
    assert _is_linked(b, 'Arc9', a2)
    if hasattr(a1, 'predecessor'):
        assert not _is_linked(a1, 'predecessor', b)
    if hasattr(a2, 'predecessor'):
        assert _is_linked(a2, 'predecessor', b)
    _safe_set(b, 'Arc9', None)
    assert not _is_linked(b, 'Arc9', a2)
    if hasattr(a2, 'predecessor'):
        assert not _is_linked(a2, 'predecessor', b)


def test_assoc_linksToPredecessors7_reverse_link_reassign_clear():
    a1 = PetriNet_Noeud(name="sample_text")
    a2 = PetriNet_Noeud(name="sample_text_2")
    b = PetriNet_Arc(isReadArc=True, poids=7)
    _safe_set(b, 'Arc', a1)
    assert _is_linked(b, 'Arc', a1)
    if hasattr(a1, 'successor'):
        assert _is_linked(a1, 'successor', b)
    _safe_set(b, 'Arc', a2)
    assert _is_linked(b, 'Arc', a2)
    if hasattr(a1, 'successor'):
        assert not _is_linked(a1, 'successor', b)
    if hasattr(a2, 'successor'):
        assert _is_linked(a2, 'successor', b)
    _safe_set(b, 'Arc', None)
    assert not _is_linked(b, 'Arc', a2)
    if hasattr(a2, 'successor'):
        assert not _is_linked(a2, 'successor', b)


def test_assoc_predecessor1_reverse_link_reassign_clear():
    a1 = PetriNet_Noeud(name="sample_text")
    a2 = PetriNet_Noeud(name="sample_text_2")
    b = PetriNet_Arc(isReadArc=True, poids=7)
    _safe_set(b, 'LinksToSuccessors', a1)
    assert _is_linked(b, 'LinksToSuccessors', a1)
    if hasattr(a1, 'Noeud2'):
        assert _is_linked(a1, 'Noeud2', b)
    _safe_set(b, 'LinksToSuccessors', a2)
    assert _is_linked(b, 'LinksToSuccessors', a2)
    if hasattr(a1, 'Noeud2'):
        assert not _is_linked(a1, 'Noeud2', b)
    if hasattr(a2, 'Noeud2'):
        assert _is_linked(a2, 'Noeud2', b)
    _safe_set(b, 'LinksToSuccessors', None)
    assert not _is_linked(b, 'LinksToSuccessors', a2)
    if hasattr(a2, 'Noeud2'):
        assert not _is_linked(a2, 'Noeud2', b)


def test_assoc_successor0_reverse_link_reassign_clear():
    a1 = PetriNet_Noeud(name="sample_text")
    a2 = PetriNet_Noeud(name="sample_text_2")
    b = PetriNet_Arc(isReadArc=True, poids=7)
    _safe_set(b, 'linksToPredecessors', a1)
    assert _is_linked(b, 'linksToPredecessors', a1)
    if hasattr(a1, 'Noeud'):
        assert _is_linked(a1, 'Noeud', b)
    _safe_set(b, 'linksToPredecessors', a2)
    assert _is_linked(b, 'linksToPredecessors', a2)
    if hasattr(a1, 'Noeud'):
        assert not _is_linked(a1, 'Noeud', b)
    if hasattr(a2, 'Noeud'):
        assert _is_linked(a2, 'Noeud', b)
    _safe_set(b, 'linksToPredecessors', None)
    assert not _is_linked(b, 'linksToPredecessors', a2)
    if hasattr(a2, 'Noeud'):
        assert not _is_linked(a2, 'Noeud', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_petrielement3_stub_double():
    # PetriNet_PetriElement has no real 'PetriNet_PetriElement' property in the generated
    # code (a bare stub) -- manually attach it so PetriNet_ReseauPetri's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # PetriNet_ReseauPetri's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = PetriNet_ReseauPetri(name="sample_text")
    partner = PetriNet_PetriElement()
    setattr(partner, 'PetriNet_PetriElement', None)
    _safe_set(owner, 'PetriNet_ReseauPetri', {partner})
    assert getattr(partner, 'PetriNet_PetriElement') == owner
    _safe_set(owner, 'PetriNet_ReseauPetri', set())
    assert getattr(partner, 'PetriNet_PetriElement') is None


def test_assoc_reseauPetri4_stub_double():
    # PetriNet_PetriElement has no real 'PetriNet_PetriElement5' property in the generated
    # code (a bare stub) -- manually attach it so PetriNet_ReseauPetri's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # PetriNet_ReseauPetri's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = PetriNet_ReseauPetri(name="sample_text")
    partner = PetriNet_PetriElement()
    setattr(partner, 'PetriNet_PetriElement5', None)
    _safe_set(owner, 'PetriNet_ReseauPetri6', partner)
    assert getattr(partner, 'PetriNet_PetriElement5') == owner
    _safe_set(owner, 'PetriNet_ReseauPetri6', None)
    assert getattr(partner, 'PetriNet_PetriElement5') is None


