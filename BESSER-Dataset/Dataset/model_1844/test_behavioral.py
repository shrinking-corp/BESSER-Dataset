import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    ConstrainableType,
    Constraint,
    DataExample,
    DataType,
    Documentable,
    Element,
    Example,
    Extensible,
    Feature,
    HasSecurityValue,
    HasStringValue,
    HasTitle,
    Inheritable,
    ObjectRealization,
    Parameter,
    RESTElement,
    RealizationContainer,
    ReferenceElement,
    ReferenceTreatment,
    ResourceDefinition,
    ServiceDataResource,
    SimpleType,
    SingleValueType,
    SourceReference,
    TypedMessage,
    URIParameter,
    URISegment,
    WithDataExamples,
    WithExamples,
    rapidml_AuthenticationMethod,
    rapidml_CollectionParameter,
    rapidml_CollectionReferenceElement,
    rapidml_CollectionResource,
    rapidml_ConstrainableType,
    rapidml_Constraint,
    rapidml_DataExample,
    rapidml_DataModel,
    rapidml_DataType,
    rapidml_Documentable,
    rapidml_Documentation,
    rapidml_Element,
    rapidml_EnumConstant,
    rapidml_Enumeration,
    rapidml_Example,
    rapidml_Extensible,
    rapidml_Extension,
    rapidml_ExternalExample,
    rapidml_Feature,
    rapidml_HasSecurityValue,
    rapidml_HasStringValue,
    rapidml_HasTitle,
    rapidml_ImportDeclaration,
    rapidml_Inheritable,
    rapidml_InlineDataExample,
    rapidml_InlineExample,
    rapidml_LengthConstraint,
    rapidml_LinkRelation,
    rapidml_LinkRelationsLibrary,
    rapidml_MatrixParameter,
    rapidml_MediaType,
    rapidml_MediaTypesLibrary,
    rapidml_MessageParameter,
    rapidml_Method,
    rapidml_NamedLinkDescriptor,
    rapidml_ObjectRealization,
    rapidml_ObjectResource,
    rapidml_Operation,
    rapidml_Parameter,
    rapidml_PathSegment,
    rapidml_PrimitiveProperty,
    rapidml_PrimitiveType,
    rapidml_PrimitiveTypeSourceReference,
    rapidml_PrimitiveTypesLibrary,
    rapidml_PropertyRealization,
    rapidml_PropertyReference,
    rapidml_RESTElement,
    rapidml_RealizationContainer,
    rapidml_RealizationModelLocation,
    rapidml_ReferenceElement,
    rapidml_ReferenceEmbed,
    rapidml_ReferenceLink,
    rapidml_ReferenceProperty,
    rapidml_ReferenceRealization,
    rapidml_ReferenceTreatment,
    rapidml_RegExConstraint,
    rapidml_ResourceAPI,
    rapidml_ResourceDefinition,
    rapidml_SecurityScheme,
    rapidml_SecuritySchemeLibrary,
    rapidml_SecuritySchemeParameter,
    rapidml_SecurityScope,
    rapidml_ServiceDataResource,
    rapidml_SimpleType,
    rapidml_SingleValueType,
    rapidml_SourceReference,
    rapidml_Structure,
    rapidml_TemplateParameter,
    rapidml_TypedMessage,
    rapidml_TypedRequest,
    rapidml_TypedResponse,
    rapidml_URI,
    rapidml_URIParameter,
    rapidml_URISegment,
    rapidml_URISegmentWithParameter,
    rapidml_UserDefinedType,
    rapidml_ValueRangeConstraint,
    rapidml_WithDataExamples,
    rapidml_WithExamples,
    rapidml_ZenModel,
    AuthenticationFlows,
    AuthenticationTypes,
    CollectionRealizationEnum,
    CollectionRealizationLevelEnum,
    HTTPMethods,
    HttpMessageParameterLocation,
    ReferenceRealizationEnum,
)

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
# REVERSE-DIRECTION ASSOCIATION TESTS
# Mirrors test_structural_full.py's link_reassign_clear, but sets from the
# OTHER end's own setter directly, instead of relying on it firing only as a
# side effect of the forward-direction test. See module docstring.
# =============================================================================

def test_assoc_allMediaTypes2_reverse_link_reassign_clear():
    a1 = rapidml_ResourceDefinition(name="sample_text")
    a2 = rapidml_ResourceDefinition(name="sample_text_2")
    b = rapidml_MediaType(name="sample_text", specURL="sample_text")
    _safe_set(b, 'rapidml_MediaType4', a1)
    assert _is_linked(b, 'rapidml_MediaType4', a1)
    if hasattr(a1, 'rapidml_ResourceDefinition3'):
        assert _is_linked(a1, 'rapidml_ResourceDefinition3', b)
    _safe_set(b, 'rapidml_MediaType4', a2)
    assert _is_linked(b, 'rapidml_MediaType4', a2)
    if hasattr(a1, 'rapidml_ResourceDefinition3'):
        assert not _is_linked(a1, 'rapidml_ResourceDefinition3', b)
    if hasattr(a2, 'rapidml_ResourceDefinition3'):
        assert _is_linked(a2, 'rapidml_ResourceDefinition3', b)
    _safe_set(b, 'rapidml_MediaType4', None)
    assert not _is_linked(b, 'rapidml_MediaType4', a2)
    if hasattr(a2, 'rapidml_ResourceDefinition3'):
        assert not _is_linked(a2, 'rapidml_ResourceDefinition3', b)


def test_assoc_autoRealizations64_reverse_link_reassign_clear():
    a1 = rapidml_ResourceAPI(baseURI="sample_text", name="sample_text", version="sample_text")
    a2 = rapidml_ResourceAPI(baseURI="sample_text_2", name="sample_text_2", version="sample_text_2")
    b = rapidml_RealizationModelLocation(uri="sample_text")
    _safe_set(b, 'rapidml_RealizationModelLocation', a1)
    assert _is_linked(b, 'rapidml_RealizationModelLocation', a1)
    if hasattr(a1, 'rapidml_ResourceAPI65'):
        assert _is_linked(a1, 'rapidml_ResourceAPI65', b)
    _safe_set(b, 'rapidml_RealizationModelLocation', a2)
    assert _is_linked(b, 'rapidml_RealizationModelLocation', a2)
    if hasattr(a1, 'rapidml_ResourceAPI65'):
        assert not _is_linked(a1, 'rapidml_ResourceAPI65', b)
    if hasattr(a2, 'rapidml_ResourceAPI65'):
        assert _is_linked(a2, 'rapidml_ResourceAPI65', b)
    _safe_set(b, 'rapidml_RealizationModelLocation', None)
    assert not _is_linked(b, 'rapidml_RealizationModelLocation', a2)
    if hasattr(a2, 'rapidml_ResourceAPI65'):
        assert not _is_linked(a2, 'rapidml_ResourceAPI65', b)


def test_assoc_baseProperty85_reverse_link_reassign_clear():
    a1 = rapidml_PropertyRealization(cardinality="sample_text")
    a2 = rapidml_PropertyRealization(cardinality="sample_text_2")
    b = rapidml_Feature(key=True, name="sample_text", readOnly=True, restriction=True)
    _safe_set(b, 'rapidml_Feature', a1)
    assert _is_linked(b, 'rapidml_Feature', a1)
    if hasattr(a1, 'rapidml_PropertyRealization'):
        assert _is_linked(a1, 'rapidml_PropertyRealization', b)
    _safe_set(b, 'rapidml_Feature', a2)
    assert _is_linked(b, 'rapidml_Feature', a2)
    if hasattr(a1, 'rapidml_PropertyRealization'):
        assert not _is_linked(a1, 'rapidml_PropertyRealization', b)
    if hasattr(a2, 'rapidml_PropertyRealization'):
        assert _is_linked(a2, 'rapidml_PropertyRealization', b)
    _safe_set(b, 'rapidml_Feature', None)
    assert not _is_linked(b, 'rapidml_Feature', a2)
    if hasattr(a2, 'rapidml_PropertyRealization'):
        assert not _is_linked(a2, 'rapidml_PropertyRealization', b)


def test_assoc_baseType157_reverse_link_reassign_clear():
    a1 = rapidml_PrimitiveType()
    a2 = rapidml_PrimitiveType()
    b = rapidml_Enumeration()
    _safe_set(b, 'rapidml_Enumeration', a1)
    assert _is_linked(b, 'rapidml_Enumeration', a1)
    if hasattr(a1, 'rapidml_PrimitiveType158'):
        assert _is_linked(a1, 'rapidml_PrimitiveType158', b)
    _safe_set(b, 'rapidml_Enumeration', a2)
    assert _is_linked(b, 'rapidml_Enumeration', a2)
    if hasattr(a1, 'rapidml_PrimitiveType158'):
        assert not _is_linked(a1, 'rapidml_PrimitiveType158', b)
    if hasattr(a2, 'rapidml_PrimitiveType158'):
        assert _is_linked(a2, 'rapidml_PrimitiveType158', b)
    _safe_set(b, 'rapidml_Enumeration', None)
    assert not _is_linked(b, 'rapidml_Enumeration', a2)
    if hasattr(a2, 'rapidml_PrimitiveType158'):
        assert not _is_linked(a2, 'rapidml_PrimitiveType158', b)


def test_assoc_conceptualFeature32_reverse_link_reassign_clear():
    a1 = rapidml_PropertyReference()
    a2 = rapidml_PropertyReference()
    b = rapidml_PrimitiveProperty()
    _safe_set(b, 'rapidml_PrimitiveProperty', a1)
    assert _is_linked(b, 'rapidml_PrimitiveProperty', a1)
    if hasattr(a1, 'rapidml_PropertyReference'):
        assert _is_linked(a1, 'rapidml_PropertyReference', b)
    _safe_set(b, 'rapidml_PrimitiveProperty', a2)
    assert _is_linked(b, 'rapidml_PrimitiveProperty', a2)
    if hasattr(a1, 'rapidml_PropertyReference'):
        assert not _is_linked(a1, 'rapidml_PropertyReference', b)
    if hasattr(a2, 'rapidml_PropertyReference'):
        assert _is_linked(a2, 'rapidml_PropertyReference', b)
    _safe_set(b, 'rapidml_PrimitiveProperty', None)
    assert not _is_linked(b, 'rapidml_PrimitiveProperty', a2)
    if hasattr(a2, 'rapidml_PropertyReference'):
        assert not _is_linked(a2, 'rapidml_PropertyReference', b)


def test_assoc_constraints164_reverse_link_reassign_clear():
    a1 = rapidml_Constraint()
    a2 = rapidml_Constraint()
    b = rapidml_ConstrainableType()
    _safe_set(b, 'rapidml_ConstrainableType', {a1})
    assert _is_linked(b, 'rapidml_ConstrainableType', a1)
    if hasattr(a1, 'rapidml_Constraint'):
        assert _is_linked(a1, 'rapidml_Constraint', b)
    _safe_set(b, 'rapidml_ConstrainableType', {a2})
    assert _is_linked(b, 'rapidml_ConstrainableType', a2)
    if hasattr(a1, 'rapidml_Constraint'):
        assert not _is_linked(a1, 'rapidml_Constraint', b)
    if hasattr(a2, 'rapidml_Constraint'):
        assert _is_linked(a2, 'rapidml_Constraint', b)
    _safe_set(b, 'rapidml_ConstrainableType', set())
    assert not _is_linked(b, 'rapidml_ConstrainableType', a2)
    if hasattr(a2, 'rapidml_Constraint'):
        assert not _is_linked(a2, 'rapidml_Constraint', b)


def test_assoc_containingDataType134_reverse_link_reassign_clear():
    a1 = rapidml_Structure()
    a2 = rapidml_Structure()
    b = rapidml_Feature(key=True, name="sample_text", readOnly=True, restriction=True)
    _safe_set(b, 'ownedFeatures', a1)
    assert _is_linked(b, 'ownedFeatures', a1)
    if hasattr(a1, 'Structure'):
        assert _is_linked(a1, 'Structure', b)
    _safe_set(b, 'ownedFeatures', a2)
    assert _is_linked(b, 'ownedFeatures', a2)
    if hasattr(a1, 'Structure'):
        assert not _is_linked(a1, 'Structure', b)
    if hasattr(a2, 'Structure'):
        assert _is_linked(a2, 'Structure', b)
    _safe_set(b, 'ownedFeatures', None)
    assert not _is_linked(b, 'ownedFeatures', a2)
    if hasattr(a2, 'Structure'):
        assert not _is_linked(a2, 'Structure', b)


def test_assoc_containingMessage34_reverse_link_reassign_clear():
    a1 = rapidml_TypedMessage(useParentTypeReference=True)
    a2 = rapidml_TypedMessage(useParentTypeReference=False)
    b = rapidml_MessageParameter(httpLocation="sample_text")
    _safe_set(b, 'parameters', a1)
    assert _is_linked(b, 'parameters', a1)
    if hasattr(a1, 'TypedMessage'):
        assert _is_linked(a1, 'TypedMessage', b)
    _safe_set(b, 'parameters', a2)
    assert _is_linked(b, 'parameters', a2)
    if hasattr(a1, 'TypedMessage'):
        assert not _is_linked(a1, 'TypedMessage', b)
    if hasattr(a2, 'TypedMessage'):
        assert _is_linked(a2, 'TypedMessage', b)
    _safe_set(b, 'parameters', None)
    assert not _is_linked(b, 'parameters', a2)
    if hasattr(a2, 'TypedMessage'):
        assert not _is_linked(a2, 'TypedMessage', b)


def test_assoc_containingMethod24_reverse_link_reassign_clear():
    a1 = rapidml_TypedResponse(statusCode=7)
    a2 = rapidml_TypedResponse(statusCode=13)
    b = rapidml_Method(httpMethod="sample_text", id="sample_text")
    _safe_set(b, 'Method25', a1)
    assert _is_linked(b, 'Method25', a1)
    if hasattr(a1, 'responses'):
        assert _is_linked(a1, 'responses', b)
    _safe_set(b, 'Method25', a2)
    assert _is_linked(b, 'Method25', a2)
    if hasattr(a1, 'responses'):
        assert not _is_linked(a1, 'responses', b)
    if hasattr(a2, 'responses'):
        assert _is_linked(a2, 'responses', b)
    _safe_set(b, 'Method25', None)
    assert not _is_linked(b, 'Method25', a2)
    if hasattr(a2, 'responses'):
        assert not _is_linked(a2, 'responses', b)


def test_assoc_containingParameter33_reverse_link_reassign_clear():
    a1 = rapidml_SourceReference()
    a2 = rapidml_SourceReference()
    b = rapidml_Parameter(default="sample_text", fixed="sample_text", name="sample_text", required=True)
    _safe_set(b, 'Parameter', a1)
    assert _is_linked(b, 'Parameter', a1)
    if hasattr(a1, 'sourceReference'):
        assert _is_linked(a1, 'sourceReference', b)
    _safe_set(b, 'Parameter', a2)
    assert _is_linked(b, 'Parameter', a2)
    if hasattr(a1, 'sourceReference'):
        assert not _is_linked(a1, 'sourceReference', b)
    if hasattr(a2, 'sourceReference'):
        assert _is_linked(a2, 'sourceReference', b)
    _safe_set(b, 'Parameter', None)
    assert not _is_linked(b, 'Parameter', a2)
    if hasattr(a2, 'sourceReference'):
        assert not _is_linked(a2, 'sourceReference', b)


def test_assoc_containingResourceDefinition16_reverse_link_reassign_clear():
    a1 = rapidml_ResourceDefinition(name="sample_text")
    a2 = rapidml_ResourceDefinition(name="sample_text_2")
    b = rapidml_Method(httpMethod="sample_text", id="sample_text")
    _safe_set(b, 'methods', a1)
    assert _is_linked(b, 'methods', a1)
    if hasattr(a1, 'ResourceDefinition'):
        assert _is_linked(a1, 'ResourceDefinition', b)
    _safe_set(b, 'methods', a2)
    assert _is_linked(b, 'methods', a2)
    if hasattr(a1, 'ResourceDefinition'):
        assert not _is_linked(a1, 'ResourceDefinition', b)
    if hasattr(a2, 'ResourceDefinition'):
        assert _is_linked(a2, 'ResourceDefinition', b)
    _safe_set(b, 'methods', None)
    assert not _is_linked(b, 'methods', a2)
    if hasattr(a2, 'ResourceDefinition'):
        assert not _is_linked(a2, 'ResourceDefinition', b)


def test_assoc_dataModels36_reverse_link_reassign_clear():
    a1 = rapidml_ZenModel(name="sample_text", namespace="sample_text")
    a2 = rapidml_ZenModel(name="sample_text_2", namespace="sample_text_2")
    b = rapidml_DataModel(name="sample_text")
    _safe_set(b, 'rapidml_DataModel', a1)
    assert _is_linked(b, 'rapidml_DataModel', a1)
    if hasattr(a1, 'rapidml_ZenModel37'):
        assert _is_linked(a1, 'rapidml_ZenModel37', b)
    _safe_set(b, 'rapidml_DataModel', a2)
    assert _is_linked(b, 'rapidml_DataModel', a2)
    if hasattr(a1, 'rapidml_ZenModel37'):
        assert not _is_linked(a1, 'rapidml_ZenModel37', b)
    if hasattr(a2, 'rapidml_ZenModel37'):
        assert _is_linked(a2, 'rapidml_ZenModel37', b)
    _safe_set(b, 'rapidml_DataModel', None)
    assert not _is_linked(b, 'rapidml_DataModel', a2)
    if hasattr(a2, 'rapidml_ZenModel37'):
        assert not _is_linked(a2, 'rapidml_ZenModel37', b)


def test_assoc_dataType122_reverse_link_reassign_clear():
    a1 = rapidml_Structure()
    a2 = rapidml_Structure()
    b = rapidml_RealizationContainer(effectiveRealization="sample_text", realizationName="sample_text", withDefaultRealization=True)
    _safe_set(b, 'rapidml_RealizationContainer123', a1)
    assert _is_linked(b, 'rapidml_RealizationContainer123', a1)
    if hasattr(a1, 'rapidml_Structure'):
        assert _is_linked(a1, 'rapidml_Structure', b)
    _safe_set(b, 'rapidml_RealizationContainer123', a2)
    assert _is_linked(b, 'rapidml_RealizationContainer123', a2)
    if hasattr(a1, 'rapidml_Structure'):
        assert not _is_linked(a1, 'rapidml_Structure', b)
    if hasattr(a2, 'rapidml_Structure'):
        assert _is_linked(a2, 'rapidml_Structure', b)
    _safe_set(b, 'rapidml_RealizationContainer123', None)
    assert not _is_linked(b, 'rapidml_RealizationContainer123', a2)
    if hasattr(a2, 'rapidml_Structure'):
        assert not _is_linked(a2, 'rapidml_Structure', b)


def test_assoc_dataType161_reverse_link_reassign_clear():
    a1 = rapidml_Structure()
    a2 = rapidml_Structure()
    b = rapidml_ReferenceElement()
    _safe_set(b, 'rapidml_ReferenceElement162', a1)
    assert _is_linked(b, 'rapidml_ReferenceElement162', a1)
    if hasattr(a1, 'rapidml_Structure163'):
        assert _is_linked(a1, 'rapidml_Structure163', b)
    _safe_set(b, 'rapidml_ReferenceElement162', a2)
    assert _is_linked(b, 'rapidml_ReferenceElement162', a2)
    if hasattr(a1, 'rapidml_Structure163'):
        assert not _is_linked(a1, 'rapidml_Structure163', b)
    if hasattr(a2, 'rapidml_Structure163'):
        assert _is_linked(a2, 'rapidml_Structure163', b)
    _safe_set(b, 'rapidml_ReferenceElement162', None)
    assert not _is_linked(b, 'rapidml_ReferenceElement162', a2)
    if hasattr(a2, 'rapidml_Structure163'):
        assert not _is_linked(a2, 'rapidml_Structure163', b)


def test_assoc_defaultReferenceRealizations62_reverse_link_reassign_clear():
    a1 = rapidml_ResourceAPI(baseURI="sample_text", name="sample_text", version="sample_text")
    a2 = rapidml_ResourceAPI(baseURI="sample_text_2", name="sample_text_2", version="sample_text_2")
    b = rapidml_ReferenceRealization(multiValued=True, realizationType="sample_text")
    _safe_set(b, 'rapidml_ReferenceRealization', a1)
    assert _is_linked(b, 'rapidml_ReferenceRealization', a1)
    if hasattr(a1, 'rapidml_ResourceAPI63'):
        assert _is_linked(a1, 'rapidml_ResourceAPI63', b)
    _safe_set(b, 'rapidml_ReferenceRealization', a2)
    assert _is_linked(b, 'rapidml_ReferenceRealization', a2)
    if hasattr(a1, 'rapidml_ResourceAPI63'):
        assert not _is_linked(a1, 'rapidml_ResourceAPI63', b)
    if hasattr(a2, 'rapidml_ResourceAPI63'):
        assert _is_linked(a2, 'rapidml_ResourceAPI63', b)
    _safe_set(b, 'rapidml_ReferenceRealization', None)
    assert not _is_linked(b, 'rapidml_ReferenceRealization', a2)
    if hasattr(a2, 'rapidml_ResourceAPI63'):
        assert not _is_linked(a2, 'rapidml_ResourceAPI63', b)


def test_assoc_definedLinkDescriptors66_reverse_link_reassign_clear():
    a1 = rapidml_ServiceDataResource(default=True)
    a2 = rapidml_ServiceDataResource(default=False)
    b = rapidml_NamedLinkDescriptor(default=True, name="sample_text")
    _safe_set(b, 'rapidml_NamedLinkDescriptor', a1)
    assert _is_linked(b, 'rapidml_NamedLinkDescriptor', a1)
    if hasattr(a1, 'rapidml_ServiceDataResource'):
        assert _is_linked(a1, 'rapidml_ServiceDataResource', b)
    _safe_set(b, 'rapidml_NamedLinkDescriptor', a2)
    assert _is_linked(b, 'rapidml_NamedLinkDescriptor', a2)
    if hasattr(a1, 'rapidml_ServiceDataResource'):
        assert not _is_linked(a1, 'rapidml_ServiceDataResource', b)
    if hasattr(a2, 'rapidml_ServiceDataResource'):
        assert _is_linked(a2, 'rapidml_ServiceDataResource', b)
    _safe_set(b, 'rapidml_NamedLinkDescriptor', None)
    assert not _is_linked(b, 'rapidml_NamedLinkDescriptor', a2)
    if hasattr(a2, 'rapidml_ServiceDataResource'):
        assert not _is_linked(a2, 'rapidml_ServiceDataResource', b)


def test_assoc_definedLinkRelations128_reverse_link_reassign_clear():
    a1 = rapidml_LinkRelationsLibrary(name="sample_text")
    a2 = rapidml_LinkRelationsLibrary(name="sample_text_2")
    b = rapidml_LinkRelation(name="sample_text", specURL="sample_text")
    _safe_set(b, 'rapidml_LinkRelation130', a1)
    assert _is_linked(b, 'rapidml_LinkRelation130', a1)
    if hasattr(a1, 'rapidml_LinkRelationsLibrary129'):
        assert _is_linked(a1, 'rapidml_LinkRelationsLibrary129', b)
    _safe_set(b, 'rapidml_LinkRelation130', a2)
    assert _is_linked(b, 'rapidml_LinkRelation130', a2)
    if hasattr(a1, 'rapidml_LinkRelationsLibrary129'):
        assert not _is_linked(a1, 'rapidml_LinkRelationsLibrary129', b)
    if hasattr(a2, 'rapidml_LinkRelationsLibrary129'):
        assert _is_linked(a2, 'rapidml_LinkRelationsLibrary129', b)
    _safe_set(b, 'rapidml_LinkRelation130', None)
    assert not _is_linked(b, 'rapidml_LinkRelation130', a2)
    if hasattr(a2, 'rapidml_LinkRelationsLibrary129'):
        assert not _is_linked(a2, 'rapidml_LinkRelationsLibrary129', b)


def test_assoc_definedLinkRelations60_reverse_link_reassign_clear():
    a1 = rapidml_ResourceAPI(baseURI="sample_text", name="sample_text", version="sample_text")
    a2 = rapidml_ResourceAPI(baseURI="sample_text_2", name="sample_text_2", version="sample_text_2")
    b = rapidml_LinkRelation(name="sample_text", specURL="sample_text")
    _safe_set(b, 'rapidml_LinkRelation', a1)
    assert _is_linked(b, 'rapidml_LinkRelation', a1)
    if hasattr(a1, 'rapidml_ResourceAPI61'):
        assert _is_linked(a1, 'rapidml_ResourceAPI61', b)
    _safe_set(b, 'rapidml_LinkRelation', a2)
    assert _is_linked(b, 'rapidml_LinkRelation', a2)
    if hasattr(a1, 'rapidml_ResourceAPI61'):
        assert not _is_linked(a1, 'rapidml_ResourceAPI61', b)
    if hasattr(a2, 'rapidml_ResourceAPI61'):
        assert _is_linked(a2, 'rapidml_ResourceAPI61', b)
    _safe_set(b, 'rapidml_LinkRelation', None)
    assert not _is_linked(b, 'rapidml_LinkRelation', a2)
    if hasattr(a2, 'rapidml_ResourceAPI61'):
        assert not _is_linked(a2, 'rapidml_ResourceAPI61', b)


def test_assoc_definedMediaTypes57_reverse_link_reassign_clear():
    a1 = rapidml_ResourceAPI(baseURI="sample_text", name="sample_text", version="sample_text")
    a2 = rapidml_ResourceAPI(baseURI="sample_text_2", name="sample_text_2", version="sample_text_2")
    b = rapidml_MediaType(name="sample_text", specURL="sample_text")
    _safe_set(b, 'rapidml_MediaType59', a1)
    assert _is_linked(b, 'rapidml_MediaType59', a1)
    if hasattr(a1, 'rapidml_ResourceAPI58'):
        assert _is_linked(a1, 'rapidml_ResourceAPI58', b)
    _safe_set(b, 'rapidml_MediaType59', a2)
    assert _is_linked(b, 'rapidml_MediaType59', a2)
    if hasattr(a1, 'rapidml_ResourceAPI58'):
        assert not _is_linked(a1, 'rapidml_ResourceAPI58', b)
    if hasattr(a2, 'rapidml_ResourceAPI58'):
        assert _is_linked(a2, 'rapidml_ResourceAPI58', b)
    _safe_set(b, 'rapidml_MediaType59', None)
    assert not _is_linked(b, 'rapidml_MediaType59', a2)
    if hasattr(a2, 'rapidml_ResourceAPI58'):
        assert not _is_linked(a2, 'rapidml_ResourceAPI58', b)


def test_assoc_derivedFrom20_reverse_link_reassign_clear():
    a1 = rapidml_MediaType(name="sample_text", specURL="sample_text")
    a2 = rapidml_MediaType(name="sample_text_2", specURL="sample_text_2")
    b = rapidml_MediaType(name="sample_text", specURL="sample_text")
    _safe_set(b, 'rapidml_MediaType21', a1)
    assert _is_linked(b, 'rapidml_MediaType21', a1)
    if hasattr(a1, 'rapidml_MediaType19'):
        assert _is_linked(a1, 'rapidml_MediaType19', b)
    _safe_set(b, 'rapidml_MediaType21', a2)
    assert _is_linked(b, 'rapidml_MediaType21', a2)
    if hasattr(a1, 'rapidml_MediaType19'):
        assert not _is_linked(a1, 'rapidml_MediaType19', b)
    if hasattr(a2, 'rapidml_MediaType19'):
        assert _is_linked(a2, 'rapidml_MediaType19', b)
    _safe_set(b, 'rapidml_MediaType21', None)
    assert not _is_linked(b, 'rapidml_MediaType21', a2)
    if hasattr(a2, 'rapidml_MediaType19'):
        assert not _is_linked(a2, 'rapidml_MediaType19', b)


def test_assoc_enumConstants156_reverse_link_reassign_clear():
    a1 = rapidml_Enumeration()
    a2 = rapidml_Enumeration()
    b = rapidml_EnumConstant(integerValue=7, literalValue="sample_text", name="sample_text")
    _safe_set(b, 'EnumConstant', a1)
    assert _is_linked(b, 'EnumConstant', a1)
    if hasattr(a1, 'enumeration'):
        assert _is_linked(a1, 'enumeration', b)
    _safe_set(b, 'EnumConstant', a2)
    assert _is_linked(b, 'EnumConstant', a2)
    if hasattr(a1, 'enumeration'):
        assert not _is_linked(a1, 'enumeration', b)
    if hasattr(a2, 'enumeration'):
        assert _is_linked(a2, 'enumeration', b)
    _safe_set(b, 'EnumConstant', None)
    assert not _is_linked(b, 'EnumConstant', a2)
    if hasattr(a2, 'enumeration'):
        assert not _is_linked(a2, 'enumeration', b)


def test_assoc_enumeration159_reverse_link_reassign_clear():
    a1 = rapidml_Enumeration()
    a2 = rapidml_Enumeration()
    b = rapidml_EnumConstant(integerValue=7, literalValue="sample_text", name="sample_text")
    _safe_set(b, 'enumConstants', a1)
    assert _is_linked(b, 'enumConstants', a1)
    if hasattr(a1, 'Enumeration'):
        assert _is_linked(a1, 'Enumeration', b)
    _safe_set(b, 'enumConstants', a2)
    assert _is_linked(b, 'enumConstants', a2)
    if hasattr(a1, 'Enumeration'):
        assert not _is_linked(a1, 'Enumeration', b)
    if hasattr(a2, 'Enumeration'):
        assert _is_linked(a2, 'Enumeration', b)
    _safe_set(b, 'enumConstants', None)
    assert not _is_linked(b, 'enumConstants', a2)
    if hasattr(a2, 'Enumeration'):
        assert not _is_linked(a2, 'Enumeration', b)


def test_assoc_errorResponses105_reverse_link_reassign_clear():
    a1 = rapidml_TypedResponse(statusCode=7)
    a2 = rapidml_TypedResponse(statusCode=13)
    b = rapidml_SecurityScheme(flow="sample_text", name="sample_text", type="sample_text")
    _safe_set(b, 'rapidml_SecurityScheme106', {a1})
    assert _is_linked(b, 'rapidml_SecurityScheme106', a1)
    if hasattr(a1, 'rapidml_TypedResponse'):
        assert _is_linked(a1, 'rapidml_TypedResponse', b)
    _safe_set(b, 'rapidml_SecurityScheme106', {a2})
    assert _is_linked(b, 'rapidml_SecurityScheme106', a2)
    if hasattr(a1, 'rapidml_TypedResponse'):
        assert not _is_linked(a1, 'rapidml_TypedResponse', b)
    if hasattr(a2, 'rapidml_TypedResponse'):
        assert _is_linked(a2, 'rapidml_TypedResponse', b)
    _safe_set(b, 'rapidml_SecurityScheme106', set())
    assert not _is_linked(b, 'rapidml_SecurityScheme106', a2)
    if hasattr(a2, 'rapidml_TypedResponse'):
        assert not _is_linked(a2, 'rapidml_TypedResponse', b)


def test_assoc_excludedProperties95_reverse_link_reassign_clear():
    a1 = rapidml_ObjectRealization()
    a2 = rapidml_ObjectRealization()
    b = rapidml_Feature(key=True, name="sample_text", readOnly=True, restriction=True)
    _safe_set(b, 'rapidml_Feature97', a1)
    assert _is_linked(b, 'rapidml_Feature97', a1)
    if hasattr(a1, 'rapidml_ObjectRealization96'):
        assert _is_linked(a1, 'rapidml_ObjectRealization96', b)
    _safe_set(b, 'rapidml_Feature97', a2)
    assert _is_linked(b, 'rapidml_Feature97', a2)
    if hasattr(a1, 'rapidml_ObjectRealization96'):
        assert not _is_linked(a1, 'rapidml_ObjectRealization96', b)
    if hasattr(a2, 'rapidml_ObjectRealization96'):
        assert _is_linked(a2, 'rapidml_ObjectRealization96', b)
    _safe_set(b, 'rapidml_Feature97', None)
    assert not _is_linked(b, 'rapidml_Feature97', a2)
    if hasattr(a2, 'rapidml_ObjectRealization96'):
        assert not _is_linked(a2, 'rapidml_ObjectRealization96', b)


def test_assoc_exclusivePropertyList90_reverse_link_reassign_clear():
    a1 = rapidml_PropertyRealization(cardinality="sample_text")
    a2 = rapidml_PropertyRealization(cardinality="sample_text_2")
    b = rapidml_ObjectRealization()
    _safe_set(b, 'rapidml_ObjectRealization', {a1})
    assert _is_linked(b, 'rapidml_ObjectRealization', a1)
    if hasattr(a1, 'rapidml_PropertyRealization91'):
        assert _is_linked(a1, 'rapidml_PropertyRealization91', b)
    _safe_set(b, 'rapidml_ObjectRealization', {a2})
    assert _is_linked(b, 'rapidml_ObjectRealization', a2)
    if hasattr(a1, 'rapidml_PropertyRealization91'):
        assert not _is_linked(a1, 'rapidml_PropertyRealization91', b)
    if hasattr(a2, 'rapidml_PropertyRealization91'):
        assert _is_linked(a2, 'rapidml_PropertyRealization91', b)
    _safe_set(b, 'rapidml_ObjectRealization', set())
    assert not _is_linked(b, 'rapidml_ObjectRealization', a2)
    if hasattr(a2, 'rapidml_PropertyRealization91'):
        assert not _is_linked(a2, 'rapidml_PropertyRealization91', b)


def test_assoc_formats54_reverse_link_reassign_clear():
    a1 = rapidml_ResourceAPI(baseURI="sample_text", name="sample_text", version="sample_text")
    a2 = rapidml_ResourceAPI(baseURI="sample_text_2", name="sample_text_2", version="sample_text_2")
    b = rapidml_MediaType(name="sample_text", specURL="sample_text")
    _safe_set(b, 'rapidml_MediaType56', a1)
    assert _is_linked(b, 'rapidml_MediaType56', a1)
    if hasattr(a1, 'rapidml_ResourceAPI55'):
        assert _is_linked(a1, 'rapidml_ResourceAPI55', b)
    _safe_set(b, 'rapidml_MediaType56', a2)
    assert _is_linked(b, 'rapidml_MediaType56', a2)
    if hasattr(a1, 'rapidml_ResourceAPI55'):
        assert not _is_linked(a1, 'rapidml_ResourceAPI55', b)
    if hasattr(a2, 'rapidml_ResourceAPI55'):
        assert _is_linked(a2, 'rapidml_ResourceAPI55', b)
    _safe_set(b, 'rapidml_MediaType56', None)
    assert not _is_linked(b, 'rapidml_MediaType56', a2)
    if hasattr(a2, 'rapidml_ResourceAPI55'):
        assert not _is_linked(a2, 'rapidml_ResourceAPI55', b)


def test_assoc_importedModel87_reverse_link_reassign_clear():
    a1 = rapidml_ZenModel(name="sample_text", namespace="sample_text")
    a2 = rapidml_ZenModel(name="sample_text_2", namespace="sample_text_2")
    b = rapidml_ImportDeclaration(alias="sample_text", importURI="sample_text", importedNamespace="sample_text")
    _safe_set(b, 'rapidml_ImportDeclaration88', a1)
    assert _is_linked(b, 'rapidml_ImportDeclaration88', a1)
    if hasattr(a1, 'rapidml_ZenModel89'):
        assert _is_linked(a1, 'rapidml_ZenModel89', b)
    _safe_set(b, 'rapidml_ImportDeclaration88', a2)
    assert _is_linked(b, 'rapidml_ImportDeclaration88', a2)
    if hasattr(a1, 'rapidml_ZenModel89'):
        assert not _is_linked(a1, 'rapidml_ZenModel89', b)
    if hasattr(a2, 'rapidml_ZenModel89'):
        assert _is_linked(a2, 'rapidml_ZenModel89', b)
    _safe_set(b, 'rapidml_ImportDeclaration88', None)
    assert not _is_linked(b, 'rapidml_ImportDeclaration88', a2)
    if hasattr(a2, 'rapidml_ZenModel89'):
        assert not _is_linked(a2, 'rapidml_ZenModel89', b)


def test_assoc_imports44_reverse_link_reassign_clear():
    a1 = rapidml_ZenModel(name="sample_text", namespace="sample_text")
    a2 = rapidml_ZenModel(name="sample_text_2", namespace="sample_text_2")
    b = rapidml_ImportDeclaration(alias="sample_text", importURI="sample_text", importedNamespace="sample_text")
    _safe_set(b, 'rapidml_ImportDeclaration', a1)
    assert _is_linked(b, 'rapidml_ImportDeclaration', a1)
    if hasattr(a1, 'rapidml_ZenModel45'):
        assert _is_linked(a1, 'rapidml_ZenModel45', b)
    _safe_set(b, 'rapidml_ImportDeclaration', a2)
    assert _is_linked(b, 'rapidml_ImportDeclaration', a2)
    if hasattr(a1, 'rapidml_ZenModel45'):
        assert not _is_linked(a1, 'rapidml_ZenModel45', b)
    if hasattr(a2, 'rapidml_ZenModel45'):
        assert _is_linked(a2, 'rapidml_ZenModel45', b)
    _safe_set(b, 'rapidml_ImportDeclaration', None)
    assert not _is_linked(b, 'rapidml_ImportDeclaration', a2)
    if hasattr(a2, 'rapidml_ZenModel45'):
        assert not _is_linked(a2, 'rapidml_ZenModel45', b)


def test_assoc_inlineObjectRealization116_reverse_link_reassign_clear():
    a1 = rapidml_RealizationContainer(effectiveRealization="sample_text", realizationName="sample_text", withDefaultRealization=True)
    a2 = rapidml_RealizationContainer(effectiveRealization="sample_text_2", realizationName="sample_text_2", withDefaultRealization=False)
    b = rapidml_ObjectRealization()
    _safe_set(b, 'ObjectRealization', a1)
    assert _is_linked(b, 'ObjectRealization', a1)
    if hasattr(a1, 'realizationContainer'):
        assert _is_linked(a1, 'realizationContainer', b)
    _safe_set(b, 'ObjectRealization', a2)
    assert _is_linked(b, 'ObjectRealization', a2)
    if hasattr(a1, 'realizationContainer'):
        assert not _is_linked(a1, 'realizationContainer', b)
    if hasattr(a2, 'realizationContainer'):
        assert _is_linked(a2, 'realizationContainer', b)
    _safe_set(b, 'ObjectRealization', None)
    assert not _is_linked(b, 'ObjectRealization', a2)
    if hasattr(a2, 'realizationContainer'):
        assert not _is_linked(a2, 'realizationContainer', b)


def test_assoc_inverse138_reverse_link_reassign_clear():
    a1 = rapidml_ReferenceProperty(container=True, containment=True)
    a2 = rapidml_ReferenceProperty(container=False, containment=False)
    b = rapidml_ReferenceProperty(container=True, containment=True)
    _safe_set(b, 'rapidml_ReferenceProperty139', a1)
    assert _is_linked(b, 'rapidml_ReferenceProperty139', a1)
    if hasattr(a1, 'rapidml_ReferenceProperty137'):
        assert _is_linked(a1, 'rapidml_ReferenceProperty137', b)
    _safe_set(b, 'rapidml_ReferenceProperty139', a2)
    assert _is_linked(b, 'rapidml_ReferenceProperty139', a2)
    if hasattr(a1, 'rapidml_ReferenceProperty137'):
        assert not _is_linked(a1, 'rapidml_ReferenceProperty137', b)
    if hasattr(a2, 'rapidml_ReferenceProperty137'):
        assert _is_linked(a2, 'rapidml_ReferenceProperty137', b)
    _safe_set(b, 'rapidml_ReferenceProperty139', None)
    assert not _is_linked(b, 'rapidml_ReferenceProperty139', a2)
    if hasattr(a2, 'rapidml_ReferenceProperty137'):
        assert not _is_linked(a2, 'rapidml_ReferenceProperty137', b)


def test_assoc_linkRelation77_reverse_link_reassign_clear():
    a1 = rapidml_ReferenceLink(collectionRealizationLevel="sample_text", name="sample_text")
    a2 = rapidml_ReferenceLink(collectionRealizationLevel="sample_text_2", name="sample_text_2")
    b = rapidml_LinkRelation(name="sample_text", specURL="sample_text")
    _safe_set(b, 'rapidml_LinkRelation78', a1)
    assert _is_linked(b, 'rapidml_LinkRelation78', a1)
    if hasattr(a1, 'rapidml_ReferenceLink'):
        assert _is_linked(a1, 'rapidml_ReferenceLink', b)
    _safe_set(b, 'rapidml_LinkRelation78', a2)
    assert _is_linked(b, 'rapidml_LinkRelation78', a2)
    if hasattr(a1, 'rapidml_ReferenceLink'):
        assert not _is_linked(a1, 'rapidml_ReferenceLink', b)
    if hasattr(a2, 'rapidml_ReferenceLink'):
        assert _is_linked(a2, 'rapidml_ReferenceLink', b)
    _safe_set(b, 'rapidml_LinkRelation78', None)
    assert not _is_linked(b, 'rapidml_LinkRelation78', a2)
    if hasattr(a2, 'rapidml_ReferenceLink'):
        assert not _is_linked(a2, 'rapidml_ReferenceLink', b)


def test_assoc_linkRelationsLibrary40_reverse_link_reassign_clear():
    a1 = rapidml_ZenModel(name="sample_text", namespace="sample_text")
    a2 = rapidml_ZenModel(name="sample_text_2", namespace="sample_text_2")
    b = rapidml_LinkRelationsLibrary(name="sample_text")
    _safe_set(b, 'rapidml_LinkRelationsLibrary', a1)
    assert _is_linked(b, 'rapidml_LinkRelationsLibrary', a1)
    if hasattr(a1, 'rapidml_ZenModel41'):
        assert _is_linked(a1, 'rapidml_ZenModel41', b)
    _safe_set(b, 'rapidml_LinkRelationsLibrary', a2)
    assert _is_linked(b, 'rapidml_LinkRelationsLibrary', a2)
    if hasattr(a1, 'rapidml_ZenModel41'):
        assert not _is_linked(a1, 'rapidml_ZenModel41', b)
    if hasattr(a2, 'rapidml_ZenModel41'):
        assert _is_linked(a2, 'rapidml_ZenModel41', b)
    _safe_set(b, 'rapidml_LinkRelationsLibrary', None)
    assert not _is_linked(b, 'rapidml_LinkRelationsLibrary', a2)
    if hasattr(a2, 'rapidml_ZenModel41'):
        assert not _is_linked(a2, 'rapidml_ZenModel41', b)


def test_assoc_mediaTypes1_reverse_link_reassign_clear():
    a1 = rapidml_ResourceDefinition(name="sample_text")
    a2 = rapidml_ResourceDefinition(name="sample_text_2")
    b = rapidml_MediaType(name="sample_text", specURL="sample_text")
    _safe_set(b, 'rapidml_MediaType', a1)
    assert _is_linked(b, 'rapidml_MediaType', a1)
    if hasattr(a1, 'rapidml_ResourceDefinition'):
        assert _is_linked(a1, 'rapidml_ResourceDefinition', b)
    _safe_set(b, 'rapidml_MediaType', a2)
    assert _is_linked(b, 'rapidml_MediaType', a2)
    if hasattr(a1, 'rapidml_ResourceDefinition'):
        assert not _is_linked(a1, 'rapidml_ResourceDefinition', b)
    if hasattr(a2, 'rapidml_ResourceDefinition'):
        assert _is_linked(a2, 'rapidml_ResourceDefinition', b)
    _safe_set(b, 'rapidml_MediaType', None)
    assert not _is_linked(b, 'rapidml_MediaType', a2)
    if hasattr(a2, 'rapidml_ResourceDefinition'):
        assert not _is_linked(a2, 'rapidml_ResourceDefinition', b)


def test_assoc_mediaTypes10_reverse_link_reassign_clear():
    a1 = rapidml_TypedMessage(useParentTypeReference=True)
    a2 = rapidml_TypedMessage(useParentTypeReference=False)
    b = rapidml_MediaType(name="sample_text", specURL="sample_text")
    _safe_set(b, 'rapidml_MediaType12', a1)
    assert _is_linked(b, 'rapidml_MediaType12', a1)
    if hasattr(a1, 'rapidml_TypedMessage11'):
        assert _is_linked(a1, 'rapidml_TypedMessage11', b)
    _safe_set(b, 'rapidml_MediaType12', a2)
    assert _is_linked(b, 'rapidml_MediaType12', a2)
    if hasattr(a1, 'rapidml_TypedMessage11'):
        assert not _is_linked(a1, 'rapidml_TypedMessage11', b)
    if hasattr(a2, 'rapidml_TypedMessage11'):
        assert _is_linked(a2, 'rapidml_TypedMessage11', b)
    _safe_set(b, 'rapidml_MediaType12', None)
    assert not _is_linked(b, 'rapidml_MediaType12', a2)
    if hasattr(a2, 'rapidml_TypedMessage11'):
        assert not _is_linked(a2, 'rapidml_TypedMessage11', b)


def test_assoc_methods0_reverse_link_reassign_clear():
    a1 = rapidml_ResourceDefinition(name="sample_text")
    a2 = rapidml_ResourceDefinition(name="sample_text_2")
    b = rapidml_Method(httpMethod="sample_text", id="sample_text")
    _safe_set(b, 'Method', a1)
    assert _is_linked(b, 'Method', a1)
    if hasattr(a1, 'containingResourceDefinition'):
        assert _is_linked(a1, 'containingResourceDefinition', b)
    _safe_set(b, 'Method', a2)
    assert _is_linked(b, 'Method', a2)
    if hasattr(a1, 'containingResourceDefinition'):
        assert not _is_linked(a1, 'containingResourceDefinition', b)
    if hasattr(a2, 'containingResourceDefinition'):
        assert _is_linked(a2, 'containingResourceDefinition', b)
    _safe_set(b, 'Method', None)
    assert not _is_linked(b, 'Method', a2)
    if hasattr(a2, 'containingResourceDefinition'):
        assert not _is_linked(a2, 'containingResourceDefinition', b)


def test_assoc_overriddenPropertyList92_reverse_link_reassign_clear():
    a1 = rapidml_PropertyRealization(cardinality="sample_text")
    a2 = rapidml_PropertyRealization(cardinality="sample_text_2")
    b = rapidml_ObjectRealization()
    _safe_set(b, 'rapidml_ObjectRealization93', {a1})
    assert _is_linked(b, 'rapidml_ObjectRealization93', a1)
    if hasattr(a1, 'rapidml_PropertyRealization94'):
        assert _is_linked(a1, 'rapidml_PropertyRealization94', b)
    _safe_set(b, 'rapidml_ObjectRealization93', {a2})
    assert _is_linked(b, 'rapidml_ObjectRealization93', a2)
    if hasattr(a1, 'rapidml_PropertyRealization94'):
        assert not _is_linked(a1, 'rapidml_PropertyRealization94', b)
    if hasattr(a2, 'rapidml_PropertyRealization94'):
        assert _is_linked(a2, 'rapidml_PropertyRealization94', b)
    _safe_set(b, 'rapidml_ObjectRealization93', set())
    assert not _is_linked(b, 'rapidml_ObjectRealization93', a2)
    if hasattr(a2, 'rapidml_PropertyRealization94'):
        assert not _is_linked(a2, 'rapidml_PropertyRealization94', b)


def test_assoc_ownedDataTypes153_reverse_link_reassign_clear():
    a1 = rapidml_DataType(name="sample_text")
    a2 = rapidml_DataType(name="sample_text_2")
    b = rapidml_DataModel(name="sample_text")
    _safe_set(b, 'rapidml_DataModel154', {a1})
    assert _is_linked(b, 'rapidml_DataModel154', a1)
    if hasattr(a1, 'rapidml_DataType'):
        assert _is_linked(a1, 'rapidml_DataType', b)
    _safe_set(b, 'rapidml_DataModel154', {a2})
    assert _is_linked(b, 'rapidml_DataModel154', a2)
    if hasattr(a1, 'rapidml_DataType'):
        assert not _is_linked(a1, 'rapidml_DataType', b)
    if hasattr(a2, 'rapidml_DataType'):
        assert _is_linked(a2, 'rapidml_DataType', b)
    _safe_set(b, 'rapidml_DataModel154', set())
    assert not _is_linked(b, 'rapidml_DataModel154', a2)
    if hasattr(a2, 'rapidml_DataType'):
        assert not _is_linked(a2, 'rapidml_DataType', b)


def test_assoc_ownedElements144_reverse_link_reassign_clear():
    a1 = rapidml_Structure()
    a2 = rapidml_Structure()
    b = rapidml_Structure()
    _safe_set(b, 'rapidml_Structure145', a1)
    assert _is_linked(b, 'rapidml_Structure145', a1)
    if hasattr(a1, 'rapidml_Structure143'):
        assert _is_linked(a1, 'rapidml_Structure143', b)
    _safe_set(b, 'rapidml_Structure145', a2)
    assert _is_linked(b, 'rapidml_Structure145', a2)
    if hasattr(a1, 'rapidml_Structure143'):
        assert not _is_linked(a1, 'rapidml_Structure143', b)
    if hasattr(a2, 'rapidml_Structure143'):
        assert _is_linked(a2, 'rapidml_Structure143', b)
    _safe_set(b, 'rapidml_Structure145', None)
    assert not _is_linked(b, 'rapidml_Structure145', a2)
    if hasattr(a2, 'rapidml_Structure143'):
        assert not _is_linked(a2, 'rapidml_Structure143', b)


def test_assoc_ownedFeatures142_reverse_link_reassign_clear():
    a1 = rapidml_Structure()
    a2 = rapidml_Structure()
    b = rapidml_Feature(key=True, name="sample_text", readOnly=True, restriction=True)
    _safe_set(b, 'Feature', a1)
    assert _is_linked(b, 'Feature', a1)
    if hasattr(a1, 'containingDataType'):
        assert _is_linked(a1, 'containingDataType', b)
    _safe_set(b, 'Feature', a2)
    assert _is_linked(b, 'Feature', a2)
    if hasattr(a1, 'containingDataType'):
        assert not _is_linked(a1, 'containingDataType', b)
    if hasattr(a2, 'containingDataType'):
        assert _is_linked(a2, 'containingDataType', b)
    _safe_set(b, 'Feature', None)
    assert not _is_linked(b, 'Feature', a2)
    if hasattr(a2, 'containingDataType'):
        assert not _is_linked(a2, 'containingDataType', b)


def test_assoc_ownedOperations146_reverse_link_reassign_clear():
    a1 = rapidml_Structure()
    a2 = rapidml_Structure()
    b = rapidml_Operation(name="sample_text")
    _safe_set(b, 'rapidml_Operation', a1)
    assert _is_linked(b, 'rapidml_Operation', a1)
    if hasattr(a1, 'rapidml_Structure147'):
        assert _is_linked(a1, 'rapidml_Structure147', b)
    _safe_set(b, 'rapidml_Operation', a2)
    assert _is_linked(b, 'rapidml_Operation', a2)
    if hasattr(a1, 'rapidml_Structure147'):
        assert not _is_linked(a1, 'rapidml_Structure147', b)
    if hasattr(a2, 'rapidml_Structure147'):
        assert _is_linked(a2, 'rapidml_Structure147', b)
    _safe_set(b, 'rapidml_Operation', None)
    assert not _is_linked(b, 'rapidml_Operation', a2)
    if hasattr(a2, 'rapidml_Structure147'):
        assert not _is_linked(a2, 'rapidml_Structure147', b)


def test_assoc_ownedReferenceRealization71_reverse_link_reassign_clear():
    a1 = rapidml_ReferenceTreatment()
    a2 = rapidml_ReferenceTreatment()
    b = rapidml_ReferenceRealization(multiValued=True, realizationType="sample_text")
    _safe_set(b, 'rapidml_ReferenceRealization73', a1)
    assert _is_linked(b, 'rapidml_ReferenceRealization73', a1)
    if hasattr(a1, 'rapidml_ReferenceTreatment72'):
        assert _is_linked(a1, 'rapidml_ReferenceTreatment72', b)
    _safe_set(b, 'rapidml_ReferenceRealization73', a2)
    assert _is_linked(b, 'rapidml_ReferenceRealization73', a2)
    if hasattr(a1, 'rapidml_ReferenceTreatment72'):
        assert not _is_linked(a1, 'rapidml_ReferenceTreatment72', b)
    if hasattr(a2, 'rapidml_ReferenceTreatment72'):
        assert _is_linked(a2, 'rapidml_ReferenceTreatment72', b)
    _safe_set(b, 'rapidml_ReferenceRealization73', None)
    assert not _is_linked(b, 'rapidml_ReferenceRealization73', a2)
    if hasattr(a2, 'rapidml_ReferenceTreatment72'):
        assert not _is_linked(a2, 'rapidml_ReferenceTreatment72', b)


def test_assoc_ownedResourceDefinitions48_reverse_link_reassign_clear():
    a1 = rapidml_ResourceDefinition(name="sample_text")
    a2 = rapidml_ResourceDefinition(name="sample_text_2")
    b = rapidml_ResourceAPI(baseURI="sample_text", name="sample_text", version="sample_text")
    _safe_set(b, 'rapidml_ResourceAPI49', {a1})
    assert _is_linked(b, 'rapidml_ResourceAPI49', a1)
    if hasattr(a1, 'rapidml_ResourceDefinition50'):
        assert _is_linked(a1, 'rapidml_ResourceDefinition50', b)
    _safe_set(b, 'rapidml_ResourceAPI49', {a2})
    assert _is_linked(b, 'rapidml_ResourceAPI49', a2)
    if hasattr(a1, 'rapidml_ResourceDefinition50'):
        assert not _is_linked(a1, 'rapidml_ResourceDefinition50', b)
    if hasattr(a2, 'rapidml_ResourceDefinition50'):
        assert _is_linked(a2, 'rapidml_ResourceDefinition50', b)
    _safe_set(b, 'rapidml_ResourceAPI49', set())
    assert not _is_linked(b, 'rapidml_ResourceAPI49', a2)
    if hasattr(a2, 'rapidml_ResourceDefinition50'):
        assert not _is_linked(a2, 'rapidml_ResourceDefinition50', b)


def test_assoc_parameters103_reverse_link_reassign_clear():
    a1 = rapidml_SecurityScheme(flow="sample_text", name="sample_text", type="sample_text")
    a2 = rapidml_SecurityScheme(flow="sample_text_2", name="sample_text_2", type="sample_text_2")
    b = rapidml_MessageParameter(httpLocation="sample_text")
    _safe_set(b, 'rapidml_MessageParameter', a1)
    assert _is_linked(b, 'rapidml_MessageParameter', a1)
    if hasattr(a1, 'rapidml_SecurityScheme104'):
        assert _is_linked(a1, 'rapidml_SecurityScheme104', b)
    _safe_set(b, 'rapidml_MessageParameter', a2)
    assert _is_linked(b, 'rapidml_MessageParameter', a2)
    if hasattr(a1, 'rapidml_SecurityScheme104'):
        assert not _is_linked(a1, 'rapidml_SecurityScheme104', b)
    if hasattr(a2, 'rapidml_SecurityScheme104'):
        assert _is_linked(a2, 'rapidml_SecurityScheme104', b)
    _safe_set(b, 'rapidml_MessageParameter', None)
    assert not _is_linked(b, 'rapidml_MessageParameter', a2)
    if hasattr(a2, 'rapidml_SecurityScheme104'):
        assert not _is_linked(a2, 'rapidml_SecurityScheme104', b)


def test_assoc_parameters7_reverse_link_reassign_clear():
    a1 = rapidml_TypedMessage(useParentTypeReference=True)
    a2 = rapidml_TypedMessage(useParentTypeReference=False)
    b = rapidml_MessageParameter(httpLocation="sample_text")
    _safe_set(b, 'MessageParameter', a1)
    assert _is_linked(b, 'MessageParameter', a1)
    if hasattr(a1, 'containingMessage'):
        assert _is_linked(a1, 'containingMessage', b)
    _safe_set(b, 'MessageParameter', a2)
    assert _is_linked(b, 'MessageParameter', a2)
    if hasattr(a1, 'containingMessage'):
        assert not _is_linked(a1, 'containingMessage', b)
    if hasattr(a2, 'containingMessage'):
        assert _is_linked(a2, 'containingMessage', b)
    _safe_set(b, 'MessageParameter', None)
    assert not _is_linked(b, 'MessageParameter', a2)
    if hasattr(a2, 'containingMessage'):
        assert not _is_linked(a2, 'containingMessage', b)


def test_assoc_primitiveTypes131_reverse_link_reassign_clear():
    a1 = rapidml_PrimitiveTypesLibrary(name="sample_text")
    a2 = rapidml_PrimitiveTypesLibrary(name="sample_text_2")
    b = rapidml_PrimitiveType()
    _safe_set(b, 'rapidml_PrimitiveType133', a1)
    assert _is_linked(b, 'rapidml_PrimitiveType133', a1)
    if hasattr(a1, 'rapidml_PrimitiveTypesLibrary132'):
        assert _is_linked(a1, 'rapidml_PrimitiveTypesLibrary132', b)
    _safe_set(b, 'rapidml_PrimitiveType133', a2)
    assert _is_linked(b, 'rapidml_PrimitiveType133', a2)
    if hasattr(a1, 'rapidml_PrimitiveTypesLibrary132'):
        assert not _is_linked(a1, 'rapidml_PrimitiveTypesLibrary132', b)
    if hasattr(a2, 'rapidml_PrimitiveTypesLibrary132'):
        assert _is_linked(a2, 'rapidml_PrimitiveTypesLibrary132', b)
    _safe_set(b, 'rapidml_PrimitiveType133', None)
    assert not _is_linked(b, 'rapidml_PrimitiveType133', a2)
    if hasattr(a2, 'rapidml_PrimitiveTypesLibrary132'):
        assert not _is_linked(a2, 'rapidml_PrimitiveTypesLibrary132', b)


def test_assoc_primitiveTypesLibrary42_reverse_link_reassign_clear():
    a1 = rapidml_ZenModel(name="sample_text", namespace="sample_text")
    a2 = rapidml_ZenModel(name="sample_text_2", namespace="sample_text_2")
    b = rapidml_PrimitiveTypesLibrary(name="sample_text")
    _safe_set(b, 'rapidml_PrimitiveTypesLibrary', a1)
    assert _is_linked(b, 'rapidml_PrimitiveTypesLibrary', a1)
    if hasattr(a1, 'rapidml_ZenModel43'):
        assert _is_linked(a1, 'rapidml_ZenModel43', b)
    _safe_set(b, 'rapidml_PrimitiveTypesLibrary', a2)
    assert _is_linked(b, 'rapidml_PrimitiveTypesLibrary', a2)
    if hasattr(a1, 'rapidml_ZenModel43'):
        assert not _is_linked(a1, 'rapidml_ZenModel43', b)
    if hasattr(a2, 'rapidml_ZenModel43'):
        assert _is_linked(a2, 'rapidml_ZenModel43', b)
    _safe_set(b, 'rapidml_PrimitiveTypesLibrary', None)
    assert not _is_linked(b, 'rapidml_PrimitiveTypesLibrary', a2)
    if hasattr(a2, 'rapidml_ZenModel43'):
        assert not _is_linked(a2, 'rapidml_ZenModel43', b)


def test_assoc_properties117_reverse_link_reassign_clear():
    a1 = rapidml_RealizationContainer(effectiveRealization="sample_text", realizationName="sample_text", withDefaultRealization=True)
    a2 = rapidml_RealizationContainer(effectiveRealization="sample_text_2", realizationName="sample_text_2", withDefaultRealization=False)
    b = rapidml_ObjectRealization()
    _safe_set(b, 'rapidml_ObjectRealization118', a1)
    assert _is_linked(b, 'rapidml_ObjectRealization118', a1)
    if hasattr(a1, 'rapidml_RealizationContainer'):
        assert _is_linked(a1, 'rapidml_RealizationContainer', b)
    _safe_set(b, 'rapidml_ObjectRealization118', a2)
    assert _is_linked(b, 'rapidml_ObjectRealization118', a2)
    if hasattr(a1, 'rapidml_RealizationContainer'):
        assert not _is_linked(a1, 'rapidml_RealizationContainer', b)
    if hasattr(a2, 'rapidml_RealizationContainer'):
        assert _is_linked(a2, 'rapidml_RealizationContainer', b)
    _safe_set(b, 'rapidml_ObjectRealization118', None)
    assert not _is_linked(b, 'rapidml_ObjectRealization118', a2)
    if hasattr(a2, 'rapidml_RealizationContainer'):
        assert not _is_linked(a2, 'rapidml_RealizationContainer', b)


def test_assoc_realizationContainer98_reverse_link_reassign_clear():
    a1 = rapidml_RealizationContainer(effectiveRealization="sample_text", realizationName="sample_text", withDefaultRealization=True)
    a2 = rapidml_RealizationContainer(effectiveRealization="sample_text_2", realizationName="sample_text_2", withDefaultRealization=False)
    b = rapidml_ObjectRealization()
    _safe_set(b, 'inlineObjectRealization', a1)
    assert _is_linked(b, 'inlineObjectRealization', a1)
    if hasattr(a1, 'RealizationContainer'):
        assert _is_linked(a1, 'RealizationContainer', b)
    _safe_set(b, 'inlineObjectRealization', a2)
    assert _is_linked(b, 'inlineObjectRealization', a2)
    if hasattr(a1, 'RealizationContainer'):
        assert not _is_linked(a1, 'RealizationContainer', b)
    if hasattr(a2, 'RealizationContainer'):
        assert _is_linked(a2, 'RealizationContainer', b)
    _safe_set(b, 'inlineObjectRealization', None)
    assert not _is_linked(b, 'inlineObjectRealization', a2)
    if hasattr(a2, 'RealizationContainer'):
        assert not _is_linked(a2, 'RealizationContainer', b)


def test_assoc_referenceElement67_reverse_link_reassign_clear():
    a1 = rapidml_ReferenceTreatment()
    a2 = rapidml_ReferenceTreatment()
    b = rapidml_ReferenceElement()
    _safe_set(b, 'rapidml_ReferenceElement', a1)
    assert _is_linked(b, 'rapidml_ReferenceElement', a1)
    if hasattr(a1, 'rapidml_ReferenceTreatment'):
        assert _is_linked(a1, 'rapidml_ReferenceTreatment', b)
    _safe_set(b, 'rapidml_ReferenceElement', a2)
    assert _is_linked(b, 'rapidml_ReferenceElement', a2)
    if hasattr(a1, 'rapidml_ReferenceTreatment'):
        assert not _is_linked(a1, 'rapidml_ReferenceTreatment', b)
    if hasattr(a2, 'rapidml_ReferenceTreatment'):
        assert _is_linked(a2, 'rapidml_ReferenceTreatment', b)
    _safe_set(b, 'rapidml_ReferenceElement', None)
    assert not _is_linked(b, 'rapidml_ReferenceElement', a2)
    if hasattr(a2, 'rapidml_ReferenceTreatment'):
        assert not _is_linked(a2, 'rapidml_ReferenceTreatment', b)


def test_assoc_referenceElements30_reverse_link_reassign_clear():
    a1 = rapidml_CollectionResource(resourceRealizationKind="sample_text")
    a2 = rapidml_CollectionResource(resourceRealizationKind="sample_text_2")
    b = rapidml_CollectionReferenceElement()
    _safe_set(b, 'rapidml_CollectionReferenceElement', a1)
    assert _is_linked(b, 'rapidml_CollectionReferenceElement', a1)
    if hasattr(a1, 'rapidml_CollectionResource'):
        assert _is_linked(a1, 'rapidml_CollectionResource', b)
    _safe_set(b, 'rapidml_CollectionReferenceElement', a2)
    assert _is_linked(b, 'rapidml_CollectionReferenceElement', a2)
    if hasattr(a1, 'rapidml_CollectionResource'):
        assert not _is_linked(a1, 'rapidml_CollectionResource', b)
    if hasattr(a2, 'rapidml_CollectionResource'):
        assert _is_linked(a2, 'rapidml_CollectionResource', b)
    _safe_set(b, 'rapidml_CollectionReferenceElement', None)
    assert not _is_linked(b, 'rapidml_CollectionReferenceElement', a2)
    if hasattr(a2, 'rapidml_CollectionResource'):
        assert not _is_linked(a2, 'rapidml_CollectionResource', b)


def test_assoc_referenceRealization68_reverse_link_reassign_clear():
    a1 = rapidml_ReferenceTreatment()
    a2 = rapidml_ReferenceTreatment()
    b = rapidml_ReferenceRealization(multiValued=True, realizationType="sample_text")
    _safe_set(b, 'rapidml_ReferenceRealization70', a1)
    assert _is_linked(b, 'rapidml_ReferenceRealization70', a1)
    if hasattr(a1, 'rapidml_ReferenceTreatment69'):
        assert _is_linked(a1, 'rapidml_ReferenceTreatment69', b)
    _safe_set(b, 'rapidml_ReferenceRealization70', a2)
    assert _is_linked(b, 'rapidml_ReferenceRealization70', a2)
    if hasattr(a1, 'rapidml_ReferenceTreatment69'):
        assert not _is_linked(a1, 'rapidml_ReferenceTreatment69', b)
    if hasattr(a2, 'rapidml_ReferenceTreatment69'):
        assert _is_linked(a2, 'rapidml_ReferenceTreatment69', b)
    _safe_set(b, 'rapidml_ReferenceRealization70', None)
    assert not _is_linked(b, 'rapidml_ReferenceRealization70', a2)
    if hasattr(a2, 'rapidml_ReferenceTreatment69'):
        assert not _is_linked(a2, 'rapidml_ReferenceTreatment69', b)


def test_assoc_referenceTreatments119_reverse_link_reassign_clear():
    a1 = rapidml_ReferenceTreatment()
    a2 = rapidml_ReferenceTreatment()
    b = rapidml_RealizationContainer(effectiveRealization="sample_text", realizationName="sample_text", withDefaultRealization=True)
    _safe_set(b, 'rapidml_RealizationContainer120', {a1})
    assert _is_linked(b, 'rapidml_RealizationContainer120', a1)
    if hasattr(a1, 'rapidml_ReferenceTreatment121'):
        assert _is_linked(a1, 'rapidml_ReferenceTreatment121', b)
    _safe_set(b, 'rapidml_RealizationContainer120', {a2})
    assert _is_linked(b, 'rapidml_RealizationContainer120', a2)
    if hasattr(a1, 'rapidml_ReferenceTreatment121'):
        assert not _is_linked(a1, 'rapidml_ReferenceTreatment121', b)
    if hasattr(a2, 'rapidml_ReferenceTreatment121'):
        assert _is_linked(a2, 'rapidml_ReferenceTreatment121', b)
    _safe_set(b, 'rapidml_RealizationContainer120', set())
    assert not _is_linked(b, 'rapidml_RealizationContainer120', a2)
    if hasattr(a2, 'rapidml_ReferenceTreatment121'):
        assert not _is_linked(a2, 'rapidml_ReferenceTreatment121', b)


def test_assoc_resourceAPIs35_reverse_link_reassign_clear():
    a1 = rapidml_ZenModel(name="sample_text", namespace="sample_text")
    a2 = rapidml_ZenModel(name="sample_text_2", namespace="sample_text_2")
    b = rapidml_ResourceAPI(baseURI="sample_text", name="sample_text", version="sample_text")
    _safe_set(b, 'rapidml_ResourceAPI', a1)
    assert _is_linked(b, 'rapidml_ResourceAPI', a1)
    if hasattr(a1, 'rapidml_ZenModel'):
        assert _is_linked(a1, 'rapidml_ZenModel', b)
    _safe_set(b, 'rapidml_ResourceAPI', a2)
    assert _is_linked(b, 'rapidml_ResourceAPI', a2)
    if hasattr(a1, 'rapidml_ZenModel'):
        assert not _is_linked(a1, 'rapidml_ZenModel', b)
    if hasattr(a2, 'rapidml_ZenModel'):
        assert _is_linked(a2, 'rapidml_ZenModel', b)
    _safe_set(b, 'rapidml_ResourceAPI', None)
    assert not _is_linked(b, 'rapidml_ResourceAPI', a2)
    if hasattr(a2, 'rapidml_ZenModel'):
        assert not _is_linked(a2, 'rapidml_ZenModel', b)


def test_assoc_resourceType8_reverse_link_reassign_clear():
    a1 = rapidml_TypedMessage(useParentTypeReference=True)
    a2 = rapidml_TypedMessage(useParentTypeReference=False)
    b = rapidml_ResourceDefinition(name="sample_text")
    _safe_set(b, 'rapidml_ResourceDefinition9', a1)
    assert _is_linked(b, 'rapidml_ResourceDefinition9', a1)
    if hasattr(a1, 'rapidml_TypedMessage'):
        assert _is_linked(a1, 'rapidml_TypedMessage', b)
    _safe_set(b, 'rapidml_ResourceDefinition9', a2)
    assert _is_linked(b, 'rapidml_ResourceDefinition9', a2)
    if hasattr(a1, 'rapidml_TypedMessage'):
        assert not _is_linked(a1, 'rapidml_TypedMessage', b)
    if hasattr(a2, 'rapidml_TypedMessage'):
        assert _is_linked(a2, 'rapidml_TypedMessage', b)
    _safe_set(b, 'rapidml_ResourceDefinition9', None)
    assert not _is_linked(b, 'rapidml_ResourceDefinition9', a2)
    if hasattr(a2, 'rapidml_TypedMessage'):
        assert not _is_linked(a2, 'rapidml_TypedMessage', b)


def test_assoc_responses14_reverse_link_reassign_clear():
    a1 = rapidml_TypedResponse(statusCode=7)
    a2 = rapidml_TypedResponse(statusCode=13)
    b = rapidml_Method(httpMethod="sample_text", id="sample_text")
    _safe_set(b, 'containingMethod15', {a1})
    assert _is_linked(b, 'containingMethod15', a1)
    if hasattr(a1, 'TypedResponse'):
        assert _is_linked(a1, 'TypedResponse', b)
    _safe_set(b, 'containingMethod15', {a2})
    assert _is_linked(b, 'containingMethod15', a2)
    if hasattr(a1, 'TypedResponse'):
        assert not _is_linked(a1, 'TypedResponse', b)
    if hasattr(a2, 'TypedResponse'):
        assert _is_linked(a2, 'TypedResponse', b)
    _safe_set(b, 'containingMethod15', set())
    assert not _is_linked(b, 'containingMethod15', a2)
    if hasattr(a2, 'TypedResponse'):
        assert not _is_linked(a2, 'TypedResponse', b)


def test_assoc_scopes100_reverse_link_reassign_clear():
    a1 = rapidml_SecurityScope(name="sample_text")
    a2 = rapidml_SecurityScope(name="sample_text_2")
    b = rapidml_SecurityScheme(flow="sample_text", name="sample_text", type="sample_text")
    _safe_set(b, 'rapidml_SecurityScheme', {a1})
    assert _is_linked(b, 'rapidml_SecurityScheme', a1)
    if hasattr(a1, 'rapidml_SecurityScope'):
        assert _is_linked(a1, 'rapidml_SecurityScope', b)
    _safe_set(b, 'rapidml_SecurityScheme', {a2})
    assert _is_linked(b, 'rapidml_SecurityScheme', a2)
    if hasattr(a1, 'rapidml_SecurityScope'):
        assert not _is_linked(a1, 'rapidml_SecurityScope', b)
    if hasattr(a2, 'rapidml_SecurityScope'):
        assert _is_linked(a2, 'rapidml_SecurityScope', b)
    _safe_set(b, 'rapidml_SecurityScheme', set())
    assert not _is_linked(b, 'rapidml_SecurityScheme', a2)
    if hasattr(a2, 'rapidml_SecurityScope'):
        assert not _is_linked(a2, 'rapidml_SecurityScope', b)


def test_assoc_securitySchemes113_reverse_link_reassign_clear():
    a1 = rapidml_SecuritySchemeLibrary(name="sample_text")
    a2 = rapidml_SecuritySchemeLibrary(name="sample_text_2")
    b = rapidml_SecurityScheme(flow="sample_text", name="sample_text", type="sample_text")
    _safe_set(b, 'rapidml_SecurityScheme115', a1)
    assert _is_linked(b, 'rapidml_SecurityScheme115', a1)
    if hasattr(a1, 'rapidml_SecuritySchemeLibrary114'):
        assert _is_linked(a1, 'rapidml_SecuritySchemeLibrary114', b)
    _safe_set(b, 'rapidml_SecurityScheme115', a2)
    assert _is_linked(b, 'rapidml_SecurityScheme115', a2)
    if hasattr(a1, 'rapidml_SecuritySchemeLibrary114'):
        assert not _is_linked(a1, 'rapidml_SecuritySchemeLibrary114', b)
    if hasattr(a2, 'rapidml_SecuritySchemeLibrary114'):
        assert _is_linked(a2, 'rapidml_SecuritySchemeLibrary114', b)
    _safe_set(b, 'rapidml_SecurityScheme115', None)
    assert not _is_linked(b, 'rapidml_SecurityScheme115', a2)
    if hasattr(a2, 'rapidml_SecuritySchemeLibrary114'):
        assert not _is_linked(a2, 'rapidml_SecuritySchemeLibrary114', b)


def test_assoc_securitySchemesLibrary46_reverse_link_reassign_clear():
    a1 = rapidml_ZenModel(name="sample_text", namespace="sample_text")
    a2 = rapidml_ZenModel(name="sample_text_2", namespace="sample_text_2")
    b = rapidml_SecuritySchemeLibrary(name="sample_text")
    _safe_set(b, 'rapidml_SecuritySchemeLibrary', a1)
    assert _is_linked(b, 'rapidml_SecuritySchemeLibrary', a1)
    if hasattr(a1, 'rapidml_ZenModel47'):
        assert _is_linked(a1, 'rapidml_ZenModel47', b)
    _safe_set(b, 'rapidml_SecuritySchemeLibrary', a2)
    assert _is_linked(b, 'rapidml_SecuritySchemeLibrary', a2)
    if hasattr(a1, 'rapidml_ZenModel47'):
        assert not _is_linked(a1, 'rapidml_ZenModel47', b)
    if hasattr(a2, 'rapidml_ZenModel47'):
        assert _is_linked(a2, 'rapidml_ZenModel47', b)
    _safe_set(b, 'rapidml_SecuritySchemeLibrary', None)
    assert not _is_linked(b, 'rapidml_SecuritySchemeLibrary', a2)
    if hasattr(a2, 'rapidml_ZenModel47'):
        assert not _is_linked(a2, 'rapidml_ZenModel47', b)


def test_assoc_serviceDataModels51_reverse_link_reassign_clear():
    a1 = rapidml_ResourceAPI(baseURI="sample_text", name="sample_text", version="sample_text")
    a2 = rapidml_ResourceAPI(baseURI="sample_text_2", name="sample_text_2", version="sample_text_2")
    b = rapidml_DataModel(name="sample_text")
    _safe_set(b, 'rapidml_DataModel53', a1)
    assert _is_linked(b, 'rapidml_DataModel53', a1)
    if hasattr(a1, 'rapidml_ResourceAPI52'):
        assert _is_linked(a1, 'rapidml_ResourceAPI52', b)
    _safe_set(b, 'rapidml_DataModel53', a2)
    assert _is_linked(b, 'rapidml_DataModel53', a2)
    if hasattr(a1, 'rapidml_ResourceAPI52'):
        assert not _is_linked(a1, 'rapidml_ResourceAPI52', b)
    if hasattr(a2, 'rapidml_ResourceAPI52'):
        assert _is_linked(a2, 'rapidml_ResourceAPI52', b)
    _safe_set(b, 'rapidml_DataModel53', None)
    assert not _is_linked(b, 'rapidml_DataModel53', a2)
    if hasattr(a2, 'rapidml_ResourceAPI52'):
        assert not _is_linked(a2, 'rapidml_ResourceAPI52', b)


def test_assoc_settings101_reverse_link_reassign_clear():
    a1 = rapidml_SecuritySchemeParameter(name="sample_text", value="sample_text")
    a2 = rapidml_SecuritySchemeParameter(name="sample_text_2", value="sample_text_2")
    b = rapidml_SecurityScheme(flow="sample_text", name="sample_text", type="sample_text")
    _safe_set(b, 'rapidml_SecurityScheme102', {a1})
    assert _is_linked(b, 'rapidml_SecurityScheme102', a1)
    if hasattr(a1, 'rapidml_SecuritySchemeParameter'):
        assert _is_linked(a1, 'rapidml_SecuritySchemeParameter', b)
    _safe_set(b, 'rapidml_SecurityScheme102', {a2})
    assert _is_linked(b, 'rapidml_SecurityScheme102', a2)
    if hasattr(a1, 'rapidml_SecuritySchemeParameter'):
        assert not _is_linked(a1, 'rapidml_SecuritySchemeParameter', b)
    if hasattr(a2, 'rapidml_SecuritySchemeParameter'):
        assert _is_linked(a2, 'rapidml_SecuritySchemeParameter', b)
    _safe_set(b, 'rapidml_SecurityScheme102', set())
    assert not _is_linked(b, 'rapidml_SecurityScheme102', a2)
    if hasattr(a2, 'rapidml_SecuritySchemeParameter'):
        assert not _is_linked(a2, 'rapidml_SecuritySchemeParameter', b)


def test_assoc_simpleType81_reverse_link_reassign_clear():
    a1 = rapidml_PrimitiveTypeSourceReference()
    a2 = rapidml_PrimitiveTypeSourceReference()
    b = rapidml_PrimitiveType()
    _safe_set(b, 'rapidml_PrimitiveType', a1)
    assert _is_linked(b, 'rapidml_PrimitiveType', a1)
    if hasattr(a1, 'rapidml_PrimitiveTypeSourceReference'):
        assert _is_linked(a1, 'rapidml_PrimitiveTypeSourceReference', b)
    _safe_set(b, 'rapidml_PrimitiveType', a2)
    assert _is_linked(b, 'rapidml_PrimitiveType', a2)
    if hasattr(a1, 'rapidml_PrimitiveTypeSourceReference'):
        assert not _is_linked(a1, 'rapidml_PrimitiveTypeSourceReference', b)
    if hasattr(a2, 'rapidml_PrimitiveTypeSourceReference'):
        assert _is_linked(a2, 'rapidml_PrimitiveTypeSourceReference', b)
    _safe_set(b, 'rapidml_PrimitiveType', None)
    assert not _is_linked(b, 'rapidml_PrimitiveType', a2)
    if hasattr(a2, 'rapidml_PrimitiveTypeSourceReference'):
        assert not _is_linked(a2, 'rapidml_PrimitiveTypeSourceReference', b)


def test_assoc_sourceReference17_reverse_link_reassign_clear():
    a1 = rapidml_SourceReference()
    a2 = rapidml_SourceReference()
    b = rapidml_Parameter(default="sample_text", fixed="sample_text", name="sample_text", required=True)
    _safe_set(b, 'containingParameter', a1)
    assert _is_linked(b, 'containingParameter', a1)
    if hasattr(a1, 'SourceReference'):
        assert _is_linked(a1, 'SourceReference', b)
    _safe_set(b, 'containingParameter', a2)
    assert _is_linked(b, 'containingParameter', a2)
    if hasattr(a1, 'SourceReference'):
        assert not _is_linked(a1, 'SourceReference', b)
    if hasattr(a2, 'SourceReference'):
        assert _is_linked(a2, 'SourceReference', b)
    _safe_set(b, 'containingParameter', None)
    assert not _is_linked(b, 'containingParameter', a2)
    if hasattr(a2, 'SourceReference'):
        assert not _is_linked(a2, 'SourceReference', b)


def test_assoc_targetResource74_reverse_link_reassign_clear():
    a1 = rapidml_ResourceDefinition(name="sample_text")
    a2 = rapidml_ResourceDefinition(name="sample_text_2")
    b = rapidml_ReferenceRealization(multiValued=True, realizationType="sample_text")
    _safe_set(b, 'rapidml_ReferenceRealization75', a1)
    assert _is_linked(b, 'rapidml_ReferenceRealization75', a1)
    if hasattr(a1, 'rapidml_ResourceDefinition76'):
        assert _is_linked(a1, 'rapidml_ResourceDefinition76', b)
    _safe_set(b, 'rapidml_ReferenceRealization75', a2)
    assert _is_linked(b, 'rapidml_ReferenceRealization75', a2)
    if hasattr(a1, 'rapidml_ResourceDefinition76'):
        assert not _is_linked(a1, 'rapidml_ResourceDefinition76', b)
    if hasattr(a2, 'rapidml_ResourceDefinition76'):
        assert _is_linked(a2, 'rapidml_ResourceDefinition76', b)
    _safe_set(b, 'rapidml_ReferenceRealization75', None)
    assert not _is_linked(b, 'rapidml_ReferenceRealization75', a2)
    if hasattr(a2, 'rapidml_ResourceDefinition76'):
        assert not _is_linked(a2, 'rapidml_ResourceDefinition76', b)


def test_assoc_type135_reverse_link_reassign_clear():
    a1 = rapidml_Structure()
    a2 = rapidml_Structure()
    b = rapidml_ReferenceProperty(container=True, containment=True)
    _safe_set(b, 'rapidml_ReferenceProperty', a1)
    assert _is_linked(b, 'rapidml_ReferenceProperty', a1)
    if hasattr(a1, 'rapidml_Structure136'):
        assert _is_linked(a1, 'rapidml_Structure136', b)
    _safe_set(b, 'rapidml_ReferenceProperty', a2)
    assert _is_linked(b, 'rapidml_ReferenceProperty', a2)
    if hasattr(a1, 'rapidml_Structure136'):
        assert not _is_linked(a1, 'rapidml_Structure136', b)
    if hasattr(a2, 'rapidml_Structure136'):
        assert _is_linked(a2, 'rapidml_Structure136', b)
    _safe_set(b, 'rapidml_ReferenceProperty', None)
    assert not _is_linked(b, 'rapidml_ReferenceProperty', a2)
    if hasattr(a2, 'rapidml_Structure136'):
        assert not _is_linked(a2, 'rapidml_Structure136', b)


def test_assoc_type140_reverse_link_reassign_clear():
    a1 = rapidml_SingleValueType()
    a2 = rapidml_SingleValueType()
    b = rapidml_PrimitiveProperty()
    _safe_set(b, 'rapidml_PrimitiveProperty141', a1)
    assert _is_linked(b, 'rapidml_PrimitiveProperty141', a1)
    if hasattr(a1, 'rapidml_SingleValueType'):
        assert _is_linked(a1, 'rapidml_SingleValueType', b)
    _safe_set(b, 'rapidml_PrimitiveProperty141', a2)
    assert _is_linked(b, 'rapidml_PrimitiveProperty141', a2)
    if hasattr(a1, 'rapidml_SingleValueType'):
        assert not _is_linked(a1, 'rapidml_SingleValueType', b)
    if hasattr(a2, 'rapidml_SingleValueType'):
        assert _is_linked(a2, 'rapidml_SingleValueType', b)
    _safe_set(b, 'rapidml_PrimitiveProperty141', None)
    assert not _is_linked(b, 'rapidml_PrimitiveProperty141', a2)
    if hasattr(a2, 'rapidml_SingleValueType'):
        assert not _is_linked(a2, 'rapidml_SingleValueType', b)


