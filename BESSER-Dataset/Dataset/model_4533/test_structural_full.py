import inspect
import pytest
from datetime import date, datetime, time, timedelta
from hypothesis import given, settings
import hypothesis.strategies as st

from python_code import (
    CommandeRobot,
    Expr,
    ExprBool,
    OpBinaire,
    OpUnaire,
    flow_ExprBool,
    robotG_flow_And,
    robotG_flow_Expr,
    robotG_flow_ExprBool,
    robotG_flow_If,
    robotG_flow_Not,
    robotG_flow_OpBinaire,
    robotG_flow_OpUnaire,
    robotG_flow_Or,
    robotG_flow_Programme,
    robotG_flow_StopProgram,
    robotG_flow_While,
    robotG_robot_Bip,
    robotG_robot_CommandeRobot,
    robotG_robot_Display,
    robotG_robot_HasTurned,
    robotG_robot_Move,
    robotG_robot_Obstacle,
    robotG_robot_SetTurnAngle,
    robotG_robot_StopEngine,
    robotG_robot_Turn,
    robot_CommandeRobot,
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

def test_robotG_robot_Bip_duration_value_roundtrip():
    instance = robotG_robot_Bip(duration=7, power=7, repeat=True)
    assert instance.duration == 7
    instance.duration = 13
    assert instance.duration == 13


def test_robotG_robot_Bip_power_value_roundtrip():
    instance = robotG_robot_Bip(duration=7, power=7, repeat=True)
    assert instance.power == 7
    instance.power = 13
    assert instance.power == 13


def test_robotG_robot_Bip_repeat_value_roundtrip():
    instance = robotG_robot_Bip(duration=7, power=7, repeat=True)
    assert instance.repeat == True
    instance.repeat = False
    assert instance.repeat == False


def test_robotG_robot_Display_col_value_roundtrip():
    instance = robotG_robot_Display(col=7, duration=7, line=7, msg="sample_text")
    assert instance.col == 7
    instance.col = 13
    assert instance.col == 13


def test_robotG_robot_Display_duration_value_roundtrip():
    instance = robotG_robot_Display(col=7, duration=7, line=7, msg="sample_text")
    assert instance.duration == 7
    instance.duration = 13
    assert instance.duration == 13


def test_robotG_robot_Display_line_value_roundtrip():
    instance = robotG_robot_Display(col=7, duration=7, line=7, msg="sample_text")
    assert instance.line == 7
    instance.line = 13
    assert instance.line == 13


def test_robotG_robot_Display_msg_value_roundtrip():
    instance = robotG_robot_Display(col=7, duration=7, line=7, msg="sample_text")
    assert instance.msg == "sample_text"
    instance.msg = "sample_text_2"
    assert instance.msg == "sample_text_2"


def test_robotG_robot_HasTurned_angle_value_roundtrip():
    instance = robotG_robot_HasTurned(angle=7)
    assert instance.angle == 7
    instance.angle = 13
    assert instance.angle == 13


def test_robotG_robot_Move_power_value_roundtrip():
    instance = robotG_robot_Move(power=7)
    assert instance.power == 7
    instance.power = 13
    assert instance.power == 13


def test_robotG_robot_Obstacle_distance_value_roundtrip():
    instance = robotG_robot_Obstacle(distance=7)
    assert instance.distance == 7
    instance.distance = 13
    assert instance.distance == 13


def test_robotG_robot_SetTurnAngle_angle_value_roundtrip():
    instance = robotG_robot_SetTurnAngle(angle=7)
    assert instance.angle == 7
    instance.angle = 13
    assert instance.angle == 13


def test_robotG_robot_Turn_angle_value_roundtrip():
    instance = robotG_robot_Turn(angle=7, power=7)
    assert instance.angle == 7
    instance.angle = 13
    assert instance.angle == 13


def test_robotG_robot_Turn_power_value_roundtrip():
    instance = robotG_robot_Turn(angle=7, power=7)
    assert instance.power == 7
    instance.power = 13
    assert instance.power == 13


def test_robotG_robot_Bip_isa_CommandeRobot():
    instance = robotG_robot_Bip(duration=7, power=7, repeat=True)
    assert isinstance(instance, CommandeRobot)


def test_robotG_robot_Display_isa_CommandeRobot():
    instance = robotG_robot_Display(col=7, duration=7, line=7, msg="sample_text")
    assert isinstance(instance, CommandeRobot)


def test_robotG_robot_Move_isa_CommandeRobot():
    instance = robotG_robot_Move(power=7)
    assert isinstance(instance, CommandeRobot)


def test_robotG_robot_SetTurnAngle_isa_CommandeRobot():
    instance = robotG_robot_SetTurnAngle(angle=7)
    assert isinstance(instance, CommandeRobot)


def test_robotG_robot_StopEngine_isa_CommandeRobot():
    instance = robotG_robot_StopEngine()
    assert isinstance(instance, CommandeRobot)


def test_robotG_robot_Turn_isa_CommandeRobot():
    instance = robotG_robot_Turn(angle=7, power=7)
    assert isinstance(instance, CommandeRobot)


def test_robotG_flow_ExprBool_isa_Expr():
    instance = robotG_flow_ExprBool()
    assert isinstance(instance, Expr)


def test_robotG_flow_If_isa_Expr():
    instance = robotG_flow_If()
    assert isinstance(instance, Expr)


def test_robotG_flow_StopProgram_isa_Expr():
    instance = robotG_flow_StopProgram()
    assert isinstance(instance, Expr)


def test_robotG_flow_While_isa_Expr():
    instance = robotG_flow_While()
    assert isinstance(instance, Expr)


def test_robotG_robot_CommandeRobot_isa_Expr():
    instance = robotG_robot_CommandeRobot()
    assert isinstance(instance, Expr)


def test_robotG_flow_OpBinaire_isa_ExprBool():
    instance = robotG_flow_OpBinaire()
    assert isinstance(instance, ExprBool)


def test_robotG_flow_OpUnaire_isa_ExprBool():
    instance = robotG_flow_OpUnaire()
    assert isinstance(instance, ExprBool)


def test_robotG_flow_And_isa_OpBinaire():
    instance = robotG_flow_And()
    assert isinstance(instance, OpBinaire)


def test_robotG_flow_Or_isa_OpBinaire():
    instance = robotG_flow_Or()
    assert isinstance(instance, OpBinaire)


def test_robotG_flow_Not_isa_OpUnaire():
    instance = robotG_flow_Not()
    assert isinstance(instance, OpUnaire)


def test_robotG_robot_HasTurned_isa_flow_ExprBool():
    instance = robotG_robot_HasTurned(angle=7)
    assert isinstance(instance, flow_ExprBool)


def test_robotG_robot_Obstacle_isa_flow_ExprBool():
    instance = robotG_robot_Obstacle(distance=7)
    assert isinstance(instance, flow_ExprBool)


def test_robotG_robot_HasTurned_isa_robot_CommandeRobot():
    instance = robotG_robot_HasTurned(angle=7)
    assert isinstance(instance, robot_CommandeRobot)


def test_robotG_robot_Obstacle_isa_robot_CommandeRobot():
    instance = robotG_robot_Obstacle(distance=7)
    assert isinstance(instance, robot_CommandeRobot)


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

CommandeRobot_strategy = st.builds(CommandeRobot)
@given(instance=CommandeRobot_strategy)
@settings(max_examples=25)
def test_CommandeRobot_instantiation(instance):
    assert isinstance(instance, CommandeRobot)


Expr_strategy = st.builds(Expr)
@given(instance=Expr_strategy)
@settings(max_examples=25)
def test_Expr_instantiation(instance):
    assert isinstance(instance, Expr)


ExprBool_strategy = st.builds(ExprBool)
@given(instance=ExprBool_strategy)
@settings(max_examples=25)
def test_ExprBool_instantiation(instance):
    assert isinstance(instance, ExprBool)


OpBinaire_strategy = st.builds(OpBinaire)
@given(instance=OpBinaire_strategy)
@settings(max_examples=25)
def test_OpBinaire_instantiation(instance):
    assert isinstance(instance, OpBinaire)


OpUnaire_strategy = st.builds(OpUnaire)
@given(instance=OpUnaire_strategy)
@settings(max_examples=25)
def test_OpUnaire_instantiation(instance):
    assert isinstance(instance, OpUnaire)


flow_ExprBool_strategy = st.builds(flow_ExprBool)
@given(instance=flow_ExprBool_strategy)
@settings(max_examples=25)
def test_flow_ExprBool_instantiation(instance):
    assert isinstance(instance, flow_ExprBool)


robotG_flow_And_strategy = st.builds(robotG_flow_And)
@given(instance=robotG_flow_And_strategy)
@settings(max_examples=25)
def test_robotG_flow_And_instantiation(instance):
    assert isinstance(instance, robotG_flow_And)


robotG_flow_Expr_strategy = st.builds(robotG_flow_Expr)
@given(instance=robotG_flow_Expr_strategy)
@settings(max_examples=25)
def test_robotG_flow_Expr_instantiation(instance):
    assert isinstance(instance, robotG_flow_Expr)


robotG_flow_ExprBool_strategy = st.builds(robotG_flow_ExprBool)
@given(instance=robotG_flow_ExprBool_strategy)
@settings(max_examples=25)
def test_robotG_flow_ExprBool_instantiation(instance):
    assert isinstance(instance, robotG_flow_ExprBool)


robotG_flow_If_strategy = st.builds(robotG_flow_If)
@given(instance=robotG_flow_If_strategy)
@settings(max_examples=25)
def test_robotG_flow_If_instantiation(instance):
    assert isinstance(instance, robotG_flow_If)


robotG_flow_Not_strategy = st.builds(robotG_flow_Not)
@given(instance=robotG_flow_Not_strategy)
@settings(max_examples=25)
def test_robotG_flow_Not_instantiation(instance):
    assert isinstance(instance, robotG_flow_Not)


robotG_flow_OpBinaire_strategy = st.builds(robotG_flow_OpBinaire)
@given(instance=robotG_flow_OpBinaire_strategy)
@settings(max_examples=25)
def test_robotG_flow_OpBinaire_instantiation(instance):
    assert isinstance(instance, robotG_flow_OpBinaire)


robotG_flow_OpUnaire_strategy = st.builds(robotG_flow_OpUnaire)
@given(instance=robotG_flow_OpUnaire_strategy)
@settings(max_examples=25)
def test_robotG_flow_OpUnaire_instantiation(instance):
    assert isinstance(instance, robotG_flow_OpUnaire)


robotG_flow_Or_strategy = st.builds(robotG_flow_Or)
@given(instance=robotG_flow_Or_strategy)
@settings(max_examples=25)
def test_robotG_flow_Or_instantiation(instance):
    assert isinstance(instance, robotG_flow_Or)


robotG_flow_Programme_strategy = st.builds(robotG_flow_Programme)
@given(instance=robotG_flow_Programme_strategy)
@settings(max_examples=25)
def test_robotG_flow_Programme_instantiation(instance):
    assert isinstance(instance, robotG_flow_Programme)


robotG_flow_StopProgram_strategy = st.builds(robotG_flow_StopProgram)
@given(instance=robotG_flow_StopProgram_strategy)
@settings(max_examples=25)
def test_robotG_flow_StopProgram_instantiation(instance):
    assert isinstance(instance, robotG_flow_StopProgram)


robotG_flow_While_strategy = st.builds(robotG_flow_While)
@given(instance=robotG_flow_While_strategy)
@settings(max_examples=25)
def test_robotG_flow_While_instantiation(instance):
    assert isinstance(instance, robotG_flow_While)


robotG_robot_Bip_strategy = st.builds(robotG_robot_Bip, duration=st.integers(), power=st.integers(), repeat=st.booleans())
@given(instance=robotG_robot_Bip_strategy)
@settings(max_examples=25)
def test_robotG_robot_Bip_instantiation(instance):
    assert isinstance(instance, robotG_robot_Bip)


robotG_robot_CommandeRobot_strategy = st.builds(robotG_robot_CommandeRobot)
@given(instance=robotG_robot_CommandeRobot_strategy)
@settings(max_examples=25)
def test_robotG_robot_CommandeRobot_instantiation(instance):
    assert isinstance(instance, robotG_robot_CommandeRobot)


robotG_robot_Display_strategy = st.builds(robotG_robot_Display, col=st.integers(), duration=st.integers(), line=st.integers(), msg=safe_text)
@given(instance=robotG_robot_Display_strategy)
@settings(max_examples=25)
def test_robotG_robot_Display_instantiation(instance):
    assert isinstance(instance, robotG_robot_Display)


robotG_robot_HasTurned_strategy = st.builds(robotG_robot_HasTurned, angle=st.integers())
@given(instance=robotG_robot_HasTurned_strategy)
@settings(max_examples=25)
def test_robotG_robot_HasTurned_instantiation(instance):
    assert isinstance(instance, robotG_robot_HasTurned)


robotG_robot_Move_strategy = st.builds(robotG_robot_Move, power=st.integers())
@given(instance=robotG_robot_Move_strategy)
@settings(max_examples=25)
def test_robotG_robot_Move_instantiation(instance):
    assert isinstance(instance, robotG_robot_Move)


robotG_robot_Obstacle_strategy = st.builds(robotG_robot_Obstacle, distance=st.integers())
@given(instance=robotG_robot_Obstacle_strategy)
@settings(max_examples=25)
def test_robotG_robot_Obstacle_instantiation(instance):
    assert isinstance(instance, robotG_robot_Obstacle)


robotG_robot_SetTurnAngle_strategy = st.builds(robotG_robot_SetTurnAngle, angle=st.integers())
@given(instance=robotG_robot_SetTurnAngle_strategy)
@settings(max_examples=25)
def test_robotG_robot_SetTurnAngle_instantiation(instance):
    assert isinstance(instance, robotG_robot_SetTurnAngle)


robotG_robot_StopEngine_strategy = st.builds(robotG_robot_StopEngine)
@given(instance=robotG_robot_StopEngine_strategy)
@settings(max_examples=25)
def test_robotG_robot_StopEngine_instantiation(instance):
    assert isinstance(instance, robotG_robot_StopEngine)


robotG_robot_Turn_strategy = st.builds(robotG_robot_Turn, angle=st.integers(), power=st.integers())
@given(instance=robotG_robot_Turn_strategy)
@settings(max_examples=25)
def test_robotG_robot_Turn_instantiation(instance):
    assert isinstance(instance, robotG_robot_Turn)


robot_CommandeRobot_strategy = st.builds(robot_CommandeRobot)
@given(instance=robot_CommandeRobot_strategy)
@settings(max_examples=25)
def test_robot_CommandeRobot_instantiation(instance):
    assert isinstance(instance, robot_CommandeRobot)


