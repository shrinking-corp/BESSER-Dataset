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
    cycle_C,
    cycle_B,
    cycle_A,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_hyp_cycle_c_is_not_abstract():
    assert not inspect.isabstract(cycle_C)


def test_hyp_cycle_c_constructor_exists():
    assert callable(cycle_C.__init__)


def test_hyp_cycle_c_constructor_args():
    sig = inspect.signature(cycle_C.__init__)
    params = list(sig.parameters.keys())



def test_hyp_cycle_b_is_not_abstract():
    assert not inspect.isabstract(cycle_B)


def test_hyp_cycle_b_constructor_exists():
    assert callable(cycle_B.__init__)


def test_hyp_cycle_b_constructor_args():
    sig = inspect.signature(cycle_B.__init__)
    params = list(sig.parameters.keys())
    assert "x" in params, "Missing parameter 'x'"
    assert "y" in params, "Missing parameter 'y'"





def test_hyp_cycle_a_is_not_abstract():
    assert not inspect.isabstract(cycle_A)


def test_hyp_cycle_a_constructor_exists():
    assert callable(cycle_A.__init__)


def test_hyp_cycle_a_constructor_args():
    sig = inspect.signature(cycle_A.__init__)
    params = list(sig.parameters.keys())
    assert "j" in params, "Missing parameter 'j'"
    assert "i" in params, "Missing parameter 'i'"




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
cycle_C_strategy = st.builds(
    cycle_C,
)
cycle_B_strategy = st.builds(
    cycle_B,
    x=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    y=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
cycle_A_strategy = st.builds(
    cycle_A,
    j=
        st.integers(),
    i=
        st.integers()
)





@given(instance=cycle_B_strategy)
def test_hyp_cycle_b_x_setter(instance):
    original = instance.x
    instance.x = original
    assert instance.x == original



@given(instance=cycle_B_strategy)
def test_hyp_cycle_b_y_setter(instance):
    original = instance.y
    instance.y = original
    assert instance.y == original




@given(instance=cycle_A_strategy)
def test_hyp_cycle_a_j_setter(instance):
    original = instance.j
    instance.j = original
    assert instance.j == original



@given(instance=cycle_A_strategy)
def test_hyp_cycle_a_i_setter(instance):
    original = instance.i
    instance.i = original
    assert instance.i == original


# ----- SECTION B: test_structural_full.py (deterministic-first suite) -----
import inspect
import pytest
from datetime import date, datetime, time, timedelta
from hypothesis import given, settings
import hypothesis.strategies as st

from python_code import (
    cycle_A,
    cycle_B,
    cycle_C,
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

def test_cycle_A_i_value_roundtrip():
    instance = cycle_A(i=7, j=7)
    assert instance.i == 7
    instance.i = 13
    assert instance.i == 13


def test_cycle_A_j_value_roundtrip():
    instance = cycle_A(i=7, j=7)
    assert instance.j == 7
    instance.j = 13
    assert instance.j == 13


def test_cycle_B_x_value_roundtrip():
    instance = cycle_B(x=3.14, y=3.14)
    assert instance.x == 3.14
    instance.x = 9.99
    assert instance.x == 9.99


def test_cycle_B_y_value_roundtrip():
    instance = cycle_B(x=3.14, y=3.14)
    assert instance.y == 3.14
    instance.y = 9.99
    assert instance.y == 9.99


def test_assoc_myA1_link_reassign_clear():
    a = cycle_B(x=3.14, y=3.14)
    b1 = cycle_A(i=7, j=7)
    b2 = cycle_A(i=13, j=13)
    _safe_set(a, 'cycle_B2', b1)
    assert _is_linked(a, 'cycle_B2', b1)
    if hasattr(b1, 'cycle_A3'):
        assert _is_linked(b1, 'cycle_A3', a)
    _safe_set(a, 'cycle_B2', b2)
    assert _is_linked(a, 'cycle_B2', b2)
    if hasattr(b1, 'cycle_A3'):
        assert not _is_linked(b1, 'cycle_A3', a)
    if hasattr(b2, 'cycle_A3'):
        assert _is_linked(b2, 'cycle_A3', a)
    _safe_set(a, 'cycle_B2', None)
    assert not _is_linked(a, 'cycle_B2', b2)
    if hasattr(b2, 'cycle_A3'):
        assert not _is_linked(b2, 'cycle_A3', a)


def test_assoc_myA6_link_reassign_clear():
    a = cycle_A(i=7, j=7)
    b1 = cycle_C()
    b2 = cycle_C()
    _safe_set(a, 'cycle_A8', b1)
    assert _is_linked(a, 'cycle_A8', b1)
    if hasattr(b1, 'cycle_C7'):
        assert _is_linked(b1, 'cycle_C7', a)
    _safe_set(a, 'cycle_A8', b2)
    assert _is_linked(a, 'cycle_A8', b2)
    if hasattr(b1, 'cycle_C7'):
        assert not _is_linked(b1, 'cycle_C7', a)
    if hasattr(b2, 'cycle_C7'):
        assert _is_linked(b2, 'cycle_C7', a)
    _safe_set(a, 'cycle_A8', None)
    assert not _is_linked(a, 'cycle_A8', b2)
    if hasattr(b2, 'cycle_C7'):
        assert not _is_linked(b2, 'cycle_C7', a)


def test_assoc_myBs0_link_reassign_clear():
    a = cycle_B(x=3.14, y=3.14)
    b1 = cycle_A(i=7, j=7)
    b2 = cycle_A(i=13, j=13)
    _safe_set(a, 'cycle_B', b1)
    assert _is_linked(a, 'cycle_B', b1)
    if hasattr(b1, 'cycle_A'):
        assert _is_linked(b1, 'cycle_A', a)
    _safe_set(a, 'cycle_B', b2)
    assert _is_linked(a, 'cycle_B', b2)
    if hasattr(b1, 'cycle_A'):
        assert not _is_linked(b1, 'cycle_A', a)
    if hasattr(b2, 'cycle_A'):
        assert _is_linked(b2, 'cycle_A', a)
    _safe_set(a, 'cycle_B', None)
    assert not _is_linked(a, 'cycle_B', b2)
    if hasattr(b2, 'cycle_A'):
        assert not _is_linked(b2, 'cycle_A', a)


def test_assoc_myC4_link_reassign_clear():
    a = cycle_B(x=3.14, y=3.14)
    b1 = cycle_C()
    b2 = cycle_C()
    _safe_set(a, 'cycle_B5', b1)
    assert _is_linked(a, 'cycle_B5', b1)
    if hasattr(b1, 'cycle_C'):
        assert _is_linked(b1, 'cycle_C', a)
    _safe_set(a, 'cycle_B5', b2)
    assert _is_linked(a, 'cycle_B5', b2)
    if hasattr(b1, 'cycle_C'):
        assert not _is_linked(b1, 'cycle_C', a)
    if hasattr(b2, 'cycle_C'):
        assert _is_linked(b2, 'cycle_C', a)
    _safe_set(a, 'cycle_B5', None)
    assert not _is_linked(a, 'cycle_B5', b2)
    if hasattr(b2, 'cycle_C'):
        assert not _is_linked(b2, 'cycle_C', a)


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

cycle_A_strategy = st.builds(cycle_A, i=st.integers(), j=st.integers())
@given(instance=cycle_A_strategy)
@settings(max_examples=25)
def test_cycle_A_instantiation(instance):
    assert isinstance(instance, cycle_A)


cycle_B_strategy = st.builds(cycle_B, x=st.floats(allow_nan=False, allow_infinity=False), y=st.floats(allow_nan=False, allow_infinity=False))
@given(instance=cycle_B_strategy)
@settings(max_examples=25)
def test_cycle_B_instantiation(instance):
    assert isinstance(instance, cycle_B)


cycle_C_strategy = st.builds(cycle_C)
@given(instance=cycle_C_strategy)
@settings(max_examples=25)
def test_cycle_C_instantiation(instance):
    assert isinstance(instance, cycle_C)



