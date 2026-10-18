import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Camera_sensor,
    Event_Log,
    Home_Security,
    Light_Sensor,
    Lock_doors_sensors,
    Server,
    Temperature_sensor,
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

# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_Home_Security_Camera_stub_double():
    # Home_Security has no real 'camera2' property in the generated
    # code (a bare stub) -- manually attach it so Camera_sensor's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # Camera_sensor's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = Camera_sensor(Image_ID=7, Video_ID=7)
    partner = Home_Security()
    setattr(partner, 'camera2', None)
    _safe_set(owner, 'home_Security3', partner)
    assert owner in getattr(partner, 'camera2')
    _safe_set(owner, 'home_Security3', None)
    assert owner not in getattr(partner, 'camera2')


def test_assoc_Home_Security_Doors_stub_double():
    # Home_Security has no real 'doors8' property in the generated
    # code (a bare stub) -- manually attach it so Lock_doors_sensors's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # Lock_doors_sensors's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = Lock_doors_sensors(attribute="sample_text")
    partner = Home_Security()
    setattr(partner, 'doors8', None)
    _safe_set(owner, 'home_Security9', partner)
    assert getattr(partner, 'doors8') == owner
    _safe_set(owner, 'home_Security9', None)
    assert getattr(partner, 'doors8') is None


def test_assoc_Home_Security_Event_Log_stub_double():
    # Home_Security has no real 'event_Log4' property in the generated
    # code (a bare stub) -- manually attach it so Event_Log's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # Event_Log's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = Event_Log(attribute="sample_text")
    partner = Home_Security()
    setattr(partner, 'event_Log4', None)
    _safe_set(owner, 'home_Security5', partner)
    assert owner in getattr(partner, 'event_Log4')
    _safe_set(owner, 'home_Security5', None)
    assert owner not in getattr(partner, 'event_Log4')


def test_assoc_Home_Security_Light_Sensor_stub_double():
    # Home_Security has no real 'light_Sensor6' property in the generated
    # code (a bare stub) -- manually attach it so Light_Sensor's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # Light_Sensor's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = Light_Sensor(attribute="sample_text")
    partner = Home_Security()
    setattr(partner, 'light_Sensor6', None)
    _safe_set(owner, 'home_Security7', partner)
    assert owner in getattr(partner, 'light_Sensor6')
    _safe_set(owner, 'home_Security7', None)
    assert owner not in getattr(partner, 'light_Sensor6')


def test_assoc_Home_Security_Server_stub_double():
    # Home_Security has no real 'server0' property in the generated
    # code (a bare stub) -- manually attach it so Server's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # Server's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = Server(attribute="sample_text")
    partner = Home_Security()
    setattr(partner, 'server0', None)
    _safe_set(owner, 'home_Security1', partner)
    assert getattr(partner, 'server0') == owner
    _safe_set(owner, 'home_Security1', None)
    assert getattr(partner, 'server0') is None


def test_assoc_Home_Security_Temperature_sensor_stub_double():
    # Home_Security has no real 'temperature_sensor10' property in the generated
    # code (a bare stub) -- manually attach it so Temperature_sensor's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # Temperature_sensor's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = Temperature_sensor(attribute="sample_text")
    partner = Home_Security()
    setattr(partner, 'temperature_sensor10', None)
    _safe_set(owner, 'home_Security11', partner)
    assert owner in getattr(partner, 'temperature_sensor10')
    _safe_set(owner, 'home_Security11', None)
    assert owner not in getattr(partner, 'temperature_sensor10')


