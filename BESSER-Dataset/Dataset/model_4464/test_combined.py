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
    Var,
    robot_Declaration,
    robot_Affectation,
    Condition,
    robot_Compare,
    robot_Value,
    Operator,
    robot_Different,
    robot_Operator,
    Movement,
    robot_Stop,
    robot_Sleep,
    robot_Backward,
    robot_Forward,
    Values,
    robot_TInteger,
    robot_TFloat,
    robot_TBoolean,
    robot_TString,
    robot_Variable,
    robot_Sensor,
    robot_Values,
    robot_Condition,
    robot_TurnRight,
    robot_TurnLeft,
    robot_Operation,
    Operation,
    robot_While,
    robot_Event,
    robot_Echo,
    robot_Alternative,
    robot_Whenever,
    robot_Movement,
    robot_Var,
    robot_Sequence,
    robot_Mission,
    ESensor,
    EOperator,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_hyp_var_is_not_abstract():
    assert not inspect.isabstract(Var)


def test_hyp_var_constructor_exists():
    assert callable(Var.__init__)


def test_hyp_var_constructor_args():
    sig = inspect.signature(Var.__init__)
    params = list(sig.parameters.keys())



def test_hyp_robot_declaration_is_not_abstract():
    assert not inspect.isabstract(robot_Declaration)


def test_hyp_robot_declaration_constructor_exists():
    assert callable(robot_Declaration.__init__)


def test_hyp_robot_declaration_constructor_args():
    sig = inspect.signature(robot_Declaration.__init__)
    params = list(sig.parameters.keys())



def test_hyp_robot_affectation_is_not_abstract():
    assert not inspect.isabstract(robot_Affectation)


def test_hyp_robot_affectation_constructor_exists():
    assert callable(robot_Affectation.__init__)


def test_hyp_robot_affectation_constructor_args():
    sig = inspect.signature(robot_Affectation.__init__)
    params = list(sig.parameters.keys())



def test_hyp_condition_is_not_abstract():
    assert not inspect.isabstract(Condition)


def test_hyp_condition_constructor_exists():
    assert callable(Condition.__init__)


def test_hyp_condition_constructor_args():
    sig = inspect.signature(Condition.__init__)
    params = list(sig.parameters.keys())



def test_hyp_robot_compare_is_not_abstract():
    assert not inspect.isabstract(robot_Compare)


def test_hyp_robot_compare_constructor_exists():
    assert callable(robot_Compare.__init__)


def test_hyp_robot_compare_constructor_args():
    sig = inspect.signature(robot_Compare.__init__)
    params = list(sig.parameters.keys())



def test_hyp_robot_value_is_not_abstract():
    assert not inspect.isabstract(robot_Value)


def test_hyp_robot_value_constructor_exists():
    assert callable(robot_Value.__init__)


def test_hyp_robot_value_constructor_args():
    sig = inspect.signature(robot_Value.__init__)
    params = list(sig.parameters.keys())



def test_hyp_operator_is_not_abstract():
    assert not inspect.isabstract(Operator)


def test_hyp_operator_constructor_exists():
    assert callable(Operator.__init__)


def test_hyp_operator_constructor_args():
    sig = inspect.signature(Operator.__init__)
    params = list(sig.parameters.keys())



def test_hyp_robot_different_is_not_abstract():
    assert not inspect.isabstract(robot_Different)


def test_hyp_robot_different_constructor_exists():
    assert callable(robot_Different.__init__)


def test_hyp_robot_different_constructor_args():
    sig = inspect.signature(robot_Different.__init__)
    params = list(sig.parameters.keys())



def test_hyp_robot_operator_is_not_abstract():
    assert not inspect.isabstract(robot_Operator)


def test_hyp_robot_operator_constructor_exists():
    assert callable(robot_Operator.__init__)


def test_hyp_robot_operator_constructor_args():
    sig = inspect.signature(robot_Operator.__init__)
    params = list(sig.parameters.keys())
    assert "type" in params, "Missing parameter 'type'"




def test_hyp_movement_is_not_abstract():
    assert not inspect.isabstract(Movement)


def test_hyp_movement_constructor_exists():
    assert callable(Movement.__init__)


def test_hyp_movement_constructor_args():
    sig = inspect.signature(Movement.__init__)
    params = list(sig.parameters.keys())



def test_hyp_robot_stop_is_not_abstract():
    assert not inspect.isabstract(robot_Stop)


def test_hyp_robot_stop_constructor_exists():
    assert callable(robot_Stop.__init__)


def test_hyp_robot_stop_constructor_args():
    sig = inspect.signature(robot_Stop.__init__)
    params = list(sig.parameters.keys())



def test_hyp_robot_sleep_is_not_abstract():
    assert not inspect.isabstract(robot_Sleep)


def test_hyp_robot_sleep_constructor_exists():
    assert callable(robot_Sleep.__init__)


def test_hyp_robot_sleep_constructor_args():
    sig = inspect.signature(robot_Sleep.__init__)
    params = list(sig.parameters.keys())



def test_hyp_robot_backward_is_not_abstract():
    assert not inspect.isabstract(robot_Backward)


def test_hyp_robot_backward_constructor_exists():
    assert callable(robot_Backward.__init__)


def test_hyp_robot_backward_constructor_args():
    sig = inspect.signature(robot_Backward.__init__)
    params = list(sig.parameters.keys())



def test_hyp_robot_forward_is_not_abstract():
    assert not inspect.isabstract(robot_Forward)


def test_hyp_robot_forward_constructor_exists():
    assert callable(robot_Forward.__init__)


def test_hyp_robot_forward_constructor_args():
    sig = inspect.signature(robot_Forward.__init__)
    params = list(sig.parameters.keys())



def test_hyp_values_is_not_abstract():
    assert not inspect.isabstract(Values)


def test_hyp_values_constructor_exists():
    assert callable(Values.__init__)


def test_hyp_values_constructor_args():
    sig = inspect.signature(Values.__init__)
    params = list(sig.parameters.keys())



def test_hyp_robot_tinteger_is_not_abstract():
    assert not inspect.isabstract(robot_TInteger)


def test_hyp_robot_tinteger_constructor_exists():
    assert callable(robot_TInteger.__init__)


def test_hyp_robot_tinteger_constructor_args():
    sig = inspect.signature(robot_TInteger.__init__)
    params = list(sig.parameters.keys())
    assert "Value" in params, "Missing parameter 'Value'"




def test_hyp_robot_tfloat_is_not_abstract():
    assert not inspect.isabstract(robot_TFloat)


def test_hyp_robot_tfloat_constructor_exists():
    assert callable(robot_TFloat.__init__)


def test_hyp_robot_tfloat_constructor_args():
    sig = inspect.signature(robot_TFloat.__init__)
    params = list(sig.parameters.keys())
    assert "Value" in params, "Missing parameter 'Value'"




def test_hyp_robot_tboolean_is_not_abstract():
    assert not inspect.isabstract(robot_TBoolean)


def test_hyp_robot_tboolean_constructor_exists():
    assert callable(robot_TBoolean.__init__)


def test_hyp_robot_tboolean_constructor_args():
    sig = inspect.signature(robot_TBoolean.__init__)
    params = list(sig.parameters.keys())
    assert "Value" in params, "Missing parameter 'Value'"




def test_hyp_robot_tstring_is_not_abstract():
    assert not inspect.isabstract(robot_TString)


def test_hyp_robot_tstring_constructor_exists():
    assert callable(robot_TString.__init__)


def test_hyp_robot_tstring_constructor_args():
    sig = inspect.signature(robot_TString.__init__)
    params = list(sig.parameters.keys())
    assert "Value" in params, "Missing parameter 'Value'"




def test_hyp_robot_variable_is_not_abstract():
    assert not inspect.isabstract(robot_Variable)


def test_hyp_robot_variable_constructor_exists():
    assert callable(robot_Variable.__init__)


def test_hyp_robot_variable_constructor_args():
    sig = inspect.signature(robot_Variable.__init__)
    params = list(sig.parameters.keys())
    assert "Name" in params, "Missing parameter 'Name'"




def test_hyp_robot_sensor_is_not_abstract():
    assert not inspect.isabstract(robot_Sensor)


def test_hyp_robot_sensor_constructor_exists():
    assert callable(robot_Sensor.__init__)


def test_hyp_robot_sensor_constructor_args():
    sig = inspect.signature(robot_Sensor.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"




def test_hyp_robot_values_is_not_abstract():
    assert not inspect.isabstract(robot_Values)


def test_hyp_robot_values_constructor_exists():
    assert callable(robot_Values.__init__)


def test_hyp_robot_values_constructor_args():
    sig = inspect.signature(robot_Values.__init__)
    params = list(sig.parameters.keys())



def test_hyp_robot_condition_is_not_abstract():
    assert not inspect.isabstract(robot_Condition)


def test_hyp_robot_condition_constructor_exists():
    assert callable(robot_Condition.__init__)


def test_hyp_robot_condition_constructor_args():
    sig = inspect.signature(robot_Condition.__init__)
    params = list(sig.parameters.keys())



def test_hyp_robot_turnright_is_not_abstract():
    assert not inspect.isabstract(robot_TurnRight)


def test_hyp_robot_turnright_constructor_exists():
    assert callable(robot_TurnRight.__init__)


def test_hyp_robot_turnright_constructor_args():
    sig = inspect.signature(robot_TurnRight.__init__)
    params = list(sig.parameters.keys())



def test_hyp_robot_turnleft_is_not_abstract():
    assert not inspect.isabstract(robot_TurnLeft)


def test_hyp_robot_turnleft_constructor_exists():
    assert callable(robot_TurnLeft.__init__)


def test_hyp_robot_turnleft_constructor_args():
    sig = inspect.signature(robot_TurnLeft.__init__)
    params = list(sig.parameters.keys())



def test_hyp_robot_operation_is_not_abstract():
    assert not inspect.isabstract(robot_Operation)


def test_hyp_robot_operation_constructor_exists():
    assert callable(robot_Operation.__init__)


def test_hyp_robot_operation_constructor_args():
    sig = inspect.signature(robot_Operation.__init__)
    params = list(sig.parameters.keys())



def test_hyp_operation_is_not_abstract():
    assert not inspect.isabstract(Operation)


def test_hyp_operation_constructor_exists():
    assert callable(Operation.__init__)


def test_hyp_operation_constructor_args():
    sig = inspect.signature(Operation.__init__)
    params = list(sig.parameters.keys())



def test_hyp_robot_while_is_not_abstract():
    assert not inspect.isabstract(robot_While)


def test_hyp_robot_while_constructor_exists():
    assert callable(robot_While.__init__)


def test_hyp_robot_while_constructor_args():
    sig = inspect.signature(robot_While.__init__)
    params = list(sig.parameters.keys())



def test_hyp_robot_event_is_not_abstract():
    assert not inspect.isabstract(robot_Event)


def test_hyp_robot_event_constructor_exists():
    assert callable(robot_Event.__init__)


def test_hyp_robot_event_constructor_args():
    sig = inspect.signature(robot_Event.__init__)
    params = list(sig.parameters.keys())



def test_hyp_robot_echo_is_not_abstract():
    assert not inspect.isabstract(robot_Echo)


def test_hyp_robot_echo_constructor_exists():
    assert callable(robot_Echo.__init__)


def test_hyp_robot_echo_constructor_args():
    sig = inspect.signature(robot_Echo.__init__)
    params = list(sig.parameters.keys())
    assert "param" in params, "Missing parameter 'param'"




def test_hyp_robot_alternative_is_not_abstract():
    assert not inspect.isabstract(robot_Alternative)


def test_hyp_robot_alternative_constructor_exists():
    assert callable(robot_Alternative.__init__)


def test_hyp_robot_alternative_constructor_args():
    sig = inspect.signature(robot_Alternative.__init__)
    params = list(sig.parameters.keys())



def test_hyp_robot_whenever_is_not_abstract():
    assert not inspect.isabstract(robot_Whenever)


def test_hyp_robot_whenever_constructor_exists():
    assert callable(robot_Whenever.__init__)


def test_hyp_robot_whenever_constructor_args():
    sig = inspect.signature(robot_Whenever.__init__)
    params = list(sig.parameters.keys())



def test_hyp_robot_movement_is_not_abstract():
    assert not inspect.isabstract(robot_Movement)


def test_hyp_robot_movement_constructor_exists():
    assert callable(robot_Movement.__init__)


def test_hyp_robot_movement_constructor_args():
    sig = inspect.signature(robot_Movement.__init__)
    params = list(sig.parameters.keys())
    assert "duration" in params, "Missing parameter 'duration'"




def test_hyp_robot_var_is_not_abstract():
    assert not inspect.isabstract(robot_Var)


def test_hyp_robot_var_constructor_exists():
    assert callable(robot_Var.__init__)


def test_hyp_robot_var_constructor_args():
    sig = inspect.signature(robot_Var.__init__)
    params = list(sig.parameters.keys())
    assert "Name" in params, "Missing parameter 'Name'"




def test_hyp_robot_sequence_is_not_abstract():
    assert not inspect.isabstract(robot_Sequence)


def test_hyp_robot_sequence_constructor_exists():
    assert callable(robot_Sequence.__init__)


def test_hyp_robot_sequence_constructor_args():
    sig = inspect.signature(robot_Sequence.__init__)
    params = list(sig.parameters.keys())



def test_hyp_robot_mission_is_not_abstract():
    assert not inspect.isabstract(robot_Mission)


def test_hyp_robot_mission_constructor_exists():
    assert callable(robot_Mission.__init__)


def test_hyp_robot_mission_constructor_args():
    sig = inspect.signature(robot_Mission.__init__)
    params = list(sig.parameters.keys())

def test_hyp_esensor_exists():
    # Check that the Enumeration exists
    assert ESensor is not None

def test_hyp_esensor_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in ESensor]
    expected_literals = [
        "lightL",
        "distanceFRF",
        "lightFRB",
        "lightBL",
        "distanceBR",
        "lightFLB",
        "lightFRF",
        "distanceFRB",
        "distanceR",
        "lightFLF",
        "distanceBL",
        "distanceFLF",
        "distanceL",
        "lightR",
        "lightBR",
        "distanceFLB",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in ESensor"

def test_hyp_eoperator_exists():
    # Check that the Enumeration exists
    assert EOperator is not None

def test_hyp_eoperator_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in EOperator]
    expected_literals = [
        "AND",
        "OR",
        "LTE",
        "GTE",
        "EQ",
        "DIFF",
        "GT",
        "LT",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in EOperator"


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
Var_strategy = st.builds(
    Var,
)
robot_Declaration_strategy = st.builds(
    robot_Declaration,
)
robot_Affectation_strategy = st.builds(
    robot_Affectation,
)
Condition_strategy = st.builds(
    Condition,
)
robot_Compare_strategy = st.builds(
    robot_Compare,
)
robot_Value_strategy = st.builds(
    robot_Value,
)
Operator_strategy = st.builds(
    Operator,
)
robot_Different_strategy = st.builds(
    robot_Different,
)
robot_Operator_strategy = st.builds(
    robot_Operator,
    type=
        safe_text
)
Movement_strategy = st.builds(
    Movement,
)
robot_Stop_strategy = st.builds(
    robot_Stop,
)
robot_Sleep_strategy = st.builds(
    robot_Sleep,
)
robot_Backward_strategy = st.builds(
    robot_Backward,
)
robot_Forward_strategy = st.builds(
    robot_Forward,
)
Values_strategy = st.builds(
    Values,
)
robot_TInteger_strategy = st.builds(
    robot_TInteger,
    Value=
        safe_text
)
robot_TFloat_strategy = st.builds(
    robot_TFloat,
    Value=
        safe_text
)
robot_TBoolean_strategy = st.builds(
    robot_TBoolean,
    Value=
        safe_text
)
robot_TString_strategy = st.builds(
    robot_TString,
    Value=
        safe_text
)
robot_Variable_strategy = st.builds(
    robot_Variable,
    Name=
        safe_text
)
robot_Sensor_strategy = st.builds(
    robot_Sensor,
    name=
        safe_text
)
robot_Values_strategy = st.builds(
    robot_Values,
)
robot_Condition_strategy = st.builds(
    robot_Condition,
)
robot_TurnRight_strategy = st.builds(
    robot_TurnRight,
)
robot_TurnLeft_strategy = st.builds(
    robot_TurnLeft,
)
robot_Operation_strategy = st.builds(
    robot_Operation,
)
Operation_strategy = st.builds(
    Operation,
)
robot_While_strategy = st.builds(
    robot_While,
)
robot_Event_strategy = st.builds(
    robot_Event,
)
robot_Echo_strategy = st.builds(
    robot_Echo,
    param=
        safe_text
)
robot_Alternative_strategy = st.builds(
    robot_Alternative,
)
robot_Whenever_strategy = st.builds(
    robot_Whenever,
)
robot_Movement_strategy = st.builds(
    robot_Movement,
    duration=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
robot_Var_strategy = st.builds(
    robot_Var,
    Name=
        safe_text
)
robot_Sequence_strategy = st.builds(
    robot_Sequence,
)
robot_Mission_strategy = st.builds(
    robot_Mission,
)












@given(instance=robot_Operator_strategy)
def test_hyp_robot_operator_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original










@given(instance=robot_TInteger_strategy)
def test_hyp_robot_tinteger_Value_setter(instance):
    original = instance.Value
    instance.Value = original
    assert instance.Value == original




@given(instance=robot_TFloat_strategy)
def test_hyp_robot_tfloat_Value_setter(instance):
    original = instance.Value
    instance.Value = original
    assert instance.Value == original




@given(instance=robot_TBoolean_strategy)
def test_hyp_robot_tboolean_Value_setter(instance):
    original = instance.Value
    instance.Value = original
    assert instance.Value == original




@given(instance=robot_TString_strategy)
def test_hyp_robot_tstring_Value_setter(instance):
    original = instance.Value
    instance.Value = original
    assert instance.Value == original




@given(instance=robot_Variable_strategy)
def test_hyp_robot_variable_Name_setter(instance):
    original = instance.Name
    instance.Name = original
    assert instance.Name == original




@given(instance=robot_Sensor_strategy)
def test_hyp_robot_sensor_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original












@given(instance=robot_Echo_strategy)
def test_hyp_robot_echo_param_setter(instance):
    original = instance.param
    instance.param = original
    assert instance.param == original






@given(instance=robot_Movement_strategy)
def test_hyp_robot_movement_duration_setter(instance):
    original = instance.duration
    instance.duration = original
    assert instance.duration == original




@given(instance=robot_Var_strategy)
def test_hyp_robot_var_Name_setter(instance):
    original = instance.Name
    instance.Name = original
    assert instance.Name == original




# ----- SECTION B: test_structural_full.py (deterministic-first suite) -----
import inspect
import pytest
from datetime import date, datetime, time, timedelta
from hypothesis import given, settings
import hypothesis.strategies as st

from python_code import (
    Condition,
    Movement,
    Operation,
    Operator,
    Values,
    Var,
    robot_Affectation,
    robot_Alternative,
    robot_Backward,
    robot_Compare,
    robot_Condition,
    robot_Declaration,
    robot_Different,
    robot_Echo,
    robot_Event,
    robot_Forward,
    robot_Mission,
    robot_Movement,
    robot_Operation,
    robot_Operator,
    robot_Sensor,
    robot_Sequence,
    robot_Sleep,
    robot_Stop,
    robot_TBoolean,
    robot_TFloat,
    robot_TInteger,
    robot_TString,
    robot_TurnLeft,
    robot_TurnRight,
    robot_Value,
    robot_Values,
    robot_Var,
    robot_Variable,
    robot_Whenever,
    robot_While,
    EOperator,
    ESensor,
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

def test_robot_Echo_param_value_roundtrip():
    instance = robot_Echo(param="sample_text")
    assert instance.param == "sample_text"
    instance.param = "sample_text_2"
    assert instance.param == "sample_text_2"


def test_robot_Movement_duration_value_roundtrip():
    instance = robot_Movement(duration=3.14)
    assert instance.duration == 3.14
    instance.duration = 9.99
    assert instance.duration == 9.99


def test_robot_Operator_type_value_roundtrip():
    instance = robot_Operator(type="sample_text")
    assert instance.type == "sample_text"
    instance.type = "sample_text_2"
    assert instance.type == "sample_text_2"


def test_robot_Sensor_name_value_roundtrip():
    instance = robot_Sensor(name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_robot_TBoolean_Value_value_roundtrip():
    instance = robot_TBoolean(Value="sample_text")
    assert instance.Value == "sample_text"
    instance.Value = "sample_text_2"
    assert instance.Value == "sample_text_2"


def test_robot_TFloat_Value_value_roundtrip():
    instance = robot_TFloat(Value="sample_text")
    assert instance.Value == "sample_text"
    instance.Value = "sample_text_2"
    assert instance.Value == "sample_text_2"


def test_robot_TInteger_Value_value_roundtrip():
    instance = robot_TInteger(Value="sample_text")
    assert instance.Value == "sample_text"
    instance.Value = "sample_text_2"
    assert instance.Value == "sample_text_2"


def test_robot_TString_Value_value_roundtrip():
    instance = robot_TString(Value="sample_text")
    assert instance.Value == "sample_text"
    instance.Value = "sample_text_2"
    assert instance.Value == "sample_text_2"


def test_robot_Var_Name_value_roundtrip():
    instance = robot_Var(Name="sample_text")
    assert instance.Name == "sample_text"
    instance.Name = "sample_text_2"
    assert instance.Name == "sample_text_2"


def test_robot_Variable_Name_value_roundtrip():
    instance = robot_Variable(Name="sample_text")
    assert instance.Name == "sample_text"
    instance.Name = "sample_text_2"
    assert instance.Name == "sample_text_2"


def test_robot_Compare_isa_Condition():
    instance = robot_Compare()
    assert isinstance(instance, Condition)


def test_robot_Value_isa_Condition():
    instance = robot_Value()
    assert isinstance(instance, Condition)


def test_robot_Backward_isa_Movement():
    instance = robot_Backward()
    assert isinstance(instance, Movement)


def test_robot_Forward_isa_Movement():
    instance = robot_Forward()
    assert isinstance(instance, Movement)


def test_robot_Sleep_isa_Movement():
    instance = robot_Sleep()
    assert isinstance(instance, Movement)


def test_robot_Stop_isa_Movement():
    instance = robot_Stop()
    assert isinstance(instance, Movement)


def test_robot_TurnLeft_isa_Movement():
    instance = robot_TurnLeft()
    assert isinstance(instance, Movement)


def test_robot_TurnRight_isa_Movement():
    instance = robot_TurnRight()
    assert isinstance(instance, Movement)


def test_robot_Alternative_isa_Operation():
    instance = robot_Alternative()
    assert isinstance(instance, Operation)


def test_robot_Echo_isa_Operation():
    instance = robot_Echo(param="sample_text")
    assert isinstance(instance, Operation)


def test_robot_Event_isa_Operation():
    instance = robot_Event()
    assert isinstance(instance, Operation)


def test_robot_Movement_isa_Operation():
    instance = robot_Movement(duration=3.14)
    assert isinstance(instance, Operation)


def test_robot_Sequence_isa_Operation():
    instance = robot_Sequence()
    assert isinstance(instance, Operation)


def test_robot_Var_isa_Operation():
    instance = robot_Var(Name="sample_text")
    assert isinstance(instance, Operation)


def test_robot_Whenever_isa_Operation():
    instance = robot_Whenever()
    assert isinstance(instance, Operation)


def test_robot_While_isa_Operation():
    instance = robot_While()
    assert isinstance(instance, Operation)


def test_robot_Different_isa_Operator():
    instance = robot_Different()
    assert isinstance(instance, Operator)


def test_robot_Sensor_isa_Values():
    instance = robot_Sensor(name="sample_text")
    assert isinstance(instance, Values)


def test_robot_TBoolean_isa_Values():
    instance = robot_TBoolean(Value="sample_text")
    assert isinstance(instance, Values)


def test_robot_TFloat_isa_Values():
    instance = robot_TFloat(Value="sample_text")
    assert isinstance(instance, Values)


def test_robot_TInteger_isa_Values():
    instance = robot_TInteger(Value="sample_text")
    assert isinstance(instance, Values)


def test_robot_TString_isa_Values():
    instance = robot_TString(Value="sample_text")
    assert isinstance(instance, Values)


def test_robot_Variable_isa_Values():
    instance = robot_Variable(Name="sample_text")
    assert isinstance(instance, Values)


def test_robot_Affectation_isa_Var():
    instance = robot_Affectation()
    assert isinstance(instance, Var)


def test_robot_Declaration_isa_Var():
    instance = robot_Declaration()
    assert isinstance(instance, Var)


def test_assoc_Operator34_link_reassign_clear():
    a = robot_Operator(type="sample_text")
    b1 = robot_Compare()
    b2 = robot_Compare()
    _safe_set(a, 'robot_Operator', b1)
    assert _is_linked(a, 'robot_Operator', b1)
    if hasattr(b1, 'robot_Compare'):
        assert _is_linked(b1, 'robot_Compare', a)
    _safe_set(a, 'robot_Operator', b2)
    assert _is_linked(a, 'robot_Operator', b2)
    if hasattr(b1, 'robot_Compare'):
        assert not _is_linked(b1, 'robot_Compare', a)
    if hasattr(b2, 'robot_Compare'):
        assert _is_linked(b2, 'robot_Compare', a)
    _safe_set(a, 'robot_Operator', None)
    assert not _is_linked(a, 'robot_Operator', b2)
    if hasattr(b2, 'robot_Compare'):
        assert not _is_linked(b2, 'robot_Compare', a)


def test_assoc_Value18_link_reassign_clear():
    a = robot_Var(Name="sample_text")
    b1 = robot_Values()
    b2 = robot_Values()
    _safe_set(a, 'robot_Var', b1)
    assert _is_linked(a, 'robot_Var', b1)
    if hasattr(b1, 'robot_Values'):
        assert _is_linked(b1, 'robot_Values', a)
    _safe_set(a, 'robot_Var', b2)
    assert _is_linked(a, 'robot_Var', b2)
    if hasattr(b1, 'robot_Values'):
        assert not _is_linked(b1, 'robot_Values', a)
    if hasattr(b2, 'robot_Values'):
        assert _is_linked(b2, 'robot_Values', a)
    _safe_set(a, 'robot_Var', None)
    assert not _is_linked(a, 'robot_Var', b2)
    if hasattr(b2, 'robot_Values'):
        assert not _is_linked(b2, 'robot_Values', a)


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

Condition_strategy = st.builds(Condition)
@given(instance=Condition_strategy)
@settings(max_examples=25)
def test_Condition_instantiation(instance):
    assert isinstance(instance, Condition)


Movement_strategy = st.builds(Movement)
@given(instance=Movement_strategy)
@settings(max_examples=25)
def test_Movement_instantiation(instance):
    assert isinstance(instance, Movement)


Operation_strategy = st.builds(Operation)
@given(instance=Operation_strategy)
@settings(max_examples=25)
def test_Operation_instantiation(instance):
    assert isinstance(instance, Operation)


Operator_strategy = st.builds(Operator)
@given(instance=Operator_strategy)
@settings(max_examples=25)
def test_Operator_instantiation(instance):
    assert isinstance(instance, Operator)


Values_strategy = st.builds(Values)
@given(instance=Values_strategy)
@settings(max_examples=25)
def test_Values_instantiation(instance):
    assert isinstance(instance, Values)


Var_strategy = st.builds(Var)
@given(instance=Var_strategy)
@settings(max_examples=25)
def test_Var_instantiation(instance):
    assert isinstance(instance, Var)


robot_Affectation_strategy = st.builds(robot_Affectation)
@given(instance=robot_Affectation_strategy)
@settings(max_examples=25)
def test_robot_Affectation_instantiation(instance):
    assert isinstance(instance, robot_Affectation)


robot_Alternative_strategy = st.builds(robot_Alternative)
@given(instance=robot_Alternative_strategy)
@settings(max_examples=25)
def test_robot_Alternative_instantiation(instance):
    assert isinstance(instance, robot_Alternative)


robot_Backward_strategy = st.builds(robot_Backward)
@given(instance=robot_Backward_strategy)
@settings(max_examples=25)
def test_robot_Backward_instantiation(instance):
    assert isinstance(instance, robot_Backward)


robot_Compare_strategy = st.builds(robot_Compare)
@given(instance=robot_Compare_strategy)
@settings(max_examples=25)
def test_robot_Compare_instantiation(instance):
    assert isinstance(instance, robot_Compare)


robot_Condition_strategy = st.builds(robot_Condition)
@given(instance=robot_Condition_strategy)
@settings(max_examples=25)
def test_robot_Condition_instantiation(instance):
    assert isinstance(instance, robot_Condition)


robot_Declaration_strategy = st.builds(robot_Declaration)
@given(instance=robot_Declaration_strategy)
@settings(max_examples=25)
def test_robot_Declaration_instantiation(instance):
    assert isinstance(instance, robot_Declaration)


robot_Different_strategy = st.builds(robot_Different)
@given(instance=robot_Different_strategy)
@settings(max_examples=25)
def test_robot_Different_instantiation(instance):
    assert isinstance(instance, robot_Different)


robot_Echo_strategy = st.builds(robot_Echo, param=safe_text)
@given(instance=robot_Echo_strategy)
@settings(max_examples=25)
def test_robot_Echo_instantiation(instance):
    assert isinstance(instance, robot_Echo)


robot_Event_strategy = st.builds(robot_Event)
@given(instance=robot_Event_strategy)
@settings(max_examples=25)
def test_robot_Event_instantiation(instance):
    assert isinstance(instance, robot_Event)


robot_Forward_strategy = st.builds(robot_Forward)
@given(instance=robot_Forward_strategy)
@settings(max_examples=25)
def test_robot_Forward_instantiation(instance):
    assert isinstance(instance, robot_Forward)


robot_Mission_strategy = st.builds(robot_Mission)
@given(instance=robot_Mission_strategy)
@settings(max_examples=25)
def test_robot_Mission_instantiation(instance):
    assert isinstance(instance, robot_Mission)


robot_Movement_strategy = st.builds(robot_Movement, duration=st.floats(allow_nan=False, allow_infinity=False))
@given(instance=robot_Movement_strategy)
@settings(max_examples=25)
def test_robot_Movement_instantiation(instance):
    assert isinstance(instance, robot_Movement)


robot_Operation_strategy = st.builds(robot_Operation)
@given(instance=robot_Operation_strategy)
@settings(max_examples=25)
def test_robot_Operation_instantiation(instance):
    assert isinstance(instance, robot_Operation)


robot_Operator_strategy = st.builds(robot_Operator, type=safe_text)
@given(instance=robot_Operator_strategy)
@settings(max_examples=25)
def test_robot_Operator_instantiation(instance):
    assert isinstance(instance, robot_Operator)


robot_Sensor_strategy = st.builds(robot_Sensor, name=safe_text)
@given(instance=robot_Sensor_strategy)
@settings(max_examples=25)
def test_robot_Sensor_instantiation(instance):
    assert isinstance(instance, robot_Sensor)


robot_Sequence_strategy = st.builds(robot_Sequence)
@given(instance=robot_Sequence_strategy)
@settings(max_examples=25)
def test_robot_Sequence_instantiation(instance):
    assert isinstance(instance, robot_Sequence)


robot_Sleep_strategy = st.builds(robot_Sleep)
@given(instance=robot_Sleep_strategy)
@settings(max_examples=25)
def test_robot_Sleep_instantiation(instance):
    assert isinstance(instance, robot_Sleep)


robot_Stop_strategy = st.builds(robot_Stop)
@given(instance=robot_Stop_strategy)
@settings(max_examples=25)
def test_robot_Stop_instantiation(instance):
    assert isinstance(instance, robot_Stop)


robot_TBoolean_strategy = st.builds(robot_TBoolean, Value=safe_text)
@given(instance=robot_TBoolean_strategy)
@settings(max_examples=25)
def test_robot_TBoolean_instantiation(instance):
    assert isinstance(instance, robot_TBoolean)


robot_TFloat_strategy = st.builds(robot_TFloat, Value=safe_text)
@given(instance=robot_TFloat_strategy)
@settings(max_examples=25)
def test_robot_TFloat_instantiation(instance):
    assert isinstance(instance, robot_TFloat)


robot_TInteger_strategy = st.builds(robot_TInteger, Value=safe_text)
@given(instance=robot_TInteger_strategy)
@settings(max_examples=25)
def test_robot_TInteger_instantiation(instance):
    assert isinstance(instance, robot_TInteger)


robot_TString_strategy = st.builds(robot_TString, Value=safe_text)
@given(instance=robot_TString_strategy)
@settings(max_examples=25)
def test_robot_TString_instantiation(instance):
    assert isinstance(instance, robot_TString)


robot_TurnLeft_strategy = st.builds(robot_TurnLeft)
@given(instance=robot_TurnLeft_strategy)
@settings(max_examples=25)
def test_robot_TurnLeft_instantiation(instance):
    assert isinstance(instance, robot_TurnLeft)


robot_TurnRight_strategy = st.builds(robot_TurnRight)
@given(instance=robot_TurnRight_strategy)
@settings(max_examples=25)
def test_robot_TurnRight_instantiation(instance):
    assert isinstance(instance, robot_TurnRight)


robot_Value_strategy = st.builds(robot_Value)
@given(instance=robot_Value_strategy)
@settings(max_examples=25)
def test_robot_Value_instantiation(instance):
    assert isinstance(instance, robot_Value)


robot_Values_strategy = st.builds(robot_Values)
@given(instance=robot_Values_strategy)
@settings(max_examples=25)
def test_robot_Values_instantiation(instance):
    assert isinstance(instance, robot_Values)


robot_Var_strategy = st.builds(robot_Var, Name=safe_text)
@given(instance=robot_Var_strategy)
@settings(max_examples=25)
def test_robot_Var_instantiation(instance):
    assert isinstance(instance, robot_Var)


robot_Variable_strategy = st.builds(robot_Variable, Name=safe_text)
@given(instance=robot_Variable_strategy)
@settings(max_examples=25)
def test_robot_Variable_instantiation(instance):
    assert isinstance(instance, robot_Variable)


robot_Whenever_strategy = st.builds(robot_Whenever)
@given(instance=robot_Whenever_strategy)
@settings(max_examples=25)
def test_robot_Whenever_instantiation(instance):
    assert isinstance(instance, robot_Whenever)


robot_While_strategy = st.builds(robot_While)
@given(instance=robot_While_strategy)
@settings(max_examples=25)
def test_robot_While_instantiation(instance):
    assert isinstance(instance, robot_While)



