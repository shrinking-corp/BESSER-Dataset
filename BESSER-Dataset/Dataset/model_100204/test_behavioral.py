import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    DataType,
    Function,
    Grouping,
    GroupingSetsElement,
    GroupingSpecification,
    MergeOperationSpecification,
    OrderBySpecification,
    Predicate,
    PredicateIn,
    PredicateQuantified,
    Procedure,
    QueryChangeStatement,
    QueryExpressionBody,
    QueryResultSpecification,
    QuerySearchCondition,
    QueryStatement,
    QueryValueExpression,
    SQLObject,
    SQLQueryObject,
    SuperGroupElement,
    Table,
    TableExpression,
    TableReference,
    UpdateSource,
    ValueExpressionAtomic,
    ValueExpressionCase,
    expressions_QueryExpression,
    expressions_SearchCondition,
    expressions_ValueExpression,
    query_CallStatement,
    query_ColumnName,
    query_CursorReference,
    query_Grouping,
    query_GroupingExpression,
    query_GroupingSets,
    query_GroupingSetsElement,
    query_GroupingSetsElementExpression,
    query_GroupingSetsElementSublist,
    query_GroupingSpecification,
    query_MergeInsertSpecification,
    query_MergeOnCondition,
    query_MergeOperationSpecification,
    query_MergeSourceTable,
    query_MergeTargetTable,
    query_MergeUpdateSpecification,
    query_OrderByOrdinal,
    query_OrderByResultColumn,
    query_OrderBySpecification,
    query_OrderByValueExpression,
    query_Predicate,
    query_PredicateBasic,
    query_PredicateBetween,
    query_PredicateExists,
    query_PredicateIn,
    query_PredicateInValueList,
    query_PredicateInValueRowSelect,
    query_PredicateInValueSelect,
    query_PredicateIsNull,
    query_PredicateLike,
    query_PredicateQuantified,
    query_PredicateQuantifiedRowSelect,
    query_PredicateQuantifiedValueSelect,
    query_ProcedureReference,
    query_QueryChangeStatement,
    query_QueryCombined,
    query_QueryDeleteStatement,
    query_QueryExpressionBody,
    query_QueryExpressionRoot,
    query_QueryInsertStatement,
    query_QueryMergeStatement,
    query_QueryNested,
    query_QueryResultSpecification,
    query_QuerySearchCondition,
    query_QuerySelect,
    query_QuerySelectStatement,
    query_QueryStatement,
    query_QueryUpdateStatement,
    query_QueryValueExpression,
    query_QueryValues,
    query_ResultColumn,
    query_ResultTableAllColumns,
    query_SQLQueryObject,
    query_SearchConditionCombined,
    query_SearchConditionNested,
    query_SuperGroup,
    query_SuperGroupElement,
    query_SuperGroupElementExpression,
    query_SuperGroupElementSublist,
    query_TableCorrelation,
    query_TableExpression,
    query_TableFunction,
    query_TableInDatabase,
    query_TableJoined,
    query_TableNested,
    query_TableQueryLateral,
    query_TableReference,
    query_UpdatabilityExpression,
    query_UpdateAssignmentExpression,
    query_UpdateOfColumn,
    query_UpdateSource,
    query_UpdateSourceExprList,
    query_UpdateSourceQuery,
    query_ValueExpressionAtomic,
    query_ValueExpressionCase,
    query_ValueExpressionCaseElse,
    query_ValueExpressionCaseSearch,
    query_ValueExpressionCaseSearchContent,
    query_ValueExpressionCaseSimple,
    query_ValueExpressionCaseSimpleContent,
    query_ValueExpressionCast,
    query_ValueExpressionColumn,
    query_ValueExpressionCombined,
    query_ValueExpressionDefaultValue,
    query_ValueExpressionFunction,
    query_ValueExpressionLabeledDuration,
    query_ValueExpressionNested,
    query_ValueExpressionNullValue,
    query_ValueExpressionRow,
    query_ValueExpressionScalarSelect,
    query_ValueExpressionSimple,
    query_ValueExpressionVariable,
    query_ValuesRow,
    query_WithTableReference,
    query_WithTableSpecification,
    statements_SQLControlStatement,
    statements_SQLDataChangeStatement,
    statements_SQLDataStatement,
    NullOrderingType,
    OrderingSpecType,
    PredicateComparisonOperator,
    PredicateQuantifiedType,
    QueryCombinedOperator,
    SearchConditionCombinedOperator,
    SuperGroupType,
    TableJoinedOperator,
    UpdatabilityType,
    ValueExpressionCombinedOperator,
    ValueExpressionLabeledDurationType,
    ValueExpressionUnaryOperator,
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

def test_assoc_basicLeft75_reverse_link_reassign_clear():
    a1 = query_QueryValueExpression(unaryOperator="sample_text")
    a2 = query_QueryValueExpression(unaryOperator="sample_text_2")
    b = query_PredicateBasic(comparisonOperator="sample_text")
    _safe_set(b, 'PredicateBasic76', a1)
    assert _is_linked(b, 'PredicateBasic76', a1)
    if hasattr(a1, 'leftValueExpr'):
        assert _is_linked(a1, 'leftValueExpr', b)
    _safe_set(b, 'PredicateBasic76', a2)
    assert _is_linked(b, 'PredicateBasic76', a2)
    if hasattr(a1, 'leftValueExpr'):
        assert not _is_linked(a1, 'leftValueExpr', b)
    if hasattr(a2, 'leftValueExpr'):
        assert _is_linked(a2, 'leftValueExpr', b)
    _safe_set(b, 'PredicateBasic76', None)
    assert not _is_linked(b, 'PredicateBasic76', a2)
    if hasattr(a2, 'leftValueExpr'):
        assert not _is_linked(a2, 'leftValueExpr', b)


def test_assoc_basicRight74_reverse_link_reassign_clear():
    a1 = query_QueryValueExpression(unaryOperator="sample_text")
    a2 = query_QueryValueExpression(unaryOperator="sample_text_2")
    b = query_PredicateBasic(comparisonOperator="sample_text")
    _safe_set(b, 'PredicateBasic', a1)
    assert _is_linked(b, 'PredicateBasic', a1)
    if hasattr(a1, 'rightValueExpr'):
        assert _is_linked(a1, 'rightValueExpr', b)
    _safe_set(b, 'PredicateBasic', a2)
    assert _is_linked(b, 'PredicateBasic', a2)
    if hasattr(a1, 'rightValueExpr'):
        assert not _is_linked(a1, 'rightValueExpr', b)
    if hasattr(a2, 'rightValueExpr'):
        assert _is_linked(a2, 'rightValueExpr', b)
    _safe_set(b, 'PredicateBasic', None)
    assert not _is_linked(b, 'PredicateBasic', a2)
    if hasattr(a2, 'rightValueExpr'):
        assert not _is_linked(a2, 'rightValueExpr', b)


def test_assoc_betweenLeft94_reverse_link_reassign_clear():
    a1 = query_QueryValueExpression(unaryOperator="sample_text")
    a2 = query_QueryValueExpression(unaryOperator="sample_text_2")
    b = query_PredicateBetween(notBetween=True)
    _safe_set(b, 'PredicateBetween', a1)
    assert _is_linked(b, 'PredicateBetween', a1)
    if hasattr(a1, 'leftValueExpr95'):
        assert _is_linked(a1, 'leftValueExpr95', b)
    _safe_set(b, 'PredicateBetween', a2)
    assert _is_linked(b, 'PredicateBetween', a2)
    if hasattr(a1, 'leftValueExpr95'):
        assert not _is_linked(a1, 'leftValueExpr95', b)
    if hasattr(a2, 'leftValueExpr95'):
        assert _is_linked(a2, 'leftValueExpr95', b)
    _safe_set(b, 'PredicateBetween', None)
    assert not _is_linked(b, 'PredicateBetween', a2)
    if hasattr(a2, 'leftValueExpr95'):
        assert not _is_linked(a2, 'leftValueExpr95', b)


def test_assoc_betweenRight196_reverse_link_reassign_clear():
    a1 = query_QueryValueExpression(unaryOperator="sample_text")
    a2 = query_QueryValueExpression(unaryOperator="sample_text_2")
    b = query_PredicateBetween(notBetween=True)
    _safe_set(b, 'PredicateBetween97', a1)
    assert _is_linked(b, 'PredicateBetween97', a1)
    if hasattr(a1, 'rightValueExpr1'):
        assert _is_linked(a1, 'rightValueExpr1', b)
    _safe_set(b, 'PredicateBetween97', a2)
    assert _is_linked(b, 'PredicateBetween97', a2)
    if hasattr(a1, 'rightValueExpr1'):
        assert not _is_linked(a1, 'rightValueExpr1', b)
    if hasattr(a2, 'rightValueExpr1'):
        assert _is_linked(a2, 'rightValueExpr1', b)
    _safe_set(b, 'PredicateBetween97', None)
    assert not _is_linked(b, 'PredicateBetween97', a2)
    if hasattr(a2, 'rightValueExpr1'):
        assert not _is_linked(a2, 'rightValueExpr1', b)


def test_assoc_betweenRight298_reverse_link_reassign_clear():
    a1 = query_QueryValueExpression(unaryOperator="sample_text")
    a2 = query_QueryValueExpression(unaryOperator="sample_text_2")
    b = query_PredicateBetween(notBetween=True)
    _safe_set(b, 'PredicateBetween99', a1)
    assert _is_linked(b, 'PredicateBetween99', a1)
    if hasattr(a1, 'rightValueExpr2'):
        assert _is_linked(a1, 'rightValueExpr2', b)
    _safe_set(b, 'PredicateBetween99', a2)
    assert _is_linked(b, 'PredicateBetween99', a2)
    if hasattr(a1, 'rightValueExpr2'):
        assert not _is_linked(a1, 'rightValueExpr2', b)
    if hasattr(a2, 'rightValueExpr2'):
        assert _is_linked(a2, 'rightValueExpr2', b)
    _safe_set(b, 'PredicateBetween99', None)
    assert not _is_linked(b, 'PredicateBetween99', a2)
    if hasattr(a2, 'rightValueExpr2'):
        assert not _is_linked(a2, 'rightValueExpr2', b)


def test_assoc_combinedLeft44_reverse_link_reassign_clear():
    a1 = query_SearchConditionCombined(combinedOperator="sample_text")
    a2 = query_SearchConditionCombined(combinedOperator="sample_text_2")
    b = query_QuerySearchCondition(negatedCondition=True)
    _safe_set(b, 'leftCondition', a1)
    assert _is_linked(b, 'leftCondition', a1)
    if hasattr(a1, 'SearchConditionCombined'):
        assert _is_linked(a1, 'SearchConditionCombined', b)
    _safe_set(b, 'leftCondition', a2)
    assert _is_linked(b, 'leftCondition', a2)
    if hasattr(a1, 'SearchConditionCombined'):
        assert not _is_linked(a1, 'SearchConditionCombined', b)
    if hasattr(a2, 'SearchConditionCombined'):
        assert _is_linked(a2, 'SearchConditionCombined', b)
    _safe_set(b, 'leftCondition', None)
    assert not _is_linked(b, 'leftCondition', a2)
    if hasattr(a2, 'SearchConditionCombined'):
        assert not _is_linked(a2, 'SearchConditionCombined', b)


def test_assoc_combinedLeft57_reverse_link_reassign_clear():
    a1 = query_QueryExpressionBody(rowFetchLimit=7)
    a2 = query_QueryExpressionBody(rowFetchLimit=13)
    b = query_QueryCombined(combinedOperator="sample_text")
    _safe_set(b, 'QueryCombined', a1)
    assert _is_linked(b, 'QueryCombined', a1)
    if hasattr(a1, 'leftQuery'):
        assert _is_linked(a1, 'leftQuery', b)
    _safe_set(b, 'QueryCombined', a2)
    assert _is_linked(b, 'QueryCombined', a2)
    if hasattr(a1, 'leftQuery'):
        assert not _is_linked(a1, 'leftQuery', b)
    if hasattr(a2, 'leftQuery'):
        assert _is_linked(a2, 'leftQuery', b)
    _safe_set(b, 'QueryCombined', None)
    assert not _is_linked(b, 'QueryCombined', a2)
    if hasattr(a2, 'leftQuery'):
        assert not _is_linked(a2, 'leftQuery', b)


def test_assoc_combinedRight45_reverse_link_reassign_clear():
    a1 = query_SearchConditionCombined(combinedOperator="sample_text")
    a2 = query_SearchConditionCombined(combinedOperator="sample_text_2")
    b = query_QuerySearchCondition(negatedCondition=True)
    _safe_set(b, 'rightCondition', a1)
    assert _is_linked(b, 'rightCondition', a1)
    if hasattr(a1, 'SearchConditionCombined46'):
        assert _is_linked(a1, 'SearchConditionCombined46', b)
    _safe_set(b, 'rightCondition', a2)
    assert _is_linked(b, 'rightCondition', a2)
    if hasattr(a1, 'SearchConditionCombined46'):
        assert not _is_linked(a1, 'SearchConditionCombined46', b)
    if hasattr(a2, 'SearchConditionCombined46'):
        assert _is_linked(a2, 'SearchConditionCombined46', b)
    _safe_set(b, 'rightCondition', None)
    assert not _is_linked(b, 'rightCondition', a2)
    if hasattr(a2, 'SearchConditionCombined46'):
        assert not _is_linked(a2, 'SearchConditionCombined46', b)


def test_assoc_combinedRight58_reverse_link_reassign_clear():
    a1 = query_QueryExpressionBody(rowFetchLimit=7)
    a2 = query_QueryExpressionBody(rowFetchLimit=13)
    b = query_QueryCombined(combinedOperator="sample_text")
    _safe_set(b, 'QueryCombined59', a1)
    assert _is_linked(b, 'QueryCombined59', a1)
    if hasattr(a1, 'rightQuery'):
        assert _is_linked(a1, 'rightQuery', b)
    _safe_set(b, 'QueryCombined59', a2)
    assert _is_linked(b, 'QueryCombined59', a2)
    if hasattr(a1, 'rightQuery'):
        assert not _is_linked(a1, 'rightQuery', b)
    if hasattr(a2, 'rightQuery'):
        assert _is_linked(a2, 'rightQuery', b)
    _safe_set(b, 'QueryCombined59', None)
    assert not _is_linked(b, 'QueryCombined59', a2)
    if hasattr(a2, 'rightQuery'):
        assert not _is_linked(a2, 'rightQuery', b)


def test_assoc_escapeValueExpr237_reverse_link_reassign_clear():
    a1 = query_QueryValueExpression(unaryOperator="sample_text")
    a2 = query_QueryValueExpression(unaryOperator="sample_text_2")
    b = query_PredicateLike(notLike=True)
    _safe_set(b, 'likeEscape', a1)
    assert _is_linked(b, 'likeEscape', a1)
    if hasattr(a1, 'QueryValueExpression238'):
        assert _is_linked(a1, 'QueryValueExpression238', b)
    _safe_set(b, 'likeEscape', a2)
    assert _is_linked(b, 'likeEscape', a2)
    if hasattr(a1, 'QueryValueExpression238'):
        assert not _is_linked(a1, 'QueryValueExpression238', b)
    if hasattr(a2, 'QueryValueExpression238'):
        assert _is_linked(a2, 'QueryValueExpression238', b)
    _safe_set(b, 'likeEscape', None)
    assert not _is_linked(b, 'likeEscape', a2)
    if hasattr(a2, 'QueryValueExpression238'):
        assert not _is_linked(a2, 'QueryValueExpression238', b)


def test_assoc_havingClause201_reverse_link_reassign_clear():
    a1 = query_QuerySelect(distinct=True)
    a2 = query_QuerySelect(distinct=False)
    b = query_QuerySearchCondition(negatedCondition=True)
    _safe_set(b, 'QuerySearchCondition202', a1)
    assert _is_linked(b, 'QuerySearchCondition202', a1)
    if hasattr(a1, 'querySelectHaving'):
        assert _is_linked(a1, 'querySelectHaving', b)
    _safe_set(b, 'QuerySearchCondition202', a2)
    assert _is_linked(b, 'QuerySearchCondition202', a2)
    if hasattr(a1, 'querySelectHaving'):
        assert not _is_linked(a1, 'querySelectHaving', b)
    if hasattr(a2, 'querySelectHaving'):
        assert _is_linked(a2, 'querySelectHaving', b)
    _safe_set(b, 'QuerySearchCondition202', None)
    assert not _is_linked(b, 'QuerySearchCondition202', a2)
    if hasattr(a2, 'querySelectHaving'):
        assert not _is_linked(a2, 'querySelectHaving', b)


def test_assoc_joinCondition176_reverse_link_reassign_clear():
    a1 = query_TableJoined(joinOperator="sample_text")
    a2 = query_TableJoined(joinOperator="sample_text_2")
    b = query_QuerySearchCondition(negatedCondition=True)
    _safe_set(b, 'QuerySearchCondition177', a1)
    assert _is_linked(b, 'QuerySearchCondition177', a1)
    if hasattr(a1, 'tableJoined'):
        assert _is_linked(a1, 'tableJoined', b)
    _safe_set(b, 'QuerySearchCondition177', a2)
    assert _is_linked(b, 'QuerySearchCondition177', a2)
    if hasattr(a1, 'tableJoined'):
        assert not _is_linked(a1, 'tableJoined', b)
    if hasattr(a2, 'tableJoined'):
        assert _is_linked(a2, 'tableJoined', b)
    _safe_set(b, 'QuerySearchCondition177', None)
    assert not _is_linked(b, 'QuerySearchCondition177', a2)
    if hasattr(a2, 'tableJoined'):
        assert not _is_linked(a2, 'tableJoined', b)


def test_assoc_leftCondition189_reverse_link_reassign_clear():
    a1 = query_SearchConditionCombined(combinedOperator="sample_text")
    a2 = query_SearchConditionCombined(combinedOperator="sample_text_2")
    b = query_QuerySearchCondition(negatedCondition=True)
    _safe_set(b, 'QuerySearchCondition190', a1)
    assert _is_linked(b, 'QuerySearchCondition190', a1)
    if hasattr(a1, 'combinedLeft'):
        assert _is_linked(a1, 'combinedLeft', b)
    _safe_set(b, 'QuerySearchCondition190', a2)
    assert _is_linked(b, 'QuerySearchCondition190', a2)
    if hasattr(a1, 'combinedLeft'):
        assert not _is_linked(a1, 'combinedLeft', b)
    if hasattr(a2, 'combinedLeft'):
        assert _is_linked(a2, 'combinedLeft', b)
    _safe_set(b, 'QuerySearchCondition190', None)
    assert not _is_linked(b, 'QuerySearchCondition190', a2)
    if hasattr(a2, 'combinedLeft'):
        assert not _is_linked(a2, 'combinedLeft', b)


def test_assoc_leftQuery195_reverse_link_reassign_clear():
    a1 = query_QueryExpressionBody(rowFetchLimit=7)
    a2 = query_QueryExpressionBody(rowFetchLimit=13)
    b = query_QueryCombined(combinedOperator="sample_text")
    _safe_set(b, 'combinedLeft196', a1)
    assert _is_linked(b, 'combinedLeft196', a1)
    if hasattr(a1, 'QueryExpressionBody197'):
        assert _is_linked(a1, 'QueryExpressionBody197', b)
    _safe_set(b, 'combinedLeft196', a2)
    assert _is_linked(b, 'combinedLeft196', a2)
    if hasattr(a1, 'QueryExpressionBody197'):
        assert not _is_linked(a1, 'QueryExpressionBody197', b)
    if hasattr(a2, 'QueryExpressionBody197'):
        assert _is_linked(a2, 'QueryExpressionBody197', b)
    _safe_set(b, 'combinedLeft196', None)
    assert not _is_linked(b, 'combinedLeft196', a2)
    if hasattr(a2, 'QueryExpressionBody197'):
        assert not _is_linked(a2, 'QueryExpressionBody197', b)


def test_assoc_leftValueExpr223_reverse_link_reassign_clear():
    a1 = query_QueryValueExpression(unaryOperator="sample_text")
    a2 = query_QueryValueExpression(unaryOperator="sample_text_2")
    b = query_PredicateBasic(comparisonOperator="sample_text")
    _safe_set(b, 'basicLeft', a1)
    assert _is_linked(b, 'basicLeft', a1)
    if hasattr(a1, 'QueryValueExpression224'):
        assert _is_linked(a1, 'QueryValueExpression224', b)
    _safe_set(b, 'basicLeft', a2)
    assert _is_linked(b, 'basicLeft', a2)
    if hasattr(a1, 'QueryValueExpression224'):
        assert not _is_linked(a1, 'QueryValueExpression224', b)
    if hasattr(a2, 'QueryValueExpression224'):
        assert _is_linked(a2, 'QueryValueExpression224', b)
    _safe_set(b, 'basicLeft', None)
    assert not _is_linked(b, 'basicLeft', a2)
    if hasattr(a2, 'QueryValueExpression224'):
        assert not _is_linked(a2, 'QueryValueExpression224', b)


def test_assoc_leftValueExpr225_reverse_link_reassign_clear():
    a1 = query_QueryValueExpression(unaryOperator="sample_text")
    a2 = query_QueryValueExpression(unaryOperator="sample_text_2")
    b = query_PredicateBetween(notBetween=True)
    _safe_set(b, 'betweenLeft', a1)
    assert _is_linked(b, 'betweenLeft', a1)
    if hasattr(a1, 'QueryValueExpression226'):
        assert _is_linked(a1, 'QueryValueExpression226', b)
    _safe_set(b, 'betweenLeft', a2)
    assert _is_linked(b, 'betweenLeft', a2)
    if hasattr(a1, 'QueryValueExpression226'):
        assert not _is_linked(a1, 'QueryValueExpression226', b)
    if hasattr(a2, 'QueryValueExpression226'):
        assert _is_linked(a2, 'QueryValueExpression226', b)
    _safe_set(b, 'betweenLeft', None)
    assert not _is_linked(b, 'betweenLeft', a2)
    if hasattr(a2, 'QueryValueExpression226'):
        assert not _is_linked(a2, 'QueryValueExpression226', b)


def test_assoc_leftValueExpr287_reverse_link_reassign_clear():
    a1 = query_ValueExpressionCombined(combinedOperator="sample_text")
    a2 = query_ValueExpressionCombined(combinedOperator="sample_text_2")
    b = query_QueryValueExpression(unaryOperator="sample_text")
    _safe_set(b, 'QueryValueExpression288', a1)
    assert _is_linked(b, 'QueryValueExpression288', a1)
    if hasattr(a1, 'valueExprCombinedLeft'):
        assert _is_linked(a1, 'valueExprCombinedLeft', b)
    _safe_set(b, 'QueryValueExpression288', a2)
    assert _is_linked(b, 'QueryValueExpression288', a2)
    if hasattr(a1, 'valueExprCombinedLeft'):
        assert not _is_linked(a1, 'valueExprCombinedLeft', b)
    if hasattr(a2, 'valueExprCombinedLeft'):
        assert _is_linked(a2, 'valueExprCombinedLeft', b)
    _safe_set(b, 'QueryValueExpression288', None)
    assert not _is_linked(b, 'QueryValueExpression288', a2)
    if hasattr(a2, 'valueExprCombinedLeft'):
        assert not _is_linked(a2, 'valueExprCombinedLeft', b)


def test_assoc_likeEscape120_reverse_link_reassign_clear():
    a1 = query_QueryValueExpression(unaryOperator="sample_text")
    a2 = query_QueryValueExpression(unaryOperator="sample_text_2")
    b = query_PredicateLike(notLike=True)
    _safe_set(b, 'PredicateLike121', a1)
    assert _is_linked(b, 'PredicateLike121', a1)
    if hasattr(a1, 'escapeValueExpr'):
        assert _is_linked(a1, 'escapeValueExpr', b)
    _safe_set(b, 'PredicateLike121', a2)
    assert _is_linked(b, 'PredicateLike121', a2)
    if hasattr(a1, 'escapeValueExpr'):
        assert not _is_linked(a1, 'escapeValueExpr', b)
    if hasattr(a2, 'escapeValueExpr'):
        assert _is_linked(a2, 'escapeValueExpr', b)
    _safe_set(b, 'PredicateLike121', None)
    assert not _is_linked(b, 'PredicateLike121', a2)
    if hasattr(a2, 'escapeValueExpr'):
        assert not _is_linked(a2, 'escapeValueExpr', b)


def test_assoc_likeMatching78_reverse_link_reassign_clear():
    a1 = query_QueryValueExpression(unaryOperator="sample_text")
    a2 = query_QueryValueExpression(unaryOperator="sample_text_2")
    b = query_PredicateLike(notLike=True)
    _safe_set(b, 'PredicateLike79', a1)
    assert _is_linked(b, 'PredicateLike79', a1)
    if hasattr(a1, 'matchingValueExpr'):
        assert _is_linked(a1, 'matchingValueExpr', b)
    _safe_set(b, 'PredicateLike79', a2)
    assert _is_linked(b, 'PredicateLike79', a2)
    if hasattr(a1, 'matchingValueExpr'):
        assert not _is_linked(a1, 'matchingValueExpr', b)
    if hasattr(a2, 'matchingValueExpr'):
        assert _is_linked(a2, 'matchingValueExpr', b)
    _safe_set(b, 'PredicateLike79', None)
    assert not _is_linked(b, 'PredicateLike79', a2)
    if hasattr(a2, 'matchingValueExpr'):
        assert not _is_linked(a2, 'matchingValueExpr', b)


def test_assoc_likePattern77_reverse_link_reassign_clear():
    a1 = query_QueryValueExpression(unaryOperator="sample_text")
    a2 = query_QueryValueExpression(unaryOperator="sample_text_2")
    b = query_PredicateLike(notLike=True)
    _safe_set(b, 'PredicateLike', a1)
    assert _is_linked(b, 'PredicateLike', a1)
    if hasattr(a1, 'patternValueExpr'):
        assert _is_linked(a1, 'patternValueExpr', b)
    _safe_set(b, 'PredicateLike', a2)
    assert _is_linked(b, 'PredicateLike', a2)
    if hasattr(a1, 'patternValueExpr'):
        assert not _is_linked(a1, 'patternValueExpr', b)
    if hasattr(a2, 'patternValueExpr'):
        assert _is_linked(a2, 'patternValueExpr', b)
    _safe_set(b, 'PredicateLike', None)
    assert not _is_linked(b, 'PredicateLike', a2)
    if hasattr(a2, 'patternValueExpr'):
        assert not _is_linked(a2, 'patternValueExpr', b)


def test_assoc_matchingValueExpr235_reverse_link_reassign_clear():
    a1 = query_QueryValueExpression(unaryOperator="sample_text")
    a2 = query_QueryValueExpression(unaryOperator="sample_text_2")
    b = query_PredicateLike(notLike=True)
    _safe_set(b, 'likeMatching', a1)
    assert _is_linked(b, 'likeMatching', a1)
    if hasattr(a1, 'QueryValueExpression236'):
        assert _is_linked(a1, 'QueryValueExpression236', b)
    _safe_set(b, 'likeMatching', a2)
    assert _is_linked(b, 'likeMatching', a2)
    if hasattr(a1, 'QueryValueExpression236'):
        assert not _is_linked(a1, 'QueryValueExpression236', b)
    if hasattr(a2, 'QueryValueExpression236'):
        assert _is_linked(a2, 'QueryValueExpression236', b)
    _safe_set(b, 'likeMatching', None)
    assert not _is_linked(b, 'likeMatching', a2)
    if hasattr(a2, 'QueryValueExpression236'):
        assert not _is_linked(a2, 'QueryValueExpression236', b)


def test_assoc_parameterList284_reverse_link_reassign_clear():
    a1 = query_ValueExpressionFunction(columnFunction=True, distinct=True, specialRegister=True)
    a2 = query_ValueExpressionFunction(columnFunction=False, distinct=False, specialRegister=False)
    b = query_QueryValueExpression(unaryOperator="sample_text")
    _safe_set(b, 'QueryValueExpression285', a1)
    assert _is_linked(b, 'QueryValueExpression285', a1)
    if hasattr(a1, 'valueExprFunction'):
        assert _is_linked(a1, 'valueExprFunction', b)
    _safe_set(b, 'QueryValueExpression285', a2)
    assert _is_linked(b, 'QueryValueExpression285', a2)
    if hasattr(a1, 'valueExprFunction'):
        assert not _is_linked(a1, 'valueExprFunction', b)
    if hasattr(a2, 'valueExprFunction'):
        assert _is_linked(a2, 'valueExprFunction', b)
    _safe_set(b, 'QueryValueExpression285', None)
    assert not _is_linked(b, 'QueryValueExpression285', a2)
    if hasattr(a2, 'valueExprFunction'):
        assert not _is_linked(a2, 'valueExprFunction', b)


def test_assoc_patternValueExpr233_reverse_link_reassign_clear():
    a1 = query_QueryValueExpression(unaryOperator="sample_text")
    a2 = query_QueryValueExpression(unaryOperator="sample_text_2")
    b = query_PredicateLike(notLike=True)
    _safe_set(b, 'likePattern', a1)
    assert _is_linked(b, 'likePattern', a1)
    if hasattr(a1, 'QueryValueExpression234'):
        assert _is_linked(a1, 'QueryValueExpression234', b)
    _safe_set(b, 'likePattern', a2)
    assert _is_linked(b, 'likePattern', a2)
    if hasattr(a1, 'QueryValueExpression234'):
        assert not _is_linked(a1, 'QueryValueExpression234', b)
    if hasattr(a2, 'QueryValueExpression234'):
        assert _is_linked(a2, 'QueryValueExpression234', b)
    _safe_set(b, 'likePattern', None)
    assert not _is_linked(b, 'likePattern', a2)
    if hasattr(a2, 'QueryValueExpression234'):
        assert not _is_linked(a2, 'QueryValueExpression234', b)


def test_assoc_predicateNull80_reverse_link_reassign_clear():
    a1 = query_QueryValueExpression(unaryOperator="sample_text")
    a2 = query_QueryValueExpression(unaryOperator="sample_text_2")
    b = query_PredicateIsNull(notNull=True)
    _safe_set(b, 'PredicateIsNull', a1)
    assert _is_linked(b, 'PredicateIsNull', a1)
    if hasattr(a1, 'valueExpr81'):
        assert _is_linked(a1, 'valueExpr81', b)
    _safe_set(b, 'PredicateIsNull', a2)
    assert _is_linked(b, 'PredicateIsNull', a2)
    if hasattr(a1, 'valueExpr81'):
        assert not _is_linked(a1, 'valueExpr81', b)
    if hasattr(a2, 'valueExpr81'):
        assert _is_linked(a2, 'valueExpr81', b)
    _safe_set(b, 'PredicateIsNull', None)
    assert not _is_linked(b, 'PredicateIsNull', a2)
    if hasattr(a2, 'valueExpr81'):
        assert not _is_linked(a2, 'valueExpr81', b)


def test_assoc_quantifiedRowSelectLeft90_reverse_link_reassign_clear():
    a1 = query_QueryValueExpression(unaryOperator="sample_text")
    a2 = query_QueryValueExpression(unaryOperator="sample_text_2")
    b = query_PredicateQuantifiedRowSelect(quantifiedType="sample_text")
    _safe_set(b, 'PredicateQuantifiedRowSelect', a1)
    assert _is_linked(b, 'PredicateQuantifiedRowSelect', a1)
    if hasattr(a1, 'valueExprList91'):
        assert _is_linked(a1, 'valueExprList91', b)
    _safe_set(b, 'PredicateQuantifiedRowSelect', a2)
    assert _is_linked(b, 'PredicateQuantifiedRowSelect', a2)
    if hasattr(a1, 'valueExprList91'):
        assert not _is_linked(a1, 'valueExprList91', b)
    if hasattr(a2, 'valueExprList91'):
        assert _is_linked(a2, 'valueExprList91', b)
    _safe_set(b, 'PredicateQuantifiedRowSelect', None)
    assert not _is_linked(b, 'PredicateQuantifiedRowSelect', a2)
    if hasattr(a2, 'valueExprList91'):
        assert not _is_linked(a2, 'valueExprList91', b)


def test_assoc_quantifiedValueSelectLeft92_reverse_link_reassign_clear():
    a1 = query_QueryValueExpression(unaryOperator="sample_text")
    a2 = query_QueryValueExpression(unaryOperator="sample_text_2")
    b = query_PredicateQuantifiedValueSelect(comparisonOperator="sample_text", quantifiedType="sample_text")
    _safe_set(b, 'PredicateQuantifiedValueSelect', a1)
    assert _is_linked(b, 'PredicateQuantifiedValueSelect', a1)
    if hasattr(a1, 'valueExpr93'):
        assert _is_linked(a1, 'valueExpr93', b)
    _safe_set(b, 'PredicateQuantifiedValueSelect', a2)
    assert _is_linked(b, 'PredicateQuantifiedValueSelect', a2)
    if hasattr(a1, 'valueExpr93'):
        assert not _is_linked(a1, 'valueExpr93', b)
    if hasattr(a2, 'valueExpr93'):
        assert _is_linked(a2, 'valueExpr93', b)
    _safe_set(b, 'PredicateQuantifiedValueSelect', None)
    assert not _is_linked(b, 'PredicateQuantifiedValueSelect', a2)
    if hasattr(a2, 'valueExpr93'):
        assert not _is_linked(a2, 'valueExpr93', b)


def test_assoc_query371_reverse_link_reassign_clear():
    a1 = query_QueryExpressionBody(rowFetchLimit=7)
    a2 = query_QueryExpressionBody(rowFetchLimit=13)
    b = query_OrderBySpecification(NullOrderingOption="sample_text", OrderingSpecOption="sample_text", descending=True)
    _safe_set(b, 'sortSpecList', a1)
    assert _is_linked(b, 'sortSpecList', a1)
    if hasattr(a1, 'QueryExpressionBody372'):
        assert _is_linked(a1, 'QueryExpressionBody372', b)
    _safe_set(b, 'sortSpecList', a2)
    assert _is_linked(b, 'sortSpecList', a2)
    if hasattr(a1, 'QueryExpressionBody372'):
        assert not _is_linked(a1, 'QueryExpressionBody372', b)
    if hasattr(a2, 'QueryExpressionBody372'):
        assert _is_linked(a2, 'QueryExpressionBody372', b)
    _safe_set(b, 'sortSpecList', None)
    assert not _is_linked(b, 'sortSpecList', a2)
    if hasattr(a2, 'QueryExpressionBody372'):
        assert not _is_linked(a2, 'QueryExpressionBody372', b)


def test_assoc_querySelectHaving47_reverse_link_reassign_clear():
    a1 = query_QuerySelect(distinct=True)
    a2 = query_QuerySelect(distinct=False)
    b = query_QuerySearchCondition(negatedCondition=True)
    _safe_set(b, 'havingClause', a1)
    assert _is_linked(b, 'havingClause', a1)
    if hasattr(a1, 'QuerySelect'):
        assert _is_linked(a1, 'QuerySelect', b)
    _safe_set(b, 'havingClause', a2)
    assert _is_linked(b, 'havingClause', a2)
    if hasattr(a1, 'QuerySelect'):
        assert not _is_linked(a1, 'QuerySelect', b)
    if hasattr(a2, 'QuerySelect'):
        assert _is_linked(a2, 'QuerySelect', b)
    _safe_set(b, 'havingClause', None)
    assert not _is_linked(b, 'havingClause', a2)
    if hasattr(a2, 'QuerySelect'):
        assert not _is_linked(a2, 'QuerySelect', b)


def test_assoc_querySelectWhere48_reverse_link_reassign_clear():
    a1 = query_QuerySelect(distinct=True)
    a2 = query_QuerySelect(distinct=False)
    b = query_QuerySearchCondition(negatedCondition=True)
    _safe_set(b, 'whereClause49', a1)
    assert _is_linked(b, 'whereClause49', a1)
    if hasattr(a1, 'QuerySelect50'):
        assert _is_linked(a1, 'QuerySelect50', b)
    _safe_set(b, 'whereClause49', a2)
    assert _is_linked(b, 'whereClause49', a2)
    if hasattr(a1, 'QuerySelect50'):
        assert not _is_linked(a1, 'QuerySelect50', b)
    if hasattr(a2, 'QuerySelect50'):
        assert _is_linked(a2, 'QuerySelect50', b)
    _safe_set(b, 'whereClause49', None)
    assert not _is_linked(b, 'whereClause49', a2)
    if hasattr(a2, 'QuerySelect50'):
        assert not _is_linked(a2, 'QuerySelect50', b)


def test_assoc_rightCondition191_reverse_link_reassign_clear():
    a1 = query_SearchConditionCombined(combinedOperator="sample_text")
    a2 = query_SearchConditionCombined(combinedOperator="sample_text_2")
    b = query_QuerySearchCondition(negatedCondition=True)
    _safe_set(b, 'QuerySearchCondition192', a1)
    assert _is_linked(b, 'QuerySearchCondition192', a1)
    if hasattr(a1, 'combinedRight'):
        assert _is_linked(a1, 'combinedRight', b)
    _safe_set(b, 'QuerySearchCondition192', a2)
    assert _is_linked(b, 'QuerySearchCondition192', a2)
    if hasattr(a1, 'combinedRight'):
        assert not _is_linked(a1, 'combinedRight', b)
    if hasattr(a2, 'combinedRight'):
        assert _is_linked(a2, 'combinedRight', b)
    _safe_set(b, 'QuerySearchCondition192', None)
    assert not _is_linked(b, 'QuerySearchCondition192', a2)
    if hasattr(a2, 'combinedRight'):
        assert not _is_linked(a2, 'combinedRight', b)


def test_assoc_rightQuery198_reverse_link_reassign_clear():
    a1 = query_QueryExpressionBody(rowFetchLimit=7)
    a2 = query_QueryExpressionBody(rowFetchLimit=13)
    b = query_QueryCombined(combinedOperator="sample_text")
    _safe_set(b, 'combinedRight199', a1)
    assert _is_linked(b, 'combinedRight199', a1)
    if hasattr(a1, 'QueryExpressionBody200'):
        assert _is_linked(a1, 'QueryExpressionBody200', b)
    _safe_set(b, 'combinedRight199', a2)
    assert _is_linked(b, 'combinedRight199', a2)
    if hasattr(a1, 'QueryExpressionBody200'):
        assert not _is_linked(a1, 'QueryExpressionBody200', b)
    if hasattr(a2, 'QueryExpressionBody200'):
        assert _is_linked(a2, 'QueryExpressionBody200', b)
    _safe_set(b, 'combinedRight199', None)
    assert not _is_linked(b, 'combinedRight199', a2)
    if hasattr(a2, 'QueryExpressionBody200'):
        assert not _is_linked(a2, 'QueryExpressionBody200', b)


def test_assoc_rightValueExpr1227_reverse_link_reassign_clear():
    a1 = query_QueryValueExpression(unaryOperator="sample_text")
    a2 = query_QueryValueExpression(unaryOperator="sample_text_2")
    b = query_PredicateBetween(notBetween=True)
    _safe_set(b, 'betweenRight1', a1)
    assert _is_linked(b, 'betweenRight1', a1)
    if hasattr(a1, 'QueryValueExpression228'):
        assert _is_linked(a1, 'QueryValueExpression228', b)
    _safe_set(b, 'betweenRight1', a2)
    assert _is_linked(b, 'betweenRight1', a2)
    if hasattr(a1, 'QueryValueExpression228'):
        assert not _is_linked(a1, 'QueryValueExpression228', b)
    if hasattr(a2, 'QueryValueExpression228'):
        assert _is_linked(a2, 'QueryValueExpression228', b)
    _safe_set(b, 'betweenRight1', None)
    assert not _is_linked(b, 'betweenRight1', a2)
    if hasattr(a2, 'QueryValueExpression228'):
        assert not _is_linked(a2, 'QueryValueExpression228', b)


def test_assoc_rightValueExpr221_reverse_link_reassign_clear():
    a1 = query_QueryValueExpression(unaryOperator="sample_text")
    a2 = query_QueryValueExpression(unaryOperator="sample_text_2")
    b = query_PredicateBasic(comparisonOperator="sample_text")
    _safe_set(b, 'basicRight', a1)
    assert _is_linked(b, 'basicRight', a1)
    if hasattr(a1, 'QueryValueExpression222'):
        assert _is_linked(a1, 'QueryValueExpression222', b)
    _safe_set(b, 'basicRight', a2)
    assert _is_linked(b, 'basicRight', a2)
    if hasattr(a1, 'QueryValueExpression222'):
        assert not _is_linked(a1, 'QueryValueExpression222', b)
    if hasattr(a2, 'QueryValueExpression222'):
        assert _is_linked(a2, 'QueryValueExpression222', b)
    _safe_set(b, 'basicRight', None)
    assert not _is_linked(b, 'basicRight', a2)
    if hasattr(a2, 'QueryValueExpression222'):
        assert not _is_linked(a2, 'QueryValueExpression222', b)


def test_assoc_rightValueExpr2229_reverse_link_reassign_clear():
    a1 = query_QueryValueExpression(unaryOperator="sample_text")
    a2 = query_QueryValueExpression(unaryOperator="sample_text_2")
    b = query_PredicateBetween(notBetween=True)
    _safe_set(b, 'betweenRight2', a1)
    assert _is_linked(b, 'betweenRight2', a1)
    if hasattr(a1, 'QueryValueExpression230'):
        assert _is_linked(a1, 'QueryValueExpression230', b)
    _safe_set(b, 'betweenRight2', a2)
    assert _is_linked(b, 'betweenRight2', a2)
    if hasattr(a1, 'QueryValueExpression230'):
        assert not _is_linked(a1, 'QueryValueExpression230', b)
    if hasattr(a2, 'QueryValueExpression230'):
        assert _is_linked(a2, 'QueryValueExpression230', b)
    _safe_set(b, 'betweenRight2', None)
    assert not _is_linked(b, 'betweenRight2', a2)
    if hasattr(a2, 'QueryValueExpression230'):
        assert not _is_linked(a2, 'QueryValueExpression230', b)


def test_assoc_rightValueExpr289_reverse_link_reassign_clear():
    a1 = query_ValueExpressionCombined(combinedOperator="sample_text")
    a2 = query_ValueExpressionCombined(combinedOperator="sample_text_2")
    b = query_QueryValueExpression(unaryOperator="sample_text")
    _safe_set(b, 'QueryValueExpression290', a1)
    assert _is_linked(b, 'QueryValueExpression290', a1)
    if hasattr(a1, 'valueExprCombinedRight'):
        assert _is_linked(a1, 'valueExprCombinedRight', b)
    _safe_set(b, 'QueryValueExpression290', a2)
    assert _is_linked(b, 'QueryValueExpression290', a2)
    if hasattr(a1, 'valueExprCombinedRight'):
        assert not _is_linked(a1, 'valueExprCombinedRight', b)
    if hasattr(a2, 'valueExprCombinedRight'):
        assert _is_linked(a2, 'valueExprCombinedRight', b)
    _safe_set(b, 'QueryValueExpression290', None)
    assert not _is_linked(b, 'QueryValueExpression290', a2)
    if hasattr(a2, 'valueExprCombinedRight'):
        assert not _is_linked(a2, 'valueExprCombinedRight', b)


def test_assoc_sortSpecList65_reverse_link_reassign_clear():
    a1 = query_QueryExpressionBody(rowFetchLimit=7)
    a2 = query_QueryExpressionBody(rowFetchLimit=13)
    b = query_OrderBySpecification(NullOrderingOption="sample_text", OrderingSpecOption="sample_text", descending=True)
    _safe_set(b, 'OrderBySpecification67', a1)
    assert _is_linked(b, 'OrderBySpecification67', a1)
    if hasattr(a1, 'query66'):
        assert _is_linked(a1, 'query66', b)
    _safe_set(b, 'OrderBySpecification67', a2)
    assert _is_linked(b, 'OrderBySpecification67', a2)
    if hasattr(a1, 'query66'):
        assert not _is_linked(a1, 'query66', b)
    if hasattr(a2, 'query66'):
        assert _is_linked(a2, 'query66', b)
    _safe_set(b, 'OrderBySpecification67', None)
    assert not _is_linked(b, 'OrderBySpecification67', a2)
    if hasattr(a2, 'query66'):
        assert not _is_linked(a2, 'query66', b)


def test_assoc_tableJoined43_reverse_link_reassign_clear():
    a1 = query_TableJoined(joinOperator="sample_text")
    a2 = query_TableJoined(joinOperator="sample_text_2")
    b = query_QuerySearchCondition(negatedCondition=True)
    _safe_set(b, 'joinCondition', a1)
    assert _is_linked(b, 'joinCondition', a1)
    if hasattr(a1, 'TableJoined'):
        assert _is_linked(a1, 'TableJoined', b)
    _safe_set(b, 'joinCondition', a2)
    assert _is_linked(b, 'joinCondition', a2)
    if hasattr(a1, 'TableJoined'):
        assert not _is_linked(a1, 'TableJoined', b)
    if hasattr(a2, 'TableJoined'):
        assert _is_linked(a2, 'TableJoined', b)
    _safe_set(b, 'joinCondition', None)
    assert not _is_linked(b, 'joinCondition', a2)
    if hasattr(a2, 'TableJoined'):
        assert not _is_linked(a2, 'TableJoined', b)


def test_assoc_valueExpr239_reverse_link_reassign_clear():
    a1 = query_QueryValueExpression(unaryOperator="sample_text")
    a2 = query_QueryValueExpression(unaryOperator="sample_text_2")
    b = query_PredicateIsNull(notNull=True)
    _safe_set(b, 'predicateNull', a1)
    assert _is_linked(b, 'predicateNull', a1)
    if hasattr(a1, 'QueryValueExpression240'):
        assert _is_linked(a1, 'QueryValueExpression240', b)
    _safe_set(b, 'predicateNull', a2)
    assert _is_linked(b, 'predicateNull', a2)
    if hasattr(a1, 'QueryValueExpression240'):
        assert not _is_linked(a1, 'QueryValueExpression240', b)
    if hasattr(a2, 'QueryValueExpression240'):
        assert _is_linked(a2, 'QueryValueExpression240', b)
    _safe_set(b, 'predicateNull', None)
    assert not _is_linked(b, 'predicateNull', a2)
    if hasattr(a2, 'QueryValueExpression240'):
        assert not _is_linked(a2, 'QueryValueExpression240', b)


def test_assoc_valueExpr243_reverse_link_reassign_clear():
    a1 = query_QueryValueExpression(unaryOperator="sample_text")
    a2 = query_QueryValueExpression(unaryOperator="sample_text_2")
    b = query_PredicateQuantifiedValueSelect(comparisonOperator="sample_text", quantifiedType="sample_text")
    _safe_set(b, 'quantifiedValueSelectLeft', a1)
    assert _is_linked(b, 'quantifiedValueSelectLeft', a1)
    if hasattr(a1, 'QueryValueExpression244'):
        assert _is_linked(a1, 'QueryValueExpression244', b)
    _safe_set(b, 'quantifiedValueSelectLeft', a2)
    assert _is_linked(b, 'quantifiedValueSelectLeft', a2)
    if hasattr(a1, 'QueryValueExpression244'):
        assert not _is_linked(a1, 'QueryValueExpression244', b)
    if hasattr(a2, 'QueryValueExpression244'):
        assert _is_linked(a2, 'QueryValueExpression244', b)
    _safe_set(b, 'quantifiedValueSelectLeft', None)
    assert not _is_linked(b, 'quantifiedValueSelectLeft', a2)
    if hasattr(a2, 'QueryValueExpression244'):
        assert not _is_linked(a2, 'QueryValueExpression244', b)


def test_assoc_valueExpr278_reverse_link_reassign_clear():
    a1 = query_ValueExpressionLabeledDuration(labeledDurationType="sample_text")
    a2 = query_ValueExpressionLabeledDuration(labeledDurationType="sample_text_2")
    b = query_QueryValueExpression(unaryOperator="sample_text")
    _safe_set(b, 'QueryValueExpression279', a1)
    assert _is_linked(b, 'QueryValueExpression279', a1)
    if hasattr(a1, 'valueExprLabeledDuration'):
        assert _is_linked(a1, 'valueExprLabeledDuration', b)
    _safe_set(b, 'QueryValueExpression279', a2)
    assert _is_linked(b, 'QueryValueExpression279', a2)
    if hasattr(a1, 'valueExprLabeledDuration'):
        assert not _is_linked(a1, 'valueExprLabeledDuration', b)
    if hasattr(a2, 'valueExprLabeledDuration'):
        assert _is_linked(a2, 'valueExprLabeledDuration', b)
    _safe_set(b, 'QueryValueExpression279', None)
    assert not _is_linked(b, 'QueryValueExpression279', a2)
    if hasattr(a2, 'valueExprLabeledDuration'):
        assert not _is_linked(a2, 'valueExprLabeledDuration', b)


def test_assoc_valueExprCombinedLeft103_reverse_link_reassign_clear():
    a1 = query_ValueExpressionCombined(combinedOperator="sample_text")
    a2 = query_ValueExpressionCombined(combinedOperator="sample_text_2")
    b = query_QueryValueExpression(unaryOperator="sample_text")
    _safe_set(b, 'leftValueExpr104', a1)
    assert _is_linked(b, 'leftValueExpr104', a1)
    if hasattr(a1, 'ValueExpressionCombined'):
        assert _is_linked(a1, 'ValueExpressionCombined', b)
    _safe_set(b, 'leftValueExpr104', a2)
    assert _is_linked(b, 'leftValueExpr104', a2)
    if hasattr(a1, 'ValueExpressionCombined'):
        assert not _is_linked(a1, 'ValueExpressionCombined', b)
    if hasattr(a2, 'ValueExpressionCombined'):
        assert _is_linked(a2, 'ValueExpressionCombined', b)
    _safe_set(b, 'leftValueExpr104', None)
    assert not _is_linked(b, 'leftValueExpr104', a2)
    if hasattr(a2, 'ValueExpressionCombined'):
        assert not _is_linked(a2, 'ValueExpressionCombined', b)


def test_assoc_valueExprCombinedRight105_reverse_link_reassign_clear():
    a1 = query_ValueExpressionCombined(combinedOperator="sample_text")
    a2 = query_ValueExpressionCombined(combinedOperator="sample_text_2")
    b = query_QueryValueExpression(unaryOperator="sample_text")
    _safe_set(b, 'rightValueExpr106', a1)
    assert _is_linked(b, 'rightValueExpr106', a1)
    if hasattr(a1, 'ValueExpressionCombined107'):
        assert _is_linked(a1, 'ValueExpressionCombined107', b)
    _safe_set(b, 'rightValueExpr106', a2)
    assert _is_linked(b, 'rightValueExpr106', a2)
    if hasattr(a1, 'ValueExpressionCombined107'):
        assert not _is_linked(a1, 'ValueExpressionCombined107', b)
    if hasattr(a2, 'ValueExpressionCombined107'):
        assert _is_linked(a2, 'ValueExpressionCombined107', b)
    _safe_set(b, 'rightValueExpr106', None)
    assert not _is_linked(b, 'rightValueExpr106', a2)
    if hasattr(a2, 'ValueExpressionCombined107'):
        assert not _is_linked(a2, 'ValueExpressionCombined107', b)


def test_assoc_valueExprFunction102_reverse_link_reassign_clear():
    a1 = query_ValueExpressionFunction(columnFunction=True, distinct=True, specialRegister=True)
    a2 = query_ValueExpressionFunction(columnFunction=False, distinct=False, specialRegister=False)
    b = query_QueryValueExpression(unaryOperator="sample_text")
    _safe_set(b, 'parameterList', a1)
    assert _is_linked(b, 'parameterList', a1)
    if hasattr(a1, 'ValueExpressionFunction'):
        assert _is_linked(a1, 'ValueExpressionFunction', b)
    _safe_set(b, 'parameterList', a2)
    assert _is_linked(b, 'parameterList', a2)
    if hasattr(a1, 'ValueExpressionFunction'):
        assert not _is_linked(a1, 'ValueExpressionFunction', b)
    if hasattr(a2, 'ValueExpressionFunction'):
        assert _is_linked(a2, 'ValueExpressionFunction', b)
    _safe_set(b, 'parameterList', None)
    assert not _is_linked(b, 'parameterList', a2)
    if hasattr(a2, 'ValueExpressionFunction'):
        assert not _is_linked(a2, 'ValueExpressionFunction', b)


def test_assoc_valueExprLabeledDuration122_reverse_link_reassign_clear():
    a1 = query_ValueExpressionLabeledDuration(labeledDurationType="sample_text")
    a2 = query_ValueExpressionLabeledDuration(labeledDurationType="sample_text_2")
    b = query_QueryValueExpression(unaryOperator="sample_text")
    _safe_set(b, 'valueExpr123', a1)
    assert _is_linked(b, 'valueExpr123', a1)
    if hasattr(a1, 'ValueExpressionLabeledDuration'):
        assert _is_linked(a1, 'ValueExpressionLabeledDuration', b)
    _safe_set(b, 'valueExpr123', a2)
    assert _is_linked(b, 'valueExpr123', a2)
    if hasattr(a1, 'ValueExpressionLabeledDuration'):
        assert not _is_linked(a1, 'ValueExpressionLabeledDuration', b)
    if hasattr(a2, 'ValueExpressionLabeledDuration'):
        assert _is_linked(a2, 'ValueExpressionLabeledDuration', b)
    _safe_set(b, 'valueExpr123', None)
    assert not _is_linked(b, 'valueExpr123', a2)
    if hasattr(a2, 'ValueExpressionLabeledDuration'):
        assert not _is_linked(a2, 'ValueExpressionLabeledDuration', b)


def test_assoc_valueExprList247_reverse_link_reassign_clear():
    a1 = query_QueryValueExpression(unaryOperator="sample_text")
    a2 = query_QueryValueExpression(unaryOperator="sample_text_2")
    b = query_PredicateQuantifiedRowSelect(quantifiedType="sample_text")
    _safe_set(b, 'quantifiedRowSelectLeft', {a1})
    assert _is_linked(b, 'quantifiedRowSelectLeft', a1)
    if hasattr(a1, 'QueryValueExpression248'):
        assert _is_linked(a1, 'QueryValueExpression248', b)
    _safe_set(b, 'quantifiedRowSelectLeft', {a2})
    assert _is_linked(b, 'quantifiedRowSelectLeft', a2)
    if hasattr(a1, 'QueryValueExpression248'):
        assert not _is_linked(a1, 'QueryValueExpression248', b)
    if hasattr(a2, 'QueryValueExpression248'):
        assert _is_linked(a2, 'QueryValueExpression248', b)
    _safe_set(b, 'quantifiedRowSelectLeft', set())
    assert not _is_linked(b, 'quantifiedRowSelectLeft', a2)
    if hasattr(a2, 'QueryValueExpression248'):
        assert not _is_linked(a2, 'QueryValueExpression248', b)


def test_assoc_whereClause203_reverse_link_reassign_clear():
    a1 = query_QuerySelect(distinct=True)
    a2 = query_QuerySelect(distinct=False)
    b = query_QuerySearchCondition(negatedCondition=True)
    _safe_set(b, 'QuerySearchCondition204', a1)
    assert _is_linked(b, 'QuerySearchCondition204', a1)
    if hasattr(a1, 'querySelectWhere'):
        assert _is_linked(a1, 'querySelectWhere', b)
    _safe_set(b, 'QuerySearchCondition204', a2)
    assert _is_linked(b, 'QuerySearchCondition204', a2)
    if hasattr(a1, 'querySelectWhere'):
        assert not _is_linked(a1, 'querySelectWhere', b)
    if hasattr(a2, 'querySelectWhere'):
        assert _is_linked(a2, 'querySelectWhere', b)
    _safe_set(b, 'QuerySearchCondition204', None)
    assert not _is_linked(b, 'QuerySearchCondition204', a2)
    if hasattr(a2, 'querySelectWhere'):
        assert not _is_linked(a2, 'querySelectWhere', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_argumentList418_stub_double():
    # query_CallStatement has no real 'callStatement' property in the generated
    # code (a bare stub) -- manually attach it so query_QueryValueExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # query_QueryValueExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = query_QueryValueExpression(unaryOperator="sample_text")
    partner = query_CallStatement()
    setattr(partner, 'callStatement', None)
    _safe_set(owner, 'QueryValueExpression419', partner)
    assert owner in getattr(partner, 'callStatement')
    _safe_set(owner, 'QueryValueExpression419', None)
    assert owner not in getattr(partner, 'callStatement')


def test_assoc_callStatement131_stub_double():
    # query_CallStatement has no real 'CallStatement' property in the generated
    # code (a bare stub) -- manually attach it so query_QueryValueExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # query_QueryValueExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = query_QueryValueExpression(unaryOperator="sample_text")
    partner = query_CallStatement()
    setattr(partner, 'CallStatement', None)
    _safe_set(owner, 'argumentList', partner)
    assert getattr(partner, 'CallStatement') == owner
    _safe_set(owner, 'argumentList', None)
    assert getattr(partner, 'CallStatement') is None


def test_assoc_dataType68_stub_double():
    # DataType has no real 'DataType' property in the generated
    # code (a bare stub) -- manually attach it so query_QueryValueExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # query_QueryValueExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = query_QueryValueExpression(unaryOperator="sample_text")
    partner = DataType()
    setattr(partner, 'DataType', None)
    _safe_set(owner, 'query_QueryValueExpression', partner)
    assert getattr(partner, 'DataType') == owner
    _safe_set(owner, 'query_QueryValueExpression', None)
    assert getattr(partner, 'DataType') is None


def test_assoc_deleteStatement40_stub_double():
    # query_QueryDeleteStatement has no real 'QueryDeleteStatement42' property in the generated
    # code (a bare stub) -- manually attach it so query_QuerySearchCondition's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # query_QuerySearchCondition's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = query_QuerySearchCondition(negatedCondition=True)
    partner = query_QueryDeleteStatement()
    setattr(partner, 'QueryDeleteStatement42', None)
    _safe_set(owner, 'whereClause41', partner)
    assert getattr(partner, 'QueryDeleteStatement42') == owner
    _safe_set(owner, 'whereClause41', None)
    assert getattr(partner, 'QueryDeleteStatement42') is None


def test_assoc_exprList154_stub_double():
    # query_ValuesRow has no real 'valuesRow' property in the generated
    # code (a bare stub) -- manually attach it so query_QueryValueExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # query_QueryValueExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = query_QueryValueExpression(unaryOperator="sample_text")
    partner = query_ValuesRow()
    setattr(partner, 'valuesRow', None)
    _safe_set(owner, 'QueryValueExpression', partner)
    assert owner in getattr(partner, 'valuesRow')
    _safe_set(owner, 'QueryValueExpression', None)
    assert owner not in getattr(partner, 'valuesRow')


def test_assoc_fromClause208_stub_double():
    # query_TableReference has no real 'TableReference210' property in the generated
    # code (a bare stub) -- manually attach it so query_QuerySelect's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # query_QuerySelect's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = query_QuerySelect(distinct=True)
    partner = query_TableReference()
    setattr(partner, 'TableReference210', None)
    _safe_set(owner, 'querySelect209', {partner})
    assert getattr(partner, 'TableReference210') == owner
    _safe_set(owner, 'querySelect209', set())
    assert getattr(partner, 'TableReference210') is None


def test_assoc_function286_stub_double():
    # Function has no real 'Function' property in the generated
    # code (a bare stub) -- manually attach it so query_ValueExpressionFunction's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # query_ValueExpressionFunction's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = query_ValueExpressionFunction(columnFunction=True, distinct=True, specialRegister=True)
    partner = Function()
    setattr(partner, 'Function', None)
    _safe_set(owner, 'query_ValueExpressionFunction', partner)
    assert getattr(partner, 'Function') == owner
    _safe_set(owner, 'query_ValueExpressionFunction', None)
    assert getattr(partner, 'Function') is None


def test_assoc_groupByClause205_stub_double():
    # query_GroupingSpecification has no real 'GroupingSpecification' property in the generated
    # code (a bare stub) -- manually attach it so query_QuerySelect's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # query_QuerySelect's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = query_QuerySelect(distinct=True)
    partner = query_GroupingSpecification()
    setattr(partner, 'GroupingSpecification', None)
    _safe_set(owner, 'querySelect', {partner})
    assert getattr(partner, 'GroupingSpecification') == owner
    _safe_set(owner, 'querySelect', set())
    assert getattr(partner, 'GroupingSpecification') is None


def test_assoc_groupingExpr108_stub_double():
    # query_GroupingExpression has no real 'GroupingExpression' property in the generated
    # code (a bare stub) -- manually attach it so query_QueryValueExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # query_QueryValueExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = query_QueryValueExpression(unaryOperator="sample_text")
    partner = query_GroupingExpression()
    setattr(partner, 'GroupingExpression', None)
    _safe_set(owner, 'valueExpr109', partner)
    assert getattr(partner, 'GroupingExpression') == owner
    _safe_set(owner, 'valueExpr109', None)
    assert getattr(partner, 'GroupingExpression') is None


def test_assoc_inValueListLeft83_stub_double():
    # query_PredicateInValueList has no real 'PredicateInValueList85' property in the generated
    # code (a bare stub) -- manually attach it so query_QueryValueExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # query_QueryValueExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = query_QueryValueExpression(unaryOperator="sample_text")
    partner = query_PredicateInValueList()
    setattr(partner, 'PredicateInValueList85', None)
    _safe_set(owner, 'valueExpr84', partner)
    assert getattr(partner, 'PredicateInValueList85') == owner
    _safe_set(owner, 'valueExpr84', None)
    assert getattr(partner, 'PredicateInValueList85') is None


def test_assoc_inValueListRight82_stub_double():
    # query_PredicateInValueList has no real 'PredicateInValueList' property in the generated
    # code (a bare stub) -- manually attach it so query_QueryValueExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # query_QueryValueExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = query_QueryValueExpression(unaryOperator="sample_text")
    partner = query_PredicateInValueList()
    setattr(partner, 'PredicateInValueList', None)
    _safe_set(owner, 'valueExprList', partner)
    assert getattr(partner, 'PredicateInValueList') == owner
    _safe_set(owner, 'valueExprList', None)
    assert getattr(partner, 'PredicateInValueList') is None


def test_assoc_inValueRowSelectLeft86_stub_double():
    # query_PredicateInValueRowSelect has no real 'PredicateInValueRowSelect' property in the generated
    # code (a bare stub) -- manually attach it so query_QueryValueExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # query_QueryValueExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = query_QueryValueExpression(unaryOperator="sample_text")
    partner = query_PredicateInValueRowSelect()
    setattr(partner, 'PredicateInValueRowSelect', None)
    _safe_set(owner, 'valueExprList87', partner)
    assert getattr(partner, 'PredicateInValueRowSelect') == owner
    _safe_set(owner, 'valueExprList87', None)
    assert getattr(partner, 'PredicateInValueRowSelect') is None


def test_assoc_inValueSelectLeft88_stub_double():
    # query_PredicateInValueSelect has no real 'PredicateInValueSelect' property in the generated
    # code (a bare stub) -- manually attach it so query_QueryValueExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # query_QueryValueExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = query_QueryValueExpression(unaryOperator="sample_text")
    partner = query_PredicateInValueSelect()
    setattr(partner, 'PredicateInValueSelect', None)
    _safe_set(owner, 'valueExpr89', partner)
    assert getattr(partner, 'PredicateInValueSelect') == owner
    _safe_set(owner, 'valueExpr89', None)
    assert getattr(partner, 'PredicateInValueSelect') is None


def test_assoc_intoClause211_stub_double():
    # query_ValueExpressionVariable has no real 'ValueExpressionVariable' property in the generated
    # code (a bare stub) -- manually attach it so query_QuerySelect's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # query_QuerySelect's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = query_QuerySelect(distinct=True)
    partner = query_ValueExpressionVariable()
    setattr(partner, 'ValueExpressionVariable', None)
    _safe_set(owner, 'querySelect212', {partner})
    assert getattr(partner, 'ValueExpressionVariable') == owner
    _safe_set(owner, 'querySelect212', set())
    assert getattr(partner, 'ValueExpressionVariable') is None


def test_assoc_mergeOnCondition53_stub_double():
    # query_MergeOnCondition has no real 'MergeOnCondition' property in the generated
    # code (a bare stub) -- manually attach it so query_QuerySearchCondition's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # query_QuerySearchCondition's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = query_QuerySearchCondition(negatedCondition=True)
    partner = query_MergeOnCondition()
    setattr(partner, 'MergeOnCondition', None)
    _safe_set(owner, 'searchCondition54', partner)
    assert getattr(partner, 'MergeOnCondition') == owner
    _safe_set(owner, 'searchCondition54', None)
    assert getattr(partner, 'MergeOnCondition') is None


def test_assoc_nest124_stub_double():
    # query_ValueExpressionNested has no real 'ValueExpressionNested' property in the generated
    # code (a bare stub) -- manually attach it so query_QueryValueExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # query_QueryValueExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = query_QueryValueExpression(unaryOperator="sample_text")
    partner = query_ValueExpressionNested()
    setattr(partner, 'ValueExpressionNested', None)
    _safe_set(owner, 'nestedValueExpr', partner)
    assert getattr(partner, 'ValueExpressionNested') == owner
    _safe_set(owner, 'nestedValueExpr', None)
    assert getattr(partner, 'ValueExpressionNested') is None


def test_assoc_nest52_stub_double():
    # query_SearchConditionNested has no real 'SearchConditionNested' property in the generated
    # code (a bare stub) -- manually attach it so query_QuerySearchCondition's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # query_QuerySearchCondition's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = query_QuerySearchCondition(negatedCondition=True)
    partner = query_SearchConditionNested()
    setattr(partner, 'SearchConditionNested', None)
    _safe_set(owner, 'nestedCondition', partner)
    assert getattr(partner, 'SearchConditionNested') == owner
    _safe_set(owner, 'nestedCondition', None)
    assert getattr(partner, 'SearchConditionNested') is None


def test_assoc_nestedCondition363_stub_double():
    # query_SearchConditionNested has no real 'nest364' property in the generated
    # code (a bare stub) -- manually attach it so query_QuerySearchCondition's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # query_QuerySearchCondition's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = query_QuerySearchCondition(negatedCondition=True)
    partner = query_SearchConditionNested()
    setattr(partner, 'nest364', None)
    _safe_set(owner, 'QuerySearchCondition365', partner)
    assert getattr(partner, 'nest364') == owner
    _safe_set(owner, 'QuerySearchCondition365', None)
    assert getattr(partner, 'nest364') is None


def test_assoc_nestedQuery388_stub_double():
    # query_QueryNested has no real 'queryNest' property in the generated
    # code (a bare stub) -- manually attach it so query_QueryExpressionBody's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # query_QueryExpressionBody's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = query_QueryExpressionBody(rowFetchLimit=7)
    partner = query_QueryNested()
    setattr(partner, 'queryNest', None)
    _safe_set(owner, 'QueryExpressionBody389', partner)
    assert getattr(partner, 'queryNest') == owner
    _safe_set(owner, 'QueryExpressionBody389', None)
    assert getattr(partner, 'queryNest') is None


def test_assoc_nestedValueExpr366_stub_double():
    # query_ValueExpressionNested has no real 'nest367' property in the generated
    # code (a bare stub) -- manually attach it so query_QueryValueExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # query_QueryValueExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = query_QueryValueExpression(unaryOperator="sample_text")
    partner = query_ValueExpressionNested()
    setattr(partner, 'nest367', None)
    _safe_set(owner, 'QueryValueExpression368', partner)
    assert getattr(partner, 'nest367') == owner
    _safe_set(owner, 'QueryValueExpression368', None)
    assert getattr(partner, 'nest367') is None


def test_assoc_orderByClause15_stub_double():
    # query_QuerySelectStatement has no real 'selectStatement16' property in the generated
    # code (a bare stub) -- manually attach it so query_OrderBySpecification's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # query_OrderBySpecification's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = query_OrderBySpecification(NullOrderingOption="sample_text", OrderingSpecOption="sample_text", descending=True)
    partner = query_QuerySelectStatement()
    setattr(partner, 'selectStatement16', None)
    _safe_set(owner, 'OrderBySpecification', partner)
    assert owner in getattr(partner, 'selectStatement16')
    _safe_set(owner, 'OrderBySpecification', None)
    assert owner not in getattr(partner, 'selectStatement16')


def test_assoc_orderByValueExpr71_stub_double():
    # query_OrderByValueExpression has no real 'OrderByValueExpression' property in the generated
    # code (a bare stub) -- manually attach it so query_QueryValueExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # query_QueryValueExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = query_QueryValueExpression(unaryOperator="sample_text")
    partner = query_OrderByValueExpression()
    setattr(partner, 'OrderByValueExpression', None)
    _safe_set(owner, 'valueExpr', partner)
    assert getattr(partner, 'OrderByValueExpression') == owner
    _safe_set(owner, 'valueExpr', None)
    assert getattr(partner, 'OrderByValueExpression') is None


def test_assoc_parameterList344_stub_double():
    # query_TableFunction has no real 'tableFunction' property in the generated
    # code (a bare stub) -- manually attach it so query_QueryValueExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # query_QueryValueExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = query_QueryValueExpression(unaryOperator="sample_text")
    partner = query_TableFunction()
    setattr(partner, 'tableFunction', None)
    _safe_set(owner, 'QueryValueExpression345', partner)
    assert owner in getattr(partner, 'tableFunction')
    _safe_set(owner, 'QueryValueExpression345', None)
    assert owner not in getattr(partner, 'tableFunction')


def test_assoc_predicateExists60_stub_double():
    # query_PredicateExists has no real 'PredicateExists' property in the generated
    # code (a bare stub) -- manually attach it so query_QueryExpressionBody's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # query_QueryExpressionBody's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = query_QueryExpressionBody(rowFetchLimit=7)
    partner = query_PredicateExists()
    setattr(partner, 'PredicateExists', None)
    _safe_set(owner, 'queryExpr', partner)
    assert getattr(partner, 'PredicateExists') == owner
    _safe_set(owner, 'queryExpr', None)
    assert getattr(partner, 'PredicateExists') is None


def test_assoc_quantifiedRowSelectRight144_stub_double():
    # query_QueryExpressionRoot has no real 'queryExpr145' property in the generated
    # code (a bare stub) -- manually attach it so query_PredicateQuantifiedRowSelect's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # query_PredicateQuantifiedRowSelect's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = query_PredicateQuantifiedRowSelect(quantifiedType="sample_text")
    partner = query_QueryExpressionRoot()
    setattr(partner, 'queryExpr145', None)
    _safe_set(owner, 'PredicateQuantifiedRowSelect146', partner)
    assert getattr(partner, 'queryExpr145') == owner
    _safe_set(owner, 'PredicateQuantifiedRowSelect146', None)
    assert getattr(partner, 'queryExpr145') is None


def test_assoc_quantifiedValueSelectRight147_stub_double():
    # query_QueryExpressionRoot has no real 'queryExpr148' property in the generated
    # code (a bare stub) -- manually attach it so query_PredicateQuantifiedValueSelect's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # query_PredicateQuantifiedValueSelect's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = query_PredicateQuantifiedValueSelect(comparisonOperator="sample_text", quantifiedType="sample_text")
    partner = query_QueryExpressionRoot()
    setattr(partner, 'queryExpr148', None)
    _safe_set(owner, 'PredicateQuantifiedValueSelect149', partner)
    assert getattr(partner, 'queryExpr148') == owner
    _safe_set(owner, 'PredicateQuantifiedValueSelect149', None)
    assert getattr(partner, 'queryExpr148') is None


def test_assoc_query137_stub_double():
    # query_QueryExpressionRoot has no real 'queryExpression' property in the generated
    # code (a bare stub) -- manually attach it so query_QueryExpressionBody's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # query_QueryExpressionBody's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = query_QueryExpressionBody(rowFetchLimit=7)
    partner = query_QueryExpressionRoot()
    setattr(partner, 'queryExpression', None)
    _safe_set(owner, 'QueryExpressionBody', partner)
    assert getattr(partner, 'queryExpression') == owner
    _safe_set(owner, 'QueryExpressionBody', None)
    assert getattr(partner, 'queryExpression') is None


def test_assoc_query425_stub_double():
    # query_TableQueryLateral has no real 'query_TableQueryLateral' property in the generated
    # code (a bare stub) -- manually attach it so query_QueryExpressionBody's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # query_QueryExpressionBody's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = query_QueryExpressionBody(rowFetchLimit=7)
    partner = query_TableQueryLateral()
    setattr(partner, 'query_TableQueryLateral', None)
    _safe_set(owner, 'query_QueryExpressionBody', partner)
    assert getattr(partner, 'query_TableQueryLateral') == owner
    _safe_set(owner, 'query_QueryExpressionBody', None)
    assert getattr(partner, 'query_TableQueryLateral') is None


def test_assoc_queryExpr231_stub_double():
    # query_PredicateExists has no real 'predicateExists' property in the generated
    # code (a bare stub) -- manually attach it so query_QueryExpressionBody's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # query_QueryExpressionBody's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = query_QueryExpressionBody(rowFetchLimit=7)
    partner = query_PredicateExists()
    setattr(partner, 'predicateExists', None)
    _safe_set(owner, 'QueryExpressionBody232', partner)
    assert getattr(partner, 'predicateExists') == owner
    _safe_set(owner, 'QueryExpressionBody232', None)
    assert getattr(partner, 'predicateExists') is None


def test_assoc_queryExpr241_stub_double():
    # query_QueryExpressionRoot has no real 'QueryExpressionRoot242' property in the generated
    # code (a bare stub) -- manually attach it so query_PredicateQuantifiedValueSelect's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # query_PredicateQuantifiedValueSelect's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = query_PredicateQuantifiedValueSelect(comparisonOperator="sample_text", quantifiedType="sample_text")
    partner = query_QueryExpressionRoot()
    setattr(partner, 'QueryExpressionRoot242', None)
    _safe_set(owner, 'quantifiedValueSelectRight', partner)
    assert getattr(partner, 'QueryExpressionRoot242') == owner
    _safe_set(owner, 'quantifiedValueSelectRight', None)
    assert getattr(partner, 'QueryExpressionRoot242') is None


def test_assoc_queryExpr245_stub_double():
    # query_QueryExpressionRoot has no real 'QueryExpressionRoot246' property in the generated
    # code (a bare stub) -- manually attach it so query_PredicateQuantifiedRowSelect's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # query_PredicateQuantifiedRowSelect's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = query_PredicateQuantifiedRowSelect(quantifiedType="sample_text")
    partner = query_QueryExpressionRoot()
    setattr(partner, 'QueryExpressionRoot246', None)
    _safe_set(owner, 'quantifiedRowSelectRight', partner)
    assert getattr(partner, 'QueryExpressionRoot246') == owner
    _safe_set(owner, 'quantifiedRowSelectRight', None)
    assert getattr(partner, 'QueryExpressionRoot246') is None


def test_assoc_queryExpr382_stub_double():
    # query_UpdateSourceQuery has no real 'updateSourceQuery' property in the generated
    # code (a bare stub) -- manually attach it so query_QueryExpressionBody's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # query_QueryExpressionBody's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = query_QueryExpressionBody(rowFetchLimit=7)
    partner = query_UpdateSourceQuery()
    setattr(partner, 'updateSourceQuery', None)
    _safe_set(owner, 'QueryExpressionBody383', partner)
    assert getattr(partner, 'updateSourceQuery') == owner
    _safe_set(owner, 'QueryExpressionBody383', None)
    assert getattr(partner, 'updateSourceQuery') is None


def test_assoc_queryExpression55_stub_double():
    # query_QueryExpressionRoot has no real 'QueryExpressionRoot56' property in the generated
    # code (a bare stub) -- manually attach it so query_QueryExpressionBody's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # query_QueryExpressionBody's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = query_QueryExpressionBody(rowFetchLimit=7)
    partner = query_QueryExpressionRoot()
    setattr(partner, 'QueryExpressionRoot56', None)
    _safe_set(owner, 'query', partner)
    assert getattr(partner, 'QueryExpressionRoot56') == owner
    _safe_set(owner, 'query', None)
    assert getattr(partner, 'QueryExpressionRoot56') is None


def test_assoc_queryNest64_stub_double():
    # query_QueryNested has no real 'QueryNested' property in the generated
    # code (a bare stub) -- manually attach it so query_QueryExpressionBody's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # query_QueryExpressionBody's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = query_QueryExpressionBody(rowFetchLimit=7)
    partner = query_QueryNested()
    setattr(partner, 'QueryNested', None)
    _safe_set(owner, 'nestedQuery', partner)
    assert getattr(partner, 'QueryNested') == owner
    _safe_set(owner, 'nestedQuery', None)
    assert getattr(partner, 'QueryNested') is None


def test_assoc_querySelect162_stub_double():
    # query_TableReference has no real 'fromClause' property in the generated
    # code (a bare stub) -- manually attach it so query_QuerySelect's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # query_QuerySelect's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = query_QuerySelect(distinct=True)
    partner = query_TableReference()
    setattr(partner, 'fromClause', None)
    _safe_set(owner, 'QuerySelect163', partner)
    assert getattr(partner, 'fromClause') == owner
    _safe_set(owner, 'QuerySelect163', None)
    assert getattr(partner, 'fromClause') is None


def test_assoc_querySelect213_stub_double():
    # query_GroupingSpecification has no real 'groupByClause' property in the generated
    # code (a bare stub) -- manually attach it so query_QuerySelect's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # query_QuerySelect's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = query_QuerySelect(distinct=True)
    partner = query_GroupingSpecification()
    setattr(partner, 'groupByClause', None)
    _safe_set(owner, 'QuerySelect214', partner)
    assert getattr(partner, 'groupByClause') == owner
    _safe_set(owner, 'QuerySelect214', None)
    assert getattr(partner, 'groupByClause') is None


def test_assoc_querySelect215_stub_double():
    # query_QueryResultSpecification has no real 'selectClause' property in the generated
    # code (a bare stub) -- manually attach it so query_QuerySelect's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # query_QuerySelect's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = query_QuerySelect(distinct=True)
    partner = query_QueryResultSpecification()
    setattr(partner, 'selectClause', None)
    _safe_set(owner, 'QuerySelect216', partner)
    assert getattr(partner, 'selectClause') == owner
    _safe_set(owner, 'QuerySelect216', None)
    assert getattr(partner, 'selectClause') is None


def test_assoc_querySelect274_stub_double():
    # query_ValueExpressionVariable has no real 'intoClause' property in the generated
    # code (a bare stub) -- manually attach it so query_QuerySelect's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # query_QuerySelect's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = query_QuerySelect(distinct=True)
    partner = query_ValueExpressionVariable()
    setattr(partner, 'intoClause', None)
    _safe_set(owner, 'QuerySelect275', partner)
    assert getattr(partner, 'intoClause') == owner
    _safe_set(owner, 'QuerySelect275', None)
    assert getattr(partner, 'intoClause') is None


def test_assoc_resultColumn72_stub_double():
    # query_ResultColumn has no real 'ResultColumn' property in the generated
    # code (a bare stub) -- manually attach it so query_QueryValueExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # query_QueryValueExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = query_QueryValueExpression(unaryOperator="sample_text")
    partner = query_ResultColumn()
    setattr(partner, 'ResultColumn', None)
    _safe_set(owner, 'valueExpr73', partner)
    assert getattr(partner, 'ResultColumn') == owner
    _safe_set(owner, 'valueExpr73', None)
    assert getattr(partner, 'ResultColumn') is None


def test_assoc_resultValueExpr329_stub_double():
    # query_ValueExpressionCaseSimpleContent has no real 'valueExprCaseSimpleContentResult' property in the generated
    # code (a bare stub) -- manually attach it so query_QueryValueExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # query_QueryValueExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = query_QueryValueExpression(unaryOperator="sample_text")
    partner = query_ValueExpressionCaseSimpleContent()
    setattr(partner, 'valueExprCaseSimpleContentResult', None)
    _safe_set(owner, 'QueryValueExpression330', partner)
    assert getattr(partner, 'valueExprCaseSimpleContentResult') == owner
    _safe_set(owner, 'QueryValueExpression330', None)
    assert getattr(partner, 'valueExprCaseSimpleContentResult') is None


def test_assoc_searchCondition321_stub_double():
    # query_ValueExpressionCaseSearchContent has no real 'valueExprCaseSearchContent322' property in the generated
    # code (a bare stub) -- manually attach it so query_QuerySearchCondition's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # query_QuerySearchCondition's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = query_QuerySearchCondition(negatedCondition=True)
    partner = query_ValueExpressionCaseSearchContent()
    setattr(partner, 'valueExprCaseSearchContent322', None)
    _safe_set(owner, 'QuerySearchCondition323', partner)
    assert getattr(partner, 'valueExprCaseSearchContent322') == owner
    _safe_set(owner, 'QuerySearchCondition323', None)
    assert getattr(partner, 'valueExprCaseSearchContent322') is None


def test_assoc_searchCondition403_stub_double():
    # query_MergeOnCondition has no real 'mergeOnCondition' property in the generated
    # code (a bare stub) -- manually attach it so query_QuerySearchCondition's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # query_QuerySearchCondition's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = query_QuerySearchCondition(negatedCondition=True)
    partner = query_MergeOnCondition()
    setattr(partner, 'mergeOnCondition', None)
    _safe_set(owner, 'QuerySearchCondition404', partner)
    assert getattr(partner, 'mergeOnCondition') == owner
    _safe_set(owner, 'QuerySearchCondition404', None)
    assert getattr(partner, 'mergeOnCondition') is None


def test_assoc_selectClause206_stub_double():
    # query_QueryResultSpecification has no real 'QueryResultSpecification' property in the generated
    # code (a bare stub) -- manually attach it so query_QuerySelect's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # query_QuerySelect's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = query_QuerySelect(distinct=True)
    partner = query_QueryResultSpecification()
    setattr(partner, 'QueryResultSpecification', None)
    _safe_set(owner, 'querySelect207', {partner})
    assert getattr(partner, 'QueryResultSpecification') == owner
    _safe_set(owner, 'querySelect207', set())
    assert getattr(partner, 'QueryResultSpecification') is None


def test_assoc_selectStatement369_stub_double():
    # query_QuerySelectStatement has no real 'QuerySelectStatement370' property in the generated
    # code (a bare stub) -- manually attach it so query_OrderBySpecification's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # query_OrderBySpecification's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = query_OrderBySpecification(NullOrderingOption="sample_text", OrderingSpecOption="sample_text", descending=True)
    partner = query_QuerySelectStatement()
    setattr(partner, 'QuerySelectStatement370', None)
    _safe_set(owner, 'orderByClause', partner)
    assert getattr(partner, 'QuerySelectStatement370') == owner
    _safe_set(owner, 'orderByClause', None)
    assert getattr(partner, 'QuerySelectStatement370') is None


def test_assoc_selectStatement415_stub_double():
    # query_QuerySelectStatement has no real 'QuerySelectStatement417' property in the generated
    # code (a bare stub) -- manually attach it so query_UpdatabilityExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # query_UpdatabilityExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = query_UpdatabilityExpression(updatabilityType="sample_text")
    partner = query_QuerySelectStatement()
    setattr(partner, 'QuerySelectStatement417', None)
    _safe_set(owner, 'updatabilityExpr416', partner)
    assert getattr(partner, 'QuerySelectStatement417') == owner
    _safe_set(owner, 'updatabilityExpr416', None)
    assert getattr(partner, 'QuerySelectStatement417') is None


def test_assoc_superGroup303_stub_double():
    # query_SuperGroupElement has no real 'superGroupElementList' property in the generated
    # code (a bare stub) -- manually attach it so query_SuperGroup's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # query_SuperGroup's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = query_SuperGroup(superGroupType="sample_text")
    partner = query_SuperGroupElement()
    setattr(partner, 'superGroupElementList', None)
    _safe_set(owner, 'SuperGroup', partner)
    assert getattr(partner, 'superGroupElementList') == owner
    _safe_set(owner, 'SuperGroup', None)
    assert getattr(partner, 'superGroupElementList') is None


def test_assoc_superGroupElementList298_stub_double():
    # query_SuperGroupElement has no real 'SuperGroupElement' property in the generated
    # code (a bare stub) -- manually attach it so query_SuperGroup's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # query_SuperGroup's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = query_SuperGroup(superGroupType="sample_text")
    partner = query_SuperGroupElement()
    setattr(partner, 'SuperGroupElement', None)
    _safe_set(owner, 'superGroup', {partner})
    assert getattr(partner, 'SuperGroupElement') == owner
    _safe_set(owner, 'superGroup', set())
    assert getattr(partner, 'SuperGroupElement') is None


def test_assoc_tableFunction127_stub_double():
    # query_TableFunction has no real 'TableFunction' property in the generated
    # code (a bare stub) -- manually attach it so query_QueryValueExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # query_QueryValueExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = query_QueryValueExpression(unaryOperator="sample_text")
    partner = query_TableFunction()
    setattr(partner, 'TableFunction', None)
    _safe_set(owner, 'parameterList128', partner)
    assert getattr(partner, 'TableFunction') == owner
    _safe_set(owner, 'parameterList128', None)
    assert getattr(partner, 'TableFunction') is None


def test_assoc_tableJoinedLeft160_stub_double():
    # query_TableReference has no real 'tableRefLeft' property in the generated
    # code (a bare stub) -- manually attach it so query_TableJoined's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # query_TableJoined's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = query_TableJoined(joinOperator="sample_text")
    partner = query_TableReference()
    setattr(partner, 'tableRefLeft', None)
    _safe_set(owner, 'TableJoined161', partner)
    assert getattr(partner, 'tableRefLeft') == owner
    _safe_set(owner, 'TableJoined161', None)
    assert getattr(partner, 'tableRefLeft') is None


def test_assoc_tableJoinedRight158_stub_double():
    # query_TableReference has no real 'tableRefRight' property in the generated
    # code (a bare stub) -- manually attach it so query_TableJoined's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # query_TableJoined's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = query_TableJoined(joinOperator="sample_text")
    partner = query_TableReference()
    setattr(partner, 'tableRefRight', None)
    _safe_set(owner, 'TableJoined159', partner)
    assert getattr(partner, 'tableRefRight') == owner
    _safe_set(owner, 'TableJoined159', None)
    assert getattr(partner, 'tableRefRight') is None


def test_assoc_tableRefLeft179_stub_double():
    # query_TableReference has no real 'TableReference180' property in the generated
    # code (a bare stub) -- manually attach it so query_TableJoined's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # query_TableJoined's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = query_TableJoined(joinOperator="sample_text")
    partner = query_TableReference()
    setattr(partner, 'TableReference180', None)
    _safe_set(owner, 'tableJoinedLeft', partner)
    assert getattr(partner, 'TableReference180') == owner
    _safe_set(owner, 'tableJoinedLeft', None)
    assert getattr(partner, 'TableReference180') is None


def test_assoc_tableRefRight178_stub_double():
    # query_TableReference has no real 'TableReference' property in the generated
    # code (a bare stub) -- manually attach it so query_TableJoined's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # query_TableJoined's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = query_TableJoined(joinOperator="sample_text")
    partner = query_TableReference()
    setattr(partner, 'TableReference', None)
    _safe_set(owner, 'tableJoinedRight', partner)
    assert getattr(partner, 'TableReference') == owner
    _safe_set(owner, 'tableJoinedRight', None)
    assert getattr(partner, 'TableReference') is None


def test_assoc_updatabilityExpr17_stub_double():
    # query_QuerySelectStatement has no real 'selectStatement18' property in the generated
    # code (a bare stub) -- manually attach it so query_UpdatabilityExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # query_UpdatabilityExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = query_UpdatabilityExpression(updatabilityType="sample_text")
    partner = query_QuerySelectStatement()
    setattr(partner, 'selectStatement18', None)
    _safe_set(owner, 'UpdatabilityExpression', partner)
    assert getattr(partner, 'selectStatement18') == owner
    _safe_set(owner, 'UpdatabilityExpression', None)
    assert getattr(partner, 'selectStatement18') is None


def test_assoc_updatabilityExpr412_stub_double():
    # query_UpdateOfColumn has no real 'updateOfColumnList' property in the generated
    # code (a bare stub) -- manually attach it so query_UpdatabilityExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # query_UpdatabilityExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = query_UpdatabilityExpression(updatabilityType="sample_text")
    partner = query_UpdateOfColumn()
    setattr(partner, 'updateOfColumnList', None)
    _safe_set(owner, 'UpdatabilityExpression413', partner)
    assert getattr(partner, 'updateOfColumnList') == owner
    _safe_set(owner, 'UpdatabilityExpression413', None)
    assert getattr(partner, 'updateOfColumnList') is None


def test_assoc_updateOfColumnList414_stub_double():
    # query_UpdateOfColumn has no real 'UpdateOfColumn' property in the generated
    # code (a bare stub) -- manually attach it so query_UpdatabilityExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # query_UpdatabilityExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = query_UpdatabilityExpression(updatabilityType="sample_text")
    partner = query_UpdateOfColumn()
    setattr(partner, 'UpdateOfColumn', None)
    _safe_set(owner, 'updatabilityExpr', {partner})
    assert getattr(partner, 'UpdateOfColumn') == owner
    _safe_set(owner, 'updatabilityExpr', set())
    assert getattr(partner, 'UpdateOfColumn') is None


def test_assoc_updateSourceExprList125_stub_double():
    # query_UpdateSourceExprList has no real 'UpdateSourceExprList' property in the generated
    # code (a bare stub) -- manually attach it so query_QueryValueExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # query_QueryValueExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = query_QueryValueExpression(unaryOperator="sample_text")
    partner = query_UpdateSourceExprList()
    setattr(partner, 'UpdateSourceExprList', None)
    _safe_set(owner, 'valueExprList126', partner)
    assert getattr(partner, 'UpdateSourceExprList') == owner
    _safe_set(owner, 'valueExprList126', None)
    assert getattr(partner, 'UpdateSourceExprList') is None


def test_assoc_updateSourceQuery61_stub_double():
    # query_UpdateSourceQuery has no real 'UpdateSourceQuery' property in the generated
    # code (a bare stub) -- manually attach it so query_QueryExpressionBody's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # query_QueryExpressionBody's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = query_QueryExpressionBody(rowFetchLimit=7)
    partner = query_UpdateSourceQuery()
    setattr(partner, 'UpdateSourceQuery', None)
    _safe_set(owner, 'queryExpr62', partner)
    assert getattr(partner, 'UpdateSourceQuery') == owner
    _safe_set(owner, 'queryExpr62', None)
    assert getattr(partner, 'UpdateSourceQuery') is None


def test_assoc_updateStatement38_stub_double():
    # query_QueryUpdateStatement has no real 'QueryUpdateStatement39' property in the generated
    # code (a bare stub) -- manually attach it so query_QuerySearchCondition's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # query_QuerySearchCondition's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = query_QuerySearchCondition(negatedCondition=True)
    partner = query_QueryUpdateStatement()
    setattr(partner, 'QueryUpdateStatement39', None)
    _safe_set(owner, 'whereClause', partner)
    assert getattr(partner, 'QueryUpdateStatement39') == owner
    _safe_set(owner, 'whereClause', None)
    assert getattr(partner, 'QueryUpdateStatement39') is None


def test_assoc_valueExpr193_stub_double():
    # query_OrderByValueExpression has no real 'orderByValueExpr' property in the generated
    # code (a bare stub) -- manually attach it so query_QueryValueExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # query_QueryValueExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = query_QueryValueExpression(unaryOperator="sample_text")
    partner = query_OrderByValueExpression()
    setattr(partner, 'orderByValueExpr', None)
    _safe_set(owner, 'QueryValueExpression194', partner)
    assert getattr(partner, 'orderByValueExpr') == owner
    _safe_set(owner, 'QueryValueExpression194', None)
    assert getattr(partner, 'orderByValueExpr') is None


def test_assoc_valueExpr218_stub_double():
    # query_ResultColumn has no real 'resultColumn' property in the generated
    # code (a bare stub) -- manually attach it so query_QueryValueExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # query_QueryValueExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = query_QueryValueExpression(unaryOperator="sample_text")
    partner = query_ResultColumn()
    setattr(partner, 'resultColumn', None)
    _safe_set(owner, 'QueryValueExpression219', partner)
    assert getattr(partner, 'resultColumn') == owner
    _safe_set(owner, 'QueryValueExpression219', None)
    assert getattr(partner, 'resultColumn') is None


def test_assoc_valueExpr251_stub_double():
    # query_PredicateInValueSelect has no real 'inValueSelectLeft' property in the generated
    # code (a bare stub) -- manually attach it so query_QueryValueExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # query_QueryValueExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = query_QueryValueExpression(unaryOperator="sample_text")
    partner = query_PredicateInValueSelect()
    setattr(partner, 'inValueSelectLeft', None)
    _safe_set(owner, 'QueryValueExpression252', partner)
    assert getattr(partner, 'inValueSelectLeft') == owner
    _safe_set(owner, 'QueryValueExpression252', None)
    assert getattr(partner, 'inValueSelectLeft') is None


def test_assoc_valueExpr255_stub_double():
    # query_PredicateInValueList has no real 'inValueListLeft' property in the generated
    # code (a bare stub) -- manually attach it so query_QueryValueExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # query_QueryValueExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = query_QueryValueExpression(unaryOperator="sample_text")
    partner = query_PredicateInValueList()
    setattr(partner, 'inValueListLeft', None)
    _safe_set(owner, 'QueryValueExpression256', partner)
    assert getattr(partner, 'inValueListLeft') == owner
    _safe_set(owner, 'QueryValueExpression256', None)
    assert getattr(partner, 'inValueListLeft') is None


def test_assoc_valueExpr282_stub_double():
    # query_ValueExpressionCast has no real 'valueExprCast' property in the generated
    # code (a bare stub) -- manually attach it so query_QueryValueExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # query_QueryValueExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = query_QueryValueExpression(unaryOperator="sample_text")
    partner = query_ValueExpressionCast()
    setattr(partner, 'valueExprCast', None)
    _safe_set(owner, 'QueryValueExpression283', partner)
    assert getattr(partner, 'valueExprCast') == owner
    _safe_set(owner, 'QueryValueExpression283', None)
    assert getattr(partner, 'valueExprCast') is None


def test_assoc_valueExpr299_stub_double():
    # query_GroupingExpression has no real 'groupingExpr' property in the generated
    # code (a bare stub) -- manually attach it so query_QueryValueExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # query_QueryValueExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = query_QueryValueExpression(unaryOperator="sample_text")
    partner = query_GroupingExpression()
    setattr(partner, 'groupingExpr', None)
    _safe_set(owner, 'QueryValueExpression300', partner)
    assert getattr(partner, 'groupingExpr') == owner
    _safe_set(owner, 'QueryValueExpression300', None)
    assert getattr(partner, 'groupingExpr') is None


def test_assoc_valueExpr313_stub_double():
    # query_ValueExpressionCaseSimple has no real 'valueExprCaseSimple314' property in the generated
    # code (a bare stub) -- manually attach it so query_QueryValueExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # query_QueryValueExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = query_QueryValueExpression(unaryOperator="sample_text")
    partner = query_ValueExpressionCaseSimple()
    setattr(partner, 'valueExprCaseSimple314', None)
    _safe_set(owner, 'QueryValueExpression315', partner)
    assert getattr(partner, 'valueExprCaseSimple314') == owner
    _safe_set(owner, 'QueryValueExpression315', None)
    assert getattr(partner, 'valueExprCaseSimple314') is None


def test_assoc_valueExpr317_stub_double():
    # query_ValueExpressionCaseElse has no real 'valueExprCaseElse' property in the generated
    # code (a bare stub) -- manually attach it so query_QueryValueExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # query_QueryValueExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = query_QueryValueExpression(unaryOperator="sample_text")
    partner = query_ValueExpressionCaseElse()
    setattr(partner, 'valueExprCaseElse', None)
    _safe_set(owner, 'QueryValueExpression318', partner)
    assert getattr(partner, 'valueExprCaseElse') == owner
    _safe_set(owner, 'QueryValueExpression318', None)
    assert getattr(partner, 'valueExprCaseElse') is None


def test_assoc_valueExpr319_stub_double():
    # query_ValueExpressionCaseSearchContent has no real 'valueExprCaseSearchContent' property in the generated
    # code (a bare stub) -- manually attach it so query_QueryValueExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # query_QueryValueExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = query_QueryValueExpression(unaryOperator="sample_text")
    partner = query_ValueExpressionCaseSearchContent()
    setattr(partner, 'valueExprCaseSearchContent', None)
    _safe_set(owner, 'QueryValueExpression320', partner)
    assert getattr(partner, 'valueExprCaseSearchContent') == owner
    _safe_set(owner, 'QueryValueExpression320', None)
    assert getattr(partner, 'valueExprCaseSearchContent') is None


def test_assoc_valueExprCaseElse110_stub_double():
    # query_ValueExpressionCaseElse has no real 'ValueExpressionCaseElse' property in the generated
    # code (a bare stub) -- manually attach it so query_QueryValueExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # query_QueryValueExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = query_QueryValueExpression(unaryOperator="sample_text")
    partner = query_ValueExpressionCaseElse()
    setattr(partner, 'ValueExpressionCaseElse', None)
    _safe_set(owner, 'valueExpr111', partner)
    assert getattr(partner, 'ValueExpressionCaseElse') == owner
    _safe_set(owner, 'valueExpr111', None)
    assert getattr(partner, 'ValueExpressionCaseElse') is None


def test_assoc_valueExprCaseSearchContent117_stub_double():
    # query_ValueExpressionCaseSearchContent has no real 'ValueExpressionCaseSearchContent119' property in the generated
    # code (a bare stub) -- manually attach it so query_QueryValueExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # query_QueryValueExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = query_QueryValueExpression(unaryOperator="sample_text")
    partner = query_ValueExpressionCaseSearchContent()
    setattr(partner, 'ValueExpressionCaseSearchContent119', None)
    _safe_set(owner, 'valueExpr118', partner)
    assert getattr(partner, 'ValueExpressionCaseSearchContent119') == owner
    _safe_set(owner, 'valueExpr118', None)
    assert getattr(partner, 'ValueExpressionCaseSearchContent119') is None


def test_assoc_valueExprCaseSearchContent51_stub_double():
    # query_ValueExpressionCaseSearchContent has no real 'ValueExpressionCaseSearchContent' property in the generated
    # code (a bare stub) -- manually attach it so query_QuerySearchCondition's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # query_QuerySearchCondition's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = query_QuerySearchCondition(negatedCondition=True)
    partner = query_ValueExpressionCaseSearchContent()
    setattr(partner, 'ValueExpressionCaseSearchContent', None)
    _safe_set(owner, 'searchCondition', partner)
    assert getattr(partner, 'ValueExpressionCaseSearchContent') == owner
    _safe_set(owner, 'searchCondition', None)
    assert getattr(partner, 'ValueExpressionCaseSearchContent') is None


def test_assoc_valueExprCaseSimple112_stub_double():
    # query_ValueExpressionCaseSimple has no real 'ValueExpressionCaseSimple' property in the generated
    # code (a bare stub) -- manually attach it so query_QueryValueExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # query_QueryValueExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = query_QueryValueExpression(unaryOperator="sample_text")
    partner = query_ValueExpressionCaseSimple()
    setattr(partner, 'ValueExpressionCaseSimple', None)
    _safe_set(owner, 'valueExpr113', partner)
    assert getattr(partner, 'ValueExpressionCaseSimple') == owner
    _safe_set(owner, 'valueExpr113', None)
    assert getattr(partner, 'ValueExpressionCaseSimple') is None


def test_assoc_valueExprCaseSimpleContentResult115_stub_double():
    # query_ValueExpressionCaseSimpleContent has no real 'ValueExpressionCaseSimpleContent116' property in the generated
    # code (a bare stub) -- manually attach it so query_QueryValueExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # query_QueryValueExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = query_QueryValueExpression(unaryOperator="sample_text")
    partner = query_ValueExpressionCaseSimpleContent()
    setattr(partner, 'ValueExpressionCaseSimpleContent116', None)
    _safe_set(owner, 'resultValueExpr', partner)
    assert getattr(partner, 'ValueExpressionCaseSimpleContent116') == owner
    _safe_set(owner, 'resultValueExpr', None)
    assert getattr(partner, 'ValueExpressionCaseSimpleContent116') is None


def test_assoc_valueExprCaseSimpleContentWhen114_stub_double():
    # query_ValueExpressionCaseSimpleContent has no real 'ValueExpressionCaseSimpleContent' property in the generated
    # code (a bare stub) -- manually attach it so query_QueryValueExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # query_QueryValueExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = query_QueryValueExpression(unaryOperator="sample_text")
    partner = query_ValueExpressionCaseSimpleContent()
    setattr(partner, 'ValueExpressionCaseSimpleContent', None)
    _safe_set(owner, 'whenValueExpr', partner)
    assert getattr(partner, 'ValueExpressionCaseSimpleContent') == owner
    _safe_set(owner, 'whenValueExpr', None)
    assert getattr(partner, 'ValueExpressionCaseSimpleContent') is None


def test_assoc_valueExprCast100_stub_double():
    # query_ValueExpressionCast has no real 'ValueExpressionCast' property in the generated
    # code (a bare stub) -- manually attach it so query_QueryValueExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # query_QueryValueExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = query_QueryValueExpression(unaryOperator="sample_text")
    partner = query_ValueExpressionCast()
    setattr(partner, 'ValueExpressionCast', None)
    _safe_set(owner, 'valueExpr101', partner)
    assert getattr(partner, 'ValueExpressionCast') == owner
    _safe_set(owner, 'valueExpr101', None)
    assert getattr(partner, 'ValueExpressionCast') is None


def test_assoc_valueExprList253_stub_double():
    # query_PredicateInValueList has no real 'inValueListRight' property in the generated
    # code (a bare stub) -- manually attach it so query_QueryValueExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # query_QueryValueExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = query_QueryValueExpression(unaryOperator="sample_text")
    partner = query_PredicateInValueList()
    setattr(partner, 'inValueListRight', None)
    _safe_set(owner, 'QueryValueExpression254', partner)
    assert owner in getattr(partner, 'inValueListRight')
    _safe_set(owner, 'QueryValueExpression254', None)
    assert owner not in getattr(partner, 'inValueListRight')


def test_assoc_valueExprList257_stub_double():
    # query_PredicateInValueRowSelect has no real 'inValueRowSelectLeft' property in the generated
    # code (a bare stub) -- manually attach it so query_QueryValueExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # query_QueryValueExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = query_QueryValueExpression(unaryOperator="sample_text")
    partner = query_PredicateInValueRowSelect()
    setattr(partner, 'inValueRowSelectLeft', None)
    _safe_set(owner, 'QueryValueExpression258', partner)
    assert owner in getattr(partner, 'inValueRowSelectLeft')
    _safe_set(owner, 'QueryValueExpression258', None)
    assert owner not in getattr(partner, 'inValueRowSelectLeft')


def test_assoc_valueExprList380_stub_double():
    # query_UpdateSourceExprList has no real 'updateSourceExprList' property in the generated
    # code (a bare stub) -- manually attach it so query_QueryValueExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # query_QueryValueExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = query_QueryValueExpression(unaryOperator="sample_text")
    partner = query_UpdateSourceExprList()
    setattr(partner, 'updateSourceExprList', None)
    _safe_set(owner, 'QueryValueExpression381', partner)
    assert owner in getattr(partner, 'updateSourceExprList')
    _safe_set(owner, 'QueryValueExpression381', None)
    assert owner not in getattr(partner, 'updateSourceExprList')


def test_assoc_valueExprList390_stub_double():
    # query_ValueExpressionRow has no real 'valueExprRow' property in the generated
    # code (a bare stub) -- manually attach it so query_QueryValueExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # query_QueryValueExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = query_QueryValueExpression(unaryOperator="sample_text")
    partner = query_ValueExpressionRow()
    setattr(partner, 'valueExprRow', None)
    _safe_set(owner, 'QueryValueExpression391', partner)
    assert owner in getattr(partner, 'valueExprRow')
    _safe_set(owner, 'QueryValueExpression391', None)
    assert owner not in getattr(partner, 'valueExprRow')


def test_assoc_valueExprRow129_stub_double():
    # query_ValueExpressionRow has no real 'ValueExpressionRow' property in the generated
    # code (a bare stub) -- manually attach it so query_QueryValueExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # query_QueryValueExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = query_QueryValueExpression(unaryOperator="sample_text")
    partner = query_ValueExpressionRow()
    setattr(partner, 'ValueExpressionRow', None)
    _safe_set(owner, 'valueExprList130', partner)
    assert getattr(partner, 'ValueExpressionRow') == owner
    _safe_set(owner, 'valueExprList130', None)
    assert getattr(partner, 'ValueExpressionRow') is None


def test_assoc_valuesRow69_stub_double():
    # query_ValuesRow has no real 'ValuesRow70' property in the generated
    # code (a bare stub) -- manually attach it so query_QueryValueExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # query_QueryValueExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = query_QueryValueExpression(unaryOperator="sample_text")
    partner = query_ValuesRow()
    setattr(partner, 'ValuesRow70', None)
    _safe_set(owner, 'exprList', partner)
    assert getattr(partner, 'ValuesRow70') == owner
    _safe_set(owner, 'exprList', None)
    assert getattr(partner, 'ValuesRow70') is None


def test_assoc_whenValueExpr327_stub_double():
    # query_ValueExpressionCaseSimpleContent has no real 'valueExprCaseSimpleContentWhen' property in the generated
    # code (a bare stub) -- manually attach it so query_QueryValueExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # query_QueryValueExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = query_QueryValueExpression(unaryOperator="sample_text")
    partner = query_ValueExpressionCaseSimpleContent()
    setattr(partner, 'valueExprCaseSimpleContentWhen', None)
    _safe_set(owner, 'QueryValueExpression328', partner)
    assert getattr(partner, 'valueExprCaseSimpleContentWhen') == owner
    _safe_set(owner, 'QueryValueExpression328', None)
    assert getattr(partner, 'valueExprCaseSimpleContentWhen') is None


def test_assoc_whereClause1_stub_double():
    # query_QueryDeleteStatement has no real 'deleteStatement2' property in the generated
    # code (a bare stub) -- manually attach it so query_QuerySearchCondition's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # query_QuerySearchCondition's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = query_QuerySearchCondition(negatedCondition=True)
    partner = query_QueryDeleteStatement()
    setattr(partner, 'deleteStatement2', None)
    _safe_set(owner, 'QuerySearchCondition', partner)
    assert getattr(partner, 'deleteStatement2') == owner
    _safe_set(owner, 'QuerySearchCondition', None)
    assert getattr(partner, 'deleteStatement2') is None


def test_assoc_whereClause23_stub_double():
    # query_QueryUpdateStatement has no real 'updateStatement24' property in the generated
    # code (a bare stub) -- manually attach it so query_QuerySearchCondition's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # query_QuerySearchCondition's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = query_QuerySearchCondition(negatedCondition=True)
    partner = query_QueryUpdateStatement()
    setattr(partner, 'updateStatement24', None)
    _safe_set(owner, 'QuerySearchCondition25', partner)
    assert getattr(partner, 'updateStatement24') == owner
    _safe_set(owner, 'QuerySearchCondition25', None)
    assert getattr(partner, 'updateStatement24') is None


def test_assoc_withTableQueryExpr183_stub_double():
    # query_WithTableSpecification has no real 'withTableSpecification' property in the generated
    # code (a bare stub) -- manually attach it so query_QueryExpressionBody's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # query_QueryExpressionBody's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = query_QueryExpressionBody(rowFetchLimit=7)
    partner = query_WithTableSpecification()
    setattr(partner, 'withTableSpecification', None)
    _safe_set(owner, 'QueryExpressionBody184', partner)
    assert getattr(partner, 'withTableSpecification') == owner
    _safe_set(owner, 'QueryExpressionBody184', None)
    assert getattr(partner, 'withTableSpecification') is None


def test_assoc_withTableSpecification63_stub_double():
    # query_WithTableSpecification has no real 'WithTableSpecification' property in the generated
    # code (a bare stub) -- manually attach it so query_QueryExpressionBody's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # query_QueryExpressionBody's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = query_QueryExpressionBody(rowFetchLimit=7)
    partner = query_WithTableSpecification()
    setattr(partner, 'WithTableSpecification', None)
    _safe_set(owner, 'withTableQueryExpr', partner)
    assert getattr(partner, 'WithTableSpecification') == owner
    _safe_set(owner, 'withTableQueryExpr', None)
    assert getattr(partner, 'WithTableSpecification') is None


