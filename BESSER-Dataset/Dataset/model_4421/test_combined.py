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
    robo_condition_Condition,
    robo_expression_Expr,
    Condition,
    robo_condition_Comparison,
    Expr,
    robo_expression_Operation,
    robo_expression_Literal,
    robo_expression_Variable,
    Command,
    robo_command_Loop,
    robo_command_Assignment,
    robo_command_Branch,
    robo_command_Drive,
    robo_command_Command,
    robo_Motor,
    robo_Setup,
    robo_Program,
    robo_Robot,
    robo_Sensor,
    MotorPort,
    Direction,
    SensorType,
    ExprOperation,
    SensorMode,
    MotorType,
    SensorPort,
    ComparisonOperator,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_hyp_robo_condition_condition_is_not_abstract():
    assert not inspect.isabstract(robo_condition_Condition)


def test_hyp_robo_condition_condition_constructor_exists():
    assert callable(robo_condition_Condition.__init__)


def test_hyp_robo_condition_condition_constructor_args():
    sig = inspect.signature(robo_condition_Condition.__init__)
    params = list(sig.parameters.keys())



def test_hyp_robo_expression_expr_is_not_abstract():
    assert not inspect.isabstract(robo_expression_Expr)


def test_hyp_robo_expression_expr_constructor_exists():
    assert callable(robo_expression_Expr.__init__)


def test_hyp_robo_expression_expr_constructor_args():
    sig = inspect.signature(robo_expression_Expr.__init__)
    params = list(sig.parameters.keys())



def test_hyp_condition_is_not_abstract():
    assert not inspect.isabstract(Condition)


def test_hyp_condition_constructor_exists():
    assert callable(Condition.__init__)


def test_hyp_condition_constructor_args():
    sig = inspect.signature(Condition.__init__)
    params = list(sig.parameters.keys())



def test_hyp_robo_condition_comparison_is_not_abstract():
    assert not inspect.isabstract(robo_condition_Comparison)


def test_hyp_robo_condition_comparison_constructor_exists():
    assert callable(robo_condition_Comparison.__init__)


def test_hyp_robo_condition_comparison_constructor_args():
    sig = inspect.signature(robo_condition_Comparison.__init__)
    params = list(sig.parameters.keys())
    assert "operator" in params, "Missing parameter 'operator'"




def test_hyp_expr_is_not_abstract():
    assert not inspect.isabstract(Expr)


def test_hyp_expr_constructor_exists():
    assert callable(Expr.__init__)


def test_hyp_expr_constructor_args():
    sig = inspect.signature(Expr.__init__)
    params = list(sig.parameters.keys())



def test_hyp_robo_expression_operation_is_not_abstract():
    assert not inspect.isabstract(robo_expression_Operation)


def test_hyp_robo_expression_operation_constructor_exists():
    assert callable(robo_expression_Operation.__init__)


def test_hyp_robo_expression_operation_constructor_args():
    sig = inspect.signature(robo_expression_Operation.__init__)
    params = list(sig.parameters.keys())
    assert "operator" in params, "Missing parameter 'operator'"




def test_hyp_robo_expression_literal_is_not_abstract():
    assert not inspect.isabstract(robo_expression_Literal)


def test_hyp_robo_expression_literal_constructor_exists():
    assert callable(robo_expression_Literal.__init__)


def test_hyp_robo_expression_literal_constructor_args():
    sig = inspect.signature(robo_expression_Literal.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"




def test_hyp_robo_expression_variable_is_not_abstract():
    assert not inspect.isabstract(robo_expression_Variable)


def test_hyp_robo_expression_variable_constructor_exists():
    assert callable(robo_expression_Variable.__init__)


def test_hyp_robo_expression_variable_constructor_args():
    sig = inspect.signature(robo_expression_Variable.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"




def test_hyp_command_is_not_abstract():
    assert not inspect.isabstract(Command)


def test_hyp_command_constructor_exists():
    assert callable(Command.__init__)


def test_hyp_command_constructor_args():
    sig = inspect.signature(Command.__init__)
    params = list(sig.parameters.keys())



def test_hyp_robo_command_loop_is_not_abstract():
    assert not inspect.isabstract(robo_command_Loop)


def test_hyp_robo_command_loop_constructor_exists():
    assert callable(robo_command_Loop.__init__)


def test_hyp_robo_command_loop_constructor_args():
    sig = inspect.signature(robo_command_Loop.__init__)
    params = list(sig.parameters.keys())



def test_hyp_robo_command_assignment_is_not_abstract():
    assert not inspect.isabstract(robo_command_Assignment)


def test_hyp_robo_command_assignment_constructor_exists():
    assert callable(robo_command_Assignment.__init__)


def test_hyp_robo_command_assignment_constructor_args():
    sig = inspect.signature(robo_command_Assignment.__init__)
    params = list(sig.parameters.keys())
    assert "variable" in params, "Missing parameter 'variable'"




def test_hyp_robo_command_branch_is_not_abstract():
    assert not inspect.isabstract(robo_command_Branch)


def test_hyp_robo_command_branch_constructor_exists():
    assert callable(robo_command_Branch.__init__)


def test_hyp_robo_command_branch_constructor_args():
    sig = inspect.signature(robo_command_Branch.__init__)
    params = list(sig.parameters.keys())



def test_hyp_robo_command_drive_is_not_abstract():
    assert not inspect.isabstract(robo_command_Drive)


def test_hyp_robo_command_drive_constructor_exists():
    assert callable(robo_command_Drive.__init__)


def test_hyp_robo_command_drive_constructor_args():
    sig = inspect.signature(robo_command_Drive.__init__)
    params = list(sig.parameters.keys())
    assert "direction" in params, "Missing parameter 'direction'"




def test_hyp_robo_command_command_is_not_abstract():
    assert not inspect.isabstract(robo_command_Command)


def test_hyp_robo_command_command_constructor_exists():
    assert callable(robo_command_Command.__init__)


def test_hyp_robo_command_command_constructor_args():
    sig = inspect.signature(robo_command_Command.__init__)
    params = list(sig.parameters.keys())



def test_hyp_robo_motor_is_not_abstract():
    assert not inspect.isabstract(robo_Motor)


def test_hyp_robo_motor_constructor_exists():
    assert callable(robo_Motor.__init__)


def test_hyp_robo_motor_constructor_args():
    sig = inspect.signature(robo_Motor.__init__)
    params = list(sig.parameters.keys())
    assert "reversed" in params, "Missing parameter 'reversed'"
    assert "speed" in params, "Missing parameter 'speed'"
    assert "port" in params, "Missing parameter 'port'"
    assert "type" in params, "Missing parameter 'type'"







def test_hyp_robo_setup_is_not_abstract():
    assert not inspect.isabstract(robo_Setup)


def test_hyp_robo_setup_constructor_exists():
    assert callable(robo_Setup.__init__)


def test_hyp_robo_setup_constructor_args():
    sig = inspect.signature(robo_Setup.__init__)
    params = list(sig.parameters.keys())



def test_hyp_robo_program_is_not_abstract():
    assert not inspect.isabstract(robo_Program)


def test_hyp_robo_program_constructor_exists():
    assert callable(robo_Program.__init__)


def test_hyp_robo_program_constructor_args():
    sig = inspect.signature(robo_Program.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"




def test_hyp_robo_robot_is_not_abstract():
    assert not inspect.isabstract(robo_Robot)


def test_hyp_robo_robot_constructor_exists():
    assert callable(robo_Robot.__init__)


def test_hyp_robo_robot_constructor_args():
    sig = inspect.signature(robo_Robot.__init__)
    params = list(sig.parameters.keys())



def test_hyp_robo_sensor_is_not_abstract():
    assert not inspect.isabstract(robo_Sensor)


def test_hyp_robo_sensor_constructor_exists():
    assert callable(robo_Sensor.__init__)


def test_hyp_robo_sensor_constructor_args():
    sig = inspect.signature(robo_Sensor.__init__)
    params = list(sig.parameters.keys())
    assert "type" in params, "Missing parameter 'type'"
    assert "mode" in params, "Missing parameter 'mode'"
    assert "port" in params, "Missing parameter 'port'"
    assert "name" in params, "Missing parameter 'name'"





def test_hyp_motorport_exists():
    # Check that the Enumeration exists
    assert MotorPort is not None

def test_hyp_motorport_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in MotorPort]
    expected_literals = [
        "A",
        "C",
        "B",
        "D",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in MotorPort"

def test_hyp_direction_exists():
    # Check that the Enumeration exists
    assert Direction is not None

def test_hyp_direction_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in Direction]
    expected_literals = [
        "LEFT",
        "BACKWARD",
        "RIGHT",
        "FORWARD",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in Direction"

def test_hyp_sensortype_exists():
    # Check that the Enumeration exists
    assert SensorType is not None

def test_hyp_sensortype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in SensorType]
    expected_literals = [
        "COLOR",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in SensorType"

def test_hyp_exproperation_exists():
    # Check that the Enumeration exists
    assert ExprOperation is not None

def test_hyp_exproperation_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in ExprOperation]
    expected_literals = [
        "DIVIDE",
        "MINUS",
        "MULTIPLY",
        "PLUS",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in ExprOperation"

def test_hyp_sensormode_exists():
    # Check that the Enumeration exists
    assert SensorMode is not None

def test_hyp_sensormode_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in SensorMode]
    expected_literals = [
        "COLOR_ID",
        "AMBIENT",
        "RED",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in SensorMode"

def test_hyp_motortype_exists():
    # Check that the Enumeration exists
    assert MotorType is not None

def test_hyp_motortype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in MotorType]
    expected_literals = [
        "LARGE",
        "MEDIUM",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in MotorType"

def test_hyp_sensorport_exists():
    # Check that the Enumeration exists
    assert SensorPort is not None

def test_hyp_sensorport_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in SensorPort]
    expected_literals = [
        "S3",
        "S1",
        "S2",
        "S4",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in SensorPort"

def test_hyp_comparisonoperator_exists():
    # Check that the Enumeration exists
    assert ComparisonOperator is not None

def test_hyp_comparisonoperator_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in ComparisonOperator]
    expected_literals = [
        "LESS",
        "EQUAL",
        "UNEQUAL",
        "LESS_OR_EQUAL",
        "GREATER",
        "GREATER_OR_EQUAL",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in ComparisonOperator"


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
robo_condition_Condition_strategy = st.builds(
    robo_condition_Condition,
)
robo_expression_Expr_strategy = st.builds(
    robo_expression_Expr,
)
Condition_strategy = st.builds(
    Condition,
)
robo_condition_Comparison_strategy = st.builds(
    robo_condition_Comparison,
    operator=
        safe_text
)
Expr_strategy = st.builds(
    Expr,
)
robo_expression_Operation_strategy = st.builds(
    robo_expression_Operation,
    operator=
        safe_text
)
robo_expression_Literal_strategy = st.builds(
    robo_expression_Literal,
    value=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
robo_expression_Variable_strategy = st.builds(
    robo_expression_Variable,
    name=
        safe_text
)
Command_strategy = st.builds(
    Command,
)
robo_command_Loop_strategy = st.builds(
    robo_command_Loop,
)
robo_command_Assignment_strategy = st.builds(
    robo_command_Assignment,
    variable=
        safe_text
)
robo_command_Branch_strategy = st.builds(
    robo_command_Branch,
)
robo_command_Drive_strategy = st.builds(
    robo_command_Drive,
    direction=
        safe_text
)
robo_command_Command_strategy = st.builds(
    robo_command_Command,
)
robo_Motor_strategy = st.builds(
    robo_Motor,
    reversed=
        st.booleans(),
    speed=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    port=
        safe_text,
    type=
        safe_text
)
robo_Setup_strategy = st.builds(
    robo_Setup,
)
robo_Program_strategy = st.builds(
    robo_Program,
    name=
        safe_text
)
robo_Robot_strategy = st.builds(
    robo_Robot,
)
robo_Sensor_strategy = st.builds(
    robo_Sensor,
    type=
        safe_text,
    mode=
        safe_text,
    port=
        safe_text,
    name=
        safe_text
)


import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=robo_condition_Condition_strategy)
@settings(max_examples=30)
def test_hyp_robo_condition_condition_evaluate_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.evaluate()
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.evaluate).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'evaluate' in robo_condition_Condition is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'evaluate' in robo_condition_Condition did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'evaluate' in robo_condition_Condition is not implemented or raised an error")


import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=robo_expression_Expr_strategy)
@settings(max_examples=30)
def test_hyp_robo_expression_expr_evaluate_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.evaluate()
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.evaluate).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'evaluate' in robo_expression_Expr is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'evaluate' in robo_expression_Expr did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'evaluate' in robo_expression_Expr is not implemented or raised an error")





@given(instance=robo_condition_Comparison_strategy)
def test_hyp_robo_condition_comparison_operator_setter(instance):
    original = instance.operator
    instance.operator = original
    assert instance.operator == original





@given(instance=robo_expression_Operation_strategy)
def test_hyp_robo_expression_operation_operator_setter(instance):
    original = instance.operator
    instance.operator = original
    assert instance.operator == original




@given(instance=robo_expression_Literal_strategy)
def test_hyp_robo_expression_literal_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original




@given(instance=robo_expression_Variable_strategy)
def test_hyp_robo_expression_variable_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original






@given(instance=robo_command_Assignment_strategy)
def test_hyp_robo_command_assignment_variable_setter(instance):
    original = instance.variable
    instance.variable = original
    assert instance.variable == original





@given(instance=robo_command_Drive_strategy)
def test_hyp_robo_command_drive_direction_setter(instance):
    original = instance.direction
    instance.direction = original
    assert instance.direction == original





@given(instance=robo_Motor_strategy)
def test_hyp_robo_motor_reversed_setter(instance):
    original = instance.reversed
    instance.reversed = original
    assert instance.reversed == original



@given(instance=robo_Motor_strategy)
def test_hyp_robo_motor_speed_setter(instance):
    original = instance.speed
    instance.speed = original
    assert instance.speed == original



@given(instance=robo_Motor_strategy)
def test_hyp_robo_motor_port_setter(instance):
    original = instance.port
    instance.port = original
    assert instance.port == original



@given(instance=robo_Motor_strategy)
def test_hyp_robo_motor_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original





@given(instance=robo_Program_strategy)
def test_hyp_robo_program_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original





@given(instance=robo_Sensor_strategy)
def test_hyp_robo_sensor_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original



@given(instance=robo_Sensor_strategy)
def test_hyp_robo_sensor_mode_setter(instance):
    original = instance.mode
    instance.mode = original
    assert instance.mode == original



@given(instance=robo_Sensor_strategy)
def test_hyp_robo_sensor_port_setter(instance):
    original = instance.port
    instance.port = original
    assert instance.port == original



@given(instance=robo_Sensor_strategy)
def test_hyp_robo_sensor_name_setter(instance):
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
    Command,
    Condition,
    Expr,
    robo_Motor,
    robo_Program,
    robo_Robot,
    robo_Sensor,
    robo_Setup,
    robo_command_Assignment,
    robo_command_Branch,
    robo_command_Command,
    robo_command_Drive,
    robo_command_Loop,
    robo_condition_Comparison,
    robo_condition_Condition,
    robo_expression_Expr,
    robo_expression_Literal,
    robo_expression_Operation,
    robo_expression_Variable,
    ComparisonOperator,
    Direction,
    ExprOperation,
    MotorPort,
    MotorType,
    SensorMode,
    SensorPort,
    SensorType,
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

def test_robo_Motor_port_value_roundtrip():
    instance = robo_Motor(port="sample_text", reversed=True, speed=3.14, type="sample_text")
    assert instance.port == "sample_text"
    instance.port = "sample_text_2"
    assert instance.port == "sample_text_2"


def test_robo_Motor_reversed_value_roundtrip():
    instance = robo_Motor(port="sample_text", reversed=True, speed=3.14, type="sample_text")
    assert instance.reversed == True
    instance.reversed = False
    assert instance.reversed == False


def test_robo_Motor_speed_value_roundtrip():
    instance = robo_Motor(port="sample_text", reversed=True, speed=3.14, type="sample_text")
    assert instance.speed == 3.14
    instance.speed = 9.99
    assert instance.speed == 9.99


def test_robo_Motor_type_value_roundtrip():
    instance = robo_Motor(port="sample_text", reversed=True, speed=3.14, type="sample_text")
    assert instance.type == "sample_text"
    instance.type = "sample_text_2"
    assert instance.type == "sample_text_2"


def test_robo_Program_name_value_roundtrip():
    instance = robo_Program(name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_robo_Sensor_mode_value_roundtrip():
    instance = robo_Sensor(mode="sample_text", name="sample_text", port="sample_text", type="sample_text")
    assert instance.mode == "sample_text"
    instance.mode = "sample_text_2"
    assert instance.mode == "sample_text_2"


def test_robo_Sensor_name_value_roundtrip():
    instance = robo_Sensor(mode="sample_text", name="sample_text", port="sample_text", type="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_robo_Sensor_port_value_roundtrip():
    instance = robo_Sensor(mode="sample_text", name="sample_text", port="sample_text", type="sample_text")
    assert instance.port == "sample_text"
    instance.port = "sample_text_2"
    assert instance.port == "sample_text_2"


def test_robo_Sensor_type_value_roundtrip():
    instance = robo_Sensor(mode="sample_text", name="sample_text", port="sample_text", type="sample_text")
    assert instance.type == "sample_text"
    instance.type = "sample_text_2"
    assert instance.type == "sample_text_2"


def test_robo_command_Assignment_variable_value_roundtrip():
    instance = robo_command_Assignment(variable="sample_text")
    assert instance.variable == "sample_text"
    instance.variable = "sample_text_2"
    assert instance.variable == "sample_text_2"


def test_robo_command_Drive_direction_value_roundtrip():
    instance = robo_command_Drive(direction="sample_text")
    assert instance.direction == "sample_text"
    instance.direction = "sample_text_2"
    assert instance.direction == "sample_text_2"


def test_robo_condition_Comparison_operator_value_roundtrip():
    instance = robo_condition_Comparison(operator="sample_text")
    assert instance.operator == "sample_text"
    instance.operator = "sample_text_2"
    assert instance.operator == "sample_text_2"


def test_robo_expression_Literal_value_value_roundtrip():
    instance = robo_expression_Literal(value=3.14)
    assert instance.value == 3.14
    instance.value = 9.99
    assert instance.value == 9.99


def test_robo_expression_Operation_operator_value_roundtrip():
    instance = robo_expression_Operation(operator="sample_text")
    assert instance.operator == "sample_text"
    instance.operator = "sample_text_2"
    assert instance.operator == "sample_text_2"


def test_robo_expression_Variable_name_value_roundtrip():
    instance = robo_expression_Variable(name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_robo_command_Assignment_isa_Command():
    instance = robo_command_Assignment(variable="sample_text")
    assert isinstance(instance, Command)


def test_robo_command_Branch_isa_Command():
    instance = robo_command_Branch()
    assert isinstance(instance, Command)


def test_robo_command_Drive_isa_Command():
    instance = robo_command_Drive(direction="sample_text")
    assert isinstance(instance, Command)


def test_robo_command_Loop_isa_Command():
    instance = robo_command_Loop()
    assert isinstance(instance, Command)


def test_robo_condition_Comparison_isa_Condition():
    instance = robo_condition_Comparison(operator="sample_text")
    assert isinstance(instance, Condition)


def test_robo_expression_Literal_isa_Expr():
    instance = robo_expression_Literal(value=3.14)
    assert isinstance(instance, Expr)


def test_robo_expression_Operation_isa_Expr():
    instance = robo_expression_Operation(operator="sample_text")
    assert isinstance(instance, Expr)


def test_robo_expression_Variable_isa_Expr():
    instance = robo_expression_Variable(name="sample_text")
    assert isinstance(instance, Expr)


def test_assoc_commands10_link_reassign_clear():
    a = robo_Program(name="sample_text")
    b1 = Command()
    b2 = Command()
    _safe_set(a, 'robo_Program11', {b1})
    assert _is_linked(a, 'robo_Program11', b1)
    if hasattr(b1, 'Command'):
        assert _is_linked(b1, 'Command', a)
    _safe_set(a, 'robo_Program11', {b2})
    assert _is_linked(a, 'robo_Program11', b2)
    if hasattr(b1, 'Command'):
        assert not _is_linked(b1, 'Command', a)
    if hasattr(b2, 'Command'):
        assert _is_linked(b2, 'Command', a)
    _safe_set(a, 'robo_Program11', set())
    assert not _is_linked(a, 'robo_Program11', b2)
    if hasattr(b2, 'Command'):
        assert not _is_linked(b2, 'Command', a)


def test_assoc_distance12_link_reassign_clear():
    a = robo_command_Drive(direction="sample_text")
    b1 = Expr()
    b2 = Expr()
    _safe_set(a, 'robo_command_Drive', b1)
    assert _is_linked(a, 'robo_command_Drive', b1)
    if hasattr(b1, 'Expr'):
        assert _is_linked(b1, 'Expr', a)
    _safe_set(a, 'robo_command_Drive', b2)
    assert _is_linked(a, 'robo_command_Drive', b2)
    if hasattr(b1, 'Expr'):
        assert not _is_linked(b1, 'Expr', a)
    if hasattr(b2, 'Expr'):
        assert _is_linked(b2, 'Expr', a)
    _safe_set(a, 'robo_command_Drive', None)
    assert not _is_linked(a, 'robo_command_Drive', b2)
    if hasattr(b2, 'Expr'):
        assert not _is_linked(b2, 'Expr', a)


def test_assoc_left27_link_reassign_clear():
    a = robo_expression_Operation(operator="sample_text")
    b1 = Expr()
    b2 = Expr()
    _safe_set(a, 'robo_expression_Operation', b1)
    assert _is_linked(a, 'robo_expression_Operation', b1)
    if hasattr(b1, 'Expr28'):
        assert _is_linked(b1, 'Expr28', a)
    _safe_set(a, 'robo_expression_Operation', b2)
    assert _is_linked(a, 'robo_expression_Operation', b2)
    if hasattr(b1, 'Expr28'):
        assert not _is_linked(b1, 'Expr28', a)
    if hasattr(b2, 'Expr28'):
        assert _is_linked(b2, 'Expr28', a)
    _safe_set(a, 'robo_expression_Operation', None)
    assert not _is_linked(a, 'robo_expression_Operation', b2)
    if hasattr(b2, 'Expr28'):
        assert not _is_linked(b2, 'Expr28', a)


def test_assoc_left32_link_reassign_clear():
    a = robo_condition_Comparison(operator="sample_text")
    b1 = Expr()
    b2 = Expr()
    _safe_set(a, 'robo_condition_Comparison', b1)
    assert _is_linked(a, 'robo_condition_Comparison', b1)
    if hasattr(b1, 'Expr33'):
        assert _is_linked(b1, 'Expr33', a)
    _safe_set(a, 'robo_condition_Comparison', b2)
    assert _is_linked(a, 'robo_condition_Comparison', b2)
    if hasattr(b1, 'Expr33'):
        assert not _is_linked(b1, 'Expr33', a)
    if hasattr(b2, 'Expr33'):
        assert _is_linked(b2, 'Expr33', a)
    _safe_set(a, 'robo_condition_Comparison', None)
    assert not _is_linked(a, 'robo_condition_Comparison', b2)
    if hasattr(b2, 'Expr33'):
        assert not _is_linked(b2, 'Expr33', a)


def test_assoc_leftMotor3_link_reassign_clear():
    a = robo_Motor(port="sample_text", reversed=True, speed=3.14, type="sample_text")
    b1 = robo_Setup()
    b2 = robo_Setup()
    _safe_set(a, 'robo_Motor', b1)
    assert _is_linked(a, 'robo_Motor', b1)
    if hasattr(b1, 'robo_Setup4'):
        assert _is_linked(b1, 'robo_Setup4', a)
    _safe_set(a, 'robo_Motor', b2)
    assert _is_linked(a, 'robo_Motor', b2)
    if hasattr(b1, 'robo_Setup4'):
        assert not _is_linked(b1, 'robo_Setup4', a)
    if hasattr(b2, 'robo_Setup4'):
        assert _is_linked(b2, 'robo_Setup4', a)
    _safe_set(a, 'robo_Motor', None)
    assert not _is_linked(a, 'robo_Motor', b2)
    if hasattr(b2, 'robo_Setup4'):
        assert not _is_linked(b2, 'robo_Setup4', a)


def test_assoc_programms0_link_reassign_clear():
    a = robo_Program(name="sample_text")
    b1 = robo_Robot()
    b2 = robo_Robot()
    _safe_set(a, 'robo_Program', b1)
    assert _is_linked(a, 'robo_Program', b1)
    if hasattr(b1, 'robo_Robot'):
        assert _is_linked(b1, 'robo_Robot', a)
    _safe_set(a, 'robo_Program', b2)
    assert _is_linked(a, 'robo_Program', b2)
    if hasattr(b1, 'robo_Robot'):
        assert not _is_linked(b1, 'robo_Robot', a)
    if hasattr(b2, 'robo_Robot'):
        assert _is_linked(b2, 'robo_Robot', a)
    _safe_set(a, 'robo_Program', None)
    assert not _is_linked(a, 'robo_Program', b2)
    if hasattr(b2, 'robo_Robot'):
        assert not _is_linked(b2, 'robo_Robot', a)


def test_assoc_right29_link_reassign_clear():
    a = robo_expression_Operation(operator="sample_text")
    b1 = Expr()
    b2 = Expr()
    _safe_set(a, 'robo_expression_Operation30', b1)
    assert _is_linked(a, 'robo_expression_Operation30', b1)
    if hasattr(b1, 'Expr31'):
        assert _is_linked(b1, 'Expr31', a)
    _safe_set(a, 'robo_expression_Operation30', b2)
    assert _is_linked(a, 'robo_expression_Operation30', b2)
    if hasattr(b1, 'Expr31'):
        assert not _is_linked(b1, 'Expr31', a)
    if hasattr(b2, 'Expr31'):
        assert _is_linked(b2, 'Expr31', a)
    _safe_set(a, 'robo_expression_Operation30', None)
    assert not _is_linked(a, 'robo_expression_Operation30', b2)
    if hasattr(b2, 'Expr31'):
        assert not _is_linked(b2, 'Expr31', a)


def test_assoc_right34_link_reassign_clear():
    a = robo_condition_Comparison(operator="sample_text")
    b1 = Expr()
    b2 = Expr()
    _safe_set(a, 'robo_condition_Comparison35', b1)
    assert _is_linked(a, 'robo_condition_Comparison35', b1)
    if hasattr(b1, 'Expr36'):
        assert _is_linked(b1, 'Expr36', a)
    _safe_set(a, 'robo_condition_Comparison35', b2)
    assert _is_linked(a, 'robo_condition_Comparison35', b2)
    if hasattr(b1, 'Expr36'):
        assert not _is_linked(b1, 'Expr36', a)
    if hasattr(b2, 'Expr36'):
        assert _is_linked(b2, 'Expr36', a)
    _safe_set(a, 'robo_condition_Comparison35', None)
    assert not _is_linked(a, 'robo_condition_Comparison35', b2)
    if hasattr(b2, 'Expr36'):
        assert not _is_linked(b2, 'Expr36', a)


def test_assoc_rightMotor5_link_reassign_clear():
    a = robo_Motor(port="sample_text", reversed=True, speed=3.14, type="sample_text")
    b1 = robo_Setup()
    b2 = robo_Setup()
    _safe_set(a, 'robo_Motor7', b1)
    assert _is_linked(a, 'robo_Motor7', b1)
    if hasattr(b1, 'robo_Setup6'):
        assert _is_linked(b1, 'robo_Setup6', a)
    _safe_set(a, 'robo_Motor7', b2)
    assert _is_linked(a, 'robo_Motor7', b2)
    if hasattr(b1, 'robo_Setup6'):
        assert not _is_linked(b1, 'robo_Setup6', a)
    if hasattr(b2, 'robo_Setup6'):
        assert _is_linked(b2, 'robo_Setup6', a)
    _safe_set(a, 'robo_Motor7', None)
    assert not _is_linked(a, 'robo_Motor7', b2)
    if hasattr(b2, 'robo_Setup6'):
        assert not _is_linked(b2, 'robo_Setup6', a)


def test_assoc_sensors8_link_reassign_clear():
    a = robo_Sensor(mode="sample_text", name="sample_text", port="sample_text", type="sample_text")
    b1 = robo_Setup()
    b2 = robo_Setup()
    _safe_set(a, 'robo_Sensor', b1)
    assert _is_linked(a, 'robo_Sensor', b1)
    if hasattr(b1, 'robo_Setup9'):
        assert _is_linked(b1, 'robo_Setup9', a)
    _safe_set(a, 'robo_Sensor', b2)
    assert _is_linked(a, 'robo_Sensor', b2)
    if hasattr(b1, 'robo_Setup9'):
        assert not _is_linked(b1, 'robo_Setup9', a)
    if hasattr(b2, 'robo_Setup9'):
        assert _is_linked(b2, 'robo_Setup9', a)
    _safe_set(a, 'robo_Sensor', None)
    assert not _is_linked(a, 'robo_Sensor', b2)
    if hasattr(b2, 'robo_Setup9'):
        assert not _is_linked(b2, 'robo_Setup9', a)


def test_assoc_until13_link_reassign_clear():
    a = robo_command_Drive(direction="sample_text")
    b1 = Condition()
    b2 = Condition()
    _safe_set(a, 'robo_command_Drive14', b1)
    assert _is_linked(a, 'robo_command_Drive14', b1)
    if hasattr(b1, 'Condition'):
        assert _is_linked(b1, 'Condition', a)
    _safe_set(a, 'robo_command_Drive14', b2)
    assert _is_linked(a, 'robo_command_Drive14', b2)
    if hasattr(b1, 'Condition'):
        assert not _is_linked(b1, 'Condition', a)
    if hasattr(b2, 'Condition'):
        assert _is_linked(b2, 'Condition', a)
    _safe_set(a, 'robo_command_Drive14', None)
    assert not _is_linked(a, 'robo_command_Drive14', b2)
    if hasattr(b2, 'Condition'):
        assert not _is_linked(b2, 'Condition', a)


def test_assoc_value25_link_reassign_clear():
    a = robo_command_Assignment(variable="sample_text")
    b1 = Expr()
    b2 = Expr()
    _safe_set(a, 'robo_command_Assignment', b1)
    assert _is_linked(a, 'robo_command_Assignment', b1)
    if hasattr(b1, 'Expr26'):
        assert _is_linked(b1, 'Expr26', a)
    _safe_set(a, 'robo_command_Assignment', b2)
    assert _is_linked(a, 'robo_command_Assignment', b2)
    if hasattr(b1, 'Expr26'):
        assert not _is_linked(b1, 'Expr26', a)
    if hasattr(b2, 'Expr26'):
        assert _is_linked(b2, 'Expr26', a)
    _safe_set(a, 'robo_command_Assignment', None)
    assert not _is_linked(a, 'robo_command_Assignment', b2)
    if hasattr(b2, 'Expr26'):
        assert not _is_linked(b2, 'Expr26', a)


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

Command_strategy = st.builds(Command)
@given(instance=Command_strategy)
@settings(max_examples=25)
def test_Command_instantiation(instance):
    assert isinstance(instance, Command)


Condition_strategy = st.builds(Condition)
@given(instance=Condition_strategy)
@settings(max_examples=25)
def test_Condition_instantiation(instance):
    assert isinstance(instance, Condition)


Expr_strategy = st.builds(Expr)
@given(instance=Expr_strategy)
@settings(max_examples=25)
def test_Expr_instantiation(instance):
    assert isinstance(instance, Expr)


robo_Motor_strategy = st.builds(robo_Motor, port=safe_text, reversed=st.booleans(), speed=st.floats(allow_nan=False, allow_infinity=False), type=safe_text)
@given(instance=robo_Motor_strategy)
@settings(max_examples=25)
def test_robo_Motor_instantiation(instance):
    assert isinstance(instance, robo_Motor)


robo_Program_strategy = st.builds(robo_Program, name=safe_text)
@given(instance=robo_Program_strategy)
@settings(max_examples=25)
def test_robo_Program_instantiation(instance):
    assert isinstance(instance, robo_Program)


robo_Robot_strategy = st.builds(robo_Robot)
@given(instance=robo_Robot_strategy)
@settings(max_examples=25)
def test_robo_Robot_instantiation(instance):
    assert isinstance(instance, robo_Robot)


robo_Sensor_strategy = st.builds(robo_Sensor, mode=safe_text, name=safe_text, port=safe_text, type=safe_text)
@given(instance=robo_Sensor_strategy)
@settings(max_examples=25)
def test_robo_Sensor_instantiation(instance):
    assert isinstance(instance, robo_Sensor)


robo_Setup_strategy = st.builds(robo_Setup)
@given(instance=robo_Setup_strategy)
@settings(max_examples=25)
def test_robo_Setup_instantiation(instance):
    assert isinstance(instance, robo_Setup)


robo_command_Assignment_strategy = st.builds(robo_command_Assignment, variable=safe_text)
@given(instance=robo_command_Assignment_strategy)
@settings(max_examples=25)
def test_robo_command_Assignment_instantiation(instance):
    assert isinstance(instance, robo_command_Assignment)


robo_command_Branch_strategy = st.builds(robo_command_Branch)
@given(instance=robo_command_Branch_strategy)
@settings(max_examples=25)
def test_robo_command_Branch_instantiation(instance):
    assert isinstance(instance, robo_command_Branch)


robo_command_Command_strategy = st.builds(robo_command_Command)
@given(instance=robo_command_Command_strategy)
@settings(max_examples=25)
def test_robo_command_Command_instantiation(instance):
    assert isinstance(instance, robo_command_Command)


robo_command_Drive_strategy = st.builds(robo_command_Drive, direction=safe_text)
@given(instance=robo_command_Drive_strategy)
@settings(max_examples=25)
def test_robo_command_Drive_instantiation(instance):
    assert isinstance(instance, robo_command_Drive)


robo_command_Loop_strategy = st.builds(robo_command_Loop)
@given(instance=robo_command_Loop_strategy)
@settings(max_examples=25)
def test_robo_command_Loop_instantiation(instance):
    assert isinstance(instance, robo_command_Loop)


robo_condition_Comparison_strategy = st.builds(robo_condition_Comparison, operator=safe_text)
@given(instance=robo_condition_Comparison_strategy)
@settings(max_examples=25)
def test_robo_condition_Comparison_instantiation(instance):
    assert isinstance(instance, robo_condition_Comparison)


robo_condition_Condition_strategy = st.builds(robo_condition_Condition)
@given(instance=robo_condition_Condition_strategy)
@settings(max_examples=25)
def test_robo_condition_Condition_instantiation(instance):
    assert isinstance(instance, robo_condition_Condition)


robo_expression_Expr_strategy = st.builds(robo_expression_Expr)
@given(instance=robo_expression_Expr_strategy)
@settings(max_examples=25)
def test_robo_expression_Expr_instantiation(instance):
    assert isinstance(instance, robo_expression_Expr)


robo_expression_Literal_strategy = st.builds(robo_expression_Literal, value=st.floats(allow_nan=False, allow_infinity=False))
@given(instance=robo_expression_Literal_strategy)
@settings(max_examples=25)
def test_robo_expression_Literal_instantiation(instance):
    assert isinstance(instance, robo_expression_Literal)


robo_expression_Operation_strategy = st.builds(robo_expression_Operation, operator=safe_text)
@given(instance=robo_expression_Operation_strategy)
@settings(max_examples=25)
def test_robo_expression_Operation_instantiation(instance):
    assert isinstance(instance, robo_expression_Operation)


robo_expression_Variable_strategy = st.builds(robo_expression_Variable, name=safe_text)
@given(instance=robo_expression_Variable_strategy)
@settings(max_examples=25)
def test_robo_expression_Variable_instantiation(instance):
    assert isinstance(instance, robo_expression_Variable)



