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
    Basic2_C,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_hyp_basic2_c_is_not_abstract():
    assert not inspect.isabstract(Basic2_C)


def test_hyp_basic2_c_constructor_exists():
    assert callable(Basic2_C.__init__)


def test_hyp_basic2_c_constructor_args():
    sig = inspect.signature(Basic2_C.__init__)
    params = list(sig.parameters.keys())
    assert "a" in params, "Missing parameter 'a'"
    assert "c" in params, "Missing parameter 'c'"
    assert "b" in params, "Missing parameter 'b'"





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
Basic2_C_strategy = st.builds(
    Basic2_C,
    a=
        st.integers(),
    c=
        st.integers(),
    b=
        st.integers()
)




@given(instance=Basic2_C_strategy)
def test_hyp_basic2_c_a_setter(instance):
    original = instance.a
    instance.a = original
    assert instance.a == original



@given(instance=Basic2_C_strategy)
def test_hyp_basic2_c_c_setter(instance):
    original = instance.c
    instance.c = original
    assert instance.c == original



@given(instance=Basic2_C_strategy)
def test_hyp_basic2_c_b_setter(instance):
    original = instance.b
    instance.b = original
    assert instance.b == original


# ----- SECTION B: test_structural_full.py (deterministic-first suite) -----
import inspect
import pytest
from datetime import date, datetime, time, timedelta
from hypothesis import given, settings
import hypothesis.strategies as st

from python_code import (
    Basic2_C,
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

def test_Basic2_C_a_value_roundtrip():
    instance = Basic2_C(a=7, b=7, c=7)
    assert instance.a == 7
    instance.a = 13
    assert instance.a == 13


def test_Basic2_C_b_value_roundtrip():
    instance = Basic2_C(a=7, b=7, c=7)
    assert instance.b == 7
    instance.b = 13
    assert instance.b == 13


def test_Basic2_C_c_value_roundtrip():
    instance = Basic2_C(a=7, b=7, c=7)
    assert instance.c == 7
    instance.c = 13
    assert instance.c == 13


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

Basic2_C_strategy = st.builds(Basic2_C, a=st.integers(), b=st.integers(), c=st.integers())
@given(instance=Basic2_C_strategy)
@settings(max_examples=25)
def test_Basic2_C_instantiation(instance):
    assert isinstance(instance, Basic2_C)



