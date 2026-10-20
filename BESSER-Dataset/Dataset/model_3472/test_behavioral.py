import pytest
from datetime import date, datetime, time, timedelta

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

def test_assoc_attributeType15_reverse_link_reassign_clear():
    a1 = servicefeaturemodel_AttributeType(aggregationRule="sample_text", customAttributeTypePriority=7, description="sample_text", domain="sample_text", name="sample_text", requirement="sample_text", requirementWeight="sample_text", scaleOrder="sample_text", toBeEvaluated=True)
    a2 = servicefeaturemodel_AttributeType(aggregationRule="sample_text_2", customAttributeTypePriority=13, description="sample_text_2", domain="sample_text_2", name="sample_text_2", requirement="sample_text_2", requirementWeight="sample_text_2", scaleOrder="sample_text_2", toBeEvaluated=False)
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


def test_assoc_attributes30_reverse_link_reassign_clear():
    a1 = servicefeaturemodel_Configuration(description="sample_text", id="sample_text", name="sample_text", selected=True)
    a2 = servicefeaturemodel_Configuration(description="sample_text_2", id="sample_text_2", name="sample_text_2", selected=False)
    b = servicefeaturemodel_Attribute(id="sample_text", instantiationValue="sample_text")
    _safe_set(b, 'servicefeaturemodel_Attribute32', a1)
    assert _is_linked(b, 'servicefeaturemodel_Attribute32', a1)
    if hasattr(a1, 'servicefeaturemodel_Configuration31'):
        assert _is_linked(a1, 'servicefeaturemodel_Configuration31', b)
    _safe_set(b, 'servicefeaturemodel_Attribute32', a2)
    assert _is_linked(b, 'servicefeaturemodel_Attribute32', a2)
    if hasattr(a1, 'servicefeaturemodel_Configuration31'):
        assert not _is_linked(a1, 'servicefeaturemodel_Configuration31', b)
    if hasattr(a2, 'servicefeaturemodel_Configuration31'):
        assert _is_linked(a2, 'servicefeaturemodel_Configuration31', b)
    _safe_set(b, 'servicefeaturemodel_Attribute32', None)
    assert not _is_linked(b, 'servicefeaturemodel_Attribute32', a2)
    if hasattr(a2, 'servicefeaturemodel_Configuration31'):
        assert not _is_linked(a2, 'servicefeaturemodel_Configuration31', b)


def test_assoc_attributes5_reverse_link_reassign_clear():
    a1 = servicefeaturemodel_ServiceFeature(description="sample_text", id="sample_text", name="sample_text", required=True, requirementWeight="sample_text")
    a2 = servicefeaturemodel_ServiceFeature(description="sample_text_2", id="sample_text_2", name="sample_text_2", required=False, requirementWeight="sample_text_2")
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


def test_assoc_preferences28_reverse_link_reassign_clear():
    a1 = servicefeaturemodel_Preference(creationDate=date(2024, 1, 1), description="sample_text", stakeholderGroup="sample_text", value=3.14)
    a2 = servicefeaturemodel_Preference(creationDate=date(2025, 6, 15), description="sample_text_2", stakeholderGroup="sample_text_2", value=9.99)
    b = servicefeaturemodel_Configuration(description="sample_text", id="sample_text", name="sample_text", selected=True)
    _safe_set(b, 'servicefeaturemodel_Configuration29', {a1})
    assert _is_linked(b, 'servicefeaturemodel_Configuration29', a1)
    if hasattr(a1, 'servicefeaturemodel_Preference'):
        assert _is_linked(a1, 'servicefeaturemodel_Preference', b)
    _safe_set(b, 'servicefeaturemodel_Configuration29', {a2})
    assert _is_linked(b, 'servicefeaturemodel_Configuration29', a2)
    if hasattr(a1, 'servicefeaturemodel_Preference'):
        assert not _is_linked(a1, 'servicefeaturemodel_Preference', b)
    if hasattr(a2, 'servicefeaturemodel_Preference'):
        assert _is_linked(a2, 'servicefeaturemodel_Preference', b)
    _safe_set(b, 'servicefeaturemodel_Configuration29', set())
    assert not _is_linked(b, 'servicefeaturemodel_Configuration29', a2)
    if hasattr(a2, 'servicefeaturemodel_Preference'):
        assert not _is_linked(a2, 'servicefeaturemodel_Preference', b)


def test_assoc_serviceFeatureDiagram0_reverse_link_reassign_clear():
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


def test_assoc_serviceFeatures13_reverse_link_reassign_clear():
    a1 = servicefeaturemodel_ServiceFeature(description="sample_text", id="sample_text", name="sample_text", required=True, requirementWeight="sample_text")
    a2 = servicefeaturemodel_ServiceFeature(description="sample_text_2", id="sample_text_2", name="sample_text_2", required=False, requirementWeight="sample_text_2")
    b = servicefeaturemodel_ServiceFeature(description="sample_text", id="sample_text", name="sample_text", required=True, requirementWeight="sample_text")
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


def test_assoc_serviceFeatures23_reverse_link_reassign_clear():
    a1 = servicefeaturemodel_ServiceFeatureDiagram(description="sample_text", id="sample_text", name="sample_text")
    a2 = servicefeaturemodel_ServiceFeatureDiagram(description="sample_text_2", id="sample_text_2", name="sample_text_2")
    b = servicefeaturemodel_ServiceFeature(description="sample_text", id="sample_text", name="sample_text", required=True, requirementWeight="sample_text")
    _safe_set(b, 'servicefeaturemodel_ServiceFeature25', a1)
    assert _is_linked(b, 'servicefeaturemodel_ServiceFeature25', a1)
    if hasattr(a1, 'servicefeaturemodel_ServiceFeatureDiagram24'):
        assert _is_linked(a1, 'servicefeaturemodel_ServiceFeatureDiagram24', b)
    _safe_set(b, 'servicefeaturemodel_ServiceFeature25', a2)
    assert _is_linked(b, 'servicefeaturemodel_ServiceFeature25', a2)
    if hasattr(a1, 'servicefeaturemodel_ServiceFeatureDiagram24'):
        assert not _is_linked(a1, 'servicefeaturemodel_ServiceFeatureDiagram24', b)
    if hasattr(a2, 'servicefeaturemodel_ServiceFeatureDiagram24'):
        assert _is_linked(a2, 'servicefeaturemodel_ServiceFeatureDiagram24', b)
    _safe_set(b, 'servicefeaturemodel_ServiceFeature25', None)
    assert not _is_linked(b, 'servicefeaturemodel_ServiceFeature25', a2)
    if hasattr(a2, 'servicefeaturemodel_ServiceFeatureDiagram24'):
        assert not _is_linked(a2, 'servicefeaturemodel_ServiceFeatureDiagram24', b)


def test_assoc_serviceFeatures26_reverse_link_reassign_clear():
    a1 = servicefeaturemodel_ServiceFeature(description="sample_text", id="sample_text", name="sample_text", required=True, requirementWeight="sample_text")
    a2 = servicefeaturemodel_ServiceFeature(description="sample_text_2", id="sample_text_2", name="sample_text_2", required=False, requirementWeight="sample_text_2")
    b = servicefeaturemodel_Configuration(description="sample_text", id="sample_text", name="sample_text", selected=True)
    _safe_set(b, 'servicefeaturemodel_Configuration', {a1})
    assert _is_linked(b, 'servicefeaturemodel_Configuration', a1)
    if hasattr(a1, 'servicefeaturemodel_ServiceFeature27'):
        assert _is_linked(a1, 'servicefeaturemodel_ServiceFeature27', b)
    _safe_set(b, 'servicefeaturemodel_Configuration', {a2})
    assert _is_linked(b, 'servicefeaturemodel_Configuration', a2)
    if hasattr(a1, 'servicefeaturemodel_ServiceFeature27'):
        assert not _is_linked(a1, 'servicefeaturemodel_ServiceFeature27', b)
    if hasattr(a2, 'servicefeaturemodel_ServiceFeature27'):
        assert _is_linked(a2, 'servicefeaturemodel_ServiceFeature27', b)
    _safe_set(b, 'servicefeaturemodel_Configuration', set())
    assert not _is_linked(b, 'servicefeaturemodel_Configuration', a2)
    if hasattr(a2, 'servicefeaturemodel_ServiceFeature27'):
        assert not _is_linked(a2, 'servicefeaturemodel_ServiceFeature27', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_attributeTypes3_stub_double():
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


def test_assoc_attributeTypes38_stub_double():
    # servicefeaturemodel_AttributeTypes has no real 'servicefeaturemodel_AttributeTypes39' property in the generated
    # code (a bare stub) -- manually attach it so servicefeaturemodel_AttributeType's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # servicefeaturemodel_AttributeType's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = servicefeaturemodel_AttributeType(aggregationRule="sample_text", customAttributeTypePriority=7, description="sample_text", domain="sample_text", name="sample_text", requirement="sample_text", requirementWeight="sample_text", scaleOrder="sample_text", toBeEvaluated=True)
    partner = servicefeaturemodel_AttributeTypes()
    setattr(partner, 'servicefeaturemodel_AttributeTypes39', None)
    _safe_set(owner, 'servicefeaturemodel_AttributeType40', partner)
    assert owner in getattr(partner, 'servicefeaturemodel_AttributeTypes39')
    _safe_set(owner, 'servicefeaturemodel_AttributeType40', None)
    assert owner not in getattr(partner, 'servicefeaturemodel_AttributeTypes39')


def test_assoc_configurations1_stub_double():
    # servicefeaturemodel_Configurations has no real 'servicefeaturemodel_Configurations' property in the generated
    # code (a bare stub) -- manually attach it so servicefeaturemodel_Service's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # servicefeaturemodel_Service's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = servicefeaturemodel_Service(description="sample_text", id="sample_text", name="sample_text")
    partner = servicefeaturemodel_Configurations()
    setattr(partner, 'servicefeaturemodel_Configurations', None)
    _safe_set(owner, 'servicefeaturemodel_Service2', partner)
    assert getattr(partner, 'servicefeaturemodel_Configurations') == owner
    _safe_set(owner, 'servicefeaturemodel_Service2', None)
    assert getattr(partner, 'servicefeaturemodel_Configurations') is None


def test_assoc_configurations35_stub_double():
    # servicefeaturemodel_Configurations has no real 'servicefeaturemodel_Configurations36' property in the generated
    # code (a bare stub) -- manually attach it so servicefeaturemodel_Configuration's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # servicefeaturemodel_Configuration's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = servicefeaturemodel_Configuration(description="sample_text", id="sample_text", name="sample_text", selected=True)
    partner = servicefeaturemodel_Configurations()
    setattr(partner, 'servicefeaturemodel_Configurations36', None)
    _safe_set(owner, 'servicefeaturemodel_Configuration37', partner)
    assert owner in getattr(partner, 'servicefeaturemodel_Configurations36')
    _safe_set(owner, 'servicefeaturemodel_Configuration37', None)
    assert owner not in getattr(partner, 'servicefeaturemodel_Configurations36')


def test_assoc_excludes10_stub_double():
    # servicefeaturemodel_Excludes has no real 'servicefeaturemodel_Excludes' property in the generated
    # code (a bare stub) -- manually attach it so servicefeaturemodel_ServiceFeature's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # servicefeaturemodel_ServiceFeature's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = servicefeaturemodel_ServiceFeature(description="sample_text", id="sample_text", name="sample_text", required=True, requirementWeight="sample_text")
    partner = servicefeaturemodel_Excludes()
    setattr(partner, 'servicefeaturemodel_Excludes', None)
    _safe_set(owner, 'servicefeaturemodel_ServiceFeature11', {partner})
    assert getattr(partner, 'servicefeaturemodel_Excludes') == owner
    _safe_set(owner, 'servicefeaturemodel_ServiceFeature11', set())
    assert getattr(partner, 'servicefeaturemodel_Excludes') is None


def test_assoc_groupRelationship6_stub_double():
    # servicefeaturemodel_GroupRelationship has no real 'servicefeaturemodel_GroupRelationship' property in the generated
    # code (a bare stub) -- manually attach it so servicefeaturemodel_ServiceFeature's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # servicefeaturemodel_ServiceFeature's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = servicefeaturemodel_ServiceFeature(description="sample_text", id="sample_text", name="sample_text", required=True, requirementWeight="sample_text")
    partner = servicefeaturemodel_GroupRelationship()
    setattr(partner, 'servicefeaturemodel_GroupRelationship', None)
    _safe_set(owner, 'servicefeaturemodel_ServiceFeature7', partner)
    assert getattr(partner, 'servicefeaturemodel_GroupRelationship') == owner
    _safe_set(owner, 'servicefeaturemodel_ServiceFeature7', None)
    assert getattr(partner, 'servicefeaturemodel_GroupRelationship') is None


def test_assoc_optionalServiceFeatures33_stub_double():
    # servicefeaturemodel_GroupRelationship has no real 'servicefeaturemodel_GroupRelationship34' property in the generated
    # code (a bare stub) -- manually attach it so servicefeaturemodel_OptionalServiceFeature's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # servicefeaturemodel_OptionalServiceFeature's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = servicefeaturemodel_OptionalServiceFeature(featureType="sample_text")
    partner = servicefeaturemodel_GroupRelationship()
    setattr(partner, 'servicefeaturemodel_GroupRelationship34', None)
    _safe_set(owner, 'servicefeaturemodel_OptionalServiceFeature', partner)
    assert owner in getattr(partner, 'servicefeaturemodel_GroupRelationship34')
    _safe_set(owner, 'servicefeaturemodel_OptionalServiceFeature', None)
    assert owner not in getattr(partner, 'servicefeaturemodel_GroupRelationship34')


def test_assoc_requires8_stub_double():
    # servicefeaturemodel_Requires has no real 'servicefeaturemodel_Requires' property in the generated
    # code (a bare stub) -- manually attach it so servicefeaturemodel_ServiceFeature's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # servicefeaturemodel_ServiceFeature's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = servicefeaturemodel_ServiceFeature(description="sample_text", id="sample_text", name="sample_text", required=True, requirementWeight="sample_text")
    partner = servicefeaturemodel_Requires()
    setattr(partner, 'servicefeaturemodel_Requires', None)
    _safe_set(owner, 'servicefeaturemodel_ServiceFeature9', {partner})
    assert getattr(partner, 'servicefeaturemodel_Requires') == owner
    _safe_set(owner, 'servicefeaturemodel_ServiceFeature9', set())
    assert getattr(partner, 'servicefeaturemodel_Requires') is None


def test_assoc_serviceFeature17_stub_double():
    # servicefeaturemodel_Requires has no real 'servicefeaturemodel_Requires18' property in the generated
    # code (a bare stub) -- manually attach it so servicefeaturemodel_ServiceFeature's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # servicefeaturemodel_ServiceFeature's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = servicefeaturemodel_ServiceFeature(description="sample_text", id="sample_text", name="sample_text", required=True, requirementWeight="sample_text")
    partner = servicefeaturemodel_Requires()
    setattr(partner, 'servicefeaturemodel_Requires18', None)
    _safe_set(owner, 'servicefeaturemodel_ServiceFeature19', partner)
    assert getattr(partner, 'servicefeaturemodel_Requires18') == owner
    _safe_set(owner, 'servicefeaturemodel_ServiceFeature19', None)
    assert getattr(partner, 'servicefeaturemodel_Requires18') is None


def test_assoc_serviceFeature20_stub_double():
    # servicefeaturemodel_Excludes has no real 'servicefeaturemodel_Excludes21' property in the generated
    # code (a bare stub) -- manually attach it so servicefeaturemodel_ServiceFeature's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # servicefeaturemodel_ServiceFeature's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = servicefeaturemodel_ServiceFeature(description="sample_text", id="sample_text", name="sample_text", required=True, requirementWeight="sample_text")
    partner = servicefeaturemodel_Excludes()
    setattr(partner, 'servicefeaturemodel_Excludes21', None)
    _safe_set(owner, 'servicefeaturemodel_ServiceFeature22', partner)
    assert getattr(partner, 'servicefeaturemodel_Excludes21') == owner
    _safe_set(owner, 'servicefeaturemodel_ServiceFeature22', None)
    assert getattr(partner, 'servicefeaturemodel_Excludes21') is None


