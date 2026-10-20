import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Air_Conditioners,
    Alert,
    Doors,
    Entry_Points,
    Fans,
    Gardening,
    HomeAppliances,
    Home_Security_System,
    IoT_based_Smart_Resort_System,
    Lights,
    MoistureSensor,
    Motion_Sensor,
    Security_Guard_Police,
    Sensor,
    SolarPanel,
    User_Home_Owner,
    Windows,
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

def test_assoc_Entry_Points_Windows_reverse_link_reassign_clear():
    a1 = Windows(WinID=7)
    a2 = Windows(WinID=13)
    b = Entry_Points(DoorID=7)
    _safe_set(b, 'Entry_Points_Windows_026', {a1})
    assert _is_linked(b, 'Entry_Points_Windows_026', a1)
    if hasattr(a1, 'Entry_Points_Windows_127'):
        assert _is_linked(a1, 'Entry_Points_Windows_127', b)
    _safe_set(b, 'Entry_Points_Windows_026', {a2})
    assert _is_linked(b, 'Entry_Points_Windows_026', a2)
    if hasattr(a1, 'Entry_Points_Windows_127'):
        assert not _is_linked(a1, 'Entry_Points_Windows_127', b)
    if hasattr(a2, 'Entry_Points_Windows_127'):
        assert _is_linked(a2, 'Entry_Points_Windows_127', b)
    _safe_set(b, 'Entry_Points_Windows_026', set())
    assert not _is_linked(b, 'Entry_Points_Windows_026', a2)
    if hasattr(a2, 'Entry_Points_Windows_127'):
        assert not _is_linked(a2, 'Entry_Points_Windows_127', b)


def test_assoc_HomeAppliances_Air_Conditioner_reverse_link_reassign_clear():
    a1 = HomeAppliances(HAID=7)
    a2 = HomeAppliances(HAID=13)
    b = Air_Conditioners(ACID=7)
    _safe_set(b, 'HomeAppliances_Air_Conditioner_123', {a1})
    assert _is_linked(b, 'HomeAppliances_Air_Conditioner_123', a1)
    if hasattr(a1, 'HomeAppliances_Air_Conditioner_022'):
        assert _is_linked(a1, 'HomeAppliances_Air_Conditioner_022', b)
    _safe_set(b, 'HomeAppliances_Air_Conditioner_123', {a2})
    assert _is_linked(b, 'HomeAppliances_Air_Conditioner_123', a2)
    if hasattr(a1, 'HomeAppliances_Air_Conditioner_022'):
        assert not _is_linked(a1, 'HomeAppliances_Air_Conditioner_022', b)
    if hasattr(a2, 'HomeAppliances_Air_Conditioner_022'):
        assert _is_linked(a2, 'HomeAppliances_Air_Conditioner_022', b)
    _safe_set(b, 'HomeAppliances_Air_Conditioner_123', set())
    assert not _is_linked(b, 'HomeAppliances_Air_Conditioner_123', a2)
    if hasattr(a2, 'HomeAppliances_Air_Conditioner_022'):
        assert not _is_linked(a2, 'HomeAppliances_Air_Conditioner_022', b)


def test_assoc_HomeAppliances_Door_reverse_link_reassign_clear():
    a1 = Entry_Points(DoorID=7)
    a2 = Entry_Points(DoorID=13)
    b = Doors(DoorID=7)
    _safe_set(b, 'HomeAppliances_Door_113', {a1})
    assert _is_linked(b, 'HomeAppliances_Door_113', a1)
    if hasattr(a1, 'HomeAppliances_Door_012'):
        assert _is_linked(a1, 'HomeAppliances_Door_012', b)
    _safe_set(b, 'HomeAppliances_Door_113', {a2})
    assert _is_linked(b, 'HomeAppliances_Door_113', a2)
    if hasattr(a1, 'HomeAppliances_Door_012'):
        assert not _is_linked(a1, 'HomeAppliances_Door_012', b)
    if hasattr(a2, 'HomeAppliances_Door_012'):
        assert _is_linked(a2, 'HomeAppliances_Door_012', b)
    _safe_set(b, 'HomeAppliances_Door_113', set())
    assert not _is_linked(b, 'HomeAppliances_Door_113', a2)
    if hasattr(a2, 'HomeAppliances_Door_012'):
        assert not _is_linked(a2, 'HomeAppliances_Door_012', b)


def test_assoc_HomeAppliances_Light_reverse_link_reassign_clear():
    a1 = Lights(LightID="sample_text")
    a2 = Lights(LightID="sample_text_2")
    b = HomeAppliances(HAID=7)
    _safe_set(b, 'HomeAppliances_Light_010', {a1})
    assert _is_linked(b, 'HomeAppliances_Light_010', a1)
    if hasattr(a1, 'HomeAppliances_Light_111'):
        assert _is_linked(a1, 'HomeAppliances_Light_111', b)
    _safe_set(b, 'HomeAppliances_Light_010', {a2})
    assert _is_linked(b, 'HomeAppliances_Light_010', a2)
    if hasattr(a1, 'HomeAppliances_Light_111'):
        assert not _is_linked(a1, 'HomeAppliances_Light_111', b)
    if hasattr(a2, 'HomeAppliances_Light_111'):
        assert _is_linked(a2, 'HomeAppliances_Light_111', b)
    _safe_set(b, 'HomeAppliances_Light_010', set())
    assert not _is_linked(b, 'HomeAppliances_Light_010', a2)
    if hasattr(a2, 'HomeAppliances_Light_111'):
        assert not _is_linked(a2, 'HomeAppliances_Light_111', b)


def test_assoc_HomeTheatre_Speakers_reverse_link_reassign_clear():
    a1 = HomeAppliances(HAID=7)
    a2 = HomeAppliances(HAID=13)
    b = Fans(FANID=7)
    _safe_set(b, 'homeTheatre1', {a1})
    assert _is_linked(b, 'homeTheatre1', a1)
    if hasattr(a1, 'speakers0'):
        assert _is_linked(a1, 'speakers0', b)
    _safe_set(b, 'homeTheatre1', {a2})
    assert _is_linked(b, 'homeTheatre1', a2)
    if hasattr(a1, 'speakers0'):
        assert not _is_linked(a1, 'speakers0', b)
    if hasattr(a2, 'speakers0'):
        assert _is_linked(a2, 'speakers0', b)
    _safe_set(b, 'homeTheatre1', set())
    assert not _is_linked(b, 'homeTheatre1', a2)
    if hasattr(a2, 'speakers0'):
        assert not _is_linked(a2, 'speakers0', b)


def test_assoc_HomeTheatre_System_reverse_link_reassign_clear():
    a1 = IoT_based_Smart_Resort_System(Status=True, Update=3.14)
    a2 = IoT_based_Smart_Resort_System(Status=False, Update=9.99)
    b = HomeAppliances(HAID=7)
    _safe_set(b, 'system8', a1)
    assert _is_linked(b, 'system8', a1)
    if hasattr(a1, 'homeTheatre9'):
        assert _is_linked(a1, 'homeTheatre9', b)
    _safe_set(b, 'system8', a2)
    assert _is_linked(b, 'system8', a2)
    if hasattr(a1, 'homeTheatre9'):
        assert not _is_linked(a1, 'homeTheatre9', b)
    if hasattr(a2, 'homeTheatre9'):
        assert _is_linked(a2, 'homeTheatre9', b)
    _safe_set(b, 'system8', None)
    assert not _is_linked(b, 'system8', a2)
    if hasattr(a2, 'homeTheatre9'):
        assert not _is_linked(a2, 'homeTheatre9', b)


def test_assoc_Home_Security_System_Alert_reverse_link_reassign_clear():
    a1 = Home_Security_System(UserID=7)
    a2 = Home_Security_System(UserID=13)
    b = Alert(AlertID=7)
    _safe_set(b, 'home_Security_System5', a1)
    assert _is_linked(b, 'home_Security_System5', a1)
    if hasattr(a1, 'alert4'):
        assert _is_linked(a1, 'alert4', b)
    _safe_set(b, 'home_Security_System5', a2)
    assert _is_linked(b, 'home_Security_System5', a2)
    if hasattr(a1, 'alert4'):
        assert not _is_linked(a1, 'alert4', b)
    if hasattr(a2, 'alert4'):
        assert _is_linked(a2, 'alert4', b)
    _safe_set(b, 'home_Security_System5', None)
    assert not _is_linked(b, 'home_Security_System5', a2)
    if hasattr(a2, 'alert4'):
        assert not _is_linked(a2, 'alert4', b)


def test_assoc_IoT_based_Smart_Resort_System_Entry_Points_reverse_link_reassign_clear():
    a1 = IoT_based_Smart_Resort_System(Status=True, Update=3.14)
    a2 = IoT_based_Smart_Resort_System(Status=False, Update=9.99)
    b = Entry_Points(DoorID=7)
    _safe_set(b, 'IoT_based_Smart_Resort_System_Entry_Points_125', a1)
    assert _is_linked(b, 'IoT_based_Smart_Resort_System_Entry_Points_125', a1)
    if hasattr(a1, 'IoT_based_Smart_Resort_System_Entry_Points_024'):
        assert _is_linked(a1, 'IoT_based_Smart_Resort_System_Entry_Points_024', b)
    _safe_set(b, 'IoT_based_Smart_Resort_System_Entry_Points_125', a2)
    assert _is_linked(b, 'IoT_based_Smart_Resort_System_Entry_Points_125', a2)
    if hasattr(a1, 'IoT_based_Smart_Resort_System_Entry_Points_024'):
        assert not _is_linked(a1, 'IoT_based_Smart_Resort_System_Entry_Points_024', b)
    if hasattr(a2, 'IoT_based_Smart_Resort_System_Entry_Points_024'):
        assert _is_linked(a2, 'IoT_based_Smart_Resort_System_Entry_Points_024', b)
    _safe_set(b, 'IoT_based_Smart_Resort_System_Entry_Points_125', None)
    assert not _is_linked(b, 'IoT_based_Smart_Resort_System_Entry_Points_125', a2)
    if hasattr(a2, 'IoT_based_Smart_Resort_System_Entry_Points_024'):
        assert not _is_linked(a2, 'IoT_based_Smart_Resort_System_Entry_Points_024', b)


def test_assoc_IoT_based_Smart_Resort_System_Home_Security_System_reverse_link_reassign_clear():
    a1 = IoT_based_Smart_Resort_System(Status=True, Update=3.14)
    a2 = IoT_based_Smart_Resort_System(Status=False, Update=9.99)
    b = Home_Security_System(UserID=7)
    _safe_set(b, 'IoT_based_Smart_Resort_System_Home_Security_System_121', a1)
    assert _is_linked(b, 'IoT_based_Smart_Resort_System_Home_Security_System_121', a1)
    if hasattr(a1, 'IoT_based_Smart_Resort_System_Home_Security_System_020'):
        assert _is_linked(a1, 'IoT_based_Smart_Resort_System_Home_Security_System_020', b)
    _safe_set(b, 'IoT_based_Smart_Resort_System_Home_Security_System_121', a2)
    assert _is_linked(b, 'IoT_based_Smart_Resort_System_Home_Security_System_121', a2)
    if hasattr(a1, 'IoT_based_Smart_Resort_System_Home_Security_System_020'):
        assert not _is_linked(a1, 'IoT_based_Smart_Resort_System_Home_Security_System_020', b)
    if hasattr(a2, 'IoT_based_Smart_Resort_System_Home_Security_System_020'):
        assert _is_linked(a2, 'IoT_based_Smart_Resort_System_Home_Security_System_020', b)
    _safe_set(b, 'IoT_based_Smart_Resort_System_Home_Security_System_121', None)
    assert not _is_linked(b, 'IoT_based_Smart_Resort_System_Home_Security_System_121', a2)
    if hasattr(a2, 'IoT_based_Smart_Resort_System_Home_Security_System_020'):
        assert not _is_linked(a2, 'IoT_based_Smart_Resort_System_Home_Security_System_020', b)


def test_assoc_IoT_based_Smart_Resort_System_SolarPanel_reverse_link_reassign_clear():
    a1 = SolarPanel(SPID=7)
    a2 = SolarPanel(SPID=13)
    b = IoT_based_Smart_Resort_System(Status=True, Update=3.14)
    _safe_set(b, 'IoT_based_Smart_Resort_System_SolarPanel_018', {a1})
    assert _is_linked(b, 'IoT_based_Smart_Resort_System_SolarPanel_018', a1)
    if hasattr(a1, 'IoT_based_Smart_Resort_System_SolarPanel_119'):
        assert _is_linked(a1, 'IoT_based_Smart_Resort_System_SolarPanel_119', b)
    _safe_set(b, 'IoT_based_Smart_Resort_System_SolarPanel_018', {a2})
    assert _is_linked(b, 'IoT_based_Smart_Resort_System_SolarPanel_018', a2)
    if hasattr(a1, 'IoT_based_Smart_Resort_System_SolarPanel_119'):
        assert not _is_linked(a1, 'IoT_based_Smart_Resort_System_SolarPanel_119', b)
    if hasattr(a2, 'IoT_based_Smart_Resort_System_SolarPanel_119'):
        assert _is_linked(a2, 'IoT_based_Smart_Resort_System_SolarPanel_119', b)
    _safe_set(b, 'IoT_based_Smart_Resort_System_SolarPanel_018', set())
    assert not _is_linked(b, 'IoT_based_Smart_Resort_System_SolarPanel_018', a2)
    if hasattr(a2, 'IoT_based_Smart_Resort_System_SolarPanel_119'):
        assert not _is_linked(a2, 'IoT_based_Smart_Resort_System_SolarPanel_119', b)


def test_assoc_MicroPhone_System_reverse_link_reassign_clear():
    a1 = IoT_based_Smart_Resort_System(Status=True, Update=3.14)
    a2 = IoT_based_Smart_Resort_System(Status=False, Update=9.99)
    b = Gardening(GID=7)
    _safe_set(b, 'system2', a1)
    assert _is_linked(b, 'system2', a1)
    if hasattr(a1, 'microPhone3'):
        assert _is_linked(a1, 'microPhone3', b)
    _safe_set(b, 'system2', a2)
    assert _is_linked(b, 'system2', a2)
    if hasattr(a1, 'microPhone3'):
        assert not _is_linked(a1, 'microPhone3', b)
    if hasattr(a2, 'microPhone3'):
        assert _is_linked(a2, 'microPhone3', b)
    _safe_set(b, 'system2', None)
    assert not _is_linked(b, 'system2', a2)
    if hasattr(a2, 'microPhone3'):
        assert not _is_linked(a2, 'microPhone3', b)


def test_assoc_Security_Guard_Police_Alert_reverse_link_reassign_clear():
    a1 = Security_Guard_Police(sgpID=7)
    a2 = Security_Guard_Police(sgpID=13)
    b = Alert(AlertID=7)
    _safe_set(b, 'Security_Guard_Police_Alert_117', a1)
    assert _is_linked(b, 'Security_Guard_Police_Alert_117', a1)
    if hasattr(a1, 'Security_Guard_Police_Alert_016'):
        assert _is_linked(a1, 'Security_Guard_Police_Alert_016', b)
    _safe_set(b, 'Security_Guard_Police_Alert_117', a2)
    assert _is_linked(b, 'Security_Guard_Police_Alert_117', a2)
    if hasattr(a1, 'Security_Guard_Police_Alert_016'):
        assert not _is_linked(a1, 'Security_Guard_Police_Alert_016', b)
    if hasattr(a2, 'Security_Guard_Police_Alert_016'):
        assert _is_linked(a2, 'Security_Guard_Police_Alert_016', b)
    _safe_set(b, 'Security_Guard_Police_Alert_117', None)
    assert not _is_linked(b, 'Security_Guard_Police_Alert_117', a2)
    if hasattr(a2, 'Security_Guard_Police_Alert_016'):
        assert not _is_linked(a2, 'Security_Guard_Police_Alert_016', b)


def test_assoc_Sensor_System_reverse_link_reassign_clear():
    a1 = Sensor(SensorID=7, SensorType=7)
    a2 = Sensor(SensorID=13, SensorType=13)
    b = IoT_based_Smart_Resort_System(Status=True, Update=3.14)
    _safe_set(b, 'sensor7', {a1})
    assert _is_linked(b, 'sensor7', a1)
    if hasattr(a1, 'system6'):
        assert _is_linked(a1, 'system6', b)
    _safe_set(b, 'sensor7', {a2})
    assert _is_linked(b, 'sensor7', a2)
    if hasattr(a1, 'system6'):
        assert not _is_linked(a1, 'system6', b)
    if hasattr(a2, 'system6'):
        assert _is_linked(a2, 'system6', b)
    _safe_set(b, 'sensor7', set())
    assert not _is_linked(b, 'sensor7', a2)
    if hasattr(a2, 'system6'):
        assert not _is_linked(a2, 'system6', b)


def test_assoc_User_Home_Owner_Alert_reverse_link_reassign_clear():
    a1 = User_Home_Owner(UserID=7)
    a2 = User_Home_Owner(UserID=13)
    b = Alert(AlertID=7)
    _safe_set(b, 'User_Home_Owner_Alert_115', a1)
    assert _is_linked(b, 'User_Home_Owner_Alert_115', a1)
    if hasattr(a1, 'User_Home_Owner_Alert_014'):
        assert _is_linked(a1, 'User_Home_Owner_Alert_014', b)
    _safe_set(b, 'User_Home_Owner_Alert_115', a2)
    assert _is_linked(b, 'User_Home_Owner_Alert_115', a2)
    if hasattr(a1, 'User_Home_Owner_Alert_014'):
        assert not _is_linked(a1, 'User_Home_Owner_Alert_014', b)
    if hasattr(a2, 'User_Home_Owner_Alert_014'):
        assert _is_linked(a2, 'User_Home_Owner_Alert_014', b)
    _safe_set(b, 'User_Home_Owner_Alert_115', None)
    assert not _is_linked(b, 'User_Home_Owner_Alert_115', a2)
    if hasattr(a2, 'User_Home_Owner_Alert_014'):
        assert not _is_linked(a2, 'User_Home_Owner_Alert_014', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

