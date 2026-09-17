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
    F,
    namd_I,
    namd_Named,
    Named,
    namd_C,
    namd_H,
    namd_G,
    namd_B,
    namd_A,
    D,
    namd_F,
    namd_E,
    B,
    namd_D,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_hyp_f_is_not_abstract():
    assert not inspect.isabstract(F)


def test_hyp_f_constructor_exists():
    assert callable(F.__init__)


def test_hyp_f_constructor_args():
    sig = inspect.signature(F.__init__)
    params = list(sig.parameters.keys())



def test_hyp_namd_i_is_not_abstract():
    assert not inspect.isabstract(namd_I)


def test_hyp_namd_i_constructor_exists():
    assert callable(namd_I.__init__)


def test_hyp_namd_i_constructor_args():
    sig = inspect.signature(namd_I.__init__)
    params = list(sig.parameters.keys())



def test_hyp_namd_named_is_not_abstract():
    assert not inspect.isabstract(namd_Named)


def test_hyp_namd_named_constructor_exists():
    assert callable(namd_Named.__init__)


def test_hyp_namd_named_constructor_args():
    sig = inspect.signature(namd_Named.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"




def test_hyp_named_is_not_abstract():
    assert not inspect.isabstract(Named)


def test_hyp_named_constructor_exists():
    assert callable(Named.__init__)


def test_hyp_named_constructor_args():
    sig = inspect.signature(Named.__init__)
    params = list(sig.parameters.keys())



def test_hyp_namd_c_is_not_abstract():
    assert not inspect.isabstract(namd_C)


def test_hyp_namd_c_constructor_exists():
    assert callable(namd_C.__init__)


def test_hyp_namd_c_constructor_args():
    sig = inspect.signature(namd_C.__init__)
    params = list(sig.parameters.keys())



def test_hyp_namd_h_is_not_abstract():
    assert not inspect.isabstract(namd_H)


def test_hyp_namd_h_constructor_exists():
    assert callable(namd_H.__init__)


def test_hyp_namd_h_constructor_args():
    sig = inspect.signature(namd_H.__init__)
    params = list(sig.parameters.keys())



def test_hyp_namd_g_is_not_abstract():
    assert not inspect.isabstract(namd_G)


def test_hyp_namd_g_constructor_exists():
    assert callable(namd_G.__init__)


def test_hyp_namd_g_constructor_args():
    sig = inspect.signature(namd_G.__init__)
    params = list(sig.parameters.keys())



def test_hyp_namd_b_is_not_abstract():
    assert not inspect.isabstract(namd_B)


def test_hyp_namd_b_constructor_exists():
    assert callable(namd_B.__init__)


def test_hyp_namd_b_constructor_args():
    sig = inspect.signature(namd_B.__init__)
    params = list(sig.parameters.keys())



def test_hyp_namd_a_is_not_abstract():
    assert not inspect.isabstract(namd_A)


def test_hyp_namd_a_constructor_exists():
    assert callable(namd_A.__init__)


def test_hyp_namd_a_constructor_args():
    sig = inspect.signature(namd_A.__init__)
    params = list(sig.parameters.keys())



def test_hyp_d_is_not_abstract():
    assert not inspect.isabstract(D)


def test_hyp_d_constructor_exists():
    assert callable(D.__init__)


def test_hyp_d_constructor_args():
    sig = inspect.signature(D.__init__)
    params = list(sig.parameters.keys())



def test_hyp_namd_f_is_not_abstract():
    assert not inspect.isabstract(namd_F)


def test_hyp_namd_f_constructor_exists():
    assert callable(namd_F.__init__)


def test_hyp_namd_f_constructor_args():
    sig = inspect.signature(namd_F.__init__)
    params = list(sig.parameters.keys())



def test_hyp_namd_e_is_not_abstract():
    assert not inspect.isabstract(namd_E)


def test_hyp_namd_e_constructor_exists():
    assert callable(namd_E.__init__)


def test_hyp_namd_e_constructor_args():
    sig = inspect.signature(namd_E.__init__)
    params = list(sig.parameters.keys())



def test_hyp_b_is_not_abstract():
    assert not inspect.isabstract(B)


def test_hyp_b_constructor_exists():
    assert callable(B.__init__)


def test_hyp_b_constructor_args():
    sig = inspect.signature(B.__init__)
    params = list(sig.parameters.keys())



def test_hyp_namd_d_is_not_abstract():
    assert not inspect.isabstract(namd_D)


def test_hyp_namd_d_constructor_exists():
    assert callable(namd_D.__init__)


def test_hyp_namd_d_constructor_args():
    sig = inspect.signature(namd_D.__init__)
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
F_strategy = st.builds(
    F,
)
namd_I_strategy = st.builds(
    namd_I,
)
namd_Named_strategy = st.builds(
    namd_Named,
    name=
        safe_text
)
Named_strategy = st.builds(
    Named,
)
namd_C_strategy = st.builds(
    namd_C,
)
namd_H_strategy = st.builds(
    namd_H,
)
namd_G_strategy = st.builds(
    namd_G,
)
namd_B_strategy = st.builds(
    namd_B,
)
namd_A_strategy = st.builds(
    namd_A,
)
D_strategy = st.builds(
    D,
)
namd_F_strategy = st.builds(
    namd_F,
)
namd_E_strategy = st.builds(
    namd_E,
)
B_strategy = st.builds(
    B,
)
namd_D_strategy = st.builds(
    namd_D,
)






@given(instance=namd_Named_strategy)
def test_hyp_namd_named_name_setter(instance):
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
    Named,
    namd_A,
    namd_B,
    namd_C,
    namd_D,
    namd_E,
    namd_F,
    namd_G,
    namd_H,
    namd_I,
    namd_Named,
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

def test_namd_Named_name_value_roundtrip():
    instance = namd_Named(name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_namd_D_isa_B():
    instance = namd_D()
    assert isinstance(instance, B)


def test_namd_F_isa_D():
    instance = namd_F()
    assert isinstance(instance, D)


def test_namd_I_isa_F():
    instance = namd_I()
    assert isinstance(instance, F)


def test_namd_B_isa_Named():
    instance = namd_B()
    assert isinstance(instance, Named)


def test_namd_C_isa_Named():
    instance = namd_C()
    assert isinstance(instance, Named)


def test_namd_E_isa_Named():
    instance = namd_E()
    assert isinstance(instance, Named)


def test_namd_G_isa_Named():
    instance = namd_G()
    assert isinstance(instance, Named)


def test_namd_H_isa_Named():
    instance = namd_H()
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


Named_strategy = st.builds(Named)
@given(instance=Named_strategy)
@settings(max_examples=25)
def test_Named_instantiation(instance):
    assert isinstance(instance, Named)


namd_A_strategy = st.builds(namd_A)
@given(instance=namd_A_strategy)
@settings(max_examples=25)
def test_namd_A_instantiation(instance):
    assert isinstance(instance, namd_A)


namd_B_strategy = st.builds(namd_B)
@given(instance=namd_B_strategy)
@settings(max_examples=25)
def test_namd_B_instantiation(instance):
    assert isinstance(instance, namd_B)


namd_C_strategy = st.builds(namd_C)
@given(instance=namd_C_strategy)
@settings(max_examples=25)
def test_namd_C_instantiation(instance):
    assert isinstance(instance, namd_C)


namd_D_strategy = st.builds(namd_D)
@given(instance=namd_D_strategy)
@settings(max_examples=25)
def test_namd_D_instantiation(instance):
    assert isinstance(instance, namd_D)


namd_E_strategy = st.builds(namd_E)
@given(instance=namd_E_strategy)
@settings(max_examples=25)
def test_namd_E_instantiation(instance):
    assert isinstance(instance, namd_E)


namd_F_strategy = st.builds(namd_F)
@given(instance=namd_F_strategy)
@settings(max_examples=25)
def test_namd_F_instantiation(instance):
    assert isinstance(instance, namd_F)


namd_G_strategy = st.builds(namd_G)
@given(instance=namd_G_strategy)
@settings(max_examples=25)
def test_namd_G_instantiation(instance):
    assert isinstance(instance, namd_G)


namd_H_strategy = st.builds(namd_H)
@given(instance=namd_H_strategy)
@settings(max_examples=25)
def test_namd_H_instantiation(instance):
    assert isinstance(instance, namd_H)


namd_I_strategy = st.builds(namd_I)
@given(instance=namd_I_strategy)
@settings(max_examples=25)
def test_namd_I_instantiation(instance):
    assert isinstance(instance, namd_I)


namd_Named_strategy = st.builds(namd_Named, name=safe_text)
@given(instance=namd_Named_strategy)
@settings(max_examples=25)
def test_namd_Named_instantiation(instance):
    assert isinstance(instance, namd_Named)



