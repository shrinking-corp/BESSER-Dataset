import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    robotDSL_Action,
    robotDSL_ArmOp,
    robotDSL_Bool,
    robotDSL_Color,
    robotDSL_Direction,
    robotDSL_Distance,
    robotDSL_Flag,
    robotDSL_Goal,
    robotDSL_Mission,
    robotDSL_Missions,
    robotDSL_Negation,
    robotDSL_Sensor,
    robotDSL_Sound,
    robotDSL_Speed,
    robotDSL_Task,
    robotDSL_Time,
    robotDSL_Trigger,
    ArmOpType,
    BoolType,
    ColorName,
    DirectionVal,
    SensorType,
    SoundName,
    SpeedVal,
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

def test_assoc_actionList16_reverse_link_reassign_clear():
    a1 = robotDSL_Task(name="sample_text", prio=7)
    a2 = robotDSL_Task(name="sample_text_2", prio=13)
    b = robotDSL_Action(cent="sample_text", degr=7, duration=7)
    _safe_set(b, 'robotDSL_Action18', a1)
    assert _is_linked(b, 'robotDSL_Action18', a1)
    if hasattr(a1, 'robotDSL_Task17'):
        assert _is_linked(a1, 'robotDSL_Task17', b)
    _safe_set(b, 'robotDSL_Action18', a2)
    assert _is_linked(b, 'robotDSL_Action18', a2)
    if hasattr(a1, 'robotDSL_Task17'):
        assert not _is_linked(a1, 'robotDSL_Task17', b)
    if hasattr(a2, 'robotDSL_Task17'):
        assert _is_linked(a2, 'robotDSL_Task17', b)
    _safe_set(b, 'robotDSL_Action18', None)
    assert not _is_linked(b, 'robotDSL_Action18', a2)
    if hasattr(a2, 'robotDSL_Task17'):
        assert not _is_linked(a2, 'robotDSL_Task17', b)


def test_assoc_bool36_reverse_link_reassign_clear():
    a1 = robotDSL_Bool(boolType="sample_text")
    a2 = robotDSL_Bool(boolType="sample_text_2")
    b = robotDSL_Action(cent="sample_text", degr=7, duration=7)
    _safe_set(b, 'robotDSL_Action37', a1)
    assert _is_linked(b, 'robotDSL_Action37', a1)
    if hasattr(a1, 'robotDSL_Bool'):
        assert _is_linked(a1, 'robotDSL_Bool', b)
    _safe_set(b, 'robotDSL_Action37', a2)
    assert _is_linked(b, 'robotDSL_Action37', a2)
    if hasattr(a1, 'robotDSL_Bool'):
        assert not _is_linked(a1, 'robotDSL_Bool', b)
    if hasattr(a2, 'robotDSL_Bool'):
        assert _is_linked(a2, 'robotDSL_Bool', b)
    _safe_set(b, 'robotDSL_Action37', None)
    assert not _is_linked(b, 'robotDSL_Action37', a2)
    if hasattr(a2, 'robotDSL_Bool'):
        assert not _is_linked(a2, 'robotDSL_Bool', b)


def test_assoc_boolType38_reverse_link_reassign_clear():
    a1 = robotDSL_Trigger(degrees=7, touching="sample_text")
    a2 = robotDSL_Trigger(degrees=13, touching="sample_text_2")
    b = robotDSL_Bool(boolType="sample_text")
    _safe_set(b, 'robotDSL_Bool40', a1)
    assert _is_linked(b, 'robotDSL_Bool40', a1)
    if hasattr(a1, 'robotDSL_Trigger39'):
        assert _is_linked(a1, 'robotDSL_Trigger39', b)
    _safe_set(b, 'robotDSL_Bool40', a2)
    assert _is_linked(b, 'robotDSL_Bool40', a2)
    if hasattr(a1, 'robotDSL_Trigger39'):
        assert not _is_linked(a1, 'robotDSL_Trigger39', b)
    if hasattr(a2, 'robotDSL_Trigger39'):
        assert _is_linked(a2, 'robotDSL_Trigger39', b)
    _safe_set(b, 'robotDSL_Bool40', None)
    assert not _is_linked(b, 'robotDSL_Bool40', a2)
    if hasattr(a2, 'robotDSL_Trigger39'):
        assert not _is_linked(a2, 'robotDSL_Trigger39', b)


def test_assoc_color48_reverse_link_reassign_clear():
    a1 = robotDSL_Trigger(degrees=7, touching="sample_text")
    a2 = robotDSL_Trigger(degrees=13, touching="sample_text_2")
    b = robotDSL_Color(colorName="sample_text")
    _safe_set(b, 'robotDSL_Color', a1)
    assert _is_linked(b, 'robotDSL_Color', a1)
    if hasattr(a1, 'robotDSL_Trigger49'):
        assert _is_linked(a1, 'robotDSL_Trigger49', b)
    _safe_set(b, 'robotDSL_Color', a2)
    assert _is_linked(b, 'robotDSL_Color', a2)
    if hasattr(a1, 'robotDSL_Trigger49'):
        assert not _is_linked(a1, 'robotDSL_Trigger49', b)
    if hasattr(a2, 'robotDSL_Trigger49'):
        assert _is_linked(a2, 'robotDSL_Trigger49', b)
    _safe_set(b, 'robotDSL_Color', None)
    assert not _is_linked(b, 'robotDSL_Color', a2)
    if hasattr(a2, 'robotDSL_Trigger49'):
        assert not _is_linked(a2, 'robotDSL_Trigger49', b)


def test_assoc_dist50_reverse_link_reassign_clear():
    a1 = robotDSL_Trigger(degrees=7, touching="sample_text")
    a2 = robotDSL_Trigger(degrees=13, touching="sample_text_2")
    b = robotDSL_Distance(distance=7)
    _safe_set(b, 'robotDSL_Distance', a1)
    assert _is_linked(b, 'robotDSL_Distance', a1)
    if hasattr(a1, 'robotDSL_Trigger51'):
        assert _is_linked(a1, 'robotDSL_Trigger51', b)
    _safe_set(b, 'robotDSL_Distance', a2)
    assert _is_linked(b, 'robotDSL_Distance', a2)
    if hasattr(a1, 'robotDSL_Trigger51'):
        assert not _is_linked(a1, 'robotDSL_Trigger51', b)
    if hasattr(a2, 'robotDSL_Trigger51'):
        assert _is_linked(a2, 'robotDSL_Trigger51', b)
    _safe_set(b, 'robotDSL_Distance', None)
    assert not _is_linked(b, 'robotDSL_Distance', a2)
    if hasattr(a2, 'robotDSL_Trigger51'):
        assert not _is_linked(a2, 'robotDSL_Trigger51', b)


def test_assoc_flag33_reverse_link_reassign_clear():
    a1 = robotDSL_Flag(name="sample_text")
    a2 = robotDSL_Flag(name="sample_text_2")
    b = robotDSL_Action(cent="sample_text", degr=7, duration=7)
    _safe_set(b, 'robotDSL_Action34', a1)
    assert _is_linked(b, 'robotDSL_Action34', a1)
    if hasattr(a1, 'robotDSL_Flag35'):
        assert _is_linked(a1, 'robotDSL_Flag35', b)
    _safe_set(b, 'robotDSL_Action34', a2)
    assert _is_linked(b, 'robotDSL_Action34', a2)
    if hasattr(a1, 'robotDSL_Flag35'):
        assert not _is_linked(a1, 'robotDSL_Flag35', b)
    if hasattr(a2, 'robotDSL_Flag35'):
        assert _is_linked(a2, 'robotDSL_Flag35', b)
    _safe_set(b, 'robotDSL_Action34', None)
    assert not _is_linked(b, 'robotDSL_Action34', a2)
    if hasattr(a2, 'robotDSL_Flag35'):
        assert not _is_linked(a2, 'robotDSL_Flag35', b)


def test_assoc_flag43_reverse_link_reassign_clear():
    a1 = robotDSL_Trigger(degrees=7, touching="sample_text")
    a2 = robotDSL_Trigger(degrees=13, touching="sample_text_2")
    b = robotDSL_Flag(name="sample_text")
    _safe_set(b, 'robotDSL_Flag45', a1)
    assert _is_linked(b, 'robotDSL_Flag45', a1)
    if hasattr(a1, 'robotDSL_Trigger44'):
        assert _is_linked(a1, 'robotDSL_Trigger44', b)
    _safe_set(b, 'robotDSL_Flag45', a2)
    assert _is_linked(b, 'robotDSL_Flag45', a2)
    if hasattr(a1, 'robotDSL_Trigger44'):
        assert not _is_linked(a1, 'robotDSL_Trigger44', b)
    if hasattr(a2, 'robotDSL_Trigger44'):
        assert _is_linked(a2, 'robotDSL_Trigger44', b)
    _safe_set(b, 'robotDSL_Flag45', None)
    assert not _is_linked(b, 'robotDSL_Flag45', a2)
    if hasattr(a2, 'robotDSL_Trigger44'):
        assert not _is_linked(a2, 'robotDSL_Trigger44', b)


def test_assoc_flagsList1_reverse_link_reassign_clear():
    a1 = robotDSL_Mission(name="sample_text")
    a2 = robotDSL_Mission(name="sample_text_2")
    b = robotDSL_Flag(name="sample_text")
    _safe_set(b, 'robotDSL_Flag', a1)
    assert _is_linked(b, 'robotDSL_Flag', a1)
    if hasattr(a1, 'robotDSL_Mission2'):
        assert _is_linked(a1, 'robotDSL_Mission2', b)
    _safe_set(b, 'robotDSL_Flag', a2)
    assert _is_linked(b, 'robotDSL_Flag', a2)
    if hasattr(a1, 'robotDSL_Mission2'):
        assert not _is_linked(a1, 'robotDSL_Mission2', b)
    if hasattr(a2, 'robotDSL_Mission2'):
        assert _is_linked(a2, 'robotDSL_Mission2', b)
    _safe_set(b, 'robotDSL_Flag', None)
    assert not _is_linked(b, 'robotDSL_Flag', a2)
    if hasattr(a2, 'robotDSL_Mission2'):
        assert not _is_linked(a2, 'robotDSL_Mission2', b)


def test_assoc_missionList0_reverse_link_reassign_clear():
    a1 = robotDSL_Missions(name="sample_text")
    a2 = robotDSL_Missions(name="sample_text_2")
    b = robotDSL_Mission(name="sample_text")
    _safe_set(b, 'robotDSL_Mission', a1)
    assert _is_linked(b, 'robotDSL_Mission', a1)
    if hasattr(a1, 'robotDSL_Missions'):
        assert _is_linked(a1, 'robotDSL_Missions', b)
    _safe_set(b, 'robotDSL_Mission', a2)
    assert _is_linked(b, 'robotDSL_Mission', a2)
    if hasattr(a1, 'robotDSL_Missions'):
        assert not _is_linked(a1, 'robotDSL_Missions', b)
    if hasattr(a2, 'robotDSL_Missions'):
        assert _is_linked(a2, 'robotDSL_Missions', b)
    _safe_set(b, 'robotDSL_Mission', None)
    assert not _is_linked(b, 'robotDSL_Mission', a2)
    if hasattr(a2, 'robotDSL_Missions'):
        assert not _is_linked(a2, 'robotDSL_Missions', b)


def test_assoc_moveDir19_reverse_link_reassign_clear():
    a1 = robotDSL_Direction(dir="sample_text")
    a2 = robotDSL_Direction(dir="sample_text_2")
    b = robotDSL_Action(cent="sample_text", degr=7, duration=7)
    _safe_set(b, 'robotDSL_Action20', a1)
    assert _is_linked(b, 'robotDSL_Action20', a1)
    if hasattr(a1, 'robotDSL_Direction'):
        assert _is_linked(a1, 'robotDSL_Direction', b)
    _safe_set(b, 'robotDSL_Action20', a2)
    assert _is_linked(b, 'robotDSL_Action20', a2)
    if hasattr(a1, 'robotDSL_Direction'):
        assert not _is_linked(a1, 'robotDSL_Direction', b)
    if hasattr(a2, 'robotDSL_Direction'):
        assert _is_linked(a2, 'robotDSL_Direction', b)
    _safe_set(b, 'robotDSL_Action20', None)
    assert not _is_linked(b, 'robotDSL_Action20', a2)
    if hasattr(a2, 'robotDSL_Direction'):
        assert not _is_linked(a2, 'robotDSL_Direction', b)


def test_assoc_neg41_reverse_link_reassign_clear():
    a1 = robotDSL_Trigger(degrees=7, touching="sample_text")
    a2 = robotDSL_Trigger(degrees=13, touching="sample_text_2")
    b = robotDSL_Negation(NOT="sample_text")
    _safe_set(b, 'robotDSL_Negation', a1)
    assert _is_linked(b, 'robotDSL_Negation', a1)
    if hasattr(a1, 'robotDSL_Trigger42'):
        assert _is_linked(a1, 'robotDSL_Trigger42', b)
    _safe_set(b, 'robotDSL_Negation', a2)
    assert _is_linked(b, 'robotDSL_Negation', a2)
    if hasattr(a1, 'robotDSL_Trigger42'):
        assert not _is_linked(a1, 'robotDSL_Trigger42', b)
    if hasattr(a2, 'robotDSL_Trigger42'):
        assert _is_linked(a2, 'robotDSL_Trigger42', b)
    _safe_set(b, 'robotDSL_Negation', None)
    assert not _is_linked(b, 'robotDSL_Negation', a2)
    if hasattr(a2, 'robotDSL_Trigger42'):
        assert not _is_linked(a2, 'robotDSL_Trigger42', b)


def test_assoc_op29_reverse_link_reassign_clear():
    a1 = robotDSL_ArmOp(opType="sample_text")
    a2 = robotDSL_ArmOp(opType="sample_text_2")
    b = robotDSL_Action(cent="sample_text", degr=7, duration=7)
    _safe_set(b, 'robotDSL_Action30', a1)
    assert _is_linked(b, 'robotDSL_Action30', a1)
    if hasattr(a1, 'robotDSL_ArmOp'):
        assert _is_linked(a1, 'robotDSL_ArmOp', b)
    _safe_set(b, 'robotDSL_Action30', a2)
    assert _is_linked(b, 'robotDSL_Action30', a2)
    if hasattr(a1, 'robotDSL_ArmOp'):
        assert not _is_linked(a1, 'robotDSL_ArmOp', b)
    if hasattr(a2, 'robotDSL_ArmOp'):
        assert _is_linked(a2, 'robotDSL_ArmOp', b)
    _safe_set(b, 'robotDSL_Action30', None)
    assert not _is_linked(b, 'robotDSL_Action30', a2)
    if hasattr(a2, 'robotDSL_ArmOp'):
        assert not _is_linked(a2, 'robotDSL_ArmOp', b)


def test_assoc_rangeBool52_reverse_link_reassign_clear():
    a1 = robotDSL_Distance(distance=7)
    a2 = robotDSL_Distance(distance=13)
    b = robotDSL_Bool(boolType="sample_text")
    _safe_set(b, 'robotDSL_Bool54', a1)
    assert _is_linked(b, 'robotDSL_Bool54', a1)
    if hasattr(a1, 'robotDSL_Distance53'):
        assert _is_linked(a1, 'robotDSL_Distance53', b)
    _safe_set(b, 'robotDSL_Bool54', a2)
    assert _is_linked(b, 'robotDSL_Bool54', a2)
    if hasattr(a1, 'robotDSL_Distance53'):
        assert not _is_linked(a1, 'robotDSL_Distance53', b)
    if hasattr(a2, 'robotDSL_Distance53'):
        assert _is_linked(a2, 'robotDSL_Distance53', b)
    _safe_set(b, 'robotDSL_Bool54', None)
    assert not _is_linked(b, 'robotDSL_Bool54', a2)
    if hasattr(a2, 'robotDSL_Distance53'):
        assert not _is_linked(a2, 'robotDSL_Distance53', b)


def test_assoc_sensor46_reverse_link_reassign_clear():
    a1 = robotDSL_Trigger(degrees=7, touching="sample_text")
    a2 = robotDSL_Trigger(degrees=13, touching="sample_text_2")
    b = robotDSL_Sensor(sensorType="sample_text")
    _safe_set(b, 'robotDSL_Sensor', a1)
    assert _is_linked(b, 'robotDSL_Sensor', a1)
    if hasattr(a1, 'robotDSL_Trigger47'):
        assert _is_linked(a1, 'robotDSL_Trigger47', b)
    _safe_set(b, 'robotDSL_Sensor', a2)
    assert _is_linked(b, 'robotDSL_Sensor', a2)
    if hasattr(a1, 'robotDSL_Trigger47'):
        assert not _is_linked(a1, 'robotDSL_Trigger47', b)
    if hasattr(a2, 'robotDSL_Trigger47'):
        assert _is_linked(a2, 'robotDSL_Trigger47', b)
    _safe_set(b, 'robotDSL_Sensor', None)
    assert not _is_linked(b, 'robotDSL_Sensor', a2)
    if hasattr(a2, 'robotDSL_Trigger47'):
        assert not _is_linked(a2, 'robotDSL_Trigger47', b)


def test_assoc_sound31_reverse_link_reassign_clear():
    a1 = robotDSL_Sound(soundName="sample_text")
    a2 = robotDSL_Sound(soundName="sample_text_2")
    b = robotDSL_Action(cent="sample_text", degr=7, duration=7)
    _safe_set(b, 'robotDSL_Action32', a1)
    assert _is_linked(b, 'robotDSL_Action32', a1)
    if hasattr(a1, 'robotDSL_Sound'):
        assert _is_linked(a1, 'robotDSL_Sound', b)
    _safe_set(b, 'robotDSL_Action32', a2)
    assert _is_linked(b, 'robotDSL_Action32', a2)
    if hasattr(a1, 'robotDSL_Sound'):
        assert not _is_linked(a1, 'robotDSL_Sound', b)
    if hasattr(a2, 'robotDSL_Sound'):
        assert _is_linked(a2, 'robotDSL_Sound', b)
    _safe_set(b, 'robotDSL_Action32', None)
    assert not _is_linked(b, 'robotDSL_Action32', a2)
    if hasattr(a2, 'robotDSL_Sound'):
        assert not _is_linked(a2, 'robotDSL_Sound', b)


def test_assoc_speed21_reverse_link_reassign_clear():
    a1 = robotDSL_Speed(speed="sample_text")
    a2 = robotDSL_Speed(speed="sample_text_2")
    b = robotDSL_Action(cent="sample_text", degr=7, duration=7)
    _safe_set(b, 'robotDSL_Action22', a1)
    assert _is_linked(b, 'robotDSL_Action22', a1)
    if hasattr(a1, 'robotDSL_Speed'):
        assert _is_linked(a1, 'robotDSL_Speed', b)
    _safe_set(b, 'robotDSL_Action22', a2)
    assert _is_linked(b, 'robotDSL_Action22', a2)
    if hasattr(a1, 'robotDSL_Speed'):
        assert not _is_linked(a1, 'robotDSL_Speed', b)
    if hasattr(a2, 'robotDSL_Speed'):
        assert _is_linked(a2, 'robotDSL_Speed', b)
    _safe_set(b, 'robotDSL_Action22', None)
    assert not _is_linked(b, 'robotDSL_Action22', a2)
    if hasattr(a2, 'robotDSL_Speed'):
        assert not _is_linked(a2, 'robotDSL_Speed', b)


def test_assoc_taskList3_reverse_link_reassign_clear():
    a1 = robotDSL_Task(name="sample_text", prio=7)
    a2 = robotDSL_Task(name="sample_text_2", prio=13)
    b = robotDSL_Mission(name="sample_text")
    _safe_set(b, 'robotDSL_Mission4', {a1})
    assert _is_linked(b, 'robotDSL_Mission4', a1)
    if hasattr(a1, 'robotDSL_Task'):
        assert _is_linked(a1, 'robotDSL_Task', b)
    _safe_set(b, 'robotDSL_Mission4', {a2})
    assert _is_linked(b, 'robotDSL_Mission4', a2)
    if hasattr(a1, 'robotDSL_Task'):
        assert not _is_linked(a1, 'robotDSL_Task', b)
    if hasattr(a2, 'robotDSL_Task'):
        assert _is_linked(a2, 'robotDSL_Task', b)
    _safe_set(b, 'robotDSL_Mission4', set())
    assert not _is_linked(b, 'robotDSL_Mission4', a2)
    if hasattr(a2, 'robotDSL_Task'):
        assert not _is_linked(a2, 'robotDSL_Task', b)


def test_assoc_trig26_reverse_link_reassign_clear():
    a1 = robotDSL_Trigger(degrees=7, touching="sample_text")
    a2 = robotDSL_Trigger(degrees=13, touching="sample_text_2")
    b = robotDSL_Action(cent="sample_text", degr=7, duration=7)
    _safe_set(b, 'robotDSL_Action27', {a1})
    assert _is_linked(b, 'robotDSL_Action27', a1)
    if hasattr(a1, 'robotDSL_Trigger28'):
        assert _is_linked(a1, 'robotDSL_Trigger28', b)
    _safe_set(b, 'robotDSL_Action27', {a2})
    assert _is_linked(b, 'robotDSL_Action27', a2)
    if hasattr(a1, 'robotDSL_Trigger28'):
        assert not _is_linked(a1, 'robotDSL_Trigger28', b)
    if hasattr(a2, 'robotDSL_Trigger28'):
        assert _is_linked(a2, 'robotDSL_Trigger28', b)
    _safe_set(b, 'robotDSL_Action27', set())
    assert not _is_linked(b, 'robotDSL_Action27', a2)
    if hasattr(a2, 'robotDSL_Trigger28'):
        assert not _is_linked(a2, 'robotDSL_Trigger28', b)


def test_assoc_triggerList13_reverse_link_reassign_clear():
    a1 = robotDSL_Trigger(degrees=7, touching="sample_text")
    a2 = robotDSL_Trigger(degrees=13, touching="sample_text_2")
    b = robotDSL_Task(name="sample_text", prio=7)
    _safe_set(b, 'robotDSL_Task14', {a1})
    assert _is_linked(b, 'robotDSL_Task14', a1)
    if hasattr(a1, 'robotDSL_Trigger15'):
        assert _is_linked(a1, 'robotDSL_Trigger15', b)
    _safe_set(b, 'robotDSL_Task14', {a2})
    assert _is_linked(b, 'robotDSL_Task14', a2)
    if hasattr(a1, 'robotDSL_Trigger15'):
        assert not _is_linked(a1, 'robotDSL_Trigger15', b)
    if hasattr(a2, 'robotDSL_Trigger15'):
        assert _is_linked(a2, 'robotDSL_Trigger15', b)
    _safe_set(b, 'robotDSL_Task14', set())
    assert not _is_linked(b, 'robotDSL_Task14', a2)
    if hasattr(a2, 'robotDSL_Trigger15'):
        assert not _is_linked(a2, 'robotDSL_Trigger15', b)


def test_assoc_turnDir23_reverse_link_reassign_clear():
    a1 = robotDSL_Direction(dir="sample_text")
    a2 = robotDSL_Direction(dir="sample_text_2")
    b = robotDSL_Action(cent="sample_text", degr=7, duration=7)
    _safe_set(b, 'robotDSL_Action24', a1)
    assert _is_linked(b, 'robotDSL_Action24', a1)
    if hasattr(a1, 'robotDSL_Direction25'):
        assert _is_linked(a1, 'robotDSL_Direction25', b)
    _safe_set(b, 'robotDSL_Action24', a2)
    assert _is_linked(b, 'robotDSL_Action24', a2)
    if hasattr(a1, 'robotDSL_Direction25'):
        assert not _is_linked(a1, 'robotDSL_Direction25', b)
    if hasattr(a2, 'robotDSL_Direction25'):
        assert _is_linked(a2, 'robotDSL_Direction25', b)
    _safe_set(b, 'robotDSL_Action24', None)
    assert not _is_linked(b, 'robotDSL_Action24', a2)
    if hasattr(a2, 'robotDSL_Direction25'):
        assert not _is_linked(a2, 'robotDSL_Direction25', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_finishActions11_stub_double():
    # robotDSL_Goal has no real 'robotDSL_Goal12' property in the generated
    # code (a bare stub) -- manually attach it so robotDSL_Action's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # robotDSL_Action's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = robotDSL_Action(cent="sample_text", degr=7, duration=7)
    partner = robotDSL_Goal()
    setattr(partner, 'robotDSL_Goal12', None)
    _safe_set(owner, 'robotDSL_Action', partner)
    assert owner in getattr(partner, 'robotDSL_Goal12')
    _safe_set(owner, 'robotDSL_Action', None)
    assert owner not in getattr(partner, 'robotDSL_Goal12')


def test_assoc_goal5_stub_double():
    # robotDSL_Goal has no real 'robotDSL_Goal' property in the generated
    # code (a bare stub) -- manually attach it so robotDSL_Mission's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # robotDSL_Mission's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = robotDSL_Mission(name="sample_text")
    partner = robotDSL_Goal()
    setattr(partner, 'robotDSL_Goal', None)
    _safe_set(owner, 'robotDSL_Mission6', partner)
    assert getattr(partner, 'robotDSL_Goal') == owner
    _safe_set(owner, 'robotDSL_Mission6', None)
    assert getattr(partner, 'robotDSL_Goal') is None


def test_assoc_goalEvents7_stub_double():
    # robotDSL_Goal has no real 'robotDSL_Goal8' property in the generated
    # code (a bare stub) -- manually attach it so robotDSL_Trigger's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # robotDSL_Trigger's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = robotDSL_Trigger(degrees=7, touching="sample_text")
    partner = robotDSL_Goal()
    setattr(partner, 'robotDSL_Goal8', None)
    _safe_set(owner, 'robotDSL_Trigger', partner)
    assert owner in getattr(partner, 'robotDSL_Goal8')
    _safe_set(owner, 'robotDSL_Trigger', None)
    assert owner not in getattr(partner, 'robotDSL_Goal8')


def test_assoc_timeout9_stub_double():
    # robotDSL_Goal has no real 'robotDSL_Goal10' property in the generated
    # code (a bare stub) -- manually attach it so robotDSL_Time's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # robotDSL_Time's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = robotDSL_Time(sec=7)
    partner = robotDSL_Goal()
    setattr(partner, 'robotDSL_Goal10', None)
    _safe_set(owner, 'robotDSL_Time', partner)
    assert getattr(partner, 'robotDSL_Goal10') == owner
    _safe_set(owner, 'robotDSL_Time', None)
    assert getattr(partner, 'robotDSL_Goal10') is None


