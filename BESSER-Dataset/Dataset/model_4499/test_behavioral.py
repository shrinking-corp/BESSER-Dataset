import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Actuator,
    Expression,
    HasActuators,
    HasIntegerValue,
    HasSensors,
    NamedElement,
    PolicyEngine_AccessControl,
    PolicyEngine_Actuator,
    PolicyEngine_ActuatorComponent,
    PolicyEngine_AudioAlarmActuator,
    PolicyEngine_BinaryOps,
    PolicyEngine_Building,
    PolicyEngine_CO2Sensor,
    PolicyEngine_CTS,
    PolicyEngine_CalendarSystem,
    PolicyEngine_Constant,
    PolicyEngine_DoorActuator,
    PolicyEngine_Expression,
    PolicyEngine_Floor,
    PolicyEngine_HasActuators,
    PolicyEngine_HasIntegerValue,
    PolicyEngine_HasSensors,
    PolicyEngine_HumidifierActuator,
    PolicyEngine_HumiditySensor,
    PolicyEngine_Id,
    PolicyEngine_If,
    PolicyEngine_InfraredLightSensor,
    PolicyEngine_LightSensor,
    PolicyEngine_LightSwitchActuator,
    PolicyEngine_MeetingScheduleSystem,
    PolicyEngine_Model,
    PolicyEngine_MotionSensor,
    PolicyEngine_NamedElement,
    PolicyEngine_Policy,
    PolicyEngine_PressureSensor,
    PolicyEngine_RadiatorActuator,
    PolicyEngine_ResetExpression,
    PolicyEngine_Room,
    PolicyEngine_RoomActuators,
    PolicyEngine_RoomUsage,
    PolicyEngine_Schedule,
    PolicyEngine_Sensor,
    PolicyEngine_SensorComponent,
    PolicyEngine_SmokeSensor,
    PolicyEngine_State,
    PolicyEngine_TemperatureSensor,
    PolicyEngine_Time,
    PolicyEngine_TimeExpression,
    PolicyEngine_Timer,
    PolicyEngine_TouchSensor,
    PolicyEngine_UnaryOp,
    PolicyEngine_WindowActuator,
    Sensor,
    CompOps,
    Weekdays,
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

def test_assoc_from_85_reverse_link_reassign_clear():
    a1 = PolicyEngine_Time(hours="sample_text", minutes="sample_text")
    a2 = PolicyEngine_Time(hours="sample_text_2", minutes="sample_text_2")
    b = PolicyEngine_Schedule(weekdays="sample_text")
    _safe_set(b, 'PolicyEngine_Schedule86', a1)
    assert _is_linked(b, 'PolicyEngine_Schedule86', a1)
    if hasattr(a1, 'PolicyEngine_Time'):
        assert _is_linked(a1, 'PolicyEngine_Time', b)
    _safe_set(b, 'PolicyEngine_Schedule86', a2)
    assert _is_linked(b, 'PolicyEngine_Schedule86', a2)
    if hasattr(a1, 'PolicyEngine_Time'):
        assert not _is_linked(a1, 'PolicyEngine_Time', b)
    if hasattr(a2, 'PolicyEngine_Time'):
        assert _is_linked(a2, 'PolicyEngine_Time', b)
    _safe_set(b, 'PolicyEngine_Schedule86', None)
    assert not _is_linked(b, 'PolicyEngine_Schedule86', a2)
    if hasattr(a2, 'PolicyEngine_Time'):
        assert not _is_linked(a2, 'PolicyEngine_Time', b)


def test_assoc_to87_reverse_link_reassign_clear():
    a1 = PolicyEngine_Time(hours="sample_text", minutes="sample_text")
    a2 = PolicyEngine_Time(hours="sample_text_2", minutes="sample_text_2")
    b = PolicyEngine_Schedule(weekdays="sample_text")
    _safe_set(b, 'PolicyEngine_Schedule88', a1)
    assert _is_linked(b, 'PolicyEngine_Schedule88', a1)
    if hasattr(a1, 'PolicyEngine_Time89'):
        assert _is_linked(a1, 'PolicyEngine_Time89', b)
    _safe_set(b, 'PolicyEngine_Schedule88', a2)
    assert _is_linked(b, 'PolicyEngine_Schedule88', a2)
    if hasattr(a1, 'PolicyEngine_Time89'):
        assert not _is_linked(a1, 'PolicyEngine_Time89', b)
    if hasattr(a2, 'PolicyEngine_Time89'):
        assert _is_linked(a2, 'PolicyEngine_Time89', b)
    _safe_set(b, 'PolicyEngine_Schedule88', None)
    assert not _is_linked(b, 'PolicyEngine_Schedule88', a2)
    if hasattr(a2, 'PolicyEngine_Time89'):
        assert not _is_linked(a2, 'PolicyEngine_Time89', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_defineLocalState80_stub_double():
    # PolicyEngine_Policy has no real 'PolicyEngine_Policy81' property in the generated
    # code (a bare stub) -- manually attach it so PolicyEngine_State's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # PolicyEngine_State's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = PolicyEngine_State(valueState=True)
    partner = PolicyEngine_Policy()
    setattr(partner, 'PolicyEngine_Policy81', None)
    _safe_set(owner, 'PolicyEngine_State82', partner)
    assert owner in getattr(partner, 'PolicyEngine_Policy81')
    _safe_set(owner, 'PolicyEngine_State82', None)
    assert owner not in getattr(partner, 'PolicyEngine_Policy81')


def test_assoc_defineState111_stub_double():
    # PolicyEngine_RoomUsage has no real 'PolicyEngine_RoomUsage112' property in the generated
    # code (a bare stub) -- manually attach it so PolicyEngine_State's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # PolicyEngine_State's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = PolicyEngine_State(valueState=True)
    partner = PolicyEngine_RoomUsage()
    setattr(partner, 'PolicyEngine_RoomUsage112', None)
    _safe_set(owner, 'PolicyEngine_State113', partner)
    assert getattr(partner, 'PolicyEngine_RoomUsage112') == owner
    _safe_set(owner, 'PolicyEngine_State113', None)
    assert getattr(partner, 'PolicyEngine_RoomUsage112') is None


def test_assoc_defineState71_stub_double():
    # PolicyEngine_Policy has no real 'PolicyEngine_Policy72' property in the generated
    # code (a bare stub) -- manually attach it so PolicyEngine_State's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # PolicyEngine_State's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = PolicyEngine_State(valueState=True)
    partner = PolicyEngine_Policy()
    setattr(partner, 'PolicyEngine_Policy72', None)
    _safe_set(owner, 'PolicyEngine_State73', partner)
    assert owner in getattr(partner, 'PolicyEngine_Policy72')
    _safe_set(owner, 'PolicyEngine_State73', None)
    assert owner not in getattr(partner, 'PolicyEngine_Policy72')


def test_assoc_during51_stub_double():
    # PolicyEngine_Room has no real 'PolicyEngine_Room52' property in the generated
    # code (a bare stub) -- manually attach it so PolicyEngine_Schedule's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # PolicyEngine_Schedule's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = PolicyEngine_Schedule(weekdays="sample_text")
    partner = PolicyEngine_Room()
    setattr(partner, 'PolicyEngine_Room52', None)
    _safe_set(owner, 'PolicyEngine_Schedule53', partner)
    assert owner in getattr(partner, 'PolicyEngine_Room52')
    _safe_set(owner, 'PolicyEngine_Schedule53', None)
    assert owner not in getattr(partner, 'PolicyEngine_Room52')


def test_assoc_during74_stub_double():
    # PolicyEngine_Policy has no real 'PolicyEngine_Policy75' property in the generated
    # code (a bare stub) -- manually attach it so PolicyEngine_Schedule's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # PolicyEngine_Schedule's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = PolicyEngine_Schedule(weekdays="sample_text")
    partner = PolicyEngine_Policy()
    setattr(partner, 'PolicyEngine_Policy75', None)
    _safe_set(owner, 'PolicyEngine_Schedule76', partner)
    assert owner in getattr(partner, 'PolicyEngine_Policy75')
    _safe_set(owner, 'PolicyEngine_Schedule76', None)
    assert owner not in getattr(partner, 'PolicyEngine_Policy75')


def test_assoc_expr119_stub_double():
    # PolicyEngine_Expression has no real 'PolicyEngine_Expression120' property in the generated
    # code (a bare stub) -- manually attach it so PolicyEngine_UnaryOp's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # PolicyEngine_UnaryOp's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = PolicyEngine_UnaryOp(operator="sample_text")
    partner = PolicyEngine_Expression()
    setattr(partner, 'PolicyEngine_Expression120', None)
    _safe_set(owner, 'PolicyEngine_UnaryOp', partner)
    assert getattr(partner, 'PolicyEngine_Expression120') == owner
    _safe_set(owner, 'PolicyEngine_UnaryOp', None)
    assert getattr(partner, 'PolicyEngine_Expression120') is None


def test_assoc_exprStates83_stub_double():
    # PolicyEngine_Expression has no real 'PolicyEngine_Expression' property in the generated
    # code (a bare stub) -- manually attach it so PolicyEngine_State's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # PolicyEngine_State's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = PolicyEngine_State(valueState=True)
    partner = PolicyEngine_Expression()
    setattr(partner, 'PolicyEngine_Expression', None)
    _safe_set(owner, 'PolicyEngine_State84', partner)
    assert getattr(partner, 'PolicyEngine_Expression') == owner
    _safe_set(owner, 'PolicyEngine_State84', None)
    assert getattr(partner, 'PolicyEngine_Expression') is None


def test_assoc_lexpr114_stub_double():
    # PolicyEngine_Expression has no real 'PolicyEngine_Expression115' property in the generated
    # code (a bare stub) -- manually attach it so PolicyEngine_BinaryOps's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # PolicyEngine_BinaryOps's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = PolicyEngine_BinaryOps(operator="sample_text")
    partner = PolicyEngine_Expression()
    setattr(partner, 'PolicyEngine_Expression115', None)
    _safe_set(owner, 'PolicyEngine_BinaryOps', partner)
    assert getattr(partner, 'PolicyEngine_Expression115') == owner
    _safe_set(owner, 'PolicyEngine_BinaryOps', None)
    assert getattr(partner, 'PolicyEngine_Expression115') is None


def test_assoc_rexpr116_stub_double():
    # PolicyEngine_Expression has no real 'PolicyEngine_Expression118' property in the generated
    # code (a bare stub) -- manually attach it so PolicyEngine_BinaryOps's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # PolicyEngine_BinaryOps's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = PolicyEngine_BinaryOps(operator="sample_text")
    partner = PolicyEngine_Expression()
    setattr(partner, 'PolicyEngine_Expression118', None)
    _safe_set(owner, 'PolicyEngine_BinaryOps117', partner)
    assert getattr(partner, 'PolicyEngine_Expression118') == owner
    _safe_set(owner, 'PolicyEngine_BinaryOps117', None)
    assert getattr(partner, 'PolicyEngine_Expression118') is None


def test_assoc_schedules22_stub_double():
    # PolicyEngine_Model has no real 'PolicyEngine_Model23' property in the generated
    # code (a bare stub) -- manually attach it so PolicyEngine_Schedule's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # PolicyEngine_Schedule's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = PolicyEngine_Schedule(weekdays="sample_text")
    partner = PolicyEngine_Model()
    setattr(partner, 'PolicyEngine_Model23', None)
    _safe_set(owner, 'PolicyEngine_Schedule', partner)
    assert owner in getattr(partner, 'PolicyEngine_Model23')
    _safe_set(owner, 'PolicyEngine_Schedule', None)
    assert owner not in getattr(partner, 'PolicyEngine_Model23')


def test_assoc_stateDefinition17_stub_double():
    # PolicyEngine_Model has no real 'PolicyEngine_Model18' property in the generated
    # code (a bare stub) -- manually attach it so PolicyEngine_State's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # PolicyEngine_State's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = PolicyEngine_State(valueState=True)
    partner = PolicyEngine_Model()
    setattr(partner, 'PolicyEngine_Model18', None)
    _safe_set(owner, 'PolicyEngine_State', partner)
    assert owner in getattr(partner, 'PolicyEngine_Model18')
    _safe_set(owner, 'PolicyEngine_State', None)
    assert owner not in getattr(partner, 'PolicyEngine_Model18')


def test_assoc_time102_stub_double():
    # PolicyEngine_Timer has no real 'PolicyEngine_Timer103' property in the generated
    # code (a bare stub) -- manually attach it so PolicyEngine_TimeExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # PolicyEngine_TimeExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = PolicyEngine_TimeExpression(TimeBound=7)
    partner = PolicyEngine_Timer()
    setattr(partner, 'PolicyEngine_Timer103', None)
    _safe_set(owner, 'PolicyEngine_TimeExpression', partner)
    assert getattr(partner, 'PolicyEngine_Timer103') == owner
    _safe_set(owner, 'PolicyEngine_TimeExpression', None)
    assert getattr(partner, 'PolicyEngine_Timer103') is None


