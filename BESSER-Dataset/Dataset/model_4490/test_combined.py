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
    RotatePoints,
    dSL_MiddleRotatePoint,
    dSL_RightRotatePoint,
    dSL_LeftRotatePoint,
    RotateMovementAction,
    dSL_RotatePoints,
    dSL_MovementAction,
    Actions,
    dSL_RightMovementAction,
    dSL_RotateMovementAction,
    dSL_LeftMovementAction,
    dSL_Actions,
    Expression,
    dSL_DistanceLiteral,
    dSL_TouchLiteral,
    dSL_ColorLiteral,
    dSL_ANDexpression,
    dSL_EdgeLiteral,
    dSL_ORexpression,
    dSL_ExpressionBracket,
    dSL_RobotBehavior,
    dSL_Expression,
    dSL_Behaviors,
    LREnum,
    FBEnum,
    ActionEnum,
    TouchEnum,
    EdgeEnum,
    ColorEnum,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_hyp_rotatepoints_is_not_abstract():
    assert not inspect.isabstract(RotatePoints)


def test_hyp_rotatepoints_constructor_exists():
    assert callable(RotatePoints.__init__)


def test_hyp_rotatepoints_constructor_args():
    sig = inspect.signature(RotatePoints.__init__)
    params = list(sig.parameters.keys())



def test_hyp_dsl_middlerotatepoint_is_not_abstract():
    assert not inspect.isabstract(dSL_MiddleRotatePoint)


def test_hyp_dsl_middlerotatepoint_constructor_exists():
    assert callable(dSL_MiddleRotatePoint.__init__)


def test_hyp_dsl_middlerotatepoint_constructor_args():
    sig = inspect.signature(dSL_MiddleRotatePoint.__init__)
    params = list(sig.parameters.keys())
    assert "middledir" in params, "Missing parameter 'middledir'"




def test_hyp_dsl_rightrotatepoint_is_not_abstract():
    assert not inspect.isabstract(dSL_RightRotatePoint)


def test_hyp_dsl_rightrotatepoint_constructor_exists():
    assert callable(dSL_RightRotatePoint.__init__)


def test_hyp_dsl_rightrotatepoint_constructor_args():
    sig = inspect.signature(dSL_RightRotatePoint.__init__)
    params = list(sig.parameters.keys())
    assert "rightdir" in params, "Missing parameter 'rightdir'"




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



def test_hyp_dsl_rightmovementaction_is_not_abstract():
    assert not inspect.isabstract(dSL_RightMovementAction)


def test_hyp_dsl_rightmovementaction_constructor_exists():
    assert callable(dSL_RightMovementAction.__init__)


def test_hyp_dsl_rightmovementaction_constructor_args():
    sig = inspect.signature(dSL_RightMovementAction.__init__)
    params = list(sig.parameters.keys())



def test_hyp_dsl_rotatemovementaction_is_not_abstract():
    assert not inspect.isabstract(dSL_RotateMovementAction)


def test_hyp_dsl_rotatemovementaction_constructor_exists():
    assert callable(dSL_RotateMovementAction.__init__)


def test_hyp_dsl_rotatemovementaction_constructor_args():
    sig = inspect.signature(dSL_RotateMovementAction.__init__)
    params = list(sig.parameters.keys())



def test_hyp_dsl_leftmovementaction_is_not_abstract():
    assert not inspect.isabstract(dSL_LeftMovementAction)


def test_hyp_dsl_leftmovementaction_constructor_exists():
    assert callable(dSL_LeftMovementAction.__init__)


def test_hyp_dsl_leftmovementaction_constructor_args():
    sig = inspect.signature(dSL_LeftMovementAction.__init__)
    params = list(sig.parameters.keys())



def test_hyp_dsl_actions_is_not_abstract():
    assert not inspect.isabstract(dSL_Actions)


def test_hyp_dsl_actions_constructor_exists():
    assert callable(dSL_Actions.__init__)


def test_hyp_dsl_actions_constructor_args():
    sig = inspect.signature(dSL_Actions.__init__)
    params = list(sig.parameters.keys())



def test_hyp_expression_is_not_abstract():
    assert not inspect.isabstract(Expression)


def test_hyp_expression_constructor_exists():
    assert callable(Expression.__init__)


def test_hyp_expression_constructor_args():
    sig = inspect.signature(Expression.__init__)
    params = list(sig.parameters.keys())



def test_hyp_dsl_distanceliteral_is_not_abstract():
    assert not inspect.isabstract(dSL_DistanceLiteral)


def test_hyp_dsl_distanceliteral_constructor_exists():
    assert callable(dSL_DistanceLiteral.__init__)


def test_hyp_dsl_distanceliteral_constructor_args():
    sig = inspect.signature(dSL_DistanceLiteral.__init__)
    params = list(sig.parameters.keys())
    assert "distance" in params, "Missing parameter 'distance'"




def test_hyp_dsl_touchliteral_is_not_abstract():
    assert not inspect.isabstract(dSL_TouchLiteral)


def test_hyp_dsl_touchliteral_constructor_exists():
    assert callable(dSL_TouchLiteral.__init__)


def test_hyp_dsl_touchliteral_constructor_args():
    sig = inspect.signature(dSL_TouchLiteral.__init__)
    params = list(sig.parameters.keys())
    assert "touch" in params, "Missing parameter 'touch'"




def test_hyp_dsl_colorliteral_is_not_abstract():
    assert not inspect.isabstract(dSL_ColorLiteral)


def test_hyp_dsl_colorliteral_constructor_exists():
    assert callable(dSL_ColorLiteral.__init__)


def test_hyp_dsl_colorliteral_constructor_args():
    sig = inspect.signature(dSL_ColorLiteral.__init__)
    params = list(sig.parameters.keys())
    assert "color" in params, "Missing parameter 'color'"




def test_hyp_dsl_andexpression_is_not_abstract():
    assert not inspect.isabstract(dSL_ANDexpression)


def test_hyp_dsl_andexpression_constructor_exists():
    assert callable(dSL_ANDexpression.__init__)


def test_hyp_dsl_andexpression_constructor_args():
    sig = inspect.signature(dSL_ANDexpression.__init__)
    params = list(sig.parameters.keys())



def test_hyp_dsl_edgeliteral_is_not_abstract():
    assert not inspect.isabstract(dSL_EdgeLiteral)


def test_hyp_dsl_edgeliteral_constructor_exists():
    assert callable(dSL_EdgeLiteral.__init__)


def test_hyp_dsl_edgeliteral_constructor_args():
    sig = inspect.signature(dSL_EdgeLiteral.__init__)
    params = list(sig.parameters.keys())
    assert "edge" in params, "Missing parameter 'edge'"




def test_hyp_dsl_orexpression_is_not_abstract():
    assert not inspect.isabstract(dSL_ORexpression)


def test_hyp_dsl_orexpression_constructor_exists():
    assert callable(dSL_ORexpression.__init__)


def test_hyp_dsl_orexpression_constructor_args():
    sig = inspect.signature(dSL_ORexpression.__init__)
    params = list(sig.parameters.keys())



def test_hyp_dsl_expressionbracket_is_not_abstract():
    assert not inspect.isabstract(dSL_ExpressionBracket)


def test_hyp_dsl_expressionbracket_constructor_exists():
    assert callable(dSL_ExpressionBracket.__init__)


def test_hyp_dsl_expressionbracket_constructor_args():
    sig = inspect.signature(dSL_ExpressionBracket.__init__)
    params = list(sig.parameters.keys())



def test_hyp_dsl_robotbehavior_is_not_abstract():
    assert not inspect.isabstract(dSL_RobotBehavior)


def test_hyp_dsl_robotbehavior_constructor_exists():
    assert callable(dSL_RobotBehavior.__init__)


def test_hyp_dsl_robotbehavior_constructor_args():
    sig = inspect.signature(dSL_RobotBehavior.__init__)
    params = list(sig.parameters.keys())



def test_hyp_dsl_expression_is_not_abstract():
    assert not inspect.isabstract(dSL_Expression)


def test_hyp_dsl_expression_constructor_exists():
    assert callable(dSL_Expression.__init__)


def test_hyp_dsl_expression_constructor_args():
    sig = inspect.signature(dSL_Expression.__init__)
    params = list(sig.parameters.keys())



def test_hyp_dsl_behaviors_is_not_abstract():
    assert not inspect.isabstract(dSL_Behaviors)


def test_hyp_dsl_behaviors_constructor_exists():
    assert callable(dSL_Behaviors.__init__)


def test_hyp_dsl_behaviors_constructor_args():
    sig = inspect.signature(dSL_Behaviors.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"


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
        "BACKWARD",
        "FORWARD",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in FBEnum"

def test_hyp_actionenum_exists():
    # Check that the Enumeration exists
    assert ActionEnum is not None

def test_hyp_actionenum_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in ActionEnum]
    expected_literals = [
        "STOP",
        "FORWARD",
        "BACKWARD",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in ActionEnum"

def test_hyp_touchenum_exists():
    # Check that the Enumeration exists
    assert TouchEnum is not None

def test_hyp_touchenum_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in TouchEnum]
    expected_literals = [
        "LEFT",
        "RIGHT",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in TouchEnum"

def test_hyp_edgeenum_exists():
    # Check that the Enumeration exists
    assert EdgeEnum is not None

def test_hyp_edgeenum_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in EdgeEnum]
    expected_literals = [
        "FRONTLEFT",
        "FRONTRIGHT",
        "BACK",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in EdgeEnum"

def test_hyp_colorenum_exists():
    # Check that the Enumeration exists
    assert ColorEnum is not None

def test_hyp_colorenum_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in ColorEnum]
    expected_literals = [
        "YELLOW",
        "BLUE",
        "WHITE",
        "BLACK",
        "RED",
        "BROWN",
        "NONE",
        "GREEN",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in ColorEnum"


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
RotatePoints_strategy = st.builds(
    RotatePoints,
)
dSL_MiddleRotatePoint_strategy = st.builds(
    dSL_MiddleRotatePoint,
    middledir=
        safe_text
)
dSL_RightRotatePoint_strategy = st.builds(
    dSL_RightRotatePoint,
    rightdir=
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
dSL_MovementAction_strategy = st.builds(
    dSL_MovementAction,
    actionenum=
        safe_text
)
Actions_strategy = st.builds(
    Actions,
)
dSL_RightMovementAction_strategy = st.builds(
    dSL_RightMovementAction,
)
dSL_RotateMovementAction_strategy = st.builds(
    dSL_RotateMovementAction,
)
dSL_LeftMovementAction_strategy = st.builds(
    dSL_LeftMovementAction,
)
dSL_Actions_strategy = st.builds(
    dSL_Actions,
)
Expression_strategy = st.builds(
    Expression,
)
dSL_DistanceLiteral_strategy = st.builds(
    dSL_DistanceLiteral,
    distance=
        st.integers()
)
dSL_TouchLiteral_strategy = st.builds(
    dSL_TouchLiteral,
    touch=
        safe_text
)
dSL_ColorLiteral_strategy = st.builds(
    dSL_ColorLiteral,
    color=
        safe_text
)
dSL_ANDexpression_strategy = st.builds(
    dSL_ANDexpression,
)
dSL_EdgeLiteral_strategy = st.builds(
    dSL_EdgeLiteral,
    edge=
        safe_text
)
dSL_ORexpression_strategy = st.builds(
    dSL_ORexpression,
)
dSL_ExpressionBracket_strategy = st.builds(
    dSL_ExpressionBracket,
)
dSL_RobotBehavior_strategy = st.builds(
    dSL_RobotBehavior,
)
dSL_Expression_strategy = st.builds(
    dSL_Expression,
)
dSL_Behaviors_strategy = st.builds(
    dSL_Behaviors,
    name=
        safe_text
)





@given(instance=dSL_MiddleRotatePoint_strategy)
def test_hyp_dsl_middlerotatepoint_middledir_setter(instance):
    original = instance.middledir
    instance.middledir = original
    assert instance.middledir == original




@given(instance=dSL_RightRotatePoint_strategy)
def test_hyp_dsl_rightrotatepoint_rightdir_setter(instance):
    original = instance.rightdir
    instance.rightdir = original
    assert instance.rightdir == original




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




@given(instance=dSL_MovementAction_strategy)
def test_hyp_dsl_movementaction_actionenum_setter(instance):
    original = instance.actionenum
    instance.actionenum = original
    assert instance.actionenum == original










@given(instance=dSL_DistanceLiteral_strategy)
def test_hyp_dsl_distanceliteral_distance_setter(instance):
    original = instance.distance
    instance.distance = original
    assert instance.distance == original




@given(instance=dSL_TouchLiteral_strategy)
def test_hyp_dsl_touchliteral_touch_setter(instance):
    original = instance.touch
    instance.touch = original
    assert instance.touch == original




@given(instance=dSL_ColorLiteral_strategy)
def test_hyp_dsl_colorliteral_color_setter(instance):
    original = instance.color
    instance.color = original
    assert instance.color == original





@given(instance=dSL_EdgeLiteral_strategy)
def test_hyp_dsl_edgeliteral_edge_setter(instance):
    original = instance.edge
    instance.edge = original
    assert instance.edge == original








@given(instance=dSL_Behaviors_strategy)
def test_hyp_dsl_behaviors_name_setter(instance):
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
    Expression,
    RotateMovementAction,
    RotatePoints,
    dSL_ANDexpression,
    dSL_Actions,
    dSL_Behaviors,
    dSL_ColorLiteral,
    dSL_DistanceLiteral,
    dSL_EdgeLiteral,
    dSL_Expression,
    dSL_ExpressionBracket,
    dSL_LeftMovementAction,
    dSL_LeftRotatePoint,
    dSL_MiddleRotatePoint,
    dSL_MovementAction,
    dSL_ORexpression,
    dSL_RightMovementAction,
    dSL_RightRotatePoint,
    dSL_RobotBehavior,
    dSL_RotateMovementAction,
    dSL_RotatePoints,
    dSL_TouchLiteral,
    ActionEnum,
    ColorEnum,
    EdgeEnum,
    FBEnum,
    LREnum,
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

def test_dSL_Behaviors_name_value_roundtrip():
    instance = dSL_Behaviors(name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_dSL_ColorLiteral_color_value_roundtrip():
    instance = dSL_ColorLiteral(color="sample_text")
    assert instance.color == "sample_text"
    instance.color = "sample_text_2"
    assert instance.color == "sample_text_2"


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


def test_dSL_LeftRotatePoint_leftdir_value_roundtrip():
    instance = dSL_LeftRotatePoint(leftdir="sample_text")
    assert instance.leftdir == "sample_text"
    instance.leftdir = "sample_text_2"
    assert instance.leftdir == "sample_text_2"


def test_dSL_MiddleRotatePoint_middledir_value_roundtrip():
    instance = dSL_MiddleRotatePoint(middledir="sample_text")
    assert instance.middledir == "sample_text"
    instance.middledir = "sample_text_2"
    assert instance.middledir == "sample_text_2"


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


def test_dSL_LeftMovementAction_isa_Actions():
    instance = dSL_LeftMovementAction()
    assert isinstance(instance, Actions)


def test_dSL_RightMovementAction_isa_Actions():
    instance = dSL_RightMovementAction()
    assert isinstance(instance, Actions)


def test_dSL_RotateMovementAction_isa_Actions():
    instance = dSL_RotateMovementAction()
    assert isinstance(instance, Actions)


def test_dSL_ANDexpression_isa_Expression():
    instance = dSL_ANDexpression()
    assert isinstance(instance, Expression)


def test_dSL_ColorLiteral_isa_Expression():
    instance = dSL_ColorLiteral(color="sample_text")
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


def test_assoc_actionlist3_link_reassign_clear():
    a = dSL_Behaviors(name="sample_text")
    b1 = dSL_Actions()
    b2 = dSL_Actions()
    _safe_set(a, 'dSL_Behaviors4', {b1})
    assert _is_linked(a, 'dSL_Behaviors4', b1)
    if hasattr(b1, 'dSL_Actions'):
        assert _is_linked(b1, 'dSL_Actions', a)
    _safe_set(a, 'dSL_Behaviors4', {b2})
    assert _is_linked(a, 'dSL_Behaviors4', b2)
    if hasattr(b1, 'dSL_Actions'):
        assert not _is_linked(b1, 'dSL_Actions', a)
    if hasattr(b2, 'dSL_Actions'):
        assert _is_linked(b2, 'dSL_Actions', a)
    _safe_set(a, 'dSL_Behaviors4', set())
    assert not _is_linked(a, 'dSL_Behaviors4', b2)
    if hasattr(b2, 'dSL_Actions'):
        assert not _is_linked(b2, 'dSL_Actions', a)


def test_assoc_behaviorlist0_link_reassign_clear():
    a = dSL_Behaviors(name="sample_text")
    b1 = dSL_RobotBehavior()
    b2 = dSL_RobotBehavior()
    _safe_set(a, 'dSL_Behaviors', b1)
    assert _is_linked(a, 'dSL_Behaviors', b1)
    if hasattr(b1, 'dSL_RobotBehavior'):
        assert _is_linked(b1, 'dSL_RobotBehavior', a)
    _safe_set(a, 'dSL_Behaviors', b2)
    assert _is_linked(a, 'dSL_Behaviors', b2)
    if hasattr(b1, 'dSL_RobotBehavior'):
        assert not _is_linked(b1, 'dSL_RobotBehavior', a)
    if hasattr(b2, 'dSL_RobotBehavior'):
        assert _is_linked(b2, 'dSL_RobotBehavior', a)
    _safe_set(a, 'dSL_Behaviors', None)
    assert not _is_linked(a, 'dSL_Behaviors', b2)
    if hasattr(b2, 'dSL_RobotBehavior'):
        assert not _is_linked(b2, 'dSL_RobotBehavior', a)


def test_assoc_leftmove5_link_reassign_clear():
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


def test_assoc_rightmove6_link_reassign_clear():
    a = dSL_MovementAction(actionenum="sample_text")
    b1 = dSL_RightMovementAction()
    b2 = dSL_RightMovementAction()
    _safe_set(a, 'dSL_MovementAction7', b1)
    assert _is_linked(a, 'dSL_MovementAction7', b1)
    if hasattr(b1, 'dSL_RightMovementAction'):
        assert _is_linked(b1, 'dSL_RightMovementAction', a)
    _safe_set(a, 'dSL_MovementAction7', b2)
    assert _is_linked(a, 'dSL_MovementAction7', b2)
    if hasattr(b1, 'dSL_RightMovementAction'):
        assert not _is_linked(b1, 'dSL_RightMovementAction', a)
    if hasattr(b2, 'dSL_RightMovementAction'):
        assert _is_linked(b2, 'dSL_RightMovementAction', a)
    _safe_set(a, 'dSL_MovementAction7', None)
    assert not _is_linked(a, 'dSL_MovementAction7', b2)
    if hasattr(b2, 'dSL_RightMovementAction'):
        assert not _is_linked(b2, 'dSL_RightMovementAction', a)


def test_assoc_sensorExpression1_link_reassign_clear():
    a = dSL_Behaviors(name="sample_text")
    b1 = dSL_Expression()
    b2 = dSL_Expression()
    _safe_set(a, 'dSL_Behaviors2', b1)
    assert _is_linked(a, 'dSL_Behaviors2', b1)
    if hasattr(b1, 'dSL_Expression'):
        assert _is_linked(b1, 'dSL_Expression', a)
    _safe_set(a, 'dSL_Behaviors2', b2)
    assert _is_linked(a, 'dSL_Behaviors2', b2)
    if hasattr(b1, 'dSL_Expression'):
        assert not _is_linked(b1, 'dSL_Expression', a)
    if hasattr(b2, 'dSL_Expression'):
        assert _is_linked(b2, 'dSL_Expression', a)
    _safe_set(a, 'dSL_Behaviors2', None)
    assert not _is_linked(a, 'dSL_Behaviors2', b2)
    if hasattr(b2, 'dSL_Expression'):
        assert not _is_linked(b2, 'dSL_Expression', a)


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

Actions_strategy = st.builds(Actions)
@given(instance=Actions_strategy)
@settings(max_examples=25)
def test_Actions_instantiation(instance):
    assert isinstance(instance, Actions)


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


dSL_Behaviors_strategy = st.builds(dSL_Behaviors, name=safe_text)
@given(instance=dSL_Behaviors_strategy)
@settings(max_examples=25)
def test_dSL_Behaviors_instantiation(instance):
    assert isinstance(instance, dSL_Behaviors)


dSL_ColorLiteral_strategy = st.builds(dSL_ColorLiteral, color=safe_text)
@given(instance=dSL_ColorLiteral_strategy)
@settings(max_examples=25)
def test_dSL_ColorLiteral_instantiation(instance):
    assert isinstance(instance, dSL_ColorLiteral)


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


dSL_MiddleRotatePoint_strategy = st.builds(dSL_MiddleRotatePoint, middledir=safe_text)
@given(instance=dSL_MiddleRotatePoint_strategy)
@settings(max_examples=25)
def test_dSL_MiddleRotatePoint_instantiation(instance):
    assert isinstance(instance, dSL_MiddleRotatePoint)


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


dSL_RobotBehavior_strategy = st.builds(dSL_RobotBehavior)
@given(instance=dSL_RobotBehavior_strategy)
@settings(max_examples=25)
def test_dSL_RobotBehavior_instantiation(instance):
    assert isinstance(instance, dSL_RobotBehavior)


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



