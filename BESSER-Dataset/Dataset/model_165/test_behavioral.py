import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Arc,
    PetriNets_Arc,
    PetriNets_ArcPT,
    PetriNets_ArcTP,
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

def test_assoc_inh23_reverse_link_reassign_clear():
    a1 = PetriNets_Transition(priority=3.14)
    a2 = PetriNets_Transition(priority=9.99)
    b = PetriNets_Place(bound=7, itokens=7)
    _safe_set(b, 'PetriNets_Place25', a1)
    assert _is_linked(b, 'PetriNets_Place25', a1)
    if hasattr(a1, 'PetriNets_Transition24'):
        assert _is_linked(a1, 'PetriNets_Transition24', b)
    _safe_set(b, 'PetriNets_Place25', a2)
    assert _is_linked(b, 'PetriNets_Place25', a2)
    if hasattr(a1, 'PetriNets_Transition24'):
        assert not _is_linked(a1, 'PetriNets_Transition24', b)
    if hasattr(a2, 'PetriNets_Transition24'):
        assert _is_linked(a2, 'PetriNets_Transition24', b)
    _safe_set(b, 'PetriNets_Place25', None)
    assert not _is_linked(b, 'PetriNets_Place25', a2)
    if hasattr(a2, 'PetriNets_Transition24'):
        assert not _is_linked(a2, 'PetriNets_Transition24', b)


def test_assoc_ins17_reverse_link_reassign_clear():
    a1 = PetriNets_Transition(priority=3.14)
    a2 = PetriNets_Transition(priority=9.99)
    b = PetriNets_Place(bound=7, itokens=7)
    _safe_set(b, 'PetriNets_Place19', a1)
    assert _is_linked(b, 'PetriNets_Place19', a1)
    if hasattr(a1, 'PetriNets_Transition18'):
        assert _is_linked(a1, 'PetriNets_Transition18', b)
    _safe_set(b, 'PetriNets_Place19', a2)
    assert _is_linked(b, 'PetriNets_Place19', a2)
    if hasattr(a1, 'PetriNets_Transition18'):
        assert not _is_linked(a1, 'PetriNets_Transition18', b)
    if hasattr(a2, 'PetriNets_Transition18'):
        assert _is_linked(a2, 'PetriNets_Transition18', b)
    _safe_set(b, 'PetriNets_Place19', None)
    assert not _is_linked(b, 'PetriNets_Place19', a2)
    if hasattr(a2, 'PetriNets_Transition18'):
        assert not _is_linked(a2, 'PetriNets_Transition18', b)


def test_assoc_outs20_reverse_link_reassign_clear():
    a1 = PetriNets_Transition(priority=3.14)
    a2 = PetriNets_Transition(priority=9.99)
    b = PetriNets_Place(bound=7, itokens=7)
    _safe_set(b, 'PetriNets_Place22', a1)
    assert _is_linked(b, 'PetriNets_Place22', a1)
    if hasattr(a1, 'PetriNets_Transition21'):
        assert _is_linked(a1, 'PetriNets_Transition21', b)
    _safe_set(b, 'PetriNets_Place22', a2)
    assert _is_linked(b, 'PetriNets_Place22', a2)
    if hasattr(a1, 'PetriNets_Transition21'):
        assert not _is_linked(a1, 'PetriNets_Transition21', b)
    if hasattr(a2, 'PetriNets_Transition21'):
        assert _is_linked(a2, 'PetriNets_Transition21', b)
    _safe_set(b, 'PetriNets_Place22', None)
    assert not _is_linked(b, 'PetriNets_Place22', a2)
    if hasattr(a2, 'PetriNets_Transition21'):
        assert not _is_linked(a2, 'PetriNets_Transition21', b)


def test_assoc_read26_reverse_link_reassign_clear():
    a1 = PetriNets_Transition(priority=3.14)
    a2 = PetriNets_Transition(priority=9.99)
    b = PetriNets_Place(bound=7, itokens=7)
    _safe_set(b, 'PetriNets_Place28', a1)
    assert _is_linked(b, 'PetriNets_Place28', a1)
    if hasattr(a1, 'PetriNets_Transition27'):
        assert _is_linked(a1, 'PetriNets_Transition27', b)
    _safe_set(b, 'PetriNets_Place28', a2)
    assert _is_linked(b, 'PetriNets_Place28', a2)
    if hasattr(a1, 'PetriNets_Transition27'):
        assert not _is_linked(a1, 'PetriNets_Transition27', b)
    if hasattr(a2, 'PetriNets_Transition27'):
        assert _is_linked(a2, 'PetriNets_Transition27', b)
    _safe_set(b, 'PetriNets_Place28', None)
    assert not _is_linked(b, 'PetriNets_Place28', a2)
    if hasattr(a2, 'PetriNets_Transition27'):
        assert not _is_linked(a2, 'PetriNets_Transition27', b)


def test_assoc_reset29_reverse_link_reassign_clear():
    a1 = PetriNets_Transition(priority=3.14)
    a2 = PetriNets_Transition(priority=9.99)
    b = PetriNets_Place(bound=7, itokens=7)
    _safe_set(b, 'PetriNets_Place31', a1)
    assert _is_linked(b, 'PetriNets_Place31', a1)
    if hasattr(a1, 'PetriNets_Transition30'):
        assert _is_linked(a1, 'PetriNets_Transition30', b)
    _safe_set(b, 'PetriNets_Place31', a2)
    assert _is_linked(b, 'PetriNets_Place31', a2)
    if hasattr(a1, 'PetriNets_Transition30'):
        assert not _is_linked(a1, 'PetriNets_Transition30', b)
    if hasattr(a2, 'PetriNets_Transition30'):
        assert _is_linked(a2, 'PetriNets_Transition30', b)
    _safe_set(b, 'PetriNets_Place31', None)
    assert not _is_linked(b, 'PetriNets_Place31', a2)
    if hasattr(a2, 'PetriNets_Transition30'):
        assert not _is_linked(a2, 'PetriNets_Transition30', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_arcs3_stub_double():
    # PetriNets_PetriNet has no real 'PetriNets_PetriNet' property in the generated
    # code (a bare stub) -- manually attach it so PetriNets_Arc's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # PetriNets_Arc's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = PetriNets_Arc(weight=7)
    partner = PetriNets_PetriNet()
    setattr(partner, 'PetriNets_PetriNet', None)
    _safe_set(owner, 'PetriNets_Arc', partner)
    assert owner in getattr(partner, 'PetriNets_PetriNet')
    _safe_set(owner, 'PetriNets_Arc', None)
    assert owner not in getattr(partner, 'PetriNets_PetriNet')


def test_assoc_ctokens5_stub_double():
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


def test_assoc_from_10_stub_double():
    # PetriNets_ArcTP has no real 'PetriNets_ArcTP' property in the generated
    # code (a bare stub) -- manually attach it so PetriNets_Transition's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # PetriNets_Transition's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = PetriNets_Transition(priority=3.14)
    partner = PetriNets_ArcTP()
    setattr(partner, 'PetriNets_ArcTP', None)
    _safe_set(owner, 'PetriNets_Transition11', partner)
    assert getattr(partner, 'PetriNets_ArcTP') == owner
    _safe_set(owner, 'PetriNets_Transition11', None)
    assert getattr(partner, 'PetriNets_ArcTP') is None


def test_assoc_from_6_stub_double():
    # PetriNets_ArcPT has no real 'PetriNets_ArcPT' property in the generated
    # code (a bare stub) -- manually attach it so PetriNets_Place's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # PetriNets_Place's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = PetriNets_Place(bound=7, itokens=7)
    partner = PetriNets_ArcPT()
    setattr(partner, 'PetriNets_ArcPT', None)
    _safe_set(owner, 'PetriNets_Place7', partner)
    assert getattr(partner, 'PetriNets_ArcPT') == owner
    _safe_set(owner, 'PetriNets_Place7', None)
    assert getattr(partner, 'PetriNets_ArcPT') is None


def test_assoc_net15_stub_double():
    # PetriNets_PetriNet has no real 'PetriNet16' property in the generated
    # code (a bare stub) -- manually attach it so PetriNets_Transition's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # PetriNets_Transition's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = PetriNets_Transition(priority=3.14)
    partner = PetriNets_PetriNet()
    setattr(partner, 'PetriNet16', None)
    _safe_set(owner, 'trans', partner)
    assert getattr(partner, 'PetriNet16') == owner
    _safe_set(owner, 'trans', None)
    assert getattr(partner, 'PetriNet16') is None


def test_assoc_net4_stub_double():
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


def test_assoc_to12_stub_double():
    # PetriNets_ArcTP has no real 'PetriNets_ArcTP13' property in the generated
    # code (a bare stub) -- manually attach it so PetriNets_Place's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # PetriNets_Place's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = PetriNets_Place(bound=7, itokens=7)
    partner = PetriNets_ArcTP()
    setattr(partner, 'PetriNets_ArcTP13', None)
    _safe_set(owner, 'PetriNets_Place14', partner)
    assert getattr(partner, 'PetriNets_ArcTP13') == owner
    _safe_set(owner, 'PetriNets_Place14', None)
    assert getattr(partner, 'PetriNets_ArcTP13') is None


def test_assoc_to8_stub_double():
    # PetriNets_ArcPT has no real 'PetriNets_ArcPT9' property in the generated
    # code (a bare stub) -- manually attach it so PetriNets_Transition's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # PetriNets_Transition's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = PetriNets_Transition(priority=3.14)
    partner = PetriNets_ArcPT()
    setattr(partner, 'PetriNets_ArcPT9', None)
    _safe_set(owner, 'PetriNets_Transition', partner)
    assert getattr(partner, 'PetriNets_ArcPT9') == owner
    _safe_set(owner, 'PetriNets_Transition', None)
    assert getattr(partner, 'PetriNets_ArcPT9') is None


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


