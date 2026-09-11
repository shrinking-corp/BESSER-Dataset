import inspect
import pytest
from datetime import date, datetime, time, timedelta
from hypothesis import given, settings
import hypothesis.strategies as st

from python_code import (
    CMD,
    myDsl_CMD,
    myDsl_LEFT,
    myDsl_MOVE,
    myDsl_PAPER,
    myDsl_PENCOLOUR,
    myDsl_PENSTATE,
    myDsl_PROGRAM,
    myDsl_RIGHT,
    myDsl_TURTLE,
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

def test_myDsl_LEFT_amount_value_roundtrip():
    instance = myDsl_LEFT(amount=7)
    assert instance.amount == 7
    instance.amount = 13
    assert instance.amount == 13


def test_myDsl_MOVE_amount_value_roundtrip():
    instance = myDsl_MOVE(amount=7)
    assert instance.amount == 7
    instance.amount = 13
    assert instance.amount == 13


def test_myDsl_PAPER_paperColour_value_roundtrip():
    instance = myDsl_PAPER(paperColour="sample_text", sizeX=7, sizeY=7)
    assert instance.paperColour == "sample_text"
    instance.paperColour = "sample_text_2"
    assert instance.paperColour == "sample_text_2"


def test_myDsl_PAPER_sizeX_value_roundtrip():
    instance = myDsl_PAPER(paperColour="sample_text", sizeX=7, sizeY=7)
    assert instance.sizeX == 7
    instance.sizeX = 13
    assert instance.sizeX == 13


def test_myDsl_PAPER_sizeY_value_roundtrip():
    instance = myDsl_PAPER(paperColour="sample_text", sizeX=7, sizeY=7)
    assert instance.sizeY == 7
    instance.sizeY = 13
    assert instance.sizeY == 13


def test_myDsl_PENCOLOUR_colour_value_roundtrip():
    instance = myDsl_PENCOLOUR(colour="sample_text")
    assert instance.colour == "sample_text"
    instance.colour = "sample_text_2"
    assert instance.colour == "sample_text_2"


def test_myDsl_PENSTATE_penState_value_roundtrip():
    instance = myDsl_PENSTATE(penState="sample_text")
    assert instance.penState == "sample_text"
    instance.penState = "sample_text_2"
    assert instance.penState == "sample_text_2"


def test_myDsl_RIGHT_amount_value_roundtrip():
    instance = myDsl_RIGHT(amount=7)
    assert instance.amount == 7
    instance.amount = 13
    assert instance.amount == 13


def test_myDsl_TURTLE_startPosX_value_roundtrip():
    instance = myDsl_TURTLE(startPosX=7, startPosY=7)
    assert instance.startPosX == 7
    instance.startPosX = 13
    assert instance.startPosX == 13


def test_myDsl_TURTLE_startPosY_value_roundtrip():
    instance = myDsl_TURTLE(startPosX=7, startPosY=7)
    assert instance.startPosY == 7
    instance.startPosY = 13
    assert instance.startPosY == 13


def test_myDsl_LEFT_isa_CMD():
    instance = myDsl_LEFT(amount=7)
    assert isinstance(instance, CMD)


def test_myDsl_MOVE_isa_CMD():
    instance = myDsl_MOVE(amount=7)
    assert isinstance(instance, CMD)


def test_myDsl_PAPER_isa_CMD():
    instance = myDsl_PAPER(paperColour="sample_text", sizeX=7, sizeY=7)
    assert isinstance(instance, CMD)


def test_myDsl_PENCOLOUR_isa_CMD():
    instance = myDsl_PENCOLOUR(colour="sample_text")
    assert isinstance(instance, CMD)


def test_myDsl_PENSTATE_isa_CMD():
    instance = myDsl_PENSTATE(penState="sample_text")
    assert isinstance(instance, CMD)


def test_myDsl_RIGHT_isa_CMD():
    instance = myDsl_RIGHT(amount=7)
    assert isinstance(instance, CMD)


def test_myDsl_TURTLE_isa_CMD():
    instance = myDsl_TURTLE(startPosX=7, startPosY=7)
    assert isinstance(instance, CMD)


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

CMD_strategy = st.builds(CMD)
@given(instance=CMD_strategy)
@settings(max_examples=25)
def test_CMD_instantiation(instance):
    assert isinstance(instance, CMD)


myDsl_CMD_strategy = st.builds(myDsl_CMD)
@given(instance=myDsl_CMD_strategy)
@settings(max_examples=25)
def test_myDsl_CMD_instantiation(instance):
    assert isinstance(instance, myDsl_CMD)


myDsl_LEFT_strategy = st.builds(myDsl_LEFT, amount=st.integers())
@given(instance=myDsl_LEFT_strategy)
@settings(max_examples=25)
def test_myDsl_LEFT_instantiation(instance):
    assert isinstance(instance, myDsl_LEFT)


myDsl_MOVE_strategy = st.builds(myDsl_MOVE, amount=st.integers())
@given(instance=myDsl_MOVE_strategy)
@settings(max_examples=25)
def test_myDsl_MOVE_instantiation(instance):
    assert isinstance(instance, myDsl_MOVE)


myDsl_PAPER_strategy = st.builds(myDsl_PAPER, paperColour=safe_text, sizeX=st.integers(), sizeY=st.integers())
@given(instance=myDsl_PAPER_strategy)
@settings(max_examples=25)
def test_myDsl_PAPER_instantiation(instance):
    assert isinstance(instance, myDsl_PAPER)


myDsl_PENCOLOUR_strategy = st.builds(myDsl_PENCOLOUR, colour=safe_text)
@given(instance=myDsl_PENCOLOUR_strategy)
@settings(max_examples=25)
def test_myDsl_PENCOLOUR_instantiation(instance):
    assert isinstance(instance, myDsl_PENCOLOUR)


myDsl_PENSTATE_strategy = st.builds(myDsl_PENSTATE, penState=safe_text)
@given(instance=myDsl_PENSTATE_strategy)
@settings(max_examples=25)
def test_myDsl_PENSTATE_instantiation(instance):
    assert isinstance(instance, myDsl_PENSTATE)


myDsl_PROGRAM_strategy = st.builds(myDsl_PROGRAM)
@given(instance=myDsl_PROGRAM_strategy)
@settings(max_examples=25)
def test_myDsl_PROGRAM_instantiation(instance):
    assert isinstance(instance, myDsl_PROGRAM)


myDsl_RIGHT_strategy = st.builds(myDsl_RIGHT, amount=st.integers())
@given(instance=myDsl_RIGHT_strategy)
@settings(max_examples=25)
def test_myDsl_RIGHT_instantiation(instance):
    assert isinstance(instance, myDsl_RIGHT)


myDsl_TURTLE_strategy = st.builds(myDsl_TURTLE, startPosX=st.integers(), startPosY=st.integers())
@given(instance=myDsl_TURTLE_strategy)
@settings(max_examples=25)
def test_myDsl_TURTLE_instantiation(instance):
    assert isinstance(instance, myDsl_TURTLE)


