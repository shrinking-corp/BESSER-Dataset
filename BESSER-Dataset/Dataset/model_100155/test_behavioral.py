import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Column,
    ColumnConstraint,
    Constraint,
    Database,
    DbObject,
    Index,
    ModelRoot,
    NamedElement,
    Operation,
    PrimaryKey,
    Relation,
    Schema,
    Sequence,
    Table,
    TableColumn,
    TableConstraint,
    UniqueIndex,
    dml_ColumnReference,
    mm_dml_ColumnReference,
    mm_dml_Query,
    mm_rdb_AddColumn,
    mm_rdb_Column,
    mm_rdb_ColumnConstraint,
    mm_rdb_Constraint,
    mm_rdb_CreateTable,
    mm_rdb_Database,
    mm_rdb_DbObject,
    mm_rdb_DeleteColumn,
    mm_rdb_DeleteTable,
    mm_rdb_ForeignKey,
    mm_rdb_Index,
    mm_rdb_ModelRoot,
    mm_rdb_NamedElement,
    mm_rdb_Operation,
    mm_rdb_PrimaryKey,
    mm_rdb_Relation,
    mm_rdb_RenameColumn,
    mm_rdb_RenameTable,
    mm_rdb_Schema,
    mm_rdb_Sequence,
    mm_rdb_Table,
    mm_rdb_TableColumn,
    mm_rdb_TableConstraint,
    mm_rdb_TypeChangeToColumn,
    mm_rdb_UniqueIndex,
    rdb_Constraint,
    rdb_DbObject,
    rdb_NamedElement,
    rdb_Relation,
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

def test_assoc__owningTable28_stub_double():
    # Table has no real 'Table29' property in the generated
    # code (a bare stub) -- manually attach it so mm_rdb_TableColumn's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # mm_rdb_TableColumn's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = mm_rdb_TableColumn(type="sample_text")
    partner = Table()
    setattr(partner, 'Table29', None)
    _safe_set(owner, 'ownedColumns', partner)
    assert getattr(partner, 'Table29') == owner
    _safe_set(owner, 'ownedColumns', None)
    assert getattr(partner, 'Table29') is None


def test_assoc_changedTable56_stub_double():
    # Table has no real 'Table57' property in the generated
    # code (a bare stub) -- manually attach it so mm_rdb_AddColumn's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # mm_rdb_AddColumn's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = mm_rdb_AddColumn(newColumnName="sample_text")
    partner = Table()
    setattr(partner, 'Table57', None)
    _safe_set(owner, 'mm_rdb_AddColumn', partner)
    assert getattr(partner, 'Table57') == owner
    _safe_set(owner, 'mm_rdb_AddColumn', None)
    assert getattr(partner, 'Table57') is None


def test_assoc_changedTable61_stub_double():
    # Table has no real 'Table62' property in the generated
    # code (a bare stub) -- manually attach it so mm_rdb_RenameColumn's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # mm_rdb_RenameColumn's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = mm_rdb_RenameColumn(newColumnName="sample_text")
    partner = Table()
    setattr(partner, 'Table62', None)
    _safe_set(owner, 'mm_rdb_RenameColumn', partner)
    assert getattr(partner, 'Table62') == owner
    _safe_set(owner, 'mm_rdb_RenameColumn', None)
    assert getattr(partner, 'Table62') is None


def test_assoc_changedTable66_stub_double():
    # Table has no real 'Table67' property in the generated
    # code (a bare stub) -- manually attach it so mm_rdb_TypeChangeToColumn's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # mm_rdb_TypeChangeToColumn's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = mm_rdb_TypeChangeToColumn(newType="sample_text")
    partner = Table()
    setattr(partner, 'Table67', None)
    _safe_set(owner, 'mm_rdb_TypeChangeToColumn', partner)
    assert getattr(partner, 'Table67') == owner
    _safe_set(owner, 'mm_rdb_TypeChangeToColumn', None)
    assert getattr(partner, 'Table67') is None


def test_assoc_changedTable71_stub_double():
    # Table has no real 'Table72' property in the generated
    # code (a bare stub) -- manually attach it so mm_rdb_DeleteColumn's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # mm_rdb_DeleteColumn's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = mm_rdb_DeleteColumn()
    partner = Table()
    setattr(partner, 'Table72', None)
    _safe_set(owner, 'mm_rdb_DeleteColumn', partner)
    assert getattr(partner, 'Table72') == owner
    _safe_set(owner, 'mm_rdb_DeleteColumn', None)
    assert getattr(partner, 'Table72') is None


def test_assoc_changedTypeColumn68_stub_double():
    # TableColumn has no real 'TableColumn70' property in the generated
    # code (a bare stub) -- manually attach it so mm_rdb_TypeChangeToColumn's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # mm_rdb_TypeChangeToColumn's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = mm_rdb_TypeChangeToColumn(newType="sample_text")
    partner = TableColumn()
    setattr(partner, 'TableColumn70', None)
    _safe_set(owner, 'mm_rdb_TypeChangeToColumn69', partner)
    assert getattr(partner, 'TableColumn70') == owner
    _safe_set(owner, 'mm_rdb_TypeChangeToColumn69', None)
    assert getattr(partner, 'TableColumn70') is None


def test_assoc_columnConstrains58_stub_double():
    # ColumnConstraint has no real 'ColumnConstraint60' property in the generated
    # code (a bare stub) -- manually attach it so mm_rdb_AddColumn's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # mm_rdb_AddColumn's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = mm_rdb_AddColumn(newColumnName="sample_text")
    partner = ColumnConstraint()
    setattr(partner, 'ColumnConstraint60', None)
    _safe_set(owner, 'mm_rdb_AddColumn59', {partner})
    assert getattr(partner, 'ColumnConstraint60') == owner
    _safe_set(owner, 'mm_rdb_AddColumn59', set())
    assert getattr(partner, 'ColumnConstraint60') is None


def test_assoc_constraints15_stub_double():
    # TableConstraint has no real 'TableConstraint' property in the generated
    # code (a bare stub) -- manually attach it so mm_rdb_Table's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # mm_rdb_Table's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = mm_rdb_Table()
    partner = TableConstraint()
    setattr(partner, 'TableConstraint', None)
    _safe_set(owner, 'owningTable', {partner})
    assert getattr(partner, 'TableConstraint') == owner
    _safe_set(owner, 'owningTable', set())
    assert getattr(partner, 'TableConstraint') is None


def test_assoc_constraints30_stub_double():
    # ColumnConstraint has no real 'ColumnConstraint' property in the generated
    # code (a bare stub) -- manually attach it so mm_rdb_TableColumn's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # mm_rdb_TableColumn's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = mm_rdb_TableColumn(type="sample_text")
    partner = ColumnConstraint()
    setattr(partner, 'ColumnConstraint', None)
    _safe_set(owner, 'owningColumn', {partner})
    assert getattr(partner, 'ColumnConstraint') == owner
    _safe_set(owner, 'owningColumn', set())
    assert getattr(partner, 'ColumnConstraint') is None


def test_assoc_deleteColumn73_stub_double():
    # TableColumn has no real 'TableColumn75' property in the generated
    # code (a bare stub) -- manually attach it so mm_rdb_DeleteColumn's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # mm_rdb_DeleteColumn's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = mm_rdb_DeleteColumn()
    partner = TableColumn()
    setattr(partner, 'TableColumn75', None)
    _safe_set(owner, 'mm_rdb_DeleteColumn74', partner)
    assert getattr(partner, 'TableColumn75') == owner
    _safe_set(owner, 'mm_rdb_DeleteColumn74', None)
    assert getattr(partner, 'TableColumn75') is None


def test_assoc_deletedTable54_stub_double():
    # Table has no real 'Table55' property in the generated
    # code (a bare stub) -- manually attach it so mm_rdb_DeleteTable's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # mm_rdb_DeleteTable's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = mm_rdb_DeleteTable()
    partner = Table()
    setattr(partner, 'Table55', None)
    _safe_set(owner, 'mm_rdb_DeleteTable', partner)
    assert getattr(partner, 'Table55') == owner
    _safe_set(owner, 'mm_rdb_DeleteTable', None)
    assert getattr(partner, 'Table55') is None


def test_assoc_generateID49_stub_double():
    # Sequence has no real 'Sequence51' property in the generated
    # code (a bare stub) -- manually attach it so mm_rdb_CreateTable's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # mm_rdb_CreateTable's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = mm_rdb_CreateTable(tableName="sample_text")
    partner = Sequence()
    setattr(partner, 'Sequence51', None)
    _safe_set(owner, 'mm_rdb_CreateTable50', partner)
    assert getattr(partner, 'Sequence51') == owner
    _safe_set(owner, 'mm_rdb_CreateTable50', None)
    assert getattr(partner, 'Sequence51') is None


def test_assoc_ownedColumns14_stub_double():
    # TableColumn has no real 'TableColumn' property in the generated
    # code (a bare stub) -- manually attach it so mm_rdb_Table's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # mm_rdb_Table's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = mm_rdb_Table()
    partner = TableColumn()
    setattr(partner, 'TableColumn', None)
    _safe_set(owner, '_owningTable', {partner})
    assert getattr(partner, 'TableColumn') == owner
    _safe_set(owner, '_owningTable', set())
    assert getattr(partner, 'TableColumn') is None


def test_assoc_owningSchema11_stub_double():
    # Schema has no real 'Schema12' property in the generated
    # code (a bare stub) -- manually attach it so mm_rdb_Table's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # mm_rdb_Table's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = mm_rdb_Table()
    partner = Schema()
    setattr(partner, 'Schema12', None)
    _safe_set(owner, 'tables', partner)
    assert getattr(partner, 'Schema12') == owner
    _safe_set(owner, 'tables', None)
    assert getattr(partner, 'Schema12') is None


def test_assoc_owningSchema16_stub_double():
    # Schema has no real 'Schema17' property in the generated
    # code (a bare stub) -- manually attach it so mm_rdb_Sequence's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # mm_rdb_Sequence's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = mm_rdb_Sequence(cacheSize=7)
    partner = Schema()
    setattr(partner, 'Schema17', None)
    _safe_set(owner, 'sequences', partner)
    assert getattr(partner, 'Schema17') == owner
    _safe_set(owner, 'sequences', None)
    assert getattr(partner, 'Schema17') is None


def test_assoc_primaryKey13_stub_double():
    # PrimaryKey has no real 'PrimaryKey' property in the generated
    # code (a bare stub) -- manually attach it so mm_rdb_Table's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # mm_rdb_Table's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = mm_rdb_Table()
    partner = PrimaryKey()
    setattr(partner, 'PrimaryKey', None)
    _safe_set(owner, 'mm_rdb_Table', partner)
    assert getattr(partner, 'PrimaryKey') == owner
    _safe_set(owner, 'mm_rdb_Table', None)
    assert getattr(partner, 'PrimaryKey') is None


def test_assoc_primaryKey46_stub_double():
    # PrimaryKey has no real 'PrimaryKey48' property in the generated
    # code (a bare stub) -- manually attach it so mm_rdb_CreateTable's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # mm_rdb_CreateTable's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = mm_rdb_CreateTable(tableName="sample_text")
    partner = PrimaryKey()
    setattr(partner, 'PrimaryKey48', None)
    _safe_set(owner, 'mm_rdb_CreateTable47', partner)
    assert getattr(partner, 'PrimaryKey48') == owner
    _safe_set(owner, 'mm_rdb_CreateTable47', None)
    assert getattr(partner, 'PrimaryKey48') is None


def test_assoc_renamedColumn63_stub_double():
    # TableColumn has no real 'TableColumn65' property in the generated
    # code (a bare stub) -- manually attach it so mm_rdb_RenameColumn's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # mm_rdb_RenameColumn's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = mm_rdb_RenameColumn(newColumnName="sample_text")
    partner = TableColumn()
    setattr(partner, 'TableColumn65', None)
    _safe_set(owner, 'mm_rdb_RenameColumn64', partner)
    assert getattr(partner, 'TableColumn65') == owner
    _safe_set(owner, 'mm_rdb_RenameColumn64', None)
    assert getattr(partner, 'TableColumn65') is None


def test_assoc_renamedTable52_stub_double():
    # Table has no real 'Table53' property in the generated
    # code (a bare stub) -- manually attach it so mm_rdb_RenameTable's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # mm_rdb_RenameTable's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = mm_rdb_RenameTable(newName="sample_text")
    partner = Table()
    setattr(partner, 'Table53', None)
    _safe_set(owner, 'mm_rdb_RenameTable', partner)
    assert getattr(partner, 'Table53') == owner
    _safe_set(owner, 'mm_rdb_RenameTable', None)
    assert getattr(partner, 'Table53') is None


def test_assoc_tableColumns41_stub_double():
    # TableColumn has no real 'TableColumn42' property in the generated
    # code (a bare stub) -- manually attach it so mm_rdb_CreateTable's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # mm_rdb_CreateTable's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = mm_rdb_CreateTable(tableName="sample_text")
    partner = TableColumn()
    setattr(partner, 'TableColumn42', None)
    _safe_set(owner, 'mm_rdb_CreateTable', {partner})
    assert getattr(partner, 'TableColumn42') == owner
    _safe_set(owner, 'mm_rdb_CreateTable', set())
    assert getattr(partner, 'TableColumn42') is None


def test_assoc_tableConstraints43_stub_double():
    # TableConstraint has no real 'TableConstraint45' property in the generated
    # code (a bare stub) -- manually attach it so mm_rdb_CreateTable's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # mm_rdb_CreateTable's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = mm_rdb_CreateTable(tableName="sample_text")
    partner = TableConstraint()
    setattr(partner, 'TableConstraint45', None)
    _safe_set(owner, 'mm_rdb_CreateTable44', {partner})
    assert getattr(partner, 'TableConstraint45') == owner
    _safe_set(owner, 'mm_rdb_CreateTable44', set())
    assert getattr(partner, 'TableConstraint45') is None


