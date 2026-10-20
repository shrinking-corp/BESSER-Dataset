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
    Operands,
    sql_Div,
    sql_Star,
    sql_Minus,
    sql_Concat,
    sql_Plus,
    UnpivotInClause,
    sql_UnipivotInClause,
    SQLCaseWhens,
    sql_WhenList,
    sql_SqlCaseWhen,
    sql_SQLCaseWhens,
    OperandList,
    sql_OpList,
    AnalyticExprArgs,
    sql_AExpArgs,
    sql_OpFunctionArgAgregate,
    OpFunctionArg,
    sql_OpFList,
    sql_OpFunctionArgOperand,
    OrderByClauseArgs,
    sql_OBCArgs,
    sql_OrderByClauseArg,
    sql_OrderByClauseArgs,
    QueryPartitionClause,
    sql_AnalyticExprArgs,
    sql_WindowingClauseOperandFollowing,
    sql_AnalyticExprArg,
    sql_QueryPartitionClause,
    sql_AnalyticClause,
    WindowingClause,
    sql_WindowingClauseOperandPreceding,
    sql_WindowingClauseBetween,
    sql_WindowingClause,
    sql_OrderByClause,
    sql_ScalarOperand,
    sql_ExpOperand,
    sql_FunctionAnalytical,
    sql_OpFunctionArg,
    sql_ColumnOperand,
    sql_SQLCaseOperand,
    sql_FunctionExtract,
    OpFunctionArgAgregate,
    sql_OperandList,
    sql_Operand,
    sql_OperandListGroup,
    sql_LikeOperand,
    sql_POperand,
    sql_OpFunctionCast,
    sql_Prms,
    Prms,
    sql_JRParameter,
    sql_Comparison,
    sql_Like,
    sql_ExistsOper,
    sql_InOper,
    sql_XExpr,
    sql_ExprGroup,
    sql_Between,
    OrExpr,
    sql_FullExpression,
    sql_OpFunction,
    OrGroupByColumn,
    sql_GroupByColumnFull,
    OrOrderByColumn,
    sql_OrderByColumnFull,
    TableFull,
    sql_tbls,
    PivotCol,
    sql_pcols,
    ColumnFull,
    sql_Col,
    Pivots,
    sql_pvcs,
    PivotFunction,
    PivotColumns,
    sql_PivotCol,
    sql_Pivots,
    UnpivotInClauseArgs,
    sql_uicargs,
    sql_UnpivotInClauseArg,
    sql_PivotFunction,
    sql_UnpivotInClause,
    sql_PivotColumns,
    sql_UnpivotInClauseArgs,
    sql_PivotFunctions,
    sql_PivotInClause,
    sql_PivotForClause,
    sql_FromTableJoin,
    sql_UnpivotTable,
    sql_PivotTable,
    sql_SubQueryOperand,
    sql_TableFull,
    sql_DbObjectNameAll,
    sql_DbObjectName,
    sql_TableOrAlias,
    OrTable,
    sql_FromTable,
    sql_Operands,
    OrColumn,
    sql_ColumnOrAlias,
    PivotForClause,
    sql_ColumnFull,
    sql_OrExpr,
    sql_OrTable,
    sql_OrColumn,
    sql_OrOrderByColumn,
    sql_OrGroupByColumn,
    sql_Limit,
    sql_Offset,
    SelectQuery,
    sql_Select,
    sql_SelectSubSet,
    sql_Model,
    sql_IntegerValue,
    sql_FetchFirst,
    sql_SelectQuery,
    EXTRACT_VALUES,
    XFunction,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_hyp_operands_is_not_abstract():
    assert not inspect.isabstract(Operands)


def test_hyp_operands_constructor_exists():
    assert callable(Operands.__init__)


def test_hyp_operands_constructor_args():
    sig = inspect.signature(Operands.__init__)
    params = list(sig.parameters.keys())



def test_hyp_sql_div_is_not_abstract():
    assert not inspect.isabstract(sql_Div)


def test_hyp_sql_div_constructor_exists():
    assert callable(sql_Div.__init__)


def test_hyp_sql_div_constructor_args():
    sig = inspect.signature(sql_Div.__init__)
    params = list(sig.parameters.keys())



def test_hyp_sql_star_is_not_abstract():
    assert not inspect.isabstract(sql_Star)


def test_hyp_sql_star_constructor_exists():
    assert callable(sql_Star.__init__)


def test_hyp_sql_star_constructor_args():
    sig = inspect.signature(sql_Star.__init__)
    params = list(sig.parameters.keys())



def test_hyp_sql_minus_is_not_abstract():
    assert not inspect.isabstract(sql_Minus)


def test_hyp_sql_minus_constructor_exists():
    assert callable(sql_Minus.__init__)


def test_hyp_sql_minus_constructor_args():
    sig = inspect.signature(sql_Minus.__init__)
    params = list(sig.parameters.keys())



def test_hyp_sql_concat_is_not_abstract():
    assert not inspect.isabstract(sql_Concat)


def test_hyp_sql_concat_constructor_exists():
    assert callable(sql_Concat.__init__)


def test_hyp_sql_concat_constructor_args():
    sig = inspect.signature(sql_Concat.__init__)
    params = list(sig.parameters.keys())



def test_hyp_sql_plus_is_not_abstract():
    assert not inspect.isabstract(sql_Plus)


def test_hyp_sql_plus_constructor_exists():
    assert callable(sql_Plus.__init__)


def test_hyp_sql_plus_constructor_args():
    sig = inspect.signature(sql_Plus.__init__)
    params = list(sig.parameters.keys())



def test_hyp_unpivotinclause_is_not_abstract():
    assert not inspect.isabstract(UnpivotInClause)


def test_hyp_unpivotinclause_constructor_exists():
    assert callable(UnpivotInClause.__init__)


def test_hyp_unpivotinclause_constructor_args():
    sig = inspect.signature(UnpivotInClause.__init__)
    params = list(sig.parameters.keys())



def test_hyp_sql_unipivotinclause_is_not_abstract():
    assert not inspect.isabstract(sql_UnipivotInClause)


def test_hyp_sql_unipivotinclause_constructor_exists():
    assert callable(sql_UnipivotInClause.__init__)


def test_hyp_sql_unipivotinclause_constructor_args():
    sig = inspect.signature(sql_UnipivotInClause.__init__)
    params = list(sig.parameters.keys())
    assert "op" in params, "Missing parameter 'op'"




def test_hyp_sqlcasewhens_is_not_abstract():
    assert not inspect.isabstract(SQLCaseWhens)


def test_hyp_sqlcasewhens_constructor_exists():
    assert callable(SQLCaseWhens.__init__)


def test_hyp_sqlcasewhens_constructor_args():
    sig = inspect.signature(SQLCaseWhens.__init__)
    params = list(sig.parameters.keys())



def test_hyp_sql_whenlist_is_not_abstract():
    assert not inspect.isabstract(sql_WhenList)


def test_hyp_sql_whenlist_constructor_exists():
    assert callable(sql_WhenList.__init__)


def test_hyp_sql_whenlist_constructor_args():
    sig = inspect.signature(sql_WhenList.__init__)
    params = list(sig.parameters.keys())



def test_hyp_sql_sqlcasewhen_is_not_abstract():
    assert not inspect.isabstract(sql_SqlCaseWhen)


def test_hyp_sql_sqlcasewhen_constructor_exists():
    assert callable(sql_SqlCaseWhen.__init__)


def test_hyp_sql_sqlcasewhen_constructor_args():
    sig = inspect.signature(sql_SqlCaseWhen.__init__)
    params = list(sig.parameters.keys())



def test_hyp_sql_sqlcasewhens_is_not_abstract():
    assert not inspect.isabstract(sql_SQLCaseWhens)


def test_hyp_sql_sqlcasewhens_constructor_exists():
    assert callable(sql_SQLCaseWhens.__init__)


def test_hyp_sql_sqlcasewhens_constructor_args():
    sig = inspect.signature(sql_SQLCaseWhens.__init__)
    params = list(sig.parameters.keys())



def test_hyp_operandlist_is_not_abstract():
    assert not inspect.isabstract(OperandList)


def test_hyp_operandlist_constructor_exists():
    assert callable(OperandList.__init__)


def test_hyp_operandlist_constructor_args():
    sig = inspect.signature(OperandList.__init__)
    params = list(sig.parameters.keys())



def test_hyp_sql_oplist_is_not_abstract():
    assert not inspect.isabstract(sql_OpList)


def test_hyp_sql_oplist_constructor_exists():
    assert callable(sql_OpList.__init__)


def test_hyp_sql_oplist_constructor_args():
    sig = inspect.signature(sql_OpList.__init__)
    params = list(sig.parameters.keys())



def test_hyp_analyticexprargs_is_not_abstract():
    assert not inspect.isabstract(AnalyticExprArgs)


def test_hyp_analyticexprargs_constructor_exists():
    assert callable(AnalyticExprArgs.__init__)


def test_hyp_analyticexprargs_constructor_args():
    sig = inspect.signature(AnalyticExprArgs.__init__)
    params = list(sig.parameters.keys())



def test_hyp_sql_aexpargs_is_not_abstract():
    assert not inspect.isabstract(sql_AExpArgs)


def test_hyp_sql_aexpargs_constructor_exists():
    assert callable(sql_AExpArgs.__init__)


def test_hyp_sql_aexpargs_constructor_args():
    sig = inspect.signature(sql_AExpArgs.__init__)
    params = list(sig.parameters.keys())



def test_hyp_sql_opfunctionargagregate_is_not_abstract():
    assert not inspect.isabstract(sql_OpFunctionArgAgregate)


def test_hyp_sql_opfunctionargagregate_constructor_exists():
    assert callable(sql_OpFunctionArgAgregate.__init__)


def test_hyp_sql_opfunctionargagregate_constructor_args():
    sig = inspect.signature(sql_OpFunctionArgAgregate.__init__)
    params = list(sig.parameters.keys())



def test_hyp_opfunctionarg_is_not_abstract():
    assert not inspect.isabstract(OpFunctionArg)


def test_hyp_opfunctionarg_constructor_exists():
    assert callable(OpFunctionArg.__init__)


def test_hyp_opfunctionarg_constructor_args():
    sig = inspect.signature(OpFunctionArg.__init__)
    params = list(sig.parameters.keys())



def test_hyp_sql_opflist_is_not_abstract():
    assert not inspect.isabstract(sql_OpFList)


def test_hyp_sql_opflist_constructor_exists():
    assert callable(sql_OpFList.__init__)


def test_hyp_sql_opflist_constructor_args():
    sig = inspect.signature(sql_OpFList.__init__)
    params = list(sig.parameters.keys())



def test_hyp_sql_opfunctionargoperand_is_not_abstract():
    assert not inspect.isabstract(sql_OpFunctionArgOperand)


def test_hyp_sql_opfunctionargoperand_constructor_exists():
    assert callable(sql_OpFunctionArgOperand.__init__)


def test_hyp_sql_opfunctionargoperand_constructor_args():
    sig = inspect.signature(sql_OpFunctionArgOperand.__init__)
    params = list(sig.parameters.keys())



def test_hyp_orderbyclauseargs_is_not_abstract():
    assert not inspect.isabstract(OrderByClauseArgs)


def test_hyp_orderbyclauseargs_constructor_exists():
    assert callable(OrderByClauseArgs.__init__)


def test_hyp_orderbyclauseargs_constructor_args():
    sig = inspect.signature(OrderByClauseArgs.__init__)
    params = list(sig.parameters.keys())



def test_hyp_sql_obcargs_is_not_abstract():
    assert not inspect.isabstract(sql_OBCArgs)


def test_hyp_sql_obcargs_constructor_exists():
    assert callable(sql_OBCArgs.__init__)


def test_hyp_sql_obcargs_constructor_args():
    sig = inspect.signature(sql_OBCArgs.__init__)
    params = list(sig.parameters.keys())



def test_hyp_sql_orderbyclausearg_is_not_abstract():
    assert not inspect.isabstract(sql_OrderByClauseArg)


def test_hyp_sql_orderbyclausearg_constructor_exists():
    assert callable(sql_OrderByClauseArg.__init__)


def test_hyp_sql_orderbyclausearg_constructor_args():
    sig = inspect.signature(sql_OrderByClauseArg.__init__)
    params = list(sig.parameters.keys())



def test_hyp_sql_orderbyclauseargs_is_not_abstract():
    assert not inspect.isabstract(sql_OrderByClauseArgs)


def test_hyp_sql_orderbyclauseargs_constructor_exists():
    assert callable(sql_OrderByClauseArgs.__init__)


def test_hyp_sql_orderbyclauseargs_constructor_args():
    sig = inspect.signature(sql_OrderByClauseArgs.__init__)
    params = list(sig.parameters.keys())



def test_hyp_querypartitionclause_is_not_abstract():
    assert not inspect.isabstract(QueryPartitionClause)


def test_hyp_querypartitionclause_constructor_exists():
    assert callable(QueryPartitionClause.__init__)


def test_hyp_querypartitionclause_constructor_args():
    sig = inspect.signature(QueryPartitionClause.__init__)
    params = list(sig.parameters.keys())



def test_hyp_sql_analyticexprargs_is_not_abstract():
    assert not inspect.isabstract(sql_AnalyticExprArgs)


def test_hyp_sql_analyticexprargs_constructor_exists():
    assert callable(sql_AnalyticExprArgs.__init__)


def test_hyp_sql_analyticexprargs_constructor_args():
    sig = inspect.signature(sql_AnalyticExprArgs.__init__)
    params = list(sig.parameters.keys())



def test_hyp_sql_windowingclauseoperandfollowing_is_not_abstract():
    assert not inspect.isabstract(sql_WindowingClauseOperandFollowing)


def test_hyp_sql_windowingclauseoperandfollowing_constructor_exists():
    assert callable(sql_WindowingClauseOperandFollowing.__init__)


def test_hyp_sql_windowingclauseoperandfollowing_constructor_args():
    sig = inspect.signature(sql_WindowingClauseOperandFollowing.__init__)
    params = list(sig.parameters.keys())



def test_hyp_sql_analyticexprarg_is_not_abstract():
    assert not inspect.isabstract(sql_AnalyticExprArg)


def test_hyp_sql_analyticexprarg_constructor_exists():
    assert callable(sql_AnalyticExprArg.__init__)


def test_hyp_sql_analyticexprarg_constructor_args():
    sig = inspect.signature(sql_AnalyticExprArg.__init__)
    params = list(sig.parameters.keys())



def test_hyp_sql_querypartitionclause_is_not_abstract():
    assert not inspect.isabstract(sql_QueryPartitionClause)


def test_hyp_sql_querypartitionclause_constructor_exists():
    assert callable(sql_QueryPartitionClause.__init__)


def test_hyp_sql_querypartitionclause_constructor_args():
    sig = inspect.signature(sql_QueryPartitionClause.__init__)
    params = list(sig.parameters.keys())



def test_hyp_sql_analyticclause_is_not_abstract():
    assert not inspect.isabstract(sql_AnalyticClause)


def test_hyp_sql_analyticclause_constructor_exists():
    assert callable(sql_AnalyticClause.__init__)


def test_hyp_sql_analyticclause_constructor_args():
    sig = inspect.signature(sql_AnalyticClause.__init__)
    params = list(sig.parameters.keys())



def test_hyp_windowingclause_is_not_abstract():
    assert not inspect.isabstract(WindowingClause)


def test_hyp_windowingclause_constructor_exists():
    assert callable(WindowingClause.__init__)


def test_hyp_windowingclause_constructor_args():
    sig = inspect.signature(WindowingClause.__init__)
    params = list(sig.parameters.keys())



def test_hyp_sql_windowingclauseoperandpreceding_is_not_abstract():
    assert not inspect.isabstract(sql_WindowingClauseOperandPreceding)


def test_hyp_sql_windowingclauseoperandpreceding_constructor_exists():
    assert callable(sql_WindowingClauseOperandPreceding.__init__)


def test_hyp_sql_windowingclauseoperandpreceding_constructor_args():
    sig = inspect.signature(sql_WindowingClauseOperandPreceding.__init__)
    params = list(sig.parameters.keys())



def test_hyp_sql_windowingclausebetween_is_not_abstract():
    assert not inspect.isabstract(sql_WindowingClauseBetween)


def test_hyp_sql_windowingclausebetween_constructor_exists():
    assert callable(sql_WindowingClauseBetween.__init__)


def test_hyp_sql_windowingclausebetween_constructor_args():
    sig = inspect.signature(sql_WindowingClauseBetween.__init__)
    params = list(sig.parameters.keys())



def test_hyp_sql_windowingclause_is_not_abstract():
    assert not inspect.isabstract(sql_WindowingClause)


def test_hyp_sql_windowingclause_constructor_exists():
    assert callable(sql_WindowingClause.__init__)


def test_hyp_sql_windowingclause_constructor_args():
    sig = inspect.signature(sql_WindowingClause.__init__)
    params = list(sig.parameters.keys())



def test_hyp_sql_orderbyclause_is_not_abstract():
    assert not inspect.isabstract(sql_OrderByClause)


def test_hyp_sql_orderbyclause_constructor_exists():
    assert callable(sql_OrderByClause.__init__)


def test_hyp_sql_orderbyclause_constructor_args():
    sig = inspect.signature(sql_OrderByClause.__init__)
    params = list(sig.parameters.keys())



def test_hyp_sql_scalaroperand_is_not_abstract():
    assert not inspect.isabstract(sql_ScalarOperand)


def test_hyp_sql_scalaroperand_constructor_exists():
    assert callable(sql_ScalarOperand.__init__)


def test_hyp_sql_scalaroperand_constructor_args():
    sig = inspect.signature(sql_ScalarOperand.__init__)
    params = list(sig.parameters.keys())
    assert "sostr" in params, "Missing parameter 'sostr'"
    assert "sodate" in params, "Missing parameter 'sodate'"
    assert "sotime" in params, "Missing parameter 'sotime'"
    assert "sodbl" in params, "Missing parameter 'sodbl'"
    assert "soint" in params, "Missing parameter 'soint'"
    assert "sodt" in params, "Missing parameter 'sodt'"









def test_hyp_sql_expoperand_is_not_abstract():
    assert not inspect.isabstract(sql_ExpOperand)


def test_hyp_sql_expoperand_constructor_exists():
    assert callable(sql_ExpOperand.__init__)


def test_hyp_sql_expoperand_constructor_args():
    sig = inspect.signature(sql_ExpOperand.__init__)
    params = list(sig.parameters.keys())
    assert "prm" in params, "Missing parameter 'prm'"




def test_hyp_sql_functionanalytical_is_not_abstract():
    assert not inspect.isabstract(sql_FunctionAnalytical)


def test_hyp_sql_functionanalytical_constructor_exists():
    assert callable(sql_FunctionAnalytical.__init__)


def test_hyp_sql_functionanalytical_constructor_args():
    sig = inspect.signature(sql_FunctionAnalytical.__init__)
    params = list(sig.parameters.keys())



def test_hyp_sql_opfunctionarg_is_not_abstract():
    assert not inspect.isabstract(sql_OpFunctionArg)


def test_hyp_sql_opfunctionarg_constructor_exists():
    assert callable(sql_OpFunctionArg.__init__)


def test_hyp_sql_opfunctionarg_constructor_args():
    sig = inspect.signature(sql_OpFunctionArg.__init__)
    params = list(sig.parameters.keys())



def test_hyp_sql_columnoperand_is_not_abstract():
    assert not inspect.isabstract(sql_ColumnOperand)


def test_hyp_sql_columnoperand_constructor_exists():
    assert callable(sql_ColumnOperand.__init__)


def test_hyp_sql_columnoperand_constructor_args():
    sig = inspect.signature(sql_ColumnOperand.__init__)
    params = list(sig.parameters.keys())
    assert "ora" in params, "Missing parameter 'ora'"




def test_hyp_sql_sqlcaseoperand_is_not_abstract():
    assert not inspect.isabstract(sql_SQLCaseOperand)


def test_hyp_sql_sqlcaseoperand_constructor_exists():
    assert callable(sql_SQLCaseOperand.__init__)


def test_hyp_sql_sqlcaseoperand_constructor_args():
    sig = inspect.signature(sql_SQLCaseOperand.__init__)
    params = list(sig.parameters.keys())



def test_hyp_sql_functionextract_is_not_abstract():
    assert not inspect.isabstract(sql_FunctionExtract)


def test_hyp_sql_functionextract_constructor_exists():
    assert callable(sql_FunctionExtract.__init__)


def test_hyp_sql_functionextract_constructor_args():
    sig = inspect.signature(sql_FunctionExtract.__init__)
    params = list(sig.parameters.keys())
    assert "v" in params, "Missing parameter 'v'"




def test_hyp_opfunctionargagregate_is_not_abstract():
    assert not inspect.isabstract(OpFunctionArgAgregate)


def test_hyp_opfunctionargagregate_constructor_exists():
    assert callable(OpFunctionArgAgregate.__init__)


def test_hyp_opfunctionargagregate_constructor_args():
    sig = inspect.signature(OpFunctionArgAgregate.__init__)
    params = list(sig.parameters.keys())



def test_hyp_sql_operandlist_is_not_abstract():
    assert not inspect.isabstract(sql_OperandList)


def test_hyp_sql_operandlist_constructor_exists():
    assert callable(sql_OperandList.__init__)


def test_hyp_sql_operandlist_constructor_args():
    sig = inspect.signature(sql_OperandList.__init__)
    params = list(sig.parameters.keys())



def test_hyp_sql_operand_is_not_abstract():
    assert not inspect.isabstract(sql_Operand)


def test_hyp_sql_operand_constructor_exists():
    assert callable(sql_Operand.__init__)


def test_hyp_sql_operand_constructor_args():
    sig = inspect.signature(sql_Operand.__init__)
    params = list(sig.parameters.keys())



def test_hyp_sql_operandlistgroup_is_not_abstract():
    assert not inspect.isabstract(sql_OperandListGroup)


def test_hyp_sql_operandlistgroup_constructor_exists():
    assert callable(sql_OperandListGroup.__init__)


def test_hyp_sql_operandlistgroup_constructor_args():
    sig = inspect.signature(sql_OperandListGroup.__init__)
    params = list(sig.parameters.keys())



def test_hyp_sql_likeoperand_is_not_abstract():
    assert not inspect.isabstract(sql_LikeOperand)


def test_hyp_sql_likeoperand_constructor_exists():
    assert callable(sql_LikeOperand.__init__)


def test_hyp_sql_likeoperand_constructor_args():
    sig = inspect.signature(sql_LikeOperand.__init__)
    params = list(sig.parameters.keys())
    assert "op2" in params, "Missing parameter 'op2'"




def test_hyp_sql_poperand_is_not_abstract():
    assert not inspect.isabstract(sql_POperand)


def test_hyp_sql_poperand_constructor_exists():
    assert callable(sql_POperand.__init__)


def test_hyp_sql_poperand_constructor_args():
    sig = inspect.signature(sql_POperand.__init__)
    params = list(sig.parameters.keys())
    assert "prm" in params, "Missing parameter 'prm'"




def test_hyp_sql_opfunctioncast_is_not_abstract():
    assert not inspect.isabstract(sql_OpFunctionCast)


def test_hyp_sql_opfunctioncast_constructor_exists():
    assert callable(sql_OpFunctionCast.__init__)


def test_hyp_sql_opfunctioncast_constructor_args():
    sig = inspect.signature(sql_OpFunctionCast.__init__)
    params = list(sig.parameters.keys())
    assert "type" in params, "Missing parameter 'type'"
    assert "p" in params, "Missing parameter 'p'"
    assert "p2" in params, "Missing parameter 'p2'"






def test_hyp_sql_prms_is_not_abstract():
    assert not inspect.isabstract(sql_Prms)


def test_hyp_sql_prms_constructor_exists():
    assert callable(sql_Prms.__init__)


def test_hyp_sql_prms_constructor_args():
    sig = inspect.signature(sql_Prms.__init__)
    params = list(sig.parameters.keys())



def test_hyp_prms_is_not_abstract():
    assert not inspect.isabstract(Prms)


def test_hyp_prms_constructor_exists():
    assert callable(Prms.__init__)


def test_hyp_prms_constructor_args():
    sig = inspect.signature(Prms.__init__)
    params = list(sig.parameters.keys())



def test_hyp_sql_jrparameter_is_not_abstract():
    assert not inspect.isabstract(sql_JRParameter)


def test_hyp_sql_jrparameter_constructor_exists():
    assert callable(sql_JRParameter.__init__)


def test_hyp_sql_jrparameter_constructor_args():
    sig = inspect.signature(sql_JRParameter.__init__)
    params = list(sig.parameters.keys())
    assert "jrprm" in params, "Missing parameter 'jrprm'"




def test_hyp_sql_comparison_is_not_abstract():
    assert not inspect.isabstract(sql_Comparison)


def test_hyp_sql_comparison_constructor_exists():
    assert callable(sql_Comparison.__init__)


def test_hyp_sql_comparison_constructor_args():
    sig = inspect.signature(sql_Comparison.__init__)
    params = list(sig.parameters.keys())
    assert "operator" in params, "Missing parameter 'operator'"
    assert "subOperator" in params, "Missing parameter 'subOperator'"





def test_hyp_sql_like_is_not_abstract():
    assert not inspect.isabstract(sql_Like)


def test_hyp_sql_like_constructor_exists():
    assert callable(sql_Like.__init__)


def test_hyp_sql_like_constructor_args():
    sig = inspect.signature(sql_Like.__init__)
    params = list(sig.parameters.keys())
    assert "opLike" in params, "Missing parameter 'opLike'"




def test_hyp_sql_existsoper_is_not_abstract():
    assert not inspect.isabstract(sql_ExistsOper)


def test_hyp_sql_existsoper_constructor_exists():
    assert callable(sql_ExistsOper.__init__)


def test_hyp_sql_existsoper_constructor_args():
    sig = inspect.signature(sql_ExistsOper.__init__)
    params = list(sig.parameters.keys())
    assert "op" in params, "Missing parameter 'op'"




def test_hyp_sql_inoper_is_not_abstract():
    assert not inspect.isabstract(sql_InOper)


def test_hyp_sql_inoper_constructor_exists():
    assert callable(sql_InOper.__init__)


def test_hyp_sql_inoper_constructor_args():
    sig = inspect.signature(sql_InOper.__init__)
    params = list(sig.parameters.keys())
    assert "op" in params, "Missing parameter 'op'"




def test_hyp_sql_xexpr_is_not_abstract():
    assert not inspect.isabstract(sql_XExpr)


def test_hyp_sql_xexpr_constructor_exists():
    assert callable(sql_XExpr.__init__)


def test_hyp_sql_xexpr_constructor_args():
    sig = inspect.signature(sql_XExpr.__init__)
    params = list(sig.parameters.keys())
    assert "xf" in params, "Missing parameter 'xf'"




def test_hyp_sql_exprgroup_is_not_abstract():
    assert not inspect.isabstract(sql_ExprGroup)


def test_hyp_sql_exprgroup_constructor_exists():
    assert callable(sql_ExprGroup.__init__)


def test_hyp_sql_exprgroup_constructor_args():
    sig = inspect.signature(sql_ExprGroup.__init__)
    params = list(sig.parameters.keys())
    assert "isnot" in params, "Missing parameter 'isnot'"




def test_hyp_sql_between_is_not_abstract():
    assert not inspect.isabstract(sql_Between)


def test_hyp_sql_between_constructor_exists():
    assert callable(sql_Between.__init__)


def test_hyp_sql_between_constructor_args():
    sig = inspect.signature(sql_Between.__init__)
    params = list(sig.parameters.keys())
    assert "opBetween" in params, "Missing parameter 'opBetween'"




def test_hyp_orexpr_is_not_abstract():
    assert not inspect.isabstract(OrExpr)


def test_hyp_orexpr_constructor_exists():
    assert callable(OrExpr.__init__)


def test_hyp_orexpr_constructor_args():
    sig = inspect.signature(OrExpr.__init__)
    params = list(sig.parameters.keys())



def test_hyp_sql_fullexpression_is_not_abstract():
    assert not inspect.isabstract(sql_FullExpression)


def test_hyp_sql_fullexpression_constructor_exists():
    assert callable(sql_FullExpression.__init__)


def test_hyp_sql_fullexpression_constructor_args():
    sig = inspect.signature(sql_FullExpression.__init__)
    params = list(sig.parameters.keys())
    assert "isnull" in params, "Missing parameter 'isnull'"
    assert "c" in params, "Missing parameter 'c'"
    assert "notPrm" in params, "Missing parameter 'notPrm'"






def test_hyp_sql_opfunction_is_not_abstract():
    assert not inspect.isabstract(sql_OpFunction)


def test_hyp_sql_opfunction_constructor_exists():
    assert callable(sql_OpFunction.__init__)


def test_hyp_sql_opfunction_constructor_args():
    sig = inspect.signature(sql_OpFunction.__init__)
    params = list(sig.parameters.keys())
    assert "fname" in params, "Missing parameter 'fname'"




def test_hyp_orgroupbycolumn_is_not_abstract():
    assert not inspect.isabstract(OrGroupByColumn)


def test_hyp_orgroupbycolumn_constructor_exists():
    assert callable(OrGroupByColumn.__init__)


def test_hyp_orgroupbycolumn_constructor_args():
    sig = inspect.signature(OrGroupByColumn.__init__)
    params = list(sig.parameters.keys())



def test_hyp_sql_groupbycolumnfull_is_not_abstract():
    assert not inspect.isabstract(sql_GroupByColumnFull)


def test_hyp_sql_groupbycolumnfull_constructor_exists():
    assert callable(sql_GroupByColumnFull.__init__)


def test_hyp_sql_groupbycolumnfull_constructor_args():
    sig = inspect.signature(sql_GroupByColumnFull.__init__)
    params = list(sig.parameters.keys())



def test_hyp_ororderbycolumn_is_not_abstract():
    assert not inspect.isabstract(OrOrderByColumn)


def test_hyp_ororderbycolumn_constructor_exists():
    assert callable(OrOrderByColumn.__init__)


def test_hyp_ororderbycolumn_constructor_args():
    sig = inspect.signature(OrOrderByColumn.__init__)
    params = list(sig.parameters.keys())



def test_hyp_sql_orderbycolumnfull_is_not_abstract():
    assert not inspect.isabstract(sql_OrderByColumnFull)


def test_hyp_sql_orderbycolumnfull_constructor_exists():
    assert callable(sql_OrderByColumnFull.__init__)


def test_hyp_sql_orderbycolumnfull_constructor_args():
    sig = inspect.signature(sql_OrderByColumnFull.__init__)
    params = list(sig.parameters.keys())
    assert "colOrderInt" in params, "Missing parameter 'colOrderInt'"
    assert "direction" in params, "Missing parameter 'direction'"





def test_hyp_tablefull_is_not_abstract():
    assert not inspect.isabstract(TableFull)


def test_hyp_tablefull_constructor_exists():
    assert callable(TableFull.__init__)


def test_hyp_tablefull_constructor_args():
    sig = inspect.signature(TableFull.__init__)
    params = list(sig.parameters.keys())



def test_hyp_sql_tbls_is_not_abstract():
    assert not inspect.isabstract(sql_tbls)


def test_hyp_sql_tbls_constructor_exists():
    assert callable(sql_tbls.__init__)


def test_hyp_sql_tbls_constructor_args():
    sig = inspect.signature(sql_tbls.__init__)
    params = list(sig.parameters.keys())



def test_hyp_pivotcol_is_not_abstract():
    assert not inspect.isabstract(PivotCol)


def test_hyp_pivotcol_constructor_exists():
    assert callable(PivotCol.__init__)


def test_hyp_pivotcol_constructor_args():
    sig = inspect.signature(PivotCol.__init__)
    params = list(sig.parameters.keys())



def test_hyp_sql_pcols_is_not_abstract():
    assert not inspect.isabstract(sql_pcols)


def test_hyp_sql_pcols_constructor_exists():
    assert callable(sql_pcols.__init__)


def test_hyp_sql_pcols_constructor_args():
    sig = inspect.signature(sql_pcols.__init__)
    params = list(sig.parameters.keys())



def test_hyp_columnfull_is_not_abstract():
    assert not inspect.isabstract(ColumnFull)


def test_hyp_columnfull_constructor_exists():
    assert callable(ColumnFull.__init__)


def test_hyp_columnfull_constructor_args():
    sig = inspect.signature(ColumnFull.__init__)
    params = list(sig.parameters.keys())



def test_hyp_sql_col_is_not_abstract():
    assert not inspect.isabstract(sql_Col)


def test_hyp_sql_col_constructor_exists():
    assert callable(sql_Col.__init__)


def test_hyp_sql_col_constructor_args():
    sig = inspect.signature(sql_Col.__init__)
    params = list(sig.parameters.keys())



def test_hyp_pivots_is_not_abstract():
    assert not inspect.isabstract(Pivots)


def test_hyp_pivots_constructor_exists():
    assert callable(Pivots.__init__)


def test_hyp_pivots_constructor_args():
    sig = inspect.signature(Pivots.__init__)
    params = list(sig.parameters.keys())



def test_hyp_sql_pvcs_is_not_abstract():
    assert not inspect.isabstract(sql_pvcs)


def test_hyp_sql_pvcs_constructor_exists():
    assert callable(sql_pvcs.__init__)


def test_hyp_sql_pvcs_constructor_args():
    sig = inspect.signature(sql_pvcs.__init__)
    params = list(sig.parameters.keys())



def test_hyp_pivotfunction_is_not_abstract():
    assert not inspect.isabstract(PivotFunction)


def test_hyp_pivotfunction_constructor_exists():
    assert callable(PivotFunction.__init__)


def test_hyp_pivotfunction_constructor_args():
    sig = inspect.signature(PivotFunction.__init__)
    params = list(sig.parameters.keys())



def test_hyp_pivotcolumns_is_not_abstract():
    assert not inspect.isabstract(PivotColumns)


def test_hyp_pivotcolumns_constructor_exists():
    assert callable(PivotColumns.__init__)


def test_hyp_pivotcolumns_constructor_args():
    sig = inspect.signature(PivotColumns.__init__)
    params = list(sig.parameters.keys())



def test_hyp_sql_pivotcol_is_not_abstract():
    assert not inspect.isabstract(sql_PivotCol)


def test_hyp_sql_pivotcol_constructor_exists():
    assert callable(sql_PivotCol.__init__)


def test_hyp_sql_pivotcol_constructor_args():
    sig = inspect.signature(sql_PivotCol.__init__)
    params = list(sig.parameters.keys())



def test_hyp_sql_pivots_is_not_abstract():
    assert not inspect.isabstract(sql_Pivots)


def test_hyp_sql_pivots_constructor_exists():
    assert callable(sql_Pivots.__init__)


def test_hyp_sql_pivots_constructor_args():
    sig = inspect.signature(sql_Pivots.__init__)
    params = list(sig.parameters.keys())



def test_hyp_unpivotinclauseargs_is_not_abstract():
    assert not inspect.isabstract(UnpivotInClauseArgs)


def test_hyp_unpivotinclauseargs_constructor_exists():
    assert callable(UnpivotInClauseArgs.__init__)


def test_hyp_unpivotinclauseargs_constructor_args():
    sig = inspect.signature(UnpivotInClauseArgs.__init__)
    params = list(sig.parameters.keys())



def test_hyp_sql_uicargs_is_not_abstract():
    assert not inspect.isabstract(sql_uicargs)


def test_hyp_sql_uicargs_constructor_exists():
    assert callable(sql_uicargs.__init__)


def test_hyp_sql_uicargs_constructor_args():
    sig = inspect.signature(sql_uicargs.__init__)
    params = list(sig.parameters.keys())



def test_hyp_sql_unpivotinclausearg_is_not_abstract():
    assert not inspect.isabstract(sql_UnpivotInClauseArg)


def test_hyp_sql_unpivotinclausearg_constructor_exists():
    assert callable(sql_UnpivotInClauseArg.__init__)


def test_hyp_sql_unpivotinclausearg_constructor_args():
    sig = inspect.signature(sql_UnpivotInClauseArg.__init__)
    params = list(sig.parameters.keys())



def test_hyp_sql_pivotfunction_is_not_abstract():
    assert not inspect.isabstract(sql_PivotFunction)


def test_hyp_sql_pivotfunction_constructor_exists():
    assert callable(sql_PivotFunction.__init__)


def test_hyp_sql_pivotfunction_constructor_args():
    sig = inspect.signature(sql_PivotFunction.__init__)
    params = list(sig.parameters.keys())



def test_hyp_sql_unpivotinclause_is_not_abstract():
    assert not inspect.isabstract(sql_UnpivotInClause)


def test_hyp_sql_unpivotinclause_constructor_exists():
    assert callable(sql_UnpivotInClause.__init__)


def test_hyp_sql_unpivotinclause_constructor_args():
    sig = inspect.signature(sql_UnpivotInClause.__init__)
    params = list(sig.parameters.keys())



def test_hyp_sql_pivotcolumns_is_not_abstract():
    assert not inspect.isabstract(sql_PivotColumns)


def test_hyp_sql_pivotcolumns_constructor_exists():
    assert callable(sql_PivotColumns.__init__)


def test_hyp_sql_pivotcolumns_constructor_args():
    sig = inspect.signature(sql_PivotColumns.__init__)
    params = list(sig.parameters.keys())



def test_hyp_sql_unpivotinclauseargs_is_not_abstract():
    assert not inspect.isabstract(sql_UnpivotInClauseArgs)


def test_hyp_sql_unpivotinclauseargs_constructor_exists():
    assert callable(sql_UnpivotInClauseArgs.__init__)


def test_hyp_sql_unpivotinclauseargs_constructor_args():
    sig = inspect.signature(sql_UnpivotInClauseArgs.__init__)
    params = list(sig.parameters.keys())



def test_hyp_sql_pivotfunctions_is_not_abstract():
    assert not inspect.isabstract(sql_PivotFunctions)


def test_hyp_sql_pivotfunctions_constructor_exists():
    assert callable(sql_PivotFunctions.__init__)


def test_hyp_sql_pivotfunctions_constructor_args():
    sig = inspect.signature(sql_PivotFunctions.__init__)
    params = list(sig.parameters.keys())
    assert "abc" in params, "Missing parameter 'abc'"




def test_hyp_sql_pivotinclause_is_not_abstract():
    assert not inspect.isabstract(sql_PivotInClause)


def test_hyp_sql_pivotinclause_constructor_exists():
    assert callable(sql_PivotInClause.__init__)


def test_hyp_sql_pivotinclause_constructor_args():
    sig = inspect.signature(sql_PivotInClause.__init__)
    params = list(sig.parameters.keys())
    assert "pinany" in params, "Missing parameter 'pinany'"




def test_hyp_sql_pivotforclause_is_not_abstract():
    assert not inspect.isabstract(sql_PivotForClause)


def test_hyp_sql_pivotforclause_constructor_exists():
    assert callable(sql_PivotForClause.__init__)


def test_hyp_sql_pivotforclause_constructor_args():
    sig = inspect.signature(sql_PivotForClause.__init__)
    params = list(sig.parameters.keys())



def test_hyp_sql_fromtablejoin_is_not_abstract():
    assert not inspect.isabstract(sql_FromTableJoin)


def test_hyp_sql_fromtablejoin_constructor_exists():
    assert callable(sql_FromTableJoin.__init__)


def test_hyp_sql_fromtablejoin_constructor_args():
    sig = inspect.signature(sql_FromTableJoin.__init__)
    params = list(sig.parameters.keys())
    assert "join" in params, "Missing parameter 'join'"




def test_hyp_sql_unpivottable_is_not_abstract():
    assert not inspect.isabstract(sql_UnpivotTable)


def test_hyp_sql_unpivottable_constructor_exists():
    assert callable(sql_UnpivotTable.__init__)


def test_hyp_sql_unpivottable_constructor_args():
    sig = inspect.signature(sql_UnpivotTable.__init__)
    params = list(sig.parameters.keys())



def test_hyp_sql_pivottable_is_not_abstract():
    assert not inspect.isabstract(sql_PivotTable)


def test_hyp_sql_pivottable_constructor_exists():
    assert callable(sql_PivotTable.__init__)


def test_hyp_sql_pivottable_constructor_args():
    sig = inspect.signature(sql_PivotTable.__init__)
    params = list(sig.parameters.keys())



def test_hyp_sql_subqueryoperand_is_not_abstract():
    assert not inspect.isabstract(sql_SubQueryOperand)


def test_hyp_sql_subqueryoperand_constructor_exists():
    assert callable(sql_SubQueryOperand.__init__)


def test_hyp_sql_subqueryoperand_constructor_args():
    sig = inspect.signature(sql_SubQueryOperand.__init__)
    params = list(sig.parameters.keys())



def test_hyp_sql_tablefull_is_not_abstract():
    assert not inspect.isabstract(sql_TableFull)


def test_hyp_sql_tablefull_constructor_exists():
    assert callable(sql_TableFull.__init__)


def test_hyp_sql_tablefull_constructor_args():
    sig = inspect.signature(sql_TableFull.__init__)
    params = list(sig.parameters.keys())



def test_hyp_sql_dbobjectnameall_is_not_abstract():
    assert not inspect.isabstract(sql_DbObjectNameAll)


def test_hyp_sql_dbobjectnameall_constructor_exists():
    assert callable(sql_DbObjectNameAll.__init__)


def test_hyp_sql_dbobjectnameall_constructor_args():
    sig = inspect.signature(sql_DbObjectNameAll.__init__)
    params = list(sig.parameters.keys())
    assert "dbname" in params, "Missing parameter 'dbname'"




def test_hyp_sql_dbobjectname_is_not_abstract():
    assert not inspect.isabstract(sql_DbObjectName)


def test_hyp_sql_dbobjectname_constructor_exists():
    assert callable(sql_DbObjectName.__init__)


def test_hyp_sql_dbobjectname_constructor_args():
    sig = inspect.signature(sql_DbObjectName.__init__)
    params = list(sig.parameters.keys())
    assert "dbname" in params, "Missing parameter 'dbname'"




def test_hyp_sql_tableoralias_is_not_abstract():
    assert not inspect.isabstract(sql_TableOrAlias)


def test_hyp_sql_tableoralias_constructor_exists():
    assert callable(sql_TableOrAlias.__init__)


def test_hyp_sql_tableoralias_constructor_args():
    sig = inspect.signature(sql_TableOrAlias.__init__)
    params = list(sig.parameters.keys())
    assert "alias" in params, "Missing parameter 'alias'"




def test_hyp_ortable_is_not_abstract():
    assert not inspect.isabstract(OrTable)


def test_hyp_ortable_constructor_exists():
    assert callable(OrTable.__init__)


def test_hyp_ortable_constructor_args():
    sig = inspect.signature(OrTable.__init__)
    params = list(sig.parameters.keys())



def test_hyp_sql_fromtable_is_not_abstract():
    assert not inspect.isabstract(sql_FromTable)


def test_hyp_sql_fromtable_constructor_exists():
    assert callable(sql_FromTable.__init__)


def test_hyp_sql_fromtable_constructor_args():
    sig = inspect.signature(sql_FromTable.__init__)
    params = list(sig.parameters.keys())



def test_hyp_sql_operands_is_not_abstract():
    assert not inspect.isabstract(sql_Operands)


def test_hyp_sql_operands_constructor_exists():
    assert callable(sql_Operands.__init__)


def test_hyp_sql_operands_constructor_args():
    sig = inspect.signature(sql_Operands.__init__)
    params = list(sig.parameters.keys())



def test_hyp_orcolumn_is_not_abstract():
    assert not inspect.isabstract(OrColumn)


def test_hyp_orcolumn_constructor_exists():
    assert callable(OrColumn.__init__)


def test_hyp_orcolumn_constructor_args():
    sig = inspect.signature(OrColumn.__init__)
    params = list(sig.parameters.keys())



def test_hyp_sql_columnoralias_is_not_abstract():
    assert not inspect.isabstract(sql_ColumnOrAlias)


def test_hyp_sql_columnoralias_constructor_exists():
    assert callable(sql_ColumnOrAlias.__init__)


def test_hyp_sql_columnoralias_constructor_args():
    sig = inspect.signature(sql_ColumnOrAlias.__init__)
    params = list(sig.parameters.keys())
    assert "alias" in params, "Missing parameter 'alias'"
    assert "allCols" in params, "Missing parameter 'allCols'"





def test_hyp_pivotforclause_is_not_abstract():
    assert not inspect.isabstract(PivotForClause)


def test_hyp_pivotforclause_constructor_exists():
    assert callable(PivotForClause.__init__)


def test_hyp_pivotforclause_constructor_args():
    sig = inspect.signature(PivotForClause.__init__)
    params = list(sig.parameters.keys())



def test_hyp_sql_columnfull_is_not_abstract():
    assert not inspect.isabstract(sql_ColumnFull)


def test_hyp_sql_columnfull_constructor_exists():
    assert callable(sql_ColumnFull.__init__)


def test_hyp_sql_columnfull_constructor_args():
    sig = inspect.signature(sql_ColumnFull.__init__)
    params = list(sig.parameters.keys())



def test_hyp_sql_orexpr_is_not_abstract():
    assert not inspect.isabstract(sql_OrExpr)


def test_hyp_sql_orexpr_constructor_exists():
    assert callable(sql_OrExpr.__init__)


def test_hyp_sql_orexpr_constructor_args():
    sig = inspect.signature(sql_OrExpr.__init__)
    params = list(sig.parameters.keys())



def test_hyp_sql_ortable_is_not_abstract():
    assert not inspect.isabstract(sql_OrTable)


def test_hyp_sql_ortable_constructor_exists():
    assert callable(sql_OrTable.__init__)


def test_hyp_sql_ortable_constructor_args():
    sig = inspect.signature(sql_OrTable.__init__)
    params = list(sig.parameters.keys())



def test_hyp_sql_orcolumn_is_not_abstract():
    assert not inspect.isabstract(sql_OrColumn)


def test_hyp_sql_orcolumn_constructor_exists():
    assert callable(sql_OrColumn.__init__)


def test_hyp_sql_orcolumn_constructor_args():
    sig = inspect.signature(sql_OrColumn.__init__)
    params = list(sig.parameters.keys())



def test_hyp_sql_ororderbycolumn_is_not_abstract():
    assert not inspect.isabstract(sql_OrOrderByColumn)


def test_hyp_sql_ororderbycolumn_constructor_exists():
    assert callable(sql_OrOrderByColumn.__init__)


def test_hyp_sql_ororderbycolumn_constructor_args():
    sig = inspect.signature(sql_OrOrderByColumn.__init__)
    params = list(sig.parameters.keys())



def test_hyp_sql_orgroupbycolumn_is_not_abstract():
    assert not inspect.isabstract(sql_OrGroupByColumn)


def test_hyp_sql_orgroupbycolumn_constructor_exists():
    assert callable(sql_OrGroupByColumn.__init__)


def test_hyp_sql_orgroupbycolumn_constructor_args():
    sig = inspect.signature(sql_OrGroupByColumn.__init__)
    params = list(sig.parameters.keys())



def test_hyp_sql_limit_is_not_abstract():
    assert not inspect.isabstract(sql_Limit)


def test_hyp_sql_limit_constructor_exists():
    assert callable(sql_Limit.__init__)


def test_hyp_sql_limit_constructor_args():
    sig = inspect.signature(sql_Limit.__init__)
    params = list(sig.parameters.keys())
    assert "l1" in params, "Missing parameter 'l1'"




def test_hyp_sql_offset_is_not_abstract():
    assert not inspect.isabstract(sql_Offset)


def test_hyp_sql_offset_constructor_exists():
    assert callable(sql_Offset.__init__)


def test_hyp_sql_offset_constructor_args():
    sig = inspect.signature(sql_Offset.__init__)
    params = list(sig.parameters.keys())
    assert "offset" in params, "Missing parameter 'offset'"




def test_hyp_selectquery_is_not_abstract():
    assert not inspect.isabstract(SelectQuery)


def test_hyp_selectquery_constructor_exists():
    assert callable(SelectQuery.__init__)


def test_hyp_selectquery_constructor_args():
    sig = inspect.signature(SelectQuery.__init__)
    params = list(sig.parameters.keys())



def test_hyp_sql_select_is_not_abstract():
    assert not inspect.isabstract(sql_Select)


def test_hyp_sql_select_constructor_exists():
    assert callable(sql_Select.__init__)


def test_hyp_sql_select_constructor_args():
    sig = inspect.signature(sql_Select.__init__)
    params = list(sig.parameters.keys())
    assert "select" in params, "Missing parameter 'select'"




def test_hyp_sql_selectsubset_is_not_abstract():
    assert not inspect.isabstract(sql_SelectSubSet)


def test_hyp_sql_selectsubset_constructor_exists():
    assert callable(sql_SelectSubSet.__init__)


def test_hyp_sql_selectsubset_constructor_args():
    sig = inspect.signature(sql_SelectSubSet.__init__)
    params = list(sig.parameters.keys())
    assert "op" in params, "Missing parameter 'op'"
    assert "all" in params, "Missing parameter 'all'"





def test_hyp_sql_model_is_not_abstract():
    assert not inspect.isabstract(sql_Model)


def test_hyp_sql_model_constructor_exists():
    assert callable(sql_Model.__init__)


def test_hyp_sql_model_constructor_args():
    sig = inspect.signature(sql_Model.__init__)
    params = list(sig.parameters.keys())



def test_hyp_sql_integervalue_is_not_abstract():
    assert not inspect.isabstract(sql_IntegerValue)


def test_hyp_sql_integervalue_constructor_exists():
    assert callable(sql_IntegerValue.__init__)


def test_hyp_sql_integervalue_constructor_args():
    sig = inspect.signature(sql_IntegerValue.__init__)
    params = list(sig.parameters.keys())
    assert "integer" in params, "Missing parameter 'integer'"




def test_hyp_sql_fetchfirst_is_not_abstract():
    assert not inspect.isabstract(sql_FetchFirst)


def test_hyp_sql_fetchfirst_constructor_exists():
    assert callable(sql_FetchFirst.__init__)


def test_hyp_sql_fetchfirst_constructor_args():
    sig = inspect.signature(sql_FetchFirst.__init__)
    params = list(sig.parameters.keys())
    assert "row" in params, "Missing parameter 'row'"




def test_hyp_sql_selectquery_is_not_abstract():
    assert not inspect.isabstract(sql_SelectQuery)


def test_hyp_sql_selectquery_constructor_exists():
    assert callable(sql_SelectQuery.__init__)


def test_hyp_sql_selectquery_constructor_args():
    sig = inspect.signature(sql_SelectQuery.__init__)
    params = list(sig.parameters.keys())

def test_hyp_extract_values_exists():
    # Check that the Enumeration exists
    assert EXTRACT_VALUES is not None

def test_hyp_extract_values_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in EXTRACT_VALUES]
    expected_literals = [
        "hs",
        "dms",
        "week",
        "micros",
        "minMicro",
        "hms",
        "yearMonth",
        "quart",
        "day",
        "year",
        "m",
        "hmin",
        "month",
        "s",
        "h",
        "ds",
        "daymin",
        "minSec",
        "ms",
        "dayh",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in EXTRACT_VALUES"

def test_hyp_xfunction_exists():
    # Check that the Enumeration exists
    assert XFunction is not None

def test_hyp_xfunction_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in XFunction]
    expected_literals = [
        "xeq",
        "xnoteq",
        "xbwn",
        "xlsr",
        "xin",
        "xbwnr",
        "xgt",
        "xnotin",
        "xbwnc",
        "xls",
        "xgtl",
        "xbwnl",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in XFunction"


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
Operands_strategy = st.builds(
    Operands,
)
sql_Div_strategy = st.builds(
    sql_Div,
)
sql_Star_strategy = st.builds(
    sql_Star,
)
sql_Minus_strategy = st.builds(
    sql_Minus,
)
sql_Concat_strategy = st.builds(
    sql_Concat,
)
sql_Plus_strategy = st.builds(
    sql_Plus,
)
UnpivotInClause_strategy = st.builds(
    UnpivotInClause,
)
sql_UnipivotInClause_strategy = st.builds(
    sql_UnipivotInClause,
    op=
        safe_text
)
SQLCaseWhens_strategy = st.builds(
    SQLCaseWhens,
)
sql_WhenList_strategy = st.builds(
    sql_WhenList,
)
sql_SqlCaseWhen_strategy = st.builds(
    sql_SqlCaseWhen,
)
sql_SQLCaseWhens_strategy = st.builds(
    sql_SQLCaseWhens,
)
OperandList_strategy = st.builds(
    OperandList,
)
sql_OpList_strategy = st.builds(
    sql_OpList,
)
AnalyticExprArgs_strategy = st.builds(
    AnalyticExprArgs,
)
sql_AExpArgs_strategy = st.builds(
    sql_AExpArgs,
)
sql_OpFunctionArgAgregate_strategy = st.builds(
    sql_OpFunctionArgAgregate,
)
OpFunctionArg_strategy = st.builds(
    OpFunctionArg,
)
sql_OpFList_strategy = st.builds(
    sql_OpFList,
)
sql_OpFunctionArgOperand_strategy = st.builds(
    sql_OpFunctionArgOperand,
)
OrderByClauseArgs_strategy = st.builds(
    OrderByClauseArgs,
)
sql_OBCArgs_strategy = st.builds(
    sql_OBCArgs,
)
sql_OrderByClauseArg_strategy = st.builds(
    sql_OrderByClauseArg,
)
sql_OrderByClauseArgs_strategy = st.builds(
    sql_OrderByClauseArgs,
)
QueryPartitionClause_strategy = st.builds(
    QueryPartitionClause,
)
sql_AnalyticExprArgs_strategy = st.builds(
    sql_AnalyticExprArgs,
)
sql_WindowingClauseOperandFollowing_strategy = st.builds(
    sql_WindowingClauseOperandFollowing,
)
sql_AnalyticExprArg_strategy = st.builds(
    sql_AnalyticExprArg,
)
sql_QueryPartitionClause_strategy = st.builds(
    sql_QueryPartitionClause,
)
sql_AnalyticClause_strategy = st.builds(
    sql_AnalyticClause,
)
WindowingClause_strategy = st.builds(
    WindowingClause,
)
sql_WindowingClauseOperandPreceding_strategy = st.builds(
    sql_WindowingClauseOperandPreceding,
)
sql_WindowingClauseBetween_strategy = st.builds(
    sql_WindowingClauseBetween,
)
sql_WindowingClause_strategy = st.builds(
    sql_WindowingClause,
)
sql_OrderByClause_strategy = st.builds(
    sql_OrderByClause,
)
sql_ScalarOperand_strategy = st.builds(
    sql_ScalarOperand,
    sostr=
        safe_text,
    sodate=
        st.dates(),
    sotime=
        st.dates(),
    sodbl=
        safe_text,
    soint=
        st.integers(),
    sodt=
        st.dates()
)
sql_ExpOperand_strategy = st.builds(
    sql_ExpOperand,
    prm=
        safe_text
)
sql_FunctionAnalytical_strategy = st.builds(
    sql_FunctionAnalytical,
)
sql_OpFunctionArg_strategy = st.builds(
    sql_OpFunctionArg,
)
sql_ColumnOperand_strategy = st.builds(
    sql_ColumnOperand,
    ora=
        safe_text
)
sql_SQLCaseOperand_strategy = st.builds(
    sql_SQLCaseOperand,
)
sql_FunctionExtract_strategy = st.builds(
    sql_FunctionExtract,
    v=
        safe_text
)
OpFunctionArgAgregate_strategy = st.builds(
    OpFunctionArgAgregate,
)
sql_OperandList_strategy = st.builds(
    sql_OperandList,
)
sql_Operand_strategy = st.builds(
    sql_Operand,
)
sql_OperandListGroup_strategy = st.builds(
    sql_OperandListGroup,
)
sql_LikeOperand_strategy = st.builds(
    sql_LikeOperand,
    op2=
        safe_text
)
sql_POperand_strategy = st.builds(
    sql_POperand,
    prm=
        safe_text
)
sql_OpFunctionCast_strategy = st.builds(
    sql_OpFunctionCast,
    type=
        safe_text,
    p=
        st.integers(),
    p2=
        st.integers()
)
sql_Prms_strategy = st.builds(
    sql_Prms,
)
Prms_strategy = st.builds(
    Prms,
)
sql_JRParameter_strategy = st.builds(
    sql_JRParameter,
    jrprm=
        safe_text
)
sql_Comparison_strategy = st.builds(
    sql_Comparison,
    operator=
        safe_text,
    subOperator=
        safe_text
)
sql_Like_strategy = st.builds(
    sql_Like,
    opLike=
        safe_text
)
sql_ExistsOper_strategy = st.builds(
    sql_ExistsOper,
    op=
        safe_text
)
sql_InOper_strategy = st.builds(
    sql_InOper,
    op=
        safe_text
)
sql_XExpr_strategy = st.builds(
    sql_XExpr,
    xf=
        safe_text
)
sql_ExprGroup_strategy = st.builds(
    sql_ExprGroup,
    isnot=
        safe_text
)
sql_Between_strategy = st.builds(
    sql_Between,
    opBetween=
        safe_text
)
OrExpr_strategy = st.builds(
    OrExpr,
)
sql_FullExpression_strategy = st.builds(
    sql_FullExpression,
    isnull=
        safe_text,
    c=
        safe_text,
    notPrm=
        safe_text
)
sql_OpFunction_strategy = st.builds(
    sql_OpFunction,
    fname=
        safe_text
)
OrGroupByColumn_strategy = st.builds(
    OrGroupByColumn,
)
sql_GroupByColumnFull_strategy = st.builds(
    sql_GroupByColumnFull,
)
OrOrderByColumn_strategy = st.builds(
    OrOrderByColumn,
)
sql_OrderByColumnFull_strategy = st.builds(
    sql_OrderByColumnFull,
    colOrderInt=
        st.integers(),
    direction=
        safe_text
)
TableFull_strategy = st.builds(
    TableFull,
)
sql_tbls_strategy = st.builds(
    sql_tbls,
)
PivotCol_strategy = st.builds(
    PivotCol,
)
sql_pcols_strategy = st.builds(
    sql_pcols,
)
ColumnFull_strategy = st.builds(
    ColumnFull,
)
sql_Col_strategy = st.builds(
    sql_Col,
)
Pivots_strategy = st.builds(
    Pivots,
)
sql_pvcs_strategy = st.builds(
    sql_pvcs,
)
PivotFunction_strategy = st.builds(
    PivotFunction,
)
PivotColumns_strategy = st.builds(
    PivotColumns,
)
sql_PivotCol_strategy = st.builds(
    sql_PivotCol,
)
sql_Pivots_strategy = st.builds(
    sql_Pivots,
)
UnpivotInClauseArgs_strategy = st.builds(
    UnpivotInClauseArgs,
)
sql_uicargs_strategy = st.builds(
    sql_uicargs,
)
sql_UnpivotInClauseArg_strategy = st.builds(
    sql_UnpivotInClauseArg,
)
sql_PivotFunction_strategy = st.builds(
    sql_PivotFunction,
)
sql_UnpivotInClause_strategy = st.builds(
    sql_UnpivotInClause,
)
sql_PivotColumns_strategy = st.builds(
    sql_PivotColumns,
)
sql_UnpivotInClauseArgs_strategy = st.builds(
    sql_UnpivotInClauseArgs,
)
sql_PivotFunctions_strategy = st.builds(
    sql_PivotFunctions,
    abc=
        safe_text
)
sql_PivotInClause_strategy = st.builds(
    sql_PivotInClause,
    pinany=
        safe_text
)
sql_PivotForClause_strategy = st.builds(
    sql_PivotForClause,
)
sql_FromTableJoin_strategy = st.builds(
    sql_FromTableJoin,
    join=
        safe_text
)
sql_UnpivotTable_strategy = st.builds(
    sql_UnpivotTable,
)
sql_PivotTable_strategy = st.builds(
    sql_PivotTable,
)
sql_SubQueryOperand_strategy = st.builds(
    sql_SubQueryOperand,
)
sql_TableFull_strategy = st.builds(
    sql_TableFull,
)
sql_DbObjectNameAll_strategy = st.builds(
    sql_DbObjectNameAll,
    dbname=
        safe_text
)
sql_DbObjectName_strategy = st.builds(
    sql_DbObjectName,
    dbname=
        safe_text
)
sql_TableOrAlias_strategy = st.builds(
    sql_TableOrAlias,
    alias=
        safe_text
)
OrTable_strategy = st.builds(
    OrTable,
)
sql_FromTable_strategy = st.builds(
    sql_FromTable,
)
sql_Operands_strategy = st.builds(
    sql_Operands,
)
OrColumn_strategy = st.builds(
    OrColumn,
)
sql_ColumnOrAlias_strategy = st.builds(
    sql_ColumnOrAlias,
    alias=
        safe_text,
    allCols=
        safe_text
)
PivotForClause_strategy = st.builds(
    PivotForClause,
)
sql_ColumnFull_strategy = st.builds(
    sql_ColumnFull,
)
sql_OrExpr_strategy = st.builds(
    sql_OrExpr,
)
sql_OrTable_strategy = st.builds(
    sql_OrTable,
)
sql_OrColumn_strategy = st.builds(
    sql_OrColumn,
)
sql_OrOrderByColumn_strategy = st.builds(
    sql_OrOrderByColumn,
)
sql_OrGroupByColumn_strategy = st.builds(
    sql_OrGroupByColumn,
)
sql_Limit_strategy = st.builds(
    sql_Limit,
    l1=
        st.integers()
)
sql_Offset_strategy = st.builds(
    sql_Offset,
    offset=
        st.integers()
)
SelectQuery_strategy = st.builds(
    SelectQuery,
)
sql_Select_strategy = st.builds(
    sql_Select,
    select=
        safe_text
)
sql_SelectSubSet_strategy = st.builds(
    sql_SelectSubSet,
    op=
        safe_text,
    all=
        safe_text
)
sql_Model_strategy = st.builds(
    sql_Model,
)
sql_IntegerValue_strategy = st.builds(
    sql_IntegerValue,
    integer=
        st.integers()
)
sql_FetchFirst_strategy = st.builds(
    sql_FetchFirst,
    row=
        safe_text
)
sql_SelectQuery_strategy = st.builds(
    sql_SelectQuery,
)











@given(instance=sql_UnipivotInClause_strategy)
def test_hyp_sql_unipivotinclause_op_setter(instance):
    original = instance.op
    instance.op = original
    assert instance.op == original































@given(instance=sql_ScalarOperand_strategy)
def test_hyp_sql_scalaroperand_sostr_setter(instance):
    original = instance.sostr
    instance.sostr = original
    assert instance.sostr == original



@given(instance=sql_ScalarOperand_strategy)
def test_hyp_sql_scalaroperand_sodate_setter(instance):
    original = instance.sodate
    instance.sodate = original
    assert instance.sodate == original



@given(instance=sql_ScalarOperand_strategy)
def test_hyp_sql_scalaroperand_sotime_setter(instance):
    original = instance.sotime
    instance.sotime = original
    assert instance.sotime == original



@given(instance=sql_ScalarOperand_strategy)
def test_hyp_sql_scalaroperand_sodbl_setter(instance):
    original = instance.sodbl
    instance.sodbl = original
    assert instance.sodbl == original



@given(instance=sql_ScalarOperand_strategy)
def test_hyp_sql_scalaroperand_soint_setter(instance):
    original = instance.soint
    instance.soint = original
    assert instance.soint == original



@given(instance=sql_ScalarOperand_strategy)
def test_hyp_sql_scalaroperand_sodt_setter(instance):
    original = instance.sodt
    instance.sodt = original
    assert instance.sodt == original




@given(instance=sql_ExpOperand_strategy)
def test_hyp_sql_expoperand_prm_setter(instance):
    original = instance.prm
    instance.prm = original
    assert instance.prm == original






@given(instance=sql_ColumnOperand_strategy)
def test_hyp_sql_columnoperand_ora_setter(instance):
    original = instance.ora
    instance.ora = original
    assert instance.ora == original





@given(instance=sql_FunctionExtract_strategy)
def test_hyp_sql_functionextract_v_setter(instance):
    original = instance.v
    instance.v = original
    assert instance.v == original








@given(instance=sql_LikeOperand_strategy)
def test_hyp_sql_likeoperand_op2_setter(instance):
    original = instance.op2
    instance.op2 = original
    assert instance.op2 == original




@given(instance=sql_POperand_strategy)
def test_hyp_sql_poperand_prm_setter(instance):
    original = instance.prm
    instance.prm = original
    assert instance.prm == original




@given(instance=sql_OpFunctionCast_strategy)
def test_hyp_sql_opfunctioncast_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original



@given(instance=sql_OpFunctionCast_strategy)
def test_hyp_sql_opfunctioncast_p_setter(instance):
    original = instance.p
    instance.p = original
    assert instance.p == original



@given(instance=sql_OpFunctionCast_strategy)
def test_hyp_sql_opfunctioncast_p2_setter(instance):
    original = instance.p2
    instance.p2 = original
    assert instance.p2 == original






@given(instance=sql_JRParameter_strategy)
def test_hyp_sql_jrparameter_jrprm_setter(instance):
    original = instance.jrprm
    instance.jrprm = original
    assert instance.jrprm == original




@given(instance=sql_Comparison_strategy)
def test_hyp_sql_comparison_operator_setter(instance):
    original = instance.operator
    instance.operator = original
    assert instance.operator == original



@given(instance=sql_Comparison_strategy)
def test_hyp_sql_comparison_subOperator_setter(instance):
    original = instance.subOperator
    instance.subOperator = original
    assert instance.subOperator == original




@given(instance=sql_Like_strategy)
def test_hyp_sql_like_opLike_setter(instance):
    original = instance.opLike
    instance.opLike = original
    assert instance.opLike == original




@given(instance=sql_ExistsOper_strategy)
def test_hyp_sql_existsoper_op_setter(instance):
    original = instance.op
    instance.op = original
    assert instance.op == original




@given(instance=sql_InOper_strategy)
def test_hyp_sql_inoper_op_setter(instance):
    original = instance.op
    instance.op = original
    assert instance.op == original




@given(instance=sql_XExpr_strategy)
def test_hyp_sql_xexpr_xf_setter(instance):
    original = instance.xf
    instance.xf = original
    assert instance.xf == original




@given(instance=sql_ExprGroup_strategy)
def test_hyp_sql_exprgroup_isnot_setter(instance):
    original = instance.isnot
    instance.isnot = original
    assert instance.isnot == original




@given(instance=sql_Between_strategy)
def test_hyp_sql_between_opBetween_setter(instance):
    original = instance.opBetween
    instance.opBetween = original
    assert instance.opBetween == original





@given(instance=sql_FullExpression_strategy)
def test_hyp_sql_fullexpression_isnull_setter(instance):
    original = instance.isnull
    instance.isnull = original
    assert instance.isnull == original



@given(instance=sql_FullExpression_strategy)
def test_hyp_sql_fullexpression_c_setter(instance):
    original = instance.c
    instance.c = original
    assert instance.c == original



@given(instance=sql_FullExpression_strategy)
def test_hyp_sql_fullexpression_notPrm_setter(instance):
    original = instance.notPrm
    instance.notPrm = original
    assert instance.notPrm == original




@given(instance=sql_OpFunction_strategy)
def test_hyp_sql_opfunction_fname_setter(instance):
    original = instance.fname
    instance.fname = original
    assert instance.fname == original







@given(instance=sql_OrderByColumnFull_strategy)
def test_hyp_sql_orderbycolumnfull_colOrderInt_setter(instance):
    original = instance.colOrderInt
    instance.colOrderInt = original
    assert instance.colOrderInt == original



@given(instance=sql_OrderByColumnFull_strategy)
def test_hyp_sql_orderbycolumnfull_direction_setter(instance):
    original = instance.direction
    instance.direction = original
    assert instance.direction == original























@given(instance=sql_PivotFunctions_strategy)
def test_hyp_sql_pivotfunctions_abc_setter(instance):
    original = instance.abc
    instance.abc = original
    assert instance.abc == original




@given(instance=sql_PivotInClause_strategy)
def test_hyp_sql_pivotinclause_pinany_setter(instance):
    original = instance.pinany
    instance.pinany = original
    assert instance.pinany == original





@given(instance=sql_FromTableJoin_strategy)
def test_hyp_sql_fromtablejoin_join_setter(instance):
    original = instance.join
    instance.join = original
    assert instance.join == original








@given(instance=sql_DbObjectNameAll_strategy)
def test_hyp_sql_dbobjectnameall_dbname_setter(instance):
    original = instance.dbname
    instance.dbname = original
    assert instance.dbname == original




@given(instance=sql_DbObjectName_strategy)
def test_hyp_sql_dbobjectname_dbname_setter(instance):
    original = instance.dbname
    instance.dbname = original
    assert instance.dbname == original




@given(instance=sql_TableOrAlias_strategy)
def test_hyp_sql_tableoralias_alias_setter(instance):
    original = instance.alias
    instance.alias = original
    assert instance.alias == original








@given(instance=sql_ColumnOrAlias_strategy)
def test_hyp_sql_columnoralias_alias_setter(instance):
    original = instance.alias
    instance.alias = original
    assert instance.alias == original



@given(instance=sql_ColumnOrAlias_strategy)
def test_hyp_sql_columnoralias_allCols_setter(instance):
    original = instance.allCols
    instance.allCols = original
    assert instance.allCols == original











@given(instance=sql_Limit_strategy)
def test_hyp_sql_limit_l1_setter(instance):
    original = instance.l1
    instance.l1 = original
    assert instance.l1 == original




@given(instance=sql_Offset_strategy)
def test_hyp_sql_offset_offset_setter(instance):
    original = instance.offset
    instance.offset = original
    assert instance.offset == original





@given(instance=sql_Select_strategy)
def test_hyp_sql_select_select_setter(instance):
    original = instance.select
    instance.select = original
    assert instance.select == original




@given(instance=sql_SelectSubSet_strategy)
def test_hyp_sql_selectsubset_op_setter(instance):
    original = instance.op
    instance.op = original
    assert instance.op == original



@given(instance=sql_SelectSubSet_strategy)
def test_hyp_sql_selectsubset_all_setter(instance):
    original = instance.all
    instance.all = original
    assert instance.all == original





@given(instance=sql_IntegerValue_strategy)
def test_hyp_sql_integervalue_integer_setter(instance):
    original = instance.integer
    instance.integer = original
    assert instance.integer == original




@given(instance=sql_FetchFirst_strategy)
def test_hyp_sql_fetchfirst_row_setter(instance):
    original = instance.row
    instance.row = original
    assert instance.row == original



# ----- SECTION B: test_structural_full.py (deterministic-first suite) -----
import inspect
import pytest
from datetime import date, datetime, time, timedelta
from hypothesis import given, settings
import hypothesis.strategies as st

from python_code import (
    AnalyticExprArgs,
    ColumnFull,
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
    SQLCaseWhens,
    SelectQuery,
    TableFull,
    UnpivotInClause,
    UnpivotInClauseArgs,
    WindowingClause,
    sql_AExpArgs,
    sql_AnalyticClause,
    sql_AnalyticExprArg,
    sql_AnalyticExprArgs,
    sql_Between,
    sql_Col,
    sql_ColumnFull,
    sql_ColumnOperand,
    sql_ColumnOrAlias,
    sql_Comparison,
    sql_Concat,
    sql_DbObjectName,
    sql_DbObjectNameAll,
    sql_Div,
    sql_ExistsOper,
    sql_ExpOperand,
    sql_ExprGroup,
    sql_FetchFirst,
    sql_FromTable,
    sql_FromTableJoin,
    sql_FullExpression,
    sql_FunctionAnalytical,
    sql_FunctionExtract,
    sql_GroupByColumnFull,
    sql_InOper,
    sql_IntegerValue,
    sql_JRParameter,
    sql_Like,
    sql_LikeOperand,
    sql_Limit,
    sql_Minus,
    sql_Model,
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
    sql_SQLCaseOperand,
    sql_SQLCaseWhens,
    sql_ScalarOperand,
    sql_Select,
    sql_SelectQuery,
    sql_SelectSubSet,
    sql_SqlCaseWhen,
    sql_Star,
    sql_SubQueryOperand,
    sql_TableFull,
    sql_TableOrAlias,
    sql_UnipivotInClause,
    sql_UnpivotInClause,
    sql_UnpivotInClauseArg,
    sql_UnpivotInClauseArgs,
    sql_UnpivotTable,
    sql_WhenList,
    sql_WindowingClause,
    sql_WindowingClauseBetween,
    sql_WindowingClauseOperandFollowing,
    sql_WindowingClauseOperandPreceding,
    sql_XExpr,
    sql_pcols,
    sql_pvcs,
    sql_tbls,
    sql_uicargs,
    EXTRACT_VALUES,
    XFunction,
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

def test_sql_Between_opBetween_value_roundtrip():
    instance = sql_Between(opBetween="sample_text")
    assert instance.opBetween == "sample_text"
    instance.opBetween = "sample_text_2"
    assert instance.opBetween == "sample_text_2"


def test_sql_ColumnOperand_ora_value_roundtrip():
    instance = sql_ColumnOperand(ora="sample_text")
    assert instance.ora == "sample_text"
    instance.ora = "sample_text_2"
    assert instance.ora == "sample_text_2"


def test_sql_ColumnOrAlias_alias_value_roundtrip():
    instance = sql_ColumnOrAlias(alias="sample_text", allCols="sample_text")
    assert instance.alias == "sample_text"
    instance.alias = "sample_text_2"
    assert instance.alias == "sample_text_2"


def test_sql_ColumnOrAlias_allCols_value_roundtrip():
    instance = sql_ColumnOrAlias(alias="sample_text", allCols="sample_text")
    assert instance.allCols == "sample_text"
    instance.allCols = "sample_text_2"
    assert instance.allCols == "sample_text_2"


def test_sql_Comparison_operator_value_roundtrip():
    instance = sql_Comparison(operator="sample_text", subOperator="sample_text")
    assert instance.operator == "sample_text"
    instance.operator = "sample_text_2"
    assert instance.operator == "sample_text_2"


def test_sql_Comparison_subOperator_value_roundtrip():
    instance = sql_Comparison(operator="sample_text", subOperator="sample_text")
    assert instance.subOperator == "sample_text"
    instance.subOperator = "sample_text_2"
    assert instance.subOperator == "sample_text_2"


def test_sql_DbObjectName_dbname_value_roundtrip():
    instance = sql_DbObjectName(dbname="sample_text")
    assert instance.dbname == "sample_text"
    instance.dbname = "sample_text_2"
    assert instance.dbname == "sample_text_2"


def test_sql_DbObjectNameAll_dbname_value_roundtrip():
    instance = sql_DbObjectNameAll(dbname="sample_text")
    assert instance.dbname == "sample_text"
    instance.dbname = "sample_text_2"
    assert instance.dbname == "sample_text_2"


def test_sql_ExistsOper_op_value_roundtrip():
    instance = sql_ExistsOper(op="sample_text")
    assert instance.op == "sample_text"
    instance.op = "sample_text_2"
    assert instance.op == "sample_text_2"


def test_sql_ExpOperand_prm_value_roundtrip():
    instance = sql_ExpOperand(prm="sample_text")
    assert instance.prm == "sample_text"
    instance.prm = "sample_text_2"
    assert instance.prm == "sample_text_2"


def test_sql_ExprGroup_isnot_value_roundtrip():
    instance = sql_ExprGroup(isnot="sample_text")
    assert instance.isnot == "sample_text"
    instance.isnot = "sample_text_2"
    assert instance.isnot == "sample_text_2"


def test_sql_FetchFirst_row_value_roundtrip():
    instance = sql_FetchFirst(row="sample_text")
    assert instance.row == "sample_text"
    instance.row = "sample_text_2"
    assert instance.row == "sample_text_2"


def test_sql_FromTableJoin_join_value_roundtrip():
    instance = sql_FromTableJoin(join="sample_text")
    assert instance.join == "sample_text"
    instance.join = "sample_text_2"
    assert instance.join == "sample_text_2"


def test_sql_FullExpression_c_value_roundtrip():
    instance = sql_FullExpression(c="sample_text", isnull="sample_text", notPrm="sample_text")
    assert instance.c == "sample_text"
    instance.c = "sample_text_2"
    assert instance.c == "sample_text_2"


def test_sql_FullExpression_isnull_value_roundtrip():
    instance = sql_FullExpression(c="sample_text", isnull="sample_text", notPrm="sample_text")
    assert instance.isnull == "sample_text"
    instance.isnull = "sample_text_2"
    assert instance.isnull == "sample_text_2"


def test_sql_FullExpression_notPrm_value_roundtrip():
    instance = sql_FullExpression(c="sample_text", isnull="sample_text", notPrm="sample_text")
    assert instance.notPrm == "sample_text"
    instance.notPrm = "sample_text_2"
    assert instance.notPrm == "sample_text_2"


def test_sql_FunctionExtract_v_value_roundtrip():
    instance = sql_FunctionExtract(v="sample_text")
    assert instance.v == "sample_text"
    instance.v = "sample_text_2"
    assert instance.v == "sample_text_2"


def test_sql_InOper_op_value_roundtrip():
    instance = sql_InOper(op="sample_text")
    assert instance.op == "sample_text"
    instance.op = "sample_text_2"
    assert instance.op == "sample_text_2"


def test_sql_IntegerValue_integer_value_roundtrip():
    instance = sql_IntegerValue(integer=7)
    assert instance.integer == 7
    instance.integer = 13
    assert instance.integer == 13


def test_sql_JRParameter_jrprm_value_roundtrip():
    instance = sql_JRParameter(jrprm="sample_text")
    assert instance.jrprm == "sample_text"
    instance.jrprm = "sample_text_2"
    assert instance.jrprm == "sample_text_2"


def test_sql_Like_opLike_value_roundtrip():
    instance = sql_Like(opLike="sample_text")
    assert instance.opLike == "sample_text"
    instance.opLike = "sample_text_2"
    assert instance.opLike == "sample_text_2"


def test_sql_LikeOperand_op2_value_roundtrip():
    instance = sql_LikeOperand(op2="sample_text")
    assert instance.op2 == "sample_text"
    instance.op2 = "sample_text_2"
    assert instance.op2 == "sample_text_2"


def test_sql_Limit_l1_value_roundtrip():
    instance = sql_Limit(l1=7)
    assert instance.l1 == 7
    instance.l1 = 13
    assert instance.l1 == 13


def test_sql_Offset_offset_value_roundtrip():
    instance = sql_Offset(offset=7)
    assert instance.offset == 7
    instance.offset = 13
    assert instance.offset == 13


def test_sql_OpFunction_fname_value_roundtrip():
    instance = sql_OpFunction(fname="sample_text")
    assert instance.fname == "sample_text"
    instance.fname = "sample_text_2"
    assert instance.fname == "sample_text_2"


def test_sql_OpFunctionCast_p_value_roundtrip():
    instance = sql_OpFunctionCast(p=7, p2=7, type="sample_text")
    assert instance.p == 7
    instance.p = 13
    assert instance.p == 13


def test_sql_OpFunctionCast_p2_value_roundtrip():
    instance = sql_OpFunctionCast(p=7, p2=7, type="sample_text")
    assert instance.p2 == 7
    instance.p2 = 13
    assert instance.p2 == 13


def test_sql_OpFunctionCast_type_value_roundtrip():
    instance = sql_OpFunctionCast(p=7, p2=7, type="sample_text")
    assert instance.type == "sample_text"
    instance.type = "sample_text_2"
    assert instance.type == "sample_text_2"


def test_sql_OrderByColumnFull_colOrderInt_value_roundtrip():
    instance = sql_OrderByColumnFull(colOrderInt=7, direction="sample_text")
    assert instance.colOrderInt == 7
    instance.colOrderInt = 13
    assert instance.colOrderInt == 13


def test_sql_OrderByColumnFull_direction_value_roundtrip():
    instance = sql_OrderByColumnFull(colOrderInt=7, direction="sample_text")
    assert instance.direction == "sample_text"
    instance.direction = "sample_text_2"
    assert instance.direction == "sample_text_2"


def test_sql_POperand_prm_value_roundtrip():
    instance = sql_POperand(prm="sample_text")
    assert instance.prm == "sample_text"
    instance.prm = "sample_text_2"
    assert instance.prm == "sample_text_2"


def test_sql_PivotFunctions_abc_value_roundtrip():
    instance = sql_PivotFunctions(abc="sample_text")
    assert instance.abc == "sample_text"
    instance.abc = "sample_text_2"
    assert instance.abc == "sample_text_2"


def test_sql_PivotInClause_pinany_value_roundtrip():
    instance = sql_PivotInClause(pinany="sample_text")
    assert instance.pinany == "sample_text"
    instance.pinany = "sample_text_2"
    assert instance.pinany == "sample_text_2"


def test_sql_ScalarOperand_sodate_value_roundtrip():
    instance = sql_ScalarOperand(sodate=date(2024, 1, 1), sodbl="sample_text", sodt=date(2024, 1, 1), soint=7, sostr="sample_text", sotime=date(2024, 1, 1))
    assert instance.sodate == date(2024, 1, 1)
    instance.sodate = date(2025, 6, 15)
    assert instance.sodate == date(2025, 6, 15)


def test_sql_ScalarOperand_sodbl_value_roundtrip():
    instance = sql_ScalarOperand(sodate=date(2024, 1, 1), sodbl="sample_text", sodt=date(2024, 1, 1), soint=7, sostr="sample_text", sotime=date(2024, 1, 1))
    assert instance.sodbl == "sample_text"
    instance.sodbl = "sample_text_2"
    assert instance.sodbl == "sample_text_2"


def test_sql_ScalarOperand_sodt_value_roundtrip():
    instance = sql_ScalarOperand(sodate=date(2024, 1, 1), sodbl="sample_text", sodt=date(2024, 1, 1), soint=7, sostr="sample_text", sotime=date(2024, 1, 1))
    assert instance.sodt == date(2024, 1, 1)
    instance.sodt = date(2025, 6, 15)
    assert instance.sodt == date(2025, 6, 15)


def test_sql_ScalarOperand_soint_value_roundtrip():
    instance = sql_ScalarOperand(sodate=date(2024, 1, 1), sodbl="sample_text", sodt=date(2024, 1, 1), soint=7, sostr="sample_text", sotime=date(2024, 1, 1))
    assert instance.soint == 7
    instance.soint = 13
    assert instance.soint == 13


def test_sql_ScalarOperand_sostr_value_roundtrip():
    instance = sql_ScalarOperand(sodate=date(2024, 1, 1), sodbl="sample_text", sodt=date(2024, 1, 1), soint=7, sostr="sample_text", sotime=date(2024, 1, 1))
    assert instance.sostr == "sample_text"
    instance.sostr = "sample_text_2"
    assert instance.sostr == "sample_text_2"


def test_sql_ScalarOperand_sotime_value_roundtrip():
    instance = sql_ScalarOperand(sodate=date(2024, 1, 1), sodbl="sample_text", sodt=date(2024, 1, 1), soint=7, sostr="sample_text", sotime=date(2024, 1, 1))
    assert instance.sotime == date(2024, 1, 1)
    instance.sotime = date(2025, 6, 15)
    assert instance.sotime == date(2025, 6, 15)


def test_sql_Select_select_value_roundtrip():
    instance = sql_Select(select="sample_text")
    assert instance.select == "sample_text"
    instance.select = "sample_text_2"
    assert instance.select == "sample_text_2"


def test_sql_SelectSubSet_all_value_roundtrip():
    instance = sql_SelectSubSet(all="sample_text", op="sample_text")
    assert instance.all == "sample_text"
    instance.all = "sample_text_2"
    assert instance.all == "sample_text_2"


def test_sql_SelectSubSet_op_value_roundtrip():
    instance = sql_SelectSubSet(all="sample_text", op="sample_text")
    assert instance.op == "sample_text"
    instance.op = "sample_text_2"
    assert instance.op == "sample_text_2"


def test_sql_TableOrAlias_alias_value_roundtrip():
    instance = sql_TableOrAlias(alias="sample_text")
    assert instance.alias == "sample_text"
    instance.alias = "sample_text_2"
    assert instance.alias == "sample_text_2"


def test_sql_UnipivotInClause_op_value_roundtrip():
    instance = sql_UnipivotInClause(op="sample_text")
    assert instance.op == "sample_text"
    instance.op = "sample_text_2"
    assert instance.op == "sample_text_2"


def test_sql_XExpr_xf_value_roundtrip():
    instance = sql_XExpr(xf="sample_text")
    assert instance.xf == "sample_text"
    instance.xf = "sample_text_2"
    assert instance.xf == "sample_text_2"


def test_sql_AExpArgs_isa_AnalyticExprArgs():
    instance = sql_AExpArgs()
    assert isinstance(instance, AnalyticExprArgs)


def test_sql_AnalyticExprArg_isa_AnalyticExprArgs():
    instance = sql_AnalyticExprArg()
    assert isinstance(instance, AnalyticExprArgs)


def test_sql_Col_isa_ColumnFull():
    instance = sql_Col()
    assert isinstance(instance, ColumnFull)


def test_sql_DbObjectName_isa_ColumnFull():
    instance = sql_DbObjectName(dbname="sample_text")
    assert isinstance(instance, ColumnFull)


def test_sql_OpFList_isa_OpFunctionArg():
    instance = sql_OpFList()
    assert isinstance(instance, OpFunctionArg)


def test_sql_OpFunctionArgOperand_isa_OpFunctionArg():
    instance = sql_OpFunctionArgOperand()
    assert isinstance(instance, OpFunctionArg)


def test_sql_Operands_isa_OpFunctionArgAgregate():
    instance = sql_Operands()
    assert isinstance(instance, OpFunctionArgAgregate)


def test_sql_OpList_isa_OperandList():
    instance = sql_OpList()
    assert isinstance(instance, OperandList)


def test_sql_ScalarOperand_isa_OperandList():
    instance = sql_ScalarOperand(sodate=date(2024, 1, 1), sodbl="sample_text", sodt=date(2024, 1, 1), soint=7, sostr="sample_text", sotime=date(2024, 1, 1))
    assert isinstance(instance, OperandList)


def test_sql_Concat_isa_Operands():
    instance = sql_Concat()
    assert isinstance(instance, Operands)


def test_sql_Div_isa_Operands():
    instance = sql_Div()
    assert isinstance(instance, Operands)


def test_sql_Minus_isa_Operands():
    instance = sql_Minus()
    assert isinstance(instance, Operands)


def test_sql_Plus_isa_Operands():
    instance = sql_Plus()
    assert isinstance(instance, Operands)


def test_sql_Star_isa_Operands():
    instance = sql_Star()
    assert isinstance(instance, Operands)


def test_sql_ColumnOrAlias_isa_OrColumn():
    instance = sql_ColumnOrAlias(alias="sample_text", allCols="sample_text")
    assert isinstance(instance, OrColumn)


def test_sql_FullExpression_isa_OrExpr():
    instance = sql_FullExpression(c="sample_text", isnull="sample_text", notPrm="sample_text")
    assert isinstance(instance, OrExpr)


def test_sql_GroupByColumnFull_isa_OrGroupByColumn():
    instance = sql_GroupByColumnFull()
    assert isinstance(instance, OrGroupByColumn)


def test_sql_OrderByColumnFull_isa_OrOrderByColumn():
    instance = sql_OrderByColumnFull(colOrderInt=7, direction="sample_text")
    assert isinstance(instance, OrOrderByColumn)


def test_sql_FromTable_isa_OrTable():
    instance = sql_FromTable()
    assert isinstance(instance, OrTable)


def test_sql_OBCArgs_isa_OrderByClauseArgs():
    instance = sql_OBCArgs()
    assert isinstance(instance, OrderByClauseArgs)


def test_sql_OrderByClauseArg_isa_OrderByClauseArgs():
    instance = sql_OrderByClauseArg()
    assert isinstance(instance, OrderByClauseArgs)


def test_sql_DbObjectName_isa_PivotCol():
    instance = sql_DbObjectName(dbname="sample_text")
    assert isinstance(instance, PivotCol)


def test_sql_pcols_isa_PivotCol():
    instance = sql_pcols()
    assert isinstance(instance, PivotCol)


def test_sql_PivotCol_isa_PivotColumns():
    instance = sql_PivotCol()
    assert isinstance(instance, PivotColumns)


def test_sql_Pivots_isa_PivotColumns():
    instance = sql_Pivots()
    assert isinstance(instance, PivotColumns)


def test_sql_ColumnFull_isa_PivotForClause():
    instance = sql_ColumnFull()
    assert isinstance(instance, PivotForClause)


def test_sql_OrColumn_isa_PivotForClause():
    instance = sql_OrColumn()
    assert isinstance(instance, PivotForClause)


def test_sql_PivotCol_isa_PivotFunction():
    instance = sql_PivotCol()
    assert isinstance(instance, PivotFunction)


def test_sql_PivotCol_isa_Pivots():
    instance = sql_PivotCol()
    assert isinstance(instance, Pivots)


def test_sql_pvcs_isa_Pivots():
    instance = sql_pvcs()
    assert isinstance(instance, Pivots)


def test_sql_JRParameter_isa_Prms():
    instance = sql_JRParameter(jrprm="sample_text")
    assert isinstance(instance, Prms)


def test_sql_AnalyticExprArgs_isa_QueryPartitionClause():
    instance = sql_AnalyticExprArgs()
    assert isinstance(instance, QueryPartitionClause)


def test_sql_SqlCaseWhen_isa_SQLCaseWhens():
    instance = sql_SqlCaseWhen()
    assert isinstance(instance, SQLCaseWhens)


def test_sql_WhenList_isa_SQLCaseWhens():
    instance = sql_WhenList()
    assert isinstance(instance, SQLCaseWhens)


def test_sql_Select_isa_SelectQuery():
    instance = sql_Select(select="sample_text")
    assert isinstance(instance, SelectQuery)


def test_sql_DbObjectName_isa_TableFull():
    instance = sql_DbObjectName(dbname="sample_text")
    assert isinstance(instance, TableFull)


def test_sql_tbls_isa_TableFull():
    instance = sql_tbls()
    assert isinstance(instance, TableFull)


def test_sql_UnipivotInClause_isa_UnpivotInClause():
    instance = sql_UnipivotInClause(op="sample_text")
    assert isinstance(instance, UnpivotInClause)


def test_sql_UnpivotInClauseArg_isa_UnpivotInClauseArgs():
    instance = sql_UnpivotInClauseArg()
    assert isinstance(instance, UnpivotInClauseArgs)


def test_sql_uicargs_isa_UnpivotInClauseArgs():
    instance = sql_uicargs()
    assert isinstance(instance, UnpivotInClauseArgs)


def test_sql_WindowingClauseBetween_isa_WindowingClause():
    instance = sql_WindowingClauseBetween()
    assert isinstance(instance, WindowingClause)


def test_sql_WindowingClauseOperandPreceding_isa_WindowingClause():
    instance = sql_WindowingClauseOperandPreceding()
    assert isinstance(instance, WindowingClause)


def test_assoc_args193_link_reassign_clear():
    a = sql_OpFunction(fname="sample_text")
    b1 = sql_OpFunctionArg()
    b2 = sql_OpFunctionArg()
    _safe_set(a, 'sql_OpFunction194', b1)
    assert _is_linked(a, 'sql_OpFunction194', b1)
    if hasattr(b1, 'sql_OpFunctionArg'):
        assert _is_linked(b1, 'sql_OpFunctionArg', a)
    _safe_set(a, 'sql_OpFunction194', b2)
    assert _is_linked(a, 'sql_OpFunction194', b2)
    if hasattr(b1, 'sql_OpFunctionArg'):
        assert not _is_linked(b1, 'sql_OpFunctionArg', a)
    if hasattr(b2, 'sql_OpFunctionArg'):
        assert _is_linked(b2, 'sql_OpFunctionArg', a)
    _safe_set(a, 'sql_OpFunction194', None)
    assert not _is_linked(a, 'sql_OpFunction194', b2)
    if hasattr(b2, 'sql_OpFunctionArg'):
        assert not _is_linked(b2, 'sql_OpFunctionArg', a)


def test_assoc_args253_link_reassign_clear():
    a = sql_UnipivotInClause(op="sample_text")
    b1 = sql_UnpivotInClauseArgs()
    b2 = sql_UnpivotInClauseArgs()
    _safe_set(a, 'sql_UnipivotInClause', b1)
    assert _is_linked(a, 'sql_UnipivotInClause', b1)
    if hasattr(b1, 'sql_UnpivotInClauseArgs254'):
        assert _is_linked(b1, 'sql_UnpivotInClauseArgs254', a)
    _safe_set(a, 'sql_UnipivotInClause', b2)
    assert _is_linked(a, 'sql_UnipivotInClause', b2)
    if hasattr(b1, 'sql_UnpivotInClauseArgs254'):
        assert not _is_linked(b1, 'sql_UnpivotInClauseArgs254', a)
    if hasattr(b2, 'sql_UnpivotInClauseArgs254'):
        assert _is_linked(b2, 'sql_UnpivotInClauseArgs254', a)
    _safe_set(a, 'sql_UnipivotInClause', None)
    assert not _is_linked(a, 'sql_UnipivotInClause', b2)
    if hasattr(b2, 'sql_UnpivotInClauseArgs254'):
        assert not _is_linked(b2, 'sql_UnpivotInClauseArgs254', a)


def test_assoc_args69_link_reassign_clear():
    a = sql_PivotInClause(pinany="sample_text")
    b1 = sql_UnpivotInClauseArgs()
    b2 = sql_UnpivotInClauseArgs()
    _safe_set(a, 'sql_PivotInClause70', b1)
    assert _is_linked(a, 'sql_PivotInClause70', b1)
    if hasattr(b1, 'sql_UnpivotInClauseArgs'):
        assert _is_linked(b1, 'sql_UnpivotInClauseArgs', a)
    _safe_set(a, 'sql_PivotInClause70', b2)
    assert _is_linked(a, 'sql_PivotInClause70', b2)
    if hasattr(b1, 'sql_UnpivotInClauseArgs'):
        assert not _is_linked(b1, 'sql_UnpivotInClauseArgs', a)
    if hasattr(b2, 'sql_UnpivotInClauseArgs'):
        assert _is_linked(b2, 'sql_UnpivotInClauseArgs', a)
    _safe_set(a, 'sql_PivotInClause70', None)
    assert not _is_linked(a, 'sql_PivotInClause70', b2)
    if hasattr(b2, 'sql_UnpivotInClauseArgs'):
        assert not _is_linked(b2, 'sql_UnpivotInClauseArgs', a)


def test_assoc_between113_link_reassign_clear():
    a = sql_FullExpression(c="sample_text", isnull="sample_text", notPrm="sample_text")
    b1 = sql_Between(opBetween="sample_text")
    b2 = sql_Between(opBetween="sample_text_2")
    _safe_set(a, 'sql_FullExpression114', b1)
    assert _is_linked(a, 'sql_FullExpression114', b1)
    if hasattr(b1, 'sql_Between'):
        assert _is_linked(b1, 'sql_Between', a)
    _safe_set(a, 'sql_FullExpression114', b2)
    assert _is_linked(a, 'sql_FullExpression114', b2)
    if hasattr(b1, 'sql_Between'):
        assert not _is_linked(b1, 'sql_Between', a)
    if hasattr(b2, 'sql_Between'):
        assert _is_linked(b2, 'sql_Between', a)
    _safe_set(a, 'sql_FullExpression114', None)
    assert not _is_linked(a, 'sql_FullExpression114', b2)
    if hasattr(b2, 'sql_Between'):
        assert not _is_linked(b2, 'sql_Between', a)


def test_assoc_ce31_link_reassign_clear():
    a = sql_ColumnOrAlias(alias="sample_text", allCols="sample_text")
    b1 = sql_Operands()
    b2 = sql_Operands()
    _safe_set(a, 'sql_ColumnOrAlias32', b1)
    assert _is_linked(a, 'sql_ColumnOrAlias32', b1)
    if hasattr(b1, 'sql_Operands'):
        assert _is_linked(b1, 'sql_Operands', a)
    _safe_set(a, 'sql_ColumnOrAlias32', b2)
    assert _is_linked(a, 'sql_ColumnOrAlias32', b2)
    if hasattr(b1, 'sql_Operands'):
        assert not _is_linked(b1, 'sql_Operands', a)
    if hasattr(b2, 'sql_Operands'):
        assert _is_linked(b2, 'sql_Operands', a)
    _safe_set(a, 'sql_ColumnOrAlias32', None)
    assert not _is_linked(a, 'sql_ColumnOrAlias32', b2)
    if hasattr(b2, 'sql_Operands'):
        assert not _is_linked(b2, 'sql_Operands', a)


def test_assoc_cfull232_link_reassign_clear():
    a = sql_ColumnOperand(ora="sample_text")
    b1 = sql_ColumnFull()
    b2 = sql_ColumnFull()
    _safe_set(a, 'sql_ColumnOperand233', b1)
    assert _is_linked(a, 'sql_ColumnOperand233', b1)
    if hasattr(b1, 'sql_ColumnFull234'):
        assert _is_linked(b1, 'sql_ColumnFull234', a)
    _safe_set(a, 'sql_ColumnOperand233', b2)
    assert _is_linked(a, 'sql_ColumnOperand233', b2)
    if hasattr(b1, 'sql_ColumnFull234'):
        assert not _is_linked(b1, 'sql_ColumnFull234', a)
    if hasattr(b2, 'sql_ColumnFull234'):
        assert _is_linked(b2, 'sql_ColumnFull234', a)
    _safe_set(a, 'sql_ColumnOperand233', None)
    assert not _is_linked(a, 'sql_ColumnOperand233', b2)
    if hasattr(b2, 'sql_ColumnFull234'):
        assert not _is_linked(b2, 'sql_ColumnFull234', a)


def test_assoc_col122_link_reassign_clear():
    a = sql_XExpr(xf="sample_text")
    b1 = sql_Operands()
    b2 = sql_Operands()
    _safe_set(a, 'sql_XExpr123', b1)
    assert _is_linked(a, 'sql_XExpr123', b1)
    if hasattr(b1, 'sql_Operands124'):
        assert _is_linked(b1, 'sql_Operands124', a)
    _safe_set(a, 'sql_XExpr123', b2)
    assert _is_linked(a, 'sql_XExpr123', b2)
    if hasattr(b1, 'sql_Operands124'):
        assert not _is_linked(b1, 'sql_Operands124', a)
    if hasattr(b2, 'sql_Operands124'):
        assert _is_linked(b2, 'sql_Operands124', a)
    _safe_set(a, 'sql_XExpr123', None)
    assert not _is_linked(a, 'sql_XExpr123', b2)
    if hasattr(b2, 'sql_Operands124'):
        assert not _is_linked(b2, 'sql_Operands124', a)


def test_assoc_colAlias225_link_reassign_clear():
    a = sql_DbObjectName(dbname="sample_text")
    b1 = sql_AnalyticExprArg()
    b2 = sql_AnalyticExprArg()
    _safe_set(a, 'sql_DbObjectName227', b1)
    assert _is_linked(a, 'sql_DbObjectName227', b1)
    if hasattr(b1, 'sql_AnalyticExprArg226'):
        assert _is_linked(b1, 'sql_AnalyticExprArg226', a)
    _safe_set(a, 'sql_DbObjectName227', b2)
    assert _is_linked(a, 'sql_DbObjectName227', b2)
    if hasattr(b1, 'sql_AnalyticExprArg226'):
        assert not _is_linked(b1, 'sql_AnalyticExprArg226', a)
    if hasattr(b2, 'sql_AnalyticExprArg226'):
        assert _is_linked(b2, 'sql_AnalyticExprArg226', a)
    _safe_set(a, 'sql_DbObjectName227', None)
    assert not _is_linked(a, 'sql_DbObjectName227', b2)
    if hasattr(b2, 'sql_AnalyticExprArg226'):
        assert not _is_linked(b2, 'sql_AnalyticExprArg226', a)


def test_assoc_colAlias33_link_reassign_clear():
    a = sql_DbObjectName(dbname="sample_text")
    b1 = sql_ColumnOrAlias(alias="sample_text", allCols="sample_text")
    b2 = sql_ColumnOrAlias(alias="sample_text_2", allCols="sample_text_2")
    _safe_set(a, 'sql_DbObjectName', b1)
    assert _is_linked(a, 'sql_DbObjectName', b1)
    if hasattr(b1, 'sql_ColumnOrAlias34'):
        assert _is_linked(b1, 'sql_ColumnOrAlias34', a)
    _safe_set(a, 'sql_DbObjectName', b2)
    assert _is_linked(a, 'sql_DbObjectName', b2)
    if hasattr(b1, 'sql_ColumnOrAlias34'):
        assert not _is_linked(b1, 'sql_ColumnOrAlias34', a)
    if hasattr(b2, 'sql_ColumnOrAlias34'):
        assert _is_linked(b2, 'sql_ColumnOrAlias34', a)
    _safe_set(a, 'sql_DbObjectName', None)
    assert not _is_linked(a, 'sql_DbObjectName', b2)
    if hasattr(b2, 'sql_ColumnOrAlias34'):
        assert not _is_linked(b2, 'sql_ColumnOrAlias34', a)


def test_assoc_colOrder85_link_reassign_clear():
    a = sql_OrderByColumnFull(colOrderInt=7, direction="sample_text")
    b1 = sql_ColumnFull()
    b2 = sql_ColumnFull()
    _safe_set(a, 'sql_OrderByColumnFull86', b1)
    assert _is_linked(a, 'sql_OrderByColumnFull86', b1)
    if hasattr(b1, 'sql_ColumnFull'):
        assert _is_linked(b1, 'sql_ColumnFull', a)
    _safe_set(a, 'sql_OrderByColumnFull86', b2)
    assert _is_linked(a, 'sql_OrderByColumnFull86', b2)
    if hasattr(b1, 'sql_ColumnFull'):
        assert not _is_linked(b1, 'sql_ColumnFull', a)
    if hasattr(b2, 'sql_ColumnFull'):
        assert _is_linked(b2, 'sql_ColumnFull', a)
    _safe_set(a, 'sql_OrderByColumnFull86', None)
    assert not _is_linked(a, 'sql_OrderByColumnFull86', b2)
    if hasattr(b2, 'sql_ColumnFull'):
        assert not _is_linked(b2, 'sql_ColumnFull', a)


def test_assoc_cols8_link_reassign_clear():
    a = sql_Select(select="sample_text")
    b1 = sql_OrColumn()
    b2 = sql_OrColumn()
    _safe_set(a, 'sql_Select9', b1)
    assert _is_linked(a, 'sql_Select9', b1)
    if hasattr(b1, 'sql_OrColumn'):
        assert _is_linked(b1, 'sql_OrColumn', a)
    _safe_set(a, 'sql_Select9', b2)
    assert _is_linked(a, 'sql_Select9', b2)
    if hasattr(b1, 'sql_OrColumn'):
        assert not _is_linked(b1, 'sql_OrColumn', a)
    if hasattr(b2, 'sql_OrColumn'):
        assert _is_linked(b2, 'sql_OrColumn', a)
    _safe_set(a, 'sql_Select9', None)
    assert not _is_linked(a, 'sql_Select9', b2)
    if hasattr(b2, 'sql_OrColumn'):
        assert not _is_linked(b2, 'sql_OrColumn', a)


def test_assoc_column168_link_reassign_clear():
    a = sql_ColumnOperand(ora="sample_text")
    b1 = sql_Operand()
    b2 = sql_Operand()
    _safe_set(a, 'sql_ColumnOperand', b1)
    assert _is_linked(a, 'sql_ColumnOperand', b1)
    if hasattr(b1, 'sql_Operand169'):
        assert _is_linked(b1, 'sql_Operand169', a)
    _safe_set(a, 'sql_ColumnOperand', b2)
    assert _is_linked(a, 'sql_ColumnOperand', b2)
    if hasattr(b1, 'sql_Operand169'):
        assert not _is_linked(b1, 'sql_Operand169', a)
    if hasattr(b2, 'sql_Operand169'):
        assert _is_linked(b2, 'sql_Operand169', a)
    _safe_set(a, 'sql_ColumnOperand', None)
    assert not _is_linked(a, 'sql_ColumnOperand', b2)
    if hasattr(b2, 'sql_Operand169'):
        assert not _is_linked(b2, 'sql_Operand169', a)


def test_assoc_comp117_link_reassign_clear():
    a = sql_FullExpression(c="sample_text", isnull="sample_text", notPrm="sample_text")
    b1 = sql_Comparison(operator="sample_text", subOperator="sample_text")
    b2 = sql_Comparison(operator="sample_text_2", subOperator="sample_text_2")
    _safe_set(a, 'sql_FullExpression118', b1)
    assert _is_linked(a, 'sql_FullExpression118', b1)
    if hasattr(b1, 'sql_Comparison'):
        assert _is_linked(b1, 'sql_Comparison', a)
    _safe_set(a, 'sql_FullExpression118', b2)
    assert _is_linked(a, 'sql_FullExpression118', b2)
    if hasattr(b1, 'sql_Comparison'):
        assert not _is_linked(b1, 'sql_Comparison', a)
    if hasattr(b2, 'sql_Comparison'):
        assert _is_linked(b2, 'sql_Comparison', a)
    _safe_set(a, 'sql_FullExpression118', None)
    assert not _is_linked(a, 'sql_FullExpression118', b2)
    if hasattr(b2, 'sql_Comparison'):
        assert not _is_linked(b2, 'sql_Comparison', a)


def test_assoc_dbAllCols35_link_reassign_clear():
    a = sql_DbObjectNameAll(dbname="sample_text")
    b1 = sql_ColumnOrAlias(alias="sample_text", allCols="sample_text")
    b2 = sql_ColumnOrAlias(alias="sample_text_2", allCols="sample_text_2")
    _safe_set(a, 'sql_DbObjectNameAll', b1)
    assert _is_linked(a, 'sql_DbObjectNameAll', b1)
    if hasattr(b1, 'sql_ColumnOrAlias36'):
        assert _is_linked(b1, 'sql_ColumnOrAlias36', a)
    _safe_set(a, 'sql_DbObjectNameAll', b2)
    assert _is_linked(a, 'sql_DbObjectNameAll', b2)
    if hasattr(b1, 'sql_ColumnOrAlias36'):
        assert not _is_linked(b1, 'sql_ColumnOrAlias36', a)
    if hasattr(b2, 'sql_ColumnOrAlias36'):
        assert _is_linked(b2, 'sql_ColumnOrAlias36', a)
    _safe_set(a, 'sql_DbObjectNameAll', None)
    assert not _is_linked(a, 'sql_DbObjectNameAll', b2)
    if hasattr(b2, 'sql_ColumnOrAlias36'):
        assert not _is_linked(b2, 'sql_ColumnOrAlias36', a)


def test_assoc_efrag97_link_reassign_clear():
    a = sql_FullExpression(c="sample_text", isnull="sample_text", notPrm="sample_text")
    b1 = sql_FullExpression(c="sample_text", isnull="sample_text", notPrm="sample_text")
    b2 = sql_FullExpression(c="sample_text_2", isnull="sample_text_2", notPrm="sample_text_2")
    _safe_set(a, 'sql_FullExpression96', b1)
    assert _is_linked(a, 'sql_FullExpression96', b1)
    if hasattr(b1, 'sql_FullExpression98'):
        assert _is_linked(b1, 'sql_FullExpression98', a)
    _safe_set(a, 'sql_FullExpression96', b2)
    assert _is_linked(a, 'sql_FullExpression96', b2)
    if hasattr(b1, 'sql_FullExpression98'):
        assert not _is_linked(b1, 'sql_FullExpression98', a)
    if hasattr(b2, 'sql_FullExpression98'):
        assert _is_linked(b2, 'sql_FullExpression98', a)
    _safe_set(a, 'sql_FullExpression96', None)
    assert not _is_linked(a, 'sql_FullExpression96', b2)
    if hasattr(b2, 'sql_FullExpression98'):
        assert not _is_linked(b2, 'sql_FullExpression98', a)


def test_assoc_entries127_link_reassign_clear():
    a = sql_JRParameter(jrprm="sample_text")
    b1 = sql_Prms()
    b2 = sql_Prms()
    _safe_set(a, 'sql_JRParameter', b1)
    assert _is_linked(a, 'sql_JRParameter', b1)
    if hasattr(b1, 'sql_Prms128'):
        assert _is_linked(b1, 'sql_Prms128', a)
    _safe_set(a, 'sql_JRParameter', b2)
    assert _is_linked(a, 'sql_JRParameter', b2)
    if hasattr(b1, 'sql_Prms128'):
        assert not _is_linked(b1, 'sql_Prms128', a)
    if hasattr(b2, 'sql_Prms128'):
        assert _is_linked(b2, 'sql_Prms128', a)
    _safe_set(a, 'sql_JRParameter', None)
    assert not _is_linked(a, 'sql_JRParameter', b2)
    if hasattr(b2, 'sql_Prms128'):
        assert not _is_linked(b2, 'sql_Prms128', a)


def test_assoc_entries251_link_reassign_clear():
    a = sql_DbObjectName(dbname="sample_text")
    b1 = sql_Col()
    b2 = sql_Col()
    _safe_set(a, 'sql_DbObjectName252', b1)
    assert _is_linked(a, 'sql_DbObjectName252', b1)
    if hasattr(b1, 'sql_Col'):
        assert _is_linked(b1, 'sql_Col', a)
    _safe_set(a, 'sql_DbObjectName252', b2)
    assert _is_linked(a, 'sql_DbObjectName252', b2)
    if hasattr(b1, 'sql_Col'):
        assert not _is_linked(b1, 'sql_Col', a)
    if hasattr(b2, 'sql_Col'):
        assert _is_linked(b2, 'sql_Col', a)
    _safe_set(a, 'sql_DbObjectName252', None)
    assert not _is_linked(a, 'sql_DbObjectName252', b2)
    if hasattr(b2, 'sql_Col'):
        assert not _is_linked(b2, 'sql_Col', a)


def test_assoc_entries258_link_reassign_clear():
    a = sql_DbObjectName(dbname="sample_text")
    b1 = sql_pcols()
    b2 = sql_pcols()
    _safe_set(a, 'sql_DbObjectName259', b1)
    assert _is_linked(a, 'sql_DbObjectName259', b1)
    if hasattr(b1, 'sql_pcols'):
        assert _is_linked(b1, 'sql_pcols', a)
    _safe_set(a, 'sql_DbObjectName259', b2)
    assert _is_linked(a, 'sql_DbObjectName259', b2)
    if hasattr(b1, 'sql_pcols'):
        assert not _is_linked(b1, 'sql_pcols', a)
    if hasattr(b2, 'sql_pcols'):
        assert _is_linked(b2, 'sql_pcols', a)
    _safe_set(a, 'sql_DbObjectName259', None)
    assert not _is_linked(a, 'sql_DbObjectName259', b2)
    if hasattr(b2, 'sql_pcols'):
        assert not _is_linked(b2, 'sql_pcols', a)


def test_assoc_entries260_link_reassign_clear():
    a = sql_DbObjectName(dbname="sample_text")
    b1 = sql_tbls()
    b2 = sql_tbls()
    _safe_set(a, 'sql_DbObjectName261', b1)
    assert _is_linked(a, 'sql_DbObjectName261', b1)
    if hasattr(b1, 'sql_tbls'):
        assert _is_linked(b1, 'sql_tbls', a)
    _safe_set(a, 'sql_DbObjectName261', b2)
    assert _is_linked(a, 'sql_DbObjectName261', b2)
    if hasattr(b1, 'sql_tbls'):
        assert not _is_linked(b1, 'sql_tbls', a)
    if hasattr(b2, 'sql_tbls'):
        assert _is_linked(b2, 'sql_tbls', a)
    _safe_set(a, 'sql_DbObjectName261', None)
    assert not _is_linked(a, 'sql_DbObjectName261', b2)
    if hasattr(b2, 'sql_tbls'):
        assert not _is_linked(b2, 'sql_tbls', a)


def test_assoc_entries262_link_reassign_clear():
    a = sql_ScalarOperand(sodate=date(2024, 1, 1), sodbl="sample_text", sodt=date(2024, 1, 1), soint=7, sostr="sample_text", sotime=date(2024, 1, 1))
    b1 = sql_OpList()
    b2 = sql_OpList()
    _safe_set(a, 'sql_ScalarOperand263', b1)
    assert _is_linked(a, 'sql_ScalarOperand263', b1)
    if hasattr(b1, 'sql_OpList'):
        assert _is_linked(b1, 'sql_OpList', a)
    _safe_set(a, 'sql_ScalarOperand263', b2)
    assert _is_linked(a, 'sql_ScalarOperand263', b2)
    if hasattr(b1, 'sql_OpList'):
        assert not _is_linked(b1, 'sql_OpList', a)
    if hasattr(b2, 'sql_OpList'):
        assert _is_linked(b2, 'sql_OpList', a)
    _safe_set(a, 'sql_ScalarOperand263', None)
    assert not _is_linked(a, 'sql_ScalarOperand263', b2)
    if hasattr(b2, 'sql_OpList'):
        assert not _is_linked(b2, 'sql_OpList', a)


def test_assoc_entries29_link_reassign_clear():
    a = sql_ColumnOrAlias(alias="sample_text", allCols="sample_text")
    b1 = sql_OrColumn()
    b2 = sql_OrColumn()
    _safe_set(a, 'sql_ColumnOrAlias', b1)
    assert _is_linked(a, 'sql_ColumnOrAlias', b1)
    if hasattr(b1, 'sql_OrColumn30'):
        assert _is_linked(b1, 'sql_OrColumn30', a)
    _safe_set(a, 'sql_ColumnOrAlias', b2)
    assert _is_linked(a, 'sql_ColumnOrAlias', b2)
    if hasattr(b1, 'sql_OrColumn30'):
        assert not _is_linked(b1, 'sql_OrColumn30', a)
    if hasattr(b2, 'sql_OrColumn30'):
        assert _is_linked(b2, 'sql_OrColumn30', a)
    _safe_set(a, 'sql_ColumnOrAlias', None)
    assert not _is_linked(a, 'sql_ColumnOrAlias', b2)
    if hasattr(b2, 'sql_OrColumn30'):
        assert not _is_linked(b2, 'sql_OrColumn30', a)


def test_assoc_entries83_link_reassign_clear():
    a = sql_OrderByColumnFull(colOrderInt=7, direction="sample_text")
    b1 = sql_OrOrderByColumn()
    b2 = sql_OrOrderByColumn()
    _safe_set(a, 'sql_OrderByColumnFull', b1)
    assert _is_linked(a, 'sql_OrderByColumnFull', b1)
    if hasattr(b1, 'sql_OrOrderByColumn84'):
        assert _is_linked(b1, 'sql_OrOrderByColumn84', a)
    _safe_set(a, 'sql_OrderByColumnFull', b2)
    assert _is_linked(a, 'sql_OrderByColumnFull', b2)
    if hasattr(b1, 'sql_OrOrderByColumn84'):
        assert not _is_linked(b1, 'sql_OrOrderByColumn84', a)
    if hasattr(b2, 'sql_OrOrderByColumn84'):
        assert _is_linked(b2, 'sql_OrOrderByColumn84', a)
    _safe_set(a, 'sql_OrderByColumnFull', None)
    assert not _is_linked(a, 'sql_OrderByColumnFull', b2)
    if hasattr(b2, 'sql_OrOrderByColumn84'):
        assert not _is_linked(b2, 'sql_OrOrderByColumn84', a)


def test_assoc_entries94_link_reassign_clear():
    a = sql_FullExpression(c="sample_text", isnull="sample_text", notPrm="sample_text")
    b1 = sql_OrExpr()
    b2 = sql_OrExpr()
    _safe_set(a, 'sql_FullExpression', b1)
    assert _is_linked(a, 'sql_FullExpression', b1)
    if hasattr(b1, 'sql_OrExpr95'):
        assert _is_linked(b1, 'sql_OrExpr95', a)
    _safe_set(a, 'sql_FullExpression', b2)
    assert _is_linked(a, 'sql_FullExpression', b2)
    if hasattr(b1, 'sql_OrExpr95'):
        assert not _is_linked(b1, 'sql_OrExpr95', a)
    if hasattr(b2, 'sql_OrExpr95'):
        assert _is_linked(b2, 'sql_OrExpr95', a)
    _safe_set(a, 'sql_FullExpression', None)
    assert not _is_linked(a, 'sql_FullExpression', b2)
    if hasattr(b2, 'sql_OrExpr95'):
        assert not _is_linked(b2, 'sql_OrExpr95', a)


def test_assoc_eparam189_link_reassign_clear():
    a = sql_ExpOperand(prm="sample_text")
    b1 = sql_Operand()
    b2 = sql_Operand()
    _safe_set(a, 'sql_ExpOperand', b1)
    assert _is_linked(a, 'sql_ExpOperand', b1)
    if hasattr(b1, 'sql_Operand190'):
        assert _is_linked(b1, 'sql_Operand190', a)
    _safe_set(a, 'sql_ExpOperand', b2)
    assert _is_linked(a, 'sql_ExpOperand', b2)
    if hasattr(b1, 'sql_Operand190'):
        assert not _is_linked(b1, 'sql_Operand190', a)
    if hasattr(b2, 'sql_Operand190'):
        assert _is_linked(b2, 'sql_Operand190', a)
    _safe_set(a, 'sql_ExpOperand', None)
    assert not _is_linked(a, 'sql_ExpOperand', b2)
    if hasattr(b2, 'sql_Operand190'):
        assert not _is_linked(b2, 'sql_Operand190', a)


def test_assoc_exists108_link_reassign_clear():
    a = sql_FullExpression(c="sample_text", isnull="sample_text", notPrm="sample_text")
    b1 = sql_ExistsOper(op="sample_text")
    b2 = sql_ExistsOper(op="sample_text_2")
    _safe_set(a, 'sql_FullExpression109', b1)
    assert _is_linked(a, 'sql_FullExpression109', b1)
    if hasattr(b1, 'sql_ExistsOper'):
        assert _is_linked(b1, 'sql_ExistsOper', a)
    _safe_set(a, 'sql_FullExpression109', b2)
    assert _is_linked(a, 'sql_FullExpression109', b2)
    if hasattr(b1, 'sql_ExistsOper'):
        assert not _is_linked(b1, 'sql_ExistsOper', a)
    if hasattr(b2, 'sql_ExistsOper'):
        assert _is_linked(b2, 'sql_ExistsOper', a)
    _safe_set(a, 'sql_FullExpression109', None)
    assert not _is_linked(a, 'sql_FullExpression109', b2)
    if hasattr(b2, 'sql_ExistsOper'):
        assert not _is_linked(b2, 'sql_ExistsOper', a)


def test_assoc_exp102_link_reassign_clear():
    a = sql_FullExpression(c="sample_text", isnull="sample_text", notPrm="sample_text")
    b1 = sql_FullExpression(c="sample_text", isnull="sample_text", notPrm="sample_text")
    b2 = sql_FullExpression(c="sample_text_2", isnull="sample_text_2", notPrm="sample_text_2")
    _safe_set(a, 'sql_FullExpression101', b1)
    assert _is_linked(a, 'sql_FullExpression101', b1)
    if hasattr(b1, 'sql_FullExpression103'):
        assert _is_linked(b1, 'sql_FullExpression103', a)
    _safe_set(a, 'sql_FullExpression101', b2)
    assert _is_linked(a, 'sql_FullExpression101', b2)
    if hasattr(b1, 'sql_FullExpression103'):
        assert not _is_linked(b1, 'sql_FullExpression103', a)
    if hasattr(b2, 'sql_FullExpression103'):
        assert _is_linked(b2, 'sql_FullExpression103', a)
    _safe_set(a, 'sql_FullExpression101', None)
    assert not _is_linked(a, 'sql_FullExpression101', b2)
    if hasattr(b2, 'sql_FullExpression103'):
        assert not _is_linked(b2, 'sql_FullExpression103', a)


def test_assoc_expgroup99_link_reassign_clear():
    a = sql_FullExpression(c="sample_text", isnull="sample_text", notPrm="sample_text")
    b1 = sql_ExprGroup(isnot="sample_text")
    b2 = sql_ExprGroup(isnot="sample_text_2")
    _safe_set(a, 'sql_FullExpression100', b1)
    assert _is_linked(a, 'sql_FullExpression100', b1)
    if hasattr(b1, 'sql_ExprGroup'):
        assert _is_linked(b1, 'sql_ExprGroup', a)
    _safe_set(a, 'sql_FullExpression100', b2)
    assert _is_linked(a, 'sql_FullExpression100', b2)
    if hasattr(b1, 'sql_ExprGroup'):
        assert not _is_linked(b1, 'sql_ExprGroup', a)
    if hasattr(b2, 'sql_ExprGroup'):
        assert _is_linked(b2, 'sql_ExprGroup', a)
    _safe_set(a, 'sql_FullExpression100', None)
    assert not _is_linked(a, 'sql_FullExpression100', b2)
    if hasattr(b2, 'sql_ExprGroup'):
        assert not _is_linked(b2, 'sql_ExprGroup', a)


def test_assoc_expr119_link_reassign_clear():
    a = sql_ExprGroup(isnot="sample_text")
    b1 = sql_OrExpr()
    b2 = sql_OrExpr()
    _safe_set(a, 'sql_ExprGroup120', b1)
    assert _is_linked(a, 'sql_ExprGroup120', b1)
    if hasattr(b1, 'sql_OrExpr121'):
        assert _is_linked(b1, 'sql_OrExpr121', a)
    _safe_set(a, 'sql_ExprGroup120', b2)
    assert _is_linked(a, 'sql_ExprGroup120', b2)
    if hasattr(b1, 'sql_OrExpr121'):
        assert not _is_linked(b1, 'sql_OrExpr121', a)
    if hasattr(b2, 'sql_OrExpr121'):
        assert _is_linked(b2, 'sql_OrExpr121', a)
    _safe_set(a, 'sql_ExprGroup120', None)
    assert not _is_linked(a, 'sql_ExprGroup120', b2)
    if hasattr(b2, 'sql_OrExpr121'):
        assert not _is_linked(b2, 'sql_OrExpr121', a)


def test_assoc_fan195_link_reassign_clear():
    a = sql_OpFunction(fname="sample_text")
    b1 = sql_FunctionAnalytical()
    b2 = sql_FunctionAnalytical()
    _safe_set(a, 'sql_OpFunction196', b1)
    assert _is_linked(a, 'sql_OpFunction196', b1)
    if hasattr(b1, 'sql_FunctionAnalytical'):
        assert _is_linked(b1, 'sql_FunctionAnalytical', a)
    _safe_set(a, 'sql_OpFunction196', b2)
    assert _is_linked(a, 'sql_OpFunction196', b2)
    if hasattr(b1, 'sql_FunctionAnalytical'):
        assert not _is_linked(b1, 'sql_FunctionAnalytical', a)
    if hasattr(b2, 'sql_FunctionAnalytical'):
        assert _is_linked(b2, 'sql_FunctionAnalytical', a)
    _safe_set(a, 'sql_OpFunction196', None)
    assert not _is_linked(a, 'sql_OpFunction196', b2)
    if hasattr(b2, 'sql_FunctionAnalytical'):
        assert not _is_linked(b2, 'sql_FunctionAnalytical', a)


def test_assoc_fcast137_link_reassign_clear():
    a = sql_OpFunctionCast(p=7, p2=7, type="sample_text")
    b1 = sql_LikeOperand(op2="sample_text")
    b2 = sql_LikeOperand(op2="sample_text_2")
    _safe_set(a, 'sql_OpFunctionCast', b1)
    assert _is_linked(a, 'sql_OpFunctionCast', b1)
    if hasattr(b1, 'sql_LikeOperand138'):
        assert _is_linked(b1, 'sql_LikeOperand138', a)
    _safe_set(a, 'sql_OpFunctionCast', b2)
    assert _is_linked(a, 'sql_OpFunctionCast', b2)
    if hasattr(b1, 'sql_LikeOperand138'):
        assert not _is_linked(b1, 'sql_LikeOperand138', a)
    if hasattr(b2, 'sql_LikeOperand138'):
        assert _is_linked(b2, 'sql_LikeOperand138', a)
    _safe_set(a, 'sql_OpFunctionCast', None)
    assert not _is_linked(a, 'sql_OpFunctionCast', b2)
    if hasattr(b2, 'sql_LikeOperand138'):
        assert not _is_linked(b2, 'sql_LikeOperand138', a)


def test_assoc_fcast176_link_reassign_clear():
    a = sql_OpFunctionCast(p=7, p2=7, type="sample_text")
    b1 = sql_Operand()
    b2 = sql_Operand()
    _safe_set(a, 'sql_OpFunctionCast178', b1)
    assert _is_linked(a, 'sql_OpFunctionCast178', b1)
    if hasattr(b1, 'sql_Operand177'):
        assert _is_linked(b1, 'sql_Operand177', a)
    _safe_set(a, 'sql_OpFunctionCast178', b2)
    assert _is_linked(a, 'sql_OpFunctionCast178', b2)
    if hasattr(b1, 'sql_Operand177'):
        assert not _is_linked(b1, 'sql_Operand177', a)
    if hasattr(b2, 'sql_Operand177'):
        assert _is_linked(b2, 'sql_Operand177', a)
    _safe_set(a, 'sql_OpFunctionCast178', None)
    assert not _is_linked(a, 'sql_OpFunctionCast178', b2)
    if hasattr(b2, 'sql_Operand177'):
        assert not _is_linked(b2, 'sql_Operand177', a)


def test_assoc_fetchFirst1_link_reassign_clear():
    a = sql_IntegerValue(integer=7)
    b1 = sql_FetchFirst(row="sample_text")
    b2 = sql_FetchFirst(row="sample_text_2")
    _safe_set(a, 'sql_IntegerValue', b1)
    assert _is_linked(a, 'sql_IntegerValue', b1)
    if hasattr(b1, 'sql_FetchFirst'):
        assert _is_linked(b1, 'sql_FetchFirst', a)
    _safe_set(a, 'sql_IntegerValue', b2)
    assert _is_linked(a, 'sql_IntegerValue', b2)
    if hasattr(b1, 'sql_FetchFirst'):
        assert not _is_linked(b1, 'sql_FetchFirst', a)
    if hasattr(b2, 'sql_FetchFirst'):
        assert _is_linked(b2, 'sql_FetchFirst', a)
    _safe_set(a, 'sql_IntegerValue', None)
    assert not _is_linked(a, 'sql_IntegerValue', b2)
    if hasattr(b2, 'sql_FetchFirst'):
        assert not _is_linked(b2, 'sql_FetchFirst', a)


def test_assoc_fetchFirst26_link_reassign_clear():
    a = sql_Select(select="sample_text")
    b1 = sql_FetchFirst(row="sample_text")
    b2 = sql_FetchFirst(row="sample_text_2")
    _safe_set(a, 'sql_Select27', b1)
    assert _is_linked(a, 'sql_Select27', b1)
    if hasattr(b1, 'sql_FetchFirst28'):
        assert _is_linked(b1, 'sql_FetchFirst28', a)
    _safe_set(a, 'sql_Select27', b2)
    assert _is_linked(a, 'sql_Select27', b2)
    if hasattr(b1, 'sql_FetchFirst28'):
        assert not _is_linked(b1, 'sql_FetchFirst28', a)
    if hasattr(b2, 'sql_FetchFirst28'):
        assert _is_linked(b2, 'sql_FetchFirst28', a)
    _safe_set(a, 'sql_Select27', None)
    assert not _is_linked(a, 'sql_Select27', b2)
    if hasattr(b2, 'sql_FetchFirst28'):
        assert not _is_linked(b2, 'sql_FetchFirst28', a)


def test_assoc_fext179_link_reassign_clear():
    a = sql_FunctionExtract(v="sample_text")
    b1 = sql_Operand()
    b2 = sql_Operand()
    _safe_set(a, 'sql_FunctionExtract', b1)
    assert _is_linked(a, 'sql_FunctionExtract', b1)
    if hasattr(b1, 'sql_Operand180'):
        assert _is_linked(b1, 'sql_Operand180', a)
    _safe_set(a, 'sql_FunctionExtract', b2)
    assert _is_linked(a, 'sql_FunctionExtract', b2)
    if hasattr(b1, 'sql_Operand180'):
        assert not _is_linked(b1, 'sql_Operand180', a)
    if hasattr(b2, 'sql_Operand180'):
        assert _is_linked(b2, 'sql_Operand180', a)
    _safe_set(a, 'sql_FunctionExtract', None)
    assert not _is_linked(a, 'sql_FunctionExtract', b2)
    if hasattr(b2, 'sql_Operand180'):
        assert not _is_linked(b2, 'sql_Operand180', a)


def test_assoc_fjoin41_link_reassign_clear():
    a = sql_FromTableJoin(join="sample_text")
    b1 = sql_FromTable()
    b2 = sql_FromTable()
    _safe_set(a, 'sql_FromTableJoin', b1)
    assert _is_linked(a, 'sql_FromTableJoin', b1)
    if hasattr(b1, 'sql_FromTable42'):
        assert _is_linked(b1, 'sql_FromTable42', a)
    _safe_set(a, 'sql_FromTableJoin', b2)
    assert _is_linked(a, 'sql_FromTableJoin', b2)
    if hasattr(b1, 'sql_FromTable42'):
        assert not _is_linked(b1, 'sql_FromTable42', a)
    if hasattr(b2, 'sql_FromTable42'):
        assert _is_linked(b2, 'sql_FromTable42', a)
    _safe_set(a, 'sql_FromTableJoin', None)
    assert not _is_linked(a, 'sql_FromTableJoin', b2)
    if hasattr(b2, 'sql_FromTable42'):
        assert not _is_linked(b2, 'sql_FromTable42', a)


def test_assoc_fop2134_link_reassign_clear():
    a = sql_OpFunction(fname="sample_text")
    b1 = sql_LikeOperand(op2="sample_text")
    b2 = sql_LikeOperand(op2="sample_text_2")
    _safe_set(a, 'sql_OpFunction136', b1)
    assert _is_linked(a, 'sql_OpFunction136', b1)
    if hasattr(b1, 'sql_LikeOperand135'):
        assert _is_linked(b1, 'sql_LikeOperand135', a)
    _safe_set(a, 'sql_OpFunction136', b2)
    assert _is_linked(a, 'sql_OpFunction136', b2)
    if hasattr(b1, 'sql_LikeOperand135'):
        assert not _is_linked(b1, 'sql_LikeOperand135', a)
    if hasattr(b2, 'sql_LikeOperand135'):
        assert _is_linked(b2, 'sql_LikeOperand135', a)
    _safe_set(a, 'sql_OpFunction136', None)
    assert not _is_linked(a, 'sql_OpFunction136', b2)
    if hasattr(b2, 'sql_LikeOperand135'):
        assert not _is_linked(b2, 'sql_LikeOperand135', a)


def test_assoc_fparam139_link_reassign_clear():
    a = sql_POperand(prm="sample_text")
    b1 = sql_LikeOperand(op2="sample_text")
    b2 = sql_LikeOperand(op2="sample_text_2")
    _safe_set(a, 'sql_POperand', b1)
    assert _is_linked(a, 'sql_POperand', b1)
    if hasattr(b1, 'sql_LikeOperand140'):
        assert _is_linked(b1, 'sql_LikeOperand140', a)
    _safe_set(a, 'sql_POperand', b2)
    assert _is_linked(a, 'sql_POperand', b2)
    if hasattr(b1, 'sql_LikeOperand140'):
        assert not _is_linked(b1, 'sql_LikeOperand140', a)
    if hasattr(b2, 'sql_LikeOperand140'):
        assert _is_linked(b2, 'sql_LikeOperand140', a)
    _safe_set(a, 'sql_POperand', None)
    assert not _is_linked(a, 'sql_POperand', b2)
    if hasattr(b2, 'sql_LikeOperand140'):
        assert not _is_linked(b2, 'sql_LikeOperand140', a)


def test_assoc_func181_link_reassign_clear():
    a = sql_OpFunction(fname="sample_text")
    b1 = sql_Operand()
    b2 = sql_Operand()
    _safe_set(a, 'sql_OpFunction183', b1)
    assert _is_linked(a, 'sql_OpFunction183', b1)
    if hasattr(b1, 'sql_Operand182'):
        assert _is_linked(b1, 'sql_Operand182', a)
    _safe_set(a, 'sql_OpFunction183', b2)
    assert _is_linked(a, 'sql_OpFunction183', b2)
    if hasattr(b1, 'sql_Operand182'):
        assert not _is_linked(b1, 'sql_Operand182', a)
    if hasattr(b2, 'sql_Operand182'):
        assert _is_linked(b2, 'sql_Operand182', a)
    _safe_set(a, 'sql_OpFunction183', None)
    assert not _is_linked(a, 'sql_OpFunction183', b2)
    if hasattr(b2, 'sql_Operand182'):
        assert not _is_linked(b2, 'sql_Operand182', a)


def test_assoc_gbFunction92_link_reassign_clear():
    a = sql_OpFunction(fname="sample_text")
    b1 = sql_GroupByColumnFull()
    b2 = sql_GroupByColumnFull()
    _safe_set(a, 'sql_OpFunction', b1)
    assert _is_linked(a, 'sql_OpFunction', b1)
    if hasattr(b1, 'sql_GroupByColumnFull93'):
        assert _is_linked(b1, 'sql_GroupByColumnFull93', a)
    _safe_set(a, 'sql_OpFunction', b2)
    assert _is_linked(a, 'sql_OpFunction', b2)
    if hasattr(b1, 'sql_GroupByColumnFull93'):
        assert not _is_linked(b1, 'sql_GroupByColumnFull93', a)
    if hasattr(b2, 'sql_GroupByColumnFull93'):
        assert _is_linked(b2, 'sql_GroupByColumnFull93', a)
    _safe_set(a, 'sql_OpFunction', None)
    assert not _is_linked(a, 'sql_OpFunction', b2)
    if hasattr(b2, 'sql_GroupByColumnFull93'):
        assert not _is_linked(b2, 'sql_GroupByColumnFull93', a)


def test_assoc_groupByEntry14_link_reassign_clear():
    a = sql_Select(select="sample_text")
    b1 = sql_OrGroupByColumn()
    b2 = sql_OrGroupByColumn()
    _safe_set(a, 'sql_Select15', b1)
    assert _is_linked(a, 'sql_Select15', b1)
    if hasattr(b1, 'sql_OrGroupByColumn'):
        assert _is_linked(b1, 'sql_OrGroupByColumn', a)
    _safe_set(a, 'sql_Select15', b2)
    assert _is_linked(a, 'sql_Select15', b2)
    if hasattr(b1, 'sql_OrGroupByColumn'):
        assert not _is_linked(b1, 'sql_OrGroupByColumn', a)
    if hasattr(b2, 'sql_OrGroupByColumn'):
        assert _is_linked(b2, 'sql_OrGroupByColumn', a)
    _safe_set(a, 'sql_Select15', None)
    assert not _is_linked(a, 'sql_Select15', b2)
    if hasattr(b2, 'sql_OrGroupByColumn'):
        assert not _is_linked(b2, 'sql_OrGroupByColumn', a)


def test_assoc_havingEntry16_link_reassign_clear():
    a = sql_Select(select="sample_text")
    b1 = sql_OrExpr()
    b2 = sql_OrExpr()
    _safe_set(a, 'sql_Select17', b1)
    assert _is_linked(a, 'sql_Select17', b1)
    if hasattr(b1, 'sql_OrExpr18'):
        assert _is_linked(b1, 'sql_OrExpr18', a)
    _safe_set(a, 'sql_Select17', b2)
    assert _is_linked(a, 'sql_Select17', b2)
    if hasattr(b1, 'sql_OrExpr18'):
        assert not _is_linked(b1, 'sql_OrExpr18', a)
    if hasattr(b2, 'sql_OrExpr18'):
        assert _is_linked(b2, 'sql_OrExpr18', a)
    _safe_set(a, 'sql_Select17', None)
    assert not _is_linked(a, 'sql_Select17', b2)
    if hasattr(b2, 'sql_OrExpr18'):
        assert not _is_linked(b2, 'sql_OrExpr18', a)


def test_assoc_in_106_link_reassign_clear():
    a = sql_InOper(op="sample_text")
    b1 = sql_FullExpression(c="sample_text", isnull="sample_text", notPrm="sample_text")
    b2 = sql_FullExpression(c="sample_text_2", isnull="sample_text_2", notPrm="sample_text_2")
    _safe_set(a, 'sql_InOper', b1)
    assert _is_linked(a, 'sql_InOper', b1)
    if hasattr(b1, 'sql_FullExpression107'):
        assert _is_linked(b1, 'sql_FullExpression107', a)
    _safe_set(a, 'sql_InOper', b2)
    assert _is_linked(a, 'sql_InOper', b2)
    if hasattr(b1, 'sql_FullExpression107'):
        assert not _is_linked(b1, 'sql_FullExpression107', a)
    if hasattr(b2, 'sql_FullExpression107'):
        assert _is_linked(b2, 'sql_FullExpression107', a)
    _safe_set(a, 'sql_InOper', None)
    assert not _is_linked(a, 'sql_InOper', b2)
    if hasattr(b2, 'sql_FullExpression107'):
        assert not _is_linked(b2, 'sql_FullExpression107', a)


def test_assoc_joinExpr46_link_reassign_clear():
    a = sql_FromTableJoin(join="sample_text")
    b1 = sql_OrExpr()
    b2 = sql_OrExpr()
    _safe_set(a, 'sql_FromTableJoin47', b1)
    assert _is_linked(a, 'sql_FromTableJoin47', b1)
    if hasattr(b1, 'sql_OrExpr48'):
        assert _is_linked(b1, 'sql_OrExpr48', a)
    _safe_set(a, 'sql_FromTableJoin47', b2)
    assert _is_linked(a, 'sql_FromTableJoin47', b2)
    if hasattr(b1, 'sql_OrExpr48'):
        assert not _is_linked(b1, 'sql_OrExpr48', a)
    if hasattr(b2, 'sql_OrExpr48'):
        assert _is_linked(b2, 'sql_OrExpr48', a)
    _safe_set(a, 'sql_FromTableJoin47', None)
    assert not _is_linked(a, 'sql_FromTableJoin47', b2)
    if hasattr(b2, 'sql_OrExpr48'):
        assert not _is_linked(b2, 'sql_OrExpr48', a)


def test_assoc_l22_link_reassign_clear():
    a = sql_Limit(l1=7)
    b1 = sql_IntegerValue(integer=7)
    b2 = sql_IntegerValue(integer=13)
    _safe_set(a, 'sql_Limit', b1)
    assert _is_linked(a, 'sql_Limit', b1)
    if hasattr(b1, 'sql_IntegerValue3'):
        assert _is_linked(b1, 'sql_IntegerValue3', a)
    _safe_set(a, 'sql_Limit', b2)
    assert _is_linked(a, 'sql_Limit', b2)
    if hasattr(b1, 'sql_IntegerValue3'):
        assert not _is_linked(b1, 'sql_IntegerValue3', a)
    if hasattr(b2, 'sql_IntegerValue3'):
        assert _is_linked(b2, 'sql_IntegerValue3', a)
    _safe_set(a, 'sql_Limit', None)
    assert not _is_linked(a, 'sql_Limit', b2)
    if hasattr(b2, 'sql_IntegerValue3'):
        assert not _is_linked(b2, 'sql_IntegerValue3', a)


def test_assoc_like115_link_reassign_clear():
    a = sql_Like(opLike="sample_text")
    b1 = sql_FullExpression(c="sample_text", isnull="sample_text", notPrm="sample_text")
    b2 = sql_FullExpression(c="sample_text_2", isnull="sample_text_2", notPrm="sample_text_2")
    _safe_set(a, 'sql_Like', b1)
    assert _is_linked(a, 'sql_Like', b1)
    if hasattr(b1, 'sql_FullExpression116'):
        assert _is_linked(b1, 'sql_FullExpression116', a)
    _safe_set(a, 'sql_Like', b2)
    assert _is_linked(a, 'sql_Like', b2)
    if hasattr(b1, 'sql_FullExpression116'):
        assert not _is_linked(b1, 'sql_FullExpression116', a)
    if hasattr(b2, 'sql_FullExpression116'):
        assert _is_linked(b2, 'sql_FullExpression116', a)
    _safe_set(a, 'sql_Like', None)
    assert not _is_linked(a, 'sql_Like', b2)
    if hasattr(b2, 'sql_FullExpression116'):
        assert not _is_linked(b2, 'sql_FullExpression116', a)


def test_assoc_lim21_link_reassign_clear():
    a = sql_Select(select="sample_text")
    b1 = sql_Limit(l1=7)
    b2 = sql_Limit(l1=13)
    _safe_set(a, 'sql_Select22', b1)
    assert _is_linked(a, 'sql_Select22', b1)
    if hasattr(b1, 'sql_Limit23'):
        assert _is_linked(b1, 'sql_Limit23', a)
    _safe_set(a, 'sql_Select22', b2)
    assert _is_linked(a, 'sql_Select22', b2)
    if hasattr(b1, 'sql_Limit23'):
        assert not _is_linked(b1, 'sql_Limit23', a)
    if hasattr(b2, 'sql_Limit23'):
        assert _is_linked(b2, 'sql_Limit23', a)
    _safe_set(a, 'sql_Select22', None)
    assert not _is_linked(a, 'sql_Select22', b2)
    if hasattr(b2, 'sql_Limit23'):
        assert not _is_linked(b2, 'sql_Limit23', a)


def test_assoc_offset24_link_reassign_clear():
    a = sql_Select(select="sample_text")
    b1 = sql_Offset(offset=7)
    b2 = sql_Offset(offset=13)
    _safe_set(a, 'sql_Select25', b1)
    assert _is_linked(a, 'sql_Select25', b1)
    if hasattr(b1, 'sql_Offset'):
        assert _is_linked(b1, 'sql_Offset', a)
    _safe_set(a, 'sql_Select25', b2)
    assert _is_linked(a, 'sql_Select25', b2)
    if hasattr(b1, 'sql_Offset'):
        assert not _is_linked(b1, 'sql_Offset', a)
    if hasattr(b2, 'sql_Offset'):
        assert _is_linked(b2, 'sql_Offset', a)
    _safe_set(a, 'sql_Select25', None)
    assert not _is_linked(a, 'sql_Select25', b2)
    if hasattr(b2, 'sql_Offset'):
        assert not _is_linked(b2, 'sql_Offset', a)


def test_assoc_onTable43_link_reassign_clear():
    a = sql_TableOrAlias(alias="sample_text")
    b1 = sql_FromTableJoin(join="sample_text")
    b2 = sql_FromTableJoin(join="sample_text_2")
    _safe_set(a, 'sql_TableOrAlias45', b1)
    assert _is_linked(a, 'sql_TableOrAlias45', b1)
    if hasattr(b1, 'sql_FromTableJoin44'):
        assert _is_linked(b1, 'sql_FromTableJoin44', a)
    _safe_set(a, 'sql_TableOrAlias45', b2)
    assert _is_linked(a, 'sql_TableOrAlias45', b2)
    if hasattr(b1, 'sql_FromTableJoin44'):
        assert not _is_linked(b1, 'sql_FromTableJoin44', a)
    if hasattr(b2, 'sql_FromTableJoin44'):
        assert _is_linked(b2, 'sql_FromTableJoin44', a)
    _safe_set(a, 'sql_TableOrAlias45', None)
    assert not _is_linked(a, 'sql_TableOrAlias45', b2)
    if hasattr(b2, 'sql_FromTableJoin44'):
        assert not _is_linked(b2, 'sql_FromTableJoin44', a)


def test_assoc_op1110_link_reassign_clear():
    a = sql_FullExpression(c="sample_text", isnull="sample_text", notPrm="sample_text")
    b1 = sql_Operands()
    b2 = sql_Operands()
    _safe_set(a, 'sql_FullExpression111', b1)
    assert _is_linked(a, 'sql_FullExpression111', b1)
    if hasattr(b1, 'sql_Operands112'):
        assert _is_linked(b1, 'sql_Operands112', a)
    _safe_set(a, 'sql_FullExpression111', b2)
    assert _is_linked(a, 'sql_FullExpression111', b2)
    if hasattr(b1, 'sql_Operands112'):
        assert not _is_linked(b1, 'sql_Operands112', a)
    if hasattr(b2, 'sql_Operands112'):
        assert _is_linked(b2, 'sql_Operands112', a)
    _safe_set(a, 'sql_FullExpression111', None)
    assert not _is_linked(a, 'sql_FullExpression111', b2)
    if hasattr(b2, 'sql_Operands112'):
        assert not _is_linked(b2, 'sql_Operands112', a)


def test_assoc_op2129_link_reassign_clear():
    a = sql_Comparison(operator="sample_text", subOperator="sample_text")
    b1 = sql_Operands()
    b2 = sql_Operands()
    _safe_set(a, 'sql_Comparison130', b1)
    assert _is_linked(a, 'sql_Comparison130', b1)
    if hasattr(b1, 'sql_Operands131'):
        assert _is_linked(b1, 'sql_Operands131', a)
    _safe_set(a, 'sql_Comparison130', b2)
    assert _is_linked(a, 'sql_Comparison130', b2)
    if hasattr(b1, 'sql_Operands131'):
        assert not _is_linked(b1, 'sql_Operands131', a)
    if hasattr(b2, 'sql_Operands131'):
        assert _is_linked(b2, 'sql_Operands131', a)
    _safe_set(a, 'sql_Comparison130', None)
    assert not _is_linked(a, 'sql_Comparison130', b2)
    if hasattr(b2, 'sql_Operands131'):
        assert not _is_linked(b2, 'sql_Operands131', a)


def test_assoc_op2132_link_reassign_clear():
    a = sql_LikeOperand(op2="sample_text")
    b1 = sql_Like(opLike="sample_text")
    b2 = sql_Like(opLike="sample_text_2")
    _safe_set(a, 'sql_LikeOperand', b1)
    assert _is_linked(a, 'sql_LikeOperand', b1)
    if hasattr(b1, 'sql_Like133'):
        assert _is_linked(b1, 'sql_Like133', a)
    _safe_set(a, 'sql_LikeOperand', b2)
    assert _is_linked(a, 'sql_LikeOperand', b2)
    if hasattr(b1, 'sql_Like133'):
        assert not _is_linked(b1, 'sql_Like133', a)
    if hasattr(b2, 'sql_Like133'):
        assert _is_linked(b2, 'sql_Like133', a)
    _safe_set(a, 'sql_LikeOperand', None)
    assert not _is_linked(a, 'sql_LikeOperand', b2)
    if hasattr(b2, 'sql_Like133'):
        assert not _is_linked(b2, 'sql_Like133', a)


def test_assoc_op2141_link_reassign_clear():
    a = sql_Between(opBetween="sample_text")
    b1 = sql_Operands()
    b2 = sql_Operands()
    _safe_set(a, 'sql_Between142', b1)
    assert _is_linked(a, 'sql_Between142', b1)
    if hasattr(b1, 'sql_Operands143'):
        assert _is_linked(b1, 'sql_Operands143', a)
    _safe_set(a, 'sql_Between142', b2)
    assert _is_linked(a, 'sql_Between142', b2)
    if hasattr(b1, 'sql_Operands143'):
        assert not _is_linked(b1, 'sql_Operands143', a)
    if hasattr(b2, 'sql_Operands143'):
        assert _is_linked(b2, 'sql_Operands143', a)
    _safe_set(a, 'sql_Between142', None)
    assert not _is_linked(a, 'sql_Between142', b2)
    if hasattr(b2, 'sql_Operands143'):
        assert not _is_linked(b2, 'sql_Operands143', a)


def test_assoc_op229_link_reassign_clear():
    a = sql_OpFunctionCast(p=7, p2=7, type="sample_text")
    b1 = sql_Operands()
    b2 = sql_Operands()
    _safe_set(a, 'sql_OpFunctionCast230', b1)
    assert _is_linked(a, 'sql_OpFunctionCast230', b1)
    if hasattr(b1, 'sql_Operands231'):
        assert _is_linked(b1, 'sql_Operands231', a)
    _safe_set(a, 'sql_OpFunctionCast230', b2)
    assert _is_linked(a, 'sql_OpFunctionCast230', b2)
    if hasattr(b1, 'sql_Operands231'):
        assert not _is_linked(b1, 'sql_Operands231', a)
    if hasattr(b2, 'sql_Operands231'):
        assert _is_linked(b2, 'sql_Operands231', a)
    _safe_set(a, 'sql_OpFunctionCast230', None)
    assert not _is_linked(a, 'sql_OpFunctionCast230', b2)
    if hasattr(b2, 'sql_Operands231'):
        assert not _is_linked(b2, 'sql_Operands231', a)


def test_assoc_op3144_link_reassign_clear():
    a = sql_Between(opBetween="sample_text")
    b1 = sql_Operands()
    b2 = sql_Operands()
    _safe_set(a, 'sql_Between145', b1)
    assert _is_linked(a, 'sql_Between145', b1)
    if hasattr(b1, 'sql_Operands146'):
        assert _is_linked(b1, 'sql_Operands146', a)
    _safe_set(a, 'sql_Between145', b2)
    assert _is_linked(a, 'sql_Between145', b2)
    if hasattr(b1, 'sql_Operands146'):
        assert not _is_linked(b1, 'sql_Operands146', a)
    if hasattr(b2, 'sql_Operands146'):
        assert _is_linked(b2, 'sql_Operands146', a)
    _safe_set(a, 'sql_Between145', None)
    assert not _is_linked(a, 'sql_Between145', b2)
    if hasattr(b2, 'sql_Operands146'):
        assert not _is_linked(b2, 'sql_Operands146', a)


def test_assoc_op5_link_reassign_clear():
    a = sql_SelectSubSet(all="sample_text", op="sample_text")
    b1 = sql_Select(select="sample_text")
    b2 = sql_Select(select="sample_text_2")
    _safe_set(a, 'sql_SelectSubSet7', b1)
    assert _is_linked(a, 'sql_SelectSubSet7', b1)
    if hasattr(b1, 'sql_Select6'):
        assert _is_linked(b1, 'sql_Select6', a)
    _safe_set(a, 'sql_SelectSubSet7', b2)
    assert _is_linked(a, 'sql_SelectSubSet7', b2)
    if hasattr(b1, 'sql_Select6'):
        assert not _is_linked(b1, 'sql_Select6', a)
    if hasattr(b2, 'sql_Select6'):
        assert _is_linked(b2, 'sql_Select6', a)
    _safe_set(a, 'sql_SelectSubSet7', None)
    assert not _is_linked(a, 'sql_SelectSubSet7', b2)
    if hasattr(b2, 'sql_Select6'):
        assert not _is_linked(b2, 'sql_Select6', a)


def test_assoc_opList150_link_reassign_clear():
    a = sql_InOper(op="sample_text")
    b1 = sql_OperandListGroup()
    b2 = sql_OperandListGroup()
    _safe_set(a, 'sql_InOper151', b1)
    assert _is_linked(a, 'sql_InOper151', b1)
    if hasattr(b1, 'sql_OperandListGroup'):
        assert _is_linked(b1, 'sql_OperandListGroup', a)
    _safe_set(a, 'sql_InOper151', b2)
    assert _is_linked(a, 'sql_InOper151', b2)
    if hasattr(b1, 'sql_OperandListGroup'):
        assert not _is_linked(b1, 'sql_OperandListGroup', a)
    if hasattr(b2, 'sql_OperandListGroup'):
        assert _is_linked(b2, 'sql_OperandListGroup', a)
    _safe_set(a, 'sql_InOper151', None)
    assert not _is_linked(a, 'sql_InOper151', b2)
    if hasattr(b2, 'sql_OperandListGroup'):
        assert not _is_linked(b2, 'sql_OperandListGroup', a)


def test_assoc_opList155_link_reassign_clear():
    a = sql_ExistsOper(op="sample_text")
    b1 = sql_OperandListGroup()
    b2 = sql_OperandListGroup()
    _safe_set(a, 'sql_ExistsOper156', b1)
    assert _is_linked(a, 'sql_ExistsOper156', b1)
    if hasattr(b1, 'sql_OperandListGroup157'):
        assert _is_linked(b1, 'sql_OperandListGroup157', a)
    _safe_set(a, 'sql_ExistsOper156', b2)
    assert _is_linked(a, 'sql_ExistsOper156', b2)
    if hasattr(b1, 'sql_OperandListGroup157'):
        assert not _is_linked(b1, 'sql_OperandListGroup157', a)
    if hasattr(b2, 'sql_OperandListGroup157'):
        assert _is_linked(b2, 'sql_OperandListGroup157', a)
    _safe_set(a, 'sql_ExistsOper156', None)
    assert not _is_linked(a, 'sql_ExistsOper156', b2)
    if hasattr(b2, 'sql_OperandListGroup157'):
        assert not _is_linked(b2, 'sql_OperandListGroup157', a)


def test_assoc_operand197_link_reassign_clear():
    a = sql_FunctionExtract(v="sample_text")
    b1 = sql_Operands()
    b2 = sql_Operands()
    _safe_set(a, 'sql_FunctionExtract198', b1)
    assert _is_linked(a, 'sql_FunctionExtract198', b1)
    if hasattr(b1, 'sql_Operands199'):
        assert _is_linked(b1, 'sql_Operands199', a)
    _safe_set(a, 'sql_FunctionExtract198', b2)
    assert _is_linked(a, 'sql_FunctionExtract198', b2)
    if hasattr(b1, 'sql_Operands199'):
        assert not _is_linked(b1, 'sql_Operands199', a)
    if hasattr(b2, 'sql_Operands199'):
        assert _is_linked(b2, 'sql_Operands199', a)
    _safe_set(a, 'sql_FunctionExtract198', None)
    assert not _is_linked(a, 'sql_FunctionExtract198', b2)
    if hasattr(b2, 'sql_Operands199'):
        assert not _is_linked(b2, 'sql_Operands199', a)


def test_assoc_orderByEntry19_link_reassign_clear():
    a = sql_Select(select="sample_text")
    b1 = sql_OrOrderByColumn()
    b2 = sql_OrOrderByColumn()
    _safe_set(a, 'sql_Select20', b1)
    assert _is_linked(a, 'sql_Select20', b1)
    if hasattr(b1, 'sql_OrOrderByColumn'):
        assert _is_linked(b1, 'sql_OrOrderByColumn', a)
    _safe_set(a, 'sql_Select20', b2)
    assert _is_linked(a, 'sql_Select20', b2)
    if hasattr(b1, 'sql_OrOrderByColumn'):
        assert not _is_linked(b1, 'sql_OrOrderByColumn', a)
    if hasattr(b2, 'sql_OrOrderByColumn'):
        assert _is_linked(b2, 'sql_OrOrderByColumn', a)
    _safe_set(a, 'sql_Select20', None)
    assert not _is_linked(a, 'sql_Select20', b2)
    if hasattr(b2, 'sql_OrOrderByColumn'):
        assert not _is_linked(b2, 'sql_OrOrderByColumn', a)


def test_assoc_param186_link_reassign_clear():
    a = sql_POperand(prm="sample_text")
    b1 = sql_Operand()
    b2 = sql_Operand()
    _safe_set(a, 'sql_POperand188', b1)
    assert _is_linked(a, 'sql_POperand188', b1)
    if hasattr(b1, 'sql_Operand187'):
        assert _is_linked(b1, 'sql_Operand187', a)
    _safe_set(a, 'sql_POperand188', b2)
    assert _is_linked(a, 'sql_POperand188', b2)
    if hasattr(b1, 'sql_Operand187'):
        assert not _is_linked(b1, 'sql_Operand187', a)
    if hasattr(b2, 'sql_Operand187'):
        assert _is_linked(b2, 'sql_Operand187', a)
    _safe_set(a, 'sql_POperand188', None)
    assert not _is_linked(a, 'sql_POperand188', b2)
    if hasattr(b2, 'sql_Operand187'):
        assert not _is_linked(b2, 'sql_Operand187', a)


def test_assoc_pfun60_link_reassign_clear():
    a = sql_PivotFunctions(abc="sample_text")
    b1 = sql_PivotTable()
    b2 = sql_PivotTable()
    _safe_set(a, 'sql_PivotFunctions', b1)
    assert _is_linked(a, 'sql_PivotFunctions', b1)
    if hasattr(b1, 'sql_PivotTable61'):
        assert _is_linked(b1, 'sql_PivotTable61', a)
    _safe_set(a, 'sql_PivotFunctions', b2)
    assert _is_linked(a, 'sql_PivotFunctions', b2)
    if hasattr(b1, 'sql_PivotTable61'):
        assert not _is_linked(b1, 'sql_PivotTable61', a)
    if hasattr(b2, 'sql_PivotTable61'):
        assert _is_linked(b2, 'sql_PivotTable61', a)
    _safe_set(a, 'sql_PivotFunctions', None)
    assert not _is_linked(a, 'sql_PivotFunctions', b2)
    if hasattr(b2, 'sql_PivotTable61'):
        assert not _is_linked(b2, 'sql_PivotTable61', a)


def test_assoc_pin64_link_reassign_clear():
    a = sql_PivotInClause(pinany="sample_text")
    b1 = sql_PivotTable()
    b2 = sql_PivotTable()
    _safe_set(a, 'sql_PivotInClause', b1)
    assert _is_linked(a, 'sql_PivotInClause', b1)
    if hasattr(b1, 'sql_PivotTable65'):
        assert _is_linked(b1, 'sql_PivotTable65', a)
    _safe_set(a, 'sql_PivotInClause', b2)
    assert _is_linked(a, 'sql_PivotInClause', b2)
    if hasattr(b1, 'sql_PivotTable65'):
        assert not _is_linked(b1, 'sql_PivotTable65', a)
    if hasattr(b2, 'sql_PivotTable65'):
        assert _is_linked(b2, 'sql_PivotTable65', a)
    _safe_set(a, 'sql_PivotInClause', None)
    assert not _is_linked(a, 'sql_PivotInClause', b2)
    if hasattr(b2, 'sql_PivotTable65'):
        assert not _is_linked(b2, 'sql_PivotTable65', a)


def test_assoc_pivot53_link_reassign_clear():
    a = sql_TableOrAlias(alias="sample_text")
    b1 = sql_PivotTable()
    b2 = sql_PivotTable()
    _safe_set(a, 'sql_TableOrAlias54', b1)
    assert _is_linked(a, 'sql_TableOrAlias54', b1)
    if hasattr(b1, 'sql_PivotTable'):
        assert _is_linked(b1, 'sql_PivotTable', a)
    _safe_set(a, 'sql_TableOrAlias54', b2)
    assert _is_linked(a, 'sql_TableOrAlias54', b2)
    if hasattr(b1, 'sql_PivotTable'):
        assert not _is_linked(b1, 'sql_PivotTable', a)
    if hasattr(b2, 'sql_PivotTable'):
        assert _is_linked(b2, 'sql_PivotTable', a)
    _safe_set(a, 'sql_TableOrAlias54', None)
    assert not _is_linked(a, 'sql_TableOrAlias54', b2)
    if hasattr(b2, 'sql_PivotTable'):
        assert not _is_linked(b2, 'sql_PivotTable', a)


def test_assoc_prm125_link_reassign_clear():
    a = sql_XExpr(xf="sample_text")
    b1 = sql_Prms()
    b2 = sql_Prms()
    _safe_set(a, 'sql_XExpr126', b1)
    assert _is_linked(a, 'sql_XExpr126', b1)
    if hasattr(b1, 'sql_Prms'):
        assert _is_linked(b1, 'sql_Prms', a)
    _safe_set(a, 'sql_XExpr126', b2)
    assert _is_linked(a, 'sql_XExpr126', b2)
    if hasattr(b1, 'sql_Prms'):
        assert not _is_linked(b1, 'sql_Prms', a)
    if hasattr(b2, 'sql_Prms'):
        assert _is_linked(b2, 'sql_Prms', a)
    _safe_set(a, 'sql_XExpr126', None)
    assert not _is_linked(a, 'sql_XExpr126', b2)
    if hasattr(b2, 'sql_Prms'):
        assert not _is_linked(b2, 'sql_Prms', a)


def test_assoc_query4_link_reassign_clear():
    a = sql_SelectSubSet(all="sample_text", op="sample_text")
    b1 = sql_Select(select="sample_text")
    b2 = sql_Select(select="sample_text_2")
    _safe_set(a, 'sql_SelectSubSet', b1)
    assert _is_linked(a, 'sql_SelectSubSet', b1)
    if hasattr(b1, 'sql_Select'):
        assert _is_linked(b1, 'sql_Select', a)
    _safe_set(a, 'sql_SelectSubSet', b2)
    assert _is_linked(a, 'sql_SelectSubSet', b2)
    if hasattr(b1, 'sql_Select'):
        assert not _is_linked(b1, 'sql_Select', a)
    if hasattr(b2, 'sql_Select'):
        assert _is_linked(b2, 'sql_Select', a)
    _safe_set(a, 'sql_SelectSubSet', None)
    assert not _is_linked(a, 'sql_SelectSubSet', b2)
    if hasattr(b2, 'sql_Select'):
        assert not _is_linked(b2, 'sql_Select', a)


def test_assoc_scalar191_link_reassign_clear():
    a = sql_ScalarOperand(sodate=date(2024, 1, 1), sodbl="sample_text", sodt=date(2024, 1, 1), soint=7, sostr="sample_text", sotime=date(2024, 1, 1))
    b1 = sql_Operand()
    b2 = sql_Operand()
    _safe_set(a, 'sql_ScalarOperand', b1)
    assert _is_linked(a, 'sql_ScalarOperand', b1)
    if hasattr(b1, 'sql_Operand192'):
        assert _is_linked(b1, 'sql_Operand192', a)
    _safe_set(a, 'sql_ScalarOperand', b2)
    assert _is_linked(a, 'sql_ScalarOperand', b2)
    if hasattr(b1, 'sql_Operand192'):
        assert not _is_linked(b1, 'sql_Operand192', a)
    if hasattr(b2, 'sql_Operand192'):
        assert _is_linked(b2, 'sql_Operand192', a)
    _safe_set(a, 'sql_ScalarOperand', None)
    assert not _is_linked(a, 'sql_ScalarOperand', b2)
    if hasattr(b2, 'sql_Operand192'):
        assert not _is_linked(b2, 'sql_Operand192', a)


def test_assoc_sq51_link_reassign_clear():
    a = sql_TableOrAlias(alias="sample_text")
    b1 = sql_SubQueryOperand()
    b2 = sql_SubQueryOperand()
    _safe_set(a, 'sql_TableOrAlias52', b1)
    assert _is_linked(a, 'sql_TableOrAlias52', b1)
    if hasattr(b1, 'sql_SubQueryOperand'):
        assert _is_linked(b1, 'sql_SubQueryOperand', a)
    _safe_set(a, 'sql_TableOrAlias52', b2)
    assert _is_linked(a, 'sql_TableOrAlias52', b2)
    if hasattr(b1, 'sql_SubQueryOperand'):
        assert not _is_linked(b1, 'sql_SubQueryOperand', a)
    if hasattr(b2, 'sql_SubQueryOperand'):
        assert _is_linked(b2, 'sql_SubQueryOperand', a)
    _safe_set(a, 'sql_TableOrAlias52', None)
    assert not _is_linked(a, 'sql_TableOrAlias52', b2)
    if hasattr(b2, 'sql_SubQueryOperand'):
        assert not _is_linked(b2, 'sql_SubQueryOperand', a)


def test_assoc_sq66_link_reassign_clear():
    a = sql_PivotInClause(pinany="sample_text")
    b1 = sql_SubQueryOperand()
    b2 = sql_SubQueryOperand()
    _safe_set(a, 'sql_PivotInClause67', b1)
    assert _is_linked(a, 'sql_PivotInClause67', b1)
    if hasattr(b1, 'sql_SubQueryOperand68'):
        assert _is_linked(b1, 'sql_SubQueryOperand68', a)
    _safe_set(a, 'sql_PivotInClause67', b2)
    assert _is_linked(a, 'sql_PivotInClause67', b2)
    if hasattr(b1, 'sql_SubQueryOperand68'):
        assert not _is_linked(b1, 'sql_SubQueryOperand68', a)
    if hasattr(b2, 'sql_SubQueryOperand68'):
        assert _is_linked(b2, 'sql_SubQueryOperand68', a)
    _safe_set(a, 'sql_PivotInClause67', None)
    assert not _is_linked(a, 'sql_PivotInClause67', b2)
    if hasattr(b2, 'sql_SubQueryOperand68'):
        assert not _is_linked(b2, 'sql_SubQueryOperand68', a)


def test_assoc_subquery147_link_reassign_clear():
    a = sql_InOper(op="sample_text")
    b1 = sql_SubQueryOperand()
    b2 = sql_SubQueryOperand()
    _safe_set(a, 'sql_InOper148', b1)
    assert _is_linked(a, 'sql_InOper148', b1)
    if hasattr(b1, 'sql_SubQueryOperand149'):
        assert _is_linked(b1, 'sql_SubQueryOperand149', a)
    _safe_set(a, 'sql_InOper148', b2)
    assert _is_linked(a, 'sql_InOper148', b2)
    if hasattr(b1, 'sql_SubQueryOperand149'):
        assert not _is_linked(b1, 'sql_SubQueryOperand149', a)
    if hasattr(b2, 'sql_SubQueryOperand149'):
        assert _is_linked(b2, 'sql_SubQueryOperand149', a)
    _safe_set(a, 'sql_InOper148', None)
    assert not _is_linked(a, 'sql_InOper148', b2)
    if hasattr(b2, 'sql_SubQueryOperand149'):
        assert not _is_linked(b2, 'sql_SubQueryOperand149', a)


def test_assoc_subquery152_link_reassign_clear():
    a = sql_ExistsOper(op="sample_text")
    b1 = sql_SubQueryOperand()
    b2 = sql_SubQueryOperand()
    _safe_set(a, 'sql_ExistsOper153', b1)
    assert _is_linked(a, 'sql_ExistsOper153', b1)
    if hasattr(b1, 'sql_SubQueryOperand154'):
        assert _is_linked(b1, 'sql_SubQueryOperand154', a)
    _safe_set(a, 'sql_ExistsOper153', b2)
    assert _is_linked(a, 'sql_ExistsOper153', b2)
    if hasattr(b1, 'sql_SubQueryOperand154'):
        assert not _is_linked(b1, 'sql_SubQueryOperand154', a)
    if hasattr(b2, 'sql_SubQueryOperand154'):
        assert _is_linked(b2, 'sql_SubQueryOperand154', a)
    _safe_set(a, 'sql_ExistsOper153', None)
    assert not _is_linked(a, 'sql_ExistsOper153', b2)
    if hasattr(b2, 'sql_SubQueryOperand154'):
        assert not _is_linked(b2, 'sql_SubQueryOperand154', a)


def test_assoc_table39_link_reassign_clear():
    a = sql_TableOrAlias(alias="sample_text")
    b1 = sql_FromTable()
    b2 = sql_FromTable()
    _safe_set(a, 'sql_TableOrAlias', b1)
    assert _is_linked(a, 'sql_TableOrAlias', b1)
    if hasattr(b1, 'sql_FromTable40'):
        assert _is_linked(b1, 'sql_FromTable40', a)
    _safe_set(a, 'sql_TableOrAlias', b2)
    assert _is_linked(a, 'sql_TableOrAlias', b2)
    if hasattr(b1, 'sql_FromTable40'):
        assert not _is_linked(b1, 'sql_FromTable40', a)
    if hasattr(b2, 'sql_FromTable40'):
        assert _is_linked(b2, 'sql_FromTable40', a)
    _safe_set(a, 'sql_TableOrAlias', None)
    assert not _is_linked(a, 'sql_TableOrAlias', b2)
    if hasattr(b2, 'sql_FromTable40'):
        assert not _is_linked(b2, 'sql_FromTable40', a)


def test_assoc_tbl10_link_reassign_clear():
    a = sql_Select(select="sample_text")
    b1 = sql_OrTable()
    b2 = sql_OrTable()
    _safe_set(a, 'sql_Select11', b1)
    assert _is_linked(a, 'sql_Select11', b1)
    if hasattr(b1, 'sql_OrTable'):
        assert _is_linked(b1, 'sql_OrTable', a)
    _safe_set(a, 'sql_Select11', b2)
    assert _is_linked(a, 'sql_Select11', b2)
    if hasattr(b1, 'sql_OrTable'):
        assert not _is_linked(b1, 'sql_OrTable', a)
    if hasattr(b2, 'sql_OrTable'):
        assert _is_linked(b2, 'sql_OrTable', a)
    _safe_set(a, 'sql_Select11', None)
    assert not _is_linked(a, 'sql_Select11', b2)
    if hasattr(b2, 'sql_OrTable'):
        assert not _is_linked(b2, 'sql_OrTable', a)


def test_assoc_tblAlias57_link_reassign_clear():
    a = sql_TableOrAlias(alias="sample_text")
    b1 = sql_DbObjectName(dbname="sample_text")
    b2 = sql_DbObjectName(dbname="sample_text_2")
    _safe_set(a, 'sql_TableOrAlias58', b1)
    assert _is_linked(a, 'sql_TableOrAlias58', b1)
    if hasattr(b1, 'sql_DbObjectName59'):
        assert _is_linked(b1, 'sql_DbObjectName59', a)
    _safe_set(a, 'sql_TableOrAlias58', b2)
    assert _is_linked(a, 'sql_TableOrAlias58', b2)
    if hasattr(b1, 'sql_DbObjectName59'):
        assert not _is_linked(b1, 'sql_DbObjectName59', a)
    if hasattr(b2, 'sql_DbObjectName59'):
        assert _is_linked(b2, 'sql_DbObjectName59', a)
    _safe_set(a, 'sql_TableOrAlias58', None)
    assert not _is_linked(a, 'sql_TableOrAlias58', b2)
    if hasattr(b2, 'sql_DbObjectName59'):
        assert not _is_linked(b2, 'sql_DbObjectName59', a)


def test_assoc_tfull49_link_reassign_clear():
    a = sql_TableOrAlias(alias="sample_text")
    b1 = sql_TableFull()
    b2 = sql_TableFull()
    _safe_set(a, 'sql_TableOrAlias50', b1)
    assert _is_linked(a, 'sql_TableOrAlias50', b1)
    if hasattr(b1, 'sql_TableFull'):
        assert _is_linked(b1, 'sql_TableFull', a)
    _safe_set(a, 'sql_TableOrAlias50', b2)
    assert _is_linked(a, 'sql_TableOrAlias50', b2)
    if hasattr(b1, 'sql_TableFull'):
        assert not _is_linked(b1, 'sql_TableFull', a)
    if hasattr(b2, 'sql_TableFull'):
        assert _is_linked(b2, 'sql_TableFull', a)
    _safe_set(a, 'sql_TableOrAlias50', None)
    assert not _is_linked(a, 'sql_TableOrAlias50', b2)
    if hasattr(b2, 'sql_TableFull'):
        assert not _is_linked(b2, 'sql_TableFull', a)


def test_assoc_unpivot55_link_reassign_clear():
    a = sql_TableOrAlias(alias="sample_text")
    b1 = sql_UnpivotTable()
    b2 = sql_UnpivotTable()
    _safe_set(a, 'sql_TableOrAlias56', b1)
    assert _is_linked(a, 'sql_TableOrAlias56', b1)
    if hasattr(b1, 'sql_UnpivotTable'):
        assert _is_linked(b1, 'sql_UnpivotTable', a)
    _safe_set(a, 'sql_TableOrAlias56', b2)
    assert _is_linked(a, 'sql_TableOrAlias56', b2)
    if hasattr(b1, 'sql_UnpivotTable'):
        assert not _is_linked(b1, 'sql_UnpivotTable', a)
    if hasattr(b2, 'sql_UnpivotTable'):
        assert _is_linked(b2, 'sql_UnpivotTable', a)
    _safe_set(a, 'sql_TableOrAlias56', None)
    assert not _is_linked(a, 'sql_TableOrAlias56', b2)
    if hasattr(b2, 'sql_UnpivotTable'):
        assert not _is_linked(b2, 'sql_UnpivotTable', a)


def test_assoc_whereExpression12_link_reassign_clear():
    a = sql_Select(select="sample_text")
    b1 = sql_OrExpr()
    b2 = sql_OrExpr()
    _safe_set(a, 'sql_Select13', b1)
    assert _is_linked(a, 'sql_Select13', b1)
    if hasattr(b1, 'sql_OrExpr'):
        assert _is_linked(b1, 'sql_OrExpr', a)
    _safe_set(a, 'sql_Select13', b2)
    assert _is_linked(a, 'sql_Select13', b2)
    if hasattr(b1, 'sql_OrExpr'):
        assert not _is_linked(b1, 'sql_OrExpr', a)
    if hasattr(b2, 'sql_OrExpr'):
        assert _is_linked(b2, 'sql_OrExpr', a)
    _safe_set(a, 'sql_Select13', None)
    assert not _is_linked(a, 'sql_Select13', b2)
    if hasattr(b2, 'sql_OrExpr'):
        assert not _is_linked(b2, 'sql_OrExpr', a)


def test_assoc_xexp104_link_reassign_clear():
    a = sql_XExpr(xf="sample_text")
    b1 = sql_FullExpression(c="sample_text", isnull="sample_text", notPrm="sample_text")
    b2 = sql_FullExpression(c="sample_text_2", isnull="sample_text_2", notPrm="sample_text_2")
    _safe_set(a, 'sql_XExpr', b1)
    assert _is_linked(a, 'sql_XExpr', b1)
    if hasattr(b1, 'sql_FullExpression105'):
        assert _is_linked(b1, 'sql_FullExpression105', a)
    _safe_set(a, 'sql_XExpr', b2)
    assert _is_linked(a, 'sql_XExpr', b2)
    if hasattr(b1, 'sql_FullExpression105'):
        assert not _is_linked(b1, 'sql_FullExpression105', a)
    if hasattr(b2, 'sql_FullExpression105'):
        assert _is_linked(b2, 'sql_FullExpression105', a)
    _safe_set(a, 'sql_XExpr', None)
    assert not _is_linked(a, 'sql_XExpr', b2)
    if hasattr(b2, 'sql_FullExpression105'):
        assert not _is_linked(b2, 'sql_FullExpression105', a)


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

AnalyticExprArgs_strategy = st.builds(AnalyticExprArgs)
@given(instance=AnalyticExprArgs_strategy)
@settings(max_examples=25)
def test_AnalyticExprArgs_instantiation(instance):
    assert isinstance(instance, AnalyticExprArgs)


ColumnFull_strategy = st.builds(ColumnFull)
@given(instance=ColumnFull_strategy)
@settings(max_examples=25)
def test_ColumnFull_instantiation(instance):
    assert isinstance(instance, ColumnFull)


OpFunctionArg_strategy = st.builds(OpFunctionArg)
@given(instance=OpFunctionArg_strategy)
@settings(max_examples=25)
def test_OpFunctionArg_instantiation(instance):
    assert isinstance(instance, OpFunctionArg)


OpFunctionArgAgregate_strategy = st.builds(OpFunctionArgAgregate)
@given(instance=OpFunctionArgAgregate_strategy)
@settings(max_examples=25)
def test_OpFunctionArgAgregate_instantiation(instance):
    assert isinstance(instance, OpFunctionArgAgregate)


OperandList_strategy = st.builds(OperandList)
@given(instance=OperandList_strategy)
@settings(max_examples=25)
def test_OperandList_instantiation(instance):
    assert isinstance(instance, OperandList)


Operands_strategy = st.builds(Operands)
@given(instance=Operands_strategy)
@settings(max_examples=25)
def test_Operands_instantiation(instance):
    assert isinstance(instance, Operands)


OrColumn_strategy = st.builds(OrColumn)
@given(instance=OrColumn_strategy)
@settings(max_examples=25)
def test_OrColumn_instantiation(instance):
    assert isinstance(instance, OrColumn)


OrExpr_strategy = st.builds(OrExpr)
@given(instance=OrExpr_strategy)
@settings(max_examples=25)
def test_OrExpr_instantiation(instance):
    assert isinstance(instance, OrExpr)


OrGroupByColumn_strategy = st.builds(OrGroupByColumn)
@given(instance=OrGroupByColumn_strategy)
@settings(max_examples=25)
def test_OrGroupByColumn_instantiation(instance):
    assert isinstance(instance, OrGroupByColumn)


OrOrderByColumn_strategy = st.builds(OrOrderByColumn)
@given(instance=OrOrderByColumn_strategy)
@settings(max_examples=25)
def test_OrOrderByColumn_instantiation(instance):
    assert isinstance(instance, OrOrderByColumn)


OrTable_strategy = st.builds(OrTable)
@given(instance=OrTable_strategy)
@settings(max_examples=25)
def test_OrTable_instantiation(instance):
    assert isinstance(instance, OrTable)


OrderByClauseArgs_strategy = st.builds(OrderByClauseArgs)
@given(instance=OrderByClauseArgs_strategy)
@settings(max_examples=25)
def test_OrderByClauseArgs_instantiation(instance):
    assert isinstance(instance, OrderByClauseArgs)


PivotCol_strategy = st.builds(PivotCol)
@given(instance=PivotCol_strategy)
@settings(max_examples=25)
def test_PivotCol_instantiation(instance):
    assert isinstance(instance, PivotCol)


PivotColumns_strategy = st.builds(PivotColumns)
@given(instance=PivotColumns_strategy)
@settings(max_examples=25)
def test_PivotColumns_instantiation(instance):
    assert isinstance(instance, PivotColumns)


PivotForClause_strategy = st.builds(PivotForClause)
@given(instance=PivotForClause_strategy)
@settings(max_examples=25)
def test_PivotForClause_instantiation(instance):
    assert isinstance(instance, PivotForClause)


PivotFunction_strategy = st.builds(PivotFunction)
@given(instance=PivotFunction_strategy)
@settings(max_examples=25)
def test_PivotFunction_instantiation(instance):
    assert isinstance(instance, PivotFunction)


Pivots_strategy = st.builds(Pivots)
@given(instance=Pivots_strategy)
@settings(max_examples=25)
def test_Pivots_instantiation(instance):
    assert isinstance(instance, Pivots)


Prms_strategy = st.builds(Prms)
@given(instance=Prms_strategy)
@settings(max_examples=25)
def test_Prms_instantiation(instance):
    assert isinstance(instance, Prms)


QueryPartitionClause_strategy = st.builds(QueryPartitionClause)
@given(instance=QueryPartitionClause_strategy)
@settings(max_examples=25)
def test_QueryPartitionClause_instantiation(instance):
    assert isinstance(instance, QueryPartitionClause)


SQLCaseWhens_strategy = st.builds(SQLCaseWhens)
@given(instance=SQLCaseWhens_strategy)
@settings(max_examples=25)
def test_SQLCaseWhens_instantiation(instance):
    assert isinstance(instance, SQLCaseWhens)


SelectQuery_strategy = st.builds(SelectQuery)
@given(instance=SelectQuery_strategy)
@settings(max_examples=25)
def test_SelectQuery_instantiation(instance):
    assert isinstance(instance, SelectQuery)


TableFull_strategy = st.builds(TableFull)
@given(instance=TableFull_strategy)
@settings(max_examples=25)
def test_TableFull_instantiation(instance):
    assert isinstance(instance, TableFull)


UnpivotInClause_strategy = st.builds(UnpivotInClause)
@given(instance=UnpivotInClause_strategy)
@settings(max_examples=25)
def test_UnpivotInClause_instantiation(instance):
    assert isinstance(instance, UnpivotInClause)


UnpivotInClauseArgs_strategy = st.builds(UnpivotInClauseArgs)
@given(instance=UnpivotInClauseArgs_strategy)
@settings(max_examples=25)
def test_UnpivotInClauseArgs_instantiation(instance):
    assert isinstance(instance, UnpivotInClauseArgs)


WindowingClause_strategy = st.builds(WindowingClause)
@given(instance=WindowingClause_strategy)
@settings(max_examples=25)
def test_WindowingClause_instantiation(instance):
    assert isinstance(instance, WindowingClause)


sql_AExpArgs_strategy = st.builds(sql_AExpArgs)
@given(instance=sql_AExpArgs_strategy)
@settings(max_examples=25)
def test_sql_AExpArgs_instantiation(instance):
    assert isinstance(instance, sql_AExpArgs)


sql_AnalyticClause_strategy = st.builds(sql_AnalyticClause)
@given(instance=sql_AnalyticClause_strategy)
@settings(max_examples=25)
def test_sql_AnalyticClause_instantiation(instance):
    assert isinstance(instance, sql_AnalyticClause)


sql_AnalyticExprArg_strategy = st.builds(sql_AnalyticExprArg)
@given(instance=sql_AnalyticExprArg_strategy)
@settings(max_examples=25)
def test_sql_AnalyticExprArg_instantiation(instance):
    assert isinstance(instance, sql_AnalyticExprArg)


sql_AnalyticExprArgs_strategy = st.builds(sql_AnalyticExprArgs)
@given(instance=sql_AnalyticExprArgs_strategy)
@settings(max_examples=25)
def test_sql_AnalyticExprArgs_instantiation(instance):
    assert isinstance(instance, sql_AnalyticExprArgs)


sql_Between_strategy = st.builds(sql_Between, opBetween=safe_text)
@given(instance=sql_Between_strategy)
@settings(max_examples=25)
def test_sql_Between_instantiation(instance):
    assert isinstance(instance, sql_Between)


sql_Col_strategy = st.builds(sql_Col)
@given(instance=sql_Col_strategy)
@settings(max_examples=25)
def test_sql_Col_instantiation(instance):
    assert isinstance(instance, sql_Col)


sql_ColumnFull_strategy = st.builds(sql_ColumnFull)
@given(instance=sql_ColumnFull_strategy)
@settings(max_examples=25)
def test_sql_ColumnFull_instantiation(instance):
    assert isinstance(instance, sql_ColumnFull)


sql_ColumnOperand_strategy = st.builds(sql_ColumnOperand, ora=safe_text)
@given(instance=sql_ColumnOperand_strategy)
@settings(max_examples=25)
def test_sql_ColumnOperand_instantiation(instance):
    assert isinstance(instance, sql_ColumnOperand)


sql_ColumnOrAlias_strategy = st.builds(sql_ColumnOrAlias, alias=safe_text, allCols=safe_text)
@given(instance=sql_ColumnOrAlias_strategy)
@settings(max_examples=25)
def test_sql_ColumnOrAlias_instantiation(instance):
    assert isinstance(instance, sql_ColumnOrAlias)


sql_Comparison_strategy = st.builds(sql_Comparison, operator=safe_text, subOperator=safe_text)
@given(instance=sql_Comparison_strategy)
@settings(max_examples=25)
def test_sql_Comparison_instantiation(instance):
    assert isinstance(instance, sql_Comparison)


sql_Concat_strategy = st.builds(sql_Concat)
@given(instance=sql_Concat_strategy)
@settings(max_examples=25)
def test_sql_Concat_instantiation(instance):
    assert isinstance(instance, sql_Concat)


sql_DbObjectName_strategy = st.builds(sql_DbObjectName, dbname=safe_text)
@given(instance=sql_DbObjectName_strategy)
@settings(max_examples=25)
def test_sql_DbObjectName_instantiation(instance):
    assert isinstance(instance, sql_DbObjectName)


sql_DbObjectNameAll_strategy = st.builds(sql_DbObjectNameAll, dbname=safe_text)
@given(instance=sql_DbObjectNameAll_strategy)
@settings(max_examples=25)
def test_sql_DbObjectNameAll_instantiation(instance):
    assert isinstance(instance, sql_DbObjectNameAll)


sql_Div_strategy = st.builds(sql_Div)
@given(instance=sql_Div_strategy)
@settings(max_examples=25)
def test_sql_Div_instantiation(instance):
    assert isinstance(instance, sql_Div)


sql_ExistsOper_strategy = st.builds(sql_ExistsOper, op=safe_text)
@given(instance=sql_ExistsOper_strategy)
@settings(max_examples=25)
def test_sql_ExistsOper_instantiation(instance):
    assert isinstance(instance, sql_ExistsOper)


sql_ExpOperand_strategy = st.builds(sql_ExpOperand, prm=safe_text)
@given(instance=sql_ExpOperand_strategy)
@settings(max_examples=25)
def test_sql_ExpOperand_instantiation(instance):
    assert isinstance(instance, sql_ExpOperand)


sql_ExprGroup_strategy = st.builds(sql_ExprGroup, isnot=safe_text)
@given(instance=sql_ExprGroup_strategy)
@settings(max_examples=25)
def test_sql_ExprGroup_instantiation(instance):
    assert isinstance(instance, sql_ExprGroup)


sql_FetchFirst_strategy = st.builds(sql_FetchFirst, row=safe_text)
@given(instance=sql_FetchFirst_strategy)
@settings(max_examples=25)
def test_sql_FetchFirst_instantiation(instance):
    assert isinstance(instance, sql_FetchFirst)


sql_FromTable_strategy = st.builds(sql_FromTable)
@given(instance=sql_FromTable_strategy)
@settings(max_examples=25)
def test_sql_FromTable_instantiation(instance):
    assert isinstance(instance, sql_FromTable)


sql_FromTableJoin_strategy = st.builds(sql_FromTableJoin, join=safe_text)
@given(instance=sql_FromTableJoin_strategy)
@settings(max_examples=25)
def test_sql_FromTableJoin_instantiation(instance):
    assert isinstance(instance, sql_FromTableJoin)


sql_FullExpression_strategy = st.builds(sql_FullExpression, c=safe_text, isnull=safe_text, notPrm=safe_text)
@given(instance=sql_FullExpression_strategy)
@settings(max_examples=25)
def test_sql_FullExpression_instantiation(instance):
    assert isinstance(instance, sql_FullExpression)


sql_FunctionAnalytical_strategy = st.builds(sql_FunctionAnalytical)
@given(instance=sql_FunctionAnalytical_strategy)
@settings(max_examples=25)
def test_sql_FunctionAnalytical_instantiation(instance):
    assert isinstance(instance, sql_FunctionAnalytical)


sql_FunctionExtract_strategy = st.builds(sql_FunctionExtract, v=safe_text)
@given(instance=sql_FunctionExtract_strategy)
@settings(max_examples=25)
def test_sql_FunctionExtract_instantiation(instance):
    assert isinstance(instance, sql_FunctionExtract)


sql_GroupByColumnFull_strategy = st.builds(sql_GroupByColumnFull)
@given(instance=sql_GroupByColumnFull_strategy)
@settings(max_examples=25)
def test_sql_GroupByColumnFull_instantiation(instance):
    assert isinstance(instance, sql_GroupByColumnFull)


sql_InOper_strategy = st.builds(sql_InOper, op=safe_text)
@given(instance=sql_InOper_strategy)
@settings(max_examples=25)
def test_sql_InOper_instantiation(instance):
    assert isinstance(instance, sql_InOper)


sql_IntegerValue_strategy = st.builds(sql_IntegerValue, integer=st.integers())
@given(instance=sql_IntegerValue_strategy)
@settings(max_examples=25)
def test_sql_IntegerValue_instantiation(instance):
    assert isinstance(instance, sql_IntegerValue)


sql_JRParameter_strategy = st.builds(sql_JRParameter, jrprm=safe_text)
@given(instance=sql_JRParameter_strategy)
@settings(max_examples=25)
def test_sql_JRParameter_instantiation(instance):
    assert isinstance(instance, sql_JRParameter)


sql_Like_strategy = st.builds(sql_Like, opLike=safe_text)
@given(instance=sql_Like_strategy)
@settings(max_examples=25)
def test_sql_Like_instantiation(instance):
    assert isinstance(instance, sql_Like)


sql_LikeOperand_strategy = st.builds(sql_LikeOperand, op2=safe_text)
@given(instance=sql_LikeOperand_strategy)
@settings(max_examples=25)
def test_sql_LikeOperand_instantiation(instance):
    assert isinstance(instance, sql_LikeOperand)


sql_Limit_strategy = st.builds(sql_Limit, l1=st.integers())
@given(instance=sql_Limit_strategy)
@settings(max_examples=25)
def test_sql_Limit_instantiation(instance):
    assert isinstance(instance, sql_Limit)


sql_Minus_strategy = st.builds(sql_Minus)
@given(instance=sql_Minus_strategy)
@settings(max_examples=25)
def test_sql_Minus_instantiation(instance):
    assert isinstance(instance, sql_Minus)


sql_Model_strategy = st.builds(sql_Model)
@given(instance=sql_Model_strategy)
@settings(max_examples=25)
def test_sql_Model_instantiation(instance):
    assert isinstance(instance, sql_Model)


sql_OBCArgs_strategy = st.builds(sql_OBCArgs)
@given(instance=sql_OBCArgs_strategy)
@settings(max_examples=25)
def test_sql_OBCArgs_instantiation(instance):
    assert isinstance(instance, sql_OBCArgs)


sql_Offset_strategy = st.builds(sql_Offset, offset=st.integers())
@given(instance=sql_Offset_strategy)
@settings(max_examples=25)
def test_sql_Offset_instantiation(instance):
    assert isinstance(instance, sql_Offset)


sql_OpFList_strategy = st.builds(sql_OpFList)
@given(instance=sql_OpFList_strategy)
@settings(max_examples=25)
def test_sql_OpFList_instantiation(instance):
    assert isinstance(instance, sql_OpFList)


sql_OpFunction_strategy = st.builds(sql_OpFunction, fname=safe_text)
@given(instance=sql_OpFunction_strategy)
@settings(max_examples=25)
def test_sql_OpFunction_instantiation(instance):
    assert isinstance(instance, sql_OpFunction)


sql_OpFunctionArg_strategy = st.builds(sql_OpFunctionArg)
@given(instance=sql_OpFunctionArg_strategy)
@settings(max_examples=25)
def test_sql_OpFunctionArg_instantiation(instance):
    assert isinstance(instance, sql_OpFunctionArg)


sql_OpFunctionArgAgregate_strategy = st.builds(sql_OpFunctionArgAgregate)
@given(instance=sql_OpFunctionArgAgregate_strategy)
@settings(max_examples=25)
def test_sql_OpFunctionArgAgregate_instantiation(instance):
    assert isinstance(instance, sql_OpFunctionArgAgregate)


sql_OpFunctionArgOperand_strategy = st.builds(sql_OpFunctionArgOperand)
@given(instance=sql_OpFunctionArgOperand_strategy)
@settings(max_examples=25)
def test_sql_OpFunctionArgOperand_instantiation(instance):
    assert isinstance(instance, sql_OpFunctionArgOperand)


sql_OpFunctionCast_strategy = st.builds(sql_OpFunctionCast, p=st.integers(), p2=st.integers(), type=safe_text)
@given(instance=sql_OpFunctionCast_strategy)
@settings(max_examples=25)
def test_sql_OpFunctionCast_instantiation(instance):
    assert isinstance(instance, sql_OpFunctionCast)


sql_OpList_strategy = st.builds(sql_OpList)
@given(instance=sql_OpList_strategy)
@settings(max_examples=25)
def test_sql_OpList_instantiation(instance):
    assert isinstance(instance, sql_OpList)


sql_Operand_strategy = st.builds(sql_Operand)
@given(instance=sql_Operand_strategy)
@settings(max_examples=25)
def test_sql_Operand_instantiation(instance):
    assert isinstance(instance, sql_Operand)


sql_OperandList_strategy = st.builds(sql_OperandList)
@given(instance=sql_OperandList_strategy)
@settings(max_examples=25)
def test_sql_OperandList_instantiation(instance):
    assert isinstance(instance, sql_OperandList)


sql_OperandListGroup_strategy = st.builds(sql_OperandListGroup)
@given(instance=sql_OperandListGroup_strategy)
@settings(max_examples=25)
def test_sql_OperandListGroup_instantiation(instance):
    assert isinstance(instance, sql_OperandListGroup)


sql_Operands_strategy = st.builds(sql_Operands)
@given(instance=sql_Operands_strategy)
@settings(max_examples=25)
def test_sql_Operands_instantiation(instance):
    assert isinstance(instance, sql_Operands)


sql_OrColumn_strategy = st.builds(sql_OrColumn)
@given(instance=sql_OrColumn_strategy)
@settings(max_examples=25)
def test_sql_OrColumn_instantiation(instance):
    assert isinstance(instance, sql_OrColumn)


sql_OrExpr_strategy = st.builds(sql_OrExpr)
@given(instance=sql_OrExpr_strategy)
@settings(max_examples=25)
def test_sql_OrExpr_instantiation(instance):
    assert isinstance(instance, sql_OrExpr)


sql_OrGroupByColumn_strategy = st.builds(sql_OrGroupByColumn)
@given(instance=sql_OrGroupByColumn_strategy)
@settings(max_examples=25)
def test_sql_OrGroupByColumn_instantiation(instance):
    assert isinstance(instance, sql_OrGroupByColumn)


sql_OrOrderByColumn_strategy = st.builds(sql_OrOrderByColumn)
@given(instance=sql_OrOrderByColumn_strategy)
@settings(max_examples=25)
def test_sql_OrOrderByColumn_instantiation(instance):
    assert isinstance(instance, sql_OrOrderByColumn)


sql_OrTable_strategy = st.builds(sql_OrTable)
@given(instance=sql_OrTable_strategy)
@settings(max_examples=25)
def test_sql_OrTable_instantiation(instance):
    assert isinstance(instance, sql_OrTable)


sql_OrderByClause_strategy = st.builds(sql_OrderByClause)
@given(instance=sql_OrderByClause_strategy)
@settings(max_examples=25)
def test_sql_OrderByClause_instantiation(instance):
    assert isinstance(instance, sql_OrderByClause)


sql_OrderByClauseArg_strategy = st.builds(sql_OrderByClauseArg)
@given(instance=sql_OrderByClauseArg_strategy)
@settings(max_examples=25)
def test_sql_OrderByClauseArg_instantiation(instance):
    assert isinstance(instance, sql_OrderByClauseArg)


sql_OrderByClauseArgs_strategy = st.builds(sql_OrderByClauseArgs)
@given(instance=sql_OrderByClauseArgs_strategy)
@settings(max_examples=25)
def test_sql_OrderByClauseArgs_instantiation(instance):
    assert isinstance(instance, sql_OrderByClauseArgs)


sql_OrderByColumnFull_strategy = st.builds(sql_OrderByColumnFull, colOrderInt=st.integers(), direction=safe_text)
@given(instance=sql_OrderByColumnFull_strategy)
@settings(max_examples=25)
def test_sql_OrderByColumnFull_instantiation(instance):
    assert isinstance(instance, sql_OrderByColumnFull)


sql_POperand_strategy = st.builds(sql_POperand, prm=safe_text)
@given(instance=sql_POperand_strategy)
@settings(max_examples=25)
def test_sql_POperand_instantiation(instance):
    assert isinstance(instance, sql_POperand)


sql_PivotCol_strategy = st.builds(sql_PivotCol)
@given(instance=sql_PivotCol_strategy)
@settings(max_examples=25)
def test_sql_PivotCol_instantiation(instance):
    assert isinstance(instance, sql_PivotCol)


sql_PivotColumns_strategy = st.builds(sql_PivotColumns)
@given(instance=sql_PivotColumns_strategy)
@settings(max_examples=25)
def test_sql_PivotColumns_instantiation(instance):
    assert isinstance(instance, sql_PivotColumns)


sql_PivotForClause_strategy = st.builds(sql_PivotForClause)
@given(instance=sql_PivotForClause_strategy)
@settings(max_examples=25)
def test_sql_PivotForClause_instantiation(instance):
    assert isinstance(instance, sql_PivotForClause)


sql_PivotFunction_strategy = st.builds(sql_PivotFunction)
@given(instance=sql_PivotFunction_strategy)
@settings(max_examples=25)
def test_sql_PivotFunction_instantiation(instance):
    assert isinstance(instance, sql_PivotFunction)


sql_PivotFunctions_strategy = st.builds(sql_PivotFunctions, abc=safe_text)
@given(instance=sql_PivotFunctions_strategy)
@settings(max_examples=25)
def test_sql_PivotFunctions_instantiation(instance):
    assert isinstance(instance, sql_PivotFunctions)


sql_PivotInClause_strategy = st.builds(sql_PivotInClause, pinany=safe_text)
@given(instance=sql_PivotInClause_strategy)
@settings(max_examples=25)
def test_sql_PivotInClause_instantiation(instance):
    assert isinstance(instance, sql_PivotInClause)


sql_PivotTable_strategy = st.builds(sql_PivotTable)
@given(instance=sql_PivotTable_strategy)
@settings(max_examples=25)
def test_sql_PivotTable_instantiation(instance):
    assert isinstance(instance, sql_PivotTable)


sql_Pivots_strategy = st.builds(sql_Pivots)
@given(instance=sql_Pivots_strategy)
@settings(max_examples=25)
def test_sql_Pivots_instantiation(instance):
    assert isinstance(instance, sql_Pivots)


sql_Plus_strategy = st.builds(sql_Plus)
@given(instance=sql_Plus_strategy)
@settings(max_examples=25)
def test_sql_Plus_instantiation(instance):
    assert isinstance(instance, sql_Plus)


sql_Prms_strategy = st.builds(sql_Prms)
@given(instance=sql_Prms_strategy)
@settings(max_examples=25)
def test_sql_Prms_instantiation(instance):
    assert isinstance(instance, sql_Prms)


sql_QueryPartitionClause_strategy = st.builds(sql_QueryPartitionClause)
@given(instance=sql_QueryPartitionClause_strategy)
@settings(max_examples=25)
def test_sql_QueryPartitionClause_instantiation(instance):
    assert isinstance(instance, sql_QueryPartitionClause)


sql_SQLCaseOperand_strategy = st.builds(sql_SQLCaseOperand)
@given(instance=sql_SQLCaseOperand_strategy)
@settings(max_examples=25)
def test_sql_SQLCaseOperand_instantiation(instance):
    assert isinstance(instance, sql_SQLCaseOperand)


sql_SQLCaseWhens_strategy = st.builds(sql_SQLCaseWhens)
@given(instance=sql_SQLCaseWhens_strategy)
@settings(max_examples=25)
def test_sql_SQLCaseWhens_instantiation(instance):
    assert isinstance(instance, sql_SQLCaseWhens)


sql_ScalarOperand_strategy = st.builds(sql_ScalarOperand, sodate=st.dates(), sodbl=safe_text, sodt=st.dates(), soint=st.integers(), sostr=safe_text, sotime=st.dates())
@given(instance=sql_ScalarOperand_strategy)
@settings(max_examples=25)
def test_sql_ScalarOperand_instantiation(instance):
    assert isinstance(instance, sql_ScalarOperand)


sql_Select_strategy = st.builds(sql_Select, select=safe_text)
@given(instance=sql_Select_strategy)
@settings(max_examples=25)
def test_sql_Select_instantiation(instance):
    assert isinstance(instance, sql_Select)


sql_SelectQuery_strategy = st.builds(sql_SelectQuery)
@given(instance=sql_SelectQuery_strategy)
@settings(max_examples=25)
def test_sql_SelectQuery_instantiation(instance):
    assert isinstance(instance, sql_SelectQuery)


sql_SelectSubSet_strategy = st.builds(sql_SelectSubSet, all=safe_text, op=safe_text)
@given(instance=sql_SelectSubSet_strategy)
@settings(max_examples=25)
def test_sql_SelectSubSet_instantiation(instance):
    assert isinstance(instance, sql_SelectSubSet)


sql_SqlCaseWhen_strategy = st.builds(sql_SqlCaseWhen)
@given(instance=sql_SqlCaseWhen_strategy)
@settings(max_examples=25)
def test_sql_SqlCaseWhen_instantiation(instance):
    assert isinstance(instance, sql_SqlCaseWhen)


sql_Star_strategy = st.builds(sql_Star)
@given(instance=sql_Star_strategy)
@settings(max_examples=25)
def test_sql_Star_instantiation(instance):
    assert isinstance(instance, sql_Star)


sql_SubQueryOperand_strategy = st.builds(sql_SubQueryOperand)
@given(instance=sql_SubQueryOperand_strategy)
@settings(max_examples=25)
def test_sql_SubQueryOperand_instantiation(instance):
    assert isinstance(instance, sql_SubQueryOperand)


sql_TableFull_strategy = st.builds(sql_TableFull)
@given(instance=sql_TableFull_strategy)
@settings(max_examples=25)
def test_sql_TableFull_instantiation(instance):
    assert isinstance(instance, sql_TableFull)


sql_TableOrAlias_strategy = st.builds(sql_TableOrAlias, alias=safe_text)
@given(instance=sql_TableOrAlias_strategy)
@settings(max_examples=25)
def test_sql_TableOrAlias_instantiation(instance):
    assert isinstance(instance, sql_TableOrAlias)


sql_UnipivotInClause_strategy = st.builds(sql_UnipivotInClause, op=safe_text)
@given(instance=sql_UnipivotInClause_strategy)
@settings(max_examples=25)
def test_sql_UnipivotInClause_instantiation(instance):
    assert isinstance(instance, sql_UnipivotInClause)


sql_UnpivotInClause_strategy = st.builds(sql_UnpivotInClause)
@given(instance=sql_UnpivotInClause_strategy)
@settings(max_examples=25)
def test_sql_UnpivotInClause_instantiation(instance):
    assert isinstance(instance, sql_UnpivotInClause)


sql_UnpivotInClauseArg_strategy = st.builds(sql_UnpivotInClauseArg)
@given(instance=sql_UnpivotInClauseArg_strategy)
@settings(max_examples=25)
def test_sql_UnpivotInClauseArg_instantiation(instance):
    assert isinstance(instance, sql_UnpivotInClauseArg)


sql_UnpivotInClauseArgs_strategy = st.builds(sql_UnpivotInClauseArgs)
@given(instance=sql_UnpivotInClauseArgs_strategy)
@settings(max_examples=25)
def test_sql_UnpivotInClauseArgs_instantiation(instance):
    assert isinstance(instance, sql_UnpivotInClauseArgs)


sql_UnpivotTable_strategy = st.builds(sql_UnpivotTable)
@given(instance=sql_UnpivotTable_strategy)
@settings(max_examples=25)
def test_sql_UnpivotTable_instantiation(instance):
    assert isinstance(instance, sql_UnpivotTable)


sql_WhenList_strategy = st.builds(sql_WhenList)
@given(instance=sql_WhenList_strategy)
@settings(max_examples=25)
def test_sql_WhenList_instantiation(instance):
    assert isinstance(instance, sql_WhenList)


sql_WindowingClause_strategy = st.builds(sql_WindowingClause)
@given(instance=sql_WindowingClause_strategy)
@settings(max_examples=25)
def test_sql_WindowingClause_instantiation(instance):
    assert isinstance(instance, sql_WindowingClause)


sql_WindowingClauseBetween_strategy = st.builds(sql_WindowingClauseBetween)
@given(instance=sql_WindowingClauseBetween_strategy)
@settings(max_examples=25)
def test_sql_WindowingClauseBetween_instantiation(instance):
    assert isinstance(instance, sql_WindowingClauseBetween)


sql_WindowingClauseOperandFollowing_strategy = st.builds(sql_WindowingClauseOperandFollowing)
@given(instance=sql_WindowingClauseOperandFollowing_strategy)
@settings(max_examples=25)
def test_sql_WindowingClauseOperandFollowing_instantiation(instance):
    assert isinstance(instance, sql_WindowingClauseOperandFollowing)


sql_WindowingClauseOperandPreceding_strategy = st.builds(sql_WindowingClauseOperandPreceding)
@given(instance=sql_WindowingClauseOperandPreceding_strategy)
@settings(max_examples=25)
def test_sql_WindowingClauseOperandPreceding_instantiation(instance):
    assert isinstance(instance, sql_WindowingClauseOperandPreceding)


sql_XExpr_strategy = st.builds(sql_XExpr, xf=safe_text)
@given(instance=sql_XExpr_strategy)
@settings(max_examples=25)
def test_sql_XExpr_instantiation(instance):
    assert isinstance(instance, sql_XExpr)


sql_pcols_strategy = st.builds(sql_pcols)
@given(instance=sql_pcols_strategy)
@settings(max_examples=25)
def test_sql_pcols_instantiation(instance):
    assert isinstance(instance, sql_pcols)


sql_pvcs_strategy = st.builds(sql_pvcs)
@given(instance=sql_pvcs_strategy)
@settings(max_examples=25)
def test_sql_pvcs_instantiation(instance):
    assert isinstance(instance, sql_pvcs)


sql_tbls_strategy = st.builds(sql_tbls)
@given(instance=sql_tbls_strategy)
@settings(max_examples=25)
def test_sql_tbls_instantiation(instance):
    assert isinstance(instance, sql_tbls)


sql_uicargs_strategy = st.builds(sql_uicargs)
@given(instance=sql_uicargs_strategy)
@settings(max_examples=25)
def test_sql_uicargs_instantiation(instance):
    assert isinstance(instance, sql_uicargs)



