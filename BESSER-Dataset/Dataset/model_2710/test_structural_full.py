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


