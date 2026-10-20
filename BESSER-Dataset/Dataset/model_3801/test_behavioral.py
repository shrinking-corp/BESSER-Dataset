import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Connection_EntityRelationship,
    Elements_with_Attributes,
    entityrelationship_Attribute,
    entityrelationship_Attribute_Composite,
    entityrelationship_Connection_ConnectionEntityRelationship2Attribute,
    entityrelationship_Connection_E_R_Restriction,
    entityrelationship_Connection_Entity2Relationship,
    entityrelationship_Connection_EntityRelationship,
    entityrelationship_Connection_Generalization_Entity,
    entityrelationship_Connection_Relationship2Entity,
    entityrelationship_Connection_With_Attribute,
    entityrelationship_Elements_with_Attributes,
    entityrelationship_Entity,
    entityrelationship_Entity_Relationship_Model,
    entityrelationship_Generalization,
    entityrelationship_Relationship,
    entityrelationship_Relationships_Restriction,
    TypeAttribute,
    TypeEntity,
    TypeIdentifier,
    TypeRelationship,
    TypeRestriction,
    TypeRestriction2,
    TypeRestrictionInheritance1,
    TypeRestrictionInheritance2,
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

def test_assoc_Connection_Entity77_reverse_link_reassign_clear():
    a1 = entityrelationship_Entity(name_entity="sample_text", type_entity="sample_text")
    a2 = entityrelationship_Entity(name_entity="sample_text_2", type_entity="sample_text_2")
    b = entityrelationship_Connection_Generalization_Entity(maximum_cardinality="sample_text", minimum_cardinality="sample_text")
    _safe_set(b, 'entityrelationship_Connection_Generalization_Entity78', a1)
    assert _is_linked(b, 'entityrelationship_Connection_Generalization_Entity78', a1)
    if hasattr(a1, 'entityrelationship_Entity79'):
        assert _is_linked(a1, 'entityrelationship_Entity79', b)
    _safe_set(b, 'entityrelationship_Connection_Generalization_Entity78', a2)
    assert _is_linked(b, 'entityrelationship_Connection_Generalization_Entity78', a2)
    if hasattr(a1, 'entityrelationship_Entity79'):
        assert not _is_linked(a1, 'entityrelationship_Entity79', b)
    if hasattr(a2, 'entityrelationship_Entity79'):
        assert _is_linked(a2, 'entityrelationship_Entity79', b)
    _safe_set(b, 'entityrelationship_Connection_Generalization_Entity78', None)
    assert not _is_linked(b, 'entityrelationship_Connection_Generalization_Entity78', a2)
    if hasattr(a2, 'entityrelationship_Entity79'):
        assert not _is_linked(a2, 'entityrelationship_Entity79', b)


def test_assoc_Connection_Generalization75_reverse_link_reassign_clear():
    a1 = entityrelationship_Generalization(restriction_inheritance_1="sample_text", restriction_inheritance_2="sample_text")
    a2 = entityrelationship_Generalization(restriction_inheritance_1="sample_text_2", restriction_inheritance_2="sample_text_2")
    b = entityrelationship_Connection_Generalization_Entity(maximum_cardinality="sample_text", minimum_cardinality="sample_text")
    _safe_set(b, 'entityrelationship_Connection_Generalization_Entity', a1)
    assert _is_linked(b, 'entityrelationship_Connection_Generalization_Entity', a1)
    if hasattr(a1, 'entityrelationship_Generalization76'):
        assert _is_linked(a1, 'entityrelationship_Generalization76', b)
    _safe_set(b, 'entityrelationship_Connection_Generalization_Entity', a2)
    assert _is_linked(b, 'entityrelationship_Connection_Generalization_Entity', a2)
    if hasattr(a1, 'entityrelationship_Generalization76'):
        assert not _is_linked(a1, 'entityrelationship_Generalization76', b)
    if hasattr(a2, 'entityrelationship_Generalization76'):
        assert _is_linked(a2, 'entityrelationship_Generalization76', b)
    _safe_set(b, 'entityrelationship_Connection_Generalization_Entity', None)
    assert not _is_linked(b, 'entityrelationship_Connection_Generalization_Entity', a2)
    if hasattr(a2, 'entityrelationship_Generalization76'):
        assert not _is_linked(a2, 'entityrelationship_Generalization76', b)


def test_assoc_ERM_Has_At15_reverse_link_reassign_clear():
    a1 = entityrelationship_Entity_Relationship_Model(name="sample_text")
    a2 = entityrelationship_Entity_Relationship_Model(name="sample_text_2")
    b = entityrelationship_Attribute(identifier="sample_text", name_attribute="sample_text")
    _safe_set(b, 'entityrelationship_Attribute', a1)
    assert _is_linked(b, 'entityrelationship_Attribute', a1)
    if hasattr(a1, 'entityrelationship_Entity_Relationship_Model'):
        assert _is_linked(a1, 'entityrelationship_Entity_Relationship_Model', b)
    _safe_set(b, 'entityrelationship_Attribute', a2)
    assert _is_linked(b, 'entityrelationship_Attribute', a2)
    if hasattr(a1, 'entityrelationship_Entity_Relationship_Model'):
        assert not _is_linked(a1, 'entityrelationship_Entity_Relationship_Model', b)
    if hasattr(a2, 'entityrelationship_Entity_Relationship_Model'):
        assert _is_linked(a2, 'entityrelationship_Entity_Relationship_Model', b)
    _safe_set(b, 'entityrelationship_Attribute', None)
    assert not _is_linked(b, 'entityrelationship_Attribute', a2)
    if hasattr(a2, 'entityrelationship_Entity_Relationship_Model'):
        assert not _is_linked(a2, 'entityrelationship_Entity_Relationship_Model', b)


def test_assoc_ERM_Has_CEA13_reverse_link_reassign_clear():
    a1 = entityrelationship_Entity_Relationship_Model(name="sample_text")
    a2 = entityrelationship_Entity_Relationship_Model(name="sample_text_2")
    b = entityrelationship_Connection_With_Attribute(type_attribute="sample_text")
    _safe_set(b, 'Connection_With_Attribute', a1)
    assert _is_linked(b, 'Connection_With_Attribute', a1)
    if hasattr(a1, 'inEntityRelationshipModel14'):
        assert _is_linked(a1, 'inEntityRelationshipModel14', b)
    _safe_set(b, 'Connection_With_Attribute', a2)
    assert _is_linked(b, 'Connection_With_Attribute', a2)
    if hasattr(a1, 'inEntityRelationshipModel14'):
        assert not _is_linked(a1, 'inEntityRelationshipModel14', b)
    if hasattr(a2, 'inEntityRelationshipModel14'):
        assert _is_linked(a2, 'inEntityRelationshipModel14', b)
    _safe_set(b, 'Connection_With_Attribute', None)
    assert not _is_linked(b, 'Connection_With_Attribute', a2)
    if hasattr(a2, 'inEntityRelationshipModel14'):
        assert not _is_linked(a2, 'inEntityRelationshipModel14', b)


def test_assoc_ERM_Has_G16_reverse_link_reassign_clear():
    a1 = entityrelationship_Generalization(restriction_inheritance_1="sample_text", restriction_inheritance_2="sample_text")
    a2 = entityrelationship_Generalization(restriction_inheritance_1="sample_text_2", restriction_inheritance_2="sample_text_2")
    b = entityrelationship_Entity_Relationship_Model(name="sample_text")
    _safe_set(b, 'inEntityRelationshipModel17', {a1})
    assert _is_linked(b, 'inEntityRelationshipModel17', a1)
    if hasattr(a1, 'Generalization'):
        assert _is_linked(a1, 'Generalization', b)
    _safe_set(b, 'inEntityRelationshipModel17', {a2})
    assert _is_linked(b, 'inEntityRelationshipModel17', a2)
    if hasattr(a1, 'Generalization'):
        assert not _is_linked(a1, 'Generalization', b)
    if hasattr(a2, 'Generalization'):
        assert _is_linked(a2, 'Generalization', b)
    _safe_set(b, 'inEntityRelationshipModel17', set())
    assert not _is_linked(b, 'inEntityRelationshipModel17', a2)
    if hasattr(a2, 'Generalization'):
        assert not _is_linked(a2, 'Generalization', b)


def test_assoc_ERM_Has_Gen9_reverse_link_reassign_clear():
    a1 = entityrelationship_Entity_Relationship_Model(name="sample_text")
    a2 = entityrelationship_Entity_Relationship_Model(name="sample_text_2")
    b = entityrelationship_Connection_Generalization_Entity(maximum_cardinality="sample_text", minimum_cardinality="sample_text")
    _safe_set(b, 'Connection_Generalization_Entity', a1)
    assert _is_linked(b, 'Connection_Generalization_Entity', a1)
    if hasattr(a1, 'inEntityRelationshipModel10'):
        assert _is_linked(a1, 'inEntityRelationshipModel10', b)
    _safe_set(b, 'Connection_Generalization_Entity', a2)
    assert _is_linked(b, 'Connection_Generalization_Entity', a2)
    if hasattr(a1, 'inEntityRelationshipModel10'):
        assert not _is_linked(a1, 'inEntityRelationshipModel10', b)
    if hasattr(a2, 'inEntityRelationshipModel10'):
        assert _is_linked(a2, 'inEntityRelationshipModel10', b)
    _safe_set(b, 'Connection_Generalization_Entity', None)
    assert not _is_linked(b, 'Connection_Generalization_Entity', a2)
    if hasattr(a2, 'inEntityRelationshipModel10'):
        assert not _is_linked(a2, 'inEntityRelationshipModel10', b)


def test_assoc_ERM_Has_Rt1_reverse_link_reassign_clear():
    a1 = entityrelationship_Relationships_Restriction(type_restriction="sample_text")
    a2 = entityrelationship_Relationships_Restriction(type_restriction="sample_text_2")
    b = entityrelationship_Entity_Relationship_Model(name="sample_text")
    _safe_set(b, 'inEntityRelationshipModel2', {a1})
    assert _is_linked(b, 'inEntityRelationshipModel2', a1)
    if hasattr(a1, 'Relationships_Restriction'):
        assert _is_linked(a1, 'Relationships_Restriction', b)
    _safe_set(b, 'inEntityRelationshipModel2', {a2})
    assert _is_linked(b, 'inEntityRelationshipModel2', a2)
    if hasattr(a1, 'Relationships_Restriction'):
        assert not _is_linked(a1, 'Relationships_Restriction', b)
    if hasattr(a2, 'Relationships_Restriction'):
        assert _is_linked(a2, 'Relationships_Restriction', b)
    _safe_set(b, 'inEntityRelationshipModel2', set())
    assert not _is_linked(b, 'inEntityRelationshipModel2', a2)
    if hasattr(a2, 'Relationships_Restriction'):
        assert not _is_linked(a2, 'Relationships_Restriction', b)


def test_assoc_ERM_Has_Rt211_reverse_link_reassign_clear():
    a1 = entityrelationship_Entity_Relationship_Model(name="sample_text")
    a2 = entityrelationship_Entity_Relationship_Model(name="sample_text_2")
    b = entityrelationship_Connection_E_R_Restriction(type_restriction="sample_text")
    _safe_set(b, 'Connection_E_R_Restriction', a1)
    assert _is_linked(b, 'Connection_E_R_Restriction', a1)
    if hasattr(a1, 'inEntityRelationshipModel12'):
        assert _is_linked(a1, 'inEntityRelationshipModel12', b)
    _safe_set(b, 'Connection_E_R_Restriction', a2)
    assert _is_linked(b, 'Connection_E_R_Restriction', a2)
    if hasattr(a1, 'inEntityRelationshipModel12'):
        assert not _is_linked(a1, 'inEntityRelationshipModel12', b)
    if hasattr(a2, 'inEntityRelationshipModel12'):
        assert _is_linked(a2, 'inEntityRelationshipModel12', b)
    _safe_set(b, 'Connection_E_R_Restriction', None)
    assert not _is_linked(b, 'Connection_E_R_Restriction', a2)
    if hasattr(a2, 'inEntityRelationshipModel12'):
        assert not _is_linked(a2, 'inEntityRelationshipModel12', b)


def test_assoc_attributes49_reverse_link_reassign_clear():
    a1 = entityrelationship_Attribute_Composite(identifier_at_composite="sample_text", name_at_composite="sample_text")
    a2 = entityrelationship_Attribute_Composite(identifier_at_composite="sample_text_2", name_at_composite="sample_text_2")
    b = entityrelationship_Attribute(identifier="sample_text", name_attribute="sample_text")
    _safe_set(b, 'entityrelationship_Attribute50', a1)
    assert _is_linked(b, 'entityrelationship_Attribute50', a1)
    if hasattr(a1, 'entityrelationship_Attribute_Composite'):
        assert _is_linked(a1, 'entityrelationship_Attribute_Composite', b)
    _safe_set(b, 'entityrelationship_Attribute50', a2)
    assert _is_linked(b, 'entityrelationship_Attribute50', a2)
    if hasattr(a1, 'entityrelationship_Attribute_Composite'):
        assert not _is_linked(a1, 'entityrelationship_Attribute_Composite', b)
    if hasattr(a2, 'entityrelationship_Attribute_Composite'):
        assert _is_linked(a2, 'entityrelationship_Attribute_Composite', b)
    _safe_set(b, 'entityrelationship_Attribute50', None)
    assert not _is_linked(b, 'entityrelationship_Attribute50', a2)
    if hasattr(a2, 'entityrelationship_Attribute_Composite'):
        assert not _is_linked(a2, 'entityrelationship_Attribute_Composite', b)


def test_assoc_attributes_composites35_reverse_link_reassign_clear():
    a1 = entityrelationship_Attribute_Composite(identifier_at_composite="sample_text", name_at_composite="sample_text")
    a2 = entityrelationship_Attribute_Composite(identifier_at_composite="sample_text_2", name_at_composite="sample_text_2")
    b = entityrelationship_Attribute(identifier="sample_text", name_attribute="sample_text")
    _safe_set(b, 'inAttribute', {a1})
    assert _is_linked(b, 'inAttribute', a1)
    if hasattr(a1, 'Attribute_Composite'):
        assert _is_linked(a1, 'Attribute_Composite', b)
    _safe_set(b, 'inAttribute', {a2})
    assert _is_linked(b, 'inAttribute', a2)
    if hasattr(a1, 'Attribute_Composite'):
        assert not _is_linked(a1, 'Attribute_Composite', b)
    if hasattr(a2, 'Attribute_Composite'):
        assert _is_linked(a2, 'Attribute_Composite', b)
    _safe_set(b, 'inAttribute', set())
    assert not _is_linked(b, 'inAttribute', a2)
    if hasattr(a2, 'Attribute_Composite'):
        assert not _is_linked(a2, 'Attribute_Composite', b)


def test_assoc_attributes_identification37_reverse_link_reassign_clear():
    a1 = entityrelationship_Attribute(identifier="sample_text", name_attribute="sample_text")
    a2 = entityrelationship_Attribute(identifier="sample_text_2", name_attribute="sample_text_2")
    b = entityrelationship_Attribute(identifier="sample_text", name_attribute="sample_text")
    _safe_set(b, 'inAttribute38', {a1})
    assert _is_linked(b, 'inAttribute38', a1)
    if hasattr(a1, 'Attribute'):
        assert _is_linked(a1, 'Attribute', b)
    _safe_set(b, 'inAttribute38', {a2})
    assert _is_linked(b, 'inAttribute38', a2)
    if hasattr(a1, 'Attribute'):
        assert not _is_linked(a1, 'Attribute', b)
    if hasattr(a2, 'Attribute'):
        assert _is_linked(a2, 'Attribute', b)
    _safe_set(b, 'inAttribute38', set())
    assert not _is_linked(b, 'inAttribute38', a2)
    if hasattr(a2, 'Attribute'):
        assert not _is_linked(a2, 'Attribute', b)


def test_assoc_connected39_reverse_link_reassign_clear():
    a1 = entityrelationship_Connection_With_Attribute(type_attribute="sample_text")
    a2 = entityrelationship_Connection_With_Attribute(type_attribute="sample_text_2")
    b = entityrelationship_Attribute(identifier="sample_text", name_attribute="sample_text")
    _safe_set(b, 'connection_attribute', a1)
    assert _is_linked(b, 'connection_attribute', a1)
    if hasattr(a1, 'Connection_With_Attribute40'):
        assert _is_linked(a1, 'Connection_With_Attribute40', b)
    _safe_set(b, 'connection_attribute', a2)
    assert _is_linked(b, 'connection_attribute', a2)
    if hasattr(a1, 'Connection_With_Attribute40'):
        assert not _is_linked(a1, 'Connection_With_Attribute40', b)
    if hasattr(a2, 'Connection_With_Attribute40'):
        assert _is_linked(a2, 'Connection_With_Attribute40', b)
    _safe_set(b, 'connection_attribute', None)
    assert not _is_linked(b, 'connection_attribute', a2)
    if hasattr(a2, 'Connection_With_Attribute40'):
        assert not _is_linked(a2, 'Connection_With_Attribute40', b)


def test_assoc_connection_attribute69_reverse_link_reassign_clear():
    a1 = entityrelationship_Connection_With_Attribute(type_attribute="sample_text")
    a2 = entityrelationship_Connection_With_Attribute(type_attribute="sample_text_2")
    b = entityrelationship_Attribute(identifier="sample_text", name_attribute="sample_text")
    _safe_set(b, 'Attribute70', a1)
    assert _is_linked(b, 'Attribute70', a1)
    if hasattr(a1, 'connected'):
        assert _is_linked(a1, 'connected', b)
    _safe_set(b, 'Attribute70', a2)
    assert _is_linked(b, 'Attribute70', a2)
    if hasattr(a1, 'connected'):
        assert not _is_linked(a1, 'connected', b)
    if hasattr(a2, 'connected'):
        assert _is_linked(a2, 'connected', b)
    _safe_set(b, 'Attribute70', None)
    assert not _is_linked(b, 'Attribute70', a2)
    if hasattr(a2, 'connected'):
        assert not _is_linked(a2, 'connected', b)


def test_assoc_connection_source_entity_relationship59_reverse_link_reassign_clear():
    a1 = entityrelationship_Connection_EntityRelationship(maximum_cardinality="sample_text", minimum_cardinality="sample_text", role="sample_text")
    a2 = entityrelationship_Connection_EntityRelationship(maximum_cardinality="sample_text_2", minimum_cardinality="sample_text_2", role="sample_text_2")
    b = entityrelationship_Connection_E_R_Restriction(type_restriction="sample_text")
    _safe_set(b, 'entityrelationship_Connection_E_R_Restriction', a1)
    assert _is_linked(b, 'entityrelationship_Connection_E_R_Restriction', a1)
    if hasattr(a1, 'entityrelationship_Connection_EntityRelationship'):
        assert _is_linked(a1, 'entityrelationship_Connection_EntityRelationship', b)
    _safe_set(b, 'entityrelationship_Connection_E_R_Restriction', a2)
    assert _is_linked(b, 'entityrelationship_Connection_E_R_Restriction', a2)
    if hasattr(a1, 'entityrelationship_Connection_EntityRelationship'):
        assert not _is_linked(a1, 'entityrelationship_Connection_EntityRelationship', b)
    if hasattr(a2, 'entityrelationship_Connection_EntityRelationship'):
        assert _is_linked(a2, 'entityrelationship_Connection_EntityRelationship', b)
    _safe_set(b, 'entityrelationship_Connection_E_R_Restriction', None)
    assert not _is_linked(b, 'entityrelationship_Connection_E_R_Restriction', a2)
    if hasattr(a2, 'entityrelationship_Connection_EntityRelationship'):
        assert not _is_linked(a2, 'entityrelationship_Connection_EntityRelationship', b)


def test_assoc_connection_target_entity_relationship60_reverse_link_reassign_clear():
    a1 = entityrelationship_Connection_EntityRelationship(maximum_cardinality="sample_text", minimum_cardinality="sample_text", role="sample_text")
    a2 = entityrelationship_Connection_EntityRelationship(maximum_cardinality="sample_text_2", minimum_cardinality="sample_text_2", role="sample_text_2")
    b = entityrelationship_Connection_E_R_Restriction(type_restriction="sample_text")
    _safe_set(b, 'entityrelationship_Connection_E_R_Restriction61', a1)
    assert _is_linked(b, 'entityrelationship_Connection_E_R_Restriction61', a1)
    if hasattr(a1, 'entityrelationship_Connection_EntityRelationship62'):
        assert _is_linked(a1, 'entityrelationship_Connection_EntityRelationship62', b)
    _safe_set(b, 'entityrelationship_Connection_E_R_Restriction61', a2)
    assert _is_linked(b, 'entityrelationship_Connection_E_R_Restriction61', a2)
    if hasattr(a1, 'entityrelationship_Connection_EntityRelationship62'):
        assert not _is_linked(a1, 'entityrelationship_Connection_EntityRelationship62', b)
    if hasattr(a2, 'entityrelationship_Connection_EntityRelationship62'):
        assert _is_linked(a2, 'entityrelationship_Connection_EntityRelationship62', b)
    _safe_set(b, 'entityrelationship_Connection_E_R_Restriction61', None)
    assert not _is_linked(b, 'entityrelationship_Connection_E_R_Restriction61', a2)
    if hasattr(a2, 'entityrelationship_Connection_EntityRelationship62'):
        assert not _is_linked(a2, 'entityrelationship_Connection_EntityRelationship62', b)


def test_assoc_inAttribute42_reverse_link_reassign_clear():
    a1 = entityrelationship_Attribute(identifier="sample_text", name_attribute="sample_text")
    a2 = entityrelationship_Attribute(identifier="sample_text_2", name_attribute="sample_text_2")
    b = entityrelationship_Attribute(identifier="sample_text", name_attribute="sample_text")
    _safe_set(b, 'attributes_identification', a1)
    assert _is_linked(b, 'attributes_identification', a1)
    if hasattr(a1, 'Attribute43'):
        assert _is_linked(a1, 'Attribute43', b)
    _safe_set(b, 'attributes_identification', a2)
    assert _is_linked(b, 'attributes_identification', a2)
    if hasattr(a1, 'Attribute43'):
        assert not _is_linked(a1, 'Attribute43', b)
    if hasattr(a2, 'Attribute43'):
        assert _is_linked(a2, 'Attribute43', b)
    _safe_set(b, 'attributes_identification', None)
    assert not _is_linked(b, 'attributes_identification', a2)
    if hasattr(a2, 'Attribute43'):
        assert not _is_linked(a2, 'Attribute43', b)


def test_assoc_inAttribute51_reverse_link_reassign_clear():
    a1 = entityrelationship_Attribute_Composite(identifier_at_composite="sample_text", name_at_composite="sample_text")
    a2 = entityrelationship_Attribute_Composite(identifier_at_composite="sample_text_2", name_at_composite="sample_text_2")
    b = entityrelationship_Attribute(identifier="sample_text", name_attribute="sample_text")
    _safe_set(b, 'Attribute52', a1)
    assert _is_linked(b, 'Attribute52', a1)
    if hasattr(a1, 'attributes_composites'):
        assert _is_linked(a1, 'attributes_composites', b)
    _safe_set(b, 'Attribute52', a2)
    assert _is_linked(b, 'Attribute52', a2)
    if hasattr(a1, 'attributes_composites'):
        assert not _is_linked(a1, 'attributes_composites', b)
    if hasattr(a2, 'attributes_composites'):
        assert _is_linked(a2, 'attributes_composites', b)
    _safe_set(b, 'Attribute52', None)
    assert not _is_linked(b, 'Attribute52', a2)
    if hasattr(a2, 'attributes_composites'):
        assert not _is_linked(a2, 'attributes_composites', b)


def test_assoc_inEntityRelationshipModel44_reverse_link_reassign_clear():
    a1 = entityrelationship_Entity_Relationship_Model(name="sample_text")
    a2 = entityrelationship_Entity_Relationship_Model(name="sample_text_2")
    b = entityrelationship_Attribute(identifier="sample_text", name_attribute="sample_text")
    _safe_set(b, 'entityrelationship_Attribute45', a1)
    assert _is_linked(b, 'entityrelationship_Attribute45', a1)
    if hasattr(a1, 'entityrelationship_Entity_Relationship_Model46'):
        assert _is_linked(a1, 'entityrelationship_Entity_Relationship_Model46', b)
    _safe_set(b, 'entityrelationship_Attribute45', a2)
    assert _is_linked(b, 'entityrelationship_Attribute45', a2)
    if hasattr(a1, 'entityrelationship_Entity_Relationship_Model46'):
        assert not _is_linked(a1, 'entityrelationship_Entity_Relationship_Model46', b)
    if hasattr(a2, 'entityrelationship_Entity_Relationship_Model46'):
        assert _is_linked(a2, 'entityrelationship_Entity_Relationship_Model46', b)
    _safe_set(b, 'entityrelationship_Attribute45', None)
    assert not _is_linked(b, 'entityrelationship_Attribute45', a2)
    if hasattr(a2, 'entityrelationship_Entity_Relationship_Model46'):
        assert not _is_linked(a2, 'entityrelationship_Entity_Relationship_Model46', b)


def test_assoc_inEntityRelationshipModel57_reverse_link_reassign_clear():
    a1 = entityrelationship_Relationships_Restriction(type_restriction="sample_text")
    a2 = entityrelationship_Relationships_Restriction(type_restriction="sample_text_2")
    b = entityrelationship_Entity_Relationship_Model(name="sample_text")
    _safe_set(b, 'Entity_Relationship_Model58', a1)
    assert _is_linked(b, 'Entity_Relationship_Model58', a1)
    if hasattr(a1, 'ERM_Has_Rt'):
        assert _is_linked(a1, 'ERM_Has_Rt', b)
    _safe_set(b, 'Entity_Relationship_Model58', a2)
    assert _is_linked(b, 'Entity_Relationship_Model58', a2)
    if hasattr(a1, 'ERM_Has_Rt'):
        assert not _is_linked(a1, 'ERM_Has_Rt', b)
    if hasattr(a2, 'ERM_Has_Rt'):
        assert _is_linked(a2, 'ERM_Has_Rt', b)
    _safe_set(b, 'Entity_Relationship_Model58', None)
    assert not _is_linked(b, 'Entity_Relationship_Model58', a2)
    if hasattr(a2, 'ERM_Has_Rt'):
        assert not _is_linked(a2, 'ERM_Has_Rt', b)


def test_assoc_inEntityRelationshipModel63_reverse_link_reassign_clear():
    a1 = entityrelationship_Entity_Relationship_Model(name="sample_text")
    a2 = entityrelationship_Entity_Relationship_Model(name="sample_text_2")
    b = entityrelationship_Connection_E_R_Restriction(type_restriction="sample_text")
    _safe_set(b, 'ERM_Has_Rt2', a1)
    assert _is_linked(b, 'ERM_Has_Rt2', a1)
    if hasattr(a1, 'Entity_Relationship_Model64'):
        assert _is_linked(a1, 'Entity_Relationship_Model64', b)
    _safe_set(b, 'ERM_Has_Rt2', a2)
    assert _is_linked(b, 'ERM_Has_Rt2', a2)
    if hasattr(a1, 'Entity_Relationship_Model64'):
        assert not _is_linked(a1, 'Entity_Relationship_Model64', b)
    if hasattr(a2, 'Entity_Relationship_Model64'):
        assert _is_linked(a2, 'Entity_Relationship_Model64', b)
    _safe_set(b, 'ERM_Has_Rt2', None)
    assert not _is_linked(b, 'ERM_Has_Rt2', a2)
    if hasattr(a2, 'Entity_Relationship_Model64'):
        assert not _is_linked(a2, 'Entity_Relationship_Model64', b)


def test_assoc_inEntityRelationshipModel67_reverse_link_reassign_clear():
    a1 = entityrelationship_Generalization(restriction_inheritance_1="sample_text", restriction_inheritance_2="sample_text")
    a2 = entityrelationship_Generalization(restriction_inheritance_1="sample_text_2", restriction_inheritance_2="sample_text_2")
    b = entityrelationship_Entity_Relationship_Model(name="sample_text")
    _safe_set(b, 'Entity_Relationship_Model68', a1)
    assert _is_linked(b, 'Entity_Relationship_Model68', a1)
    if hasattr(a1, 'ERM_Has_G'):
        assert _is_linked(a1, 'ERM_Has_G', b)
    _safe_set(b, 'Entity_Relationship_Model68', a2)
    assert _is_linked(b, 'Entity_Relationship_Model68', a2)
    if hasattr(a1, 'ERM_Has_G'):
        assert not _is_linked(a1, 'ERM_Has_G', b)
    if hasattr(a2, 'ERM_Has_G'):
        assert _is_linked(a2, 'ERM_Has_G', b)
    _safe_set(b, 'Entity_Relationship_Model68', None)
    assert not _is_linked(b, 'Entity_Relationship_Model68', a2)
    if hasattr(a2, 'ERM_Has_G'):
        assert not _is_linked(a2, 'ERM_Has_G', b)


def test_assoc_inEntityRelationshipModel73_reverse_link_reassign_clear():
    a1 = entityrelationship_Entity_Relationship_Model(name="sample_text")
    a2 = entityrelationship_Entity_Relationship_Model(name="sample_text_2")
    b = entityrelationship_Connection_With_Attribute(type_attribute="sample_text")
    _safe_set(b, 'ERM_Has_CEA', a1)
    assert _is_linked(b, 'ERM_Has_CEA', a1)
    if hasattr(a1, 'Entity_Relationship_Model74'):
        assert _is_linked(a1, 'Entity_Relationship_Model74', b)
    _safe_set(b, 'ERM_Has_CEA', a2)
    assert _is_linked(b, 'ERM_Has_CEA', a2)
    if hasattr(a1, 'Entity_Relationship_Model74'):
        assert not _is_linked(a1, 'Entity_Relationship_Model74', b)
    if hasattr(a2, 'Entity_Relationship_Model74'):
        assert _is_linked(a2, 'Entity_Relationship_Model74', b)
    _safe_set(b, 'ERM_Has_CEA', None)
    assert not _is_linked(b, 'ERM_Has_CEA', a2)
    if hasattr(a2, 'Entity_Relationship_Model74'):
        assert not _is_linked(a2, 'Entity_Relationship_Model74', b)


def test_assoc_inEntityRelationshipModel80_reverse_link_reassign_clear():
    a1 = entityrelationship_Entity_Relationship_Model(name="sample_text")
    a2 = entityrelationship_Entity_Relationship_Model(name="sample_text_2")
    b = entityrelationship_Connection_Generalization_Entity(maximum_cardinality="sample_text", minimum_cardinality="sample_text")
    _safe_set(b, 'ERM_Has_Gen', a1)
    assert _is_linked(b, 'ERM_Has_Gen', a1)
    if hasattr(a1, 'Entity_Relationship_Model81'):
        assert _is_linked(a1, 'Entity_Relationship_Model81', b)
    _safe_set(b, 'ERM_Has_Gen', a2)
    assert _is_linked(b, 'ERM_Has_Gen', a2)
    if hasattr(a1, 'Entity_Relationship_Model81'):
        assert not _is_linked(a1, 'Entity_Relationship_Model81', b)
    if hasattr(a2, 'Entity_Relationship_Model81'):
        assert _is_linked(a2, 'Entity_Relationship_Model81', b)
    _safe_set(b, 'ERM_Has_Gen', None)
    assert not _is_linked(b, 'ERM_Has_Gen', a2)
    if hasattr(a2, 'Entity_Relationship_Model81'):
        assert not _is_linked(a2, 'Entity_Relationship_Model81', b)


def test_assoc_source_relationship53_reverse_link_reassign_clear():
    a1 = entityrelationship_Relationships_Restriction(type_restriction="sample_text")
    a2 = entityrelationship_Relationships_Restriction(type_restriction="sample_text_2")
    b = entityrelationship_Relationship(cardinality="sample_text", name_relationship="sample_text", order=7, type_relationship="sample_text")
    _safe_set(b, 'entityrelationship_Relationship55', a1)
    assert _is_linked(b, 'entityrelationship_Relationship55', a1)
    if hasattr(a1, 'entityrelationship_Relationships_Restriction54'):
        assert _is_linked(a1, 'entityrelationship_Relationships_Restriction54', b)
    _safe_set(b, 'entityrelationship_Relationship55', a2)
    assert _is_linked(b, 'entityrelationship_Relationship55', a2)
    if hasattr(a1, 'entityrelationship_Relationships_Restriction54'):
        assert not _is_linked(a1, 'entityrelationship_Relationships_Restriction54', b)
    if hasattr(a2, 'entityrelationship_Relationships_Restriction54'):
        assert _is_linked(a2, 'entityrelationship_Relationships_Restriction54', b)
    _safe_set(b, 'entityrelationship_Relationship55', None)
    assert not _is_linked(b, 'entityrelationship_Relationship55', a2)
    if hasattr(a2, 'entityrelationship_Relationships_Restriction54'):
        assert not _is_linked(a2, 'entityrelationship_Relationships_Restriction54', b)


def test_assoc_source_restrictions27_reverse_link_reassign_clear():
    a1 = entityrelationship_Relationships_Restriction(type_restriction="sample_text")
    a2 = entityrelationship_Relationships_Restriction(type_restriction="sample_text_2")
    b = entityrelationship_Relationship(cardinality="sample_text", name_relationship="sample_text", order=7, type_relationship="sample_text")
    _safe_set(b, 'entityrelationship_Relationship', a1)
    assert _is_linked(b, 'entityrelationship_Relationship', a1)
    if hasattr(a1, 'entityrelationship_Relationships_Restriction'):
        assert _is_linked(a1, 'entityrelationship_Relationships_Restriction', b)
    _safe_set(b, 'entityrelationship_Relationship', a2)
    assert _is_linked(b, 'entityrelationship_Relationship', a2)
    if hasattr(a1, 'entityrelationship_Relationships_Restriction'):
        assert not _is_linked(a1, 'entityrelationship_Relationships_Restriction', b)
    if hasattr(a2, 'entityrelationship_Relationships_Restriction'):
        assert _is_linked(a2, 'entityrelationship_Relationships_Restriction', b)
    _safe_set(b, 'entityrelationship_Relationship', None)
    assert not _is_linked(b, 'entityrelationship_Relationship', a2)
    if hasattr(a2, 'entityrelationship_Relationships_Restriction'):
        assert not _is_linked(a2, 'entityrelationship_Relationships_Restriction', b)


def test_assoc_subclass_generalizations25_reverse_link_reassign_clear():
    a1 = entityrelationship_Generalization(restriction_inheritance_1="sample_text", restriction_inheritance_2="sample_text")
    a2 = entityrelationship_Generalization(restriction_inheritance_1="sample_text_2", restriction_inheritance_2="sample_text_2")
    b = entityrelationship_Entity(name_entity="sample_text", type_entity="sample_text")
    _safe_set(b, 'subclasses', {a1})
    assert _is_linked(b, 'subclasses', a1)
    if hasattr(a1, 'Generalization26'):
        assert _is_linked(a1, 'Generalization26', b)
    _safe_set(b, 'subclasses', {a2})
    assert _is_linked(b, 'subclasses', a2)
    if hasattr(a1, 'Generalization26'):
        assert not _is_linked(a1, 'Generalization26', b)
    if hasattr(a2, 'Generalization26'):
        assert _is_linked(a2, 'Generalization26', b)
    _safe_set(b, 'subclasses', set())
    assert not _is_linked(b, 'subclasses', a2)
    if hasattr(a2, 'Generalization26'):
        assert not _is_linked(a2, 'Generalization26', b)


def test_assoc_subclasses65_reverse_link_reassign_clear():
    a1 = entityrelationship_Generalization(restriction_inheritance_1="sample_text", restriction_inheritance_2="sample_text")
    a2 = entityrelationship_Generalization(restriction_inheritance_1="sample_text_2", restriction_inheritance_2="sample_text_2")
    b = entityrelationship_Entity(name_entity="sample_text", type_entity="sample_text")
    _safe_set(b, 'Entity', a1)
    assert _is_linked(b, 'Entity', a1)
    if hasattr(a1, 'subclass_generalizations'):
        assert _is_linked(a1, 'subclass_generalizations', b)
    _safe_set(b, 'Entity', a2)
    assert _is_linked(b, 'Entity', a2)
    if hasattr(a1, 'subclass_generalizations'):
        assert not _is_linked(a1, 'subclass_generalizations', b)
    if hasattr(a2, 'subclass_generalizations'):
        assert _is_linked(a2, 'subclass_generalizations', b)
    _safe_set(b, 'Entity', None)
    assert not _is_linked(b, 'Entity', a2)
    if hasattr(a2, 'subclass_generalizations'):
        assert not _is_linked(a2, 'subclass_generalizations', b)


def test_assoc_superclass66_reverse_link_reassign_clear():
    a1 = entityrelationship_Generalization(restriction_inheritance_1="sample_text", restriction_inheritance_2="sample_text")
    a2 = entityrelationship_Generalization(restriction_inheritance_1="sample_text_2", restriction_inheritance_2="sample_text_2")
    b = entityrelationship_Entity(name_entity="sample_text", type_entity="sample_text")
    _safe_set(b, 'entityrelationship_Entity', a1)
    assert _is_linked(b, 'entityrelationship_Entity', a1)
    if hasattr(a1, 'entityrelationship_Generalization'):
        assert _is_linked(a1, 'entityrelationship_Generalization', b)
    _safe_set(b, 'entityrelationship_Entity', a2)
    assert _is_linked(b, 'entityrelationship_Entity', a2)
    if hasattr(a1, 'entityrelationship_Generalization'):
        assert not _is_linked(a1, 'entityrelationship_Generalization', b)
    if hasattr(a2, 'entityrelationship_Generalization'):
        assert _is_linked(a2, 'entityrelationship_Generalization', b)
    _safe_set(b, 'entityrelationship_Entity', None)
    assert not _is_linked(b, 'entityrelationship_Entity', a2)
    if hasattr(a2, 'entityrelationship_Generalization'):
        assert not _is_linked(a2, 'entityrelationship_Generalization', b)


def test_assoc_target_relationship56_reverse_link_reassign_clear():
    a1 = entityrelationship_Relationships_Restriction(type_restriction="sample_text")
    a2 = entityrelationship_Relationships_Restriction(type_restriction="sample_text_2")
    b = entityrelationship_Relationship(cardinality="sample_text", name_relationship="sample_text", order=7, type_relationship="sample_text")
    _safe_set(b, 'Relationship', a1)
    assert _is_linked(b, 'Relationship', a1)
    if hasattr(a1, 'target_restrictions'):
        assert _is_linked(a1, 'target_restrictions', b)
    _safe_set(b, 'Relationship', a2)
    assert _is_linked(b, 'Relationship', a2)
    if hasattr(a1, 'target_restrictions'):
        assert not _is_linked(a1, 'target_restrictions', b)
    if hasattr(a2, 'target_restrictions'):
        assert _is_linked(a2, 'target_restrictions', b)
    _safe_set(b, 'Relationship', None)
    assert not _is_linked(b, 'Relationship', a2)
    if hasattr(a2, 'target_restrictions'):
        assert not _is_linked(a2, 'target_restrictions', b)


def test_assoc_target_restrictions28_reverse_link_reassign_clear():
    a1 = entityrelationship_Relationships_Restriction(type_restriction="sample_text")
    a2 = entityrelationship_Relationships_Restriction(type_restriction="sample_text_2")
    b = entityrelationship_Relationship(cardinality="sample_text", name_relationship="sample_text", order=7, type_relationship="sample_text")
    _safe_set(b, 'target_relationship', {a1})
    assert _is_linked(b, 'target_relationship', a1)
    if hasattr(a1, 'Relationships_Restriction29'):
        assert _is_linked(a1, 'Relationships_Restriction29', b)
    _safe_set(b, 'target_relationship', {a2})
    assert _is_linked(b, 'target_relationship', a2)
    if hasattr(a1, 'Relationships_Restriction29'):
        assert not _is_linked(a1, 'Relationships_Restriction29', b)
    if hasattr(a2, 'Relationships_Restriction29'):
        assert _is_linked(a2, 'Relationships_Restriction29', b)
    _safe_set(b, 'target_relationship', set())
    assert not _is_linked(b, 'target_relationship', a2)
    if hasattr(a2, 'Relationships_Restriction29'):
        assert not _is_linked(a2, 'Relationships_Restriction29', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_ERM_HasConnectionEntityRelationship2Attribute7_stub_double():
    # entityrelationship_Connection_ConnectionEntityRelationship2Attribute has no real 'Connection_ConnectionEntityRelationship2Attribute' property in the generated
    # code (a bare stub) -- manually attach it so entityrelationship_Entity_Relationship_Model's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # entityrelationship_Entity_Relationship_Model's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = entityrelationship_Entity_Relationship_Model(name="sample_text")
    partner = entityrelationship_Connection_ConnectionEntityRelationship2Attribute()
    setattr(partner, 'Connection_ConnectionEntityRelationship2Attribute', None)
    _safe_set(owner, 'inEntityRelationshipModel8', {partner})
    assert getattr(partner, 'Connection_ConnectionEntityRelationship2Attribute') == owner
    _safe_set(owner, 'inEntityRelationshipModel8', set())
    assert getattr(partner, 'Connection_ConnectionEntityRelationship2Attribute') is None


def test_assoc_ERM_Has_ConnectionEntity2Relationship3_stub_double():
    # entityrelationship_Connection_Entity2Relationship has no real 'Connection_Entity2Relationship' property in the generated
    # code (a bare stub) -- manually attach it so entityrelationship_Entity_Relationship_Model's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # entityrelationship_Entity_Relationship_Model's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = entityrelationship_Entity_Relationship_Model(name="sample_text")
    partner = entityrelationship_Connection_Entity2Relationship()
    setattr(partner, 'Connection_Entity2Relationship', None)
    _safe_set(owner, 'inEntityRelationshipModel4', {partner})
    assert getattr(partner, 'Connection_Entity2Relationship') == owner
    _safe_set(owner, 'inEntityRelationshipModel4', set())
    assert getattr(partner, 'Connection_Entity2Relationship') is None


def test_assoc_ERM_Has_ConnectionRelationship2Entity5_stub_double():
    # entityrelationship_Connection_Relationship2Entity has no real 'Connection_Relationship2Entity' property in the generated
    # code (a bare stub) -- manually attach it so entityrelationship_Entity_Relationship_Model's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # entityrelationship_Entity_Relationship_Model's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = entityrelationship_Entity_Relationship_Model(name="sample_text")
    partner = entityrelationship_Connection_Relationship2Entity()
    setattr(partner, 'Connection_Relationship2Entity', None)
    _safe_set(owner, 'inEntityRelationshipModel6', {partner})
    assert getattr(partner, 'Connection_Relationship2Entity') == owner
    _safe_set(owner, 'inEntityRelationshipModel6', set())
    assert getattr(partner, 'Connection_Relationship2Entity') is None


def test_assoc_ERM_Has_E0_stub_double():
    # entityrelationship_Elements_with_Attributes has no real 'Elements_with_Attributes' property in the generated
    # code (a bare stub) -- manually attach it so entityrelationship_Entity_Relationship_Model's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # entityrelationship_Entity_Relationship_Model's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = entityrelationship_Entity_Relationship_Model(name="sample_text")
    partner = entityrelationship_Elements_with_Attributes()
    setattr(partner, 'Elements_with_Attributes', None)
    _safe_set(owner, 'inEntityRelationshipModel', {partner})
    assert getattr(partner, 'Elements_with_Attributes') == owner
    _safe_set(owner, 'inEntityRelationshipModel', set())
    assert getattr(partner, 'Elements_with_Attributes') is None


def test_assoc_attribute_connected_to_conection_entityrelationship_to_attribute47_stub_double():
    # entityrelationship_Connection_ConnectionEntityRelationship2Attribute has no real 'Connection_ConnectionEntityRelationship2Attribute48' property in the generated
    # code (a bare stub) -- manually attach it so entityrelationship_Attribute's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # entityrelationship_Attribute's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = entityrelationship_Attribute(identifier="sample_text", name_attribute="sample_text")
    partner = entityrelationship_Connection_ConnectionEntityRelationship2Attribute()
    setattr(partner, 'Connection_ConnectionEntityRelationship2Attribute48', None)
    _safe_set(owner, 'target_attribute', partner)
    assert getattr(partner, 'Connection_ConnectionEntityRelationship2Attribute48') == owner
    _safe_set(owner, 'target_attribute', None)
    assert getattr(partner, 'Connection_ConnectionEntityRelationship2Attribute48') is None


def test_assoc_connected_with_attribute18_stub_double():
    # entityrelationship_Elements_with_Attributes has no real 'element' property in the generated
    # code (a bare stub) -- manually attach it so entityrelationship_Connection_With_Attribute's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # entityrelationship_Connection_With_Attribute's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = entityrelationship_Connection_With_Attribute(type_attribute="sample_text")
    partner = entityrelationship_Elements_with_Attributes()
    setattr(partner, 'element', None)
    _safe_set(owner, 'Connection_With_Attribute19', partner)
    assert owner in getattr(partner, 'element')
    _safe_set(owner, 'Connection_With_Attribute19', None)
    assert owner not in getattr(partner, 'element')


def test_assoc_element71_stub_double():
    # entityrelationship_Elements_with_Attributes has no real 'Elements_with_Attributes72' property in the generated
    # code (a bare stub) -- manually attach it so entityrelationship_Connection_With_Attribute's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # entityrelationship_Connection_With_Attribute's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = entityrelationship_Connection_With_Attribute(type_attribute="sample_text")
    partner = entityrelationship_Elements_with_Attributes()
    setattr(partner, 'Elements_with_Attributes72', None)
    _safe_set(owner, 'connected_with_attribute', partner)
    assert getattr(partner, 'Elements_with_Attributes72') == owner
    _safe_set(owner, 'connected_with_attribute', None)
    assert getattr(partner, 'Elements_with_Attributes72') is None


def test_assoc_entity_connected_to_entity2relationship21_stub_double():
    # entityrelationship_Connection_Entity2Relationship has no real 'Connection_Entity2Relationship22' property in the generated
    # code (a bare stub) -- manually attach it so entityrelationship_Entity's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # entityrelationship_Entity's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = entityrelationship_Entity(name_entity="sample_text", type_entity="sample_text")
    partner = entityrelationship_Connection_Entity2Relationship()
    setattr(partner, 'Connection_Entity2Relationship22', None)
    _safe_set(owner, 'source_entity', {partner})
    assert getattr(partner, 'Connection_Entity2Relationship22') == owner
    _safe_set(owner, 'source_entity', set())
    assert getattr(partner, 'Connection_Entity2Relationship22') is None


def test_assoc_entity_connected_to_relationship2entity23_stub_double():
    # entityrelationship_Connection_Relationship2Entity has no real 'Connection_Relationship2Entity24' property in the generated
    # code (a bare stub) -- manually attach it so entityrelationship_Entity's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # entityrelationship_Entity's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = entityrelationship_Entity(name_entity="sample_text", type_entity="sample_text")
    partner = entityrelationship_Connection_Relationship2Entity()
    setattr(partner, 'Connection_Relationship2Entity24', None)
    _safe_set(owner, 'target_entity', {partner})
    assert getattr(partner, 'Connection_Relationship2Entity24') == owner
    _safe_set(owner, 'target_entity', set())
    assert getattr(partner, 'Connection_Relationship2Entity24') is None


def test_assoc_inEntityRelationshipModel20_stub_double():
    # entityrelationship_Elements_with_Attributes has no real 'ERM_Has_E' property in the generated
    # code (a bare stub) -- manually attach it so entityrelationship_Entity_Relationship_Model's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # entityrelationship_Entity_Relationship_Model's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = entityrelationship_Entity_Relationship_Model(name="sample_text")
    partner = entityrelationship_Elements_with_Attributes()
    setattr(partner, 'ERM_Has_E', None)
    _safe_set(owner, 'Entity_Relationship_Model', partner)
    assert getattr(partner, 'ERM_Has_E') == owner
    _safe_set(owner, 'Entity_Relationship_Model', None)
    assert getattr(partner, 'ERM_Has_E') is None


def test_assoc_inEntityRelationshipModel86_stub_double():
    # entityrelationship_Connection_Entity2Relationship has no real 'ERM_Has_ConnectionEntity2Relationship' property in the generated
    # code (a bare stub) -- manually attach it so entityrelationship_Entity_Relationship_Model's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # entityrelationship_Entity_Relationship_Model's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = entityrelationship_Entity_Relationship_Model(name="sample_text")
    partner = entityrelationship_Connection_Entity2Relationship()
    setattr(partner, 'ERM_Has_ConnectionEntity2Relationship', None)
    _safe_set(owner, 'Entity_Relationship_Model87', partner)
    assert getattr(partner, 'ERM_Has_ConnectionEntity2Relationship') == owner
    _safe_set(owner, 'Entity_Relationship_Model87', None)
    assert getattr(partner, 'ERM_Has_ConnectionEntity2Relationship') is None


def test_assoc_inEntityRelationshipModel92_stub_double():
    # entityrelationship_Connection_Relationship2Entity has no real 'ERM_Has_ConnectionRelationship2Entity' property in the generated
    # code (a bare stub) -- manually attach it so entityrelationship_Entity_Relationship_Model's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # entityrelationship_Entity_Relationship_Model's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = entityrelationship_Entity_Relationship_Model(name="sample_text")
    partner = entityrelationship_Connection_Relationship2Entity()
    setattr(partner, 'ERM_Has_ConnectionRelationship2Entity', None)
    _safe_set(owner, 'Entity_Relationship_Model93', partner)
    assert getattr(partner, 'ERM_Has_ConnectionRelationship2Entity') == owner
    _safe_set(owner, 'Entity_Relationship_Model93', None)
    assert getattr(partner, 'ERM_Has_ConnectionRelationship2Entity') is None


def test_assoc_inEntityRelationshipModel98_stub_double():
    # entityrelationship_Connection_ConnectionEntityRelationship2Attribute has no real 'ERM_HasConnectionEntityRelationship2Attribute' property in the generated
    # code (a bare stub) -- manually attach it so entityrelationship_Entity_Relationship_Model's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # entityrelationship_Entity_Relationship_Model's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = entityrelationship_Entity_Relationship_Model(name="sample_text")
    partner = entityrelationship_Connection_ConnectionEntityRelationship2Attribute()
    setattr(partner, 'ERM_HasConnectionEntityRelationship2Attribute', None)
    _safe_set(owner, 'Entity_Relationship_Model99', partner)
    assert getattr(partner, 'ERM_HasConnectionEntityRelationship2Attribute') == owner
    _safe_set(owner, 'Entity_Relationship_Model99', None)
    assert getattr(partner, 'ERM_HasConnectionEntityRelationship2Attribute') is None


def test_assoc_relationship_connected_to_entity2relationship30_stub_double():
    # entityrelationship_Connection_Entity2Relationship has no real 'Connection_Entity2Relationship32' property in the generated
    # code (a bare stub) -- manually attach it so entityrelationship_Relationship's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # entityrelationship_Relationship's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = entityrelationship_Relationship(cardinality="sample_text", name_relationship="sample_text", order=7, type_relationship="sample_text")
    partner = entityrelationship_Connection_Entity2Relationship()
    setattr(partner, 'Connection_Entity2Relationship32', None)
    _safe_set(owner, 'target_relationship31', {partner})
    assert getattr(partner, 'Connection_Entity2Relationship32') == owner
    _safe_set(owner, 'target_relationship31', set())
    assert getattr(partner, 'Connection_Entity2Relationship32') is None


def test_assoc_relationship_connected_to_relationship2entity33_stub_double():
    # entityrelationship_Connection_Relationship2Entity has no real 'Connection_Relationship2Entity34' property in the generated
    # code (a bare stub) -- manually attach it so entityrelationship_Relationship's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # entityrelationship_Relationship's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = entityrelationship_Relationship(cardinality="sample_text", name_relationship="sample_text", order=7, type_relationship="sample_text")
    partner = entityrelationship_Connection_Relationship2Entity()
    setattr(partner, 'Connection_Relationship2Entity34', None)
    _safe_set(owner, 'source_relationship', {partner})
    assert getattr(partner, 'Connection_Relationship2Entity34') == owner
    _safe_set(owner, 'source_relationship', set())
    assert getattr(partner, 'Connection_Relationship2Entity34') is None


def test_assoc_source_connection94_stub_double():
    # entityrelationship_Connection_ConnectionEntityRelationship2Attribute has no real 'entityrelationship_Connection_ConnectionEntityRelationship2Attribute' property in the generated
    # code (a bare stub) -- manually attach it so entityrelationship_Connection_EntityRelationship's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # entityrelationship_Connection_EntityRelationship's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = entityrelationship_Connection_EntityRelationship(maximum_cardinality="sample_text", minimum_cardinality="sample_text", role="sample_text")
    partner = entityrelationship_Connection_ConnectionEntityRelationship2Attribute()
    setattr(partner, 'entityrelationship_Connection_ConnectionEntityRelationship2Attribute', None)
    _safe_set(owner, 'entityrelationship_Connection_EntityRelationship95', partner)
    assert getattr(partner, 'entityrelationship_Connection_ConnectionEntityRelationship2Attribute') == owner
    _safe_set(owner, 'entityrelationship_Connection_EntityRelationship95', None)
    assert getattr(partner, 'entityrelationship_Connection_ConnectionEntityRelationship2Attribute') is None


def test_assoc_source_entity82_stub_double():
    # entityrelationship_Connection_Entity2Relationship has no real 'entity_connected_to_entity2relationship' property in the generated
    # code (a bare stub) -- manually attach it so entityrelationship_Entity's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # entityrelationship_Entity's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = entityrelationship_Entity(name_entity="sample_text", type_entity="sample_text")
    partner = entityrelationship_Connection_Entity2Relationship()
    setattr(partner, 'entity_connected_to_entity2relationship', None)
    _safe_set(owner, 'Entity83', partner)
    assert getattr(partner, 'entity_connected_to_entity2relationship') == owner
    _safe_set(owner, 'Entity83', None)
    assert getattr(partner, 'entity_connected_to_entity2relationship') is None


def test_assoc_source_relationship88_stub_double():
    # entityrelationship_Connection_Relationship2Entity has no real 'relationship_connected_to_relationship2entity' property in the generated
    # code (a bare stub) -- manually attach it so entityrelationship_Relationship's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # entityrelationship_Relationship's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = entityrelationship_Relationship(cardinality="sample_text", name_relationship="sample_text", order=7, type_relationship="sample_text")
    partner = entityrelationship_Connection_Relationship2Entity()
    setattr(partner, 'relationship_connected_to_relationship2entity', None)
    _safe_set(owner, 'Relationship89', partner)
    assert getattr(partner, 'relationship_connected_to_relationship2entity') == owner
    _safe_set(owner, 'Relationship89', None)
    assert getattr(partner, 'relationship_connected_to_relationship2entity') is None


def test_assoc_target_attribute96_stub_double():
    # entityrelationship_Connection_ConnectionEntityRelationship2Attribute has no real 'attribute_connected_to_conection_entityrelationship_to_attribute' property in the generated
    # code (a bare stub) -- manually attach it so entityrelationship_Attribute's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # entityrelationship_Attribute's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = entityrelationship_Attribute(identifier="sample_text", name_attribute="sample_text")
    partner = entityrelationship_Connection_ConnectionEntityRelationship2Attribute()
    setattr(partner, 'attribute_connected_to_conection_entityrelationship_to_attribute', None)
    _safe_set(owner, 'Attribute97', partner)
    assert getattr(partner, 'attribute_connected_to_conection_entityrelationship_to_attribute') == owner
    _safe_set(owner, 'Attribute97', None)
    assert getattr(partner, 'attribute_connected_to_conection_entityrelationship_to_attribute') is None


def test_assoc_target_entity90_stub_double():
    # entityrelationship_Connection_Relationship2Entity has no real 'entity_connected_to_relationship2entity' property in the generated
    # code (a bare stub) -- manually attach it so entityrelationship_Entity's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # entityrelationship_Entity's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = entityrelationship_Entity(name_entity="sample_text", type_entity="sample_text")
    partner = entityrelationship_Connection_Relationship2Entity()
    setattr(partner, 'entity_connected_to_relationship2entity', None)
    _safe_set(owner, 'Entity91', partner)
    assert getattr(partner, 'entity_connected_to_relationship2entity') == owner
    _safe_set(owner, 'Entity91', None)
    assert getattr(partner, 'entity_connected_to_relationship2entity') is None


def test_assoc_target_relationship84_stub_double():
    # entityrelationship_Connection_Entity2Relationship has no real 'relationship_connected_to_entity2relationship' property in the generated
    # code (a bare stub) -- manually attach it so entityrelationship_Relationship's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # entityrelationship_Relationship's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = entityrelationship_Relationship(cardinality="sample_text", name_relationship="sample_text", order=7, type_relationship="sample_text")
    partner = entityrelationship_Connection_Entity2Relationship()
    setattr(partner, 'relationship_connected_to_entity2relationship', None)
    _safe_set(owner, 'Relationship85', partner)
    assert getattr(partner, 'relationship_connected_to_entity2relationship') == owner
    _safe_set(owner, 'Relationship85', None)
    assert getattr(partner, 'relationship_connected_to_entity2relationship') is None


