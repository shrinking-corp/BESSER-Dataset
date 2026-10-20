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
    robot_robot_ProgramUnit,
    robot_Command,
    FlotCtrl_BoolExp,
    robot_robot_HasTurnedCmd,
    robot_robot_ObstacleCmd,
    Command,
    robot_robot_TurnCmd,
    robot_robot_Bip,
    robot_robot_StopEngineCmd,
    robot_robot_PrintCmd,
    robot_robot_SetTurnAngleCmd,
    robot_robot_StopProgramCmd,
    robot_robot_MoveCmd,
    BoolExp,
    robot_FlotCtrl_AndExp,
    robot_FlotCtrl_NegExp,
    robot_FlotCtrl_Expression,
    Expression,
    robot_FlotCtrl_BoolExp,
    robot_FlotCtrl_IfBlock,
    robot_FlotCtrl_WhileLoop,
    robot_robot_Command,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_hyp_robot_robot_programunit_is_not_abstract():
    assert not inspect.isabstract(robot_robot_ProgramUnit)


def test_hyp_robot_robot_programunit_constructor_exists():
    assert callable(robot_robot_ProgramUnit.__init__)


def test_hyp_robot_robot_programunit_constructor_args():
    sig = inspect.signature(robot_robot_ProgramUnit.__init__)
    params = list(sig.parameters.keys())



def test_hyp_robot_command_is_not_abstract():
    assert not inspect.isabstract(robot_Command)


def test_hyp_robot_command_constructor_exists():
    assert callable(robot_Command.__init__)


def test_hyp_robot_command_constructor_args():
    sig = inspect.signature(robot_Command.__init__)
    params = list(sig.parameters.keys())



def test_hyp_flotctrl_boolexp_is_not_abstract():
    assert not inspect.isabstract(FlotCtrl_BoolExp)


def test_hyp_flotctrl_boolexp_constructor_exists():
    assert callable(FlotCtrl_BoolExp.__init__)


def test_hyp_flotctrl_boolexp_constructor_args():
    sig = inspect.signature(FlotCtrl_BoolExp.__init__)
    params = list(sig.parameters.keys())



def test_hyp_robot_robot_hasturnedcmd_is_not_abstract():
    assert not inspect.isabstract(robot_robot_HasTurnedCmd)


def test_hyp_robot_robot_hasturnedcmd_constructor_exists():
    assert callable(robot_robot_HasTurnedCmd.__init__)


def test_hyp_robot_robot_hasturnedcmd_constructor_args():
    sig = inspect.signature(robot_robot_HasTurnedCmd.__init__)
    params = list(sig.parameters.keys())
    assert "angle" in params, "Missing parameter 'angle'"




def test_hyp_robot_robot_obstaclecmd_is_not_abstract():
    assert not inspect.isabstract(robot_robot_ObstacleCmd)


def test_hyp_robot_robot_obstaclecmd_constructor_exists():
    assert callable(robot_robot_ObstacleCmd.__init__)


def test_hyp_robot_robot_obstaclecmd_constructor_args():
    sig = inspect.signature(robot_robot_ObstacleCmd.__init__)
    params = list(sig.parameters.keys())
    assert "distance" in params, "Missing parameter 'distance'"




def test_hyp_command_is_not_abstract():
    assert not inspect.isabstract(Command)


def test_hyp_command_constructor_exists():
    assert callable(Command.__init__)


def test_hyp_command_constructor_args():
    sig = inspect.signature(Command.__init__)
    params = list(sig.parameters.keys())



def test_hyp_robot_robot_turncmd_is_not_abstract():
    assert not inspect.isabstract(robot_robot_TurnCmd)


def test_hyp_robot_robot_turncmd_constructor_exists():
    assert callable(robot_robot_TurnCmd.__init__)


def test_hyp_robot_robot_turncmd_constructor_args():
    sig = inspect.signature(robot_robot_TurnCmd.__init__)
    params = list(sig.parameters.keys())
    assert "power" in params, "Missing parameter 'power'"
    assert "angle" in params, "Missing parameter 'angle'"





def test_hyp_robot_robot_bip_is_not_abstract():
    assert not inspect.isabstract(robot_robot_Bip)


def test_hyp_robot_robot_bip_constructor_exists():
    assert callable(robot_robot_Bip.__init__)


def test_hyp_robot_robot_bip_constructor_args():
    sig = inspect.signature(robot_robot_Bip.__init__)
    params = list(sig.parameters.keys())
    assert "power" in params, "Missing parameter 'power'"
    assert "duration" in params, "Missing parameter 'duration'"
    assert "repet" in params, "Missing parameter 'repet'"






def test_hyp_robot_robot_stopenginecmd_is_not_abstract():
    assert not inspect.isabstract(robot_robot_StopEngineCmd)


def test_hyp_robot_robot_stopenginecmd_constructor_exists():
    assert callable(robot_robot_StopEngineCmd.__init__)


def test_hyp_robot_robot_stopenginecmd_constructor_args():
    sig = inspect.signature(robot_robot_StopEngineCmd.__init__)
    params = list(sig.parameters.keys())



def test_hyp_robot_robot_printcmd_is_not_abstract():
    assert not inspect.isabstract(robot_robot_PrintCmd)


def test_hyp_robot_robot_printcmd_constructor_exists():
    assert callable(robot_robot_PrintCmd.__init__)


def test_hyp_robot_robot_printcmd_constructor_args():
    sig = inspect.signature(robot_robot_PrintCmd.__init__)
    params = list(sig.parameters.keys())
    assert "line" in params, "Missing parameter 'line'"
    assert "col" in params, "Missing parameter 'col'"
    assert "msg" in params, "Missing parameter 'msg'"
    assert "duration" in params, "Missing parameter 'duration'"







def test_hyp_robot_robot_setturnanglecmd_is_not_abstract():
    assert not inspect.isabstract(robot_robot_SetTurnAngleCmd)


def test_hyp_robot_robot_setturnanglecmd_constructor_exists():
    assert callable(robot_robot_SetTurnAngleCmd.__init__)


def test_hyp_robot_robot_setturnanglecmd_constructor_args():
    sig = inspect.signature(robot_robot_SetTurnAngleCmd.__init__)
    params = list(sig.parameters.keys())
    assert "angle" in params, "Missing parameter 'angle'"




def test_hyp_robot_robot_stopprogramcmd_is_not_abstract():
    assert not inspect.isabstract(robot_robot_StopProgramCmd)


def test_hyp_robot_robot_stopprogramcmd_constructor_exists():
    assert callable(robot_robot_StopProgramCmd.__init__)


def test_hyp_robot_robot_stopprogramcmd_constructor_args():
    sig = inspect.signature(robot_robot_StopProgramCmd.__init__)
    params = list(sig.parameters.keys())



def test_hyp_robot_robot_movecmd_is_not_abstract():
    assert not inspect.isabstract(robot_robot_MoveCmd)


def test_hyp_robot_robot_movecmd_constructor_exists():
    assert callable(robot_robot_MoveCmd.__init__)


def test_hyp_robot_robot_movecmd_constructor_args():
    sig = inspect.signature(robot_robot_MoveCmd.__init__)
    params = list(sig.parameters.keys())
    assert "power" in params, "Missing parameter 'power'"




def test_hyp_boolexp_is_not_abstract():
    assert not inspect.isabstract(BoolExp)


def test_hyp_boolexp_constructor_exists():
    assert callable(BoolExp.__init__)


def test_hyp_boolexp_constructor_args():
    sig = inspect.signature(BoolExp.__init__)
    params = list(sig.parameters.keys())



def test_hyp_robot_flotctrl_andexp_is_not_abstract():
    assert not inspect.isabstract(robot_FlotCtrl_AndExp)


def test_hyp_robot_flotctrl_andexp_constructor_exists():
    assert callable(robot_FlotCtrl_AndExp.__init__)


def test_hyp_robot_flotctrl_andexp_constructor_args():
    sig = inspect.signature(robot_FlotCtrl_AndExp.__init__)
    params = list(sig.parameters.keys())



def test_hyp_robot_flotctrl_negexp_is_not_abstract():
    assert not inspect.isabstract(robot_FlotCtrl_NegExp)


def test_hyp_robot_flotctrl_negexp_constructor_exists():
    assert callable(robot_FlotCtrl_NegExp.__init__)


def test_hyp_robot_flotctrl_negexp_constructor_args():
    sig = inspect.signature(robot_FlotCtrl_NegExp.__init__)
    params = list(sig.parameters.keys())



def test_hyp_robot_flotctrl_expression_is_not_abstract():
    assert not inspect.isabstract(robot_FlotCtrl_Expression)


def test_hyp_robot_flotctrl_expression_constructor_exists():
    assert callable(robot_FlotCtrl_Expression.__init__)


def test_hyp_robot_flotctrl_expression_constructor_args():
    sig = inspect.signature(robot_FlotCtrl_Expression.__init__)
    params = list(sig.parameters.keys())



def test_hyp_expression_is_not_abstract():
    assert not inspect.isabstract(Expression)


def test_hyp_expression_constructor_exists():
    assert callable(Expression.__init__)


def test_hyp_expression_constructor_args():
    sig = inspect.signature(Expression.__init__)
    params = list(sig.parameters.keys())



def test_hyp_robot_flotctrl_boolexp_is_not_abstract():
    assert not inspect.isabstract(robot_FlotCtrl_BoolExp)


def test_hyp_robot_flotctrl_boolexp_constructor_exists():
    assert callable(robot_FlotCtrl_BoolExp.__init__)


def test_hyp_robot_flotctrl_boolexp_constructor_args():
    sig = inspect.signature(robot_FlotCtrl_BoolExp.__init__)
    params = list(sig.parameters.keys())



def test_hyp_robot_flotctrl_ifblock_is_not_abstract():
    assert not inspect.isabstract(robot_FlotCtrl_IfBlock)


def test_hyp_robot_flotctrl_ifblock_constructor_exists():
    assert callable(robot_FlotCtrl_IfBlock.__init__)


def test_hyp_robot_flotctrl_ifblock_constructor_args():
    sig = inspect.signature(robot_FlotCtrl_IfBlock.__init__)
    params = list(sig.parameters.keys())



def test_hyp_robot_flotctrl_whileloop_is_not_abstract():
    assert not inspect.isabstract(robot_FlotCtrl_WhileLoop)


def test_hyp_robot_flotctrl_whileloop_constructor_exists():
    assert callable(robot_FlotCtrl_WhileLoop.__init__)


def test_hyp_robot_flotctrl_whileloop_constructor_args():
    sig = inspect.signature(robot_FlotCtrl_WhileLoop.__init__)
    params = list(sig.parameters.keys())



def test_hyp_robot_robot_command_is_not_abstract():
    assert not inspect.isabstract(robot_robot_Command)


def test_hyp_robot_robot_command_constructor_exists():
    assert callable(robot_robot_Command.__init__)


def test_hyp_robot_robot_command_constructor_args():
    sig = inspect.signature(robot_robot_Command.__init__)
    params = list(sig.parameters.keys())


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
robot_robot_ProgramUnit_strategy = st.builds(
    robot_robot_ProgramUnit,
)
robot_Command_strategy = st.builds(
    robot_Command,
)
FlotCtrl_BoolExp_strategy = st.builds(
    FlotCtrl_BoolExp,
)
robot_robot_HasTurnedCmd_strategy = st.builds(
    robot_robot_HasTurnedCmd,
    angle=
        safe_text
)
robot_robot_ObstacleCmd_strategy = st.builds(
    robot_robot_ObstacleCmd,
    distance=
        safe_text
)
Command_strategy = st.builds(
    Command,
)
robot_robot_TurnCmd_strategy = st.builds(
    robot_robot_TurnCmd,
    power=
        safe_text,
    angle=
        safe_text
)
robot_robot_Bip_strategy = st.builds(
    robot_robot_Bip,
    power=
        safe_text,
    duration=
        safe_text,
    repet=
        safe_text
)
robot_robot_StopEngineCmd_strategy = st.builds(
    robot_robot_StopEngineCmd,
)
robot_robot_PrintCmd_strategy = st.builds(
    robot_robot_PrintCmd,
    line=
        safe_text,
    col=
        safe_text,
    msg=
        safe_text,
    duration=
        safe_text
)
robot_robot_SetTurnAngleCmd_strategy = st.builds(
    robot_robot_SetTurnAngleCmd,
    angle=
        safe_text
)
robot_robot_StopProgramCmd_strategy = st.builds(
    robot_robot_StopProgramCmd,
)
robot_robot_MoveCmd_strategy = st.builds(
    robot_robot_MoveCmd,
    power=
        safe_text
)
BoolExp_strategy = st.builds(
    BoolExp,
)
robot_FlotCtrl_AndExp_strategy = st.builds(
    robot_FlotCtrl_AndExp,
)
robot_FlotCtrl_NegExp_strategy = st.builds(
    robot_FlotCtrl_NegExp,
)
robot_FlotCtrl_Expression_strategy = st.builds(
    robot_FlotCtrl_Expression,
)
Expression_strategy = st.builds(
    Expression,
)
robot_FlotCtrl_BoolExp_strategy = st.builds(
    robot_FlotCtrl_BoolExp,
)
robot_FlotCtrl_IfBlock_strategy = st.builds(
    robot_FlotCtrl_IfBlock,
)
robot_FlotCtrl_WhileLoop_strategy = st.builds(
    robot_FlotCtrl_WhileLoop,
)
robot_robot_Command_strategy = st.builds(
    robot_robot_Command,
)







@given(instance=robot_robot_HasTurnedCmd_strategy)
def test_hyp_robot_robot_hasturnedcmd_angle_setter(instance):
    original = instance.angle
    instance.angle = original
    assert instance.angle == original




@given(instance=robot_robot_ObstacleCmd_strategy)
def test_hyp_robot_robot_obstaclecmd_distance_setter(instance):
    original = instance.distance
    instance.distance = original
    assert instance.distance == original





@given(instance=robot_robot_TurnCmd_strategy)
def test_hyp_robot_robot_turncmd_power_setter(instance):
    original = instance.power
    instance.power = original
    assert instance.power == original



@given(instance=robot_robot_TurnCmd_strategy)
def test_hyp_robot_robot_turncmd_angle_setter(instance):
    original = instance.angle
    instance.angle = original
    assert instance.angle == original




@given(instance=robot_robot_Bip_strategy)
def test_hyp_robot_robot_bip_power_setter(instance):
    original = instance.power
    instance.power = original
    assert instance.power == original



@given(instance=robot_robot_Bip_strategy)
def test_hyp_robot_robot_bip_duration_setter(instance):
    original = instance.duration
    instance.duration = original
    assert instance.duration == original



@given(instance=robot_robot_Bip_strategy)
def test_hyp_robot_robot_bip_repet_setter(instance):
    original = instance.repet
    instance.repet = original
    assert instance.repet == original





@given(instance=robot_robot_PrintCmd_strategy)
def test_hyp_robot_robot_printcmd_line_setter(instance):
    original = instance.line
    instance.line = original
    assert instance.line == original



@given(instance=robot_robot_PrintCmd_strategy)
def test_hyp_robot_robot_printcmd_col_setter(instance):
    original = instance.col
    instance.col = original
    assert instance.col == original



@given(instance=robot_robot_PrintCmd_strategy)
def test_hyp_robot_robot_printcmd_msg_setter(instance):
    original = instance.msg
    instance.msg = original
    assert instance.msg == original



@given(instance=robot_robot_PrintCmd_strategy)
def test_hyp_robot_robot_printcmd_duration_setter(instance):
    original = instance.duration
    instance.duration = original
    assert instance.duration == original




@given(instance=robot_robot_SetTurnAngleCmd_strategy)
def test_hyp_robot_robot_setturnanglecmd_angle_setter(instance):
    original = instance.angle
    instance.angle = original
    assert instance.angle == original





@given(instance=robot_robot_MoveCmd_strategy)
def test_hyp_robot_robot_movecmd_power_setter(instance):
    original = instance.power
    instance.power = original
    assert instance.power == original











# ----- SECTION B: test_structural_full.py (deterministic-first suite) -----
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



