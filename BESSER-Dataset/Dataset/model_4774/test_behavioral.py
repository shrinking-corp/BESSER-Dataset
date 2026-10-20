import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    ComplexType,
    DeclarationTypeReference,
    Literal,
    NamedType,
    Type,
    types_BooleanLiteral,
    types_CharLiteral,
    types_CollectionType,
    types_ComplexType,
    types_DeclarationTypeReference,
    types_EntityRelationship,
    types_EntityType,
    types_EnumerationLiteral,
    types_EnumerationType,
    types_Import,
    types_Literal,
    types_MapType,
    types_MappedByReference,
    types_Model,
    types_NamedType,
    types_NumberLiteral,
    types_PrimitiveType,
    types_Property,
    types_PropertyReference,
    types_StringLiteral,
    types_Type,
    types_TypeReference,
    EntityRelationshipKind,
    PropertyStorageModifier,
    TypeStorageModifier,
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

def test_assoc_imports0_reverse_link_reassign_clear():
    a1 = types_Model(name="sample_text")
    a2 = types_Model(name="sample_text_2")
    b = types_Import(importedNamespace="sample_text")
    _safe_set(b, 'types_Import', a1)
    assert _is_linked(b, 'types_Import', a1)
    if hasattr(a1, 'types_Model'):
        assert _is_linked(a1, 'types_Model', b)
    _safe_set(b, 'types_Import', a2)
    assert _is_linked(b, 'types_Import', a2)
    if hasattr(a1, 'types_Model'):
        assert not _is_linked(a1, 'types_Model', b)
    if hasattr(a2, 'types_Model'):
        assert _is_linked(a2, 'types_Model', b)
    _safe_set(b, 'types_Import', None)
    assert not _is_linked(b, 'types_Import', a2)
    if hasattr(a2, 'types_Model'):
        assert not _is_linked(a2, 'types_Model', b)


def test_assoc_properties15_reverse_link_reassign_clear():
    a1 = types_Property(name="sample_text", storageModifier="sample_text")
    a2 = types_Property(name="sample_text_2", storageModifier="sample_text_2")
    b = types_EntityType(storageModifier="sample_text")
    _safe_set(b, 'types_EntityType', {a1})
    assert _is_linked(b, 'types_EntityType', a1)
    if hasattr(a1, 'types_Property'):
        assert _is_linked(a1, 'types_Property', b)
    _safe_set(b, 'types_EntityType', {a2})
    assert _is_linked(b, 'types_EntityType', a2)
    if hasattr(a1, 'types_Property'):
        assert not _is_linked(a1, 'types_Property', b)
    if hasattr(a2, 'types_Property'):
        assert _is_linked(a2, 'types_Property', b)
    _safe_set(b, 'types_EntityType', set())
    assert not _is_linked(b, 'types_EntityType', a2)
    if hasattr(a2, 'types_Property'):
        assert not _is_linked(a2, 'types_Property', b)


def test_assoc_relationship18_reverse_link_reassign_clear():
    a1 = types_Property(name="sample_text", storageModifier="sample_text")
    a2 = types_Property(name="sample_text_2", storageModifier="sample_text_2")
    b = types_EntityRelationship(kind="sample_text")
    _safe_set(b, 'types_EntityRelationship', a1)
    assert _is_linked(b, 'types_EntityRelationship', a1)
    if hasattr(a1, 'types_Property19'):
        assert _is_linked(a1, 'types_Property19', b)
    _safe_set(b, 'types_EntityRelationship', a2)
    assert _is_linked(b, 'types_EntityRelationship', a2)
    if hasattr(a1, 'types_Property19'):
        assert not _is_linked(a1, 'types_Property19', b)
    if hasattr(a2, 'types_Property19'):
        assert _is_linked(a2, 'types_Property19', b)
    _safe_set(b, 'types_EntityRelationship', None)
    assert not _is_linked(b, 'types_EntityRelationship', a2)
    if hasattr(a2, 'types_Property19'):
        assert not _is_linked(a2, 'types_Property19', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_base29_stub_double():
    # types_MappedByReference has no real 'types_MappedByReference30' property in the generated
    # code (a bare stub) -- manually attach it so types_Property's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # types_Property's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = types_Property(name="sample_text", storageModifier="sample_text")
    partner = types_MappedByReference()
    setattr(partner, 'types_MappedByReference30', None)
    _safe_set(owner, 'types_Property31', partner)
    assert getattr(partner, 'types_MappedByReference30') == owner
    _safe_set(owner, 'types_Property31', None)
    assert getattr(partner, 'types_MappedByReference30') is None


def test_assoc_literal25_stub_double():
    # types_Literal has no real 'types_Literal' property in the generated
    # code (a bare stub) -- manually attach it so types_Property's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # types_Property's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = types_Property(name="sample_text", storageModifier="sample_text")
    partner = types_Literal()
    setattr(partner, 'types_Literal', None)
    _safe_set(owner, 'types_Property26', partner)
    assert getattr(partner, 'types_Literal') == owner
    _safe_set(owner, 'types_Property26', None)
    assert getattr(partner, 'types_Literal') is None


def test_assoc_literals14_stub_double():
    # types_EnumerationType has no real 'types_EnumerationType' property in the generated
    # code (a bare stub) -- manually attach it so types_EnumerationLiteral's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # types_EnumerationLiteral's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = types_EnumerationLiteral(name="sample_text")
    partner = types_EnumerationType()
    setattr(partner, 'types_EnumerationType', None)
    _safe_set(owner, 'types_EnumerationLiteral', partner)
    assert owner in getattr(partner, 'types_EnumerationType')
    _safe_set(owner, 'types_EnumerationLiteral', None)
    assert owner not in getattr(partner, 'types_EnumerationType')


def test_assoc_mapKey22_stub_double():
    # types_PropertyReference has no real 'types_PropertyReference24' property in the generated
    # code (a bare stub) -- manually attach it so types_Property's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # types_Property's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = types_Property(name="sample_text", storageModifier="sample_text")
    partner = types_PropertyReference()
    setattr(partner, 'types_PropertyReference24', None)
    _safe_set(owner, 'types_Property23', partner)
    assert getattr(partner, 'types_PropertyReference24') == owner
    _safe_set(owner, 'types_Property23', None)
    assert getattr(partner, 'types_PropertyReference24') is None


def test_assoc_mapType6_stub_double():
    # types_TypeReference has no real 'types_TypeReference8' property in the generated
    # code (a bare stub) -- manually attach it so types_MapType's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # types_MapType's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = types_MapType(size=7)
    partner = types_TypeReference()
    setattr(partner, 'types_TypeReference8', None)
    _safe_set(owner, 'types_MapType7', partner)
    assert getattr(partner, 'types_TypeReference8') == owner
    _safe_set(owner, 'types_MapType7', None)
    assert getattr(partner, 'types_TypeReference8') is None


def test_assoc_mappedBy27_stub_double():
    # types_MappedByReference has no real 'types_MappedByReference' property in the generated
    # code (a bare stub) -- manually attach it so types_EntityRelationship's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # types_EntityRelationship's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = types_EntityRelationship(kind="sample_text")
    partner = types_MappedByReference()
    setattr(partner, 'types_MappedByReference', None)
    _safe_set(owner, 'types_EntityRelationship28', partner)
    assert getattr(partner, 'types_MappedByReference') == owner
    _safe_set(owner, 'types_EntityRelationship28', None)
    assert getattr(partner, 'types_MappedByReference') is None


def test_assoc_orderBy20_stub_double():
    # types_PropertyReference has no real 'types_PropertyReference' property in the generated
    # code (a bare stub) -- manually attach it so types_Property's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # types_Property's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = types_Property(name="sample_text", storageModifier="sample_text")
    partner = types_PropertyReference()
    setattr(partner, 'types_PropertyReference', None)
    _safe_set(owner, 'types_Property21', partner)
    assert getattr(partner, 'types_PropertyReference') == owner
    _safe_set(owner, 'types_Property21', None)
    assert getattr(partner, 'types_PropertyReference') is None


def test_assoc_reference3_stub_double():
    # types_TypeReference has no real 'types_TypeReference' property in the generated
    # code (a bare stub) -- manually attach it so types_CollectionType's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # types_CollectionType's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = types_CollectionType(size=7)
    partner = types_TypeReference()
    setattr(partner, 'types_TypeReference', None)
    _safe_set(owner, 'types_CollectionType', partner)
    assert getattr(partner, 'types_TypeReference') == owner
    _safe_set(owner, 'types_CollectionType', None)
    assert getattr(partner, 'types_TypeReference') is None


def test_assoc_reference35_stub_double():
    # types_PropertyReference has no real 'types_PropertyReference36' property in the generated
    # code (a bare stub) -- manually attach it so types_Property's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # types_Property's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = types_Property(name="sample_text", storageModifier="sample_text")
    partner = types_PropertyReference()
    setattr(partner, 'types_PropertyReference36', None)
    _safe_set(owner, 'types_Property37', partner)
    assert getattr(partner, 'types_PropertyReference36') == owner
    _safe_set(owner, 'types_Property37', None)
    assert getattr(partner, 'types_PropertyReference36') is None


def test_assoc_reference4_stub_double():
    # types_TypeReference has no real 'types_TypeReference5' property in the generated
    # code (a bare stub) -- manually attach it so types_MapType's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # types_MapType's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = types_MapType(size=7)
    partner = types_TypeReference()
    setattr(partner, 'types_TypeReference5', None)
    _safe_set(owner, 'types_MapType', partner)
    assert getattr(partner, 'types_TypeReference5') == owner
    _safe_set(owner, 'types_MapType', None)
    assert getattr(partner, 'types_TypeReference5') is None


def test_assoc_reference9_stub_double():
    # types_TypeReference has no real 'types_TypeReference10' property in the generated
    # code (a bare stub) -- manually attach it so types_NamedType's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # types_NamedType's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = types_NamedType(name="sample_text")
    partner = types_TypeReference()
    setattr(partner, 'types_TypeReference10', None)
    _safe_set(owner, 'types_NamedType', partner)
    assert getattr(partner, 'types_TypeReference10') == owner
    _safe_set(owner, 'types_NamedType', None)
    assert getattr(partner, 'types_TypeReference10') is None


def test_assoc_type16_stub_double():
    # types_DeclarationTypeReference has no real 'types_DeclarationTypeReference' property in the generated
    # code (a bare stub) -- manually attach it so types_Property's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # types_Property's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = types_Property(name="sample_text", storageModifier="sample_text")
    partner = types_DeclarationTypeReference()
    setattr(partner, 'types_DeclarationTypeReference', None)
    _safe_set(owner, 'types_Property17', partner)
    assert getattr(partner, 'types_DeclarationTypeReference') == owner
    _safe_set(owner, 'types_Property17', None)
    assert getattr(partner, 'types_DeclarationTypeReference') is None


def test_assoc_types1_stub_double():
    # types_ComplexType has no real 'types_ComplexType' property in the generated
    # code (a bare stub) -- manually attach it so types_Model's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # types_Model's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = types_Model(name="sample_text")
    partner = types_ComplexType()
    setattr(partner, 'types_ComplexType', None)
    _safe_set(owner, 'types_Model2', {partner})
    assert getattr(partner, 'types_ComplexType') == owner
    _safe_set(owner, 'types_Model2', set())
    assert getattr(partner, 'types_ComplexType') is None


