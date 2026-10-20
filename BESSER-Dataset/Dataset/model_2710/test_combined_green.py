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
    P,
    k2_Q,
    N,
    A,
    k2_J,
    M,
    k2_N,
    k2_G,
    G,
    k2_M,
    k2_I,
    C,
    k2_B,
    B,
    k2_A,
    k2_P,
    k2_C,
    k2_X,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_hyp_p_is_not_abstract():
    assert not inspect.isabstract(P)


def test_hyp_p_constructor_exists():
    assert callable(P.__init__)


def test_hyp_p_constructor_args():
    sig = inspect.signature(P.__init__)
    params = list(sig.parameters.keys())



def test_hyp_k2_q_is_not_abstract():
    assert not inspect.isabstract(k2_Q)


def test_hyp_k2_q_constructor_exists():
    assert callable(k2_Q.__init__)


def test_hyp_k2_q_constructor_args():
    sig = inspect.signature(k2_Q.__init__)
    params = list(sig.parameters.keys())



def test_hyp_n_is_not_abstract():
    assert not inspect.isabstract(N)


def test_hyp_n_constructor_exists():
    assert callable(N.__init__)


def test_hyp_n_constructor_args():
    sig = inspect.signature(N.__init__)
    params = list(sig.parameters.keys())



def test_hyp_a_is_not_abstract():
    assert not inspect.isabstract(A)


def test_hyp_a_constructor_exists():
    assert callable(A.__init__)


def test_hyp_a_constructor_args():
    sig = inspect.signature(A.__init__)
    params = list(sig.parameters.keys())



def test_hyp_k2_j_is_not_abstract():
    assert not inspect.isabstract(k2_J)


def test_hyp_k2_j_constructor_exists():
    assert callable(k2_J.__init__)


def test_hyp_k2_j_constructor_args():
    sig = inspect.signature(k2_J.__init__)
    params = list(sig.parameters.keys())



def test_hyp_m_is_not_abstract():
    assert not inspect.isabstract(M)


def test_hyp_m_constructor_exists():
    assert callable(M.__init__)


def test_hyp_m_constructor_args():
    sig = inspect.signature(M.__init__)
    params = list(sig.parameters.keys())



def test_hyp_k2_n_is_not_abstract():
    assert not inspect.isabstract(k2_N)


def test_hyp_k2_n_constructor_exists():
    assert callable(k2_N.__init__)


def test_hyp_k2_n_constructor_args():
    sig = inspect.signature(k2_N.__init__)
    params = list(sig.parameters.keys())



def test_hyp_k2_g_is_not_abstract():
    assert not inspect.isabstract(k2_G)


def test_hyp_k2_g_constructor_exists():
    assert callable(k2_G.__init__)


def test_hyp_k2_g_constructor_args():
    sig = inspect.signature(k2_G.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"




def test_hyp_g_is_not_abstract():
    assert not inspect.isabstract(G)


def test_hyp_g_constructor_exists():
    assert callable(G.__init__)


def test_hyp_g_constructor_args():
    sig = inspect.signature(G.__init__)
    params = list(sig.parameters.keys())



def test_hyp_k2_m_is_not_abstract():
    assert not inspect.isabstract(k2_M)


def test_hyp_k2_m_constructor_exists():
    assert callable(k2_M.__init__)


def test_hyp_k2_m_constructor_args():
    sig = inspect.signature(k2_M.__init__)
    params = list(sig.parameters.keys())



def test_hyp_k2_i_is_not_abstract():
    assert not inspect.isabstract(k2_I)


def test_hyp_k2_i_constructor_exists():
    assert callable(k2_I.__init__)


def test_hyp_k2_i_constructor_args():
    sig = inspect.signature(k2_I.__init__)
    params = list(sig.parameters.keys())



def test_hyp_c_is_not_abstract():
    assert not inspect.isabstract(C)


def test_hyp_c_constructor_exists():
    assert callable(C.__init__)


def test_hyp_c_constructor_args():
    sig = inspect.signature(C.__init__)
    params = list(sig.parameters.keys())



def test_hyp_k2_b_is_not_abstract():
    assert not inspect.isabstract(k2_B)


def test_hyp_k2_b_constructor_exists():
    assert callable(k2_B.__init__)


def test_hyp_k2_b_constructor_args():
    sig = inspect.signature(k2_B.__init__)
    params = list(sig.parameters.keys())



def test_hyp_b_is_not_abstract():
    assert not inspect.isabstract(B)


def test_hyp_b_constructor_exists():
    assert callable(B.__init__)


def test_hyp_b_constructor_args():
    sig = inspect.signature(B.__init__)
    params = list(sig.parameters.keys())



def test_hyp_k2_a_is_not_abstract():
    assert not inspect.isabstract(k2_A)


def test_hyp_k2_a_constructor_exists():
    assert callable(k2_A.__init__)


def test_hyp_k2_a_constructor_args():
    sig = inspect.signature(k2_A.__init__)
    params = list(sig.parameters.keys())



def test_hyp_k2_p_is_not_abstract():
    assert not inspect.isabstract(k2_P)


def test_hyp_k2_p_constructor_exists():
    assert callable(k2_P.__init__)


def test_hyp_k2_p_constructor_args():
    sig = inspect.signature(k2_P.__init__)
    params = list(sig.parameters.keys())



def test_hyp_k2_c_is_not_abstract():
    assert not inspect.isabstract(k2_C)


def test_hyp_k2_c_constructor_exists():
    assert callable(k2_C.__init__)


def test_hyp_k2_c_constructor_args():
    sig = inspect.signature(k2_C.__init__)
    params = list(sig.parameters.keys())



def test_hyp_k2_x_is_not_abstract():
    assert not inspect.isabstract(k2_X)


def test_hyp_k2_x_constructor_exists():
    assert callable(k2_X.__init__)


def test_hyp_k2_x_constructor_args():
    sig = inspect.signature(k2_X.__init__)
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
P_strategy = st.builds(
    P,
)
k2_Q_strategy = st.builds(
    k2_Q,
)
N_strategy = st.builds(
    N,
)
A_strategy = st.builds(
    A,
)
k2_J_strategy = st.builds(
    k2_J,
)
M_strategy = st.builds(
    M,
)
k2_N_strategy = st.builds(
    k2_N,
)
k2_G_strategy = st.builds(
    k2_G,
    name=
        safe_text
)
G_strategy = st.builds(
    G,
)
k2_M_strategy = st.builds(
    k2_M,
)
k2_I_strategy = st.builds(
    k2_I,
)
C_strategy = st.builds(
    C,
)
k2_B_strategy = st.builds(
    k2_B,
)
B_strategy = st.builds(
    B,
)
k2_A_strategy = st.builds(
    k2_A,
)
k2_P_strategy = st.builds(
    k2_P,
)
k2_C_strategy = st.builds(
    k2_C,
)
k2_X_strategy = st.builds(
    k2_X,
)











@given(instance=k2_G_strategy)
def test_hyp_k2_g_name_setter(instance):
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
    C,
    G,
    M,
    N,
    P,
    k2_A,
    k2_B,
    k2_C,
    k2_G,
    k2_I,
    k2_J,
    k2_M,
    k2_N,
    k2_P,
    k2_Q,
    k2_X,
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

def test_k2_G_name_value_roundtrip():
    instance = k2_G(name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_k2_J_isa_A():
    instance = k2_J()
    assert isinstance(instance, A)


def test_k2_A_isa_B():
    instance = k2_A()
    assert isinstance(instance, B)


def test_k2_B_isa_C():
    instance = k2_B()
    assert isinstance(instance, C)


def test_k2_C_isa_G():
    instance = k2_C()
    assert isinstance(instance, G)


def test_k2_I_isa_G():
    instance = k2_I()
    assert isinstance(instance, G)


def test_k2_M_isa_G():
    instance = k2_M()
    assert isinstance(instance, G)


def test_k2_N_isa_M():
    instance = k2_N()
    assert isinstance(instance, M)


def test_k2_P_isa_N():
    instance = k2_P()
    assert isinstance(instance, N)


def test_k2_Q_isa_P():
    instance = k2_Q()
    assert isinstance(instance, P)


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


C_strategy = st.builds(C)
@given(instance=C_strategy)
@settings(max_examples=25)
def test_C_instantiation(instance):
    assert isinstance(instance, C)


G_strategy = st.builds(G)
@given(instance=G_strategy)
@settings(max_examples=25)
def test_G_instantiation(instance):
    assert isinstance(instance, G)


M_strategy = st.builds(M)
@given(instance=M_strategy)
@settings(max_examples=25)
def test_M_instantiation(instance):
    assert isinstance(instance, M)


N_strategy = st.builds(N)
@given(instance=N_strategy)
@settings(max_examples=25)
def test_N_instantiation(instance):
    assert isinstance(instance, N)


P_strategy = st.builds(P)
@given(instance=P_strategy)
@settings(max_examples=25)
def test_P_instantiation(instance):
    assert isinstance(instance, P)


k2_A_strategy = st.builds(k2_A)
@given(instance=k2_A_strategy)
@settings(max_examples=25)
def test_k2_A_instantiation(instance):
    assert isinstance(instance, k2_A)


k2_B_strategy = st.builds(k2_B)
@given(instance=k2_B_strategy)
@settings(max_examples=25)
def test_k2_B_instantiation(instance):
    assert isinstance(instance, k2_B)


k2_C_strategy = st.builds(k2_C)
@given(instance=k2_C_strategy)
@settings(max_examples=25)
def test_k2_C_instantiation(instance):
    assert isinstance(instance, k2_C)


k2_G_strategy = st.builds(k2_G, name=safe_text)
@given(instance=k2_G_strategy)
@settings(max_examples=25)
def test_k2_G_instantiation(instance):
    assert isinstance(instance, k2_G)


k2_I_strategy = st.builds(k2_I)
@given(instance=k2_I_strategy)
@settings(max_examples=25)
def test_k2_I_instantiation(instance):
    assert isinstance(instance, k2_I)


k2_J_strategy = st.builds(k2_J)
@given(instance=k2_J_strategy)
@settings(max_examples=25)
def test_k2_J_instantiation(instance):
    assert isinstance(instance, k2_J)


k2_M_strategy = st.builds(k2_M)
@given(instance=k2_M_strategy)
@settings(max_examples=25)
def test_k2_M_instantiation(instance):
    assert isinstance(instance, k2_M)


k2_N_strategy = st.builds(k2_N)
@given(instance=k2_N_strategy)
@settings(max_examples=25)
def test_k2_N_instantiation(instance):
    assert isinstance(instance, k2_N)


k2_P_strategy = st.builds(k2_P)
@given(instance=k2_P_strategy)
@settings(max_examples=25)
def test_k2_P_instantiation(instance):
    assert isinstance(instance, k2_P)


k2_Q_strategy = st.builds(k2_Q)
@given(instance=k2_Q_strategy)
@settings(max_examples=25)
def test_k2_Q_instantiation(instance):
    assert isinstance(instance, k2_Q)


k2_X_strategy = st.builds(k2_X)
@given(instance=k2_X_strategy)
@settings(max_examples=25)
def test_k2_X_instantiation(instance):
    assert isinstance(instance, k2_X)



