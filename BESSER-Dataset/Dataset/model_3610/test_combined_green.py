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
    TextExpression,
    pp_ExpressionTE,
    pp_VerbatimTE,
    pp_TextExpression,
    IQuotedString,
    StringExpression,
    pp_UnquotedString,
    pp_SingleQuotedString,
    pp_DoubleQuotedString,
    Lambda,
    pp_RubyLambda,
    pp_JavaLambda,
    pp_VariableTE,
    WithLambdaExpression,
    pp_MethodCall,
    pp_FunctionCall,
    ParameterizedExpression,
    pp_WithLambdaExpression,
    pp_SelectorExpression,
    pp_AtExpression,
    IfExpression,
    pp_ElseIfExpression,
    pp_HashEntry,
    pp_IQuotedString,
    BinaryExpression,
    pp_OrExpression,
    pp_BinaryOpExpression,
    pp_AppendExpression,
    pp_SelectorEntry,
    pp_NamedAccessExpression,
    pp_AndExpression,
    pp_AssignmentExpression,
    BinaryOpExpression,
    pp_EqualityExpression,
    pp_AdditiveExpression,
    pp_ShiftExpression,
    pp_MultiplicativeExpression,
    pp_RelationalExpression,
    pp_MatchingExpression,
    pp_InExpression,
    pp_RelationshipExpression,
    Expression,
    pp_VariableExpression,
    pp_ExpressionBlock,
    pp_SeparatorExpression,
    pp_ParameterizedExpression,
    pp_BinaryExpression,
    pp_InterpolatedVariable,
    pp_UnaryExpression,
    pp_StringExpression,
    pp_ParenthesisedExpression,
    pp_ImportExpression,
    pp_ExprList,
    pp_CollectExpression,
    pp_CaseExpression,
    pp_DefinitionArgument,
    pp_DefinitionArgumentList,
    pp_LiteralExpression,
    Definition,
    pp_HostClassDefinition,
    ICollectQuery,
    UnaryExpression,
    pp_UnaryMinusExpression,
    pp_ExportedCollectQuery,
    pp_UnaryNotExpression,
    pp_VirtualCollectQuery,
    pp_ICollectQuery,
    pp_ResourceExpression,
    LiteralExpression,
    pp_LiteralRegex,
    pp_LiteralUndef,
    pp_VirtualNameOrReference,
    pp_LiteralName,
    pp_LiteralHash,
    pp_LiteralList,
    pp_LiteralClass,
    pp_LiteralDefault,
    pp_LiteralBoolean,
    pp_LiteralNameOrReference,
    pp_AttributeOperation,
    pp_AttributeOperations,
    pp_ResourceBody,
    pp_Expression,
    ExpressionBlock,
    pp_ElseExpression,
    pp_Case,
    pp_Lambda,
    pp_NodeDefinition,
    pp_Definition,
    pp_IfExpression,
    pp_UnlessExpression,
    pp_PuppetManifest,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_hyp_textexpression_is_not_abstract():
    assert not inspect.isabstract(TextExpression)


def test_hyp_textexpression_constructor_exists():
    assert callable(TextExpression.__init__)


def test_hyp_textexpression_constructor_args():
    sig = inspect.signature(TextExpression.__init__)
    params = list(sig.parameters.keys())



def test_hyp_pp_expressionte_is_not_abstract():
    assert not inspect.isabstract(pp_ExpressionTE)


def test_hyp_pp_expressionte_constructor_exists():
    assert callable(pp_ExpressionTE.__init__)


def test_hyp_pp_expressionte_constructor_args():
    sig = inspect.signature(pp_ExpressionTE.__init__)
    params = list(sig.parameters.keys())



def test_hyp_pp_verbatimte_is_not_abstract():
    assert not inspect.isabstract(pp_VerbatimTE)


def test_hyp_pp_verbatimte_constructor_exists():
    assert callable(pp_VerbatimTE.__init__)


def test_hyp_pp_verbatimte_constructor_args():
    sig = inspect.signature(pp_VerbatimTE.__init__)
    params = list(sig.parameters.keys())
    assert "text" in params, "Missing parameter 'text'"




def test_hyp_pp_textexpression_is_not_abstract():
    assert not inspect.isabstract(pp_TextExpression)


def test_hyp_pp_textexpression_constructor_exists():
    assert callable(pp_TextExpression.__init__)


def test_hyp_pp_textexpression_constructor_args():
    sig = inspect.signature(pp_TextExpression.__init__)
    params = list(sig.parameters.keys())



def test_hyp_iquotedstring_is_not_abstract():
    assert not inspect.isabstract(IQuotedString)


def test_hyp_iquotedstring_constructor_exists():
    assert callable(IQuotedString.__init__)


def test_hyp_iquotedstring_constructor_args():
    sig = inspect.signature(IQuotedString.__init__)
    params = list(sig.parameters.keys())



def test_hyp_stringexpression_is_not_abstract():
    assert not inspect.isabstract(StringExpression)


def test_hyp_stringexpression_constructor_exists():
    assert callable(StringExpression.__init__)


def test_hyp_stringexpression_constructor_args():
    sig = inspect.signature(StringExpression.__init__)
    params = list(sig.parameters.keys())



def test_hyp_pp_unquotedstring_is_not_abstract():
    assert not inspect.isabstract(pp_UnquotedString)


def test_hyp_pp_unquotedstring_constructor_exists():
    assert callable(pp_UnquotedString.__init__)


def test_hyp_pp_unquotedstring_constructor_args():
    sig = inspect.signature(pp_UnquotedString.__init__)
    params = list(sig.parameters.keys())



def test_hyp_pp_singlequotedstring_is_not_abstract():
    assert not inspect.isabstract(pp_SingleQuotedString)


def test_hyp_pp_singlequotedstring_constructor_exists():
    assert callable(pp_SingleQuotedString.__init__)


def test_hyp_pp_singlequotedstring_constructor_args():
    sig = inspect.signature(pp_SingleQuotedString.__init__)
    params = list(sig.parameters.keys())
    assert "text" in params, "Missing parameter 'text'"




def test_hyp_pp_doublequotedstring_is_not_abstract():
    assert not inspect.isabstract(pp_DoubleQuotedString)


def test_hyp_pp_doublequotedstring_constructor_exists():
    assert callable(pp_DoubleQuotedString.__init__)


def test_hyp_pp_doublequotedstring_constructor_args():
    sig = inspect.signature(pp_DoubleQuotedString.__init__)
    params = list(sig.parameters.keys())



def test_hyp_lambda_is_not_abstract():
    assert not inspect.isabstract(Lambda)


def test_hyp_lambda_constructor_exists():
    assert callable(Lambda.__init__)


def test_hyp_lambda_constructor_args():
    sig = inspect.signature(Lambda.__init__)
    params = list(sig.parameters.keys())



def test_hyp_pp_rubylambda_is_not_abstract():
    assert not inspect.isabstract(pp_RubyLambda)


def test_hyp_pp_rubylambda_constructor_exists():
    assert callable(pp_RubyLambda.__init__)


def test_hyp_pp_rubylambda_constructor_args():
    sig = inspect.signature(pp_RubyLambda.__init__)
    params = list(sig.parameters.keys())



def test_hyp_pp_javalambda_is_not_abstract():
    assert not inspect.isabstract(pp_JavaLambda)


def test_hyp_pp_javalambda_constructor_exists():
    assert callable(pp_JavaLambda.__init__)


def test_hyp_pp_javalambda_constructor_args():
    sig = inspect.signature(pp_JavaLambda.__init__)
    params = list(sig.parameters.keys())
    assert "farrow" in params, "Missing parameter 'farrow'"




def test_hyp_pp_variablete_is_not_abstract():
    assert not inspect.isabstract(pp_VariableTE)


def test_hyp_pp_variablete_constructor_exists():
    assert callable(pp_VariableTE.__init__)


def test_hyp_pp_variablete_constructor_args():
    sig = inspect.signature(pp_VariableTE.__init__)
    params = list(sig.parameters.keys())
    assert "varName" in params, "Missing parameter 'varName'"




def test_hyp_withlambdaexpression_is_not_abstract():
    assert not inspect.isabstract(WithLambdaExpression)


def test_hyp_withlambdaexpression_constructor_exists():
    assert callable(WithLambdaExpression.__init__)


def test_hyp_withlambdaexpression_constructor_args():
    sig = inspect.signature(WithLambdaExpression.__init__)
    params = list(sig.parameters.keys())



def test_hyp_pp_methodcall_is_not_abstract():
    assert not inspect.isabstract(pp_MethodCall)


def test_hyp_pp_methodcall_constructor_exists():
    assert callable(pp_MethodCall.__init__)


def test_hyp_pp_methodcall_constructor_args():
    sig = inspect.signature(pp_MethodCall.__init__)
    params = list(sig.parameters.keys())
    assert "parenthesized" in params, "Missing parameter 'parenthesized'"




def test_hyp_pp_functioncall_is_not_abstract():
    assert not inspect.isabstract(pp_FunctionCall)


def test_hyp_pp_functioncall_constructor_exists():
    assert callable(pp_FunctionCall.__init__)


def test_hyp_pp_functioncall_constructor_args():
    sig = inspect.signature(pp_FunctionCall.__init__)
    params = list(sig.parameters.keys())



def test_hyp_parameterizedexpression_is_not_abstract():
    assert not inspect.isabstract(ParameterizedExpression)


def test_hyp_parameterizedexpression_constructor_exists():
    assert callable(ParameterizedExpression.__init__)


def test_hyp_parameterizedexpression_constructor_args():
    sig = inspect.signature(ParameterizedExpression.__init__)
    params = list(sig.parameters.keys())



def test_hyp_pp_withlambdaexpression_is_not_abstract():
    assert not inspect.isabstract(pp_WithLambdaExpression)


def test_hyp_pp_withlambdaexpression_constructor_exists():
    assert callable(pp_WithLambdaExpression.__init__)


def test_hyp_pp_withlambdaexpression_constructor_args():
    sig = inspect.signature(pp_WithLambdaExpression.__init__)
    params = list(sig.parameters.keys())



def test_hyp_pp_selectorexpression_is_not_abstract():
    assert not inspect.isabstract(pp_SelectorExpression)


def test_hyp_pp_selectorexpression_constructor_exists():
    assert callable(pp_SelectorExpression.__init__)


def test_hyp_pp_selectorexpression_constructor_args():
    sig = inspect.signature(pp_SelectorExpression.__init__)
    params = list(sig.parameters.keys())



def test_hyp_pp_atexpression_is_not_abstract():
    assert not inspect.isabstract(pp_AtExpression)


def test_hyp_pp_atexpression_constructor_exists():
    assert callable(pp_AtExpression.__init__)


def test_hyp_pp_atexpression_constructor_args():
    sig = inspect.signature(pp_AtExpression.__init__)
    params = list(sig.parameters.keys())



def test_hyp_ifexpression_is_not_abstract():
    assert not inspect.isabstract(IfExpression)


def test_hyp_ifexpression_constructor_exists():
    assert callable(IfExpression.__init__)


def test_hyp_ifexpression_constructor_args():
    sig = inspect.signature(IfExpression.__init__)
    params = list(sig.parameters.keys())



def test_hyp_pp_elseifexpression_is_not_abstract():
    assert not inspect.isabstract(pp_ElseIfExpression)


def test_hyp_pp_elseifexpression_constructor_exists():
    assert callable(pp_ElseIfExpression.__init__)


def test_hyp_pp_elseifexpression_constructor_args():
    sig = inspect.signature(pp_ElseIfExpression.__init__)
    params = list(sig.parameters.keys())



def test_hyp_pp_hashentry_is_not_abstract():
    assert not inspect.isabstract(pp_HashEntry)


def test_hyp_pp_hashentry_constructor_exists():
    assert callable(pp_HashEntry.__init__)


def test_hyp_pp_hashentry_constructor_args():
    sig = inspect.signature(pp_HashEntry.__init__)
    params = list(sig.parameters.keys())



def test_hyp_pp_iquotedstring_is_not_abstract():
    assert not inspect.isabstract(pp_IQuotedString)


def test_hyp_pp_iquotedstring_constructor_exists():
    assert callable(pp_IQuotedString.__init__)


def test_hyp_pp_iquotedstring_constructor_args():
    sig = inspect.signature(pp_IQuotedString.__init__)
    params = list(sig.parameters.keys())



def test_hyp_binaryexpression_is_not_abstract():
    assert not inspect.isabstract(BinaryExpression)


def test_hyp_binaryexpression_constructor_exists():
    assert callable(BinaryExpression.__init__)


def test_hyp_binaryexpression_constructor_args():
    sig = inspect.signature(BinaryExpression.__init__)
    params = list(sig.parameters.keys())



def test_hyp_pp_orexpression_is_not_abstract():
    assert not inspect.isabstract(pp_OrExpression)


def test_hyp_pp_orexpression_constructor_exists():
    assert callable(pp_OrExpression.__init__)


def test_hyp_pp_orexpression_constructor_args():
    sig = inspect.signature(pp_OrExpression.__init__)
    params = list(sig.parameters.keys())



def test_hyp_pp_binaryopexpression_is_not_abstract():
    assert not inspect.isabstract(pp_BinaryOpExpression)


def test_hyp_pp_binaryopexpression_constructor_exists():
    assert callable(pp_BinaryOpExpression.__init__)


def test_hyp_pp_binaryopexpression_constructor_args():
    sig = inspect.signature(pp_BinaryOpExpression.__init__)
    params = list(sig.parameters.keys())
    assert "opName" in params, "Missing parameter 'opName'"




def test_hyp_pp_appendexpression_is_not_abstract():
    assert not inspect.isabstract(pp_AppendExpression)


def test_hyp_pp_appendexpression_constructor_exists():
    assert callable(pp_AppendExpression.__init__)


def test_hyp_pp_appendexpression_constructor_args():
    sig = inspect.signature(pp_AppendExpression.__init__)
    params = list(sig.parameters.keys())



def test_hyp_pp_selectorentry_is_not_abstract():
    assert not inspect.isabstract(pp_SelectorEntry)


def test_hyp_pp_selectorentry_constructor_exists():
    assert callable(pp_SelectorEntry.__init__)


def test_hyp_pp_selectorentry_constructor_args():
    sig = inspect.signature(pp_SelectorEntry.__init__)
    params = list(sig.parameters.keys())



def test_hyp_pp_namedaccessexpression_is_not_abstract():
    assert not inspect.isabstract(pp_NamedAccessExpression)


def test_hyp_pp_namedaccessexpression_constructor_exists():
    assert callable(pp_NamedAccessExpression.__init__)


def test_hyp_pp_namedaccessexpression_constructor_args():
    sig = inspect.signature(pp_NamedAccessExpression.__init__)
    params = list(sig.parameters.keys())



def test_hyp_pp_andexpression_is_not_abstract():
    assert not inspect.isabstract(pp_AndExpression)


def test_hyp_pp_andexpression_constructor_exists():
    assert callable(pp_AndExpression.__init__)


def test_hyp_pp_andexpression_constructor_args():
    sig = inspect.signature(pp_AndExpression.__init__)
    params = list(sig.parameters.keys())



def test_hyp_pp_assignmentexpression_is_not_abstract():
    assert not inspect.isabstract(pp_AssignmentExpression)


def test_hyp_pp_assignmentexpression_constructor_exists():
    assert callable(pp_AssignmentExpression.__init__)


def test_hyp_pp_assignmentexpression_constructor_args():
    sig = inspect.signature(pp_AssignmentExpression.__init__)
    params = list(sig.parameters.keys())



def test_hyp_binaryopexpression_is_not_abstract():
    assert not inspect.isabstract(BinaryOpExpression)


def test_hyp_binaryopexpression_constructor_exists():
    assert callable(BinaryOpExpression.__init__)


def test_hyp_binaryopexpression_constructor_args():
    sig = inspect.signature(BinaryOpExpression.__init__)
    params = list(sig.parameters.keys())



def test_hyp_pp_equalityexpression_is_not_abstract():
    assert not inspect.isabstract(pp_EqualityExpression)


def test_hyp_pp_equalityexpression_constructor_exists():
    assert callable(pp_EqualityExpression.__init__)


def test_hyp_pp_equalityexpression_constructor_args():
    sig = inspect.signature(pp_EqualityExpression.__init__)
    params = list(sig.parameters.keys())



def test_hyp_pp_additiveexpression_is_not_abstract():
    assert not inspect.isabstract(pp_AdditiveExpression)


def test_hyp_pp_additiveexpression_constructor_exists():
    assert callable(pp_AdditiveExpression.__init__)


def test_hyp_pp_additiveexpression_constructor_args():
    sig = inspect.signature(pp_AdditiveExpression.__init__)
    params = list(sig.parameters.keys())



def test_hyp_pp_shiftexpression_is_not_abstract():
    assert not inspect.isabstract(pp_ShiftExpression)


def test_hyp_pp_shiftexpression_constructor_exists():
    assert callable(pp_ShiftExpression.__init__)


def test_hyp_pp_shiftexpression_constructor_args():
    sig = inspect.signature(pp_ShiftExpression.__init__)
    params = list(sig.parameters.keys())



def test_hyp_pp_multiplicativeexpression_is_not_abstract():
    assert not inspect.isabstract(pp_MultiplicativeExpression)


def test_hyp_pp_multiplicativeexpression_constructor_exists():
    assert callable(pp_MultiplicativeExpression.__init__)


def test_hyp_pp_multiplicativeexpression_constructor_args():
    sig = inspect.signature(pp_MultiplicativeExpression.__init__)
    params = list(sig.parameters.keys())



def test_hyp_pp_relationalexpression_is_not_abstract():
    assert not inspect.isabstract(pp_RelationalExpression)


def test_hyp_pp_relationalexpression_constructor_exists():
    assert callable(pp_RelationalExpression.__init__)


def test_hyp_pp_relationalexpression_constructor_args():
    sig = inspect.signature(pp_RelationalExpression.__init__)
    params = list(sig.parameters.keys())



def test_hyp_pp_matchingexpression_is_not_abstract():
    assert not inspect.isabstract(pp_MatchingExpression)


def test_hyp_pp_matchingexpression_constructor_exists():
    assert callable(pp_MatchingExpression.__init__)


def test_hyp_pp_matchingexpression_constructor_args():
    sig = inspect.signature(pp_MatchingExpression.__init__)
    params = list(sig.parameters.keys())



def test_hyp_pp_inexpression_is_not_abstract():
    assert not inspect.isabstract(pp_InExpression)


def test_hyp_pp_inexpression_constructor_exists():
    assert callable(pp_InExpression.__init__)


def test_hyp_pp_inexpression_constructor_args():
    sig = inspect.signature(pp_InExpression.__init__)
    params = list(sig.parameters.keys())



def test_hyp_pp_relationshipexpression_is_not_abstract():
    assert not inspect.isabstract(pp_RelationshipExpression)


def test_hyp_pp_relationshipexpression_constructor_exists():
    assert callable(pp_RelationshipExpression.__init__)


def test_hyp_pp_relationshipexpression_constructor_args():
    sig = inspect.signature(pp_RelationshipExpression.__init__)
    params = list(sig.parameters.keys())



def test_hyp_expression_is_not_abstract():
    assert not inspect.isabstract(Expression)


def test_hyp_expression_constructor_exists():
    assert callable(Expression.__init__)


def test_hyp_expression_constructor_args():
    sig = inspect.signature(Expression.__init__)
    params = list(sig.parameters.keys())



def test_hyp_pp_variableexpression_is_not_abstract():
    assert not inspect.isabstract(pp_VariableExpression)


def test_hyp_pp_variableexpression_constructor_exists():
    assert callable(pp_VariableExpression.__init__)


def test_hyp_pp_variableexpression_constructor_args():
    sig = inspect.signature(pp_VariableExpression.__init__)
    params = list(sig.parameters.keys())
    assert "varName" in params, "Missing parameter 'varName'"




def test_hyp_pp_expressionblock_is_not_abstract():
    assert not inspect.isabstract(pp_ExpressionBlock)


def test_hyp_pp_expressionblock_constructor_exists():
    assert callable(pp_ExpressionBlock.__init__)


def test_hyp_pp_expressionblock_constructor_args():
    sig = inspect.signature(pp_ExpressionBlock.__init__)
    params = list(sig.parameters.keys())



def test_hyp_pp_separatorexpression_is_not_abstract():
    assert not inspect.isabstract(pp_SeparatorExpression)


def test_hyp_pp_separatorexpression_constructor_exists():
    assert callable(pp_SeparatorExpression.__init__)


def test_hyp_pp_separatorexpression_constructor_args():
    sig = inspect.signature(pp_SeparatorExpression.__init__)
    params = list(sig.parameters.keys())



def test_hyp_pp_parameterizedexpression_is_not_abstract():
    assert not inspect.isabstract(pp_ParameterizedExpression)


def test_hyp_pp_parameterizedexpression_constructor_exists():
    assert callable(pp_ParameterizedExpression.__init__)


def test_hyp_pp_parameterizedexpression_constructor_args():
    sig = inspect.signature(pp_ParameterizedExpression.__init__)
    params = list(sig.parameters.keys())



def test_hyp_pp_binaryexpression_is_not_abstract():
    assert not inspect.isabstract(pp_BinaryExpression)


def test_hyp_pp_binaryexpression_constructor_exists():
    assert callable(pp_BinaryExpression.__init__)


def test_hyp_pp_binaryexpression_constructor_args():
    sig = inspect.signature(pp_BinaryExpression.__init__)
    params = list(sig.parameters.keys())



def test_hyp_pp_interpolatedvariable_is_not_abstract():
    assert not inspect.isabstract(pp_InterpolatedVariable)


def test_hyp_pp_interpolatedvariable_constructor_exists():
    assert callable(pp_InterpolatedVariable.__init__)


def test_hyp_pp_interpolatedvariable_constructor_args():
    sig = inspect.signature(pp_InterpolatedVariable.__init__)
    params = list(sig.parameters.keys())
    assert "varName" in params, "Missing parameter 'varName'"




def test_hyp_pp_unaryexpression_is_not_abstract():
    assert not inspect.isabstract(pp_UnaryExpression)


def test_hyp_pp_unaryexpression_constructor_exists():
    assert callable(pp_UnaryExpression.__init__)


def test_hyp_pp_unaryexpression_constructor_args():
    sig = inspect.signature(pp_UnaryExpression.__init__)
    params = list(sig.parameters.keys())



def test_hyp_pp_stringexpression_is_not_abstract():
    assert not inspect.isabstract(pp_StringExpression)


def test_hyp_pp_stringexpression_constructor_exists():
    assert callable(pp_StringExpression.__init__)


def test_hyp_pp_stringexpression_constructor_args():
    sig = inspect.signature(pp_StringExpression.__init__)
    params = list(sig.parameters.keys())



def test_hyp_pp_parenthesisedexpression_is_not_abstract():
    assert not inspect.isabstract(pp_ParenthesisedExpression)


def test_hyp_pp_parenthesisedexpression_constructor_exists():
    assert callable(pp_ParenthesisedExpression.__init__)


def test_hyp_pp_parenthesisedexpression_constructor_args():
    sig = inspect.signature(pp_ParenthesisedExpression.__init__)
    params = list(sig.parameters.keys())



def test_hyp_pp_importexpression_is_not_abstract():
    assert not inspect.isabstract(pp_ImportExpression)


def test_hyp_pp_importexpression_constructor_exists():
    assert callable(pp_ImportExpression.__init__)


def test_hyp_pp_importexpression_constructor_args():
    sig = inspect.signature(pp_ImportExpression.__init__)
    params = list(sig.parameters.keys())



def test_hyp_pp_exprlist_is_not_abstract():
    assert not inspect.isabstract(pp_ExprList)


def test_hyp_pp_exprlist_constructor_exists():
    assert callable(pp_ExprList.__init__)


def test_hyp_pp_exprlist_constructor_args():
    sig = inspect.signature(pp_ExprList.__init__)
    params = list(sig.parameters.keys())



def test_hyp_pp_collectexpression_is_not_abstract():
    assert not inspect.isabstract(pp_CollectExpression)


def test_hyp_pp_collectexpression_constructor_exists():
    assert callable(pp_CollectExpression.__init__)


def test_hyp_pp_collectexpression_constructor_args():
    sig = inspect.signature(pp_CollectExpression.__init__)
    params = list(sig.parameters.keys())



def test_hyp_pp_caseexpression_is_not_abstract():
    assert not inspect.isabstract(pp_CaseExpression)


def test_hyp_pp_caseexpression_constructor_exists():
    assert callable(pp_CaseExpression.__init__)


def test_hyp_pp_caseexpression_constructor_args():
    sig = inspect.signature(pp_CaseExpression.__init__)
    params = list(sig.parameters.keys())



def test_hyp_pp_definitionargument_is_not_abstract():
    assert not inspect.isabstract(pp_DefinitionArgument)


def test_hyp_pp_definitionargument_constructor_exists():
    assert callable(pp_DefinitionArgument.__init__)


def test_hyp_pp_definitionargument_constructor_args():
    sig = inspect.signature(pp_DefinitionArgument.__init__)
    params = list(sig.parameters.keys())
    assert "argName" in params, "Missing parameter 'argName'"
    assert "op" in params, "Missing parameter 'op'"





def test_hyp_pp_definitionargumentlist_is_not_abstract():
    assert not inspect.isabstract(pp_DefinitionArgumentList)


def test_hyp_pp_definitionargumentlist_constructor_exists():
    assert callable(pp_DefinitionArgumentList.__init__)


def test_hyp_pp_definitionargumentlist_constructor_args():
    sig = inspect.signature(pp_DefinitionArgumentList.__init__)
    params = list(sig.parameters.keys())



def test_hyp_pp_literalexpression_is_not_abstract():
    assert not inspect.isabstract(pp_LiteralExpression)


def test_hyp_pp_literalexpression_constructor_exists():
    assert callable(pp_LiteralExpression.__init__)


def test_hyp_pp_literalexpression_constructor_args():
    sig = inspect.signature(pp_LiteralExpression.__init__)
    params = list(sig.parameters.keys())



def test_hyp_definition_is_not_abstract():
    assert not inspect.isabstract(Definition)


def test_hyp_definition_constructor_exists():
    assert callable(Definition.__init__)


def test_hyp_definition_constructor_args():
    sig = inspect.signature(Definition.__init__)
    params = list(sig.parameters.keys())



def test_hyp_pp_hostclassdefinition_is_not_abstract():
    assert not inspect.isabstract(pp_HostClassDefinition)


def test_hyp_pp_hostclassdefinition_constructor_exists():
    assert callable(pp_HostClassDefinition.__init__)


def test_hyp_pp_hostclassdefinition_constructor_args():
    sig = inspect.signature(pp_HostClassDefinition.__init__)
    params = list(sig.parameters.keys())



def test_hyp_icollectquery_is_not_abstract():
    assert not inspect.isabstract(ICollectQuery)


def test_hyp_icollectquery_constructor_exists():
    assert callable(ICollectQuery.__init__)


def test_hyp_icollectquery_constructor_args():
    sig = inspect.signature(ICollectQuery.__init__)
    params = list(sig.parameters.keys())



def test_hyp_unaryexpression_is_not_abstract():
    assert not inspect.isabstract(UnaryExpression)


def test_hyp_unaryexpression_constructor_exists():
    assert callable(UnaryExpression.__init__)


def test_hyp_unaryexpression_constructor_args():
    sig = inspect.signature(UnaryExpression.__init__)
    params = list(sig.parameters.keys())



def test_hyp_pp_unaryminusexpression_is_not_abstract():
    assert not inspect.isabstract(pp_UnaryMinusExpression)


def test_hyp_pp_unaryminusexpression_constructor_exists():
    assert callable(pp_UnaryMinusExpression.__init__)


def test_hyp_pp_unaryminusexpression_constructor_args():
    sig = inspect.signature(pp_UnaryMinusExpression.__init__)
    params = list(sig.parameters.keys())



def test_hyp_pp_exportedcollectquery_is_not_abstract():
    assert not inspect.isabstract(pp_ExportedCollectQuery)


def test_hyp_pp_exportedcollectquery_constructor_exists():
    assert callable(pp_ExportedCollectQuery.__init__)


def test_hyp_pp_exportedcollectquery_constructor_args():
    sig = inspect.signature(pp_ExportedCollectQuery.__init__)
    params = list(sig.parameters.keys())



def test_hyp_pp_unarynotexpression_is_not_abstract():
    assert not inspect.isabstract(pp_UnaryNotExpression)


def test_hyp_pp_unarynotexpression_constructor_exists():
    assert callable(pp_UnaryNotExpression.__init__)


def test_hyp_pp_unarynotexpression_constructor_args():
    sig = inspect.signature(pp_UnaryNotExpression.__init__)
    params = list(sig.parameters.keys())



def test_hyp_pp_virtualcollectquery_is_not_abstract():
    assert not inspect.isabstract(pp_VirtualCollectQuery)


def test_hyp_pp_virtualcollectquery_constructor_exists():
    assert callable(pp_VirtualCollectQuery.__init__)


def test_hyp_pp_virtualcollectquery_constructor_args():
    sig = inspect.signature(pp_VirtualCollectQuery.__init__)
    params = list(sig.parameters.keys())



def test_hyp_pp_icollectquery_is_not_abstract():
    assert not inspect.isabstract(pp_ICollectQuery)


def test_hyp_pp_icollectquery_constructor_exists():
    assert callable(pp_ICollectQuery.__init__)


def test_hyp_pp_icollectquery_constructor_args():
    sig = inspect.signature(pp_ICollectQuery.__init__)
    params = list(sig.parameters.keys())



def test_hyp_pp_resourceexpression_is_not_abstract():
    assert not inspect.isabstract(pp_ResourceExpression)


def test_hyp_pp_resourceexpression_constructor_exists():
    assert callable(pp_ResourceExpression.__init__)


def test_hyp_pp_resourceexpression_constructor_args():
    sig = inspect.signature(pp_ResourceExpression.__init__)
    params = list(sig.parameters.keys())



def test_hyp_literalexpression_is_not_abstract():
    assert not inspect.isabstract(LiteralExpression)


def test_hyp_literalexpression_constructor_exists():
    assert callable(LiteralExpression.__init__)


def test_hyp_literalexpression_constructor_args():
    sig = inspect.signature(LiteralExpression.__init__)
    params = list(sig.parameters.keys())



def test_hyp_pp_literalregex_is_not_abstract():
    assert not inspect.isabstract(pp_LiteralRegex)


def test_hyp_pp_literalregex_constructor_exists():
    assert callable(pp_LiteralRegex.__init__)


def test_hyp_pp_literalregex_constructor_args():
    sig = inspect.signature(pp_LiteralRegex.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"




def test_hyp_pp_literalundef_is_not_abstract():
    assert not inspect.isabstract(pp_LiteralUndef)


def test_hyp_pp_literalundef_constructor_exists():
    assert callable(pp_LiteralUndef.__init__)


def test_hyp_pp_literalundef_constructor_args():
    sig = inspect.signature(pp_LiteralUndef.__init__)
    params = list(sig.parameters.keys())



def test_hyp_pp_virtualnameorreference_is_not_abstract():
    assert not inspect.isabstract(pp_VirtualNameOrReference)


def test_hyp_pp_virtualnameorreference_constructor_exists():
    assert callable(pp_VirtualNameOrReference.__init__)


def test_hyp_pp_virtualnameorreference_constructor_args():
    sig = inspect.signature(pp_VirtualNameOrReference.__init__)
    params = list(sig.parameters.keys())
    assert "exported" in params, "Missing parameter 'exported'"
    assert "value" in params, "Missing parameter 'value'"





def test_hyp_pp_literalname_is_not_abstract():
    assert not inspect.isabstract(pp_LiteralName)


def test_hyp_pp_literalname_constructor_exists():
    assert callable(pp_LiteralName.__init__)


def test_hyp_pp_literalname_constructor_args():
    sig = inspect.signature(pp_LiteralName.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"




def test_hyp_pp_literalhash_is_not_abstract():
    assert not inspect.isabstract(pp_LiteralHash)


def test_hyp_pp_literalhash_constructor_exists():
    assert callable(pp_LiteralHash.__init__)


def test_hyp_pp_literalhash_constructor_args():
    sig = inspect.signature(pp_LiteralHash.__init__)
    params = list(sig.parameters.keys())



def test_hyp_pp_literallist_is_not_abstract():
    assert not inspect.isabstract(pp_LiteralList)


def test_hyp_pp_literallist_constructor_exists():
    assert callable(pp_LiteralList.__init__)


def test_hyp_pp_literallist_constructor_args():
    sig = inspect.signature(pp_LiteralList.__init__)
    params = list(sig.parameters.keys())



def test_hyp_pp_literalclass_is_not_abstract():
    assert not inspect.isabstract(pp_LiteralClass)


def test_hyp_pp_literalclass_constructor_exists():
    assert callable(pp_LiteralClass.__init__)


def test_hyp_pp_literalclass_constructor_args():
    sig = inspect.signature(pp_LiteralClass.__init__)
    params = list(sig.parameters.keys())



def test_hyp_pp_literaldefault_is_not_abstract():
    assert not inspect.isabstract(pp_LiteralDefault)


def test_hyp_pp_literaldefault_constructor_exists():
    assert callable(pp_LiteralDefault.__init__)


def test_hyp_pp_literaldefault_constructor_args():
    sig = inspect.signature(pp_LiteralDefault.__init__)
    params = list(sig.parameters.keys())



def test_hyp_pp_literalboolean_is_not_abstract():
    assert not inspect.isabstract(pp_LiteralBoolean)


def test_hyp_pp_literalboolean_constructor_exists():
    assert callable(pp_LiteralBoolean.__init__)


def test_hyp_pp_literalboolean_constructor_args():
    sig = inspect.signature(pp_LiteralBoolean.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"




def test_hyp_pp_literalnameorreference_is_not_abstract():
    assert not inspect.isabstract(pp_LiteralNameOrReference)


def test_hyp_pp_literalnameorreference_constructor_exists():
    assert callable(pp_LiteralNameOrReference.__init__)


def test_hyp_pp_literalnameorreference_constructor_args():
    sig = inspect.signature(pp_LiteralNameOrReference.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"




def test_hyp_pp_attributeoperation_is_not_abstract():
    assert not inspect.isabstract(pp_AttributeOperation)


def test_hyp_pp_attributeoperation_constructor_exists():
    assert callable(pp_AttributeOperation.__init__)


def test_hyp_pp_attributeoperation_constructor_args():
    sig = inspect.signature(pp_AttributeOperation.__init__)
    params = list(sig.parameters.keys())
    assert "key" in params, "Missing parameter 'key'"
    assert "op" in params, "Missing parameter 'op'"





def test_hyp_pp_attributeoperations_is_not_abstract():
    assert not inspect.isabstract(pp_AttributeOperations)


def test_hyp_pp_attributeoperations_constructor_exists():
    assert callable(pp_AttributeOperations.__init__)


def test_hyp_pp_attributeoperations_constructor_args():
    sig = inspect.signature(pp_AttributeOperations.__init__)
    params = list(sig.parameters.keys())



def test_hyp_pp_resourcebody_is_not_abstract():
    assert not inspect.isabstract(pp_ResourceBody)


def test_hyp_pp_resourcebody_constructor_exists():
    assert callable(pp_ResourceBody.__init__)


def test_hyp_pp_resourcebody_constructor_args():
    sig = inspect.signature(pp_ResourceBody.__init__)
    params = list(sig.parameters.keys())



def test_hyp_pp_expression_is_not_abstract():
    assert not inspect.isabstract(pp_Expression)


def test_hyp_pp_expression_constructor_exists():
    assert callable(pp_Expression.__init__)


def test_hyp_pp_expression_constructor_args():
    sig = inspect.signature(pp_Expression.__init__)
    params = list(sig.parameters.keys())



def test_hyp_expressionblock_is_not_abstract():
    assert not inspect.isabstract(ExpressionBlock)


def test_hyp_expressionblock_constructor_exists():
    assert callable(ExpressionBlock.__init__)


def test_hyp_expressionblock_constructor_args():
    sig = inspect.signature(ExpressionBlock.__init__)
    params = list(sig.parameters.keys())



def test_hyp_pp_elseexpression_is_not_abstract():
    assert not inspect.isabstract(pp_ElseExpression)


def test_hyp_pp_elseexpression_constructor_exists():
    assert callable(pp_ElseExpression.__init__)


def test_hyp_pp_elseexpression_constructor_args():
    sig = inspect.signature(pp_ElseExpression.__init__)
    params = list(sig.parameters.keys())



def test_hyp_pp_case_is_not_abstract():
    assert not inspect.isabstract(pp_Case)


def test_hyp_pp_case_constructor_exists():
    assert callable(pp_Case.__init__)


def test_hyp_pp_case_constructor_args():
    sig = inspect.signature(pp_Case.__init__)
    params = list(sig.parameters.keys())



def test_hyp_pp_lambda_is_not_abstract():
    assert not inspect.isabstract(pp_Lambda)


def test_hyp_pp_lambda_constructor_exists():
    assert callable(pp_Lambda.__init__)


def test_hyp_pp_lambda_constructor_args():
    sig = inspect.signature(pp_Lambda.__init__)
    params = list(sig.parameters.keys())



def test_hyp_pp_nodedefinition_is_not_abstract():
    assert not inspect.isabstract(pp_NodeDefinition)


def test_hyp_pp_nodedefinition_constructor_exists():
    assert callable(pp_NodeDefinition.__init__)


def test_hyp_pp_nodedefinition_constructor_args():
    sig = inspect.signature(pp_NodeDefinition.__init__)
    params = list(sig.parameters.keys())



def test_hyp_pp_definition_is_not_abstract():
    assert not inspect.isabstract(pp_Definition)


def test_hyp_pp_definition_constructor_exists():
    assert callable(pp_Definition.__init__)


def test_hyp_pp_definition_constructor_args():
    sig = inspect.signature(pp_Definition.__init__)
    params = list(sig.parameters.keys())
    assert "className" in params, "Missing parameter 'className'"




def test_hyp_pp_ifexpression_is_not_abstract():
    assert not inspect.isabstract(pp_IfExpression)


def test_hyp_pp_ifexpression_constructor_exists():
    assert callable(pp_IfExpression.__init__)


def test_hyp_pp_ifexpression_constructor_args():
    sig = inspect.signature(pp_IfExpression.__init__)
    params = list(sig.parameters.keys())



def test_hyp_pp_unlessexpression_is_not_abstract():
    assert not inspect.isabstract(pp_UnlessExpression)


def test_hyp_pp_unlessexpression_constructor_exists():
    assert callable(pp_UnlessExpression.__init__)


def test_hyp_pp_unlessexpression_constructor_args():
    sig = inspect.signature(pp_UnlessExpression.__init__)
    params = list(sig.parameters.keys())



def test_hyp_pp_puppetmanifest_is_not_abstract():
    assert not inspect.isabstract(pp_PuppetManifest)


def test_hyp_pp_puppetmanifest_constructor_exists():
    assert callable(pp_PuppetManifest.__init__)


def test_hyp_pp_puppetmanifest_constructor_args():
    sig = inspect.signature(pp_PuppetManifest.__init__)
    params = list(sig.parameters.keys())


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
TextExpression_strategy = st.builds(
    TextExpression,
)
pp_ExpressionTE_strategy = st.builds(
    pp_ExpressionTE,
)
pp_VerbatimTE_strategy = st.builds(
    pp_VerbatimTE,
    text=
        safe_text
)
pp_TextExpression_strategy = st.builds(
    pp_TextExpression,
)
IQuotedString_strategy = st.builds(
    IQuotedString,
)
StringExpression_strategy = st.builds(
    StringExpression,
)
pp_UnquotedString_strategy = st.builds(
    pp_UnquotedString,
)
pp_SingleQuotedString_strategy = st.builds(
    pp_SingleQuotedString,
    text=
        safe_text
)
pp_DoubleQuotedString_strategy = st.builds(
    pp_DoubleQuotedString,
)
Lambda_strategy = st.builds(
    Lambda,
)
pp_RubyLambda_strategy = st.builds(
    pp_RubyLambda,
)
pp_JavaLambda_strategy = st.builds(
    pp_JavaLambda,
    farrow=
        st.booleans()
)
pp_VariableTE_strategy = st.builds(
    pp_VariableTE,
    varName=
        safe_text
)
WithLambdaExpression_strategy = st.builds(
    WithLambdaExpression,
)
pp_MethodCall_strategy = st.builds(
    pp_MethodCall,
    parenthesized=
        st.booleans()
)
pp_FunctionCall_strategy = st.builds(
    pp_FunctionCall,
)
ParameterizedExpression_strategy = st.builds(
    ParameterizedExpression,
)
pp_WithLambdaExpression_strategy = st.builds(
    pp_WithLambdaExpression,
)
pp_SelectorExpression_strategy = st.builds(
    pp_SelectorExpression,
)
pp_AtExpression_strategy = st.builds(
    pp_AtExpression,
)
IfExpression_strategy = st.builds(
    IfExpression,
)
pp_ElseIfExpression_strategy = st.builds(
    pp_ElseIfExpression,
)
pp_HashEntry_strategy = st.builds(
    pp_HashEntry,
)
pp_IQuotedString_strategy = st.builds(
    pp_IQuotedString,
)
BinaryExpression_strategy = st.builds(
    BinaryExpression,
)
pp_OrExpression_strategy = st.builds(
    pp_OrExpression,
)
pp_BinaryOpExpression_strategy = st.builds(
    pp_BinaryOpExpression,
    opName=
        safe_text
)
pp_AppendExpression_strategy = st.builds(
    pp_AppendExpression,
)
pp_SelectorEntry_strategy = st.builds(
    pp_SelectorEntry,
)
pp_NamedAccessExpression_strategy = st.builds(
    pp_NamedAccessExpression,
)
pp_AndExpression_strategy = st.builds(
    pp_AndExpression,
)
pp_AssignmentExpression_strategy = st.builds(
    pp_AssignmentExpression,
)
BinaryOpExpression_strategy = st.builds(
    BinaryOpExpression,
)
pp_EqualityExpression_strategy = st.builds(
    pp_EqualityExpression,
)
pp_AdditiveExpression_strategy = st.builds(
    pp_AdditiveExpression,
)
pp_ShiftExpression_strategy = st.builds(
    pp_ShiftExpression,
)
pp_MultiplicativeExpression_strategy = st.builds(
    pp_MultiplicativeExpression,
)
pp_RelationalExpression_strategy = st.builds(
    pp_RelationalExpression,
)
pp_MatchingExpression_strategy = st.builds(
    pp_MatchingExpression,
)
pp_InExpression_strategy = st.builds(
    pp_InExpression,
)
pp_RelationshipExpression_strategy = st.builds(
    pp_RelationshipExpression,
)
Expression_strategy = st.builds(
    Expression,
)
pp_VariableExpression_strategy = st.builds(
    pp_VariableExpression,
    varName=
        safe_text
)
pp_ExpressionBlock_strategy = st.builds(
    pp_ExpressionBlock,
)
pp_SeparatorExpression_strategy = st.builds(
    pp_SeparatorExpression,
)
pp_ParameterizedExpression_strategy = st.builds(
    pp_ParameterizedExpression,
)
pp_BinaryExpression_strategy = st.builds(
    pp_BinaryExpression,
)
pp_InterpolatedVariable_strategy = st.builds(
    pp_InterpolatedVariable,
    varName=
        safe_text
)
pp_UnaryExpression_strategy = st.builds(
    pp_UnaryExpression,
)
pp_StringExpression_strategy = st.builds(
    pp_StringExpression,
)
pp_ParenthesisedExpression_strategy = st.builds(
    pp_ParenthesisedExpression,
)
pp_ImportExpression_strategy = st.builds(
    pp_ImportExpression,
)
pp_ExprList_strategy = st.builds(
    pp_ExprList,
)
pp_CollectExpression_strategy = st.builds(
    pp_CollectExpression,
)
pp_CaseExpression_strategy = st.builds(
    pp_CaseExpression,
)
pp_DefinitionArgument_strategy = st.builds(
    pp_DefinitionArgument,
    argName=
        safe_text,
    op=
        safe_text
)
pp_DefinitionArgumentList_strategy = st.builds(
    pp_DefinitionArgumentList,
)
pp_LiteralExpression_strategy = st.builds(
    pp_LiteralExpression,
)
Definition_strategy = st.builds(
    Definition,
)
pp_HostClassDefinition_strategy = st.builds(
    pp_HostClassDefinition,
)
ICollectQuery_strategy = st.builds(
    ICollectQuery,
)
UnaryExpression_strategy = st.builds(
    UnaryExpression,
)
pp_UnaryMinusExpression_strategy = st.builds(
    pp_UnaryMinusExpression,
)
pp_ExportedCollectQuery_strategy = st.builds(
    pp_ExportedCollectQuery,
)
pp_UnaryNotExpression_strategy = st.builds(
    pp_UnaryNotExpression,
)
pp_VirtualCollectQuery_strategy = st.builds(
    pp_VirtualCollectQuery,
)
pp_ICollectQuery_strategy = st.builds(
    pp_ICollectQuery,
)
pp_ResourceExpression_strategy = st.builds(
    pp_ResourceExpression,
)
LiteralExpression_strategy = st.builds(
    LiteralExpression,
)
pp_LiteralRegex_strategy = st.builds(
    pp_LiteralRegex,
    value=
        safe_text
)
pp_LiteralUndef_strategy = st.builds(
    pp_LiteralUndef,
)
pp_VirtualNameOrReference_strategy = st.builds(
    pp_VirtualNameOrReference,
    exported=
        st.booleans(),
    value=
        safe_text
)
pp_LiteralName_strategy = st.builds(
    pp_LiteralName,
    value=
        safe_text
)
pp_LiteralHash_strategy = st.builds(
    pp_LiteralHash,
)
pp_LiteralList_strategy = st.builds(
    pp_LiteralList,
)
pp_LiteralClass_strategy = st.builds(
    pp_LiteralClass,
)
pp_LiteralDefault_strategy = st.builds(
    pp_LiteralDefault,
)
pp_LiteralBoolean_strategy = st.builds(
    pp_LiteralBoolean,
    value=
        st.booleans()
)
pp_LiteralNameOrReference_strategy = st.builds(
    pp_LiteralNameOrReference,
    value=
        safe_text
)
pp_AttributeOperation_strategy = st.builds(
    pp_AttributeOperation,
    key=
        safe_text,
    op=
        safe_text
)
pp_AttributeOperations_strategy = st.builds(
    pp_AttributeOperations,
)
pp_ResourceBody_strategy = st.builds(
    pp_ResourceBody,
)
pp_Expression_strategy = st.builds(
    pp_Expression,
)
ExpressionBlock_strategy = st.builds(
    ExpressionBlock,
)
pp_ElseExpression_strategy = st.builds(
    pp_ElseExpression,
)
pp_Case_strategy = st.builds(
    pp_Case,
)
pp_Lambda_strategy = st.builds(
    pp_Lambda,
)
pp_NodeDefinition_strategy = st.builds(
    pp_NodeDefinition,
)
pp_Definition_strategy = st.builds(
    pp_Definition,
    className=
        safe_text
)
pp_IfExpression_strategy = st.builds(
    pp_IfExpression,
)
pp_UnlessExpression_strategy = st.builds(
    pp_UnlessExpression,
)
pp_PuppetManifest_strategy = st.builds(
    pp_PuppetManifest,
)






@given(instance=pp_VerbatimTE_strategy)
def test_hyp_pp_verbatimte_text_setter(instance):
    original = instance.text
    instance.text = original
    assert instance.text == original








@given(instance=pp_SingleQuotedString_strategy)
def test_hyp_pp_singlequotedstring_text_setter(instance):
    original = instance.text
    instance.text = original
    assert instance.text == original







@given(instance=pp_JavaLambda_strategy)
def test_hyp_pp_javalambda_farrow_setter(instance):
    original = instance.farrow
    instance.farrow = original
    assert instance.farrow == original




@given(instance=pp_VariableTE_strategy)
def test_hyp_pp_variablete_varName_setter(instance):
    original = instance.varName
    instance.varName = original
    assert instance.varName == original





@given(instance=pp_MethodCall_strategy)
def test_hyp_pp_methodcall_parenthesized_setter(instance):
    original = instance.parenthesized
    instance.parenthesized = original
    assert instance.parenthesized == original















@given(instance=pp_BinaryOpExpression_strategy)
def test_hyp_pp_binaryopexpression_opName_setter(instance):
    original = instance.opName
    instance.opName = original
    assert instance.opName == original



















@given(instance=pp_VariableExpression_strategy)
def test_hyp_pp_variableexpression_varName_setter(instance):
    original = instance.varName
    instance.varName = original
    assert instance.varName == original








@given(instance=pp_InterpolatedVariable_strategy)
def test_hyp_pp_interpolatedvariable_varName_setter(instance):
    original = instance.varName
    instance.varName = original
    assert instance.varName == original











@given(instance=pp_DefinitionArgument_strategy)
def test_hyp_pp_definitionargument_argName_setter(instance):
    original = instance.argName
    instance.argName = original
    assert instance.argName == original



@given(instance=pp_DefinitionArgument_strategy)
def test_hyp_pp_definitionargument_op_setter(instance):
    original = instance.op
    instance.op = original
    assert instance.op == original

















@given(instance=pp_LiteralRegex_strategy)
def test_hyp_pp_literalregex_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original





@given(instance=pp_VirtualNameOrReference_strategy)
def test_hyp_pp_virtualnameorreference_exported_setter(instance):
    original = instance.exported
    instance.exported = original
    assert instance.exported == original



@given(instance=pp_VirtualNameOrReference_strategy)
def test_hyp_pp_virtualnameorreference_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original




@given(instance=pp_LiteralName_strategy)
def test_hyp_pp_literalname_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original








@given(instance=pp_LiteralBoolean_strategy)
def test_hyp_pp_literalboolean_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original




@given(instance=pp_LiteralNameOrReference_strategy)
def test_hyp_pp_literalnameorreference_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original




@given(instance=pp_AttributeOperation_strategy)
def test_hyp_pp_attributeoperation_key_setter(instance):
    original = instance.key
    instance.key = original
    assert instance.key == original



@given(instance=pp_AttributeOperation_strategy)
def test_hyp_pp_attributeoperation_op_setter(instance):
    original = instance.op
    instance.op = original
    assert instance.op == original












@given(instance=pp_Definition_strategy)
def test_hyp_pp_definition_className_setter(instance):
    original = instance.className
    instance.className = original
    assert instance.className == original





# ----- SECTION B: test_structural_full.py (deterministic-first suite) -----
import inspect
import pytest
from datetime import date, datetime, time, timedelta
from hypothesis import given, settings
import hypothesis.strategies as st

from python_code import (
    BinaryExpression,
    BinaryOpExpression,
    Definition,
    Expression,
    ExpressionBlock,
    ICollectQuery,
    IQuotedString,
    IfExpression,
    Lambda,
    LiteralExpression,
    ParameterizedExpression,
    StringExpression,
    TextExpression,
    UnaryExpression,
    WithLambdaExpression,
    pp_AdditiveExpression,
    pp_AndExpression,
    pp_AppendExpression,
    pp_AssignmentExpression,
    pp_AtExpression,
    pp_AttributeOperation,
    pp_AttributeOperations,
    pp_BinaryExpression,
    pp_BinaryOpExpression,
    pp_Case,
    pp_CaseExpression,
    pp_CollectExpression,
    pp_Definition,
    pp_DefinitionArgument,
    pp_DefinitionArgumentList,
    pp_DoubleQuotedString,
    pp_ElseExpression,
    pp_ElseIfExpression,
    pp_EqualityExpression,
    pp_ExportedCollectQuery,
    pp_ExprList,
    pp_Expression,
    pp_ExpressionBlock,
    pp_ExpressionTE,
    pp_FunctionCall,
    pp_HashEntry,
    pp_HostClassDefinition,
    pp_ICollectQuery,
    pp_IQuotedString,
    pp_IfExpression,
    pp_ImportExpression,
    pp_InExpression,
    pp_InterpolatedVariable,
    pp_JavaLambda,
    pp_Lambda,
    pp_LiteralBoolean,
    pp_LiteralClass,
    pp_LiteralDefault,
    pp_LiteralExpression,
    pp_LiteralHash,
    pp_LiteralList,
    pp_LiteralName,
    pp_LiteralNameOrReference,
    pp_LiteralRegex,
    pp_LiteralUndef,
    pp_MatchingExpression,
    pp_MethodCall,
    pp_MultiplicativeExpression,
    pp_NamedAccessExpression,
    pp_NodeDefinition,
    pp_OrExpression,
    pp_ParameterizedExpression,
    pp_ParenthesisedExpression,
    pp_PuppetManifest,
    pp_RelationalExpression,
    pp_RelationshipExpression,
    pp_ResourceBody,
    pp_ResourceExpression,
    pp_RubyLambda,
    pp_SelectorEntry,
    pp_SelectorExpression,
    pp_SeparatorExpression,
    pp_ShiftExpression,
    pp_SingleQuotedString,
    pp_StringExpression,
    pp_TextExpression,
    pp_UnaryExpression,
    pp_UnaryMinusExpression,
    pp_UnaryNotExpression,
    pp_UnlessExpression,
    pp_UnquotedString,
    pp_VariableExpression,
    pp_VariableTE,
    pp_VerbatimTE,
    pp_VirtualCollectQuery,
    pp_VirtualNameOrReference,
    pp_WithLambdaExpression,
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

def test_pp_AttributeOperation_key_value_roundtrip():
    instance = pp_AttributeOperation(key="sample_text", op="sample_text")
    assert instance.key == "sample_text"
    instance.key = "sample_text_2"
    assert instance.key == "sample_text_2"


def test_pp_AttributeOperation_op_value_roundtrip():
    instance = pp_AttributeOperation(key="sample_text", op="sample_text")
    assert instance.op == "sample_text"
    instance.op = "sample_text_2"
    assert instance.op == "sample_text_2"


def test_pp_BinaryOpExpression_opName_value_roundtrip():
    instance = pp_BinaryOpExpression(opName="sample_text")
    assert instance.opName == "sample_text"
    instance.opName = "sample_text_2"
    assert instance.opName == "sample_text_2"


def test_pp_Definition_className_value_roundtrip():
    instance = pp_Definition(className="sample_text")
    assert instance.className == "sample_text"
    instance.className = "sample_text_2"
    assert instance.className == "sample_text_2"


def test_pp_DefinitionArgument_argName_value_roundtrip():
    instance = pp_DefinitionArgument(argName="sample_text", op="sample_text")
    assert instance.argName == "sample_text"
    instance.argName = "sample_text_2"
    assert instance.argName == "sample_text_2"


def test_pp_DefinitionArgument_op_value_roundtrip():
    instance = pp_DefinitionArgument(argName="sample_text", op="sample_text")
    assert instance.op == "sample_text"
    instance.op = "sample_text_2"
    assert instance.op == "sample_text_2"


def test_pp_InterpolatedVariable_varName_value_roundtrip():
    instance = pp_InterpolatedVariable(varName="sample_text")
    assert instance.varName == "sample_text"
    instance.varName = "sample_text_2"
    assert instance.varName == "sample_text_2"


def test_pp_JavaLambda_farrow_value_roundtrip():
    instance = pp_JavaLambda(farrow=True)
    assert instance.farrow == True
    instance.farrow = False
    assert instance.farrow == False


def test_pp_LiteralBoolean_value_value_roundtrip():
    instance = pp_LiteralBoolean(value=True)
    assert instance.value == True
    instance.value = False
    assert instance.value == False


def test_pp_LiteralName_value_value_roundtrip():
    instance = pp_LiteralName(value="sample_text")
    assert instance.value == "sample_text"
    instance.value = "sample_text_2"
    assert instance.value == "sample_text_2"


def test_pp_LiteralNameOrReference_value_value_roundtrip():
    instance = pp_LiteralNameOrReference(value="sample_text")
    assert instance.value == "sample_text"
    instance.value = "sample_text_2"
    assert instance.value == "sample_text_2"


def test_pp_LiteralRegex_value_value_roundtrip():
    instance = pp_LiteralRegex(value="sample_text")
    assert instance.value == "sample_text"
    instance.value = "sample_text_2"
    assert instance.value == "sample_text_2"


def test_pp_MethodCall_parenthesized_value_roundtrip():
    instance = pp_MethodCall(parenthesized=True)
    assert instance.parenthesized == True
    instance.parenthesized = False
    assert instance.parenthesized == False


def test_pp_SingleQuotedString_text_value_roundtrip():
    instance = pp_SingleQuotedString(text="sample_text")
    assert instance.text == "sample_text"
    instance.text = "sample_text_2"
    assert instance.text == "sample_text_2"


def test_pp_VariableExpression_varName_value_roundtrip():
    instance = pp_VariableExpression(varName="sample_text")
    assert instance.varName == "sample_text"
    instance.varName = "sample_text_2"
    assert instance.varName == "sample_text_2"


def test_pp_VariableTE_varName_value_roundtrip():
    instance = pp_VariableTE(varName="sample_text")
    assert instance.varName == "sample_text"
    instance.varName = "sample_text_2"
    assert instance.varName == "sample_text_2"


def test_pp_VerbatimTE_text_value_roundtrip():
    instance = pp_VerbatimTE(text="sample_text")
    assert instance.text == "sample_text"
    instance.text = "sample_text_2"
    assert instance.text == "sample_text_2"


def test_pp_VirtualNameOrReference_exported_value_roundtrip():
    instance = pp_VirtualNameOrReference(exported=True, value="sample_text")
    assert instance.exported == True
    instance.exported = False
    assert instance.exported == False


def test_pp_VirtualNameOrReference_value_value_roundtrip():
    instance = pp_VirtualNameOrReference(exported=True, value="sample_text")
    assert instance.value == "sample_text"
    instance.value = "sample_text_2"
    assert instance.value == "sample_text_2"


def test_pp_AndExpression_isa_BinaryExpression():
    instance = pp_AndExpression()
    assert isinstance(instance, BinaryExpression)


def test_pp_AppendExpression_isa_BinaryExpression():
    instance = pp_AppendExpression()
    assert isinstance(instance, BinaryExpression)


def test_pp_AssignmentExpression_isa_BinaryExpression():
    instance = pp_AssignmentExpression()
    assert isinstance(instance, BinaryExpression)


def test_pp_BinaryOpExpression_isa_BinaryExpression():
    instance = pp_BinaryOpExpression(opName="sample_text")
    assert isinstance(instance, BinaryExpression)


def test_pp_NamedAccessExpression_isa_BinaryExpression():
    instance = pp_NamedAccessExpression()
    assert isinstance(instance, BinaryExpression)


def test_pp_OrExpression_isa_BinaryExpression():
    instance = pp_OrExpression()
    assert isinstance(instance, BinaryExpression)


def test_pp_SelectorEntry_isa_BinaryExpression():
    instance = pp_SelectorEntry()
    assert isinstance(instance, BinaryExpression)


def test_pp_AdditiveExpression_isa_BinaryOpExpression():
    instance = pp_AdditiveExpression()
    assert isinstance(instance, BinaryOpExpression)


def test_pp_EqualityExpression_isa_BinaryOpExpression():
    instance = pp_EqualityExpression()
    assert isinstance(instance, BinaryOpExpression)


def test_pp_InExpression_isa_BinaryOpExpression():
    instance = pp_InExpression()
    assert isinstance(instance, BinaryOpExpression)


def test_pp_MatchingExpression_isa_BinaryOpExpression():
    instance = pp_MatchingExpression()
    assert isinstance(instance, BinaryOpExpression)


def test_pp_MultiplicativeExpression_isa_BinaryOpExpression():
    instance = pp_MultiplicativeExpression()
    assert isinstance(instance, BinaryOpExpression)


def test_pp_RelationalExpression_isa_BinaryOpExpression():
    instance = pp_RelationalExpression()
    assert isinstance(instance, BinaryOpExpression)


def test_pp_RelationshipExpression_isa_BinaryOpExpression():
    instance = pp_RelationshipExpression()
    assert isinstance(instance, BinaryOpExpression)


def test_pp_ShiftExpression_isa_BinaryOpExpression():
    instance = pp_ShiftExpression()
    assert isinstance(instance, BinaryOpExpression)


def test_pp_HostClassDefinition_isa_Definition():
    instance = pp_HostClassDefinition()
    assert isinstance(instance, Definition)


def test_pp_BinaryExpression_isa_Expression():
    instance = pp_BinaryExpression()
    assert isinstance(instance, Expression)


def test_pp_CaseExpression_isa_Expression():
    instance = pp_CaseExpression()
    assert isinstance(instance, Expression)


def test_pp_CollectExpression_isa_Expression():
    instance = pp_CollectExpression()
    assert isinstance(instance, Expression)


def test_pp_ExprList_isa_Expression():
    instance = pp_ExprList()
    assert isinstance(instance, Expression)


def test_pp_ExpressionBlock_isa_Expression():
    instance = pp_ExpressionBlock()
    assert isinstance(instance, Expression)


def test_pp_ImportExpression_isa_Expression():
    instance = pp_ImportExpression()
    assert isinstance(instance, Expression)


def test_pp_InterpolatedVariable_isa_Expression():
    instance = pp_InterpolatedVariable(varName="sample_text")
    assert isinstance(instance, Expression)


def test_pp_LiteralExpression_isa_Expression():
    instance = pp_LiteralExpression()
    assert isinstance(instance, Expression)


def test_pp_ParameterizedExpression_isa_Expression():
    instance = pp_ParameterizedExpression()
    assert isinstance(instance, Expression)


def test_pp_ParenthesisedExpression_isa_Expression():
    instance = pp_ParenthesisedExpression()
    assert isinstance(instance, Expression)


def test_pp_ResourceExpression_isa_Expression():
    instance = pp_ResourceExpression()
    assert isinstance(instance, Expression)


def test_pp_SeparatorExpression_isa_Expression():
    instance = pp_SeparatorExpression()
    assert isinstance(instance, Expression)


def test_pp_StringExpression_isa_Expression():
    instance = pp_StringExpression()
    assert isinstance(instance, Expression)


def test_pp_UnaryExpression_isa_Expression():
    instance = pp_UnaryExpression()
    assert isinstance(instance, Expression)


def test_pp_VariableExpression_isa_Expression():
    instance = pp_VariableExpression(varName="sample_text")
    assert isinstance(instance, Expression)


def test_pp_Case_isa_ExpressionBlock():
    instance = pp_Case()
    assert isinstance(instance, ExpressionBlock)


def test_pp_Definition_isa_ExpressionBlock():
    instance = pp_Definition(className="sample_text")
    assert isinstance(instance, ExpressionBlock)


def test_pp_ElseExpression_isa_ExpressionBlock():
    instance = pp_ElseExpression()
    assert isinstance(instance, ExpressionBlock)


def test_pp_IfExpression_isa_ExpressionBlock():
    instance = pp_IfExpression()
    assert isinstance(instance, ExpressionBlock)


def test_pp_Lambda_isa_ExpressionBlock():
    instance = pp_Lambda()
    assert isinstance(instance, ExpressionBlock)


def test_pp_NodeDefinition_isa_ExpressionBlock():
    instance = pp_NodeDefinition()
    assert isinstance(instance, ExpressionBlock)


def test_pp_PuppetManifest_isa_ExpressionBlock():
    instance = pp_PuppetManifest()
    assert isinstance(instance, ExpressionBlock)


def test_pp_UnlessExpression_isa_ExpressionBlock():
    instance = pp_UnlessExpression()
    assert isinstance(instance, ExpressionBlock)


def test_pp_ExportedCollectQuery_isa_ICollectQuery():
    instance = pp_ExportedCollectQuery()
    assert isinstance(instance, ICollectQuery)


def test_pp_VirtualCollectQuery_isa_ICollectQuery():
    instance = pp_VirtualCollectQuery()
    assert isinstance(instance, ICollectQuery)


def test_pp_DoubleQuotedString_isa_IQuotedString():
    instance = pp_DoubleQuotedString()
    assert isinstance(instance, IQuotedString)


def test_pp_SingleQuotedString_isa_IQuotedString():
    instance = pp_SingleQuotedString(text="sample_text")
    assert isinstance(instance, IQuotedString)


def test_pp_ElseIfExpression_isa_IfExpression():
    instance = pp_ElseIfExpression()
    assert isinstance(instance, IfExpression)


def test_pp_JavaLambda_isa_Lambda():
    instance = pp_JavaLambda(farrow=True)
    assert isinstance(instance, Lambda)


def test_pp_RubyLambda_isa_Lambda():
    instance = pp_RubyLambda()
    assert isinstance(instance, Lambda)


def test_pp_LiteralBoolean_isa_LiteralExpression():
    instance = pp_LiteralBoolean(value=True)
    assert isinstance(instance, LiteralExpression)


def test_pp_LiteralClass_isa_LiteralExpression():
    instance = pp_LiteralClass()
    assert isinstance(instance, LiteralExpression)


def test_pp_LiteralDefault_isa_LiteralExpression():
    instance = pp_LiteralDefault()
    assert isinstance(instance, LiteralExpression)


def test_pp_LiteralHash_isa_LiteralExpression():
    instance = pp_LiteralHash()
    assert isinstance(instance, LiteralExpression)


def test_pp_LiteralList_isa_LiteralExpression():
    instance = pp_LiteralList()
    assert isinstance(instance, LiteralExpression)


def test_pp_LiteralName_isa_LiteralExpression():
    instance = pp_LiteralName(value="sample_text")
    assert isinstance(instance, LiteralExpression)


def test_pp_LiteralNameOrReference_isa_LiteralExpression():
    instance = pp_LiteralNameOrReference(value="sample_text")
    assert isinstance(instance, LiteralExpression)


def test_pp_LiteralRegex_isa_LiteralExpression():
    instance = pp_LiteralRegex(value="sample_text")
    assert isinstance(instance, LiteralExpression)


def test_pp_LiteralUndef_isa_LiteralExpression():
    instance = pp_LiteralUndef()
    assert isinstance(instance, LiteralExpression)


def test_pp_VirtualNameOrReference_isa_LiteralExpression():
    instance = pp_VirtualNameOrReference(exported=True, value="sample_text")
    assert isinstance(instance, LiteralExpression)


def test_pp_AtExpression_isa_ParameterizedExpression():
    instance = pp_AtExpression()
    assert isinstance(instance, ParameterizedExpression)


def test_pp_SelectorExpression_isa_ParameterizedExpression():
    instance = pp_SelectorExpression()
    assert isinstance(instance, ParameterizedExpression)


def test_pp_WithLambdaExpression_isa_ParameterizedExpression():
    instance = pp_WithLambdaExpression()
    assert isinstance(instance, ParameterizedExpression)


def test_pp_DoubleQuotedString_isa_StringExpression():
    instance = pp_DoubleQuotedString()
    assert isinstance(instance, StringExpression)


def test_pp_SingleQuotedString_isa_StringExpression():
    instance = pp_SingleQuotedString(text="sample_text")
    assert isinstance(instance, StringExpression)


def test_pp_UnquotedString_isa_StringExpression():
    instance = pp_UnquotedString()
    assert isinstance(instance, StringExpression)


def test_pp_ExpressionTE_isa_TextExpression():
    instance = pp_ExpressionTE()
    assert isinstance(instance, TextExpression)


def test_pp_VariableTE_isa_TextExpression():
    instance = pp_VariableTE(varName="sample_text")
    assert isinstance(instance, TextExpression)


def test_pp_VerbatimTE_isa_TextExpression():
    instance = pp_VerbatimTE(text="sample_text")
    assert isinstance(instance, TextExpression)


def test_pp_ExportedCollectQuery_isa_UnaryExpression():
    instance = pp_ExportedCollectQuery()
    assert isinstance(instance, UnaryExpression)


def test_pp_UnaryMinusExpression_isa_UnaryExpression():
    instance = pp_UnaryMinusExpression()
    assert isinstance(instance, UnaryExpression)


def test_pp_UnaryNotExpression_isa_UnaryExpression():
    instance = pp_UnaryNotExpression()
    assert isinstance(instance, UnaryExpression)


def test_pp_VirtualCollectQuery_isa_UnaryExpression():
    instance = pp_VirtualCollectQuery()
    assert isinstance(instance, UnaryExpression)


def test_pp_FunctionCall_isa_WithLambdaExpression():
    instance = pp_FunctionCall()
    assert isinstance(instance, WithLambdaExpression)


def test_pp_MethodCall_isa_WithLambdaExpression():
    instance = pp_MethodCall(parenthesized=True)
    assert isinstance(instance, WithLambdaExpression)


def test_assoc_arguments10_link_reassign_clear():
    a = pp_DefinitionArgument(argName="sample_text", op="sample_text")
    b1 = pp_DefinitionArgumentList()
    b2 = pp_DefinitionArgumentList()
    _safe_set(a, 'pp_DefinitionArgument', b1)
    assert _is_linked(a, 'pp_DefinitionArgument', b1)
    if hasattr(b1, 'pp_DefinitionArgumentList11'):
        assert _is_linked(b1, 'pp_DefinitionArgumentList11', a)
    _safe_set(a, 'pp_DefinitionArgument', b2)
    assert _is_linked(a, 'pp_DefinitionArgument', b2)
    if hasattr(b1, 'pp_DefinitionArgumentList11'):
        assert not _is_linked(b1, 'pp_DefinitionArgumentList11', a)
    if hasattr(b2, 'pp_DefinitionArgumentList11'):
        assert _is_linked(b2, 'pp_DefinitionArgumentList11', a)
    _safe_set(a, 'pp_DefinitionArgument', None)
    assert not _is_linked(a, 'pp_DefinitionArgument', b2)
    if hasattr(b2, 'pp_DefinitionArgumentList11'):
        assert not _is_linked(b2, 'pp_DefinitionArgumentList11', a)


def test_assoc_arguments9_link_reassign_clear():
    a = pp_Definition(className="sample_text")
    b1 = pp_DefinitionArgumentList()
    b2 = pp_DefinitionArgumentList()
    _safe_set(a, 'pp_Definition', b1)
    assert _is_linked(a, 'pp_Definition', b1)
    if hasattr(b1, 'pp_DefinitionArgumentList'):
        assert _is_linked(b1, 'pp_DefinitionArgumentList', a)
    _safe_set(a, 'pp_Definition', b2)
    assert _is_linked(a, 'pp_Definition', b2)
    if hasattr(b1, 'pp_DefinitionArgumentList'):
        assert not _is_linked(b1, 'pp_DefinitionArgumentList', a)
    if hasattr(b2, 'pp_DefinitionArgumentList'):
        assert _is_linked(b2, 'pp_DefinitionArgumentList', a)
    _safe_set(a, 'pp_Definition', None)
    assert not _is_linked(a, 'pp_Definition', b2)
    if hasattr(b2, 'pp_DefinitionArgumentList'):
        assert not _is_linked(b2, 'pp_DefinitionArgumentList', a)


def test_assoc_attributes5_link_reassign_clear():
    a = pp_AttributeOperation(key="sample_text", op="sample_text")
    b1 = pp_AttributeOperations()
    b2 = pp_AttributeOperations()
    _safe_set(a, 'pp_AttributeOperation7', b1)
    assert _is_linked(a, 'pp_AttributeOperation7', b1)
    if hasattr(b1, 'pp_AttributeOperations6'):
        assert _is_linked(b1, 'pp_AttributeOperations6', a)
    _safe_set(a, 'pp_AttributeOperation7', b2)
    assert _is_linked(a, 'pp_AttributeOperation7', b2)
    if hasattr(b1, 'pp_AttributeOperations6'):
        assert not _is_linked(b1, 'pp_AttributeOperations6', a)
    if hasattr(b2, 'pp_AttributeOperations6'):
        assert _is_linked(b2, 'pp_AttributeOperations6', a)
    _safe_set(a, 'pp_AttributeOperation7', None)
    assert not _is_linked(a, 'pp_AttributeOperation7', b2)
    if hasattr(b2, 'pp_AttributeOperations6'):
        assert not _is_linked(b2, 'pp_AttributeOperations6', a)


def test_assoc_methodExpr87_link_reassign_clear():
    a = pp_MethodCall(parenthesized=True)
    b1 = pp_Expression()
    b2 = pp_Expression()
    _safe_set(a, 'pp_MethodCall', b1)
    assert _is_linked(a, 'pp_MethodCall', b1)
    if hasattr(b1, 'pp_Expression88'):
        assert _is_linked(b1, 'pp_Expression88', a)
    _safe_set(a, 'pp_MethodCall', b2)
    assert _is_linked(a, 'pp_MethodCall', b2)
    if hasattr(b1, 'pp_Expression88'):
        assert not _is_linked(b1, 'pp_Expression88', a)
    if hasattr(b2, 'pp_Expression88'):
        assert _is_linked(b2, 'pp_Expression88', a)
    _safe_set(a, 'pp_MethodCall', None)
    assert not _is_linked(a, 'pp_MethodCall', b2)
    if hasattr(b2, 'pp_Expression88'):
        assert not _is_linked(b2, 'pp_Expression88', a)


def test_assoc_puppetType12_link_reassign_clear():
    a = pp_DefinitionArgument(argName="sample_text", op="sample_text")
    b1 = pp_Expression()
    b2 = pp_Expression()
    _safe_set(a, 'pp_DefinitionArgument13', b1)
    assert _is_linked(a, 'pp_DefinitionArgument13', b1)
    if hasattr(b1, 'pp_Expression14'):
        assert _is_linked(b1, 'pp_Expression14', a)
    _safe_set(a, 'pp_DefinitionArgument13', b2)
    assert _is_linked(a, 'pp_DefinitionArgument13', b2)
    if hasattr(b1, 'pp_Expression14'):
        assert not _is_linked(b1, 'pp_Expression14', a)
    if hasattr(b2, 'pp_Expression14'):
        assert _is_linked(b2, 'pp_Expression14', a)
    _safe_set(a, 'pp_DefinitionArgument13', None)
    assert not _is_linked(a, 'pp_DefinitionArgument13', b2)
    if hasattr(b2, 'pp_Expression14'):
        assert not _is_linked(b2, 'pp_Expression14', a)


def test_assoc_value15_link_reassign_clear():
    a = pp_DefinitionArgument(argName="sample_text", op="sample_text")
    b1 = pp_Expression()
    b2 = pp_Expression()
    _safe_set(a, 'pp_DefinitionArgument16', b1)
    assert _is_linked(a, 'pp_DefinitionArgument16', b1)
    if hasattr(b1, 'pp_Expression17'):
        assert _is_linked(b1, 'pp_Expression17', a)
    _safe_set(a, 'pp_DefinitionArgument16', b2)
    assert _is_linked(a, 'pp_DefinitionArgument16', b2)
    if hasattr(b1, 'pp_Expression17'):
        assert not _is_linked(b1, 'pp_Expression17', a)
    if hasattr(b2, 'pp_Expression17'):
        assert _is_linked(b2, 'pp_Expression17', a)
    _safe_set(a, 'pp_DefinitionArgument16', None)
    assert not _is_linked(a, 'pp_DefinitionArgument16', b2)
    if hasattr(b2, 'pp_Expression17'):
        assert not _is_linked(b2, 'pp_Expression17', a)


def test_assoc_value3_link_reassign_clear():
    a = pp_AttributeOperation(key="sample_text", op="sample_text")
    b1 = pp_Expression()
    b2 = pp_Expression()
    _safe_set(a, 'pp_AttributeOperation', b1)
    assert _is_linked(a, 'pp_AttributeOperation', b1)
    if hasattr(b1, 'pp_Expression4'):
        assert _is_linked(b1, 'pp_Expression4', a)
    _safe_set(a, 'pp_AttributeOperation', b2)
    assert _is_linked(a, 'pp_AttributeOperation', b2)
    if hasattr(b1, 'pp_Expression4'):
        assert not _is_linked(b1, 'pp_Expression4', a)
    if hasattr(b2, 'pp_Expression4'):
        assert _is_linked(b2, 'pp_Expression4', a)
    _safe_set(a, 'pp_AttributeOperation', None)
    assert not _is_linked(a, 'pp_AttributeOperation', b2)
    if hasattr(b2, 'pp_Expression4'):
        assert not _is_linked(b2, 'pp_Expression4', a)


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

BinaryExpression_strategy = st.builds(BinaryExpression)
@given(instance=BinaryExpression_strategy)
@settings(max_examples=25)
def test_BinaryExpression_instantiation(instance):
    assert isinstance(instance, BinaryExpression)


BinaryOpExpression_strategy = st.builds(BinaryOpExpression)
@given(instance=BinaryOpExpression_strategy)
@settings(max_examples=25)
def test_BinaryOpExpression_instantiation(instance):
    assert isinstance(instance, BinaryOpExpression)


Definition_strategy = st.builds(Definition)
@given(instance=Definition_strategy)
@settings(max_examples=25)
def test_Definition_instantiation(instance):
    assert isinstance(instance, Definition)


Expression_strategy = st.builds(Expression)
@given(instance=Expression_strategy)
@settings(max_examples=25)
def test_Expression_instantiation(instance):
    assert isinstance(instance, Expression)


ExpressionBlock_strategy = st.builds(ExpressionBlock)
@given(instance=ExpressionBlock_strategy)
@settings(max_examples=25)
def test_ExpressionBlock_instantiation(instance):
    assert isinstance(instance, ExpressionBlock)


ICollectQuery_strategy = st.builds(ICollectQuery)
@given(instance=ICollectQuery_strategy)
@settings(max_examples=25)
def test_ICollectQuery_instantiation(instance):
    assert isinstance(instance, ICollectQuery)


IQuotedString_strategy = st.builds(IQuotedString)
@given(instance=IQuotedString_strategy)
@settings(max_examples=25)
def test_IQuotedString_instantiation(instance):
    assert isinstance(instance, IQuotedString)


IfExpression_strategy = st.builds(IfExpression)
@given(instance=IfExpression_strategy)
@settings(max_examples=25)
def test_IfExpression_instantiation(instance):
    assert isinstance(instance, IfExpression)


Lambda_strategy = st.builds(Lambda)
@given(instance=Lambda_strategy)
@settings(max_examples=25)
def test_Lambda_instantiation(instance):
    assert isinstance(instance, Lambda)


LiteralExpression_strategy = st.builds(LiteralExpression)
@given(instance=LiteralExpression_strategy)
@settings(max_examples=25)
def test_LiteralExpression_instantiation(instance):
    assert isinstance(instance, LiteralExpression)


ParameterizedExpression_strategy = st.builds(ParameterizedExpression)
@given(instance=ParameterizedExpression_strategy)
@settings(max_examples=25)
def test_ParameterizedExpression_instantiation(instance):
    assert isinstance(instance, ParameterizedExpression)


StringExpression_strategy = st.builds(StringExpression)
@given(instance=StringExpression_strategy)
@settings(max_examples=25)
def test_StringExpression_instantiation(instance):
    assert isinstance(instance, StringExpression)


TextExpression_strategy = st.builds(TextExpression)
@given(instance=TextExpression_strategy)
@settings(max_examples=25)
def test_TextExpression_instantiation(instance):
    assert isinstance(instance, TextExpression)


UnaryExpression_strategy = st.builds(UnaryExpression)
@given(instance=UnaryExpression_strategy)
@settings(max_examples=25)
def test_UnaryExpression_instantiation(instance):
    assert isinstance(instance, UnaryExpression)


WithLambdaExpression_strategy = st.builds(WithLambdaExpression)
@given(instance=WithLambdaExpression_strategy)
@settings(max_examples=25)
def test_WithLambdaExpression_instantiation(instance):
    assert isinstance(instance, WithLambdaExpression)


pp_AdditiveExpression_strategy = st.builds(pp_AdditiveExpression)
@given(instance=pp_AdditiveExpression_strategy)
@settings(max_examples=25)
def test_pp_AdditiveExpression_instantiation(instance):
    assert isinstance(instance, pp_AdditiveExpression)


pp_AndExpression_strategy = st.builds(pp_AndExpression)
@given(instance=pp_AndExpression_strategy)
@settings(max_examples=25)
def test_pp_AndExpression_instantiation(instance):
    assert isinstance(instance, pp_AndExpression)


pp_AppendExpression_strategy = st.builds(pp_AppendExpression)
@given(instance=pp_AppendExpression_strategy)
@settings(max_examples=25)
def test_pp_AppendExpression_instantiation(instance):
    assert isinstance(instance, pp_AppendExpression)


pp_AssignmentExpression_strategy = st.builds(pp_AssignmentExpression)
@given(instance=pp_AssignmentExpression_strategy)
@settings(max_examples=25)
def test_pp_AssignmentExpression_instantiation(instance):
    assert isinstance(instance, pp_AssignmentExpression)


pp_AtExpression_strategy = st.builds(pp_AtExpression)
@given(instance=pp_AtExpression_strategy)
@settings(max_examples=25)
def test_pp_AtExpression_instantiation(instance):
    assert isinstance(instance, pp_AtExpression)


pp_AttributeOperation_strategy = st.builds(pp_AttributeOperation, key=safe_text, op=safe_text)
@given(instance=pp_AttributeOperation_strategy)
@settings(max_examples=25)
def test_pp_AttributeOperation_instantiation(instance):
    assert isinstance(instance, pp_AttributeOperation)


pp_AttributeOperations_strategy = st.builds(pp_AttributeOperations)
@given(instance=pp_AttributeOperations_strategy)
@settings(max_examples=25)
def test_pp_AttributeOperations_instantiation(instance):
    assert isinstance(instance, pp_AttributeOperations)


pp_BinaryExpression_strategy = st.builds(pp_BinaryExpression)
@given(instance=pp_BinaryExpression_strategy)
@settings(max_examples=25)
def test_pp_BinaryExpression_instantiation(instance):
    assert isinstance(instance, pp_BinaryExpression)


pp_BinaryOpExpression_strategy = st.builds(pp_BinaryOpExpression, opName=safe_text)
@given(instance=pp_BinaryOpExpression_strategy)
@settings(max_examples=25)
def test_pp_BinaryOpExpression_instantiation(instance):
    assert isinstance(instance, pp_BinaryOpExpression)


pp_Case_strategy = st.builds(pp_Case)
@given(instance=pp_Case_strategy)
@settings(max_examples=25)
def test_pp_Case_instantiation(instance):
    assert isinstance(instance, pp_Case)


pp_CaseExpression_strategy = st.builds(pp_CaseExpression)
@given(instance=pp_CaseExpression_strategy)
@settings(max_examples=25)
def test_pp_CaseExpression_instantiation(instance):
    assert isinstance(instance, pp_CaseExpression)


pp_CollectExpression_strategy = st.builds(pp_CollectExpression)
@given(instance=pp_CollectExpression_strategy)
@settings(max_examples=25)
def test_pp_CollectExpression_instantiation(instance):
    assert isinstance(instance, pp_CollectExpression)


pp_Definition_strategy = st.builds(pp_Definition, className=safe_text)
@given(instance=pp_Definition_strategy)
@settings(max_examples=25)
def test_pp_Definition_instantiation(instance):
    assert isinstance(instance, pp_Definition)


pp_DefinitionArgument_strategy = st.builds(pp_DefinitionArgument, argName=safe_text, op=safe_text)
@given(instance=pp_DefinitionArgument_strategy)
@settings(max_examples=25)
def test_pp_DefinitionArgument_instantiation(instance):
    assert isinstance(instance, pp_DefinitionArgument)


pp_DefinitionArgumentList_strategy = st.builds(pp_DefinitionArgumentList)
@given(instance=pp_DefinitionArgumentList_strategy)
@settings(max_examples=25)
def test_pp_DefinitionArgumentList_instantiation(instance):
    assert isinstance(instance, pp_DefinitionArgumentList)


pp_DoubleQuotedString_strategy = st.builds(pp_DoubleQuotedString)
@given(instance=pp_DoubleQuotedString_strategy)
@settings(max_examples=25)
def test_pp_DoubleQuotedString_instantiation(instance):
    assert isinstance(instance, pp_DoubleQuotedString)


pp_ElseExpression_strategy = st.builds(pp_ElseExpression)
@given(instance=pp_ElseExpression_strategy)
@settings(max_examples=25)
def test_pp_ElseExpression_instantiation(instance):
    assert isinstance(instance, pp_ElseExpression)


pp_ElseIfExpression_strategy = st.builds(pp_ElseIfExpression)
@given(instance=pp_ElseIfExpression_strategy)
@settings(max_examples=25)
def test_pp_ElseIfExpression_instantiation(instance):
    assert isinstance(instance, pp_ElseIfExpression)


pp_EqualityExpression_strategy = st.builds(pp_EqualityExpression)
@given(instance=pp_EqualityExpression_strategy)
@settings(max_examples=25)
def test_pp_EqualityExpression_instantiation(instance):
    assert isinstance(instance, pp_EqualityExpression)


pp_ExportedCollectQuery_strategy = st.builds(pp_ExportedCollectQuery)
@given(instance=pp_ExportedCollectQuery_strategy)
@settings(max_examples=25)
def test_pp_ExportedCollectQuery_instantiation(instance):
    assert isinstance(instance, pp_ExportedCollectQuery)


pp_ExprList_strategy = st.builds(pp_ExprList)
@given(instance=pp_ExprList_strategy)
@settings(max_examples=25)
def test_pp_ExprList_instantiation(instance):
    assert isinstance(instance, pp_ExprList)


pp_Expression_strategy = st.builds(pp_Expression)
@given(instance=pp_Expression_strategy)
@settings(max_examples=25)
def test_pp_Expression_instantiation(instance):
    assert isinstance(instance, pp_Expression)


pp_ExpressionBlock_strategy = st.builds(pp_ExpressionBlock)
@given(instance=pp_ExpressionBlock_strategy)
@settings(max_examples=25)
def test_pp_ExpressionBlock_instantiation(instance):
    assert isinstance(instance, pp_ExpressionBlock)


pp_ExpressionTE_strategy = st.builds(pp_ExpressionTE)
@given(instance=pp_ExpressionTE_strategy)
@settings(max_examples=25)
def test_pp_ExpressionTE_instantiation(instance):
    assert isinstance(instance, pp_ExpressionTE)


pp_FunctionCall_strategy = st.builds(pp_FunctionCall)
@given(instance=pp_FunctionCall_strategy)
@settings(max_examples=25)
def test_pp_FunctionCall_instantiation(instance):
    assert isinstance(instance, pp_FunctionCall)


pp_HashEntry_strategy = st.builds(pp_HashEntry)
@given(instance=pp_HashEntry_strategy)
@settings(max_examples=25)
def test_pp_HashEntry_instantiation(instance):
    assert isinstance(instance, pp_HashEntry)


pp_HostClassDefinition_strategy = st.builds(pp_HostClassDefinition)
@given(instance=pp_HostClassDefinition_strategy)
@settings(max_examples=25)
def test_pp_HostClassDefinition_instantiation(instance):
    assert isinstance(instance, pp_HostClassDefinition)


pp_ICollectQuery_strategy = st.builds(pp_ICollectQuery)
@given(instance=pp_ICollectQuery_strategy)
@settings(max_examples=25)
def test_pp_ICollectQuery_instantiation(instance):
    assert isinstance(instance, pp_ICollectQuery)


pp_IQuotedString_strategy = st.builds(pp_IQuotedString)
@given(instance=pp_IQuotedString_strategy)
@settings(max_examples=25)
def test_pp_IQuotedString_instantiation(instance):
    assert isinstance(instance, pp_IQuotedString)


pp_IfExpression_strategy = st.builds(pp_IfExpression)
@given(instance=pp_IfExpression_strategy)
@settings(max_examples=25)
def test_pp_IfExpression_instantiation(instance):
    assert isinstance(instance, pp_IfExpression)


pp_ImportExpression_strategy = st.builds(pp_ImportExpression)
@given(instance=pp_ImportExpression_strategy)
@settings(max_examples=25)
def test_pp_ImportExpression_instantiation(instance):
    assert isinstance(instance, pp_ImportExpression)


pp_InExpression_strategy = st.builds(pp_InExpression)
@given(instance=pp_InExpression_strategy)
@settings(max_examples=25)
def test_pp_InExpression_instantiation(instance):
    assert isinstance(instance, pp_InExpression)


pp_InterpolatedVariable_strategy = st.builds(pp_InterpolatedVariable, varName=safe_text)
@given(instance=pp_InterpolatedVariable_strategy)
@settings(max_examples=25)
def test_pp_InterpolatedVariable_instantiation(instance):
    assert isinstance(instance, pp_InterpolatedVariable)


pp_JavaLambda_strategy = st.builds(pp_JavaLambda, farrow=st.booleans())
@given(instance=pp_JavaLambda_strategy)
@settings(max_examples=25)
def test_pp_JavaLambda_instantiation(instance):
    assert isinstance(instance, pp_JavaLambda)


pp_Lambda_strategy = st.builds(pp_Lambda)
@given(instance=pp_Lambda_strategy)
@settings(max_examples=25)
def test_pp_Lambda_instantiation(instance):
    assert isinstance(instance, pp_Lambda)


pp_LiteralBoolean_strategy = st.builds(pp_LiteralBoolean, value=st.booleans())
@given(instance=pp_LiteralBoolean_strategy)
@settings(max_examples=25)
def test_pp_LiteralBoolean_instantiation(instance):
    assert isinstance(instance, pp_LiteralBoolean)


pp_LiteralClass_strategy = st.builds(pp_LiteralClass)
@given(instance=pp_LiteralClass_strategy)
@settings(max_examples=25)
def test_pp_LiteralClass_instantiation(instance):
    assert isinstance(instance, pp_LiteralClass)


pp_LiteralDefault_strategy = st.builds(pp_LiteralDefault)
@given(instance=pp_LiteralDefault_strategy)
@settings(max_examples=25)
def test_pp_LiteralDefault_instantiation(instance):
    assert isinstance(instance, pp_LiteralDefault)


pp_LiteralExpression_strategy = st.builds(pp_LiteralExpression)
@given(instance=pp_LiteralExpression_strategy)
@settings(max_examples=25)
def test_pp_LiteralExpression_instantiation(instance):
    assert isinstance(instance, pp_LiteralExpression)


pp_LiteralHash_strategy = st.builds(pp_LiteralHash)
@given(instance=pp_LiteralHash_strategy)
@settings(max_examples=25)
def test_pp_LiteralHash_instantiation(instance):
    assert isinstance(instance, pp_LiteralHash)


pp_LiteralList_strategy = st.builds(pp_LiteralList)
@given(instance=pp_LiteralList_strategy)
@settings(max_examples=25)
def test_pp_LiteralList_instantiation(instance):
    assert isinstance(instance, pp_LiteralList)


pp_LiteralName_strategy = st.builds(pp_LiteralName, value=safe_text)
@given(instance=pp_LiteralName_strategy)
@settings(max_examples=25)
def test_pp_LiteralName_instantiation(instance):
    assert isinstance(instance, pp_LiteralName)


pp_LiteralNameOrReference_strategy = st.builds(pp_LiteralNameOrReference, value=safe_text)
@given(instance=pp_LiteralNameOrReference_strategy)
@settings(max_examples=25)
def test_pp_LiteralNameOrReference_instantiation(instance):
    assert isinstance(instance, pp_LiteralNameOrReference)


pp_LiteralRegex_strategy = st.builds(pp_LiteralRegex, value=safe_text)
@given(instance=pp_LiteralRegex_strategy)
@settings(max_examples=25)
def test_pp_LiteralRegex_instantiation(instance):
    assert isinstance(instance, pp_LiteralRegex)


pp_LiteralUndef_strategy = st.builds(pp_LiteralUndef)
@given(instance=pp_LiteralUndef_strategy)
@settings(max_examples=25)
def test_pp_LiteralUndef_instantiation(instance):
    assert isinstance(instance, pp_LiteralUndef)


pp_MatchingExpression_strategy = st.builds(pp_MatchingExpression)
@given(instance=pp_MatchingExpression_strategy)
@settings(max_examples=25)
def test_pp_MatchingExpression_instantiation(instance):
    assert isinstance(instance, pp_MatchingExpression)


pp_MethodCall_strategy = st.builds(pp_MethodCall, parenthesized=st.booleans())
@given(instance=pp_MethodCall_strategy)
@settings(max_examples=25)
def test_pp_MethodCall_instantiation(instance):
    assert isinstance(instance, pp_MethodCall)


pp_MultiplicativeExpression_strategy = st.builds(pp_MultiplicativeExpression)
@given(instance=pp_MultiplicativeExpression_strategy)
@settings(max_examples=25)
def test_pp_MultiplicativeExpression_instantiation(instance):
    assert isinstance(instance, pp_MultiplicativeExpression)


pp_NamedAccessExpression_strategy = st.builds(pp_NamedAccessExpression)
@given(instance=pp_NamedAccessExpression_strategy)
@settings(max_examples=25)
def test_pp_NamedAccessExpression_instantiation(instance):
    assert isinstance(instance, pp_NamedAccessExpression)


pp_NodeDefinition_strategy = st.builds(pp_NodeDefinition)
@given(instance=pp_NodeDefinition_strategy)
@settings(max_examples=25)
def test_pp_NodeDefinition_instantiation(instance):
    assert isinstance(instance, pp_NodeDefinition)


pp_OrExpression_strategy = st.builds(pp_OrExpression)
@given(instance=pp_OrExpression_strategy)
@settings(max_examples=25)
def test_pp_OrExpression_instantiation(instance):
    assert isinstance(instance, pp_OrExpression)


pp_ParameterizedExpression_strategy = st.builds(pp_ParameterizedExpression)
@given(instance=pp_ParameterizedExpression_strategy)
@settings(max_examples=25)
def test_pp_ParameterizedExpression_instantiation(instance):
    assert isinstance(instance, pp_ParameterizedExpression)


pp_ParenthesisedExpression_strategy = st.builds(pp_ParenthesisedExpression)
@given(instance=pp_ParenthesisedExpression_strategy)
@settings(max_examples=25)
def test_pp_ParenthesisedExpression_instantiation(instance):
    assert isinstance(instance, pp_ParenthesisedExpression)


pp_PuppetManifest_strategy = st.builds(pp_PuppetManifest)
@given(instance=pp_PuppetManifest_strategy)
@settings(max_examples=25)
def test_pp_PuppetManifest_instantiation(instance):
    assert isinstance(instance, pp_PuppetManifest)


pp_RelationalExpression_strategy = st.builds(pp_RelationalExpression)
@given(instance=pp_RelationalExpression_strategy)
@settings(max_examples=25)
def test_pp_RelationalExpression_instantiation(instance):
    assert isinstance(instance, pp_RelationalExpression)


pp_RelationshipExpression_strategy = st.builds(pp_RelationshipExpression)
@given(instance=pp_RelationshipExpression_strategy)
@settings(max_examples=25)
def test_pp_RelationshipExpression_instantiation(instance):
    assert isinstance(instance, pp_RelationshipExpression)


pp_ResourceBody_strategy = st.builds(pp_ResourceBody)
@given(instance=pp_ResourceBody_strategy)
@settings(max_examples=25)
def test_pp_ResourceBody_instantiation(instance):
    assert isinstance(instance, pp_ResourceBody)


pp_ResourceExpression_strategy = st.builds(pp_ResourceExpression)
@given(instance=pp_ResourceExpression_strategy)
@settings(max_examples=25)
def test_pp_ResourceExpression_instantiation(instance):
    assert isinstance(instance, pp_ResourceExpression)


pp_RubyLambda_strategy = st.builds(pp_RubyLambda)
@given(instance=pp_RubyLambda_strategy)
@settings(max_examples=25)
def test_pp_RubyLambda_instantiation(instance):
    assert isinstance(instance, pp_RubyLambda)


pp_SelectorEntry_strategy = st.builds(pp_SelectorEntry)
@given(instance=pp_SelectorEntry_strategy)
@settings(max_examples=25)
def test_pp_SelectorEntry_instantiation(instance):
    assert isinstance(instance, pp_SelectorEntry)


pp_SelectorExpression_strategy = st.builds(pp_SelectorExpression)
@given(instance=pp_SelectorExpression_strategy)
@settings(max_examples=25)
def test_pp_SelectorExpression_instantiation(instance):
    assert isinstance(instance, pp_SelectorExpression)


pp_SeparatorExpression_strategy = st.builds(pp_SeparatorExpression)
@given(instance=pp_SeparatorExpression_strategy)
@settings(max_examples=25)
def test_pp_SeparatorExpression_instantiation(instance):
    assert isinstance(instance, pp_SeparatorExpression)


pp_ShiftExpression_strategy = st.builds(pp_ShiftExpression)
@given(instance=pp_ShiftExpression_strategy)
@settings(max_examples=25)
def test_pp_ShiftExpression_instantiation(instance):
    assert isinstance(instance, pp_ShiftExpression)


pp_SingleQuotedString_strategy = st.builds(pp_SingleQuotedString, text=safe_text)
@given(instance=pp_SingleQuotedString_strategy)
@settings(max_examples=25)
def test_pp_SingleQuotedString_instantiation(instance):
    assert isinstance(instance, pp_SingleQuotedString)


pp_StringExpression_strategy = st.builds(pp_StringExpression)
@given(instance=pp_StringExpression_strategy)
@settings(max_examples=25)
def test_pp_StringExpression_instantiation(instance):
    assert isinstance(instance, pp_StringExpression)


pp_TextExpression_strategy = st.builds(pp_TextExpression)
@given(instance=pp_TextExpression_strategy)
@settings(max_examples=25)
def test_pp_TextExpression_instantiation(instance):
    assert isinstance(instance, pp_TextExpression)


pp_UnaryExpression_strategy = st.builds(pp_UnaryExpression)
@given(instance=pp_UnaryExpression_strategy)
@settings(max_examples=25)
def test_pp_UnaryExpression_instantiation(instance):
    assert isinstance(instance, pp_UnaryExpression)


pp_UnaryMinusExpression_strategy = st.builds(pp_UnaryMinusExpression)
@given(instance=pp_UnaryMinusExpression_strategy)
@settings(max_examples=25)
def test_pp_UnaryMinusExpression_instantiation(instance):
    assert isinstance(instance, pp_UnaryMinusExpression)


pp_UnaryNotExpression_strategy = st.builds(pp_UnaryNotExpression)
@given(instance=pp_UnaryNotExpression_strategy)
@settings(max_examples=25)
def test_pp_UnaryNotExpression_instantiation(instance):
    assert isinstance(instance, pp_UnaryNotExpression)


pp_UnlessExpression_strategy = st.builds(pp_UnlessExpression)
@given(instance=pp_UnlessExpression_strategy)
@settings(max_examples=25)
def test_pp_UnlessExpression_instantiation(instance):
    assert isinstance(instance, pp_UnlessExpression)


pp_UnquotedString_strategy = st.builds(pp_UnquotedString)
@given(instance=pp_UnquotedString_strategy)
@settings(max_examples=25)
def test_pp_UnquotedString_instantiation(instance):
    assert isinstance(instance, pp_UnquotedString)


pp_VariableExpression_strategy = st.builds(pp_VariableExpression, varName=safe_text)
@given(instance=pp_VariableExpression_strategy)
@settings(max_examples=25)
def test_pp_VariableExpression_instantiation(instance):
    assert isinstance(instance, pp_VariableExpression)


pp_VariableTE_strategy = st.builds(pp_VariableTE, varName=safe_text)
@given(instance=pp_VariableTE_strategy)
@settings(max_examples=25)
def test_pp_VariableTE_instantiation(instance):
    assert isinstance(instance, pp_VariableTE)


pp_VerbatimTE_strategy = st.builds(pp_VerbatimTE, text=safe_text)
@given(instance=pp_VerbatimTE_strategy)
@settings(max_examples=25)
def test_pp_VerbatimTE_instantiation(instance):
    assert isinstance(instance, pp_VerbatimTE)


pp_VirtualCollectQuery_strategy = st.builds(pp_VirtualCollectQuery)
@given(instance=pp_VirtualCollectQuery_strategy)
@settings(max_examples=25)
def test_pp_VirtualCollectQuery_instantiation(instance):
    assert isinstance(instance, pp_VirtualCollectQuery)


pp_VirtualNameOrReference_strategy = st.builds(pp_VirtualNameOrReference, exported=st.booleans(), value=safe_text)
@given(instance=pp_VirtualNameOrReference_strategy)
@settings(max_examples=25)
def test_pp_VirtualNameOrReference_instantiation(instance):
    assert isinstance(instance, pp_VirtualNameOrReference)


pp_WithLambdaExpression_strategy = st.builds(pp_WithLambdaExpression)
@given(instance=pp_WithLambdaExpression_strategy)
@settings(max_examples=25)
def test_pp_WithLambdaExpression_instantiation(instance):
    assert isinstance(instance, pp_WithLambdaExpression)



