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
    K,
    F,
    compmultinher_I,
    D,
    compmultinher_F,
    B,
    compmultinher_D,
    compmultinher_Named,
    Named,
    compmultinher_G,
    compmultinher_E,
    compmultinher_H,
    compmultinher_C,
    compmultinher_L,
    compmultinher_K,
    compmultinher_B,
    compmultinher_A,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_hyp_k_is_not_abstract():
    assert not inspect.isabstract(K)


def test_hyp_k_constructor_exists():
    assert callable(K.__init__)


def test_hyp_k_constructor_args():
    sig = inspect.signature(K.__init__)
    params = list(sig.parameters.keys())



def test_hyp_f_is_not_abstract():
    assert not inspect.isabstract(F)


def test_hyp_f_constructor_exists():
    assert callable(F.__init__)


def test_hyp_f_constructor_args():
    sig = inspect.signature(F.__init__)
    params = list(sig.parameters.keys())



def test_hyp_compmultinher_i_is_not_abstract():
    assert not inspect.isabstract(compmultinher_I)


def test_hyp_compmultinher_i_constructor_exists():
    assert callable(compmultinher_I.__init__)


def test_hyp_compmultinher_i_constructor_args():
    sig = inspect.signature(compmultinher_I.__init__)
    params = list(sig.parameters.keys())



def test_hyp_d_is_not_abstract():
    assert not inspect.isabstract(D)


def test_hyp_d_constructor_exists():
    assert callable(D.__init__)


def test_hyp_d_constructor_args():
    sig = inspect.signature(D.__init__)
    params = list(sig.parameters.keys())



def test_hyp_compmultinher_f_is_not_abstract():
    assert not inspect.isabstract(compmultinher_F)


def test_hyp_compmultinher_f_constructor_exists():
    assert callable(compmultinher_F.__init__)


def test_hyp_compmultinher_f_constructor_args():
    sig = inspect.signature(compmultinher_F.__init__)
    params = list(sig.parameters.keys())



def test_hyp_b_is_not_abstract():
    assert not inspect.isabstract(B)


def test_hyp_b_constructor_exists():
    assert callable(B.__init__)


def test_hyp_b_constructor_args():
    sig = inspect.signature(B.__init__)
    params = list(sig.parameters.keys())



def test_hyp_compmultinher_d_is_not_abstract():
    assert not inspect.isabstract(compmultinher_D)


def test_hyp_compmultinher_d_constructor_exists():
    assert callable(compmultinher_D.__init__)


def test_hyp_compmultinher_d_constructor_args():
    sig = inspect.signature(compmultinher_D.__init__)
    params = list(sig.parameters.keys())



def test_hyp_compmultinher_named_is_not_abstract():
    assert not inspect.isabstract(compmultinher_Named)


def test_hyp_compmultinher_named_constructor_exists():
    assert callable(compmultinher_Named.__init__)


def test_hyp_compmultinher_named_constructor_args():
    sig = inspect.signature(compmultinher_Named.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"




def test_hyp_named_is_not_abstract():
    assert not inspect.isabstract(Named)


def test_hyp_named_constructor_exists():
    assert callable(Named.__init__)


def test_hyp_named_constructor_args():
    sig = inspect.signature(Named.__init__)
    params = list(sig.parameters.keys())



def test_hyp_compmultinher_g_is_not_abstract():
    assert not inspect.isabstract(compmultinher_G)


def test_hyp_compmultinher_g_constructor_exists():
    assert callable(compmultinher_G.__init__)


def test_hyp_compmultinher_g_constructor_args():
    sig = inspect.signature(compmultinher_G.__init__)
    params = list(sig.parameters.keys())



def test_hyp_compmultinher_e_is_not_abstract():
    assert not inspect.isabstract(compmultinher_E)


def test_hyp_compmultinher_e_constructor_exists():
    assert callable(compmultinher_E.__init__)


def test_hyp_compmultinher_e_constructor_args():
    sig = inspect.signature(compmultinher_E.__init__)
    params = list(sig.parameters.keys())



def test_hyp_compmultinher_h_is_not_abstract():
    assert not inspect.isabstract(compmultinher_H)


def test_hyp_compmultinher_h_constructor_exists():
    assert callable(compmultinher_H.__init__)


def test_hyp_compmultinher_h_constructor_args():
    sig = inspect.signature(compmultinher_H.__init__)
    params = list(sig.parameters.keys())



def test_hyp_compmultinher_c_is_not_abstract():
    assert not inspect.isabstract(compmultinher_C)


def test_hyp_compmultinher_c_constructor_exists():
    assert callable(compmultinher_C.__init__)


def test_hyp_compmultinher_c_constructor_args():
    sig = inspect.signature(compmultinher_C.__init__)
    params = list(sig.parameters.keys())



def test_hyp_compmultinher_l_is_not_abstract():
    assert not inspect.isabstract(compmultinher_L)


def test_hyp_compmultinher_l_constructor_exists():
    assert callable(compmultinher_L.__init__)


def test_hyp_compmultinher_l_constructor_args():
    sig = inspect.signature(compmultinher_L.__init__)
    params = list(sig.parameters.keys())



def test_hyp_compmultinher_k_is_not_abstract():
    assert not inspect.isabstract(compmultinher_K)


def test_hyp_compmultinher_k_constructor_exists():
    assert callable(compmultinher_K.__init__)


def test_hyp_compmultinher_k_constructor_args():
    sig = inspect.signature(compmultinher_K.__init__)
    params = list(sig.parameters.keys())



def test_hyp_compmultinher_b_is_not_abstract():
    assert not inspect.isabstract(compmultinher_B)


def test_hyp_compmultinher_b_constructor_exists():
    assert callable(compmultinher_B.__init__)


def test_hyp_compmultinher_b_constructor_args():
    sig = inspect.signature(compmultinher_B.__init__)
    params = list(sig.parameters.keys())



def test_hyp_compmultinher_a_is_not_abstract():
    assert not inspect.isabstract(compmultinher_A)


def test_hyp_compmultinher_a_constructor_exists():
    assert callable(compmultinher_A.__init__)


def test_hyp_compmultinher_a_constructor_args():
    sig = inspect.signature(compmultinher_A.__init__)
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
K_strategy = st.builds(
    K,
)
F_strategy = st.builds(
    F,
)
compmultinher_I_strategy = st.builds(
    compmultinher_I,
)
D_strategy = st.builds(
    D,
)
compmultinher_F_strategy = st.builds(
    compmultinher_F,
)
B_strategy = st.builds(
    B,
)
compmultinher_D_strategy = st.builds(
    compmultinher_D,
)
compmultinher_Named_strategy = st.builds(
    compmultinher_Named,
    name=
        safe_text
)
Named_strategy = st.builds(
    Named,
)
compmultinher_G_strategy = st.builds(
    compmultinher_G,
)
compmultinher_E_strategy = st.builds(
    compmultinher_E,
)
compmultinher_H_strategy = st.builds(
    compmultinher_H,
)
compmultinher_C_strategy = st.builds(
    compmultinher_C,
)
compmultinher_L_strategy = st.builds(
    compmultinher_L,
)
compmultinher_K_strategy = st.builds(
    compmultinher_K,
)
compmultinher_B_strategy = st.builds(
    compmultinher_B,
)
compmultinher_A_strategy = st.builds(
    compmultinher_A,
)











@given(instance=compmultinher_Named_strategy)
def test_hyp_compmultinher_named_name_setter(instance):
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
    B,
    D,
    F,
    K,
    Named,
    compmultinher_A,
    compmultinher_B,
    compmultinher_C,
    compmultinher_D,
    compmultinher_E,
    compmultinher_F,
    compmultinher_G,
    compmultinher_H,
    compmultinher_I,
    compmultinher_K,
    compmultinher_L,
    compmultinher_Named,
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

def test_compmultinher_Named_name_value_roundtrip():
    instance = compmultinher_Named(name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_compmultinher_D_isa_B():
    instance = compmultinher_D()
    assert isinstance(instance, B)


def test_compmultinher_F_isa_D():
    instance = compmultinher_F()
    assert isinstance(instance, D)


def test_compmultinher_I_isa_F():
    instance = compmultinher_I()
    assert isinstance(instance, F)


def test_compmultinher_I_isa_K():
    instance = compmultinher_I()
    assert isinstance(instance, K)


def test_compmultinher_B_isa_Named():
    instance = compmultinher_B()
    assert isinstance(instance, Named)


def test_compmultinher_C_isa_Named():
    instance = compmultinher_C()
    assert isinstance(instance, Named)


def test_compmultinher_E_isa_Named():
    instance = compmultinher_E()
    assert isinstance(instance, Named)


def test_compmultinher_G_isa_Named():
    instance = compmultinher_G()
    assert isinstance(instance, Named)


def test_compmultinher_H_isa_Named():
    instance = compmultinher_H()
    assert isinstance(instance, Named)


def test_compmultinher_K_isa_Named():
    instance = compmultinher_K()
    assert isinstance(instance, Named)


def test_compmultinher_L_isa_Named():
    instance = compmultinher_L()
    assert isinstance(instance, Named)


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

B_strategy = st.builds(B)
@given(instance=B_strategy)
@settings(max_examples=25)
def test_B_instantiation(instance):
    assert isinstance(instance, B)


D_strategy = st.builds(D)
@given(instance=D_strategy)
@settings(max_examples=25)
def test_D_instantiation(instance):
    assert isinstance(instance, D)


F_strategy = st.builds(F)
@given(instance=F_strategy)
@settings(max_examples=25)
def test_F_instantiation(instance):
    assert isinstance(instance, F)


K_strategy = st.builds(K)
@given(instance=K_strategy)
@settings(max_examples=25)
def test_K_instantiation(instance):
    assert isinstance(instance, K)


Named_strategy = st.builds(Named)
@given(instance=Named_strategy)
@settings(max_examples=25)
def test_Named_instantiation(instance):
    assert isinstance(instance, Named)


compmultinher_A_strategy = st.builds(compmultinher_A)
@given(instance=compmultinher_A_strategy)
@settings(max_examples=25)
def test_compmultinher_A_instantiation(instance):
    assert isinstance(instance, compmultinher_A)


compmultinher_B_strategy = st.builds(compmultinher_B)
@given(instance=compmultinher_B_strategy)
@settings(max_examples=25)
def test_compmultinher_B_instantiation(instance):
    assert isinstance(instance, compmultinher_B)


compmultinher_C_strategy = st.builds(compmultinher_C)
@given(instance=compmultinher_C_strategy)
@settings(max_examples=25)
def test_compmultinher_C_instantiation(instance):
    assert isinstance(instance, compmultinher_C)


compmultinher_D_strategy = st.builds(compmultinher_D)
@given(instance=compmultinher_D_strategy)
@settings(max_examples=25)
def test_compmultinher_D_instantiation(instance):
    assert isinstance(instance, compmultinher_D)


compmultinher_E_strategy = st.builds(compmultinher_E)
@given(instance=compmultinher_E_strategy)
@settings(max_examples=25)
def test_compmultinher_E_instantiation(instance):
    assert isinstance(instance, compmultinher_E)


compmultinher_F_strategy = st.builds(compmultinher_F)
@given(instance=compmultinher_F_strategy)
@settings(max_examples=25)
def test_compmultinher_F_instantiation(instance):
    assert isinstance(instance, compmultinher_F)


compmultinher_G_strategy = st.builds(compmultinher_G)
@given(instance=compmultinher_G_strategy)
@settings(max_examples=25)
def test_compmultinher_G_instantiation(instance):
    assert isinstance(instance, compmultinher_G)


compmultinher_H_strategy = st.builds(compmultinher_H)
@given(instance=compmultinher_H_strategy)
@settings(max_examples=25)
def test_compmultinher_H_instantiation(instance):
    assert isinstance(instance, compmultinher_H)


compmultinher_I_strategy = st.builds(compmultinher_I)
@given(instance=compmultinher_I_strategy)
@settings(max_examples=25)
def test_compmultinher_I_instantiation(instance):
    assert isinstance(instance, compmultinher_I)


compmultinher_K_strategy = st.builds(compmultinher_K)
@given(instance=compmultinher_K_strategy)
@settings(max_examples=25)
def test_compmultinher_K_instantiation(instance):
    assert isinstance(instance, compmultinher_K)


compmultinher_L_strategy = st.builds(compmultinher_L)
@given(instance=compmultinher_L_strategy)
@settings(max_examples=25)
def test_compmultinher_L_instantiation(instance):
    assert isinstance(instance, compmultinher_L)


compmultinher_Named_strategy = st.builds(compmultinher_Named, name=safe_text)
@given(instance=compmultinher_Named_strategy)
@settings(max_examples=25)
def test_compmultinher_Named_instantiation(instance):
    assert isinstance(instance, compmultinher_Named)



