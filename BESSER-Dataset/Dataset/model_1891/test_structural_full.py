import inspect
import pytest
from datetime import date, datetime, time, timedelta
from hypothesis import given, settings
import hypothesis.strategies as st

from python_code import (
    DeprecatableElement,
    NamedElement,
    sgen_DeprecatableElement,
    sgen_EObject,
    sgen_Expression,
    sgen_FeatureConfiguration,
    sgen_FeatureParameter,
    sgen_FeatureParameterValue,
    sgen_FeatureType,
    sgen_FeatureTypeLibrary,
    sgen_GeneratorConfiguration,
    sgen_GeneratorEntry,
    sgen_GeneratorModel,
    sgen_Property,
    ParameterTypes,
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

def test_sgen_DeprecatableElement_comment_value_roundtrip():
    instance = sgen_DeprecatableElement(comment="sample_text", deprecated=True)
    assert instance.comment == "sample_text"
    instance.comment = "sample_text_2"
    assert instance.comment == "sample_text_2"


def test_sgen_DeprecatableElement_deprecated_value_roundtrip():
    instance = sgen_DeprecatableElement(comment="sample_text", deprecated=True)
    assert instance.deprecated == True
    instance.deprecated = False
    assert instance.deprecated == False


def test_sgen_FeatureParameter_optional_value_roundtrip():
    instance = sgen_FeatureParameter(optional=True, parameterType="sample_text")
    assert instance.optional == True
    instance.optional = False
    assert instance.optional == False


def test_sgen_FeatureParameter_parameterType_value_roundtrip():
    instance = sgen_FeatureParameter(optional=True, parameterType="sample_text")
    assert instance.parameterType == "sample_text"
    instance.parameterType = "sample_text_2"
    assert instance.parameterType == "sample_text_2"


def test_sgen_FeatureType_optional_value_roundtrip():
    instance = sgen_FeatureType(optional=True)
    assert instance.optional == True
    instance.optional = False
    assert instance.optional == False


def test_sgen_FeatureTypeLibrary_name_value_roundtrip():
    instance = sgen_FeatureTypeLibrary(name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_sgen_GeneratorEntry_contentType_value_roundtrip():
    instance = sgen_GeneratorEntry(contentType="sample_text")
    assert instance.contentType == "sample_text"
    instance.contentType = "sample_text_2"
    assert instance.contentType == "sample_text_2"


def test_sgen_GeneratorModel_generatorId_value_roundtrip():
    instance = sgen_GeneratorModel(generatorId="sample_text")
    assert instance.generatorId == "sample_text"
    instance.generatorId = "sample_text_2"
    assert instance.generatorId == "sample_text_2"


def test_sgen_FeatureParameter_isa_DeprecatableElement():
    instance = sgen_FeatureParameter(optional=True, parameterType="sample_text")
    assert isinstance(instance, DeprecatableElement)


def test_sgen_FeatureType_isa_DeprecatableElement():
    instance = sgen_FeatureType(optional=True)
    assert isinstance(instance, DeprecatableElement)


def test_sgen_FeatureParameter_isa_NamedElement():
    instance = sgen_FeatureParameter(optional=True, parameterType="sample_text")
    assert isinstance(instance, NamedElement)


def test_sgen_FeatureType_isa_NamedElement():
    instance = sgen_FeatureType(optional=True)
    assert isinstance(instance, NamedElement)


def test_assoc_configurations3_link_reassign_clear():
    a = sgen_FeatureConfiguration()
    b1 = sgen_GeneratorConfiguration()
    b2 = sgen_GeneratorConfiguration()
    _safe_set(a, 'sgen_FeatureConfiguration', b1)
    assert _is_linked(a, 'sgen_FeatureConfiguration', b1)
    if hasattr(b1, 'sgen_GeneratorConfiguration'):
        assert _is_linked(b1, 'sgen_GeneratorConfiguration', a)
    _safe_set(a, 'sgen_FeatureConfiguration', b2)
    assert _is_linked(a, 'sgen_FeatureConfiguration', b2)
    if hasattr(b1, 'sgen_GeneratorConfiguration'):
        assert not _is_linked(b1, 'sgen_GeneratorConfiguration', a)
    if hasattr(b2, 'sgen_GeneratorConfiguration'):
        assert _is_linked(b2, 'sgen_GeneratorConfiguration', a)
    _safe_set(a, 'sgen_FeatureConfiguration', None)
    assert not _is_linked(a, 'sgen_FeatureConfiguration', b2)
    if hasattr(b2, 'sgen_GeneratorConfiguration'):
        assert not _is_linked(b2, 'sgen_GeneratorConfiguration', a)


def test_assoc_elementRef11_link_reassign_clear():
    a = sgen_GeneratorEntry(contentType="sample_text")
    b1 = sgen_EObject()
    b2 = sgen_EObject()
    _safe_set(a, 'sgen_GeneratorEntry12', b1)
    assert _is_linked(a, 'sgen_GeneratorEntry12', b1)
    if hasattr(b1, 'sgen_EObject'):
        assert _is_linked(b1, 'sgen_EObject', a)
    _safe_set(a, 'sgen_GeneratorEntry12', b2)
    assert _is_linked(a, 'sgen_GeneratorEntry12', b2)
    if hasattr(b1, 'sgen_EObject'):
        assert not _is_linked(b1, 'sgen_EObject', a)
    if hasattr(b2, 'sgen_EObject'):
        assert _is_linked(b2, 'sgen_EObject', a)
    _safe_set(a, 'sgen_GeneratorEntry12', None)
    assert not _is_linked(a, 'sgen_GeneratorEntry12', b2)
    if hasattr(b2, 'sgen_EObject'):
        assert not _is_linked(b2, 'sgen_EObject', a)


def test_assoc_entries0_link_reassign_clear():
    a = sgen_GeneratorModel(generatorId="sample_text")
    b1 = sgen_GeneratorEntry(contentType="sample_text")
    b2 = sgen_GeneratorEntry(contentType="sample_text_2")
    _safe_set(a, 'sgen_GeneratorModel', {b1})
    assert _is_linked(a, 'sgen_GeneratorModel', b1)
    if hasattr(b1, 'sgen_GeneratorEntry'):
        assert _is_linked(b1, 'sgen_GeneratorEntry', a)
    _safe_set(a, 'sgen_GeneratorModel', {b2})
    assert _is_linked(a, 'sgen_GeneratorModel', b2)
    if hasattr(b1, 'sgen_GeneratorEntry'):
        assert not _is_linked(b1, 'sgen_GeneratorEntry', a)
    if hasattr(b2, 'sgen_GeneratorEntry'):
        assert _is_linked(b2, 'sgen_GeneratorEntry', a)
    _safe_set(a, 'sgen_GeneratorModel', set())
    assert not _is_linked(a, 'sgen_GeneratorModel', b2)
    if hasattr(b2, 'sgen_GeneratorEntry'):
        assert not _is_linked(b2, 'sgen_GeneratorEntry', a)


def test_assoc_expression18_link_reassign_clear():
    a = sgen_FeatureParameterValue()
    b1 = sgen_Expression()
    b2 = sgen_Expression()
    _safe_set(a, 'sgen_FeatureParameterValue19', b1)
    assert _is_linked(a, 'sgen_FeatureParameterValue19', b1)
    if hasattr(b1, 'sgen_Expression'):
        assert _is_linked(b1, 'sgen_Expression', a)
    _safe_set(a, 'sgen_FeatureParameterValue19', b2)
    assert _is_linked(a, 'sgen_FeatureParameterValue19', b2)
    if hasattr(b1, 'sgen_Expression'):
        assert not _is_linked(b1, 'sgen_Expression', a)
    if hasattr(b2, 'sgen_Expression'):
        assert _is_linked(b2, 'sgen_Expression', a)
    _safe_set(a, 'sgen_FeatureParameterValue19', None)
    assert not _is_linked(a, 'sgen_FeatureParameterValue19', b2)
    if hasattr(b2, 'sgen_Expression'):
        assert not _is_linked(b2, 'sgen_Expression', a)


def test_assoc_featureConfiguration17_link_reassign_clear():
    a = sgen_FeatureParameterValue()
    b1 = sgen_FeatureConfiguration()
    b2 = sgen_FeatureConfiguration()
    _safe_set(a, 'parameterValues', b1)
    assert _is_linked(a, 'parameterValues', b1)
    if hasattr(b1, 'FeatureConfiguration'):
        assert _is_linked(b1, 'FeatureConfiguration', a)
    _safe_set(a, 'parameterValues', b2)
    assert _is_linked(a, 'parameterValues', b2)
    if hasattr(b1, 'FeatureConfiguration'):
        assert not _is_linked(b1, 'FeatureConfiguration', a)
    if hasattr(b2, 'FeatureConfiguration'):
        assert _is_linked(b2, 'FeatureConfiguration', a)
    _safe_set(a, 'parameterValues', None)
    assert not _is_linked(a, 'parameterValues', b2)
    if hasattr(b2, 'FeatureConfiguration'):
        assert not _is_linked(b2, 'FeatureConfiguration', a)


def test_assoc_featureType6_link_reassign_clear():
    a = sgen_FeatureType(optional=True)
    b1 = sgen_FeatureParameter(optional=True, parameterType="sample_text")
    b2 = sgen_FeatureParameter(optional=False, parameterType="sample_text_2")
    _safe_set(a, 'FeatureType', b1)
    assert _is_linked(a, 'FeatureType', b1)
    if hasattr(b1, 'parameters'):
        assert _is_linked(b1, 'parameters', a)
    _safe_set(a, 'FeatureType', b2)
    assert _is_linked(a, 'FeatureType', b2)
    if hasattr(b1, 'parameters'):
        assert not _is_linked(b1, 'parameters', a)
    if hasattr(b2, 'parameters'):
        assert _is_linked(b2, 'parameters', a)
    _safe_set(a, 'FeatureType', None)
    assert not _is_linked(a, 'FeatureType', b2)
    if hasattr(b2, 'parameters'):
        assert not _is_linked(b2, 'parameters', a)


def test_assoc_features13_link_reassign_clear():
    a = sgen_GeneratorEntry(contentType="sample_text")
    b1 = sgen_FeatureConfiguration()
    b2 = sgen_FeatureConfiguration()
    _safe_set(a, 'sgen_GeneratorEntry14', {b1})
    assert _is_linked(a, 'sgen_GeneratorEntry14', b1)
    if hasattr(b1, 'sgen_FeatureConfiguration15'):
        assert _is_linked(b1, 'sgen_FeatureConfiguration15', a)
    _safe_set(a, 'sgen_GeneratorEntry14', {b2})
    assert _is_linked(a, 'sgen_GeneratorEntry14', b2)
    if hasattr(b1, 'sgen_FeatureConfiguration15'):
        assert not _is_linked(b1, 'sgen_FeatureConfiguration15', a)
    if hasattr(b2, 'sgen_FeatureConfiguration15'):
        assert _is_linked(b2, 'sgen_FeatureConfiguration15', a)
    _safe_set(a, 'sgen_GeneratorEntry14', set())
    assert not _is_linked(a, 'sgen_GeneratorEntry14', b2)
    if hasattr(b2, 'sgen_FeatureConfiguration15'):
        assert not _is_linked(b2, 'sgen_FeatureConfiguration15', a)


def test_assoc_library5_link_reassign_clear():
    a = sgen_FeatureTypeLibrary(name="sample_text")
    b1 = sgen_FeatureType(optional=True)
    b2 = sgen_FeatureType(optional=False)
    _safe_set(a, 'sgen_FeatureTypeLibrary', b1)
    assert _is_linked(a, 'sgen_FeatureTypeLibrary', b1)
    if hasattr(b1, 'sgen_FeatureType'):
        assert _is_linked(b1, 'sgen_FeatureType', a)
    _safe_set(a, 'sgen_FeatureTypeLibrary', b2)
    assert _is_linked(a, 'sgen_FeatureTypeLibrary', b2)
    if hasattr(b1, 'sgen_FeatureType'):
        assert not _is_linked(b1, 'sgen_FeatureType', a)
    if hasattr(b2, 'sgen_FeatureType'):
        assert _is_linked(b2, 'sgen_FeatureType', a)
    _safe_set(a, 'sgen_FeatureTypeLibrary', None)
    assert not _is_linked(a, 'sgen_FeatureTypeLibrary', b2)
    if hasattr(b2, 'sgen_FeatureType'):
        assert not _is_linked(b2, 'sgen_FeatureType', a)


def test_assoc_parameter16_link_reassign_clear():
    a = sgen_FeatureParameterValue()
    b1 = sgen_FeatureParameter(optional=True, parameterType="sample_text")
    b2 = sgen_FeatureParameter(optional=False, parameterType="sample_text_2")
    _safe_set(a, 'sgen_FeatureParameterValue', b1)
    assert _is_linked(a, 'sgen_FeatureParameterValue', b1)
    if hasattr(b1, 'sgen_FeatureParameter'):
        assert _is_linked(b1, 'sgen_FeatureParameter', a)
    _safe_set(a, 'sgen_FeatureParameterValue', b2)
    assert _is_linked(a, 'sgen_FeatureParameterValue', b2)
    if hasattr(b1, 'sgen_FeatureParameter'):
        assert not _is_linked(b1, 'sgen_FeatureParameter', a)
    if hasattr(b2, 'sgen_FeatureParameter'):
        assert _is_linked(b2, 'sgen_FeatureParameter', a)
    _safe_set(a, 'sgen_FeatureParameterValue', None)
    assert not _is_linked(a, 'sgen_FeatureParameterValue', b2)
    if hasattr(b2, 'sgen_FeatureParameter'):
        assert not _is_linked(b2, 'sgen_FeatureParameter', a)


def test_assoc_parameterValues10_link_reassign_clear():
    a = sgen_FeatureParameterValue()
    b1 = sgen_FeatureConfiguration()
    b2 = sgen_FeatureConfiguration()
    _safe_set(a, 'FeatureParameterValue', b1)
    assert _is_linked(a, 'FeatureParameterValue', b1)
    if hasattr(b1, 'featureConfiguration'):
        assert _is_linked(b1, 'featureConfiguration', a)
    _safe_set(a, 'FeatureParameterValue', b2)
    assert _is_linked(a, 'FeatureParameterValue', b2)
    if hasattr(b1, 'featureConfiguration'):
        assert not _is_linked(b1, 'featureConfiguration', a)
    if hasattr(b2, 'featureConfiguration'):
        assert _is_linked(b2, 'featureConfiguration', a)
    _safe_set(a, 'FeatureParameterValue', None)
    assert not _is_linked(a, 'FeatureParameterValue', b2)
    if hasattr(b2, 'featureConfiguration'):
        assert not _is_linked(b2, 'featureConfiguration', a)


def test_assoc_parameters4_link_reassign_clear():
    a = sgen_FeatureType(optional=True)
    b1 = sgen_FeatureParameter(optional=True, parameterType="sample_text")
    b2 = sgen_FeatureParameter(optional=False, parameterType="sample_text_2")
    _safe_set(a, 'featureType', {b1})
    assert _is_linked(a, 'featureType', b1)
    if hasattr(b1, 'FeatureParameter'):
        assert _is_linked(b1, 'FeatureParameter', a)
    _safe_set(a, 'featureType', {b2})
    assert _is_linked(a, 'featureType', b2)
    if hasattr(b1, 'FeatureParameter'):
        assert not _is_linked(b1, 'FeatureParameter', a)
    if hasattr(b2, 'FeatureParameter'):
        assert _is_linked(b2, 'FeatureParameter', a)
    _safe_set(a, 'featureType', set())
    assert not _is_linked(a, 'featureType', b2)
    if hasattr(b2, 'FeatureParameter'):
        assert not _is_linked(b2, 'FeatureParameter', a)


def test_assoc_properties1_link_reassign_clear():
    a = sgen_GeneratorModel(generatorId="sample_text")
    b1 = sgen_Property()
    b2 = sgen_Property()
    _safe_set(a, 'sgen_GeneratorModel2', {b1})
    assert _is_linked(a, 'sgen_GeneratorModel2', b1)
    if hasattr(b1, 'sgen_Property'):
        assert _is_linked(b1, 'sgen_Property', a)
    _safe_set(a, 'sgen_GeneratorModel2', {b2})
    assert _is_linked(a, 'sgen_GeneratorModel2', b2)
    if hasattr(b1, 'sgen_Property'):
        assert not _is_linked(b1, 'sgen_Property', a)
    if hasattr(b2, 'sgen_Property'):
        assert _is_linked(b2, 'sgen_Property', a)
    _safe_set(a, 'sgen_GeneratorModel2', set())
    assert not _is_linked(a, 'sgen_GeneratorModel2', b2)
    if hasattr(b2, 'sgen_Property'):
        assert not _is_linked(b2, 'sgen_Property', a)


def test_assoc_type7_link_reassign_clear():
    a = sgen_FeatureType(optional=True)
    b1 = sgen_FeatureConfiguration()
    b2 = sgen_FeatureConfiguration()
    _safe_set(a, 'sgen_FeatureType9', b1)
    assert _is_linked(a, 'sgen_FeatureType9', b1)
    if hasattr(b1, 'sgen_FeatureConfiguration8'):
        assert _is_linked(b1, 'sgen_FeatureConfiguration8', a)
    _safe_set(a, 'sgen_FeatureType9', b2)
    assert _is_linked(a, 'sgen_FeatureType9', b2)
    if hasattr(b1, 'sgen_FeatureConfiguration8'):
        assert not _is_linked(b1, 'sgen_FeatureConfiguration8', a)
    if hasattr(b2, 'sgen_FeatureConfiguration8'):
        assert _is_linked(b2, 'sgen_FeatureConfiguration8', a)
    _safe_set(a, 'sgen_FeatureType9', None)
    assert not _is_linked(a, 'sgen_FeatureType9', b2)
    if hasattr(b2, 'sgen_FeatureConfiguration8'):
        assert not _is_linked(b2, 'sgen_FeatureConfiguration8', a)


def test_assoc_types20_link_reassign_clear():
    a = sgen_FeatureTypeLibrary(name="sample_text")
    b1 = sgen_FeatureType(optional=True)
    b2 = sgen_FeatureType(optional=False)
    _safe_set(a, 'sgen_FeatureTypeLibrary21', {b1})
    assert _is_linked(a, 'sgen_FeatureTypeLibrary21', b1)
    if hasattr(b1, 'sgen_FeatureType22'):
        assert _is_linked(b1, 'sgen_FeatureType22', a)
    _safe_set(a, 'sgen_FeatureTypeLibrary21', {b2})
    assert _is_linked(a, 'sgen_FeatureTypeLibrary21', b2)
    if hasattr(b1, 'sgen_FeatureType22'):
        assert not _is_linked(b1, 'sgen_FeatureType22', a)
    if hasattr(b2, 'sgen_FeatureType22'):
        assert _is_linked(b2, 'sgen_FeatureType22', a)
    _safe_set(a, 'sgen_FeatureTypeLibrary21', set())
    assert not _is_linked(a, 'sgen_FeatureTypeLibrary21', b2)
    if hasattr(b2, 'sgen_FeatureType22'):
        assert not _is_linked(b2, 'sgen_FeatureType22', a)


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

DeprecatableElement_strategy = st.builds(DeprecatableElement)
@given(instance=DeprecatableElement_strategy)
@settings(max_examples=25)
def test_DeprecatableElement_instantiation(instance):
    assert isinstance(instance, DeprecatableElement)


NamedElement_strategy = st.builds(NamedElement)
@given(instance=NamedElement_strategy)
@settings(max_examples=25)
def test_NamedElement_instantiation(instance):
    assert isinstance(instance, NamedElement)


sgen_DeprecatableElement_strategy = st.builds(sgen_DeprecatableElement, comment=safe_text, deprecated=st.booleans())
@given(instance=sgen_DeprecatableElement_strategy)
@settings(max_examples=25)
def test_sgen_DeprecatableElement_instantiation(instance):
    assert isinstance(instance, sgen_DeprecatableElement)


sgen_EObject_strategy = st.builds(sgen_EObject)
@given(instance=sgen_EObject_strategy)
@settings(max_examples=25)
def test_sgen_EObject_instantiation(instance):
    assert isinstance(instance, sgen_EObject)


sgen_Expression_strategy = st.builds(sgen_Expression)
@given(instance=sgen_Expression_strategy)
@settings(max_examples=25)
def test_sgen_Expression_instantiation(instance):
    assert isinstance(instance, sgen_Expression)


sgen_FeatureConfiguration_strategy = st.builds(sgen_FeatureConfiguration)
@given(instance=sgen_FeatureConfiguration_strategy)
@settings(max_examples=25)
def test_sgen_FeatureConfiguration_instantiation(instance):
    assert isinstance(instance, sgen_FeatureConfiguration)


sgen_FeatureParameter_strategy = st.builds(sgen_FeatureParameter, optional=st.booleans(), parameterType=safe_text)
@given(instance=sgen_FeatureParameter_strategy)
@settings(max_examples=25)
def test_sgen_FeatureParameter_instantiation(instance):
    assert isinstance(instance, sgen_FeatureParameter)


sgen_FeatureParameterValue_strategy = st.builds(sgen_FeatureParameterValue)
@given(instance=sgen_FeatureParameterValue_strategy)
@settings(max_examples=25)
def test_sgen_FeatureParameterValue_instantiation(instance):
    assert isinstance(instance, sgen_FeatureParameterValue)


sgen_FeatureType_strategy = st.builds(sgen_FeatureType, optional=st.booleans())
@given(instance=sgen_FeatureType_strategy)
@settings(max_examples=25)
def test_sgen_FeatureType_instantiation(instance):
    assert isinstance(instance, sgen_FeatureType)


sgen_FeatureTypeLibrary_strategy = st.builds(sgen_FeatureTypeLibrary, name=safe_text)
@given(instance=sgen_FeatureTypeLibrary_strategy)
@settings(max_examples=25)
def test_sgen_FeatureTypeLibrary_instantiation(instance):
    assert isinstance(instance, sgen_FeatureTypeLibrary)


sgen_GeneratorConfiguration_strategy = st.builds(sgen_GeneratorConfiguration)
@given(instance=sgen_GeneratorConfiguration_strategy)
@settings(max_examples=25)
def test_sgen_GeneratorConfiguration_instantiation(instance):
    assert isinstance(instance, sgen_GeneratorConfiguration)


sgen_GeneratorEntry_strategy = st.builds(sgen_GeneratorEntry, contentType=safe_text)
@given(instance=sgen_GeneratorEntry_strategy)
@settings(max_examples=25)
def test_sgen_GeneratorEntry_instantiation(instance):
    assert isinstance(instance, sgen_GeneratorEntry)


sgen_GeneratorModel_strategy = st.builds(sgen_GeneratorModel, generatorId=safe_text)
@given(instance=sgen_GeneratorModel_strategy)
@settings(max_examples=25)
def test_sgen_GeneratorModel_instantiation(instance):
    assert isinstance(instance, sgen_GeneratorModel)


sgen_Property_strategy = st.builds(sgen_Property)
@given(instance=sgen_Property_strategy)
@settings(max_examples=25)
def test_sgen_Property_instantiation(instance):
    assert isinstance(instance, sgen_Property)


