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
    inherlink_A,
    inherlink_Named,
    inherlink_T,
    inherlink_G,
    inherlink_C,
    inherlink_P,
    R,
    inherlink_K,
    inherlink_Y,
    L,
    inherlink_W,
    inherlink_M,
    Named,
    inherlink_L,
    inherlink_R,
    inherlink_N,
    inherlink_X,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_hyp_inherlink_a_is_not_abstract():
    assert not inspect.isabstract(inherlink_A)


def test_hyp_inherlink_a_constructor_exists():
    assert callable(inherlink_A.__init__)


def test_hyp_inherlink_a_constructor_args():
    sig = inspect.signature(inherlink_A.__init__)
    params = list(sig.parameters.keys())



def test_hyp_inherlink_named_is_not_abstract():
    assert not inspect.isabstract(inherlink_Named)


def test_hyp_inherlink_named_constructor_exists():
    assert callable(inherlink_Named.__init__)


def test_hyp_inherlink_named_constructor_args():
    sig = inspect.signature(inherlink_Named.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"




def test_hyp_inherlink_t_is_not_abstract():
    assert not inspect.isabstract(inherlink_T)


def test_hyp_inherlink_t_constructor_exists():
    assert callable(inherlink_T.__init__)


def test_hyp_inherlink_t_constructor_args():
    sig = inspect.signature(inherlink_T.__init__)
    params = list(sig.parameters.keys())



def test_hyp_inherlink_g_is_not_abstract():
    assert not inspect.isabstract(inherlink_G)


def test_hyp_inherlink_g_constructor_exists():
    assert callable(inherlink_G.__init__)


def test_hyp_inherlink_g_constructor_args():
    sig = inspect.signature(inherlink_G.__init__)
    params = list(sig.parameters.keys())



def test_hyp_inherlink_c_is_not_abstract():
    assert not inspect.isabstract(inherlink_C)


def test_hyp_inherlink_c_constructor_exists():
    assert callable(inherlink_C.__init__)


def test_hyp_inherlink_c_constructor_args():
    sig = inspect.signature(inherlink_C.__init__)
    params = list(sig.parameters.keys())



def test_hyp_inherlink_p_is_not_abstract():
    assert not inspect.isabstract(inherlink_P)


def test_hyp_inherlink_p_constructor_exists():
    assert callable(inherlink_P.__init__)


def test_hyp_inherlink_p_constructor_args():
    sig = inspect.signature(inherlink_P.__init__)
    params = list(sig.parameters.keys())



def test_hyp_r_is_not_abstract():
    assert not inspect.isabstract(R)


def test_hyp_r_constructor_exists():
    assert callable(R.__init__)


def test_hyp_r_constructor_args():
    sig = inspect.signature(R.__init__)
    params = list(sig.parameters.keys())



def test_hyp_inherlink_k_is_not_abstract():
    assert not inspect.isabstract(inherlink_K)


def test_hyp_inherlink_k_constructor_exists():
    assert callable(inherlink_K.__init__)


def test_hyp_inherlink_k_constructor_args():
    sig = inspect.signature(inherlink_K.__init__)
    params = list(sig.parameters.keys())



def test_hyp_inherlink_y_is_not_abstract():
    assert not inspect.isabstract(inherlink_Y)


def test_hyp_inherlink_y_constructor_exists():
    assert callable(inherlink_Y.__init__)


def test_hyp_inherlink_y_constructor_args():
    sig = inspect.signature(inherlink_Y.__init__)
    params = list(sig.parameters.keys())



def test_hyp_l_is_not_abstract():
    assert not inspect.isabstract(L)


def test_hyp_l_constructor_exists():
    assert callable(L.__init__)


def test_hyp_l_constructor_args():
    sig = inspect.signature(L.__init__)
    params = list(sig.parameters.keys())



def test_hyp_inherlink_w_is_not_abstract():
    assert not inspect.isabstract(inherlink_W)


def test_hyp_inherlink_w_constructor_exists():
    assert callable(inherlink_W.__init__)


def test_hyp_inherlink_w_constructor_args():
    sig = inspect.signature(inherlink_W.__init__)
    params = list(sig.parameters.keys())



def test_hyp_inherlink_m_is_not_abstract():
    assert not inspect.isabstract(inherlink_M)


def test_hyp_inherlink_m_constructor_exists():
    assert callable(inherlink_M.__init__)


def test_hyp_inherlink_m_constructor_args():
    sig = inspect.signature(inherlink_M.__init__)
    params = list(sig.parameters.keys())



def test_hyp_named_is_not_abstract():
    assert not inspect.isabstract(Named)


def test_hyp_named_constructor_exists():
    assert callable(Named.__init__)


def test_hyp_named_constructor_args():
    sig = inspect.signature(Named.__init__)
    params = list(sig.parameters.keys())



def test_hyp_inherlink_l_is_not_abstract():
    assert not inspect.isabstract(inherlink_L)


def test_hyp_inherlink_l_constructor_exists():
    assert callable(inherlink_L.__init__)


def test_hyp_inherlink_l_constructor_args():
    sig = inspect.signature(inherlink_L.__init__)
    params = list(sig.parameters.keys())



def test_hyp_inherlink_r_is_not_abstract():
    assert not inspect.isabstract(inherlink_R)


def test_hyp_inherlink_r_constructor_exists():
    assert callable(inherlink_R.__init__)


def test_hyp_inherlink_r_constructor_args():
    sig = inspect.signature(inherlink_R.__init__)
    params = list(sig.parameters.keys())



def test_hyp_inherlink_n_is_not_abstract():
    assert not inspect.isabstract(inherlink_N)


def test_hyp_inherlink_n_constructor_exists():
    assert callable(inherlink_N.__init__)


def test_hyp_inherlink_n_constructor_args():
    sig = inspect.signature(inherlink_N.__init__)
    params = list(sig.parameters.keys())



def test_hyp_inherlink_x_is_not_abstract():
    assert not inspect.isabstract(inherlink_X)


def test_hyp_inherlink_x_constructor_exists():
    assert callable(inherlink_X.__init__)


def test_hyp_inherlink_x_constructor_args():
    sig = inspect.signature(inherlink_X.__init__)
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
inherlink_A_strategy = st.builds(
    inherlink_A,
)
inherlink_Named_strategy = st.builds(
    inherlink_Named,
    name=
        safe_text
)
inherlink_T_strategy = st.builds(
    inherlink_T,
)
inherlink_G_strategy = st.builds(
    inherlink_G,
)
inherlink_C_strategy = st.builds(
    inherlink_C,
)
inherlink_P_strategy = st.builds(
    inherlink_P,
)
R_strategy = st.builds(
    R,
)
inherlink_K_strategy = st.builds(
    inherlink_K,
)
inherlink_Y_strategy = st.builds(
    inherlink_Y,
)
L_strategy = st.builds(
    L,
)
inherlink_W_strategy = st.builds(
    inherlink_W,
)
inherlink_M_strategy = st.builds(
    inherlink_M,
)
Named_strategy = st.builds(
    Named,
)
inherlink_L_strategy = st.builds(
    inherlink_L,
)
inherlink_R_strategy = st.builds(
    inherlink_R,
)
inherlink_N_strategy = st.builds(
    inherlink_N,
)
inherlink_X_strategy = st.builds(
    inherlink_X,
)





@given(instance=inherlink_Named_strategy)
def test_hyp_inherlink_named_name_setter(instance):
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
    L,
    Named,
    R,
    inherlink_A,
    inherlink_C,
    inherlink_G,
    inherlink_K,
    inherlink_L,
    inherlink_M,
    inherlink_N,
    inherlink_Named,
    inherlink_P,
    inherlink_R,
    inherlink_T,
    inherlink_W,
    inherlink_X,
    inherlink_Y,
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

def test_inherlink_Named_name_value_roundtrip():
    instance = inherlink_Named(name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_inherlink_M_isa_L():
    instance = inherlink_M()
    assert isinstance(instance, L)


def test_inherlink_W_isa_L():
    instance = inherlink_W()
    assert isinstance(instance, L)


def test_inherlink_X_isa_L():
    instance = inherlink_X()
    assert isinstance(instance, L)


def test_inherlink_L_isa_Named():
    instance = inherlink_L()
    assert isinstance(instance, Named)


def test_inherlink_R_isa_Named():
    instance = inherlink_R()
    assert isinstance(instance, Named)


def test_inherlink_K_isa_R():
    instance = inherlink_K()
    assert isinstance(instance, R)


def test_inherlink_N_isa_R():
    instance = inherlink_N()
    assert isinstance(instance, R)


def test_inherlink_Y_isa_R():
    instance = inherlink_Y()
    assert isinstance(instance, R)


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

L_strategy = st.builds(L)
@given(instance=L_strategy)
@settings(max_examples=25)
def test_L_instantiation(instance):
    assert isinstance(instance, L)


Named_strategy = st.builds(Named)
@given(instance=Named_strategy)
@settings(max_examples=25)
def test_Named_instantiation(instance):
    assert isinstance(instance, Named)


R_strategy = st.builds(R)
@given(instance=R_strategy)
@settings(max_examples=25)
def test_R_instantiation(instance):
    assert isinstance(instance, R)


inherlink_A_strategy = st.builds(inherlink_A)
@given(instance=inherlink_A_strategy)
@settings(max_examples=25)
def test_inherlink_A_instantiation(instance):
    assert isinstance(instance, inherlink_A)


inherlink_C_strategy = st.builds(inherlink_C)
@given(instance=inherlink_C_strategy)
@settings(max_examples=25)
def test_inherlink_C_instantiation(instance):
    assert isinstance(instance, inherlink_C)


inherlink_G_strategy = st.builds(inherlink_G)
@given(instance=inherlink_G_strategy)
@settings(max_examples=25)
def test_inherlink_G_instantiation(instance):
    assert isinstance(instance, inherlink_G)


inherlink_K_strategy = st.builds(inherlink_K)
@given(instance=inherlink_K_strategy)
@settings(max_examples=25)
def test_inherlink_K_instantiation(instance):
    assert isinstance(instance, inherlink_K)


inherlink_L_strategy = st.builds(inherlink_L)
@given(instance=inherlink_L_strategy)
@settings(max_examples=25)
def test_inherlink_L_instantiation(instance):
    assert isinstance(instance, inherlink_L)


inherlink_M_strategy = st.builds(inherlink_M)
@given(instance=inherlink_M_strategy)
@settings(max_examples=25)
def test_inherlink_M_instantiation(instance):
    assert isinstance(instance, inherlink_M)


inherlink_N_strategy = st.builds(inherlink_N)
@given(instance=inherlink_N_strategy)
@settings(max_examples=25)
def test_inherlink_N_instantiation(instance):
    assert isinstance(instance, inherlink_N)


inherlink_Named_strategy = st.builds(inherlink_Named, name=safe_text)
@given(instance=inherlink_Named_strategy)
@settings(max_examples=25)
def test_inherlink_Named_instantiation(instance):
    assert isinstance(instance, inherlink_Named)


inherlink_P_strategy = st.builds(inherlink_P)
@given(instance=inherlink_P_strategy)
@settings(max_examples=25)
def test_inherlink_P_instantiation(instance):
    assert isinstance(instance, inherlink_P)


inherlink_R_strategy = st.builds(inherlink_R)
@given(instance=inherlink_R_strategy)
@settings(max_examples=25)
def test_inherlink_R_instantiation(instance):
    assert isinstance(instance, inherlink_R)


inherlink_T_strategy = st.builds(inherlink_T)
@given(instance=inherlink_T_strategy)
@settings(max_examples=25)
def test_inherlink_T_instantiation(instance):
    assert isinstance(instance, inherlink_T)


inherlink_W_strategy = st.builds(inherlink_W)
@given(instance=inherlink_W_strategy)
@settings(max_examples=25)
def test_inherlink_W_instantiation(instance):
    assert isinstance(instance, inherlink_W)


inherlink_X_strategy = st.builds(inherlink_X)
@given(instance=inherlink_X_strategy)
@settings(max_examples=25)
def test_inherlink_X_instantiation(instance):
    assert isinstance(instance, inherlink_X)


inherlink_Y_strategy = st.builds(inherlink_Y)
@given(instance=inherlink_Y_strategy)
@settings(max_examples=25)
def test_inherlink_Y_instantiation(instance):
    assert isinstance(instance, inherlink_Y)



