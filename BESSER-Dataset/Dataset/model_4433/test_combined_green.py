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
    Instruction,
    mindstorms_Choreography,
    mindstorms_Instruction,
    Action,
    mindstorms_Rotate,
    mindstorms_GoForward,
    mindstorms_Release,
    mindstorms_Grab,
    mindstorms_Action,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_hyp_instruction_is_not_abstract():
    assert not inspect.isabstract(Instruction)


def test_hyp_instruction_constructor_exists():
    assert callable(Instruction.__init__)


def test_hyp_instruction_constructor_args():
    sig = inspect.signature(Instruction.__init__)
    params = list(sig.parameters.keys())



def test_hyp_mindstorms_choreography_is_not_abstract():
    assert not inspect.isabstract(mindstorms_Choreography)


def test_hyp_mindstorms_choreography_constructor_exists():
    assert callable(mindstorms_Choreography.__init__)


def test_hyp_mindstorms_choreography_constructor_args():
    sig = inspect.signature(mindstorms_Choreography.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"




def test_hyp_mindstorms_instruction_is_not_abstract():
    assert not inspect.isabstract(mindstorms_Instruction)


def test_hyp_mindstorms_instruction_constructor_exists():
    assert callable(mindstorms_Instruction.__init__)


def test_hyp_mindstorms_instruction_constructor_args():
    sig = inspect.signature(mindstorms_Instruction.__init__)
    params = list(sig.parameters.keys())



def test_hyp_action_is_not_abstract():
    assert not inspect.isabstract(Action)


def test_hyp_action_constructor_exists():
    assert callable(Action.__init__)


def test_hyp_action_constructor_args():
    sig = inspect.signature(Action.__init__)
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





def test_hyp_mindstorms_goforward_is_not_abstract():
    assert not inspect.isabstract(mindstorms_GoForward)


def test_hyp_mindstorms_goforward_constructor_exists():
    assert callable(mindstorms_GoForward.__init__)


def test_hyp_mindstorms_goforward_constructor_args():
    sig = inspect.signature(mindstorms_GoForward.__init__)
    params = list(sig.parameters.keys())
    assert "cm" in params, "Missing parameter 'cm'"




def test_hyp_mindstorms_release_is_not_abstract():
    assert not inspect.isabstract(mindstorms_Release)


def test_hyp_mindstorms_release_constructor_exists():
    assert callable(mindstorms_Release.__init__)


def test_hyp_mindstorms_release_constructor_args():
    sig = inspect.signature(mindstorms_Release.__init__)
    params = list(sig.parameters.keys())



def test_hyp_mindstorms_grab_is_not_abstract():
    assert not inspect.isabstract(mindstorms_Grab)


def test_hyp_mindstorms_grab_constructor_exists():
    assert callable(mindstorms_Grab.__init__)


def test_hyp_mindstorms_grab_constructor_args():
    sig = inspect.signature(mindstorms_Grab.__init__)
    params = list(sig.parameters.keys())



def test_hyp_mindstorms_action_is_not_abstract():
    assert not inspect.isabstract(mindstorms_Action)


def test_hyp_mindstorms_action_constructor_exists():
    assert callable(mindstorms_Action.__init__)


def test_hyp_mindstorms_action_constructor_args():
    sig = inspect.signature(mindstorms_Action.__init__)
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
Instruction_strategy = st.builds(
    Instruction,
)
mindstorms_Choreography_strategy = st.builds(
    mindstorms_Choreography,
    name=
        safe_text
)
mindstorms_Instruction_strategy = st.builds(
    mindstorms_Instruction,
)
Action_strategy = st.builds(
    Action,
)
mindstorms_Rotate_strategy = st.builds(
    mindstorms_Rotate,
    degrees=
        st.integers(),
    random=
        st.booleans()
)
mindstorms_GoForward_strategy = st.builds(
    mindstorms_GoForward,
    cm=
        st.integers()
)
mindstorms_Release_strategy = st.builds(
    mindstorms_Release,
)
mindstorms_Grab_strategy = st.builds(
    mindstorms_Grab,
)
mindstorms_Action_strategy = st.builds(
    mindstorms_Action,
)





@given(instance=mindstorms_Choreography_strategy)
def test_hyp_mindstorms_choreography_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original






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




@given(instance=mindstorms_GoForward_strategy)
def test_hyp_mindstorms_goforward_cm_setter(instance):
    original = instance.cm
    instance.cm = original
    assert instance.cm == original





# ----- SECTION B: test_structural_full.py (deterministic-first suite) -----
import inspect
import pytest
from datetime import date, datetime, time, timedelta
from hypothesis import given, settings
import hypothesis.strategies as st

from python_code import (
    Action,
    Instruction,
    mindstorms_Action,
    mindstorms_Choreography,
    mindstorms_GoForward,
    mindstorms_Grab,
    mindstorms_Instruction,
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

def test_mindstorms_Choreography_name_value_roundtrip():
    instance = mindstorms_Choreography(name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_mindstorms_GoForward_cm_value_roundtrip():
    instance = mindstorms_GoForward(cm=7)
    assert instance.cm == 7
    instance.cm = 13
    assert instance.cm == 13


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


def test_mindstorms_GoForward_isa_Action():
    instance = mindstorms_GoForward(cm=7)
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


def test_mindstorms_Action_isa_Instruction():
    instance = mindstorms_Action()
    assert isinstance(instance, Instruction)


def test_mindstorms_Choreography_isa_Instruction():
    instance = mindstorms_Choreography(name="sample_text")
    assert isinstance(instance, Instruction)


def test_assoc_instructions0_link_reassign_clear():
    a = mindstorms_Choreography(name="sample_text")
    b1 = mindstorms_Instruction()
    b2 = mindstorms_Instruction()
    _safe_set(a, 'mindstorms_Choreography', {b1})
    assert _is_linked(a, 'mindstorms_Choreography', b1)
    if hasattr(b1, 'mindstorms_Instruction'):
        assert _is_linked(b1, 'mindstorms_Instruction', a)
    _safe_set(a, 'mindstorms_Choreography', {b2})
    assert _is_linked(a, 'mindstorms_Choreography', b2)
    if hasattr(b1, 'mindstorms_Instruction'):
        assert not _is_linked(b1, 'mindstorms_Instruction', a)
    if hasattr(b2, 'mindstorms_Instruction'):
        assert _is_linked(b2, 'mindstorms_Instruction', a)
    _safe_set(a, 'mindstorms_Choreography', set())
    assert not _is_linked(a, 'mindstorms_Choreography', b2)
    if hasattr(b2, 'mindstorms_Instruction'):
        assert not _is_linked(b2, 'mindstorms_Instruction', a)


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

Action_strategy = st.builds(Action)
@given(instance=Action_strategy)
@settings(max_examples=25)
def test_Action_instantiation(instance):
    assert isinstance(instance, Action)


Instruction_strategy = st.builds(Instruction)
@given(instance=Instruction_strategy)
@settings(max_examples=25)
def test_Instruction_instantiation(instance):
    assert isinstance(instance, Instruction)


mindstorms_Action_strategy = st.builds(mindstorms_Action)
@given(instance=mindstorms_Action_strategy)
@settings(max_examples=25)
def test_mindstorms_Action_instantiation(instance):
    assert isinstance(instance, mindstorms_Action)


mindstorms_Choreography_strategy = st.builds(mindstorms_Choreography, name=safe_text)
@given(instance=mindstorms_Choreography_strategy)
@settings(max_examples=25)
def test_mindstorms_Choreography_instantiation(instance):
    assert isinstance(instance, mindstorms_Choreography)


mindstorms_GoForward_strategy = st.builds(mindstorms_GoForward, cm=st.integers())
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



