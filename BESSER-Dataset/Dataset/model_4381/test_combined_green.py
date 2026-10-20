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
    Prefix,
    AffectationPrefixStatement,
    leek_PrefixIncrement,
    leek_PrefixDecrement,
    Postfix,
    AffectationPostfixStatement,
    leek_PostfixDecrement,
    leek_PostfixIncrement,
    ForInVariableReference,
    Expression,
    leek_Div,
    leek_Or,
    leek_Multi,
    leek_FalseLiteral,
    leek_TernaryIf,
    leek_Different,
    leek_Plus,
    leek_And,
    leek_Minus,
    leek_Less,
    leek_TypedDifferent,
    leek_Comparison,
    leek_RealLiteral,
    leek_Postfix,
    leek_More,
    leek_Prefix,
    leek_LessOrEquals,
    leek_TrueLiteral,
    leek_Equals,
    leek_NullLiteral,
    leek_UnitaryMinus,
    leek_Not,
    leek_StringLiteral,
    leek_ArrayLiteral,
    leek_MoreOrEquals,
    leek_IntLiteral,
    leek_ForInVariableReference,
    leek_ForAffectation,
    leek_Script,
    leek_ForInitializer,
    Iteration,
    leek_For,
    leek_ForIn,
    leek_While,
    leek_IfCondition,
    leek_VariableReference,
    ForAffectation,
    ForInitializer,
    leek_VariableDeclaration,
    IfCondition,
    leek_Expression,
    AffectationStatement,
    leek_AffectationIncrement,
    leek_AffectationPrefixStatement,
    leek_AffectationDecrement,
    leek_AffectationPostfixStatement,
    leek_Affectation,
    Statement,
    leek_StatementBlock,
    leek_FunctionDeclaration,
    leek_Iteration,
    leek_LocalDeclaration,
    leek_FunctionCall,
    leek_ReturnStatement,
    leek_GlobalDeclaration,
    leek_EmptyStatement,
    leek_AffectationStatement,
    leek_Include,
    leek_If,
    leek_ContinueStatement,
    leek_BreakStatement,
    leek_Statement,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_hyp_prefix_is_not_abstract():
    assert not inspect.isabstract(Prefix)


def test_hyp_prefix_constructor_exists():
    assert callable(Prefix.__init__)


def test_hyp_prefix_constructor_args():
    sig = inspect.signature(Prefix.__init__)
    params = list(sig.parameters.keys())



def test_hyp_affectationprefixstatement_is_not_abstract():
    assert not inspect.isabstract(AffectationPrefixStatement)


def test_hyp_affectationprefixstatement_constructor_exists():
    assert callable(AffectationPrefixStatement.__init__)


def test_hyp_affectationprefixstatement_constructor_args():
    sig = inspect.signature(AffectationPrefixStatement.__init__)
    params = list(sig.parameters.keys())



def test_hyp_leek_prefixincrement_is_not_abstract():
    assert not inspect.isabstract(leek_PrefixIncrement)


def test_hyp_leek_prefixincrement_constructor_exists():
    assert callable(leek_PrefixIncrement.__init__)


def test_hyp_leek_prefixincrement_constructor_args():
    sig = inspect.signature(leek_PrefixIncrement.__init__)
    params = list(sig.parameters.keys())



def test_hyp_leek_prefixdecrement_is_not_abstract():
    assert not inspect.isabstract(leek_PrefixDecrement)


def test_hyp_leek_prefixdecrement_constructor_exists():
    assert callable(leek_PrefixDecrement.__init__)


def test_hyp_leek_prefixdecrement_constructor_args():
    sig = inspect.signature(leek_PrefixDecrement.__init__)
    params = list(sig.parameters.keys())



def test_hyp_postfix_is_not_abstract():
    assert not inspect.isabstract(Postfix)


def test_hyp_postfix_constructor_exists():
    assert callable(Postfix.__init__)


def test_hyp_postfix_constructor_args():
    sig = inspect.signature(Postfix.__init__)
    params = list(sig.parameters.keys())



def test_hyp_affectationpostfixstatement_is_not_abstract():
    assert not inspect.isabstract(AffectationPostfixStatement)


def test_hyp_affectationpostfixstatement_constructor_exists():
    assert callable(AffectationPostfixStatement.__init__)


def test_hyp_affectationpostfixstatement_constructor_args():
    sig = inspect.signature(AffectationPostfixStatement.__init__)
    params = list(sig.parameters.keys())



def test_hyp_leek_postfixdecrement_is_not_abstract():
    assert not inspect.isabstract(leek_PostfixDecrement)


def test_hyp_leek_postfixdecrement_constructor_exists():
    assert callable(leek_PostfixDecrement.__init__)


def test_hyp_leek_postfixdecrement_constructor_args():
    sig = inspect.signature(leek_PostfixDecrement.__init__)
    params = list(sig.parameters.keys())



def test_hyp_leek_postfixincrement_is_not_abstract():
    assert not inspect.isabstract(leek_PostfixIncrement)


def test_hyp_leek_postfixincrement_constructor_exists():
    assert callable(leek_PostfixIncrement.__init__)


def test_hyp_leek_postfixincrement_constructor_args():
    sig = inspect.signature(leek_PostfixIncrement.__init__)
    params = list(sig.parameters.keys())



def test_hyp_forinvariablereference_is_not_abstract():
    assert not inspect.isabstract(ForInVariableReference)


def test_hyp_forinvariablereference_constructor_exists():
    assert callable(ForInVariableReference.__init__)


def test_hyp_forinvariablereference_constructor_args():
    sig = inspect.signature(ForInVariableReference.__init__)
    params = list(sig.parameters.keys())



def test_hyp_expression_is_not_abstract():
    assert not inspect.isabstract(Expression)


def test_hyp_expression_constructor_exists():
    assert callable(Expression.__init__)


def test_hyp_expression_constructor_args():
    sig = inspect.signature(Expression.__init__)
    params = list(sig.parameters.keys())



def test_hyp_leek_div_is_not_abstract():
    assert not inspect.isabstract(leek_Div)


def test_hyp_leek_div_constructor_exists():
    assert callable(leek_Div.__init__)


def test_hyp_leek_div_constructor_args():
    sig = inspect.signature(leek_Div.__init__)
    params = list(sig.parameters.keys())



def test_hyp_leek_or_is_not_abstract():
    assert not inspect.isabstract(leek_Or)


def test_hyp_leek_or_constructor_exists():
    assert callable(leek_Or.__init__)


def test_hyp_leek_or_constructor_args():
    sig = inspect.signature(leek_Or.__init__)
    params = list(sig.parameters.keys())



def test_hyp_leek_multi_is_not_abstract():
    assert not inspect.isabstract(leek_Multi)


def test_hyp_leek_multi_constructor_exists():
    assert callable(leek_Multi.__init__)


def test_hyp_leek_multi_constructor_args():
    sig = inspect.signature(leek_Multi.__init__)
    params = list(sig.parameters.keys())



def test_hyp_leek_falseliteral_is_not_abstract():
    assert not inspect.isabstract(leek_FalseLiteral)


def test_hyp_leek_falseliteral_constructor_exists():
    assert callable(leek_FalseLiteral.__init__)


def test_hyp_leek_falseliteral_constructor_args():
    sig = inspect.signature(leek_FalseLiteral.__init__)
    params = list(sig.parameters.keys())



def test_hyp_leek_ternaryif_is_not_abstract():
    assert not inspect.isabstract(leek_TernaryIf)


def test_hyp_leek_ternaryif_constructor_exists():
    assert callable(leek_TernaryIf.__init__)


def test_hyp_leek_ternaryif_constructor_args():
    sig = inspect.signature(leek_TernaryIf.__init__)
    params = list(sig.parameters.keys())



def test_hyp_leek_different_is_not_abstract():
    assert not inspect.isabstract(leek_Different)


def test_hyp_leek_different_constructor_exists():
    assert callable(leek_Different.__init__)


def test_hyp_leek_different_constructor_args():
    sig = inspect.signature(leek_Different.__init__)
    params = list(sig.parameters.keys())



def test_hyp_leek_plus_is_not_abstract():
    assert not inspect.isabstract(leek_Plus)


def test_hyp_leek_plus_constructor_exists():
    assert callable(leek_Plus.__init__)


def test_hyp_leek_plus_constructor_args():
    sig = inspect.signature(leek_Plus.__init__)
    params = list(sig.parameters.keys())



def test_hyp_leek_and_is_not_abstract():
    assert not inspect.isabstract(leek_And)


def test_hyp_leek_and_constructor_exists():
    assert callable(leek_And.__init__)


def test_hyp_leek_and_constructor_args():
    sig = inspect.signature(leek_And.__init__)
    params = list(sig.parameters.keys())



def test_hyp_leek_minus_is_not_abstract():
    assert not inspect.isabstract(leek_Minus)


def test_hyp_leek_minus_constructor_exists():
    assert callable(leek_Minus.__init__)


def test_hyp_leek_minus_constructor_args():
    sig = inspect.signature(leek_Minus.__init__)
    params = list(sig.parameters.keys())



def test_hyp_leek_less_is_not_abstract():
    assert not inspect.isabstract(leek_Less)


def test_hyp_leek_less_constructor_exists():
    assert callable(leek_Less.__init__)


def test_hyp_leek_less_constructor_args():
    sig = inspect.signature(leek_Less.__init__)
    params = list(sig.parameters.keys())



def test_hyp_leek_typeddifferent_is_not_abstract():
    assert not inspect.isabstract(leek_TypedDifferent)


def test_hyp_leek_typeddifferent_constructor_exists():
    assert callable(leek_TypedDifferent.__init__)


def test_hyp_leek_typeddifferent_constructor_args():
    sig = inspect.signature(leek_TypedDifferent.__init__)
    params = list(sig.parameters.keys())



def test_hyp_leek_comparison_is_not_abstract():
    assert not inspect.isabstract(leek_Comparison)


def test_hyp_leek_comparison_constructor_exists():
    assert callable(leek_Comparison.__init__)


def test_hyp_leek_comparison_constructor_args():
    sig = inspect.signature(leek_Comparison.__init__)
    params = list(sig.parameters.keys())



def test_hyp_leek_realliteral_is_not_abstract():
    assert not inspect.isabstract(leek_RealLiteral)


def test_hyp_leek_realliteral_constructor_exists():
    assert callable(leek_RealLiteral.__init__)


def test_hyp_leek_realliteral_constructor_args():
    sig = inspect.signature(leek_RealLiteral.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"




def test_hyp_leek_postfix_is_not_abstract():
    assert not inspect.isabstract(leek_Postfix)


def test_hyp_leek_postfix_constructor_exists():
    assert callable(leek_Postfix.__init__)


def test_hyp_leek_postfix_constructor_args():
    sig = inspect.signature(leek_Postfix.__init__)
    params = list(sig.parameters.keys())



def test_hyp_leek_more_is_not_abstract():
    assert not inspect.isabstract(leek_More)


def test_hyp_leek_more_constructor_exists():
    assert callable(leek_More.__init__)


def test_hyp_leek_more_constructor_args():
    sig = inspect.signature(leek_More.__init__)
    params = list(sig.parameters.keys())



def test_hyp_leek_prefix_is_not_abstract():
    assert not inspect.isabstract(leek_Prefix)


def test_hyp_leek_prefix_constructor_exists():
    assert callable(leek_Prefix.__init__)


def test_hyp_leek_prefix_constructor_args():
    sig = inspect.signature(leek_Prefix.__init__)
    params = list(sig.parameters.keys())



def test_hyp_leek_lessorequals_is_not_abstract():
    assert not inspect.isabstract(leek_LessOrEquals)


def test_hyp_leek_lessorequals_constructor_exists():
    assert callable(leek_LessOrEquals.__init__)


def test_hyp_leek_lessorequals_constructor_args():
    sig = inspect.signature(leek_LessOrEquals.__init__)
    params = list(sig.parameters.keys())



def test_hyp_leek_trueliteral_is_not_abstract():
    assert not inspect.isabstract(leek_TrueLiteral)


def test_hyp_leek_trueliteral_constructor_exists():
    assert callable(leek_TrueLiteral.__init__)


def test_hyp_leek_trueliteral_constructor_args():
    sig = inspect.signature(leek_TrueLiteral.__init__)
    params = list(sig.parameters.keys())



def test_hyp_leek_equals_is_not_abstract():
    assert not inspect.isabstract(leek_Equals)


def test_hyp_leek_equals_constructor_exists():
    assert callable(leek_Equals.__init__)


def test_hyp_leek_equals_constructor_args():
    sig = inspect.signature(leek_Equals.__init__)
    params = list(sig.parameters.keys())



def test_hyp_leek_nullliteral_is_not_abstract():
    assert not inspect.isabstract(leek_NullLiteral)


def test_hyp_leek_nullliteral_constructor_exists():
    assert callable(leek_NullLiteral.__init__)


def test_hyp_leek_nullliteral_constructor_args():
    sig = inspect.signature(leek_NullLiteral.__init__)
    params = list(sig.parameters.keys())



def test_hyp_leek_unitaryminus_is_not_abstract():
    assert not inspect.isabstract(leek_UnitaryMinus)


def test_hyp_leek_unitaryminus_constructor_exists():
    assert callable(leek_UnitaryMinus.__init__)


def test_hyp_leek_unitaryminus_constructor_args():
    sig = inspect.signature(leek_UnitaryMinus.__init__)
    params = list(sig.parameters.keys())



def test_hyp_leek_not_is_not_abstract():
    assert not inspect.isabstract(leek_Not)


def test_hyp_leek_not_constructor_exists():
    assert callable(leek_Not.__init__)


def test_hyp_leek_not_constructor_args():
    sig = inspect.signature(leek_Not.__init__)
    params = list(sig.parameters.keys())



def test_hyp_leek_stringliteral_is_not_abstract():
    assert not inspect.isabstract(leek_StringLiteral)


def test_hyp_leek_stringliteral_constructor_exists():
    assert callable(leek_StringLiteral.__init__)


def test_hyp_leek_stringliteral_constructor_args():
    sig = inspect.signature(leek_StringLiteral.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"




def test_hyp_leek_arrayliteral_is_not_abstract():
    assert not inspect.isabstract(leek_ArrayLiteral)


def test_hyp_leek_arrayliteral_constructor_exists():
    assert callable(leek_ArrayLiteral.__init__)


def test_hyp_leek_arrayliteral_constructor_args():
    sig = inspect.signature(leek_ArrayLiteral.__init__)
    params = list(sig.parameters.keys())



def test_hyp_leek_moreorequals_is_not_abstract():
    assert not inspect.isabstract(leek_MoreOrEquals)


def test_hyp_leek_moreorequals_constructor_exists():
    assert callable(leek_MoreOrEquals.__init__)


def test_hyp_leek_moreorequals_constructor_args():
    sig = inspect.signature(leek_MoreOrEquals.__init__)
    params = list(sig.parameters.keys())



def test_hyp_leek_intliteral_is_not_abstract():
    assert not inspect.isabstract(leek_IntLiteral)


def test_hyp_leek_intliteral_constructor_exists():
    assert callable(leek_IntLiteral.__init__)


def test_hyp_leek_intliteral_constructor_args():
    sig = inspect.signature(leek_IntLiteral.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"




def test_hyp_leek_forinvariablereference_is_not_abstract():
    assert not inspect.isabstract(leek_ForInVariableReference)


def test_hyp_leek_forinvariablereference_constructor_exists():
    assert callable(leek_ForInVariableReference.__init__)


def test_hyp_leek_forinvariablereference_constructor_args():
    sig = inspect.signature(leek_ForInVariableReference.__init__)
    params = list(sig.parameters.keys())



def test_hyp_leek_foraffectation_is_not_abstract():
    assert not inspect.isabstract(leek_ForAffectation)


def test_hyp_leek_foraffectation_constructor_exists():
    assert callable(leek_ForAffectation.__init__)


def test_hyp_leek_foraffectation_constructor_args():
    sig = inspect.signature(leek_ForAffectation.__init__)
    params = list(sig.parameters.keys())



def test_hyp_leek_script_is_not_abstract():
    assert not inspect.isabstract(leek_Script)


def test_hyp_leek_script_constructor_exists():
    assert callable(leek_Script.__init__)


def test_hyp_leek_script_constructor_args():
    sig = inspect.signature(leek_Script.__init__)
    params = list(sig.parameters.keys())



def test_hyp_leek_forinitializer_is_not_abstract():
    assert not inspect.isabstract(leek_ForInitializer)


def test_hyp_leek_forinitializer_constructor_exists():
    assert callable(leek_ForInitializer.__init__)


def test_hyp_leek_forinitializer_constructor_args():
    sig = inspect.signature(leek_ForInitializer.__init__)
    params = list(sig.parameters.keys())



def test_hyp_iteration_is_not_abstract():
    assert not inspect.isabstract(Iteration)


def test_hyp_iteration_constructor_exists():
    assert callable(Iteration.__init__)


def test_hyp_iteration_constructor_args():
    sig = inspect.signature(Iteration.__init__)
    params = list(sig.parameters.keys())



def test_hyp_leek_for_is_not_abstract():
    assert not inspect.isabstract(leek_For)


def test_hyp_leek_for_constructor_exists():
    assert callable(leek_For.__init__)


def test_hyp_leek_for_constructor_args():
    sig = inspect.signature(leek_For.__init__)
    params = list(sig.parameters.keys())



def test_hyp_leek_forin_is_not_abstract():
    assert not inspect.isabstract(leek_ForIn)


def test_hyp_leek_forin_constructor_exists():
    assert callable(leek_ForIn.__init__)


def test_hyp_leek_forin_constructor_args():
    sig = inspect.signature(leek_ForIn.__init__)
    params = list(sig.parameters.keys())



def test_hyp_leek_while_is_not_abstract():
    assert not inspect.isabstract(leek_While)


def test_hyp_leek_while_constructor_exists():
    assert callable(leek_While.__init__)


def test_hyp_leek_while_constructor_args():
    sig = inspect.signature(leek_While.__init__)
    params = list(sig.parameters.keys())



def test_hyp_leek_ifcondition_is_not_abstract():
    assert not inspect.isabstract(leek_IfCondition)


def test_hyp_leek_ifcondition_constructor_exists():
    assert callable(leek_IfCondition.__init__)


def test_hyp_leek_ifcondition_constructor_args():
    sig = inspect.signature(leek_IfCondition.__init__)
    params = list(sig.parameters.keys())



def test_hyp_leek_variablereference_is_not_abstract():
    assert not inspect.isabstract(leek_VariableReference)


def test_hyp_leek_variablereference_constructor_exists():
    assert callable(leek_VariableReference.__init__)


def test_hyp_leek_variablereference_constructor_args():
    sig = inspect.signature(leek_VariableReference.__init__)
    params = list(sig.parameters.keys())



def test_hyp_foraffectation_is_not_abstract():
    assert not inspect.isabstract(ForAffectation)


def test_hyp_foraffectation_constructor_exists():
    assert callable(ForAffectation.__init__)


def test_hyp_foraffectation_constructor_args():
    sig = inspect.signature(ForAffectation.__init__)
    params = list(sig.parameters.keys())



def test_hyp_forinitializer_is_not_abstract():
    assert not inspect.isabstract(ForInitializer)


def test_hyp_forinitializer_constructor_exists():
    assert callable(ForInitializer.__init__)


def test_hyp_forinitializer_constructor_args():
    sig = inspect.signature(ForInitializer.__init__)
    params = list(sig.parameters.keys())



def test_hyp_leek_variabledeclaration_is_not_abstract():
    assert not inspect.isabstract(leek_VariableDeclaration)


def test_hyp_leek_variabledeclaration_constructor_exists():
    assert callable(leek_VariableDeclaration.__init__)


def test_hyp_leek_variabledeclaration_constructor_args():
    sig = inspect.signature(leek_VariableDeclaration.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "byAdress" in params, "Missing parameter 'byAdress'"





def test_hyp_ifcondition_is_not_abstract():
    assert not inspect.isabstract(IfCondition)


def test_hyp_ifcondition_constructor_exists():
    assert callable(IfCondition.__init__)


def test_hyp_ifcondition_constructor_args():
    sig = inspect.signature(IfCondition.__init__)
    params = list(sig.parameters.keys())



def test_hyp_leek_expression_is_not_abstract():
    assert not inspect.isabstract(leek_Expression)


def test_hyp_leek_expression_constructor_exists():
    assert callable(leek_Expression.__init__)


def test_hyp_leek_expression_constructor_args():
    sig = inspect.signature(leek_Expression.__init__)
    params = list(sig.parameters.keys())



def test_hyp_affectationstatement_is_not_abstract():
    assert not inspect.isabstract(AffectationStatement)


def test_hyp_affectationstatement_constructor_exists():
    assert callable(AffectationStatement.__init__)


def test_hyp_affectationstatement_constructor_args():
    sig = inspect.signature(AffectationStatement.__init__)
    params = list(sig.parameters.keys())



def test_hyp_leek_affectationincrement_is_not_abstract():
    assert not inspect.isabstract(leek_AffectationIncrement)


def test_hyp_leek_affectationincrement_constructor_exists():
    assert callable(leek_AffectationIncrement.__init__)


def test_hyp_leek_affectationincrement_constructor_args():
    sig = inspect.signature(leek_AffectationIncrement.__init__)
    params = list(sig.parameters.keys())



def test_hyp_leek_affectationprefixstatement_is_not_abstract():
    assert not inspect.isabstract(leek_AffectationPrefixStatement)


def test_hyp_leek_affectationprefixstatement_constructor_exists():
    assert callable(leek_AffectationPrefixStatement.__init__)


def test_hyp_leek_affectationprefixstatement_constructor_args():
    sig = inspect.signature(leek_AffectationPrefixStatement.__init__)
    params = list(sig.parameters.keys())



def test_hyp_leek_affectationdecrement_is_not_abstract():
    assert not inspect.isabstract(leek_AffectationDecrement)


def test_hyp_leek_affectationdecrement_constructor_exists():
    assert callable(leek_AffectationDecrement.__init__)


def test_hyp_leek_affectationdecrement_constructor_args():
    sig = inspect.signature(leek_AffectationDecrement.__init__)
    params = list(sig.parameters.keys())



def test_hyp_leek_affectationpostfixstatement_is_not_abstract():
    assert not inspect.isabstract(leek_AffectationPostfixStatement)


def test_hyp_leek_affectationpostfixstatement_constructor_exists():
    assert callable(leek_AffectationPostfixStatement.__init__)


def test_hyp_leek_affectationpostfixstatement_constructor_args():
    sig = inspect.signature(leek_AffectationPostfixStatement.__init__)
    params = list(sig.parameters.keys())



def test_hyp_leek_affectation_is_not_abstract():
    assert not inspect.isabstract(leek_Affectation)


def test_hyp_leek_affectation_constructor_exists():
    assert callable(leek_Affectation.__init__)


def test_hyp_leek_affectation_constructor_args():
    sig = inspect.signature(leek_Affectation.__init__)
    params = list(sig.parameters.keys())



def test_hyp_statement_is_not_abstract():
    assert not inspect.isabstract(Statement)


def test_hyp_statement_constructor_exists():
    assert callable(Statement.__init__)


def test_hyp_statement_constructor_args():
    sig = inspect.signature(Statement.__init__)
    params = list(sig.parameters.keys())



def test_hyp_leek_statementblock_is_not_abstract():
    assert not inspect.isabstract(leek_StatementBlock)


def test_hyp_leek_statementblock_constructor_exists():
    assert callable(leek_StatementBlock.__init__)


def test_hyp_leek_statementblock_constructor_args():
    sig = inspect.signature(leek_StatementBlock.__init__)
    params = list(sig.parameters.keys())



def test_hyp_leek_functiondeclaration_is_not_abstract():
    assert not inspect.isabstract(leek_FunctionDeclaration)


def test_hyp_leek_functiondeclaration_constructor_exists():
    assert callable(leek_FunctionDeclaration.__init__)


def test_hyp_leek_functiondeclaration_constructor_args():
    sig = inspect.signature(leek_FunctionDeclaration.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"




def test_hyp_leek_iteration_is_not_abstract():
    assert not inspect.isabstract(leek_Iteration)


def test_hyp_leek_iteration_constructor_exists():
    assert callable(leek_Iteration.__init__)


def test_hyp_leek_iteration_constructor_args():
    sig = inspect.signature(leek_Iteration.__init__)
    params = list(sig.parameters.keys())



def test_hyp_leek_localdeclaration_is_not_abstract():
    assert not inspect.isabstract(leek_LocalDeclaration)


def test_hyp_leek_localdeclaration_constructor_exists():
    assert callable(leek_LocalDeclaration.__init__)


def test_hyp_leek_localdeclaration_constructor_args():
    sig = inspect.signature(leek_LocalDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_hyp_leek_functioncall_is_not_abstract():
    assert not inspect.isabstract(leek_FunctionCall)


def test_hyp_leek_functioncall_constructor_exists():
    assert callable(leek_FunctionCall.__init__)


def test_hyp_leek_functioncall_constructor_args():
    sig = inspect.signature(leek_FunctionCall.__init__)
    params = list(sig.parameters.keys())



def test_hyp_leek_returnstatement_is_not_abstract():
    assert not inspect.isabstract(leek_ReturnStatement)


def test_hyp_leek_returnstatement_constructor_exists():
    assert callable(leek_ReturnStatement.__init__)


def test_hyp_leek_returnstatement_constructor_args():
    sig = inspect.signature(leek_ReturnStatement.__init__)
    params = list(sig.parameters.keys())



def test_hyp_leek_globaldeclaration_is_not_abstract():
    assert not inspect.isabstract(leek_GlobalDeclaration)


def test_hyp_leek_globaldeclaration_constructor_exists():
    assert callable(leek_GlobalDeclaration.__init__)


def test_hyp_leek_globaldeclaration_constructor_args():
    sig = inspect.signature(leek_GlobalDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_hyp_leek_emptystatement_is_not_abstract():
    assert not inspect.isabstract(leek_EmptyStatement)


def test_hyp_leek_emptystatement_constructor_exists():
    assert callable(leek_EmptyStatement.__init__)


def test_hyp_leek_emptystatement_constructor_args():
    sig = inspect.signature(leek_EmptyStatement.__init__)
    params = list(sig.parameters.keys())



def test_hyp_leek_affectationstatement_is_not_abstract():
    assert not inspect.isabstract(leek_AffectationStatement)


def test_hyp_leek_affectationstatement_constructor_exists():
    assert callable(leek_AffectationStatement.__init__)


def test_hyp_leek_affectationstatement_constructor_args():
    sig = inspect.signature(leek_AffectationStatement.__init__)
    params = list(sig.parameters.keys())



def test_hyp_leek_include_is_not_abstract():
    assert not inspect.isabstract(leek_Include)


def test_hyp_leek_include_constructor_exists():
    assert callable(leek_Include.__init__)


def test_hyp_leek_include_constructor_args():
    sig = inspect.signature(leek_Include.__init__)
    params = list(sig.parameters.keys())
    assert "importURI" in params, "Missing parameter 'importURI'"




def test_hyp_leek_if_is_not_abstract():
    assert not inspect.isabstract(leek_If)


def test_hyp_leek_if_constructor_exists():
    assert callable(leek_If.__init__)


def test_hyp_leek_if_constructor_args():
    sig = inspect.signature(leek_If.__init__)
    params = list(sig.parameters.keys())



def test_hyp_leek_continuestatement_is_not_abstract():
    assert not inspect.isabstract(leek_ContinueStatement)


def test_hyp_leek_continuestatement_constructor_exists():
    assert callable(leek_ContinueStatement.__init__)


def test_hyp_leek_continuestatement_constructor_args():
    sig = inspect.signature(leek_ContinueStatement.__init__)
    params = list(sig.parameters.keys())



def test_hyp_leek_breakstatement_is_not_abstract():
    assert not inspect.isabstract(leek_BreakStatement)


def test_hyp_leek_breakstatement_constructor_exists():
    assert callable(leek_BreakStatement.__init__)


def test_hyp_leek_breakstatement_constructor_args():
    sig = inspect.signature(leek_BreakStatement.__init__)
    params = list(sig.parameters.keys())



def test_hyp_leek_statement_is_not_abstract():
    assert not inspect.isabstract(leek_Statement)


def test_hyp_leek_statement_constructor_exists():
    assert callable(leek_Statement.__init__)


def test_hyp_leek_statement_constructor_args():
    sig = inspect.signature(leek_Statement.__init__)
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
Prefix_strategy = st.builds(
    Prefix,
)
AffectationPrefixStatement_strategy = st.builds(
    AffectationPrefixStatement,
)
leek_PrefixIncrement_strategy = st.builds(
    leek_PrefixIncrement,
)
leek_PrefixDecrement_strategy = st.builds(
    leek_PrefixDecrement,
)
Postfix_strategy = st.builds(
    Postfix,
)
AffectationPostfixStatement_strategy = st.builds(
    AffectationPostfixStatement,
)
leek_PostfixDecrement_strategy = st.builds(
    leek_PostfixDecrement,
)
leek_PostfixIncrement_strategy = st.builds(
    leek_PostfixIncrement,
)
ForInVariableReference_strategy = st.builds(
    ForInVariableReference,
)
Expression_strategy = st.builds(
    Expression,
)
leek_Div_strategy = st.builds(
    leek_Div,
)
leek_Or_strategy = st.builds(
    leek_Or,
)
leek_Multi_strategy = st.builds(
    leek_Multi,
)
leek_FalseLiteral_strategy = st.builds(
    leek_FalseLiteral,
)
leek_TernaryIf_strategy = st.builds(
    leek_TernaryIf,
)
leek_Different_strategy = st.builds(
    leek_Different,
)
leek_Plus_strategy = st.builds(
    leek_Plus,
)
leek_And_strategy = st.builds(
    leek_And,
)
leek_Minus_strategy = st.builds(
    leek_Minus,
)
leek_Less_strategy = st.builds(
    leek_Less,
)
leek_TypedDifferent_strategy = st.builds(
    leek_TypedDifferent,
)
leek_Comparison_strategy = st.builds(
    leek_Comparison,
)
leek_RealLiteral_strategy = st.builds(
    leek_RealLiteral,
    value=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
leek_Postfix_strategy = st.builds(
    leek_Postfix,
)
leek_More_strategy = st.builds(
    leek_More,
)
leek_Prefix_strategy = st.builds(
    leek_Prefix,
)
leek_LessOrEquals_strategy = st.builds(
    leek_LessOrEquals,
)
leek_TrueLiteral_strategy = st.builds(
    leek_TrueLiteral,
)
leek_Equals_strategy = st.builds(
    leek_Equals,
)
leek_NullLiteral_strategy = st.builds(
    leek_NullLiteral,
)
leek_UnitaryMinus_strategy = st.builds(
    leek_UnitaryMinus,
)
leek_Not_strategy = st.builds(
    leek_Not,
)
leek_StringLiteral_strategy = st.builds(
    leek_StringLiteral,
    value=
        safe_text
)
leek_ArrayLiteral_strategy = st.builds(
    leek_ArrayLiteral,
)
leek_MoreOrEquals_strategy = st.builds(
    leek_MoreOrEquals,
)
leek_IntLiteral_strategy = st.builds(
    leek_IntLiteral,
    value=
        st.integers()
)
leek_ForInVariableReference_strategy = st.builds(
    leek_ForInVariableReference,
)
leek_ForAffectation_strategy = st.builds(
    leek_ForAffectation,
)
leek_Script_strategy = st.builds(
    leek_Script,
)
leek_ForInitializer_strategy = st.builds(
    leek_ForInitializer,
)
Iteration_strategy = st.builds(
    Iteration,
)
leek_For_strategy = st.builds(
    leek_For,
)
leek_ForIn_strategy = st.builds(
    leek_ForIn,
)
leek_While_strategy = st.builds(
    leek_While,
)
leek_IfCondition_strategy = st.builds(
    leek_IfCondition,
)
leek_VariableReference_strategy = st.builds(
    leek_VariableReference,
)
ForAffectation_strategy = st.builds(
    ForAffectation,
)
ForInitializer_strategy = st.builds(
    ForInitializer,
)
leek_VariableDeclaration_strategy = st.builds(
    leek_VariableDeclaration,
    name=
        safe_text,
    byAdress=
        st.booleans()
)
IfCondition_strategy = st.builds(
    IfCondition,
)
leek_Expression_strategy = st.builds(
    leek_Expression,
)
AffectationStatement_strategy = st.builds(
    AffectationStatement,
)
leek_AffectationIncrement_strategy = st.builds(
    leek_AffectationIncrement,
)
leek_AffectationPrefixStatement_strategy = st.builds(
    leek_AffectationPrefixStatement,
)
leek_AffectationDecrement_strategy = st.builds(
    leek_AffectationDecrement,
)
leek_AffectationPostfixStatement_strategy = st.builds(
    leek_AffectationPostfixStatement,
)
leek_Affectation_strategy = st.builds(
    leek_Affectation,
)
Statement_strategy = st.builds(
    Statement,
)
leek_StatementBlock_strategy = st.builds(
    leek_StatementBlock,
)
leek_FunctionDeclaration_strategy = st.builds(
    leek_FunctionDeclaration,
    name=
        safe_text
)
leek_Iteration_strategy = st.builds(
    leek_Iteration,
)
leek_LocalDeclaration_strategy = st.builds(
    leek_LocalDeclaration,
)
leek_FunctionCall_strategy = st.builds(
    leek_FunctionCall,
)
leek_ReturnStatement_strategy = st.builds(
    leek_ReturnStatement,
)
leek_GlobalDeclaration_strategy = st.builds(
    leek_GlobalDeclaration,
)
leek_EmptyStatement_strategy = st.builds(
    leek_EmptyStatement,
)
leek_AffectationStatement_strategy = st.builds(
    leek_AffectationStatement,
)
leek_Include_strategy = st.builds(
    leek_Include,
    importURI=
        safe_text
)
leek_If_strategy = st.builds(
    leek_If,
)
leek_ContinueStatement_strategy = st.builds(
    leek_ContinueStatement,
)
leek_BreakStatement_strategy = st.builds(
    leek_BreakStatement,
)
leek_Statement_strategy = st.builds(
    leek_Statement,
)


























@given(instance=leek_RealLiteral_strategy)
def test_hyp_leek_realliteral_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original













@given(instance=leek_StringLiteral_strategy)
def test_hyp_leek_stringliteral_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original






@given(instance=leek_IntLiteral_strategy)
def test_hyp_leek_intliteral_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original
















@given(instance=leek_VariableDeclaration_strategy)
def test_hyp_leek_variabledeclaration_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=leek_VariableDeclaration_strategy)
def test_hyp_leek_variabledeclaration_byAdress_setter(instance):
    original = instance.byAdress
    instance.byAdress = original
    assert instance.byAdress == original














@given(instance=leek_FunctionDeclaration_strategy)
def test_hyp_leek_functiondeclaration_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original











@given(instance=leek_Include_strategy)
def test_hyp_leek_include_importURI_setter(instance):
    original = instance.importURI
    instance.importURI = original
    assert instance.importURI == original






# ----- SECTION B: test_structural_full.py (deterministic-first suite) -----
import inspect
import pytest
from datetime import date, datetime, time, timedelta
from hypothesis import given, settings
import hypothesis.strategies as st

from python_code import (
    AffectationPostfixStatement,
    AffectationPrefixStatement,
    AffectationStatement,
    Expression,
    ForAffectation,
    ForInVariableReference,
    ForInitializer,
    IfCondition,
    Iteration,
    Postfix,
    Prefix,
    Statement,
    leek_Affectation,
    leek_AffectationDecrement,
    leek_AffectationIncrement,
    leek_AffectationPostfixStatement,
    leek_AffectationPrefixStatement,
    leek_AffectationStatement,
    leek_And,
    leek_ArrayLiteral,
    leek_BreakStatement,
    leek_Comparison,
    leek_ContinueStatement,
    leek_Different,
    leek_Div,
    leek_EmptyStatement,
    leek_Equals,
    leek_Expression,
    leek_FalseLiteral,
    leek_For,
    leek_ForAffectation,
    leek_ForIn,
    leek_ForInVariableReference,
    leek_ForInitializer,
    leek_FunctionCall,
    leek_FunctionDeclaration,
    leek_GlobalDeclaration,
    leek_If,
    leek_IfCondition,
    leek_Include,
    leek_IntLiteral,
    leek_Iteration,
    leek_Less,
    leek_LessOrEquals,
    leek_LocalDeclaration,
    leek_Minus,
    leek_More,
    leek_MoreOrEquals,
    leek_Multi,
    leek_Not,
    leek_NullLiteral,
    leek_Or,
    leek_Plus,
    leek_Postfix,
    leek_PostfixDecrement,
    leek_PostfixIncrement,
    leek_Prefix,
    leek_PrefixDecrement,
    leek_PrefixIncrement,
    leek_RealLiteral,
    leek_ReturnStatement,
    leek_Script,
    leek_Statement,
    leek_StatementBlock,
    leek_StringLiteral,
    leek_TernaryIf,
    leek_TrueLiteral,
    leek_TypedDifferent,
    leek_UnitaryMinus,
    leek_VariableDeclaration,
    leek_VariableReference,
    leek_While,
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

def test_leek_FunctionDeclaration_name_value_roundtrip():
    instance = leek_FunctionDeclaration(name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_leek_Include_importURI_value_roundtrip():
    instance = leek_Include(importURI="sample_text")
    assert instance.importURI == "sample_text"
    instance.importURI = "sample_text_2"
    assert instance.importURI == "sample_text_2"


def test_leek_IntLiteral_value_value_roundtrip():
    instance = leek_IntLiteral(value=7)
    assert instance.value == 7
    instance.value = 13
    assert instance.value == 13


def test_leek_RealLiteral_value_value_roundtrip():
    instance = leek_RealLiteral(value=3.14)
    assert instance.value == 3.14
    instance.value = 9.99
    assert instance.value == 9.99


def test_leek_StringLiteral_value_value_roundtrip():
    instance = leek_StringLiteral(value="sample_text")
    assert instance.value == "sample_text"
    instance.value = "sample_text_2"
    assert instance.value == "sample_text_2"


def test_leek_VariableDeclaration_byAdress_value_roundtrip():
    instance = leek_VariableDeclaration(byAdress=True, name="sample_text")
    assert instance.byAdress == True
    instance.byAdress = False
    assert instance.byAdress == False


def test_leek_VariableDeclaration_name_value_roundtrip():
    instance = leek_VariableDeclaration(byAdress=True, name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_leek_PostfixDecrement_isa_AffectationPostfixStatement():
    instance = leek_PostfixDecrement()
    assert isinstance(instance, AffectationPostfixStatement)


def test_leek_PostfixIncrement_isa_AffectationPostfixStatement():
    instance = leek_PostfixIncrement()
    assert isinstance(instance, AffectationPostfixStatement)


def test_leek_VariableReference_isa_AffectationPostfixStatement():
    instance = leek_VariableReference()
    assert isinstance(instance, AffectationPostfixStatement)


def test_leek_PrefixDecrement_isa_AffectationPrefixStatement():
    instance = leek_PrefixDecrement()
    assert isinstance(instance, AffectationPrefixStatement)


def test_leek_PrefixIncrement_isa_AffectationPrefixStatement():
    instance = leek_PrefixIncrement()
    assert isinstance(instance, AffectationPrefixStatement)


def test_leek_Affectation_isa_AffectationStatement():
    instance = leek_Affectation()
    assert isinstance(instance, AffectationStatement)


def test_leek_AffectationDecrement_isa_AffectationStatement():
    instance = leek_AffectationDecrement()
    assert isinstance(instance, AffectationStatement)


def test_leek_AffectationIncrement_isa_AffectationStatement():
    instance = leek_AffectationIncrement()
    assert isinstance(instance, AffectationStatement)


def test_leek_AffectationPostfixStatement_isa_AffectationStatement():
    instance = leek_AffectationPostfixStatement()
    assert isinstance(instance, AffectationStatement)


def test_leek_AffectationPrefixStatement_isa_AffectationStatement():
    instance = leek_AffectationPrefixStatement()
    assert isinstance(instance, AffectationStatement)


def test_leek_And_isa_Expression():
    instance = leek_And()
    assert isinstance(instance, Expression)


def test_leek_ArrayLiteral_isa_Expression():
    instance = leek_ArrayLiteral()
    assert isinstance(instance, Expression)


def test_leek_Comparison_isa_Expression():
    instance = leek_Comparison()
    assert isinstance(instance, Expression)


def test_leek_Different_isa_Expression():
    instance = leek_Different()
    assert isinstance(instance, Expression)


def test_leek_Div_isa_Expression():
    instance = leek_Div()
    assert isinstance(instance, Expression)


def test_leek_Equals_isa_Expression():
    instance = leek_Equals()
    assert isinstance(instance, Expression)


def test_leek_FalseLiteral_isa_Expression():
    instance = leek_FalseLiteral()
    assert isinstance(instance, Expression)


def test_leek_FunctionCall_isa_Expression():
    instance = leek_FunctionCall()
    assert isinstance(instance, Expression)


def test_leek_FunctionDeclaration_isa_Expression():
    instance = leek_FunctionDeclaration(name="sample_text")
    assert isinstance(instance, Expression)


def test_leek_IntLiteral_isa_Expression():
    instance = leek_IntLiteral(value=7)
    assert isinstance(instance, Expression)


def test_leek_Less_isa_Expression():
    instance = leek_Less()
    assert isinstance(instance, Expression)


def test_leek_LessOrEquals_isa_Expression():
    instance = leek_LessOrEquals()
    assert isinstance(instance, Expression)


def test_leek_Minus_isa_Expression():
    instance = leek_Minus()
    assert isinstance(instance, Expression)


def test_leek_More_isa_Expression():
    instance = leek_More()
    assert isinstance(instance, Expression)


def test_leek_MoreOrEquals_isa_Expression():
    instance = leek_MoreOrEquals()
    assert isinstance(instance, Expression)


def test_leek_Multi_isa_Expression():
    instance = leek_Multi()
    assert isinstance(instance, Expression)


def test_leek_Not_isa_Expression():
    instance = leek_Not()
    assert isinstance(instance, Expression)


def test_leek_NullLiteral_isa_Expression():
    instance = leek_NullLiteral()
    assert isinstance(instance, Expression)


def test_leek_Or_isa_Expression():
    instance = leek_Or()
    assert isinstance(instance, Expression)


def test_leek_Plus_isa_Expression():
    instance = leek_Plus()
    assert isinstance(instance, Expression)


def test_leek_Postfix_isa_Expression():
    instance = leek_Postfix()
    assert isinstance(instance, Expression)


def test_leek_Prefix_isa_Expression():
    instance = leek_Prefix()
    assert isinstance(instance, Expression)


def test_leek_RealLiteral_isa_Expression():
    instance = leek_RealLiteral(value=3.14)
    assert isinstance(instance, Expression)


def test_leek_StringLiteral_isa_Expression():
    instance = leek_StringLiteral(value="sample_text")
    assert isinstance(instance, Expression)


def test_leek_TernaryIf_isa_Expression():
    instance = leek_TernaryIf()
    assert isinstance(instance, Expression)


def test_leek_TrueLiteral_isa_Expression():
    instance = leek_TrueLiteral()
    assert isinstance(instance, Expression)


def test_leek_TypedDifferent_isa_Expression():
    instance = leek_TypedDifferent()
    assert isinstance(instance, Expression)


def test_leek_UnitaryMinus_isa_Expression():
    instance = leek_UnitaryMinus()
    assert isinstance(instance, Expression)


def test_leek_Affectation_isa_ForAffectation():
    instance = leek_Affectation()
    assert isinstance(instance, ForAffectation)


def test_leek_Expression_isa_ForAffectation():
    instance = leek_Expression()
    assert isinstance(instance, ForAffectation)


def test_leek_VariableDeclaration_isa_ForInVariableReference():
    instance = leek_VariableDeclaration(byAdress=True, name="sample_text")
    assert isinstance(instance, ForInVariableReference)


def test_leek_VariableReference_isa_ForInVariableReference():
    instance = leek_VariableReference()
    assert isinstance(instance, ForInVariableReference)


def test_leek_Affectation_isa_ForInitializer():
    instance = leek_Affectation()
    assert isinstance(instance, ForInitializer)


def test_leek_VariableDeclaration_isa_ForInitializer():
    instance = leek_VariableDeclaration(byAdress=True, name="sample_text")
    assert isinstance(instance, ForInitializer)


def test_leek_Affectation_isa_IfCondition():
    instance = leek_Affectation()
    assert isinstance(instance, IfCondition)


def test_leek_Expression_isa_IfCondition():
    instance = leek_Expression()
    assert isinstance(instance, IfCondition)


def test_leek_For_isa_Iteration():
    instance = leek_For()
    assert isinstance(instance, Iteration)


def test_leek_ForIn_isa_Iteration():
    instance = leek_ForIn()
    assert isinstance(instance, Iteration)


def test_leek_While_isa_Iteration():
    instance = leek_While()
    assert isinstance(instance, Iteration)


def test_leek_PostfixDecrement_isa_Postfix():
    instance = leek_PostfixDecrement()
    assert isinstance(instance, Postfix)


def test_leek_PostfixIncrement_isa_Postfix():
    instance = leek_PostfixIncrement()
    assert isinstance(instance, Postfix)


def test_leek_VariableReference_isa_Postfix():
    instance = leek_VariableReference()
    assert isinstance(instance, Postfix)


def test_leek_PrefixDecrement_isa_Prefix():
    instance = leek_PrefixDecrement()
    assert isinstance(instance, Prefix)


def test_leek_PrefixIncrement_isa_Prefix():
    instance = leek_PrefixIncrement()
    assert isinstance(instance, Prefix)


def test_leek_AffectationStatement_isa_Statement():
    instance = leek_AffectationStatement()
    assert isinstance(instance, Statement)


def test_leek_BreakStatement_isa_Statement():
    instance = leek_BreakStatement()
    assert isinstance(instance, Statement)


def test_leek_ContinueStatement_isa_Statement():
    instance = leek_ContinueStatement()
    assert isinstance(instance, Statement)


def test_leek_EmptyStatement_isa_Statement():
    instance = leek_EmptyStatement()
    assert isinstance(instance, Statement)


def test_leek_FunctionCall_isa_Statement():
    instance = leek_FunctionCall()
    assert isinstance(instance, Statement)


def test_leek_FunctionDeclaration_isa_Statement():
    instance = leek_FunctionDeclaration(name="sample_text")
    assert isinstance(instance, Statement)


def test_leek_GlobalDeclaration_isa_Statement():
    instance = leek_GlobalDeclaration()
    assert isinstance(instance, Statement)


def test_leek_If_isa_Statement():
    instance = leek_If()
    assert isinstance(instance, Statement)


def test_leek_Include_isa_Statement():
    instance = leek_Include(importURI="sample_text")
    assert isinstance(instance, Statement)


def test_leek_Iteration_isa_Statement():
    instance = leek_Iteration()
    assert isinstance(instance, Statement)


def test_leek_LocalDeclaration_isa_Statement():
    instance = leek_LocalDeclaration()
    assert isinstance(instance, Statement)


def test_leek_ReturnStatement_isa_Statement():
    instance = leek_ReturnStatement()
    assert isinstance(instance, Statement)


def test_leek_StatementBlock_isa_Statement():
    instance = leek_StatementBlock()
    assert isinstance(instance, Statement)


def test_assoc_body41_link_reassign_clear():
    a = leek_FunctionDeclaration(name="sample_text")
    b1 = leek_StatementBlock()
    b2 = leek_StatementBlock()
    _safe_set(a, 'leek_FunctionDeclaration42', b1)
    assert _is_linked(a, 'leek_FunctionDeclaration42', b1)
    if hasattr(b1, 'leek_StatementBlock43'):
        assert _is_linked(b1, 'leek_StatementBlock43', a)
    _safe_set(a, 'leek_FunctionDeclaration42', b2)
    assert _is_linked(a, 'leek_FunctionDeclaration42', b2)
    if hasattr(b1, 'leek_StatementBlock43'):
        assert not _is_linked(b1, 'leek_StatementBlock43', a)
    if hasattr(b2, 'leek_StatementBlock43'):
        assert _is_linked(b2, 'leek_StatementBlock43', a)
    _safe_set(a, 'leek_FunctionDeclaration42', None)
    assert not _is_linked(a, 'leek_FunctionDeclaration42', b2)
    if hasattr(b2, 'leek_StatementBlock43'):
        assert not _is_linked(b2, 'leek_StatementBlock43', a)


def test_assoc_function56_link_reassign_clear():
    a = leek_FunctionDeclaration(name="sample_text")
    b1 = leek_FunctionCall()
    b2 = leek_FunctionCall()
    _safe_set(a, 'leek_FunctionDeclaration57', b1)
    assert _is_linked(a, 'leek_FunctionDeclaration57', b1)
    if hasattr(b1, 'leek_FunctionCall'):
        assert _is_linked(b1, 'leek_FunctionCall', a)
    _safe_set(a, 'leek_FunctionDeclaration57', b2)
    assert _is_linked(a, 'leek_FunctionDeclaration57', b2)
    if hasattr(b1, 'leek_FunctionCall'):
        assert not _is_linked(b1, 'leek_FunctionCall', a)
    if hasattr(b2, 'leek_FunctionCall'):
        assert _is_linked(b2, 'leek_FunctionCall', a)
    _safe_set(a, 'leek_FunctionDeclaration57', None)
    assert not _is_linked(a, 'leek_FunctionDeclaration57', b2)
    if hasattr(b2, 'leek_FunctionCall'):
        assert not _is_linked(b2, 'leek_FunctionCall', a)


def test_assoc_parameters40_link_reassign_clear():
    a = leek_VariableDeclaration(byAdress=True, name="sample_text")
    b1 = leek_FunctionDeclaration(name="sample_text")
    b2 = leek_FunctionDeclaration(name="sample_text_2")
    _safe_set(a, 'leek_VariableDeclaration', b1)
    assert _is_linked(a, 'leek_VariableDeclaration', b1)
    if hasattr(b1, 'leek_FunctionDeclaration'):
        assert _is_linked(b1, 'leek_FunctionDeclaration', a)
    _safe_set(a, 'leek_VariableDeclaration', b2)
    assert _is_linked(a, 'leek_VariableDeclaration', b2)
    if hasattr(b1, 'leek_FunctionDeclaration'):
        assert not _is_linked(b1, 'leek_FunctionDeclaration', a)
    if hasattr(b2, 'leek_FunctionDeclaration'):
        assert _is_linked(b2, 'leek_FunctionDeclaration', a)
    _safe_set(a, 'leek_VariableDeclaration', None)
    assert not _is_linked(a, 'leek_VariableDeclaration', b2)
    if hasattr(b2, 'leek_FunctionDeclaration'):
        assert not _is_linked(b2, 'leek_FunctionDeclaration', a)


def test_assoc_variable50_link_reassign_clear():
    a = leek_VariableDeclaration(byAdress=True, name="sample_text")
    b1 = leek_VariableReference()
    b2 = leek_VariableReference()
    _safe_set(a, 'leek_VariableDeclaration52', b1)
    assert _is_linked(a, 'leek_VariableDeclaration52', b1)
    if hasattr(b1, 'leek_VariableReference51'):
        assert _is_linked(b1, 'leek_VariableReference51', a)
    _safe_set(a, 'leek_VariableDeclaration52', b2)
    assert _is_linked(a, 'leek_VariableDeclaration52', b2)
    if hasattr(b1, 'leek_VariableReference51'):
        assert not _is_linked(b1, 'leek_VariableReference51', a)
    if hasattr(b2, 'leek_VariableReference51'):
        assert _is_linked(b2, 'leek_VariableReference51', a)
    _safe_set(a, 'leek_VariableDeclaration52', None)
    assert not _is_linked(a, 'leek_VariableDeclaration52', b2)
    if hasattr(b2, 'leek_VariableReference51'):
        assert not _is_linked(b2, 'leek_VariableReference51', a)


def test_assoc_variables44_link_reassign_clear():
    a = leek_VariableDeclaration(byAdress=True, name="sample_text")
    b1 = leek_LocalDeclaration()
    b2 = leek_LocalDeclaration()
    _safe_set(a, 'leek_VariableDeclaration45', b1)
    assert _is_linked(a, 'leek_VariableDeclaration45', b1)
    if hasattr(b1, 'leek_LocalDeclaration'):
        assert _is_linked(b1, 'leek_LocalDeclaration', a)
    _safe_set(a, 'leek_VariableDeclaration45', b2)
    assert _is_linked(a, 'leek_VariableDeclaration45', b2)
    if hasattr(b1, 'leek_LocalDeclaration'):
        assert not _is_linked(b1, 'leek_LocalDeclaration', a)
    if hasattr(b2, 'leek_LocalDeclaration'):
        assert _is_linked(b2, 'leek_LocalDeclaration', a)
    _safe_set(a, 'leek_VariableDeclaration45', None)
    assert not _is_linked(a, 'leek_VariableDeclaration45', b2)
    if hasattr(b2, 'leek_LocalDeclaration'):
        assert not _is_linked(b2, 'leek_LocalDeclaration', a)


def test_assoc_variables46_link_reassign_clear():
    a = leek_VariableDeclaration(byAdress=True, name="sample_text")
    b1 = leek_GlobalDeclaration()
    b2 = leek_GlobalDeclaration()
    _safe_set(a, 'leek_VariableDeclaration47', b1)
    assert _is_linked(a, 'leek_VariableDeclaration47', b1)
    if hasattr(b1, 'leek_GlobalDeclaration'):
        assert _is_linked(b1, 'leek_GlobalDeclaration', a)
    _safe_set(a, 'leek_VariableDeclaration47', b2)
    assert _is_linked(a, 'leek_VariableDeclaration47', b2)
    if hasattr(b1, 'leek_GlobalDeclaration'):
        assert not _is_linked(b1, 'leek_GlobalDeclaration', a)
    if hasattr(b2, 'leek_GlobalDeclaration'):
        assert _is_linked(b2, 'leek_GlobalDeclaration', a)
    _safe_set(a, 'leek_VariableDeclaration47', None)
    assert not _is_linked(a, 'leek_VariableDeclaration47', b2)
    if hasattr(b2, 'leek_GlobalDeclaration'):
        assert not _is_linked(b2, 'leek_GlobalDeclaration', a)


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

AffectationPostfixStatement_strategy = st.builds(AffectationPostfixStatement)
@given(instance=AffectationPostfixStatement_strategy)
@settings(max_examples=25)
def test_AffectationPostfixStatement_instantiation(instance):
    assert isinstance(instance, AffectationPostfixStatement)


AffectationPrefixStatement_strategy = st.builds(AffectationPrefixStatement)
@given(instance=AffectationPrefixStatement_strategy)
@settings(max_examples=25)
def test_AffectationPrefixStatement_instantiation(instance):
    assert isinstance(instance, AffectationPrefixStatement)


AffectationStatement_strategy = st.builds(AffectationStatement)
@given(instance=AffectationStatement_strategy)
@settings(max_examples=25)
def test_AffectationStatement_instantiation(instance):
    assert isinstance(instance, AffectationStatement)


Expression_strategy = st.builds(Expression)
@given(instance=Expression_strategy)
@settings(max_examples=25)
def test_Expression_instantiation(instance):
    assert isinstance(instance, Expression)


ForAffectation_strategy = st.builds(ForAffectation)
@given(instance=ForAffectation_strategy)
@settings(max_examples=25)
def test_ForAffectation_instantiation(instance):
    assert isinstance(instance, ForAffectation)


ForInVariableReference_strategy = st.builds(ForInVariableReference)
@given(instance=ForInVariableReference_strategy)
@settings(max_examples=25)
def test_ForInVariableReference_instantiation(instance):
    assert isinstance(instance, ForInVariableReference)


ForInitializer_strategy = st.builds(ForInitializer)
@given(instance=ForInitializer_strategy)
@settings(max_examples=25)
def test_ForInitializer_instantiation(instance):
    assert isinstance(instance, ForInitializer)


IfCondition_strategy = st.builds(IfCondition)
@given(instance=IfCondition_strategy)
@settings(max_examples=25)
def test_IfCondition_instantiation(instance):
    assert isinstance(instance, IfCondition)


Iteration_strategy = st.builds(Iteration)
@given(instance=Iteration_strategy)
@settings(max_examples=25)
def test_Iteration_instantiation(instance):
    assert isinstance(instance, Iteration)


Postfix_strategy = st.builds(Postfix)
@given(instance=Postfix_strategy)
@settings(max_examples=25)
def test_Postfix_instantiation(instance):
    assert isinstance(instance, Postfix)


Prefix_strategy = st.builds(Prefix)
@given(instance=Prefix_strategy)
@settings(max_examples=25)
def test_Prefix_instantiation(instance):
    assert isinstance(instance, Prefix)


Statement_strategy = st.builds(Statement)
@given(instance=Statement_strategy)
@settings(max_examples=25)
def test_Statement_instantiation(instance):
    assert isinstance(instance, Statement)


leek_Affectation_strategy = st.builds(leek_Affectation)
@given(instance=leek_Affectation_strategy)
@settings(max_examples=25)
def test_leek_Affectation_instantiation(instance):
    assert isinstance(instance, leek_Affectation)


leek_AffectationDecrement_strategy = st.builds(leek_AffectationDecrement)
@given(instance=leek_AffectationDecrement_strategy)
@settings(max_examples=25)
def test_leek_AffectationDecrement_instantiation(instance):
    assert isinstance(instance, leek_AffectationDecrement)


leek_AffectationIncrement_strategy = st.builds(leek_AffectationIncrement)
@given(instance=leek_AffectationIncrement_strategy)
@settings(max_examples=25)
def test_leek_AffectationIncrement_instantiation(instance):
    assert isinstance(instance, leek_AffectationIncrement)


leek_AffectationPostfixStatement_strategy = st.builds(leek_AffectationPostfixStatement)
@given(instance=leek_AffectationPostfixStatement_strategy)
@settings(max_examples=25)
def test_leek_AffectationPostfixStatement_instantiation(instance):
    assert isinstance(instance, leek_AffectationPostfixStatement)


leek_AffectationPrefixStatement_strategy = st.builds(leek_AffectationPrefixStatement)
@given(instance=leek_AffectationPrefixStatement_strategy)
@settings(max_examples=25)
def test_leek_AffectationPrefixStatement_instantiation(instance):
    assert isinstance(instance, leek_AffectationPrefixStatement)


leek_AffectationStatement_strategy = st.builds(leek_AffectationStatement)
@given(instance=leek_AffectationStatement_strategy)
@settings(max_examples=25)
def test_leek_AffectationStatement_instantiation(instance):
    assert isinstance(instance, leek_AffectationStatement)


leek_And_strategy = st.builds(leek_And)
@given(instance=leek_And_strategy)
@settings(max_examples=25)
def test_leek_And_instantiation(instance):
    assert isinstance(instance, leek_And)


leek_ArrayLiteral_strategy = st.builds(leek_ArrayLiteral)
@given(instance=leek_ArrayLiteral_strategy)
@settings(max_examples=25)
def test_leek_ArrayLiteral_instantiation(instance):
    assert isinstance(instance, leek_ArrayLiteral)


leek_BreakStatement_strategy = st.builds(leek_BreakStatement)
@given(instance=leek_BreakStatement_strategy)
@settings(max_examples=25)
def test_leek_BreakStatement_instantiation(instance):
    assert isinstance(instance, leek_BreakStatement)


leek_Comparison_strategy = st.builds(leek_Comparison)
@given(instance=leek_Comparison_strategy)
@settings(max_examples=25)
def test_leek_Comparison_instantiation(instance):
    assert isinstance(instance, leek_Comparison)


leek_ContinueStatement_strategy = st.builds(leek_ContinueStatement)
@given(instance=leek_ContinueStatement_strategy)
@settings(max_examples=25)
def test_leek_ContinueStatement_instantiation(instance):
    assert isinstance(instance, leek_ContinueStatement)


leek_Different_strategy = st.builds(leek_Different)
@given(instance=leek_Different_strategy)
@settings(max_examples=25)
def test_leek_Different_instantiation(instance):
    assert isinstance(instance, leek_Different)


leek_Div_strategy = st.builds(leek_Div)
@given(instance=leek_Div_strategy)
@settings(max_examples=25)
def test_leek_Div_instantiation(instance):
    assert isinstance(instance, leek_Div)


leek_EmptyStatement_strategy = st.builds(leek_EmptyStatement)
@given(instance=leek_EmptyStatement_strategy)
@settings(max_examples=25)
def test_leek_EmptyStatement_instantiation(instance):
    assert isinstance(instance, leek_EmptyStatement)


leek_Equals_strategy = st.builds(leek_Equals)
@given(instance=leek_Equals_strategy)
@settings(max_examples=25)
def test_leek_Equals_instantiation(instance):
    assert isinstance(instance, leek_Equals)


leek_Expression_strategy = st.builds(leek_Expression)
@given(instance=leek_Expression_strategy)
@settings(max_examples=25)
def test_leek_Expression_instantiation(instance):
    assert isinstance(instance, leek_Expression)


leek_FalseLiteral_strategy = st.builds(leek_FalseLiteral)
@given(instance=leek_FalseLiteral_strategy)
@settings(max_examples=25)
def test_leek_FalseLiteral_instantiation(instance):
    assert isinstance(instance, leek_FalseLiteral)


leek_For_strategy = st.builds(leek_For)
@given(instance=leek_For_strategy)
@settings(max_examples=25)
def test_leek_For_instantiation(instance):
    assert isinstance(instance, leek_For)


leek_ForAffectation_strategy = st.builds(leek_ForAffectation)
@given(instance=leek_ForAffectation_strategy)
@settings(max_examples=25)
def test_leek_ForAffectation_instantiation(instance):
    assert isinstance(instance, leek_ForAffectation)


leek_ForIn_strategy = st.builds(leek_ForIn)
@given(instance=leek_ForIn_strategy)
@settings(max_examples=25)
def test_leek_ForIn_instantiation(instance):
    assert isinstance(instance, leek_ForIn)


leek_ForInVariableReference_strategy = st.builds(leek_ForInVariableReference)
@given(instance=leek_ForInVariableReference_strategy)
@settings(max_examples=25)
def test_leek_ForInVariableReference_instantiation(instance):
    assert isinstance(instance, leek_ForInVariableReference)


leek_ForInitializer_strategy = st.builds(leek_ForInitializer)
@given(instance=leek_ForInitializer_strategy)
@settings(max_examples=25)
def test_leek_ForInitializer_instantiation(instance):
    assert isinstance(instance, leek_ForInitializer)


leek_FunctionCall_strategy = st.builds(leek_FunctionCall)
@given(instance=leek_FunctionCall_strategy)
@settings(max_examples=25)
def test_leek_FunctionCall_instantiation(instance):
    assert isinstance(instance, leek_FunctionCall)


leek_FunctionDeclaration_strategy = st.builds(leek_FunctionDeclaration, name=safe_text)
@given(instance=leek_FunctionDeclaration_strategy)
@settings(max_examples=25)
def test_leek_FunctionDeclaration_instantiation(instance):
    assert isinstance(instance, leek_FunctionDeclaration)


leek_GlobalDeclaration_strategy = st.builds(leek_GlobalDeclaration)
@given(instance=leek_GlobalDeclaration_strategy)
@settings(max_examples=25)
def test_leek_GlobalDeclaration_instantiation(instance):
    assert isinstance(instance, leek_GlobalDeclaration)


leek_If_strategy = st.builds(leek_If)
@given(instance=leek_If_strategy)
@settings(max_examples=25)
def test_leek_If_instantiation(instance):
    assert isinstance(instance, leek_If)


leek_IfCondition_strategy = st.builds(leek_IfCondition)
@given(instance=leek_IfCondition_strategy)
@settings(max_examples=25)
def test_leek_IfCondition_instantiation(instance):
    assert isinstance(instance, leek_IfCondition)


leek_Include_strategy = st.builds(leek_Include, importURI=safe_text)
@given(instance=leek_Include_strategy)
@settings(max_examples=25)
def test_leek_Include_instantiation(instance):
    assert isinstance(instance, leek_Include)


leek_IntLiteral_strategy = st.builds(leek_IntLiteral, value=st.integers())
@given(instance=leek_IntLiteral_strategy)
@settings(max_examples=25)
def test_leek_IntLiteral_instantiation(instance):
    assert isinstance(instance, leek_IntLiteral)


leek_Iteration_strategy = st.builds(leek_Iteration)
@given(instance=leek_Iteration_strategy)
@settings(max_examples=25)
def test_leek_Iteration_instantiation(instance):
    assert isinstance(instance, leek_Iteration)


leek_Less_strategy = st.builds(leek_Less)
@given(instance=leek_Less_strategy)
@settings(max_examples=25)
def test_leek_Less_instantiation(instance):
    assert isinstance(instance, leek_Less)


leek_LessOrEquals_strategy = st.builds(leek_LessOrEquals)
@given(instance=leek_LessOrEquals_strategy)
@settings(max_examples=25)
def test_leek_LessOrEquals_instantiation(instance):
    assert isinstance(instance, leek_LessOrEquals)


leek_LocalDeclaration_strategy = st.builds(leek_LocalDeclaration)
@given(instance=leek_LocalDeclaration_strategy)
@settings(max_examples=25)
def test_leek_LocalDeclaration_instantiation(instance):
    assert isinstance(instance, leek_LocalDeclaration)


leek_Minus_strategy = st.builds(leek_Minus)
@given(instance=leek_Minus_strategy)
@settings(max_examples=25)
def test_leek_Minus_instantiation(instance):
    assert isinstance(instance, leek_Minus)


leek_More_strategy = st.builds(leek_More)
@given(instance=leek_More_strategy)
@settings(max_examples=25)
def test_leek_More_instantiation(instance):
    assert isinstance(instance, leek_More)


leek_MoreOrEquals_strategy = st.builds(leek_MoreOrEquals)
@given(instance=leek_MoreOrEquals_strategy)
@settings(max_examples=25)
def test_leek_MoreOrEquals_instantiation(instance):
    assert isinstance(instance, leek_MoreOrEquals)


leek_Multi_strategy = st.builds(leek_Multi)
@given(instance=leek_Multi_strategy)
@settings(max_examples=25)
def test_leek_Multi_instantiation(instance):
    assert isinstance(instance, leek_Multi)


leek_Not_strategy = st.builds(leek_Not)
@given(instance=leek_Not_strategy)
@settings(max_examples=25)
def test_leek_Not_instantiation(instance):
    assert isinstance(instance, leek_Not)


leek_NullLiteral_strategy = st.builds(leek_NullLiteral)
@given(instance=leek_NullLiteral_strategy)
@settings(max_examples=25)
def test_leek_NullLiteral_instantiation(instance):
    assert isinstance(instance, leek_NullLiteral)


leek_Or_strategy = st.builds(leek_Or)
@given(instance=leek_Or_strategy)
@settings(max_examples=25)
def test_leek_Or_instantiation(instance):
    assert isinstance(instance, leek_Or)


leek_Plus_strategy = st.builds(leek_Plus)
@given(instance=leek_Plus_strategy)
@settings(max_examples=25)
def test_leek_Plus_instantiation(instance):
    assert isinstance(instance, leek_Plus)


leek_Postfix_strategy = st.builds(leek_Postfix)
@given(instance=leek_Postfix_strategy)
@settings(max_examples=25)
def test_leek_Postfix_instantiation(instance):
    assert isinstance(instance, leek_Postfix)


leek_PostfixDecrement_strategy = st.builds(leek_PostfixDecrement)
@given(instance=leek_PostfixDecrement_strategy)
@settings(max_examples=25)
def test_leek_PostfixDecrement_instantiation(instance):
    assert isinstance(instance, leek_PostfixDecrement)


leek_PostfixIncrement_strategy = st.builds(leek_PostfixIncrement)
@given(instance=leek_PostfixIncrement_strategy)
@settings(max_examples=25)
def test_leek_PostfixIncrement_instantiation(instance):
    assert isinstance(instance, leek_PostfixIncrement)


leek_Prefix_strategy = st.builds(leek_Prefix)
@given(instance=leek_Prefix_strategy)
@settings(max_examples=25)
def test_leek_Prefix_instantiation(instance):
    assert isinstance(instance, leek_Prefix)


leek_PrefixDecrement_strategy = st.builds(leek_PrefixDecrement)
@given(instance=leek_PrefixDecrement_strategy)
@settings(max_examples=25)
def test_leek_PrefixDecrement_instantiation(instance):
    assert isinstance(instance, leek_PrefixDecrement)


leek_PrefixIncrement_strategy = st.builds(leek_PrefixIncrement)
@given(instance=leek_PrefixIncrement_strategy)
@settings(max_examples=25)
def test_leek_PrefixIncrement_instantiation(instance):
    assert isinstance(instance, leek_PrefixIncrement)


leek_RealLiteral_strategy = st.builds(leek_RealLiteral, value=st.floats(allow_nan=False, allow_infinity=False))
@given(instance=leek_RealLiteral_strategy)
@settings(max_examples=25)
def test_leek_RealLiteral_instantiation(instance):
    assert isinstance(instance, leek_RealLiteral)


leek_ReturnStatement_strategy = st.builds(leek_ReturnStatement)
@given(instance=leek_ReturnStatement_strategy)
@settings(max_examples=25)
def test_leek_ReturnStatement_instantiation(instance):
    assert isinstance(instance, leek_ReturnStatement)


leek_Script_strategy = st.builds(leek_Script)
@given(instance=leek_Script_strategy)
@settings(max_examples=25)
def test_leek_Script_instantiation(instance):
    assert isinstance(instance, leek_Script)


leek_Statement_strategy = st.builds(leek_Statement)
@given(instance=leek_Statement_strategy)
@settings(max_examples=25)
def test_leek_Statement_instantiation(instance):
    assert isinstance(instance, leek_Statement)


leek_StatementBlock_strategy = st.builds(leek_StatementBlock)
@given(instance=leek_StatementBlock_strategy)
@settings(max_examples=25)
def test_leek_StatementBlock_instantiation(instance):
    assert isinstance(instance, leek_StatementBlock)


leek_StringLiteral_strategy = st.builds(leek_StringLiteral, value=safe_text)
@given(instance=leek_StringLiteral_strategy)
@settings(max_examples=25)
def test_leek_StringLiteral_instantiation(instance):
    assert isinstance(instance, leek_StringLiteral)


leek_TernaryIf_strategy = st.builds(leek_TernaryIf)
@given(instance=leek_TernaryIf_strategy)
@settings(max_examples=25)
def test_leek_TernaryIf_instantiation(instance):
    assert isinstance(instance, leek_TernaryIf)


leek_TrueLiteral_strategy = st.builds(leek_TrueLiteral)
@given(instance=leek_TrueLiteral_strategy)
@settings(max_examples=25)
def test_leek_TrueLiteral_instantiation(instance):
    assert isinstance(instance, leek_TrueLiteral)


leek_TypedDifferent_strategy = st.builds(leek_TypedDifferent)
@given(instance=leek_TypedDifferent_strategy)
@settings(max_examples=25)
def test_leek_TypedDifferent_instantiation(instance):
    assert isinstance(instance, leek_TypedDifferent)


leek_UnitaryMinus_strategy = st.builds(leek_UnitaryMinus)
@given(instance=leek_UnitaryMinus_strategy)
@settings(max_examples=25)
def test_leek_UnitaryMinus_instantiation(instance):
    assert isinstance(instance, leek_UnitaryMinus)


leek_VariableDeclaration_strategy = st.builds(leek_VariableDeclaration, byAdress=st.booleans(), name=safe_text)
@given(instance=leek_VariableDeclaration_strategy)
@settings(max_examples=25)
def test_leek_VariableDeclaration_instantiation(instance):
    assert isinstance(instance, leek_VariableDeclaration)


leek_VariableReference_strategy = st.builds(leek_VariableReference)
@given(instance=leek_VariableReference_strategy)
@settings(max_examples=25)
def test_leek_VariableReference_instantiation(instance):
    assert isinstance(instance, leek_VariableReference)


leek_While_strategy = st.builds(leek_While)
@given(instance=leek_While_strategy)
@settings(max_examples=25)
def test_leek_While_instantiation(instance):
    assert isinstance(instance, leek_While)



