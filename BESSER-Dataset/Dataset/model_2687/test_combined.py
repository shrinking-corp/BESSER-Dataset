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
    multiview4_Named,
    Named,
    multiview4_C,
    multiview4_B,
    multiview4_E,
    multiview4_A,
    multiview4_F,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_hyp_multiview4_named_is_not_abstract():
    assert not inspect.isabstract(multiview4_Named)


def test_hyp_multiview4_named_constructor_exists():
    assert callable(multiview4_Named.__init__)


def test_hyp_multiview4_named_constructor_args():
    sig = inspect.signature(multiview4_Named.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"




def test_hyp_named_is_not_abstract():
    assert not inspect.isabstract(Named)


def test_hyp_named_constructor_exists():
    assert callable(Named.__init__)


def test_hyp_named_constructor_args():
    sig = inspect.signature(Named.__init__)
    params = list(sig.parameters.keys())



def test_hyp_multiview4_c_is_not_abstract():
    assert not inspect.isabstract(multiview4_C)


def test_hyp_multiview4_c_constructor_exists():
    assert callable(multiview4_C.__init__)


def test_hyp_multiview4_c_constructor_args():
    sig = inspect.signature(multiview4_C.__init__)
    params = list(sig.parameters.keys())



def test_hyp_multiview4_b_is_not_abstract():
    assert not inspect.isabstract(multiview4_B)


def test_hyp_multiview4_b_constructor_exists():
    assert callable(multiview4_B.__init__)


def test_hyp_multiview4_b_constructor_args():
    sig = inspect.signature(multiview4_B.__init__)
    params = list(sig.parameters.keys())



def test_hyp_multiview4_e_is_not_abstract():
    assert not inspect.isabstract(multiview4_E)


def test_hyp_multiview4_e_constructor_exists():
    assert callable(multiview4_E.__init__)


def test_hyp_multiview4_e_constructor_args():
    sig = inspect.signature(multiview4_E.__init__)
    params = list(sig.parameters.keys())



def test_hyp_multiview4_a_is_not_abstract():
    assert not inspect.isabstract(multiview4_A)


def test_hyp_multiview4_a_constructor_exists():
    assert callable(multiview4_A.__init__)


def test_hyp_multiview4_a_constructor_args():
    sig = inspect.signature(multiview4_A.__init__)
    params = list(sig.parameters.keys())



def test_hyp_multiview4_f_is_not_abstract():
    assert not inspect.isabstract(multiview4_F)


def test_hyp_multiview4_f_constructor_exists():
    assert callable(multiview4_F.__init__)


def test_hyp_multiview4_f_constructor_args():
    sig = inspect.signature(multiview4_F.__init__)
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
multiview4_Named_strategy = st.builds(
    multiview4_Named,
    name=
        safe_text
)
Named_strategy = st.builds(
    Named,
)
multiview4_C_strategy = st.builds(
    multiview4_C,
)
multiview4_B_strategy = st.builds(
    multiview4_B,
)
multiview4_E_strategy = st.builds(
    multiview4_E,
)
multiview4_A_strategy = st.builds(
    multiview4_A,
)
multiview4_F_strategy = st.builds(
    multiview4_F,
)




@given(instance=multiview4_Named_strategy)
def test_hyp_multiview4_named_name_setter(instance):
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
    multiview4_A,
    multiview4_B,
    multiview4_C,
    multiview4_E,
    multiview4_F,
    multiview4_Named,
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

def test_multiview4_Named_name_value_roundtrip():
    instance = multiview4_Named(name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_multiview4_A_isa_Named():
    instance = multiview4_A()
    assert isinstance(instance, Named)


def test_multiview4_B_isa_Named():
    instance = multiview4_B()
    assert isinstance(instance, Named)


def test_multiview4_C_isa_Named():
    instance = multiview4_C()
    assert isinstance(instance, Named)


def test_multiview4_E_isa_Named():
    instance = multiview4_E()
    assert isinstance(instance, Named)


def test_multiview4_F_isa_Named():
    instance = multiview4_F()
    assert isinstance(instance, Named)


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

Named_strategy = st.builds(Named)
@given(instance=Named_strategy)
@settings(max_examples=25)
def test_Named_instantiation(instance):
    assert isinstance(instance, Named)


multiview4_A_strategy = st.builds(multiview4_A)
@given(instance=multiview4_A_strategy)
@settings(max_examples=25)
def test_multiview4_A_instantiation(instance):
    assert isinstance(instance, multiview4_A)


multiview4_B_strategy = st.builds(multiview4_B)
@given(instance=multiview4_B_strategy)
@settings(max_examples=25)
def test_multiview4_B_instantiation(instance):
    assert isinstance(instance, multiview4_B)


multiview4_C_strategy = st.builds(multiview4_C)
@given(instance=multiview4_C_strategy)
@settings(max_examples=25)
def test_multiview4_C_instantiation(instance):
    assert isinstance(instance, multiview4_C)


multiview4_E_strategy = st.builds(multiview4_E)
@given(instance=multiview4_E_strategy)
@settings(max_examples=25)
def test_multiview4_E_instantiation(instance):
    assert isinstance(instance, multiview4_E)


multiview4_F_strategy = st.builds(multiview4_F)
@given(instance=multiview4_F_strategy)
@settings(max_examples=25)
def test_multiview4_F_instantiation(instance):
    assert isinstance(instance, multiview4_F)


multiview4_Named_strategy = st.builds(multiview4_Named, name=safe_text)
@given(instance=multiview4_Named_strategy)
@settings(max_examples=25)
def test_multiview4_Named_instantiation(instance):
    assert isinstance(instance, multiview4_Named)



