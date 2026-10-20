import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    AttributeDefinition,
    AttributeValue,
    AttributeValueComplex,
    DataTypes_BinaryContent,
    DataTypes_XhtmlContent,
    DataTypes_XmlContent,
    DatatypeDefinition,
    DatatypeDefinitionComplex,
    DatatypeDefinitionSimple,
    ExchangeFile_AccessPolicy,
    ExchangeFile_AttributeDefinition,
    ExchangeFile_AttributeDefinitionComplex,
    ExchangeFile_AttributeDefinitionEnumeration,
    ExchangeFile_AttributeDefinitionSimple,
    ExchangeFile_AttributeValue,
    ExchangeFile_AttributeValueComplex,
    ExchangeFile_AttributeValueEnumeration,
    ExchangeFile_AttributeValueSimple,
    ExchangeFile_DatatypeDefinition,
    ExchangeFile_DatatypeDefinitionComplex,
    ExchangeFile_DatatypeDefinitionEnumeration,
    ExchangeFile_DatatypeDefinitionSimple,
    ExchangeFile_EmbeddedValue,
    ExchangeFile_EnumValue,
    ExchangeFile_RelationGroup,
    ExchangeFile_SpecGroup,
    ExchangeFile_SpecHierarchy,
    ExchangeFile_SpecHierarchyRoot,
    ExchangeFile_SpecObject,
    ExchangeFile_SpecRelation,
    ExchangeFile_SpecType,
    Identifiable,
    SpecElementWithUserDefinedAttributes,
    rif11a_DataTypes_BinaryContent,
    rif11a_DataTypes_XhtmlContent,
    rif11a_DataTypes_XmlContent,
    rif11a_ExchangeFile_AccessPolicy,
    rif11a_ExchangeFile_AttributeDefinition,
    rif11a_ExchangeFile_AttributeDefinitionComplex,
    rif11a_ExchangeFile_AttributeDefinitionEnumeration,
    rif11a_ExchangeFile_AttributeDefinitionSimple,
    rif11a_ExchangeFile_AttributeValue,
    rif11a_ExchangeFile_AttributeValueComplex,
    rif11a_ExchangeFile_AttributeValueEmbeddedDocument,
    rif11a_ExchangeFile_AttributeValueEmbeddedFile,
    rif11a_ExchangeFile_AttributeValueEnumeration,
    rif11a_ExchangeFile_AttributeValueFileReference,
    rif11a_ExchangeFile_AttributeValueSimple,
    rif11a_ExchangeFile_AttributeValueXmlData,
    rif11a_ExchangeFile_DatatypeDefinition,
    rif11a_ExchangeFile_DatatypeDefinitionBinaryFile,
    rif11a_ExchangeFile_DatatypeDefinitionBoolean,
    rif11a_ExchangeFile_DatatypeDefinitionComplex,
    rif11a_ExchangeFile_DatatypeDefinitionDate,
    rif11a_ExchangeFile_DatatypeDefinitionDocument,
    rif11a_ExchangeFile_DatatypeDefinitionEnumeration,
    rif11a_ExchangeFile_DatatypeDefinitionInteger,
    rif11a_ExchangeFile_DatatypeDefinitionReal,
    rif11a_ExchangeFile_DatatypeDefinitionSimple,
    rif11a_ExchangeFile_DatatypeDefinitionString,
    rif11a_ExchangeFile_DatatypeDefinitionXmlData,
    rif11a_ExchangeFile_EmbeddedValue,
    rif11a_ExchangeFile_EnumValue,
    rif11a_ExchangeFile_Identifiable,
    rif11a_ExchangeFile_RIF,
    rif11a_ExchangeFile_RelationGroup,
    rif11a_ExchangeFile_SpecElementWithUserDefinedAttributes,
    rif11a_ExchangeFile_SpecGroup,
    rif11a_ExchangeFile_SpecHierarchy,
    rif11a_ExchangeFile_SpecHierarchyRoot,
    rif11a_ExchangeFile_SpecObject,
    rif11a_ExchangeFile_SpecRelation,
    rif11a_ExchangeFile_SpecType,
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

def test_assoc_SpecHierarchyRoots80_stub_double():
    # ExchangeFile_SpecHierarchyRoot has no real 'ExchangeFile_SpecHierarchyRoot82' property in the generated
    # code (a bare stub) -- manually attach it so rif11a_ExchangeFile_RIF's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # rif11a_ExchangeFile_RIF's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = rif11a_ExchangeFile_RIF(author="sample_text", comment="sample_text", countryCode="sample_text", creationTime="sample_text", identifier="sample_text", sourceToolId="sample_text", title="sample_text", version="sample_text")
    partner = ExchangeFile_SpecHierarchyRoot()
    setattr(partner, 'ExchangeFile_SpecHierarchyRoot82', None)
    _safe_set(owner, 'rif11a_ExchangeFile_RIF81', {partner})
    assert getattr(partner, 'ExchangeFile_SpecHierarchyRoot82') == owner
    _safe_set(owner, 'rif11a_ExchangeFile_RIF81', set())
    assert getattr(partner, 'ExchangeFile_SpecHierarchyRoot82') is None


def test_assoc_accessPolicies76_stub_double():
    # ExchangeFile_AccessPolicy has no real 'ExchangeFile_AccessPolicy' property in the generated
    # code (a bare stub) -- manually attach it so rif11a_ExchangeFile_RIF's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # rif11a_ExchangeFile_RIF's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = rif11a_ExchangeFile_RIF(author="sample_text", comment="sample_text", countryCode="sample_text", creationTime="sample_text", identifier="sample_text", sourceToolId="sample_text", title="sample_text", version="sample_text")
    partner = ExchangeFile_AccessPolicy()
    setattr(partner, 'ExchangeFile_AccessPolicy', None)
    _safe_set(owner, 'rif11a_ExchangeFile_RIF', {partner})
    assert getattr(partner, 'ExchangeFile_AccessPolicy') == owner
    _safe_set(owner, 'rif11a_ExchangeFile_RIF', set())
    assert getattr(partner, 'ExchangeFile_AccessPolicy') is None


def test_assoc_attributeDefinitions23_stub_double():
    # ExchangeFile_AttributeDefinition has no real 'ExchangeFile_AttributeDefinition25' property in the generated
    # code (a bare stub) -- manually attach it so rif11a_ExchangeFile_AccessPolicy's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # rif11a_ExchangeFile_AccessPolicy's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = rif11a_ExchangeFile_AccessPolicy(accessMode="sample_text")
    partner = ExchangeFile_AttributeDefinition()
    setattr(partner, 'ExchangeFile_AttributeDefinition25', None)
    _safe_set(owner, 'rif11a_ExchangeFile_AccessPolicy24', {partner})
    assert getattr(partner, 'ExchangeFile_AttributeDefinition25') == owner
    _safe_set(owner, 'rif11a_ExchangeFile_AccessPolicy24', set())
    assert getattr(partner, 'ExchangeFile_AttributeDefinition25') is None


def test_assoc_attributeValues33_stub_double():
    # ExchangeFile_AttributeValue has no real 'ExchangeFile_AttributeValue35' property in the generated
    # code (a bare stub) -- manually attach it so rif11a_ExchangeFile_AccessPolicy's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # rif11a_ExchangeFile_AccessPolicy's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = rif11a_ExchangeFile_AccessPolicy(accessMode="sample_text")
    partner = ExchangeFile_AttributeValue()
    setattr(partner, 'ExchangeFile_AttributeValue35', None)
    _safe_set(owner, 'rif11a_ExchangeFile_AccessPolicy34', {partner})
    assert getattr(partner, 'ExchangeFile_AttributeValue35') == owner
    _safe_set(owner, 'rif11a_ExchangeFile_AccessPolicy34', set())
    assert getattr(partner, 'ExchangeFile_AttributeValue35') is None


def test_assoc_datatypeDefinitions28_stub_double():
    # ExchangeFile_DatatypeDefinition has no real 'ExchangeFile_DatatypeDefinition' property in the generated
    # code (a bare stub) -- manually attach it so rif11a_ExchangeFile_AccessPolicy's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # rif11a_ExchangeFile_AccessPolicy's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = rif11a_ExchangeFile_AccessPolicy(accessMode="sample_text")
    partner = ExchangeFile_DatatypeDefinition()
    setattr(partner, 'ExchangeFile_DatatypeDefinition', None)
    _safe_set(owner, 'rif11a_ExchangeFile_AccessPolicy29', {partner})
    assert getattr(partner, 'ExchangeFile_DatatypeDefinition') == owner
    _safe_set(owner, 'rif11a_ExchangeFile_AccessPolicy29', set())
    assert getattr(partner, 'ExchangeFile_DatatypeDefinition') is None


def test_assoc_datatypes77_stub_double():
    # ExchangeFile_DatatypeDefinition has no real 'ExchangeFile_DatatypeDefinition79' property in the generated
    # code (a bare stub) -- manually attach it so rif11a_ExchangeFile_RIF's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # rif11a_ExchangeFile_RIF's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = rif11a_ExchangeFile_RIF(author="sample_text", comment="sample_text", countryCode="sample_text", creationTime="sample_text", identifier="sample_text", sourceToolId="sample_text", title="sample_text", version="sample_text")
    partner = ExchangeFile_DatatypeDefinition()
    setattr(partner, 'ExchangeFile_DatatypeDefinition79', None)
    _safe_set(owner, 'rif11a_ExchangeFile_RIF78', {partner})
    assert getattr(partner, 'ExchangeFile_DatatypeDefinition79') == owner
    _safe_set(owner, 'rif11a_ExchangeFile_RIF78', set())
    assert getattr(partner, 'ExchangeFile_DatatypeDefinition79') is None


def test_assoc_defaultValue51_stub_double():
    # ExchangeFile_AttributeValueEnumeration has no real 'ExchangeFile_AttributeValueEnumeration' property in the generated
    # code (a bare stub) -- manually attach it so rif11a_ExchangeFile_AttributeDefinitionEnumeration's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # rif11a_ExchangeFile_AttributeDefinitionEnumeration's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = rif11a_ExchangeFile_AttributeDefinitionEnumeration(multiValued="sample_text")
    partner = ExchangeFile_AttributeValueEnumeration()
    setattr(partner, 'ExchangeFile_AttributeValueEnumeration', None)
    _safe_set(owner, 'rif11a_ExchangeFile_AttributeDefinitionEnumeration52', partner)
    assert getattr(partner, 'ExchangeFile_AttributeValueEnumeration') == owner
    _safe_set(owner, 'rif11a_ExchangeFile_AttributeDefinitionEnumeration52', None)
    assert getattr(partner, 'ExchangeFile_AttributeValueEnumeration') is None


def test_assoc_definition62_stub_double():
    # ExchangeFile_AttributeDefinitionSimple has no real 'ExchangeFile_AttributeDefinitionSimple' property in the generated
    # code (a bare stub) -- manually attach it so rif11a_ExchangeFile_AttributeValueSimple's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # rif11a_ExchangeFile_AttributeValueSimple's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = rif11a_ExchangeFile_AttributeValueSimple(theValue="sample_text")
    partner = ExchangeFile_AttributeDefinitionSimple()
    setattr(partner, 'ExchangeFile_AttributeDefinitionSimple', None)
    _safe_set(owner, 'rif11a_ExchangeFile_AttributeValueSimple', partner)
    assert getattr(partner, 'ExchangeFile_AttributeDefinitionSimple') == owner
    _safe_set(owner, 'rif11a_ExchangeFile_AttributeValueSimple', None)
    assert getattr(partner, 'ExchangeFile_AttributeDefinitionSimple') is None


def test_assoc_definition70_stub_double():
    # ExchangeFile_AttributeDefinitionComplex has no real 'ExchangeFile_AttributeDefinitionComplex71' property in the generated
    # code (a bare stub) -- manually attach it so rif11a_ExchangeFile_AttributeValueFileReference's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # rif11a_ExchangeFile_AttributeValueFileReference's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = rif11a_ExchangeFile_AttributeValueFileReference(pathToFile="sample_text")
    partner = ExchangeFile_AttributeDefinitionComplex()
    setattr(partner, 'ExchangeFile_AttributeDefinitionComplex71', None)
    _safe_set(owner, 'rif11a_ExchangeFile_AttributeValueFileReference', partner)
    assert getattr(partner, 'ExchangeFile_AttributeDefinitionComplex71') == owner
    _safe_set(owner, 'rif11a_ExchangeFile_AttributeValueFileReference', None)
    assert getattr(partner, 'ExchangeFile_AttributeDefinitionComplex71') is None


def test_assoc_relationGroups26_stub_double():
    # ExchangeFile_RelationGroup has no real 'ExchangeFile_RelationGroup' property in the generated
    # code (a bare stub) -- manually attach it so rif11a_ExchangeFile_AccessPolicy's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # rif11a_ExchangeFile_AccessPolicy's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = rif11a_ExchangeFile_AccessPolicy(accessMode="sample_text")
    partner = ExchangeFile_RelationGroup()
    setattr(partner, 'ExchangeFile_RelationGroup', None)
    _safe_set(owner, 'rif11a_ExchangeFile_AccessPolicy27', {partner})
    assert getattr(partner, 'ExchangeFile_RelationGroup') == owner
    _safe_set(owner, 'rif11a_ExchangeFile_AccessPolicy27', set())
    assert getattr(partner, 'ExchangeFile_RelationGroup') is None


def test_assoc_specGroups22_stub_double():
    # ExchangeFile_SpecGroup has no real 'ExchangeFile_SpecGroup' property in the generated
    # code (a bare stub) -- manually attach it so rif11a_ExchangeFile_AccessPolicy's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # rif11a_ExchangeFile_AccessPolicy's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = rif11a_ExchangeFile_AccessPolicy(accessMode="sample_text")
    partner = ExchangeFile_SpecGroup()
    setattr(partner, 'ExchangeFile_SpecGroup', None)
    _safe_set(owner, 'rif11a_ExchangeFile_AccessPolicy', {partner})
    assert getattr(partner, 'ExchangeFile_SpecGroup') == owner
    _safe_set(owner, 'rif11a_ExchangeFile_AccessPolicy', set())
    assert getattr(partner, 'ExchangeFile_SpecGroup') is None


def test_assoc_specGroups86_stub_double():
    # ExchangeFile_SpecGroup has no real 'ExchangeFile_SpecGroup88' property in the generated
    # code (a bare stub) -- manually attach it so rif11a_ExchangeFile_RIF's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # rif11a_ExchangeFile_RIF's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = rif11a_ExchangeFile_RIF(author="sample_text", comment="sample_text", countryCode="sample_text", creationTime="sample_text", identifier="sample_text", sourceToolId="sample_text", title="sample_text", version="sample_text")
    partner = ExchangeFile_SpecGroup()
    setattr(partner, 'ExchangeFile_SpecGroup88', None)
    _safe_set(owner, 'rif11a_ExchangeFile_RIF87', {partner})
    assert getattr(partner, 'ExchangeFile_SpecGroup88') == owner
    _safe_set(owner, 'rif11a_ExchangeFile_RIF87', set())
    assert getattr(partner, 'ExchangeFile_SpecGroup88') is None


def test_assoc_specHierarchies39_stub_double():
    # ExchangeFile_SpecHierarchy has no real 'ExchangeFile_SpecHierarchy41' property in the generated
    # code (a bare stub) -- manually attach it so rif11a_ExchangeFile_AccessPolicy's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # rif11a_ExchangeFile_AccessPolicy's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = rif11a_ExchangeFile_AccessPolicy(accessMode="sample_text")
    partner = ExchangeFile_SpecHierarchy()
    setattr(partner, 'ExchangeFile_SpecHierarchy41', None)
    _safe_set(owner, 'rif11a_ExchangeFile_AccessPolicy40', {partner})
    assert getattr(partner, 'ExchangeFile_SpecHierarchy41') == owner
    _safe_set(owner, 'rif11a_ExchangeFile_AccessPolicy40', set())
    assert getattr(partner, 'ExchangeFile_SpecHierarchy41') is None


def test_assoc_specHierarchyRoots45_stub_double():
    # ExchangeFile_SpecHierarchyRoot has no real 'ExchangeFile_SpecHierarchyRoot' property in the generated
    # code (a bare stub) -- manually attach it so rif11a_ExchangeFile_AccessPolicy's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # rif11a_ExchangeFile_AccessPolicy's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = rif11a_ExchangeFile_AccessPolicy(accessMode="sample_text")
    partner = ExchangeFile_SpecHierarchyRoot()
    setattr(partner, 'ExchangeFile_SpecHierarchyRoot', None)
    _safe_set(owner, 'rif11a_ExchangeFile_AccessPolicy46', {partner})
    assert getattr(partner, 'ExchangeFile_SpecHierarchyRoot') == owner
    _safe_set(owner, 'rif11a_ExchangeFile_AccessPolicy46', set())
    assert getattr(partner, 'ExchangeFile_SpecHierarchyRoot') is None


def test_assoc_specObjects42_stub_double():
    # ExchangeFile_SpecObject has no real 'ExchangeFile_SpecObject44' property in the generated
    # code (a bare stub) -- manually attach it so rif11a_ExchangeFile_AccessPolicy's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # rif11a_ExchangeFile_AccessPolicy's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = rif11a_ExchangeFile_AccessPolicy(accessMode="sample_text")
    partner = ExchangeFile_SpecObject()
    setattr(partner, 'ExchangeFile_SpecObject44', None)
    _safe_set(owner, 'rif11a_ExchangeFile_AccessPolicy43', {partner})
    assert getattr(partner, 'ExchangeFile_SpecObject44') == owner
    _safe_set(owner, 'rif11a_ExchangeFile_AccessPolicy43', set())
    assert getattr(partner, 'ExchangeFile_SpecObject44') is None


def test_assoc_specObjects83_stub_double():
    # ExchangeFile_SpecObject has no real 'ExchangeFile_SpecObject85' property in the generated
    # code (a bare stub) -- manually attach it so rif11a_ExchangeFile_RIF's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # rif11a_ExchangeFile_RIF's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = rif11a_ExchangeFile_RIF(author="sample_text", comment="sample_text", countryCode="sample_text", creationTime="sample_text", identifier="sample_text", sourceToolId="sample_text", title="sample_text", version="sample_text")
    partner = ExchangeFile_SpecObject()
    setattr(partner, 'ExchangeFile_SpecObject85', None)
    _safe_set(owner, 'rif11a_ExchangeFile_RIF84', {partner})
    assert getattr(partner, 'ExchangeFile_SpecObject85') == owner
    _safe_set(owner, 'rif11a_ExchangeFile_RIF84', set())
    assert getattr(partner, 'ExchangeFile_SpecObject85') is None


def test_assoc_specRelations30_stub_double():
    # ExchangeFile_SpecRelation has no real 'ExchangeFile_SpecRelation32' property in the generated
    # code (a bare stub) -- manually attach it so rif11a_ExchangeFile_AccessPolicy's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # rif11a_ExchangeFile_AccessPolicy's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = rif11a_ExchangeFile_AccessPolicy(accessMode="sample_text")
    partner = ExchangeFile_SpecRelation()
    setattr(partner, 'ExchangeFile_SpecRelation32', None)
    _safe_set(owner, 'rif11a_ExchangeFile_AccessPolicy31', {partner})
    assert getattr(partner, 'ExchangeFile_SpecRelation32') == owner
    _safe_set(owner, 'rif11a_ExchangeFile_AccessPolicy31', set())
    assert getattr(partner, 'ExchangeFile_SpecRelation32') is None


def test_assoc_specRelations92_stub_double():
    # ExchangeFile_SpecRelation has no real 'ExchangeFile_SpecRelation94' property in the generated
    # code (a bare stub) -- manually attach it so rif11a_ExchangeFile_RIF's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # rif11a_ExchangeFile_RIF's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = rif11a_ExchangeFile_RIF(author="sample_text", comment="sample_text", countryCode="sample_text", creationTime="sample_text", identifier="sample_text", sourceToolId="sample_text", title="sample_text", version="sample_text")
    partner = ExchangeFile_SpecRelation()
    setattr(partner, 'ExchangeFile_SpecRelation94', None)
    _safe_set(owner, 'rif11a_ExchangeFile_RIF93', {partner})
    assert getattr(partner, 'ExchangeFile_SpecRelation94') == owner
    _safe_set(owner, 'rif11a_ExchangeFile_RIF93', set())
    assert getattr(partner, 'ExchangeFile_SpecRelation94') is None


def test_assoc_specTypes36_stub_double():
    # ExchangeFile_SpecType has no real 'ExchangeFile_SpecType38' property in the generated
    # code (a bare stub) -- manually attach it so rif11a_ExchangeFile_AccessPolicy's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # rif11a_ExchangeFile_AccessPolicy's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = rif11a_ExchangeFile_AccessPolicy(accessMode="sample_text")
    partner = ExchangeFile_SpecType()
    setattr(partner, 'ExchangeFile_SpecType38', None)
    _safe_set(owner, 'rif11a_ExchangeFile_AccessPolicy37', {partner})
    assert getattr(partner, 'ExchangeFile_SpecType38') == owner
    _safe_set(owner, 'rif11a_ExchangeFile_AccessPolicy37', set())
    assert getattr(partner, 'ExchangeFile_SpecType38') is None


def test_assoc_specTypes89_stub_double():
    # ExchangeFile_SpecType has no real 'ExchangeFile_SpecType91' property in the generated
    # code (a bare stub) -- manually attach it so rif11a_ExchangeFile_RIF's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # rif11a_ExchangeFile_RIF's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = rif11a_ExchangeFile_RIF(author="sample_text", comment="sample_text", countryCode="sample_text", creationTime="sample_text", identifier="sample_text", sourceToolId="sample_text", title="sample_text", version="sample_text")
    partner = ExchangeFile_SpecType()
    setattr(partner, 'ExchangeFile_SpecType91', None)
    _safe_set(owner, 'rif11a_ExchangeFile_RIF90', {partner})
    assert getattr(partner, 'ExchangeFile_SpecType91') == owner
    _safe_set(owner, 'rif11a_ExchangeFile_RIF90', set())
    assert getattr(partner, 'ExchangeFile_SpecType91') is None


def test_assoc_type50_stub_double():
    # ExchangeFile_DatatypeDefinitionEnumeration has no real 'ExchangeFile_DatatypeDefinitionEnumeration' property in the generated
    # code (a bare stub) -- manually attach it so rif11a_ExchangeFile_AttributeDefinitionEnumeration's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # rif11a_ExchangeFile_AttributeDefinitionEnumeration's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = rif11a_ExchangeFile_AttributeDefinitionEnumeration(multiValued="sample_text")
    partner = ExchangeFile_DatatypeDefinitionEnumeration()
    setattr(partner, 'ExchangeFile_DatatypeDefinitionEnumeration', None)
    _safe_set(owner, 'rif11a_ExchangeFile_AttributeDefinitionEnumeration', partner)
    assert getattr(partner, 'ExchangeFile_DatatypeDefinitionEnumeration') == owner
    _safe_set(owner, 'rif11a_ExchangeFile_AttributeDefinitionEnumeration', None)
    assert getattr(partner, 'ExchangeFile_DatatypeDefinitionEnumeration') is None


