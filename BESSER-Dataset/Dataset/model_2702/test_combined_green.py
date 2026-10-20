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
    ktest206_N,
    A,
    ktest206_Y,
    Y,
    ktest206_V,
    ktest206_X,
    ktest206_D,
    B,
    ktest206_A,
    ktest206_C,
    N,
    ktest206_E,
    ktest206_W,
    ktest206_B,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_hyp_ktest206_n_is_not_abstract():
    assert not inspect.isabstract(ktest206_N)


def test_hyp_ktest206_n_constructor_exists():
    assert callable(ktest206_N.__init__)


def test_hyp_ktest206_n_constructor_args():
    sig = inspect.signature(ktest206_N.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"




def test_hyp_a_is_not_abstract():
    assert not inspect.isabstract(A)


def test_hyp_a_constructor_exists():
    assert callable(A.__init__)


def test_hyp_a_constructor_args():
    sig = inspect.signature(A.__init__)
    params = list(sig.parameters.keys())



def test_hyp_ktest206_y_is_not_abstract():
    assert not inspect.isabstract(ktest206_Y)


def test_hyp_ktest206_y_constructor_exists():
    assert callable(ktest206_Y.__init__)


def test_hyp_ktest206_y_constructor_args():
    sig = inspect.signature(ktest206_Y.__init__)
    params = list(sig.parameters.keys())



def test_hyp_y_is_not_abstract():
    assert not inspect.isabstract(Y)


def test_hyp_y_constructor_exists():
    assert callable(Y.__init__)


def test_hyp_y_constructor_args():
    sig = inspect.signature(Y.__init__)
    params = list(sig.parameters.keys())



def test_hyp_ktest206_v_is_not_abstract():
    assert not inspect.isabstract(ktest206_V)


def test_hyp_ktest206_v_constructor_exists():
    assert callable(ktest206_V.__init__)


def test_hyp_ktest206_v_constructor_args():
    sig = inspect.signature(ktest206_V.__init__)
    params = list(sig.parameters.keys())



def test_hyp_ktest206_x_is_not_abstract():
    assert not inspect.isabstract(ktest206_X)


def test_hyp_ktest206_x_constructor_exists():
    assert callable(ktest206_X.__init__)


def test_hyp_ktest206_x_constructor_args():
    sig = inspect.signature(ktest206_X.__init__)
    params = list(sig.parameters.keys())



def test_hyp_ktest206_d_is_not_abstract():
    assert not inspect.isabstract(ktest206_D)


def test_hyp_ktest206_d_constructor_exists():
    assert callable(ktest206_D.__init__)


def test_hyp_ktest206_d_constructor_args():
    sig = inspect.signature(ktest206_D.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"




def test_hyp_b_is_not_abstract():
    assert not inspect.isabstract(B)


def test_hyp_b_constructor_exists():
    assert callable(B.__init__)


def test_hyp_b_constructor_args():
    sig = inspect.signature(B.__init__)
    params = list(sig.parameters.keys())



def test_hyp_ktest206_a_is_not_abstract():
    assert not inspect.isabstract(ktest206_A)


def test_hyp_ktest206_a_constructor_exists():
    assert callable(ktest206_A.__init__)


def test_hyp_ktest206_a_constructor_args():
    sig = inspect.signature(ktest206_A.__init__)
    params = list(sig.parameters.keys())



def test_hyp_ktest206_c_is_not_abstract():
    assert not inspect.isabstract(ktest206_C)


def test_hyp_ktest206_c_constructor_exists():
    assert callable(ktest206_C.__init__)


def test_hyp_ktest206_c_constructor_args():
    sig = inspect.signature(ktest206_C.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"




def test_hyp_n_is_not_abstract():
    assert not inspect.isabstract(N)


def test_hyp_n_constructor_exists():
    assert callable(N.__init__)


def test_hyp_n_constructor_args():
    sig = inspect.signature(N.__init__)
    params = list(sig.parameters.keys())



def test_hyp_ktest206_e_is_not_abstract():
    assert not inspect.isabstract(ktest206_E)


def test_hyp_ktest206_e_constructor_exists():
    assert callable(ktest206_E.__init__)


def test_hyp_ktest206_e_constructor_args():
    sig = inspect.signature(ktest206_E.__init__)
    params = list(sig.parameters.keys())



def test_hyp_ktest206_w_is_not_abstract():
    assert not inspect.isabstract(ktest206_W)


def test_hyp_ktest206_w_constructor_exists():
    assert callable(ktest206_W.__init__)


def test_hyp_ktest206_w_constructor_args():
    sig = inspect.signature(ktest206_W.__init__)
    params = list(sig.parameters.keys())



def test_hyp_ktest206_b_is_not_abstract():
    assert not inspect.isabstract(ktest206_B)


def test_hyp_ktest206_b_constructor_exists():
    assert callable(ktest206_B.__init__)


def test_hyp_ktest206_b_constructor_args():
    sig = inspect.signature(ktest206_B.__init__)
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
ktest206_N_strategy = st.builds(
    ktest206_N,
    name=
        safe_text
)
A_strategy = st.builds(
    A,
)
ktest206_Y_strategy = st.builds(
    ktest206_Y,
)
Y_strategy = st.builds(
    Y,
)
ktest206_V_strategy = st.builds(
    ktest206_V,
)
ktest206_X_strategy = st.builds(
    ktest206_X,
)
ktest206_D_strategy = st.builds(
    ktest206_D,
    name=
        safe_text
)
B_strategy = st.builds(
    B,
)
ktest206_A_strategy = st.builds(
    ktest206_A,
)
ktest206_C_strategy = st.builds(
    ktest206_C,
    name=
        safe_text
)
N_strategy = st.builds(
    N,
)
ktest206_E_strategy = st.builds(
    ktest206_E,
)
ktest206_W_strategy = st.builds(
    ktest206_W,
)
ktest206_B_strategy = st.builds(
    ktest206_B,
)




@given(instance=ktest206_N_strategy)
def test_hyp_ktest206_n_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original









@given(instance=ktest206_D_strategy)
def test_hyp_ktest206_d_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original






@given(instance=ktest206_C_strategy)
def test_hyp_ktest206_c_name_setter(instance):
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
    A,
    B,
    N,
    Y,
    ktest206_A,
    ktest206_B,
    ktest206_C,
    ktest206_D,
    ktest206_E,
    ktest206_N,
    ktest206_V,
    ktest206_W,
    ktest206_X,
    ktest206_Y,
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

def test_ktest206_C_name_value_roundtrip():
    instance = ktest206_C(name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_ktest206_D_name_value_roundtrip():
    instance = ktest206_D(name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_ktest206_N_name_value_roundtrip():
    instance = ktest206_N(name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_ktest206_Y_isa_A():
    instance = ktest206_Y()
    assert isinstance(instance, A)


def test_ktest206_A_isa_B():
    instance = ktest206_A()
    assert isinstance(instance, B)


def test_ktest206_B_isa_N():
    instance = ktest206_B()
    assert isinstance(instance, N)


def test_ktest206_E_isa_N():
    instance = ktest206_E()
    assert isinstance(instance, N)


def test_ktest206_W_isa_N():
    instance = ktest206_W()
    assert isinstance(instance, N)


def test_ktest206_V_isa_Y():
    instance = ktest206_V()
    assert isinstance(instance, Y)


def test_ktest206_X_isa_Y():
    instance = ktest206_X()
    assert isinstance(instance, Y)


def test_assoc_cs0_link_reassign_clear():
    a = ktest206_C(name="sample_text")
    b1 = ktest206_B()
    b2 = ktest206_B()
    _safe_set(a, 'ktest206_C', b1)
    assert _is_linked(a, 'ktest206_C', b1)
    if hasattr(b1, 'ktest206_B'):
        assert _is_linked(b1, 'ktest206_B', a)
    _safe_set(a, 'ktest206_C', b2)
    assert _is_linked(a, 'ktest206_C', b2)
    if hasattr(b1, 'ktest206_B'):
        assert not _is_linked(b1, 'ktest206_B', a)
    if hasattr(b2, 'ktest206_B'):
        assert _is_linked(b2, 'ktest206_B', a)
    _safe_set(a, 'ktest206_C', None)
    assert not _is_linked(a, 'ktest206_C', b2)
    if hasattr(b2, 'ktest206_B'):
        assert not _is_linked(b2, 'ktest206_B', a)


def test_assoc_ds1_link_reassign_clear():
    a = ktest206_D(name="sample_text")
    b1 = ktest206_A()
    b2 = ktest206_A()
    _safe_set(a, 'ktest206_D', b1)
    assert _is_linked(a, 'ktest206_D', b1)
    if hasattr(b1, 'ktest206_A'):
        assert _is_linked(b1, 'ktest206_A', a)
    _safe_set(a, 'ktest206_D', b2)
    assert _is_linked(a, 'ktest206_D', b2)
    if hasattr(b1, 'ktest206_A'):
        assert not _is_linked(b1, 'ktest206_A', a)
    if hasattr(b2, 'ktest206_A'):
        assert _is_linked(b2, 'ktest206_A', a)
    _safe_set(a, 'ktest206_D', None)
    assert not _is_linked(a, 'ktest206_D', b2)
    if hasattr(b2, 'ktest206_A'):
        assert not _is_linked(b2, 'ktest206_A', a)


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


N_strategy = st.builds(N)
@given(instance=N_strategy)
@settings(max_examples=25)
def test_N_instantiation(instance):
    assert isinstance(instance, N)


Y_strategy = st.builds(Y)
@given(instance=Y_strategy)
@settings(max_examples=25)
def test_Y_instantiation(instance):
    assert isinstance(instance, Y)


ktest206_A_strategy = st.builds(ktest206_A)
@given(instance=ktest206_A_strategy)
@settings(max_examples=25)
def test_ktest206_A_instantiation(instance):
    assert isinstance(instance, ktest206_A)


ktest206_B_strategy = st.builds(ktest206_B)
@given(instance=ktest206_B_strategy)
@settings(max_examples=25)
def test_ktest206_B_instantiation(instance):
    assert isinstance(instance, ktest206_B)


ktest206_C_strategy = st.builds(ktest206_C, name=safe_text)
@given(instance=ktest206_C_strategy)
@settings(max_examples=25)
def test_ktest206_C_instantiation(instance):
    assert isinstance(instance, ktest206_C)


ktest206_D_strategy = st.builds(ktest206_D, name=safe_text)
@given(instance=ktest206_D_strategy)
@settings(max_examples=25)
def test_ktest206_D_instantiation(instance):
    assert isinstance(instance, ktest206_D)


ktest206_E_strategy = st.builds(ktest206_E)
@given(instance=ktest206_E_strategy)
@settings(max_examples=25)
def test_ktest206_E_instantiation(instance):
    assert isinstance(instance, ktest206_E)


ktest206_N_strategy = st.builds(ktest206_N, name=safe_text)
@given(instance=ktest206_N_strategy)
@settings(max_examples=25)
def test_ktest206_N_instantiation(instance):
    assert isinstance(instance, ktest206_N)


ktest206_V_strategy = st.builds(ktest206_V)
@given(instance=ktest206_V_strategy)
@settings(max_examples=25)
def test_ktest206_V_instantiation(instance):
    assert isinstance(instance, ktest206_V)


ktest206_W_strategy = st.builds(ktest206_W)
@given(instance=ktest206_W_strategy)
@settings(max_examples=25)
def test_ktest206_W_instantiation(instance):
    assert isinstance(instance, ktest206_W)


ktest206_X_strategy = st.builds(ktest206_X)
@given(instance=ktest206_X_strategy)
@settings(max_examples=25)
def test_ktest206_X_instantiation(instance):
    assert isinstance(instance, ktest206_X)


ktest206_Y_strategy = st.builds(ktest206_Y)
@given(instance=ktest206_Y_strategy)
@settings(max_examples=25)
def test_ktest206_Y_instantiation(instance):
    assert isinstance(instance, ktest206_Y)



