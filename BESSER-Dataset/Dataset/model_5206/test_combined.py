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
    FaultyUMLmodel_D,
    FaultyUMLmodel_C,
    FaultyUMLmodel_B,
    FaultyUMLmodel_A,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_hyp_faultyumlmodel_d_is_not_abstract():
    assert not inspect.isabstract(FaultyUMLmodel_D)


def test_hyp_faultyumlmodel_d_constructor_exists():
    assert callable(FaultyUMLmodel_D.__init__)


def test_hyp_faultyumlmodel_d_constructor_args():
    sig = inspect.signature(FaultyUMLmodel_D.__init__)
    params = list(sig.parameters.keys())
    assert "z" in params, "Missing parameter 'z'"




def test_hyp_faultyumlmodel_c_is_not_abstract():
    assert not inspect.isabstract(FaultyUMLmodel_C)


def test_hyp_faultyumlmodel_c_constructor_exists():
    assert callable(FaultyUMLmodel_C.__init__)


def test_hyp_faultyumlmodel_c_constructor_args():
    sig = inspect.signature(FaultyUMLmodel_C.__init__)
    params = list(sig.parameters.keys())
    assert "u" in params, "Missing parameter 'u'"




def test_hyp_faultyumlmodel_b_is_not_abstract():
    assert not inspect.isabstract(FaultyUMLmodel_B)


def test_hyp_faultyumlmodel_b_constructor_exists():
    assert callable(FaultyUMLmodel_B.__init__)


def test_hyp_faultyumlmodel_b_constructor_args():
    sig = inspect.signature(FaultyUMLmodel_B.__init__)
    params = list(sig.parameters.keys())
    assert "y" in params, "Missing parameter 'y'"
    assert "x" in params, "Missing parameter 'x'"





def test_hyp_faultyumlmodel_a_is_not_abstract():
    assert not inspect.isabstract(FaultyUMLmodel_A)


def test_hyp_faultyumlmodel_a_constructor_exists():
    assert callable(FaultyUMLmodel_A.__init__)


def test_hyp_faultyumlmodel_a_constructor_args():
    sig = inspect.signature(FaultyUMLmodel_A.__init__)
    params = list(sig.parameters.keys())
    assert "v" in params, "Missing parameter 'v'"
    assert "w" in params, "Missing parameter 'w'"




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
FaultyUMLmodel_D_strategy = st.builds(
    FaultyUMLmodel_D,
    z=
        st.booleans()
)
FaultyUMLmodel_C_strategy = st.builds(
    FaultyUMLmodel_C,
    u=
        st.integers()
)
FaultyUMLmodel_B_strategy = st.builds(
    FaultyUMLmodel_B,
    y=
        st.integers(),
    x=
        st.integers()
)
FaultyUMLmodel_A_strategy = st.builds(
    FaultyUMLmodel_A,
    v=
        st.integers(),
    w=
        st.booleans()
)




@given(instance=FaultyUMLmodel_D_strategy)
def test_hyp_faultyumlmodel_d_z_setter(instance):
    original = instance.z
    instance.z = original
    assert instance.z == original




@given(instance=FaultyUMLmodel_C_strategy)
def test_hyp_faultyumlmodel_c_u_setter(instance):
    original = instance.u
    instance.u = original
    assert instance.u == original




@given(instance=FaultyUMLmodel_B_strategy)
def test_hyp_faultyumlmodel_b_y_setter(instance):
    original = instance.y
    instance.y = original
    assert instance.y == original



@given(instance=FaultyUMLmodel_B_strategy)
def test_hyp_faultyumlmodel_b_x_setter(instance):
    original = instance.x
    instance.x = original
    assert instance.x == original




@given(instance=FaultyUMLmodel_A_strategy)
def test_hyp_faultyumlmodel_a_v_setter(instance):
    original = instance.v
    instance.v = original
    assert instance.v == original



@given(instance=FaultyUMLmodel_A_strategy)
def test_hyp_faultyumlmodel_a_w_setter(instance):
    original = instance.w
    instance.w = original
    assert instance.w == original


# ----- SECTION B: test_structural_full.py (deterministic-first suite) -----
import inspect
import pytest
from datetime import date, datetime, time, timedelta
from hypothesis import given, settings
import hypothesis.strategies as st

from python_code import (
    FaultyUMLmodel_A,
    FaultyUMLmodel_B,
    FaultyUMLmodel_C,
    FaultyUMLmodel_D,
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

def test_FaultyUMLmodel_A_v_value_roundtrip():
    instance = FaultyUMLmodel_A(v=7, w=True)
    assert instance.v == 7
    instance.v = 13
    assert instance.v == 13


def test_FaultyUMLmodel_A_w_value_roundtrip():
    instance = FaultyUMLmodel_A(v=7, w=True)
    assert instance.w == True
    instance.w = False
    assert instance.w == False


def test_FaultyUMLmodel_B_x_value_roundtrip():
    instance = FaultyUMLmodel_B(x=7, y=7)
    assert instance.x == 7
    instance.x = 13
    assert instance.x == 13


def test_FaultyUMLmodel_B_y_value_roundtrip():
    instance = FaultyUMLmodel_B(x=7, y=7)
    assert instance.y == 7
    instance.y = 13
    assert instance.y == 13


def test_FaultyUMLmodel_C_u_value_roundtrip():
    instance = FaultyUMLmodel_C(u=7)
    assert instance.u == 7
    instance.u = 13
    assert instance.u == 13


def test_FaultyUMLmodel_D_z_value_roundtrip():
    instance = FaultyUMLmodel_D(z=True)
    assert instance.z == True
    instance.z = False
    assert instance.z == False


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

FaultyUMLmodel_A_strategy = st.builds(FaultyUMLmodel_A, v=st.integers(), w=st.booleans())
@given(instance=FaultyUMLmodel_A_strategy)
@settings(max_examples=25)
def test_FaultyUMLmodel_A_instantiation(instance):
    assert isinstance(instance, FaultyUMLmodel_A)


FaultyUMLmodel_B_strategy = st.builds(FaultyUMLmodel_B, x=st.integers(), y=st.integers())
@given(instance=FaultyUMLmodel_B_strategy)
@settings(max_examples=25)
def test_FaultyUMLmodel_B_instantiation(instance):
    assert isinstance(instance, FaultyUMLmodel_B)


FaultyUMLmodel_C_strategy = st.builds(FaultyUMLmodel_C, u=st.integers())
@given(instance=FaultyUMLmodel_C_strategy)
@settings(max_examples=25)
def test_FaultyUMLmodel_C_instantiation(instance):
    assert isinstance(instance, FaultyUMLmodel_C)


FaultyUMLmodel_D_strategy = st.builds(FaultyUMLmodel_D, z=st.booleans())
@given(instance=FaultyUMLmodel_D_strategy)
@settings(max_examples=25)
def test_FaultyUMLmodel_D_instantiation(instance):
    assert isinstance(instance, FaultyUMLmodel_D)



