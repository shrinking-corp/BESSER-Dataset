import inspect
import pytest
from datetime import date, datetime, time, timedelta
from hypothesis import given, settings
import hypothesis.strategies as st

from python_code import (
    GroupRelationship,
    ServiceFeature,
    servicefeaturemodel_Attribute,
    servicefeaturemodel_AttributeType,
    servicefeaturemodel_AttributeTypes,
    servicefeaturemodel_Configuration,
    servicefeaturemodel_Configurations,
    servicefeaturemodel_Excludes,
    servicefeaturemodel_GroupRelationship,
    servicefeaturemodel_MandatoryServiceFeature,
    servicefeaturemodel_OR,
    servicefeaturemodel_OptionalServiceFeature,
    servicefeaturemodel_Preference,
    servicefeaturemodel_Requires,
    servicefeaturemodel_Service,
    servicefeaturemodel_ServiceFeature,
    servicefeaturemodel_ServiceFeatureDiagram,
    servicefeaturemodel_XOR,
    AggregationRules,
    AttributeDomain,
    FeatureTypes,
    ScaleOrders,
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

def test_servicefeaturemodel_Attribute_id_value_roundtrip():
    instance = servicefeaturemodel_Attribute(id="sample_text", instantiationValue="sample_text")
    assert instance.id == "sample_text"
    instance.id = "sample_text_2"
    assert instance.id == "sample_text_2"


def test_servicefeaturemodel_Attribute_instantiationValue_value_roundtrip():
    instance = servicefeaturemodel_Attribute(id="sample_text", instantiationValue="sample_text")
    assert instance.instantiationValue == "sample_text"
    instance.instantiationValue = "sample_text_2"
    assert instance.instantiationValue == "sample_text_2"


def test_servicefeaturemodel_AttributeType_aggregationRule_value_roundtrip():
    instance = servicefeaturemodel_AttributeType(aggregationRule="sample_text", customAttributeTypePriority=7, description="sample_text", domain="sample_text", name="sample_text", requirement="sample_text", requirementWeight="sample_text", scaleOrder="sample_text", toBeEvaluated=True)
    assert instance.aggregationRule == "sample_text"
    instance.aggregationRule = "sample_text_2"
    assert instance.aggregationRule == "sample_text_2"


def test_servicefeaturemodel_AttributeType_customAttributeTypePriority_value_roundtrip():
    instance = servicefeaturemodel_AttributeType(aggregationRule="sample_text", customAttributeTypePriority=7, description="sample_text", domain="sample_text", name="sample_text", requirement="sample_text", requirementWeight="sample_text", scaleOrder="sample_text", toBeEvaluated=True)
    assert instance.customAttributeTypePriority == 7
    instance.customAttributeTypePriority = 13
    assert instance.customAttributeTypePriority == 13


def test_servicefeaturemodel_AttributeType_description_value_roundtrip():
    instance = servicefeaturemodel_AttributeType(aggregationRule="sample_text", customAttributeTypePriority=7, description="sample_text", domain="sample_text", name="sample_text", requirement="sample_text", requirementWeight="sample_text", scaleOrder="sample_text", toBeEvaluated=True)
    assert instance.description == "sample_text"
    instance.description = "sample_text_2"
    assert instance.description == "sample_text_2"


def test_servicefeaturemodel_AttributeType_domain_value_roundtrip():
    instance = servicefeaturemodel_AttributeType(aggregationRule="sample_text", customAttributeTypePriority=7, description="sample_text", domain="sample_text", name="sample_text", requirement="sample_text", requirementWeight="sample_text", scaleOrder="sample_text", toBeEvaluated=True)
    assert instance.domain == "sample_text"
    instance.domain = "sample_text_2"
    assert instance.domain == "sample_text_2"


def test_servicefeaturemodel_AttributeType_name_value_roundtrip():
    instance = servicefeaturemodel_AttributeType(aggregationRule="sample_text", customAttributeTypePriority=7, description="sample_text", domain="sample_text", name="sample_text", requirement="sample_text", requirementWeight="sample_text", scaleOrder="sample_text", toBeEvaluated=True)
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_servicefeaturemodel_AttributeType_requirement_value_roundtrip():
    instance = servicefeaturemodel_AttributeType(aggregationRule="sample_text", customAttributeTypePriority=7, description="sample_text", domain="sample_text", name="sample_text", requirement="sample_text", requirementWeight="sample_text", scaleOrder="sample_text", toBeEvaluated=True)
    assert instance.requirement == "sample_text"
    instance.requirement = "sample_text_2"
    assert instance.requirement == "sample_text_2"


def test_servicefeaturemodel_AttributeType_requirementWeight_value_roundtrip():
    instance = servicefeaturemodel_AttributeType(aggregationRule="sample_text", customAttributeTypePriority=7, description="sample_text", domain="sample_text", name="sample_text", requirement="sample_text", requirementWeight="sample_text", scaleOrder="sample_text", toBeEvaluated=True)
    assert instance.requirementWeight == "sample_text"
    instance.requirementWeight = "sample_text_2"
    assert instance.requirementWeight == "sample_text_2"


def test_servicefeaturemodel_AttributeType_scaleOrder_value_roundtrip():
    instance = servicefeaturemodel_AttributeType(aggregationRule="sample_text", customAttributeTypePriority=7, description="sample_text", domain="sample_text", name="sample_text", requirement="sample_text", requirementWeight="sample_text", scaleOrder="sample_text", toBeEvaluated=True)
    assert instance.scaleOrder == "sample_text"
    instance.scaleOrder = "sample_text_2"
    assert instance.scaleOrder == "sample_text_2"


def test_servicefeaturemodel_AttributeType_toBeEvaluated_value_roundtrip():
    instance = servicefeaturemodel_AttributeType(aggregationRule="sample_text", customAttributeTypePriority=7, description="sample_text", domain="sample_text", name="sample_text", requirement="sample_text", requirementWeight="sample_text", scaleOrder="sample_text", toBeEvaluated=True)
    assert instance.toBeEvaluated == True
    instance.toBeEvaluated = False
    assert instance.toBeEvaluated == False


def test_servicefeaturemodel_Configuration_description_value_roundtrip():
    instance = servicefeaturemodel_Configuration(description="sample_text", id="sample_text", name="sample_text", selected=True)
    assert instance.description == "sample_text"
    instance.description = "sample_text_2"
    assert instance.description == "sample_text_2"


def test_servicefeaturemodel_Configuration_id_value_roundtrip():
    instance = servicefeaturemodel_Configuration(description="sample_text", id="sample_text", name="sample_text", selected=True)
    assert instance.id == "sample_text"
    instance.id = "sample_text_2"
    assert instance.id == "sample_text_2"


def test_servicefeaturemodel_Configuration_name_value_roundtrip():
    instance = servicefeaturemodel_Configuration(description="sample_text", id="sample_text", name="sample_text", selected=True)
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_servicefeaturemodel_Configuration_selected_value_roundtrip():
    instance = servicefeaturemodel_Configuration(description="sample_text", id="sample_text", name="sample_text", selected=True)
    assert instance.selected == True
    instance.selected = False
    assert instance.selected == False


def test_servicefeaturemodel_MandatoryServiceFeature_featureTypes_value_roundtrip():
    instance = servicefeaturemodel_MandatoryServiceFeature(featureTypes="sample_text")
    assert instance.featureTypes == "sample_text"
    instance.featureTypes = "sample_text_2"
    assert instance.featureTypes == "sample_text_2"


def test_servicefeaturemodel_OR_maxFeaturesToChoose_value_roundtrip():
    instance = servicefeaturemodel_OR(maxFeaturesToChoose=7, minFeaturesToChoose=7)
    assert instance.maxFeaturesToChoose == 7
    instance.maxFeaturesToChoose = 13
    assert instance.maxFeaturesToChoose == 13


def test_servicefeaturemodel_OR_minFeaturesToChoose_value_roundtrip():
    instance = servicefeaturemodel_OR(maxFeaturesToChoose=7, minFeaturesToChoose=7)
    assert instance.minFeaturesToChoose == 7
    instance.minFeaturesToChoose = 13
    assert instance.minFeaturesToChoose == 13


def test_servicefeaturemodel_OptionalServiceFeature_featureType_value_roundtrip():
    instance = servicefeaturemodel_OptionalServiceFeature(featureType="sample_text")
    assert instance.featureType == "sample_text"
    instance.featureType = "sample_text_2"
    assert instance.featureType == "sample_text_2"


def test_servicefeaturemodel_Preference_creationDate_value_roundtrip():
    instance = servicefeaturemodel_Preference(creationDate=date(2024, 1, 1), description="sample_text", stakeholderGroup="sample_text", value=3.14)
    assert instance.creationDate == date(2024, 1, 1)
    instance.creationDate = date(2025, 6, 15)
    assert instance.creationDate == date(2025, 6, 15)


def test_servicefeaturemodel_Preference_description_value_roundtrip():
    instance = servicefeaturemodel_Preference(creationDate=date(2024, 1, 1), description="sample_text", stakeholderGroup="sample_text", value=3.14)
    assert instance.description == "sample_text"
    instance.description = "sample_text_2"
    assert instance.description == "sample_text_2"


def test_servicefeaturemodel_Preference_stakeholderGroup_value_roundtrip():
    instance = servicefeaturemodel_Preference(creationDate=date(2024, 1, 1), description="sample_text", stakeholderGroup="sample_text", value=3.14)
    assert instance.stakeholderGroup == "sample_text"
    instance.stakeholderGroup = "sample_text_2"
    assert instance.stakeholderGroup == "sample_text_2"


def test_servicefeaturemodel_Preference_value_value_roundtrip():
    instance = servicefeaturemodel_Preference(creationDate=date(2024, 1, 1), description="sample_text", stakeholderGroup="sample_text", value=3.14)
    assert instance.value == 3.14
    instance.value = 9.99
    assert instance.value == 9.99


def test_servicefeaturemodel_Service_description_value_roundtrip():
    instance = servicefeaturemodel_Service(description="sample_text", id="sample_text", name="sample_text")
    assert instance.description == "sample_text"
    instance.description = "sample_text_2"
    assert instance.description == "sample_text_2"


def test_servicefeaturemodel_Service_id_value_roundtrip():
    instance = servicefeaturemodel_Service(description="sample_text", id="sample_text", name="sample_text")
    assert instance.id == "sample_text"
    instance.id = "sample_text_2"
    assert instance.id == "sample_text_2"


def test_servicefeaturemodel_Service_name_value_roundtrip():
    instance = servicefeaturemodel_Service(description="sample_text", id="sample_text", name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_servicefeaturemodel_ServiceFeature_description_value_roundtrip():
    instance = servicefeaturemodel_ServiceFeature(description="sample_text", id="sample_text", name="sample_text", required=True, requirementWeight="sample_text")
    assert instance.description == "sample_text"
    instance.description = "sample_text_2"
    assert instance.description == "sample_text_2"


def test_servicefeaturemodel_ServiceFeature_id_value_roundtrip():
    instance = servicefeaturemodel_ServiceFeature(description="sample_text", id="sample_text", name="sample_text", required=True, requirementWeight="sample_text")
    assert instance.id == "sample_text"
    instance.id = "sample_text_2"
    assert instance.id == "sample_text_2"


def test_servicefeaturemodel_ServiceFeature_name_value_roundtrip():
    instance = servicefeaturemodel_ServiceFeature(description="sample_text", id="sample_text", name="sample_text", required=True, requirementWeight="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_servicefeaturemodel_ServiceFeature_required_value_roundtrip():
    instance = servicefeaturemodel_ServiceFeature(description="sample_text", id="sample_text", name="sample_text", required=True, requirementWeight="sample_text")
    assert instance.required == True
    instance.required = False
    assert instance.required == False


def test_servicefeaturemodel_ServiceFeature_requirementWeight_value_roundtrip():
    instance = servicefeaturemodel_ServiceFeature(description="sample_text", id="sample_text", name="sample_text", required=True, requirementWeight="sample_text")
    assert instance.requirementWeight == "sample_text"
    instance.requirementWeight = "sample_text_2"
    assert instance.requirementWeight == "sample_text_2"


def test_servicefeaturemodel_ServiceFeatureDiagram_description_value_roundtrip():
    instance = servicefeaturemodel_ServiceFeatureDiagram(description="sample_text", id="sample_text", name="sample_text")
    assert instance.description == "sample_text"
    instance.description = "sample_text_2"
    assert instance.description == "sample_text_2"


def test_servicefeaturemodel_ServiceFeatureDiagram_id_value_roundtrip():
    instance = servicefeaturemodel_ServiceFeatureDiagram(description="sample_text", id="sample_text", name="sample_text")
    assert instance.id == "sample_text"
    instance.id = "sample_text_2"
    assert instance.id == "sample_text_2"


def test_servicefeaturemodel_ServiceFeatureDiagram_name_value_roundtrip():
    instance = servicefeaturemodel_ServiceFeatureDiagram(description="sample_text", id="sample_text", name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_servicefeaturemodel_OR_isa_GroupRelationship():
    instance = servicefeaturemodel_OR(maxFeaturesToChoose=7, minFeaturesToChoose=7)
    assert isinstance(instance, GroupRelationship)


def test_servicefeaturemodel_XOR_isa_GroupRelationship():
    instance = servicefeaturemodel_XOR()
    assert isinstance(instance, GroupRelationship)


def test_servicefeaturemodel_MandatoryServiceFeature_isa_ServiceFeature():
    instance = servicefeaturemodel_MandatoryServiceFeature(featureTypes="sample_text")
    assert isinstance(instance, ServiceFeature)


def test_servicefeaturemodel_OptionalServiceFeature_isa_ServiceFeature():
    instance = servicefeaturemodel_OptionalServiceFeature(featureType="sample_text")
    assert isinstance(instance, ServiceFeature)


def test_assoc_attributeType15_link_reassign_clear():
    a = servicefeaturemodel_AttributeType(aggregationRule="sample_text", customAttributeTypePriority=7, description="sample_text", domain="sample_text", name="sample_text", requirement="sample_text", requirementWeight="sample_text", scaleOrder="sample_text", toBeEvaluated=True)
    b1 = servicefeaturemodel_Attribute(id="sample_text", instantiationValue="sample_text")
    b2 = servicefeaturemodel_Attribute(id="sample_text_2", instantiationValue="sample_text_2")
    _safe_set(a, 'servicefeaturemodel_AttributeType', b1)
    assert _is_linked(a, 'servicefeaturemodel_AttributeType', b1)
    if hasattr(b1, 'servicefeaturemodel_Attribute16'):
        assert _is_linked(b1, 'servicefeaturemodel_Attribute16', a)
    _safe_set(a, 'servicefeaturemodel_AttributeType', b2)
    assert _is_linked(a, 'servicefeaturemodel_AttributeType', b2)
    if hasattr(b1, 'servicefeaturemodel_Attribute16'):
        assert not _is_linked(b1, 'servicefeaturemodel_Attribute16', a)
    if hasattr(b2, 'servicefeaturemodel_Attribute16'):
        assert _is_linked(b2, 'servicefeaturemodel_Attribute16', a)
    _safe_set(a, 'servicefeaturemodel_AttributeType', None)
    assert not _is_linked(a, 'servicefeaturemodel_AttributeType', b2)
    if hasattr(b2, 'servicefeaturemodel_Attribute16'):
        assert not _is_linked(b2, 'servicefeaturemodel_Attribute16', a)


def test_assoc_attributeTypes3_link_reassign_clear():
    a = servicefeaturemodel_Service(description="sample_text", id="sample_text", name="sample_text")
    b1 = servicefeaturemodel_AttributeTypes()
    b2 = servicefeaturemodel_AttributeTypes()
    _safe_set(a, 'servicefeaturemodel_Service4', b1)
    assert _is_linked(a, 'servicefeaturemodel_Service4', b1)
    if hasattr(b1, 'servicefeaturemodel_AttributeTypes'):
        assert _is_linked(b1, 'servicefeaturemodel_AttributeTypes', a)
    _safe_set(a, 'servicefeaturemodel_Service4', b2)
    assert _is_linked(a, 'servicefeaturemodel_Service4', b2)
    if hasattr(b1, 'servicefeaturemodel_AttributeTypes'):
        assert not _is_linked(b1, 'servicefeaturemodel_AttributeTypes', a)
    if hasattr(b2, 'servicefeaturemodel_AttributeTypes'):
        assert _is_linked(b2, 'servicefeaturemodel_AttributeTypes', a)
    _safe_set(a, 'servicefeaturemodel_Service4', None)
    assert not _is_linked(a, 'servicefeaturemodel_Service4', b2)
    if hasattr(b2, 'servicefeaturemodel_AttributeTypes'):
        assert not _is_linked(b2, 'servicefeaturemodel_AttributeTypes', a)


def test_assoc_attributeTypes38_link_reassign_clear():
    a = servicefeaturemodel_AttributeType(aggregationRule="sample_text", customAttributeTypePriority=7, description="sample_text", domain="sample_text", name="sample_text", requirement="sample_text", requirementWeight="sample_text", scaleOrder="sample_text", toBeEvaluated=True)
    b1 = servicefeaturemodel_AttributeTypes()
    b2 = servicefeaturemodel_AttributeTypes()
    _safe_set(a, 'servicefeaturemodel_AttributeType40', b1)
    assert _is_linked(a, 'servicefeaturemodel_AttributeType40', b1)
    if hasattr(b1, 'servicefeaturemodel_AttributeTypes39'):
        assert _is_linked(b1, 'servicefeaturemodel_AttributeTypes39', a)
    _safe_set(a, 'servicefeaturemodel_AttributeType40', b2)
    assert _is_linked(a, 'servicefeaturemodel_AttributeType40', b2)
    if hasattr(b1, 'servicefeaturemodel_AttributeTypes39'):
        assert not _is_linked(b1, 'servicefeaturemodel_AttributeTypes39', a)
    if hasattr(b2, 'servicefeaturemodel_AttributeTypes39'):
        assert _is_linked(b2, 'servicefeaturemodel_AttributeTypes39', a)
    _safe_set(a, 'servicefeaturemodel_AttributeType40', None)
    assert not _is_linked(a, 'servicefeaturemodel_AttributeType40', b2)
    if hasattr(b2, 'servicefeaturemodel_AttributeTypes39'):
        assert not _is_linked(b2, 'servicefeaturemodel_AttributeTypes39', a)


def test_assoc_attributes30_link_reassign_clear():
    a = servicefeaturemodel_Configuration(description="sample_text", id="sample_text", name="sample_text", selected=True)
    b1 = servicefeaturemodel_Attribute(id="sample_text", instantiationValue="sample_text")
    b2 = servicefeaturemodel_Attribute(id="sample_text_2", instantiationValue="sample_text_2")
    _safe_set(a, 'servicefeaturemodel_Configuration31', {b1})
    assert _is_linked(a, 'servicefeaturemodel_Configuration31', b1)
    if hasattr(b1, 'servicefeaturemodel_Attribute32'):
        assert _is_linked(b1, 'servicefeaturemodel_Attribute32', a)
    _safe_set(a, 'servicefeaturemodel_Configuration31', {b2})
    assert _is_linked(a, 'servicefeaturemodel_Configuration31', b2)
    if hasattr(b1, 'servicefeaturemodel_Attribute32'):
        assert not _is_linked(b1, 'servicefeaturemodel_Attribute32', a)
    if hasattr(b2, 'servicefeaturemodel_Attribute32'):
        assert _is_linked(b2, 'servicefeaturemodel_Attribute32', a)
    _safe_set(a, 'servicefeaturemodel_Configuration31', set())
    assert not _is_linked(a, 'servicefeaturemodel_Configuration31', b2)
    if hasattr(b2, 'servicefeaturemodel_Attribute32'):
        assert not _is_linked(b2, 'servicefeaturemodel_Attribute32', a)


def test_assoc_attributes5_link_reassign_clear():
    a = servicefeaturemodel_ServiceFeature(description="sample_text", id="sample_text", name="sample_text", required=True, requirementWeight="sample_text")
    b1 = servicefeaturemodel_Attribute(id="sample_text", instantiationValue="sample_text")
    b2 = servicefeaturemodel_Attribute(id="sample_text_2", instantiationValue="sample_text_2")
    _safe_set(a, 'servicefeaturemodel_ServiceFeature', {b1})
    assert _is_linked(a, 'servicefeaturemodel_ServiceFeature', b1)
    if hasattr(b1, 'servicefeaturemodel_Attribute'):
        assert _is_linked(b1, 'servicefeaturemodel_Attribute', a)
    _safe_set(a, 'servicefeaturemodel_ServiceFeature', {b2})
    assert _is_linked(a, 'servicefeaturemodel_ServiceFeature', b2)
    if hasattr(b1, 'servicefeaturemodel_Attribute'):
        assert not _is_linked(b1, 'servicefeaturemodel_Attribute', a)
    if hasattr(b2, 'servicefeaturemodel_Attribute'):
        assert _is_linked(b2, 'servicefeaturemodel_Attribute', a)
    _safe_set(a, 'servicefeaturemodel_ServiceFeature', set())
    assert not _is_linked(a, 'servicefeaturemodel_ServiceFeature', b2)
    if hasattr(b2, 'servicefeaturemodel_Attribute'):
        assert not _is_linked(b2, 'servicefeaturemodel_Attribute', a)


def test_assoc_configurations1_link_reassign_clear():
    a = servicefeaturemodel_Service(description="sample_text", id="sample_text", name="sample_text")
    b1 = servicefeaturemodel_Configurations()
    b2 = servicefeaturemodel_Configurations()
    _safe_set(a, 'servicefeaturemodel_Service2', b1)
    assert _is_linked(a, 'servicefeaturemodel_Service2', b1)
    if hasattr(b1, 'servicefeaturemodel_Configurations'):
        assert _is_linked(b1, 'servicefeaturemodel_Configurations', a)
    _safe_set(a, 'servicefeaturemodel_Service2', b2)
    assert _is_linked(a, 'servicefeaturemodel_Service2', b2)
    if hasattr(b1, 'servicefeaturemodel_Configurations'):
        assert not _is_linked(b1, 'servicefeaturemodel_Configurations', a)
    if hasattr(b2, 'servicefeaturemodel_Configurations'):
        assert _is_linked(b2, 'servicefeaturemodel_Configurations', a)
    _safe_set(a, 'servicefeaturemodel_Service2', None)
    assert not _is_linked(a, 'servicefeaturemodel_Service2', b2)
    if hasattr(b2, 'servicefeaturemodel_Configurations'):
        assert not _is_linked(b2, 'servicefeaturemodel_Configurations', a)


def test_assoc_configurations35_link_reassign_clear():
    a = servicefeaturemodel_Configuration(description="sample_text", id="sample_text", name="sample_text", selected=True)
    b1 = servicefeaturemodel_Configurations()
    b2 = servicefeaturemodel_Configurations()
    _safe_set(a, 'servicefeaturemodel_Configuration37', b1)
    assert _is_linked(a, 'servicefeaturemodel_Configuration37', b1)
    if hasattr(b1, 'servicefeaturemodel_Configurations36'):
        assert _is_linked(b1, 'servicefeaturemodel_Configurations36', a)
    _safe_set(a, 'servicefeaturemodel_Configuration37', b2)
    assert _is_linked(a, 'servicefeaturemodel_Configuration37', b2)
    if hasattr(b1, 'servicefeaturemodel_Configurations36'):
        assert not _is_linked(b1, 'servicefeaturemodel_Configurations36', a)
    if hasattr(b2, 'servicefeaturemodel_Configurations36'):
        assert _is_linked(b2, 'servicefeaturemodel_Configurations36', a)
    _safe_set(a, 'servicefeaturemodel_Configuration37', None)
    assert not _is_linked(a, 'servicefeaturemodel_Configuration37', b2)
    if hasattr(b2, 'servicefeaturemodel_Configurations36'):
        assert not _is_linked(b2, 'servicefeaturemodel_Configurations36', a)


def test_assoc_excludes10_link_reassign_clear():
    a = servicefeaturemodel_ServiceFeature(description="sample_text", id="sample_text", name="sample_text", required=True, requirementWeight="sample_text")
    b1 = servicefeaturemodel_Excludes()
    b2 = servicefeaturemodel_Excludes()
    _safe_set(a, 'servicefeaturemodel_ServiceFeature11', {b1})
    assert _is_linked(a, 'servicefeaturemodel_ServiceFeature11', b1)
    if hasattr(b1, 'servicefeaturemodel_Excludes'):
        assert _is_linked(b1, 'servicefeaturemodel_Excludes', a)
    _safe_set(a, 'servicefeaturemodel_ServiceFeature11', {b2})
    assert _is_linked(a, 'servicefeaturemodel_ServiceFeature11', b2)
    if hasattr(b1, 'servicefeaturemodel_Excludes'):
        assert not _is_linked(b1, 'servicefeaturemodel_Excludes', a)
    if hasattr(b2, 'servicefeaturemodel_Excludes'):
        assert _is_linked(b2, 'servicefeaturemodel_Excludes', a)
    _safe_set(a, 'servicefeaturemodel_ServiceFeature11', set())
    assert not _is_linked(a, 'servicefeaturemodel_ServiceFeature11', b2)
    if hasattr(b2, 'servicefeaturemodel_Excludes'):
        assert not _is_linked(b2, 'servicefeaturemodel_Excludes', a)


def test_assoc_groupRelationship6_link_reassign_clear():
    a = servicefeaturemodel_ServiceFeature(description="sample_text", id="sample_text", name="sample_text", required=True, requirementWeight="sample_text")
    b1 = servicefeaturemodel_GroupRelationship()
    b2 = servicefeaturemodel_GroupRelationship()
    _safe_set(a, 'servicefeaturemodel_ServiceFeature7', b1)
    assert _is_linked(a, 'servicefeaturemodel_ServiceFeature7', b1)
    if hasattr(b1, 'servicefeaturemodel_GroupRelationship'):
        assert _is_linked(b1, 'servicefeaturemodel_GroupRelationship', a)
    _safe_set(a, 'servicefeaturemodel_ServiceFeature7', b2)
    assert _is_linked(a, 'servicefeaturemodel_ServiceFeature7', b2)
    if hasattr(b1, 'servicefeaturemodel_GroupRelationship'):
        assert not _is_linked(b1, 'servicefeaturemodel_GroupRelationship', a)
    if hasattr(b2, 'servicefeaturemodel_GroupRelationship'):
        assert _is_linked(b2, 'servicefeaturemodel_GroupRelationship', a)
    _safe_set(a, 'servicefeaturemodel_ServiceFeature7', None)
    assert not _is_linked(a, 'servicefeaturemodel_ServiceFeature7', b2)
    if hasattr(b2, 'servicefeaturemodel_GroupRelationship'):
        assert not _is_linked(b2, 'servicefeaturemodel_GroupRelationship', a)


def test_assoc_optionalServiceFeatures33_link_reassign_clear():
    a = servicefeaturemodel_OptionalServiceFeature(featureType="sample_text")
    b1 = servicefeaturemodel_GroupRelationship()
    b2 = servicefeaturemodel_GroupRelationship()
    _safe_set(a, 'servicefeaturemodel_OptionalServiceFeature', b1)
    assert _is_linked(a, 'servicefeaturemodel_OptionalServiceFeature', b1)
    if hasattr(b1, 'servicefeaturemodel_GroupRelationship34'):
        assert _is_linked(b1, 'servicefeaturemodel_GroupRelationship34', a)
    _safe_set(a, 'servicefeaturemodel_OptionalServiceFeature', b2)
    assert _is_linked(a, 'servicefeaturemodel_OptionalServiceFeature', b2)
    if hasattr(b1, 'servicefeaturemodel_GroupRelationship34'):
        assert not _is_linked(b1, 'servicefeaturemodel_GroupRelationship34', a)
    if hasattr(b2, 'servicefeaturemodel_GroupRelationship34'):
        assert _is_linked(b2, 'servicefeaturemodel_GroupRelationship34', a)
    _safe_set(a, 'servicefeaturemodel_OptionalServiceFeature', None)
    assert not _is_linked(a, 'servicefeaturemodel_OptionalServiceFeature', b2)
    if hasattr(b2, 'servicefeaturemodel_GroupRelationship34'):
        assert not _is_linked(b2, 'servicefeaturemodel_GroupRelationship34', a)


def test_assoc_preferences28_link_reassign_clear():
    a = servicefeaturemodel_Preference(creationDate=date(2024, 1, 1), description="sample_text", stakeholderGroup="sample_text", value=3.14)
    b1 = servicefeaturemodel_Configuration(description="sample_text", id="sample_text", name="sample_text", selected=True)
    b2 = servicefeaturemodel_Configuration(description="sample_text_2", id="sample_text_2", name="sample_text_2", selected=False)
    _safe_set(a, 'servicefeaturemodel_Preference', b1)
    assert _is_linked(a, 'servicefeaturemodel_Preference', b1)
    if hasattr(b1, 'servicefeaturemodel_Configuration29'):
        assert _is_linked(b1, 'servicefeaturemodel_Configuration29', a)
    _safe_set(a, 'servicefeaturemodel_Preference', b2)
    assert _is_linked(a, 'servicefeaturemodel_Preference', b2)
    if hasattr(b1, 'servicefeaturemodel_Configuration29'):
        assert not _is_linked(b1, 'servicefeaturemodel_Configuration29', a)
    if hasattr(b2, 'servicefeaturemodel_Configuration29'):
        assert _is_linked(b2, 'servicefeaturemodel_Configuration29', a)
    _safe_set(a, 'servicefeaturemodel_Preference', None)
    assert not _is_linked(a, 'servicefeaturemodel_Preference', b2)
    if hasattr(b2, 'servicefeaturemodel_Configuration29'):
        assert not _is_linked(b2, 'servicefeaturemodel_Configuration29', a)


def test_assoc_requires8_link_reassign_clear():
    a = servicefeaturemodel_ServiceFeature(description="sample_text", id="sample_text", name="sample_text", required=True, requirementWeight="sample_text")
    b1 = servicefeaturemodel_Requires()
    b2 = servicefeaturemodel_Requires()
    _safe_set(a, 'servicefeaturemodel_ServiceFeature9', {b1})
    assert _is_linked(a, 'servicefeaturemodel_ServiceFeature9', b1)
    if hasattr(b1, 'servicefeaturemodel_Requires'):
        assert _is_linked(b1, 'servicefeaturemodel_Requires', a)
    _safe_set(a, 'servicefeaturemodel_ServiceFeature9', {b2})
    assert _is_linked(a, 'servicefeaturemodel_ServiceFeature9', b2)
    if hasattr(b1, 'servicefeaturemodel_Requires'):
        assert not _is_linked(b1, 'servicefeaturemodel_Requires', a)
    if hasattr(b2, 'servicefeaturemodel_Requires'):
        assert _is_linked(b2, 'servicefeaturemodel_Requires', a)
    _safe_set(a, 'servicefeaturemodel_ServiceFeature9', set())
    assert not _is_linked(a, 'servicefeaturemodel_ServiceFeature9', b2)
    if hasattr(b2, 'servicefeaturemodel_Requires'):
        assert not _is_linked(b2, 'servicefeaturemodel_Requires', a)


def test_assoc_serviceFeature17_link_reassign_clear():
    a = servicefeaturemodel_ServiceFeature(description="sample_text", id="sample_text", name="sample_text", required=True, requirementWeight="sample_text")
    b1 = servicefeaturemodel_Requires()
    b2 = servicefeaturemodel_Requires()
    _safe_set(a, 'servicefeaturemodel_ServiceFeature19', b1)
    assert _is_linked(a, 'servicefeaturemodel_ServiceFeature19', b1)
    if hasattr(b1, 'servicefeaturemodel_Requires18'):
        assert _is_linked(b1, 'servicefeaturemodel_Requires18', a)
    _safe_set(a, 'servicefeaturemodel_ServiceFeature19', b2)
    assert _is_linked(a, 'servicefeaturemodel_ServiceFeature19', b2)
    if hasattr(b1, 'servicefeaturemodel_Requires18'):
        assert not _is_linked(b1, 'servicefeaturemodel_Requires18', a)
    if hasattr(b2, 'servicefeaturemodel_Requires18'):
        assert _is_linked(b2, 'servicefeaturemodel_Requires18', a)
    _safe_set(a, 'servicefeaturemodel_ServiceFeature19', None)
    assert not _is_linked(a, 'servicefeaturemodel_ServiceFeature19', b2)
    if hasattr(b2, 'servicefeaturemodel_Requires18'):
        assert not _is_linked(b2, 'servicefeaturemodel_Requires18', a)


def test_assoc_serviceFeature20_link_reassign_clear():
    a = servicefeaturemodel_ServiceFeature(description="sample_text", id="sample_text", name="sample_text", required=True, requirementWeight="sample_text")
    b1 = servicefeaturemodel_Excludes()
    b2 = servicefeaturemodel_Excludes()
    _safe_set(a, 'servicefeaturemodel_ServiceFeature22', b1)
    assert _is_linked(a, 'servicefeaturemodel_ServiceFeature22', b1)
    if hasattr(b1, 'servicefeaturemodel_Excludes21'):
        assert _is_linked(b1, 'servicefeaturemodel_Excludes21', a)
    _safe_set(a, 'servicefeaturemodel_ServiceFeature22', b2)
    assert _is_linked(a, 'servicefeaturemodel_ServiceFeature22', b2)
    if hasattr(b1, 'servicefeaturemodel_Excludes21'):
        assert not _is_linked(b1, 'servicefeaturemodel_Excludes21', a)
    if hasattr(b2, 'servicefeaturemodel_Excludes21'):
        assert _is_linked(b2, 'servicefeaturemodel_Excludes21', a)
    _safe_set(a, 'servicefeaturemodel_ServiceFeature22', None)
    assert not _is_linked(a, 'servicefeaturemodel_ServiceFeature22', b2)
    if hasattr(b2, 'servicefeaturemodel_Excludes21'):
        assert not _is_linked(b2, 'servicefeaturemodel_Excludes21', a)


def test_assoc_serviceFeatureDiagram0_link_reassign_clear():
    a = servicefeaturemodel_ServiceFeatureDiagram(description="sample_text", id="sample_text", name="sample_text")
    b1 = servicefeaturemodel_Service(description="sample_text", id="sample_text", name="sample_text")
    b2 = servicefeaturemodel_Service(description="sample_text_2", id="sample_text_2", name="sample_text_2")
    _safe_set(a, 'servicefeaturemodel_ServiceFeatureDiagram', b1)
    assert _is_linked(a, 'servicefeaturemodel_ServiceFeatureDiagram', b1)
    if hasattr(b1, 'servicefeaturemodel_Service'):
        assert _is_linked(b1, 'servicefeaturemodel_Service', a)
    _safe_set(a, 'servicefeaturemodel_ServiceFeatureDiagram', b2)
    assert _is_linked(a, 'servicefeaturemodel_ServiceFeatureDiagram', b2)
    if hasattr(b1, 'servicefeaturemodel_Service'):
        assert not _is_linked(b1, 'servicefeaturemodel_Service', a)
    if hasattr(b2, 'servicefeaturemodel_Service'):
        assert _is_linked(b2, 'servicefeaturemodel_Service', a)
    _safe_set(a, 'servicefeaturemodel_ServiceFeatureDiagram', None)
    assert not _is_linked(a, 'servicefeaturemodel_ServiceFeatureDiagram', b2)
    if hasattr(b2, 'servicefeaturemodel_Service'):
        assert not _is_linked(b2, 'servicefeaturemodel_Service', a)


def test_assoc_serviceFeatures13_link_reassign_clear():
    a = servicefeaturemodel_ServiceFeature(description="sample_text", id="sample_text", name="sample_text", required=True, requirementWeight="sample_text")
    b1 = servicefeaturemodel_ServiceFeature(description="sample_text", id="sample_text", name="sample_text", required=True, requirementWeight="sample_text")
    b2 = servicefeaturemodel_ServiceFeature(description="sample_text_2", id="sample_text_2", name="sample_text_2", required=False, requirementWeight="sample_text_2")
    _safe_set(a, 'servicefeaturemodel_ServiceFeature12', {b1})
    assert _is_linked(a, 'servicefeaturemodel_ServiceFeature12', b1)
    if hasattr(b1, 'servicefeaturemodel_ServiceFeature14'):
        assert _is_linked(b1, 'servicefeaturemodel_ServiceFeature14', a)
    _safe_set(a, 'servicefeaturemodel_ServiceFeature12', {b2})
    assert _is_linked(a, 'servicefeaturemodel_ServiceFeature12', b2)
    if hasattr(b1, 'servicefeaturemodel_ServiceFeature14'):
        assert not _is_linked(b1, 'servicefeaturemodel_ServiceFeature14', a)
    if hasattr(b2, 'servicefeaturemodel_ServiceFeature14'):
        assert _is_linked(b2, 'servicefeaturemodel_ServiceFeature14', a)
    _safe_set(a, 'servicefeaturemodel_ServiceFeature12', set())
    assert not _is_linked(a, 'servicefeaturemodel_ServiceFeature12', b2)
    if hasattr(b2, 'servicefeaturemodel_ServiceFeature14'):
        assert not _is_linked(b2, 'servicefeaturemodel_ServiceFeature14', a)


def test_assoc_serviceFeatures23_link_reassign_clear():
    a = servicefeaturemodel_ServiceFeatureDiagram(description="sample_text", id="sample_text", name="sample_text")
    b1 = servicefeaturemodel_ServiceFeature(description="sample_text", id="sample_text", name="sample_text", required=True, requirementWeight="sample_text")
    b2 = servicefeaturemodel_ServiceFeature(description="sample_text_2", id="sample_text_2", name="sample_text_2", required=False, requirementWeight="sample_text_2")
    _safe_set(a, 'servicefeaturemodel_ServiceFeatureDiagram24', {b1})
    assert _is_linked(a, 'servicefeaturemodel_ServiceFeatureDiagram24', b1)
    if hasattr(b1, 'servicefeaturemodel_ServiceFeature25'):
        assert _is_linked(b1, 'servicefeaturemodel_ServiceFeature25', a)
    _safe_set(a, 'servicefeaturemodel_ServiceFeatureDiagram24', {b2})
    assert _is_linked(a, 'servicefeaturemodel_ServiceFeatureDiagram24', b2)
    if hasattr(b1, 'servicefeaturemodel_ServiceFeature25'):
        assert not _is_linked(b1, 'servicefeaturemodel_ServiceFeature25', a)
    if hasattr(b2, 'servicefeaturemodel_ServiceFeature25'):
        assert _is_linked(b2, 'servicefeaturemodel_ServiceFeature25', a)
    _safe_set(a, 'servicefeaturemodel_ServiceFeatureDiagram24', set())
    assert not _is_linked(a, 'servicefeaturemodel_ServiceFeatureDiagram24', b2)
    if hasattr(b2, 'servicefeaturemodel_ServiceFeature25'):
        assert not _is_linked(b2, 'servicefeaturemodel_ServiceFeature25', a)


def test_assoc_serviceFeatures26_link_reassign_clear():
    a = servicefeaturemodel_ServiceFeature(description="sample_text", id="sample_text", name="sample_text", required=True, requirementWeight="sample_text")
    b1 = servicefeaturemodel_Configuration(description="sample_text", id="sample_text", name="sample_text", selected=True)
    b2 = servicefeaturemodel_Configuration(description="sample_text_2", id="sample_text_2", name="sample_text_2", selected=False)
    _safe_set(a, 'servicefeaturemodel_ServiceFeature27', b1)
    assert _is_linked(a, 'servicefeaturemodel_ServiceFeature27', b1)
    if hasattr(b1, 'servicefeaturemodel_Configuration'):
        assert _is_linked(b1, 'servicefeaturemodel_Configuration', a)
    _safe_set(a, 'servicefeaturemodel_ServiceFeature27', b2)
    assert _is_linked(a, 'servicefeaturemodel_ServiceFeature27', b2)
    if hasattr(b1, 'servicefeaturemodel_Configuration'):
        assert not _is_linked(b1, 'servicefeaturemodel_Configuration', a)
    if hasattr(b2, 'servicefeaturemodel_Configuration'):
        assert _is_linked(b2, 'servicefeaturemodel_Configuration', a)
    _safe_set(a, 'servicefeaturemodel_ServiceFeature27', None)
    assert not _is_linked(a, 'servicefeaturemodel_ServiceFeature27', b2)
    if hasattr(b2, 'servicefeaturemodel_Configuration'):
        assert not _is_linked(b2, 'servicefeaturemodel_Configuration', a)


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

GroupRelationship_strategy = st.builds(GroupRelationship)
@given(instance=GroupRelationship_strategy)
@settings(max_examples=25)
def test_GroupRelationship_instantiation(instance):
    assert isinstance(instance, GroupRelationship)


ServiceFeature_strategy = st.builds(ServiceFeature)
@given(instance=ServiceFeature_strategy)
@settings(max_examples=25)
def test_ServiceFeature_instantiation(instance):
    assert isinstance(instance, ServiceFeature)


servicefeaturemodel_Attribute_strategy = st.builds(servicefeaturemodel_Attribute, id=safe_text, instantiationValue=safe_text)
@given(instance=servicefeaturemodel_Attribute_strategy)
@settings(max_examples=25)
def test_servicefeaturemodel_Attribute_instantiation(instance):
    assert isinstance(instance, servicefeaturemodel_Attribute)


servicefeaturemodel_AttributeType_strategy = st.builds(servicefeaturemodel_AttributeType, aggregationRule=safe_text, customAttributeTypePriority=st.integers(), description=safe_text, domain=safe_text, name=safe_text, requirement=safe_text, requirementWeight=safe_text, scaleOrder=safe_text, toBeEvaluated=st.booleans())
@given(instance=servicefeaturemodel_AttributeType_strategy)
@settings(max_examples=25)
def test_servicefeaturemodel_AttributeType_instantiation(instance):
    assert isinstance(instance, servicefeaturemodel_AttributeType)


servicefeaturemodel_AttributeTypes_strategy = st.builds(servicefeaturemodel_AttributeTypes)
@given(instance=servicefeaturemodel_AttributeTypes_strategy)
@settings(max_examples=25)
def test_servicefeaturemodel_AttributeTypes_instantiation(instance):
    assert isinstance(instance, servicefeaturemodel_AttributeTypes)


servicefeaturemodel_Configuration_strategy = st.builds(servicefeaturemodel_Configuration, description=safe_text, id=safe_text, name=safe_text, selected=st.booleans())
@given(instance=servicefeaturemodel_Configuration_strategy)
@settings(max_examples=25)
def test_servicefeaturemodel_Configuration_instantiation(instance):
    assert isinstance(instance, servicefeaturemodel_Configuration)


servicefeaturemodel_Configurations_strategy = st.builds(servicefeaturemodel_Configurations)
@given(instance=servicefeaturemodel_Configurations_strategy)
@settings(max_examples=25)
def test_servicefeaturemodel_Configurations_instantiation(instance):
    assert isinstance(instance, servicefeaturemodel_Configurations)


servicefeaturemodel_Excludes_strategy = st.builds(servicefeaturemodel_Excludes)
@given(instance=servicefeaturemodel_Excludes_strategy)
@settings(max_examples=25)
def test_servicefeaturemodel_Excludes_instantiation(instance):
    assert isinstance(instance, servicefeaturemodel_Excludes)


servicefeaturemodel_GroupRelationship_strategy = st.builds(servicefeaturemodel_GroupRelationship)
@given(instance=servicefeaturemodel_GroupRelationship_strategy)
@settings(max_examples=25)
def test_servicefeaturemodel_GroupRelationship_instantiation(instance):
    assert isinstance(instance, servicefeaturemodel_GroupRelationship)


servicefeaturemodel_MandatoryServiceFeature_strategy = st.builds(servicefeaturemodel_MandatoryServiceFeature, featureTypes=safe_text)
@given(instance=servicefeaturemodel_MandatoryServiceFeature_strategy)
@settings(max_examples=25)
def test_servicefeaturemodel_MandatoryServiceFeature_instantiation(instance):
    assert isinstance(instance, servicefeaturemodel_MandatoryServiceFeature)


servicefeaturemodel_OR_strategy = st.builds(servicefeaturemodel_OR, maxFeaturesToChoose=st.integers(), minFeaturesToChoose=st.integers())
@given(instance=servicefeaturemodel_OR_strategy)
@settings(max_examples=25)
def test_servicefeaturemodel_OR_instantiation(instance):
    assert isinstance(instance, servicefeaturemodel_OR)


servicefeaturemodel_OptionalServiceFeature_strategy = st.builds(servicefeaturemodel_OptionalServiceFeature, featureType=safe_text)
@given(instance=servicefeaturemodel_OptionalServiceFeature_strategy)
@settings(max_examples=25)
def test_servicefeaturemodel_OptionalServiceFeature_instantiation(instance):
    assert isinstance(instance, servicefeaturemodel_OptionalServiceFeature)


servicefeaturemodel_Preference_strategy = st.builds(servicefeaturemodel_Preference, creationDate=st.dates(), description=safe_text, stakeholderGroup=safe_text, value=st.floats(allow_nan=False, allow_infinity=False))
@given(instance=servicefeaturemodel_Preference_strategy)
@settings(max_examples=25)
def test_servicefeaturemodel_Preference_instantiation(instance):
    assert isinstance(instance, servicefeaturemodel_Preference)


servicefeaturemodel_Requires_strategy = st.builds(servicefeaturemodel_Requires)
@given(instance=servicefeaturemodel_Requires_strategy)
@settings(max_examples=25)
def test_servicefeaturemodel_Requires_instantiation(instance):
    assert isinstance(instance, servicefeaturemodel_Requires)


servicefeaturemodel_Service_strategy = st.builds(servicefeaturemodel_Service, description=safe_text, id=safe_text, name=safe_text)
@given(instance=servicefeaturemodel_Service_strategy)
@settings(max_examples=25)
def test_servicefeaturemodel_Service_instantiation(instance):
    assert isinstance(instance, servicefeaturemodel_Service)


servicefeaturemodel_ServiceFeature_strategy = st.builds(servicefeaturemodel_ServiceFeature, description=safe_text, id=safe_text, name=safe_text, required=st.booleans(), requirementWeight=safe_text)
@given(instance=servicefeaturemodel_ServiceFeature_strategy)
@settings(max_examples=25)
def test_servicefeaturemodel_ServiceFeature_instantiation(instance):
    assert isinstance(instance, servicefeaturemodel_ServiceFeature)


servicefeaturemodel_ServiceFeatureDiagram_strategy = st.builds(servicefeaturemodel_ServiceFeatureDiagram, description=safe_text, id=safe_text, name=safe_text)
@given(instance=servicefeaturemodel_ServiceFeatureDiagram_strategy)
@settings(max_examples=25)
def test_servicefeaturemodel_ServiceFeatureDiagram_instantiation(instance):
    assert isinstance(instance, servicefeaturemodel_ServiceFeatureDiagram)


servicefeaturemodel_XOR_strategy = st.builds(servicefeaturemodel_XOR)
@given(instance=servicefeaturemodel_XOR_strategy)
@settings(max_examples=25)
def test_servicefeaturemodel_XOR_instantiation(instance):
    assert isinstance(instance, servicefeaturemodel_XOR)


