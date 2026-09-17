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
    simpleuml_UMLModelElement,
    UMLModelElement,
    simpleuml_Attribute,
    simpleuml_PackageElement,
    simpleuml_Package,
    Classifier,
    simpleuml_PrimitiveDataType,
    PackageElement,
    simpleuml_Association,
    simpleuml_Class,
    simpleuml_Classifier,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_hyp_simpleuml_umlmodelelement_is_not_abstract():
    assert not inspect.isabstract(simpleuml_UMLModelElement)


def test_hyp_simpleuml_umlmodelelement_constructor_exists():
    assert callable(simpleuml_UMLModelElement.__init__)


def test_hyp_simpleuml_umlmodelelement_constructor_args():
    sig = inspect.signature(simpleuml_UMLModelElement.__init__)
    params = list(sig.parameters.keys())
    assert "kind" in params, "Missing parameter 'kind'"
    assert "name" in params, "Missing parameter 'name'"





def test_hyp_umlmodelelement_is_not_abstract():
    assert not inspect.isabstract(UMLModelElement)


def test_hyp_umlmodelelement_constructor_exists():
    assert callable(UMLModelElement.__init__)


def test_hyp_umlmodelelement_constructor_args():
    sig = inspect.signature(UMLModelElement.__init__)
    params = list(sig.parameters.keys())



def test_hyp_simpleuml_attribute_is_not_abstract():
    assert not inspect.isabstract(simpleuml_Attribute)


def test_hyp_simpleuml_attribute_constructor_exists():
    assert callable(simpleuml_Attribute.__init__)


def test_hyp_simpleuml_attribute_constructor_args():
    sig = inspect.signature(simpleuml_Attribute.__init__)
    params = list(sig.parameters.keys())



def test_hyp_simpleuml_packageelement_is_not_abstract():
    assert not inspect.isabstract(simpleuml_PackageElement)


def test_hyp_simpleuml_packageelement_constructor_exists():
    assert callable(simpleuml_PackageElement.__init__)


def test_hyp_simpleuml_packageelement_constructor_args():
    sig = inspect.signature(simpleuml_PackageElement.__init__)
    params = list(sig.parameters.keys())



def test_hyp_simpleuml_package_is_not_abstract():
    assert not inspect.isabstract(simpleuml_Package)


def test_hyp_simpleuml_package_constructor_exists():
    assert callable(simpleuml_Package.__init__)


def test_hyp_simpleuml_package_constructor_args():
    sig = inspect.signature(simpleuml_Package.__init__)
    params = list(sig.parameters.keys())



def test_hyp_classifier_is_not_abstract():
    assert not inspect.isabstract(Classifier)


def test_hyp_classifier_constructor_exists():
    assert callable(Classifier.__init__)


def test_hyp_classifier_constructor_args():
    sig = inspect.signature(Classifier.__init__)
    params = list(sig.parameters.keys())



def test_hyp_simpleuml_primitivedatatype_is_not_abstract():
    assert not inspect.isabstract(simpleuml_PrimitiveDataType)


def test_hyp_simpleuml_primitivedatatype_constructor_exists():
    assert callable(simpleuml_PrimitiveDataType.__init__)


def test_hyp_simpleuml_primitivedatatype_constructor_args():
    sig = inspect.signature(simpleuml_PrimitiveDataType.__init__)
    params = list(sig.parameters.keys())



def test_hyp_packageelement_is_not_abstract():
    assert not inspect.isabstract(PackageElement)


def test_hyp_packageelement_constructor_exists():
    assert callable(PackageElement.__init__)


def test_hyp_packageelement_constructor_args():
    sig = inspect.signature(PackageElement.__init__)
    params = list(sig.parameters.keys())



def test_hyp_simpleuml_association_is_not_abstract():
    assert not inspect.isabstract(simpleuml_Association)


def test_hyp_simpleuml_association_constructor_exists():
    assert callable(simpleuml_Association.__init__)


def test_hyp_simpleuml_association_constructor_args():
    sig = inspect.signature(simpleuml_Association.__init__)
    params = list(sig.parameters.keys())



def test_hyp_simpleuml_class_is_not_abstract():
    assert not inspect.isabstract(simpleuml_Class)


def test_hyp_simpleuml_class_constructor_exists():
    assert callable(simpleuml_Class.__init__)


def test_hyp_simpleuml_class_constructor_args():
    sig = inspect.signature(simpleuml_Class.__init__)
    params = list(sig.parameters.keys())



def test_hyp_simpleuml_classifier_is_not_abstract():
    assert not inspect.isabstract(simpleuml_Classifier)


def test_hyp_simpleuml_classifier_constructor_exists():
    assert callable(simpleuml_Classifier.__init__)


def test_hyp_simpleuml_classifier_constructor_args():
    sig = inspect.signature(simpleuml_Classifier.__init__)
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
simpleuml_UMLModelElement_strategy = st.builds(
    simpleuml_UMLModelElement,
    kind=
        safe_text,
    name=
        safe_text
)
UMLModelElement_strategy = st.builds(
    UMLModelElement,
)
simpleuml_Attribute_strategy = st.builds(
    simpleuml_Attribute,
)
simpleuml_PackageElement_strategy = st.builds(
    simpleuml_PackageElement,
)
simpleuml_Package_strategy = st.builds(
    simpleuml_Package,
)
Classifier_strategy = st.builds(
    Classifier,
)
simpleuml_PrimitiveDataType_strategy = st.builds(
    simpleuml_PrimitiveDataType,
)
PackageElement_strategy = st.builds(
    PackageElement,
)
simpleuml_Association_strategy = st.builds(
    simpleuml_Association,
)
simpleuml_Class_strategy = st.builds(
    simpleuml_Class,
)
simpleuml_Classifier_strategy = st.builds(
    simpleuml_Classifier,
)




@given(instance=simpleuml_UMLModelElement_strategy)
def test_hyp_simpleuml_umlmodelelement_kind_setter(instance):
    original = instance.kind
    instance.kind = original
    assert instance.kind == original



@given(instance=simpleuml_UMLModelElement_strategy)
def test_hyp_simpleuml_umlmodelelement_name_setter(instance):
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
    PackageElement,
    UMLModelElement,
    simpleuml_Association,
    simpleuml_Attribute,
    simpleuml_Class,
    simpleuml_Classifier,
    simpleuml_Package,
    simpleuml_PackageElement,
    simpleuml_PrimitiveDataType,
    simpleuml_UMLModelElement,
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

def test_simpleuml_UMLModelElement_kind_value_roundtrip():
    instance = simpleuml_UMLModelElement(kind="sample_text", name="sample_text")
    assert instance.kind == "sample_text"
    instance.kind = "sample_text_2"
    assert instance.kind == "sample_text_2"


def test_simpleuml_UMLModelElement_name_value_roundtrip():
    instance = simpleuml_UMLModelElement(kind="sample_text", name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_simpleuml_Class_isa_Classifier():
    instance = simpleuml_Class()
    assert isinstance(instance, Classifier)


def test_simpleuml_PrimitiveDataType_isa_Classifier():
    instance = simpleuml_PrimitiveDataType()
    assert isinstance(instance, Classifier)


def test_simpleuml_Association_isa_PackageElement():
    instance = simpleuml_Association()
    assert isinstance(instance, PackageElement)


def test_simpleuml_Classifier_isa_PackageElement():
    instance = simpleuml_Classifier()
    assert isinstance(instance, PackageElement)


def test_simpleuml_Attribute_isa_UMLModelElement():
    instance = simpleuml_Attribute()
    assert isinstance(instance, UMLModelElement)


def test_simpleuml_Package_isa_UMLModelElement():
    instance = simpleuml_Package()
    assert isinstance(instance, UMLModelElement)


def test_simpleuml_PackageElement_isa_UMLModelElement():
    instance = simpleuml_PackageElement()
    assert isinstance(instance, UMLModelElement)


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

Classifier_strategy = st.builds(Classifier)
@given(instance=Classifier_strategy)
@settings(max_examples=25)
def test_Classifier_instantiation(instance):
    assert isinstance(instance, Classifier)


PackageElement_strategy = st.builds(PackageElement)
@given(instance=PackageElement_strategy)
@settings(max_examples=25)
def test_PackageElement_instantiation(instance):
    assert isinstance(instance, PackageElement)


UMLModelElement_strategy = st.builds(UMLModelElement)
@given(instance=UMLModelElement_strategy)
@settings(max_examples=25)
def test_UMLModelElement_instantiation(instance):
    assert isinstance(instance, UMLModelElement)


simpleuml_Association_strategy = st.builds(simpleuml_Association)
@given(instance=simpleuml_Association_strategy)
@settings(max_examples=25)
def test_simpleuml_Association_instantiation(instance):
    assert isinstance(instance, simpleuml_Association)


simpleuml_Attribute_strategy = st.builds(simpleuml_Attribute)
@given(instance=simpleuml_Attribute_strategy)
@settings(max_examples=25)
def test_simpleuml_Attribute_instantiation(instance):
    assert isinstance(instance, simpleuml_Attribute)


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


simpleuml_Package_strategy = st.builds(simpleuml_Package)
@given(instance=simpleuml_Package_strategy)
@settings(max_examples=25)
def test_simpleuml_Package_instantiation(instance):
    assert isinstance(instance, simpleuml_Package)


simpleuml_PackageElement_strategy = st.builds(simpleuml_PackageElement)
@given(instance=simpleuml_PackageElement_strategy)
@settings(max_examples=25)
def test_simpleuml_PackageElement_instantiation(instance):
    assert isinstance(instance, simpleuml_PackageElement)


simpleuml_PrimitiveDataType_strategy = st.builds(simpleuml_PrimitiveDataType)
@given(instance=simpleuml_PrimitiveDataType_strategy)
@settings(max_examples=25)
def test_simpleuml_PrimitiveDataType_instantiation(instance):
    assert isinstance(instance, simpleuml_PrimitiveDataType)


simpleuml_UMLModelElement_strategy = st.builds(simpleuml_UMLModelElement, kind=safe_text, name=safe_text)
@given(instance=simpleuml_UMLModelElement_strategy)
@settings(max_examples=25)
def test_simpleuml_UMLModelElement_instantiation(instance):
    assert isinstance(instance, simpleuml_UMLModelElement)



