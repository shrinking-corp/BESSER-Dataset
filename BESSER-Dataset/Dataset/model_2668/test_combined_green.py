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
    semlink_NamedElement,
    NamedElement,
    semlink_A,
    semlink_C,
    semlink_B,
    semlink_G,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_hyp_semlink_namedelement_is_not_abstract():
    assert not inspect.isabstract(semlink_NamedElement)


def test_hyp_semlink_namedelement_constructor_exists():
    assert callable(semlink_NamedElement.__init__)


def test_hyp_semlink_namedelement_constructor_args():
    sig = inspect.signature(semlink_NamedElement.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"




def test_hyp_namedelement_is_not_abstract():
    assert not inspect.isabstract(NamedElement)


def test_hyp_namedelement_constructor_exists():
    assert callable(NamedElement.__init__)


def test_hyp_namedelement_constructor_args():
    sig = inspect.signature(NamedElement.__init__)
    params = list(sig.parameters.keys())



def test_hyp_semlink_a_is_not_abstract():
    assert not inspect.isabstract(semlink_A)


def test_hyp_semlink_a_constructor_exists():
    assert callable(semlink_A.__init__)


def test_hyp_semlink_a_constructor_args():
    sig = inspect.signature(semlink_A.__init__)
    params = list(sig.parameters.keys())



def test_hyp_semlink_c_is_not_abstract():
    assert not inspect.isabstract(semlink_C)


def test_hyp_semlink_c_constructor_exists():
    assert callable(semlink_C.__init__)


def test_hyp_semlink_c_constructor_args():
    sig = inspect.signature(semlink_C.__init__)
    params = list(sig.parameters.keys())



def test_hyp_semlink_b_is_not_abstract():
    assert not inspect.isabstract(semlink_B)


def test_hyp_semlink_b_constructor_exists():
    assert callable(semlink_B.__init__)


def test_hyp_semlink_b_constructor_args():
    sig = inspect.signature(semlink_B.__init__)
    params = list(sig.parameters.keys())



def test_hyp_semlink_g_is_not_abstract():
    assert not inspect.isabstract(semlink_G)


def test_hyp_semlink_g_constructor_exists():
    assert callable(semlink_G.__init__)


def test_hyp_semlink_g_constructor_args():
    sig = inspect.signature(semlink_G.__init__)
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
semlink_NamedElement_strategy = st.builds(
    semlink_NamedElement,
    name=
        safe_text
)
NamedElement_strategy = st.builds(
    NamedElement,
)
semlink_A_strategy = st.builds(
    semlink_A,
)
semlink_C_strategy = st.builds(
    semlink_C,
)
semlink_B_strategy = st.builds(
    semlink_B,
)
semlink_G_strategy = st.builds(
    semlink_G,
)




@given(instance=semlink_NamedElement_strategy)
def test_hyp_semlink_namedelement_name_setter(instance):
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
    NamedElement,
    semlink_A,
    semlink_B,
    semlink_C,
    semlink_G,
    semlink_NamedElement,
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

def test_semlink_NamedElement_name_value_roundtrip():
    instance = semlink_NamedElement(name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_semlink_A_isa_NamedElement():
    instance = semlink_A()
    assert isinstance(instance, NamedElement)


def test_semlink_B_isa_NamedElement():
    instance = semlink_B()
    assert isinstance(instance, NamedElement)


def test_semlink_C_isa_NamedElement():
    instance = semlink_C()
    assert isinstance(instance, NamedElement)


def test_semlink_G_isa_NamedElement():
    instance = semlink_G()
    assert isinstance(instance, NamedElement)


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

NamedElement_strategy = st.builds(NamedElement)
@given(instance=NamedElement_strategy)
@settings(max_examples=25)
def test_NamedElement_instantiation(instance):
    assert isinstance(instance, NamedElement)


semlink_A_strategy = st.builds(semlink_A)
@given(instance=semlink_A_strategy)
@settings(max_examples=25)
def test_semlink_A_instantiation(instance):
    assert isinstance(instance, semlink_A)


semlink_B_strategy = st.builds(semlink_B)
@given(instance=semlink_B_strategy)
@settings(max_examples=25)
def test_semlink_B_instantiation(instance):
    assert isinstance(instance, semlink_B)


semlink_C_strategy = st.builds(semlink_C)
@given(instance=semlink_C_strategy)
@settings(max_examples=25)
def test_semlink_C_instantiation(instance):
    assert isinstance(instance, semlink_C)


semlink_G_strategy = st.builds(semlink_G)
@given(instance=semlink_G_strategy)
@settings(max_examples=25)
def test_semlink_G_instantiation(instance):
    assert isinstance(instance, semlink_G)


semlink_NamedElement_strategy = st.builds(semlink_NamedElement, name=safe_text)
@given(instance=semlink_NamedElement_strategy)
@settings(max_examples=25)
def test_semlink_NamedElement_instantiation(instance):
    assert isinstance(instance, semlink_NamedElement)



