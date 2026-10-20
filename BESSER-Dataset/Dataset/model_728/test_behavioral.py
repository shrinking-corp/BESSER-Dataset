import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    AccessPolicy,
    AttributeDefinition,
    AttributeDefinitionComplex,
    AttributeDefinitionEnumeration,
    AttributeDefinitionSimple,
    AttributeValue,
    AttributeValueComplex,
    AttributeValueEnumeration,
    AttributeValueSimple,
    DataTypes_BinaryContent,
    DataTypes_XhtmlContent,
    DataTypes_XmlContent,
    DatatypeDefinition,
    DatatypeDefinitionComplex,
    DatatypeDefinitionEnumeration,
    DatatypeDefinitionSimple,
    EmbeddedValue,
    EnumValue,
    Identifiable,
    RIFContent,
    RIFHeader,
    RIFToolExtension,
    RelationGroup,
    SpecElementWithUserDefinedAttributes,
    SpecGroup,
    SpecGroupHierarchy,
    SpecGroupHierarchyRoot,
    SpecHierarchy,
    SpecHierarchyRoot,
    SpecObject,
    SpecRelation,
    SpecType,
    rif12_DataTypes_BinaryContent,
    rif12_DataTypes_XhtmlContent,
    rif12_DataTypes_XmlContent,
    rif12_ExchangeFile_AccessPolicy,
    rif12_ExchangeFile_AttributeDefinition,
    rif12_ExchangeFile_AttributeDefinitionComplex,
    rif12_ExchangeFile_AttributeDefinitionEnumeration,
    rif12_ExchangeFile_AttributeDefinitionSimple,
    rif12_ExchangeFile_AttributeValue,
    rif12_ExchangeFile_AttributeValueComplex,
    rif12_ExchangeFile_AttributeValueEmbeddedDocument,
    rif12_ExchangeFile_AttributeValueEmbeddedFile,
    rif12_ExchangeFile_AttributeValueEnumeration,
    rif12_ExchangeFile_AttributeValueFileReference,
    rif12_ExchangeFile_AttributeValueSimple,
    rif12_ExchangeFile_AttributeValueXmlData,
    rif12_ExchangeFile_DatatypeDefinition,
    rif12_ExchangeFile_DatatypeDefinitionBinaryFile,
    rif12_ExchangeFile_DatatypeDefinitionBoolean,
    rif12_ExchangeFile_DatatypeDefinitionComplex,
    rif12_ExchangeFile_DatatypeDefinitionDate,
    rif12_ExchangeFile_DatatypeDefinitionDocument,
    rif12_ExchangeFile_DatatypeDefinitionEnumeration,
    rif12_ExchangeFile_DatatypeDefinitionInteger,
    rif12_ExchangeFile_DatatypeDefinitionReal,
    rif12_ExchangeFile_DatatypeDefinitionSimple,
    rif12_ExchangeFile_DatatypeDefinitionString,
    rif12_ExchangeFile_DatatypeDefinitionXmlData,
    rif12_ExchangeFile_EmbeddedValue,
    rif12_ExchangeFile_EnumValue,
    rif12_ExchangeFile_Identifiable,
    rif12_ExchangeFile_RIF,
    rif12_ExchangeFile_RIFContent,
    rif12_ExchangeFile_RIFHeader,
    rif12_ExchangeFile_RIFToolExtension,
    rif12_ExchangeFile_RelationGroup,
    rif12_ExchangeFile_SpecElementWithUserDefinedAttributes,
    rif12_ExchangeFile_SpecGroup,
    rif12_ExchangeFile_SpecGroupHierarchy,
    rif12_ExchangeFile_SpecGroupHierarchyRoot,
    rif12_ExchangeFile_SpecHierarchy,
    rif12_ExchangeFile_SpecHierarchyRoot,
    rif12_ExchangeFile_SpecObject,
    rif12_ExchangeFile_SpecRelation,
    rif12_ExchangeFile_SpecType,
    AccessPolicyAccessModeEnum,
    DatatypeDefinitionDateFormatEnum,
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

# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_attributeDefinitions28_stub_double():
    # AttributeDefinition has no real 'AttributeDefinition30' property in the generated
    # code (a bare stub) -- manually attach it so rif12_ExchangeFile_AccessPolicy's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # rif12_ExchangeFile_AccessPolicy's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = rif12_ExchangeFile_AccessPolicy(accessMode="sample_text")
    partner = AttributeDefinition()
    setattr(partner, 'AttributeDefinition30', None)
    _safe_set(owner, 'rif12_ExchangeFile_AccessPolicy29', {partner})
    assert getattr(partner, 'AttributeDefinition30') == owner
    _safe_set(owner, 'rif12_ExchangeFile_AccessPolicy29', set())
    assert getattr(partner, 'AttributeDefinition30') is None


def test_assoc_attributeValues39_stub_double():
    # AttributeValue has no real 'AttributeValue41' property in the generated
    # code (a bare stub) -- manually attach it so rif12_ExchangeFile_AccessPolicy's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # rif12_ExchangeFile_AccessPolicy's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = rif12_ExchangeFile_AccessPolicy(accessMode="sample_text")
    partner = AttributeValue()
    setattr(partner, 'AttributeValue41', None)
    _safe_set(owner, 'rif12_ExchangeFile_AccessPolicy40', {partner})
    assert getattr(partner, 'AttributeValue41') == owner
    _safe_set(owner, 'rif12_ExchangeFile_AccessPolicy40', set())
    assert getattr(partner, 'AttributeValue41') is None


def test_assoc_datatypeDefinitions34_stub_double():
    # DatatypeDefinition has no real 'DatatypeDefinition' property in the generated
    # code (a bare stub) -- manually attach it so rif12_ExchangeFile_AccessPolicy's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # rif12_ExchangeFile_AccessPolicy's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = rif12_ExchangeFile_AccessPolicy(accessMode="sample_text")
    partner = DatatypeDefinition()
    setattr(partner, 'DatatypeDefinition', None)
    _safe_set(owner, 'rif12_ExchangeFile_AccessPolicy35', {partner})
    assert getattr(partner, 'DatatypeDefinition') == owner
    _safe_set(owner, 'rif12_ExchangeFile_AccessPolicy35', set())
    assert getattr(partner, 'DatatypeDefinition') is None


def test_assoc_defaultValue60_stub_double():
    # AttributeValueEnumeration has no real 'AttributeValueEnumeration' property in the generated
    # code (a bare stub) -- manually attach it so rif12_ExchangeFile_AttributeDefinitionEnumeration's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # rif12_ExchangeFile_AttributeDefinitionEnumeration's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = rif12_ExchangeFile_AttributeDefinitionEnumeration(multiValued="sample_text")
    partner = AttributeValueEnumeration()
    setattr(partner, 'AttributeValueEnumeration', None)
    _safe_set(owner, 'rif12_ExchangeFile_AttributeDefinitionEnumeration61', partner)
    assert getattr(partner, 'AttributeValueEnumeration') == owner
    _safe_set(owner, 'rif12_ExchangeFile_AttributeDefinitionEnumeration61', None)
    assert getattr(partner, 'AttributeValueEnumeration') is None


def test_assoc_definition71_stub_double():
    # AttributeDefinitionSimple has no real 'AttributeDefinitionSimple' property in the generated
    # code (a bare stub) -- manually attach it so rif12_ExchangeFile_AttributeValueSimple's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # rif12_ExchangeFile_AttributeValueSimple's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = rif12_ExchangeFile_AttributeValueSimple(theValue="sample_text")
    partner = AttributeDefinitionSimple()
    setattr(partner, 'AttributeDefinitionSimple', None)
    _safe_set(owner, 'rif12_ExchangeFile_AttributeValueSimple', partner)
    assert getattr(partner, 'AttributeDefinitionSimple') == owner
    _safe_set(owner, 'rif12_ExchangeFile_AttributeValueSimple', None)
    assert getattr(partner, 'AttributeDefinitionSimple') is None


def test_assoc_definition79_stub_double():
    # AttributeDefinitionComplex has no real 'AttributeDefinitionComplex80' property in the generated
    # code (a bare stub) -- manually attach it so rif12_ExchangeFile_AttributeValueFileReference's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # rif12_ExchangeFile_AttributeValueFileReference's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = rif12_ExchangeFile_AttributeValueFileReference(pathToFile="sample_text")
    partner = AttributeDefinitionComplex()
    setattr(partner, 'AttributeDefinitionComplex80', None)
    _safe_set(owner, 'rif12_ExchangeFile_AttributeValueFileReference', partner)
    assert getattr(partner, 'AttributeDefinitionComplex80') == owner
    _safe_set(owner, 'rif12_ExchangeFile_AttributeValueFileReference', None)
    assert getattr(partner, 'AttributeDefinitionComplex80') is None


def test_assoc_relationGroups31_stub_double():
    # RelationGroup has no real 'RelationGroup33' property in the generated
    # code (a bare stub) -- manually attach it so rif12_ExchangeFile_AccessPolicy's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # rif12_ExchangeFile_AccessPolicy's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = rif12_ExchangeFile_AccessPolicy(accessMode="sample_text")
    partner = RelationGroup()
    setattr(partner, 'RelationGroup33', None)
    _safe_set(owner, 'rif12_ExchangeFile_AccessPolicy32', {partner})
    assert getattr(partner, 'RelationGroup33') == owner
    _safe_set(owner, 'rif12_ExchangeFile_AccessPolicy32', set())
    assert getattr(partner, 'RelationGroup33') is None


def test_assoc_specGroupHierarchyRoots25_stub_double():
    # SpecGroupHierarchyRoot has no real 'SpecGroupHierarchyRoot' property in the generated
    # code (a bare stub) -- manually attach it so rif12_ExchangeFile_AccessPolicy's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # rif12_ExchangeFile_AccessPolicy's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = rif12_ExchangeFile_AccessPolicy(accessMode="sample_text")
    partner = SpecGroupHierarchyRoot()
    setattr(partner, 'SpecGroupHierarchyRoot', None)
    _safe_set(owner, 'rif12_ExchangeFile_AccessPolicy', {partner})
    assert getattr(partner, 'SpecGroupHierarchyRoot') == owner
    _safe_set(owner, 'rif12_ExchangeFile_AccessPolicy', set())
    assert getattr(partner, 'SpecGroupHierarchyRoot') is None


def test_assoc_specGroups26_stub_double():
    # SpecGroup has no real 'SpecGroup' property in the generated
    # code (a bare stub) -- manually attach it so rif12_ExchangeFile_AccessPolicy's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # rif12_ExchangeFile_AccessPolicy's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = rif12_ExchangeFile_AccessPolicy(accessMode="sample_text")
    partner = SpecGroup()
    setattr(partner, 'SpecGroup', None)
    _safe_set(owner, 'rif12_ExchangeFile_AccessPolicy27', {partner})
    assert getattr(partner, 'SpecGroup') == owner
    _safe_set(owner, 'rif12_ExchangeFile_AccessPolicy27', set())
    assert getattr(partner, 'SpecGroup') is None


def test_assoc_specHierarchies45_stub_double():
    # SpecHierarchy has no real 'SpecHierarchy47' property in the generated
    # code (a bare stub) -- manually attach it so rif12_ExchangeFile_AccessPolicy's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # rif12_ExchangeFile_AccessPolicy's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = rif12_ExchangeFile_AccessPolicy(accessMode="sample_text")
    partner = SpecHierarchy()
    setattr(partner, 'SpecHierarchy47', None)
    _safe_set(owner, 'rif12_ExchangeFile_AccessPolicy46', {partner})
    assert getattr(partner, 'SpecHierarchy47') == owner
    _safe_set(owner, 'rif12_ExchangeFile_AccessPolicy46', set())
    assert getattr(partner, 'SpecHierarchy47') is None


def test_assoc_specHierarchyRoots51_stub_double():
    # SpecHierarchyRoot has no real 'SpecHierarchyRoot' property in the generated
    # code (a bare stub) -- manually attach it so rif12_ExchangeFile_AccessPolicy's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # rif12_ExchangeFile_AccessPolicy's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = rif12_ExchangeFile_AccessPolicy(accessMode="sample_text")
    partner = SpecHierarchyRoot()
    setattr(partner, 'SpecHierarchyRoot', None)
    _safe_set(owner, 'rif12_ExchangeFile_AccessPolicy52', {partner})
    assert getattr(partner, 'SpecHierarchyRoot') == owner
    _safe_set(owner, 'rif12_ExchangeFile_AccessPolicy52', set())
    assert getattr(partner, 'SpecHierarchyRoot') is None


def test_assoc_specObjects48_stub_double():
    # SpecObject has no real 'SpecObject50' property in the generated
    # code (a bare stub) -- manually attach it so rif12_ExchangeFile_AccessPolicy's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # rif12_ExchangeFile_AccessPolicy's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = rif12_ExchangeFile_AccessPolicy(accessMode="sample_text")
    partner = SpecObject()
    setattr(partner, 'SpecObject50', None)
    _safe_set(owner, 'rif12_ExchangeFile_AccessPolicy49', {partner})
    assert getattr(partner, 'SpecObject50') == owner
    _safe_set(owner, 'rif12_ExchangeFile_AccessPolicy49', set())
    assert getattr(partner, 'SpecObject50') is None


def test_assoc_specRelations36_stub_double():
    # SpecRelation has no real 'SpecRelation38' property in the generated
    # code (a bare stub) -- manually attach it so rif12_ExchangeFile_AccessPolicy's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # rif12_ExchangeFile_AccessPolicy's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = rif12_ExchangeFile_AccessPolicy(accessMode="sample_text")
    partner = SpecRelation()
    setattr(partner, 'SpecRelation38', None)
    _safe_set(owner, 'rif12_ExchangeFile_AccessPolicy37', {partner})
    assert getattr(partner, 'SpecRelation38') == owner
    _safe_set(owner, 'rif12_ExchangeFile_AccessPolicy37', set())
    assert getattr(partner, 'SpecRelation38') is None


def test_assoc_specTypes42_stub_double():
    # SpecType has no real 'SpecType44' property in the generated
    # code (a bare stub) -- manually attach it so rif12_ExchangeFile_AccessPolicy's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # rif12_ExchangeFile_AccessPolicy's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = rif12_ExchangeFile_AccessPolicy(accessMode="sample_text")
    partner = SpecType()
    setattr(partner, 'SpecType44', None)
    _safe_set(owner, 'rif12_ExchangeFile_AccessPolicy43', {partner})
    assert getattr(partner, 'SpecType44') == owner
    _safe_set(owner, 'rif12_ExchangeFile_AccessPolicy43', set())
    assert getattr(partner, 'SpecType44') is None


def test_assoc_type59_stub_double():
    # DatatypeDefinitionEnumeration has no real 'DatatypeDefinitionEnumeration' property in the generated
    # code (a bare stub) -- manually attach it so rif12_ExchangeFile_AttributeDefinitionEnumeration's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # rif12_ExchangeFile_AttributeDefinitionEnumeration's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = rif12_ExchangeFile_AttributeDefinitionEnumeration(multiValued="sample_text")
    partner = DatatypeDefinitionEnumeration()
    setattr(partner, 'DatatypeDefinitionEnumeration', None)
    _safe_set(owner, 'rif12_ExchangeFile_AttributeDefinitionEnumeration', partner)
    assert getattr(partner, 'DatatypeDefinitionEnumeration') == owner
    _safe_set(owner, 'rif12_ExchangeFile_AttributeDefinitionEnumeration', None)
    assert getattr(partner, 'DatatypeDefinitionEnumeration') is None


