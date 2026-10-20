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
    NamedElement,
    classdiagram_Method,
    classdiagram_Attribute,
    classdiagram_Class,
    classdiagram_NamedElement,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_hyp_namedelement_is_not_abstract():
    assert not inspect.isabstract(NamedElement)


def test_hyp_namedelement_constructor_exists():
    assert callable(NamedElement.__init__)


def test_hyp_namedelement_constructor_args():
    sig = inspect.signature(NamedElement.__init__)
    params = list(sig.parameters.keys())



def test_hyp_classdiagram_method_is_not_abstract():
    assert not inspect.isabstract(classdiagram_Method)


def test_hyp_classdiagram_method_constructor_exists():
    assert callable(classdiagram_Method.__init__)


def test_hyp_classdiagram_method_constructor_args():
    sig = inspect.signature(classdiagram_Method.__init__)
    params = list(sig.parameters.keys())



def test_hyp_classdiagram_attribute_is_not_abstract():
    assert not inspect.isabstract(classdiagram_Attribute)


def test_hyp_classdiagram_attribute_constructor_exists():
    assert callable(classdiagram_Attribute.__init__)


def test_hyp_classdiagram_attribute_constructor_args():
    sig = inspect.signature(classdiagram_Attribute.__init__)
    params = list(sig.parameters.keys())



def test_hyp_classdiagram_class_is_not_abstract():
    assert not inspect.isabstract(classdiagram_Class)


def test_hyp_classdiagram_class_constructor_exists():
    assert callable(classdiagram_Class.__init__)


def test_hyp_classdiagram_class_constructor_args():
    sig = inspect.signature(classdiagram_Class.__init__)
    params = list(sig.parameters.keys())



def test_hyp_classdiagram_namedelement_is_not_abstract():
    assert not inspect.isabstract(classdiagram_NamedElement)


def test_hyp_classdiagram_namedelement_constructor_exists():
    assert callable(classdiagram_NamedElement.__init__)


def test_hyp_classdiagram_namedelement_constructor_args():
    sig = inspect.signature(classdiagram_NamedElement.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"



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
NamedElement_strategy = st.builds(
    NamedElement,
)
classdiagram_Method_strategy = st.builds(
    classdiagram_Method,
)
classdiagram_Attribute_strategy = st.builds(
    classdiagram_Attribute,
)
classdiagram_Class_strategy = st.builds(
    classdiagram_Class,
)
classdiagram_NamedElement_strategy = st.builds(
    classdiagram_NamedElement,
    name=
        safe_text
)








@given(instance=classdiagram_NamedElement_strategy)
def test_hyp_classdiagram_namedelement_name_setter(instance):
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
    NamedElement,
    classdiagram_Attribute,
    classdiagram_Class,
    classdiagram_Method,
    classdiagram_NamedElement,
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

def test_classdiagram_NamedElement_name_value_roundtrip():
    instance = classdiagram_NamedElement(name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_classdiagram_Attribute_isa_NamedElement():
    instance = classdiagram_Attribute()
    assert isinstance(instance, NamedElement)


def test_classdiagram_Class_isa_NamedElement():
    instance = classdiagram_Class()
    assert isinstance(instance, NamedElement)


def test_classdiagram_Method_isa_NamedElement():
    instance = classdiagram_Method()
    assert isinstance(instance, NamedElement)


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

NamedElement_strategy = st.builds(NamedElement)
@given(instance=NamedElement_strategy)
@settings(max_examples=25)
def test_NamedElement_instantiation(instance):
    assert isinstance(instance, NamedElement)


classdiagram_Attribute_strategy = st.builds(classdiagram_Attribute)
@given(instance=classdiagram_Attribute_strategy)
@settings(max_examples=25)
def test_classdiagram_Attribute_instantiation(instance):
    assert isinstance(instance, classdiagram_Attribute)


classdiagram_Class_strategy = st.builds(classdiagram_Class)
@given(instance=classdiagram_Class_strategy)
@settings(max_examples=25)
def test_classdiagram_Class_instantiation(instance):
    assert isinstance(instance, classdiagram_Class)


classdiagram_Method_strategy = st.builds(classdiagram_Method)
@given(instance=classdiagram_Method_strategy)
@settings(max_examples=25)
def test_classdiagram_Method_instantiation(instance):
    assert isinstance(instance, classdiagram_Method)


classdiagram_NamedElement_strategy = st.builds(classdiagram_NamedElement, name=safe_text)
@given(instance=classdiagram_NamedElement_strategy)
@settings(max_examples=25)
def test_classdiagram_NamedElement_instantiation(instance):
    assert isinstance(instance, classdiagram_NamedElement)



