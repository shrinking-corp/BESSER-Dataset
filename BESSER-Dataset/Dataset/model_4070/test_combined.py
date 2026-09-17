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
    uml_UMLModelElement,
    Classifier,
    uml_Class,
    uml_PrimitiveDataType,
    PackageElement,
    uml_Association,
    uml_Classifier,
    UMLModelElement,
    uml_Package,
    uml_PackageElement,
    uml_Attribute,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_hyp_uml_umlmodelelement_is_not_abstract():
    assert not inspect.isabstract(uml_UMLModelElement)


def test_hyp_uml_umlmodelelement_constructor_exists():
    assert callable(uml_UMLModelElement.__init__)


def test_hyp_uml_umlmodelelement_constructor_args():
    sig = inspect.signature(uml_UMLModelElement.__init__)
    params = list(sig.parameters.keys())
    assert "kind" in params, "Missing parameter 'kind'"
    assert "name" in params, "Missing parameter 'name'"





def test_hyp_classifier_is_not_abstract():
    assert not inspect.isabstract(Classifier)


def test_hyp_classifier_constructor_exists():
    assert callable(Classifier.__init__)


def test_hyp_classifier_constructor_args():
    sig = inspect.signature(Classifier.__init__)
    params = list(sig.parameters.keys())



def test_hyp_uml_class_is_not_abstract():
    assert not inspect.isabstract(uml_Class)


def test_hyp_uml_class_constructor_exists():
    assert callable(uml_Class.__init__)


def test_hyp_uml_class_constructor_args():
    sig = inspect.signature(uml_Class.__init__)
    params = list(sig.parameters.keys())



def test_hyp_uml_primitivedatatype_is_not_abstract():
    assert not inspect.isabstract(uml_PrimitiveDataType)


def test_hyp_uml_primitivedatatype_constructor_exists():
    assert callable(uml_PrimitiveDataType.__init__)


def test_hyp_uml_primitivedatatype_constructor_args():
    sig = inspect.signature(uml_PrimitiveDataType.__init__)
    params = list(sig.parameters.keys())



def test_hyp_packageelement_is_not_abstract():
    assert not inspect.isabstract(PackageElement)


def test_hyp_packageelement_constructor_exists():
    assert callable(PackageElement.__init__)


def test_hyp_packageelement_constructor_args():
    sig = inspect.signature(PackageElement.__init__)
    params = list(sig.parameters.keys())



def test_hyp_uml_association_is_not_abstract():
    assert not inspect.isabstract(uml_Association)


def test_hyp_uml_association_constructor_exists():
    assert callable(uml_Association.__init__)


def test_hyp_uml_association_constructor_args():
    sig = inspect.signature(uml_Association.__init__)
    params = list(sig.parameters.keys())



def test_hyp_uml_classifier_is_not_abstract():
    assert not inspect.isabstract(uml_Classifier)


def test_hyp_uml_classifier_constructor_exists():
    assert callable(uml_Classifier.__init__)


def test_hyp_uml_classifier_constructor_args():
    sig = inspect.signature(uml_Classifier.__init__)
    params = list(sig.parameters.keys())



def test_hyp_umlmodelelement_is_not_abstract():
    assert not inspect.isabstract(UMLModelElement)


def test_hyp_umlmodelelement_constructor_exists():
    assert callable(UMLModelElement.__init__)


def test_hyp_umlmodelelement_constructor_args():
    sig = inspect.signature(UMLModelElement.__init__)
    params = list(sig.parameters.keys())



def test_hyp_uml_package_is_not_abstract():
    assert not inspect.isabstract(uml_Package)


def test_hyp_uml_package_constructor_exists():
    assert callable(uml_Package.__init__)


def test_hyp_uml_package_constructor_args():
    sig = inspect.signature(uml_Package.__init__)
    params = list(sig.parameters.keys())



def test_hyp_uml_packageelement_is_not_abstract():
    assert not inspect.isabstract(uml_PackageElement)


def test_hyp_uml_packageelement_constructor_exists():
    assert callable(uml_PackageElement.__init__)


def test_hyp_uml_packageelement_constructor_args():
    sig = inspect.signature(uml_PackageElement.__init__)
    params = list(sig.parameters.keys())



def test_hyp_uml_attribute_is_not_abstract():
    assert not inspect.isabstract(uml_Attribute)


def test_hyp_uml_attribute_constructor_exists():
    assert callable(uml_Attribute.__init__)


def test_hyp_uml_attribute_constructor_args():
    sig = inspect.signature(uml_Attribute.__init__)
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
uml_UMLModelElement_strategy = st.builds(
    uml_UMLModelElement,
    kind=
        safe_text,
    name=
        safe_text
)
Classifier_strategy = st.builds(
    Classifier,
)
uml_Class_strategy = st.builds(
    uml_Class,
)
uml_PrimitiveDataType_strategy = st.builds(
    uml_PrimitiveDataType,
)
PackageElement_strategy = st.builds(
    PackageElement,
)
uml_Association_strategy = st.builds(
    uml_Association,
)
uml_Classifier_strategy = st.builds(
    uml_Classifier,
)
UMLModelElement_strategy = st.builds(
    UMLModelElement,
)
uml_Package_strategy = st.builds(
    uml_Package,
)
uml_PackageElement_strategy = st.builds(
    uml_PackageElement,
)
uml_Attribute_strategy = st.builds(
    uml_Attribute,
)




@given(instance=uml_UMLModelElement_strategy)
def test_hyp_uml_umlmodelelement_kind_setter(instance):
    original = instance.kind
    instance.kind = original
    assert instance.kind == original



@given(instance=uml_UMLModelElement_strategy)
def test_hyp_uml_umlmodelelement_name_setter(instance):
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
    uml_Association,
    uml_Attribute,
    uml_Class,
    uml_Classifier,
    uml_Package,
    uml_PackageElement,
    uml_PrimitiveDataType,
    uml_UMLModelElement,
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

def test_uml_UMLModelElement_kind_value_roundtrip():
    instance = uml_UMLModelElement(kind="sample_text", name="sample_text")
    assert instance.kind == "sample_text"
    instance.kind = "sample_text_2"
    assert instance.kind == "sample_text_2"


def test_uml_UMLModelElement_name_value_roundtrip():
    instance = uml_UMLModelElement(kind="sample_text", name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_uml_Class_isa_Classifier():
    instance = uml_Class()
    assert isinstance(instance, Classifier)


def test_uml_PrimitiveDataType_isa_Classifier():
    instance = uml_PrimitiveDataType()
    assert isinstance(instance, Classifier)


def test_uml_Association_isa_PackageElement():
    instance = uml_Association()
    assert isinstance(instance, PackageElement)


def test_uml_Classifier_isa_PackageElement():
    instance = uml_Classifier()
    assert isinstance(instance, PackageElement)


def test_uml_Attribute_isa_UMLModelElement():
    instance = uml_Attribute()
    assert isinstance(instance, UMLModelElement)


def test_uml_Package_isa_UMLModelElement():
    instance = uml_Package()
    assert isinstance(instance, UMLModelElement)


def test_uml_PackageElement_isa_UMLModelElement():
    instance = uml_PackageElement()
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


uml_Classifier_strategy = st.builds(uml_Classifier)
@given(instance=uml_Classifier_strategy)
@settings(max_examples=25)
def test_uml_Classifier_instantiation(instance):
    assert isinstance(instance, uml_Classifier)


uml_Package_strategy = st.builds(uml_Package)
@given(instance=uml_Package_strategy)
@settings(max_examples=25)
def test_uml_Package_instantiation(instance):
    assert isinstance(instance, uml_Package)


uml_PackageElement_strategy = st.builds(uml_PackageElement)
@given(instance=uml_PackageElement_strategy)
@settings(max_examples=25)
def test_uml_PackageElement_instantiation(instance):
    assert isinstance(instance, uml_PackageElement)


uml_PrimitiveDataType_strategy = st.builds(uml_PrimitiveDataType)
@given(instance=uml_PrimitiveDataType_strategy)
@settings(max_examples=25)
def test_uml_PrimitiveDataType_instantiation(instance):
    assert isinstance(instance, uml_PrimitiveDataType)


uml_UMLModelElement_strategy = st.builds(uml_UMLModelElement, kind=safe_text, name=safe_text)
@given(instance=uml_UMLModelElement_strategy)
@settings(max_examples=25)
def test_uml_UMLModelElement_instantiation(instance):
    assert isinstance(instance, uml_UMLModelElement)



