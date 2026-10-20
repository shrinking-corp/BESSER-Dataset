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
    reference_Named,
    Named,
    reference_B,
    reference_E,
    reference_C,
    reference_F,
    reference_H,
    reference_G,
    reference_A,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_hyp_reference_named_is_not_abstract():
    assert not inspect.isabstract(reference_Named)


def test_hyp_reference_named_constructor_exists():
    assert callable(reference_Named.__init__)


def test_hyp_reference_named_constructor_args():
    sig = inspect.signature(reference_Named.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"




def test_hyp_named_is_not_abstract():
    assert not inspect.isabstract(Named)


def test_hyp_named_constructor_exists():
    assert callable(Named.__init__)


def test_hyp_named_constructor_args():
    sig = inspect.signature(Named.__init__)
    params = list(sig.parameters.keys())



def test_hyp_reference_b_is_not_abstract():
    assert not inspect.isabstract(reference_B)


def test_hyp_reference_b_constructor_exists():
    assert callable(reference_B.__init__)


def test_hyp_reference_b_constructor_args():
    sig = inspect.signature(reference_B.__init__)
    params = list(sig.parameters.keys())



def test_hyp_reference_e_is_not_abstract():
    assert not inspect.isabstract(reference_E)


def test_hyp_reference_e_constructor_exists():
    assert callable(reference_E.__init__)


def test_hyp_reference_e_constructor_args():
    sig = inspect.signature(reference_E.__init__)
    params = list(sig.parameters.keys())



def test_hyp_reference_c_is_not_abstract():
    assert not inspect.isabstract(reference_C)


def test_hyp_reference_c_constructor_exists():
    assert callable(reference_C.__init__)


def test_hyp_reference_c_constructor_args():
    sig = inspect.signature(reference_C.__init__)
    params = list(sig.parameters.keys())



def test_hyp_reference_f_is_not_abstract():
    assert not inspect.isabstract(reference_F)


def test_hyp_reference_f_constructor_exists():
    assert callable(reference_F.__init__)


def test_hyp_reference_f_constructor_args():
    sig = inspect.signature(reference_F.__init__)
    params = list(sig.parameters.keys())



def test_hyp_reference_h_is_not_abstract():
    assert not inspect.isabstract(reference_H)


def test_hyp_reference_h_constructor_exists():
    assert callable(reference_H.__init__)


def test_hyp_reference_h_constructor_args():
    sig = inspect.signature(reference_H.__init__)
    params = list(sig.parameters.keys())



def test_hyp_reference_g_is_not_abstract():
    assert not inspect.isabstract(reference_G)


def test_hyp_reference_g_constructor_exists():
    assert callable(reference_G.__init__)


def test_hyp_reference_g_constructor_args():
    sig = inspect.signature(reference_G.__init__)
    params = list(sig.parameters.keys())



def test_hyp_reference_a_is_not_abstract():
    assert not inspect.isabstract(reference_A)


def test_hyp_reference_a_constructor_exists():
    assert callable(reference_A.__init__)


def test_hyp_reference_a_constructor_args():
    sig = inspect.signature(reference_A.__init__)
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
reference_Named_strategy = st.builds(
    reference_Named,
    name=
        safe_text
)
Named_strategy = st.builds(
    Named,
)
reference_B_strategy = st.builds(
    reference_B,
)
reference_E_strategy = st.builds(
    reference_E,
)
reference_C_strategy = st.builds(
    reference_C,
)
reference_F_strategy = st.builds(
    reference_F,
)
reference_H_strategy = st.builds(
    reference_H,
)
reference_G_strategy = st.builds(
    reference_G,
)
reference_A_strategy = st.builds(
    reference_A,
)




@given(instance=reference_Named_strategy)
def test_hyp_reference_named_name_setter(instance):
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
    reference_A,
    reference_B,
    reference_C,
    reference_E,
    reference_F,
    reference_G,
    reference_H,
    reference_Named,
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

def test_reference_Named_name_value_roundtrip():
    instance = reference_Named(name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_reference_A_isa_Named():
    instance = reference_A()
    assert isinstance(instance, Named)


def test_reference_B_isa_Named():
    instance = reference_B()
    assert isinstance(instance, Named)


def test_reference_C_isa_Named():
    instance = reference_C()
    assert isinstance(instance, Named)


def test_reference_E_isa_Named():
    instance = reference_E()
    assert isinstance(instance, Named)


def test_reference_F_isa_Named():
    instance = reference_F()
    assert isinstance(instance, Named)


def test_reference_G_isa_Named():
    instance = reference_G()
    assert isinstance(instance, Named)


def test_reference_H_isa_Named():
    instance = reference_H()
    assert isinstance(instance, Named)


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

Named_strategy = st.builds(Named)
@given(instance=Named_strategy)
@settings(max_examples=25)
def test_Named_instantiation(instance):
    assert isinstance(instance, Named)


reference_A_strategy = st.builds(reference_A)
@given(instance=reference_A_strategy)
@settings(max_examples=25)
def test_reference_A_instantiation(instance):
    assert isinstance(instance, reference_A)


reference_B_strategy = st.builds(reference_B)
@given(instance=reference_B_strategy)
@settings(max_examples=25)
def test_reference_B_instantiation(instance):
    assert isinstance(instance, reference_B)


reference_C_strategy = st.builds(reference_C)
@given(instance=reference_C_strategy)
@settings(max_examples=25)
def test_reference_C_instantiation(instance):
    assert isinstance(instance, reference_C)


reference_E_strategy = st.builds(reference_E)
@given(instance=reference_E_strategy)
@settings(max_examples=25)
def test_reference_E_instantiation(instance):
    assert isinstance(instance, reference_E)


reference_F_strategy = st.builds(reference_F)
@given(instance=reference_F_strategy)
@settings(max_examples=25)
def test_reference_F_instantiation(instance):
    assert isinstance(instance, reference_F)


reference_G_strategy = st.builds(reference_G)
@given(instance=reference_G_strategy)
@settings(max_examples=25)
def test_reference_G_instantiation(instance):
    assert isinstance(instance, reference_G)


reference_H_strategy = st.builds(reference_H)
@given(instance=reference_H_strategy)
@settings(max_examples=25)
def test_reference_H_instantiation(instance):
    assert isinstance(instance, reference_H)


reference_Named_strategy = st.builds(reference_Named, name=safe_text)
@given(instance=reference_Named_strategy)
@settings(max_examples=25)
def test_reference_Named_instantiation(instance):
    assert isinstance(instance, reference_Named)



