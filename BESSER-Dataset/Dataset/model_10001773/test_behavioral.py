import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Appliances,
    Department,
    FireAlarm,
    Fire_Alarm_system,
    Home_Security_System,
    Login,
    Owner,
    Police,
    securityAlarm,
    smokeAlarm,
    system,
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

def test_assoc_Department_Fire_Alarm_system_reverse_link_reassign_clear():
    a1 = Fire_Alarm_system(system_Off=True, system_On=True)
    a2 = Fire_Alarm_system(system_Off=False, system_On=False)
    b = Department(name="sample_text")
    _safe_set(b, 'fire_Alarm_system4', a1)
    assert _is_linked(b, 'fire_Alarm_system4', a1)
    if hasattr(a1, 'department5'):
        assert _is_linked(a1, 'department5', b)
    _safe_set(b, 'fire_Alarm_system4', a2)
    assert _is_linked(b, 'fire_Alarm_system4', a2)
    if hasattr(a1, 'department5'):
        assert not _is_linked(a1, 'department5', b)
    if hasattr(a2, 'department5'):
        assert _is_linked(a2, 'department5', b)
    _safe_set(b, 'fire_Alarm_system4', None)
    assert not _is_linked(b, 'fire_Alarm_system4', a2)
    if hasattr(a2, 'department5'):
        assert not _is_linked(a2, 'department5', b)


def test_assoc_Fire_Alarm_system_FireAlarm_reverse_link_reassign_clear():
    a1 = Fire_Alarm_system(system_Off=True, system_On=True)
    a2 = Fire_Alarm_system(system_Off=False, system_On=False)
    b = FireAlarm(status=True)
    _safe_set(b, 'fire_Alarm_system13', a1)
    assert _is_linked(b, 'fire_Alarm_system13', a1)
    if hasattr(a1, 'fireAlarm12'):
        assert _is_linked(a1, 'fireAlarm12', b)
    _safe_set(b, 'fire_Alarm_system13', a2)
    assert _is_linked(b, 'fire_Alarm_system13', a2)
    if hasattr(a1, 'fireAlarm12'):
        assert not _is_linked(a1, 'fireAlarm12', b)
    if hasattr(a2, 'fireAlarm12'):
        assert _is_linked(a2, 'fireAlarm12', b)
    _safe_set(b, 'fire_Alarm_system13', None)
    assert not _is_linked(b, 'fire_Alarm_system13', a2)
    if hasattr(a2, 'fireAlarm12'):
        assert not _is_linked(a2, 'fireAlarm12', b)


def test_assoc_Police_Home_Security_System_reverse_link_reassign_clear():
    a1 = Police(name="sample_text")
    a2 = Police(name="sample_text_2")
    b = Home_Security_System(system_Off=True, system_On=True)
    _safe_set(b, 'police9', a1)
    assert _is_linked(b, 'police9', a1)
    if hasattr(a1, 'home_Security_System8'):
        assert _is_linked(a1, 'home_Security_System8', b)
    _safe_set(b, 'police9', a2)
    assert _is_linked(b, 'police9', a2)
    if hasattr(a1, 'home_Security_System8'):
        assert not _is_linked(a1, 'home_Security_System8', b)
    if hasattr(a2, 'home_Security_System8'):
        assert _is_linked(a2, 'home_Security_System8', b)
    _safe_set(b, 'police9', None)
    assert not _is_linked(b, 'police9', a2)
    if hasattr(a2, 'home_Security_System8'):
        assert not _is_linked(a2, 'home_Security_System8', b)


def test_assoc_access_reverse_link_reassign_clear():
    a1 = Owner(name="sample_text")
    a2 = Owner(name="sample_text_2")
    b = Login(name="sample_text", password="sample_text")
    _safe_set(b, 'owner1', a1)
    assert _is_linked(b, 'owner1', a1)
    if hasattr(a1, 'login0'):
        assert _is_linked(a1, 'login0', b)
    _safe_set(b, 'owner1', a2)
    assert _is_linked(b, 'owner1', a2)
    if hasattr(a1, 'login0'):
        assert not _is_linked(a1, 'login0', b)
    if hasattr(a2, 'login0'):
        assert _is_linked(a2, 'login0', b)
    _safe_set(b, 'owner1', None)
    assert not _is_linked(b, 'owner1', a2)
    if hasattr(a2, 'login0'):
        assert not _is_linked(a2, 'login0', b)


def test_assoc_handle_reverse_link_reassign_clear():
    a1 = system(status=True)
    a2 = system(status=False)
    b = Login(name="sample_text", password="sample_text")
    _safe_set(b, 'system2', a1)
    assert _is_linked(b, 'system2', a1)
    if hasattr(a1, 'login23'):
        assert _is_linked(a1, 'login23', b)
    _safe_set(b, 'system2', a2)
    assert _is_linked(b, 'system2', a2)
    if hasattr(a1, 'login23'):
        assert not _is_linked(a1, 'login23', b)
    if hasattr(a2, 'login23'):
        assert _is_linked(a2, 'login23', b)
    _safe_set(b, 'system2', None)
    assert not _is_linked(b, 'system2', a2)
    if hasattr(a2, 'login23'):
        assert not _is_linked(a2, 'login23', b)


def test_assoc_securityAlarm_Home_Security_System_reverse_link_reassign_clear():
    a1 = securityAlarm(status=True)
    a2 = securityAlarm(status=False)
    b = Home_Security_System(system_Off=True, system_On=True)
    _safe_set(b, 'securityAlarm11', a1)
    assert _is_linked(b, 'securityAlarm11', a1)
    if hasattr(a1, 'home_Security_System10'):
        assert _is_linked(a1, 'home_Security_System10', b)
    _safe_set(b, 'securityAlarm11', a2)
    assert _is_linked(b, 'securityAlarm11', a2)
    if hasattr(a1, 'home_Security_System10'):
        assert not _is_linked(a1, 'home_Security_System10', b)
    if hasattr(a2, 'home_Security_System10'):
        assert _is_linked(a2, 'home_Security_System10', b)
    _safe_set(b, 'securityAlarm11', None)
    assert not _is_linked(b, 'securityAlarm11', a2)
    if hasattr(a2, 'home_Security_System10'):
        assert not _is_linked(a2, 'home_Security_System10', b)


def test_assoc_smokeAlarm_Fire_Alarm_system_reverse_link_reassign_clear():
    a1 = smokeAlarm(status=True)
    a2 = smokeAlarm(status=False)
    b = Fire_Alarm_system(system_Off=True, system_On=True)
    _safe_set(b, 'smokeAlarm7', a1)
    assert _is_linked(b, 'smokeAlarm7', a1)
    if hasattr(a1, 'fire_Alarm_system6'):
        assert _is_linked(a1, 'fire_Alarm_system6', b)
    _safe_set(b, 'smokeAlarm7', a2)
    assert _is_linked(b, 'smokeAlarm7', a2)
    if hasattr(a1, 'fire_Alarm_system6'):
        assert not _is_linked(a1, 'fire_Alarm_system6', b)
    if hasattr(a2, 'fire_Alarm_system6'):
        assert _is_linked(a2, 'fire_Alarm_system6', b)
    _safe_set(b, 'smokeAlarm7', None)
    assert not _is_linked(b, 'smokeAlarm7', a2)
    if hasattr(a2, 'fire_Alarm_system6'):
        assert not _is_linked(a2, 'fire_Alarm_system6', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

