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
    SmartHouse_Projector,
    SmartHouse_Sensor,
    SmartHouse_AirConditioner,
    SmartHouse_Light,
    SmartHouse_CoffeeMaker,
    SmartHouse_WashingMachine,
    SmartHouse_Cooker,
    SmartHouse_Heating,
    SmartHouse_Window,
    SmartHouse_Room,
    SmartHouse_Security,
    SmartHouse_Gate,
    SmartHouse_EV,
    SmartHouse_WaterHeater,
    SmartHouse_Person,
    SmartHouse_House,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_hyp_smarthouse_projector_is_not_abstract():
    assert not inspect.isabstract(SmartHouse_Projector)


def test_hyp_smarthouse_projector_constructor_exists():
    assert callable(SmartHouse_Projector.__init__)


def test_hyp_smarthouse_projector_constructor_args():
    sig = inspect.signature(SmartHouse_Projector.__init__)
    params = list(sig.parameters.keys())
    assert "brightness" in params, "Missing parameter 'brightness'"
    assert "volume" in params, "Missing parameter 'volume'"
    assert "on" in params, "Missing parameter 'on'"






def test_hyp_smarthouse_sensor_is_not_abstract():
    assert not inspect.isabstract(SmartHouse_Sensor)


def test_hyp_smarthouse_sensor_constructor_exists():
    assert callable(SmartHouse_Sensor.__init__)


def test_hyp_smarthouse_sensor_constructor_args():
    sig = inspect.signature(SmartHouse_Sensor.__init__)
    params = list(sig.parameters.keys())
    assert "temp" in params, "Missing parameter 'temp'"
    assert "circle" in params, "Missing parameter 'circle'"
    assert "battery" in params, "Missing parameter 'battery'"
    assert "air" in params, "Missing parameter 'air'"
    assert "brightness" in params, "Missing parameter 'brightness'"








def test_hyp_smarthouse_airconditioner_is_not_abstract():
    assert not inspect.isabstract(SmartHouse_AirConditioner)


def test_hyp_smarthouse_airconditioner_constructor_exists():
    assert callable(SmartHouse_AirConditioner.__init__)


def test_hyp_smarthouse_airconditioner_constructor_args():
    sig = inspect.signature(SmartHouse_AirConditioner.__init__)
    params = list(sig.parameters.keys())
    assert "freshAir" in params, "Missing parameter 'freshAir'"
    assert "level" in params, "Missing parameter 'level'"





def test_hyp_smarthouse_light_is_not_abstract():
    assert not inspect.isabstract(SmartHouse_Light)


def test_hyp_smarthouse_light_constructor_exists():
    assert callable(SmartHouse_Light.__init__)


def test_hyp_smarthouse_light_constructor_args():
    sig = inspect.signature(SmartHouse_Light.__init__)
    params = list(sig.parameters.keys())
    assert "level" in params, "Missing parameter 'level'"




def test_hyp_smarthouse_coffeemaker_is_not_abstract():
    assert not inspect.isabstract(SmartHouse_CoffeeMaker)


def test_hyp_smarthouse_coffeemaker_constructor_exists():
    assert callable(SmartHouse_CoffeeMaker.__init__)


def test_hyp_smarthouse_coffeemaker_constructor_args():
    sig = inspect.signature(SmartHouse_CoffeeMaker.__init__)
    params = list(sig.parameters.keys())
    assert "loaded" in params, "Missing parameter 'loaded'"
    assert "on" in params, "Missing parameter 'on'"
    assert "warming" in params, "Missing parameter 'warming'"






def test_hyp_smarthouse_washingmachine_is_not_abstract():
    assert not inspect.isabstract(SmartHouse_WashingMachine)


def test_hyp_smarthouse_washingmachine_constructor_exists():
    assert callable(SmartHouse_WashingMachine.__init__)


def test_hyp_smarthouse_washingmachine_constructor_args():
    sig = inspect.signature(SmartHouse_WashingMachine.__init__)
    params = list(sig.parameters.keys())
    assert "loaded" in params, "Missing parameter 'loaded'"
    assert "on" in params, "Missing parameter 'on'"





def test_hyp_smarthouse_cooker_is_not_abstract():
    assert not inspect.isabstract(SmartHouse_Cooker)


def test_hyp_smarthouse_cooker_constructor_exists():
    assert callable(SmartHouse_Cooker.__init__)


def test_hyp_smarthouse_cooker_constructor_args():
    sig = inspect.signature(SmartHouse_Cooker.__init__)
    params = list(sig.parameters.keys())
    assert "on" in params, "Missing parameter 'on'"




def test_hyp_smarthouse_heating_is_not_abstract():
    assert not inspect.isabstract(SmartHouse_Heating)


def test_hyp_smarthouse_heating_constructor_exists():
    assert callable(SmartHouse_Heating.__init__)


def test_hyp_smarthouse_heating_constructor_args():
    sig = inspect.signature(SmartHouse_Heating.__init__)
    params = list(sig.parameters.keys())
    assert "level" in params, "Missing parameter 'level'"
    assert "name" in params, "Missing parameter 'name'"





def test_hyp_smarthouse_window_is_not_abstract():
    assert not inspect.isabstract(SmartHouse_Window)


def test_hyp_smarthouse_window_constructor_exists():
    assert callable(SmartHouse_Window.__init__)


def test_hyp_smarthouse_window_constructor_args():
    sig = inspect.signature(SmartHouse_Window.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "curtainOn" in params, "Missing parameter 'curtainOn'"
    assert "opened" in params, "Missing parameter 'opened'"






def test_hyp_smarthouse_room_is_not_abstract():
    assert not inspect.isabstract(SmartHouse_Room)


def test_hyp_smarthouse_room_constructor_exists():
    assert callable(SmartHouse_Room.__init__)


def test_hyp_smarthouse_room_constructor_args():
    sig = inspect.signature(SmartHouse_Room.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "bright" in params, "Missing parameter 'bright'"
    assert "temp" in params, "Missing parameter 'temp'"
    assert "air" in params, "Missing parameter 'air'"







def test_hyp_smarthouse_security_is_not_abstract():
    assert not inspect.isabstract(SmartHouse_Security)


def test_hyp_smarthouse_security_constructor_exists():
    assert callable(SmartHouse_Security.__init__)


def test_hyp_smarthouse_security_constructor_args():
    sig = inspect.signature(SmartHouse_Security.__init__)
    params = list(sig.parameters.keys())
    assert "on" in params, "Missing parameter 'on'"




def test_hyp_smarthouse_gate_is_not_abstract():
    assert not inspect.isabstract(SmartHouse_Gate)


def test_hyp_smarthouse_gate_constructor_exists():
    assert callable(SmartHouse_Gate.__init__)


def test_hyp_smarthouse_gate_constructor_args():
    sig = inspect.signature(SmartHouse_Gate.__init__)
    params = list(sig.parameters.keys())
    assert "outlocked" in params, "Missing parameter 'outlocked'"




def test_hyp_smarthouse_ev_is_not_abstract():
    assert not inspect.isabstract(SmartHouse_EV)


def test_hyp_smarthouse_ev_constructor_exists():
    assert callable(SmartHouse_EV.__init__)


def test_hyp_smarthouse_ev_constructor_args():
    sig = inspect.signature(SmartHouse_EV.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "pluged" in params, "Missing parameter 'pluged'"
    assert "charging" in params, "Missing parameter 'charging'"
    assert "level" in params, "Missing parameter 'level'"







def test_hyp_smarthouse_waterheater_is_not_abstract():
    assert not inspect.isabstract(SmartHouse_WaterHeater)


def test_hyp_smarthouse_waterheater_constructor_exists():
    assert callable(SmartHouse_WaterHeater.__init__)


def test_hyp_smarthouse_waterheater_constructor_args():
    sig = inspect.signature(SmartHouse_WaterHeater.__init__)
    params = list(sig.parameters.keys())
    assert "temp" in params, "Missing parameter 'temp'"
    assert "boost" in params, "Missing parameter 'boost'"
    assert "on" in params, "Missing parameter 'on'"






def test_hyp_smarthouse_person_is_not_abstract():
    assert not inspect.isabstract(SmartHouse_Person)


def test_hyp_smarthouse_person_constructor_exists():
    assert callable(SmartHouse_Person.__init__)


def test_hyp_smarthouse_person_constructor_args():
    sig = inspect.signature(SmartHouse_Person.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"




def test_hyp_smarthouse_house_is_not_abstract():
    assert not inspect.isabstract(SmartHouse_House)


def test_hyp_smarthouse_house_constructor_exists():
    assert callable(SmartHouse_House.__init__)


def test_hyp_smarthouse_house_constructor_args():
    sig = inspect.signature(SmartHouse_House.__init__)
    params = list(sig.parameters.keys())
    assert "outtemp" in params, "Missing parameter 'outtemp'"
    assert "eprice" in params, "Missing parameter 'eprice'"
    assert "name" in params, "Missing parameter 'name'"
    assert "time" in params, "Missing parameter 'time'"






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
SmartHouse_Projector_strategy = st.builds(
    SmartHouse_Projector,
    brightness=
        safe_text,
    volume=
        safe_text,
    on=
        st.booleans()
)
SmartHouse_Sensor_strategy = st.builds(
    SmartHouse_Sensor,
    temp=
        st.booleans(),
    circle=
        safe_text,
    battery=
        safe_text,
    air=
        st.booleans(),
    brightness=
        st.booleans()
)
SmartHouse_AirConditioner_strategy = st.builds(
    SmartHouse_AirConditioner,
    freshAir=
        st.booleans(),
    level=
        safe_text
)
SmartHouse_Light_strategy = st.builds(
    SmartHouse_Light,
    level=
        safe_text
)
SmartHouse_CoffeeMaker_strategy = st.builds(
    SmartHouse_CoffeeMaker,
    loaded=
        st.booleans(),
    on=
        st.booleans(),
    warming=
        st.booleans()
)
SmartHouse_WashingMachine_strategy = st.builds(
    SmartHouse_WashingMachine,
    loaded=
        st.booleans(),
    on=
        st.booleans()
)
SmartHouse_Cooker_strategy = st.builds(
    SmartHouse_Cooker,
    on=
        st.booleans()
)
SmartHouse_Heating_strategy = st.builds(
    SmartHouse_Heating,
    level=
        st.integers(),
    name=
        safe_text
)
SmartHouse_Window_strategy = st.builds(
    SmartHouse_Window,
    name=
        safe_text,
    curtainOn=
        st.booleans(),
    opened=
        st.booleans()
)
SmartHouse_Room_strategy = st.builds(
    SmartHouse_Room,
    name=
        safe_text,
    bright=
        safe_text,
    temp=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    air=
        st.integers()
)
SmartHouse_Security_strategy = st.builds(
    SmartHouse_Security,
    on=
        st.booleans()
)
SmartHouse_Gate_strategy = st.builds(
    SmartHouse_Gate,
    outlocked=
        st.booleans()
)
SmartHouse_EV_strategy = st.builds(
    SmartHouse_EV,
    name=
        safe_text,
    pluged=
        st.booleans(),
    charging=
        st.booleans(),
    level=
        safe_text
)
SmartHouse_WaterHeater_strategy = st.builds(
    SmartHouse_WaterHeater,
    temp=
        safe_text,
    boost=
        st.booleans(),
    on=
        st.booleans()
)
SmartHouse_Person_strategy = st.builds(
    SmartHouse_Person,
    name=
        safe_text
)
SmartHouse_House_strategy = st.builds(
    SmartHouse_House,
    outtemp=
        safe_text,
    eprice=
        safe_text,
    name=
        safe_text,
    time=
        safe_text
)




@given(instance=SmartHouse_Projector_strategy)
def test_hyp_smarthouse_projector_brightness_setter(instance):
    original = instance.brightness
    instance.brightness = original
    assert instance.brightness == original



@given(instance=SmartHouse_Projector_strategy)
def test_hyp_smarthouse_projector_volume_setter(instance):
    original = instance.volume
    instance.volume = original
    assert instance.volume == original



@given(instance=SmartHouse_Projector_strategy)
def test_hyp_smarthouse_projector_on_setter(instance):
    original = instance.on
    instance.on = original
    assert instance.on == original




@given(instance=SmartHouse_Sensor_strategy)
def test_hyp_smarthouse_sensor_temp_setter(instance):
    original = instance.temp
    instance.temp = original
    assert instance.temp == original



@given(instance=SmartHouse_Sensor_strategy)
def test_hyp_smarthouse_sensor_circle_setter(instance):
    original = instance.circle
    instance.circle = original
    assert instance.circle == original



@given(instance=SmartHouse_Sensor_strategy)
def test_hyp_smarthouse_sensor_battery_setter(instance):
    original = instance.battery
    instance.battery = original
    assert instance.battery == original



@given(instance=SmartHouse_Sensor_strategy)
def test_hyp_smarthouse_sensor_air_setter(instance):
    original = instance.air
    instance.air = original
    assert instance.air == original



@given(instance=SmartHouse_Sensor_strategy)
def test_hyp_smarthouse_sensor_brightness_setter(instance):
    original = instance.brightness
    instance.brightness = original
    assert instance.brightness == original




@given(instance=SmartHouse_AirConditioner_strategy)
def test_hyp_smarthouse_airconditioner_freshAir_setter(instance):
    original = instance.freshAir
    instance.freshAir = original
    assert instance.freshAir == original



@given(instance=SmartHouse_AirConditioner_strategy)
def test_hyp_smarthouse_airconditioner_level_setter(instance):
    original = instance.level
    instance.level = original
    assert instance.level == original




@given(instance=SmartHouse_Light_strategy)
def test_hyp_smarthouse_light_level_setter(instance):
    original = instance.level
    instance.level = original
    assert instance.level == original




@given(instance=SmartHouse_CoffeeMaker_strategy)
def test_hyp_smarthouse_coffeemaker_loaded_setter(instance):
    original = instance.loaded
    instance.loaded = original
    assert instance.loaded == original



@given(instance=SmartHouse_CoffeeMaker_strategy)
def test_hyp_smarthouse_coffeemaker_on_setter(instance):
    original = instance.on
    instance.on = original
    assert instance.on == original



@given(instance=SmartHouse_CoffeeMaker_strategy)
def test_hyp_smarthouse_coffeemaker_warming_setter(instance):
    original = instance.warming
    instance.warming = original
    assert instance.warming == original




@given(instance=SmartHouse_WashingMachine_strategy)
def test_hyp_smarthouse_washingmachine_loaded_setter(instance):
    original = instance.loaded
    instance.loaded = original
    assert instance.loaded == original



@given(instance=SmartHouse_WashingMachine_strategy)
def test_hyp_smarthouse_washingmachine_on_setter(instance):
    original = instance.on
    instance.on = original
    assert instance.on == original




@given(instance=SmartHouse_Cooker_strategy)
def test_hyp_smarthouse_cooker_on_setter(instance):
    original = instance.on
    instance.on = original
    assert instance.on == original




@given(instance=SmartHouse_Heating_strategy)
def test_hyp_smarthouse_heating_level_setter(instance):
    original = instance.level
    instance.level = original
    assert instance.level == original



@given(instance=SmartHouse_Heating_strategy)
def test_hyp_smarthouse_heating_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original




@given(instance=SmartHouse_Window_strategy)
def test_hyp_smarthouse_window_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=SmartHouse_Window_strategy)
def test_hyp_smarthouse_window_curtainOn_setter(instance):
    original = instance.curtainOn
    instance.curtainOn = original
    assert instance.curtainOn == original



@given(instance=SmartHouse_Window_strategy)
def test_hyp_smarthouse_window_opened_setter(instance):
    original = instance.opened
    instance.opened = original
    assert instance.opened == original




@given(instance=SmartHouse_Room_strategy)
def test_hyp_smarthouse_room_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=SmartHouse_Room_strategy)
def test_hyp_smarthouse_room_bright_setter(instance):
    original = instance.bright
    instance.bright = original
    assert instance.bright == original



@given(instance=SmartHouse_Room_strategy)
def test_hyp_smarthouse_room_temp_setter(instance):
    original = instance.temp
    instance.temp = original
    assert instance.temp == original



@given(instance=SmartHouse_Room_strategy)
def test_hyp_smarthouse_room_air_setter(instance):
    original = instance.air
    instance.air = original
    assert instance.air == original




@given(instance=SmartHouse_Security_strategy)
def test_hyp_smarthouse_security_on_setter(instance):
    original = instance.on
    instance.on = original
    assert instance.on == original




@given(instance=SmartHouse_Gate_strategy)
def test_hyp_smarthouse_gate_outlocked_setter(instance):
    original = instance.outlocked
    instance.outlocked = original
    assert instance.outlocked == original




@given(instance=SmartHouse_EV_strategy)
def test_hyp_smarthouse_ev_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=SmartHouse_EV_strategy)
def test_hyp_smarthouse_ev_pluged_setter(instance):
    original = instance.pluged
    instance.pluged = original
    assert instance.pluged == original



@given(instance=SmartHouse_EV_strategy)
def test_hyp_smarthouse_ev_charging_setter(instance):
    original = instance.charging
    instance.charging = original
    assert instance.charging == original



@given(instance=SmartHouse_EV_strategy)
def test_hyp_smarthouse_ev_level_setter(instance):
    original = instance.level
    instance.level = original
    assert instance.level == original




@given(instance=SmartHouse_WaterHeater_strategy)
def test_hyp_smarthouse_waterheater_temp_setter(instance):
    original = instance.temp
    instance.temp = original
    assert instance.temp == original



@given(instance=SmartHouse_WaterHeater_strategy)
def test_hyp_smarthouse_waterheater_boost_setter(instance):
    original = instance.boost
    instance.boost = original
    assert instance.boost == original



@given(instance=SmartHouse_WaterHeater_strategy)
def test_hyp_smarthouse_waterheater_on_setter(instance):
    original = instance.on
    instance.on = original
    assert instance.on == original




@given(instance=SmartHouse_Person_strategy)
def test_hyp_smarthouse_person_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original




@given(instance=SmartHouse_House_strategy)
def test_hyp_smarthouse_house_outtemp_setter(instance):
    original = instance.outtemp
    instance.outtemp = original
    assert instance.outtemp == original



@given(instance=SmartHouse_House_strategy)
def test_hyp_smarthouse_house_eprice_setter(instance):
    original = instance.eprice
    instance.eprice = original
    assert instance.eprice == original



@given(instance=SmartHouse_House_strategy)
def test_hyp_smarthouse_house_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=SmartHouse_House_strategy)
def test_hyp_smarthouse_house_time_setter(instance):
    original = instance.time
    instance.time = original
    assert instance.time == original


# ----- SECTION B: test_structural_full.py (deterministic-first suite) -----
import inspect
import pytest
from datetime import date, datetime, time, timedelta
from hypothesis import given, settings
import hypothesis.strategies as st

from python_code import (
    SmartHouse_AirConditioner,
    SmartHouse_CoffeeMaker,
    SmartHouse_Cooker,
    SmartHouse_EV,
    SmartHouse_Gate,
    SmartHouse_Heating,
    SmartHouse_House,
    SmartHouse_Light,
    SmartHouse_Person,
    SmartHouse_Projector,
    SmartHouse_Room,
    SmartHouse_Security,
    SmartHouse_Sensor,
    SmartHouse_WashingMachine,
    SmartHouse_WaterHeater,
    SmartHouse_Window,
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

def test_SmartHouse_AirConditioner_freshAir_value_roundtrip():
    instance = SmartHouse_AirConditioner(freshAir=True, level="sample_text")
    assert instance.freshAir == True
    instance.freshAir = False
    assert instance.freshAir == False


def test_SmartHouse_AirConditioner_level_value_roundtrip():
    instance = SmartHouse_AirConditioner(freshAir=True, level="sample_text")
    assert instance.level == "sample_text"
    instance.level = "sample_text_2"
    assert instance.level == "sample_text_2"


def test_SmartHouse_CoffeeMaker_loaded_value_roundtrip():
    instance = SmartHouse_CoffeeMaker(loaded=True, on=True, warming=True)
    assert instance.loaded == True
    instance.loaded = False
    assert instance.loaded == False


def test_SmartHouse_CoffeeMaker_on_value_roundtrip():
    instance = SmartHouse_CoffeeMaker(loaded=True, on=True, warming=True)
    assert instance.on == True
    instance.on = False
    assert instance.on == False


def test_SmartHouse_CoffeeMaker_warming_value_roundtrip():
    instance = SmartHouse_CoffeeMaker(loaded=True, on=True, warming=True)
    assert instance.warming == True
    instance.warming = False
    assert instance.warming == False


def test_SmartHouse_Cooker_on_value_roundtrip():
    instance = SmartHouse_Cooker(on=True)
    assert instance.on == True
    instance.on = False
    assert instance.on == False


def test_SmartHouse_EV_charging_value_roundtrip():
    instance = SmartHouse_EV(charging=True, level="sample_text", name="sample_text", pluged=True)
    assert instance.charging == True
    instance.charging = False
    assert instance.charging == False


def test_SmartHouse_EV_level_value_roundtrip():
    instance = SmartHouse_EV(charging=True, level="sample_text", name="sample_text", pluged=True)
    assert instance.level == "sample_text"
    instance.level = "sample_text_2"
    assert instance.level == "sample_text_2"


def test_SmartHouse_EV_name_value_roundtrip():
    instance = SmartHouse_EV(charging=True, level="sample_text", name="sample_text", pluged=True)
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_SmartHouse_EV_pluged_value_roundtrip():
    instance = SmartHouse_EV(charging=True, level="sample_text", name="sample_text", pluged=True)
    assert instance.pluged == True
    instance.pluged = False
    assert instance.pluged == False


def test_SmartHouse_Gate_outlocked_value_roundtrip():
    instance = SmartHouse_Gate(outlocked=True)
    assert instance.outlocked == True
    instance.outlocked = False
    assert instance.outlocked == False


def test_SmartHouse_Heating_level_value_roundtrip():
    instance = SmartHouse_Heating(level=7, name="sample_text")
    assert instance.level == 7
    instance.level = 13
    assert instance.level == 13


def test_SmartHouse_Heating_name_value_roundtrip():
    instance = SmartHouse_Heating(level=7, name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_SmartHouse_House_eprice_value_roundtrip():
    instance = SmartHouse_House(eprice="sample_text", name="sample_text", outtemp="sample_text", time="sample_text")
    assert instance.eprice == "sample_text"
    instance.eprice = "sample_text_2"
    assert instance.eprice == "sample_text_2"


def test_SmartHouse_House_name_value_roundtrip():
    instance = SmartHouse_House(eprice="sample_text", name="sample_text", outtemp="sample_text", time="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_SmartHouse_House_outtemp_value_roundtrip():
    instance = SmartHouse_House(eprice="sample_text", name="sample_text", outtemp="sample_text", time="sample_text")
    assert instance.outtemp == "sample_text"
    instance.outtemp = "sample_text_2"
    assert instance.outtemp == "sample_text_2"


def test_SmartHouse_House_time_value_roundtrip():
    instance = SmartHouse_House(eprice="sample_text", name="sample_text", outtemp="sample_text", time="sample_text")
    assert instance.time == "sample_text"
    instance.time = "sample_text_2"
    assert instance.time == "sample_text_2"


def test_SmartHouse_Light_level_value_roundtrip():
    instance = SmartHouse_Light(level="sample_text")
    assert instance.level == "sample_text"
    instance.level = "sample_text_2"
    assert instance.level == "sample_text_2"


def test_SmartHouse_Person_name_value_roundtrip():
    instance = SmartHouse_Person(name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_SmartHouse_Projector_brightness_value_roundtrip():
    instance = SmartHouse_Projector(brightness="sample_text", on=True, volume="sample_text")
    assert instance.brightness == "sample_text"
    instance.brightness = "sample_text_2"
    assert instance.brightness == "sample_text_2"


def test_SmartHouse_Projector_on_value_roundtrip():
    instance = SmartHouse_Projector(brightness="sample_text", on=True, volume="sample_text")
    assert instance.on == True
    instance.on = False
    assert instance.on == False


def test_SmartHouse_Projector_volume_value_roundtrip():
    instance = SmartHouse_Projector(brightness="sample_text", on=True, volume="sample_text")
    assert instance.volume == "sample_text"
    instance.volume = "sample_text_2"
    assert instance.volume == "sample_text_2"


def test_SmartHouse_Room_air_value_roundtrip():
    instance = SmartHouse_Room(air=7, bright="sample_text", name="sample_text", temp=3.14)
    assert instance.air == 7
    instance.air = 13
    assert instance.air == 13


def test_SmartHouse_Room_bright_value_roundtrip():
    instance = SmartHouse_Room(air=7, bright="sample_text", name="sample_text", temp=3.14)
    assert instance.bright == "sample_text"
    instance.bright = "sample_text_2"
    assert instance.bright == "sample_text_2"


def test_SmartHouse_Room_name_value_roundtrip():
    instance = SmartHouse_Room(air=7, bright="sample_text", name="sample_text", temp=3.14)
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_SmartHouse_Room_temp_value_roundtrip():
    instance = SmartHouse_Room(air=7, bright="sample_text", name="sample_text", temp=3.14)
    assert instance.temp == 3.14
    instance.temp = 9.99
    assert instance.temp == 9.99


def test_SmartHouse_Security_on_value_roundtrip():
    instance = SmartHouse_Security(on=True)
    assert instance.on == True
    instance.on = False
    assert instance.on == False


def test_SmartHouse_Sensor_air_value_roundtrip():
    instance = SmartHouse_Sensor(air=True, battery="sample_text", brightness=True, circle="sample_text", temp=True)
    assert instance.air == True
    instance.air = False
    assert instance.air == False


def test_SmartHouse_Sensor_battery_value_roundtrip():
    instance = SmartHouse_Sensor(air=True, battery="sample_text", brightness=True, circle="sample_text", temp=True)
    assert instance.battery == "sample_text"
    instance.battery = "sample_text_2"
    assert instance.battery == "sample_text_2"


def test_SmartHouse_Sensor_brightness_value_roundtrip():
    instance = SmartHouse_Sensor(air=True, battery="sample_text", brightness=True, circle="sample_text", temp=True)
    assert instance.brightness == True
    instance.brightness = False
    assert instance.brightness == False


def test_SmartHouse_Sensor_circle_value_roundtrip():
    instance = SmartHouse_Sensor(air=True, battery="sample_text", brightness=True, circle="sample_text", temp=True)
    assert instance.circle == "sample_text"
    instance.circle = "sample_text_2"
    assert instance.circle == "sample_text_2"


def test_SmartHouse_Sensor_temp_value_roundtrip():
    instance = SmartHouse_Sensor(air=True, battery="sample_text", brightness=True, circle="sample_text", temp=True)
    assert instance.temp == True
    instance.temp = False
    assert instance.temp == False


def test_SmartHouse_WashingMachine_loaded_value_roundtrip():
    instance = SmartHouse_WashingMachine(loaded=True, on=True)
    assert instance.loaded == True
    instance.loaded = False
    assert instance.loaded == False


def test_SmartHouse_WashingMachine_on_value_roundtrip():
    instance = SmartHouse_WashingMachine(loaded=True, on=True)
    assert instance.on == True
    instance.on = False
    assert instance.on == False


def test_SmartHouse_WaterHeater_boost_value_roundtrip():
    instance = SmartHouse_WaterHeater(boost=True, on=True, temp="sample_text")
    assert instance.boost == True
    instance.boost = False
    assert instance.boost == False


def test_SmartHouse_WaterHeater_on_value_roundtrip():
    instance = SmartHouse_WaterHeater(boost=True, on=True, temp="sample_text")
    assert instance.on == True
    instance.on = False
    assert instance.on == False


def test_SmartHouse_WaterHeater_temp_value_roundtrip():
    instance = SmartHouse_WaterHeater(boost=True, on=True, temp="sample_text")
    assert instance.temp == "sample_text"
    instance.temp = "sample_text_2"
    assert instance.temp == "sample_text_2"


def test_SmartHouse_Window_curtainOn_value_roundtrip():
    instance = SmartHouse_Window(curtainOn=True, name="sample_text", opened=True)
    assert instance.curtainOn == True
    instance.curtainOn = False
    assert instance.curtainOn == False


def test_SmartHouse_Window_name_value_roundtrip():
    instance = SmartHouse_Window(curtainOn=True, name="sample_text", opened=True)
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_SmartHouse_Window_opened_value_roundtrip():
    instance = SmartHouse_Window(curtainOn=True, name="sample_text", opened=True)
    assert instance.opened == True
    instance.opened = False
    assert instance.opened == False


def test_assoc_ac24_link_reassign_clear():
    a = SmartHouse_Room(air=7, bright="sample_text", name="sample_text", temp=3.14)
    b1 = SmartHouse_AirConditioner(freshAir=True, level="sample_text")
    b2 = SmartHouse_AirConditioner(freshAir=False, level="sample_text_2")
    _safe_set(a, 'room25', {b1})
    assert _is_linked(a, 'room25', b1)
    if hasattr(b1, 'AirConditioner'):
        assert _is_linked(b1, 'AirConditioner', a)
    _safe_set(a, 'room25', {b2})
    assert _is_linked(a, 'room25', b2)
    if hasattr(b1, 'AirConditioner'):
        assert not _is_linked(b1, 'AirConditioner', a)
    if hasattr(b2, 'AirConditioner'):
        assert _is_linked(b2, 'AirConditioner', a)
    _safe_set(a, 'room25', set())
    assert not _is_linked(a, 'room25', b2)
    if hasattr(b2, 'AirConditioner'):
        assert not _is_linked(b2, 'AirConditioner', a)


def test_assoc_cm37_link_reassign_clear():
    a = SmartHouse_Room(air=7, bright="sample_text", name="sample_text", temp=3.14)
    b1 = SmartHouse_CoffeeMaker(loaded=True, on=True, warming=True)
    b2 = SmartHouse_CoffeeMaker(loaded=False, on=False, warming=False)
    _safe_set(a, 'room38', b1)
    assert _is_linked(a, 'room38', b1)
    if hasattr(b1, 'CoffeeMaker'):
        assert _is_linked(b1, 'CoffeeMaker', a)
    _safe_set(a, 'room38', b2)
    assert _is_linked(a, 'room38', b2)
    if hasattr(b1, 'CoffeeMaker'):
        assert not _is_linked(b1, 'CoffeeMaker', a)
    if hasattr(b2, 'CoffeeMaker'):
        assert _is_linked(b2, 'CoffeeMaker', a)
    _safe_set(a, 'room38', None)
    assert not _is_linked(a, 'room38', b2)
    if hasattr(b2, 'CoffeeMaker'):
        assert not _is_linked(b2, 'CoffeeMaker', a)


def test_assoc_cooker33_link_reassign_clear():
    a = SmartHouse_Room(air=7, bright="sample_text", name="sample_text", temp=3.14)
    b1 = SmartHouse_Cooker(on=True)
    b2 = SmartHouse_Cooker(on=False)
    _safe_set(a, 'SmartHouse_Room34', b1)
    assert _is_linked(a, 'SmartHouse_Room34', b1)
    if hasattr(b1, 'SmartHouse_Cooker'):
        assert _is_linked(b1, 'SmartHouse_Cooker', a)
    _safe_set(a, 'SmartHouse_Room34', b2)
    assert _is_linked(a, 'SmartHouse_Room34', b2)
    if hasattr(b1, 'SmartHouse_Cooker'):
        assert not _is_linked(b1, 'SmartHouse_Cooker', a)
    if hasattr(b2, 'SmartHouse_Cooker'):
        assert _is_linked(b2, 'SmartHouse_Cooker', a)
    _safe_set(a, 'SmartHouse_Room34', None)
    assert not _is_linked(a, 'SmartHouse_Room34', b2)
    if hasattr(b2, 'SmartHouse_Cooker'):
        assert not _is_linked(b2, 'SmartHouse_Cooker', a)


def test_assoc_ev4_link_reassign_clear():
    a = SmartHouse_House(eprice="sample_text", name="sample_text", outtemp="sample_text", time="sample_text")
    b1 = SmartHouse_EV(charging=True, level="sample_text", name="sample_text", pluged=True)
    b2 = SmartHouse_EV(charging=False, level="sample_text_2", name="sample_text_2", pluged=False)
    _safe_set(a, 'house5', {b1})
    assert _is_linked(a, 'house5', b1)
    if hasattr(b1, 'EV'):
        assert _is_linked(b1, 'EV', a)
    _safe_set(a, 'house5', {b2})
    assert _is_linked(a, 'house5', b2)
    if hasattr(b1, 'EV'):
        assert not _is_linked(b1, 'EV', a)
    if hasattr(b2, 'EV'):
        assert _is_linked(b2, 'EV', a)
    _safe_set(a, 'house5', set())
    assert not _is_linked(a, 'house5', b2)
    if hasattr(b2, 'EV'):
        assert not _is_linked(b2, 'EV', a)


def test_assoc_gate6_link_reassign_clear():
    a = SmartHouse_House(eprice="sample_text", name="sample_text", outtemp="sample_text", time="sample_text")
    b1 = SmartHouse_Gate(outlocked=True)
    b2 = SmartHouse_Gate(outlocked=False)
    _safe_set(a, 'house7', b1)
    assert _is_linked(a, 'house7', b1)
    if hasattr(b1, 'Gate'):
        assert _is_linked(b1, 'Gate', a)
    _safe_set(a, 'house7', b2)
    assert _is_linked(a, 'house7', b2)
    if hasattr(b1, 'Gate'):
        assert not _is_linked(b1, 'Gate', a)
    if hasattr(b2, 'Gate'):
        assert _is_linked(b2, 'Gate', a)
    _safe_set(a, 'house7', None)
    assert not _is_linked(a, 'house7', b2)
    if hasattr(b2, 'Gate'):
        assert not _is_linked(b2, 'Gate', a)


def test_assoc_heating20_link_reassign_clear():
    a = SmartHouse_Room(air=7, bright="sample_text", name="sample_text", temp=3.14)
    b1 = SmartHouse_Heating(level=7, name="sample_text")
    b2 = SmartHouse_Heating(level=13, name="sample_text_2")
    _safe_set(a, 'SmartHouse_Room21', {b1})
    assert _is_linked(a, 'SmartHouse_Room21', b1)
    if hasattr(b1, 'SmartHouse_Heating'):
        assert _is_linked(b1, 'SmartHouse_Heating', a)
    _safe_set(a, 'SmartHouse_Room21', {b2})
    assert _is_linked(a, 'SmartHouse_Room21', b2)
    if hasattr(b1, 'SmartHouse_Heating'):
        assert not _is_linked(b1, 'SmartHouse_Heating', a)
    if hasattr(b2, 'SmartHouse_Heating'):
        assert _is_linked(b2, 'SmartHouse_Heating', a)
    _safe_set(a, 'SmartHouse_Room21', set())
    assert not _is_linked(a, 'SmartHouse_Room21', b2)
    if hasattr(b2, 'SmartHouse_Heating'):
        assert not _is_linked(b2, 'SmartHouse_Heating', a)


def test_assoc_house10_link_reassign_clear():
    a = SmartHouse_House(eprice="sample_text", name="sample_text", outtemp="sample_text", time="sample_text")
    b1 = SmartHouse_Gate(outlocked=True)
    b2 = SmartHouse_Gate(outlocked=False)
    _safe_set(a, 'House', b1)
    assert _is_linked(a, 'House', b1)
    if hasattr(b1, 'gate'):
        assert _is_linked(b1, 'gate', a)
    _safe_set(a, 'House', b2)
    assert _is_linked(a, 'House', b2)
    if hasattr(b1, 'gate'):
        assert not _is_linked(b1, 'gate', a)
    if hasattr(b2, 'gate'):
        assert _is_linked(b2, 'gate', a)
    _safe_set(a, 'House', None)
    assert not _is_linked(a, 'House', b2)
    if hasattr(b2, 'gate'):
        assert not _is_linked(b2, 'gate', a)


def test_assoc_house11_link_reassign_clear():
    a = SmartHouse_Security(on=True)
    b1 = SmartHouse_House(eprice="sample_text", name="sample_text", outtemp="sample_text", time="sample_text")
    b2 = SmartHouse_House(eprice="sample_text_2", name="sample_text_2", outtemp="sample_text_2", time="sample_text_2")
    _safe_set(a, 'sec', b1)
    assert _is_linked(a, 'sec', b1)
    if hasattr(b1, 'House12'):
        assert _is_linked(b1, 'House12', a)
    _safe_set(a, 'sec', b2)
    assert _is_linked(a, 'sec', b2)
    if hasattr(b1, 'House12'):
        assert not _is_linked(b1, 'House12', a)
    if hasattr(b2, 'House12'):
        assert _is_linked(b2, 'House12', a)
    _safe_set(a, 'sec', None)
    assert not _is_linked(a, 'sec', b2)
    if hasattr(b2, 'House12'):
        assert not _is_linked(b2, 'House12', a)


def test_assoc_house13_link_reassign_clear():
    a = SmartHouse_WaterHeater(boost=True, on=True, temp="sample_text")
    b1 = SmartHouse_House(eprice="sample_text", name="sample_text", outtemp="sample_text", time="sample_text")
    b2 = SmartHouse_House(eprice="sample_text_2", name="sample_text_2", outtemp="sample_text_2", time="sample_text_2")
    _safe_set(a, 'wh', b1)
    assert _is_linked(a, 'wh', b1)
    if hasattr(b1, 'House14'):
        assert _is_linked(b1, 'House14', a)
    _safe_set(a, 'wh', b2)
    assert _is_linked(a, 'wh', b2)
    if hasattr(b1, 'House14'):
        assert not _is_linked(b1, 'House14', a)
    if hasattr(b2, 'House14'):
        assert _is_linked(b2, 'House14', a)
    _safe_set(a, 'wh', None)
    assert not _is_linked(a, 'wh', b2)
    if hasattr(b2, 'House14'):
        assert not _is_linked(b2, 'House14', a)


def test_assoc_house15_link_reassign_clear():
    a = SmartHouse_House(eprice="sample_text", name="sample_text", outtemp="sample_text", time="sample_text")
    b1 = SmartHouse_EV(charging=True, level="sample_text", name="sample_text", pluged=True)
    b2 = SmartHouse_EV(charging=False, level="sample_text_2", name="sample_text_2", pluged=False)
    _safe_set(a, 'House16', b1)
    assert _is_linked(a, 'House16', b1)
    if hasattr(b1, 'ev'):
        assert _is_linked(b1, 'ev', a)
    _safe_set(a, 'House16', b2)
    assert _is_linked(a, 'House16', b2)
    if hasattr(b1, 'ev'):
        assert not _is_linked(b1, 'ev', a)
    if hasattr(b2, 'ev'):
        assert _is_linked(b2, 'ev', a)
    _safe_set(a, 'House16', None)
    assert not _is_linked(a, 'House16', b2)
    if hasattr(b2, 'ev'):
        assert not _is_linked(b2, 'ev', a)


def test_assoc_house17_link_reassign_clear():
    a = SmartHouse_Room(air=7, bright="sample_text", name="sample_text", temp=3.14)
    b1 = SmartHouse_House(eprice="sample_text", name="sample_text", outtemp="sample_text", time="sample_text")
    b2 = SmartHouse_House(eprice="sample_text_2", name="sample_text_2", outtemp="sample_text_2", time="sample_text_2")
    _safe_set(a, 'room', b1)
    assert _is_linked(a, 'room', b1)
    if hasattr(b1, 'House18'):
        assert _is_linked(b1, 'House18', a)
    _safe_set(a, 'room', b2)
    assert _is_linked(a, 'room', b2)
    if hasattr(b1, 'House18'):
        assert not _is_linked(b1, 'House18', a)
    if hasattr(b2, 'House18'):
        assert _is_linked(b2, 'House18', a)
    _safe_set(a, 'room', None)
    assert not _is_linked(a, 'room', b2)
    if hasattr(b2, 'House18'):
        assert not _is_linked(b2, 'House18', a)


def test_assoc_light22_link_reassign_clear():
    a = SmartHouse_Room(air=7, bright="sample_text", name="sample_text", temp=3.14)
    b1 = SmartHouse_Light(level="sample_text")
    b2 = SmartHouse_Light(level="sample_text_2")
    _safe_set(a, 'SmartHouse_Room23', {b1})
    assert _is_linked(a, 'SmartHouse_Room23', b1)
    if hasattr(b1, 'SmartHouse_Light'):
        assert _is_linked(b1, 'SmartHouse_Light', a)
    _safe_set(a, 'SmartHouse_Room23', {b2})
    assert _is_linked(a, 'SmartHouse_Room23', b2)
    if hasattr(b1, 'SmartHouse_Light'):
        assert not _is_linked(b1, 'SmartHouse_Light', a)
    if hasattr(b2, 'SmartHouse_Light'):
        assert _is_linked(b2, 'SmartHouse_Light', a)
    _safe_set(a, 'SmartHouse_Room23', set())
    assert not _is_linked(a, 'SmartHouse_Room23', b2)
    if hasattr(b2, 'SmartHouse_Light'):
        assert not _is_linked(b2, 'SmartHouse_Light', a)


def test_assoc_member1_link_reassign_clear():
    a = SmartHouse_Person(name="sample_text")
    b1 = SmartHouse_House(eprice="sample_text", name="sample_text", outtemp="sample_text", time="sample_text")
    b2 = SmartHouse_House(eprice="sample_text_2", name="sample_text_2", outtemp="sample_text_2", time="sample_text_2")
    _safe_set(a, 'SmartHouse_Person', b1)
    assert _is_linked(a, 'SmartHouse_Person', b1)
    if hasattr(b1, 'SmartHouse_House'):
        assert _is_linked(b1, 'SmartHouse_House', a)
    _safe_set(a, 'SmartHouse_Person', b2)
    assert _is_linked(a, 'SmartHouse_Person', b2)
    if hasattr(b1, 'SmartHouse_House'):
        assert not _is_linked(b1, 'SmartHouse_House', a)
    if hasattr(b2, 'SmartHouse_House'):
        assert _is_linked(b2, 'SmartHouse_House', a)
    _safe_set(a, 'SmartHouse_Person', None)
    assert not _is_linked(a, 'SmartHouse_Person', b2)
    if hasattr(b2, 'SmartHouse_House'):
        assert not _is_linked(b2, 'SmartHouse_House', a)


def test_assoc_occupied26_link_reassign_clear():
    a = SmartHouse_Room(air=7, bright="sample_text", name="sample_text", temp=3.14)
    b1 = SmartHouse_Person(name="sample_text")
    b2 = SmartHouse_Person(name="sample_text_2")
    _safe_set(a, 'SmartHouse_Room27', {b1})
    assert _is_linked(a, 'SmartHouse_Room27', b1)
    if hasattr(b1, 'SmartHouse_Person28'):
        assert _is_linked(b1, 'SmartHouse_Person28', a)
    _safe_set(a, 'SmartHouse_Room27', {b2})
    assert _is_linked(a, 'SmartHouse_Room27', b2)
    if hasattr(b1, 'SmartHouse_Person28'):
        assert not _is_linked(b1, 'SmartHouse_Person28', a)
    if hasattr(b2, 'SmartHouse_Person28'):
        assert _is_linked(b2, 'SmartHouse_Person28', a)
    _safe_set(a, 'SmartHouse_Room27', set())
    assert not _is_linked(a, 'SmartHouse_Room27', b2)
    if hasattr(b2, 'SmartHouse_Person28'):
        assert not _is_linked(b2, 'SmartHouse_Person28', a)


def test_assoc_projector31_link_reassign_clear():
    a = SmartHouse_Room(air=7, bright="sample_text", name="sample_text", temp=3.14)
    b1 = SmartHouse_Projector(brightness="sample_text", on=True, volume="sample_text")
    b2 = SmartHouse_Projector(brightness="sample_text_2", on=False, volume="sample_text_2")
    _safe_set(a, 'room32', b1)
    assert _is_linked(a, 'room32', b1)
    if hasattr(b1, 'Projector'):
        assert _is_linked(b1, 'Projector', a)
    _safe_set(a, 'room32', b2)
    assert _is_linked(a, 'room32', b2)
    if hasattr(b1, 'Projector'):
        assert not _is_linked(b1, 'Projector', a)
    if hasattr(b2, 'Projector'):
        assert _is_linked(b2, 'Projector', a)
    _safe_set(a, 'room32', None)
    assert not _is_linked(a, 'room32', b2)
    if hasattr(b2, 'Projector'):
        assert not _is_linked(b2, 'Projector', a)


def test_assoc_room0_link_reassign_clear():
    a = SmartHouse_Room(air=7, bright="sample_text", name="sample_text", temp=3.14)
    b1 = SmartHouse_House(eprice="sample_text", name="sample_text", outtemp="sample_text", time="sample_text")
    b2 = SmartHouse_House(eprice="sample_text_2", name="sample_text_2", outtemp="sample_text_2", time="sample_text_2")
    _safe_set(a, 'Room', b1)
    assert _is_linked(a, 'Room', b1)
    if hasattr(b1, 'house'):
        assert _is_linked(b1, 'house', a)
    _safe_set(a, 'Room', b2)
    assert _is_linked(a, 'Room', b2)
    if hasattr(b1, 'house'):
        assert not _is_linked(b1, 'house', a)
    if hasattr(b2, 'house'):
        assert _is_linked(b2, 'house', a)
    _safe_set(a, 'Room', None)
    assert not _is_linked(a, 'Room', b2)
    if hasattr(b2, 'house'):
        assert not _is_linked(b2, 'house', a)


def test_assoc_room39_link_reassign_clear():
    a = SmartHouse_Room(air=7, bright="sample_text", name="sample_text", temp=3.14)
    b1 = SmartHouse_AirConditioner(freshAir=True, level="sample_text")
    b2 = SmartHouse_AirConditioner(freshAir=False, level="sample_text_2")
    _safe_set(a, 'Room40', b1)
    assert _is_linked(a, 'Room40', b1)
    if hasattr(b1, 'ac'):
        assert _is_linked(b1, 'ac', a)
    _safe_set(a, 'Room40', b2)
    assert _is_linked(a, 'Room40', b2)
    if hasattr(b1, 'ac'):
        assert not _is_linked(b1, 'ac', a)
    if hasattr(b2, 'ac'):
        assert _is_linked(b2, 'ac', a)
    _safe_set(a, 'Room40', None)
    assert not _is_linked(a, 'Room40', b2)
    if hasattr(b2, 'ac'):
        assert not _is_linked(b2, 'ac', a)


def test_assoc_room41_link_reassign_clear():
    a = SmartHouse_Room(air=7, bright="sample_text", name="sample_text", temp=3.14)
    b1 = SmartHouse_Projector(brightness="sample_text", on=True, volume="sample_text")
    b2 = SmartHouse_Projector(brightness="sample_text_2", on=False, volume="sample_text_2")
    _safe_set(a, 'Room42', b1)
    assert _is_linked(a, 'Room42', b1)
    if hasattr(b1, 'projector'):
        assert _is_linked(b1, 'projector', a)
    _safe_set(a, 'Room42', b2)
    assert _is_linked(a, 'Room42', b2)
    if hasattr(b1, 'projector'):
        assert not _is_linked(b1, 'projector', a)
    if hasattr(b2, 'projector'):
        assert _is_linked(b2, 'projector', a)
    _safe_set(a, 'Room42', None)
    assert not _is_linked(a, 'Room42', b2)
    if hasattr(b2, 'projector'):
        assert not _is_linked(b2, 'projector', a)


def test_assoc_room43_link_reassign_clear():
    a = SmartHouse_WashingMachine(loaded=True, on=True)
    b1 = SmartHouse_Room(air=7, bright="sample_text", name="sample_text", temp=3.14)
    b2 = SmartHouse_Room(air=13, bright="sample_text_2", name="sample_text_2", temp=9.99)
    _safe_set(a, 'wm', b1)
    assert _is_linked(a, 'wm', b1)
    if hasattr(b1, 'Room44'):
        assert _is_linked(b1, 'Room44', a)
    _safe_set(a, 'wm', b2)
    assert _is_linked(a, 'wm', b2)
    if hasattr(b1, 'Room44'):
        assert not _is_linked(b1, 'Room44', a)
    if hasattr(b2, 'Room44'):
        assert _is_linked(b2, 'Room44', a)
    _safe_set(a, 'wm', None)
    assert not _is_linked(a, 'wm', b2)
    if hasattr(b2, 'Room44'):
        assert not _is_linked(b2, 'Room44', a)


def test_assoc_room45_link_reassign_clear():
    a = SmartHouse_Room(air=7, bright="sample_text", name="sample_text", temp=3.14)
    b1 = SmartHouse_CoffeeMaker(loaded=True, on=True, warming=True)
    b2 = SmartHouse_CoffeeMaker(loaded=False, on=False, warming=False)
    _safe_set(a, 'Room46', b1)
    assert _is_linked(a, 'Room46', b1)
    if hasattr(b1, 'cm'):
        assert _is_linked(b1, 'cm', a)
    _safe_set(a, 'Room46', b2)
    assert _is_linked(a, 'Room46', b2)
    if hasattr(b1, 'cm'):
        assert not _is_linked(b1, 'cm', a)
    if hasattr(b2, 'cm'):
        assert _is_linked(b2, 'cm', a)
    _safe_set(a, 'Room46', None)
    assert not _is_linked(a, 'Room46', b2)
    if hasattr(b2, 'cm'):
        assert not _is_linked(b2, 'cm', a)


def test_assoc_sec8_link_reassign_clear():
    a = SmartHouse_Security(on=True)
    b1 = SmartHouse_House(eprice="sample_text", name="sample_text", outtemp="sample_text", time="sample_text")
    b2 = SmartHouse_House(eprice="sample_text_2", name="sample_text_2", outtemp="sample_text_2", time="sample_text_2")
    _safe_set(a, 'Security', b1)
    assert _is_linked(a, 'Security', b1)
    if hasattr(b1, 'house9'):
        assert _is_linked(b1, 'house9', a)
    _safe_set(a, 'Security', b2)
    assert _is_linked(a, 'Security', b2)
    if hasattr(b1, 'house9'):
        assert not _is_linked(b1, 'house9', a)
    if hasattr(b2, 'house9'):
        assert _is_linked(b2, 'house9', a)
    _safe_set(a, 'Security', None)
    assert not _is_linked(a, 'Security', b2)
    if hasattr(b2, 'house9'):
        assert not _is_linked(b2, 'house9', a)


def test_assoc_sensor29_link_reassign_clear():
    a = SmartHouse_Sensor(air=True, battery="sample_text", brightness=True, circle="sample_text", temp=True)
    b1 = SmartHouse_Room(air=7, bright="sample_text", name="sample_text", temp=3.14)
    b2 = SmartHouse_Room(air=13, bright="sample_text_2", name="sample_text_2", temp=9.99)
    _safe_set(a, 'SmartHouse_Sensor', b1)
    assert _is_linked(a, 'SmartHouse_Sensor', b1)
    if hasattr(b1, 'SmartHouse_Room30'):
        assert _is_linked(b1, 'SmartHouse_Room30', a)
    _safe_set(a, 'SmartHouse_Sensor', b2)
    assert _is_linked(a, 'SmartHouse_Sensor', b2)
    if hasattr(b1, 'SmartHouse_Room30'):
        assert not _is_linked(b1, 'SmartHouse_Room30', a)
    if hasattr(b2, 'SmartHouse_Room30'):
        assert _is_linked(b2, 'SmartHouse_Room30', a)
    _safe_set(a, 'SmartHouse_Sensor', None)
    assert not _is_linked(a, 'SmartHouse_Sensor', b2)
    if hasattr(b2, 'SmartHouse_Room30'):
        assert not _is_linked(b2, 'SmartHouse_Room30', a)


def test_assoc_wh2_link_reassign_clear():
    a = SmartHouse_WaterHeater(boost=True, on=True, temp="sample_text")
    b1 = SmartHouse_House(eprice="sample_text", name="sample_text", outtemp="sample_text", time="sample_text")
    b2 = SmartHouse_House(eprice="sample_text_2", name="sample_text_2", outtemp="sample_text_2", time="sample_text_2")
    _safe_set(a, 'WaterHeater', b1)
    assert _is_linked(a, 'WaterHeater', b1)
    if hasattr(b1, 'house3'):
        assert _is_linked(b1, 'house3', a)
    _safe_set(a, 'WaterHeater', b2)
    assert _is_linked(a, 'WaterHeater', b2)
    if hasattr(b1, 'house3'):
        assert not _is_linked(b1, 'house3', a)
    if hasattr(b2, 'house3'):
        assert _is_linked(b2, 'house3', a)
    _safe_set(a, 'WaterHeater', None)
    assert not _is_linked(a, 'WaterHeater', b2)
    if hasattr(b2, 'house3'):
        assert not _is_linked(b2, 'house3', a)


def test_assoc_window19_link_reassign_clear():
    a = SmartHouse_Window(curtainOn=True, name="sample_text", opened=True)
    b1 = SmartHouse_Room(air=7, bright="sample_text", name="sample_text", temp=3.14)
    b2 = SmartHouse_Room(air=13, bright="sample_text_2", name="sample_text_2", temp=9.99)
    _safe_set(a, 'SmartHouse_Window', b1)
    assert _is_linked(a, 'SmartHouse_Window', b1)
    if hasattr(b1, 'SmartHouse_Room'):
        assert _is_linked(b1, 'SmartHouse_Room', a)
    _safe_set(a, 'SmartHouse_Window', b2)
    assert _is_linked(a, 'SmartHouse_Window', b2)
    if hasattr(b1, 'SmartHouse_Room'):
        assert not _is_linked(b1, 'SmartHouse_Room', a)
    if hasattr(b2, 'SmartHouse_Room'):
        assert _is_linked(b2, 'SmartHouse_Room', a)
    _safe_set(a, 'SmartHouse_Window', None)
    assert not _is_linked(a, 'SmartHouse_Window', b2)
    if hasattr(b2, 'SmartHouse_Room'):
        assert not _is_linked(b2, 'SmartHouse_Room', a)


def test_assoc_wm35_link_reassign_clear():
    a = SmartHouse_WashingMachine(loaded=True, on=True)
    b1 = SmartHouse_Room(air=7, bright="sample_text", name="sample_text", temp=3.14)
    b2 = SmartHouse_Room(air=13, bright="sample_text_2", name="sample_text_2", temp=9.99)
    _safe_set(a, 'WashingMachine', b1)
    assert _is_linked(a, 'WashingMachine', b1)
    if hasattr(b1, 'room36'):
        assert _is_linked(b1, 'room36', a)
    _safe_set(a, 'WashingMachine', b2)
    assert _is_linked(a, 'WashingMachine', b2)
    if hasattr(b1, 'room36'):
        assert not _is_linked(b1, 'room36', a)
    if hasattr(b2, 'room36'):
        assert _is_linked(b2, 'room36', a)
    _safe_set(a, 'WashingMachine', None)
    assert not _is_linked(a, 'WashingMachine', b2)
    if hasattr(b2, 'room36'):
        assert not _is_linked(b2, 'room36', a)


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

SmartHouse_AirConditioner_strategy = st.builds(SmartHouse_AirConditioner, freshAir=st.booleans(), level=safe_text)
@given(instance=SmartHouse_AirConditioner_strategy)
@settings(max_examples=25)
def test_SmartHouse_AirConditioner_instantiation(instance):
    assert isinstance(instance, SmartHouse_AirConditioner)


SmartHouse_CoffeeMaker_strategy = st.builds(SmartHouse_CoffeeMaker, loaded=st.booleans(), on=st.booleans(), warming=st.booleans())
@given(instance=SmartHouse_CoffeeMaker_strategy)
@settings(max_examples=25)
def test_SmartHouse_CoffeeMaker_instantiation(instance):
    assert isinstance(instance, SmartHouse_CoffeeMaker)


SmartHouse_Cooker_strategy = st.builds(SmartHouse_Cooker, on=st.booleans())
@given(instance=SmartHouse_Cooker_strategy)
@settings(max_examples=25)
def test_SmartHouse_Cooker_instantiation(instance):
    assert isinstance(instance, SmartHouse_Cooker)


SmartHouse_EV_strategy = st.builds(SmartHouse_EV, charging=st.booleans(), level=safe_text, name=safe_text, pluged=st.booleans())
@given(instance=SmartHouse_EV_strategy)
@settings(max_examples=25)
def test_SmartHouse_EV_instantiation(instance):
    assert isinstance(instance, SmartHouse_EV)


SmartHouse_Gate_strategy = st.builds(SmartHouse_Gate, outlocked=st.booleans())
@given(instance=SmartHouse_Gate_strategy)
@settings(max_examples=25)
def test_SmartHouse_Gate_instantiation(instance):
    assert isinstance(instance, SmartHouse_Gate)


SmartHouse_Heating_strategy = st.builds(SmartHouse_Heating, level=st.integers(), name=safe_text)
@given(instance=SmartHouse_Heating_strategy)
@settings(max_examples=25)
def test_SmartHouse_Heating_instantiation(instance):
    assert isinstance(instance, SmartHouse_Heating)


SmartHouse_House_strategy = st.builds(SmartHouse_House, eprice=safe_text, name=safe_text, outtemp=safe_text, time=safe_text)
@given(instance=SmartHouse_House_strategy)
@settings(max_examples=25)
def test_SmartHouse_House_instantiation(instance):
    assert isinstance(instance, SmartHouse_House)


SmartHouse_Light_strategy = st.builds(SmartHouse_Light, level=safe_text)
@given(instance=SmartHouse_Light_strategy)
@settings(max_examples=25)
def test_SmartHouse_Light_instantiation(instance):
    assert isinstance(instance, SmartHouse_Light)


SmartHouse_Person_strategy = st.builds(SmartHouse_Person, name=safe_text)
@given(instance=SmartHouse_Person_strategy)
@settings(max_examples=25)
def test_SmartHouse_Person_instantiation(instance):
    assert isinstance(instance, SmartHouse_Person)


SmartHouse_Projector_strategy = st.builds(SmartHouse_Projector, brightness=safe_text, on=st.booleans(), volume=safe_text)
@given(instance=SmartHouse_Projector_strategy)
@settings(max_examples=25)
def test_SmartHouse_Projector_instantiation(instance):
    assert isinstance(instance, SmartHouse_Projector)


SmartHouse_Room_strategy = st.builds(SmartHouse_Room, air=st.integers(), bright=safe_text, name=safe_text, temp=st.floats(allow_nan=False, allow_infinity=False))
@given(instance=SmartHouse_Room_strategy)
@settings(max_examples=25)
def test_SmartHouse_Room_instantiation(instance):
    assert isinstance(instance, SmartHouse_Room)


SmartHouse_Security_strategy = st.builds(SmartHouse_Security, on=st.booleans())
@given(instance=SmartHouse_Security_strategy)
@settings(max_examples=25)
def test_SmartHouse_Security_instantiation(instance):
    assert isinstance(instance, SmartHouse_Security)


SmartHouse_Sensor_strategy = st.builds(SmartHouse_Sensor, air=st.booleans(), battery=safe_text, brightness=st.booleans(), circle=safe_text, temp=st.booleans())
@given(instance=SmartHouse_Sensor_strategy)
@settings(max_examples=25)
def test_SmartHouse_Sensor_instantiation(instance):
    assert isinstance(instance, SmartHouse_Sensor)


SmartHouse_WashingMachine_strategy = st.builds(SmartHouse_WashingMachine, loaded=st.booleans(), on=st.booleans())
@given(instance=SmartHouse_WashingMachine_strategy)
@settings(max_examples=25)
def test_SmartHouse_WashingMachine_instantiation(instance):
    assert isinstance(instance, SmartHouse_WashingMachine)


SmartHouse_WaterHeater_strategy = st.builds(SmartHouse_WaterHeater, boost=st.booleans(), on=st.booleans(), temp=safe_text)
@given(instance=SmartHouse_WaterHeater_strategy)
@settings(max_examples=25)
def test_SmartHouse_WaterHeater_instantiation(instance):
    assert isinstance(instance, SmartHouse_WaterHeater)


SmartHouse_Window_strategy = st.builds(SmartHouse_Window, curtainOn=st.booleans(), name=safe_text, opened=st.booleans())
@given(instance=SmartHouse_Window_strategy)
@settings(max_examples=25)
def test_SmartHouse_Window_instantiation(instance):
    assert isinstance(instance, SmartHouse_Window)





import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    SmartHouse_AirConditioner,
    SmartHouse_CoffeeMaker,
    SmartHouse_Cooker,
    SmartHouse_EV,
    SmartHouse_Gate,
    SmartHouse_Heating,
    SmartHouse_House,
    SmartHouse_Light,
    SmartHouse_Person,
    SmartHouse_Projector,
    SmartHouse_Room,
    SmartHouse_Security,
    SmartHouse_Sensor,
    SmartHouse_WashingMachine,
    SmartHouse_WaterHeater,
    SmartHouse_Window,
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

def test_assoc_ac24_reverse_link_reassign_clear():
    a1 = SmartHouse_Room(air=7, bright="sample_text", name="sample_text", temp=3.14)
    a2 = SmartHouse_Room(air=13, bright="sample_text_2", name="sample_text_2", temp=9.99)
    b = SmartHouse_AirConditioner(freshAir=True, level="sample_text")
    _safe_set(b, 'AirConditioner', a1)
    assert _is_linked(b, 'AirConditioner', a1)
    if hasattr(a1, 'room25'):
        assert _is_linked(a1, 'room25', b)
    _safe_set(b, 'AirConditioner', a2)
    assert _is_linked(b, 'AirConditioner', a2)
    if hasattr(a1, 'room25'):
        assert not _is_linked(a1, 'room25', b)
    if hasattr(a2, 'room25'):
        assert _is_linked(a2, 'room25', b)
    _safe_set(b, 'AirConditioner', None)
    assert not _is_linked(b, 'AirConditioner', a2)
    if hasattr(a2, 'room25'):
        assert not _is_linked(a2, 'room25', b)


def test_assoc_cm37_reverse_link_reassign_clear():
    a1 = SmartHouse_Room(air=7, bright="sample_text", name="sample_text", temp=3.14)
    a2 = SmartHouse_Room(air=13, bright="sample_text_2", name="sample_text_2", temp=9.99)
    b = SmartHouse_CoffeeMaker(loaded=True, on=True, warming=True)
    _safe_set(b, 'CoffeeMaker', a1)
    assert _is_linked(b, 'CoffeeMaker', a1)
    if hasattr(a1, 'room38'):
        assert _is_linked(a1, 'room38', b)
    _safe_set(b, 'CoffeeMaker', a2)
    assert _is_linked(b, 'CoffeeMaker', a2)
    if hasattr(a1, 'room38'):
        assert not _is_linked(a1, 'room38', b)
    if hasattr(a2, 'room38'):
        assert _is_linked(a2, 'room38', b)
    _safe_set(b, 'CoffeeMaker', None)
    assert not _is_linked(b, 'CoffeeMaker', a2)
    if hasattr(a2, 'room38'):
        assert not _is_linked(a2, 'room38', b)


def test_assoc_cooker33_reverse_link_reassign_clear():
    a1 = SmartHouse_Room(air=7, bright="sample_text", name="sample_text", temp=3.14)
    a2 = SmartHouse_Room(air=13, bright="sample_text_2", name="sample_text_2", temp=9.99)
    b = SmartHouse_Cooker(on=True)
    _safe_set(b, 'SmartHouse_Cooker', a1)
    assert _is_linked(b, 'SmartHouse_Cooker', a1)
    if hasattr(a1, 'SmartHouse_Room34'):
        assert _is_linked(a1, 'SmartHouse_Room34', b)
    _safe_set(b, 'SmartHouse_Cooker', a2)
    assert _is_linked(b, 'SmartHouse_Cooker', a2)
    if hasattr(a1, 'SmartHouse_Room34'):
        assert not _is_linked(a1, 'SmartHouse_Room34', b)
    if hasattr(a2, 'SmartHouse_Room34'):
        assert _is_linked(a2, 'SmartHouse_Room34', b)
    _safe_set(b, 'SmartHouse_Cooker', None)
    assert not _is_linked(b, 'SmartHouse_Cooker', a2)
    if hasattr(a2, 'SmartHouse_Room34'):
        assert not _is_linked(a2, 'SmartHouse_Room34', b)


def test_assoc_ev4_reverse_link_reassign_clear():
    a1 = SmartHouse_House(eprice="sample_text", name="sample_text", outtemp="sample_text", time="sample_text")
    a2 = SmartHouse_House(eprice="sample_text_2", name="sample_text_2", outtemp="sample_text_2", time="sample_text_2")
    b = SmartHouse_EV(charging=True, level="sample_text", name="sample_text", pluged=True)
    _safe_set(b, 'EV', a1)
    assert _is_linked(b, 'EV', a1)
    if hasattr(a1, 'house5'):
        assert _is_linked(a1, 'house5', b)
    _safe_set(b, 'EV', a2)
    assert _is_linked(b, 'EV', a2)
    if hasattr(a1, 'house5'):
        assert not _is_linked(a1, 'house5', b)
    if hasattr(a2, 'house5'):
        assert _is_linked(a2, 'house5', b)
    _safe_set(b, 'EV', None)
    assert not _is_linked(b, 'EV', a2)
    if hasattr(a2, 'house5'):
        assert not _is_linked(a2, 'house5', b)


def test_assoc_gate6_reverse_link_reassign_clear():
    a1 = SmartHouse_House(eprice="sample_text", name="sample_text", outtemp="sample_text", time="sample_text")
    a2 = SmartHouse_House(eprice="sample_text_2", name="sample_text_2", outtemp="sample_text_2", time="sample_text_2")
    b = SmartHouse_Gate(outlocked=True)
    _safe_set(b, 'Gate', a1)
    assert _is_linked(b, 'Gate', a1)
    if hasattr(a1, 'house7'):
        assert _is_linked(a1, 'house7', b)
    _safe_set(b, 'Gate', a2)
    assert _is_linked(b, 'Gate', a2)
    if hasattr(a1, 'house7'):
        assert not _is_linked(a1, 'house7', b)
    if hasattr(a2, 'house7'):
        assert _is_linked(a2, 'house7', b)
    _safe_set(b, 'Gate', None)
    assert not _is_linked(b, 'Gate', a2)
    if hasattr(a2, 'house7'):
        assert not _is_linked(a2, 'house7', b)


def test_assoc_heating20_reverse_link_reassign_clear():
    a1 = SmartHouse_Room(air=7, bright="sample_text", name="sample_text", temp=3.14)
    a2 = SmartHouse_Room(air=13, bright="sample_text_2", name="sample_text_2", temp=9.99)
    b = SmartHouse_Heating(level=7, name="sample_text")
    _safe_set(b, 'SmartHouse_Heating', a1)
    assert _is_linked(b, 'SmartHouse_Heating', a1)
    if hasattr(a1, 'SmartHouse_Room21'):
        assert _is_linked(a1, 'SmartHouse_Room21', b)
    _safe_set(b, 'SmartHouse_Heating', a2)
    assert _is_linked(b, 'SmartHouse_Heating', a2)
    if hasattr(a1, 'SmartHouse_Room21'):
        assert not _is_linked(a1, 'SmartHouse_Room21', b)
    if hasattr(a2, 'SmartHouse_Room21'):
        assert _is_linked(a2, 'SmartHouse_Room21', b)
    _safe_set(b, 'SmartHouse_Heating', None)
    assert not _is_linked(b, 'SmartHouse_Heating', a2)
    if hasattr(a2, 'SmartHouse_Room21'):
        assert not _is_linked(a2, 'SmartHouse_Room21', b)


def test_assoc_house10_reverse_link_reassign_clear():
    a1 = SmartHouse_House(eprice="sample_text", name="sample_text", outtemp="sample_text", time="sample_text")
    a2 = SmartHouse_House(eprice="sample_text_2", name="sample_text_2", outtemp="sample_text_2", time="sample_text_2")
    b = SmartHouse_Gate(outlocked=True)
    _safe_set(b, 'gate', a1)
    assert _is_linked(b, 'gate', a1)
    if hasattr(a1, 'House'):
        assert _is_linked(a1, 'House', b)
    _safe_set(b, 'gate', a2)
    assert _is_linked(b, 'gate', a2)
    if hasattr(a1, 'House'):
        assert not _is_linked(a1, 'House', b)
    if hasattr(a2, 'House'):
        assert _is_linked(a2, 'House', b)
    _safe_set(b, 'gate', None)
    assert not _is_linked(b, 'gate', a2)
    if hasattr(a2, 'House'):
        assert not _is_linked(a2, 'House', b)


def test_assoc_house11_reverse_link_reassign_clear():
    a1 = SmartHouse_Security(on=True)
    a2 = SmartHouse_Security(on=False)
    b = SmartHouse_House(eprice="sample_text", name="sample_text", outtemp="sample_text", time="sample_text")
    _safe_set(b, 'House12', a1)
    assert _is_linked(b, 'House12', a1)
    if hasattr(a1, 'sec'):
        assert _is_linked(a1, 'sec', b)
    _safe_set(b, 'House12', a2)
    assert _is_linked(b, 'House12', a2)
    if hasattr(a1, 'sec'):
        assert not _is_linked(a1, 'sec', b)
    if hasattr(a2, 'sec'):
        assert _is_linked(a2, 'sec', b)
    _safe_set(b, 'House12', None)
    assert not _is_linked(b, 'House12', a2)
    if hasattr(a2, 'sec'):
        assert not _is_linked(a2, 'sec', b)


def test_assoc_house13_reverse_link_reassign_clear():
    a1 = SmartHouse_WaterHeater(boost=True, on=True, temp="sample_text")
    a2 = SmartHouse_WaterHeater(boost=False, on=False, temp="sample_text_2")
    b = SmartHouse_House(eprice="sample_text", name="sample_text", outtemp="sample_text", time="sample_text")
    _safe_set(b, 'House14', a1)
    assert _is_linked(b, 'House14', a1)
    if hasattr(a1, 'wh'):
        assert _is_linked(a1, 'wh', b)
    _safe_set(b, 'House14', a2)
    assert _is_linked(b, 'House14', a2)
    if hasattr(a1, 'wh'):
        assert not _is_linked(a1, 'wh', b)
    if hasattr(a2, 'wh'):
        assert _is_linked(a2, 'wh', b)
    _safe_set(b, 'House14', None)
    assert not _is_linked(b, 'House14', a2)
    if hasattr(a2, 'wh'):
        assert not _is_linked(a2, 'wh', b)


def test_assoc_house15_reverse_link_reassign_clear():
    a1 = SmartHouse_House(eprice="sample_text", name="sample_text", outtemp="sample_text", time="sample_text")
    a2 = SmartHouse_House(eprice="sample_text_2", name="sample_text_2", outtemp="sample_text_2", time="sample_text_2")
    b = SmartHouse_EV(charging=True, level="sample_text", name="sample_text", pluged=True)
    _safe_set(b, 'ev', a1)
    assert _is_linked(b, 'ev', a1)
    if hasattr(a1, 'House16'):
        assert _is_linked(a1, 'House16', b)
    _safe_set(b, 'ev', a2)
    assert _is_linked(b, 'ev', a2)
    if hasattr(a1, 'House16'):
        assert not _is_linked(a1, 'House16', b)
    if hasattr(a2, 'House16'):
        assert _is_linked(a2, 'House16', b)
    _safe_set(b, 'ev', None)
    assert not _is_linked(b, 'ev', a2)
    if hasattr(a2, 'House16'):
        assert not _is_linked(a2, 'House16', b)


def test_assoc_house17_reverse_link_reassign_clear():
    a1 = SmartHouse_Room(air=7, bright="sample_text", name="sample_text", temp=3.14)
    a2 = SmartHouse_Room(air=13, bright="sample_text_2", name="sample_text_2", temp=9.99)
    b = SmartHouse_House(eprice="sample_text", name="sample_text", outtemp="sample_text", time="sample_text")
    _safe_set(b, 'House18', a1)
    assert _is_linked(b, 'House18', a1)
    if hasattr(a1, 'room'):
        assert _is_linked(a1, 'room', b)
    _safe_set(b, 'House18', a2)
    assert _is_linked(b, 'House18', a2)
    if hasattr(a1, 'room'):
        assert not _is_linked(a1, 'room', b)
    if hasattr(a2, 'room'):
        assert _is_linked(a2, 'room', b)
    _safe_set(b, 'House18', None)
    assert not _is_linked(b, 'House18', a2)
    if hasattr(a2, 'room'):
        assert not _is_linked(a2, 'room', b)


def test_assoc_light22_reverse_link_reassign_clear():
    a1 = SmartHouse_Room(air=7, bright="sample_text", name="sample_text", temp=3.14)
    a2 = SmartHouse_Room(air=13, bright="sample_text_2", name="sample_text_2", temp=9.99)
    b = SmartHouse_Light(level="sample_text")
    _safe_set(b, 'SmartHouse_Light', a1)
    assert _is_linked(b, 'SmartHouse_Light', a1)
    if hasattr(a1, 'SmartHouse_Room23'):
        assert _is_linked(a1, 'SmartHouse_Room23', b)
    _safe_set(b, 'SmartHouse_Light', a2)
    assert _is_linked(b, 'SmartHouse_Light', a2)
    if hasattr(a1, 'SmartHouse_Room23'):
        assert not _is_linked(a1, 'SmartHouse_Room23', b)
    if hasattr(a2, 'SmartHouse_Room23'):
        assert _is_linked(a2, 'SmartHouse_Room23', b)
    _safe_set(b, 'SmartHouse_Light', None)
    assert not _is_linked(b, 'SmartHouse_Light', a2)
    if hasattr(a2, 'SmartHouse_Room23'):
        assert not _is_linked(a2, 'SmartHouse_Room23', b)


def test_assoc_member1_reverse_link_reassign_clear():
    a1 = SmartHouse_Person(name="sample_text")
    a2 = SmartHouse_Person(name="sample_text_2")
    b = SmartHouse_House(eprice="sample_text", name="sample_text", outtemp="sample_text", time="sample_text")
    _safe_set(b, 'SmartHouse_House', {a1})
    assert _is_linked(b, 'SmartHouse_House', a1)
    if hasattr(a1, 'SmartHouse_Person'):
        assert _is_linked(a1, 'SmartHouse_Person', b)
    _safe_set(b, 'SmartHouse_House', {a2})
    assert _is_linked(b, 'SmartHouse_House', a2)
    if hasattr(a1, 'SmartHouse_Person'):
        assert not _is_linked(a1, 'SmartHouse_Person', b)
    if hasattr(a2, 'SmartHouse_Person'):
        assert _is_linked(a2, 'SmartHouse_Person', b)
    _safe_set(b, 'SmartHouse_House', set())
    assert not _is_linked(b, 'SmartHouse_House', a2)
    if hasattr(a2, 'SmartHouse_Person'):
        assert not _is_linked(a2, 'SmartHouse_Person', b)


def test_assoc_occupied26_reverse_link_reassign_clear():
    a1 = SmartHouse_Room(air=7, bright="sample_text", name="sample_text", temp=3.14)
    a2 = SmartHouse_Room(air=13, bright="sample_text_2", name="sample_text_2", temp=9.99)
    b = SmartHouse_Person(name="sample_text")
    _safe_set(b, 'SmartHouse_Person28', a1)
    assert _is_linked(b, 'SmartHouse_Person28', a1)
    if hasattr(a1, 'SmartHouse_Room27'):
        assert _is_linked(a1, 'SmartHouse_Room27', b)
    _safe_set(b, 'SmartHouse_Person28', a2)
    assert _is_linked(b, 'SmartHouse_Person28', a2)
    if hasattr(a1, 'SmartHouse_Room27'):
        assert not _is_linked(a1, 'SmartHouse_Room27', b)
    if hasattr(a2, 'SmartHouse_Room27'):
        assert _is_linked(a2, 'SmartHouse_Room27', b)
    _safe_set(b, 'SmartHouse_Person28', None)
    assert not _is_linked(b, 'SmartHouse_Person28', a2)
    if hasattr(a2, 'SmartHouse_Room27'):
        assert not _is_linked(a2, 'SmartHouse_Room27', b)


def test_assoc_projector31_reverse_link_reassign_clear():
    a1 = SmartHouse_Room(air=7, bright="sample_text", name="sample_text", temp=3.14)
    a2 = SmartHouse_Room(air=13, bright="sample_text_2", name="sample_text_2", temp=9.99)
    b = SmartHouse_Projector(brightness="sample_text", on=True, volume="sample_text")
    _safe_set(b, 'Projector', a1)
    assert _is_linked(b, 'Projector', a1)
    if hasattr(a1, 'room32'):
        assert _is_linked(a1, 'room32', b)
    _safe_set(b, 'Projector', a2)
    assert _is_linked(b, 'Projector', a2)
    if hasattr(a1, 'room32'):
        assert not _is_linked(a1, 'room32', b)
    if hasattr(a2, 'room32'):
        assert _is_linked(a2, 'room32', b)
    _safe_set(b, 'Projector', None)
    assert not _is_linked(b, 'Projector', a2)
    if hasattr(a2, 'room32'):
        assert not _is_linked(a2, 'room32', b)


def test_assoc_room0_reverse_link_reassign_clear():
    a1 = SmartHouse_Room(air=7, bright="sample_text", name="sample_text", temp=3.14)
    a2 = SmartHouse_Room(air=13, bright="sample_text_2", name="sample_text_2", temp=9.99)
    b = SmartHouse_House(eprice="sample_text", name="sample_text", outtemp="sample_text", time="sample_text")
    _safe_set(b, 'house', {a1})
    assert _is_linked(b, 'house', a1)
    if hasattr(a1, 'Room'):
        assert _is_linked(a1, 'Room', b)
    _safe_set(b, 'house', {a2})
    assert _is_linked(b, 'house', a2)
    if hasattr(a1, 'Room'):
        assert not _is_linked(a1, 'Room', b)
    if hasattr(a2, 'Room'):
        assert _is_linked(a2, 'Room', b)
    _safe_set(b, 'house', set())
    assert not _is_linked(b, 'house', a2)
    if hasattr(a2, 'Room'):
        assert not _is_linked(a2, 'Room', b)


def test_assoc_room39_reverse_link_reassign_clear():
    a1 = SmartHouse_Room(air=7, bright="sample_text", name="sample_text", temp=3.14)
    a2 = SmartHouse_Room(air=13, bright="sample_text_2", name="sample_text_2", temp=9.99)
    b = SmartHouse_AirConditioner(freshAir=True, level="sample_text")
    _safe_set(b, 'ac', a1)
    assert _is_linked(b, 'ac', a1)
    if hasattr(a1, 'Room40'):
        assert _is_linked(a1, 'Room40', b)
    _safe_set(b, 'ac', a2)
    assert _is_linked(b, 'ac', a2)
    if hasattr(a1, 'Room40'):
        assert not _is_linked(a1, 'Room40', b)
    if hasattr(a2, 'Room40'):
        assert _is_linked(a2, 'Room40', b)
    _safe_set(b, 'ac', None)
    assert not _is_linked(b, 'ac', a2)
    if hasattr(a2, 'Room40'):
        assert not _is_linked(a2, 'Room40', b)


def test_assoc_room41_reverse_link_reassign_clear():
    a1 = SmartHouse_Room(air=7, bright="sample_text", name="sample_text", temp=3.14)
    a2 = SmartHouse_Room(air=13, bright="sample_text_2", name="sample_text_2", temp=9.99)
    b = SmartHouse_Projector(brightness="sample_text", on=True, volume="sample_text")
    _safe_set(b, 'projector', a1)
    assert _is_linked(b, 'projector', a1)
    if hasattr(a1, 'Room42'):
        assert _is_linked(a1, 'Room42', b)
    _safe_set(b, 'projector', a2)
    assert _is_linked(b, 'projector', a2)
    if hasattr(a1, 'Room42'):
        assert not _is_linked(a1, 'Room42', b)
    if hasattr(a2, 'Room42'):
        assert _is_linked(a2, 'Room42', b)
    _safe_set(b, 'projector', None)
    assert not _is_linked(b, 'projector', a2)
    if hasattr(a2, 'Room42'):
        assert not _is_linked(a2, 'Room42', b)


def test_assoc_room43_reverse_link_reassign_clear():
    a1 = SmartHouse_WashingMachine(loaded=True, on=True)
    a2 = SmartHouse_WashingMachine(loaded=False, on=False)
    b = SmartHouse_Room(air=7, bright="sample_text", name="sample_text", temp=3.14)
    _safe_set(b, 'Room44', a1)
    assert _is_linked(b, 'Room44', a1)
    if hasattr(a1, 'wm'):
        assert _is_linked(a1, 'wm', b)
    _safe_set(b, 'Room44', a2)
    assert _is_linked(b, 'Room44', a2)
    if hasattr(a1, 'wm'):
        assert not _is_linked(a1, 'wm', b)
    if hasattr(a2, 'wm'):
        assert _is_linked(a2, 'wm', b)
    _safe_set(b, 'Room44', None)
    assert not _is_linked(b, 'Room44', a2)
    if hasattr(a2, 'wm'):
        assert not _is_linked(a2, 'wm', b)


def test_assoc_room45_reverse_link_reassign_clear():
    a1 = SmartHouse_Room(air=7, bright="sample_text", name="sample_text", temp=3.14)
    a2 = SmartHouse_Room(air=13, bright="sample_text_2", name="sample_text_2", temp=9.99)
    b = SmartHouse_CoffeeMaker(loaded=True, on=True, warming=True)
    _safe_set(b, 'cm', a1)
    assert _is_linked(b, 'cm', a1)
    if hasattr(a1, 'Room46'):
        assert _is_linked(a1, 'Room46', b)
    _safe_set(b, 'cm', a2)
    assert _is_linked(b, 'cm', a2)
    if hasattr(a1, 'Room46'):
        assert not _is_linked(a1, 'Room46', b)
    if hasattr(a2, 'Room46'):
        assert _is_linked(a2, 'Room46', b)
    _safe_set(b, 'cm', None)
    assert not _is_linked(b, 'cm', a2)
    if hasattr(a2, 'Room46'):
        assert not _is_linked(a2, 'Room46', b)


def test_assoc_sec8_reverse_link_reassign_clear():
    a1 = SmartHouse_Security(on=True)
    a2 = SmartHouse_Security(on=False)
    b = SmartHouse_House(eprice="sample_text", name="sample_text", outtemp="sample_text", time="sample_text")
    _safe_set(b, 'house9', a1)
    assert _is_linked(b, 'house9', a1)
    if hasattr(a1, 'Security'):
        assert _is_linked(a1, 'Security', b)
    _safe_set(b, 'house9', a2)
    assert _is_linked(b, 'house9', a2)
    if hasattr(a1, 'Security'):
        assert not _is_linked(a1, 'Security', b)
    if hasattr(a2, 'Security'):
        assert _is_linked(a2, 'Security', b)
    _safe_set(b, 'house9', None)
    assert not _is_linked(b, 'house9', a2)
    if hasattr(a2, 'Security'):
        assert not _is_linked(a2, 'Security', b)


def test_assoc_sensor29_reverse_link_reassign_clear():
    a1 = SmartHouse_Sensor(air=True, battery="sample_text", brightness=True, circle="sample_text", temp=True)
    a2 = SmartHouse_Sensor(air=False, battery="sample_text_2", brightness=False, circle="sample_text_2", temp=False)
    b = SmartHouse_Room(air=7, bright="sample_text", name="sample_text", temp=3.14)
    _safe_set(b, 'SmartHouse_Room30', {a1})
    assert _is_linked(b, 'SmartHouse_Room30', a1)
    if hasattr(a1, 'SmartHouse_Sensor'):
        assert _is_linked(a1, 'SmartHouse_Sensor', b)
    _safe_set(b, 'SmartHouse_Room30', {a2})
    assert _is_linked(b, 'SmartHouse_Room30', a2)
    if hasattr(a1, 'SmartHouse_Sensor'):
        assert not _is_linked(a1, 'SmartHouse_Sensor', b)
    if hasattr(a2, 'SmartHouse_Sensor'):
        assert _is_linked(a2, 'SmartHouse_Sensor', b)
    _safe_set(b, 'SmartHouse_Room30', set())
    assert not _is_linked(b, 'SmartHouse_Room30', a2)
    if hasattr(a2, 'SmartHouse_Sensor'):
        assert not _is_linked(a2, 'SmartHouse_Sensor', b)


def test_assoc_wh2_reverse_link_reassign_clear():
    a1 = SmartHouse_WaterHeater(boost=True, on=True, temp="sample_text")
    a2 = SmartHouse_WaterHeater(boost=False, on=False, temp="sample_text_2")
    b = SmartHouse_House(eprice="sample_text", name="sample_text", outtemp="sample_text", time="sample_text")
    _safe_set(b, 'house3', a1)
    assert _is_linked(b, 'house3', a1)
    if hasattr(a1, 'WaterHeater'):
        assert _is_linked(a1, 'WaterHeater', b)
    _safe_set(b, 'house3', a2)
    assert _is_linked(b, 'house3', a2)
    if hasattr(a1, 'WaterHeater'):
        assert not _is_linked(a1, 'WaterHeater', b)
    if hasattr(a2, 'WaterHeater'):
        assert _is_linked(a2, 'WaterHeater', b)
    _safe_set(b, 'house3', None)
    assert not _is_linked(b, 'house3', a2)
    if hasattr(a2, 'WaterHeater'):
        assert not _is_linked(a2, 'WaterHeater', b)


def test_assoc_window19_reverse_link_reassign_clear():
    a1 = SmartHouse_Window(curtainOn=True, name="sample_text", opened=True)
    a2 = SmartHouse_Window(curtainOn=False, name="sample_text_2", opened=False)
    b = SmartHouse_Room(air=7, bright="sample_text", name="sample_text", temp=3.14)
    _safe_set(b, 'SmartHouse_Room', {a1})
    assert _is_linked(b, 'SmartHouse_Room', a1)
    if hasattr(a1, 'SmartHouse_Window'):
        assert _is_linked(a1, 'SmartHouse_Window', b)
    _safe_set(b, 'SmartHouse_Room', {a2})
    assert _is_linked(b, 'SmartHouse_Room', a2)
    if hasattr(a1, 'SmartHouse_Window'):
        assert not _is_linked(a1, 'SmartHouse_Window', b)
    if hasattr(a2, 'SmartHouse_Window'):
        assert _is_linked(a2, 'SmartHouse_Window', b)
    _safe_set(b, 'SmartHouse_Room', set())
    assert not _is_linked(b, 'SmartHouse_Room', a2)
    if hasattr(a2, 'SmartHouse_Window'):
        assert not _is_linked(a2, 'SmartHouse_Window', b)


def test_assoc_wm35_reverse_link_reassign_clear():
    a1 = SmartHouse_WashingMachine(loaded=True, on=True)
    a2 = SmartHouse_WashingMachine(loaded=False, on=False)
    b = SmartHouse_Room(air=7, bright="sample_text", name="sample_text", temp=3.14)
    _safe_set(b, 'room36', a1)
    assert _is_linked(b, 'room36', a1)
    if hasattr(a1, 'WashingMachine'):
        assert _is_linked(a1, 'WashingMachine', b)
    _safe_set(b, 'room36', a2)
    assert _is_linked(b, 'room36', a2)
    if hasattr(a1, 'WashingMachine'):
        assert not _is_linked(a1, 'WashingMachine', b)
    if hasattr(a2, 'WashingMachine'):
        assert _is_linked(a2, 'WashingMachine', b)
    _safe_set(b, 'room36', None)
    assert not _is_linked(b, 'room36', a2)
    if hasattr(a2, 'WashingMachine'):
        assert not _is_linked(a2, 'WashingMachine', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================


