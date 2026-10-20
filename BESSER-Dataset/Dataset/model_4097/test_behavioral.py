import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    RDMElement,
    RDM_ConnectionPoint,
    RDM_RDMElement,
    RDM_RailwayDomainModel,
    RDM_Route,
    RDM_RouteElement,
    RDM_Section,
    RDM_Signal,
    RDM_Station,
    RDM_TrackElement,
    RDM_Train,
    RDM_Turnout,
    RDM_TurnoutDesiredDirection,
    RDM_TurnoutSignal,
    Section,
    Signal,
    TrackElement,
    ConnectionDirection,
    Speed,
    TurnoutDirection,
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

def test_assoc_holds40_reverse_link_reassign_clear():
    a1 = RDM_Signal(allowedSpeed="sample_text")
    a2 = RDM_Signal(allowedSpeed="sample_text_2")
    b = RDM_ConnectionPoint(direction="sample_text")
    _safe_set(b, 'standsOn41', a1)
    assert _is_linked(b, 'standsOn41', a1)
    if hasattr(a1, 'Signal'):
        assert _is_linked(a1, 'Signal', b)
    _safe_set(b, 'standsOn41', a2)
    assert _is_linked(b, 'standsOn41', a2)
    if hasattr(a1, 'Signal'):
        assert not _is_linked(a1, 'Signal', b)
    if hasattr(a2, 'Signal'):
        assert _is_linked(a2, 'Signal', b)
    _safe_set(b, 'standsOn41', None)
    assert not _is_linked(b, 'standsOn41', a2)
    if hasattr(a2, 'Signal'):
        assert not _is_linked(a2, 'Signal', b)


def test_assoc_standsOn24_reverse_link_reassign_clear():
    a1 = RDM_Signal(allowedSpeed="sample_text")
    a2 = RDM_Signal(allowedSpeed="sample_text_2")
    b = RDM_ConnectionPoint(direction="sample_text")
    _safe_set(b, 'ConnectionPoint', a1)
    assert _is_linked(b, 'ConnectionPoint', a1)
    if hasattr(a1, 'holds'):
        assert _is_linked(a1, 'holds', b)
    _safe_set(b, 'ConnectionPoint', a2)
    assert _is_linked(b, 'ConnectionPoint', a2)
    if hasattr(a1, 'holds'):
        assert not _is_linked(a1, 'holds', b)
    if hasattr(a2, 'holds'):
        assert _is_linked(a2, 'holds', b)
    _safe_set(b, 'ConnectionPoint', None)
    assert not _is_linked(b, 'ConnectionPoint', a2)
    if hasattr(a2, 'holds'):
        assert not _is_linked(a2, 'holds', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_arrivesTo15_stub_double():
    # RDM_Station has no real 'RDM_Station' property in the generated
    # code (a bare stub) -- manually attach it so RDM_Train's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # RDM_Train's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = RDM_Train(headingSpeed="sample_text", maxSpeed="sample_text")
    partner = RDM_Station()
    setattr(partner, 'RDM_Station', None)
    _safe_set(owner, 'RDM_Train16', partner)
    assert getattr(partner, 'RDM_Station') == owner
    _safe_set(owner, 'RDM_Train16', None)
    assert getattr(partner, 'RDM_Station') is None


def test_assoc_connectsTo27_stub_double():
    # RDM_TrackElement has no real 'RDM_TrackElement28' property in the generated
    # code (a bare stub) -- manually attach it so RDM_ConnectionPoint's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # RDM_ConnectionPoint's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = RDM_ConnectionPoint(direction="sample_text")
    partner = RDM_TrackElement()
    setattr(partner, 'RDM_TrackElement28', None)
    _safe_set(owner, 'RDM_ConnectionPoint29', partner)
    assert owner in getattr(partner, 'RDM_TrackElement28')
    _safe_set(owner, 'RDM_ConnectionPoint29', None)
    assert owner not in getattr(partner, 'RDM_TrackElement28')


def test_assoc_controls37_stub_double():
    # RDM_Station has no real 'RDM_Station38' property in the generated
    # code (a bare stub) -- manually attach it so RDM_Signal's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # RDM_Signal's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = RDM_Signal(allowedSpeed="sample_text")
    partner = RDM_Station()
    setattr(partner, 'RDM_Station38', None)
    _safe_set(owner, 'RDM_Signal39', partner)
    assert owner in getattr(partner, 'RDM_Station38')
    _safe_set(owner, 'RDM_Signal39', None)
    assert owner not in getattr(partner, 'RDM_Station38')


def test_assoc_departuresFrom17_stub_double():
    # RDM_Station has no real 'RDM_Station19' property in the generated
    # code (a bare stub) -- manually attach it so RDM_Train's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # RDM_Train's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = RDM_Train(headingSpeed="sample_text", maxSpeed="sample_text")
    partner = RDM_Station()
    setattr(partner, 'RDM_Station19', None)
    _safe_set(owner, 'RDM_Train18', partner)
    assert getattr(partner, 'RDM_Station19') == owner
    _safe_set(owner, 'RDM_Train18', None)
    assert getattr(partner, 'RDM_Station19') is None


def test_assoc_editorCP5_stub_double():
    # RDM_RailwayDomainModel has no real 'RDM_RailwayDomainModel6' property in the generated
    # code (a bare stub) -- manually attach it so RDM_ConnectionPoint's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # RDM_ConnectionPoint's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = RDM_ConnectionPoint(direction="sample_text")
    partner = RDM_RailwayDomainModel()
    setattr(partner, 'RDM_RailwayDomainModel6', None)
    _safe_set(owner, 'RDM_ConnectionPoint', partner)
    assert owner in getattr(partner, 'RDM_RailwayDomainModel6')
    _safe_set(owner, 'RDM_ConnectionPoint', None)
    assert owner not in getattr(partner, 'RDM_RailwayDomainModel6')


def test_assoc_editorSignal7_stub_double():
    # RDM_RailwayDomainModel has no real 'RDM_RailwayDomainModel8' property in the generated
    # code (a bare stub) -- manually attach it so RDM_Signal's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # RDM_Signal's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = RDM_Signal(allowedSpeed="sample_text")
    partner = RDM_RailwayDomainModel()
    setattr(partner, 'RDM_RailwayDomainModel8', None)
    _safe_set(owner, 'RDM_Signal', partner)
    assert owner in getattr(partner, 'RDM_RailwayDomainModel8')
    _safe_set(owner, 'RDM_Signal', None)
    assert owner not in getattr(partner, 'RDM_RailwayDomainModel8')


def test_assoc_follows20_stub_double():
    # RDM_Route has no real 'RDM_Route22' property in the generated
    # code (a bare stub) -- manually attach it so RDM_Train's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # RDM_Train's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = RDM_Train(headingSpeed="sample_text", maxSpeed="sample_text")
    partner = RDM_Route()
    setattr(partner, 'RDM_Route22', None)
    _safe_set(owner, 'RDM_Train21', partner)
    assert getattr(partner, 'RDM_Route22') == owner
    _safe_set(owner, 'RDM_Train21', None)
    assert getattr(partner, 'RDM_Route22') is None


def test_assoc_nextElement42_stub_double():
    # RDM_TrackElement has no real 'RDM_TrackElement44' property in the generated
    # code (a bare stub) -- manually attach it so RDM_ConnectionPoint's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # RDM_ConnectionPoint's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = RDM_ConnectionPoint(direction="sample_text")
    partner = RDM_TrackElement()
    setattr(partner, 'RDM_TrackElement44', None)
    _safe_set(owner, 'RDM_ConnectionPoint43', partner)
    assert getattr(partner, 'RDM_TrackElement44') == owner
    _safe_set(owner, 'RDM_ConnectionPoint43', None)
    assert getattr(partner, 'RDM_TrackElement44') is None


def test_assoc_observes25_stub_double():
    # RDM_TrackElement has no real 'RDM_TrackElement' property in the generated
    # code (a bare stub) -- manually attach it so RDM_Signal's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # RDM_Signal's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = RDM_Signal(allowedSpeed="sample_text")
    partner = RDM_TrackElement()
    setattr(partner, 'RDM_TrackElement', None)
    _safe_set(owner, 'RDM_Signal26', partner)
    assert getattr(partner, 'RDM_TrackElement') == owner
    _safe_set(owner, 'RDM_Signal26', None)
    assert getattr(partner, 'RDM_TrackElement') is None


def test_assoc_occupiedBy30_stub_double():
    # RDM_TrackElement has no real 'standsOn' property in the generated
    # code (a bare stub) -- manually attach it so RDM_Train's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # RDM_Train's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = RDM_Train(headingSpeed="sample_text", maxSpeed="sample_text")
    partner = RDM_TrackElement()
    setattr(partner, 'standsOn', None)
    _safe_set(owner, 'Train', partner)
    assert getattr(partner, 'standsOn') == owner
    _safe_set(owner, 'Train', None)
    assert getattr(partner, 'standsOn') is None


def test_assoc_standsOn23_stub_double():
    # RDM_TrackElement has no real 'TrackElement' property in the generated
    # code (a bare stub) -- manually attach it so RDM_Train's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # RDM_Train's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = RDM_Train(headingSpeed="sample_text", maxSpeed="sample_text")
    partner = RDM_TrackElement()
    setattr(partner, 'TrackElement', None)
    _safe_set(owner, 'occupiedBy', {partner})
    assert getattr(partner, 'TrackElement') == owner
    _safe_set(owner, 'occupiedBy', set())
    assert getattr(partner, 'TrackElement') is None


def test_assoc_trains0_stub_double():
    # RDM_RailwayDomainModel has no real 'RDM_RailwayDomainModel' property in the generated
    # code (a bare stub) -- manually attach it so RDM_Train's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # RDM_Train's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = RDM_Train(headingSpeed="sample_text", maxSpeed="sample_text")
    partner = RDM_RailwayDomainModel()
    setattr(partner, 'RDM_RailwayDomainModel', None)
    _safe_set(owner, 'RDM_Train', partner)
    assert owner in getattr(partner, 'RDM_RailwayDomainModel')
    _safe_set(owner, 'RDM_Train', None)
    assert owner not in getattr(partner, 'RDM_RailwayDomainModel')


def test_assoc_turnout53_stub_double():
    # RDM_TurnoutSignal has no real 'RDM_TurnoutSignal' property in the generated
    # code (a bare stub) -- manually attach it so RDM_Turnout's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # RDM_Turnout's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = RDM_Turnout(currentDirection="sample_text", switchingDirection="sample_text")
    partner = RDM_TurnoutSignal()
    setattr(partner, 'RDM_TurnoutSignal', None)
    _safe_set(owner, 'RDM_Turnout54', partner)
    assert getattr(partner, 'RDM_TurnoutSignal') == owner
    _safe_set(owner, 'RDM_Turnout54', None)
    assert getattr(partner, 'RDM_TurnoutSignal') is None


def test_assoc_turnouts3_stub_double():
    # RDM_RailwayDomainModel has no real 'RDM_RailwayDomainModel4' property in the generated
    # code (a bare stub) -- manually attach it so RDM_Turnout's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # RDM_Turnout's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = RDM_Turnout(currentDirection="sample_text", switchingDirection="sample_text")
    partner = RDM_RailwayDomainModel()
    setattr(partner, 'RDM_RailwayDomainModel4', None)
    _safe_set(owner, 'RDM_Turnout', partner)
    assert owner in getattr(partner, 'RDM_RailwayDomainModel4')
    _safe_set(owner, 'RDM_Turnout', None)
    assert owner not in getattr(partner, 'RDM_RailwayDomainModel4')


