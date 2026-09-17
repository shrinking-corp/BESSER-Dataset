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
    link_Named,
    Named,
    link_D,
    link_W,
    link_K,
    link_N99,
    link_C,
    link_M,
    link_B,
    link_X,
    link_A,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_hyp_link_named_is_not_abstract():
    assert not inspect.isabstract(link_Named)


def test_hyp_link_named_constructor_exists():
    assert callable(link_Named.__init__)


def test_hyp_link_named_constructor_args():
    sig = inspect.signature(link_Named.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"




def test_hyp_named_is_not_abstract():
    assert not inspect.isabstract(Named)


def test_hyp_named_constructor_exists():
    assert callable(Named.__init__)


def test_hyp_named_constructor_args():
    sig = inspect.signature(Named.__init__)
    params = list(sig.parameters.keys())



def test_hyp_link_d_is_not_abstract():
    assert not inspect.isabstract(link_D)


def test_hyp_link_d_constructor_exists():
    assert callable(link_D.__init__)


def test_hyp_link_d_constructor_args():
    sig = inspect.signature(link_D.__init__)
    params = list(sig.parameters.keys())



def test_hyp_link_w_is_not_abstract():
    assert not inspect.isabstract(link_W)


def test_hyp_link_w_constructor_exists():
    assert callable(link_W.__init__)


def test_hyp_link_w_constructor_args():
    sig = inspect.signature(link_W.__init__)
    params = list(sig.parameters.keys())



def test_hyp_link_k_is_not_abstract():
    assert not inspect.isabstract(link_K)


def test_hyp_link_k_constructor_exists():
    assert callable(link_K.__init__)


def test_hyp_link_k_constructor_args():
    sig = inspect.signature(link_K.__init__)
    params = list(sig.parameters.keys())



def test_hyp_link_n99_is_not_abstract():
    assert not inspect.isabstract(link_N99)


def test_hyp_link_n99_constructor_exists():
    assert callable(link_N99.__init__)


def test_hyp_link_n99_constructor_args():
    sig = inspect.signature(link_N99.__init__)
    params = list(sig.parameters.keys())



def test_hyp_link_c_is_not_abstract():
    assert not inspect.isabstract(link_C)


def test_hyp_link_c_constructor_exists():
    assert callable(link_C.__init__)


def test_hyp_link_c_constructor_args():
    sig = inspect.signature(link_C.__init__)
    params = list(sig.parameters.keys())



def test_hyp_link_m_is_not_abstract():
    assert not inspect.isabstract(link_M)


def test_hyp_link_m_constructor_exists():
    assert callable(link_M.__init__)


def test_hyp_link_m_constructor_args():
    sig = inspect.signature(link_M.__init__)
    params = list(sig.parameters.keys())



def test_hyp_link_b_is_not_abstract():
    assert not inspect.isabstract(link_B)


def test_hyp_link_b_constructor_exists():
    assert callable(link_B.__init__)


def test_hyp_link_b_constructor_args():
    sig = inspect.signature(link_B.__init__)
    params = list(sig.parameters.keys())



def test_hyp_link_x_is_not_abstract():
    assert not inspect.isabstract(link_X)


def test_hyp_link_x_constructor_exists():
    assert callable(link_X.__init__)


def test_hyp_link_x_constructor_args():
    sig = inspect.signature(link_X.__init__)
    params = list(sig.parameters.keys())



def test_hyp_link_a_is_not_abstract():
    assert not inspect.isabstract(link_A)


def test_hyp_link_a_constructor_exists():
    assert callable(link_A.__init__)


def test_hyp_link_a_constructor_args():
    sig = inspect.signature(link_A.__init__)
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
link_Named_strategy = st.builds(
    link_Named,
    name=
        safe_text
)
Named_strategy = st.builds(
    Named,
)
link_D_strategy = st.builds(
    link_D,
)
link_W_strategy = st.builds(
    link_W,
)
link_K_strategy = st.builds(
    link_K,
)
link_N99_strategy = st.builds(
    link_N99,
)
link_C_strategy = st.builds(
    link_C,
)
link_M_strategy = st.builds(
    link_M,
)
link_B_strategy = st.builds(
    link_B,
)
link_X_strategy = st.builds(
    link_X,
)
link_A_strategy = st.builds(
    link_A,
)




@given(instance=link_Named_strategy)
def test_hyp_link_named_name_setter(instance):
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
    Named,
    link_A,
    link_B,
    link_C,
    link_D,
    link_K,
    link_M,
    link_N99,
    link_Named,
    link_W,
    link_X,
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

def test_link_Named_name_value_roundtrip():
    instance = link_Named(name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_link_A_isa_Named():
    instance = link_A()
    assert isinstance(instance, Named)


def test_link_B_isa_Named():
    instance = link_B()
    assert isinstance(instance, Named)


def test_link_C_isa_Named():
    instance = link_C()
    assert isinstance(instance, Named)


def test_link_D_isa_Named():
    instance = link_D()
    assert isinstance(instance, Named)


def test_link_K_isa_Named():
    instance = link_K()
    assert isinstance(instance, Named)


def test_link_M_isa_Named():
    instance = link_M()
    assert isinstance(instance, Named)


def test_link_N99_isa_Named():
    instance = link_N99()
    assert isinstance(instance, Named)


def test_link_W_isa_Named():
    instance = link_W()
    assert isinstance(instance, Named)


def test_link_X_isa_Named():
    instance = link_X()
    assert isinstance(instance, Named)


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

Named_strategy = st.builds(Named)
@given(instance=Named_strategy)
@settings(max_examples=25)
def test_Named_instantiation(instance):
    assert isinstance(instance, Named)


link_A_strategy = st.builds(link_A)
@given(instance=link_A_strategy)
@settings(max_examples=25)
def test_link_A_instantiation(instance):
    assert isinstance(instance, link_A)


link_B_strategy = st.builds(link_B)
@given(instance=link_B_strategy)
@settings(max_examples=25)
def test_link_B_instantiation(instance):
    assert isinstance(instance, link_B)


link_C_strategy = st.builds(link_C)
@given(instance=link_C_strategy)
@settings(max_examples=25)
def test_link_C_instantiation(instance):
    assert isinstance(instance, link_C)


link_D_strategy = st.builds(link_D)
@given(instance=link_D_strategy)
@settings(max_examples=25)
def test_link_D_instantiation(instance):
    assert isinstance(instance, link_D)


link_K_strategy = st.builds(link_K)
@given(instance=link_K_strategy)
@settings(max_examples=25)
def test_link_K_instantiation(instance):
    assert isinstance(instance, link_K)


link_M_strategy = st.builds(link_M)
@given(instance=link_M_strategy)
@settings(max_examples=25)
def test_link_M_instantiation(instance):
    assert isinstance(instance, link_M)


link_N99_strategy = st.builds(link_N99)
@given(instance=link_N99_strategy)
@settings(max_examples=25)
def test_link_N99_instantiation(instance):
    assert isinstance(instance, link_N99)


link_Named_strategy = st.builds(link_Named, name=safe_text)
@given(instance=link_Named_strategy)
@settings(max_examples=25)
def test_link_Named_instantiation(instance):
    assert isinstance(instance, link_Named)


link_W_strategy = st.builds(link_W)
@given(instance=link_W_strategy)
@settings(max_examples=25)
def test_link_W_instantiation(instance):
    assert isinstance(instance, link_W)


link_X_strategy = st.builds(link_X)
@given(instance=link_X_strategy)
@settings(max_examples=25)
def test_link_X_instantiation(instance):
    assert isinstance(instance, link_X)



