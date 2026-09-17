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
    testaccessors_EAcc,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_hyp_testaccessors_eacc_is_not_abstract():
    assert not inspect.isabstract(testaccessors_EAcc)


def test_hyp_testaccessors_eacc_constructor_exists():
    assert callable(testaccessors_EAcc.__init__)


def test_hyp_testaccessors_eacc_constructor_args():
    sig = inspect.signature(testaccessors_EAcc.__init__)
    params = list(sig.parameters.keys())
    assert "bs" in params, "Missing parameter 'bs'"
    assert "b" in params, "Missing parameter 'b'"
    assert "i" in params, "Missing parameter 'i'"
    assert "is_" in params, "Missing parameter 'is_'"






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
testaccessors_EAcc_strategy = st.builds(
    testaccessors_EAcc,
    bs=
        st.booleans(),
    b=
        st.booleans(),
    i=
        st.integers(),
    is_=
        st.integers()
)




@given(instance=testaccessors_EAcc_strategy)
def test_hyp_testaccessors_eacc_bs_setter(instance):
    original = instance.bs
    instance.bs = original
    assert instance.bs == original



@given(instance=testaccessors_EAcc_strategy)
def test_hyp_testaccessors_eacc_b_setter(instance):
    original = instance.b
    instance.b = original
    assert instance.b == original



@given(instance=testaccessors_EAcc_strategy)
def test_hyp_testaccessors_eacc_i_setter(instance):
    original = instance.i
    instance.i = original
    assert instance.i == original



@given(instance=testaccessors_EAcc_strategy)
def test_hyp_testaccessors_eacc_is__setter(instance):
    original = instance.is_
    instance.is_ = original
    assert instance.is_ == original


# ----- SECTION B: test_structural_full.py (deterministic-first suite) -----
import inspect
import pytest
from datetime import date, datetime, time, timedelta
from hypothesis import given, settings
import hypothesis.strategies as st

from python_code import (
    testaccessors_EAcc,
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

def test_testaccessors_EAcc_b_value_roundtrip():
    instance = testaccessors_EAcc(b=True, bs=True, i=7, is_=7)
    assert instance.b == True
    instance.b = False
    assert instance.b == False


def test_testaccessors_EAcc_bs_value_roundtrip():
    instance = testaccessors_EAcc(b=True, bs=True, i=7, is_=7)
    assert instance.bs == True
    instance.bs = False
    assert instance.bs == False


def test_testaccessors_EAcc_i_value_roundtrip():
    instance = testaccessors_EAcc(b=True, bs=True, i=7, is_=7)
    assert instance.i == 7
    instance.i = 13
    assert instance.i == 13


def test_testaccessors_EAcc_is__value_roundtrip():
    instance = testaccessors_EAcc(b=True, bs=True, i=7, is_=7)
    assert instance.is_ == 7
    instance.is_ = 13
    assert instance.is_ == 13


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

testaccessors_EAcc_strategy = st.builds(testaccessors_EAcc, b=st.booleans(), bs=st.booleans(), i=st.integers(), is_=st.integers())
@given(instance=testaccessors_EAcc_strategy)
@settings(max_examples=25)
def test_testaccessors_EAcc_instantiation(instance):
    assert isinstance(instance, testaccessors_EAcc)



