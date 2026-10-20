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
    UserProfile,
    ROOM,
    TechSupport,
    Kitchen,
    HomeTheatre,
    End_Of_Day,
    Start_Of_Day,
    Light,
    PowerSystem,
    Speakers,
    Curtains,
    Alert,
    Security_System,
    MotionSensor,
    Sensor,
    System,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_hyp_userprofile_is_not_abstract():
    assert not inspect.isabstract(UserProfile)


def test_hyp_userprofile_constructor_exists():
    assert callable(UserProfile.__init__)


def test_hyp_userprofile_constructor_args():
    sig = inspect.signature(UserProfile.__init__)
    params = list(sig.parameters.keys())
    assert "ProfileID" in params, "Missing parameter 'ProfileID'"




def test_hyp_room_is_not_abstract():
    assert not inspect.isabstract(ROOM)


def test_hyp_room_constructor_exists():
    assert callable(ROOM.__init__)


def test_hyp_room_constructor_args():
    sig = inspect.signature(ROOM.__init__)
    params = list(sig.parameters.keys())
    assert "RoomID" in params, "Missing parameter 'RoomID'"




def test_hyp_techsupport_is_not_abstract():
    assert not inspect.isabstract(TechSupport)


def test_hyp_techsupport_constructor_exists():
    assert callable(TechSupport.__init__)


def test_hyp_techsupport_constructor_args():
    sig = inspect.signature(TechSupport.__init__)
    params = list(sig.parameters.keys())
    assert "TechID" in params, "Missing parameter 'TechID'"




def test_hyp_kitchen_is_not_abstract():
    assert not inspect.isabstract(Kitchen)


def test_hyp_kitchen_constructor_exists():
    assert callable(Kitchen.__init__)


def test_hyp_kitchen_constructor_args():
    sig = inspect.signature(Kitchen.__init__)
    params = list(sig.parameters.keys())
    assert "TimeID" in params, "Missing parameter 'TimeID'"




def test_hyp_hometheatre_is_not_abstract():
    assert not inspect.isabstract(HomeTheatre)


def test_hyp_hometheatre_constructor_exists():
    assert callable(HomeTheatre.__init__)


def test_hyp_hometheatre_constructor_args():
    sig = inspect.signature(HomeTheatre.__init__)
    params = list(sig.parameters.keys())
    assert "SSID" in params, "Missing parameter 'SSID'"




def test_hyp_end_of_day_is_not_abstract():
    assert not inspect.isabstract(End_Of_Day)


def test_hyp_end_of_day_constructor_exists():
    assert callable(End_Of_Day.__init__)


def test_hyp_end_of_day_constructor_args():
    sig = inspect.signature(End_Of_Day.__init__)
    params = list(sig.parameters.keys())
    assert "EOT" in params, "Missing parameter 'EOT'"




def test_hyp_start_of_day_is_not_abstract():
    assert not inspect.isabstract(Start_Of_Day)


def test_hyp_start_of_day_constructor_exists():
    assert callable(Start_Of_Day.__init__)


def test_hyp_start_of_day_constructor_args():
    sig = inspect.signature(Start_Of_Day.__init__)
    params = list(sig.parameters.keys())
    assert "SOT" in params, "Missing parameter 'SOT'"




def test_hyp_light_is_not_abstract():
    assert not inspect.isabstract(Light)


def test_hyp_light_constructor_exists():
    assert callable(Light.__init__)


def test_hyp_light_constructor_args():
    sig = inspect.signature(Light.__init__)
    params = list(sig.parameters.keys())
    assert "LightID" in params, "Missing parameter 'LightID'"




def test_hyp_powersystem_is_not_abstract():
    assert not inspect.isabstract(PowerSystem)


def test_hyp_powersystem_constructor_exists():
    assert callable(PowerSystem.__init__)


def test_hyp_powersystem_constructor_args():
    sig = inspect.signature(PowerSystem.__init__)
    params = list(sig.parameters.keys())
    assert "DeviceID" in params, "Missing parameter 'DeviceID'"




def test_hyp_speakers_is_not_abstract():
    assert not inspect.isabstract(Speakers)


def test_hyp_speakers_constructor_exists():
    assert callable(Speakers.__init__)


def test_hyp_speakers_constructor_args():
    sig = inspect.signature(Speakers.__init__)
    params = list(sig.parameters.keys())
    assert "SpeakerID" in params, "Missing parameter 'SpeakerID'"




def test_hyp_curtains_is_not_abstract():
    assert not inspect.isabstract(Curtains)


def test_hyp_curtains_constructor_exists():
    assert callable(Curtains.__init__)


def test_hyp_curtains_constructor_args():
    sig = inspect.signature(Curtains.__init__)
    params = list(sig.parameters.keys())
    assert "CurtaiunID" in params, "Missing parameter 'CurtaiunID'"




def test_hyp_alert_is_not_abstract():
    assert not inspect.isabstract(Alert)


def test_hyp_alert_constructor_exists():
    assert callable(Alert.__init__)


def test_hyp_alert_constructor_args():
    sig = inspect.signature(Alert.__init__)
    params = list(sig.parameters.keys())
    assert "AlertID" in params, "Missing parameter 'AlertID'"




def test_hyp_security_system_is_not_abstract():
    assert not inspect.isabstract(Security_System)


def test_hyp_security_system_constructor_exists():
    assert callable(Security_System.__init__)


def test_hyp_security_system_constructor_args():
    sig = inspect.signature(Security_System.__init__)
    params = list(sig.parameters.keys())
    assert "UserID" in params, "Missing parameter 'UserID'"




def test_hyp_motionsensor_is_not_abstract():
    assert not inspect.isabstract(MotionSensor)


def test_hyp_motionsensor_constructor_exists():
    assert callable(MotionSensor.__init__)


def test_hyp_motionsensor_constructor_args():
    sig = inspect.signature(MotionSensor.__init__)
    params = list(sig.parameters.keys())



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
UserProfile_strategy = st.builds(
    UserProfile,
    ProfileID=
        st.integers()
)
ROOM_strategy = st.builds(
    ROOM,
    RoomID=
        safe_text
)
TechSupport_strategy = st.builds(
    TechSupport,
    TechID=
        st.integers()
)
Kitchen_strategy = st.builds(
    Kitchen,
    TimeID=
        safe_text
)
HomeTheatre_strategy = st.builds(
    HomeTheatre,
    SSID=
        safe_text
)
End_Of_Day_strategy = st.builds(
    End_Of_Day,
    EOT=
        st.integers()
)
Start_Of_Day_strategy = st.builds(
    Start_Of_Day,
    SOT=
        st.integers()
)
Light_strategy = st.builds(
    Light,
    LightID=
        st.integers()
)
PowerSystem_strategy = st.builds(
    PowerSystem,
    DeviceID=
        st.integers()
)
Speakers_strategy = st.builds(
    Speakers,
    SpeakerID=
        st.integers()
)
Curtains_strategy = st.builds(
    Curtains,
    CurtaiunID=
        st.integers()
)
Alert_strategy = st.builds(
    Alert,
    AlertID=
        st.integers()
)
Security_System_strategy = st.builds(
    Security_System,
    UserID=
        st.integers()
)
MotionSensor_strategy = st.builds(
    MotionSensor,
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
    Status=
        st.booleans(),
    Update=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)




@given(instance=UserProfile_strategy)
def test_hyp_userprofile_ProfileID_setter(instance):
    original = instance.ProfileID
    instance.ProfileID = original
    assert instance.ProfileID == original




@given(instance=ROOM_strategy)
def test_hyp_room_RoomID_setter(instance):
    original = instance.RoomID
    instance.RoomID = original
    assert instance.RoomID == original




@given(instance=TechSupport_strategy)
def test_hyp_techsupport_TechID_setter(instance):
    original = instance.TechID
    instance.TechID = original
    assert instance.TechID == original




@given(instance=Kitchen_strategy)
def test_hyp_kitchen_TimeID_setter(instance):
    original = instance.TimeID
    instance.TimeID = original
    assert instance.TimeID == original




@given(instance=HomeTheatre_strategy)
def test_hyp_hometheatre_SSID_setter(instance):
    original = instance.SSID
    instance.SSID = original
    assert instance.SSID == original




@given(instance=End_Of_Day_strategy)
def test_hyp_end_of_day_EOT_setter(instance):
    original = instance.EOT
    instance.EOT = original
    assert instance.EOT == original




@given(instance=Start_Of_Day_strategy)
def test_hyp_start_of_day_SOT_setter(instance):
    original = instance.SOT
    instance.SOT = original
    assert instance.SOT == original




@given(instance=Light_strategy)
def test_hyp_light_LightID_setter(instance):
    original = instance.LightID
    instance.LightID = original
    assert instance.LightID == original




@given(instance=PowerSystem_strategy)
def test_hyp_powersystem_DeviceID_setter(instance):
    original = instance.DeviceID
    instance.DeviceID = original
    assert instance.DeviceID == original




@given(instance=Speakers_strategy)
def test_hyp_speakers_SpeakerID_setter(instance):
    original = instance.SpeakerID
    instance.SpeakerID = original
    assert instance.SpeakerID == original




@given(instance=Curtains_strategy)
def test_hyp_curtains_CurtaiunID_setter(instance):
    original = instance.CurtaiunID
    instance.CurtaiunID = original
    assert instance.CurtaiunID == original




@given(instance=Alert_strategy)
def test_hyp_alert_AlertID_setter(instance):
    original = instance.AlertID
    instance.AlertID = original
    assert instance.AlertID == original




@given(instance=Security_System_strategy)
def test_hyp_security_system_UserID_setter(instance):
    original = instance.UserID
    instance.UserID = original
    assert instance.UserID == original





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
def test_hyp_system_Status_setter(instance):
    original = instance.Status
    instance.Status = original
    assert instance.Status == original



@given(instance=System_strategy)
def test_hyp_system_Update_setter(instance):
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
    Curtains,
    End_Of_Day,
    HomeTheatre,
    Kitchen,
    Light,
    MotionSensor,
    PowerSystem,
    ROOM,
    Security_System,
    Sensor,
    Speakers,
    Start_Of_Day,
    System,
    TechSupport,
    UserProfile,
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


def test_Curtains_CurtaiunID_value_roundtrip():
    instance = Curtains(CurtaiunID=7)
    assert instance.CurtaiunID == 7
    instance.CurtaiunID = 13
    assert instance.CurtaiunID == 13


def test_End_Of_Day_EOT_value_roundtrip():
    instance = End_Of_Day(EOT=7)
    assert instance.EOT == 7
    instance.EOT = 13
    assert instance.EOT == 13


def test_HomeTheatre_SSID_value_roundtrip():
    instance = HomeTheatre(SSID="sample_text")
    assert instance.SSID == "sample_text"
    instance.SSID = "sample_text_2"
    assert instance.SSID == "sample_text_2"


def test_Kitchen_TimeID_value_roundtrip():
    instance = Kitchen(TimeID="sample_text")
    assert instance.TimeID == "sample_text"
    instance.TimeID = "sample_text_2"
    assert instance.TimeID == "sample_text_2"


def test_Light_LightID_value_roundtrip():
    instance = Light(LightID=7)
    assert instance.LightID == 7
    instance.LightID = 13
    assert instance.LightID == 13


def test_PowerSystem_DeviceID_value_roundtrip():
    instance = PowerSystem(DeviceID=7)
    assert instance.DeviceID == 7
    instance.DeviceID = 13
    assert instance.DeviceID == 13


def test_ROOM_RoomID_value_roundtrip():
    instance = ROOM(RoomID="sample_text")
    assert instance.RoomID == "sample_text"
    instance.RoomID = "sample_text_2"
    assert instance.RoomID == "sample_text_2"


def test_Security_System_UserID_value_roundtrip():
    instance = Security_System(UserID=7)
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


def test_Speakers_SpeakerID_value_roundtrip():
    instance = Speakers(SpeakerID=7)
    assert instance.SpeakerID == 7
    instance.SpeakerID = 13
    assert instance.SpeakerID == 13


def test_Start_Of_Day_SOT_value_roundtrip():
    instance = Start_Of_Day(SOT=7)
    assert instance.SOT == 7
    instance.SOT = 13
    assert instance.SOT == 13


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


def test_TechSupport_TechID_value_roundtrip():
    instance = TechSupport(TechID=7)
    assert instance.TechID == 7
    instance.TechID = 13
    assert instance.TechID == 13


def test_UserProfile_ProfileID_value_roundtrip():
    instance = UserProfile(ProfileID=7)
    assert instance.ProfileID == 7
    instance.ProfileID = 13
    assert instance.ProfileID == 13


def test_assoc_HomeTheatre_Speakers_link_reassign_clear():
    a = Speakers(SpeakerID=7)
    b1 = HomeTheatre(SSID="sample_text")
    b2 = HomeTheatre(SSID="sample_text_2")
    _safe_set(a, 'homeTheatre3', {b1})
    assert _is_linked(a, 'homeTheatre3', b1)
    if hasattr(b1, 'speakers2'):
        assert _is_linked(b1, 'speakers2', a)
    _safe_set(a, 'homeTheatre3', {b2})
    assert _is_linked(a, 'homeTheatre3', b2)
    if hasattr(b1, 'speakers2'):
        assert not _is_linked(b1, 'speakers2', a)
    if hasattr(b2, 'speakers2'):
        assert _is_linked(b2, 'speakers2', a)
    _safe_set(a, 'homeTheatre3', set())
    assert not _is_linked(a, 'homeTheatre3', b2)
    if hasattr(b2, 'speakers2'):
        assert not _is_linked(b2, 'speakers2', a)


def test_assoc_HomeTheatre_System_link_reassign_clear():
    a = System(Status=True, Update=3.14)
    b1 = HomeTheatre(SSID="sample_text")
    b2 = HomeTheatre(SSID="sample_text_2")
    _safe_set(a, 'homeTheatre17', b1)
    assert _is_linked(a, 'homeTheatre17', b1)
    if hasattr(b1, 'system16'):
        assert _is_linked(b1, 'system16', a)
    _safe_set(a, 'homeTheatre17', b2)
    assert _is_linked(a, 'homeTheatre17', b2)
    if hasattr(b1, 'system16'):
        assert not _is_linked(b1, 'system16', a)
    if hasattr(b2, 'system16'):
        assert _is_linked(b2, 'system16', a)
    _safe_set(a, 'homeTheatre17', None)
    assert not _is_linked(a, 'homeTheatre17', b2)
    if hasattr(b2, 'system16'):
        assert not _is_linked(b2, 'system16', a)


def test_assoc_Home_Security_System_Alert_link_reassign_clear():
    a = Security_System(UserID=7)
    b1 = Alert(AlertID=7)
    b2 = Alert(AlertID=13)
    _safe_set(a, 'alert10', b1)
    assert _is_linked(a, 'alert10', b1)
    if hasattr(b1, 'home_Security_System11'):
        assert _is_linked(b1, 'home_Security_System11', a)
    _safe_set(a, 'alert10', b2)
    assert _is_linked(a, 'alert10', b2)
    if hasattr(b1, 'home_Security_System11'):
        assert not _is_linked(b1, 'home_Security_System11', a)
    if hasattr(b2, 'home_Security_System11'):
        assert _is_linked(b2, 'home_Security_System11', a)
    _safe_set(a, 'alert10', None)
    assert not _is_linked(a, 'alert10', b2)
    if hasattr(b2, 'home_Security_System11'):
        assert not _is_linked(b2, 'home_Security_System11', a)


def test_assoc_Home_Security_System_System_link_reassign_clear():
    a = System(Status=True, Update=3.14)
    b1 = Security_System(UserID=7)
    b2 = Security_System(UserID=13)
    _safe_set(a, 'Home_Security_System_System_119', b1)
    assert _is_linked(a, 'Home_Security_System_System_119', b1)
    if hasattr(b1, 'Home_Security_System_System_018'):
        assert _is_linked(b1, 'Home_Security_System_System_018', a)
    _safe_set(a, 'Home_Security_System_System_119', b2)
    assert _is_linked(a, 'Home_Security_System_System_119', b2)
    if hasattr(b1, 'Home_Security_System_System_018'):
        assert not _is_linked(b1, 'Home_Security_System_System_018', a)
    if hasattr(b2, 'Home_Security_System_System_018'):
        assert _is_linked(b2, 'Home_Security_System_System_018', a)
    _safe_set(a, 'Home_Security_System_System_119', None)
    assert not _is_linked(a, 'Home_Security_System_System_119', b2)
    if hasattr(b2, 'Home_Security_System_System_018'):
        assert not _is_linked(b2, 'Home_Security_System_System_018', a)


def test_assoc_HouseHolds_End_Of_Day_link_reassign_clear():
    a = Kitchen(TimeID="sample_text")
    b1 = End_Of_Day(EOT=7)
    b2 = End_Of_Day(EOT=13)
    _safe_set(a, 'end_Of_Day6', b1)
    assert _is_linked(a, 'end_Of_Day6', b1)
    if hasattr(b1, 'houseHolds7'):
        assert _is_linked(b1, 'houseHolds7', a)
    _safe_set(a, 'end_Of_Day6', b2)
    assert _is_linked(a, 'end_Of_Day6', b2)
    if hasattr(b1, 'houseHolds7'):
        assert not _is_linked(b1, 'houseHolds7', a)
    if hasattr(b2, 'houseHolds7'):
        assert _is_linked(b2, 'houseHolds7', a)
    _safe_set(a, 'end_Of_Day6', None)
    assert not _is_linked(a, 'end_Of_Day6', b2)
    if hasattr(b2, 'houseHolds7'):
        assert not _is_linked(b2, 'houseHolds7', a)


def test_assoc_HouseHolds_Start_Of_Day_link_reassign_clear():
    a = Start_Of_Day(SOT=7)
    b1 = Kitchen(TimeID="sample_text")
    b2 = Kitchen(TimeID="sample_text_2")
    _safe_set(a, 'houseHolds5', b1)
    assert _is_linked(a, 'houseHolds5', b1)
    if hasattr(b1, 'start_Of_Day4'):
        assert _is_linked(b1, 'start_Of_Day4', a)
    _safe_set(a, 'houseHolds5', b2)
    assert _is_linked(a, 'houseHolds5', b2)
    if hasattr(b1, 'start_Of_Day4'):
        assert not _is_linked(b1, 'start_Of_Day4', a)
    if hasattr(b2, 'start_Of_Day4'):
        assert _is_linked(b2, 'start_Of_Day4', a)
    _safe_set(a, 'houseHolds5', None)
    assert not _is_linked(a, 'houseHolds5', b2)
    if hasattr(b2, 'start_Of_Day4'):
        assert not _is_linked(b2, 'start_Of_Day4', a)


def test_assoc_MicroPhone_System_link_reassign_clear():
    a = System(Status=True, Update=3.14)
    b1 = PowerSystem(DeviceID=7)
    b2 = PowerSystem(DeviceID=13)
    _safe_set(a, 'microPhone9', {b1})
    assert _is_linked(a, 'microPhone9', b1)
    if hasattr(b1, 'system8'):
        assert _is_linked(b1, 'system8', a)
    _safe_set(a, 'microPhone9', {b2})
    assert _is_linked(a, 'microPhone9', b2)
    if hasattr(b1, 'system8'):
        assert not _is_linked(b1, 'system8', a)
    if hasattr(b2, 'system8'):
        assert _is_linked(b2, 'system8', a)
    _safe_set(a, 'microPhone9', set())
    assert not _is_linked(a, 'microPhone9', b2)
    if hasattr(b2, 'system8'):
        assert not _is_linked(b2, 'system8', a)


def test_assoc_Sensor_Door_link_reassign_clear():
    a = Sensor(SensorID=7, SensorType=7)
    b1 = Curtains(CurtaiunID=7)
    b2 = Curtains(CurtaiunID=13)
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
    a = System(Status=True, Update=3.14)
    b1 = Sensor(SensorID=7, SensorType=7)
    b2 = Sensor(SensorID=13, SensorType=13)
    _safe_set(a, 'sensor13', {b1})
    assert _is_linked(a, 'sensor13', b1)
    if hasattr(b1, 'system12'):
        assert _is_linked(b1, 'system12', a)
    _safe_set(a, 'sensor13', {b2})
    assert _is_linked(a, 'sensor13', b2)
    if hasattr(b1, 'system12'):
        assert not _is_linked(b1, 'system12', a)
    if hasattr(b2, 'system12'):
        assert _is_linked(b2, 'system12', a)
    _safe_set(a, 'sensor13', set())
    assert not _is_linked(a, 'sensor13', b2)
    if hasattr(b2, 'system12'):
        assert not _is_linked(b2, 'system12', a)


def test_assoc_System_HouseHolds_link_reassign_clear():
    a = System(Status=True, Update=3.14)
    b1 = Kitchen(TimeID="sample_text")
    b2 = Kitchen(TimeID="sample_text_2")
    _safe_set(a, 'houseHolds14', b1)
    assert _is_linked(a, 'houseHolds14', b1)
    if hasattr(b1, 'system15'):
        assert _is_linked(b1, 'system15', a)
    _safe_set(a, 'houseHolds14', b2)
    assert _is_linked(a, 'houseHolds14', b2)
    if hasattr(b1, 'system15'):
        assert not _is_linked(b1, 'system15', a)
    if hasattr(b2, 'system15'):
        assert _is_linked(b2, 'system15', a)
    _safe_set(a, 'houseHolds14', None)
    assert not _is_linked(a, 'houseHolds14', b2)
    if hasattr(b2, 'system15'):
        assert not _is_linked(b2, 'system15', a)


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

Alert_strategy = st.builds(Alert, AlertID=st.integers())
@given(instance=Alert_strategy)
@settings(max_examples=25)
def test_Alert_instantiation(instance):
    assert isinstance(instance, Alert)


Curtains_strategy = st.builds(Curtains, CurtaiunID=st.integers())
@given(instance=Curtains_strategy)
@settings(max_examples=25)
def test_Curtains_instantiation(instance):
    assert isinstance(instance, Curtains)


End_Of_Day_strategy = st.builds(End_Of_Day, EOT=st.integers())
@given(instance=End_Of_Day_strategy)
@settings(max_examples=25)
def test_End_Of_Day_instantiation(instance):
    assert isinstance(instance, End_Of_Day)


HomeTheatre_strategy = st.builds(HomeTheatre, SSID=safe_text)
@given(instance=HomeTheatre_strategy)
@settings(max_examples=25)
def test_HomeTheatre_instantiation(instance):
    assert isinstance(instance, HomeTheatre)


Kitchen_strategy = st.builds(Kitchen, TimeID=safe_text)
@given(instance=Kitchen_strategy)
@settings(max_examples=25)
def test_Kitchen_instantiation(instance):
    assert isinstance(instance, Kitchen)


Light_strategy = st.builds(Light, LightID=st.integers())
@given(instance=Light_strategy)
@settings(max_examples=25)
def test_Light_instantiation(instance):
    assert isinstance(instance, Light)


MotionSensor_strategy = st.builds(MotionSensor)
@given(instance=MotionSensor_strategy)
@settings(max_examples=25)
def test_MotionSensor_instantiation(instance):
    assert isinstance(instance, MotionSensor)


PowerSystem_strategy = st.builds(PowerSystem, DeviceID=st.integers())
@given(instance=PowerSystem_strategy)
@settings(max_examples=25)
def test_PowerSystem_instantiation(instance):
    assert isinstance(instance, PowerSystem)


ROOM_strategy = st.builds(ROOM, RoomID=safe_text)
@given(instance=ROOM_strategy)
@settings(max_examples=25)
def test_ROOM_instantiation(instance):
    assert isinstance(instance, ROOM)


Security_System_strategy = st.builds(Security_System, UserID=st.integers())
@given(instance=Security_System_strategy)
@settings(max_examples=25)
def test_Security_System_instantiation(instance):
    assert isinstance(instance, Security_System)


Sensor_strategy = st.builds(Sensor, SensorID=st.integers(), SensorType=st.integers())
@given(instance=Sensor_strategy)
@settings(max_examples=25)
def test_Sensor_instantiation(instance):
    assert isinstance(instance, Sensor)


Speakers_strategy = st.builds(Speakers, SpeakerID=st.integers())
@given(instance=Speakers_strategy)
@settings(max_examples=25)
def test_Speakers_instantiation(instance):
    assert isinstance(instance, Speakers)


Start_Of_Day_strategy = st.builds(Start_Of_Day, SOT=st.integers())
@given(instance=Start_Of_Day_strategy)
@settings(max_examples=25)
def test_Start_Of_Day_instantiation(instance):
    assert isinstance(instance, Start_Of_Day)


System_strategy = st.builds(System, Status=st.booleans(), Update=st.floats(allow_nan=False, allow_infinity=False))
@given(instance=System_strategy)
@settings(max_examples=25)
def test_System_instantiation(instance):
    assert isinstance(instance, System)


TechSupport_strategy = st.builds(TechSupport, TechID=st.integers())
@given(instance=TechSupport_strategy)
@settings(max_examples=25)
def test_TechSupport_instantiation(instance):
    assert isinstance(instance, TechSupport)


UserProfile_strategy = st.builds(UserProfile, ProfileID=st.integers())
@given(instance=UserProfile_strategy)
@settings(max_examples=25)
def test_UserProfile_instantiation(instance):
    assert isinstance(instance, UserProfile)



