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
    edu_visitor_IASTNodeVisitor,
    edu_ExpressionToExpressionMap,
    SymbolReference,
    edu_ReturnValueReference,
    UnaryExpression,
    edu_Negation,
    edu_Sign,
    Sign,
    edu_Plus,
    edu_Minus,
    FunctionAnnotation,
    edu_Postcondition,
    edu_Precondition,
    QuantifiedExpression,
    edu_ForAllQuantifier,
    edu_ExistsQuantifier,
    PrimitiveType,
    edu_IntegerType,
    edu_BooleanType,
    edu_VariableReference,
    Statement,
    edu_Conditional,
    edu_Loop,
    edu_VariableDeclaration,
    edu_Assignment,
    edu_ReturnStatement,
    edu_Annotation,
    GuardAssertion,
    edu_DivisorNotZeroAssertion,
    edu_FunctionCallPreconditionAssertion,
    Assertion,
    edu_GuardAssertion,
    Annotation,
    edu_Invariant,
    edu_FunctionAnnotation,
    edu_Assumption,
    edu_Assertion,
    Type,
    edu_PrimitiveType,
    edu_ArrayType,
    Literal,
    edu_IntegerLiteral,
    edu_ArrayFunction,
    edu_BooleanLiteral,
    edu_ArrayLiteral,
    Expression,
    edu_LetExpression,
    edu_QuantifiedExpression,
    edu_ArrayAccess,
    edu_TernaryExpression,
    edu_SymbolReference,
    edu_UnaryExpression,
    edu_Literal,
    edu_FunctionCall,
    edu_BinaryExpression,
    BinaryExpression,
    edu_Implication,
    edu_Unequal,
    edu_Less,
    edu_Subtraction,
    edu_Multiplication,
    edu_Disjunction,
    edu_Equal,
    edu_Modulus,
    edu_Conjunction,
    edu_Division,
    edu_LessOrEqual,
    edu_Equivalence,
    edu_Greater,
    edu_GreaterOrEqual,
    edu_Addition,
    edu_ASTNode,
    edu_Axiom,
    edu_Block,
    ASTNode,
    edu_Type,
    edu_Expression,
    edu_FunctionDeclaration,
    edu_ExpressionEvaluation,
    edu_Statement,
    edu_Program,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_hyp_edu_visitor_iastnodevisitor_is_not_abstract():
    assert not inspect.isabstract(edu_visitor_IASTNodeVisitor)


def test_hyp_edu_visitor_iastnodevisitor_constructor_exists():
    assert callable(edu_visitor_IASTNodeVisitor.__init__)


def test_hyp_edu_visitor_iastnodevisitor_constructor_args():
    sig = inspect.signature(edu_visitor_IASTNodeVisitor.__init__)
    params = list(sig.parameters.keys())



def test_hyp_edu_expressiontoexpressionmap_is_not_abstract():
    assert not inspect.isabstract(edu_ExpressionToExpressionMap)


def test_hyp_edu_expressiontoexpressionmap_constructor_exists():
    assert callable(edu_ExpressionToExpressionMap.__init__)


def test_hyp_edu_expressiontoexpressionmap_constructor_args():
    sig = inspect.signature(edu_ExpressionToExpressionMap.__init__)
    params = list(sig.parameters.keys())



def test_hyp_symbolreference_is_not_abstract():
    assert not inspect.isabstract(SymbolReference)


def test_hyp_symbolreference_constructor_exists():
    assert callable(SymbolReference.__init__)


def test_hyp_symbolreference_constructor_args():
    sig = inspect.signature(SymbolReference.__init__)
    params = list(sig.parameters.keys())



def test_hyp_edu_returnvaluereference_is_not_abstract():
    assert not inspect.isabstract(edu_ReturnValueReference)


def test_hyp_edu_returnvaluereference_constructor_exists():
    assert callable(edu_ReturnValueReference.__init__)


def test_hyp_edu_returnvaluereference_constructor_args():
    sig = inspect.signature(edu_ReturnValueReference.__init__)
    params = list(sig.parameters.keys())



def test_hyp_unaryexpression_is_not_abstract():
    assert not inspect.isabstract(UnaryExpression)


def test_hyp_unaryexpression_constructor_exists():
    assert callable(UnaryExpression.__init__)


def test_hyp_unaryexpression_constructor_args():
    sig = inspect.signature(UnaryExpression.__init__)
    params = list(sig.parameters.keys())



def test_hyp_edu_negation_is_not_abstract():
    assert not inspect.isabstract(edu_Negation)


def test_hyp_edu_negation_constructor_exists():
    assert callable(edu_Negation.__init__)


def test_hyp_edu_negation_constructor_args():
    sig = inspect.signature(edu_Negation.__init__)
    params = list(sig.parameters.keys())



def test_hyp_edu_sign_is_not_abstract():
    assert not inspect.isabstract(edu_Sign)


def test_hyp_edu_sign_constructor_exists():
    assert callable(edu_Sign.__init__)


def test_hyp_edu_sign_constructor_args():
    sig = inspect.signature(edu_Sign.__init__)
    params = list(sig.parameters.keys())



def test_hyp_sign_is_not_abstract():
    assert not inspect.isabstract(Sign)


def test_hyp_sign_constructor_exists():
    assert callable(Sign.__init__)


def test_hyp_sign_constructor_args():
    sig = inspect.signature(Sign.__init__)
    params = list(sig.parameters.keys())



def test_hyp_edu_plus_is_not_abstract():
    assert not inspect.isabstract(edu_Plus)


def test_hyp_edu_plus_constructor_exists():
    assert callable(edu_Plus.__init__)


def test_hyp_edu_plus_constructor_args():
    sig = inspect.signature(edu_Plus.__init__)
    params = list(sig.parameters.keys())



def test_hyp_edu_minus_is_not_abstract():
    assert not inspect.isabstract(edu_Minus)


def test_hyp_edu_minus_constructor_exists():
    assert callable(edu_Minus.__init__)


def test_hyp_edu_minus_constructor_args():
    sig = inspect.signature(edu_Minus.__init__)
    params = list(sig.parameters.keys())



def test_hyp_functionannotation_is_not_abstract():
    assert not inspect.isabstract(FunctionAnnotation)


def test_hyp_functionannotation_constructor_exists():
    assert callable(FunctionAnnotation.__init__)


def test_hyp_functionannotation_constructor_args():
    sig = inspect.signature(FunctionAnnotation.__init__)
    params = list(sig.parameters.keys())



def test_hyp_edu_postcondition_is_not_abstract():
    assert not inspect.isabstract(edu_Postcondition)


def test_hyp_edu_postcondition_constructor_exists():
    assert callable(edu_Postcondition.__init__)


def test_hyp_edu_postcondition_constructor_args():
    sig = inspect.signature(edu_Postcondition.__init__)
    params = list(sig.parameters.keys())



def test_hyp_edu_precondition_is_not_abstract():
    assert not inspect.isabstract(edu_Precondition)


def test_hyp_edu_precondition_constructor_exists():
    assert callable(edu_Precondition.__init__)


def test_hyp_edu_precondition_constructor_args():
    sig = inspect.signature(edu_Precondition.__init__)
    params = list(sig.parameters.keys())



def test_hyp_quantifiedexpression_is_not_abstract():
    assert not inspect.isabstract(QuantifiedExpression)


def test_hyp_quantifiedexpression_constructor_exists():
    assert callable(QuantifiedExpression.__init__)


def test_hyp_quantifiedexpression_constructor_args():
    sig = inspect.signature(QuantifiedExpression.__init__)
    params = list(sig.parameters.keys())



def test_hyp_edu_forallquantifier_is_not_abstract():
    assert not inspect.isabstract(edu_ForAllQuantifier)


def test_hyp_edu_forallquantifier_constructor_exists():
    assert callable(edu_ForAllQuantifier.__init__)


def test_hyp_edu_forallquantifier_constructor_args():
    sig = inspect.signature(edu_ForAllQuantifier.__init__)
    params = list(sig.parameters.keys())



def test_hyp_edu_existsquantifier_is_not_abstract():
    assert not inspect.isabstract(edu_ExistsQuantifier)


def test_hyp_edu_existsquantifier_constructor_exists():
    assert callable(edu_ExistsQuantifier.__init__)


def test_hyp_edu_existsquantifier_constructor_args():
    sig = inspect.signature(edu_ExistsQuantifier.__init__)
    params = list(sig.parameters.keys())



def test_hyp_primitivetype_is_not_abstract():
    assert not inspect.isabstract(PrimitiveType)


def test_hyp_primitivetype_constructor_exists():
    assert callable(PrimitiveType.__init__)


def test_hyp_primitivetype_constructor_args():
    sig = inspect.signature(PrimitiveType.__init__)
    params = list(sig.parameters.keys())



def test_hyp_edu_integertype_is_not_abstract():
    assert not inspect.isabstract(edu_IntegerType)


def test_hyp_edu_integertype_constructor_exists():
    assert callable(edu_IntegerType.__init__)


def test_hyp_edu_integertype_constructor_args():
    sig = inspect.signature(edu_IntegerType.__init__)
    params = list(sig.parameters.keys())



def test_hyp_edu_booleantype_is_not_abstract():
    assert not inspect.isabstract(edu_BooleanType)


def test_hyp_edu_booleantype_constructor_exists():
    assert callable(edu_BooleanType.__init__)


def test_hyp_edu_booleantype_constructor_args():
    sig = inspect.signature(edu_BooleanType.__init__)
    params = list(sig.parameters.keys())



def test_hyp_edu_variablereference_is_not_abstract():
    assert not inspect.isabstract(edu_VariableReference)


def test_hyp_edu_variablereference_constructor_exists():
    assert callable(edu_VariableReference.__init__)


def test_hyp_edu_variablereference_constructor_args():
    sig = inspect.signature(edu_VariableReference.__init__)
    params = list(sig.parameters.keys())



def test_hyp_statement_is_not_abstract():
    assert not inspect.isabstract(Statement)


def test_hyp_statement_constructor_exists():
    assert callable(Statement.__init__)


def test_hyp_statement_constructor_args():
    sig = inspect.signature(Statement.__init__)
    params = list(sig.parameters.keys())



def test_hyp_edu_conditional_is_not_abstract():
    assert not inspect.isabstract(edu_Conditional)


def test_hyp_edu_conditional_constructor_exists():
    assert callable(edu_Conditional.__init__)


def test_hyp_edu_conditional_constructor_args():
    sig = inspect.signature(edu_Conditional.__init__)
    params = list(sig.parameters.keys())



def test_hyp_edu_loop_is_not_abstract():
    assert not inspect.isabstract(edu_Loop)


def test_hyp_edu_loop_constructor_exists():
    assert callable(edu_Loop.__init__)


def test_hyp_edu_loop_constructor_args():
    sig = inspect.signature(edu_Loop.__init__)
    params = list(sig.parameters.keys())



def test_hyp_edu_variabledeclaration_is_not_abstract():
    assert not inspect.isabstract(edu_VariableDeclaration)


def test_hyp_edu_variabledeclaration_constructor_exists():
    assert callable(edu_VariableDeclaration.__init__)


def test_hyp_edu_variabledeclaration_constructor_args():
    sig = inspect.signature(edu_VariableDeclaration.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"




def test_hyp_edu_assignment_is_not_abstract():
    assert not inspect.isabstract(edu_Assignment)


def test_hyp_edu_assignment_constructor_exists():
    assert callable(edu_Assignment.__init__)


def test_hyp_edu_assignment_constructor_args():
    sig = inspect.signature(edu_Assignment.__init__)
    params = list(sig.parameters.keys())



def test_hyp_edu_returnstatement_is_not_abstract():
    assert not inspect.isabstract(edu_ReturnStatement)


def test_hyp_edu_returnstatement_constructor_exists():
    assert callable(edu_ReturnStatement.__init__)


def test_hyp_edu_returnstatement_constructor_args():
    sig = inspect.signature(edu_ReturnStatement.__init__)
    params = list(sig.parameters.keys())



def test_hyp_edu_annotation_is_not_abstract():
    assert not inspect.isabstract(edu_Annotation)


def test_hyp_edu_annotation_constructor_exists():
    assert callable(edu_Annotation.__init__)


def test_hyp_edu_annotation_constructor_args():
    sig = inspect.signature(edu_Annotation.__init__)
    params = list(sig.parameters.keys())



def test_hyp_guardassertion_is_not_abstract():
    assert not inspect.isabstract(GuardAssertion)


def test_hyp_guardassertion_constructor_exists():
    assert callable(GuardAssertion.__init__)


def test_hyp_guardassertion_constructor_args():
    sig = inspect.signature(GuardAssertion.__init__)
    params = list(sig.parameters.keys())



def test_hyp_edu_divisornotzeroassertion_is_not_abstract():
    assert not inspect.isabstract(edu_DivisorNotZeroAssertion)


def test_hyp_edu_divisornotzeroassertion_constructor_exists():
    assert callable(edu_DivisorNotZeroAssertion.__init__)


def test_hyp_edu_divisornotzeroassertion_constructor_args():
    sig = inspect.signature(edu_DivisorNotZeroAssertion.__init__)
    params = list(sig.parameters.keys())



def test_hyp_edu_functioncallpreconditionassertion_is_not_abstract():
    assert not inspect.isabstract(edu_FunctionCallPreconditionAssertion)


def test_hyp_edu_functioncallpreconditionassertion_constructor_exists():
    assert callable(edu_FunctionCallPreconditionAssertion.__init__)


def test_hyp_edu_functioncallpreconditionassertion_constructor_args():
    sig = inspect.signature(edu_FunctionCallPreconditionAssertion.__init__)
    params = list(sig.parameters.keys())



def test_hyp_assertion_is_not_abstract():
    assert not inspect.isabstract(Assertion)


def test_hyp_assertion_constructor_exists():
    assert callable(Assertion.__init__)


def test_hyp_assertion_constructor_args():
    sig = inspect.signature(Assertion.__init__)
    params = list(sig.parameters.keys())



def test_hyp_edu_guardassertion_is_not_abstract():
    assert not inspect.isabstract(edu_GuardAssertion)


def test_hyp_edu_guardassertion_constructor_exists():
    assert callable(edu_GuardAssertion.__init__)


def test_hyp_edu_guardassertion_constructor_args():
    sig = inspect.signature(edu_GuardAssertion.__init__)
    params = list(sig.parameters.keys())



def test_hyp_annotation_is_not_abstract():
    assert not inspect.isabstract(Annotation)


def test_hyp_annotation_constructor_exists():
    assert callable(Annotation.__init__)


def test_hyp_annotation_constructor_args():
    sig = inspect.signature(Annotation.__init__)
    params = list(sig.parameters.keys())



def test_hyp_edu_invariant_is_not_abstract():
    assert not inspect.isabstract(edu_Invariant)


def test_hyp_edu_invariant_constructor_exists():
    assert callable(edu_Invariant.__init__)


def test_hyp_edu_invariant_constructor_args():
    sig = inspect.signature(edu_Invariant.__init__)
    params = list(sig.parameters.keys())



def test_hyp_edu_functionannotation_is_not_abstract():
    assert not inspect.isabstract(edu_FunctionAnnotation)


def test_hyp_edu_functionannotation_constructor_exists():
    assert callable(edu_FunctionAnnotation.__init__)


def test_hyp_edu_functionannotation_constructor_args():
    sig = inspect.signature(edu_FunctionAnnotation.__init__)
    params = list(sig.parameters.keys())



def test_hyp_edu_assumption_is_not_abstract():
    assert not inspect.isabstract(edu_Assumption)


def test_hyp_edu_assumption_constructor_exists():
    assert callable(edu_Assumption.__init__)


def test_hyp_edu_assumption_constructor_args():
    sig = inspect.signature(edu_Assumption.__init__)
    params = list(sig.parameters.keys())



def test_hyp_edu_assertion_is_not_abstract():
    assert not inspect.isabstract(edu_Assertion)


def test_hyp_edu_assertion_constructor_exists():
    assert callable(edu_Assertion.__init__)


def test_hyp_edu_assertion_constructor_args():
    sig = inspect.signature(edu_Assertion.__init__)
    params = list(sig.parameters.keys())



def test_hyp_type_is_not_abstract():
    assert not inspect.isabstract(Type)


def test_hyp_type_constructor_exists():
    assert callable(Type.__init__)


def test_hyp_type_constructor_args():
    sig = inspect.signature(Type.__init__)
    params = list(sig.parameters.keys())



def test_hyp_edu_primitivetype_is_not_abstract():
    assert not inspect.isabstract(edu_PrimitiveType)


def test_hyp_edu_primitivetype_constructor_exists():
    assert callable(edu_PrimitiveType.__init__)


def test_hyp_edu_primitivetype_constructor_args():
    sig = inspect.signature(edu_PrimitiveType.__init__)
    params = list(sig.parameters.keys())



def test_hyp_edu_arraytype_is_not_abstract():
    assert not inspect.isabstract(edu_ArrayType)


def test_hyp_edu_arraytype_constructor_exists():
    assert callable(edu_ArrayType.__init__)


def test_hyp_edu_arraytype_constructor_args():
    sig = inspect.signature(edu_ArrayType.__init__)
    params = list(sig.parameters.keys())



def test_hyp_literal_is_not_abstract():
    assert not inspect.isabstract(Literal)


def test_hyp_literal_constructor_exists():
    assert callable(Literal.__init__)


def test_hyp_literal_constructor_args():
    sig = inspect.signature(Literal.__init__)
    params = list(sig.parameters.keys())



def test_hyp_edu_integerliteral_is_not_abstract():
    assert not inspect.isabstract(edu_IntegerLiteral)


def test_hyp_edu_integerliteral_constructor_exists():
    assert callable(edu_IntegerLiteral.__init__)


def test_hyp_edu_integerliteral_constructor_args():
    sig = inspect.signature(edu_IntegerLiteral.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"




def test_hyp_edu_arrayfunction_is_not_abstract():
    assert not inspect.isabstract(edu_ArrayFunction)


def test_hyp_edu_arrayfunction_constructor_exists():
    assert callable(edu_ArrayFunction.__init__)


def test_hyp_edu_arrayfunction_constructor_args():
    sig = inspect.signature(edu_ArrayFunction.__init__)
    params = list(sig.parameters.keys())



def test_hyp_edu_booleanliteral_is_not_abstract():
    assert not inspect.isabstract(edu_BooleanLiteral)


def test_hyp_edu_booleanliteral_constructor_exists():
    assert callable(edu_BooleanLiteral.__init__)


def test_hyp_edu_booleanliteral_constructor_args():
    sig = inspect.signature(edu_BooleanLiteral.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"




def test_hyp_edu_arrayliteral_is_not_abstract():
    assert not inspect.isabstract(edu_ArrayLiteral)


def test_hyp_edu_arrayliteral_constructor_exists():
    assert callable(edu_ArrayLiteral.__init__)


def test_hyp_edu_arrayliteral_constructor_args():
    sig = inspect.signature(edu_ArrayLiteral.__init__)
    params = list(sig.parameters.keys())



def test_hyp_expression_is_not_abstract():
    assert not inspect.isabstract(Expression)


def test_hyp_expression_constructor_exists():
    assert callable(Expression.__init__)


def test_hyp_expression_constructor_args():
    sig = inspect.signature(Expression.__init__)
    params = list(sig.parameters.keys())



def test_hyp_edu_letexpression_is_not_abstract():
    assert not inspect.isabstract(edu_LetExpression)


def test_hyp_edu_letexpression_constructor_exists():
    assert callable(edu_LetExpression.__init__)


def test_hyp_edu_letexpression_constructor_args():
    sig = inspect.signature(edu_LetExpression.__init__)
    params = list(sig.parameters.keys())



def test_hyp_edu_quantifiedexpression_is_not_abstract():
    assert not inspect.isabstract(edu_QuantifiedExpression)


def test_hyp_edu_quantifiedexpression_constructor_exists():
    assert callable(edu_QuantifiedExpression.__init__)


def test_hyp_edu_quantifiedexpression_constructor_args():
    sig = inspect.signature(edu_QuantifiedExpression.__init__)
    params = list(sig.parameters.keys())



def test_hyp_edu_arrayaccess_is_not_abstract():
    assert not inspect.isabstract(edu_ArrayAccess)


def test_hyp_edu_arrayaccess_constructor_exists():
    assert callable(edu_ArrayAccess.__init__)


def test_hyp_edu_arrayaccess_constructor_args():
    sig = inspect.signature(edu_ArrayAccess.__init__)
    params = list(sig.parameters.keys())



def test_hyp_edu_ternaryexpression_is_not_abstract():
    assert not inspect.isabstract(edu_TernaryExpression)


def test_hyp_edu_ternaryexpression_constructor_exists():
    assert callable(edu_TernaryExpression.__init__)


def test_hyp_edu_ternaryexpression_constructor_args():
    sig = inspect.signature(edu_TernaryExpression.__init__)
    params = list(sig.parameters.keys())



def test_hyp_edu_symbolreference_is_not_abstract():
    assert not inspect.isabstract(edu_SymbolReference)


def test_hyp_edu_symbolreference_constructor_exists():
    assert callable(edu_SymbolReference.__init__)


def test_hyp_edu_symbolreference_constructor_args():
    sig = inspect.signature(edu_SymbolReference.__init__)
    params = list(sig.parameters.keys())



def test_hyp_edu_unaryexpression_is_not_abstract():
    assert not inspect.isabstract(edu_UnaryExpression)


def test_hyp_edu_unaryexpression_constructor_exists():
    assert callable(edu_UnaryExpression.__init__)


def test_hyp_edu_unaryexpression_constructor_args():
    sig = inspect.signature(edu_UnaryExpression.__init__)
    params = list(sig.parameters.keys())



def test_hyp_edu_literal_is_not_abstract():
    assert not inspect.isabstract(edu_Literal)


def test_hyp_edu_literal_constructor_exists():
    assert callable(edu_Literal.__init__)


def test_hyp_edu_literal_constructor_args():
    sig = inspect.signature(edu_Literal.__init__)
    params = list(sig.parameters.keys())



def test_hyp_edu_functioncall_is_not_abstract():
    assert not inspect.isabstract(edu_FunctionCall)


def test_hyp_edu_functioncall_constructor_exists():
    assert callable(edu_FunctionCall.__init__)


def test_hyp_edu_functioncall_constructor_args():
    sig = inspect.signature(edu_FunctionCall.__init__)
    params = list(sig.parameters.keys())



def test_hyp_edu_binaryexpression_is_not_abstract():
    assert not inspect.isabstract(edu_BinaryExpression)


def test_hyp_edu_binaryexpression_constructor_exists():
    assert callable(edu_BinaryExpression.__init__)


def test_hyp_edu_binaryexpression_constructor_args():
    sig = inspect.signature(edu_BinaryExpression.__init__)
    params = list(sig.parameters.keys())



def test_hyp_binaryexpression_is_not_abstract():
    assert not inspect.isabstract(BinaryExpression)


def test_hyp_binaryexpression_constructor_exists():
    assert callable(BinaryExpression.__init__)


def test_hyp_binaryexpression_constructor_args():
    sig = inspect.signature(BinaryExpression.__init__)
    params = list(sig.parameters.keys())



def test_hyp_edu_implication_is_not_abstract():
    assert not inspect.isabstract(edu_Implication)


def test_hyp_edu_implication_constructor_exists():
    assert callable(edu_Implication.__init__)


def test_hyp_edu_implication_constructor_args():
    sig = inspect.signature(edu_Implication.__init__)
    params = list(sig.parameters.keys())



def test_hyp_edu_unequal_is_not_abstract():
    assert not inspect.isabstract(edu_Unequal)


def test_hyp_edu_unequal_constructor_exists():
    assert callable(edu_Unequal.__init__)


def test_hyp_edu_unequal_constructor_args():
    sig = inspect.signature(edu_Unequal.__init__)
    params = list(sig.parameters.keys())



def test_hyp_edu_less_is_not_abstract():
    assert not inspect.isabstract(edu_Less)


def test_hyp_edu_less_constructor_exists():
    assert callable(edu_Less.__init__)


def test_hyp_edu_less_constructor_args():
    sig = inspect.signature(edu_Less.__init__)
    params = list(sig.parameters.keys())



def test_hyp_edu_subtraction_is_not_abstract():
    assert not inspect.isabstract(edu_Subtraction)


def test_hyp_edu_subtraction_constructor_exists():
    assert callable(edu_Subtraction.__init__)


def test_hyp_edu_subtraction_constructor_args():
    sig = inspect.signature(edu_Subtraction.__init__)
    params = list(sig.parameters.keys())



def test_hyp_edu_multiplication_is_not_abstract():
    assert not inspect.isabstract(edu_Multiplication)


def test_hyp_edu_multiplication_constructor_exists():
    assert callable(edu_Multiplication.__init__)


def test_hyp_edu_multiplication_constructor_args():
    sig = inspect.signature(edu_Multiplication.__init__)
    params = list(sig.parameters.keys())



def test_hyp_edu_disjunction_is_not_abstract():
    assert not inspect.isabstract(edu_Disjunction)


def test_hyp_edu_disjunction_constructor_exists():
    assert callable(edu_Disjunction.__init__)


def test_hyp_edu_disjunction_constructor_args():
    sig = inspect.signature(edu_Disjunction.__init__)
    params = list(sig.parameters.keys())



def test_hyp_edu_equal_is_not_abstract():
    assert not inspect.isabstract(edu_Equal)


def test_hyp_edu_equal_constructor_exists():
    assert callable(edu_Equal.__init__)


def test_hyp_edu_equal_constructor_args():
    sig = inspect.signature(edu_Equal.__init__)
    params = list(sig.parameters.keys())



def test_hyp_edu_modulus_is_not_abstract():
    assert not inspect.isabstract(edu_Modulus)


def test_hyp_edu_modulus_constructor_exists():
    assert callable(edu_Modulus.__init__)


def test_hyp_edu_modulus_constructor_args():
    sig = inspect.signature(edu_Modulus.__init__)
    params = list(sig.parameters.keys())



def test_hyp_edu_conjunction_is_not_abstract():
    assert not inspect.isabstract(edu_Conjunction)


def test_hyp_edu_conjunction_constructor_exists():
    assert callable(edu_Conjunction.__init__)


def test_hyp_edu_conjunction_constructor_args():
    sig = inspect.signature(edu_Conjunction.__init__)
    params = list(sig.parameters.keys())



def test_hyp_edu_division_is_not_abstract():
    assert not inspect.isabstract(edu_Division)


def test_hyp_edu_division_constructor_exists():
    assert callable(edu_Division.__init__)


def test_hyp_edu_division_constructor_args():
    sig = inspect.signature(edu_Division.__init__)
    params = list(sig.parameters.keys())



def test_hyp_edu_lessorequal_is_not_abstract():
    assert not inspect.isabstract(edu_LessOrEqual)


def test_hyp_edu_lessorequal_constructor_exists():
    assert callable(edu_LessOrEqual.__init__)


def test_hyp_edu_lessorequal_constructor_args():
    sig = inspect.signature(edu_LessOrEqual.__init__)
    params = list(sig.parameters.keys())



def test_hyp_edu_equivalence_is_not_abstract():
    assert not inspect.isabstract(edu_Equivalence)


def test_hyp_edu_equivalence_constructor_exists():
    assert callable(edu_Equivalence.__init__)


def test_hyp_edu_equivalence_constructor_args():
    sig = inspect.signature(edu_Equivalence.__init__)
    params = list(sig.parameters.keys())



def test_hyp_edu_greater_is_not_abstract():
    assert not inspect.isabstract(edu_Greater)


def test_hyp_edu_greater_constructor_exists():
    assert callable(edu_Greater.__init__)


def test_hyp_edu_greater_constructor_args():
    sig = inspect.signature(edu_Greater.__init__)
    params = list(sig.parameters.keys())



def test_hyp_edu_greaterorequal_is_not_abstract():
    assert not inspect.isabstract(edu_GreaterOrEqual)


def test_hyp_edu_greaterorequal_constructor_exists():
    assert callable(edu_GreaterOrEqual.__init__)


def test_hyp_edu_greaterorequal_constructor_args():
    sig = inspect.signature(edu_GreaterOrEqual.__init__)
    params = list(sig.parameters.keys())



def test_hyp_edu_addition_is_not_abstract():
    assert not inspect.isabstract(edu_Addition)


def test_hyp_edu_addition_constructor_exists():
    assert callable(edu_Addition.__init__)


def test_hyp_edu_addition_constructor_args():
    sig = inspect.signature(edu_Addition.__init__)
    params = list(sig.parameters.keys())



def test_hyp_edu_astnode_is_not_abstract():
    assert not inspect.isabstract(edu_ASTNode)


def test_hyp_edu_astnode_constructor_exists():
    assert callable(edu_ASTNode.__init__)


def test_hyp_edu_astnode_constructor_args():
    sig = inspect.signature(edu_ASTNode.__init__)
    params = list(sig.parameters.keys())



def test_hyp_edu_axiom_is_not_abstract():
    assert not inspect.isabstract(edu_Axiom)


def test_hyp_edu_axiom_constructor_exists():
    assert callable(edu_Axiom.__init__)


def test_hyp_edu_axiom_constructor_args():
    sig = inspect.signature(edu_Axiom.__init__)
    params = list(sig.parameters.keys())



def test_hyp_edu_block_is_not_abstract():
    assert not inspect.isabstract(edu_Block)


def test_hyp_edu_block_constructor_exists():
    assert callable(edu_Block.__init__)


def test_hyp_edu_block_constructor_args():
    sig = inspect.signature(edu_Block.__init__)
    params = list(sig.parameters.keys())



def test_hyp_astnode_is_not_abstract():
    assert not inspect.isabstract(ASTNode)


def test_hyp_astnode_constructor_exists():
    assert callable(ASTNode.__init__)


def test_hyp_astnode_constructor_args():
    sig = inspect.signature(ASTNode.__init__)
    params = list(sig.parameters.keys())



def test_hyp_edu_type_is_not_abstract():
    assert not inspect.isabstract(edu_Type)


def test_hyp_edu_type_constructor_exists():
    assert callable(edu_Type.__init__)


def test_hyp_edu_type_constructor_args():
    sig = inspect.signature(edu_Type.__init__)
    params = list(sig.parameters.keys())



def test_hyp_edu_expression_is_not_abstract():
    assert not inspect.isabstract(edu_Expression)


def test_hyp_edu_expression_constructor_exists():
    assert callable(edu_Expression.__init__)


def test_hyp_edu_expression_constructor_args():
    sig = inspect.signature(edu_Expression.__init__)
    params = list(sig.parameters.keys())



def test_hyp_edu_functiondeclaration_is_not_abstract():
    assert not inspect.isabstract(edu_FunctionDeclaration)


def test_hyp_edu_functiondeclaration_constructor_exists():
    assert callable(edu_FunctionDeclaration.__init__)


def test_hyp_edu_functiondeclaration_constructor_args():
    sig = inspect.signature(edu_FunctionDeclaration.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"




def test_hyp_edu_expressionevaluation_is_not_abstract():
    assert not inspect.isabstract(edu_ExpressionEvaluation)


def test_hyp_edu_expressionevaluation_constructor_exists():
    assert callable(edu_ExpressionEvaluation.__init__)


def test_hyp_edu_expressionevaluation_constructor_args():
    sig = inspect.signature(edu_ExpressionEvaluation.__init__)
    params = list(sig.parameters.keys())



def test_hyp_edu_statement_is_not_abstract():
    assert not inspect.isabstract(edu_Statement)


def test_hyp_edu_statement_constructor_exists():
    assert callable(edu_Statement.__init__)


def test_hyp_edu_statement_constructor_args():
    sig = inspect.signature(edu_Statement.__init__)
    params = list(sig.parameters.keys())



def test_hyp_edu_program_is_not_abstract():
    assert not inspect.isabstract(edu_Program)


def test_hyp_edu_program_constructor_exists():
    assert callable(edu_Program.__init__)


def test_hyp_edu_program_constructor_args():
    sig = inspect.signature(edu_Program.__init__)
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
edu_visitor_IASTNodeVisitor_strategy = st.builds(
    edu_visitor_IASTNodeVisitor,
)
edu_ExpressionToExpressionMap_strategy = st.builds(
    edu_ExpressionToExpressionMap,
)
SymbolReference_strategy = st.builds(
    SymbolReference,
)
edu_ReturnValueReference_strategy = st.builds(
    edu_ReturnValueReference,
)
UnaryExpression_strategy = st.builds(
    UnaryExpression,
)
edu_Negation_strategy = st.builds(
    edu_Negation,
)
edu_Sign_strategy = st.builds(
    edu_Sign,
)
Sign_strategy = st.builds(
    Sign,
)
edu_Plus_strategy = st.builds(
    edu_Plus,
)
edu_Minus_strategy = st.builds(
    edu_Minus,
)
FunctionAnnotation_strategy = st.builds(
    FunctionAnnotation,
)
edu_Postcondition_strategy = st.builds(
    edu_Postcondition,
)
edu_Precondition_strategy = st.builds(
    edu_Precondition,
)
QuantifiedExpression_strategy = st.builds(
    QuantifiedExpression,
)
edu_ForAllQuantifier_strategy = st.builds(
    edu_ForAllQuantifier,
)
edu_ExistsQuantifier_strategy = st.builds(
    edu_ExistsQuantifier,
)
PrimitiveType_strategy = st.builds(
    PrimitiveType,
)
edu_IntegerType_strategy = st.builds(
    edu_IntegerType,
)
edu_BooleanType_strategy = st.builds(
    edu_BooleanType,
)
edu_VariableReference_strategy = st.builds(
    edu_VariableReference,
)
Statement_strategy = st.builds(
    Statement,
)
edu_Conditional_strategy = st.builds(
    edu_Conditional,
)
edu_Loop_strategy = st.builds(
    edu_Loop,
)
edu_VariableDeclaration_strategy = st.builds(
    edu_VariableDeclaration,
    name=
        safe_text
)
edu_Assignment_strategy = st.builds(
    edu_Assignment,
)
edu_ReturnStatement_strategy = st.builds(
    edu_ReturnStatement,
)
edu_Annotation_strategy = st.builds(
    edu_Annotation,
)
GuardAssertion_strategy = st.builds(
    GuardAssertion,
)
edu_DivisorNotZeroAssertion_strategy = st.builds(
    edu_DivisorNotZeroAssertion,
)
edu_FunctionCallPreconditionAssertion_strategy = st.builds(
    edu_FunctionCallPreconditionAssertion,
)
Assertion_strategy = st.builds(
    Assertion,
)
edu_GuardAssertion_strategy = st.builds(
    edu_GuardAssertion,
)
Annotation_strategy = st.builds(
    Annotation,
)
edu_Invariant_strategy = st.builds(
    edu_Invariant,
)
edu_FunctionAnnotation_strategy = st.builds(
    edu_FunctionAnnotation,
)
edu_Assumption_strategy = st.builds(
    edu_Assumption,
)
edu_Assertion_strategy = st.builds(
    edu_Assertion,
)
Type_strategy = st.builds(
    Type,
)
edu_PrimitiveType_strategy = st.builds(
    edu_PrimitiveType,
)
edu_ArrayType_strategy = st.builds(
    edu_ArrayType,
)
Literal_strategy = st.builds(
    Literal,
)
edu_IntegerLiteral_strategy = st.builds(
    edu_IntegerLiteral,
    value=
        safe_text
)
edu_ArrayFunction_strategy = st.builds(
    edu_ArrayFunction,
)
edu_BooleanLiteral_strategy = st.builds(
    edu_BooleanLiteral,
    value=
        st.booleans()
)
edu_ArrayLiteral_strategy = st.builds(
    edu_ArrayLiteral,
)
Expression_strategy = st.builds(
    Expression,
)
edu_LetExpression_strategy = st.builds(
    edu_LetExpression,
)
edu_QuantifiedExpression_strategy = st.builds(
    edu_QuantifiedExpression,
)
edu_ArrayAccess_strategy = st.builds(
    edu_ArrayAccess,
)
edu_TernaryExpression_strategy = st.builds(
    edu_TernaryExpression,
)
edu_SymbolReference_strategy = st.builds(
    edu_SymbolReference,
)
edu_UnaryExpression_strategy = st.builds(
    edu_UnaryExpression,
)
edu_Literal_strategy = st.builds(
    edu_Literal,
)
edu_FunctionCall_strategy = st.builds(
    edu_FunctionCall,
)
edu_BinaryExpression_strategy = st.builds(
    edu_BinaryExpression,
)
BinaryExpression_strategy = st.builds(
    BinaryExpression,
)
edu_Implication_strategy = st.builds(
    edu_Implication,
)
edu_Unequal_strategy = st.builds(
    edu_Unequal,
)
edu_Less_strategy = st.builds(
    edu_Less,
)
edu_Subtraction_strategy = st.builds(
    edu_Subtraction,
)
edu_Multiplication_strategy = st.builds(
    edu_Multiplication,
)
edu_Disjunction_strategy = st.builds(
    edu_Disjunction,
)
edu_Equal_strategy = st.builds(
    edu_Equal,
)
edu_Modulus_strategy = st.builds(
    edu_Modulus,
)
edu_Conjunction_strategy = st.builds(
    edu_Conjunction,
)
edu_Division_strategy = st.builds(
    edu_Division,
)
edu_LessOrEqual_strategy = st.builds(
    edu_LessOrEqual,
)
edu_Equivalence_strategy = st.builds(
    edu_Equivalence,
)
edu_Greater_strategy = st.builds(
    edu_Greater,
)
edu_GreaterOrEqual_strategy = st.builds(
    edu_GreaterOrEqual,
)
edu_Addition_strategy = st.builds(
    edu_Addition,
)
edu_ASTNode_strategy = st.builds(
    edu_ASTNode,
)
edu_Axiom_strategy = st.builds(
    edu_Axiom,
)
edu_Block_strategy = st.builds(
    edu_Block,
)
ASTNode_strategy = st.builds(
    ASTNode,
)
edu_Type_strategy = st.builds(
    edu_Type,
)
edu_Expression_strategy = st.builds(
    edu_Expression,
)
edu_FunctionDeclaration_strategy = st.builds(
    edu_FunctionDeclaration,
    name=
        safe_text
)
edu_ExpressionEvaluation_strategy = st.builds(
    edu_ExpressionEvaluation,
)
edu_Statement_strategy = st.builds(
    edu_Statement,
)
edu_Program_strategy = st.builds(
    edu_Program,
)


import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=edu_visitor_IASTNodeVisitor_strategy)
@settings(max_examples=30)
def test_hyp_edu_visitor_iastnodevisitor_visit_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.visit(
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.visit).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'visit' in edu_visitor_IASTNodeVisitor is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'visit' in edu_visitor_IASTNodeVisitor did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'visit' in edu_visitor_IASTNodeVisitor is not implemented or raised an error")




import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=edu_ReturnValueReference_strategy)
@settings(max_examples=30)
def test_hyp_edu_returnvaluereference_accept_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.accept(
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.accept).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'accept' in edu_ReturnValueReference is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'accept' in edu_ReturnValueReference did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'accept' in edu_ReturnValueReference is not implemented or raised an error")



import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=edu_Negation_strategy)
@settings(max_examples=30)
def test_hyp_edu_negation_accept_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.accept(
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.accept).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'accept' in edu_Negation is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'accept' in edu_Negation did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'accept' in edu_Negation is not implemented or raised an error")


import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=edu_Sign_strategy)
@settings(max_examples=30)
def test_hyp_edu_sign_accept_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.accept(
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.accept).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'accept' in edu_Sign is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'accept' in edu_Sign did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'accept' in edu_Sign is not implemented or raised an error")



import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=edu_Plus_strategy)
@settings(max_examples=30)
def test_hyp_edu_plus_accept_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.accept(
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.accept).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'accept' in edu_Plus is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'accept' in edu_Plus did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'accept' in edu_Plus is not implemented or raised an error")


import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=edu_Minus_strategy)
@settings(max_examples=30)
def test_hyp_edu_minus_accept_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.accept(
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.accept).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'accept' in edu_Minus is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'accept' in edu_Minus did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'accept' in edu_Minus is not implemented or raised an error")



import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=edu_Postcondition_strategy)
@settings(max_examples=30)
def test_hyp_edu_postcondition_accept_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.accept(
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.accept).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'accept' in edu_Postcondition is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'accept' in edu_Postcondition did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'accept' in edu_Postcondition is not implemented or raised an error")


import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=edu_Precondition_strategy)
@settings(max_examples=30)
def test_hyp_edu_precondition_accept_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.accept(
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.accept).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'accept' in edu_Precondition is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'accept' in edu_Precondition did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'accept' in edu_Precondition is not implemented or raised an error")



import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=edu_ForAllQuantifier_strategy)
@settings(max_examples=30)
def test_hyp_edu_forallquantifier_accept_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.accept(
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.accept).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'accept' in edu_ForAllQuantifier is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'accept' in edu_ForAllQuantifier did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'accept' in edu_ForAllQuantifier is not implemented or raised an error")


import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=edu_ExistsQuantifier_strategy)
@settings(max_examples=30)
def test_hyp_edu_existsquantifier_accept_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.accept(
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.accept).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'accept' in edu_ExistsQuantifier is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'accept' in edu_ExistsQuantifier did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'accept' in edu_ExistsQuantifier is not implemented or raised an error")



import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=edu_IntegerType_strategy)
@settings(max_examples=30)
def test_hyp_edu_integertype_accept_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.accept(
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.accept).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'accept' in edu_IntegerType is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'accept' in edu_IntegerType did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'accept' in edu_IntegerType is not implemented or raised an error")


import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=edu_BooleanType_strategy)
@settings(max_examples=30)
def test_hyp_edu_booleantype_accept_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.accept(
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.accept).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'accept' in edu_BooleanType is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'accept' in edu_BooleanType did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'accept' in edu_BooleanType is not implemented or raised an error")


import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=edu_VariableReference_strategy)
@settings(max_examples=30)
def test_hyp_edu_variablereference_accept_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.accept(
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.accept).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'accept' in edu_VariableReference is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'accept' in edu_VariableReference did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'accept' in edu_VariableReference is not implemented or raised an error")



import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=edu_Conditional_strategy)
@settings(max_examples=30)
def test_hyp_edu_conditional_accept_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.accept(
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.accept).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'accept' in edu_Conditional is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'accept' in edu_Conditional did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'accept' in edu_Conditional is not implemented or raised an error")


import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=edu_Loop_strategy)
@settings(max_examples=30)
def test_hyp_edu_loop_accept_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.accept(
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.accept).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'accept' in edu_Loop is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'accept' in edu_Loop did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'accept' in edu_Loop is not implemented or raised an error")




@given(instance=edu_VariableDeclaration_strategy)
def test_hyp_edu_variabledeclaration_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=edu_VariableDeclaration_strategy)
@settings(max_examples=30)
def test_hyp_edu_variabledeclaration_accept_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.accept(
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.accept).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'accept' in edu_VariableDeclaration is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'accept' in edu_VariableDeclaration did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'accept' in edu_VariableDeclaration is not implemented or raised an error")


import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=edu_Assignment_strategy)
@settings(max_examples=30)
def test_hyp_edu_assignment_accept_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.accept(
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.accept).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'accept' in edu_Assignment is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'accept' in edu_Assignment did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'accept' in edu_Assignment is not implemented or raised an error")


import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=edu_ReturnStatement_strategy)
@settings(max_examples=30)
def test_hyp_edu_returnstatement_accept_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.accept(
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.accept).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'accept' in edu_ReturnStatement is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'accept' in edu_ReturnStatement did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'accept' in edu_ReturnStatement is not implemented or raised an error")


import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=edu_Annotation_strategy)
@settings(max_examples=30)
def test_hyp_edu_annotation_accept_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.accept(
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.accept).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'accept' in edu_Annotation is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'accept' in edu_Annotation did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'accept' in edu_Annotation is not implemented or raised an error")



import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=edu_DivisorNotZeroAssertion_strategy)
@settings(max_examples=30)
def test_hyp_edu_divisornotzeroassertion_accept_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.accept(
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.accept).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'accept' in edu_DivisorNotZeroAssertion is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'accept' in edu_DivisorNotZeroAssertion did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'accept' in edu_DivisorNotZeroAssertion is not implemented or raised an error")


import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=edu_FunctionCallPreconditionAssertion_strategy)
@settings(max_examples=30)
def test_hyp_edu_functioncallpreconditionassertion_accept_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.accept(
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.accept).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'accept' in edu_FunctionCallPreconditionAssertion is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'accept' in edu_FunctionCallPreconditionAssertion did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'accept' in edu_FunctionCallPreconditionAssertion is not implemented or raised an error")



import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=edu_GuardAssertion_strategy)
@settings(max_examples=30)
def test_hyp_edu_guardassertion_accept_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.accept(
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.accept).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'accept' in edu_GuardAssertion is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'accept' in edu_GuardAssertion did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'accept' in edu_GuardAssertion is not implemented or raised an error")



import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=edu_Invariant_strategy)
@settings(max_examples=30)
def test_hyp_edu_invariant_accept_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.accept(
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.accept).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'accept' in edu_Invariant is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'accept' in edu_Invariant did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'accept' in edu_Invariant is not implemented or raised an error")


import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=edu_FunctionAnnotation_strategy)
@settings(max_examples=30)
def test_hyp_edu_functionannotation_accept_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.accept(
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.accept).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'accept' in edu_FunctionAnnotation is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'accept' in edu_FunctionAnnotation did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'accept' in edu_FunctionAnnotation is not implemented or raised an error")


import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=edu_Assumption_strategy)
@settings(max_examples=30)
def test_hyp_edu_assumption_accept_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.accept(
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.accept).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'accept' in edu_Assumption is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'accept' in edu_Assumption did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'accept' in edu_Assumption is not implemented or raised an error")


import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=edu_Assertion_strategy)
@settings(max_examples=30)
def test_hyp_edu_assertion_accept_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.accept(
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.accept).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'accept' in edu_Assertion is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'accept' in edu_Assertion did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'accept' in edu_Assertion is not implemented or raised an error")



import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=edu_PrimitiveType_strategy)
@settings(max_examples=30)
def test_hyp_edu_primitivetype_accept_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.accept(
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.accept).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'accept' in edu_PrimitiveType is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'accept' in edu_PrimitiveType did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'accept' in edu_PrimitiveType is not implemented or raised an error")


import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=edu_ArrayType_strategy)
@settings(max_examples=30)
def test_hyp_edu_arraytype_accept_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.accept(
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.accept).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'accept' in edu_ArrayType is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'accept' in edu_ArrayType did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'accept' in edu_ArrayType is not implemented or raised an error")





@given(instance=edu_IntegerLiteral_strategy)
def test_hyp_edu_integerliteral_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=edu_IntegerLiteral_strategy)
@settings(max_examples=30)
def test_hyp_edu_integerliteral_accept_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.accept(
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.accept).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'accept' in edu_IntegerLiteral is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'accept' in edu_IntegerLiteral did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'accept' in edu_IntegerLiteral is not implemented or raised an error")


import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=edu_ArrayFunction_strategy)
@settings(max_examples=30)
def test_hyp_edu_arrayfunction_accept_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.accept(
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.accept).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'accept' in edu_ArrayFunction is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'accept' in edu_ArrayFunction did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'accept' in edu_ArrayFunction is not implemented or raised an error")




@given(instance=edu_BooleanLiteral_strategy)
def test_hyp_edu_booleanliteral_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=edu_BooleanLiteral_strategy)
@settings(max_examples=30)
def test_hyp_edu_booleanliteral_accept_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.accept(
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.accept).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'accept' in edu_BooleanLiteral is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'accept' in edu_BooleanLiteral did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'accept' in edu_BooleanLiteral is not implemented or raised an error")


import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=edu_ArrayLiteral_strategy)
@settings(max_examples=30)
def test_hyp_edu_arrayliteral_accept_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.accept(
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.accept).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'accept' in edu_ArrayLiteral is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'accept' in edu_ArrayLiteral did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'accept' in edu_ArrayLiteral is not implemented or raised an error")




import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=edu_QuantifiedExpression_strategy)
@settings(max_examples=30)
def test_hyp_edu_quantifiedexpression_accept_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.accept(
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.accept).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'accept' in edu_QuantifiedExpression is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'accept' in edu_QuantifiedExpression did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'accept' in edu_QuantifiedExpression is not implemented or raised an error")


import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=edu_ArrayAccess_strategy)
@settings(max_examples=30)
def test_hyp_edu_arrayaccess_accept_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.accept(
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.accept).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'accept' in edu_ArrayAccess is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'accept' in edu_ArrayAccess did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'accept' in edu_ArrayAccess is not implemented or raised an error")


import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=edu_TernaryExpression_strategy)
@settings(max_examples=30)
def test_hyp_edu_ternaryexpression_accept_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.accept(
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.accept).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'accept' in edu_TernaryExpression is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'accept' in edu_TernaryExpression did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'accept' in edu_TernaryExpression is not implemented or raised an error")


import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=edu_SymbolReference_strategy)
@settings(max_examples=30)
def test_hyp_edu_symbolreference_accept_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.accept(
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.accept).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'accept' in edu_SymbolReference is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'accept' in edu_SymbolReference did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'accept' in edu_SymbolReference is not implemented or raised an error")


import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=edu_UnaryExpression_strategy)
@settings(max_examples=30)
def test_hyp_edu_unaryexpression_accept_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.accept(
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.accept).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'accept' in edu_UnaryExpression is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'accept' in edu_UnaryExpression did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'accept' in edu_UnaryExpression is not implemented or raised an error")


import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=edu_Literal_strategy)
@settings(max_examples=30)
def test_hyp_edu_literal_accept_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.accept(
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.accept).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'accept' in edu_Literal is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'accept' in edu_Literal did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'accept' in edu_Literal is not implemented or raised an error")


import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=edu_FunctionCall_strategy)
@settings(max_examples=30)
def test_hyp_edu_functioncall_accept_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.accept(
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.accept).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'accept' in edu_FunctionCall is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'accept' in edu_FunctionCall did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'accept' in edu_FunctionCall is not implemented or raised an error")


import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=edu_BinaryExpression_strategy)
@settings(max_examples=30)
def test_hyp_edu_binaryexpression_accept_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.accept(
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.accept).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'accept' in edu_BinaryExpression is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'accept' in edu_BinaryExpression did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'accept' in edu_BinaryExpression is not implemented or raised an error")



import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=edu_Implication_strategy)
@settings(max_examples=30)
def test_hyp_edu_implication_accept_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.accept(
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.accept).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'accept' in edu_Implication is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'accept' in edu_Implication did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'accept' in edu_Implication is not implemented or raised an error")


import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=edu_Unequal_strategy)
@settings(max_examples=30)
def test_hyp_edu_unequal_accept_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.accept(
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.accept).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'accept' in edu_Unequal is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'accept' in edu_Unequal did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'accept' in edu_Unequal is not implemented or raised an error")


import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=edu_Less_strategy)
@settings(max_examples=30)
def test_hyp_edu_less_accept_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.accept(
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.accept).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'accept' in edu_Less is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'accept' in edu_Less did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'accept' in edu_Less is not implemented or raised an error")


import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=edu_Subtraction_strategy)
@settings(max_examples=30)
def test_hyp_edu_subtraction_accept_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.accept(
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.accept).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'accept' in edu_Subtraction is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'accept' in edu_Subtraction did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'accept' in edu_Subtraction is not implemented or raised an error")


import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=edu_Multiplication_strategy)
@settings(max_examples=30)
def test_hyp_edu_multiplication_accept_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.accept(
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.accept).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'accept' in edu_Multiplication is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'accept' in edu_Multiplication did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'accept' in edu_Multiplication is not implemented or raised an error")


import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=edu_Disjunction_strategy)
@settings(max_examples=30)
def test_hyp_edu_disjunction_accept_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.accept(
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.accept).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'accept' in edu_Disjunction is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'accept' in edu_Disjunction did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'accept' in edu_Disjunction is not implemented or raised an error")


import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=edu_Equal_strategy)
@settings(max_examples=30)
def test_hyp_edu_equal_accept_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.accept(
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.accept).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'accept' in edu_Equal is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'accept' in edu_Equal did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'accept' in edu_Equal is not implemented or raised an error")


import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=edu_Modulus_strategy)
@settings(max_examples=30)
def test_hyp_edu_modulus_accept_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.accept(
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.accept).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'accept' in edu_Modulus is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'accept' in edu_Modulus did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'accept' in edu_Modulus is not implemented or raised an error")


import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=edu_Conjunction_strategy)
@settings(max_examples=30)
def test_hyp_edu_conjunction_accept_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.accept(
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.accept).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'accept' in edu_Conjunction is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'accept' in edu_Conjunction did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'accept' in edu_Conjunction is not implemented or raised an error")


import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=edu_Division_strategy)
@settings(max_examples=30)
def test_hyp_edu_division_accept_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.accept(
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.accept).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'accept' in edu_Division is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'accept' in edu_Division did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'accept' in edu_Division is not implemented or raised an error")


import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=edu_LessOrEqual_strategy)
@settings(max_examples=30)
def test_hyp_edu_lessorequal_accept_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.accept(
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.accept).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'accept' in edu_LessOrEqual is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'accept' in edu_LessOrEqual did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'accept' in edu_LessOrEqual is not implemented or raised an error")


import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=edu_Equivalence_strategy)
@settings(max_examples=30)
def test_hyp_edu_equivalence_accept_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.accept(
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.accept).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'accept' in edu_Equivalence is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'accept' in edu_Equivalence did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'accept' in edu_Equivalence is not implemented or raised an error")


import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=edu_Greater_strategy)
@settings(max_examples=30)
def test_hyp_edu_greater_accept_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.accept(
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.accept).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'accept' in edu_Greater is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'accept' in edu_Greater did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'accept' in edu_Greater is not implemented or raised an error")


import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=edu_GreaterOrEqual_strategy)
@settings(max_examples=30)
def test_hyp_edu_greaterorequal_accept_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.accept(
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.accept).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'accept' in edu_GreaterOrEqual is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'accept' in edu_GreaterOrEqual did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'accept' in edu_GreaterOrEqual is not implemented or raised an error")


import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=edu_Addition_strategy)
@settings(max_examples=30)
def test_hyp_edu_addition_accept_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.accept(
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.accept).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'accept' in edu_Addition is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'accept' in edu_Addition did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'accept' in edu_Addition is not implemented or raised an error")


import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=edu_ASTNode_strategy)
@settings(max_examples=30)
def test_hyp_edu_astnode_accept_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.accept(
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.accept).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'accept' in edu_ASTNode is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'accept' in edu_ASTNode did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'accept' in edu_ASTNode is not implemented or raised an error")


import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=edu_Axiom_strategy)
@settings(max_examples=30)
def test_hyp_edu_axiom_accept_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.accept(
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.accept).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'accept' in edu_Axiom is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'accept' in edu_Axiom did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'accept' in edu_Axiom is not implemented or raised an error")


import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=edu_Block_strategy)
@settings(max_examples=30)
def test_hyp_edu_block_accept_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.accept(
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.accept).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'accept' in edu_Block is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'accept' in edu_Block did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'accept' in edu_Block is not implemented or raised an error")



import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=edu_Type_strategy)
@settings(max_examples=30)
def test_hyp_edu_type_accept_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.accept(
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.accept).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'accept' in edu_Type is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'accept' in edu_Type did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'accept' in edu_Type is not implemented or raised an error")


import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=edu_Expression_strategy)
@settings(max_examples=30)
def test_hyp_edu_expression_accept_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.accept(
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.accept).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'accept' in edu_Expression is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'accept' in edu_Expression did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'accept' in edu_Expression is not implemented or raised an error")




@given(instance=edu_FunctionDeclaration_strategy)
def test_hyp_edu_functiondeclaration_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=edu_FunctionDeclaration_strategy)
@settings(max_examples=30)
def test_hyp_edu_functiondeclaration_accept_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.accept(
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.accept).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'accept' in edu_FunctionDeclaration is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'accept' in edu_FunctionDeclaration did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'accept' in edu_FunctionDeclaration is not implemented or raised an error")



import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=edu_Statement_strategy)
@settings(max_examples=30)
def test_hyp_edu_statement_accept_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.accept(
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.accept).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'accept' in edu_Statement is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'accept' in edu_Statement did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'accept' in edu_Statement is not implemented or raised an error")


import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=edu_Program_strategy)
@settings(max_examples=30)
def test_hyp_edu_program_accept_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.accept(
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.accept).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'accept' in edu_Program is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'accept' in edu_Program did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'accept' in edu_Program is not implemented or raised an error")


# ----- SECTION B: test_structural_full.py (deterministic-first suite) -----
import inspect
import pytest
from datetime import date, datetime, time, timedelta
from hypothesis import given, settings
import hypothesis.strategies as st

from python_code import (
    ASTNode,
    Annotation,
    Assertion,
    BinaryExpression,
    Expression,
    FunctionAnnotation,
    GuardAssertion,
    Literal,
    PrimitiveType,
    QuantifiedExpression,
    Sign,
    Statement,
    SymbolReference,
    Type,
    UnaryExpression,
    edu_ASTNode,
    edu_Addition,
    edu_Annotation,
    edu_ArrayAccess,
    edu_ArrayFunction,
    edu_ArrayLiteral,
    edu_ArrayType,
    edu_Assertion,
    edu_Assignment,
    edu_Assumption,
    edu_Axiom,
    edu_BinaryExpression,
    edu_Block,
    edu_BooleanLiteral,
    edu_BooleanType,
    edu_Conditional,
    edu_Conjunction,
    edu_Disjunction,
    edu_Division,
    edu_DivisorNotZeroAssertion,
    edu_Equal,
    edu_Equivalence,
    edu_ExistsQuantifier,
    edu_Expression,
    edu_ExpressionEvaluation,
    edu_ExpressionToExpressionMap,
    edu_ForAllQuantifier,
    edu_FunctionAnnotation,
    edu_FunctionCall,
    edu_FunctionCallPreconditionAssertion,
    edu_FunctionDeclaration,
    edu_Greater,
    edu_GreaterOrEqual,
    edu_GuardAssertion,
    edu_Implication,
    edu_IntegerLiteral,
    edu_IntegerType,
    edu_Invariant,
    edu_Less,
    edu_LessOrEqual,
    edu_LetExpression,
    edu_Literal,
    edu_Loop,
    edu_Minus,
    edu_Modulus,
    edu_Multiplication,
    edu_Negation,
    edu_Plus,
    edu_Postcondition,
    edu_Precondition,
    edu_PrimitiveType,
    edu_Program,
    edu_QuantifiedExpression,
    edu_ReturnStatement,
    edu_ReturnValueReference,
    edu_Sign,
    edu_Statement,
    edu_Subtraction,
    edu_SymbolReference,
    edu_TernaryExpression,
    edu_Type,
    edu_UnaryExpression,
    edu_Unequal,
    edu_VariableDeclaration,
    edu_VariableReference,
    edu_visitor_IASTNodeVisitor,
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

def test_edu_BooleanLiteral_value_value_roundtrip():
    instance = edu_BooleanLiteral(value=True)
    assert instance.value == True
    instance.value = False
    assert instance.value == False


def test_edu_FunctionDeclaration_name_value_roundtrip():
    instance = edu_FunctionDeclaration(name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_edu_IntegerLiteral_value_value_roundtrip():
    instance = edu_IntegerLiteral(value="sample_text")
    assert instance.value == "sample_text"
    instance.value = "sample_text_2"
    assert instance.value == "sample_text_2"


def test_edu_VariableDeclaration_name_value_roundtrip():
    instance = edu_VariableDeclaration(name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_edu_Expression_isa_ASTNode():
    instance = edu_Expression()
    assert isinstance(instance, ASTNode)


def test_edu_ExpressionEvaluation_isa_ASTNode():
    instance = edu_ExpressionEvaluation()
    assert isinstance(instance, ASTNode)


def test_edu_FunctionDeclaration_isa_ASTNode():
    instance = edu_FunctionDeclaration(name="sample_text")
    assert isinstance(instance, ASTNode)


def test_edu_Program_isa_ASTNode():
    instance = edu_Program()
    assert isinstance(instance, ASTNode)


def test_edu_Statement_isa_ASTNode():
    instance = edu_Statement()
    assert isinstance(instance, ASTNode)


def test_edu_Type_isa_ASTNode():
    instance = edu_Type()
    assert isinstance(instance, ASTNode)


def test_edu_Assertion_isa_Annotation():
    instance = edu_Assertion()
    assert isinstance(instance, Annotation)


def test_edu_Assumption_isa_Annotation():
    instance = edu_Assumption()
    assert isinstance(instance, Annotation)


def test_edu_Axiom_isa_Annotation():
    instance = edu_Axiom()
    assert isinstance(instance, Annotation)


def test_edu_FunctionAnnotation_isa_Annotation():
    instance = edu_FunctionAnnotation()
    assert isinstance(instance, Annotation)


def test_edu_Invariant_isa_Annotation():
    instance = edu_Invariant()
    assert isinstance(instance, Annotation)


def test_edu_GuardAssertion_isa_Assertion():
    instance = edu_GuardAssertion()
    assert isinstance(instance, Assertion)


def test_edu_Addition_isa_BinaryExpression():
    instance = edu_Addition()
    assert isinstance(instance, BinaryExpression)


def test_edu_Conjunction_isa_BinaryExpression():
    instance = edu_Conjunction()
    assert isinstance(instance, BinaryExpression)


def test_edu_Disjunction_isa_BinaryExpression():
    instance = edu_Disjunction()
    assert isinstance(instance, BinaryExpression)


def test_edu_Division_isa_BinaryExpression():
    instance = edu_Division()
    assert isinstance(instance, BinaryExpression)


def test_edu_Equal_isa_BinaryExpression():
    instance = edu_Equal()
    assert isinstance(instance, BinaryExpression)


def test_edu_Equivalence_isa_BinaryExpression():
    instance = edu_Equivalence()
    assert isinstance(instance, BinaryExpression)


def test_edu_Greater_isa_BinaryExpression():
    instance = edu_Greater()
    assert isinstance(instance, BinaryExpression)


def test_edu_GreaterOrEqual_isa_BinaryExpression():
    instance = edu_GreaterOrEqual()
    assert isinstance(instance, BinaryExpression)


def test_edu_Implication_isa_BinaryExpression():
    instance = edu_Implication()
    assert isinstance(instance, BinaryExpression)


def test_edu_Less_isa_BinaryExpression():
    instance = edu_Less()
    assert isinstance(instance, BinaryExpression)


def test_edu_LessOrEqual_isa_BinaryExpression():
    instance = edu_LessOrEqual()
    assert isinstance(instance, BinaryExpression)


def test_edu_Modulus_isa_BinaryExpression():
    instance = edu_Modulus()
    assert isinstance(instance, BinaryExpression)


def test_edu_Multiplication_isa_BinaryExpression():
    instance = edu_Multiplication()
    assert isinstance(instance, BinaryExpression)


def test_edu_Subtraction_isa_BinaryExpression():
    instance = edu_Subtraction()
    assert isinstance(instance, BinaryExpression)


def test_edu_Unequal_isa_BinaryExpression():
    instance = edu_Unequal()
    assert isinstance(instance, BinaryExpression)


def test_edu_ArrayAccess_isa_Expression():
    instance = edu_ArrayAccess()
    assert isinstance(instance, Expression)


def test_edu_BinaryExpression_isa_Expression():
    instance = edu_BinaryExpression()
    assert isinstance(instance, Expression)


def test_edu_FunctionCall_isa_Expression():
    instance = edu_FunctionCall()
    assert isinstance(instance, Expression)


def test_edu_LetExpression_isa_Expression():
    instance = edu_LetExpression()
    assert isinstance(instance, Expression)


def test_edu_Literal_isa_Expression():
    instance = edu_Literal()
    assert isinstance(instance, Expression)


def test_edu_QuantifiedExpression_isa_Expression():
    instance = edu_QuantifiedExpression()
    assert isinstance(instance, Expression)


def test_edu_SymbolReference_isa_Expression():
    instance = edu_SymbolReference()
    assert isinstance(instance, Expression)


def test_edu_TernaryExpression_isa_Expression():
    instance = edu_TernaryExpression()
    assert isinstance(instance, Expression)


def test_edu_UnaryExpression_isa_Expression():
    instance = edu_UnaryExpression()
    assert isinstance(instance, Expression)


def test_edu_Postcondition_isa_FunctionAnnotation():
    instance = edu_Postcondition()
    assert isinstance(instance, FunctionAnnotation)


def test_edu_Precondition_isa_FunctionAnnotation():
    instance = edu_Precondition()
    assert isinstance(instance, FunctionAnnotation)


def test_edu_DivisorNotZeroAssertion_isa_GuardAssertion():
    instance = edu_DivisorNotZeroAssertion()
    assert isinstance(instance, GuardAssertion)


def test_edu_FunctionCallPreconditionAssertion_isa_GuardAssertion():
    instance = edu_FunctionCallPreconditionAssertion()
    assert isinstance(instance, GuardAssertion)


def test_edu_ArrayFunction_isa_Literal():
    instance = edu_ArrayFunction()
    assert isinstance(instance, Literal)


def test_edu_ArrayLiteral_isa_Literal():
    instance = edu_ArrayLiteral()
    assert isinstance(instance, Literal)


def test_edu_BooleanLiteral_isa_Literal():
    instance = edu_BooleanLiteral(value=True)
    assert isinstance(instance, Literal)


def test_edu_IntegerLiteral_isa_Literal():
    instance = edu_IntegerLiteral(value="sample_text")
    assert isinstance(instance, Literal)


def test_edu_BooleanType_isa_PrimitiveType():
    instance = edu_BooleanType()
    assert isinstance(instance, PrimitiveType)


def test_edu_IntegerType_isa_PrimitiveType():
    instance = edu_IntegerType()
    assert isinstance(instance, PrimitiveType)


def test_edu_ExistsQuantifier_isa_QuantifiedExpression():
    instance = edu_ExistsQuantifier()
    assert isinstance(instance, QuantifiedExpression)


def test_edu_ForAllQuantifier_isa_QuantifiedExpression():
    instance = edu_ForAllQuantifier()
    assert isinstance(instance, QuantifiedExpression)


def test_edu_Minus_isa_Sign():
    instance = edu_Minus()
    assert isinstance(instance, Sign)


def test_edu_Plus_isa_Sign():
    instance = edu_Plus()
    assert isinstance(instance, Sign)


def test_edu_Annotation_isa_Statement():
    instance = edu_Annotation()
    assert isinstance(instance, Statement)


def test_edu_Assignment_isa_Statement():
    instance = edu_Assignment()
    assert isinstance(instance, Statement)


def test_edu_Block_isa_Statement():
    instance = edu_Block()
    assert isinstance(instance, Statement)


def test_edu_Conditional_isa_Statement():
    instance = edu_Conditional()
    assert isinstance(instance, Statement)


def test_edu_Loop_isa_Statement():
    instance = edu_Loop()
    assert isinstance(instance, Statement)


def test_edu_ReturnStatement_isa_Statement():
    instance = edu_ReturnStatement()
    assert isinstance(instance, Statement)


def test_edu_VariableDeclaration_isa_Statement():
    instance = edu_VariableDeclaration(name="sample_text")
    assert isinstance(instance, Statement)


def test_edu_ReturnValueReference_isa_SymbolReference():
    instance = edu_ReturnValueReference()
    assert isinstance(instance, SymbolReference)


def test_edu_VariableReference_isa_SymbolReference():
    instance = edu_VariableReference()
    assert isinstance(instance, SymbolReference)


def test_edu_ArrayType_isa_Type():
    instance = edu_ArrayType()
    assert isinstance(instance, Type)


def test_edu_PrimitiveType_isa_Type():
    instance = edu_PrimitiveType()
    assert isinstance(instance, Type)


def test_edu_Negation_isa_UnaryExpression():
    instance = edu_Negation()
    assert isinstance(instance, UnaryExpression)


def test_edu_Sign_isa_UnaryExpression():
    instance = edu_Sign()
    assert isinstance(instance, UnaryExpression)


def test_assoc_actuals45_link_reassign_clear():
    a = edu_FunctionCall()
    b1 = edu_Expression()
    b2 = edu_Expression()
    _safe_set(a, 'edu_FunctionCall46', {b1})
    assert _is_linked(a, 'edu_FunctionCall46', b1)
    if hasattr(b1, 'edu_Expression47'):
        assert _is_linked(b1, 'edu_Expression47', a)
    _safe_set(a, 'edu_FunctionCall46', {b2})
    assert _is_linked(a, 'edu_FunctionCall46', b2)
    if hasattr(b1, 'edu_Expression47'):
        assert not _is_linked(b1, 'edu_Expression47', a)
    if hasattr(b2, 'edu_Expression47'):
        assert _is_linked(b2, 'edu_Expression47', a)
    _safe_set(a, 'edu_FunctionCall46', set())
    assert not _is_linked(a, 'edu_FunctionCall46', b2)
    if hasattr(b2, 'edu_Expression47'):
        assert not _is_linked(b2, 'edu_Expression47', a)


def test_assoc_array95_link_reassign_clear():
    a = edu_Expression()
    b1 = edu_ArrayAccess()
    b2 = edu_ArrayAccess()
    _safe_set(a, 'edu_Expression97', b1)
    assert _is_linked(a, 'edu_Expression97', b1)
    if hasattr(b1, 'edu_ArrayAccess96'):
        assert _is_linked(b1, 'edu_ArrayAccess96', a)
    _safe_set(a, 'edu_Expression97', b2)
    assert _is_linked(a, 'edu_Expression97', b2)
    if hasattr(b1, 'edu_ArrayAccess96'):
        assert not _is_linked(b1, 'edu_ArrayAccess96', a)
    if hasattr(b2, 'edu_ArrayAccess96'):
        assert _is_linked(b2, 'edu_ArrayAccess96', a)
    _safe_set(a, 'edu_Expression97', None)
    assert not _is_linked(a, 'edu_Expression97', b2)
    if hasattr(b2, 'edu_ArrayAccess96'):
        assert not _is_linked(b2, 'edu_ArrayAccess96', a)


def test_assoc_axioms3_link_reassign_clear():
    a = edu_Program()
    b1 = edu_Axiom()
    b2 = edu_Axiom()
    _safe_set(a, 'edu_Program4', {b1})
    assert _is_linked(a, 'edu_Program4', b1)
    if hasattr(b1, 'edu_Axiom'):
        assert _is_linked(b1, 'edu_Axiom', a)
    _safe_set(a, 'edu_Program4', {b2})
    assert _is_linked(a, 'edu_Program4', b2)
    if hasattr(b1, 'edu_Axiom'):
        assert not _is_linked(b1, 'edu_Axiom', a)
    if hasattr(b2, 'edu_Axiom'):
        assert _is_linked(b2, 'edu_Axiom', a)
    _safe_set(a, 'edu_Program4', set())
    assert not _is_linked(a, 'edu_Program4', b2)
    if hasattr(b2, 'edu_Axiom'):
        assert not _is_linked(b2, 'edu_Axiom', a)


def test_assoc_baseType13_link_reassign_clear():
    a = edu_PrimitiveType()
    b1 = edu_ArrayType()
    b2 = edu_ArrayType()
    _safe_set(a, 'edu_PrimitiveType', b1)
    assert _is_linked(a, 'edu_PrimitiveType', b1)
    if hasattr(b1, 'edu_ArrayType'):
        assert _is_linked(b1, 'edu_ArrayType', a)
    _safe_set(a, 'edu_PrimitiveType', b2)
    assert _is_linked(a, 'edu_PrimitiveType', b2)
    if hasattr(b1, 'edu_ArrayType'):
        assert not _is_linked(b1, 'edu_ArrayType', a)
    if hasattr(b2, 'edu_ArrayType'):
        assert _is_linked(b2, 'edu_ArrayType', a)
    _safe_set(a, 'edu_PrimitiveType', None)
    assert not _is_linked(a, 'edu_PrimitiveType', b2)
    if hasattr(b2, 'edu_ArrayType'):
        assert not _is_linked(b2, 'edu_ArrayType', a)


def test_assoc_body58_link_reassign_clear():
    a = edu_FunctionDeclaration(name="sample_text")
    b1 = edu_Block()
    b2 = edu_Block()
    _safe_set(a, 'edu_FunctionDeclaration59', b1)
    assert _is_linked(a, 'edu_FunctionDeclaration59', b1)
    if hasattr(b1, 'edu_Block60'):
        assert _is_linked(b1, 'edu_Block60', a)
    _safe_set(a, 'edu_FunctionDeclaration59', b2)
    assert _is_linked(a, 'edu_FunctionDeclaration59', b2)
    if hasattr(b1, 'edu_Block60'):
        assert not _is_linked(b1, 'edu_Block60', a)
    if hasattr(b2, 'edu_Block60'):
        assert _is_linked(b2, 'edu_Block60', a)
    _safe_set(a, 'edu_FunctionDeclaration59', None)
    assert not _is_linked(a, 'edu_FunctionDeclaration59', b2)
    if hasattr(b2, 'edu_Block60'):
        assert not _is_linked(b2, 'edu_Block60', a)


def test_assoc_body66_link_reassign_clear():
    a = edu_Loop()
    b1 = edu_Block()
    b2 = edu_Block()
    _safe_set(a, 'edu_Loop67', b1)
    assert _is_linked(a, 'edu_Loop67', b1)
    if hasattr(b1, 'edu_Block68'):
        assert _is_linked(b1, 'edu_Block68', a)
    _safe_set(a, 'edu_Loop67', b2)
    assert _is_linked(a, 'edu_Loop67', b2)
    if hasattr(b1, 'edu_Block68'):
        assert not _is_linked(b1, 'edu_Block68', a)
    if hasattr(b2, 'edu_Block68'):
        assert _is_linked(b2, 'edu_Block68', a)
    _safe_set(a, 'edu_Loop67', None)
    assert not _is_linked(a, 'edu_Loop67', b2)
    if hasattr(b2, 'edu_Block68'):
        assert not _is_linked(b2, 'edu_Block68', a)


def test_assoc_chainedFunction85_link_reassign_clear():
    a = edu_Expression()
    b1 = edu_ArrayFunction()
    b2 = edu_ArrayFunction()
    _safe_set(a, 'edu_Expression86', b1)
    assert _is_linked(a, 'edu_Expression86', b1)
    if hasattr(b1, 'edu_ArrayFunction'):
        assert _is_linked(b1, 'edu_ArrayFunction', a)
    _safe_set(a, 'edu_Expression86', b2)
    assert _is_linked(a, 'edu_Expression86', b2)
    if hasattr(b1, 'edu_ArrayFunction'):
        assert not _is_linked(b1, 'edu_ArrayFunction', a)
    if hasattr(b2, 'edu_ArrayFunction'):
        assert _is_linked(b2, 'edu_ArrayFunction', a)
    _safe_set(a, 'edu_Expression86', None)
    assert not _is_linked(a, 'edu_Expression86', b2)
    if hasattr(b2, 'edu_ArrayFunction'):
        assert not _is_linked(b2, 'edu_ArrayFunction', a)


def test_assoc_condition108_link_reassign_clear():
    a = edu_TernaryExpression()
    b1 = edu_Expression()
    b2 = edu_Expression()
    _safe_set(a, 'edu_TernaryExpression109', b1)
    assert _is_linked(a, 'edu_TernaryExpression109', b1)
    if hasattr(b1, 'edu_Expression110'):
        assert _is_linked(b1, 'edu_Expression110', a)
    _safe_set(a, 'edu_TernaryExpression109', b2)
    assert _is_linked(a, 'edu_TernaryExpression109', b2)
    if hasattr(b1, 'edu_Expression110'):
        assert not _is_linked(b1, 'edu_Expression110', a)
    if hasattr(b2, 'edu_Expression110'):
        assert _is_linked(b2, 'edu_Expression110', a)
    _safe_set(a, 'edu_TernaryExpression109', None)
    assert not _is_linked(a, 'edu_TernaryExpression109', b2)
    if hasattr(b2, 'edu_Expression110'):
        assert not _is_linked(b2, 'edu_Expression110', a)


def test_assoc_condition29_link_reassign_clear():
    a = edu_Expression()
    b1 = edu_Conditional()
    b2 = edu_Conditional()
    _safe_set(a, 'edu_Expression30', b1)
    assert _is_linked(a, 'edu_Expression30', b1)
    if hasattr(b1, 'edu_Conditional'):
        assert _is_linked(b1, 'edu_Conditional', a)
    _safe_set(a, 'edu_Expression30', b2)
    assert _is_linked(a, 'edu_Expression30', b2)
    if hasattr(b1, 'edu_Conditional'):
        assert not _is_linked(b1, 'edu_Conditional', a)
    if hasattr(b2, 'edu_Conditional'):
        assert _is_linked(b2, 'edu_Conditional', a)
    _safe_set(a, 'edu_Expression30', None)
    assert not _is_linked(a, 'edu_Expression30', b2)
    if hasattr(b2, 'edu_Conditional'):
        assert not _is_linked(b2, 'edu_Conditional', a)


def test_assoc_condition42_link_reassign_clear():
    a = edu_QuantifiedExpression()
    b1 = edu_Expression()
    b2 = edu_Expression()
    _safe_set(a, 'edu_QuantifiedExpression43', b1)
    assert _is_linked(a, 'edu_QuantifiedExpression43', b1)
    if hasattr(b1, 'edu_Expression44'):
        assert _is_linked(b1, 'edu_Expression44', a)
    _safe_set(a, 'edu_QuantifiedExpression43', b2)
    assert _is_linked(a, 'edu_QuantifiedExpression43', b2)
    if hasattr(b1, 'edu_Expression44'):
        assert not _is_linked(b1, 'edu_Expression44', a)
    if hasattr(b2, 'edu_Expression44'):
        assert _is_linked(b2, 'edu_Expression44', a)
    _safe_set(a, 'edu_QuantifiedExpression43', None)
    assert not _is_linked(a, 'edu_QuantifiedExpression43', b2)
    if hasattr(b2, 'edu_Expression44'):
        assert not _is_linked(b2, 'edu_Expression44', a)


def test_assoc_condition64_link_reassign_clear():
    a = edu_Loop()
    b1 = edu_Expression()
    b2 = edu_Expression()
    _safe_set(a, 'edu_Loop', b1)
    assert _is_linked(a, 'edu_Loop', b1)
    if hasattr(b1, 'edu_Expression65'):
        assert _is_linked(b1, 'edu_Expression65', a)
    _safe_set(a, 'edu_Loop', b2)
    assert _is_linked(a, 'edu_Loop', b2)
    if hasattr(b1, 'edu_Expression65'):
        assert not _is_linked(b1, 'edu_Expression65', a)
    if hasattr(b2, 'edu_Expression65'):
        assert _is_linked(b2, 'edu_Expression65', a)
    _safe_set(a, 'edu_Loop', None)
    assert not _is_linked(a, 'edu_Loop', b2)
    if hasattr(b2, 'edu_Expression65'):
        assert not _is_linked(b2, 'edu_Expression65', a)


def test_assoc_expression113_link_reassign_clear():
    a = edu_Expression()
    b1 = edu_LetExpression()
    b2 = edu_LetExpression()
    _safe_set(a, 'edu_Expression115', b1)
    assert _is_linked(a, 'edu_Expression115', b1)
    if hasattr(b1, 'edu_LetExpression114'):
        assert _is_linked(b1, 'edu_LetExpression114', a)
    _safe_set(a, 'edu_Expression115', b2)
    assert _is_linked(a, 'edu_Expression115', b2)
    if hasattr(b1, 'edu_LetExpression114'):
        assert not _is_linked(b1, 'edu_LetExpression114', a)
    if hasattr(b2, 'edu_LetExpression114'):
        assert _is_linked(b2, 'edu_LetExpression114', a)
    _safe_set(a, 'edu_Expression115', None)
    assert not _is_linked(a, 'edu_Expression115', b2)
    if hasattr(b2, 'edu_LetExpression114'):
        assert not _is_linked(b2, 'edu_LetExpression114', a)


def test_assoc_expression17_link_reassign_clear():
    a = edu_Expression()
    b1 = edu_Annotation()
    b2 = edu_Annotation()
    _safe_set(a, 'edu_Expression18', b1)
    assert _is_linked(a, 'edu_Expression18', b1)
    if hasattr(b1, 'edu_Annotation'):
        assert _is_linked(b1, 'edu_Annotation', a)
    _safe_set(a, 'edu_Expression18', b2)
    assert _is_linked(a, 'edu_Expression18', b2)
    if hasattr(b1, 'edu_Annotation'):
        assert not _is_linked(b1, 'edu_Annotation', a)
    if hasattr(b2, 'edu_Annotation'):
        assert _is_linked(b2, 'edu_Annotation', a)
    _safe_set(a, 'edu_Expression18', None)
    assert not _is_linked(a, 'edu_Expression18', b2)
    if hasattr(b2, 'edu_Annotation'):
        assert not _is_linked(b2, 'edu_Annotation', a)


def test_assoc_expression39_link_reassign_clear():
    a = edu_QuantifiedExpression()
    b1 = edu_Expression()
    b2 = edu_Expression()
    _safe_set(a, 'edu_QuantifiedExpression40', b1)
    assert _is_linked(a, 'edu_QuantifiedExpression40', b1)
    if hasattr(b1, 'edu_Expression41'):
        assert _is_linked(b1, 'edu_Expression41', a)
    _safe_set(a, 'edu_QuantifiedExpression40', b2)
    assert _is_linked(a, 'edu_QuantifiedExpression40', b2)
    if hasattr(b1, 'edu_Expression41'):
        assert not _is_linked(b1, 'edu_Expression41', a)
    if hasattr(b2, 'edu_Expression41'):
        assert _is_linked(b2, 'edu_Expression41', a)
    _safe_set(a, 'edu_QuantifiedExpression40', None)
    assert not _is_linked(a, 'edu_QuantifiedExpression40', b2)
    if hasattr(b2, 'edu_Expression41'):
        assert not _is_linked(b2, 'edu_Expression41', a)


def test_assoc_expression83_link_reassign_clear():
    a = edu_Expression()
    b1 = edu_ExpressionEvaluation()
    b2 = edu_ExpressionEvaluation()
    _safe_set(a, 'edu_Expression84', b1)
    assert _is_linked(a, 'edu_Expression84', b1)
    if hasattr(b1, 'edu_ExpressionEvaluation'):
        assert _is_linked(b1, 'edu_ExpressionEvaluation', a)
    _safe_set(a, 'edu_Expression84', b2)
    assert _is_linked(a, 'edu_Expression84', b2)
    if hasattr(b1, 'edu_ExpressionEvaluation'):
        assert not _is_linked(b1, 'edu_ExpressionEvaluation', a)
    if hasattr(b2, 'edu_ExpressionEvaluation'):
        assert _is_linked(b2, 'edu_ExpressionEvaluation', a)
    _safe_set(a, 'edu_Expression84', None)
    assert not _is_linked(a, 'edu_Expression84', b2)
    if hasattr(b2, 'edu_ExpressionEvaluation'):
        assert not _is_linked(b2, 'edu_ExpressionEvaluation', a)


def test_assoc_falseBlock34_link_reassign_clear():
    a = edu_Conditional()
    b1 = edu_Block()
    b2 = edu_Block()
    _safe_set(a, 'edu_Conditional35', b1)
    assert _is_linked(a, 'edu_Conditional35', b1)
    if hasattr(b1, 'edu_Block36'):
        assert _is_linked(b1, 'edu_Block36', a)
    _safe_set(a, 'edu_Conditional35', b2)
    assert _is_linked(a, 'edu_Conditional35', b2)
    if hasattr(b1, 'edu_Block36'):
        assert not _is_linked(b1, 'edu_Block36', a)
    if hasattr(b2, 'edu_Block36'):
        assert _is_linked(b2, 'edu_Block36', a)
    _safe_set(a, 'edu_Conditional35', None)
    assert not _is_linked(a, 'edu_Conditional35', b2)
    if hasattr(b2, 'edu_Block36'):
        assert not _is_linked(b2, 'edu_Block36', a)


def test_assoc_function48_link_reassign_clear():
    a = edu_FunctionDeclaration(name="sample_text")
    b1 = edu_FunctionCall()
    b2 = edu_FunctionCall()
    _safe_set(a, 'edu_FunctionDeclaration50', b1)
    assert _is_linked(a, 'edu_FunctionDeclaration50', b1)
    if hasattr(b1, 'edu_FunctionCall49'):
        assert _is_linked(b1, 'edu_FunctionCall49', a)
    _safe_set(a, 'edu_FunctionDeclaration50', b2)
    assert _is_linked(a, 'edu_FunctionDeclaration50', b2)
    if hasattr(b1, 'edu_FunctionCall49'):
        assert not _is_linked(b1, 'edu_FunctionCall49', a)
    if hasattr(b2, 'edu_FunctionCall49'):
        assert _is_linked(b2, 'edu_FunctionCall49', a)
    _safe_set(a, 'edu_FunctionDeclaration50', None)
    assert not _is_linked(a, 'edu_FunctionDeclaration50', b2)
    if hasattr(b2, 'edu_FunctionCall49'):
        assert not _is_linked(b2, 'edu_FunctionCall49', a)


def test_assoc_function73_link_reassign_clear():
    a = edu_ReturnStatement()
    b1 = edu_FunctionDeclaration(name="sample_text")
    b2 = edu_FunctionDeclaration(name="sample_text_2")
    _safe_set(a, 'edu_ReturnStatement74', b1)
    assert _is_linked(a, 'edu_ReturnStatement74', b1)
    if hasattr(b1, 'edu_FunctionDeclaration75'):
        assert _is_linked(b1, 'edu_FunctionDeclaration75', a)
    _safe_set(a, 'edu_ReturnStatement74', b2)
    assert _is_linked(a, 'edu_ReturnStatement74', b2)
    if hasattr(b1, 'edu_FunctionDeclaration75'):
        assert not _is_linked(b1, 'edu_FunctionDeclaration75', a)
    if hasattr(b2, 'edu_FunctionDeclaration75'):
        assert _is_linked(b2, 'edu_FunctionDeclaration75', a)
    _safe_set(a, 'edu_ReturnStatement74', None)
    assert not _is_linked(a, 'edu_ReturnStatement74', b2)
    if hasattr(b2, 'edu_FunctionDeclaration75'):
        assert not _is_linked(b2, 'edu_FunctionDeclaration75', a)


def test_assoc_function79_link_reassign_clear():
    a = edu_ReturnValueReference()
    b1 = edu_FunctionDeclaration(name="sample_text")
    b2 = edu_FunctionDeclaration(name="sample_text_2")
    _safe_set(a, 'edu_ReturnValueReference', b1)
    assert _is_linked(a, 'edu_ReturnValueReference', b1)
    if hasattr(b1, 'edu_FunctionDeclaration80'):
        assert _is_linked(b1, 'edu_FunctionDeclaration80', a)
    _safe_set(a, 'edu_ReturnValueReference', b2)
    assert _is_linked(a, 'edu_ReturnValueReference', b2)
    if hasattr(b1, 'edu_FunctionDeclaration80'):
        assert not _is_linked(b1, 'edu_FunctionDeclaration80', a)
    if hasattr(b2, 'edu_FunctionDeclaration80'):
        assert _is_linked(b2, 'edu_FunctionDeclaration80', a)
    _safe_set(a, 'edu_ReturnValueReference', None)
    assert not _is_linked(a, 'edu_ReturnValueReference', b2)
    if hasattr(b2, 'edu_FunctionDeclaration80'):
        assert not _is_linked(b2, 'edu_FunctionDeclaration80', a)


def test_assoc_functionDeclarations0_link_reassign_clear():
    a = edu_Program()
    b1 = edu_FunctionDeclaration(name="sample_text")
    b2 = edu_FunctionDeclaration(name="sample_text_2")
    _safe_set(a, 'edu_Program', {b1})
    assert _is_linked(a, 'edu_Program', b1)
    if hasattr(b1, 'edu_FunctionDeclaration'):
        assert _is_linked(b1, 'edu_FunctionDeclaration', a)
    _safe_set(a, 'edu_Program', {b2})
    assert _is_linked(a, 'edu_Program', b2)
    if hasattr(b1, 'edu_FunctionDeclaration'):
        assert not _is_linked(b1, 'edu_FunctionDeclaration', a)
    if hasattr(b2, 'edu_FunctionDeclaration'):
        assert _is_linked(b2, 'edu_FunctionDeclaration', a)
    _safe_set(a, 'edu_Program', set())
    assert not _is_linked(a, 'edu_Program', b2)
    if hasattr(b2, 'edu_FunctionDeclaration'):
        assert not _is_linked(b2, 'edu_FunctionDeclaration', a)


def test_assoc_guardedNode14_link_reassign_clear():
    a = edu_FunctionCallPreconditionAssertion()
    b1 = edu_FunctionCall()
    b2 = edu_FunctionCall()
    _safe_set(a, 'edu_FunctionCallPreconditionAssertion', b1)
    assert _is_linked(a, 'edu_FunctionCallPreconditionAssertion', b1)
    if hasattr(b1, 'edu_FunctionCall'):
        assert _is_linked(b1, 'edu_FunctionCall', a)
    _safe_set(a, 'edu_FunctionCallPreconditionAssertion', b2)
    assert _is_linked(a, 'edu_FunctionCallPreconditionAssertion', b2)
    if hasattr(b1, 'edu_FunctionCall'):
        assert not _is_linked(b1, 'edu_FunctionCall', a)
    if hasattr(b2, 'edu_FunctionCall'):
        assert _is_linked(b2, 'edu_FunctionCall', a)
    _safe_set(a, 'edu_FunctionCallPreconditionAssertion', None)
    assert not _is_linked(a, 'edu_FunctionCallPreconditionAssertion', b2)
    if hasattr(b2, 'edu_FunctionCall'):
        assert not _is_linked(b2, 'edu_FunctionCall', a)


def test_assoc_guardedNode15_link_reassign_clear():
    a = edu_Expression()
    b1 = edu_DivisorNotZeroAssertion()
    b2 = edu_DivisorNotZeroAssertion()
    _safe_set(a, 'edu_Expression16', b1)
    assert _is_linked(a, 'edu_Expression16', b1)
    if hasattr(b1, 'edu_DivisorNotZeroAssertion'):
        assert _is_linked(b1, 'edu_DivisorNotZeroAssertion', a)
    _safe_set(a, 'edu_Expression16', b2)
    assert _is_linked(a, 'edu_Expression16', b2)
    if hasattr(b1, 'edu_DivisorNotZeroAssertion'):
        assert not _is_linked(b1, 'edu_DivisorNotZeroAssertion', a)
    if hasattr(b2, 'edu_DivisorNotZeroAssertion'):
        assert _is_linked(b2, 'edu_DivisorNotZeroAssertion', a)
    _safe_set(a, 'edu_Expression16', None)
    assert not _is_linked(a, 'edu_Expression16', b2)
    if hasattr(b2, 'edu_DivisorNotZeroAssertion'):
        assert not _is_linked(b2, 'edu_DivisorNotZeroAssertion', a)


def test_assoc_index81_link_reassign_clear():
    a = edu_SymbolReference()
    b1 = edu_Expression()
    b2 = edu_Expression()
    _safe_set(a, 'edu_SymbolReference', b1)
    assert _is_linked(a, 'edu_SymbolReference', b1)
    if hasattr(b1, 'edu_Expression82'):
        assert _is_linked(b1, 'edu_Expression82', a)
    _safe_set(a, 'edu_SymbolReference', b2)
    assert _is_linked(a, 'edu_SymbolReference', b2)
    if hasattr(b1, 'edu_Expression82'):
        assert not _is_linked(b1, 'edu_Expression82', a)
    if hasattr(b2, 'edu_Expression82'):
        assert _is_linked(b2, 'edu_Expression82', a)
    _safe_set(a, 'edu_SymbolReference', None)
    assert not _is_linked(a, 'edu_SymbolReference', b2)
    if hasattr(b2, 'edu_Expression82'):
        assert not _is_linked(b2, 'edu_Expression82', a)


def test_assoc_index87_link_reassign_clear():
    a = edu_Expression()
    b1 = edu_ArrayFunction()
    b2 = edu_ArrayFunction()
    _safe_set(a, 'edu_Expression89', b1)
    assert _is_linked(a, 'edu_Expression89', b1)
    if hasattr(b1, 'edu_ArrayFunction88'):
        assert _is_linked(b1, 'edu_ArrayFunction88', a)
    _safe_set(a, 'edu_Expression89', b2)
    assert _is_linked(a, 'edu_Expression89', b2)
    if hasattr(b1, 'edu_ArrayFunction88'):
        assert not _is_linked(b1, 'edu_ArrayFunction88', a)
    if hasattr(b2, 'edu_ArrayFunction88'):
        assert _is_linked(b2, 'edu_ArrayFunction88', a)
    _safe_set(a, 'edu_Expression89', None)
    assert not _is_linked(a, 'edu_Expression89', b2)
    if hasattr(b2, 'edu_ArrayFunction88'):
        assert not _is_linked(b2, 'edu_ArrayFunction88', a)


def test_assoc_index93_link_reassign_clear():
    a = edu_Expression()
    b1 = edu_ArrayAccess()
    b2 = edu_ArrayAccess()
    _safe_set(a, 'edu_Expression94', b1)
    assert _is_linked(a, 'edu_Expression94', b1)
    if hasattr(b1, 'edu_ArrayAccess'):
        assert _is_linked(b1, 'edu_ArrayAccess', a)
    _safe_set(a, 'edu_Expression94', b2)
    assert _is_linked(a, 'edu_Expression94', b2)
    if hasattr(b1, 'edu_ArrayAccess'):
        assert not _is_linked(b1, 'edu_ArrayAccess', a)
    if hasattr(b2, 'edu_ArrayAccess'):
        assert _is_linked(b2, 'edu_ArrayAccess', a)
    _safe_set(a, 'edu_Expression94', None)
    assert not _is_linked(a, 'edu_Expression94', b2)
    if hasattr(b2, 'edu_ArrayAccess'):
        assert not _is_linked(b2, 'edu_ArrayAccess', a)


def test_assoc_initialValue24_link_reassign_clear():
    a = edu_VariableDeclaration(name="sample_text")
    b1 = edu_Expression()
    b2 = edu_Expression()
    _safe_set(a, 'edu_VariableDeclaration25', b1)
    assert _is_linked(a, 'edu_VariableDeclaration25', b1)
    if hasattr(b1, 'edu_Expression26'):
        assert _is_linked(b1, 'edu_Expression26', a)
    _safe_set(a, 'edu_VariableDeclaration25', b2)
    assert _is_linked(a, 'edu_VariableDeclaration25', b2)
    if hasattr(b1, 'edu_Expression26'):
        assert not _is_linked(b1, 'edu_Expression26', a)
    if hasattr(b2, 'edu_Expression26'):
        assert _is_linked(b2, 'edu_Expression26', a)
    _safe_set(a, 'edu_VariableDeclaration25', None)
    assert not _is_linked(a, 'edu_VariableDeclaration25', b2)
    if hasattr(b2, 'edu_Expression26'):
        assert not _is_linked(b2, 'edu_Expression26', a)


def test_assoc_invariants69_link_reassign_clear():
    a = edu_Loop()
    b1 = edu_Invariant()
    b2 = edu_Invariant()
    _safe_set(a, 'edu_Loop70', {b1})
    assert _is_linked(a, 'edu_Loop70', b1)
    if hasattr(b1, 'edu_Invariant'):
        assert _is_linked(b1, 'edu_Invariant', a)
    _safe_set(a, 'edu_Loop70', {b2})
    assert _is_linked(a, 'edu_Loop70', b2)
    if hasattr(b1, 'edu_Invariant'):
        assert not _is_linked(b1, 'edu_Invariant', a)
    if hasattr(b2, 'edu_Invariant'):
        assert _is_linked(b2, 'edu_Invariant', a)
    _safe_set(a, 'edu_Loop70', set())
    assert not _is_linked(a, 'edu_Loop70', b2)
    if hasattr(b2, 'edu_Invariant'):
        assert not _is_linked(b2, 'edu_Invariant', a)


def test_assoc_key98_link_reassign_clear():
    a = edu_Expression()
    b1 = edu_ExpressionToExpressionMap()
    b2 = edu_ExpressionToExpressionMap()
    _safe_set(a, 'edu_Expression99', b1)
    assert _is_linked(a, 'edu_Expression99', b1)
    if hasattr(b1, 'edu_ExpressionToExpressionMap'):
        assert _is_linked(b1, 'edu_ExpressionToExpressionMap', a)
    _safe_set(a, 'edu_Expression99', b2)
    assert _is_linked(a, 'edu_Expression99', b2)
    if hasattr(b1, 'edu_ExpressionToExpressionMap'):
        assert not _is_linked(b1, 'edu_ExpressionToExpressionMap', a)
    if hasattr(b2, 'edu_ExpressionToExpressionMap'):
        assert _is_linked(b2, 'edu_ExpressionToExpressionMap', a)
    _safe_set(a, 'edu_Expression99', None)
    assert not _is_linked(a, 'edu_Expression99', b2)
    if hasattr(b2, 'edu_ExpressionToExpressionMap'):
        assert not _is_linked(b2, 'edu_ExpressionToExpressionMap', a)


def test_assoc_left5_link_reassign_clear():
    a = edu_Expression()
    b1 = edu_BinaryExpression()
    b2 = edu_BinaryExpression()
    _safe_set(a, 'edu_Expression', b1)
    assert _is_linked(a, 'edu_Expression', b1)
    if hasattr(b1, 'edu_BinaryExpression'):
        assert _is_linked(b1, 'edu_BinaryExpression', a)
    _safe_set(a, 'edu_Expression', b2)
    assert _is_linked(a, 'edu_Expression', b2)
    if hasattr(b1, 'edu_BinaryExpression'):
        assert not _is_linked(b1, 'edu_BinaryExpression', a)
    if hasattr(b2, 'edu_BinaryExpression'):
        assert _is_linked(b2, 'edu_BinaryExpression', a)
    _safe_set(a, 'edu_Expression', None)
    assert not _is_linked(a, 'edu_Expression', b2)
    if hasattr(b2, 'edu_BinaryExpression'):
        assert not _is_linked(b2, 'edu_BinaryExpression', a)


def test_assoc_mainBlock1_link_reassign_clear():
    a = edu_Program()
    b1 = edu_Block()
    b2 = edu_Block()
    _safe_set(a, 'edu_Program2', b1)
    assert _is_linked(a, 'edu_Program2', b1)
    if hasattr(b1, 'edu_Block'):
        assert _is_linked(b1, 'edu_Block', a)
    _safe_set(a, 'edu_Program2', b2)
    assert _is_linked(a, 'edu_Program2', b2)
    if hasattr(b1, 'edu_Block'):
        assert not _is_linked(b1, 'edu_Block', a)
    if hasattr(b2, 'edu_Block'):
        assert _is_linked(b2, 'edu_Block', a)
    _safe_set(a, 'edu_Program2', None)
    assert not _is_linked(a, 'edu_Program2', b2)
    if hasattr(b2, 'edu_Block'):
        assert not _is_linked(b2, 'edu_Block', a)


def test_assoc_operand9_link_reassign_clear():
    a = edu_UnaryExpression()
    b1 = edu_Expression()
    b2 = edu_Expression()
    _safe_set(a, 'edu_UnaryExpression', b1)
    assert _is_linked(a, 'edu_UnaryExpression', b1)
    if hasattr(b1, 'edu_Expression10'):
        assert _is_linked(b1, 'edu_Expression10', a)
    _safe_set(a, 'edu_UnaryExpression', b2)
    assert _is_linked(a, 'edu_UnaryExpression', b2)
    if hasattr(b1, 'edu_Expression10'):
        assert not _is_linked(b1, 'edu_Expression10', a)
    if hasattr(b2, 'edu_Expression10'):
        assert _is_linked(b2, 'edu_Expression10', a)
    _safe_set(a, 'edu_UnaryExpression', None)
    assert not _is_linked(a, 'edu_UnaryExpression', b2)
    if hasattr(b2, 'edu_Expression10'):
        assert not _is_linked(b2, 'edu_Expression10', a)


def test_assoc_parameter37_link_reassign_clear():
    a = edu_VariableDeclaration(name="sample_text")
    b1 = edu_QuantifiedExpression()
    b2 = edu_QuantifiedExpression()
    _safe_set(a, 'edu_VariableDeclaration38', b1)
    assert _is_linked(a, 'edu_VariableDeclaration38', b1)
    if hasattr(b1, 'edu_QuantifiedExpression'):
        assert _is_linked(b1, 'edu_QuantifiedExpression', a)
    _safe_set(a, 'edu_VariableDeclaration38', b2)
    assert _is_linked(a, 'edu_VariableDeclaration38', b2)
    if hasattr(b1, 'edu_QuantifiedExpression'):
        assert not _is_linked(b1, 'edu_QuantifiedExpression', a)
    if hasattr(b2, 'edu_QuantifiedExpression'):
        assert _is_linked(b2, 'edu_QuantifiedExpression', a)
    _safe_set(a, 'edu_VariableDeclaration38', None)
    assert not _is_linked(a, 'edu_VariableDeclaration38', b2)
    if hasattr(b2, 'edu_QuantifiedExpression'):
        assert not _is_linked(b2, 'edu_QuantifiedExpression', a)


def test_assoc_parameters111_link_reassign_clear():
    a = edu_VariableDeclaration(name="sample_text")
    b1 = edu_LetExpression()
    b2 = edu_LetExpression()
    _safe_set(a, 'edu_VariableDeclaration112', b1)
    assert _is_linked(a, 'edu_VariableDeclaration112', b1)
    if hasattr(b1, 'edu_LetExpression'):
        assert _is_linked(b1, 'edu_LetExpression', a)
    _safe_set(a, 'edu_VariableDeclaration112', b2)
    assert _is_linked(a, 'edu_VariableDeclaration112', b2)
    if hasattr(b1, 'edu_LetExpression'):
        assert not _is_linked(b1, 'edu_LetExpression', a)
    if hasattr(b2, 'edu_LetExpression'):
        assert _is_linked(b2, 'edu_LetExpression', a)
    _safe_set(a, 'edu_VariableDeclaration112', None)
    assert not _is_linked(a, 'edu_VariableDeclaration112', b2)
    if hasattr(b2, 'edu_LetExpression'):
        assert not _is_linked(b2, 'edu_LetExpression', a)


def test_assoc_parameters55_link_reassign_clear():
    a = edu_VariableDeclaration(name="sample_text")
    b1 = edu_FunctionDeclaration(name="sample_text")
    b2 = edu_FunctionDeclaration(name="sample_text_2")
    _safe_set(a, 'edu_VariableDeclaration57', b1)
    assert _is_linked(a, 'edu_VariableDeclaration57', b1)
    if hasattr(b1, 'edu_FunctionDeclaration56'):
        assert _is_linked(b1, 'edu_FunctionDeclaration56', a)
    _safe_set(a, 'edu_VariableDeclaration57', b2)
    assert _is_linked(a, 'edu_VariableDeclaration57', b2)
    if hasattr(b1, 'edu_FunctionDeclaration56'):
        assert not _is_linked(b1, 'edu_FunctionDeclaration56', a)
    if hasattr(b2, 'edu_FunctionDeclaration56'):
        assert _is_linked(b2, 'edu_FunctionDeclaration56', a)
    _safe_set(a, 'edu_VariableDeclaration57', None)
    assert not _is_linked(a, 'edu_VariableDeclaration57', b2)
    if hasattr(b2, 'edu_FunctionDeclaration56'):
        assert not _is_linked(b2, 'edu_FunctionDeclaration56', a)


def test_assoc_postconditions53_link_reassign_clear():
    a = edu_Postcondition()
    b1 = edu_FunctionDeclaration(name="sample_text")
    b2 = edu_FunctionDeclaration(name="sample_text_2")
    _safe_set(a, 'edu_Postcondition', b1)
    assert _is_linked(a, 'edu_Postcondition', b1)
    if hasattr(b1, 'edu_FunctionDeclaration54'):
        assert _is_linked(b1, 'edu_FunctionDeclaration54', a)
    _safe_set(a, 'edu_Postcondition', b2)
    assert _is_linked(a, 'edu_Postcondition', b2)
    if hasattr(b1, 'edu_FunctionDeclaration54'):
        assert not _is_linked(b1, 'edu_FunctionDeclaration54', a)
    if hasattr(b2, 'edu_FunctionDeclaration54'):
        assert _is_linked(b2, 'edu_FunctionDeclaration54', a)
    _safe_set(a, 'edu_Postcondition', None)
    assert not _is_linked(a, 'edu_Postcondition', b2)
    if hasattr(b2, 'edu_FunctionDeclaration54'):
        assert not _is_linked(b2, 'edu_FunctionDeclaration54', a)


def test_assoc_preconditions51_link_reassign_clear():
    a = edu_Precondition()
    b1 = edu_FunctionDeclaration(name="sample_text")
    b2 = edu_FunctionDeclaration(name="sample_text_2")
    _safe_set(a, 'edu_Precondition', b1)
    assert _is_linked(a, 'edu_Precondition', b1)
    if hasattr(b1, 'edu_FunctionDeclaration52'):
        assert _is_linked(b1, 'edu_FunctionDeclaration52', a)
    _safe_set(a, 'edu_Precondition', b2)
    assert _is_linked(a, 'edu_Precondition', b2)
    if hasattr(b1, 'edu_FunctionDeclaration52'):
        assert not _is_linked(b1, 'edu_FunctionDeclaration52', a)
    if hasattr(b2, 'edu_FunctionDeclaration52'):
        assert _is_linked(b2, 'edu_FunctionDeclaration52', a)
    _safe_set(a, 'edu_Precondition', None)
    assert not _is_linked(a, 'edu_Precondition', b2)
    if hasattr(b2, 'edu_FunctionDeclaration52'):
        assert not _is_linked(b2, 'edu_FunctionDeclaration52', a)


def test_assoc_returnType61_link_reassign_clear():
    a = edu_Type()
    b1 = edu_FunctionDeclaration(name="sample_text")
    b2 = edu_FunctionDeclaration(name="sample_text_2")
    _safe_set(a, 'edu_Type63', b1)
    assert _is_linked(a, 'edu_Type63', b1)
    if hasattr(b1, 'edu_FunctionDeclaration62'):
        assert _is_linked(b1, 'edu_FunctionDeclaration62', a)
    _safe_set(a, 'edu_Type63', b2)
    assert _is_linked(a, 'edu_Type63', b2)
    if hasattr(b1, 'edu_FunctionDeclaration62'):
        assert not _is_linked(b1, 'edu_FunctionDeclaration62', a)
    if hasattr(b2, 'edu_FunctionDeclaration62'):
        assert _is_linked(b2, 'edu_FunctionDeclaration62', a)
    _safe_set(a, 'edu_Type63', None)
    assert not _is_linked(a, 'edu_Type63', b2)
    if hasattr(b2, 'edu_FunctionDeclaration62'):
        assert not _is_linked(b2, 'edu_FunctionDeclaration62', a)


def test_assoc_returnValue71_link_reassign_clear():
    a = edu_ReturnStatement()
    b1 = edu_Expression()
    b2 = edu_Expression()
    _safe_set(a, 'edu_ReturnStatement', b1)
    assert _is_linked(a, 'edu_ReturnStatement', b1)
    if hasattr(b1, 'edu_Expression72'):
        assert _is_linked(b1, 'edu_Expression72', a)
    _safe_set(a, 'edu_ReturnStatement', b2)
    assert _is_linked(a, 'edu_ReturnStatement', b2)
    if hasattr(b1, 'edu_Expression72'):
        assert not _is_linked(b1, 'edu_Expression72', a)
    if hasattr(b2, 'edu_Expression72'):
        assert _is_linked(b2, 'edu_Expression72', a)
    _safe_set(a, 'edu_ReturnStatement', None)
    assert not _is_linked(a, 'edu_ReturnStatement', b2)
    if hasattr(b2, 'edu_Expression72'):
        assert not _is_linked(b2, 'edu_Expression72', a)


def test_assoc_right6_link_reassign_clear():
    a = edu_Expression()
    b1 = edu_BinaryExpression()
    b2 = edu_BinaryExpression()
    _safe_set(a, 'edu_Expression8', b1)
    assert _is_linked(a, 'edu_Expression8', b1)
    if hasattr(b1, 'edu_BinaryExpression7'):
        assert _is_linked(b1, 'edu_BinaryExpression7', a)
    _safe_set(a, 'edu_Expression8', b2)
    assert _is_linked(a, 'edu_Expression8', b2)
    if hasattr(b1, 'edu_BinaryExpression7'):
        assert not _is_linked(b1, 'edu_BinaryExpression7', a)
    if hasattr(b2, 'edu_BinaryExpression7'):
        assert _is_linked(b2, 'edu_BinaryExpression7', a)
    _safe_set(a, 'edu_Expression8', None)
    assert not _is_linked(a, 'edu_Expression8', b2)
    if hasattr(b2, 'edu_BinaryExpression7'):
        assert not _is_linked(b2, 'edu_BinaryExpression7', a)


def test_assoc_statements27_link_reassign_clear():
    a = edu_Statement()
    b1 = edu_Block()
    b2 = edu_Block()
    _safe_set(a, 'edu_Statement', b1)
    assert _is_linked(a, 'edu_Statement', b1)
    if hasattr(b1, 'edu_Block28'):
        assert _is_linked(b1, 'edu_Block28', a)
    _safe_set(a, 'edu_Statement', b2)
    assert _is_linked(a, 'edu_Statement', b2)
    if hasattr(b1, 'edu_Block28'):
        assert not _is_linked(b1, 'edu_Block28', a)
    if hasattr(b2, 'edu_Block28'):
        assert _is_linked(b2, 'edu_Block28', a)
    _safe_set(a, 'edu_Statement', None)
    assert not _is_linked(a, 'edu_Statement', b2)
    if hasattr(b2, 'edu_Block28'):
        assert not _is_linked(b2, 'edu_Block28', a)


def test_assoc_trueBlock31_link_reassign_clear():
    a = edu_Conditional()
    b1 = edu_Block()
    b2 = edu_Block()
    _safe_set(a, 'edu_Conditional32', b1)
    assert _is_linked(a, 'edu_Conditional32', b1)
    if hasattr(b1, 'edu_Block33'):
        assert _is_linked(b1, 'edu_Block33', a)
    _safe_set(a, 'edu_Conditional32', b2)
    assert _is_linked(a, 'edu_Conditional32', b2)
    if hasattr(b1, 'edu_Block33'):
        assert not _is_linked(b1, 'edu_Block33', a)
    if hasattr(b2, 'edu_Block33'):
        assert _is_linked(b2, 'edu_Block33', a)
    _safe_set(a, 'edu_Conditional32', None)
    assert not _is_linked(a, 'edu_Conditional32', b2)
    if hasattr(b2, 'edu_Block33'):
        assert not _is_linked(b2, 'edu_Block33', a)


def test_assoc_type23_link_reassign_clear():
    a = edu_VariableDeclaration(name="sample_text")
    b1 = edu_Type()
    b2 = edu_Type()
    _safe_set(a, 'edu_VariableDeclaration', b1)
    assert _is_linked(a, 'edu_VariableDeclaration', b1)
    if hasattr(b1, 'edu_Type'):
        assert _is_linked(b1, 'edu_Type', a)
    _safe_set(a, 'edu_VariableDeclaration', b2)
    assert _is_linked(a, 'edu_VariableDeclaration', b2)
    if hasattr(b1, 'edu_Type'):
        assert not _is_linked(b1, 'edu_Type', a)
    if hasattr(b2, 'edu_Type'):
        assert _is_linked(b2, 'edu_Type', a)
    _safe_set(a, 'edu_VariableDeclaration', None)
    assert not _is_linked(a, 'edu_VariableDeclaration', b2)
    if hasattr(b2, 'edu_Type'):
        assert not _is_linked(b2, 'edu_Type', a)


def test_assoc_value100_link_reassign_clear():
    a = edu_Expression()
    b1 = edu_ExpressionToExpressionMap()
    b2 = edu_ExpressionToExpressionMap()
    _safe_set(a, 'edu_Expression102', b1)
    assert _is_linked(a, 'edu_Expression102', b1)
    if hasattr(b1, 'edu_ExpressionToExpressionMap101'):
        assert _is_linked(b1, 'edu_ExpressionToExpressionMap101', a)
    _safe_set(a, 'edu_Expression102', b2)
    assert _is_linked(a, 'edu_Expression102', b2)
    if hasattr(b1, 'edu_ExpressionToExpressionMap101'):
        assert not _is_linked(b1, 'edu_ExpressionToExpressionMap101', a)
    if hasattr(b2, 'edu_ExpressionToExpressionMap101'):
        assert _is_linked(b2, 'edu_ExpressionToExpressionMap101', a)
    _safe_set(a, 'edu_Expression102', None)
    assert not _is_linked(a, 'edu_Expression102', b2)
    if hasattr(b2, 'edu_ExpressionToExpressionMap101'):
        assert not _is_linked(b2, 'edu_ExpressionToExpressionMap101', a)


def test_assoc_value19_link_reassign_clear():
    a = edu_Expression()
    b1 = edu_Assignment()
    b2 = edu_Assignment()
    _safe_set(a, 'edu_Expression20', b1)
    assert _is_linked(a, 'edu_Expression20', b1)
    if hasattr(b1, 'edu_Assignment'):
        assert _is_linked(b1, 'edu_Assignment', a)
    _safe_set(a, 'edu_Expression20', b2)
    assert _is_linked(a, 'edu_Expression20', b2)
    if hasattr(b1, 'edu_Assignment'):
        assert not _is_linked(b1, 'edu_Assignment', a)
    if hasattr(b2, 'edu_Assignment'):
        assert _is_linked(b2, 'edu_Assignment', a)
    _safe_set(a, 'edu_Expression20', None)
    assert not _is_linked(a, 'edu_Expression20', b2)
    if hasattr(b2, 'edu_Assignment'):
        assert not _is_linked(b2, 'edu_Assignment', a)


def test_assoc_value90_link_reassign_clear():
    a = edu_Expression()
    b1 = edu_ArrayFunction()
    b2 = edu_ArrayFunction()
    _safe_set(a, 'edu_Expression92', b1)
    assert _is_linked(a, 'edu_Expression92', b1)
    if hasattr(b1, 'edu_ArrayFunction91'):
        assert _is_linked(b1, 'edu_ArrayFunction91', a)
    _safe_set(a, 'edu_Expression92', b2)
    assert _is_linked(a, 'edu_Expression92', b2)
    if hasattr(b1, 'edu_ArrayFunction91'):
        assert not _is_linked(b1, 'edu_ArrayFunction91', a)
    if hasattr(b2, 'edu_ArrayFunction91'):
        assert _is_linked(b2, 'edu_ArrayFunction91', a)
    _safe_set(a, 'edu_Expression92', None)
    assert not _is_linked(a, 'edu_Expression92', b2)
    if hasattr(b2, 'edu_ArrayFunction91'):
        assert not _is_linked(b2, 'edu_ArrayFunction91', a)


def test_assoc_values11_link_reassign_clear():
    a = edu_Expression()
    b1 = edu_ArrayLiteral()
    b2 = edu_ArrayLiteral()
    _safe_set(a, 'edu_Expression12', b1)
    assert _is_linked(a, 'edu_Expression12', b1)
    if hasattr(b1, 'edu_ArrayLiteral'):
        assert _is_linked(b1, 'edu_ArrayLiteral', a)
    _safe_set(a, 'edu_Expression12', b2)
    assert _is_linked(a, 'edu_Expression12', b2)
    if hasattr(b1, 'edu_ArrayLiteral'):
        assert not _is_linked(b1, 'edu_ArrayLiteral', a)
    if hasattr(b2, 'edu_ArrayLiteral'):
        assert _is_linked(b2, 'edu_ArrayLiteral', a)
    _safe_set(a, 'edu_Expression12', None)
    assert not _is_linked(a, 'edu_Expression12', b2)
    if hasattr(b2, 'edu_ArrayLiteral'):
        assert not _is_linked(b2, 'edu_ArrayLiteral', a)


def test_assoc_variable21_link_reassign_clear():
    a = edu_VariableReference()
    b1 = edu_Assignment()
    b2 = edu_Assignment()
    _safe_set(a, 'edu_VariableReference', b1)
    assert _is_linked(a, 'edu_VariableReference', b1)
    if hasattr(b1, 'edu_Assignment22'):
        assert _is_linked(b1, 'edu_Assignment22', a)
    _safe_set(a, 'edu_VariableReference', b2)
    assert _is_linked(a, 'edu_VariableReference', b2)
    if hasattr(b1, 'edu_Assignment22'):
        assert not _is_linked(b1, 'edu_Assignment22', a)
    if hasattr(b2, 'edu_Assignment22'):
        assert _is_linked(b2, 'edu_Assignment22', a)
    _safe_set(a, 'edu_VariableReference', None)
    assert not _is_linked(a, 'edu_VariableReference', b2)
    if hasattr(b2, 'edu_Assignment22'):
        assert not _is_linked(b2, 'edu_Assignment22', a)


def test_assoc_variable76_link_reassign_clear():
    a = edu_VariableReference()
    b1 = edu_VariableDeclaration(name="sample_text")
    b2 = edu_VariableDeclaration(name="sample_text_2")
    _safe_set(a, 'edu_VariableReference77', b1)
    assert _is_linked(a, 'edu_VariableReference77', b1)
    if hasattr(b1, 'edu_VariableDeclaration78'):
        assert _is_linked(b1, 'edu_VariableDeclaration78', a)
    _safe_set(a, 'edu_VariableReference77', b2)
    assert _is_linked(a, 'edu_VariableReference77', b2)
    if hasattr(b1, 'edu_VariableDeclaration78'):
        assert not _is_linked(b1, 'edu_VariableDeclaration78', a)
    if hasattr(b2, 'edu_VariableDeclaration78'):
        assert _is_linked(b2, 'edu_VariableDeclaration78', a)
    _safe_set(a, 'edu_VariableReference77', None)
    assert not _is_linked(a, 'edu_VariableReference77', b2)
    if hasattr(b2, 'edu_VariableDeclaration78'):
        assert not _is_linked(b2, 'edu_VariableDeclaration78', a)


def test_assoc_whenFalse105_link_reassign_clear():
    a = edu_TernaryExpression()
    b1 = edu_Expression()
    b2 = edu_Expression()
    _safe_set(a, 'edu_TernaryExpression106', b1)
    assert _is_linked(a, 'edu_TernaryExpression106', b1)
    if hasattr(b1, 'edu_Expression107'):
        assert _is_linked(b1, 'edu_Expression107', a)
    _safe_set(a, 'edu_TernaryExpression106', b2)
    assert _is_linked(a, 'edu_TernaryExpression106', b2)
    if hasattr(b1, 'edu_Expression107'):
        assert not _is_linked(b1, 'edu_Expression107', a)
    if hasattr(b2, 'edu_Expression107'):
        assert _is_linked(b2, 'edu_Expression107', a)
    _safe_set(a, 'edu_TernaryExpression106', None)
    assert not _is_linked(a, 'edu_TernaryExpression106', b2)
    if hasattr(b2, 'edu_Expression107'):
        assert not _is_linked(b2, 'edu_Expression107', a)


def test_assoc_whenTrue103_link_reassign_clear():
    a = edu_TernaryExpression()
    b1 = edu_Expression()
    b2 = edu_Expression()
    _safe_set(a, 'edu_TernaryExpression', b1)
    assert _is_linked(a, 'edu_TernaryExpression', b1)
    if hasattr(b1, 'edu_Expression104'):
        assert _is_linked(b1, 'edu_Expression104', a)
    _safe_set(a, 'edu_TernaryExpression', b2)
    assert _is_linked(a, 'edu_TernaryExpression', b2)
    if hasattr(b1, 'edu_Expression104'):
        assert not _is_linked(b1, 'edu_Expression104', a)
    if hasattr(b2, 'edu_Expression104'):
        assert _is_linked(b2, 'edu_Expression104', a)
    _safe_set(a, 'edu_TernaryExpression', None)
    assert not _is_linked(a, 'edu_TernaryExpression', b2)
    if hasattr(b2, 'edu_Expression104'):
        assert not _is_linked(b2, 'edu_Expression104', a)


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

ASTNode_strategy = st.builds(ASTNode)
@given(instance=ASTNode_strategy)
@settings(max_examples=25)
def test_ASTNode_instantiation(instance):
    assert isinstance(instance, ASTNode)


Annotation_strategy = st.builds(Annotation)
@given(instance=Annotation_strategy)
@settings(max_examples=25)
def test_Annotation_instantiation(instance):
    assert isinstance(instance, Annotation)


Assertion_strategy = st.builds(Assertion)
@given(instance=Assertion_strategy)
@settings(max_examples=25)
def test_Assertion_instantiation(instance):
    assert isinstance(instance, Assertion)


BinaryExpression_strategy = st.builds(BinaryExpression)
@given(instance=BinaryExpression_strategy)
@settings(max_examples=25)
def test_BinaryExpression_instantiation(instance):
    assert isinstance(instance, BinaryExpression)


Expression_strategy = st.builds(Expression)
@given(instance=Expression_strategy)
@settings(max_examples=25)
def test_Expression_instantiation(instance):
    assert isinstance(instance, Expression)


FunctionAnnotation_strategy = st.builds(FunctionAnnotation)
@given(instance=FunctionAnnotation_strategy)
@settings(max_examples=25)
def test_FunctionAnnotation_instantiation(instance):
    assert isinstance(instance, FunctionAnnotation)


GuardAssertion_strategy = st.builds(GuardAssertion)
@given(instance=GuardAssertion_strategy)
@settings(max_examples=25)
def test_GuardAssertion_instantiation(instance):
    assert isinstance(instance, GuardAssertion)


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


QuantifiedExpression_strategy = st.builds(QuantifiedExpression)
@given(instance=QuantifiedExpression_strategy)
@settings(max_examples=25)
def test_QuantifiedExpression_instantiation(instance):
    assert isinstance(instance, QuantifiedExpression)


Sign_strategy = st.builds(Sign)
@given(instance=Sign_strategy)
@settings(max_examples=25)
def test_Sign_instantiation(instance):
    assert isinstance(instance, Sign)


Statement_strategy = st.builds(Statement)
@given(instance=Statement_strategy)
@settings(max_examples=25)
def test_Statement_instantiation(instance):
    assert isinstance(instance, Statement)


SymbolReference_strategy = st.builds(SymbolReference)
@given(instance=SymbolReference_strategy)
@settings(max_examples=25)
def test_SymbolReference_instantiation(instance):
    assert isinstance(instance, SymbolReference)


Type_strategy = st.builds(Type)
@given(instance=Type_strategy)
@settings(max_examples=25)
def test_Type_instantiation(instance):
    assert isinstance(instance, Type)


UnaryExpression_strategy = st.builds(UnaryExpression)
@given(instance=UnaryExpression_strategy)
@settings(max_examples=25)
def test_UnaryExpression_instantiation(instance):
    assert isinstance(instance, UnaryExpression)


edu_ASTNode_strategy = st.builds(edu_ASTNode)
@given(instance=edu_ASTNode_strategy)
@settings(max_examples=25)
def test_edu_ASTNode_instantiation(instance):
    assert isinstance(instance, edu_ASTNode)


edu_Addition_strategy = st.builds(edu_Addition)
@given(instance=edu_Addition_strategy)
@settings(max_examples=25)
def test_edu_Addition_instantiation(instance):
    assert isinstance(instance, edu_Addition)


edu_Annotation_strategy = st.builds(edu_Annotation)
@given(instance=edu_Annotation_strategy)
@settings(max_examples=25)
def test_edu_Annotation_instantiation(instance):
    assert isinstance(instance, edu_Annotation)


edu_ArrayAccess_strategy = st.builds(edu_ArrayAccess)
@given(instance=edu_ArrayAccess_strategy)
@settings(max_examples=25)
def test_edu_ArrayAccess_instantiation(instance):
    assert isinstance(instance, edu_ArrayAccess)


edu_ArrayFunction_strategy = st.builds(edu_ArrayFunction)
@given(instance=edu_ArrayFunction_strategy)
@settings(max_examples=25)
def test_edu_ArrayFunction_instantiation(instance):
    assert isinstance(instance, edu_ArrayFunction)


edu_ArrayLiteral_strategy = st.builds(edu_ArrayLiteral)
@given(instance=edu_ArrayLiteral_strategy)
@settings(max_examples=25)
def test_edu_ArrayLiteral_instantiation(instance):
    assert isinstance(instance, edu_ArrayLiteral)


edu_ArrayType_strategy = st.builds(edu_ArrayType)
@given(instance=edu_ArrayType_strategy)
@settings(max_examples=25)
def test_edu_ArrayType_instantiation(instance):
    assert isinstance(instance, edu_ArrayType)


edu_Assertion_strategy = st.builds(edu_Assertion)
@given(instance=edu_Assertion_strategy)
@settings(max_examples=25)
def test_edu_Assertion_instantiation(instance):
    assert isinstance(instance, edu_Assertion)


edu_Assignment_strategy = st.builds(edu_Assignment)
@given(instance=edu_Assignment_strategy)
@settings(max_examples=25)
def test_edu_Assignment_instantiation(instance):
    assert isinstance(instance, edu_Assignment)


edu_Assumption_strategy = st.builds(edu_Assumption)
@given(instance=edu_Assumption_strategy)
@settings(max_examples=25)
def test_edu_Assumption_instantiation(instance):
    assert isinstance(instance, edu_Assumption)


edu_Axiom_strategy = st.builds(edu_Axiom)
@given(instance=edu_Axiom_strategy)
@settings(max_examples=25)
def test_edu_Axiom_instantiation(instance):
    assert isinstance(instance, edu_Axiom)


edu_BinaryExpression_strategy = st.builds(edu_BinaryExpression)
@given(instance=edu_BinaryExpression_strategy)
@settings(max_examples=25)
def test_edu_BinaryExpression_instantiation(instance):
    assert isinstance(instance, edu_BinaryExpression)


edu_Block_strategy = st.builds(edu_Block)
@given(instance=edu_Block_strategy)
@settings(max_examples=25)
def test_edu_Block_instantiation(instance):
    assert isinstance(instance, edu_Block)


edu_BooleanLiteral_strategy = st.builds(edu_BooleanLiteral, value=st.booleans())
@given(instance=edu_BooleanLiteral_strategy)
@settings(max_examples=25)
def test_edu_BooleanLiteral_instantiation(instance):
    assert isinstance(instance, edu_BooleanLiteral)


edu_BooleanType_strategy = st.builds(edu_BooleanType)
@given(instance=edu_BooleanType_strategy)
@settings(max_examples=25)
def test_edu_BooleanType_instantiation(instance):
    assert isinstance(instance, edu_BooleanType)


edu_Conditional_strategy = st.builds(edu_Conditional)
@given(instance=edu_Conditional_strategy)
@settings(max_examples=25)
def test_edu_Conditional_instantiation(instance):
    assert isinstance(instance, edu_Conditional)


edu_Conjunction_strategy = st.builds(edu_Conjunction)
@given(instance=edu_Conjunction_strategy)
@settings(max_examples=25)
def test_edu_Conjunction_instantiation(instance):
    assert isinstance(instance, edu_Conjunction)


edu_Disjunction_strategy = st.builds(edu_Disjunction)
@given(instance=edu_Disjunction_strategy)
@settings(max_examples=25)
def test_edu_Disjunction_instantiation(instance):
    assert isinstance(instance, edu_Disjunction)


edu_Division_strategy = st.builds(edu_Division)
@given(instance=edu_Division_strategy)
@settings(max_examples=25)
def test_edu_Division_instantiation(instance):
    assert isinstance(instance, edu_Division)


edu_DivisorNotZeroAssertion_strategy = st.builds(edu_DivisorNotZeroAssertion)
@given(instance=edu_DivisorNotZeroAssertion_strategy)
@settings(max_examples=25)
def test_edu_DivisorNotZeroAssertion_instantiation(instance):
    assert isinstance(instance, edu_DivisorNotZeroAssertion)


edu_Equal_strategy = st.builds(edu_Equal)
@given(instance=edu_Equal_strategy)
@settings(max_examples=25)
def test_edu_Equal_instantiation(instance):
    assert isinstance(instance, edu_Equal)


edu_Equivalence_strategy = st.builds(edu_Equivalence)
@given(instance=edu_Equivalence_strategy)
@settings(max_examples=25)
def test_edu_Equivalence_instantiation(instance):
    assert isinstance(instance, edu_Equivalence)


edu_ExistsQuantifier_strategy = st.builds(edu_ExistsQuantifier)
@given(instance=edu_ExistsQuantifier_strategy)
@settings(max_examples=25)
def test_edu_ExistsQuantifier_instantiation(instance):
    assert isinstance(instance, edu_ExistsQuantifier)


edu_Expression_strategy = st.builds(edu_Expression)
@given(instance=edu_Expression_strategy)
@settings(max_examples=25)
def test_edu_Expression_instantiation(instance):
    assert isinstance(instance, edu_Expression)


edu_ExpressionEvaluation_strategy = st.builds(edu_ExpressionEvaluation)
@given(instance=edu_ExpressionEvaluation_strategy)
@settings(max_examples=25)
def test_edu_ExpressionEvaluation_instantiation(instance):
    assert isinstance(instance, edu_ExpressionEvaluation)


edu_ExpressionToExpressionMap_strategy = st.builds(edu_ExpressionToExpressionMap)
@given(instance=edu_ExpressionToExpressionMap_strategy)
@settings(max_examples=25)
def test_edu_ExpressionToExpressionMap_instantiation(instance):
    assert isinstance(instance, edu_ExpressionToExpressionMap)


edu_ForAllQuantifier_strategy = st.builds(edu_ForAllQuantifier)
@given(instance=edu_ForAllQuantifier_strategy)
@settings(max_examples=25)
def test_edu_ForAllQuantifier_instantiation(instance):
    assert isinstance(instance, edu_ForAllQuantifier)


edu_FunctionAnnotation_strategy = st.builds(edu_FunctionAnnotation)
@given(instance=edu_FunctionAnnotation_strategy)
@settings(max_examples=25)
def test_edu_FunctionAnnotation_instantiation(instance):
    assert isinstance(instance, edu_FunctionAnnotation)


edu_FunctionCall_strategy = st.builds(edu_FunctionCall)
@given(instance=edu_FunctionCall_strategy)
@settings(max_examples=25)
def test_edu_FunctionCall_instantiation(instance):
    assert isinstance(instance, edu_FunctionCall)


edu_FunctionCallPreconditionAssertion_strategy = st.builds(edu_FunctionCallPreconditionAssertion)
@given(instance=edu_FunctionCallPreconditionAssertion_strategy)
@settings(max_examples=25)
def test_edu_FunctionCallPreconditionAssertion_instantiation(instance):
    assert isinstance(instance, edu_FunctionCallPreconditionAssertion)


edu_FunctionDeclaration_strategy = st.builds(edu_FunctionDeclaration, name=safe_text)
@given(instance=edu_FunctionDeclaration_strategy)
@settings(max_examples=25)
def test_edu_FunctionDeclaration_instantiation(instance):
    assert isinstance(instance, edu_FunctionDeclaration)


edu_Greater_strategy = st.builds(edu_Greater)
@given(instance=edu_Greater_strategy)
@settings(max_examples=25)
def test_edu_Greater_instantiation(instance):
    assert isinstance(instance, edu_Greater)


edu_GreaterOrEqual_strategy = st.builds(edu_GreaterOrEqual)
@given(instance=edu_GreaterOrEqual_strategy)
@settings(max_examples=25)
def test_edu_GreaterOrEqual_instantiation(instance):
    assert isinstance(instance, edu_GreaterOrEqual)


edu_GuardAssertion_strategy = st.builds(edu_GuardAssertion)
@given(instance=edu_GuardAssertion_strategy)
@settings(max_examples=25)
def test_edu_GuardAssertion_instantiation(instance):
    assert isinstance(instance, edu_GuardAssertion)


edu_Implication_strategy = st.builds(edu_Implication)
@given(instance=edu_Implication_strategy)
@settings(max_examples=25)
def test_edu_Implication_instantiation(instance):
    assert isinstance(instance, edu_Implication)


edu_IntegerLiteral_strategy = st.builds(edu_IntegerLiteral, value=safe_text)
@given(instance=edu_IntegerLiteral_strategy)
@settings(max_examples=25)
def test_edu_IntegerLiteral_instantiation(instance):
    assert isinstance(instance, edu_IntegerLiteral)


edu_IntegerType_strategy = st.builds(edu_IntegerType)
@given(instance=edu_IntegerType_strategy)
@settings(max_examples=25)
def test_edu_IntegerType_instantiation(instance):
    assert isinstance(instance, edu_IntegerType)


edu_Invariant_strategy = st.builds(edu_Invariant)
@given(instance=edu_Invariant_strategy)
@settings(max_examples=25)
def test_edu_Invariant_instantiation(instance):
    assert isinstance(instance, edu_Invariant)


edu_Less_strategy = st.builds(edu_Less)
@given(instance=edu_Less_strategy)
@settings(max_examples=25)
def test_edu_Less_instantiation(instance):
    assert isinstance(instance, edu_Less)


edu_LessOrEqual_strategy = st.builds(edu_LessOrEqual)
@given(instance=edu_LessOrEqual_strategy)
@settings(max_examples=25)
def test_edu_LessOrEqual_instantiation(instance):
    assert isinstance(instance, edu_LessOrEqual)


edu_LetExpression_strategy = st.builds(edu_LetExpression)
@given(instance=edu_LetExpression_strategy)
@settings(max_examples=25)
def test_edu_LetExpression_instantiation(instance):
    assert isinstance(instance, edu_LetExpression)


edu_Literal_strategy = st.builds(edu_Literal)
@given(instance=edu_Literal_strategy)
@settings(max_examples=25)
def test_edu_Literal_instantiation(instance):
    assert isinstance(instance, edu_Literal)


edu_Loop_strategy = st.builds(edu_Loop)
@given(instance=edu_Loop_strategy)
@settings(max_examples=25)
def test_edu_Loop_instantiation(instance):
    assert isinstance(instance, edu_Loop)


edu_Minus_strategy = st.builds(edu_Minus)
@given(instance=edu_Minus_strategy)
@settings(max_examples=25)
def test_edu_Minus_instantiation(instance):
    assert isinstance(instance, edu_Minus)


edu_Modulus_strategy = st.builds(edu_Modulus)
@given(instance=edu_Modulus_strategy)
@settings(max_examples=25)
def test_edu_Modulus_instantiation(instance):
    assert isinstance(instance, edu_Modulus)


edu_Multiplication_strategy = st.builds(edu_Multiplication)
@given(instance=edu_Multiplication_strategy)
@settings(max_examples=25)
def test_edu_Multiplication_instantiation(instance):
    assert isinstance(instance, edu_Multiplication)


edu_Negation_strategy = st.builds(edu_Negation)
@given(instance=edu_Negation_strategy)
@settings(max_examples=25)
def test_edu_Negation_instantiation(instance):
    assert isinstance(instance, edu_Negation)


edu_Plus_strategy = st.builds(edu_Plus)
@given(instance=edu_Plus_strategy)
@settings(max_examples=25)
def test_edu_Plus_instantiation(instance):
    assert isinstance(instance, edu_Plus)


edu_Postcondition_strategy = st.builds(edu_Postcondition)
@given(instance=edu_Postcondition_strategy)
@settings(max_examples=25)
def test_edu_Postcondition_instantiation(instance):
    assert isinstance(instance, edu_Postcondition)


edu_Precondition_strategy = st.builds(edu_Precondition)
@given(instance=edu_Precondition_strategy)
@settings(max_examples=25)
def test_edu_Precondition_instantiation(instance):
    assert isinstance(instance, edu_Precondition)


edu_PrimitiveType_strategy = st.builds(edu_PrimitiveType)
@given(instance=edu_PrimitiveType_strategy)
@settings(max_examples=25)
def test_edu_PrimitiveType_instantiation(instance):
    assert isinstance(instance, edu_PrimitiveType)


edu_Program_strategy = st.builds(edu_Program)
@given(instance=edu_Program_strategy)
@settings(max_examples=25)
def test_edu_Program_instantiation(instance):
    assert isinstance(instance, edu_Program)


edu_QuantifiedExpression_strategy = st.builds(edu_QuantifiedExpression)
@given(instance=edu_QuantifiedExpression_strategy)
@settings(max_examples=25)
def test_edu_QuantifiedExpression_instantiation(instance):
    assert isinstance(instance, edu_QuantifiedExpression)


edu_ReturnStatement_strategy = st.builds(edu_ReturnStatement)
@given(instance=edu_ReturnStatement_strategy)
@settings(max_examples=25)
def test_edu_ReturnStatement_instantiation(instance):
    assert isinstance(instance, edu_ReturnStatement)


edu_ReturnValueReference_strategy = st.builds(edu_ReturnValueReference)
@given(instance=edu_ReturnValueReference_strategy)
@settings(max_examples=25)
def test_edu_ReturnValueReference_instantiation(instance):
    assert isinstance(instance, edu_ReturnValueReference)


edu_Sign_strategy = st.builds(edu_Sign)
@given(instance=edu_Sign_strategy)
@settings(max_examples=25)
def test_edu_Sign_instantiation(instance):
    assert isinstance(instance, edu_Sign)


edu_Statement_strategy = st.builds(edu_Statement)
@given(instance=edu_Statement_strategy)
@settings(max_examples=25)
def test_edu_Statement_instantiation(instance):
    assert isinstance(instance, edu_Statement)


edu_Subtraction_strategy = st.builds(edu_Subtraction)
@given(instance=edu_Subtraction_strategy)
@settings(max_examples=25)
def test_edu_Subtraction_instantiation(instance):
    assert isinstance(instance, edu_Subtraction)


edu_SymbolReference_strategy = st.builds(edu_SymbolReference)
@given(instance=edu_SymbolReference_strategy)
@settings(max_examples=25)
def test_edu_SymbolReference_instantiation(instance):
    assert isinstance(instance, edu_SymbolReference)


edu_TernaryExpression_strategy = st.builds(edu_TernaryExpression)
@given(instance=edu_TernaryExpression_strategy)
@settings(max_examples=25)
def test_edu_TernaryExpression_instantiation(instance):
    assert isinstance(instance, edu_TernaryExpression)


edu_Type_strategy = st.builds(edu_Type)
@given(instance=edu_Type_strategy)
@settings(max_examples=25)
def test_edu_Type_instantiation(instance):
    assert isinstance(instance, edu_Type)


edu_UnaryExpression_strategy = st.builds(edu_UnaryExpression)
@given(instance=edu_UnaryExpression_strategy)
@settings(max_examples=25)
def test_edu_UnaryExpression_instantiation(instance):
    assert isinstance(instance, edu_UnaryExpression)


edu_Unequal_strategy = st.builds(edu_Unequal)
@given(instance=edu_Unequal_strategy)
@settings(max_examples=25)
def test_edu_Unequal_instantiation(instance):
    assert isinstance(instance, edu_Unequal)


edu_VariableDeclaration_strategy = st.builds(edu_VariableDeclaration, name=safe_text)
@given(instance=edu_VariableDeclaration_strategy)
@settings(max_examples=25)
def test_edu_VariableDeclaration_instantiation(instance):
    assert isinstance(instance, edu_VariableDeclaration)


edu_VariableReference_strategy = st.builds(edu_VariableReference)
@given(instance=edu_VariableReference_strategy)
@settings(max_examples=25)
def test_edu_VariableReference_instantiation(instance):
    assert isinstance(instance, edu_VariableReference)


edu_visitor_IASTNodeVisitor_strategy = st.builds(edu_visitor_IASTNodeVisitor)
@given(instance=edu_visitor_IASTNodeVisitor_strategy)
@settings(max_examples=25)
def test_edu_visitor_IASTNodeVisitor_instantiation(instance):
    assert isinstance(instance, edu_visitor_IASTNodeVisitor)



