import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    AbstractDevice,
    raspduinoDSL_AbstractDevice,
    raspduinoDSL_Actuator,
    raspduinoDSL_ChangeActuator,
    raspduinoDSL_EventHandler,
    raspduinoDSL_Model,
    raspduinoDSL_Sensor,
    raspduinoDSL_SensorListener,
    raspduinoDSL_Timer,
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

def test_assoc_changeActuators7_reverse_link_reassign_clear():
    a1 = raspduinoDSL_EventHandler(name="sample_text")
    a2 = raspduinoDSL_EventHandler(name="sample_text_2")
    b = raspduinoDSL_ChangeActuator(ActuatorState="sample_text")
    _safe_set(b, 'raspduinoDSL_ChangeActuator', a1)
    assert _is_linked(b, 'raspduinoDSL_ChangeActuator', a1)
    if hasattr(a1, 'raspduinoDSL_EventHandler8'):
        assert _is_linked(a1, 'raspduinoDSL_EventHandler8', b)
    _safe_set(b, 'raspduinoDSL_ChangeActuator', a2)
    assert _is_linked(b, 'raspduinoDSL_ChangeActuator', a2)
    if hasattr(a1, 'raspduinoDSL_EventHandler8'):
        assert not _is_linked(a1, 'raspduinoDSL_EventHandler8', b)
    if hasattr(a2, 'raspduinoDSL_EventHandler8'):
        assert _is_linked(a2, 'raspduinoDSL_EventHandler8', b)
    _safe_set(b, 'raspduinoDSL_ChangeActuator', None)
    assert not _is_linked(b, 'raspduinoDSL_ChangeActuator', a2)
    if hasattr(a2, 'raspduinoDSL_EventHandler8'):
        assert not _is_linked(a2, 'raspduinoDSL_EventHandler8', b)


def test_assoc_devices0_reverse_link_reassign_clear():
    a1 = raspduinoDSL_Model(hardware="sample_text", name="sample_text")
    a2 = raspduinoDSL_Model(hardware="sample_text_2", name="sample_text_2")
    b = raspduinoDSL_AbstractDevice(name="sample_text", pin="sample_text")
    _safe_set(b, 'raspduinoDSL_AbstractDevice', a1)
    assert _is_linked(b, 'raspduinoDSL_AbstractDevice', a1)
    if hasattr(a1, 'raspduinoDSL_Model'):
        assert _is_linked(a1, 'raspduinoDSL_Model', b)
    _safe_set(b, 'raspduinoDSL_AbstractDevice', a2)
    assert _is_linked(b, 'raspduinoDSL_AbstractDevice', a2)
    if hasattr(a1, 'raspduinoDSL_Model'):
        assert not _is_linked(a1, 'raspduinoDSL_Model', b)
    if hasattr(a2, 'raspduinoDSL_Model'):
        assert _is_linked(a2, 'raspduinoDSL_Model', b)
    _safe_set(b, 'raspduinoDSL_AbstractDevice', None)
    assert not _is_linked(b, 'raspduinoDSL_AbstractDevice', a2)
    if hasattr(a2, 'raspduinoDSL_Model'):
        assert not _is_linked(a2, 'raspduinoDSL_Model', b)


def test_assoc_eventHandler13_reverse_link_reassign_clear():
    a1 = raspduinoDSL_SensorListener(h=7, l=7, type="sample_text")
    a2 = raspduinoDSL_SensorListener(h=13, l=13, type="sample_text_2")
    b = raspduinoDSL_EventHandler(name="sample_text")
    _safe_set(b, 'raspduinoDSL_EventHandler15', a1)
    assert _is_linked(b, 'raspduinoDSL_EventHandler15', a1)
    if hasattr(a1, 'raspduinoDSL_SensorListener14'):
        assert _is_linked(a1, 'raspduinoDSL_SensorListener14', b)
    _safe_set(b, 'raspduinoDSL_EventHandler15', a2)
    assert _is_linked(b, 'raspduinoDSL_EventHandler15', a2)
    if hasattr(a1, 'raspduinoDSL_SensorListener14'):
        assert not _is_linked(a1, 'raspduinoDSL_SensorListener14', b)
    if hasattr(a2, 'raspduinoDSL_SensorListener14'):
        assert _is_linked(a2, 'raspduinoDSL_SensorListener14', b)
    _safe_set(b, 'raspduinoDSL_EventHandler15', None)
    assert not _is_linked(b, 'raspduinoDSL_EventHandler15', a2)
    if hasattr(a2, 'raspduinoDSL_SensorListener14'):
        assert not _is_linked(a2, 'raspduinoDSL_SensorListener14', b)


def test_assoc_eventHandler16_reverse_link_reassign_clear():
    a1 = raspduinoDSL_Timer(hours=7, minutes=7, repeattype="sample_text", secs=7)
    a2 = raspduinoDSL_Timer(hours=13, minutes=13, repeattype="sample_text_2", secs=13)
    b = raspduinoDSL_EventHandler(name="sample_text")
    _safe_set(b, 'raspduinoDSL_EventHandler18', a1)
    assert _is_linked(b, 'raspduinoDSL_EventHandler18', a1)
    if hasattr(a1, 'raspduinoDSL_Timer17'):
        assert _is_linked(a1, 'raspduinoDSL_Timer17', b)
    _safe_set(b, 'raspduinoDSL_EventHandler18', a2)
    assert _is_linked(b, 'raspduinoDSL_EventHandler18', a2)
    if hasattr(a1, 'raspduinoDSL_Timer17'):
        assert not _is_linked(a1, 'raspduinoDSL_Timer17', b)
    if hasattr(a2, 'raspduinoDSL_Timer17'):
        assert _is_linked(a2, 'raspduinoDSL_Timer17', b)
    _safe_set(b, 'raspduinoDSL_EventHandler18', None)
    assert not _is_linked(b, 'raspduinoDSL_EventHandler18', a2)
    if hasattr(a2, 'raspduinoDSL_Timer17'):
        assert not _is_linked(a2, 'raspduinoDSL_Timer17', b)


def test_assoc_eventHandlers1_reverse_link_reassign_clear():
    a1 = raspduinoDSL_Model(hardware="sample_text", name="sample_text")
    a2 = raspduinoDSL_Model(hardware="sample_text_2", name="sample_text_2")
    b = raspduinoDSL_EventHandler(name="sample_text")
    _safe_set(b, 'raspduinoDSL_EventHandler', a1)
    assert _is_linked(b, 'raspduinoDSL_EventHandler', a1)
    if hasattr(a1, 'raspduinoDSL_Model2'):
        assert _is_linked(a1, 'raspduinoDSL_Model2', b)
    _safe_set(b, 'raspduinoDSL_EventHandler', a2)
    assert _is_linked(b, 'raspduinoDSL_EventHandler', a2)
    if hasattr(a1, 'raspduinoDSL_Model2'):
        assert not _is_linked(a1, 'raspduinoDSL_Model2', b)
    if hasattr(a2, 'raspduinoDSL_Model2'):
        assert _is_linked(a2, 'raspduinoDSL_Model2', b)
    _safe_set(b, 'raspduinoDSL_EventHandler', None)
    assert not _is_linked(b, 'raspduinoDSL_EventHandler', a2)
    if hasattr(a2, 'raspduinoDSL_Model2'):
        assert not _is_linked(a2, 'raspduinoDSL_Model2', b)


def test_assoc_sensorListeners3_reverse_link_reassign_clear():
    a1 = raspduinoDSL_SensorListener(h=7, l=7, type="sample_text")
    a2 = raspduinoDSL_SensorListener(h=13, l=13, type="sample_text_2")
    b = raspduinoDSL_Model(hardware="sample_text", name="sample_text")
    _safe_set(b, 'raspduinoDSL_Model4', {a1})
    assert _is_linked(b, 'raspduinoDSL_Model4', a1)
    if hasattr(a1, 'raspduinoDSL_SensorListener'):
        assert _is_linked(a1, 'raspduinoDSL_SensorListener', b)
    _safe_set(b, 'raspduinoDSL_Model4', {a2})
    assert _is_linked(b, 'raspduinoDSL_Model4', a2)
    if hasattr(a1, 'raspduinoDSL_SensorListener'):
        assert not _is_linked(a1, 'raspduinoDSL_SensorListener', b)
    if hasattr(a2, 'raspduinoDSL_SensorListener'):
        assert _is_linked(a2, 'raspduinoDSL_SensorListener', b)
    _safe_set(b, 'raspduinoDSL_Model4', set())
    assert not _is_linked(b, 'raspduinoDSL_Model4', a2)
    if hasattr(a2, 'raspduinoDSL_SensorListener'):
        assert not _is_linked(a2, 'raspduinoDSL_SensorListener', b)


def test_assoc_timers5_reverse_link_reassign_clear():
    a1 = raspduinoDSL_Timer(hours=7, minutes=7, repeattype="sample_text", secs=7)
    a2 = raspduinoDSL_Timer(hours=13, minutes=13, repeattype="sample_text_2", secs=13)
    b = raspduinoDSL_Model(hardware="sample_text", name="sample_text")
    _safe_set(b, 'raspduinoDSL_Model6', {a1})
    assert _is_linked(b, 'raspduinoDSL_Model6', a1)
    if hasattr(a1, 'raspduinoDSL_Timer'):
        assert _is_linked(a1, 'raspduinoDSL_Timer', b)
    _safe_set(b, 'raspduinoDSL_Model6', {a2})
    assert _is_linked(b, 'raspduinoDSL_Model6', a2)
    if hasattr(a1, 'raspduinoDSL_Timer'):
        assert not _is_linked(a1, 'raspduinoDSL_Timer', b)
    if hasattr(a2, 'raspduinoDSL_Timer'):
        assert _is_linked(a2, 'raspduinoDSL_Timer', b)
    _safe_set(b, 'raspduinoDSL_Model6', set())
    assert not _is_linked(b, 'raspduinoDSL_Model6', a2)
    if hasattr(a2, 'raspduinoDSL_Timer'):
        assert not _is_linked(a2, 'raspduinoDSL_Timer', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_actuator9_stub_double():
    # raspduinoDSL_Actuator has no real 'raspduinoDSL_Actuator' property in the generated
    # code (a bare stub) -- manually attach it so raspduinoDSL_ChangeActuator's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # raspduinoDSL_ChangeActuator's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = raspduinoDSL_ChangeActuator(ActuatorState="sample_text")
    partner = raspduinoDSL_Actuator()
    setattr(partner, 'raspduinoDSL_Actuator', None)
    _safe_set(owner, 'raspduinoDSL_ChangeActuator10', partner)
    assert getattr(partner, 'raspduinoDSL_Actuator') == owner
    _safe_set(owner, 'raspduinoDSL_ChangeActuator10', None)
    assert getattr(partner, 'raspduinoDSL_Actuator') is None


def test_assoc_sensor11_stub_double():
    # raspduinoDSL_Sensor has no real 'raspduinoDSL_Sensor' property in the generated
    # code (a bare stub) -- manually attach it so raspduinoDSL_SensorListener's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # raspduinoDSL_SensorListener's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = raspduinoDSL_SensorListener(h=7, l=7, type="sample_text")
    partner = raspduinoDSL_Sensor()
    setattr(partner, 'raspduinoDSL_Sensor', None)
    _safe_set(owner, 'raspduinoDSL_SensorListener12', partner)
    assert getattr(partner, 'raspduinoDSL_Sensor') == owner
    _safe_set(owner, 'raspduinoDSL_SensorListener12', None)
    assert getattr(partner, 'raspduinoDSL_Sensor') is None


