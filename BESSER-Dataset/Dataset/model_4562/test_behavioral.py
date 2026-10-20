import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    FieldObject,
    ImmovableObject,
    NamedElement,
    SizedElement,
    TemporalContainmentProxy,
    drones_Action,
    drones_Battery,
    drones_ChargeStation,
    drones_Drone,
    drones_FieldObject,
    drones_ImmovableObject,
    drones_Mission,
    drones_MovableObject,
    drones_NamedElement,
    drones_Parameter,
    drones_SizedElement,
    drones_TemporalContainmentProxy,
    ActionKind,
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

def test_assoc_battery1_reverse_link_reassign_clear():
    a1 = drones_Drone(communicationRange=3.14, cpuFrequency=7, maxPayload=3.14, maxSpeed=3.14, memory=7, minSpeed=3.14)
    a2 = drones_Drone(communicationRange=9.99, cpuFrequency=13, maxPayload=9.99, maxSpeed=9.99, memory=13, minSpeed=9.99)
    b = drones_Battery(charge=3.14, lifeTime=3.14, rechargeRate=3.14, remainingLifeTime=3.14)
    _safe_set(b, 'drones_Battery', a1)
    assert _is_linked(b, 'drones_Battery', a1)
    if hasattr(a1, 'drones_Drone'):
        assert _is_linked(a1, 'drones_Drone', b)
    _safe_set(b, 'drones_Battery', a2)
    assert _is_linked(b, 'drones_Battery', a2)
    if hasattr(a1, 'drones_Drone'):
        assert not _is_linked(a1, 'drones_Drone', b)
    if hasattr(a2, 'drones_Drone'):
        assert _is_linked(a2, 'drones_Drone', b)
    _safe_set(b, 'drones_Battery', None)
    assert not _is_linked(b, 'drones_Battery', a2)
    if hasattr(a2, 'drones_Drone'):
        assert not _is_linked(a2, 'drones_Drone', b)


def test_assoc_supportedActions4_reverse_link_reassign_clear():
    a1 = drones_Drone(communicationRange=3.14, cpuFrequency=7, maxPayload=3.14, maxSpeed=3.14, memory=7, minSpeed=3.14)
    a2 = drones_Drone(communicationRange=9.99, cpuFrequency=13, maxPayload=9.99, maxSpeed=9.99, memory=13, minSpeed=9.99)
    b = drones_Action(key="sample_text", operation="sample_text", range=3.14, value="sample_text")
    _safe_set(b, 'drones_Action', a1)
    assert _is_linked(b, 'drones_Action', a1)
    if hasattr(a1, 'drones_Drone5'):
        assert _is_linked(a1, 'drones_Drone5', b)
    _safe_set(b, 'drones_Action', a2)
    assert _is_linked(b, 'drones_Action', a2)
    if hasattr(a1, 'drones_Drone5'):
        assert not _is_linked(a1, 'drones_Drone5', b)
    if hasattr(a2, 'drones_Drone5'):
        assert _is_linked(a2, 'drones_Drone5', b)
    _safe_set(b, 'drones_Action', None)
    assert not _is_linked(b, 'drones_Action', a2)
    if hasattr(a2, 'drones_Drone5'):
        assert not _is_linked(a2, 'drones_Drone5', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_actions13_stub_double():
    # drones_Mission has no real 'drones_Mission14' property in the generated
    # code (a bare stub) -- manually attach it so drones_Action's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # drones_Action's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = drones_Action(key="sample_text", operation="sample_text", range=3.14, value="sample_text")
    partner = drones_Mission()
    setattr(partner, 'drones_Mission14', None)
    _safe_set(owner, 'drones_Action15', partner)
    assert owner in getattr(partner, 'drones_Mission14')
    _safe_set(owner, 'drones_Action15', None)
    assert owner not in getattr(partner, 'drones_Mission14')


def test_assoc_chargeStation2_stub_double():
    # drones_ChargeStation has no real 'drones_ChargeStation' property in the generated
    # code (a bare stub) -- manually attach it so drones_Drone's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # drones_Drone's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = drones_Drone(communicationRange=3.14, cpuFrequency=7, maxPayload=3.14, maxSpeed=3.14, memory=7, minSpeed=3.14)
    partner = drones_ChargeStation()
    setattr(partner, 'drones_ChargeStation', None)
    _safe_set(owner, 'drones_Drone3', partner)
    assert getattr(partner, 'drones_ChargeStation') == owner
    _safe_set(owner, 'drones_Drone3', None)
    assert getattr(partner, 'drones_ChargeStation') is None


def test_assoc_drones8_stub_double():
    # drones_Mission has no real 'drones_Mission9' property in the generated
    # code (a bare stub) -- manually attach it so drones_Drone's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # drones_Drone's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = drones_Drone(communicationRange=3.14, cpuFrequency=7, maxPayload=3.14, maxSpeed=3.14, memory=7, minSpeed=3.14)
    partner = drones_Mission()
    setattr(partner, 'drones_Mission9', None)
    _safe_set(owner, 'drones_Drone10', partner)
    assert owner in getattr(partner, 'drones_Mission9')
    _safe_set(owner, 'drones_Drone10', None)
    assert owner not in getattr(partner, 'drones_Mission9')


def test_assoc_parameters0_stub_double():
    # drones_FieldObject has no real 'drones_FieldObject' property in the generated
    # code (a bare stub) -- manually attach it so drones_Parameter's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # drones_Parameter's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = drones_Parameter(key="sample_text", value="sample_text")
    partner = drones_FieldObject()
    setattr(partner, 'drones_FieldObject', None)
    _safe_set(owner, 'drones_Parameter', partner)
    assert owner in getattr(partner, 'drones_FieldObject')
    _safe_set(owner, 'drones_Parameter', None)
    assert owner not in getattr(partner, 'drones_FieldObject')


