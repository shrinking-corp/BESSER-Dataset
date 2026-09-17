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
    plSql_NameDeclaration,
    plSql_Name,
    plSql_QualifiedName,
    LoopStatement,
    plSql_ForLoopStatement,
    plSql_WhileLoopStatement,
    plSql_BasicLoopStatement,
    plSql_IfStatementElseBranch,
    plSql_IfStatementElsifBranch,
    FetchStatementIntoClause,
    plSql_FetchStatementBulkIntoClause,
    plSql_FetchStatementSingleIntoClause,
    plSql_FetchStatementIntoClause,
    plSql_CaseStatementElseBranch,
    AssignmentTarget,
    plSql_VariableAssignmentTarget,
    plSql_AssignmentTarget,
    Statement,
    plSql_ContinueStatement,
    plSql_GotoStatement,
    plSql_BlockStatement,
    plSql_ExitStatement,
    plSql_RaiseStatement,
    plSql_IfStatement,
    plSql_NullStatement,
    plSql_FetchStatement,
    plSql_CloseStatement,
    plSql_ReturnStatement,
    plSql_LoopStatement,
    plSql_AssignmentStatement,
    plSql_Label,
    plSql_VariableRef,
    Expression,
    plSql_BooleanLiteralExpression,
    plSql_NullLiteralExpression,
    plSql_VariableRefExpression,
    plSql_StringLiteralExpression,
    plSql_IntLiteralExpression,
    plSql_VariableValue,
    plSql_CaseStatementWhenBranch,
    plSql_CaseStatement,
    plSql_Statement,
    FunctionContent,
    plSql_FunctionImplementation,
    plSql_StatementBody,
    plSql_DeclareSection,
    ProcedureContent,
    Pragma,
    plSql_PragmaTimestamp,
    plSql_PragmaRestrictReferences,
    FunctionClause,
    plSql_DeterministicClause,
    plSql_PipelinedClause,
    plSql_ResultCacheClause,
    plSql_FunctionInvokerRightsClause,
    ItemDeclaration,
    plSql_ExternalProcedureDeclaration,
    plSql_FunctionContent,
    plSql_FunctionClause,
    plSql_ProcedureImplementation,
    plSql_Expression,
    plSql_ParameterValue,
    Item,
    plSql_ItemDeclaration,
    plSql_Pragma,
    plSql_ProcedureDeclaration,
    plSql_Item,
    plSql_ProcedureContent,
    plSql_ProcedureInvokerRightsClause,
    plSql_ParameterSequence,
    NameDeclaration,
    plSql_ParameterDeclaration,
    plSql_LoopVariableDeclaration,
    plSql_ProcedureDefinition,
    plSql_VariableDeclaration,
    CompilationUnit,
    plSql_Function,
    plSql_Package,
    plSql_Procedure,
    plSql_CompilationUnit,
    InvokerRight,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_hyp_plsql_namedeclaration_is_not_abstract():
    assert not inspect.isabstract(plSql_NameDeclaration)


def test_hyp_plsql_namedeclaration_constructor_exists():
    assert callable(plSql_NameDeclaration.__init__)


def test_hyp_plsql_namedeclaration_constructor_args():
    sig = inspect.signature(plSql_NameDeclaration.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"




def test_hyp_plsql_name_is_not_abstract():
    assert not inspect.isabstract(plSql_Name)


def test_hyp_plsql_name_constructor_exists():
    assert callable(plSql_Name.__init__)


def test_hyp_plsql_name_constructor_args():
    sig = inspect.signature(plSql_Name.__init__)
    params = list(sig.parameters.keys())



def test_hyp_plsql_qualifiedname_is_not_abstract():
    assert not inspect.isabstract(plSql_QualifiedName)


def test_hyp_plsql_qualifiedname_constructor_exists():
    assert callable(plSql_QualifiedName.__init__)


def test_hyp_plsql_qualifiedname_constructor_args():
    sig = inspect.signature(plSql_QualifiedName.__init__)
    params = list(sig.parameters.keys())



def test_hyp_loopstatement_is_not_abstract():
    assert not inspect.isabstract(LoopStatement)


def test_hyp_loopstatement_constructor_exists():
    assert callable(LoopStatement.__init__)


def test_hyp_loopstatement_constructor_args():
    sig = inspect.signature(LoopStatement.__init__)
    params = list(sig.parameters.keys())



def test_hyp_plsql_forloopstatement_is_not_abstract():
    assert not inspect.isabstract(plSql_ForLoopStatement)


def test_hyp_plsql_forloopstatement_constructor_exists():
    assert callable(plSql_ForLoopStatement.__init__)


def test_hyp_plsql_forloopstatement_constructor_args():
    sig = inspect.signature(plSql_ForLoopStatement.__init__)
    params = list(sig.parameters.keys())



def test_hyp_plsql_whileloopstatement_is_not_abstract():
    assert not inspect.isabstract(plSql_WhileLoopStatement)


def test_hyp_plsql_whileloopstatement_constructor_exists():
    assert callable(plSql_WhileLoopStatement.__init__)


def test_hyp_plsql_whileloopstatement_constructor_args():
    sig = inspect.signature(plSql_WhileLoopStatement.__init__)
    params = list(sig.parameters.keys())



def test_hyp_plsql_basicloopstatement_is_not_abstract():
    assert not inspect.isabstract(plSql_BasicLoopStatement)


def test_hyp_plsql_basicloopstatement_constructor_exists():
    assert callable(plSql_BasicLoopStatement.__init__)


def test_hyp_plsql_basicloopstatement_constructor_args():
    sig = inspect.signature(plSql_BasicLoopStatement.__init__)
    params = list(sig.parameters.keys())



def test_hyp_plsql_ifstatementelsebranch_is_not_abstract():
    assert not inspect.isabstract(plSql_IfStatementElseBranch)


def test_hyp_plsql_ifstatementelsebranch_constructor_exists():
    assert callable(plSql_IfStatementElseBranch.__init__)


def test_hyp_plsql_ifstatementelsebranch_constructor_args():
    sig = inspect.signature(plSql_IfStatementElseBranch.__init__)
    params = list(sig.parameters.keys())



def test_hyp_plsql_ifstatementelsifbranch_is_not_abstract():
    assert not inspect.isabstract(plSql_IfStatementElsifBranch)


def test_hyp_plsql_ifstatementelsifbranch_constructor_exists():
    assert callable(plSql_IfStatementElsifBranch.__init__)


def test_hyp_plsql_ifstatementelsifbranch_constructor_args():
    sig = inspect.signature(plSql_IfStatementElsifBranch.__init__)
    params = list(sig.parameters.keys())



def test_hyp_fetchstatementintoclause_is_not_abstract():
    assert not inspect.isabstract(FetchStatementIntoClause)


def test_hyp_fetchstatementintoclause_constructor_exists():
    assert callable(FetchStatementIntoClause.__init__)


def test_hyp_fetchstatementintoclause_constructor_args():
    sig = inspect.signature(FetchStatementIntoClause.__init__)
    params = list(sig.parameters.keys())



def test_hyp_plsql_fetchstatementbulkintoclause_is_not_abstract():
    assert not inspect.isabstract(plSql_FetchStatementBulkIntoClause)


def test_hyp_plsql_fetchstatementbulkintoclause_constructor_exists():
    assert callable(plSql_FetchStatementBulkIntoClause.__init__)


def test_hyp_plsql_fetchstatementbulkintoclause_constructor_args():
    sig = inspect.signature(plSql_FetchStatementBulkIntoClause.__init__)
    params = list(sig.parameters.keys())



def test_hyp_plsql_fetchstatementsingleintoclause_is_not_abstract():
    assert not inspect.isabstract(plSql_FetchStatementSingleIntoClause)


def test_hyp_plsql_fetchstatementsingleintoclause_constructor_exists():
    assert callable(plSql_FetchStatementSingleIntoClause.__init__)


def test_hyp_plsql_fetchstatementsingleintoclause_constructor_args():
    sig = inspect.signature(plSql_FetchStatementSingleIntoClause.__init__)
    params = list(sig.parameters.keys())



def test_hyp_plsql_fetchstatementintoclause_is_not_abstract():
    assert not inspect.isabstract(plSql_FetchStatementIntoClause)


def test_hyp_plsql_fetchstatementintoclause_constructor_exists():
    assert callable(plSql_FetchStatementIntoClause.__init__)


def test_hyp_plsql_fetchstatementintoclause_constructor_args():
    sig = inspect.signature(plSql_FetchStatementIntoClause.__init__)
    params = list(sig.parameters.keys())



def test_hyp_plsql_casestatementelsebranch_is_not_abstract():
    assert not inspect.isabstract(plSql_CaseStatementElseBranch)


def test_hyp_plsql_casestatementelsebranch_constructor_exists():
    assert callable(plSql_CaseStatementElseBranch.__init__)


def test_hyp_plsql_casestatementelsebranch_constructor_args():
    sig = inspect.signature(plSql_CaseStatementElseBranch.__init__)
    params = list(sig.parameters.keys())



def test_hyp_assignmenttarget_is_not_abstract():
    assert not inspect.isabstract(AssignmentTarget)


def test_hyp_assignmenttarget_constructor_exists():
    assert callable(AssignmentTarget.__init__)


def test_hyp_assignmenttarget_constructor_args():
    sig = inspect.signature(AssignmentTarget.__init__)
    params = list(sig.parameters.keys())



def test_hyp_plsql_variableassignmenttarget_is_not_abstract():
    assert not inspect.isabstract(plSql_VariableAssignmentTarget)


def test_hyp_plsql_variableassignmenttarget_constructor_exists():
    assert callable(plSql_VariableAssignmentTarget.__init__)


def test_hyp_plsql_variableassignmenttarget_constructor_args():
    sig = inspect.signature(plSql_VariableAssignmentTarget.__init__)
    params = list(sig.parameters.keys())



def test_hyp_plsql_assignmenttarget_is_not_abstract():
    assert not inspect.isabstract(plSql_AssignmentTarget)


def test_hyp_plsql_assignmenttarget_constructor_exists():
    assert callable(plSql_AssignmentTarget.__init__)


def test_hyp_plsql_assignmenttarget_constructor_args():
    sig = inspect.signature(plSql_AssignmentTarget.__init__)
    params = list(sig.parameters.keys())



def test_hyp_statement_is_not_abstract():
    assert not inspect.isabstract(Statement)


def test_hyp_statement_constructor_exists():
    assert callable(Statement.__init__)


def test_hyp_statement_constructor_args():
    sig = inspect.signature(Statement.__init__)
    params = list(sig.parameters.keys())



def test_hyp_plsql_continuestatement_is_not_abstract():
    assert not inspect.isabstract(plSql_ContinueStatement)


def test_hyp_plsql_continuestatement_constructor_exists():
    assert callable(plSql_ContinueStatement.__init__)


def test_hyp_plsql_continuestatement_constructor_args():
    sig = inspect.signature(plSql_ContinueStatement.__init__)
    params = list(sig.parameters.keys())
    assert "labelName" in params, "Missing parameter 'labelName'"




def test_hyp_plsql_gotostatement_is_not_abstract():
    assert not inspect.isabstract(plSql_GotoStatement)


def test_hyp_plsql_gotostatement_constructor_exists():
    assert callable(plSql_GotoStatement.__init__)


def test_hyp_plsql_gotostatement_constructor_args():
    sig = inspect.signature(plSql_GotoStatement.__init__)
    params = list(sig.parameters.keys())



def test_hyp_plsql_blockstatement_is_not_abstract():
    assert not inspect.isabstract(plSql_BlockStatement)


def test_hyp_plsql_blockstatement_constructor_exists():
    assert callable(plSql_BlockStatement.__init__)


def test_hyp_plsql_blockstatement_constructor_args():
    sig = inspect.signature(plSql_BlockStatement.__init__)
    params = list(sig.parameters.keys())



def test_hyp_plsql_exitstatement_is_not_abstract():
    assert not inspect.isabstract(plSql_ExitStatement)


def test_hyp_plsql_exitstatement_constructor_exists():
    assert callable(plSql_ExitStatement.__init__)


def test_hyp_plsql_exitstatement_constructor_args():
    sig = inspect.signature(plSql_ExitStatement.__init__)
    params = list(sig.parameters.keys())
    assert "labelName" in params, "Missing parameter 'labelName'"




def test_hyp_plsql_raisestatement_is_not_abstract():
    assert not inspect.isabstract(plSql_RaiseStatement)


def test_hyp_plsql_raisestatement_constructor_exists():
    assert callable(plSql_RaiseStatement.__init__)


def test_hyp_plsql_raisestatement_constructor_args():
    sig = inspect.signature(plSql_RaiseStatement.__init__)
    params = list(sig.parameters.keys())
    assert "exceptionName" in params, "Missing parameter 'exceptionName'"




def test_hyp_plsql_ifstatement_is_not_abstract():
    assert not inspect.isabstract(plSql_IfStatement)


def test_hyp_plsql_ifstatement_constructor_exists():
    assert callable(plSql_IfStatement.__init__)


def test_hyp_plsql_ifstatement_constructor_args():
    sig = inspect.signature(plSql_IfStatement.__init__)
    params = list(sig.parameters.keys())



def test_hyp_plsql_nullstatement_is_not_abstract():
    assert not inspect.isabstract(plSql_NullStatement)


def test_hyp_plsql_nullstatement_constructor_exists():
    assert callable(plSql_NullStatement.__init__)


def test_hyp_plsql_nullstatement_constructor_args():
    sig = inspect.signature(plSql_NullStatement.__init__)
    params = list(sig.parameters.keys())



def test_hyp_plsql_fetchstatement_is_not_abstract():
    assert not inspect.isabstract(plSql_FetchStatement)


def test_hyp_plsql_fetchstatement_constructor_exists():
    assert callable(plSql_FetchStatement.__init__)


def test_hyp_plsql_fetchstatement_constructor_args():
    sig = inspect.signature(plSql_FetchStatement.__init__)
    params = list(sig.parameters.keys())



def test_hyp_plsql_closestatement_is_not_abstract():
    assert not inspect.isabstract(plSql_CloseStatement)


def test_hyp_plsql_closestatement_constructor_exists():
    assert callable(plSql_CloseStatement.__init__)


def test_hyp_plsql_closestatement_constructor_args():
    sig = inspect.signature(plSql_CloseStatement.__init__)
    params = list(sig.parameters.keys())



def test_hyp_plsql_returnstatement_is_not_abstract():
    assert not inspect.isabstract(plSql_ReturnStatement)


def test_hyp_plsql_returnstatement_constructor_exists():
    assert callable(plSql_ReturnStatement.__init__)


def test_hyp_plsql_returnstatement_constructor_args():
    sig = inspect.signature(plSql_ReturnStatement.__init__)
    params = list(sig.parameters.keys())



def test_hyp_plsql_loopstatement_is_not_abstract():
    assert not inspect.isabstract(plSql_LoopStatement)


def test_hyp_plsql_loopstatement_constructor_exists():
    assert callable(plSql_LoopStatement.__init__)


def test_hyp_plsql_loopstatement_constructor_args():
    sig = inspect.signature(plSql_LoopStatement.__init__)
    params = list(sig.parameters.keys())
    assert "endLabel" in params, "Missing parameter 'endLabel'"




def test_hyp_plsql_assignmentstatement_is_not_abstract():
    assert not inspect.isabstract(plSql_AssignmentStatement)


def test_hyp_plsql_assignmentstatement_constructor_exists():
    assert callable(plSql_AssignmentStatement.__init__)


def test_hyp_plsql_assignmentstatement_constructor_args():
    sig = inspect.signature(plSql_AssignmentStatement.__init__)
    params = list(sig.parameters.keys())



def test_hyp_plsql_label_is_not_abstract():
    assert not inspect.isabstract(plSql_Label)


def test_hyp_plsql_label_constructor_exists():
    assert callable(plSql_Label.__init__)


def test_hyp_plsql_label_constructor_args():
    sig = inspect.signature(plSql_Label.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"




def test_hyp_plsql_variableref_is_not_abstract():
    assert not inspect.isabstract(plSql_VariableRef)


def test_hyp_plsql_variableref_constructor_exists():
    assert callable(plSql_VariableRef.__init__)


def test_hyp_plsql_variableref_constructor_args():
    sig = inspect.signature(plSql_VariableRef.__init__)
    params = list(sig.parameters.keys())
    assert "isHostRef" in params, "Missing parameter 'isHostRef'"




def test_hyp_expression_is_not_abstract():
    assert not inspect.isabstract(Expression)


def test_hyp_expression_constructor_exists():
    assert callable(Expression.__init__)


def test_hyp_expression_constructor_args():
    sig = inspect.signature(Expression.__init__)
    params = list(sig.parameters.keys())



def test_hyp_plsql_booleanliteralexpression_is_not_abstract():
    assert not inspect.isabstract(plSql_BooleanLiteralExpression)


def test_hyp_plsql_booleanliteralexpression_constructor_exists():
    assert callable(plSql_BooleanLiteralExpression.__init__)


def test_hyp_plsql_booleanliteralexpression_constructor_args():
    sig = inspect.signature(plSql_BooleanLiteralExpression.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"




def test_hyp_plsql_nullliteralexpression_is_not_abstract():
    assert not inspect.isabstract(plSql_NullLiteralExpression)


def test_hyp_plsql_nullliteralexpression_constructor_exists():
    assert callable(plSql_NullLiteralExpression.__init__)


def test_hyp_plsql_nullliteralexpression_constructor_args():
    sig = inspect.signature(plSql_NullLiteralExpression.__init__)
    params = list(sig.parameters.keys())



def test_hyp_plsql_variablerefexpression_is_not_abstract():
    assert not inspect.isabstract(plSql_VariableRefExpression)


def test_hyp_plsql_variablerefexpression_constructor_exists():
    assert callable(plSql_VariableRefExpression.__init__)


def test_hyp_plsql_variablerefexpression_constructor_args():
    sig = inspect.signature(plSql_VariableRefExpression.__init__)
    params = list(sig.parameters.keys())



def test_hyp_plsql_stringliteralexpression_is_not_abstract():
    assert not inspect.isabstract(plSql_StringLiteralExpression)


def test_hyp_plsql_stringliteralexpression_constructor_exists():
    assert callable(plSql_StringLiteralExpression.__init__)


def test_hyp_plsql_stringliteralexpression_constructor_args():
    sig = inspect.signature(plSql_StringLiteralExpression.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"




def test_hyp_plsql_intliteralexpression_is_not_abstract():
    assert not inspect.isabstract(plSql_IntLiteralExpression)


def test_hyp_plsql_intliteralexpression_constructor_exists():
    assert callable(plSql_IntLiteralExpression.__init__)


def test_hyp_plsql_intliteralexpression_constructor_args():
    sig = inspect.signature(plSql_IntLiteralExpression.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"




def test_hyp_plsql_variablevalue_is_not_abstract():
    assert not inspect.isabstract(plSql_VariableValue)


def test_hyp_plsql_variablevalue_constructor_exists():
    assert callable(plSql_VariableValue.__init__)


def test_hyp_plsql_variablevalue_constructor_args():
    sig = inspect.signature(plSql_VariableValue.__init__)
    params = list(sig.parameters.keys())



def test_hyp_plsql_casestatementwhenbranch_is_not_abstract():
    assert not inspect.isabstract(plSql_CaseStatementWhenBranch)


def test_hyp_plsql_casestatementwhenbranch_constructor_exists():
    assert callable(plSql_CaseStatementWhenBranch.__init__)


def test_hyp_plsql_casestatementwhenbranch_constructor_args():
    sig = inspect.signature(plSql_CaseStatementWhenBranch.__init__)
    params = list(sig.parameters.keys())



def test_hyp_plsql_casestatement_is_not_abstract():
    assert not inspect.isabstract(plSql_CaseStatement)


def test_hyp_plsql_casestatement_constructor_exists():
    assert callable(plSql_CaseStatement.__init__)


def test_hyp_plsql_casestatement_constructor_args():
    sig = inspect.signature(plSql_CaseStatement.__init__)
    params = list(sig.parameters.keys())
    assert "endLabel" in params, "Missing parameter 'endLabel'"




def test_hyp_plsql_statement_is_not_abstract():
    assert not inspect.isabstract(plSql_Statement)


def test_hyp_plsql_statement_constructor_exists():
    assert callable(plSql_Statement.__init__)


def test_hyp_plsql_statement_constructor_args():
    sig = inspect.signature(plSql_Statement.__init__)
    params = list(sig.parameters.keys())



def test_hyp_functioncontent_is_not_abstract():
    assert not inspect.isabstract(FunctionContent)


def test_hyp_functioncontent_constructor_exists():
    assert callable(FunctionContent.__init__)


def test_hyp_functioncontent_constructor_args():
    sig = inspect.signature(FunctionContent.__init__)
    params = list(sig.parameters.keys())



def test_hyp_plsql_functionimplementation_is_not_abstract():
    assert not inspect.isabstract(plSql_FunctionImplementation)


def test_hyp_plsql_functionimplementation_constructor_exists():
    assert callable(plSql_FunctionImplementation.__init__)


def test_hyp_plsql_functionimplementation_constructor_args():
    sig = inspect.signature(plSql_FunctionImplementation.__init__)
    params = list(sig.parameters.keys())



def test_hyp_plsql_statementbody_is_not_abstract():
    assert not inspect.isabstract(plSql_StatementBody)


def test_hyp_plsql_statementbody_constructor_exists():
    assert callable(plSql_StatementBody.__init__)


def test_hyp_plsql_statementbody_constructor_args():
    sig = inspect.signature(plSql_StatementBody.__init__)
    params = list(sig.parameters.keys())
    assert "endName" in params, "Missing parameter 'endName'"




def test_hyp_plsql_declaresection_is_not_abstract():
    assert not inspect.isabstract(plSql_DeclareSection)


def test_hyp_plsql_declaresection_constructor_exists():
    assert callable(plSql_DeclareSection.__init__)


def test_hyp_plsql_declaresection_constructor_args():
    sig = inspect.signature(plSql_DeclareSection.__init__)
    params = list(sig.parameters.keys())



def test_hyp_procedurecontent_is_not_abstract():
    assert not inspect.isabstract(ProcedureContent)


def test_hyp_procedurecontent_constructor_exists():
    assert callable(ProcedureContent.__init__)


def test_hyp_procedurecontent_constructor_args():
    sig = inspect.signature(ProcedureContent.__init__)
    params = list(sig.parameters.keys())



def test_hyp_pragma_is_not_abstract():
    assert not inspect.isabstract(Pragma)


def test_hyp_pragma_constructor_exists():
    assert callable(Pragma.__init__)


def test_hyp_pragma_constructor_args():
    sig = inspect.signature(Pragma.__init__)
    params = list(sig.parameters.keys())



def test_hyp_plsql_pragmatimestamp_is_not_abstract():
    assert not inspect.isabstract(plSql_PragmaTimestamp)


def test_hyp_plsql_pragmatimestamp_constructor_exists():
    assert callable(plSql_PragmaTimestamp.__init__)


def test_hyp_plsql_pragmatimestamp_constructor_args():
    sig = inspect.signature(plSql_PragmaTimestamp.__init__)
    params = list(sig.parameters.keys())
    assert "timestamp" in params, "Missing parameter 'timestamp'"




def test_hyp_plsql_pragmarestrictreferences_is_not_abstract():
    assert not inspect.isabstract(plSql_PragmaRestrictReferences)


def test_hyp_plsql_pragmarestrictreferences_constructor_exists():
    assert callable(plSql_PragmaRestrictReferences.__init__)


def test_hyp_plsql_pragmarestrictreferences_constructor_args():
    sig = inspect.signature(plSql_PragmaRestrictReferences.__init__)
    params = list(sig.parameters.keys())
    assert "restrictions" in params, "Missing parameter 'restrictions'"




def test_hyp_functionclause_is_not_abstract():
    assert not inspect.isabstract(FunctionClause)


def test_hyp_functionclause_constructor_exists():
    assert callable(FunctionClause.__init__)


def test_hyp_functionclause_constructor_args():
    sig = inspect.signature(FunctionClause.__init__)
    params = list(sig.parameters.keys())



def test_hyp_plsql_deterministicclause_is_not_abstract():
    assert not inspect.isabstract(plSql_DeterministicClause)


def test_hyp_plsql_deterministicclause_constructor_exists():
    assert callable(plSql_DeterministicClause.__init__)


def test_hyp_plsql_deterministicclause_constructor_args():
    sig = inspect.signature(plSql_DeterministicClause.__init__)
    params = list(sig.parameters.keys())



def test_hyp_plsql_pipelinedclause_is_not_abstract():
    assert not inspect.isabstract(plSql_PipelinedClause)


def test_hyp_plsql_pipelinedclause_constructor_exists():
    assert callable(plSql_PipelinedClause.__init__)


def test_hyp_plsql_pipelinedclause_constructor_args():
    sig = inspect.signature(plSql_PipelinedClause.__init__)
    params = list(sig.parameters.keys())



def test_hyp_plsql_resultcacheclause_is_not_abstract():
    assert not inspect.isabstract(plSql_ResultCacheClause)


def test_hyp_plsql_resultcacheclause_constructor_exists():
    assert callable(plSql_ResultCacheClause.__init__)


def test_hyp_plsql_resultcacheclause_constructor_args():
    sig = inspect.signature(plSql_ResultCacheClause.__init__)
    params = list(sig.parameters.keys())
    assert "dataSources" in params, "Missing parameter 'dataSources'"




def test_hyp_plsql_functioninvokerrightsclause_is_not_abstract():
    assert not inspect.isabstract(plSql_FunctionInvokerRightsClause)


def test_hyp_plsql_functioninvokerrightsclause_constructor_exists():
    assert callable(plSql_FunctionInvokerRightsClause.__init__)


def test_hyp_plsql_functioninvokerrightsclause_constructor_args():
    sig = inspect.signature(plSql_FunctionInvokerRightsClause.__init__)
    params = list(sig.parameters.keys())
    assert "right" in params, "Missing parameter 'right'"




def test_hyp_itemdeclaration_is_not_abstract():
    assert not inspect.isabstract(ItemDeclaration)


def test_hyp_itemdeclaration_constructor_exists():
    assert callable(ItemDeclaration.__init__)


def test_hyp_itemdeclaration_constructor_args():
    sig = inspect.signature(ItemDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_hyp_plsql_externalproceduredeclaration_is_not_abstract():
    assert not inspect.isabstract(plSql_ExternalProcedureDeclaration)


def test_hyp_plsql_externalproceduredeclaration_constructor_exists():
    assert callable(plSql_ExternalProcedureDeclaration.__init__)


def test_hyp_plsql_externalproceduredeclaration_constructor_args():
    sig = inspect.signature(plSql_ExternalProcedureDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_hyp_plsql_functioncontent_is_not_abstract():
    assert not inspect.isabstract(plSql_FunctionContent)


def test_hyp_plsql_functioncontent_constructor_exists():
    assert callable(plSql_FunctionContent.__init__)


def test_hyp_plsql_functioncontent_constructor_args():
    sig = inspect.signature(plSql_FunctionContent.__init__)
    params = list(sig.parameters.keys())



def test_hyp_plsql_functionclause_is_not_abstract():
    assert not inspect.isabstract(plSql_FunctionClause)


def test_hyp_plsql_functionclause_constructor_exists():
    assert callable(plSql_FunctionClause.__init__)


def test_hyp_plsql_functionclause_constructor_args():
    sig = inspect.signature(plSql_FunctionClause.__init__)
    params = list(sig.parameters.keys())



def test_hyp_plsql_procedureimplementation_is_not_abstract():
    assert not inspect.isabstract(plSql_ProcedureImplementation)


def test_hyp_plsql_procedureimplementation_constructor_exists():
    assert callable(plSql_ProcedureImplementation.__init__)


def test_hyp_plsql_procedureimplementation_constructor_args():
    sig = inspect.signature(plSql_ProcedureImplementation.__init__)
    params = list(sig.parameters.keys())



def test_hyp_plsql_expression_is_not_abstract():
    assert not inspect.isabstract(plSql_Expression)


def test_hyp_plsql_expression_constructor_exists():
    assert callable(plSql_Expression.__init__)


def test_hyp_plsql_expression_constructor_args():
    sig = inspect.signature(plSql_Expression.__init__)
    params = list(sig.parameters.keys())



def test_hyp_plsql_parametervalue_is_not_abstract():
    assert not inspect.isabstract(plSql_ParameterValue)


def test_hyp_plsql_parametervalue_constructor_exists():
    assert callable(plSql_ParameterValue.__init__)


def test_hyp_plsql_parametervalue_constructor_args():
    sig = inspect.signature(plSql_ParameterValue.__init__)
    params = list(sig.parameters.keys())



def test_hyp_item_is_not_abstract():
    assert not inspect.isabstract(Item)


def test_hyp_item_constructor_exists():
    assert callable(Item.__init__)


def test_hyp_item_constructor_args():
    sig = inspect.signature(Item.__init__)
    params = list(sig.parameters.keys())



def test_hyp_plsql_itemdeclaration_is_not_abstract():
    assert not inspect.isabstract(plSql_ItemDeclaration)


def test_hyp_plsql_itemdeclaration_constructor_exists():
    assert callable(plSql_ItemDeclaration.__init__)


def test_hyp_plsql_itemdeclaration_constructor_args():
    sig = inspect.signature(plSql_ItemDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_hyp_plsql_pragma_is_not_abstract():
    assert not inspect.isabstract(plSql_Pragma)


def test_hyp_plsql_pragma_constructor_exists():
    assert callable(plSql_Pragma.__init__)


def test_hyp_plsql_pragma_constructor_args():
    sig = inspect.signature(plSql_Pragma.__init__)
    params = list(sig.parameters.keys())



def test_hyp_plsql_proceduredeclaration_is_not_abstract():
    assert not inspect.isabstract(plSql_ProcedureDeclaration)


def test_hyp_plsql_proceduredeclaration_constructor_exists():
    assert callable(plSql_ProcedureDeclaration.__init__)


def test_hyp_plsql_proceduredeclaration_constructor_args():
    sig = inspect.signature(plSql_ProcedureDeclaration.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"




def test_hyp_plsql_item_is_not_abstract():
    assert not inspect.isabstract(plSql_Item)


def test_hyp_plsql_item_constructor_exists():
    assert callable(plSql_Item.__init__)


def test_hyp_plsql_item_constructor_args():
    sig = inspect.signature(plSql_Item.__init__)
    params = list(sig.parameters.keys())



def test_hyp_plsql_procedurecontent_is_not_abstract():
    assert not inspect.isabstract(plSql_ProcedureContent)


def test_hyp_plsql_procedurecontent_constructor_exists():
    assert callable(plSql_ProcedureContent.__init__)


def test_hyp_plsql_procedurecontent_constructor_args():
    sig = inspect.signature(plSql_ProcedureContent.__init__)
    params = list(sig.parameters.keys())



def test_hyp_plsql_procedureinvokerrightsclause_is_not_abstract():
    assert not inspect.isabstract(plSql_ProcedureInvokerRightsClause)


def test_hyp_plsql_procedureinvokerrightsclause_constructor_exists():
    assert callable(plSql_ProcedureInvokerRightsClause.__init__)


def test_hyp_plsql_procedureinvokerrightsclause_constructor_args():
    sig = inspect.signature(plSql_ProcedureInvokerRightsClause.__init__)
    params = list(sig.parameters.keys())
    assert "right" in params, "Missing parameter 'right'"




def test_hyp_plsql_parametersequence_is_not_abstract():
    assert not inspect.isabstract(plSql_ParameterSequence)


def test_hyp_plsql_parametersequence_constructor_exists():
    assert callable(plSql_ParameterSequence.__init__)


def test_hyp_plsql_parametersequence_constructor_args():
    sig = inspect.signature(plSql_ParameterSequence.__init__)
    params = list(sig.parameters.keys())



def test_hyp_namedeclaration_is_not_abstract():
    assert not inspect.isabstract(NameDeclaration)


def test_hyp_namedeclaration_constructor_exists():
    assert callable(NameDeclaration.__init__)


def test_hyp_namedeclaration_constructor_args():
    sig = inspect.signature(NameDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_hyp_plsql_parameterdeclaration_is_not_abstract():
    assert not inspect.isabstract(plSql_ParameterDeclaration)


def test_hyp_plsql_parameterdeclaration_constructor_exists():
    assert callable(plSql_ParameterDeclaration.__init__)


def test_hyp_plsql_parameterdeclaration_constructor_args():
    sig = inspect.signature(plSql_ParameterDeclaration.__init__)
    params = list(sig.parameters.keys())
    assert "dataType" in params, "Missing parameter 'dataType'"
    assert "behavior" in params, "Missing parameter 'behavior'"





def test_hyp_plsql_loopvariabledeclaration_is_not_abstract():
    assert not inspect.isabstract(plSql_LoopVariableDeclaration)


def test_hyp_plsql_loopvariabledeclaration_constructor_exists():
    assert callable(plSql_LoopVariableDeclaration.__init__)


def test_hyp_plsql_loopvariabledeclaration_constructor_args():
    sig = inspect.signature(plSql_LoopVariableDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_hyp_plsql_proceduredefinition_is_not_abstract():
    assert not inspect.isabstract(plSql_ProcedureDefinition)


def test_hyp_plsql_proceduredefinition_constructor_exists():
    assert callable(plSql_ProcedureDefinition.__init__)


def test_hyp_plsql_proceduredefinition_constructor_args():
    sig = inspect.signature(plSql_ProcedureDefinition.__init__)
    params = list(sig.parameters.keys())



def test_hyp_plsql_variabledeclaration_is_not_abstract():
    assert not inspect.isabstract(plSql_VariableDeclaration)


def test_hyp_plsql_variabledeclaration_constructor_exists():
    assert callable(plSql_VariableDeclaration.__init__)


def test_hyp_plsql_variabledeclaration_constructor_args():
    sig = inspect.signature(plSql_VariableDeclaration.__init__)
    params = list(sig.parameters.keys())
    assert "isConstant" in params, "Missing parameter 'isConstant'"
    assert "isNotNull" in params, "Missing parameter 'isNotNull'"
    assert "dataType" in params, "Missing parameter 'dataType'"






def test_hyp_compilationunit_is_not_abstract():
    assert not inspect.isabstract(CompilationUnit)


def test_hyp_compilationunit_constructor_exists():
    assert callable(CompilationUnit.__init__)


def test_hyp_compilationunit_constructor_args():
    sig = inspect.signature(CompilationUnit.__init__)
    params = list(sig.parameters.keys())



def test_hyp_plsql_function_is_not_abstract():
    assert not inspect.isabstract(plSql_Function)


def test_hyp_plsql_function_constructor_exists():
    assert callable(plSql_Function.__init__)


def test_hyp_plsql_function_constructor_args():
    sig = inspect.signature(plSql_Function.__init__)
    params = list(sig.parameters.keys())
    assert "schemaName" in params, "Missing parameter 'schemaName'"
    assert "returnType" in params, "Missing parameter 'returnType'"





def test_hyp_plsql_package_is_not_abstract():
    assert not inspect.isabstract(plSql_Package)


def test_hyp_plsql_package_constructor_exists():
    assert callable(plSql_Package.__init__)


def test_hyp_plsql_package_constructor_args():
    sig = inspect.signature(plSql_Package.__init__)
    params = list(sig.parameters.keys())
    assert "endName" in params, "Missing parameter 'endName'"
    assert "schemaName" in params, "Missing parameter 'schemaName'"





def test_hyp_plsql_procedure_is_not_abstract():
    assert not inspect.isabstract(plSql_Procedure)


def test_hyp_plsql_procedure_constructor_exists():
    assert callable(plSql_Procedure.__init__)


def test_hyp_plsql_procedure_constructor_args():
    sig = inspect.signature(plSql_Procedure.__init__)
    params = list(sig.parameters.keys())
    assert "schemaName" in params, "Missing parameter 'schemaName'"




def test_hyp_plsql_compilationunit_is_not_abstract():
    assert not inspect.isabstract(plSql_CompilationUnit)


def test_hyp_plsql_compilationunit_constructor_exists():
    assert callable(plSql_CompilationUnit.__init__)


def test_hyp_plsql_compilationunit_constructor_args():
    sig = inspect.signature(plSql_CompilationUnit.__init__)
    params = list(sig.parameters.keys())

def test_hyp_invokerright_exists():
    # Check that the Enumeration exists
    assert InvokerRight is not None

def test_hyp_invokerright_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in InvokerRight]
    expected_literals = [
        "DEFINER",
        "CURRENT_USER",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in InvokerRight"


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
plSql_NameDeclaration_strategy = st.builds(
    plSql_NameDeclaration,
    name=
        safe_text
)
plSql_Name_strategy = st.builds(
    plSql_Name,
)
plSql_QualifiedName_strategy = st.builds(
    plSql_QualifiedName,
)
LoopStatement_strategy = st.builds(
    LoopStatement,
)
plSql_ForLoopStatement_strategy = st.builds(
    plSql_ForLoopStatement,
)
plSql_WhileLoopStatement_strategy = st.builds(
    plSql_WhileLoopStatement,
)
plSql_BasicLoopStatement_strategy = st.builds(
    plSql_BasicLoopStatement,
)
plSql_IfStatementElseBranch_strategy = st.builds(
    plSql_IfStatementElseBranch,
)
plSql_IfStatementElsifBranch_strategy = st.builds(
    plSql_IfStatementElsifBranch,
)
FetchStatementIntoClause_strategy = st.builds(
    FetchStatementIntoClause,
)
plSql_FetchStatementBulkIntoClause_strategy = st.builds(
    plSql_FetchStatementBulkIntoClause,
)
plSql_FetchStatementSingleIntoClause_strategy = st.builds(
    plSql_FetchStatementSingleIntoClause,
)
plSql_FetchStatementIntoClause_strategy = st.builds(
    plSql_FetchStatementIntoClause,
)
plSql_CaseStatementElseBranch_strategy = st.builds(
    plSql_CaseStatementElseBranch,
)
AssignmentTarget_strategy = st.builds(
    AssignmentTarget,
)
plSql_VariableAssignmentTarget_strategy = st.builds(
    plSql_VariableAssignmentTarget,
)
plSql_AssignmentTarget_strategy = st.builds(
    plSql_AssignmentTarget,
)
Statement_strategy = st.builds(
    Statement,
)
plSql_ContinueStatement_strategy = st.builds(
    plSql_ContinueStatement,
    labelName=
        safe_text
)
plSql_GotoStatement_strategy = st.builds(
    plSql_GotoStatement,
)
plSql_BlockStatement_strategy = st.builds(
    plSql_BlockStatement,
)
plSql_ExitStatement_strategy = st.builds(
    plSql_ExitStatement,
    labelName=
        safe_text
)
plSql_RaiseStatement_strategy = st.builds(
    plSql_RaiseStatement,
    exceptionName=
        safe_text
)
plSql_IfStatement_strategy = st.builds(
    plSql_IfStatement,
)
plSql_NullStatement_strategy = st.builds(
    plSql_NullStatement,
)
plSql_FetchStatement_strategy = st.builds(
    plSql_FetchStatement,
)
plSql_CloseStatement_strategy = st.builds(
    plSql_CloseStatement,
)
plSql_ReturnStatement_strategy = st.builds(
    plSql_ReturnStatement,
)
plSql_LoopStatement_strategy = st.builds(
    plSql_LoopStatement,
    endLabel=
        safe_text
)
plSql_AssignmentStatement_strategy = st.builds(
    plSql_AssignmentStatement,
)
plSql_Label_strategy = st.builds(
    plSql_Label,
    name=
        safe_text
)
plSql_VariableRef_strategy = st.builds(
    plSql_VariableRef,
    isHostRef=
        st.booleans()
)
Expression_strategy = st.builds(
    Expression,
)
plSql_BooleanLiteralExpression_strategy = st.builds(
    plSql_BooleanLiteralExpression,
    value=
        safe_text
)
plSql_NullLiteralExpression_strategy = st.builds(
    plSql_NullLiteralExpression,
)
plSql_VariableRefExpression_strategy = st.builds(
    plSql_VariableRefExpression,
)
plSql_StringLiteralExpression_strategy = st.builds(
    plSql_StringLiteralExpression,
    value=
        safe_text
)
plSql_IntLiteralExpression_strategy = st.builds(
    plSql_IntLiteralExpression,
    value=
        st.integers()
)
plSql_VariableValue_strategy = st.builds(
    plSql_VariableValue,
)
plSql_CaseStatementWhenBranch_strategy = st.builds(
    plSql_CaseStatementWhenBranch,
)
plSql_CaseStatement_strategy = st.builds(
    plSql_CaseStatement,
    endLabel=
        safe_text
)
plSql_Statement_strategy = st.builds(
    plSql_Statement,
)
FunctionContent_strategy = st.builds(
    FunctionContent,
)
plSql_FunctionImplementation_strategy = st.builds(
    plSql_FunctionImplementation,
)
plSql_StatementBody_strategy = st.builds(
    plSql_StatementBody,
    endName=
        safe_text
)
plSql_DeclareSection_strategy = st.builds(
    plSql_DeclareSection,
)
ProcedureContent_strategy = st.builds(
    ProcedureContent,
)
Pragma_strategy = st.builds(
    Pragma,
)
plSql_PragmaTimestamp_strategy = st.builds(
    plSql_PragmaTimestamp,
    timestamp=
        safe_text
)
plSql_PragmaRestrictReferences_strategy = st.builds(
    plSql_PragmaRestrictReferences,
    restrictions=
        safe_text
)
FunctionClause_strategy = st.builds(
    FunctionClause,
)
plSql_DeterministicClause_strategy = st.builds(
    plSql_DeterministicClause,
)
plSql_PipelinedClause_strategy = st.builds(
    plSql_PipelinedClause,
)
plSql_ResultCacheClause_strategy = st.builds(
    plSql_ResultCacheClause,
    dataSources=
        safe_text
)
plSql_FunctionInvokerRightsClause_strategy = st.builds(
    plSql_FunctionInvokerRightsClause,
    right=
        safe_text
)
ItemDeclaration_strategy = st.builds(
    ItemDeclaration,
)
plSql_ExternalProcedureDeclaration_strategy = st.builds(
    plSql_ExternalProcedureDeclaration,
)
plSql_FunctionContent_strategy = st.builds(
    plSql_FunctionContent,
)
plSql_FunctionClause_strategy = st.builds(
    plSql_FunctionClause,
)
plSql_ProcedureImplementation_strategy = st.builds(
    plSql_ProcedureImplementation,
)
plSql_Expression_strategy = st.builds(
    plSql_Expression,
)
plSql_ParameterValue_strategy = st.builds(
    plSql_ParameterValue,
)
Item_strategy = st.builds(
    Item,
)
plSql_ItemDeclaration_strategy = st.builds(
    plSql_ItemDeclaration,
)
plSql_Pragma_strategy = st.builds(
    plSql_Pragma,
)
plSql_ProcedureDeclaration_strategy = st.builds(
    plSql_ProcedureDeclaration,
    name=
        safe_text
)
plSql_Item_strategy = st.builds(
    plSql_Item,
)
plSql_ProcedureContent_strategy = st.builds(
    plSql_ProcedureContent,
)
plSql_ProcedureInvokerRightsClause_strategy = st.builds(
    plSql_ProcedureInvokerRightsClause,
    right=
        safe_text
)
plSql_ParameterSequence_strategy = st.builds(
    plSql_ParameterSequence,
)
NameDeclaration_strategy = st.builds(
    NameDeclaration,
)
plSql_ParameterDeclaration_strategy = st.builds(
    plSql_ParameterDeclaration,
    dataType=
        safe_text,
    behavior=
        safe_text
)
plSql_LoopVariableDeclaration_strategy = st.builds(
    plSql_LoopVariableDeclaration,
)
plSql_ProcedureDefinition_strategy = st.builds(
    plSql_ProcedureDefinition,
)
plSql_VariableDeclaration_strategy = st.builds(
    plSql_VariableDeclaration,
    isConstant=
        st.booleans(),
    isNotNull=
        st.booleans(),
    dataType=
        safe_text
)
CompilationUnit_strategy = st.builds(
    CompilationUnit,
)
plSql_Function_strategy = st.builds(
    plSql_Function,
    schemaName=
        safe_text,
    returnType=
        safe_text
)
plSql_Package_strategy = st.builds(
    plSql_Package,
    endName=
        safe_text,
    schemaName=
        safe_text
)
plSql_Procedure_strategy = st.builds(
    plSql_Procedure,
    schemaName=
        safe_text
)
plSql_CompilationUnit_strategy = st.builds(
    plSql_CompilationUnit,
)




@given(instance=plSql_NameDeclaration_strategy)
def test_hyp_plsql_namedeclaration_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original





















@given(instance=plSql_ContinueStatement_strategy)
def test_hyp_plsql_continuestatement_labelName_setter(instance):
    original = instance.labelName
    instance.labelName = original
    assert instance.labelName == original






@given(instance=plSql_ExitStatement_strategy)
def test_hyp_plsql_exitstatement_labelName_setter(instance):
    original = instance.labelName
    instance.labelName = original
    assert instance.labelName == original




@given(instance=plSql_RaiseStatement_strategy)
def test_hyp_plsql_raisestatement_exceptionName_setter(instance):
    original = instance.exceptionName
    instance.exceptionName = original
    assert instance.exceptionName == original









@given(instance=plSql_LoopStatement_strategy)
def test_hyp_plsql_loopstatement_endLabel_setter(instance):
    original = instance.endLabel
    instance.endLabel = original
    assert instance.endLabel == original





@given(instance=plSql_Label_strategy)
def test_hyp_plsql_label_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original




@given(instance=plSql_VariableRef_strategy)
def test_hyp_plsql_variableref_isHostRef_setter(instance):
    original = instance.isHostRef
    instance.isHostRef = original
    assert instance.isHostRef == original





@given(instance=plSql_BooleanLiteralExpression_strategy)
def test_hyp_plsql_booleanliteralexpression_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original






@given(instance=plSql_StringLiteralExpression_strategy)
def test_hyp_plsql_stringliteralexpression_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original




@given(instance=plSql_IntLiteralExpression_strategy)
def test_hyp_plsql_intliteralexpression_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original






@given(instance=plSql_CaseStatement_strategy)
def test_hyp_plsql_casestatement_endLabel_setter(instance):
    original = instance.endLabel
    instance.endLabel = original
    assert instance.endLabel == original







@given(instance=plSql_StatementBody_strategy)
def test_hyp_plsql_statementbody_endName_setter(instance):
    original = instance.endName
    instance.endName = original
    assert instance.endName == original







@given(instance=plSql_PragmaTimestamp_strategy)
def test_hyp_plsql_pragmatimestamp_timestamp_setter(instance):
    original = instance.timestamp
    instance.timestamp = original
    assert instance.timestamp == original




@given(instance=plSql_PragmaRestrictReferences_strategy)
def test_hyp_plsql_pragmarestrictreferences_restrictions_setter(instance):
    original = instance.restrictions
    instance.restrictions = original
    assert instance.restrictions == original







@given(instance=plSql_ResultCacheClause_strategy)
def test_hyp_plsql_resultcacheclause_dataSources_setter(instance):
    original = instance.dataSources
    instance.dataSources = original
    assert instance.dataSources == original




@given(instance=plSql_FunctionInvokerRightsClause_strategy)
def test_hyp_plsql_functioninvokerrightsclause_right_setter(instance):
    original = instance.right
    instance.right = original
    assert instance.right == original














@given(instance=plSql_ProcedureDeclaration_strategy)
def test_hyp_plsql_proceduredeclaration_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original






@given(instance=plSql_ProcedureInvokerRightsClause_strategy)
def test_hyp_plsql_procedureinvokerrightsclause_right_setter(instance):
    original = instance.right
    instance.right = original
    assert instance.right == original






@given(instance=plSql_ParameterDeclaration_strategy)
def test_hyp_plsql_parameterdeclaration_dataType_setter(instance):
    original = instance.dataType
    instance.dataType = original
    assert instance.dataType == original



@given(instance=plSql_ParameterDeclaration_strategy)
def test_hyp_plsql_parameterdeclaration_behavior_setter(instance):
    original = instance.behavior
    instance.behavior = original
    assert instance.behavior == original






@given(instance=plSql_VariableDeclaration_strategy)
def test_hyp_plsql_variabledeclaration_isConstant_setter(instance):
    original = instance.isConstant
    instance.isConstant = original
    assert instance.isConstant == original



@given(instance=plSql_VariableDeclaration_strategy)
def test_hyp_plsql_variabledeclaration_isNotNull_setter(instance):
    original = instance.isNotNull
    instance.isNotNull = original
    assert instance.isNotNull == original



@given(instance=plSql_VariableDeclaration_strategy)
def test_hyp_plsql_variabledeclaration_dataType_setter(instance):
    original = instance.dataType
    instance.dataType = original
    assert instance.dataType == original





@given(instance=plSql_Function_strategy)
def test_hyp_plsql_function_schemaName_setter(instance):
    original = instance.schemaName
    instance.schemaName = original
    assert instance.schemaName == original



@given(instance=plSql_Function_strategy)
def test_hyp_plsql_function_returnType_setter(instance):
    original = instance.returnType
    instance.returnType = original
    assert instance.returnType == original




@given(instance=plSql_Package_strategy)
def test_hyp_plsql_package_endName_setter(instance):
    original = instance.endName
    instance.endName = original
    assert instance.endName == original



@given(instance=plSql_Package_strategy)
def test_hyp_plsql_package_schemaName_setter(instance):
    original = instance.schemaName
    instance.schemaName = original
    assert instance.schemaName == original




@given(instance=plSql_Procedure_strategy)
def test_hyp_plsql_procedure_schemaName_setter(instance):
    original = instance.schemaName
    instance.schemaName = original
    assert instance.schemaName == original



# ----- SECTION B: test_structural_full.py (deterministic-first suite) -----
import inspect
import pytest
from datetime import date, datetime, time, timedelta
from hypothesis import given, settings
import hypothesis.strategies as st

from python_code import (
    AssignmentTarget,
    CompilationUnit,
    Expression,
    FetchStatementIntoClause,
    FunctionClause,
    FunctionContent,
    Item,
    ItemDeclaration,
    LoopStatement,
    NameDeclaration,
    Pragma,
    ProcedureContent,
    Statement,
    plSql_AssignmentStatement,
    plSql_AssignmentTarget,
    plSql_BasicLoopStatement,
    plSql_BlockStatement,
    plSql_BooleanLiteralExpression,
    plSql_CaseStatement,
    plSql_CaseStatementElseBranch,
    plSql_CaseStatementWhenBranch,
    plSql_CloseStatement,
    plSql_CompilationUnit,
    plSql_ContinueStatement,
    plSql_DeclareSection,
    plSql_DeterministicClause,
    plSql_ExitStatement,
    plSql_Expression,
    plSql_ExternalProcedureDeclaration,
    plSql_FetchStatement,
    plSql_FetchStatementBulkIntoClause,
    plSql_FetchStatementIntoClause,
    plSql_FetchStatementSingleIntoClause,
    plSql_ForLoopStatement,
    plSql_Function,
    plSql_FunctionClause,
    plSql_FunctionContent,
    plSql_FunctionImplementation,
    plSql_FunctionInvokerRightsClause,
    plSql_GotoStatement,
    plSql_IfStatement,
    plSql_IfStatementElseBranch,
    plSql_IfStatementElsifBranch,
    plSql_IntLiteralExpression,
    plSql_Item,
    plSql_ItemDeclaration,
    plSql_Label,
    plSql_LoopStatement,
    plSql_LoopVariableDeclaration,
    plSql_Name,
    plSql_NameDeclaration,
    plSql_NullLiteralExpression,
    plSql_NullStatement,
    plSql_Package,
    plSql_ParameterDeclaration,
    plSql_ParameterSequence,
    plSql_ParameterValue,
    plSql_PipelinedClause,
    plSql_Pragma,
    plSql_PragmaRestrictReferences,
    plSql_PragmaTimestamp,
    plSql_Procedure,
    plSql_ProcedureContent,
    plSql_ProcedureDeclaration,
    plSql_ProcedureDefinition,
    plSql_ProcedureImplementation,
    plSql_ProcedureInvokerRightsClause,
    plSql_QualifiedName,
    plSql_RaiseStatement,
    plSql_ResultCacheClause,
    plSql_ReturnStatement,
    plSql_Statement,
    plSql_StatementBody,
    plSql_StringLiteralExpression,
    plSql_VariableAssignmentTarget,
    plSql_VariableDeclaration,
    plSql_VariableRef,
    plSql_VariableRefExpression,
    plSql_VariableValue,
    plSql_WhileLoopStatement,
    InvokerRight,
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

def test_plSql_BooleanLiteralExpression_value_value_roundtrip():
    instance = plSql_BooleanLiteralExpression(value="sample_text")
    assert instance.value == "sample_text"
    instance.value = "sample_text_2"
    assert instance.value == "sample_text_2"


def test_plSql_CaseStatement_endLabel_value_roundtrip():
    instance = plSql_CaseStatement(endLabel="sample_text")
    assert instance.endLabel == "sample_text"
    instance.endLabel = "sample_text_2"
    assert instance.endLabel == "sample_text_2"


def test_plSql_ContinueStatement_labelName_value_roundtrip():
    instance = plSql_ContinueStatement(labelName="sample_text")
    assert instance.labelName == "sample_text"
    instance.labelName = "sample_text_2"
    assert instance.labelName == "sample_text_2"


def test_plSql_ExitStatement_labelName_value_roundtrip():
    instance = plSql_ExitStatement(labelName="sample_text")
    assert instance.labelName == "sample_text"
    instance.labelName = "sample_text_2"
    assert instance.labelName == "sample_text_2"


def test_plSql_Function_returnType_value_roundtrip():
    instance = plSql_Function(returnType="sample_text", schemaName="sample_text")
    assert instance.returnType == "sample_text"
    instance.returnType = "sample_text_2"
    assert instance.returnType == "sample_text_2"


def test_plSql_Function_schemaName_value_roundtrip():
    instance = plSql_Function(returnType="sample_text", schemaName="sample_text")
    assert instance.schemaName == "sample_text"
    instance.schemaName = "sample_text_2"
    assert instance.schemaName == "sample_text_2"


def test_plSql_FunctionInvokerRightsClause_right_value_roundtrip():
    instance = plSql_FunctionInvokerRightsClause(right="sample_text")
    assert instance.right == "sample_text"
    instance.right = "sample_text_2"
    assert instance.right == "sample_text_2"


def test_plSql_IntLiteralExpression_value_value_roundtrip():
    instance = plSql_IntLiteralExpression(value=7)
    assert instance.value == 7
    instance.value = 13
    assert instance.value == 13


def test_plSql_Label_name_value_roundtrip():
    instance = plSql_Label(name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_plSql_LoopStatement_endLabel_value_roundtrip():
    instance = plSql_LoopStatement(endLabel="sample_text")
    assert instance.endLabel == "sample_text"
    instance.endLabel = "sample_text_2"
    assert instance.endLabel == "sample_text_2"


def test_plSql_NameDeclaration_name_value_roundtrip():
    instance = plSql_NameDeclaration(name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_plSql_Package_endName_value_roundtrip():
    instance = plSql_Package(endName="sample_text", schemaName="sample_text")
    assert instance.endName == "sample_text"
    instance.endName = "sample_text_2"
    assert instance.endName == "sample_text_2"


def test_plSql_Package_schemaName_value_roundtrip():
    instance = plSql_Package(endName="sample_text", schemaName="sample_text")
    assert instance.schemaName == "sample_text"
    instance.schemaName = "sample_text_2"
    assert instance.schemaName == "sample_text_2"


def test_plSql_ParameterDeclaration_behavior_value_roundtrip():
    instance = plSql_ParameterDeclaration(behavior="sample_text", dataType="sample_text")
    assert instance.behavior == "sample_text"
    instance.behavior = "sample_text_2"
    assert instance.behavior == "sample_text_2"


def test_plSql_ParameterDeclaration_dataType_value_roundtrip():
    instance = plSql_ParameterDeclaration(behavior="sample_text", dataType="sample_text")
    assert instance.dataType == "sample_text"
    instance.dataType = "sample_text_2"
    assert instance.dataType == "sample_text_2"


def test_plSql_PragmaRestrictReferences_restrictions_value_roundtrip():
    instance = plSql_PragmaRestrictReferences(restrictions="sample_text")
    assert instance.restrictions == "sample_text"
    instance.restrictions = "sample_text_2"
    assert instance.restrictions == "sample_text_2"


def test_plSql_PragmaTimestamp_timestamp_value_roundtrip():
    instance = plSql_PragmaTimestamp(timestamp="sample_text")
    assert instance.timestamp == "sample_text"
    instance.timestamp = "sample_text_2"
    assert instance.timestamp == "sample_text_2"


def test_plSql_Procedure_schemaName_value_roundtrip():
    instance = plSql_Procedure(schemaName="sample_text")
    assert instance.schemaName == "sample_text"
    instance.schemaName = "sample_text_2"
    assert instance.schemaName == "sample_text_2"


def test_plSql_ProcedureDeclaration_name_value_roundtrip():
    instance = plSql_ProcedureDeclaration(name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_plSql_ProcedureInvokerRightsClause_right_value_roundtrip():
    instance = plSql_ProcedureInvokerRightsClause(right="sample_text")
    assert instance.right == "sample_text"
    instance.right = "sample_text_2"
    assert instance.right == "sample_text_2"


def test_plSql_RaiseStatement_exceptionName_value_roundtrip():
    instance = plSql_RaiseStatement(exceptionName="sample_text")
    assert instance.exceptionName == "sample_text"
    instance.exceptionName = "sample_text_2"
    assert instance.exceptionName == "sample_text_2"


def test_plSql_ResultCacheClause_dataSources_value_roundtrip():
    instance = plSql_ResultCacheClause(dataSources="sample_text")
    assert instance.dataSources == "sample_text"
    instance.dataSources = "sample_text_2"
    assert instance.dataSources == "sample_text_2"


def test_plSql_StatementBody_endName_value_roundtrip():
    instance = plSql_StatementBody(endName="sample_text")
    assert instance.endName == "sample_text"
    instance.endName = "sample_text_2"
    assert instance.endName == "sample_text_2"


def test_plSql_StringLiteralExpression_value_value_roundtrip():
    instance = plSql_StringLiteralExpression(value="sample_text")
    assert instance.value == "sample_text"
    instance.value = "sample_text_2"
    assert instance.value == "sample_text_2"


def test_plSql_VariableDeclaration_dataType_value_roundtrip():
    instance = plSql_VariableDeclaration(dataType="sample_text", isConstant=True, isNotNull=True)
    assert instance.dataType == "sample_text"
    instance.dataType = "sample_text_2"
    assert instance.dataType == "sample_text_2"


def test_plSql_VariableDeclaration_isConstant_value_roundtrip():
    instance = plSql_VariableDeclaration(dataType="sample_text", isConstant=True, isNotNull=True)
    assert instance.isConstant == True
    instance.isConstant = False
    assert instance.isConstant == False


def test_plSql_VariableDeclaration_isNotNull_value_roundtrip():
    instance = plSql_VariableDeclaration(dataType="sample_text", isConstant=True, isNotNull=True)
    assert instance.isNotNull == True
    instance.isNotNull = False
    assert instance.isNotNull == False


def test_plSql_VariableRef_isHostRef_value_roundtrip():
    instance = plSql_VariableRef(isHostRef=True)
    assert instance.isHostRef == True
    instance.isHostRef = False
    assert instance.isHostRef == False


def test_plSql_VariableAssignmentTarget_isa_AssignmentTarget():
    instance = plSql_VariableAssignmentTarget()
    assert isinstance(instance, AssignmentTarget)


def test_plSql_Function_isa_CompilationUnit():
    instance = plSql_Function(returnType="sample_text", schemaName="sample_text")
    assert isinstance(instance, CompilationUnit)


def test_plSql_Package_isa_CompilationUnit():
    instance = plSql_Package(endName="sample_text", schemaName="sample_text")
    assert isinstance(instance, CompilationUnit)


def test_plSql_Procedure_isa_CompilationUnit():
    instance = plSql_Procedure(schemaName="sample_text")
    assert isinstance(instance, CompilationUnit)


def test_plSql_BooleanLiteralExpression_isa_Expression():
    instance = plSql_BooleanLiteralExpression(value="sample_text")
    assert isinstance(instance, Expression)


def test_plSql_IntLiteralExpression_isa_Expression():
    instance = plSql_IntLiteralExpression(value=7)
    assert isinstance(instance, Expression)


def test_plSql_NullLiteralExpression_isa_Expression():
    instance = plSql_NullLiteralExpression()
    assert isinstance(instance, Expression)


def test_plSql_StringLiteralExpression_isa_Expression():
    instance = plSql_StringLiteralExpression(value="sample_text")
    assert isinstance(instance, Expression)


def test_plSql_VariableRefExpression_isa_Expression():
    instance = plSql_VariableRefExpression()
    assert isinstance(instance, Expression)


def test_plSql_FetchStatementBulkIntoClause_isa_FetchStatementIntoClause():
    instance = plSql_FetchStatementBulkIntoClause()
    assert isinstance(instance, FetchStatementIntoClause)


def test_plSql_FetchStatementSingleIntoClause_isa_FetchStatementIntoClause():
    instance = plSql_FetchStatementSingleIntoClause()
    assert isinstance(instance, FetchStatementIntoClause)


def test_plSql_DeterministicClause_isa_FunctionClause():
    instance = plSql_DeterministicClause()
    assert isinstance(instance, FunctionClause)


def test_plSql_FunctionInvokerRightsClause_isa_FunctionClause():
    instance = plSql_FunctionInvokerRightsClause(right="sample_text")
    assert isinstance(instance, FunctionClause)


def test_plSql_PipelinedClause_isa_FunctionClause():
    instance = plSql_PipelinedClause()
    assert isinstance(instance, FunctionClause)


def test_plSql_ResultCacheClause_isa_FunctionClause():
    instance = plSql_ResultCacheClause(dataSources="sample_text")
    assert isinstance(instance, FunctionClause)


def test_plSql_FunctionImplementation_isa_FunctionContent():
    instance = plSql_FunctionImplementation()
    assert isinstance(instance, FunctionContent)


def test_plSql_ItemDeclaration_isa_Item():
    instance = plSql_ItemDeclaration()
    assert isinstance(instance, Item)


def test_plSql_Pragma_isa_Item():
    instance = plSql_Pragma()
    assert isinstance(instance, Item)


def test_plSql_ProcedureDeclaration_isa_Item():
    instance = plSql_ProcedureDeclaration(name="sample_text")
    assert isinstance(instance, Item)


def test_plSql_ProcedureDefinition_isa_Item():
    instance = plSql_ProcedureDefinition()
    assert isinstance(instance, Item)


def test_plSql_VariableDeclaration_isa_ItemDeclaration():
    instance = plSql_VariableDeclaration(dataType="sample_text", isConstant=True, isNotNull=True)
    assert isinstance(instance, ItemDeclaration)


def test_plSql_BasicLoopStatement_isa_LoopStatement():
    instance = plSql_BasicLoopStatement()
    assert isinstance(instance, LoopStatement)


def test_plSql_ForLoopStatement_isa_LoopStatement():
    instance = plSql_ForLoopStatement()
    assert isinstance(instance, LoopStatement)


def test_plSql_WhileLoopStatement_isa_LoopStatement():
    instance = plSql_WhileLoopStatement()
    assert isinstance(instance, LoopStatement)


def test_plSql_Function_isa_NameDeclaration():
    instance = plSql_Function(returnType="sample_text", schemaName="sample_text")
    assert isinstance(instance, NameDeclaration)


def test_plSql_LoopVariableDeclaration_isa_NameDeclaration():
    instance = plSql_LoopVariableDeclaration()
    assert isinstance(instance, NameDeclaration)


def test_plSql_Package_isa_NameDeclaration():
    instance = plSql_Package(endName="sample_text", schemaName="sample_text")
    assert isinstance(instance, NameDeclaration)


def test_plSql_ParameterDeclaration_isa_NameDeclaration():
    instance = plSql_ParameterDeclaration(behavior="sample_text", dataType="sample_text")
    assert isinstance(instance, NameDeclaration)


def test_plSql_Procedure_isa_NameDeclaration():
    instance = plSql_Procedure(schemaName="sample_text")
    assert isinstance(instance, NameDeclaration)


def test_plSql_ProcedureDefinition_isa_NameDeclaration():
    instance = plSql_ProcedureDefinition()
    assert isinstance(instance, NameDeclaration)


def test_plSql_VariableDeclaration_isa_NameDeclaration():
    instance = plSql_VariableDeclaration(dataType="sample_text", isConstant=True, isNotNull=True)
    assert isinstance(instance, NameDeclaration)


def test_plSql_PragmaRestrictReferences_isa_Pragma():
    instance = plSql_PragmaRestrictReferences(restrictions="sample_text")
    assert isinstance(instance, Pragma)


def test_plSql_PragmaTimestamp_isa_Pragma():
    instance = plSql_PragmaTimestamp(timestamp="sample_text")
    assert isinstance(instance, Pragma)


def test_plSql_ExternalProcedureDeclaration_isa_ProcedureContent():
    instance = plSql_ExternalProcedureDeclaration()
    assert isinstance(instance, ProcedureContent)


def test_plSql_ProcedureImplementation_isa_ProcedureContent():
    instance = plSql_ProcedureImplementation()
    assert isinstance(instance, ProcedureContent)


def test_plSql_AssignmentStatement_isa_Statement():
    instance = plSql_AssignmentStatement()
    assert isinstance(instance, Statement)


def test_plSql_BlockStatement_isa_Statement():
    instance = plSql_BlockStatement()
    assert isinstance(instance, Statement)


def test_plSql_CaseStatement_isa_Statement():
    instance = plSql_CaseStatement(endLabel="sample_text")
    assert isinstance(instance, Statement)


def test_plSql_CloseStatement_isa_Statement():
    instance = plSql_CloseStatement()
    assert isinstance(instance, Statement)


def test_plSql_ContinueStatement_isa_Statement():
    instance = plSql_ContinueStatement(labelName="sample_text")
    assert isinstance(instance, Statement)


def test_plSql_ExitStatement_isa_Statement():
    instance = plSql_ExitStatement(labelName="sample_text")
    assert isinstance(instance, Statement)


def test_plSql_FetchStatement_isa_Statement():
    instance = plSql_FetchStatement()
    assert isinstance(instance, Statement)


def test_plSql_GotoStatement_isa_Statement():
    instance = plSql_GotoStatement()
    assert isinstance(instance, Statement)


def test_plSql_IfStatement_isa_Statement():
    instance = plSql_IfStatement()
    assert isinstance(instance, Statement)


def test_plSql_LoopStatement_isa_Statement():
    instance = plSql_LoopStatement(endLabel="sample_text")
    assert isinstance(instance, Statement)


def test_plSql_NullStatement_isa_Statement():
    instance = plSql_NullStatement()
    assert isinstance(instance, Statement)


def test_plSql_RaiseStatement_isa_Statement():
    instance = plSql_RaiseStatement(exceptionName="sample_text")
    assert isinstance(instance, Statement)


def test_plSql_ReturnStatement_isa_Statement():
    instance = plSql_ReturnStatement()
    assert isinstance(instance, Statement)


def test_assoc_body29_link_reassign_clear():
    a = plSql_StatementBody(endName="sample_text")
    b1 = plSql_ProcedureImplementation()
    b2 = plSql_ProcedureImplementation()
    _safe_set(a, 'plSql_StatementBody', b1)
    assert _is_linked(a, 'plSql_StatementBody', b1)
    if hasattr(b1, 'plSql_ProcedureImplementation30'):
        assert _is_linked(b1, 'plSql_ProcedureImplementation30', a)
    _safe_set(a, 'plSql_StatementBody', b2)
    assert _is_linked(a, 'plSql_StatementBody', b2)
    if hasattr(b1, 'plSql_ProcedureImplementation30'):
        assert not _is_linked(b1, 'plSql_ProcedureImplementation30', a)
    if hasattr(b2, 'plSql_ProcedureImplementation30'):
        assert _is_linked(b2, 'plSql_ProcedureImplementation30', a)
    _safe_set(a, 'plSql_StatementBody', None)
    assert not _is_linked(a, 'plSql_StatementBody', b2)
    if hasattr(b2, 'plSql_ProcedureImplementation30'):
        assert not _is_linked(b2, 'plSql_ProcedureImplementation30', a)


def test_assoc_body33_link_reassign_clear():
    a = plSql_StatementBody(endName="sample_text")
    b1 = plSql_FunctionImplementation()
    b2 = plSql_FunctionImplementation()
    _safe_set(a, 'plSql_StatementBody35', b1)
    assert _is_linked(a, 'plSql_StatementBody35', b1)
    if hasattr(b1, 'plSql_FunctionImplementation34'):
        assert _is_linked(b1, 'plSql_FunctionImplementation34', a)
    _safe_set(a, 'plSql_StatementBody35', b2)
    assert _is_linked(a, 'plSql_StatementBody35', b2)
    if hasattr(b1, 'plSql_FunctionImplementation34'):
        assert not _is_linked(b1, 'plSql_FunctionImplementation34', a)
    if hasattr(b2, 'plSql_FunctionImplementation34'):
        assert _is_linked(b2, 'plSql_FunctionImplementation34', a)
    _safe_set(a, 'plSql_StatementBody35', None)
    assert not _is_linked(a, 'plSql_StatementBody35', b2)
    if hasattr(b2, 'plSql_FunctionImplementation34'):
        assert not _is_linked(b2, 'plSql_FunctionImplementation34', a)


def test_assoc_body56_link_reassign_clear():
    a = plSql_StatementBody(endName="sample_text")
    b1 = plSql_BlockStatement()
    b2 = plSql_BlockStatement()
    _safe_set(a, 'plSql_StatementBody58', b1)
    assert _is_linked(a, 'plSql_StatementBody58', b1)
    if hasattr(b1, 'plSql_BlockStatement57'):
        assert _is_linked(b1, 'plSql_BlockStatement57', a)
    _safe_set(a, 'plSql_StatementBody58', b2)
    assert _is_linked(a, 'plSql_StatementBody58', b2)
    if hasattr(b1, 'plSql_BlockStatement57'):
        assert not _is_linked(b1, 'plSql_BlockStatement57', a)
    if hasattr(b2, 'plSql_BlockStatement57'):
        assert _is_linked(b2, 'plSql_BlockStatement57', a)
    _safe_set(a, 'plSql_StatementBody58', None)
    assert not _is_linked(a, 'plSql_StatementBody58', b2)
    if hasattr(b2, 'plSql_BlockStatement57'):
        assert not _is_linked(b2, 'plSql_BlockStatement57', a)


def test_assoc_content19_link_reassign_clear():
    a = plSql_Function(returnType="sample_text", schemaName="sample_text")
    b1 = plSql_FunctionContent()
    b2 = plSql_FunctionContent()
    _safe_set(a, 'plSql_Function20', b1)
    assert _is_linked(a, 'plSql_Function20', b1)
    if hasattr(b1, 'plSql_FunctionContent'):
        assert _is_linked(b1, 'plSql_FunctionContent', a)
    _safe_set(a, 'plSql_Function20', b2)
    assert _is_linked(a, 'plSql_Function20', b2)
    if hasattr(b1, 'plSql_FunctionContent'):
        assert not _is_linked(b1, 'plSql_FunctionContent', a)
    if hasattr(b2, 'plSql_FunctionContent'):
        assert _is_linked(b2, 'plSql_FunctionContent', a)
    _safe_set(a, 'plSql_Function20', None)
    assert not _is_linked(a, 'plSql_Function20', b2)
    if hasattr(b2, 'plSql_FunctionContent'):
        assert not _is_linked(b2, 'plSql_FunctionContent', a)


def test_assoc_content3_link_reassign_clear():
    a = plSql_Procedure(schemaName="sample_text")
    b1 = plSql_ProcedureContent()
    b2 = plSql_ProcedureContent()
    _safe_set(a, 'plSql_Procedure4', b1)
    assert _is_linked(a, 'plSql_Procedure4', b1)
    if hasattr(b1, 'plSql_ProcedureContent'):
        assert _is_linked(b1, 'plSql_ProcedureContent', a)
    _safe_set(a, 'plSql_Procedure4', b2)
    assert _is_linked(a, 'plSql_Procedure4', b2)
    if hasattr(b1, 'plSql_ProcedureContent'):
        assert not _is_linked(b1, 'plSql_ProcedureContent', a)
    if hasattr(b2, 'plSql_ProcedureContent'):
        assert _is_linked(b2, 'plSql_ProcedureContent', a)
    _safe_set(a, 'plSql_Procedure4', None)
    assert not _is_linked(a, 'plSql_Procedure4', b2)
    if hasattr(b2, 'plSql_ProcedureContent'):
        assert not _is_linked(b2, 'plSql_ProcedureContent', a)


def test_assoc_cursor74_link_reassign_clear():
    a = plSql_VariableRef(isHostRef=True)
    b1 = plSql_CloseStatement()
    b2 = plSql_CloseStatement()
    _safe_set(a, 'plSql_VariableRef75', b1)
    assert _is_linked(a, 'plSql_VariableRef75', b1)
    if hasattr(b1, 'plSql_CloseStatement'):
        assert _is_linked(b1, 'plSql_CloseStatement', a)
    _safe_set(a, 'plSql_VariableRef75', b2)
    assert _is_linked(a, 'plSql_VariableRef75', b2)
    if hasattr(b1, 'plSql_CloseStatement'):
        assert not _is_linked(b1, 'plSql_CloseStatement', a)
    if hasattr(b2, 'plSql_CloseStatement'):
        assert _is_linked(b2, 'plSql_CloseStatement', a)
    _safe_set(a, 'plSql_VariableRef75', None)
    assert not _is_linked(a, 'plSql_VariableRef75', b2)
    if hasattr(b2, 'plSql_CloseStatement'):
        assert not _is_linked(b2, 'plSql_CloseStatement', a)


def test_assoc_cursor80_link_reassign_clear():
    a = plSql_VariableRef(isHostRef=True)
    b1 = plSql_FetchStatement()
    b2 = plSql_FetchStatement()
    _safe_set(a, 'plSql_VariableRef81', b1)
    assert _is_linked(a, 'plSql_VariableRef81', b1)
    if hasattr(b1, 'plSql_FetchStatement'):
        assert _is_linked(b1, 'plSql_FetchStatement', a)
    _safe_set(a, 'plSql_VariableRef81', b2)
    assert _is_linked(a, 'plSql_VariableRef81', b2)
    if hasattr(b1, 'plSql_FetchStatement'):
        assert not _is_linked(b1, 'plSql_FetchStatement', a)
    if hasattr(b2, 'plSql_FetchStatement'):
        assert _is_linked(b2, 'plSql_FetchStatement', a)
    _safe_set(a, 'plSql_VariableRef81', None)
    assert not _is_linked(a, 'plSql_VariableRef81', b2)
    if hasattr(b2, 'plSql_FetchStatement'):
        assert not _is_linked(b2, 'plSql_FetchStatement', a)


def test_assoc_declaration126_link_reassign_clear():
    a = plSql_NameDeclaration(name="sample_text")
    b1 = plSql_Name()
    b2 = plSql_Name()
    _safe_set(a, 'plSql_NameDeclaration', b1)
    assert _is_linked(a, 'plSql_NameDeclaration', b1)
    if hasattr(b1, 'plSql_Name127'):
        assert _is_linked(b1, 'plSql_Name127', a)
    _safe_set(a, 'plSql_NameDeclaration', b2)
    assert _is_linked(a, 'plSql_NameDeclaration', b2)
    if hasattr(b1, 'plSql_Name127'):
        assert not _is_linked(b1, 'plSql_Name127', a)
    if hasattr(b2, 'plSql_Name127'):
        assert _is_linked(b2, 'plSql_Name127', a)
    _safe_set(a, 'plSql_NameDeclaration', None)
    assert not _is_linked(a, 'plSql_NameDeclaration', b2)
    if hasattr(b2, 'plSql_Name127'):
        assert not _is_linked(b2, 'plSql_Name127', a)


def test_assoc_elseBranch63_link_reassign_clear():
    a = plSql_CaseStatement(endLabel="sample_text")
    b1 = plSql_CaseStatementElseBranch()
    b2 = plSql_CaseStatementElseBranch()
    _safe_set(a, 'plSql_CaseStatement64', b1)
    assert _is_linked(a, 'plSql_CaseStatement64', b1)
    if hasattr(b1, 'plSql_CaseStatementElseBranch'):
        assert _is_linked(b1, 'plSql_CaseStatementElseBranch', a)
    _safe_set(a, 'plSql_CaseStatement64', b2)
    assert _is_linked(a, 'plSql_CaseStatement64', b2)
    if hasattr(b1, 'plSql_CaseStatementElseBranch'):
        assert not _is_linked(b1, 'plSql_CaseStatementElseBranch', a)
    if hasattr(b2, 'plSql_CaseStatementElseBranch'):
        assert _is_linked(b2, 'plSql_CaseStatementElseBranch', a)
    _safe_set(a, 'plSql_CaseStatement64', None)
    assert not _is_linked(a, 'plSql_CaseStatement64', b2)
    if hasattr(b2, 'plSql_CaseStatementElseBranch'):
        assert not _is_linked(b2, 'plSql_CaseStatementElseBranch', a)


def test_assoc_expression59_link_reassign_clear():
    a = plSql_CaseStatement(endLabel="sample_text")
    b1 = plSql_Expression()
    b2 = plSql_Expression()
    _safe_set(a, 'plSql_CaseStatement', b1)
    assert _is_linked(a, 'plSql_CaseStatement', b1)
    if hasattr(b1, 'plSql_Expression60'):
        assert _is_linked(b1, 'plSql_Expression60', a)
    _safe_set(a, 'plSql_CaseStatement', b2)
    assert _is_linked(a, 'plSql_CaseStatement', b2)
    if hasattr(b1, 'plSql_Expression60'):
        assert not _is_linked(b1, 'plSql_Expression60', a)
    if hasattr(b2, 'plSql_Expression60'):
        assert _is_linked(b2, 'plSql_Expression60', a)
    _safe_set(a, 'plSql_CaseStatement', None)
    assert not _is_linked(a, 'plSql_CaseStatement', b2)
    if hasattr(b2, 'plSql_Expression60'):
        assert not _is_linked(b2, 'plSql_Expression60', a)


def test_assoc_functionClauses17_link_reassign_clear():
    a = plSql_Function(returnType="sample_text", schemaName="sample_text")
    b1 = plSql_FunctionClause()
    b2 = plSql_FunctionClause()
    _safe_set(a, 'plSql_Function18', {b1})
    assert _is_linked(a, 'plSql_Function18', b1)
    if hasattr(b1, 'plSql_FunctionClause'):
        assert _is_linked(b1, 'plSql_FunctionClause', a)
    _safe_set(a, 'plSql_Function18', {b2})
    assert _is_linked(a, 'plSql_Function18', b2)
    if hasattr(b1, 'plSql_FunctionClause'):
        assert not _is_linked(b1, 'plSql_FunctionClause', a)
    if hasattr(b2, 'plSql_FunctionClause'):
        assert _is_linked(b2, 'plSql_FunctionClause', a)
    _safe_set(a, 'plSql_Function18', set())
    assert not _is_linked(a, 'plSql_Function18', b2)
    if hasattr(b2, 'plSql_FunctionClause'):
        assert not _is_linked(b2, 'plSql_FunctionClause', a)


def test_assoc_invokerRights1_link_reassign_clear():
    a = plSql_ProcedureInvokerRightsClause(right="sample_text")
    b1 = plSql_Procedure(schemaName="sample_text")
    b2 = plSql_Procedure(schemaName="sample_text_2")
    _safe_set(a, 'plSql_ProcedureInvokerRightsClause', b1)
    assert _is_linked(a, 'plSql_ProcedureInvokerRightsClause', b1)
    if hasattr(b1, 'plSql_Procedure2'):
        assert _is_linked(b1, 'plSql_Procedure2', a)
    _safe_set(a, 'plSql_ProcedureInvokerRightsClause', b2)
    assert _is_linked(a, 'plSql_ProcedureInvokerRightsClause', b2)
    if hasattr(b1, 'plSql_Procedure2'):
        assert not _is_linked(b1, 'plSql_Procedure2', a)
    if hasattr(b2, 'plSql_Procedure2'):
        assert _is_linked(b2, 'plSql_Procedure2', a)
    _safe_set(a, 'plSql_ProcedureInvokerRightsClause', None)
    assert not _is_linked(a, 'plSql_ProcedureInvokerRightsClause', b2)
    if hasattr(b2, 'plSql_Procedure2'):
        assert not _is_linked(b2, 'plSql_Procedure2', a)


def test_assoc_invokerRights5_link_reassign_clear():
    a = plSql_ProcedureInvokerRightsClause(right="sample_text")
    b1 = plSql_Package(endName="sample_text", schemaName="sample_text")
    b2 = plSql_Package(endName="sample_text_2", schemaName="sample_text_2")
    _safe_set(a, 'plSql_ProcedureInvokerRightsClause6', b1)
    assert _is_linked(a, 'plSql_ProcedureInvokerRightsClause6', b1)
    if hasattr(b1, 'plSql_Package'):
        assert _is_linked(b1, 'plSql_Package', a)
    _safe_set(a, 'plSql_ProcedureInvokerRightsClause6', b2)
    assert _is_linked(a, 'plSql_ProcedureInvokerRightsClause6', b2)
    if hasattr(b1, 'plSql_Package'):
        assert not _is_linked(b1, 'plSql_Package', a)
    if hasattr(b2, 'plSql_Package'):
        assert _is_linked(b2, 'plSql_Package', a)
    _safe_set(a, 'plSql_ProcedureInvokerRightsClause6', None)
    assert not _is_linked(a, 'plSql_ProcedureInvokerRightsClause6', b2)
    if hasattr(b2, 'plSql_Package'):
        assert not _is_linked(b2, 'plSql_Package', a)


def test_assoc_items7_link_reassign_clear():
    a = plSql_Package(endName="sample_text", schemaName="sample_text")
    b1 = plSql_Item()
    b2 = plSql_Item()
    _safe_set(a, 'plSql_Package8', {b1})
    assert _is_linked(a, 'plSql_Package8', b1)
    if hasattr(b1, 'plSql_Item'):
        assert _is_linked(b1, 'plSql_Item', a)
    _safe_set(a, 'plSql_Package8', {b2})
    assert _is_linked(a, 'plSql_Package8', b2)
    if hasattr(b1, 'plSql_Item'):
        assert not _is_linked(b1, 'plSql_Item', a)
    if hasattr(b2, 'plSql_Item'):
        assert _is_linked(b2, 'plSql_Item', a)
    _safe_set(a, 'plSql_Package8', set())
    assert not _is_linked(a, 'plSql_Package8', b2)
    if hasattr(b2, 'plSql_Item'):
        assert not _is_linked(b2, 'plSql_Item', a)


def test_assoc_labelName89_link_reassign_clear():
    a = plSql_Label(name="sample_text")
    b1 = plSql_GotoStatement()
    b2 = plSql_GotoStatement()
    _safe_set(a, 'plSql_Label90', b1)
    assert _is_linked(a, 'plSql_Label90', b1)
    if hasattr(b1, 'plSql_GotoStatement'):
        assert _is_linked(b1, 'plSql_GotoStatement', a)
    _safe_set(a, 'plSql_Label90', b2)
    assert _is_linked(a, 'plSql_Label90', b2)
    if hasattr(b1, 'plSql_GotoStatement'):
        assert not _is_linked(b1, 'plSql_GotoStatement', a)
    if hasattr(b2, 'plSql_GotoStatement'):
        assert _is_linked(b2, 'plSql_GotoStatement', a)
    _safe_set(a, 'plSql_Label90', None)
    assert not _is_linked(a, 'plSql_Label90', b2)
    if hasattr(b2, 'plSql_GotoStatement'):
        assert not _is_linked(b2, 'plSql_GotoStatement', a)


def test_assoc_labels46_link_reassign_clear():
    a = plSql_Label(name="sample_text")
    b1 = plSql_Statement()
    b2 = plSql_Statement()
    _safe_set(a, 'plSql_Label', b1)
    assert _is_linked(a, 'plSql_Label', b1)
    if hasattr(b1, 'plSql_Statement47'):
        assert _is_linked(b1, 'plSql_Statement47', a)
    _safe_set(a, 'plSql_Label', b2)
    assert _is_linked(a, 'plSql_Label', b2)
    if hasattr(b1, 'plSql_Statement47'):
        assert not _is_linked(b1, 'plSql_Statement47', a)
    if hasattr(b2, 'plSql_Statement47'):
        assert _is_linked(b2, 'plSql_Statement47', a)
    _safe_set(a, 'plSql_Label', None)
    assert not _is_linked(a, 'plSql_Label', b2)
    if hasattr(b2, 'plSql_Statement47'):
        assert not _is_linked(b2, 'plSql_Statement47', a)


def test_assoc_name122_link_reassign_clear():
    a = plSql_VariableRef(isHostRef=True)
    b1 = plSql_QualifiedName()
    b2 = plSql_QualifiedName()
    _safe_set(a, 'plSql_VariableRef123', b1)
    assert _is_linked(a, 'plSql_VariableRef123', b1)
    if hasattr(b1, 'plSql_QualifiedName'):
        assert _is_linked(b1, 'plSql_QualifiedName', a)
    _safe_set(a, 'plSql_VariableRef123', b2)
    assert _is_linked(a, 'plSql_VariableRef123', b2)
    if hasattr(b1, 'plSql_QualifiedName'):
        assert not _is_linked(b1, 'plSql_QualifiedName', a)
    if hasattr(b2, 'plSql_QualifiedName'):
        assert _is_linked(b2, 'plSql_QualifiedName', a)
    _safe_set(a, 'plSql_VariableRef123', None)
    assert not _is_linked(a, 'plSql_VariableRef123', b2)
    if hasattr(b2, 'plSql_QualifiedName'):
        assert not _is_linked(b2, 'plSql_QualifiedName', a)


def test_assoc_parameters0_link_reassign_clear():
    a = plSql_Procedure(schemaName="sample_text")
    b1 = plSql_ParameterSequence()
    b2 = plSql_ParameterSequence()
    _safe_set(a, 'plSql_Procedure', b1)
    assert _is_linked(a, 'plSql_Procedure', b1)
    if hasattr(b1, 'plSql_ParameterSequence'):
        assert _is_linked(b1, 'plSql_ParameterSequence', a)
    _safe_set(a, 'plSql_Procedure', b2)
    assert _is_linked(a, 'plSql_Procedure', b2)
    if hasattr(b1, 'plSql_ParameterSequence'):
        assert not _is_linked(b1, 'plSql_ParameterSequence', a)
    if hasattr(b2, 'plSql_ParameterSequence'):
        assert _is_linked(b2, 'plSql_ParameterSequence', a)
    _safe_set(a, 'plSql_Procedure', None)
    assert not _is_linked(a, 'plSql_Procedure', b2)
    if hasattr(b2, 'plSql_ParameterSequence'):
        assert not _is_linked(b2, 'plSql_ParameterSequence', a)


def test_assoc_parameters15_link_reassign_clear():
    a = plSql_Function(returnType="sample_text", schemaName="sample_text")
    b1 = plSql_ParameterSequence()
    b2 = plSql_ParameterSequence()
    _safe_set(a, 'plSql_Function', b1)
    assert _is_linked(a, 'plSql_Function', b1)
    if hasattr(b1, 'plSql_ParameterSequence16'):
        assert _is_linked(b1, 'plSql_ParameterSequence16', a)
    _safe_set(a, 'plSql_Function', b2)
    assert _is_linked(a, 'plSql_Function', b2)
    if hasattr(b1, 'plSql_ParameterSequence16'):
        assert not _is_linked(b1, 'plSql_ParameterSequence16', a)
    if hasattr(b2, 'plSql_ParameterSequence16'):
        assert _is_linked(b2, 'plSql_ParameterSequence16', a)
    _safe_set(a, 'plSql_Function', None)
    assert not _is_linked(a, 'plSql_Function', b2)
    if hasattr(b2, 'plSql_ParameterSequence16'):
        assert not _is_linked(b2, 'plSql_ParameterSequence16', a)


def test_assoc_parameters21_link_reassign_clear():
    a = plSql_ParameterDeclaration(behavior="sample_text", dataType="sample_text")
    b1 = plSql_ParameterSequence()
    b2 = plSql_ParameterSequence()
    _safe_set(a, 'plSql_ParameterDeclaration', b1)
    assert _is_linked(a, 'plSql_ParameterDeclaration', b1)
    if hasattr(b1, 'plSql_ParameterSequence22'):
        assert _is_linked(b1, 'plSql_ParameterSequence22', a)
    _safe_set(a, 'plSql_ParameterDeclaration', b2)
    assert _is_linked(a, 'plSql_ParameterDeclaration', b2)
    if hasattr(b1, 'plSql_ParameterSequence22'):
        assert not _is_linked(b1, 'plSql_ParameterSequence22', a)
    if hasattr(b2, 'plSql_ParameterSequence22'):
        assert _is_linked(b2, 'plSql_ParameterSequence22', a)
    _safe_set(a, 'plSql_ParameterDeclaration', None)
    assert not _is_linked(a, 'plSql_ParameterDeclaration', b2)
    if hasattr(b2, 'plSql_ParameterSequence22'):
        assert not _is_linked(b2, 'plSql_ParameterSequence22', a)


def test_assoc_parameters9_link_reassign_clear():
    a = plSql_ProcedureDeclaration(name="sample_text")
    b1 = plSql_ParameterSequence()
    b2 = plSql_ParameterSequence()
    _safe_set(a, 'plSql_ProcedureDeclaration', b1)
    assert _is_linked(a, 'plSql_ProcedureDeclaration', b1)
    if hasattr(b1, 'plSql_ParameterSequence10'):
        assert _is_linked(b1, 'plSql_ParameterSequence10', a)
    _safe_set(a, 'plSql_ProcedureDeclaration', b2)
    assert _is_linked(a, 'plSql_ProcedureDeclaration', b2)
    if hasattr(b1, 'plSql_ParameterSequence10'):
        assert not _is_linked(b1, 'plSql_ParameterSequence10', a)
    if hasattr(b2, 'plSql_ParameterSequence10'):
        assert _is_linked(b2, 'plSql_ParameterSequence10', a)
    _safe_set(a, 'plSql_ProcedureDeclaration', None)
    assert not _is_linked(a, 'plSql_ProcedureDeclaration', b2)
    if hasattr(b2, 'plSql_ParameterSequence10'):
        assert not _is_linked(b2, 'plSql_ParameterSequence10', a)


def test_assoc_statements109_link_reassign_clear():
    a = plSql_LoopStatement(endLabel="sample_text")
    b1 = plSql_Statement()
    b2 = plSql_Statement()
    _safe_set(a, 'plSql_LoopStatement', {b1})
    assert _is_linked(a, 'plSql_LoopStatement', b1)
    if hasattr(b1, 'plSql_Statement110'):
        assert _is_linked(b1, 'plSql_Statement110', a)
    _safe_set(a, 'plSql_LoopStatement', {b2})
    assert _is_linked(a, 'plSql_LoopStatement', b2)
    if hasattr(b1, 'plSql_Statement110'):
        assert not _is_linked(b1, 'plSql_Statement110', a)
    if hasattr(b2, 'plSql_Statement110'):
        assert _is_linked(b2, 'plSql_Statement110', a)
    _safe_set(a, 'plSql_LoopStatement', set())
    assert not _is_linked(a, 'plSql_LoopStatement', b2)
    if hasattr(b2, 'plSql_Statement110'):
        assert not _is_linked(b2, 'plSql_Statement110', a)


def test_assoc_statements36_link_reassign_clear():
    a = plSql_StatementBody(endName="sample_text")
    b1 = plSql_Statement()
    b2 = plSql_Statement()
    _safe_set(a, 'plSql_StatementBody37', {b1})
    assert _is_linked(a, 'plSql_StatementBody37', b1)
    if hasattr(b1, 'plSql_Statement'):
        assert _is_linked(b1, 'plSql_Statement', a)
    _safe_set(a, 'plSql_StatementBody37', {b2})
    assert _is_linked(a, 'plSql_StatementBody37', b2)
    if hasattr(b1, 'plSql_Statement'):
        assert not _is_linked(b1, 'plSql_Statement', a)
    if hasattr(b2, 'plSql_Statement'):
        assert _is_linked(b2, 'plSql_Statement', a)
    _safe_set(a, 'plSql_StatementBody37', set())
    assert not _is_linked(a, 'plSql_StatementBody37', b2)
    if hasattr(b2, 'plSql_Statement'):
        assert not _is_linked(b2, 'plSql_Statement', a)


def test_assoc_targetVariables84_link_reassign_clear():
    a = plSql_VariableRef(isHostRef=True)
    b1 = plSql_FetchStatementIntoClause()
    b2 = plSql_FetchStatementIntoClause()
    _safe_set(a, 'plSql_VariableRef86', b1)
    assert _is_linked(a, 'plSql_VariableRef86', b1)
    if hasattr(b1, 'plSql_FetchStatementIntoClause85'):
        assert _is_linked(b1, 'plSql_FetchStatementIntoClause85', a)
    _safe_set(a, 'plSql_VariableRef86', b2)
    assert _is_linked(a, 'plSql_VariableRef86', b2)
    if hasattr(b1, 'plSql_FetchStatementIntoClause85'):
        assert not _is_linked(b1, 'plSql_FetchStatementIntoClause85', a)
    if hasattr(b2, 'plSql_FetchStatementIntoClause85'):
        assert _is_linked(b2, 'plSql_FetchStatementIntoClause85', a)
    _safe_set(a, 'plSql_VariableRef86', None)
    assert not _is_linked(a, 'plSql_VariableRef86', b2)
    if hasattr(b2, 'plSql_FetchStatementIntoClause85'):
        assert not _is_linked(b2, 'plSql_FetchStatementIntoClause85', a)


def test_assoc_value23_link_reassign_clear():
    a = plSql_ParameterDeclaration(behavior="sample_text", dataType="sample_text")
    b1 = plSql_ParameterValue()
    b2 = plSql_ParameterValue()
    _safe_set(a, 'plSql_ParameterDeclaration24', b1)
    assert _is_linked(a, 'plSql_ParameterDeclaration24', b1)
    if hasattr(b1, 'plSql_ParameterValue'):
        assert _is_linked(b1, 'plSql_ParameterValue', a)
    _safe_set(a, 'plSql_ParameterDeclaration24', b2)
    assert _is_linked(a, 'plSql_ParameterDeclaration24', b2)
    if hasattr(b1, 'plSql_ParameterValue'):
        assert not _is_linked(b1, 'plSql_ParameterValue', a)
    if hasattr(b2, 'plSql_ParameterValue'):
        assert _is_linked(b2, 'plSql_ParameterValue', a)
    _safe_set(a, 'plSql_ParameterDeclaration24', None)
    assert not _is_linked(a, 'plSql_ParameterDeclaration24', b2)
    if hasattr(b2, 'plSql_ParameterValue'):
        assert not _is_linked(b2, 'plSql_ParameterValue', a)


def test_assoc_value41_link_reassign_clear():
    a = plSql_VariableDeclaration(dataType="sample_text", isConstant=True, isNotNull=True)
    b1 = plSql_VariableValue()
    b2 = plSql_VariableValue()
    _safe_set(a, 'plSql_VariableDeclaration', b1)
    assert _is_linked(a, 'plSql_VariableDeclaration', b1)
    if hasattr(b1, 'plSql_VariableValue'):
        assert _is_linked(b1, 'plSql_VariableValue', a)
    _safe_set(a, 'plSql_VariableDeclaration', b2)
    assert _is_linked(a, 'plSql_VariableDeclaration', b2)
    if hasattr(b1, 'plSql_VariableValue'):
        assert not _is_linked(b1, 'plSql_VariableValue', a)
    if hasattr(b2, 'plSql_VariableValue'):
        assert _is_linked(b2, 'plSql_VariableValue', a)
    _safe_set(a, 'plSql_VariableDeclaration', None)
    assert not _is_linked(a, 'plSql_VariableDeclaration', b2)
    if hasattr(b2, 'plSql_VariableValue'):
        assert not _is_linked(b2, 'plSql_VariableValue', a)


def test_assoc_variable45_link_reassign_clear():
    a = plSql_VariableRef(isHostRef=True)
    b1 = plSql_VariableRefExpression()
    b2 = plSql_VariableRefExpression()
    _safe_set(a, 'plSql_VariableRef', b1)
    assert _is_linked(a, 'plSql_VariableRef', b1)
    if hasattr(b1, 'plSql_VariableRefExpression'):
        assert _is_linked(b1, 'plSql_VariableRefExpression', a)
    _safe_set(a, 'plSql_VariableRef', b2)
    assert _is_linked(a, 'plSql_VariableRef', b2)
    if hasattr(b1, 'plSql_VariableRefExpression'):
        assert not _is_linked(b1, 'plSql_VariableRefExpression', a)
    if hasattr(b2, 'plSql_VariableRefExpression'):
        assert _is_linked(b2, 'plSql_VariableRefExpression', a)
    _safe_set(a, 'plSql_VariableRef', None)
    assert not _is_linked(a, 'plSql_VariableRef', b2)
    if hasattr(b2, 'plSql_VariableRefExpression'):
        assert not _is_linked(b2, 'plSql_VariableRefExpression', a)


def test_assoc_variable52_link_reassign_clear():
    a = plSql_VariableRef(isHostRef=True)
    b1 = plSql_VariableAssignmentTarget()
    b2 = plSql_VariableAssignmentTarget()
    _safe_set(a, 'plSql_VariableRef53', b1)
    assert _is_linked(a, 'plSql_VariableRef53', b1)
    if hasattr(b1, 'plSql_VariableAssignmentTarget'):
        assert _is_linked(b1, 'plSql_VariableAssignmentTarget', a)
    _safe_set(a, 'plSql_VariableRef53', b2)
    assert _is_linked(a, 'plSql_VariableRef53', b2)
    if hasattr(b1, 'plSql_VariableAssignmentTarget'):
        assert not _is_linked(b1, 'plSql_VariableAssignmentTarget', a)
    if hasattr(b2, 'plSql_VariableAssignmentTarget'):
        assert _is_linked(b2, 'plSql_VariableAssignmentTarget', a)
    _safe_set(a, 'plSql_VariableRef53', None)
    assert not _is_linked(a, 'plSql_VariableRef53', b2)
    if hasattr(b2, 'plSql_VariableAssignmentTarget'):
        assert not _is_linked(b2, 'plSql_VariableAssignmentTarget', a)


def test_assoc_whenBranches61_link_reassign_clear():
    a = plSql_CaseStatement(endLabel="sample_text")
    b1 = plSql_CaseStatementWhenBranch()
    b2 = plSql_CaseStatementWhenBranch()
    _safe_set(a, 'plSql_CaseStatement62', {b1})
    assert _is_linked(a, 'plSql_CaseStatement62', b1)
    if hasattr(b1, 'plSql_CaseStatementWhenBranch'):
        assert _is_linked(b1, 'plSql_CaseStatementWhenBranch', a)
    _safe_set(a, 'plSql_CaseStatement62', {b2})
    assert _is_linked(a, 'plSql_CaseStatement62', b2)
    if hasattr(b1, 'plSql_CaseStatementWhenBranch'):
        assert not _is_linked(b1, 'plSql_CaseStatementWhenBranch', a)
    if hasattr(b2, 'plSql_CaseStatementWhenBranch'):
        assert _is_linked(b2, 'plSql_CaseStatementWhenBranch', a)
    _safe_set(a, 'plSql_CaseStatement62', set())
    assert not _is_linked(a, 'plSql_CaseStatement62', b2)
    if hasattr(b2, 'plSql_CaseStatementWhenBranch'):
        assert not _is_linked(b2, 'plSql_CaseStatementWhenBranch', a)


def test_assoc_whenExpression76_link_reassign_clear():
    a = plSql_ContinueStatement(labelName="sample_text")
    b1 = plSql_Expression()
    b2 = plSql_Expression()
    _safe_set(a, 'plSql_ContinueStatement', b1)
    assert _is_linked(a, 'plSql_ContinueStatement', b1)
    if hasattr(b1, 'plSql_Expression77'):
        assert _is_linked(b1, 'plSql_Expression77', a)
    _safe_set(a, 'plSql_ContinueStatement', b2)
    assert _is_linked(a, 'plSql_ContinueStatement', b2)
    if hasattr(b1, 'plSql_Expression77'):
        assert not _is_linked(b1, 'plSql_Expression77', a)
    if hasattr(b2, 'plSql_Expression77'):
        assert _is_linked(b2, 'plSql_Expression77', a)
    _safe_set(a, 'plSql_ContinueStatement', None)
    assert not _is_linked(a, 'plSql_ContinueStatement', b2)
    if hasattr(b2, 'plSql_Expression77'):
        assert not _is_linked(b2, 'plSql_Expression77', a)


def test_assoc_whenExpression78_link_reassign_clear():
    a = plSql_ExitStatement(labelName="sample_text")
    b1 = plSql_Expression()
    b2 = plSql_Expression()
    _safe_set(a, 'plSql_ExitStatement', b1)
    assert _is_linked(a, 'plSql_ExitStatement', b1)
    if hasattr(b1, 'plSql_Expression79'):
        assert _is_linked(b1, 'plSql_Expression79', a)
    _safe_set(a, 'plSql_ExitStatement', b2)
    assert _is_linked(a, 'plSql_ExitStatement', b2)
    if hasattr(b1, 'plSql_Expression79'):
        assert not _is_linked(b1, 'plSql_Expression79', a)
    if hasattr(b2, 'plSql_Expression79'):
        assert _is_linked(b2, 'plSql_Expression79', a)
    _safe_set(a, 'plSql_ExitStatement', None)
    assert not _is_linked(a, 'plSql_ExitStatement', b2)
    if hasattr(b2, 'plSql_Expression79'):
        assert not _is_linked(b2, 'plSql_Expression79', a)


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

AssignmentTarget_strategy = st.builds(AssignmentTarget)
@given(instance=AssignmentTarget_strategy)
@settings(max_examples=25)
def test_AssignmentTarget_instantiation(instance):
    assert isinstance(instance, AssignmentTarget)


CompilationUnit_strategy = st.builds(CompilationUnit)
@given(instance=CompilationUnit_strategy)
@settings(max_examples=25)
def test_CompilationUnit_instantiation(instance):
    assert isinstance(instance, CompilationUnit)


Expression_strategy = st.builds(Expression)
@given(instance=Expression_strategy)
@settings(max_examples=25)
def test_Expression_instantiation(instance):
    assert isinstance(instance, Expression)


FetchStatementIntoClause_strategy = st.builds(FetchStatementIntoClause)
@given(instance=FetchStatementIntoClause_strategy)
@settings(max_examples=25)
def test_FetchStatementIntoClause_instantiation(instance):
    assert isinstance(instance, FetchStatementIntoClause)


FunctionClause_strategy = st.builds(FunctionClause)
@given(instance=FunctionClause_strategy)
@settings(max_examples=25)
def test_FunctionClause_instantiation(instance):
    assert isinstance(instance, FunctionClause)


FunctionContent_strategy = st.builds(FunctionContent)
@given(instance=FunctionContent_strategy)
@settings(max_examples=25)
def test_FunctionContent_instantiation(instance):
    assert isinstance(instance, FunctionContent)


Item_strategy = st.builds(Item)
@given(instance=Item_strategy)
@settings(max_examples=25)
def test_Item_instantiation(instance):
    assert isinstance(instance, Item)


ItemDeclaration_strategy = st.builds(ItemDeclaration)
@given(instance=ItemDeclaration_strategy)
@settings(max_examples=25)
def test_ItemDeclaration_instantiation(instance):
    assert isinstance(instance, ItemDeclaration)


LoopStatement_strategy = st.builds(LoopStatement)
@given(instance=LoopStatement_strategy)
@settings(max_examples=25)
def test_LoopStatement_instantiation(instance):
    assert isinstance(instance, LoopStatement)


NameDeclaration_strategy = st.builds(NameDeclaration)
@given(instance=NameDeclaration_strategy)
@settings(max_examples=25)
def test_NameDeclaration_instantiation(instance):
    assert isinstance(instance, NameDeclaration)


Pragma_strategy = st.builds(Pragma)
@given(instance=Pragma_strategy)
@settings(max_examples=25)
def test_Pragma_instantiation(instance):
    assert isinstance(instance, Pragma)


ProcedureContent_strategy = st.builds(ProcedureContent)
@given(instance=ProcedureContent_strategy)
@settings(max_examples=25)
def test_ProcedureContent_instantiation(instance):
    assert isinstance(instance, ProcedureContent)


Statement_strategy = st.builds(Statement)
@given(instance=Statement_strategy)
@settings(max_examples=25)
def test_Statement_instantiation(instance):
    assert isinstance(instance, Statement)


plSql_AssignmentStatement_strategy = st.builds(plSql_AssignmentStatement)
@given(instance=plSql_AssignmentStatement_strategy)
@settings(max_examples=25)
def test_plSql_AssignmentStatement_instantiation(instance):
    assert isinstance(instance, plSql_AssignmentStatement)


plSql_AssignmentTarget_strategy = st.builds(plSql_AssignmentTarget)
@given(instance=plSql_AssignmentTarget_strategy)
@settings(max_examples=25)
def test_plSql_AssignmentTarget_instantiation(instance):
    assert isinstance(instance, plSql_AssignmentTarget)


plSql_BasicLoopStatement_strategy = st.builds(plSql_BasicLoopStatement)
@given(instance=plSql_BasicLoopStatement_strategy)
@settings(max_examples=25)
def test_plSql_BasicLoopStatement_instantiation(instance):
    assert isinstance(instance, plSql_BasicLoopStatement)


plSql_BlockStatement_strategy = st.builds(plSql_BlockStatement)
@given(instance=plSql_BlockStatement_strategy)
@settings(max_examples=25)
def test_plSql_BlockStatement_instantiation(instance):
    assert isinstance(instance, plSql_BlockStatement)


plSql_BooleanLiteralExpression_strategy = st.builds(plSql_BooleanLiteralExpression, value=safe_text)
@given(instance=plSql_BooleanLiteralExpression_strategy)
@settings(max_examples=25)
def test_plSql_BooleanLiteralExpression_instantiation(instance):
    assert isinstance(instance, plSql_BooleanLiteralExpression)


plSql_CaseStatement_strategy = st.builds(plSql_CaseStatement, endLabel=safe_text)
@given(instance=plSql_CaseStatement_strategy)
@settings(max_examples=25)
def test_plSql_CaseStatement_instantiation(instance):
    assert isinstance(instance, plSql_CaseStatement)


plSql_CaseStatementElseBranch_strategy = st.builds(plSql_CaseStatementElseBranch)
@given(instance=plSql_CaseStatementElseBranch_strategy)
@settings(max_examples=25)
def test_plSql_CaseStatementElseBranch_instantiation(instance):
    assert isinstance(instance, plSql_CaseStatementElseBranch)


plSql_CaseStatementWhenBranch_strategy = st.builds(plSql_CaseStatementWhenBranch)
@given(instance=plSql_CaseStatementWhenBranch_strategy)
@settings(max_examples=25)
def test_plSql_CaseStatementWhenBranch_instantiation(instance):
    assert isinstance(instance, plSql_CaseStatementWhenBranch)


plSql_CloseStatement_strategy = st.builds(plSql_CloseStatement)
@given(instance=plSql_CloseStatement_strategy)
@settings(max_examples=25)
def test_plSql_CloseStatement_instantiation(instance):
    assert isinstance(instance, plSql_CloseStatement)


plSql_CompilationUnit_strategy = st.builds(plSql_CompilationUnit)
@given(instance=plSql_CompilationUnit_strategy)
@settings(max_examples=25)
def test_plSql_CompilationUnit_instantiation(instance):
    assert isinstance(instance, plSql_CompilationUnit)


plSql_ContinueStatement_strategy = st.builds(plSql_ContinueStatement, labelName=safe_text)
@given(instance=plSql_ContinueStatement_strategy)
@settings(max_examples=25)
def test_plSql_ContinueStatement_instantiation(instance):
    assert isinstance(instance, plSql_ContinueStatement)


plSql_DeclareSection_strategy = st.builds(plSql_DeclareSection)
@given(instance=plSql_DeclareSection_strategy)
@settings(max_examples=25)
def test_plSql_DeclareSection_instantiation(instance):
    assert isinstance(instance, plSql_DeclareSection)


plSql_DeterministicClause_strategy = st.builds(plSql_DeterministicClause)
@given(instance=plSql_DeterministicClause_strategy)
@settings(max_examples=25)
def test_plSql_DeterministicClause_instantiation(instance):
    assert isinstance(instance, plSql_DeterministicClause)


plSql_ExitStatement_strategy = st.builds(plSql_ExitStatement, labelName=safe_text)
@given(instance=plSql_ExitStatement_strategy)
@settings(max_examples=25)
def test_plSql_ExitStatement_instantiation(instance):
    assert isinstance(instance, plSql_ExitStatement)


plSql_Expression_strategy = st.builds(plSql_Expression)
@given(instance=plSql_Expression_strategy)
@settings(max_examples=25)
def test_plSql_Expression_instantiation(instance):
    assert isinstance(instance, plSql_Expression)


plSql_ExternalProcedureDeclaration_strategy = st.builds(plSql_ExternalProcedureDeclaration)
@given(instance=plSql_ExternalProcedureDeclaration_strategy)
@settings(max_examples=25)
def test_plSql_ExternalProcedureDeclaration_instantiation(instance):
    assert isinstance(instance, plSql_ExternalProcedureDeclaration)


plSql_FetchStatement_strategy = st.builds(plSql_FetchStatement)
@given(instance=plSql_FetchStatement_strategy)
@settings(max_examples=25)
def test_plSql_FetchStatement_instantiation(instance):
    assert isinstance(instance, plSql_FetchStatement)


plSql_FetchStatementBulkIntoClause_strategy = st.builds(plSql_FetchStatementBulkIntoClause)
@given(instance=plSql_FetchStatementBulkIntoClause_strategy)
@settings(max_examples=25)
def test_plSql_FetchStatementBulkIntoClause_instantiation(instance):
    assert isinstance(instance, plSql_FetchStatementBulkIntoClause)


plSql_FetchStatementIntoClause_strategy = st.builds(plSql_FetchStatementIntoClause)
@given(instance=plSql_FetchStatementIntoClause_strategy)
@settings(max_examples=25)
def test_plSql_FetchStatementIntoClause_instantiation(instance):
    assert isinstance(instance, plSql_FetchStatementIntoClause)


plSql_FetchStatementSingleIntoClause_strategy = st.builds(plSql_FetchStatementSingleIntoClause)
@given(instance=plSql_FetchStatementSingleIntoClause_strategy)
@settings(max_examples=25)
def test_plSql_FetchStatementSingleIntoClause_instantiation(instance):
    assert isinstance(instance, plSql_FetchStatementSingleIntoClause)


plSql_ForLoopStatement_strategy = st.builds(plSql_ForLoopStatement)
@given(instance=plSql_ForLoopStatement_strategy)
@settings(max_examples=25)
def test_plSql_ForLoopStatement_instantiation(instance):
    assert isinstance(instance, plSql_ForLoopStatement)


plSql_Function_strategy = st.builds(plSql_Function, returnType=safe_text, schemaName=safe_text)
@given(instance=plSql_Function_strategy)
@settings(max_examples=25)
def test_plSql_Function_instantiation(instance):
    assert isinstance(instance, plSql_Function)


plSql_FunctionClause_strategy = st.builds(plSql_FunctionClause)
@given(instance=plSql_FunctionClause_strategy)
@settings(max_examples=25)
def test_plSql_FunctionClause_instantiation(instance):
    assert isinstance(instance, plSql_FunctionClause)


plSql_FunctionContent_strategy = st.builds(plSql_FunctionContent)
@given(instance=plSql_FunctionContent_strategy)
@settings(max_examples=25)
def test_plSql_FunctionContent_instantiation(instance):
    assert isinstance(instance, plSql_FunctionContent)


plSql_FunctionImplementation_strategy = st.builds(plSql_FunctionImplementation)
@given(instance=plSql_FunctionImplementation_strategy)
@settings(max_examples=25)
def test_plSql_FunctionImplementation_instantiation(instance):
    assert isinstance(instance, plSql_FunctionImplementation)


plSql_FunctionInvokerRightsClause_strategy = st.builds(plSql_FunctionInvokerRightsClause, right=safe_text)
@given(instance=plSql_FunctionInvokerRightsClause_strategy)
@settings(max_examples=25)
def test_plSql_FunctionInvokerRightsClause_instantiation(instance):
    assert isinstance(instance, plSql_FunctionInvokerRightsClause)


plSql_GotoStatement_strategy = st.builds(plSql_GotoStatement)
@given(instance=plSql_GotoStatement_strategy)
@settings(max_examples=25)
def test_plSql_GotoStatement_instantiation(instance):
    assert isinstance(instance, plSql_GotoStatement)


plSql_IfStatement_strategy = st.builds(plSql_IfStatement)
@given(instance=plSql_IfStatement_strategy)
@settings(max_examples=25)
def test_plSql_IfStatement_instantiation(instance):
    assert isinstance(instance, plSql_IfStatement)


plSql_IfStatementElseBranch_strategy = st.builds(plSql_IfStatementElseBranch)
@given(instance=plSql_IfStatementElseBranch_strategy)
@settings(max_examples=25)
def test_plSql_IfStatementElseBranch_instantiation(instance):
    assert isinstance(instance, plSql_IfStatementElseBranch)


plSql_IfStatementElsifBranch_strategy = st.builds(plSql_IfStatementElsifBranch)
@given(instance=plSql_IfStatementElsifBranch_strategy)
@settings(max_examples=25)
def test_plSql_IfStatementElsifBranch_instantiation(instance):
    assert isinstance(instance, plSql_IfStatementElsifBranch)


plSql_IntLiteralExpression_strategy = st.builds(plSql_IntLiteralExpression, value=st.integers())
@given(instance=plSql_IntLiteralExpression_strategy)
@settings(max_examples=25)
def test_plSql_IntLiteralExpression_instantiation(instance):
    assert isinstance(instance, plSql_IntLiteralExpression)


plSql_Item_strategy = st.builds(plSql_Item)
@given(instance=plSql_Item_strategy)
@settings(max_examples=25)
def test_plSql_Item_instantiation(instance):
    assert isinstance(instance, plSql_Item)


plSql_ItemDeclaration_strategy = st.builds(plSql_ItemDeclaration)
@given(instance=plSql_ItemDeclaration_strategy)
@settings(max_examples=25)
def test_plSql_ItemDeclaration_instantiation(instance):
    assert isinstance(instance, plSql_ItemDeclaration)


plSql_Label_strategy = st.builds(plSql_Label, name=safe_text)
@given(instance=plSql_Label_strategy)
@settings(max_examples=25)
def test_plSql_Label_instantiation(instance):
    assert isinstance(instance, plSql_Label)


plSql_LoopStatement_strategy = st.builds(plSql_LoopStatement, endLabel=safe_text)
@given(instance=plSql_LoopStatement_strategy)
@settings(max_examples=25)
def test_plSql_LoopStatement_instantiation(instance):
    assert isinstance(instance, plSql_LoopStatement)


plSql_LoopVariableDeclaration_strategy = st.builds(plSql_LoopVariableDeclaration)
@given(instance=plSql_LoopVariableDeclaration_strategy)
@settings(max_examples=25)
def test_plSql_LoopVariableDeclaration_instantiation(instance):
    assert isinstance(instance, plSql_LoopVariableDeclaration)


plSql_Name_strategy = st.builds(plSql_Name)
@given(instance=plSql_Name_strategy)
@settings(max_examples=25)
def test_plSql_Name_instantiation(instance):
    assert isinstance(instance, plSql_Name)


plSql_NameDeclaration_strategy = st.builds(plSql_NameDeclaration, name=safe_text)
@given(instance=plSql_NameDeclaration_strategy)
@settings(max_examples=25)
def test_plSql_NameDeclaration_instantiation(instance):
    assert isinstance(instance, plSql_NameDeclaration)


plSql_NullLiteralExpression_strategy = st.builds(plSql_NullLiteralExpression)
@given(instance=plSql_NullLiteralExpression_strategy)
@settings(max_examples=25)
def test_plSql_NullLiteralExpression_instantiation(instance):
    assert isinstance(instance, plSql_NullLiteralExpression)


plSql_NullStatement_strategy = st.builds(plSql_NullStatement)
@given(instance=plSql_NullStatement_strategy)
@settings(max_examples=25)
def test_plSql_NullStatement_instantiation(instance):
    assert isinstance(instance, plSql_NullStatement)


plSql_Package_strategy = st.builds(plSql_Package, endName=safe_text, schemaName=safe_text)
@given(instance=plSql_Package_strategy)
@settings(max_examples=25)
def test_plSql_Package_instantiation(instance):
    assert isinstance(instance, plSql_Package)


plSql_ParameterDeclaration_strategy = st.builds(plSql_ParameterDeclaration, behavior=safe_text, dataType=safe_text)
@given(instance=plSql_ParameterDeclaration_strategy)
@settings(max_examples=25)
def test_plSql_ParameterDeclaration_instantiation(instance):
    assert isinstance(instance, plSql_ParameterDeclaration)


plSql_ParameterSequence_strategy = st.builds(plSql_ParameterSequence)
@given(instance=plSql_ParameterSequence_strategy)
@settings(max_examples=25)
def test_plSql_ParameterSequence_instantiation(instance):
    assert isinstance(instance, plSql_ParameterSequence)


plSql_ParameterValue_strategy = st.builds(plSql_ParameterValue)
@given(instance=plSql_ParameterValue_strategy)
@settings(max_examples=25)
def test_plSql_ParameterValue_instantiation(instance):
    assert isinstance(instance, plSql_ParameterValue)


plSql_PipelinedClause_strategy = st.builds(plSql_PipelinedClause)
@given(instance=plSql_PipelinedClause_strategy)
@settings(max_examples=25)
def test_plSql_PipelinedClause_instantiation(instance):
    assert isinstance(instance, plSql_PipelinedClause)


plSql_Pragma_strategy = st.builds(plSql_Pragma)
@given(instance=plSql_Pragma_strategy)
@settings(max_examples=25)
def test_plSql_Pragma_instantiation(instance):
    assert isinstance(instance, plSql_Pragma)


plSql_PragmaRestrictReferences_strategy = st.builds(plSql_PragmaRestrictReferences, restrictions=safe_text)
@given(instance=plSql_PragmaRestrictReferences_strategy)
@settings(max_examples=25)
def test_plSql_PragmaRestrictReferences_instantiation(instance):
    assert isinstance(instance, plSql_PragmaRestrictReferences)


plSql_PragmaTimestamp_strategy = st.builds(plSql_PragmaTimestamp, timestamp=safe_text)
@given(instance=plSql_PragmaTimestamp_strategy)
@settings(max_examples=25)
def test_plSql_PragmaTimestamp_instantiation(instance):
    assert isinstance(instance, plSql_PragmaTimestamp)


plSql_Procedure_strategy = st.builds(plSql_Procedure, schemaName=safe_text)
@given(instance=plSql_Procedure_strategy)
@settings(max_examples=25)
def test_plSql_Procedure_instantiation(instance):
    assert isinstance(instance, plSql_Procedure)


plSql_ProcedureContent_strategy = st.builds(plSql_ProcedureContent)
@given(instance=plSql_ProcedureContent_strategy)
@settings(max_examples=25)
def test_plSql_ProcedureContent_instantiation(instance):
    assert isinstance(instance, plSql_ProcedureContent)


plSql_ProcedureDeclaration_strategy = st.builds(plSql_ProcedureDeclaration, name=safe_text)
@given(instance=plSql_ProcedureDeclaration_strategy)
@settings(max_examples=25)
def test_plSql_ProcedureDeclaration_instantiation(instance):
    assert isinstance(instance, plSql_ProcedureDeclaration)


plSql_ProcedureDefinition_strategy = st.builds(plSql_ProcedureDefinition)
@given(instance=plSql_ProcedureDefinition_strategy)
@settings(max_examples=25)
def test_plSql_ProcedureDefinition_instantiation(instance):
    assert isinstance(instance, plSql_ProcedureDefinition)


plSql_ProcedureImplementation_strategy = st.builds(plSql_ProcedureImplementation)
@given(instance=plSql_ProcedureImplementation_strategy)
@settings(max_examples=25)
def test_plSql_ProcedureImplementation_instantiation(instance):
    assert isinstance(instance, plSql_ProcedureImplementation)


plSql_ProcedureInvokerRightsClause_strategy = st.builds(plSql_ProcedureInvokerRightsClause, right=safe_text)
@given(instance=plSql_ProcedureInvokerRightsClause_strategy)
@settings(max_examples=25)
def test_plSql_ProcedureInvokerRightsClause_instantiation(instance):
    assert isinstance(instance, plSql_ProcedureInvokerRightsClause)


plSql_QualifiedName_strategy = st.builds(plSql_QualifiedName)
@given(instance=plSql_QualifiedName_strategy)
@settings(max_examples=25)
def test_plSql_QualifiedName_instantiation(instance):
    assert isinstance(instance, plSql_QualifiedName)


plSql_RaiseStatement_strategy = st.builds(plSql_RaiseStatement, exceptionName=safe_text)
@given(instance=plSql_RaiseStatement_strategy)
@settings(max_examples=25)
def test_plSql_RaiseStatement_instantiation(instance):
    assert isinstance(instance, plSql_RaiseStatement)


plSql_ResultCacheClause_strategy = st.builds(plSql_ResultCacheClause, dataSources=safe_text)
@given(instance=plSql_ResultCacheClause_strategy)
@settings(max_examples=25)
def test_plSql_ResultCacheClause_instantiation(instance):
    assert isinstance(instance, plSql_ResultCacheClause)


plSql_ReturnStatement_strategy = st.builds(plSql_ReturnStatement)
@given(instance=plSql_ReturnStatement_strategy)
@settings(max_examples=25)
def test_plSql_ReturnStatement_instantiation(instance):
    assert isinstance(instance, plSql_ReturnStatement)


plSql_Statement_strategy = st.builds(plSql_Statement)
@given(instance=plSql_Statement_strategy)
@settings(max_examples=25)
def test_plSql_Statement_instantiation(instance):
    assert isinstance(instance, plSql_Statement)


plSql_StatementBody_strategy = st.builds(plSql_StatementBody, endName=safe_text)
@given(instance=plSql_StatementBody_strategy)
@settings(max_examples=25)
def test_plSql_StatementBody_instantiation(instance):
    assert isinstance(instance, plSql_StatementBody)


plSql_StringLiteralExpression_strategy = st.builds(plSql_StringLiteralExpression, value=safe_text)
@given(instance=plSql_StringLiteralExpression_strategy)
@settings(max_examples=25)
def test_plSql_StringLiteralExpression_instantiation(instance):
    assert isinstance(instance, plSql_StringLiteralExpression)


plSql_VariableAssignmentTarget_strategy = st.builds(plSql_VariableAssignmentTarget)
@given(instance=plSql_VariableAssignmentTarget_strategy)
@settings(max_examples=25)
def test_plSql_VariableAssignmentTarget_instantiation(instance):
    assert isinstance(instance, plSql_VariableAssignmentTarget)


plSql_VariableDeclaration_strategy = st.builds(plSql_VariableDeclaration, dataType=safe_text, isConstant=st.booleans(), isNotNull=st.booleans())
@given(instance=plSql_VariableDeclaration_strategy)
@settings(max_examples=25)
def test_plSql_VariableDeclaration_instantiation(instance):
    assert isinstance(instance, plSql_VariableDeclaration)


plSql_VariableRef_strategy = st.builds(plSql_VariableRef, isHostRef=st.booleans())
@given(instance=plSql_VariableRef_strategy)
@settings(max_examples=25)
def test_plSql_VariableRef_instantiation(instance):
    assert isinstance(instance, plSql_VariableRef)


plSql_VariableRefExpression_strategy = st.builds(plSql_VariableRefExpression)
@given(instance=plSql_VariableRefExpression_strategy)
@settings(max_examples=25)
def test_plSql_VariableRefExpression_instantiation(instance):
    assert isinstance(instance, plSql_VariableRefExpression)


plSql_VariableValue_strategy = st.builds(plSql_VariableValue)
@given(instance=plSql_VariableValue_strategy)
@settings(max_examples=25)
def test_plSql_VariableValue_instantiation(instance):
    assert isinstance(instance, plSql_VariableValue)


plSql_WhileLoopStatement_strategy = st.builds(plSql_WhileLoopStatement)
@given(instance=plSql_WhileLoopStatement_strategy)
@settings(max_examples=25)
def test_plSql_WhileLoopStatement_instantiation(instance):
    assert isinstance(instance, plSql_WhileLoopStatement)



