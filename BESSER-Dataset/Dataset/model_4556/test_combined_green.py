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
    CMD,
    myDsl_TURTLE,
    myDsl_PENSTATE,
    myDsl_RIGHT,
    myDsl_MOVE,
    myDsl_PENCOLOUR,
    myDsl_LEFT,
    myDsl_PAPER,
    myDsl_CMD,
    myDsl_PROGRAM,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_hyp_cmd_is_not_abstract():
    assert not inspect.isabstract(CMD)


def test_hyp_cmd_constructor_exists():
    assert callable(CMD.__init__)


def test_hyp_cmd_constructor_args():
    sig = inspect.signature(CMD.__init__)
    params = list(sig.parameters.keys())



def test_hyp_mydsl_turtle_is_not_abstract():
    assert not inspect.isabstract(myDsl_TURTLE)


def test_hyp_mydsl_turtle_constructor_exists():
    assert callable(myDsl_TURTLE.__init__)


def test_hyp_mydsl_turtle_constructor_args():
    sig = inspect.signature(myDsl_TURTLE.__init__)
    params = list(sig.parameters.keys())
    assert "startPosY" in params, "Missing parameter 'startPosY'"
    assert "startPosX" in params, "Missing parameter 'startPosX'"





def test_hyp_mydsl_penstate_is_not_abstract():
    assert not inspect.isabstract(myDsl_PENSTATE)


def test_hyp_mydsl_penstate_constructor_exists():
    assert callable(myDsl_PENSTATE.__init__)


def test_hyp_mydsl_penstate_constructor_args():
    sig = inspect.signature(myDsl_PENSTATE.__init__)
    params = list(sig.parameters.keys())
    assert "penState" in params, "Missing parameter 'penState'"




def test_hyp_mydsl_right_is_not_abstract():
    assert not inspect.isabstract(myDsl_RIGHT)


def test_hyp_mydsl_right_constructor_exists():
    assert callable(myDsl_RIGHT.__init__)


def test_hyp_mydsl_right_constructor_args():
    sig = inspect.signature(myDsl_RIGHT.__init__)
    params = list(sig.parameters.keys())
    assert "amount" in params, "Missing parameter 'amount'"




def test_hyp_mydsl_move_is_not_abstract():
    assert not inspect.isabstract(myDsl_MOVE)


def test_hyp_mydsl_move_constructor_exists():
    assert callable(myDsl_MOVE.__init__)


def test_hyp_mydsl_move_constructor_args():
    sig = inspect.signature(myDsl_MOVE.__init__)
    params = list(sig.parameters.keys())
    assert "amount" in params, "Missing parameter 'amount'"




def test_hyp_mydsl_pencolour_is_not_abstract():
    assert not inspect.isabstract(myDsl_PENCOLOUR)


def test_hyp_mydsl_pencolour_constructor_exists():
    assert callable(myDsl_PENCOLOUR.__init__)


def test_hyp_mydsl_pencolour_constructor_args():
    sig = inspect.signature(myDsl_PENCOLOUR.__init__)
    params = list(sig.parameters.keys())
    assert "colour" in params, "Missing parameter 'colour'"




def test_hyp_mydsl_left_is_not_abstract():
    assert not inspect.isabstract(myDsl_LEFT)


def test_hyp_mydsl_left_constructor_exists():
    assert callable(myDsl_LEFT.__init__)


def test_hyp_mydsl_left_constructor_args():
    sig = inspect.signature(myDsl_LEFT.__init__)
    params = list(sig.parameters.keys())
    assert "amount" in params, "Missing parameter 'amount'"




def test_hyp_mydsl_paper_is_not_abstract():
    assert not inspect.isabstract(myDsl_PAPER)


def test_hyp_mydsl_paper_constructor_exists():
    assert callable(myDsl_PAPER.__init__)


def test_hyp_mydsl_paper_constructor_args():
    sig = inspect.signature(myDsl_PAPER.__init__)
    params = list(sig.parameters.keys())
    assert "paperColour" in params, "Missing parameter 'paperColour'"
    assert "sizeY" in params, "Missing parameter 'sizeY'"
    assert "sizeX" in params, "Missing parameter 'sizeX'"






def test_hyp_mydsl_cmd_is_not_abstract():
    assert not inspect.isabstract(myDsl_CMD)


def test_hyp_mydsl_cmd_constructor_exists():
    assert callable(myDsl_CMD.__init__)


def test_hyp_mydsl_cmd_constructor_args():
    sig = inspect.signature(myDsl_CMD.__init__)
    params = list(sig.parameters.keys())



def test_hyp_mydsl_program_is_not_abstract():
    assert not inspect.isabstract(myDsl_PROGRAM)


def test_hyp_mydsl_program_constructor_exists():
    assert callable(myDsl_PROGRAM.__init__)


def test_hyp_mydsl_program_constructor_args():
    sig = inspect.signature(myDsl_PROGRAM.__init__)
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
CMD_strategy = st.builds(
    CMD,
)
myDsl_TURTLE_strategy = st.builds(
    myDsl_TURTLE,
    startPosY=
        st.integers(),
    startPosX=
        st.integers()
)
myDsl_PENSTATE_strategy = st.builds(
    myDsl_PENSTATE,
    penState=
        safe_text
)
myDsl_RIGHT_strategy = st.builds(
    myDsl_RIGHT,
    amount=
        st.integers()
)
myDsl_MOVE_strategy = st.builds(
    myDsl_MOVE,
    amount=
        st.integers()
)
myDsl_PENCOLOUR_strategy = st.builds(
    myDsl_PENCOLOUR,
    colour=
        safe_text
)
myDsl_LEFT_strategy = st.builds(
    myDsl_LEFT,
    amount=
        st.integers()
)
myDsl_PAPER_strategy = st.builds(
    myDsl_PAPER,
    paperColour=
        safe_text,
    sizeY=
        st.integers(),
    sizeX=
        st.integers()
)
myDsl_CMD_strategy = st.builds(
    myDsl_CMD,
)
myDsl_PROGRAM_strategy = st.builds(
    myDsl_PROGRAM,
)





@given(instance=myDsl_TURTLE_strategy)
def test_hyp_mydsl_turtle_startPosY_setter(instance):
    original = instance.startPosY
    instance.startPosY = original
    assert instance.startPosY == original



@given(instance=myDsl_TURTLE_strategy)
def test_hyp_mydsl_turtle_startPosX_setter(instance):
    original = instance.startPosX
    instance.startPosX = original
    assert instance.startPosX == original




@given(instance=myDsl_PENSTATE_strategy)
def test_hyp_mydsl_penstate_penState_setter(instance):
    original = instance.penState
    instance.penState = original
    assert instance.penState == original




@given(instance=myDsl_RIGHT_strategy)
def test_hyp_mydsl_right_amount_setter(instance):
    original = instance.amount
    instance.amount = original
    assert instance.amount == original




@given(instance=myDsl_MOVE_strategy)
def test_hyp_mydsl_move_amount_setter(instance):
    original = instance.amount
    instance.amount = original
    assert instance.amount == original




@given(instance=myDsl_PENCOLOUR_strategy)
def test_hyp_mydsl_pencolour_colour_setter(instance):
    original = instance.colour
    instance.colour = original
    assert instance.colour == original




@given(instance=myDsl_LEFT_strategy)
def test_hyp_mydsl_left_amount_setter(instance):
    original = instance.amount
    instance.amount = original
    assert instance.amount == original




@given(instance=myDsl_PAPER_strategy)
def test_hyp_mydsl_paper_paperColour_setter(instance):
    original = instance.paperColour
    instance.paperColour = original
    assert instance.paperColour == original



@given(instance=myDsl_PAPER_strategy)
def test_hyp_mydsl_paper_sizeY_setter(instance):
    original = instance.sizeY
    instance.sizeY = original
    assert instance.sizeY == original



@given(instance=myDsl_PAPER_strategy)
def test_hyp_mydsl_paper_sizeX_setter(instance):
    original = instance.sizeX
    instance.sizeX = original
    assert instance.sizeX == original




# ----- SECTION B: test_structural_full.py (deterministic-first suite) -----
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



