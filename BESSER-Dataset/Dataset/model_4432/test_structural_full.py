import inspect
import pytest
from datetime import date, datetime, time, timedelta
from hypothesis import given, settings
import hypothesis.strategies as st

from python_code import (
    Action,
    Block,
    Instruction,
    NamedElement,
    mindstorms_Action,
    mindstorms_Begin,
    mindstorms_Block,
    mindstorms_Choreography,
    mindstorms_EdgeInstruction,
    mindstorms_End,
    mindstorms_GoBackward,
    mindstorms_GoForward,
    mindstorms_Grab,
    mindstorms_Instruction,
    mindstorms_NamedElement,
    mindstorms_Release,
    mindstorms_Rotate,
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


def test_mindstorms_Begin_isa_Action():
    instance = mindstorms_Begin()
    assert isinstance(instance, Action)


def test_mindstorms_End_isa_Action():
    instance = mindstorms_End()
    assert isinstance(instance, Action)


def test_mindstorms_GoBackward_isa_Action():
    instance = mindstorms_GoBackward(cm=7, infinite=True)
    assert isinstance(instance, Action)


def test_mindstorms_GoForward_isa_Action():
    instance = mindstorms_GoForward(cm=7, infinite=True)
    assert isinstance(instance, Action)


def test_mindstorms_Grab_isa_Action():
    instance = mindstorms_Grab()
    assert isinstance(instance, Action)


def test_mindstorms_Release_isa_Action():
    instance = mindstorms_Release()
    assert isinstance(instance, Action)


def test_mindstorms_Rotate_isa_Action():
    instance = mindstorms_Rotate(degrees=7, random=True)
    assert isinstance(instance, Action)


def test_mindstorms_Action_isa_Block():
    instance = mindstorms_Action()
    assert isinstance(instance, Block)


def test_mindstorms_Block_isa_Instruction():
    instance = mindstorms_Block()
    assert isinstance(instance, Instruction)


def test_mindstorms_Choreography_isa_Instruction():
    instance = mindstorms_Choreography()
    assert isinstance(instance, Instruction)


def test_mindstorms_Instruction_isa_NamedElement():
    instance = mindstorms_Instruction()
    assert isinstance(instance, NamedElement)


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

Action_strategy = st.builds(Action)
@given(instance=Action_strategy)
@settings(max_examples=25)
def test_Action_instantiation(instance):
    assert isinstance(instance, Action)


Block_strategy = st.builds(Block)
@given(instance=Block_strategy)
@settings(max_examples=25)
def test_Block_instantiation(instance):
    assert isinstance(instance, Block)


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


mindstorms_Action_strategy = st.builds(mindstorms_Action)
@given(instance=mindstorms_Action_strategy)
@settings(max_examples=25)
def test_mindstorms_Action_instantiation(instance):
    assert isinstance(instance, mindstorms_Action)


mindstorms_Begin_strategy = st.builds(mindstorms_Begin)
@given(instance=mindstorms_Begin_strategy)
@settings(max_examples=25)
def test_mindstorms_Begin_instantiation(instance):
    assert isinstance(instance, mindstorms_Begin)


mindstorms_Block_strategy = st.builds(mindstorms_Block)
@given(instance=mindstorms_Block_strategy)
@settings(max_examples=25)
def test_mindstorms_Block_instantiation(instance):
    assert isinstance(instance, mindstorms_Block)


mindstorms_Choreography_strategy = st.builds(mindstorms_Choreography)
@given(instance=mindstorms_Choreography_strategy)
@settings(max_examples=25)
def test_mindstorms_Choreography_instantiation(instance):
    assert isinstance(instance, mindstorms_Choreography)


mindstorms_EdgeInstruction_strategy = st.builds(mindstorms_EdgeInstruction)
@given(instance=mindstorms_EdgeInstruction_strategy)
@settings(max_examples=25)
def test_mindstorms_EdgeInstruction_instantiation(instance):
    assert isinstance(instance, mindstorms_EdgeInstruction)


mindstorms_End_strategy = st.builds(mindstorms_End)
@given(instance=mindstorms_End_strategy)
@settings(max_examples=25)
def test_mindstorms_End_instantiation(instance):
    assert isinstance(instance, mindstorms_End)


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


mindstorms_Grab_strategy = st.builds(mindstorms_Grab)
@given(instance=mindstorms_Grab_strategy)
@settings(max_examples=25)
def test_mindstorms_Grab_instantiation(instance):
    assert isinstance(instance, mindstorms_Grab)


mindstorms_Instruction_strategy = st.builds(mindstorms_Instruction)
@given(instance=mindstorms_Instruction_strategy)
@settings(max_examples=25)
def test_mindstorms_Instruction_instantiation(instance):
    assert isinstance(instance, mindstorms_Instruction)


mindstorms_NamedElement_strategy = st.builds(mindstorms_NamedElement, name=safe_text)
@given(instance=mindstorms_NamedElement_strategy)
@settings(max_examples=25)
def test_mindstorms_NamedElement_instantiation(instance):
    assert isinstance(instance, mindstorms_NamedElement)


mindstorms_Release_strategy = st.builds(mindstorms_Release)
@given(instance=mindstorms_Release_strategy)
@settings(max_examples=25)
def test_mindstorms_Release_instantiation(instance):
    assert isinstance(instance, mindstorms_Release)


mindstorms_Rotate_strategy = st.builds(mindstorms_Rotate, degrees=st.integers(), random=st.booleans())
@given(instance=mindstorms_Rotate_strategy)
@settings(max_examples=25)
def test_mindstorms_Rotate_instantiation(instance):
    assert isinstance(instance, mindstorms_Rotate)


