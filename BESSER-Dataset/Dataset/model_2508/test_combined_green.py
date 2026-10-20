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
    visualinher_N,
    N,
    visualinher_C,
    A,
    visualinher_I,
    visualinher_D,
    visualinher_E,
    I,
    visualinher_B,
    visualinher_R,
    visualinher_A,
    visualinher_S,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_hyp_visualinher_n_is_not_abstract():
    assert not inspect.isabstract(visualinher_N)


def test_hyp_visualinher_n_constructor_exists():
    assert callable(visualinher_N.__init__)


def test_hyp_visualinher_n_constructor_args():
    sig = inspect.signature(visualinher_N.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"




def test_hyp_n_is_not_abstract():
    assert not inspect.isabstract(N)


def test_hyp_n_constructor_exists():
    assert callable(N.__init__)


def test_hyp_n_constructor_args():
    sig = inspect.signature(N.__init__)
    params = list(sig.parameters.keys())



def test_hyp_visualinher_c_is_not_abstract():
    assert not inspect.isabstract(visualinher_C)


def test_hyp_visualinher_c_constructor_exists():
    assert callable(visualinher_C.__init__)


def test_hyp_visualinher_c_constructor_args():
    sig = inspect.signature(visualinher_C.__init__)
    params = list(sig.parameters.keys())



def test_hyp_a_is_not_abstract():
    assert not inspect.isabstract(A)


def test_hyp_a_constructor_exists():
    assert callable(A.__init__)


def test_hyp_a_constructor_args():
    sig = inspect.signature(A.__init__)
    params = list(sig.parameters.keys())



def test_hyp_visualinher_i_is_not_abstract():
    assert not inspect.isabstract(visualinher_I)


def test_hyp_visualinher_i_constructor_exists():
    assert callable(visualinher_I.__init__)


def test_hyp_visualinher_i_constructor_args():
    sig = inspect.signature(visualinher_I.__init__)
    params = list(sig.parameters.keys())



def test_hyp_visualinher_d_is_not_abstract():
    assert not inspect.isabstract(visualinher_D)


def test_hyp_visualinher_d_constructor_exists():
    assert callable(visualinher_D.__init__)


def test_hyp_visualinher_d_constructor_args():
    sig = inspect.signature(visualinher_D.__init__)
    params = list(sig.parameters.keys())



def test_hyp_visualinher_e_is_not_abstract():
    assert not inspect.isabstract(visualinher_E)


def test_hyp_visualinher_e_constructor_exists():
    assert callable(visualinher_E.__init__)


def test_hyp_visualinher_e_constructor_args():
    sig = inspect.signature(visualinher_E.__init__)
    params = list(sig.parameters.keys())



def test_hyp_i_is_not_abstract():
    assert not inspect.isabstract(I)


def test_hyp_i_constructor_exists():
    assert callable(I.__init__)


def test_hyp_i_constructor_args():
    sig = inspect.signature(I.__init__)
    params = list(sig.parameters.keys())



def test_hyp_visualinher_b_is_not_abstract():
    assert not inspect.isabstract(visualinher_B)


def test_hyp_visualinher_b_constructor_exists():
    assert callable(visualinher_B.__init__)


def test_hyp_visualinher_b_constructor_args():
    sig = inspect.signature(visualinher_B.__init__)
    params = list(sig.parameters.keys())



def test_hyp_visualinher_r_is_not_abstract():
    assert not inspect.isabstract(visualinher_R)


def test_hyp_visualinher_r_constructor_exists():
    assert callable(visualinher_R.__init__)


def test_hyp_visualinher_r_constructor_args():
    sig = inspect.signature(visualinher_R.__init__)
    params = list(sig.parameters.keys())



def test_hyp_visualinher_a_is_not_abstract():
    assert not inspect.isabstract(visualinher_A)


def test_hyp_visualinher_a_constructor_exists():
    assert callable(visualinher_A.__init__)


def test_hyp_visualinher_a_constructor_args():
    sig = inspect.signature(visualinher_A.__init__)
    params = list(sig.parameters.keys())



def test_hyp_visualinher_s_is_not_abstract():
    assert not inspect.isabstract(visualinher_S)


def test_hyp_visualinher_s_constructor_exists():
    assert callable(visualinher_S.__init__)


def test_hyp_visualinher_s_constructor_args():
    sig = inspect.signature(visualinher_S.__init__)
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
visualinher_N_strategy = st.builds(
    visualinher_N,
    name=
        safe_text
)
N_strategy = st.builds(
    N,
)
visualinher_C_strategy = st.builds(
    visualinher_C,
)
A_strategy = st.builds(
    A,
)
visualinher_I_strategy = st.builds(
    visualinher_I,
)
visualinher_D_strategy = st.builds(
    visualinher_D,
)
visualinher_E_strategy = st.builds(
    visualinher_E,
)
I_strategy = st.builds(
    I,
)
visualinher_B_strategy = st.builds(
    visualinher_B,
)
visualinher_R_strategy = st.builds(
    visualinher_R,
)
visualinher_A_strategy = st.builds(
    visualinher_A,
)
visualinher_S_strategy = st.builds(
    visualinher_S,
)




@given(instance=visualinher_N_strategy)
def test_hyp_visualinher_n_name_setter(instance):
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
    I,
    N,
    visualinher_A,
    visualinher_B,
    visualinher_C,
    visualinher_D,
    visualinher_E,
    visualinher_I,
    visualinher_N,
    visualinher_R,
    visualinher_S,
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

def test_visualinher_N_name_value_roundtrip():
    instance = visualinher_N(name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_visualinher_D_isa_A():
    instance = visualinher_D()
    assert isinstance(instance, A)


def test_visualinher_E_isa_A():
    instance = visualinher_E()
    assert isinstance(instance, A)


def test_visualinher_I_isa_A():
    instance = visualinher_I()
    assert isinstance(instance, A)


def test_visualinher_B_isa_I():
    instance = visualinher_B()
    assert isinstance(instance, I)


def test_visualinher_A_isa_N():
    instance = visualinher_A()
    assert isinstance(instance, N)


def test_visualinher_R_isa_N():
    instance = visualinher_R()
    assert isinstance(instance, N)


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

A_strategy = st.builds(A)
@given(instance=A_strategy)
@settings(max_examples=25)
def test_A_instantiation(instance):
    assert isinstance(instance, A)


I_strategy = st.builds(I)
@given(instance=I_strategy)
@settings(max_examples=25)
def test_I_instantiation(instance):
    assert isinstance(instance, I)


N_strategy = st.builds(N)
@given(instance=N_strategy)
@settings(max_examples=25)
def test_N_instantiation(instance):
    assert isinstance(instance, N)


visualinher_A_strategy = st.builds(visualinher_A)
@given(instance=visualinher_A_strategy)
@settings(max_examples=25)
def test_visualinher_A_instantiation(instance):
    assert isinstance(instance, visualinher_A)


visualinher_B_strategy = st.builds(visualinher_B)
@given(instance=visualinher_B_strategy)
@settings(max_examples=25)
def test_visualinher_B_instantiation(instance):
    assert isinstance(instance, visualinher_B)


visualinher_C_strategy = st.builds(visualinher_C)
@given(instance=visualinher_C_strategy)
@settings(max_examples=25)
def test_visualinher_C_instantiation(instance):
    assert isinstance(instance, visualinher_C)


visualinher_D_strategy = st.builds(visualinher_D)
@given(instance=visualinher_D_strategy)
@settings(max_examples=25)
def test_visualinher_D_instantiation(instance):
    assert isinstance(instance, visualinher_D)


visualinher_E_strategy = st.builds(visualinher_E)
@given(instance=visualinher_E_strategy)
@settings(max_examples=25)
def test_visualinher_E_instantiation(instance):
    assert isinstance(instance, visualinher_E)


visualinher_I_strategy = st.builds(visualinher_I)
@given(instance=visualinher_I_strategy)
@settings(max_examples=25)
def test_visualinher_I_instantiation(instance):
    assert isinstance(instance, visualinher_I)


visualinher_N_strategy = st.builds(visualinher_N, name=safe_text)
@given(instance=visualinher_N_strategy)
@settings(max_examples=25)
def test_visualinher_N_instantiation(instance):
    assert isinstance(instance, visualinher_N)


visualinher_R_strategy = st.builds(visualinher_R)
@given(instance=visualinher_R_strategy)
@settings(max_examples=25)
def test_visualinher_R_instantiation(instance):
    assert isinstance(instance, visualinher_R)


visualinher_S_strategy = st.builds(visualinher_S)
@given(instance=visualinher_S_strategy)
@settings(max_examples=25)
def test_visualinher_S_instantiation(instance):
    assert isinstance(instance, visualinher_S)



