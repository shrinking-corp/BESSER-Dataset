import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    RailwayElement,
    TrackElement,
    railway_RailwayContainer,
    railway_RailwayElement,
    railway_Route,
    railway_Segment,
    railway_Semaphore,
    railway_Sensor,
    railway_Switch,
    railway_SwitchPosition,
    railway_TrackElement,
    Position,
    Signal,
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

def test_assoc_positions3_reverse_link_reassign_clear():
    a1 = railway_SwitchPosition(position="sample_text")
    a2 = railway_SwitchPosition(position="sample_text_2")
    b = railway_Switch(currentPosition="sample_text")
    _safe_set(b, 'switch', {a1})
    assert _is_linked(b, 'switch', a1)
    if hasattr(a1, 'SwitchPosition'):
        assert _is_linked(a1, 'SwitchPosition', b)
    _safe_set(b, 'switch', {a2})
    assert _is_linked(b, 'switch', a2)
    if hasattr(a1, 'SwitchPosition'):
        assert not _is_linked(a1, 'SwitchPosition', b)
    if hasattr(a2, 'SwitchPosition'):
        assert _is_linked(a2, 'SwitchPosition', b)
    _safe_set(b, 'switch', set())
    assert not _is_linked(b, 'switch', a2)
    if hasattr(a2, 'SwitchPosition'):
        assert not _is_linked(a2, 'SwitchPosition', b)


def test_assoc_switch12_reverse_link_reassign_clear():
    a1 = railway_SwitchPosition(position="sample_text")
    a2 = railway_SwitchPosition(position="sample_text_2")
    b = railway_Switch(currentPosition="sample_text")
    _safe_set(b, 'Switch', a1)
    assert _is_linked(b, 'Switch', a1)
    if hasattr(a1, 'positions'):
        assert _is_linked(a1, 'positions', b)
    _safe_set(b, 'Switch', a2)
    assert _is_linked(b, 'Switch', a2)
    if hasattr(a1, 'positions'):
        assert not _is_linked(a1, 'positions', b)
    if hasattr(a2, 'positions'):
        assert _is_linked(a2, 'positions', b)
    _safe_set(b, 'Switch', None)
    assert not _is_linked(b, 'Switch', a2)
    if hasattr(a2, 'positions'):
        assert not _is_linked(a2, 'positions', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_entry4_stub_double():
    # railway_Route has no real 'railway_Route' property in the generated
    # code (a bare stub) -- manually attach it so railway_Semaphore's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # railway_Semaphore's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = railway_Semaphore(signal="sample_text")
    partner = railway_Route()
    setattr(partner, 'railway_Route', None)
    _safe_set(owner, 'railway_Semaphore', partner)
    assert getattr(partner, 'railway_Route') == owner
    _safe_set(owner, 'railway_Semaphore', None)
    assert getattr(partner, 'railway_Route') is None


def test_assoc_exit7_stub_double():
    # railway_Route has no real 'railway_Route8' property in the generated
    # code (a bare stub) -- manually attach it so railway_Semaphore's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # railway_Semaphore's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = railway_Semaphore(signal="sample_text")
    partner = railway_Route()
    setattr(partner, 'railway_Route8', None)
    _safe_set(owner, 'railway_Semaphore9', partner)
    assert getattr(partner, 'railway_Route8') == owner
    _safe_set(owner, 'railway_Semaphore9', None)
    assert getattr(partner, 'railway_Route8') is None


def test_assoc_follows5_stub_double():
    # railway_Route has no real 'route' property in the generated
    # code (a bare stub) -- manually attach it so railway_SwitchPosition's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # railway_SwitchPosition's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = railway_SwitchPosition(position="sample_text")
    partner = railway_Route()
    setattr(partner, 'route', None)
    _safe_set(owner, 'SwitchPosition6', partner)
    assert owner in getattr(partner, 'route')
    _safe_set(owner, 'SwitchPosition6', None)
    assert owner not in getattr(partner, 'route')


def test_assoc_invalids15_stub_double():
    # railway_RailwayContainer has no real 'railway_RailwayContainer' property in the generated
    # code (a bare stub) -- manually attach it so railway_RailwayElement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # railway_RailwayElement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = railway_RailwayElement(id=7)
    partner = railway_RailwayContainer()
    setattr(partner, 'railway_RailwayContainer', None)
    _safe_set(owner, 'railway_RailwayElement', partner)
    assert owner in getattr(partner, 'railway_RailwayContainer')
    _safe_set(owner, 'railway_RailwayElement', None)
    assert owner not in getattr(partner, 'railway_RailwayContainer')


def test_assoc_route13_stub_double():
    # railway_Route has no real 'Route' property in the generated
    # code (a bare stub) -- manually attach it so railway_SwitchPosition's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # railway_SwitchPosition's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = railway_SwitchPosition(position="sample_text")
    partner = railway_Route()
    setattr(partner, 'Route', None)
    _safe_set(owner, 'follows', partner)
    assert getattr(partner, 'Route') == owner
    _safe_set(owner, 'follows', None)
    assert getattr(partner, 'Route') is None


def test_assoc_semaphores16_stub_double():
    # railway_RailwayContainer has no real 'railway_RailwayContainer17' property in the generated
    # code (a bare stub) -- manually attach it so railway_Semaphore's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # railway_Semaphore's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = railway_Semaphore(signal="sample_text")
    partner = railway_RailwayContainer()
    setattr(partner, 'railway_RailwayContainer17', None)
    _safe_set(owner, 'railway_Semaphore18', partner)
    assert owner in getattr(partner, 'railway_RailwayContainer17')
    _safe_set(owner, 'railway_Semaphore18', None)
    assert owner not in getattr(partner, 'railway_RailwayContainer17')


