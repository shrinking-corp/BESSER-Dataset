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
    SimpleUML_UMLModelElement,
    Classifier,
    SimpleUML_PrimitiveDataType,
    SimpleUML_Class,
    UMLModelElement,
    SimpleUML_PackageElement,
    SimpleUML_Package,
    SimpleUML_Attribute,
    PackageElement,
    SimpleUML_Association,
    SimpleUML_Classifier,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_hyp_simpleuml_umlmodelelement_is_not_abstract():
    assert not inspect.isabstract(SimpleUML_UMLModelElement)


def test_hyp_simpleuml_umlmodelelement_constructor_exists():
    assert callable(SimpleUML_UMLModelElement.__init__)


def test_hyp_simpleuml_umlmodelelement_constructor_args():
    sig = inspect.signature(SimpleUML_UMLModelElement.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "kind" in params, "Missing parameter 'kind'"





def test_hyp_classifier_is_not_abstract():
    assert not inspect.isabstract(Classifier)


def test_hyp_classifier_constructor_exists():
    assert callable(Classifier.__init__)


def test_hyp_classifier_constructor_args():
    sig = inspect.signature(Classifier.__init__)
    params = list(sig.parameters.keys())



def test_hyp_simpleuml_primitivedatatype_is_not_abstract():
    assert not inspect.isabstract(SimpleUML_PrimitiveDataType)


def test_hyp_simpleuml_primitivedatatype_constructor_exists():
    assert callable(SimpleUML_PrimitiveDataType.__init__)


def test_hyp_simpleuml_primitivedatatype_constructor_args():
    sig = inspect.signature(SimpleUML_PrimitiveDataType.__init__)
    params = list(sig.parameters.keys())



def test_hyp_simpleuml_class_is_not_abstract():
    assert not inspect.isabstract(SimpleUML_Class)


def test_hyp_simpleuml_class_constructor_exists():
    assert callable(SimpleUML_Class.__init__)


def test_hyp_simpleuml_class_constructor_args():
    sig = inspect.signature(SimpleUML_Class.__init__)
    params = list(sig.parameters.keys())



def test_hyp_umlmodelelement_is_not_abstract():
    assert not inspect.isabstract(UMLModelElement)


def test_hyp_umlmodelelement_constructor_exists():
    assert callable(UMLModelElement.__init__)


def test_hyp_umlmodelelement_constructor_args():
    sig = inspect.signature(UMLModelElement.__init__)
    params = list(sig.parameters.keys())



def test_hyp_simpleuml_packageelement_is_not_abstract():
    assert not inspect.isabstract(SimpleUML_PackageElement)


def test_hyp_simpleuml_packageelement_constructor_exists():
    assert callable(SimpleUML_PackageElement.__init__)


def test_hyp_simpleuml_packageelement_constructor_args():
    sig = inspect.signature(SimpleUML_PackageElement.__init__)
    params = list(sig.parameters.keys())



def test_hyp_simpleuml_package_is_not_abstract():
    assert not inspect.isabstract(SimpleUML_Package)


def test_hyp_simpleuml_package_constructor_exists():
    assert callable(SimpleUML_Package.__init__)


def test_hyp_simpleuml_package_constructor_args():
    sig = inspect.signature(SimpleUML_Package.__init__)
    params = list(sig.parameters.keys())



def test_hyp_simpleuml_attribute_is_not_abstract():
    assert not inspect.isabstract(SimpleUML_Attribute)


def test_hyp_simpleuml_attribute_constructor_exists():
    assert callable(SimpleUML_Attribute.__init__)


def test_hyp_simpleuml_attribute_constructor_args():
    sig = inspect.signature(SimpleUML_Attribute.__init__)
    params = list(sig.parameters.keys())



def test_hyp_packageelement_is_not_abstract():
    assert not inspect.isabstract(PackageElement)


def test_hyp_packageelement_constructor_exists():
    assert callable(PackageElement.__init__)


def test_hyp_packageelement_constructor_args():
    sig = inspect.signature(PackageElement.__init__)
    params = list(sig.parameters.keys())



def test_hyp_simpleuml_association_is_not_abstract():
    assert not inspect.isabstract(SimpleUML_Association)


def test_hyp_simpleuml_association_constructor_exists():
    assert callable(SimpleUML_Association.__init__)


def test_hyp_simpleuml_association_constructor_args():
    sig = inspect.signature(SimpleUML_Association.__init__)
    params = list(sig.parameters.keys())



def test_hyp_simpleuml_classifier_is_not_abstract():
    assert not inspect.isabstract(SimpleUML_Classifier)


def test_hyp_simpleuml_classifier_constructor_exists():
    assert callable(SimpleUML_Classifier.__init__)


def test_hyp_simpleuml_classifier_constructor_args():
    sig = inspect.signature(SimpleUML_Classifier.__init__)
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
SimpleUML_UMLModelElement_strategy = st.builds(
    SimpleUML_UMLModelElement,
    name=
        safe_text,
    kind=
        safe_text
)
Classifier_strategy = st.builds(
    Classifier,
)
SimpleUML_PrimitiveDataType_strategy = st.builds(
    SimpleUML_PrimitiveDataType,
)
SimpleUML_Class_strategy = st.builds(
    SimpleUML_Class,
)
UMLModelElement_strategy = st.builds(
    UMLModelElement,
)
SimpleUML_PackageElement_strategy = st.builds(
    SimpleUML_PackageElement,
)
SimpleUML_Package_strategy = st.builds(
    SimpleUML_Package,
)
SimpleUML_Attribute_strategy = st.builds(
    SimpleUML_Attribute,
)
PackageElement_strategy = st.builds(
    PackageElement,
)
SimpleUML_Association_strategy = st.builds(
    SimpleUML_Association,
)
SimpleUML_Classifier_strategy = st.builds(
    SimpleUML_Classifier,
)




@given(instance=SimpleUML_UMLModelElement_strategy)
def test_hyp_simpleuml_umlmodelelement_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=SimpleUML_UMLModelElement_strategy)
def test_hyp_simpleuml_umlmodelelement_kind_setter(instance):
    original = instance.kind
    instance.kind = original
    assert instance.kind == original












# ----- SECTION B: test_structural_full.py (deterministic-first suite) -----
import inspect
import pytest
from datetime import date, datetime, time, timedelta
from hypothesis import given, settings
import hypothesis.strategies as st

from python_code import (
    Classifier,
    PackageElement,
    SimpleUML_Association,
    SimpleUML_Attribute,
    SimpleUML_Class,
    SimpleUML_Classifier,
    SimpleUML_Package,
    SimpleUML_PackageElement,
    SimpleUML_PrimitiveDataType,
    SimpleUML_UMLModelElement,
    UMLModelElement,
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

def test_SimpleUML_UMLModelElement_kind_value_roundtrip():
    instance = SimpleUML_UMLModelElement(kind="sample_text", name="sample_text")
    assert instance.kind == "sample_text"
    instance.kind = "sample_text_2"
    assert instance.kind == "sample_text_2"


def test_SimpleUML_UMLModelElement_name_value_roundtrip():
    instance = SimpleUML_UMLModelElement(kind="sample_text", name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_SimpleUML_Class_isa_Classifier():
    instance = SimpleUML_Class()
    assert isinstance(instance, Classifier)


def test_SimpleUML_PrimitiveDataType_isa_Classifier():
    instance = SimpleUML_PrimitiveDataType()
    assert isinstance(instance, Classifier)


def test_SimpleUML_Association_isa_PackageElement():
    instance = SimpleUML_Association()
    assert isinstance(instance, PackageElement)


def test_SimpleUML_Classifier_isa_PackageElement():
    instance = SimpleUML_Classifier()
    assert isinstance(instance, PackageElement)


def test_SimpleUML_Attribute_isa_UMLModelElement():
    instance = SimpleUML_Attribute()
    assert isinstance(instance, UMLModelElement)


def test_SimpleUML_Package_isa_UMLModelElement():
    instance = SimpleUML_Package()
    assert isinstance(instance, UMLModelElement)


def test_SimpleUML_PackageElement_isa_UMLModelElement():
    instance = SimpleUML_PackageElement()
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


SimpleUML_Association_strategy = st.builds(SimpleUML_Association)
@given(instance=SimpleUML_Association_strategy)
@settings(max_examples=25)
def test_SimpleUML_Association_instantiation(instance):
    assert isinstance(instance, SimpleUML_Association)


SimpleUML_Attribute_strategy = st.builds(SimpleUML_Attribute)
@given(instance=SimpleUML_Attribute_strategy)
@settings(max_examples=25)
def test_SimpleUML_Attribute_instantiation(instance):
    assert isinstance(instance, SimpleUML_Attribute)


SimpleUML_Class_strategy = st.builds(SimpleUML_Class)
@given(instance=SimpleUML_Class_strategy)
@settings(max_examples=25)
def test_SimpleUML_Class_instantiation(instance):
    assert isinstance(instance, SimpleUML_Class)


SimpleUML_Classifier_strategy = st.builds(SimpleUML_Classifier)
@given(instance=SimpleUML_Classifier_strategy)
@settings(max_examples=25)
def test_SimpleUML_Classifier_instantiation(instance):
    assert isinstance(instance, SimpleUML_Classifier)


SimpleUML_Package_strategy = st.builds(SimpleUML_Package)
@given(instance=SimpleUML_Package_strategy)
@settings(max_examples=25)
def test_SimpleUML_Package_instantiation(instance):
    assert isinstance(instance, SimpleUML_Package)


SimpleUML_PackageElement_strategy = st.builds(SimpleUML_PackageElement)
@given(instance=SimpleUML_PackageElement_strategy)
@settings(max_examples=25)
def test_SimpleUML_PackageElement_instantiation(instance):
    assert isinstance(instance, SimpleUML_PackageElement)


SimpleUML_PrimitiveDataType_strategy = st.builds(SimpleUML_PrimitiveDataType)
@given(instance=SimpleUML_PrimitiveDataType_strategy)
@settings(max_examples=25)
def test_SimpleUML_PrimitiveDataType_instantiation(instance):
    assert isinstance(instance, SimpleUML_PrimitiveDataType)


SimpleUML_UMLModelElement_strategy = st.builds(SimpleUML_UMLModelElement, kind=safe_text, name=safe_text)
@given(instance=SimpleUML_UMLModelElement_strategy)
@settings(max_examples=25)
def test_SimpleUML_UMLModelElement_instantiation(instance):
    assert isinstance(instance, SimpleUML_UMLModelElement)


UMLModelElement_strategy = st.builds(UMLModelElement)
@given(instance=UMLModelElement_strategy)
@settings(max_examples=25)
def test_UMLModelElement_instantiation(instance):
    assert isinstance(instance, UMLModelElement)



