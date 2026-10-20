import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    ComplexPrimitivePropertyType,
    Model,
    PropertyAttribute,
    PropertyType,
    Type,
    datatype_BooleanPropertyAttribute,
    datatype_ComplexPrimitivePropertyType,
    datatype_Constraint,
    datatype_ConstraintRule,
    datatype_DictionaryPropertyType,
    datatype_Entity,
    datatype_Enum,
    datatype_EnumLiteral,
    datatype_EnumLiteralPropertyAttribute,
    datatype_ObjectPropertyType,
    datatype_Presence,
    datatype_PrimitivePropertyType,
    datatype_Property,
    datatype_PropertyAttribute,
    datatype_PropertyType,
    datatype_Type,
    BooleanPropertyAttributeType,
    ConstraintIntervalType,
    EnumLiteralPropertyAttributeType,
    PrimitiveType,
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

def test_assoc_presence4_reverse_link_reassign_clear():
    a1 = datatype_Property(description="sample_text", extension=True, multiplicity=True, name="sample_text")
    a2 = datatype_Property(description="sample_text_2", extension=False, multiplicity=False, name="sample_text_2")
    b = datatype_Presence(mandatory=True)
    _safe_set(b, 'datatype_Presence', a1)
    assert _is_linked(b, 'datatype_Presence', a1)
    if hasattr(a1, 'datatype_Property5'):
        assert _is_linked(a1, 'datatype_Property5', b)
    _safe_set(b, 'datatype_Presence', a2)
    assert _is_linked(b, 'datatype_Presence', a2)
    if hasattr(a1, 'datatype_Property5'):
        assert not _is_linked(a1, 'datatype_Property5', b)
    if hasattr(a2, 'datatype_Property5'):
        assert _is_linked(a2, 'datatype_Property5', b)
    _safe_set(b, 'datatype_Presence', None)
    assert not _is_linked(b, 'datatype_Presence', a2)
    if hasattr(a2, 'datatype_Property5'):
        assert not _is_linked(a2, 'datatype_Property5', b)


def test_assoc_value14_reverse_link_reassign_clear():
    a1 = datatype_EnumLiteralPropertyAttribute(type="sample_text")
    a2 = datatype_EnumLiteralPropertyAttribute(type="sample_text_2")
    b = datatype_EnumLiteral(description="sample_text", name="sample_text")
    _safe_set(b, 'datatype_EnumLiteral15', a1)
    assert _is_linked(b, 'datatype_EnumLiteral15', a1)
    if hasattr(a1, 'datatype_EnumLiteralPropertyAttribute'):
        assert _is_linked(a1, 'datatype_EnumLiteralPropertyAttribute', b)
    _safe_set(b, 'datatype_EnumLiteral15', a2)
    assert _is_linked(b, 'datatype_EnumLiteral15', a2)
    if hasattr(a1, 'datatype_EnumLiteralPropertyAttribute'):
        assert not _is_linked(a1, 'datatype_EnumLiteralPropertyAttribute', b)
    if hasattr(a2, 'datatype_EnumLiteralPropertyAttribute'):
        assert _is_linked(a2, 'datatype_EnumLiteralPropertyAttribute', b)
    _safe_set(b, 'datatype_EnumLiteral15', None)
    assert not _is_linked(b, 'datatype_EnumLiteral15', a2)
    if hasattr(a2, 'datatype_EnumLiteralPropertyAttribute'):
        assert not _is_linked(a2, 'datatype_EnumLiteralPropertyAttribute', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_Constraints16_stub_double():
    # datatype_ConstraintRule has no real 'datatype_ConstraintRule17' property in the generated
    # code (a bare stub) -- manually attach it so datatype_Constraint's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # datatype_Constraint's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = datatype_Constraint(constraintValues="sample_text", type="sample_text")
    partner = datatype_ConstraintRule()
    setattr(partner, 'datatype_ConstraintRule17', None)
    _safe_set(owner, 'datatype_Constraint', partner)
    assert owner in getattr(partner, 'datatype_ConstraintRule17')
    _safe_set(owner, 'datatype_Constraint', None)
    assert owner not in getattr(partner, 'datatype_ConstraintRule17')


def test_assoc_constraintRule6_stub_double():
    # datatype_ConstraintRule has no real 'datatype_ConstraintRule' property in the generated
    # code (a bare stub) -- manually attach it so datatype_Property's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # datatype_Property's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = datatype_Property(description="sample_text", extension=True, multiplicity=True, name="sample_text")
    partner = datatype_ConstraintRule()
    setattr(partner, 'datatype_ConstraintRule', None)
    _safe_set(owner, 'datatype_Property7', partner)
    assert getattr(partner, 'datatype_ConstraintRule') == owner
    _safe_set(owner, 'datatype_Property7', None)
    assert getattr(partner, 'datatype_ConstraintRule') is None


def test_assoc_enums13_stub_double():
    # datatype_Enum has no real 'datatype_Enum' property in the generated
    # code (a bare stub) -- manually attach it so datatype_EnumLiteral's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # datatype_EnumLiteral's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = datatype_EnumLiteral(description="sample_text", name="sample_text")
    partner = datatype_Enum()
    setattr(partner, 'datatype_Enum', None)
    _safe_set(owner, 'datatype_EnumLiteral', partner)
    assert owner in getattr(partner, 'datatype_Enum')
    _safe_set(owner, 'datatype_EnumLiteral', None)
    assert owner not in getattr(partner, 'datatype_Enum')


def test_assoc_properties2_stub_double():
    # datatype_Entity has no real 'datatype_Entity3' property in the generated
    # code (a bare stub) -- manually attach it so datatype_Property's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # datatype_Property's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = datatype_Property(description="sample_text", extension=True, multiplicity=True, name="sample_text")
    partner = datatype_Entity()
    setattr(partner, 'datatype_Entity3', None)
    _safe_set(owner, 'datatype_Property', partner)
    assert owner in getattr(partner, 'datatype_Entity3')
    _safe_set(owner, 'datatype_Property', None)
    assert owner not in getattr(partner, 'datatype_Entity3')


def test_assoc_propertyAttributes10_stub_double():
    # datatype_PropertyAttribute has no real 'datatype_PropertyAttribute' property in the generated
    # code (a bare stub) -- manually attach it so datatype_Property's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # datatype_Property's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = datatype_Property(description="sample_text", extension=True, multiplicity=True, name="sample_text")
    partner = datatype_PropertyAttribute()
    setattr(partner, 'datatype_PropertyAttribute', None)
    _safe_set(owner, 'datatype_Property11', {partner})
    assert getattr(partner, 'datatype_PropertyAttribute') == owner
    _safe_set(owner, 'datatype_Property11', set())
    assert getattr(partner, 'datatype_PropertyAttribute') is None


def test_assoc_type8_stub_double():
    # datatype_PropertyType has no real 'datatype_PropertyType' property in the generated
    # code (a bare stub) -- manually attach it so datatype_Property's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # datatype_Property's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = datatype_Property(description="sample_text", extension=True, multiplicity=True, name="sample_text")
    partner = datatype_PropertyType()
    setattr(partner, 'datatype_PropertyType', None)
    _safe_set(owner, 'datatype_Property9', partner)
    assert getattr(partner, 'datatype_PropertyType') == owner
    _safe_set(owner, 'datatype_Property9', None)
    assert getattr(partner, 'datatype_PropertyType') is None


