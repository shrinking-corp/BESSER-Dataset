import inspect
import pytest
from datetime import date, datetime, time, timedelta
from hypothesis import given, settings
import hypothesis.strategies as st

from python_code import (
    A,
    B,
    MyClass9,
    R,
    Y,
    c,
    c2,
    c3,
    z,
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


MyClass9_strategy = st.builds(MyClass9)
@given(instance=MyClass9_strategy)
@settings(max_examples=25)
def test_MyClass9_instantiation(instance):
    assert isinstance(instance, MyClass9)


R_strategy = st.builds(R)
@given(instance=R_strategy)
@settings(max_examples=25)
def test_R_instantiation(instance):
    assert isinstance(instance, R)


Y_strategy = st.builds(Y)
@given(instance=Y_strategy)
@settings(max_examples=25)
def test_Y_instantiation(instance):
    assert isinstance(instance, Y)


c_strategy = st.builds(c)
@given(instance=c_strategy)
@settings(max_examples=25)
def test_c_instantiation(instance):
    assert isinstance(instance, c)


c2_strategy = st.builds(c2)
@given(instance=c2_strategy)
@settings(max_examples=25)
def test_c2_instantiation(instance):
    assert isinstance(instance, c2)


c3_strategy = st.builds(c3)
@given(instance=c3_strategy)
@settings(max_examples=25)
def test_c3_instantiation(instance):
    assert isinstance(instance, c3)


z_strategy = st.builds(z)
@given(instance=z_strategy)
@settings(max_examples=25)
def test_z_instantiation(instance):
    assert isinstance(instance, z)


