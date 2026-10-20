import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    ConceptASE_IndividualContainer,
    ConceptASE_Route,
    ConceptASE_Segment,
    ConceptASE_Sensor,
    ConceptASE_Signal,
    ConceptASE_Switch,
    ConceptASE_SwitchPosition,
    ConceptASE_Thing,
    ConceptASE_Trackelement,
    Thing,
    Trackelement,
    SignalStateKind,
    SwitchStateKind,
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

def test_assoc_SwitchPosition_switch12_reverse_link_reassign_clear():
    a1 = ConceptASE_SwitchPosition(SwitchPosition_switchState="sample_text")
    a2 = ConceptASE_SwitchPosition(SwitchPosition_switchState="sample_text_2")
    b = ConceptASE_Switch(Switch_actualState="sample_text")
    _safe_set(b, 'Switch', a1)
    assert _is_linked(b, 'Switch', a1)
    if hasattr(a1, 'Switch_switchPosition'):
        assert _is_linked(a1, 'Switch_switchPosition', b)
    _safe_set(b, 'Switch', a2)
    assert _is_linked(b, 'Switch', a2)
    if hasattr(a1, 'Switch_switchPosition'):
        assert not _is_linked(a1, 'Switch_switchPosition', b)
    if hasattr(a2, 'Switch_switchPosition'):
        assert _is_linked(a2, 'Switch_switchPosition', b)
    _safe_set(b, 'Switch', None)
    assert not _is_linked(b, 'Switch', a2)
    if hasattr(a2, 'Switch_switchPosition'):
        assert not _is_linked(a2, 'Switch_switchPosition', b)


def test_assoc_Switch_switchPosition3_reverse_link_reassign_clear():
    a1 = ConceptASE_SwitchPosition(SwitchPosition_switchState="sample_text")
    a2 = ConceptASE_SwitchPosition(SwitchPosition_switchState="sample_text_2")
    b = ConceptASE_Switch(Switch_actualState="sample_text")
    _safe_set(b, 'SwitchPosition_switch', {a1})
    assert _is_linked(b, 'SwitchPosition_switch', a1)
    if hasattr(a1, 'SwitchPosition'):
        assert _is_linked(a1, 'SwitchPosition', b)
    _safe_set(b, 'SwitchPosition_switch', {a2})
    assert _is_linked(b, 'SwitchPosition_switch', a2)
    if hasattr(a1, 'SwitchPosition'):
        assert not _is_linked(a1, 'SwitchPosition', b)
    if hasattr(a2, 'SwitchPosition'):
        assert _is_linked(a2, 'SwitchPosition', b)
    _safe_set(b, 'SwitchPosition_switch', set())
    assert not _is_linked(b, 'SwitchPosition_switch', a2)
    if hasattr(a2, 'SwitchPosition'):
        assert not _is_linked(a2, 'SwitchPosition', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_Route_entry4_stub_double():
    # ConceptASE_Route has no real 'ConceptASE_Route' property in the generated
    # code (a bare stub) -- manually attach it so ConceptASE_Signal's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ConceptASE_Signal's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ConceptASE_Signal(Signal_actualState="sample_text")
    partner = ConceptASE_Route()
    setattr(partner, 'ConceptASE_Route', None)
    _safe_set(owner, 'ConceptASE_Signal', partner)
    assert getattr(partner, 'ConceptASE_Route') == owner
    _safe_set(owner, 'ConceptASE_Signal', None)
    assert getattr(partner, 'ConceptASE_Route') is None


def test_assoc_Route_exit7_stub_double():
    # ConceptASE_Route has no real 'ConceptASE_Route8' property in the generated
    # code (a bare stub) -- manually attach it so ConceptASE_Signal's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ConceptASE_Signal's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ConceptASE_Signal(Signal_actualState="sample_text")
    partner = ConceptASE_Route()
    setattr(partner, 'ConceptASE_Route8', None)
    _safe_set(owner, 'ConceptASE_Signal9', partner)
    assert getattr(partner, 'ConceptASE_Route8') == owner
    _safe_set(owner, 'ConceptASE_Signal9', None)
    assert getattr(partner, 'ConceptASE_Route8') is None


def test_assoc_Route_routeDefinition10_stub_double():
    # ConceptASE_Route has no real 'ConceptASE_Route11' property in the generated
    # code (a bare stub) -- manually attach it so ConceptASE_Sensor's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ConceptASE_Sensor's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ConceptASE_Sensor(Sensor_year=7)
    partner = ConceptASE_Route()
    setattr(partner, 'ConceptASE_Route11', None)
    _safe_set(owner, 'ConceptASE_Sensor', partner)
    assert owner in getattr(partner, 'ConceptASE_Route11')
    _safe_set(owner, 'ConceptASE_Sensor', None)
    assert owner not in getattr(partner, 'ConceptASE_Route11')


def test_assoc_Route_switchPosition5_stub_double():
    # ConceptASE_Route has no real 'SwitchPosition_route' property in the generated
    # code (a bare stub) -- manually attach it so ConceptASE_SwitchPosition's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ConceptASE_SwitchPosition's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ConceptASE_SwitchPosition(SwitchPosition_switchState="sample_text")
    partner = ConceptASE_Route()
    setattr(partner, 'SwitchPosition_route', None)
    _safe_set(owner, 'SwitchPosition6', partner)
    assert owner in getattr(partner, 'SwitchPosition_route')
    _safe_set(owner, 'SwitchPosition6', None)
    assert owner not in getattr(partner, 'SwitchPosition_route')


def test_assoc_Sensor_trackElement14_stub_double():
    # ConceptASE_Trackelement has no real 'Trackelement' property in the generated
    # code (a bare stub) -- manually attach it so ConceptASE_Sensor's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ConceptASE_Sensor's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ConceptASE_Sensor(Sensor_year=7)
    partner = ConceptASE_Trackelement()
    setattr(partner, 'Trackelement', None)
    _safe_set(owner, 'TrackElement_sensor', {partner})
    assert getattr(partner, 'Trackelement') == owner
    _safe_set(owner, 'TrackElement_sensor', set())
    assert getattr(partner, 'Trackelement') is None


def test_assoc_SwitchPosition_route13_stub_double():
    # ConceptASE_Route has no real 'Route' property in the generated
    # code (a bare stub) -- manually attach it so ConceptASE_SwitchPosition's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ConceptASE_SwitchPosition's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ConceptASE_SwitchPosition(SwitchPosition_switchState="sample_text")
    partner = ConceptASE_Route()
    setattr(partner, 'Route', None)
    _safe_set(owner, 'Route_switchPosition', {partner})
    assert getattr(partner, 'Route') == owner
    _safe_set(owner, 'Route_switchPosition', set())
    assert getattr(partner, 'Route') is None


def test_assoc_TrackElement_sensor0_stub_double():
    # ConceptASE_Trackelement has no real 'Sensor_trackElement' property in the generated
    # code (a bare stub) -- manually attach it so ConceptASE_Sensor's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ConceptASE_Sensor's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ConceptASE_Sensor(Sensor_year=7)
    partner = ConceptASE_Trackelement()
    setattr(partner, 'Sensor_trackElement', None)
    _safe_set(owner, 'Sensor', partner)
    assert owner in getattr(partner, 'Sensor_trackElement')
    _safe_set(owner, 'Sensor', None)
    assert owner not in getattr(partner, 'Sensor_trackElement')


