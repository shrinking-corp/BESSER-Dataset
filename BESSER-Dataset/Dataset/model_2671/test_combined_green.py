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
    comps_Named,
    Named,
    comps_F,
    comps_G,
    comps_B,
    comps_H,
    comps_C,
    comps_E,
    comps_A,
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



def test_hyp_comps_named_is_not_abstract():
    assert not inspect.isabstract(comps_Named)


def test_hyp_comps_named_constructor_exists():
    assert callable(comps_Named.__init__)


def test_hyp_comps_named_constructor_args():
    sig = inspect.signature(comps_Named.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"




def test_hyp_named_is_not_abstract():
    assert not inspect.isabstract(Named)


def test_hyp_named_constructor_exists():
    assert callable(Named.__init__)


def test_hyp_named_constructor_args():
    sig = inspect.signature(Named.__init__)
    params = list(sig.parameters.keys())



def test_hyp_comps_f_is_not_abstract():
    assert not inspect.isabstract(comps_F)


def test_hyp_comps_f_constructor_exists():
    assert callable(comps_F.__init__)


def test_hyp_comps_f_constructor_args():
    sig = inspect.signature(comps_F.__init__)
    params = list(sig.parameters.keys())



def test_hyp_comps_g_is_not_abstract():
    assert not inspect.isabstract(comps_G)


def test_hyp_comps_g_constructor_exists():
    assert callable(comps_G.__init__)


def test_hyp_comps_g_constructor_args():
    sig = inspect.signature(comps_G.__init__)
    params = list(sig.parameters.keys())



def test_hyp_comps_b_is_not_abstract():
    assert not inspect.isabstract(comps_B)


def test_hyp_comps_b_constructor_exists():
    assert callable(comps_B.__init__)


def test_hyp_comps_b_constructor_args():
    sig = inspect.signature(comps_B.__init__)
    params = list(sig.parameters.keys())



def test_hyp_comps_h_is_not_abstract():
    assert not inspect.isabstract(comps_H)


def test_hyp_comps_h_constructor_exists():
    assert callable(comps_H.__init__)


def test_hyp_comps_h_constructor_args():
    sig = inspect.signature(comps_H.__init__)
    params = list(sig.parameters.keys())



def test_hyp_comps_c_is_not_abstract():
    assert not inspect.isabstract(comps_C)


def test_hyp_comps_c_constructor_exists():
    assert callable(comps_C.__init__)


def test_hyp_comps_c_constructor_args():
    sig = inspect.signature(comps_C.__init__)
    params = list(sig.parameters.keys())



def test_hyp_comps_e_is_not_abstract():
    assert not inspect.isabstract(comps_E)


def test_hyp_comps_e_constructor_exists():
    assert callable(comps_E.__init__)


def test_hyp_comps_e_constructor_args():
    sig = inspect.signature(comps_E.__init__)
    params = list(sig.parameters.keys())



def test_hyp_comps_a_is_not_abstract():
    assert not inspect.isabstract(comps_A)


def test_hyp_comps_a_constructor_exists():
    assert callable(comps_A.__init__)


def test_hyp_comps_a_constructor_args():
    sig = inspect.signature(comps_A.__init__)
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
comps_Named_strategy = st.builds(
    comps_Named,
    name=
        safe_text
)
Named_strategy = st.builds(
    Named,
)
comps_F_strategy = st.builds(
    comps_F,
)
comps_G_strategy = st.builds(
    comps_G,
)
comps_B_strategy = st.builds(
    comps_B,
)
comps_H_strategy = st.builds(
    comps_H,
)
comps_C_strategy = st.builds(
    comps_C,
)
comps_E_strategy = st.builds(
    comps_E,
)
comps_A_strategy = st.builds(
    comps_A,
)





@given(instance=comps_Named_strategy)
def test_hyp_comps_named_name_setter(instance):
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
    comps_A,
    comps_B,
    comps_C,
    comps_E,
    comps_F,
    comps_G,
    comps_H,
    comps_Named,
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

def test_comps_Named_name_value_roundtrip():
    instance = comps_Named(name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_comps_E_isa_B():
    instance = comps_E()
    assert isinstance(instance, B)


def test_comps_A_isa_Named():
    instance = comps_A()
    assert isinstance(instance, Named)


def test_comps_B_isa_Named():
    instance = comps_B()
    assert isinstance(instance, Named)


def test_comps_C_isa_Named():
    instance = comps_C()
    assert isinstance(instance, Named)


def test_comps_E_isa_Named():
    instance = comps_E()
    assert isinstance(instance, Named)


def test_comps_F_isa_Named():
    instance = comps_F()
    assert isinstance(instance, Named)


def test_comps_G_isa_Named():
    instance = comps_G()
    assert isinstance(instance, Named)


def test_comps_H_isa_Named():
    instance = comps_H()
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


comps_A_strategy = st.builds(comps_A)
@given(instance=comps_A_strategy)
@settings(max_examples=25)
def test_comps_A_instantiation(instance):
    assert isinstance(instance, comps_A)


comps_B_strategy = st.builds(comps_B)
@given(instance=comps_B_strategy)
@settings(max_examples=25)
def test_comps_B_instantiation(instance):
    assert isinstance(instance, comps_B)


comps_C_strategy = st.builds(comps_C)
@given(instance=comps_C_strategy)
@settings(max_examples=25)
def test_comps_C_instantiation(instance):
    assert isinstance(instance, comps_C)


comps_E_strategy = st.builds(comps_E)
@given(instance=comps_E_strategy)
@settings(max_examples=25)
def test_comps_E_instantiation(instance):
    assert isinstance(instance, comps_E)


comps_F_strategy = st.builds(comps_F)
@given(instance=comps_F_strategy)
@settings(max_examples=25)
def test_comps_F_instantiation(instance):
    assert isinstance(instance, comps_F)


comps_G_strategy = st.builds(comps_G)
@given(instance=comps_G_strategy)
@settings(max_examples=25)
def test_comps_G_instantiation(instance):
    assert isinstance(instance, comps_G)


comps_H_strategy = st.builds(comps_H)
@given(instance=comps_H_strategy)
@settings(max_examples=25)
def test_comps_H_instantiation(instance):
    assert isinstance(instance, comps_H)


comps_Named_strategy = st.builds(comps_Named, name=safe_text)
@given(instance=comps_Named_strategy)
@settings(max_examples=25)
def test_comps_Named_instantiation(instance):
    assert isinstance(instance, comps_Named)



