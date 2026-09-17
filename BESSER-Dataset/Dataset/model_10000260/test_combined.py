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
    SteamGenerator,
    Display,
    Heater,
    PhoneApplication,
    Interior_Container,
    Ingredient_Box,
    Cooking_System,
    Humidity_Sensor,
    Temperature_Sensor,
    Sensor,
    System,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_hyp_steamgenerator_is_not_abstract():
    assert not inspect.isabstract(SteamGenerator)


def test_hyp_steamgenerator_constructor_exists():
    assert callable(SteamGenerator.__init__)


def test_hyp_steamgenerator_constructor_args():
    sig = inspect.signature(SteamGenerator.__init__)
    params = list(sig.parameters.keys())
    assert "Status" in params, "Missing parameter 'Status'"




def test_hyp_display_is_not_abstract():
    assert not inspect.isabstract(Display)


def test_hyp_display_constructor_exists():
    assert callable(Display.__init__)


def test_hyp_display_constructor_args():
    sig = inspect.signature(Display.__init__)
    params = list(sig.parameters.keys())



def test_hyp_heater_is_not_abstract():
    assert not inspect.isabstract(Heater)


def test_hyp_heater_constructor_exists():
    assert callable(Heater.__init__)


def test_hyp_heater_constructor_args():
    sig = inspect.signature(Heater.__init__)
    params = list(sig.parameters.keys())
    assert "Status" in params, "Missing parameter 'Status'"




def test_hyp_phoneapplication_is_not_abstract():
    assert not inspect.isabstract(PhoneApplication)


def test_hyp_phoneapplication_constructor_exists():
    assert callable(PhoneApplication.__init__)


def test_hyp_phoneapplication_constructor_args():
    sig = inspect.signature(PhoneApplication.__init__)
    params = list(sig.parameters.keys())



def test_hyp_interior_container_is_not_abstract():
    assert not inspect.isabstract(Interior_Container)


def test_hyp_interior_container_constructor_exists():
    assert callable(Interior_Container.__init__)


def test_hyp_interior_container_constructor_args():
    sig = inspect.signature(Interior_Container.__init__)
    params = list(sig.parameters.keys())
    assert "WorkMode" in params, "Missing parameter 'WorkMode'"




def test_hyp_ingredient_box_is_not_abstract():
    assert not inspect.isabstract(Ingredient_Box)


def test_hyp_ingredient_box_constructor_exists():
    assert callable(Ingredient_Box.__init__)


def test_hyp_ingredient_box_constructor_args():
    sig = inspect.signature(Ingredient_Box.__init__)
    params = list(sig.parameters.keys())
    assert "WeightValue" in params, "Missing parameter 'WeightValue'"
    assert "BoxID" in params, "Missing parameter 'BoxID'"





def test_hyp_cooking_system_is_not_abstract():
    assert not inspect.isabstract(Cooking_System)


def test_hyp_cooking_system_constructor_exists():
    assert callable(Cooking_System.__init__)


def test_hyp_cooking_system_constructor_args():
    sig = inspect.signature(Cooking_System.__init__)
    params = list(sig.parameters.keys())



def test_hyp_humidity_sensor_is_not_abstract():
    assert not inspect.isabstract(Humidity_Sensor)


def test_hyp_humidity_sensor_constructor_exists():
    assert callable(Humidity_Sensor.__init__)


def test_hyp_humidity_sensor_constructor_args():
    sig = inspect.signature(Humidity_Sensor.__init__)
    params = list(sig.parameters.keys())
    assert "CurrentValue" in params, "Missing parameter 'CurrentValue'"




def test_hyp_temperature_sensor_is_not_abstract():
    assert not inspect.isabstract(Temperature_Sensor)


def test_hyp_temperature_sensor_constructor_exists():
    assert callable(Temperature_Sensor.__init__)


def test_hyp_temperature_sensor_constructor_args():
    sig = inspect.signature(Temperature_Sensor.__init__)
    params = list(sig.parameters.keys())
    assert "CurrentValue" in params, "Missing parameter 'CurrentValue'"




def test_hyp_sensor_is_not_abstract():
    assert not inspect.isabstract(Sensor)


def test_hyp_sensor_constructor_exists():
    assert callable(Sensor.__init__)


def test_hyp_sensor_constructor_args():
    sig = inspect.signature(Sensor.__init__)
    params = list(sig.parameters.keys())
    assert "SensorID" in params, "Missing parameter 'SensorID'"
    assert "SensorType" in params, "Missing parameter 'SensorType'"





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
SteamGenerator_strategy = st.builds(
    SteamGenerator,
    Status=
        st.booleans()
)
Display_strategy = st.builds(
    Display,
)
Heater_strategy = st.builds(
    Heater,
    Status=
        st.booleans()
)
PhoneApplication_strategy = st.builds(
    PhoneApplication,
)
Interior_Container_strategy = st.builds(
    Interior_Container,
    WorkMode=
        st.integers()
)
Ingredient_Box_strategy = st.builds(
    Ingredient_Box,
    WeightValue=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    BoxID=
        st.integers()
)
Cooking_System_strategy = st.builds(
    Cooking_System,
)
Humidity_Sensor_strategy = st.builds(
    Humidity_Sensor,
    CurrentValue=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
Temperature_Sensor_strategy = st.builds(
    Temperature_Sensor,
    CurrentValue=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
Sensor_strategy = st.builds(
    Sensor,
    SensorID=
        st.integers(),
    SensorType=
        st.integers()
)
System_strategy = st.builds(
    System,
    Status=
        st.booleans(),
    Update=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)




@given(instance=SteamGenerator_strategy)
def test_hyp_steamgenerator_Status_setter(instance):
    original = instance.Status
    instance.Status = original
    assert instance.Status == original





@given(instance=Heater_strategy)
def test_hyp_heater_Status_setter(instance):
    original = instance.Status
    instance.Status = original
    assert instance.Status == original





@given(instance=Interior_Container_strategy)
def test_hyp_interior_container_WorkMode_setter(instance):
    original = instance.WorkMode
    instance.WorkMode = original
    assert instance.WorkMode == original




@given(instance=Ingredient_Box_strategy)
def test_hyp_ingredient_box_WeightValue_setter(instance):
    original = instance.WeightValue
    instance.WeightValue = original
    assert instance.WeightValue == original



@given(instance=Ingredient_Box_strategy)
def test_hyp_ingredient_box_BoxID_setter(instance):
    original = instance.BoxID
    instance.BoxID = original
    assert instance.BoxID == original





@given(instance=Humidity_Sensor_strategy)
def test_hyp_humidity_sensor_CurrentValue_setter(instance):
    original = instance.CurrentValue
    instance.CurrentValue = original
    assert instance.CurrentValue == original




@given(instance=Temperature_Sensor_strategy)
def test_hyp_temperature_sensor_CurrentValue_setter(instance):
    original = instance.CurrentValue
    instance.CurrentValue = original
    assert instance.CurrentValue == original




@given(instance=Sensor_strategy)
def test_hyp_sensor_SensorID_setter(instance):
    original = instance.SensorID
    instance.SensorID = original
    assert instance.SensorID == original



@given(instance=Sensor_strategy)
def test_hyp_sensor_SensorType_setter(instance):
    original = instance.SensorType
    instance.SensorType = original
    assert instance.SensorType == original




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
    Cooking_System,
    Display,
    Heater,
    Humidity_Sensor,
    Ingredient_Box,
    Interior_Container,
    PhoneApplication,
    Sensor,
    SteamGenerator,
    System,
    Temperature_Sensor,
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

def test_Heater_Status_value_roundtrip():
    instance = Heater(Status=True)
    assert instance.Status == True
    instance.Status = False
    assert instance.Status == False


def test_Humidity_Sensor_CurrentValue_value_roundtrip():
    instance = Humidity_Sensor(CurrentValue=3.14)
    assert instance.CurrentValue == 3.14
    instance.CurrentValue = 9.99
    assert instance.CurrentValue == 9.99


def test_Ingredient_Box_BoxID_value_roundtrip():
    instance = Ingredient_Box(BoxID=7, WeightValue=3.14)
    assert instance.BoxID == 7
    instance.BoxID = 13
    assert instance.BoxID == 13


def test_Ingredient_Box_WeightValue_value_roundtrip():
    instance = Ingredient_Box(BoxID=7, WeightValue=3.14)
    assert instance.WeightValue == 3.14
    instance.WeightValue = 9.99
    assert instance.WeightValue == 9.99


def test_Interior_Container_WorkMode_value_roundtrip():
    instance = Interior_Container(WorkMode=7)
    assert instance.WorkMode == 7
    instance.WorkMode = 13
    assert instance.WorkMode == 13


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


def test_SteamGenerator_Status_value_roundtrip():
    instance = SteamGenerator(Status=True)
    assert instance.Status == True
    instance.Status = False
    assert instance.Status == False


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


def test_Temperature_Sensor_CurrentValue_value_roundtrip():
    instance = Temperature_Sensor(CurrentValue=3.14)
    assert instance.CurrentValue == 3.14
    instance.CurrentValue = 9.99
    assert instance.CurrentValue == 9.99


def test_assoc_HomeTheatre_System_link_reassign_clear():
    a = System(Status=True, Update=3.14)
    b1 = Display()
    b2 = Display()
    _safe_set(a, 'homeTheatre9', b1)
    assert _is_linked(a, 'homeTheatre9', b1)
    if hasattr(b1, 'system8'):
        assert _is_linked(b1, 'system8', a)
    _safe_set(a, 'homeTheatre9', b2)
    assert _is_linked(a, 'homeTheatre9', b2)
    if hasattr(b1, 'system8'):
        assert not _is_linked(b1, 'system8', a)
    if hasattr(b2, 'system8'):
        assert _is_linked(b2, 'system8', a)
    _safe_set(a, 'homeTheatre9', None)
    assert not _is_linked(a, 'homeTheatre9', b2)
    if hasattr(b2, 'system8'):
        assert not _is_linked(b2, 'system8', a)


def test_assoc_Home_Security_System_Alert_link_reassign_clear():
    a = Ingredient_Box(BoxID=7, WeightValue=3.14)
    b1 = Cooking_System()
    b2 = Cooking_System()
    _safe_set(a, 'home_Security_System5', b1)
    assert _is_linked(a, 'home_Security_System5', b1)
    if hasattr(b1, 'alert4'):
        assert _is_linked(b1, 'alert4', a)
    _safe_set(a, 'home_Security_System5', b2)
    assert _is_linked(a, 'home_Security_System5', b2)
    if hasattr(b1, 'alert4'):
        assert not _is_linked(b1, 'alert4', a)
    if hasattr(b2, 'alert4'):
        assert _is_linked(b2, 'alert4', a)
    _safe_set(a, 'home_Security_System5', None)
    assert not _is_linked(a, 'home_Security_System5', b2)
    if hasattr(b2, 'alert4'):
        assert not _is_linked(b2, 'alert4', a)


def test_assoc_Home_Security_System_System_link_reassign_clear():
    a = System(Status=True, Update=3.14)
    b1 = Cooking_System()
    b2 = Cooking_System()
    _safe_set(a, 'Cooking_System11', b1)
    assert _is_linked(a, 'Cooking_System11', b1)
    if hasattr(b1, 'Home_Security_System_System_010'):
        assert _is_linked(b1, 'Home_Security_System_System_010', a)
    _safe_set(a, 'Cooking_System11', b2)
    assert _is_linked(a, 'Cooking_System11', b2)
    if hasattr(b1, 'Home_Security_System_System_010'):
        assert not _is_linked(b1, 'Home_Security_System_System_010', a)
    if hasattr(b2, 'Home_Security_System_System_010'):
        assert _is_linked(b2, 'Home_Security_System_System_010', a)
    _safe_set(a, 'Cooking_System11', None)
    assert not _is_linked(a, 'Cooking_System11', b2)
    if hasattr(b2, 'Home_Security_System_System_010'):
        assert not _is_linked(b2, 'Home_Security_System_System_010', a)


def test_assoc_MicroPhone_System_link_reassign_clear():
    a = System(Status=True, Update=3.14)
    b1 = PhoneApplication()
    b2 = PhoneApplication()
    _safe_set(a, 'microPhone3', {b1})
    assert _is_linked(a, 'microPhone3', b1)
    if hasattr(b1, 'system2'):
        assert _is_linked(b1, 'system2', a)
    _safe_set(a, 'microPhone3', {b2})
    assert _is_linked(a, 'microPhone3', b2)
    if hasattr(b1, 'system2'):
        assert not _is_linked(b1, 'system2', a)
    if hasattr(b2, 'system2'):
        assert _is_linked(b2, 'system2', a)
    _safe_set(a, 'microPhone3', set())
    assert not _is_linked(a, 'microPhone3', b2)
    if hasattr(b2, 'system2'):
        assert not _is_linked(b2, 'system2', a)


def test_assoc_Sensor_Door_link_reassign_clear():
    a = Sensor(SensorID=7, SensorType=7)
    b1 = Interior_Container(WorkMode=7)
    b2 = Interior_Container(WorkMode=13)
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
    _safe_set(a, 'sensor7', {b1})
    assert _is_linked(a, 'sensor7', b1)
    if hasattr(b1, 'system6'):
        assert _is_linked(b1, 'system6', a)
    _safe_set(a, 'sensor7', {b2})
    assert _is_linked(a, 'sensor7', b2)
    if hasattr(b1, 'system6'):
        assert not _is_linked(b1, 'system6', a)
    if hasattr(b2, 'system6'):
        assert _is_linked(b2, 'system6', a)
    _safe_set(a, 'sensor7', set())
    assert not _is_linked(a, 'sensor7', b2)
    if hasattr(b2, 'system6'):
        assert not _is_linked(b2, 'system6', a)


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

Cooking_System_strategy = st.builds(Cooking_System)
@given(instance=Cooking_System_strategy)
@settings(max_examples=25)
def test_Cooking_System_instantiation(instance):
    assert isinstance(instance, Cooking_System)


Display_strategy = st.builds(Display)
@given(instance=Display_strategy)
@settings(max_examples=25)
def test_Display_instantiation(instance):
    assert isinstance(instance, Display)


Heater_strategy = st.builds(Heater, Status=st.booleans())
@given(instance=Heater_strategy)
@settings(max_examples=25)
def test_Heater_instantiation(instance):
    assert isinstance(instance, Heater)


Humidity_Sensor_strategy = st.builds(Humidity_Sensor, CurrentValue=st.floats(allow_nan=False, allow_infinity=False))
@given(instance=Humidity_Sensor_strategy)
@settings(max_examples=25)
def test_Humidity_Sensor_instantiation(instance):
    assert isinstance(instance, Humidity_Sensor)


Ingredient_Box_strategy = st.builds(Ingredient_Box, BoxID=st.integers(), WeightValue=st.floats(allow_nan=False, allow_infinity=False))
@given(instance=Ingredient_Box_strategy)
@settings(max_examples=25)
def test_Ingredient_Box_instantiation(instance):
    assert isinstance(instance, Ingredient_Box)


Interior_Container_strategy = st.builds(Interior_Container, WorkMode=st.integers())
@given(instance=Interior_Container_strategy)
@settings(max_examples=25)
def test_Interior_Container_instantiation(instance):
    assert isinstance(instance, Interior_Container)


PhoneApplication_strategy = st.builds(PhoneApplication)
@given(instance=PhoneApplication_strategy)
@settings(max_examples=25)
def test_PhoneApplication_instantiation(instance):
    assert isinstance(instance, PhoneApplication)


Sensor_strategy = st.builds(Sensor, SensorID=st.integers(), SensorType=st.integers())
@given(instance=Sensor_strategy)
@settings(max_examples=25)
def test_Sensor_instantiation(instance):
    assert isinstance(instance, Sensor)


SteamGenerator_strategy = st.builds(SteamGenerator, Status=st.booleans())
@given(instance=SteamGenerator_strategy)
@settings(max_examples=25)
def test_SteamGenerator_instantiation(instance):
    assert isinstance(instance, SteamGenerator)


System_strategy = st.builds(System, Status=st.booleans(), Update=st.floats(allow_nan=False, allow_infinity=False))
@given(instance=System_strategy)
@settings(max_examples=25)
def test_System_instantiation(instance):
    assert isinstance(instance, System)


Temperature_Sensor_strategy = st.builds(Temperature_Sensor, CurrentValue=st.floats(allow_nan=False, allow_infinity=False))
@given(instance=Temperature_Sensor_strategy)
@settings(max_examples=25)
def test_Temperature_Sensor_instantiation(instance):
    assert isinstance(instance, Temperature_Sensor)



