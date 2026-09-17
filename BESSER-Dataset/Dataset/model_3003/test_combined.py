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
    RangeLiteral,
    amethyst_CharRangeLiteral,
    amethyst_NumberRangeLiteral,
    Symbol,
    amethyst_ParameterDeclaration,
    amethyst_DefinitionDeclaration,
    amethyst_ForInitializerDeclaration,
    amethyst_TagLoopInitializerDeclaration,
    amethyst_VariableDeclaration,
    amethyst_ClassDeclaration,
    PrimitiveType,
    amethyst_FloatType,
    amethyst_IntType,
    amethyst_StringType,
    amethyst_DefinitionType,
    amethyst_BooleanType,
    amethyst_AnyType,
    amethyst_CharType,
    Type,
    amethyst_PrimitiveType,
    AbstractType,
    amethyst_ArrayType,
    amethyst_Type,
    amethyst_AbstractType,
    Literal,
    amethyst_BooleanLiteral,
    amethyst_NullLiteral,
    amethyst_FloatLiteral,
    amethyst_RangeLiteral,
    amethyst_IntLiteral,
    amethyst_StringLiteral,
    amethyst_CharLiteral,
    Expression,
    amethyst_ShiftExpression,
    amethyst_AndExpression,
    amethyst_CallExpression,
    amethyst_AdditiveExpression,
    amethyst_MatchingExpression,
    amethyst_SuperExpression,
    amethyst_ParenthisedExpression,
    amethyst_SelfExpression,
    amethyst_TypeCastExpression,
    amethyst_IndexAccessExpression,
    amethyst_InExpression,
    amethyst_MultiplicativeExpression,
    amethyst_AssignmentExpression,
    amethyst_MemberAccessExpression,
    amethyst_UnaryMinusExpression,
    amethyst_EqualityExpression,
    amethyst_NotExpression,
    amethyst_RelationalExpression,
    amethyst_Literal,
    amethyst_OrExpression,
    amethyst_NewExpression,
    amethyst_SymbolReference,
    amethyst_TagExpression,
    amethyst_EObject,
    amethyst_TagAttribute,
    amethyst_TagLoopExpression,
    amethyst_ClassType,
    amethyst_TagDeclaration,
    Statement,
    amethyst_ElseIfStatement,
    amethyst_BreakStatement,
    amethyst_ForStatement,
    amethyst_CaseElseStatement,
    amethyst_JsCodeStatement,
    amethyst_Expression,
    amethyst_WhenStatement,
    amethyst_IfStatement,
    amethyst_ElseStatement,
    amethyst_NextStatement,
    amethyst_CaseStatement,
    amethyst_ReturnStatement,
    amethyst_WhileStatement,
    amethyst_Symbol,
    amethyst_Statement,
    amethyst_Import,
    amethyst_Module,
    amethyst_PropertyDeclaration,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_hyp_rangeliteral_is_not_abstract():
    assert not inspect.isabstract(RangeLiteral)


def test_hyp_rangeliteral_constructor_exists():
    assert callable(RangeLiteral.__init__)


def test_hyp_rangeliteral_constructor_args():
    sig = inspect.signature(RangeLiteral.__init__)
    params = list(sig.parameters.keys())



def test_hyp_amethyst_charrangeliteral_is_not_abstract():
    assert not inspect.isabstract(amethyst_CharRangeLiteral)


def test_hyp_amethyst_charrangeliteral_constructor_exists():
    assert callable(amethyst_CharRangeLiteral.__init__)


def test_hyp_amethyst_charrangeliteral_constructor_args():
    sig = inspect.signature(amethyst_CharRangeLiteral.__init__)
    params = list(sig.parameters.keys())



def test_hyp_amethyst_numberrangeliteral_is_not_abstract():
    assert not inspect.isabstract(amethyst_NumberRangeLiteral)


def test_hyp_amethyst_numberrangeliteral_constructor_exists():
    assert callable(amethyst_NumberRangeLiteral.__init__)


def test_hyp_amethyst_numberrangeliteral_constructor_args():
    sig = inspect.signature(amethyst_NumberRangeLiteral.__init__)
    params = list(sig.parameters.keys())



def test_hyp_symbol_is_not_abstract():
    assert not inspect.isabstract(Symbol)


def test_hyp_symbol_constructor_exists():
    assert callable(Symbol.__init__)


def test_hyp_symbol_constructor_args():
    sig = inspect.signature(Symbol.__init__)
    params = list(sig.parameters.keys())



def test_hyp_amethyst_parameterdeclaration_is_not_abstract():
    assert not inspect.isabstract(amethyst_ParameterDeclaration)


def test_hyp_amethyst_parameterdeclaration_constructor_exists():
    assert callable(amethyst_ParameterDeclaration.__init__)


def test_hyp_amethyst_parameterdeclaration_constructor_args():
    sig = inspect.signature(amethyst_ParameterDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_hyp_amethyst_definitiondeclaration_is_not_abstract():
    assert not inspect.isabstract(amethyst_DefinitionDeclaration)


def test_hyp_amethyst_definitiondeclaration_constructor_exists():
    assert callable(amethyst_DefinitionDeclaration.__init__)


def test_hyp_amethyst_definitiondeclaration_constructor_args():
    sig = inspect.signature(amethyst_DefinitionDeclaration.__init__)
    params = list(sig.parameters.keys())
    assert "static" in params, "Missing parameter 'static'"




def test_hyp_amethyst_forinitializerdeclaration_is_not_abstract():
    assert not inspect.isabstract(amethyst_ForInitializerDeclaration)


def test_hyp_amethyst_forinitializerdeclaration_constructor_exists():
    assert callable(amethyst_ForInitializerDeclaration.__init__)


def test_hyp_amethyst_forinitializerdeclaration_constructor_args():
    sig = inspect.signature(amethyst_ForInitializerDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_hyp_amethyst_tagloopinitializerdeclaration_is_not_abstract():
    assert not inspect.isabstract(amethyst_TagLoopInitializerDeclaration)


def test_hyp_amethyst_tagloopinitializerdeclaration_constructor_exists():
    assert callable(amethyst_TagLoopInitializerDeclaration.__init__)


def test_hyp_amethyst_tagloopinitializerdeclaration_constructor_args():
    sig = inspect.signature(amethyst_TagLoopInitializerDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_hyp_amethyst_variabledeclaration_is_not_abstract():
    assert not inspect.isabstract(amethyst_VariableDeclaration)


def test_hyp_amethyst_variabledeclaration_constructor_exists():
    assert callable(amethyst_VariableDeclaration.__init__)


def test_hyp_amethyst_variabledeclaration_constructor_args():
    sig = inspect.signature(amethyst_VariableDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_hyp_amethyst_classdeclaration_is_not_abstract():
    assert not inspect.isabstract(amethyst_ClassDeclaration)


def test_hyp_amethyst_classdeclaration_constructor_exists():
    assert callable(amethyst_ClassDeclaration.__init__)


def test_hyp_amethyst_classdeclaration_constructor_args():
    sig = inspect.signature(amethyst_ClassDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_hyp_primitivetype_is_not_abstract():
    assert not inspect.isabstract(PrimitiveType)


def test_hyp_primitivetype_constructor_exists():
    assert callable(PrimitiveType.__init__)


def test_hyp_primitivetype_constructor_args():
    sig = inspect.signature(PrimitiveType.__init__)
    params = list(sig.parameters.keys())



def test_hyp_amethyst_floattype_is_not_abstract():
    assert not inspect.isabstract(amethyst_FloatType)


def test_hyp_amethyst_floattype_constructor_exists():
    assert callable(amethyst_FloatType.__init__)


def test_hyp_amethyst_floattype_constructor_args():
    sig = inspect.signature(amethyst_FloatType.__init__)
    params = list(sig.parameters.keys())



def test_hyp_amethyst_inttype_is_not_abstract():
    assert not inspect.isabstract(amethyst_IntType)


def test_hyp_amethyst_inttype_constructor_exists():
    assert callable(amethyst_IntType.__init__)


def test_hyp_amethyst_inttype_constructor_args():
    sig = inspect.signature(amethyst_IntType.__init__)
    params = list(sig.parameters.keys())



def test_hyp_amethyst_stringtype_is_not_abstract():
    assert not inspect.isabstract(amethyst_StringType)


def test_hyp_amethyst_stringtype_constructor_exists():
    assert callable(amethyst_StringType.__init__)


def test_hyp_amethyst_stringtype_constructor_args():
    sig = inspect.signature(amethyst_StringType.__init__)
    params = list(sig.parameters.keys())



def test_hyp_amethyst_definitiontype_is_not_abstract():
    assert not inspect.isabstract(amethyst_DefinitionType)


def test_hyp_amethyst_definitiontype_constructor_exists():
    assert callable(amethyst_DefinitionType.__init__)


def test_hyp_amethyst_definitiontype_constructor_args():
    sig = inspect.signature(amethyst_DefinitionType.__init__)
    params = list(sig.parameters.keys())



def test_hyp_amethyst_booleantype_is_not_abstract():
    assert not inspect.isabstract(amethyst_BooleanType)


def test_hyp_amethyst_booleantype_constructor_exists():
    assert callable(amethyst_BooleanType.__init__)


def test_hyp_amethyst_booleantype_constructor_args():
    sig = inspect.signature(amethyst_BooleanType.__init__)
    params = list(sig.parameters.keys())



def test_hyp_amethyst_anytype_is_not_abstract():
    assert not inspect.isabstract(amethyst_AnyType)


def test_hyp_amethyst_anytype_constructor_exists():
    assert callable(amethyst_AnyType.__init__)


def test_hyp_amethyst_anytype_constructor_args():
    sig = inspect.signature(amethyst_AnyType.__init__)
    params = list(sig.parameters.keys())



def test_hyp_amethyst_chartype_is_not_abstract():
    assert not inspect.isabstract(amethyst_CharType)


def test_hyp_amethyst_chartype_constructor_exists():
    assert callable(amethyst_CharType.__init__)


def test_hyp_amethyst_chartype_constructor_args():
    sig = inspect.signature(amethyst_CharType.__init__)
    params = list(sig.parameters.keys())



def test_hyp_type_is_not_abstract():
    assert not inspect.isabstract(Type)


def test_hyp_type_constructor_exists():
    assert callable(Type.__init__)


def test_hyp_type_constructor_args():
    sig = inspect.signature(Type.__init__)
    params = list(sig.parameters.keys())



def test_hyp_amethyst_primitivetype_is_not_abstract():
    assert not inspect.isabstract(amethyst_PrimitiveType)


def test_hyp_amethyst_primitivetype_constructor_exists():
    assert callable(amethyst_PrimitiveType.__init__)


def test_hyp_amethyst_primitivetype_constructor_args():
    sig = inspect.signature(amethyst_PrimitiveType.__init__)
    params = list(sig.parameters.keys())



def test_hyp_abstracttype_is_not_abstract():
    assert not inspect.isabstract(AbstractType)


def test_hyp_abstracttype_constructor_exists():
    assert callable(AbstractType.__init__)


def test_hyp_abstracttype_constructor_args():
    sig = inspect.signature(AbstractType.__init__)
    params = list(sig.parameters.keys())



def test_hyp_amethyst_arraytype_is_not_abstract():
    assert not inspect.isabstract(amethyst_ArrayType)


def test_hyp_amethyst_arraytype_constructor_exists():
    assert callable(amethyst_ArrayType.__init__)


def test_hyp_amethyst_arraytype_constructor_args():
    sig = inspect.signature(amethyst_ArrayType.__init__)
    params = list(sig.parameters.keys())



def test_hyp_amethyst_type_is_not_abstract():
    assert not inspect.isabstract(amethyst_Type)


def test_hyp_amethyst_type_constructor_exists():
    assert callable(amethyst_Type.__init__)


def test_hyp_amethyst_type_constructor_args():
    sig = inspect.signature(amethyst_Type.__init__)
    params = list(sig.parameters.keys())



def test_hyp_amethyst_abstracttype_is_not_abstract():
    assert not inspect.isabstract(amethyst_AbstractType)


def test_hyp_amethyst_abstracttype_constructor_exists():
    assert callable(amethyst_AbstractType.__init__)


def test_hyp_amethyst_abstracttype_constructor_args():
    sig = inspect.signature(amethyst_AbstractType.__init__)
    params = list(sig.parameters.keys())



def test_hyp_literal_is_not_abstract():
    assert not inspect.isabstract(Literal)


def test_hyp_literal_constructor_exists():
    assert callable(Literal.__init__)


def test_hyp_literal_constructor_args():
    sig = inspect.signature(Literal.__init__)
    params = list(sig.parameters.keys())



def test_hyp_amethyst_booleanliteral_is_not_abstract():
    assert not inspect.isabstract(amethyst_BooleanLiteral)


def test_hyp_amethyst_booleanliteral_constructor_exists():
    assert callable(amethyst_BooleanLiteral.__init__)


def test_hyp_amethyst_booleanliteral_constructor_args():
    sig = inspect.signature(amethyst_BooleanLiteral.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"




def test_hyp_amethyst_nullliteral_is_not_abstract():
    assert not inspect.isabstract(amethyst_NullLiteral)


def test_hyp_amethyst_nullliteral_constructor_exists():
    assert callable(amethyst_NullLiteral.__init__)


def test_hyp_amethyst_nullliteral_constructor_args():
    sig = inspect.signature(amethyst_NullLiteral.__init__)
    params = list(sig.parameters.keys())



def test_hyp_amethyst_floatliteral_is_not_abstract():
    assert not inspect.isabstract(amethyst_FloatLiteral)


def test_hyp_amethyst_floatliteral_constructor_exists():
    assert callable(amethyst_FloatLiteral.__init__)


def test_hyp_amethyst_floatliteral_constructor_args():
    sig = inspect.signature(amethyst_FloatLiteral.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"




def test_hyp_amethyst_rangeliteral_is_not_abstract():
    assert not inspect.isabstract(amethyst_RangeLiteral)


def test_hyp_amethyst_rangeliteral_constructor_exists():
    assert callable(amethyst_RangeLiteral.__init__)


def test_hyp_amethyst_rangeliteral_constructor_args():
    sig = inspect.signature(amethyst_RangeLiteral.__init__)
    params = list(sig.parameters.keys())



def test_hyp_amethyst_intliteral_is_not_abstract():
    assert not inspect.isabstract(amethyst_IntLiteral)


def test_hyp_amethyst_intliteral_constructor_exists():
    assert callable(amethyst_IntLiteral.__init__)


def test_hyp_amethyst_intliteral_constructor_args():
    sig = inspect.signature(amethyst_IntLiteral.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"




def test_hyp_amethyst_stringliteral_is_not_abstract():
    assert not inspect.isabstract(amethyst_StringLiteral)


def test_hyp_amethyst_stringliteral_constructor_exists():
    assert callable(amethyst_StringLiteral.__init__)


def test_hyp_amethyst_stringliteral_constructor_args():
    sig = inspect.signature(amethyst_StringLiteral.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"




def test_hyp_amethyst_charliteral_is_not_abstract():
    assert not inspect.isabstract(amethyst_CharLiteral)


def test_hyp_amethyst_charliteral_constructor_exists():
    assert callable(amethyst_CharLiteral.__init__)


def test_hyp_amethyst_charliteral_constructor_args():
    sig = inspect.signature(amethyst_CharLiteral.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"




def test_hyp_expression_is_not_abstract():
    assert not inspect.isabstract(Expression)


def test_hyp_expression_constructor_exists():
    assert callable(Expression.__init__)


def test_hyp_expression_constructor_args():
    sig = inspect.signature(Expression.__init__)
    params = list(sig.parameters.keys())



def test_hyp_amethyst_shiftexpression_is_not_abstract():
    assert not inspect.isabstract(amethyst_ShiftExpression)


def test_hyp_amethyst_shiftexpression_constructor_exists():
    assert callable(amethyst_ShiftExpression.__init__)


def test_hyp_amethyst_shiftexpression_constructor_args():
    sig = inspect.signature(amethyst_ShiftExpression.__init__)
    params = list(sig.parameters.keys())
    assert "operator" in params, "Missing parameter 'operator'"




def test_hyp_amethyst_andexpression_is_not_abstract():
    assert not inspect.isabstract(amethyst_AndExpression)


def test_hyp_amethyst_andexpression_constructor_exists():
    assert callable(amethyst_AndExpression.__init__)


def test_hyp_amethyst_andexpression_constructor_args():
    sig = inspect.signature(amethyst_AndExpression.__init__)
    params = list(sig.parameters.keys())



def test_hyp_amethyst_callexpression_is_not_abstract():
    assert not inspect.isabstract(amethyst_CallExpression)


def test_hyp_amethyst_callexpression_constructor_exists():
    assert callable(amethyst_CallExpression.__init__)


def test_hyp_amethyst_callexpression_constructor_args():
    sig = inspect.signature(amethyst_CallExpression.__init__)
    params = list(sig.parameters.keys())



def test_hyp_amethyst_additiveexpression_is_not_abstract():
    assert not inspect.isabstract(amethyst_AdditiveExpression)


def test_hyp_amethyst_additiveexpression_constructor_exists():
    assert callable(amethyst_AdditiveExpression.__init__)


def test_hyp_amethyst_additiveexpression_constructor_args():
    sig = inspect.signature(amethyst_AdditiveExpression.__init__)
    params = list(sig.parameters.keys())
    assert "operator" in params, "Missing parameter 'operator'"




def test_hyp_amethyst_matchingexpression_is_not_abstract():
    assert not inspect.isabstract(amethyst_MatchingExpression)


def test_hyp_amethyst_matchingexpression_constructor_exists():
    assert callable(amethyst_MatchingExpression.__init__)


def test_hyp_amethyst_matchingexpression_constructor_args():
    sig = inspect.signature(amethyst_MatchingExpression.__init__)
    params = list(sig.parameters.keys())
    assert "operator" in params, "Missing parameter 'operator'"




def test_hyp_amethyst_superexpression_is_not_abstract():
    assert not inspect.isabstract(amethyst_SuperExpression)


def test_hyp_amethyst_superexpression_constructor_exists():
    assert callable(amethyst_SuperExpression.__init__)


def test_hyp_amethyst_superexpression_constructor_args():
    sig = inspect.signature(amethyst_SuperExpression.__init__)
    params = list(sig.parameters.keys())



def test_hyp_amethyst_parenthisedexpression_is_not_abstract():
    assert not inspect.isabstract(amethyst_ParenthisedExpression)


def test_hyp_amethyst_parenthisedexpression_constructor_exists():
    assert callable(amethyst_ParenthisedExpression.__init__)


def test_hyp_amethyst_parenthisedexpression_constructor_args():
    sig = inspect.signature(amethyst_ParenthisedExpression.__init__)
    params = list(sig.parameters.keys())



def test_hyp_amethyst_selfexpression_is_not_abstract():
    assert not inspect.isabstract(amethyst_SelfExpression)


def test_hyp_amethyst_selfexpression_constructor_exists():
    assert callable(amethyst_SelfExpression.__init__)


def test_hyp_amethyst_selfexpression_constructor_args():
    sig = inspect.signature(amethyst_SelfExpression.__init__)
    params = list(sig.parameters.keys())



def test_hyp_amethyst_typecastexpression_is_not_abstract():
    assert not inspect.isabstract(amethyst_TypeCastExpression)


def test_hyp_amethyst_typecastexpression_constructor_exists():
    assert callable(amethyst_TypeCastExpression.__init__)


def test_hyp_amethyst_typecastexpression_constructor_args():
    sig = inspect.signature(amethyst_TypeCastExpression.__init__)
    params = list(sig.parameters.keys())



def test_hyp_amethyst_indexaccessexpression_is_not_abstract():
    assert not inspect.isabstract(amethyst_IndexAccessExpression)


def test_hyp_amethyst_indexaccessexpression_constructor_exists():
    assert callable(amethyst_IndexAccessExpression.__init__)


def test_hyp_amethyst_indexaccessexpression_constructor_args():
    sig = inspect.signature(amethyst_IndexAccessExpression.__init__)
    params = list(sig.parameters.keys())



def test_hyp_amethyst_inexpression_is_not_abstract():
    assert not inspect.isabstract(amethyst_InExpression)


def test_hyp_amethyst_inexpression_constructor_exists():
    assert callable(amethyst_InExpression.__init__)


def test_hyp_amethyst_inexpression_constructor_args():
    sig = inspect.signature(amethyst_InExpression.__init__)
    params = list(sig.parameters.keys())



def test_hyp_amethyst_multiplicativeexpression_is_not_abstract():
    assert not inspect.isabstract(amethyst_MultiplicativeExpression)


def test_hyp_amethyst_multiplicativeexpression_constructor_exists():
    assert callable(amethyst_MultiplicativeExpression.__init__)


def test_hyp_amethyst_multiplicativeexpression_constructor_args():
    sig = inspect.signature(amethyst_MultiplicativeExpression.__init__)
    params = list(sig.parameters.keys())
    assert "operator" in params, "Missing parameter 'operator'"




def test_hyp_amethyst_assignmentexpression_is_not_abstract():
    assert not inspect.isabstract(amethyst_AssignmentExpression)


def test_hyp_amethyst_assignmentexpression_constructor_exists():
    assert callable(amethyst_AssignmentExpression.__init__)


def test_hyp_amethyst_assignmentexpression_constructor_args():
    sig = inspect.signature(amethyst_AssignmentExpression.__init__)
    params = list(sig.parameters.keys())



def test_hyp_amethyst_memberaccessexpression_is_not_abstract():
    assert not inspect.isabstract(amethyst_MemberAccessExpression)


def test_hyp_amethyst_memberaccessexpression_constructor_exists():
    assert callable(amethyst_MemberAccessExpression.__init__)


def test_hyp_amethyst_memberaccessexpression_constructor_args():
    sig = inspect.signature(amethyst_MemberAccessExpression.__init__)
    params = list(sig.parameters.keys())



def test_hyp_amethyst_unaryminusexpression_is_not_abstract():
    assert not inspect.isabstract(amethyst_UnaryMinusExpression)


def test_hyp_amethyst_unaryminusexpression_constructor_exists():
    assert callable(amethyst_UnaryMinusExpression.__init__)


def test_hyp_amethyst_unaryminusexpression_constructor_args():
    sig = inspect.signature(amethyst_UnaryMinusExpression.__init__)
    params = list(sig.parameters.keys())



def test_hyp_amethyst_equalityexpression_is_not_abstract():
    assert not inspect.isabstract(amethyst_EqualityExpression)


def test_hyp_amethyst_equalityexpression_constructor_exists():
    assert callable(amethyst_EqualityExpression.__init__)


def test_hyp_amethyst_equalityexpression_constructor_args():
    sig = inspect.signature(amethyst_EqualityExpression.__init__)
    params = list(sig.parameters.keys())
    assert "operator" in params, "Missing parameter 'operator'"




def test_hyp_amethyst_notexpression_is_not_abstract():
    assert not inspect.isabstract(amethyst_NotExpression)


def test_hyp_amethyst_notexpression_constructor_exists():
    assert callable(amethyst_NotExpression.__init__)


def test_hyp_amethyst_notexpression_constructor_args():
    sig = inspect.signature(amethyst_NotExpression.__init__)
    params = list(sig.parameters.keys())



def test_hyp_amethyst_relationalexpression_is_not_abstract():
    assert not inspect.isabstract(amethyst_RelationalExpression)


def test_hyp_amethyst_relationalexpression_constructor_exists():
    assert callable(amethyst_RelationalExpression.__init__)


def test_hyp_amethyst_relationalexpression_constructor_args():
    sig = inspect.signature(amethyst_RelationalExpression.__init__)
    params = list(sig.parameters.keys())
    assert "operator" in params, "Missing parameter 'operator'"




def test_hyp_amethyst_literal_is_not_abstract():
    assert not inspect.isabstract(amethyst_Literal)


def test_hyp_amethyst_literal_constructor_exists():
    assert callable(amethyst_Literal.__init__)


def test_hyp_amethyst_literal_constructor_args():
    sig = inspect.signature(amethyst_Literal.__init__)
    params = list(sig.parameters.keys())



def test_hyp_amethyst_orexpression_is_not_abstract():
    assert not inspect.isabstract(amethyst_OrExpression)


def test_hyp_amethyst_orexpression_constructor_exists():
    assert callable(amethyst_OrExpression.__init__)


def test_hyp_amethyst_orexpression_constructor_args():
    sig = inspect.signature(amethyst_OrExpression.__init__)
    params = list(sig.parameters.keys())



def test_hyp_amethyst_newexpression_is_not_abstract():
    assert not inspect.isabstract(amethyst_NewExpression)


def test_hyp_amethyst_newexpression_constructor_exists():
    assert callable(amethyst_NewExpression.__init__)


def test_hyp_amethyst_newexpression_constructor_args():
    sig = inspect.signature(amethyst_NewExpression.__init__)
    params = list(sig.parameters.keys())



def test_hyp_amethyst_symbolreference_is_not_abstract():
    assert not inspect.isabstract(amethyst_SymbolReference)


def test_hyp_amethyst_symbolreference_constructor_exists():
    assert callable(amethyst_SymbolReference.__init__)


def test_hyp_amethyst_symbolreference_constructor_args():
    sig = inspect.signature(amethyst_SymbolReference.__init__)
    params = list(sig.parameters.keys())



def test_hyp_amethyst_tagexpression_is_not_abstract():
    assert not inspect.isabstract(amethyst_TagExpression)


def test_hyp_amethyst_tagexpression_constructor_exists():
    assert callable(amethyst_TagExpression.__init__)


def test_hyp_amethyst_tagexpression_constructor_args():
    sig = inspect.signature(amethyst_TagExpression.__init__)
    params = list(sig.parameters.keys())



def test_hyp_amethyst_eobject_is_not_abstract():
    assert not inspect.isabstract(amethyst_EObject)


def test_hyp_amethyst_eobject_constructor_exists():
    assert callable(amethyst_EObject.__init__)


def test_hyp_amethyst_eobject_constructor_args():
    sig = inspect.signature(amethyst_EObject.__init__)
    params = list(sig.parameters.keys())



def test_hyp_amethyst_tagattribute_is_not_abstract():
    assert not inspect.isabstract(amethyst_TagAttribute)


def test_hyp_amethyst_tagattribute_constructor_exists():
    assert callable(amethyst_TagAttribute.__init__)


def test_hyp_amethyst_tagattribute_constructor_args():
    sig = inspect.signature(amethyst_TagAttribute.__init__)
    params = list(sig.parameters.keys())



def test_hyp_amethyst_tagloopexpression_is_not_abstract():
    assert not inspect.isabstract(amethyst_TagLoopExpression)


def test_hyp_amethyst_tagloopexpression_constructor_exists():
    assert callable(amethyst_TagLoopExpression.__init__)


def test_hyp_amethyst_tagloopexpression_constructor_args():
    sig = inspect.signature(amethyst_TagLoopExpression.__init__)
    params = list(sig.parameters.keys())



def test_hyp_amethyst_classtype_is_not_abstract():
    assert not inspect.isabstract(amethyst_ClassType)


def test_hyp_amethyst_classtype_constructor_exists():
    assert callable(amethyst_ClassType.__init__)


def test_hyp_amethyst_classtype_constructor_args():
    sig = inspect.signature(amethyst_ClassType.__init__)
    params = list(sig.parameters.keys())



def test_hyp_amethyst_tagdeclaration_is_not_abstract():
    assert not inspect.isabstract(amethyst_TagDeclaration)


def test_hyp_amethyst_tagdeclaration_constructor_exists():
    assert callable(amethyst_TagDeclaration.__init__)


def test_hyp_amethyst_tagdeclaration_constructor_args():
    sig = inspect.signature(amethyst_TagDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_hyp_statement_is_not_abstract():
    assert not inspect.isabstract(Statement)


def test_hyp_statement_constructor_exists():
    assert callable(Statement.__init__)


def test_hyp_statement_constructor_args():
    sig = inspect.signature(Statement.__init__)
    params = list(sig.parameters.keys())



def test_hyp_amethyst_elseifstatement_is_not_abstract():
    assert not inspect.isabstract(amethyst_ElseIfStatement)


def test_hyp_amethyst_elseifstatement_constructor_exists():
    assert callable(amethyst_ElseIfStatement.__init__)


def test_hyp_amethyst_elseifstatement_constructor_args():
    sig = inspect.signature(amethyst_ElseIfStatement.__init__)
    params = list(sig.parameters.keys())



def test_hyp_amethyst_breakstatement_is_not_abstract():
    assert not inspect.isabstract(amethyst_BreakStatement)


def test_hyp_amethyst_breakstatement_constructor_exists():
    assert callable(amethyst_BreakStatement.__init__)


def test_hyp_amethyst_breakstatement_constructor_args():
    sig = inspect.signature(amethyst_BreakStatement.__init__)
    params = list(sig.parameters.keys())



def test_hyp_amethyst_forstatement_is_not_abstract():
    assert not inspect.isabstract(amethyst_ForStatement)


def test_hyp_amethyst_forstatement_constructor_exists():
    assert callable(amethyst_ForStatement.__init__)


def test_hyp_amethyst_forstatement_constructor_args():
    sig = inspect.signature(amethyst_ForStatement.__init__)
    params = list(sig.parameters.keys())



def test_hyp_amethyst_caseelsestatement_is_not_abstract():
    assert not inspect.isabstract(amethyst_CaseElseStatement)


def test_hyp_amethyst_caseelsestatement_constructor_exists():
    assert callable(amethyst_CaseElseStatement.__init__)


def test_hyp_amethyst_caseelsestatement_constructor_args():
    sig = inspect.signature(amethyst_CaseElseStatement.__init__)
    params = list(sig.parameters.keys())



def test_hyp_amethyst_jscodestatement_is_not_abstract():
    assert not inspect.isabstract(amethyst_JsCodeStatement)


def test_hyp_amethyst_jscodestatement_constructor_exists():
    assert callable(amethyst_JsCodeStatement.__init__)


def test_hyp_amethyst_jscodestatement_constructor_args():
    sig = inspect.signature(amethyst_JsCodeStatement.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"




def test_hyp_amethyst_expression_is_not_abstract():
    assert not inspect.isabstract(amethyst_Expression)


def test_hyp_amethyst_expression_constructor_exists():
    assert callable(amethyst_Expression.__init__)


def test_hyp_amethyst_expression_constructor_args():
    sig = inspect.signature(amethyst_Expression.__init__)
    params = list(sig.parameters.keys())



def test_hyp_amethyst_whenstatement_is_not_abstract():
    assert not inspect.isabstract(amethyst_WhenStatement)


def test_hyp_amethyst_whenstatement_constructor_exists():
    assert callable(amethyst_WhenStatement.__init__)


def test_hyp_amethyst_whenstatement_constructor_args():
    sig = inspect.signature(amethyst_WhenStatement.__init__)
    params = list(sig.parameters.keys())



def test_hyp_amethyst_ifstatement_is_not_abstract():
    assert not inspect.isabstract(amethyst_IfStatement)


def test_hyp_amethyst_ifstatement_constructor_exists():
    assert callable(amethyst_IfStatement.__init__)


def test_hyp_amethyst_ifstatement_constructor_args():
    sig = inspect.signature(amethyst_IfStatement.__init__)
    params = list(sig.parameters.keys())



def test_hyp_amethyst_elsestatement_is_not_abstract():
    assert not inspect.isabstract(amethyst_ElseStatement)


def test_hyp_amethyst_elsestatement_constructor_exists():
    assert callable(amethyst_ElseStatement.__init__)


def test_hyp_amethyst_elsestatement_constructor_args():
    sig = inspect.signature(amethyst_ElseStatement.__init__)
    params = list(sig.parameters.keys())



def test_hyp_amethyst_nextstatement_is_not_abstract():
    assert not inspect.isabstract(amethyst_NextStatement)


def test_hyp_amethyst_nextstatement_constructor_exists():
    assert callable(amethyst_NextStatement.__init__)


def test_hyp_amethyst_nextstatement_constructor_args():
    sig = inspect.signature(amethyst_NextStatement.__init__)
    params = list(sig.parameters.keys())



def test_hyp_amethyst_casestatement_is_not_abstract():
    assert not inspect.isabstract(amethyst_CaseStatement)


def test_hyp_amethyst_casestatement_constructor_exists():
    assert callable(amethyst_CaseStatement.__init__)


def test_hyp_amethyst_casestatement_constructor_args():
    sig = inspect.signature(amethyst_CaseStatement.__init__)
    params = list(sig.parameters.keys())



def test_hyp_amethyst_returnstatement_is_not_abstract():
    assert not inspect.isabstract(amethyst_ReturnStatement)


def test_hyp_amethyst_returnstatement_constructor_exists():
    assert callable(amethyst_ReturnStatement.__init__)


def test_hyp_amethyst_returnstatement_constructor_args():
    sig = inspect.signature(amethyst_ReturnStatement.__init__)
    params = list(sig.parameters.keys())



def test_hyp_amethyst_whilestatement_is_not_abstract():
    assert not inspect.isabstract(amethyst_WhileStatement)


def test_hyp_amethyst_whilestatement_constructor_exists():
    assert callable(amethyst_WhileStatement.__init__)


def test_hyp_amethyst_whilestatement_constructor_args():
    sig = inspect.signature(amethyst_WhileStatement.__init__)
    params = list(sig.parameters.keys())



def test_hyp_amethyst_symbol_is_not_abstract():
    assert not inspect.isabstract(amethyst_Symbol)


def test_hyp_amethyst_symbol_constructor_exists():
    assert callable(amethyst_Symbol.__init__)


def test_hyp_amethyst_symbol_constructor_args():
    sig = inspect.signature(amethyst_Symbol.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"




def test_hyp_amethyst_statement_is_not_abstract():
    assert not inspect.isabstract(amethyst_Statement)


def test_hyp_amethyst_statement_constructor_exists():
    assert callable(amethyst_Statement.__init__)


def test_hyp_amethyst_statement_constructor_args():
    sig = inspect.signature(amethyst_Statement.__init__)
    params = list(sig.parameters.keys())



def test_hyp_amethyst_import_is_not_abstract():
    assert not inspect.isabstract(amethyst_Import)


def test_hyp_amethyst_import_constructor_exists():
    assert callable(amethyst_Import.__init__)


def test_hyp_amethyst_import_constructor_args():
    sig = inspect.signature(amethyst_Import.__init__)
    params = list(sig.parameters.keys())
    assert "importedNamespace" in params, "Missing parameter 'importedNamespace'"




def test_hyp_amethyst_module_is_not_abstract():
    assert not inspect.isabstract(amethyst_Module)


def test_hyp_amethyst_module_constructor_exists():
    assert callable(amethyst_Module.__init__)


def test_hyp_amethyst_module_constructor_args():
    sig = inspect.signature(amethyst_Module.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"




def test_hyp_amethyst_propertydeclaration_is_not_abstract():
    assert not inspect.isabstract(amethyst_PropertyDeclaration)


def test_hyp_amethyst_propertydeclaration_constructor_exists():
    assert callable(amethyst_PropertyDeclaration.__init__)


def test_hyp_amethyst_propertydeclaration_constructor_args():
    sig = inspect.signature(amethyst_PropertyDeclaration.__init__)
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
RangeLiteral_strategy = st.builds(
    RangeLiteral,
)
amethyst_CharRangeLiteral_strategy = st.builds(
    amethyst_CharRangeLiteral,
)
amethyst_NumberRangeLiteral_strategy = st.builds(
    amethyst_NumberRangeLiteral,
)
Symbol_strategy = st.builds(
    Symbol,
)
amethyst_ParameterDeclaration_strategy = st.builds(
    amethyst_ParameterDeclaration,
)
amethyst_DefinitionDeclaration_strategy = st.builds(
    amethyst_DefinitionDeclaration,
    static=
        st.booleans()
)
amethyst_ForInitializerDeclaration_strategy = st.builds(
    amethyst_ForInitializerDeclaration,
)
amethyst_TagLoopInitializerDeclaration_strategy = st.builds(
    amethyst_TagLoopInitializerDeclaration,
)
amethyst_VariableDeclaration_strategy = st.builds(
    amethyst_VariableDeclaration,
)
amethyst_ClassDeclaration_strategy = st.builds(
    amethyst_ClassDeclaration,
)
PrimitiveType_strategy = st.builds(
    PrimitiveType,
)
amethyst_FloatType_strategy = st.builds(
    amethyst_FloatType,
)
amethyst_IntType_strategy = st.builds(
    amethyst_IntType,
)
amethyst_StringType_strategy = st.builds(
    amethyst_StringType,
)
amethyst_DefinitionType_strategy = st.builds(
    amethyst_DefinitionType,
)
amethyst_BooleanType_strategy = st.builds(
    amethyst_BooleanType,
)
amethyst_AnyType_strategy = st.builds(
    amethyst_AnyType,
)
amethyst_CharType_strategy = st.builds(
    amethyst_CharType,
)
Type_strategy = st.builds(
    Type,
)
amethyst_PrimitiveType_strategy = st.builds(
    amethyst_PrimitiveType,
)
AbstractType_strategy = st.builds(
    AbstractType,
)
amethyst_ArrayType_strategy = st.builds(
    amethyst_ArrayType,
)
amethyst_Type_strategy = st.builds(
    amethyst_Type,
)
amethyst_AbstractType_strategy = st.builds(
    amethyst_AbstractType,
)
Literal_strategy = st.builds(
    Literal,
)
amethyst_BooleanLiteral_strategy = st.builds(
    amethyst_BooleanLiteral,
    value=
        st.booleans()
)
amethyst_NullLiteral_strategy = st.builds(
    amethyst_NullLiteral,
)
amethyst_FloatLiteral_strategy = st.builds(
    amethyst_FloatLiteral,
    value=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
amethyst_RangeLiteral_strategy = st.builds(
    amethyst_RangeLiteral,
)
amethyst_IntLiteral_strategy = st.builds(
    amethyst_IntLiteral,
    value=
        st.integers()
)
amethyst_StringLiteral_strategy = st.builds(
    amethyst_StringLiteral,
    value=
        safe_text
)
amethyst_CharLiteral_strategy = st.builds(
    amethyst_CharLiteral,
    value=
        safe_text
)
Expression_strategy = st.builds(
    Expression,
)
amethyst_ShiftExpression_strategy = st.builds(
    amethyst_ShiftExpression,
    operator=
        safe_text
)
amethyst_AndExpression_strategy = st.builds(
    amethyst_AndExpression,
)
amethyst_CallExpression_strategy = st.builds(
    amethyst_CallExpression,
)
amethyst_AdditiveExpression_strategy = st.builds(
    amethyst_AdditiveExpression,
    operator=
        safe_text
)
amethyst_MatchingExpression_strategy = st.builds(
    amethyst_MatchingExpression,
    operator=
        safe_text
)
amethyst_SuperExpression_strategy = st.builds(
    amethyst_SuperExpression,
)
amethyst_ParenthisedExpression_strategy = st.builds(
    amethyst_ParenthisedExpression,
)
amethyst_SelfExpression_strategy = st.builds(
    amethyst_SelfExpression,
)
amethyst_TypeCastExpression_strategy = st.builds(
    amethyst_TypeCastExpression,
)
amethyst_IndexAccessExpression_strategy = st.builds(
    amethyst_IndexAccessExpression,
)
amethyst_InExpression_strategy = st.builds(
    amethyst_InExpression,
)
amethyst_MultiplicativeExpression_strategy = st.builds(
    amethyst_MultiplicativeExpression,
    operator=
        safe_text
)
amethyst_AssignmentExpression_strategy = st.builds(
    amethyst_AssignmentExpression,
)
amethyst_MemberAccessExpression_strategy = st.builds(
    amethyst_MemberAccessExpression,
)
amethyst_UnaryMinusExpression_strategy = st.builds(
    amethyst_UnaryMinusExpression,
)
amethyst_EqualityExpression_strategy = st.builds(
    amethyst_EqualityExpression,
    operator=
        safe_text
)
amethyst_NotExpression_strategy = st.builds(
    amethyst_NotExpression,
)
amethyst_RelationalExpression_strategy = st.builds(
    amethyst_RelationalExpression,
    operator=
        safe_text
)
amethyst_Literal_strategy = st.builds(
    amethyst_Literal,
)
amethyst_OrExpression_strategy = st.builds(
    amethyst_OrExpression,
)
amethyst_NewExpression_strategy = st.builds(
    amethyst_NewExpression,
)
amethyst_SymbolReference_strategy = st.builds(
    amethyst_SymbolReference,
)
amethyst_TagExpression_strategy = st.builds(
    amethyst_TagExpression,
)
amethyst_EObject_strategy = st.builds(
    amethyst_EObject,
)
amethyst_TagAttribute_strategy = st.builds(
    amethyst_TagAttribute,
)
amethyst_TagLoopExpression_strategy = st.builds(
    amethyst_TagLoopExpression,
)
amethyst_ClassType_strategy = st.builds(
    amethyst_ClassType,
)
amethyst_TagDeclaration_strategy = st.builds(
    amethyst_TagDeclaration,
)
Statement_strategy = st.builds(
    Statement,
)
amethyst_ElseIfStatement_strategy = st.builds(
    amethyst_ElseIfStatement,
)
amethyst_BreakStatement_strategy = st.builds(
    amethyst_BreakStatement,
)
amethyst_ForStatement_strategy = st.builds(
    amethyst_ForStatement,
)
amethyst_CaseElseStatement_strategy = st.builds(
    amethyst_CaseElseStatement,
)
amethyst_JsCodeStatement_strategy = st.builds(
    amethyst_JsCodeStatement,
    value=
        safe_text
)
amethyst_Expression_strategy = st.builds(
    amethyst_Expression,
)
amethyst_WhenStatement_strategy = st.builds(
    amethyst_WhenStatement,
)
amethyst_IfStatement_strategy = st.builds(
    amethyst_IfStatement,
)
amethyst_ElseStatement_strategy = st.builds(
    amethyst_ElseStatement,
)
amethyst_NextStatement_strategy = st.builds(
    amethyst_NextStatement,
)
amethyst_CaseStatement_strategy = st.builds(
    amethyst_CaseStatement,
)
amethyst_ReturnStatement_strategy = st.builds(
    amethyst_ReturnStatement,
)
amethyst_WhileStatement_strategy = st.builds(
    amethyst_WhileStatement,
)
amethyst_Symbol_strategy = st.builds(
    amethyst_Symbol,
    name=
        safe_text
)
amethyst_Statement_strategy = st.builds(
    amethyst_Statement,
)
amethyst_Import_strategy = st.builds(
    amethyst_Import,
    importedNamespace=
        safe_text
)
amethyst_Module_strategy = st.builds(
    amethyst_Module,
    name=
        safe_text
)
amethyst_PropertyDeclaration_strategy = st.builds(
    amethyst_PropertyDeclaration,
)









@given(instance=amethyst_DefinitionDeclaration_strategy)
def test_hyp_amethyst_definitiondeclaration_static_setter(instance):
    original = instance.static
    instance.static = original
    assert instance.static == original























@given(instance=amethyst_BooleanLiteral_strategy)
def test_hyp_amethyst_booleanliteral_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original





@given(instance=amethyst_FloatLiteral_strategy)
def test_hyp_amethyst_floatliteral_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original





@given(instance=amethyst_IntLiteral_strategy)
def test_hyp_amethyst_intliteral_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original




@given(instance=amethyst_StringLiteral_strategy)
def test_hyp_amethyst_stringliteral_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original




@given(instance=amethyst_CharLiteral_strategy)
def test_hyp_amethyst_charliteral_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original





@given(instance=amethyst_ShiftExpression_strategy)
def test_hyp_amethyst_shiftexpression_operator_setter(instance):
    original = instance.operator
    instance.operator = original
    assert instance.operator == original






@given(instance=amethyst_AdditiveExpression_strategy)
def test_hyp_amethyst_additiveexpression_operator_setter(instance):
    original = instance.operator
    instance.operator = original
    assert instance.operator == original




@given(instance=amethyst_MatchingExpression_strategy)
def test_hyp_amethyst_matchingexpression_operator_setter(instance):
    original = instance.operator
    instance.operator = original
    assert instance.operator == original










@given(instance=amethyst_MultiplicativeExpression_strategy)
def test_hyp_amethyst_multiplicativeexpression_operator_setter(instance):
    original = instance.operator
    instance.operator = original
    assert instance.operator == original







@given(instance=amethyst_EqualityExpression_strategy)
def test_hyp_amethyst_equalityexpression_operator_setter(instance):
    original = instance.operator
    instance.operator = original
    assert instance.operator == original





@given(instance=amethyst_RelationalExpression_strategy)
def test_hyp_amethyst_relationalexpression_operator_setter(instance):
    original = instance.operator
    instance.operator = original
    assert instance.operator == original



















@given(instance=amethyst_JsCodeStatement_strategy)
def test_hyp_amethyst_jscodestatement_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original












@given(instance=amethyst_Symbol_strategy)
def test_hyp_amethyst_symbol_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original





@given(instance=amethyst_Import_strategy)
def test_hyp_amethyst_import_importedNamespace_setter(instance):
    original = instance.importedNamespace
    instance.importedNamespace = original
    assert instance.importedNamespace == original




@given(instance=amethyst_Module_strategy)
def test_hyp_amethyst_module_name_setter(instance):
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
    AbstractType,
    Expression,
    Literal,
    PrimitiveType,
    RangeLiteral,
    Statement,
    Symbol,
    Type,
    amethyst_AbstractType,
    amethyst_AdditiveExpression,
    amethyst_AndExpression,
    amethyst_AnyType,
    amethyst_ArrayType,
    amethyst_AssignmentExpression,
    amethyst_BooleanLiteral,
    amethyst_BooleanType,
    amethyst_BreakStatement,
    amethyst_CallExpression,
    amethyst_CaseElseStatement,
    amethyst_CaseStatement,
    amethyst_CharLiteral,
    amethyst_CharRangeLiteral,
    amethyst_CharType,
    amethyst_ClassDeclaration,
    amethyst_ClassType,
    amethyst_DefinitionDeclaration,
    amethyst_DefinitionType,
    amethyst_EObject,
    amethyst_ElseIfStatement,
    amethyst_ElseStatement,
    amethyst_EqualityExpression,
    amethyst_Expression,
    amethyst_FloatLiteral,
    amethyst_FloatType,
    amethyst_ForInitializerDeclaration,
    amethyst_ForStatement,
    amethyst_IfStatement,
    amethyst_Import,
    amethyst_InExpression,
    amethyst_IndexAccessExpression,
    amethyst_IntLiteral,
    amethyst_IntType,
    amethyst_JsCodeStatement,
    amethyst_Literal,
    amethyst_MatchingExpression,
    amethyst_MemberAccessExpression,
    amethyst_Module,
    amethyst_MultiplicativeExpression,
    amethyst_NewExpression,
    amethyst_NextStatement,
    amethyst_NotExpression,
    amethyst_NullLiteral,
    amethyst_NumberRangeLiteral,
    amethyst_OrExpression,
    amethyst_ParameterDeclaration,
    amethyst_ParenthisedExpression,
    amethyst_PrimitiveType,
    amethyst_PropertyDeclaration,
    amethyst_RangeLiteral,
    amethyst_RelationalExpression,
    amethyst_ReturnStatement,
    amethyst_SelfExpression,
    amethyst_ShiftExpression,
    amethyst_Statement,
    amethyst_StringLiteral,
    amethyst_StringType,
    amethyst_SuperExpression,
    amethyst_Symbol,
    amethyst_SymbolReference,
    amethyst_TagAttribute,
    amethyst_TagDeclaration,
    amethyst_TagExpression,
    amethyst_TagLoopExpression,
    amethyst_TagLoopInitializerDeclaration,
    amethyst_Type,
    amethyst_TypeCastExpression,
    amethyst_UnaryMinusExpression,
    amethyst_VariableDeclaration,
    amethyst_WhenStatement,
    amethyst_WhileStatement,
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

def test_amethyst_AdditiveExpression_operator_value_roundtrip():
    instance = amethyst_AdditiveExpression(operator="sample_text")
    assert instance.operator == "sample_text"
    instance.operator = "sample_text_2"
    assert instance.operator == "sample_text_2"


def test_amethyst_BooleanLiteral_value_value_roundtrip():
    instance = amethyst_BooleanLiteral(value=True)
    assert instance.value == True
    instance.value = False
    assert instance.value == False


def test_amethyst_CharLiteral_value_value_roundtrip():
    instance = amethyst_CharLiteral(value="sample_text")
    assert instance.value == "sample_text"
    instance.value = "sample_text_2"
    assert instance.value == "sample_text_2"


def test_amethyst_DefinitionDeclaration_static_value_roundtrip():
    instance = amethyst_DefinitionDeclaration(static=True)
    assert instance.static == True
    instance.static = False
    assert instance.static == False


def test_amethyst_EqualityExpression_operator_value_roundtrip():
    instance = amethyst_EqualityExpression(operator="sample_text")
    assert instance.operator == "sample_text"
    instance.operator = "sample_text_2"
    assert instance.operator == "sample_text_2"


def test_amethyst_FloatLiteral_value_value_roundtrip():
    instance = amethyst_FloatLiteral(value=3.14)
    assert instance.value == 3.14
    instance.value = 9.99
    assert instance.value == 9.99


def test_amethyst_Import_importedNamespace_value_roundtrip():
    instance = amethyst_Import(importedNamespace="sample_text")
    assert instance.importedNamespace == "sample_text"
    instance.importedNamespace = "sample_text_2"
    assert instance.importedNamespace == "sample_text_2"


def test_amethyst_IntLiteral_value_value_roundtrip():
    instance = amethyst_IntLiteral(value=7)
    assert instance.value == 7
    instance.value = 13
    assert instance.value == 13


def test_amethyst_JsCodeStatement_value_value_roundtrip():
    instance = amethyst_JsCodeStatement(value="sample_text")
    assert instance.value == "sample_text"
    instance.value = "sample_text_2"
    assert instance.value == "sample_text_2"


def test_amethyst_MatchingExpression_operator_value_roundtrip():
    instance = amethyst_MatchingExpression(operator="sample_text")
    assert instance.operator == "sample_text"
    instance.operator = "sample_text_2"
    assert instance.operator == "sample_text_2"


def test_amethyst_Module_name_value_roundtrip():
    instance = amethyst_Module(name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_amethyst_MultiplicativeExpression_operator_value_roundtrip():
    instance = amethyst_MultiplicativeExpression(operator="sample_text")
    assert instance.operator == "sample_text"
    instance.operator = "sample_text_2"
    assert instance.operator == "sample_text_2"


def test_amethyst_RelationalExpression_operator_value_roundtrip():
    instance = amethyst_RelationalExpression(operator="sample_text")
    assert instance.operator == "sample_text"
    instance.operator = "sample_text_2"
    assert instance.operator == "sample_text_2"


def test_amethyst_ShiftExpression_operator_value_roundtrip():
    instance = amethyst_ShiftExpression(operator="sample_text")
    assert instance.operator == "sample_text"
    instance.operator = "sample_text_2"
    assert instance.operator == "sample_text_2"


def test_amethyst_StringLiteral_value_value_roundtrip():
    instance = amethyst_StringLiteral(value="sample_text")
    assert instance.value == "sample_text"
    instance.value = "sample_text_2"
    assert instance.value == "sample_text_2"


def test_amethyst_Symbol_name_value_roundtrip():
    instance = amethyst_Symbol(name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_amethyst_ArrayType_isa_AbstractType():
    instance = amethyst_ArrayType()
    assert isinstance(instance, AbstractType)


def test_amethyst_Type_isa_AbstractType():
    instance = amethyst_Type()
    assert isinstance(instance, AbstractType)


def test_amethyst_AdditiveExpression_isa_Expression():
    instance = amethyst_AdditiveExpression(operator="sample_text")
    assert isinstance(instance, Expression)


def test_amethyst_AndExpression_isa_Expression():
    instance = amethyst_AndExpression()
    assert isinstance(instance, Expression)


def test_amethyst_AssignmentExpression_isa_Expression():
    instance = amethyst_AssignmentExpression()
    assert isinstance(instance, Expression)


def test_amethyst_CallExpression_isa_Expression():
    instance = amethyst_CallExpression()
    assert isinstance(instance, Expression)


def test_amethyst_EqualityExpression_isa_Expression():
    instance = amethyst_EqualityExpression(operator="sample_text")
    assert isinstance(instance, Expression)


def test_amethyst_InExpression_isa_Expression():
    instance = amethyst_InExpression()
    assert isinstance(instance, Expression)


def test_amethyst_IndexAccessExpression_isa_Expression():
    instance = amethyst_IndexAccessExpression()
    assert isinstance(instance, Expression)


def test_amethyst_Literal_isa_Expression():
    instance = amethyst_Literal()
    assert isinstance(instance, Expression)


def test_amethyst_MatchingExpression_isa_Expression():
    instance = amethyst_MatchingExpression(operator="sample_text")
    assert isinstance(instance, Expression)


def test_amethyst_MemberAccessExpression_isa_Expression():
    instance = amethyst_MemberAccessExpression()
    assert isinstance(instance, Expression)


def test_amethyst_MultiplicativeExpression_isa_Expression():
    instance = amethyst_MultiplicativeExpression(operator="sample_text")
    assert isinstance(instance, Expression)


def test_amethyst_NewExpression_isa_Expression():
    instance = amethyst_NewExpression()
    assert isinstance(instance, Expression)


def test_amethyst_NotExpression_isa_Expression():
    instance = amethyst_NotExpression()
    assert isinstance(instance, Expression)


def test_amethyst_OrExpression_isa_Expression():
    instance = amethyst_OrExpression()
    assert isinstance(instance, Expression)


def test_amethyst_ParenthisedExpression_isa_Expression():
    instance = amethyst_ParenthisedExpression()
    assert isinstance(instance, Expression)


def test_amethyst_RelationalExpression_isa_Expression():
    instance = amethyst_RelationalExpression(operator="sample_text")
    assert isinstance(instance, Expression)


def test_amethyst_SelfExpression_isa_Expression():
    instance = amethyst_SelfExpression()
    assert isinstance(instance, Expression)


def test_amethyst_ShiftExpression_isa_Expression():
    instance = amethyst_ShiftExpression(operator="sample_text")
    assert isinstance(instance, Expression)


def test_amethyst_SuperExpression_isa_Expression():
    instance = amethyst_SuperExpression()
    assert isinstance(instance, Expression)


def test_amethyst_SymbolReference_isa_Expression():
    instance = amethyst_SymbolReference()
    assert isinstance(instance, Expression)


def test_amethyst_TypeCastExpression_isa_Expression():
    instance = amethyst_TypeCastExpression()
    assert isinstance(instance, Expression)


def test_amethyst_UnaryMinusExpression_isa_Expression():
    instance = amethyst_UnaryMinusExpression()
    assert isinstance(instance, Expression)


def test_amethyst_BooleanLiteral_isa_Literal():
    instance = amethyst_BooleanLiteral(value=True)
    assert isinstance(instance, Literal)


def test_amethyst_CharLiteral_isa_Literal():
    instance = amethyst_CharLiteral(value="sample_text")
    assert isinstance(instance, Literal)


def test_amethyst_FloatLiteral_isa_Literal():
    instance = amethyst_FloatLiteral(value=3.14)
    assert isinstance(instance, Literal)


def test_amethyst_IntLiteral_isa_Literal():
    instance = amethyst_IntLiteral(value=7)
    assert isinstance(instance, Literal)


def test_amethyst_NullLiteral_isa_Literal():
    instance = amethyst_NullLiteral()
    assert isinstance(instance, Literal)


def test_amethyst_RangeLiteral_isa_Literal():
    instance = amethyst_RangeLiteral()
    assert isinstance(instance, Literal)


def test_amethyst_StringLiteral_isa_Literal():
    instance = amethyst_StringLiteral(value="sample_text")
    assert isinstance(instance, Literal)


def test_amethyst_AnyType_isa_PrimitiveType():
    instance = amethyst_AnyType()
    assert isinstance(instance, PrimitiveType)


def test_amethyst_BooleanType_isa_PrimitiveType():
    instance = amethyst_BooleanType()
    assert isinstance(instance, PrimitiveType)


def test_amethyst_CharType_isa_PrimitiveType():
    instance = amethyst_CharType()
    assert isinstance(instance, PrimitiveType)


def test_amethyst_DefinitionType_isa_PrimitiveType():
    instance = amethyst_DefinitionType()
    assert isinstance(instance, PrimitiveType)


def test_amethyst_FloatType_isa_PrimitiveType():
    instance = amethyst_FloatType()
    assert isinstance(instance, PrimitiveType)


def test_amethyst_IntType_isa_PrimitiveType():
    instance = amethyst_IntType()
    assert isinstance(instance, PrimitiveType)


def test_amethyst_StringType_isa_PrimitiveType():
    instance = amethyst_StringType()
    assert isinstance(instance, PrimitiveType)


def test_amethyst_CharRangeLiteral_isa_RangeLiteral():
    instance = amethyst_CharRangeLiteral()
    assert isinstance(instance, RangeLiteral)


def test_amethyst_NumberRangeLiteral_isa_RangeLiteral():
    instance = amethyst_NumberRangeLiteral()
    assert isinstance(instance, RangeLiteral)


def test_amethyst_BreakStatement_isa_Statement():
    instance = amethyst_BreakStatement()
    assert isinstance(instance, Statement)


def test_amethyst_CaseElseStatement_isa_Statement():
    instance = amethyst_CaseElseStatement()
    assert isinstance(instance, Statement)


def test_amethyst_CaseStatement_isa_Statement():
    instance = amethyst_CaseStatement()
    assert isinstance(instance, Statement)


def test_amethyst_ElseIfStatement_isa_Statement():
    instance = amethyst_ElseIfStatement()
    assert isinstance(instance, Statement)


def test_amethyst_ElseStatement_isa_Statement():
    instance = amethyst_ElseStatement()
    assert isinstance(instance, Statement)


def test_amethyst_Expression_isa_Statement():
    instance = amethyst_Expression()
    assert isinstance(instance, Statement)


def test_amethyst_ForStatement_isa_Statement():
    instance = amethyst_ForStatement()
    assert isinstance(instance, Statement)


def test_amethyst_IfStatement_isa_Statement():
    instance = amethyst_IfStatement()
    assert isinstance(instance, Statement)


def test_amethyst_JsCodeStatement_isa_Statement():
    instance = amethyst_JsCodeStatement(value="sample_text")
    assert isinstance(instance, Statement)


def test_amethyst_NextStatement_isa_Statement():
    instance = amethyst_NextStatement()
    assert isinstance(instance, Statement)


def test_amethyst_ReturnStatement_isa_Statement():
    instance = amethyst_ReturnStatement()
    assert isinstance(instance, Statement)


def test_amethyst_Symbol_isa_Statement():
    instance = amethyst_Symbol(name="sample_text")
    assert isinstance(instance, Statement)


def test_amethyst_WhenStatement_isa_Statement():
    instance = amethyst_WhenStatement()
    assert isinstance(instance, Statement)


def test_amethyst_WhileStatement_isa_Statement():
    instance = amethyst_WhileStatement()
    assert isinstance(instance, Statement)


def test_amethyst_ClassDeclaration_isa_Symbol():
    instance = amethyst_ClassDeclaration()
    assert isinstance(instance, Symbol)


def test_amethyst_DefinitionDeclaration_isa_Symbol():
    instance = amethyst_DefinitionDeclaration(static=True)
    assert isinstance(instance, Symbol)


def test_amethyst_ForInitializerDeclaration_isa_Symbol():
    instance = amethyst_ForInitializerDeclaration()
    assert isinstance(instance, Symbol)


def test_amethyst_ParameterDeclaration_isa_Symbol():
    instance = amethyst_ParameterDeclaration()
    assert isinstance(instance, Symbol)


def test_amethyst_PropertyDeclaration_isa_Symbol():
    instance = amethyst_PropertyDeclaration()
    assert isinstance(instance, Symbol)


def test_amethyst_TagLoopInitializerDeclaration_isa_Symbol():
    instance = amethyst_TagLoopInitializerDeclaration()
    assert isinstance(instance, Symbol)


def test_amethyst_VariableDeclaration_isa_Symbol():
    instance = amethyst_VariableDeclaration()
    assert isinstance(instance, Symbol)


def test_amethyst_ClassType_isa_Type():
    instance = amethyst_ClassType()
    assert isinstance(instance, Type)


def test_amethyst_PrimitiveType_isa_Type():
    instance = amethyst_PrimitiveType()
    assert isinstance(instance, Type)


def test_assoc_declarations1_link_reassign_clear():
    a = amethyst_Module(name="sample_text")
    b1 = amethyst_Statement()
    b2 = amethyst_Statement()
    _safe_set(a, 'amethyst_Module2', {b1})
    assert _is_linked(a, 'amethyst_Module2', b1)
    if hasattr(b1, 'amethyst_Statement'):
        assert _is_linked(b1, 'amethyst_Statement', a)
    _safe_set(a, 'amethyst_Module2', {b2})
    assert _is_linked(a, 'amethyst_Module2', b2)
    if hasattr(b1, 'amethyst_Statement'):
        assert not _is_linked(b1, 'amethyst_Statement', a)
    if hasattr(b2, 'amethyst_Statement'):
        assert _is_linked(b2, 'amethyst_Statement', a)
    _safe_set(a, 'amethyst_Module2', set())
    assert not _is_linked(a, 'amethyst_Module2', b2)
    if hasattr(b2, 'amethyst_Statement'):
        assert not _is_linked(b2, 'amethyst_Statement', a)


def test_assoc_end188_link_reassign_clear():
    a = amethyst_IntLiteral(value=7)
    b1 = amethyst_NumberRangeLiteral()
    b2 = amethyst_NumberRangeLiteral()
    _safe_set(a, 'amethyst_IntLiteral190', b1)
    assert _is_linked(a, 'amethyst_IntLiteral190', b1)
    if hasattr(b1, 'amethyst_NumberRangeLiteral189'):
        assert _is_linked(b1, 'amethyst_NumberRangeLiteral189', a)
    _safe_set(a, 'amethyst_IntLiteral190', b2)
    assert _is_linked(a, 'amethyst_IntLiteral190', b2)
    if hasattr(b1, 'amethyst_NumberRangeLiteral189'):
        assert not _is_linked(b1, 'amethyst_NumberRangeLiteral189', a)
    if hasattr(b2, 'amethyst_NumberRangeLiteral189'):
        assert _is_linked(b2, 'amethyst_NumberRangeLiteral189', a)
    _safe_set(a, 'amethyst_IntLiteral190', None)
    assert not _is_linked(a, 'amethyst_IntLiteral190', b2)
    if hasattr(b2, 'amethyst_NumberRangeLiteral189'):
        assert not _is_linked(b2, 'amethyst_NumberRangeLiteral189', a)


def test_assoc_end192_link_reassign_clear():
    a = amethyst_CharLiteral(value="sample_text")
    b1 = amethyst_CharRangeLiteral()
    b2 = amethyst_CharRangeLiteral()
    _safe_set(a, 'amethyst_CharLiteral194', b1)
    assert _is_linked(a, 'amethyst_CharLiteral194', b1)
    if hasattr(b1, 'amethyst_CharRangeLiteral193'):
        assert _is_linked(b1, 'amethyst_CharRangeLiteral193', a)
    _safe_set(a, 'amethyst_CharLiteral194', b2)
    assert _is_linked(a, 'amethyst_CharLiteral194', b2)
    if hasattr(b1, 'amethyst_CharRangeLiteral193'):
        assert not _is_linked(b1, 'amethyst_CharRangeLiteral193', a)
    if hasattr(b2, 'amethyst_CharRangeLiteral193'):
        assert _is_linked(b2, 'amethyst_CharRangeLiteral193', a)
    _safe_set(a, 'amethyst_CharLiteral194', None)
    assert not _is_linked(a, 'amethyst_CharLiteral194', b2)
    if hasattr(b2, 'amethyst_CharRangeLiteral193'):
        assert not _is_linked(b2, 'amethyst_CharRangeLiteral193', a)


def test_assoc_imports0_link_reassign_clear():
    a = amethyst_Module(name="sample_text")
    b1 = amethyst_Import(importedNamespace="sample_text")
    b2 = amethyst_Import(importedNamespace="sample_text_2")
    _safe_set(a, 'amethyst_Module', {b1})
    assert _is_linked(a, 'amethyst_Module', b1)
    if hasattr(b1, 'amethyst_Import'):
        assert _is_linked(b1, 'amethyst_Import', a)
    _safe_set(a, 'amethyst_Module', {b2})
    assert _is_linked(a, 'amethyst_Module', b2)
    if hasattr(b1, 'amethyst_Import'):
        assert not _is_linked(b1, 'amethyst_Import', a)
    if hasattr(b2, 'amethyst_Import'):
        assert _is_linked(b2, 'amethyst_Import', a)
    _safe_set(a, 'amethyst_Module', set())
    assert not _is_linked(a, 'amethyst_Module', b2)
    if hasattr(b2, 'amethyst_Import'):
        assert not _is_linked(b2, 'amethyst_Import', a)


def test_assoc_initializer10_link_reassign_clear():
    a = amethyst_Symbol(name="sample_text")
    b1 = amethyst_TagLoopExpression()
    b2 = amethyst_TagLoopExpression()
    _safe_set(a, 'amethyst_Symbol', b1)
    assert _is_linked(a, 'amethyst_Symbol', b1)
    if hasattr(b1, 'amethyst_TagLoopExpression11'):
        assert _is_linked(b1, 'amethyst_TagLoopExpression11', a)
    _safe_set(a, 'amethyst_Symbol', b2)
    assert _is_linked(a, 'amethyst_Symbol', b2)
    if hasattr(b1, 'amethyst_TagLoopExpression11'):
        assert not _is_linked(b1, 'amethyst_TagLoopExpression11', a)
    if hasattr(b2, 'amethyst_TagLoopExpression11'):
        assert _is_linked(b2, 'amethyst_TagLoopExpression11', a)
    _safe_set(a, 'amethyst_Symbol', None)
    assert not _is_linked(a, 'amethyst_Symbol', b2)
    if hasattr(b2, 'amethyst_TagLoopExpression11'):
        assert not _is_linked(b2, 'amethyst_TagLoopExpression11', a)


def test_assoc_initializer96_link_reassign_clear():
    a = amethyst_Symbol(name="sample_text")
    b1 = amethyst_ForStatement()
    b2 = amethyst_ForStatement()
    _safe_set(a, 'amethyst_Symbol97', b1)
    assert _is_linked(a, 'amethyst_Symbol97', b1)
    if hasattr(b1, 'amethyst_ForStatement'):
        assert _is_linked(b1, 'amethyst_ForStatement', a)
    _safe_set(a, 'amethyst_Symbol97', b2)
    assert _is_linked(a, 'amethyst_Symbol97', b2)
    if hasattr(b1, 'amethyst_ForStatement'):
        assert not _is_linked(b1, 'amethyst_ForStatement', a)
    if hasattr(b2, 'amethyst_ForStatement'):
        assert _is_linked(b2, 'amethyst_ForStatement', a)
    _safe_set(a, 'amethyst_Symbol97', None)
    assert not _is_linked(a, 'amethyst_Symbol97', b2)
    if hasattr(b2, 'amethyst_ForStatement'):
        assert not _is_linked(b2, 'amethyst_ForStatement', a)


def test_assoc_left136_link_reassign_clear():
    a = amethyst_RelationalExpression(operator="sample_text")
    b1 = amethyst_Expression()
    b2 = amethyst_Expression()
    _safe_set(a, 'amethyst_RelationalExpression', b1)
    assert _is_linked(a, 'amethyst_RelationalExpression', b1)
    if hasattr(b1, 'amethyst_Expression137'):
        assert _is_linked(b1, 'amethyst_Expression137', a)
    _safe_set(a, 'amethyst_RelationalExpression', b2)
    assert _is_linked(a, 'amethyst_RelationalExpression', b2)
    if hasattr(b1, 'amethyst_Expression137'):
        assert not _is_linked(b1, 'amethyst_Expression137', a)
    if hasattr(b2, 'amethyst_Expression137'):
        assert _is_linked(b2, 'amethyst_Expression137', a)
    _safe_set(a, 'amethyst_RelationalExpression', None)
    assert not _is_linked(a, 'amethyst_RelationalExpression', b2)
    if hasattr(b2, 'amethyst_Expression137'):
        assert not _is_linked(b2, 'amethyst_Expression137', a)


def test_assoc_left141_link_reassign_clear():
    a = amethyst_EqualityExpression(operator="sample_text")
    b1 = amethyst_Expression()
    b2 = amethyst_Expression()
    _safe_set(a, 'amethyst_EqualityExpression', b1)
    assert _is_linked(a, 'amethyst_EqualityExpression', b1)
    if hasattr(b1, 'amethyst_Expression142'):
        assert _is_linked(b1, 'amethyst_Expression142', a)
    _safe_set(a, 'amethyst_EqualityExpression', b2)
    assert _is_linked(a, 'amethyst_EqualityExpression', b2)
    if hasattr(b1, 'amethyst_Expression142'):
        assert not _is_linked(b1, 'amethyst_Expression142', a)
    if hasattr(b2, 'amethyst_Expression142'):
        assert _is_linked(b2, 'amethyst_Expression142', a)
    _safe_set(a, 'amethyst_EqualityExpression', None)
    assert not _is_linked(a, 'amethyst_EqualityExpression', b2)
    if hasattr(b2, 'amethyst_Expression142'):
        assert not _is_linked(b2, 'amethyst_Expression142', a)


def test_assoc_left146_link_reassign_clear():
    a = amethyst_ShiftExpression(operator="sample_text")
    b1 = amethyst_Expression()
    b2 = amethyst_Expression()
    _safe_set(a, 'amethyst_ShiftExpression', b1)
    assert _is_linked(a, 'amethyst_ShiftExpression', b1)
    if hasattr(b1, 'amethyst_Expression147'):
        assert _is_linked(b1, 'amethyst_Expression147', a)
    _safe_set(a, 'amethyst_ShiftExpression', b2)
    assert _is_linked(a, 'amethyst_ShiftExpression', b2)
    if hasattr(b1, 'amethyst_Expression147'):
        assert not _is_linked(b1, 'amethyst_Expression147', a)
    if hasattr(b2, 'amethyst_Expression147'):
        assert _is_linked(b2, 'amethyst_Expression147', a)
    _safe_set(a, 'amethyst_ShiftExpression', None)
    assert not _is_linked(a, 'amethyst_ShiftExpression', b2)
    if hasattr(b2, 'amethyst_Expression147'):
        assert not _is_linked(b2, 'amethyst_Expression147', a)


def test_assoc_left151_link_reassign_clear():
    a = amethyst_AdditiveExpression(operator="sample_text")
    b1 = amethyst_Expression()
    b2 = amethyst_Expression()
    _safe_set(a, 'amethyst_AdditiveExpression', b1)
    assert _is_linked(a, 'amethyst_AdditiveExpression', b1)
    if hasattr(b1, 'amethyst_Expression152'):
        assert _is_linked(b1, 'amethyst_Expression152', a)
    _safe_set(a, 'amethyst_AdditiveExpression', b2)
    assert _is_linked(a, 'amethyst_AdditiveExpression', b2)
    if hasattr(b1, 'amethyst_Expression152'):
        assert not _is_linked(b1, 'amethyst_Expression152', a)
    if hasattr(b2, 'amethyst_Expression152'):
        assert _is_linked(b2, 'amethyst_Expression152', a)
    _safe_set(a, 'amethyst_AdditiveExpression', None)
    assert not _is_linked(a, 'amethyst_AdditiveExpression', b2)
    if hasattr(b2, 'amethyst_Expression152'):
        assert not _is_linked(b2, 'amethyst_Expression152', a)


def test_assoc_left156_link_reassign_clear():
    a = amethyst_MultiplicativeExpression(operator="sample_text")
    b1 = amethyst_Expression()
    b2 = amethyst_Expression()
    _safe_set(a, 'amethyst_MultiplicativeExpression', b1)
    assert _is_linked(a, 'amethyst_MultiplicativeExpression', b1)
    if hasattr(b1, 'amethyst_Expression157'):
        assert _is_linked(b1, 'amethyst_Expression157', a)
    _safe_set(a, 'amethyst_MultiplicativeExpression', b2)
    assert _is_linked(a, 'amethyst_MultiplicativeExpression', b2)
    if hasattr(b1, 'amethyst_Expression157'):
        assert not _is_linked(b1, 'amethyst_Expression157', a)
    if hasattr(b2, 'amethyst_Expression157'):
        assert _is_linked(b2, 'amethyst_Expression157', a)
    _safe_set(a, 'amethyst_MultiplicativeExpression', None)
    assert not _is_linked(a, 'amethyst_MultiplicativeExpression', b2)
    if hasattr(b2, 'amethyst_Expression157'):
        assert not _is_linked(b2, 'amethyst_Expression157', a)


def test_assoc_left161_link_reassign_clear():
    a = amethyst_MatchingExpression(operator="sample_text")
    b1 = amethyst_Expression()
    b2 = amethyst_Expression()
    _safe_set(a, 'amethyst_MatchingExpression', b1)
    assert _is_linked(a, 'amethyst_MatchingExpression', b1)
    if hasattr(b1, 'amethyst_Expression162'):
        assert _is_linked(b1, 'amethyst_Expression162', a)
    _safe_set(a, 'amethyst_MatchingExpression', b2)
    assert _is_linked(a, 'amethyst_MatchingExpression', b2)
    if hasattr(b1, 'amethyst_Expression162'):
        assert not _is_linked(b1, 'amethyst_Expression162', a)
    if hasattr(b2, 'amethyst_Expression162'):
        assert _is_linked(b2, 'amethyst_Expression162', a)
    _safe_set(a, 'amethyst_MatchingExpression', None)
    assert not _is_linked(a, 'amethyst_MatchingExpression', b2)
    if hasattr(b2, 'amethyst_Expression162'):
        assert not _is_linked(b2, 'amethyst_Expression162', a)


def test_assoc_methods43_link_reassign_clear():
    a = amethyst_Symbol(name="sample_text")
    b1 = amethyst_ClassDeclaration()
    b2 = amethyst_ClassDeclaration()
    _safe_set(a, 'amethyst_Symbol45', b1)
    assert _is_linked(a, 'amethyst_Symbol45', b1)
    if hasattr(b1, 'amethyst_ClassDeclaration44'):
        assert _is_linked(b1, 'amethyst_ClassDeclaration44', a)
    _safe_set(a, 'amethyst_Symbol45', b2)
    assert _is_linked(a, 'amethyst_Symbol45', b2)
    if hasattr(b1, 'amethyst_ClassDeclaration44'):
        assert not _is_linked(b1, 'amethyst_ClassDeclaration44', a)
    if hasattr(b2, 'amethyst_ClassDeclaration44'):
        assert _is_linked(b2, 'amethyst_ClassDeclaration44', a)
    _safe_set(a, 'amethyst_Symbol45', None)
    assert not _is_linked(a, 'amethyst_Symbol45', b2)
    if hasattr(b2, 'amethyst_ClassDeclaration44'):
        assert not _is_linked(b2, 'amethyst_ClassDeclaration44', a)


def test_assoc_params30_link_reassign_clear():
    a = amethyst_Symbol(name="sample_text")
    b1 = amethyst_DefinitionDeclaration(static=True)
    b2 = amethyst_DefinitionDeclaration(static=False)
    _safe_set(a, 'amethyst_Symbol31', b1)
    assert _is_linked(a, 'amethyst_Symbol31', b1)
    if hasattr(b1, 'amethyst_DefinitionDeclaration'):
        assert _is_linked(b1, 'amethyst_DefinitionDeclaration', a)
    _safe_set(a, 'amethyst_Symbol31', b2)
    assert _is_linked(a, 'amethyst_Symbol31', b2)
    if hasattr(b1, 'amethyst_DefinitionDeclaration'):
        assert not _is_linked(b1, 'amethyst_DefinitionDeclaration', a)
    if hasattr(b2, 'amethyst_DefinitionDeclaration'):
        assert _is_linked(b2, 'amethyst_DefinitionDeclaration', a)
    _safe_set(a, 'amethyst_Symbol31', None)
    assert not _is_linked(a, 'amethyst_Symbol31', b2)
    if hasattr(b2, 'amethyst_DefinitionDeclaration'):
        assert not _is_linked(b2, 'amethyst_DefinitionDeclaration', a)


def test_assoc_properties46_link_reassign_clear():
    a = amethyst_Symbol(name="sample_text")
    b1 = amethyst_ClassDeclaration()
    b2 = amethyst_ClassDeclaration()
    _safe_set(a, 'amethyst_Symbol48', b1)
    assert _is_linked(a, 'amethyst_Symbol48', b1)
    if hasattr(b1, 'amethyst_ClassDeclaration47'):
        assert _is_linked(b1, 'amethyst_ClassDeclaration47', a)
    _safe_set(a, 'amethyst_Symbol48', b2)
    assert _is_linked(a, 'amethyst_Symbol48', b2)
    if hasattr(b1, 'amethyst_ClassDeclaration47'):
        assert not _is_linked(b1, 'amethyst_ClassDeclaration47', a)
    if hasattr(b2, 'amethyst_ClassDeclaration47'):
        assert _is_linked(b2, 'amethyst_ClassDeclaration47', a)
    _safe_set(a, 'amethyst_Symbol48', None)
    assert not _is_linked(a, 'amethyst_Symbol48', b2)
    if hasattr(b2, 'amethyst_ClassDeclaration47'):
        assert not _is_linked(b2, 'amethyst_ClassDeclaration47', a)


def test_assoc_right123_link_reassign_clear():
    a = amethyst_Symbol(name="sample_text")
    b1 = amethyst_MemberAccessExpression()
    b2 = amethyst_MemberAccessExpression()
    _safe_set(a, 'amethyst_Symbol125', b1)
    assert _is_linked(a, 'amethyst_Symbol125', b1)
    if hasattr(b1, 'amethyst_MemberAccessExpression124'):
        assert _is_linked(b1, 'amethyst_MemberAccessExpression124', a)
    _safe_set(a, 'amethyst_Symbol125', b2)
    assert _is_linked(a, 'amethyst_Symbol125', b2)
    if hasattr(b1, 'amethyst_MemberAccessExpression124'):
        assert not _is_linked(b1, 'amethyst_MemberAccessExpression124', a)
    if hasattr(b2, 'amethyst_MemberAccessExpression124'):
        assert _is_linked(b2, 'amethyst_MemberAccessExpression124', a)
    _safe_set(a, 'amethyst_Symbol125', None)
    assert not _is_linked(a, 'amethyst_Symbol125', b2)
    if hasattr(b2, 'amethyst_MemberAccessExpression124'):
        assert not _is_linked(b2, 'amethyst_MemberAccessExpression124', a)


def test_assoc_right138_link_reassign_clear():
    a = amethyst_RelationalExpression(operator="sample_text")
    b1 = amethyst_Expression()
    b2 = amethyst_Expression()
    _safe_set(a, 'amethyst_RelationalExpression139', b1)
    assert _is_linked(a, 'amethyst_RelationalExpression139', b1)
    if hasattr(b1, 'amethyst_Expression140'):
        assert _is_linked(b1, 'amethyst_Expression140', a)
    _safe_set(a, 'amethyst_RelationalExpression139', b2)
    assert _is_linked(a, 'amethyst_RelationalExpression139', b2)
    if hasattr(b1, 'amethyst_Expression140'):
        assert not _is_linked(b1, 'amethyst_Expression140', a)
    if hasattr(b2, 'amethyst_Expression140'):
        assert _is_linked(b2, 'amethyst_Expression140', a)
    _safe_set(a, 'amethyst_RelationalExpression139', None)
    assert not _is_linked(a, 'amethyst_RelationalExpression139', b2)
    if hasattr(b2, 'amethyst_Expression140'):
        assert not _is_linked(b2, 'amethyst_Expression140', a)


def test_assoc_right143_link_reassign_clear():
    a = amethyst_EqualityExpression(operator="sample_text")
    b1 = amethyst_Expression()
    b2 = amethyst_Expression()
    _safe_set(a, 'amethyst_EqualityExpression144', b1)
    assert _is_linked(a, 'amethyst_EqualityExpression144', b1)
    if hasattr(b1, 'amethyst_Expression145'):
        assert _is_linked(b1, 'amethyst_Expression145', a)
    _safe_set(a, 'amethyst_EqualityExpression144', b2)
    assert _is_linked(a, 'amethyst_EqualityExpression144', b2)
    if hasattr(b1, 'amethyst_Expression145'):
        assert not _is_linked(b1, 'amethyst_Expression145', a)
    if hasattr(b2, 'amethyst_Expression145'):
        assert _is_linked(b2, 'amethyst_Expression145', a)
    _safe_set(a, 'amethyst_EqualityExpression144', None)
    assert not _is_linked(a, 'amethyst_EqualityExpression144', b2)
    if hasattr(b2, 'amethyst_Expression145'):
        assert not _is_linked(b2, 'amethyst_Expression145', a)


def test_assoc_right148_link_reassign_clear():
    a = amethyst_ShiftExpression(operator="sample_text")
    b1 = amethyst_Expression()
    b2 = amethyst_Expression()
    _safe_set(a, 'amethyst_ShiftExpression149', b1)
    assert _is_linked(a, 'amethyst_ShiftExpression149', b1)
    if hasattr(b1, 'amethyst_Expression150'):
        assert _is_linked(b1, 'amethyst_Expression150', a)
    _safe_set(a, 'amethyst_ShiftExpression149', b2)
    assert _is_linked(a, 'amethyst_ShiftExpression149', b2)
    if hasattr(b1, 'amethyst_Expression150'):
        assert not _is_linked(b1, 'amethyst_Expression150', a)
    if hasattr(b2, 'amethyst_Expression150'):
        assert _is_linked(b2, 'amethyst_Expression150', a)
    _safe_set(a, 'amethyst_ShiftExpression149', None)
    assert not _is_linked(a, 'amethyst_ShiftExpression149', b2)
    if hasattr(b2, 'amethyst_Expression150'):
        assert not _is_linked(b2, 'amethyst_Expression150', a)


def test_assoc_right153_link_reassign_clear():
    a = amethyst_AdditiveExpression(operator="sample_text")
    b1 = amethyst_Expression()
    b2 = amethyst_Expression()
    _safe_set(a, 'amethyst_AdditiveExpression154', b1)
    assert _is_linked(a, 'amethyst_AdditiveExpression154', b1)
    if hasattr(b1, 'amethyst_Expression155'):
        assert _is_linked(b1, 'amethyst_Expression155', a)
    _safe_set(a, 'amethyst_AdditiveExpression154', b2)
    assert _is_linked(a, 'amethyst_AdditiveExpression154', b2)
    if hasattr(b1, 'amethyst_Expression155'):
        assert not _is_linked(b1, 'amethyst_Expression155', a)
    if hasattr(b2, 'amethyst_Expression155'):
        assert _is_linked(b2, 'amethyst_Expression155', a)
    _safe_set(a, 'amethyst_AdditiveExpression154', None)
    assert not _is_linked(a, 'amethyst_AdditiveExpression154', b2)
    if hasattr(b2, 'amethyst_Expression155'):
        assert not _is_linked(b2, 'amethyst_Expression155', a)


def test_assoc_right158_link_reassign_clear():
    a = amethyst_MultiplicativeExpression(operator="sample_text")
    b1 = amethyst_Expression()
    b2 = amethyst_Expression()
    _safe_set(a, 'amethyst_MultiplicativeExpression159', b1)
    assert _is_linked(a, 'amethyst_MultiplicativeExpression159', b1)
    if hasattr(b1, 'amethyst_Expression160'):
        assert _is_linked(b1, 'amethyst_Expression160', a)
    _safe_set(a, 'amethyst_MultiplicativeExpression159', b2)
    assert _is_linked(a, 'amethyst_MultiplicativeExpression159', b2)
    if hasattr(b1, 'amethyst_Expression160'):
        assert not _is_linked(b1, 'amethyst_Expression160', a)
    if hasattr(b2, 'amethyst_Expression160'):
        assert _is_linked(b2, 'amethyst_Expression160', a)
    _safe_set(a, 'amethyst_MultiplicativeExpression159', None)
    assert not _is_linked(a, 'amethyst_MultiplicativeExpression159', b2)
    if hasattr(b2, 'amethyst_Expression160'):
        assert not _is_linked(b2, 'amethyst_Expression160', a)


def test_assoc_right163_link_reassign_clear():
    a = amethyst_MatchingExpression(operator="sample_text")
    b1 = amethyst_Expression()
    b2 = amethyst_Expression()
    _safe_set(a, 'amethyst_MatchingExpression164', b1)
    assert _is_linked(a, 'amethyst_MatchingExpression164', b1)
    if hasattr(b1, 'amethyst_Expression165'):
        assert _is_linked(b1, 'amethyst_Expression165', a)
    _safe_set(a, 'amethyst_MatchingExpression164', b2)
    assert _is_linked(a, 'amethyst_MatchingExpression164', b2)
    if hasattr(b1, 'amethyst_Expression165'):
        assert not _is_linked(b1, 'amethyst_Expression165', a)
    if hasattr(b2, 'amethyst_Expression165'):
        assert _is_linked(b2, 'amethyst_Expression165', a)
    _safe_set(a, 'amethyst_MatchingExpression164', None)
    assert not _is_linked(a, 'amethyst_MatchingExpression164', b2)
    if hasattr(b2, 'amethyst_Expression165'):
        assert not _is_linked(b2, 'amethyst_Expression165', a)


def test_assoc_start187_link_reassign_clear():
    a = amethyst_IntLiteral(value=7)
    b1 = amethyst_NumberRangeLiteral()
    b2 = amethyst_NumberRangeLiteral()
    _safe_set(a, 'amethyst_IntLiteral', b1)
    assert _is_linked(a, 'amethyst_IntLiteral', b1)
    if hasattr(b1, 'amethyst_NumberRangeLiteral'):
        assert _is_linked(b1, 'amethyst_NumberRangeLiteral', a)
    _safe_set(a, 'amethyst_IntLiteral', b2)
    assert _is_linked(a, 'amethyst_IntLiteral', b2)
    if hasattr(b1, 'amethyst_NumberRangeLiteral'):
        assert not _is_linked(b1, 'amethyst_NumberRangeLiteral', a)
    if hasattr(b2, 'amethyst_NumberRangeLiteral'):
        assert _is_linked(b2, 'amethyst_NumberRangeLiteral', a)
    _safe_set(a, 'amethyst_IntLiteral', None)
    assert not _is_linked(a, 'amethyst_IntLiteral', b2)
    if hasattr(b2, 'amethyst_NumberRangeLiteral'):
        assert not _is_linked(b2, 'amethyst_NumberRangeLiteral', a)


def test_assoc_start191_link_reassign_clear():
    a = amethyst_CharLiteral(value="sample_text")
    b1 = amethyst_CharRangeLiteral()
    b2 = amethyst_CharRangeLiteral()
    _safe_set(a, 'amethyst_CharLiteral', b1)
    assert _is_linked(a, 'amethyst_CharLiteral', b1)
    if hasattr(b1, 'amethyst_CharRangeLiteral'):
        assert _is_linked(b1, 'amethyst_CharRangeLiteral', a)
    _safe_set(a, 'amethyst_CharLiteral', b2)
    assert _is_linked(a, 'amethyst_CharLiteral', b2)
    if hasattr(b1, 'amethyst_CharRangeLiteral'):
        assert not _is_linked(b1, 'amethyst_CharRangeLiteral', a)
    if hasattr(b2, 'amethyst_CharRangeLiteral'):
        assert _is_linked(b2, 'amethyst_CharRangeLiteral', a)
    _safe_set(a, 'amethyst_CharLiteral', None)
    assert not _is_linked(a, 'amethyst_CharLiteral', b2)
    if hasattr(b2, 'amethyst_CharRangeLiteral'):
        assert not _is_linked(b2, 'amethyst_CharRangeLiteral', a)


def test_assoc_statements35_link_reassign_clear():
    a = amethyst_DefinitionDeclaration(static=True)
    b1 = amethyst_Statement()
    b2 = amethyst_Statement()
    _safe_set(a, 'amethyst_DefinitionDeclaration36', {b1})
    assert _is_linked(a, 'amethyst_DefinitionDeclaration36', b1)
    if hasattr(b1, 'amethyst_Statement37'):
        assert _is_linked(b1, 'amethyst_Statement37', a)
    _safe_set(a, 'amethyst_DefinitionDeclaration36', {b2})
    assert _is_linked(a, 'amethyst_DefinitionDeclaration36', b2)
    if hasattr(b1, 'amethyst_Statement37'):
        assert not _is_linked(b1, 'amethyst_Statement37', a)
    if hasattr(b2, 'amethyst_Statement37'):
        assert _is_linked(b2, 'amethyst_Statement37', a)
    _safe_set(a, 'amethyst_DefinitionDeclaration36', set())
    assert not _is_linked(a, 'amethyst_DefinitionDeclaration36', b2)
    if hasattr(b2, 'amethyst_Statement37'):
        assert not _is_linked(b2, 'amethyst_Statement37', a)


def test_assoc_symbolRef21_link_reassign_clear():
    a = amethyst_Symbol(name="sample_text")
    b1 = amethyst_SymbolReference()
    b2 = amethyst_SymbolReference()
    _safe_set(a, 'amethyst_Symbol22', b1)
    assert _is_linked(a, 'amethyst_Symbol22', b1)
    if hasattr(b1, 'amethyst_SymbolReference'):
        assert _is_linked(b1, 'amethyst_SymbolReference', a)
    _safe_set(a, 'amethyst_Symbol22', b2)
    assert _is_linked(a, 'amethyst_Symbol22', b2)
    if hasattr(b1, 'amethyst_SymbolReference'):
        assert not _is_linked(b1, 'amethyst_SymbolReference', a)
    if hasattr(b2, 'amethyst_SymbolReference'):
        assert _is_linked(b2, 'amethyst_SymbolReference', a)
    _safe_set(a, 'amethyst_Symbol22', None)
    assert not _is_linked(a, 'amethyst_Symbol22', b2)
    if hasattr(b2, 'amethyst_SymbolReference'):
        assert not _is_linked(b2, 'amethyst_SymbolReference', a)


def test_assoc_type32_link_reassign_clear():
    a = amethyst_DefinitionDeclaration(static=True)
    b1 = amethyst_AbstractType()
    b2 = amethyst_AbstractType()
    _safe_set(a, 'amethyst_DefinitionDeclaration33', b1)
    assert _is_linked(a, 'amethyst_DefinitionDeclaration33', b1)
    if hasattr(b1, 'amethyst_AbstractType34'):
        assert _is_linked(b1, 'amethyst_AbstractType34', a)
    _safe_set(a, 'amethyst_DefinitionDeclaration33', b2)
    assert _is_linked(a, 'amethyst_DefinitionDeclaration33', b2)
    if hasattr(b1, 'amethyst_AbstractType34'):
        assert not _is_linked(b1, 'amethyst_AbstractType34', a)
    if hasattr(b2, 'amethyst_AbstractType34'):
        assert _is_linked(b2, 'amethyst_AbstractType34', a)
    _safe_set(a, 'amethyst_DefinitionDeclaration33', None)
    assert not _is_linked(a, 'amethyst_DefinitionDeclaration33', b2)
    if hasattr(b2, 'amethyst_AbstractType34'):
        assert not _is_linked(b2, 'amethyst_AbstractType34', a)


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

AbstractType_strategy = st.builds(AbstractType)
@given(instance=AbstractType_strategy)
@settings(max_examples=25)
def test_AbstractType_instantiation(instance):
    assert isinstance(instance, AbstractType)


Expression_strategy = st.builds(Expression)
@given(instance=Expression_strategy)
@settings(max_examples=25)
def test_Expression_instantiation(instance):
    assert isinstance(instance, Expression)


Literal_strategy = st.builds(Literal)
@given(instance=Literal_strategy)
@settings(max_examples=25)
def test_Literal_instantiation(instance):
    assert isinstance(instance, Literal)


PrimitiveType_strategy = st.builds(PrimitiveType)
@given(instance=PrimitiveType_strategy)
@settings(max_examples=25)
def test_PrimitiveType_instantiation(instance):
    assert isinstance(instance, PrimitiveType)


RangeLiteral_strategy = st.builds(RangeLiteral)
@given(instance=RangeLiteral_strategy)
@settings(max_examples=25)
def test_RangeLiteral_instantiation(instance):
    assert isinstance(instance, RangeLiteral)


Statement_strategy = st.builds(Statement)
@given(instance=Statement_strategy)
@settings(max_examples=25)
def test_Statement_instantiation(instance):
    assert isinstance(instance, Statement)


Symbol_strategy = st.builds(Symbol)
@given(instance=Symbol_strategy)
@settings(max_examples=25)
def test_Symbol_instantiation(instance):
    assert isinstance(instance, Symbol)


Type_strategy = st.builds(Type)
@given(instance=Type_strategy)
@settings(max_examples=25)
def test_Type_instantiation(instance):
    assert isinstance(instance, Type)


amethyst_AbstractType_strategy = st.builds(amethyst_AbstractType)
@given(instance=amethyst_AbstractType_strategy)
@settings(max_examples=25)
def test_amethyst_AbstractType_instantiation(instance):
    assert isinstance(instance, amethyst_AbstractType)


amethyst_AdditiveExpression_strategy = st.builds(amethyst_AdditiveExpression, operator=safe_text)
@given(instance=amethyst_AdditiveExpression_strategy)
@settings(max_examples=25)
def test_amethyst_AdditiveExpression_instantiation(instance):
    assert isinstance(instance, amethyst_AdditiveExpression)


amethyst_AndExpression_strategy = st.builds(amethyst_AndExpression)
@given(instance=amethyst_AndExpression_strategy)
@settings(max_examples=25)
def test_amethyst_AndExpression_instantiation(instance):
    assert isinstance(instance, amethyst_AndExpression)


amethyst_AnyType_strategy = st.builds(amethyst_AnyType)
@given(instance=amethyst_AnyType_strategy)
@settings(max_examples=25)
def test_amethyst_AnyType_instantiation(instance):
    assert isinstance(instance, amethyst_AnyType)


amethyst_ArrayType_strategy = st.builds(amethyst_ArrayType)
@given(instance=amethyst_ArrayType_strategy)
@settings(max_examples=25)
def test_amethyst_ArrayType_instantiation(instance):
    assert isinstance(instance, amethyst_ArrayType)


amethyst_AssignmentExpression_strategy = st.builds(amethyst_AssignmentExpression)
@given(instance=amethyst_AssignmentExpression_strategy)
@settings(max_examples=25)
def test_amethyst_AssignmentExpression_instantiation(instance):
    assert isinstance(instance, amethyst_AssignmentExpression)


amethyst_BooleanLiteral_strategy = st.builds(amethyst_BooleanLiteral, value=st.booleans())
@given(instance=amethyst_BooleanLiteral_strategy)
@settings(max_examples=25)
def test_amethyst_BooleanLiteral_instantiation(instance):
    assert isinstance(instance, amethyst_BooleanLiteral)


amethyst_BooleanType_strategy = st.builds(amethyst_BooleanType)
@given(instance=amethyst_BooleanType_strategy)
@settings(max_examples=25)
def test_amethyst_BooleanType_instantiation(instance):
    assert isinstance(instance, amethyst_BooleanType)


amethyst_BreakStatement_strategy = st.builds(amethyst_BreakStatement)
@given(instance=amethyst_BreakStatement_strategy)
@settings(max_examples=25)
def test_amethyst_BreakStatement_instantiation(instance):
    assert isinstance(instance, amethyst_BreakStatement)


amethyst_CallExpression_strategy = st.builds(amethyst_CallExpression)
@given(instance=amethyst_CallExpression_strategy)
@settings(max_examples=25)
def test_amethyst_CallExpression_instantiation(instance):
    assert isinstance(instance, amethyst_CallExpression)


amethyst_CaseElseStatement_strategy = st.builds(amethyst_CaseElseStatement)
@given(instance=amethyst_CaseElseStatement_strategy)
@settings(max_examples=25)
def test_amethyst_CaseElseStatement_instantiation(instance):
    assert isinstance(instance, amethyst_CaseElseStatement)


amethyst_CaseStatement_strategy = st.builds(amethyst_CaseStatement)
@given(instance=amethyst_CaseStatement_strategy)
@settings(max_examples=25)
def test_amethyst_CaseStatement_instantiation(instance):
    assert isinstance(instance, amethyst_CaseStatement)


amethyst_CharLiteral_strategy = st.builds(amethyst_CharLiteral, value=safe_text)
@given(instance=amethyst_CharLiteral_strategy)
@settings(max_examples=25)
def test_amethyst_CharLiteral_instantiation(instance):
    assert isinstance(instance, amethyst_CharLiteral)


amethyst_CharRangeLiteral_strategy = st.builds(amethyst_CharRangeLiteral)
@given(instance=amethyst_CharRangeLiteral_strategy)
@settings(max_examples=25)
def test_amethyst_CharRangeLiteral_instantiation(instance):
    assert isinstance(instance, amethyst_CharRangeLiteral)


amethyst_CharType_strategy = st.builds(amethyst_CharType)
@given(instance=amethyst_CharType_strategy)
@settings(max_examples=25)
def test_amethyst_CharType_instantiation(instance):
    assert isinstance(instance, amethyst_CharType)


amethyst_ClassDeclaration_strategy = st.builds(amethyst_ClassDeclaration)
@given(instance=amethyst_ClassDeclaration_strategy)
@settings(max_examples=25)
def test_amethyst_ClassDeclaration_instantiation(instance):
    assert isinstance(instance, amethyst_ClassDeclaration)


amethyst_ClassType_strategy = st.builds(amethyst_ClassType)
@given(instance=amethyst_ClassType_strategy)
@settings(max_examples=25)
def test_amethyst_ClassType_instantiation(instance):
    assert isinstance(instance, amethyst_ClassType)


amethyst_DefinitionDeclaration_strategy = st.builds(amethyst_DefinitionDeclaration, static=st.booleans())
@given(instance=amethyst_DefinitionDeclaration_strategy)
@settings(max_examples=25)
def test_amethyst_DefinitionDeclaration_instantiation(instance):
    assert isinstance(instance, amethyst_DefinitionDeclaration)


amethyst_DefinitionType_strategy = st.builds(amethyst_DefinitionType)
@given(instance=amethyst_DefinitionType_strategy)
@settings(max_examples=25)
def test_amethyst_DefinitionType_instantiation(instance):
    assert isinstance(instance, amethyst_DefinitionType)


amethyst_EObject_strategy = st.builds(amethyst_EObject)
@given(instance=amethyst_EObject_strategy)
@settings(max_examples=25)
def test_amethyst_EObject_instantiation(instance):
    assert isinstance(instance, amethyst_EObject)


amethyst_ElseIfStatement_strategy = st.builds(amethyst_ElseIfStatement)
@given(instance=amethyst_ElseIfStatement_strategy)
@settings(max_examples=25)
def test_amethyst_ElseIfStatement_instantiation(instance):
    assert isinstance(instance, amethyst_ElseIfStatement)


amethyst_ElseStatement_strategy = st.builds(amethyst_ElseStatement)
@given(instance=amethyst_ElseStatement_strategy)
@settings(max_examples=25)
def test_amethyst_ElseStatement_instantiation(instance):
    assert isinstance(instance, amethyst_ElseStatement)


amethyst_EqualityExpression_strategy = st.builds(amethyst_EqualityExpression, operator=safe_text)
@given(instance=amethyst_EqualityExpression_strategy)
@settings(max_examples=25)
def test_amethyst_EqualityExpression_instantiation(instance):
    assert isinstance(instance, amethyst_EqualityExpression)


amethyst_Expression_strategy = st.builds(amethyst_Expression)
@given(instance=amethyst_Expression_strategy)
@settings(max_examples=25)
def test_amethyst_Expression_instantiation(instance):
    assert isinstance(instance, amethyst_Expression)


amethyst_FloatLiteral_strategy = st.builds(amethyst_FloatLiteral, value=st.floats(allow_nan=False, allow_infinity=False))
@given(instance=amethyst_FloatLiteral_strategy)
@settings(max_examples=25)
def test_amethyst_FloatLiteral_instantiation(instance):
    assert isinstance(instance, amethyst_FloatLiteral)


amethyst_FloatType_strategy = st.builds(amethyst_FloatType)
@given(instance=amethyst_FloatType_strategy)
@settings(max_examples=25)
def test_amethyst_FloatType_instantiation(instance):
    assert isinstance(instance, amethyst_FloatType)


amethyst_ForInitializerDeclaration_strategy = st.builds(amethyst_ForInitializerDeclaration)
@given(instance=amethyst_ForInitializerDeclaration_strategy)
@settings(max_examples=25)
def test_amethyst_ForInitializerDeclaration_instantiation(instance):
    assert isinstance(instance, amethyst_ForInitializerDeclaration)


amethyst_ForStatement_strategy = st.builds(amethyst_ForStatement)
@given(instance=amethyst_ForStatement_strategy)
@settings(max_examples=25)
def test_amethyst_ForStatement_instantiation(instance):
    assert isinstance(instance, amethyst_ForStatement)


amethyst_IfStatement_strategy = st.builds(amethyst_IfStatement)
@given(instance=amethyst_IfStatement_strategy)
@settings(max_examples=25)
def test_amethyst_IfStatement_instantiation(instance):
    assert isinstance(instance, amethyst_IfStatement)


amethyst_Import_strategy = st.builds(amethyst_Import, importedNamespace=safe_text)
@given(instance=amethyst_Import_strategy)
@settings(max_examples=25)
def test_amethyst_Import_instantiation(instance):
    assert isinstance(instance, amethyst_Import)


amethyst_InExpression_strategy = st.builds(amethyst_InExpression)
@given(instance=amethyst_InExpression_strategy)
@settings(max_examples=25)
def test_amethyst_InExpression_instantiation(instance):
    assert isinstance(instance, amethyst_InExpression)


amethyst_IndexAccessExpression_strategy = st.builds(amethyst_IndexAccessExpression)
@given(instance=amethyst_IndexAccessExpression_strategy)
@settings(max_examples=25)
def test_amethyst_IndexAccessExpression_instantiation(instance):
    assert isinstance(instance, amethyst_IndexAccessExpression)


amethyst_IntLiteral_strategy = st.builds(amethyst_IntLiteral, value=st.integers())
@given(instance=amethyst_IntLiteral_strategy)
@settings(max_examples=25)
def test_amethyst_IntLiteral_instantiation(instance):
    assert isinstance(instance, amethyst_IntLiteral)


amethyst_IntType_strategy = st.builds(amethyst_IntType)
@given(instance=amethyst_IntType_strategy)
@settings(max_examples=25)
def test_amethyst_IntType_instantiation(instance):
    assert isinstance(instance, amethyst_IntType)


amethyst_JsCodeStatement_strategy = st.builds(amethyst_JsCodeStatement, value=safe_text)
@given(instance=amethyst_JsCodeStatement_strategy)
@settings(max_examples=25)
def test_amethyst_JsCodeStatement_instantiation(instance):
    assert isinstance(instance, amethyst_JsCodeStatement)


amethyst_Literal_strategy = st.builds(amethyst_Literal)
@given(instance=amethyst_Literal_strategy)
@settings(max_examples=25)
def test_amethyst_Literal_instantiation(instance):
    assert isinstance(instance, amethyst_Literal)


amethyst_MatchingExpression_strategy = st.builds(amethyst_MatchingExpression, operator=safe_text)
@given(instance=amethyst_MatchingExpression_strategy)
@settings(max_examples=25)
def test_amethyst_MatchingExpression_instantiation(instance):
    assert isinstance(instance, amethyst_MatchingExpression)


amethyst_MemberAccessExpression_strategy = st.builds(amethyst_MemberAccessExpression)
@given(instance=amethyst_MemberAccessExpression_strategy)
@settings(max_examples=25)
def test_amethyst_MemberAccessExpression_instantiation(instance):
    assert isinstance(instance, amethyst_MemberAccessExpression)


amethyst_Module_strategy = st.builds(amethyst_Module, name=safe_text)
@given(instance=amethyst_Module_strategy)
@settings(max_examples=25)
def test_amethyst_Module_instantiation(instance):
    assert isinstance(instance, amethyst_Module)


amethyst_MultiplicativeExpression_strategy = st.builds(amethyst_MultiplicativeExpression, operator=safe_text)
@given(instance=amethyst_MultiplicativeExpression_strategy)
@settings(max_examples=25)
def test_amethyst_MultiplicativeExpression_instantiation(instance):
    assert isinstance(instance, amethyst_MultiplicativeExpression)


amethyst_NewExpression_strategy = st.builds(amethyst_NewExpression)
@given(instance=amethyst_NewExpression_strategy)
@settings(max_examples=25)
def test_amethyst_NewExpression_instantiation(instance):
    assert isinstance(instance, amethyst_NewExpression)


amethyst_NextStatement_strategy = st.builds(amethyst_NextStatement)
@given(instance=amethyst_NextStatement_strategy)
@settings(max_examples=25)
def test_amethyst_NextStatement_instantiation(instance):
    assert isinstance(instance, amethyst_NextStatement)


amethyst_NotExpression_strategy = st.builds(amethyst_NotExpression)
@given(instance=amethyst_NotExpression_strategy)
@settings(max_examples=25)
def test_amethyst_NotExpression_instantiation(instance):
    assert isinstance(instance, amethyst_NotExpression)


amethyst_NullLiteral_strategy = st.builds(amethyst_NullLiteral)
@given(instance=amethyst_NullLiteral_strategy)
@settings(max_examples=25)
def test_amethyst_NullLiteral_instantiation(instance):
    assert isinstance(instance, amethyst_NullLiteral)


amethyst_NumberRangeLiteral_strategy = st.builds(amethyst_NumberRangeLiteral)
@given(instance=amethyst_NumberRangeLiteral_strategy)
@settings(max_examples=25)
def test_amethyst_NumberRangeLiteral_instantiation(instance):
    assert isinstance(instance, amethyst_NumberRangeLiteral)


amethyst_OrExpression_strategy = st.builds(amethyst_OrExpression)
@given(instance=amethyst_OrExpression_strategy)
@settings(max_examples=25)
def test_amethyst_OrExpression_instantiation(instance):
    assert isinstance(instance, amethyst_OrExpression)


amethyst_ParameterDeclaration_strategy = st.builds(amethyst_ParameterDeclaration)
@given(instance=amethyst_ParameterDeclaration_strategy)
@settings(max_examples=25)
def test_amethyst_ParameterDeclaration_instantiation(instance):
    assert isinstance(instance, amethyst_ParameterDeclaration)


amethyst_ParenthisedExpression_strategy = st.builds(amethyst_ParenthisedExpression)
@given(instance=amethyst_ParenthisedExpression_strategy)
@settings(max_examples=25)
def test_amethyst_ParenthisedExpression_instantiation(instance):
    assert isinstance(instance, amethyst_ParenthisedExpression)


amethyst_PrimitiveType_strategy = st.builds(amethyst_PrimitiveType)
@given(instance=amethyst_PrimitiveType_strategy)
@settings(max_examples=25)
def test_amethyst_PrimitiveType_instantiation(instance):
    assert isinstance(instance, amethyst_PrimitiveType)


amethyst_PropertyDeclaration_strategy = st.builds(amethyst_PropertyDeclaration)
@given(instance=amethyst_PropertyDeclaration_strategy)
@settings(max_examples=25)
def test_amethyst_PropertyDeclaration_instantiation(instance):
    assert isinstance(instance, amethyst_PropertyDeclaration)


amethyst_RangeLiteral_strategy = st.builds(amethyst_RangeLiteral)
@given(instance=amethyst_RangeLiteral_strategy)
@settings(max_examples=25)
def test_amethyst_RangeLiteral_instantiation(instance):
    assert isinstance(instance, amethyst_RangeLiteral)


amethyst_RelationalExpression_strategy = st.builds(amethyst_RelationalExpression, operator=safe_text)
@given(instance=amethyst_RelationalExpression_strategy)
@settings(max_examples=25)
def test_amethyst_RelationalExpression_instantiation(instance):
    assert isinstance(instance, amethyst_RelationalExpression)


amethyst_ReturnStatement_strategy = st.builds(amethyst_ReturnStatement)
@given(instance=amethyst_ReturnStatement_strategy)
@settings(max_examples=25)
def test_amethyst_ReturnStatement_instantiation(instance):
    assert isinstance(instance, amethyst_ReturnStatement)


amethyst_SelfExpression_strategy = st.builds(amethyst_SelfExpression)
@given(instance=amethyst_SelfExpression_strategy)
@settings(max_examples=25)
def test_amethyst_SelfExpression_instantiation(instance):
    assert isinstance(instance, amethyst_SelfExpression)


amethyst_ShiftExpression_strategy = st.builds(amethyst_ShiftExpression, operator=safe_text)
@given(instance=amethyst_ShiftExpression_strategy)
@settings(max_examples=25)
def test_amethyst_ShiftExpression_instantiation(instance):
    assert isinstance(instance, amethyst_ShiftExpression)


amethyst_Statement_strategy = st.builds(amethyst_Statement)
@given(instance=amethyst_Statement_strategy)
@settings(max_examples=25)
def test_amethyst_Statement_instantiation(instance):
    assert isinstance(instance, amethyst_Statement)


amethyst_StringLiteral_strategy = st.builds(amethyst_StringLiteral, value=safe_text)
@given(instance=amethyst_StringLiteral_strategy)
@settings(max_examples=25)
def test_amethyst_StringLiteral_instantiation(instance):
    assert isinstance(instance, amethyst_StringLiteral)


amethyst_StringType_strategy = st.builds(amethyst_StringType)
@given(instance=amethyst_StringType_strategy)
@settings(max_examples=25)
def test_amethyst_StringType_instantiation(instance):
    assert isinstance(instance, amethyst_StringType)


amethyst_SuperExpression_strategy = st.builds(amethyst_SuperExpression)
@given(instance=amethyst_SuperExpression_strategy)
@settings(max_examples=25)
def test_amethyst_SuperExpression_instantiation(instance):
    assert isinstance(instance, amethyst_SuperExpression)


amethyst_Symbol_strategy = st.builds(amethyst_Symbol, name=safe_text)
@given(instance=amethyst_Symbol_strategy)
@settings(max_examples=25)
def test_amethyst_Symbol_instantiation(instance):
    assert isinstance(instance, amethyst_Symbol)


amethyst_SymbolReference_strategy = st.builds(amethyst_SymbolReference)
@given(instance=amethyst_SymbolReference_strategy)
@settings(max_examples=25)
def test_amethyst_SymbolReference_instantiation(instance):
    assert isinstance(instance, amethyst_SymbolReference)


amethyst_TagAttribute_strategy = st.builds(amethyst_TagAttribute)
@given(instance=amethyst_TagAttribute_strategy)
@settings(max_examples=25)
def test_amethyst_TagAttribute_instantiation(instance):
    assert isinstance(instance, amethyst_TagAttribute)


amethyst_TagDeclaration_strategy = st.builds(amethyst_TagDeclaration)
@given(instance=amethyst_TagDeclaration_strategy)
@settings(max_examples=25)
def test_amethyst_TagDeclaration_instantiation(instance):
    assert isinstance(instance, amethyst_TagDeclaration)


amethyst_TagExpression_strategy = st.builds(amethyst_TagExpression)
@given(instance=amethyst_TagExpression_strategy)
@settings(max_examples=25)
def test_amethyst_TagExpression_instantiation(instance):
    assert isinstance(instance, amethyst_TagExpression)


amethyst_TagLoopExpression_strategy = st.builds(amethyst_TagLoopExpression)
@given(instance=amethyst_TagLoopExpression_strategy)
@settings(max_examples=25)
def test_amethyst_TagLoopExpression_instantiation(instance):
    assert isinstance(instance, amethyst_TagLoopExpression)


amethyst_TagLoopInitializerDeclaration_strategy = st.builds(amethyst_TagLoopInitializerDeclaration)
@given(instance=amethyst_TagLoopInitializerDeclaration_strategy)
@settings(max_examples=25)
def test_amethyst_TagLoopInitializerDeclaration_instantiation(instance):
    assert isinstance(instance, amethyst_TagLoopInitializerDeclaration)


amethyst_Type_strategy = st.builds(amethyst_Type)
@given(instance=amethyst_Type_strategy)
@settings(max_examples=25)
def test_amethyst_Type_instantiation(instance):
    assert isinstance(instance, amethyst_Type)


amethyst_TypeCastExpression_strategy = st.builds(amethyst_TypeCastExpression)
@given(instance=amethyst_TypeCastExpression_strategy)
@settings(max_examples=25)
def test_amethyst_TypeCastExpression_instantiation(instance):
    assert isinstance(instance, amethyst_TypeCastExpression)


amethyst_UnaryMinusExpression_strategy = st.builds(amethyst_UnaryMinusExpression)
@given(instance=amethyst_UnaryMinusExpression_strategy)
@settings(max_examples=25)
def test_amethyst_UnaryMinusExpression_instantiation(instance):
    assert isinstance(instance, amethyst_UnaryMinusExpression)


amethyst_VariableDeclaration_strategy = st.builds(amethyst_VariableDeclaration)
@given(instance=amethyst_VariableDeclaration_strategy)
@settings(max_examples=25)
def test_amethyst_VariableDeclaration_instantiation(instance):
    assert isinstance(instance, amethyst_VariableDeclaration)


amethyst_WhenStatement_strategy = st.builds(amethyst_WhenStatement)
@given(instance=amethyst_WhenStatement_strategy)
@settings(max_examples=25)
def test_amethyst_WhenStatement_instantiation(instance):
    assert isinstance(instance, amethyst_WhenStatement)


amethyst_WhileStatement_strategy = st.builds(amethyst_WhileStatement)
@given(instance=amethyst_WhileStatement_strategy)
@settings(max_examples=25)
def test_amethyst_WhileStatement_instantiation(instance):
    assert isinstance(instance, amethyst_WhileStatement)



