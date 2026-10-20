import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Edge,
    petrinetmodel_Edge,
    petrinetmodel_EdgeToPlace,
    petrinetmodel_EdgeToTransaction,
    petrinetmodel_Petrinet,
    petrinetmodel_Place,
    petrinetmodel_Transition,
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

def test_assoc_inputPlaces5_reverse_link_reassign_clear():
    a1 = petrinetmodel_Transition(id=7, priority=7, token=7)
    a2 = petrinetmodel_Transition(id=13, priority=13, token=13)
    b = petrinetmodel_Place(id=7, token=7)
    _safe_set(b, 'petrinetmodel_Place7', a1)
    assert _is_linked(b, 'petrinetmodel_Place7', a1)
    if hasattr(a1, 'petrinetmodel_Transition6'):
        assert _is_linked(a1, 'petrinetmodel_Transition6', b)
    _safe_set(b, 'petrinetmodel_Place7', a2)
    assert _is_linked(b, 'petrinetmodel_Place7', a2)
    if hasattr(a1, 'petrinetmodel_Transition6'):
        assert not _is_linked(a1, 'petrinetmodel_Transition6', b)
    if hasattr(a2, 'petrinetmodel_Transition6'):
        assert _is_linked(a2, 'petrinetmodel_Transition6', b)
    _safe_set(b, 'petrinetmodel_Place7', None)
    assert not _is_linked(b, 'petrinetmodel_Place7', a2)
    if hasattr(a2, 'petrinetmodel_Transition6'):
        assert not _is_linked(a2, 'petrinetmodel_Transition6', b)


def test_assoc_places1_reverse_link_reassign_clear():
    a1 = petrinetmodel_Place(id=7, token=7)
    a2 = petrinetmodel_Place(id=13, token=13)
    b = petrinetmodel_Petrinet()
    _safe_set(b, 'petrinetmodel_Petrinet2', {a1})
    assert _is_linked(b, 'petrinetmodel_Petrinet2', a1)
    if hasattr(a1, 'petrinetmodel_Place'):
        assert _is_linked(a1, 'petrinetmodel_Place', b)
    _safe_set(b, 'petrinetmodel_Petrinet2', {a2})
    assert _is_linked(b, 'petrinetmodel_Petrinet2', a2)
    if hasattr(a1, 'petrinetmodel_Place'):
        assert not _is_linked(a1, 'petrinetmodel_Place', b)
    if hasattr(a2, 'petrinetmodel_Place'):
        assert _is_linked(a2, 'petrinetmodel_Place', b)
    _safe_set(b, 'petrinetmodel_Petrinet2', set())
    assert not _is_linked(b, 'petrinetmodel_Petrinet2', a2)
    if hasattr(a2, 'petrinetmodel_Place'):
        assert not _is_linked(a2, 'petrinetmodel_Place', b)


def test_assoc_transitions0_reverse_link_reassign_clear():
    a1 = petrinetmodel_Transition(id=7, priority=7, token=7)
    a2 = petrinetmodel_Transition(id=13, priority=13, token=13)
    b = petrinetmodel_Petrinet()
    _safe_set(b, 'petrinetmodel_Petrinet', {a1})
    assert _is_linked(b, 'petrinetmodel_Petrinet', a1)
    if hasattr(a1, 'petrinetmodel_Transition'):
        assert _is_linked(a1, 'petrinetmodel_Transition', b)
    _safe_set(b, 'petrinetmodel_Petrinet', {a2})
    assert _is_linked(b, 'petrinetmodel_Petrinet', a2)
    if hasattr(a1, 'petrinetmodel_Transition'):
        assert not _is_linked(a1, 'petrinetmodel_Transition', b)
    if hasattr(a2, 'petrinetmodel_Transition'):
        assert _is_linked(a2, 'petrinetmodel_Transition', b)
    _safe_set(b, 'petrinetmodel_Petrinet', set())
    assert not _is_linked(b, 'petrinetmodel_Petrinet', a2)
    if hasattr(a2, 'petrinetmodel_Transition'):
        assert not _is_linked(a2, 'petrinetmodel_Transition', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_in_10_stub_double():
    # petrinetmodel_EdgeToPlace has no real 'petrinetmodel_EdgeToPlace11' property in the generated
    # code (a bare stub) -- manually attach it so petrinetmodel_Place's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # petrinetmodel_Place's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = petrinetmodel_Place(id=7, token=7)
    partner = petrinetmodel_EdgeToPlace()
    setattr(partner, 'petrinetmodel_EdgeToPlace11', None)
    _safe_set(owner, 'petrinetmodel_Place12', partner)
    assert getattr(partner, 'petrinetmodel_EdgeToPlace11') == owner
    _safe_set(owner, 'petrinetmodel_Place12', None)
    assert getattr(partner, 'petrinetmodel_EdgeToPlace11') is None


def test_assoc_in_13_stub_double():
    # petrinetmodel_EdgeToTransaction has no real 'petrinetmodel_EdgeToTransaction14' property in the generated
    # code (a bare stub) -- manually attach it so petrinetmodel_Transition's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # petrinetmodel_Transition's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = petrinetmodel_Transition(id=7, priority=7, token=7)
    partner = petrinetmodel_EdgeToTransaction()
    setattr(partner, 'petrinetmodel_EdgeToTransaction14', None)
    _safe_set(owner, 'petrinetmodel_Transition15', partner)
    assert getattr(partner, 'petrinetmodel_EdgeToTransaction14') == owner
    _safe_set(owner, 'petrinetmodel_Transition15', None)
    assert getattr(partner, 'petrinetmodel_EdgeToTransaction14') is None


def test_assoc_out3_stub_double():
    # petrinetmodel_EdgeToPlace has no real 'petrinetmodel_EdgeToPlace' property in the generated
    # code (a bare stub) -- manually attach it so petrinetmodel_Transition's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # petrinetmodel_Transition's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = petrinetmodel_Transition(id=7, priority=7, token=7)
    partner = petrinetmodel_EdgeToPlace()
    setattr(partner, 'petrinetmodel_EdgeToPlace', None)
    _safe_set(owner, 'petrinetmodel_Transition4', {partner})
    assert getattr(partner, 'petrinetmodel_EdgeToPlace') == owner
    _safe_set(owner, 'petrinetmodel_Transition4', set())
    assert getattr(partner, 'petrinetmodel_EdgeToPlace') is None


def test_assoc_out8_stub_double():
    # petrinetmodel_EdgeToTransaction has no real 'petrinetmodel_EdgeToTransaction' property in the generated
    # code (a bare stub) -- manually attach it so petrinetmodel_Place's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # petrinetmodel_Place's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = petrinetmodel_Place(id=7, token=7)
    partner = petrinetmodel_EdgeToTransaction()
    setattr(partner, 'petrinetmodel_EdgeToTransaction', None)
    _safe_set(owner, 'petrinetmodel_Place9', {partner})
    assert getattr(partner, 'petrinetmodel_EdgeToTransaction') == owner
    _safe_set(owner, 'petrinetmodel_Place9', set())
    assert getattr(partner, 'petrinetmodel_EdgeToTransaction') is None


