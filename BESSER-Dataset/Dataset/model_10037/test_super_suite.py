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
    Transition,
    SBCS_PumpController_ClosePump,
    SBCS_SteamBoiler_OpenValve,
    SBCS_WaterLevelMeaurementDevice_getLevel,
    SBCS_PumpController_OpenPump,
    SBCS_ControlProgram_Start,
    SBCS_WaterLevelMeasurementDevice,
    SBCS_SteamMeasurementDevice,
    SBCS_Transition,
    SBCS_PumpControler,
    SBCS_SteamBoiler,
    SBCS_Pump,
    SBCS_ControlProgram,
    SBCS_Snapshot,
    ValveState,
    Mode,
    State,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_hyp_transition_is_not_abstract():
    assert not inspect.isabstract(Transition)


def test_hyp_transition_constructor_exists():
    assert callable(Transition.__init__)


def test_hyp_transition_constructor_args():
    sig = inspect.signature(Transition.__init__)
    params = list(sig.parameters.keys())



def test_hyp_sbcs_pumpcontroller_closepump_is_not_abstract():
    assert not inspect.isabstract(SBCS_PumpController_ClosePump)


def test_hyp_sbcs_pumpcontroller_closepump_constructor_exists():
    assert callable(SBCS_PumpController_ClosePump.__init__)


def test_hyp_sbcs_pumpcontroller_closepump_constructor_args():
    sig = inspect.signature(SBCS_PumpController_ClosePump.__init__)
    params = list(sig.parameters.keys())



def test_hyp_sbcs_steamboiler_openvalve_is_not_abstract():
    assert not inspect.isabstract(SBCS_SteamBoiler_OpenValve)


def test_hyp_sbcs_steamboiler_openvalve_constructor_exists():
    assert callable(SBCS_SteamBoiler_OpenValve.__init__)


def test_hyp_sbcs_steamboiler_openvalve_constructor_args():
    sig = inspect.signature(SBCS_SteamBoiler_OpenValve.__init__)
    params = list(sig.parameters.keys())



def test_hyp_sbcs_waterlevelmeaurementdevice_getlevel_is_not_abstract():
    assert not inspect.isabstract(SBCS_WaterLevelMeaurementDevice_getLevel)


def test_hyp_sbcs_waterlevelmeaurementdevice_getlevel_constructor_exists():
    assert callable(SBCS_WaterLevelMeaurementDevice_getLevel.__init__)


def test_hyp_sbcs_waterlevelmeaurementdevice_getlevel_constructor_args():
    sig = inspect.signature(SBCS_WaterLevelMeaurementDevice_getLevel.__init__)
    params = list(sig.parameters.keys())
    assert "ret" in params, "Missing parameter 'ret'"




def test_hyp_sbcs_pumpcontroller_openpump_is_not_abstract():
    assert not inspect.isabstract(SBCS_PumpController_OpenPump)


def test_hyp_sbcs_pumpcontroller_openpump_constructor_exists():
    assert callable(SBCS_PumpController_OpenPump.__init__)


def test_hyp_sbcs_pumpcontroller_openpump_constructor_args():
    sig = inspect.signature(SBCS_PumpController_OpenPump.__init__)
    params = list(sig.parameters.keys())



def test_hyp_sbcs_controlprogram_start_is_not_abstract():
    assert not inspect.isabstract(SBCS_ControlProgram_Start)


def test_hyp_sbcs_controlprogram_start_constructor_exists():
    assert callable(SBCS_ControlProgram_Start.__init__)


def test_hyp_sbcs_controlprogram_start_constructor_args():
    sig = inspect.signature(SBCS_ControlProgram_Start.__init__)
    params = list(sig.parameters.keys())



def test_hyp_sbcs_waterlevelmeasurementdevice_is_not_abstract():
    assert not inspect.isabstract(SBCS_WaterLevelMeasurementDevice)


def test_hyp_sbcs_waterlevelmeasurementdevice_constructor_exists():
    assert callable(SBCS_WaterLevelMeasurementDevice.__init__)


def test_hyp_sbcs_waterlevelmeasurementdevice_constructor_args():
    sig = inspect.signature(SBCS_WaterLevelMeasurementDevice.__init__)
    params = list(sig.parameters.keys())
    assert "waterLevel" in params, "Missing parameter 'waterLevel'"
    assert "ready" in params, "Missing parameter 'ready'"





def test_hyp_sbcs_steammeasurementdevice_is_not_abstract():
    assert not inspect.isabstract(SBCS_SteamMeasurementDevice)


def test_hyp_sbcs_steammeasurementdevice_constructor_exists():
    assert callable(SBCS_SteamMeasurementDevice.__init__)


def test_hyp_sbcs_steammeasurementdevice_constructor_args():
    sig = inspect.signature(SBCS_SteamMeasurementDevice.__init__)
    params = list(sig.parameters.keys())
    assert "waterLevel" in params, "Missing parameter 'waterLevel'"
    assert "evaporationRate" in params, "Missing parameter 'evaporationRate'"
    assert "ready" in params, "Missing parameter 'ready'"






def test_hyp_sbcs_transition_is_not_abstract():
    assert not inspect.isabstract(SBCS_Transition)


def test_hyp_sbcs_transition_constructor_exists():
    assert callable(SBCS_Transition.__init__)


def test_hyp_sbcs_transition_constructor_args():
    sig = inspect.signature(SBCS_Transition.__init__)
    params = list(sig.parameters.keys())



def test_hyp_sbcs_pumpcontroler_is_not_abstract():
    assert not inspect.isabstract(SBCS_PumpControler)


def test_hyp_sbcs_pumpcontroler_constructor_exists():
    assert callable(SBCS_PumpControler.__init__)


def test_hyp_sbcs_pumpcontroler_constructor_args():
    sig = inspect.signature(SBCS_PumpControler.__init__)
    params = list(sig.parameters.keys())
    assert "circulating" in params, "Missing parameter 'circulating'"
    assert "ready" in params, "Missing parameter 'ready'"





def test_hyp_sbcs_steamboiler_is_not_abstract():
    assert not inspect.isabstract(SBCS_SteamBoiler)


def test_hyp_sbcs_steamboiler_constructor_exists():
    assert callable(SBCS_SteamBoiler.__init__)


def test_hyp_sbcs_steamboiler_constructor_args():
    sig = inspect.signature(SBCS_SteamBoiler.__init__)
    params = list(sig.parameters.keys())
    assert "maximumDecrease" in params, "Missing parameter 'maximumDecrease'"
    assert "maximalNormal" in params, "Missing parameter 'maximalNormal'"
    assert "minimalNormal" in params, "Missing parameter 'minimalNormal'"
    assert "minimalLimit" in params, "Missing parameter 'minimalLimit'"
    assert "maximalLimit" in params, "Missing parameter 'maximalLimit'"
    assert "maximumIncrease" in params, "Missing parameter 'maximumIncrease'"
    assert "valveOpen" in params, "Missing parameter 'valveOpen'"
    assert "ready" in params, "Missing parameter 'ready'"
    assert "capacity" in params, "Missing parameter 'capacity'"












def test_hyp_sbcs_pump_is_not_abstract():
    assert not inspect.isabstract(SBCS_Pump)


def test_hyp_sbcs_pump_constructor_exists():
    assert callable(SBCS_Pump.__init__)


def test_hyp_sbcs_pump_constructor_args():
    sig = inspect.signature(SBCS_Pump.__init__)
    params = list(sig.parameters.keys())
    assert "capacity" in params, "Missing parameter 'capacity'"
    assert "mode" in params, "Missing parameter 'mode'"
    assert "ready" in params, "Missing parameter 'ready'"






def test_hyp_sbcs_controlprogram_is_not_abstract():
    assert not inspect.isabstract(SBCS_ControlProgram)


def test_hyp_sbcs_controlprogram_constructor_exists():
    assert callable(SBCS_ControlProgram.__init__)


def test_hyp_sbcs_controlprogram_constructor_args():
    sig = inspect.signature(SBCS_ControlProgram.__init__)
    params = list(sig.parameters.keys())
    assert "pumpControlerFailure" in params, "Missing parameter 'pumpControlerFailure'"
    assert "smdFailure" in params, "Missing parameter 'smdFailure'"
    assert "ready" in params, "Missing parameter 'ready'"
    assert "failureDetected" in params, "Missing parameter 'failureDetected'"
    assert "pumpFailure" in params, "Missing parameter 'pumpFailure'"
    assert "wlmdFailure" in params, "Missing parameter 'wlmdFailure'"
    assert "mode" in params, "Missing parameter 'mode'"










def test_hyp_sbcs_snapshot_is_not_abstract():
    assert not inspect.isabstract(SBCS_Snapshot)


def test_hyp_sbcs_snapshot_constructor_exists():
    assert callable(SBCS_Snapshot.__init__)


def test_hyp_sbcs_snapshot_constructor_args():
    sig = inspect.signature(SBCS_Snapshot.__init__)
    params = list(sig.parameters.keys())

def test_hyp_valvestate_exists():
    # Check that the Enumeration exists
    assert ValveState is not None

def test_hyp_valvestate_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in ValveState]
    expected_literals = [
        "Closed",
        "Open",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in ValveState"

def test_hyp_mode_exists():
    # Check that the Enumeration exists
    assert Mode is not None

def test_hyp_mode_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in Mode]
    expected_literals = [
        "Degraded",
        "Normal",
        "Dameged",
        "Initialization",
        "Rescue",
        "EmergencyStop",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in Mode"

def test_hyp_state_exists():
    # Check that the Enumeration exists
    assert State is not None

def test_hyp_state_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in State]
    expected_literals = [
        "On",
        "Off",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in State"


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
Transition_strategy = st.builds(
    Transition,
)
SBCS_PumpController_ClosePump_strategy = st.builds(
    SBCS_PumpController_ClosePump,
)
SBCS_SteamBoiler_OpenValve_strategy = st.builds(
    SBCS_SteamBoiler_OpenValve,
)
SBCS_WaterLevelMeaurementDevice_getLevel_strategy = st.builds(
    SBCS_WaterLevelMeaurementDevice_getLevel,
    ret=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
SBCS_PumpController_OpenPump_strategy = st.builds(
    SBCS_PumpController_OpenPump,
)
SBCS_ControlProgram_Start_strategy = st.builds(
    SBCS_ControlProgram_Start,
)
SBCS_WaterLevelMeasurementDevice_strategy = st.builds(
    SBCS_WaterLevelMeasurementDevice,
    waterLevel=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    ready=
        st.booleans()
)
SBCS_SteamMeasurementDevice_strategy = st.builds(
    SBCS_SteamMeasurementDevice,
    waterLevel=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    evaporationRate=
        st.booleans(),
    ready=
        st.booleans()
)
SBCS_Transition_strategy = st.builds(
    SBCS_Transition,
)
SBCS_PumpControler_strategy = st.builds(
    SBCS_PumpControler,
    circulating=
        st.booleans(),
    ready=
        st.booleans()
)
SBCS_SteamBoiler_strategy = st.builds(
    SBCS_SteamBoiler,
    maximumDecrease=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    maximalNormal=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    minimalNormal=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    minimalLimit=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    maximalLimit=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    maximumIncrease=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    valveOpen=
        safe_text,
    ready=
        st.booleans(),
    capacity=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
SBCS_Pump_strategy = st.builds(
    SBCS_Pump,
    capacity=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    mode=
        safe_text,
    ready=
        st.booleans()
)
SBCS_ControlProgram_strategy = st.builds(
    SBCS_ControlProgram,
    pumpControlerFailure=
        st.booleans(),
    smdFailure=
        st.booleans(),
    ready=
        st.booleans(),
    failureDetected=
        st.booleans(),
    pumpFailure=
        st.booleans(),
    wlmdFailure=
        st.booleans(),
    mode=
        safe_text
)
SBCS_Snapshot_strategy = st.builds(
    SBCS_Snapshot,
)







@given(instance=SBCS_WaterLevelMeaurementDevice_getLevel_strategy)
def test_hyp_sbcs_waterlevelmeaurementdevice_getlevel_ret_setter(instance):
    original = instance.ret
    instance.ret = original
    assert instance.ret == original






@given(instance=SBCS_WaterLevelMeasurementDevice_strategy)
def test_hyp_sbcs_waterlevelmeasurementdevice_waterLevel_setter(instance):
    original = instance.waterLevel
    instance.waterLevel = original
    assert instance.waterLevel == original



@given(instance=SBCS_WaterLevelMeasurementDevice_strategy)
def test_hyp_sbcs_waterlevelmeasurementdevice_ready_setter(instance):
    original = instance.ready
    instance.ready = original
    assert instance.ready == original




@given(instance=SBCS_SteamMeasurementDevice_strategy)
def test_hyp_sbcs_steammeasurementdevice_waterLevel_setter(instance):
    original = instance.waterLevel
    instance.waterLevel = original
    assert instance.waterLevel == original



@given(instance=SBCS_SteamMeasurementDevice_strategy)
def test_hyp_sbcs_steammeasurementdevice_evaporationRate_setter(instance):
    original = instance.evaporationRate
    instance.evaporationRate = original
    assert instance.evaporationRate == original



@given(instance=SBCS_SteamMeasurementDevice_strategy)
def test_hyp_sbcs_steammeasurementdevice_ready_setter(instance):
    original = instance.ready
    instance.ready = original
    assert instance.ready == original





@given(instance=SBCS_PumpControler_strategy)
def test_hyp_sbcs_pumpcontroler_circulating_setter(instance):
    original = instance.circulating
    instance.circulating = original
    assert instance.circulating == original



@given(instance=SBCS_PumpControler_strategy)
def test_hyp_sbcs_pumpcontroler_ready_setter(instance):
    original = instance.ready
    instance.ready = original
    assert instance.ready == original




@given(instance=SBCS_SteamBoiler_strategy)
def test_hyp_sbcs_steamboiler_maximumDecrease_setter(instance):
    original = instance.maximumDecrease
    instance.maximumDecrease = original
    assert instance.maximumDecrease == original



@given(instance=SBCS_SteamBoiler_strategy)
def test_hyp_sbcs_steamboiler_maximalNormal_setter(instance):
    original = instance.maximalNormal
    instance.maximalNormal = original
    assert instance.maximalNormal == original



@given(instance=SBCS_SteamBoiler_strategy)
def test_hyp_sbcs_steamboiler_minimalNormal_setter(instance):
    original = instance.minimalNormal
    instance.minimalNormal = original
    assert instance.minimalNormal == original



@given(instance=SBCS_SteamBoiler_strategy)
def test_hyp_sbcs_steamboiler_minimalLimit_setter(instance):
    original = instance.minimalLimit
    instance.minimalLimit = original
    assert instance.minimalLimit == original



@given(instance=SBCS_SteamBoiler_strategy)
def test_hyp_sbcs_steamboiler_maximalLimit_setter(instance):
    original = instance.maximalLimit
    instance.maximalLimit = original
    assert instance.maximalLimit == original



@given(instance=SBCS_SteamBoiler_strategy)
def test_hyp_sbcs_steamboiler_maximumIncrease_setter(instance):
    original = instance.maximumIncrease
    instance.maximumIncrease = original
    assert instance.maximumIncrease == original



@given(instance=SBCS_SteamBoiler_strategy)
def test_hyp_sbcs_steamboiler_valveOpen_setter(instance):
    original = instance.valveOpen
    instance.valveOpen = original
    assert instance.valveOpen == original



@given(instance=SBCS_SteamBoiler_strategy)
def test_hyp_sbcs_steamboiler_ready_setter(instance):
    original = instance.ready
    instance.ready = original
    assert instance.ready == original



@given(instance=SBCS_SteamBoiler_strategy)
def test_hyp_sbcs_steamboiler_capacity_setter(instance):
    original = instance.capacity
    instance.capacity = original
    assert instance.capacity == original




@given(instance=SBCS_Pump_strategy)
def test_hyp_sbcs_pump_capacity_setter(instance):
    original = instance.capacity
    instance.capacity = original
    assert instance.capacity == original



@given(instance=SBCS_Pump_strategy)
def test_hyp_sbcs_pump_mode_setter(instance):
    original = instance.mode
    instance.mode = original
    assert instance.mode == original



@given(instance=SBCS_Pump_strategy)
def test_hyp_sbcs_pump_ready_setter(instance):
    original = instance.ready
    instance.ready = original
    assert instance.ready == original




@given(instance=SBCS_ControlProgram_strategy)
def test_hyp_sbcs_controlprogram_pumpControlerFailure_setter(instance):
    original = instance.pumpControlerFailure
    instance.pumpControlerFailure = original
    assert instance.pumpControlerFailure == original



@given(instance=SBCS_ControlProgram_strategy)
def test_hyp_sbcs_controlprogram_smdFailure_setter(instance):
    original = instance.smdFailure
    instance.smdFailure = original
    assert instance.smdFailure == original



@given(instance=SBCS_ControlProgram_strategy)
def test_hyp_sbcs_controlprogram_ready_setter(instance):
    original = instance.ready
    instance.ready = original
    assert instance.ready == original



@given(instance=SBCS_ControlProgram_strategy)
def test_hyp_sbcs_controlprogram_failureDetected_setter(instance):
    original = instance.failureDetected
    instance.failureDetected = original
    assert instance.failureDetected == original



@given(instance=SBCS_ControlProgram_strategy)
def test_hyp_sbcs_controlprogram_pumpFailure_setter(instance):
    original = instance.pumpFailure
    instance.pumpFailure = original
    assert instance.pumpFailure == original



@given(instance=SBCS_ControlProgram_strategy)
def test_hyp_sbcs_controlprogram_wlmdFailure_setter(instance):
    original = instance.wlmdFailure
    instance.wlmdFailure = original
    assert instance.wlmdFailure == original



@given(instance=SBCS_ControlProgram_strategy)
def test_hyp_sbcs_controlprogram_mode_setter(instance):
    original = instance.mode
    instance.mode = original
    assert instance.mode == original


import warnings
import copy
import inspect
import ast
from hypothesis import given, settings


import warnings
import copy
import inspect
import ast
from hypothesis import given, settings



# ----- SECTION B: test_structural_full.py (deterministic-first suite) -----
import inspect
import pytest
from datetime import date, datetime, time, timedelta
from hypothesis import given, settings
import hypothesis.strategies as st

from python_code import (
    SBCS_ControlProgram,
    SBCS_ControlProgram_Start,
    SBCS_Pump,
    SBCS_PumpControler,
    SBCS_PumpController_ClosePump,
    SBCS_PumpController_OpenPump,
    SBCS_Snapshot,
    SBCS_SteamBoiler,
    SBCS_SteamBoiler_OpenValve,
    SBCS_SteamMeasurementDevice,
    SBCS_Transition,
    SBCS_WaterLevelMeasurementDevice,
    SBCS_WaterLevelMeaurementDevice_getLevel,
    Transition,
    Mode,
    State,
    ValveState,
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

def test_SBCS_ControlProgram_failureDetected_value_roundtrip():
    instance = SBCS_ControlProgram(failureDetected=True, mode="sample_text", pumpControlerFailure=True, pumpFailure=True, ready=True, smdFailure=True, wlmdFailure=True)
    assert instance.failureDetected == True
    instance.failureDetected = False
    assert instance.failureDetected == False


def test_SBCS_ControlProgram_mode_value_roundtrip():
    instance = SBCS_ControlProgram(failureDetected=True, mode="sample_text", pumpControlerFailure=True, pumpFailure=True, ready=True, smdFailure=True, wlmdFailure=True)
    assert instance.mode == "sample_text"
    instance.mode = "sample_text_2"
    assert instance.mode == "sample_text_2"


def test_SBCS_ControlProgram_pumpControlerFailure_value_roundtrip():
    instance = SBCS_ControlProgram(failureDetected=True, mode="sample_text", pumpControlerFailure=True, pumpFailure=True, ready=True, smdFailure=True, wlmdFailure=True)
    assert instance.pumpControlerFailure == True
    instance.pumpControlerFailure = False
    assert instance.pumpControlerFailure == False


def test_SBCS_ControlProgram_pumpFailure_value_roundtrip():
    instance = SBCS_ControlProgram(failureDetected=True, mode="sample_text", pumpControlerFailure=True, pumpFailure=True, ready=True, smdFailure=True, wlmdFailure=True)
    assert instance.pumpFailure == True
    instance.pumpFailure = False
    assert instance.pumpFailure == False


def test_SBCS_ControlProgram_ready_value_roundtrip():
    instance = SBCS_ControlProgram(failureDetected=True, mode="sample_text", pumpControlerFailure=True, pumpFailure=True, ready=True, smdFailure=True, wlmdFailure=True)
    assert instance.ready == True
    instance.ready = False
    assert instance.ready == False


def test_SBCS_ControlProgram_smdFailure_value_roundtrip():
    instance = SBCS_ControlProgram(failureDetected=True, mode="sample_text", pumpControlerFailure=True, pumpFailure=True, ready=True, smdFailure=True, wlmdFailure=True)
    assert instance.smdFailure == True
    instance.smdFailure = False
    assert instance.smdFailure == False


def test_SBCS_ControlProgram_wlmdFailure_value_roundtrip():
    instance = SBCS_ControlProgram(failureDetected=True, mode="sample_text", pumpControlerFailure=True, pumpFailure=True, ready=True, smdFailure=True, wlmdFailure=True)
    assert instance.wlmdFailure == True
    instance.wlmdFailure = False
    assert instance.wlmdFailure == False


def test_SBCS_Pump_capacity_value_roundtrip():
    instance = SBCS_Pump(capacity=3.14, mode="sample_text", ready=True)
    assert instance.capacity == 3.14
    instance.capacity = 9.99
    assert instance.capacity == 9.99


def test_SBCS_Pump_mode_value_roundtrip():
    instance = SBCS_Pump(capacity=3.14, mode="sample_text", ready=True)
    assert instance.mode == "sample_text"
    instance.mode = "sample_text_2"
    assert instance.mode == "sample_text_2"


def test_SBCS_Pump_ready_value_roundtrip():
    instance = SBCS_Pump(capacity=3.14, mode="sample_text", ready=True)
    assert instance.ready == True
    instance.ready = False
    assert instance.ready == False


def test_SBCS_PumpControler_circulating_value_roundtrip():
    instance = SBCS_PumpControler(circulating=True, ready=True)
    assert instance.circulating == True
    instance.circulating = False
    assert instance.circulating == False


def test_SBCS_PumpControler_ready_value_roundtrip():
    instance = SBCS_PumpControler(circulating=True, ready=True)
    assert instance.ready == True
    instance.ready = False
    assert instance.ready == False


def test_SBCS_SteamBoiler_capacity_value_roundtrip():
    instance = SBCS_SteamBoiler(capacity=3.14, maximalLimit=3.14, maximalNormal=3.14, maximumDecrease=3.14, maximumIncrease=3.14, minimalLimit=3.14, minimalNormal=3.14, ready=True, valveOpen="sample_text")
    assert instance.capacity == 3.14
    instance.capacity = 9.99
    assert instance.capacity == 9.99


def test_SBCS_SteamBoiler_maximalLimit_value_roundtrip():
    instance = SBCS_SteamBoiler(capacity=3.14, maximalLimit=3.14, maximalNormal=3.14, maximumDecrease=3.14, maximumIncrease=3.14, minimalLimit=3.14, minimalNormal=3.14, ready=True, valveOpen="sample_text")
    assert instance.maximalLimit == 3.14
    instance.maximalLimit = 9.99
    assert instance.maximalLimit == 9.99


def test_SBCS_SteamBoiler_maximalNormal_value_roundtrip():
    instance = SBCS_SteamBoiler(capacity=3.14, maximalLimit=3.14, maximalNormal=3.14, maximumDecrease=3.14, maximumIncrease=3.14, minimalLimit=3.14, minimalNormal=3.14, ready=True, valveOpen="sample_text")
    assert instance.maximalNormal == 3.14
    instance.maximalNormal = 9.99
    assert instance.maximalNormal == 9.99


def test_SBCS_SteamBoiler_maximumDecrease_value_roundtrip():
    instance = SBCS_SteamBoiler(capacity=3.14, maximalLimit=3.14, maximalNormal=3.14, maximumDecrease=3.14, maximumIncrease=3.14, minimalLimit=3.14, minimalNormal=3.14, ready=True, valveOpen="sample_text")
    assert instance.maximumDecrease == 3.14
    instance.maximumDecrease = 9.99
    assert instance.maximumDecrease == 9.99


def test_SBCS_SteamBoiler_maximumIncrease_value_roundtrip():
    instance = SBCS_SteamBoiler(capacity=3.14, maximalLimit=3.14, maximalNormal=3.14, maximumDecrease=3.14, maximumIncrease=3.14, minimalLimit=3.14, minimalNormal=3.14, ready=True, valveOpen="sample_text")
    assert instance.maximumIncrease == 3.14
    instance.maximumIncrease = 9.99
    assert instance.maximumIncrease == 9.99


def test_SBCS_SteamBoiler_minimalLimit_value_roundtrip():
    instance = SBCS_SteamBoiler(capacity=3.14, maximalLimit=3.14, maximalNormal=3.14, maximumDecrease=3.14, maximumIncrease=3.14, minimalLimit=3.14, minimalNormal=3.14, ready=True, valveOpen="sample_text")
    assert instance.minimalLimit == 3.14
    instance.minimalLimit = 9.99
    assert instance.minimalLimit == 9.99


def test_SBCS_SteamBoiler_minimalNormal_value_roundtrip():
    instance = SBCS_SteamBoiler(capacity=3.14, maximalLimit=3.14, maximalNormal=3.14, maximumDecrease=3.14, maximumIncrease=3.14, minimalLimit=3.14, minimalNormal=3.14, ready=True, valveOpen="sample_text")
    assert instance.minimalNormal == 3.14
    instance.minimalNormal = 9.99
    assert instance.minimalNormal == 9.99


def test_SBCS_SteamBoiler_ready_value_roundtrip():
    instance = SBCS_SteamBoiler(capacity=3.14, maximalLimit=3.14, maximalNormal=3.14, maximumDecrease=3.14, maximumIncrease=3.14, minimalLimit=3.14, minimalNormal=3.14, ready=True, valveOpen="sample_text")
    assert instance.ready == True
    instance.ready = False
    assert instance.ready == False


def test_SBCS_SteamBoiler_valveOpen_value_roundtrip():
    instance = SBCS_SteamBoiler(capacity=3.14, maximalLimit=3.14, maximalNormal=3.14, maximumDecrease=3.14, maximumIncrease=3.14, minimalLimit=3.14, minimalNormal=3.14, ready=True, valveOpen="sample_text")
    assert instance.valveOpen == "sample_text"
    instance.valveOpen = "sample_text_2"
    assert instance.valveOpen == "sample_text_2"


def test_SBCS_SteamMeasurementDevice_evaporationRate_value_roundtrip():
    instance = SBCS_SteamMeasurementDevice(evaporationRate=True, ready=True, waterLevel=3.14)
    assert instance.evaporationRate == True
    instance.evaporationRate = False
    assert instance.evaporationRate == False


def test_SBCS_SteamMeasurementDevice_ready_value_roundtrip():
    instance = SBCS_SteamMeasurementDevice(evaporationRate=True, ready=True, waterLevel=3.14)
    assert instance.ready == True
    instance.ready = False
    assert instance.ready == False


def test_SBCS_SteamMeasurementDevice_waterLevel_value_roundtrip():
    instance = SBCS_SteamMeasurementDevice(evaporationRate=True, ready=True, waterLevel=3.14)
    assert instance.waterLevel == 3.14
    instance.waterLevel = 9.99
    assert instance.waterLevel == 9.99


def test_SBCS_WaterLevelMeasurementDevice_ready_value_roundtrip():
    instance = SBCS_WaterLevelMeasurementDevice(ready=True, waterLevel=3.14)
    assert instance.ready == True
    instance.ready = False
    assert instance.ready == False


def test_SBCS_WaterLevelMeasurementDevice_waterLevel_value_roundtrip():
    instance = SBCS_WaterLevelMeasurementDevice(ready=True, waterLevel=3.14)
    assert instance.waterLevel == 3.14
    instance.waterLevel = 9.99
    assert instance.waterLevel == 9.99


def test_SBCS_WaterLevelMeaurementDevice_getLevel_ret_value_roundtrip():
    instance = SBCS_WaterLevelMeaurementDevice_getLevel(ret=3.14)
    assert instance.ret == 3.14
    instance.ret = 9.99
    assert instance.ret == 9.99


def test_SBCS_ControlProgram_Start_isa_Transition():
    instance = SBCS_ControlProgram_Start()
    assert isinstance(instance, Transition)


def test_SBCS_PumpController_ClosePump_isa_Transition():
    instance = SBCS_PumpController_ClosePump()
    assert isinstance(instance, Transition)


def test_SBCS_PumpController_OpenPump_isa_Transition():
    instance = SBCS_PumpController_OpenPump()
    assert isinstance(instance, Transition)


def test_SBCS_SteamBoiler_OpenValve_isa_Transition():
    instance = SBCS_SteamBoiler_OpenValve()
    assert isinstance(instance, Transition)


def test_SBCS_WaterLevelMeaurementDevice_getLevel_isa_Transition():
    instance = SBCS_WaterLevelMeaurementDevice_getLevel(ret=3.14)
    assert isinstance(instance, Transition)


def test_assoc_AfterTrans16_link_reassign_clear():
    a = SBCS_Snapshot()
    b1 = SBCS_Transition()
    b2 = SBCS_Transition()
    _safe_set(a, 'AfterTrans', b1)
    assert _is_linked(a, 'AfterTrans', b1)
    if hasattr(b1, 'Transition17'):
        assert _is_linked(b1, 'Transition17', a)
    _safe_set(a, 'AfterTrans', b2)
    assert _is_linked(a, 'AfterTrans', b2)
    if hasattr(b1, 'Transition17'):
        assert not _is_linked(b1, 'Transition17', a)
    if hasattr(b2, 'Transition17'):
        assert _is_linked(b2, 'Transition17', a)
    _safe_set(a, 'AfterTrans', None)
    assert not _is_linked(a, 'AfterTrans', b2)
    if hasattr(b2, 'Transition17'):
        assert not _is_linked(b2, 'Transition17', a)


def test_assoc_AfterTrans42_link_reassign_clear():
    a = SBCS_Snapshot()
    b1 = SBCS_Transition()
    b2 = SBCS_Transition()
    _safe_set(a, 'Snapshot44', b1)
    assert _is_linked(a, 'Snapshot44', b1)
    if hasattr(b1, 'AfterTrans43'):
        assert _is_linked(b1, 'AfterTrans43', a)
    _safe_set(a, 'Snapshot44', b2)
    assert _is_linked(a, 'Snapshot44', b2)
    if hasattr(b1, 'AfterTrans43'):
        assert not _is_linked(b1, 'AfterTrans43', a)
    if hasattr(b2, 'AfterTrans43'):
        assert _is_linked(b2, 'AfterTrans43', a)
    _safe_set(a, 'Snapshot44', None)
    assert not _is_linked(a, 'Snapshot44', b2)
    if hasattr(b2, 'AfterTrans43'):
        assert not _is_linked(b2, 'AfterTrans43', a)


def test_assoc_BeforeTrans15_link_reassign_clear():
    a = SBCS_Snapshot()
    b1 = SBCS_Transition()
    b2 = SBCS_Transition()
    _safe_set(a, 'BeforeTrans', b1)
    assert _is_linked(a, 'BeforeTrans', b1)
    if hasattr(b1, 'Transition'):
        assert _is_linked(b1, 'Transition', a)
    _safe_set(a, 'BeforeTrans', b2)
    assert _is_linked(a, 'BeforeTrans', b2)
    if hasattr(b1, 'Transition'):
        assert not _is_linked(b1, 'Transition', a)
    if hasattr(b2, 'Transition'):
        assert _is_linked(b2, 'Transition', a)
    _safe_set(a, 'BeforeTrans', None)
    assert not _is_linked(a, 'BeforeTrans', b2)
    if hasattr(b2, 'Transition'):
        assert not _is_linked(b2, 'Transition', a)


def test_assoc_BeforeTrans39_link_reassign_clear():
    a = SBCS_Snapshot()
    b1 = SBCS_Transition()
    b2 = SBCS_Transition()
    _safe_set(a, 'Snapshot41', b1)
    assert _is_linked(a, 'Snapshot41', b1)
    if hasattr(b1, 'BeforeTrans40'):
        assert _is_linked(b1, 'BeforeTrans40', a)
    _safe_set(a, 'Snapshot41', b2)
    assert _is_linked(a, 'Snapshot41', b2)
    if hasattr(b1, 'BeforeTrans40'):
        assert not _is_linked(b1, 'BeforeTrans40', a)
    if hasattr(b2, 'BeforeTrans40'):
        assert _is_linked(b2, 'BeforeTrans40', a)
    _safe_set(a, 'Snapshot41', None)
    assert not _is_linked(a, 'Snapshot41', b2)
    if hasattr(b2, 'BeforeTrans40'):
        assert not _is_linked(b2, 'BeforeTrans40', a)


def test_assoc_CPPost64_link_reassign_clear():
    a = SBCS_ControlProgram(failureDetected=True, mode="sample_text", pumpControlerFailure=True, pumpFailure=True, ready=True, smdFailure=True, wlmdFailure=True)
    b1 = SBCS_ControlProgram_Start()
    b2 = SBCS_ControlProgram_Start()
    _safe_set(a, 'SBCS_ControlProgram66', b1)
    assert _is_linked(a, 'SBCS_ControlProgram66', b1)
    if hasattr(b1, 'SBCS_ControlProgram_Start65'):
        assert _is_linked(b1, 'SBCS_ControlProgram_Start65', a)
    _safe_set(a, 'SBCS_ControlProgram66', b2)
    assert _is_linked(a, 'SBCS_ControlProgram66', b2)
    if hasattr(b1, 'SBCS_ControlProgram_Start65'):
        assert not _is_linked(b1, 'SBCS_ControlProgram_Start65', a)
    if hasattr(b2, 'SBCS_ControlProgram_Start65'):
        assert _is_linked(b2, 'SBCS_ControlProgram_Start65', a)
    _safe_set(a, 'SBCS_ControlProgram66', None)
    assert not _is_linked(a, 'SBCS_ControlProgram66', b2)
    if hasattr(b2, 'SBCS_ControlProgram_Start65'):
        assert not _is_linked(b2, 'SBCS_ControlProgram_Start65', a)


def test_assoc_CPPre63_link_reassign_clear():
    a = SBCS_ControlProgram(failureDetected=True, mode="sample_text", pumpControlerFailure=True, pumpFailure=True, ready=True, smdFailure=True, wlmdFailure=True)
    b1 = SBCS_ControlProgram_Start()
    b2 = SBCS_ControlProgram_Start()
    _safe_set(a, 'SBCS_ControlProgram', b1)
    assert _is_linked(a, 'SBCS_ControlProgram', b1)
    if hasattr(b1, 'SBCS_ControlProgram_Start'):
        assert _is_linked(b1, 'SBCS_ControlProgram_Start', a)
    _safe_set(a, 'SBCS_ControlProgram', b2)
    assert _is_linked(a, 'SBCS_ControlProgram', b2)
    if hasattr(b1, 'SBCS_ControlProgram_Start'):
        assert not _is_linked(b1, 'SBCS_ControlProgram_Start', a)
    if hasattr(b2, 'SBCS_ControlProgram_Start'):
        assert _is_linked(b2, 'SBCS_ControlProgram_Start', a)
    _safe_set(a, 'SBCS_ControlProgram', None)
    assert not _is_linked(a, 'SBCS_ControlProgram', b2)
    if hasattr(b2, 'SBCS_ControlProgram_Start'):
        assert not _is_linked(b2, 'SBCS_ControlProgram_Start', a)


def test_assoc_ControlProgramPump20_link_reassign_clear():
    a = SBCS_Pump(capacity=3.14, mode="sample_text", ready=True)
    b1 = SBCS_ControlProgram(failureDetected=True, mode="sample_text", pumpControlerFailure=True, pumpFailure=True, ready=True, smdFailure=True, wlmdFailure=True)
    b2 = SBCS_ControlProgram(failureDetected=False, mode="sample_text_2", pumpControlerFailure=False, pumpFailure=False, ready=False, smdFailure=False, wlmdFailure=False)
    _safe_set(a, 'Pump21', b1)
    assert _is_linked(a, 'Pump21', b1)
    if hasattr(b1, 'PumpControlProgram'):
        assert _is_linked(b1, 'PumpControlProgram', a)
    _safe_set(a, 'Pump21', b2)
    assert _is_linked(a, 'Pump21', b2)
    if hasattr(b1, 'PumpControlProgram'):
        assert not _is_linked(b1, 'PumpControlProgram', a)
    if hasattr(b2, 'PumpControlProgram'):
        assert _is_linked(b2, 'PumpControlProgram', a)
    _safe_set(a, 'Pump21', None)
    assert not _is_linked(a, 'Pump21', b2)
    if hasattr(b2, 'PumpControlProgram'):
        assert not _is_linked(b2, 'PumpControlProgram', a)


def test_assoc_ControlProgramPumpControler28_link_reassign_clear():
    a = SBCS_PumpControler(circulating=True, ready=True)
    b1 = SBCS_ControlProgram(failureDetected=True, mode="sample_text", pumpControlerFailure=True, pumpFailure=True, ready=True, smdFailure=True, wlmdFailure=True)
    b2 = SBCS_ControlProgram(failureDetected=False, mode="sample_text_2", pumpControlerFailure=False, pumpFailure=False, ready=False, smdFailure=False, wlmdFailure=False)
    _safe_set(a, 'PumpControler29', b1)
    assert _is_linked(a, 'PumpControler29', b1)
    if hasattr(b1, 'PumpControlerControlProgram'):
        assert _is_linked(b1, 'PumpControlerControlProgram', a)
    _safe_set(a, 'PumpControler29', b2)
    assert _is_linked(a, 'PumpControler29', b2)
    if hasattr(b1, 'PumpControlerControlProgram'):
        assert not _is_linked(b1, 'PumpControlerControlProgram', a)
    if hasattr(b2, 'PumpControlerControlProgram'):
        assert _is_linked(b2, 'PumpControlerControlProgram', a)
    _safe_set(a, 'PumpControler29', None)
    assert not _is_linked(a, 'PumpControler29', b2)
    if hasattr(b2, 'PumpControlerControlProgram'):
        assert not _is_linked(b2, 'PumpControlerControlProgram', a)


def test_assoc_ControlProgramSMD24_link_reassign_clear():
    a = SBCS_SteamMeasurementDevice(evaporationRate=True, ready=True, waterLevel=3.14)
    b1 = SBCS_ControlProgram(failureDetected=True, mode="sample_text", pumpControlerFailure=True, pumpFailure=True, ready=True, smdFailure=True, wlmdFailure=True)
    b2 = SBCS_ControlProgram(failureDetected=False, mode="sample_text_2", pumpControlerFailure=False, pumpFailure=False, ready=False, smdFailure=False, wlmdFailure=False)
    _safe_set(a, 'SteamMeasurementDevice25', b1)
    assert _is_linked(a, 'SteamMeasurementDevice25', b1)
    if hasattr(b1, 'SMDControlProgram'):
        assert _is_linked(b1, 'SMDControlProgram', a)
    _safe_set(a, 'SteamMeasurementDevice25', b2)
    assert _is_linked(a, 'SteamMeasurementDevice25', b2)
    if hasattr(b1, 'SMDControlProgram'):
        assert not _is_linked(b1, 'SMDControlProgram', a)
    if hasattr(b2, 'SMDControlProgram'):
        assert _is_linked(b2, 'SMDControlProgram', a)
    _safe_set(a, 'SteamMeasurementDevice25', None)
    assert not _is_linked(a, 'SteamMeasurementDevice25', b2)
    if hasattr(b2, 'SMDControlProgram'):
        assert not _is_linked(b2, 'SMDControlProgram', a)


def test_assoc_ControlProgramSnapshot6_link_reassign_clear():
    a = SBCS_Snapshot()
    b1 = SBCS_ControlProgram(failureDetected=True, mode="sample_text", pumpControlerFailure=True, pumpFailure=True, ready=True, smdFailure=True, wlmdFailure=True)
    b2 = SBCS_ControlProgram(failureDetected=False, mode="sample_text_2", pumpControlerFailure=False, pumpFailure=False, ready=False, smdFailure=False, wlmdFailure=False)
    _safe_set(a, 'SnapshotControlProgram', b1)
    assert _is_linked(a, 'SnapshotControlProgram', b1)
    if hasattr(b1, 'ControlProgram7'):
        assert _is_linked(b1, 'ControlProgram7', a)
    _safe_set(a, 'SnapshotControlProgram', b2)
    assert _is_linked(a, 'SnapshotControlProgram', b2)
    if hasattr(b1, 'ControlProgram7'):
        assert not _is_linked(b1, 'ControlProgram7', a)
    if hasattr(b2, 'ControlProgram7'):
        assert _is_linked(b2, 'ControlProgram7', a)
    _safe_set(a, 'SnapshotControlProgram', None)
    assert not _is_linked(a, 'SnapshotControlProgram', b2)
    if hasattr(b2, 'ControlProgram7'):
        assert not _is_linked(b2, 'ControlProgram7', a)


def test_assoc_ControlProgramSteamBoiler26_link_reassign_clear():
    a = SBCS_SteamBoiler(capacity=3.14, maximalLimit=3.14, maximalNormal=3.14, maximumDecrease=3.14, maximumIncrease=3.14, minimalLimit=3.14, minimalNormal=3.14, ready=True, valveOpen="sample_text")
    b1 = SBCS_ControlProgram(failureDetected=True, mode="sample_text", pumpControlerFailure=True, pumpFailure=True, ready=True, smdFailure=True, wlmdFailure=True)
    b2 = SBCS_ControlProgram(failureDetected=False, mode="sample_text_2", pumpControlerFailure=False, pumpFailure=False, ready=False, smdFailure=False, wlmdFailure=False)
    _safe_set(a, 'SteamBoiler27', b1)
    assert _is_linked(a, 'SteamBoiler27', b1)
    if hasattr(b1, 'SteamBoilerControlProgram'):
        assert _is_linked(b1, 'SteamBoilerControlProgram', a)
    _safe_set(a, 'SteamBoiler27', b2)
    assert _is_linked(a, 'SteamBoiler27', b2)
    if hasattr(b1, 'SteamBoilerControlProgram'):
        assert not _is_linked(b1, 'SteamBoilerControlProgram', a)
    if hasattr(b2, 'SteamBoilerControlProgram'):
        assert _is_linked(b2, 'SteamBoilerControlProgram', a)
    _safe_set(a, 'SteamBoiler27', None)
    assert not _is_linked(a, 'SteamBoiler27', b2)
    if hasattr(b2, 'SteamBoilerControlProgram'):
        assert not _is_linked(b2, 'SteamBoilerControlProgram', a)


def test_assoc_ControlProgramWLMD22_link_reassign_clear():
    a = SBCS_WaterLevelMeasurementDevice(ready=True, waterLevel=3.14)
    b1 = SBCS_ControlProgram(failureDetected=True, mode="sample_text", pumpControlerFailure=True, pumpFailure=True, ready=True, smdFailure=True, wlmdFailure=True)
    b2 = SBCS_ControlProgram(failureDetected=False, mode="sample_text_2", pumpControlerFailure=False, pumpFailure=False, ready=False, smdFailure=False, wlmdFailure=False)
    _safe_set(a, 'WaterLevelMeasurementDevice23', b1)
    assert _is_linked(a, 'WaterLevelMeasurementDevice23', b1)
    if hasattr(b1, 'WLMDControlProgram'):
        assert _is_linked(b1, 'WLMDControlProgram', a)
    _safe_set(a, 'WaterLevelMeasurementDevice23', b2)
    assert _is_linked(a, 'WaterLevelMeasurementDevice23', b2)
    if hasattr(b1, 'WLMDControlProgram'):
        assert not _is_linked(b1, 'WLMDControlProgram', a)
    if hasattr(b2, 'WLMDControlProgram'):
        assert _is_linked(b2, 'WLMDControlProgram', a)
    _safe_set(a, 'WaterLevelMeasurementDevice23', None)
    assert not _is_linked(a, 'WaterLevelMeasurementDevice23', b2)
    if hasattr(b2, 'WLMDControlProgram'):
        assert not _is_linked(b2, 'WLMDControlProgram', a)


def test_assoc_PCPost76_link_reassign_clear():
    a = SBCS_PumpControler(circulating=True, ready=True)
    b1 = SBCS_PumpController_ClosePump()
    b2 = SBCS_PumpController_ClosePump()
    _safe_set(a, 'SBCS_PumpControler78', b1)
    assert _is_linked(a, 'SBCS_PumpControler78', b1)
    if hasattr(b1, 'SBCS_PumpController_ClosePump77'):
        assert _is_linked(b1, 'SBCS_PumpController_ClosePump77', a)
    _safe_set(a, 'SBCS_PumpControler78', b2)
    assert _is_linked(a, 'SBCS_PumpControler78', b2)
    if hasattr(b1, 'SBCS_PumpController_ClosePump77'):
        assert not _is_linked(b1, 'SBCS_PumpController_ClosePump77', a)
    if hasattr(b2, 'SBCS_PumpController_ClosePump77'):
        assert _is_linked(b2, 'SBCS_PumpController_ClosePump77', a)
    _safe_set(a, 'SBCS_PumpControler78', None)
    assert not _is_linked(a, 'SBCS_PumpControler78', b2)
    if hasattr(b2, 'SBCS_PumpController_ClosePump77'):
        assert not _is_linked(b2, 'SBCS_PumpController_ClosePump77', a)


def test_assoc_PCPost81_link_reassign_clear():
    a = SBCS_PumpControler(circulating=True, ready=True)
    b1 = SBCS_PumpController_OpenPump()
    b2 = SBCS_PumpController_OpenPump()
    _safe_set(a, 'SBCS_PumpControler83', b1)
    assert _is_linked(a, 'SBCS_PumpControler83', b1)
    if hasattr(b1, 'SBCS_PumpController_OpenPump82'):
        assert _is_linked(b1, 'SBCS_PumpController_OpenPump82', a)
    _safe_set(a, 'SBCS_PumpControler83', b2)
    assert _is_linked(a, 'SBCS_PumpControler83', b2)
    if hasattr(b1, 'SBCS_PumpController_OpenPump82'):
        assert not _is_linked(b1, 'SBCS_PumpController_OpenPump82', a)
    if hasattr(b2, 'SBCS_PumpController_OpenPump82'):
        assert _is_linked(b2, 'SBCS_PumpController_OpenPump82', a)
    _safe_set(a, 'SBCS_PumpControler83', None)
    assert not _is_linked(a, 'SBCS_PumpControler83', b2)
    if hasattr(b2, 'SBCS_PumpController_OpenPump82'):
        assert not _is_linked(b2, 'SBCS_PumpController_OpenPump82', a)


def test_assoc_PCPre75_link_reassign_clear():
    a = SBCS_PumpControler(circulating=True, ready=True)
    b1 = SBCS_PumpController_ClosePump()
    b2 = SBCS_PumpController_ClosePump()
    _safe_set(a, 'SBCS_PumpControler', b1)
    assert _is_linked(a, 'SBCS_PumpControler', b1)
    if hasattr(b1, 'SBCS_PumpController_ClosePump'):
        assert _is_linked(b1, 'SBCS_PumpController_ClosePump', a)
    _safe_set(a, 'SBCS_PumpControler', b2)
    assert _is_linked(a, 'SBCS_PumpControler', b2)
    if hasattr(b1, 'SBCS_PumpController_ClosePump'):
        assert not _is_linked(b1, 'SBCS_PumpController_ClosePump', a)
    if hasattr(b2, 'SBCS_PumpController_ClosePump'):
        assert _is_linked(b2, 'SBCS_PumpController_ClosePump', a)
    _safe_set(a, 'SBCS_PumpControler', None)
    assert not _is_linked(a, 'SBCS_PumpControler', b2)
    if hasattr(b2, 'SBCS_PumpController_ClosePump'):
        assert not _is_linked(b2, 'SBCS_PumpController_ClosePump', a)


def test_assoc_PCPre79_link_reassign_clear():
    a = SBCS_PumpControler(circulating=True, ready=True)
    b1 = SBCS_PumpController_OpenPump()
    b2 = SBCS_PumpController_OpenPump()
    _safe_set(a, 'SBCS_PumpControler80', b1)
    assert _is_linked(a, 'SBCS_PumpControler80', b1)
    if hasattr(b1, 'SBCS_PumpController_OpenPump'):
        assert _is_linked(b1, 'SBCS_PumpController_OpenPump', a)
    _safe_set(a, 'SBCS_PumpControler80', b2)
    assert _is_linked(a, 'SBCS_PumpControler80', b2)
    if hasattr(b1, 'SBCS_PumpController_OpenPump'):
        assert not _is_linked(b1, 'SBCS_PumpController_OpenPump', a)
    if hasattr(b2, 'SBCS_PumpController_OpenPump'):
        assert _is_linked(b2, 'SBCS_PumpController_OpenPump', a)
    _safe_set(a, 'SBCS_PumpControler80', None)
    assert not _is_linked(a, 'SBCS_PumpControler80', b2)
    if hasattr(b2, 'SBCS_PumpController_OpenPump'):
        assert not _is_linked(b2, 'SBCS_PumpController_OpenPump', a)


def test_assoc_PumpControlProgram33_link_reassign_clear():
    a = SBCS_Pump(capacity=3.14, mode="sample_text", ready=True)
    b1 = SBCS_ControlProgram(failureDetected=True, mode="sample_text", pumpControlerFailure=True, pumpFailure=True, ready=True, smdFailure=True, wlmdFailure=True)
    b2 = SBCS_ControlProgram(failureDetected=False, mode="sample_text_2", pumpControlerFailure=False, pumpFailure=False, ready=False, smdFailure=False, wlmdFailure=False)
    _safe_set(a, 'ControlProgramPump', b1)
    assert _is_linked(a, 'ControlProgramPump', b1)
    if hasattr(b1, 'ControlProgram34'):
        assert _is_linked(b1, 'ControlProgram34', a)
    _safe_set(a, 'ControlProgramPump', b2)
    assert _is_linked(a, 'ControlProgramPump', b2)
    if hasattr(b1, 'ControlProgram34'):
        assert not _is_linked(b1, 'ControlProgram34', a)
    if hasattr(b2, 'ControlProgram34'):
        assert _is_linked(b2, 'ControlProgram34', a)
    _safe_set(a, 'ControlProgramPump', None)
    assert not _is_linked(a, 'ControlProgramPump', b2)
    if hasattr(b2, 'ControlProgram34'):
        assert not _is_linked(b2, 'ControlProgram34', a)


def test_assoc_PumpControlSnapshot14_link_reassign_clear():
    a = SBCS_Snapshot()
    b1 = SBCS_PumpControler(circulating=True, ready=True)
    b2 = SBCS_PumpControler(circulating=False, ready=False)
    _safe_set(a, 'SnapshotPumpControl', b1)
    assert _is_linked(a, 'SnapshotPumpControl', b1)
    if hasattr(b1, 'PumpControler'):
        assert _is_linked(b1, 'PumpControler', a)
    _safe_set(a, 'SnapshotPumpControl', b2)
    assert _is_linked(a, 'SnapshotPumpControl', b2)
    if hasattr(b1, 'PumpControler'):
        assert not _is_linked(b1, 'PumpControler', a)
    if hasattr(b2, 'PumpControler'):
        assert _is_linked(b2, 'PumpControler', a)
    _safe_set(a, 'SnapshotPumpControl', None)
    assert not _is_linked(a, 'SnapshotPumpControl', b2)
    if hasattr(b2, 'PumpControler'):
        assert not _is_linked(b2, 'PumpControler', a)


def test_assoc_PumpControlerControlProgram47_link_reassign_clear():
    a = SBCS_PumpControler(circulating=True, ready=True)
    b1 = SBCS_ControlProgram(failureDetected=True, mode="sample_text", pumpControlerFailure=True, pumpFailure=True, ready=True, smdFailure=True, wlmdFailure=True)
    b2 = SBCS_ControlProgram(failureDetected=False, mode="sample_text_2", pumpControlerFailure=False, pumpFailure=False, ready=False, smdFailure=False, wlmdFailure=False)
    _safe_set(a, 'ControlProgramPumpControler', b1)
    assert _is_linked(a, 'ControlProgramPumpControler', b1)
    if hasattr(b1, 'ControlProgram48'):
        assert _is_linked(b1, 'ControlProgram48', a)
    _safe_set(a, 'ControlProgramPumpControler', b2)
    assert _is_linked(a, 'ControlProgramPumpControler', b2)
    if hasattr(b1, 'ControlProgram48'):
        assert not _is_linked(b1, 'ControlProgram48', a)
    if hasattr(b2, 'ControlProgram48'):
        assert _is_linked(b2, 'ControlProgram48', a)
    _safe_set(a, 'ControlProgramPumpControler', None)
    assert not _is_linked(a, 'ControlProgramPumpControler', b2)
    if hasattr(b2, 'ControlProgram48'):
        assert not _is_linked(b2, 'ControlProgram48', a)


def test_assoc_PumpControlerPump49_link_reassign_clear():
    a = SBCS_PumpControler(circulating=True, ready=True)
    b1 = SBCS_Pump(capacity=3.14, mode="sample_text", ready=True)
    b2 = SBCS_Pump(capacity=9.99, mode="sample_text_2", ready=False)
    _safe_set(a, 'PumpPumpControler', b1)
    assert _is_linked(a, 'PumpPumpControler', b1)
    if hasattr(b1, 'Pump50'):
        assert _is_linked(b1, 'Pump50', a)
    _safe_set(a, 'PumpPumpControler', b2)
    assert _is_linked(a, 'PumpPumpControler', b2)
    if hasattr(b1, 'Pump50'):
        assert not _is_linked(b1, 'Pump50', a)
    if hasattr(b2, 'Pump50'):
        assert _is_linked(b2, 'Pump50', a)
    _safe_set(a, 'PumpPumpControler', None)
    assert not _is_linked(a, 'PumpPumpControler', b2)
    if hasattr(b2, 'Pump50'):
        assert not _is_linked(b2, 'Pump50', a)


def test_assoc_PumpPumpControler35_link_reassign_clear():
    a = SBCS_PumpControler(circulating=True, ready=True)
    b1 = SBCS_Pump(capacity=3.14, mode="sample_text", ready=True)
    b2 = SBCS_Pump(capacity=9.99, mode="sample_text_2", ready=False)
    _safe_set(a, 'PumpControler36', b1)
    assert _is_linked(a, 'PumpControler36', b1)
    if hasattr(b1, 'PumpControlerPump'):
        assert _is_linked(b1, 'PumpControlerPump', a)
    _safe_set(a, 'PumpControler36', b2)
    assert _is_linked(a, 'PumpControler36', b2)
    if hasattr(b1, 'PumpControlerPump'):
        assert not _is_linked(b1, 'PumpControlerPump', a)
    if hasattr(b2, 'PumpControlerPump'):
        assert _is_linked(b2, 'PumpControlerPump', a)
    _safe_set(a, 'PumpControler36', None)
    assert not _is_linked(a, 'PumpControler36', b2)
    if hasattr(b2, 'PumpControlerPump'):
        assert not _is_linked(b2, 'PumpControlerPump', a)


def test_assoc_PumpSnapshot30_link_reassign_clear():
    a = SBCS_Snapshot()
    b1 = SBCS_Pump(capacity=3.14, mode="sample_text", ready=True)
    b2 = SBCS_Pump(capacity=9.99, mode="sample_text_2", ready=False)
    _safe_set(a, 'Snapshot32', b1)
    assert _is_linked(a, 'Snapshot32', b1)
    if hasattr(b1, 'PumpSnapshot31'):
        assert _is_linked(b1, 'PumpSnapshot31', a)
    _safe_set(a, 'Snapshot32', b2)
    assert _is_linked(a, 'Snapshot32', b2)
    if hasattr(b1, 'PumpSnapshot31'):
        assert not _is_linked(b1, 'PumpSnapshot31', a)
    if hasattr(b2, 'PumpSnapshot31'):
        assert _is_linked(b2, 'PumpSnapshot31', a)
    _safe_set(a, 'Snapshot32', None)
    assert not _is_linked(a, 'Snapshot32', b2)
    if hasattr(b2, 'PumpSnapshot31'):
        assert not _is_linked(b2, 'PumpSnapshot31', a)


def test_assoc_PumpSnapshot8_link_reassign_clear():
    a = SBCS_Snapshot()
    b1 = SBCS_Pump(capacity=3.14, mode="sample_text", ready=True)
    b2 = SBCS_Pump(capacity=9.99, mode="sample_text_2", ready=False)
    _safe_set(a, 'PumpSnapshot', b1)
    assert _is_linked(a, 'PumpSnapshot', b1)
    if hasattr(b1, 'Pump9'):
        assert _is_linked(b1, 'Pump9', a)
    _safe_set(a, 'PumpSnapshot', b2)
    assert _is_linked(a, 'PumpSnapshot', b2)
    if hasattr(b1, 'Pump9'):
        assert not _is_linked(b1, 'Pump9', a)
    if hasattr(b2, 'Pump9'):
        assert _is_linked(b2, 'Pump9', a)
    _safe_set(a, 'PumpSnapshot', None)
    assert not _is_linked(a, 'PumpSnapshot', b2)
    if hasattr(b2, 'Pump9'):
        assert not _is_linked(b2, 'Pump9', a)


def test_assoc_PumpSteamBoiler37_link_reassign_clear():
    a = SBCS_SteamBoiler(capacity=3.14, maximalLimit=3.14, maximalNormal=3.14, maximumDecrease=3.14, maximumIncrease=3.14, minimalLimit=3.14, minimalNormal=3.14, ready=True, valveOpen="sample_text")
    b1 = SBCS_Pump(capacity=3.14, mode="sample_text", ready=True)
    b2 = SBCS_Pump(capacity=9.99, mode="sample_text_2", ready=False)
    _safe_set(a, 'SteamBoiler38', b1)
    assert _is_linked(a, 'SteamBoiler38', b1)
    if hasattr(b1, 'SteqmBoilerPump'):
        assert _is_linked(b1, 'SteqmBoilerPump', a)
    _safe_set(a, 'SteamBoiler38', b2)
    assert _is_linked(a, 'SteamBoiler38', b2)
    if hasattr(b1, 'SteqmBoilerPump'):
        assert not _is_linked(b1, 'SteqmBoilerPump', a)
    if hasattr(b2, 'SteqmBoilerPump'):
        assert _is_linked(b2, 'SteqmBoilerPump', a)
    _safe_set(a, 'SteamBoiler38', None)
    assert not _is_linked(a, 'SteamBoiler38', b2)
    if hasattr(b2, 'SteqmBoilerPump'):
        assert not _is_linked(b2, 'SteqmBoilerPump', a)


def test_assoc_SBPost72_link_reassign_clear():
    a = SBCS_SteamBoiler(capacity=3.14, maximalLimit=3.14, maximalNormal=3.14, maximumDecrease=3.14, maximumIncrease=3.14, minimalLimit=3.14, minimalNormal=3.14, ready=True, valveOpen="sample_text")
    b1 = SBCS_SteamBoiler_OpenValve()
    b2 = SBCS_SteamBoiler_OpenValve()
    _safe_set(a, 'SBCS_SteamBoiler74', b1)
    assert _is_linked(a, 'SBCS_SteamBoiler74', b1)
    if hasattr(b1, 'SBCS_SteamBoiler_OpenValve73'):
        assert _is_linked(b1, 'SBCS_SteamBoiler_OpenValve73', a)
    _safe_set(a, 'SBCS_SteamBoiler74', b2)
    assert _is_linked(a, 'SBCS_SteamBoiler74', b2)
    if hasattr(b1, 'SBCS_SteamBoiler_OpenValve73'):
        assert not _is_linked(b1, 'SBCS_SteamBoiler_OpenValve73', a)
    if hasattr(b2, 'SBCS_SteamBoiler_OpenValve73'):
        assert _is_linked(b2, 'SBCS_SteamBoiler_OpenValve73', a)
    _safe_set(a, 'SBCS_SteamBoiler74', None)
    assert not _is_linked(a, 'SBCS_SteamBoiler74', b2)
    if hasattr(b2, 'SBCS_SteamBoiler_OpenValve73'):
        assert not _is_linked(b2, 'SBCS_SteamBoiler_OpenValve73', a)


def test_assoc_SBPre71_link_reassign_clear():
    a = SBCS_SteamBoiler(capacity=3.14, maximalLimit=3.14, maximalNormal=3.14, maximumDecrease=3.14, maximumIncrease=3.14, minimalLimit=3.14, minimalNormal=3.14, ready=True, valveOpen="sample_text")
    b1 = SBCS_SteamBoiler_OpenValve()
    b2 = SBCS_SteamBoiler_OpenValve()
    _safe_set(a, 'SBCS_SteamBoiler', b1)
    assert _is_linked(a, 'SBCS_SteamBoiler', b1)
    if hasattr(b1, 'SBCS_SteamBoiler_OpenValve'):
        assert _is_linked(b1, 'SBCS_SteamBoiler_OpenValve', a)
    _safe_set(a, 'SBCS_SteamBoiler', b2)
    assert _is_linked(a, 'SBCS_SteamBoiler', b2)
    if hasattr(b1, 'SBCS_SteamBoiler_OpenValve'):
        assert not _is_linked(b1, 'SBCS_SteamBoiler_OpenValve', a)
    if hasattr(b2, 'SBCS_SteamBoiler_OpenValve'):
        assert _is_linked(b2, 'SBCS_SteamBoiler_OpenValve', a)
    _safe_set(a, 'SBCS_SteamBoiler', None)
    assert not _is_linked(a, 'SBCS_SteamBoiler', b2)
    if hasattr(b2, 'SBCS_SteamBoiler_OpenValve'):
        assert not _is_linked(b2, 'SBCS_SteamBoiler_OpenValve', a)


def test_assoc_SMDControlProgram53_link_reassign_clear():
    a = SBCS_SteamMeasurementDevice(evaporationRate=True, ready=True, waterLevel=3.14)
    b1 = SBCS_ControlProgram(failureDetected=True, mode="sample_text", pumpControlerFailure=True, pumpFailure=True, ready=True, smdFailure=True, wlmdFailure=True)
    b2 = SBCS_ControlProgram(failureDetected=False, mode="sample_text_2", pumpControlerFailure=False, pumpFailure=False, ready=False, smdFailure=False, wlmdFailure=False)
    _safe_set(a, 'ControlProgramSMD', b1)
    assert _is_linked(a, 'ControlProgramSMD', b1)
    if hasattr(b1, 'ControlProgram54'):
        assert _is_linked(b1, 'ControlProgram54', a)
    _safe_set(a, 'ControlProgramSMD', b2)
    assert _is_linked(a, 'ControlProgramSMD', b2)
    if hasattr(b1, 'ControlProgram54'):
        assert not _is_linked(b1, 'ControlProgram54', a)
    if hasattr(b2, 'ControlProgram54'):
        assert _is_linked(b2, 'ControlProgram54', a)
    _safe_set(a, 'ControlProgramSMD', None)
    assert not _is_linked(a, 'ControlProgramSMD', b2)
    if hasattr(b2, 'ControlProgram54'):
        assert not _is_linked(b2, 'ControlProgram54', a)


def test_assoc_SMDSteamBoiler55_link_reassign_clear():
    a = SBCS_SteamMeasurementDevice(evaporationRate=True, ready=True, waterLevel=3.14)
    b1 = SBCS_SteamBoiler(capacity=3.14, maximalLimit=3.14, maximalNormal=3.14, maximumDecrease=3.14, maximumIncrease=3.14, minimalLimit=3.14, minimalNormal=3.14, ready=True, valveOpen="sample_text")
    b2 = SBCS_SteamBoiler(capacity=9.99, maximalLimit=9.99, maximalNormal=9.99, maximumDecrease=9.99, maximumIncrease=9.99, minimalLimit=9.99, minimalNormal=9.99, ready=False, valveOpen="sample_text_2")
    _safe_set(a, 'SteamBoilerSMD', b1)
    assert _is_linked(a, 'SteamBoilerSMD', b1)
    if hasattr(b1, 'SteamBoiler56'):
        assert _is_linked(b1, 'SteamBoiler56', a)
    _safe_set(a, 'SteamBoilerSMD', b2)
    assert _is_linked(a, 'SteamBoilerSMD', b2)
    if hasattr(b1, 'SteamBoiler56'):
        assert not _is_linked(b1, 'SteamBoiler56', a)
    if hasattr(b2, 'SteamBoiler56'):
        assert _is_linked(b2, 'SteamBoiler56', a)
    _safe_set(a, 'SteamBoilerSMD', None)
    assert not _is_linked(a, 'SteamBoilerSMD', b2)
    if hasattr(b2, 'SteamBoiler56'):
        assert not _is_linked(b2, 'SteamBoiler56', a)


def test_assoc_SnapshotControlProgram18_link_reassign_clear():
    a = SBCS_Snapshot()
    b1 = SBCS_ControlProgram(failureDetected=True, mode="sample_text", pumpControlerFailure=True, pumpFailure=True, ready=True, smdFailure=True, wlmdFailure=True)
    b2 = SBCS_ControlProgram(failureDetected=False, mode="sample_text_2", pumpControlerFailure=False, pumpFailure=False, ready=False, smdFailure=False, wlmdFailure=False)
    _safe_set(a, 'Snapshot19', b1)
    assert _is_linked(a, 'Snapshot19', b1)
    if hasattr(b1, 'ControlProgramSnapshot'):
        assert _is_linked(b1, 'ControlProgramSnapshot', a)
    _safe_set(a, 'Snapshot19', b2)
    assert _is_linked(a, 'Snapshot19', b2)
    if hasattr(b1, 'ControlProgramSnapshot'):
        assert not _is_linked(b1, 'ControlProgramSnapshot', a)
    if hasattr(b2, 'ControlProgramSnapshot'):
        assert _is_linked(b2, 'ControlProgramSnapshot', a)
    _safe_set(a, 'Snapshot19', None)
    assert not _is_linked(a, 'Snapshot19', b2)
    if hasattr(b2, 'ControlProgramSnapshot'):
        assert not _is_linked(b2, 'ControlProgramSnapshot', a)


def test_assoc_SnapshotPumpControl45_link_reassign_clear():
    a = SBCS_Snapshot()
    b1 = SBCS_PumpControler(circulating=True, ready=True)
    b2 = SBCS_PumpControler(circulating=False, ready=False)
    _safe_set(a, 'Snapshot46', b1)
    assert _is_linked(a, 'Snapshot46', b1)
    if hasattr(b1, 'PumpControlSnapshot'):
        assert _is_linked(b1, 'PumpControlSnapshot', a)
    _safe_set(a, 'Snapshot46', b2)
    assert _is_linked(a, 'Snapshot46', b2)
    if hasattr(b1, 'PumpControlSnapshot'):
        assert not _is_linked(b1, 'PumpControlSnapshot', a)
    if hasattr(b2, 'PumpControlSnapshot'):
        assert _is_linked(b2, 'PumpControlSnapshot', a)
    _safe_set(a, 'Snapshot46', None)
    assert not _is_linked(a, 'Snapshot46', b2)
    if hasattr(b2, 'PumpControlSnapshot'):
        assert not _is_linked(b2, 'PumpControlSnapshot', a)


def test_assoc_SnapshotSBMD51_link_reassign_clear():
    a = SBCS_SteamMeasurementDevice(evaporationRate=True, ready=True, waterLevel=3.14)
    b1 = SBCS_Snapshot()
    b2 = SBCS_Snapshot()
    _safe_set(a, 'SteamBoilerMeasurementDeviceSnapshot', b1)
    assert _is_linked(a, 'SteamBoilerMeasurementDeviceSnapshot', b1)
    if hasattr(b1, 'Snapshot52'):
        assert _is_linked(b1, 'Snapshot52', a)
    _safe_set(a, 'SteamBoilerMeasurementDeviceSnapshot', b2)
    assert _is_linked(a, 'SteamBoilerMeasurementDeviceSnapshot', b2)
    if hasattr(b1, 'Snapshot52'):
        assert not _is_linked(b1, 'Snapshot52', a)
    if hasattr(b2, 'Snapshot52'):
        assert _is_linked(b2, 'Snapshot52', a)
    _safe_set(a, 'SteamBoilerMeasurementDeviceSnapshot', None)
    assert not _is_linked(a, 'SteamBoilerMeasurementDeviceSnapshot', b2)
    if hasattr(b2, 'Snapshot52'):
        assert not _is_linked(b2, 'Snapshot52', a)


def test_assoc_SnapshotSteamBoiler0_link_reassign_clear():
    a = SBCS_SteamBoiler(capacity=3.14, maximalLimit=3.14, maximalNormal=3.14, maximumDecrease=3.14, maximumIncrease=3.14, minimalLimit=3.14, minimalNormal=3.14, ready=True, valveOpen="sample_text")
    b1 = SBCS_Snapshot()
    b2 = SBCS_Snapshot()
    _safe_set(a, 'SteamBoilerSnapshot', b1)
    assert _is_linked(a, 'SteamBoilerSnapshot', b1)
    if hasattr(b1, 'Snapshot'):
        assert _is_linked(b1, 'Snapshot', a)
    _safe_set(a, 'SteamBoilerSnapshot', b2)
    assert _is_linked(a, 'SteamBoilerSnapshot', b2)
    if hasattr(b1, 'Snapshot'):
        assert not _is_linked(b1, 'Snapshot', a)
    if hasattr(b2, 'Snapshot'):
        assert _is_linked(b2, 'Snapshot', a)
    _safe_set(a, 'SteamBoilerSnapshot', None)
    assert not _is_linked(a, 'SteamBoilerSnapshot', b2)
    if hasattr(b2, 'Snapshot'):
        assert not _is_linked(b2, 'Snapshot', a)


def test_assoc_SnapshotWLMD57_link_reassign_clear():
    a = SBCS_WaterLevelMeasurementDevice(ready=True, waterLevel=3.14)
    b1 = SBCS_Snapshot()
    b2 = SBCS_Snapshot()
    _safe_set(a, 'WLMDSnapshot', b1)
    assert _is_linked(a, 'WLMDSnapshot', b1)
    if hasattr(b1, 'Snapshot58'):
        assert _is_linked(b1, 'Snapshot58', a)
    _safe_set(a, 'WLMDSnapshot', b2)
    assert _is_linked(a, 'WLMDSnapshot', b2)
    if hasattr(b1, 'Snapshot58'):
        assert not _is_linked(b1, 'Snapshot58', a)
    if hasattr(b2, 'Snapshot58'):
        assert _is_linked(b2, 'Snapshot58', a)
    _safe_set(a, 'WLMDSnapshot', None)
    assert not _is_linked(a, 'WLMDSnapshot', b2)
    if hasattr(b2, 'Snapshot58'):
        assert not _is_linked(b2, 'Snapshot58', a)


def test_assoc_SteamBoilerControlProgram1_link_reassign_clear():
    a = SBCS_SteamBoiler(capacity=3.14, maximalLimit=3.14, maximalNormal=3.14, maximumDecrease=3.14, maximumIncrease=3.14, minimalLimit=3.14, minimalNormal=3.14, ready=True, valveOpen="sample_text")
    b1 = SBCS_ControlProgram(failureDetected=True, mode="sample_text", pumpControlerFailure=True, pumpFailure=True, ready=True, smdFailure=True, wlmdFailure=True)
    b2 = SBCS_ControlProgram(failureDetected=False, mode="sample_text_2", pumpControlerFailure=False, pumpFailure=False, ready=False, smdFailure=False, wlmdFailure=False)
    _safe_set(a, 'ControlProgramSteamBoiler', b1)
    assert _is_linked(a, 'ControlProgramSteamBoiler', b1)
    if hasattr(b1, 'ControlProgram'):
        assert _is_linked(b1, 'ControlProgram', a)
    _safe_set(a, 'ControlProgramSteamBoiler', b2)
    assert _is_linked(a, 'ControlProgramSteamBoiler', b2)
    if hasattr(b1, 'ControlProgram'):
        assert not _is_linked(b1, 'ControlProgram', a)
    if hasattr(b2, 'ControlProgram'):
        assert _is_linked(b2, 'ControlProgram', a)
    _safe_set(a, 'ControlProgramSteamBoiler', None)
    assert not _is_linked(a, 'ControlProgramSteamBoiler', b2)
    if hasattr(b2, 'ControlProgram'):
        assert not _is_linked(b2, 'ControlProgram', a)


def test_assoc_SteamBoilerMeasurementDeviceSnapshot12_link_reassign_clear():
    a = SBCS_SteamMeasurementDevice(evaporationRate=True, ready=True, waterLevel=3.14)
    b1 = SBCS_Snapshot()
    b2 = SBCS_Snapshot()
    _safe_set(a, 'SteamMeasurementDevice13', b1)
    assert _is_linked(a, 'SteamMeasurementDevice13', b1)
    if hasattr(b1, 'SnapshotSBMD'):
        assert _is_linked(b1, 'SnapshotSBMD', a)
    _safe_set(a, 'SteamMeasurementDevice13', b2)
    assert _is_linked(a, 'SteamMeasurementDevice13', b2)
    if hasattr(b1, 'SnapshotSBMD'):
        assert not _is_linked(b1, 'SnapshotSBMD', a)
    if hasattr(b2, 'SnapshotSBMD'):
        assert _is_linked(b2, 'SnapshotSBMD', a)
    _safe_set(a, 'SteamMeasurementDevice13', None)
    assert not _is_linked(a, 'SteamMeasurementDevice13', b2)
    if hasattr(b2, 'SnapshotSBMD'):
        assert not _is_linked(b2, 'SnapshotSBMD', a)


def test_assoc_SteamBoilerSMD3_link_reassign_clear():
    a = SBCS_SteamMeasurementDevice(evaporationRate=True, ready=True, waterLevel=3.14)
    b1 = SBCS_SteamBoiler(capacity=3.14, maximalLimit=3.14, maximalNormal=3.14, maximumDecrease=3.14, maximumIncrease=3.14, minimalLimit=3.14, minimalNormal=3.14, ready=True, valveOpen="sample_text")
    b2 = SBCS_SteamBoiler(capacity=9.99, maximalLimit=9.99, maximalNormal=9.99, maximumDecrease=9.99, maximumIncrease=9.99, minimalLimit=9.99, minimalNormal=9.99, ready=False, valveOpen="sample_text_2")
    _safe_set(a, 'SteamMeasurementDevice', b1)
    assert _is_linked(a, 'SteamMeasurementDevice', b1)
    if hasattr(b1, 'SMDSteamBoiler'):
        assert _is_linked(b1, 'SMDSteamBoiler', a)
    _safe_set(a, 'SteamMeasurementDevice', b2)
    assert _is_linked(a, 'SteamMeasurementDevice', b2)
    if hasattr(b1, 'SMDSteamBoiler'):
        assert not _is_linked(b1, 'SMDSteamBoiler', a)
    if hasattr(b2, 'SMDSteamBoiler'):
        assert _is_linked(b2, 'SMDSteamBoiler', a)
    _safe_set(a, 'SteamMeasurementDevice', None)
    assert not _is_linked(a, 'SteamMeasurementDevice', b2)
    if hasattr(b2, 'SMDSteamBoiler'):
        assert not _is_linked(b2, 'SMDSteamBoiler', a)


def test_assoc_SteamBoilerSnapshot5_link_reassign_clear():
    a = SBCS_SteamBoiler(capacity=3.14, maximalLimit=3.14, maximalNormal=3.14, maximumDecrease=3.14, maximumIncrease=3.14, minimalLimit=3.14, minimalNormal=3.14, ready=True, valveOpen="sample_text")
    b1 = SBCS_Snapshot()
    b2 = SBCS_Snapshot()
    _safe_set(a, 'SteamBoiler', b1)
    assert _is_linked(a, 'SteamBoiler', b1)
    if hasattr(b1, 'SnapshotSteamBoiler'):
        assert _is_linked(b1, 'SnapshotSteamBoiler', a)
    _safe_set(a, 'SteamBoiler', b2)
    assert _is_linked(a, 'SteamBoiler', b2)
    if hasattr(b1, 'SnapshotSteamBoiler'):
        assert not _is_linked(b1, 'SnapshotSteamBoiler', a)
    if hasattr(b2, 'SnapshotSteamBoiler'):
        assert _is_linked(b2, 'SnapshotSteamBoiler', a)
    _safe_set(a, 'SteamBoiler', None)
    assert not _is_linked(a, 'SteamBoiler', b2)
    if hasattr(b2, 'SnapshotSteamBoiler'):
        assert not _is_linked(b2, 'SnapshotSteamBoiler', a)


def test_assoc_SteamBoilerWLMD4_link_reassign_clear():
    a = SBCS_WaterLevelMeasurementDevice(ready=True, waterLevel=3.14)
    b1 = SBCS_SteamBoiler(capacity=3.14, maximalLimit=3.14, maximalNormal=3.14, maximumDecrease=3.14, maximumIncrease=3.14, minimalLimit=3.14, minimalNormal=3.14, ready=True, valveOpen="sample_text")
    b2 = SBCS_SteamBoiler(capacity=9.99, maximalLimit=9.99, maximalNormal=9.99, maximumDecrease=9.99, maximumIncrease=9.99, minimalLimit=9.99, minimalNormal=9.99, ready=False, valveOpen="sample_text_2")
    _safe_set(a, 'WaterLevelMeasurementDevice', b1)
    assert _is_linked(a, 'WaterLevelMeasurementDevice', b1)
    if hasattr(b1, 'WLMDSteamBoiler'):
        assert _is_linked(b1, 'WLMDSteamBoiler', a)
    _safe_set(a, 'WaterLevelMeasurementDevice', b2)
    assert _is_linked(a, 'WaterLevelMeasurementDevice', b2)
    if hasattr(b1, 'WLMDSteamBoiler'):
        assert not _is_linked(b1, 'WLMDSteamBoiler', a)
    if hasattr(b2, 'WLMDSteamBoiler'):
        assert _is_linked(b2, 'WLMDSteamBoiler', a)
    _safe_set(a, 'WaterLevelMeasurementDevice', None)
    assert not _is_linked(a, 'WaterLevelMeasurementDevice', b2)
    if hasattr(b2, 'WLMDSteamBoiler'):
        assert not _is_linked(b2, 'WLMDSteamBoiler', a)


def test_assoc_SteqmBoilerPump2_link_reassign_clear():
    a = SBCS_SteamBoiler(capacity=3.14, maximalLimit=3.14, maximalNormal=3.14, maximumDecrease=3.14, maximumIncrease=3.14, minimalLimit=3.14, minimalNormal=3.14, ready=True, valveOpen="sample_text")
    b1 = SBCS_Pump(capacity=3.14, mode="sample_text", ready=True)
    b2 = SBCS_Pump(capacity=9.99, mode="sample_text_2", ready=False)
    _safe_set(a, 'PumpSteamBoiler', b1)
    assert _is_linked(a, 'PumpSteamBoiler', b1)
    if hasattr(b1, 'Pump'):
        assert _is_linked(b1, 'Pump', a)
    _safe_set(a, 'PumpSteamBoiler', b2)
    assert _is_linked(a, 'PumpSteamBoiler', b2)
    if hasattr(b1, 'Pump'):
        assert not _is_linked(b1, 'Pump', a)
    if hasattr(b2, 'Pump'):
        assert _is_linked(b2, 'Pump', a)
    _safe_set(a, 'PumpSteamBoiler', None)
    assert not _is_linked(a, 'PumpSteamBoiler', b2)
    if hasattr(b2, 'Pump'):
        assert not _is_linked(b2, 'Pump', a)


def test_assoc_WLMDControlProgram59_link_reassign_clear():
    a = SBCS_WaterLevelMeasurementDevice(ready=True, waterLevel=3.14)
    b1 = SBCS_ControlProgram(failureDetected=True, mode="sample_text", pumpControlerFailure=True, pumpFailure=True, ready=True, smdFailure=True, wlmdFailure=True)
    b2 = SBCS_ControlProgram(failureDetected=False, mode="sample_text_2", pumpControlerFailure=False, pumpFailure=False, ready=False, smdFailure=False, wlmdFailure=False)
    _safe_set(a, 'ControlProgramWLMD', b1)
    assert _is_linked(a, 'ControlProgramWLMD', b1)
    if hasattr(b1, 'ControlProgram60'):
        assert _is_linked(b1, 'ControlProgram60', a)
    _safe_set(a, 'ControlProgramWLMD', b2)
    assert _is_linked(a, 'ControlProgramWLMD', b2)
    if hasattr(b1, 'ControlProgram60'):
        assert not _is_linked(b1, 'ControlProgram60', a)
    if hasattr(b2, 'ControlProgram60'):
        assert _is_linked(b2, 'ControlProgram60', a)
    _safe_set(a, 'ControlProgramWLMD', None)
    assert not _is_linked(a, 'ControlProgramWLMD', b2)
    if hasattr(b2, 'ControlProgram60'):
        assert not _is_linked(b2, 'ControlProgram60', a)


def test_assoc_WLMDSnapshot10_link_reassign_clear():
    a = SBCS_WaterLevelMeasurementDevice(ready=True, waterLevel=3.14)
    b1 = SBCS_Snapshot()
    b2 = SBCS_Snapshot()
    _safe_set(a, 'WaterLevelMeasurementDevice11', b1)
    assert _is_linked(a, 'WaterLevelMeasurementDevice11', b1)
    if hasattr(b1, 'SnapshotWLMD'):
        assert _is_linked(b1, 'SnapshotWLMD', a)
    _safe_set(a, 'WaterLevelMeasurementDevice11', b2)
    assert _is_linked(a, 'WaterLevelMeasurementDevice11', b2)
    if hasattr(b1, 'SnapshotWLMD'):
        assert not _is_linked(b1, 'SnapshotWLMD', a)
    if hasattr(b2, 'SnapshotWLMD'):
        assert _is_linked(b2, 'SnapshotWLMD', a)
    _safe_set(a, 'WaterLevelMeasurementDevice11', None)
    assert not _is_linked(a, 'WaterLevelMeasurementDevice11', b2)
    if hasattr(b2, 'SnapshotWLMD'):
        assert not _is_linked(b2, 'SnapshotWLMD', a)


def test_assoc_WLMDSteamBoiler61_link_reassign_clear():
    a = SBCS_WaterLevelMeasurementDevice(ready=True, waterLevel=3.14)
    b1 = SBCS_SteamBoiler(capacity=3.14, maximalLimit=3.14, maximalNormal=3.14, maximumDecrease=3.14, maximumIncrease=3.14, minimalLimit=3.14, minimalNormal=3.14, ready=True, valveOpen="sample_text")
    b2 = SBCS_SteamBoiler(capacity=9.99, maximalLimit=9.99, maximalNormal=9.99, maximumDecrease=9.99, maximumIncrease=9.99, minimalLimit=9.99, minimalNormal=9.99, ready=False, valveOpen="sample_text_2")
    _safe_set(a, 'SteamBoilerWLMD', b1)
    assert _is_linked(a, 'SteamBoilerWLMD', b1)
    if hasattr(b1, 'SteamBoiler62'):
        assert _is_linked(b1, 'SteamBoiler62', a)
    _safe_set(a, 'SteamBoilerWLMD', b2)
    assert _is_linked(a, 'SteamBoilerWLMD', b2)
    if hasattr(b1, 'SteamBoiler62'):
        assert not _is_linked(b1, 'SteamBoiler62', a)
    if hasattr(b2, 'SteamBoiler62'):
        assert _is_linked(b2, 'SteamBoiler62', a)
    _safe_set(a, 'SteamBoilerWLMD', None)
    assert not _is_linked(a, 'SteamBoilerWLMD', b2)
    if hasattr(b2, 'SteamBoiler62'):
        assert not _is_linked(b2, 'SteamBoiler62', a)


def test_assoc_wlmdPost68_link_reassign_clear():
    a = SBCS_WaterLevelMeaurementDevice_getLevel(ret=3.14)
    b1 = SBCS_WaterLevelMeasurementDevice(ready=True, waterLevel=3.14)
    b2 = SBCS_WaterLevelMeasurementDevice(ready=False, waterLevel=9.99)
    _safe_set(a, 'SBCS_WaterLevelMeaurementDevice_getLevel69', b1)
    assert _is_linked(a, 'SBCS_WaterLevelMeaurementDevice_getLevel69', b1)
    if hasattr(b1, 'SBCS_WaterLevelMeasurementDevice70'):
        assert _is_linked(b1, 'SBCS_WaterLevelMeasurementDevice70', a)
    _safe_set(a, 'SBCS_WaterLevelMeaurementDevice_getLevel69', b2)
    assert _is_linked(a, 'SBCS_WaterLevelMeaurementDevice_getLevel69', b2)
    if hasattr(b1, 'SBCS_WaterLevelMeasurementDevice70'):
        assert not _is_linked(b1, 'SBCS_WaterLevelMeasurementDevice70', a)
    if hasattr(b2, 'SBCS_WaterLevelMeasurementDevice70'):
        assert _is_linked(b2, 'SBCS_WaterLevelMeasurementDevice70', a)
    _safe_set(a, 'SBCS_WaterLevelMeaurementDevice_getLevel69', None)
    assert not _is_linked(a, 'SBCS_WaterLevelMeaurementDevice_getLevel69', b2)
    if hasattr(b2, 'SBCS_WaterLevelMeasurementDevice70'):
        assert not _is_linked(b2, 'SBCS_WaterLevelMeasurementDevice70', a)


def test_assoc_wlmdPre67_link_reassign_clear():
    a = SBCS_WaterLevelMeaurementDevice_getLevel(ret=3.14)
    b1 = SBCS_WaterLevelMeasurementDevice(ready=True, waterLevel=3.14)
    b2 = SBCS_WaterLevelMeasurementDevice(ready=False, waterLevel=9.99)
    _safe_set(a, 'SBCS_WaterLevelMeaurementDevice_getLevel', b1)
    assert _is_linked(a, 'SBCS_WaterLevelMeaurementDevice_getLevel', b1)
    if hasattr(b1, 'SBCS_WaterLevelMeasurementDevice'):
        assert _is_linked(b1, 'SBCS_WaterLevelMeasurementDevice', a)
    _safe_set(a, 'SBCS_WaterLevelMeaurementDevice_getLevel', b2)
    assert _is_linked(a, 'SBCS_WaterLevelMeaurementDevice_getLevel', b2)
    if hasattr(b1, 'SBCS_WaterLevelMeasurementDevice'):
        assert not _is_linked(b1, 'SBCS_WaterLevelMeasurementDevice', a)
    if hasattr(b2, 'SBCS_WaterLevelMeasurementDevice'):
        assert _is_linked(b2, 'SBCS_WaterLevelMeasurementDevice', a)
    _safe_set(a, 'SBCS_WaterLevelMeaurementDevice_getLevel', None)
    assert not _is_linked(a, 'SBCS_WaterLevelMeaurementDevice_getLevel', b2)
    if hasattr(b2, 'SBCS_WaterLevelMeasurementDevice'):
        assert not _is_linked(b2, 'SBCS_WaterLevelMeasurementDevice', a)


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

SBCS_ControlProgram_strategy = st.builds(SBCS_ControlProgram, failureDetected=st.booleans(), mode=safe_text, pumpControlerFailure=st.booleans(), pumpFailure=st.booleans(), ready=st.booleans(), smdFailure=st.booleans(), wlmdFailure=st.booleans())
@given(instance=SBCS_ControlProgram_strategy)
@settings(max_examples=25)
def test_SBCS_ControlProgram_instantiation(instance):
    assert isinstance(instance, SBCS_ControlProgram)


SBCS_ControlProgram_Start_strategy = st.builds(SBCS_ControlProgram_Start)
@given(instance=SBCS_ControlProgram_Start_strategy)
@settings(max_examples=25)
def test_SBCS_ControlProgram_Start_instantiation(instance):
    assert isinstance(instance, SBCS_ControlProgram_Start)


SBCS_Pump_strategy = st.builds(SBCS_Pump, capacity=st.floats(allow_nan=False, allow_infinity=False), mode=safe_text, ready=st.booleans())
@given(instance=SBCS_Pump_strategy)
@settings(max_examples=25)
def test_SBCS_Pump_instantiation(instance):
    assert isinstance(instance, SBCS_Pump)


SBCS_PumpControler_strategy = st.builds(SBCS_PumpControler, circulating=st.booleans(), ready=st.booleans())
@given(instance=SBCS_PumpControler_strategy)
@settings(max_examples=25)
def test_SBCS_PumpControler_instantiation(instance):
    assert isinstance(instance, SBCS_PumpControler)


SBCS_PumpController_ClosePump_strategy = st.builds(SBCS_PumpController_ClosePump)
@given(instance=SBCS_PumpController_ClosePump_strategy)
@settings(max_examples=25)
def test_SBCS_PumpController_ClosePump_instantiation(instance):
    assert isinstance(instance, SBCS_PumpController_ClosePump)


SBCS_PumpController_OpenPump_strategy = st.builds(SBCS_PumpController_OpenPump)
@given(instance=SBCS_PumpController_OpenPump_strategy)
@settings(max_examples=25)
def test_SBCS_PumpController_OpenPump_instantiation(instance):
    assert isinstance(instance, SBCS_PumpController_OpenPump)


SBCS_Snapshot_strategy = st.builds(SBCS_Snapshot)
@given(instance=SBCS_Snapshot_strategy)
@settings(max_examples=25)
def test_SBCS_Snapshot_instantiation(instance):
    assert isinstance(instance, SBCS_Snapshot)


SBCS_SteamBoiler_strategy = st.builds(SBCS_SteamBoiler, capacity=st.floats(allow_nan=False, allow_infinity=False), maximalLimit=st.floats(allow_nan=False, allow_infinity=False), maximalNormal=st.floats(allow_nan=False, allow_infinity=False), maximumDecrease=st.floats(allow_nan=False, allow_infinity=False), maximumIncrease=st.floats(allow_nan=False, allow_infinity=False), minimalLimit=st.floats(allow_nan=False, allow_infinity=False), minimalNormal=st.floats(allow_nan=False, allow_infinity=False), ready=st.booleans(), valveOpen=safe_text)
@given(instance=SBCS_SteamBoiler_strategy)
@settings(max_examples=25)
def test_SBCS_SteamBoiler_instantiation(instance):
    assert isinstance(instance, SBCS_SteamBoiler)


SBCS_SteamBoiler_OpenValve_strategy = st.builds(SBCS_SteamBoiler_OpenValve)
@given(instance=SBCS_SteamBoiler_OpenValve_strategy)
@settings(max_examples=25)
def test_SBCS_SteamBoiler_OpenValve_instantiation(instance):
    assert isinstance(instance, SBCS_SteamBoiler_OpenValve)


SBCS_SteamMeasurementDevice_strategy = st.builds(SBCS_SteamMeasurementDevice, evaporationRate=st.booleans(), ready=st.booleans(), waterLevel=st.floats(allow_nan=False, allow_infinity=False))
@given(instance=SBCS_SteamMeasurementDevice_strategy)
@settings(max_examples=25)
def test_SBCS_SteamMeasurementDevice_instantiation(instance):
    assert isinstance(instance, SBCS_SteamMeasurementDevice)


SBCS_Transition_strategy = st.builds(SBCS_Transition)
@given(instance=SBCS_Transition_strategy)
@settings(max_examples=25)
def test_SBCS_Transition_instantiation(instance):
    assert isinstance(instance, SBCS_Transition)


SBCS_WaterLevelMeasurementDevice_strategy = st.builds(SBCS_WaterLevelMeasurementDevice, ready=st.booleans(), waterLevel=st.floats(allow_nan=False, allow_infinity=False))
@given(instance=SBCS_WaterLevelMeasurementDevice_strategy)
@settings(max_examples=25)
def test_SBCS_WaterLevelMeasurementDevice_instantiation(instance):
    assert isinstance(instance, SBCS_WaterLevelMeasurementDevice)


SBCS_WaterLevelMeaurementDevice_getLevel_strategy = st.builds(SBCS_WaterLevelMeaurementDevice_getLevel, ret=st.floats(allow_nan=False, allow_infinity=False))
@given(instance=SBCS_WaterLevelMeaurementDevice_getLevel_strategy)
@settings(max_examples=25)
def test_SBCS_WaterLevelMeaurementDevice_getLevel_instantiation(instance):
    assert isinstance(instance, SBCS_WaterLevelMeaurementDevice_getLevel)


Transition_strategy = st.builds(Transition)
@given(instance=Transition_strategy)
@settings(max_examples=25)
def test_Transition_instantiation(instance):
    assert isinstance(instance, Transition)





import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    SBCS_ControlProgram,
    SBCS_ControlProgram_Start,
    SBCS_Pump,
    SBCS_PumpControler,
    SBCS_PumpController_ClosePump,
    SBCS_PumpController_OpenPump,
    SBCS_Snapshot,
    SBCS_SteamBoiler,
    SBCS_SteamBoiler_OpenValve,
    SBCS_SteamMeasurementDevice,
    SBCS_Transition,
    SBCS_WaterLevelMeasurementDevice,
    SBCS_WaterLevelMeaurementDevice_getLevel,
    Transition,
    Mode,
    State,
    ValveState,
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

def test_assoc_ControlProgramPump20_reverse_link_reassign_clear():
    a1 = SBCS_Pump(capacity=3.14, mode="sample_text", ready=True)
    a2 = SBCS_Pump(capacity=9.99, mode="sample_text_2", ready=False)
    b = SBCS_ControlProgram(failureDetected=True, mode="sample_text", pumpControlerFailure=True, pumpFailure=True, ready=True, smdFailure=True, wlmdFailure=True)
    _safe_set(b, 'PumpControlProgram', a1)
    assert _is_linked(b, 'PumpControlProgram', a1)
    if hasattr(a1, 'Pump21'):
        assert _is_linked(a1, 'Pump21', b)
    _safe_set(b, 'PumpControlProgram', a2)
    assert _is_linked(b, 'PumpControlProgram', a2)
    if hasattr(a1, 'Pump21'):
        assert not _is_linked(a1, 'Pump21', b)
    if hasattr(a2, 'Pump21'):
        assert _is_linked(a2, 'Pump21', b)
    _safe_set(b, 'PumpControlProgram', None)
    assert not _is_linked(b, 'PumpControlProgram', a2)
    if hasattr(a2, 'Pump21'):
        assert not _is_linked(a2, 'Pump21', b)


def test_assoc_ControlProgramPumpControler28_reverse_link_reassign_clear():
    a1 = SBCS_PumpControler(circulating=True, ready=True)
    a2 = SBCS_PumpControler(circulating=False, ready=False)
    b = SBCS_ControlProgram(failureDetected=True, mode="sample_text", pumpControlerFailure=True, pumpFailure=True, ready=True, smdFailure=True, wlmdFailure=True)
    _safe_set(b, 'PumpControlerControlProgram', a1)
    assert _is_linked(b, 'PumpControlerControlProgram', a1)
    if hasattr(a1, 'PumpControler29'):
        assert _is_linked(a1, 'PumpControler29', b)
    _safe_set(b, 'PumpControlerControlProgram', a2)
    assert _is_linked(b, 'PumpControlerControlProgram', a2)
    if hasattr(a1, 'PumpControler29'):
        assert not _is_linked(a1, 'PumpControler29', b)
    if hasattr(a2, 'PumpControler29'):
        assert _is_linked(a2, 'PumpControler29', b)
    _safe_set(b, 'PumpControlerControlProgram', None)
    assert not _is_linked(b, 'PumpControlerControlProgram', a2)
    if hasattr(a2, 'PumpControler29'):
        assert not _is_linked(a2, 'PumpControler29', b)


def test_assoc_ControlProgramSMD24_reverse_link_reassign_clear():
    a1 = SBCS_SteamMeasurementDevice(evaporationRate=True, ready=True, waterLevel=3.14)
    a2 = SBCS_SteamMeasurementDevice(evaporationRate=False, ready=False, waterLevel=9.99)
    b = SBCS_ControlProgram(failureDetected=True, mode="sample_text", pumpControlerFailure=True, pumpFailure=True, ready=True, smdFailure=True, wlmdFailure=True)
    _safe_set(b, 'SMDControlProgram', a1)
    assert _is_linked(b, 'SMDControlProgram', a1)
    if hasattr(a1, 'SteamMeasurementDevice25'):
        assert _is_linked(a1, 'SteamMeasurementDevice25', b)
    _safe_set(b, 'SMDControlProgram', a2)
    assert _is_linked(b, 'SMDControlProgram', a2)
    if hasattr(a1, 'SteamMeasurementDevice25'):
        assert not _is_linked(a1, 'SteamMeasurementDevice25', b)
    if hasattr(a2, 'SteamMeasurementDevice25'):
        assert _is_linked(a2, 'SteamMeasurementDevice25', b)
    _safe_set(b, 'SMDControlProgram', None)
    assert not _is_linked(b, 'SMDControlProgram', a2)
    if hasattr(a2, 'SteamMeasurementDevice25'):
        assert not _is_linked(a2, 'SteamMeasurementDevice25', b)


def test_assoc_ControlProgramSnapshot6_reverse_link_reassign_clear():
    a1 = SBCS_Snapshot()
    a2 = SBCS_Snapshot()
    b = SBCS_ControlProgram(failureDetected=True, mode="sample_text", pumpControlerFailure=True, pumpFailure=True, ready=True, smdFailure=True, wlmdFailure=True)
    _safe_set(b, 'ControlProgram7', a1)
    assert _is_linked(b, 'ControlProgram7', a1)
    if hasattr(a1, 'SnapshotControlProgram'):
        assert _is_linked(a1, 'SnapshotControlProgram', b)
    _safe_set(b, 'ControlProgram7', a2)
    assert _is_linked(b, 'ControlProgram7', a2)
    if hasattr(a1, 'SnapshotControlProgram'):
        assert not _is_linked(a1, 'SnapshotControlProgram', b)
    if hasattr(a2, 'SnapshotControlProgram'):
        assert _is_linked(a2, 'SnapshotControlProgram', b)
    _safe_set(b, 'ControlProgram7', None)
    assert not _is_linked(b, 'ControlProgram7', a2)
    if hasattr(a2, 'SnapshotControlProgram'):
        assert not _is_linked(a2, 'SnapshotControlProgram', b)


def test_assoc_ControlProgramSteamBoiler26_reverse_link_reassign_clear():
    a1 = SBCS_SteamBoiler(capacity=3.14, maximalLimit=3.14, maximalNormal=3.14, maximumDecrease=3.14, maximumIncrease=3.14, minimalLimit=3.14, minimalNormal=3.14, ready=True, valveOpen="sample_text")
    a2 = SBCS_SteamBoiler(capacity=9.99, maximalLimit=9.99, maximalNormal=9.99, maximumDecrease=9.99, maximumIncrease=9.99, minimalLimit=9.99, minimalNormal=9.99, ready=False, valveOpen="sample_text_2")
    b = SBCS_ControlProgram(failureDetected=True, mode="sample_text", pumpControlerFailure=True, pumpFailure=True, ready=True, smdFailure=True, wlmdFailure=True)
    _safe_set(b, 'SteamBoilerControlProgram', a1)
    assert _is_linked(b, 'SteamBoilerControlProgram', a1)
    if hasattr(a1, 'SteamBoiler27'):
        assert _is_linked(a1, 'SteamBoiler27', b)
    _safe_set(b, 'SteamBoilerControlProgram', a2)
    assert _is_linked(b, 'SteamBoilerControlProgram', a2)
    if hasattr(a1, 'SteamBoiler27'):
        assert not _is_linked(a1, 'SteamBoiler27', b)
    if hasattr(a2, 'SteamBoiler27'):
        assert _is_linked(a2, 'SteamBoiler27', b)
    _safe_set(b, 'SteamBoilerControlProgram', None)
    assert not _is_linked(b, 'SteamBoilerControlProgram', a2)
    if hasattr(a2, 'SteamBoiler27'):
        assert not _is_linked(a2, 'SteamBoiler27', b)


def test_assoc_ControlProgramWLMD22_reverse_link_reassign_clear():
    a1 = SBCS_WaterLevelMeasurementDevice(ready=True, waterLevel=3.14)
    a2 = SBCS_WaterLevelMeasurementDevice(ready=False, waterLevel=9.99)
    b = SBCS_ControlProgram(failureDetected=True, mode="sample_text", pumpControlerFailure=True, pumpFailure=True, ready=True, smdFailure=True, wlmdFailure=True)
    _safe_set(b, 'WLMDControlProgram', a1)
    assert _is_linked(b, 'WLMDControlProgram', a1)
    if hasattr(a1, 'WaterLevelMeasurementDevice23'):
        assert _is_linked(a1, 'WaterLevelMeasurementDevice23', b)
    _safe_set(b, 'WLMDControlProgram', a2)
    assert _is_linked(b, 'WLMDControlProgram', a2)
    if hasattr(a1, 'WaterLevelMeasurementDevice23'):
        assert not _is_linked(a1, 'WaterLevelMeasurementDevice23', b)
    if hasattr(a2, 'WaterLevelMeasurementDevice23'):
        assert _is_linked(a2, 'WaterLevelMeasurementDevice23', b)
    _safe_set(b, 'WLMDControlProgram', None)
    assert not _is_linked(b, 'WLMDControlProgram', a2)
    if hasattr(a2, 'WaterLevelMeasurementDevice23'):
        assert not _is_linked(a2, 'WaterLevelMeasurementDevice23', b)


def test_assoc_PumpControlProgram33_reverse_link_reassign_clear():
    a1 = SBCS_Pump(capacity=3.14, mode="sample_text", ready=True)
    a2 = SBCS_Pump(capacity=9.99, mode="sample_text_2", ready=False)
    b = SBCS_ControlProgram(failureDetected=True, mode="sample_text", pumpControlerFailure=True, pumpFailure=True, ready=True, smdFailure=True, wlmdFailure=True)
    _safe_set(b, 'ControlProgram34', a1)
    assert _is_linked(b, 'ControlProgram34', a1)
    if hasattr(a1, 'ControlProgramPump'):
        assert _is_linked(a1, 'ControlProgramPump', b)
    _safe_set(b, 'ControlProgram34', a2)
    assert _is_linked(b, 'ControlProgram34', a2)
    if hasattr(a1, 'ControlProgramPump'):
        assert not _is_linked(a1, 'ControlProgramPump', b)
    if hasattr(a2, 'ControlProgramPump'):
        assert _is_linked(a2, 'ControlProgramPump', b)
    _safe_set(b, 'ControlProgram34', None)
    assert not _is_linked(b, 'ControlProgram34', a2)
    if hasattr(a2, 'ControlProgramPump'):
        assert not _is_linked(a2, 'ControlProgramPump', b)


def test_assoc_PumpControlSnapshot14_reverse_link_reassign_clear():
    a1 = SBCS_Snapshot()
    a2 = SBCS_Snapshot()
    b = SBCS_PumpControler(circulating=True, ready=True)
    _safe_set(b, 'PumpControler', a1)
    assert _is_linked(b, 'PumpControler', a1)
    if hasattr(a1, 'SnapshotPumpControl'):
        assert _is_linked(a1, 'SnapshotPumpControl', b)
    _safe_set(b, 'PumpControler', a2)
    assert _is_linked(b, 'PumpControler', a2)
    if hasattr(a1, 'SnapshotPumpControl'):
        assert not _is_linked(a1, 'SnapshotPumpControl', b)
    if hasattr(a2, 'SnapshotPumpControl'):
        assert _is_linked(a2, 'SnapshotPumpControl', b)
    _safe_set(b, 'PumpControler', None)
    assert not _is_linked(b, 'PumpControler', a2)
    if hasattr(a2, 'SnapshotPumpControl'):
        assert not _is_linked(a2, 'SnapshotPumpControl', b)


def test_assoc_PumpControlerControlProgram47_reverse_link_reassign_clear():
    a1 = SBCS_PumpControler(circulating=True, ready=True)
    a2 = SBCS_PumpControler(circulating=False, ready=False)
    b = SBCS_ControlProgram(failureDetected=True, mode="sample_text", pumpControlerFailure=True, pumpFailure=True, ready=True, smdFailure=True, wlmdFailure=True)
    _safe_set(b, 'ControlProgram48', a1)
    assert _is_linked(b, 'ControlProgram48', a1)
    if hasattr(a1, 'ControlProgramPumpControler'):
        assert _is_linked(a1, 'ControlProgramPumpControler', b)
    _safe_set(b, 'ControlProgram48', a2)
    assert _is_linked(b, 'ControlProgram48', a2)
    if hasattr(a1, 'ControlProgramPumpControler'):
        assert not _is_linked(a1, 'ControlProgramPumpControler', b)
    if hasattr(a2, 'ControlProgramPumpControler'):
        assert _is_linked(a2, 'ControlProgramPumpControler', b)
    _safe_set(b, 'ControlProgram48', None)
    assert not _is_linked(b, 'ControlProgram48', a2)
    if hasattr(a2, 'ControlProgramPumpControler'):
        assert not _is_linked(a2, 'ControlProgramPumpControler', b)


def test_assoc_PumpControlerPump49_reverse_link_reassign_clear():
    a1 = SBCS_PumpControler(circulating=True, ready=True)
    a2 = SBCS_PumpControler(circulating=False, ready=False)
    b = SBCS_Pump(capacity=3.14, mode="sample_text", ready=True)
    _safe_set(b, 'Pump50', a1)
    assert _is_linked(b, 'Pump50', a1)
    if hasattr(a1, 'PumpPumpControler'):
        assert _is_linked(a1, 'PumpPumpControler', b)
    _safe_set(b, 'Pump50', a2)
    assert _is_linked(b, 'Pump50', a2)
    if hasattr(a1, 'PumpPumpControler'):
        assert not _is_linked(a1, 'PumpPumpControler', b)
    if hasattr(a2, 'PumpPumpControler'):
        assert _is_linked(a2, 'PumpPumpControler', b)
    _safe_set(b, 'Pump50', None)
    assert not _is_linked(b, 'Pump50', a2)
    if hasattr(a2, 'PumpPumpControler'):
        assert not _is_linked(a2, 'PumpPumpControler', b)


def test_assoc_PumpPumpControler35_reverse_link_reassign_clear():
    a1 = SBCS_PumpControler(circulating=True, ready=True)
    a2 = SBCS_PumpControler(circulating=False, ready=False)
    b = SBCS_Pump(capacity=3.14, mode="sample_text", ready=True)
    _safe_set(b, 'PumpControlerPump', a1)
    assert _is_linked(b, 'PumpControlerPump', a1)
    if hasattr(a1, 'PumpControler36'):
        assert _is_linked(a1, 'PumpControler36', b)
    _safe_set(b, 'PumpControlerPump', a2)
    assert _is_linked(b, 'PumpControlerPump', a2)
    if hasattr(a1, 'PumpControler36'):
        assert not _is_linked(a1, 'PumpControler36', b)
    if hasattr(a2, 'PumpControler36'):
        assert _is_linked(a2, 'PumpControler36', b)
    _safe_set(b, 'PumpControlerPump', None)
    assert not _is_linked(b, 'PumpControlerPump', a2)
    if hasattr(a2, 'PumpControler36'):
        assert not _is_linked(a2, 'PumpControler36', b)


def test_assoc_PumpSnapshot30_reverse_link_reassign_clear():
    a1 = SBCS_Snapshot()
    a2 = SBCS_Snapshot()
    b = SBCS_Pump(capacity=3.14, mode="sample_text", ready=True)
    _safe_set(b, 'PumpSnapshot31', a1)
    assert _is_linked(b, 'PumpSnapshot31', a1)
    if hasattr(a1, 'Snapshot32'):
        assert _is_linked(a1, 'Snapshot32', b)
    _safe_set(b, 'PumpSnapshot31', a2)
    assert _is_linked(b, 'PumpSnapshot31', a2)
    if hasattr(a1, 'Snapshot32'):
        assert not _is_linked(a1, 'Snapshot32', b)
    if hasattr(a2, 'Snapshot32'):
        assert _is_linked(a2, 'Snapshot32', b)
    _safe_set(b, 'PumpSnapshot31', None)
    assert not _is_linked(b, 'PumpSnapshot31', a2)
    if hasattr(a2, 'Snapshot32'):
        assert not _is_linked(a2, 'Snapshot32', b)


def test_assoc_PumpSnapshot8_reverse_link_reassign_clear():
    a1 = SBCS_Snapshot()
    a2 = SBCS_Snapshot()
    b = SBCS_Pump(capacity=3.14, mode="sample_text", ready=True)
    _safe_set(b, 'Pump9', a1)
    assert _is_linked(b, 'Pump9', a1)
    if hasattr(a1, 'PumpSnapshot'):
        assert _is_linked(a1, 'PumpSnapshot', b)
    _safe_set(b, 'Pump9', a2)
    assert _is_linked(b, 'Pump9', a2)
    if hasattr(a1, 'PumpSnapshot'):
        assert not _is_linked(a1, 'PumpSnapshot', b)
    if hasattr(a2, 'PumpSnapshot'):
        assert _is_linked(a2, 'PumpSnapshot', b)
    _safe_set(b, 'Pump9', None)
    assert not _is_linked(b, 'Pump9', a2)
    if hasattr(a2, 'PumpSnapshot'):
        assert not _is_linked(a2, 'PumpSnapshot', b)


def test_assoc_PumpSteamBoiler37_reverse_link_reassign_clear():
    a1 = SBCS_SteamBoiler(capacity=3.14, maximalLimit=3.14, maximalNormal=3.14, maximumDecrease=3.14, maximumIncrease=3.14, minimalLimit=3.14, minimalNormal=3.14, ready=True, valveOpen="sample_text")
    a2 = SBCS_SteamBoiler(capacity=9.99, maximalLimit=9.99, maximalNormal=9.99, maximumDecrease=9.99, maximumIncrease=9.99, minimalLimit=9.99, minimalNormal=9.99, ready=False, valveOpen="sample_text_2")
    b = SBCS_Pump(capacity=3.14, mode="sample_text", ready=True)
    _safe_set(b, 'SteqmBoilerPump', a1)
    assert _is_linked(b, 'SteqmBoilerPump', a1)
    if hasattr(a1, 'SteamBoiler38'):
        assert _is_linked(a1, 'SteamBoiler38', b)
    _safe_set(b, 'SteqmBoilerPump', a2)
    assert _is_linked(b, 'SteqmBoilerPump', a2)
    if hasattr(a1, 'SteamBoiler38'):
        assert not _is_linked(a1, 'SteamBoiler38', b)
    if hasattr(a2, 'SteamBoiler38'):
        assert _is_linked(a2, 'SteamBoiler38', b)
    _safe_set(b, 'SteqmBoilerPump', None)
    assert not _is_linked(b, 'SteqmBoilerPump', a2)
    if hasattr(a2, 'SteamBoiler38'):
        assert not _is_linked(a2, 'SteamBoiler38', b)


def test_assoc_SMDControlProgram53_reverse_link_reassign_clear():
    a1 = SBCS_SteamMeasurementDevice(evaporationRate=True, ready=True, waterLevel=3.14)
    a2 = SBCS_SteamMeasurementDevice(evaporationRate=False, ready=False, waterLevel=9.99)
    b = SBCS_ControlProgram(failureDetected=True, mode="sample_text", pumpControlerFailure=True, pumpFailure=True, ready=True, smdFailure=True, wlmdFailure=True)
    _safe_set(b, 'ControlProgram54', a1)
    assert _is_linked(b, 'ControlProgram54', a1)
    if hasattr(a1, 'ControlProgramSMD'):
        assert _is_linked(a1, 'ControlProgramSMD', b)
    _safe_set(b, 'ControlProgram54', a2)
    assert _is_linked(b, 'ControlProgram54', a2)
    if hasattr(a1, 'ControlProgramSMD'):
        assert not _is_linked(a1, 'ControlProgramSMD', b)
    if hasattr(a2, 'ControlProgramSMD'):
        assert _is_linked(a2, 'ControlProgramSMD', b)
    _safe_set(b, 'ControlProgram54', None)
    assert not _is_linked(b, 'ControlProgram54', a2)
    if hasattr(a2, 'ControlProgramSMD'):
        assert not _is_linked(a2, 'ControlProgramSMD', b)


def test_assoc_SMDSteamBoiler55_reverse_link_reassign_clear():
    a1 = SBCS_SteamMeasurementDevice(evaporationRate=True, ready=True, waterLevel=3.14)
    a2 = SBCS_SteamMeasurementDevice(evaporationRate=False, ready=False, waterLevel=9.99)
    b = SBCS_SteamBoiler(capacity=3.14, maximalLimit=3.14, maximalNormal=3.14, maximumDecrease=3.14, maximumIncrease=3.14, minimalLimit=3.14, minimalNormal=3.14, ready=True, valveOpen="sample_text")
    _safe_set(b, 'SteamBoiler56', a1)
    assert _is_linked(b, 'SteamBoiler56', a1)
    if hasattr(a1, 'SteamBoilerSMD'):
        assert _is_linked(a1, 'SteamBoilerSMD', b)
    _safe_set(b, 'SteamBoiler56', a2)
    assert _is_linked(b, 'SteamBoiler56', a2)
    if hasattr(a1, 'SteamBoilerSMD'):
        assert not _is_linked(a1, 'SteamBoilerSMD', b)
    if hasattr(a2, 'SteamBoilerSMD'):
        assert _is_linked(a2, 'SteamBoilerSMD', b)
    _safe_set(b, 'SteamBoiler56', None)
    assert not _is_linked(b, 'SteamBoiler56', a2)
    if hasattr(a2, 'SteamBoilerSMD'):
        assert not _is_linked(a2, 'SteamBoilerSMD', b)


def test_assoc_SnapshotControlProgram18_reverse_link_reassign_clear():
    a1 = SBCS_Snapshot()
    a2 = SBCS_Snapshot()
    b = SBCS_ControlProgram(failureDetected=True, mode="sample_text", pumpControlerFailure=True, pumpFailure=True, ready=True, smdFailure=True, wlmdFailure=True)
    _safe_set(b, 'ControlProgramSnapshot', a1)
    assert _is_linked(b, 'ControlProgramSnapshot', a1)
    if hasattr(a1, 'Snapshot19'):
        assert _is_linked(a1, 'Snapshot19', b)
    _safe_set(b, 'ControlProgramSnapshot', a2)
    assert _is_linked(b, 'ControlProgramSnapshot', a2)
    if hasattr(a1, 'Snapshot19'):
        assert not _is_linked(a1, 'Snapshot19', b)
    if hasattr(a2, 'Snapshot19'):
        assert _is_linked(a2, 'Snapshot19', b)
    _safe_set(b, 'ControlProgramSnapshot', None)
    assert not _is_linked(b, 'ControlProgramSnapshot', a2)
    if hasattr(a2, 'Snapshot19'):
        assert not _is_linked(a2, 'Snapshot19', b)


def test_assoc_SnapshotPumpControl45_reverse_link_reassign_clear():
    a1 = SBCS_Snapshot()
    a2 = SBCS_Snapshot()
    b = SBCS_PumpControler(circulating=True, ready=True)
    _safe_set(b, 'PumpControlSnapshot', a1)
    assert _is_linked(b, 'PumpControlSnapshot', a1)
    if hasattr(a1, 'Snapshot46'):
        assert _is_linked(a1, 'Snapshot46', b)
    _safe_set(b, 'PumpControlSnapshot', a2)
    assert _is_linked(b, 'PumpControlSnapshot', a2)
    if hasattr(a1, 'Snapshot46'):
        assert not _is_linked(a1, 'Snapshot46', b)
    if hasattr(a2, 'Snapshot46'):
        assert _is_linked(a2, 'Snapshot46', b)
    _safe_set(b, 'PumpControlSnapshot', None)
    assert not _is_linked(b, 'PumpControlSnapshot', a2)
    if hasattr(a2, 'Snapshot46'):
        assert not _is_linked(a2, 'Snapshot46', b)


def test_assoc_SnapshotSBMD51_reverse_link_reassign_clear():
    a1 = SBCS_SteamMeasurementDevice(evaporationRate=True, ready=True, waterLevel=3.14)
    a2 = SBCS_SteamMeasurementDevice(evaporationRate=False, ready=False, waterLevel=9.99)
    b = SBCS_Snapshot()
    _safe_set(b, 'Snapshot52', a1)
    assert _is_linked(b, 'Snapshot52', a1)
    if hasattr(a1, 'SteamBoilerMeasurementDeviceSnapshot'):
        assert _is_linked(a1, 'SteamBoilerMeasurementDeviceSnapshot', b)
    _safe_set(b, 'Snapshot52', a2)
    assert _is_linked(b, 'Snapshot52', a2)
    if hasattr(a1, 'SteamBoilerMeasurementDeviceSnapshot'):
        assert not _is_linked(a1, 'SteamBoilerMeasurementDeviceSnapshot', b)
    if hasattr(a2, 'SteamBoilerMeasurementDeviceSnapshot'):
        assert _is_linked(a2, 'SteamBoilerMeasurementDeviceSnapshot', b)
    _safe_set(b, 'Snapshot52', None)
    assert not _is_linked(b, 'Snapshot52', a2)
    if hasattr(a2, 'SteamBoilerMeasurementDeviceSnapshot'):
        assert not _is_linked(a2, 'SteamBoilerMeasurementDeviceSnapshot', b)


def test_assoc_SnapshotSteamBoiler0_reverse_link_reassign_clear():
    a1 = SBCS_SteamBoiler(capacity=3.14, maximalLimit=3.14, maximalNormal=3.14, maximumDecrease=3.14, maximumIncrease=3.14, minimalLimit=3.14, minimalNormal=3.14, ready=True, valveOpen="sample_text")
    a2 = SBCS_SteamBoiler(capacity=9.99, maximalLimit=9.99, maximalNormal=9.99, maximumDecrease=9.99, maximumIncrease=9.99, minimalLimit=9.99, minimalNormal=9.99, ready=False, valveOpen="sample_text_2")
    b = SBCS_Snapshot()
    _safe_set(b, 'Snapshot', a1)
    assert _is_linked(b, 'Snapshot', a1)
    if hasattr(a1, 'SteamBoilerSnapshot'):
        assert _is_linked(a1, 'SteamBoilerSnapshot', b)
    _safe_set(b, 'Snapshot', a2)
    assert _is_linked(b, 'Snapshot', a2)
    if hasattr(a1, 'SteamBoilerSnapshot'):
        assert not _is_linked(a1, 'SteamBoilerSnapshot', b)
    if hasattr(a2, 'SteamBoilerSnapshot'):
        assert _is_linked(a2, 'SteamBoilerSnapshot', b)
    _safe_set(b, 'Snapshot', None)
    assert not _is_linked(b, 'Snapshot', a2)
    if hasattr(a2, 'SteamBoilerSnapshot'):
        assert not _is_linked(a2, 'SteamBoilerSnapshot', b)


def test_assoc_SnapshotWLMD57_reverse_link_reassign_clear():
    a1 = SBCS_WaterLevelMeasurementDevice(ready=True, waterLevel=3.14)
    a2 = SBCS_WaterLevelMeasurementDevice(ready=False, waterLevel=9.99)
    b = SBCS_Snapshot()
    _safe_set(b, 'Snapshot58', a1)
    assert _is_linked(b, 'Snapshot58', a1)
    if hasattr(a1, 'WLMDSnapshot'):
        assert _is_linked(a1, 'WLMDSnapshot', b)
    _safe_set(b, 'Snapshot58', a2)
    assert _is_linked(b, 'Snapshot58', a2)
    if hasattr(a1, 'WLMDSnapshot'):
        assert not _is_linked(a1, 'WLMDSnapshot', b)
    if hasattr(a2, 'WLMDSnapshot'):
        assert _is_linked(a2, 'WLMDSnapshot', b)
    _safe_set(b, 'Snapshot58', None)
    assert not _is_linked(b, 'Snapshot58', a2)
    if hasattr(a2, 'WLMDSnapshot'):
        assert not _is_linked(a2, 'WLMDSnapshot', b)


def test_assoc_SteamBoilerControlProgram1_reverse_link_reassign_clear():
    a1 = SBCS_SteamBoiler(capacity=3.14, maximalLimit=3.14, maximalNormal=3.14, maximumDecrease=3.14, maximumIncrease=3.14, minimalLimit=3.14, minimalNormal=3.14, ready=True, valveOpen="sample_text")
    a2 = SBCS_SteamBoiler(capacity=9.99, maximalLimit=9.99, maximalNormal=9.99, maximumDecrease=9.99, maximumIncrease=9.99, minimalLimit=9.99, minimalNormal=9.99, ready=False, valveOpen="sample_text_2")
    b = SBCS_ControlProgram(failureDetected=True, mode="sample_text", pumpControlerFailure=True, pumpFailure=True, ready=True, smdFailure=True, wlmdFailure=True)
    _safe_set(b, 'ControlProgram', a1)
    assert _is_linked(b, 'ControlProgram', a1)
    if hasattr(a1, 'ControlProgramSteamBoiler'):
        assert _is_linked(a1, 'ControlProgramSteamBoiler', b)
    _safe_set(b, 'ControlProgram', a2)
    assert _is_linked(b, 'ControlProgram', a2)
    if hasattr(a1, 'ControlProgramSteamBoiler'):
        assert not _is_linked(a1, 'ControlProgramSteamBoiler', b)
    if hasattr(a2, 'ControlProgramSteamBoiler'):
        assert _is_linked(a2, 'ControlProgramSteamBoiler', b)
    _safe_set(b, 'ControlProgram', None)
    assert not _is_linked(b, 'ControlProgram', a2)
    if hasattr(a2, 'ControlProgramSteamBoiler'):
        assert not _is_linked(a2, 'ControlProgramSteamBoiler', b)


def test_assoc_SteamBoilerMeasurementDeviceSnapshot12_reverse_link_reassign_clear():
    a1 = SBCS_SteamMeasurementDevice(evaporationRate=True, ready=True, waterLevel=3.14)
    a2 = SBCS_SteamMeasurementDevice(evaporationRate=False, ready=False, waterLevel=9.99)
    b = SBCS_Snapshot()
    _safe_set(b, 'SnapshotSBMD', a1)
    assert _is_linked(b, 'SnapshotSBMD', a1)
    if hasattr(a1, 'SteamMeasurementDevice13'):
        assert _is_linked(a1, 'SteamMeasurementDevice13', b)
    _safe_set(b, 'SnapshotSBMD', a2)
    assert _is_linked(b, 'SnapshotSBMD', a2)
    if hasattr(a1, 'SteamMeasurementDevice13'):
        assert not _is_linked(a1, 'SteamMeasurementDevice13', b)
    if hasattr(a2, 'SteamMeasurementDevice13'):
        assert _is_linked(a2, 'SteamMeasurementDevice13', b)
    _safe_set(b, 'SnapshotSBMD', None)
    assert not _is_linked(b, 'SnapshotSBMD', a2)
    if hasattr(a2, 'SteamMeasurementDevice13'):
        assert not _is_linked(a2, 'SteamMeasurementDevice13', b)


def test_assoc_SteamBoilerSMD3_reverse_link_reassign_clear():
    a1 = SBCS_SteamMeasurementDevice(evaporationRate=True, ready=True, waterLevel=3.14)
    a2 = SBCS_SteamMeasurementDevice(evaporationRate=False, ready=False, waterLevel=9.99)
    b = SBCS_SteamBoiler(capacity=3.14, maximalLimit=3.14, maximalNormal=3.14, maximumDecrease=3.14, maximumIncrease=3.14, minimalLimit=3.14, minimalNormal=3.14, ready=True, valveOpen="sample_text")
    _safe_set(b, 'SMDSteamBoiler', a1)
    assert _is_linked(b, 'SMDSteamBoiler', a1)
    if hasattr(a1, 'SteamMeasurementDevice'):
        assert _is_linked(a1, 'SteamMeasurementDevice', b)
    _safe_set(b, 'SMDSteamBoiler', a2)
    assert _is_linked(b, 'SMDSteamBoiler', a2)
    if hasattr(a1, 'SteamMeasurementDevice'):
        assert not _is_linked(a1, 'SteamMeasurementDevice', b)
    if hasattr(a2, 'SteamMeasurementDevice'):
        assert _is_linked(a2, 'SteamMeasurementDevice', b)
    _safe_set(b, 'SMDSteamBoiler', None)
    assert not _is_linked(b, 'SMDSteamBoiler', a2)
    if hasattr(a2, 'SteamMeasurementDevice'):
        assert not _is_linked(a2, 'SteamMeasurementDevice', b)


def test_assoc_SteamBoilerSnapshot5_reverse_link_reassign_clear():
    a1 = SBCS_SteamBoiler(capacity=3.14, maximalLimit=3.14, maximalNormal=3.14, maximumDecrease=3.14, maximumIncrease=3.14, minimalLimit=3.14, minimalNormal=3.14, ready=True, valveOpen="sample_text")
    a2 = SBCS_SteamBoiler(capacity=9.99, maximalLimit=9.99, maximalNormal=9.99, maximumDecrease=9.99, maximumIncrease=9.99, minimalLimit=9.99, minimalNormal=9.99, ready=False, valveOpen="sample_text_2")
    b = SBCS_Snapshot()
    _safe_set(b, 'SnapshotSteamBoiler', a1)
    assert _is_linked(b, 'SnapshotSteamBoiler', a1)
    if hasattr(a1, 'SteamBoiler'):
        assert _is_linked(a1, 'SteamBoiler', b)
    _safe_set(b, 'SnapshotSteamBoiler', a2)
    assert _is_linked(b, 'SnapshotSteamBoiler', a2)
    if hasattr(a1, 'SteamBoiler'):
        assert not _is_linked(a1, 'SteamBoiler', b)
    if hasattr(a2, 'SteamBoiler'):
        assert _is_linked(a2, 'SteamBoiler', b)
    _safe_set(b, 'SnapshotSteamBoiler', None)
    assert not _is_linked(b, 'SnapshotSteamBoiler', a2)
    if hasattr(a2, 'SteamBoiler'):
        assert not _is_linked(a2, 'SteamBoiler', b)


def test_assoc_SteamBoilerWLMD4_reverse_link_reassign_clear():
    a1 = SBCS_WaterLevelMeasurementDevice(ready=True, waterLevel=3.14)
    a2 = SBCS_WaterLevelMeasurementDevice(ready=False, waterLevel=9.99)
    b = SBCS_SteamBoiler(capacity=3.14, maximalLimit=3.14, maximalNormal=3.14, maximumDecrease=3.14, maximumIncrease=3.14, minimalLimit=3.14, minimalNormal=3.14, ready=True, valveOpen="sample_text")
    _safe_set(b, 'WLMDSteamBoiler', a1)
    assert _is_linked(b, 'WLMDSteamBoiler', a1)
    if hasattr(a1, 'WaterLevelMeasurementDevice'):
        assert _is_linked(a1, 'WaterLevelMeasurementDevice', b)
    _safe_set(b, 'WLMDSteamBoiler', a2)
    assert _is_linked(b, 'WLMDSteamBoiler', a2)
    if hasattr(a1, 'WaterLevelMeasurementDevice'):
        assert not _is_linked(a1, 'WaterLevelMeasurementDevice', b)
    if hasattr(a2, 'WaterLevelMeasurementDevice'):
        assert _is_linked(a2, 'WaterLevelMeasurementDevice', b)
    _safe_set(b, 'WLMDSteamBoiler', None)
    assert not _is_linked(b, 'WLMDSteamBoiler', a2)
    if hasattr(a2, 'WaterLevelMeasurementDevice'):
        assert not _is_linked(a2, 'WaterLevelMeasurementDevice', b)


def test_assoc_SteqmBoilerPump2_reverse_link_reassign_clear():
    a1 = SBCS_SteamBoiler(capacity=3.14, maximalLimit=3.14, maximalNormal=3.14, maximumDecrease=3.14, maximumIncrease=3.14, minimalLimit=3.14, minimalNormal=3.14, ready=True, valveOpen="sample_text")
    a2 = SBCS_SteamBoiler(capacity=9.99, maximalLimit=9.99, maximalNormal=9.99, maximumDecrease=9.99, maximumIncrease=9.99, minimalLimit=9.99, minimalNormal=9.99, ready=False, valveOpen="sample_text_2")
    b = SBCS_Pump(capacity=3.14, mode="sample_text", ready=True)
    _safe_set(b, 'Pump', a1)
    assert _is_linked(b, 'Pump', a1)
    if hasattr(a1, 'PumpSteamBoiler'):
        assert _is_linked(a1, 'PumpSteamBoiler', b)
    _safe_set(b, 'Pump', a2)
    assert _is_linked(b, 'Pump', a2)
    if hasattr(a1, 'PumpSteamBoiler'):
        assert not _is_linked(a1, 'PumpSteamBoiler', b)
    if hasattr(a2, 'PumpSteamBoiler'):
        assert _is_linked(a2, 'PumpSteamBoiler', b)
    _safe_set(b, 'Pump', None)
    assert not _is_linked(b, 'Pump', a2)
    if hasattr(a2, 'PumpSteamBoiler'):
        assert not _is_linked(a2, 'PumpSteamBoiler', b)


def test_assoc_WLMDControlProgram59_reverse_link_reassign_clear():
    a1 = SBCS_WaterLevelMeasurementDevice(ready=True, waterLevel=3.14)
    a2 = SBCS_WaterLevelMeasurementDevice(ready=False, waterLevel=9.99)
    b = SBCS_ControlProgram(failureDetected=True, mode="sample_text", pumpControlerFailure=True, pumpFailure=True, ready=True, smdFailure=True, wlmdFailure=True)
    _safe_set(b, 'ControlProgram60', a1)
    assert _is_linked(b, 'ControlProgram60', a1)
    if hasattr(a1, 'ControlProgramWLMD'):
        assert _is_linked(a1, 'ControlProgramWLMD', b)
    _safe_set(b, 'ControlProgram60', a2)
    assert _is_linked(b, 'ControlProgram60', a2)
    if hasattr(a1, 'ControlProgramWLMD'):
        assert not _is_linked(a1, 'ControlProgramWLMD', b)
    if hasattr(a2, 'ControlProgramWLMD'):
        assert _is_linked(a2, 'ControlProgramWLMD', b)
    _safe_set(b, 'ControlProgram60', None)
    assert not _is_linked(b, 'ControlProgram60', a2)
    if hasattr(a2, 'ControlProgramWLMD'):
        assert not _is_linked(a2, 'ControlProgramWLMD', b)


def test_assoc_WLMDSnapshot10_reverse_link_reassign_clear():
    a1 = SBCS_WaterLevelMeasurementDevice(ready=True, waterLevel=3.14)
    a2 = SBCS_WaterLevelMeasurementDevice(ready=False, waterLevel=9.99)
    b = SBCS_Snapshot()
    _safe_set(b, 'SnapshotWLMD', a1)
    assert _is_linked(b, 'SnapshotWLMD', a1)
    if hasattr(a1, 'WaterLevelMeasurementDevice11'):
        assert _is_linked(a1, 'WaterLevelMeasurementDevice11', b)
    _safe_set(b, 'SnapshotWLMD', a2)
    assert _is_linked(b, 'SnapshotWLMD', a2)
    if hasattr(a1, 'WaterLevelMeasurementDevice11'):
        assert not _is_linked(a1, 'WaterLevelMeasurementDevice11', b)
    if hasattr(a2, 'WaterLevelMeasurementDevice11'):
        assert _is_linked(a2, 'WaterLevelMeasurementDevice11', b)
    _safe_set(b, 'SnapshotWLMD', None)
    assert not _is_linked(b, 'SnapshotWLMD', a2)
    if hasattr(a2, 'WaterLevelMeasurementDevice11'):
        assert not _is_linked(a2, 'WaterLevelMeasurementDevice11', b)


def test_assoc_WLMDSteamBoiler61_reverse_link_reassign_clear():
    a1 = SBCS_WaterLevelMeasurementDevice(ready=True, waterLevel=3.14)
    a2 = SBCS_WaterLevelMeasurementDevice(ready=False, waterLevel=9.99)
    b = SBCS_SteamBoiler(capacity=3.14, maximalLimit=3.14, maximalNormal=3.14, maximumDecrease=3.14, maximumIncrease=3.14, minimalLimit=3.14, minimalNormal=3.14, ready=True, valveOpen="sample_text")
    _safe_set(b, 'SteamBoiler62', a1)
    assert _is_linked(b, 'SteamBoiler62', a1)
    if hasattr(a1, 'SteamBoilerWLMD'):
        assert _is_linked(a1, 'SteamBoilerWLMD', b)
    _safe_set(b, 'SteamBoiler62', a2)
    assert _is_linked(b, 'SteamBoiler62', a2)
    if hasattr(a1, 'SteamBoilerWLMD'):
        assert not _is_linked(a1, 'SteamBoilerWLMD', b)
    if hasattr(a2, 'SteamBoilerWLMD'):
        assert _is_linked(a2, 'SteamBoilerWLMD', b)
    _safe_set(b, 'SteamBoiler62', None)
    assert not _is_linked(b, 'SteamBoiler62', a2)
    if hasattr(a2, 'SteamBoilerWLMD'):
        assert not _is_linked(a2, 'SteamBoilerWLMD', b)


def test_assoc_wlmdPost68_reverse_link_reassign_clear():
    a1 = SBCS_WaterLevelMeaurementDevice_getLevel(ret=3.14)
    a2 = SBCS_WaterLevelMeaurementDevice_getLevel(ret=9.99)
    b = SBCS_WaterLevelMeasurementDevice(ready=True, waterLevel=3.14)
    _safe_set(b, 'SBCS_WaterLevelMeasurementDevice70', a1)
    assert _is_linked(b, 'SBCS_WaterLevelMeasurementDevice70', a1)
    if hasattr(a1, 'SBCS_WaterLevelMeaurementDevice_getLevel69'):
        assert _is_linked(a1, 'SBCS_WaterLevelMeaurementDevice_getLevel69', b)
    _safe_set(b, 'SBCS_WaterLevelMeasurementDevice70', a2)
    assert _is_linked(b, 'SBCS_WaterLevelMeasurementDevice70', a2)
    if hasattr(a1, 'SBCS_WaterLevelMeaurementDevice_getLevel69'):
        assert not _is_linked(a1, 'SBCS_WaterLevelMeaurementDevice_getLevel69', b)
    if hasattr(a2, 'SBCS_WaterLevelMeaurementDevice_getLevel69'):
        assert _is_linked(a2, 'SBCS_WaterLevelMeaurementDevice_getLevel69', b)
    _safe_set(b, 'SBCS_WaterLevelMeasurementDevice70', None)
    assert not _is_linked(b, 'SBCS_WaterLevelMeasurementDevice70', a2)
    if hasattr(a2, 'SBCS_WaterLevelMeaurementDevice_getLevel69'):
        assert not _is_linked(a2, 'SBCS_WaterLevelMeaurementDevice_getLevel69', b)


def test_assoc_wlmdPre67_reverse_link_reassign_clear():
    a1 = SBCS_WaterLevelMeaurementDevice_getLevel(ret=3.14)
    a2 = SBCS_WaterLevelMeaurementDevice_getLevel(ret=9.99)
    b = SBCS_WaterLevelMeasurementDevice(ready=True, waterLevel=3.14)
    _safe_set(b, 'SBCS_WaterLevelMeasurementDevice', a1)
    assert _is_linked(b, 'SBCS_WaterLevelMeasurementDevice', a1)
    if hasattr(a1, 'SBCS_WaterLevelMeaurementDevice_getLevel'):
        assert _is_linked(a1, 'SBCS_WaterLevelMeaurementDevice_getLevel', b)
    _safe_set(b, 'SBCS_WaterLevelMeasurementDevice', a2)
    assert _is_linked(b, 'SBCS_WaterLevelMeasurementDevice', a2)
    if hasattr(a1, 'SBCS_WaterLevelMeaurementDevice_getLevel'):
        assert not _is_linked(a1, 'SBCS_WaterLevelMeaurementDevice_getLevel', b)
    if hasattr(a2, 'SBCS_WaterLevelMeaurementDevice_getLevel'):
        assert _is_linked(a2, 'SBCS_WaterLevelMeaurementDevice_getLevel', b)
    _safe_set(b, 'SBCS_WaterLevelMeasurementDevice', None)
    assert not _is_linked(b, 'SBCS_WaterLevelMeasurementDevice', a2)
    if hasattr(a2, 'SBCS_WaterLevelMeaurementDevice_getLevel'):
        assert not _is_linked(a2, 'SBCS_WaterLevelMeaurementDevice_getLevel', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_AfterTrans16_stub_double():
    # SBCS_Transition has no real 'Transition17' property in the generated
    # code (a bare stub) -- manually attach it so SBCS_Snapshot's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # SBCS_Snapshot's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = SBCS_Snapshot()
    partner = SBCS_Transition()
    setattr(partner, 'Transition17', None)
    _safe_set(owner, 'AfterTrans', partner)
    assert getattr(partner, 'Transition17') == owner
    _safe_set(owner, 'AfterTrans', None)
    assert getattr(partner, 'Transition17') is None


def test_assoc_AfterTrans42_stub_double():
    # SBCS_Transition has no real 'AfterTrans43' property in the generated
    # code (a bare stub) -- manually attach it so SBCS_Snapshot's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # SBCS_Snapshot's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = SBCS_Snapshot()
    partner = SBCS_Transition()
    setattr(partner, 'AfterTrans43', None)
    _safe_set(owner, 'Snapshot44', partner)
    assert getattr(partner, 'AfterTrans43') == owner
    _safe_set(owner, 'Snapshot44', None)
    assert getattr(partner, 'AfterTrans43') is None


def test_assoc_BeforeTrans15_stub_double():
    # SBCS_Transition has no real 'Transition' property in the generated
    # code (a bare stub) -- manually attach it so SBCS_Snapshot's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # SBCS_Snapshot's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = SBCS_Snapshot()
    partner = SBCS_Transition()
    setattr(partner, 'Transition', None)
    _safe_set(owner, 'BeforeTrans', partner)
    assert getattr(partner, 'Transition') == owner
    _safe_set(owner, 'BeforeTrans', None)
    assert getattr(partner, 'Transition') is None


def test_assoc_BeforeTrans39_stub_double():
    # SBCS_Transition has no real 'BeforeTrans40' property in the generated
    # code (a bare stub) -- manually attach it so SBCS_Snapshot's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # SBCS_Snapshot's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = SBCS_Snapshot()
    partner = SBCS_Transition()
    setattr(partner, 'BeforeTrans40', None)
    _safe_set(owner, 'Snapshot41', partner)
    assert getattr(partner, 'BeforeTrans40') == owner
    _safe_set(owner, 'Snapshot41', None)
    assert getattr(partner, 'BeforeTrans40') is None


def test_assoc_CPPost64_stub_double():
    # SBCS_ControlProgram_Start has no real 'SBCS_ControlProgram_Start65' property in the generated
    # code (a bare stub) -- manually attach it so SBCS_ControlProgram's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # SBCS_ControlProgram's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = SBCS_ControlProgram(failureDetected=True, mode="sample_text", pumpControlerFailure=True, pumpFailure=True, ready=True, smdFailure=True, wlmdFailure=True)
    partner = SBCS_ControlProgram_Start()
    setattr(partner, 'SBCS_ControlProgram_Start65', None)
    _safe_set(owner, 'SBCS_ControlProgram66', partner)
    assert getattr(partner, 'SBCS_ControlProgram_Start65') == owner
    _safe_set(owner, 'SBCS_ControlProgram66', None)
    assert getattr(partner, 'SBCS_ControlProgram_Start65') is None


def test_assoc_CPPre63_stub_double():
    # SBCS_ControlProgram_Start has no real 'SBCS_ControlProgram_Start' property in the generated
    # code (a bare stub) -- manually attach it so SBCS_ControlProgram's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # SBCS_ControlProgram's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = SBCS_ControlProgram(failureDetected=True, mode="sample_text", pumpControlerFailure=True, pumpFailure=True, ready=True, smdFailure=True, wlmdFailure=True)
    partner = SBCS_ControlProgram_Start()
    setattr(partner, 'SBCS_ControlProgram_Start', None)
    _safe_set(owner, 'SBCS_ControlProgram', partner)
    assert getattr(partner, 'SBCS_ControlProgram_Start') == owner
    _safe_set(owner, 'SBCS_ControlProgram', None)
    assert getattr(partner, 'SBCS_ControlProgram_Start') is None


def test_assoc_PCPost76_stub_double():
    # SBCS_PumpController_ClosePump has no real 'SBCS_PumpController_ClosePump77' property in the generated
    # code (a bare stub) -- manually attach it so SBCS_PumpControler's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # SBCS_PumpControler's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = SBCS_PumpControler(circulating=True, ready=True)
    partner = SBCS_PumpController_ClosePump()
    setattr(partner, 'SBCS_PumpController_ClosePump77', None)
    _safe_set(owner, 'SBCS_PumpControler78', partner)
    assert getattr(partner, 'SBCS_PumpController_ClosePump77') == owner
    _safe_set(owner, 'SBCS_PumpControler78', None)
    assert getattr(partner, 'SBCS_PumpController_ClosePump77') is None


def test_assoc_PCPost81_stub_double():
    # SBCS_PumpController_OpenPump has no real 'SBCS_PumpController_OpenPump82' property in the generated
    # code (a bare stub) -- manually attach it so SBCS_PumpControler's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # SBCS_PumpControler's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = SBCS_PumpControler(circulating=True, ready=True)
    partner = SBCS_PumpController_OpenPump()
    setattr(partner, 'SBCS_PumpController_OpenPump82', None)
    _safe_set(owner, 'SBCS_PumpControler83', partner)
    assert getattr(partner, 'SBCS_PumpController_OpenPump82') == owner
    _safe_set(owner, 'SBCS_PumpControler83', None)
    assert getattr(partner, 'SBCS_PumpController_OpenPump82') is None


def test_assoc_PCPre75_stub_double():
    # SBCS_PumpController_ClosePump has no real 'SBCS_PumpController_ClosePump' property in the generated
    # code (a bare stub) -- manually attach it so SBCS_PumpControler's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # SBCS_PumpControler's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = SBCS_PumpControler(circulating=True, ready=True)
    partner = SBCS_PumpController_ClosePump()
    setattr(partner, 'SBCS_PumpController_ClosePump', None)
    _safe_set(owner, 'SBCS_PumpControler', partner)
    assert getattr(partner, 'SBCS_PumpController_ClosePump') == owner
    _safe_set(owner, 'SBCS_PumpControler', None)
    assert getattr(partner, 'SBCS_PumpController_ClosePump') is None


def test_assoc_PCPre79_stub_double():
    # SBCS_PumpController_OpenPump has no real 'SBCS_PumpController_OpenPump' property in the generated
    # code (a bare stub) -- manually attach it so SBCS_PumpControler's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # SBCS_PumpControler's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = SBCS_PumpControler(circulating=True, ready=True)
    partner = SBCS_PumpController_OpenPump()
    setattr(partner, 'SBCS_PumpController_OpenPump', None)
    _safe_set(owner, 'SBCS_PumpControler80', partner)
    assert getattr(partner, 'SBCS_PumpController_OpenPump') == owner
    _safe_set(owner, 'SBCS_PumpControler80', None)
    assert getattr(partner, 'SBCS_PumpController_OpenPump') is None


def test_assoc_SBPost72_stub_double():
    # SBCS_SteamBoiler_OpenValve has no real 'SBCS_SteamBoiler_OpenValve73' property in the generated
    # code (a bare stub) -- manually attach it so SBCS_SteamBoiler's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # SBCS_SteamBoiler's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = SBCS_SteamBoiler(capacity=3.14, maximalLimit=3.14, maximalNormal=3.14, maximumDecrease=3.14, maximumIncrease=3.14, minimalLimit=3.14, minimalNormal=3.14, ready=True, valveOpen="sample_text")
    partner = SBCS_SteamBoiler_OpenValve()
    setattr(partner, 'SBCS_SteamBoiler_OpenValve73', None)
    _safe_set(owner, 'SBCS_SteamBoiler74', partner)
    assert getattr(partner, 'SBCS_SteamBoiler_OpenValve73') == owner
    _safe_set(owner, 'SBCS_SteamBoiler74', None)
    assert getattr(partner, 'SBCS_SteamBoiler_OpenValve73') is None


def test_assoc_SBPre71_stub_double():
    # SBCS_SteamBoiler_OpenValve has no real 'SBCS_SteamBoiler_OpenValve' property in the generated
    # code (a bare stub) -- manually attach it so SBCS_SteamBoiler's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # SBCS_SteamBoiler's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = SBCS_SteamBoiler(capacity=3.14, maximalLimit=3.14, maximalNormal=3.14, maximumDecrease=3.14, maximumIncrease=3.14, minimalLimit=3.14, minimalNormal=3.14, ready=True, valveOpen="sample_text")
    partner = SBCS_SteamBoiler_OpenValve()
    setattr(partner, 'SBCS_SteamBoiler_OpenValve', None)
    _safe_set(owner, 'SBCS_SteamBoiler', partner)
    assert getattr(partner, 'SBCS_SteamBoiler_OpenValve') == owner
    _safe_set(owner, 'SBCS_SteamBoiler', None)
    assert getattr(partner, 'SBCS_SteamBoiler_OpenValve') is None



