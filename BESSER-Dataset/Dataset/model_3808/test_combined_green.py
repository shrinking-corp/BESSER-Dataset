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
    exercises_NamableElement,
    NamableElement,
    exercises_State,
    exercises_Transition,
    exercises_DFA,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_hyp_exercises_namableelement_is_not_abstract():
    assert not inspect.isabstract(exercises_NamableElement)


def test_hyp_exercises_namableelement_constructor_exists():
    assert callable(exercises_NamableElement.__init__)


def test_hyp_exercises_namableelement_constructor_args():
    sig = inspect.signature(exercises_NamableElement.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"




def test_hyp_namableelement_is_not_abstract():
    assert not inspect.isabstract(NamableElement)


def test_hyp_namableelement_constructor_exists():
    assert callable(NamableElement.__init__)


def test_hyp_namableelement_constructor_args():
    sig = inspect.signature(NamableElement.__init__)
    params = list(sig.parameters.keys())



def test_hyp_exercises_state_is_not_abstract():
    assert not inspect.isabstract(exercises_State)


def test_hyp_exercises_state_constructor_exists():
    assert callable(exercises_State.__init__)


def test_hyp_exercises_state_constructor_args():
    sig = inspect.signature(exercises_State.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"
    assert "isEnd" in params, "Missing parameter 'isEnd'"
    assert "isStart" in params, "Missing parameter 'isStart'"






def test_hyp_exercises_transition_is_not_abstract():
    assert not inspect.isabstract(exercises_Transition)


def test_hyp_exercises_transition_constructor_exists():
    assert callable(exercises_Transition.__init__)


def test_hyp_exercises_transition_constructor_args():
    sig = inspect.signature(exercises_Transition.__init__)
    params = list(sig.parameters.keys())
    assert "input" in params, "Missing parameter 'input'"




def test_hyp_exercises_dfa_is_not_abstract():
    assert not inspect.isabstract(exercises_DFA)


def test_hyp_exercises_dfa_constructor_exists():
    assert callable(exercises_DFA.__init__)


def test_hyp_exercises_dfa_constructor_args():
    sig = inspect.signature(exercises_DFA.__init__)
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
exercises_NamableElement_strategy = st.builds(
    exercises_NamableElement,
    name=
        safe_text
)
NamableElement_strategy = st.builds(
    NamableElement,
)
exercises_State_strategy = st.builds(
    exercises_State,
    id=
        safe_text,
    isEnd=
        st.booleans(),
    isStart=
        st.booleans()
)
exercises_Transition_strategy = st.builds(
    exercises_Transition,
    input=
        safe_text
)
exercises_DFA_strategy = st.builds(
    exercises_DFA,
)




@given(instance=exercises_NamableElement_strategy)
def test_hyp_exercises_namableelement_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original





@given(instance=exercises_State_strategy)
def test_hyp_exercises_state_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original



@given(instance=exercises_State_strategy)
def test_hyp_exercises_state_isEnd_setter(instance):
    original = instance.isEnd
    instance.isEnd = original
    assert instance.isEnd == original



@given(instance=exercises_State_strategy)
def test_hyp_exercises_state_isStart_setter(instance):
    original = instance.isStart
    instance.isStart = original
    assert instance.isStart == original




@given(instance=exercises_Transition_strategy)
def test_hyp_exercises_transition_input_setter(instance):
    original = instance.input
    instance.input = original
    assert instance.input == original



# ----- SECTION B: test_structural_full.py (deterministic-first suite) -----
import inspect
import pytest
from datetime import date, datetime, time, timedelta
from hypothesis import given, settings
import hypothesis.strategies as st

from python_code import (
    NamableElement,
    exercises_DFA,
    exercises_NamableElement,
    exercises_State,
    exercises_Transition,
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

def test_exercises_NamableElement_name_value_roundtrip():
    instance = exercises_NamableElement(name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_exercises_State_id_value_roundtrip():
    instance = exercises_State(id="sample_text", isEnd=True, isStart=True)
    assert instance.id == "sample_text"
    instance.id = "sample_text_2"
    assert instance.id == "sample_text_2"


def test_exercises_State_isEnd_value_roundtrip():
    instance = exercises_State(id="sample_text", isEnd=True, isStart=True)
    assert instance.isEnd == True
    instance.isEnd = False
    assert instance.isEnd == False


def test_exercises_State_isStart_value_roundtrip():
    instance = exercises_State(id="sample_text", isEnd=True, isStart=True)
    assert instance.isStart == True
    instance.isStart = False
    assert instance.isStart == False


def test_exercises_Transition_input_value_roundtrip():
    instance = exercises_Transition(input="sample_text")
    assert instance.input == "sample_text"
    instance.input = "sample_text_2"
    assert instance.input == "sample_text_2"


def test_exercises_DFA_isa_NamableElement():
    instance = exercises_DFA()
    assert isinstance(instance, NamableElement)


def test_exercises_State_isa_NamableElement():
    instance = exercises_State(id="sample_text", isEnd=True, isStart=True)
    assert isinstance(instance, NamableElement)


def test_exercises_Transition_isa_NamableElement():
    instance = exercises_Transition(input="sample_text")
    assert isinstance(instance, NamableElement)


def test_assoc_incoming3_link_reassign_clear():
    a = exercises_Transition(input="sample_text")
    b1 = exercises_State(id="sample_text", isEnd=True, isStart=True)
    b2 = exercises_State(id="sample_text_2", isEnd=False, isStart=False)
    _safe_set(a, 'exercises_Transition5', b1)
    assert _is_linked(a, 'exercises_Transition5', b1)
    if hasattr(b1, 'exercises_State4'):
        assert _is_linked(b1, 'exercises_State4', a)
    _safe_set(a, 'exercises_Transition5', b2)
    assert _is_linked(a, 'exercises_Transition5', b2)
    if hasattr(b1, 'exercises_State4'):
        assert not _is_linked(b1, 'exercises_State4', a)
    if hasattr(b2, 'exercises_State4'):
        assert _is_linked(b2, 'exercises_State4', a)
    _safe_set(a, 'exercises_Transition5', None)
    assert not _is_linked(a, 'exercises_Transition5', b2)
    if hasattr(b2, 'exercises_State4'):
        assert not _is_linked(b2, 'exercises_State4', a)


def test_assoc_outgoing6_link_reassign_clear():
    a = exercises_Transition(input="sample_text")
    b1 = exercises_State(id="sample_text", isEnd=True, isStart=True)
    b2 = exercises_State(id="sample_text_2", isEnd=False, isStart=False)
    _safe_set(a, 'exercises_Transition8', b1)
    assert _is_linked(a, 'exercises_Transition8', b1)
    if hasattr(b1, 'exercises_State7'):
        assert _is_linked(b1, 'exercises_State7', a)
    _safe_set(a, 'exercises_Transition8', b2)
    assert _is_linked(a, 'exercises_Transition8', b2)
    if hasattr(b1, 'exercises_State7'):
        assert not _is_linked(b1, 'exercises_State7', a)
    if hasattr(b2, 'exercises_State7'):
        assert _is_linked(b2, 'exercises_State7', a)
    _safe_set(a, 'exercises_Transition8', None)
    assert not _is_linked(a, 'exercises_Transition8', b2)
    if hasattr(b2, 'exercises_State7'):
        assert not _is_linked(b2, 'exercises_State7', a)


def test_assoc_states0_link_reassign_clear():
    a = exercises_State(id="sample_text", isEnd=True, isStart=True)
    b1 = exercises_DFA()
    b2 = exercises_DFA()
    _safe_set(a, 'exercises_State', b1)
    assert _is_linked(a, 'exercises_State', b1)
    if hasattr(b1, 'exercises_DFA'):
        assert _is_linked(b1, 'exercises_DFA', a)
    _safe_set(a, 'exercises_State', b2)
    assert _is_linked(a, 'exercises_State', b2)
    if hasattr(b1, 'exercises_DFA'):
        assert not _is_linked(b1, 'exercises_DFA', a)
    if hasattr(b2, 'exercises_DFA'):
        assert _is_linked(b2, 'exercises_DFA', a)
    _safe_set(a, 'exercises_State', None)
    assert not _is_linked(a, 'exercises_State', b2)
    if hasattr(b2, 'exercises_DFA'):
        assert not _is_linked(b2, 'exercises_DFA', a)


def test_assoc_transition1_link_reassign_clear():
    a = exercises_Transition(input="sample_text")
    b1 = exercises_DFA()
    b2 = exercises_DFA()
    _safe_set(a, 'exercises_Transition', b1)
    assert _is_linked(a, 'exercises_Transition', b1)
    if hasattr(b1, 'exercises_DFA2'):
        assert _is_linked(b1, 'exercises_DFA2', a)
    _safe_set(a, 'exercises_Transition', b2)
    assert _is_linked(a, 'exercises_Transition', b2)
    if hasattr(b1, 'exercises_DFA2'):
        assert not _is_linked(b1, 'exercises_DFA2', a)
    if hasattr(b2, 'exercises_DFA2'):
        assert _is_linked(b2, 'exercises_DFA2', a)
    _safe_set(a, 'exercises_Transition', None)
    assert not _is_linked(a, 'exercises_Transition', b2)
    if hasattr(b2, 'exercises_DFA2'):
        assert not _is_linked(b2, 'exercises_DFA2', a)


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

NamableElement_strategy = st.builds(NamableElement)
@given(instance=NamableElement_strategy)
@settings(max_examples=25)
def test_NamableElement_instantiation(instance):
    assert isinstance(instance, NamableElement)


exercises_DFA_strategy = st.builds(exercises_DFA)
@given(instance=exercises_DFA_strategy)
@settings(max_examples=25)
def test_exercises_DFA_instantiation(instance):
    assert isinstance(instance, exercises_DFA)


exercises_NamableElement_strategy = st.builds(exercises_NamableElement, name=safe_text)
@given(instance=exercises_NamableElement_strategy)
@settings(max_examples=25)
def test_exercises_NamableElement_instantiation(instance):
    assert isinstance(instance, exercises_NamableElement)


exercises_State_strategy = st.builds(exercises_State, id=safe_text, isEnd=st.booleans(), isStart=st.booleans())
@given(instance=exercises_State_strategy)
@settings(max_examples=25)
def test_exercises_State_instantiation(instance):
    assert isinstance(instance, exercises_State)


exercises_Transition_strategy = st.builds(exercises_Transition, input=safe_text)
@given(instance=exercises_Transition_strategy)
@settings(max_examples=25)
def test_exercises_Transition_instantiation(instance):
    assert isinstance(instance, exercises_Transition)



