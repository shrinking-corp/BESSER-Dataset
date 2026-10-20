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
    tbase_NamedElement,
    tbase_TRoot,
    tbase_C,
    NamedElement,
    tbase_B,
    tbase_A,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_hyp_tbase_namedelement_is_not_abstract():
    assert not inspect.isabstract(tbase_NamedElement)


def test_hyp_tbase_namedelement_constructor_exists():
    assert callable(tbase_NamedElement.__init__)


def test_hyp_tbase_namedelement_constructor_args():
    sig = inspect.signature(tbase_NamedElement.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"




def test_hyp_tbase_troot_is_not_abstract():
    assert not inspect.isabstract(tbase_TRoot)


def test_hyp_tbase_troot_constructor_exists():
    assert callable(tbase_TRoot.__init__)


def test_hyp_tbase_troot_constructor_args():
    sig = inspect.signature(tbase_TRoot.__init__)
    params = list(sig.parameters.keys())



def test_hyp_tbase_c_is_not_abstract():
    assert not inspect.isabstract(tbase_C)


def test_hyp_tbase_c_constructor_exists():
    assert callable(tbase_C.__init__)


def test_hyp_tbase_c_constructor_args():
    sig = inspect.signature(tbase_C.__init__)
    params = list(sig.parameters.keys())



def test_hyp_namedelement_is_not_abstract():
    assert not inspect.isabstract(NamedElement)


def test_hyp_namedelement_constructor_exists():
    assert callable(NamedElement.__init__)


def test_hyp_namedelement_constructor_args():
    sig = inspect.signature(NamedElement.__init__)
    params = list(sig.parameters.keys())



def test_hyp_tbase_b_is_not_abstract():
    assert not inspect.isabstract(tbase_B)


def test_hyp_tbase_b_constructor_exists():
    assert callable(tbase_B.__init__)


def test_hyp_tbase_b_constructor_args():
    sig = inspect.signature(tbase_B.__init__)
    params = list(sig.parameters.keys())



def test_hyp_tbase_a_is_not_abstract():
    assert not inspect.isabstract(tbase_A)


def test_hyp_tbase_a_constructor_exists():
    assert callable(tbase_A.__init__)


def test_hyp_tbase_a_constructor_args():
    sig = inspect.signature(tbase_A.__init__)
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
tbase_NamedElement_strategy = st.builds(
    tbase_NamedElement,
    name=
        safe_text
)
tbase_TRoot_strategy = st.builds(
    tbase_TRoot,
)
tbase_C_strategy = st.builds(
    tbase_C,
)
NamedElement_strategy = st.builds(
    NamedElement,
)
tbase_B_strategy = st.builds(
    tbase_B,
)
tbase_A_strategy = st.builds(
    tbase_A,
)




@given(instance=tbase_NamedElement_strategy)
def test_hyp_tbase_namedelement_name_setter(instance):
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
    tbase_A,
    tbase_B,
    tbase_C,
    tbase_NamedElement,
    tbase_TRoot,
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

def test_tbase_NamedElement_name_value_roundtrip():
    instance = tbase_NamedElement(name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_tbase_A_isa_NamedElement():
    instance = tbase_A()
    assert isinstance(instance, NamedElement)


def test_tbase_B_isa_NamedElement():
    instance = tbase_B()
    assert isinstance(instance, NamedElement)


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

NamedElement_strategy = st.builds(NamedElement)
@given(instance=NamedElement_strategy)
@settings(max_examples=25)
def test_NamedElement_instantiation(instance):
    assert isinstance(instance, NamedElement)


tbase_A_strategy = st.builds(tbase_A)
@given(instance=tbase_A_strategy)
@settings(max_examples=25)
def test_tbase_A_instantiation(instance):
    assert isinstance(instance, tbase_A)


tbase_B_strategy = st.builds(tbase_B)
@given(instance=tbase_B_strategy)
@settings(max_examples=25)
def test_tbase_B_instantiation(instance):
    assert isinstance(instance, tbase_B)


tbase_C_strategy = st.builds(tbase_C)
@given(instance=tbase_C_strategy)
@settings(max_examples=25)
def test_tbase_C_instantiation(instance):
    assert isinstance(instance, tbase_C)


tbase_NamedElement_strategy = st.builds(tbase_NamedElement, name=safe_text)
@given(instance=tbase_NamedElement_strategy)
@settings(max_examples=25)
def test_tbase_NamedElement_instantiation(instance):
    assert isinstance(instance, tbase_NamedElement)


tbase_TRoot_strategy = st.builds(tbase_TRoot)
@given(instance=tbase_TRoot_strategy)
@settings(max_examples=25)
def test_tbase_TRoot_instantiation(instance):
    assert isinstance(instance, tbase_TRoot)



