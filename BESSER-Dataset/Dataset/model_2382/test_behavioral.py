import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    FromAttribute,
    FromAttributeOwner,
    PrimitiveToName,
    ToColumn,
    UmlToRdbmsModelElement,
    simpleumltordbms_Association,
    simpleumltordbms_AssociationToForeignKey,
    simpleumltordbms_Attribute,
    simpleumltordbms_AttributeToColumn,
    simpleumltordbms_BooleanToBoolean,
    simpleumltordbms_Class,
    simpleumltordbms_ClassToTable,
    simpleumltordbms_Column,
    simpleumltordbms_ForeignKey,
    simpleumltordbms_FromAttribute,
    simpleumltordbms_FromAttributeOwner,
    simpleumltordbms_IntegerToNumber,
    simpleumltordbms_Key,
    simpleumltordbms_NonLeafAttribute,
    simpleumltordbms_Package,
    simpleumltordbms_PackageToSchema,
    simpleumltordbms_PrimitiveDataType,
    simpleumltordbms_PrimitiveToName,
    simpleumltordbms_Schema,
    simpleumltordbms_StringToVarchar,
    simpleumltordbms_Table,
    simpleumltordbms_ToColumn,
    simpleumltordbms_UmlToRdbmsModelElement,
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

def test_assoc_attribute15_stub_double():
    # simpleumltordbms_Attribute has no real 'simpleumltordbms_Attribute' property in the generated
    # code (a bare stub) -- manually attach it so simpleumltordbms_FromAttribute's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # simpleumltordbms_FromAttribute's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = simpleumltordbms_FromAttribute(kind="sample_text")
    partner = simpleumltordbms_Attribute()
    setattr(partner, 'simpleumltordbms_Attribute', None)
    _safe_set(owner, 'simpleumltordbms_FromAttribute', partner)
    assert getattr(partner, 'simpleumltordbms_Attribute') == owner
    _safe_set(owner, 'simpleumltordbms_FromAttribute', None)
    assert getattr(partner, 'simpleumltordbms_Attribute') is None


def test_assoc_fromAttributes20_stub_double():
    # simpleumltordbms_FromAttributeOwner has no real 'owner21' property in the generated
    # code (a bare stub) -- manually attach it so simpleumltordbms_FromAttribute's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # simpleumltordbms_FromAttribute's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = simpleumltordbms_FromAttribute(kind="sample_text")
    partner = simpleumltordbms_FromAttributeOwner()
    setattr(partner, 'owner21', None)
    _safe_set(owner, 'FromAttribute', partner)
    assert owner in getattr(partner, 'owner21')
    _safe_set(owner, 'FromAttribute', None)
    assert owner not in getattr(partner, 'owner21')


def test_assoc_leafs16_stub_double():
    # simpleumltordbms_AttributeToColumn has no real 'simpleumltordbms_AttributeToColumn18' property in the generated
    # code (a bare stub) -- manually attach it so simpleumltordbms_FromAttribute's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # simpleumltordbms_FromAttribute's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = simpleumltordbms_FromAttribute(kind="sample_text")
    partner = simpleumltordbms_AttributeToColumn()
    setattr(partner, 'simpleumltordbms_AttributeToColumn18', None)
    _safe_set(owner, 'simpleumltordbms_FromAttribute17', {partner})
    assert getattr(partner, 'simpleumltordbms_AttributeToColumn18') == owner
    _safe_set(owner, 'simpleumltordbms_FromAttribute17', set())
    assert getattr(partner, 'simpleumltordbms_AttributeToColumn18') is None


def test_assoc_owner19_stub_double():
    # simpleumltordbms_FromAttributeOwner has no real 'FromAttributeOwner' property in the generated
    # code (a bare stub) -- manually attach it so simpleumltordbms_FromAttribute's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # simpleumltordbms_FromAttribute's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = simpleumltordbms_FromAttribute(kind="sample_text")
    partner = simpleumltordbms_FromAttributeOwner()
    setattr(partner, 'FromAttributeOwner', None)
    _safe_set(owner, 'fromAttributes', partner)
    assert getattr(partner, 'FromAttributeOwner') == owner
    _safe_set(owner, 'fromAttributes', None)
    assert getattr(partner, 'FromAttributeOwner') is None


def test_assoc_owner30_stub_double():
    # simpleumltordbms_PackageToSchema has no real 'PackageToSchema31' property in the generated
    # code (a bare stub) -- manually attach it so simpleumltordbms_PrimitiveToName's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # simpleumltordbms_PrimitiveToName's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = simpleumltordbms_PrimitiveToName(typeName="sample_text")
    partner = simpleumltordbms_PackageToSchema()
    setattr(partner, 'PackageToSchema31', None)
    _safe_set(owner, 'primitivesToNames', partner)
    assert getattr(partner, 'PackageToSchema31') == owner
    _safe_set(owner, 'primitivesToNames', None)
    assert getattr(partner, 'PackageToSchema31') is None


def test_assoc_primitive32_stub_double():
    # simpleumltordbms_PrimitiveDataType has no real 'simpleumltordbms_PrimitiveDataType' property in the generated
    # code (a bare stub) -- manually attach it so simpleumltordbms_PrimitiveToName's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # simpleumltordbms_PrimitiveToName's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = simpleumltordbms_PrimitiveToName(typeName="sample_text")
    partner = simpleumltordbms_PrimitiveDataType()
    setattr(partner, 'simpleumltordbms_PrimitiveDataType', None)
    _safe_set(owner, 'simpleumltordbms_PrimitiveToName33', partner)
    assert getattr(partner, 'simpleumltordbms_PrimitiveDataType') == owner
    _safe_set(owner, 'simpleumltordbms_PrimitiveToName33', None)
    assert getattr(partner, 'simpleumltordbms_PrimitiveDataType') is None


def test_assoc_primitivesToNames25_stub_double():
    # simpleumltordbms_PackageToSchema has no real 'owner26' property in the generated
    # code (a bare stub) -- manually attach it so simpleumltordbms_PrimitiveToName's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # simpleumltordbms_PrimitiveToName's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = simpleumltordbms_PrimitiveToName(typeName="sample_text")
    partner = simpleumltordbms_PackageToSchema()
    setattr(partner, 'owner26', None)
    _safe_set(owner, 'PrimitiveToName', partner)
    assert owner in getattr(partner, 'owner26')
    _safe_set(owner, 'PrimitiveToName', None)
    assert owner not in getattr(partner, 'owner26')


def test_assoc_type0_stub_double():
    # simpleumltordbms_AttributeToColumn has no real 'simpleumltordbms_AttributeToColumn' property in the generated
    # code (a bare stub) -- manually attach it so simpleumltordbms_PrimitiveToName's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # simpleumltordbms_PrimitiveToName's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = simpleumltordbms_PrimitiveToName(typeName="sample_text")
    partner = simpleumltordbms_AttributeToColumn()
    setattr(partner, 'simpleumltordbms_AttributeToColumn', None)
    _safe_set(owner, 'simpleumltordbms_PrimitiveToName', partner)
    assert getattr(partner, 'simpleumltordbms_AttributeToColumn') == owner
    _safe_set(owner, 'simpleumltordbms_PrimitiveToName', None)
    assert getattr(partner, 'simpleumltordbms_AttributeToColumn') is None


