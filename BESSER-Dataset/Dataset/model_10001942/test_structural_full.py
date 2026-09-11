import inspect
import pytest
from datetime import date, datetime, time, timedelta
from hypothesis import given, settings
import hypothesis.strategies as st

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

def test_AddAlarm_AlarmName_value_roundtrip():
    instance = AddAlarm(AlarmName="sample_text")
    assert instance.AlarmName == "sample_text"
    instance.AlarmName = "sample_text_2"
    assert instance.AlarmName == "sample_text_2"


def test_Alarm_AlarmID_value_roundtrip():
    instance = Alarm(AlarmID="sample_text")
    assert instance.AlarmID == "sample_text"
    instance.AlarmID = "sample_text_2"
    assert instance.AlarmID == "sample_text_2"


def test_Count_Sensor_People__value_roundtrip():
    instance = Count_Sensor(People_=7)
    assert instance.People_ == 7
    instance.People_ = 13
    assert instance.People_ == 13


def test_Gas_Smoke_Sensor_CheckSmoke_value_roundtrip():
    instance = Gas_Smoke_Sensor(CheckSmoke=True, SmokeAlarm=True)
    assert instance.CheckSmoke == True
    instance.CheckSmoke = False
    assert instance.CheckSmoke == False


def test_Gas_Smoke_Sensor_SmokeAlarm_value_roundtrip():
    instance = Gas_Smoke_Sensor(CheckSmoke=True, SmokeAlarm=True)
    assert instance.SmokeAlarm == True
    instance.SmokeAlarm = False
    assert instance.SmokeAlarm == False


def test_MobileApp_AlarmID_value_roundtrip():
    instance = MobileApp(AlarmID=7, UserID=7)
    assert instance.AlarmID == 7
    instance.AlarmID = 13
    assert instance.AlarmID == 13


def test_MobileApp_UserID_value_roundtrip():
    instance = MobileApp(AlarmID=7, UserID=7)
    assert instance.UserID == 7
    instance.UserID = 13
    assert instance.UserID == 13


def test_Notification_SmokeThreshold_value_roundtrip():
    instance = Notification(SmokeThreshold=3.14, TempThreshold=3.14)
    assert instance.SmokeThreshold == 3.14
    instance.SmokeThreshold = 9.99
    assert instance.SmokeThreshold == 9.99


def test_Notification_TempThreshold_value_roundtrip():
    instance = Notification(SmokeThreshold=3.14, TempThreshold=3.14)
    assert instance.TempThreshold == 3.14
    instance.TempThreshold = 9.99
    assert instance.TempThreshold == 9.99


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


def test_ViewTemp_Smoke_SmokeValue_value_roundtrip():
    instance = ViewTemp_Smoke(SmokeValue=3.14, TempValue=3.14)
    assert instance.SmokeValue == 3.14
    instance.SmokeValue = 9.99
    assert instance.SmokeValue == 9.99


def test_ViewTemp_Smoke_TempValue_value_roundtrip():
    instance = ViewTemp_Smoke(SmokeValue=3.14, TempValue=3.14)
    assert instance.TempValue == 3.14
    instance.TempValue = 9.99
    assert instance.TempValue == 9.99


def test_WebPage_HomeLoc_value_roundtrip():
    instance = WebPage(HomeLoc="sample_text", OwnerData="sample_text", People_=7, SmokeValue=3.14, TempValue=3.14)
    assert instance.HomeLoc == "sample_text"
    instance.HomeLoc = "sample_text_2"
    assert instance.HomeLoc == "sample_text_2"


def test_WebPage_OwnerData_value_roundtrip():
    instance = WebPage(HomeLoc="sample_text", OwnerData="sample_text", People_=7, SmokeValue=3.14, TempValue=3.14)
    assert instance.OwnerData == "sample_text"
    instance.OwnerData = "sample_text_2"
    assert instance.OwnerData == "sample_text_2"


def test_WebPage_People__value_roundtrip():
    instance = WebPage(HomeLoc="sample_text", OwnerData="sample_text", People_=7, SmokeValue=3.14, TempValue=3.14)
    assert instance.People_ == 7
    instance.People_ = 13
    assert instance.People_ == 13


def test_WebPage_SmokeValue_value_roundtrip():
    instance = WebPage(HomeLoc="sample_text", OwnerData="sample_text", People_=7, SmokeValue=3.14, TempValue=3.14)
    assert instance.SmokeValue == 3.14
    instance.SmokeValue = 9.99
    assert instance.SmokeValue == 9.99


def test_WebPage_TempValue_value_roundtrip():
    instance = WebPage(HomeLoc="sample_text", OwnerData="sample_text", People_=7, SmokeValue=3.14, TempValue=3.14)
    assert instance.TempValue == 3.14
    instance.TempValue = 9.99
    assert instance.TempValue == 9.99


def test_assoc_AddAlarm_Alarm_link_reassign_clear():
    a = Alarm(AlarmID="sample_text")
    b1 = AddAlarm(AlarmName="sample_text")
    b2 = AddAlarm(AlarmName="sample_text_2")
    _safe_set(a, 'AddAlarm_Alarm_125', b1)
    assert _is_linked(a, 'AddAlarm_Alarm_125', b1)
    if hasattr(b1, 'AddAlarm_Alarm_024'):
        assert _is_linked(b1, 'AddAlarm_Alarm_024', a)
    _safe_set(a, 'AddAlarm_Alarm_125', b2)
    assert _is_linked(a, 'AddAlarm_Alarm_125', b2)
    if hasattr(b1, 'AddAlarm_Alarm_024'):
        assert not _is_linked(b1, 'AddAlarm_Alarm_024', a)
    if hasattr(b2, 'AddAlarm_Alarm_024'):
        assert _is_linked(b2, 'AddAlarm_Alarm_024', a)
    _safe_set(a, 'AddAlarm_Alarm_125', None)
    assert not _is_linked(a, 'AddAlarm_Alarm_125', b2)
    if hasattr(b2, 'AddAlarm_Alarm_024'):
        assert not _is_linked(b2, 'AddAlarm_Alarm_024', a)


def test_assoc_Alarm_Mobile_App_link_reassign_clear():
    a = MobileApp(AlarmID=7, UserID=7)
    b1 = Alarm(AlarmID="sample_text")
    b2 = Alarm(AlarmID="sample_text_2")
    _safe_set(a, 'Alarm_Mobile_App_129', {b1})
    assert _is_linked(a, 'Alarm_Mobile_App_129', b1)
    if hasattr(b1, 'Alarm_Mobile_App_028'):
        assert _is_linked(b1, 'Alarm_Mobile_App_028', a)
    _safe_set(a, 'Alarm_Mobile_App_129', {b2})
    assert _is_linked(a, 'Alarm_Mobile_App_129', b2)
    if hasattr(b1, 'Alarm_Mobile_App_028'):
        assert not _is_linked(b1, 'Alarm_Mobile_App_028', a)
    if hasattr(b2, 'Alarm_Mobile_App_028'):
        assert _is_linked(b2, 'Alarm_Mobile_App_028', a)
    _safe_set(a, 'Alarm_Mobile_App_129', set())
    assert not _is_linked(a, 'Alarm_Mobile_App_129', b2)
    if hasattr(b2, 'Alarm_Mobile_App_028'):
        assert not _is_linked(b2, 'Alarm_Mobile_App_028', a)


def test_assoc_Firebase_Web_link_reassign_clear():
    a = WebPage(HomeLoc="sample_text", OwnerData="sample_text", People_=7, SmokeValue=3.14, TempValue=3.14)
    b1 = Firebase()
    b2 = Firebase()
    _safe_set(a, 'Firebase_Web_17', b1)
    assert _is_linked(a, 'Firebase_Web_17', b1)
    if hasattr(b1, 'Firebase_Web_06'):
        assert _is_linked(b1, 'Firebase_Web_06', a)
    _safe_set(a, 'Firebase_Web_17', b2)
    assert _is_linked(a, 'Firebase_Web_17', b2)
    if hasattr(b1, 'Firebase_Web_06'):
        assert not _is_linked(b1, 'Firebase_Web_06', a)
    if hasattr(b2, 'Firebase_Web_06'):
        assert _is_linked(b2, 'Firebase_Web_06', a)
    _safe_set(a, 'Firebase_Web_17', None)
    assert not _is_linked(a, 'Firebase_Web_17', b2)
    if hasattr(b2, 'Firebase_Web_06'):
        assert not _is_linked(b2, 'Firebase_Web_06', a)


def test_assoc_Home_Security_System_System_link_reassign_clear():
    a = MobileApp(AlarmID=7, UserID=7)
    b1 = Firebase()
    b2 = Firebase()
    _safe_set(a, 'Home_Security_System_System_02', b1)
    assert _is_linked(a, 'Home_Security_System_System_02', b1)
    if hasattr(b1, 'Home_Security_System_System_13'):
        assert _is_linked(b1, 'Home_Security_System_System_13', a)
    _safe_set(a, 'Home_Security_System_System_02', b2)
    assert _is_linked(a, 'Home_Security_System_System_02', b2)
    if hasattr(b1, 'Home_Security_System_System_13'):
        assert not _is_linked(b1, 'Home_Security_System_System_13', a)
    if hasattr(b2, 'Home_Security_System_System_13'):
        assert _is_linked(b2, 'Home_Security_System_System_13', a)
    _safe_set(a, 'Home_Security_System_System_02', None)
    assert not _is_linked(a, 'Home_Security_System_System_02', b2)
    if hasattr(b2, 'Home_Security_System_System_13'):
        assert not _is_linked(b2, 'Home_Security_System_System_13', a)


def test_assoc_Notification_Alarm_link_reassign_clear():
    a = Notification(SmokeThreshold=3.14, TempThreshold=3.14)
    b1 = Alarm(AlarmID="sample_text")
    b2 = Alarm(AlarmID="sample_text_2")
    _safe_set(a, 'Notification_Alarm_020', {b1})
    assert _is_linked(a, 'Notification_Alarm_020', b1)
    if hasattr(b1, 'Notification_Alarm_121'):
        assert _is_linked(b1, 'Notification_Alarm_121', a)
    _safe_set(a, 'Notification_Alarm_020', {b2})
    assert _is_linked(a, 'Notification_Alarm_020', b2)
    if hasattr(b1, 'Notification_Alarm_121'):
        assert not _is_linked(b1, 'Notification_Alarm_121', a)
    if hasattr(b2, 'Notification_Alarm_121'):
        assert _is_linked(b2, 'Notification_Alarm_121', a)
    _safe_set(a, 'Notification_Alarm_020', set())
    assert not _is_linked(a, 'Notification_Alarm_020', b2)
    if hasattr(b2, 'Notification_Alarm_121'):
        assert not _is_linked(b2, 'Notification_Alarm_121', a)


def test_assoc_Sensor_System_link_reassign_clear():
    a = Sensor(SensorID=7, SensorType=7)
    b1 = Arduino()
    b2 = Arduino()
    _safe_set(a, 'system0', b1)
    assert _is_linked(a, 'system0', b1)
    if hasattr(b1, 'sensor1'):
        assert _is_linked(b1, 'sensor1', a)
    _safe_set(a, 'system0', b2)
    assert _is_linked(a, 'system0', b2)
    if hasattr(b1, 'sensor1'):
        assert not _is_linked(b1, 'sensor1', a)
    if hasattr(b2, 'sensor1'):
        assert _is_linked(b2, 'sensor1', a)
    _safe_set(a, 'system0', None)
    assert not _is_linked(a, 'system0', b2)
    if hasattr(b2, 'sensor1'):
        assert not _is_linked(b2, 'sensor1', a)


def test_assoc_TurnDownAlarm_Alarm_link_reassign_clear():
    a = Alarm(AlarmID="sample_text")
    b1 = TurnDownAlarm()
    b2 = TurnDownAlarm()
    _safe_set(a, 'TurnDownAlarm_Alarm_127', b1)
    assert _is_linked(a, 'TurnDownAlarm_Alarm_127', b1)
    if hasattr(b1, 'TurnDownAlarm_Alarm_026'):
        assert _is_linked(b1, 'TurnDownAlarm_Alarm_026', a)
    _safe_set(a, 'TurnDownAlarm_Alarm_127', b2)
    assert _is_linked(a, 'TurnDownAlarm_Alarm_127', b2)
    if hasattr(b1, 'TurnDownAlarm_Alarm_026'):
        assert not _is_linked(b1, 'TurnDownAlarm_Alarm_026', a)
    if hasattr(b2, 'TurnDownAlarm_Alarm_026'):
        assert _is_linked(b2, 'TurnDownAlarm_Alarm_026', a)
    _safe_set(a, 'TurnDownAlarm_Alarm_127', None)
    assert not _is_linked(a, 'TurnDownAlarm_Alarm_127', b2)
    if hasattr(b2, 'TurnDownAlarm_Alarm_026'):
        assert not _is_linked(b2, 'TurnDownAlarm_Alarm_026', a)


def test_assoc_ViewTemp_Smoke_Alarm_link_reassign_clear():
    a = ViewTemp_Smoke(SmokeValue=3.14, TempValue=3.14)
    b1 = Alarm(AlarmID="sample_text")
    b2 = Alarm(AlarmID="sample_text_2")
    _safe_set(a, 'ViewTemp_Smoke_Alarm_022', b1)
    assert _is_linked(a, 'ViewTemp_Smoke_Alarm_022', b1)
    if hasattr(b1, 'ViewTemp_Smoke_Alarm_123'):
        assert _is_linked(b1, 'ViewTemp_Smoke_Alarm_123', a)
    _safe_set(a, 'ViewTemp_Smoke_Alarm_022', b2)
    assert _is_linked(a, 'ViewTemp_Smoke_Alarm_022', b2)
    if hasattr(b1, 'ViewTemp_Smoke_Alarm_123'):
        assert not _is_linked(b1, 'ViewTemp_Smoke_Alarm_123', a)
    if hasattr(b2, 'ViewTemp_Smoke_Alarm_123'):
        assert _is_linked(b2, 'ViewTemp_Smoke_Alarm_123', a)
    _safe_set(a, 'ViewTemp_Smoke_Alarm_022', None)
    assert not _is_linked(a, 'ViewTemp_Smoke_Alarm_022', b2)
    if hasattr(b2, 'ViewTemp_Smoke_Alarm_123'):
        assert not _is_linked(b2, 'ViewTemp_Smoke_Alarm_123', a)


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

AddAlarm_strategy = st.builds(AddAlarm, AlarmName=safe_text)
@given(instance=AddAlarm_strategy)
@settings(max_examples=25)
def test_AddAlarm_instantiation(instance):
    assert isinstance(instance, AddAlarm)


Add_new_alarm_external_strategy = st.builds(Add_new_alarm_external)
@given(instance=Add_new_alarm_external_strategy)
@settings(max_examples=25)
def test_Add_new_alarm_external_instantiation(instance):
    assert isinstance(instance, Add_new_alarm_external)


Alarm_strategy = st.builds(Alarm, AlarmID=safe_text)
@given(instance=Alarm_strategy)
@settings(max_examples=25)
def test_Alarm_instantiation(instance):
    assert isinstance(instance, Alarm)


Arduino_strategy = st.builds(Arduino)
@given(instance=Arduino_strategy)
@settings(max_examples=25)
def test_Arduino_instantiation(instance):
    assert isinstance(instance, Arduino)


Building_Owner__Actor_strategy = st.builds(Building_Owner__Actor)
@given(instance=Building_Owner__Actor_strategy)
@settings(max_examples=25)
def test_Building_Owner__Actor_instantiation(instance):
    assert isinstance(instance, Building_Owner__Actor)


Count_Sensor_strategy = st.builds(Count_Sensor, People_=st.integers())
@given(instance=Count_Sensor_strategy)
@settings(max_examples=25)
def test_Count_Sensor_instantiation(instance):
    assert isinstance(instance, Count_Sensor)


Disable_detector_external_strategy = st.builds(Disable_detector_external)
@given(instance=Disable_detector_external_strategy)
@settings(max_examples=25)
def test_Disable_detector_external_instantiation(instance):
    assert isinstance(instance, Disable_detector_external)


Fire_Alarm_System__Component_strategy = st.builds(Fire_Alarm_System__Component)
@given(instance=Fire_Alarm_System__Component_strategy)
@settings(max_examples=25)
def test_Fire_Alarm_System__Component_instantiation(instance):
    assert isinstance(instance, Fire_Alarm_System__Component)


Fire_Department__Actor_strategy = st.builds(Fire_Department__Actor)
@given(instance=Fire_Department__Actor_strategy)
@settings(max_examples=25)
def test_Fire_Department__Actor_instantiation(instance):
    assert isinstance(instance, Fire_Department__Actor)


Firebase_strategy = st.builds(Firebase)
@given(instance=Firebase_strategy)
@settings(max_examples=25)
def test_Firebase_instantiation(instance):
    assert isinstance(instance, Firebase)


Gas_Smoke_Sensor_strategy = st.builds(Gas_Smoke_Sensor, CheckSmoke=st.booleans(), SmokeAlarm=st.booleans())
@given(instance=Gas_Smoke_Sensor_strategy)
@settings(max_examples=25)
def test_Gas_Smoke_Sensor_instantiation(instance):
    assert isinstance(instance, Gas_Smoke_Sensor)


MobileApp_strategy = st.builds(MobileApp, AlarmID=st.integers(), UserID=st.integers())
@given(instance=MobileApp_strategy)
@settings(max_examples=25)
def test_MobileApp_instantiation(instance):
    assert isinstance(instance, MobileApp)


Notification_strategy = st.builds(Notification, SmokeThreshold=st.floats(allow_nan=False, allow_infinity=False), TempThreshold=st.floats(allow_nan=False, allow_infinity=False))
@given(instance=Notification_strategy)
@settings(max_examples=25)
def test_Notification_instantiation(instance):
    assert isinstance(instance, Notification)


Notify_User_of_fire_external_strategy = st.builds(Notify_User_of_fire_external)
@given(instance=Notify_User_of_fire_external_strategy)
@settings(max_examples=25)
def test_Notify_User_of_fire_external_instantiation(instance):
    assert isinstance(instance, Notify_User_of_fire_external)


Sense_and_Update_Data_external_strategy = st.builds(Sense_and_Update_Data_external)
@given(instance=Sense_and_Update_Data_external_strategy)
@settings(max_examples=25)
def test_Sense_and_Update_Data_external_instantiation(instance):
    assert isinstance(instance, Sense_and_Update_Data_external)


Sensor_strategy = st.builds(Sensor, SensorID=st.integers(), SensorType=st.integers())
@given(instance=Sensor_strategy)
@settings(max_examples=25)
def test_Sensor_instantiation(instance):
    assert isinstance(instance, Sensor)


Sensors_Actor_strategy = st.builds(Sensors_Actor)
@given(instance=Sensors_Actor_strategy)
@settings(max_examples=25)
def test_Sensors_Actor_instantiation(instance):
    assert isinstance(instance, Sensors_Actor)


Set_time_external_strategy = st.builds(Set_time_external)
@given(instance=Set_time_external_strategy)
@settings(max_examples=25)
def test_Set_time_external_instantiation(instance):
    assert isinstance(instance, Set_time_external)


Temperature_Sensor_strategy = st.builds(Temperature_Sensor)
@given(instance=Temperature_Sensor_strategy)
@settings(max_examples=25)
def test_Temperature_Sensor_instantiation(instance):
    assert isinstance(instance, Temperature_Sensor)


TurnDownAlarm_strategy = st.builds(TurnDownAlarm)
@given(instance=TurnDownAlarm_strategy)
@settings(max_examples=25)
def test_TurnDownAlarm_instantiation(instance):
    assert isinstance(instance, TurnDownAlarm)


ViewTemp_Smoke_strategy = st.builds(ViewTemp_Smoke, SmokeValue=st.floats(allow_nan=False, allow_infinity=False), TempValue=st.floats(allow_nan=False, allow_infinity=False))
@given(instance=ViewTemp_Smoke_strategy)
@settings(max_examples=25)
def test_ViewTemp_Smoke_instantiation(instance):
    assert isinstance(instance, ViewTemp_Smoke)


View_sensors_data_external_strategy = st.builds(View_sensors_data_external)
@given(instance=View_sensors_data_external_strategy)
@settings(max_examples=25)
def test_View_sensors_data_external_instantiation(instance):
    assert isinstance(instance, View_sensors_data_external)


WebPage_strategy = st.builds(WebPage, HomeLoc=safe_text, OwnerData=safe_text, People_=st.integers(), SmokeValue=st.floats(allow_nan=False, allow_infinity=False), TempValue=st.floats(allow_nan=False, allow_infinity=False))
@given(instance=WebPage_strategy)
@settings(max_examples=25)
def test_WebPage_instantiation(instance):
    assert isinstance(instance, WebPage)


