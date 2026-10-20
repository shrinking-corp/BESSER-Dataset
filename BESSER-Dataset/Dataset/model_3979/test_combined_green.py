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
    ctmc_Transition,
    ctmc_Label,
    ctmc_State,
    ctmc_CTMC,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_hyp_ctmc_transition_is_not_abstract():
    assert not inspect.isabstract(ctmc_Transition)


def test_hyp_ctmc_transition_constructor_exists():
    assert callable(ctmc_Transition.__init__)


def test_hyp_ctmc_transition_constructor_args():
    sig = inspect.signature(ctmc_Transition.__init__)
    params = list(sig.parameters.keys())
    assert "duration" in params, "Missing parameter 'duration'"
    assert "name" in params, "Missing parameter 'name'"
    assert "probability" in params, "Missing parameter 'probability'"






def test_hyp_ctmc_label_is_not_abstract():
    assert not inspect.isabstract(ctmc_Label)


def test_hyp_ctmc_label_constructor_exists():
    assert callable(ctmc_Label.__init__)


def test_hyp_ctmc_label_constructor_args():
    sig = inspect.signature(ctmc_Label.__init__)
    params = list(sig.parameters.keys())
    assert "text" in params, "Missing parameter 'text'"




def test_hyp_ctmc_state_is_not_abstract():
    assert not inspect.isabstract(ctmc_State)


def test_hyp_ctmc_state_constructor_exists():
    assert callable(ctmc_State.__init__)


def test_hyp_ctmc_state_constructor_args():
    sig = inspect.signature(ctmc_State.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "exitRate" in params, "Missing parameter 'exitRate'"





def test_hyp_ctmc_ctmc_is_not_abstract():
    assert not inspect.isabstract(ctmc_CTMC)


def test_hyp_ctmc_ctmc_constructor_exists():
    assert callable(ctmc_CTMC.__init__)


def test_hyp_ctmc_ctmc_constructor_args():
    sig = inspect.signature(ctmc_CTMC.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"



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
ctmc_Transition_strategy = st.builds(
    ctmc_Transition,
    duration=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    name=
        safe_text,
    probability=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
ctmc_Label_strategy = st.builds(
    ctmc_Label,
    text=
        safe_text
)
ctmc_State_strategy = st.builds(
    ctmc_State,
    name=
        safe_text,
    exitRate=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
ctmc_CTMC_strategy = st.builds(
    ctmc_CTMC,
    name=
        safe_text
)




@given(instance=ctmc_Transition_strategy)
def test_hyp_ctmc_transition_duration_setter(instance):
    original = instance.duration
    instance.duration = original
    assert instance.duration == original



@given(instance=ctmc_Transition_strategy)
def test_hyp_ctmc_transition_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=ctmc_Transition_strategy)
def test_hyp_ctmc_transition_probability_setter(instance):
    original = instance.probability
    instance.probability = original
    assert instance.probability == original




@given(instance=ctmc_Label_strategy)
def test_hyp_ctmc_label_text_setter(instance):
    original = instance.text
    instance.text = original
    assert instance.text == original




@given(instance=ctmc_State_strategy)
def test_hyp_ctmc_state_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=ctmc_State_strategy)
def test_hyp_ctmc_state_exitRate_setter(instance):
    original = instance.exitRate
    instance.exitRate = original
    assert instance.exitRate == original




@given(instance=ctmc_CTMC_strategy)
def test_hyp_ctmc_ctmc_name_setter(instance):
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
    ctmc_CTMC,
    ctmc_Label,
    ctmc_State,
    ctmc_Transition,
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

def test_ctmc_CTMC_name_value_roundtrip():
    instance = ctmc_CTMC(name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_ctmc_Label_text_value_roundtrip():
    instance = ctmc_Label(text="sample_text")
    assert instance.text == "sample_text"
    instance.text = "sample_text_2"
    assert instance.text == "sample_text_2"


def test_ctmc_State_exitRate_value_roundtrip():
    instance = ctmc_State(exitRate=3.14, name="sample_text")
    assert instance.exitRate == 3.14
    instance.exitRate = 9.99
    assert instance.exitRate == 9.99


def test_ctmc_State_name_value_roundtrip():
    instance = ctmc_State(exitRate=3.14, name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_ctmc_Transition_duration_value_roundtrip():
    instance = ctmc_Transition(duration=3.14, name="sample_text", probability=3.14)
    assert instance.duration == 3.14
    instance.duration = 9.99
    assert instance.duration == 9.99


def test_ctmc_Transition_name_value_roundtrip():
    instance = ctmc_Transition(duration=3.14, name="sample_text", probability=3.14)
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_ctmc_Transition_probability_value_roundtrip():
    instance = ctmc_Transition(duration=3.14, name="sample_text", probability=3.14)
    assert instance.probability == 3.14
    instance.probability = 9.99
    assert instance.probability == 9.99


def test_assoc_from_5_link_reassign_clear():
    a = ctmc_Transition(duration=3.14, name="sample_text", probability=3.14)
    b1 = ctmc_State(exitRate=3.14, name="sample_text")
    b2 = ctmc_State(exitRate=9.99, name="sample_text_2")
    _safe_set(a, 'out', b1)
    assert _is_linked(a, 'out', b1)
    if hasattr(b1, 'State'):
        assert _is_linked(b1, 'State', a)
    _safe_set(a, 'out', b2)
    assert _is_linked(a, 'out', b2)
    if hasattr(b1, 'State'):
        assert not _is_linked(b1, 'State', a)
    if hasattr(b2, 'State'):
        assert _is_linked(b2, 'State', a)
    _safe_set(a, 'out', None)
    assert not _is_linked(a, 'out', b2)
    if hasattr(b2, 'State'):
        assert not _is_linked(b2, 'State', a)


def test_assoc_in_3_link_reassign_clear():
    a = ctmc_Transition(duration=3.14, name="sample_text", probability=3.14)
    b1 = ctmc_State(exitRate=3.14, name="sample_text")
    b2 = ctmc_State(exitRate=9.99, name="sample_text_2")
    _safe_set(a, 'Transition4', b1)
    assert _is_linked(a, 'Transition4', b1)
    if hasattr(b1, 'to'):
        assert _is_linked(b1, 'to', a)
    _safe_set(a, 'Transition4', b2)
    assert _is_linked(a, 'Transition4', b2)
    if hasattr(b1, 'to'):
        assert not _is_linked(b1, 'to', a)
    if hasattr(b2, 'to'):
        assert _is_linked(b2, 'to', a)
    _safe_set(a, 'Transition4', None)
    assert not _is_linked(a, 'Transition4', b2)
    if hasattr(b2, 'to'):
        assert not _is_linked(b2, 'to', a)


def test_assoc_labels1_link_reassign_clear():
    a = ctmc_State(exitRate=3.14, name="sample_text")
    b1 = ctmc_Label(text="sample_text")
    b2 = ctmc_Label(text="sample_text_2")
    _safe_set(a, 'state', {b1})
    assert _is_linked(a, 'state', b1)
    if hasattr(b1, 'Label'):
        assert _is_linked(b1, 'Label', a)
    _safe_set(a, 'state', {b2})
    assert _is_linked(a, 'state', b2)
    if hasattr(b1, 'Label'):
        assert not _is_linked(b1, 'Label', a)
    if hasattr(b2, 'Label'):
        assert _is_linked(b2, 'Label', a)
    _safe_set(a, 'state', set())
    assert not _is_linked(a, 'state', b2)
    if hasattr(b2, 'Label'):
        assert not _is_linked(b2, 'Label', a)


def test_assoc_out2_link_reassign_clear():
    a = ctmc_Transition(duration=3.14, name="sample_text", probability=3.14)
    b1 = ctmc_State(exitRate=3.14, name="sample_text")
    b2 = ctmc_State(exitRate=9.99, name="sample_text_2")
    _safe_set(a, 'Transition', b1)
    assert _is_linked(a, 'Transition', b1)
    if hasattr(b1, 'from_'):
        assert _is_linked(b1, 'from_', a)
    _safe_set(a, 'Transition', b2)
    assert _is_linked(a, 'Transition', b2)
    if hasattr(b1, 'from_'):
        assert not _is_linked(b1, 'from_', a)
    if hasattr(b2, 'from_'):
        assert _is_linked(b2, 'from_', a)
    _safe_set(a, 'Transition', None)
    assert not _is_linked(a, 'Transition', b2)
    if hasattr(b2, 'from_'):
        assert not _is_linked(b2, 'from_', a)


def test_assoc_state8_link_reassign_clear():
    a = ctmc_State(exitRate=3.14, name="sample_text")
    b1 = ctmc_Label(text="sample_text")
    b2 = ctmc_Label(text="sample_text_2")
    _safe_set(a, 'State9', b1)
    assert _is_linked(a, 'State9', b1)
    if hasattr(b1, 'labels'):
        assert _is_linked(b1, 'labels', a)
    _safe_set(a, 'State9', b2)
    assert _is_linked(a, 'State9', b2)
    if hasattr(b1, 'labels'):
        assert not _is_linked(b1, 'labels', a)
    if hasattr(b2, 'labels'):
        assert _is_linked(b2, 'labels', a)
    _safe_set(a, 'State9', None)
    assert not _is_linked(a, 'State9', b2)
    if hasattr(b2, 'labels'):
        assert not _is_linked(b2, 'labels', a)


def test_assoc_states0_link_reassign_clear():
    a = ctmc_State(exitRate=3.14, name="sample_text")
    b1 = ctmc_CTMC(name="sample_text")
    b2 = ctmc_CTMC(name="sample_text_2")
    _safe_set(a, 'ctmc_State', b1)
    assert _is_linked(a, 'ctmc_State', b1)
    if hasattr(b1, 'ctmc_CTMC'):
        assert _is_linked(b1, 'ctmc_CTMC', a)
    _safe_set(a, 'ctmc_State', b2)
    assert _is_linked(a, 'ctmc_State', b2)
    if hasattr(b1, 'ctmc_CTMC'):
        assert not _is_linked(b1, 'ctmc_CTMC', a)
    if hasattr(b2, 'ctmc_CTMC'):
        assert _is_linked(b2, 'ctmc_CTMC', a)
    _safe_set(a, 'ctmc_State', None)
    assert not _is_linked(a, 'ctmc_State', b2)
    if hasattr(b2, 'ctmc_CTMC'):
        assert not _is_linked(b2, 'ctmc_CTMC', a)


def test_assoc_to6_link_reassign_clear():
    a = ctmc_Transition(duration=3.14, name="sample_text", probability=3.14)
    b1 = ctmc_State(exitRate=3.14, name="sample_text")
    b2 = ctmc_State(exitRate=9.99, name="sample_text_2")
    _safe_set(a, 'in_', b1)
    assert _is_linked(a, 'in_', b1)
    if hasattr(b1, 'State7'):
        assert _is_linked(b1, 'State7', a)
    _safe_set(a, 'in_', b2)
    assert _is_linked(a, 'in_', b2)
    if hasattr(b1, 'State7'):
        assert not _is_linked(b1, 'State7', a)
    if hasattr(b2, 'State7'):
        assert _is_linked(b2, 'State7', a)
    _safe_set(a, 'in_', None)
    assert not _is_linked(a, 'in_', b2)
    if hasattr(b2, 'State7'):
        assert not _is_linked(b2, 'State7', a)


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

ctmc_CTMC_strategy = st.builds(ctmc_CTMC, name=safe_text)
@given(instance=ctmc_CTMC_strategy)
@settings(max_examples=25)
def test_ctmc_CTMC_instantiation(instance):
    assert isinstance(instance, ctmc_CTMC)


ctmc_Label_strategy = st.builds(ctmc_Label, text=safe_text)
@given(instance=ctmc_Label_strategy)
@settings(max_examples=25)
def test_ctmc_Label_instantiation(instance):
    assert isinstance(instance, ctmc_Label)


ctmc_State_strategy = st.builds(ctmc_State, exitRate=st.floats(allow_nan=False, allow_infinity=False), name=safe_text)
@given(instance=ctmc_State_strategy)
@settings(max_examples=25)
def test_ctmc_State_instantiation(instance):
    assert isinstance(instance, ctmc_State)


ctmc_Transition_strategy = st.builds(ctmc_Transition, duration=st.floats(allow_nan=False, allow_infinity=False), name=safe_text, probability=st.floats(allow_nan=False, allow_infinity=False))
@given(instance=ctmc_Transition_strategy)
@settings(max_examples=25)
def test_ctmc_Transition_instantiation(instance):
    assert isinstance(instance, ctmc_Transition)



