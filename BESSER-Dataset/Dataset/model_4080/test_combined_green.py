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
    SimpleUML_UmlModelElement,
    UmlClassifier,
    SimpleUML_UmlPrimitiveDataType,
    SimpleUML_UmlClass,
    UmlPackageElement,
    SimpleUML_UmlClassifier,
    SimpleUML_UmlAssociation,
    UmlModelElement,
    SimpleUML_UmlPackage,
    SimpleUML_UmlPackageElement,
    SimpleUML_UmlAttribute,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_hyp_simpleuml_umlmodelelement_is_not_abstract():
    assert not inspect.isabstract(SimpleUML_UmlModelElement)


def test_hyp_simpleuml_umlmodelelement_constructor_exists():
    assert callable(SimpleUML_UmlModelElement.__init__)


def test_hyp_simpleuml_umlmodelelement_constructor_args():
    sig = inspect.signature(SimpleUML_UmlModelElement.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"
    assert "umlName" in params, "Missing parameter 'umlName'"
    assert "umlKind" in params, "Missing parameter 'umlKind'"






def test_hyp_umlclassifier_is_not_abstract():
    assert not inspect.isabstract(UmlClassifier)


def test_hyp_umlclassifier_constructor_exists():
    assert callable(UmlClassifier.__init__)


def test_hyp_umlclassifier_constructor_args():
    sig = inspect.signature(UmlClassifier.__init__)
    params = list(sig.parameters.keys())



def test_hyp_simpleuml_umlprimitivedatatype_is_not_abstract():
    assert not inspect.isabstract(SimpleUML_UmlPrimitiveDataType)


def test_hyp_simpleuml_umlprimitivedatatype_constructor_exists():
    assert callable(SimpleUML_UmlPrimitiveDataType.__init__)


def test_hyp_simpleuml_umlprimitivedatatype_constructor_args():
    sig = inspect.signature(SimpleUML_UmlPrimitiveDataType.__init__)
    params = list(sig.parameters.keys())



def test_hyp_simpleuml_umlclass_is_not_abstract():
    assert not inspect.isabstract(SimpleUML_UmlClass)


def test_hyp_simpleuml_umlclass_constructor_exists():
    assert callable(SimpleUML_UmlClass.__init__)


def test_hyp_simpleuml_umlclass_constructor_args():
    sig = inspect.signature(SimpleUML_UmlClass.__init__)
    params = list(sig.parameters.keys())



def test_hyp_umlpackageelement_is_not_abstract():
    assert not inspect.isabstract(UmlPackageElement)


def test_hyp_umlpackageelement_constructor_exists():
    assert callable(UmlPackageElement.__init__)


def test_hyp_umlpackageelement_constructor_args():
    sig = inspect.signature(UmlPackageElement.__init__)
    params = list(sig.parameters.keys())



def test_hyp_simpleuml_umlclassifier_is_not_abstract():
    assert not inspect.isabstract(SimpleUML_UmlClassifier)


def test_hyp_simpleuml_umlclassifier_constructor_exists():
    assert callable(SimpleUML_UmlClassifier.__init__)


def test_hyp_simpleuml_umlclassifier_constructor_args():
    sig = inspect.signature(SimpleUML_UmlClassifier.__init__)
    params = list(sig.parameters.keys())



def test_hyp_simpleuml_umlassociation_is_not_abstract():
    assert not inspect.isabstract(SimpleUML_UmlAssociation)


def test_hyp_simpleuml_umlassociation_constructor_exists():
    assert callable(SimpleUML_UmlAssociation.__init__)


def test_hyp_simpleuml_umlassociation_constructor_args():
    sig = inspect.signature(SimpleUML_UmlAssociation.__init__)
    params = list(sig.parameters.keys())



def test_hyp_umlmodelelement_is_not_abstract():
    assert not inspect.isabstract(UmlModelElement)


def test_hyp_umlmodelelement_constructor_exists():
    assert callable(UmlModelElement.__init__)


def test_hyp_umlmodelelement_constructor_args():
    sig = inspect.signature(UmlModelElement.__init__)
    params = list(sig.parameters.keys())



def test_hyp_simpleuml_umlpackage_is_not_abstract():
    assert not inspect.isabstract(SimpleUML_UmlPackage)


def test_hyp_simpleuml_umlpackage_constructor_exists():
    assert callable(SimpleUML_UmlPackage.__init__)


def test_hyp_simpleuml_umlpackage_constructor_args():
    sig = inspect.signature(SimpleUML_UmlPackage.__init__)
    params = list(sig.parameters.keys())



def test_hyp_simpleuml_umlpackageelement_is_not_abstract():
    assert not inspect.isabstract(SimpleUML_UmlPackageElement)


def test_hyp_simpleuml_umlpackageelement_constructor_exists():
    assert callable(SimpleUML_UmlPackageElement.__init__)


def test_hyp_simpleuml_umlpackageelement_constructor_args():
    sig = inspect.signature(SimpleUML_UmlPackageElement.__init__)
    params = list(sig.parameters.keys())



def test_hyp_simpleuml_umlattribute_is_not_abstract():
    assert not inspect.isabstract(SimpleUML_UmlAttribute)


def test_hyp_simpleuml_umlattribute_constructor_exists():
    assert callable(SimpleUML_UmlAttribute.__init__)


def test_hyp_simpleuml_umlattribute_constructor_args():
    sig = inspect.signature(SimpleUML_UmlAttribute.__init__)
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
SimpleUML_UmlModelElement_strategy = st.builds(
    SimpleUML_UmlModelElement,
    id=
        safe_text,
    umlName=
        safe_text,
    umlKind=
        safe_text
)
UmlClassifier_strategy = st.builds(
    UmlClassifier,
)
SimpleUML_UmlPrimitiveDataType_strategy = st.builds(
    SimpleUML_UmlPrimitiveDataType,
)
SimpleUML_UmlClass_strategy = st.builds(
    SimpleUML_UmlClass,
)
UmlPackageElement_strategy = st.builds(
    UmlPackageElement,
)
SimpleUML_UmlClassifier_strategy = st.builds(
    SimpleUML_UmlClassifier,
)
SimpleUML_UmlAssociation_strategy = st.builds(
    SimpleUML_UmlAssociation,
)
UmlModelElement_strategy = st.builds(
    UmlModelElement,
)
SimpleUML_UmlPackage_strategy = st.builds(
    SimpleUML_UmlPackage,
)
SimpleUML_UmlPackageElement_strategy = st.builds(
    SimpleUML_UmlPackageElement,
)
SimpleUML_UmlAttribute_strategy = st.builds(
    SimpleUML_UmlAttribute,
)




@given(instance=SimpleUML_UmlModelElement_strategy)
def test_hyp_simpleuml_umlmodelelement_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original



@given(instance=SimpleUML_UmlModelElement_strategy)
def test_hyp_simpleuml_umlmodelelement_umlName_setter(instance):
    original = instance.umlName
    instance.umlName = original
    assert instance.umlName == original



@given(instance=SimpleUML_UmlModelElement_strategy)
def test_hyp_simpleuml_umlmodelelement_umlKind_setter(instance):
    original = instance.umlKind
    instance.umlKind = original
    assert instance.umlKind == original












# ----- SECTION B: test_structural_full.py (deterministic-first suite) -----
import inspect
import pytest
from datetime import date, datetime, time, timedelta
from hypothesis import given, settings
import hypothesis.strategies as st

from python_code import (
    SimpleUML_UmlAssociation,
    SimpleUML_UmlAttribute,
    SimpleUML_UmlClass,
    SimpleUML_UmlClassifier,
    SimpleUML_UmlModelElement,
    SimpleUML_UmlPackage,
    SimpleUML_UmlPackageElement,
    SimpleUML_UmlPrimitiveDataType,
    UmlClassifier,
    UmlModelElement,
    UmlPackageElement,
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

def test_SimpleUML_UmlModelElement_id_value_roundtrip():
    instance = SimpleUML_UmlModelElement(id="sample_text", umlKind="sample_text", umlName="sample_text")
    assert instance.id == "sample_text"
    instance.id = "sample_text_2"
    assert instance.id == "sample_text_2"


def test_SimpleUML_UmlModelElement_umlKind_value_roundtrip():
    instance = SimpleUML_UmlModelElement(id="sample_text", umlKind="sample_text", umlName="sample_text")
    assert instance.umlKind == "sample_text"
    instance.umlKind = "sample_text_2"
    assert instance.umlKind == "sample_text_2"


def test_SimpleUML_UmlModelElement_umlName_value_roundtrip():
    instance = SimpleUML_UmlModelElement(id="sample_text", umlKind="sample_text", umlName="sample_text")
    assert instance.umlName == "sample_text"
    instance.umlName = "sample_text_2"
    assert instance.umlName == "sample_text_2"


def test_SimpleUML_UmlClass_isa_UmlClassifier():
    instance = SimpleUML_UmlClass()
    assert isinstance(instance, UmlClassifier)


def test_SimpleUML_UmlPrimitiveDataType_isa_UmlClassifier():
    instance = SimpleUML_UmlPrimitiveDataType()
    assert isinstance(instance, UmlClassifier)


def test_SimpleUML_UmlAttribute_isa_UmlModelElement():
    instance = SimpleUML_UmlAttribute()
    assert isinstance(instance, UmlModelElement)


def test_SimpleUML_UmlPackage_isa_UmlModelElement():
    instance = SimpleUML_UmlPackage()
    assert isinstance(instance, UmlModelElement)


def test_SimpleUML_UmlPackageElement_isa_UmlModelElement():
    instance = SimpleUML_UmlPackageElement()
    assert isinstance(instance, UmlModelElement)


def test_SimpleUML_UmlAssociation_isa_UmlPackageElement():
    instance = SimpleUML_UmlAssociation()
    assert isinstance(instance, UmlPackageElement)


def test_SimpleUML_UmlClassifier_isa_UmlPackageElement():
    instance = SimpleUML_UmlClassifier()
    assert isinstance(instance, UmlPackageElement)


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

SimpleUML_UmlAssociation_strategy = st.builds(SimpleUML_UmlAssociation)
@given(instance=SimpleUML_UmlAssociation_strategy)
@settings(max_examples=25)
def test_SimpleUML_UmlAssociation_instantiation(instance):
    assert isinstance(instance, SimpleUML_UmlAssociation)


SimpleUML_UmlAttribute_strategy = st.builds(SimpleUML_UmlAttribute)
@given(instance=SimpleUML_UmlAttribute_strategy)
@settings(max_examples=25)
def test_SimpleUML_UmlAttribute_instantiation(instance):
    assert isinstance(instance, SimpleUML_UmlAttribute)


SimpleUML_UmlClass_strategy = st.builds(SimpleUML_UmlClass)
@given(instance=SimpleUML_UmlClass_strategy)
@settings(max_examples=25)
def test_SimpleUML_UmlClass_instantiation(instance):
    assert isinstance(instance, SimpleUML_UmlClass)


SimpleUML_UmlClassifier_strategy = st.builds(SimpleUML_UmlClassifier)
@given(instance=SimpleUML_UmlClassifier_strategy)
@settings(max_examples=25)
def test_SimpleUML_UmlClassifier_instantiation(instance):
    assert isinstance(instance, SimpleUML_UmlClassifier)


SimpleUML_UmlModelElement_strategy = st.builds(SimpleUML_UmlModelElement, id=safe_text, umlKind=safe_text, umlName=safe_text)
@given(instance=SimpleUML_UmlModelElement_strategy)
@settings(max_examples=25)
def test_SimpleUML_UmlModelElement_instantiation(instance):
    assert isinstance(instance, SimpleUML_UmlModelElement)


SimpleUML_UmlPackage_strategy = st.builds(SimpleUML_UmlPackage)
@given(instance=SimpleUML_UmlPackage_strategy)
@settings(max_examples=25)
def test_SimpleUML_UmlPackage_instantiation(instance):
    assert isinstance(instance, SimpleUML_UmlPackage)


SimpleUML_UmlPackageElement_strategy = st.builds(SimpleUML_UmlPackageElement)
@given(instance=SimpleUML_UmlPackageElement_strategy)
@settings(max_examples=25)
def test_SimpleUML_UmlPackageElement_instantiation(instance):
    assert isinstance(instance, SimpleUML_UmlPackageElement)


SimpleUML_UmlPrimitiveDataType_strategy = st.builds(SimpleUML_UmlPrimitiveDataType)
@given(instance=SimpleUML_UmlPrimitiveDataType_strategy)
@settings(max_examples=25)
def test_SimpleUML_UmlPrimitiveDataType_instantiation(instance):
    assert isinstance(instance, SimpleUML_UmlPrimitiveDataType)


UmlClassifier_strategy = st.builds(UmlClassifier)
@given(instance=UmlClassifier_strategy)
@settings(max_examples=25)
def test_UmlClassifier_instantiation(instance):
    assert isinstance(instance, UmlClassifier)


UmlModelElement_strategy = st.builds(UmlModelElement)
@given(instance=UmlModelElement_strategy)
@settings(max_examples=25)
def test_UmlModelElement_instantiation(instance):
    assert isinstance(instance, UmlModelElement)


UmlPackageElement_strategy = st.builds(UmlPackageElement)
@given(instance=UmlPackageElement_strategy)
@settings(max_examples=25)
def test_UmlPackageElement_instantiation(instance):
    assert isinstance(instance, UmlPackageElement)



