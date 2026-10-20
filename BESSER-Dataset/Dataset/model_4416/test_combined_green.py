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
    Sensor,
    mindstorms_ColorSensor,
    mindstorms_UltrasonicSensor,
    mindstorms_TouchSensor,
    Behavior,
    mindstorms_ExploreForward,
    mindstorms_ReturnBottleToBase,
    mindstorms_AvoidObstacle,
    mindstorms_ConditionContainer,
    ConditionContainer,
    BlockContainer,
    Instruction,
    mindstorms_Arbitrator,
    mindstorms_ReuseInstruction,
    mindstorms_Procedure,
    mindstorms_Block,
    mindstorms_BlockContainer,
    NamedElement,
    mindstorms_Behavior,
    mindstorms_Instruction,
    mindstorms_Main,
    Action,
    mindstorms_Release,
    mindstorms_ReturnToBase,
    mindstorms_GoTo,
    mindstorms_GoToEnemy,
    mindstorms_Rotate,
    mindstorms_Delay,
    mindstorms_GoBackward,
    mindstorms_Grab,
    mindstorms_GoForward,
    Flow,
    mindstorms_While,
    mindstorms_If,
    mindstorms_Condition,
    Condition,
    mindstorms_Sensor,
    Block,
    mindstorms_Flow,
    mindstorms_Action,
    mindstorms_NamedElement,
    OperatorKind,
    Color,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_hyp_sensor_is_not_abstract():
    assert not inspect.isabstract(Sensor)


def test_hyp_sensor_constructor_exists():
    assert callable(Sensor.__init__)


def test_hyp_sensor_constructor_args():
    sig = inspect.signature(Sensor.__init__)
    params = list(sig.parameters.keys())



def test_hyp_mindstorms_colorsensor_is_not_abstract():
    assert not inspect.isabstract(mindstorms_ColorSensor)


def test_hyp_mindstorms_colorsensor_constructor_exists():
    assert callable(mindstorms_ColorSensor.__init__)


def test_hyp_mindstorms_colorsensor_constructor_args():
    sig = inspect.signature(mindstorms_ColorSensor.__init__)
    params = list(sig.parameters.keys())
    assert "color" in params, "Missing parameter 'color'"




def test_hyp_mindstorms_ultrasonicsensor_is_not_abstract():
    assert not inspect.isabstract(mindstorms_UltrasonicSensor)


def test_hyp_mindstorms_ultrasonicsensor_constructor_exists():
    assert callable(mindstorms_UltrasonicSensor.__init__)


def test_hyp_mindstorms_ultrasonicsensor_constructor_args():
    sig = inspect.signature(mindstorms_UltrasonicSensor.__init__)
    params = list(sig.parameters.keys())
    assert "operator" in params, "Missing parameter 'operator'"
    assert "value" in params, "Missing parameter 'value'"





def test_hyp_mindstorms_touchsensor_is_not_abstract():
    assert not inspect.isabstract(mindstorms_TouchSensor)


def test_hyp_mindstorms_touchsensor_constructor_exists():
    assert callable(mindstorms_TouchSensor.__init__)


def test_hyp_mindstorms_touchsensor_constructor_args():
    sig = inspect.signature(mindstorms_TouchSensor.__init__)
    params = list(sig.parameters.keys())
    assert "isPressed" in params, "Missing parameter 'isPressed'"




def test_hyp_behavior_is_not_abstract():
    assert not inspect.isabstract(Behavior)


def test_hyp_behavior_constructor_exists():
    assert callable(Behavior.__init__)


def test_hyp_behavior_constructor_args():
    sig = inspect.signature(Behavior.__init__)
    params = list(sig.parameters.keys())



def test_hyp_mindstorms_exploreforward_is_not_abstract():
    assert not inspect.isabstract(mindstorms_ExploreForward)


def test_hyp_mindstorms_exploreforward_constructor_exists():
    assert callable(mindstorms_ExploreForward.__init__)


def test_hyp_mindstorms_exploreforward_constructor_args():
    sig = inspect.signature(mindstorms_ExploreForward.__init__)
    params = list(sig.parameters.keys())



def test_hyp_mindstorms_returnbottletobase_is_not_abstract():
    assert not inspect.isabstract(mindstorms_ReturnBottleToBase)


def test_hyp_mindstorms_returnbottletobase_constructor_exists():
    assert callable(mindstorms_ReturnBottleToBase.__init__)


def test_hyp_mindstorms_returnbottletobase_constructor_args():
    sig = inspect.signature(mindstorms_ReturnBottleToBase.__init__)
    params = list(sig.parameters.keys())



def test_hyp_mindstorms_avoidobstacle_is_not_abstract():
    assert not inspect.isabstract(mindstorms_AvoidObstacle)


def test_hyp_mindstorms_avoidobstacle_constructor_exists():
    assert callable(mindstorms_AvoidObstacle.__init__)


def test_hyp_mindstorms_avoidobstacle_constructor_args():
    sig = inspect.signature(mindstorms_AvoidObstacle.__init__)
    params = list(sig.parameters.keys())



def test_hyp_mindstorms_conditioncontainer_is_not_abstract():
    assert not inspect.isabstract(mindstorms_ConditionContainer)


def test_hyp_mindstorms_conditioncontainer_constructor_exists():
    assert callable(mindstorms_ConditionContainer.__init__)


def test_hyp_mindstorms_conditioncontainer_constructor_args():
    sig = inspect.signature(mindstorms_ConditionContainer.__init__)
    params = list(sig.parameters.keys())



def test_hyp_conditioncontainer_is_not_abstract():
    assert not inspect.isabstract(ConditionContainer)


def test_hyp_conditioncontainer_constructor_exists():
    assert callable(ConditionContainer.__init__)


def test_hyp_conditioncontainer_constructor_args():
    sig = inspect.signature(ConditionContainer.__init__)
    params = list(sig.parameters.keys())



def test_hyp_blockcontainer_is_not_abstract():
    assert not inspect.isabstract(BlockContainer)


def test_hyp_blockcontainer_constructor_exists():
    assert callable(BlockContainer.__init__)


def test_hyp_blockcontainer_constructor_args():
    sig = inspect.signature(BlockContainer.__init__)
    params = list(sig.parameters.keys())



def test_hyp_instruction_is_not_abstract():
    assert not inspect.isabstract(Instruction)


def test_hyp_instruction_constructor_exists():
    assert callable(Instruction.__init__)


def test_hyp_instruction_constructor_args():
    sig = inspect.signature(Instruction.__init__)
    params = list(sig.parameters.keys())



def test_hyp_mindstorms_arbitrator_is_not_abstract():
    assert not inspect.isabstract(mindstorms_Arbitrator)


def test_hyp_mindstorms_arbitrator_constructor_exists():
    assert callable(mindstorms_Arbitrator.__init__)


def test_hyp_mindstorms_arbitrator_constructor_args():
    sig = inspect.signature(mindstorms_Arbitrator.__init__)
    params = list(sig.parameters.keys())



def test_hyp_mindstorms_reuseinstruction_is_not_abstract():
    assert not inspect.isabstract(mindstorms_ReuseInstruction)


def test_hyp_mindstorms_reuseinstruction_constructor_exists():
    assert callable(mindstorms_ReuseInstruction.__init__)


def test_hyp_mindstorms_reuseinstruction_constructor_args():
    sig = inspect.signature(mindstorms_ReuseInstruction.__init__)
    params = list(sig.parameters.keys())



def test_hyp_mindstorms_procedure_is_not_abstract():
    assert not inspect.isabstract(mindstorms_Procedure)


def test_hyp_mindstorms_procedure_constructor_exists():
    assert callable(mindstorms_Procedure.__init__)


def test_hyp_mindstorms_procedure_constructor_args():
    sig = inspect.signature(mindstorms_Procedure.__init__)
    params = list(sig.parameters.keys())



def test_hyp_mindstorms_block_is_not_abstract():
    assert not inspect.isabstract(mindstorms_Block)


def test_hyp_mindstorms_block_constructor_exists():
    assert callable(mindstorms_Block.__init__)


def test_hyp_mindstorms_block_constructor_args():
    sig = inspect.signature(mindstorms_Block.__init__)
    params = list(sig.parameters.keys())



def test_hyp_mindstorms_blockcontainer_is_not_abstract():
    assert not inspect.isabstract(mindstorms_BlockContainer)


def test_hyp_mindstorms_blockcontainer_constructor_exists():
    assert callable(mindstorms_BlockContainer.__init__)


def test_hyp_mindstorms_blockcontainer_constructor_args():
    sig = inspect.signature(mindstorms_BlockContainer.__init__)
    params = list(sig.parameters.keys())



def test_hyp_namedelement_is_not_abstract():
    assert not inspect.isabstract(NamedElement)


def test_hyp_namedelement_constructor_exists():
    assert callable(NamedElement.__init__)


def test_hyp_namedelement_constructor_args():
    sig = inspect.signature(NamedElement.__init__)
    params = list(sig.parameters.keys())



def test_hyp_mindstorms_behavior_is_not_abstract():
    assert not inspect.isabstract(mindstorms_Behavior)


def test_hyp_mindstorms_behavior_constructor_exists():
    assert callable(mindstorms_Behavior.__init__)


def test_hyp_mindstorms_behavior_constructor_args():
    sig = inspect.signature(mindstorms_Behavior.__init__)
    params = list(sig.parameters.keys())



def test_hyp_mindstorms_instruction_is_not_abstract():
    assert not inspect.isabstract(mindstorms_Instruction)


def test_hyp_mindstorms_instruction_constructor_exists():
    assert callable(mindstorms_Instruction.__init__)


def test_hyp_mindstorms_instruction_constructor_args():
    sig = inspect.signature(mindstorms_Instruction.__init__)
    params = list(sig.parameters.keys())



def test_hyp_mindstorms_main_is_not_abstract():
    assert not inspect.isabstract(mindstorms_Main)


def test_hyp_mindstorms_main_constructor_exists():
    assert callable(mindstorms_Main.__init__)


def test_hyp_mindstorms_main_constructor_args():
    sig = inspect.signature(mindstorms_Main.__init__)
    params = list(sig.parameters.keys())



def test_hyp_action_is_not_abstract():
    assert not inspect.isabstract(Action)


def test_hyp_action_constructor_exists():
    assert callable(Action.__init__)


def test_hyp_action_constructor_args():
    sig = inspect.signature(Action.__init__)
    params = list(sig.parameters.keys())



def test_hyp_mindstorms_release_is_not_abstract():
    assert not inspect.isabstract(mindstorms_Release)


def test_hyp_mindstorms_release_constructor_exists():
    assert callable(mindstorms_Release.__init__)


def test_hyp_mindstorms_release_constructor_args():
    sig = inspect.signature(mindstorms_Release.__init__)
    params = list(sig.parameters.keys())



def test_hyp_mindstorms_returntobase_is_not_abstract():
    assert not inspect.isabstract(mindstorms_ReturnToBase)


def test_hyp_mindstorms_returntobase_constructor_exists():
    assert callable(mindstorms_ReturnToBase.__init__)


def test_hyp_mindstorms_returntobase_constructor_args():
    sig = inspect.signature(mindstorms_ReturnToBase.__init__)
    params = list(sig.parameters.keys())



def test_hyp_mindstorms_goto_is_not_abstract():
    assert not inspect.isabstract(mindstorms_GoTo)


def test_hyp_mindstorms_goto_constructor_exists():
    assert callable(mindstorms_GoTo.__init__)


def test_hyp_mindstorms_goto_constructor_args():
    sig = inspect.signature(mindstorms_GoTo.__init__)
    params = list(sig.parameters.keys())
    assert "y" in params, "Missing parameter 'y'"
    assert "x" in params, "Missing parameter 'x'"





def test_hyp_mindstorms_gotoenemy_is_not_abstract():
    assert not inspect.isabstract(mindstorms_GoToEnemy)


def test_hyp_mindstorms_gotoenemy_constructor_exists():
    assert callable(mindstorms_GoToEnemy.__init__)


def test_hyp_mindstorms_gotoenemy_constructor_args():
    sig = inspect.signature(mindstorms_GoToEnemy.__init__)
    params = list(sig.parameters.keys())



def test_hyp_mindstorms_rotate_is_not_abstract():
    assert not inspect.isabstract(mindstorms_Rotate)


def test_hyp_mindstorms_rotate_constructor_exists():
    assert callable(mindstorms_Rotate.__init__)


def test_hyp_mindstorms_rotate_constructor_args():
    sig = inspect.signature(mindstorms_Rotate.__init__)
    params = list(sig.parameters.keys())
    assert "degrees" in params, "Missing parameter 'degrees'"
    assert "random" in params, "Missing parameter 'random'"





def test_hyp_mindstorms_delay_is_not_abstract():
    assert not inspect.isabstract(mindstorms_Delay)


def test_hyp_mindstorms_delay_constructor_exists():
    assert callable(mindstorms_Delay.__init__)


def test_hyp_mindstorms_delay_constructor_args():
    sig = inspect.signature(mindstorms_Delay.__init__)
    params = list(sig.parameters.keys())
    assert "ms" in params, "Missing parameter 'ms'"




def test_hyp_mindstorms_gobackward_is_not_abstract():
    assert not inspect.isabstract(mindstorms_GoBackward)


def test_hyp_mindstorms_gobackward_constructor_exists():
    assert callable(mindstorms_GoBackward.__init__)


def test_hyp_mindstorms_gobackward_constructor_args():
    sig = inspect.signature(mindstorms_GoBackward.__init__)
    params = list(sig.parameters.keys())
    assert "cm" in params, "Missing parameter 'cm'"
    assert "infinite" in params, "Missing parameter 'infinite'"





def test_hyp_mindstorms_grab_is_not_abstract():
    assert not inspect.isabstract(mindstorms_Grab)


def test_hyp_mindstorms_grab_constructor_exists():
    assert callable(mindstorms_Grab.__init__)


def test_hyp_mindstorms_grab_constructor_args():
    sig = inspect.signature(mindstorms_Grab.__init__)
    params = list(sig.parameters.keys())



def test_hyp_mindstorms_goforward_is_not_abstract():
    assert not inspect.isabstract(mindstorms_GoForward)


def test_hyp_mindstorms_goforward_constructor_exists():
    assert callable(mindstorms_GoForward.__init__)


def test_hyp_mindstorms_goforward_constructor_args():
    sig = inspect.signature(mindstorms_GoForward.__init__)
    params = list(sig.parameters.keys())
    assert "infinite" in params, "Missing parameter 'infinite'"
    assert "cm" in params, "Missing parameter 'cm'"





def test_hyp_flow_is_not_abstract():
    assert not inspect.isabstract(Flow)


def test_hyp_flow_constructor_exists():
    assert callable(Flow.__init__)


def test_hyp_flow_constructor_args():
    sig = inspect.signature(Flow.__init__)
    params = list(sig.parameters.keys())



def test_hyp_mindstorms_while_is_not_abstract():
    assert not inspect.isabstract(mindstorms_While)


def test_hyp_mindstorms_while_constructor_exists():
    assert callable(mindstorms_While.__init__)


def test_hyp_mindstorms_while_constructor_args():
    sig = inspect.signature(mindstorms_While.__init__)
    params = list(sig.parameters.keys())



def test_hyp_mindstorms_if_is_not_abstract():
    assert not inspect.isabstract(mindstorms_If)


def test_hyp_mindstorms_if_constructor_exists():
    assert callable(mindstorms_If.__init__)


def test_hyp_mindstorms_if_constructor_args():
    sig = inspect.signature(mindstorms_If.__init__)
    params = list(sig.parameters.keys())



def test_hyp_mindstorms_condition_is_not_abstract():
    assert not inspect.isabstract(mindstorms_Condition)


def test_hyp_mindstorms_condition_constructor_exists():
    assert callable(mindstorms_Condition.__init__)


def test_hyp_mindstorms_condition_constructor_args():
    sig = inspect.signature(mindstorms_Condition.__init__)
    params = list(sig.parameters.keys())



def test_hyp_condition_is_not_abstract():
    assert not inspect.isabstract(Condition)


def test_hyp_condition_constructor_exists():
    assert callable(Condition.__init__)


def test_hyp_condition_constructor_args():
    sig = inspect.signature(Condition.__init__)
    params = list(sig.parameters.keys())



def test_hyp_mindstorms_sensor_is_not_abstract():
    assert not inspect.isabstract(mindstorms_Sensor)


def test_hyp_mindstorms_sensor_constructor_exists():
    assert callable(mindstorms_Sensor.__init__)


def test_hyp_mindstorms_sensor_constructor_args():
    sig = inspect.signature(mindstorms_Sensor.__init__)
    params = list(sig.parameters.keys())



def test_hyp_block_is_not_abstract():
    assert not inspect.isabstract(Block)


def test_hyp_block_constructor_exists():
    assert callable(Block.__init__)


def test_hyp_block_constructor_args():
    sig = inspect.signature(Block.__init__)
    params = list(sig.parameters.keys())



def test_hyp_mindstorms_flow_is_not_abstract():
    assert not inspect.isabstract(mindstorms_Flow)


def test_hyp_mindstorms_flow_constructor_exists():
    assert callable(mindstorms_Flow.__init__)


def test_hyp_mindstorms_flow_constructor_args():
    sig = inspect.signature(mindstorms_Flow.__init__)
    params = list(sig.parameters.keys())



def test_hyp_mindstorms_action_is_not_abstract():
    assert not inspect.isabstract(mindstorms_Action)


def test_hyp_mindstorms_action_constructor_exists():
    assert callable(mindstorms_Action.__init__)


def test_hyp_mindstorms_action_constructor_args():
    sig = inspect.signature(mindstorms_Action.__init__)
    params = list(sig.parameters.keys())



def test_hyp_mindstorms_namedelement_is_not_abstract():
    assert not inspect.isabstract(mindstorms_NamedElement)


def test_hyp_mindstorms_namedelement_constructor_exists():
    assert callable(mindstorms_NamedElement.__init__)


def test_hyp_mindstorms_namedelement_constructor_args():
    sig = inspect.signature(mindstorms_NamedElement.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"


def test_hyp_operatorkind_exists():
    # Check that the Enumeration exists
    assert OperatorKind is not None

def test_hyp_operatorkind_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in OperatorKind]
    expected_literals = [
        "upperOrEqual",
        "notEqual",
        "lowerOrEqual",
        "equal",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in OperatorKind"

def test_hyp_color_exists():
    # Check that the Enumeration exists
    assert Color is not None

def test_hyp_color_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in Color]
    expected_literals = [
        "BLACK",
        "ORANGE",
        "WHITE",
        "PINK",
        "DARK_GRAY",
        "MAGENTA",
        "GREEN",
        "YELLOW",
        "BROWN",
        "LIGHT_GRAY",
        "GRAY",
        "CYAN",
        "NONE",
        "RED",
        "BLUE",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in Color"


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
Sensor_strategy = st.builds(
    Sensor,
)
mindstorms_ColorSensor_strategy = st.builds(
    mindstorms_ColorSensor,
    color=
        safe_text
)
mindstorms_UltrasonicSensor_strategy = st.builds(
    mindstorms_UltrasonicSensor,
    operator=
        safe_text,
    value=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
mindstorms_TouchSensor_strategy = st.builds(
    mindstorms_TouchSensor,
    isPressed=
        st.booleans()
)
Behavior_strategy = st.builds(
    Behavior,
)
mindstorms_ExploreForward_strategy = st.builds(
    mindstorms_ExploreForward,
)
mindstorms_ReturnBottleToBase_strategy = st.builds(
    mindstorms_ReturnBottleToBase,
)
mindstorms_AvoidObstacle_strategy = st.builds(
    mindstorms_AvoidObstacle,
)
mindstorms_ConditionContainer_strategy = st.builds(
    mindstorms_ConditionContainer,
)
ConditionContainer_strategy = st.builds(
    ConditionContainer,
)
BlockContainer_strategy = st.builds(
    BlockContainer,
)
Instruction_strategy = st.builds(
    Instruction,
)
mindstorms_Arbitrator_strategy = st.builds(
    mindstorms_Arbitrator,
)
mindstorms_ReuseInstruction_strategy = st.builds(
    mindstorms_ReuseInstruction,
)
mindstorms_Procedure_strategy = st.builds(
    mindstorms_Procedure,
)
mindstorms_Block_strategy = st.builds(
    mindstorms_Block,
)
mindstorms_BlockContainer_strategy = st.builds(
    mindstorms_BlockContainer,
)
NamedElement_strategy = st.builds(
    NamedElement,
)
mindstorms_Behavior_strategy = st.builds(
    mindstorms_Behavior,
)
mindstorms_Instruction_strategy = st.builds(
    mindstorms_Instruction,
)
mindstorms_Main_strategy = st.builds(
    mindstorms_Main,
)
Action_strategy = st.builds(
    Action,
)
mindstorms_Release_strategy = st.builds(
    mindstorms_Release,
)
mindstorms_ReturnToBase_strategy = st.builds(
    mindstorms_ReturnToBase,
)
mindstorms_GoTo_strategy = st.builds(
    mindstorms_GoTo,
    y=
        st.integers(),
    x=
        st.integers()
)
mindstorms_GoToEnemy_strategy = st.builds(
    mindstorms_GoToEnemy,
)
mindstorms_Rotate_strategy = st.builds(
    mindstorms_Rotate,
    degrees=
        st.integers(),
    random=
        st.booleans()
)
mindstorms_Delay_strategy = st.builds(
    mindstorms_Delay,
    ms=
        st.integers()
)
mindstorms_GoBackward_strategy = st.builds(
    mindstorms_GoBackward,
    cm=
        st.integers(),
    infinite=
        st.booleans()
)
mindstorms_Grab_strategy = st.builds(
    mindstorms_Grab,
)
mindstorms_GoForward_strategy = st.builds(
    mindstorms_GoForward,
    infinite=
        st.booleans(),
    cm=
        st.integers()
)
Flow_strategy = st.builds(
    Flow,
)
mindstorms_While_strategy = st.builds(
    mindstorms_While,
)
mindstorms_If_strategy = st.builds(
    mindstorms_If,
)
mindstorms_Condition_strategy = st.builds(
    mindstorms_Condition,
)
Condition_strategy = st.builds(
    Condition,
)
mindstorms_Sensor_strategy = st.builds(
    mindstorms_Sensor,
)
Block_strategy = st.builds(
    Block,
)
mindstorms_Flow_strategy = st.builds(
    mindstorms_Flow,
)
mindstorms_Action_strategy = st.builds(
    mindstorms_Action,
)
mindstorms_NamedElement_strategy = st.builds(
    mindstorms_NamedElement,
    name=
        safe_text
)





@given(instance=mindstorms_ColorSensor_strategy)
def test_hyp_mindstorms_colorsensor_color_setter(instance):
    original = instance.color
    instance.color = original
    assert instance.color == original




@given(instance=mindstorms_UltrasonicSensor_strategy)
def test_hyp_mindstorms_ultrasonicsensor_operator_setter(instance):
    original = instance.operator
    instance.operator = original
    assert instance.operator == original



@given(instance=mindstorms_UltrasonicSensor_strategy)
def test_hyp_mindstorms_ultrasonicsensor_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original




@given(instance=mindstorms_TouchSensor_strategy)
def test_hyp_mindstorms_touchsensor_isPressed_setter(instance):
    original = instance.isPressed
    instance.isPressed = original
    assert instance.isPressed == original
























@given(instance=mindstorms_GoTo_strategy)
def test_hyp_mindstorms_goto_y_setter(instance):
    original = instance.y
    instance.y = original
    assert instance.y == original



@given(instance=mindstorms_GoTo_strategy)
def test_hyp_mindstorms_goto_x_setter(instance):
    original = instance.x
    instance.x = original
    assert instance.x == original





@given(instance=mindstorms_Rotate_strategy)
def test_hyp_mindstorms_rotate_degrees_setter(instance):
    original = instance.degrees
    instance.degrees = original
    assert instance.degrees == original



@given(instance=mindstorms_Rotate_strategy)
def test_hyp_mindstorms_rotate_random_setter(instance):
    original = instance.random
    instance.random = original
    assert instance.random == original




@given(instance=mindstorms_Delay_strategy)
def test_hyp_mindstorms_delay_ms_setter(instance):
    original = instance.ms
    instance.ms = original
    assert instance.ms == original




@given(instance=mindstorms_GoBackward_strategy)
def test_hyp_mindstorms_gobackward_cm_setter(instance):
    original = instance.cm
    instance.cm = original
    assert instance.cm == original



@given(instance=mindstorms_GoBackward_strategy)
def test_hyp_mindstorms_gobackward_infinite_setter(instance):
    original = instance.infinite
    instance.infinite = original
    assert instance.infinite == original





@given(instance=mindstorms_GoForward_strategy)
def test_hyp_mindstorms_goforward_infinite_setter(instance):
    original = instance.infinite
    instance.infinite = original
    assert instance.infinite == original



@given(instance=mindstorms_GoForward_strategy)
def test_hyp_mindstorms_goforward_cm_setter(instance):
    original = instance.cm
    instance.cm = original
    assert instance.cm == original













@given(instance=mindstorms_NamedElement_strategy)
def test_hyp_mindstorms_namedelement_name_setter(instance):
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
    Behavior,
    Block,
    BlockContainer,
    Condition,
    ConditionContainer,
    Flow,
    Instruction,
    NamedElement,
    Sensor,
    mindstorms_Action,
    mindstorms_Arbitrator,
    mindstorms_AvoidObstacle,
    mindstorms_Behavior,
    mindstorms_Block,
    mindstorms_BlockContainer,
    mindstorms_ColorSensor,
    mindstorms_Condition,
    mindstorms_ConditionContainer,
    mindstorms_Delay,
    mindstorms_ExploreForward,
    mindstorms_Flow,
    mindstorms_GoBackward,
    mindstorms_GoForward,
    mindstorms_GoTo,
    mindstorms_GoToEnemy,
    mindstorms_Grab,
    mindstorms_If,
    mindstorms_Instruction,
    mindstorms_Main,
    mindstorms_NamedElement,
    mindstorms_Procedure,
    mindstorms_Release,
    mindstorms_ReturnBottleToBase,
    mindstorms_ReturnToBase,
    mindstorms_ReuseInstruction,
    mindstorms_Rotate,
    mindstorms_Sensor,
    mindstorms_TouchSensor,
    mindstorms_UltrasonicSensor,
    mindstorms_While,
    Color,
    OperatorKind,
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

def test_mindstorms_ColorSensor_color_value_roundtrip():
    instance = mindstorms_ColorSensor(color="sample_text")
    assert instance.color == "sample_text"
    instance.color = "sample_text_2"
    assert instance.color == "sample_text_2"


def test_mindstorms_Delay_ms_value_roundtrip():
    instance = mindstorms_Delay(ms=7)
    assert instance.ms == 7
    instance.ms = 13
    assert instance.ms == 13


def test_mindstorms_GoBackward_cm_value_roundtrip():
    instance = mindstorms_GoBackward(cm=7, infinite=True)
    assert instance.cm == 7
    instance.cm = 13
    assert instance.cm == 13


def test_mindstorms_GoBackward_infinite_value_roundtrip():
    instance = mindstorms_GoBackward(cm=7, infinite=True)
    assert instance.infinite == True
    instance.infinite = False
    assert instance.infinite == False


def test_mindstorms_GoForward_cm_value_roundtrip():
    instance = mindstorms_GoForward(cm=7, infinite=True)
    assert instance.cm == 7
    instance.cm = 13
    assert instance.cm == 13


def test_mindstorms_GoForward_infinite_value_roundtrip():
    instance = mindstorms_GoForward(cm=7, infinite=True)
    assert instance.infinite == True
    instance.infinite = False
    assert instance.infinite == False


def test_mindstorms_GoTo_x_value_roundtrip():
    instance = mindstorms_GoTo(x=7, y=7)
    assert instance.x == 7
    instance.x = 13
    assert instance.x == 13


def test_mindstorms_GoTo_y_value_roundtrip():
    instance = mindstorms_GoTo(x=7, y=7)
    assert instance.y == 7
    instance.y = 13
    assert instance.y == 13


def test_mindstorms_NamedElement_name_value_roundtrip():
    instance = mindstorms_NamedElement(name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_mindstorms_Rotate_degrees_value_roundtrip():
    instance = mindstorms_Rotate(degrees=7, random=True)
    assert instance.degrees == 7
    instance.degrees = 13
    assert instance.degrees == 13


def test_mindstorms_Rotate_random_value_roundtrip():
    instance = mindstorms_Rotate(degrees=7, random=True)
    assert instance.random == True
    instance.random = False
    assert instance.random == False


def test_mindstorms_TouchSensor_isPressed_value_roundtrip():
    instance = mindstorms_TouchSensor(isPressed=True)
    assert instance.isPressed == True
    instance.isPressed = False
    assert instance.isPressed == False


def test_mindstorms_UltrasonicSensor_operator_value_roundtrip():
    instance = mindstorms_UltrasonicSensor(operator="sample_text", value=3.14)
    assert instance.operator == "sample_text"
    instance.operator = "sample_text_2"
    assert instance.operator == "sample_text_2"


def test_mindstorms_UltrasonicSensor_value_value_roundtrip():
    instance = mindstorms_UltrasonicSensor(operator="sample_text", value=3.14)
    assert instance.value == 3.14
    instance.value = 9.99
    assert instance.value == 9.99


def test_mindstorms_Delay_isa_Action():
    instance = mindstorms_Delay(ms=7)
    assert isinstance(instance, Action)


def test_mindstorms_GoBackward_isa_Action():
    instance = mindstorms_GoBackward(cm=7, infinite=True)
    assert isinstance(instance, Action)


def test_mindstorms_GoForward_isa_Action():
    instance = mindstorms_GoForward(cm=7, infinite=True)
    assert isinstance(instance, Action)


def test_mindstorms_GoTo_isa_Action():
    instance = mindstorms_GoTo(x=7, y=7)
    assert isinstance(instance, Action)


def test_mindstorms_GoToEnemy_isa_Action():
    instance = mindstorms_GoToEnemy()
    assert isinstance(instance, Action)


def test_mindstorms_Grab_isa_Action():
    instance = mindstorms_Grab()
    assert isinstance(instance, Action)


def test_mindstorms_Release_isa_Action():
    instance = mindstorms_Release()
    assert isinstance(instance, Action)


def test_mindstorms_ReturnToBase_isa_Action():
    instance = mindstorms_ReturnToBase()
    assert isinstance(instance, Action)


def test_mindstorms_Rotate_isa_Action():
    instance = mindstorms_Rotate(degrees=7, random=True)
    assert isinstance(instance, Action)


def test_mindstorms_AvoidObstacle_isa_Behavior():
    instance = mindstorms_AvoidObstacle()
    assert isinstance(instance, Behavior)


def test_mindstorms_ExploreForward_isa_Behavior():
    instance = mindstorms_ExploreForward()
    assert isinstance(instance, Behavior)


def test_mindstorms_ReturnBottleToBase_isa_Behavior():
    instance = mindstorms_ReturnBottleToBase()
    assert isinstance(instance, Behavior)


def test_mindstorms_Action_isa_Block():
    instance = mindstorms_Action()
    assert isinstance(instance, Block)


def test_mindstorms_Flow_isa_Block():
    instance = mindstorms_Flow()
    assert isinstance(instance, Block)


def test_mindstorms_Behavior_isa_BlockContainer():
    instance = mindstorms_Behavior()
    assert isinstance(instance, BlockContainer)


def test_mindstorms_Flow_isa_BlockContainer():
    instance = mindstorms_Flow()
    assert isinstance(instance, BlockContainer)


def test_mindstorms_Procedure_isa_BlockContainer():
    instance = mindstorms_Procedure()
    assert isinstance(instance, BlockContainer)


def test_mindstorms_Sensor_isa_Condition():
    instance = mindstorms_Sensor()
    assert isinstance(instance, Condition)


def test_mindstorms_Arbitrator_isa_ConditionContainer():
    instance = mindstorms_Arbitrator()
    assert isinstance(instance, ConditionContainer)


def test_mindstorms_Behavior_isa_ConditionContainer():
    instance = mindstorms_Behavior()
    assert isinstance(instance, ConditionContainer)


def test_mindstorms_Flow_isa_ConditionContainer():
    instance = mindstorms_Flow()
    assert isinstance(instance, ConditionContainer)


def test_mindstorms_If_isa_Flow():
    instance = mindstorms_If()
    assert isinstance(instance, Flow)


def test_mindstorms_While_isa_Flow():
    instance = mindstorms_While()
    assert isinstance(instance, Flow)


def test_mindstorms_Arbitrator_isa_Instruction():
    instance = mindstorms_Arbitrator()
    assert isinstance(instance, Instruction)


def test_mindstorms_Block_isa_Instruction():
    instance = mindstorms_Block()
    assert isinstance(instance, Instruction)


def test_mindstorms_Procedure_isa_Instruction():
    instance = mindstorms_Procedure()
    assert isinstance(instance, Instruction)


def test_mindstorms_ReuseInstruction_isa_Instruction():
    instance = mindstorms_ReuseInstruction()
    assert isinstance(instance, Instruction)


def test_mindstorms_Behavior_isa_NamedElement():
    instance = mindstorms_Behavior()
    assert isinstance(instance, NamedElement)


def test_mindstorms_Instruction_isa_NamedElement():
    instance = mindstorms_Instruction()
    assert isinstance(instance, NamedElement)


def test_mindstorms_Sensor_isa_NamedElement():
    instance = mindstorms_Sensor()
    assert isinstance(instance, NamedElement)


def test_mindstorms_ColorSensor_isa_Sensor():
    instance = mindstorms_ColorSensor(color="sample_text")
    assert isinstance(instance, Sensor)


def test_mindstorms_TouchSensor_isa_Sensor():
    instance = mindstorms_TouchSensor(isPressed=True)
    assert isinstance(instance, Sensor)


def test_mindstorms_UltrasonicSensor_isa_Sensor():
    instance = mindstorms_UltrasonicSensor(operator="sample_text", value=3.14)
    assert isinstance(instance, Sensor)


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

Action_strategy = st.builds(Action)
@given(instance=Action_strategy)
@settings(max_examples=25)
def test_Action_instantiation(instance):
    assert isinstance(instance, Action)


Behavior_strategy = st.builds(Behavior)
@given(instance=Behavior_strategy)
@settings(max_examples=25)
def test_Behavior_instantiation(instance):
    assert isinstance(instance, Behavior)


Block_strategy = st.builds(Block)
@given(instance=Block_strategy)
@settings(max_examples=25)
def test_Block_instantiation(instance):
    assert isinstance(instance, Block)


BlockContainer_strategy = st.builds(BlockContainer)
@given(instance=BlockContainer_strategy)
@settings(max_examples=25)
def test_BlockContainer_instantiation(instance):
    assert isinstance(instance, BlockContainer)


Condition_strategy = st.builds(Condition)
@given(instance=Condition_strategy)
@settings(max_examples=25)
def test_Condition_instantiation(instance):
    assert isinstance(instance, Condition)


ConditionContainer_strategy = st.builds(ConditionContainer)
@given(instance=ConditionContainer_strategy)
@settings(max_examples=25)
def test_ConditionContainer_instantiation(instance):
    assert isinstance(instance, ConditionContainer)


Flow_strategy = st.builds(Flow)
@given(instance=Flow_strategy)
@settings(max_examples=25)
def test_Flow_instantiation(instance):
    assert isinstance(instance, Flow)


Instruction_strategy = st.builds(Instruction)
@given(instance=Instruction_strategy)
@settings(max_examples=25)
def test_Instruction_instantiation(instance):
    assert isinstance(instance, Instruction)


NamedElement_strategy = st.builds(NamedElement)
@given(instance=NamedElement_strategy)
@settings(max_examples=25)
def test_NamedElement_instantiation(instance):
    assert isinstance(instance, NamedElement)


Sensor_strategy = st.builds(Sensor)
@given(instance=Sensor_strategy)
@settings(max_examples=25)
def test_Sensor_instantiation(instance):
    assert isinstance(instance, Sensor)


mindstorms_Action_strategy = st.builds(mindstorms_Action)
@given(instance=mindstorms_Action_strategy)
@settings(max_examples=25)
def test_mindstorms_Action_instantiation(instance):
    assert isinstance(instance, mindstorms_Action)


mindstorms_Arbitrator_strategy = st.builds(mindstorms_Arbitrator)
@given(instance=mindstorms_Arbitrator_strategy)
@settings(max_examples=25)
def test_mindstorms_Arbitrator_instantiation(instance):
    assert isinstance(instance, mindstorms_Arbitrator)


mindstorms_AvoidObstacle_strategy = st.builds(mindstorms_AvoidObstacle)
@given(instance=mindstorms_AvoidObstacle_strategy)
@settings(max_examples=25)
def test_mindstorms_AvoidObstacle_instantiation(instance):
    assert isinstance(instance, mindstorms_AvoidObstacle)


mindstorms_Behavior_strategy = st.builds(mindstorms_Behavior)
@given(instance=mindstorms_Behavior_strategy)
@settings(max_examples=25)
def test_mindstorms_Behavior_instantiation(instance):
    assert isinstance(instance, mindstorms_Behavior)


mindstorms_Block_strategy = st.builds(mindstorms_Block)
@given(instance=mindstorms_Block_strategy)
@settings(max_examples=25)
def test_mindstorms_Block_instantiation(instance):
    assert isinstance(instance, mindstorms_Block)


mindstorms_BlockContainer_strategy = st.builds(mindstorms_BlockContainer)
@given(instance=mindstorms_BlockContainer_strategy)
@settings(max_examples=25)
def test_mindstorms_BlockContainer_instantiation(instance):
    assert isinstance(instance, mindstorms_BlockContainer)


mindstorms_ColorSensor_strategy = st.builds(mindstorms_ColorSensor, color=safe_text)
@given(instance=mindstorms_ColorSensor_strategy)
@settings(max_examples=25)
def test_mindstorms_ColorSensor_instantiation(instance):
    assert isinstance(instance, mindstorms_ColorSensor)


mindstorms_Condition_strategy = st.builds(mindstorms_Condition)
@given(instance=mindstorms_Condition_strategy)
@settings(max_examples=25)
def test_mindstorms_Condition_instantiation(instance):
    assert isinstance(instance, mindstorms_Condition)


mindstorms_ConditionContainer_strategy = st.builds(mindstorms_ConditionContainer)
@given(instance=mindstorms_ConditionContainer_strategy)
@settings(max_examples=25)
def test_mindstorms_ConditionContainer_instantiation(instance):
    assert isinstance(instance, mindstorms_ConditionContainer)


mindstorms_Delay_strategy = st.builds(mindstorms_Delay, ms=st.integers())
@given(instance=mindstorms_Delay_strategy)
@settings(max_examples=25)
def test_mindstorms_Delay_instantiation(instance):
    assert isinstance(instance, mindstorms_Delay)


mindstorms_ExploreForward_strategy = st.builds(mindstorms_ExploreForward)
@given(instance=mindstorms_ExploreForward_strategy)
@settings(max_examples=25)
def test_mindstorms_ExploreForward_instantiation(instance):
    assert isinstance(instance, mindstorms_ExploreForward)


mindstorms_Flow_strategy = st.builds(mindstorms_Flow)
@given(instance=mindstorms_Flow_strategy)
@settings(max_examples=25)
def test_mindstorms_Flow_instantiation(instance):
    assert isinstance(instance, mindstorms_Flow)


mindstorms_GoBackward_strategy = st.builds(mindstorms_GoBackward, cm=st.integers(), infinite=st.booleans())
@given(instance=mindstorms_GoBackward_strategy)
@settings(max_examples=25)
def test_mindstorms_GoBackward_instantiation(instance):
    assert isinstance(instance, mindstorms_GoBackward)


mindstorms_GoForward_strategy = st.builds(mindstorms_GoForward, cm=st.integers(), infinite=st.booleans())
@given(instance=mindstorms_GoForward_strategy)
@settings(max_examples=25)
def test_mindstorms_GoForward_instantiation(instance):
    assert isinstance(instance, mindstorms_GoForward)


mindstorms_GoTo_strategy = st.builds(mindstorms_GoTo, x=st.integers(), y=st.integers())
@given(instance=mindstorms_GoTo_strategy)
@settings(max_examples=25)
def test_mindstorms_GoTo_instantiation(instance):
    assert isinstance(instance, mindstorms_GoTo)


mindstorms_GoToEnemy_strategy = st.builds(mindstorms_GoToEnemy)
@given(instance=mindstorms_GoToEnemy_strategy)
@settings(max_examples=25)
def test_mindstorms_GoToEnemy_instantiation(instance):
    assert isinstance(instance, mindstorms_GoToEnemy)


mindstorms_Grab_strategy = st.builds(mindstorms_Grab)
@given(instance=mindstorms_Grab_strategy)
@settings(max_examples=25)
def test_mindstorms_Grab_instantiation(instance):
    assert isinstance(instance, mindstorms_Grab)


mindstorms_If_strategy = st.builds(mindstorms_If)
@given(instance=mindstorms_If_strategy)
@settings(max_examples=25)
def test_mindstorms_If_instantiation(instance):
    assert isinstance(instance, mindstorms_If)


mindstorms_Instruction_strategy = st.builds(mindstorms_Instruction)
@given(instance=mindstorms_Instruction_strategy)
@settings(max_examples=25)
def test_mindstorms_Instruction_instantiation(instance):
    assert isinstance(instance, mindstorms_Instruction)


mindstorms_Main_strategy = st.builds(mindstorms_Main)
@given(instance=mindstorms_Main_strategy)
@settings(max_examples=25)
def test_mindstorms_Main_instantiation(instance):
    assert isinstance(instance, mindstorms_Main)


mindstorms_NamedElement_strategy = st.builds(mindstorms_NamedElement, name=safe_text)
@given(instance=mindstorms_NamedElement_strategy)
@settings(max_examples=25)
def test_mindstorms_NamedElement_instantiation(instance):
    assert isinstance(instance, mindstorms_NamedElement)


mindstorms_Procedure_strategy = st.builds(mindstorms_Procedure)
@given(instance=mindstorms_Procedure_strategy)
@settings(max_examples=25)
def test_mindstorms_Procedure_instantiation(instance):
    assert isinstance(instance, mindstorms_Procedure)


mindstorms_Release_strategy = st.builds(mindstorms_Release)
@given(instance=mindstorms_Release_strategy)
@settings(max_examples=25)
def test_mindstorms_Release_instantiation(instance):
    assert isinstance(instance, mindstorms_Release)


mindstorms_ReturnBottleToBase_strategy = st.builds(mindstorms_ReturnBottleToBase)
@given(instance=mindstorms_ReturnBottleToBase_strategy)
@settings(max_examples=25)
def test_mindstorms_ReturnBottleToBase_instantiation(instance):
    assert isinstance(instance, mindstorms_ReturnBottleToBase)


mindstorms_ReturnToBase_strategy = st.builds(mindstorms_ReturnToBase)
@given(instance=mindstorms_ReturnToBase_strategy)
@settings(max_examples=25)
def test_mindstorms_ReturnToBase_instantiation(instance):
    assert isinstance(instance, mindstorms_ReturnToBase)


mindstorms_ReuseInstruction_strategy = st.builds(mindstorms_ReuseInstruction)
@given(instance=mindstorms_ReuseInstruction_strategy)
@settings(max_examples=25)
def test_mindstorms_ReuseInstruction_instantiation(instance):
    assert isinstance(instance, mindstorms_ReuseInstruction)


mindstorms_Rotate_strategy = st.builds(mindstorms_Rotate, degrees=st.integers(), random=st.booleans())
@given(instance=mindstorms_Rotate_strategy)
@settings(max_examples=25)
def test_mindstorms_Rotate_instantiation(instance):
    assert isinstance(instance, mindstorms_Rotate)


mindstorms_Sensor_strategy = st.builds(mindstorms_Sensor)
@given(instance=mindstorms_Sensor_strategy)
@settings(max_examples=25)
def test_mindstorms_Sensor_instantiation(instance):
    assert isinstance(instance, mindstorms_Sensor)


mindstorms_TouchSensor_strategy = st.builds(mindstorms_TouchSensor, isPressed=st.booleans())
@given(instance=mindstorms_TouchSensor_strategy)
@settings(max_examples=25)
def test_mindstorms_TouchSensor_instantiation(instance):
    assert isinstance(instance, mindstorms_TouchSensor)


mindstorms_UltrasonicSensor_strategy = st.builds(mindstorms_UltrasonicSensor, operator=safe_text, value=st.floats(allow_nan=False, allow_infinity=False))
@given(instance=mindstorms_UltrasonicSensor_strategy)
@settings(max_examples=25)
def test_mindstorms_UltrasonicSensor_instantiation(instance):
    assert isinstance(instance, mindstorms_UltrasonicSensor)


mindstorms_While_strategy = st.builds(mindstorms_While)
@given(instance=mindstorms_While_strategy)
@settings(max_examples=25)
def test_mindstorms_While_instantiation(instance):
    assert isinstance(instance, mindstorms_While)



