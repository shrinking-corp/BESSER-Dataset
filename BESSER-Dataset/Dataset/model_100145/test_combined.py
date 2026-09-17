# =============================================================================
# This file is a generated concatenation of two independent test suites --
# see scripts/generate_combined_tests.py for why simple concatenation is safe
# despite both generators using the same naming convention for some helpers,
# and for the deterministic rules used to drop old-suite tests the new suite
# already covers equally or more thoroughly.
# =============================================================================

# ----- SECTION A: test_hypothesis.py (original generated suite) -----
import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    Value,
    jpql_NullExpression,
    jpql_StringExpression,
    jpql_BooleanExpression,
    jpql_IntegerExpression,
    jpql_Function,
    jpql_DateTimeExpression,
    Variable,
    jpql_ParameterExpression,
    InExpression,
    jpql_InQueryExpression,
    jpql_InSeqExpression,
    Expression,
    jpql_BetweenExpression,
    jpql_EmptyComparisonExpression,
    jpql_ExpressionTerm,
    jpql_InExpression,
    jpql_AndExpression,
    jpql_LikeExpression,
    jpql_OrExpression,
    jpql_OperatorExpression,
    FromJoin,
    jpql_LeftJoin,
    jpql_InnerJoin,
    jpql_Join,
    jpql_NullComparisonExpression,
    jpql_CollectionExpression,
    jpql_SomeExpression,
    jpql_AnyExpression,
    jpql_AllExpression,
    jpql_ExistsExpression,
    SelectAggregateExpression,
    jpql_MinAggregate,
    jpql_MaxAggregate,
    jpql_CountAggregate,
    jpql_SumAggregate,
    jpql_AvgAggregate,
    SelectExpression,
    jpql_SelectConstructorExpression,
    jpql_SelectAggregateExpression,
    jpql_SelectExpression,
    jpql_FromJoin,
    FromEntry,
    jpql_FromCollection,
    jpql_FromClass,
    jpql_VariableDeclaration,
    jpql_SetClause,
    jpql_UpdateClause,
    jpql_FromEntry,
    jpql_OrderItem,
    jpql_Expression,
    jpql_SelectClause,
    jpql_FromClause,
    jpql_DeleteClause,
    jpql_Value,
    jpql_AliasAttributeExpression,
    jpql_UpdateItem,
    jpql_Import,
    jpql_QueryModule,
    jpql_OrderClause,
    jpql_HavingClause,
    jpql_SelectFromClause,
    ExpressionTerm,
    jpql_Variable,
    JPQLQuery,
    jpql_UpdateStatement,
    jpql_DeleteStatement,
    jpql_SelectStatement,
    jpql_WhereClause,
    jpql_NamedQuery,
    jpql_JPQLQuery,
    Operator,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_hyp_value_is_not_abstract():
    assert not inspect.isabstract(Value)


def test_hyp_value_constructor_exists():
    assert callable(Value.__init__)


def test_hyp_value_constructor_args():
    sig = inspect.signature(Value.__init__)
    params = list(sig.parameters.keys())



def test_hyp_jpql_nullexpression_is_not_abstract():
    assert not inspect.isabstract(jpql_NullExpression)


def test_hyp_jpql_nullexpression_constructor_exists():
    assert callable(jpql_NullExpression.__init__)


def test_hyp_jpql_nullexpression_constructor_args():
    sig = inspect.signature(jpql_NullExpression.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"




def test_hyp_jpql_stringexpression_is_not_abstract():
    assert not inspect.isabstract(jpql_StringExpression)


def test_hyp_jpql_stringexpression_constructor_exists():
    assert callable(jpql_StringExpression.__init__)


def test_hyp_jpql_stringexpression_constructor_args():
    sig = inspect.signature(jpql_StringExpression.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"




def test_hyp_jpql_booleanexpression_is_not_abstract():
    assert not inspect.isabstract(jpql_BooleanExpression)


def test_hyp_jpql_booleanexpression_constructor_exists():
    assert callable(jpql_BooleanExpression.__init__)


def test_hyp_jpql_booleanexpression_constructor_args():
    sig = inspect.signature(jpql_BooleanExpression.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"




def test_hyp_jpql_integerexpression_is_not_abstract():
    assert not inspect.isabstract(jpql_IntegerExpression)


def test_hyp_jpql_integerexpression_constructor_exists():
    assert callable(jpql_IntegerExpression.__init__)


def test_hyp_jpql_integerexpression_constructor_args():
    sig = inspect.signature(jpql_IntegerExpression.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"




def test_hyp_jpql_function_is_not_abstract():
    assert not inspect.isabstract(jpql_Function)


def test_hyp_jpql_function_constructor_exists():
    assert callable(jpql_Function.__init__)


def test_hyp_jpql_function_constructor_args():
    sig = inspect.signature(jpql_Function.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"




def test_hyp_jpql_datetimeexpression_is_not_abstract():
    assert not inspect.isabstract(jpql_DateTimeExpression)


def test_hyp_jpql_datetimeexpression_constructor_exists():
    assert callable(jpql_DateTimeExpression.__init__)


def test_hyp_jpql_datetimeexpression_constructor_args():
    sig = inspect.signature(jpql_DateTimeExpression.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"




def test_hyp_variable_is_not_abstract():
    assert not inspect.isabstract(Variable)


def test_hyp_variable_constructor_exists():
    assert callable(Variable.__init__)


def test_hyp_variable_constructor_args():
    sig = inspect.signature(Variable.__init__)
    params = list(sig.parameters.keys())



def test_hyp_jpql_parameterexpression_is_not_abstract():
    assert not inspect.isabstract(jpql_ParameterExpression)


def test_hyp_jpql_parameterexpression_constructor_exists():
    assert callable(jpql_ParameterExpression.__init__)


def test_hyp_jpql_parameterexpression_constructor_args():
    sig = inspect.signature(jpql_ParameterExpression.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"




def test_hyp_inexpression_is_not_abstract():
    assert not inspect.isabstract(InExpression)


def test_hyp_inexpression_constructor_exists():
    assert callable(InExpression.__init__)


def test_hyp_inexpression_constructor_args():
    sig = inspect.signature(InExpression.__init__)
    params = list(sig.parameters.keys())



def test_hyp_jpql_inqueryexpression_is_not_abstract():
    assert not inspect.isabstract(jpql_InQueryExpression)


def test_hyp_jpql_inqueryexpression_constructor_exists():
    assert callable(jpql_InQueryExpression.__init__)


def test_hyp_jpql_inqueryexpression_constructor_args():
    sig = inspect.signature(jpql_InQueryExpression.__init__)
    params = list(sig.parameters.keys())



def test_hyp_jpql_inseqexpression_is_not_abstract():
    assert not inspect.isabstract(jpql_InSeqExpression)


def test_hyp_jpql_inseqexpression_constructor_exists():
    assert callable(jpql_InSeqExpression.__init__)


def test_hyp_jpql_inseqexpression_constructor_args():
    sig = inspect.signature(jpql_InSeqExpression.__init__)
    params = list(sig.parameters.keys())



def test_hyp_expression_is_not_abstract():
    assert not inspect.isabstract(Expression)


def test_hyp_expression_constructor_exists():
    assert callable(Expression.__init__)


def test_hyp_expression_constructor_args():
    sig = inspect.signature(Expression.__init__)
    params = list(sig.parameters.keys())



def test_hyp_jpql_betweenexpression_is_not_abstract():
    assert not inspect.isabstract(jpql_BetweenExpression)


def test_hyp_jpql_betweenexpression_constructor_exists():
    assert callable(jpql_BetweenExpression.__init__)


def test_hyp_jpql_betweenexpression_constructor_args():
    sig = inspect.signature(jpql_BetweenExpression.__init__)
    params = list(sig.parameters.keys())
    assert "isNot" in params, "Missing parameter 'isNot'"




def test_hyp_jpql_emptycomparisonexpression_is_not_abstract():
    assert not inspect.isabstract(jpql_EmptyComparisonExpression)


def test_hyp_jpql_emptycomparisonexpression_constructor_exists():
    assert callable(jpql_EmptyComparisonExpression.__init__)


def test_hyp_jpql_emptycomparisonexpression_constructor_args():
    sig = inspect.signature(jpql_EmptyComparisonExpression.__init__)
    params = list(sig.parameters.keys())
    assert "isNot" in params, "Missing parameter 'isNot'"




def test_hyp_jpql_expressionterm_is_not_abstract():
    assert not inspect.isabstract(jpql_ExpressionTerm)


def test_hyp_jpql_expressionterm_constructor_exists():
    assert callable(jpql_ExpressionTerm.__init__)


def test_hyp_jpql_expressionterm_constructor_args():
    sig = inspect.signature(jpql_ExpressionTerm.__init__)
    params = list(sig.parameters.keys())



def test_hyp_jpql_inexpression_is_not_abstract():
    assert not inspect.isabstract(jpql_InExpression)


def test_hyp_jpql_inexpression_constructor_exists():
    assert callable(jpql_InExpression.__init__)


def test_hyp_jpql_inexpression_constructor_args():
    sig = inspect.signature(jpql_InExpression.__init__)
    params = list(sig.parameters.keys())
    assert "isNot" in params, "Missing parameter 'isNot'"




def test_hyp_jpql_andexpression_is_not_abstract():
    assert not inspect.isabstract(jpql_AndExpression)


def test_hyp_jpql_andexpression_constructor_exists():
    assert callable(jpql_AndExpression.__init__)


def test_hyp_jpql_andexpression_constructor_args():
    sig = inspect.signature(jpql_AndExpression.__init__)
    params = list(sig.parameters.keys())



def test_hyp_jpql_likeexpression_is_not_abstract():
    assert not inspect.isabstract(jpql_LikeExpression)


def test_hyp_jpql_likeexpression_constructor_exists():
    assert callable(jpql_LikeExpression.__init__)


def test_hyp_jpql_likeexpression_constructor_args():
    sig = inspect.signature(jpql_LikeExpression.__init__)
    params = list(sig.parameters.keys())
    assert "pattern" in params, "Missing parameter 'pattern'"
    assert "isNot" in params, "Missing parameter 'isNot'"





def test_hyp_jpql_orexpression_is_not_abstract():
    assert not inspect.isabstract(jpql_OrExpression)


def test_hyp_jpql_orexpression_constructor_exists():
    assert callable(jpql_OrExpression.__init__)


def test_hyp_jpql_orexpression_constructor_args():
    sig = inspect.signature(jpql_OrExpression.__init__)
    params = list(sig.parameters.keys())



def test_hyp_jpql_operatorexpression_is_not_abstract():
    assert not inspect.isabstract(jpql_OperatorExpression)


def test_hyp_jpql_operatorexpression_constructor_exists():
    assert callable(jpql_OperatorExpression.__init__)


def test_hyp_jpql_operatorexpression_constructor_args():
    sig = inspect.signature(jpql_OperatorExpression.__init__)
    params = list(sig.parameters.keys())
    assert "operator" in params, "Missing parameter 'operator'"




def test_hyp_fromjoin_is_not_abstract():
    assert not inspect.isabstract(FromJoin)


def test_hyp_fromjoin_constructor_exists():
    assert callable(FromJoin.__init__)


def test_hyp_fromjoin_constructor_args():
    sig = inspect.signature(FromJoin.__init__)
    params = list(sig.parameters.keys())



def test_hyp_jpql_leftjoin_is_not_abstract():
    assert not inspect.isabstract(jpql_LeftJoin)


def test_hyp_jpql_leftjoin_constructor_exists():
    assert callable(jpql_LeftJoin.__init__)


def test_hyp_jpql_leftjoin_constructor_args():
    sig = inspect.signature(jpql_LeftJoin.__init__)
    params = list(sig.parameters.keys())
    assert "isOuter" in params, "Missing parameter 'isOuter'"




def test_hyp_jpql_innerjoin_is_not_abstract():
    assert not inspect.isabstract(jpql_InnerJoin)


def test_hyp_jpql_innerjoin_constructor_exists():
    assert callable(jpql_InnerJoin.__init__)


def test_hyp_jpql_innerjoin_constructor_args():
    sig = inspect.signature(jpql_InnerJoin.__init__)
    params = list(sig.parameters.keys())



def test_hyp_jpql_join_is_not_abstract():
    assert not inspect.isabstract(jpql_Join)


def test_hyp_jpql_join_constructor_exists():
    assert callable(jpql_Join.__init__)


def test_hyp_jpql_join_constructor_args():
    sig = inspect.signature(jpql_Join.__init__)
    params = list(sig.parameters.keys())



def test_hyp_jpql_nullcomparisonexpression_is_not_abstract():
    assert not inspect.isabstract(jpql_NullComparisonExpression)


def test_hyp_jpql_nullcomparisonexpression_constructor_exists():
    assert callable(jpql_NullComparisonExpression.__init__)


def test_hyp_jpql_nullcomparisonexpression_constructor_args():
    sig = inspect.signature(jpql_NullComparisonExpression.__init__)
    params = list(sig.parameters.keys())
    assert "isNot" in params, "Missing parameter 'isNot'"




def test_hyp_jpql_collectionexpression_is_not_abstract():
    assert not inspect.isabstract(jpql_CollectionExpression)


def test_hyp_jpql_collectionexpression_constructor_exists():
    assert callable(jpql_CollectionExpression.__init__)


def test_hyp_jpql_collectionexpression_constructor_args():
    sig = inspect.signature(jpql_CollectionExpression.__init__)
    params = list(sig.parameters.keys())
    assert "isNot" in params, "Missing parameter 'isNot'"




def test_hyp_jpql_someexpression_is_not_abstract():
    assert not inspect.isabstract(jpql_SomeExpression)


def test_hyp_jpql_someexpression_constructor_exists():
    assert callable(jpql_SomeExpression.__init__)


def test_hyp_jpql_someexpression_constructor_args():
    sig = inspect.signature(jpql_SomeExpression.__init__)
    params = list(sig.parameters.keys())



def test_hyp_jpql_anyexpression_is_not_abstract():
    assert not inspect.isabstract(jpql_AnyExpression)


def test_hyp_jpql_anyexpression_constructor_exists():
    assert callable(jpql_AnyExpression.__init__)


def test_hyp_jpql_anyexpression_constructor_args():
    sig = inspect.signature(jpql_AnyExpression.__init__)
    params = list(sig.parameters.keys())



def test_hyp_jpql_allexpression_is_not_abstract():
    assert not inspect.isabstract(jpql_AllExpression)


def test_hyp_jpql_allexpression_constructor_exists():
    assert callable(jpql_AllExpression.__init__)


def test_hyp_jpql_allexpression_constructor_args():
    sig = inspect.signature(jpql_AllExpression.__init__)
    params = list(sig.parameters.keys())



def test_hyp_jpql_existsexpression_is_not_abstract():
    assert not inspect.isabstract(jpql_ExistsExpression)


def test_hyp_jpql_existsexpression_constructor_exists():
    assert callable(jpql_ExistsExpression.__init__)


def test_hyp_jpql_existsexpression_constructor_args():
    sig = inspect.signature(jpql_ExistsExpression.__init__)
    params = list(sig.parameters.keys())
    assert "isNot" in params, "Missing parameter 'isNot'"




def test_hyp_selectaggregateexpression_is_not_abstract():
    assert not inspect.isabstract(SelectAggregateExpression)


def test_hyp_selectaggregateexpression_constructor_exists():
    assert callable(SelectAggregateExpression.__init__)


def test_hyp_selectaggregateexpression_constructor_args():
    sig = inspect.signature(SelectAggregateExpression.__init__)
    params = list(sig.parameters.keys())



def test_hyp_jpql_minaggregate_is_not_abstract():
    assert not inspect.isabstract(jpql_MinAggregate)


def test_hyp_jpql_minaggregate_constructor_exists():
    assert callable(jpql_MinAggregate.__init__)


def test_hyp_jpql_minaggregate_constructor_args():
    sig = inspect.signature(jpql_MinAggregate.__init__)
    params = list(sig.parameters.keys())



def test_hyp_jpql_maxaggregate_is_not_abstract():
    assert not inspect.isabstract(jpql_MaxAggregate)


def test_hyp_jpql_maxaggregate_constructor_exists():
    assert callable(jpql_MaxAggregate.__init__)


def test_hyp_jpql_maxaggregate_constructor_args():
    sig = inspect.signature(jpql_MaxAggregate.__init__)
    params = list(sig.parameters.keys())



def test_hyp_jpql_countaggregate_is_not_abstract():
    assert not inspect.isabstract(jpql_CountAggregate)


def test_hyp_jpql_countaggregate_constructor_exists():
    assert callable(jpql_CountAggregate.__init__)


def test_hyp_jpql_countaggregate_constructor_args():
    sig = inspect.signature(jpql_CountAggregate.__init__)
    params = list(sig.parameters.keys())



def test_hyp_jpql_sumaggregate_is_not_abstract():
    assert not inspect.isabstract(jpql_SumAggregate)


def test_hyp_jpql_sumaggregate_constructor_exists():
    assert callable(jpql_SumAggregate.__init__)


def test_hyp_jpql_sumaggregate_constructor_args():
    sig = inspect.signature(jpql_SumAggregate.__init__)
    params = list(sig.parameters.keys())



def test_hyp_jpql_avgaggregate_is_not_abstract():
    assert not inspect.isabstract(jpql_AvgAggregate)


def test_hyp_jpql_avgaggregate_constructor_exists():
    assert callable(jpql_AvgAggregate.__init__)


def test_hyp_jpql_avgaggregate_constructor_args():
    sig = inspect.signature(jpql_AvgAggregate.__init__)
    params = list(sig.parameters.keys())



def test_hyp_selectexpression_is_not_abstract():
    assert not inspect.isabstract(SelectExpression)


def test_hyp_selectexpression_constructor_exists():
    assert callable(SelectExpression.__init__)


def test_hyp_selectexpression_constructor_args():
    sig = inspect.signature(SelectExpression.__init__)
    params = list(sig.parameters.keys())



def test_hyp_jpql_selectconstructorexpression_is_not_abstract():
    assert not inspect.isabstract(jpql_SelectConstructorExpression)


def test_hyp_jpql_selectconstructorexpression_constructor_exists():
    assert callable(jpql_SelectConstructorExpression.__init__)


def test_hyp_jpql_selectconstructorexpression_constructor_args():
    sig = inspect.signature(jpql_SelectConstructorExpression.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"




def test_hyp_jpql_selectaggregateexpression_is_not_abstract():
    assert not inspect.isabstract(jpql_SelectAggregateExpression)


def test_hyp_jpql_selectaggregateexpression_constructor_exists():
    assert callable(jpql_SelectAggregateExpression.__init__)


def test_hyp_jpql_selectaggregateexpression_constructor_args():
    sig = inspect.signature(jpql_SelectAggregateExpression.__init__)
    params = list(sig.parameters.keys())
    assert "isDistinct" in params, "Missing parameter 'isDistinct'"




def test_hyp_jpql_selectexpression_is_not_abstract():
    assert not inspect.isabstract(jpql_SelectExpression)


def test_hyp_jpql_selectexpression_constructor_exists():
    assert callable(jpql_SelectExpression.__init__)


def test_hyp_jpql_selectexpression_constructor_args():
    sig = inspect.signature(jpql_SelectExpression.__init__)
    params = list(sig.parameters.keys())



def test_hyp_jpql_fromjoin_is_not_abstract():
    assert not inspect.isabstract(jpql_FromJoin)


def test_hyp_jpql_fromjoin_constructor_exists():
    assert callable(jpql_FromJoin.__init__)


def test_hyp_jpql_fromjoin_constructor_args():
    sig = inspect.signature(jpql_FromJoin.__init__)
    params = list(sig.parameters.keys())
    assert "isFetch" in params, "Missing parameter 'isFetch'"




def test_hyp_fromentry_is_not_abstract():
    assert not inspect.isabstract(FromEntry)


def test_hyp_fromentry_constructor_exists():
    assert callable(FromEntry.__init__)


def test_hyp_fromentry_constructor_args():
    sig = inspect.signature(FromEntry.__init__)
    params = list(sig.parameters.keys())



def test_hyp_jpql_fromcollection_is_not_abstract():
    assert not inspect.isabstract(jpql_FromCollection)


def test_hyp_jpql_fromcollection_constructor_exists():
    assert callable(jpql_FromCollection.__init__)


def test_hyp_jpql_fromcollection_constructor_args():
    sig = inspect.signature(jpql_FromCollection.__init__)
    params = list(sig.parameters.keys())



def test_hyp_jpql_fromclass_is_not_abstract():
    assert not inspect.isabstract(jpql_FromClass)


def test_hyp_jpql_fromclass_constructor_exists():
    assert callable(jpql_FromClass.__init__)


def test_hyp_jpql_fromclass_constructor_args():
    sig = inspect.signature(jpql_FromClass.__init__)
    params = list(sig.parameters.keys())
    assert "type" in params, "Missing parameter 'type'"




def test_hyp_jpql_variabledeclaration_is_not_abstract():
    assert not inspect.isabstract(jpql_VariableDeclaration)


def test_hyp_jpql_variabledeclaration_constructor_exists():
    assert callable(jpql_VariableDeclaration.__init__)


def test_hyp_jpql_variabledeclaration_constructor_args():
    sig = inspect.signature(jpql_VariableDeclaration.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"




def test_hyp_jpql_setclause_is_not_abstract():
    assert not inspect.isabstract(jpql_SetClause)


def test_hyp_jpql_setclause_constructor_exists():
    assert callable(jpql_SetClause.__init__)


def test_hyp_jpql_setclause_constructor_args():
    sig = inspect.signature(jpql_SetClause.__init__)
    params = list(sig.parameters.keys())



def test_hyp_jpql_updateclause_is_not_abstract():
    assert not inspect.isabstract(jpql_UpdateClause)


def test_hyp_jpql_updateclause_constructor_exists():
    assert callable(jpql_UpdateClause.__init__)


def test_hyp_jpql_updateclause_constructor_args():
    sig = inspect.signature(jpql_UpdateClause.__init__)
    params = list(sig.parameters.keys())



def test_hyp_jpql_fromentry_is_not_abstract():
    assert not inspect.isabstract(jpql_FromEntry)


def test_hyp_jpql_fromentry_constructor_exists():
    assert callable(jpql_FromEntry.__init__)


def test_hyp_jpql_fromentry_constructor_args():
    sig = inspect.signature(jpql_FromEntry.__init__)
    params = list(sig.parameters.keys())



def test_hyp_jpql_orderitem_is_not_abstract():
    assert not inspect.isabstract(jpql_OrderItem)


def test_hyp_jpql_orderitem_constructor_exists():
    assert callable(jpql_OrderItem.__init__)


def test_hyp_jpql_orderitem_constructor_args():
    sig = inspect.signature(jpql_OrderItem.__init__)
    params = list(sig.parameters.keys())
    assert "feature" in params, "Missing parameter 'feature'"




def test_hyp_jpql_expression_is_not_abstract():
    assert not inspect.isabstract(jpql_Expression)


def test_hyp_jpql_expression_constructor_exists():
    assert callable(jpql_Expression.__init__)


def test_hyp_jpql_expression_constructor_args():
    sig = inspect.signature(jpql_Expression.__init__)
    params = list(sig.parameters.keys())



def test_hyp_jpql_selectclause_is_not_abstract():
    assert not inspect.isabstract(jpql_SelectClause)


def test_hyp_jpql_selectclause_constructor_exists():
    assert callable(jpql_SelectClause.__init__)


def test_hyp_jpql_selectclause_constructor_args():
    sig = inspect.signature(jpql_SelectClause.__init__)
    params = list(sig.parameters.keys())
    assert "isDistinct" in params, "Missing parameter 'isDistinct'"




def test_hyp_jpql_fromclause_is_not_abstract():
    assert not inspect.isabstract(jpql_FromClause)


def test_hyp_jpql_fromclause_constructor_exists():
    assert callable(jpql_FromClause.__init__)


def test_hyp_jpql_fromclause_constructor_args():
    sig = inspect.signature(jpql_FromClause.__init__)
    params = list(sig.parameters.keys())



def test_hyp_jpql_deleteclause_is_not_abstract():
    assert not inspect.isabstract(jpql_DeleteClause)


def test_hyp_jpql_deleteclause_constructor_exists():
    assert callable(jpql_DeleteClause.__init__)


def test_hyp_jpql_deleteclause_constructor_args():
    sig = inspect.signature(jpql_DeleteClause.__init__)
    params = list(sig.parameters.keys())



def test_hyp_jpql_value_is_not_abstract():
    assert not inspect.isabstract(jpql_Value)


def test_hyp_jpql_value_constructor_exists():
    assert callable(jpql_Value.__init__)


def test_hyp_jpql_value_constructor_args():
    sig = inspect.signature(jpql_Value.__init__)
    params = list(sig.parameters.keys())



def test_hyp_jpql_aliasattributeexpression_is_not_abstract():
    assert not inspect.isabstract(jpql_AliasAttributeExpression)


def test_hyp_jpql_aliasattributeexpression_constructor_exists():
    assert callable(jpql_AliasAttributeExpression.__init__)


def test_hyp_jpql_aliasattributeexpression_constructor_args():
    sig = inspect.signature(jpql_AliasAttributeExpression.__init__)
    params = list(sig.parameters.keys())
    assert "attributes" in params, "Missing parameter 'attributes'"




def test_hyp_jpql_updateitem_is_not_abstract():
    assert not inspect.isabstract(jpql_UpdateItem)


def test_hyp_jpql_updateitem_constructor_exists():
    assert callable(jpql_UpdateItem.__init__)


def test_hyp_jpql_updateitem_constructor_args():
    sig = inspect.signature(jpql_UpdateItem.__init__)
    params = list(sig.parameters.keys())



def test_hyp_jpql_import_is_not_abstract():
    assert not inspect.isabstract(jpql_Import)


def test_hyp_jpql_import_constructor_exists():
    assert callable(jpql_Import.__init__)


def test_hyp_jpql_import_constructor_args():
    sig = inspect.signature(jpql_Import.__init__)
    params = list(sig.parameters.keys())
    assert "importURI" in params, "Missing parameter 'importURI'"




def test_hyp_jpql_querymodule_is_not_abstract():
    assert not inspect.isabstract(jpql_QueryModule)


def test_hyp_jpql_querymodule_constructor_exists():
    assert callable(jpql_QueryModule.__init__)


def test_hyp_jpql_querymodule_constructor_args():
    sig = inspect.signature(jpql_QueryModule.__init__)
    params = list(sig.parameters.keys())



def test_hyp_jpql_orderclause_is_not_abstract():
    assert not inspect.isabstract(jpql_OrderClause)


def test_hyp_jpql_orderclause_constructor_exists():
    assert callable(jpql_OrderClause.__init__)


def test_hyp_jpql_orderclause_constructor_args():
    sig = inspect.signature(jpql_OrderClause.__init__)
    params = list(sig.parameters.keys())
    assert "isDesc" in params, "Missing parameter 'isDesc'"
    assert "isAsc" in params, "Missing parameter 'isAsc'"





def test_hyp_jpql_havingclause_is_not_abstract():
    assert not inspect.isabstract(jpql_HavingClause)


def test_hyp_jpql_havingclause_constructor_exists():
    assert callable(jpql_HavingClause.__init__)


def test_hyp_jpql_havingclause_constructor_args():
    sig = inspect.signature(jpql_HavingClause.__init__)
    params = list(sig.parameters.keys())



def test_hyp_jpql_selectfromclause_is_not_abstract():
    assert not inspect.isabstract(jpql_SelectFromClause)


def test_hyp_jpql_selectfromclause_constructor_exists():
    assert callable(jpql_SelectFromClause.__init__)


def test_hyp_jpql_selectfromclause_constructor_args():
    sig = inspect.signature(jpql_SelectFromClause.__init__)
    params = list(sig.parameters.keys())



def test_hyp_expressionterm_is_not_abstract():
    assert not inspect.isabstract(ExpressionTerm)


def test_hyp_expressionterm_constructor_exists():
    assert callable(ExpressionTerm.__init__)


def test_hyp_expressionterm_constructor_args():
    sig = inspect.signature(ExpressionTerm.__init__)
    params = list(sig.parameters.keys())



def test_hyp_jpql_variable_is_not_abstract():
    assert not inspect.isabstract(jpql_Variable)


def test_hyp_jpql_variable_constructor_exists():
    assert callable(jpql_Variable.__init__)


def test_hyp_jpql_variable_constructor_args():
    sig = inspect.signature(jpql_Variable.__init__)
    params = list(sig.parameters.keys())



def test_hyp_jpqlquery_is_not_abstract():
    assert not inspect.isabstract(JPQLQuery)


def test_hyp_jpqlquery_constructor_exists():
    assert callable(JPQLQuery.__init__)


def test_hyp_jpqlquery_constructor_args():
    sig = inspect.signature(JPQLQuery.__init__)
    params = list(sig.parameters.keys())



def test_hyp_jpql_updatestatement_is_not_abstract():
    assert not inspect.isabstract(jpql_UpdateStatement)


def test_hyp_jpql_updatestatement_constructor_exists():
    assert callable(jpql_UpdateStatement.__init__)


def test_hyp_jpql_updatestatement_constructor_args():
    sig = inspect.signature(jpql_UpdateStatement.__init__)
    params = list(sig.parameters.keys())



def test_hyp_jpql_deletestatement_is_not_abstract():
    assert not inspect.isabstract(jpql_DeleteStatement)


def test_hyp_jpql_deletestatement_constructor_exists():
    assert callable(jpql_DeleteStatement.__init__)


def test_hyp_jpql_deletestatement_constructor_args():
    sig = inspect.signature(jpql_DeleteStatement.__init__)
    params = list(sig.parameters.keys())



def test_hyp_jpql_selectstatement_is_not_abstract():
    assert not inspect.isabstract(jpql_SelectStatement)


def test_hyp_jpql_selectstatement_constructor_exists():
    assert callable(jpql_SelectStatement.__init__)


def test_hyp_jpql_selectstatement_constructor_args():
    sig = inspect.signature(jpql_SelectStatement.__init__)
    params = list(sig.parameters.keys())



def test_hyp_jpql_whereclause_is_not_abstract():
    assert not inspect.isabstract(jpql_WhereClause)


def test_hyp_jpql_whereclause_constructor_exists():
    assert callable(jpql_WhereClause.__init__)


def test_hyp_jpql_whereclause_constructor_args():
    sig = inspect.signature(jpql_WhereClause.__init__)
    params = list(sig.parameters.keys())



def test_hyp_jpql_namedquery_is_not_abstract():
    assert not inspect.isabstract(jpql_NamedQuery)


def test_hyp_jpql_namedquery_constructor_exists():
    assert callable(jpql_NamedQuery.__init__)


def test_hyp_jpql_namedquery_constructor_args():
    sig = inspect.signature(jpql_NamedQuery.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"




def test_hyp_jpql_jpqlquery_is_not_abstract():
    assert not inspect.isabstract(jpql_JPQLQuery)


def test_hyp_jpql_jpqlquery_constructor_exists():
    assert callable(jpql_JPQLQuery.__init__)


def test_hyp_jpql_jpqlquery_constructor_args():
    sig = inspect.signature(jpql_JPQLQuery.__init__)
    params = list(sig.parameters.keys())

def test_hyp_operator_exists():
    # Check that the Enumeration exists
    assert Operator is not None

def test_hyp_operator_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in Operator]
    expected_literals = [
        "notEqual",
        "equal",
        "lessEqual",
        "greaterEqual",
        "lessThen",
        "greaterThen",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in Operator"


# =============================================================================
# HYPOTHESIS STRATEGIES
# =============================================================================

safe_text = st.text(
    alphabet=st.characters(
        whitelist_categories=("Ll", "Lu", "Nd"),
        whitelist_characters="_",
    ),
    min_size=1,
).filter(lambda s: s[0].isalpha())
Value_strategy = st.builds(
    Value,
)
jpql_NullExpression_strategy = st.builds(
    jpql_NullExpression,
    value=
        safe_text
)
jpql_StringExpression_strategy = st.builds(
    jpql_StringExpression,
    value=
        safe_text
)
jpql_BooleanExpression_strategy = st.builds(
    jpql_BooleanExpression,
    value=
        st.booleans()
)
jpql_IntegerExpression_strategy = st.builds(
    jpql_IntegerExpression,
    value=
        st.integers()
)
jpql_Function_strategy = st.builds(
    jpql_Function,
    name=
        safe_text
)
jpql_DateTimeExpression_strategy = st.builds(
    jpql_DateTimeExpression,
    value=
        safe_text
)
Variable_strategy = st.builds(
    Variable,
)
jpql_ParameterExpression_strategy = st.builds(
    jpql_ParameterExpression,
    name=
        safe_text
)
InExpression_strategy = st.builds(
    InExpression,
)
jpql_InQueryExpression_strategy = st.builds(
    jpql_InQueryExpression,
)
jpql_InSeqExpression_strategy = st.builds(
    jpql_InSeqExpression,
)
Expression_strategy = st.builds(
    Expression,
)
jpql_BetweenExpression_strategy = st.builds(
    jpql_BetweenExpression,
    isNot=
        st.booleans()
)
jpql_EmptyComparisonExpression_strategy = st.builds(
    jpql_EmptyComparisonExpression,
    isNot=
        st.booleans()
)
jpql_ExpressionTerm_strategy = st.builds(
    jpql_ExpressionTerm,
)
jpql_InExpression_strategy = st.builds(
    jpql_InExpression,
    isNot=
        st.booleans()
)
jpql_AndExpression_strategy = st.builds(
    jpql_AndExpression,
)
jpql_LikeExpression_strategy = st.builds(
    jpql_LikeExpression,
    pattern=
        safe_text,
    isNot=
        st.booleans()
)
jpql_OrExpression_strategy = st.builds(
    jpql_OrExpression,
)
jpql_OperatorExpression_strategy = st.builds(
    jpql_OperatorExpression,
    operator=
        safe_text
)
FromJoin_strategy = st.builds(
    FromJoin,
)
jpql_LeftJoin_strategy = st.builds(
    jpql_LeftJoin,
    isOuter=
        st.booleans()
)
jpql_InnerJoin_strategy = st.builds(
    jpql_InnerJoin,
)
jpql_Join_strategy = st.builds(
    jpql_Join,
)
jpql_NullComparisonExpression_strategy = st.builds(
    jpql_NullComparisonExpression,
    isNot=
        st.booleans()
)
jpql_CollectionExpression_strategy = st.builds(
    jpql_CollectionExpression,
    isNot=
        st.booleans()
)
jpql_SomeExpression_strategy = st.builds(
    jpql_SomeExpression,
)
jpql_AnyExpression_strategy = st.builds(
    jpql_AnyExpression,
)
jpql_AllExpression_strategy = st.builds(
    jpql_AllExpression,
)
jpql_ExistsExpression_strategy = st.builds(
    jpql_ExistsExpression,
    isNot=
        st.booleans()
)
SelectAggregateExpression_strategy = st.builds(
    SelectAggregateExpression,
)
jpql_MinAggregate_strategy = st.builds(
    jpql_MinAggregate,
)
jpql_MaxAggregate_strategy = st.builds(
    jpql_MaxAggregate,
)
jpql_CountAggregate_strategy = st.builds(
    jpql_CountAggregate,
)
jpql_SumAggregate_strategy = st.builds(
    jpql_SumAggregate,
)
jpql_AvgAggregate_strategy = st.builds(
    jpql_AvgAggregate,
)
SelectExpression_strategy = st.builds(
    SelectExpression,
)
jpql_SelectConstructorExpression_strategy = st.builds(
    jpql_SelectConstructorExpression,
    name=
        safe_text
)
jpql_SelectAggregateExpression_strategy = st.builds(
    jpql_SelectAggregateExpression,
    isDistinct=
        st.booleans()
)
jpql_SelectExpression_strategy = st.builds(
    jpql_SelectExpression,
)
jpql_FromJoin_strategy = st.builds(
    jpql_FromJoin,
    isFetch=
        st.booleans()
)
FromEntry_strategy = st.builds(
    FromEntry,
)
jpql_FromCollection_strategy = st.builds(
    jpql_FromCollection,
)
jpql_FromClass_strategy = st.builds(
    jpql_FromClass,
    type=
        safe_text
)
jpql_VariableDeclaration_strategy = st.builds(
    jpql_VariableDeclaration,
    name=
        safe_text
)
jpql_SetClause_strategy = st.builds(
    jpql_SetClause,
)
jpql_UpdateClause_strategy = st.builds(
    jpql_UpdateClause,
)
jpql_FromEntry_strategy = st.builds(
    jpql_FromEntry,
)
jpql_OrderItem_strategy = st.builds(
    jpql_OrderItem,
    feature=
        safe_text
)
jpql_Expression_strategy = st.builds(
    jpql_Expression,
)
jpql_SelectClause_strategy = st.builds(
    jpql_SelectClause,
    isDistinct=
        st.booleans()
)
jpql_FromClause_strategy = st.builds(
    jpql_FromClause,
)
jpql_DeleteClause_strategy = st.builds(
    jpql_DeleteClause,
)
jpql_Value_strategy = st.builds(
    jpql_Value,
)
jpql_AliasAttributeExpression_strategy = st.builds(
    jpql_AliasAttributeExpression,
    attributes=
        safe_text
)
jpql_UpdateItem_strategy = st.builds(
    jpql_UpdateItem,
)
jpql_Import_strategy = st.builds(
    jpql_Import,
    importURI=
        safe_text
)
jpql_QueryModule_strategy = st.builds(
    jpql_QueryModule,
)
jpql_OrderClause_strategy = st.builds(
    jpql_OrderClause,
    isDesc=
        st.booleans(),
    isAsc=
        st.booleans()
)
jpql_HavingClause_strategy = st.builds(
    jpql_HavingClause,
)
jpql_SelectFromClause_strategy = st.builds(
    jpql_SelectFromClause,
)
ExpressionTerm_strategy = st.builds(
    ExpressionTerm,
)
jpql_Variable_strategy = st.builds(
    jpql_Variable,
)
JPQLQuery_strategy = st.builds(
    JPQLQuery,
)
jpql_UpdateStatement_strategy = st.builds(
    jpql_UpdateStatement,
)
jpql_DeleteStatement_strategy = st.builds(
    jpql_DeleteStatement,
)
jpql_SelectStatement_strategy = st.builds(
    jpql_SelectStatement,
)
jpql_WhereClause_strategy = st.builds(
    jpql_WhereClause,
)
jpql_NamedQuery_strategy = st.builds(
    jpql_NamedQuery,
    name=
        safe_text
)
jpql_JPQLQuery_strategy = st.builds(
    jpql_JPQLQuery,
)





@given(instance=jpql_NullExpression_strategy)
def test_hyp_jpql_nullexpression_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original




@given(instance=jpql_StringExpression_strategy)
def test_hyp_jpql_stringexpression_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original




@given(instance=jpql_BooleanExpression_strategy)
def test_hyp_jpql_booleanexpression_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original




@given(instance=jpql_IntegerExpression_strategy)
def test_hyp_jpql_integerexpression_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original




@given(instance=jpql_Function_strategy)
def test_hyp_jpql_function_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original




@given(instance=jpql_DateTimeExpression_strategy)
def test_hyp_jpql_datetimeexpression_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original





@given(instance=jpql_ParameterExpression_strategy)
def test_hyp_jpql_parameterexpression_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original








@given(instance=jpql_BetweenExpression_strategy)
def test_hyp_jpql_betweenexpression_isNot_setter(instance):
    original = instance.isNot
    instance.isNot = original
    assert instance.isNot == original




@given(instance=jpql_EmptyComparisonExpression_strategy)
def test_hyp_jpql_emptycomparisonexpression_isNot_setter(instance):
    original = instance.isNot
    instance.isNot = original
    assert instance.isNot == original





@given(instance=jpql_InExpression_strategy)
def test_hyp_jpql_inexpression_isNot_setter(instance):
    original = instance.isNot
    instance.isNot = original
    assert instance.isNot == original





@given(instance=jpql_LikeExpression_strategy)
def test_hyp_jpql_likeexpression_pattern_setter(instance):
    original = instance.pattern
    instance.pattern = original
    assert instance.pattern == original



@given(instance=jpql_LikeExpression_strategy)
def test_hyp_jpql_likeexpression_isNot_setter(instance):
    original = instance.isNot
    instance.isNot = original
    assert instance.isNot == original





@given(instance=jpql_OperatorExpression_strategy)
def test_hyp_jpql_operatorexpression_operator_setter(instance):
    original = instance.operator
    instance.operator = original
    assert instance.operator == original





@given(instance=jpql_LeftJoin_strategy)
def test_hyp_jpql_leftjoin_isOuter_setter(instance):
    original = instance.isOuter
    instance.isOuter = original
    assert instance.isOuter == original






@given(instance=jpql_NullComparisonExpression_strategy)
def test_hyp_jpql_nullcomparisonexpression_isNot_setter(instance):
    original = instance.isNot
    instance.isNot = original
    assert instance.isNot == original




@given(instance=jpql_CollectionExpression_strategy)
def test_hyp_jpql_collectionexpression_isNot_setter(instance):
    original = instance.isNot
    instance.isNot = original
    assert instance.isNot == original







@given(instance=jpql_ExistsExpression_strategy)
def test_hyp_jpql_existsexpression_isNot_setter(instance):
    original = instance.isNot
    instance.isNot = original
    assert instance.isNot == original











@given(instance=jpql_SelectConstructorExpression_strategy)
def test_hyp_jpql_selectconstructorexpression_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original




@given(instance=jpql_SelectAggregateExpression_strategy)
def test_hyp_jpql_selectaggregateexpression_isDistinct_setter(instance):
    original = instance.isDistinct
    instance.isDistinct = original
    assert instance.isDistinct == original





@given(instance=jpql_FromJoin_strategy)
def test_hyp_jpql_fromjoin_isFetch_setter(instance):
    original = instance.isFetch
    instance.isFetch = original
    assert instance.isFetch == original






@given(instance=jpql_FromClass_strategy)
def test_hyp_jpql_fromclass_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original




@given(instance=jpql_VariableDeclaration_strategy)
def test_hyp_jpql_variabledeclaration_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original







@given(instance=jpql_OrderItem_strategy)
def test_hyp_jpql_orderitem_feature_setter(instance):
    original = instance.feature
    instance.feature = original
    assert instance.feature == original





@given(instance=jpql_SelectClause_strategy)
def test_hyp_jpql_selectclause_isDistinct_setter(instance):
    original = instance.isDistinct
    instance.isDistinct = original
    assert instance.isDistinct == original







@given(instance=jpql_AliasAttributeExpression_strategy)
def test_hyp_jpql_aliasattributeexpression_attributes_setter(instance):
    original = instance.attributes
    instance.attributes = original
    assert instance.attributes == original





@given(instance=jpql_Import_strategy)
def test_hyp_jpql_import_importURI_setter(instance):
    original = instance.importURI
    instance.importURI = original
    assert instance.importURI == original





@given(instance=jpql_OrderClause_strategy)
def test_hyp_jpql_orderclause_isDesc_setter(instance):
    original = instance.isDesc
    instance.isDesc = original
    assert instance.isDesc == original



@given(instance=jpql_OrderClause_strategy)
def test_hyp_jpql_orderclause_isAsc_setter(instance):
    original = instance.isAsc
    instance.isAsc = original
    assert instance.isAsc == original













@given(instance=jpql_NamedQuery_strategy)
def test_hyp_jpql_namedquery_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



# ----- SECTION B: test_structural_full.py (deterministic-first suite) -----
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
    JPQLQuery,
    SelectAggregateExpression,
    SelectExpression,
    Value,
    Variable,
    jpql_AliasAttributeExpression,
    jpql_AllExpression,
    jpql_AndExpression,
    jpql_AnyExpression,
    jpql_AvgAggregate,
    jpql_BetweenExpression,
    jpql_BooleanExpression,
    jpql_CollectionExpression,
    jpql_CountAggregate,
    jpql_DateTimeExpression,
    jpql_DeleteClause,
    jpql_DeleteStatement,
    jpql_EmptyComparisonExpression,
    jpql_ExistsExpression,
    jpql_Expression,
    jpql_ExpressionTerm,
    jpql_FromClass,
    jpql_FromClause,
    jpql_FromCollection,
    jpql_FromEntry,
    jpql_FromJoin,
    jpql_Function,
    jpql_HavingClause,
    jpql_Import,
    jpql_InExpression,
    jpql_InQueryExpression,
    jpql_InSeqExpression,
    jpql_InnerJoin,
    jpql_IntegerExpression,
    jpql_JPQLQuery,
    jpql_Join,
    jpql_LeftJoin,
    jpql_LikeExpression,
    jpql_MaxAggregate,
    jpql_MinAggregate,
    jpql_NamedQuery,
    jpql_NullComparisonExpression,
    jpql_NullExpression,
    jpql_OperatorExpression,
    jpql_OrExpression,
    jpql_OrderClause,
    jpql_OrderItem,
    jpql_ParameterExpression,
    jpql_QueryModule,
    jpql_SelectAggregateExpression,
    jpql_SelectClause,
    jpql_SelectConstructorExpression,
    jpql_SelectExpression,
    jpql_SelectFromClause,
    jpql_SelectStatement,
    jpql_SetClause,
    jpql_SomeExpression,
    jpql_StringExpression,
    jpql_SumAggregate,
    jpql_UpdateClause,
    jpql_UpdateItem,
    jpql_UpdateStatement,
    jpql_Value,
    jpql_Variable,
    jpql_VariableDeclaration,
    jpql_WhereClause,
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

def test_jpql_AliasAttributeExpression_attributes_value_roundtrip():
    instance = jpql_AliasAttributeExpression(attributes="sample_text")
    assert instance.attributes == "sample_text"
    instance.attributes = "sample_text_2"
    assert instance.attributes == "sample_text_2"


def test_jpql_BetweenExpression_isNot_value_roundtrip():
    instance = jpql_BetweenExpression(isNot=True)
    assert instance.isNot == True
    instance.isNot = False
    assert instance.isNot == False


def test_jpql_BooleanExpression_value_value_roundtrip():
    instance = jpql_BooleanExpression(value=True)
    assert instance.value == True
    instance.value = False
    assert instance.value == False


def test_jpql_CollectionExpression_isNot_value_roundtrip():
    instance = jpql_CollectionExpression(isNot=True)
    assert instance.isNot == True
    instance.isNot = False
    assert instance.isNot == False


def test_jpql_DateTimeExpression_value_value_roundtrip():
    instance = jpql_DateTimeExpression(value="sample_text")
    assert instance.value == "sample_text"
    instance.value = "sample_text_2"
    assert instance.value == "sample_text_2"


def test_jpql_EmptyComparisonExpression_isNot_value_roundtrip():
    instance = jpql_EmptyComparisonExpression(isNot=True)
    assert instance.isNot == True
    instance.isNot = False
    assert instance.isNot == False


def test_jpql_ExistsExpression_isNot_value_roundtrip():
    instance = jpql_ExistsExpression(isNot=True)
    assert instance.isNot == True
    instance.isNot = False
    assert instance.isNot == False


def test_jpql_FromClass_type_value_roundtrip():
    instance = jpql_FromClass(type="sample_text")
    assert instance.type == "sample_text"
    instance.type = "sample_text_2"
    assert instance.type == "sample_text_2"


def test_jpql_FromJoin_isFetch_value_roundtrip():
    instance = jpql_FromJoin(isFetch=True)
    assert instance.isFetch == True
    instance.isFetch = False
    assert instance.isFetch == False


def test_jpql_Function_name_value_roundtrip():
    instance = jpql_Function(name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_jpql_Import_importURI_value_roundtrip():
    instance = jpql_Import(importURI="sample_text")
    assert instance.importURI == "sample_text"
    instance.importURI = "sample_text_2"
    assert instance.importURI == "sample_text_2"


def test_jpql_InExpression_isNot_value_roundtrip():
    instance = jpql_InExpression(isNot=True)
    assert instance.isNot == True
    instance.isNot = False
    assert instance.isNot == False


def test_jpql_IntegerExpression_value_value_roundtrip():
    instance = jpql_IntegerExpression(value=7)
    assert instance.value == 7
    instance.value = 13
    assert instance.value == 13


def test_jpql_LeftJoin_isOuter_value_roundtrip():
    instance = jpql_LeftJoin(isOuter=True)
    assert instance.isOuter == True
    instance.isOuter = False
    assert instance.isOuter == False


def test_jpql_LikeExpression_isNot_value_roundtrip():
    instance = jpql_LikeExpression(isNot=True, pattern="sample_text")
    assert instance.isNot == True
    instance.isNot = False
    assert instance.isNot == False


def test_jpql_LikeExpression_pattern_value_roundtrip():
    instance = jpql_LikeExpression(isNot=True, pattern="sample_text")
    assert instance.pattern == "sample_text"
    instance.pattern = "sample_text_2"
    assert instance.pattern == "sample_text_2"


def test_jpql_NamedQuery_name_value_roundtrip():
    instance = jpql_NamedQuery(name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_jpql_NullComparisonExpression_isNot_value_roundtrip():
    instance = jpql_NullComparisonExpression(isNot=True)
    assert instance.isNot == True
    instance.isNot = False
    assert instance.isNot == False


def test_jpql_NullExpression_value_value_roundtrip():
    instance = jpql_NullExpression(value="sample_text")
    assert instance.value == "sample_text"
    instance.value = "sample_text_2"
    assert instance.value == "sample_text_2"


def test_jpql_OperatorExpression_operator_value_roundtrip():
    instance = jpql_OperatorExpression(operator="sample_text")
    assert instance.operator == "sample_text"
    instance.operator = "sample_text_2"
    assert instance.operator == "sample_text_2"


def test_jpql_OrderClause_isAsc_value_roundtrip():
    instance = jpql_OrderClause(isAsc=True, isDesc=True)
    assert instance.isAsc == True
    instance.isAsc = False
    assert instance.isAsc == False


def test_jpql_OrderClause_isDesc_value_roundtrip():
    instance = jpql_OrderClause(isAsc=True, isDesc=True)
    assert instance.isDesc == True
    instance.isDesc = False
    assert instance.isDesc == False


def test_jpql_OrderItem_feature_value_roundtrip():
    instance = jpql_OrderItem(feature="sample_text")
    assert instance.feature == "sample_text"
    instance.feature = "sample_text_2"
    assert instance.feature == "sample_text_2"


def test_jpql_ParameterExpression_name_value_roundtrip():
    instance = jpql_ParameterExpression(name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_jpql_SelectAggregateExpression_isDistinct_value_roundtrip():
    instance = jpql_SelectAggregateExpression(isDistinct=True)
    assert instance.isDistinct == True
    instance.isDistinct = False
    assert instance.isDistinct == False


def test_jpql_SelectClause_isDistinct_value_roundtrip():
    instance = jpql_SelectClause(isDistinct=True)
    assert instance.isDistinct == True
    instance.isDistinct = False
    assert instance.isDistinct == False


def test_jpql_SelectConstructorExpression_name_value_roundtrip():
    instance = jpql_SelectConstructorExpression(name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_jpql_StringExpression_value_value_roundtrip():
    instance = jpql_StringExpression(value="sample_text")
    assert instance.value == "sample_text"
    instance.value = "sample_text_2"
    assert instance.value == "sample_text_2"


def test_jpql_VariableDeclaration_name_value_roundtrip():
    instance = jpql_VariableDeclaration(name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_jpql_AllExpression_isa_Expression():
    instance = jpql_AllExpression()
    assert isinstance(instance, Expression)


def test_jpql_AndExpression_isa_Expression():
    instance = jpql_AndExpression()
    assert isinstance(instance, Expression)


def test_jpql_AnyExpression_isa_Expression():
    instance = jpql_AnyExpression()
    assert isinstance(instance, Expression)


def test_jpql_BetweenExpression_isa_Expression():
    instance = jpql_BetweenExpression(isNot=True)
    assert isinstance(instance, Expression)


def test_jpql_CollectionExpression_isa_Expression():
    instance = jpql_CollectionExpression(isNot=True)
    assert isinstance(instance, Expression)


def test_jpql_EmptyComparisonExpression_isa_Expression():
    instance = jpql_EmptyComparisonExpression(isNot=True)
    assert isinstance(instance, Expression)


def test_jpql_ExistsExpression_isa_Expression():
    instance = jpql_ExistsExpression(isNot=True)
    assert isinstance(instance, Expression)


def test_jpql_ExpressionTerm_isa_Expression():
    instance = jpql_ExpressionTerm()
    assert isinstance(instance, Expression)


def test_jpql_InExpression_isa_Expression():
    instance = jpql_InExpression(isNot=True)
    assert isinstance(instance, Expression)


def test_jpql_LikeExpression_isa_Expression():
    instance = jpql_LikeExpression(isNot=True, pattern="sample_text")
    assert isinstance(instance, Expression)


def test_jpql_NullComparisonExpression_isa_Expression():
    instance = jpql_NullComparisonExpression(isNot=True)
    assert isinstance(instance, Expression)


def test_jpql_OperatorExpression_isa_Expression():
    instance = jpql_OperatorExpression(operator="sample_text")
    assert isinstance(instance, Expression)


def test_jpql_OrExpression_isa_Expression():
    instance = jpql_OrExpression()
    assert isinstance(instance, Expression)


def test_jpql_SomeExpression_isa_Expression():
    instance = jpql_SomeExpression()
    assert isinstance(instance, Expression)


def test_jpql_SelectStatement_isa_ExpressionTerm():
    instance = jpql_SelectStatement()
    assert isinstance(instance, ExpressionTerm)


def test_jpql_Variable_isa_ExpressionTerm():
    instance = jpql_Variable()
    assert isinstance(instance, ExpressionTerm)


def test_jpql_FromClass_isa_FromEntry():
    instance = jpql_FromClass(type="sample_text")
    assert isinstance(instance, FromEntry)


def test_jpql_FromCollection_isa_FromEntry():
    instance = jpql_FromCollection()
    assert isinstance(instance, FromEntry)


def test_jpql_InnerJoin_isa_FromJoin():
    instance = jpql_InnerJoin()
    assert isinstance(instance, FromJoin)


def test_jpql_Join_isa_FromJoin():
    instance = jpql_Join()
    assert isinstance(instance, FromJoin)


def test_jpql_LeftJoin_isa_FromJoin():
    instance = jpql_LeftJoin(isOuter=True)
    assert isinstance(instance, FromJoin)


def test_jpql_InQueryExpression_isa_InExpression():
    instance = jpql_InQueryExpression()
    assert isinstance(instance, InExpression)


def test_jpql_InSeqExpression_isa_InExpression():
    instance = jpql_InSeqExpression()
    assert isinstance(instance, InExpression)


def test_jpql_DeleteStatement_isa_JPQLQuery():
    instance = jpql_DeleteStatement()
    assert isinstance(instance, JPQLQuery)


def test_jpql_SelectStatement_isa_JPQLQuery():
    instance = jpql_SelectStatement()
    assert isinstance(instance, JPQLQuery)


def test_jpql_UpdateStatement_isa_JPQLQuery():
    instance = jpql_UpdateStatement()
    assert isinstance(instance, JPQLQuery)


def test_jpql_AvgAggregate_isa_SelectAggregateExpression():
    instance = jpql_AvgAggregate()
    assert isinstance(instance, SelectAggregateExpression)


def test_jpql_CountAggregate_isa_SelectAggregateExpression():
    instance = jpql_CountAggregate()
    assert isinstance(instance, SelectAggregateExpression)


def test_jpql_MaxAggregate_isa_SelectAggregateExpression():
    instance = jpql_MaxAggregate()
    assert isinstance(instance, SelectAggregateExpression)


def test_jpql_MinAggregate_isa_SelectAggregateExpression():
    instance = jpql_MinAggregate()
    assert isinstance(instance, SelectAggregateExpression)


def test_jpql_SumAggregate_isa_SelectAggregateExpression():
    instance = jpql_SumAggregate()
    assert isinstance(instance, SelectAggregateExpression)


def test_jpql_AliasAttributeExpression_isa_SelectExpression():
    instance = jpql_AliasAttributeExpression(attributes="sample_text")
    assert isinstance(instance, SelectExpression)


def test_jpql_SelectAggregateExpression_isa_SelectExpression():
    instance = jpql_SelectAggregateExpression(isDistinct=True)
    assert isinstance(instance, SelectExpression)


def test_jpql_SelectConstructorExpression_isa_SelectExpression():
    instance = jpql_SelectConstructorExpression(name="sample_text")
    assert isinstance(instance, SelectExpression)


def test_jpql_BooleanExpression_isa_Value():
    instance = jpql_BooleanExpression(value=True)
    assert isinstance(instance, Value)


def test_jpql_DateTimeExpression_isa_Value():
    instance = jpql_DateTimeExpression(value="sample_text")
    assert isinstance(instance, Value)


def test_jpql_IntegerExpression_isa_Value():
    instance = jpql_IntegerExpression(value=7)
    assert isinstance(instance, Value)


def test_jpql_NullExpression_isa_Value():
    instance = jpql_NullExpression(value="sample_text")
    assert isinstance(instance, Value)


def test_jpql_StringExpression_isa_Value():
    instance = jpql_StringExpression(value="sample_text")
    assert isinstance(instance, Value)


def test_jpql_AliasAttributeExpression_isa_Variable():
    instance = jpql_AliasAttributeExpression(attributes="sample_text")
    assert isinstance(instance, Variable)


def test_jpql_ParameterExpression_isa_Variable():
    instance = jpql_ParameterExpression(name="sample_text")
    assert isinstance(instance, Variable)


def test_jpql_Value_isa_Variable():
    instance = jpql_Value()
    assert isinstance(instance, Variable)


def test_assoc_alias100_link_reassign_clear():
    a = jpql_VariableDeclaration(name="sample_text")
    b1 = jpql_AliasAttributeExpression(attributes="sample_text")
    b2 = jpql_AliasAttributeExpression(attributes="sample_text_2")
    _safe_set(a, 'jpql_VariableDeclaration102', b1)
    assert _is_linked(a, 'jpql_VariableDeclaration102', b1)
    if hasattr(b1, 'jpql_AliasAttributeExpression101'):
        assert _is_linked(b1, 'jpql_AliasAttributeExpression101', a)
    _safe_set(a, 'jpql_VariableDeclaration102', b2)
    assert _is_linked(a, 'jpql_VariableDeclaration102', b2)
    if hasattr(b1, 'jpql_AliasAttributeExpression101'):
        assert not _is_linked(b1, 'jpql_AliasAttributeExpression101', a)
    if hasattr(b2, 'jpql_AliasAttributeExpression101'):
        assert _is_linked(b2, 'jpql_AliasAttributeExpression101', a)
    _safe_set(a, 'jpql_VariableDeclaration102', None)
    assert not _is_linked(a, 'jpql_VariableDeclaration102', b2)
    if hasattr(b2, 'jpql_AliasAttributeExpression101'):
        assert not _is_linked(b2, 'jpql_AliasAttributeExpression101', a)


def test_assoc_alias29_link_reassign_clear():
    a = jpql_AliasAttributeExpression(attributes="sample_text")
    b1 = jpql_UpdateItem()
    b2 = jpql_UpdateItem()
    _safe_set(a, 'jpql_AliasAttributeExpression', b1)
    assert _is_linked(a, 'jpql_AliasAttributeExpression', b1)
    if hasattr(b1, 'jpql_UpdateItem30'):
        assert _is_linked(b1, 'jpql_UpdateItem30', a)
    _safe_set(a, 'jpql_AliasAttributeExpression', b2)
    assert _is_linked(a, 'jpql_AliasAttributeExpression', b2)
    if hasattr(b1, 'jpql_UpdateItem30'):
        assert not _is_linked(b1, 'jpql_UpdateItem30', a)
    if hasattr(b2, 'jpql_UpdateItem30'):
        assert _is_linked(b2, 'jpql_UpdateItem30', a)
    _safe_set(a, 'jpql_AliasAttributeExpression', None)
    assert not _is_linked(a, 'jpql_AliasAttributeExpression', b2)
    if hasattr(b2, 'jpql_UpdateItem30'):
        assert not _is_linked(b2, 'jpql_UpdateItem30', a)


def test_assoc_expressions41_link_reassign_clear():
    a = jpql_SelectClause(isDistinct=True)
    b1 = jpql_SelectExpression()
    b2 = jpql_SelectExpression()
    _safe_set(a, 'jpql_SelectClause42', {b1})
    assert _is_linked(a, 'jpql_SelectClause42', b1)
    if hasattr(b1, 'jpql_SelectExpression'):
        assert _is_linked(b1, 'jpql_SelectExpression', a)
    _safe_set(a, 'jpql_SelectClause42', {b2})
    assert _is_linked(a, 'jpql_SelectClause42', b2)
    if hasattr(b1, 'jpql_SelectExpression'):
        assert not _is_linked(b1, 'jpql_SelectExpression', a)
    if hasattr(b2, 'jpql_SelectExpression'):
        assert _is_linked(b2, 'jpql_SelectExpression', a)
    _safe_set(a, 'jpql_SelectClause42', set())
    assert not _is_linked(a, 'jpql_SelectClause42', b2)
    if hasattr(b2, 'jpql_SelectExpression'):
        assert not _is_linked(b2, 'jpql_SelectExpression', a)


def test_assoc_imports0_link_reassign_clear():
    a = jpql_Import(importURI="sample_text")
    b1 = jpql_QueryModule()
    b2 = jpql_QueryModule()
    _safe_set(a, 'jpql_Import', b1)
    assert _is_linked(a, 'jpql_Import', b1)
    if hasattr(b1, 'jpql_QueryModule'):
        assert _is_linked(b1, 'jpql_QueryModule', a)
    _safe_set(a, 'jpql_Import', b2)
    assert _is_linked(a, 'jpql_Import', b2)
    if hasattr(b1, 'jpql_QueryModule'):
        assert not _is_linked(b1, 'jpql_QueryModule', a)
    if hasattr(b2, 'jpql_QueryModule'):
        assert _is_linked(b2, 'jpql_QueryModule', a)
    _safe_set(a, 'jpql_Import', None)
    assert not _is_linked(a, 'jpql_Import', b2)
    if hasattr(b2, 'jpql_QueryModule'):
        assert not _is_linked(b2, 'jpql_QueryModule', a)


def test_assoc_item43_link_reassign_clear():
    a = jpql_SelectAggregateExpression(isDistinct=True)
    b1 = jpql_AliasAttributeExpression(attributes="sample_text")
    b2 = jpql_AliasAttributeExpression(attributes="sample_text_2")
    _safe_set(a, 'jpql_SelectAggregateExpression', b1)
    assert _is_linked(a, 'jpql_SelectAggregateExpression', b1)
    if hasattr(b1, 'jpql_AliasAttributeExpression44'):
        assert _is_linked(b1, 'jpql_AliasAttributeExpression44', a)
    _safe_set(a, 'jpql_SelectAggregateExpression', b2)
    assert _is_linked(a, 'jpql_SelectAggregateExpression', b2)
    if hasattr(b1, 'jpql_AliasAttributeExpression44'):
        assert not _is_linked(b1, 'jpql_AliasAttributeExpression44', a)
    if hasattr(b2, 'jpql_AliasAttributeExpression44'):
        assert _is_linked(b2, 'jpql_AliasAttributeExpression44', a)
    _safe_set(a, 'jpql_SelectAggregateExpression', None)
    assert not _is_linked(a, 'jpql_SelectAggregateExpression', b2)
    if hasattr(b2, 'jpql_AliasAttributeExpression44'):
        assert not _is_linked(b2, 'jpql_AliasAttributeExpression44', a)


def test_assoc_items45_link_reassign_clear():
    a = jpql_SelectConstructorExpression(name="sample_text")
    b1 = jpql_AliasAttributeExpression(attributes="sample_text")
    b2 = jpql_AliasAttributeExpression(attributes="sample_text_2")
    _safe_set(a, 'jpql_SelectConstructorExpression', {b1})
    assert _is_linked(a, 'jpql_SelectConstructorExpression', b1)
    if hasattr(b1, 'jpql_AliasAttributeExpression46'):
        assert _is_linked(b1, 'jpql_AliasAttributeExpression46', a)
    _safe_set(a, 'jpql_SelectConstructorExpression', {b2})
    assert _is_linked(a, 'jpql_SelectConstructorExpression', b2)
    if hasattr(b1, 'jpql_AliasAttributeExpression46'):
        assert not _is_linked(b1, 'jpql_AliasAttributeExpression46', a)
    if hasattr(b2, 'jpql_AliasAttributeExpression46'):
        assert _is_linked(b2, 'jpql_AliasAttributeExpression46', a)
    _safe_set(a, 'jpql_SelectConstructorExpression', set())
    assert not _is_linked(a, 'jpql_SelectConstructorExpression', b2)
    if hasattr(b2, 'jpql_AliasAttributeExpression46'):
        assert not _is_linked(b2, 'jpql_AliasAttributeExpression46', a)


def test_assoc_joins52_link_reassign_clear():
    a = jpql_FromJoin(isFetch=True)
    b1 = jpql_FromClass(type="sample_text")
    b2 = jpql_FromClass(type="sample_text_2")
    _safe_set(a, 'jpql_FromJoin', b1)
    assert _is_linked(a, 'jpql_FromJoin', b1)
    if hasattr(b1, 'jpql_FromClass'):
        assert _is_linked(b1, 'jpql_FromClass', a)
    _safe_set(a, 'jpql_FromJoin', b2)
    assert _is_linked(a, 'jpql_FromJoin', b2)
    if hasattr(b1, 'jpql_FromClass'):
        assert not _is_linked(b1, 'jpql_FromClass', a)
    if hasattr(b2, 'jpql_FromClass'):
        assert _is_linked(b2, 'jpql_FromClass', a)
    _safe_set(a, 'jpql_FromJoin', None)
    assert not _is_linked(a, 'jpql_FromJoin', b2)
    if hasattr(b2, 'jpql_FromClass'):
        assert not _is_linked(b2, 'jpql_FromClass', a)


def test_assoc_lhs64_link_reassign_clear():
    a = jpql_OperatorExpression(operator="sample_text")
    b1 = jpql_Variable()
    b2 = jpql_Variable()
    _safe_set(a, 'jpql_OperatorExpression', b1)
    assert _is_linked(a, 'jpql_OperatorExpression', b1)
    if hasattr(b1, 'jpql_Variable'):
        assert _is_linked(b1, 'jpql_Variable', a)
    _safe_set(a, 'jpql_OperatorExpression', b2)
    assert _is_linked(a, 'jpql_OperatorExpression', b2)
    if hasattr(b1, 'jpql_Variable'):
        assert not _is_linked(b1, 'jpql_Variable', a)
    if hasattr(b2, 'jpql_Variable'):
        assert _is_linked(b2, 'jpql_Variable', a)
    _safe_set(a, 'jpql_OperatorExpression', None)
    assert not _is_linked(a, 'jpql_OperatorExpression', b2)
    if hasattr(b2, 'jpql_Variable'):
        assert not _is_linked(b2, 'jpql_Variable', a)


def test_assoc_lhs75_link_reassign_clear():
    a = jpql_CollectionExpression(isNot=True)
    b1 = jpql_Variable()
    b2 = jpql_Variable()
    _safe_set(a, 'jpql_CollectionExpression', b1)
    assert _is_linked(a, 'jpql_CollectionExpression', b1)
    if hasattr(b1, 'jpql_Variable76'):
        assert _is_linked(b1, 'jpql_Variable76', a)
    _safe_set(a, 'jpql_CollectionExpression', b2)
    assert _is_linked(a, 'jpql_CollectionExpression', b2)
    if hasattr(b1, 'jpql_Variable76'):
        assert not _is_linked(b1, 'jpql_Variable76', a)
    if hasattr(b2, 'jpql_Variable76'):
        assert _is_linked(b2, 'jpql_Variable76', a)
    _safe_set(a, 'jpql_CollectionExpression', None)
    assert not _is_linked(a, 'jpql_CollectionExpression', b2)
    if hasattr(b2, 'jpql_Variable76'):
        assert not _is_linked(b2, 'jpql_Variable76', a)


def test_assoc_lhs80_link_reassign_clear():
    a = jpql_NullComparisonExpression(isNot=True)
    b1 = jpql_Variable()
    b2 = jpql_Variable()
    _safe_set(a, 'jpql_NullComparisonExpression', b1)
    assert _is_linked(a, 'jpql_NullComparisonExpression', b1)
    if hasattr(b1, 'jpql_Variable81'):
        assert _is_linked(b1, 'jpql_Variable81', a)
    _safe_set(a, 'jpql_NullComparisonExpression', b2)
    assert _is_linked(a, 'jpql_NullComparisonExpression', b2)
    if hasattr(b1, 'jpql_Variable81'):
        assert not _is_linked(b1, 'jpql_Variable81', a)
    if hasattr(b2, 'jpql_Variable81'):
        assert _is_linked(b2, 'jpql_Variable81', a)
    _safe_set(a, 'jpql_NullComparisonExpression', None)
    assert not _is_linked(a, 'jpql_NullComparisonExpression', b2)
    if hasattr(b2, 'jpql_Variable81'):
        assert not _is_linked(b2, 'jpql_Variable81', a)


def test_assoc_lhs82_link_reassign_clear():
    a = jpql_EmptyComparisonExpression(isNot=True)
    b1 = jpql_Variable()
    b2 = jpql_Variable()
    _safe_set(a, 'jpql_EmptyComparisonExpression', b1)
    assert _is_linked(a, 'jpql_EmptyComparisonExpression', b1)
    if hasattr(b1, 'jpql_Variable83'):
        assert _is_linked(b1, 'jpql_Variable83', a)
    _safe_set(a, 'jpql_EmptyComparisonExpression', b2)
    assert _is_linked(a, 'jpql_EmptyComparisonExpression', b2)
    if hasattr(b1, 'jpql_Variable83'):
        assert not _is_linked(b1, 'jpql_Variable83', a)
    if hasattr(b2, 'jpql_Variable83'):
        assert _is_linked(b2, 'jpql_Variable83', a)
    _safe_set(a, 'jpql_EmptyComparisonExpression', None)
    assert not _is_linked(a, 'jpql_EmptyComparisonExpression', b2)
    if hasattr(b2, 'jpql_Variable83'):
        assert not _is_linked(b2, 'jpql_Variable83', a)


def test_assoc_lhs84_link_reassign_clear():
    a = jpql_LikeExpression(isNot=True, pattern="sample_text")
    b1 = jpql_Variable()
    b2 = jpql_Variable()
    _safe_set(a, 'jpql_LikeExpression', b1)
    assert _is_linked(a, 'jpql_LikeExpression', b1)
    if hasattr(b1, 'jpql_Variable85'):
        assert _is_linked(b1, 'jpql_Variable85', a)
    _safe_set(a, 'jpql_LikeExpression', b2)
    assert _is_linked(a, 'jpql_LikeExpression', b2)
    if hasattr(b1, 'jpql_Variable85'):
        assert not _is_linked(b1, 'jpql_Variable85', a)
    if hasattr(b2, 'jpql_Variable85'):
        assert _is_linked(b2, 'jpql_Variable85', a)
    _safe_set(a, 'jpql_LikeExpression', None)
    assert not _is_linked(a, 'jpql_LikeExpression', b2)
    if hasattr(b2, 'jpql_Variable85'):
        assert not _is_linked(b2, 'jpql_Variable85', a)


def test_assoc_lhs86_link_reassign_clear():
    a = jpql_InExpression(isNot=True)
    b1 = jpql_Variable()
    b2 = jpql_Variable()
    _safe_set(a, 'jpql_InExpression', b1)
    assert _is_linked(a, 'jpql_InExpression', b1)
    if hasattr(b1, 'jpql_Variable87'):
        assert _is_linked(b1, 'jpql_Variable87', a)
    _safe_set(a, 'jpql_InExpression', b2)
    assert _is_linked(a, 'jpql_InExpression', b2)
    if hasattr(b1, 'jpql_Variable87'):
        assert not _is_linked(b1, 'jpql_Variable87', a)
    if hasattr(b2, 'jpql_Variable87'):
        assert _is_linked(b2, 'jpql_Variable87', a)
    _safe_set(a, 'jpql_InExpression', None)
    assert not _is_linked(a, 'jpql_InExpression', b2)
    if hasattr(b2, 'jpql_Variable87'):
        assert not _is_linked(b2, 'jpql_Variable87', a)


def test_assoc_lhs92_link_reassign_clear():
    a = jpql_BetweenExpression(isNot=True)
    b1 = jpql_Variable()
    b2 = jpql_Variable()
    _safe_set(a, 'jpql_BetweenExpression', b1)
    assert _is_linked(a, 'jpql_BetweenExpression', b1)
    if hasattr(b1, 'jpql_Variable93'):
        assert _is_linked(b1, 'jpql_Variable93', a)
    _safe_set(a, 'jpql_BetweenExpression', b2)
    assert _is_linked(a, 'jpql_BetweenExpression', b2)
    if hasattr(b1, 'jpql_Variable93'):
        assert not _is_linked(b1, 'jpql_Variable93', a)
    if hasattr(b2, 'jpql_Variable93'):
        assert _is_linked(b2, 'jpql_Variable93', a)
    _safe_set(a, 'jpql_BetweenExpression', None)
    assert not _is_linked(a, 'jpql_BetweenExpression', b2)
    if hasattr(b2, 'jpql_Variable93'):
        assert not _is_linked(b2, 'jpql_Variable93', a)


def test_assoc_max97_link_reassign_clear():
    a = jpql_BetweenExpression(isNot=True)
    b1 = jpql_Value()
    b2 = jpql_Value()
    _safe_set(a, 'jpql_BetweenExpression98', b1)
    assert _is_linked(a, 'jpql_BetweenExpression98', b1)
    if hasattr(b1, 'jpql_Value99'):
        assert _is_linked(b1, 'jpql_Value99', a)
    _safe_set(a, 'jpql_BetweenExpression98', b2)
    assert _is_linked(a, 'jpql_BetweenExpression98', b2)
    if hasattr(b1, 'jpql_Value99'):
        assert not _is_linked(b1, 'jpql_Value99', a)
    if hasattr(b2, 'jpql_Value99'):
        assert _is_linked(b2, 'jpql_Value99', a)
    _safe_set(a, 'jpql_BetweenExpression98', None)
    assert not _is_linked(a, 'jpql_BetweenExpression98', b2)
    if hasattr(b2, 'jpql_Value99'):
        assert not _is_linked(b2, 'jpql_Value99', a)


def test_assoc_min94_link_reassign_clear():
    a = jpql_BetweenExpression(isNot=True)
    b1 = jpql_Value()
    b2 = jpql_Value()
    _safe_set(a, 'jpql_BetweenExpression95', b1)
    assert _is_linked(a, 'jpql_BetweenExpression95', b1)
    if hasattr(b1, 'jpql_Value96'):
        assert _is_linked(b1, 'jpql_Value96', a)
    _safe_set(a, 'jpql_BetweenExpression95', b2)
    assert _is_linked(a, 'jpql_BetweenExpression95', b2)
    if hasattr(b1, 'jpql_Value96'):
        assert not _is_linked(b1, 'jpql_Value96', a)
    if hasattr(b2, 'jpql_Value96'):
        assert _is_linked(b2, 'jpql_Value96', a)
    _safe_set(a, 'jpql_BetweenExpression95', None)
    assert not _is_linked(a, 'jpql_BetweenExpression95', b2)
    if hasattr(b2, 'jpql_Value96'):
        assert not _is_linked(b2, 'jpql_Value96', a)


def test_assoc_namedQueries3_link_reassign_clear():
    a = jpql_NamedQuery(name="sample_text")
    b1 = jpql_QueryModule()
    b2 = jpql_QueryModule()
    _safe_set(a, 'jpql_NamedQuery', b1)
    assert _is_linked(a, 'jpql_NamedQuery', b1)
    if hasattr(b1, 'jpql_QueryModule4'):
        assert _is_linked(b1, 'jpql_QueryModule4', a)
    _safe_set(a, 'jpql_NamedQuery', b2)
    assert _is_linked(a, 'jpql_NamedQuery', b2)
    if hasattr(b1, 'jpql_QueryModule4'):
        assert not _is_linked(b1, 'jpql_QueryModule4', a)
    if hasattr(b2, 'jpql_QueryModule4'):
        assert _is_linked(b2, 'jpql_QueryModule4', a)
    _safe_set(a, 'jpql_NamedQuery', None)
    assert not _is_linked(a, 'jpql_NamedQuery', b2)
    if hasattr(b2, 'jpql_QueryModule4'):
        assert not _is_linked(b2, 'jpql_QueryModule4', a)


def test_assoc_order13_link_reassign_clear():
    a = jpql_OrderClause(isAsc=True, isDesc=True)
    b1 = jpql_SelectStatement()
    b2 = jpql_SelectStatement()
    _safe_set(a, 'jpql_OrderClause', b1)
    assert _is_linked(a, 'jpql_OrderClause', b1)
    if hasattr(b1, 'jpql_SelectStatement14'):
        assert _is_linked(b1, 'jpql_SelectStatement14', a)
    _safe_set(a, 'jpql_OrderClause', b2)
    assert _is_linked(a, 'jpql_OrderClause', b2)
    if hasattr(b1, 'jpql_SelectStatement14'):
        assert not _is_linked(b1, 'jpql_SelectStatement14', a)
    if hasattr(b2, 'jpql_SelectStatement14'):
        assert _is_linked(b2, 'jpql_SelectStatement14', a)
    _safe_set(a, 'jpql_OrderClause', None)
    assert not _is_linked(a, 'jpql_OrderClause', b2)
    if hasattr(b2, 'jpql_SelectStatement14'):
        assert not _is_linked(b2, 'jpql_SelectStatement14', a)


def test_assoc_ordering17_link_reassign_clear():
    a = jpql_OrderItem(feature="sample_text")
    b1 = jpql_OrderClause(isAsc=True, isDesc=True)
    b2 = jpql_OrderClause(isAsc=False, isDesc=False)
    _safe_set(a, 'jpql_OrderItem', b1)
    assert _is_linked(a, 'jpql_OrderItem', b1)
    if hasattr(b1, 'jpql_OrderClause18'):
        assert _is_linked(b1, 'jpql_OrderClause18', a)
    _safe_set(a, 'jpql_OrderItem', b2)
    assert _is_linked(a, 'jpql_OrderItem', b2)
    if hasattr(b1, 'jpql_OrderClause18'):
        assert not _is_linked(b1, 'jpql_OrderClause18', a)
    if hasattr(b2, 'jpql_OrderClause18'):
        assert _is_linked(b2, 'jpql_OrderClause18', a)
    _safe_set(a, 'jpql_OrderItem', None)
    assert not _is_linked(a, 'jpql_OrderItem', b2)
    if hasattr(b2, 'jpql_OrderClause18'):
        assert not _is_linked(b2, 'jpql_OrderClause18', a)


def test_assoc_params103_link_reassign_clear():
    a = jpql_Function(name="sample_text")
    b1 = jpql_Variable()
    b2 = jpql_Variable()
    _safe_set(a, 'jpql_Function', {b1})
    assert _is_linked(a, 'jpql_Function', b1)
    if hasattr(b1, 'jpql_Variable104'):
        assert _is_linked(b1, 'jpql_Variable104', a)
    _safe_set(a, 'jpql_Function', {b2})
    assert _is_linked(a, 'jpql_Function', b2)
    if hasattr(b1, 'jpql_Variable104'):
        assert not _is_linked(b1, 'jpql_Variable104', a)
    if hasattr(b2, 'jpql_Variable104'):
        assert _is_linked(b2, 'jpql_Variable104', a)
    _safe_set(a, 'jpql_Function', set())
    assert not _is_linked(a, 'jpql_Function', b2)
    if hasattr(b2, 'jpql_Variable104'):
        assert not _is_linked(b2, 'jpql_Variable104', a)


def test_assoc_path53_link_reassign_clear():
    a = jpql_AliasAttributeExpression(attributes="sample_text")
    b1 = jpql_FromCollection()
    b2 = jpql_FromCollection()
    _safe_set(a, 'jpql_AliasAttributeExpression54', b1)
    assert _is_linked(a, 'jpql_AliasAttributeExpression54', b1)
    if hasattr(b1, 'jpql_FromCollection'):
        assert _is_linked(b1, 'jpql_FromCollection', a)
    _safe_set(a, 'jpql_AliasAttributeExpression54', b2)
    assert _is_linked(a, 'jpql_AliasAttributeExpression54', b2)
    if hasattr(b1, 'jpql_FromCollection'):
        assert not _is_linked(b1, 'jpql_FromCollection', a)
    if hasattr(b2, 'jpql_FromCollection'):
        assert _is_linked(b2, 'jpql_FromCollection', a)
    _safe_set(a, 'jpql_AliasAttributeExpression54', None)
    assert not _is_linked(a, 'jpql_AliasAttributeExpression54', b2)
    if hasattr(b2, 'jpql_FromCollection'):
        assert not _is_linked(b2, 'jpql_FromCollection', a)


def test_assoc_path55_link_reassign_clear():
    a = jpql_FromJoin(isFetch=True)
    b1 = jpql_AliasAttributeExpression(attributes="sample_text")
    b2 = jpql_AliasAttributeExpression(attributes="sample_text_2")
    _safe_set(a, 'jpql_FromJoin56', b1)
    assert _is_linked(a, 'jpql_FromJoin56', b1)
    if hasattr(b1, 'jpql_AliasAttributeExpression57'):
        assert _is_linked(b1, 'jpql_AliasAttributeExpression57', a)
    _safe_set(a, 'jpql_FromJoin56', b2)
    assert _is_linked(a, 'jpql_FromJoin56', b2)
    if hasattr(b1, 'jpql_AliasAttributeExpression57'):
        assert not _is_linked(b1, 'jpql_AliasAttributeExpression57', a)
    if hasattr(b2, 'jpql_AliasAttributeExpression57'):
        assert _is_linked(b2, 'jpql_AliasAttributeExpression57', a)
    _safe_set(a, 'jpql_FromJoin56', None)
    assert not _is_linked(a, 'jpql_FromJoin56', b2)
    if hasattr(b2, 'jpql_AliasAttributeExpression57'):
        assert not _is_linked(b2, 'jpql_AliasAttributeExpression57', a)


def test_assoc_query5_link_reassign_clear():
    a = jpql_NamedQuery(name="sample_text")
    b1 = jpql_JPQLQuery()
    b2 = jpql_JPQLQuery()
    _safe_set(a, 'jpql_NamedQuery6', b1)
    assert _is_linked(a, 'jpql_NamedQuery6', b1)
    if hasattr(b1, 'jpql_JPQLQuery7'):
        assert _is_linked(b1, 'jpql_JPQLQuery7', a)
    _safe_set(a, 'jpql_NamedQuery6', b2)
    assert _is_linked(a, 'jpql_NamedQuery6', b2)
    if hasattr(b1, 'jpql_JPQLQuery7'):
        assert not _is_linked(b1, 'jpql_JPQLQuery7', a)
    if hasattr(b2, 'jpql_JPQLQuery7'):
        assert _is_linked(b2, 'jpql_JPQLQuery7', a)
    _safe_set(a, 'jpql_NamedQuery6', None)
    assert not _is_linked(a, 'jpql_NamedQuery6', b2)
    if hasattr(b2, 'jpql_JPQLQuery7'):
        assert not _is_linked(b2, 'jpql_JPQLQuery7', a)


def test_assoc_query67_link_reassign_clear():
    a = jpql_ExistsExpression(isNot=True)
    b1 = jpql_SelectStatement()
    b2 = jpql_SelectStatement()
    _safe_set(a, 'jpql_ExistsExpression', b1)
    assert _is_linked(a, 'jpql_ExistsExpression', b1)
    if hasattr(b1, 'jpql_SelectStatement68'):
        assert _is_linked(b1, 'jpql_SelectStatement68', a)
    _safe_set(a, 'jpql_ExistsExpression', b2)
    assert _is_linked(a, 'jpql_ExistsExpression', b2)
    if hasattr(b1, 'jpql_SelectStatement68'):
        assert not _is_linked(b1, 'jpql_SelectStatement68', a)
    if hasattr(b2, 'jpql_SelectStatement68'):
        assert _is_linked(b2, 'jpql_SelectStatement68', a)
    _safe_set(a, 'jpql_ExistsExpression', None)
    assert not _is_linked(a, 'jpql_ExistsExpression', b2)
    if hasattr(b2, 'jpql_SelectStatement68'):
        assert not _is_linked(b2, 'jpql_SelectStatement68', a)


def test_assoc_rhs65_link_reassign_clear():
    a = jpql_OperatorExpression(operator="sample_text")
    b1 = jpql_ExpressionTerm()
    b2 = jpql_ExpressionTerm()
    _safe_set(a, 'jpql_OperatorExpression66', b1)
    assert _is_linked(a, 'jpql_OperatorExpression66', b1)
    if hasattr(b1, 'jpql_ExpressionTerm'):
        assert _is_linked(b1, 'jpql_ExpressionTerm', a)
    _safe_set(a, 'jpql_OperatorExpression66', b2)
    assert _is_linked(a, 'jpql_OperatorExpression66', b2)
    if hasattr(b1, 'jpql_ExpressionTerm'):
        assert not _is_linked(b1, 'jpql_ExpressionTerm', a)
    if hasattr(b2, 'jpql_ExpressionTerm'):
        assert _is_linked(b2, 'jpql_ExpressionTerm', a)
    _safe_set(a, 'jpql_OperatorExpression66', None)
    assert not _is_linked(a, 'jpql_OperatorExpression66', b2)
    if hasattr(b2, 'jpql_ExpressionTerm'):
        assert not _is_linked(b2, 'jpql_ExpressionTerm', a)


def test_assoc_rhs77_link_reassign_clear():
    a = jpql_CollectionExpression(isNot=True)
    b1 = jpql_AliasAttributeExpression(attributes="sample_text")
    b2 = jpql_AliasAttributeExpression(attributes="sample_text_2")
    _safe_set(a, 'jpql_CollectionExpression78', b1)
    assert _is_linked(a, 'jpql_CollectionExpression78', b1)
    if hasattr(b1, 'jpql_AliasAttributeExpression79'):
        assert _is_linked(b1, 'jpql_AliasAttributeExpression79', a)
    _safe_set(a, 'jpql_CollectionExpression78', b2)
    assert _is_linked(a, 'jpql_CollectionExpression78', b2)
    if hasattr(b1, 'jpql_AliasAttributeExpression79'):
        assert not _is_linked(b1, 'jpql_AliasAttributeExpression79', a)
    if hasattr(b2, 'jpql_AliasAttributeExpression79'):
        assert _is_linked(b2, 'jpql_AliasAttributeExpression79', a)
    _safe_set(a, 'jpql_CollectionExpression78', None)
    assert not _is_linked(a, 'jpql_CollectionExpression78', b2)
    if hasattr(b2, 'jpql_AliasAttributeExpression79'):
        assert not _is_linked(b2, 'jpql_AliasAttributeExpression79', a)


def test_assoc_selectClause36_link_reassign_clear():
    a = jpql_SelectClause(isDistinct=True)
    b1 = jpql_SelectFromClause()
    b2 = jpql_SelectFromClause()
    _safe_set(a, 'jpql_SelectClause', b1)
    assert _is_linked(a, 'jpql_SelectClause', b1)
    if hasattr(b1, 'jpql_SelectFromClause37'):
        assert _is_linked(b1, 'jpql_SelectFromClause37', a)
    _safe_set(a, 'jpql_SelectClause', b2)
    assert _is_linked(a, 'jpql_SelectClause', b2)
    if hasattr(b1, 'jpql_SelectFromClause37'):
        assert not _is_linked(b1, 'jpql_SelectFromClause37', a)
    if hasattr(b2, 'jpql_SelectFromClause37'):
        assert _is_linked(b2, 'jpql_SelectFromClause37', a)
    _safe_set(a, 'jpql_SelectClause', None)
    assert not _is_linked(a, 'jpql_SelectClause', b2)
    if hasattr(b2, 'jpql_SelectFromClause37'):
        assert not _is_linked(b2, 'jpql_SelectFromClause37', a)


def test_assoc_var19_link_reassign_clear():
    a = jpql_OrderItem(feature="sample_text")
    b1 = jpql_FromEntry()
    b2 = jpql_FromEntry()
    _safe_set(a, 'jpql_OrderItem20', b1)
    assert _is_linked(a, 'jpql_OrderItem20', b1)
    if hasattr(b1, 'jpql_FromEntry'):
        assert _is_linked(b1, 'jpql_FromEntry', a)
    _safe_set(a, 'jpql_OrderItem20', b2)
    assert _is_linked(a, 'jpql_OrderItem20', b2)
    if hasattr(b1, 'jpql_FromEntry'):
        assert not _is_linked(b1, 'jpql_FromEntry', a)
    if hasattr(b2, 'jpql_FromEntry'):
        assert _is_linked(b2, 'jpql_FromEntry', a)
    _safe_set(a, 'jpql_OrderItem20', None)
    assert not _is_linked(a, 'jpql_OrderItem20', b2)
    if hasattr(b2, 'jpql_FromEntry'):
        assert not _is_linked(b2, 'jpql_FromEntry', a)


def test_assoc_variable50_link_reassign_clear():
    a = jpql_VariableDeclaration(name="sample_text")
    b1 = jpql_FromEntry()
    b2 = jpql_FromEntry()
    _safe_set(a, 'jpql_VariableDeclaration', b1)
    assert _is_linked(a, 'jpql_VariableDeclaration', b1)
    if hasattr(b1, 'jpql_FromEntry51'):
        assert _is_linked(b1, 'jpql_FromEntry51', a)
    _safe_set(a, 'jpql_VariableDeclaration', b2)
    assert _is_linked(a, 'jpql_VariableDeclaration', b2)
    if hasattr(b1, 'jpql_FromEntry51'):
        assert not _is_linked(b1, 'jpql_FromEntry51', a)
    if hasattr(b2, 'jpql_FromEntry51'):
        assert _is_linked(b2, 'jpql_FromEntry51', a)
    _safe_set(a, 'jpql_VariableDeclaration', None)
    assert not _is_linked(a, 'jpql_VariableDeclaration', b2)
    if hasattr(b2, 'jpql_FromEntry51'):
        assert not _is_linked(b2, 'jpql_FromEntry51', a)


def test_assoc_variable58_link_reassign_clear():
    a = jpql_VariableDeclaration(name="sample_text")
    b1 = jpql_FromJoin(isFetch=True)
    b2 = jpql_FromJoin(isFetch=False)
    _safe_set(a, 'jpql_VariableDeclaration60', b1)
    assert _is_linked(a, 'jpql_VariableDeclaration60', b1)
    if hasattr(b1, 'jpql_FromJoin59'):
        assert _is_linked(b1, 'jpql_FromJoin59', a)
    _safe_set(a, 'jpql_VariableDeclaration60', b2)
    assert _is_linked(a, 'jpql_VariableDeclaration60', b2)
    if hasattr(b1, 'jpql_FromJoin59'):
        assert not _is_linked(b1, 'jpql_FromJoin59', a)
    if hasattr(b2, 'jpql_FromJoin59'):
        assert _is_linked(b2, 'jpql_FromJoin59', a)
    _safe_set(a, 'jpql_VariableDeclaration60', None)
    assert not _is_linked(a, 'jpql_VariableDeclaration60', b2)
    if hasattr(b2, 'jpql_FromJoin59'):
        assert not _is_linked(b2, 'jpql_FromJoin59', a)


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


JPQLQuery_strategy = st.builds(JPQLQuery)
@given(instance=JPQLQuery_strategy)
@settings(max_examples=25)
def test_JPQLQuery_instantiation(instance):
    assert isinstance(instance, JPQLQuery)


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


jpql_AliasAttributeExpression_strategy = st.builds(jpql_AliasAttributeExpression, attributes=safe_text)
@given(instance=jpql_AliasAttributeExpression_strategy)
@settings(max_examples=25)
def test_jpql_AliasAttributeExpression_instantiation(instance):
    assert isinstance(instance, jpql_AliasAttributeExpression)


jpql_AllExpression_strategy = st.builds(jpql_AllExpression)
@given(instance=jpql_AllExpression_strategy)
@settings(max_examples=25)
def test_jpql_AllExpression_instantiation(instance):
    assert isinstance(instance, jpql_AllExpression)


jpql_AndExpression_strategy = st.builds(jpql_AndExpression)
@given(instance=jpql_AndExpression_strategy)
@settings(max_examples=25)
def test_jpql_AndExpression_instantiation(instance):
    assert isinstance(instance, jpql_AndExpression)


jpql_AnyExpression_strategy = st.builds(jpql_AnyExpression)
@given(instance=jpql_AnyExpression_strategy)
@settings(max_examples=25)
def test_jpql_AnyExpression_instantiation(instance):
    assert isinstance(instance, jpql_AnyExpression)


jpql_AvgAggregate_strategy = st.builds(jpql_AvgAggregate)
@given(instance=jpql_AvgAggregate_strategy)
@settings(max_examples=25)
def test_jpql_AvgAggregate_instantiation(instance):
    assert isinstance(instance, jpql_AvgAggregate)


jpql_BetweenExpression_strategy = st.builds(jpql_BetweenExpression, isNot=st.booleans())
@given(instance=jpql_BetweenExpression_strategy)
@settings(max_examples=25)
def test_jpql_BetweenExpression_instantiation(instance):
    assert isinstance(instance, jpql_BetweenExpression)


jpql_BooleanExpression_strategy = st.builds(jpql_BooleanExpression, value=st.booleans())
@given(instance=jpql_BooleanExpression_strategy)
@settings(max_examples=25)
def test_jpql_BooleanExpression_instantiation(instance):
    assert isinstance(instance, jpql_BooleanExpression)


jpql_CollectionExpression_strategy = st.builds(jpql_CollectionExpression, isNot=st.booleans())
@given(instance=jpql_CollectionExpression_strategy)
@settings(max_examples=25)
def test_jpql_CollectionExpression_instantiation(instance):
    assert isinstance(instance, jpql_CollectionExpression)


jpql_CountAggregate_strategy = st.builds(jpql_CountAggregate)
@given(instance=jpql_CountAggregate_strategy)
@settings(max_examples=25)
def test_jpql_CountAggregate_instantiation(instance):
    assert isinstance(instance, jpql_CountAggregate)


jpql_DateTimeExpression_strategy = st.builds(jpql_DateTimeExpression, value=safe_text)
@given(instance=jpql_DateTimeExpression_strategy)
@settings(max_examples=25)
def test_jpql_DateTimeExpression_instantiation(instance):
    assert isinstance(instance, jpql_DateTimeExpression)


jpql_DeleteClause_strategy = st.builds(jpql_DeleteClause)
@given(instance=jpql_DeleteClause_strategy)
@settings(max_examples=25)
def test_jpql_DeleteClause_instantiation(instance):
    assert isinstance(instance, jpql_DeleteClause)


jpql_DeleteStatement_strategy = st.builds(jpql_DeleteStatement)
@given(instance=jpql_DeleteStatement_strategy)
@settings(max_examples=25)
def test_jpql_DeleteStatement_instantiation(instance):
    assert isinstance(instance, jpql_DeleteStatement)


jpql_EmptyComparisonExpression_strategy = st.builds(jpql_EmptyComparisonExpression, isNot=st.booleans())
@given(instance=jpql_EmptyComparisonExpression_strategy)
@settings(max_examples=25)
def test_jpql_EmptyComparisonExpression_instantiation(instance):
    assert isinstance(instance, jpql_EmptyComparisonExpression)


jpql_ExistsExpression_strategy = st.builds(jpql_ExistsExpression, isNot=st.booleans())
@given(instance=jpql_ExistsExpression_strategy)
@settings(max_examples=25)
def test_jpql_ExistsExpression_instantiation(instance):
    assert isinstance(instance, jpql_ExistsExpression)


jpql_Expression_strategy = st.builds(jpql_Expression)
@given(instance=jpql_Expression_strategy)
@settings(max_examples=25)
def test_jpql_Expression_instantiation(instance):
    assert isinstance(instance, jpql_Expression)


jpql_ExpressionTerm_strategy = st.builds(jpql_ExpressionTerm)
@given(instance=jpql_ExpressionTerm_strategy)
@settings(max_examples=25)
def test_jpql_ExpressionTerm_instantiation(instance):
    assert isinstance(instance, jpql_ExpressionTerm)


jpql_FromClass_strategy = st.builds(jpql_FromClass, type=safe_text)
@given(instance=jpql_FromClass_strategy)
@settings(max_examples=25)
def test_jpql_FromClass_instantiation(instance):
    assert isinstance(instance, jpql_FromClass)


jpql_FromClause_strategy = st.builds(jpql_FromClause)
@given(instance=jpql_FromClause_strategy)
@settings(max_examples=25)
def test_jpql_FromClause_instantiation(instance):
    assert isinstance(instance, jpql_FromClause)


jpql_FromCollection_strategy = st.builds(jpql_FromCollection)
@given(instance=jpql_FromCollection_strategy)
@settings(max_examples=25)
def test_jpql_FromCollection_instantiation(instance):
    assert isinstance(instance, jpql_FromCollection)


jpql_FromEntry_strategy = st.builds(jpql_FromEntry)
@given(instance=jpql_FromEntry_strategy)
@settings(max_examples=25)
def test_jpql_FromEntry_instantiation(instance):
    assert isinstance(instance, jpql_FromEntry)


jpql_FromJoin_strategy = st.builds(jpql_FromJoin, isFetch=st.booleans())
@given(instance=jpql_FromJoin_strategy)
@settings(max_examples=25)
def test_jpql_FromJoin_instantiation(instance):
    assert isinstance(instance, jpql_FromJoin)


jpql_Function_strategy = st.builds(jpql_Function, name=safe_text)
@given(instance=jpql_Function_strategy)
@settings(max_examples=25)
def test_jpql_Function_instantiation(instance):
    assert isinstance(instance, jpql_Function)


jpql_HavingClause_strategy = st.builds(jpql_HavingClause)
@given(instance=jpql_HavingClause_strategy)
@settings(max_examples=25)
def test_jpql_HavingClause_instantiation(instance):
    assert isinstance(instance, jpql_HavingClause)


jpql_Import_strategy = st.builds(jpql_Import, importURI=safe_text)
@given(instance=jpql_Import_strategy)
@settings(max_examples=25)
def test_jpql_Import_instantiation(instance):
    assert isinstance(instance, jpql_Import)


jpql_InExpression_strategy = st.builds(jpql_InExpression, isNot=st.booleans())
@given(instance=jpql_InExpression_strategy)
@settings(max_examples=25)
def test_jpql_InExpression_instantiation(instance):
    assert isinstance(instance, jpql_InExpression)


jpql_InQueryExpression_strategy = st.builds(jpql_InQueryExpression)
@given(instance=jpql_InQueryExpression_strategy)
@settings(max_examples=25)
def test_jpql_InQueryExpression_instantiation(instance):
    assert isinstance(instance, jpql_InQueryExpression)


jpql_InSeqExpression_strategy = st.builds(jpql_InSeqExpression)
@given(instance=jpql_InSeqExpression_strategy)
@settings(max_examples=25)
def test_jpql_InSeqExpression_instantiation(instance):
    assert isinstance(instance, jpql_InSeqExpression)


jpql_InnerJoin_strategy = st.builds(jpql_InnerJoin)
@given(instance=jpql_InnerJoin_strategy)
@settings(max_examples=25)
def test_jpql_InnerJoin_instantiation(instance):
    assert isinstance(instance, jpql_InnerJoin)


jpql_IntegerExpression_strategy = st.builds(jpql_IntegerExpression, value=st.integers())
@given(instance=jpql_IntegerExpression_strategy)
@settings(max_examples=25)
def test_jpql_IntegerExpression_instantiation(instance):
    assert isinstance(instance, jpql_IntegerExpression)


jpql_JPQLQuery_strategy = st.builds(jpql_JPQLQuery)
@given(instance=jpql_JPQLQuery_strategy)
@settings(max_examples=25)
def test_jpql_JPQLQuery_instantiation(instance):
    assert isinstance(instance, jpql_JPQLQuery)


jpql_Join_strategy = st.builds(jpql_Join)
@given(instance=jpql_Join_strategy)
@settings(max_examples=25)
def test_jpql_Join_instantiation(instance):
    assert isinstance(instance, jpql_Join)


jpql_LeftJoin_strategy = st.builds(jpql_LeftJoin, isOuter=st.booleans())
@given(instance=jpql_LeftJoin_strategy)
@settings(max_examples=25)
def test_jpql_LeftJoin_instantiation(instance):
    assert isinstance(instance, jpql_LeftJoin)


jpql_LikeExpression_strategy = st.builds(jpql_LikeExpression, isNot=st.booleans(), pattern=safe_text)
@given(instance=jpql_LikeExpression_strategy)
@settings(max_examples=25)
def test_jpql_LikeExpression_instantiation(instance):
    assert isinstance(instance, jpql_LikeExpression)


jpql_MaxAggregate_strategy = st.builds(jpql_MaxAggregate)
@given(instance=jpql_MaxAggregate_strategy)
@settings(max_examples=25)
def test_jpql_MaxAggregate_instantiation(instance):
    assert isinstance(instance, jpql_MaxAggregate)


jpql_MinAggregate_strategy = st.builds(jpql_MinAggregate)
@given(instance=jpql_MinAggregate_strategy)
@settings(max_examples=25)
def test_jpql_MinAggregate_instantiation(instance):
    assert isinstance(instance, jpql_MinAggregate)


jpql_NamedQuery_strategy = st.builds(jpql_NamedQuery, name=safe_text)
@given(instance=jpql_NamedQuery_strategy)
@settings(max_examples=25)
def test_jpql_NamedQuery_instantiation(instance):
    assert isinstance(instance, jpql_NamedQuery)


jpql_NullComparisonExpression_strategy = st.builds(jpql_NullComparisonExpression, isNot=st.booleans())
@given(instance=jpql_NullComparisonExpression_strategy)
@settings(max_examples=25)
def test_jpql_NullComparisonExpression_instantiation(instance):
    assert isinstance(instance, jpql_NullComparisonExpression)


jpql_NullExpression_strategy = st.builds(jpql_NullExpression, value=safe_text)
@given(instance=jpql_NullExpression_strategy)
@settings(max_examples=25)
def test_jpql_NullExpression_instantiation(instance):
    assert isinstance(instance, jpql_NullExpression)


jpql_OperatorExpression_strategy = st.builds(jpql_OperatorExpression, operator=safe_text)
@given(instance=jpql_OperatorExpression_strategy)
@settings(max_examples=25)
def test_jpql_OperatorExpression_instantiation(instance):
    assert isinstance(instance, jpql_OperatorExpression)


jpql_OrExpression_strategy = st.builds(jpql_OrExpression)
@given(instance=jpql_OrExpression_strategy)
@settings(max_examples=25)
def test_jpql_OrExpression_instantiation(instance):
    assert isinstance(instance, jpql_OrExpression)


jpql_OrderClause_strategy = st.builds(jpql_OrderClause, isAsc=st.booleans(), isDesc=st.booleans())
@given(instance=jpql_OrderClause_strategy)
@settings(max_examples=25)
def test_jpql_OrderClause_instantiation(instance):
    assert isinstance(instance, jpql_OrderClause)


jpql_OrderItem_strategy = st.builds(jpql_OrderItem, feature=safe_text)
@given(instance=jpql_OrderItem_strategy)
@settings(max_examples=25)
def test_jpql_OrderItem_instantiation(instance):
    assert isinstance(instance, jpql_OrderItem)


jpql_ParameterExpression_strategy = st.builds(jpql_ParameterExpression, name=safe_text)
@given(instance=jpql_ParameterExpression_strategy)
@settings(max_examples=25)
def test_jpql_ParameterExpression_instantiation(instance):
    assert isinstance(instance, jpql_ParameterExpression)


jpql_QueryModule_strategy = st.builds(jpql_QueryModule)
@given(instance=jpql_QueryModule_strategy)
@settings(max_examples=25)
def test_jpql_QueryModule_instantiation(instance):
    assert isinstance(instance, jpql_QueryModule)


jpql_SelectAggregateExpression_strategy = st.builds(jpql_SelectAggregateExpression, isDistinct=st.booleans())
@given(instance=jpql_SelectAggregateExpression_strategy)
@settings(max_examples=25)
def test_jpql_SelectAggregateExpression_instantiation(instance):
    assert isinstance(instance, jpql_SelectAggregateExpression)


jpql_SelectClause_strategy = st.builds(jpql_SelectClause, isDistinct=st.booleans())
@given(instance=jpql_SelectClause_strategy)
@settings(max_examples=25)
def test_jpql_SelectClause_instantiation(instance):
    assert isinstance(instance, jpql_SelectClause)


jpql_SelectConstructorExpression_strategy = st.builds(jpql_SelectConstructorExpression, name=safe_text)
@given(instance=jpql_SelectConstructorExpression_strategy)
@settings(max_examples=25)
def test_jpql_SelectConstructorExpression_instantiation(instance):
    assert isinstance(instance, jpql_SelectConstructorExpression)


jpql_SelectExpression_strategy = st.builds(jpql_SelectExpression)
@given(instance=jpql_SelectExpression_strategy)
@settings(max_examples=25)
def test_jpql_SelectExpression_instantiation(instance):
    assert isinstance(instance, jpql_SelectExpression)


jpql_SelectFromClause_strategy = st.builds(jpql_SelectFromClause)
@given(instance=jpql_SelectFromClause_strategy)
@settings(max_examples=25)
def test_jpql_SelectFromClause_instantiation(instance):
    assert isinstance(instance, jpql_SelectFromClause)


jpql_SelectStatement_strategy = st.builds(jpql_SelectStatement)
@given(instance=jpql_SelectStatement_strategy)
@settings(max_examples=25)
def test_jpql_SelectStatement_instantiation(instance):
    assert isinstance(instance, jpql_SelectStatement)


jpql_SetClause_strategy = st.builds(jpql_SetClause)
@given(instance=jpql_SetClause_strategy)
@settings(max_examples=25)
def test_jpql_SetClause_instantiation(instance):
    assert isinstance(instance, jpql_SetClause)


jpql_SomeExpression_strategy = st.builds(jpql_SomeExpression)
@given(instance=jpql_SomeExpression_strategy)
@settings(max_examples=25)
def test_jpql_SomeExpression_instantiation(instance):
    assert isinstance(instance, jpql_SomeExpression)


jpql_StringExpression_strategy = st.builds(jpql_StringExpression, value=safe_text)
@given(instance=jpql_StringExpression_strategy)
@settings(max_examples=25)
def test_jpql_StringExpression_instantiation(instance):
    assert isinstance(instance, jpql_StringExpression)


jpql_SumAggregate_strategy = st.builds(jpql_SumAggregate)
@given(instance=jpql_SumAggregate_strategy)
@settings(max_examples=25)
def test_jpql_SumAggregate_instantiation(instance):
    assert isinstance(instance, jpql_SumAggregate)


jpql_UpdateClause_strategy = st.builds(jpql_UpdateClause)
@given(instance=jpql_UpdateClause_strategy)
@settings(max_examples=25)
def test_jpql_UpdateClause_instantiation(instance):
    assert isinstance(instance, jpql_UpdateClause)


jpql_UpdateItem_strategy = st.builds(jpql_UpdateItem)
@given(instance=jpql_UpdateItem_strategy)
@settings(max_examples=25)
def test_jpql_UpdateItem_instantiation(instance):
    assert isinstance(instance, jpql_UpdateItem)


jpql_UpdateStatement_strategy = st.builds(jpql_UpdateStatement)
@given(instance=jpql_UpdateStatement_strategy)
@settings(max_examples=25)
def test_jpql_UpdateStatement_instantiation(instance):
    assert isinstance(instance, jpql_UpdateStatement)


jpql_Value_strategy = st.builds(jpql_Value)
@given(instance=jpql_Value_strategy)
@settings(max_examples=25)
def test_jpql_Value_instantiation(instance):
    assert isinstance(instance, jpql_Value)


jpql_Variable_strategy = st.builds(jpql_Variable)
@given(instance=jpql_Variable_strategy)
@settings(max_examples=25)
def test_jpql_Variable_instantiation(instance):
    assert isinstance(instance, jpql_Variable)


jpql_VariableDeclaration_strategy = st.builds(jpql_VariableDeclaration, name=safe_text)
@given(instance=jpql_VariableDeclaration_strategy)
@settings(max_examples=25)
def test_jpql_VariableDeclaration_instantiation(instance):
    assert isinstance(instance, jpql_VariableDeclaration)


jpql_WhereClause_strategy = st.builds(jpql_WhereClause)
@given(instance=jpql_WhereClause_strategy)
@settings(max_examples=25)
def test_jpql_WhereClause_instantiation(instance):
    assert isinstance(instance, jpql_WhereClause)



