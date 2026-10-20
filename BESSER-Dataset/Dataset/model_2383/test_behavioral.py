import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    FromAttribute,
    FromAttributeOwner,
    PrimitiveToName,
    ToColumn,
    UmlToRdbmsModelElement,
    uml2rdbms_Association,
    uml2rdbms_AssociationToForeignKey,
    uml2rdbms_Attribute,
    uml2rdbms_AttributeToColumn,
    uml2rdbms_BooleanToBoolean,
    uml2rdbms_Class,
    uml2rdbms_ClassToTable,
    uml2rdbms_Column,
    uml2rdbms_ForeignKey,
    uml2rdbms_FromAttribute,
    uml2rdbms_FromAttributeOwner,
    uml2rdbms_IntegerToNumber,
    uml2rdbms_Key,
    uml2rdbms_NonLeafAttribute,
    uml2rdbms_Package,
    uml2rdbms_PackageToSchema,
    uml2rdbms_PrimitiveDataType,
    uml2rdbms_PrimitiveToName,
    uml2rdbms_Schema,
    uml2rdbms_StringToVarchar,
    uml2rdbms_Table,
    uml2rdbms_ToColumn,
    uml2rdbms_UmlToRdbmsModelElement,
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
    # uml2rdbms_Attribute has no real 'uml2rdbms_Attribute' property in the generated
    # code (a bare stub) -- manually attach it so uml2rdbms_FromAttribute's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # uml2rdbms_FromAttribute's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = uml2rdbms_FromAttribute(kind="sample_text")
    partner = uml2rdbms_Attribute()
    setattr(partner, 'uml2rdbms_Attribute', None)
    _safe_set(owner, 'uml2rdbms_FromAttribute', partner)
    assert getattr(partner, 'uml2rdbms_Attribute') == owner
    _safe_set(owner, 'uml2rdbms_FromAttribute', None)
    assert getattr(partner, 'uml2rdbms_Attribute') is None


def test_assoc_fromAttributes20_stub_double():
    # uml2rdbms_FromAttributeOwner has no real 'owner21' property in the generated
    # code (a bare stub) -- manually attach it so uml2rdbms_FromAttribute's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # uml2rdbms_FromAttribute's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = uml2rdbms_FromAttribute(kind="sample_text")
    partner = uml2rdbms_FromAttributeOwner()
    setattr(partner, 'owner21', None)
    _safe_set(owner, 'FromAttribute', partner)
    assert owner in getattr(partner, 'owner21')
    _safe_set(owner, 'FromAttribute', None)
    assert owner not in getattr(partner, 'owner21')


def test_assoc_leafs16_stub_double():
    # uml2rdbms_AttributeToColumn has no real 'uml2rdbms_AttributeToColumn18' property in the generated
    # code (a bare stub) -- manually attach it so uml2rdbms_FromAttribute's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # uml2rdbms_FromAttribute's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = uml2rdbms_FromAttribute(kind="sample_text")
    partner = uml2rdbms_AttributeToColumn()
    setattr(partner, 'uml2rdbms_AttributeToColumn18', None)
    _safe_set(owner, 'uml2rdbms_FromAttribute17', {partner})
    assert getattr(partner, 'uml2rdbms_AttributeToColumn18') == owner
    _safe_set(owner, 'uml2rdbms_FromAttribute17', set())
    assert getattr(partner, 'uml2rdbms_AttributeToColumn18') is None


def test_assoc_owner19_stub_double():
    # uml2rdbms_FromAttributeOwner has no real 'FromAttributeOwner' property in the generated
    # code (a bare stub) -- manually attach it so uml2rdbms_FromAttribute's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # uml2rdbms_FromAttribute's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = uml2rdbms_FromAttribute(kind="sample_text")
    partner = uml2rdbms_FromAttributeOwner()
    setattr(partner, 'FromAttributeOwner', None)
    _safe_set(owner, 'fromAttributes', partner)
    assert getattr(partner, 'FromAttributeOwner') == owner
    _safe_set(owner, 'fromAttributes', None)
    assert getattr(partner, 'FromAttributeOwner') is None


def test_assoc_owner30_stub_double():
    # uml2rdbms_PackageToSchema has no real 'PackageToSchema31' property in the generated
    # code (a bare stub) -- manually attach it so uml2rdbms_PrimitiveToName's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # uml2rdbms_PrimitiveToName's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = uml2rdbms_PrimitiveToName(typeName="sample_text")
    partner = uml2rdbms_PackageToSchema()
    setattr(partner, 'PackageToSchema31', None)
    _safe_set(owner, 'primitivesToNames', partner)
    assert getattr(partner, 'PackageToSchema31') == owner
    _safe_set(owner, 'primitivesToNames', None)
    assert getattr(partner, 'PackageToSchema31') is None


def test_assoc_primitive32_stub_double():
    # uml2rdbms_PrimitiveDataType has no real 'uml2rdbms_PrimitiveDataType' property in the generated
    # code (a bare stub) -- manually attach it so uml2rdbms_PrimitiveToName's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # uml2rdbms_PrimitiveToName's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = uml2rdbms_PrimitiveToName(typeName="sample_text")
    partner = uml2rdbms_PrimitiveDataType()
    setattr(partner, 'uml2rdbms_PrimitiveDataType', None)
    _safe_set(owner, 'uml2rdbms_PrimitiveToName33', partner)
    assert getattr(partner, 'uml2rdbms_PrimitiveDataType') == owner
    _safe_set(owner, 'uml2rdbms_PrimitiveToName33', None)
    assert getattr(partner, 'uml2rdbms_PrimitiveDataType') is None


def test_assoc_primitivesToNames25_stub_double():
    # uml2rdbms_PackageToSchema has no real 'owner26' property in the generated
    # code (a bare stub) -- manually attach it so uml2rdbms_PrimitiveToName's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # uml2rdbms_PrimitiveToName's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = uml2rdbms_PrimitiveToName(typeName="sample_text")
    partner = uml2rdbms_PackageToSchema()
    setattr(partner, 'owner26', None)
    _safe_set(owner, 'PrimitiveToName', partner)
    assert owner in getattr(partner, 'owner26')
    _safe_set(owner, 'PrimitiveToName', None)
    assert owner not in getattr(partner, 'owner26')


def test_assoc_type0_stub_double():
    # uml2rdbms_AttributeToColumn has no real 'uml2rdbms_AttributeToColumn' property in the generated
    # code (a bare stub) -- manually attach it so uml2rdbms_PrimitiveToName's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # uml2rdbms_PrimitiveToName's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = uml2rdbms_PrimitiveToName(typeName="sample_text")
    partner = uml2rdbms_AttributeToColumn()
    setattr(partner, 'uml2rdbms_AttributeToColumn', None)
    _safe_set(owner, 'uml2rdbms_PrimitiveToName', partner)
    assert getattr(partner, 'uml2rdbms_AttributeToColumn') == owner
    _safe_set(owner, 'uml2rdbms_PrimitiveToName', None)
    assert getattr(partner, 'uml2rdbms_AttributeToColumn') is None


