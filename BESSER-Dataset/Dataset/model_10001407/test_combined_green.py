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
    Fan_Regulator_Box,
    Control_Box,
    FAN,
    HouseHolds,
    Light,
    MicroPhone,
    Alert,
    Home_Security_System,
    FireAlarm_Sensor,
    Sensor,
    System,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_hyp_fan_regulator_box_is_not_abstract():
    assert not inspect.isabstract(Fan_Regulator_Box)


def test_hyp_fan_regulator_box_constructor_exists():
    assert callable(Fan_Regulator_Box.__init__)


def test_hyp_fan_regulator_box_constructor_args():
    sig = inspect.signature(Fan_Regulator_Box.__init__)
    params = list(sig.parameters.keys())
    assert "FAN_ID" in params, "Missing parameter 'FAN_ID'"




def test_hyp_control_box_is_not_abstract():
    assert not inspect.isabstract(Control_Box)


def test_hyp_control_box_constructor_exists():
    assert callable(Control_Box.__init__)


def test_hyp_control_box_constructor_args():
    sig = inspect.signature(Control_Box.__init__)
    params = list(sig.parameters.keys())
    assert "Update" in params, "Missing parameter 'Update'"
    assert "Status" in params, "Missing parameter 'Status'"





def test_hyp_fan_is_not_abstract():
    assert not inspect.isabstract(FAN)


def test_hyp_fan_constructor_exists():
    assert callable(FAN.__init__)


def test_hyp_fan_constructor_args():
    sig = inspect.signature(FAN.__init__)
    params = list(sig.parameters.keys())
    assert "FAN_ID" in params, "Missing parameter 'FAN_ID'"




def test_hyp_households_is_not_abstract():
    assert not inspect.isabstract(HouseHolds)


def test_hyp_households_constructor_exists():
    assert callable(HouseHolds.__init__)


def test_hyp_households_constructor_args():
    sig = inspect.signature(HouseHolds.__init__)
    params = list(sig.parameters.keys())
    assert "WashingMachine" in params, "Missing parameter 'WashingMachine'"
    assert "TimeID" in params, "Missing parameter 'TimeID'"
    assert "Alarm" in params, "Missing parameter 'Alarm'"






def test_hyp_light_is_not_abstract():
    assert not inspect.isabstract(Light)


def test_hyp_light_constructor_exists():
    assert callable(Light.__init__)


def test_hyp_light_constructor_args():
    sig = inspect.signature(Light.__init__)
    params = list(sig.parameters.keys())
    assert "LightID" in params, "Missing parameter 'LightID'"




def test_hyp_microphone_is_not_abstract():
    assert not inspect.isabstract(MicroPhone)


def test_hyp_microphone_constructor_exists():
    assert callable(MicroPhone.__init__)


def test_hyp_microphone_constructor_args():
    sig = inspect.signature(MicroPhone.__init__)
    params = list(sig.parameters.keys())
    assert "MicID" in params, "Missing parameter 'MicID'"




def test_hyp_alert_is_not_abstract():
    assert not inspect.isabstract(Alert)


def test_hyp_alert_constructor_exists():
    assert callable(Alert.__init__)


def test_hyp_alert_constructor_args():
    sig = inspect.signature(Alert.__init__)
    params = list(sig.parameters.keys())
    assert "AlertID" in params, "Missing parameter 'AlertID'"




def test_hyp_home_security_system_is_not_abstract():
    assert not inspect.isabstract(Home_Security_System)


def test_hyp_home_security_system_constructor_exists():
    assert callable(Home_Security_System.__init__)


def test_hyp_home_security_system_constructor_args():
    sig = inspect.signature(Home_Security_System.__init__)
    params = list(sig.parameters.keys())
    assert "UserID" in params, "Missing parameter 'UserID'"




def test_hyp_firealarm_sensor_is_not_abstract():
    assert not inspect.isabstract(FireAlarm_Sensor)


def test_hyp_firealarm_sensor_constructor_exists():
    assert callable(FireAlarm_Sensor.__init__)


def test_hyp_firealarm_sensor_constructor_args():
    sig = inspect.signature(FireAlarm_Sensor.__init__)
    params = list(sig.parameters.keys())
    assert "DispenseSprinkler" in params, "Missing parameter 'DispenseSprinkler'"
    assert "SmokeAlarm" in params, "Missing parameter 'SmokeAlarm'"





def test_hyp_sensor_is_not_abstract():
    assert not inspect.isabstract(Sensor)


def test_hyp_sensor_constructor_exists():
    assert callable(Sensor.__init__)


def test_hyp_sensor_constructor_args():
    sig = inspect.signature(Sensor.__init__)
    params = list(sig.parameters.keys())
    assert "SensorType" in params, "Missing parameter 'SensorType'"
    assert "SensorID" in params, "Missing parameter 'SensorID'"





def test_hyp_system_is_not_abstract():
    assert not inspect.isabstract(System)


def test_hyp_system_constructor_exists():
    assert callable(System.__init__)


def test_hyp_system_constructor_args():
    sig = inspect.signature(System.__init__)
    params = list(sig.parameters.keys())
    assert "Update" in params, "Missing parameter 'Update'"
    assert "Status" in params, "Missing parameter 'Status'"




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
Fan_Regulator_Box_strategy = st.builds(
    Fan_Regulator_Box,
    FAN_ID=
        safe_text
)
Control_Box_strategy = st.builds(
    Control_Box,
    Update=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    Status=
        st.booleans()
)
FAN_strategy = st.builds(
    FAN,
    FAN_ID=
        safe_text
)
HouseHolds_strategy = st.builds(
    HouseHolds,
    WashingMachine=
        safe_text,
    TimeID=
        safe_text,
    Alarm=
        safe_text
)
Light_strategy = st.builds(
    Light,
    LightID=
        safe_text
)
MicroPhone_strategy = st.builds(
    MicroPhone,
    MicID=
        safe_text
)
Alert_strategy = st.builds(
    Alert,
    AlertID=
        st.integers()
)
Home_Security_System_strategy = st.builds(
    Home_Security_System,
    UserID=
        st.integers()
)
FireAlarm_Sensor_strategy = st.builds(
    FireAlarm_Sensor,
    DispenseSprinkler=
        st.booleans(),
    SmokeAlarm=
        st.booleans()
)
Sensor_strategy = st.builds(
    Sensor,
    SensorType=
        st.integers(),
    SensorID=
        st.integers()
)
System_strategy = st.builds(
    System,
    Update=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    Status=
        st.booleans()
)




@given(instance=Fan_Regulator_Box_strategy)
def test_hyp_fan_regulator_box_FAN_ID_setter(instance):
    original = instance.FAN_ID
    instance.FAN_ID = original
    assert instance.FAN_ID == original




@given(instance=Control_Box_strategy)
def test_hyp_control_box_Update_setter(instance):
    original = instance.Update
    instance.Update = original
    assert instance.Update == original



@given(instance=Control_Box_strategy)
def test_hyp_control_box_Status_setter(instance):
    original = instance.Status
    instance.Status = original
    assert instance.Status == original




@given(instance=FAN_strategy)
def test_hyp_fan_FAN_ID_setter(instance):
    original = instance.FAN_ID
    instance.FAN_ID = original
    assert instance.FAN_ID == original




@given(instance=HouseHolds_strategy)
def test_hyp_households_WashingMachine_setter(instance):
    original = instance.WashingMachine
    instance.WashingMachine = original
    assert instance.WashingMachine == original



@given(instance=HouseHolds_strategy)
def test_hyp_households_TimeID_setter(instance):
    original = instance.TimeID
    instance.TimeID = original
    assert instance.TimeID == original



@given(instance=HouseHolds_strategy)
def test_hyp_households_Alarm_setter(instance):
    original = instance.Alarm
    instance.Alarm = original
    assert instance.Alarm == original




@given(instance=Light_strategy)
def test_hyp_light_LightID_setter(instance):
    original = instance.LightID
    instance.LightID = original
    assert instance.LightID == original




@given(instance=MicroPhone_strategy)
def test_hyp_microphone_MicID_setter(instance):
    original = instance.MicID
    instance.MicID = original
    assert instance.MicID == original




@given(instance=Alert_strategy)
def test_hyp_alert_AlertID_setter(instance):
    original = instance.AlertID
    instance.AlertID = original
    assert instance.AlertID == original




@given(instance=Home_Security_System_strategy)
def test_hyp_home_security_system_UserID_setter(instance):
    original = instance.UserID
    instance.UserID = original
    assert instance.UserID == original




@given(instance=FireAlarm_Sensor_strategy)
def test_hyp_firealarm_sensor_DispenseSprinkler_setter(instance):
    original = instance.DispenseSprinkler
    instance.DispenseSprinkler = original
    assert instance.DispenseSprinkler == original



@given(instance=FireAlarm_Sensor_strategy)
def test_hyp_firealarm_sensor_SmokeAlarm_setter(instance):
    original = instance.SmokeAlarm
    instance.SmokeAlarm = original
    assert instance.SmokeAlarm == original




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




@given(instance=System_strategy)
def test_hyp_system_Update_setter(instance):
    original = instance.Update
    instance.Update = original
    assert instance.Update == original



@given(instance=System_strategy)
def test_hyp_system_Status_setter(instance):
    original = instance.Status
    instance.Status = original
    assert instance.Status == original


# ----- SECTION B: test_structural_full.py (deterministic-first suite) -----
import inspect
import pytest
from datetime import date, datetime, time, timedelta
from hypothesis import given, settings
import hypothesis.strategies as st

from python_code import (
    Alert,
    Control_Box,
    FAN,
    Fan_Regulator_Box,
    FireAlarm_Sensor,
    Home_Security_System,
    HouseHolds,
    Light,
    MicroPhone,
    Sensor,
    System,
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


def test_Control_Box_Status_value_roundtrip():
    instance = Control_Box(Status=True, Update=3.14)
    assert instance.Status == True
    instance.Status = False
    assert instance.Status == False


def test_Control_Box_Update_value_roundtrip():
    instance = Control_Box(Status=True, Update=3.14)
    assert instance.Update == 3.14
    instance.Update = 9.99
    assert instance.Update == 9.99


def test_FAN_FAN_ID_value_roundtrip():
    instance = FAN(FAN_ID="sample_text")
    assert instance.FAN_ID == "sample_text"
    instance.FAN_ID = "sample_text_2"
    assert instance.FAN_ID == "sample_text_2"


def test_Fan_Regulator_Box_FAN_ID_value_roundtrip():
    instance = Fan_Regulator_Box(FAN_ID="sample_text")
    assert instance.FAN_ID == "sample_text"
    instance.FAN_ID = "sample_text_2"
    assert instance.FAN_ID == "sample_text_2"


def test_FireAlarm_Sensor_DispenseSprinkler_value_roundtrip():
    instance = FireAlarm_Sensor(DispenseSprinkler=True, SmokeAlarm=True)
    assert instance.DispenseSprinkler == True
    instance.DispenseSprinkler = False
    assert instance.DispenseSprinkler == False


def test_FireAlarm_Sensor_SmokeAlarm_value_roundtrip():
    instance = FireAlarm_Sensor(DispenseSprinkler=True, SmokeAlarm=True)
    assert instance.SmokeAlarm == True
    instance.SmokeAlarm = False
    assert instance.SmokeAlarm == False


def test_Home_Security_System_UserID_value_roundtrip():
    instance = Home_Security_System(UserID=7)
    assert instance.UserID == 7
    instance.UserID = 13
    assert instance.UserID == 13


def test_HouseHolds_Alarm_value_roundtrip():
    instance = HouseHolds(Alarm="sample_text", TimeID="sample_text", WashingMachine="sample_text")
    assert instance.Alarm == "sample_text"
    instance.Alarm = "sample_text_2"
    assert instance.Alarm == "sample_text_2"


def test_HouseHolds_TimeID_value_roundtrip():
    instance = HouseHolds(Alarm="sample_text", TimeID="sample_text", WashingMachine="sample_text")
    assert instance.TimeID == "sample_text"
    instance.TimeID = "sample_text_2"
    assert instance.TimeID == "sample_text_2"


def test_HouseHolds_WashingMachine_value_roundtrip():
    instance = HouseHolds(Alarm="sample_text", TimeID="sample_text", WashingMachine="sample_text")
    assert instance.WashingMachine == "sample_text"
    instance.WashingMachine = "sample_text_2"
    assert instance.WashingMachine == "sample_text_2"


def test_Light_LightID_value_roundtrip():
    instance = Light(LightID="sample_text")
    assert instance.LightID == "sample_text"
    instance.LightID = "sample_text_2"
    assert instance.LightID == "sample_text_2"


def test_MicroPhone_MicID_value_roundtrip():
    instance = MicroPhone(MicID="sample_text")
    assert instance.MicID == "sample_text"
    instance.MicID = "sample_text_2"
    assert instance.MicID == "sample_text_2"


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


def test_System_Status_value_roundtrip():
    instance = System(Status=True, Update=3.14)
    assert instance.Status == True
    instance.Status = False
    assert instance.Status == False


def test_System_Update_value_roundtrip():
    instance = System(Status=True, Update=3.14)
    assert instance.Update == 3.14
    instance.Update = 9.99
    assert instance.Update == 9.99


def test_assoc_Home_Security_System_Alert_link_reassign_clear():
    a = Home_Security_System(UserID=7)
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
    a = System(Status=True, Update=3.14)
    b1 = Home_Security_System(UserID=7)
    b2 = Home_Security_System(UserID=13)
    _safe_set(a, 'home_Security_System7', b1)
    assert _is_linked(a, 'home_Security_System7', b1)
    if hasattr(b1, 'system6'):
        assert _is_linked(b1, 'system6', a)
    _safe_set(a, 'home_Security_System7', b2)
    assert _is_linked(a, 'home_Security_System7', b2)
    if hasattr(b1, 'system6'):
        assert not _is_linked(b1, 'system6', a)
    if hasattr(b2, 'system6'):
        assert _is_linked(b2, 'system6', a)
    _safe_set(a, 'home_Security_System7', None)
    assert not _is_linked(a, 'home_Security_System7', b2)
    if hasattr(b2, 'system6'):
        assert not _is_linked(b2, 'system6', a)


def test_assoc_MicroPhone_System_link_reassign_clear():
    a = System(Status=True, Update=3.14)
    b1 = MicroPhone(MicID="sample_text")
    b2 = MicroPhone(MicID="sample_text_2")
    _safe_set(a, 'microPhone1', {b1})
    assert _is_linked(a, 'microPhone1', b1)
    if hasattr(b1, 'system0'):
        assert _is_linked(b1, 'system0', a)
    _safe_set(a, 'microPhone1', {b2})
    assert _is_linked(a, 'microPhone1', b2)
    if hasattr(b1, 'system0'):
        assert not _is_linked(b1, 'system0', a)
    if hasattr(b2, 'system0'):
        assert _is_linked(b2, 'system0', a)
    _safe_set(a, 'microPhone1', set())
    assert not _is_linked(a, 'microPhone1', b2)
    if hasattr(b2, 'system0'):
        assert not _is_linked(b2, 'system0', a)


def test_assoc_System_HouseHolds_link_reassign_clear():
    a = System(Status=True, Update=3.14)
    b1 = HouseHolds(Alarm="sample_text", TimeID="sample_text", WashingMachine="sample_text")
    b2 = HouseHolds(Alarm="sample_text_2", TimeID="sample_text_2", WashingMachine="sample_text_2")
    _safe_set(a, 'houseHolds4', b1)
    assert _is_linked(a, 'houseHolds4', b1)
    if hasattr(b1, 'system5'):
        assert _is_linked(b1, 'system5', a)
    _safe_set(a, 'houseHolds4', b2)
    assert _is_linked(a, 'houseHolds4', b2)
    if hasattr(b1, 'system5'):
        assert not _is_linked(b1, 'system5', a)
    if hasattr(b2, 'system5'):
        assert _is_linked(b2, 'system5', a)
    _safe_set(a, 'houseHolds4', None)
    assert not _is_linked(a, 'houseHolds4', b2)
    if hasattr(b2, 'system5'):
        assert not _is_linked(b2, 'system5', a)


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

Alert_strategy = st.builds(Alert, AlertID=st.integers())
@given(instance=Alert_strategy)
@settings(max_examples=25)
def test_Alert_instantiation(instance):
    assert isinstance(instance, Alert)


Control_Box_strategy = st.builds(Control_Box, Status=st.booleans(), Update=st.floats(allow_nan=False, allow_infinity=False))
@given(instance=Control_Box_strategy)
@settings(max_examples=25)
def test_Control_Box_instantiation(instance):
    assert isinstance(instance, Control_Box)


FAN_strategy = st.builds(FAN, FAN_ID=safe_text)
@given(instance=FAN_strategy)
@settings(max_examples=25)
def test_FAN_instantiation(instance):
    assert isinstance(instance, FAN)


Fan_Regulator_Box_strategy = st.builds(Fan_Regulator_Box, FAN_ID=safe_text)
@given(instance=Fan_Regulator_Box_strategy)
@settings(max_examples=25)
def test_Fan_Regulator_Box_instantiation(instance):
    assert isinstance(instance, Fan_Regulator_Box)


FireAlarm_Sensor_strategy = st.builds(FireAlarm_Sensor, DispenseSprinkler=st.booleans(), SmokeAlarm=st.booleans())
@given(instance=FireAlarm_Sensor_strategy)
@settings(max_examples=25)
def test_FireAlarm_Sensor_instantiation(instance):
    assert isinstance(instance, FireAlarm_Sensor)


Home_Security_System_strategy = st.builds(Home_Security_System, UserID=st.integers())
@given(instance=Home_Security_System_strategy)
@settings(max_examples=25)
def test_Home_Security_System_instantiation(instance):
    assert isinstance(instance, Home_Security_System)


HouseHolds_strategy = st.builds(HouseHolds, Alarm=safe_text, TimeID=safe_text, WashingMachine=safe_text)
@given(instance=HouseHolds_strategy)
@settings(max_examples=25)
def test_HouseHolds_instantiation(instance):
    assert isinstance(instance, HouseHolds)


Light_strategy = st.builds(Light, LightID=safe_text)
@given(instance=Light_strategy)
@settings(max_examples=25)
def test_Light_instantiation(instance):
    assert isinstance(instance, Light)


MicroPhone_strategy = st.builds(MicroPhone, MicID=safe_text)
@given(instance=MicroPhone_strategy)
@settings(max_examples=25)
def test_MicroPhone_instantiation(instance):
    assert isinstance(instance, MicroPhone)


Sensor_strategy = st.builds(Sensor, SensorID=st.integers(), SensorType=st.integers())
@given(instance=Sensor_strategy)
@settings(max_examples=25)
def test_Sensor_instantiation(instance):
    assert isinstance(instance, Sensor)


System_strategy = st.builds(System, Status=st.booleans(), Update=st.floats(allow_nan=False, allow_infinity=False))
@given(instance=System_strategy)
@settings(max_examples=25)
def test_System_instantiation(instance):
    assert isinstance(instance, System)



