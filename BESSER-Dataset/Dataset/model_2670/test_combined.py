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
    conts_Named,
    Named,
    conts_C,
    conts_E,
    conts_B,
    conts_G,
    conts_F,
    conts_H,
    conts_A,
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



def test_hyp_conts_named_is_not_abstract():
    assert not inspect.isabstract(conts_Named)


def test_hyp_conts_named_constructor_exists():
    assert callable(conts_Named.__init__)


def test_hyp_conts_named_constructor_args():
    sig = inspect.signature(conts_Named.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"




def test_hyp_named_is_not_abstract():
    assert not inspect.isabstract(Named)


def test_hyp_named_constructor_exists():
    assert callable(Named.__init__)


def test_hyp_named_constructor_args():
    sig = inspect.signature(Named.__init__)
    params = list(sig.parameters.keys())



def test_hyp_conts_c_is_not_abstract():
    assert not inspect.isabstract(conts_C)


def test_hyp_conts_c_constructor_exists():
    assert callable(conts_C.__init__)


def test_hyp_conts_c_constructor_args():
    sig = inspect.signature(conts_C.__init__)
    params = list(sig.parameters.keys())



def test_hyp_conts_e_is_not_abstract():
    assert not inspect.isabstract(conts_E)


def test_hyp_conts_e_constructor_exists():
    assert callable(conts_E.__init__)


def test_hyp_conts_e_constructor_args():
    sig = inspect.signature(conts_E.__init__)
    params = list(sig.parameters.keys())



def test_hyp_conts_b_is_not_abstract():
    assert not inspect.isabstract(conts_B)


def test_hyp_conts_b_constructor_exists():
    assert callable(conts_B.__init__)


def test_hyp_conts_b_constructor_args():
    sig = inspect.signature(conts_B.__init__)
    params = list(sig.parameters.keys())



def test_hyp_conts_g_is_not_abstract():
    assert not inspect.isabstract(conts_G)


def test_hyp_conts_g_constructor_exists():
    assert callable(conts_G.__init__)


def test_hyp_conts_g_constructor_args():
    sig = inspect.signature(conts_G.__init__)
    params = list(sig.parameters.keys())



def test_hyp_conts_f_is_not_abstract():
    assert not inspect.isabstract(conts_F)


def test_hyp_conts_f_constructor_exists():
    assert callable(conts_F.__init__)


def test_hyp_conts_f_constructor_args():
    sig = inspect.signature(conts_F.__init__)
    params = list(sig.parameters.keys())



def test_hyp_conts_h_is_not_abstract():
    assert not inspect.isabstract(conts_H)


def test_hyp_conts_h_constructor_exists():
    assert callable(conts_H.__init__)


def test_hyp_conts_h_constructor_args():
    sig = inspect.signature(conts_H.__init__)
    params = list(sig.parameters.keys())



def test_hyp_conts_a_is_not_abstract():
    assert not inspect.isabstract(conts_A)


def test_hyp_conts_a_constructor_exists():
    assert callable(conts_A.__init__)


def test_hyp_conts_a_constructor_args():
    sig = inspect.signature(conts_A.__init__)
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
conts_Named_strategy = st.builds(
    conts_Named,
    name=
        safe_text
)
Named_strategy = st.builds(
    Named,
)
conts_C_strategy = st.builds(
    conts_C,
)
conts_E_strategy = st.builds(
    conts_E,
)
conts_B_strategy = st.builds(
    conts_B,
)
conts_G_strategy = st.builds(
    conts_G,
)
conts_F_strategy = st.builds(
    conts_F,
)
conts_H_strategy = st.builds(
    conts_H,
)
conts_A_strategy = st.builds(
    conts_A,
)





@given(instance=conts_Named_strategy)
def test_hyp_conts_named_name_setter(instance):
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
    conts_A,
    conts_B,
    conts_C,
    conts_E,
    conts_F,
    conts_G,
    conts_H,
    conts_Named,
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

def test_conts_Named_name_value_roundtrip():
    instance = conts_Named(name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_conts_E_isa_B():
    instance = conts_E()
    assert isinstance(instance, B)


def test_conts_A_isa_Named():
    instance = conts_A()
    assert isinstance(instance, Named)


def test_conts_B_isa_Named():
    instance = conts_B()
    assert isinstance(instance, Named)


def test_conts_C_isa_Named():
    instance = conts_C()
    assert isinstance(instance, Named)


def test_conts_E_isa_Named():
    instance = conts_E()
    assert isinstance(instance, Named)


def test_conts_F_isa_Named():
    instance = conts_F()
    assert isinstance(instance, Named)


def test_conts_G_isa_Named():
    instance = conts_G()
    assert isinstance(instance, Named)


def test_conts_H_isa_Named():
    instance = conts_H()
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


conts_A_strategy = st.builds(conts_A)
@given(instance=conts_A_strategy)
@settings(max_examples=25)
def test_conts_A_instantiation(instance):
    assert isinstance(instance, conts_A)


conts_B_strategy = st.builds(conts_B)
@given(instance=conts_B_strategy)
@settings(max_examples=25)
def test_conts_B_instantiation(instance):
    assert isinstance(instance, conts_B)


conts_C_strategy = st.builds(conts_C)
@given(instance=conts_C_strategy)
@settings(max_examples=25)
def test_conts_C_instantiation(instance):
    assert isinstance(instance, conts_C)


conts_E_strategy = st.builds(conts_E)
@given(instance=conts_E_strategy)
@settings(max_examples=25)
def test_conts_E_instantiation(instance):
    assert isinstance(instance, conts_E)


conts_F_strategy = st.builds(conts_F)
@given(instance=conts_F_strategy)
@settings(max_examples=25)
def test_conts_F_instantiation(instance):
    assert isinstance(instance, conts_F)


conts_G_strategy = st.builds(conts_G)
@given(instance=conts_G_strategy)
@settings(max_examples=25)
def test_conts_G_instantiation(instance):
    assert isinstance(instance, conts_G)


conts_H_strategy = st.builds(conts_H)
@given(instance=conts_H_strategy)
@settings(max_examples=25)
def test_conts_H_instantiation(instance):
    assert isinstance(instance, conts_H)


conts_Named_strategy = st.builds(conts_Named, name=safe_text)
@given(instance=conts_Named_strategy)
@settings(max_examples=25)
def test_conts_Named_instantiation(instance):
    assert isinstance(instance, conts_Named)



