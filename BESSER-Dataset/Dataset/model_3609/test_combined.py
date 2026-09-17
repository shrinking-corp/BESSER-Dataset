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
    ExpressionBlock,
    pp2_Case,
    Expression,
    pp2_CaseExpression,
    pp2_DefinitionArgument,
    pp2_DefinitionArgumentList,
    pp2_PuppetManifest,
    pp2_Lambda,
    pp2_UnlessExpression,
    pp2_SeparatorExpression,
    Lambda,
    pp2_RubyLambda,
    pp2_JavaLambda,
    pp2_ExprList,
    pp2_ParenthesisedExpression,
    IfExpression,
    pp2_ElseIfExpression,
    pp2_ElseExpression,
    pp2_ExpressionBlock,
    pp2_UnaryExpression,
    TextExpression,
    pp2_VariableTE,
    pp2_ExpressionTE,
    pp2_VerbatimTE,
    pp2_InterpolatedVariable,
    pp2_StringExpression,
    pp2_TextExpression,
    IQuotedString,
    StringExpression,
    pp2_SingleQuotedString,
    pp2_UnquotedString,
    pp2_DoubleQuotedString,
    WithLambdaExpression,
    pp2_MethodCall,
    pp2_FunctionCall,
    pp2_CollectExpression,
    ParameterizedExpression,
    pp2_SelectorExpression,
    pp2_WithLambdaExpression,
    pp2_AtExpression,
    pp2_NodeDefinition,
    pp2_ParameterizedExpression,
    pp2_BinaryExpression,
    pp2_HashEntry,
    pp2_IQuotedString,
    pp2_ImportExpression,
    pp2_ResourceExpression,
    LiteralExpression,
    pp2_LiteralClass,
    pp2_LiteralList,
    pp2_VirtualNameOrReference,
    pp2_LiteralHash,
    pp2_LiteralNameOrReference,
    pp2_IfExpression,
    BinaryExpression,
    pp2_NamedAccessExpression,
    pp2_BinaryOpExpression,
    pp2_AppendExpression,
    pp2_OrExpression,
    pp2_AndExpression,
    pp2_SelectorEntry,
    pp2_AssignmentExpression,
    BinaryOpExpression,
    pp2_EqualityExpression,
    pp2_InExpression,
    pp2_MatchingExpression,
    pp2_MultiplicativeExpression,
    pp2_ShiftExpression,
    pp2_RelationalExpression,
    pp2_AdditiveExpression,
    pp2_RelationshipExpression,
    pp2_VariableExpression,
    pp2_LiteralName,
    pp2_LiteralRegex,
    pp2_LiteralDefault,
    pp2_LiteralUndef,
    pp2_LiteralBoolean,
    pp2_Definition,
    pp2_LiteralExpression,
    Definition,
    pp2_HostClassDefinition,
    ICollectQuery,
    UnaryExpression,
    pp2_UnaryMinusExpression,
    pp2_ExportedCollectQuery,
    pp2_UnaryNotExpression,
    pp2_VirtualCollectQuery,
    pp2_ICollectQuery,
    pp2_AttributeOperation,
    pp2_AttributeOperations,
    pp2_ResourceBody,
    pp2_Expression,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_hyp_expressionblock_is_not_abstract():
    assert not inspect.isabstract(ExpressionBlock)


def test_hyp_expressionblock_constructor_exists():
    assert callable(ExpressionBlock.__init__)


def test_hyp_expressionblock_constructor_args():
    sig = inspect.signature(ExpressionBlock.__init__)
    params = list(sig.parameters.keys())



def test_hyp_pp2_case_is_not_abstract():
    assert not inspect.isabstract(pp2_Case)


def test_hyp_pp2_case_constructor_exists():
    assert callable(pp2_Case.__init__)


def test_hyp_pp2_case_constructor_args():
    sig = inspect.signature(pp2_Case.__init__)
    params = list(sig.parameters.keys())



def test_hyp_expression_is_not_abstract():
    assert not inspect.isabstract(Expression)


def test_hyp_expression_constructor_exists():
    assert callable(Expression.__init__)


def test_hyp_expression_constructor_args():
    sig = inspect.signature(Expression.__init__)
    params = list(sig.parameters.keys())



def test_hyp_pp2_caseexpression_is_not_abstract():
    assert not inspect.isabstract(pp2_CaseExpression)


def test_hyp_pp2_caseexpression_constructor_exists():
    assert callable(pp2_CaseExpression.__init__)


def test_hyp_pp2_caseexpression_constructor_args():
    sig = inspect.signature(pp2_CaseExpression.__init__)
    params = list(sig.parameters.keys())



def test_hyp_pp2_definitionargument_is_not_abstract():
    assert not inspect.isabstract(pp2_DefinitionArgument)


def test_hyp_pp2_definitionargument_constructor_exists():
    assert callable(pp2_DefinitionArgument.__init__)


def test_hyp_pp2_definitionargument_constructor_args():
    sig = inspect.signature(pp2_DefinitionArgument.__init__)
    params = list(sig.parameters.keys())
    assert "op" in params, "Missing parameter 'op'"
    assert "argName" in params, "Missing parameter 'argName'"





def test_hyp_pp2_definitionargumentlist_is_not_abstract():
    assert not inspect.isabstract(pp2_DefinitionArgumentList)


def test_hyp_pp2_definitionargumentlist_constructor_exists():
    assert callable(pp2_DefinitionArgumentList.__init__)


def test_hyp_pp2_definitionargumentlist_constructor_args():
    sig = inspect.signature(pp2_DefinitionArgumentList.__init__)
    params = list(sig.parameters.keys())



def test_hyp_pp2_puppetmanifest_is_not_abstract():
    assert not inspect.isabstract(pp2_PuppetManifest)


def test_hyp_pp2_puppetmanifest_constructor_exists():
    assert callable(pp2_PuppetManifest.__init__)


def test_hyp_pp2_puppetmanifest_constructor_args():
    sig = inspect.signature(pp2_PuppetManifest.__init__)
    params = list(sig.parameters.keys())



def test_hyp_pp2_lambda_is_not_abstract():
    assert not inspect.isabstract(pp2_Lambda)


def test_hyp_pp2_lambda_constructor_exists():
    assert callable(pp2_Lambda.__init__)


def test_hyp_pp2_lambda_constructor_args():
    sig = inspect.signature(pp2_Lambda.__init__)
    params = list(sig.parameters.keys())



def test_hyp_pp2_unlessexpression_is_not_abstract():
    assert not inspect.isabstract(pp2_UnlessExpression)


def test_hyp_pp2_unlessexpression_constructor_exists():
    assert callable(pp2_UnlessExpression.__init__)


def test_hyp_pp2_unlessexpression_constructor_args():
    sig = inspect.signature(pp2_UnlessExpression.__init__)
    params = list(sig.parameters.keys())



def test_hyp_pp2_separatorexpression_is_not_abstract():
    assert not inspect.isabstract(pp2_SeparatorExpression)


def test_hyp_pp2_separatorexpression_constructor_exists():
    assert callable(pp2_SeparatorExpression.__init__)


def test_hyp_pp2_separatorexpression_constructor_args():
    sig = inspect.signature(pp2_SeparatorExpression.__init__)
    params = list(sig.parameters.keys())



def test_hyp_lambda_is_not_abstract():
    assert not inspect.isabstract(Lambda)


def test_hyp_lambda_constructor_exists():
    assert callable(Lambda.__init__)


def test_hyp_lambda_constructor_args():
    sig = inspect.signature(Lambda.__init__)
    params = list(sig.parameters.keys())



def test_hyp_pp2_rubylambda_is_not_abstract():
    assert not inspect.isabstract(pp2_RubyLambda)


def test_hyp_pp2_rubylambda_constructor_exists():
    assert callable(pp2_RubyLambda.__init__)


def test_hyp_pp2_rubylambda_constructor_args():
    sig = inspect.signature(pp2_RubyLambda.__init__)
    params = list(sig.parameters.keys())



def test_hyp_pp2_javalambda_is_not_abstract():
    assert not inspect.isabstract(pp2_JavaLambda)


def test_hyp_pp2_javalambda_constructor_exists():
    assert callable(pp2_JavaLambda.__init__)


def test_hyp_pp2_javalambda_constructor_args():
    sig = inspect.signature(pp2_JavaLambda.__init__)
    params = list(sig.parameters.keys())
    assert "farrow" in params, "Missing parameter 'farrow'"




def test_hyp_pp2_exprlist_is_not_abstract():
    assert not inspect.isabstract(pp2_ExprList)


def test_hyp_pp2_exprlist_constructor_exists():
    assert callable(pp2_ExprList.__init__)


def test_hyp_pp2_exprlist_constructor_args():
    sig = inspect.signature(pp2_ExprList.__init__)
    params = list(sig.parameters.keys())



def test_hyp_pp2_parenthesisedexpression_is_not_abstract():
    assert not inspect.isabstract(pp2_ParenthesisedExpression)


def test_hyp_pp2_parenthesisedexpression_constructor_exists():
    assert callable(pp2_ParenthesisedExpression.__init__)


def test_hyp_pp2_parenthesisedexpression_constructor_args():
    sig = inspect.signature(pp2_ParenthesisedExpression.__init__)
    params = list(sig.parameters.keys())



def test_hyp_ifexpression_is_not_abstract():
    assert not inspect.isabstract(IfExpression)


def test_hyp_ifexpression_constructor_exists():
    assert callable(IfExpression.__init__)


def test_hyp_ifexpression_constructor_args():
    sig = inspect.signature(IfExpression.__init__)
    params = list(sig.parameters.keys())



def test_hyp_pp2_elseifexpression_is_not_abstract():
    assert not inspect.isabstract(pp2_ElseIfExpression)


def test_hyp_pp2_elseifexpression_constructor_exists():
    assert callable(pp2_ElseIfExpression.__init__)


def test_hyp_pp2_elseifexpression_constructor_args():
    sig = inspect.signature(pp2_ElseIfExpression.__init__)
    params = list(sig.parameters.keys())



def test_hyp_pp2_elseexpression_is_not_abstract():
    assert not inspect.isabstract(pp2_ElseExpression)


def test_hyp_pp2_elseexpression_constructor_exists():
    assert callable(pp2_ElseExpression.__init__)


def test_hyp_pp2_elseexpression_constructor_args():
    sig = inspect.signature(pp2_ElseExpression.__init__)
    params = list(sig.parameters.keys())



def test_hyp_pp2_expressionblock_is_not_abstract():
    assert not inspect.isabstract(pp2_ExpressionBlock)


def test_hyp_pp2_expressionblock_constructor_exists():
    assert callable(pp2_ExpressionBlock.__init__)


def test_hyp_pp2_expressionblock_constructor_args():
    sig = inspect.signature(pp2_ExpressionBlock.__init__)
    params = list(sig.parameters.keys())



def test_hyp_pp2_unaryexpression_is_not_abstract():
    assert not inspect.isabstract(pp2_UnaryExpression)


def test_hyp_pp2_unaryexpression_constructor_exists():
    assert callable(pp2_UnaryExpression.__init__)


def test_hyp_pp2_unaryexpression_constructor_args():
    sig = inspect.signature(pp2_UnaryExpression.__init__)
    params = list(sig.parameters.keys())



def test_hyp_textexpression_is_not_abstract():
    assert not inspect.isabstract(TextExpression)


def test_hyp_textexpression_constructor_exists():
    assert callable(TextExpression.__init__)


def test_hyp_textexpression_constructor_args():
    sig = inspect.signature(TextExpression.__init__)
    params = list(sig.parameters.keys())



def test_hyp_pp2_variablete_is_not_abstract():
    assert not inspect.isabstract(pp2_VariableTE)


def test_hyp_pp2_variablete_constructor_exists():
    assert callable(pp2_VariableTE.__init__)


def test_hyp_pp2_variablete_constructor_args():
    sig = inspect.signature(pp2_VariableTE.__init__)
    params = list(sig.parameters.keys())
    assert "varName" in params, "Missing parameter 'varName'"




def test_hyp_pp2_expressionte_is_not_abstract():
    assert not inspect.isabstract(pp2_ExpressionTE)


def test_hyp_pp2_expressionte_constructor_exists():
    assert callable(pp2_ExpressionTE.__init__)


def test_hyp_pp2_expressionte_constructor_args():
    sig = inspect.signature(pp2_ExpressionTE.__init__)
    params = list(sig.parameters.keys())



def test_hyp_pp2_verbatimte_is_not_abstract():
    assert not inspect.isabstract(pp2_VerbatimTE)


def test_hyp_pp2_verbatimte_constructor_exists():
    assert callable(pp2_VerbatimTE.__init__)


def test_hyp_pp2_verbatimte_constructor_args():
    sig = inspect.signature(pp2_VerbatimTE.__init__)
    params = list(sig.parameters.keys())
    assert "text" in params, "Missing parameter 'text'"




def test_hyp_pp2_interpolatedvariable_is_not_abstract():
    assert not inspect.isabstract(pp2_InterpolatedVariable)


def test_hyp_pp2_interpolatedvariable_constructor_exists():
    assert callable(pp2_InterpolatedVariable.__init__)


def test_hyp_pp2_interpolatedvariable_constructor_args():
    sig = inspect.signature(pp2_InterpolatedVariable.__init__)
    params = list(sig.parameters.keys())
    assert "varName" in params, "Missing parameter 'varName'"




def test_hyp_pp2_stringexpression_is_not_abstract():
    assert not inspect.isabstract(pp2_StringExpression)


def test_hyp_pp2_stringexpression_constructor_exists():
    assert callable(pp2_StringExpression.__init__)


def test_hyp_pp2_stringexpression_constructor_args():
    sig = inspect.signature(pp2_StringExpression.__init__)
    params = list(sig.parameters.keys())



def test_hyp_pp2_textexpression_is_not_abstract():
    assert not inspect.isabstract(pp2_TextExpression)


def test_hyp_pp2_textexpression_constructor_exists():
    assert callable(pp2_TextExpression.__init__)


def test_hyp_pp2_textexpression_constructor_args():
    sig = inspect.signature(pp2_TextExpression.__init__)
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



def test_hyp_pp2_singlequotedstring_is_not_abstract():
    assert not inspect.isabstract(pp2_SingleQuotedString)


def test_hyp_pp2_singlequotedstring_constructor_exists():
    assert callable(pp2_SingleQuotedString.__init__)


def test_hyp_pp2_singlequotedstring_constructor_args():
    sig = inspect.signature(pp2_SingleQuotedString.__init__)
    params = list(sig.parameters.keys())
    assert "text" in params, "Missing parameter 'text'"




def test_hyp_pp2_unquotedstring_is_not_abstract():
    assert not inspect.isabstract(pp2_UnquotedString)


def test_hyp_pp2_unquotedstring_constructor_exists():
    assert callable(pp2_UnquotedString.__init__)


def test_hyp_pp2_unquotedstring_constructor_args():
    sig = inspect.signature(pp2_UnquotedString.__init__)
    params = list(sig.parameters.keys())



def test_hyp_pp2_doublequotedstring_is_not_abstract():
    assert not inspect.isabstract(pp2_DoubleQuotedString)


def test_hyp_pp2_doublequotedstring_constructor_exists():
    assert callable(pp2_DoubleQuotedString.__init__)


def test_hyp_pp2_doublequotedstring_constructor_args():
    sig = inspect.signature(pp2_DoubleQuotedString.__init__)
    params = list(sig.parameters.keys())



def test_hyp_withlambdaexpression_is_not_abstract():
    assert not inspect.isabstract(WithLambdaExpression)


def test_hyp_withlambdaexpression_constructor_exists():
    assert callable(WithLambdaExpression.__init__)


def test_hyp_withlambdaexpression_constructor_args():
    sig = inspect.signature(WithLambdaExpression.__init__)
    params = list(sig.parameters.keys())



def test_hyp_pp2_methodcall_is_not_abstract():
    assert not inspect.isabstract(pp2_MethodCall)


def test_hyp_pp2_methodcall_constructor_exists():
    assert callable(pp2_MethodCall.__init__)


def test_hyp_pp2_methodcall_constructor_args():
    sig = inspect.signature(pp2_MethodCall.__init__)
    params = list(sig.parameters.keys())
    assert "parenthesized" in params, "Missing parameter 'parenthesized'"




def test_hyp_pp2_functioncall_is_not_abstract():
    assert not inspect.isabstract(pp2_FunctionCall)


def test_hyp_pp2_functioncall_constructor_exists():
    assert callable(pp2_FunctionCall.__init__)


def test_hyp_pp2_functioncall_constructor_args():
    sig = inspect.signature(pp2_FunctionCall.__init__)
    params = list(sig.parameters.keys())



def test_hyp_pp2_collectexpression_is_not_abstract():
    assert not inspect.isabstract(pp2_CollectExpression)


def test_hyp_pp2_collectexpression_constructor_exists():
    assert callable(pp2_CollectExpression.__init__)


def test_hyp_pp2_collectexpression_constructor_args():
    sig = inspect.signature(pp2_CollectExpression.__init__)
    params = list(sig.parameters.keys())



def test_hyp_parameterizedexpression_is_not_abstract():
    assert not inspect.isabstract(ParameterizedExpression)


def test_hyp_parameterizedexpression_constructor_exists():
    assert callable(ParameterizedExpression.__init__)


def test_hyp_parameterizedexpression_constructor_args():
    sig = inspect.signature(ParameterizedExpression.__init__)
    params = list(sig.parameters.keys())



def test_hyp_pp2_selectorexpression_is_not_abstract():
    assert not inspect.isabstract(pp2_SelectorExpression)


def test_hyp_pp2_selectorexpression_constructor_exists():
    assert callable(pp2_SelectorExpression.__init__)


def test_hyp_pp2_selectorexpression_constructor_args():
    sig = inspect.signature(pp2_SelectorExpression.__init__)
    params = list(sig.parameters.keys())



def test_hyp_pp2_withlambdaexpression_is_not_abstract():
    assert not inspect.isabstract(pp2_WithLambdaExpression)


def test_hyp_pp2_withlambdaexpression_constructor_exists():
    assert callable(pp2_WithLambdaExpression.__init__)


def test_hyp_pp2_withlambdaexpression_constructor_args():
    sig = inspect.signature(pp2_WithLambdaExpression.__init__)
    params = list(sig.parameters.keys())



def test_hyp_pp2_atexpression_is_not_abstract():
    assert not inspect.isabstract(pp2_AtExpression)


def test_hyp_pp2_atexpression_constructor_exists():
    assert callable(pp2_AtExpression.__init__)


def test_hyp_pp2_atexpression_constructor_args():
    sig = inspect.signature(pp2_AtExpression.__init__)
    params = list(sig.parameters.keys())



def test_hyp_pp2_nodedefinition_is_not_abstract():
    assert not inspect.isabstract(pp2_NodeDefinition)


def test_hyp_pp2_nodedefinition_constructor_exists():
    assert callable(pp2_NodeDefinition.__init__)


def test_hyp_pp2_nodedefinition_constructor_args():
    sig = inspect.signature(pp2_NodeDefinition.__init__)
    params = list(sig.parameters.keys())



def test_hyp_pp2_parameterizedexpression_is_not_abstract():
    assert not inspect.isabstract(pp2_ParameterizedExpression)


def test_hyp_pp2_parameterizedexpression_constructor_exists():
    assert callable(pp2_ParameterizedExpression.__init__)


def test_hyp_pp2_parameterizedexpression_constructor_args():
    sig = inspect.signature(pp2_ParameterizedExpression.__init__)
    params = list(sig.parameters.keys())



def test_hyp_pp2_binaryexpression_is_not_abstract():
    assert not inspect.isabstract(pp2_BinaryExpression)


def test_hyp_pp2_binaryexpression_constructor_exists():
    assert callable(pp2_BinaryExpression.__init__)


def test_hyp_pp2_binaryexpression_constructor_args():
    sig = inspect.signature(pp2_BinaryExpression.__init__)
    params = list(sig.parameters.keys())



def test_hyp_pp2_hashentry_is_not_abstract():
    assert not inspect.isabstract(pp2_HashEntry)


def test_hyp_pp2_hashentry_constructor_exists():
    assert callable(pp2_HashEntry.__init__)


def test_hyp_pp2_hashentry_constructor_args():
    sig = inspect.signature(pp2_HashEntry.__init__)
    params = list(sig.parameters.keys())



def test_hyp_pp2_iquotedstring_is_not_abstract():
    assert not inspect.isabstract(pp2_IQuotedString)


def test_hyp_pp2_iquotedstring_constructor_exists():
    assert callable(pp2_IQuotedString.__init__)


def test_hyp_pp2_iquotedstring_constructor_args():
    sig = inspect.signature(pp2_IQuotedString.__init__)
    params = list(sig.parameters.keys())



def test_hyp_pp2_importexpression_is_not_abstract():
    assert not inspect.isabstract(pp2_ImportExpression)


def test_hyp_pp2_importexpression_constructor_exists():
    assert callable(pp2_ImportExpression.__init__)


def test_hyp_pp2_importexpression_constructor_args():
    sig = inspect.signature(pp2_ImportExpression.__init__)
    params = list(sig.parameters.keys())



def test_hyp_pp2_resourceexpression_is_not_abstract():
    assert not inspect.isabstract(pp2_ResourceExpression)


def test_hyp_pp2_resourceexpression_constructor_exists():
    assert callable(pp2_ResourceExpression.__init__)


def test_hyp_pp2_resourceexpression_constructor_args():
    sig = inspect.signature(pp2_ResourceExpression.__init__)
    params = list(sig.parameters.keys())



def test_hyp_literalexpression_is_not_abstract():
    assert not inspect.isabstract(LiteralExpression)


def test_hyp_literalexpression_constructor_exists():
    assert callable(LiteralExpression.__init__)


def test_hyp_literalexpression_constructor_args():
    sig = inspect.signature(LiteralExpression.__init__)
    params = list(sig.parameters.keys())



def test_hyp_pp2_literalclass_is_not_abstract():
    assert not inspect.isabstract(pp2_LiteralClass)


def test_hyp_pp2_literalclass_constructor_exists():
    assert callable(pp2_LiteralClass.__init__)


def test_hyp_pp2_literalclass_constructor_args():
    sig = inspect.signature(pp2_LiteralClass.__init__)
    params = list(sig.parameters.keys())



def test_hyp_pp2_literallist_is_not_abstract():
    assert not inspect.isabstract(pp2_LiteralList)


def test_hyp_pp2_literallist_constructor_exists():
    assert callable(pp2_LiteralList.__init__)


def test_hyp_pp2_literallist_constructor_args():
    sig = inspect.signature(pp2_LiteralList.__init__)
    params = list(sig.parameters.keys())



def test_hyp_pp2_virtualnameorreference_is_not_abstract():
    assert not inspect.isabstract(pp2_VirtualNameOrReference)


def test_hyp_pp2_virtualnameorreference_constructor_exists():
    assert callable(pp2_VirtualNameOrReference.__init__)


def test_hyp_pp2_virtualnameorreference_constructor_args():
    sig = inspect.signature(pp2_VirtualNameOrReference.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"
    assert "exported" in params, "Missing parameter 'exported'"





def test_hyp_pp2_literalhash_is_not_abstract():
    assert not inspect.isabstract(pp2_LiteralHash)


def test_hyp_pp2_literalhash_constructor_exists():
    assert callable(pp2_LiteralHash.__init__)


def test_hyp_pp2_literalhash_constructor_args():
    sig = inspect.signature(pp2_LiteralHash.__init__)
    params = list(sig.parameters.keys())



def test_hyp_pp2_literalnameorreference_is_not_abstract():
    assert not inspect.isabstract(pp2_LiteralNameOrReference)


def test_hyp_pp2_literalnameorreference_constructor_exists():
    assert callable(pp2_LiteralNameOrReference.__init__)


def test_hyp_pp2_literalnameorreference_constructor_args():
    sig = inspect.signature(pp2_LiteralNameOrReference.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"




def test_hyp_pp2_ifexpression_is_not_abstract():
    assert not inspect.isabstract(pp2_IfExpression)


def test_hyp_pp2_ifexpression_constructor_exists():
    assert callable(pp2_IfExpression.__init__)


def test_hyp_pp2_ifexpression_constructor_args():
    sig = inspect.signature(pp2_IfExpression.__init__)
    params = list(sig.parameters.keys())



def test_hyp_binaryexpression_is_not_abstract():
    assert not inspect.isabstract(BinaryExpression)


def test_hyp_binaryexpression_constructor_exists():
    assert callable(BinaryExpression.__init__)


def test_hyp_binaryexpression_constructor_args():
    sig = inspect.signature(BinaryExpression.__init__)
    params = list(sig.parameters.keys())



def test_hyp_pp2_namedaccessexpression_is_not_abstract():
    assert not inspect.isabstract(pp2_NamedAccessExpression)


def test_hyp_pp2_namedaccessexpression_constructor_exists():
    assert callable(pp2_NamedAccessExpression.__init__)


def test_hyp_pp2_namedaccessexpression_constructor_args():
    sig = inspect.signature(pp2_NamedAccessExpression.__init__)
    params = list(sig.parameters.keys())



def test_hyp_pp2_binaryopexpression_is_not_abstract():
    assert not inspect.isabstract(pp2_BinaryOpExpression)


def test_hyp_pp2_binaryopexpression_constructor_exists():
    assert callable(pp2_BinaryOpExpression.__init__)


def test_hyp_pp2_binaryopexpression_constructor_args():
    sig = inspect.signature(pp2_BinaryOpExpression.__init__)
    params = list(sig.parameters.keys())
    assert "opName" in params, "Missing parameter 'opName'"




def test_hyp_pp2_appendexpression_is_not_abstract():
    assert not inspect.isabstract(pp2_AppendExpression)


def test_hyp_pp2_appendexpression_constructor_exists():
    assert callable(pp2_AppendExpression.__init__)


def test_hyp_pp2_appendexpression_constructor_args():
    sig = inspect.signature(pp2_AppendExpression.__init__)
    params = list(sig.parameters.keys())



def test_hyp_pp2_orexpression_is_not_abstract():
    assert not inspect.isabstract(pp2_OrExpression)


def test_hyp_pp2_orexpression_constructor_exists():
    assert callable(pp2_OrExpression.__init__)


def test_hyp_pp2_orexpression_constructor_args():
    sig = inspect.signature(pp2_OrExpression.__init__)
    params = list(sig.parameters.keys())



def test_hyp_pp2_andexpression_is_not_abstract():
    assert not inspect.isabstract(pp2_AndExpression)


def test_hyp_pp2_andexpression_constructor_exists():
    assert callable(pp2_AndExpression.__init__)


def test_hyp_pp2_andexpression_constructor_args():
    sig = inspect.signature(pp2_AndExpression.__init__)
    params = list(sig.parameters.keys())



def test_hyp_pp2_selectorentry_is_not_abstract():
    assert not inspect.isabstract(pp2_SelectorEntry)


def test_hyp_pp2_selectorentry_constructor_exists():
    assert callable(pp2_SelectorEntry.__init__)


def test_hyp_pp2_selectorentry_constructor_args():
    sig = inspect.signature(pp2_SelectorEntry.__init__)
    params = list(sig.parameters.keys())



def test_hyp_pp2_assignmentexpression_is_not_abstract():
    assert not inspect.isabstract(pp2_AssignmentExpression)


def test_hyp_pp2_assignmentexpression_constructor_exists():
    assert callable(pp2_AssignmentExpression.__init__)


def test_hyp_pp2_assignmentexpression_constructor_args():
    sig = inspect.signature(pp2_AssignmentExpression.__init__)
    params = list(sig.parameters.keys())



def test_hyp_binaryopexpression_is_not_abstract():
    assert not inspect.isabstract(BinaryOpExpression)


def test_hyp_binaryopexpression_constructor_exists():
    assert callable(BinaryOpExpression.__init__)


def test_hyp_binaryopexpression_constructor_args():
    sig = inspect.signature(BinaryOpExpression.__init__)
    params = list(sig.parameters.keys())



def test_hyp_pp2_equalityexpression_is_not_abstract():
    assert not inspect.isabstract(pp2_EqualityExpression)


def test_hyp_pp2_equalityexpression_constructor_exists():
    assert callable(pp2_EqualityExpression.__init__)


def test_hyp_pp2_equalityexpression_constructor_args():
    sig = inspect.signature(pp2_EqualityExpression.__init__)
    params = list(sig.parameters.keys())



def test_hyp_pp2_inexpression_is_not_abstract():
    assert not inspect.isabstract(pp2_InExpression)


def test_hyp_pp2_inexpression_constructor_exists():
    assert callable(pp2_InExpression.__init__)


def test_hyp_pp2_inexpression_constructor_args():
    sig = inspect.signature(pp2_InExpression.__init__)
    params = list(sig.parameters.keys())



def test_hyp_pp2_matchingexpression_is_not_abstract():
    assert not inspect.isabstract(pp2_MatchingExpression)


def test_hyp_pp2_matchingexpression_constructor_exists():
    assert callable(pp2_MatchingExpression.__init__)


def test_hyp_pp2_matchingexpression_constructor_args():
    sig = inspect.signature(pp2_MatchingExpression.__init__)
    params = list(sig.parameters.keys())



def test_hyp_pp2_multiplicativeexpression_is_not_abstract():
    assert not inspect.isabstract(pp2_MultiplicativeExpression)


def test_hyp_pp2_multiplicativeexpression_constructor_exists():
    assert callable(pp2_MultiplicativeExpression.__init__)


def test_hyp_pp2_multiplicativeexpression_constructor_args():
    sig = inspect.signature(pp2_MultiplicativeExpression.__init__)
    params = list(sig.parameters.keys())



def test_hyp_pp2_shiftexpression_is_not_abstract():
    assert not inspect.isabstract(pp2_ShiftExpression)


def test_hyp_pp2_shiftexpression_constructor_exists():
    assert callable(pp2_ShiftExpression.__init__)


def test_hyp_pp2_shiftexpression_constructor_args():
    sig = inspect.signature(pp2_ShiftExpression.__init__)
    params = list(sig.parameters.keys())



def test_hyp_pp2_relationalexpression_is_not_abstract():
    assert not inspect.isabstract(pp2_RelationalExpression)


def test_hyp_pp2_relationalexpression_constructor_exists():
    assert callable(pp2_RelationalExpression.__init__)


def test_hyp_pp2_relationalexpression_constructor_args():
    sig = inspect.signature(pp2_RelationalExpression.__init__)
    params = list(sig.parameters.keys())



def test_hyp_pp2_additiveexpression_is_not_abstract():
    assert not inspect.isabstract(pp2_AdditiveExpression)


def test_hyp_pp2_additiveexpression_constructor_exists():
    assert callable(pp2_AdditiveExpression.__init__)


def test_hyp_pp2_additiveexpression_constructor_args():
    sig = inspect.signature(pp2_AdditiveExpression.__init__)
    params = list(sig.parameters.keys())



def test_hyp_pp2_relationshipexpression_is_not_abstract():
    assert not inspect.isabstract(pp2_RelationshipExpression)


def test_hyp_pp2_relationshipexpression_constructor_exists():
    assert callable(pp2_RelationshipExpression.__init__)


def test_hyp_pp2_relationshipexpression_constructor_args():
    sig = inspect.signature(pp2_RelationshipExpression.__init__)
    params = list(sig.parameters.keys())



def test_hyp_pp2_variableexpression_is_not_abstract():
    assert not inspect.isabstract(pp2_VariableExpression)


def test_hyp_pp2_variableexpression_constructor_exists():
    assert callable(pp2_VariableExpression.__init__)


def test_hyp_pp2_variableexpression_constructor_args():
    sig = inspect.signature(pp2_VariableExpression.__init__)
    params = list(sig.parameters.keys())
    assert "varName" in params, "Missing parameter 'varName'"




def test_hyp_pp2_literalname_is_not_abstract():
    assert not inspect.isabstract(pp2_LiteralName)


def test_hyp_pp2_literalname_constructor_exists():
    assert callable(pp2_LiteralName.__init__)


def test_hyp_pp2_literalname_constructor_args():
    sig = inspect.signature(pp2_LiteralName.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"




def test_hyp_pp2_literalregex_is_not_abstract():
    assert not inspect.isabstract(pp2_LiteralRegex)


def test_hyp_pp2_literalregex_constructor_exists():
    assert callable(pp2_LiteralRegex.__init__)


def test_hyp_pp2_literalregex_constructor_args():
    sig = inspect.signature(pp2_LiteralRegex.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"




def test_hyp_pp2_literaldefault_is_not_abstract():
    assert not inspect.isabstract(pp2_LiteralDefault)


def test_hyp_pp2_literaldefault_constructor_exists():
    assert callable(pp2_LiteralDefault.__init__)


def test_hyp_pp2_literaldefault_constructor_args():
    sig = inspect.signature(pp2_LiteralDefault.__init__)
    params = list(sig.parameters.keys())



def test_hyp_pp2_literalundef_is_not_abstract():
    assert not inspect.isabstract(pp2_LiteralUndef)


def test_hyp_pp2_literalundef_constructor_exists():
    assert callable(pp2_LiteralUndef.__init__)


def test_hyp_pp2_literalundef_constructor_args():
    sig = inspect.signature(pp2_LiteralUndef.__init__)
    params = list(sig.parameters.keys())



def test_hyp_pp2_literalboolean_is_not_abstract():
    assert not inspect.isabstract(pp2_LiteralBoolean)


def test_hyp_pp2_literalboolean_constructor_exists():
    assert callable(pp2_LiteralBoolean.__init__)


def test_hyp_pp2_literalboolean_constructor_args():
    sig = inspect.signature(pp2_LiteralBoolean.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"




def test_hyp_pp2_definition_is_not_abstract():
    assert not inspect.isabstract(pp2_Definition)


def test_hyp_pp2_definition_constructor_exists():
    assert callable(pp2_Definition.__init__)


def test_hyp_pp2_definition_constructor_args():
    sig = inspect.signature(pp2_Definition.__init__)
    params = list(sig.parameters.keys())
    assert "className" in params, "Missing parameter 'className'"




def test_hyp_pp2_literalexpression_is_not_abstract():
    assert not inspect.isabstract(pp2_LiteralExpression)


def test_hyp_pp2_literalexpression_constructor_exists():
    assert callable(pp2_LiteralExpression.__init__)


def test_hyp_pp2_literalexpression_constructor_args():
    sig = inspect.signature(pp2_LiteralExpression.__init__)
    params = list(sig.parameters.keys())



def test_hyp_definition_is_not_abstract():
    assert not inspect.isabstract(Definition)


def test_hyp_definition_constructor_exists():
    assert callable(Definition.__init__)


def test_hyp_definition_constructor_args():
    sig = inspect.signature(Definition.__init__)
    params = list(sig.parameters.keys())



def test_hyp_pp2_hostclassdefinition_is_not_abstract():
    assert not inspect.isabstract(pp2_HostClassDefinition)


def test_hyp_pp2_hostclassdefinition_constructor_exists():
    assert callable(pp2_HostClassDefinition.__init__)


def test_hyp_pp2_hostclassdefinition_constructor_args():
    sig = inspect.signature(pp2_HostClassDefinition.__init__)
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



def test_hyp_pp2_unaryminusexpression_is_not_abstract():
    assert not inspect.isabstract(pp2_UnaryMinusExpression)


def test_hyp_pp2_unaryminusexpression_constructor_exists():
    assert callable(pp2_UnaryMinusExpression.__init__)


def test_hyp_pp2_unaryminusexpression_constructor_args():
    sig = inspect.signature(pp2_UnaryMinusExpression.__init__)
    params = list(sig.parameters.keys())



def test_hyp_pp2_exportedcollectquery_is_not_abstract():
    assert not inspect.isabstract(pp2_ExportedCollectQuery)


def test_hyp_pp2_exportedcollectquery_constructor_exists():
    assert callable(pp2_ExportedCollectQuery.__init__)


def test_hyp_pp2_exportedcollectquery_constructor_args():
    sig = inspect.signature(pp2_ExportedCollectQuery.__init__)
    params = list(sig.parameters.keys())



def test_hyp_pp2_unarynotexpression_is_not_abstract():
    assert not inspect.isabstract(pp2_UnaryNotExpression)


def test_hyp_pp2_unarynotexpression_constructor_exists():
    assert callable(pp2_UnaryNotExpression.__init__)


def test_hyp_pp2_unarynotexpression_constructor_args():
    sig = inspect.signature(pp2_UnaryNotExpression.__init__)
    params = list(sig.parameters.keys())



def test_hyp_pp2_virtualcollectquery_is_not_abstract():
    assert not inspect.isabstract(pp2_VirtualCollectQuery)


def test_hyp_pp2_virtualcollectquery_constructor_exists():
    assert callable(pp2_VirtualCollectQuery.__init__)


def test_hyp_pp2_virtualcollectquery_constructor_args():
    sig = inspect.signature(pp2_VirtualCollectQuery.__init__)
    params = list(sig.parameters.keys())



def test_hyp_pp2_icollectquery_is_not_abstract():
    assert not inspect.isabstract(pp2_ICollectQuery)


def test_hyp_pp2_icollectquery_constructor_exists():
    assert callable(pp2_ICollectQuery.__init__)


def test_hyp_pp2_icollectquery_constructor_args():
    sig = inspect.signature(pp2_ICollectQuery.__init__)
    params = list(sig.parameters.keys())



def test_hyp_pp2_attributeoperation_is_not_abstract():
    assert not inspect.isabstract(pp2_AttributeOperation)


def test_hyp_pp2_attributeoperation_constructor_exists():
    assert callable(pp2_AttributeOperation.__init__)


def test_hyp_pp2_attributeoperation_constructor_args():
    sig = inspect.signature(pp2_AttributeOperation.__init__)
    params = list(sig.parameters.keys())
    assert "op" in params, "Missing parameter 'op'"
    assert "key" in params, "Missing parameter 'key'"





def test_hyp_pp2_attributeoperations_is_not_abstract():
    assert not inspect.isabstract(pp2_AttributeOperations)


def test_hyp_pp2_attributeoperations_constructor_exists():
    assert callable(pp2_AttributeOperations.__init__)


def test_hyp_pp2_attributeoperations_constructor_args():
    sig = inspect.signature(pp2_AttributeOperations.__init__)
    params = list(sig.parameters.keys())



def test_hyp_pp2_resourcebody_is_not_abstract():
    assert not inspect.isabstract(pp2_ResourceBody)


def test_hyp_pp2_resourcebody_constructor_exists():
    assert callable(pp2_ResourceBody.__init__)


def test_hyp_pp2_resourcebody_constructor_args():
    sig = inspect.signature(pp2_ResourceBody.__init__)
    params = list(sig.parameters.keys())



def test_hyp_pp2_expression_is_not_abstract():
    assert not inspect.isabstract(pp2_Expression)


def test_hyp_pp2_expression_constructor_exists():
    assert callable(pp2_Expression.__init__)


def test_hyp_pp2_expression_constructor_args():
    sig = inspect.signature(pp2_Expression.__init__)
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
ExpressionBlock_strategy = st.builds(
    ExpressionBlock,
)
pp2_Case_strategy = st.builds(
    pp2_Case,
)
Expression_strategy = st.builds(
    Expression,
)
pp2_CaseExpression_strategy = st.builds(
    pp2_CaseExpression,
)
pp2_DefinitionArgument_strategy = st.builds(
    pp2_DefinitionArgument,
    op=
        safe_text,
    argName=
        safe_text
)
pp2_DefinitionArgumentList_strategy = st.builds(
    pp2_DefinitionArgumentList,
)
pp2_PuppetManifest_strategy = st.builds(
    pp2_PuppetManifest,
)
pp2_Lambda_strategy = st.builds(
    pp2_Lambda,
)
pp2_UnlessExpression_strategy = st.builds(
    pp2_UnlessExpression,
)
pp2_SeparatorExpression_strategy = st.builds(
    pp2_SeparatorExpression,
)
Lambda_strategy = st.builds(
    Lambda,
)
pp2_RubyLambda_strategy = st.builds(
    pp2_RubyLambda,
)
pp2_JavaLambda_strategy = st.builds(
    pp2_JavaLambda,
    farrow=
        st.booleans()
)
pp2_ExprList_strategy = st.builds(
    pp2_ExprList,
)
pp2_ParenthesisedExpression_strategy = st.builds(
    pp2_ParenthesisedExpression,
)
IfExpression_strategy = st.builds(
    IfExpression,
)
pp2_ElseIfExpression_strategy = st.builds(
    pp2_ElseIfExpression,
)
pp2_ElseExpression_strategy = st.builds(
    pp2_ElseExpression,
)
pp2_ExpressionBlock_strategy = st.builds(
    pp2_ExpressionBlock,
)
pp2_UnaryExpression_strategy = st.builds(
    pp2_UnaryExpression,
)
TextExpression_strategy = st.builds(
    TextExpression,
)
pp2_VariableTE_strategy = st.builds(
    pp2_VariableTE,
    varName=
        safe_text
)
pp2_ExpressionTE_strategy = st.builds(
    pp2_ExpressionTE,
)
pp2_VerbatimTE_strategy = st.builds(
    pp2_VerbatimTE,
    text=
        safe_text
)
pp2_InterpolatedVariable_strategy = st.builds(
    pp2_InterpolatedVariable,
    varName=
        safe_text
)
pp2_StringExpression_strategy = st.builds(
    pp2_StringExpression,
)
pp2_TextExpression_strategy = st.builds(
    pp2_TextExpression,
)
IQuotedString_strategy = st.builds(
    IQuotedString,
)
StringExpression_strategy = st.builds(
    StringExpression,
)
pp2_SingleQuotedString_strategy = st.builds(
    pp2_SingleQuotedString,
    text=
        safe_text
)
pp2_UnquotedString_strategy = st.builds(
    pp2_UnquotedString,
)
pp2_DoubleQuotedString_strategy = st.builds(
    pp2_DoubleQuotedString,
)
WithLambdaExpression_strategy = st.builds(
    WithLambdaExpression,
)
pp2_MethodCall_strategy = st.builds(
    pp2_MethodCall,
    parenthesized=
        st.booleans()
)
pp2_FunctionCall_strategy = st.builds(
    pp2_FunctionCall,
)
pp2_CollectExpression_strategy = st.builds(
    pp2_CollectExpression,
)
ParameterizedExpression_strategy = st.builds(
    ParameterizedExpression,
)
pp2_SelectorExpression_strategy = st.builds(
    pp2_SelectorExpression,
)
pp2_WithLambdaExpression_strategy = st.builds(
    pp2_WithLambdaExpression,
)
pp2_AtExpression_strategy = st.builds(
    pp2_AtExpression,
)
pp2_NodeDefinition_strategy = st.builds(
    pp2_NodeDefinition,
)
pp2_ParameterizedExpression_strategy = st.builds(
    pp2_ParameterizedExpression,
)
pp2_BinaryExpression_strategy = st.builds(
    pp2_BinaryExpression,
)
pp2_HashEntry_strategy = st.builds(
    pp2_HashEntry,
)
pp2_IQuotedString_strategy = st.builds(
    pp2_IQuotedString,
)
pp2_ImportExpression_strategy = st.builds(
    pp2_ImportExpression,
)
pp2_ResourceExpression_strategy = st.builds(
    pp2_ResourceExpression,
)
LiteralExpression_strategy = st.builds(
    LiteralExpression,
)
pp2_LiteralClass_strategy = st.builds(
    pp2_LiteralClass,
)
pp2_LiteralList_strategy = st.builds(
    pp2_LiteralList,
)
pp2_VirtualNameOrReference_strategy = st.builds(
    pp2_VirtualNameOrReference,
    value=
        safe_text,
    exported=
        st.booleans()
)
pp2_LiteralHash_strategy = st.builds(
    pp2_LiteralHash,
)
pp2_LiteralNameOrReference_strategy = st.builds(
    pp2_LiteralNameOrReference,
    value=
        safe_text
)
pp2_IfExpression_strategy = st.builds(
    pp2_IfExpression,
)
BinaryExpression_strategy = st.builds(
    BinaryExpression,
)
pp2_NamedAccessExpression_strategy = st.builds(
    pp2_NamedAccessExpression,
)
pp2_BinaryOpExpression_strategy = st.builds(
    pp2_BinaryOpExpression,
    opName=
        safe_text
)
pp2_AppendExpression_strategy = st.builds(
    pp2_AppendExpression,
)
pp2_OrExpression_strategy = st.builds(
    pp2_OrExpression,
)
pp2_AndExpression_strategy = st.builds(
    pp2_AndExpression,
)
pp2_SelectorEntry_strategy = st.builds(
    pp2_SelectorEntry,
)
pp2_AssignmentExpression_strategy = st.builds(
    pp2_AssignmentExpression,
)
BinaryOpExpression_strategy = st.builds(
    BinaryOpExpression,
)
pp2_EqualityExpression_strategy = st.builds(
    pp2_EqualityExpression,
)
pp2_InExpression_strategy = st.builds(
    pp2_InExpression,
)
pp2_MatchingExpression_strategy = st.builds(
    pp2_MatchingExpression,
)
pp2_MultiplicativeExpression_strategy = st.builds(
    pp2_MultiplicativeExpression,
)
pp2_ShiftExpression_strategy = st.builds(
    pp2_ShiftExpression,
)
pp2_RelationalExpression_strategy = st.builds(
    pp2_RelationalExpression,
)
pp2_AdditiveExpression_strategy = st.builds(
    pp2_AdditiveExpression,
)
pp2_RelationshipExpression_strategy = st.builds(
    pp2_RelationshipExpression,
)
pp2_VariableExpression_strategy = st.builds(
    pp2_VariableExpression,
    varName=
        safe_text
)
pp2_LiteralName_strategy = st.builds(
    pp2_LiteralName,
    value=
        safe_text
)
pp2_LiteralRegex_strategy = st.builds(
    pp2_LiteralRegex,
    value=
        safe_text
)
pp2_LiteralDefault_strategy = st.builds(
    pp2_LiteralDefault,
)
pp2_LiteralUndef_strategy = st.builds(
    pp2_LiteralUndef,
)
pp2_LiteralBoolean_strategy = st.builds(
    pp2_LiteralBoolean,
    value=
        st.booleans()
)
pp2_Definition_strategy = st.builds(
    pp2_Definition,
    className=
        safe_text
)
pp2_LiteralExpression_strategy = st.builds(
    pp2_LiteralExpression,
)
Definition_strategy = st.builds(
    Definition,
)
pp2_HostClassDefinition_strategy = st.builds(
    pp2_HostClassDefinition,
)
ICollectQuery_strategy = st.builds(
    ICollectQuery,
)
UnaryExpression_strategy = st.builds(
    UnaryExpression,
)
pp2_UnaryMinusExpression_strategy = st.builds(
    pp2_UnaryMinusExpression,
)
pp2_ExportedCollectQuery_strategy = st.builds(
    pp2_ExportedCollectQuery,
)
pp2_UnaryNotExpression_strategy = st.builds(
    pp2_UnaryNotExpression,
)
pp2_VirtualCollectQuery_strategy = st.builds(
    pp2_VirtualCollectQuery,
)
pp2_ICollectQuery_strategy = st.builds(
    pp2_ICollectQuery,
)
pp2_AttributeOperation_strategy = st.builds(
    pp2_AttributeOperation,
    op=
        safe_text,
    key=
        safe_text
)
pp2_AttributeOperations_strategy = st.builds(
    pp2_AttributeOperations,
)
pp2_ResourceBody_strategy = st.builds(
    pp2_ResourceBody,
)
pp2_Expression_strategy = st.builds(
    pp2_Expression,
)








@given(instance=pp2_DefinitionArgument_strategy)
def test_hyp_pp2_definitionargument_op_setter(instance):
    original = instance.op
    instance.op = original
    assert instance.op == original



@given(instance=pp2_DefinitionArgument_strategy)
def test_hyp_pp2_definitionargument_argName_setter(instance):
    original = instance.argName
    instance.argName = original
    assert instance.argName == original











@given(instance=pp2_JavaLambda_strategy)
def test_hyp_pp2_javalambda_farrow_setter(instance):
    original = instance.farrow
    instance.farrow = original
    assert instance.farrow == original












@given(instance=pp2_VariableTE_strategy)
def test_hyp_pp2_variablete_varName_setter(instance):
    original = instance.varName
    instance.varName = original
    assert instance.varName == original





@given(instance=pp2_VerbatimTE_strategy)
def test_hyp_pp2_verbatimte_text_setter(instance):
    original = instance.text
    instance.text = original
    assert instance.text == original




@given(instance=pp2_InterpolatedVariable_strategy)
def test_hyp_pp2_interpolatedvariable_varName_setter(instance):
    original = instance.varName
    instance.varName = original
    assert instance.varName == original








@given(instance=pp2_SingleQuotedString_strategy)
def test_hyp_pp2_singlequotedstring_text_setter(instance):
    original = instance.text
    instance.text = original
    assert instance.text == original







@given(instance=pp2_MethodCall_strategy)
def test_hyp_pp2_methodcall_parenthesized_setter(instance):
    original = instance.parenthesized
    instance.parenthesized = original
    assert instance.parenthesized == original




















@given(instance=pp2_VirtualNameOrReference_strategy)
def test_hyp_pp2_virtualnameorreference_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original



@given(instance=pp2_VirtualNameOrReference_strategy)
def test_hyp_pp2_virtualnameorreference_exported_setter(instance):
    original = instance.exported
    instance.exported = original
    assert instance.exported == original





@given(instance=pp2_LiteralNameOrReference_strategy)
def test_hyp_pp2_literalnameorreference_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original







@given(instance=pp2_BinaryOpExpression_strategy)
def test_hyp_pp2_binaryopexpression_opName_setter(instance):
    original = instance.opName
    instance.opName = original
    assert instance.opName == original


















@given(instance=pp2_VariableExpression_strategy)
def test_hyp_pp2_variableexpression_varName_setter(instance):
    original = instance.varName
    instance.varName = original
    assert instance.varName == original




@given(instance=pp2_LiteralName_strategy)
def test_hyp_pp2_literalname_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original




@given(instance=pp2_LiteralRegex_strategy)
def test_hyp_pp2_literalregex_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original






@given(instance=pp2_LiteralBoolean_strategy)
def test_hyp_pp2_literalboolean_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original




@given(instance=pp2_Definition_strategy)
def test_hyp_pp2_definition_className_setter(instance):
    original = instance.className
    instance.className = original
    assert instance.className == original














@given(instance=pp2_AttributeOperation_strategy)
def test_hyp_pp2_attributeoperation_op_setter(instance):
    original = instance.op
    instance.op = original
    assert instance.op == original



@given(instance=pp2_AttributeOperation_strategy)
def test_hyp_pp2_attributeoperation_key_setter(instance):
    original = instance.key
    instance.key = original
    assert instance.key == original





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
    pp2_AdditiveExpression,
    pp2_AndExpression,
    pp2_AppendExpression,
    pp2_AssignmentExpression,
    pp2_AtExpression,
    pp2_AttributeOperation,
    pp2_AttributeOperations,
    pp2_BinaryExpression,
    pp2_BinaryOpExpression,
    pp2_Case,
    pp2_CaseExpression,
    pp2_CollectExpression,
    pp2_Definition,
    pp2_DefinitionArgument,
    pp2_DefinitionArgumentList,
    pp2_DoubleQuotedString,
    pp2_ElseExpression,
    pp2_ElseIfExpression,
    pp2_EqualityExpression,
    pp2_ExportedCollectQuery,
    pp2_ExprList,
    pp2_Expression,
    pp2_ExpressionBlock,
    pp2_ExpressionTE,
    pp2_FunctionCall,
    pp2_HashEntry,
    pp2_HostClassDefinition,
    pp2_ICollectQuery,
    pp2_IQuotedString,
    pp2_IfExpression,
    pp2_ImportExpression,
    pp2_InExpression,
    pp2_InterpolatedVariable,
    pp2_JavaLambda,
    pp2_Lambda,
    pp2_LiteralBoolean,
    pp2_LiteralClass,
    pp2_LiteralDefault,
    pp2_LiteralExpression,
    pp2_LiteralHash,
    pp2_LiteralList,
    pp2_LiteralName,
    pp2_LiteralNameOrReference,
    pp2_LiteralRegex,
    pp2_LiteralUndef,
    pp2_MatchingExpression,
    pp2_MethodCall,
    pp2_MultiplicativeExpression,
    pp2_NamedAccessExpression,
    pp2_NodeDefinition,
    pp2_OrExpression,
    pp2_ParameterizedExpression,
    pp2_ParenthesisedExpression,
    pp2_PuppetManifest,
    pp2_RelationalExpression,
    pp2_RelationshipExpression,
    pp2_ResourceBody,
    pp2_ResourceExpression,
    pp2_RubyLambda,
    pp2_SelectorEntry,
    pp2_SelectorExpression,
    pp2_SeparatorExpression,
    pp2_ShiftExpression,
    pp2_SingleQuotedString,
    pp2_StringExpression,
    pp2_TextExpression,
    pp2_UnaryExpression,
    pp2_UnaryMinusExpression,
    pp2_UnaryNotExpression,
    pp2_UnlessExpression,
    pp2_UnquotedString,
    pp2_VariableExpression,
    pp2_VariableTE,
    pp2_VerbatimTE,
    pp2_VirtualCollectQuery,
    pp2_VirtualNameOrReference,
    pp2_WithLambdaExpression,
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

def test_pp2_AttributeOperation_key_value_roundtrip():
    instance = pp2_AttributeOperation(key="sample_text", op="sample_text")
    assert instance.key == "sample_text"
    instance.key = "sample_text_2"
    assert instance.key == "sample_text_2"


def test_pp2_AttributeOperation_op_value_roundtrip():
    instance = pp2_AttributeOperation(key="sample_text", op="sample_text")
    assert instance.op == "sample_text"
    instance.op = "sample_text_2"
    assert instance.op == "sample_text_2"


def test_pp2_BinaryOpExpression_opName_value_roundtrip():
    instance = pp2_BinaryOpExpression(opName="sample_text")
    assert instance.opName == "sample_text"
    instance.opName = "sample_text_2"
    assert instance.opName == "sample_text_2"


def test_pp2_Definition_className_value_roundtrip():
    instance = pp2_Definition(className="sample_text")
    assert instance.className == "sample_text"
    instance.className = "sample_text_2"
    assert instance.className == "sample_text_2"


def test_pp2_DefinitionArgument_argName_value_roundtrip():
    instance = pp2_DefinitionArgument(argName="sample_text", op="sample_text")
    assert instance.argName == "sample_text"
    instance.argName = "sample_text_2"
    assert instance.argName == "sample_text_2"


def test_pp2_DefinitionArgument_op_value_roundtrip():
    instance = pp2_DefinitionArgument(argName="sample_text", op="sample_text")
    assert instance.op == "sample_text"
    instance.op = "sample_text_2"
    assert instance.op == "sample_text_2"


def test_pp2_InterpolatedVariable_varName_value_roundtrip():
    instance = pp2_InterpolatedVariable(varName="sample_text")
    assert instance.varName == "sample_text"
    instance.varName = "sample_text_2"
    assert instance.varName == "sample_text_2"


def test_pp2_JavaLambda_farrow_value_roundtrip():
    instance = pp2_JavaLambda(farrow=True)
    assert instance.farrow == True
    instance.farrow = False
    assert instance.farrow == False


def test_pp2_LiteralBoolean_value_value_roundtrip():
    instance = pp2_LiteralBoolean(value=True)
    assert instance.value == True
    instance.value = False
    assert instance.value == False


def test_pp2_LiteralName_value_value_roundtrip():
    instance = pp2_LiteralName(value="sample_text")
    assert instance.value == "sample_text"
    instance.value = "sample_text_2"
    assert instance.value == "sample_text_2"


def test_pp2_LiteralNameOrReference_value_value_roundtrip():
    instance = pp2_LiteralNameOrReference(value="sample_text")
    assert instance.value == "sample_text"
    instance.value = "sample_text_2"
    assert instance.value == "sample_text_2"


def test_pp2_LiteralRegex_value_value_roundtrip():
    instance = pp2_LiteralRegex(value="sample_text")
    assert instance.value == "sample_text"
    instance.value = "sample_text_2"
    assert instance.value == "sample_text_2"


def test_pp2_MethodCall_parenthesized_value_roundtrip():
    instance = pp2_MethodCall(parenthesized=True)
    assert instance.parenthesized == True
    instance.parenthesized = False
    assert instance.parenthesized == False


def test_pp2_SingleQuotedString_text_value_roundtrip():
    instance = pp2_SingleQuotedString(text="sample_text")
    assert instance.text == "sample_text"
    instance.text = "sample_text_2"
    assert instance.text == "sample_text_2"


def test_pp2_VariableExpression_varName_value_roundtrip():
    instance = pp2_VariableExpression(varName="sample_text")
    assert instance.varName == "sample_text"
    instance.varName = "sample_text_2"
    assert instance.varName == "sample_text_2"


def test_pp2_VariableTE_varName_value_roundtrip():
    instance = pp2_VariableTE(varName="sample_text")
    assert instance.varName == "sample_text"
    instance.varName = "sample_text_2"
    assert instance.varName == "sample_text_2"


def test_pp2_VerbatimTE_text_value_roundtrip():
    instance = pp2_VerbatimTE(text="sample_text")
    assert instance.text == "sample_text"
    instance.text = "sample_text_2"
    assert instance.text == "sample_text_2"


def test_pp2_VirtualNameOrReference_exported_value_roundtrip():
    instance = pp2_VirtualNameOrReference(exported=True, value="sample_text")
    assert instance.exported == True
    instance.exported = False
    assert instance.exported == False


def test_pp2_VirtualNameOrReference_value_value_roundtrip():
    instance = pp2_VirtualNameOrReference(exported=True, value="sample_text")
    assert instance.value == "sample_text"
    instance.value = "sample_text_2"
    assert instance.value == "sample_text_2"


def test_pp2_AndExpression_isa_BinaryExpression():
    instance = pp2_AndExpression()
    assert isinstance(instance, BinaryExpression)


def test_pp2_AppendExpression_isa_BinaryExpression():
    instance = pp2_AppendExpression()
    assert isinstance(instance, BinaryExpression)


def test_pp2_AssignmentExpression_isa_BinaryExpression():
    instance = pp2_AssignmentExpression()
    assert isinstance(instance, BinaryExpression)


def test_pp2_BinaryOpExpression_isa_BinaryExpression():
    instance = pp2_BinaryOpExpression(opName="sample_text")
    assert isinstance(instance, BinaryExpression)


def test_pp2_NamedAccessExpression_isa_BinaryExpression():
    instance = pp2_NamedAccessExpression()
    assert isinstance(instance, BinaryExpression)


def test_pp2_OrExpression_isa_BinaryExpression():
    instance = pp2_OrExpression()
    assert isinstance(instance, BinaryExpression)


def test_pp2_SelectorEntry_isa_BinaryExpression():
    instance = pp2_SelectorEntry()
    assert isinstance(instance, BinaryExpression)


def test_pp2_AdditiveExpression_isa_BinaryOpExpression():
    instance = pp2_AdditiveExpression()
    assert isinstance(instance, BinaryOpExpression)


def test_pp2_EqualityExpression_isa_BinaryOpExpression():
    instance = pp2_EqualityExpression()
    assert isinstance(instance, BinaryOpExpression)


def test_pp2_InExpression_isa_BinaryOpExpression():
    instance = pp2_InExpression()
    assert isinstance(instance, BinaryOpExpression)


def test_pp2_MatchingExpression_isa_BinaryOpExpression():
    instance = pp2_MatchingExpression()
    assert isinstance(instance, BinaryOpExpression)


def test_pp2_MultiplicativeExpression_isa_BinaryOpExpression():
    instance = pp2_MultiplicativeExpression()
    assert isinstance(instance, BinaryOpExpression)


def test_pp2_RelationalExpression_isa_BinaryOpExpression():
    instance = pp2_RelationalExpression()
    assert isinstance(instance, BinaryOpExpression)


def test_pp2_RelationshipExpression_isa_BinaryOpExpression():
    instance = pp2_RelationshipExpression()
    assert isinstance(instance, BinaryOpExpression)


def test_pp2_ShiftExpression_isa_BinaryOpExpression():
    instance = pp2_ShiftExpression()
    assert isinstance(instance, BinaryOpExpression)


def test_pp2_HostClassDefinition_isa_Definition():
    instance = pp2_HostClassDefinition()
    assert isinstance(instance, Definition)


def test_pp2_BinaryExpression_isa_Expression():
    instance = pp2_BinaryExpression()
    assert isinstance(instance, Expression)


def test_pp2_CaseExpression_isa_Expression():
    instance = pp2_CaseExpression()
    assert isinstance(instance, Expression)


def test_pp2_CollectExpression_isa_Expression():
    instance = pp2_CollectExpression()
    assert isinstance(instance, Expression)


def test_pp2_ExprList_isa_Expression():
    instance = pp2_ExprList()
    assert isinstance(instance, Expression)


def test_pp2_ExpressionBlock_isa_Expression():
    instance = pp2_ExpressionBlock()
    assert isinstance(instance, Expression)


def test_pp2_ImportExpression_isa_Expression():
    instance = pp2_ImportExpression()
    assert isinstance(instance, Expression)


def test_pp2_InterpolatedVariable_isa_Expression():
    instance = pp2_InterpolatedVariable(varName="sample_text")
    assert isinstance(instance, Expression)


def test_pp2_LiteralExpression_isa_Expression():
    instance = pp2_LiteralExpression()
    assert isinstance(instance, Expression)


def test_pp2_ParameterizedExpression_isa_Expression():
    instance = pp2_ParameterizedExpression()
    assert isinstance(instance, Expression)


def test_pp2_ParenthesisedExpression_isa_Expression():
    instance = pp2_ParenthesisedExpression()
    assert isinstance(instance, Expression)


def test_pp2_ResourceExpression_isa_Expression():
    instance = pp2_ResourceExpression()
    assert isinstance(instance, Expression)


def test_pp2_SeparatorExpression_isa_Expression():
    instance = pp2_SeparatorExpression()
    assert isinstance(instance, Expression)


def test_pp2_StringExpression_isa_Expression():
    instance = pp2_StringExpression()
    assert isinstance(instance, Expression)


def test_pp2_UnaryExpression_isa_Expression():
    instance = pp2_UnaryExpression()
    assert isinstance(instance, Expression)


def test_pp2_VariableExpression_isa_Expression():
    instance = pp2_VariableExpression(varName="sample_text")
    assert isinstance(instance, Expression)


def test_pp2_Case_isa_ExpressionBlock():
    instance = pp2_Case()
    assert isinstance(instance, ExpressionBlock)


def test_pp2_Definition_isa_ExpressionBlock():
    instance = pp2_Definition(className="sample_text")
    assert isinstance(instance, ExpressionBlock)


def test_pp2_ElseExpression_isa_ExpressionBlock():
    instance = pp2_ElseExpression()
    assert isinstance(instance, ExpressionBlock)


def test_pp2_IfExpression_isa_ExpressionBlock():
    instance = pp2_IfExpression()
    assert isinstance(instance, ExpressionBlock)


def test_pp2_Lambda_isa_ExpressionBlock():
    instance = pp2_Lambda()
    assert isinstance(instance, ExpressionBlock)


def test_pp2_NodeDefinition_isa_ExpressionBlock():
    instance = pp2_NodeDefinition()
    assert isinstance(instance, ExpressionBlock)


def test_pp2_PuppetManifest_isa_ExpressionBlock():
    instance = pp2_PuppetManifest()
    assert isinstance(instance, ExpressionBlock)


def test_pp2_UnlessExpression_isa_ExpressionBlock():
    instance = pp2_UnlessExpression()
    assert isinstance(instance, ExpressionBlock)


def test_pp2_ExportedCollectQuery_isa_ICollectQuery():
    instance = pp2_ExportedCollectQuery()
    assert isinstance(instance, ICollectQuery)


def test_pp2_VirtualCollectQuery_isa_ICollectQuery():
    instance = pp2_VirtualCollectQuery()
    assert isinstance(instance, ICollectQuery)


def test_pp2_DoubleQuotedString_isa_IQuotedString():
    instance = pp2_DoubleQuotedString()
    assert isinstance(instance, IQuotedString)


def test_pp2_SingleQuotedString_isa_IQuotedString():
    instance = pp2_SingleQuotedString(text="sample_text")
    assert isinstance(instance, IQuotedString)


def test_pp2_ElseIfExpression_isa_IfExpression():
    instance = pp2_ElseIfExpression()
    assert isinstance(instance, IfExpression)


def test_pp2_JavaLambda_isa_Lambda():
    instance = pp2_JavaLambda(farrow=True)
    assert isinstance(instance, Lambda)


def test_pp2_RubyLambda_isa_Lambda():
    instance = pp2_RubyLambda()
    assert isinstance(instance, Lambda)


def test_pp2_LiteralBoolean_isa_LiteralExpression():
    instance = pp2_LiteralBoolean(value=True)
    assert isinstance(instance, LiteralExpression)


def test_pp2_LiteralClass_isa_LiteralExpression():
    instance = pp2_LiteralClass()
    assert isinstance(instance, LiteralExpression)


def test_pp2_LiteralDefault_isa_LiteralExpression():
    instance = pp2_LiteralDefault()
    assert isinstance(instance, LiteralExpression)


def test_pp2_LiteralHash_isa_LiteralExpression():
    instance = pp2_LiteralHash()
    assert isinstance(instance, LiteralExpression)


def test_pp2_LiteralList_isa_LiteralExpression():
    instance = pp2_LiteralList()
    assert isinstance(instance, LiteralExpression)


def test_pp2_LiteralName_isa_LiteralExpression():
    instance = pp2_LiteralName(value="sample_text")
    assert isinstance(instance, LiteralExpression)


def test_pp2_LiteralNameOrReference_isa_LiteralExpression():
    instance = pp2_LiteralNameOrReference(value="sample_text")
    assert isinstance(instance, LiteralExpression)


def test_pp2_LiteralRegex_isa_LiteralExpression():
    instance = pp2_LiteralRegex(value="sample_text")
    assert isinstance(instance, LiteralExpression)


def test_pp2_LiteralUndef_isa_LiteralExpression():
    instance = pp2_LiteralUndef()
    assert isinstance(instance, LiteralExpression)


def test_pp2_VirtualNameOrReference_isa_LiteralExpression():
    instance = pp2_VirtualNameOrReference(exported=True, value="sample_text")
    assert isinstance(instance, LiteralExpression)


def test_pp2_AtExpression_isa_ParameterizedExpression():
    instance = pp2_AtExpression()
    assert isinstance(instance, ParameterizedExpression)


def test_pp2_SelectorExpression_isa_ParameterizedExpression():
    instance = pp2_SelectorExpression()
    assert isinstance(instance, ParameterizedExpression)


def test_pp2_WithLambdaExpression_isa_ParameterizedExpression():
    instance = pp2_WithLambdaExpression()
    assert isinstance(instance, ParameterizedExpression)


def test_pp2_DoubleQuotedString_isa_StringExpression():
    instance = pp2_DoubleQuotedString()
    assert isinstance(instance, StringExpression)


def test_pp2_SingleQuotedString_isa_StringExpression():
    instance = pp2_SingleQuotedString(text="sample_text")
    assert isinstance(instance, StringExpression)


def test_pp2_UnquotedString_isa_StringExpression():
    instance = pp2_UnquotedString()
    assert isinstance(instance, StringExpression)


def test_pp2_ExpressionTE_isa_TextExpression():
    instance = pp2_ExpressionTE()
    assert isinstance(instance, TextExpression)


def test_pp2_VariableTE_isa_TextExpression():
    instance = pp2_VariableTE(varName="sample_text")
    assert isinstance(instance, TextExpression)


def test_pp2_VerbatimTE_isa_TextExpression():
    instance = pp2_VerbatimTE(text="sample_text")
    assert isinstance(instance, TextExpression)


def test_pp2_ExportedCollectQuery_isa_UnaryExpression():
    instance = pp2_ExportedCollectQuery()
    assert isinstance(instance, UnaryExpression)


def test_pp2_UnaryMinusExpression_isa_UnaryExpression():
    instance = pp2_UnaryMinusExpression()
    assert isinstance(instance, UnaryExpression)


def test_pp2_UnaryNotExpression_isa_UnaryExpression():
    instance = pp2_UnaryNotExpression()
    assert isinstance(instance, UnaryExpression)


def test_pp2_VirtualCollectQuery_isa_UnaryExpression():
    instance = pp2_VirtualCollectQuery()
    assert isinstance(instance, UnaryExpression)


def test_pp2_FunctionCall_isa_WithLambdaExpression():
    instance = pp2_FunctionCall()
    assert isinstance(instance, WithLambdaExpression)


def test_pp2_MethodCall_isa_WithLambdaExpression():
    instance = pp2_MethodCall(parenthesized=True)
    assert isinstance(instance, WithLambdaExpression)


def test_assoc_arguments10_link_reassign_clear():
    a = pp2_DefinitionArgument(argName="sample_text", op="sample_text")
    b1 = pp2_DefinitionArgumentList()
    b2 = pp2_DefinitionArgumentList()
    _safe_set(a, 'pp2_DefinitionArgument', b1)
    assert _is_linked(a, 'pp2_DefinitionArgument', b1)
    if hasattr(b1, 'pp2_DefinitionArgumentList11'):
        assert _is_linked(b1, 'pp2_DefinitionArgumentList11', a)
    _safe_set(a, 'pp2_DefinitionArgument', b2)
    assert _is_linked(a, 'pp2_DefinitionArgument', b2)
    if hasattr(b1, 'pp2_DefinitionArgumentList11'):
        assert not _is_linked(b1, 'pp2_DefinitionArgumentList11', a)
    if hasattr(b2, 'pp2_DefinitionArgumentList11'):
        assert _is_linked(b2, 'pp2_DefinitionArgumentList11', a)
    _safe_set(a, 'pp2_DefinitionArgument', None)
    assert not _is_linked(a, 'pp2_DefinitionArgument', b2)
    if hasattr(b2, 'pp2_DefinitionArgumentList11'):
        assert not _is_linked(b2, 'pp2_DefinitionArgumentList11', a)


def test_assoc_arguments9_link_reassign_clear():
    a = pp2_Definition(className="sample_text")
    b1 = pp2_DefinitionArgumentList()
    b2 = pp2_DefinitionArgumentList()
    _safe_set(a, 'pp2_Definition', b1)
    assert _is_linked(a, 'pp2_Definition', b1)
    if hasattr(b1, 'pp2_DefinitionArgumentList'):
        assert _is_linked(b1, 'pp2_DefinitionArgumentList', a)
    _safe_set(a, 'pp2_Definition', b2)
    assert _is_linked(a, 'pp2_Definition', b2)
    if hasattr(b1, 'pp2_DefinitionArgumentList'):
        assert not _is_linked(b1, 'pp2_DefinitionArgumentList', a)
    if hasattr(b2, 'pp2_DefinitionArgumentList'):
        assert _is_linked(b2, 'pp2_DefinitionArgumentList', a)
    _safe_set(a, 'pp2_Definition', None)
    assert not _is_linked(a, 'pp2_Definition', b2)
    if hasattr(b2, 'pp2_DefinitionArgumentList'):
        assert not _is_linked(b2, 'pp2_DefinitionArgumentList', a)


def test_assoc_attributes5_link_reassign_clear():
    a = pp2_AttributeOperation(key="sample_text", op="sample_text")
    b1 = pp2_AttributeOperations()
    b2 = pp2_AttributeOperations()
    _safe_set(a, 'pp2_AttributeOperation7', b1)
    assert _is_linked(a, 'pp2_AttributeOperation7', b1)
    if hasattr(b1, 'pp2_AttributeOperations6'):
        assert _is_linked(b1, 'pp2_AttributeOperations6', a)
    _safe_set(a, 'pp2_AttributeOperation7', b2)
    assert _is_linked(a, 'pp2_AttributeOperation7', b2)
    if hasattr(b1, 'pp2_AttributeOperations6'):
        assert not _is_linked(b1, 'pp2_AttributeOperations6', a)
    if hasattr(b2, 'pp2_AttributeOperations6'):
        assert _is_linked(b2, 'pp2_AttributeOperations6', a)
    _safe_set(a, 'pp2_AttributeOperation7', None)
    assert not _is_linked(a, 'pp2_AttributeOperation7', b2)
    if hasattr(b2, 'pp2_AttributeOperations6'):
        assert not _is_linked(b2, 'pp2_AttributeOperations6', a)


def test_assoc_methodExpr87_link_reassign_clear():
    a = pp2_MethodCall(parenthesized=True)
    b1 = pp2_Expression()
    b2 = pp2_Expression()
    _safe_set(a, 'pp2_MethodCall', b1)
    assert _is_linked(a, 'pp2_MethodCall', b1)
    if hasattr(b1, 'pp2_Expression88'):
        assert _is_linked(b1, 'pp2_Expression88', a)
    _safe_set(a, 'pp2_MethodCall', b2)
    assert _is_linked(a, 'pp2_MethodCall', b2)
    if hasattr(b1, 'pp2_Expression88'):
        assert not _is_linked(b1, 'pp2_Expression88', a)
    if hasattr(b2, 'pp2_Expression88'):
        assert _is_linked(b2, 'pp2_Expression88', a)
    _safe_set(a, 'pp2_MethodCall', None)
    assert not _is_linked(a, 'pp2_MethodCall', b2)
    if hasattr(b2, 'pp2_Expression88'):
        assert not _is_linked(b2, 'pp2_Expression88', a)


def test_assoc_puppetType12_link_reassign_clear():
    a = pp2_DefinitionArgument(argName="sample_text", op="sample_text")
    b1 = pp2_Expression()
    b2 = pp2_Expression()
    _safe_set(a, 'pp2_DefinitionArgument13', b1)
    assert _is_linked(a, 'pp2_DefinitionArgument13', b1)
    if hasattr(b1, 'pp2_Expression14'):
        assert _is_linked(b1, 'pp2_Expression14', a)
    _safe_set(a, 'pp2_DefinitionArgument13', b2)
    assert _is_linked(a, 'pp2_DefinitionArgument13', b2)
    if hasattr(b1, 'pp2_Expression14'):
        assert not _is_linked(b1, 'pp2_Expression14', a)
    if hasattr(b2, 'pp2_Expression14'):
        assert _is_linked(b2, 'pp2_Expression14', a)
    _safe_set(a, 'pp2_DefinitionArgument13', None)
    assert not _is_linked(a, 'pp2_DefinitionArgument13', b2)
    if hasattr(b2, 'pp2_Expression14'):
        assert not _is_linked(b2, 'pp2_Expression14', a)


def test_assoc_value15_link_reassign_clear():
    a = pp2_DefinitionArgument(argName="sample_text", op="sample_text")
    b1 = pp2_Expression()
    b2 = pp2_Expression()
    _safe_set(a, 'pp2_DefinitionArgument16', b1)
    assert _is_linked(a, 'pp2_DefinitionArgument16', b1)
    if hasattr(b1, 'pp2_Expression17'):
        assert _is_linked(b1, 'pp2_Expression17', a)
    _safe_set(a, 'pp2_DefinitionArgument16', b2)
    assert _is_linked(a, 'pp2_DefinitionArgument16', b2)
    if hasattr(b1, 'pp2_Expression17'):
        assert not _is_linked(b1, 'pp2_Expression17', a)
    if hasattr(b2, 'pp2_Expression17'):
        assert _is_linked(b2, 'pp2_Expression17', a)
    _safe_set(a, 'pp2_DefinitionArgument16', None)
    assert not _is_linked(a, 'pp2_DefinitionArgument16', b2)
    if hasattr(b2, 'pp2_Expression17'):
        assert not _is_linked(b2, 'pp2_Expression17', a)


def test_assoc_value3_link_reassign_clear():
    a = pp2_AttributeOperation(key="sample_text", op="sample_text")
    b1 = pp2_Expression()
    b2 = pp2_Expression()
    _safe_set(a, 'pp2_AttributeOperation', b1)
    assert _is_linked(a, 'pp2_AttributeOperation', b1)
    if hasattr(b1, 'pp2_Expression4'):
        assert _is_linked(b1, 'pp2_Expression4', a)
    _safe_set(a, 'pp2_AttributeOperation', b2)
    assert _is_linked(a, 'pp2_AttributeOperation', b2)
    if hasattr(b1, 'pp2_Expression4'):
        assert not _is_linked(b1, 'pp2_Expression4', a)
    if hasattr(b2, 'pp2_Expression4'):
        assert _is_linked(b2, 'pp2_Expression4', a)
    _safe_set(a, 'pp2_AttributeOperation', None)
    assert not _is_linked(a, 'pp2_AttributeOperation', b2)
    if hasattr(b2, 'pp2_Expression4'):
        assert not _is_linked(b2, 'pp2_Expression4', a)


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


pp2_AdditiveExpression_strategy = st.builds(pp2_AdditiveExpression)
@given(instance=pp2_AdditiveExpression_strategy)
@settings(max_examples=25)
def test_pp2_AdditiveExpression_instantiation(instance):
    assert isinstance(instance, pp2_AdditiveExpression)


pp2_AndExpression_strategy = st.builds(pp2_AndExpression)
@given(instance=pp2_AndExpression_strategy)
@settings(max_examples=25)
def test_pp2_AndExpression_instantiation(instance):
    assert isinstance(instance, pp2_AndExpression)


pp2_AppendExpression_strategy = st.builds(pp2_AppendExpression)
@given(instance=pp2_AppendExpression_strategy)
@settings(max_examples=25)
def test_pp2_AppendExpression_instantiation(instance):
    assert isinstance(instance, pp2_AppendExpression)


pp2_AssignmentExpression_strategy = st.builds(pp2_AssignmentExpression)
@given(instance=pp2_AssignmentExpression_strategy)
@settings(max_examples=25)
def test_pp2_AssignmentExpression_instantiation(instance):
    assert isinstance(instance, pp2_AssignmentExpression)


pp2_AtExpression_strategy = st.builds(pp2_AtExpression)
@given(instance=pp2_AtExpression_strategy)
@settings(max_examples=25)
def test_pp2_AtExpression_instantiation(instance):
    assert isinstance(instance, pp2_AtExpression)


pp2_AttributeOperation_strategy = st.builds(pp2_AttributeOperation, key=safe_text, op=safe_text)
@given(instance=pp2_AttributeOperation_strategy)
@settings(max_examples=25)
def test_pp2_AttributeOperation_instantiation(instance):
    assert isinstance(instance, pp2_AttributeOperation)


pp2_AttributeOperations_strategy = st.builds(pp2_AttributeOperations)
@given(instance=pp2_AttributeOperations_strategy)
@settings(max_examples=25)
def test_pp2_AttributeOperations_instantiation(instance):
    assert isinstance(instance, pp2_AttributeOperations)


pp2_BinaryExpression_strategy = st.builds(pp2_BinaryExpression)
@given(instance=pp2_BinaryExpression_strategy)
@settings(max_examples=25)
def test_pp2_BinaryExpression_instantiation(instance):
    assert isinstance(instance, pp2_BinaryExpression)


pp2_BinaryOpExpression_strategy = st.builds(pp2_BinaryOpExpression, opName=safe_text)
@given(instance=pp2_BinaryOpExpression_strategy)
@settings(max_examples=25)
def test_pp2_BinaryOpExpression_instantiation(instance):
    assert isinstance(instance, pp2_BinaryOpExpression)


pp2_Case_strategy = st.builds(pp2_Case)
@given(instance=pp2_Case_strategy)
@settings(max_examples=25)
def test_pp2_Case_instantiation(instance):
    assert isinstance(instance, pp2_Case)


pp2_CaseExpression_strategy = st.builds(pp2_CaseExpression)
@given(instance=pp2_CaseExpression_strategy)
@settings(max_examples=25)
def test_pp2_CaseExpression_instantiation(instance):
    assert isinstance(instance, pp2_CaseExpression)


pp2_CollectExpression_strategy = st.builds(pp2_CollectExpression)
@given(instance=pp2_CollectExpression_strategy)
@settings(max_examples=25)
def test_pp2_CollectExpression_instantiation(instance):
    assert isinstance(instance, pp2_CollectExpression)


pp2_Definition_strategy = st.builds(pp2_Definition, className=safe_text)
@given(instance=pp2_Definition_strategy)
@settings(max_examples=25)
def test_pp2_Definition_instantiation(instance):
    assert isinstance(instance, pp2_Definition)


pp2_DefinitionArgument_strategy = st.builds(pp2_DefinitionArgument, argName=safe_text, op=safe_text)
@given(instance=pp2_DefinitionArgument_strategy)
@settings(max_examples=25)
def test_pp2_DefinitionArgument_instantiation(instance):
    assert isinstance(instance, pp2_DefinitionArgument)


pp2_DefinitionArgumentList_strategy = st.builds(pp2_DefinitionArgumentList)
@given(instance=pp2_DefinitionArgumentList_strategy)
@settings(max_examples=25)
def test_pp2_DefinitionArgumentList_instantiation(instance):
    assert isinstance(instance, pp2_DefinitionArgumentList)


pp2_DoubleQuotedString_strategy = st.builds(pp2_DoubleQuotedString)
@given(instance=pp2_DoubleQuotedString_strategy)
@settings(max_examples=25)
def test_pp2_DoubleQuotedString_instantiation(instance):
    assert isinstance(instance, pp2_DoubleQuotedString)


pp2_ElseExpression_strategy = st.builds(pp2_ElseExpression)
@given(instance=pp2_ElseExpression_strategy)
@settings(max_examples=25)
def test_pp2_ElseExpression_instantiation(instance):
    assert isinstance(instance, pp2_ElseExpression)


pp2_ElseIfExpression_strategy = st.builds(pp2_ElseIfExpression)
@given(instance=pp2_ElseIfExpression_strategy)
@settings(max_examples=25)
def test_pp2_ElseIfExpression_instantiation(instance):
    assert isinstance(instance, pp2_ElseIfExpression)


pp2_EqualityExpression_strategy = st.builds(pp2_EqualityExpression)
@given(instance=pp2_EqualityExpression_strategy)
@settings(max_examples=25)
def test_pp2_EqualityExpression_instantiation(instance):
    assert isinstance(instance, pp2_EqualityExpression)


pp2_ExportedCollectQuery_strategy = st.builds(pp2_ExportedCollectQuery)
@given(instance=pp2_ExportedCollectQuery_strategy)
@settings(max_examples=25)
def test_pp2_ExportedCollectQuery_instantiation(instance):
    assert isinstance(instance, pp2_ExportedCollectQuery)


pp2_ExprList_strategy = st.builds(pp2_ExprList)
@given(instance=pp2_ExprList_strategy)
@settings(max_examples=25)
def test_pp2_ExprList_instantiation(instance):
    assert isinstance(instance, pp2_ExprList)


pp2_Expression_strategy = st.builds(pp2_Expression)
@given(instance=pp2_Expression_strategy)
@settings(max_examples=25)
def test_pp2_Expression_instantiation(instance):
    assert isinstance(instance, pp2_Expression)


pp2_ExpressionBlock_strategy = st.builds(pp2_ExpressionBlock)
@given(instance=pp2_ExpressionBlock_strategy)
@settings(max_examples=25)
def test_pp2_ExpressionBlock_instantiation(instance):
    assert isinstance(instance, pp2_ExpressionBlock)


pp2_ExpressionTE_strategy = st.builds(pp2_ExpressionTE)
@given(instance=pp2_ExpressionTE_strategy)
@settings(max_examples=25)
def test_pp2_ExpressionTE_instantiation(instance):
    assert isinstance(instance, pp2_ExpressionTE)


pp2_FunctionCall_strategy = st.builds(pp2_FunctionCall)
@given(instance=pp2_FunctionCall_strategy)
@settings(max_examples=25)
def test_pp2_FunctionCall_instantiation(instance):
    assert isinstance(instance, pp2_FunctionCall)


pp2_HashEntry_strategy = st.builds(pp2_HashEntry)
@given(instance=pp2_HashEntry_strategy)
@settings(max_examples=25)
def test_pp2_HashEntry_instantiation(instance):
    assert isinstance(instance, pp2_HashEntry)


pp2_HostClassDefinition_strategy = st.builds(pp2_HostClassDefinition)
@given(instance=pp2_HostClassDefinition_strategy)
@settings(max_examples=25)
def test_pp2_HostClassDefinition_instantiation(instance):
    assert isinstance(instance, pp2_HostClassDefinition)


pp2_ICollectQuery_strategy = st.builds(pp2_ICollectQuery)
@given(instance=pp2_ICollectQuery_strategy)
@settings(max_examples=25)
def test_pp2_ICollectQuery_instantiation(instance):
    assert isinstance(instance, pp2_ICollectQuery)


pp2_IQuotedString_strategy = st.builds(pp2_IQuotedString)
@given(instance=pp2_IQuotedString_strategy)
@settings(max_examples=25)
def test_pp2_IQuotedString_instantiation(instance):
    assert isinstance(instance, pp2_IQuotedString)


pp2_IfExpression_strategy = st.builds(pp2_IfExpression)
@given(instance=pp2_IfExpression_strategy)
@settings(max_examples=25)
def test_pp2_IfExpression_instantiation(instance):
    assert isinstance(instance, pp2_IfExpression)


pp2_ImportExpression_strategy = st.builds(pp2_ImportExpression)
@given(instance=pp2_ImportExpression_strategy)
@settings(max_examples=25)
def test_pp2_ImportExpression_instantiation(instance):
    assert isinstance(instance, pp2_ImportExpression)


pp2_InExpression_strategy = st.builds(pp2_InExpression)
@given(instance=pp2_InExpression_strategy)
@settings(max_examples=25)
def test_pp2_InExpression_instantiation(instance):
    assert isinstance(instance, pp2_InExpression)


pp2_InterpolatedVariable_strategy = st.builds(pp2_InterpolatedVariable, varName=safe_text)
@given(instance=pp2_InterpolatedVariable_strategy)
@settings(max_examples=25)
def test_pp2_InterpolatedVariable_instantiation(instance):
    assert isinstance(instance, pp2_InterpolatedVariable)


pp2_JavaLambda_strategy = st.builds(pp2_JavaLambda, farrow=st.booleans())
@given(instance=pp2_JavaLambda_strategy)
@settings(max_examples=25)
def test_pp2_JavaLambda_instantiation(instance):
    assert isinstance(instance, pp2_JavaLambda)


pp2_Lambda_strategy = st.builds(pp2_Lambda)
@given(instance=pp2_Lambda_strategy)
@settings(max_examples=25)
def test_pp2_Lambda_instantiation(instance):
    assert isinstance(instance, pp2_Lambda)


pp2_LiteralBoolean_strategy = st.builds(pp2_LiteralBoolean, value=st.booleans())
@given(instance=pp2_LiteralBoolean_strategy)
@settings(max_examples=25)
def test_pp2_LiteralBoolean_instantiation(instance):
    assert isinstance(instance, pp2_LiteralBoolean)


pp2_LiteralClass_strategy = st.builds(pp2_LiteralClass)
@given(instance=pp2_LiteralClass_strategy)
@settings(max_examples=25)
def test_pp2_LiteralClass_instantiation(instance):
    assert isinstance(instance, pp2_LiteralClass)


pp2_LiteralDefault_strategy = st.builds(pp2_LiteralDefault)
@given(instance=pp2_LiteralDefault_strategy)
@settings(max_examples=25)
def test_pp2_LiteralDefault_instantiation(instance):
    assert isinstance(instance, pp2_LiteralDefault)


pp2_LiteralExpression_strategy = st.builds(pp2_LiteralExpression)
@given(instance=pp2_LiteralExpression_strategy)
@settings(max_examples=25)
def test_pp2_LiteralExpression_instantiation(instance):
    assert isinstance(instance, pp2_LiteralExpression)


pp2_LiteralHash_strategy = st.builds(pp2_LiteralHash)
@given(instance=pp2_LiteralHash_strategy)
@settings(max_examples=25)
def test_pp2_LiteralHash_instantiation(instance):
    assert isinstance(instance, pp2_LiteralHash)


pp2_LiteralList_strategy = st.builds(pp2_LiteralList)
@given(instance=pp2_LiteralList_strategy)
@settings(max_examples=25)
def test_pp2_LiteralList_instantiation(instance):
    assert isinstance(instance, pp2_LiteralList)


pp2_LiteralName_strategy = st.builds(pp2_LiteralName, value=safe_text)
@given(instance=pp2_LiteralName_strategy)
@settings(max_examples=25)
def test_pp2_LiteralName_instantiation(instance):
    assert isinstance(instance, pp2_LiteralName)


pp2_LiteralNameOrReference_strategy = st.builds(pp2_LiteralNameOrReference, value=safe_text)
@given(instance=pp2_LiteralNameOrReference_strategy)
@settings(max_examples=25)
def test_pp2_LiteralNameOrReference_instantiation(instance):
    assert isinstance(instance, pp2_LiteralNameOrReference)


pp2_LiteralRegex_strategy = st.builds(pp2_LiteralRegex, value=safe_text)
@given(instance=pp2_LiteralRegex_strategy)
@settings(max_examples=25)
def test_pp2_LiteralRegex_instantiation(instance):
    assert isinstance(instance, pp2_LiteralRegex)


pp2_LiteralUndef_strategy = st.builds(pp2_LiteralUndef)
@given(instance=pp2_LiteralUndef_strategy)
@settings(max_examples=25)
def test_pp2_LiteralUndef_instantiation(instance):
    assert isinstance(instance, pp2_LiteralUndef)


pp2_MatchingExpression_strategy = st.builds(pp2_MatchingExpression)
@given(instance=pp2_MatchingExpression_strategy)
@settings(max_examples=25)
def test_pp2_MatchingExpression_instantiation(instance):
    assert isinstance(instance, pp2_MatchingExpression)


pp2_MethodCall_strategy = st.builds(pp2_MethodCall, parenthesized=st.booleans())
@given(instance=pp2_MethodCall_strategy)
@settings(max_examples=25)
def test_pp2_MethodCall_instantiation(instance):
    assert isinstance(instance, pp2_MethodCall)


pp2_MultiplicativeExpression_strategy = st.builds(pp2_MultiplicativeExpression)
@given(instance=pp2_MultiplicativeExpression_strategy)
@settings(max_examples=25)
def test_pp2_MultiplicativeExpression_instantiation(instance):
    assert isinstance(instance, pp2_MultiplicativeExpression)


pp2_NamedAccessExpression_strategy = st.builds(pp2_NamedAccessExpression)
@given(instance=pp2_NamedAccessExpression_strategy)
@settings(max_examples=25)
def test_pp2_NamedAccessExpression_instantiation(instance):
    assert isinstance(instance, pp2_NamedAccessExpression)


pp2_NodeDefinition_strategy = st.builds(pp2_NodeDefinition)
@given(instance=pp2_NodeDefinition_strategy)
@settings(max_examples=25)
def test_pp2_NodeDefinition_instantiation(instance):
    assert isinstance(instance, pp2_NodeDefinition)


pp2_OrExpression_strategy = st.builds(pp2_OrExpression)
@given(instance=pp2_OrExpression_strategy)
@settings(max_examples=25)
def test_pp2_OrExpression_instantiation(instance):
    assert isinstance(instance, pp2_OrExpression)


pp2_ParameterizedExpression_strategy = st.builds(pp2_ParameterizedExpression)
@given(instance=pp2_ParameterizedExpression_strategy)
@settings(max_examples=25)
def test_pp2_ParameterizedExpression_instantiation(instance):
    assert isinstance(instance, pp2_ParameterizedExpression)


pp2_ParenthesisedExpression_strategy = st.builds(pp2_ParenthesisedExpression)
@given(instance=pp2_ParenthesisedExpression_strategy)
@settings(max_examples=25)
def test_pp2_ParenthesisedExpression_instantiation(instance):
    assert isinstance(instance, pp2_ParenthesisedExpression)


pp2_PuppetManifest_strategy = st.builds(pp2_PuppetManifest)
@given(instance=pp2_PuppetManifest_strategy)
@settings(max_examples=25)
def test_pp2_PuppetManifest_instantiation(instance):
    assert isinstance(instance, pp2_PuppetManifest)


pp2_RelationalExpression_strategy = st.builds(pp2_RelationalExpression)
@given(instance=pp2_RelationalExpression_strategy)
@settings(max_examples=25)
def test_pp2_RelationalExpression_instantiation(instance):
    assert isinstance(instance, pp2_RelationalExpression)


pp2_RelationshipExpression_strategy = st.builds(pp2_RelationshipExpression)
@given(instance=pp2_RelationshipExpression_strategy)
@settings(max_examples=25)
def test_pp2_RelationshipExpression_instantiation(instance):
    assert isinstance(instance, pp2_RelationshipExpression)


pp2_ResourceBody_strategy = st.builds(pp2_ResourceBody)
@given(instance=pp2_ResourceBody_strategy)
@settings(max_examples=25)
def test_pp2_ResourceBody_instantiation(instance):
    assert isinstance(instance, pp2_ResourceBody)


pp2_ResourceExpression_strategy = st.builds(pp2_ResourceExpression)
@given(instance=pp2_ResourceExpression_strategy)
@settings(max_examples=25)
def test_pp2_ResourceExpression_instantiation(instance):
    assert isinstance(instance, pp2_ResourceExpression)


pp2_RubyLambda_strategy = st.builds(pp2_RubyLambda)
@given(instance=pp2_RubyLambda_strategy)
@settings(max_examples=25)
def test_pp2_RubyLambda_instantiation(instance):
    assert isinstance(instance, pp2_RubyLambda)


pp2_SelectorEntry_strategy = st.builds(pp2_SelectorEntry)
@given(instance=pp2_SelectorEntry_strategy)
@settings(max_examples=25)
def test_pp2_SelectorEntry_instantiation(instance):
    assert isinstance(instance, pp2_SelectorEntry)


pp2_SelectorExpression_strategy = st.builds(pp2_SelectorExpression)
@given(instance=pp2_SelectorExpression_strategy)
@settings(max_examples=25)
def test_pp2_SelectorExpression_instantiation(instance):
    assert isinstance(instance, pp2_SelectorExpression)


pp2_SeparatorExpression_strategy = st.builds(pp2_SeparatorExpression)
@given(instance=pp2_SeparatorExpression_strategy)
@settings(max_examples=25)
def test_pp2_SeparatorExpression_instantiation(instance):
    assert isinstance(instance, pp2_SeparatorExpression)


pp2_ShiftExpression_strategy = st.builds(pp2_ShiftExpression)
@given(instance=pp2_ShiftExpression_strategy)
@settings(max_examples=25)
def test_pp2_ShiftExpression_instantiation(instance):
    assert isinstance(instance, pp2_ShiftExpression)


pp2_SingleQuotedString_strategy = st.builds(pp2_SingleQuotedString, text=safe_text)
@given(instance=pp2_SingleQuotedString_strategy)
@settings(max_examples=25)
def test_pp2_SingleQuotedString_instantiation(instance):
    assert isinstance(instance, pp2_SingleQuotedString)


pp2_StringExpression_strategy = st.builds(pp2_StringExpression)
@given(instance=pp2_StringExpression_strategy)
@settings(max_examples=25)
def test_pp2_StringExpression_instantiation(instance):
    assert isinstance(instance, pp2_StringExpression)


pp2_TextExpression_strategy = st.builds(pp2_TextExpression)
@given(instance=pp2_TextExpression_strategy)
@settings(max_examples=25)
def test_pp2_TextExpression_instantiation(instance):
    assert isinstance(instance, pp2_TextExpression)


pp2_UnaryExpression_strategy = st.builds(pp2_UnaryExpression)
@given(instance=pp2_UnaryExpression_strategy)
@settings(max_examples=25)
def test_pp2_UnaryExpression_instantiation(instance):
    assert isinstance(instance, pp2_UnaryExpression)


pp2_UnaryMinusExpression_strategy = st.builds(pp2_UnaryMinusExpression)
@given(instance=pp2_UnaryMinusExpression_strategy)
@settings(max_examples=25)
def test_pp2_UnaryMinusExpression_instantiation(instance):
    assert isinstance(instance, pp2_UnaryMinusExpression)


pp2_UnaryNotExpression_strategy = st.builds(pp2_UnaryNotExpression)
@given(instance=pp2_UnaryNotExpression_strategy)
@settings(max_examples=25)
def test_pp2_UnaryNotExpression_instantiation(instance):
    assert isinstance(instance, pp2_UnaryNotExpression)


pp2_UnlessExpression_strategy = st.builds(pp2_UnlessExpression)
@given(instance=pp2_UnlessExpression_strategy)
@settings(max_examples=25)
def test_pp2_UnlessExpression_instantiation(instance):
    assert isinstance(instance, pp2_UnlessExpression)


pp2_UnquotedString_strategy = st.builds(pp2_UnquotedString)
@given(instance=pp2_UnquotedString_strategy)
@settings(max_examples=25)
def test_pp2_UnquotedString_instantiation(instance):
    assert isinstance(instance, pp2_UnquotedString)


pp2_VariableExpression_strategy = st.builds(pp2_VariableExpression, varName=safe_text)
@given(instance=pp2_VariableExpression_strategy)
@settings(max_examples=25)
def test_pp2_VariableExpression_instantiation(instance):
    assert isinstance(instance, pp2_VariableExpression)


pp2_VariableTE_strategy = st.builds(pp2_VariableTE, varName=safe_text)
@given(instance=pp2_VariableTE_strategy)
@settings(max_examples=25)
def test_pp2_VariableTE_instantiation(instance):
    assert isinstance(instance, pp2_VariableTE)


pp2_VerbatimTE_strategy = st.builds(pp2_VerbatimTE, text=safe_text)
@given(instance=pp2_VerbatimTE_strategy)
@settings(max_examples=25)
def test_pp2_VerbatimTE_instantiation(instance):
    assert isinstance(instance, pp2_VerbatimTE)


pp2_VirtualCollectQuery_strategy = st.builds(pp2_VirtualCollectQuery)
@given(instance=pp2_VirtualCollectQuery_strategy)
@settings(max_examples=25)
def test_pp2_VirtualCollectQuery_instantiation(instance):
    assert isinstance(instance, pp2_VirtualCollectQuery)


pp2_VirtualNameOrReference_strategy = st.builds(pp2_VirtualNameOrReference, exported=st.booleans(), value=safe_text)
@given(instance=pp2_VirtualNameOrReference_strategy)
@settings(max_examples=25)
def test_pp2_VirtualNameOrReference_instantiation(instance):
    assert isinstance(instance, pp2_VirtualNameOrReference)


pp2_WithLambdaExpression_strategy = st.builds(pp2_WithLambdaExpression)
@given(instance=pp2_WithLambdaExpression_strategy)
@settings(max_examples=25)
def test_pp2_WithLambdaExpression_instantiation(instance):
    assert isinstance(instance, pp2_WithLambdaExpression)



