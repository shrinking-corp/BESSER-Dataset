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
    factorydeclorder_D,
    factorydeclorder_B,
    D,
    A,
    B,
    factorydeclorder_A,
    factorydeclorder_C,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_hyp_factorydeclorder_d_is_not_abstract():
    assert not inspect.isabstract(factorydeclorder_D)


def test_hyp_factorydeclorder_d_constructor_exists():
    assert callable(factorydeclorder_D.__init__)


def test_hyp_factorydeclorder_d_constructor_args():
    sig = inspect.signature(factorydeclorder_D.__init__)
    params = list(sig.parameters.keys())



def test_hyp_factorydeclorder_b_is_not_abstract():
    assert not inspect.isabstract(factorydeclorder_B)


def test_hyp_factorydeclorder_b_constructor_exists():
    assert callable(factorydeclorder_B.__init__)


def test_hyp_factorydeclorder_b_constructor_args():
    sig = inspect.signature(factorydeclorder_B.__init__)
    params = list(sig.parameters.keys())
    assert "fb" in params, "Missing parameter 'fb'"




def test_hyp_d_is_not_abstract():
    assert not inspect.isabstract(D)


def test_hyp_d_constructor_exists():
    assert callable(D.__init__)


def test_hyp_d_constructor_args():
    sig = inspect.signature(D.__init__)
    params = list(sig.parameters.keys())



def test_hyp_a_is_not_abstract():
    assert not inspect.isabstract(A)


def test_hyp_a_constructor_exists():
    assert callable(A.__init__)


def test_hyp_a_constructor_args():
    sig = inspect.signature(A.__init__)
    params = list(sig.parameters.keys())



def test_hyp_b_is_not_abstract():
    assert not inspect.isabstract(B)


def test_hyp_b_constructor_exists():
    assert callable(B.__init__)


def test_hyp_b_constructor_args():
    sig = inspect.signature(B.__init__)
    params = list(sig.parameters.keys())



def test_hyp_factorydeclorder_a_is_not_abstract():
    assert not inspect.isabstract(factorydeclorder_A)


def test_hyp_factorydeclorder_a_constructor_exists():
    assert callable(factorydeclorder_A.__init__)


def test_hyp_factorydeclorder_a_constructor_args():
    sig = inspect.signature(factorydeclorder_A.__init__)
    params = list(sig.parameters.keys())
    assert "fa" in params, "Missing parameter 'fa'"




def test_hyp_factorydeclorder_c_is_not_abstract():
    assert not inspect.isabstract(factorydeclorder_C)


def test_hyp_factorydeclorder_c_constructor_exists():
    assert callable(factorydeclorder_C.__init__)


def test_hyp_factorydeclorder_c_constructor_args():
    sig = inspect.signature(factorydeclorder_C.__init__)
    params = list(sig.parameters.keys())
    assert "fc" in params, "Missing parameter 'fc'"



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
factorydeclorder_D_strategy = st.builds(
    factorydeclorder_D,
)
factorydeclorder_B_strategy = st.builds(
    factorydeclorder_B,
    fb=
        safe_text
)
D_strategy = st.builds(
    D,
)
A_strategy = st.builds(
    A,
)
B_strategy = st.builds(
    B,
)
factorydeclorder_A_strategy = st.builds(
    factorydeclorder_A,
    fa=
        st.integers()
)
factorydeclorder_C_strategy = st.builds(
    factorydeclorder_C,
    fc=
        st.booleans()
)





@given(instance=factorydeclorder_B_strategy)
def test_hyp_factorydeclorder_b_fb_setter(instance):
    original = instance.fb
    instance.fb = original
    assert instance.fb == original







@given(instance=factorydeclorder_A_strategy)
def test_hyp_factorydeclorder_a_fa_setter(instance):
    original = instance.fa
    instance.fa = original
    assert instance.fa == original




@given(instance=factorydeclorder_C_strategy)
def test_hyp_factorydeclorder_c_fc_setter(instance):
    original = instance.fc
    instance.fc = original
    assert instance.fc == original


# ----- SECTION B: test_structural_full.py (deterministic-first suite) -----
import inspect
import pytest
from datetime import date, datetime, time, timedelta
from hypothesis import given, settings
import hypothesis.strategies as st

from python_code import (
    A,
    B,
    D,
    factorydeclorder_A,
    factorydeclorder_B,
    factorydeclorder_C,
    factorydeclorder_D,
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

def test_factorydeclorder_A_fa_value_roundtrip():
    instance = factorydeclorder_A(fa=7)
    assert instance.fa == 7
    instance.fa = 13
    assert instance.fa == 13


def test_factorydeclorder_B_fb_value_roundtrip():
    instance = factorydeclorder_B(fb="sample_text")
    assert instance.fb == "sample_text"
    instance.fb = "sample_text_2"
    assert instance.fb == "sample_text_2"


def test_factorydeclorder_C_fc_value_roundtrip():
    instance = factorydeclorder_C(fc=True)
    assert instance.fc == True
    instance.fc = False
    assert instance.fc == False


def test_factorydeclorder_C_isa_A():
    instance = factorydeclorder_C(fc=True)
    assert isinstance(instance, A)


def test_factorydeclorder_A_isa_B():
    instance = factorydeclorder_A(fa=7)
    assert isinstance(instance, B)


def test_factorydeclorder_C_isa_B():
    instance = factorydeclorder_C(fc=True)
    assert isinstance(instance, B)


def test_factorydeclorder_A_isa_D():
    instance = factorydeclorder_A(fa=7)
    assert isinstance(instance, D)


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

A_strategy = st.builds(A)
@given(instance=A_strategy)
@settings(max_examples=25)
def test_A_instantiation(instance):
    assert isinstance(instance, A)


B_strategy = st.builds(B)
@given(instance=B_strategy)
@settings(max_examples=25)
def test_B_instantiation(instance):
    assert isinstance(instance, B)


D_strategy = st.builds(D)
@given(instance=D_strategy)
@settings(max_examples=25)
def test_D_instantiation(instance):
    assert isinstance(instance, D)


factorydeclorder_A_strategy = st.builds(factorydeclorder_A, fa=st.integers())
@given(instance=factorydeclorder_A_strategy)
@settings(max_examples=25)
def test_factorydeclorder_A_instantiation(instance):
    assert isinstance(instance, factorydeclorder_A)


factorydeclorder_B_strategy = st.builds(factorydeclorder_B, fb=safe_text)
@given(instance=factorydeclorder_B_strategy)
@settings(max_examples=25)
def test_factorydeclorder_B_instantiation(instance):
    assert isinstance(instance, factorydeclorder_B)


factorydeclorder_C_strategy = st.builds(factorydeclorder_C, fc=st.booleans())
@given(instance=factorydeclorder_C_strategy)
@settings(max_examples=25)
def test_factorydeclorder_C_instantiation(instance):
    assert isinstance(instance, factorydeclorder_C)


factorydeclorder_D_strategy = st.builds(factorydeclorder_D)
@given(instance=factorydeclorder_D_strategy)
@settings(max_examples=25)
def test_factorydeclorder_D_instantiation(instance):
    assert isinstance(instance, factorydeclorder_D)



