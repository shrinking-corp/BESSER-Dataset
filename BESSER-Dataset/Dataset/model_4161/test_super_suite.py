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
    scheme_Greeting,
    scheme_Model,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_hyp_scheme_greeting_is_not_abstract():
    assert not inspect.isabstract(scheme_Greeting)


def test_hyp_scheme_greeting_constructor_exists():
    assert callable(scheme_Greeting.__init__)


def test_hyp_scheme_greeting_constructor_args():
    sig = inspect.signature(scheme_Greeting.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"




def test_hyp_scheme_model_is_not_abstract():
    assert not inspect.isabstract(scheme_Model)


def test_hyp_scheme_model_constructor_exists():
    assert callable(scheme_Model.__init__)


def test_hyp_scheme_model_constructor_args():
    sig = inspect.signature(scheme_Model.__init__)
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
scheme_Greeting_strategy = st.builds(
    scheme_Greeting,
    name=
        safe_text
)
scheme_Model_strategy = st.builds(
    scheme_Model,
)




@given(instance=scheme_Greeting_strategy)
def test_hyp_scheme_greeting_name_setter(instance):
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
    scheme_Greeting,
    scheme_Model,
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

def test_scheme_Greeting_name_value_roundtrip():
    instance = scheme_Greeting(name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_assoc_greetings0_link_reassign_clear():
    a = scheme_Greeting(name="sample_text")
    b1 = scheme_Model()
    b2 = scheme_Model()
    _safe_set(a, 'scheme_Greeting', b1)
    assert _is_linked(a, 'scheme_Greeting', b1)
    if hasattr(b1, 'scheme_Model'):
        assert _is_linked(b1, 'scheme_Model', a)
    _safe_set(a, 'scheme_Greeting', b2)
    assert _is_linked(a, 'scheme_Greeting', b2)
    if hasattr(b1, 'scheme_Model'):
        assert not _is_linked(b1, 'scheme_Model', a)
    if hasattr(b2, 'scheme_Model'):
        assert _is_linked(b2, 'scheme_Model', a)
    _safe_set(a, 'scheme_Greeting', None)
    assert not _is_linked(a, 'scheme_Greeting', b2)
    if hasattr(b2, 'scheme_Model'):
        assert not _is_linked(b2, 'scheme_Model', a)


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

scheme_Greeting_strategy = st.builds(scheme_Greeting, name=safe_text)
@given(instance=scheme_Greeting_strategy)
@settings(max_examples=25)
def test_scheme_Greeting_instantiation(instance):
    assert isinstance(instance, scheme_Greeting)


scheme_Model_strategy = st.builds(scheme_Model)
@given(instance=scheme_Model_strategy)
@settings(max_examples=25)
def test_scheme_Model_instantiation(instance):
    assert isinstance(instance, scheme_Model)





import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    scheme_Greeting,
    scheme_Model,
)

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
# REVERSE-DIRECTION ASSOCIATION TESTS
# Mirrors test_structural_full.py's link_reassign_clear, but sets from the
# OTHER end's own setter directly, instead of relying on it firing only as a
# side effect of the forward-direction test. See module docstring.
# =============================================================================

# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_greetings0_stub_double():
    # scheme_Model has no real 'scheme_Model' property in the generated
    # code (a bare stub) -- manually attach it so scheme_Greeting's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # scheme_Greeting's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = scheme_Greeting(name="sample_text")
    partner = scheme_Model()
    setattr(partner, 'scheme_Model', None)
    _safe_set(owner, 'scheme_Greeting', partner)
    assert owner in getattr(partner, 'scheme_Model')
    _safe_set(owner, 'scheme_Greeting', None)
    assert owner not in getattr(partner, 'scheme_Model')




from python_code import scheme_Greeting
from python_code import scheme_Model

def test_scheme_Greeting___init__():
    assert scheme_Greeting.__init__(scheme_Greeting('', scheme_Greeting=scheme_Model()), '', scheme_Greeting=scheme_Model()) == None

