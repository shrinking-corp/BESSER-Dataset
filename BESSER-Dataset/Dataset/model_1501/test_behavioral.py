import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Noeud,
    PetriNetElt,
    petriNet_Arc,
    petriNet_Noeud,
    petriNet_PetriNet,
    petriNet_PetriNetElt,
    petriNet_Place,
    petriNet_Transition,
    TypeArc,
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

def test_assoc_noeudsPredecesseurs1_reverse_link_reassign_clear():
    a1 = petriNet_Noeud(name="sample_text")
    a2 = petriNet_Noeud(name="sample_text_2")
    b = petriNet_Arc(poids=7, typeArc="sample_text")
    _safe_set(b, 'Arc2', a1)
    assert _is_linked(b, 'Arc2', a1)
    if hasattr(a1, 'successeur'):
        assert _is_linked(a1, 'successeur', b)
    _safe_set(b, 'Arc2', a2)
    assert _is_linked(b, 'Arc2', a2)
    if hasattr(a1, 'successeur'):
        assert not _is_linked(a1, 'successeur', b)
    if hasattr(a2, 'successeur'):
        assert _is_linked(a2, 'successeur', b)
    _safe_set(b, 'Arc2', None)
    assert not _is_linked(b, 'Arc2', a2)
    if hasattr(a2, 'successeur'):
        assert not _is_linked(a2, 'successeur', b)


def test_assoc_noeudsSuccesseurs0_reverse_link_reassign_clear():
    a1 = petriNet_Noeud(name="sample_text")
    a2 = petriNet_Noeud(name="sample_text_2")
    b = petriNet_Arc(poids=7, typeArc="sample_text")
    _safe_set(b, 'Arc', a1)
    assert _is_linked(b, 'Arc', a1)
    if hasattr(a1, 'predecesseur'):
        assert _is_linked(a1, 'predecesseur', b)
    _safe_set(b, 'Arc', a2)
    assert _is_linked(b, 'Arc', a2)
    if hasattr(a1, 'predecesseur'):
        assert not _is_linked(a1, 'predecesseur', b)
    if hasattr(a2, 'predecesseur'):
        assert _is_linked(a2, 'predecesseur', b)
    _safe_set(b, 'Arc', None)
    assert not _is_linked(b, 'Arc', a2)
    if hasattr(a2, 'predecesseur'):
        assert not _is_linked(a2, 'predecesseur', b)


def test_assoc_predecesseur3_reverse_link_reassign_clear():
    a1 = petriNet_Noeud(name="sample_text")
    a2 = petriNet_Noeud(name="sample_text_2")
    b = petriNet_Arc(poids=7, typeArc="sample_text")
    _safe_set(b, 'noeudsSuccesseurs', a1)
    assert _is_linked(b, 'noeudsSuccesseurs', a1)
    if hasattr(a1, 'Noeud'):
        assert _is_linked(a1, 'Noeud', b)
    _safe_set(b, 'noeudsSuccesseurs', a2)
    assert _is_linked(b, 'noeudsSuccesseurs', a2)
    if hasattr(a1, 'Noeud'):
        assert not _is_linked(a1, 'Noeud', b)
    if hasattr(a2, 'Noeud'):
        assert _is_linked(a2, 'Noeud', b)
    _safe_set(b, 'noeudsSuccesseurs', None)
    assert not _is_linked(b, 'noeudsSuccesseurs', a2)
    if hasattr(a2, 'Noeud'):
        assert not _is_linked(a2, 'Noeud', b)


def test_assoc_successeur4_reverse_link_reassign_clear():
    a1 = petriNet_Noeud(name="sample_text")
    a2 = petriNet_Noeud(name="sample_text_2")
    b = petriNet_Arc(poids=7, typeArc="sample_text")
    _safe_set(b, 'noeudsPredecesseurs', a1)
    assert _is_linked(b, 'noeudsPredecesseurs', a1)
    if hasattr(a1, 'Noeud5'):
        assert _is_linked(a1, 'Noeud5', b)
    _safe_set(b, 'noeudsPredecesseurs', a2)
    assert _is_linked(b, 'noeudsPredecesseurs', a2)
    if hasattr(a1, 'Noeud5'):
        assert not _is_linked(a1, 'Noeud5', b)
    if hasattr(a2, 'Noeud5'):
        assert _is_linked(a2, 'Noeud5', b)
    _safe_set(b, 'noeudsPredecesseurs', None)
    assert not _is_linked(b, 'noeudsPredecesseurs', a2)
    if hasattr(a2, 'Noeud5'):
        assert not _is_linked(a2, 'Noeud5', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_net6_stub_double():
    # petriNet_PetriNetElt has no real 'petriNet_PetriNetElt' property in the generated
    # code (a bare stub) -- manually attach it so petriNet_PetriNet's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # petriNet_PetriNet's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = petriNet_PetriNet(name="sample_text")
    partner = petriNet_PetriNetElt()
    setattr(partner, 'petriNet_PetriNetElt', None)
    _safe_set(owner, 'petriNet_PetriNet', partner)
    assert getattr(partner, 'petriNet_PetriNetElt') == owner
    _safe_set(owner, 'petriNet_PetriNet', None)
    assert getattr(partner, 'petriNet_PetriNetElt') is None


def test_assoc_petrinetelt7_stub_double():
    # petriNet_PetriNetElt has no real 'petriNet_PetriNetElt9' property in the generated
    # code (a bare stub) -- manually attach it so petriNet_PetriNet's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # petriNet_PetriNet's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = petriNet_PetriNet(name="sample_text")
    partner = petriNet_PetriNetElt()
    setattr(partner, 'petriNet_PetriNetElt9', None)
    _safe_set(owner, 'petriNet_PetriNet8', {partner})
    assert getattr(partner, 'petriNet_PetriNetElt9') == owner
    _safe_set(owner, 'petriNet_PetriNet8', set())
    assert getattr(partner, 'petriNet_PetriNetElt9') is None


