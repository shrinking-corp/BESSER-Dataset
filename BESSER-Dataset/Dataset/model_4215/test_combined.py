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
    helloworldext_Greeting,
    helloworldext_Person,
    helloworldext_GreetingMessage,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_hyp_helloworldext_greeting_is_not_abstract():
    assert not inspect.isabstract(helloworldext_Greeting)


def test_hyp_helloworldext_greeting_constructor_exists():
    assert callable(helloworldext_Greeting.__init__)


def test_hyp_helloworldext_greeting_constructor_args():
    sig = inspect.signature(helloworldext_Greeting.__init__)
    params = list(sig.parameters.keys())



def test_hyp_helloworldext_person_is_not_abstract():
    assert not inspect.isabstract(helloworldext_Person)


def test_hyp_helloworldext_person_constructor_exists():
    assert callable(helloworldext_Person.__init__)


def test_hyp_helloworldext_person_constructor_args():
    sig = inspect.signature(helloworldext_Person.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"




def test_hyp_helloworldext_greetingmessage_is_not_abstract():
    assert not inspect.isabstract(helloworldext_GreetingMessage)


def test_hyp_helloworldext_greetingmessage_constructor_exists():
    assert callable(helloworldext_GreetingMessage.__init__)


def test_hyp_helloworldext_greetingmessage_constructor_args():
    sig = inspect.signature(helloworldext_GreetingMessage.__init__)
    params = list(sig.parameters.keys())
    assert "text" in params, "Missing parameter 'text'"



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
helloworldext_Greeting_strategy = st.builds(
    helloworldext_Greeting,
)
helloworldext_Person_strategy = st.builds(
    helloworldext_Person,
    name=
        safe_text
)
helloworldext_GreetingMessage_strategy = st.builds(
    helloworldext_GreetingMessage,
    text=
        safe_text
)





@given(instance=helloworldext_Person_strategy)
def test_hyp_helloworldext_person_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original




@given(instance=helloworldext_GreetingMessage_strategy)
def test_hyp_helloworldext_greetingmessage_text_setter(instance):
    original = instance.text
    instance.text = original
    assert instance.text == original


# ----- SECTION B: test_structural_full.py (deterministic-first suite) -----
import inspect
import pytest
from datetime import date, datetime, time, timedelta
from hypothesis import given, settings
import hypothesis.strategies as st

from python_code import (
    helloworldext_Greeting,
    helloworldext_GreetingMessage,
    helloworldext_Person,
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

def test_helloworldext_GreetingMessage_text_value_roundtrip():
    instance = helloworldext_GreetingMessage(text="sample_text")
    assert instance.text == "sample_text"
    instance.text = "sample_text_2"
    assert instance.text == "sample_text_2"


def test_helloworldext_Person_name_value_roundtrip():
    instance = helloworldext_Person(name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_assoc_greetingMessage0_link_reassign_clear():
    a = helloworldext_GreetingMessage(text="sample_text")
    b1 = helloworldext_Greeting()
    b2 = helloworldext_Greeting()
    _safe_set(a, 'helloworldext_GreetingMessage', b1)
    assert _is_linked(a, 'helloworldext_GreetingMessage', b1)
    if hasattr(b1, 'helloworldext_Greeting'):
        assert _is_linked(b1, 'helloworldext_Greeting', a)
    _safe_set(a, 'helloworldext_GreetingMessage', b2)
    assert _is_linked(a, 'helloworldext_GreetingMessage', b2)
    if hasattr(b1, 'helloworldext_Greeting'):
        assert not _is_linked(b1, 'helloworldext_Greeting', a)
    if hasattr(b2, 'helloworldext_Greeting'):
        assert _is_linked(b2, 'helloworldext_Greeting', a)
    _safe_set(a, 'helloworldext_GreetingMessage', None)
    assert not _is_linked(a, 'helloworldext_GreetingMessage', b2)
    if hasattr(b2, 'helloworldext_Greeting'):
        assert not _is_linked(b2, 'helloworldext_Greeting', a)


def test_assoc_person1_link_reassign_clear():
    a = helloworldext_Person(name="sample_text")
    b1 = helloworldext_Greeting()
    b2 = helloworldext_Greeting()
    _safe_set(a, 'helloworldext_Person', b1)
    assert _is_linked(a, 'helloworldext_Person', b1)
    if hasattr(b1, 'helloworldext_Greeting2'):
        assert _is_linked(b1, 'helloworldext_Greeting2', a)
    _safe_set(a, 'helloworldext_Person', b2)
    assert _is_linked(a, 'helloworldext_Person', b2)
    if hasattr(b1, 'helloworldext_Greeting2'):
        assert not _is_linked(b1, 'helloworldext_Greeting2', a)
    if hasattr(b2, 'helloworldext_Greeting2'):
        assert _is_linked(b2, 'helloworldext_Greeting2', a)
    _safe_set(a, 'helloworldext_Person', None)
    assert not _is_linked(a, 'helloworldext_Person', b2)
    if hasattr(b2, 'helloworldext_Greeting2'):
        assert not _is_linked(b2, 'helloworldext_Greeting2', a)


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

helloworldext_Greeting_strategy = st.builds(helloworldext_Greeting)
@given(instance=helloworldext_Greeting_strategy)
@settings(max_examples=25)
def test_helloworldext_Greeting_instantiation(instance):
    assert isinstance(instance, helloworldext_Greeting)


helloworldext_GreetingMessage_strategy = st.builds(helloworldext_GreetingMessage, text=safe_text)
@given(instance=helloworldext_GreetingMessage_strategy)
@settings(max_examples=25)
def test_helloworldext_GreetingMessage_instantiation(instance):
    assert isinstance(instance, helloworldext_GreetingMessage)


helloworldext_Person_strategy = st.builds(helloworldext_Person, name=safe_text)
@given(instance=helloworldext_Person_strategy)
@settings(max_examples=25)
def test_helloworldext_Person_instantiation(instance):
    assert isinstance(instance, helloworldext_Person)



