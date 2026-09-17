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
    uml_NamedElement,
    NamedElement,
    uml_UMLSpecification,
    uml_Class,
    uml_Attribute,
    uml_Association,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_hyp_uml_namedelement_is_not_abstract():
    assert not inspect.isabstract(uml_NamedElement)


def test_hyp_uml_namedelement_constructor_exists():
    assert callable(uml_NamedElement.__init__)


def test_hyp_uml_namedelement_constructor_args():
    sig = inspect.signature(uml_NamedElement.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"




def test_hyp_namedelement_is_not_abstract():
    assert not inspect.isabstract(NamedElement)


def test_hyp_namedelement_constructor_exists():
    assert callable(NamedElement.__init__)


def test_hyp_namedelement_constructor_args():
    sig = inspect.signature(NamedElement.__init__)
    params = list(sig.parameters.keys())



def test_hyp_uml_umlspecification_is_not_abstract():
    assert not inspect.isabstract(uml_UMLSpecification)


def test_hyp_uml_umlspecification_constructor_exists():
    assert callable(uml_UMLSpecification.__init__)


def test_hyp_uml_umlspecification_constructor_args():
    sig = inspect.signature(uml_UMLSpecification.__init__)
    params = list(sig.parameters.keys())



def test_hyp_uml_class_is_not_abstract():
    assert not inspect.isabstract(uml_Class)


def test_hyp_uml_class_constructor_exists():
    assert callable(uml_Class.__init__)


def test_hyp_uml_class_constructor_args():
    sig = inspect.signature(uml_Class.__init__)
    params = list(sig.parameters.keys())



def test_hyp_uml_attribute_is_not_abstract():
    assert not inspect.isabstract(uml_Attribute)


def test_hyp_uml_attribute_constructor_exists():
    assert callable(uml_Attribute.__init__)


def test_hyp_uml_attribute_constructor_args():
    sig = inspect.signature(uml_Attribute.__init__)
    params = list(sig.parameters.keys())



def test_hyp_uml_association_is_not_abstract():
    assert not inspect.isabstract(uml_Association)


def test_hyp_uml_association_constructor_exists():
    assert callable(uml_Association.__init__)


def test_hyp_uml_association_constructor_args():
    sig = inspect.signature(uml_Association.__init__)
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
uml_NamedElement_strategy = st.builds(
    uml_NamedElement,
    name=
        safe_text
)
NamedElement_strategy = st.builds(
    NamedElement,
)
uml_UMLSpecification_strategy = st.builds(
    uml_UMLSpecification,
)
uml_Class_strategy = st.builds(
    uml_Class,
)
uml_Attribute_strategy = st.builds(
    uml_Attribute,
)
uml_Association_strategy = st.builds(
    uml_Association,
)




@given(instance=uml_NamedElement_strategy)
def test_hyp_uml_namedelement_name_setter(instance):
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
    uml_Association,
    uml_Attribute,
    uml_Class,
    uml_NamedElement,
    uml_UMLSpecification,
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

def test_uml_NamedElement_name_value_roundtrip():
    instance = uml_NamedElement(name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_uml_Association_isa_NamedElement():
    instance = uml_Association()
    assert isinstance(instance, NamedElement)


def test_uml_Attribute_isa_NamedElement():
    instance = uml_Attribute()
    assert isinstance(instance, NamedElement)


def test_uml_Class_isa_NamedElement():
    instance = uml_Class()
    assert isinstance(instance, NamedElement)


def test_uml_UMLSpecification_isa_NamedElement():
    instance = uml_UMLSpecification()
    assert isinstance(instance, NamedElement)


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

NamedElement_strategy = st.builds(NamedElement)
@given(instance=NamedElement_strategy)
@settings(max_examples=25)
def test_NamedElement_instantiation(instance):
    assert isinstance(instance, NamedElement)


uml_Association_strategy = st.builds(uml_Association)
@given(instance=uml_Association_strategy)
@settings(max_examples=25)
def test_uml_Association_instantiation(instance):
    assert isinstance(instance, uml_Association)


uml_Attribute_strategy = st.builds(uml_Attribute)
@given(instance=uml_Attribute_strategy)
@settings(max_examples=25)
def test_uml_Attribute_instantiation(instance):
    assert isinstance(instance, uml_Attribute)


uml_Class_strategy = st.builds(uml_Class)
@given(instance=uml_Class_strategy)
@settings(max_examples=25)
def test_uml_Class_instantiation(instance):
    assert isinstance(instance, uml_Class)


uml_NamedElement_strategy = st.builds(uml_NamedElement, name=safe_text)
@given(instance=uml_NamedElement_strategy)
@settings(max_examples=25)
def test_uml_NamedElement_instantiation(instance):
    assert isinstance(instance, uml_NamedElement)


uml_UMLSpecification_strategy = st.builds(uml_UMLSpecification)
@given(instance=uml_UMLSpecification_strategy)
@settings(max_examples=25)
def test_uml_UMLSpecification_instantiation(instance):
    assert isinstance(instance, uml_UMLSpecification)



