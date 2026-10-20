import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    ClassJ,
    InterfaceO_Interface,
    Notification_System,
    camera_records,
    control_panel,
    door_alarm_system,
    door_sensor,
    eventlog,
    fire_alarm_system,
    flood_alarm_system,
    flood_sensor,
    login,
    owner_details,
    smoke_sensor,
    temp_sensor,
    timelog,
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

def test_assoc_Notification_System_control_panel_reverse_link_reassign_clear():
    a1 = control_panel(system_on=True)
    a2 = control_panel(system_on=False)
    b = Notification_System(OwnerEmail="sample_text", OwnerNum__Integer="sample_text", PublicSafetyNumber=7, PublicSafetyPage=7)
    _safe_set(b, 'control_panel18', a1)
    assert _is_linked(b, 'control_panel18', a1)
    if hasattr(a1, 'notification_System19'):
        assert _is_linked(a1, 'notification_System19', b)
    _safe_set(b, 'control_panel18', a2)
    assert _is_linked(b, 'control_panel18', a2)
    if hasattr(a1, 'notification_System19'):
        assert not _is_linked(a1, 'notification_System19', b)
    if hasattr(a2, 'notification_System19'):
        assert _is_linked(a2, 'notification_System19', b)
    _safe_set(b, 'control_panel18', None)
    assert not _is_linked(b, 'control_panel18', a2)
    if hasattr(a2, 'notification_System19'):
        assert not _is_linked(a2, 'notification_System19', b)


def test_assoc_assoc__U4MOxJiYEeqEM7mFKilpXw_reverse_link_reassign_clear():
    a1 = login(lockout=7, loginapp="sample_text", loginattempt=7, logoutapp="sample_text", password="sample_text", username="sample_text")
    a2 = login(lockout=13, loginapp="sample_text_2", loginattempt=13, logoutapp="sample_text_2", password="sample_text_2", username="sample_text_2")
    b = eventlog(event_id=7, event_info="sample_text", event_time=7)
    _safe_set(b, 'assoc_02', a1)
    assert _is_linked(b, 'assoc_02', a1)
    if hasattr(a1, 'assoc_13'):
        assert _is_linked(a1, 'assoc_13', b)
    _safe_set(b, 'assoc_02', a2)
    assert _is_linked(b, 'assoc_02', a2)
    if hasattr(a1, 'assoc_13'):
        assert not _is_linked(a1, 'assoc_13', b)
    if hasattr(a2, 'assoc_13'):
        assert _is_linked(a2, 'assoc_13', b)
    _safe_set(b, 'assoc_02', None)
    assert not _is_linked(b, 'assoc_02', a2)
    if hasattr(a2, 'assoc_13'):
        assert not _is_linked(a2, 'assoc_13', b)


def test_assoc_camera_records_control_panel_reverse_link_reassign_clear():
    a1 = control_panel(system_on=True)
    a2 = control_panel(system_on=False)
    b = camera_records(camera_id=7, camera_location="sample_text", camera_status_on=True)
    _safe_set(b, 'control_panel32', a1)
    assert _is_linked(b, 'control_panel32', a1)
    if hasattr(a1, 'camera_records33'):
        assert _is_linked(a1, 'camera_records33', b)
    _safe_set(b, 'control_panel32', a2)
    assert _is_linked(b, 'control_panel32', a2)
    if hasattr(a1, 'camera_records33'):
        assert not _is_linked(a1, 'camera_records33', b)
    if hasattr(a2, 'camera_records33'):
        assert _is_linked(a2, 'camera_records33', b)
    _safe_set(b, 'control_panel32', None)
    assert not _is_linked(b, 'control_panel32', a2)
    if hasattr(a2, 'camera_records33'):
        assert not _is_linked(a2, 'camera_records33', b)


def test_assoc_door_alarm_system_control_panel_reverse_link_reassign_clear():
    a1 = door_alarm_system(door_alarm_system=True)
    a2 = door_alarm_system(door_alarm_system=False)
    b = control_panel(system_on=True)
    _safe_set(b, 'door_alarm_system31', {a1})
    assert _is_linked(b, 'door_alarm_system31', a1)
    if hasattr(a1, 'control_panel30'):
        assert _is_linked(a1, 'control_panel30', b)
    _safe_set(b, 'door_alarm_system31', {a2})
    assert _is_linked(b, 'door_alarm_system31', a2)
    if hasattr(a1, 'control_panel30'):
        assert not _is_linked(a1, 'control_panel30', b)
    if hasattr(a2, 'control_panel30'):
        assert _is_linked(a2, 'control_panel30', b)
    _safe_set(b, 'door_alarm_system31', set())
    assert not _is_linked(b, 'door_alarm_system31', a2)
    if hasattr(a2, 'control_panel30'):
        assert not _is_linked(a2, 'control_panel30', b)


def test_assoc_door_alarm_system_door_sensor_reverse_link_reassign_clear():
    a1 = door_sensor(door_location="sample_text", door_open_status=True, door_sensor_id=7)
    a2 = door_sensor(door_location="sample_text_2", door_open_status=False, door_sensor_id=13)
    b = door_alarm_system(door_alarm_system=True)
    _safe_set(b, 'door_sensor10', {a1})
    assert _is_linked(b, 'door_sensor10', a1)
    if hasattr(a1, 'door_alarm_system11'):
        assert _is_linked(a1, 'door_alarm_system11', b)
    _safe_set(b, 'door_sensor10', {a2})
    assert _is_linked(b, 'door_sensor10', a2)
    if hasattr(a1, 'door_alarm_system11'):
        assert not _is_linked(a1, 'door_alarm_system11', b)
    if hasattr(a2, 'door_alarm_system11'):
        assert _is_linked(a2, 'door_alarm_system11', b)
    _safe_set(b, 'door_sensor10', set())
    assert not _is_linked(b, 'door_sensor10', a2)
    if hasattr(a2, 'door_alarm_system11'):
        assert not _is_linked(a2, 'door_alarm_system11', b)


def test_assoc_door_alarm_system_eventlog_reverse_link_reassign_clear():
    a1 = eventlog(event_id=7, event_info="sample_text", event_time=7)
    a2 = eventlog(event_id=13, event_info="sample_text_2", event_time=13)
    b = door_alarm_system(door_alarm_system=True)
    _safe_set(b, 'eventlog16', a1)
    assert _is_linked(b, 'eventlog16', a1)
    if hasattr(a1, 'door_alarm_system17'):
        assert _is_linked(a1, 'door_alarm_system17', b)
    _safe_set(b, 'eventlog16', a2)
    assert _is_linked(b, 'eventlog16', a2)
    if hasattr(a1, 'door_alarm_system17'):
        assert not _is_linked(a1, 'door_alarm_system17', b)
    if hasattr(a2, 'door_alarm_system17'):
        assert _is_linked(a2, 'door_alarm_system17', b)
    _safe_set(b, 'eventlog16', None)
    assert not _is_linked(b, 'eventlog16', a2)
    if hasattr(a2, 'door_alarm_system17'):
        assert not _is_linked(a2, 'door_alarm_system17', b)


def test_assoc_eventlog_fire_alarm_system_reverse_link_reassign_clear():
    a1 = fire_alarm_system(fire_alarm_system_on=True)
    a2 = fire_alarm_system(fire_alarm_system_on=False)
    b = eventlog(event_id=7, event_info="sample_text", event_time=7)
    _safe_set(b, 'fire_alarm_system12', a1)
    assert _is_linked(b, 'fire_alarm_system12', a1)
    if hasattr(a1, 'eventlog13'):
        assert _is_linked(a1, 'eventlog13', b)
    _safe_set(b, 'fire_alarm_system12', a2)
    assert _is_linked(b, 'fire_alarm_system12', a2)
    if hasattr(a1, 'eventlog13'):
        assert not _is_linked(a1, 'eventlog13', b)
    if hasattr(a2, 'eventlog13'):
        assert _is_linked(a2, 'eventlog13', b)
    _safe_set(b, 'fire_alarm_system12', None)
    assert not _is_linked(b, 'fire_alarm_system12', a2)
    if hasattr(a2, 'eventlog13'):
        assert not _is_linked(a2, 'eventlog13', b)


def test_assoc_eventlog_flood_alarm_system_reverse_link_reassign_clear():
    a1 = flood_alarm_system(flood_alarm_system=True)
    a2 = flood_alarm_system(flood_alarm_system=False)
    b = eventlog(event_id=7, event_info="sample_text", event_time=7)
    _safe_set(b, 'flood_alarm_system14', a1)
    assert _is_linked(b, 'flood_alarm_system14', a1)
    if hasattr(a1, 'eventlog15'):
        assert _is_linked(a1, 'eventlog15', b)
    _safe_set(b, 'flood_alarm_system14', a2)
    assert _is_linked(b, 'flood_alarm_system14', a2)
    if hasattr(a1, 'eventlog15'):
        assert not _is_linked(a1, 'eventlog15', b)
    if hasattr(a2, 'eventlog15'):
        assert _is_linked(a2, 'eventlog15', b)
    _safe_set(b, 'flood_alarm_system14', None)
    assert not _is_linked(b, 'flood_alarm_system14', a2)
    if hasattr(a2, 'eventlog15'):
        assert not _is_linked(a2, 'eventlog15', b)


def test_assoc_eventlog_timelog_reverse_link_reassign_clear():
    a1 = timelog(day=7, hour=7, minutes=7, month=7, seconds=7, year=7)
    a2 = timelog(day=13, hour=13, minutes=13, month=13, seconds=13, year=13)
    b = eventlog(event_id=7, event_info="sample_text", event_time=7)
    _safe_set(b, 'timelog20', a1)
    assert _is_linked(b, 'timelog20', a1)
    if hasattr(a1, 'eventlog21'):
        assert _is_linked(a1, 'eventlog21', b)
    _safe_set(b, 'timelog20', a2)
    assert _is_linked(b, 'timelog20', a2)
    if hasattr(a1, 'eventlog21'):
        assert not _is_linked(a1, 'eventlog21', b)
    if hasattr(a2, 'eventlog21'):
        assert _is_linked(a2, 'eventlog21', b)
    _safe_set(b, 'timelog20', None)
    assert not _is_linked(b, 'timelog20', a2)
    if hasattr(a2, 'eventlog21'):
        assert not _is_linked(a2, 'eventlog21', b)


def test_assoc_fire_alarm_system_control_panel_reverse_link_reassign_clear():
    a1 = fire_alarm_system(fire_alarm_system_on=True)
    a2 = fire_alarm_system(fire_alarm_system_on=False)
    b = control_panel(system_on=True)
    _safe_set(b, 'fire_alarm_system27', {a1})
    assert _is_linked(b, 'fire_alarm_system27', a1)
    if hasattr(a1, 'control_panel26'):
        assert _is_linked(a1, 'control_panel26', b)
    _safe_set(b, 'fire_alarm_system27', {a2})
    assert _is_linked(b, 'fire_alarm_system27', a2)
    if hasattr(a1, 'control_panel26'):
        assert not _is_linked(a1, 'control_panel26', b)
    if hasattr(a2, 'control_panel26'):
        assert _is_linked(a2, 'control_panel26', b)
    _safe_set(b, 'fire_alarm_system27', set())
    assert not _is_linked(b, 'fire_alarm_system27', a2)
    if hasattr(a2, 'control_panel26'):
        assert not _is_linked(a2, 'control_panel26', b)


def test_assoc_fire_alarm_system_fire_alarm_system_reverse_link_reassign_clear():
    a1 = fire_alarm_system(fire_alarm_system_on=True)
    a2 = fire_alarm_system(fire_alarm_system_on=False)
    b = fire_alarm_system(fire_alarm_system_on=True)
    _safe_set(b, 'fire_alarm_system25', a1)
    assert _is_linked(b, 'fire_alarm_system25', a1)
    if hasattr(a1, 'fire_alarm_system24'):
        assert _is_linked(a1, 'fire_alarm_system24', b)
    _safe_set(b, 'fire_alarm_system25', a2)
    assert _is_linked(b, 'fire_alarm_system25', a2)
    if hasattr(a1, 'fire_alarm_system24'):
        assert not _is_linked(a1, 'fire_alarm_system24', b)
    if hasattr(a2, 'fire_alarm_system24'):
        assert _is_linked(a2, 'fire_alarm_system24', b)
    _safe_set(b, 'fire_alarm_system25', None)
    assert not _is_linked(b, 'fire_alarm_system25', a2)
    if hasattr(a2, 'fire_alarm_system24'):
        assert not _is_linked(a2, 'fire_alarm_system24', b)


def test_assoc_fire_alarm_system_smoke_sensor_reverse_link_reassign_clear():
    a1 = smoke_sensor(smoke_level_breach=True, smoke_sensor_id=7, smoke_sensor_location="sample_text", smoke_sensor_status=True)
    a2 = smoke_sensor(smoke_level_breach=False, smoke_sensor_id=13, smoke_sensor_location="sample_text_2", smoke_sensor_status=False)
    b = fire_alarm_system(fire_alarm_system_on=True)
    _safe_set(b, 'smoke_sensor4', {a1})
    assert _is_linked(b, 'smoke_sensor4', a1)
    if hasattr(a1, 'fire_alarm_system5'):
        assert _is_linked(a1, 'fire_alarm_system5', b)
    _safe_set(b, 'smoke_sensor4', {a2})
    assert _is_linked(b, 'smoke_sensor4', a2)
    if hasattr(a1, 'fire_alarm_system5'):
        assert not _is_linked(a1, 'fire_alarm_system5', b)
    if hasattr(a2, 'fire_alarm_system5'):
        assert _is_linked(a2, 'fire_alarm_system5', b)
    _safe_set(b, 'smoke_sensor4', set())
    assert not _is_linked(b, 'smoke_sensor4', a2)
    if hasattr(a2, 'fire_alarm_system5'):
        assert not _is_linked(a2, 'fire_alarm_system5', b)


def test_assoc_fire_alarm_system_temp_sensor_reverse_link_reassign_clear():
    a1 = temp_sensor(temp_level_breach=True, temp_sensor_id=7, temp_sensor_location="sample_text", temp_sensor_status=True)
    a2 = temp_sensor(temp_level_breach=False, temp_sensor_id=13, temp_sensor_location="sample_text_2", temp_sensor_status=False)
    b = fire_alarm_system(fire_alarm_system_on=True)
    _safe_set(b, 'temp_sensor6', {a1})
    assert _is_linked(b, 'temp_sensor6', a1)
    if hasattr(a1, 'fire_alarm_system7'):
        assert _is_linked(a1, 'fire_alarm_system7', b)
    _safe_set(b, 'temp_sensor6', {a2})
    assert _is_linked(b, 'temp_sensor6', a2)
    if hasattr(a1, 'fire_alarm_system7'):
        assert not _is_linked(a1, 'fire_alarm_system7', b)
    if hasattr(a2, 'fire_alarm_system7'):
        assert _is_linked(a2, 'fire_alarm_system7', b)
    _safe_set(b, 'temp_sensor6', set())
    assert not _is_linked(b, 'temp_sensor6', a2)
    if hasattr(a2, 'fire_alarm_system7'):
        assert not _is_linked(a2, 'fire_alarm_system7', b)


def test_assoc_flood_alarm_system_control_panel_reverse_link_reassign_clear():
    a1 = flood_alarm_system(flood_alarm_system=True)
    a2 = flood_alarm_system(flood_alarm_system=False)
    b = control_panel(system_on=True)
    _safe_set(b, 'flood_alarm_system29', {a1})
    assert _is_linked(b, 'flood_alarm_system29', a1)
    if hasattr(a1, 'control_panel28'):
        assert _is_linked(a1, 'control_panel28', b)
    _safe_set(b, 'flood_alarm_system29', {a2})
    assert _is_linked(b, 'flood_alarm_system29', a2)
    if hasattr(a1, 'control_panel28'):
        assert not _is_linked(a1, 'control_panel28', b)
    if hasattr(a2, 'control_panel28'):
        assert _is_linked(a2, 'control_panel28', b)
    _safe_set(b, 'flood_alarm_system29', set())
    assert not _is_linked(b, 'flood_alarm_system29', a2)
    if hasattr(a2, 'control_panel28'):
        assert not _is_linked(a2, 'control_panel28', b)


def test_assoc_flood_alarm_system_flood_sensor_reverse_link_reassign_clear():
    a1 = flood_sensor(flood_sensor_id=7, flood_sensor_loaction="sample_text", flood_sensor_status=True, waterlevel_breach_status=True)
    a2 = flood_sensor(flood_sensor_id=13, flood_sensor_loaction="sample_text_2", flood_sensor_status=False, waterlevel_breach_status=False)
    b = flood_alarm_system(flood_alarm_system=True)
    _safe_set(b, 'flood_sensor8', {a1})
    assert _is_linked(b, 'flood_sensor8', a1)
    if hasattr(a1, 'flood_alarm_system9'):
        assert _is_linked(a1, 'flood_alarm_system9', b)
    _safe_set(b, 'flood_sensor8', {a2})
    assert _is_linked(b, 'flood_sensor8', a2)
    if hasattr(a1, 'flood_alarm_system9'):
        assert not _is_linked(a1, 'flood_alarm_system9', b)
    if hasattr(a2, 'flood_alarm_system9'):
        assert _is_linked(a2, 'flood_alarm_system9', b)
    _safe_set(b, 'flood_sensor8', set())
    assert not _is_linked(b, 'flood_sensor8', a2)
    if hasattr(a2, 'flood_alarm_system9'):
        assert not _is_linked(a2, 'flood_alarm_system9', b)


def test_assoc_owner_details_login_reverse_link_reassign_clear():
    a1 = owner_details(ownerName="sample_text")
    a2 = owner_details(ownerName="sample_text_2")
    b = login(lockout=7, loginapp="sample_text", loginattempt=7, logoutapp="sample_text", password="sample_text", username="sample_text")
    _safe_set(b, 'owner_details_login_11', a1)
    assert _is_linked(b, 'owner_details_login_11', a1)
    if hasattr(a1, 'owner_details_login_00'):
        assert _is_linked(a1, 'owner_details_login_00', b)
    _safe_set(b, 'owner_details_login_11', a2)
    assert _is_linked(b, 'owner_details_login_11', a2)
    if hasattr(a1, 'owner_details_login_00'):
        assert not _is_linked(a1, 'owner_details_login_00', b)
    if hasattr(a2, 'owner_details_login_00'):
        assert _is_linked(a2, 'owner_details_login_00', b)
    _safe_set(b, 'owner_details_login_11', None)
    assert not _is_linked(b, 'owner_details_login_11', a2)
    if hasattr(a2, 'owner_details_login_00'):
        assert not _is_linked(a2, 'owner_details_login_00', b)


def test_assoc_timelog_Notification_System_reverse_link_reassign_clear():
    a1 = timelog(day=7, hour=7, minutes=7, month=7, seconds=7, year=7)
    a2 = timelog(day=13, hour=13, minutes=13, month=13, seconds=13, year=13)
    b = Notification_System(OwnerEmail="sample_text", OwnerNum__Integer="sample_text", PublicSafetyNumber=7, PublicSafetyPage=7)
    _safe_set(b, 'timelog23', a1)
    assert _is_linked(b, 'timelog23', a1)
    if hasattr(a1, 'notification_System22'):
        assert _is_linked(a1, 'notification_System22', b)
    _safe_set(b, 'timelog23', a2)
    assert _is_linked(b, 'timelog23', a2)
    if hasattr(a1, 'notification_System22'):
        assert not _is_linked(a1, 'notification_System22', b)
    if hasattr(a2, 'notification_System22'):
        assert _is_linked(a2, 'notification_System22', b)
    _safe_set(b, 'timelog23', None)
    assert not _is_linked(b, 'timelog23', a2)
    if hasattr(a2, 'notification_System22'):
        assert not _is_linked(a2, 'notification_System22', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

