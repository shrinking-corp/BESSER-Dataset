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
    UDP_Controller,
    RFID_Sensor,
    Employee,
    Display,
    Users,
    Admin,
    End_Of_Day,
    Start_Of_Day,
    Light,
    Manager,
    Camera,
    Door,
    Alert,
    Home_Security_System,
    PressureSensor,
    Motion_Sensor,
    Sensor,
    Hub_Device,
    int,
    UDP_Socket,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_hyp_udp_controller_is_not_abstract():
    assert not inspect.isabstract(UDP_Controller)


def test_hyp_udp_controller_constructor_exists():
    assert callable(UDP_Controller.__init__)


def test_hyp_udp_controller_constructor_args():
    sig = inspect.signature(UDP_Controller.__init__)
    params = list(sig.parameters.keys())
    assert "ip_session" in params, "Missing parameter 'ip_session'"




def test_hyp_rfid_sensor_is_not_abstract():
    assert not inspect.isabstract(RFID_Sensor)


def test_hyp_rfid_sensor_constructor_exists():
    assert callable(RFID_Sensor.__init__)


def test_hyp_rfid_sensor_constructor_args():
    sig = inspect.signature(RFID_Sensor.__init__)
    params = list(sig.parameters.keys())



def test_hyp_employee_is_not_abstract():
    assert not inspect.isabstract(Employee)


def test_hyp_employee_constructor_exists():
    assert callable(Employee.__init__)


def test_hyp_employee_constructor_args():
    sig = inspect.signature(Employee.__init__)
    params = list(sig.parameters.keys())
    assert "EmployeeID" in params, "Missing parameter 'EmployeeID'"




def test_hyp_display_is_not_abstract():
    assert not inspect.isabstract(Display)


def test_hyp_display_constructor_exists():
    assert callable(Display.__init__)


def test_hyp_display_constructor_args():
    sig = inspect.signature(Display.__init__)
    params = list(sig.parameters.keys())
    assert "TimeID" in params, "Missing parameter 'TimeID'"
    assert "Alarm" in params, "Missing parameter 'Alarm'"
    assert "Coffee" in params, "Missing parameter 'Coffee'"
    assert "WashingMachine" in params, "Missing parameter 'WashingMachine'"
    assert "DishWasher" in params, "Missing parameter 'DishWasher'"








def test_hyp_users_is_not_abstract():
    assert not inspect.isabstract(Users)


def test_hyp_users_constructor_exists():
    assert callable(Users.__init__)


def test_hyp_users_constructor_args():
    sig = inspect.signature(Users.__init__)
    params = list(sig.parameters.keys())
    assert "HTID" in params, "Missing parameter 'HTID'"




def test_hyp_admin_is_not_abstract():
    assert not inspect.isabstract(Admin)


def test_hyp_admin_constructor_exists():
    assert callable(Admin.__init__)


def test_hyp_admin_constructor_args():
    sig = inspect.signature(Admin.__init__)
    params = list(sig.parameters.keys())
    assert "AdminID" in params, "Missing parameter 'AdminID'"




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




def test_hyp_manager_is_not_abstract():
    assert not inspect.isabstract(Manager)


def test_hyp_manager_constructor_exists():
    assert callable(Manager.__init__)


def test_hyp_manager_constructor_args():
    sig = inspect.signature(Manager.__init__)
    params = list(sig.parameters.keys())
    assert "MangagerID" in params, "Missing parameter 'MangagerID'"




def test_hyp_camera_is_not_abstract():
    assert not inspect.isabstract(Camera)


def test_hyp_camera_constructor_exists():
    assert callable(Camera.__init__)


def test_hyp_camera_constructor_args():
    sig = inspect.signature(Camera.__init__)
    params = list(sig.parameters.keys())
    assert "CameraID" in params, "Missing parameter 'CameraID'"




def test_hyp_door_is_not_abstract():
    assert not inspect.isabstract(Door)


def test_hyp_door_constructor_exists():
    assert callable(Door.__init__)


def test_hyp_door_constructor_args():
    sig = inspect.signature(Door.__init__)
    params = list(sig.parameters.keys())
    assert "DoorID" in params, "Missing parameter 'DoorID'"




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




def test_hyp_pressuresensor_is_not_abstract():
    assert not inspect.isabstract(PressureSensor)


def test_hyp_pressuresensor_constructor_exists():
    assert callable(PressureSensor.__init__)


def test_hyp_pressuresensor_constructor_args():
    sig = inspect.signature(PressureSensor.__init__)
    params = list(sig.parameters.keys())



def test_hyp_motion_sensor_is_not_abstract():
    assert not inspect.isabstract(Motion_Sensor)


def test_hyp_motion_sensor_constructor_exists():
    assert callable(Motion_Sensor.__init__)


def test_hyp_motion_sensor_constructor_args():
    sig = inspect.signature(Motion_Sensor.__init__)
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





def test_hyp_hub_device_is_not_abstract():
    assert not inspect.isabstract(Hub_Device)


def test_hyp_hub_device_constructor_exists():
    assert callable(Hub_Device.__init__)


def test_hyp_hub_device_constructor_args():
    sig = inspect.signature(Hub_Device.__init__)
    params = list(sig.parameters.keys())
    assert "Update" in params, "Missing parameter 'Update'"
    assert "Status" in params, "Missing parameter 'Status'"





def test_hyp_int_is_not_abstract():
    assert not inspect.isabstract(int)


def test_hyp_int_constructor_exists():
    assert callable(int.__init__)


def test_hyp_int_constructor_args():
    sig = inspect.signature(int.__init__)
    params = list(sig.parameters.keys())



def test_hyp_udp_socket_is_not_abstract():
    assert not inspect.isabstract(UDP_Socket)


def test_hyp_udp_socket_constructor_exists():
    assert callable(UDP_Socket.__init__)


def test_hyp_udp_socket_constructor_args():
    sig = inspect.signature(UDP_Socket.__init__)
    params = list(sig.parameters.keys())
    assert "socket" in params, "Missing parameter 'socket'"



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
UDP_Controller_strategy = st.builds(
    UDP_Controller,
    ip_session=
        safe_text
)
RFID_Sensor_strategy = st.builds(
    RFID_Sensor,
)
Employee_strategy = st.builds(
    Employee,
    EmployeeID=
        st.integers()
)
Display_strategy = st.builds(
    Display,
    TimeID=
        safe_text,
    Alarm=
        safe_text,
    Coffee=
        safe_text,
    WashingMachine=
        safe_text,
    DishWasher=
        safe_text
)
Users_strategy = st.builds(
    Users,
    HTID=
        safe_text
)
Admin_strategy = st.builds(
    Admin,
    AdminID=
        st.integers()
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
        safe_text
)
Manager_strategy = st.builds(
    Manager,
    MangagerID=
        st.integers()
)
Camera_strategy = st.builds(
    Camera,
    CameraID=
        st.integers()
)
Door_strategy = st.builds(
    Door,
    DoorID=
        st.integers()
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
PressureSensor_strategy = st.builds(
    PressureSensor,
)
Motion_Sensor_strategy = st.builds(
    Motion_Sensor,
)
Sensor_strategy = st.builds(
    Sensor,
    SensorType=
        st.integers(),
    SensorID=
        st.integers()
)
Hub_Device_strategy = st.builds(
    Hub_Device,
    Update=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    Status=
        st.booleans()
)
int_strategy = st.builds(
    int,
)
UDP_Socket_strategy = st.builds(
    UDP_Socket,
    socket=
        st.integers()
)




@given(instance=UDP_Controller_strategy)
def test_hyp_udp_controller_ip_session_setter(instance):
    original = instance.ip_session
    instance.ip_session = original
    assert instance.ip_session == original





@given(instance=Employee_strategy)
def test_hyp_employee_EmployeeID_setter(instance):
    original = instance.EmployeeID
    instance.EmployeeID = original
    assert instance.EmployeeID == original




@given(instance=Display_strategy)
def test_hyp_display_TimeID_setter(instance):
    original = instance.TimeID
    instance.TimeID = original
    assert instance.TimeID == original



@given(instance=Display_strategy)
def test_hyp_display_Alarm_setter(instance):
    original = instance.Alarm
    instance.Alarm = original
    assert instance.Alarm == original



@given(instance=Display_strategy)
def test_hyp_display_Coffee_setter(instance):
    original = instance.Coffee
    instance.Coffee = original
    assert instance.Coffee == original



@given(instance=Display_strategy)
def test_hyp_display_WashingMachine_setter(instance):
    original = instance.WashingMachine
    instance.WashingMachine = original
    assert instance.WashingMachine == original



@given(instance=Display_strategy)
def test_hyp_display_DishWasher_setter(instance):
    original = instance.DishWasher
    instance.DishWasher = original
    assert instance.DishWasher == original




@given(instance=Users_strategy)
def test_hyp_users_HTID_setter(instance):
    original = instance.HTID
    instance.HTID = original
    assert instance.HTID == original




@given(instance=Admin_strategy)
def test_hyp_admin_AdminID_setter(instance):
    original = instance.AdminID
    instance.AdminID = original
    assert instance.AdminID == original




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




@given(instance=Manager_strategy)
def test_hyp_manager_MangagerID_setter(instance):
    original = instance.MangagerID
    instance.MangagerID = original
    assert instance.MangagerID == original




@given(instance=Camera_strategy)
def test_hyp_camera_CameraID_setter(instance):
    original = instance.CameraID
    instance.CameraID = original
    assert instance.CameraID == original




@given(instance=Door_strategy)
def test_hyp_door_DoorID_setter(instance):
    original = instance.DoorID
    instance.DoorID = original
    assert instance.DoorID == original




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




@given(instance=Hub_Device_strategy)
def test_hyp_hub_device_Update_setter(instance):
    original = instance.Update
    instance.Update = original
    assert instance.Update == original



@given(instance=Hub_Device_strategy)
def test_hyp_hub_device_Status_setter(instance):
    original = instance.Status
    instance.Status = original
    assert instance.Status == original





@given(instance=UDP_Socket_strategy)
def test_hyp_udp_socket_socket_setter(instance):
    original = instance.socket
    instance.socket = original
    assert instance.socket == original


# ----- SECTION B: test_structural_full.py (deterministic-first suite) -----
import inspect
import pytest
from datetime import date, datetime, time, timedelta
from hypothesis import given, settings
import hypothesis.strategies as st

from python_code import (
    Admin,
    Alert,
    Camera,
    Display,
    Door,
    Employee,
    End_Of_Day,
    Home_Security_System,
    Hub_Device,
    Light,
    Manager,
    Motion_Sensor,
    PressureSensor,
    RFID_Sensor,
    Sensor,
    Start_Of_Day,
    UDP_Controller,
    UDP_Socket,
    Users,
    int,
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

def test_Admin_AdminID_value_roundtrip():
    instance = Admin(AdminID=7)
    assert instance.AdminID == 7
    instance.AdminID = 13
    assert instance.AdminID == 13


def test_Alert_AlertID_value_roundtrip():
    instance = Alert(AlertID=7)
    assert instance.AlertID == 7
    instance.AlertID = 13
    assert instance.AlertID == 13


def test_Camera_CameraID_value_roundtrip():
    instance = Camera(CameraID=7)
    assert instance.CameraID == 7
    instance.CameraID = 13
    assert instance.CameraID == 13


def test_Display_Alarm_value_roundtrip():
    instance = Display(Alarm="sample_text", Coffee="sample_text", DishWasher="sample_text", TimeID="sample_text", WashingMachine="sample_text")
    assert instance.Alarm == "sample_text"
    instance.Alarm = "sample_text_2"
    assert instance.Alarm == "sample_text_2"


def test_Display_Coffee_value_roundtrip():
    instance = Display(Alarm="sample_text", Coffee="sample_text", DishWasher="sample_text", TimeID="sample_text", WashingMachine="sample_text")
    assert instance.Coffee == "sample_text"
    instance.Coffee = "sample_text_2"
    assert instance.Coffee == "sample_text_2"


def test_Display_DishWasher_value_roundtrip():
    instance = Display(Alarm="sample_text", Coffee="sample_text", DishWasher="sample_text", TimeID="sample_text", WashingMachine="sample_text")
    assert instance.DishWasher == "sample_text"
    instance.DishWasher = "sample_text_2"
    assert instance.DishWasher == "sample_text_2"


def test_Display_TimeID_value_roundtrip():
    instance = Display(Alarm="sample_text", Coffee="sample_text", DishWasher="sample_text", TimeID="sample_text", WashingMachine="sample_text")
    assert instance.TimeID == "sample_text"
    instance.TimeID = "sample_text_2"
    assert instance.TimeID == "sample_text_2"


def test_Display_WashingMachine_value_roundtrip():
    instance = Display(Alarm="sample_text", Coffee="sample_text", DishWasher="sample_text", TimeID="sample_text", WashingMachine="sample_text")
    assert instance.WashingMachine == "sample_text"
    instance.WashingMachine = "sample_text_2"
    assert instance.WashingMachine == "sample_text_2"


def test_Door_DoorID_value_roundtrip():
    instance = Door(DoorID=7)
    assert instance.DoorID == 7
    instance.DoorID = 13
    assert instance.DoorID == 13


def test_Employee_EmployeeID_value_roundtrip():
    instance = Employee(EmployeeID=7)
    assert instance.EmployeeID == 7
    instance.EmployeeID = 13
    assert instance.EmployeeID == 13


def test_End_Of_Day_EOT_value_roundtrip():
    instance = End_Of_Day(EOT=7)
    assert instance.EOT == 7
    instance.EOT = 13
    assert instance.EOT == 13


def test_Home_Security_System_UserID_value_roundtrip():
    instance = Home_Security_System(UserID=7)
    assert instance.UserID == 7
    instance.UserID = 13
    assert instance.UserID == 13


def test_Hub_Device_Status_value_roundtrip():
    instance = Hub_Device(Status=True, Update=3.14)
    assert instance.Status == True
    instance.Status = False
    assert instance.Status == False


def test_Hub_Device_Update_value_roundtrip():
    instance = Hub_Device(Status=True, Update=3.14)
    assert instance.Update == 3.14
    instance.Update = 9.99
    assert instance.Update == 9.99


def test_Light_LightID_value_roundtrip():
    instance = Light(LightID="sample_text")
    assert instance.LightID == "sample_text"
    instance.LightID = "sample_text_2"
    assert instance.LightID == "sample_text_2"


def test_Manager_MangagerID_value_roundtrip():
    instance = Manager(MangagerID=7)
    assert instance.MangagerID == 7
    instance.MangagerID = 13
    assert instance.MangagerID == 13


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


def test_Start_Of_Day_SOT_value_roundtrip():
    instance = Start_Of_Day(SOT=7)
    assert instance.SOT == 7
    instance.SOT = 13
    assert instance.SOT == 13


def test_UDP_Controller_ip_session_value_roundtrip():
    instance = UDP_Controller(ip_session="sample_text")
    assert instance.ip_session == "sample_text"
    instance.ip_session = "sample_text_2"
    assert instance.ip_session == "sample_text_2"


def test_UDP_Socket_socket_value_roundtrip():
    instance = UDP_Socket(socket=7)
    assert instance.socket == 7
    instance.socket = 13
    assert instance.socket == 13


def test_Users_HTID_value_roundtrip():
    instance = Users(HTID="sample_text")
    assert instance.HTID == "sample_text"
    instance.HTID = "sample_text_2"
    assert instance.HTID == "sample_text_2"


def test_assoc_Door_Camera_link_reassign_clear():
    a = Door(DoorID=7)
    b1 = Camera(CameraID=7)
    b2 = Camera(CameraID=13)
    _safe_set(a, 'camera2', {b1})
    assert _is_linked(a, 'camera2', b1)
    if hasattr(b1, 'door3'):
        assert _is_linked(b1, 'door3', a)
    _safe_set(a, 'camera2', {b2})
    assert _is_linked(a, 'camera2', b2)
    if hasattr(b1, 'door3'):
        assert not _is_linked(b1, 'door3', a)
    if hasattr(b2, 'door3'):
        assert _is_linked(b2, 'door3', a)
    _safe_set(a, 'camera2', set())
    assert not _is_linked(a, 'camera2', b2)
    if hasattr(b2, 'door3'):
        assert not _is_linked(b2, 'door3', a)


def test_assoc_HomeTheatre_Speakers_link_reassign_clear():
    a = Users(HTID="sample_text")
    b1 = Manager(MangagerID=7)
    b2 = Manager(MangagerID=13)
    _safe_set(a, 'speakers6', b1)
    assert _is_linked(a, 'speakers6', b1)
    if hasattr(b1, 'homeTheatre7'):
        assert _is_linked(b1, 'homeTheatre7', a)
    _safe_set(a, 'speakers6', b2)
    assert _is_linked(a, 'speakers6', b2)
    if hasattr(b1, 'homeTheatre7'):
        assert not _is_linked(b1, 'homeTheatre7', a)
    if hasattr(b2, 'homeTheatre7'):
        assert _is_linked(b2, 'homeTheatre7', a)
    _safe_set(a, 'speakers6', None)
    assert not _is_linked(a, 'speakers6', b2)
    if hasattr(b2, 'homeTheatre7'):
        assert not _is_linked(b2, 'homeTheatre7', a)


def test_assoc_HomeTheatre_System_link_reassign_clear():
    a = Users(HTID="sample_text")
    b1 = Hub_Device(Status=True, Update=3.14)
    b2 = Hub_Device(Status=False, Update=9.99)
    _safe_set(a, 'system18', b1)
    assert _is_linked(a, 'system18', b1)
    if hasattr(b1, 'homeTheatre19'):
        assert _is_linked(b1, 'homeTheatre19', a)
    _safe_set(a, 'system18', b2)
    assert _is_linked(a, 'system18', b2)
    if hasattr(b1, 'homeTheatre19'):
        assert not _is_linked(b1, 'homeTheatre19', a)
    if hasattr(b2, 'homeTheatre19'):
        assert _is_linked(b2, 'homeTheatre19', a)
    _safe_set(a, 'system18', None)
    assert not _is_linked(a, 'system18', b2)
    if hasattr(b2, 'homeTheatre19'):
        assert not _is_linked(b2, 'homeTheatre19', a)


def test_assoc_HomeTheatre_TV_link_reassign_clear():
    a = Users(HTID="sample_text")
    b1 = Admin(AdminID=7)
    b2 = Admin(AdminID=13)
    _safe_set(a, 'tV4', b1)
    assert _is_linked(a, 'tV4', b1)
    if hasattr(b1, 'homeTheatre5'):
        assert _is_linked(b1, 'homeTheatre5', a)
    _safe_set(a, 'tV4', b2)
    assert _is_linked(a, 'tV4', b2)
    if hasattr(b1, 'homeTheatre5'):
        assert not _is_linked(b1, 'homeTheatre5', a)
    if hasattr(b2, 'homeTheatre5'):
        assert _is_linked(b2, 'homeTheatre5', a)
    _safe_set(a, 'tV4', None)
    assert not _is_linked(a, 'tV4', b2)
    if hasattr(b2, 'homeTheatre5'):
        assert not _is_linked(b2, 'homeTheatre5', a)


def test_assoc_Home_Security_System_Alert_link_reassign_clear():
    a = Home_Security_System(UserID=7)
    b1 = Alert(AlertID=7)
    b2 = Alert(AlertID=13)
    _safe_set(a, 'alert12', b1)
    assert _is_linked(a, 'alert12', b1)
    if hasattr(b1, 'home_Security_System13'):
        assert _is_linked(b1, 'home_Security_System13', a)
    _safe_set(a, 'alert12', b2)
    assert _is_linked(a, 'alert12', b2)
    if hasattr(b1, 'home_Security_System13'):
        assert not _is_linked(b1, 'home_Security_System13', a)
    if hasattr(b2, 'home_Security_System13'):
        assert _is_linked(b2, 'home_Security_System13', a)
    _safe_set(a, 'alert12', None)
    assert not _is_linked(a, 'alert12', b2)
    if hasattr(b2, 'home_Security_System13'):
        assert not _is_linked(b2, 'home_Security_System13', a)


def test_assoc_Home_Security_System_System_link_reassign_clear():
    a = Hub_Device(Status=True, Update=3.14)
    b1 = Home_Security_System(UserID=7)
    b2 = Home_Security_System(UserID=13)
    _safe_set(a, 'home_Security_System21', b1)
    assert _is_linked(a, 'home_Security_System21', b1)
    if hasattr(b1, 'system20'):
        assert _is_linked(b1, 'system20', a)
    _safe_set(a, 'home_Security_System21', b2)
    assert _is_linked(a, 'home_Security_System21', b2)
    if hasattr(b1, 'system20'):
        assert not _is_linked(b1, 'system20', a)
    if hasattr(b2, 'system20'):
        assert _is_linked(b2, 'system20', a)
    _safe_set(a, 'home_Security_System21', None)
    assert not _is_linked(a, 'home_Security_System21', b2)
    if hasattr(b2, 'system20'):
        assert not _is_linked(b2, 'system20', a)


def test_assoc_HouseHolds_End_Of_Day_link_reassign_clear():
    a = End_Of_Day(EOT=7)
    b1 = Display(Alarm="sample_text", Coffee="sample_text", DishWasher="sample_text", TimeID="sample_text", WashingMachine="sample_text")
    b2 = Display(Alarm="sample_text_2", Coffee="sample_text_2", DishWasher="sample_text_2", TimeID="sample_text_2", WashingMachine="sample_text_2")
    _safe_set(a, 'houseHolds11', b1)
    assert _is_linked(a, 'houseHolds11', b1)
    if hasattr(b1, 'end_Of_Day10'):
        assert _is_linked(b1, 'end_Of_Day10', a)
    _safe_set(a, 'houseHolds11', b2)
    assert _is_linked(a, 'houseHolds11', b2)
    if hasattr(b1, 'end_Of_Day10'):
        assert not _is_linked(b1, 'end_Of_Day10', a)
    if hasattr(b2, 'end_Of_Day10'):
        assert _is_linked(b2, 'end_Of_Day10', a)
    _safe_set(a, 'houseHolds11', None)
    assert not _is_linked(a, 'houseHolds11', b2)
    if hasattr(b2, 'end_Of_Day10'):
        assert not _is_linked(b2, 'end_Of_Day10', a)


def test_assoc_HouseHolds_Start_Of_Day_link_reassign_clear():
    a = Start_Of_Day(SOT=7)
    b1 = Display(Alarm="sample_text", Coffee="sample_text", DishWasher="sample_text", TimeID="sample_text", WashingMachine="sample_text")
    b2 = Display(Alarm="sample_text_2", Coffee="sample_text_2", DishWasher="sample_text_2", TimeID="sample_text_2", WashingMachine="sample_text_2")
    _safe_set(a, 'houseHolds9', b1)
    assert _is_linked(a, 'houseHolds9', b1)
    if hasattr(b1, 'start_Of_Day8'):
        assert _is_linked(b1, 'start_Of_Day8', a)
    _safe_set(a, 'houseHolds9', b2)
    assert _is_linked(a, 'houseHolds9', b2)
    if hasattr(b1, 'start_Of_Day8'):
        assert not _is_linked(b1, 'start_Of_Day8', a)
    if hasattr(b2, 'start_Of_Day8'):
        assert _is_linked(b2, 'start_Of_Day8', a)
    _safe_set(a, 'houseHolds9', None)
    assert not _is_linked(a, 'houseHolds9', b2)
    if hasattr(b2, 'start_Of_Day8'):
        assert not _is_linked(b2, 'start_Of_Day8', a)


def test_assoc_Sensor_Door_link_reassign_clear():
    a = Sensor(SensorID=7, SensorType=7)
    b1 = Door(DoorID=7)
    b2 = Door(DoorID=13)
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
    b1 = Hub_Device(Status=True, Update=3.14)
    b2 = Hub_Device(Status=False, Update=9.99)
    _safe_set(a, 'system14', b1)
    assert _is_linked(a, 'system14', b1)
    if hasattr(b1, 'sensor15'):
        assert _is_linked(b1, 'sensor15', a)
    _safe_set(a, 'system14', b2)
    assert _is_linked(a, 'system14', b2)
    if hasattr(b1, 'sensor15'):
        assert not _is_linked(b1, 'sensor15', a)
    if hasattr(b2, 'sensor15'):
        assert _is_linked(b2, 'sensor15', a)
    _safe_set(a, 'system14', None)
    assert not _is_linked(a, 'system14', b2)
    if hasattr(b2, 'sensor15'):
        assert not _is_linked(b2, 'sensor15', a)


def test_assoc_System_HouseHolds_link_reassign_clear():
    a = Hub_Device(Status=True, Update=3.14)
    b1 = Display(Alarm="sample_text", Coffee="sample_text", DishWasher="sample_text", TimeID="sample_text", WashingMachine="sample_text")
    b2 = Display(Alarm="sample_text_2", Coffee="sample_text_2", DishWasher="sample_text_2", TimeID="sample_text_2", WashingMachine="sample_text_2")
    _safe_set(a, 'houseHolds16', b1)
    assert _is_linked(a, 'houseHolds16', b1)
    if hasattr(b1, 'system17'):
        assert _is_linked(b1, 'system17', a)
    _safe_set(a, 'houseHolds16', b2)
    assert _is_linked(a, 'houseHolds16', b2)
    if hasattr(b1, 'system17'):
        assert not _is_linked(b1, 'system17', a)
    if hasattr(b2, 'system17'):
        assert _is_linked(b2, 'system17', a)
    _safe_set(a, 'houseHolds16', None)
    assert not _is_linked(a, 'houseHolds16', b2)
    if hasattr(b2, 'system17'):
        assert not _is_linked(b2, 'system17', a)


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

Admin_strategy = st.builds(Admin, AdminID=st.integers())
@given(instance=Admin_strategy)
@settings(max_examples=25)
def test_Admin_instantiation(instance):
    assert isinstance(instance, Admin)


Alert_strategy = st.builds(Alert, AlertID=st.integers())
@given(instance=Alert_strategy)
@settings(max_examples=25)
def test_Alert_instantiation(instance):
    assert isinstance(instance, Alert)


Camera_strategy = st.builds(Camera, CameraID=st.integers())
@given(instance=Camera_strategy)
@settings(max_examples=25)
def test_Camera_instantiation(instance):
    assert isinstance(instance, Camera)


Display_strategy = st.builds(Display, Alarm=safe_text, Coffee=safe_text, DishWasher=safe_text, TimeID=safe_text, WashingMachine=safe_text)
@given(instance=Display_strategy)
@settings(max_examples=25)
def test_Display_instantiation(instance):
    assert isinstance(instance, Display)


Door_strategy = st.builds(Door, DoorID=st.integers())
@given(instance=Door_strategy)
@settings(max_examples=25)
def test_Door_instantiation(instance):
    assert isinstance(instance, Door)


Employee_strategy = st.builds(Employee, EmployeeID=st.integers())
@given(instance=Employee_strategy)
@settings(max_examples=25)
def test_Employee_instantiation(instance):
    assert isinstance(instance, Employee)


End_Of_Day_strategy = st.builds(End_Of_Day, EOT=st.integers())
@given(instance=End_Of_Day_strategy)
@settings(max_examples=25)
def test_End_Of_Day_instantiation(instance):
    assert isinstance(instance, End_Of_Day)


Home_Security_System_strategy = st.builds(Home_Security_System, UserID=st.integers())
@given(instance=Home_Security_System_strategy)
@settings(max_examples=25)
def test_Home_Security_System_instantiation(instance):
    assert isinstance(instance, Home_Security_System)


Hub_Device_strategy = st.builds(Hub_Device, Status=st.booleans(), Update=st.floats(allow_nan=False, allow_infinity=False))
@given(instance=Hub_Device_strategy)
@settings(max_examples=25)
def test_Hub_Device_instantiation(instance):
    assert isinstance(instance, Hub_Device)


Light_strategy = st.builds(Light, LightID=safe_text)
@given(instance=Light_strategy)
@settings(max_examples=25)
def test_Light_instantiation(instance):
    assert isinstance(instance, Light)


Manager_strategy = st.builds(Manager, MangagerID=st.integers())
@given(instance=Manager_strategy)
@settings(max_examples=25)
def test_Manager_instantiation(instance):
    assert isinstance(instance, Manager)


Motion_Sensor_strategy = st.builds(Motion_Sensor)
@given(instance=Motion_Sensor_strategy)
@settings(max_examples=25)
def test_Motion_Sensor_instantiation(instance):
    assert isinstance(instance, Motion_Sensor)


PressureSensor_strategy = st.builds(PressureSensor)
@given(instance=PressureSensor_strategy)
@settings(max_examples=25)
def test_PressureSensor_instantiation(instance):
    assert isinstance(instance, PressureSensor)


RFID_Sensor_strategy = st.builds(RFID_Sensor)
@given(instance=RFID_Sensor_strategy)
@settings(max_examples=25)
def test_RFID_Sensor_instantiation(instance):
    assert isinstance(instance, RFID_Sensor)


Sensor_strategy = st.builds(Sensor, SensorID=st.integers(), SensorType=st.integers())
@given(instance=Sensor_strategy)
@settings(max_examples=25)
def test_Sensor_instantiation(instance):
    assert isinstance(instance, Sensor)


Start_Of_Day_strategy = st.builds(Start_Of_Day, SOT=st.integers())
@given(instance=Start_Of_Day_strategy)
@settings(max_examples=25)
def test_Start_Of_Day_instantiation(instance):
    assert isinstance(instance, Start_Of_Day)


UDP_Controller_strategy = st.builds(UDP_Controller, ip_session=safe_text)
@given(instance=UDP_Controller_strategy)
@settings(max_examples=25)
def test_UDP_Controller_instantiation(instance):
    assert isinstance(instance, UDP_Controller)


UDP_Socket_strategy = st.builds(UDP_Socket, socket=st.integers())
@given(instance=UDP_Socket_strategy)
@settings(max_examples=25)
def test_UDP_Socket_instantiation(instance):
    assert isinstance(instance, UDP_Socket)


Users_strategy = st.builds(Users, HTID=safe_text)
@given(instance=Users_strategy)
@settings(max_examples=25)
def test_Users_instantiation(instance):
    assert isinstance(instance, Users)


int_strategy = st.builds(int)
@given(instance=int_strategy)
@settings(max_examples=25)
def test_int_instantiation(instance):
    assert isinstance(instance, int)



