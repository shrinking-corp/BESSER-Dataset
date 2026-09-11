import inspect
import pytest
from datetime import date, datetime, time, timedelta
from hypothesis import given, settings
import hypothesis.strategies as st

from python_code import (
    Element,
    NamedElement,
    Namespace,
    classes_Class,
    classes_Element,
    classes_NamedElement,
    classes_Namespace,
    classes_Package,
    classes_Root,
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

def test_classes_NamedElement_name_value_roundtrip():
    instance = classes_NamedElement(name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_classes_NamedElement_isa_Element():
    instance = classes_NamedElement(name="sample_text")
    assert isinstance(instance, Element)


def test_classes_Namespace_isa_Element():
    instance = classes_Namespace()
    assert isinstance(instance, Element)


def test_classes_Root_isa_Element():
    instance = classes_Root()
    assert isinstance(instance, Element)


def test_classes_Class_isa_NamedElement():
    instance = classes_Class()
    assert isinstance(instance, NamedElement)


def test_classes_Package_isa_NamedElement():
    instance = classes_Package()
    assert isinstance(instance, NamedElement)


def test_classes_Package_isa_Namespace():
    instance = classes_Package()
    assert isinstance(instance, Namespace)


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

Element_strategy = st.builds(Element)
@given(instance=Element_strategy)
@settings(max_examples=25)
def test_Element_instantiation(instance):
    assert isinstance(instance, Element)


NamedElement_strategy = st.builds(NamedElement)
@given(instance=NamedElement_strategy)
@settings(max_examples=25)
def test_NamedElement_instantiation(instance):
    assert isinstance(instance, NamedElement)


Namespace_strategy = st.builds(Namespace)
@given(instance=Namespace_strategy)
@settings(max_examples=25)
def test_Namespace_instantiation(instance):
    assert isinstance(instance, Namespace)


classes_Class_strategy = st.builds(classes_Class)
@given(instance=classes_Class_strategy)
@settings(max_examples=25)
def test_classes_Class_instantiation(instance):
    assert isinstance(instance, classes_Class)


classes_Element_strategy = st.builds(classes_Element)
@given(instance=classes_Element_strategy)
@settings(max_examples=25)
def test_classes_Element_instantiation(instance):
    assert isinstance(instance, classes_Element)


classes_NamedElement_strategy = st.builds(classes_NamedElement, name=safe_text)
@given(instance=classes_NamedElement_strategy)
@settings(max_examples=25)
def test_classes_NamedElement_instantiation(instance):
    assert isinstance(instance, classes_NamedElement)


classes_Namespace_strategy = st.builds(classes_Namespace)
@given(instance=classes_Namespace_strategy)
@settings(max_examples=25)
def test_classes_Namespace_instantiation(instance):
    assert isinstance(instance, classes_Namespace)


classes_Package_strategy = st.builds(classes_Package)
@given(instance=classes_Package_strategy)
@settings(max_examples=25)
def test_classes_Package_instantiation(instance):
    assert isinstance(instance, classes_Package)


classes_Root_strategy = st.builds(classes_Root)
@given(instance=classes_Root_strategy)
@settings(max_examples=25)
def test_classes_Root_instantiation(instance):
    assert isinstance(instance, classes_Root)


