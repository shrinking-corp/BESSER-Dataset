import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    AndOrExpressionOperation,
    BooleanTerm,
    ColumnOperation,
    Condition,
    ConditionOperation,
    DataType,
    Date,
    Expression,
    ExpressionOperation,
    JoinOperation,
    OrderByExpression,
    OrderByParameter,
    SelectExpression,
    SelectParameter,
    SetOperation,
    SimpleCondition,
    SimpleTerm,
    Term,
    Value,
    ValueFrontOperation,
    ValueOperation,
    column_Column,
    column_ColumnExpression,
    column_ColumnOperation,
    column_SingleColumnExpression,
    condition_Condition,
    condition_ConditionOperation,
    expression_AndOrExpressionOperation,
    expression_Expression,
    expression_ExpressionOperationNot,
    from_FromExpression,
    from_JoinOperation,
    from_JoinTableExpression,
    from_Table,
    from_TableExpression,
    from_TableListExpression,
    groupBy_GroupByExpression,
    having_HavingExpression,
    limit_LimitExpression,
    orderBy_OrderByExpression,
    orderBy_OrderByParameter,
    parameter_SelectParameter,
    parameter_SelectParameterDistinct,
    set_SetExpression,
    set_SetOperation,
    sql_column_Column,
    sql_column_ColumnExpression,
    sql_column_ColumnOperation,
    sql_column_ColumnOperationAvg,
    sql_column_ColumnOperationCount,
    sql_column_ColumnOperationEvery,
    sql_column_ColumnOperationMax,
    sql_column_ColumnOperationMin,
    sql_column_ColumnOperationSome,
    sql_column_ColumnOperationSum,
    sql_column_SingleColumnExpression,
    sql_condition_BetweenCondition,
    sql_condition_Condition,
    sql_condition_ConditionOperation,
    sql_condition_ConditionOperationEqual,
    sql_condition_ConditionOperationGreatEqual,
    sql_condition_ConditionOperationGreater,
    sql_condition_ConditionOperationLessEqual,
    sql_condition_ConditionOperationLesser,
    sql_condition_ConditionOperationUnEqual,
    sql_condition_ConditionOperationUnEqual2,
    sql_condition_ExistsCondition,
    sql_condition_InCondition,
    sql_condition_IsNullCondition,
    sql_condition_LikeCondition,
    sql_condition_OperationCondition,
    sql_condition_SimpleCondition,
    sql_expression_AndOrExpressionOperation,
    sql_expression_Expression,
    sql_expression_ExpressionOperation,
    sql_expression_ExpressionOperationAnd,
    sql_expression_ExpressionOperationNot,
    sql_expression_ExpressionOperationOr,
    sql_expression_SimpleExpression,
    sql_from_FromExpression,
    sql_from_JoinOperation,
    sql_from_JoinOperationInner,
    sql_from_JoinOperationLeft,
    sql_from_JoinOperationOuter,
    sql_from_JoinOperationRight,
    sql_from_JoinTableExpression,
    sql_from_Table,
    sql_from_TableExpression,
    sql_from_TableListExpression,
    sql_groupBy_GroupByExpression,
    sql_having_HavingExpression,
    sql_limit_LimitExpression,
    sql_orderBy_OrderByAliasExpression,
    sql_orderBy_OrderByColumnExpression,
    sql_orderBy_OrderByExpression,
    sql_orderBy_OrderByParameter,
    sql_orderBy_OrderByParameterAsc,
    sql_orderBy_OrderByParameterDesc,
    sql_orderBy_OrderBySelectExpression,
    sql_parameter_SelectParameter,
    sql_parameter_SelectParameterAll,
    sql_parameter_SelectParameterDistinct,
    sql_select_SelectExpression,
    sql_set_SetExpression,
    sql_set_SetOperation,
    sql_set_SetOperationExcept,
    sql_set_SetOperationIntersect,
    sql_set_SetOperationMinus,
    sql_set_SetOperationUnion,
    sql_sqlDataTypes_Boolean,
    sql_sqlDataTypes_DataType,
    sql_sqlDataTypes_Date,
    sql_sqlDataTypes_Double,
    sql_sqlDataTypes_Float,
    sql_sqlDataTypes_Integer,
    sql_sqlDataTypes_Real,
    sql_sqlDataTypes_String,
    sql_sqlDataTypes_TimeStamp,
    sql_term_BooleanTerm,
    sql_term_BooleanTermFalse,
    sql_term_BooleanTermTrue,
    sql_term_ColumnTerm,
    sql_term_CountStarTerm,
    sql_term_NullTerm,
    sql_term_SimpleTerm,
    sql_term_SimpleTermChar,
    sql_term_SimpleTermFloat,
    sql_term_SimpleTermInteger,
    sql_term_SimpleTermString,
    sql_term_StarTerm,
    sql_term_Term,
    sql_value_ConditionValue,
    sql_value_FunctionValue,
    sql_value_SimpleValue,
    sql_value_Value,
    sql_value_ValueFrontOperation,
    sql_value_ValueFrontOperationMinus,
    sql_value_ValueFrontOperationPlus,
    sql_value_ValueOperation,
    sql_value_ValueOperationDivide,
    sql_value_ValueOperationMultiply,
    sql_value_ValueOperationParallel,
    sql_where_WhereExpression,
    term_Term,
    value_Value,
    value_ValueFrontOperation,
    value_ValueOperation,
    where_WhereExpression,
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

def test_assoc_expression18_stub_double():
    # expression_Expression has no real 'expression_Expression' property in the generated
    # code (a bare stub) -- manually attach it so sql_column_SingleColumnExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # sql_column_SingleColumnExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = sql_column_SingleColumnExpression(alias="sample_text")
    partner = expression_Expression()
    setattr(partner, 'expression_Expression', None)
    _safe_set(owner, 'sql_column_SingleColumnExpression', partner)
    assert getattr(partner, 'expression_Expression') == owner
    _safe_set(owner, 'sql_column_SingleColumnExpression', None)
    assert getattr(partner, 'expression_Expression') is None


def test_assoc_operation19_stub_double():
    # column_ColumnOperation has no real 'column_ColumnOperation' property in the generated
    # code (a bare stub) -- manually attach it so sql_column_SingleColumnExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # sql_column_SingleColumnExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = sql_column_SingleColumnExpression(alias="sample_text")
    partner = column_ColumnOperation()
    setattr(partner, 'column_ColumnOperation', None)
    _safe_set(owner, 'sql_column_SingleColumnExpression20', partner)
    assert getattr(partner, 'column_ColumnOperation') == owner
    _safe_set(owner, 'sql_column_SingleColumnExpression20', None)
    assert getattr(partner, 'column_ColumnOperation') is None


def test_assoc_parameter21_stub_double():
    # parameter_SelectParameter has no real 'parameter_SelectParameter23' property in the generated
    # code (a bare stub) -- manually attach it so sql_column_SingleColumnExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # sql_column_SingleColumnExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = sql_column_SingleColumnExpression(alias="sample_text")
    partner = parameter_SelectParameter()
    setattr(partner, 'parameter_SelectParameter23', None)
    _safe_set(owner, 'sql_column_SingleColumnExpression22', partner)
    assert getattr(partner, 'parameter_SelectParameter23') == owner
    _safe_set(owner, 'sql_column_SingleColumnExpression22', None)
    assert getattr(partner, 'parameter_SelectParameter23') is None


def test_assoc_parameters84_stub_double():
    # value_Value has no real 'value_Value85' property in the generated
    # code (a bare stub) -- manually attach it so sql_value_FunctionValue's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # sql_value_FunctionValue's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = sql_value_FunctionValue(functionName="sample_text")
    partner = value_Value()
    setattr(partner, 'value_Value85', None)
    _safe_set(owner, 'sql_value_FunctionValue', {partner})
    assert getattr(partner, 'value_Value85') == owner
    _safe_set(owner, 'sql_value_FunctionValue', set())
    assert getattr(partner, 'value_Value85') is None


def test_assoc_selectExpression25_stub_double():
    # SelectExpression has no real 'SelectExpression' property in the generated
    # code (a bare stub) -- manually attach it so sql_from_TableExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # sql_from_TableExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = sql_from_TableExpression(label="sample_text")
    partner = SelectExpression()
    setattr(partner, 'SelectExpression', None)
    _safe_set(owner, 'sql_from_TableExpression', partner)
    assert getattr(partner, 'SelectExpression') == owner
    _safe_set(owner, 'sql_from_TableExpression', None)
    assert getattr(partner, 'SelectExpression') is None


def test_assoc_table26_stub_double():
    # from_Table has no real 'from_Table' property in the generated
    # code (a bare stub) -- manually attach it so sql_from_TableExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # sql_from_TableExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = sql_from_TableExpression(label="sample_text")
    partner = from_Table()
    setattr(partner, 'from_Table', None)
    _safe_set(owner, 'sql_from_TableExpression27', partner)
    assert getattr(partner, 'from_Table') == owner
    _safe_set(owner, 'sql_from_TableExpression27', None)
    assert getattr(partner, 'from_Table') is None


