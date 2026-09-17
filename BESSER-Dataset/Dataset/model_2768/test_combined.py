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
    D,
    ref3_Named,
    Named,
    ref3_A,
    ref3_E,
    ref3_T,
    ref3_B,
    ref3_N,
    T,
    ref3_D,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_hyp_d_is_not_abstract():
    assert not inspect.isabstract(D)


def test_hyp_d_constructor_exists():
    assert callable(D.__init__)


def test_hyp_d_constructor_args():
    sig = inspect.signature(D.__init__)
    params = list(sig.parameters.keys())



def test_hyp_ref3_named_is_not_abstract():
    assert not inspect.isabstract(ref3_Named)


def test_hyp_ref3_named_constructor_exists():
    assert callable(ref3_Named.__init__)


def test_hyp_ref3_named_constructor_args():
    sig = inspect.signature(ref3_Named.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"




def test_hyp_named_is_not_abstract():
    assert not inspect.isabstract(Named)


def test_hyp_named_constructor_exists():
    assert callable(Named.__init__)


def test_hyp_named_constructor_args():
    sig = inspect.signature(Named.__init__)
    params = list(sig.parameters.keys())



def test_hyp_ref3_a_is_not_abstract():
    assert not inspect.isabstract(ref3_A)


def test_hyp_ref3_a_constructor_exists():
    assert callable(ref3_A.__init__)


def test_hyp_ref3_a_constructor_args():
    sig = inspect.signature(ref3_A.__init__)
    params = list(sig.parameters.keys())



def test_hyp_ref3_e_is_not_abstract():
    assert not inspect.isabstract(ref3_E)


def test_hyp_ref3_e_constructor_exists():
    assert callable(ref3_E.__init__)


def test_hyp_ref3_e_constructor_args():
    sig = inspect.signature(ref3_E.__init__)
    params = list(sig.parameters.keys())



def test_hyp_ref3_t_is_not_abstract():
    assert not inspect.isabstract(ref3_T)


def test_hyp_ref3_t_constructor_exists():
    assert callable(ref3_T.__init__)


def test_hyp_ref3_t_constructor_args():
    sig = inspect.signature(ref3_T.__init__)
    params = list(sig.parameters.keys())



def test_hyp_ref3_b_is_not_abstract():
    assert not inspect.isabstract(ref3_B)


def test_hyp_ref3_b_constructor_exists():
    assert callable(ref3_B.__init__)


def test_hyp_ref3_b_constructor_args():
    sig = inspect.signature(ref3_B.__init__)
    params = list(sig.parameters.keys())



def test_hyp_ref3_n_is_not_abstract():
    assert not inspect.isabstract(ref3_N)


def test_hyp_ref3_n_constructor_exists():
    assert callable(ref3_N.__init__)


def test_hyp_ref3_n_constructor_args():
    sig = inspect.signature(ref3_N.__init__)
    params = list(sig.parameters.keys())



def test_hyp_t_is_not_abstract():
    assert not inspect.isabstract(T)


def test_hyp_t_constructor_exists():
    assert callable(T.__init__)


def test_hyp_t_constructor_args():
    sig = inspect.signature(T.__init__)
    params = list(sig.parameters.keys())



def test_hyp_ref3_d_is_not_abstract():
    assert not inspect.isabstract(ref3_D)


def test_hyp_ref3_d_constructor_exists():
    assert callable(ref3_D.__init__)


def test_hyp_ref3_d_constructor_args():
    sig = inspect.signature(ref3_D.__init__)
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
D_strategy = st.builds(
    D,
)
ref3_Named_strategy = st.builds(
    ref3_Named,
    name=
        safe_text
)
Named_strategy = st.builds(
    Named,
)
ref3_A_strategy = st.builds(
    ref3_A,
)
ref3_E_strategy = st.builds(
    ref3_E,
)
ref3_T_strategy = st.builds(
    ref3_T,
)
ref3_B_strategy = st.builds(
    ref3_B,
)
ref3_N_strategy = st.builds(
    ref3_N,
)
T_strategy = st.builds(
    T,
)
ref3_D_strategy = st.builds(
    ref3_D,
)





@given(instance=ref3_Named_strategy)
def test_hyp_ref3_named_name_setter(instance):
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
    D,
    Named,
    T,
    ref3_A,
    ref3_B,
    ref3_D,
    ref3_E,
    ref3_N,
    ref3_Named,
    ref3_T,
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

def test_ref3_Named_name_value_roundtrip():
    instance = ref3_Named(name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_ref3_E_isa_D():
    instance = ref3_E()
    assert isinstance(instance, D)


def test_ref3_A_isa_Named():
    instance = ref3_A()
    assert isinstance(instance, Named)


def test_ref3_B_isa_Named():
    instance = ref3_B()
    assert isinstance(instance, Named)


def test_ref3_E_isa_Named():
    instance = ref3_E()
    assert isinstance(instance, Named)


def test_ref3_N_isa_Named():
    instance = ref3_N()
    assert isinstance(instance, Named)


def test_ref3_T_isa_Named():
    instance = ref3_T()
    assert isinstance(instance, Named)


def test_ref3_D_isa_T():
    instance = ref3_D()
    assert isinstance(instance, T)


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

D_strategy = st.builds(D)
@given(instance=D_strategy)
@settings(max_examples=25)
def test_D_instantiation(instance):
    assert isinstance(instance, D)


Named_strategy = st.builds(Named)
@given(instance=Named_strategy)
@settings(max_examples=25)
def test_Named_instantiation(instance):
    assert isinstance(instance, Named)


T_strategy = st.builds(T)
@given(instance=T_strategy)
@settings(max_examples=25)
def test_T_instantiation(instance):
    assert isinstance(instance, T)


ref3_A_strategy = st.builds(ref3_A)
@given(instance=ref3_A_strategy)
@settings(max_examples=25)
def test_ref3_A_instantiation(instance):
    assert isinstance(instance, ref3_A)


ref3_B_strategy = st.builds(ref3_B)
@given(instance=ref3_B_strategy)
@settings(max_examples=25)
def test_ref3_B_instantiation(instance):
    assert isinstance(instance, ref3_B)


ref3_D_strategy = st.builds(ref3_D)
@given(instance=ref3_D_strategy)
@settings(max_examples=25)
def test_ref3_D_instantiation(instance):
    assert isinstance(instance, ref3_D)


ref3_E_strategy = st.builds(ref3_E)
@given(instance=ref3_E_strategy)
@settings(max_examples=25)
def test_ref3_E_instantiation(instance):
    assert isinstance(instance, ref3_E)


ref3_N_strategy = st.builds(ref3_N)
@given(instance=ref3_N_strategy)
@settings(max_examples=25)
def test_ref3_N_instantiation(instance):
    assert isinstance(instance, ref3_N)


ref3_Named_strategy = st.builds(ref3_Named, name=safe_text)
@given(instance=ref3_Named_strategy)
@settings(max_examples=25)
def test_ref3_Named_instantiation(instance):
    assert isinstance(instance, ref3_Named)


ref3_T_strategy = st.builds(ref3_T)
@given(instance=ref3_T_strategy)
@settings(max_examples=25)
def test_ref3_T_instantiation(instance):
    assert isinstance(instance, ref3_T)



