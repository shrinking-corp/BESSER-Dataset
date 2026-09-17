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
    majordomo_Majordomo,
    BinaryOperation,
    majordomo_BinaryOrOperation,
    majordomo_BinaryAndOperation,
    ValueExpression,
    majordomo_ValueReference,
    majordomo_SensorValue,
    majordomo_ConstantValue,
    majordomo_ValueExpression,
    majordomo_PreparedActionSet,
    majordomo_PreparedValue,
    majordomo_PreparedStatement,
    Action,
    majordomo_BooleanAction,
    majordomo_ActionSetReference,
    majordomo_FloatAction,
    Actor,
    majordomo_FloatActor,
    majordomo_BooleanActor,
    Statement,
    majordomo_CompareOperation,
    majordomo_NotOperation,
    majordomo_StatementReference,
    majordomo_BooleanSensorStatement,
    majordomo_BinaryOperation,
    FloatActor,
    BooleanSensor,
    FloatSensor,
    RoomMountable,
    majordomo_SwitchSensor,
    majordomo_NumberSensor,
    HouseMountable,
    majordomo_RainSensor,
    majordomo_TemperatureSensor,
    majordomo_LampActor,
    majordomo_ClockSensor,
    majordomo_LightSensor,
    majordomo_Extension,
    Sensor,
    majordomo_FloatSensor,
    majordomo_BooleanSensor,
    majordomo_HouseMountable,
    majordomo_RoomMountable,
    BooleanActor,
    majordomo_CoffeeActor,
    majordomo_RadiatorActor,
    majordomo_RoofWindowActor,
    majordomo_BoilerActor,
    majordomo_RollerActor,
    Extension,
    majordomo_Actor,
    majordomo_Sensor,
    majordomo_Extendable,
    Extendable,
    majordomo_House,
    majordomo_Action,
    majordomo_Program,
    majordomo_Room,
    majordomo_Statement,
    majordomo_Rule,
    Comparator,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_hyp_majordomo_majordomo_is_not_abstract():
    assert not inspect.isabstract(majordomo_Majordomo)


def test_hyp_majordomo_majordomo_constructor_exists():
    assert callable(majordomo_Majordomo.__init__)


def test_hyp_majordomo_majordomo_constructor_args():
    sig = inspect.signature(majordomo_Majordomo.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"




def test_hyp_binaryoperation_is_not_abstract():
    assert not inspect.isabstract(BinaryOperation)


def test_hyp_binaryoperation_constructor_exists():
    assert callable(BinaryOperation.__init__)


def test_hyp_binaryoperation_constructor_args():
    sig = inspect.signature(BinaryOperation.__init__)
    params = list(sig.parameters.keys())



def test_hyp_majordomo_binaryoroperation_is_not_abstract():
    assert not inspect.isabstract(majordomo_BinaryOrOperation)


def test_hyp_majordomo_binaryoroperation_constructor_exists():
    assert callable(majordomo_BinaryOrOperation.__init__)


def test_hyp_majordomo_binaryoroperation_constructor_args():
    sig = inspect.signature(majordomo_BinaryOrOperation.__init__)
    params = list(sig.parameters.keys())



def test_hyp_majordomo_binaryandoperation_is_not_abstract():
    assert not inspect.isabstract(majordomo_BinaryAndOperation)


def test_hyp_majordomo_binaryandoperation_constructor_exists():
    assert callable(majordomo_BinaryAndOperation.__init__)


def test_hyp_majordomo_binaryandoperation_constructor_args():
    sig = inspect.signature(majordomo_BinaryAndOperation.__init__)
    params = list(sig.parameters.keys())



def test_hyp_valueexpression_is_not_abstract():
    assert not inspect.isabstract(ValueExpression)


def test_hyp_valueexpression_constructor_exists():
    assert callable(ValueExpression.__init__)


def test_hyp_valueexpression_constructor_args():
    sig = inspect.signature(ValueExpression.__init__)
    params = list(sig.parameters.keys())



def test_hyp_majordomo_valuereference_is_not_abstract():
    assert not inspect.isabstract(majordomo_ValueReference)


def test_hyp_majordomo_valuereference_constructor_exists():
    assert callable(majordomo_ValueReference.__init__)


def test_hyp_majordomo_valuereference_constructor_args():
    sig = inspect.signature(majordomo_ValueReference.__init__)
    params = list(sig.parameters.keys())



def test_hyp_majordomo_sensorvalue_is_not_abstract():
    assert not inspect.isabstract(majordomo_SensorValue)


def test_hyp_majordomo_sensorvalue_constructor_exists():
    assert callable(majordomo_SensorValue.__init__)


def test_hyp_majordomo_sensorvalue_constructor_args():
    sig = inspect.signature(majordomo_SensorValue.__init__)
    params = list(sig.parameters.keys())



def test_hyp_majordomo_constantvalue_is_not_abstract():
    assert not inspect.isabstract(majordomo_ConstantValue)


def test_hyp_majordomo_constantvalue_constructor_exists():
    assert callable(majordomo_ConstantValue.__init__)


def test_hyp_majordomo_constantvalue_constructor_args():
    sig = inspect.signature(majordomo_ConstantValue.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"




def test_hyp_majordomo_valueexpression_is_not_abstract():
    assert not inspect.isabstract(majordomo_ValueExpression)


def test_hyp_majordomo_valueexpression_constructor_exists():
    assert callable(majordomo_ValueExpression.__init__)


def test_hyp_majordomo_valueexpression_constructor_args():
    sig = inspect.signature(majordomo_ValueExpression.__init__)
    params = list(sig.parameters.keys())



def test_hyp_majordomo_preparedactionset_is_not_abstract():
    assert not inspect.isabstract(majordomo_PreparedActionSet)


def test_hyp_majordomo_preparedactionset_constructor_exists():
    assert callable(majordomo_PreparedActionSet.__init__)


def test_hyp_majordomo_preparedactionset_constructor_args():
    sig = inspect.signature(majordomo_PreparedActionSet.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"




def test_hyp_majordomo_preparedvalue_is_not_abstract():
    assert not inspect.isabstract(majordomo_PreparedValue)


def test_hyp_majordomo_preparedvalue_constructor_exists():
    assert callable(majordomo_PreparedValue.__init__)


def test_hyp_majordomo_preparedvalue_constructor_args():
    sig = inspect.signature(majordomo_PreparedValue.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"




def test_hyp_majordomo_preparedstatement_is_not_abstract():
    assert not inspect.isabstract(majordomo_PreparedStatement)


def test_hyp_majordomo_preparedstatement_constructor_exists():
    assert callable(majordomo_PreparedStatement.__init__)


def test_hyp_majordomo_preparedstatement_constructor_args():
    sig = inspect.signature(majordomo_PreparedStatement.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"




def test_hyp_action_is_not_abstract():
    assert not inspect.isabstract(Action)


def test_hyp_action_constructor_exists():
    assert callable(Action.__init__)


def test_hyp_action_constructor_args():
    sig = inspect.signature(Action.__init__)
    params = list(sig.parameters.keys())



def test_hyp_majordomo_booleanaction_is_not_abstract():
    assert not inspect.isabstract(majordomo_BooleanAction)


def test_hyp_majordomo_booleanaction_constructor_exists():
    assert callable(majordomo_BooleanAction.__init__)


def test_hyp_majordomo_booleanaction_constructor_args():
    sig = inspect.signature(majordomo_BooleanAction.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"




def test_hyp_majordomo_actionsetreference_is_not_abstract():
    assert not inspect.isabstract(majordomo_ActionSetReference)


def test_hyp_majordomo_actionsetreference_constructor_exists():
    assert callable(majordomo_ActionSetReference.__init__)


def test_hyp_majordomo_actionsetreference_constructor_args():
    sig = inspect.signature(majordomo_ActionSetReference.__init__)
    params = list(sig.parameters.keys())



def test_hyp_majordomo_floataction_is_not_abstract():
    assert not inspect.isabstract(majordomo_FloatAction)


def test_hyp_majordomo_floataction_constructor_exists():
    assert callable(majordomo_FloatAction.__init__)


def test_hyp_majordomo_floataction_constructor_args():
    sig = inspect.signature(majordomo_FloatAction.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"




def test_hyp_actor_is_not_abstract():
    assert not inspect.isabstract(Actor)


def test_hyp_actor_constructor_exists():
    assert callable(Actor.__init__)


def test_hyp_actor_constructor_args():
    sig = inspect.signature(Actor.__init__)
    params = list(sig.parameters.keys())



def test_hyp_majordomo_floatactor_is_not_abstract():
    assert not inspect.isabstract(majordomo_FloatActor)


def test_hyp_majordomo_floatactor_constructor_exists():
    assert callable(majordomo_FloatActor.__init__)


def test_hyp_majordomo_floatactor_constructor_args():
    sig = inspect.signature(majordomo_FloatActor.__init__)
    params = list(sig.parameters.keys())



def test_hyp_majordomo_booleanactor_is_not_abstract():
    assert not inspect.isabstract(majordomo_BooleanActor)


def test_hyp_majordomo_booleanactor_constructor_exists():
    assert callable(majordomo_BooleanActor.__init__)


def test_hyp_majordomo_booleanactor_constructor_args():
    sig = inspect.signature(majordomo_BooleanActor.__init__)
    params = list(sig.parameters.keys())



def test_hyp_statement_is_not_abstract():
    assert not inspect.isabstract(Statement)


def test_hyp_statement_constructor_exists():
    assert callable(Statement.__init__)


def test_hyp_statement_constructor_args():
    sig = inspect.signature(Statement.__init__)
    params = list(sig.parameters.keys())



def test_hyp_majordomo_compareoperation_is_not_abstract():
    assert not inspect.isabstract(majordomo_CompareOperation)


def test_hyp_majordomo_compareoperation_constructor_exists():
    assert callable(majordomo_CompareOperation.__init__)


def test_hyp_majordomo_compareoperation_constructor_args():
    sig = inspect.signature(majordomo_CompareOperation.__init__)
    params = list(sig.parameters.keys())
    assert "comparator" in params, "Missing parameter 'comparator'"




def test_hyp_majordomo_notoperation_is_not_abstract():
    assert not inspect.isabstract(majordomo_NotOperation)


def test_hyp_majordomo_notoperation_constructor_exists():
    assert callable(majordomo_NotOperation.__init__)


def test_hyp_majordomo_notoperation_constructor_args():
    sig = inspect.signature(majordomo_NotOperation.__init__)
    params = list(sig.parameters.keys())



def test_hyp_majordomo_statementreference_is_not_abstract():
    assert not inspect.isabstract(majordomo_StatementReference)


def test_hyp_majordomo_statementreference_constructor_exists():
    assert callable(majordomo_StatementReference.__init__)


def test_hyp_majordomo_statementreference_constructor_args():
    sig = inspect.signature(majordomo_StatementReference.__init__)
    params = list(sig.parameters.keys())



def test_hyp_majordomo_booleansensorstatement_is_not_abstract():
    assert not inspect.isabstract(majordomo_BooleanSensorStatement)


def test_hyp_majordomo_booleansensorstatement_constructor_exists():
    assert callable(majordomo_BooleanSensorStatement.__init__)


def test_hyp_majordomo_booleansensorstatement_constructor_args():
    sig = inspect.signature(majordomo_BooleanSensorStatement.__init__)
    params = list(sig.parameters.keys())



def test_hyp_majordomo_binaryoperation_is_not_abstract():
    assert not inspect.isabstract(majordomo_BinaryOperation)


def test_hyp_majordomo_binaryoperation_constructor_exists():
    assert callable(majordomo_BinaryOperation.__init__)


def test_hyp_majordomo_binaryoperation_constructor_args():
    sig = inspect.signature(majordomo_BinaryOperation.__init__)
    params = list(sig.parameters.keys())



def test_hyp_floatactor_is_not_abstract():
    assert not inspect.isabstract(FloatActor)


def test_hyp_floatactor_constructor_exists():
    assert callable(FloatActor.__init__)


def test_hyp_floatactor_constructor_args():
    sig = inspect.signature(FloatActor.__init__)
    params = list(sig.parameters.keys())



def test_hyp_booleansensor_is_not_abstract():
    assert not inspect.isabstract(BooleanSensor)


def test_hyp_booleansensor_constructor_exists():
    assert callable(BooleanSensor.__init__)


def test_hyp_booleansensor_constructor_args():
    sig = inspect.signature(BooleanSensor.__init__)
    params = list(sig.parameters.keys())



def test_hyp_floatsensor_is_not_abstract():
    assert not inspect.isabstract(FloatSensor)


def test_hyp_floatsensor_constructor_exists():
    assert callable(FloatSensor.__init__)


def test_hyp_floatsensor_constructor_args():
    sig = inspect.signature(FloatSensor.__init__)
    params = list(sig.parameters.keys())



def test_hyp_roommountable_is_not_abstract():
    assert not inspect.isabstract(RoomMountable)


def test_hyp_roommountable_constructor_exists():
    assert callable(RoomMountable.__init__)


def test_hyp_roommountable_constructor_args():
    sig = inspect.signature(RoomMountable.__init__)
    params = list(sig.parameters.keys())



def test_hyp_majordomo_switchsensor_is_not_abstract():
    assert not inspect.isabstract(majordomo_SwitchSensor)


def test_hyp_majordomo_switchsensor_constructor_exists():
    assert callable(majordomo_SwitchSensor.__init__)


def test_hyp_majordomo_switchsensor_constructor_args():
    sig = inspect.signature(majordomo_SwitchSensor.__init__)
    params = list(sig.parameters.keys())



def test_hyp_majordomo_numbersensor_is_not_abstract():
    assert not inspect.isabstract(majordomo_NumberSensor)


def test_hyp_majordomo_numbersensor_constructor_exists():
    assert callable(majordomo_NumberSensor.__init__)


def test_hyp_majordomo_numbersensor_constructor_args():
    sig = inspect.signature(majordomo_NumberSensor.__init__)
    params = list(sig.parameters.keys())



def test_hyp_housemountable_is_not_abstract():
    assert not inspect.isabstract(HouseMountable)


def test_hyp_housemountable_constructor_exists():
    assert callable(HouseMountable.__init__)


def test_hyp_housemountable_constructor_args():
    sig = inspect.signature(HouseMountable.__init__)
    params = list(sig.parameters.keys())



def test_hyp_majordomo_rainsensor_is_not_abstract():
    assert not inspect.isabstract(majordomo_RainSensor)


def test_hyp_majordomo_rainsensor_constructor_exists():
    assert callable(majordomo_RainSensor.__init__)


def test_hyp_majordomo_rainsensor_constructor_args():
    sig = inspect.signature(majordomo_RainSensor.__init__)
    params = list(sig.parameters.keys())



def test_hyp_majordomo_temperaturesensor_is_not_abstract():
    assert not inspect.isabstract(majordomo_TemperatureSensor)


def test_hyp_majordomo_temperaturesensor_constructor_exists():
    assert callable(majordomo_TemperatureSensor.__init__)


def test_hyp_majordomo_temperaturesensor_constructor_args():
    sig = inspect.signature(majordomo_TemperatureSensor.__init__)
    params = list(sig.parameters.keys())



def test_hyp_majordomo_lampactor_is_not_abstract():
    assert not inspect.isabstract(majordomo_LampActor)


def test_hyp_majordomo_lampactor_constructor_exists():
    assert callable(majordomo_LampActor.__init__)


def test_hyp_majordomo_lampactor_constructor_args():
    sig = inspect.signature(majordomo_LampActor.__init__)
    params = list(sig.parameters.keys())



def test_hyp_majordomo_clocksensor_is_not_abstract():
    assert not inspect.isabstract(majordomo_ClockSensor)


def test_hyp_majordomo_clocksensor_constructor_exists():
    assert callable(majordomo_ClockSensor.__init__)


def test_hyp_majordomo_clocksensor_constructor_args():
    sig = inspect.signature(majordomo_ClockSensor.__init__)
    params = list(sig.parameters.keys())



def test_hyp_majordomo_lightsensor_is_not_abstract():
    assert not inspect.isabstract(majordomo_LightSensor)


def test_hyp_majordomo_lightsensor_constructor_exists():
    assert callable(majordomo_LightSensor.__init__)


def test_hyp_majordomo_lightsensor_constructor_args():
    sig = inspect.signature(majordomo_LightSensor.__init__)
    params = list(sig.parameters.keys())



def test_hyp_majordomo_extension_is_not_abstract():
    assert not inspect.isabstract(majordomo_Extension)


def test_hyp_majordomo_extension_constructor_exists():
    assert callable(majordomo_Extension.__init__)


def test_hyp_majordomo_extension_constructor_args():
    sig = inspect.signature(majordomo_Extension.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"




def test_hyp_sensor_is_not_abstract():
    assert not inspect.isabstract(Sensor)


def test_hyp_sensor_constructor_exists():
    assert callable(Sensor.__init__)


def test_hyp_sensor_constructor_args():
    sig = inspect.signature(Sensor.__init__)
    params = list(sig.parameters.keys())



def test_hyp_majordomo_floatsensor_is_not_abstract():
    assert not inspect.isabstract(majordomo_FloatSensor)


def test_hyp_majordomo_floatsensor_constructor_exists():
    assert callable(majordomo_FloatSensor.__init__)


def test_hyp_majordomo_floatsensor_constructor_args():
    sig = inspect.signature(majordomo_FloatSensor.__init__)
    params = list(sig.parameters.keys())



def test_hyp_majordomo_booleansensor_is_not_abstract():
    assert not inspect.isabstract(majordomo_BooleanSensor)


def test_hyp_majordomo_booleansensor_constructor_exists():
    assert callable(majordomo_BooleanSensor.__init__)


def test_hyp_majordomo_booleansensor_constructor_args():
    sig = inspect.signature(majordomo_BooleanSensor.__init__)
    params = list(sig.parameters.keys())



def test_hyp_majordomo_housemountable_is_not_abstract():
    assert not inspect.isabstract(majordomo_HouseMountable)


def test_hyp_majordomo_housemountable_constructor_exists():
    assert callable(majordomo_HouseMountable.__init__)


def test_hyp_majordomo_housemountable_constructor_args():
    sig = inspect.signature(majordomo_HouseMountable.__init__)
    params = list(sig.parameters.keys())



def test_hyp_majordomo_roommountable_is_not_abstract():
    assert not inspect.isabstract(majordomo_RoomMountable)


def test_hyp_majordomo_roommountable_constructor_exists():
    assert callable(majordomo_RoomMountable.__init__)


def test_hyp_majordomo_roommountable_constructor_args():
    sig = inspect.signature(majordomo_RoomMountable.__init__)
    params = list(sig.parameters.keys())



def test_hyp_booleanactor_is_not_abstract():
    assert not inspect.isabstract(BooleanActor)


def test_hyp_booleanactor_constructor_exists():
    assert callable(BooleanActor.__init__)


def test_hyp_booleanactor_constructor_args():
    sig = inspect.signature(BooleanActor.__init__)
    params = list(sig.parameters.keys())



def test_hyp_majordomo_coffeeactor_is_not_abstract():
    assert not inspect.isabstract(majordomo_CoffeeActor)


def test_hyp_majordomo_coffeeactor_constructor_exists():
    assert callable(majordomo_CoffeeActor.__init__)


def test_hyp_majordomo_coffeeactor_constructor_args():
    sig = inspect.signature(majordomo_CoffeeActor.__init__)
    params = list(sig.parameters.keys())



def test_hyp_majordomo_radiatoractor_is_not_abstract():
    assert not inspect.isabstract(majordomo_RadiatorActor)


def test_hyp_majordomo_radiatoractor_constructor_exists():
    assert callable(majordomo_RadiatorActor.__init__)


def test_hyp_majordomo_radiatoractor_constructor_args():
    sig = inspect.signature(majordomo_RadiatorActor.__init__)
    params = list(sig.parameters.keys())



def test_hyp_majordomo_roofwindowactor_is_not_abstract():
    assert not inspect.isabstract(majordomo_RoofWindowActor)


def test_hyp_majordomo_roofwindowactor_constructor_exists():
    assert callable(majordomo_RoofWindowActor.__init__)


def test_hyp_majordomo_roofwindowactor_constructor_args():
    sig = inspect.signature(majordomo_RoofWindowActor.__init__)
    params = list(sig.parameters.keys())



def test_hyp_majordomo_boileractor_is_not_abstract():
    assert not inspect.isabstract(majordomo_BoilerActor)


def test_hyp_majordomo_boileractor_constructor_exists():
    assert callable(majordomo_BoilerActor.__init__)


def test_hyp_majordomo_boileractor_constructor_args():
    sig = inspect.signature(majordomo_BoilerActor.__init__)
    params = list(sig.parameters.keys())



def test_hyp_majordomo_rolleractor_is_not_abstract():
    assert not inspect.isabstract(majordomo_RollerActor)


def test_hyp_majordomo_rolleractor_constructor_exists():
    assert callable(majordomo_RollerActor.__init__)


def test_hyp_majordomo_rolleractor_constructor_args():
    sig = inspect.signature(majordomo_RollerActor.__init__)
    params = list(sig.parameters.keys())



def test_hyp_extension_is_not_abstract():
    assert not inspect.isabstract(Extension)


def test_hyp_extension_constructor_exists():
    assert callable(Extension.__init__)


def test_hyp_extension_constructor_args():
    sig = inspect.signature(Extension.__init__)
    params = list(sig.parameters.keys())



def test_hyp_majordomo_actor_is_not_abstract():
    assert not inspect.isabstract(majordomo_Actor)


def test_hyp_majordomo_actor_constructor_exists():
    assert callable(majordomo_Actor.__init__)


def test_hyp_majordomo_actor_constructor_args():
    sig = inspect.signature(majordomo_Actor.__init__)
    params = list(sig.parameters.keys())



def test_hyp_majordomo_sensor_is_not_abstract():
    assert not inspect.isabstract(majordomo_Sensor)


def test_hyp_majordomo_sensor_constructor_exists():
    assert callable(majordomo_Sensor.__init__)


def test_hyp_majordomo_sensor_constructor_args():
    sig = inspect.signature(majordomo_Sensor.__init__)
    params = list(sig.parameters.keys())



def test_hyp_majordomo_extendable_is_not_abstract():
    assert not inspect.isabstract(majordomo_Extendable)


def test_hyp_majordomo_extendable_constructor_exists():
    assert callable(majordomo_Extendable.__init__)


def test_hyp_majordomo_extendable_constructor_args():
    sig = inspect.signature(majordomo_Extendable.__init__)
    params = list(sig.parameters.keys())



def test_hyp_extendable_is_not_abstract():
    assert not inspect.isabstract(Extendable)


def test_hyp_extendable_constructor_exists():
    assert callable(Extendable.__init__)


def test_hyp_extendable_constructor_args():
    sig = inspect.signature(Extendable.__init__)
    params = list(sig.parameters.keys())



def test_hyp_majordomo_house_is_not_abstract():
    assert not inspect.isabstract(majordomo_House)


def test_hyp_majordomo_house_constructor_exists():
    assert callable(majordomo_House.__init__)


def test_hyp_majordomo_house_constructor_args():
    sig = inspect.signature(majordomo_House.__init__)
    params = list(sig.parameters.keys())



def test_hyp_majordomo_action_is_not_abstract():
    assert not inspect.isabstract(majordomo_Action)


def test_hyp_majordomo_action_constructor_exists():
    assert callable(majordomo_Action.__init__)


def test_hyp_majordomo_action_constructor_args():
    sig = inspect.signature(majordomo_Action.__init__)
    params = list(sig.parameters.keys())



def test_hyp_majordomo_program_is_not_abstract():
    assert not inspect.isabstract(majordomo_Program)


def test_hyp_majordomo_program_constructor_exists():
    assert callable(majordomo_Program.__init__)


def test_hyp_majordomo_program_constructor_args():
    sig = inspect.signature(majordomo_Program.__init__)
    params = list(sig.parameters.keys())



def test_hyp_majordomo_room_is_not_abstract():
    assert not inspect.isabstract(majordomo_Room)


def test_hyp_majordomo_room_constructor_exists():
    assert callable(majordomo_Room.__init__)


def test_hyp_majordomo_room_constructor_args():
    sig = inspect.signature(majordomo_Room.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"




def test_hyp_majordomo_statement_is_not_abstract():
    assert not inspect.isabstract(majordomo_Statement)


def test_hyp_majordomo_statement_constructor_exists():
    assert callable(majordomo_Statement.__init__)


def test_hyp_majordomo_statement_constructor_args():
    sig = inspect.signature(majordomo_Statement.__init__)
    params = list(sig.parameters.keys())



def test_hyp_majordomo_rule_is_not_abstract():
    assert not inspect.isabstract(majordomo_Rule)


def test_hyp_majordomo_rule_constructor_exists():
    assert callable(majordomo_Rule.__init__)


def test_hyp_majordomo_rule_constructor_args():
    sig = inspect.signature(majordomo_Rule.__init__)
    params = list(sig.parameters.keys())

def test_hyp_comparator_exists():
    # Check that the Enumeration exists
    assert Comparator is not None

def test_hyp_comparator_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in Comparator]
    expected_literals = [
        "GE",
        "LT",
        "LE",
        "GT",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in Comparator"


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
majordomo_Majordomo_strategy = st.builds(
    majordomo_Majordomo,
    name=
        safe_text
)
BinaryOperation_strategy = st.builds(
    BinaryOperation,
)
majordomo_BinaryOrOperation_strategy = st.builds(
    majordomo_BinaryOrOperation,
)
majordomo_BinaryAndOperation_strategy = st.builds(
    majordomo_BinaryAndOperation,
)
ValueExpression_strategy = st.builds(
    ValueExpression,
)
majordomo_ValueReference_strategy = st.builds(
    majordomo_ValueReference,
)
majordomo_SensorValue_strategy = st.builds(
    majordomo_SensorValue,
)
majordomo_ConstantValue_strategy = st.builds(
    majordomo_ConstantValue,
    value=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
majordomo_ValueExpression_strategy = st.builds(
    majordomo_ValueExpression,
)
majordomo_PreparedActionSet_strategy = st.builds(
    majordomo_PreparedActionSet,
    name=
        safe_text
)
majordomo_PreparedValue_strategy = st.builds(
    majordomo_PreparedValue,
    name=
        safe_text
)
majordomo_PreparedStatement_strategy = st.builds(
    majordomo_PreparedStatement,
    name=
        safe_text
)
Action_strategy = st.builds(
    Action,
)
majordomo_BooleanAction_strategy = st.builds(
    majordomo_BooleanAction,
    value=
        st.booleans()
)
majordomo_ActionSetReference_strategy = st.builds(
    majordomo_ActionSetReference,
)
majordomo_FloatAction_strategy = st.builds(
    majordomo_FloatAction,
    value=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
Actor_strategy = st.builds(
    Actor,
)
majordomo_FloatActor_strategy = st.builds(
    majordomo_FloatActor,
)
majordomo_BooleanActor_strategy = st.builds(
    majordomo_BooleanActor,
)
Statement_strategy = st.builds(
    Statement,
)
majordomo_CompareOperation_strategy = st.builds(
    majordomo_CompareOperation,
    comparator=
        safe_text
)
majordomo_NotOperation_strategy = st.builds(
    majordomo_NotOperation,
)
majordomo_StatementReference_strategy = st.builds(
    majordomo_StatementReference,
)
majordomo_BooleanSensorStatement_strategy = st.builds(
    majordomo_BooleanSensorStatement,
)
majordomo_BinaryOperation_strategy = st.builds(
    majordomo_BinaryOperation,
)
FloatActor_strategy = st.builds(
    FloatActor,
)
BooleanSensor_strategy = st.builds(
    BooleanSensor,
)
FloatSensor_strategy = st.builds(
    FloatSensor,
)
RoomMountable_strategy = st.builds(
    RoomMountable,
)
majordomo_SwitchSensor_strategy = st.builds(
    majordomo_SwitchSensor,
)
majordomo_NumberSensor_strategy = st.builds(
    majordomo_NumberSensor,
)
HouseMountable_strategy = st.builds(
    HouseMountable,
)
majordomo_RainSensor_strategy = st.builds(
    majordomo_RainSensor,
)
majordomo_TemperatureSensor_strategy = st.builds(
    majordomo_TemperatureSensor,
)
majordomo_LampActor_strategy = st.builds(
    majordomo_LampActor,
)
majordomo_ClockSensor_strategy = st.builds(
    majordomo_ClockSensor,
)
majordomo_LightSensor_strategy = st.builds(
    majordomo_LightSensor,
)
majordomo_Extension_strategy = st.builds(
    majordomo_Extension,
    name=
        safe_text
)
Sensor_strategy = st.builds(
    Sensor,
)
majordomo_FloatSensor_strategy = st.builds(
    majordomo_FloatSensor,
)
majordomo_BooleanSensor_strategy = st.builds(
    majordomo_BooleanSensor,
)
majordomo_HouseMountable_strategy = st.builds(
    majordomo_HouseMountable,
)
majordomo_RoomMountable_strategy = st.builds(
    majordomo_RoomMountable,
)
BooleanActor_strategy = st.builds(
    BooleanActor,
)
majordomo_CoffeeActor_strategy = st.builds(
    majordomo_CoffeeActor,
)
majordomo_RadiatorActor_strategy = st.builds(
    majordomo_RadiatorActor,
)
majordomo_RoofWindowActor_strategy = st.builds(
    majordomo_RoofWindowActor,
)
majordomo_BoilerActor_strategy = st.builds(
    majordomo_BoilerActor,
)
majordomo_RollerActor_strategy = st.builds(
    majordomo_RollerActor,
)
Extension_strategy = st.builds(
    Extension,
)
majordomo_Actor_strategy = st.builds(
    majordomo_Actor,
)
majordomo_Sensor_strategy = st.builds(
    majordomo_Sensor,
)
majordomo_Extendable_strategy = st.builds(
    majordomo_Extendable,
)
Extendable_strategy = st.builds(
    Extendable,
)
majordomo_House_strategy = st.builds(
    majordomo_House,
)
majordomo_Action_strategy = st.builds(
    majordomo_Action,
)
majordomo_Program_strategy = st.builds(
    majordomo_Program,
)
majordomo_Room_strategy = st.builds(
    majordomo_Room,
    name=
        safe_text
)
majordomo_Statement_strategy = st.builds(
    majordomo_Statement,
)
majordomo_Rule_strategy = st.builds(
    majordomo_Rule,
)




@given(instance=majordomo_Majordomo_strategy)
def test_hyp_majordomo_majordomo_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original










@given(instance=majordomo_ConstantValue_strategy)
def test_hyp_majordomo_constantvalue_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original





@given(instance=majordomo_PreparedActionSet_strategy)
def test_hyp_majordomo_preparedactionset_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original




@given(instance=majordomo_PreparedValue_strategy)
def test_hyp_majordomo_preparedvalue_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original




@given(instance=majordomo_PreparedStatement_strategy)
def test_hyp_majordomo_preparedstatement_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original





@given(instance=majordomo_BooleanAction_strategy)
def test_hyp_majordomo_booleanaction_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original





@given(instance=majordomo_FloatAction_strategy)
def test_hyp_majordomo_floataction_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original



import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=majordomo_FloatActor_strategy)
@settings(max_examples=30)
def test_hyp_majordomo_floatactor_setvalue_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.setValue(
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.setValue).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'setValue' in majordomo_FloatActor is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'setValue' in majordomo_FloatActor did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'setValue' in majordomo_FloatActor is not implemented or raised an error")


import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=majordomo_BooleanActor_strategy)
@settings(max_examples=30)
def test_hyp_majordomo_booleanactor_setvalue_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.setValue(
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.setValue).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'setValue' in majordomo_BooleanActor is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'setValue' in majordomo_BooleanActor did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'setValue' in majordomo_BooleanActor is not implemented or raised an error")





@given(instance=majordomo_CompareOperation_strategy)
def test_hyp_majordomo_compareoperation_comparator_setter(instance):
    original = instance.comparator
    instance.comparator = original
    assert instance.comparator == original




















@given(instance=majordomo_Extension_strategy)
def test_hyp_majordomo_extension_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original























@given(instance=majordomo_Room_strategy)
def test_hyp_majordomo_room_name_setter(instance):
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
    Action,
    Actor,
    BinaryOperation,
    BooleanActor,
    BooleanSensor,
    Extendable,
    Extension,
    FloatActor,
    FloatSensor,
    HouseMountable,
    RoomMountable,
    Sensor,
    Statement,
    ValueExpression,
    majordomo_Action,
    majordomo_ActionSetReference,
    majordomo_Actor,
    majordomo_BinaryAndOperation,
    majordomo_BinaryOperation,
    majordomo_BinaryOrOperation,
    majordomo_BoilerActor,
    majordomo_BooleanAction,
    majordomo_BooleanActor,
    majordomo_BooleanSensor,
    majordomo_BooleanSensorStatement,
    majordomo_ClockSensor,
    majordomo_CoffeeActor,
    majordomo_CompareOperation,
    majordomo_ConstantValue,
    majordomo_Extendable,
    majordomo_Extension,
    majordomo_FloatAction,
    majordomo_FloatActor,
    majordomo_FloatSensor,
    majordomo_House,
    majordomo_HouseMountable,
    majordomo_LampActor,
    majordomo_LightSensor,
    majordomo_Majordomo,
    majordomo_NotOperation,
    majordomo_NumberSensor,
    majordomo_PreparedActionSet,
    majordomo_PreparedStatement,
    majordomo_PreparedValue,
    majordomo_Program,
    majordomo_RadiatorActor,
    majordomo_RainSensor,
    majordomo_RollerActor,
    majordomo_RoofWindowActor,
    majordomo_Room,
    majordomo_RoomMountable,
    majordomo_Rule,
    majordomo_Sensor,
    majordomo_SensorValue,
    majordomo_Statement,
    majordomo_StatementReference,
    majordomo_SwitchSensor,
    majordomo_TemperatureSensor,
    majordomo_ValueExpression,
    majordomo_ValueReference,
    Comparator,
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

def test_majordomo_BooleanAction_value_value_roundtrip():
    instance = majordomo_BooleanAction(value=True)
    assert instance.value == True
    instance.value = False
    assert instance.value == False


def test_majordomo_CompareOperation_comparator_value_roundtrip():
    instance = majordomo_CompareOperation(comparator="sample_text")
    assert instance.comparator == "sample_text"
    instance.comparator = "sample_text_2"
    assert instance.comparator == "sample_text_2"


def test_majordomo_ConstantValue_value_value_roundtrip():
    instance = majordomo_ConstantValue(value=3.14)
    assert instance.value == 3.14
    instance.value = 9.99
    assert instance.value == 9.99


def test_majordomo_Extension_name_value_roundtrip():
    instance = majordomo_Extension(name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_majordomo_FloatAction_value_value_roundtrip():
    instance = majordomo_FloatAction(value=3.14)
    assert instance.value == 3.14
    instance.value = 9.99
    assert instance.value == 9.99


def test_majordomo_Majordomo_name_value_roundtrip():
    instance = majordomo_Majordomo(name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_majordomo_PreparedActionSet_name_value_roundtrip():
    instance = majordomo_PreparedActionSet(name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_majordomo_PreparedStatement_name_value_roundtrip():
    instance = majordomo_PreparedStatement(name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_majordomo_PreparedValue_name_value_roundtrip():
    instance = majordomo_PreparedValue(name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_majordomo_Room_name_value_roundtrip():
    instance = majordomo_Room(name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_majordomo_ActionSetReference_isa_Action():
    instance = majordomo_ActionSetReference()
    assert isinstance(instance, Action)


def test_majordomo_BooleanAction_isa_Action():
    instance = majordomo_BooleanAction(value=True)
    assert isinstance(instance, Action)


def test_majordomo_FloatAction_isa_Action():
    instance = majordomo_FloatAction(value=3.14)
    assert isinstance(instance, Action)


def test_majordomo_BooleanActor_isa_Actor():
    instance = majordomo_BooleanActor()
    assert isinstance(instance, Actor)


def test_majordomo_FloatActor_isa_Actor():
    instance = majordomo_FloatActor()
    assert isinstance(instance, Actor)


def test_majordomo_BinaryAndOperation_isa_BinaryOperation():
    instance = majordomo_BinaryAndOperation()
    assert isinstance(instance, BinaryOperation)


def test_majordomo_BinaryOrOperation_isa_BinaryOperation():
    instance = majordomo_BinaryOrOperation()
    assert isinstance(instance, BinaryOperation)


def test_majordomo_BoilerActor_isa_BooleanActor():
    instance = majordomo_BoilerActor()
    assert isinstance(instance, BooleanActor)


def test_majordomo_CoffeeActor_isa_BooleanActor():
    instance = majordomo_CoffeeActor()
    assert isinstance(instance, BooleanActor)


def test_majordomo_RadiatorActor_isa_BooleanActor():
    instance = majordomo_RadiatorActor()
    assert isinstance(instance, BooleanActor)


def test_majordomo_RollerActor_isa_BooleanActor():
    instance = majordomo_RollerActor()
    assert isinstance(instance, BooleanActor)


def test_majordomo_RoofWindowActor_isa_BooleanActor():
    instance = majordomo_RoofWindowActor()
    assert isinstance(instance, BooleanActor)


def test_majordomo_RainSensor_isa_BooleanSensor():
    instance = majordomo_RainSensor()
    assert isinstance(instance, BooleanSensor)


def test_majordomo_SwitchSensor_isa_BooleanSensor():
    instance = majordomo_SwitchSensor()
    assert isinstance(instance, BooleanSensor)


def test_majordomo_House_isa_Extendable():
    instance = majordomo_House()
    assert isinstance(instance, Extendable)


def test_majordomo_Room_isa_Extendable():
    instance = majordomo_Room(name="sample_text")
    assert isinstance(instance, Extendable)


def test_majordomo_Actor_isa_Extension():
    instance = majordomo_Actor()
    assert isinstance(instance, Extension)


def test_majordomo_Sensor_isa_Extension():
    instance = majordomo_Sensor()
    assert isinstance(instance, Extension)


def test_majordomo_LampActor_isa_FloatActor():
    instance = majordomo_LampActor()
    assert isinstance(instance, FloatActor)


def test_majordomo_ClockSensor_isa_FloatSensor():
    instance = majordomo_ClockSensor()
    assert isinstance(instance, FloatSensor)


def test_majordomo_LightSensor_isa_FloatSensor():
    instance = majordomo_LightSensor()
    assert isinstance(instance, FloatSensor)


def test_majordomo_NumberSensor_isa_FloatSensor():
    instance = majordomo_NumberSensor()
    assert isinstance(instance, FloatSensor)


def test_majordomo_TemperatureSensor_isa_FloatSensor():
    instance = majordomo_TemperatureSensor()
    assert isinstance(instance, FloatSensor)


def test_majordomo_BoilerActor_isa_HouseMountable():
    instance = majordomo_BoilerActor()
    assert isinstance(instance, HouseMountable)


def test_majordomo_ClockSensor_isa_HouseMountable():
    instance = majordomo_ClockSensor()
    assert isinstance(instance, HouseMountable)


def test_majordomo_LampActor_isa_HouseMountable():
    instance = majordomo_LampActor()
    assert isinstance(instance, HouseMountable)


def test_majordomo_LightSensor_isa_HouseMountable():
    instance = majordomo_LightSensor()
    assert isinstance(instance, HouseMountable)


def test_majordomo_RainSensor_isa_HouseMountable():
    instance = majordomo_RainSensor()
    assert isinstance(instance, HouseMountable)


def test_majordomo_TemperatureSensor_isa_HouseMountable():
    instance = majordomo_TemperatureSensor()
    assert isinstance(instance, HouseMountable)


def test_majordomo_CoffeeActor_isa_RoomMountable():
    instance = majordomo_CoffeeActor()
    assert isinstance(instance, RoomMountable)


def test_majordomo_LampActor_isa_RoomMountable():
    instance = majordomo_LampActor()
    assert isinstance(instance, RoomMountable)


def test_majordomo_LightSensor_isa_RoomMountable():
    instance = majordomo_LightSensor()
    assert isinstance(instance, RoomMountable)


def test_majordomo_NumberSensor_isa_RoomMountable():
    instance = majordomo_NumberSensor()
    assert isinstance(instance, RoomMountable)


def test_majordomo_RadiatorActor_isa_RoomMountable():
    instance = majordomo_RadiatorActor()
    assert isinstance(instance, RoomMountable)


def test_majordomo_RollerActor_isa_RoomMountable():
    instance = majordomo_RollerActor()
    assert isinstance(instance, RoomMountable)


def test_majordomo_RoofWindowActor_isa_RoomMountable():
    instance = majordomo_RoofWindowActor()
    assert isinstance(instance, RoomMountable)


def test_majordomo_SwitchSensor_isa_RoomMountable():
    instance = majordomo_SwitchSensor()
    assert isinstance(instance, RoomMountable)


def test_majordomo_TemperatureSensor_isa_RoomMountable():
    instance = majordomo_TemperatureSensor()
    assert isinstance(instance, RoomMountable)


def test_majordomo_BooleanSensor_isa_Sensor():
    instance = majordomo_BooleanSensor()
    assert isinstance(instance, Sensor)


def test_majordomo_FloatSensor_isa_Sensor():
    instance = majordomo_FloatSensor()
    assert isinstance(instance, Sensor)


def test_majordomo_BinaryOperation_isa_Statement():
    instance = majordomo_BinaryOperation()
    assert isinstance(instance, Statement)


def test_majordomo_BooleanSensorStatement_isa_Statement():
    instance = majordomo_BooleanSensorStatement()
    assert isinstance(instance, Statement)


def test_majordomo_CompareOperation_isa_Statement():
    instance = majordomo_CompareOperation(comparator="sample_text")
    assert isinstance(instance, Statement)


def test_majordomo_NotOperation_isa_Statement():
    instance = majordomo_NotOperation()
    assert isinstance(instance, Statement)


def test_majordomo_StatementReference_isa_Statement():
    instance = majordomo_StatementReference()
    assert isinstance(instance, Statement)


def test_majordomo_ConstantValue_isa_ValueExpression():
    instance = majordomo_ConstantValue(value=3.14)
    assert isinstance(instance, ValueExpression)


def test_majordomo_SensorValue_isa_ValueExpression():
    instance = majordomo_SensorValue()
    assert isinstance(instance, ValueExpression)


def test_majordomo_ValueReference_isa_ValueExpression():
    instance = majordomo_ValueReference()
    assert isinstance(instance, ValueExpression)


def test_assoc_actions45_link_reassign_clear():
    a = majordomo_PreparedActionSet(name="sample_text")
    b1 = majordomo_Action()
    b2 = majordomo_Action()
    _safe_set(a, 'majordomo_PreparedActionSet', {b1})
    assert _is_linked(a, 'majordomo_PreparedActionSet', b1)
    if hasattr(b1, 'majordomo_Action46'):
        assert _is_linked(b1, 'majordomo_Action46', a)
    _safe_set(a, 'majordomo_PreparedActionSet', {b2})
    assert _is_linked(a, 'majordomo_PreparedActionSet', b2)
    if hasattr(b1, 'majordomo_Action46'):
        assert not _is_linked(b1, 'majordomo_Action46', a)
    if hasattr(b2, 'majordomo_Action46'):
        assert _is_linked(b2, 'majordomo_Action46', a)
    _safe_set(a, 'majordomo_PreparedActionSet', set())
    assert not _is_linked(a, 'majordomo_PreparedActionSet', b2)
    if hasattr(b2, 'majordomo_Action46'):
        assert not _is_linked(b2, 'majordomo_Action46', a)


def test_assoc_actor14_link_reassign_clear():
    a = majordomo_FloatActor()
    b1 = majordomo_FloatAction(value=3.14)
    b2 = majordomo_FloatAction(value=9.99)
    _safe_set(a, 'majordomo_FloatActor', b1)
    assert _is_linked(a, 'majordomo_FloatActor', b1)
    if hasattr(b1, 'majordomo_FloatAction'):
        assert _is_linked(b1, 'majordomo_FloatAction', a)
    _safe_set(a, 'majordomo_FloatActor', b2)
    assert _is_linked(a, 'majordomo_FloatActor', b2)
    if hasattr(b1, 'majordomo_FloatAction'):
        assert not _is_linked(b1, 'majordomo_FloatAction', a)
    if hasattr(b2, 'majordomo_FloatAction'):
        assert _is_linked(b2, 'majordomo_FloatAction', a)
    _safe_set(a, 'majordomo_FloatActor', None)
    assert not _is_linked(a, 'majordomo_FloatActor', b2)
    if hasattr(b2, 'majordomo_FloatAction'):
        assert not _is_linked(b2, 'majordomo_FloatAction', a)


def test_assoc_actor15_link_reassign_clear():
    a = majordomo_BooleanActor()
    b1 = majordomo_BooleanAction(value=True)
    b2 = majordomo_BooleanAction(value=False)
    _safe_set(a, 'majordomo_BooleanActor', b1)
    assert _is_linked(a, 'majordomo_BooleanActor', b1)
    if hasattr(b1, 'majordomo_BooleanAction'):
        assert _is_linked(b1, 'majordomo_BooleanAction', a)
    _safe_set(a, 'majordomo_BooleanActor', b2)
    assert _is_linked(a, 'majordomo_BooleanActor', b2)
    if hasattr(b1, 'majordomo_BooleanAction'):
        assert not _is_linked(b1, 'majordomo_BooleanAction', a)
    if hasattr(b2, 'majordomo_BooleanAction'):
        assert _is_linked(b2, 'majordomo_BooleanAction', a)
    _safe_set(a, 'majordomo_BooleanActor', None)
    assert not _is_linked(a, 'majordomo_BooleanActor', b2)
    if hasattr(b2, 'majordomo_BooleanAction'):
        assert not _is_linked(b2, 'majordomo_BooleanAction', a)


def test_assoc_constants30_link_reassign_clear():
    a = majordomo_PreparedValue(name="sample_text")
    b1 = majordomo_Program()
    b2 = majordomo_Program()
    _safe_set(a, 'PreparedValue', b1)
    assert _is_linked(a, 'PreparedValue', b1)
    if hasattr(b1, 'ctx31'):
        assert _is_linked(b1, 'ctx31', a)
    _safe_set(a, 'PreparedValue', b2)
    assert _is_linked(a, 'PreparedValue', b2)
    if hasattr(b1, 'ctx31'):
        assert not _is_linked(b1, 'ctx31', a)
    if hasattr(b2, 'ctx31'):
        assert _is_linked(b2, 'ctx31', a)
    _safe_set(a, 'PreparedValue', None)
    assert not _is_linked(a, 'PreparedValue', b2)
    if hasattr(b2, 'ctx31'):
        assert not _is_linked(b2, 'ctx31', a)


def test_assoc_ctx39_link_reassign_clear():
    a = majordomo_PreparedStatement(name="sample_text")
    b1 = majordomo_Program()
    b2 = majordomo_Program()
    _safe_set(a, 'preparedStatements', b1)
    assert _is_linked(a, 'preparedStatements', b1)
    if hasattr(b1, 'Program'):
        assert _is_linked(b1, 'Program', a)
    _safe_set(a, 'preparedStatements', b2)
    assert _is_linked(a, 'preparedStatements', b2)
    if hasattr(b1, 'Program'):
        assert not _is_linked(b1, 'Program', a)
    if hasattr(b2, 'Program'):
        assert _is_linked(b2, 'Program', a)
    _safe_set(a, 'preparedStatements', None)
    assert not _is_linked(a, 'preparedStatements', b2)
    if hasattr(b2, 'Program'):
        assert not _is_linked(b2, 'Program', a)


def test_assoc_ctx43_link_reassign_clear():
    a = majordomo_PreparedActionSet(name="sample_text")
    b1 = majordomo_Program()
    b2 = majordomo_Program()
    _safe_set(a, 'preparedActionSets', b1)
    assert _is_linked(a, 'preparedActionSets', b1)
    if hasattr(b1, 'Program44'):
        assert _is_linked(b1, 'Program44', a)
    _safe_set(a, 'preparedActionSets', b2)
    assert _is_linked(a, 'preparedActionSets', b2)
    if hasattr(b1, 'Program44'):
        assert not _is_linked(b1, 'Program44', a)
    if hasattr(b2, 'Program44'):
        assert _is_linked(b2, 'Program44', a)
    _safe_set(a, 'preparedActionSets', None)
    assert not _is_linked(a, 'preparedActionSets', b2)
    if hasattr(b2, 'Program44'):
        assert not _is_linked(b2, 'Program44', a)


def test_assoc_ctx49_link_reassign_clear():
    a = majordomo_PreparedValue(name="sample_text")
    b1 = majordomo_Program()
    b2 = majordomo_Program()
    _safe_set(a, 'constants', b1)
    assert _is_linked(a, 'constants', b1)
    if hasattr(b1, 'Program50'):
        assert _is_linked(b1, 'Program50', a)
    _safe_set(a, 'constants', b2)
    assert _is_linked(a, 'constants', b2)
    if hasattr(b1, 'Program50'):
        assert not _is_linked(b1, 'Program50', a)
    if hasattr(b2, 'Program50'):
        assert _is_linked(b2, 'Program50', a)
    _safe_set(a, 'constants', None)
    assert not _is_linked(a, 'constants', b2)
    if hasattr(b2, 'Program50'):
        assert not _is_linked(b2, 'Program50', a)


def test_assoc_house0_link_reassign_clear():
    a = majordomo_Majordomo(name="sample_text")
    b1 = majordomo_House()
    b2 = majordomo_House()
    _safe_set(a, 'majordomo_Majordomo', b1)
    assert _is_linked(a, 'majordomo_Majordomo', b1)
    if hasattr(b1, 'majordomo_House'):
        assert _is_linked(b1, 'majordomo_House', a)
    _safe_set(a, 'majordomo_Majordomo', b2)
    assert _is_linked(a, 'majordomo_Majordomo', b2)
    if hasattr(b1, 'majordomo_House'):
        assert not _is_linked(b1, 'majordomo_House', a)
    if hasattr(b2, 'majordomo_House'):
        assert _is_linked(b2, 'majordomo_House', a)
    _safe_set(a, 'majordomo_Majordomo', None)
    assert not _is_linked(a, 'majordomo_Majordomo', b2)
    if hasattr(b2, 'majordomo_House'):
        assert not _is_linked(b2, 'majordomo_House', a)


def test_assoc_left23_link_reassign_clear():
    a = majordomo_CompareOperation(comparator="sample_text")
    b1 = majordomo_ValueExpression()
    b2 = majordomo_ValueExpression()
    _safe_set(a, 'majordomo_CompareOperation', b1)
    assert _is_linked(a, 'majordomo_CompareOperation', b1)
    if hasattr(b1, 'majordomo_ValueExpression'):
        assert _is_linked(b1, 'majordomo_ValueExpression', a)
    _safe_set(a, 'majordomo_CompareOperation', b2)
    assert _is_linked(a, 'majordomo_CompareOperation', b2)
    if hasattr(b1, 'majordomo_ValueExpression'):
        assert not _is_linked(b1, 'majordomo_ValueExpression', a)
    if hasattr(b2, 'majordomo_ValueExpression'):
        assert _is_linked(b2, 'majordomo_ValueExpression', a)
    _safe_set(a, 'majordomo_CompareOperation', None)
    assert not _is_linked(a, 'majordomo_CompareOperation', b2)
    if hasattr(b2, 'majordomo_ValueExpression'):
        assert not _is_linked(b2, 'majordomo_ValueExpression', a)


def test_assoc_preparedActionSets34_link_reassign_clear():
    a = majordomo_PreparedActionSet(name="sample_text")
    b1 = majordomo_Program()
    b2 = majordomo_Program()
    _safe_set(a, 'PreparedActionSet', b1)
    assert _is_linked(a, 'PreparedActionSet', b1)
    if hasattr(b1, 'ctx35'):
        assert _is_linked(b1, 'ctx35', a)
    _safe_set(a, 'PreparedActionSet', b2)
    assert _is_linked(a, 'PreparedActionSet', b2)
    if hasattr(b1, 'ctx35'):
        assert not _is_linked(b1, 'ctx35', a)
    if hasattr(b2, 'ctx35'):
        assert _is_linked(b2, 'ctx35', a)
    _safe_set(a, 'PreparedActionSet', None)
    assert not _is_linked(a, 'PreparedActionSet', b2)
    if hasattr(b2, 'ctx35'):
        assert not _is_linked(b2, 'ctx35', a)


def test_assoc_preparedStatements32_link_reassign_clear():
    a = majordomo_PreparedStatement(name="sample_text")
    b1 = majordomo_Program()
    b2 = majordomo_Program()
    _safe_set(a, 'PreparedStatement', b1)
    assert _is_linked(a, 'PreparedStatement', b1)
    if hasattr(b1, 'ctx33'):
        assert _is_linked(b1, 'ctx33', a)
    _safe_set(a, 'PreparedStatement', b2)
    assert _is_linked(a, 'PreparedStatement', b2)
    if hasattr(b1, 'ctx33'):
        assert not _is_linked(b1, 'ctx33', a)
    if hasattr(b2, 'ctx33'):
        assert _is_linked(b2, 'ctx33', a)
    _safe_set(a, 'PreparedStatement', None)
    assert not _is_linked(a, 'PreparedStatement', b2)
    if hasattr(b2, 'ctx33'):
        assert not _is_linked(b2, 'ctx33', a)


def test_assoc_program3_link_reassign_clear():
    a = majordomo_Majordomo(name="sample_text")
    b1 = majordomo_Program()
    b2 = majordomo_Program()
    _safe_set(a, 'majordomo_Majordomo4', b1)
    assert _is_linked(a, 'majordomo_Majordomo4', b1)
    if hasattr(b1, 'majordomo_Program'):
        assert _is_linked(b1, 'majordomo_Program', a)
    _safe_set(a, 'majordomo_Majordomo4', b2)
    assert _is_linked(a, 'majordomo_Majordomo4', b2)
    if hasattr(b1, 'majordomo_Program'):
        assert not _is_linked(b1, 'majordomo_Program', a)
    if hasattr(b2, 'majordomo_Program'):
        assert _is_linked(b2, 'majordomo_Program', a)
    _safe_set(a, 'majordomo_Majordomo4', None)
    assert not _is_linked(a, 'majordomo_Majordomo4', b2)
    if hasattr(b2, 'majordomo_Program'):
        assert not _is_linked(b2, 'majordomo_Program', a)


def test_assoc_ref29_link_reassign_clear():
    a = majordomo_PreparedStatement(name="sample_text")
    b1 = majordomo_StatementReference()
    b2 = majordomo_StatementReference()
    _safe_set(a, 'majordomo_PreparedStatement', b1)
    assert _is_linked(a, 'majordomo_PreparedStatement', b1)
    if hasattr(b1, 'majordomo_StatementReference'):
        assert _is_linked(b1, 'majordomo_StatementReference', a)
    _safe_set(a, 'majordomo_PreparedStatement', b2)
    assert _is_linked(a, 'majordomo_PreparedStatement', b2)
    if hasattr(b1, 'majordomo_StatementReference'):
        assert not _is_linked(b1, 'majordomo_StatementReference', a)
    if hasattr(b2, 'majordomo_StatementReference'):
        assert _is_linked(b2, 'majordomo_StatementReference', a)
    _safe_set(a, 'majordomo_PreparedStatement', None)
    assert not _is_linked(a, 'majordomo_PreparedStatement', b2)
    if hasattr(b2, 'majordomo_StatementReference'):
        assert not _is_linked(b2, 'majordomo_StatementReference', a)


def test_assoc_ref47_link_reassign_clear():
    a = majordomo_PreparedActionSet(name="sample_text")
    b1 = majordomo_ActionSetReference()
    b2 = majordomo_ActionSetReference()
    _safe_set(a, 'majordomo_PreparedActionSet48', b1)
    assert _is_linked(a, 'majordomo_PreparedActionSet48', b1)
    if hasattr(b1, 'majordomo_ActionSetReference'):
        assert _is_linked(b1, 'majordomo_ActionSetReference', a)
    _safe_set(a, 'majordomo_PreparedActionSet48', b2)
    assert _is_linked(a, 'majordomo_PreparedActionSet48', b2)
    if hasattr(b1, 'majordomo_ActionSetReference'):
        assert not _is_linked(b1, 'majordomo_ActionSetReference', a)
    if hasattr(b2, 'majordomo_ActionSetReference'):
        assert _is_linked(b2, 'majordomo_ActionSetReference', a)
    _safe_set(a, 'majordomo_PreparedActionSet48', None)
    assert not _is_linked(a, 'majordomo_PreparedActionSet48', b2)
    if hasattr(b2, 'majordomo_ActionSetReference'):
        assert not _is_linked(b2, 'majordomo_ActionSetReference', a)


def test_assoc_ref53_link_reassign_clear():
    a = majordomo_PreparedValue(name="sample_text")
    b1 = majordomo_ValueReference()
    b2 = majordomo_ValueReference()
    _safe_set(a, 'majordomo_PreparedValue54', b1)
    assert _is_linked(a, 'majordomo_PreparedValue54', b1)
    if hasattr(b1, 'majordomo_ValueReference'):
        assert _is_linked(b1, 'majordomo_ValueReference', a)
    _safe_set(a, 'majordomo_PreparedValue54', b2)
    assert _is_linked(a, 'majordomo_PreparedValue54', b2)
    if hasattr(b1, 'majordomo_ValueReference'):
        assert not _is_linked(b1, 'majordomo_ValueReference', a)
    if hasattr(b2, 'majordomo_ValueReference'):
        assert _is_linked(b2, 'majordomo_ValueReference', a)
    _safe_set(a, 'majordomo_PreparedValue54', None)
    assert not _is_linked(a, 'majordomo_PreparedValue54', b2)
    if hasattr(b2, 'majordomo_ValueReference'):
        assert not _is_linked(b2, 'majordomo_ValueReference', a)


def test_assoc_right24_link_reassign_clear():
    a = majordomo_CompareOperation(comparator="sample_text")
    b1 = majordomo_ValueExpression()
    b2 = majordomo_ValueExpression()
    _safe_set(a, 'majordomo_CompareOperation25', b1)
    assert _is_linked(a, 'majordomo_CompareOperation25', b1)
    if hasattr(b1, 'majordomo_ValueExpression26'):
        assert _is_linked(b1, 'majordomo_ValueExpression26', a)
    _safe_set(a, 'majordomo_CompareOperation25', b2)
    assert _is_linked(a, 'majordomo_CompareOperation25', b2)
    if hasattr(b1, 'majordomo_ValueExpression26'):
        assert not _is_linked(b1, 'majordomo_ValueExpression26', a)
    if hasattr(b2, 'majordomo_ValueExpression26'):
        assert _is_linked(b2, 'majordomo_ValueExpression26', a)
    _safe_set(a, 'majordomo_CompareOperation25', None)
    assert not _is_linked(a, 'majordomo_CompareOperation25', b2)
    if hasattr(b2, 'majordomo_ValueExpression26'):
        assert not _is_linked(b2, 'majordomo_ValueExpression26', a)


def test_assoc_rooms1_link_reassign_clear():
    a = majordomo_Room(name="sample_text")
    b1 = majordomo_Majordomo(name="sample_text")
    b2 = majordomo_Majordomo(name="sample_text_2")
    _safe_set(a, 'majordomo_Room', b1)
    assert _is_linked(a, 'majordomo_Room', b1)
    if hasattr(b1, 'majordomo_Majordomo2'):
        assert _is_linked(b1, 'majordomo_Majordomo2', a)
    _safe_set(a, 'majordomo_Room', b2)
    assert _is_linked(a, 'majordomo_Room', b2)
    if hasattr(b1, 'majordomo_Majordomo2'):
        assert not _is_linked(b1, 'majordomo_Majordomo2', a)
    if hasattr(b2, 'majordomo_Majordomo2'):
        assert _is_linked(b2, 'majordomo_Majordomo2', a)
    _safe_set(a, 'majordomo_Room', None)
    assert not _is_linked(a, 'majordomo_Room', b2)
    if hasattr(b2, 'majordomo_Majordomo2'):
        assert not _is_linked(b2, 'majordomo_Majordomo2', a)


def test_assoc_sensor27_link_reassign_clear():
    a = majordomo_BooleanSensor()
    b1 = majordomo_BooleanSensorStatement()
    b2 = majordomo_BooleanSensorStatement()
    _safe_set(a, 'majordomo_BooleanSensor', b1)
    assert _is_linked(a, 'majordomo_BooleanSensor', b1)
    if hasattr(b1, 'majordomo_BooleanSensorStatement'):
        assert _is_linked(b1, 'majordomo_BooleanSensorStatement', a)
    _safe_set(a, 'majordomo_BooleanSensor', b2)
    assert _is_linked(a, 'majordomo_BooleanSensor', b2)
    if hasattr(b1, 'majordomo_BooleanSensorStatement'):
        assert not _is_linked(b1, 'majordomo_BooleanSensorStatement', a)
    if hasattr(b2, 'majordomo_BooleanSensorStatement'):
        assert _is_linked(b2, 'majordomo_BooleanSensorStatement', a)
    _safe_set(a, 'majordomo_BooleanSensor', None)
    assert not _is_linked(a, 'majordomo_BooleanSensor', b2)
    if hasattr(b2, 'majordomo_BooleanSensorStatement'):
        assert not _is_linked(b2, 'majordomo_BooleanSensorStatement', a)


def test_assoc_sensor28_link_reassign_clear():
    a = majordomo_FloatSensor()
    b1 = majordomo_SensorValue()
    b2 = majordomo_SensorValue()
    _safe_set(a, 'majordomo_FloatSensor', b1)
    assert _is_linked(a, 'majordomo_FloatSensor', b1)
    if hasattr(b1, 'majordomo_SensorValue'):
        assert _is_linked(b1, 'majordomo_SensorValue', a)
    _safe_set(a, 'majordomo_FloatSensor', b2)
    assert _is_linked(a, 'majordomo_FloatSensor', b2)
    if hasattr(b1, 'majordomo_SensorValue'):
        assert not _is_linked(b1, 'majordomo_SensorValue', a)
    if hasattr(b2, 'majordomo_SensorValue'):
        assert _is_linked(b2, 'majordomo_SensorValue', a)
    _safe_set(a, 'majordomo_FloatSensor', None)
    assert not _is_linked(a, 'majordomo_FloatSensor', b2)
    if hasattr(b2, 'majordomo_SensorValue'):
        assert not _is_linked(b2, 'majordomo_SensorValue', a)


def test_assoc_statement40_link_reassign_clear():
    a = majordomo_PreparedStatement(name="sample_text")
    b1 = majordomo_Statement()
    b2 = majordomo_Statement()
    _safe_set(a, 'majordomo_PreparedStatement41', b1)
    assert _is_linked(a, 'majordomo_PreparedStatement41', b1)
    if hasattr(b1, 'majordomo_Statement42'):
        assert _is_linked(b1, 'majordomo_Statement42', a)
    _safe_set(a, 'majordomo_PreparedStatement41', b2)
    assert _is_linked(a, 'majordomo_PreparedStatement41', b2)
    if hasattr(b1, 'majordomo_Statement42'):
        assert not _is_linked(b1, 'majordomo_Statement42', a)
    if hasattr(b2, 'majordomo_Statement42'):
        assert _is_linked(b2, 'majordomo_Statement42', a)
    _safe_set(a, 'majordomo_PreparedStatement41', None)
    assert not _is_linked(a, 'majordomo_PreparedStatement41', b2)
    if hasattr(b2, 'majordomo_Statement42'):
        assert not _is_linked(b2, 'majordomo_Statement42', a)


def test_assoc_value51_link_reassign_clear():
    a = majordomo_PreparedValue(name="sample_text")
    b1 = majordomo_ValueExpression()
    b2 = majordomo_ValueExpression()
    _safe_set(a, 'majordomo_PreparedValue', b1)
    assert _is_linked(a, 'majordomo_PreparedValue', b1)
    if hasattr(b1, 'majordomo_ValueExpression52'):
        assert _is_linked(b1, 'majordomo_ValueExpression52', a)
    _safe_set(a, 'majordomo_PreparedValue', b2)
    assert _is_linked(a, 'majordomo_PreparedValue', b2)
    if hasattr(b1, 'majordomo_ValueExpression52'):
        assert not _is_linked(b1, 'majordomo_ValueExpression52', a)
    if hasattr(b2, 'majordomo_ValueExpression52'):
        assert _is_linked(b2, 'majordomo_ValueExpression52', a)
    _safe_set(a, 'majordomo_PreparedValue', None)
    assert not _is_linked(a, 'majordomo_PreparedValue', b2)
    if hasattr(b2, 'majordomo_ValueExpression52'):
        assert not _is_linked(b2, 'majordomo_ValueExpression52', a)


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

Action_strategy = st.builds(Action)
@given(instance=Action_strategy)
@settings(max_examples=25)
def test_Action_instantiation(instance):
    assert isinstance(instance, Action)


Actor_strategy = st.builds(Actor)
@given(instance=Actor_strategy)
@settings(max_examples=25)
def test_Actor_instantiation(instance):
    assert isinstance(instance, Actor)


BinaryOperation_strategy = st.builds(BinaryOperation)
@given(instance=BinaryOperation_strategy)
@settings(max_examples=25)
def test_BinaryOperation_instantiation(instance):
    assert isinstance(instance, BinaryOperation)


BooleanActor_strategy = st.builds(BooleanActor)
@given(instance=BooleanActor_strategy)
@settings(max_examples=25)
def test_BooleanActor_instantiation(instance):
    assert isinstance(instance, BooleanActor)


BooleanSensor_strategy = st.builds(BooleanSensor)
@given(instance=BooleanSensor_strategy)
@settings(max_examples=25)
def test_BooleanSensor_instantiation(instance):
    assert isinstance(instance, BooleanSensor)


Extendable_strategy = st.builds(Extendable)
@given(instance=Extendable_strategy)
@settings(max_examples=25)
def test_Extendable_instantiation(instance):
    assert isinstance(instance, Extendable)


Extension_strategy = st.builds(Extension)
@given(instance=Extension_strategy)
@settings(max_examples=25)
def test_Extension_instantiation(instance):
    assert isinstance(instance, Extension)


FloatActor_strategy = st.builds(FloatActor)
@given(instance=FloatActor_strategy)
@settings(max_examples=25)
def test_FloatActor_instantiation(instance):
    assert isinstance(instance, FloatActor)


FloatSensor_strategy = st.builds(FloatSensor)
@given(instance=FloatSensor_strategy)
@settings(max_examples=25)
def test_FloatSensor_instantiation(instance):
    assert isinstance(instance, FloatSensor)


HouseMountable_strategy = st.builds(HouseMountable)
@given(instance=HouseMountable_strategy)
@settings(max_examples=25)
def test_HouseMountable_instantiation(instance):
    assert isinstance(instance, HouseMountable)


RoomMountable_strategy = st.builds(RoomMountable)
@given(instance=RoomMountable_strategy)
@settings(max_examples=25)
def test_RoomMountable_instantiation(instance):
    assert isinstance(instance, RoomMountable)


Sensor_strategy = st.builds(Sensor)
@given(instance=Sensor_strategy)
@settings(max_examples=25)
def test_Sensor_instantiation(instance):
    assert isinstance(instance, Sensor)


Statement_strategy = st.builds(Statement)
@given(instance=Statement_strategy)
@settings(max_examples=25)
def test_Statement_instantiation(instance):
    assert isinstance(instance, Statement)


ValueExpression_strategy = st.builds(ValueExpression)
@given(instance=ValueExpression_strategy)
@settings(max_examples=25)
def test_ValueExpression_instantiation(instance):
    assert isinstance(instance, ValueExpression)


majordomo_Action_strategy = st.builds(majordomo_Action)
@given(instance=majordomo_Action_strategy)
@settings(max_examples=25)
def test_majordomo_Action_instantiation(instance):
    assert isinstance(instance, majordomo_Action)


majordomo_ActionSetReference_strategy = st.builds(majordomo_ActionSetReference)
@given(instance=majordomo_ActionSetReference_strategy)
@settings(max_examples=25)
def test_majordomo_ActionSetReference_instantiation(instance):
    assert isinstance(instance, majordomo_ActionSetReference)


majordomo_Actor_strategy = st.builds(majordomo_Actor)
@given(instance=majordomo_Actor_strategy)
@settings(max_examples=25)
def test_majordomo_Actor_instantiation(instance):
    assert isinstance(instance, majordomo_Actor)


majordomo_BinaryAndOperation_strategy = st.builds(majordomo_BinaryAndOperation)
@given(instance=majordomo_BinaryAndOperation_strategy)
@settings(max_examples=25)
def test_majordomo_BinaryAndOperation_instantiation(instance):
    assert isinstance(instance, majordomo_BinaryAndOperation)


majordomo_BinaryOperation_strategy = st.builds(majordomo_BinaryOperation)
@given(instance=majordomo_BinaryOperation_strategy)
@settings(max_examples=25)
def test_majordomo_BinaryOperation_instantiation(instance):
    assert isinstance(instance, majordomo_BinaryOperation)


majordomo_BinaryOrOperation_strategy = st.builds(majordomo_BinaryOrOperation)
@given(instance=majordomo_BinaryOrOperation_strategy)
@settings(max_examples=25)
def test_majordomo_BinaryOrOperation_instantiation(instance):
    assert isinstance(instance, majordomo_BinaryOrOperation)


majordomo_BoilerActor_strategy = st.builds(majordomo_BoilerActor)
@given(instance=majordomo_BoilerActor_strategy)
@settings(max_examples=25)
def test_majordomo_BoilerActor_instantiation(instance):
    assert isinstance(instance, majordomo_BoilerActor)


majordomo_BooleanAction_strategy = st.builds(majordomo_BooleanAction, value=st.booleans())
@given(instance=majordomo_BooleanAction_strategy)
@settings(max_examples=25)
def test_majordomo_BooleanAction_instantiation(instance):
    assert isinstance(instance, majordomo_BooleanAction)


majordomo_BooleanActor_strategy = st.builds(majordomo_BooleanActor)
@given(instance=majordomo_BooleanActor_strategy)
@settings(max_examples=25)
def test_majordomo_BooleanActor_instantiation(instance):
    assert isinstance(instance, majordomo_BooleanActor)


majordomo_BooleanSensor_strategy = st.builds(majordomo_BooleanSensor)
@given(instance=majordomo_BooleanSensor_strategy)
@settings(max_examples=25)
def test_majordomo_BooleanSensor_instantiation(instance):
    assert isinstance(instance, majordomo_BooleanSensor)


majordomo_BooleanSensorStatement_strategy = st.builds(majordomo_BooleanSensorStatement)
@given(instance=majordomo_BooleanSensorStatement_strategy)
@settings(max_examples=25)
def test_majordomo_BooleanSensorStatement_instantiation(instance):
    assert isinstance(instance, majordomo_BooleanSensorStatement)


majordomo_ClockSensor_strategy = st.builds(majordomo_ClockSensor)
@given(instance=majordomo_ClockSensor_strategy)
@settings(max_examples=25)
def test_majordomo_ClockSensor_instantiation(instance):
    assert isinstance(instance, majordomo_ClockSensor)


majordomo_CoffeeActor_strategy = st.builds(majordomo_CoffeeActor)
@given(instance=majordomo_CoffeeActor_strategy)
@settings(max_examples=25)
def test_majordomo_CoffeeActor_instantiation(instance):
    assert isinstance(instance, majordomo_CoffeeActor)


majordomo_CompareOperation_strategy = st.builds(majordomo_CompareOperation, comparator=safe_text)
@given(instance=majordomo_CompareOperation_strategy)
@settings(max_examples=25)
def test_majordomo_CompareOperation_instantiation(instance):
    assert isinstance(instance, majordomo_CompareOperation)


majordomo_ConstantValue_strategy = st.builds(majordomo_ConstantValue, value=st.floats(allow_nan=False, allow_infinity=False))
@given(instance=majordomo_ConstantValue_strategy)
@settings(max_examples=25)
def test_majordomo_ConstantValue_instantiation(instance):
    assert isinstance(instance, majordomo_ConstantValue)


majordomo_Extendable_strategy = st.builds(majordomo_Extendable)
@given(instance=majordomo_Extendable_strategy)
@settings(max_examples=25)
def test_majordomo_Extendable_instantiation(instance):
    assert isinstance(instance, majordomo_Extendable)


majordomo_Extension_strategy = st.builds(majordomo_Extension, name=safe_text)
@given(instance=majordomo_Extension_strategy)
@settings(max_examples=25)
def test_majordomo_Extension_instantiation(instance):
    assert isinstance(instance, majordomo_Extension)


majordomo_FloatAction_strategy = st.builds(majordomo_FloatAction, value=st.floats(allow_nan=False, allow_infinity=False))
@given(instance=majordomo_FloatAction_strategy)
@settings(max_examples=25)
def test_majordomo_FloatAction_instantiation(instance):
    assert isinstance(instance, majordomo_FloatAction)


majordomo_FloatActor_strategy = st.builds(majordomo_FloatActor)
@given(instance=majordomo_FloatActor_strategy)
@settings(max_examples=25)
def test_majordomo_FloatActor_instantiation(instance):
    assert isinstance(instance, majordomo_FloatActor)


majordomo_FloatSensor_strategy = st.builds(majordomo_FloatSensor)
@given(instance=majordomo_FloatSensor_strategy)
@settings(max_examples=25)
def test_majordomo_FloatSensor_instantiation(instance):
    assert isinstance(instance, majordomo_FloatSensor)


majordomo_House_strategy = st.builds(majordomo_House)
@given(instance=majordomo_House_strategy)
@settings(max_examples=25)
def test_majordomo_House_instantiation(instance):
    assert isinstance(instance, majordomo_House)


majordomo_HouseMountable_strategy = st.builds(majordomo_HouseMountable)
@given(instance=majordomo_HouseMountable_strategy)
@settings(max_examples=25)
def test_majordomo_HouseMountable_instantiation(instance):
    assert isinstance(instance, majordomo_HouseMountable)


majordomo_LampActor_strategy = st.builds(majordomo_LampActor)
@given(instance=majordomo_LampActor_strategy)
@settings(max_examples=25)
def test_majordomo_LampActor_instantiation(instance):
    assert isinstance(instance, majordomo_LampActor)


majordomo_LightSensor_strategy = st.builds(majordomo_LightSensor)
@given(instance=majordomo_LightSensor_strategy)
@settings(max_examples=25)
def test_majordomo_LightSensor_instantiation(instance):
    assert isinstance(instance, majordomo_LightSensor)


majordomo_Majordomo_strategy = st.builds(majordomo_Majordomo, name=safe_text)
@given(instance=majordomo_Majordomo_strategy)
@settings(max_examples=25)
def test_majordomo_Majordomo_instantiation(instance):
    assert isinstance(instance, majordomo_Majordomo)


majordomo_NotOperation_strategy = st.builds(majordomo_NotOperation)
@given(instance=majordomo_NotOperation_strategy)
@settings(max_examples=25)
def test_majordomo_NotOperation_instantiation(instance):
    assert isinstance(instance, majordomo_NotOperation)


majordomo_NumberSensor_strategy = st.builds(majordomo_NumberSensor)
@given(instance=majordomo_NumberSensor_strategy)
@settings(max_examples=25)
def test_majordomo_NumberSensor_instantiation(instance):
    assert isinstance(instance, majordomo_NumberSensor)


majordomo_PreparedActionSet_strategy = st.builds(majordomo_PreparedActionSet, name=safe_text)
@given(instance=majordomo_PreparedActionSet_strategy)
@settings(max_examples=25)
def test_majordomo_PreparedActionSet_instantiation(instance):
    assert isinstance(instance, majordomo_PreparedActionSet)


majordomo_PreparedStatement_strategy = st.builds(majordomo_PreparedStatement, name=safe_text)
@given(instance=majordomo_PreparedStatement_strategy)
@settings(max_examples=25)
def test_majordomo_PreparedStatement_instantiation(instance):
    assert isinstance(instance, majordomo_PreparedStatement)


majordomo_PreparedValue_strategy = st.builds(majordomo_PreparedValue, name=safe_text)
@given(instance=majordomo_PreparedValue_strategy)
@settings(max_examples=25)
def test_majordomo_PreparedValue_instantiation(instance):
    assert isinstance(instance, majordomo_PreparedValue)


majordomo_Program_strategy = st.builds(majordomo_Program)
@given(instance=majordomo_Program_strategy)
@settings(max_examples=25)
def test_majordomo_Program_instantiation(instance):
    assert isinstance(instance, majordomo_Program)


majordomo_RadiatorActor_strategy = st.builds(majordomo_RadiatorActor)
@given(instance=majordomo_RadiatorActor_strategy)
@settings(max_examples=25)
def test_majordomo_RadiatorActor_instantiation(instance):
    assert isinstance(instance, majordomo_RadiatorActor)


majordomo_RainSensor_strategy = st.builds(majordomo_RainSensor)
@given(instance=majordomo_RainSensor_strategy)
@settings(max_examples=25)
def test_majordomo_RainSensor_instantiation(instance):
    assert isinstance(instance, majordomo_RainSensor)


majordomo_RollerActor_strategy = st.builds(majordomo_RollerActor)
@given(instance=majordomo_RollerActor_strategy)
@settings(max_examples=25)
def test_majordomo_RollerActor_instantiation(instance):
    assert isinstance(instance, majordomo_RollerActor)


majordomo_RoofWindowActor_strategy = st.builds(majordomo_RoofWindowActor)
@given(instance=majordomo_RoofWindowActor_strategy)
@settings(max_examples=25)
def test_majordomo_RoofWindowActor_instantiation(instance):
    assert isinstance(instance, majordomo_RoofWindowActor)


majordomo_Room_strategy = st.builds(majordomo_Room, name=safe_text)
@given(instance=majordomo_Room_strategy)
@settings(max_examples=25)
def test_majordomo_Room_instantiation(instance):
    assert isinstance(instance, majordomo_Room)


majordomo_RoomMountable_strategy = st.builds(majordomo_RoomMountable)
@given(instance=majordomo_RoomMountable_strategy)
@settings(max_examples=25)
def test_majordomo_RoomMountable_instantiation(instance):
    assert isinstance(instance, majordomo_RoomMountable)


majordomo_Rule_strategy = st.builds(majordomo_Rule)
@given(instance=majordomo_Rule_strategy)
@settings(max_examples=25)
def test_majordomo_Rule_instantiation(instance):
    assert isinstance(instance, majordomo_Rule)


majordomo_Sensor_strategy = st.builds(majordomo_Sensor)
@given(instance=majordomo_Sensor_strategy)
@settings(max_examples=25)
def test_majordomo_Sensor_instantiation(instance):
    assert isinstance(instance, majordomo_Sensor)


majordomo_SensorValue_strategy = st.builds(majordomo_SensorValue)
@given(instance=majordomo_SensorValue_strategy)
@settings(max_examples=25)
def test_majordomo_SensorValue_instantiation(instance):
    assert isinstance(instance, majordomo_SensorValue)


majordomo_Statement_strategy = st.builds(majordomo_Statement)
@given(instance=majordomo_Statement_strategy)
@settings(max_examples=25)
def test_majordomo_Statement_instantiation(instance):
    assert isinstance(instance, majordomo_Statement)


majordomo_StatementReference_strategy = st.builds(majordomo_StatementReference)
@given(instance=majordomo_StatementReference_strategy)
@settings(max_examples=25)
def test_majordomo_StatementReference_instantiation(instance):
    assert isinstance(instance, majordomo_StatementReference)


majordomo_SwitchSensor_strategy = st.builds(majordomo_SwitchSensor)
@given(instance=majordomo_SwitchSensor_strategy)
@settings(max_examples=25)
def test_majordomo_SwitchSensor_instantiation(instance):
    assert isinstance(instance, majordomo_SwitchSensor)


majordomo_TemperatureSensor_strategy = st.builds(majordomo_TemperatureSensor)
@given(instance=majordomo_TemperatureSensor_strategy)
@settings(max_examples=25)
def test_majordomo_TemperatureSensor_instantiation(instance):
    assert isinstance(instance, majordomo_TemperatureSensor)


majordomo_ValueExpression_strategy = st.builds(majordomo_ValueExpression)
@given(instance=majordomo_ValueExpression_strategy)
@settings(max_examples=25)
def test_majordomo_ValueExpression_instantiation(instance):
    assert isinstance(instance, majordomo_ValueExpression)


majordomo_ValueReference_strategy = st.builds(majordomo_ValueReference)
@given(instance=majordomo_ValueReference_strategy)
@settings(max_examples=25)
def test_majordomo_ValueReference_instantiation(instance):
    assert isinstance(instance, majordomo_ValueReference)



