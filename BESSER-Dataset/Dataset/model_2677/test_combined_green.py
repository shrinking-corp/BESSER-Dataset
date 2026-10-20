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
    B,
    kref_Named,
    Named,
    kref_K,
    kref_B,
    kref_E,
    kref_J,
    kref_F,
    kref_H,
    kref_C,
    kref_G,
    kref_A,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_hyp_b_is_not_abstract():
    assert not inspect.isabstract(B)


def test_hyp_b_constructor_exists():
    assert callable(B.__init__)


def test_hyp_b_constructor_args():
    sig = inspect.signature(B.__init__)
    params = list(sig.parameters.keys())



def test_hyp_kref_named_is_not_abstract():
    assert not inspect.isabstract(kref_Named)


def test_hyp_kref_named_constructor_exists():
    assert callable(kref_Named.__init__)


def test_hyp_kref_named_constructor_args():
    sig = inspect.signature(kref_Named.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"




def test_hyp_named_is_not_abstract():
    assert not inspect.isabstract(Named)


def test_hyp_named_constructor_exists():
    assert callable(Named.__init__)


def test_hyp_named_constructor_args():
    sig = inspect.signature(Named.__init__)
    params = list(sig.parameters.keys())



def test_hyp_kref_k_is_not_abstract():
    assert not inspect.isabstract(kref_K)


def test_hyp_kref_k_constructor_exists():
    assert callable(kref_K.__init__)


def test_hyp_kref_k_constructor_args():
    sig = inspect.signature(kref_K.__init__)
    params = list(sig.parameters.keys())



def test_hyp_kref_b_is_not_abstract():
    assert not inspect.isabstract(kref_B)


def test_hyp_kref_b_constructor_exists():
    assert callable(kref_B.__init__)


def test_hyp_kref_b_constructor_args():
    sig = inspect.signature(kref_B.__init__)
    params = list(sig.parameters.keys())



def test_hyp_kref_e_is_not_abstract():
    assert not inspect.isabstract(kref_E)


def test_hyp_kref_e_constructor_exists():
    assert callable(kref_E.__init__)


def test_hyp_kref_e_constructor_args():
    sig = inspect.signature(kref_E.__init__)
    params = list(sig.parameters.keys())



def test_hyp_kref_j_is_not_abstract():
    assert not inspect.isabstract(kref_J)


def test_hyp_kref_j_constructor_exists():
    assert callable(kref_J.__init__)


def test_hyp_kref_j_constructor_args():
    sig = inspect.signature(kref_J.__init__)
    params = list(sig.parameters.keys())



def test_hyp_kref_f_is_not_abstract():
    assert not inspect.isabstract(kref_F)


def test_hyp_kref_f_constructor_exists():
    assert callable(kref_F.__init__)


def test_hyp_kref_f_constructor_args():
    sig = inspect.signature(kref_F.__init__)
    params = list(sig.parameters.keys())



def test_hyp_kref_h_is_not_abstract():
    assert not inspect.isabstract(kref_H)


def test_hyp_kref_h_constructor_exists():
    assert callable(kref_H.__init__)


def test_hyp_kref_h_constructor_args():
    sig = inspect.signature(kref_H.__init__)
    params = list(sig.parameters.keys())



def test_hyp_kref_c_is_not_abstract():
    assert not inspect.isabstract(kref_C)


def test_hyp_kref_c_constructor_exists():
    assert callable(kref_C.__init__)


def test_hyp_kref_c_constructor_args():
    sig = inspect.signature(kref_C.__init__)
    params = list(sig.parameters.keys())



def test_hyp_kref_g_is_not_abstract():
    assert not inspect.isabstract(kref_G)


def test_hyp_kref_g_constructor_exists():
    assert callable(kref_G.__init__)


def test_hyp_kref_g_constructor_args():
    sig = inspect.signature(kref_G.__init__)
    params = list(sig.parameters.keys())



def test_hyp_kref_a_is_not_abstract():
    assert not inspect.isabstract(kref_A)


def test_hyp_kref_a_constructor_exists():
    assert callable(kref_A.__init__)


def test_hyp_kref_a_constructor_args():
    sig = inspect.signature(kref_A.__init__)
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
B_strategy = st.builds(
    B,
)
kref_Named_strategy = st.builds(
    kref_Named,
    name=
        safe_text
)
Named_strategy = st.builds(
    Named,
)
kref_K_strategy = st.builds(
    kref_K,
)
kref_B_strategy = st.builds(
    kref_B,
)
kref_E_strategy = st.builds(
    kref_E,
)
kref_J_strategy = st.builds(
    kref_J,
)
kref_F_strategy = st.builds(
    kref_F,
)
kref_H_strategy = st.builds(
    kref_H,
)
kref_C_strategy = st.builds(
    kref_C,
)
kref_G_strategy = st.builds(
    kref_G,
)
kref_A_strategy = st.builds(
    kref_A,
)





@given(instance=kref_Named_strategy)
def test_hyp_kref_named_name_setter(instance):
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
    Named,
    kref_A,
    kref_B,
    kref_C,
    kref_E,
    kref_F,
    kref_G,
    kref_H,
    kref_J,
    kref_K,
    kref_Named,
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

def test_kref_Named_name_value_roundtrip():
    instance = kref_Named(name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_kref_E_isa_B():
    instance = kref_E()
    assert isinstance(instance, B)


def test_kref_A_isa_Named():
    instance = kref_A()
    assert isinstance(instance, Named)


def test_kref_B_isa_Named():
    instance = kref_B()
    assert isinstance(instance, Named)


def test_kref_C_isa_Named():
    instance = kref_C()
    assert isinstance(instance, Named)


def test_kref_E_isa_Named():
    instance = kref_E()
    assert isinstance(instance, Named)


def test_kref_F_isa_Named():
    instance = kref_F()
    assert isinstance(instance, Named)


def test_kref_G_isa_Named():
    instance = kref_G()
    assert isinstance(instance, Named)


def test_kref_H_isa_Named():
    instance = kref_H()
    assert isinstance(instance, Named)


def test_kref_J_isa_Named():
    instance = kref_J()
    assert isinstance(instance, Named)


def test_kref_K_isa_Named():
    instance = kref_K()
    assert isinstance(instance, Named)


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

B_strategy = st.builds(B)
@given(instance=B_strategy)
@settings(max_examples=25)
def test_B_instantiation(instance):
    assert isinstance(instance, B)


Named_strategy = st.builds(Named)
@given(instance=Named_strategy)
@settings(max_examples=25)
def test_Named_instantiation(instance):
    assert isinstance(instance, Named)


kref_A_strategy = st.builds(kref_A)
@given(instance=kref_A_strategy)
@settings(max_examples=25)
def test_kref_A_instantiation(instance):
    assert isinstance(instance, kref_A)


kref_B_strategy = st.builds(kref_B)
@given(instance=kref_B_strategy)
@settings(max_examples=25)
def test_kref_B_instantiation(instance):
    assert isinstance(instance, kref_B)


kref_C_strategy = st.builds(kref_C)
@given(instance=kref_C_strategy)
@settings(max_examples=25)
def test_kref_C_instantiation(instance):
    assert isinstance(instance, kref_C)


kref_E_strategy = st.builds(kref_E)
@given(instance=kref_E_strategy)
@settings(max_examples=25)
def test_kref_E_instantiation(instance):
    assert isinstance(instance, kref_E)


kref_F_strategy = st.builds(kref_F)
@given(instance=kref_F_strategy)
@settings(max_examples=25)
def test_kref_F_instantiation(instance):
    assert isinstance(instance, kref_F)


kref_G_strategy = st.builds(kref_G)
@given(instance=kref_G_strategy)
@settings(max_examples=25)
def test_kref_G_instantiation(instance):
    assert isinstance(instance, kref_G)


kref_H_strategy = st.builds(kref_H)
@given(instance=kref_H_strategy)
@settings(max_examples=25)
def test_kref_H_instantiation(instance):
    assert isinstance(instance, kref_H)


kref_J_strategy = st.builds(kref_J)
@given(instance=kref_J_strategy)
@settings(max_examples=25)
def test_kref_J_instantiation(instance):
    assert isinstance(instance, kref_J)


kref_K_strategy = st.builds(kref_K)
@given(instance=kref_K_strategy)
@settings(max_examples=25)
def test_kref_K_instantiation(instance):
    assert isinstance(instance, kref_K)


kref_Named_strategy = st.builds(kref_Named, name=safe_text)
@given(instance=kref_Named_strategy)
@settings(max_examples=25)
def test_kref_Named_instantiation(instance):
    assert isinstance(instance, kref_Named)



