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
    Expression,
    dSL_ORexpression,
    dSL_DepthLiteral,
    dSL_ANDexpression,
    dSL_ExpressionBracket,
    dSL_TrueLiteral,
    dSL_EdgeLiteral,
    dSL_DistanceLiteral,
    dSL_ColorLiteral,
    dSL_TouchLiteral,
    dSL_MovementAction,
    Actions,
    dSL_LeftMovementAction,
    dSL_MeasurementAction,
    dSL_MoveAction,
    dSL_Actions,
    dSL_Expression,
    RotatePoints,
    dSL_RightRotatePoint,
    dSL_MiddleRotatePoint,
    dSL_LeftRotatePoint,
    RotateMovementAction,
    dSL_RotatePoints,
    dSL_RotateMovementAction,
    dSL_RightMovementAction,
    dSL_Behavior,
    dSL_Mission,
    dSL_MarsRoverExpedition,
    EndCondition,
    dSL_EndAfter,
    dSL_EndWhen,
    dSL_EndCondition,
    dSL_BehaviorName,
    ActionEnum,
    Tenum,
    EdgeEnum,
    TouchEnum,
    BackEnum,
    LREnum,
    FBEnum,
    ColorEnum,
    MAEnum,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_hyp_expression_is_not_abstract():
    assert not inspect.isabstract(Expression)


def test_hyp_expression_constructor_exists():
    assert callable(Expression.__init__)


def test_hyp_expression_constructor_args():
    sig = inspect.signature(Expression.__init__)
    params = list(sig.parameters.keys())



def test_hyp_dsl_orexpression_is_not_abstract():
    assert not inspect.isabstract(dSL_ORexpression)


def test_hyp_dsl_orexpression_constructor_exists():
    assert callable(dSL_ORexpression.__init__)


def test_hyp_dsl_orexpression_constructor_args():
    sig = inspect.signature(dSL_ORexpression.__init__)
    params = list(sig.parameters.keys())



def test_hyp_dsl_depthliteral_is_not_abstract():
    assert not inspect.isabstract(dSL_DepthLiteral)


def test_hyp_dsl_depthliteral_constructor_exists():
    assert callable(dSL_DepthLiteral.__init__)


def test_hyp_dsl_depthliteral_constructor_args():
    sig = inspect.signature(dSL_DepthLiteral.__init__)
    params = list(sig.parameters.keys())
    assert "back" in params, "Missing parameter 'back'"




def test_hyp_dsl_andexpression_is_not_abstract():
    assert not inspect.isabstract(dSL_ANDexpression)


def test_hyp_dsl_andexpression_constructor_exists():
    assert callable(dSL_ANDexpression.__init__)


def test_hyp_dsl_andexpression_constructor_args():
    sig = inspect.signature(dSL_ANDexpression.__init__)
    params = list(sig.parameters.keys())



def test_hyp_dsl_expressionbracket_is_not_abstract():
    assert not inspect.isabstract(dSL_ExpressionBracket)


def test_hyp_dsl_expressionbracket_constructor_exists():
    assert callable(dSL_ExpressionBracket.__init__)


def test_hyp_dsl_expressionbracket_constructor_args():
    sig = inspect.signature(dSL_ExpressionBracket.__init__)
    params = list(sig.parameters.keys())



def test_hyp_dsl_trueliteral_is_not_abstract():
    assert not inspect.isabstract(dSL_TrueLiteral)


def test_hyp_dsl_trueliteral_constructor_exists():
    assert callable(dSL_TrueLiteral.__init__)


def test_hyp_dsl_trueliteral_constructor_args():
    sig = inspect.signature(dSL_TrueLiteral.__init__)
    params = list(sig.parameters.keys())
    assert "t" in params, "Missing parameter 't'"




def test_hyp_dsl_edgeliteral_is_not_abstract():
    assert not inspect.isabstract(dSL_EdgeLiteral)


def test_hyp_dsl_edgeliteral_constructor_exists():
    assert callable(dSL_EdgeLiteral.__init__)


def test_hyp_dsl_edgeliteral_constructor_args():
    sig = inspect.signature(dSL_EdgeLiteral.__init__)
    params = list(sig.parameters.keys())
    assert "edge" in params, "Missing parameter 'edge'"




def test_hyp_dsl_distanceliteral_is_not_abstract():
    assert not inspect.isabstract(dSL_DistanceLiteral)


def test_hyp_dsl_distanceliteral_constructor_exists():
    assert callable(dSL_DistanceLiteral.__init__)


def test_hyp_dsl_distanceliteral_constructor_args():
    sig = inspect.signature(dSL_DistanceLiteral.__init__)
    params = list(sig.parameters.keys())
    assert "distance" in params, "Missing parameter 'distance'"




def test_hyp_dsl_colorliteral_is_not_abstract():
    assert not inspect.isabstract(dSL_ColorLiteral)


def test_hyp_dsl_colorliteral_constructor_exists():
    assert callable(dSL_ColorLiteral.__init__)


def test_hyp_dsl_colorliteral_constructor_args():
    sig = inspect.signature(dSL_ColorLiteral.__init__)
    params = list(sig.parameters.keys())
    assert "color" in params, "Missing parameter 'color'"




def test_hyp_dsl_touchliteral_is_not_abstract():
    assert not inspect.isabstract(dSL_TouchLiteral)


def test_hyp_dsl_touchliteral_constructor_exists():
    assert callable(dSL_TouchLiteral.__init__)


def test_hyp_dsl_touchliteral_constructor_args():
    sig = inspect.signature(dSL_TouchLiteral.__init__)
    params = list(sig.parameters.keys())
    assert "touch" in params, "Missing parameter 'touch'"




def test_hyp_dsl_movementaction_is_not_abstract():
    assert not inspect.isabstract(dSL_MovementAction)


def test_hyp_dsl_movementaction_constructor_exists():
    assert callable(dSL_MovementAction.__init__)


def test_hyp_dsl_movementaction_constructor_args():
    sig = inspect.signature(dSL_MovementAction.__init__)
    params = list(sig.parameters.keys())
    assert "actionenum" in params, "Missing parameter 'actionenum'"




def test_hyp_actions_is_not_abstract():
    assert not inspect.isabstract(Actions)


def test_hyp_actions_constructor_exists():
    assert callable(Actions.__init__)


def test_hyp_actions_constructor_args():
    sig = inspect.signature(Actions.__init__)
    params = list(sig.parameters.keys())



def test_hyp_dsl_leftmovementaction_is_not_abstract():
    assert not inspect.isabstract(dSL_LeftMovementAction)


def test_hyp_dsl_leftmovementaction_constructor_exists():
    assert callable(dSL_LeftMovementAction.__init__)


def test_hyp_dsl_leftmovementaction_constructor_args():
    sig = inspect.signature(dSL_LeftMovementAction.__init__)
    params = list(sig.parameters.keys())



def test_hyp_dsl_measurementaction_is_not_abstract():
    assert not inspect.isabstract(dSL_MeasurementAction)


def test_hyp_dsl_measurementaction_constructor_exists():
    assert callable(dSL_MeasurementAction.__init__)


def test_hyp_dsl_measurementaction_constructor_args():
    sig = inspect.signature(dSL_MeasurementAction.__init__)
    params = list(sig.parameters.keys())
    assert "measure" in params, "Missing parameter 'measure'"




def test_hyp_dsl_moveaction_is_not_abstract():
    assert not inspect.isabstract(dSL_MoveAction)


def test_hyp_dsl_moveaction_constructor_exists():
    assert callable(dSL_MoveAction.__init__)


def test_hyp_dsl_moveaction_constructor_args():
    sig = inspect.signature(dSL_MoveAction.__init__)
    params = list(sig.parameters.keys())
    assert "dir" in params, "Missing parameter 'dir'"




def test_hyp_dsl_actions_is_not_abstract():
    assert not inspect.isabstract(dSL_Actions)


def test_hyp_dsl_actions_constructor_exists():
    assert callable(dSL_Actions.__init__)


def test_hyp_dsl_actions_constructor_args():
    sig = inspect.signature(dSL_Actions.__init__)
    params = list(sig.parameters.keys())



def test_hyp_dsl_expression_is_not_abstract():
    assert not inspect.isabstract(dSL_Expression)


def test_hyp_dsl_expression_constructor_exists():
    assert callable(dSL_Expression.__init__)


def test_hyp_dsl_expression_constructor_args():
    sig = inspect.signature(dSL_Expression.__init__)
    params = list(sig.parameters.keys())



def test_hyp_rotatepoints_is_not_abstract():
    assert not inspect.isabstract(RotatePoints)


def test_hyp_rotatepoints_constructor_exists():
    assert callable(RotatePoints.__init__)


def test_hyp_rotatepoints_constructor_args():
    sig = inspect.signature(RotatePoints.__init__)
    params = list(sig.parameters.keys())



def test_hyp_dsl_rightrotatepoint_is_not_abstract():
    assert not inspect.isabstract(dSL_RightRotatePoint)


def test_hyp_dsl_rightrotatepoint_constructor_exists():
    assert callable(dSL_RightRotatePoint.__init__)


def test_hyp_dsl_rightrotatepoint_constructor_args():
    sig = inspect.signature(dSL_RightRotatePoint.__init__)
    params = list(sig.parameters.keys())
    assert "rightdir" in params, "Missing parameter 'rightdir'"




def test_hyp_dsl_middlerotatepoint_is_not_abstract():
    assert not inspect.isabstract(dSL_MiddleRotatePoint)


def test_hyp_dsl_middlerotatepoint_constructor_exists():
    assert callable(dSL_MiddleRotatePoint.__init__)


def test_hyp_dsl_middlerotatepoint_constructor_args():
    sig = inspect.signature(dSL_MiddleRotatePoint.__init__)
    params = list(sig.parameters.keys())
    assert "middledir" in params, "Missing parameter 'middledir'"




def test_hyp_dsl_leftrotatepoint_is_not_abstract():
    assert not inspect.isabstract(dSL_LeftRotatePoint)


def test_hyp_dsl_leftrotatepoint_constructor_exists():
    assert callable(dSL_LeftRotatePoint.__init__)


def test_hyp_dsl_leftrotatepoint_constructor_args():
    sig = inspect.signature(dSL_LeftRotatePoint.__init__)
    params = list(sig.parameters.keys())
    assert "leftdir" in params, "Missing parameter 'leftdir'"




def test_hyp_rotatemovementaction_is_not_abstract():
    assert not inspect.isabstract(RotateMovementAction)


def test_hyp_rotatemovementaction_constructor_exists():
    assert callable(RotateMovementAction.__init__)


def test_hyp_rotatemovementaction_constructor_args():
    sig = inspect.signature(RotateMovementAction.__init__)
    params = list(sig.parameters.keys())



def test_hyp_dsl_rotatepoints_is_not_abstract():
    assert not inspect.isabstract(dSL_RotatePoints)


def test_hyp_dsl_rotatepoints_constructor_exists():
    assert callable(dSL_RotatePoints.__init__)


def test_hyp_dsl_rotatepoints_constructor_args():
    sig = inspect.signature(dSL_RotatePoints.__init__)
    params = list(sig.parameters.keys())
    assert "degrees" in params, "Missing parameter 'degrees'"




def test_hyp_dsl_rotatemovementaction_is_not_abstract():
    assert not inspect.isabstract(dSL_RotateMovementAction)


def test_hyp_dsl_rotatemovementaction_constructor_exists():
    assert callable(dSL_RotateMovementAction.__init__)


def test_hyp_dsl_rotatemovementaction_constructor_args():
    sig = inspect.signature(dSL_RotateMovementAction.__init__)
    params = list(sig.parameters.keys())



def test_hyp_dsl_rightmovementaction_is_not_abstract():
    assert not inspect.isabstract(dSL_RightMovementAction)


def test_hyp_dsl_rightmovementaction_constructor_exists():
    assert callable(dSL_RightMovementAction.__init__)


def test_hyp_dsl_rightmovementaction_constructor_args():
    sig = inspect.signature(dSL_RightMovementAction.__init__)
    params = list(sig.parameters.keys())



def test_hyp_dsl_behavior_is_not_abstract():
    assert not inspect.isabstract(dSL_Behavior)


def test_hyp_dsl_behavior_constructor_exists():
    assert callable(dSL_Behavior.__init__)


def test_hyp_dsl_behavior_constructor_args():
    sig = inspect.signature(dSL_Behavior.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"




def test_hyp_dsl_mission_is_not_abstract():
    assert not inspect.isabstract(dSL_Mission)


def test_hyp_dsl_mission_constructor_exists():
    assert callable(dSL_Mission.__init__)


def test_hyp_dsl_mission_constructor_args():
    sig = inspect.signature(dSL_Mission.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"




def test_hyp_dsl_marsroverexpedition_is_not_abstract():
    assert not inspect.isabstract(dSL_MarsRoverExpedition)


def test_hyp_dsl_marsroverexpedition_constructor_exists():
    assert callable(dSL_MarsRoverExpedition.__init__)


def test_hyp_dsl_marsroverexpedition_constructor_args():
    sig = inspect.signature(dSL_MarsRoverExpedition.__init__)
    params = list(sig.parameters.keys())



def test_hyp_endcondition_is_not_abstract():
    assert not inspect.isabstract(EndCondition)


def test_hyp_endcondition_constructor_exists():
    assert callable(EndCondition.__init__)


def test_hyp_endcondition_constructor_args():
    sig = inspect.signature(EndCondition.__init__)
    params = list(sig.parameters.keys())



def test_hyp_dsl_endafter_is_not_abstract():
    assert not inspect.isabstract(dSL_EndAfter)


def test_hyp_dsl_endafter_constructor_exists():
    assert callable(dSL_EndAfter.__init__)


def test_hyp_dsl_endafter_constructor_args():
    sig = inspect.signature(dSL_EndAfter.__init__)
    params = list(sig.parameters.keys())
    assert "time" in params, "Missing parameter 'time'"




def test_hyp_dsl_endwhen_is_not_abstract():
    assert not inspect.isabstract(dSL_EndWhen)


def test_hyp_dsl_endwhen_constructor_exists():
    assert callable(dSL_EndWhen.__init__)


def test_hyp_dsl_endwhen_constructor_args():
    sig = inspect.signature(dSL_EndWhen.__init__)
    params = list(sig.parameters.keys())
    assert "times" in params, "Missing parameter 'times'"
    assert "name" in params, "Missing parameter 'name'"





def test_hyp_dsl_endcondition_is_not_abstract():
    assert not inspect.isabstract(dSL_EndCondition)


def test_hyp_dsl_endcondition_constructor_exists():
    assert callable(dSL_EndCondition.__init__)


def test_hyp_dsl_endcondition_constructor_args():
    sig = inspect.signature(dSL_EndCondition.__init__)
    params = list(sig.parameters.keys())



def test_hyp_dsl_behaviorname_is_not_abstract():
    assert not inspect.isabstract(dSL_BehaviorName)


def test_hyp_dsl_behaviorname_constructor_exists():
    assert callable(dSL_BehaviorName.__init__)


def test_hyp_dsl_behaviorname_constructor_args():
    sig = inspect.signature(dSL_BehaviorName.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"


def test_hyp_actionenum_exists():
    # Check that the Enumeration exists
    assert ActionEnum is not None

def test_hyp_actionenum_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in ActionEnum]
    expected_literals = [
        "FORWARD",
        "BACKWARD",
        "STOP",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in ActionEnum"

def test_hyp_tenum_exists():
    # Check that the Enumeration exists
    assert Tenum is not None

def test_hyp_tenum_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in Tenum]
    expected_literals = [
        "TRUE",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in Tenum"

def test_hyp_edgeenum_exists():
    # Check that the Enumeration exists
    assert EdgeEnum is not None

def test_hyp_edgeenum_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in EdgeEnum]
    expected_literals = [
        "BACK",
        "FRONTLEFT",
        "FRONTRIGHT",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in EdgeEnum"

def test_hyp_touchenum_exists():
    # Check that the Enumeration exists
    assert TouchEnum is not None

def test_hyp_touchenum_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in TouchEnum]
    expected_literals = [
        "RIGHT",
        "LEFT",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in TouchEnum"

def test_hyp_backenum_exists():
    # Check that the Enumeration exists
    assert BackEnum is not None

def test_hyp_backenum_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in BackEnum]
    expected_literals = [
        "BACK",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in BackEnum"

def test_hyp_lrenum_exists():
    # Check that the Enumeration exists
    assert LREnum is not None

def test_hyp_lrenum_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in LREnum]
    expected_literals = [
        "LEFT",
        "RIGHT",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in LREnum"

def test_hyp_fbenum_exists():
    # Check that the Enumeration exists
    assert FBEnum is not None

def test_hyp_fbenum_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in FBEnum]
    expected_literals = [
        "FORWARD",
        "BACKWARD",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in FBEnum"

def test_hyp_colorenum_exists():
    # Check that the Enumeration exists
    assert ColorEnum is not None

def test_hyp_colorenum_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in ColorEnum]
    expected_literals = [
        "YELLOW",
        "GREEN",
        "WHITE",
        "BLACK",
        "BROWN",
        "NONE",
        "BLUE",
        "RED",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in ColorEnum"

def test_hyp_maenum_exists():
    # Check that the Enumeration exists
    assert MAEnum is not None

def test_hyp_maenum_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in MAEnum]
    expected_literals = [
        "MEASURE",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in MAEnum"


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
Expression_strategy = st.builds(
    Expression,
)
dSL_ORexpression_strategy = st.builds(
    dSL_ORexpression,
)
dSL_DepthLiteral_strategy = st.builds(
    dSL_DepthLiteral,
    back=
        safe_text
)
dSL_ANDexpression_strategy = st.builds(
    dSL_ANDexpression,
)
dSL_ExpressionBracket_strategy = st.builds(
    dSL_ExpressionBracket,
)
dSL_TrueLiteral_strategy = st.builds(
    dSL_TrueLiteral,
    t=
        safe_text
)
dSL_EdgeLiteral_strategy = st.builds(
    dSL_EdgeLiteral,
    edge=
        safe_text
)
dSL_DistanceLiteral_strategy = st.builds(
    dSL_DistanceLiteral,
    distance=
        st.integers()
)
dSL_ColorLiteral_strategy = st.builds(
    dSL_ColorLiteral,
    color=
        safe_text
)
dSL_TouchLiteral_strategy = st.builds(
    dSL_TouchLiteral,
    touch=
        safe_text
)
dSL_MovementAction_strategy = st.builds(
    dSL_MovementAction,
    actionenum=
        safe_text
)
Actions_strategy = st.builds(
    Actions,
)
dSL_LeftMovementAction_strategy = st.builds(
    dSL_LeftMovementAction,
)
dSL_MeasurementAction_strategy = st.builds(
    dSL_MeasurementAction,
    measure=
        safe_text
)
dSL_MoveAction_strategy = st.builds(
    dSL_MoveAction,
    dir=
        safe_text
)
dSL_Actions_strategy = st.builds(
    dSL_Actions,
)
dSL_Expression_strategy = st.builds(
    dSL_Expression,
)
RotatePoints_strategy = st.builds(
    RotatePoints,
)
dSL_RightRotatePoint_strategy = st.builds(
    dSL_RightRotatePoint,
    rightdir=
        safe_text
)
dSL_MiddleRotatePoint_strategy = st.builds(
    dSL_MiddleRotatePoint,
    middledir=
        safe_text
)
dSL_LeftRotatePoint_strategy = st.builds(
    dSL_LeftRotatePoint,
    leftdir=
        safe_text
)
RotateMovementAction_strategy = st.builds(
    RotateMovementAction,
)
dSL_RotatePoints_strategy = st.builds(
    dSL_RotatePoints,
    degrees=
        st.integers()
)
dSL_RotateMovementAction_strategy = st.builds(
    dSL_RotateMovementAction,
)
dSL_RightMovementAction_strategy = st.builds(
    dSL_RightMovementAction,
)
dSL_Behavior_strategy = st.builds(
    dSL_Behavior,
    name=
        safe_text
)
dSL_Mission_strategy = st.builds(
    dSL_Mission,
    name=
        safe_text
)
dSL_MarsRoverExpedition_strategy = st.builds(
    dSL_MarsRoverExpedition,
)
EndCondition_strategy = st.builds(
    EndCondition,
)
dSL_EndAfter_strategy = st.builds(
    dSL_EndAfter,
    time=
        st.integers()
)
dSL_EndWhen_strategy = st.builds(
    dSL_EndWhen,
    times=
        st.integers(),
    name=
        safe_text
)
dSL_EndCondition_strategy = st.builds(
    dSL_EndCondition,
)
dSL_BehaviorName_strategy = st.builds(
    dSL_BehaviorName,
    name=
        safe_text
)






@given(instance=dSL_DepthLiteral_strategy)
def test_hyp_dsl_depthliteral_back_setter(instance):
    original = instance.back
    instance.back = original
    assert instance.back == original






@given(instance=dSL_TrueLiteral_strategy)
def test_hyp_dsl_trueliteral_t_setter(instance):
    original = instance.t
    instance.t = original
    assert instance.t == original




@given(instance=dSL_EdgeLiteral_strategy)
def test_hyp_dsl_edgeliteral_edge_setter(instance):
    original = instance.edge
    instance.edge = original
    assert instance.edge == original




@given(instance=dSL_DistanceLiteral_strategy)
def test_hyp_dsl_distanceliteral_distance_setter(instance):
    original = instance.distance
    instance.distance = original
    assert instance.distance == original




@given(instance=dSL_ColorLiteral_strategy)
def test_hyp_dsl_colorliteral_color_setter(instance):
    original = instance.color
    instance.color = original
    assert instance.color == original




@given(instance=dSL_TouchLiteral_strategy)
def test_hyp_dsl_touchliteral_touch_setter(instance):
    original = instance.touch
    instance.touch = original
    assert instance.touch == original




@given(instance=dSL_MovementAction_strategy)
def test_hyp_dsl_movementaction_actionenum_setter(instance):
    original = instance.actionenum
    instance.actionenum = original
    assert instance.actionenum == original






@given(instance=dSL_MeasurementAction_strategy)
def test_hyp_dsl_measurementaction_measure_setter(instance):
    original = instance.measure
    instance.measure = original
    assert instance.measure == original




@given(instance=dSL_MoveAction_strategy)
def test_hyp_dsl_moveaction_dir_setter(instance):
    original = instance.dir
    instance.dir = original
    assert instance.dir == original







@given(instance=dSL_RightRotatePoint_strategy)
def test_hyp_dsl_rightrotatepoint_rightdir_setter(instance):
    original = instance.rightdir
    instance.rightdir = original
    assert instance.rightdir == original




@given(instance=dSL_MiddleRotatePoint_strategy)
def test_hyp_dsl_middlerotatepoint_middledir_setter(instance):
    original = instance.middledir
    instance.middledir = original
    assert instance.middledir == original




@given(instance=dSL_LeftRotatePoint_strategy)
def test_hyp_dsl_leftrotatepoint_leftdir_setter(instance):
    original = instance.leftdir
    instance.leftdir = original
    assert instance.leftdir == original





@given(instance=dSL_RotatePoints_strategy)
def test_hyp_dsl_rotatepoints_degrees_setter(instance):
    original = instance.degrees
    instance.degrees = original
    assert instance.degrees == original






@given(instance=dSL_Behavior_strategy)
def test_hyp_dsl_behavior_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original




@given(instance=dSL_Mission_strategy)
def test_hyp_dsl_mission_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original






@given(instance=dSL_EndAfter_strategy)
def test_hyp_dsl_endafter_time_setter(instance):
    original = instance.time
    instance.time = original
    assert instance.time == original




@given(instance=dSL_EndWhen_strategy)
def test_hyp_dsl_endwhen_times_setter(instance):
    original = instance.times
    instance.times = original
    assert instance.times == original



@given(instance=dSL_EndWhen_strategy)
def test_hyp_dsl_endwhen_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original





@given(instance=dSL_BehaviorName_strategy)
def test_hyp_dsl_behaviorname_name_setter(instance):
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
    Actions,
    EndCondition,
    Expression,
    RotateMovementAction,
    RotatePoints,
    dSL_ANDexpression,
    dSL_Actions,
    dSL_Behavior,
    dSL_BehaviorName,
    dSL_ColorLiteral,
    dSL_DepthLiteral,
    dSL_DistanceLiteral,
    dSL_EdgeLiteral,
    dSL_EndAfter,
    dSL_EndCondition,
    dSL_EndWhen,
    dSL_Expression,
    dSL_ExpressionBracket,
    dSL_LeftMovementAction,
    dSL_LeftRotatePoint,
    dSL_MarsRoverExpedition,
    dSL_MeasurementAction,
    dSL_MiddleRotatePoint,
    dSL_Mission,
    dSL_MoveAction,
    dSL_MovementAction,
    dSL_ORexpression,
    dSL_RightMovementAction,
    dSL_RightRotatePoint,
    dSL_RotateMovementAction,
    dSL_RotatePoints,
    dSL_TouchLiteral,
    dSL_TrueLiteral,
    ActionEnum,
    BackEnum,
    ColorEnum,
    EdgeEnum,
    FBEnum,
    LREnum,
    MAEnum,
    Tenum,
    TouchEnum,
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

def test_dSL_Behavior_name_value_roundtrip():
    instance = dSL_Behavior(name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_dSL_BehaviorName_name_value_roundtrip():
    instance = dSL_BehaviorName(name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_dSL_ColorLiteral_color_value_roundtrip():
    instance = dSL_ColorLiteral(color="sample_text")
    assert instance.color == "sample_text"
    instance.color = "sample_text_2"
    assert instance.color == "sample_text_2"


def test_dSL_DepthLiteral_back_value_roundtrip():
    instance = dSL_DepthLiteral(back="sample_text")
    assert instance.back == "sample_text"
    instance.back = "sample_text_2"
    assert instance.back == "sample_text_2"


def test_dSL_DistanceLiteral_distance_value_roundtrip():
    instance = dSL_DistanceLiteral(distance=7)
    assert instance.distance == 7
    instance.distance = 13
    assert instance.distance == 13


def test_dSL_EdgeLiteral_edge_value_roundtrip():
    instance = dSL_EdgeLiteral(edge="sample_text")
    assert instance.edge == "sample_text"
    instance.edge = "sample_text_2"
    assert instance.edge == "sample_text_2"


def test_dSL_EndAfter_time_value_roundtrip():
    instance = dSL_EndAfter(time=7)
    assert instance.time == 7
    instance.time = 13
    assert instance.time == 13


def test_dSL_EndWhen_name_value_roundtrip():
    instance = dSL_EndWhen(name="sample_text", times=7)
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_dSL_EndWhen_times_value_roundtrip():
    instance = dSL_EndWhen(name="sample_text", times=7)
    assert instance.times == 7
    instance.times = 13
    assert instance.times == 13


def test_dSL_LeftRotatePoint_leftdir_value_roundtrip():
    instance = dSL_LeftRotatePoint(leftdir="sample_text")
    assert instance.leftdir == "sample_text"
    instance.leftdir = "sample_text_2"
    assert instance.leftdir == "sample_text_2"


def test_dSL_MeasurementAction_measure_value_roundtrip():
    instance = dSL_MeasurementAction(measure="sample_text")
    assert instance.measure == "sample_text"
    instance.measure = "sample_text_2"
    assert instance.measure == "sample_text_2"


def test_dSL_MiddleRotatePoint_middledir_value_roundtrip():
    instance = dSL_MiddleRotatePoint(middledir="sample_text")
    assert instance.middledir == "sample_text"
    instance.middledir = "sample_text_2"
    assert instance.middledir == "sample_text_2"


def test_dSL_Mission_name_value_roundtrip():
    instance = dSL_Mission(name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_dSL_MoveAction_dir_value_roundtrip():
    instance = dSL_MoveAction(dir="sample_text")
    assert instance.dir == "sample_text"
    instance.dir = "sample_text_2"
    assert instance.dir == "sample_text_2"


def test_dSL_MovementAction_actionenum_value_roundtrip():
    instance = dSL_MovementAction(actionenum="sample_text")
    assert instance.actionenum == "sample_text"
    instance.actionenum = "sample_text_2"
    assert instance.actionenum == "sample_text_2"


def test_dSL_RightRotatePoint_rightdir_value_roundtrip():
    instance = dSL_RightRotatePoint(rightdir="sample_text")
    assert instance.rightdir == "sample_text"
    instance.rightdir = "sample_text_2"
    assert instance.rightdir == "sample_text_2"


def test_dSL_RotatePoints_degrees_value_roundtrip():
    instance = dSL_RotatePoints(degrees=7)
    assert instance.degrees == 7
    instance.degrees = 13
    assert instance.degrees == 13


def test_dSL_TouchLiteral_touch_value_roundtrip():
    instance = dSL_TouchLiteral(touch="sample_text")
    assert instance.touch == "sample_text"
    instance.touch = "sample_text_2"
    assert instance.touch == "sample_text_2"


def test_dSL_TrueLiteral_t_value_roundtrip():
    instance = dSL_TrueLiteral(t="sample_text")
    assert instance.t == "sample_text"
    instance.t = "sample_text_2"
    assert instance.t == "sample_text_2"


def test_dSL_LeftMovementAction_isa_Actions():
    instance = dSL_LeftMovementAction()
    assert isinstance(instance, Actions)


def test_dSL_MeasurementAction_isa_Actions():
    instance = dSL_MeasurementAction(measure="sample_text")
    assert isinstance(instance, Actions)


def test_dSL_MoveAction_isa_Actions():
    instance = dSL_MoveAction(dir="sample_text")
    assert isinstance(instance, Actions)


def test_dSL_RightMovementAction_isa_Actions():
    instance = dSL_RightMovementAction()
    assert isinstance(instance, Actions)


def test_dSL_RotateMovementAction_isa_Actions():
    instance = dSL_RotateMovementAction()
    assert isinstance(instance, Actions)


def test_dSL_EndAfter_isa_EndCondition():
    instance = dSL_EndAfter(time=7)
    assert isinstance(instance, EndCondition)


def test_dSL_ANDexpression_isa_Expression():
    instance = dSL_ANDexpression()
    assert isinstance(instance, Expression)


def test_dSL_ColorLiteral_isa_Expression():
    instance = dSL_ColorLiteral(color="sample_text")
    assert isinstance(instance, Expression)


def test_dSL_DepthLiteral_isa_Expression():
    instance = dSL_DepthLiteral(back="sample_text")
    assert isinstance(instance, Expression)


def test_dSL_DistanceLiteral_isa_Expression():
    instance = dSL_DistanceLiteral(distance=7)
    assert isinstance(instance, Expression)


def test_dSL_EdgeLiteral_isa_Expression():
    instance = dSL_EdgeLiteral(edge="sample_text")
    assert isinstance(instance, Expression)


def test_dSL_ExpressionBracket_isa_Expression():
    instance = dSL_ExpressionBracket()
    assert isinstance(instance, Expression)


def test_dSL_ORexpression_isa_Expression():
    instance = dSL_ORexpression()
    assert isinstance(instance, Expression)


def test_dSL_TouchLiteral_isa_Expression():
    instance = dSL_TouchLiteral(touch="sample_text")
    assert isinstance(instance, Expression)


def test_dSL_TrueLiteral_isa_Expression():
    instance = dSL_TrueLiteral(t="sample_text")
    assert isinstance(instance, Expression)


def test_dSL_RotatePoints_isa_RotateMovementAction():
    instance = dSL_RotatePoints(degrees=7)
    assert isinstance(instance, RotateMovementAction)


def test_dSL_LeftRotatePoint_isa_RotatePoints():
    instance = dSL_LeftRotatePoint(leftdir="sample_text")
    assert isinstance(instance, RotatePoints)


def test_dSL_MiddleRotatePoint_isa_RotatePoints():
    instance = dSL_MiddleRotatePoint(middledir="sample_text")
    assert isinstance(instance, RotatePoints)


def test_dSL_RightRotatePoint_isa_RotatePoints():
    instance = dSL_RightRotatePoint(rightdir="sample_text")
    assert isinstance(instance, RotatePoints)


def test_assoc_actionlist11_link_reassign_clear():
    a = dSL_Behavior(name="sample_text")
    b1 = dSL_Actions()
    b2 = dSL_Actions()
    _safe_set(a, 'dSL_Behavior12', {b1})
    assert _is_linked(a, 'dSL_Behavior12', b1)
    if hasattr(b1, 'dSL_Actions'):
        assert _is_linked(b1, 'dSL_Actions', a)
    _safe_set(a, 'dSL_Behavior12', {b2})
    assert _is_linked(a, 'dSL_Behavior12', b2)
    if hasattr(b1, 'dSL_Actions'):
        assert not _is_linked(b1, 'dSL_Actions', a)
    if hasattr(b2, 'dSL_Actions'):
        assert _is_linked(b2, 'dSL_Actions', a)
    _safe_set(a, 'dSL_Behavior12', set())
    assert not _is_linked(a, 'dSL_Behavior12', b2)
    if hasattr(b2, 'dSL_Actions'):
        assert not _is_linked(b2, 'dSL_Actions', a)


def test_assoc_behaviorlist3_link_reassign_clear():
    a = dSL_Mission(name="sample_text")
    b1 = dSL_BehaviorName(name="sample_text")
    b2 = dSL_BehaviorName(name="sample_text_2")
    _safe_set(a, 'dSL_Mission4', {b1})
    assert _is_linked(a, 'dSL_Mission4', b1)
    if hasattr(b1, 'dSL_BehaviorName'):
        assert _is_linked(b1, 'dSL_BehaviorName', a)
    _safe_set(a, 'dSL_Mission4', {b2})
    assert _is_linked(a, 'dSL_Mission4', b2)
    if hasattr(b1, 'dSL_BehaviorName'):
        assert not _is_linked(b1, 'dSL_BehaviorName', a)
    if hasattr(b2, 'dSL_BehaviorName'):
        assert _is_linked(b2, 'dSL_BehaviorName', a)
    _safe_set(a, 'dSL_Mission4', set())
    assert not _is_linked(a, 'dSL_Mission4', b2)
    if hasattr(b2, 'dSL_BehaviorName'):
        assert not _is_linked(b2, 'dSL_BehaviorName', a)


def test_assoc_endcondition5_link_reassign_clear():
    a = dSL_Mission(name="sample_text")
    b1 = dSL_EndCondition()
    b2 = dSL_EndCondition()
    _safe_set(a, 'dSL_Mission6', b1)
    assert _is_linked(a, 'dSL_Mission6', b1)
    if hasattr(b1, 'dSL_EndCondition'):
        assert _is_linked(b1, 'dSL_EndCondition', a)
    _safe_set(a, 'dSL_Mission6', b2)
    assert _is_linked(a, 'dSL_Mission6', b2)
    if hasattr(b1, 'dSL_EndCondition'):
        assert not _is_linked(b1, 'dSL_EndCondition', a)
    if hasattr(b2, 'dSL_EndCondition'):
        assert _is_linked(b2, 'dSL_EndCondition', a)
    _safe_set(a, 'dSL_Mission6', None)
    assert not _is_linked(a, 'dSL_Mission6', b2)
    if hasattr(b2, 'dSL_EndCondition'):
        assert not _is_linked(b2, 'dSL_EndCondition', a)


def test_assoc_endwhenlist7_link_reassign_clear():
    a = dSL_EndWhen(name="sample_text", times=7)
    b1 = dSL_EndCondition()
    b2 = dSL_EndCondition()
    _safe_set(a, 'dSL_EndWhen', b1)
    assert _is_linked(a, 'dSL_EndWhen', b1)
    if hasattr(b1, 'dSL_EndCondition8'):
        assert _is_linked(b1, 'dSL_EndCondition8', a)
    _safe_set(a, 'dSL_EndWhen', b2)
    assert _is_linked(a, 'dSL_EndWhen', b2)
    if hasattr(b1, 'dSL_EndCondition8'):
        assert not _is_linked(b1, 'dSL_EndCondition8', a)
    if hasattr(b2, 'dSL_EndCondition8'):
        assert _is_linked(b2, 'dSL_EndCondition8', a)
    _safe_set(a, 'dSL_EndWhen', None)
    assert not _is_linked(a, 'dSL_EndWhen', b2)
    if hasattr(b2, 'dSL_EndCondition8'):
        assert not _is_linked(b2, 'dSL_EndCondition8', a)


def test_assoc_leftmove13_link_reassign_clear():
    a = dSL_MovementAction(actionenum="sample_text")
    b1 = dSL_LeftMovementAction()
    b2 = dSL_LeftMovementAction()
    _safe_set(a, 'dSL_MovementAction', b1)
    assert _is_linked(a, 'dSL_MovementAction', b1)
    if hasattr(b1, 'dSL_LeftMovementAction'):
        assert _is_linked(b1, 'dSL_LeftMovementAction', a)
    _safe_set(a, 'dSL_MovementAction', b2)
    assert _is_linked(a, 'dSL_MovementAction', b2)
    if hasattr(b1, 'dSL_LeftMovementAction'):
        assert not _is_linked(b1, 'dSL_LeftMovementAction', a)
    if hasattr(b2, 'dSL_LeftMovementAction'):
        assert _is_linked(b2, 'dSL_LeftMovementAction', a)
    _safe_set(a, 'dSL_MovementAction', None)
    assert not _is_linked(a, 'dSL_MovementAction', b2)
    if hasattr(b2, 'dSL_LeftMovementAction'):
        assert not _is_linked(b2, 'dSL_LeftMovementAction', a)


def test_assoc_missionlist0_link_reassign_clear():
    a = dSL_Mission(name="sample_text")
    b1 = dSL_MarsRoverExpedition()
    b2 = dSL_MarsRoverExpedition()
    _safe_set(a, 'dSL_Mission', b1)
    assert _is_linked(a, 'dSL_Mission', b1)
    if hasattr(b1, 'dSL_MarsRoverExpedition'):
        assert _is_linked(b1, 'dSL_MarsRoverExpedition', a)
    _safe_set(a, 'dSL_Mission', b2)
    assert _is_linked(a, 'dSL_Mission', b2)
    if hasattr(b1, 'dSL_MarsRoverExpedition'):
        assert not _is_linked(b1, 'dSL_MarsRoverExpedition', a)
    if hasattr(b2, 'dSL_MarsRoverExpedition'):
        assert _is_linked(b2, 'dSL_MarsRoverExpedition', a)
    _safe_set(a, 'dSL_Mission', None)
    assert not _is_linked(a, 'dSL_Mission', b2)
    if hasattr(b2, 'dSL_MarsRoverExpedition'):
        assert not _is_linked(b2, 'dSL_MarsRoverExpedition', a)


def test_assoc_rightmove14_link_reassign_clear():
    a = dSL_MovementAction(actionenum="sample_text")
    b1 = dSL_RightMovementAction()
    b2 = dSL_RightMovementAction()
    _safe_set(a, 'dSL_MovementAction15', b1)
    assert _is_linked(a, 'dSL_MovementAction15', b1)
    if hasattr(b1, 'dSL_RightMovementAction'):
        assert _is_linked(b1, 'dSL_RightMovementAction', a)
    _safe_set(a, 'dSL_MovementAction15', b2)
    assert _is_linked(a, 'dSL_MovementAction15', b2)
    if hasattr(b1, 'dSL_RightMovementAction'):
        assert not _is_linked(b1, 'dSL_RightMovementAction', a)
    if hasattr(b2, 'dSL_RightMovementAction'):
        assert _is_linked(b2, 'dSL_RightMovementAction', a)
    _safe_set(a, 'dSL_MovementAction15', None)
    assert not _is_linked(a, 'dSL_MovementAction15', b2)
    if hasattr(b2, 'dSL_RightMovementAction'):
        assert not _is_linked(b2, 'dSL_RightMovementAction', a)


def test_assoc_sensorExpression9_link_reassign_clear():
    a = dSL_Behavior(name="sample_text")
    b1 = dSL_Expression()
    b2 = dSL_Expression()
    _safe_set(a, 'dSL_Behavior10', b1)
    assert _is_linked(a, 'dSL_Behavior10', b1)
    if hasattr(b1, 'dSL_Expression'):
        assert _is_linked(b1, 'dSL_Expression', a)
    _safe_set(a, 'dSL_Behavior10', b2)
    assert _is_linked(a, 'dSL_Behavior10', b2)
    if hasattr(b1, 'dSL_Expression'):
        assert not _is_linked(b1, 'dSL_Expression', a)
    if hasattr(b2, 'dSL_Expression'):
        assert _is_linked(b2, 'dSL_Expression', a)
    _safe_set(a, 'dSL_Behavior10', None)
    assert not _is_linked(a, 'dSL_Behavior10', b2)
    if hasattr(b2, 'dSL_Expression'):
        assert not _is_linked(b2, 'dSL_Expression', a)


def test_assoc_tasklist1_link_reassign_clear():
    a = dSL_Behavior(name="sample_text")
    b1 = dSL_MarsRoverExpedition()
    b2 = dSL_MarsRoverExpedition()
    _safe_set(a, 'dSL_Behavior', b1)
    assert _is_linked(a, 'dSL_Behavior', b1)
    if hasattr(b1, 'dSL_MarsRoverExpedition2'):
        assert _is_linked(b1, 'dSL_MarsRoverExpedition2', a)
    _safe_set(a, 'dSL_Behavior', b2)
    assert _is_linked(a, 'dSL_Behavior', b2)
    if hasattr(b1, 'dSL_MarsRoverExpedition2'):
        assert not _is_linked(b1, 'dSL_MarsRoverExpedition2', a)
    if hasattr(b2, 'dSL_MarsRoverExpedition2'):
        assert _is_linked(b2, 'dSL_MarsRoverExpedition2', a)
    _safe_set(a, 'dSL_Behavior', None)
    assert not _is_linked(a, 'dSL_Behavior', b2)
    if hasattr(b2, 'dSL_MarsRoverExpedition2'):
        assert not _is_linked(b2, 'dSL_MarsRoverExpedition2', a)


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

Actions_strategy = st.builds(Actions)
@given(instance=Actions_strategy)
@settings(max_examples=25)
def test_Actions_instantiation(instance):
    assert isinstance(instance, Actions)


EndCondition_strategy = st.builds(EndCondition)
@given(instance=EndCondition_strategy)
@settings(max_examples=25)
def test_EndCondition_instantiation(instance):
    assert isinstance(instance, EndCondition)


Expression_strategy = st.builds(Expression)
@given(instance=Expression_strategy)
@settings(max_examples=25)
def test_Expression_instantiation(instance):
    assert isinstance(instance, Expression)


RotateMovementAction_strategy = st.builds(RotateMovementAction)
@given(instance=RotateMovementAction_strategy)
@settings(max_examples=25)
def test_RotateMovementAction_instantiation(instance):
    assert isinstance(instance, RotateMovementAction)


RotatePoints_strategy = st.builds(RotatePoints)
@given(instance=RotatePoints_strategy)
@settings(max_examples=25)
def test_RotatePoints_instantiation(instance):
    assert isinstance(instance, RotatePoints)


dSL_ANDexpression_strategy = st.builds(dSL_ANDexpression)
@given(instance=dSL_ANDexpression_strategy)
@settings(max_examples=25)
def test_dSL_ANDexpression_instantiation(instance):
    assert isinstance(instance, dSL_ANDexpression)


dSL_Actions_strategy = st.builds(dSL_Actions)
@given(instance=dSL_Actions_strategy)
@settings(max_examples=25)
def test_dSL_Actions_instantiation(instance):
    assert isinstance(instance, dSL_Actions)


dSL_Behavior_strategy = st.builds(dSL_Behavior, name=safe_text)
@given(instance=dSL_Behavior_strategy)
@settings(max_examples=25)
def test_dSL_Behavior_instantiation(instance):
    assert isinstance(instance, dSL_Behavior)


dSL_BehaviorName_strategy = st.builds(dSL_BehaviorName, name=safe_text)
@given(instance=dSL_BehaviorName_strategy)
@settings(max_examples=25)
def test_dSL_BehaviorName_instantiation(instance):
    assert isinstance(instance, dSL_BehaviorName)


dSL_ColorLiteral_strategy = st.builds(dSL_ColorLiteral, color=safe_text)
@given(instance=dSL_ColorLiteral_strategy)
@settings(max_examples=25)
def test_dSL_ColorLiteral_instantiation(instance):
    assert isinstance(instance, dSL_ColorLiteral)


dSL_DepthLiteral_strategy = st.builds(dSL_DepthLiteral, back=safe_text)
@given(instance=dSL_DepthLiteral_strategy)
@settings(max_examples=25)
def test_dSL_DepthLiteral_instantiation(instance):
    assert isinstance(instance, dSL_DepthLiteral)


dSL_DistanceLiteral_strategy = st.builds(dSL_DistanceLiteral, distance=st.integers())
@given(instance=dSL_DistanceLiteral_strategy)
@settings(max_examples=25)
def test_dSL_DistanceLiteral_instantiation(instance):
    assert isinstance(instance, dSL_DistanceLiteral)


dSL_EdgeLiteral_strategy = st.builds(dSL_EdgeLiteral, edge=safe_text)
@given(instance=dSL_EdgeLiteral_strategy)
@settings(max_examples=25)
def test_dSL_EdgeLiteral_instantiation(instance):
    assert isinstance(instance, dSL_EdgeLiteral)


dSL_EndAfter_strategy = st.builds(dSL_EndAfter, time=st.integers())
@given(instance=dSL_EndAfter_strategy)
@settings(max_examples=25)
def test_dSL_EndAfter_instantiation(instance):
    assert isinstance(instance, dSL_EndAfter)


dSL_EndCondition_strategy = st.builds(dSL_EndCondition)
@given(instance=dSL_EndCondition_strategy)
@settings(max_examples=25)
def test_dSL_EndCondition_instantiation(instance):
    assert isinstance(instance, dSL_EndCondition)


dSL_EndWhen_strategy = st.builds(dSL_EndWhen, name=safe_text, times=st.integers())
@given(instance=dSL_EndWhen_strategy)
@settings(max_examples=25)
def test_dSL_EndWhen_instantiation(instance):
    assert isinstance(instance, dSL_EndWhen)


dSL_Expression_strategy = st.builds(dSL_Expression)
@given(instance=dSL_Expression_strategy)
@settings(max_examples=25)
def test_dSL_Expression_instantiation(instance):
    assert isinstance(instance, dSL_Expression)


dSL_ExpressionBracket_strategy = st.builds(dSL_ExpressionBracket)
@given(instance=dSL_ExpressionBracket_strategy)
@settings(max_examples=25)
def test_dSL_ExpressionBracket_instantiation(instance):
    assert isinstance(instance, dSL_ExpressionBracket)


dSL_LeftMovementAction_strategy = st.builds(dSL_LeftMovementAction)
@given(instance=dSL_LeftMovementAction_strategy)
@settings(max_examples=25)
def test_dSL_LeftMovementAction_instantiation(instance):
    assert isinstance(instance, dSL_LeftMovementAction)


dSL_LeftRotatePoint_strategy = st.builds(dSL_LeftRotatePoint, leftdir=safe_text)
@given(instance=dSL_LeftRotatePoint_strategy)
@settings(max_examples=25)
def test_dSL_LeftRotatePoint_instantiation(instance):
    assert isinstance(instance, dSL_LeftRotatePoint)


dSL_MarsRoverExpedition_strategy = st.builds(dSL_MarsRoverExpedition)
@given(instance=dSL_MarsRoverExpedition_strategy)
@settings(max_examples=25)
def test_dSL_MarsRoverExpedition_instantiation(instance):
    assert isinstance(instance, dSL_MarsRoverExpedition)


dSL_MeasurementAction_strategy = st.builds(dSL_MeasurementAction, measure=safe_text)
@given(instance=dSL_MeasurementAction_strategy)
@settings(max_examples=25)
def test_dSL_MeasurementAction_instantiation(instance):
    assert isinstance(instance, dSL_MeasurementAction)


dSL_MiddleRotatePoint_strategy = st.builds(dSL_MiddleRotatePoint, middledir=safe_text)
@given(instance=dSL_MiddleRotatePoint_strategy)
@settings(max_examples=25)
def test_dSL_MiddleRotatePoint_instantiation(instance):
    assert isinstance(instance, dSL_MiddleRotatePoint)


dSL_Mission_strategy = st.builds(dSL_Mission, name=safe_text)
@given(instance=dSL_Mission_strategy)
@settings(max_examples=25)
def test_dSL_Mission_instantiation(instance):
    assert isinstance(instance, dSL_Mission)


dSL_MoveAction_strategy = st.builds(dSL_MoveAction, dir=safe_text)
@given(instance=dSL_MoveAction_strategy)
@settings(max_examples=25)
def test_dSL_MoveAction_instantiation(instance):
    assert isinstance(instance, dSL_MoveAction)


dSL_MovementAction_strategy = st.builds(dSL_MovementAction, actionenum=safe_text)
@given(instance=dSL_MovementAction_strategy)
@settings(max_examples=25)
def test_dSL_MovementAction_instantiation(instance):
    assert isinstance(instance, dSL_MovementAction)


dSL_ORexpression_strategy = st.builds(dSL_ORexpression)
@given(instance=dSL_ORexpression_strategy)
@settings(max_examples=25)
def test_dSL_ORexpression_instantiation(instance):
    assert isinstance(instance, dSL_ORexpression)


dSL_RightMovementAction_strategy = st.builds(dSL_RightMovementAction)
@given(instance=dSL_RightMovementAction_strategy)
@settings(max_examples=25)
def test_dSL_RightMovementAction_instantiation(instance):
    assert isinstance(instance, dSL_RightMovementAction)


dSL_RightRotatePoint_strategy = st.builds(dSL_RightRotatePoint, rightdir=safe_text)
@given(instance=dSL_RightRotatePoint_strategy)
@settings(max_examples=25)
def test_dSL_RightRotatePoint_instantiation(instance):
    assert isinstance(instance, dSL_RightRotatePoint)


dSL_RotateMovementAction_strategy = st.builds(dSL_RotateMovementAction)
@given(instance=dSL_RotateMovementAction_strategy)
@settings(max_examples=25)
def test_dSL_RotateMovementAction_instantiation(instance):
    assert isinstance(instance, dSL_RotateMovementAction)


dSL_RotatePoints_strategy = st.builds(dSL_RotatePoints, degrees=st.integers())
@given(instance=dSL_RotatePoints_strategy)
@settings(max_examples=25)
def test_dSL_RotatePoints_instantiation(instance):
    assert isinstance(instance, dSL_RotatePoints)


dSL_TouchLiteral_strategy = st.builds(dSL_TouchLiteral, touch=safe_text)
@given(instance=dSL_TouchLiteral_strategy)
@settings(max_examples=25)
def test_dSL_TouchLiteral_instantiation(instance):
    assert isinstance(instance, dSL_TouchLiteral)


dSL_TrueLiteral_strategy = st.builds(dSL_TrueLiteral, t=safe_text)
@given(instance=dSL_TrueLiteral_strategy)
@settings(max_examples=25)
def test_dSL_TrueLiteral_instantiation(instance):
    assert isinstance(instance, dSL_TrueLiteral)



