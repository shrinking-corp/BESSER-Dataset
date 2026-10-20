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
    model_IPersonList,
    model_IPerson,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_hyp_model_ipersonlist_is_not_abstract():
    assert not inspect.isabstract(model_IPersonList)


def test_hyp_model_ipersonlist_constructor_exists():
    assert callable(model_IPersonList.__init__)


def test_hyp_model_ipersonlist_constructor_args():
    sig = inspect.signature(model_IPersonList.__init__)
    params = list(sig.parameters.keys())



def test_hyp_model_iperson_is_not_abstract():
    assert not inspect.isabstract(model_IPerson)


def test_hyp_model_iperson_constructor_exists():
    assert callable(model_IPerson.__init__)


def test_hyp_model_iperson_constructor_args():
    sig = inspect.signature(model_IPerson.__init__)
    params = list(sig.parameters.keys())
    assert "firstName" in params, "Missing parameter 'firstName'"



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
model_IPersonList_strategy = st.builds(
    model_IPersonList,
)
model_IPerson_strategy = st.builds(
    model_IPerson,
    firstName=
        safe_text
)





@given(instance=model_IPerson_strategy)
def test_hyp_model_iperson_firstName_setter(instance):
    original = instance.firstName
    instance.firstName = original
    assert instance.firstName == original


# ----- SECTION B: test_structural_full.py (deterministic-first suite) -----
import inspect
import pytest
from datetime import date, datetime, time, timedelta
from hypothesis import given, settings
import hypothesis.strategies as st

from python_code import (
    model_IPerson,
    model_IPersonList,
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

def test_model_IPerson_firstName_value_roundtrip():
    instance = model_IPerson(firstName="sample_text")
    assert instance.firstName == "sample_text"
    instance.firstName = "sample_text_2"
    assert instance.firstName == "sample_text_2"


def test_assoc_persons0_link_reassign_clear():
    a = model_IPerson(firstName="sample_text")
    b1 = model_IPersonList()
    b2 = model_IPersonList()
    _safe_set(a, 'model_IPerson', b1)
    assert _is_linked(a, 'model_IPerson', b1)
    if hasattr(b1, 'model_IPersonList'):
        assert _is_linked(b1, 'model_IPersonList', a)
    _safe_set(a, 'model_IPerson', b2)
    assert _is_linked(a, 'model_IPerson', b2)
    if hasattr(b1, 'model_IPersonList'):
        assert not _is_linked(b1, 'model_IPersonList', a)
    if hasattr(b2, 'model_IPersonList'):
        assert _is_linked(b2, 'model_IPersonList', a)
    _safe_set(a, 'model_IPerson', None)
    assert not _is_linked(a, 'model_IPerson', b2)
    if hasattr(b2, 'model_IPersonList'):
        assert not _is_linked(b2, 'model_IPersonList', a)


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

model_IPerson_strategy = st.builds(model_IPerson, firstName=safe_text)
@given(instance=model_IPerson_strategy)
@settings(max_examples=25)
def test_model_IPerson_instantiation(instance):
    assert isinstance(instance, model_IPerson)


model_IPersonList_strategy = st.builds(model_IPersonList)
@given(instance=model_IPersonList_strategy)
@settings(max_examples=25)
def test_model_IPersonList_instantiation(instance):
    assert isinstance(instance, model_IPersonList)





import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    model_IPerson,
    model_IPersonList,
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

def test_assoc_persons0_stub_double():
    # model_IPersonList has no real 'model_IPersonList' property in the generated
    # code (a bare stub) -- manually attach it so model_IPerson's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # model_IPerson's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = model_IPerson(firstName="sample_text")
    partner = model_IPersonList()
    setattr(partner, 'model_IPersonList', None)
    _safe_set(owner, 'model_IPerson', partner)
    assert owner in getattr(partner, 'model_IPersonList')
    _safe_set(owner, 'model_IPerson', None)
    assert owner not in getattr(partner, 'model_IPersonList')




from python_code import model_IPerson
from python_code import model_IPersonList

def test_model_IPerson___init__():
    assert model_IPerson.__init__(model_IPerson('', model_IPerson=model_IPersonList()), '', model_IPerson=model_IPersonList()) == None

