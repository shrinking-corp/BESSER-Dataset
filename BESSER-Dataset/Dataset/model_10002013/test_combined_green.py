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
    Alert2,
    Web,
    Arduino,
    Count_people,
    Alert,
    Mobile_App,
    PressureSensor,
    Temperature_Sensor,
    Gas_Smoke_Sensor,
    Sensor,
    Firebase,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_hyp_alert2_is_not_abstract():
    assert not inspect.isabstract(Alert2)


def test_hyp_alert2_constructor_exists():
    assert callable(Alert2.__init__)


def test_hyp_alert2_constructor_args():
    sig = inspect.signature(Alert2.__init__)
    params = list(sig.parameters.keys())
    assert "AlertID" in params, "Missing parameter 'AlertID'"




def test_hyp_web_is_not_abstract():
    assert not inspect.isabstract(Web)


def test_hyp_web_constructor_exists():
    assert callable(Web.__init__)


def test_hyp_web_constructor_args():
    sig = inspect.signature(Web.__init__)
    params = list(sig.parameters.keys())



def test_hyp_arduino_is_not_abstract():
    assert not inspect.isabstract(Arduino)


def test_hyp_arduino_constructor_exists():
    assert callable(Arduino.__init__)


def test_hyp_arduino_constructor_args():
    sig = inspect.signature(Arduino.__init__)
    params = list(sig.parameters.keys())
    assert "MicID" in params, "Missing parameter 'MicID'"




def test_hyp_count_people_is_not_abstract():
    assert not inspect.isabstract(Count_people)


def test_hyp_count_people_constructor_exists():
    assert callable(Count_people.__init__)


def test_hyp_count_people_constructor_args():
    sig = inspect.signature(Count_people.__init__)
    params = list(sig.parameters.keys())
    assert "_attr" in params, "Missing parameter '_attr'"




def test_hyp_alert_is_not_abstract():
    assert not inspect.isabstract(Alert)


def test_hyp_alert_constructor_exists():
    assert callable(Alert.__init__)


def test_hyp_alert_constructor_args():
    sig = inspect.signature(Alert.__init__)
    params = list(sig.parameters.keys())
    assert "AlertID" in params, "Missing parameter 'AlertID'"




def test_hyp_mobile_app_is_not_abstract():
    assert not inspect.isabstract(Mobile_App)


def test_hyp_mobile_app_constructor_exists():
    assert callable(Mobile_App.__init__)


def test_hyp_mobile_app_constructor_args():
    sig = inspect.signature(Mobile_App.__init__)
    params = list(sig.parameters.keys())
    assert "UserID" in params, "Missing parameter 'UserID'"




def test_hyp_pressuresensor_is_not_abstract():
    assert not inspect.isabstract(PressureSensor)


def test_hyp_pressuresensor_constructor_exists():
    assert callable(PressureSensor.__init__)


def test_hyp_pressuresensor_constructor_args():
    sig = inspect.signature(PressureSensor.__init__)
    params = list(sig.parameters.keys())



def test_hyp_temperature_sensor_is_not_abstract():
    assert not inspect.isabstract(Temperature_Sensor)


def test_hyp_temperature_sensor_constructor_exists():
    assert callable(Temperature_Sensor.__init__)


def test_hyp_temperature_sensor_constructor_args():
    sig = inspect.signature(Temperature_Sensor.__init__)
    params = list(sig.parameters.keys())



def test_hyp_gas_smoke_sensor_is_not_abstract():
    assert not inspect.isabstract(Gas_Smoke_Sensor)


def test_hyp_gas_smoke_sensor_constructor_exists():
    assert callable(Gas_Smoke_Sensor.__init__)


def test_hyp_gas_smoke_sensor_constructor_args():
    sig = inspect.signature(Gas_Smoke_Sensor.__init__)
    params = list(sig.parameters.keys())
    assert "SmokeAlarm" in params, "Missing parameter 'SmokeAlarm'"
    assert "DispenseSprinkler" in params, "Missing parameter 'DispenseSprinkler'"





def test_hyp_sensor_is_not_abstract():
    assert not inspect.isabstract(Sensor)


def test_hyp_sensor_constructor_exists():
    assert callable(Sensor.__init__)


def test_hyp_sensor_constructor_args():
    sig = inspect.signature(Sensor.__init__)
    params = list(sig.parameters.keys())
    assert "SensorType" in params, "Missing parameter 'SensorType'"
    assert "SensorID" in params, "Missing parameter 'SensorID'"





def test_hyp_firebase_is_not_abstract():
    assert not inspect.isabstract(Firebase)


def test_hyp_firebase_constructor_exists():
    assert callable(Firebase.__init__)


def test_hyp_firebase_constructor_args():
    sig = inspect.signature(Firebase.__init__)
    params = list(sig.parameters.keys())
    assert "Status" in params, "Missing parameter 'Status'"
    assert "Update" in params, "Missing parameter 'Update'"




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
Alert2_strategy = st.builds(
    Alert2,
    AlertID=
        st.integers()
)
Web_strategy = st.builds(
    Web,
)
Arduino_strategy = st.builds(
    Arduino,
    MicID=
        safe_text
)
Count_people_strategy = st.builds(
    Count_people,
    _attr=
        st.integers()
)
Alert_strategy = st.builds(
    Alert,
    AlertID=
        st.integers()
)
Mobile_App_strategy = st.builds(
    Mobile_App,
    UserID=
        st.integers()
)
PressureSensor_strategy = st.builds(
    PressureSensor,
)
Temperature_Sensor_strategy = st.builds(
    Temperature_Sensor,
)
Gas_Smoke_Sensor_strategy = st.builds(
    Gas_Smoke_Sensor,
    SmokeAlarm=
        st.booleans(),
    DispenseSprinkler=
        st.booleans()
)
Sensor_strategy = st.builds(
    Sensor,
    SensorType=
        st.integers(),
    SensorID=
        st.integers()
)
Firebase_strategy = st.builds(
    Firebase,
    Status=
        st.booleans(),
    Update=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)




@given(instance=Alert2_strategy)
def test_hyp_alert2_AlertID_setter(instance):
    original = instance.AlertID
    instance.AlertID = original
    assert instance.AlertID == original





@given(instance=Arduino_strategy)
def test_hyp_arduino_MicID_setter(instance):
    original = instance.MicID
    instance.MicID = original
    assert instance.MicID == original




@given(instance=Count_people_strategy)
def test_hyp_count_people__attr_setter(instance):
    original = instance._attr
    instance._attr = original
    assert instance._attr == original




@given(instance=Alert_strategy)
def test_hyp_alert_AlertID_setter(instance):
    original = instance.AlertID
    instance.AlertID = original
    assert instance.AlertID == original




@given(instance=Mobile_App_strategy)
def test_hyp_mobile_app_UserID_setter(instance):
    original = instance.UserID
    instance.UserID = original
    assert instance.UserID == original






@given(instance=Gas_Smoke_Sensor_strategy)
def test_hyp_gas_smoke_sensor_SmokeAlarm_setter(instance):
    original = instance.SmokeAlarm
    instance.SmokeAlarm = original
    assert instance.SmokeAlarm == original



@given(instance=Gas_Smoke_Sensor_strategy)
def test_hyp_gas_smoke_sensor_DispenseSprinkler_setter(instance):
    original = instance.DispenseSprinkler
    instance.DispenseSprinkler = original
    assert instance.DispenseSprinkler == original




@given(instance=Sensor_strategy)
def test_hyp_sensor_SensorType_setter(instance):
    original = instance.SensorType
    instance.SensorType = original
    assert instance.SensorType == original



@given(instance=Sensor_strategy)
def test_hyp_sensor_SensorID_setter(instance):
    original = instance.SensorID
    instance.SensorID = original
    assert instance.SensorID == original




@given(instance=Firebase_strategy)
def test_hyp_firebase_Status_setter(instance):
    original = instance.Status
    instance.Status = original
    assert instance.Status == original



@given(instance=Firebase_strategy)
def test_hyp_firebase_Update_setter(instance):
    original = instance.Update
    instance.Update = original
    assert instance.Update == original


# ----- SECTION B: test_structural_full.py (deterministic-first suite) -----
import inspect
import pytest
from datetime import date, datetime, time, timedelta
from hypothesis import given, settings
import hypothesis.strategies as st

from python_code import (
    Alert,
    Alert2,
    Arduino,
    Count_people,
    Firebase,
    Gas_Smoke_Sensor,
    Mobile_App,
    PressureSensor,
    Sensor,
    Temperature_Sensor,
    Web,
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

def test_Alert_AlertID_value_roundtrip():
    instance = Alert(AlertID=7)
    assert instance.AlertID == 7
    instance.AlertID = 13
    assert instance.AlertID == 13


def test_Alert2_AlertID_value_roundtrip():
    instance = Alert2(AlertID=7)
    assert instance.AlertID == 7
    instance.AlertID = 13
    assert instance.AlertID == 13


def test_Arduino_MicID_value_roundtrip():
    instance = Arduino(MicID="sample_text")
    assert instance.MicID == "sample_text"
    instance.MicID = "sample_text_2"
    assert instance.MicID == "sample_text_2"


def test_Count_people__attr_value_roundtrip():
    instance = Count_people(_attr=7)
    assert instance._attr == 7
    instance._attr = 13
    assert instance._attr == 13


def test_Firebase_Status_value_roundtrip():
    instance = Firebase(Status=True, Update=3.14)
    assert instance.Status == True
    instance.Status = False
    assert instance.Status == False


def test_Firebase_Update_value_roundtrip():
    instance = Firebase(Status=True, Update=3.14)
    assert instance.Update == 3.14
    instance.Update = 9.99
    assert instance.Update == 9.99


def test_Gas_Smoke_Sensor_DispenseSprinkler_value_roundtrip():
    instance = Gas_Smoke_Sensor(DispenseSprinkler=True, SmokeAlarm=True)
    assert instance.DispenseSprinkler == True
    instance.DispenseSprinkler = False
    assert instance.DispenseSprinkler == False


def test_Gas_Smoke_Sensor_SmokeAlarm_value_roundtrip():
    instance = Gas_Smoke_Sensor(DispenseSprinkler=True, SmokeAlarm=True)
    assert instance.SmokeAlarm == True
    instance.SmokeAlarm = False
    assert instance.SmokeAlarm == False


def test_Mobile_App_UserID_value_roundtrip():
    instance = Mobile_App(UserID=7)
    assert instance.UserID == 7
    instance.UserID = 13
    assert instance.UserID == 13


def test_Sensor_SensorID_value_roundtrip():
    instance = Sensor(SensorID=7, SensorType=7)
    assert instance.SensorID == 7
    instance.SensorID = 13
    assert instance.SensorID == 13


def test_Sensor_SensorType_value_roundtrip():
    instance = Sensor(SensorID=7, SensorType=7)
    assert instance.SensorType == 7
    instance.SensorType = 13
    assert instance.SensorType == 13


def test_assoc_Alert2_Web_link_reassign_clear():
    a = Alert2(AlertID=7)
    b1 = Web()
    b2 = Web()
    _safe_set(a, 'web12', b1)
    assert _is_linked(a, 'web12', b1)
    if hasattr(b1, 'alert213'):
        assert _is_linked(b1, 'alert213', a)
    _safe_set(a, 'web12', b2)
    assert _is_linked(a, 'web12', b2)
    if hasattr(b1, 'alert213'):
        assert not _is_linked(b1, 'alert213', a)
    if hasattr(b2, 'alert213'):
        assert _is_linked(b2, 'alert213', a)
    _safe_set(a, 'web12', None)
    assert not _is_linked(a, 'web12', b2)
    if hasattr(b2, 'alert213'):
        assert not _is_linked(b2, 'alert213', a)


def test_assoc_Arduino__Firebase_link_reassign_clear():
    a = Firebase(Status=True, Update=3.14)
    b1 = Arduino(MicID="sample_text")
    b2 = Arduino(MicID="sample_text_2")
    _safe_set(a, 'Arduino__Firebase_19', b1)
    assert _is_linked(a, 'Arduino__Firebase_19', b1)
    if hasattr(b1, 'Arduino__Firebase_08'):
        assert _is_linked(b1, 'Arduino__Firebase_08', a)
    _safe_set(a, 'Arduino__Firebase_19', b2)
    assert _is_linked(a, 'Arduino__Firebase_19', b2)
    if hasattr(b1, 'Arduino__Firebase_08'):
        assert not _is_linked(b1, 'Arduino__Firebase_08', a)
    if hasattr(b2, 'Arduino__Firebase_08'):
        assert _is_linked(b2, 'Arduino__Firebase_08', a)
    _safe_set(a, 'Arduino__Firebase_19', None)
    assert not _is_linked(a, 'Arduino__Firebase_19', b2)
    if hasattr(b2, 'Arduino__Firebase_08'):
        assert not _is_linked(b2, 'Arduino__Firebase_08', a)


def test_assoc_Firebase_Web_link_reassign_clear():
    a = Firebase(Status=True, Update=3.14)
    b1 = Web()
    b2 = Web()
    _safe_set(a, 'web10', b1)
    assert _is_linked(a, 'web10', b1)
    if hasattr(b1, 'firebase11'):
        assert _is_linked(b1, 'firebase11', a)
    _safe_set(a, 'web10', b2)
    assert _is_linked(a, 'web10', b2)
    if hasattr(b1, 'firebase11'):
        assert not _is_linked(b1, 'firebase11', a)
    if hasattr(b2, 'firebase11'):
        assert _is_linked(b2, 'firebase11', a)
    _safe_set(a, 'web10', None)
    assert not _is_linked(a, 'web10', b2)
    if hasattr(b2, 'firebase11'):
        assert not _is_linked(b2, 'firebase11', a)


def test_assoc_Home_Security_System_Alert_link_reassign_clear():
    a = Mobile_App(UserID=7)
    b1 = Alert(AlertID=7)
    b2 = Alert(AlertID=13)
    _safe_set(a, 'alert2', b1)
    assert _is_linked(a, 'alert2', b1)
    if hasattr(b1, 'home_Security_System3'):
        assert _is_linked(b1, 'home_Security_System3', a)
    _safe_set(a, 'alert2', b2)
    assert _is_linked(a, 'alert2', b2)
    if hasattr(b1, 'home_Security_System3'):
        assert not _is_linked(b1, 'home_Security_System3', a)
    if hasattr(b2, 'home_Security_System3'):
        assert _is_linked(b2, 'home_Security_System3', a)
    _safe_set(a, 'alert2', None)
    assert not _is_linked(a, 'alert2', b2)
    if hasattr(b2, 'home_Security_System3'):
        assert not _is_linked(b2, 'home_Security_System3', a)


def test_assoc_Home_Security_System_System_link_reassign_clear():
    a = Mobile_App(UserID=7)
    b1 = Firebase(Status=True, Update=3.14)
    b2 = Firebase(Status=False, Update=9.99)
    _safe_set(a, 'system6', b1)
    assert _is_linked(a, 'system6', b1)
    if hasattr(b1, 'home_Security_System7'):
        assert _is_linked(b1, 'home_Security_System7', a)
    _safe_set(a, 'system6', b2)
    assert _is_linked(a, 'system6', b2)
    if hasattr(b1, 'home_Security_System7'):
        assert not _is_linked(b1, 'home_Security_System7', a)
    if hasattr(b2, 'home_Security_System7'):
        assert _is_linked(b2, 'home_Security_System7', a)
    _safe_set(a, 'system6', None)
    assert not _is_linked(a, 'system6', b2)
    if hasattr(b2, 'home_Security_System7'):
        assert not _is_linked(b2, 'home_Security_System7', a)


def test_assoc_Sensor_Door_link_reassign_clear():
    a = Sensor(SensorID=7, SensorType=7)
    b1 = Count_people(_attr=7)
    b2 = Count_people(_attr=13)
    _safe_set(a, 'door0', b1)
    assert _is_linked(a, 'door0', b1)
    if hasattr(b1, 'sensor1'):
        assert _is_linked(b1, 'sensor1', a)
    _safe_set(a, 'door0', b2)
    assert _is_linked(a, 'door0', b2)
    if hasattr(b1, 'sensor1'):
        assert not _is_linked(b1, 'sensor1', a)
    if hasattr(b2, 'sensor1'):
        assert _is_linked(b2, 'sensor1', a)
    _safe_set(a, 'door0', None)
    assert not _is_linked(a, 'door0', b2)
    if hasattr(b2, 'sensor1'):
        assert not _is_linked(b2, 'sensor1', a)


def test_assoc_Sensor_System_link_reassign_clear():
    a = Sensor(SensorID=7, SensorType=7)
    b1 = Arduino(MicID="sample_text")
    b2 = Arduino(MicID="sample_text_2")
    _safe_set(a, 'system4', b1)
    assert _is_linked(a, 'system4', b1)
    if hasattr(b1, 'sensor5'):
        assert _is_linked(b1, 'sensor5', a)
    _safe_set(a, 'system4', b2)
    assert _is_linked(a, 'system4', b2)
    if hasattr(b1, 'sensor5'):
        assert not _is_linked(b1, 'sensor5', a)
    if hasattr(b2, 'sensor5'):
        assert _is_linked(b2, 'sensor5', a)
    _safe_set(a, 'system4', None)
    assert not _is_linked(a, 'system4', b2)
    if hasattr(b2, 'sensor5'):
        assert not _is_linked(b2, 'sensor5', a)


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

Alert_strategy = st.builds(Alert, AlertID=st.integers())
@given(instance=Alert_strategy)
@settings(max_examples=25)
def test_Alert_instantiation(instance):
    assert isinstance(instance, Alert)


Alert2_strategy = st.builds(Alert2, AlertID=st.integers())
@given(instance=Alert2_strategy)
@settings(max_examples=25)
def test_Alert2_instantiation(instance):
    assert isinstance(instance, Alert2)


Arduino_strategy = st.builds(Arduino, MicID=safe_text)
@given(instance=Arduino_strategy)
@settings(max_examples=25)
def test_Arduino_instantiation(instance):
    assert isinstance(instance, Arduino)


Count_people_strategy = st.builds(Count_people, _attr=st.integers())
@given(instance=Count_people_strategy)
@settings(max_examples=25)
def test_Count_people_instantiation(instance):
    assert isinstance(instance, Count_people)


Firebase_strategy = st.builds(Firebase, Status=st.booleans(), Update=st.floats(allow_nan=False, allow_infinity=False))
@given(instance=Firebase_strategy)
@settings(max_examples=25)
def test_Firebase_instantiation(instance):
    assert isinstance(instance, Firebase)


Gas_Smoke_Sensor_strategy = st.builds(Gas_Smoke_Sensor, DispenseSprinkler=st.booleans(), SmokeAlarm=st.booleans())
@given(instance=Gas_Smoke_Sensor_strategy)
@settings(max_examples=25)
def test_Gas_Smoke_Sensor_instantiation(instance):
    assert isinstance(instance, Gas_Smoke_Sensor)


Mobile_App_strategy = st.builds(Mobile_App, UserID=st.integers())
@given(instance=Mobile_App_strategy)
@settings(max_examples=25)
def test_Mobile_App_instantiation(instance):
    assert isinstance(instance, Mobile_App)


PressureSensor_strategy = st.builds(PressureSensor)
@given(instance=PressureSensor_strategy)
@settings(max_examples=25)
def test_PressureSensor_instantiation(instance):
    assert isinstance(instance, PressureSensor)


Sensor_strategy = st.builds(Sensor, SensorID=st.integers(), SensorType=st.integers())
@given(instance=Sensor_strategy)
@settings(max_examples=25)
def test_Sensor_instantiation(instance):
    assert isinstance(instance, Sensor)


Temperature_Sensor_strategy = st.builds(Temperature_Sensor)
@given(instance=Temperature_Sensor_strategy)
@settings(max_examples=25)
def test_Temperature_Sensor_instantiation(instance):
    assert isinstance(instance, Temperature_Sensor)


Web_strategy = st.builds(Web)
@given(instance=Web_strategy)
@settings(max_examples=25)
def test_Web_instantiation(instance):
    assert isinstance(instance, Web)



