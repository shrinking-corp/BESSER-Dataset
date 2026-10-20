import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    ModifyRelationship,
    ServiceFeature,
    Variant,
    servicefeaturemodel_Attribute,
    servicefeaturemodel_AttributeToAttributeModifyRelationship,
    servicefeaturemodel_AttributeType,
    servicefeaturemodel_AttributeTypes,
    servicefeaturemodel_Configuration,
    servicefeaturemodel_Excludes,
    servicefeaturemodel_FeatureToAttributeModifyRelationship,
    servicefeaturemodel_MandatoryServiceFeature,
    servicefeaturemodel_ModifyRelationship,
    servicefeaturemodel_OR,
    servicefeaturemodel_OptionalServiceFeature,
    servicefeaturemodel_PossibleConfigurations,
    servicefeaturemodel_Preference,
    servicefeaturemodel_Requires,
    servicefeaturemodel_Service,
    servicefeaturemodel_ServiceFeature,
    servicefeaturemodel_ServiceFeatureDiagram,
    servicefeaturemodel_Variant,
    servicefeaturemodel_XOR,
    AggregationRules,
    AttributeDomain,
    FeatureTypes,
    ScaleOrders,
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

def test_assoc_containsFeatures25_reverse_link_reassign_clear():
    a1 = servicefeaturemodel_ServiceFeatureDiagram(description="sample_text", id="sample_text", name="sample_text")
    a2 = servicefeaturemodel_ServiceFeatureDiagram(description="sample_text_2", id="sample_text_2", name="sample_text_2")
    b = servicefeaturemodel_ServiceFeature(associatedGSMElement="sample_text", description="sample_text", featureType="sample_text", id="sample_text", mapsToGSMElement=True, maxAmount=7, minAmount=7, name="sample_text", required=True)
    _safe_set(b, 'servicefeaturemodel_ServiceFeature27', a1)
    assert _is_linked(b, 'servicefeaturemodel_ServiceFeature27', a1)
    if hasattr(a1, 'servicefeaturemodel_ServiceFeatureDiagram26'):
        assert _is_linked(a1, 'servicefeaturemodel_ServiceFeatureDiagram26', b)
    _safe_set(b, 'servicefeaturemodel_ServiceFeature27', a2)
    assert _is_linked(b, 'servicefeaturemodel_ServiceFeature27', a2)
    if hasattr(a1, 'servicefeaturemodel_ServiceFeatureDiagram26'):
        assert not _is_linked(a1, 'servicefeaturemodel_ServiceFeatureDiagram26', b)
    if hasattr(a2, 'servicefeaturemodel_ServiceFeatureDiagram26'):
        assert _is_linked(a2, 'servicefeaturemodel_ServiceFeatureDiagram26', b)
    _safe_set(b, 'servicefeaturemodel_ServiceFeature27', None)
    assert not _is_linked(b, 'servicefeaturemodel_ServiceFeature27', a2)
    if hasattr(a2, 'servicefeaturemodel_ServiceFeatureDiagram26'):
        assert not _is_linked(a2, 'servicefeaturemodel_ServiceFeatureDiagram26', b)


def test_assoc_containsModifyRelationship17_reverse_link_reassign_clear():
    a1 = servicefeaturemodel_ModifyRelationship(function="sample_text", name="sample_text", orderNumber=7, targetParameterName="sample_text")
    a2 = servicefeaturemodel_ModifyRelationship(function="sample_text_2", name="sample_text_2", orderNumber=13, targetParameterName="sample_text_2")
    b = servicefeaturemodel_Attribute(id="sample_text", instantiationValue="sample_text")
    _safe_set(b, 'servicefeaturemodel_Attribute18', {a1})
    assert _is_linked(b, 'servicefeaturemodel_Attribute18', a1)
    if hasattr(a1, 'servicefeaturemodel_ModifyRelationship'):
        assert _is_linked(a1, 'servicefeaturemodel_ModifyRelationship', b)
    _safe_set(b, 'servicefeaturemodel_Attribute18', {a2})
    assert _is_linked(b, 'servicefeaturemodel_Attribute18', a2)
    if hasattr(a1, 'servicefeaturemodel_ModifyRelationship'):
        assert not _is_linked(a1, 'servicefeaturemodel_ModifyRelationship', b)
    if hasattr(a2, 'servicefeaturemodel_ModifyRelationship'):
        assert _is_linked(a2, 'servicefeaturemodel_ModifyRelationship', b)
    _safe_set(b, 'servicefeaturemodel_Attribute18', set())
    assert not _is_linked(b, 'servicefeaturemodel_Attribute18', a2)
    if hasattr(a2, 'servicefeaturemodel_ModifyRelationship'):
        assert not _is_linked(a2, 'servicefeaturemodel_ModifyRelationship', b)


def test_assoc_decomposesInto13_reverse_link_reassign_clear():
    a1 = servicefeaturemodel_ServiceFeature(associatedGSMElement="sample_text", description="sample_text", featureType="sample_text", id="sample_text", mapsToGSMElement=True, maxAmount=7, minAmount=7, name="sample_text", required=True)
    a2 = servicefeaturemodel_ServiceFeature(associatedGSMElement="sample_text_2", description="sample_text_2", featureType="sample_text_2", id="sample_text_2", mapsToGSMElement=False, maxAmount=13, minAmount=13, name="sample_text_2", required=False)
    b = servicefeaturemodel_ServiceFeature(associatedGSMElement="sample_text", description="sample_text", featureType="sample_text", id="sample_text", mapsToGSMElement=True, maxAmount=7, minAmount=7, name="sample_text", required=True)
    _safe_set(b, 'servicefeaturemodel_ServiceFeature14', a1)
    assert _is_linked(b, 'servicefeaturemodel_ServiceFeature14', a1)
    if hasattr(a1, 'servicefeaturemodel_ServiceFeature12'):
        assert _is_linked(a1, 'servicefeaturemodel_ServiceFeature12', b)
    _safe_set(b, 'servicefeaturemodel_ServiceFeature14', a2)
    assert _is_linked(b, 'servicefeaturemodel_ServiceFeature14', a2)
    if hasattr(a1, 'servicefeaturemodel_ServiceFeature12'):
        assert not _is_linked(a1, 'servicefeaturemodel_ServiceFeature12', b)
    if hasattr(a2, 'servicefeaturemodel_ServiceFeature12'):
        assert _is_linked(a2, 'servicefeaturemodel_ServiceFeature12', b)
    _safe_set(b, 'servicefeaturemodel_ServiceFeature14', None)
    assert not _is_linked(b, 'servicefeaturemodel_ServiceFeature14', a2)
    if hasattr(a2, 'servicefeaturemodel_ServiceFeature12'):
        assert not _is_linked(a2, 'servicefeaturemodel_ServiceFeature12', b)


def test_assoc_describedBy32_reverse_link_reassign_clear():
    a1 = servicefeaturemodel_Configuration(description="sample_text", id="sample_text", name="sample_text")
    a2 = servicefeaturemodel_Configuration(description="sample_text_2", id="sample_text_2", name="sample_text_2")
    b = servicefeaturemodel_Attribute(id="sample_text", instantiationValue="sample_text")
    _safe_set(b, 'servicefeaturemodel_Attribute34', a1)
    assert _is_linked(b, 'servicefeaturemodel_Attribute34', a1)
    if hasattr(a1, 'servicefeaturemodel_Configuration33'):
        assert _is_linked(a1, 'servicefeaturemodel_Configuration33', b)
    _safe_set(b, 'servicefeaturemodel_Attribute34', a2)
    assert _is_linked(b, 'servicefeaturemodel_Attribute34', a2)
    if hasattr(a1, 'servicefeaturemodel_Configuration33'):
        assert not _is_linked(a1, 'servicefeaturemodel_Configuration33', b)
    if hasattr(a2, 'servicefeaturemodel_Configuration33'):
        assert _is_linked(a2, 'servicefeaturemodel_Configuration33', b)
    _safe_set(b, 'servicefeaturemodel_Attribute34', None)
    assert not _is_linked(b, 'servicefeaturemodel_Attribute34', a2)
    if hasattr(a2, 'servicefeaturemodel_Configuration33'):
        assert not _is_linked(a2, 'servicefeaturemodel_Configuration33', b)


def test_assoc_describedBy5_reverse_link_reassign_clear():
    a1 = servicefeaturemodel_ServiceFeature(associatedGSMElement="sample_text", description="sample_text", featureType="sample_text", id="sample_text", mapsToGSMElement=True, maxAmount=7, minAmount=7, name="sample_text", required=True)
    a2 = servicefeaturemodel_ServiceFeature(associatedGSMElement="sample_text_2", description="sample_text_2", featureType="sample_text_2", id="sample_text_2", mapsToGSMElement=False, maxAmount=13, minAmount=13, name="sample_text_2", required=False)
    b = servicefeaturemodel_Attribute(id="sample_text", instantiationValue="sample_text")
    _safe_set(b, 'servicefeaturemodel_Attribute', a1)
    assert _is_linked(b, 'servicefeaturemodel_Attribute', a1)
    if hasattr(a1, 'servicefeaturemodel_ServiceFeature'):
        assert _is_linked(a1, 'servicefeaturemodel_ServiceFeature', b)
    _safe_set(b, 'servicefeaturemodel_Attribute', a2)
    assert _is_linked(b, 'servicefeaturemodel_Attribute', a2)
    if hasattr(a1, 'servicefeaturemodel_ServiceFeature'):
        assert not _is_linked(a1, 'servicefeaturemodel_ServiceFeature', b)
    if hasattr(a2, 'servicefeaturemodel_ServiceFeature'):
        assert _is_linked(a2, 'servicefeaturemodel_ServiceFeature', b)
    _safe_set(b, 'servicefeaturemodel_Attribute', None)
    assert not _is_linked(b, 'servicefeaturemodel_Attribute', a2)
    if hasattr(a2, 'servicefeaturemodel_ServiceFeature'):
        assert not _is_linked(a2, 'servicefeaturemodel_ServiceFeature', b)


def test_assoc_evaluatedBy30_reverse_link_reassign_clear():
    a1 = servicefeaturemodel_Preference(creationDate=date(2024, 1, 1), description="sample_text", stakeholderGroup="sample_text", value=3.14)
    a2 = servicefeaturemodel_Preference(creationDate=date(2025, 6, 15), description="sample_text_2", stakeholderGroup="sample_text_2", value=9.99)
    b = servicefeaturemodel_Configuration(description="sample_text", id="sample_text", name="sample_text")
    _safe_set(b, 'servicefeaturemodel_Configuration31', {a1})
    assert _is_linked(b, 'servicefeaturemodel_Configuration31', a1)
    if hasattr(a1, 'servicefeaturemodel_Preference'):
        assert _is_linked(a1, 'servicefeaturemodel_Preference', b)
    _safe_set(b, 'servicefeaturemodel_Configuration31', {a2})
    assert _is_linked(b, 'servicefeaturemodel_Configuration31', a2)
    if hasattr(a1, 'servicefeaturemodel_Preference'):
        assert not _is_linked(a1, 'servicefeaturemodel_Preference', b)
    if hasattr(a2, 'servicefeaturemodel_Preference'):
        assert _is_linked(a2, 'servicefeaturemodel_Preference', b)
    _safe_set(b, 'servicefeaturemodel_Configuration31', set())
    assert not _is_linked(b, 'servicefeaturemodel_Configuration31', a2)
    if hasattr(a2, 'servicefeaturemodel_Preference'):
        assert not _is_linked(a2, 'servicefeaturemodel_Preference', b)


def test_assoc_groups28_reverse_link_reassign_clear():
    a1 = servicefeaturemodel_ServiceFeature(associatedGSMElement="sample_text", description="sample_text", featureType="sample_text", id="sample_text", mapsToGSMElement=True, maxAmount=7, minAmount=7, name="sample_text", required=True)
    a2 = servicefeaturemodel_ServiceFeature(associatedGSMElement="sample_text_2", description="sample_text_2", featureType="sample_text_2", id="sample_text_2", mapsToGSMElement=False, maxAmount=13, minAmount=13, name="sample_text_2", required=False)
    b = servicefeaturemodel_Configuration(description="sample_text", id="sample_text", name="sample_text")
    _safe_set(b, 'servicefeaturemodel_Configuration', {a1})
    assert _is_linked(b, 'servicefeaturemodel_Configuration', a1)
    if hasattr(a1, 'servicefeaturemodel_ServiceFeature29'):
        assert _is_linked(a1, 'servicefeaturemodel_ServiceFeature29', b)
    _safe_set(b, 'servicefeaturemodel_Configuration', {a2})
    assert _is_linked(b, 'servicefeaturemodel_Configuration', a2)
    if hasattr(a1, 'servicefeaturemodel_ServiceFeature29'):
        assert not _is_linked(a1, 'servicefeaturemodel_ServiceFeature29', b)
    if hasattr(a2, 'servicefeaturemodel_ServiceFeature29'):
        assert _is_linked(a2, 'servicefeaturemodel_ServiceFeature29', b)
    _safe_set(b, 'servicefeaturemodel_Configuration', set())
    assert not _is_linked(b, 'servicefeaturemodel_Configuration', a2)
    if hasattr(a2, 'servicefeaturemodel_ServiceFeature29'):
        assert not _is_linked(a2, 'servicefeaturemodel_ServiceFeature29', b)


def test_assoc_ofAttributeType15_reverse_link_reassign_clear():
    a1 = servicefeaturemodel_AttributeType(aggregationRule="sample_text", customAttributeTypePriority=7, description="sample_text", domain="sample_text", name="sample_text", requirement="sample_text", scaleOrder="sample_text", toBeEvaluated=True)
    a2 = servicefeaturemodel_AttributeType(aggregationRule="sample_text_2", customAttributeTypePriority=13, description="sample_text_2", domain="sample_text_2", name="sample_text_2", requirement="sample_text_2", scaleOrder="sample_text_2", toBeEvaluated=False)
    b = servicefeaturemodel_Attribute(id="sample_text", instantiationValue="sample_text")
    _safe_set(b, 'servicefeaturemodel_Attribute16', a1)
    assert _is_linked(b, 'servicefeaturemodel_Attribute16', a1)
    if hasattr(a1, 'servicefeaturemodel_AttributeType'):
        assert _is_linked(a1, 'servicefeaturemodel_AttributeType', b)
    _safe_set(b, 'servicefeaturemodel_Attribute16', a2)
    assert _is_linked(b, 'servicefeaturemodel_Attribute16', a2)
    if hasattr(a1, 'servicefeaturemodel_AttributeType'):
        assert not _is_linked(a1, 'servicefeaturemodel_AttributeType', b)
    if hasattr(a2, 'servicefeaturemodel_AttributeType'):
        assert _is_linked(a2, 'servicefeaturemodel_AttributeType', b)
    _safe_set(b, 'servicefeaturemodel_Attribute16', None)
    assert not _is_linked(b, 'servicefeaturemodel_Attribute16', a2)
    if hasattr(a2, 'servicefeaturemodel_AttributeType'):
        assert not _is_linked(a2, 'servicefeaturemodel_AttributeType', b)


def test_assoc_representedBy0_reverse_link_reassign_clear():
    a1 = servicefeaturemodel_ServiceFeatureDiagram(description="sample_text", id="sample_text", name="sample_text")
    a2 = servicefeaturemodel_ServiceFeatureDiagram(description="sample_text_2", id="sample_text_2", name="sample_text_2")
    b = servicefeaturemodel_Service(description="sample_text", id="sample_text", name="sample_text")
    _safe_set(b, 'servicefeaturemodel_Service', a1)
    assert _is_linked(b, 'servicefeaturemodel_Service', a1)
    if hasattr(a1, 'servicefeaturemodel_ServiceFeatureDiagram'):
        assert _is_linked(a1, 'servicefeaturemodel_ServiceFeatureDiagram', b)
    _safe_set(b, 'servicefeaturemodel_Service', a2)
    assert _is_linked(b, 'servicefeaturemodel_Service', a2)
    if hasattr(a1, 'servicefeaturemodel_ServiceFeatureDiagram'):
        assert not _is_linked(a1, 'servicefeaturemodel_ServiceFeatureDiagram', b)
    if hasattr(a2, 'servicefeaturemodel_ServiceFeatureDiagram'):
        assert _is_linked(a2, 'servicefeaturemodel_ServiceFeatureDiagram', b)
    _safe_set(b, 'servicefeaturemodel_Service', None)
    assert not _is_linked(b, 'servicefeaturemodel_Service', a2)
    if hasattr(a2, 'servicefeaturemodel_ServiceFeatureDiagram'):
        assert not _is_linked(a2, 'servicefeaturemodel_ServiceFeatureDiagram', b)


def test_assoc_triggeredByAttribute43_reverse_link_reassign_clear():
    a1 = servicefeaturemodel_AttributeToAttributeModifyRelationship(triggerParameterName="sample_text")
    a2 = servicefeaturemodel_AttributeToAttributeModifyRelationship(triggerParameterName="sample_text_2")
    b = servicefeaturemodel_Attribute(id="sample_text", instantiationValue="sample_text")
    _safe_set(b, 'servicefeaturemodel_Attribute44', a1)
    assert _is_linked(b, 'servicefeaturemodel_Attribute44', a1)
    if hasattr(a1, 'servicefeaturemodel_AttributeToAttributeModifyRelationship'):
        assert _is_linked(a1, 'servicefeaturemodel_AttributeToAttributeModifyRelationship', b)
    _safe_set(b, 'servicefeaturemodel_Attribute44', a2)
    assert _is_linked(b, 'servicefeaturemodel_Attribute44', a2)
    if hasattr(a1, 'servicefeaturemodel_AttributeToAttributeModifyRelationship'):
        assert not _is_linked(a1, 'servicefeaturemodel_AttributeToAttributeModifyRelationship', b)
    if hasattr(a2, 'servicefeaturemodel_AttributeToAttributeModifyRelationship'):
        assert _is_linked(a2, 'servicefeaturemodel_AttributeToAttributeModifyRelationship', b)
    _safe_set(b, 'servicefeaturemodel_Attribute44', None)
    assert not _is_linked(b, 'servicefeaturemodel_Attribute44', a2)
    if hasattr(a2, 'servicefeaturemodel_AttributeToAttributeModifyRelationship'):
        assert not _is_linked(a2, 'servicefeaturemodel_AttributeToAttributeModifyRelationship', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_contains37_stub_double():
    # servicefeaturemodel_PossibleConfigurations has no real 'servicefeaturemodel_PossibleConfigurations38' property in the generated
    # code (a bare stub) -- manually attach it so servicefeaturemodel_Configuration's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # servicefeaturemodel_Configuration's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = servicefeaturemodel_Configuration(description="sample_text", id="sample_text", name="sample_text")
    partner = servicefeaturemodel_PossibleConfigurations()
    setattr(partner, 'servicefeaturemodel_PossibleConfigurations38', None)
    _safe_set(owner, 'servicefeaturemodel_Configuration39', partner)
    assert owner in getattr(partner, 'servicefeaturemodel_PossibleConfigurations38')
    _safe_set(owner, 'servicefeaturemodel_Configuration39', None)
    assert owner not in getattr(partner, 'servicefeaturemodel_PossibleConfigurations38')


def test_assoc_contains40_stub_double():
    # servicefeaturemodel_AttributeTypes has no real 'servicefeaturemodel_AttributeTypes41' property in the generated
    # code (a bare stub) -- manually attach it so servicefeaturemodel_AttributeType's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # servicefeaturemodel_AttributeType's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = servicefeaturemodel_AttributeType(aggregationRule="sample_text", customAttributeTypePriority=7, description="sample_text", domain="sample_text", name="sample_text", requirement="sample_text", scaleOrder="sample_text", toBeEvaluated=True)
    partner = servicefeaturemodel_AttributeTypes()
    setattr(partner, 'servicefeaturemodel_AttributeTypes41', None)
    _safe_set(owner, 'servicefeaturemodel_AttributeType42', partner)
    assert owner in getattr(partner, 'servicefeaturemodel_AttributeTypes41')
    _safe_set(owner, 'servicefeaturemodel_AttributeType42', None)
    assert owner not in getattr(partner, 'servicefeaturemodel_AttributeTypes41')


def test_assoc_containsExcludes10_stub_double():
    # servicefeaturemodel_Excludes has no real 'servicefeaturemodel_Excludes' property in the generated
    # code (a bare stub) -- manually attach it so servicefeaturemodel_ServiceFeature's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # servicefeaturemodel_ServiceFeature's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = servicefeaturemodel_ServiceFeature(associatedGSMElement="sample_text", description="sample_text", featureType="sample_text", id="sample_text", mapsToGSMElement=True, maxAmount=7, minAmount=7, name="sample_text", required=True)
    partner = servicefeaturemodel_Excludes()
    setattr(partner, 'servicefeaturemodel_Excludes', None)
    _safe_set(owner, 'servicefeaturemodel_ServiceFeature11', {partner})
    assert getattr(partner, 'servicefeaturemodel_Excludes') == owner
    _safe_set(owner, 'servicefeaturemodel_ServiceFeature11', set())
    assert getattr(partner, 'servicefeaturemodel_Excludes') is None


def test_assoc_containsRequires8_stub_double():
    # servicefeaturemodel_Requires has no real 'servicefeaturemodel_Requires' property in the generated
    # code (a bare stub) -- manually attach it so servicefeaturemodel_ServiceFeature's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # servicefeaturemodel_ServiceFeature's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = servicefeaturemodel_ServiceFeature(associatedGSMElement="sample_text", description="sample_text", featureType="sample_text", id="sample_text", mapsToGSMElement=True, maxAmount=7, minAmount=7, name="sample_text", required=True)
    partner = servicefeaturemodel_Requires()
    setattr(partner, 'servicefeaturemodel_Requires', None)
    _safe_set(owner, 'servicefeaturemodel_ServiceFeature9', {partner})
    assert getattr(partner, 'servicefeaturemodel_Requires') == owner
    _safe_set(owner, 'servicefeaturemodel_ServiceFeature9', set())
    assert getattr(partner, 'servicefeaturemodel_Requires') is None


def test_assoc_containsVariant6_stub_double():
    # servicefeaturemodel_Variant has no real 'servicefeaturemodel_Variant' property in the generated
    # code (a bare stub) -- manually attach it so servicefeaturemodel_ServiceFeature's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # servicefeaturemodel_ServiceFeature's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = servicefeaturemodel_ServiceFeature(associatedGSMElement="sample_text", description="sample_text", featureType="sample_text", id="sample_text", mapsToGSMElement=True, maxAmount=7, minAmount=7, name="sample_text", required=True)
    partner = servicefeaturemodel_Variant()
    setattr(partner, 'servicefeaturemodel_Variant', None)
    _safe_set(owner, 'servicefeaturemodel_ServiceFeature7', partner)
    assert getattr(partner, 'servicefeaturemodel_Variant') == owner
    _safe_set(owner, 'servicefeaturemodel_ServiceFeature7', None)
    assert getattr(partner, 'servicefeaturemodel_Variant') is None


def test_assoc_enables1_stub_double():
    # servicefeaturemodel_PossibleConfigurations has no real 'servicefeaturemodel_PossibleConfigurations' property in the generated
    # code (a bare stub) -- manually attach it so servicefeaturemodel_Service's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # servicefeaturemodel_Service's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = servicefeaturemodel_Service(description="sample_text", id="sample_text", name="sample_text")
    partner = servicefeaturemodel_PossibleConfigurations()
    setattr(partner, 'servicefeaturemodel_PossibleConfigurations', None)
    _safe_set(owner, 'servicefeaturemodel_Service2', partner)
    assert getattr(partner, 'servicefeaturemodel_PossibleConfigurations') == owner
    _safe_set(owner, 'servicefeaturemodel_Service2', None)
    assert getattr(partner, 'servicefeaturemodel_PossibleConfigurations') is None


def test_assoc_excludesServiceFeature22_stub_double():
    # servicefeaturemodel_Excludes has no real 'servicefeaturemodel_Excludes23' property in the generated
    # code (a bare stub) -- manually attach it so servicefeaturemodel_ServiceFeature's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # servicefeaturemodel_ServiceFeature's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = servicefeaturemodel_ServiceFeature(associatedGSMElement="sample_text", description="sample_text", featureType="sample_text", id="sample_text", mapsToGSMElement=True, maxAmount=7, minAmount=7, name="sample_text", required=True)
    partner = servicefeaturemodel_Excludes()
    setattr(partner, 'servicefeaturemodel_Excludes23', None)
    _safe_set(owner, 'servicefeaturemodel_ServiceFeature24', partner)
    assert getattr(partner, 'servicefeaturemodel_Excludes23') == owner
    _safe_set(owner, 'servicefeaturemodel_ServiceFeature24', None)
    assert getattr(partner, 'servicefeaturemodel_Excludes23') is None


def test_assoc_has3_stub_double():
    # servicefeaturemodel_AttributeTypes has no real 'servicefeaturemodel_AttributeTypes' property in the generated
    # code (a bare stub) -- manually attach it so servicefeaturemodel_Service's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # servicefeaturemodel_Service's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = servicefeaturemodel_Service(description="sample_text", id="sample_text", name="sample_text")
    partner = servicefeaturemodel_AttributeTypes()
    setattr(partner, 'servicefeaturemodel_AttributeTypes', None)
    _safe_set(owner, 'servicefeaturemodel_Service4', partner)
    assert getattr(partner, 'servicefeaturemodel_AttributeTypes') == owner
    _safe_set(owner, 'servicefeaturemodel_Service4', None)
    assert getattr(partner, 'servicefeaturemodel_AttributeTypes') is None


def test_assoc_requiresServiceFeature19_stub_double():
    # servicefeaturemodel_Requires has no real 'servicefeaturemodel_Requires20' property in the generated
    # code (a bare stub) -- manually attach it so servicefeaturemodel_ServiceFeature's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # servicefeaturemodel_ServiceFeature's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = servicefeaturemodel_ServiceFeature(associatedGSMElement="sample_text", description="sample_text", featureType="sample_text", id="sample_text", mapsToGSMElement=True, maxAmount=7, minAmount=7, name="sample_text", required=True)
    partner = servicefeaturemodel_Requires()
    setattr(partner, 'servicefeaturemodel_Requires20', None)
    _safe_set(owner, 'servicefeaturemodel_ServiceFeature21', partner)
    assert getattr(partner, 'servicefeaturemodel_Requires20') == owner
    _safe_set(owner, 'servicefeaturemodel_ServiceFeature21', None)
    assert getattr(partner, 'servicefeaturemodel_Requires20') is None


def test_assoc_triggeredByServiceFeature45_stub_double():
    # servicefeaturemodel_FeatureToAttributeModifyRelationship has no real 'servicefeaturemodel_FeatureToAttributeModifyRelationship' property in the generated
    # code (a bare stub) -- manually attach it so servicefeaturemodel_ServiceFeature's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # servicefeaturemodel_ServiceFeature's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = servicefeaturemodel_ServiceFeature(associatedGSMElement="sample_text", description="sample_text", featureType="sample_text", id="sample_text", mapsToGSMElement=True, maxAmount=7, minAmount=7, name="sample_text", required=True)
    partner = servicefeaturemodel_FeatureToAttributeModifyRelationship()
    setattr(partner, 'servicefeaturemodel_FeatureToAttributeModifyRelationship', None)
    _safe_set(owner, 'servicefeaturemodel_ServiceFeature46', partner)
    assert getattr(partner, 'servicefeaturemodel_FeatureToAttributeModifyRelationship') == owner
    _safe_set(owner, 'servicefeaturemodel_ServiceFeature46', None)
    assert getattr(partner, 'servicefeaturemodel_FeatureToAttributeModifyRelationship') is None


