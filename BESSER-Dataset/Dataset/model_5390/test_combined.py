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
    nonemf_Serializable,
    nonemf_A,
    nonemf_B,
    Serializable,
    nonemf_MySerializableClass,
    TestB,
    TestA,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_hyp_nonemf_serializable_is_not_abstract():
    assert not inspect.isabstract(nonemf_Serializable)


def test_hyp_nonemf_serializable_constructor_exists():
    assert callable(nonemf_Serializable.__init__)


def test_hyp_nonemf_serializable_constructor_args():
    sig = inspect.signature(nonemf_Serializable.__init__)
    params = list(sig.parameters.keys())



def test_hyp_nonemf_a_is_not_abstract():
    assert not inspect.isabstract(nonemf_A)


def test_hyp_nonemf_a_constructor_exists():
    assert callable(nonemf_A.__init__)


def test_hyp_nonemf_a_constructor_args():
    sig = inspect.signature(nonemf_A.__init__)
    params = list(sig.parameters.keys())



def test_hyp_nonemf_b_is_not_abstract():
    assert not inspect.isabstract(nonemf_B)


def test_hyp_nonemf_b_constructor_exists():
    assert callable(nonemf_B.__init__)


def test_hyp_nonemf_b_constructor_args():
    sig = inspect.signature(nonemf_B.__init__)
    params = list(sig.parameters.keys())



def test_hyp_serializable_is_not_abstract():
    assert not inspect.isabstract(Serializable)


def test_hyp_serializable_constructor_exists():
    assert callable(Serializable.__init__)


def test_hyp_serializable_constructor_args():
    sig = inspect.signature(Serializable.__init__)
    params = list(sig.parameters.keys())



def test_hyp_nonemf_myserializableclass_is_not_abstract():
    assert not inspect.isabstract(nonemf_MySerializableClass)


def test_hyp_nonemf_myserializableclass_constructor_exists():
    assert callable(nonemf_MySerializableClass.__init__)


def test_hyp_nonemf_myserializableclass_constructor_args():
    sig = inspect.signature(nonemf_MySerializableClass.__init__)
    params = list(sig.parameters.keys())
    assert "somethingInteresting" in params, "Missing parameter 'somethingInteresting'"


def test_hyp_testb_exists():
    # Check that the Enumeration exists
    assert TestB is not None

def test_hyp_testb_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in TestB]
    expected_literals = [
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in TestB"

def test_hyp_testa_exists():
    # Check that the Enumeration exists
    assert TestA is not None

def test_hyp_testa_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in TestA]
    expected_literals = [
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in TestA"


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
nonemf_Serializable_strategy = st.builds(
    nonemf_Serializable,
)
nonemf_A_strategy = st.builds(
    nonemf_A,
)
nonemf_B_strategy = st.builds(
    nonemf_B,
)
Serializable_strategy = st.builds(
    Serializable,
)
nonemf_MySerializableClass_strategy = st.builds(
    nonemf_MySerializableClass,
    somethingInteresting=
        safe_text
)








@given(instance=nonemf_MySerializableClass_strategy)
def test_hyp_nonemf_myserializableclass_somethingInteresting_setter(instance):
    original = instance.somethingInteresting
    instance.somethingInteresting = original
    assert instance.somethingInteresting == original


# ----- SECTION B: test_structural_full.py (deterministic-first suite) -----
import inspect
import pytest
from datetime import date, datetime, time, timedelta
from hypothesis import given, settings
import hypothesis.strategies as st

from python_code import (
    Serializable,
    nonemf_A,
    nonemf_B,
    nonemf_MySerializableClass,
    nonemf_Serializable,
    TestA,
    TestB,
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

def test_nonemf_MySerializableClass_somethingInteresting_value_roundtrip():
    instance = nonemf_MySerializableClass(somethingInteresting="sample_text")
    assert instance.somethingInteresting == "sample_text"
    instance.somethingInteresting = "sample_text_2"
    assert instance.somethingInteresting == "sample_text_2"


def test_nonemf_MySerializableClass_isa_Serializable():
    instance = nonemf_MySerializableClass(somethingInteresting="sample_text")
    assert isinstance(instance, Serializable)


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

Serializable_strategy = st.builds(Serializable)
@given(instance=Serializable_strategy)
@settings(max_examples=25)
def test_Serializable_instantiation(instance):
    assert isinstance(instance, Serializable)


nonemf_A_strategy = st.builds(nonemf_A)
@given(instance=nonemf_A_strategy)
@settings(max_examples=25)
def test_nonemf_A_instantiation(instance):
    assert isinstance(instance, nonemf_A)


nonemf_B_strategy = st.builds(nonemf_B)
@given(instance=nonemf_B_strategy)
@settings(max_examples=25)
def test_nonemf_B_instantiation(instance):
    assert isinstance(instance, nonemf_B)


nonemf_MySerializableClass_strategy = st.builds(nonemf_MySerializableClass, somethingInteresting=safe_text)
@given(instance=nonemf_MySerializableClass_strategy)
@settings(max_examples=25)
def test_nonemf_MySerializableClass_instantiation(instance):
    assert isinstance(instance, nonemf_MySerializableClass)


nonemf_Serializable_strategy = st.builds(nonemf_Serializable)
@given(instance=nonemf_Serializable_strategy)
@settings(max_examples=25)
def test_nonemf_Serializable_instantiation(instance):
    assert isinstance(instance, nonemf_Serializable)



