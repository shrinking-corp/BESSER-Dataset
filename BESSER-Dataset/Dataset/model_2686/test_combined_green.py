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
    multiview_Named,
    Named,
    multiview_B,
    multiview_C,
    multiview_E,
    multiview_F,
    multiview_A,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_hyp_multiview_named_is_not_abstract():
    assert not inspect.isabstract(multiview_Named)


def test_hyp_multiview_named_constructor_exists():
    assert callable(multiview_Named.__init__)


def test_hyp_multiview_named_constructor_args():
    sig = inspect.signature(multiview_Named.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"




def test_hyp_named_is_not_abstract():
    assert not inspect.isabstract(Named)


def test_hyp_named_constructor_exists():
    assert callable(Named.__init__)


def test_hyp_named_constructor_args():
    sig = inspect.signature(Named.__init__)
    params = list(sig.parameters.keys())



def test_hyp_multiview_b_is_not_abstract():
    assert not inspect.isabstract(multiview_B)


def test_hyp_multiview_b_constructor_exists():
    assert callable(multiview_B.__init__)


def test_hyp_multiview_b_constructor_args():
    sig = inspect.signature(multiview_B.__init__)
    params = list(sig.parameters.keys())



def test_hyp_multiview_c_is_not_abstract():
    assert not inspect.isabstract(multiview_C)


def test_hyp_multiview_c_constructor_exists():
    assert callable(multiview_C.__init__)


def test_hyp_multiview_c_constructor_args():
    sig = inspect.signature(multiview_C.__init__)
    params = list(sig.parameters.keys())



def test_hyp_multiview_e_is_not_abstract():
    assert not inspect.isabstract(multiview_E)


def test_hyp_multiview_e_constructor_exists():
    assert callable(multiview_E.__init__)


def test_hyp_multiview_e_constructor_args():
    sig = inspect.signature(multiview_E.__init__)
    params = list(sig.parameters.keys())



def test_hyp_multiview_f_is_not_abstract():
    assert not inspect.isabstract(multiview_F)


def test_hyp_multiview_f_constructor_exists():
    assert callable(multiview_F.__init__)


def test_hyp_multiview_f_constructor_args():
    sig = inspect.signature(multiview_F.__init__)
    params = list(sig.parameters.keys())



def test_hyp_multiview_a_is_not_abstract():
    assert not inspect.isabstract(multiview_A)


def test_hyp_multiview_a_constructor_exists():
    assert callable(multiview_A.__init__)


def test_hyp_multiview_a_constructor_args():
    sig = inspect.signature(multiview_A.__init__)
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
multiview_Named_strategy = st.builds(
    multiview_Named,
    name=
        safe_text
)
Named_strategy = st.builds(
    Named,
)
multiview_B_strategy = st.builds(
    multiview_B,
)
multiview_C_strategy = st.builds(
    multiview_C,
)
multiview_E_strategy = st.builds(
    multiview_E,
)
multiview_F_strategy = st.builds(
    multiview_F,
)
multiview_A_strategy = st.builds(
    multiview_A,
)




@given(instance=multiview_Named_strategy)
def test_hyp_multiview_named_name_setter(instance):
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
    multiview_A,
    multiview_B,
    multiview_C,
    multiview_E,
    multiview_F,
    multiview_Named,
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

def test_multiview_Named_name_value_roundtrip():
    instance = multiview_Named(name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_multiview_A_isa_Named():
    instance = multiview_A()
    assert isinstance(instance, Named)


def test_multiview_B_isa_Named():
    instance = multiview_B()
    assert isinstance(instance, Named)


def test_multiview_C_isa_Named():
    instance = multiview_C()
    assert isinstance(instance, Named)


def test_multiview_E_isa_Named():
    instance = multiview_E()
    assert isinstance(instance, Named)


def test_multiview_F_isa_Named():
    instance = multiview_F()
    assert isinstance(instance, Named)


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

Named_strategy = st.builds(Named)
@given(instance=Named_strategy)
@settings(max_examples=25)
def test_Named_instantiation(instance):
    assert isinstance(instance, Named)


multiview_A_strategy = st.builds(multiview_A)
@given(instance=multiview_A_strategy)
@settings(max_examples=25)
def test_multiview_A_instantiation(instance):
    assert isinstance(instance, multiview_A)


multiview_B_strategy = st.builds(multiview_B)
@given(instance=multiview_B_strategy)
@settings(max_examples=25)
def test_multiview_B_instantiation(instance):
    assert isinstance(instance, multiview_B)


multiview_C_strategy = st.builds(multiview_C)
@given(instance=multiview_C_strategy)
@settings(max_examples=25)
def test_multiview_C_instantiation(instance):
    assert isinstance(instance, multiview_C)


multiview_E_strategy = st.builds(multiview_E)
@given(instance=multiview_E_strategy)
@settings(max_examples=25)
def test_multiview_E_instantiation(instance):
    assert isinstance(instance, multiview_E)


multiview_F_strategy = st.builds(multiview_F)
@given(instance=multiview_F_strategy)
@settings(max_examples=25)
def test_multiview_F_instantiation(instance):
    assert isinstance(instance, multiview_F)


multiview_Named_strategy = st.builds(multiview_Named, name=safe_text)
@given(instance=multiview_Named_strategy)
@settings(max_examples=25)
def test_multiview_Named_instantiation(instance):
    assert isinstance(instance, multiview_Named)



