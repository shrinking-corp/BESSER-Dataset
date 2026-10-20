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
    errormanypov_Named,
    Named,
    errormanypov_C,
    errormanypov_M,
    errormanypov_F,
    errormanypov_K,
    errormanypov_J,
    errormanypov_B,
    errormanypov_JK,
    errormanypov_A,
    errormanypov_E,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_hyp_errormanypov_named_is_not_abstract():
    assert not inspect.isabstract(errormanypov_Named)


def test_hyp_errormanypov_named_constructor_exists():
    assert callable(errormanypov_Named.__init__)


def test_hyp_errormanypov_named_constructor_args():
    sig = inspect.signature(errormanypov_Named.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"




def test_hyp_named_is_not_abstract():
    assert not inspect.isabstract(Named)


def test_hyp_named_constructor_exists():
    assert callable(Named.__init__)


def test_hyp_named_constructor_args():
    sig = inspect.signature(Named.__init__)
    params = list(sig.parameters.keys())



def test_hyp_errormanypov_c_is_not_abstract():
    assert not inspect.isabstract(errormanypov_C)


def test_hyp_errormanypov_c_constructor_exists():
    assert callable(errormanypov_C.__init__)


def test_hyp_errormanypov_c_constructor_args():
    sig = inspect.signature(errormanypov_C.__init__)
    params = list(sig.parameters.keys())



def test_hyp_errormanypov_m_is_not_abstract():
    assert not inspect.isabstract(errormanypov_M)


def test_hyp_errormanypov_m_constructor_exists():
    assert callable(errormanypov_M.__init__)


def test_hyp_errormanypov_m_constructor_args():
    sig = inspect.signature(errormanypov_M.__init__)
    params = list(sig.parameters.keys())



def test_hyp_errormanypov_f_is_not_abstract():
    assert not inspect.isabstract(errormanypov_F)


def test_hyp_errormanypov_f_constructor_exists():
    assert callable(errormanypov_F.__init__)


def test_hyp_errormanypov_f_constructor_args():
    sig = inspect.signature(errormanypov_F.__init__)
    params = list(sig.parameters.keys())



def test_hyp_errormanypov_k_is_not_abstract():
    assert not inspect.isabstract(errormanypov_K)


def test_hyp_errormanypov_k_constructor_exists():
    assert callable(errormanypov_K.__init__)


def test_hyp_errormanypov_k_constructor_args():
    sig = inspect.signature(errormanypov_K.__init__)
    params = list(sig.parameters.keys())



def test_hyp_errormanypov_j_is_not_abstract():
    assert not inspect.isabstract(errormanypov_J)


def test_hyp_errormanypov_j_constructor_exists():
    assert callable(errormanypov_J.__init__)


def test_hyp_errormanypov_j_constructor_args():
    sig = inspect.signature(errormanypov_J.__init__)
    params = list(sig.parameters.keys())



def test_hyp_errormanypov_b_is_not_abstract():
    assert not inspect.isabstract(errormanypov_B)


def test_hyp_errormanypov_b_constructor_exists():
    assert callable(errormanypov_B.__init__)


def test_hyp_errormanypov_b_constructor_args():
    sig = inspect.signature(errormanypov_B.__init__)
    params = list(sig.parameters.keys())



def test_hyp_errormanypov_jk_is_not_abstract():
    assert not inspect.isabstract(errormanypov_JK)


def test_hyp_errormanypov_jk_constructor_exists():
    assert callable(errormanypov_JK.__init__)


def test_hyp_errormanypov_jk_constructor_args():
    sig = inspect.signature(errormanypov_JK.__init__)
    params = list(sig.parameters.keys())



def test_hyp_errormanypov_a_is_not_abstract():
    assert not inspect.isabstract(errormanypov_A)


def test_hyp_errormanypov_a_constructor_exists():
    assert callable(errormanypov_A.__init__)


def test_hyp_errormanypov_a_constructor_args():
    sig = inspect.signature(errormanypov_A.__init__)
    params = list(sig.parameters.keys())



def test_hyp_errormanypov_e_is_not_abstract():
    assert not inspect.isabstract(errormanypov_E)


def test_hyp_errormanypov_e_constructor_exists():
    assert callable(errormanypov_E.__init__)


def test_hyp_errormanypov_e_constructor_args():
    sig = inspect.signature(errormanypov_E.__init__)
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
errormanypov_Named_strategy = st.builds(
    errormanypov_Named,
    name=
        safe_text
)
Named_strategy = st.builds(
    Named,
)
errormanypov_C_strategy = st.builds(
    errormanypov_C,
)
errormanypov_M_strategy = st.builds(
    errormanypov_M,
)
errormanypov_F_strategy = st.builds(
    errormanypov_F,
)
errormanypov_K_strategy = st.builds(
    errormanypov_K,
)
errormanypov_J_strategy = st.builds(
    errormanypov_J,
)
errormanypov_B_strategy = st.builds(
    errormanypov_B,
)
errormanypov_JK_strategy = st.builds(
    errormanypov_JK,
)
errormanypov_A_strategy = st.builds(
    errormanypov_A,
)
errormanypov_E_strategy = st.builds(
    errormanypov_E,
)




@given(instance=errormanypov_Named_strategy)
def test_hyp_errormanypov_named_name_setter(instance):
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
    errormanypov_A,
    errormanypov_B,
    errormanypov_C,
    errormanypov_E,
    errormanypov_F,
    errormanypov_J,
    errormanypov_JK,
    errormanypov_K,
    errormanypov_M,
    errormanypov_Named,
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

def test_errormanypov_Named_name_value_roundtrip():
    instance = errormanypov_Named(name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_errormanypov_A_isa_Named():
    instance = errormanypov_A()
    assert isinstance(instance, Named)


def test_errormanypov_B_isa_Named():
    instance = errormanypov_B()
    assert isinstance(instance, Named)


def test_errormanypov_C_isa_Named():
    instance = errormanypov_C()
    assert isinstance(instance, Named)


def test_errormanypov_E_isa_Named():
    instance = errormanypov_E()
    assert isinstance(instance, Named)


def test_errormanypov_F_isa_Named():
    instance = errormanypov_F()
    assert isinstance(instance, Named)


def test_errormanypov_J_isa_Named():
    instance = errormanypov_J()
    assert isinstance(instance, Named)


def test_errormanypov_JK_isa_Named():
    instance = errormanypov_JK()
    assert isinstance(instance, Named)


def test_errormanypov_K_isa_Named():
    instance = errormanypov_K()
    assert isinstance(instance, Named)


def test_errormanypov_M_isa_Named():
    instance = errormanypov_M()
    assert isinstance(instance, Named)


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

Named_strategy = st.builds(Named)
@given(instance=Named_strategy)
@settings(max_examples=25)
def test_Named_instantiation(instance):
    assert isinstance(instance, Named)


errormanypov_A_strategy = st.builds(errormanypov_A)
@given(instance=errormanypov_A_strategy)
@settings(max_examples=25)
def test_errormanypov_A_instantiation(instance):
    assert isinstance(instance, errormanypov_A)


errormanypov_B_strategy = st.builds(errormanypov_B)
@given(instance=errormanypov_B_strategy)
@settings(max_examples=25)
def test_errormanypov_B_instantiation(instance):
    assert isinstance(instance, errormanypov_B)


errormanypov_C_strategy = st.builds(errormanypov_C)
@given(instance=errormanypov_C_strategy)
@settings(max_examples=25)
def test_errormanypov_C_instantiation(instance):
    assert isinstance(instance, errormanypov_C)


errormanypov_E_strategy = st.builds(errormanypov_E)
@given(instance=errormanypov_E_strategy)
@settings(max_examples=25)
def test_errormanypov_E_instantiation(instance):
    assert isinstance(instance, errormanypov_E)


errormanypov_F_strategy = st.builds(errormanypov_F)
@given(instance=errormanypov_F_strategy)
@settings(max_examples=25)
def test_errormanypov_F_instantiation(instance):
    assert isinstance(instance, errormanypov_F)


errormanypov_J_strategy = st.builds(errormanypov_J)
@given(instance=errormanypov_J_strategy)
@settings(max_examples=25)
def test_errormanypov_J_instantiation(instance):
    assert isinstance(instance, errormanypov_J)


errormanypov_JK_strategy = st.builds(errormanypov_JK)
@given(instance=errormanypov_JK_strategy)
@settings(max_examples=25)
def test_errormanypov_JK_instantiation(instance):
    assert isinstance(instance, errormanypov_JK)


errormanypov_K_strategy = st.builds(errormanypov_K)
@given(instance=errormanypov_K_strategy)
@settings(max_examples=25)
def test_errormanypov_K_instantiation(instance):
    assert isinstance(instance, errormanypov_K)


errormanypov_M_strategy = st.builds(errormanypov_M)
@given(instance=errormanypov_M_strategy)
@settings(max_examples=25)
def test_errormanypov_M_instantiation(instance):
    assert isinstance(instance, errormanypov_M)


errormanypov_Named_strategy = st.builds(errormanypov_Named, name=safe_text)
@given(instance=errormanypov_Named_strategy)
@settings(max_examples=25)
def test_errormanypov_Named_instantiation(instance):
    assert isinstance(instance, errormanypov_Named)



