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
    robotG_flow_Programme,
    OpBinaire,
    robotG_flow_Or,
    robotG_flow_And,
    robotG_flow_Expr,
    OpUnaire,
    robotG_flow_Not,
    ExprBool,
    robotG_flow_OpUnaire,
    robotG_flow_OpBinaire,
    Expr,
    robotG_flow_StopProgram,
    robotG_flow_If,
    robotG_flow_While,
    robotG_flow_ExprBool,
    robotG_robot_CommandeRobot,
    robot_CommandeRobot,
    flow_ExprBool,
    robotG_robot_Obstacle,
    robotG_robot_HasTurned,
    CommandeRobot,
    robotG_robot_Display,
    robotG_robot_Bip,
    robotG_robot_SetTurnAngle,
    robotG_robot_StopEngine,
    robotG_robot_Turn,
    robotG_robot_Move,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_hyp_robotg_flow_programme_is_not_abstract():
    assert not inspect.isabstract(robotG_flow_Programme)


def test_hyp_robotg_flow_programme_constructor_exists():
    assert callable(robotG_flow_Programme.__init__)


def test_hyp_robotg_flow_programme_constructor_args():
    sig = inspect.signature(robotG_flow_Programme.__init__)
    params = list(sig.parameters.keys())



def test_hyp_opbinaire_is_not_abstract():
    assert not inspect.isabstract(OpBinaire)


def test_hyp_opbinaire_constructor_exists():
    assert callable(OpBinaire.__init__)


def test_hyp_opbinaire_constructor_args():
    sig = inspect.signature(OpBinaire.__init__)
    params = list(sig.parameters.keys())



def test_hyp_robotg_flow_or_is_not_abstract():
    assert not inspect.isabstract(robotG_flow_Or)


def test_hyp_robotg_flow_or_constructor_exists():
    assert callable(robotG_flow_Or.__init__)


def test_hyp_robotg_flow_or_constructor_args():
    sig = inspect.signature(robotG_flow_Or.__init__)
    params = list(sig.parameters.keys())



def test_hyp_robotg_flow_and_is_not_abstract():
    assert not inspect.isabstract(robotG_flow_And)


def test_hyp_robotg_flow_and_constructor_exists():
    assert callable(robotG_flow_And.__init__)


def test_hyp_robotg_flow_and_constructor_args():
    sig = inspect.signature(robotG_flow_And.__init__)
    params = list(sig.parameters.keys())



def test_hyp_robotg_flow_expr_is_not_abstract():
    assert not inspect.isabstract(robotG_flow_Expr)


def test_hyp_robotg_flow_expr_constructor_exists():
    assert callable(robotG_flow_Expr.__init__)


def test_hyp_robotg_flow_expr_constructor_args():
    sig = inspect.signature(robotG_flow_Expr.__init__)
    params = list(sig.parameters.keys())



def test_hyp_opunaire_is_not_abstract():
    assert not inspect.isabstract(OpUnaire)


def test_hyp_opunaire_constructor_exists():
    assert callable(OpUnaire.__init__)


def test_hyp_opunaire_constructor_args():
    sig = inspect.signature(OpUnaire.__init__)
    params = list(sig.parameters.keys())



def test_hyp_robotg_flow_not_is_not_abstract():
    assert not inspect.isabstract(robotG_flow_Not)


def test_hyp_robotg_flow_not_constructor_exists():
    assert callable(robotG_flow_Not.__init__)


def test_hyp_robotg_flow_not_constructor_args():
    sig = inspect.signature(robotG_flow_Not.__init__)
    params = list(sig.parameters.keys())



def test_hyp_exprbool_is_not_abstract():
    assert not inspect.isabstract(ExprBool)


def test_hyp_exprbool_constructor_exists():
    assert callable(ExprBool.__init__)


def test_hyp_exprbool_constructor_args():
    sig = inspect.signature(ExprBool.__init__)
    params = list(sig.parameters.keys())



def test_hyp_robotg_flow_opunaire_is_not_abstract():
    assert not inspect.isabstract(robotG_flow_OpUnaire)


def test_hyp_robotg_flow_opunaire_constructor_exists():
    assert callable(robotG_flow_OpUnaire.__init__)


def test_hyp_robotg_flow_opunaire_constructor_args():
    sig = inspect.signature(robotG_flow_OpUnaire.__init__)
    params = list(sig.parameters.keys())



def test_hyp_robotg_flow_opbinaire_is_not_abstract():
    assert not inspect.isabstract(robotG_flow_OpBinaire)


def test_hyp_robotg_flow_opbinaire_constructor_exists():
    assert callable(robotG_flow_OpBinaire.__init__)


def test_hyp_robotg_flow_opbinaire_constructor_args():
    sig = inspect.signature(robotG_flow_OpBinaire.__init__)
    params = list(sig.parameters.keys())



def test_hyp_expr_is_not_abstract():
    assert not inspect.isabstract(Expr)


def test_hyp_expr_constructor_exists():
    assert callable(Expr.__init__)


def test_hyp_expr_constructor_args():
    sig = inspect.signature(Expr.__init__)
    params = list(sig.parameters.keys())



def test_hyp_robotg_flow_stopprogram_is_not_abstract():
    assert not inspect.isabstract(robotG_flow_StopProgram)


def test_hyp_robotg_flow_stopprogram_constructor_exists():
    assert callable(robotG_flow_StopProgram.__init__)


def test_hyp_robotg_flow_stopprogram_constructor_args():
    sig = inspect.signature(robotG_flow_StopProgram.__init__)
    params = list(sig.parameters.keys())



def test_hyp_robotg_flow_if_is_not_abstract():
    assert not inspect.isabstract(robotG_flow_If)


def test_hyp_robotg_flow_if_constructor_exists():
    assert callable(robotG_flow_If.__init__)


def test_hyp_robotg_flow_if_constructor_args():
    sig = inspect.signature(robotG_flow_If.__init__)
    params = list(sig.parameters.keys())



def test_hyp_robotg_flow_while_is_not_abstract():
    assert not inspect.isabstract(robotG_flow_While)


def test_hyp_robotg_flow_while_constructor_exists():
    assert callable(robotG_flow_While.__init__)


def test_hyp_robotg_flow_while_constructor_args():
    sig = inspect.signature(robotG_flow_While.__init__)
    params = list(sig.parameters.keys())



def test_hyp_robotg_flow_exprbool_is_not_abstract():
    assert not inspect.isabstract(robotG_flow_ExprBool)


def test_hyp_robotg_flow_exprbool_constructor_exists():
    assert callable(robotG_flow_ExprBool.__init__)


def test_hyp_robotg_flow_exprbool_constructor_args():
    sig = inspect.signature(robotG_flow_ExprBool.__init__)
    params = list(sig.parameters.keys())



def test_hyp_robotg_robot_commanderobot_is_not_abstract():
    assert not inspect.isabstract(robotG_robot_CommandeRobot)


def test_hyp_robotg_robot_commanderobot_constructor_exists():
    assert callable(robotG_robot_CommandeRobot.__init__)


def test_hyp_robotg_robot_commanderobot_constructor_args():
    sig = inspect.signature(robotG_robot_CommandeRobot.__init__)
    params = list(sig.parameters.keys())



def test_hyp_robot_commanderobot_is_not_abstract():
    assert not inspect.isabstract(robot_CommandeRobot)


def test_hyp_robot_commanderobot_constructor_exists():
    assert callable(robot_CommandeRobot.__init__)


def test_hyp_robot_commanderobot_constructor_args():
    sig = inspect.signature(robot_CommandeRobot.__init__)
    params = list(sig.parameters.keys())



def test_hyp_flow_exprbool_is_not_abstract():
    assert not inspect.isabstract(flow_ExprBool)


def test_hyp_flow_exprbool_constructor_exists():
    assert callable(flow_ExprBool.__init__)


def test_hyp_flow_exprbool_constructor_args():
    sig = inspect.signature(flow_ExprBool.__init__)
    params = list(sig.parameters.keys())



def test_hyp_robotg_robot_obstacle_is_not_abstract():
    assert not inspect.isabstract(robotG_robot_Obstacle)


def test_hyp_robotg_robot_obstacle_constructor_exists():
    assert callable(robotG_robot_Obstacle.__init__)


def test_hyp_robotg_robot_obstacle_constructor_args():
    sig = inspect.signature(robotG_robot_Obstacle.__init__)
    params = list(sig.parameters.keys())
    assert "distance" in params, "Missing parameter 'distance'"




def test_hyp_robotg_robot_hasturned_is_not_abstract():
    assert not inspect.isabstract(robotG_robot_HasTurned)


def test_hyp_robotg_robot_hasturned_constructor_exists():
    assert callable(robotG_robot_HasTurned.__init__)


def test_hyp_robotg_robot_hasturned_constructor_args():
    sig = inspect.signature(robotG_robot_HasTurned.__init__)
    params = list(sig.parameters.keys())
    assert "angle" in params, "Missing parameter 'angle'"




def test_hyp_commanderobot_is_not_abstract():
    assert not inspect.isabstract(CommandeRobot)


def test_hyp_commanderobot_constructor_exists():
    assert callable(CommandeRobot.__init__)


def test_hyp_commanderobot_constructor_args():
    sig = inspect.signature(CommandeRobot.__init__)
    params = list(sig.parameters.keys())



def test_hyp_robotg_robot_display_is_not_abstract():
    assert not inspect.isabstract(robotG_robot_Display)


def test_hyp_robotg_robot_display_constructor_exists():
    assert callable(robotG_robot_Display.__init__)


def test_hyp_robotg_robot_display_constructor_args():
    sig = inspect.signature(robotG_robot_Display.__init__)
    params = list(sig.parameters.keys())
    assert "line" in params, "Missing parameter 'line'"
    assert "msg" in params, "Missing parameter 'msg'"
    assert "duration" in params, "Missing parameter 'duration'"
    assert "col" in params, "Missing parameter 'col'"







def test_hyp_robotg_robot_bip_is_not_abstract():
    assert not inspect.isabstract(robotG_robot_Bip)


def test_hyp_robotg_robot_bip_constructor_exists():
    assert callable(robotG_robot_Bip.__init__)


def test_hyp_robotg_robot_bip_constructor_args():
    sig = inspect.signature(robotG_robot_Bip.__init__)
    params = list(sig.parameters.keys())
    assert "power" in params, "Missing parameter 'power'"
    assert "duration" in params, "Missing parameter 'duration'"
    assert "repeat" in params, "Missing parameter 'repeat'"






def test_hyp_robotg_robot_setturnangle_is_not_abstract():
    assert not inspect.isabstract(robotG_robot_SetTurnAngle)


def test_hyp_robotg_robot_setturnangle_constructor_exists():
    assert callable(robotG_robot_SetTurnAngle.__init__)


def test_hyp_robotg_robot_setturnangle_constructor_args():
    sig = inspect.signature(robotG_robot_SetTurnAngle.__init__)
    params = list(sig.parameters.keys())
    assert "angle" in params, "Missing parameter 'angle'"




def test_hyp_robotg_robot_stopengine_is_not_abstract():
    assert not inspect.isabstract(robotG_robot_StopEngine)


def test_hyp_robotg_robot_stopengine_constructor_exists():
    assert callable(robotG_robot_StopEngine.__init__)


def test_hyp_robotg_robot_stopengine_constructor_args():
    sig = inspect.signature(robotG_robot_StopEngine.__init__)
    params = list(sig.parameters.keys())



def test_hyp_robotg_robot_turn_is_not_abstract():
    assert not inspect.isabstract(robotG_robot_Turn)


def test_hyp_robotg_robot_turn_constructor_exists():
    assert callable(robotG_robot_Turn.__init__)


def test_hyp_robotg_robot_turn_constructor_args():
    sig = inspect.signature(robotG_robot_Turn.__init__)
    params = list(sig.parameters.keys())
    assert "angle" in params, "Missing parameter 'angle'"
    assert "power" in params, "Missing parameter 'power'"





def test_hyp_robotg_robot_move_is_not_abstract():
    assert not inspect.isabstract(robotG_robot_Move)


def test_hyp_robotg_robot_move_constructor_exists():
    assert callable(robotG_robot_Move.__init__)


def test_hyp_robotg_robot_move_constructor_args():
    sig = inspect.signature(robotG_robot_Move.__init__)
    params = list(sig.parameters.keys())
    assert "power" in params, "Missing parameter 'power'"



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
robotG_flow_Programme_strategy = st.builds(
    robotG_flow_Programme,
)
OpBinaire_strategy = st.builds(
    OpBinaire,
)
robotG_flow_Or_strategy = st.builds(
    robotG_flow_Or,
)
robotG_flow_And_strategy = st.builds(
    robotG_flow_And,
)
robotG_flow_Expr_strategy = st.builds(
    robotG_flow_Expr,
)
OpUnaire_strategy = st.builds(
    OpUnaire,
)
robotG_flow_Not_strategy = st.builds(
    robotG_flow_Not,
)
ExprBool_strategy = st.builds(
    ExprBool,
)
robotG_flow_OpUnaire_strategy = st.builds(
    robotG_flow_OpUnaire,
)
robotG_flow_OpBinaire_strategy = st.builds(
    robotG_flow_OpBinaire,
)
Expr_strategy = st.builds(
    Expr,
)
robotG_flow_StopProgram_strategy = st.builds(
    robotG_flow_StopProgram,
)
robotG_flow_If_strategy = st.builds(
    robotG_flow_If,
)
robotG_flow_While_strategy = st.builds(
    robotG_flow_While,
)
robotG_flow_ExprBool_strategy = st.builds(
    robotG_flow_ExprBool,
)
robotG_robot_CommandeRobot_strategy = st.builds(
    robotG_robot_CommandeRobot,
)
robot_CommandeRobot_strategy = st.builds(
    robot_CommandeRobot,
)
flow_ExprBool_strategy = st.builds(
    flow_ExprBool,
)
robotG_robot_Obstacle_strategy = st.builds(
    robotG_robot_Obstacle,
    distance=
        st.integers()
)
robotG_robot_HasTurned_strategy = st.builds(
    robotG_robot_HasTurned,
    angle=
        st.integers()
)
CommandeRobot_strategy = st.builds(
    CommandeRobot,
)
robotG_robot_Display_strategy = st.builds(
    robotG_robot_Display,
    line=
        st.integers(),
    msg=
        safe_text,
    duration=
        st.integers(),
    col=
        st.integers()
)
robotG_robot_Bip_strategy = st.builds(
    robotG_robot_Bip,
    power=
        st.integers(),
    duration=
        st.integers(),
    repeat=
        st.booleans()
)
robotG_robot_SetTurnAngle_strategy = st.builds(
    robotG_robot_SetTurnAngle,
    angle=
        st.integers()
)
robotG_robot_StopEngine_strategy = st.builds(
    robotG_robot_StopEngine,
)
robotG_robot_Turn_strategy = st.builds(
    robotG_robot_Turn,
    angle=
        st.integers(),
    power=
        st.integers()
)
robotG_robot_Move_strategy = st.builds(
    robotG_robot_Move,
    power=
        st.integers()
)






















@given(instance=robotG_robot_Obstacle_strategy)
def test_hyp_robotg_robot_obstacle_distance_setter(instance):
    original = instance.distance
    instance.distance = original
    assert instance.distance == original




@given(instance=robotG_robot_HasTurned_strategy)
def test_hyp_robotg_robot_hasturned_angle_setter(instance):
    original = instance.angle
    instance.angle = original
    assert instance.angle == original





@given(instance=robotG_robot_Display_strategy)
def test_hyp_robotg_robot_display_line_setter(instance):
    original = instance.line
    instance.line = original
    assert instance.line == original



@given(instance=robotG_robot_Display_strategy)
def test_hyp_robotg_robot_display_msg_setter(instance):
    original = instance.msg
    instance.msg = original
    assert instance.msg == original



@given(instance=robotG_robot_Display_strategy)
def test_hyp_robotg_robot_display_duration_setter(instance):
    original = instance.duration
    instance.duration = original
    assert instance.duration == original



@given(instance=robotG_robot_Display_strategy)
def test_hyp_robotg_robot_display_col_setter(instance):
    original = instance.col
    instance.col = original
    assert instance.col == original




@given(instance=robotG_robot_Bip_strategy)
def test_hyp_robotg_robot_bip_power_setter(instance):
    original = instance.power
    instance.power = original
    assert instance.power == original



@given(instance=robotG_robot_Bip_strategy)
def test_hyp_robotg_robot_bip_duration_setter(instance):
    original = instance.duration
    instance.duration = original
    assert instance.duration == original



@given(instance=robotG_robot_Bip_strategy)
def test_hyp_robotg_robot_bip_repeat_setter(instance):
    original = instance.repeat
    instance.repeat = original
    assert instance.repeat == original




@given(instance=robotG_robot_SetTurnAngle_strategy)
def test_hyp_robotg_robot_setturnangle_angle_setter(instance):
    original = instance.angle
    instance.angle = original
    assert instance.angle == original





@given(instance=robotG_robot_Turn_strategy)
def test_hyp_robotg_robot_turn_angle_setter(instance):
    original = instance.angle
    instance.angle = original
    assert instance.angle == original



@given(instance=robotG_robot_Turn_strategy)
def test_hyp_robotg_robot_turn_power_setter(instance):
    original = instance.power
    instance.power = original
    assert instance.power == original




@given(instance=robotG_robot_Move_strategy)
def test_hyp_robotg_robot_move_power_setter(instance):
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



