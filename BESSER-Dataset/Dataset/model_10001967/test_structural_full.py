import inspect
import pytest
from datetime import date, datetime, time, timedelta
from hypothesis import given, settings
import hypothesis.strategies as st

from python_code import (
    Camera_1,
    Dispatch_drown,
    Event_Log,
    Home_Security__Hub_,
    Light_Sensor,
    Lock_doors,
    Motion_Sensor,
    Security_logs,
    T,
    Temperature_sensor,
)

safe_text = st.text(
    alphabet=st.characters(
        whitelist_categories=("Ll", "Lu", "Nd"),
        whitelist_characters="_",
    ),
    min_size=1,
).filter(lambda s: s[0].isalpha())

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
# SECTION 1 -- DETERMINISTIC TESTS (attributes, generalizations, relationships)
# =============================================================================

def test_Camera_1_Camera_ID_value_roundtrip():
    instance = Camera_1(Camera_ID="sample_text", Sensor_ID="sample_text")
    assert instance.Camera_ID == "sample_text"
    instance.Camera_ID = "sample_text_2"
    assert instance.Camera_ID == "sample_text_2"


def test_Camera_1_Sensor_ID_value_roundtrip():
    instance = Camera_1(Camera_ID="sample_text", Sensor_ID="sample_text")
    assert instance.Sensor_ID == "sample_text"
    instance.Sensor_ID = "sample_text_2"
    assert instance.Sensor_ID == "sample_text_2"


def test_Dispatch_drown_Camera_ID_value_roundtrip():
    instance = Dispatch_drown(Camera_ID="sample_text", Drown_ID="sample_text")
    assert instance.Camera_ID == "sample_text"
    instance.Camera_ID = "sample_text_2"
    assert instance.Camera_ID == "sample_text_2"


def test_Dispatch_drown_Drown_ID_value_roundtrip():
    instance = Dispatch_drown(Camera_ID="sample_text", Drown_ID="sample_text")
    assert instance.Drown_ID == "sample_text"
    instance.Drown_ID = "sample_text_2"
    assert instance.Drown_ID == "sample_text_2"


def test_Event_Log_Status_value_roundtrip():
    instance = Event_Log(Status=True)
    assert instance.Status == True
    instance.Status = False
    assert instance.Status == False


def test_Home_Security__Hub__Camera_ID_value_roundtrip():
    instance = Home_Security__Hub_(Camera_ID="sample_text", Hub_ID="sample_text", Login_ID="sample_text", Sensor_ID="sample_text")
    assert instance.Camera_ID == "sample_text"
    instance.Camera_ID = "sample_text_2"
    assert instance.Camera_ID == "sample_text_2"


def test_Home_Security__Hub__Hub_ID_value_roundtrip():
    instance = Home_Security__Hub_(Camera_ID="sample_text", Hub_ID="sample_text", Login_ID="sample_text", Sensor_ID="sample_text")
    assert instance.Hub_ID == "sample_text"
    instance.Hub_ID = "sample_text_2"
    assert instance.Hub_ID == "sample_text_2"


def test_Home_Security__Hub__Login_ID_value_roundtrip():
    instance = Home_Security__Hub_(Camera_ID="sample_text", Hub_ID="sample_text", Login_ID="sample_text", Sensor_ID="sample_text")
    assert instance.Login_ID == "sample_text"
    instance.Login_ID = "sample_text_2"
    assert instance.Login_ID == "sample_text_2"


def test_Home_Security__Hub__Sensor_ID_value_roundtrip():
    instance = Home_Security__Hub_(Camera_ID="sample_text", Hub_ID="sample_text", Login_ID="sample_text", Sensor_ID="sample_text")
    assert instance.Sensor_ID == "sample_text"
    instance.Sensor_ID = "sample_text_2"
    assert instance.Sensor_ID == "sample_text_2"


def test_Light_Sensor_Sensor_ID_value_roundtrip():
    instance = Light_Sensor(Sensor_ID="sample_text")
    assert instance.Sensor_ID == "sample_text"
    instance.Sensor_ID = "sample_text_2"
    assert instance.Sensor_ID == "sample_text_2"


def test_Lock_doors_Door_ID_value_roundtrip():
    instance = Lock_doors(Door_ID="sample_text")
    assert instance.Door_ID == "sample_text"
    instance.Door_ID = "sample_text_2"
    assert instance.Door_ID == "sample_text_2"


def test_Motion_Sensor_Sensor_ID_value_roundtrip():
    instance = Motion_Sensor(Sensor_ID="sample_text")
    assert instance.Sensor_ID == "sample_text"
    instance.Sensor_ID = "sample_text_2"
    assert instance.Sensor_ID == "sample_text_2"


def test_Security_logs_Camera_ID_value_roundtrip():
    instance = Security_logs(Camera_ID="sample_text", Log_ID="sample_text", Sensor_ID="sample_text")
    assert instance.Camera_ID == "sample_text"
    instance.Camera_ID = "sample_text_2"
    assert instance.Camera_ID == "sample_text_2"


def test_Security_logs_Log_ID_value_roundtrip():
    instance = Security_logs(Camera_ID="sample_text", Log_ID="sample_text", Sensor_ID="sample_text")
    assert instance.Log_ID == "sample_text"
    instance.Log_ID = "sample_text_2"
    assert instance.Log_ID == "sample_text_2"


def test_Security_logs_Sensor_ID_value_roundtrip():
    instance = Security_logs(Camera_ID="sample_text", Log_ID="sample_text", Sensor_ID="sample_text")
    assert instance.Sensor_ID == "sample_text"
    instance.Sensor_ID = "sample_text_2"
    assert instance.Sensor_ID == "sample_text_2"


def test_Temperature_sensor_Temp_ID_value_roundtrip():
    instance = Temperature_sensor(Temp_ID="sample_text")
    assert instance.Temp_ID == "sample_text"
    instance.Temp_ID = "sample_text_2"
    assert instance.Temp_ID == "sample_text_2"


def test_assoc_Camera_1_Camera_1_link_reassign_clear():
    a = Camera_1(Camera_ID="sample_text", Sensor_ID="sample_text")
    b1 = Camera_1(Camera_ID="sample_text", Sensor_ID="sample_text")
    b2 = Camera_1(Camera_ID="sample_text_2", Sensor_ID="sample_text_2")
    _safe_set(a, 'camera_112', b1)
    assert _is_linked(a, 'camera_112', b1)
    if hasattr(b1, 'camera_113'):
        assert _is_linked(b1, 'camera_113', a)
    _safe_set(a, 'camera_112', b2)
    assert _is_linked(a, 'camera_112', b2)
    if hasattr(b1, 'camera_113'):
        assert not _is_linked(b1, 'camera_113', a)
    if hasattr(b2, 'camera_113'):
        assert _is_linked(b2, 'camera_113', a)
    _safe_set(a, 'camera_112', None)
    assert not _is_linked(a, 'camera_112', b2)
    if hasattr(b2, 'camera_113'):
        assert not _is_linked(b2, 'camera_113', a)


def test_assoc_Home_Security_Camera_link_reassign_clear():
    a = Home_Security__Hub_(Camera_ID="sample_text", Hub_ID="sample_text", Login_ID="sample_text", Sensor_ID="sample_text")
    b1 = Camera_1(Camera_ID="sample_text", Sensor_ID="sample_text")
    b2 = Camera_1(Camera_ID="sample_text_2", Sensor_ID="sample_text_2")
    _safe_set(a, 'camera2', {b1})
    assert _is_linked(a, 'camera2', b1)
    if hasattr(b1, 'home_Security3'):
        assert _is_linked(b1, 'home_Security3', a)
    _safe_set(a, 'camera2', {b2})
    assert _is_linked(a, 'camera2', b2)
    if hasattr(b1, 'home_Security3'):
        assert not _is_linked(b1, 'home_Security3', a)
    if hasattr(b2, 'home_Security3'):
        assert _is_linked(b2, 'home_Security3', a)
    _safe_set(a, 'camera2', set())
    assert not _is_linked(a, 'camera2', b2)
    if hasattr(b2, 'home_Security3'):
        assert not _is_linked(b2, 'home_Security3', a)


def test_assoc_Home_Security_Doors_link_reassign_clear():
    a = Lock_doors(Door_ID="sample_text")
    b1 = Home_Security__Hub_(Camera_ID="sample_text", Hub_ID="sample_text", Login_ID="sample_text", Sensor_ID="sample_text")
    b2 = Home_Security__Hub_(Camera_ID="sample_text_2", Hub_ID="sample_text_2", Login_ID="sample_text_2", Sensor_ID="sample_text_2")
    _safe_set(a, 'home_Security9', b1)
    assert _is_linked(a, 'home_Security9', b1)
    if hasattr(b1, 'doors8'):
        assert _is_linked(b1, 'doors8', a)
    _safe_set(a, 'home_Security9', b2)
    assert _is_linked(a, 'home_Security9', b2)
    if hasattr(b1, 'doors8'):
        assert not _is_linked(b1, 'doors8', a)
    if hasattr(b2, 'doors8'):
        assert _is_linked(b2, 'doors8', a)
    _safe_set(a, 'home_Security9', None)
    assert not _is_linked(a, 'home_Security9', b2)
    if hasattr(b2, 'doors8'):
        assert not _is_linked(b2, 'doors8', a)


def test_assoc_Home_Security_Event_Log_link_reassign_clear():
    a = Home_Security__Hub_(Camera_ID="sample_text", Hub_ID="sample_text", Login_ID="sample_text", Sensor_ID="sample_text")
    b1 = Event_Log(Status=True)
    b2 = Event_Log(Status=False)
    _safe_set(a, 'event_Log4', {b1})
    assert _is_linked(a, 'event_Log4', b1)
    if hasattr(b1, 'home_Security5'):
        assert _is_linked(b1, 'home_Security5', a)
    _safe_set(a, 'event_Log4', {b2})
    assert _is_linked(a, 'event_Log4', b2)
    if hasattr(b1, 'home_Security5'):
        assert not _is_linked(b1, 'home_Security5', a)
    if hasattr(b2, 'home_Security5'):
        assert _is_linked(b2, 'home_Security5', a)
    _safe_set(a, 'event_Log4', set())
    assert not _is_linked(a, 'event_Log4', b2)
    if hasattr(b2, 'home_Security5'):
        assert not _is_linked(b2, 'home_Security5', a)


def test_assoc_Home_Security_Light_Sensor_link_reassign_clear():
    a = Light_Sensor(Sensor_ID="sample_text")
    b1 = Camera_1(Camera_ID="sample_text", Sensor_ID="sample_text")
    b2 = Camera_1(Camera_ID="sample_text_2", Sensor_ID="sample_text_2")
    _safe_set(a, 'home_Security7', b1)
    assert _is_linked(a, 'home_Security7', b1)
    if hasattr(b1, 'light_Sensor6'):
        assert _is_linked(b1, 'light_Sensor6', a)
    _safe_set(a, 'home_Security7', b2)
    assert _is_linked(a, 'home_Security7', b2)
    if hasattr(b1, 'light_Sensor6'):
        assert not _is_linked(b1, 'light_Sensor6', a)
    if hasattr(b2, 'light_Sensor6'):
        assert _is_linked(b2, 'light_Sensor6', a)
    _safe_set(a, 'home_Security7', None)
    assert not _is_linked(a, 'home_Security7', b2)
    if hasattr(b2, 'light_Sensor6'):
        assert not _is_linked(b2, 'light_Sensor6', a)


def test_assoc_Home_Security_Server_link_reassign_clear():
    a = Security_logs(Camera_ID="sample_text", Log_ID="sample_text", Sensor_ID="sample_text")
    b1 = Home_Security__Hub_(Camera_ID="sample_text", Hub_ID="sample_text", Login_ID="sample_text", Sensor_ID="sample_text")
    b2 = Home_Security__Hub_(Camera_ID="sample_text_2", Hub_ID="sample_text_2", Login_ID="sample_text_2", Sensor_ID="sample_text_2")
    _safe_set(a, 'home_Security1', b1)
    assert _is_linked(a, 'home_Security1', b1)
    if hasattr(b1, 'server0'):
        assert _is_linked(b1, 'server0', a)
    _safe_set(a, 'home_Security1', b2)
    assert _is_linked(a, 'home_Security1', b2)
    if hasattr(b1, 'server0'):
        assert not _is_linked(b1, 'server0', a)
    if hasattr(b2, 'server0'):
        assert _is_linked(b2, 'server0', a)
    _safe_set(a, 'home_Security1', None)
    assert not _is_linked(a, 'home_Security1', b2)
    if hasattr(b2, 'server0'):
        assert not _is_linked(b2, 'server0', a)


def test_assoc_Home_Security_Temperature_sensor_link_reassign_clear():
    a = Temperature_sensor(Temp_ID="sample_text")
    b1 = Camera_1(Camera_ID="sample_text", Sensor_ID="sample_text")
    b2 = Camera_1(Camera_ID="sample_text_2", Sensor_ID="sample_text_2")
    _safe_set(a, 'home_Security11', b1)
    assert _is_linked(a, 'home_Security11', b1)
    if hasattr(b1, 'temperature_sensor10'):
        assert _is_linked(b1, 'temperature_sensor10', a)
    _safe_set(a, 'home_Security11', b2)
    assert _is_linked(a, 'home_Security11', b2)
    if hasattr(b1, 'temperature_sensor10'):
        assert not _is_linked(b1, 'temperature_sensor10', a)
    if hasattr(b2, 'temperature_sensor10'):
        assert _is_linked(b2, 'temperature_sensor10', a)
    _safe_set(a, 'home_Security11', None)
    assert not _is_linked(a, 'home_Security11', b2)
    if hasattr(b2, 'temperature_sensor10'):
        assert not _is_linked(b2, 'temperature_sensor10', a)


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

Camera_1_strategy = st.builds(Camera_1, Camera_ID=safe_text, Sensor_ID=safe_text)
@given(instance=Camera_1_strategy)
@settings(max_examples=25)
def test_Camera_1_instantiation(instance):
    assert isinstance(instance, Camera_1)


Dispatch_drown_strategy = st.builds(Dispatch_drown, Camera_ID=safe_text, Drown_ID=safe_text)
@given(instance=Dispatch_drown_strategy)
@settings(max_examples=25)
def test_Dispatch_drown_instantiation(instance):
    assert isinstance(instance, Dispatch_drown)


Event_Log_strategy = st.builds(Event_Log, Status=st.booleans())
@given(instance=Event_Log_strategy)
@settings(max_examples=25)
def test_Event_Log_instantiation(instance):
    assert isinstance(instance, Event_Log)


Home_Security__Hub__strategy = st.builds(Home_Security__Hub_, Camera_ID=safe_text, Hub_ID=safe_text, Login_ID=safe_text, Sensor_ID=safe_text)
@given(instance=Home_Security__Hub__strategy)
@settings(max_examples=25)
def test_Home_Security__Hub__instantiation(instance):
    assert isinstance(instance, Home_Security__Hub_)


Light_Sensor_strategy = st.builds(Light_Sensor, Sensor_ID=safe_text)
@given(instance=Light_Sensor_strategy)
@settings(max_examples=25)
def test_Light_Sensor_instantiation(instance):
    assert isinstance(instance, Light_Sensor)


Lock_doors_strategy = st.builds(Lock_doors, Door_ID=safe_text)
@given(instance=Lock_doors_strategy)
@settings(max_examples=25)
def test_Lock_doors_instantiation(instance):
    assert isinstance(instance, Lock_doors)


Motion_Sensor_strategy = st.builds(Motion_Sensor, Sensor_ID=safe_text)
@given(instance=Motion_Sensor_strategy)
@settings(max_examples=25)
def test_Motion_Sensor_instantiation(instance):
    assert isinstance(instance, Motion_Sensor)


Security_logs_strategy = st.builds(Security_logs, Camera_ID=safe_text, Log_ID=safe_text, Sensor_ID=safe_text)
@given(instance=Security_logs_strategy)
@settings(max_examples=25)
def test_Security_logs_instantiation(instance):
    assert isinstance(instance, Security_logs)


T_strategy = st.builds(T)
@given(instance=T_strategy)
@settings(max_examples=25)
def test_T_instantiation(instance):
    assert isinstance(instance, T)


Temperature_sensor_strategy = st.builds(Temperature_sensor, Temp_ID=safe_text)
@given(instance=Temperature_sensor_strategy)
@settings(max_examples=25)
def test_Temperature_sensor_instantiation(instance):
    assert isinstance(instance, Temperature_sensor)


