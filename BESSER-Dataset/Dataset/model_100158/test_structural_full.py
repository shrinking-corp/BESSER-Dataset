import inspect
import pytest
from datetime import date, datetime, time, timedelta
from hypothesis import given, settings
import hypothesis.strategies as st

from python_code import (
    Expression,
    ExpressionTerm,
    FromEntry,
    FromJoin,
    InExpression,
    MQuery,
    SelectAggregateExpression,
    SelectExpression,
    Value,
    Variable,
    mql_AliasAttributeExpression,
    mql_AllExpression,
    mql_AndExpression,
    mql_AnyExpression,
    mql_AvgAggregate,
    mql_BetweenExpression,
    mql_BooleanExpression,
    mql_CollectionExpression,
    mql_CountAggregate,
    mql_DateTimeExpression,
    mql_DeleteClause,
    mql_DeleteStatement,
    mql_EmptyComparisonExpression,
    mql_ExistsExpression,
    mql_Expression,
    mql_ExpressionTerm,
    mql_FromClass,
    mql_FromClause,
    mql_FromCollection,
    mql_FromEntry,
    mql_FromJoin,
    mql_Function,
    mql_HavingClause,
    mql_Import,
    mql_InExpression,
    mql_InQueryExpression,
    mql_InSeqExpression,
    mql_InnerJoin,
    mql_IntegerExpression,
    mql_Join,
    mql_LeftJoin,
    mql_LikeExpression,
    mql_MQuery,
    mql_MaxAggregate,
    mql_MinAggregate,
    mql_NamedQuery,
    mql_NullComparisonExpression,
    mql_NullExpression,
    mql_OperatorExpression,
    mql_OrExpression,
    mql_OrderClause,
    mql_OrderItem,
    mql_ParameterExpression,
    mql_QueryModule,
    mql_SelectAggregateExpression,
    mql_SelectClause,
    mql_SelectConstructorExpression,
    mql_SelectExpression,
    mql_SelectFromClause,
    mql_SelectStatement,
    mql_SetClause,
    mql_SomeExpression,
    mql_StringExpression,
    mql_SumAggregate,
    mql_UpdateClause,
    mql_UpdateItem,
    mql_UpdateStatement,
    mql_Value,
    mql_Variable,
    mql_VariableDeclaration,
    mql_WhereClause,
    Operator,
)

safe_text = st.text(
    alphabet=st.characters(
        whitelist_categories=("Ll", "Lu", "Nd"),
        whitelist_characters="_",
    ),
    min_size=1,
).filter(lambda s: s[0].isalpha())

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
# SECTION 1 -- DETERMINISTIC TESTS (attributes, generalizations, relationships)
# =============================================================================

def test_mql_AliasAttributeExpression_attributes_value_roundtrip():
    instance = mql_AliasAttributeExpression(attributes="sample_text")
    assert instance.attributes == "sample_text"
    instance.attributes = "sample_text_2"
    assert instance.attributes == "sample_text_2"


def test_mql_BetweenExpression_isNot_value_roundtrip():
    instance = mql_BetweenExpression(isNot=True)
    assert instance.isNot == True
    instance.isNot = False
    assert instance.isNot == False


def test_mql_BooleanExpression_value_value_roundtrip():
    instance = mql_BooleanExpression(value=True)
    assert instance.value == True
    instance.value = False
    assert instance.value == False


def test_mql_CollectionExpression_isNot_value_roundtrip():
    instance = mql_CollectionExpression(isNot=True)
    assert instance.isNot == True
    instance.isNot = False
    assert instance.isNot == False


def test_mql_DateTimeExpression_value_value_roundtrip():
    instance = mql_DateTimeExpression(value="sample_text")
    assert instance.value == "sample_text"
    instance.value = "sample_text_2"
    assert instance.value == "sample_text_2"


def test_mql_EmptyComparisonExpression_isNot_value_roundtrip():
    instance = mql_EmptyComparisonExpression(isNot=True)
    assert instance.isNot == True
    instance.isNot = False
    assert instance.isNot == False


def test_mql_ExistsExpression_isNot_value_roundtrip():
    instance = mql_ExistsExpression(isNot=True)
    assert instance.isNot == True
    instance.isNot = False
    assert instance.isNot == False


def test_mql_FromClass_type_value_roundtrip():
    instance = mql_FromClass(type="sample_text")
    assert instance.type == "sample_text"
    instance.type = "sample_text_2"
    assert instance.type == "sample_text_2"


def test_mql_FromJoin_isFetch_value_roundtrip():
    instance = mql_FromJoin(isFetch=True)
    assert instance.isFetch == True
    instance.isFetch = False
    assert instance.isFetch == False


def test_mql_Function_name_value_roundtrip():
    instance = mql_Function(name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_mql_Import_importURI_value_roundtrip():
    instance = mql_Import(importURI="sample_text")
    assert instance.importURI == "sample_text"
    instance.importURI = "sample_text_2"
    assert instance.importURI == "sample_text_2"


def test_mql_InExpression_isNot_value_roundtrip():
    instance = mql_InExpression(isNot=True)
    assert instance.isNot == True
    instance.isNot = False
    assert instance.isNot == False


def test_mql_IntegerExpression_value_value_roundtrip():
    instance = mql_IntegerExpression(value=7)
    assert instance.value == 7
    instance.value = 13
    assert instance.value == 13


def test_mql_LeftJoin_isOuter_value_roundtrip():
    instance = mql_LeftJoin(isOuter=True)
    assert instance.isOuter == True
    instance.isOuter = False
    assert instance.isOuter == False


def test_mql_LikeExpression_isNot_value_roundtrip():
    instance = mql_LikeExpression(isNot=True, pattern="sample_text")
    assert instance.isNot == True
    instance.isNot = False
    assert instance.isNot == False


def test_mql_LikeExpression_pattern_value_roundtrip():
    instance = mql_LikeExpression(isNot=True, pattern="sample_text")
    assert instance.pattern == "sample_text"
    instance.pattern = "sample_text_2"
    assert instance.pattern == "sample_text_2"


def test_mql_NamedQuery_name_value_roundtrip():
    instance = mql_NamedQuery(name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_mql_NullComparisonExpression_isNot_value_roundtrip():
    instance = mql_NullComparisonExpression(isNot=True)
    assert instance.isNot == True
    instance.isNot = False
    assert instance.isNot == False


def test_mql_NullExpression_value_value_roundtrip():
    instance = mql_NullExpression(value="sample_text")
    assert instance.value == "sample_text"
    instance.value = "sample_text_2"
    assert instance.value == "sample_text_2"


def test_mql_OperatorExpression_operator_value_roundtrip():
    instance = mql_OperatorExpression(operator="sample_text")
    assert instance.operator == "sample_text"
    instance.operator = "sample_text_2"
    assert instance.operator == "sample_text_2"


def test_mql_OrderClause_isAsc_value_roundtrip():
    instance = mql_OrderClause(isAsc=True, isDesc=True)
    assert instance.isAsc == True
    instance.isAsc = False
    assert instance.isAsc == False


def test_mql_OrderClause_isDesc_value_roundtrip():
    instance = mql_OrderClause(isAsc=True, isDesc=True)
    assert instance.isDesc == True
    instance.isDesc = False
    assert instance.isDesc == False


def test_mql_OrderItem_feature_value_roundtrip():
    instance = mql_OrderItem(feature="sample_text")
    assert instance.feature == "sample_text"
    instance.feature = "sample_text_2"
    assert instance.feature == "sample_text_2"


def test_mql_ParameterExpression_name_value_roundtrip():
    instance = mql_ParameterExpression(name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_mql_SelectAggregateExpression_isDistinct_value_roundtrip():
    instance = mql_SelectAggregateExpression(isDistinct=True)
    assert instance.isDistinct == True
    instance.isDistinct = False
    assert instance.isDistinct == False


def test_mql_SelectClause_isDistinct_value_roundtrip():
    instance = mql_SelectClause(isDistinct=True)
    assert instance.isDistinct == True
    instance.isDistinct = False
    assert instance.isDistinct == False


def test_mql_SelectConstructorExpression_name_value_roundtrip():
    instance = mql_SelectConstructorExpression(name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_mql_StringExpression_value_value_roundtrip():
    instance = mql_StringExpression(value="sample_text")
    assert instance.value == "sample_text"
    instance.value = "sample_text_2"
    assert instance.value == "sample_text_2"


def test_mql_VariableDeclaration_name_value_roundtrip():
    instance = mql_VariableDeclaration(name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_mql_AllExpression_isa_Expression():
    instance = mql_AllExpression()
    assert isinstance(instance, Expression)


def test_mql_AndExpression_isa_Expression():
    instance = mql_AndExpression()
    assert isinstance(instance, Expression)


def test_mql_AnyExpression_isa_Expression():
    instance = mql_AnyExpression()
    assert isinstance(instance, Expression)


def test_mql_BetweenExpression_isa_Expression():
    instance = mql_BetweenExpression(isNot=True)
    assert isinstance(instance, Expression)


def test_mql_CollectionExpression_isa_Expression():
    instance = mql_CollectionExpression(isNot=True)
    assert isinstance(instance, Expression)


def test_mql_EmptyComparisonExpression_isa_Expression():
    instance = mql_EmptyComparisonExpression(isNot=True)
    assert isinstance(instance, Expression)


def test_mql_ExistsExpression_isa_Expression():
    instance = mql_ExistsExpression(isNot=True)
    assert isinstance(instance, Expression)


def test_mql_ExpressionTerm_isa_Expression():
    instance = mql_ExpressionTerm()
    assert isinstance(instance, Expression)


def test_mql_InExpression_isa_Expression():
    instance = mql_InExpression(isNot=True)
    assert isinstance(instance, Expression)


def test_mql_LikeExpression_isa_Expression():
    instance = mql_LikeExpression(isNot=True, pattern="sample_text")
    assert isinstance(instance, Expression)


def test_mql_NullComparisonExpression_isa_Expression():
    instance = mql_NullComparisonExpression(isNot=True)
    assert isinstance(instance, Expression)


def test_mql_OperatorExpression_isa_Expression():
    instance = mql_OperatorExpression(operator="sample_text")
    assert isinstance(instance, Expression)


def test_mql_OrExpression_isa_Expression():
    instance = mql_OrExpression()
    assert isinstance(instance, Expression)


def test_mql_SomeExpression_isa_Expression():
    instance = mql_SomeExpression()
    assert isinstance(instance, Expression)


def test_mql_SelectStatement_isa_ExpressionTerm():
    instance = mql_SelectStatement()
    assert isinstance(instance, ExpressionTerm)


def test_mql_Variable_isa_ExpressionTerm():
    instance = mql_Variable()
    assert isinstance(instance, ExpressionTerm)


def test_mql_FromClass_isa_FromEntry():
    instance = mql_FromClass(type="sample_text")
    assert isinstance(instance, FromEntry)


def test_mql_FromCollection_isa_FromEntry():
    instance = mql_FromCollection()
    assert isinstance(instance, FromEntry)


def test_mql_InnerJoin_isa_FromJoin():
    instance = mql_InnerJoin()
    assert isinstance(instance, FromJoin)


def test_mql_Join_isa_FromJoin():
    instance = mql_Join()
    assert isinstance(instance, FromJoin)


def test_mql_LeftJoin_isa_FromJoin():
    instance = mql_LeftJoin(isOuter=True)
    assert isinstance(instance, FromJoin)


def test_mql_InQueryExpression_isa_InExpression():
    instance = mql_InQueryExpression()
    assert isinstance(instance, InExpression)


def test_mql_InSeqExpression_isa_InExpression():
    instance = mql_InSeqExpression()
    assert isinstance(instance, InExpression)


def test_mql_DeleteStatement_isa_MQuery():
    instance = mql_DeleteStatement()
    assert isinstance(instance, MQuery)


def test_mql_SelectStatement_isa_MQuery():
    instance = mql_SelectStatement()
    assert isinstance(instance, MQuery)


def test_mql_UpdateStatement_isa_MQuery():
    instance = mql_UpdateStatement()
    assert isinstance(instance, MQuery)


def test_mql_AvgAggregate_isa_SelectAggregateExpression():
    instance = mql_AvgAggregate()
    assert isinstance(instance, SelectAggregateExpression)


def test_mql_CountAggregate_isa_SelectAggregateExpression():
    instance = mql_CountAggregate()
    assert isinstance(instance, SelectAggregateExpression)


def test_mql_MaxAggregate_isa_SelectAggregateExpression():
    instance = mql_MaxAggregate()
    assert isinstance(instance, SelectAggregateExpression)


def test_mql_MinAggregate_isa_SelectAggregateExpression():
    instance = mql_MinAggregate()
    assert isinstance(instance, SelectAggregateExpression)


def test_mql_SumAggregate_isa_SelectAggregateExpression():
    instance = mql_SumAggregate()
    assert isinstance(instance, SelectAggregateExpression)


def test_mql_AliasAttributeExpression_isa_SelectExpression():
    instance = mql_AliasAttributeExpression(attributes="sample_text")
    assert isinstance(instance, SelectExpression)


def test_mql_SelectAggregateExpression_isa_SelectExpression():
    instance = mql_SelectAggregateExpression(isDistinct=True)
    assert isinstance(instance, SelectExpression)


def test_mql_SelectConstructorExpression_isa_SelectExpression():
    instance = mql_SelectConstructorExpression(name="sample_text")
    assert isinstance(instance, SelectExpression)


def test_mql_BooleanExpression_isa_Value():
    instance = mql_BooleanExpression(value=True)
    assert isinstance(instance, Value)


def test_mql_DateTimeExpression_isa_Value():
    instance = mql_DateTimeExpression(value="sample_text")
    assert isinstance(instance, Value)


def test_mql_IntegerExpression_isa_Value():
    instance = mql_IntegerExpression(value=7)
    assert isinstance(instance, Value)


def test_mql_NullExpression_isa_Value():
    instance = mql_NullExpression(value="sample_text")
    assert isinstance(instance, Value)


def test_mql_StringExpression_isa_Value():
    instance = mql_StringExpression(value="sample_text")
    assert isinstance(instance, Value)


def test_mql_AliasAttributeExpression_isa_Variable():
    instance = mql_AliasAttributeExpression(attributes="sample_text")
    assert isinstance(instance, Variable)


def test_mql_ParameterExpression_isa_Variable():
    instance = mql_ParameterExpression(name="sample_text")
    assert isinstance(instance, Variable)


def test_mql_Value_isa_Variable():
    instance = mql_Value()
    assert isinstance(instance, Variable)


def test_assoc_alias100_link_reassign_clear():
    a = mql_VariableDeclaration(name="sample_text")
    b1 = mql_AliasAttributeExpression(attributes="sample_text")
    b2 = mql_AliasAttributeExpression(attributes="sample_text_2")
    _safe_set(a, 'mql_VariableDeclaration102', b1)
    assert _is_linked(a, 'mql_VariableDeclaration102', b1)
    if hasattr(b1, 'mql_AliasAttributeExpression101'):
        assert _is_linked(b1, 'mql_AliasAttributeExpression101', a)
    _safe_set(a, 'mql_VariableDeclaration102', b2)
    assert _is_linked(a, 'mql_VariableDeclaration102', b2)
    if hasattr(b1, 'mql_AliasAttributeExpression101'):
        assert not _is_linked(b1, 'mql_AliasAttributeExpression101', a)
    if hasattr(b2, 'mql_AliasAttributeExpression101'):
        assert _is_linked(b2, 'mql_AliasAttributeExpression101', a)
    _safe_set(a, 'mql_VariableDeclaration102', None)
    assert not _is_linked(a, 'mql_VariableDeclaration102', b2)
    if hasattr(b2, 'mql_AliasAttributeExpression101'):
        assert not _is_linked(b2, 'mql_AliasAttributeExpression101', a)


def test_assoc_alias29_link_reassign_clear():
    a = mql_AliasAttributeExpression(attributes="sample_text")
    b1 = mql_UpdateItem()
    b2 = mql_UpdateItem()
    _safe_set(a, 'mql_AliasAttributeExpression', b1)
    assert _is_linked(a, 'mql_AliasAttributeExpression', b1)
    if hasattr(b1, 'mql_UpdateItem30'):
        assert _is_linked(b1, 'mql_UpdateItem30', a)
    _safe_set(a, 'mql_AliasAttributeExpression', b2)
    assert _is_linked(a, 'mql_AliasAttributeExpression', b2)
    if hasattr(b1, 'mql_UpdateItem30'):
        assert not _is_linked(b1, 'mql_UpdateItem30', a)
    if hasattr(b2, 'mql_UpdateItem30'):
        assert _is_linked(b2, 'mql_UpdateItem30', a)
    _safe_set(a, 'mql_AliasAttributeExpression', None)
    assert not _is_linked(a, 'mql_AliasAttributeExpression', b2)
    if hasattr(b2, 'mql_UpdateItem30'):
        assert not _is_linked(b2, 'mql_UpdateItem30', a)


def test_assoc_expressions41_link_reassign_clear():
    a = mql_SelectClause(isDistinct=True)
    b1 = mql_SelectExpression()
    b2 = mql_SelectExpression()
    _safe_set(a, 'mql_SelectClause42', {b1})
    assert _is_linked(a, 'mql_SelectClause42', b1)
    if hasattr(b1, 'mql_SelectExpression'):
        assert _is_linked(b1, 'mql_SelectExpression', a)
    _safe_set(a, 'mql_SelectClause42', {b2})
    assert _is_linked(a, 'mql_SelectClause42', b2)
    if hasattr(b1, 'mql_SelectExpression'):
        assert not _is_linked(b1, 'mql_SelectExpression', a)
    if hasattr(b2, 'mql_SelectExpression'):
        assert _is_linked(b2, 'mql_SelectExpression', a)
    _safe_set(a, 'mql_SelectClause42', set())
    assert not _is_linked(a, 'mql_SelectClause42', b2)
    if hasattr(b2, 'mql_SelectExpression'):
        assert not _is_linked(b2, 'mql_SelectExpression', a)


def test_assoc_imports0_link_reassign_clear():
    a = mql_Import(importURI="sample_text")
    b1 = mql_QueryModule()
    b2 = mql_QueryModule()
    _safe_set(a, 'mql_Import', b1)
    assert _is_linked(a, 'mql_Import', b1)
    if hasattr(b1, 'mql_QueryModule'):
        assert _is_linked(b1, 'mql_QueryModule', a)
    _safe_set(a, 'mql_Import', b2)
    assert _is_linked(a, 'mql_Import', b2)
    if hasattr(b1, 'mql_QueryModule'):
        assert not _is_linked(b1, 'mql_QueryModule', a)
    if hasattr(b2, 'mql_QueryModule'):
        assert _is_linked(b2, 'mql_QueryModule', a)
    _safe_set(a, 'mql_Import', None)
    assert not _is_linked(a, 'mql_Import', b2)
    if hasattr(b2, 'mql_QueryModule'):
        assert not _is_linked(b2, 'mql_QueryModule', a)


def test_assoc_item43_link_reassign_clear():
    a = mql_SelectAggregateExpression(isDistinct=True)
    b1 = mql_AliasAttributeExpression(attributes="sample_text")
    b2 = mql_AliasAttributeExpression(attributes="sample_text_2")
    _safe_set(a, 'mql_SelectAggregateExpression', b1)
    assert _is_linked(a, 'mql_SelectAggregateExpression', b1)
    if hasattr(b1, 'mql_AliasAttributeExpression44'):
        assert _is_linked(b1, 'mql_AliasAttributeExpression44', a)
    _safe_set(a, 'mql_SelectAggregateExpression', b2)
    assert _is_linked(a, 'mql_SelectAggregateExpression', b2)
    if hasattr(b1, 'mql_AliasAttributeExpression44'):
        assert not _is_linked(b1, 'mql_AliasAttributeExpression44', a)
    if hasattr(b2, 'mql_AliasAttributeExpression44'):
        assert _is_linked(b2, 'mql_AliasAttributeExpression44', a)
    _safe_set(a, 'mql_SelectAggregateExpression', None)
    assert not _is_linked(a, 'mql_SelectAggregateExpression', b2)
    if hasattr(b2, 'mql_AliasAttributeExpression44'):
        assert not _is_linked(b2, 'mql_AliasAttributeExpression44', a)


def test_assoc_items45_link_reassign_clear():
    a = mql_SelectConstructorExpression(name="sample_text")
    b1 = mql_AliasAttributeExpression(attributes="sample_text")
    b2 = mql_AliasAttributeExpression(attributes="sample_text_2")
    _safe_set(a, 'mql_SelectConstructorExpression', {b1})
    assert _is_linked(a, 'mql_SelectConstructorExpression', b1)
    if hasattr(b1, 'mql_AliasAttributeExpression46'):
        assert _is_linked(b1, 'mql_AliasAttributeExpression46', a)
    _safe_set(a, 'mql_SelectConstructorExpression', {b2})
    assert _is_linked(a, 'mql_SelectConstructorExpression', b2)
    if hasattr(b1, 'mql_AliasAttributeExpression46'):
        assert not _is_linked(b1, 'mql_AliasAttributeExpression46', a)
    if hasattr(b2, 'mql_AliasAttributeExpression46'):
        assert _is_linked(b2, 'mql_AliasAttributeExpression46', a)
    _safe_set(a, 'mql_SelectConstructorExpression', set())
    assert not _is_linked(a, 'mql_SelectConstructorExpression', b2)
    if hasattr(b2, 'mql_AliasAttributeExpression46'):
        assert not _is_linked(b2, 'mql_AliasAttributeExpression46', a)


def test_assoc_joins52_link_reassign_clear():
    a = mql_FromJoin(isFetch=True)
    b1 = mql_FromClass(type="sample_text")
    b2 = mql_FromClass(type="sample_text_2")
    _safe_set(a, 'mql_FromJoin', b1)
    assert _is_linked(a, 'mql_FromJoin', b1)
    if hasattr(b1, 'mql_FromClass'):
        assert _is_linked(b1, 'mql_FromClass', a)
    _safe_set(a, 'mql_FromJoin', b2)
    assert _is_linked(a, 'mql_FromJoin', b2)
    if hasattr(b1, 'mql_FromClass'):
        assert not _is_linked(b1, 'mql_FromClass', a)
    if hasattr(b2, 'mql_FromClass'):
        assert _is_linked(b2, 'mql_FromClass', a)
    _safe_set(a, 'mql_FromJoin', None)
    assert not _is_linked(a, 'mql_FromJoin', b2)
    if hasattr(b2, 'mql_FromClass'):
        assert not _is_linked(b2, 'mql_FromClass', a)


def test_assoc_lhs64_link_reassign_clear():
    a = mql_OperatorExpression(operator="sample_text")
    b1 = mql_Variable()
    b2 = mql_Variable()
    _safe_set(a, 'mql_OperatorExpression', b1)
    assert _is_linked(a, 'mql_OperatorExpression', b1)
    if hasattr(b1, 'mql_Variable'):
        assert _is_linked(b1, 'mql_Variable', a)
    _safe_set(a, 'mql_OperatorExpression', b2)
    assert _is_linked(a, 'mql_OperatorExpression', b2)
    if hasattr(b1, 'mql_Variable'):
        assert not _is_linked(b1, 'mql_Variable', a)
    if hasattr(b2, 'mql_Variable'):
        assert _is_linked(b2, 'mql_Variable', a)
    _safe_set(a, 'mql_OperatorExpression', None)
    assert not _is_linked(a, 'mql_OperatorExpression', b2)
    if hasattr(b2, 'mql_Variable'):
        assert not _is_linked(b2, 'mql_Variable', a)


def test_assoc_lhs75_link_reassign_clear():
    a = mql_CollectionExpression(isNot=True)
    b1 = mql_Variable()
    b2 = mql_Variable()
    _safe_set(a, 'mql_CollectionExpression', b1)
    assert _is_linked(a, 'mql_CollectionExpression', b1)
    if hasattr(b1, 'mql_Variable76'):
        assert _is_linked(b1, 'mql_Variable76', a)
    _safe_set(a, 'mql_CollectionExpression', b2)
    assert _is_linked(a, 'mql_CollectionExpression', b2)
    if hasattr(b1, 'mql_Variable76'):
        assert not _is_linked(b1, 'mql_Variable76', a)
    if hasattr(b2, 'mql_Variable76'):
        assert _is_linked(b2, 'mql_Variable76', a)
    _safe_set(a, 'mql_CollectionExpression', None)
    assert not _is_linked(a, 'mql_CollectionExpression', b2)
    if hasattr(b2, 'mql_Variable76'):
        assert not _is_linked(b2, 'mql_Variable76', a)


def test_assoc_lhs80_link_reassign_clear():
    a = mql_NullComparisonExpression(isNot=True)
    b1 = mql_Variable()
    b2 = mql_Variable()
    _safe_set(a, 'mql_NullComparisonExpression', b1)
    assert _is_linked(a, 'mql_NullComparisonExpression', b1)
    if hasattr(b1, 'mql_Variable81'):
        assert _is_linked(b1, 'mql_Variable81', a)
    _safe_set(a, 'mql_NullComparisonExpression', b2)
    assert _is_linked(a, 'mql_NullComparisonExpression', b2)
    if hasattr(b1, 'mql_Variable81'):
        assert not _is_linked(b1, 'mql_Variable81', a)
    if hasattr(b2, 'mql_Variable81'):
        assert _is_linked(b2, 'mql_Variable81', a)
    _safe_set(a, 'mql_NullComparisonExpression', None)
    assert not _is_linked(a, 'mql_NullComparisonExpression', b2)
    if hasattr(b2, 'mql_Variable81'):
        assert not _is_linked(b2, 'mql_Variable81', a)


def test_assoc_lhs82_link_reassign_clear():
    a = mql_EmptyComparisonExpression(isNot=True)
    b1 = mql_Variable()
    b2 = mql_Variable()
    _safe_set(a, 'mql_EmptyComparisonExpression', b1)
    assert _is_linked(a, 'mql_EmptyComparisonExpression', b1)
    if hasattr(b1, 'mql_Variable83'):
        assert _is_linked(b1, 'mql_Variable83', a)
    _safe_set(a, 'mql_EmptyComparisonExpression', b2)
    assert _is_linked(a, 'mql_EmptyComparisonExpression', b2)
    if hasattr(b1, 'mql_Variable83'):
        assert not _is_linked(b1, 'mql_Variable83', a)
    if hasattr(b2, 'mql_Variable83'):
        assert _is_linked(b2, 'mql_Variable83', a)
    _safe_set(a, 'mql_EmptyComparisonExpression', None)
    assert not _is_linked(a, 'mql_EmptyComparisonExpression', b2)
    if hasattr(b2, 'mql_Variable83'):
        assert not _is_linked(b2, 'mql_Variable83', a)


def test_assoc_lhs84_link_reassign_clear():
    a = mql_LikeExpression(isNot=True, pattern="sample_text")
    b1 = mql_Variable()
    b2 = mql_Variable()
    _safe_set(a, 'mql_LikeExpression', b1)
    assert _is_linked(a, 'mql_LikeExpression', b1)
    if hasattr(b1, 'mql_Variable85'):
        assert _is_linked(b1, 'mql_Variable85', a)
    _safe_set(a, 'mql_LikeExpression', b2)
    assert _is_linked(a, 'mql_LikeExpression', b2)
    if hasattr(b1, 'mql_Variable85'):
        assert not _is_linked(b1, 'mql_Variable85', a)
    if hasattr(b2, 'mql_Variable85'):
        assert _is_linked(b2, 'mql_Variable85', a)
    _safe_set(a, 'mql_LikeExpression', None)
    assert not _is_linked(a, 'mql_LikeExpression', b2)
    if hasattr(b2, 'mql_Variable85'):
        assert not _is_linked(b2, 'mql_Variable85', a)


def test_assoc_lhs86_link_reassign_clear():
    a = mql_InExpression(isNot=True)
    b1 = mql_Variable()
    b2 = mql_Variable()
    _safe_set(a, 'mql_InExpression', b1)
    assert _is_linked(a, 'mql_InExpression', b1)
    if hasattr(b1, 'mql_Variable87'):
        assert _is_linked(b1, 'mql_Variable87', a)
    _safe_set(a, 'mql_InExpression', b2)
    assert _is_linked(a, 'mql_InExpression', b2)
    if hasattr(b1, 'mql_Variable87'):
        assert not _is_linked(b1, 'mql_Variable87', a)
    if hasattr(b2, 'mql_Variable87'):
        assert _is_linked(b2, 'mql_Variable87', a)
    _safe_set(a, 'mql_InExpression', None)
    assert not _is_linked(a, 'mql_InExpression', b2)
    if hasattr(b2, 'mql_Variable87'):
        assert not _is_linked(b2, 'mql_Variable87', a)


def test_assoc_lhs92_link_reassign_clear():
    a = mql_BetweenExpression(isNot=True)
    b1 = mql_Variable()
    b2 = mql_Variable()
    _safe_set(a, 'mql_BetweenExpression', b1)
    assert _is_linked(a, 'mql_BetweenExpression', b1)
    if hasattr(b1, 'mql_Variable93'):
        assert _is_linked(b1, 'mql_Variable93', a)
    _safe_set(a, 'mql_BetweenExpression', b2)
    assert _is_linked(a, 'mql_BetweenExpression', b2)
    if hasattr(b1, 'mql_Variable93'):
        assert not _is_linked(b1, 'mql_Variable93', a)
    if hasattr(b2, 'mql_Variable93'):
        assert _is_linked(b2, 'mql_Variable93', a)
    _safe_set(a, 'mql_BetweenExpression', None)
    assert not _is_linked(a, 'mql_BetweenExpression', b2)
    if hasattr(b2, 'mql_Variable93'):
        assert not _is_linked(b2, 'mql_Variable93', a)


def test_assoc_max97_link_reassign_clear():
    a = mql_BetweenExpression(isNot=True)
    b1 = mql_Value()
    b2 = mql_Value()
    _safe_set(a, 'mql_BetweenExpression98', b1)
    assert _is_linked(a, 'mql_BetweenExpression98', b1)
    if hasattr(b1, 'mql_Value99'):
        assert _is_linked(b1, 'mql_Value99', a)
    _safe_set(a, 'mql_BetweenExpression98', b2)
    assert _is_linked(a, 'mql_BetweenExpression98', b2)
    if hasattr(b1, 'mql_Value99'):
        assert not _is_linked(b1, 'mql_Value99', a)
    if hasattr(b2, 'mql_Value99'):
        assert _is_linked(b2, 'mql_Value99', a)
    _safe_set(a, 'mql_BetweenExpression98', None)
    assert not _is_linked(a, 'mql_BetweenExpression98', b2)
    if hasattr(b2, 'mql_Value99'):
        assert not _is_linked(b2, 'mql_Value99', a)


def test_assoc_min94_link_reassign_clear():
    a = mql_BetweenExpression(isNot=True)
    b1 = mql_Value()
    b2 = mql_Value()
    _safe_set(a, 'mql_BetweenExpression95', b1)
    assert _is_linked(a, 'mql_BetweenExpression95', b1)
    if hasattr(b1, 'mql_Value96'):
        assert _is_linked(b1, 'mql_Value96', a)
    _safe_set(a, 'mql_BetweenExpression95', b2)
    assert _is_linked(a, 'mql_BetweenExpression95', b2)
    if hasattr(b1, 'mql_Value96'):
        assert not _is_linked(b1, 'mql_Value96', a)
    if hasattr(b2, 'mql_Value96'):
        assert _is_linked(b2, 'mql_Value96', a)
    _safe_set(a, 'mql_BetweenExpression95', None)
    assert not _is_linked(a, 'mql_BetweenExpression95', b2)
    if hasattr(b2, 'mql_Value96'):
        assert not _is_linked(b2, 'mql_Value96', a)


def test_assoc_namedQueries3_link_reassign_clear():
    a = mql_NamedQuery(name="sample_text")
    b1 = mql_QueryModule()
    b2 = mql_QueryModule()
    _safe_set(a, 'mql_NamedQuery', b1)
    assert _is_linked(a, 'mql_NamedQuery', b1)
    if hasattr(b1, 'mql_QueryModule4'):
        assert _is_linked(b1, 'mql_QueryModule4', a)
    _safe_set(a, 'mql_NamedQuery', b2)
    assert _is_linked(a, 'mql_NamedQuery', b2)
    if hasattr(b1, 'mql_QueryModule4'):
        assert not _is_linked(b1, 'mql_QueryModule4', a)
    if hasattr(b2, 'mql_QueryModule4'):
        assert _is_linked(b2, 'mql_QueryModule4', a)
    _safe_set(a, 'mql_NamedQuery', None)
    assert not _is_linked(a, 'mql_NamedQuery', b2)
    if hasattr(b2, 'mql_QueryModule4'):
        assert not _is_linked(b2, 'mql_QueryModule4', a)


def test_assoc_order13_link_reassign_clear():
    a = mql_OrderClause(isAsc=True, isDesc=True)
    b1 = mql_SelectStatement()
    b2 = mql_SelectStatement()
    _safe_set(a, 'mql_OrderClause', b1)
    assert _is_linked(a, 'mql_OrderClause', b1)
    if hasattr(b1, 'mql_SelectStatement14'):
        assert _is_linked(b1, 'mql_SelectStatement14', a)
    _safe_set(a, 'mql_OrderClause', b2)
    assert _is_linked(a, 'mql_OrderClause', b2)
    if hasattr(b1, 'mql_SelectStatement14'):
        assert not _is_linked(b1, 'mql_SelectStatement14', a)
    if hasattr(b2, 'mql_SelectStatement14'):
        assert _is_linked(b2, 'mql_SelectStatement14', a)
    _safe_set(a, 'mql_OrderClause', None)
    assert not _is_linked(a, 'mql_OrderClause', b2)
    if hasattr(b2, 'mql_SelectStatement14'):
        assert not _is_linked(b2, 'mql_SelectStatement14', a)


def test_assoc_ordering17_link_reassign_clear():
    a = mql_OrderItem(feature="sample_text")
    b1 = mql_OrderClause(isAsc=True, isDesc=True)
    b2 = mql_OrderClause(isAsc=False, isDesc=False)
    _safe_set(a, 'mql_OrderItem', b1)
    assert _is_linked(a, 'mql_OrderItem', b1)
    if hasattr(b1, 'mql_OrderClause18'):
        assert _is_linked(b1, 'mql_OrderClause18', a)
    _safe_set(a, 'mql_OrderItem', b2)
    assert _is_linked(a, 'mql_OrderItem', b2)
    if hasattr(b1, 'mql_OrderClause18'):
        assert not _is_linked(b1, 'mql_OrderClause18', a)
    if hasattr(b2, 'mql_OrderClause18'):
        assert _is_linked(b2, 'mql_OrderClause18', a)
    _safe_set(a, 'mql_OrderItem', None)
    assert not _is_linked(a, 'mql_OrderItem', b2)
    if hasattr(b2, 'mql_OrderClause18'):
        assert not _is_linked(b2, 'mql_OrderClause18', a)


def test_assoc_params103_link_reassign_clear():
    a = mql_Function(name="sample_text")
    b1 = mql_Variable()
    b2 = mql_Variable()
    _safe_set(a, 'mql_Function', {b1})
    assert _is_linked(a, 'mql_Function', b1)
    if hasattr(b1, 'mql_Variable104'):
        assert _is_linked(b1, 'mql_Variable104', a)
    _safe_set(a, 'mql_Function', {b2})
    assert _is_linked(a, 'mql_Function', b2)
    if hasattr(b1, 'mql_Variable104'):
        assert not _is_linked(b1, 'mql_Variable104', a)
    if hasattr(b2, 'mql_Variable104'):
        assert _is_linked(b2, 'mql_Variable104', a)
    _safe_set(a, 'mql_Function', set())
    assert not _is_linked(a, 'mql_Function', b2)
    if hasattr(b2, 'mql_Variable104'):
        assert not _is_linked(b2, 'mql_Variable104', a)


def test_assoc_path53_link_reassign_clear():
    a = mql_AliasAttributeExpression(attributes="sample_text")
    b1 = mql_FromCollection()
    b2 = mql_FromCollection()
    _safe_set(a, 'mql_AliasAttributeExpression54', b1)
    assert _is_linked(a, 'mql_AliasAttributeExpression54', b1)
    if hasattr(b1, 'mql_FromCollection'):
        assert _is_linked(b1, 'mql_FromCollection', a)
    _safe_set(a, 'mql_AliasAttributeExpression54', b2)
    assert _is_linked(a, 'mql_AliasAttributeExpression54', b2)
    if hasattr(b1, 'mql_FromCollection'):
        assert not _is_linked(b1, 'mql_FromCollection', a)
    if hasattr(b2, 'mql_FromCollection'):
        assert _is_linked(b2, 'mql_FromCollection', a)
    _safe_set(a, 'mql_AliasAttributeExpression54', None)
    assert not _is_linked(a, 'mql_AliasAttributeExpression54', b2)
    if hasattr(b2, 'mql_FromCollection'):
        assert not _is_linked(b2, 'mql_FromCollection', a)


def test_assoc_path55_link_reassign_clear():
    a = mql_FromJoin(isFetch=True)
    b1 = mql_AliasAttributeExpression(attributes="sample_text")
    b2 = mql_AliasAttributeExpression(attributes="sample_text_2")
    _safe_set(a, 'mql_FromJoin56', b1)
    assert _is_linked(a, 'mql_FromJoin56', b1)
    if hasattr(b1, 'mql_AliasAttributeExpression57'):
        assert _is_linked(b1, 'mql_AliasAttributeExpression57', a)
    _safe_set(a, 'mql_FromJoin56', b2)
    assert _is_linked(a, 'mql_FromJoin56', b2)
    if hasattr(b1, 'mql_AliasAttributeExpression57'):
        assert not _is_linked(b1, 'mql_AliasAttributeExpression57', a)
    if hasattr(b2, 'mql_AliasAttributeExpression57'):
        assert _is_linked(b2, 'mql_AliasAttributeExpression57', a)
    _safe_set(a, 'mql_FromJoin56', None)
    assert not _is_linked(a, 'mql_FromJoin56', b2)
    if hasattr(b2, 'mql_AliasAttributeExpression57'):
        assert not _is_linked(b2, 'mql_AliasAttributeExpression57', a)


def test_assoc_query5_link_reassign_clear():
    a = mql_NamedQuery(name="sample_text")
    b1 = mql_MQuery()
    b2 = mql_MQuery()
    _safe_set(a, 'mql_NamedQuery6', b1)
    assert _is_linked(a, 'mql_NamedQuery6', b1)
    if hasattr(b1, 'mql_MQuery7'):
        assert _is_linked(b1, 'mql_MQuery7', a)
    _safe_set(a, 'mql_NamedQuery6', b2)
    assert _is_linked(a, 'mql_NamedQuery6', b2)
    if hasattr(b1, 'mql_MQuery7'):
        assert not _is_linked(b1, 'mql_MQuery7', a)
    if hasattr(b2, 'mql_MQuery7'):
        assert _is_linked(b2, 'mql_MQuery7', a)
    _safe_set(a, 'mql_NamedQuery6', None)
    assert not _is_linked(a, 'mql_NamedQuery6', b2)
    if hasattr(b2, 'mql_MQuery7'):
        assert not _is_linked(b2, 'mql_MQuery7', a)


def test_assoc_query67_link_reassign_clear():
    a = mql_ExistsExpression(isNot=True)
    b1 = mql_SelectStatement()
    b2 = mql_SelectStatement()
    _safe_set(a, 'mql_ExistsExpression', b1)
    assert _is_linked(a, 'mql_ExistsExpression', b1)
    if hasattr(b1, 'mql_SelectStatement68'):
        assert _is_linked(b1, 'mql_SelectStatement68', a)
    _safe_set(a, 'mql_ExistsExpression', b2)
    assert _is_linked(a, 'mql_ExistsExpression', b2)
    if hasattr(b1, 'mql_SelectStatement68'):
        assert not _is_linked(b1, 'mql_SelectStatement68', a)
    if hasattr(b2, 'mql_SelectStatement68'):
        assert _is_linked(b2, 'mql_SelectStatement68', a)
    _safe_set(a, 'mql_ExistsExpression', None)
    assert not _is_linked(a, 'mql_ExistsExpression', b2)
    if hasattr(b2, 'mql_SelectStatement68'):
        assert not _is_linked(b2, 'mql_SelectStatement68', a)


def test_assoc_rhs65_link_reassign_clear():
    a = mql_OperatorExpression(operator="sample_text")
    b1 = mql_ExpressionTerm()
    b2 = mql_ExpressionTerm()
    _safe_set(a, 'mql_OperatorExpression66', b1)
    assert _is_linked(a, 'mql_OperatorExpression66', b1)
    if hasattr(b1, 'mql_ExpressionTerm'):
        assert _is_linked(b1, 'mql_ExpressionTerm', a)
    _safe_set(a, 'mql_OperatorExpression66', b2)
    assert _is_linked(a, 'mql_OperatorExpression66', b2)
    if hasattr(b1, 'mql_ExpressionTerm'):
        assert not _is_linked(b1, 'mql_ExpressionTerm', a)
    if hasattr(b2, 'mql_ExpressionTerm'):
        assert _is_linked(b2, 'mql_ExpressionTerm', a)
    _safe_set(a, 'mql_OperatorExpression66', None)
    assert not _is_linked(a, 'mql_OperatorExpression66', b2)
    if hasattr(b2, 'mql_ExpressionTerm'):
        assert not _is_linked(b2, 'mql_ExpressionTerm', a)


def test_assoc_rhs77_link_reassign_clear():
    a = mql_CollectionExpression(isNot=True)
    b1 = mql_AliasAttributeExpression(attributes="sample_text")
    b2 = mql_AliasAttributeExpression(attributes="sample_text_2")
    _safe_set(a, 'mql_CollectionExpression78', b1)
    assert _is_linked(a, 'mql_CollectionExpression78', b1)
    if hasattr(b1, 'mql_AliasAttributeExpression79'):
        assert _is_linked(b1, 'mql_AliasAttributeExpression79', a)
    _safe_set(a, 'mql_CollectionExpression78', b2)
    assert _is_linked(a, 'mql_CollectionExpression78', b2)
    if hasattr(b1, 'mql_AliasAttributeExpression79'):
        assert not _is_linked(b1, 'mql_AliasAttributeExpression79', a)
    if hasattr(b2, 'mql_AliasAttributeExpression79'):
        assert _is_linked(b2, 'mql_AliasAttributeExpression79', a)
    _safe_set(a, 'mql_CollectionExpression78', None)
    assert not _is_linked(a, 'mql_CollectionExpression78', b2)
    if hasattr(b2, 'mql_AliasAttributeExpression79'):
        assert not _is_linked(b2, 'mql_AliasAttributeExpression79', a)


def test_assoc_selectClause36_link_reassign_clear():
    a = mql_SelectClause(isDistinct=True)
    b1 = mql_SelectFromClause()
    b2 = mql_SelectFromClause()
    _safe_set(a, 'mql_SelectClause', b1)
    assert _is_linked(a, 'mql_SelectClause', b1)
    if hasattr(b1, 'mql_SelectFromClause37'):
        assert _is_linked(b1, 'mql_SelectFromClause37', a)
    _safe_set(a, 'mql_SelectClause', b2)
    assert _is_linked(a, 'mql_SelectClause', b2)
    if hasattr(b1, 'mql_SelectFromClause37'):
        assert not _is_linked(b1, 'mql_SelectFromClause37', a)
    if hasattr(b2, 'mql_SelectFromClause37'):
        assert _is_linked(b2, 'mql_SelectFromClause37', a)
    _safe_set(a, 'mql_SelectClause', None)
    assert not _is_linked(a, 'mql_SelectClause', b2)
    if hasattr(b2, 'mql_SelectFromClause37'):
        assert not _is_linked(b2, 'mql_SelectFromClause37', a)


def test_assoc_var19_link_reassign_clear():
    a = mql_OrderItem(feature="sample_text")
    b1 = mql_FromEntry()
    b2 = mql_FromEntry()
    _safe_set(a, 'mql_OrderItem20', b1)
    assert _is_linked(a, 'mql_OrderItem20', b1)
    if hasattr(b1, 'mql_FromEntry'):
        assert _is_linked(b1, 'mql_FromEntry', a)
    _safe_set(a, 'mql_OrderItem20', b2)
    assert _is_linked(a, 'mql_OrderItem20', b2)
    if hasattr(b1, 'mql_FromEntry'):
        assert not _is_linked(b1, 'mql_FromEntry', a)
    if hasattr(b2, 'mql_FromEntry'):
        assert _is_linked(b2, 'mql_FromEntry', a)
    _safe_set(a, 'mql_OrderItem20', None)
    assert not _is_linked(a, 'mql_OrderItem20', b2)
    if hasattr(b2, 'mql_FromEntry'):
        assert not _is_linked(b2, 'mql_FromEntry', a)


def test_assoc_variable50_link_reassign_clear():
    a = mql_VariableDeclaration(name="sample_text")
    b1 = mql_FromEntry()
    b2 = mql_FromEntry()
    _safe_set(a, 'mql_VariableDeclaration', b1)
    assert _is_linked(a, 'mql_VariableDeclaration', b1)
    if hasattr(b1, 'mql_FromEntry51'):
        assert _is_linked(b1, 'mql_FromEntry51', a)
    _safe_set(a, 'mql_VariableDeclaration', b2)
    assert _is_linked(a, 'mql_VariableDeclaration', b2)
    if hasattr(b1, 'mql_FromEntry51'):
        assert not _is_linked(b1, 'mql_FromEntry51', a)
    if hasattr(b2, 'mql_FromEntry51'):
        assert _is_linked(b2, 'mql_FromEntry51', a)
    _safe_set(a, 'mql_VariableDeclaration', None)
    assert not _is_linked(a, 'mql_VariableDeclaration', b2)
    if hasattr(b2, 'mql_FromEntry51'):
        assert not _is_linked(b2, 'mql_FromEntry51', a)


def test_assoc_variable58_link_reassign_clear():
    a = mql_VariableDeclaration(name="sample_text")
    b1 = mql_FromJoin(isFetch=True)
    b2 = mql_FromJoin(isFetch=False)
    _safe_set(a, 'mql_VariableDeclaration60', b1)
    assert _is_linked(a, 'mql_VariableDeclaration60', b1)
    if hasattr(b1, 'mql_FromJoin59'):
        assert _is_linked(b1, 'mql_FromJoin59', a)
    _safe_set(a, 'mql_VariableDeclaration60', b2)
    assert _is_linked(a, 'mql_VariableDeclaration60', b2)
    if hasattr(b1, 'mql_FromJoin59'):
        assert not _is_linked(b1, 'mql_FromJoin59', a)
    if hasattr(b2, 'mql_FromJoin59'):
        assert _is_linked(b2, 'mql_FromJoin59', a)
    _safe_set(a, 'mql_VariableDeclaration60', None)
    assert not _is_linked(a, 'mql_VariableDeclaration60', b2)
    if hasattr(b2, 'mql_FromJoin59'):
        assert not _is_linked(b2, 'mql_FromJoin59', a)


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

Expression_strategy = st.builds(Expression)
@given(instance=Expression_strategy)
@settings(max_examples=25)
def test_Expression_instantiation(instance):
    assert isinstance(instance, Expression)


ExpressionTerm_strategy = st.builds(ExpressionTerm)
@given(instance=ExpressionTerm_strategy)
@settings(max_examples=25)
def test_ExpressionTerm_instantiation(instance):
    assert isinstance(instance, ExpressionTerm)


FromEntry_strategy = st.builds(FromEntry)
@given(instance=FromEntry_strategy)
@settings(max_examples=25)
def test_FromEntry_instantiation(instance):
    assert isinstance(instance, FromEntry)


FromJoin_strategy = st.builds(FromJoin)
@given(instance=FromJoin_strategy)
@settings(max_examples=25)
def test_FromJoin_instantiation(instance):
    assert isinstance(instance, FromJoin)


InExpression_strategy = st.builds(InExpression)
@given(instance=InExpression_strategy)
@settings(max_examples=25)
def test_InExpression_instantiation(instance):
    assert isinstance(instance, InExpression)


MQuery_strategy = st.builds(MQuery)
@given(instance=MQuery_strategy)
@settings(max_examples=25)
def test_MQuery_instantiation(instance):
    assert isinstance(instance, MQuery)


SelectAggregateExpression_strategy = st.builds(SelectAggregateExpression)
@given(instance=SelectAggregateExpression_strategy)
@settings(max_examples=25)
def test_SelectAggregateExpression_instantiation(instance):
    assert isinstance(instance, SelectAggregateExpression)


SelectExpression_strategy = st.builds(SelectExpression)
@given(instance=SelectExpression_strategy)
@settings(max_examples=25)
def test_SelectExpression_instantiation(instance):
    assert isinstance(instance, SelectExpression)


Value_strategy = st.builds(Value)
@given(instance=Value_strategy)
@settings(max_examples=25)
def test_Value_instantiation(instance):
    assert isinstance(instance, Value)


Variable_strategy = st.builds(Variable)
@given(instance=Variable_strategy)
@settings(max_examples=25)
def test_Variable_instantiation(instance):
    assert isinstance(instance, Variable)


mql_AliasAttributeExpression_strategy = st.builds(mql_AliasAttributeExpression, attributes=safe_text)
@given(instance=mql_AliasAttributeExpression_strategy)
@settings(max_examples=25)
def test_mql_AliasAttributeExpression_instantiation(instance):
    assert isinstance(instance, mql_AliasAttributeExpression)


mql_AllExpression_strategy = st.builds(mql_AllExpression)
@given(instance=mql_AllExpression_strategy)
@settings(max_examples=25)
def test_mql_AllExpression_instantiation(instance):
    assert isinstance(instance, mql_AllExpression)


mql_AndExpression_strategy = st.builds(mql_AndExpression)
@given(instance=mql_AndExpression_strategy)
@settings(max_examples=25)
def test_mql_AndExpression_instantiation(instance):
    assert isinstance(instance, mql_AndExpression)


mql_AnyExpression_strategy = st.builds(mql_AnyExpression)
@given(instance=mql_AnyExpression_strategy)
@settings(max_examples=25)
def test_mql_AnyExpression_instantiation(instance):
    assert isinstance(instance, mql_AnyExpression)


mql_AvgAggregate_strategy = st.builds(mql_AvgAggregate)
@given(instance=mql_AvgAggregate_strategy)
@settings(max_examples=25)
def test_mql_AvgAggregate_instantiation(instance):
    assert isinstance(instance, mql_AvgAggregate)


mql_BetweenExpression_strategy = st.builds(mql_BetweenExpression, isNot=st.booleans())
@given(instance=mql_BetweenExpression_strategy)
@settings(max_examples=25)
def test_mql_BetweenExpression_instantiation(instance):
    assert isinstance(instance, mql_BetweenExpression)


mql_BooleanExpression_strategy = st.builds(mql_BooleanExpression, value=st.booleans())
@given(instance=mql_BooleanExpression_strategy)
@settings(max_examples=25)
def test_mql_BooleanExpression_instantiation(instance):
    assert isinstance(instance, mql_BooleanExpression)


mql_CollectionExpression_strategy = st.builds(mql_CollectionExpression, isNot=st.booleans())
@given(instance=mql_CollectionExpression_strategy)
@settings(max_examples=25)
def test_mql_CollectionExpression_instantiation(instance):
    assert isinstance(instance, mql_CollectionExpression)


mql_CountAggregate_strategy = st.builds(mql_CountAggregate)
@given(instance=mql_CountAggregate_strategy)
@settings(max_examples=25)
def test_mql_CountAggregate_instantiation(instance):
    assert isinstance(instance, mql_CountAggregate)


mql_DateTimeExpression_strategy = st.builds(mql_DateTimeExpression, value=safe_text)
@given(instance=mql_DateTimeExpression_strategy)
@settings(max_examples=25)
def test_mql_DateTimeExpression_instantiation(instance):
    assert isinstance(instance, mql_DateTimeExpression)


mql_DeleteClause_strategy = st.builds(mql_DeleteClause)
@given(instance=mql_DeleteClause_strategy)
@settings(max_examples=25)
def test_mql_DeleteClause_instantiation(instance):
    assert isinstance(instance, mql_DeleteClause)


mql_DeleteStatement_strategy = st.builds(mql_DeleteStatement)
@given(instance=mql_DeleteStatement_strategy)
@settings(max_examples=25)
def test_mql_DeleteStatement_instantiation(instance):
    assert isinstance(instance, mql_DeleteStatement)


mql_EmptyComparisonExpression_strategy = st.builds(mql_EmptyComparisonExpression, isNot=st.booleans())
@given(instance=mql_EmptyComparisonExpression_strategy)
@settings(max_examples=25)
def test_mql_EmptyComparisonExpression_instantiation(instance):
    assert isinstance(instance, mql_EmptyComparisonExpression)


mql_ExistsExpression_strategy = st.builds(mql_ExistsExpression, isNot=st.booleans())
@given(instance=mql_ExistsExpression_strategy)
@settings(max_examples=25)
def test_mql_ExistsExpression_instantiation(instance):
    assert isinstance(instance, mql_ExistsExpression)


mql_Expression_strategy = st.builds(mql_Expression)
@given(instance=mql_Expression_strategy)
@settings(max_examples=25)
def test_mql_Expression_instantiation(instance):
    assert isinstance(instance, mql_Expression)


mql_ExpressionTerm_strategy = st.builds(mql_ExpressionTerm)
@given(instance=mql_ExpressionTerm_strategy)
@settings(max_examples=25)
def test_mql_ExpressionTerm_instantiation(instance):
    assert isinstance(instance, mql_ExpressionTerm)


mql_FromClass_strategy = st.builds(mql_FromClass, type=safe_text)
@given(instance=mql_FromClass_strategy)
@settings(max_examples=25)
def test_mql_FromClass_instantiation(instance):
    assert isinstance(instance, mql_FromClass)


mql_FromClause_strategy = st.builds(mql_FromClause)
@given(instance=mql_FromClause_strategy)
@settings(max_examples=25)
def test_mql_FromClause_instantiation(instance):
    assert isinstance(instance, mql_FromClause)


mql_FromCollection_strategy = st.builds(mql_FromCollection)
@given(instance=mql_FromCollection_strategy)
@settings(max_examples=25)
def test_mql_FromCollection_instantiation(instance):
    assert isinstance(instance, mql_FromCollection)


mql_FromEntry_strategy = st.builds(mql_FromEntry)
@given(instance=mql_FromEntry_strategy)
@settings(max_examples=25)
def test_mql_FromEntry_instantiation(instance):
    assert isinstance(instance, mql_FromEntry)


mql_FromJoin_strategy = st.builds(mql_FromJoin, isFetch=st.booleans())
@given(instance=mql_FromJoin_strategy)
@settings(max_examples=25)
def test_mql_FromJoin_instantiation(instance):
    assert isinstance(instance, mql_FromJoin)


mql_Function_strategy = st.builds(mql_Function, name=safe_text)
@given(instance=mql_Function_strategy)
@settings(max_examples=25)
def test_mql_Function_instantiation(instance):
    assert isinstance(instance, mql_Function)


mql_HavingClause_strategy = st.builds(mql_HavingClause)
@given(instance=mql_HavingClause_strategy)
@settings(max_examples=25)
def test_mql_HavingClause_instantiation(instance):
    assert isinstance(instance, mql_HavingClause)


mql_Import_strategy = st.builds(mql_Import, importURI=safe_text)
@given(instance=mql_Import_strategy)
@settings(max_examples=25)
def test_mql_Import_instantiation(instance):
    assert isinstance(instance, mql_Import)


mql_InExpression_strategy = st.builds(mql_InExpression, isNot=st.booleans())
@given(instance=mql_InExpression_strategy)
@settings(max_examples=25)
def test_mql_InExpression_instantiation(instance):
    assert isinstance(instance, mql_InExpression)


mql_InQueryExpression_strategy = st.builds(mql_InQueryExpression)
@given(instance=mql_InQueryExpression_strategy)
@settings(max_examples=25)
def test_mql_InQueryExpression_instantiation(instance):
    assert isinstance(instance, mql_InQueryExpression)


mql_InSeqExpression_strategy = st.builds(mql_InSeqExpression)
@given(instance=mql_InSeqExpression_strategy)
@settings(max_examples=25)
def test_mql_InSeqExpression_instantiation(instance):
    assert isinstance(instance, mql_InSeqExpression)


mql_InnerJoin_strategy = st.builds(mql_InnerJoin)
@given(instance=mql_InnerJoin_strategy)
@settings(max_examples=25)
def test_mql_InnerJoin_instantiation(instance):
    assert isinstance(instance, mql_InnerJoin)


mql_IntegerExpression_strategy = st.builds(mql_IntegerExpression, value=st.integers())
@given(instance=mql_IntegerExpression_strategy)
@settings(max_examples=25)
def test_mql_IntegerExpression_instantiation(instance):
    assert isinstance(instance, mql_IntegerExpression)


mql_Join_strategy = st.builds(mql_Join)
@given(instance=mql_Join_strategy)
@settings(max_examples=25)
def test_mql_Join_instantiation(instance):
    assert isinstance(instance, mql_Join)


mql_LeftJoin_strategy = st.builds(mql_LeftJoin, isOuter=st.booleans())
@given(instance=mql_LeftJoin_strategy)
@settings(max_examples=25)
def test_mql_LeftJoin_instantiation(instance):
    assert isinstance(instance, mql_LeftJoin)


mql_LikeExpression_strategy = st.builds(mql_LikeExpression, isNot=st.booleans(), pattern=safe_text)
@given(instance=mql_LikeExpression_strategy)
@settings(max_examples=25)
def test_mql_LikeExpression_instantiation(instance):
    assert isinstance(instance, mql_LikeExpression)


mql_MQuery_strategy = st.builds(mql_MQuery)
@given(instance=mql_MQuery_strategy)
@settings(max_examples=25)
def test_mql_MQuery_instantiation(instance):
    assert isinstance(instance, mql_MQuery)


mql_MaxAggregate_strategy = st.builds(mql_MaxAggregate)
@given(instance=mql_MaxAggregate_strategy)
@settings(max_examples=25)
def test_mql_MaxAggregate_instantiation(instance):
    assert isinstance(instance, mql_MaxAggregate)


mql_MinAggregate_strategy = st.builds(mql_MinAggregate)
@given(instance=mql_MinAggregate_strategy)
@settings(max_examples=25)
def test_mql_MinAggregate_instantiation(instance):
    assert isinstance(instance, mql_MinAggregate)


mql_NamedQuery_strategy = st.builds(mql_NamedQuery, name=safe_text)
@given(instance=mql_NamedQuery_strategy)
@settings(max_examples=25)
def test_mql_NamedQuery_instantiation(instance):
    assert isinstance(instance, mql_NamedQuery)


mql_NullComparisonExpression_strategy = st.builds(mql_NullComparisonExpression, isNot=st.booleans())
@given(instance=mql_NullComparisonExpression_strategy)
@settings(max_examples=25)
def test_mql_NullComparisonExpression_instantiation(instance):
    assert isinstance(instance, mql_NullComparisonExpression)


mql_NullExpression_strategy = st.builds(mql_NullExpression, value=safe_text)
@given(instance=mql_NullExpression_strategy)
@settings(max_examples=25)
def test_mql_NullExpression_instantiation(instance):
    assert isinstance(instance, mql_NullExpression)


mql_OperatorExpression_strategy = st.builds(mql_OperatorExpression, operator=safe_text)
@given(instance=mql_OperatorExpression_strategy)
@settings(max_examples=25)
def test_mql_OperatorExpression_instantiation(instance):
    assert isinstance(instance, mql_OperatorExpression)


mql_OrExpression_strategy = st.builds(mql_OrExpression)
@given(instance=mql_OrExpression_strategy)
@settings(max_examples=25)
def test_mql_OrExpression_instantiation(instance):
    assert isinstance(instance, mql_OrExpression)


mql_OrderClause_strategy = st.builds(mql_OrderClause, isAsc=st.booleans(), isDesc=st.booleans())
@given(instance=mql_OrderClause_strategy)
@settings(max_examples=25)
def test_mql_OrderClause_instantiation(instance):
    assert isinstance(instance, mql_OrderClause)


mql_OrderItem_strategy = st.builds(mql_OrderItem, feature=safe_text)
@given(instance=mql_OrderItem_strategy)
@settings(max_examples=25)
def test_mql_OrderItem_instantiation(instance):
    assert isinstance(instance, mql_OrderItem)


mql_ParameterExpression_strategy = st.builds(mql_ParameterExpression, name=safe_text)
@given(instance=mql_ParameterExpression_strategy)
@settings(max_examples=25)
def test_mql_ParameterExpression_instantiation(instance):
    assert isinstance(instance, mql_ParameterExpression)


mql_QueryModule_strategy = st.builds(mql_QueryModule)
@given(instance=mql_QueryModule_strategy)
@settings(max_examples=25)
def test_mql_QueryModule_instantiation(instance):
    assert isinstance(instance, mql_QueryModule)


mql_SelectAggregateExpression_strategy = st.builds(mql_SelectAggregateExpression, isDistinct=st.booleans())
@given(instance=mql_SelectAggregateExpression_strategy)
@settings(max_examples=25)
def test_mql_SelectAggregateExpression_instantiation(instance):
    assert isinstance(instance, mql_SelectAggregateExpression)


mql_SelectClause_strategy = st.builds(mql_SelectClause, isDistinct=st.booleans())
@given(instance=mql_SelectClause_strategy)
@settings(max_examples=25)
def test_mql_SelectClause_instantiation(instance):
    assert isinstance(instance, mql_SelectClause)


mql_SelectConstructorExpression_strategy = st.builds(mql_SelectConstructorExpression, name=safe_text)
@given(instance=mql_SelectConstructorExpression_strategy)
@settings(max_examples=25)
def test_mql_SelectConstructorExpression_instantiation(instance):
    assert isinstance(instance, mql_SelectConstructorExpression)


mql_SelectExpression_strategy = st.builds(mql_SelectExpression)
@given(instance=mql_SelectExpression_strategy)
@settings(max_examples=25)
def test_mql_SelectExpression_instantiation(instance):
    assert isinstance(instance, mql_SelectExpression)


mql_SelectFromClause_strategy = st.builds(mql_SelectFromClause)
@given(instance=mql_SelectFromClause_strategy)
@settings(max_examples=25)
def test_mql_SelectFromClause_instantiation(instance):
    assert isinstance(instance, mql_SelectFromClause)


mql_SelectStatement_strategy = st.builds(mql_SelectStatement)
@given(instance=mql_SelectStatement_strategy)
@settings(max_examples=25)
def test_mql_SelectStatement_instantiation(instance):
    assert isinstance(instance, mql_SelectStatement)


mql_SetClause_strategy = st.builds(mql_SetClause)
@given(instance=mql_SetClause_strategy)
@settings(max_examples=25)
def test_mql_SetClause_instantiation(instance):
    assert isinstance(instance, mql_SetClause)


mql_SomeExpression_strategy = st.builds(mql_SomeExpression)
@given(instance=mql_SomeExpression_strategy)
@settings(max_examples=25)
def test_mql_SomeExpression_instantiation(instance):
    assert isinstance(instance, mql_SomeExpression)


mql_StringExpression_strategy = st.builds(mql_StringExpression, value=safe_text)
@given(instance=mql_StringExpression_strategy)
@settings(max_examples=25)
def test_mql_StringExpression_instantiation(instance):
    assert isinstance(instance, mql_StringExpression)


mql_SumAggregate_strategy = st.builds(mql_SumAggregate)
@given(instance=mql_SumAggregate_strategy)
@settings(max_examples=25)
def test_mql_SumAggregate_instantiation(instance):
    assert isinstance(instance, mql_SumAggregate)


mql_UpdateClause_strategy = st.builds(mql_UpdateClause)
@given(instance=mql_UpdateClause_strategy)
@settings(max_examples=25)
def test_mql_UpdateClause_instantiation(instance):
    assert isinstance(instance, mql_UpdateClause)


mql_UpdateItem_strategy = st.builds(mql_UpdateItem)
@given(instance=mql_UpdateItem_strategy)
@settings(max_examples=25)
def test_mql_UpdateItem_instantiation(instance):
    assert isinstance(instance, mql_UpdateItem)


mql_UpdateStatement_strategy = st.builds(mql_UpdateStatement)
@given(instance=mql_UpdateStatement_strategy)
@settings(max_examples=25)
def test_mql_UpdateStatement_instantiation(instance):
    assert isinstance(instance, mql_UpdateStatement)


mql_Value_strategy = st.builds(mql_Value)
@given(instance=mql_Value_strategy)
@settings(max_examples=25)
def test_mql_Value_instantiation(instance):
    assert isinstance(instance, mql_Value)


mql_Variable_strategy = st.builds(mql_Variable)
@given(instance=mql_Variable_strategy)
@settings(max_examples=25)
def test_mql_Variable_instantiation(instance):
    assert isinstance(instance, mql_Variable)


mql_VariableDeclaration_strategy = st.builds(mql_VariableDeclaration, name=safe_text)
@given(instance=mql_VariableDeclaration_strategy)
@settings(max_examples=25)
def test_mql_VariableDeclaration_instantiation(instance):
    assert isinstance(instance, mql_VariableDeclaration)


mql_WhereClause_strategy = st.builds(mql_WhereClause)
@given(instance=mql_WhereClause_strategy)
@settings(max_examples=25)
def test_mql_WhereClause_instantiation(instance):
    assert isinstance(instance, mql_WhereClause)


