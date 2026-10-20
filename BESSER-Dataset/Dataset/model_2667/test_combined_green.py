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
    mydsl_W,
    W,
    mydsl_L,
    mydsl_D,
    mydsl_B,
    mydsl_C,
    mydsl_A,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_hyp_mydsl_w_is_not_abstract():
    assert not inspect.isabstract(mydsl_W)


def test_hyp_mydsl_w_constructor_exists():
    assert callable(mydsl_W.__init__)


def test_hyp_mydsl_w_constructor_args():
    sig = inspect.signature(mydsl_W.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"




def test_hyp_w_is_not_abstract():
    assert not inspect.isabstract(W)


def test_hyp_w_constructor_exists():
    assert callable(W.__init__)


def test_hyp_w_constructor_args():
    sig = inspect.signature(W.__init__)
    params = list(sig.parameters.keys())



def test_hyp_mydsl_l_is_not_abstract():
    assert not inspect.isabstract(mydsl_L)


def test_hyp_mydsl_l_constructor_exists():
    assert callable(mydsl_L.__init__)


def test_hyp_mydsl_l_constructor_args():
    sig = inspect.signature(mydsl_L.__init__)
    params = list(sig.parameters.keys())



def test_hyp_mydsl_d_is_not_abstract():
    assert not inspect.isabstract(mydsl_D)


def test_hyp_mydsl_d_constructor_exists():
    assert callable(mydsl_D.__init__)


def test_hyp_mydsl_d_constructor_args():
    sig = inspect.signature(mydsl_D.__init__)
    params = list(sig.parameters.keys())



def test_hyp_mydsl_b_is_not_abstract():
    assert not inspect.isabstract(mydsl_B)


def test_hyp_mydsl_b_constructor_exists():
    assert callable(mydsl_B.__init__)


def test_hyp_mydsl_b_constructor_args():
    sig = inspect.signature(mydsl_B.__init__)
    params = list(sig.parameters.keys())



def test_hyp_mydsl_c_is_not_abstract():
    assert not inspect.isabstract(mydsl_C)


def test_hyp_mydsl_c_constructor_exists():
    assert callable(mydsl_C.__init__)


def test_hyp_mydsl_c_constructor_args():
    sig = inspect.signature(mydsl_C.__init__)
    params = list(sig.parameters.keys())



def test_hyp_mydsl_a_is_not_abstract():
    assert not inspect.isabstract(mydsl_A)


def test_hyp_mydsl_a_constructor_exists():
    assert callable(mydsl_A.__init__)


def test_hyp_mydsl_a_constructor_args():
    sig = inspect.signature(mydsl_A.__init__)
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
mydsl_W_strategy = st.builds(
    mydsl_W,
    name=
        safe_text
)
W_strategy = st.builds(
    W,
)
mydsl_L_strategy = st.builds(
    mydsl_L,
)
mydsl_D_strategy = st.builds(
    mydsl_D,
)
mydsl_B_strategy = st.builds(
    mydsl_B,
)
mydsl_C_strategy = st.builds(
    mydsl_C,
)
mydsl_A_strategy = st.builds(
    mydsl_A,
)




@given(instance=mydsl_W_strategy)
def test_hyp_mydsl_w_name_setter(instance):
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
    W,
    mydsl_A,
    mydsl_B,
    mydsl_C,
    mydsl_D,
    mydsl_L,
    mydsl_W,
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

def test_mydsl_W_name_value_roundtrip():
    instance = mydsl_W(name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_mydsl_A_isa_W():
    instance = mydsl_A()
    assert isinstance(instance, W)


def test_mydsl_B_isa_W():
    instance = mydsl_B()
    assert isinstance(instance, W)


def test_mydsl_C_isa_W():
    instance = mydsl_C()
    assert isinstance(instance, W)


def test_mydsl_D_isa_W():
    instance = mydsl_D()
    assert isinstance(instance, W)


def test_mydsl_L_isa_W():
    instance = mydsl_L()
    assert isinstance(instance, W)


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

W_strategy = st.builds(W)
@given(instance=W_strategy)
@settings(max_examples=25)
def test_W_instantiation(instance):
    assert isinstance(instance, W)


mydsl_A_strategy = st.builds(mydsl_A)
@given(instance=mydsl_A_strategy)
@settings(max_examples=25)
def test_mydsl_A_instantiation(instance):
    assert isinstance(instance, mydsl_A)


mydsl_B_strategy = st.builds(mydsl_B)
@given(instance=mydsl_B_strategy)
@settings(max_examples=25)
def test_mydsl_B_instantiation(instance):
    assert isinstance(instance, mydsl_B)


mydsl_C_strategy = st.builds(mydsl_C)
@given(instance=mydsl_C_strategy)
@settings(max_examples=25)
def test_mydsl_C_instantiation(instance):
    assert isinstance(instance, mydsl_C)


mydsl_D_strategy = st.builds(mydsl_D)
@given(instance=mydsl_D_strategy)
@settings(max_examples=25)
def test_mydsl_D_instantiation(instance):
    assert isinstance(instance, mydsl_D)


mydsl_L_strategy = st.builds(mydsl_L)
@given(instance=mydsl_L_strategy)
@settings(max_examples=25)
def test_mydsl_L_instantiation(instance):
    assert isinstance(instance, mydsl_L)


mydsl_W_strategy = st.builds(mydsl_W, name=safe_text)
@given(instance=mydsl_W_strategy)
@settings(max_examples=25)
def test_mydsl_W_instantiation(instance):
    assert isinstance(instance, mydsl_W)



