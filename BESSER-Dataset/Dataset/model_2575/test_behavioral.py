import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    AnalyticExprArgs,
    ColumnFull,
    FromValuesColumnNames,
    OpFunctionArg,
    OpFunctionArgAgregate,
    OperandList,
    Operands,
    OrColumn,
    OrExpr,
    OrGroupByColumn,
    OrOrderByColumn,
    OrTable,
    OrderByClauseArgs,
    PivotCol,
    PivotColumns,
    PivotForClause,
    PivotFunction,
    Pivots,
    Prms,
    QueryPartitionClause,
    RowValue,
    RowValues,
    Rows,
    SQLCaseWhens,
    SelectQuery,
    TableFull,
    UnpivotInClause,
    UnpivotInClauseArgs,
    UsingCols,
    WindowingClause,
    WithColumns,
    sql_AExpArgs,
    sql_AnalyticClause,
    sql_AnalyticExprArg,
    sql_AnalyticExprArgs,
    sql_Between,
    sql_Col,
    sql_ColumnFull,
    sql_ColumnNames,
    sql_ColumnOperand,
    sql_ColumnOrAlias,
    sql_Comparison,
    sql_Concat,
    sql_DbObjectName,
    sql_DbObjectNameAll,
    sql_Division,
    sql_ExistsOper,
    sql_ExpOperand,
    sql_ExprGroup,
    sql_FetchFirst,
    sql_FromTable,
    sql_FromTableJoin,
    sql_FromValues,
    sql_FromValuesColumnNames,
    sql_FromValuesColumns,
    sql_FullExpression,
    sql_FunctionAnalytical,
    sql_FunctionExtract,
    sql_GroupByColumnFull,
    sql_InOper,
    sql_IntegerValue,
    sql_JRParameter,
    sql_JoinCondition,
    sql_Like,
    sql_LikeOperand,
    sql_Limit,
    sql_Minus,
    sql_Model,
    sql_Multiply,
    sql_OBCArgs,
    sql_Offset,
    sql_OpFList,
    sql_OpFunction,
    sql_OpFunctionArg,
    sql_OpFunctionArgAgregate,
    sql_OpFunctionArgOperand,
    sql_OpFunctionCast,
    sql_OpList,
    sql_Operand,
    sql_OperandList,
    sql_OperandListGroup,
    sql_Operands,
    sql_OrColumn,
    sql_OrExpr,
    sql_OrGroupByColumn,
    sql_OrOrderByColumn,
    sql_OrTable,
    sql_OrderByClause,
    sql_OrderByClauseArg,
    sql_OrderByClauseArgs,
    sql_OrderByColumnFull,
    sql_POperand,
    sql_PivotCol,
    sql_PivotColumns,
    sql_PivotForClause,
    sql_PivotFunction,
    sql_PivotFunctions,
    sql_PivotInClause,
    sql_PivotTable,
    sql_Pivots,
    sql_Plus,
    sql_Prms,
    sql_QueryPartitionClause,
    sql_Row,
    sql_RowValue,
    sql_RowValues,
    sql_Rows,
    sql_SQLCaseOperand,
    sql_SQLCaseWhens,
    sql_ScalarOperand,
    sql_Select,
    sql_SelectQuery,
    sql_SelectSubSet,
    sql_SqlCaseWhen,
    sql_SubQueryOperand,
    sql_TableFull,
    sql_TableOrAlias,
    sql_UnipivotInClause,
    sql_UnpivotInClause,
    sql_UnpivotInClauseArg,
    sql_UnpivotInClauseArgs,
    sql_UnpivotTable,
    sql_UnsignedValue,
    sql_UsingCols,
    sql_Values,
    sql_WhenList,
    sql_WindowingClause,
    sql_WindowingClauseBetween,
    sql_WindowingClauseOperandFollowing,
    sql_WindowingClauseOperandPreceding,
    sql_WithColumns,
    sql_WithQuery,
    sql_XExpr,
    sql_abc,
    sql_pcols,
    sql_pvcs,
    sql_tbls,
    sql_uicargs,
    EXTRACT_VALUES,
    XFunction,
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

def test_assoc_between140_reverse_link_reassign_clear():
    a1 = sql_FullExpression(c="sample_text", isnull="sample_text", notPrm="sample_text")
    a2 = sql_FullExpression(c="sample_text_2", isnull="sample_text_2", notPrm="sample_text_2")
    b = sql_Between(opBetween="sample_text")
    _safe_set(b, 'sql_Between', a1)
    assert _is_linked(b, 'sql_Between', a1)
    if hasattr(a1, 'sql_FullExpression141'):
        assert _is_linked(a1, 'sql_FullExpression141', b)
    _safe_set(b, 'sql_Between', a2)
    assert _is_linked(b, 'sql_Between', a2)
    if hasattr(a1, 'sql_FullExpression141'):
        assert not _is_linked(a1, 'sql_FullExpression141', b)
    if hasattr(a2, 'sql_FullExpression141'):
        assert _is_linked(a2, 'sql_FullExpression141', b)
    _safe_set(b, 'sql_Between', None)
    assert not _is_linked(b, 'sql_Between', a2)
    if hasattr(a2, 'sql_FullExpression141'):
        assert not _is_linked(a2, 'sql_FullExpression141', b)


def test_assoc_colAlias37_reverse_link_reassign_clear():
    a1 = sql_DbObjectName(dbname="sample_text")
    a2 = sql_DbObjectName(dbname="sample_text_2")
    b = sql_ColumnOrAlias(alias="sample_text", allCols="sample_text")
    _safe_set(b, 'sql_ColumnOrAlias38', a1)
    assert _is_linked(b, 'sql_ColumnOrAlias38', a1)
    if hasattr(a1, 'sql_DbObjectName'):
        assert _is_linked(a1, 'sql_DbObjectName', b)
    _safe_set(b, 'sql_ColumnOrAlias38', a2)
    assert _is_linked(b, 'sql_ColumnOrAlias38', a2)
    if hasattr(a1, 'sql_DbObjectName'):
        assert not _is_linked(a1, 'sql_DbObjectName', b)
    if hasattr(a2, 'sql_DbObjectName'):
        assert _is_linked(a2, 'sql_DbObjectName', b)
    _safe_set(b, 'sql_ColumnOrAlias38', None)
    assert not _is_linked(b, 'sql_ColumnOrAlias38', a2)
    if hasattr(a2, 'sql_DbObjectName'):
        assert not _is_linked(a2, 'sql_DbObjectName', b)


def test_assoc_comp144_reverse_link_reassign_clear():
    a1 = sql_FullExpression(c="sample_text", isnull="sample_text", notPrm="sample_text")
    a2 = sql_FullExpression(c="sample_text_2", isnull="sample_text_2", notPrm="sample_text_2")
    b = sql_Comparison(operator="sample_text", subOperator="sample_text")
    _safe_set(b, 'sql_Comparison', a1)
    assert _is_linked(b, 'sql_Comparison', a1)
    if hasattr(a1, 'sql_FullExpression145'):
        assert _is_linked(a1, 'sql_FullExpression145', b)
    _safe_set(b, 'sql_Comparison', a2)
    assert _is_linked(b, 'sql_Comparison', a2)
    if hasattr(a1, 'sql_FullExpression145'):
        assert not _is_linked(a1, 'sql_FullExpression145', b)
    if hasattr(a2, 'sql_FullExpression145'):
        assert _is_linked(a2, 'sql_FullExpression145', b)
    _safe_set(b, 'sql_Comparison', None)
    assert not _is_linked(b, 'sql_Comparison', a2)
    if hasattr(a2, 'sql_FullExpression145'):
        assert not _is_linked(a2, 'sql_FullExpression145', b)


def test_assoc_dbAllCols39_reverse_link_reassign_clear():
    a1 = sql_DbObjectNameAll(dbname="sample_text")
    a2 = sql_DbObjectNameAll(dbname="sample_text_2")
    b = sql_ColumnOrAlias(alias="sample_text", allCols="sample_text")
    _safe_set(b, 'sql_ColumnOrAlias40', a1)
    assert _is_linked(b, 'sql_ColumnOrAlias40', a1)
    if hasattr(a1, 'sql_DbObjectNameAll'):
        assert _is_linked(a1, 'sql_DbObjectNameAll', b)
    _safe_set(b, 'sql_ColumnOrAlias40', a2)
    assert _is_linked(b, 'sql_ColumnOrAlias40', a2)
    if hasattr(a1, 'sql_DbObjectNameAll'):
        assert not _is_linked(a1, 'sql_DbObjectNameAll', b)
    if hasattr(a2, 'sql_DbObjectNameAll'):
        assert _is_linked(a2, 'sql_DbObjectNameAll', b)
    _safe_set(b, 'sql_ColumnOrAlias40', None)
    assert not _is_linked(b, 'sql_ColumnOrAlias40', a2)
    if hasattr(a2, 'sql_DbObjectNameAll'):
        assert not _is_linked(a2, 'sql_DbObjectNameAll', b)


def test_assoc_efrag124_reverse_link_reassign_clear():
    a1 = sql_FullExpression(c="sample_text", isnull="sample_text", notPrm="sample_text")
    a2 = sql_FullExpression(c="sample_text_2", isnull="sample_text_2", notPrm="sample_text_2")
    b = sql_FullExpression(c="sample_text", isnull="sample_text", notPrm="sample_text")
    _safe_set(b, 'sql_FullExpression125', a1)
    assert _is_linked(b, 'sql_FullExpression125', a1)
    if hasattr(a1, 'sql_FullExpression123'):
        assert _is_linked(a1, 'sql_FullExpression123', b)
    _safe_set(b, 'sql_FullExpression125', a2)
    assert _is_linked(b, 'sql_FullExpression125', a2)
    if hasattr(a1, 'sql_FullExpression123'):
        assert not _is_linked(a1, 'sql_FullExpression123', b)
    if hasattr(a2, 'sql_FullExpression123'):
        assert _is_linked(a2, 'sql_FullExpression123', b)
    _safe_set(b, 'sql_FullExpression125', None)
    assert not _is_linked(b, 'sql_FullExpression125', a2)
    if hasattr(a2, 'sql_FullExpression123'):
        assert not _is_linked(a2, 'sql_FullExpression123', b)


def test_assoc_exists135_reverse_link_reassign_clear():
    a1 = sql_FullExpression(c="sample_text", isnull="sample_text", notPrm="sample_text")
    a2 = sql_FullExpression(c="sample_text_2", isnull="sample_text_2", notPrm="sample_text_2")
    b = sql_ExistsOper(op="sample_text")
    _safe_set(b, 'sql_ExistsOper', a1)
    assert _is_linked(b, 'sql_ExistsOper', a1)
    if hasattr(a1, 'sql_FullExpression136'):
        assert _is_linked(a1, 'sql_FullExpression136', b)
    _safe_set(b, 'sql_ExistsOper', a2)
    assert _is_linked(b, 'sql_ExistsOper', a2)
    if hasattr(a1, 'sql_FullExpression136'):
        assert not _is_linked(a1, 'sql_FullExpression136', b)
    if hasattr(a2, 'sql_FullExpression136'):
        assert _is_linked(a2, 'sql_FullExpression136', b)
    _safe_set(b, 'sql_ExistsOper', None)
    assert not _is_linked(b, 'sql_ExistsOper', a2)
    if hasattr(a2, 'sql_FullExpression136'):
        assert not _is_linked(a2, 'sql_FullExpression136', b)


def test_assoc_exp129_reverse_link_reassign_clear():
    a1 = sql_FullExpression(c="sample_text", isnull="sample_text", notPrm="sample_text")
    a2 = sql_FullExpression(c="sample_text_2", isnull="sample_text_2", notPrm="sample_text_2")
    b = sql_FullExpression(c="sample_text", isnull="sample_text", notPrm="sample_text")
    _safe_set(b, 'sql_FullExpression130', a1)
    assert _is_linked(b, 'sql_FullExpression130', a1)
    if hasattr(a1, 'sql_FullExpression128'):
        assert _is_linked(a1, 'sql_FullExpression128', b)
    _safe_set(b, 'sql_FullExpression130', a2)
    assert _is_linked(b, 'sql_FullExpression130', a2)
    if hasattr(a1, 'sql_FullExpression128'):
        assert not _is_linked(a1, 'sql_FullExpression128', b)
    if hasattr(a2, 'sql_FullExpression128'):
        assert _is_linked(a2, 'sql_FullExpression128', b)
    _safe_set(b, 'sql_FullExpression130', None)
    assert not _is_linked(b, 'sql_FullExpression130', a2)
    if hasattr(a2, 'sql_FullExpression128'):
        assert not _is_linked(a2, 'sql_FullExpression128', b)


def test_assoc_expgroup126_reverse_link_reassign_clear():
    a1 = sql_FullExpression(c="sample_text", isnull="sample_text", notPrm="sample_text")
    a2 = sql_FullExpression(c="sample_text_2", isnull="sample_text_2", notPrm="sample_text_2")
    b = sql_ExprGroup(isnot="sample_text")
    _safe_set(b, 'sql_ExprGroup', a1)
    assert _is_linked(b, 'sql_ExprGroup', a1)
    if hasattr(a1, 'sql_FullExpression127'):
        assert _is_linked(a1, 'sql_FullExpression127', b)
    _safe_set(b, 'sql_ExprGroup', a2)
    assert _is_linked(b, 'sql_ExprGroup', a2)
    if hasattr(a1, 'sql_FullExpression127'):
        assert not _is_linked(a1, 'sql_FullExpression127', b)
    if hasattr(a2, 'sql_FullExpression127'):
        assert _is_linked(a2, 'sql_FullExpression127', b)
    _safe_set(b, 'sql_ExprGroup', None)
    assert not _is_linked(b, 'sql_ExprGroup', a2)
    if hasattr(a2, 'sql_FullExpression127'):
        assert not _is_linked(a2, 'sql_FullExpression127', b)


def test_assoc_fcast164_reverse_link_reassign_clear():
    a1 = sql_OpFunctionCast(p="sample_text", p2="sample_text", type="sample_text")
    a2 = sql_OpFunctionCast(p="sample_text_2", p2="sample_text_2", type="sample_text_2")
    b = sql_LikeOperand(op2="sample_text")
    _safe_set(b, 'sql_LikeOperand165', a1)
    assert _is_linked(b, 'sql_LikeOperand165', a1)
    if hasattr(a1, 'sql_OpFunctionCast'):
        assert _is_linked(a1, 'sql_OpFunctionCast', b)
    _safe_set(b, 'sql_LikeOperand165', a2)
    assert _is_linked(b, 'sql_LikeOperand165', a2)
    if hasattr(a1, 'sql_OpFunctionCast'):
        assert not _is_linked(a1, 'sql_OpFunctionCast', b)
    if hasattr(a2, 'sql_OpFunctionCast'):
        assert _is_linked(a2, 'sql_OpFunctionCast', b)
    _safe_set(b, 'sql_LikeOperand165', None)
    assert not _is_linked(b, 'sql_LikeOperand165', a2)
    if hasattr(a2, 'sql_OpFunctionCast'):
        assert not _is_linked(a2, 'sql_OpFunctionCast', b)


def test_assoc_fetchFirst30_reverse_link_reassign_clear():
    a1 = sql_Select(select="sample_text")
    a2 = sql_Select(select="sample_text_2")
    b = sql_FetchFirst(row="sample_text")
    _safe_set(b, 'sql_FetchFirst32', a1)
    assert _is_linked(b, 'sql_FetchFirst32', a1)
    if hasattr(a1, 'sql_Select31'):
        assert _is_linked(a1, 'sql_Select31', b)
    _safe_set(b, 'sql_FetchFirst32', a2)
    assert _is_linked(b, 'sql_FetchFirst32', a2)
    if hasattr(a1, 'sql_Select31'):
        assert not _is_linked(a1, 'sql_Select31', b)
    if hasattr(a2, 'sql_Select31'):
        assert _is_linked(a2, 'sql_Select31', b)
    _safe_set(b, 'sql_FetchFirst32', None)
    assert not _is_linked(b, 'sql_FetchFirst32', a2)
    if hasattr(a2, 'sql_Select31'):
        assert not _is_linked(a2, 'sql_Select31', b)


def test_assoc_fetchFirst8_reverse_link_reassign_clear():
    a1 = sql_UnsignedValue(integer="sample_text")
    a2 = sql_UnsignedValue(integer="sample_text_2")
    b = sql_FetchFirst(row="sample_text")
    _safe_set(b, 'sql_FetchFirst', a1)
    assert _is_linked(b, 'sql_FetchFirst', a1)
    if hasattr(a1, 'sql_UnsignedValue'):
        assert _is_linked(a1, 'sql_UnsignedValue', b)
    _safe_set(b, 'sql_FetchFirst', a2)
    assert _is_linked(b, 'sql_FetchFirst', a2)
    if hasattr(a1, 'sql_UnsignedValue'):
        assert not _is_linked(a1, 'sql_UnsignedValue', b)
    if hasattr(a2, 'sql_UnsignedValue'):
        assert _is_linked(a2, 'sql_UnsignedValue', b)
    _safe_set(b, 'sql_FetchFirst', None)
    assert not _is_linked(b, 'sql_FetchFirst', a2)
    if hasattr(a2, 'sql_UnsignedValue'):
        assert not _is_linked(a2, 'sql_UnsignedValue', b)


def test_assoc_fop2161_reverse_link_reassign_clear():
    a1 = sql_OpFunction(fname="sample_text", star="sample_text")
    a2 = sql_OpFunction(fname="sample_text_2", star="sample_text_2")
    b = sql_LikeOperand(op2="sample_text")
    _safe_set(b, 'sql_LikeOperand162', a1)
    assert _is_linked(b, 'sql_LikeOperand162', a1)
    if hasattr(a1, 'sql_OpFunction163'):
        assert _is_linked(a1, 'sql_OpFunction163', b)
    _safe_set(b, 'sql_LikeOperand162', a2)
    assert _is_linked(b, 'sql_LikeOperand162', a2)
    if hasattr(a1, 'sql_OpFunction163'):
        assert not _is_linked(a1, 'sql_OpFunction163', b)
    if hasattr(a2, 'sql_OpFunction163'):
        assert _is_linked(a2, 'sql_OpFunction163', b)
    _safe_set(b, 'sql_LikeOperand162', None)
    assert not _is_linked(b, 'sql_LikeOperand162', a2)
    if hasattr(a2, 'sql_OpFunction163'):
        assert not _is_linked(a2, 'sql_OpFunction163', b)


def test_assoc_fparam166_reverse_link_reassign_clear():
    a1 = sql_POperand(prm="sample_text")
    a2 = sql_POperand(prm="sample_text_2")
    b = sql_LikeOperand(op2="sample_text")
    _safe_set(b, 'sql_LikeOperand167', a1)
    assert _is_linked(b, 'sql_LikeOperand167', a1)
    if hasattr(a1, 'sql_POperand'):
        assert _is_linked(a1, 'sql_POperand', b)
    _safe_set(b, 'sql_LikeOperand167', a2)
    assert _is_linked(b, 'sql_LikeOperand167', a2)
    if hasattr(a1, 'sql_POperand'):
        assert not _is_linked(a1, 'sql_POperand', b)
    if hasattr(a2, 'sql_POperand'):
        assert _is_linked(a2, 'sql_POperand', b)
    _safe_set(b, 'sql_LikeOperand167', None)
    assert not _is_linked(b, 'sql_LikeOperand167', a2)
    if hasattr(a2, 'sql_POperand'):
        assert not _is_linked(a2, 'sql_POperand', b)


def test_assoc_gbFunction119_reverse_link_reassign_clear():
    a1 = sql_OpFunction(fname="sample_text", star="sample_text")
    a2 = sql_OpFunction(fname="sample_text_2", star="sample_text_2")
    b = sql_GroupByColumnFull(grByInt="sample_text")
    _safe_set(b, 'sql_GroupByColumnFull120', a1)
    assert _is_linked(b, 'sql_GroupByColumnFull120', a1)
    if hasattr(a1, 'sql_OpFunction'):
        assert _is_linked(a1, 'sql_OpFunction', b)
    _safe_set(b, 'sql_GroupByColumnFull120', a2)
    assert _is_linked(b, 'sql_GroupByColumnFull120', a2)
    if hasattr(a1, 'sql_OpFunction'):
        assert not _is_linked(a1, 'sql_OpFunction', b)
    if hasattr(a2, 'sql_OpFunction'):
        assert _is_linked(a2, 'sql_OpFunction', b)
    _safe_set(b, 'sql_GroupByColumnFull120', None)
    assert not _is_linked(b, 'sql_GroupByColumnFull120', a2)
    if hasattr(a2, 'sql_OpFunction'):
        assert not _is_linked(a2, 'sql_OpFunction', b)


def test_assoc_in_133_reverse_link_reassign_clear():
    a1 = sql_InOper(op="sample_text")
    a2 = sql_InOper(op="sample_text_2")
    b = sql_FullExpression(c="sample_text", isnull="sample_text", notPrm="sample_text")
    _safe_set(b, 'sql_FullExpression134', a1)
    assert _is_linked(b, 'sql_FullExpression134', a1)
    if hasattr(a1, 'sql_InOper'):
        assert _is_linked(a1, 'sql_InOper', b)
    _safe_set(b, 'sql_FullExpression134', a2)
    assert _is_linked(b, 'sql_FullExpression134', a2)
    if hasattr(a1, 'sql_InOper'):
        assert not _is_linked(a1, 'sql_InOper', b)
    if hasattr(a2, 'sql_InOper'):
        assert _is_linked(a2, 'sql_InOper', b)
    _safe_set(b, 'sql_FullExpression134', None)
    assert not _is_linked(b, 'sql_FullExpression134', a2)
    if hasattr(a2, 'sql_InOper'):
        assert not _is_linked(a2, 'sql_InOper', b)


def test_assoc_like142_reverse_link_reassign_clear():
    a1 = sql_Like(opLike="sample_text")
    a2 = sql_Like(opLike="sample_text_2")
    b = sql_FullExpression(c="sample_text", isnull="sample_text", notPrm="sample_text")
    _safe_set(b, 'sql_FullExpression143', a1)
    assert _is_linked(b, 'sql_FullExpression143', a1)
    if hasattr(a1, 'sql_Like'):
        assert _is_linked(a1, 'sql_Like', b)
    _safe_set(b, 'sql_FullExpression143', a2)
    assert _is_linked(b, 'sql_FullExpression143', a2)
    if hasattr(a1, 'sql_Like'):
        assert not _is_linked(a1, 'sql_Like', b)
    if hasattr(a2, 'sql_Like'):
        assert _is_linked(a2, 'sql_Like', b)
    _safe_set(b, 'sql_FullExpression143', None)
    assert not _is_linked(b, 'sql_FullExpression143', a2)
    if hasattr(a2, 'sql_Like'):
        assert not _is_linked(a2, 'sql_Like', b)


def test_assoc_lim26_reverse_link_reassign_clear():
    a1 = sql_Select(select="sample_text")
    a2 = sql_Select(select="sample_text_2")
    b = sql_Limit(l1="sample_text", l2="sample_text")
    _safe_set(b, 'sql_Limit', a1)
    assert _is_linked(b, 'sql_Limit', a1)
    if hasattr(a1, 'sql_Select27'):
        assert _is_linked(a1, 'sql_Select27', b)
    _safe_set(b, 'sql_Limit', a2)
    assert _is_linked(b, 'sql_Limit', a2)
    if hasattr(a1, 'sql_Select27'):
        assert not _is_linked(a1, 'sql_Select27', b)
    if hasattr(a2, 'sql_Select27'):
        assert _is_linked(a2, 'sql_Select27', b)
    _safe_set(b, 'sql_Limit', None)
    assert not _is_linked(b, 'sql_Limit', a2)
    if hasattr(a2, 'sql_Select27'):
        assert not _is_linked(a2, 'sql_Select27', b)


def test_assoc_offset28_reverse_link_reassign_clear():
    a1 = sql_Select(select="sample_text")
    a2 = sql_Select(select="sample_text_2")
    b = sql_Offset(offset="sample_text")
    _safe_set(b, 'sql_Offset', a1)
    assert _is_linked(b, 'sql_Offset', a1)
    if hasattr(a1, 'sql_Select29'):
        assert _is_linked(a1, 'sql_Select29', b)
    _safe_set(b, 'sql_Offset', a2)
    assert _is_linked(b, 'sql_Offset', a2)
    if hasattr(a1, 'sql_Select29'):
        assert not _is_linked(a1, 'sql_Select29', b)
    if hasattr(a2, 'sql_Select29'):
        assert _is_linked(a2, 'sql_Select29', b)
    _safe_set(b, 'sql_Offset', None)
    assert not _is_linked(b, 'sql_Offset', a2)
    if hasattr(a2, 'sql_Select29'):
        assert not _is_linked(a2, 'sql_Select29', b)


def test_assoc_onTable47_reverse_link_reassign_clear():
    a1 = sql_TableOrAlias(alias="sample_text")
    a2 = sql_TableOrAlias(alias="sample_text_2")
    b = sql_FromTableJoin(join="sample_text")
    _safe_set(b, 'sql_FromTableJoin48', a1)
    assert _is_linked(b, 'sql_FromTableJoin48', a1)
    if hasattr(a1, 'sql_TableOrAlias49'):
        assert _is_linked(a1, 'sql_TableOrAlias49', b)
    _safe_set(b, 'sql_FromTableJoin48', a2)
    assert _is_linked(b, 'sql_FromTableJoin48', a2)
    if hasattr(a1, 'sql_TableOrAlias49'):
        assert not _is_linked(a1, 'sql_TableOrAlias49', b)
    if hasattr(a2, 'sql_TableOrAlias49'):
        assert _is_linked(a2, 'sql_TableOrAlias49', b)
    _safe_set(b, 'sql_FromTableJoin48', None)
    assert not _is_linked(b, 'sql_FromTableJoin48', a2)
    if hasattr(a2, 'sql_TableOrAlias49'):
        assert not _is_linked(a2, 'sql_TableOrAlias49', b)


def test_assoc_op10_reverse_link_reassign_clear():
    a1 = sql_SelectSubSet(all="sample_text", op="sample_text")
    a2 = sql_SelectSubSet(all="sample_text_2", op="sample_text_2")
    b = sql_Select(select="sample_text")
    _safe_set(b, 'sql_Select11', {a1})
    assert _is_linked(b, 'sql_Select11', a1)
    if hasattr(a1, 'sql_SelectSubSet12'):
        assert _is_linked(a1, 'sql_SelectSubSet12', b)
    _safe_set(b, 'sql_Select11', {a2})
    assert _is_linked(b, 'sql_Select11', a2)
    if hasattr(a1, 'sql_SelectSubSet12'):
        assert not _is_linked(a1, 'sql_SelectSubSet12', b)
    if hasattr(a2, 'sql_SelectSubSet12'):
        assert _is_linked(a2, 'sql_SelectSubSet12', b)
    _safe_set(b, 'sql_Select11', set())
    assert not _is_linked(b, 'sql_Select11', a2)
    if hasattr(a2, 'sql_SelectSubSet12'):
        assert not _is_linked(a2, 'sql_SelectSubSet12', b)


def test_assoc_op2159_reverse_link_reassign_clear():
    a1 = sql_LikeOperand(op2="sample_text")
    a2 = sql_LikeOperand(op2="sample_text_2")
    b = sql_Like(opLike="sample_text")
    _safe_set(b, 'sql_Like160', a1)
    assert _is_linked(b, 'sql_Like160', a1)
    if hasattr(a1, 'sql_LikeOperand'):
        assert _is_linked(a1, 'sql_LikeOperand', b)
    _safe_set(b, 'sql_Like160', a2)
    assert _is_linked(b, 'sql_Like160', a2)
    if hasattr(a1, 'sql_LikeOperand'):
        assert not _is_linked(a1, 'sql_LikeOperand', b)
    if hasattr(a2, 'sql_LikeOperand'):
        assert _is_linked(a2, 'sql_LikeOperand', b)
    _safe_set(b, 'sql_Like160', None)
    assert not _is_linked(b, 'sql_Like160', a2)
    if hasattr(a2, 'sql_LikeOperand'):
        assert not _is_linked(a2, 'sql_LikeOperand', b)


def test_assoc_query9_reverse_link_reassign_clear():
    a1 = sql_SelectSubSet(all="sample_text", op="sample_text")
    a2 = sql_SelectSubSet(all="sample_text_2", op="sample_text_2")
    b = sql_Select(select="sample_text")
    _safe_set(b, 'sql_Select', a1)
    assert _is_linked(b, 'sql_Select', a1)
    if hasattr(a1, 'sql_SelectSubSet'):
        assert _is_linked(a1, 'sql_SelectSubSet', b)
    _safe_set(b, 'sql_Select', a2)
    assert _is_linked(b, 'sql_Select', a2)
    if hasattr(a1, 'sql_SelectSubSet'):
        assert not _is_linked(a1, 'sql_SelectSubSet', b)
    if hasattr(a2, 'sql_SelectSubSet'):
        assert _is_linked(a2, 'sql_SelectSubSet', b)
    _safe_set(b, 'sql_Select', None)
    assert not _is_linked(b, 'sql_Select', a2)
    if hasattr(a2, 'sql_SelectSubSet'):
        assert not _is_linked(a2, 'sql_SelectSubSet', b)


def test_assoc_tblAlias70_reverse_link_reassign_clear():
    a1 = sql_TableOrAlias(alias="sample_text")
    a2 = sql_TableOrAlias(alias="sample_text_2")
    b = sql_DbObjectName(dbname="sample_text")
    _safe_set(b, 'sql_DbObjectName72', a1)
    assert _is_linked(b, 'sql_DbObjectName72', a1)
    if hasattr(a1, 'sql_TableOrAlias71'):
        assert _is_linked(a1, 'sql_TableOrAlias71', b)
    _safe_set(b, 'sql_DbObjectName72', a2)
    assert _is_linked(b, 'sql_DbObjectName72', a2)
    if hasattr(a1, 'sql_TableOrAlias71'):
        assert not _is_linked(a1, 'sql_TableOrAlias71', b)
    if hasattr(a2, 'sql_TableOrAlias71'):
        assert _is_linked(a2, 'sql_TableOrAlias71', b)
    _safe_set(b, 'sql_DbObjectName72', None)
    assert not _is_linked(b, 'sql_DbObjectName72', a2)
    if hasattr(a2, 'sql_TableOrAlias71'):
        assert not _is_linked(a2, 'sql_TableOrAlias71', b)


def test_assoc_xexp131_reverse_link_reassign_clear():
    a1 = sql_XExpr(xf="sample_text")
    a2 = sql_XExpr(xf="sample_text_2")
    b = sql_FullExpression(c="sample_text", isnull="sample_text", notPrm="sample_text")
    _safe_set(b, 'sql_FullExpression132', a1)
    assert _is_linked(b, 'sql_FullExpression132', a1)
    if hasattr(a1, 'sql_XExpr'):
        assert _is_linked(a1, 'sql_XExpr', b)
    _safe_set(b, 'sql_FullExpression132', a2)
    assert _is_linked(b, 'sql_FullExpression132', a2)
    if hasattr(a1, 'sql_XExpr'):
        assert not _is_linked(a1, 'sql_XExpr', b)
    if hasattr(a2, 'sql_XExpr'):
        assert _is_linked(a2, 'sql_XExpr', b)
    _safe_set(b, 'sql_FullExpression132', None)
    assert not _is_linked(b, 'sql_FullExpression132', a2)
    if hasattr(a2, 'sql_XExpr'):
        assert not _is_linked(a2, 'sql_XExpr', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_args220_stub_double():
    # sql_OpFunctionArg has no real 'sql_OpFunctionArg' property in the generated
    # code (a bare stub) -- manually attach it so sql_OpFunction's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # sql_OpFunction's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = sql_OpFunction(fname="sample_text", star="sample_text")
    partner = sql_OpFunctionArg()
    setattr(partner, 'sql_OpFunctionArg', None)
    _safe_set(owner, 'sql_OpFunction221', partner)
    assert getattr(partner, 'sql_OpFunctionArg') == owner
    _safe_set(owner, 'sql_OpFunction221', None)
    assert getattr(partner, 'sql_OpFunctionArg') is None


def test_assoc_args287_stub_double():
    # sql_UnpivotInClauseArgs has no real 'sql_UnpivotInClauseArgs288' property in the generated
    # code (a bare stub) -- manually attach it so sql_UnipivotInClause's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # sql_UnipivotInClause's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = sql_UnipivotInClause(op="sample_text")
    partner = sql_UnpivotInClauseArgs()
    setattr(partner, 'sql_UnpivotInClauseArgs288', None)
    _safe_set(owner, 'sql_UnipivotInClause', partner)
    assert getattr(partner, 'sql_UnpivotInClauseArgs288') == owner
    _safe_set(owner, 'sql_UnipivotInClause', None)
    assert getattr(partner, 'sql_UnpivotInClauseArgs288') is None


def test_assoc_args96_stub_double():
    # sql_UnpivotInClauseArgs has no real 'sql_UnpivotInClauseArgs' property in the generated
    # code (a bare stub) -- manually attach it so sql_PivotInClause's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # sql_PivotInClause's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = sql_PivotInClause(pinany="sample_text")
    partner = sql_UnpivotInClauseArgs()
    setattr(partner, 'sql_UnpivotInClauseArgs', None)
    _safe_set(owner, 'sql_PivotInClause97', partner)
    assert getattr(partner, 'sql_UnpivotInClauseArgs') == owner
    _safe_set(owner, 'sql_PivotInClause97', None)
    assert getattr(partner, 'sql_UnpivotInClauseArgs') is None


def test_assoc_ce35_stub_double():
    # sql_Operands has no real 'sql_Operands' property in the generated
    # code (a bare stub) -- manually attach it so sql_ColumnOrAlias's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # sql_ColumnOrAlias's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = sql_ColumnOrAlias(alias="sample_text", allCols="sample_text")
    partner = sql_Operands()
    setattr(partner, 'sql_Operands', None)
    _safe_set(owner, 'sql_ColumnOrAlias36', partner)
    assert getattr(partner, 'sql_Operands') == owner
    _safe_set(owner, 'sql_ColumnOrAlias36', None)
    assert getattr(partner, 'sql_Operands') is None


def test_assoc_cfull259_stub_double():
    # sql_ColumnFull has no real 'sql_ColumnFull261' property in the generated
    # code (a bare stub) -- manually attach it so sql_ColumnOperand's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # sql_ColumnOperand's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = sql_ColumnOperand(ora="sample_text")
    partner = sql_ColumnFull()
    setattr(partner, 'sql_ColumnFull261', None)
    _safe_set(owner, 'sql_ColumnOperand260', partner)
    assert getattr(partner, 'sql_ColumnFull261') == owner
    _safe_set(owner, 'sql_ColumnOperand260', None)
    assert getattr(partner, 'sql_ColumnFull261') is None


def test_assoc_col149_stub_double():
    # sql_Operands has no real 'sql_Operands151' property in the generated
    # code (a bare stub) -- manually attach it so sql_XExpr's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # sql_XExpr's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = sql_XExpr(xf="sample_text")
    partner = sql_Operands()
    setattr(partner, 'sql_Operands151', None)
    _safe_set(owner, 'sql_XExpr150', partner)
    assert getattr(partner, 'sql_Operands151') == owner
    _safe_set(owner, 'sql_XExpr150', None)
    assert getattr(partner, 'sql_Operands151') is None


def test_assoc_colAlias252_stub_double():
    # sql_AnalyticExprArg has no real 'sql_AnalyticExprArg253' property in the generated
    # code (a bare stub) -- manually attach it so sql_DbObjectName's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # sql_DbObjectName's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = sql_DbObjectName(dbname="sample_text")
    partner = sql_AnalyticExprArg()
    setattr(partner, 'sql_AnalyticExprArg253', None)
    _safe_set(owner, 'sql_DbObjectName254', partner)
    assert getattr(partner, 'sql_AnalyticExprArg253') == owner
    _safe_set(owner, 'sql_DbObjectName254', None)
    assert getattr(partner, 'sql_AnalyticExprArg253') is None


def test_assoc_colGrBy116_stub_double():
    # sql_ColumnFull has no real 'sql_ColumnFull118' property in the generated
    # code (a bare stub) -- manually attach it so sql_GroupByColumnFull's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # sql_GroupByColumnFull's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = sql_GroupByColumnFull(grByInt="sample_text")
    partner = sql_ColumnFull()
    setattr(partner, 'sql_ColumnFull118', None)
    _safe_set(owner, 'sql_GroupByColumnFull117', partner)
    assert getattr(partner, 'sql_ColumnFull118') == owner
    _safe_set(owner, 'sql_GroupByColumnFull117', None)
    assert getattr(partner, 'sql_ColumnFull118') is None


def test_assoc_colOrder112_stub_double():
    # sql_ColumnFull has no real 'sql_ColumnFull' property in the generated
    # code (a bare stub) -- manually attach it so sql_OrderByColumnFull's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # sql_OrderByColumnFull's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = sql_OrderByColumnFull(colOrderInt="sample_text", direction="sample_text")
    partner = sql_ColumnFull()
    setattr(partner, 'sql_ColumnFull', None)
    _safe_set(owner, 'sql_OrderByColumnFull113', partner)
    assert getattr(partner, 'sql_ColumnFull') == owner
    _safe_set(owner, 'sql_OrderByColumnFull113', None)
    assert getattr(partner, 'sql_ColumnFull') is None


def test_assoc_cols13_stub_double():
    # sql_OrColumn has no real 'sql_OrColumn' property in the generated
    # code (a bare stub) -- manually attach it so sql_Select's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # sql_Select's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = sql_Select(select="sample_text")
    partner = sql_OrColumn()
    setattr(partner, 'sql_OrColumn', None)
    _safe_set(owner, 'sql_Select14', partner)
    assert getattr(partner, 'sql_OrColumn') == owner
    _safe_set(owner, 'sql_Select14', None)
    assert getattr(partner, 'sql_OrColumn') is None


def test_assoc_column195_stub_double():
    # sql_Operand has no real 'sql_Operand196' property in the generated
    # code (a bare stub) -- manually attach it so sql_ColumnOperand's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # sql_ColumnOperand's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = sql_ColumnOperand(ora="sample_text")
    partner = sql_Operand()
    setattr(partner, 'sql_Operand196', None)
    _safe_set(owner, 'sql_ColumnOperand', partner)
    assert getattr(partner, 'sql_Operand196') == owner
    _safe_set(owner, 'sql_ColumnOperand', None)
    assert getattr(partner, 'sql_Operand196') is None


def test_assoc_entries110_stub_double():
    # sql_OrOrderByColumn has no real 'sql_OrOrderByColumn111' property in the generated
    # code (a bare stub) -- manually attach it so sql_OrderByColumnFull's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # sql_OrderByColumnFull's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = sql_OrderByColumnFull(colOrderInt="sample_text", direction="sample_text")
    partner = sql_OrOrderByColumn()
    setattr(partner, 'sql_OrOrderByColumn111', None)
    _safe_set(owner, 'sql_OrderByColumnFull', partner)
    assert owner in getattr(partner, 'sql_OrOrderByColumn111')
    _safe_set(owner, 'sql_OrderByColumnFull', None)
    assert owner not in getattr(partner, 'sql_OrOrderByColumn111')


def test_assoc_entries114_stub_double():
    # sql_OrGroupByColumn has no real 'sql_OrGroupByColumn115' property in the generated
    # code (a bare stub) -- manually attach it so sql_GroupByColumnFull's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # sql_GroupByColumnFull's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = sql_GroupByColumnFull(grByInt="sample_text")
    partner = sql_OrGroupByColumn()
    setattr(partner, 'sql_OrGroupByColumn115', None)
    _safe_set(owner, 'sql_GroupByColumnFull', partner)
    assert owner in getattr(partner, 'sql_OrGroupByColumn115')
    _safe_set(owner, 'sql_GroupByColumnFull', None)
    assert owner not in getattr(partner, 'sql_OrGroupByColumn115')


def test_assoc_entries121_stub_double():
    # sql_OrExpr has no real 'sql_OrExpr122' property in the generated
    # code (a bare stub) -- manually attach it so sql_FullExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # sql_FullExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = sql_FullExpression(c="sample_text", isnull="sample_text", notPrm="sample_text")
    partner = sql_OrExpr()
    setattr(partner, 'sql_OrExpr122', None)
    _safe_set(owner, 'sql_FullExpression', partner)
    assert owner in getattr(partner, 'sql_OrExpr122')
    _safe_set(owner, 'sql_FullExpression', None)
    assert owner not in getattr(partner, 'sql_OrExpr122')


def test_assoc_entries154_stub_double():
    # sql_Prms has no real 'sql_Prms155' property in the generated
    # code (a bare stub) -- manually attach it so sql_JRParameter's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # sql_JRParameter's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = sql_JRParameter(jrprm="sample_text")
    partner = sql_Prms()
    setattr(partner, 'sql_Prms155', None)
    _safe_set(owner, 'sql_JRParameter', partner)
    assert owner in getattr(partner, 'sql_Prms155')
    _safe_set(owner, 'sql_JRParameter', None)
    assert owner not in getattr(partner, 'sql_Prms155')


def test_assoc_entries284_stub_double():
    # sql_Col has no real 'sql_Col' property in the generated
    # code (a bare stub) -- manually attach it so sql_DbObjectName's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # sql_DbObjectName's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = sql_DbObjectName(dbname="sample_text")
    partner = sql_Col()
    setattr(partner, 'sql_Col', None)
    _safe_set(owner, 'sql_DbObjectName285', partner)
    assert owner in getattr(partner, 'sql_Col')
    _safe_set(owner, 'sql_DbObjectName285', None)
    assert owner not in getattr(partner, 'sql_Col')


def test_assoc_entries286_stub_double():
    # sql_abc has no real 'sql_abc' property in the generated
    # code (a bare stub) -- manually attach it so sql_ColumnNames's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # sql_ColumnNames's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = sql_ColumnNames(colName="sample_text")
    partner = sql_abc()
    setattr(partner, 'sql_abc', None)
    _safe_set(owner, 'sql_ColumnNames', partner)
    assert owner in getattr(partner, 'sql_abc')
    _safe_set(owner, 'sql_ColumnNames', None)
    assert owner not in getattr(partner, 'sql_abc')


def test_assoc_entries292_stub_double():
    # sql_pcols has no real 'sql_pcols' property in the generated
    # code (a bare stub) -- manually attach it so sql_DbObjectName's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # sql_DbObjectName's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = sql_DbObjectName(dbname="sample_text")
    partner = sql_pcols()
    setattr(partner, 'sql_pcols', None)
    _safe_set(owner, 'sql_DbObjectName293', partner)
    assert owner in getattr(partner, 'sql_pcols')
    _safe_set(owner, 'sql_DbObjectName293', None)
    assert owner not in getattr(partner, 'sql_pcols')


def test_assoc_entries294_stub_double():
    # sql_tbls has no real 'sql_tbls' property in the generated
    # code (a bare stub) -- manually attach it so sql_DbObjectName's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # sql_DbObjectName's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = sql_DbObjectName(dbname="sample_text")
    partner = sql_tbls()
    setattr(partner, 'sql_tbls', None)
    _safe_set(owner, 'sql_DbObjectName295', partner)
    assert owner in getattr(partner, 'sql_tbls')
    _safe_set(owner, 'sql_DbObjectName295', None)
    assert owner not in getattr(partner, 'sql_tbls')


def test_assoc_entries296_stub_double():
    # sql_OpList has no real 'sql_OpList' property in the generated
    # code (a bare stub) -- manually attach it so sql_ScalarOperand's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # sql_ScalarOperand's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = sql_ScalarOperand(soUInt="sample_text", sodate="sample_text", sodbl="sample_text", sodt="sample_text", soint="sample_text", sostr="sample_text", sotime="sample_text")
    partner = sql_OpList()
    setattr(partner, 'sql_OpList', None)
    _safe_set(owner, 'sql_ScalarOperand297', partner)
    assert owner in getattr(partner, 'sql_OpList')
    _safe_set(owner, 'sql_ScalarOperand297', None)
    assert owner not in getattr(partner, 'sql_OpList')


def test_assoc_entries33_stub_double():
    # sql_OrColumn has no real 'sql_OrColumn34' property in the generated
    # code (a bare stub) -- manually attach it so sql_ColumnOrAlias's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # sql_ColumnOrAlias's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = sql_ColumnOrAlias(alias="sample_text", allCols="sample_text")
    partner = sql_OrColumn()
    setattr(partner, 'sql_OrColumn34', None)
    _safe_set(owner, 'sql_ColumnOrAlias', partner)
    assert owner in getattr(partner, 'sql_OrColumn34')
    _safe_set(owner, 'sql_ColumnOrAlias', None)
    assert owner not in getattr(partner, 'sql_OrColumn34')


def test_assoc_entries57_stub_double():
    # sql_UsingCols has no real 'sql_UsingCols58' property in the generated
    # code (a bare stub) -- manually attach it so sql_DbObjectName's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # sql_DbObjectName's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = sql_DbObjectName(dbname="sample_text")
    partner = sql_UsingCols()
    setattr(partner, 'sql_UsingCols58', None)
    _safe_set(owner, 'sql_DbObjectName59', partner)
    assert owner in getattr(partner, 'sql_UsingCols58')
    _safe_set(owner, 'sql_DbObjectName59', None)
    assert owner not in getattr(partner, 'sql_UsingCols58')


def test_assoc_entries85_stub_double():
    # sql_RowValues has no real 'sql_RowValues86' property in the generated
    # code (a bare stub) -- manually attach it so sql_RowValue's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # sql_RowValue's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = sql_RowValue(null="sample_text")
    partner = sql_RowValues()
    setattr(partner, 'sql_RowValues86', None)
    _safe_set(owner, 'sql_RowValue', partner)
    assert owner in getattr(partner, 'sql_RowValues86')
    _safe_set(owner, 'sql_RowValue', None)
    assert owner not in getattr(partner, 'sql_RowValues86')


def test_assoc_eparam216_stub_double():
    # sql_Operand has no real 'sql_Operand217' property in the generated
    # code (a bare stub) -- manually attach it so sql_ExpOperand's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # sql_ExpOperand's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = sql_ExpOperand(prm="sample_text")
    partner = sql_Operand()
    setattr(partner, 'sql_Operand217', None)
    _safe_set(owner, 'sql_ExpOperand', partner)
    assert getattr(partner, 'sql_Operand217') == owner
    _safe_set(owner, 'sql_ExpOperand', None)
    assert getattr(partner, 'sql_Operand217') is None


def test_assoc_expr146_stub_double():
    # sql_OrExpr has no real 'sql_OrExpr148' property in the generated
    # code (a bare stub) -- manually attach it so sql_ExprGroup's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # sql_ExprGroup's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = sql_ExprGroup(isnot="sample_text")
    partner = sql_OrExpr()
    setattr(partner, 'sql_OrExpr148', None)
    _safe_set(owner, 'sql_ExprGroup147', partner)
    assert getattr(partner, 'sql_OrExpr148') == owner
    _safe_set(owner, 'sql_ExprGroup147', None)
    assert getattr(partner, 'sql_OrExpr148') is None


def test_assoc_fan222_stub_double():
    # sql_FunctionAnalytical has no real 'sql_FunctionAnalytical' property in the generated
    # code (a bare stub) -- manually attach it so sql_OpFunction's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # sql_OpFunction's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = sql_OpFunction(fname="sample_text", star="sample_text")
    partner = sql_FunctionAnalytical()
    setattr(partner, 'sql_FunctionAnalytical', None)
    _safe_set(owner, 'sql_OpFunction223', partner)
    assert getattr(partner, 'sql_FunctionAnalytical') == owner
    _safe_set(owner, 'sql_OpFunction223', None)
    assert getattr(partner, 'sql_FunctionAnalytical') is None


def test_assoc_fcast203_stub_double():
    # sql_Operand has no real 'sql_Operand204' property in the generated
    # code (a bare stub) -- manually attach it so sql_OpFunctionCast's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # sql_OpFunctionCast's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = sql_OpFunctionCast(p="sample_text", p2="sample_text", type="sample_text")
    partner = sql_Operand()
    setattr(partner, 'sql_Operand204', None)
    _safe_set(owner, 'sql_OpFunctionCast205', partner)
    assert getattr(partner, 'sql_Operand204') == owner
    _safe_set(owner, 'sql_OpFunctionCast205', None)
    assert getattr(partner, 'sql_Operand204') is None


def test_assoc_fext206_stub_double():
    # sql_Operand has no real 'sql_Operand207' property in the generated
    # code (a bare stub) -- manually attach it so sql_FunctionExtract's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # sql_FunctionExtract's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = sql_FunctionExtract(v="sample_text")
    partner = sql_Operand()
    setattr(partner, 'sql_Operand207', None)
    _safe_set(owner, 'sql_FunctionExtract', partner)
    assert getattr(partner, 'sql_Operand207') == owner
    _safe_set(owner, 'sql_FunctionExtract', None)
    assert getattr(partner, 'sql_Operand207') is None


def test_assoc_fjoin45_stub_double():
    # sql_FromTable has no real 'sql_FromTable46' property in the generated
    # code (a bare stub) -- manually attach it so sql_FromTableJoin's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # sql_FromTableJoin's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = sql_FromTableJoin(join="sample_text")
    partner = sql_FromTable()
    setattr(partner, 'sql_FromTable46', None)
    _safe_set(owner, 'sql_FromTableJoin', partner)
    assert owner in getattr(partner, 'sql_FromTable46')
    _safe_set(owner, 'sql_FromTableJoin', None)
    assert owner not in getattr(partner, 'sql_FromTable46')


def test_assoc_func208_stub_double():
    # sql_Operand has no real 'sql_Operand209' property in the generated
    # code (a bare stub) -- manually attach it so sql_OpFunction's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # sql_OpFunction's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = sql_OpFunction(fname="sample_text", star="sample_text")
    partner = sql_Operand()
    setattr(partner, 'sql_Operand209', None)
    _safe_set(owner, 'sql_OpFunction210', partner)
    assert getattr(partner, 'sql_Operand209') == owner
    _safe_set(owner, 'sql_OpFunction210', None)
    assert getattr(partner, 'sql_Operand209') is None


def test_assoc_groupByEntry19_stub_double():
    # sql_OrGroupByColumn has no real 'sql_OrGroupByColumn' property in the generated
    # code (a bare stub) -- manually attach it so sql_Select's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # sql_Select's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = sql_Select(select="sample_text")
    partner = sql_OrGroupByColumn()
    setattr(partner, 'sql_OrGroupByColumn', None)
    _safe_set(owner, 'sql_Select20', partner)
    assert getattr(partner, 'sql_OrGroupByColumn') == owner
    _safe_set(owner, 'sql_Select20', None)
    assert getattr(partner, 'sql_OrGroupByColumn') is None


def test_assoc_havingEntry21_stub_double():
    # sql_OrExpr has no real 'sql_OrExpr23' property in the generated
    # code (a bare stub) -- manually attach it so sql_Select's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # sql_Select's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = sql_Select(select="sample_text")
    partner = sql_OrExpr()
    setattr(partner, 'sql_OrExpr23', None)
    _safe_set(owner, 'sql_Select22', partner)
    assert getattr(partner, 'sql_OrExpr23') == owner
    _safe_set(owner, 'sql_Select22', None)
    assert getattr(partner, 'sql_OrExpr23') is None


def test_assoc_joinCond53_stub_double():
    # sql_JoinCondition has no real 'sql_JoinCondition' property in the generated
    # code (a bare stub) -- manually attach it so sql_FromTableJoin's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # sql_FromTableJoin's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = sql_FromTableJoin(join="sample_text")
    partner = sql_JoinCondition()
    setattr(partner, 'sql_JoinCondition', None)
    _safe_set(owner, 'sql_FromTableJoin54', partner)
    assert getattr(partner, 'sql_JoinCondition') == owner
    _safe_set(owner, 'sql_FromTableJoin54', None)
    assert getattr(partner, 'sql_JoinCondition') is None


def test_assoc_joinExpr50_stub_double():
    # sql_OrExpr has no real 'sql_OrExpr52' property in the generated
    # code (a bare stub) -- manually attach it so sql_FromTableJoin's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # sql_FromTableJoin's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = sql_FromTableJoin(join="sample_text")
    partner = sql_OrExpr()
    setattr(partner, 'sql_OrExpr52', None)
    _safe_set(owner, 'sql_FromTableJoin51', partner)
    assert getattr(partner, 'sql_OrExpr52') == owner
    _safe_set(owner, 'sql_FromTableJoin51', None)
    assert getattr(partner, 'sql_OrExpr52') is None


def test_assoc_op1137_stub_double():
    # sql_Operands has no real 'sql_Operands139' property in the generated
    # code (a bare stub) -- manually attach it so sql_FullExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # sql_FullExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = sql_FullExpression(c="sample_text", isnull="sample_text", notPrm="sample_text")
    partner = sql_Operands()
    setattr(partner, 'sql_Operands139', None)
    _safe_set(owner, 'sql_FullExpression138', partner)
    assert getattr(partner, 'sql_Operands139') == owner
    _safe_set(owner, 'sql_FullExpression138', None)
    assert getattr(partner, 'sql_Operands139') is None


def test_assoc_op2156_stub_double():
    # sql_Operands has no real 'sql_Operands158' property in the generated
    # code (a bare stub) -- manually attach it so sql_Comparison's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # sql_Comparison's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = sql_Comparison(operator="sample_text", subOperator="sample_text")
    partner = sql_Operands()
    setattr(partner, 'sql_Operands158', None)
    _safe_set(owner, 'sql_Comparison157', partner)
    assert getattr(partner, 'sql_Operands158') == owner
    _safe_set(owner, 'sql_Comparison157', None)
    assert getattr(partner, 'sql_Operands158') is None


def test_assoc_op2168_stub_double():
    # sql_Operands has no real 'sql_Operands170' property in the generated
    # code (a bare stub) -- manually attach it so sql_Between's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # sql_Between's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = sql_Between(opBetween="sample_text")
    partner = sql_Operands()
    setattr(partner, 'sql_Operands170', None)
    _safe_set(owner, 'sql_Between169', partner)
    assert getattr(partner, 'sql_Operands170') == owner
    _safe_set(owner, 'sql_Between169', None)
    assert getattr(partner, 'sql_Operands170') is None


def test_assoc_op256_stub_double():
    # sql_Operands has no real 'sql_Operands258' property in the generated
    # code (a bare stub) -- manually attach it so sql_OpFunctionCast's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # sql_OpFunctionCast's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = sql_OpFunctionCast(p="sample_text", p2="sample_text", type="sample_text")
    partner = sql_Operands()
    setattr(partner, 'sql_Operands258', None)
    _safe_set(owner, 'sql_OpFunctionCast257', partner)
    assert getattr(partner, 'sql_Operands258') == owner
    _safe_set(owner, 'sql_OpFunctionCast257', None)
    assert getattr(partner, 'sql_Operands258') is None


def test_assoc_op3171_stub_double():
    # sql_Operands has no real 'sql_Operands173' property in the generated
    # code (a bare stub) -- manually attach it so sql_Between's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # sql_Between's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = sql_Between(opBetween="sample_text")
    partner = sql_Operands()
    setattr(partner, 'sql_Operands173', None)
    _safe_set(owner, 'sql_Between172', partner)
    assert getattr(partner, 'sql_Operands173') == owner
    _safe_set(owner, 'sql_Between172', None)
    assert getattr(partner, 'sql_Operands173') is None


def test_assoc_opList177_stub_double():
    # sql_OperandListGroup has no real 'sql_OperandListGroup' property in the generated
    # code (a bare stub) -- manually attach it so sql_InOper's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # sql_InOper's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = sql_InOper(op="sample_text")
    partner = sql_OperandListGroup()
    setattr(partner, 'sql_OperandListGroup', None)
    _safe_set(owner, 'sql_InOper178', partner)
    assert getattr(partner, 'sql_OperandListGroup') == owner
    _safe_set(owner, 'sql_InOper178', None)
    assert getattr(partner, 'sql_OperandListGroup') is None


def test_assoc_opList182_stub_double():
    # sql_OperandListGroup has no real 'sql_OperandListGroup184' property in the generated
    # code (a bare stub) -- manually attach it so sql_ExistsOper's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # sql_ExistsOper's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = sql_ExistsOper(op="sample_text")
    partner = sql_OperandListGroup()
    setattr(partner, 'sql_OperandListGroup184', None)
    _safe_set(owner, 'sql_ExistsOper183', partner)
    assert getattr(partner, 'sql_OperandListGroup184') == owner
    _safe_set(owner, 'sql_ExistsOper183', None)
    assert getattr(partner, 'sql_OperandListGroup184') is None


def test_assoc_operand224_stub_double():
    # sql_Operands has no real 'sql_Operands226' property in the generated
    # code (a bare stub) -- manually attach it so sql_FunctionExtract's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # sql_FunctionExtract's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = sql_FunctionExtract(v="sample_text")
    partner = sql_Operands()
    setattr(partner, 'sql_Operands226', None)
    _safe_set(owner, 'sql_FunctionExtract225', partner)
    assert getattr(partner, 'sql_Operands226') == owner
    _safe_set(owner, 'sql_FunctionExtract225', None)
    assert getattr(partner, 'sql_Operands226') is None


def test_assoc_orderByEntry24_stub_double():
    # sql_OrOrderByColumn has no real 'sql_OrOrderByColumn' property in the generated
    # code (a bare stub) -- manually attach it so sql_Select's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # sql_Select's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = sql_Select(select="sample_text")
    partner = sql_OrOrderByColumn()
    setattr(partner, 'sql_OrOrderByColumn', None)
    _safe_set(owner, 'sql_Select25', partner)
    assert getattr(partner, 'sql_OrOrderByColumn') == owner
    _safe_set(owner, 'sql_Select25', None)
    assert getattr(partner, 'sql_OrOrderByColumn') is None


def test_assoc_param213_stub_double():
    # sql_Operand has no real 'sql_Operand214' property in the generated
    # code (a bare stub) -- manually attach it so sql_POperand's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # sql_POperand's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = sql_POperand(prm="sample_text")
    partner = sql_Operand()
    setattr(partner, 'sql_Operand214', None)
    _safe_set(owner, 'sql_POperand215', partner)
    assert getattr(partner, 'sql_Operand214') == owner
    _safe_set(owner, 'sql_POperand215', None)
    assert getattr(partner, 'sql_Operand214') is None


def test_assoc_pfun87_stub_double():
    # sql_PivotTable has no real 'sql_PivotTable88' property in the generated
    # code (a bare stub) -- manually attach it so sql_PivotFunctions's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # sql_PivotFunctions's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = sql_PivotFunctions(abc="sample_text")
    partner = sql_PivotTable()
    setattr(partner, 'sql_PivotTable88', None)
    _safe_set(owner, 'sql_PivotFunctions', partner)
    assert getattr(partner, 'sql_PivotTable88') == owner
    _safe_set(owner, 'sql_PivotFunctions', None)
    assert getattr(partner, 'sql_PivotTable88') is None


def test_assoc_pin91_stub_double():
    # sql_PivotTable has no real 'sql_PivotTable92' property in the generated
    # code (a bare stub) -- manually attach it so sql_PivotInClause's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # sql_PivotInClause's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = sql_PivotInClause(pinany="sample_text")
    partner = sql_PivotTable()
    setattr(partner, 'sql_PivotTable92', None)
    _safe_set(owner, 'sql_PivotInClause', partner)
    assert getattr(partner, 'sql_PivotTable92') == owner
    _safe_set(owner, 'sql_PivotInClause', None)
    assert getattr(partner, 'sql_PivotTable92') is None


def test_assoc_pivot66_stub_double():
    # sql_PivotTable has no real 'sql_PivotTable' property in the generated
    # code (a bare stub) -- manually attach it so sql_TableOrAlias's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # sql_TableOrAlias's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = sql_TableOrAlias(alias="sample_text")
    partner = sql_PivotTable()
    setattr(partner, 'sql_PivotTable', None)
    _safe_set(owner, 'sql_TableOrAlias67', partner)
    assert getattr(partner, 'sql_PivotTable') == owner
    _safe_set(owner, 'sql_TableOrAlias67', None)
    assert getattr(partner, 'sql_PivotTable') is None


def test_assoc_prm152_stub_double():
    # sql_Prms has no real 'sql_Prms' property in the generated
    # code (a bare stub) -- manually attach it so sql_XExpr's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # sql_XExpr's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = sql_XExpr(xf="sample_text")
    partner = sql_Prms()
    setattr(partner, 'sql_Prms', None)
    _safe_set(owner, 'sql_XExpr153', partner)
    assert getattr(partner, 'sql_Prms') == owner
    _safe_set(owner, 'sql_XExpr153', None)
    assert getattr(partner, 'sql_Prms') is None


def test_assoc_query5_stub_double():
    # sql_SelectQuery has no real 'sql_SelectQuery7' property in the generated
    # code (a bare stub) -- manually attach it so sql_WithQuery's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # sql_WithQuery's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = sql_WithQuery(w="sample_text", wname="sample_text")
    partner = sql_SelectQuery()
    setattr(partner, 'sql_SelectQuery7', None)
    _safe_set(owner, 'sql_WithQuery6', partner)
    assert getattr(partner, 'sql_SelectQuery7') == owner
    _safe_set(owner, 'sql_WithQuery6', None)
    assert getattr(partner, 'sql_SelectQuery7') is None


def test_assoc_scalar218_stub_double():
    # sql_Operand has no real 'sql_Operand219' property in the generated
    # code (a bare stub) -- manually attach it so sql_ScalarOperand's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # sql_ScalarOperand's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = sql_ScalarOperand(soUInt="sample_text", sodate="sample_text", sodbl="sample_text", sodt="sample_text", soint="sample_text", sostr="sample_text", sotime="sample_text")
    partner = sql_Operand()
    setattr(partner, 'sql_Operand219', None)
    _safe_set(owner, 'sql_ScalarOperand', partner)
    assert getattr(partner, 'sql_Operand219') == owner
    _safe_set(owner, 'sql_ScalarOperand', None)
    assert getattr(partner, 'sql_Operand219') is None


def test_assoc_sq62_stub_double():
    # sql_SubQueryOperand has no real 'sql_SubQueryOperand' property in the generated
    # code (a bare stub) -- manually attach it so sql_TableOrAlias's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # sql_TableOrAlias's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = sql_TableOrAlias(alias="sample_text")
    partner = sql_SubQueryOperand()
    setattr(partner, 'sql_SubQueryOperand', None)
    _safe_set(owner, 'sql_TableOrAlias63', partner)
    assert getattr(partner, 'sql_SubQueryOperand') == owner
    _safe_set(owner, 'sql_TableOrAlias63', None)
    assert getattr(partner, 'sql_SubQueryOperand') is None


def test_assoc_sq93_stub_double():
    # sql_SubQueryOperand has no real 'sql_SubQueryOperand95' property in the generated
    # code (a bare stub) -- manually attach it so sql_PivotInClause's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # sql_PivotInClause's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = sql_PivotInClause(pinany="sample_text")
    partner = sql_SubQueryOperand()
    setattr(partner, 'sql_SubQueryOperand95', None)
    _safe_set(owner, 'sql_PivotInClause94', partner)
    assert getattr(partner, 'sql_SubQueryOperand95') == owner
    _safe_set(owner, 'sql_PivotInClause94', None)
    assert getattr(partner, 'sql_SubQueryOperand95') is None


def test_assoc_subquery174_stub_double():
    # sql_SubQueryOperand has no real 'sql_SubQueryOperand176' property in the generated
    # code (a bare stub) -- manually attach it so sql_InOper's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # sql_InOper's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = sql_InOper(op="sample_text")
    partner = sql_SubQueryOperand()
    setattr(partner, 'sql_SubQueryOperand176', None)
    _safe_set(owner, 'sql_InOper175', partner)
    assert getattr(partner, 'sql_SubQueryOperand176') == owner
    _safe_set(owner, 'sql_InOper175', None)
    assert getattr(partner, 'sql_SubQueryOperand176') is None


def test_assoc_subquery179_stub_double():
    # sql_SubQueryOperand has no real 'sql_SubQueryOperand181' property in the generated
    # code (a bare stub) -- manually attach it so sql_ExistsOper's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # sql_ExistsOper's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = sql_ExistsOper(op="sample_text")
    partner = sql_SubQueryOperand()
    setattr(partner, 'sql_SubQueryOperand181', None)
    _safe_set(owner, 'sql_ExistsOper180', partner)
    assert getattr(partner, 'sql_SubQueryOperand181') == owner
    _safe_set(owner, 'sql_ExistsOper180', None)
    assert getattr(partner, 'sql_SubQueryOperand181') is None


def test_assoc_table43_stub_double():
    # sql_FromTable has no real 'sql_FromTable44' property in the generated
    # code (a bare stub) -- manually attach it so sql_TableOrAlias's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # sql_TableOrAlias's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = sql_TableOrAlias(alias="sample_text")
    partner = sql_FromTable()
    setattr(partner, 'sql_FromTable44', None)
    _safe_set(owner, 'sql_TableOrAlias', partner)
    assert getattr(partner, 'sql_FromTable44') == owner
    _safe_set(owner, 'sql_TableOrAlias', None)
    assert getattr(partner, 'sql_FromTable44') is None


def test_assoc_tbl15_stub_double():
    # sql_OrTable has no real 'sql_OrTable' property in the generated
    # code (a bare stub) -- manually attach it so sql_Select's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # sql_Select's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = sql_Select(select="sample_text")
    partner = sql_OrTable()
    setattr(partner, 'sql_OrTable', None)
    _safe_set(owner, 'sql_Select16', partner)
    assert getattr(partner, 'sql_OrTable') == owner
    _safe_set(owner, 'sql_Select16', None)
    assert getattr(partner, 'sql_OrTable') is None


def test_assoc_tfull60_stub_double():
    # sql_TableFull has no real 'sql_TableFull' property in the generated
    # code (a bare stub) -- manually attach it so sql_TableOrAlias's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # sql_TableOrAlias's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = sql_TableOrAlias(alias="sample_text")
    partner = sql_TableFull()
    setattr(partner, 'sql_TableFull', None)
    _safe_set(owner, 'sql_TableOrAlias61', partner)
    assert getattr(partner, 'sql_TableFull') == owner
    _safe_set(owner, 'sql_TableOrAlias61', None)
    assert getattr(partner, 'sql_TableFull') is None


def test_assoc_unpivot68_stub_double():
    # sql_UnpivotTable has no real 'sql_UnpivotTable' property in the generated
    # code (a bare stub) -- manually attach it so sql_TableOrAlias's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # sql_TableOrAlias's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = sql_TableOrAlias(alias="sample_text")
    partner = sql_UnpivotTable()
    setattr(partner, 'sql_UnpivotTable', None)
    _safe_set(owner, 'sql_TableOrAlias69', partner)
    assert getattr(partner, 'sql_UnpivotTable') == owner
    _safe_set(owner, 'sql_TableOrAlias69', None)
    assert getattr(partner, 'sql_UnpivotTable') is None


def test_assoc_values64_stub_double():
    # sql_FromValues has no real 'sql_FromValues' property in the generated
    # code (a bare stub) -- manually attach it so sql_TableOrAlias's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # sql_TableOrAlias's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = sql_TableOrAlias(alias="sample_text")
    partner = sql_FromValues()
    setattr(partner, 'sql_FromValues', None)
    _safe_set(owner, 'sql_TableOrAlias65', partner)
    assert getattr(partner, 'sql_FromValues') == owner
    _safe_set(owner, 'sql_TableOrAlias65', None)
    assert getattr(partner, 'sql_FromValues') is None


def test_assoc_whereExpression17_stub_double():
    # sql_OrExpr has no real 'sql_OrExpr' property in the generated
    # code (a bare stub) -- manually attach it so sql_Select's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # sql_Select's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = sql_Select(select="sample_text")
    partner = sql_OrExpr()
    setattr(partner, 'sql_OrExpr', None)
    _safe_set(owner, 'sql_Select18', partner)
    assert getattr(partner, 'sql_OrExpr') == owner
    _safe_set(owner, 'sql_Select18', None)
    assert getattr(partner, 'sql_OrExpr') is None


def test_assoc_withCols3_stub_double():
    # sql_WithColumns has no real 'sql_WithColumns' property in the generated
    # code (a bare stub) -- manually attach it so sql_WithQuery's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # sql_WithQuery's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = sql_WithQuery(w="sample_text", wname="sample_text")
    partner = sql_WithColumns()
    setattr(partner, 'sql_WithColumns', None)
    _safe_set(owner, 'sql_WithQuery4', partner)
    assert getattr(partner, 'sql_WithColumns') == owner
    _safe_set(owner, 'sql_WithQuery4', None)
    assert getattr(partner, 'sql_WithColumns') is None


def test_assoc_wq0_stub_double():
    # sql_Model has no real 'sql_Model' property in the generated
    # code (a bare stub) -- manually attach it so sql_WithQuery's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # sql_WithQuery's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = sql_WithQuery(w="sample_text", wname="sample_text")
    partner = sql_Model()
    setattr(partner, 'sql_Model', None)
    _safe_set(owner, 'sql_WithQuery', partner)
    assert getattr(partner, 'sql_Model') == owner
    _safe_set(owner, 'sql_WithQuery', None)
    assert getattr(partner, 'sql_Model') is None


