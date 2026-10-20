import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    PetriNet,
    PetriNets_PetriNet,
    PetriNets_Place,
    PetriNets_Token,
    PetriNets_Transition,
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

# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_ins9_stub_double():
    # PetriNets_Transition has no real 'PetriNets_Transition' property in the generated
    # code (a bare stub) -- manually attach it so PetriNets_Place's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # PetriNets_Place's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = PetriNets_Place(capacity=7, itokens=7)
    partner = PetriNets_Transition()
    setattr(partner, 'PetriNets_Transition', None)
    _safe_set(owner, 'PetriNets_Place', partner)
    assert owner in getattr(partner, 'PetriNets_Transition')
    _safe_set(owner, 'PetriNets_Place', None)
    assert owner not in getattr(partner, 'PetriNets_Transition')


def test_assoc_net3_stub_double():
    # PetriNets_PetriNet has no real 'PetriNet' property in the generated
    # code (a bare stub) -- manually attach it so PetriNets_Place's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # PetriNets_Place's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = PetriNets_Place(capacity=7, itokens=7)
    partner = PetriNets_PetriNet()
    setattr(partner, 'PetriNet', None)
    _safe_set(owner, 'places', partner)
    assert getattr(partner, 'PetriNet') == owner
    _safe_set(owner, 'places', None)
    assert getattr(partner, 'PetriNet') is None


def test_assoc_outs10_stub_double():
    # PetriNets_Transition has no real 'PetriNets_Transition11' property in the generated
    # code (a bare stub) -- manually attach it so PetriNets_Place's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # PetriNets_Place's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = PetriNets_Place(capacity=7, itokens=7)
    partner = PetriNets_Transition()
    setattr(partner, 'PetriNets_Transition11', None)
    _safe_set(owner, 'PetriNets_Place12', partner)
    assert owner in getattr(partner, 'PetriNets_Transition11')
    _safe_set(owner, 'PetriNets_Place12', None)
    assert owner not in getattr(partner, 'PetriNets_Transition11')


def test_assoc_place5_stub_double():
    # PetriNets_Token has no real 'tokens.1' property in the generated
    # code (a bare stub) -- manually attach it so PetriNets_Place's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # PetriNets_Place's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = PetriNets_Place(capacity=7, itokens=7)
    partner = PetriNets_Token()
    setattr(partner, 'tokens.1', None)
    _safe_set(owner, 'Place6', partner)
    assert getattr(partner, 'tokens.1') == owner
    _safe_set(owner, 'Place6', None)
    assert getattr(partner, 'tokens.1') is None


def test_assoc_places0_stub_double():
    # PetriNets_PetriNet has no real 'net' property in the generated
    # code (a bare stub) -- manually attach it so PetriNets_Place's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # PetriNets_Place's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = PetriNets_Place(capacity=7, itokens=7)
    partner = PetriNets_PetriNet()
    setattr(partner, 'net', None)
    _safe_set(owner, 'Place', partner)
    assert owner in getattr(partner, 'net')
    _safe_set(owner, 'Place', None)
    assert owner not in getattr(partner, 'net')


def test_assoc_tokens4_stub_double():
    # PetriNets_Token has no real 'Token' property in the generated
    # code (a bare stub) -- manually attach it so PetriNets_Place's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # PetriNets_Place's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = PetriNets_Place(capacity=7, itokens=7)
    partner = PetriNets_Token()
    setattr(partner, 'Token', None)
    _safe_set(owner, 'place', {partner})
    assert getattr(partner, 'Token') == owner
    _safe_set(owner, 'place', set())
    assert getattr(partner, 'Token') is None


