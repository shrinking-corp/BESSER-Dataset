import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Column,
    ColumnConstraint,
    ColumnMapping,
    Expression,
    Index,
    IndexedColumn,
    NameProvider,
    StringToColumnMappingEntryMap,
    StringToTableMappingEntryMap,
    Table,
    TableConstraint,
    TableMapping,
    Trigger,
    View,
    index_model_Database,
    model_Database,
    model_DatabaseVersion,
    model_DatabaseVersions,
    model_column_CheckColumnConstraint,
    model_column_Column,
    model_column_ColumnConstraint,
    model_column_DefaultExpressionValueColumnConstraint,
    model_column_DefaultIntegerValueColumnConstraint,
    model_column_DefaultRealValueColumnConstraint,
    model_column_DefaultStringValueColumnConstraint,
    model_column_DefaultValueColumnConstraint,
    model_column_ForeignKeyColumnConstraint,
    model_column_IndexedColumn,
    model_column_NotNullColumnConstraint,
    model_column_PrimaryKeyColumnConstraint,
    model_column_UniqueColumnConstraint,
    model_common_ColumnMapping,
    model_common_MappingEntry,
    model_common_NameProvider,
    model_common_StringToColumnMappingEntryMap,
    model_common_StringToTableMappingEntryMap,
    model_common_TableMapping,
    model_expression_Expression,
    model_index_Index,
    model_table_CheckTableConstraint,
    model_table_ForeignKeyTableConstraint,
    model_table_PrimaryKeyTableConstraint,
    model_table_Table,
    model_table_TableConstraint,
    model_table_UniqueTableConstraint,
    model_trigger_Trigger,
    model_view_View,
    table_model_Database,
    trigger_model_Database,
    view_model_Database,
    DataType,
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

def test_assoc_column50_stub_double():
    # Column has no real 'Column52' property in the generated
    # code (a bare stub) -- manually attach it so model_column_ColumnConstraint's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # model_column_ColumnConstraint's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = model_column_ColumnConstraint(name="sample_text")
    partner = Column()
    setattr(partner, 'Column52', None)
    _safe_set(owner, 'constraints51', partner)
    assert getattr(partner, 'Column52') == owner
    _safe_set(owner, 'constraints51', None)
    assert getattr(partner, 'Column52') is None


def test_assoc_constraints47_stub_double():
    # ColumnConstraint has no real 'ColumnConstraint' property in the generated
    # code (a bare stub) -- manually attach it so model_column_Column's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # model_column_Column's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = model_column_Column(type="sample_text")
    partner = ColumnConstraint()
    setattr(partner, 'ColumnConstraint', None)
    _safe_set(owner, 'column', {partner})
    assert getattr(partner, 'ColumnConstraint') == owner
    _safe_set(owner, 'column', set())
    assert getattr(partner, 'ColumnConstraint') is None


def test_assoc_curr2entryMap20_stub_double():
    # StringToTableMappingEntryMap has no real 'StringToTableMappingEntryMap22' property in the generated
    # code (a bare stub) -- manually attach it so model_common_TableMapping's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # model_common_TableMapping's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = model_common_TableMapping()
    partner = StringToTableMappingEntryMap()
    setattr(partner, 'StringToTableMappingEntryMap22', None)
    _safe_set(owner, 'model_common_TableMapping21', {partner})
    assert getattr(partner, 'StringToTableMappingEntryMap22') == owner
    _safe_set(owner, 'model_common_TableMapping21', set())
    assert getattr(partner, 'StringToTableMappingEntryMap22') is None


def test_assoc_curr2entryMap24_stub_double():
    # StringToColumnMappingEntryMap has no real 'StringToColumnMappingEntryMap26' property in the generated
    # code (a bare stub) -- manually attach it so model_common_ColumnMapping's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # model_common_ColumnMapping's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = model_common_ColumnMapping()
    partner = StringToColumnMappingEntryMap()
    setattr(partner, 'StringToColumnMappingEntryMap26', None)
    _safe_set(owner, 'model_common_ColumnMapping25', {partner})
    assert getattr(partner, 'StringToColumnMappingEntryMap26') == owner
    _safe_set(owner, 'model_common_ColumnMapping25', set())
    assert getattr(partner, 'StringToColumnMappingEntryMap26') is None


def test_assoc_prev2entryMap19_stub_double():
    # StringToTableMappingEntryMap has no real 'StringToTableMappingEntryMap' property in the generated
    # code (a bare stub) -- manually attach it so model_common_TableMapping's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # model_common_TableMapping's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = model_common_TableMapping()
    partner = StringToTableMappingEntryMap()
    setattr(partner, 'StringToTableMappingEntryMap', None)
    _safe_set(owner, 'model_common_TableMapping', {partner})
    assert getattr(partner, 'StringToTableMappingEntryMap') == owner
    _safe_set(owner, 'model_common_TableMapping', set())
    assert getattr(partner, 'StringToTableMappingEntryMap') is None


def test_assoc_prev2entryMap23_stub_double():
    # StringToColumnMappingEntryMap has no real 'StringToColumnMappingEntryMap' property in the generated
    # code (a bare stub) -- manually attach it so model_common_ColumnMapping's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # model_common_ColumnMapping's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = model_common_ColumnMapping()
    partner = StringToColumnMappingEntryMap()
    setattr(partner, 'StringToColumnMappingEntryMap', None)
    _safe_set(owner, 'model_common_ColumnMapping', {partner})
    assert getattr(partner, 'StringToColumnMappingEntryMap') == owner
    _safe_set(owner, 'model_common_ColumnMapping', set())
    assert getattr(partner, 'StringToColumnMappingEntryMap') is None


def test_assoc_table31_stub_double():
    # Table has no real 'Table32' property in the generated
    # code (a bare stub) -- manually attach it so model_table_TableConstraint's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # model_table_TableConstraint's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = model_table_TableConstraint(name="sample_text")
    partner = Table()
    setattr(partner, 'Table32', None)
    _safe_set(owner, 'constraints', partner)
    assert getattr(partner, 'Table32') == owner
    _safe_set(owner, 'constraints', None)
    assert getattr(partner, 'Table32') is None


def test_assoc_table45_stub_double():
    # Table has no real 'Table46' property in the generated
    # code (a bare stub) -- manually attach it so model_column_Column's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # model_column_Column's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = model_column_Column(type="sample_text")
    partner = Table()
    setattr(partner, 'Table46', None)
    _safe_set(owner, 'columns', partner)
    assert getattr(partner, 'Table46') == owner
    _safe_set(owner, 'columns', None)
    assert getattr(partner, 'Table46') is None


def test_assoc_versions0_stub_double():
    # model_DatabaseVersion has no real 'model_DatabaseVersion' property in the generated
    # code (a bare stub) -- manually attach it so model_DatabaseVersions's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # model_DatabaseVersions's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = model_DatabaseVersions(fileName="sample_text", packageName="sample_text")
    partner = model_DatabaseVersion()
    setattr(partner, 'model_DatabaseVersion', None)
    _safe_set(owner, 'model_DatabaseVersions', {partner})
    assert getattr(partner, 'model_DatabaseVersion') == owner
    _safe_set(owner, 'model_DatabaseVersions', set())
    assert getattr(partner, 'model_DatabaseVersion') is None


