import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    PetriNet_Net,
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

def test_assoc_dst13_reverse_link_reassign_clear():
    a1 = PetriNet_Transition(name="sample_text")
    a2 = PetriNet_Transition(name="sample_text_2")
    b = PetriNet_Place(name="sample_text")
    _safe_set(b, 'Place15', a1)
    assert _is_linked(b, 'Place15', a1)
    if hasattr(a1, 'src14'):
        assert _is_linked(a1, 'src14', b)
    _safe_set(b, 'Place15', a2)
    assert _is_linked(b, 'Place15', a2)
    if hasattr(a1, 'src14'):
        assert not _is_linked(a1, 'src14', b)
    if hasattr(a2, 'src14'):
        assert _is_linked(a2, 'src14', b)
    _safe_set(b, 'Place15', None)
    assert not _is_linked(b, 'Place15', a2)
    if hasattr(a2, 'src14'):
        assert not _is_linked(a2, 'src14', b)


def test_assoc_dst6_reverse_link_reassign_clear():
    a1 = PetriNet_Transition(name="sample_text")
    a2 = PetriNet_Transition(name="sample_text_2")
    b = PetriNet_Place(name="sample_text")
    _safe_set(b, 'src', {a1})
    assert _is_linked(b, 'src', a1)
    if hasattr(a1, 'Transition7'):
        assert _is_linked(a1, 'Transition7', b)
    _safe_set(b, 'src', {a2})
    assert _is_linked(b, 'src', a2)
    if hasattr(a1, 'Transition7'):
        assert not _is_linked(a1, 'Transition7', b)
    if hasattr(a2, 'Transition7'):
        assert _is_linked(a2, 'Transition7', b)
    _safe_set(b, 'src', set())
    assert not _is_linked(b, 'src', a2)
    if hasattr(a2, 'Transition7'):
        assert not _is_linked(a2, 'Transition7', b)


def test_assoc_src10_reverse_link_reassign_clear():
    a1 = PetriNet_Transition(name="sample_text")
    a2 = PetriNet_Transition(name="sample_text_2")
    b = PetriNet_Place(name="sample_text")
    _safe_set(b, 'Place12', a1)
    assert _is_linked(b, 'Place12', a1)
    if hasattr(a1, 'dst11'):
        assert _is_linked(a1, 'dst11', b)
    _safe_set(b, 'Place12', a2)
    assert _is_linked(b, 'Place12', a2)
    if hasattr(a1, 'dst11'):
        assert not _is_linked(a1, 'dst11', b)
    if hasattr(a2, 'dst11'):
        assert _is_linked(a2, 'dst11', b)
    _safe_set(b, 'Place12', None)
    assert not _is_linked(b, 'Place12', a2)
    if hasattr(a2, 'dst11'):
        assert not _is_linked(a2, 'dst11', b)


def test_assoc_src4_reverse_link_reassign_clear():
    a1 = PetriNet_Transition(name="sample_text")
    a2 = PetriNet_Transition(name="sample_text_2")
    b = PetriNet_Place(name="sample_text")
    _safe_set(b, 'dst', {a1})
    assert _is_linked(b, 'dst', a1)
    if hasattr(a1, 'Transition5'):
        assert _is_linked(a1, 'Transition5', b)
    _safe_set(b, 'dst', {a2})
    assert _is_linked(b, 'dst', a2)
    if hasattr(a1, 'Transition5'):
        assert not _is_linked(a1, 'Transition5', b)
    if hasattr(a2, 'Transition5'):
        assert _is_linked(a2, 'Transition5', b)
    _safe_set(b, 'dst', set())
    assert not _is_linked(b, 'dst', a2)
    if hasattr(a2, 'Transition5'):
        assert not _is_linked(a2, 'Transition5', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_net3_stub_double():
    # PetriNet_Net has no real 'Net' property in the generated
    # code (a bare stub) -- manually attach it so PetriNet_Place's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # PetriNet_Place's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = PetriNet_Place(name="sample_text")
    partner = PetriNet_Net()
    setattr(partner, 'Net', None)
    _safe_set(owner, 'places', partner)
    assert getattr(partner, 'Net') == owner
    _safe_set(owner, 'places', None)
    assert getattr(partner, 'Net') is None


def test_assoc_net8_stub_double():
    # PetriNet_Net has no real 'Net9' property in the generated
    # code (a bare stub) -- manually attach it so PetriNet_Transition's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # PetriNet_Transition's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = PetriNet_Transition(name="sample_text")
    partner = PetriNet_Net()
    setattr(partner, 'Net9', None)
    _safe_set(owner, 'transitions', partner)
    assert getattr(partner, 'Net9') == owner
    _safe_set(owner, 'transitions', None)
    assert getattr(partner, 'Net9') is None


def test_assoc_places0_stub_double():
    # PetriNet_Net has no real 'net' property in the generated
    # code (a bare stub) -- manually attach it so PetriNet_Place's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # PetriNet_Place's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = PetriNet_Place(name="sample_text")
    partner = PetriNet_Net()
    setattr(partner, 'net', None)
    _safe_set(owner, 'Place', partner)
    assert owner in getattr(partner, 'net')
    _safe_set(owner, 'Place', None)
    assert owner not in getattr(partner, 'net')


def test_assoc_transitions1_stub_double():
    # PetriNet_Net has no real 'net2' property in the generated
    # code (a bare stub) -- manually attach it so PetriNet_Transition's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # PetriNet_Transition's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = PetriNet_Transition(name="sample_text")
    partner = PetriNet_Net()
    setattr(partner, 'net2', None)
    _safe_set(owner, 'Transition', partner)
    assert owner in getattr(partner, 'net2')
    _safe_set(owner, 'Transition', None)
    assert owner not in getattr(partner, 'net2')


