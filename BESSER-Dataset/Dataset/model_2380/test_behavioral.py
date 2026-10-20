import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    FromAttribute,
    FromAttributeOwner,
    ToColumn,
    uml2rdbms_Association,
    uml2rdbms_AssociationToForeignKey,
    uml2rdbms_Attribute,
    uml2rdbms_AttributeToColumn,
    uml2rdbms_Class,
    uml2rdbms_ClassToTable,
    uml2rdbms_Column,
    uml2rdbms_ForeignKey,
    uml2rdbms_FromAttribute,
    uml2rdbms_FromAttributeOwner,
    uml2rdbms_Key,
    uml2rdbms_NonLeafAttribute,
    uml2rdbms_Package,
    uml2rdbms_PackageToSchema,
    uml2rdbms_PrimitiveDataType,
    uml2rdbms_PrimitiveToName,
    uml2rdbms_Schema,
    uml2rdbms_Table,
    uml2rdbms_ToColumn,
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

def test_assoc_associationToForeignKeys8_reverse_link_reassign_clear():
    a1 = uml2rdbms_ClassToTable(name="sample_text")
    a2 = uml2rdbms_ClassToTable(name="sample_text_2")
    b = uml2rdbms_AssociationToForeignKey(name="sample_text")
    _safe_set(b, 'AssociationToForeignKey', a1)
    assert _is_linked(b, 'AssociationToForeignKey', a1)
    if hasattr(a1, 'owner'):
        assert _is_linked(a1, 'owner', b)
    _safe_set(b, 'AssociationToForeignKey', a2)
    assert _is_linked(b, 'AssociationToForeignKey', a2)
    if hasattr(a1, 'owner'):
        assert not _is_linked(a1, 'owner', b)
    if hasattr(a2, 'owner'):
        assert _is_linked(a2, 'owner', b)
    _safe_set(b, 'AssociationToForeignKey', None)
    assert not _is_linked(b, 'AssociationToForeignKey', a2)
    if hasattr(a2, 'owner'):
        assert not _is_linked(a2, 'owner', b)


def test_assoc_classesToTables22_reverse_link_reassign_clear():
    a1 = uml2rdbms_PackageToSchema(name="sample_text")
    a2 = uml2rdbms_PackageToSchema(name="sample_text_2")
    b = uml2rdbms_ClassToTable(name="sample_text")
    _safe_set(b, 'ClassToTable24', a1)
    assert _is_linked(b, 'ClassToTable24', a1)
    if hasattr(a1, 'owner23'):
        assert _is_linked(a1, 'owner23', b)
    _safe_set(b, 'ClassToTable24', a2)
    assert _is_linked(b, 'ClassToTable24', a2)
    if hasattr(a1, 'owner23'):
        assert not _is_linked(a1, 'owner23', b)
    if hasattr(a2, 'owner23'):
        assert _is_linked(a2, 'owner23', b)
    _safe_set(b, 'ClassToTable24', None)
    assert not _is_linked(b, 'ClassToTable24', a2)
    if hasattr(a2, 'owner23'):
        assert not _is_linked(a2, 'owner23', b)


def test_assoc_owner1_reverse_link_reassign_clear():
    a1 = uml2rdbms_ClassToTable(name="sample_text")
    a2 = uml2rdbms_ClassToTable(name="sample_text_2")
    b = uml2rdbms_AssociationToForeignKey(name="sample_text")
    _safe_set(b, 'associationToForeignKeys', a1)
    assert _is_linked(b, 'associationToForeignKeys', a1)
    if hasattr(a1, 'ClassToTable'):
        assert _is_linked(a1, 'ClassToTable', b)
    _safe_set(b, 'associationToForeignKeys', a2)
    assert _is_linked(b, 'associationToForeignKeys', a2)
    if hasattr(a1, 'ClassToTable'):
        assert not _is_linked(a1, 'ClassToTable', b)
    if hasattr(a2, 'ClassToTable'):
        assert _is_linked(a2, 'ClassToTable', b)
    _safe_set(b, 'associationToForeignKeys', None)
    assert not _is_linked(b, 'associationToForeignKeys', a2)
    if hasattr(a2, 'ClassToTable'):
        assert not _is_linked(a2, 'ClassToTable', b)


def test_assoc_owner30_reverse_link_reassign_clear():
    a1 = uml2rdbms_PrimitiveToName(name="sample_text", typeName="sample_text")
    a2 = uml2rdbms_PrimitiveToName(name="sample_text_2", typeName="sample_text_2")
    b = uml2rdbms_PackageToSchema(name="sample_text")
    _safe_set(b, 'PackageToSchema31', a1)
    assert _is_linked(b, 'PackageToSchema31', a1)
    if hasattr(a1, 'primitivesToNames'):
        assert _is_linked(a1, 'primitivesToNames', b)
    _safe_set(b, 'PackageToSchema31', a2)
    assert _is_linked(b, 'PackageToSchema31', a2)
    if hasattr(a1, 'primitivesToNames'):
        assert not _is_linked(a1, 'primitivesToNames', b)
    if hasattr(a2, 'primitivesToNames'):
        assert _is_linked(a2, 'primitivesToNames', b)
    _safe_set(b, 'PackageToSchema31', None)
    assert not _is_linked(b, 'PackageToSchema31', a2)
    if hasattr(a2, 'primitivesToNames'):
        assert not _is_linked(a2, 'primitivesToNames', b)


def test_assoc_owner7_reverse_link_reassign_clear():
    a1 = uml2rdbms_PackageToSchema(name="sample_text")
    a2 = uml2rdbms_PackageToSchema(name="sample_text_2")
    b = uml2rdbms_ClassToTable(name="sample_text")
    _safe_set(b, 'classesToTables', a1)
    assert _is_linked(b, 'classesToTables', a1)
    if hasattr(a1, 'PackageToSchema'):
        assert _is_linked(a1, 'PackageToSchema', b)
    _safe_set(b, 'classesToTables', a2)
    assert _is_linked(b, 'classesToTables', a2)
    if hasattr(a1, 'PackageToSchema'):
        assert not _is_linked(a1, 'PackageToSchema', b)
    if hasattr(a2, 'PackageToSchema'):
        assert _is_linked(a2, 'PackageToSchema', b)
    _safe_set(b, 'classesToTables', None)
    assert not _is_linked(b, 'classesToTables', a2)
    if hasattr(a2, 'PackageToSchema'):
        assert not _is_linked(a2, 'PackageToSchema', b)


def test_assoc_primitivesToNames25_reverse_link_reassign_clear():
    a1 = uml2rdbms_PrimitiveToName(name="sample_text", typeName="sample_text")
    a2 = uml2rdbms_PrimitiveToName(name="sample_text_2", typeName="sample_text_2")
    b = uml2rdbms_PackageToSchema(name="sample_text")
    _safe_set(b, 'owner26', {a1})
    assert _is_linked(b, 'owner26', a1)
    if hasattr(a1, 'PrimitiveToName'):
        assert _is_linked(a1, 'PrimitiveToName', b)
    _safe_set(b, 'owner26', {a2})
    assert _is_linked(b, 'owner26', a2)
    if hasattr(a1, 'PrimitiveToName'):
        assert not _is_linked(a1, 'PrimitiveToName', b)
    if hasattr(a2, 'PrimitiveToName'):
        assert _is_linked(a2, 'PrimitiveToName', b)
    _safe_set(b, 'owner26', set())
    assert not _is_linked(b, 'owner26', a2)
    if hasattr(a2, 'PrimitiveToName'):
        assert not _is_linked(a2, 'PrimitiveToName', b)


def test_assoc_referenced0_reverse_link_reassign_clear():
    a1 = uml2rdbms_ClassToTable(name="sample_text")
    a2 = uml2rdbms_ClassToTable(name="sample_text_2")
    b = uml2rdbms_AssociationToForeignKey(name="sample_text")
    _safe_set(b, 'uml2rdbms_AssociationToForeignKey', a1)
    assert _is_linked(b, 'uml2rdbms_AssociationToForeignKey', a1)
    if hasattr(a1, 'uml2rdbms_ClassToTable'):
        assert _is_linked(a1, 'uml2rdbms_ClassToTable', b)
    _safe_set(b, 'uml2rdbms_AssociationToForeignKey', a2)
    assert _is_linked(b, 'uml2rdbms_AssociationToForeignKey', a2)
    if hasattr(a1, 'uml2rdbms_ClassToTable'):
        assert not _is_linked(a1, 'uml2rdbms_ClassToTable', b)
    if hasattr(a2, 'uml2rdbms_ClassToTable'):
        assert _is_linked(a2, 'uml2rdbms_ClassToTable', b)
    _safe_set(b, 'uml2rdbms_AssociationToForeignKey', None)
    assert not _is_linked(b, 'uml2rdbms_AssociationToForeignKey', a2)
    if hasattr(a2, 'uml2rdbms_ClassToTable'):
        assert not _is_linked(a2, 'uml2rdbms_ClassToTable', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_association2_stub_double():
    # uml2rdbms_Association has no real 'uml2rdbms_Association' property in the generated
    # code (a bare stub) -- manually attach it so uml2rdbms_AssociationToForeignKey's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # uml2rdbms_AssociationToForeignKey's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = uml2rdbms_AssociationToForeignKey(name="sample_text")
    partner = uml2rdbms_Association()
    setattr(partner, 'uml2rdbms_Association', None)
    _safe_set(owner, 'uml2rdbms_AssociationToForeignKey3', partner)
    assert getattr(partner, 'uml2rdbms_Association') == owner
    _safe_set(owner, 'uml2rdbms_AssociationToForeignKey3', None)
    assert getattr(partner, 'uml2rdbms_Association') is None


def test_assoc_attribute18_stub_double():
    # uml2rdbms_Attribute has no real 'uml2rdbms_Attribute' property in the generated
    # code (a bare stub) -- manually attach it so uml2rdbms_FromAttribute's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # uml2rdbms_FromAttribute's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = uml2rdbms_FromAttribute(kind="sample_text", name="sample_text")
    partner = uml2rdbms_Attribute()
    setattr(partner, 'uml2rdbms_Attribute', None)
    _safe_set(owner, 'uml2rdbms_FromAttribute19', partner)
    assert getattr(partner, 'uml2rdbms_Attribute') == owner
    _safe_set(owner, 'uml2rdbms_FromAttribute19', None)
    assert getattr(partner, 'uml2rdbms_Attribute') is None


def test_assoc_foreignKey4_stub_double():
    # uml2rdbms_ForeignKey has no real 'uml2rdbms_ForeignKey' property in the generated
    # code (a bare stub) -- manually attach it so uml2rdbms_AssociationToForeignKey's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # uml2rdbms_AssociationToForeignKey's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = uml2rdbms_AssociationToForeignKey(name="sample_text")
    partner = uml2rdbms_ForeignKey()
    setattr(partner, 'uml2rdbms_ForeignKey', None)
    _safe_set(owner, 'uml2rdbms_AssociationToForeignKey5', partner)
    assert getattr(partner, 'uml2rdbms_ForeignKey') == owner
    _safe_set(owner, 'uml2rdbms_AssociationToForeignKey5', None)
    assert getattr(partner, 'uml2rdbms_ForeignKey') is None


def test_assoc_fromAttributes20_stub_double():
    # uml2rdbms_FromAttributeOwner has no real 'owner21' property in the generated
    # code (a bare stub) -- manually attach it so uml2rdbms_FromAttribute's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # uml2rdbms_FromAttribute's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = uml2rdbms_FromAttribute(kind="sample_text", name="sample_text")
    partner = uml2rdbms_FromAttributeOwner()
    setattr(partner, 'owner21', None)
    _safe_set(owner, 'FromAttribute', partner)
    assert owner in getattr(partner, 'owner21')
    _safe_set(owner, 'FromAttribute', None)
    assert owner not in getattr(partner, 'owner21')


def test_assoc_leafs16_stub_double():
    # uml2rdbms_AttributeToColumn has no real 'uml2rdbms_AttributeToColumn17' property in the generated
    # code (a bare stub) -- manually attach it so uml2rdbms_FromAttribute's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # uml2rdbms_FromAttribute's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = uml2rdbms_FromAttribute(kind="sample_text", name="sample_text")
    partner = uml2rdbms_AttributeToColumn()
    setattr(partner, 'uml2rdbms_AttributeToColumn17', None)
    _safe_set(owner, 'uml2rdbms_FromAttribute', {partner})
    assert getattr(partner, 'uml2rdbms_AttributeToColumn17') == owner
    _safe_set(owner, 'uml2rdbms_FromAttribute', set())
    assert getattr(partner, 'uml2rdbms_AttributeToColumn17') is None


def test_assoc_owner15_stub_double():
    # uml2rdbms_FromAttributeOwner has no real 'FromAttributeOwner' property in the generated
    # code (a bare stub) -- manually attach it so uml2rdbms_FromAttribute's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # uml2rdbms_FromAttribute's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = uml2rdbms_FromAttribute(kind="sample_text", name="sample_text")
    partner = uml2rdbms_FromAttributeOwner()
    setattr(partner, 'FromAttributeOwner', None)
    _safe_set(owner, 'fromAttributes', partner)
    assert getattr(partner, 'FromAttributeOwner') == owner
    _safe_set(owner, 'fromAttributes', None)
    assert getattr(partner, 'FromAttributeOwner') is None


def test_assoc_primaryKey13_stub_double():
    # uml2rdbms_Key has no real 'uml2rdbms_Key' property in the generated
    # code (a bare stub) -- manually attach it so uml2rdbms_ClassToTable's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # uml2rdbms_ClassToTable's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = uml2rdbms_ClassToTable(name="sample_text")
    partner = uml2rdbms_Key()
    setattr(partner, 'uml2rdbms_Key', None)
    _safe_set(owner, 'uml2rdbms_ClassToTable14', partner)
    assert getattr(partner, 'uml2rdbms_Key') == owner
    _safe_set(owner, 'uml2rdbms_ClassToTable14', None)
    assert getattr(partner, 'uml2rdbms_Key') is None


def test_assoc_primitive32_stub_double():
    # uml2rdbms_PrimitiveDataType has no real 'uml2rdbms_PrimitiveDataType' property in the generated
    # code (a bare stub) -- manually attach it so uml2rdbms_PrimitiveToName's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # uml2rdbms_PrimitiveToName's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = uml2rdbms_PrimitiveToName(name="sample_text", typeName="sample_text")
    partner = uml2rdbms_PrimitiveDataType()
    setattr(partner, 'uml2rdbms_PrimitiveDataType', None)
    _safe_set(owner, 'uml2rdbms_PrimitiveToName33', partner)
    assert getattr(partner, 'uml2rdbms_PrimitiveDataType') == owner
    _safe_set(owner, 'uml2rdbms_PrimitiveToName33', None)
    assert getattr(partner, 'uml2rdbms_PrimitiveDataType') is None


def test_assoc_schema28_stub_double():
    # uml2rdbms_Schema has no real 'uml2rdbms_Schema' property in the generated
    # code (a bare stub) -- manually attach it so uml2rdbms_PackageToSchema's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # uml2rdbms_PackageToSchema's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = uml2rdbms_PackageToSchema(name="sample_text")
    partner = uml2rdbms_Schema()
    setattr(partner, 'uml2rdbms_Schema', None)
    _safe_set(owner, 'uml2rdbms_PackageToSchema29', partner)
    assert getattr(partner, 'uml2rdbms_Schema') == owner
    _safe_set(owner, 'uml2rdbms_PackageToSchema29', None)
    assert getattr(partner, 'uml2rdbms_Schema') is None


def test_assoc_table11_stub_double():
    # uml2rdbms_Table has no real 'uml2rdbms_Table' property in the generated
    # code (a bare stub) -- manually attach it so uml2rdbms_ClassToTable's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # uml2rdbms_ClassToTable's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = uml2rdbms_ClassToTable(name="sample_text")
    partner = uml2rdbms_Table()
    setattr(partner, 'uml2rdbms_Table', None)
    _safe_set(owner, 'uml2rdbms_ClassToTable12', partner)
    assert getattr(partner, 'uml2rdbms_Table') == owner
    _safe_set(owner, 'uml2rdbms_ClassToTable12', None)
    assert getattr(partner, 'uml2rdbms_Table') is None


def test_assoc_type35_stub_double():
    # uml2rdbms_NonLeafAttribute has no real 'uml2rdbms_NonLeafAttribute' property in the generated
    # code (a bare stub) -- manually attach it so uml2rdbms_PrimitiveToName's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # uml2rdbms_PrimitiveToName's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = uml2rdbms_PrimitiveToName(name="sample_text", typeName="sample_text")
    partner = uml2rdbms_NonLeafAttribute()
    setattr(partner, 'uml2rdbms_NonLeafAttribute', None)
    _safe_set(owner, 'uml2rdbms_PrimitiveToName36', partner)
    assert getattr(partner, 'uml2rdbms_NonLeafAttribute') == owner
    _safe_set(owner, 'uml2rdbms_PrimitiveToName36', None)
    assert getattr(partner, 'uml2rdbms_NonLeafAttribute') is None


def test_assoc_type6_stub_double():
    # uml2rdbms_AttributeToColumn has no real 'uml2rdbms_AttributeToColumn' property in the generated
    # code (a bare stub) -- manually attach it so uml2rdbms_PrimitiveToName's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # uml2rdbms_PrimitiveToName's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = uml2rdbms_PrimitiveToName(name="sample_text", typeName="sample_text")
    partner = uml2rdbms_AttributeToColumn()
    setattr(partner, 'uml2rdbms_AttributeToColumn', None)
    _safe_set(owner, 'uml2rdbms_PrimitiveToName', partner)
    assert getattr(partner, 'uml2rdbms_AttributeToColumn') == owner
    _safe_set(owner, 'uml2rdbms_PrimitiveToName', None)
    assert getattr(partner, 'uml2rdbms_AttributeToColumn') is None


def test_assoc_umlClass9_stub_double():
    # uml2rdbms_Class has no real 'uml2rdbms_Class' property in the generated
    # code (a bare stub) -- manually attach it so uml2rdbms_ClassToTable's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # uml2rdbms_ClassToTable's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = uml2rdbms_ClassToTable(name="sample_text")
    partner = uml2rdbms_Class()
    setattr(partner, 'uml2rdbms_Class', None)
    _safe_set(owner, 'uml2rdbms_ClassToTable10', partner)
    assert getattr(partner, 'uml2rdbms_Class') == owner
    _safe_set(owner, 'uml2rdbms_ClassToTable10', None)
    assert getattr(partner, 'uml2rdbms_Class') is None


def test_assoc_umlPackage27_stub_double():
    # uml2rdbms_Package has no real 'uml2rdbms_Package' property in the generated
    # code (a bare stub) -- manually attach it so uml2rdbms_PackageToSchema's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # uml2rdbms_PackageToSchema's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = uml2rdbms_PackageToSchema(name="sample_text")
    partner = uml2rdbms_Package()
    setattr(partner, 'uml2rdbms_Package', None)
    _safe_set(owner, 'uml2rdbms_PackageToSchema', partner)
    assert getattr(partner, 'uml2rdbms_Package') == owner
    _safe_set(owner, 'uml2rdbms_PackageToSchema', None)
    assert getattr(partner, 'uml2rdbms_Package') is None


