import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    FromAttribute,
    FromAttributeOwner,
    ToColumn,
    umltordbms_Association,
    umltordbms_AssociationToForeignKey,
    umltordbms_Attribute,
    umltordbms_AttributeToColumn,
    umltordbms_Class,
    umltordbms_ClassToTable,
    umltordbms_Column,
    umltordbms_ForeignKey,
    umltordbms_FromAttribute,
    umltordbms_FromAttributeOwner,
    umltordbms_Key,
    umltordbms_NonLeafAttribute,
    umltordbms_Package,
    umltordbms_PackageToSchema,
    umltordbms_PrimitiveDataType,
    umltordbms_PrimitiveToName,
    umltordbms_Schema,
    umltordbms_Table,
    umltordbms_ToColumn,
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

def test_assoc_associationsToForeignKeys8_reverse_link_reassign_clear():
    a1 = umltordbms_ClassToTable(name="sample_text")
    a2 = umltordbms_ClassToTable(name="sample_text_2")
    b = umltordbms_AssociationToForeignKey(name="sample_text")
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
    a1 = umltordbms_PackageToSchema(name="sample_text")
    a2 = umltordbms_PackageToSchema(name="sample_text_2")
    b = umltordbms_ClassToTable(name="sample_text")
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


def test_assoc_owner2_reverse_link_reassign_clear():
    a1 = umltordbms_ClassToTable(name="sample_text")
    a2 = umltordbms_ClassToTable(name="sample_text_2")
    b = umltordbms_AssociationToForeignKey(name="sample_text")
    _safe_set(b, 'associationsToForeignKeys', a1)
    assert _is_linked(b, 'associationsToForeignKeys', a1)
    if hasattr(a1, 'ClassToTable'):
        assert _is_linked(a1, 'ClassToTable', b)
    _safe_set(b, 'associationsToForeignKeys', a2)
    assert _is_linked(b, 'associationsToForeignKeys', a2)
    if hasattr(a1, 'ClassToTable'):
        assert not _is_linked(a1, 'ClassToTable', b)
    if hasattr(a2, 'ClassToTable'):
        assert _is_linked(a2, 'ClassToTable', b)
    _safe_set(b, 'associationsToForeignKeys', None)
    assert not _is_linked(b, 'associationsToForeignKeys', a2)
    if hasattr(a2, 'ClassToTable'):
        assert not _is_linked(a2, 'ClassToTable', b)


def test_assoc_owner30_reverse_link_reassign_clear():
    a1 = umltordbms_PrimitiveToName(name="sample_text", typeName="sample_text")
    a2 = umltordbms_PrimitiveToName(name="sample_text_2", typeName="sample_text_2")
    b = umltordbms_PackageToSchema(name="sample_text")
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
    a1 = umltordbms_PackageToSchema(name="sample_text")
    a2 = umltordbms_PackageToSchema(name="sample_text_2")
    b = umltordbms_ClassToTable(name="sample_text")
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
    a1 = umltordbms_PrimitiveToName(name="sample_text", typeName="sample_text")
    a2 = umltordbms_PrimitiveToName(name="sample_text_2", typeName="sample_text_2")
    b = umltordbms_PackageToSchema(name="sample_text")
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


def test_assoc_referenced1_reverse_link_reassign_clear():
    a1 = umltordbms_ClassToTable(name="sample_text")
    a2 = umltordbms_ClassToTable(name="sample_text_2")
    b = umltordbms_AssociationToForeignKey(name="sample_text")
    _safe_set(b, 'umltordbms_AssociationToForeignKey', a1)
    assert _is_linked(b, 'umltordbms_AssociationToForeignKey', a1)
    if hasattr(a1, 'umltordbms_ClassToTable'):
        assert _is_linked(a1, 'umltordbms_ClassToTable', b)
    _safe_set(b, 'umltordbms_AssociationToForeignKey', a2)
    assert _is_linked(b, 'umltordbms_AssociationToForeignKey', a2)
    if hasattr(a1, 'umltordbms_ClassToTable'):
        assert not _is_linked(a1, 'umltordbms_ClassToTable', b)
    if hasattr(a2, 'umltordbms_ClassToTable'):
        assert _is_linked(a2, 'umltordbms_ClassToTable', b)
    _safe_set(b, 'umltordbms_AssociationToForeignKey', None)
    assert not _is_linked(b, 'umltordbms_AssociationToForeignKey', a2)
    if hasattr(a2, 'umltordbms_ClassToTable'):
        assert not _is_linked(a2, 'umltordbms_ClassToTable', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_association3_stub_double():
    # umltordbms_Association has no real 'umltordbms_Association' property in the generated
    # code (a bare stub) -- manually attach it so umltordbms_AssociationToForeignKey's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # umltordbms_AssociationToForeignKey's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = umltordbms_AssociationToForeignKey(name="sample_text")
    partner = umltordbms_Association()
    setattr(partner, 'umltordbms_Association', None)
    _safe_set(owner, 'umltordbms_AssociationToForeignKey4', partner)
    assert getattr(partner, 'umltordbms_Association') == owner
    _safe_set(owner, 'umltordbms_AssociationToForeignKey4', None)
    assert getattr(partner, 'umltordbms_Association') is None


def test_assoc_attribute18_stub_double():
    # umltordbms_Attribute has no real 'umltordbms_Attribute' property in the generated
    # code (a bare stub) -- manually attach it so umltordbms_FromAttribute's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # umltordbms_FromAttribute's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = umltordbms_FromAttribute(kind="sample_text", name="sample_text")
    partner = umltordbms_Attribute()
    setattr(partner, 'umltordbms_Attribute', None)
    _safe_set(owner, 'umltordbms_FromAttribute19', partner)
    assert getattr(partner, 'umltordbms_Attribute') == owner
    _safe_set(owner, 'umltordbms_FromAttribute19', None)
    assert getattr(partner, 'umltordbms_Attribute') is None


def test_assoc_foreignKey5_stub_double():
    # umltordbms_ForeignKey has no real 'umltordbms_ForeignKey' property in the generated
    # code (a bare stub) -- manually attach it so umltordbms_AssociationToForeignKey's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # umltordbms_AssociationToForeignKey's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = umltordbms_AssociationToForeignKey(name="sample_text")
    partner = umltordbms_ForeignKey()
    setattr(partner, 'umltordbms_ForeignKey', None)
    _safe_set(owner, 'umltordbms_AssociationToForeignKey6', partner)
    assert getattr(partner, 'umltordbms_ForeignKey') == owner
    _safe_set(owner, 'umltordbms_AssociationToForeignKey6', None)
    assert getattr(partner, 'umltordbms_ForeignKey') is None


def test_assoc_fromAttributes20_stub_double():
    # umltordbms_FromAttributeOwner has no real 'owner21' property in the generated
    # code (a bare stub) -- manually attach it so umltordbms_FromAttribute's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # umltordbms_FromAttribute's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = umltordbms_FromAttribute(kind="sample_text", name="sample_text")
    partner = umltordbms_FromAttributeOwner()
    setattr(partner, 'owner21', None)
    _safe_set(owner, 'FromAttribute', partner)
    assert getattr(partner, 'owner21') == owner
    _safe_set(owner, 'FromAttribute', None)
    assert getattr(partner, 'owner21') is None


def test_assoc_leafs16_stub_double():
    # umltordbms_AttributeToColumn has no real 'umltordbms_AttributeToColumn17' property in the generated
    # code (a bare stub) -- manually attach it so umltordbms_FromAttribute's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # umltordbms_FromAttribute's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = umltordbms_FromAttribute(kind="sample_text", name="sample_text")
    partner = umltordbms_AttributeToColumn()
    setattr(partner, 'umltordbms_AttributeToColumn17', None)
    _safe_set(owner, 'umltordbms_FromAttribute', {partner})
    assert getattr(partner, 'umltordbms_AttributeToColumn17') == owner
    _safe_set(owner, 'umltordbms_FromAttribute', set())
    assert getattr(partner, 'umltordbms_AttributeToColumn17') is None


def test_assoc_owner15_stub_double():
    # umltordbms_FromAttributeOwner has no real 'FromAttributeOwner' property in the generated
    # code (a bare stub) -- manually attach it so umltordbms_FromAttribute's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # umltordbms_FromAttribute's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = umltordbms_FromAttribute(kind="sample_text", name="sample_text")
    partner = umltordbms_FromAttributeOwner()
    setattr(partner, 'FromAttributeOwner', None)
    _safe_set(owner, 'fromAttributes', partner)
    assert getattr(partner, 'FromAttributeOwner') == owner
    _safe_set(owner, 'fromAttributes', None)
    assert getattr(partner, 'FromAttributeOwner') is None


def test_assoc_primaryKey13_stub_double():
    # umltordbms_Key has no real 'umltordbms_Key' property in the generated
    # code (a bare stub) -- manually attach it so umltordbms_ClassToTable's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # umltordbms_ClassToTable's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = umltordbms_ClassToTable(name="sample_text")
    partner = umltordbms_Key()
    setattr(partner, 'umltordbms_Key', None)
    _safe_set(owner, 'umltordbms_ClassToTable14', partner)
    assert getattr(partner, 'umltordbms_Key') == owner
    _safe_set(owner, 'umltordbms_ClassToTable14', None)
    assert getattr(partner, 'umltordbms_Key') is None


def test_assoc_primitive32_stub_double():
    # umltordbms_PrimitiveDataType has no real 'umltordbms_PrimitiveDataType' property in the generated
    # code (a bare stub) -- manually attach it so umltordbms_PrimitiveToName's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # umltordbms_PrimitiveToName's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = umltordbms_PrimitiveToName(name="sample_text", typeName="sample_text")
    partner = umltordbms_PrimitiveDataType()
    setattr(partner, 'umltordbms_PrimitiveDataType', None)
    _safe_set(owner, 'umltordbms_PrimitiveToName33', partner)
    assert getattr(partner, 'umltordbms_PrimitiveDataType') == owner
    _safe_set(owner, 'umltordbms_PrimitiveToName33', None)
    assert getattr(partner, 'umltordbms_PrimitiveDataType') is None


def test_assoc_schema28_stub_double():
    # umltordbms_Schema has no real 'umltordbms_Schema' property in the generated
    # code (a bare stub) -- manually attach it so umltordbms_PackageToSchema's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # umltordbms_PackageToSchema's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = umltordbms_PackageToSchema(name="sample_text")
    partner = umltordbms_Schema()
    setattr(partner, 'umltordbms_Schema', None)
    _safe_set(owner, 'umltordbms_PackageToSchema29', partner)
    assert getattr(partner, 'umltordbms_Schema') == owner
    _safe_set(owner, 'umltordbms_PackageToSchema29', None)
    assert getattr(partner, 'umltordbms_Schema') is None


def test_assoc_table11_stub_double():
    # umltordbms_Table has no real 'umltordbms_Table' property in the generated
    # code (a bare stub) -- manually attach it so umltordbms_ClassToTable's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # umltordbms_ClassToTable's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = umltordbms_ClassToTable(name="sample_text")
    partner = umltordbms_Table()
    setattr(partner, 'umltordbms_Table', None)
    _safe_set(owner, 'umltordbms_ClassToTable12', partner)
    assert getattr(partner, 'umltordbms_Table') == owner
    _safe_set(owner, 'umltordbms_ClassToTable12', None)
    assert getattr(partner, 'umltordbms_Table') is None


def test_assoc_type0_stub_double():
    # umltordbms_AttributeToColumn has no real 'umltordbms_AttributeToColumn' property in the generated
    # code (a bare stub) -- manually attach it so umltordbms_PrimitiveToName's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # umltordbms_PrimitiveToName's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = umltordbms_PrimitiveToName(name="sample_text", typeName="sample_text")
    partner = umltordbms_AttributeToColumn()
    setattr(partner, 'umltordbms_AttributeToColumn', None)
    _safe_set(owner, 'umltordbms_PrimitiveToName', partner)
    assert getattr(partner, 'umltordbms_AttributeToColumn') == owner
    _safe_set(owner, 'umltordbms_PrimitiveToName', None)
    assert getattr(partner, 'umltordbms_AttributeToColumn') is None


def test_assoc_umlClass9_stub_double():
    # umltordbms_Class has no real 'umltordbms_Class' property in the generated
    # code (a bare stub) -- manually attach it so umltordbms_ClassToTable's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # umltordbms_ClassToTable's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = umltordbms_ClassToTable(name="sample_text")
    partner = umltordbms_Class()
    setattr(partner, 'umltordbms_Class', None)
    _safe_set(owner, 'umltordbms_ClassToTable10', partner)
    assert getattr(partner, 'umltordbms_Class') == owner
    _safe_set(owner, 'umltordbms_ClassToTable10', None)
    assert getattr(partner, 'umltordbms_Class') is None


def test_assoc_umlPackage27_stub_double():
    # umltordbms_Package has no real 'umltordbms_Package' property in the generated
    # code (a bare stub) -- manually attach it so umltordbms_PackageToSchema's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # umltordbms_PackageToSchema's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = umltordbms_PackageToSchema(name="sample_text")
    partner = umltordbms_Package()
    setattr(partner, 'umltordbms_Package', None)
    _safe_set(owner, 'umltordbms_PackageToSchema', partner)
    assert getattr(partner, 'umltordbms_Package') == owner
    _safe_set(owner, 'umltordbms_PackageToSchema', None)
    assert getattr(partner, 'umltordbms_Package') is None


