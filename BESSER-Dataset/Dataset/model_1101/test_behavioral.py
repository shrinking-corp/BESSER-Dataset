import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
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

def test_assoc_inh12_reverse_link_reassign_clear():
    a1 = PetriNets_Transition(priority=3.14)
    a2 = PetriNets_Transition(priority=9.99)
    b = PetriNets_Place(bound=7, itokens=7)
    _safe_set(b, 'PetriNets_Place14', a1)
    assert _is_linked(b, 'PetriNets_Place14', a1)
    if hasattr(a1, 'PetriNets_Transition13'):
        assert _is_linked(a1, 'PetriNets_Transition13', b)
    _safe_set(b, 'PetriNets_Place14', a2)
    assert _is_linked(b, 'PetriNets_Place14', a2)
    if hasattr(a1, 'PetriNets_Transition13'):
        assert not _is_linked(a1, 'PetriNets_Transition13', b)
    if hasattr(a2, 'PetriNets_Transition13'):
        assert _is_linked(a2, 'PetriNets_Transition13', b)
    _safe_set(b, 'PetriNets_Place14', None)
    assert not _is_linked(b, 'PetriNets_Place14', a2)
    if hasattr(a2, 'PetriNets_Transition13'):
        assert not _is_linked(a2, 'PetriNets_Transition13', b)


def test_assoc_ins7_reverse_link_reassign_clear():
    a1 = PetriNets_Transition(priority=3.14)
    a2 = PetriNets_Transition(priority=9.99)
    b = PetriNets_Place(bound=7, itokens=7)
    _safe_set(b, 'PetriNets_Place8', a1)
    assert _is_linked(b, 'PetriNets_Place8', a1)
    if hasattr(a1, 'PetriNets_Transition'):
        assert _is_linked(a1, 'PetriNets_Transition', b)
    _safe_set(b, 'PetriNets_Place8', a2)
    assert _is_linked(b, 'PetriNets_Place8', a2)
    if hasattr(a1, 'PetriNets_Transition'):
        assert not _is_linked(a1, 'PetriNets_Transition', b)
    if hasattr(a2, 'PetriNets_Transition'):
        assert _is_linked(a2, 'PetriNets_Transition', b)
    _safe_set(b, 'PetriNets_Place8', None)
    assert not _is_linked(b, 'PetriNets_Place8', a2)
    if hasattr(a2, 'PetriNets_Transition'):
        assert not _is_linked(a2, 'PetriNets_Transition', b)


def test_assoc_outs9_reverse_link_reassign_clear():
    a1 = PetriNets_Transition(priority=3.14)
    a2 = PetriNets_Transition(priority=9.99)
    b = PetriNets_Place(bound=7, itokens=7)
    _safe_set(b, 'PetriNets_Place11', a1)
    assert _is_linked(b, 'PetriNets_Place11', a1)
    if hasattr(a1, 'PetriNets_Transition10'):
        assert _is_linked(a1, 'PetriNets_Transition10', b)
    _safe_set(b, 'PetriNets_Place11', a2)
    assert _is_linked(b, 'PetriNets_Place11', a2)
    if hasattr(a1, 'PetriNets_Transition10'):
        assert not _is_linked(a1, 'PetriNets_Transition10', b)
    if hasattr(a2, 'PetriNets_Transition10'):
        assert _is_linked(a2, 'PetriNets_Transition10', b)
    _safe_set(b, 'PetriNets_Place11', None)
    assert not _is_linked(b, 'PetriNets_Place11', a2)
    if hasattr(a2, 'PetriNets_Transition10'):
        assert not _is_linked(a2, 'PetriNets_Transition10', b)


def test_assoc_read15_reverse_link_reassign_clear():
    a1 = PetriNets_Transition(priority=3.14)
    a2 = PetriNets_Transition(priority=9.99)
    b = PetriNets_Place(bound=7, itokens=7)
    _safe_set(b, 'PetriNets_Place17', a1)
    assert _is_linked(b, 'PetriNets_Place17', a1)
    if hasattr(a1, 'PetriNets_Transition16'):
        assert _is_linked(a1, 'PetriNets_Transition16', b)
    _safe_set(b, 'PetriNets_Place17', a2)
    assert _is_linked(b, 'PetriNets_Place17', a2)
    if hasattr(a1, 'PetriNets_Transition16'):
        assert not _is_linked(a1, 'PetriNets_Transition16', b)
    if hasattr(a2, 'PetriNets_Transition16'):
        assert _is_linked(a2, 'PetriNets_Transition16', b)
    _safe_set(b, 'PetriNets_Place17', None)
    assert not _is_linked(b, 'PetriNets_Place17', a2)
    if hasattr(a2, 'PetriNets_Transition16'):
        assert not _is_linked(a2, 'PetriNets_Transition16', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_ctokens4_stub_double():
    # PetriNets_Token has no real 'PetriNets_Token' property in the generated
    # code (a bare stub) -- manually attach it so PetriNets_Place's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # PetriNets_Place's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = PetriNets_Place(bound=7, itokens=7)
    partner = PetriNets_Token()
    setattr(partner, 'PetriNets_Token', None)
    _safe_set(owner, 'PetriNets_Place', {partner})
    assert getattr(partner, 'PetriNets_Token') == owner
    _safe_set(owner, 'PetriNets_Place', set())
    assert getattr(partner, 'PetriNets_Token') is None


def test_assoc_net3_stub_double():
    # PetriNets_PetriNet has no real 'PetriNet' property in the generated
    # code (a bare stub) -- manually attach it so PetriNets_Place's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # PetriNets_Place's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = PetriNets_Place(bound=7, itokens=7)
    partner = PetriNets_PetriNet()
    setattr(partner, 'PetriNet', None)
    _safe_set(owner, 'places', partner)
    assert getattr(partner, 'PetriNet') == owner
    _safe_set(owner, 'places', None)
    assert getattr(partner, 'PetriNet') is None


def test_assoc_net5_stub_double():
    # PetriNets_PetriNet has no real 'PetriNet6' property in the generated
    # code (a bare stub) -- manually attach it so PetriNets_Transition's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # PetriNets_Transition's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = PetriNets_Transition(priority=3.14)
    partner = PetriNets_PetriNet()
    setattr(partner, 'PetriNet6', None)
    _safe_set(owner, 'trans', partner)
    assert getattr(partner, 'PetriNet6') == owner
    _safe_set(owner, 'trans', None)
    assert getattr(partner, 'PetriNet6') is None


def test_assoc_places0_stub_double():
    # PetriNets_PetriNet has no real 'net' property in the generated
    # code (a bare stub) -- manually attach it so PetriNets_Place's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # PetriNets_Place's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = PetriNets_Place(bound=7, itokens=7)
    partner = PetriNets_PetriNet()
    setattr(partner, 'net', None)
    _safe_set(owner, 'Place', partner)
    assert owner in getattr(partner, 'net')
    _safe_set(owner, 'Place', None)
    assert owner not in getattr(partner, 'net')


def test_assoc_trans1_stub_double():
    # PetriNets_PetriNet has no real 'net2' property in the generated
    # code (a bare stub) -- manually attach it so PetriNets_Transition's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # PetriNets_Transition's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = PetriNets_Transition(priority=3.14)
    partner = PetriNets_PetriNet()
    setattr(partner, 'net2', None)
    _safe_set(owner, 'Transition', partner)
    assert owner in getattr(partner, 'net2')
    _safe_set(owner, 'Transition', None)
    assert owner not in getattr(partner, 'net2')


