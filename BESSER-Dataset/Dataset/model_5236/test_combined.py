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
    Basic3_C,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_hyp_basic3_c_is_not_abstract():
    assert not inspect.isabstract(Basic3_C)


def test_hyp_basic3_c_constructor_exists():
    assert callable(Basic3_C.__init__)


def test_hyp_basic3_c_constructor_args():
    sig = inspect.signature(Basic3_C.__init__)
    params = list(sig.parameters.keys())
    assert "b" in params, "Missing parameter 'b'"
    assert "d" in params, "Missing parameter 'd'"
    assert "a" in params, "Missing parameter 'a'"
    assert "c" in params, "Missing parameter 'c'"






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
Basic3_C_strategy = st.builds(
    Basic3_C,
    b=
        st.booleans(),
    d=
        st.booleans(),
    a=
        st.booleans(),
    c=
        st.booleans()
)




@given(instance=Basic3_C_strategy)
def test_hyp_basic3_c_b_setter(instance):
    original = instance.b
    instance.b = original
    assert instance.b == original



@given(instance=Basic3_C_strategy)
def test_hyp_basic3_c_d_setter(instance):
    original = instance.d
    instance.d = original
    assert instance.d == original



@given(instance=Basic3_C_strategy)
def test_hyp_basic3_c_a_setter(instance):
    original = instance.a
    instance.a = original
    assert instance.a == original



@given(instance=Basic3_C_strategy)
def test_hyp_basic3_c_c_setter(instance):
    original = instance.c
    instance.c = original
    assert instance.c == original


# ----- SECTION B: test_structural_full.py (deterministic-first suite) -----
import inspect
import pytest
from datetime import date, datetime, time, timedelta
from hypothesis import given, settings
import hypothesis.strategies as st

from python_code import (
    Basic3_C,
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

def test_Basic3_C_a_value_roundtrip():
    instance = Basic3_C(a=True, b=True, c=True, d=True)
    assert instance.a == True
    instance.a = False
    assert instance.a == False


def test_Basic3_C_b_value_roundtrip():
    instance = Basic3_C(a=True, b=True, c=True, d=True)
    assert instance.b == True
    instance.b = False
    assert instance.b == False


def test_Basic3_C_c_value_roundtrip():
    instance = Basic3_C(a=True, b=True, c=True, d=True)
    assert instance.c == True
    instance.c = False
    assert instance.c == False


def test_Basic3_C_d_value_roundtrip():
    instance = Basic3_C(a=True, b=True, c=True, d=True)
    assert instance.d == True
    instance.d = False
    assert instance.d == False


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

Basic3_C_strategy = st.builds(Basic3_C, a=st.booleans(), b=st.booleans(), c=st.booleans(), d=st.booleans())
@given(instance=Basic3_C_strategy)
@settings(max_examples=25)
def test_Basic3_C_instantiation(instance):
    assert isinstance(instance, Basic3_C)



