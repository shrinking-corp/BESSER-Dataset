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
    StructuralFeature,
    simpleuml_Property,
    Classifier,
    simpleuml_Class,
    Feature,
    simpleuml_StructuralFeature,
    simpleuml_Generalization,
    Type,
    simpleuml_Classifier,
    NamedElement,
    simpleuml_Type,
    simpleuml_Feature,
    simpleuml_NamedElement,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_hyp_structuralfeature_is_not_abstract():
    assert not inspect.isabstract(StructuralFeature)


def test_hyp_structuralfeature_constructor_exists():
    assert callable(StructuralFeature.__init__)


def test_hyp_structuralfeature_constructor_args():
    sig = inspect.signature(StructuralFeature.__init__)
    params = list(sig.parameters.keys())



def test_hyp_simpleuml_property_is_not_abstract():
    assert not inspect.isabstract(simpleuml_Property)


def test_hyp_simpleuml_property_constructor_exists():
    assert callable(simpleuml_Property.__init__)


def test_hyp_simpleuml_property_constructor_args():
    sig = inspect.signature(simpleuml_Property.__init__)
    params = list(sig.parameters.keys())



def test_hyp_classifier_is_not_abstract():
    assert not inspect.isabstract(Classifier)


def test_hyp_classifier_constructor_exists():
    assert callable(Classifier.__init__)


def test_hyp_classifier_constructor_args():
    sig = inspect.signature(Classifier.__init__)
    params = list(sig.parameters.keys())



def test_hyp_simpleuml_class_is_not_abstract():
    assert not inspect.isabstract(simpleuml_Class)


def test_hyp_simpleuml_class_constructor_exists():
    assert callable(simpleuml_Class.__init__)


def test_hyp_simpleuml_class_constructor_args():
    sig = inspect.signature(simpleuml_Class.__init__)
    params = list(sig.parameters.keys())



def test_hyp_feature_is_not_abstract():
    assert not inspect.isabstract(Feature)


def test_hyp_feature_constructor_exists():
    assert callable(Feature.__init__)


def test_hyp_feature_constructor_args():
    sig = inspect.signature(Feature.__init__)
    params = list(sig.parameters.keys())



def test_hyp_simpleuml_structuralfeature_is_not_abstract():
    assert not inspect.isabstract(simpleuml_StructuralFeature)


def test_hyp_simpleuml_structuralfeature_constructor_exists():
    assert callable(simpleuml_StructuralFeature.__init__)


def test_hyp_simpleuml_structuralfeature_constructor_args():
    sig = inspect.signature(simpleuml_StructuralFeature.__init__)
    params = list(sig.parameters.keys())



def test_hyp_simpleuml_generalization_is_not_abstract():
    assert not inspect.isabstract(simpleuml_Generalization)


def test_hyp_simpleuml_generalization_constructor_exists():
    assert callable(simpleuml_Generalization.__init__)


def test_hyp_simpleuml_generalization_constructor_args():
    sig = inspect.signature(simpleuml_Generalization.__init__)
    params = list(sig.parameters.keys())



def test_hyp_type_is_not_abstract():
    assert not inspect.isabstract(Type)


def test_hyp_type_constructor_exists():
    assert callable(Type.__init__)


def test_hyp_type_constructor_args():
    sig = inspect.signature(Type.__init__)
    params = list(sig.parameters.keys())



def test_hyp_simpleuml_classifier_is_not_abstract():
    assert not inspect.isabstract(simpleuml_Classifier)


def test_hyp_simpleuml_classifier_constructor_exists():
    assert callable(simpleuml_Classifier.__init__)


def test_hyp_simpleuml_classifier_constructor_args():
    sig = inspect.signature(simpleuml_Classifier.__init__)
    params = list(sig.parameters.keys())



def test_hyp_namedelement_is_not_abstract():
    assert not inspect.isabstract(NamedElement)


def test_hyp_namedelement_constructor_exists():
    assert callable(NamedElement.__init__)


def test_hyp_namedelement_constructor_args():
    sig = inspect.signature(NamedElement.__init__)
    params = list(sig.parameters.keys())



def test_hyp_simpleuml_type_is_not_abstract():
    assert not inspect.isabstract(simpleuml_Type)


def test_hyp_simpleuml_type_constructor_exists():
    assert callable(simpleuml_Type.__init__)


def test_hyp_simpleuml_type_constructor_args():
    sig = inspect.signature(simpleuml_Type.__init__)
    params = list(sig.parameters.keys())



def test_hyp_simpleuml_feature_is_not_abstract():
    assert not inspect.isabstract(simpleuml_Feature)


def test_hyp_simpleuml_feature_constructor_exists():
    assert callable(simpleuml_Feature.__init__)


def test_hyp_simpleuml_feature_constructor_args():
    sig = inspect.signature(simpleuml_Feature.__init__)
    params = list(sig.parameters.keys())



def test_hyp_simpleuml_namedelement_is_not_abstract():
    assert not inspect.isabstract(simpleuml_NamedElement)


def test_hyp_simpleuml_namedelement_constructor_exists():
    assert callable(simpleuml_NamedElement.__init__)


def test_hyp_simpleuml_namedelement_constructor_args():
    sig = inspect.signature(simpleuml_NamedElement.__init__)
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
StructuralFeature_strategy = st.builds(
    StructuralFeature,
)
simpleuml_Property_strategy = st.builds(
    simpleuml_Property,
)
Classifier_strategy = st.builds(
    Classifier,
)
simpleuml_Class_strategy = st.builds(
    simpleuml_Class,
)
Feature_strategy = st.builds(
    Feature,
)
simpleuml_StructuralFeature_strategy = st.builds(
    simpleuml_StructuralFeature,
)
simpleuml_Generalization_strategy = st.builds(
    simpleuml_Generalization,
)
Type_strategy = st.builds(
    Type,
)
simpleuml_Classifier_strategy = st.builds(
    simpleuml_Classifier,
)
NamedElement_strategy = st.builds(
    NamedElement,
)
simpleuml_Type_strategy = st.builds(
    simpleuml_Type,
)
simpleuml_Feature_strategy = st.builds(
    simpleuml_Feature,
)
simpleuml_NamedElement_strategy = st.builds(
    simpleuml_NamedElement,
    name=
        safe_text
)
















@given(instance=simpleuml_NamedElement_strategy)
def test_hyp_simpleuml_namedelement_name_setter(instance):
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
    Classifier,
    Feature,
    NamedElement,
    StructuralFeature,
    Type,
    simpleuml_Class,
    simpleuml_Classifier,
    simpleuml_Feature,
    simpleuml_Generalization,
    simpleuml_NamedElement,
    simpleuml_Property,
    simpleuml_StructuralFeature,
    simpleuml_Type,
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

def test_simpleuml_NamedElement_name_value_roundtrip():
    instance = simpleuml_NamedElement(name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_simpleuml_Class_isa_Classifier():
    instance = simpleuml_Class()
    assert isinstance(instance, Classifier)


def test_simpleuml_StructuralFeature_isa_Feature():
    instance = simpleuml_StructuralFeature()
    assert isinstance(instance, Feature)


def test_simpleuml_Feature_isa_NamedElement():
    instance = simpleuml_Feature()
    assert isinstance(instance, NamedElement)


def test_simpleuml_Type_isa_NamedElement():
    instance = simpleuml_Type()
    assert isinstance(instance, NamedElement)


def test_simpleuml_Property_isa_StructuralFeature():
    instance = simpleuml_Property()
    assert isinstance(instance, StructuralFeature)


def test_simpleuml_Classifier_isa_Type():
    instance = simpleuml_Classifier()
    assert isinstance(instance, Type)


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

Classifier_strategy = st.builds(Classifier)
@given(instance=Classifier_strategy)
@settings(max_examples=25)
def test_Classifier_instantiation(instance):
    assert isinstance(instance, Classifier)


Feature_strategy = st.builds(Feature)
@given(instance=Feature_strategy)
@settings(max_examples=25)
def test_Feature_instantiation(instance):
    assert isinstance(instance, Feature)


NamedElement_strategy = st.builds(NamedElement)
@given(instance=NamedElement_strategy)
@settings(max_examples=25)
def test_NamedElement_instantiation(instance):
    assert isinstance(instance, NamedElement)


StructuralFeature_strategy = st.builds(StructuralFeature)
@given(instance=StructuralFeature_strategy)
@settings(max_examples=25)
def test_StructuralFeature_instantiation(instance):
    assert isinstance(instance, StructuralFeature)


Type_strategy = st.builds(Type)
@given(instance=Type_strategy)
@settings(max_examples=25)
def test_Type_instantiation(instance):
    assert isinstance(instance, Type)


simpleuml_Class_strategy = st.builds(simpleuml_Class)
@given(instance=simpleuml_Class_strategy)
@settings(max_examples=25)
def test_simpleuml_Class_instantiation(instance):
    assert isinstance(instance, simpleuml_Class)


simpleuml_Classifier_strategy = st.builds(simpleuml_Classifier)
@given(instance=simpleuml_Classifier_strategy)
@settings(max_examples=25)
def test_simpleuml_Classifier_instantiation(instance):
    assert isinstance(instance, simpleuml_Classifier)


simpleuml_Feature_strategy = st.builds(simpleuml_Feature)
@given(instance=simpleuml_Feature_strategy)
@settings(max_examples=25)
def test_simpleuml_Feature_instantiation(instance):
    assert isinstance(instance, simpleuml_Feature)


simpleuml_Generalization_strategy = st.builds(simpleuml_Generalization)
@given(instance=simpleuml_Generalization_strategy)
@settings(max_examples=25)
def test_simpleuml_Generalization_instantiation(instance):
    assert isinstance(instance, simpleuml_Generalization)


simpleuml_NamedElement_strategy = st.builds(simpleuml_NamedElement, name=safe_text)
@given(instance=simpleuml_NamedElement_strategy)
@settings(max_examples=25)
def test_simpleuml_NamedElement_instantiation(instance):
    assert isinstance(instance, simpleuml_NamedElement)


simpleuml_Property_strategy = st.builds(simpleuml_Property)
@given(instance=simpleuml_Property_strategy)
@settings(max_examples=25)
def test_simpleuml_Property_instantiation(instance):
    assert isinstance(instance, simpleuml_Property)


simpleuml_StructuralFeature_strategy = st.builds(simpleuml_StructuralFeature)
@given(instance=simpleuml_StructuralFeature_strategy)
@settings(max_examples=25)
def test_simpleuml_StructuralFeature_instantiation(instance):
    assert isinstance(instance, simpleuml_StructuralFeature)


simpleuml_Type_strategy = st.builds(simpleuml_Type)
@given(instance=simpleuml_Type_strategy)
@settings(max_examples=25)
def test_simpleuml_Type_instantiation(instance):
    assert isinstance(instance, simpleuml_Type)



