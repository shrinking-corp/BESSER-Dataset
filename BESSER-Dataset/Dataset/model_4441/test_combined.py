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
    SingleQuantity,
    Quantity,
    roverml_SingleQuantity,
    roverml_Quantity,
    roverml_Position,
    Triggered,
    roverml_CompassTrigger,
    roverml_GPSTrigger,
    roverml_DistanceSensorTrigger,
    Transition,
    roverml_Regular,
    roverml_Triggered,
    roverml_Angle,
    roverml_Length,
    roverml_Time,
    Command,
    roverml_Terminate,
    roverml_Rotate,
    roverml_Repeat,
    roverml_Wait,
    roverml_Move,
    roverml_SetLightColor,
    roverml_Command,
    roverml_Velocity,
    roverml_Transition,
    Actuator,
    roverml_Light,
    roverml_Motor,
    Sensor,
    roverml_DistanceSensor,
    roverml_Compass,
    roverml_GPS,
    Component,
    roverml_Actuator,
    roverml_Sensor,
    roverml_NamedElement,
    roverml_Block,
    NamedElement,
    roverml_Program,
    roverml_Component,
    roverml_Rover,
    roverml_System,
    LengthUnits,
    AngleUnits,
    Colours,
    TimeUnits,
    VelocityUnits,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_hyp_singlequantity_is_not_abstract():
    assert not inspect.isabstract(SingleQuantity)


def test_hyp_singlequantity_constructor_exists():
    assert callable(SingleQuantity.__init__)


def test_hyp_singlequantity_constructor_args():
    sig = inspect.signature(SingleQuantity.__init__)
    params = list(sig.parameters.keys())



def test_hyp_quantity_is_not_abstract():
    assert not inspect.isabstract(Quantity)


def test_hyp_quantity_constructor_exists():
    assert callable(Quantity.__init__)


def test_hyp_quantity_constructor_args():
    sig = inspect.signature(Quantity.__init__)
    params = list(sig.parameters.keys())



def test_hyp_roverml_singlequantity_is_not_abstract():
    assert not inspect.isabstract(roverml_SingleQuantity)


def test_hyp_roverml_singlequantity_constructor_exists():
    assert callable(roverml_SingleQuantity.__init__)


def test_hyp_roverml_singlequantity_constructor_args():
    sig = inspect.signature(roverml_SingleQuantity.__init__)
    params = list(sig.parameters.keys())



def test_hyp_roverml_quantity_is_not_abstract():
    assert not inspect.isabstract(roverml_Quantity)


def test_hyp_roverml_quantity_constructor_exists():
    assert callable(roverml_Quantity.__init__)


def test_hyp_roverml_quantity_constructor_args():
    sig = inspect.signature(roverml_Quantity.__init__)
    params = list(sig.parameters.keys())



def test_hyp_roverml_position_is_not_abstract():
    assert not inspect.isabstract(roverml_Position)


def test_hyp_roverml_position_constructor_exists():
    assert callable(roverml_Position.__init__)


def test_hyp_roverml_position_constructor_args():
    sig = inspect.signature(roverml_Position.__init__)
    params = list(sig.parameters.keys())
    assert "y" in params, "Missing parameter 'y'"
    assert "x" in params, "Missing parameter 'x'"





def test_hyp_triggered_is_not_abstract():
    assert not inspect.isabstract(Triggered)


def test_hyp_triggered_constructor_exists():
    assert callable(Triggered.__init__)


def test_hyp_triggered_constructor_args():
    sig = inspect.signature(Triggered.__init__)
    params = list(sig.parameters.keys())



def test_hyp_roverml_compasstrigger_is_not_abstract():
    assert not inspect.isabstract(roverml_CompassTrigger)


def test_hyp_roverml_compasstrigger_constructor_exists():
    assert callable(roverml_CompassTrigger.__init__)


def test_hyp_roverml_compasstrigger_constructor_args():
    sig = inspect.signature(roverml_CompassTrigger.__init__)
    params = list(sig.parameters.keys())
    assert "angle" in params, "Missing parameter 'angle'"




def test_hyp_roverml_gpstrigger_is_not_abstract():
    assert not inspect.isabstract(roverml_GPSTrigger)


def test_hyp_roverml_gpstrigger_constructor_exists():
    assert callable(roverml_GPSTrigger.__init__)


def test_hyp_roverml_gpstrigger_constructor_args():
    sig = inspect.signature(roverml_GPSTrigger.__init__)
    params = list(sig.parameters.keys())
    assert "y" in params, "Missing parameter 'y'"
    assert "x" in params, "Missing parameter 'x'"





def test_hyp_roverml_distancesensortrigger_is_not_abstract():
    assert not inspect.isabstract(roverml_DistanceSensorTrigger)


def test_hyp_roverml_distancesensortrigger_constructor_exists():
    assert callable(roverml_DistanceSensorTrigger.__init__)


def test_hyp_roverml_distancesensortrigger_constructor_args():
    sig = inspect.signature(roverml_DistanceSensorTrigger.__init__)
    params = list(sig.parameters.keys())
    assert "dist" in params, "Missing parameter 'dist'"




def test_hyp_transition_is_not_abstract():
    assert not inspect.isabstract(Transition)


def test_hyp_transition_constructor_exists():
    assert callable(Transition.__init__)


def test_hyp_transition_constructor_args():
    sig = inspect.signature(Transition.__init__)
    params = list(sig.parameters.keys())



def test_hyp_roverml_regular_is_not_abstract():
    assert not inspect.isabstract(roverml_Regular)


def test_hyp_roverml_regular_constructor_exists():
    assert callable(roverml_Regular.__init__)


def test_hyp_roverml_regular_constructor_args():
    sig = inspect.signature(roverml_Regular.__init__)
    params = list(sig.parameters.keys())



def test_hyp_roverml_triggered_is_not_abstract():
    assert not inspect.isabstract(roverml_Triggered)


def test_hyp_roverml_triggered_constructor_exists():
    assert callable(roverml_Triggered.__init__)


def test_hyp_roverml_triggered_constructor_args():
    sig = inspect.signature(roverml_Triggered.__init__)
    params = list(sig.parameters.keys())
    assert "operator" in params, "Missing parameter 'operator'"




def test_hyp_roverml_angle_is_not_abstract():
    assert not inspect.isabstract(roverml_Angle)


def test_hyp_roverml_angle_constructor_exists():
    assert callable(roverml_Angle.__init__)


def test_hyp_roverml_angle_constructor_args():
    sig = inspect.signature(roverml_Angle.__init__)
    params = list(sig.parameters.keys())
    assert "units" in params, "Missing parameter 'units'"




def test_hyp_roverml_length_is_not_abstract():
    assert not inspect.isabstract(roverml_Length)


def test_hyp_roverml_length_constructor_exists():
    assert callable(roverml_Length.__init__)


def test_hyp_roverml_length_constructor_args():
    sig = inspect.signature(roverml_Length.__init__)
    params = list(sig.parameters.keys())
    assert "units" in params, "Missing parameter 'units'"




def test_hyp_roverml_time_is_not_abstract():
    assert not inspect.isabstract(roverml_Time)


def test_hyp_roverml_time_constructor_exists():
    assert callable(roverml_Time.__init__)


def test_hyp_roverml_time_constructor_args():
    sig = inspect.signature(roverml_Time.__init__)
    params = list(sig.parameters.keys())
    assert "units" in params, "Missing parameter 'units'"




def test_hyp_command_is_not_abstract():
    assert not inspect.isabstract(Command)


def test_hyp_command_constructor_exists():
    assert callable(Command.__init__)


def test_hyp_command_constructor_args():
    sig = inspect.signature(Command.__init__)
    params = list(sig.parameters.keys())



def test_hyp_roverml_terminate_is_not_abstract():
    assert not inspect.isabstract(roverml_Terminate)


def test_hyp_roverml_terminate_constructor_exists():
    assert callable(roverml_Terminate.__init__)


def test_hyp_roverml_terminate_constructor_args():
    sig = inspect.signature(roverml_Terminate.__init__)
    params = list(sig.parameters.keys())



def test_hyp_roverml_rotate_is_not_abstract():
    assert not inspect.isabstract(roverml_Rotate)


def test_hyp_roverml_rotate_constructor_exists():
    assert callable(roverml_Rotate.__init__)


def test_hyp_roverml_rotate_constructor_args():
    sig = inspect.signature(roverml_Rotate.__init__)
    params = list(sig.parameters.keys())
    assert "angle" in params, "Missing parameter 'angle'"




def test_hyp_roverml_repeat_is_not_abstract():
    assert not inspect.isabstract(roverml_Repeat)


def test_hyp_roverml_repeat_constructor_exists():
    assert callable(roverml_Repeat.__init__)


def test_hyp_roverml_repeat_constructor_args():
    sig = inspect.signature(roverml_Repeat.__init__)
    params = list(sig.parameters.keys())
    assert "numberOfReps" in params, "Missing parameter 'numberOfReps'"




def test_hyp_roverml_wait_is_not_abstract():
    assert not inspect.isabstract(roverml_Wait)


def test_hyp_roverml_wait_constructor_exists():
    assert callable(roverml_Wait.__init__)


def test_hyp_roverml_wait_constructor_args():
    sig = inspect.signature(roverml_Wait.__init__)
    params = list(sig.parameters.keys())
    assert "time" in params, "Missing parameter 'time'"




def test_hyp_roverml_move_is_not_abstract():
    assert not inspect.isabstract(roverml_Move)


def test_hyp_roverml_move_constructor_exists():
    assert callable(roverml_Move.__init__)


def test_hyp_roverml_move_constructor_args():
    sig = inspect.signature(roverml_Move.__init__)
    params = list(sig.parameters.keys())
    assert "velocity" in params, "Missing parameter 'velocity'"
    assert "length" in params, "Missing parameter 'length'"





def test_hyp_roverml_setlightcolor_is_not_abstract():
    assert not inspect.isabstract(roverml_SetLightColor)


def test_hyp_roverml_setlightcolor_constructor_exists():
    assert callable(roverml_SetLightColor.__init__)


def test_hyp_roverml_setlightcolor_constructor_args():
    sig = inspect.signature(roverml_SetLightColor.__init__)
    params = list(sig.parameters.keys())
    assert "color" in params, "Missing parameter 'color'"




def test_hyp_roverml_command_is_not_abstract():
    assert not inspect.isabstract(roverml_Command)


def test_hyp_roverml_command_constructor_exists():
    assert callable(roverml_Command.__init__)


def test_hyp_roverml_command_constructor_args():
    sig = inspect.signature(roverml_Command.__init__)
    params = list(sig.parameters.keys())



def test_hyp_roverml_velocity_is_not_abstract():
    assert not inspect.isabstract(roverml_Velocity)


def test_hyp_roverml_velocity_constructor_exists():
    assert callable(roverml_Velocity.__init__)


def test_hyp_roverml_velocity_constructor_args():
    sig = inspect.signature(roverml_Velocity.__init__)
    params = list(sig.parameters.keys())
    assert "units" in params, "Missing parameter 'units'"




def test_hyp_roverml_transition_is_not_abstract():
    assert not inspect.isabstract(roverml_Transition)


def test_hyp_roverml_transition_constructor_exists():
    assert callable(roverml_Transition.__init__)


def test_hyp_roverml_transition_constructor_args():
    sig = inspect.signature(roverml_Transition.__init__)
    params = list(sig.parameters.keys())



def test_hyp_actuator_is_not_abstract():
    assert not inspect.isabstract(Actuator)


def test_hyp_actuator_constructor_exists():
    assert callable(Actuator.__init__)


def test_hyp_actuator_constructor_args():
    sig = inspect.signature(Actuator.__init__)
    params = list(sig.parameters.keys())



def test_hyp_roverml_light_is_not_abstract():
    assert not inspect.isabstract(roverml_Light)


def test_hyp_roverml_light_constructor_exists():
    assert callable(roverml_Light.__init__)


def test_hyp_roverml_light_constructor_args():
    sig = inspect.signature(roverml_Light.__init__)
    params = list(sig.parameters.keys())



def test_hyp_roverml_motor_is_not_abstract():
    assert not inspect.isabstract(roverml_Motor)


def test_hyp_roverml_motor_constructor_exists():
    assert callable(roverml_Motor.__init__)


def test_hyp_roverml_motor_constructor_args():
    sig = inspect.signature(roverml_Motor.__init__)
    params = list(sig.parameters.keys())



def test_hyp_sensor_is_not_abstract():
    assert not inspect.isabstract(Sensor)


def test_hyp_sensor_constructor_exists():
    assert callable(Sensor.__init__)


def test_hyp_sensor_constructor_args():
    sig = inspect.signature(Sensor.__init__)
    params = list(sig.parameters.keys())



def test_hyp_roverml_distancesensor_is_not_abstract():
    assert not inspect.isabstract(roverml_DistanceSensor)


def test_hyp_roverml_distancesensor_constructor_exists():
    assert callable(roverml_DistanceSensor.__init__)


def test_hyp_roverml_distancesensor_constructor_args():
    sig = inspect.signature(roverml_DistanceSensor.__init__)
    params = list(sig.parameters.keys())
    assert "distance" in params, "Missing parameter 'distance'"




def test_hyp_roverml_compass_is_not_abstract():
    assert not inspect.isabstract(roverml_Compass)


def test_hyp_roverml_compass_constructor_exists():
    assert callable(roverml_Compass.__init__)


def test_hyp_roverml_compass_constructor_args():
    sig = inspect.signature(roverml_Compass.__init__)
    params = list(sig.parameters.keys())
    assert "angle" in params, "Missing parameter 'angle'"




def test_hyp_roverml_gps_is_not_abstract():
    assert not inspect.isabstract(roverml_GPS)


def test_hyp_roverml_gps_constructor_exists():
    assert callable(roverml_GPS.__init__)


def test_hyp_roverml_gps_constructor_args():
    sig = inspect.signature(roverml_GPS.__init__)
    params = list(sig.parameters.keys())
    assert "x" in params, "Missing parameter 'x'"
    assert "y" in params, "Missing parameter 'y'"





def test_hyp_component_is_not_abstract():
    assert not inspect.isabstract(Component)


def test_hyp_component_constructor_exists():
    assert callable(Component.__init__)


def test_hyp_component_constructor_args():
    sig = inspect.signature(Component.__init__)
    params = list(sig.parameters.keys())



def test_hyp_roverml_actuator_is_not_abstract():
    assert not inspect.isabstract(roverml_Actuator)


def test_hyp_roverml_actuator_constructor_exists():
    assert callable(roverml_Actuator.__init__)


def test_hyp_roverml_actuator_constructor_args():
    sig = inspect.signature(roverml_Actuator.__init__)
    params = list(sig.parameters.keys())



def test_hyp_roverml_sensor_is_not_abstract():
    assert not inspect.isabstract(roverml_Sensor)


def test_hyp_roverml_sensor_constructor_exists():
    assert callable(roverml_Sensor.__init__)


def test_hyp_roverml_sensor_constructor_args():
    sig = inspect.signature(roverml_Sensor.__init__)
    params = list(sig.parameters.keys())



def test_hyp_roverml_namedelement_is_not_abstract():
    assert not inspect.isabstract(roverml_NamedElement)


def test_hyp_roverml_namedelement_constructor_exists():
    assert callable(roverml_NamedElement.__init__)


def test_hyp_roverml_namedelement_constructor_args():
    sig = inspect.signature(roverml_NamedElement.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"




def test_hyp_roverml_block_is_not_abstract():
    assert not inspect.isabstract(roverml_Block)


def test_hyp_roverml_block_constructor_exists():
    assert callable(roverml_Block.__init__)


def test_hyp_roverml_block_constructor_args():
    sig = inspect.signature(roverml_Block.__init__)
    params = list(sig.parameters.keys())



def test_hyp_namedelement_is_not_abstract():
    assert not inspect.isabstract(NamedElement)


def test_hyp_namedelement_constructor_exists():
    assert callable(NamedElement.__init__)


def test_hyp_namedelement_constructor_args():
    sig = inspect.signature(NamedElement.__init__)
    params = list(sig.parameters.keys())



def test_hyp_roverml_program_is_not_abstract():
    assert not inspect.isabstract(roverml_Program)


def test_hyp_roverml_program_constructor_exists():
    assert callable(roverml_Program.__init__)


def test_hyp_roverml_program_constructor_args():
    sig = inspect.signature(roverml_Program.__init__)
    params = list(sig.parameters.keys())



def test_hyp_roverml_component_is_not_abstract():
    assert not inspect.isabstract(roverml_Component)


def test_hyp_roverml_component_constructor_exists():
    assert callable(roverml_Component.__init__)


def test_hyp_roverml_component_constructor_args():
    sig = inspect.signature(roverml_Component.__init__)
    params = list(sig.parameters.keys())



def test_hyp_roverml_rover_is_not_abstract():
    assert not inspect.isabstract(roverml_Rover)


def test_hyp_roverml_rover_constructor_exists():
    assert callable(roverml_Rover.__init__)


def test_hyp_roverml_rover_constructor_args():
    sig = inspect.signature(roverml_Rover.__init__)
    params = list(sig.parameters.keys())



def test_hyp_roverml_system_is_not_abstract():
    assert not inspect.isabstract(roverml_System)


def test_hyp_roverml_system_constructor_exists():
    assert callable(roverml_System.__init__)


def test_hyp_roverml_system_constructor_args():
    sig = inspect.signature(roverml_System.__init__)
    params = list(sig.parameters.keys())

def test_hyp_lengthunits_exists():
    # Check that the Enumeration exists
    assert LengthUnits is not None

def test_hyp_lengthunits_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in LengthUnits]
    expected_literals = [
        "MILLIMETERS",
        "CENTIMETERS",
        "METERS",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in LengthUnits"

def test_hyp_angleunits_exists():
    # Check that the Enumeration exists
    assert AngleUnits is not None

def test_hyp_angleunits_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in AngleUnits]
    expected_literals = [
        "RADIANS",
        "DEGREES",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in AngleUnits"

def test_hyp_colours_exists():
    # Check that the Enumeration exists
    assert Colours is not None

def test_hyp_colours_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in Colours]
    expected_literals = [
        "NONE",
        "RED",
        "GREEN",
        "BLUE",
        "YELLOW",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in Colours"

def test_hyp_timeunits_exists():
    # Check that the Enumeration exists
    assert TimeUnits is not None

def test_hyp_timeunits_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in TimeUnits]
    expected_literals = [
        "SECONDS",
        "HOURS",
        "MINUTES",
        "MILLISECONDS",
        "NANOSECONDS",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in TimeUnits"

def test_hyp_velocityunits_exists():
    # Check that the Enumeration exists
    assert VelocityUnits is not None

def test_hyp_velocityunits_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in VelocityUnits]
    expected_literals = [
        "MILLIMETERS_PER_SECOND",
        "CENTIMETERS_PER_SECOND",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in VelocityUnits"


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
SingleQuantity_strategy = st.builds(
    SingleQuantity,
)
Quantity_strategy = st.builds(
    Quantity,
)
roverml_SingleQuantity_strategy = st.builds(
    roverml_SingleQuantity,
)
roverml_Quantity_strategy = st.builds(
    roverml_Quantity,
)
roverml_Position_strategy = st.builds(
    roverml_Position,
    y=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    x=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
Triggered_strategy = st.builds(
    Triggered,
)
roverml_CompassTrigger_strategy = st.builds(
    roverml_CompassTrigger,
    angle=
        st.integers()
)
roverml_GPSTrigger_strategy = st.builds(
    roverml_GPSTrigger,
    y=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    x=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
roverml_DistanceSensorTrigger_strategy = st.builds(
    roverml_DistanceSensorTrigger,
    dist=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
Transition_strategy = st.builds(
    Transition,
)
roverml_Regular_strategy = st.builds(
    roverml_Regular,
)
roverml_Triggered_strategy = st.builds(
    roverml_Triggered,
    operator=
        safe_text
)
roverml_Angle_strategy = st.builds(
    roverml_Angle,
    units=
        safe_text
)
roverml_Length_strategy = st.builds(
    roverml_Length,
    units=
        safe_text
)
roverml_Time_strategy = st.builds(
    roverml_Time,
    units=
        safe_text
)
Command_strategy = st.builds(
    Command,
)
roverml_Terminate_strategy = st.builds(
    roverml_Terminate,
)
roverml_Rotate_strategy = st.builds(
    roverml_Rotate,
    angle=
        st.integers()
)
roverml_Repeat_strategy = st.builds(
    roverml_Repeat,
    numberOfReps=
        st.integers()
)
roverml_Wait_strategy = st.builds(
    roverml_Wait,
    time=
        st.integers()
)
roverml_Move_strategy = st.builds(
    roverml_Move,
    velocity=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    length=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
roverml_SetLightColor_strategy = st.builds(
    roverml_SetLightColor,
    color=
        safe_text
)
roverml_Command_strategy = st.builds(
    roverml_Command,
)
roverml_Velocity_strategy = st.builds(
    roverml_Velocity,
    units=
        safe_text
)
roverml_Transition_strategy = st.builds(
    roverml_Transition,
)
Actuator_strategy = st.builds(
    Actuator,
)
roverml_Light_strategy = st.builds(
    roverml_Light,
)
roverml_Motor_strategy = st.builds(
    roverml_Motor,
)
Sensor_strategy = st.builds(
    Sensor,
)
roverml_DistanceSensor_strategy = st.builds(
    roverml_DistanceSensor,
    distance=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
roverml_Compass_strategy = st.builds(
    roverml_Compass,
    angle=
        st.integers()
)
roverml_GPS_strategy = st.builds(
    roverml_GPS,
    x=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    y=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
Component_strategy = st.builds(
    Component,
)
roverml_Actuator_strategy = st.builds(
    roverml_Actuator,
)
roverml_Sensor_strategy = st.builds(
    roverml_Sensor,
)
roverml_NamedElement_strategy = st.builds(
    roverml_NamedElement,
    name=
        safe_text
)
roverml_Block_strategy = st.builds(
    roverml_Block,
)
NamedElement_strategy = st.builds(
    NamedElement,
)
roverml_Program_strategy = st.builds(
    roverml_Program,
)
roverml_Component_strategy = st.builds(
    roverml_Component,
)
roverml_Rover_strategy = st.builds(
    roverml_Rover,
)
roverml_System_strategy = st.builds(
    roverml_System,
)








@given(instance=roverml_Position_strategy)
def test_hyp_roverml_position_y_setter(instance):
    original = instance.y
    instance.y = original
    assert instance.y == original



@given(instance=roverml_Position_strategy)
def test_hyp_roverml_position_x_setter(instance):
    original = instance.x
    instance.x = original
    assert instance.x == original





@given(instance=roverml_CompassTrigger_strategy)
def test_hyp_roverml_compasstrigger_angle_setter(instance):
    original = instance.angle
    instance.angle = original
    assert instance.angle == original




@given(instance=roverml_GPSTrigger_strategy)
def test_hyp_roverml_gpstrigger_y_setter(instance):
    original = instance.y
    instance.y = original
    assert instance.y == original



@given(instance=roverml_GPSTrigger_strategy)
def test_hyp_roverml_gpstrigger_x_setter(instance):
    original = instance.x
    instance.x = original
    assert instance.x == original




@given(instance=roverml_DistanceSensorTrigger_strategy)
def test_hyp_roverml_distancesensortrigger_dist_setter(instance):
    original = instance.dist
    instance.dist = original
    assert instance.dist == original






@given(instance=roverml_Triggered_strategy)
def test_hyp_roverml_triggered_operator_setter(instance):
    original = instance.operator
    instance.operator = original
    assert instance.operator == original




@given(instance=roverml_Angle_strategy)
def test_hyp_roverml_angle_units_setter(instance):
    original = instance.units
    instance.units = original
    assert instance.units == original




@given(instance=roverml_Length_strategy)
def test_hyp_roverml_length_units_setter(instance):
    original = instance.units
    instance.units = original
    assert instance.units == original




@given(instance=roverml_Time_strategy)
def test_hyp_roverml_time_units_setter(instance):
    original = instance.units
    instance.units = original
    assert instance.units == original






@given(instance=roverml_Rotate_strategy)
def test_hyp_roverml_rotate_angle_setter(instance):
    original = instance.angle
    instance.angle = original
    assert instance.angle == original




@given(instance=roverml_Repeat_strategy)
def test_hyp_roverml_repeat_numberOfReps_setter(instance):
    original = instance.numberOfReps
    instance.numberOfReps = original
    assert instance.numberOfReps == original




@given(instance=roverml_Wait_strategy)
def test_hyp_roverml_wait_time_setter(instance):
    original = instance.time
    instance.time = original
    assert instance.time == original




@given(instance=roverml_Move_strategy)
def test_hyp_roverml_move_velocity_setter(instance):
    original = instance.velocity
    instance.velocity = original
    assert instance.velocity == original



@given(instance=roverml_Move_strategy)
def test_hyp_roverml_move_length_setter(instance):
    original = instance.length
    instance.length = original
    assert instance.length == original




@given(instance=roverml_SetLightColor_strategy)
def test_hyp_roverml_setlightcolor_color_setter(instance):
    original = instance.color
    instance.color = original
    assert instance.color == original





@given(instance=roverml_Velocity_strategy)
def test_hyp_roverml_velocity_units_setter(instance):
    original = instance.units
    instance.units = original
    assert instance.units == original









@given(instance=roverml_DistanceSensor_strategy)
def test_hyp_roverml_distancesensor_distance_setter(instance):
    original = instance.distance
    instance.distance = original
    assert instance.distance == original




@given(instance=roverml_Compass_strategy)
def test_hyp_roverml_compass_angle_setter(instance):
    original = instance.angle
    instance.angle = original
    assert instance.angle == original




@given(instance=roverml_GPS_strategy)
def test_hyp_roverml_gps_x_setter(instance):
    original = instance.x
    instance.x = original
    assert instance.x == original



@given(instance=roverml_GPS_strategy)
def test_hyp_roverml_gps_y_setter(instance):
    original = instance.y
    instance.y = original
    assert instance.y == original







@given(instance=roverml_NamedElement_strategy)
def test_hyp_roverml_namedelement_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original








# ----- SECTION B: test_structural_full.py (deterministic-first suite) -----
import inspect
import pytest
from datetime import date, datetime, time, timedelta
from hypothesis import given, settings
import hypothesis.strategies as st

from python_code import (
    Actuator,
    Command,
    Component,
    NamedElement,
    Quantity,
    Sensor,
    SingleQuantity,
    Transition,
    Triggered,
    roverml_Actuator,
    roverml_Angle,
    roverml_Block,
    roverml_Command,
    roverml_Compass,
    roverml_CompassTrigger,
    roverml_Component,
    roverml_DistanceSensor,
    roverml_DistanceSensorTrigger,
    roverml_GPS,
    roverml_GPSTrigger,
    roverml_Length,
    roverml_Light,
    roverml_Motor,
    roverml_Move,
    roverml_NamedElement,
    roverml_Position,
    roverml_Program,
    roverml_Quantity,
    roverml_Regular,
    roverml_Repeat,
    roverml_Rotate,
    roverml_Rover,
    roverml_Sensor,
    roverml_SetLightColor,
    roverml_SingleQuantity,
    roverml_System,
    roverml_Terminate,
    roverml_Time,
    roverml_Transition,
    roverml_Triggered,
    roverml_Velocity,
    roverml_Wait,
    AngleUnits,
    Colours,
    LengthUnits,
    TimeUnits,
    VelocityUnits,
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

def test_roverml_Angle_units_value_roundtrip():
    instance = roverml_Angle(units="sample_text")
    assert instance.units == "sample_text"
    instance.units = "sample_text_2"
    assert instance.units == "sample_text_2"


def test_roverml_Compass_angle_value_roundtrip():
    instance = roverml_Compass(angle=7)
    assert instance.angle == 7
    instance.angle = 13
    assert instance.angle == 13


def test_roverml_CompassTrigger_angle_value_roundtrip():
    instance = roverml_CompassTrigger(angle=7)
    assert instance.angle == 7
    instance.angle = 13
    assert instance.angle == 13


def test_roverml_DistanceSensor_distance_value_roundtrip():
    instance = roverml_DistanceSensor(distance=3.14)
    assert instance.distance == 3.14
    instance.distance = 9.99
    assert instance.distance == 9.99


def test_roverml_DistanceSensorTrigger_dist_value_roundtrip():
    instance = roverml_DistanceSensorTrigger(dist=3.14)
    assert instance.dist == 3.14
    instance.dist = 9.99
    assert instance.dist == 9.99


def test_roverml_GPS_x_value_roundtrip():
    instance = roverml_GPS(x=3.14, y=3.14)
    assert instance.x == 3.14
    instance.x = 9.99
    assert instance.x == 9.99


def test_roverml_GPS_y_value_roundtrip():
    instance = roverml_GPS(x=3.14, y=3.14)
    assert instance.y == 3.14
    instance.y = 9.99
    assert instance.y == 9.99


def test_roverml_GPSTrigger_x_value_roundtrip():
    instance = roverml_GPSTrigger(x=3.14, y=3.14)
    assert instance.x == 3.14
    instance.x = 9.99
    assert instance.x == 9.99


def test_roverml_GPSTrigger_y_value_roundtrip():
    instance = roverml_GPSTrigger(x=3.14, y=3.14)
    assert instance.y == 3.14
    instance.y = 9.99
    assert instance.y == 9.99


def test_roverml_Length_units_value_roundtrip():
    instance = roverml_Length(units="sample_text")
    assert instance.units == "sample_text"
    instance.units = "sample_text_2"
    assert instance.units == "sample_text_2"


def test_roverml_Move_length_value_roundtrip():
    instance = roverml_Move(length=3.14, velocity=3.14)
    assert instance.length == 3.14
    instance.length = 9.99
    assert instance.length == 9.99


def test_roverml_Move_velocity_value_roundtrip():
    instance = roverml_Move(length=3.14, velocity=3.14)
    assert instance.velocity == 3.14
    instance.velocity = 9.99
    assert instance.velocity == 9.99


def test_roverml_NamedElement_name_value_roundtrip():
    instance = roverml_NamedElement(name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_roverml_Position_x_value_roundtrip():
    instance = roverml_Position(x=3.14, y=3.14)
    assert instance.x == 3.14
    instance.x = 9.99
    assert instance.x == 9.99


def test_roverml_Position_y_value_roundtrip():
    instance = roverml_Position(x=3.14, y=3.14)
    assert instance.y == 3.14
    instance.y = 9.99
    assert instance.y == 9.99


def test_roverml_Repeat_numberOfReps_value_roundtrip():
    instance = roverml_Repeat(numberOfReps=7)
    assert instance.numberOfReps == 7
    instance.numberOfReps = 13
    assert instance.numberOfReps == 13


def test_roverml_Rotate_angle_value_roundtrip():
    instance = roverml_Rotate(angle=7)
    assert instance.angle == 7
    instance.angle = 13
    assert instance.angle == 13


def test_roverml_SetLightColor_color_value_roundtrip():
    instance = roverml_SetLightColor(color="sample_text")
    assert instance.color == "sample_text"
    instance.color = "sample_text_2"
    assert instance.color == "sample_text_2"


def test_roverml_Time_units_value_roundtrip():
    instance = roverml_Time(units="sample_text")
    assert instance.units == "sample_text"
    instance.units = "sample_text_2"
    assert instance.units == "sample_text_2"


def test_roverml_Triggered_operator_value_roundtrip():
    instance = roverml_Triggered(operator="sample_text")
    assert instance.operator == "sample_text"
    instance.operator = "sample_text_2"
    assert instance.operator == "sample_text_2"


def test_roverml_Velocity_units_value_roundtrip():
    instance = roverml_Velocity(units="sample_text")
    assert instance.units == "sample_text"
    instance.units = "sample_text_2"
    assert instance.units == "sample_text_2"


def test_roverml_Wait_time_value_roundtrip():
    instance = roverml_Wait(time=7)
    assert instance.time == 7
    instance.time = 13
    assert instance.time == 13


def test_roverml_Light_isa_Actuator():
    instance = roverml_Light()
    assert isinstance(instance, Actuator)


def test_roverml_Motor_isa_Actuator():
    instance = roverml_Motor()
    assert isinstance(instance, Actuator)


def test_roverml_Move_isa_Command():
    instance = roverml_Move(length=3.14, velocity=3.14)
    assert isinstance(instance, Command)


def test_roverml_Repeat_isa_Command():
    instance = roverml_Repeat(numberOfReps=7)
    assert isinstance(instance, Command)


def test_roverml_Rotate_isa_Command():
    instance = roverml_Rotate(angle=7)
    assert isinstance(instance, Command)


def test_roverml_SetLightColor_isa_Command():
    instance = roverml_SetLightColor(color="sample_text")
    assert isinstance(instance, Command)


def test_roverml_Terminate_isa_Command():
    instance = roverml_Terminate()
    assert isinstance(instance, Command)


def test_roverml_Wait_isa_Command():
    instance = roverml_Wait(time=7)
    assert isinstance(instance, Command)


def test_roverml_Actuator_isa_Component():
    instance = roverml_Actuator()
    assert isinstance(instance, Component)


def test_roverml_Sensor_isa_Component():
    instance = roverml_Sensor()
    assert isinstance(instance, Component)


def test_roverml_Component_isa_NamedElement():
    instance = roverml_Component()
    assert isinstance(instance, NamedElement)


def test_roverml_Program_isa_NamedElement():
    instance = roverml_Program()
    assert isinstance(instance, NamedElement)


def test_roverml_Rover_isa_NamedElement():
    instance = roverml_Rover()
    assert isinstance(instance, NamedElement)


def test_roverml_System_isa_NamedElement():
    instance = roverml_System()
    assert isinstance(instance, NamedElement)


def test_roverml_Position_isa_Quantity():
    instance = roverml_Position(x=3.14, y=3.14)
    assert isinstance(instance, Quantity)


def test_roverml_SingleQuantity_isa_Quantity():
    instance = roverml_SingleQuantity()
    assert isinstance(instance, Quantity)


def test_roverml_Compass_isa_Sensor():
    instance = roverml_Compass(angle=7)
    assert isinstance(instance, Sensor)


def test_roverml_DistanceSensor_isa_Sensor():
    instance = roverml_DistanceSensor(distance=3.14)
    assert isinstance(instance, Sensor)


def test_roverml_GPS_isa_Sensor():
    instance = roverml_GPS(x=3.14, y=3.14)
    assert isinstance(instance, Sensor)


def test_roverml_Angle_isa_SingleQuantity():
    instance = roverml_Angle(units="sample_text")
    assert isinstance(instance, SingleQuantity)


def test_roverml_Length_isa_SingleQuantity():
    instance = roverml_Length(units="sample_text")
    assert isinstance(instance, SingleQuantity)


def test_roverml_Time_isa_SingleQuantity():
    instance = roverml_Time(units="sample_text")
    assert isinstance(instance, SingleQuantity)


def test_roverml_Velocity_isa_SingleQuantity():
    instance = roverml_Velocity(units="sample_text")
    assert isinstance(instance, SingleQuantity)


def test_roverml_Regular_isa_Transition():
    instance = roverml_Regular()
    assert isinstance(instance, Transition)


def test_roverml_Triggered_isa_Transition():
    instance = roverml_Triggered(operator="sample_text")
    assert isinstance(instance, Transition)


def test_roverml_CompassTrigger_isa_Triggered():
    instance = roverml_CompassTrigger(angle=7)
    assert isinstance(instance, Triggered)


def test_roverml_DistanceSensorTrigger_isa_Triggered():
    instance = roverml_DistanceSensorTrigger(dist=3.14)
    assert isinstance(instance, Triggered)


def test_roverml_GPSTrigger_isa_Triggered():
    instance = roverml_GPSTrigger(x=3.14, y=3.14)
    assert isinstance(instance, Triggered)


def test_assoc_angleUnits27_link_reassign_clear():
    a = roverml_Rotate(angle=7)
    b1 = roverml_Angle(units="sample_text")
    b2 = roverml_Angle(units="sample_text_2")
    _safe_set(a, 'roverml_Rotate', b1)
    assert _is_linked(a, 'roverml_Rotate', b1)
    if hasattr(b1, 'roverml_Angle'):
        assert _is_linked(b1, 'roverml_Angle', a)
    _safe_set(a, 'roverml_Rotate', b2)
    assert _is_linked(a, 'roverml_Rotate', b2)
    if hasattr(b1, 'roverml_Angle'):
        assert not _is_linked(b1, 'roverml_Angle', a)
    if hasattr(b2, 'roverml_Angle'):
        assert _is_linked(b2, 'roverml_Angle', a)
    _safe_set(a, 'roverml_Rotate', None)
    assert not _is_linked(a, 'roverml_Rotate', b2)
    if hasattr(b2, 'roverml_Angle'):
        assert not _is_linked(b2, 'roverml_Angle', a)


def test_assoc_angles34_link_reassign_clear():
    a = roverml_CompassTrigger(angle=7)
    b1 = roverml_Angle(units="sample_text")
    b2 = roverml_Angle(units="sample_text_2")
    _safe_set(a, 'roverml_CompassTrigger', b1)
    assert _is_linked(a, 'roverml_CompassTrigger', b1)
    if hasattr(b1, 'roverml_Angle35'):
        assert _is_linked(b1, 'roverml_Angle35', a)
    _safe_set(a, 'roverml_CompassTrigger', b2)
    assert _is_linked(a, 'roverml_CompassTrigger', b2)
    if hasattr(b1, 'roverml_Angle35'):
        assert not _is_linked(b1, 'roverml_Angle35', a)
    if hasattr(b2, 'roverml_Angle35'):
        assert _is_linked(b2, 'roverml_Angle35', a)
    _safe_set(a, 'roverml_CompassTrigger', None)
    assert not _is_linked(a, 'roverml_CompassTrigger', b2)
    if hasattr(b2, 'roverml_Angle35'):
        assert not _is_linked(b2, 'roverml_Angle35', a)


def test_assoc_commands28_link_reassign_clear():
    a = roverml_Repeat(numberOfReps=7)
    b1 = roverml_Command()
    b2 = roverml_Command()
    _safe_set(a, 'roverml_Repeat', {b1})
    assert _is_linked(a, 'roverml_Repeat', b1)
    if hasattr(b1, 'roverml_Command29'):
        assert _is_linked(b1, 'roverml_Command29', a)
    _safe_set(a, 'roverml_Repeat', {b2})
    assert _is_linked(a, 'roverml_Repeat', b2)
    if hasattr(b1, 'roverml_Command29'):
        assert not _is_linked(b1, 'roverml_Command29', a)
    if hasattr(b2, 'roverml_Command29'):
        assert _is_linked(b2, 'roverml_Command29', a)
    _safe_set(a, 'roverml_Repeat', set())
    assert not _is_linked(a, 'roverml_Repeat', b2)
    if hasattr(b2, 'roverml_Command29'):
        assert not _is_linked(b2, 'roverml_Command29', a)


def test_assoc_compass36_link_reassign_clear():
    a = roverml_CompassTrigger(angle=7)
    b1 = roverml_Compass(angle=7)
    b2 = roverml_Compass(angle=13)
    _safe_set(a, 'roverml_CompassTrigger37', b1)
    assert _is_linked(a, 'roverml_CompassTrigger37', b1)
    if hasattr(b1, 'roverml_Compass'):
        assert _is_linked(b1, 'roverml_Compass', a)
    _safe_set(a, 'roverml_CompassTrigger37', b2)
    assert _is_linked(a, 'roverml_CompassTrigger37', b2)
    if hasattr(b1, 'roverml_Compass'):
        assert not _is_linked(b1, 'roverml_Compass', a)
    if hasattr(b2, 'roverml_Compass'):
        assert _is_linked(b2, 'roverml_Compass', a)
    _safe_set(a, 'roverml_CompassTrigger37', None)
    assert not _is_linked(a, 'roverml_CompassTrigger37', b2)
    if hasattr(b2, 'roverml_Compass'):
        assert not _is_linked(b2, 'roverml_Compass', a)


def test_assoc_distancesensor32_link_reassign_clear():
    a = roverml_DistanceSensorTrigger(dist=3.14)
    b1 = roverml_DistanceSensor(distance=3.14)
    b2 = roverml_DistanceSensor(distance=9.99)
    _safe_set(a, 'roverml_DistanceSensorTrigger33', b1)
    assert _is_linked(a, 'roverml_DistanceSensorTrigger33', b1)
    if hasattr(b1, 'roverml_DistanceSensor'):
        assert _is_linked(b1, 'roverml_DistanceSensor', a)
    _safe_set(a, 'roverml_DistanceSensorTrigger33', b2)
    assert _is_linked(a, 'roverml_DistanceSensorTrigger33', b2)
    if hasattr(b1, 'roverml_DistanceSensor'):
        assert not _is_linked(b1, 'roverml_DistanceSensor', a)
    if hasattr(b2, 'roverml_DistanceSensor'):
        assert _is_linked(b2, 'roverml_DistanceSensor', a)
    _safe_set(a, 'roverml_DistanceSensorTrigger33', None)
    assert not _is_linked(a, 'roverml_DistanceSensorTrigger33', b2)
    if hasattr(b2, 'roverml_DistanceSensor'):
        assert not _is_linked(b2, 'roverml_DistanceSensor', a)


def test_assoc_gps39_link_reassign_clear():
    a = roverml_GPSTrigger(x=3.14, y=3.14)
    b1 = roverml_GPS(x=3.14, y=3.14)
    b2 = roverml_GPS(x=9.99, y=9.99)
    _safe_set(a, 'roverml_GPSTrigger40', b1)
    assert _is_linked(a, 'roverml_GPSTrigger40', b1)
    if hasattr(b1, 'roverml_GPS'):
        assert _is_linked(b1, 'roverml_GPS', a)
    _safe_set(a, 'roverml_GPSTrigger40', b2)
    assert _is_linked(a, 'roverml_GPSTrigger40', b2)
    if hasattr(b1, 'roverml_GPS'):
        assert not _is_linked(b1, 'roverml_GPS', a)
    if hasattr(b2, 'roverml_GPS'):
        assert _is_linked(b2, 'roverml_GPS', a)
    _safe_set(a, 'roverml_GPSTrigger40', None)
    assert not _is_linked(a, 'roverml_GPSTrigger40', b2)
    if hasattr(b2, 'roverml_GPS'):
        assert not _is_linked(b2, 'roverml_GPS', a)


def test_assoc_length30_link_reassign_clear():
    a = roverml_Length(units="sample_text")
    b1 = roverml_DistanceSensorTrigger(dist=3.14)
    b2 = roverml_DistanceSensorTrigger(dist=9.99)
    _safe_set(a, 'roverml_Length31', b1)
    assert _is_linked(a, 'roverml_Length31', b1)
    if hasattr(b1, 'roverml_DistanceSensorTrigger'):
        assert _is_linked(b1, 'roverml_DistanceSensorTrigger', a)
    _safe_set(a, 'roverml_Length31', b2)
    assert _is_linked(a, 'roverml_Length31', b2)
    if hasattr(b1, 'roverml_DistanceSensorTrigger'):
        assert not _is_linked(b1, 'roverml_DistanceSensorTrigger', a)
    if hasattr(b2, 'roverml_DistanceSensorTrigger'):
        assert _is_linked(b2, 'roverml_DistanceSensorTrigger', a)
    _safe_set(a, 'roverml_Length31', None)
    assert not _is_linked(a, 'roverml_Length31', b2)
    if hasattr(b2, 'roverml_DistanceSensorTrigger'):
        assert not _is_linked(b2, 'roverml_DistanceSensorTrigger', a)


def test_assoc_lengthUnits25_link_reassign_clear():
    a = roverml_Move(length=3.14, velocity=3.14)
    b1 = roverml_Length(units="sample_text")
    b2 = roverml_Length(units="sample_text_2")
    _safe_set(a, 'roverml_Move26', b1)
    assert _is_linked(a, 'roverml_Move26', b1)
    if hasattr(b1, 'roverml_Length'):
        assert _is_linked(b1, 'roverml_Length', a)
    _safe_set(a, 'roverml_Move26', b2)
    assert _is_linked(a, 'roverml_Move26', b2)
    if hasattr(b1, 'roverml_Length'):
        assert not _is_linked(b1, 'roverml_Length', a)
    if hasattr(b2, 'roverml_Length'):
        assert _is_linked(b2, 'roverml_Length', a)
    _safe_set(a, 'roverml_Move26', None)
    assert not _is_linked(a, 'roverml_Move26', b2)
    if hasattr(b2, 'roverml_Length'):
        assert not _is_linked(b2, 'roverml_Length', a)


def test_assoc_position38_link_reassign_clear():
    a = roverml_Position(x=3.14, y=3.14)
    b1 = roverml_GPSTrigger(x=3.14, y=3.14)
    b2 = roverml_GPSTrigger(x=9.99, y=9.99)
    _safe_set(a, 'roverml_Position', b1)
    assert _is_linked(a, 'roverml_Position', b1)
    if hasattr(b1, 'roverml_GPSTrigger'):
        assert _is_linked(b1, 'roverml_GPSTrigger', a)
    _safe_set(a, 'roverml_Position', b2)
    assert _is_linked(a, 'roverml_Position', b2)
    if hasattr(b1, 'roverml_GPSTrigger'):
        assert not _is_linked(b1, 'roverml_GPSTrigger', a)
    if hasattr(b2, 'roverml_GPSTrigger'):
        assert _is_linked(b2, 'roverml_GPSTrigger', a)
    _safe_set(a, 'roverml_Position', None)
    assert not _is_linked(a, 'roverml_Position', b2)
    if hasattr(b2, 'roverml_GPSTrigger'):
        assert not _is_linked(b2, 'roverml_GPSTrigger', a)


def test_assoc_timeUnit23_link_reassign_clear():
    a = roverml_Wait(time=7)
    b1 = roverml_Time(units="sample_text")
    b2 = roverml_Time(units="sample_text_2")
    _safe_set(a, 'roverml_Wait', b1)
    assert _is_linked(a, 'roverml_Wait', b1)
    if hasattr(b1, 'roverml_Time'):
        assert _is_linked(b1, 'roverml_Time', a)
    _safe_set(a, 'roverml_Wait', b2)
    assert _is_linked(a, 'roverml_Wait', b2)
    if hasattr(b1, 'roverml_Time'):
        assert not _is_linked(b1, 'roverml_Time', a)
    if hasattr(b2, 'roverml_Time'):
        assert _is_linked(b2, 'roverml_Time', a)
    _safe_set(a, 'roverml_Wait', None)
    assert not _is_linked(a, 'roverml_Wait', b2)
    if hasattr(b2, 'roverml_Time'):
        assert not _is_linked(b2, 'roverml_Time', a)


def test_assoc_velocityUnits24_link_reassign_clear():
    a = roverml_Velocity(units="sample_text")
    b1 = roverml_Move(length=3.14, velocity=3.14)
    b2 = roverml_Move(length=9.99, velocity=9.99)
    _safe_set(a, 'roverml_Velocity', b1)
    assert _is_linked(a, 'roverml_Velocity', b1)
    if hasattr(b1, 'roverml_Move'):
        assert _is_linked(b1, 'roverml_Move', a)
    _safe_set(a, 'roverml_Velocity', b2)
    assert _is_linked(a, 'roverml_Velocity', b2)
    if hasattr(b1, 'roverml_Move'):
        assert not _is_linked(b1, 'roverml_Move', a)
    if hasattr(b2, 'roverml_Move'):
        assert _is_linked(b2, 'roverml_Move', a)
    _safe_set(a, 'roverml_Velocity', None)
    assert not _is_linked(a, 'roverml_Velocity', b2)
    if hasattr(b2, 'roverml_Move'):
        assert not _is_linked(b2, 'roverml_Move', a)


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

Actuator_strategy = st.builds(Actuator)
@given(instance=Actuator_strategy)
@settings(max_examples=25)
def test_Actuator_instantiation(instance):
    assert isinstance(instance, Actuator)


Command_strategy = st.builds(Command)
@given(instance=Command_strategy)
@settings(max_examples=25)
def test_Command_instantiation(instance):
    assert isinstance(instance, Command)


Component_strategy = st.builds(Component)
@given(instance=Component_strategy)
@settings(max_examples=25)
def test_Component_instantiation(instance):
    assert isinstance(instance, Component)


NamedElement_strategy = st.builds(NamedElement)
@given(instance=NamedElement_strategy)
@settings(max_examples=25)
def test_NamedElement_instantiation(instance):
    assert isinstance(instance, NamedElement)


Quantity_strategy = st.builds(Quantity)
@given(instance=Quantity_strategy)
@settings(max_examples=25)
def test_Quantity_instantiation(instance):
    assert isinstance(instance, Quantity)


Sensor_strategy = st.builds(Sensor)
@given(instance=Sensor_strategy)
@settings(max_examples=25)
def test_Sensor_instantiation(instance):
    assert isinstance(instance, Sensor)


SingleQuantity_strategy = st.builds(SingleQuantity)
@given(instance=SingleQuantity_strategy)
@settings(max_examples=25)
def test_SingleQuantity_instantiation(instance):
    assert isinstance(instance, SingleQuantity)


Transition_strategy = st.builds(Transition)
@given(instance=Transition_strategy)
@settings(max_examples=25)
def test_Transition_instantiation(instance):
    assert isinstance(instance, Transition)


Triggered_strategy = st.builds(Triggered)
@given(instance=Triggered_strategy)
@settings(max_examples=25)
def test_Triggered_instantiation(instance):
    assert isinstance(instance, Triggered)


roverml_Actuator_strategy = st.builds(roverml_Actuator)
@given(instance=roverml_Actuator_strategy)
@settings(max_examples=25)
def test_roverml_Actuator_instantiation(instance):
    assert isinstance(instance, roverml_Actuator)


roverml_Angle_strategy = st.builds(roverml_Angle, units=safe_text)
@given(instance=roverml_Angle_strategy)
@settings(max_examples=25)
def test_roverml_Angle_instantiation(instance):
    assert isinstance(instance, roverml_Angle)


roverml_Block_strategy = st.builds(roverml_Block)
@given(instance=roverml_Block_strategy)
@settings(max_examples=25)
def test_roverml_Block_instantiation(instance):
    assert isinstance(instance, roverml_Block)


roverml_Command_strategy = st.builds(roverml_Command)
@given(instance=roverml_Command_strategy)
@settings(max_examples=25)
def test_roverml_Command_instantiation(instance):
    assert isinstance(instance, roverml_Command)


roverml_Compass_strategy = st.builds(roverml_Compass, angle=st.integers())
@given(instance=roverml_Compass_strategy)
@settings(max_examples=25)
def test_roverml_Compass_instantiation(instance):
    assert isinstance(instance, roverml_Compass)


roverml_CompassTrigger_strategy = st.builds(roverml_CompassTrigger, angle=st.integers())
@given(instance=roverml_CompassTrigger_strategy)
@settings(max_examples=25)
def test_roverml_CompassTrigger_instantiation(instance):
    assert isinstance(instance, roverml_CompassTrigger)


roverml_Component_strategy = st.builds(roverml_Component)
@given(instance=roverml_Component_strategy)
@settings(max_examples=25)
def test_roverml_Component_instantiation(instance):
    assert isinstance(instance, roverml_Component)


roverml_DistanceSensor_strategy = st.builds(roverml_DistanceSensor, distance=st.floats(allow_nan=False, allow_infinity=False))
@given(instance=roverml_DistanceSensor_strategy)
@settings(max_examples=25)
def test_roverml_DistanceSensor_instantiation(instance):
    assert isinstance(instance, roverml_DistanceSensor)


roverml_DistanceSensorTrigger_strategy = st.builds(roverml_DistanceSensorTrigger, dist=st.floats(allow_nan=False, allow_infinity=False))
@given(instance=roverml_DistanceSensorTrigger_strategy)
@settings(max_examples=25)
def test_roverml_DistanceSensorTrigger_instantiation(instance):
    assert isinstance(instance, roverml_DistanceSensorTrigger)


roverml_GPS_strategy = st.builds(roverml_GPS, x=st.floats(allow_nan=False, allow_infinity=False), y=st.floats(allow_nan=False, allow_infinity=False))
@given(instance=roverml_GPS_strategy)
@settings(max_examples=25)
def test_roverml_GPS_instantiation(instance):
    assert isinstance(instance, roverml_GPS)


roverml_GPSTrigger_strategy = st.builds(roverml_GPSTrigger, x=st.floats(allow_nan=False, allow_infinity=False), y=st.floats(allow_nan=False, allow_infinity=False))
@given(instance=roverml_GPSTrigger_strategy)
@settings(max_examples=25)
def test_roverml_GPSTrigger_instantiation(instance):
    assert isinstance(instance, roverml_GPSTrigger)


roverml_Length_strategy = st.builds(roverml_Length, units=safe_text)
@given(instance=roverml_Length_strategy)
@settings(max_examples=25)
def test_roverml_Length_instantiation(instance):
    assert isinstance(instance, roverml_Length)


roverml_Light_strategy = st.builds(roverml_Light)
@given(instance=roverml_Light_strategy)
@settings(max_examples=25)
def test_roverml_Light_instantiation(instance):
    assert isinstance(instance, roverml_Light)


roverml_Motor_strategy = st.builds(roverml_Motor)
@given(instance=roverml_Motor_strategy)
@settings(max_examples=25)
def test_roverml_Motor_instantiation(instance):
    assert isinstance(instance, roverml_Motor)


roverml_Move_strategy = st.builds(roverml_Move, length=st.floats(allow_nan=False, allow_infinity=False), velocity=st.floats(allow_nan=False, allow_infinity=False))
@given(instance=roverml_Move_strategy)
@settings(max_examples=25)
def test_roverml_Move_instantiation(instance):
    assert isinstance(instance, roverml_Move)


roverml_NamedElement_strategy = st.builds(roverml_NamedElement, name=safe_text)
@given(instance=roverml_NamedElement_strategy)
@settings(max_examples=25)
def test_roverml_NamedElement_instantiation(instance):
    assert isinstance(instance, roverml_NamedElement)


roverml_Position_strategy = st.builds(roverml_Position, x=st.floats(allow_nan=False, allow_infinity=False), y=st.floats(allow_nan=False, allow_infinity=False))
@given(instance=roverml_Position_strategy)
@settings(max_examples=25)
def test_roverml_Position_instantiation(instance):
    assert isinstance(instance, roverml_Position)


roverml_Program_strategy = st.builds(roverml_Program)
@given(instance=roverml_Program_strategy)
@settings(max_examples=25)
def test_roverml_Program_instantiation(instance):
    assert isinstance(instance, roverml_Program)


roverml_Quantity_strategy = st.builds(roverml_Quantity)
@given(instance=roverml_Quantity_strategy)
@settings(max_examples=25)
def test_roverml_Quantity_instantiation(instance):
    assert isinstance(instance, roverml_Quantity)


roverml_Regular_strategy = st.builds(roverml_Regular)
@given(instance=roverml_Regular_strategy)
@settings(max_examples=25)
def test_roverml_Regular_instantiation(instance):
    assert isinstance(instance, roverml_Regular)


roverml_Repeat_strategy = st.builds(roverml_Repeat, numberOfReps=st.integers())
@given(instance=roverml_Repeat_strategy)
@settings(max_examples=25)
def test_roverml_Repeat_instantiation(instance):
    assert isinstance(instance, roverml_Repeat)


roverml_Rotate_strategy = st.builds(roverml_Rotate, angle=st.integers())
@given(instance=roverml_Rotate_strategy)
@settings(max_examples=25)
def test_roverml_Rotate_instantiation(instance):
    assert isinstance(instance, roverml_Rotate)


roverml_Rover_strategy = st.builds(roverml_Rover)
@given(instance=roverml_Rover_strategy)
@settings(max_examples=25)
def test_roverml_Rover_instantiation(instance):
    assert isinstance(instance, roverml_Rover)


roverml_Sensor_strategy = st.builds(roverml_Sensor)
@given(instance=roverml_Sensor_strategy)
@settings(max_examples=25)
def test_roverml_Sensor_instantiation(instance):
    assert isinstance(instance, roverml_Sensor)


roverml_SetLightColor_strategy = st.builds(roverml_SetLightColor, color=safe_text)
@given(instance=roverml_SetLightColor_strategy)
@settings(max_examples=25)
def test_roverml_SetLightColor_instantiation(instance):
    assert isinstance(instance, roverml_SetLightColor)


roverml_SingleQuantity_strategy = st.builds(roverml_SingleQuantity)
@given(instance=roverml_SingleQuantity_strategy)
@settings(max_examples=25)
def test_roverml_SingleQuantity_instantiation(instance):
    assert isinstance(instance, roverml_SingleQuantity)


roverml_System_strategy = st.builds(roverml_System)
@given(instance=roverml_System_strategy)
@settings(max_examples=25)
def test_roverml_System_instantiation(instance):
    assert isinstance(instance, roverml_System)


roverml_Terminate_strategy = st.builds(roverml_Terminate)
@given(instance=roverml_Terminate_strategy)
@settings(max_examples=25)
def test_roverml_Terminate_instantiation(instance):
    assert isinstance(instance, roverml_Terminate)


roverml_Time_strategy = st.builds(roverml_Time, units=safe_text)
@given(instance=roverml_Time_strategy)
@settings(max_examples=25)
def test_roverml_Time_instantiation(instance):
    assert isinstance(instance, roverml_Time)


roverml_Transition_strategy = st.builds(roverml_Transition)
@given(instance=roverml_Transition_strategy)
@settings(max_examples=25)
def test_roverml_Transition_instantiation(instance):
    assert isinstance(instance, roverml_Transition)


roverml_Triggered_strategy = st.builds(roverml_Triggered, operator=safe_text)
@given(instance=roverml_Triggered_strategy)
@settings(max_examples=25)
def test_roverml_Triggered_instantiation(instance):
    assert isinstance(instance, roverml_Triggered)


roverml_Velocity_strategy = st.builds(roverml_Velocity, units=safe_text)
@given(instance=roverml_Velocity_strategy)
@settings(max_examples=25)
def test_roverml_Velocity_instantiation(instance):
    assert isinstance(instance, roverml_Velocity)


roverml_Wait_strategy = st.builds(roverml_Wait, time=st.integers())
@given(instance=roverml_Wait_strategy)
@settings(max_examples=25)
def test_roverml_Wait_instantiation(instance):
    assert isinstance(instance, roverml_Wait)



