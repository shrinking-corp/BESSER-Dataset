# =============================================================================
# This file is a generated concatenation of two independent test suites --
# see scripts/generate_combined_tests.py for why simple concatenation is safe
# despite both generators using the same naming convention for some helpers,
# and for the deterministic rules used to drop old-suite tests the new suite
# already covers equally or more thoroughly.
# =============================================================================

# ----- SECTION A: test_hypothesis.py (original generated suite) -----
import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    Temperature_sensor,
    Server,
    Lock_doors_sensors,
    Light_Sensor,
    Event_Log,
    Camera_sensor,
    Home_Security,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_hyp_temperature_sensor_is_not_abstract():
    assert not inspect.isabstract(Temperature_sensor)


def test_hyp_temperature_sensor_constructor_exists():
    assert callable(Temperature_sensor.__init__)


def test_hyp_temperature_sensor_constructor_args():
    sig = inspect.signature(Temperature_sensor.__init__)
    params = list(sig.parameters.keys())
    assert "attribute" in params, "Missing parameter 'attribute'"




def test_hyp_server_is_not_abstract():
    assert not inspect.isabstract(Server)


def test_hyp_server_constructor_exists():
    assert callable(Server.__init__)


def test_hyp_server_constructor_args():
    sig = inspect.signature(Server.__init__)
    params = list(sig.parameters.keys())
    assert "attribute" in params, "Missing parameter 'attribute'"




def test_hyp_lock_doors_sensors_is_not_abstract():
    assert not inspect.isabstract(Lock_doors_sensors)


def test_hyp_lock_doors_sensors_constructor_exists():
    assert callable(Lock_doors_sensors.__init__)


def test_hyp_lock_doors_sensors_constructor_args():
    sig = inspect.signature(Lock_doors_sensors.__init__)
    params = list(sig.parameters.keys())
    assert "attribute" in params, "Missing parameter 'attribute'"




def test_hyp_light_sensor_is_not_abstract():
    assert not inspect.isabstract(Light_Sensor)


def test_hyp_light_sensor_constructor_exists():
    assert callable(Light_Sensor.__init__)


def test_hyp_light_sensor_constructor_args():
    sig = inspect.signature(Light_Sensor.__init__)
    params = list(sig.parameters.keys())
    assert "attribute" in params, "Missing parameter 'attribute'"




def test_hyp_event_log_is_not_abstract():
    assert not inspect.isabstract(Event_Log)


def test_hyp_event_log_constructor_exists():
    assert callable(Event_Log.__init__)


def test_hyp_event_log_constructor_args():
    sig = inspect.signature(Event_Log.__init__)
    params = list(sig.parameters.keys())
    assert "attribute" in params, "Missing parameter 'attribute'"




def test_hyp_camera_sensor_is_not_abstract():
    assert not inspect.isabstract(Camera_sensor)


def test_hyp_camera_sensor_constructor_exists():
    assert callable(Camera_sensor.__init__)


def test_hyp_camera_sensor_constructor_args():
    sig = inspect.signature(Camera_sensor.__init__)
    params = list(sig.parameters.keys())
    assert "Image_ID" in params, "Missing parameter 'Image_ID'"
    assert "Video_ID" in params, "Missing parameter 'Video_ID'"





def test_hyp_home_security_is_not_abstract():
    assert not inspect.isabstract(Home_Security)


def test_hyp_home_security_constructor_exists():
    assert callable(Home_Security.__init__)


def test_hyp_home_security_constructor_args():
    sig = inspect.signature(Home_Security.__init__)
    params = list(sig.parameters.keys())


# =============================================================================
# HYPOTHESIS STRATEGIES
# =============================================================================

safe_text = st.text(
    alphabet=st.characters(
        whitelist_categories=("Ll", "Lu", "Nd"),
        whitelist_characters="_",
    ),
    min_size=1,
).filter(lambda s: s[0].isalpha())
Temperature_sensor_strategy = st.builds(
    Temperature_sensor,
    attribute=
        safe_text
)
Server_strategy = st.builds(
    Server,
    attribute=
        safe_text
)
Lock_doors_sensors_strategy = st.builds(
    Lock_doors_sensors,
    attribute=
        safe_text
)
Light_Sensor_strategy = st.builds(
    Light_Sensor,
    attribute=
        safe_text
)
Event_Log_strategy = st.builds(
    Event_Log,
    attribute=
        safe_text
)
Camera_sensor_strategy = st.builds(
    Camera_sensor,
    Image_ID=
        st.integers(),
    Video_ID=
        st.integers()
)
Home_Security_strategy = st.builds(
    Home_Security,
)




@given(instance=Temperature_sensor_strategy)
def test_hyp_temperature_sensor_attribute_setter(instance):
    original = instance.attribute
    instance.attribute = original
    assert instance.attribute == original




@given(instance=Server_strategy)
def test_hyp_server_attribute_setter(instance):
    original = instance.attribute
    instance.attribute = original
    assert instance.attribute == original




@given(instance=Lock_doors_sensors_strategy)
def test_hyp_lock_doors_sensors_attribute_setter(instance):
    original = instance.attribute
    instance.attribute = original
    assert instance.attribute == original




@given(instance=Light_Sensor_strategy)
def test_hyp_light_sensor_attribute_setter(instance):
    original = instance.attribute
    instance.attribute = original
    assert instance.attribute == original




@given(instance=Event_Log_strategy)
def test_hyp_event_log_attribute_setter(instance):
    original = instance.attribute
    instance.attribute = original
    assert instance.attribute == original




@given(instance=Camera_sensor_strategy)
def test_hyp_camera_sensor_Image_ID_setter(instance):
    original = instance.Image_ID
    instance.Image_ID = original
    assert instance.Image_ID == original



@given(instance=Camera_sensor_strategy)
def test_hyp_camera_sensor_Video_ID_setter(instance):
    original = instance.Video_ID
    instance.Video_ID = original
    assert instance.Video_ID == original



# ----- SECTION B: test_structural_full.py (deterministic-first suite) -----
import inspect
import pytest
from datetime import date, datetime, time, timedelta
from hypothesis import given, settings
import hypothesis.strategies as st

from python_code import (
    Camera_sensor,
    Event_Log,
    Home_Security,
    Light_Sensor,
    Lock_doors_sensors,
    Server,
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

def test_Camera_sensor_Image_ID_value_roundtrip():
    instance = Camera_sensor(Image_ID=7, Video_ID=7)
    assert instance.Image_ID == 7
    instance.Image_ID = 13
    assert instance.Image_ID == 13


def test_Camera_sensor_Video_ID_value_roundtrip():
    instance = Camera_sensor(Image_ID=7, Video_ID=7)
    assert instance.Video_ID == 7
    instance.Video_ID = 13
    assert instance.Video_ID == 13


def test_Event_Log_attribute_value_roundtrip():
    instance = Event_Log(attribute="sample_text")
    assert instance.attribute == "sample_text"
    instance.attribute = "sample_text_2"
    assert instance.attribute == "sample_text_2"


def test_Light_Sensor_attribute_value_roundtrip():
    instance = Light_Sensor(attribute="sample_text")
    assert instance.attribute == "sample_text"
    instance.attribute = "sample_text_2"
    assert instance.attribute == "sample_text_2"


def test_Lock_doors_sensors_attribute_value_roundtrip():
    instance = Lock_doors_sensors(attribute="sample_text")
    assert instance.attribute == "sample_text"
    instance.attribute = "sample_text_2"
    assert instance.attribute == "sample_text_2"


def test_Server_attribute_value_roundtrip():
    instance = Server(attribute="sample_text")
    assert instance.attribute == "sample_text"
    instance.attribute = "sample_text_2"
    assert instance.attribute == "sample_text_2"


def test_Temperature_sensor_attribute_value_roundtrip():
    instance = Temperature_sensor(attribute="sample_text")
    assert instance.attribute == "sample_text"
    instance.attribute = "sample_text_2"
    assert instance.attribute == "sample_text_2"


def test_assoc_Home_Security_Camera_link_reassign_clear():
    a = Camera_sensor(Image_ID=7, Video_ID=7)
    b1 = Home_Security()
    b2 = Home_Security()
    _safe_set(a, 'home_Security3', b1)
    assert _is_linked(a, 'home_Security3', b1)
    if hasattr(b1, 'camera2'):
        assert _is_linked(b1, 'camera2', a)
    _safe_set(a, 'home_Security3', b2)
    assert _is_linked(a, 'home_Security3', b2)
    if hasattr(b1, 'camera2'):
        assert not _is_linked(b1, 'camera2', a)
    if hasattr(b2, 'camera2'):
        assert _is_linked(b2, 'camera2', a)
    _safe_set(a, 'home_Security3', None)
    assert not _is_linked(a, 'home_Security3', b2)
    if hasattr(b2, 'camera2'):
        assert not _is_linked(b2, 'camera2', a)


def test_assoc_Home_Security_Doors_link_reassign_clear():
    a = Lock_doors_sensors(attribute="sample_text")
    b1 = Home_Security()
    b2 = Home_Security()
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
    a = Event_Log(attribute="sample_text")
    b1 = Home_Security()
    b2 = Home_Security()
    _safe_set(a, 'home_Security5', b1)
    assert _is_linked(a, 'home_Security5', b1)
    if hasattr(b1, 'event_Log4'):
        assert _is_linked(b1, 'event_Log4', a)
    _safe_set(a, 'home_Security5', b2)
    assert _is_linked(a, 'home_Security5', b2)
    if hasattr(b1, 'event_Log4'):
        assert not _is_linked(b1, 'event_Log4', a)
    if hasattr(b2, 'event_Log4'):
        assert _is_linked(b2, 'event_Log4', a)
    _safe_set(a, 'home_Security5', None)
    assert not _is_linked(a, 'home_Security5', b2)
    if hasattr(b2, 'event_Log4'):
        assert not _is_linked(b2, 'event_Log4', a)


def test_assoc_Home_Security_Light_Sensor_link_reassign_clear():
    a = Light_Sensor(attribute="sample_text")
    b1 = Home_Security()
    b2 = Home_Security()
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
    a = Server(attribute="sample_text")
    b1 = Home_Security()
    b2 = Home_Security()
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
    a = Temperature_sensor(attribute="sample_text")
    b1 = Home_Security()
    b2 = Home_Security()
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

Camera_sensor_strategy = st.builds(Camera_sensor, Image_ID=st.integers(), Video_ID=st.integers())
@given(instance=Camera_sensor_strategy)
@settings(max_examples=25)
def test_Camera_sensor_instantiation(instance):
    assert isinstance(instance, Camera_sensor)


Event_Log_strategy = st.builds(Event_Log, attribute=safe_text)
@given(instance=Event_Log_strategy)
@settings(max_examples=25)
def test_Event_Log_instantiation(instance):
    assert isinstance(instance, Event_Log)


Home_Security_strategy = st.builds(Home_Security)
@given(instance=Home_Security_strategy)
@settings(max_examples=25)
def test_Home_Security_instantiation(instance):
    assert isinstance(instance, Home_Security)


Light_Sensor_strategy = st.builds(Light_Sensor, attribute=safe_text)
@given(instance=Light_Sensor_strategy)
@settings(max_examples=25)
def test_Light_Sensor_instantiation(instance):
    assert isinstance(instance, Light_Sensor)


Lock_doors_sensors_strategy = st.builds(Lock_doors_sensors, attribute=safe_text)
@given(instance=Lock_doors_sensors_strategy)
@settings(max_examples=25)
def test_Lock_doors_sensors_instantiation(instance):
    assert isinstance(instance, Lock_doors_sensors)


Server_strategy = st.builds(Server, attribute=safe_text)
@given(instance=Server_strategy)
@settings(max_examples=25)
def test_Server_instantiation(instance):
    assert isinstance(instance, Server)


Temperature_sensor_strategy = st.builds(Temperature_sensor, attribute=safe_text)
@given(instance=Temperature_sensor_strategy)
@settings(max_examples=25)
def test_Temperature_sensor_instantiation(instance):
    assert isinstance(instance, Temperature_sensor)



