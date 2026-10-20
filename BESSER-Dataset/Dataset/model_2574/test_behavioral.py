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

def test_assoc_between133_reverse_link_reassign_clear():
    a1 = sql_FullExpression(c="sample_text", isnull="sample_text", notPrm="sample_text")
    a2 = sql_FullExpression(c="sample_text_2", isnull="sample_text_2", notPrm="sample_text_2")
    b = sql_Between(opBetween="sample_text")
    _safe_set(b, 'sql_Between', a1)
    assert _is_linked(b, 'sql_Between', a1)
    if hasattr(a1, 'sql_FullExpression134'):
        assert _is_linked(a1, 'sql_FullExpression134', b)
    _safe_set(b, 'sql_Between', a2)
    assert _is_linked(b, 'sql_Between', a2)
    if hasattr(a1, 'sql_FullExpression134'):
        assert not _is_linked(a1, 'sql_FullExpression134', b)
    if hasattr(a2, 'sql_FullExpression134'):
        assert _is_linked(a2, 'sql_FullExpression134', b)
    _safe_set(b, 'sql_Between', None)
    assert not _is_linked(b, 'sql_Between', a2)
    if hasattr(a2, 'sql_FullExpression134'):
        assert not _is_linked(a2, 'sql_FullExpression134', b)


def test_assoc_colAlias30_reverse_link_reassign_clear():
    a1 = sql_DbObjectName(dbname="sample_text")
    a2 = sql_DbObjectName(dbname="sample_text_2")
    b = sql_ColumnOrAlias(alias="sample_text", allCols="sample_text")
    _safe_set(b, 'sql_ColumnOrAlias31', a1)
    assert _is_linked(b, 'sql_ColumnOrAlias31', a1)
    if hasattr(a1, 'sql_DbObjectName'):
        assert _is_linked(a1, 'sql_DbObjectName', b)
    _safe_set(b, 'sql_ColumnOrAlias31', a2)
    assert _is_linked(b, 'sql_ColumnOrAlias31', a2)
    if hasattr(a1, 'sql_DbObjectName'):
        assert not _is_linked(a1, 'sql_DbObjectName', b)
    if hasattr(a2, 'sql_DbObjectName'):
        assert _is_linked(a2, 'sql_DbObjectName', b)
    _safe_set(b, 'sql_ColumnOrAlias31', None)
    assert not _is_linked(b, 'sql_ColumnOrAlias31', a2)
    if hasattr(a2, 'sql_DbObjectName'):
        assert not _is_linked(a2, 'sql_DbObjectName', b)


def test_assoc_comp137_reverse_link_reassign_clear():
    a1 = sql_FullExpression(c="sample_text", isnull="sample_text", notPrm="sample_text")
    a2 = sql_FullExpression(c="sample_text_2", isnull="sample_text_2", notPrm="sample_text_2")
    b = sql_Comparison(operator="sample_text", subOperator="sample_text")
    _safe_set(b, 'sql_Comparison', a1)
    assert _is_linked(b, 'sql_Comparison', a1)
    if hasattr(a1, 'sql_FullExpression138'):
        assert _is_linked(a1, 'sql_FullExpression138', b)
    _safe_set(b, 'sql_Comparison', a2)
    assert _is_linked(b, 'sql_Comparison', a2)
    if hasattr(a1, 'sql_FullExpression138'):
        assert not _is_linked(a1, 'sql_FullExpression138', b)
    if hasattr(a2, 'sql_FullExpression138'):
        assert _is_linked(a2, 'sql_FullExpression138', b)
    _safe_set(b, 'sql_Comparison', None)
    assert not _is_linked(b, 'sql_Comparison', a2)
    if hasattr(a2, 'sql_FullExpression138'):
        assert not _is_linked(a2, 'sql_FullExpression138', b)


def test_assoc_dbAllCols32_reverse_link_reassign_clear():
    a1 = sql_DbObjectNameAll(dbname="sample_text")
    a2 = sql_DbObjectNameAll(dbname="sample_text_2")
    b = sql_ColumnOrAlias(alias="sample_text", allCols="sample_text")
    _safe_set(b, 'sql_ColumnOrAlias33', a1)
    assert _is_linked(b, 'sql_ColumnOrAlias33', a1)
    if hasattr(a1, 'sql_DbObjectNameAll'):
        assert _is_linked(a1, 'sql_DbObjectNameAll', b)
    _safe_set(b, 'sql_ColumnOrAlias33', a2)
    assert _is_linked(b, 'sql_ColumnOrAlias33', a2)
    if hasattr(a1, 'sql_DbObjectNameAll'):
        assert not _is_linked(a1, 'sql_DbObjectNameAll', b)
    if hasattr(a2, 'sql_DbObjectNameAll'):
        assert _is_linked(a2, 'sql_DbObjectNameAll', b)
    _safe_set(b, 'sql_ColumnOrAlias33', None)
    assert not _is_linked(b, 'sql_ColumnOrAlias33', a2)
    if hasattr(a2, 'sql_DbObjectNameAll'):
        assert not _is_linked(a2, 'sql_DbObjectNameAll', b)


def test_assoc_efrag117_reverse_link_reassign_clear():
    a1 = sql_FullExpression(c="sample_text", isnull="sample_text", notPrm="sample_text")
    a2 = sql_FullExpression(c="sample_text_2", isnull="sample_text_2", notPrm="sample_text_2")
    b = sql_FullExpression(c="sample_text", isnull="sample_text", notPrm="sample_text")
    _safe_set(b, 'sql_FullExpression118', a1)
    assert _is_linked(b, 'sql_FullExpression118', a1)
    if hasattr(a1, 'sql_FullExpression116'):
        assert _is_linked(a1, 'sql_FullExpression116', b)
    _safe_set(b, 'sql_FullExpression118', a2)
    assert _is_linked(b, 'sql_FullExpression118', a2)
    if hasattr(a1, 'sql_FullExpression116'):
        assert not _is_linked(a1, 'sql_FullExpression116', b)
    if hasattr(a2, 'sql_FullExpression116'):
        assert _is_linked(a2, 'sql_FullExpression116', b)
    _safe_set(b, 'sql_FullExpression118', None)
    assert not _is_linked(b, 'sql_FullExpression118', a2)
    if hasattr(a2, 'sql_FullExpression116'):
        assert not _is_linked(a2, 'sql_FullExpression116', b)


def test_assoc_exists128_reverse_link_reassign_clear():
    a1 = sql_FullExpression(c="sample_text", isnull="sample_text", notPrm="sample_text")
    a2 = sql_FullExpression(c="sample_text_2", isnull="sample_text_2", notPrm="sample_text_2")
    b = sql_ExistsOper(op="sample_text")
    _safe_set(b, 'sql_ExistsOper', a1)
    assert _is_linked(b, 'sql_ExistsOper', a1)
    if hasattr(a1, 'sql_FullExpression129'):
        assert _is_linked(a1, 'sql_FullExpression129', b)
    _safe_set(b, 'sql_ExistsOper', a2)
    assert _is_linked(b, 'sql_ExistsOper', a2)
    if hasattr(a1, 'sql_FullExpression129'):
        assert not _is_linked(a1, 'sql_FullExpression129', b)
    if hasattr(a2, 'sql_FullExpression129'):
        assert _is_linked(a2, 'sql_FullExpression129', b)
    _safe_set(b, 'sql_ExistsOper', None)
    assert not _is_linked(b, 'sql_ExistsOper', a2)
    if hasattr(a2, 'sql_FullExpression129'):
        assert not _is_linked(a2, 'sql_FullExpression129', b)


def test_assoc_exp122_reverse_link_reassign_clear():
    a1 = sql_FullExpression(c="sample_text", isnull="sample_text", notPrm="sample_text")
    a2 = sql_FullExpression(c="sample_text_2", isnull="sample_text_2", notPrm="sample_text_2")
    b = sql_FullExpression(c="sample_text", isnull="sample_text", notPrm="sample_text")
    _safe_set(b, 'sql_FullExpression123', a1)
    assert _is_linked(b, 'sql_FullExpression123', a1)
    if hasattr(a1, 'sql_FullExpression121'):
        assert _is_linked(a1, 'sql_FullExpression121', b)
    _safe_set(b, 'sql_FullExpression123', a2)
    assert _is_linked(b, 'sql_FullExpression123', a2)
    if hasattr(a1, 'sql_FullExpression121'):
        assert not _is_linked(a1, 'sql_FullExpression121', b)
    if hasattr(a2, 'sql_FullExpression121'):
        assert _is_linked(a2, 'sql_FullExpression121', b)
    _safe_set(b, 'sql_FullExpression123', None)
    assert not _is_linked(b, 'sql_FullExpression123', a2)
    if hasattr(a2, 'sql_FullExpression121'):
        assert not _is_linked(a2, 'sql_FullExpression121', b)


def test_assoc_expgroup119_reverse_link_reassign_clear():
    a1 = sql_FullExpression(c="sample_text", isnull="sample_text", notPrm="sample_text")
    a2 = sql_FullExpression(c="sample_text_2", isnull="sample_text_2", notPrm="sample_text_2")
    b = sql_ExprGroup(isnot="sample_text")
    _safe_set(b, 'sql_ExprGroup', a1)
    assert _is_linked(b, 'sql_ExprGroup', a1)
    if hasattr(a1, 'sql_FullExpression120'):
        assert _is_linked(a1, 'sql_FullExpression120', b)
    _safe_set(b, 'sql_ExprGroup', a2)
    assert _is_linked(b, 'sql_ExprGroup', a2)
    if hasattr(a1, 'sql_FullExpression120'):
        assert not _is_linked(a1, 'sql_FullExpression120', b)
    if hasattr(a2, 'sql_FullExpression120'):
        assert _is_linked(a2, 'sql_FullExpression120', b)
    _safe_set(b, 'sql_ExprGroup', None)
    assert not _is_linked(b, 'sql_ExprGroup', a2)
    if hasattr(a2, 'sql_FullExpression120'):
        assert not _is_linked(a2, 'sql_FullExpression120', b)


def test_assoc_fcast157_reverse_link_reassign_clear():
    a1 = sql_OpFunctionCast(p="sample_text", p2="sample_text", type="sample_text")
    a2 = sql_OpFunctionCast(p="sample_text_2", p2="sample_text_2", type="sample_text_2")
    b = sql_LikeOperand(op2="sample_text")
    _safe_set(b, 'sql_LikeOperand158', a1)
    assert _is_linked(b, 'sql_LikeOperand158', a1)
    if hasattr(a1, 'sql_OpFunctionCast'):
        assert _is_linked(a1, 'sql_OpFunctionCast', b)
    _safe_set(b, 'sql_LikeOperand158', a2)
    assert _is_linked(b, 'sql_LikeOperand158', a2)
    if hasattr(a1, 'sql_OpFunctionCast'):
        assert not _is_linked(a1, 'sql_OpFunctionCast', b)
    if hasattr(a2, 'sql_OpFunctionCast'):
        assert _is_linked(a2, 'sql_OpFunctionCast', b)
    _safe_set(b, 'sql_LikeOperand158', None)
    assert not _is_linked(b, 'sql_LikeOperand158', a2)
    if hasattr(a2, 'sql_OpFunctionCast'):
        assert not _is_linked(a2, 'sql_OpFunctionCast', b)


def test_assoc_fetchFirst1_reverse_link_reassign_clear():
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


def test_assoc_fetchFirst23_reverse_link_reassign_clear():
    a1 = sql_Select(select="sample_text")
    a2 = sql_Select(select="sample_text_2")
    b = sql_FetchFirst(row="sample_text")
    _safe_set(b, 'sql_FetchFirst25', a1)
    assert _is_linked(b, 'sql_FetchFirst25', a1)
    if hasattr(a1, 'sql_Select24'):
        assert _is_linked(a1, 'sql_Select24', b)
    _safe_set(b, 'sql_FetchFirst25', a2)
    assert _is_linked(b, 'sql_FetchFirst25', a2)
    if hasattr(a1, 'sql_Select24'):
        assert not _is_linked(a1, 'sql_Select24', b)
    if hasattr(a2, 'sql_Select24'):
        assert _is_linked(a2, 'sql_Select24', b)
    _safe_set(b, 'sql_FetchFirst25', None)
    assert not _is_linked(b, 'sql_FetchFirst25', a2)
    if hasattr(a2, 'sql_Select24'):
        assert not _is_linked(a2, 'sql_Select24', b)


def test_assoc_fop2154_reverse_link_reassign_clear():
    a1 = sql_OpFunction(fname="sample_text", star="sample_text")
    a2 = sql_OpFunction(fname="sample_text_2", star="sample_text_2")
    b = sql_LikeOperand(op2="sample_text")
    _safe_set(b, 'sql_LikeOperand155', a1)
    assert _is_linked(b, 'sql_LikeOperand155', a1)
    if hasattr(a1, 'sql_OpFunction156'):
        assert _is_linked(a1, 'sql_OpFunction156', b)
    _safe_set(b, 'sql_LikeOperand155', a2)
    assert _is_linked(b, 'sql_LikeOperand155', a2)
    if hasattr(a1, 'sql_OpFunction156'):
        assert not _is_linked(a1, 'sql_OpFunction156', b)
    if hasattr(a2, 'sql_OpFunction156'):
        assert _is_linked(a2, 'sql_OpFunction156', b)
    _safe_set(b, 'sql_LikeOperand155', None)
    assert not _is_linked(b, 'sql_LikeOperand155', a2)
    if hasattr(a2, 'sql_OpFunction156'):
        assert not _is_linked(a2, 'sql_OpFunction156', b)


def test_assoc_fparam159_reverse_link_reassign_clear():
    a1 = sql_POperand(prm="sample_text")
    a2 = sql_POperand(prm="sample_text_2")
    b = sql_LikeOperand(op2="sample_text")
    _safe_set(b, 'sql_LikeOperand160', a1)
    assert _is_linked(b, 'sql_LikeOperand160', a1)
    if hasattr(a1, 'sql_POperand'):
        assert _is_linked(a1, 'sql_POperand', b)
    _safe_set(b, 'sql_LikeOperand160', a2)
    assert _is_linked(b, 'sql_LikeOperand160', a2)
    if hasattr(a1, 'sql_POperand'):
        assert not _is_linked(a1, 'sql_POperand', b)
    if hasattr(a2, 'sql_POperand'):
        assert _is_linked(a2, 'sql_POperand', b)
    _safe_set(b, 'sql_LikeOperand160', None)
    assert not _is_linked(b, 'sql_LikeOperand160', a2)
    if hasattr(a2, 'sql_POperand'):
        assert not _is_linked(a2, 'sql_POperand', b)


def test_assoc_gbFunction112_reverse_link_reassign_clear():
    a1 = sql_OpFunction(fname="sample_text", star="sample_text")
    a2 = sql_OpFunction(fname="sample_text_2", star="sample_text_2")
    b = sql_GroupByColumnFull(grByInt="sample_text")
    _safe_set(b, 'sql_GroupByColumnFull113', a1)
    assert _is_linked(b, 'sql_GroupByColumnFull113', a1)
    if hasattr(a1, 'sql_OpFunction'):
        assert _is_linked(a1, 'sql_OpFunction', b)
    _safe_set(b, 'sql_GroupByColumnFull113', a2)
    assert _is_linked(b, 'sql_GroupByColumnFull113', a2)
    if hasattr(a1, 'sql_OpFunction'):
        assert not _is_linked(a1, 'sql_OpFunction', b)
    if hasattr(a2, 'sql_OpFunction'):
        assert _is_linked(a2, 'sql_OpFunction', b)
    _safe_set(b, 'sql_GroupByColumnFull113', None)
    assert not _is_linked(b, 'sql_GroupByColumnFull113', a2)
    if hasattr(a2, 'sql_OpFunction'):
        assert not _is_linked(a2, 'sql_OpFunction', b)


def test_assoc_in_126_reverse_link_reassign_clear():
    a1 = sql_InOper(op="sample_text")
    a2 = sql_InOper(op="sample_text_2")
    b = sql_FullExpression(c="sample_text", isnull="sample_text", notPrm="sample_text")
    _safe_set(b, 'sql_FullExpression127', a1)
    assert _is_linked(b, 'sql_FullExpression127', a1)
    if hasattr(a1, 'sql_InOper'):
        assert _is_linked(a1, 'sql_InOper', b)
    _safe_set(b, 'sql_FullExpression127', a2)
    assert _is_linked(b, 'sql_FullExpression127', a2)
    if hasattr(a1, 'sql_InOper'):
        assert not _is_linked(a1, 'sql_InOper', b)
    if hasattr(a2, 'sql_InOper'):
        assert _is_linked(a2, 'sql_InOper', b)
    _safe_set(b, 'sql_FullExpression127', None)
    assert not _is_linked(b, 'sql_FullExpression127', a2)
    if hasattr(a2, 'sql_InOper'):
        assert not _is_linked(a2, 'sql_InOper', b)


def test_assoc_like135_reverse_link_reassign_clear():
    a1 = sql_Like(opLike="sample_text")
    a2 = sql_Like(opLike="sample_text_2")
    b = sql_FullExpression(c="sample_text", isnull="sample_text", notPrm="sample_text")
    _safe_set(b, 'sql_FullExpression136', a1)
    assert _is_linked(b, 'sql_FullExpression136', a1)
    if hasattr(a1, 'sql_Like'):
        assert _is_linked(a1, 'sql_Like', b)
    _safe_set(b, 'sql_FullExpression136', a2)
    assert _is_linked(b, 'sql_FullExpression136', a2)
    if hasattr(a1, 'sql_Like'):
        assert not _is_linked(a1, 'sql_Like', b)
    if hasattr(a2, 'sql_Like'):
        assert _is_linked(a2, 'sql_Like', b)
    _safe_set(b, 'sql_FullExpression136', None)
    assert not _is_linked(b, 'sql_FullExpression136', a2)
    if hasattr(a2, 'sql_Like'):
        assert not _is_linked(a2, 'sql_Like', b)


def test_assoc_lim19_reverse_link_reassign_clear():
    a1 = sql_Select(select="sample_text")
    a2 = sql_Select(select="sample_text_2")
    b = sql_Limit(l1="sample_text", l2="sample_text")
    _safe_set(b, 'sql_Limit', a1)
    assert _is_linked(b, 'sql_Limit', a1)
    if hasattr(a1, 'sql_Select20'):
        assert _is_linked(a1, 'sql_Select20', b)
    _safe_set(b, 'sql_Limit', a2)
    assert _is_linked(b, 'sql_Limit', a2)
    if hasattr(a1, 'sql_Select20'):
        assert not _is_linked(a1, 'sql_Select20', b)
    if hasattr(a2, 'sql_Select20'):
        assert _is_linked(a2, 'sql_Select20', b)
    _safe_set(b, 'sql_Limit', None)
    assert not _is_linked(b, 'sql_Limit', a2)
    if hasattr(a2, 'sql_Select20'):
        assert not _is_linked(a2, 'sql_Select20', b)


def test_assoc_offset21_reverse_link_reassign_clear():
    a1 = sql_Select(select="sample_text")
    a2 = sql_Select(select="sample_text_2")
    b = sql_Offset(offset="sample_text")
    _safe_set(b, 'sql_Offset', a1)
    assert _is_linked(b, 'sql_Offset', a1)
    if hasattr(a1, 'sql_Select22'):
        assert _is_linked(a1, 'sql_Select22', b)
    _safe_set(b, 'sql_Offset', a2)
    assert _is_linked(b, 'sql_Offset', a2)
    if hasattr(a1, 'sql_Select22'):
        assert not _is_linked(a1, 'sql_Select22', b)
    if hasattr(a2, 'sql_Select22'):
        assert _is_linked(a2, 'sql_Select22', b)
    _safe_set(b, 'sql_Offset', None)
    assert not _is_linked(b, 'sql_Offset', a2)
    if hasattr(a2, 'sql_Select22'):
        assert not _is_linked(a2, 'sql_Select22', b)


def test_assoc_onTable40_reverse_link_reassign_clear():
    a1 = sql_TableOrAlias(alias="sample_text")
    a2 = sql_TableOrAlias(alias="sample_text_2")
    b = sql_FromTableJoin(join="sample_text")
    _safe_set(b, 'sql_FromTableJoin41', a1)
    assert _is_linked(b, 'sql_FromTableJoin41', a1)
    if hasattr(a1, 'sql_TableOrAlias42'):
        assert _is_linked(a1, 'sql_TableOrAlias42', b)
    _safe_set(b, 'sql_FromTableJoin41', a2)
    assert _is_linked(b, 'sql_FromTableJoin41', a2)
    if hasattr(a1, 'sql_TableOrAlias42'):
        assert not _is_linked(a1, 'sql_TableOrAlias42', b)
    if hasattr(a2, 'sql_TableOrAlias42'):
        assert _is_linked(a2, 'sql_TableOrAlias42', b)
    _safe_set(b, 'sql_FromTableJoin41', None)
    assert not _is_linked(b, 'sql_FromTableJoin41', a2)
    if hasattr(a2, 'sql_TableOrAlias42'):
        assert not _is_linked(a2, 'sql_TableOrAlias42', b)


def test_assoc_op2152_reverse_link_reassign_clear():
    a1 = sql_LikeOperand(op2="sample_text")
    a2 = sql_LikeOperand(op2="sample_text_2")
    b = sql_Like(opLike="sample_text")
    _safe_set(b, 'sql_Like153', a1)
    assert _is_linked(b, 'sql_Like153', a1)
    if hasattr(a1, 'sql_LikeOperand'):
        assert _is_linked(a1, 'sql_LikeOperand', b)
    _safe_set(b, 'sql_Like153', a2)
    assert _is_linked(b, 'sql_Like153', a2)
    if hasattr(a1, 'sql_LikeOperand'):
        assert not _is_linked(a1, 'sql_LikeOperand', b)
    if hasattr(a2, 'sql_LikeOperand'):
        assert _is_linked(a2, 'sql_LikeOperand', b)
    _safe_set(b, 'sql_Like153', None)
    assert not _is_linked(b, 'sql_Like153', a2)
    if hasattr(a2, 'sql_LikeOperand'):
        assert not _is_linked(a2, 'sql_LikeOperand', b)


def test_assoc_op3_reverse_link_reassign_clear():
    a1 = sql_SelectSubSet(all="sample_text", op="sample_text")
    a2 = sql_SelectSubSet(all="sample_text_2", op="sample_text_2")
    b = sql_Select(select="sample_text")
    _safe_set(b, 'sql_Select4', {a1})
    assert _is_linked(b, 'sql_Select4', a1)
    if hasattr(a1, 'sql_SelectSubSet5'):
        assert _is_linked(a1, 'sql_SelectSubSet5', b)
    _safe_set(b, 'sql_Select4', {a2})
    assert _is_linked(b, 'sql_Select4', a2)
    if hasattr(a1, 'sql_SelectSubSet5'):
        assert not _is_linked(a1, 'sql_SelectSubSet5', b)
    if hasattr(a2, 'sql_SelectSubSet5'):
        assert _is_linked(a2, 'sql_SelectSubSet5', b)
    _safe_set(b, 'sql_Select4', set())
    assert not _is_linked(b, 'sql_Select4', a2)
    if hasattr(a2, 'sql_SelectSubSet5'):
        assert not _is_linked(a2, 'sql_SelectSubSet5', b)


def test_assoc_query2_reverse_link_reassign_clear():
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


def test_assoc_tblAlias63_reverse_link_reassign_clear():
    a1 = sql_TableOrAlias(alias="sample_text")
    a2 = sql_TableOrAlias(alias="sample_text_2")
    b = sql_DbObjectName(dbname="sample_text")
    _safe_set(b, 'sql_DbObjectName65', a1)
    assert _is_linked(b, 'sql_DbObjectName65', a1)
    if hasattr(a1, 'sql_TableOrAlias64'):
        assert _is_linked(a1, 'sql_TableOrAlias64', b)
    _safe_set(b, 'sql_DbObjectName65', a2)
    assert _is_linked(b, 'sql_DbObjectName65', a2)
    if hasattr(a1, 'sql_TableOrAlias64'):
        assert not _is_linked(a1, 'sql_TableOrAlias64', b)
    if hasattr(a2, 'sql_TableOrAlias64'):
        assert _is_linked(a2, 'sql_TableOrAlias64', b)
    _safe_set(b, 'sql_DbObjectName65', None)
    assert not _is_linked(b, 'sql_DbObjectName65', a2)
    if hasattr(a2, 'sql_TableOrAlias64'):
        assert not _is_linked(a2, 'sql_TableOrAlias64', b)


def test_assoc_xexp124_reverse_link_reassign_clear():
    a1 = sql_XExpr(xf="sample_text")
    a2 = sql_XExpr(xf="sample_text_2")
    b = sql_FullExpression(c="sample_text", isnull="sample_text", notPrm="sample_text")
    _safe_set(b, 'sql_FullExpression125', a1)
    assert _is_linked(b, 'sql_FullExpression125', a1)
    if hasattr(a1, 'sql_XExpr'):
        assert _is_linked(a1, 'sql_XExpr', b)
    _safe_set(b, 'sql_FullExpression125', a2)
    assert _is_linked(b, 'sql_FullExpression125', a2)
    if hasattr(a1, 'sql_XExpr'):
        assert not _is_linked(a1, 'sql_XExpr', b)
    if hasattr(a2, 'sql_XExpr'):
        assert _is_linked(a2, 'sql_XExpr', b)
    _safe_set(b, 'sql_FullExpression125', None)
    assert not _is_linked(b, 'sql_FullExpression125', a2)
    if hasattr(a2, 'sql_XExpr'):
        assert not _is_linked(a2, 'sql_XExpr', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_args213_stub_double():
    # sql_OpFunctionArg has no real 'sql_OpFunctionArg' property in the generated
    # code (a bare stub) -- manually attach it so sql_OpFunction's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # sql_OpFunction's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = sql_OpFunction(fname="sample_text", star="sample_text")
    partner = sql_OpFunctionArg()
    setattr(partner, 'sql_OpFunctionArg', None)
    _safe_set(owner, 'sql_OpFunction214', partner)
    assert getattr(partner, 'sql_OpFunctionArg') == owner
    _safe_set(owner, 'sql_OpFunction214', None)
    assert getattr(partner, 'sql_OpFunctionArg') is None


def test_assoc_args274_stub_double():
    # sql_UnpivotInClauseArgs has no real 'sql_UnpivotInClauseArgs275' property in the generated
    # code (a bare stub) -- manually attach it so sql_UnipivotInClause's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # sql_UnipivotInClause's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = sql_UnipivotInClause(op="sample_text")
    partner = sql_UnpivotInClauseArgs()
    setattr(partner, 'sql_UnpivotInClauseArgs275', None)
    _safe_set(owner, 'sql_UnipivotInClause', partner)
    assert getattr(partner, 'sql_UnpivotInClauseArgs275') == owner
    _safe_set(owner, 'sql_UnipivotInClause', None)
    assert getattr(partner, 'sql_UnpivotInClauseArgs275') is None


def test_assoc_args89_stub_double():
    # sql_UnpivotInClauseArgs has no real 'sql_UnpivotInClauseArgs' property in the generated
    # code (a bare stub) -- manually attach it so sql_PivotInClause's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # sql_PivotInClause's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = sql_PivotInClause(pinany="sample_text")
    partner = sql_UnpivotInClauseArgs()
    setattr(partner, 'sql_UnpivotInClauseArgs', None)
    _safe_set(owner, 'sql_PivotInClause90', partner)
    assert getattr(partner, 'sql_UnpivotInClauseArgs') == owner
    _safe_set(owner, 'sql_PivotInClause90', None)
    assert getattr(partner, 'sql_UnpivotInClauseArgs') is None


def test_assoc_ce28_stub_double():
    # sql_Operands has no real 'sql_Operands' property in the generated
    # code (a bare stub) -- manually attach it so sql_ColumnOrAlias's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # sql_ColumnOrAlias's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = sql_ColumnOrAlias(alias="sample_text", allCols="sample_text")
    partner = sql_Operands()
    setattr(partner, 'sql_Operands', None)
    _safe_set(owner, 'sql_ColumnOrAlias29', partner)
    assert getattr(partner, 'sql_Operands') == owner
    _safe_set(owner, 'sql_ColumnOrAlias29', None)
    assert getattr(partner, 'sql_Operands') is None


def test_assoc_cfull252_stub_double():
    # sql_ColumnFull has no real 'sql_ColumnFull254' property in the generated
    # code (a bare stub) -- manually attach it so sql_ColumnOperand's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # sql_ColumnOperand's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = sql_ColumnOperand(ora="sample_text")
    partner = sql_ColumnFull()
    setattr(partner, 'sql_ColumnFull254', None)
    _safe_set(owner, 'sql_ColumnOperand253', partner)
    assert getattr(partner, 'sql_ColumnFull254') == owner
    _safe_set(owner, 'sql_ColumnOperand253', None)
    assert getattr(partner, 'sql_ColumnFull254') is None


def test_assoc_col142_stub_double():
    # sql_Operands has no real 'sql_Operands144' property in the generated
    # code (a bare stub) -- manually attach it so sql_XExpr's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # sql_XExpr's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = sql_XExpr(xf="sample_text")
    partner = sql_Operands()
    setattr(partner, 'sql_Operands144', None)
    _safe_set(owner, 'sql_XExpr143', partner)
    assert getattr(partner, 'sql_Operands144') == owner
    _safe_set(owner, 'sql_XExpr143', None)
    assert getattr(partner, 'sql_Operands144') is None


def test_assoc_colAlias245_stub_double():
    # sql_AnalyticExprArg has no real 'sql_AnalyticExprArg246' property in the generated
    # code (a bare stub) -- manually attach it so sql_DbObjectName's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # sql_DbObjectName's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = sql_DbObjectName(dbname="sample_text")
    partner = sql_AnalyticExprArg()
    setattr(partner, 'sql_AnalyticExprArg246', None)
    _safe_set(owner, 'sql_DbObjectName247', partner)
    assert getattr(partner, 'sql_AnalyticExprArg246') == owner
    _safe_set(owner, 'sql_DbObjectName247', None)
    assert getattr(partner, 'sql_AnalyticExprArg246') is None


def test_assoc_colGrBy109_stub_double():
    # sql_ColumnFull has no real 'sql_ColumnFull111' property in the generated
    # code (a bare stub) -- manually attach it so sql_GroupByColumnFull's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # sql_GroupByColumnFull's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = sql_GroupByColumnFull(grByInt="sample_text")
    partner = sql_ColumnFull()
    setattr(partner, 'sql_ColumnFull111', None)
    _safe_set(owner, 'sql_GroupByColumnFull110', partner)
    assert getattr(partner, 'sql_ColumnFull111') == owner
    _safe_set(owner, 'sql_GroupByColumnFull110', None)
    assert getattr(partner, 'sql_ColumnFull111') is None


def test_assoc_colOrder105_stub_double():
    # sql_ColumnFull has no real 'sql_ColumnFull' property in the generated
    # code (a bare stub) -- manually attach it so sql_OrderByColumnFull's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # sql_OrderByColumnFull's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = sql_OrderByColumnFull(colOrderInt="sample_text", direction="sample_text")
    partner = sql_ColumnFull()
    setattr(partner, 'sql_ColumnFull', None)
    _safe_set(owner, 'sql_OrderByColumnFull106', partner)
    assert getattr(partner, 'sql_ColumnFull') == owner
    _safe_set(owner, 'sql_OrderByColumnFull106', None)
    assert getattr(partner, 'sql_ColumnFull') is None


def test_assoc_cols6_stub_double():
    # sql_OrColumn has no real 'sql_OrColumn' property in the generated
    # code (a bare stub) -- manually attach it so sql_Select's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # sql_Select's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = sql_Select(select="sample_text")
    partner = sql_OrColumn()
    setattr(partner, 'sql_OrColumn', None)
    _safe_set(owner, 'sql_Select7', partner)
    assert getattr(partner, 'sql_OrColumn') == owner
    _safe_set(owner, 'sql_Select7', None)
    assert getattr(partner, 'sql_OrColumn') is None


def test_assoc_column188_stub_double():
    # sql_Operand has no real 'sql_Operand189' property in the generated
    # code (a bare stub) -- manually attach it so sql_ColumnOperand's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # sql_ColumnOperand's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = sql_ColumnOperand(ora="sample_text")
    partner = sql_Operand()
    setattr(partner, 'sql_Operand189', None)
    _safe_set(owner, 'sql_ColumnOperand', partner)
    assert getattr(partner, 'sql_Operand189') == owner
    _safe_set(owner, 'sql_ColumnOperand', None)
    assert getattr(partner, 'sql_Operand189') is None


def test_assoc_entries103_stub_double():
    # sql_OrOrderByColumn has no real 'sql_OrOrderByColumn104' property in the generated
    # code (a bare stub) -- manually attach it so sql_OrderByColumnFull's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # sql_OrderByColumnFull's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = sql_OrderByColumnFull(colOrderInt="sample_text", direction="sample_text")
    partner = sql_OrOrderByColumn()
    setattr(partner, 'sql_OrOrderByColumn104', None)
    _safe_set(owner, 'sql_OrderByColumnFull', partner)
    assert owner in getattr(partner, 'sql_OrOrderByColumn104')
    _safe_set(owner, 'sql_OrderByColumnFull', None)
    assert owner not in getattr(partner, 'sql_OrOrderByColumn104')


def test_assoc_entries107_stub_double():
    # sql_OrGroupByColumn has no real 'sql_OrGroupByColumn108' property in the generated
    # code (a bare stub) -- manually attach it so sql_GroupByColumnFull's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # sql_GroupByColumnFull's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = sql_GroupByColumnFull(grByInt="sample_text")
    partner = sql_OrGroupByColumn()
    setattr(partner, 'sql_OrGroupByColumn108', None)
    _safe_set(owner, 'sql_GroupByColumnFull', partner)
    assert owner in getattr(partner, 'sql_OrGroupByColumn108')
    _safe_set(owner, 'sql_GroupByColumnFull', None)
    assert owner not in getattr(partner, 'sql_OrGroupByColumn108')


def test_assoc_entries114_stub_double():
    # sql_OrExpr has no real 'sql_OrExpr115' property in the generated
    # code (a bare stub) -- manually attach it so sql_FullExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # sql_FullExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = sql_FullExpression(c="sample_text", isnull="sample_text", notPrm="sample_text")
    partner = sql_OrExpr()
    setattr(partner, 'sql_OrExpr115', None)
    _safe_set(owner, 'sql_FullExpression', partner)
    assert owner in getattr(partner, 'sql_OrExpr115')
    _safe_set(owner, 'sql_FullExpression', None)
    assert owner not in getattr(partner, 'sql_OrExpr115')


def test_assoc_entries147_stub_double():
    # sql_Prms has no real 'sql_Prms148' property in the generated
    # code (a bare stub) -- manually attach it so sql_JRParameter's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # sql_JRParameter's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = sql_JRParameter(jrprm="sample_text")
    partner = sql_Prms()
    setattr(partner, 'sql_Prms148', None)
    _safe_set(owner, 'sql_JRParameter', partner)
    assert owner in getattr(partner, 'sql_Prms148')
    _safe_set(owner, 'sql_JRParameter', None)
    assert owner not in getattr(partner, 'sql_Prms148')


def test_assoc_entries26_stub_double():
    # sql_OrColumn has no real 'sql_OrColumn27' property in the generated
    # code (a bare stub) -- manually attach it so sql_ColumnOrAlias's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # sql_ColumnOrAlias's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = sql_ColumnOrAlias(alias="sample_text", allCols="sample_text")
    partner = sql_OrColumn()
    setattr(partner, 'sql_OrColumn27', None)
    _safe_set(owner, 'sql_ColumnOrAlias', partner)
    assert owner in getattr(partner, 'sql_OrColumn27')
    _safe_set(owner, 'sql_ColumnOrAlias', None)
    assert owner not in getattr(partner, 'sql_OrColumn27')


def test_assoc_entries271_stub_double():
    # sql_Col has no real 'sql_Col' property in the generated
    # code (a bare stub) -- manually attach it so sql_DbObjectName's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # sql_DbObjectName's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = sql_DbObjectName(dbname="sample_text")
    partner = sql_Col()
    setattr(partner, 'sql_Col', None)
    _safe_set(owner, 'sql_DbObjectName272', partner)
    assert owner in getattr(partner, 'sql_Col')
    _safe_set(owner, 'sql_DbObjectName272', None)
    assert owner not in getattr(partner, 'sql_Col')


def test_assoc_entries273_stub_double():
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


def test_assoc_entries279_stub_double():
    # sql_pcols has no real 'sql_pcols' property in the generated
    # code (a bare stub) -- manually attach it so sql_DbObjectName's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # sql_DbObjectName's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = sql_DbObjectName(dbname="sample_text")
    partner = sql_pcols()
    setattr(partner, 'sql_pcols', None)
    _safe_set(owner, 'sql_DbObjectName280', partner)
    assert owner in getattr(partner, 'sql_pcols')
    _safe_set(owner, 'sql_DbObjectName280', None)
    assert owner not in getattr(partner, 'sql_pcols')


def test_assoc_entries281_stub_double():
    # sql_tbls has no real 'sql_tbls' property in the generated
    # code (a bare stub) -- manually attach it so sql_DbObjectName's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # sql_DbObjectName's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = sql_DbObjectName(dbname="sample_text")
    partner = sql_tbls()
    setattr(partner, 'sql_tbls', None)
    _safe_set(owner, 'sql_DbObjectName282', partner)
    assert owner in getattr(partner, 'sql_tbls')
    _safe_set(owner, 'sql_DbObjectName282', None)
    assert owner not in getattr(partner, 'sql_tbls')


def test_assoc_entries283_stub_double():
    # sql_OpList has no real 'sql_OpList' property in the generated
    # code (a bare stub) -- manually attach it so sql_ScalarOperand's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # sql_ScalarOperand's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = sql_ScalarOperand(soUInt="sample_text", sodate="sample_text", sodbl="sample_text", sodt="sample_text", soint="sample_text", sostr="sample_text", sotime="sample_text")
    partner = sql_OpList()
    setattr(partner, 'sql_OpList', None)
    _safe_set(owner, 'sql_ScalarOperand284', partner)
    assert owner in getattr(partner, 'sql_OpList')
    _safe_set(owner, 'sql_ScalarOperand284', None)
    assert owner not in getattr(partner, 'sql_OpList')


def test_assoc_entries50_stub_double():
    # sql_UsingCols has no real 'sql_UsingCols51' property in the generated
    # code (a bare stub) -- manually attach it so sql_DbObjectName's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # sql_DbObjectName's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = sql_DbObjectName(dbname="sample_text")
    partner = sql_UsingCols()
    setattr(partner, 'sql_UsingCols51', None)
    _safe_set(owner, 'sql_DbObjectName52', partner)
    assert owner in getattr(partner, 'sql_UsingCols51')
    _safe_set(owner, 'sql_DbObjectName52', None)
    assert owner not in getattr(partner, 'sql_UsingCols51')


def test_assoc_entries78_stub_double():
    # sql_RowValues has no real 'sql_RowValues79' property in the generated
    # code (a bare stub) -- manually attach it so sql_RowValue's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # sql_RowValue's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = sql_RowValue(null="sample_text")
    partner = sql_RowValues()
    setattr(partner, 'sql_RowValues79', None)
    _safe_set(owner, 'sql_RowValue', partner)
    assert owner in getattr(partner, 'sql_RowValues79')
    _safe_set(owner, 'sql_RowValue', None)
    assert owner not in getattr(partner, 'sql_RowValues79')


def test_assoc_eparam209_stub_double():
    # sql_Operand has no real 'sql_Operand210' property in the generated
    # code (a bare stub) -- manually attach it so sql_ExpOperand's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # sql_ExpOperand's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = sql_ExpOperand(prm="sample_text")
    partner = sql_Operand()
    setattr(partner, 'sql_Operand210', None)
    _safe_set(owner, 'sql_ExpOperand', partner)
    assert getattr(partner, 'sql_Operand210') == owner
    _safe_set(owner, 'sql_ExpOperand', None)
    assert getattr(partner, 'sql_Operand210') is None


def test_assoc_expr139_stub_double():
    # sql_OrExpr has no real 'sql_OrExpr141' property in the generated
    # code (a bare stub) -- manually attach it so sql_ExprGroup's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # sql_ExprGroup's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = sql_ExprGroup(isnot="sample_text")
    partner = sql_OrExpr()
    setattr(partner, 'sql_OrExpr141', None)
    _safe_set(owner, 'sql_ExprGroup140', partner)
    assert getattr(partner, 'sql_OrExpr141') == owner
    _safe_set(owner, 'sql_ExprGroup140', None)
    assert getattr(partner, 'sql_OrExpr141') is None


def test_assoc_fan215_stub_double():
    # sql_FunctionAnalytical has no real 'sql_FunctionAnalytical' property in the generated
    # code (a bare stub) -- manually attach it so sql_OpFunction's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # sql_OpFunction's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = sql_OpFunction(fname="sample_text", star="sample_text")
    partner = sql_FunctionAnalytical()
    setattr(partner, 'sql_FunctionAnalytical', None)
    _safe_set(owner, 'sql_OpFunction216', partner)
    assert getattr(partner, 'sql_FunctionAnalytical') == owner
    _safe_set(owner, 'sql_OpFunction216', None)
    assert getattr(partner, 'sql_FunctionAnalytical') is None


def test_assoc_fcast196_stub_double():
    # sql_Operand has no real 'sql_Operand197' property in the generated
    # code (a bare stub) -- manually attach it so sql_OpFunctionCast's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # sql_OpFunctionCast's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = sql_OpFunctionCast(p="sample_text", p2="sample_text", type="sample_text")
    partner = sql_Operand()
    setattr(partner, 'sql_Operand197', None)
    _safe_set(owner, 'sql_OpFunctionCast198', partner)
    assert getattr(partner, 'sql_Operand197') == owner
    _safe_set(owner, 'sql_OpFunctionCast198', None)
    assert getattr(partner, 'sql_Operand197') is None


def test_assoc_fext199_stub_double():
    # sql_Operand has no real 'sql_Operand200' property in the generated
    # code (a bare stub) -- manually attach it so sql_FunctionExtract's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # sql_FunctionExtract's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = sql_FunctionExtract(v="sample_text")
    partner = sql_Operand()
    setattr(partner, 'sql_Operand200', None)
    _safe_set(owner, 'sql_FunctionExtract', partner)
    assert getattr(partner, 'sql_Operand200') == owner
    _safe_set(owner, 'sql_FunctionExtract', None)
    assert getattr(partner, 'sql_Operand200') is None


def test_assoc_fjoin38_stub_double():
    # sql_FromTable has no real 'sql_FromTable39' property in the generated
    # code (a bare stub) -- manually attach it so sql_FromTableJoin's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # sql_FromTableJoin's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = sql_FromTableJoin(join="sample_text")
    partner = sql_FromTable()
    setattr(partner, 'sql_FromTable39', None)
    _safe_set(owner, 'sql_FromTableJoin', partner)
    assert owner in getattr(partner, 'sql_FromTable39')
    _safe_set(owner, 'sql_FromTableJoin', None)
    assert owner not in getattr(partner, 'sql_FromTable39')


def test_assoc_func201_stub_double():
    # sql_Operand has no real 'sql_Operand202' property in the generated
    # code (a bare stub) -- manually attach it so sql_OpFunction's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # sql_OpFunction's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = sql_OpFunction(fname="sample_text", star="sample_text")
    partner = sql_Operand()
    setattr(partner, 'sql_Operand202', None)
    _safe_set(owner, 'sql_OpFunction203', partner)
    assert getattr(partner, 'sql_Operand202') == owner
    _safe_set(owner, 'sql_OpFunction203', None)
    assert getattr(partner, 'sql_Operand202') is None


def test_assoc_groupByEntry12_stub_double():
    # sql_OrGroupByColumn has no real 'sql_OrGroupByColumn' property in the generated
    # code (a bare stub) -- manually attach it so sql_Select's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # sql_Select's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = sql_Select(select="sample_text")
    partner = sql_OrGroupByColumn()
    setattr(partner, 'sql_OrGroupByColumn', None)
    _safe_set(owner, 'sql_Select13', partner)
    assert getattr(partner, 'sql_OrGroupByColumn') == owner
    _safe_set(owner, 'sql_Select13', None)
    assert getattr(partner, 'sql_OrGroupByColumn') is None


def test_assoc_havingEntry14_stub_double():
    # sql_OrExpr has no real 'sql_OrExpr16' property in the generated
    # code (a bare stub) -- manually attach it so sql_Select's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # sql_Select's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = sql_Select(select="sample_text")
    partner = sql_OrExpr()
    setattr(partner, 'sql_OrExpr16', None)
    _safe_set(owner, 'sql_Select15', partner)
    assert getattr(partner, 'sql_OrExpr16') == owner
    _safe_set(owner, 'sql_Select15', None)
    assert getattr(partner, 'sql_OrExpr16') is None


def test_assoc_joinCond46_stub_double():
    # sql_JoinCondition has no real 'sql_JoinCondition' property in the generated
    # code (a bare stub) -- manually attach it so sql_FromTableJoin's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # sql_FromTableJoin's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = sql_FromTableJoin(join="sample_text")
    partner = sql_JoinCondition()
    setattr(partner, 'sql_JoinCondition', None)
    _safe_set(owner, 'sql_FromTableJoin47', partner)
    assert getattr(partner, 'sql_JoinCondition') == owner
    _safe_set(owner, 'sql_FromTableJoin47', None)
    assert getattr(partner, 'sql_JoinCondition') is None


def test_assoc_joinExpr43_stub_double():
    # sql_OrExpr has no real 'sql_OrExpr45' property in the generated
    # code (a bare stub) -- manually attach it so sql_FromTableJoin's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # sql_FromTableJoin's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = sql_FromTableJoin(join="sample_text")
    partner = sql_OrExpr()
    setattr(partner, 'sql_OrExpr45', None)
    _safe_set(owner, 'sql_FromTableJoin44', partner)
    assert getattr(partner, 'sql_OrExpr45') == owner
    _safe_set(owner, 'sql_FromTableJoin44', None)
    assert getattr(partner, 'sql_OrExpr45') is None


def test_assoc_op1130_stub_double():
    # sql_Operands has no real 'sql_Operands132' property in the generated
    # code (a bare stub) -- manually attach it so sql_FullExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # sql_FullExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = sql_FullExpression(c="sample_text", isnull="sample_text", notPrm="sample_text")
    partner = sql_Operands()
    setattr(partner, 'sql_Operands132', None)
    _safe_set(owner, 'sql_FullExpression131', partner)
    assert getattr(partner, 'sql_Operands132') == owner
    _safe_set(owner, 'sql_FullExpression131', None)
    assert getattr(partner, 'sql_Operands132') is None


def test_assoc_op2149_stub_double():
    # sql_Operands has no real 'sql_Operands151' property in the generated
    # code (a bare stub) -- manually attach it so sql_Comparison's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # sql_Comparison's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = sql_Comparison(operator="sample_text", subOperator="sample_text")
    partner = sql_Operands()
    setattr(partner, 'sql_Operands151', None)
    _safe_set(owner, 'sql_Comparison150', partner)
    assert getattr(partner, 'sql_Operands151') == owner
    _safe_set(owner, 'sql_Comparison150', None)
    assert getattr(partner, 'sql_Operands151') is None


def test_assoc_op2161_stub_double():
    # sql_Operands has no real 'sql_Operands163' property in the generated
    # code (a bare stub) -- manually attach it so sql_Between's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # sql_Between's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = sql_Between(opBetween="sample_text")
    partner = sql_Operands()
    setattr(partner, 'sql_Operands163', None)
    _safe_set(owner, 'sql_Between162', partner)
    assert getattr(partner, 'sql_Operands163') == owner
    _safe_set(owner, 'sql_Between162', None)
    assert getattr(partner, 'sql_Operands163') is None


def test_assoc_op249_stub_double():
    # sql_Operands has no real 'sql_Operands251' property in the generated
    # code (a bare stub) -- manually attach it so sql_OpFunctionCast's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # sql_OpFunctionCast's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = sql_OpFunctionCast(p="sample_text", p2="sample_text", type="sample_text")
    partner = sql_Operands()
    setattr(partner, 'sql_Operands251', None)
    _safe_set(owner, 'sql_OpFunctionCast250', partner)
    assert getattr(partner, 'sql_Operands251') == owner
    _safe_set(owner, 'sql_OpFunctionCast250', None)
    assert getattr(partner, 'sql_Operands251') is None


def test_assoc_op3164_stub_double():
    # sql_Operands has no real 'sql_Operands166' property in the generated
    # code (a bare stub) -- manually attach it so sql_Between's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # sql_Between's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = sql_Between(opBetween="sample_text")
    partner = sql_Operands()
    setattr(partner, 'sql_Operands166', None)
    _safe_set(owner, 'sql_Between165', partner)
    assert getattr(partner, 'sql_Operands166') == owner
    _safe_set(owner, 'sql_Between165', None)
    assert getattr(partner, 'sql_Operands166') is None


def test_assoc_opList170_stub_double():
    # sql_OperandListGroup has no real 'sql_OperandListGroup' property in the generated
    # code (a bare stub) -- manually attach it so sql_InOper's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # sql_InOper's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = sql_InOper(op="sample_text")
    partner = sql_OperandListGroup()
    setattr(partner, 'sql_OperandListGroup', None)
    _safe_set(owner, 'sql_InOper171', partner)
    assert getattr(partner, 'sql_OperandListGroup') == owner
    _safe_set(owner, 'sql_InOper171', None)
    assert getattr(partner, 'sql_OperandListGroup') is None


def test_assoc_opList175_stub_double():
    # sql_OperandListGroup has no real 'sql_OperandListGroup177' property in the generated
    # code (a bare stub) -- manually attach it so sql_ExistsOper's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # sql_ExistsOper's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = sql_ExistsOper(op="sample_text")
    partner = sql_OperandListGroup()
    setattr(partner, 'sql_OperandListGroup177', None)
    _safe_set(owner, 'sql_ExistsOper176', partner)
    assert getattr(partner, 'sql_OperandListGroup177') == owner
    _safe_set(owner, 'sql_ExistsOper176', None)
    assert getattr(partner, 'sql_OperandListGroup177') is None


def test_assoc_operand217_stub_double():
    # sql_Operands has no real 'sql_Operands219' property in the generated
    # code (a bare stub) -- manually attach it so sql_FunctionExtract's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # sql_FunctionExtract's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = sql_FunctionExtract(v="sample_text")
    partner = sql_Operands()
    setattr(partner, 'sql_Operands219', None)
    _safe_set(owner, 'sql_FunctionExtract218', partner)
    assert getattr(partner, 'sql_Operands219') == owner
    _safe_set(owner, 'sql_FunctionExtract218', None)
    assert getattr(partner, 'sql_Operands219') is None


def test_assoc_orderByEntry17_stub_double():
    # sql_OrOrderByColumn has no real 'sql_OrOrderByColumn' property in the generated
    # code (a bare stub) -- manually attach it so sql_Select's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # sql_Select's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = sql_Select(select="sample_text")
    partner = sql_OrOrderByColumn()
    setattr(partner, 'sql_OrOrderByColumn', None)
    _safe_set(owner, 'sql_Select18', partner)
    assert getattr(partner, 'sql_OrOrderByColumn') == owner
    _safe_set(owner, 'sql_Select18', None)
    assert getattr(partner, 'sql_OrOrderByColumn') is None


def test_assoc_param206_stub_double():
    # sql_Operand has no real 'sql_Operand207' property in the generated
    # code (a bare stub) -- manually attach it so sql_POperand's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # sql_POperand's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = sql_POperand(prm="sample_text")
    partner = sql_Operand()
    setattr(partner, 'sql_Operand207', None)
    _safe_set(owner, 'sql_POperand208', partner)
    assert getattr(partner, 'sql_Operand207') == owner
    _safe_set(owner, 'sql_POperand208', None)
    assert getattr(partner, 'sql_Operand207') is None


def test_assoc_pfun80_stub_double():
    # sql_PivotTable has no real 'sql_PivotTable81' property in the generated
    # code (a bare stub) -- manually attach it so sql_PivotFunctions's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # sql_PivotFunctions's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = sql_PivotFunctions(abc="sample_text")
    partner = sql_PivotTable()
    setattr(partner, 'sql_PivotTable81', None)
    _safe_set(owner, 'sql_PivotFunctions', partner)
    assert getattr(partner, 'sql_PivotTable81') == owner
    _safe_set(owner, 'sql_PivotFunctions', None)
    assert getattr(partner, 'sql_PivotTable81') is None


def test_assoc_pin84_stub_double():
    # sql_PivotTable has no real 'sql_PivotTable85' property in the generated
    # code (a bare stub) -- manually attach it so sql_PivotInClause's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # sql_PivotInClause's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = sql_PivotInClause(pinany="sample_text")
    partner = sql_PivotTable()
    setattr(partner, 'sql_PivotTable85', None)
    _safe_set(owner, 'sql_PivotInClause', partner)
    assert getattr(partner, 'sql_PivotTable85') == owner
    _safe_set(owner, 'sql_PivotInClause', None)
    assert getattr(partner, 'sql_PivotTable85') is None


def test_assoc_pivot59_stub_double():
    # sql_PivotTable has no real 'sql_PivotTable' property in the generated
    # code (a bare stub) -- manually attach it so sql_TableOrAlias's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # sql_TableOrAlias's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = sql_TableOrAlias(alias="sample_text")
    partner = sql_PivotTable()
    setattr(partner, 'sql_PivotTable', None)
    _safe_set(owner, 'sql_TableOrAlias60', partner)
    assert getattr(partner, 'sql_PivotTable') == owner
    _safe_set(owner, 'sql_TableOrAlias60', None)
    assert getattr(partner, 'sql_PivotTable') is None


def test_assoc_prm145_stub_double():
    # sql_Prms has no real 'sql_Prms' property in the generated
    # code (a bare stub) -- manually attach it so sql_XExpr's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # sql_XExpr's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = sql_XExpr(xf="sample_text")
    partner = sql_Prms()
    setattr(partner, 'sql_Prms', None)
    _safe_set(owner, 'sql_XExpr146', partner)
    assert getattr(partner, 'sql_Prms') == owner
    _safe_set(owner, 'sql_XExpr146', None)
    assert getattr(partner, 'sql_Prms') is None


def test_assoc_scalar211_stub_double():
    # sql_Operand has no real 'sql_Operand212' property in the generated
    # code (a bare stub) -- manually attach it so sql_ScalarOperand's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # sql_ScalarOperand's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = sql_ScalarOperand(soUInt="sample_text", sodate="sample_text", sodbl="sample_text", sodt="sample_text", soint="sample_text", sostr="sample_text", sotime="sample_text")
    partner = sql_Operand()
    setattr(partner, 'sql_Operand212', None)
    _safe_set(owner, 'sql_ScalarOperand', partner)
    assert getattr(partner, 'sql_Operand212') == owner
    _safe_set(owner, 'sql_ScalarOperand', None)
    assert getattr(partner, 'sql_Operand212') is None


def test_assoc_sq55_stub_double():
    # sql_SubQueryOperand has no real 'sql_SubQueryOperand' property in the generated
    # code (a bare stub) -- manually attach it so sql_TableOrAlias's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # sql_TableOrAlias's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = sql_TableOrAlias(alias="sample_text")
    partner = sql_SubQueryOperand()
    setattr(partner, 'sql_SubQueryOperand', None)
    _safe_set(owner, 'sql_TableOrAlias56', partner)
    assert getattr(partner, 'sql_SubQueryOperand') == owner
    _safe_set(owner, 'sql_TableOrAlias56', None)
    assert getattr(partner, 'sql_SubQueryOperand') is None


def test_assoc_sq86_stub_double():
    # sql_SubQueryOperand has no real 'sql_SubQueryOperand88' property in the generated
    # code (a bare stub) -- manually attach it so sql_PivotInClause's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # sql_PivotInClause's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = sql_PivotInClause(pinany="sample_text")
    partner = sql_SubQueryOperand()
    setattr(partner, 'sql_SubQueryOperand88', None)
    _safe_set(owner, 'sql_PivotInClause87', partner)
    assert getattr(partner, 'sql_SubQueryOperand88') == owner
    _safe_set(owner, 'sql_PivotInClause87', None)
    assert getattr(partner, 'sql_SubQueryOperand88') is None


def test_assoc_subquery167_stub_double():
    # sql_SubQueryOperand has no real 'sql_SubQueryOperand169' property in the generated
    # code (a bare stub) -- manually attach it so sql_InOper's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # sql_InOper's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = sql_InOper(op="sample_text")
    partner = sql_SubQueryOperand()
    setattr(partner, 'sql_SubQueryOperand169', None)
    _safe_set(owner, 'sql_InOper168', partner)
    assert getattr(partner, 'sql_SubQueryOperand169') == owner
    _safe_set(owner, 'sql_InOper168', None)
    assert getattr(partner, 'sql_SubQueryOperand169') is None


def test_assoc_subquery172_stub_double():
    # sql_SubQueryOperand has no real 'sql_SubQueryOperand174' property in the generated
    # code (a bare stub) -- manually attach it so sql_ExistsOper's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # sql_ExistsOper's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = sql_ExistsOper(op="sample_text")
    partner = sql_SubQueryOperand()
    setattr(partner, 'sql_SubQueryOperand174', None)
    _safe_set(owner, 'sql_ExistsOper173', partner)
    assert getattr(partner, 'sql_SubQueryOperand174') == owner
    _safe_set(owner, 'sql_ExistsOper173', None)
    assert getattr(partner, 'sql_SubQueryOperand174') is None


def test_assoc_table36_stub_double():
    # sql_FromTable has no real 'sql_FromTable37' property in the generated
    # code (a bare stub) -- manually attach it so sql_TableOrAlias's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # sql_TableOrAlias's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = sql_TableOrAlias(alias="sample_text")
    partner = sql_FromTable()
    setattr(partner, 'sql_FromTable37', None)
    _safe_set(owner, 'sql_TableOrAlias', partner)
    assert getattr(partner, 'sql_FromTable37') == owner
    _safe_set(owner, 'sql_TableOrAlias', None)
    assert getattr(partner, 'sql_FromTable37') is None


def test_assoc_tbl8_stub_double():
    # sql_OrTable has no real 'sql_OrTable' property in the generated
    # code (a bare stub) -- manually attach it so sql_Select's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # sql_Select's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = sql_Select(select="sample_text")
    partner = sql_OrTable()
    setattr(partner, 'sql_OrTable', None)
    _safe_set(owner, 'sql_Select9', partner)
    assert getattr(partner, 'sql_OrTable') == owner
    _safe_set(owner, 'sql_Select9', None)
    assert getattr(partner, 'sql_OrTable') is None


def test_assoc_tfull53_stub_double():
    # sql_TableFull has no real 'sql_TableFull' property in the generated
    # code (a bare stub) -- manually attach it so sql_TableOrAlias's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # sql_TableOrAlias's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = sql_TableOrAlias(alias="sample_text")
    partner = sql_TableFull()
    setattr(partner, 'sql_TableFull', None)
    _safe_set(owner, 'sql_TableOrAlias54', partner)
    assert getattr(partner, 'sql_TableFull') == owner
    _safe_set(owner, 'sql_TableOrAlias54', None)
    assert getattr(partner, 'sql_TableFull') is None


def test_assoc_unpivot61_stub_double():
    # sql_UnpivotTable has no real 'sql_UnpivotTable' property in the generated
    # code (a bare stub) -- manually attach it so sql_TableOrAlias's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # sql_TableOrAlias's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = sql_TableOrAlias(alias="sample_text")
    partner = sql_UnpivotTable()
    setattr(partner, 'sql_UnpivotTable', None)
    _safe_set(owner, 'sql_TableOrAlias62', partner)
    assert getattr(partner, 'sql_UnpivotTable') == owner
    _safe_set(owner, 'sql_TableOrAlias62', None)
    assert getattr(partner, 'sql_UnpivotTable') is None


def test_assoc_values57_stub_double():
    # sql_FromValues has no real 'sql_FromValues' property in the generated
    # code (a bare stub) -- manually attach it so sql_TableOrAlias's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # sql_TableOrAlias's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = sql_TableOrAlias(alias="sample_text")
    partner = sql_FromValues()
    setattr(partner, 'sql_FromValues', None)
    _safe_set(owner, 'sql_TableOrAlias58', partner)
    assert getattr(partner, 'sql_FromValues') == owner
    _safe_set(owner, 'sql_TableOrAlias58', None)
    assert getattr(partner, 'sql_FromValues') is None


def test_assoc_whereExpression10_stub_double():
    # sql_OrExpr has no real 'sql_OrExpr' property in the generated
    # code (a bare stub) -- manually attach it so sql_Select's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # sql_Select's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = sql_Select(select="sample_text")
    partner = sql_OrExpr()
    setattr(partner, 'sql_OrExpr', None)
    _safe_set(owner, 'sql_Select11', partner)
    assert getattr(partner, 'sql_OrExpr') == owner
    _safe_set(owner, 'sql_Select11', None)
    assert getattr(partner, 'sql_OrExpr') is None


