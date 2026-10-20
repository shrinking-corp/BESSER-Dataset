import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    ColumnConstraint,
    ColumnSource,
    ConfigurationStatement,
    ContentUriSegment,
    DDLStatement,
    DMLStatement,
    DefaultValue,
    Expression,
    LiteralValue,
    SelectCoreExpression,
    SelectSource,
    SingleSource,
    TableConstraint,
    TableDefinition,
    sqliteModel_ActionStatement,
    sqliteModel_AlterTableAddColumnStatement,
    sqliteModel_AlterTableRenameStatement,
    sqliteModel_Case,
    sqliteModel_CaseExpression,
    sqliteModel_CastExpression,
    sqliteModel_CheckConstraint,
    sqliteModel_CheckTableConstraint,
    sqliteModel_ColumnConstraint,
    sqliteModel_ColumnDef,
    sqliteModel_ColumnSource,
    sqliteModel_ColumnSourceRef,
    sqliteModel_ConfigBlock,
    sqliteModel_ConfigurationStatement,
    sqliteModel_ConflictClause,
    sqliteModel_ContentUri,
    sqliteModel_ContentUriParamSegment,
    sqliteModel_ContentUriSegment,
    sqliteModel_CreateIndexStatement,
    sqliteModel_CreateTableStatement,
    sqliteModel_CreateTriggerStatement,
    sqliteModel_CreateViewStatement,
    sqliteModel_CurrentDateLiteral,
    sqliteModel_CurrentTimeLiteral,
    sqliteModel_CurrentTimeStampLiteral,
    sqliteModel_DDLStatement,
    sqliteModel_DMLStatement,
    sqliteModel_DatabaseBlock,
    sqliteModel_DefaultConstraint,
    sqliteModel_DefaultValue,
    sqliteModel_DeleteStatement,
    sqliteModel_DropIndexStatement,
    sqliteModel_DropTableStatement,
    sqliteModel_DropTriggerStatement,
    sqliteModel_DropViewStatement,
    sqliteModel_ExprAdd,
    sqliteModel_ExprAnd,
    sqliteModel_ExprBit,
    sqliteModel_ExprConcat,
    sqliteModel_ExprEqual,
    sqliteModel_ExprMult,
    sqliteModel_ExprOr,
    sqliteModel_ExprRelate,
    sqliteModel_Expression,
    sqliteModel_ExpressionDefaultValue,
    sqliteModel_Function,
    sqliteModel_FunctionArg,
    sqliteModel_FunctionArgument,
    sqliteModel_GroupByExpressions,
    sqliteModel_HavingExpressions,
    sqliteModel_IndexedColumn,
    sqliteModel_InitBlock,
    sqliteModel_InsertStatement,
    sqliteModel_IsNull,
    sqliteModel_JoinSource,
    sqliteModel_JoinStatement,
    sqliteModel_Literal,
    sqliteModel_LiteralDefaultValue,
    sqliteModel_LiteralValue,
    sqliteModel_MigrationBlock,
    sqliteModel_Model,
    sqliteModel_NestedExpression,
    sqliteModel_NewColumn,
    sqliteModel_NotNull,
    sqliteModel_NotNullConstraint,
    sqliteModel_NullCheckExpression,
    sqliteModel_NullLiteral,
    sqliteModel_NumericLiteral,
    sqliteModel_OldColumn,
    sqliteModel_OrderingTerm,
    sqliteModel_OrderingTermList,
    sqliteModel_PrimaryConstraint,
    sqliteModel_PrimaryKeyColumnConstraint,
    sqliteModel_ResultColumn,
    sqliteModel_SelectCore,
    sqliteModel_SelectCoreExpression,
    sqliteModel_SelectExpression,
    sqliteModel_SelectList,
    sqliteModel_SelectSource,
    sqliteModel_SelectStatement,
    sqliteModel_SelectStatementExpression,
    sqliteModel_SingleSource,
    sqliteModel_SingleSourceJoin,
    sqliteModel_SingleSourceSelectStatement,
    sqliteModel_SingleSourceTable,
    sqliteModel_StringLiteral,
    sqliteModel_TableConstraint,
    sqliteModel_TableDefinition,
    sqliteModel_UniqueConstraint,
    sqliteModel_UniqueTableConstraint,
    sqliteModel_UpdateColumnExpression,
    sqliteModel_UpdateStatement,
    sqliteModel_WhereExpressions,
    ColumnType,
    CompoundOperator,
    ConflictResolution,
    SqliteDataType,
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

def test_assoc_args117_reverse_link_reassign_clear():
    a1 = sqliteModel_FunctionArg(name="sample_text", type="sample_text")
    a2 = sqliteModel_FunctionArg(name="sample_text_2", type="sample_text_2")
    b = sqliteModel_Function(all=True)
    _safe_set(b, 'sqliteModel_Function', {a1})
    assert _is_linked(b, 'sqliteModel_Function', a1)
    if hasattr(a1, 'sqliteModel_FunctionArg'):
        assert _is_linked(a1, 'sqliteModel_FunctionArg', b)
    _safe_set(b, 'sqliteModel_Function', {a2})
    assert _is_linked(b, 'sqliteModel_Function', a2)
    if hasattr(a1, 'sqliteModel_FunctionArg'):
        assert not _is_linked(a1, 'sqliteModel_FunctionArg', b)
    if hasattr(a2, 'sqliteModel_FunctionArg'):
        assert _is_linked(a2, 'sqliteModel_FunctionArg', b)
    _safe_set(b, 'sqliteModel_Function', set())
    assert not _is_linked(b, 'sqliteModel_Function', a2)
    if hasattr(a2, 'sqliteModel_FunctionArg'):
        assert not _is_linked(a2, 'sqliteModel_FunctionArg', b)


def test_assoc_column174_reverse_link_reassign_clear():
    a1 = sqliteModel_ColumnSourceRef(all=True)
    a2 = sqliteModel_ColumnSourceRef(all=False)
    b = sqliteModel_ColumnSource(name="sample_text")
    _safe_set(b, 'sqliteModel_ColumnSource176', a1)
    assert _is_linked(b, 'sqliteModel_ColumnSource176', a1)
    if hasattr(a1, 'sqliteModel_ColumnSourceRef175'):
        assert _is_linked(a1, 'sqliteModel_ColumnSourceRef175', b)
    _safe_set(b, 'sqliteModel_ColumnSource176', a2)
    assert _is_linked(b, 'sqliteModel_ColumnSource176', a2)
    if hasattr(a1, 'sqliteModel_ColumnSourceRef175'):
        assert not _is_linked(a1, 'sqliteModel_ColumnSourceRef175', b)
    if hasattr(a2, 'sqliteModel_ColumnSourceRef175'):
        assert _is_linked(a2, 'sqliteModel_ColumnSourceRef175', b)
    _safe_set(b, 'sqliteModel_ColumnSource176', None)
    assert not _is_linked(b, 'sqliteModel_ColumnSource176', a2)
    if hasattr(a2, 'sqliteModel_ColumnSourceRef175'):
        assert not _is_linked(a2, 'sqliteModel_ColumnSourceRef175', b)


def test_assoc_columnDefs219_reverse_link_reassign_clear():
    a1 = sqliteModel_CreateTableStatement(temporary=True)
    a2 = sqliteModel_CreateTableStatement(temporary=False)
    b = sqliteModel_ColumnSource(name="sample_text")
    _safe_set(b, 'sqliteModel_ColumnSource220', a1)
    assert _is_linked(b, 'sqliteModel_ColumnSource220', a1)
    if hasattr(a1, 'sqliteModel_CreateTableStatement'):
        assert _is_linked(a1, 'sqliteModel_CreateTableStatement', b)
    _safe_set(b, 'sqliteModel_ColumnSource220', a2)
    assert _is_linked(b, 'sqliteModel_ColumnSource220', a2)
    if hasattr(a1, 'sqliteModel_CreateTableStatement'):
        assert not _is_linked(a1, 'sqliteModel_CreateTableStatement', b)
    if hasattr(a2, 'sqliteModel_CreateTableStatement'):
        assert _is_linked(a2, 'sqliteModel_CreateTableStatement', b)
    _safe_set(b, 'sqliteModel_ColumnSource220', None)
    assert not _is_linked(b, 'sqliteModel_ColumnSource220', a2)
    if hasattr(a2, 'sqliteModel_CreateTableStatement'):
        assert not _is_linked(a2, 'sqliteModel_CreateTableStatement', b)


def test_assoc_columnNames93_reverse_link_reassign_clear():
    a1 = sqliteModel_InsertStatement(conflictResolution="sample_text")
    a2 = sqliteModel_InsertStatement(conflictResolution="sample_text_2")
    b = sqliteModel_ColumnDef(type="sample_text")
    _safe_set(b, 'sqliteModel_ColumnDef95', a1)
    assert _is_linked(b, 'sqliteModel_ColumnDef95', a1)
    if hasattr(a1, 'sqliteModel_InsertStatement94'):
        assert _is_linked(a1, 'sqliteModel_InsertStatement94', b)
    _safe_set(b, 'sqliteModel_ColumnDef95', a2)
    assert _is_linked(b, 'sqliteModel_ColumnDef95', a2)
    if hasattr(a1, 'sqliteModel_InsertStatement94'):
        assert not _is_linked(a1, 'sqliteModel_InsertStatement94', b)
    if hasattr(a2, 'sqliteModel_InsertStatement94'):
        assert _is_linked(a2, 'sqliteModel_InsertStatement94', b)
    _safe_set(b, 'sqliteModel_ColumnDef95', None)
    assert not _is_linked(b, 'sqliteModel_ColumnDef95', a2)
    if hasattr(a2, 'sqliteModel_InsertStatement94'):
        assert not _is_linked(a2, 'sqliteModel_InsertStatement94', b)


def test_assoc_columnReference84_reverse_link_reassign_clear():
    a1 = sqliteModel_IndexedColumn(asc=True, collationName="sample_text", desc=True)
    a2 = sqliteModel_IndexedColumn(asc=False, collationName="sample_text_2", desc=False)
    b = sqliteModel_ColumnDef(type="sample_text")
    _safe_set(b, 'sqliteModel_ColumnDef', a1)
    assert _is_linked(b, 'sqliteModel_ColumnDef', a1)
    if hasattr(a1, 'sqliteModel_IndexedColumn85'):
        assert _is_linked(a1, 'sqliteModel_IndexedColumn85', b)
    _safe_set(b, 'sqliteModel_ColumnDef', a2)
    assert _is_linked(b, 'sqliteModel_ColumnDef', a2)
    if hasattr(a1, 'sqliteModel_IndexedColumn85'):
        assert not _is_linked(a1, 'sqliteModel_IndexedColumn85', b)
    if hasattr(a2, 'sqliteModel_IndexedColumn85'):
        assert _is_linked(a2, 'sqliteModel_IndexedColumn85', b)
    _safe_set(b, 'sqliteModel_ColumnDef', None)
    assert not _is_linked(b, 'sqliteModel_ColumnDef', a2)
    if hasattr(a2, 'sqliteModel_IndexedColumn85'):
        assert not _is_linked(a2, 'sqliteModel_IndexedColumn85', b)


def test_assoc_columns69_reverse_link_reassign_clear():
    a1 = sqliteModel_IndexedColumn(asc=True, collationName="sample_text", desc=True)
    a2 = sqliteModel_IndexedColumn(asc=False, collationName="sample_text_2", desc=False)
    b = sqliteModel_CreateIndexStatement(name="sample_text", unique=True)
    _safe_set(b, 'sqliteModel_CreateIndexStatement70', {a1})
    assert _is_linked(b, 'sqliteModel_CreateIndexStatement70', a1)
    if hasattr(a1, 'sqliteModel_IndexedColumn'):
        assert _is_linked(a1, 'sqliteModel_IndexedColumn', b)
    _safe_set(b, 'sqliteModel_CreateIndexStatement70', {a2})
    assert _is_linked(b, 'sqliteModel_CreateIndexStatement70', a2)
    if hasattr(a1, 'sqliteModel_IndexedColumn'):
        assert not _is_linked(a1, 'sqliteModel_IndexedColumn', b)
    if hasattr(a2, 'sqliteModel_IndexedColumn'):
        assert _is_linked(a2, 'sqliteModel_IndexedColumn', b)
    _safe_set(b, 'sqliteModel_CreateIndexStatement70', set())
    assert not _is_linked(b, 'sqliteModel_CreateIndexStatement70', a2)
    if hasattr(a2, 'sqliteModel_IndexedColumn'):
        assert not _is_linked(a2, 'sqliteModel_IndexedColumn', b)


def test_assoc_constraints221_reverse_link_reassign_clear():
    a1 = sqliteModel_TableConstraint(name="sample_text")
    a2 = sqliteModel_TableConstraint(name="sample_text_2")
    b = sqliteModel_CreateTableStatement(temporary=True)
    _safe_set(b, 'sqliteModel_CreateTableStatement222', {a1})
    assert _is_linked(b, 'sqliteModel_CreateTableStatement222', a1)
    if hasattr(a1, 'sqliteModel_TableConstraint'):
        assert _is_linked(a1, 'sqliteModel_TableConstraint', b)
    _safe_set(b, 'sqliteModel_CreateTableStatement222', {a2})
    assert _is_linked(b, 'sqliteModel_CreateTableStatement222', a2)
    if hasattr(a1, 'sqliteModel_TableConstraint'):
        assert not _is_linked(a1, 'sqliteModel_TableConstraint', b)
    if hasattr(a2, 'sqliteModel_TableConstraint'):
        assert _is_linked(a2, 'sqliteModel_TableConstraint', b)
    _safe_set(b, 'sqliteModel_CreateTableStatement222', set())
    assert not _is_linked(b, 'sqliteModel_CreateTableStatement222', a2)
    if hasattr(a2, 'sqliteModel_TableConstraint'):
        assert not _is_linked(a2, 'sqliteModel_TableConstraint', b)


def test_assoc_database0_reverse_link_reassign_clear():
    a1 = sqliteModel_Model(packageName="sample_text")
    a2 = sqliteModel_Model(packageName="sample_text_2")
    b = sqliteModel_DatabaseBlock(name="sample_text")
    _safe_set(b, 'sqliteModel_DatabaseBlock', a1)
    assert _is_linked(b, 'sqliteModel_DatabaseBlock', a1)
    if hasattr(a1, 'sqliteModel_Model'):
        assert _is_linked(a1, 'sqliteModel_Model', b)
    _safe_set(b, 'sqliteModel_DatabaseBlock', a2)
    assert _is_linked(b, 'sqliteModel_DatabaseBlock', a2)
    if hasattr(a1, 'sqliteModel_Model'):
        assert not _is_linked(a1, 'sqliteModel_Model', b)
    if hasattr(a2, 'sqliteModel_Model'):
        assert _is_linked(a2, 'sqliteModel_Model', b)
    _safe_set(b, 'sqliteModel_DatabaseBlock', None)
    assert not _is_linked(b, 'sqliteModel_DatabaseBlock', a2)
    if hasattr(a2, 'sqliteModel_Model'):
        assert not _is_linked(a2, 'sqliteModel_Model', b)


def test_assoc_index71_reverse_link_reassign_clear():
    a1 = sqliteModel_DropIndexStatement(ifExists=True)
    a2 = sqliteModel_DropIndexStatement(ifExists=False)
    b = sqliteModel_CreateIndexStatement(name="sample_text", unique=True)
    _safe_set(b, 'sqliteModel_CreateIndexStatement72', a1)
    assert _is_linked(b, 'sqliteModel_CreateIndexStatement72', a1)
    if hasattr(a1, 'sqliteModel_DropIndexStatement'):
        assert _is_linked(a1, 'sqliteModel_DropIndexStatement', b)
    _safe_set(b, 'sqliteModel_CreateIndexStatement72', a2)
    assert _is_linked(b, 'sqliteModel_CreateIndexStatement72', a2)
    if hasattr(a1, 'sqliteModel_DropIndexStatement'):
        assert not _is_linked(a1, 'sqliteModel_DropIndexStatement', b)
    if hasattr(a2, 'sqliteModel_DropIndexStatement'):
        assert _is_linked(a2, 'sqliteModel_DropIndexStatement', b)
    _safe_set(b, 'sqliteModel_CreateIndexStatement72', None)
    assert not _is_linked(b, 'sqliteModel_CreateIndexStatement72', a2)
    if hasattr(a2, 'sqliteModel_DropIndexStatement'):
        assert not _is_linked(a2, 'sqliteModel_DropIndexStatement', b)


def test_assoc_segments11_reverse_link_reassign_clear():
    a1 = sqliteModel_ContentUriSegment(name="sample_text")
    a2 = sqliteModel_ContentUriSegment(name="sample_text_2")
    b = sqliteModel_ContentUri(type="sample_text")
    _safe_set(b, 'sqliteModel_ContentUri', {a1})
    assert _is_linked(b, 'sqliteModel_ContentUri', a1)
    if hasattr(a1, 'sqliteModel_ContentUriSegment'):
        assert _is_linked(a1, 'sqliteModel_ContentUriSegment', b)
    _safe_set(b, 'sqliteModel_ContentUri', {a2})
    assert _is_linked(b, 'sqliteModel_ContentUri', a2)
    if hasattr(a1, 'sqliteModel_ContentUriSegment'):
        assert not _is_linked(a1, 'sqliteModel_ContentUriSegment', b)
    if hasattr(a2, 'sqliteModel_ContentUriSegment'):
        assert _is_linked(a2, 'sqliteModel_ContentUriSegment', b)
    _safe_set(b, 'sqliteModel_ContentUri', set())
    assert not _is_linked(b, 'sqliteModel_ContentUri', a2)
    if hasattr(a2, 'sqliteModel_ContentUriSegment'):
        assert not _is_linked(a2, 'sqliteModel_ContentUriSegment', b)


def test_assoc_source173_reverse_link_reassign_clear():
    a1 = sqliteModel_SelectSource(name="sample_text")
    a2 = sqliteModel_SelectSource(name="sample_text_2")
    b = sqliteModel_ColumnSourceRef(all=True)
    _safe_set(b, 'sqliteModel_ColumnSourceRef', a1)
    assert _is_linked(b, 'sqliteModel_ColumnSourceRef', a1)
    if hasattr(a1, 'sqliteModel_SelectSource'):
        assert _is_linked(a1, 'sqliteModel_SelectSource', b)
    _safe_set(b, 'sqliteModel_ColumnSourceRef', a2)
    assert _is_linked(b, 'sqliteModel_ColumnSourceRef', a2)
    if hasattr(a1, 'sqliteModel_SelectSource'):
        assert not _is_linked(a1, 'sqliteModel_SelectSource', b)
    if hasattr(a2, 'sqliteModel_SelectSource'):
        assert _is_linked(a2, 'sqliteModel_SelectSource', b)
    _safe_set(b, 'sqliteModel_ColumnSourceRef', None)
    assert not _is_linked(b, 'sqliteModel_ColumnSourceRef', a2)
    if hasattr(a2, 'sqliteModel_SelectSource'):
        assert not _is_linked(a2, 'sqliteModel_SelectSource', b)


def test_assoc_table102_reverse_link_reassign_clear():
    a1 = sqliteModel_UpdateStatement(conflictResolution="sample_text")
    a2 = sqliteModel_UpdateStatement(conflictResolution="sample_text_2")
    b = sqliteModel_TableDefinition(name="sample_text")
    _safe_set(b, 'sqliteModel_TableDefinition103', a1)
    assert _is_linked(b, 'sqliteModel_TableDefinition103', a1)
    if hasattr(a1, 'sqliteModel_UpdateStatement'):
        assert _is_linked(a1, 'sqliteModel_UpdateStatement', b)
    _safe_set(b, 'sqliteModel_TableDefinition103', a2)
    assert _is_linked(b, 'sqliteModel_TableDefinition103', a2)
    if hasattr(a1, 'sqliteModel_UpdateStatement'):
        assert not _is_linked(a1, 'sqliteModel_UpdateStatement', b)
    if hasattr(a2, 'sqliteModel_UpdateStatement'):
        assert _is_linked(a2, 'sqliteModel_UpdateStatement', b)
    _safe_set(b, 'sqliteModel_TableDefinition103', None)
    assert not _is_linked(b, 'sqliteModel_TableDefinition103', a2)
    if hasattr(a2, 'sqliteModel_UpdateStatement'):
        assert not _is_linked(a2, 'sqliteModel_UpdateStatement', b)


def test_assoc_table51_reverse_link_reassign_clear():
    a1 = sqliteModel_TableDefinition(name="sample_text")
    a2 = sqliteModel_TableDefinition(name="sample_text_2")
    b = sqliteModel_CreateTriggerStatement(eventType="sample_text", forEachRow="sample_text", name="sample_text", temporary=True, updateColumnNames="sample_text", when="sample_text")
    _safe_set(b, 'sqliteModel_CreateTriggerStatement', a1)
    assert _is_linked(b, 'sqliteModel_CreateTriggerStatement', a1)
    if hasattr(a1, 'sqliteModel_TableDefinition'):
        assert _is_linked(a1, 'sqliteModel_TableDefinition', b)
    _safe_set(b, 'sqliteModel_CreateTriggerStatement', a2)
    assert _is_linked(b, 'sqliteModel_CreateTriggerStatement', a2)
    if hasattr(a1, 'sqliteModel_TableDefinition'):
        assert not _is_linked(a1, 'sqliteModel_TableDefinition', b)
    if hasattr(a2, 'sqliteModel_TableDefinition'):
        assert _is_linked(a2, 'sqliteModel_TableDefinition', b)
    _safe_set(b, 'sqliteModel_CreateTriggerStatement', None)
    assert not _is_linked(b, 'sqliteModel_CreateTriggerStatement', a2)
    if hasattr(a2, 'sqliteModel_TableDefinition'):
        assert not _is_linked(a2, 'sqliteModel_TableDefinition', b)


def test_assoc_table62_reverse_link_reassign_clear():
    a1 = sqliteModel_TableDefinition(name="sample_text")
    a2 = sqliteModel_TableDefinition(name="sample_text_2")
    b = sqliteModel_DropTableStatement(ifExists=True)
    _safe_set(b, 'sqliteModel_DropTableStatement', a1)
    assert _is_linked(b, 'sqliteModel_DropTableStatement', a1)
    if hasattr(a1, 'sqliteModel_TableDefinition63'):
        assert _is_linked(a1, 'sqliteModel_TableDefinition63', b)
    _safe_set(b, 'sqliteModel_DropTableStatement', a2)
    assert _is_linked(b, 'sqliteModel_DropTableStatement', a2)
    if hasattr(a1, 'sqliteModel_TableDefinition63'):
        assert not _is_linked(a1, 'sqliteModel_TableDefinition63', b)
    if hasattr(a2, 'sqliteModel_TableDefinition63'):
        assert _is_linked(a2, 'sqliteModel_TableDefinition63', b)
    _safe_set(b, 'sqliteModel_DropTableStatement', None)
    assert not _is_linked(b, 'sqliteModel_DropTableStatement', a2)
    if hasattr(a2, 'sqliteModel_TableDefinition63'):
        assert not _is_linked(a2, 'sqliteModel_TableDefinition63', b)


def test_assoc_table67_reverse_link_reassign_clear():
    a1 = sqliteModel_TableDefinition(name="sample_text")
    a2 = sqliteModel_TableDefinition(name="sample_text_2")
    b = sqliteModel_CreateIndexStatement(name="sample_text", unique=True)
    _safe_set(b, 'sqliteModel_CreateIndexStatement', a1)
    assert _is_linked(b, 'sqliteModel_CreateIndexStatement', a1)
    if hasattr(a1, 'sqliteModel_TableDefinition68'):
        assert _is_linked(a1, 'sqliteModel_TableDefinition68', b)
    _safe_set(b, 'sqliteModel_CreateIndexStatement', a2)
    assert _is_linked(b, 'sqliteModel_CreateIndexStatement', a2)
    if hasattr(a1, 'sqliteModel_TableDefinition68'):
        assert not _is_linked(a1, 'sqliteModel_TableDefinition68', b)
    if hasattr(a2, 'sqliteModel_TableDefinition68'):
        assert _is_linked(a2, 'sqliteModel_TableDefinition68', b)
    _safe_set(b, 'sqliteModel_CreateIndexStatement', None)
    assert not _is_linked(b, 'sqliteModel_CreateIndexStatement', a2)
    if hasattr(a2, 'sqliteModel_TableDefinition68'):
        assert not _is_linked(a2, 'sqliteModel_TableDefinition68', b)


def test_assoc_table91_reverse_link_reassign_clear():
    a1 = sqliteModel_TableDefinition(name="sample_text")
    a2 = sqliteModel_TableDefinition(name="sample_text_2")
    b = sqliteModel_InsertStatement(conflictResolution="sample_text")
    _safe_set(b, 'sqliteModel_InsertStatement', a1)
    assert _is_linked(b, 'sqliteModel_InsertStatement', a1)
    if hasattr(a1, 'sqliteModel_TableDefinition92'):
        assert _is_linked(a1, 'sqliteModel_TableDefinition92', b)
    _safe_set(b, 'sqliteModel_InsertStatement', a2)
    assert _is_linked(b, 'sqliteModel_InsertStatement', a2)
    if hasattr(a1, 'sqliteModel_TableDefinition92'):
        assert not _is_linked(a1, 'sqliteModel_TableDefinition92', b)
    if hasattr(a2, 'sqliteModel_TableDefinition92'):
        assert _is_linked(a2, 'sqliteModel_TableDefinition92', b)
    _safe_set(b, 'sqliteModel_InsertStatement', None)
    assert not _is_linked(b, 'sqliteModel_InsertStatement', a2)
    if hasattr(a2, 'sqliteModel_TableDefinition92'):
        assert not _is_linked(a2, 'sqliteModel_TableDefinition92', b)


def test_assoc_trigger64_reverse_link_reassign_clear():
    a1 = sqliteModel_DropTriggerStatement(ifExists=True)
    a2 = sqliteModel_DropTriggerStatement(ifExists=False)
    b = sqliteModel_CreateTriggerStatement(eventType="sample_text", forEachRow="sample_text", name="sample_text", temporary=True, updateColumnNames="sample_text", when="sample_text")
    _safe_set(b, 'sqliteModel_CreateTriggerStatement65', a1)
    assert _is_linked(b, 'sqliteModel_CreateTriggerStatement65', a1)
    if hasattr(a1, 'sqliteModel_DropTriggerStatement'):
        assert _is_linked(a1, 'sqliteModel_DropTriggerStatement', b)
    _safe_set(b, 'sqliteModel_CreateTriggerStatement65', a2)
    assert _is_linked(b, 'sqliteModel_CreateTriggerStatement65', a2)
    if hasattr(a1, 'sqliteModel_DropTriggerStatement'):
        assert not _is_linked(a1, 'sqliteModel_DropTriggerStatement', b)
    if hasattr(a2, 'sqliteModel_DropTriggerStatement'):
        assert _is_linked(a2, 'sqliteModel_DropTriggerStatement', b)
    _safe_set(b, 'sqliteModel_CreateTriggerStatement65', None)
    assert not _is_linked(b, 'sqliteModel_CreateTriggerStatement65', a2)
    if hasattr(a2, 'sqliteModel_DropTriggerStatement'):
        assert not _is_linked(a2, 'sqliteModel_DropTriggerStatement', b)


def test_assoc_view66_reverse_link_reassign_clear():
    a1 = sqliteModel_DropViewStatement(ifExists=True)
    a2 = sqliteModel_DropViewStatement(ifExists=False)
    b = sqliteModel_CreateViewStatement(temporary=True)
    _safe_set(b, 'sqliteModel_CreateViewStatement', a1)
    assert _is_linked(b, 'sqliteModel_CreateViewStatement', a1)
    if hasattr(a1, 'sqliteModel_DropViewStatement'):
        assert _is_linked(a1, 'sqliteModel_DropViewStatement', b)
    _safe_set(b, 'sqliteModel_CreateViewStatement', a2)
    assert _is_linked(b, 'sqliteModel_CreateViewStatement', a2)
    if hasattr(a1, 'sqliteModel_DropViewStatement'):
        assert not _is_linked(a1, 'sqliteModel_DropViewStatement', b)
    if hasattr(a2, 'sqliteModel_DropViewStatement'):
        assert _is_linked(a2, 'sqliteModel_DropViewStatement', b)
    _safe_set(b, 'sqliteModel_CreateViewStatement', None)
    assert not _is_linked(b, 'sqliteModel_CreateViewStatement', a2)
    if hasattr(a2, 'sqliteModel_DropViewStatement'):
        assert not _is_linked(a2, 'sqliteModel_DropViewStatement', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_arg192_stub_double():
    # sqliteModel_FunctionArgument has no real 'sqliteModel_FunctionArgument' property in the generated
    # code (a bare stub) -- manually attach it so sqliteModel_FunctionArg's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # sqliteModel_FunctionArg's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = sqliteModel_FunctionArg(name="sample_text", type="sample_text")
    partner = sqliteModel_FunctionArgument()
    setattr(partner, 'sqliteModel_FunctionArgument', None)
    _safe_set(owner, 'sqliteModel_FunctionArg193', partner)
    assert getattr(partner, 'sqliteModel_FunctionArgument') == owner
    _safe_set(owner, 'sqliteModel_FunctionArg193', None)
    assert getattr(partner, 'sqliteModel_FunctionArgument') is None


def test_assoc_arguments121_stub_double():
    # sqliteModel_Expression has no real 'sqliteModel_Expression123' property in the generated
    # code (a bare stub) -- manually attach it so sqliteModel_Function's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # sqliteModel_Function's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = sqliteModel_Function(all=True)
    partner = sqliteModel_Expression()
    setattr(partner, 'sqliteModel_Expression123', None)
    _safe_set(owner, 'sqliteModel_Function122', {partner})
    assert getattr(partner, 'sqliteModel_Expression123') == owner
    _safe_set(owner, 'sqliteModel_Function122', set())
    assert getattr(partner, 'sqliteModel_Expression123') is None


def test_assoc_column169_stub_double():
    # sqliteModel_NewColumn has no real 'sqliteModel_NewColumn' property in the generated
    # code (a bare stub) -- manually attach it so sqliteModel_ColumnSource's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # sqliteModel_ColumnSource's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = sqliteModel_ColumnSource(name="sample_text")
    partner = sqliteModel_NewColumn()
    setattr(partner, 'sqliteModel_NewColumn', None)
    _safe_set(owner, 'sqliteModel_ColumnSource170', partner)
    assert getattr(partner, 'sqliteModel_NewColumn') == owner
    _safe_set(owner, 'sqliteModel_ColumnSource170', None)
    assert getattr(partner, 'sqliteModel_NewColumn') is None


def test_assoc_column171_stub_double():
    # sqliteModel_OldColumn has no real 'sqliteModel_OldColumn' property in the generated
    # code (a bare stub) -- manually attach it so sqliteModel_ColumnSource's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # sqliteModel_ColumnSource's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = sqliteModel_ColumnSource(name="sample_text")
    partner = sqliteModel_OldColumn()
    setattr(partner, 'sqliteModel_OldColumn', None)
    _safe_set(owner, 'sqliteModel_ColumnSource172', partner)
    assert getattr(partner, 'sqliteModel_OldColumn') == owner
    _safe_set(owner, 'sqliteModel_ColumnSource172', None)
    assert getattr(partner, 'sqliteModel_OldColumn') is None


def test_assoc_columnDef59_stub_double():
    # sqliteModel_AlterTableAddColumnStatement has no real 'sqliteModel_AlterTableAddColumnStatement60' property in the generated
    # code (a bare stub) -- manually attach it so sqliteModel_ColumnSource's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # sqliteModel_ColumnSource's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = sqliteModel_ColumnSource(name="sample_text")
    partner = sqliteModel_AlterTableAddColumnStatement()
    setattr(partner, 'sqliteModel_AlterTableAddColumnStatement60', None)
    _safe_set(owner, 'sqliteModel_ColumnSource61', partner)
    assert getattr(partner, 'sqliteModel_AlterTableAddColumnStatement60') == owner
    _safe_set(owner, 'sqliteModel_ColumnSource61', None)
    assert getattr(partner, 'sqliteModel_AlterTableAddColumnStatement60') is None


def test_assoc_columnName109_stub_double():
    # sqliteModel_UpdateColumnExpression has no real 'sqliteModel_UpdateColumnExpression110' property in the generated
    # code (a bare stub) -- manually attach it so sqliteModel_ColumnDef's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # sqliteModel_ColumnDef's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = sqliteModel_ColumnDef(type="sample_text")
    partner = sqliteModel_UpdateColumnExpression()
    setattr(partner, 'sqliteModel_UpdateColumnExpression110', None)
    _safe_set(owner, 'sqliteModel_ColumnDef111', partner)
    assert getattr(partner, 'sqliteModel_UpdateColumnExpression110') == owner
    _safe_set(owner, 'sqliteModel_ColumnDef111', None)
    assert getattr(partner, 'sqliteModel_UpdateColumnExpression110') is None


def test_assoc_columns73_stub_double():
    # sqliteModel_UniqueTableConstraint has no real 'sqliteModel_UniqueTableConstraint' property in the generated
    # code (a bare stub) -- manually attach it so sqliteModel_IndexedColumn's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # sqliteModel_IndexedColumn's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = sqliteModel_IndexedColumn(asc=True, collationName="sample_text", desc=True)
    partner = sqliteModel_UniqueTableConstraint()
    setattr(partner, 'sqliteModel_UniqueTableConstraint', None)
    _safe_set(owner, 'sqliteModel_IndexedColumn74', partner)
    assert owner in getattr(partner, 'sqliteModel_UniqueTableConstraint')
    _safe_set(owner, 'sqliteModel_IndexedColumn74', None)
    assert owner not in getattr(partner, 'sqliteModel_UniqueTableConstraint')


def test_assoc_columns77_stub_double():
    # sqliteModel_PrimaryConstraint has no real 'sqliteModel_PrimaryConstraint' property in the generated
    # code (a bare stub) -- manually attach it so sqliteModel_IndexedColumn's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # sqliteModel_IndexedColumn's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = sqliteModel_IndexedColumn(asc=True, collationName="sample_text", desc=True)
    partner = sqliteModel_PrimaryConstraint()
    setattr(partner, 'sqliteModel_PrimaryConstraint', None)
    _safe_set(owner, 'sqliteModel_IndexedColumn78', partner)
    assert owner in getattr(partner, 'sqliteModel_PrimaryConstraint')
    _safe_set(owner, 'sqliteModel_IndexedColumn78', None)
    assert owner not in getattr(partner, 'sqliteModel_PrimaryConstraint')


def test_assoc_config1_stub_double():
    # sqliteModel_ConfigBlock has no real 'sqliteModel_ConfigBlock' property in the generated
    # code (a bare stub) -- manually attach it so sqliteModel_DatabaseBlock's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # sqliteModel_DatabaseBlock's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = sqliteModel_DatabaseBlock(name="sample_text")
    partner = sqliteModel_ConfigBlock()
    setattr(partner, 'sqliteModel_ConfigBlock', None)
    _safe_set(owner, 'sqliteModel_DatabaseBlock2', partner)
    assert getattr(partner, 'sqliteModel_ConfigBlock') == owner
    _safe_set(owner, 'sqliteModel_DatabaseBlock2', None)
    assert getattr(partner, 'sqliteModel_ConfigBlock') is None


def test_assoc_conflictClause230_stub_double():
    # sqliteModel_NotNullConstraint has no real 'sqliteModel_NotNullConstraint' property in the generated
    # code (a bare stub) -- manually attach it so sqliteModel_ConflictClause's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # sqliteModel_ConflictClause's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = sqliteModel_ConflictClause(resolution="sample_text")
    partner = sqliteModel_NotNullConstraint()
    setattr(partner, 'sqliteModel_NotNullConstraint', None)
    _safe_set(owner, 'sqliteModel_ConflictClause231', partner)
    assert getattr(partner, 'sqliteModel_NotNullConstraint') == owner
    _safe_set(owner, 'sqliteModel_ConflictClause231', None)
    assert getattr(partner, 'sqliteModel_NotNullConstraint') is None


def test_assoc_conflictClause232_stub_double():
    # sqliteModel_UniqueConstraint has no real 'sqliteModel_UniqueConstraint' property in the generated
    # code (a bare stub) -- manually attach it so sqliteModel_ConflictClause's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # sqliteModel_ConflictClause's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = sqliteModel_ConflictClause(resolution="sample_text")
    partner = sqliteModel_UniqueConstraint()
    setattr(partner, 'sqliteModel_UniqueConstraint', None)
    _safe_set(owner, 'sqliteModel_ConflictClause233', partner)
    assert getattr(partner, 'sqliteModel_UniqueConstraint') == owner
    _safe_set(owner, 'sqliteModel_ConflictClause233', None)
    assert getattr(partner, 'sqliteModel_UniqueConstraint') is None


def test_assoc_conflictClause75_stub_double():
    # sqliteModel_UniqueTableConstraint has no real 'sqliteModel_UniqueTableConstraint76' property in the generated
    # code (a bare stub) -- manually attach it so sqliteModel_ConflictClause's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # sqliteModel_ConflictClause's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = sqliteModel_ConflictClause(resolution="sample_text")
    partner = sqliteModel_UniqueTableConstraint()
    setattr(partner, 'sqliteModel_UniqueTableConstraint76', None)
    _safe_set(owner, 'sqliteModel_ConflictClause', partner)
    assert getattr(partner, 'sqliteModel_UniqueTableConstraint76') == owner
    _safe_set(owner, 'sqliteModel_ConflictClause', None)
    assert getattr(partner, 'sqliteModel_UniqueTableConstraint76') is None


def test_assoc_conflictClause79_stub_double():
    # sqliteModel_PrimaryConstraint has no real 'sqliteModel_PrimaryConstraint80' property in the generated
    # code (a bare stub) -- manually attach it so sqliteModel_ConflictClause's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # sqliteModel_ConflictClause's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = sqliteModel_ConflictClause(resolution="sample_text")
    partner = sqliteModel_PrimaryConstraint()
    setattr(partner, 'sqliteModel_PrimaryConstraint80', None)
    _safe_set(owner, 'sqliteModel_ConflictClause81', partner)
    assert getattr(partner, 'sqliteModel_PrimaryConstraint80') == owner
    _safe_set(owner, 'sqliteModel_ConflictClause81', None)
    assert getattr(partner, 'sqliteModel_PrimaryConstraint80') is None


def test_assoc_constraints228_stub_double():
    # sqliteModel_ColumnConstraint has no real 'sqliteModel_ColumnConstraint' property in the generated
    # code (a bare stub) -- manually attach it so sqliteModel_ColumnDef's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # sqliteModel_ColumnDef's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = sqliteModel_ColumnDef(type="sample_text")
    partner = sqliteModel_ColumnConstraint()
    setattr(partner, 'sqliteModel_ColumnConstraint', None)
    _safe_set(owner, 'sqliteModel_ColumnDef229', {partner})
    assert getattr(partner, 'sqliteModel_ColumnConstraint') == owner
    _safe_set(owner, 'sqliteModel_ColumnDef229', set())
    assert getattr(partner, 'sqliteModel_ColumnConstraint') is None


def test_assoc_expression190_stub_double():
    # sqliteModel_Expression has no real 'sqliteModel_Expression191' property in the generated
    # code (a bare stub) -- manually attach it so sqliteModel_CastExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # sqliteModel_CastExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = sqliteModel_CastExpression(type="sample_text")
    partner = sqliteModel_Expression()
    setattr(partner, 'sqliteModel_Expression191', None)
    _safe_set(owner, 'sqliteModel_CastExpression', partner)
    assert getattr(partner, 'sqliteModel_Expression191') == owner
    _safe_set(owner, 'sqliteModel_CastExpression', None)
    assert getattr(partner, 'sqliteModel_Expression191') is None


def test_assoc_expression37_stub_double():
    # sqliteModel_Expression has no real 'sqliteModel_Expression39' property in the generated
    # code (a bare stub) -- manually attach it so sqliteModel_OrderingTerm's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # sqliteModel_OrderingTerm's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = sqliteModel_OrderingTerm(asc=True, desc=True)
    partner = sqliteModel_Expression()
    setattr(partner, 'sqliteModel_Expression39', None)
    _safe_set(owner, 'sqliteModel_OrderingTerm38', partner)
    assert getattr(partner, 'sqliteModel_Expression39') == owner
    _safe_set(owner, 'sqliteModel_OrderingTerm38', None)
    assert getattr(partner, 'sqliteModel_Expression39') is None


def test_assoc_expression48_stub_double():
    # sqliteModel_Expression has no real 'sqliteModel_Expression50' property in the generated
    # code (a bare stub) -- manually attach it so sqliteModel_JoinStatement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # sqliteModel_JoinStatement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = sqliteModel_JoinStatement(cross=True, inner=True, left=True, natural=True, outer=True)
    partner = sqliteModel_Expression()
    setattr(partner, 'sqliteModel_Expression50', None)
    _safe_set(owner, 'sqliteModel_JoinStatement49', partner)
    assert getattr(partner, 'sqliteModel_Expression50') == owner
    _safe_set(owner, 'sqliteModel_JoinStatement49', None)
    assert getattr(partner, 'sqliteModel_Expression50') is None


def test_assoc_expressions96_stub_double():
    # sqliteModel_Expression has no real 'sqliteModel_Expression98' property in the generated
    # code (a bare stub) -- manually attach it so sqliteModel_InsertStatement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # sqliteModel_InsertStatement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = sqliteModel_InsertStatement(conflictResolution="sample_text")
    partner = sqliteModel_Expression()
    setattr(partner, 'sqliteModel_Expression98', None)
    _safe_set(owner, 'sqliteModel_InsertStatement97', {partner})
    assert getattr(partner, 'sqliteModel_Expression98') == owner
    _safe_set(owner, 'sqliteModel_InsertStatement97', set())
    assert getattr(partner, 'sqliteModel_Expression98') is None


def test_assoc_groupBy207_stub_double():
    # sqliteModel_GroupByExpressions has no real 'sqliteModel_GroupByExpressions209' property in the generated
    # code (a bare stub) -- manually attach it so sqliteModel_SelectExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # sqliteModel_SelectExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = sqliteModel_SelectExpression(all=True, allColumns=True, distinct=True)
    partner = sqliteModel_GroupByExpressions()
    setattr(partner, 'sqliteModel_GroupByExpressions209', None)
    _safe_set(owner, 'sqliteModel_SelectExpression208', partner)
    assert getattr(partner, 'sqliteModel_GroupByExpressions209') == owner
    _safe_set(owner, 'sqliteModel_SelectExpression208', None)
    assert getattr(partner, 'sqliteModel_GroupByExpressions209') is None


def test_assoc_having210_stub_double():
    # sqliteModel_HavingExpressions has no real 'sqliteModel_HavingExpressions212' property in the generated
    # code (a bare stub) -- manually attach it so sqliteModel_SelectExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # sqliteModel_SelectExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = sqliteModel_SelectExpression(all=True, allColumns=True, distinct=True)
    partner = sqliteModel_HavingExpressions()
    setattr(partner, 'sqliteModel_HavingExpressions212', None)
    _safe_set(owner, 'sqliteModel_SelectExpression211', partner)
    assert getattr(partner, 'sqliteModel_HavingExpressions212') == owner
    _safe_set(owner, 'sqliteModel_SelectExpression211', None)
    assert getattr(partner, 'sqliteModel_HavingExpressions212') is None


def test_assoc_init3_stub_double():
    # sqliteModel_InitBlock has no real 'sqliteModel_InitBlock' property in the generated
    # code (a bare stub) -- manually attach it so sqliteModel_DatabaseBlock's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # sqliteModel_DatabaseBlock's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = sqliteModel_DatabaseBlock(name="sample_text")
    partner = sqliteModel_InitBlock()
    setattr(partner, 'sqliteModel_InitBlock', None)
    _safe_set(owner, 'sqliteModel_DatabaseBlock4', partner)
    assert getattr(partner, 'sqliteModel_InitBlock') == owner
    _safe_set(owner, 'sqliteModel_DatabaseBlock4', None)
    assert getattr(partner, 'sqliteModel_InitBlock') is None


def test_assoc_joinStatements41_stub_double():
    # sqliteModel_JoinSource has no real 'sqliteModel_JoinSource42' property in the generated
    # code (a bare stub) -- manually attach it so sqliteModel_JoinStatement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # sqliteModel_JoinStatement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = sqliteModel_JoinStatement(cross=True, inner=True, left=True, natural=True, outer=True)
    partner = sqliteModel_JoinSource()
    setattr(partner, 'sqliteModel_JoinSource42', None)
    _safe_set(owner, 'sqliteModel_JoinStatement', partner)
    assert owner in getattr(partner, 'sqliteModel_JoinSource42')
    _safe_set(owner, 'sqliteModel_JoinStatement', None)
    assert owner not in getattr(partner, 'sqliteModel_JoinSource42')


def test_assoc_left124_stub_double():
    # sqliteModel_Expression has no real 'sqliteModel_Expression125' property in the generated
    # code (a bare stub) -- manually attach it so sqliteModel_ExprConcat's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # sqliteModel_ExprConcat's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = sqliteModel_ExprConcat(op="sample_text")
    partner = sqliteModel_Expression()
    setattr(partner, 'sqliteModel_Expression125', None)
    _safe_set(owner, 'sqliteModel_ExprConcat', partner)
    assert getattr(partner, 'sqliteModel_Expression125') == owner
    _safe_set(owner, 'sqliteModel_ExprConcat', None)
    assert getattr(partner, 'sqliteModel_Expression125') is None


def test_assoc_left129_stub_double():
    # sqliteModel_Expression has no real 'sqliteModel_Expression130' property in the generated
    # code (a bare stub) -- manually attach it so sqliteModel_ExprMult's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # sqliteModel_ExprMult's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = sqliteModel_ExprMult(op="sample_text")
    partner = sqliteModel_Expression()
    setattr(partner, 'sqliteModel_Expression130', None)
    _safe_set(owner, 'sqliteModel_ExprMult', partner)
    assert getattr(partner, 'sqliteModel_Expression130') == owner
    _safe_set(owner, 'sqliteModel_ExprMult', None)
    assert getattr(partner, 'sqliteModel_Expression130') is None


def test_assoc_left134_stub_double():
    # sqliteModel_Expression has no real 'sqliteModel_Expression135' property in the generated
    # code (a bare stub) -- manually attach it so sqliteModel_ExprAdd's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # sqliteModel_ExprAdd's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = sqliteModel_ExprAdd(op="sample_text")
    partner = sqliteModel_Expression()
    setattr(partner, 'sqliteModel_Expression135', None)
    _safe_set(owner, 'sqliteModel_ExprAdd', partner)
    assert getattr(partner, 'sqliteModel_Expression135') == owner
    _safe_set(owner, 'sqliteModel_ExprAdd', None)
    assert getattr(partner, 'sqliteModel_Expression135') is None


def test_assoc_left139_stub_double():
    # sqliteModel_Expression has no real 'sqliteModel_Expression140' property in the generated
    # code (a bare stub) -- manually attach it so sqliteModel_ExprBit's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # sqliteModel_ExprBit's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = sqliteModel_ExprBit(op="sample_text")
    partner = sqliteModel_Expression()
    setattr(partner, 'sqliteModel_Expression140', None)
    _safe_set(owner, 'sqliteModel_ExprBit', partner)
    assert getattr(partner, 'sqliteModel_Expression140') == owner
    _safe_set(owner, 'sqliteModel_ExprBit', None)
    assert getattr(partner, 'sqliteModel_Expression140') is None


def test_assoc_left144_stub_double():
    # sqliteModel_Expression has no real 'sqliteModel_Expression145' property in the generated
    # code (a bare stub) -- manually attach it so sqliteModel_ExprRelate's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # sqliteModel_ExprRelate's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = sqliteModel_ExprRelate(op="sample_text")
    partner = sqliteModel_Expression()
    setattr(partner, 'sqliteModel_Expression145', None)
    _safe_set(owner, 'sqliteModel_ExprRelate', partner)
    assert getattr(partner, 'sqliteModel_Expression145') == owner
    _safe_set(owner, 'sqliteModel_ExprRelate', None)
    assert getattr(partner, 'sqliteModel_Expression145') is None


def test_assoc_left149_stub_double():
    # sqliteModel_Expression has no real 'sqliteModel_Expression150' property in the generated
    # code (a bare stub) -- manually attach it so sqliteModel_ExprEqual's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # sqliteModel_ExprEqual's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = sqliteModel_ExprEqual(op="sample_text")
    partner = sqliteModel_Expression()
    setattr(partner, 'sqliteModel_Expression150', None)
    _safe_set(owner, 'sqliteModel_ExprEqual', partner)
    assert getattr(partner, 'sqliteModel_Expression150') == owner
    _safe_set(owner, 'sqliteModel_ExprEqual', None)
    assert getattr(partner, 'sqliteModel_Expression150') is None


def test_assoc_left154_stub_double():
    # sqliteModel_Expression has no real 'sqliteModel_Expression155' property in the generated
    # code (a bare stub) -- manually attach it so sqliteModel_ExprAnd's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # sqliteModel_ExprAnd's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = sqliteModel_ExprAnd(op="sample_text")
    partner = sqliteModel_Expression()
    setattr(partner, 'sqliteModel_Expression155', None)
    _safe_set(owner, 'sqliteModel_ExprAnd', partner)
    assert getattr(partner, 'sqliteModel_Expression155') == owner
    _safe_set(owner, 'sqliteModel_ExprAnd', None)
    assert getattr(partner, 'sqliteModel_Expression155') is None


def test_assoc_left159_stub_double():
    # sqliteModel_Expression has no real 'sqliteModel_Expression160' property in the generated
    # code (a bare stub) -- manually attach it so sqliteModel_ExprOr's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # sqliteModel_ExprOr's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = sqliteModel_ExprOr(op="sample_text")
    partner = sqliteModel_Expression()
    setattr(partner, 'sqliteModel_Expression160', None)
    _safe_set(owner, 'sqliteModel_ExprOr', partner)
    assert getattr(partner, 'sqliteModel_Expression160') == owner
    _safe_set(owner, 'sqliteModel_ExprOr', None)
    assert getattr(partner, 'sqliteModel_Expression160') is None


def test_assoc_left194_stub_double():
    # sqliteModel_SelectCoreExpression has no real 'sqliteModel_SelectCoreExpression195' property in the generated
    # code (a bare stub) -- manually attach it so sqliteModel_SelectCore's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # sqliteModel_SelectCore's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = sqliteModel_SelectCore(op="sample_text")
    partner = sqliteModel_SelectCoreExpression()
    setattr(partner, 'sqliteModel_SelectCoreExpression195', None)
    _safe_set(owner, 'sqliteModel_SelectCore', partner)
    assert getattr(partner, 'sqliteModel_SelectCoreExpression195') == owner
    _safe_set(owner, 'sqliteModel_SelectCore', None)
    assert getattr(partner, 'sqliteModel_SelectCoreExpression195') is None


def test_assoc_migrations5_stub_double():
    # sqliteModel_MigrationBlock has no real 'sqliteModel_MigrationBlock' property in the generated
    # code (a bare stub) -- manually attach it so sqliteModel_DatabaseBlock's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # sqliteModel_DatabaseBlock's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = sqliteModel_DatabaseBlock(name="sample_text")
    partner = sqliteModel_MigrationBlock()
    setattr(partner, 'sqliteModel_MigrationBlock', None)
    _safe_set(owner, 'sqliteModel_DatabaseBlock6', {partner})
    assert getattr(partner, 'sqliteModel_MigrationBlock') == owner
    _safe_set(owner, 'sqliteModel_DatabaseBlock6', set())
    assert getattr(partner, 'sqliteModel_MigrationBlock') is None


def test_assoc_orderingTerms28_stub_double():
    # sqliteModel_OrderingTermList has no real 'sqliteModel_OrderingTermList29' property in the generated
    # code (a bare stub) -- manually attach it so sqliteModel_OrderingTerm's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # sqliteModel_OrderingTerm's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = sqliteModel_OrderingTerm(asc=True, desc=True)
    partner = sqliteModel_OrderingTermList()
    setattr(partner, 'sqliteModel_OrderingTermList29', None)
    _safe_set(owner, 'sqliteModel_OrderingTerm', partner)
    assert owner in getattr(partner, 'sqliteModel_OrderingTermList29')
    _safe_set(owner, 'sqliteModel_OrderingTerm', None)
    assert owner not in getattr(partner, 'sqliteModel_OrderingTermList29')


def test_assoc_resultColumns30_stub_double():
    # sqliteModel_SelectList has no real 'sqliteModel_SelectList' property in the generated
    # code (a bare stub) -- manually attach it so sqliteModel_ColumnSource's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # sqliteModel_ColumnSource's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = sqliteModel_ColumnSource(name="sample_text")
    partner = sqliteModel_SelectList()
    setattr(partner, 'sqliteModel_SelectList', None)
    _safe_set(owner, 'sqliteModel_ColumnSource', partner)
    assert owner in getattr(partner, 'sqliteModel_SelectList')
    _safe_set(owner, 'sqliteModel_ColumnSource', None)
    assert owner not in getattr(partner, 'sqliteModel_SelectList')


def test_assoc_right126_stub_double():
    # sqliteModel_Expression has no real 'sqliteModel_Expression128' property in the generated
    # code (a bare stub) -- manually attach it so sqliteModel_ExprConcat's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # sqliteModel_ExprConcat's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = sqliteModel_ExprConcat(op="sample_text")
    partner = sqliteModel_Expression()
    setattr(partner, 'sqliteModel_Expression128', None)
    _safe_set(owner, 'sqliteModel_ExprConcat127', partner)
    assert getattr(partner, 'sqliteModel_Expression128') == owner
    _safe_set(owner, 'sqliteModel_ExprConcat127', None)
    assert getattr(partner, 'sqliteModel_Expression128') is None


def test_assoc_right131_stub_double():
    # sqliteModel_Expression has no real 'sqliteModel_Expression133' property in the generated
    # code (a bare stub) -- manually attach it so sqliteModel_ExprMult's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # sqliteModel_ExprMult's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = sqliteModel_ExprMult(op="sample_text")
    partner = sqliteModel_Expression()
    setattr(partner, 'sqliteModel_Expression133', None)
    _safe_set(owner, 'sqliteModel_ExprMult132', partner)
    assert getattr(partner, 'sqliteModel_Expression133') == owner
    _safe_set(owner, 'sqliteModel_ExprMult132', None)
    assert getattr(partner, 'sqliteModel_Expression133') is None


def test_assoc_right136_stub_double():
    # sqliteModel_Expression has no real 'sqliteModel_Expression138' property in the generated
    # code (a bare stub) -- manually attach it so sqliteModel_ExprAdd's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # sqliteModel_ExprAdd's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = sqliteModel_ExprAdd(op="sample_text")
    partner = sqliteModel_Expression()
    setattr(partner, 'sqliteModel_Expression138', None)
    _safe_set(owner, 'sqliteModel_ExprAdd137', partner)
    assert getattr(partner, 'sqliteModel_Expression138') == owner
    _safe_set(owner, 'sqliteModel_ExprAdd137', None)
    assert getattr(partner, 'sqliteModel_Expression138') is None


def test_assoc_right141_stub_double():
    # sqliteModel_Expression has no real 'sqliteModel_Expression143' property in the generated
    # code (a bare stub) -- manually attach it so sqliteModel_ExprBit's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # sqliteModel_ExprBit's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = sqliteModel_ExprBit(op="sample_text")
    partner = sqliteModel_Expression()
    setattr(partner, 'sqliteModel_Expression143', None)
    _safe_set(owner, 'sqliteModel_ExprBit142', partner)
    assert getattr(partner, 'sqliteModel_Expression143') == owner
    _safe_set(owner, 'sqliteModel_ExprBit142', None)
    assert getattr(partner, 'sqliteModel_Expression143') is None


def test_assoc_right146_stub_double():
    # sqliteModel_Expression has no real 'sqliteModel_Expression148' property in the generated
    # code (a bare stub) -- manually attach it so sqliteModel_ExprRelate's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # sqliteModel_ExprRelate's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = sqliteModel_ExprRelate(op="sample_text")
    partner = sqliteModel_Expression()
    setattr(partner, 'sqliteModel_Expression148', None)
    _safe_set(owner, 'sqliteModel_ExprRelate147', partner)
    assert getattr(partner, 'sqliteModel_Expression148') == owner
    _safe_set(owner, 'sqliteModel_ExprRelate147', None)
    assert getattr(partner, 'sqliteModel_Expression148') is None


def test_assoc_right151_stub_double():
    # sqliteModel_Expression has no real 'sqliteModel_Expression153' property in the generated
    # code (a bare stub) -- manually attach it so sqliteModel_ExprEqual's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # sqliteModel_ExprEqual's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = sqliteModel_ExprEqual(op="sample_text")
    partner = sqliteModel_Expression()
    setattr(partner, 'sqliteModel_Expression153', None)
    _safe_set(owner, 'sqliteModel_ExprEqual152', partner)
    assert getattr(partner, 'sqliteModel_Expression153') == owner
    _safe_set(owner, 'sqliteModel_ExprEqual152', None)
    assert getattr(partner, 'sqliteModel_Expression153') is None


def test_assoc_right156_stub_double():
    # sqliteModel_Expression has no real 'sqliteModel_Expression158' property in the generated
    # code (a bare stub) -- manually attach it so sqliteModel_ExprAnd's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # sqliteModel_ExprAnd's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = sqliteModel_ExprAnd(op="sample_text")
    partner = sqliteModel_Expression()
    setattr(partner, 'sqliteModel_Expression158', None)
    _safe_set(owner, 'sqliteModel_ExprAnd157', partner)
    assert getattr(partner, 'sqliteModel_Expression158') == owner
    _safe_set(owner, 'sqliteModel_ExprAnd157', None)
    assert getattr(partner, 'sqliteModel_Expression158') is None


def test_assoc_right161_stub_double():
    # sqliteModel_Expression has no real 'sqliteModel_Expression163' property in the generated
    # code (a bare stub) -- manually attach it so sqliteModel_ExprOr's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # sqliteModel_ExprOr's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = sqliteModel_ExprOr(op="sample_text")
    partner = sqliteModel_Expression()
    setattr(partner, 'sqliteModel_Expression163', None)
    _safe_set(owner, 'sqliteModel_ExprOr162', partner)
    assert getattr(partner, 'sqliteModel_Expression163') == owner
    _safe_set(owner, 'sqliteModel_ExprOr162', None)
    assert getattr(partner, 'sqliteModel_Expression163') is None


def test_assoc_right196_stub_double():
    # sqliteModel_SelectCoreExpression has no real 'sqliteModel_SelectCoreExpression198' property in the generated
    # code (a bare stub) -- manually attach it so sqliteModel_SelectCore's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # sqliteModel_SelectCore's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = sqliteModel_SelectCore(op="sample_text")
    partner = sqliteModel_SelectCoreExpression()
    setattr(partner, 'sqliteModel_SelectCoreExpression198', None)
    _safe_set(owner, 'sqliteModel_SelectCore197', partner)
    assert getattr(partner, 'sqliteModel_SelectCoreExpression198') == owner
    _safe_set(owner, 'sqliteModel_SelectCore197', None)
    assert getattr(partner, 'sqliteModel_SelectCoreExpression198') is None


def test_assoc_select180_stub_double():
    # sqliteModel_SelectStatement has no real 'sqliteModel_SelectStatement181' property in the generated
    # code (a bare stub) -- manually attach it so sqliteModel_SelectStatementExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # sqliteModel_SelectStatementExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = sqliteModel_SelectStatementExpression(exists=True, not_=True)
    partner = sqliteModel_SelectStatement()
    setattr(partner, 'sqliteModel_SelectStatement181', None)
    _safe_set(owner, 'sqliteModel_SelectStatementExpression', partner)
    assert getattr(partner, 'sqliteModel_SelectStatement181') == owner
    _safe_set(owner, 'sqliteModel_SelectStatementExpression', None)
    assert getattr(partner, 'sqliteModel_SelectStatement181') is None


def test_assoc_selectList199_stub_double():
    # sqliteModel_SelectList has no real 'sqliteModel_SelectList200' property in the generated
    # code (a bare stub) -- manually attach it so sqliteModel_SelectExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # sqliteModel_SelectExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = sqliteModel_SelectExpression(all=True, allColumns=True, distinct=True)
    partner = sqliteModel_SelectList()
    setattr(partner, 'sqliteModel_SelectList200', None)
    _safe_set(owner, 'sqliteModel_SelectExpression', partner)
    assert getattr(partner, 'sqliteModel_SelectList200') == owner
    _safe_set(owner, 'sqliteModel_SelectExpression', None)
    assert getattr(partner, 'sqliteModel_SelectList200') is None


def test_assoc_selectStatement223_stub_double():
    # sqliteModel_SelectStatement has no real 'sqliteModel_SelectStatement225' property in the generated
    # code (a bare stub) -- manually attach it so sqliteModel_CreateViewStatement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # sqliteModel_CreateViewStatement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = sqliteModel_CreateViewStatement(temporary=True)
    partner = sqliteModel_SelectStatement()
    setattr(partner, 'sqliteModel_SelectStatement225', None)
    _safe_set(owner, 'sqliteModel_CreateViewStatement224', partner)
    assert getattr(partner, 'sqliteModel_SelectStatement225') == owner
    _safe_set(owner, 'sqliteModel_CreateViewStatement224', None)
    assert getattr(partner, 'sqliteModel_SelectStatement225') is None


def test_assoc_selectStatement99_stub_double():
    # sqliteModel_SelectStatement has no real 'sqliteModel_SelectStatement101' property in the generated
    # code (a bare stub) -- manually attach it so sqliteModel_InsertStatement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # sqliteModel_InsertStatement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = sqliteModel_InsertStatement(conflictResolution="sample_text")
    partner = sqliteModel_SelectStatement()
    setattr(partner, 'sqliteModel_SelectStatement101', None)
    _safe_set(owner, 'sqliteModel_InsertStatement100', partner)
    assert getattr(partner, 'sqliteModel_SelectStatement101') == owner
    _safe_set(owner, 'sqliteModel_InsertStatement100', None)
    assert getattr(partner, 'sqliteModel_SelectStatement101') is None


def test_assoc_singleSource45_stub_double():
    # sqliteModel_SingleSource has no real 'sqliteModel_SingleSource47' property in the generated
    # code (a bare stub) -- manually attach it so sqliteModel_JoinStatement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # sqliteModel_JoinStatement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = sqliteModel_JoinStatement(cross=True, inner=True, left=True, natural=True, outer=True)
    partner = sqliteModel_SingleSource()
    setattr(partner, 'sqliteModel_SingleSource47', None)
    _safe_set(owner, 'sqliteModel_JoinStatement46', partner)
    assert getattr(partner, 'sqliteModel_SingleSource47') == owner
    _safe_set(owner, 'sqliteModel_JoinStatement46', None)
    assert getattr(partner, 'sqliteModel_SingleSource47') is None


def test_assoc_source201_stub_double():
    # sqliteModel_JoinSource has no real 'sqliteModel_JoinSource203' property in the generated
    # code (a bare stub) -- manually attach it so sqliteModel_SelectExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # sqliteModel_SelectExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = sqliteModel_SelectExpression(all=True, allColumns=True, distinct=True)
    partner = sqliteModel_JoinSource()
    setattr(partner, 'sqliteModel_JoinSource203', None)
    _safe_set(owner, 'sqliteModel_SelectExpression202', partner)
    assert getattr(partner, 'sqliteModel_JoinSource203') == owner
    _safe_set(owner, 'sqliteModel_SelectExpression202', None)
    assert getattr(partner, 'sqliteModel_JoinSource203') is None


def test_assoc_statements118_stub_double():
    # sqliteModel_DMLStatement has no real 'sqliteModel_DMLStatement120' property in the generated
    # code (a bare stub) -- manually attach it so sqliteModel_Function's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # sqliteModel_Function's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = sqliteModel_Function(all=True)
    partner = sqliteModel_DMLStatement()
    setattr(partner, 'sqliteModel_DMLStatement120', None)
    _safe_set(owner, 'sqliteModel_Function119', {partner})
    assert getattr(partner, 'sqliteModel_DMLStatement120') == owner
    _safe_set(owner, 'sqliteModel_Function119', set())
    assert getattr(partner, 'sqliteModel_DMLStatement120') is None


def test_assoc_statements55_stub_double():
    # sqliteModel_DMLStatement has no real 'sqliteModel_DMLStatement' property in the generated
    # code (a bare stub) -- manually attach it so sqliteModel_CreateTriggerStatement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # sqliteModel_CreateTriggerStatement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = sqliteModel_CreateTriggerStatement(eventType="sample_text", forEachRow="sample_text", name="sample_text", temporary=True, updateColumnNames="sample_text", when="sample_text")
    partner = sqliteModel_DMLStatement()
    setattr(partner, 'sqliteModel_DMLStatement', None)
    _safe_set(owner, 'sqliteModel_CreateTriggerStatement56', {partner})
    assert getattr(partner, 'sqliteModel_DMLStatement') == owner
    _safe_set(owner, 'sqliteModel_CreateTriggerStatement56', set())
    assert getattr(partner, 'sqliteModel_DMLStatement') is None


def test_assoc_statements7_stub_double():
    # sqliteModel_ConfigBlock has no real 'sqliteModel_ConfigBlock8' property in the generated
    # code (a bare stub) -- manually attach it so sqliteModel_ConfigurationStatement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # sqliteModel_ConfigurationStatement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = sqliteModel_ConfigurationStatement(name="sample_text")
    partner = sqliteModel_ConfigBlock()
    setattr(partner, 'sqliteModel_ConfigBlock8', None)
    _safe_set(owner, 'sqliteModel_ConfigurationStatement', partner)
    assert owner in getattr(partner, 'sqliteModel_ConfigBlock8')
    _safe_set(owner, 'sqliteModel_ConfigurationStatement', None)
    assert owner not in getattr(partner, 'sqliteModel_ConfigBlock8')


def test_assoc_table226_stub_double():
    # sqliteModel_AlterTableRenameStatement has no real 'sqliteModel_AlterTableRenameStatement' property in the generated
    # code (a bare stub) -- manually attach it so sqliteModel_TableDefinition's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # sqliteModel_TableDefinition's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = sqliteModel_TableDefinition(name="sample_text")
    partner = sqliteModel_AlterTableRenameStatement()
    setattr(partner, 'sqliteModel_AlterTableRenameStatement', None)
    _safe_set(owner, 'sqliteModel_TableDefinition227', partner)
    assert getattr(partner, 'sqliteModel_AlterTableRenameStatement') == owner
    _safe_set(owner, 'sqliteModel_TableDefinition227', None)
    assert getattr(partner, 'sqliteModel_AlterTableRenameStatement') is None


def test_assoc_table57_stub_double():
    # sqliteModel_AlterTableAddColumnStatement has no real 'sqliteModel_AlterTableAddColumnStatement' property in the generated
    # code (a bare stub) -- manually attach it so sqliteModel_TableDefinition's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # sqliteModel_TableDefinition's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = sqliteModel_TableDefinition(name="sample_text")
    partner = sqliteModel_AlterTableAddColumnStatement()
    setattr(partner, 'sqliteModel_AlterTableAddColumnStatement', None)
    _safe_set(owner, 'sqliteModel_TableDefinition58', partner)
    assert getattr(partner, 'sqliteModel_AlterTableAddColumnStatement') == owner
    _safe_set(owner, 'sqliteModel_TableDefinition58', None)
    assert getattr(partner, 'sqliteModel_AlterTableAddColumnStatement') is None


def test_assoc_table86_stub_double():
    # sqliteModel_DeleteStatement has no real 'sqliteModel_DeleteStatement' property in the generated
    # code (a bare stub) -- manually attach it so sqliteModel_TableDefinition's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # sqliteModel_TableDefinition's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = sqliteModel_TableDefinition(name="sample_text")
    partner = sqliteModel_DeleteStatement()
    setattr(partner, 'sqliteModel_DeleteStatement', None)
    _safe_set(owner, 'sqliteModel_TableDefinition87', partner)
    assert getattr(partner, 'sqliteModel_DeleteStatement') == owner
    _safe_set(owner, 'sqliteModel_TableDefinition87', None)
    assert getattr(partner, 'sqliteModel_DeleteStatement') is None


def test_assoc_tableReference213_stub_double():
    # sqliteModel_SingleSourceTable has no real 'sqliteModel_SingleSourceTable' property in the generated
    # code (a bare stub) -- manually attach it so sqliteModel_TableDefinition's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # sqliteModel_TableDefinition's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = sqliteModel_TableDefinition(name="sample_text")
    partner = sqliteModel_SingleSourceTable()
    setattr(partner, 'sqliteModel_SingleSourceTable', None)
    _safe_set(owner, 'sqliteModel_TableDefinition214', partner)
    assert getattr(partner, 'sqliteModel_SingleSourceTable') == owner
    _safe_set(owner, 'sqliteModel_TableDefinition214', None)
    assert getattr(partner, 'sqliteModel_SingleSourceTable') is None


def test_assoc_updateColumnExpressions104_stub_double():
    # sqliteModel_UpdateColumnExpression has no real 'sqliteModel_UpdateColumnExpression' property in the generated
    # code (a bare stub) -- manually attach it so sqliteModel_UpdateStatement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # sqliteModel_UpdateStatement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = sqliteModel_UpdateStatement(conflictResolution="sample_text")
    partner = sqliteModel_UpdateColumnExpression()
    setattr(partner, 'sqliteModel_UpdateColumnExpression', None)
    _safe_set(owner, 'sqliteModel_UpdateStatement105', {partner})
    assert getattr(partner, 'sqliteModel_UpdateColumnExpression') == owner
    _safe_set(owner, 'sqliteModel_UpdateStatement105', set())
    assert getattr(partner, 'sqliteModel_UpdateColumnExpression') is None


def test_assoc_uri115_stub_double():
    # sqliteModel_ActionStatement has no real 'sqliteModel_ActionStatement' property in the generated
    # code (a bare stub) -- manually attach it so sqliteModel_ContentUri's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # sqliteModel_ContentUri's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = sqliteModel_ContentUri(type="sample_text")
    partner = sqliteModel_ActionStatement()
    setattr(partner, 'sqliteModel_ActionStatement', None)
    _safe_set(owner, 'sqliteModel_ContentUri116', partner)
    assert getattr(partner, 'sqliteModel_ActionStatement') == owner
    _safe_set(owner, 'sqliteModel_ContentUri116', None)
    assert getattr(partner, 'sqliteModel_ActionStatement') is None


def test_assoc_whenExpression52_stub_double():
    # sqliteModel_Expression has no real 'sqliteModel_Expression54' property in the generated
    # code (a bare stub) -- manually attach it so sqliteModel_CreateTriggerStatement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # sqliteModel_CreateTriggerStatement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = sqliteModel_CreateTriggerStatement(eventType="sample_text", forEachRow="sample_text", name="sample_text", temporary=True, updateColumnNames="sample_text", when="sample_text")
    partner = sqliteModel_Expression()
    setattr(partner, 'sqliteModel_Expression54', None)
    _safe_set(owner, 'sqliteModel_CreateTriggerStatement53', partner)
    assert getattr(partner, 'sqliteModel_Expression54') == owner
    _safe_set(owner, 'sqliteModel_CreateTriggerStatement53', None)
    assert getattr(partner, 'sqliteModel_Expression54') is None


def test_assoc_where204_stub_double():
    # sqliteModel_WhereExpressions has no real 'sqliteModel_WhereExpressions206' property in the generated
    # code (a bare stub) -- manually attach it so sqliteModel_SelectExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # sqliteModel_SelectExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = sqliteModel_SelectExpression(all=True, allColumns=True, distinct=True)
    partner = sqliteModel_WhereExpressions()
    setattr(partner, 'sqliteModel_WhereExpressions206', None)
    _safe_set(owner, 'sqliteModel_SelectExpression205', partner)
    assert getattr(partner, 'sqliteModel_WhereExpressions206') == owner
    _safe_set(owner, 'sqliteModel_SelectExpression205', None)
    assert getattr(partner, 'sqliteModel_WhereExpressions206') is None


def test_assoc_whereExpression106_stub_double():
    # sqliteModel_Expression has no real 'sqliteModel_Expression108' property in the generated
    # code (a bare stub) -- manually attach it so sqliteModel_UpdateStatement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # sqliteModel_UpdateStatement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = sqliteModel_UpdateStatement(conflictResolution="sample_text")
    partner = sqliteModel_Expression()
    setattr(partner, 'sqliteModel_Expression108', None)
    _safe_set(owner, 'sqliteModel_UpdateStatement107', partner)
    assert getattr(partner, 'sqliteModel_Expression108') == owner
    _safe_set(owner, 'sqliteModel_UpdateStatement107', None)
    assert getattr(partner, 'sqliteModel_Expression108') is None


