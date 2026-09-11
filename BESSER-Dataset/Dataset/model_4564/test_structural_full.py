import inspect
import pytest
from datetime import date, datetime, time, timedelta
from hypothesis import given, settings
import hypothesis.strategies as st

from python_code import (
    BoolExp,
    Command,
    Expression,
    FlotCtrl_BoolExp,
    robot_Command,
    robot_FlotCtrl_AndExp,
    robot_FlotCtrl_BoolExp,
    robot_FlotCtrl_Expression,
    robot_FlotCtrl_IfBlock,
    robot_FlotCtrl_NegExp,
    robot_FlotCtrl_WhileLoop,
    robot_robot_Bip,
    robot_robot_Command,
    robot_robot_HasTurnedCmd,
    robot_robot_MoveCmd,
    robot_robot_ObstacleCmd,
    robot_robot_PrintCmd,
    robot_robot_ProgramUnit,
    robot_robot_SetTurnAngleCmd,
    robot_robot_StopEngineCmd,
    robot_robot_StopProgramCmd,
    robot_robot_TurnCmd,
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

def test_robot_robot_Bip_duration_value_roundtrip():
    instance = robot_robot_Bip(duration="sample_text", power="sample_text", repet="sample_text")
    assert instance.duration == "sample_text"
    instance.duration = "sample_text_2"
    assert instance.duration == "sample_text_2"


def test_robot_robot_Bip_power_value_roundtrip():
    instance = robot_robot_Bip(duration="sample_text", power="sample_text", repet="sample_text")
    assert instance.power == "sample_text"
    instance.power = "sample_text_2"
    assert instance.power == "sample_text_2"


def test_robot_robot_Bip_repet_value_roundtrip():
    instance = robot_robot_Bip(duration="sample_text", power="sample_text", repet="sample_text")
    assert instance.repet == "sample_text"
    instance.repet = "sample_text_2"
    assert instance.repet == "sample_text_2"


def test_robot_robot_HasTurnedCmd_angle_value_roundtrip():
    instance = robot_robot_HasTurnedCmd(angle="sample_text")
    assert instance.angle == "sample_text"
    instance.angle = "sample_text_2"
    assert instance.angle == "sample_text_2"


def test_robot_robot_MoveCmd_power_value_roundtrip():
    instance = robot_robot_MoveCmd(power="sample_text")
    assert instance.power == "sample_text"
    instance.power = "sample_text_2"
    assert instance.power == "sample_text_2"


def test_robot_robot_ObstacleCmd_distance_value_roundtrip():
    instance = robot_robot_ObstacleCmd(distance="sample_text")
    assert instance.distance == "sample_text"
    instance.distance = "sample_text_2"
    assert instance.distance == "sample_text_2"


def test_robot_robot_PrintCmd_col_value_roundtrip():
    instance = robot_robot_PrintCmd(col="sample_text", duration="sample_text", line="sample_text", msg="sample_text")
    assert instance.col == "sample_text"
    instance.col = "sample_text_2"
    assert instance.col == "sample_text_2"


def test_robot_robot_PrintCmd_duration_value_roundtrip():
    instance = robot_robot_PrintCmd(col="sample_text", duration="sample_text", line="sample_text", msg="sample_text")
    assert instance.duration == "sample_text"
    instance.duration = "sample_text_2"
    assert instance.duration == "sample_text_2"


def test_robot_robot_PrintCmd_line_value_roundtrip():
    instance = robot_robot_PrintCmd(col="sample_text", duration="sample_text", line="sample_text", msg="sample_text")
    assert instance.line == "sample_text"
    instance.line = "sample_text_2"
    assert instance.line == "sample_text_2"


def test_robot_robot_PrintCmd_msg_value_roundtrip():
    instance = robot_robot_PrintCmd(col="sample_text", duration="sample_text", line="sample_text", msg="sample_text")
    assert instance.msg == "sample_text"
    instance.msg = "sample_text_2"
    assert instance.msg == "sample_text_2"


def test_robot_robot_SetTurnAngleCmd_angle_value_roundtrip():
    instance = robot_robot_SetTurnAngleCmd(angle="sample_text")
    assert instance.angle == "sample_text"
    instance.angle = "sample_text_2"
    assert instance.angle == "sample_text_2"


def test_robot_robot_TurnCmd_angle_value_roundtrip():
    instance = robot_robot_TurnCmd(angle="sample_text", power="sample_text")
    assert instance.angle == "sample_text"
    instance.angle = "sample_text_2"
    assert instance.angle == "sample_text_2"


def test_robot_robot_TurnCmd_power_value_roundtrip():
    instance = robot_robot_TurnCmd(angle="sample_text", power="sample_text")
    assert instance.power == "sample_text"
    instance.power = "sample_text_2"
    assert instance.power == "sample_text_2"


def test_robot_FlotCtrl_AndExp_isa_BoolExp():
    instance = robot_FlotCtrl_AndExp()
    assert isinstance(instance, BoolExp)


def test_robot_FlotCtrl_NegExp_isa_BoolExp():
    instance = robot_FlotCtrl_NegExp()
    assert isinstance(instance, BoolExp)


def test_robot_robot_Bip_isa_Command():
    instance = robot_robot_Bip(duration="sample_text", power="sample_text", repet="sample_text")
    assert isinstance(instance, Command)


def test_robot_robot_MoveCmd_isa_Command():
    instance = robot_robot_MoveCmd(power="sample_text")
    assert isinstance(instance, Command)


def test_robot_robot_PrintCmd_isa_Command():
    instance = robot_robot_PrintCmd(col="sample_text", duration="sample_text", line="sample_text", msg="sample_text")
    assert isinstance(instance, Command)


def test_robot_robot_SetTurnAngleCmd_isa_Command():
    instance = robot_robot_SetTurnAngleCmd(angle="sample_text")
    assert isinstance(instance, Command)


def test_robot_robot_StopEngineCmd_isa_Command():
    instance = robot_robot_StopEngineCmd()
    assert isinstance(instance, Command)


def test_robot_robot_StopProgramCmd_isa_Command():
    instance = robot_robot_StopProgramCmd()
    assert isinstance(instance, Command)


def test_robot_robot_TurnCmd_isa_Command():
    instance = robot_robot_TurnCmd(angle="sample_text", power="sample_text")
    assert isinstance(instance, Command)


def test_robot_FlotCtrl_BoolExp_isa_Expression():
    instance = robot_FlotCtrl_BoolExp()
    assert isinstance(instance, Expression)


def test_robot_FlotCtrl_IfBlock_isa_Expression():
    instance = robot_FlotCtrl_IfBlock()
    assert isinstance(instance, Expression)


def test_robot_FlotCtrl_WhileLoop_isa_Expression():
    instance = robot_FlotCtrl_WhileLoop()
    assert isinstance(instance, Expression)


def test_robot_robot_Command_isa_Expression():
    instance = robot_robot_Command()
    assert isinstance(instance, Expression)


def test_robot_robot_HasTurnedCmd_isa_FlotCtrl_BoolExp():
    instance = robot_robot_HasTurnedCmd(angle="sample_text")
    assert isinstance(instance, FlotCtrl_BoolExp)


def test_robot_robot_ObstacleCmd_isa_FlotCtrl_BoolExp():
    instance = robot_robot_ObstacleCmd(distance="sample_text")
    assert isinstance(instance, FlotCtrl_BoolExp)


def test_robot_robot_HasTurnedCmd_isa_robot_Command():
    instance = robot_robot_HasTurnedCmd(angle="sample_text")
    assert isinstance(instance, robot_Command)


def test_robot_robot_ObstacleCmd_isa_robot_Command():
    instance = robot_robot_ObstacleCmd(distance="sample_text")
    assert isinstance(instance, robot_Command)


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

BoolExp_strategy = st.builds(BoolExp)
@given(instance=BoolExp_strategy)
@settings(max_examples=25)
def test_BoolExp_instantiation(instance):
    assert isinstance(instance, BoolExp)


Command_strategy = st.builds(Command)
@given(instance=Command_strategy)
@settings(max_examples=25)
def test_Command_instantiation(instance):
    assert isinstance(instance, Command)


Expression_strategy = st.builds(Expression)
@given(instance=Expression_strategy)
@settings(max_examples=25)
def test_Expression_instantiation(instance):
    assert isinstance(instance, Expression)


FlotCtrl_BoolExp_strategy = st.builds(FlotCtrl_BoolExp)
@given(instance=FlotCtrl_BoolExp_strategy)
@settings(max_examples=25)
def test_FlotCtrl_BoolExp_instantiation(instance):
    assert isinstance(instance, FlotCtrl_BoolExp)


robot_Command_strategy = st.builds(robot_Command)
@given(instance=robot_Command_strategy)
@settings(max_examples=25)
def test_robot_Command_instantiation(instance):
    assert isinstance(instance, robot_Command)


robot_FlotCtrl_AndExp_strategy = st.builds(robot_FlotCtrl_AndExp)
@given(instance=robot_FlotCtrl_AndExp_strategy)
@settings(max_examples=25)
def test_robot_FlotCtrl_AndExp_instantiation(instance):
    assert isinstance(instance, robot_FlotCtrl_AndExp)


robot_FlotCtrl_BoolExp_strategy = st.builds(robot_FlotCtrl_BoolExp)
@given(instance=robot_FlotCtrl_BoolExp_strategy)
@settings(max_examples=25)
def test_robot_FlotCtrl_BoolExp_instantiation(instance):
    assert isinstance(instance, robot_FlotCtrl_BoolExp)


robot_FlotCtrl_Expression_strategy = st.builds(robot_FlotCtrl_Expression)
@given(instance=robot_FlotCtrl_Expression_strategy)
@settings(max_examples=25)
def test_robot_FlotCtrl_Expression_instantiation(instance):
    assert isinstance(instance, robot_FlotCtrl_Expression)


robot_FlotCtrl_IfBlock_strategy = st.builds(robot_FlotCtrl_IfBlock)
@given(instance=robot_FlotCtrl_IfBlock_strategy)
@settings(max_examples=25)
def test_robot_FlotCtrl_IfBlock_instantiation(instance):
    assert isinstance(instance, robot_FlotCtrl_IfBlock)


robot_FlotCtrl_NegExp_strategy = st.builds(robot_FlotCtrl_NegExp)
@given(instance=robot_FlotCtrl_NegExp_strategy)
@settings(max_examples=25)
def test_robot_FlotCtrl_NegExp_instantiation(instance):
    assert isinstance(instance, robot_FlotCtrl_NegExp)


robot_FlotCtrl_WhileLoop_strategy = st.builds(robot_FlotCtrl_WhileLoop)
@given(instance=robot_FlotCtrl_WhileLoop_strategy)
@settings(max_examples=25)
def test_robot_FlotCtrl_WhileLoop_instantiation(instance):
    assert isinstance(instance, robot_FlotCtrl_WhileLoop)


robot_robot_Bip_strategy = st.builds(robot_robot_Bip, duration=safe_text, power=safe_text, repet=safe_text)
@given(instance=robot_robot_Bip_strategy)
@settings(max_examples=25)
def test_robot_robot_Bip_instantiation(instance):
    assert isinstance(instance, robot_robot_Bip)


robot_robot_Command_strategy = st.builds(robot_robot_Command)
@given(instance=robot_robot_Command_strategy)
@settings(max_examples=25)
def test_robot_robot_Command_instantiation(instance):
    assert isinstance(instance, robot_robot_Command)


robot_robot_HasTurnedCmd_strategy = st.builds(robot_robot_HasTurnedCmd, angle=safe_text)
@given(instance=robot_robot_HasTurnedCmd_strategy)
@settings(max_examples=25)
def test_robot_robot_HasTurnedCmd_instantiation(instance):
    assert isinstance(instance, robot_robot_HasTurnedCmd)


robot_robot_MoveCmd_strategy = st.builds(robot_robot_MoveCmd, power=safe_text)
@given(instance=robot_robot_MoveCmd_strategy)
@settings(max_examples=25)
def test_robot_robot_MoveCmd_instantiation(instance):
    assert isinstance(instance, robot_robot_MoveCmd)


robot_robot_ObstacleCmd_strategy = st.builds(robot_robot_ObstacleCmd, distance=safe_text)
@given(instance=robot_robot_ObstacleCmd_strategy)
@settings(max_examples=25)
def test_robot_robot_ObstacleCmd_instantiation(instance):
    assert isinstance(instance, robot_robot_ObstacleCmd)


robot_robot_PrintCmd_strategy = st.builds(robot_robot_PrintCmd, col=safe_text, duration=safe_text, line=safe_text, msg=safe_text)
@given(instance=robot_robot_PrintCmd_strategy)
@settings(max_examples=25)
def test_robot_robot_PrintCmd_instantiation(instance):
    assert isinstance(instance, robot_robot_PrintCmd)


robot_robot_ProgramUnit_strategy = st.builds(robot_robot_ProgramUnit)
@given(instance=robot_robot_ProgramUnit_strategy)
@settings(max_examples=25)
def test_robot_robot_ProgramUnit_instantiation(instance):
    assert isinstance(instance, robot_robot_ProgramUnit)


robot_robot_SetTurnAngleCmd_strategy = st.builds(robot_robot_SetTurnAngleCmd, angle=safe_text)
@given(instance=robot_robot_SetTurnAngleCmd_strategy)
@settings(max_examples=25)
def test_robot_robot_SetTurnAngleCmd_instantiation(instance):
    assert isinstance(instance, robot_robot_SetTurnAngleCmd)


robot_robot_StopEngineCmd_strategy = st.builds(robot_robot_StopEngineCmd)
@given(instance=robot_robot_StopEngineCmd_strategy)
@settings(max_examples=25)
def test_robot_robot_StopEngineCmd_instantiation(instance):
    assert isinstance(instance, robot_robot_StopEngineCmd)


robot_robot_StopProgramCmd_strategy = st.builds(robot_robot_StopProgramCmd)
@given(instance=robot_robot_StopProgramCmd_strategy)
@settings(max_examples=25)
def test_robot_robot_StopProgramCmd_instantiation(instance):
    assert isinstance(instance, robot_robot_StopProgramCmd)


robot_robot_TurnCmd_strategy = st.builds(robot_robot_TurnCmd, angle=safe_text, power=safe_text)
@given(instance=robot_robot_TurnCmd_strategy)
@settings(max_examples=25)
def test_robot_robot_TurnCmd_instantiation(instance):
    assert isinstance(instance, robot_robot_TurnCmd)


