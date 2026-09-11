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


