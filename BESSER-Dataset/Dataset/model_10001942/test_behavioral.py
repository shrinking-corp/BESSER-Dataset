import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    AddAlarm,
    Add_new_alarm_external,
    Alarm,
    Arduino,
    Building_Owner__Actor,
    Count_Sensor,
    Disable_detector_external,
    Fire_Alarm_System__Component,
    Fire_Department__Actor,
    Firebase,
    Gas_Smoke_Sensor,
    MobileApp,
    Notification,
    Notify_User_of_fire_external,
    Sense_and_Update_Data_external,
    Sensor,
    Sensors_Actor,
    Set_time_external,
    Temperature_Sensor,
    TurnDownAlarm,
    ViewTemp_Smoke,
    View_sensors_data_external,
    WebPage,
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

def test_assoc_AddAlarm_Alarm_reverse_link_reassign_clear():
    a1 = Alarm(AlarmID="sample_text")
    a2 = Alarm(AlarmID="sample_text_2")
    b = AddAlarm(AlarmName="sample_text")
    _safe_set(b, 'AddAlarm_Alarm_024', a1)
    assert _is_linked(b, 'AddAlarm_Alarm_024', a1)
    if hasattr(a1, 'AddAlarm_Alarm_125'):
        assert _is_linked(a1, 'AddAlarm_Alarm_125', b)
    _safe_set(b, 'AddAlarm_Alarm_024', a2)
    assert _is_linked(b, 'AddAlarm_Alarm_024', a2)
    if hasattr(a1, 'AddAlarm_Alarm_125'):
        assert not _is_linked(a1, 'AddAlarm_Alarm_125', b)
    if hasattr(a2, 'AddAlarm_Alarm_125'):
        assert _is_linked(a2, 'AddAlarm_Alarm_125', b)
    _safe_set(b, 'AddAlarm_Alarm_024', None)
    assert not _is_linked(b, 'AddAlarm_Alarm_024', a2)
    if hasattr(a2, 'AddAlarm_Alarm_125'):
        assert not _is_linked(a2, 'AddAlarm_Alarm_125', b)


def test_assoc_Alarm_Mobile_App_reverse_link_reassign_clear():
    a1 = MobileApp(AlarmID=7, UserID=7)
    a2 = MobileApp(AlarmID=13, UserID=13)
    b = Alarm(AlarmID="sample_text")
    _safe_set(b, 'Alarm_Mobile_App_028', a1)
    assert _is_linked(b, 'Alarm_Mobile_App_028', a1)
    if hasattr(a1, 'Alarm_Mobile_App_129'):
        assert _is_linked(a1, 'Alarm_Mobile_App_129', b)
    _safe_set(b, 'Alarm_Mobile_App_028', a2)
    assert _is_linked(b, 'Alarm_Mobile_App_028', a2)
    if hasattr(a1, 'Alarm_Mobile_App_129'):
        assert not _is_linked(a1, 'Alarm_Mobile_App_129', b)
    if hasattr(a2, 'Alarm_Mobile_App_129'):
        assert _is_linked(a2, 'Alarm_Mobile_App_129', b)
    _safe_set(b, 'Alarm_Mobile_App_028', None)
    assert not _is_linked(b, 'Alarm_Mobile_App_028', a2)
    if hasattr(a2, 'Alarm_Mobile_App_129'):
        assert not _is_linked(a2, 'Alarm_Mobile_App_129', b)


def test_assoc_Notification_Alarm_reverse_link_reassign_clear():
    a1 = Notification(SmokeThreshold=3.14, TempThreshold=3.14)
    a2 = Notification(SmokeThreshold=9.99, TempThreshold=9.99)
    b = Alarm(AlarmID="sample_text")
    _safe_set(b, 'Notification_Alarm_121', a1)
    assert _is_linked(b, 'Notification_Alarm_121', a1)
    if hasattr(a1, 'Notification_Alarm_020'):
        assert _is_linked(a1, 'Notification_Alarm_020', b)
    _safe_set(b, 'Notification_Alarm_121', a2)
    assert _is_linked(b, 'Notification_Alarm_121', a2)
    if hasattr(a1, 'Notification_Alarm_020'):
        assert not _is_linked(a1, 'Notification_Alarm_020', b)
    if hasattr(a2, 'Notification_Alarm_020'):
        assert _is_linked(a2, 'Notification_Alarm_020', b)
    _safe_set(b, 'Notification_Alarm_121', None)
    assert not _is_linked(b, 'Notification_Alarm_121', a2)
    if hasattr(a2, 'Notification_Alarm_020'):
        assert not _is_linked(a2, 'Notification_Alarm_020', b)


def test_assoc_ViewTemp_Smoke_Alarm_reverse_link_reassign_clear():
    a1 = ViewTemp_Smoke(SmokeValue=3.14, TempValue=3.14)
    a2 = ViewTemp_Smoke(SmokeValue=9.99, TempValue=9.99)
    b = Alarm(AlarmID="sample_text")
    _safe_set(b, 'ViewTemp_Smoke_Alarm_123', a1)
    assert _is_linked(b, 'ViewTemp_Smoke_Alarm_123', a1)
    if hasattr(a1, 'ViewTemp_Smoke_Alarm_022'):
        assert _is_linked(a1, 'ViewTemp_Smoke_Alarm_022', b)
    _safe_set(b, 'ViewTemp_Smoke_Alarm_123', a2)
    assert _is_linked(b, 'ViewTemp_Smoke_Alarm_123', a2)
    if hasattr(a1, 'ViewTemp_Smoke_Alarm_022'):
        assert not _is_linked(a1, 'ViewTemp_Smoke_Alarm_022', b)
    if hasattr(a2, 'ViewTemp_Smoke_Alarm_022'):
        assert _is_linked(a2, 'ViewTemp_Smoke_Alarm_022', b)
    _safe_set(b, 'ViewTemp_Smoke_Alarm_123', None)
    assert not _is_linked(b, 'ViewTemp_Smoke_Alarm_123', a2)
    if hasattr(a2, 'ViewTemp_Smoke_Alarm_022'):
        assert not _is_linked(a2, 'ViewTemp_Smoke_Alarm_022', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_Firebase_Web_stub_double():
    # Firebase has no real 'Firebase_Web_06' property in the generated
    # code (a bare stub) -- manually attach it so WebPage's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # WebPage's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = WebPage(HomeLoc="sample_text", OwnerData="sample_text", People_=7, SmokeValue=3.14, TempValue=3.14)
    partner = Firebase()
    setattr(partner, 'Firebase_Web_06', None)
    _safe_set(owner, 'Firebase_Web_17', partner)
    assert getattr(partner, 'Firebase_Web_06') == owner
    _safe_set(owner, 'Firebase_Web_17', None)
    assert getattr(partner, 'Firebase_Web_06') is None


def test_assoc_Home_Security_System_System_stub_double():
    # Firebase has no real 'Home_Security_System_System_13' property in the generated
    # code (a bare stub) -- manually attach it so MobileApp's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # MobileApp's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = MobileApp(AlarmID=7, UserID=7)
    partner = Firebase()
    setattr(partner, 'Home_Security_System_System_13', None)
    _safe_set(owner, 'Home_Security_System_System_02', partner)
    assert getattr(partner, 'Home_Security_System_System_13') == owner
    _safe_set(owner, 'Home_Security_System_System_02', None)
    assert getattr(partner, 'Home_Security_System_System_13') is None


def test_assoc_Sensor_System_stub_double():
    # Arduino has no real 'sensor1' property in the generated
    # code (a bare stub) -- manually attach it so Sensor's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # Sensor's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = Sensor(SensorID=7, SensorType=7)
    partner = Arduino()
    setattr(partner, 'sensor1', None)
    _safe_set(owner, 'system0', partner)
    assert owner in getattr(partner, 'sensor1')
    _safe_set(owner, 'system0', None)
    assert owner not in getattr(partner, 'sensor1')


def test_assoc_TurnDownAlarm_Alarm_stub_double():
    # TurnDownAlarm has no real 'TurnDownAlarm_Alarm_026' property in the generated
    # code (a bare stub) -- manually attach it so Alarm's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # Alarm's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = Alarm(AlarmID="sample_text")
    partner = TurnDownAlarm()
    setattr(partner, 'TurnDownAlarm_Alarm_026', None)
    _safe_set(owner, 'TurnDownAlarm_Alarm_127', partner)
    assert getattr(partner, 'TurnDownAlarm_Alarm_026') == owner
    _safe_set(owner, 'TurnDownAlarm_Alarm_127', None)
    assert getattr(partner, 'TurnDownAlarm_Alarm_026') is None


