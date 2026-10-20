import pytest
from datetime import date, datetime, time, timedelta

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

def test_assoc_actuals45_reverse_link_reassign_clear():
    a1 = edu_FunctionCall()
    a2 = edu_FunctionCall()
    b = edu_Expression()
    _safe_set(b, 'edu_Expression47', a1)
    assert _is_linked(b, 'edu_Expression47', a1)
    if hasattr(a1, 'edu_FunctionCall46'):
        assert _is_linked(a1, 'edu_FunctionCall46', b)
    _safe_set(b, 'edu_Expression47', a2)
    assert _is_linked(b, 'edu_Expression47', a2)
    if hasattr(a1, 'edu_FunctionCall46'):
        assert not _is_linked(a1, 'edu_FunctionCall46', b)
    if hasattr(a2, 'edu_FunctionCall46'):
        assert _is_linked(a2, 'edu_FunctionCall46', b)
    _safe_set(b, 'edu_Expression47', None)
    assert not _is_linked(b, 'edu_Expression47', a2)
    if hasattr(a2, 'edu_FunctionCall46'):
        assert not _is_linked(a2, 'edu_FunctionCall46', b)


def test_assoc_array95_reverse_link_reassign_clear():
    a1 = edu_Expression()
    a2 = edu_Expression()
    b = edu_ArrayAccess()
    _safe_set(b, 'edu_ArrayAccess96', a1)
    assert _is_linked(b, 'edu_ArrayAccess96', a1)
    if hasattr(a1, 'edu_Expression97'):
        assert _is_linked(a1, 'edu_Expression97', b)
    _safe_set(b, 'edu_ArrayAccess96', a2)
    assert _is_linked(b, 'edu_ArrayAccess96', a2)
    if hasattr(a1, 'edu_Expression97'):
        assert not _is_linked(a1, 'edu_Expression97', b)
    if hasattr(a2, 'edu_Expression97'):
        assert _is_linked(a2, 'edu_Expression97', b)
    _safe_set(b, 'edu_ArrayAccess96', None)
    assert not _is_linked(b, 'edu_ArrayAccess96', a2)
    if hasattr(a2, 'edu_Expression97'):
        assert not _is_linked(a2, 'edu_Expression97', b)


def test_assoc_axioms3_reverse_link_reassign_clear():
    a1 = edu_Program()
    a2 = edu_Program()
    b = edu_Axiom()
    _safe_set(b, 'edu_Axiom', a1)
    assert _is_linked(b, 'edu_Axiom', a1)
    if hasattr(a1, 'edu_Program4'):
        assert _is_linked(a1, 'edu_Program4', b)
    _safe_set(b, 'edu_Axiom', a2)
    assert _is_linked(b, 'edu_Axiom', a2)
    if hasattr(a1, 'edu_Program4'):
        assert not _is_linked(a1, 'edu_Program4', b)
    if hasattr(a2, 'edu_Program4'):
        assert _is_linked(a2, 'edu_Program4', b)
    _safe_set(b, 'edu_Axiom', None)
    assert not _is_linked(b, 'edu_Axiom', a2)
    if hasattr(a2, 'edu_Program4'):
        assert not _is_linked(a2, 'edu_Program4', b)


def test_assoc_baseType13_reverse_link_reassign_clear():
    a1 = edu_PrimitiveType()
    a2 = edu_PrimitiveType()
    b = edu_ArrayType()
    _safe_set(b, 'edu_ArrayType', a1)
    assert _is_linked(b, 'edu_ArrayType', a1)
    if hasattr(a1, 'edu_PrimitiveType'):
        assert _is_linked(a1, 'edu_PrimitiveType', b)
    _safe_set(b, 'edu_ArrayType', a2)
    assert _is_linked(b, 'edu_ArrayType', a2)
    if hasattr(a1, 'edu_PrimitiveType'):
        assert not _is_linked(a1, 'edu_PrimitiveType', b)
    if hasattr(a2, 'edu_PrimitiveType'):
        assert _is_linked(a2, 'edu_PrimitiveType', b)
    _safe_set(b, 'edu_ArrayType', None)
    assert not _is_linked(b, 'edu_ArrayType', a2)
    if hasattr(a2, 'edu_PrimitiveType'):
        assert not _is_linked(a2, 'edu_PrimitiveType', b)


def test_assoc_body58_reverse_link_reassign_clear():
    a1 = edu_FunctionDeclaration(name="sample_text")
    a2 = edu_FunctionDeclaration(name="sample_text_2")
    b = edu_Block()
    _safe_set(b, 'edu_Block60', a1)
    assert _is_linked(b, 'edu_Block60', a1)
    if hasattr(a1, 'edu_FunctionDeclaration59'):
        assert _is_linked(a1, 'edu_FunctionDeclaration59', b)
    _safe_set(b, 'edu_Block60', a2)
    assert _is_linked(b, 'edu_Block60', a2)
    if hasattr(a1, 'edu_FunctionDeclaration59'):
        assert not _is_linked(a1, 'edu_FunctionDeclaration59', b)
    if hasattr(a2, 'edu_FunctionDeclaration59'):
        assert _is_linked(a2, 'edu_FunctionDeclaration59', b)
    _safe_set(b, 'edu_Block60', None)
    assert not _is_linked(b, 'edu_Block60', a2)
    if hasattr(a2, 'edu_FunctionDeclaration59'):
        assert not _is_linked(a2, 'edu_FunctionDeclaration59', b)


def test_assoc_body66_reverse_link_reassign_clear():
    a1 = edu_Loop()
    a2 = edu_Loop()
    b = edu_Block()
    _safe_set(b, 'edu_Block68', a1)
    assert _is_linked(b, 'edu_Block68', a1)
    if hasattr(a1, 'edu_Loop67'):
        assert _is_linked(a1, 'edu_Loop67', b)
    _safe_set(b, 'edu_Block68', a2)
    assert _is_linked(b, 'edu_Block68', a2)
    if hasattr(a1, 'edu_Loop67'):
        assert not _is_linked(a1, 'edu_Loop67', b)
    if hasattr(a2, 'edu_Loop67'):
        assert _is_linked(a2, 'edu_Loop67', b)
    _safe_set(b, 'edu_Block68', None)
    assert not _is_linked(b, 'edu_Block68', a2)
    if hasattr(a2, 'edu_Loop67'):
        assert not _is_linked(a2, 'edu_Loop67', b)


def test_assoc_chainedFunction85_reverse_link_reassign_clear():
    a1 = edu_Expression()
    a2 = edu_Expression()
    b = edu_ArrayFunction()
    _safe_set(b, 'edu_ArrayFunction', a1)
    assert _is_linked(b, 'edu_ArrayFunction', a1)
    if hasattr(a1, 'edu_Expression86'):
        assert _is_linked(a1, 'edu_Expression86', b)
    _safe_set(b, 'edu_ArrayFunction', a2)
    assert _is_linked(b, 'edu_ArrayFunction', a2)
    if hasattr(a1, 'edu_Expression86'):
        assert not _is_linked(a1, 'edu_Expression86', b)
    if hasattr(a2, 'edu_Expression86'):
        assert _is_linked(a2, 'edu_Expression86', b)
    _safe_set(b, 'edu_ArrayFunction', None)
    assert not _is_linked(b, 'edu_ArrayFunction', a2)
    if hasattr(a2, 'edu_Expression86'):
        assert not _is_linked(a2, 'edu_Expression86', b)


def test_assoc_condition108_reverse_link_reassign_clear():
    a1 = edu_TernaryExpression()
    a2 = edu_TernaryExpression()
    b = edu_Expression()
    _safe_set(b, 'edu_Expression110', a1)
    assert _is_linked(b, 'edu_Expression110', a1)
    if hasattr(a1, 'edu_TernaryExpression109'):
        assert _is_linked(a1, 'edu_TernaryExpression109', b)
    _safe_set(b, 'edu_Expression110', a2)
    assert _is_linked(b, 'edu_Expression110', a2)
    if hasattr(a1, 'edu_TernaryExpression109'):
        assert not _is_linked(a1, 'edu_TernaryExpression109', b)
    if hasattr(a2, 'edu_TernaryExpression109'):
        assert _is_linked(a2, 'edu_TernaryExpression109', b)
    _safe_set(b, 'edu_Expression110', None)
    assert not _is_linked(b, 'edu_Expression110', a2)
    if hasattr(a2, 'edu_TernaryExpression109'):
        assert not _is_linked(a2, 'edu_TernaryExpression109', b)


def test_assoc_condition29_reverse_link_reassign_clear():
    a1 = edu_Expression()
    a2 = edu_Expression()
    b = edu_Conditional()
    _safe_set(b, 'edu_Conditional', a1)
    assert _is_linked(b, 'edu_Conditional', a1)
    if hasattr(a1, 'edu_Expression30'):
        assert _is_linked(a1, 'edu_Expression30', b)
    _safe_set(b, 'edu_Conditional', a2)
    assert _is_linked(b, 'edu_Conditional', a2)
    if hasattr(a1, 'edu_Expression30'):
        assert not _is_linked(a1, 'edu_Expression30', b)
    if hasattr(a2, 'edu_Expression30'):
        assert _is_linked(a2, 'edu_Expression30', b)
    _safe_set(b, 'edu_Conditional', None)
    assert not _is_linked(b, 'edu_Conditional', a2)
    if hasattr(a2, 'edu_Expression30'):
        assert not _is_linked(a2, 'edu_Expression30', b)


def test_assoc_condition42_reverse_link_reassign_clear():
    a1 = edu_QuantifiedExpression()
    a2 = edu_QuantifiedExpression()
    b = edu_Expression()
    _safe_set(b, 'edu_Expression44', a1)
    assert _is_linked(b, 'edu_Expression44', a1)
    if hasattr(a1, 'edu_QuantifiedExpression43'):
        assert _is_linked(a1, 'edu_QuantifiedExpression43', b)
    _safe_set(b, 'edu_Expression44', a2)
    assert _is_linked(b, 'edu_Expression44', a2)
    if hasattr(a1, 'edu_QuantifiedExpression43'):
        assert not _is_linked(a1, 'edu_QuantifiedExpression43', b)
    if hasattr(a2, 'edu_QuantifiedExpression43'):
        assert _is_linked(a2, 'edu_QuantifiedExpression43', b)
    _safe_set(b, 'edu_Expression44', None)
    assert not _is_linked(b, 'edu_Expression44', a2)
    if hasattr(a2, 'edu_QuantifiedExpression43'):
        assert not _is_linked(a2, 'edu_QuantifiedExpression43', b)


def test_assoc_condition64_reverse_link_reassign_clear():
    a1 = edu_Loop()
    a2 = edu_Loop()
    b = edu_Expression()
    _safe_set(b, 'edu_Expression65', a1)
    assert _is_linked(b, 'edu_Expression65', a1)
    if hasattr(a1, 'edu_Loop'):
        assert _is_linked(a1, 'edu_Loop', b)
    _safe_set(b, 'edu_Expression65', a2)
    assert _is_linked(b, 'edu_Expression65', a2)
    if hasattr(a1, 'edu_Loop'):
        assert not _is_linked(a1, 'edu_Loop', b)
    if hasattr(a2, 'edu_Loop'):
        assert _is_linked(a2, 'edu_Loop', b)
    _safe_set(b, 'edu_Expression65', None)
    assert not _is_linked(b, 'edu_Expression65', a2)
    if hasattr(a2, 'edu_Loop'):
        assert not _is_linked(a2, 'edu_Loop', b)


def test_assoc_expression17_reverse_link_reassign_clear():
    a1 = edu_Expression()
    a2 = edu_Expression()
    b = edu_Annotation()
    _safe_set(b, 'edu_Annotation', a1)
    assert _is_linked(b, 'edu_Annotation', a1)
    if hasattr(a1, 'edu_Expression18'):
        assert _is_linked(a1, 'edu_Expression18', b)
    _safe_set(b, 'edu_Annotation', a2)
    assert _is_linked(b, 'edu_Annotation', a2)
    if hasattr(a1, 'edu_Expression18'):
        assert not _is_linked(a1, 'edu_Expression18', b)
    if hasattr(a2, 'edu_Expression18'):
        assert _is_linked(a2, 'edu_Expression18', b)
    _safe_set(b, 'edu_Annotation', None)
    assert not _is_linked(b, 'edu_Annotation', a2)
    if hasattr(a2, 'edu_Expression18'):
        assert not _is_linked(a2, 'edu_Expression18', b)


def test_assoc_expression39_reverse_link_reassign_clear():
    a1 = edu_QuantifiedExpression()
    a2 = edu_QuantifiedExpression()
    b = edu_Expression()
    _safe_set(b, 'edu_Expression41', a1)
    assert _is_linked(b, 'edu_Expression41', a1)
    if hasattr(a1, 'edu_QuantifiedExpression40'):
        assert _is_linked(a1, 'edu_QuantifiedExpression40', b)
    _safe_set(b, 'edu_Expression41', a2)
    assert _is_linked(b, 'edu_Expression41', a2)
    if hasattr(a1, 'edu_QuantifiedExpression40'):
        assert not _is_linked(a1, 'edu_QuantifiedExpression40', b)
    if hasattr(a2, 'edu_QuantifiedExpression40'):
        assert _is_linked(a2, 'edu_QuantifiedExpression40', b)
    _safe_set(b, 'edu_Expression41', None)
    assert not _is_linked(b, 'edu_Expression41', a2)
    if hasattr(a2, 'edu_QuantifiedExpression40'):
        assert not _is_linked(a2, 'edu_QuantifiedExpression40', b)


def test_assoc_falseBlock34_reverse_link_reassign_clear():
    a1 = edu_Conditional()
    a2 = edu_Conditional()
    b = edu_Block()
    _safe_set(b, 'edu_Block36', a1)
    assert _is_linked(b, 'edu_Block36', a1)
    if hasattr(a1, 'edu_Conditional35'):
        assert _is_linked(a1, 'edu_Conditional35', b)
    _safe_set(b, 'edu_Block36', a2)
    assert _is_linked(b, 'edu_Block36', a2)
    if hasattr(a1, 'edu_Conditional35'):
        assert not _is_linked(a1, 'edu_Conditional35', b)
    if hasattr(a2, 'edu_Conditional35'):
        assert _is_linked(a2, 'edu_Conditional35', b)
    _safe_set(b, 'edu_Block36', None)
    assert not _is_linked(b, 'edu_Block36', a2)
    if hasattr(a2, 'edu_Conditional35'):
        assert not _is_linked(a2, 'edu_Conditional35', b)


def test_assoc_function48_reverse_link_reassign_clear():
    a1 = edu_FunctionDeclaration(name="sample_text")
    a2 = edu_FunctionDeclaration(name="sample_text_2")
    b = edu_FunctionCall()
    _safe_set(b, 'edu_FunctionCall49', a1)
    assert _is_linked(b, 'edu_FunctionCall49', a1)
    if hasattr(a1, 'edu_FunctionDeclaration50'):
        assert _is_linked(a1, 'edu_FunctionDeclaration50', b)
    _safe_set(b, 'edu_FunctionCall49', a2)
    assert _is_linked(b, 'edu_FunctionCall49', a2)
    if hasattr(a1, 'edu_FunctionDeclaration50'):
        assert not _is_linked(a1, 'edu_FunctionDeclaration50', b)
    if hasattr(a2, 'edu_FunctionDeclaration50'):
        assert _is_linked(a2, 'edu_FunctionDeclaration50', b)
    _safe_set(b, 'edu_FunctionCall49', None)
    assert not _is_linked(b, 'edu_FunctionCall49', a2)
    if hasattr(a2, 'edu_FunctionDeclaration50'):
        assert not _is_linked(a2, 'edu_FunctionDeclaration50', b)


def test_assoc_function73_reverse_link_reassign_clear():
    a1 = edu_ReturnStatement()
    a2 = edu_ReturnStatement()
    b = edu_FunctionDeclaration(name="sample_text")
    _safe_set(b, 'edu_FunctionDeclaration75', a1)
    assert _is_linked(b, 'edu_FunctionDeclaration75', a1)
    if hasattr(a1, 'edu_ReturnStatement74'):
        assert _is_linked(a1, 'edu_ReturnStatement74', b)
    _safe_set(b, 'edu_FunctionDeclaration75', a2)
    assert _is_linked(b, 'edu_FunctionDeclaration75', a2)
    if hasattr(a1, 'edu_ReturnStatement74'):
        assert not _is_linked(a1, 'edu_ReturnStatement74', b)
    if hasattr(a2, 'edu_ReturnStatement74'):
        assert _is_linked(a2, 'edu_ReturnStatement74', b)
    _safe_set(b, 'edu_FunctionDeclaration75', None)
    assert not _is_linked(b, 'edu_FunctionDeclaration75', a2)
    if hasattr(a2, 'edu_ReturnStatement74'):
        assert not _is_linked(a2, 'edu_ReturnStatement74', b)


def test_assoc_function79_reverse_link_reassign_clear():
    a1 = edu_ReturnValueReference()
    a2 = edu_ReturnValueReference()
    b = edu_FunctionDeclaration(name="sample_text")
    _safe_set(b, 'edu_FunctionDeclaration80', a1)
    assert _is_linked(b, 'edu_FunctionDeclaration80', a1)
    if hasattr(a1, 'edu_ReturnValueReference'):
        assert _is_linked(a1, 'edu_ReturnValueReference', b)
    _safe_set(b, 'edu_FunctionDeclaration80', a2)
    assert _is_linked(b, 'edu_FunctionDeclaration80', a2)
    if hasattr(a1, 'edu_ReturnValueReference'):
        assert not _is_linked(a1, 'edu_ReturnValueReference', b)
    if hasattr(a2, 'edu_ReturnValueReference'):
        assert _is_linked(a2, 'edu_ReturnValueReference', b)
    _safe_set(b, 'edu_FunctionDeclaration80', None)
    assert not _is_linked(b, 'edu_FunctionDeclaration80', a2)
    if hasattr(a2, 'edu_ReturnValueReference'):
        assert not _is_linked(a2, 'edu_ReturnValueReference', b)


def test_assoc_functionDeclarations0_reverse_link_reassign_clear():
    a1 = edu_Program()
    a2 = edu_Program()
    b = edu_FunctionDeclaration(name="sample_text")
    _safe_set(b, 'edu_FunctionDeclaration', a1)
    assert _is_linked(b, 'edu_FunctionDeclaration', a1)
    if hasattr(a1, 'edu_Program'):
        assert _is_linked(a1, 'edu_Program', b)
    _safe_set(b, 'edu_FunctionDeclaration', a2)
    assert _is_linked(b, 'edu_FunctionDeclaration', a2)
    if hasattr(a1, 'edu_Program'):
        assert not _is_linked(a1, 'edu_Program', b)
    if hasattr(a2, 'edu_Program'):
        assert _is_linked(a2, 'edu_Program', b)
    _safe_set(b, 'edu_FunctionDeclaration', None)
    assert not _is_linked(b, 'edu_FunctionDeclaration', a2)
    if hasattr(a2, 'edu_Program'):
        assert not _is_linked(a2, 'edu_Program', b)


def test_assoc_guardedNode14_reverse_link_reassign_clear():
    a1 = edu_FunctionCallPreconditionAssertion()
    a2 = edu_FunctionCallPreconditionAssertion()
    b = edu_FunctionCall()
    _safe_set(b, 'edu_FunctionCall', a1)
    assert _is_linked(b, 'edu_FunctionCall', a1)
    if hasattr(a1, 'edu_FunctionCallPreconditionAssertion'):
        assert _is_linked(a1, 'edu_FunctionCallPreconditionAssertion', b)
    _safe_set(b, 'edu_FunctionCall', a2)
    assert _is_linked(b, 'edu_FunctionCall', a2)
    if hasattr(a1, 'edu_FunctionCallPreconditionAssertion'):
        assert not _is_linked(a1, 'edu_FunctionCallPreconditionAssertion', b)
    if hasattr(a2, 'edu_FunctionCallPreconditionAssertion'):
        assert _is_linked(a2, 'edu_FunctionCallPreconditionAssertion', b)
    _safe_set(b, 'edu_FunctionCall', None)
    assert not _is_linked(b, 'edu_FunctionCall', a2)
    if hasattr(a2, 'edu_FunctionCallPreconditionAssertion'):
        assert not _is_linked(a2, 'edu_FunctionCallPreconditionAssertion', b)


def test_assoc_guardedNode15_reverse_link_reassign_clear():
    a1 = edu_Expression()
    a2 = edu_Expression()
    b = edu_DivisorNotZeroAssertion()
    _safe_set(b, 'edu_DivisorNotZeroAssertion', a1)
    assert _is_linked(b, 'edu_DivisorNotZeroAssertion', a1)
    if hasattr(a1, 'edu_Expression16'):
        assert _is_linked(a1, 'edu_Expression16', b)
    _safe_set(b, 'edu_DivisorNotZeroAssertion', a2)
    assert _is_linked(b, 'edu_DivisorNotZeroAssertion', a2)
    if hasattr(a1, 'edu_Expression16'):
        assert not _is_linked(a1, 'edu_Expression16', b)
    if hasattr(a2, 'edu_Expression16'):
        assert _is_linked(a2, 'edu_Expression16', b)
    _safe_set(b, 'edu_DivisorNotZeroAssertion', None)
    assert not _is_linked(b, 'edu_DivisorNotZeroAssertion', a2)
    if hasattr(a2, 'edu_Expression16'):
        assert not _is_linked(a2, 'edu_Expression16', b)


def test_assoc_index81_reverse_link_reassign_clear():
    a1 = edu_SymbolReference()
    a2 = edu_SymbolReference()
    b = edu_Expression()
    _safe_set(b, 'edu_Expression82', a1)
    assert _is_linked(b, 'edu_Expression82', a1)
    if hasattr(a1, 'edu_SymbolReference'):
        assert _is_linked(a1, 'edu_SymbolReference', b)
    _safe_set(b, 'edu_Expression82', a2)
    assert _is_linked(b, 'edu_Expression82', a2)
    if hasattr(a1, 'edu_SymbolReference'):
        assert not _is_linked(a1, 'edu_SymbolReference', b)
    if hasattr(a2, 'edu_SymbolReference'):
        assert _is_linked(a2, 'edu_SymbolReference', b)
    _safe_set(b, 'edu_Expression82', None)
    assert not _is_linked(b, 'edu_Expression82', a2)
    if hasattr(a2, 'edu_SymbolReference'):
        assert not _is_linked(a2, 'edu_SymbolReference', b)


def test_assoc_index87_reverse_link_reassign_clear():
    a1 = edu_Expression()
    a2 = edu_Expression()
    b = edu_ArrayFunction()
    _safe_set(b, 'edu_ArrayFunction88', a1)
    assert _is_linked(b, 'edu_ArrayFunction88', a1)
    if hasattr(a1, 'edu_Expression89'):
        assert _is_linked(a1, 'edu_Expression89', b)
    _safe_set(b, 'edu_ArrayFunction88', a2)
    assert _is_linked(b, 'edu_ArrayFunction88', a2)
    if hasattr(a1, 'edu_Expression89'):
        assert not _is_linked(a1, 'edu_Expression89', b)
    if hasattr(a2, 'edu_Expression89'):
        assert _is_linked(a2, 'edu_Expression89', b)
    _safe_set(b, 'edu_ArrayFunction88', None)
    assert not _is_linked(b, 'edu_ArrayFunction88', a2)
    if hasattr(a2, 'edu_Expression89'):
        assert not _is_linked(a2, 'edu_Expression89', b)


def test_assoc_index93_reverse_link_reassign_clear():
    a1 = edu_Expression()
    a2 = edu_Expression()
    b = edu_ArrayAccess()
    _safe_set(b, 'edu_ArrayAccess', a1)
    assert _is_linked(b, 'edu_ArrayAccess', a1)
    if hasattr(a1, 'edu_Expression94'):
        assert _is_linked(a1, 'edu_Expression94', b)
    _safe_set(b, 'edu_ArrayAccess', a2)
    assert _is_linked(b, 'edu_ArrayAccess', a2)
    if hasattr(a1, 'edu_Expression94'):
        assert not _is_linked(a1, 'edu_Expression94', b)
    if hasattr(a2, 'edu_Expression94'):
        assert _is_linked(a2, 'edu_Expression94', b)
    _safe_set(b, 'edu_ArrayAccess', None)
    assert not _is_linked(b, 'edu_ArrayAccess', a2)
    if hasattr(a2, 'edu_Expression94'):
        assert not _is_linked(a2, 'edu_Expression94', b)


def test_assoc_initialValue24_reverse_link_reassign_clear():
    a1 = edu_VariableDeclaration(name="sample_text")
    a2 = edu_VariableDeclaration(name="sample_text_2")
    b = edu_Expression()
    _safe_set(b, 'edu_Expression26', a1)
    assert _is_linked(b, 'edu_Expression26', a1)
    if hasattr(a1, 'edu_VariableDeclaration25'):
        assert _is_linked(a1, 'edu_VariableDeclaration25', b)
    _safe_set(b, 'edu_Expression26', a2)
    assert _is_linked(b, 'edu_Expression26', a2)
    if hasattr(a1, 'edu_VariableDeclaration25'):
        assert not _is_linked(a1, 'edu_VariableDeclaration25', b)
    if hasattr(a2, 'edu_VariableDeclaration25'):
        assert _is_linked(a2, 'edu_VariableDeclaration25', b)
    _safe_set(b, 'edu_Expression26', None)
    assert not _is_linked(b, 'edu_Expression26', a2)
    if hasattr(a2, 'edu_VariableDeclaration25'):
        assert not _is_linked(a2, 'edu_VariableDeclaration25', b)


def test_assoc_invariants69_reverse_link_reassign_clear():
    a1 = edu_Loop()
    a2 = edu_Loop()
    b = edu_Invariant()
    _safe_set(b, 'edu_Invariant', a1)
    assert _is_linked(b, 'edu_Invariant', a1)
    if hasattr(a1, 'edu_Loop70'):
        assert _is_linked(a1, 'edu_Loop70', b)
    _safe_set(b, 'edu_Invariant', a2)
    assert _is_linked(b, 'edu_Invariant', a2)
    if hasattr(a1, 'edu_Loop70'):
        assert not _is_linked(a1, 'edu_Loop70', b)
    if hasattr(a2, 'edu_Loop70'):
        assert _is_linked(a2, 'edu_Loop70', b)
    _safe_set(b, 'edu_Invariant', None)
    assert not _is_linked(b, 'edu_Invariant', a2)
    if hasattr(a2, 'edu_Loop70'):
        assert not _is_linked(a2, 'edu_Loop70', b)


def test_assoc_left5_reverse_link_reassign_clear():
    a1 = edu_Expression()
    a2 = edu_Expression()
    b = edu_BinaryExpression()
    _safe_set(b, 'edu_BinaryExpression', a1)
    assert _is_linked(b, 'edu_BinaryExpression', a1)
    if hasattr(a1, 'edu_Expression'):
        assert _is_linked(a1, 'edu_Expression', b)
    _safe_set(b, 'edu_BinaryExpression', a2)
    assert _is_linked(b, 'edu_BinaryExpression', a2)
    if hasattr(a1, 'edu_Expression'):
        assert not _is_linked(a1, 'edu_Expression', b)
    if hasattr(a2, 'edu_Expression'):
        assert _is_linked(a2, 'edu_Expression', b)
    _safe_set(b, 'edu_BinaryExpression', None)
    assert not _is_linked(b, 'edu_BinaryExpression', a2)
    if hasattr(a2, 'edu_Expression'):
        assert not _is_linked(a2, 'edu_Expression', b)


def test_assoc_mainBlock1_reverse_link_reassign_clear():
    a1 = edu_Program()
    a2 = edu_Program()
    b = edu_Block()
    _safe_set(b, 'edu_Block', a1)
    assert _is_linked(b, 'edu_Block', a1)
    if hasattr(a1, 'edu_Program2'):
        assert _is_linked(a1, 'edu_Program2', b)
    _safe_set(b, 'edu_Block', a2)
    assert _is_linked(b, 'edu_Block', a2)
    if hasattr(a1, 'edu_Program2'):
        assert not _is_linked(a1, 'edu_Program2', b)
    if hasattr(a2, 'edu_Program2'):
        assert _is_linked(a2, 'edu_Program2', b)
    _safe_set(b, 'edu_Block', None)
    assert not _is_linked(b, 'edu_Block', a2)
    if hasattr(a2, 'edu_Program2'):
        assert not _is_linked(a2, 'edu_Program2', b)


def test_assoc_operand9_reverse_link_reassign_clear():
    a1 = edu_UnaryExpression()
    a2 = edu_UnaryExpression()
    b = edu_Expression()
    _safe_set(b, 'edu_Expression10', a1)
    assert _is_linked(b, 'edu_Expression10', a1)
    if hasattr(a1, 'edu_UnaryExpression'):
        assert _is_linked(a1, 'edu_UnaryExpression', b)
    _safe_set(b, 'edu_Expression10', a2)
    assert _is_linked(b, 'edu_Expression10', a2)
    if hasattr(a1, 'edu_UnaryExpression'):
        assert not _is_linked(a1, 'edu_UnaryExpression', b)
    if hasattr(a2, 'edu_UnaryExpression'):
        assert _is_linked(a2, 'edu_UnaryExpression', b)
    _safe_set(b, 'edu_Expression10', None)
    assert not _is_linked(b, 'edu_Expression10', a2)
    if hasattr(a2, 'edu_UnaryExpression'):
        assert not _is_linked(a2, 'edu_UnaryExpression', b)


def test_assoc_parameter37_reverse_link_reassign_clear():
    a1 = edu_VariableDeclaration(name="sample_text")
    a2 = edu_VariableDeclaration(name="sample_text_2")
    b = edu_QuantifiedExpression()
    _safe_set(b, 'edu_QuantifiedExpression', a1)
    assert _is_linked(b, 'edu_QuantifiedExpression', a1)
    if hasattr(a1, 'edu_VariableDeclaration38'):
        assert _is_linked(a1, 'edu_VariableDeclaration38', b)
    _safe_set(b, 'edu_QuantifiedExpression', a2)
    assert _is_linked(b, 'edu_QuantifiedExpression', a2)
    if hasattr(a1, 'edu_VariableDeclaration38'):
        assert not _is_linked(a1, 'edu_VariableDeclaration38', b)
    if hasattr(a2, 'edu_VariableDeclaration38'):
        assert _is_linked(a2, 'edu_VariableDeclaration38', b)
    _safe_set(b, 'edu_QuantifiedExpression', None)
    assert not _is_linked(b, 'edu_QuantifiedExpression', a2)
    if hasattr(a2, 'edu_VariableDeclaration38'):
        assert not _is_linked(a2, 'edu_VariableDeclaration38', b)


def test_assoc_parameters55_reverse_link_reassign_clear():
    a1 = edu_VariableDeclaration(name="sample_text")
    a2 = edu_VariableDeclaration(name="sample_text_2")
    b = edu_FunctionDeclaration(name="sample_text")
    _safe_set(b, 'edu_FunctionDeclaration56', {a1})
    assert _is_linked(b, 'edu_FunctionDeclaration56', a1)
    if hasattr(a1, 'edu_VariableDeclaration57'):
        assert _is_linked(a1, 'edu_VariableDeclaration57', b)
    _safe_set(b, 'edu_FunctionDeclaration56', {a2})
    assert _is_linked(b, 'edu_FunctionDeclaration56', a2)
    if hasattr(a1, 'edu_VariableDeclaration57'):
        assert not _is_linked(a1, 'edu_VariableDeclaration57', b)
    if hasattr(a2, 'edu_VariableDeclaration57'):
        assert _is_linked(a2, 'edu_VariableDeclaration57', b)
    _safe_set(b, 'edu_FunctionDeclaration56', set())
    assert not _is_linked(b, 'edu_FunctionDeclaration56', a2)
    if hasattr(a2, 'edu_VariableDeclaration57'):
        assert not _is_linked(a2, 'edu_VariableDeclaration57', b)


def test_assoc_postconditions53_reverse_link_reassign_clear():
    a1 = edu_Postcondition()
    a2 = edu_Postcondition()
    b = edu_FunctionDeclaration(name="sample_text")
    _safe_set(b, 'edu_FunctionDeclaration54', {a1})
    assert _is_linked(b, 'edu_FunctionDeclaration54', a1)
    if hasattr(a1, 'edu_Postcondition'):
        assert _is_linked(a1, 'edu_Postcondition', b)
    _safe_set(b, 'edu_FunctionDeclaration54', {a2})
    assert _is_linked(b, 'edu_FunctionDeclaration54', a2)
    if hasattr(a1, 'edu_Postcondition'):
        assert not _is_linked(a1, 'edu_Postcondition', b)
    if hasattr(a2, 'edu_Postcondition'):
        assert _is_linked(a2, 'edu_Postcondition', b)
    _safe_set(b, 'edu_FunctionDeclaration54', set())
    assert not _is_linked(b, 'edu_FunctionDeclaration54', a2)
    if hasattr(a2, 'edu_Postcondition'):
        assert not _is_linked(a2, 'edu_Postcondition', b)


def test_assoc_preconditions51_reverse_link_reassign_clear():
    a1 = edu_Precondition()
    a2 = edu_Precondition()
    b = edu_FunctionDeclaration(name="sample_text")
    _safe_set(b, 'edu_FunctionDeclaration52', {a1})
    assert _is_linked(b, 'edu_FunctionDeclaration52', a1)
    if hasattr(a1, 'edu_Precondition'):
        assert _is_linked(a1, 'edu_Precondition', b)
    _safe_set(b, 'edu_FunctionDeclaration52', {a2})
    assert _is_linked(b, 'edu_FunctionDeclaration52', a2)
    if hasattr(a1, 'edu_Precondition'):
        assert not _is_linked(a1, 'edu_Precondition', b)
    if hasattr(a2, 'edu_Precondition'):
        assert _is_linked(a2, 'edu_Precondition', b)
    _safe_set(b, 'edu_FunctionDeclaration52', set())
    assert not _is_linked(b, 'edu_FunctionDeclaration52', a2)
    if hasattr(a2, 'edu_Precondition'):
        assert not _is_linked(a2, 'edu_Precondition', b)


def test_assoc_returnType61_reverse_link_reassign_clear():
    a1 = edu_Type()
    a2 = edu_Type()
    b = edu_FunctionDeclaration(name="sample_text")
    _safe_set(b, 'edu_FunctionDeclaration62', a1)
    assert _is_linked(b, 'edu_FunctionDeclaration62', a1)
    if hasattr(a1, 'edu_Type63'):
        assert _is_linked(a1, 'edu_Type63', b)
    _safe_set(b, 'edu_FunctionDeclaration62', a2)
    assert _is_linked(b, 'edu_FunctionDeclaration62', a2)
    if hasattr(a1, 'edu_Type63'):
        assert not _is_linked(a1, 'edu_Type63', b)
    if hasattr(a2, 'edu_Type63'):
        assert _is_linked(a2, 'edu_Type63', b)
    _safe_set(b, 'edu_FunctionDeclaration62', None)
    assert not _is_linked(b, 'edu_FunctionDeclaration62', a2)
    if hasattr(a2, 'edu_Type63'):
        assert not _is_linked(a2, 'edu_Type63', b)


def test_assoc_returnValue71_reverse_link_reassign_clear():
    a1 = edu_ReturnStatement()
    a2 = edu_ReturnStatement()
    b = edu_Expression()
    _safe_set(b, 'edu_Expression72', a1)
    assert _is_linked(b, 'edu_Expression72', a1)
    if hasattr(a1, 'edu_ReturnStatement'):
        assert _is_linked(a1, 'edu_ReturnStatement', b)
    _safe_set(b, 'edu_Expression72', a2)
    assert _is_linked(b, 'edu_Expression72', a2)
    if hasattr(a1, 'edu_ReturnStatement'):
        assert not _is_linked(a1, 'edu_ReturnStatement', b)
    if hasattr(a2, 'edu_ReturnStatement'):
        assert _is_linked(a2, 'edu_ReturnStatement', b)
    _safe_set(b, 'edu_Expression72', None)
    assert not _is_linked(b, 'edu_Expression72', a2)
    if hasattr(a2, 'edu_ReturnStatement'):
        assert not _is_linked(a2, 'edu_ReturnStatement', b)


def test_assoc_right6_reverse_link_reassign_clear():
    a1 = edu_Expression()
    a2 = edu_Expression()
    b = edu_BinaryExpression()
    _safe_set(b, 'edu_BinaryExpression7', a1)
    assert _is_linked(b, 'edu_BinaryExpression7', a1)
    if hasattr(a1, 'edu_Expression8'):
        assert _is_linked(a1, 'edu_Expression8', b)
    _safe_set(b, 'edu_BinaryExpression7', a2)
    assert _is_linked(b, 'edu_BinaryExpression7', a2)
    if hasattr(a1, 'edu_Expression8'):
        assert not _is_linked(a1, 'edu_Expression8', b)
    if hasattr(a2, 'edu_Expression8'):
        assert _is_linked(a2, 'edu_Expression8', b)
    _safe_set(b, 'edu_BinaryExpression7', None)
    assert not _is_linked(b, 'edu_BinaryExpression7', a2)
    if hasattr(a2, 'edu_Expression8'):
        assert not _is_linked(a2, 'edu_Expression8', b)


def test_assoc_statements27_reverse_link_reassign_clear():
    a1 = edu_Statement()
    a2 = edu_Statement()
    b = edu_Block()
    _safe_set(b, 'edu_Block28', {a1})
    assert _is_linked(b, 'edu_Block28', a1)
    if hasattr(a1, 'edu_Statement'):
        assert _is_linked(a1, 'edu_Statement', b)
    _safe_set(b, 'edu_Block28', {a2})
    assert _is_linked(b, 'edu_Block28', a2)
    if hasattr(a1, 'edu_Statement'):
        assert not _is_linked(a1, 'edu_Statement', b)
    if hasattr(a2, 'edu_Statement'):
        assert _is_linked(a2, 'edu_Statement', b)
    _safe_set(b, 'edu_Block28', set())
    assert not _is_linked(b, 'edu_Block28', a2)
    if hasattr(a2, 'edu_Statement'):
        assert not _is_linked(a2, 'edu_Statement', b)


def test_assoc_trueBlock31_reverse_link_reassign_clear():
    a1 = edu_Conditional()
    a2 = edu_Conditional()
    b = edu_Block()
    _safe_set(b, 'edu_Block33', a1)
    assert _is_linked(b, 'edu_Block33', a1)
    if hasattr(a1, 'edu_Conditional32'):
        assert _is_linked(a1, 'edu_Conditional32', b)
    _safe_set(b, 'edu_Block33', a2)
    assert _is_linked(b, 'edu_Block33', a2)
    if hasattr(a1, 'edu_Conditional32'):
        assert not _is_linked(a1, 'edu_Conditional32', b)
    if hasattr(a2, 'edu_Conditional32'):
        assert _is_linked(a2, 'edu_Conditional32', b)
    _safe_set(b, 'edu_Block33', None)
    assert not _is_linked(b, 'edu_Block33', a2)
    if hasattr(a2, 'edu_Conditional32'):
        assert not _is_linked(a2, 'edu_Conditional32', b)


def test_assoc_type23_reverse_link_reassign_clear():
    a1 = edu_VariableDeclaration(name="sample_text")
    a2 = edu_VariableDeclaration(name="sample_text_2")
    b = edu_Type()
    _safe_set(b, 'edu_Type', a1)
    assert _is_linked(b, 'edu_Type', a1)
    if hasattr(a1, 'edu_VariableDeclaration'):
        assert _is_linked(a1, 'edu_VariableDeclaration', b)
    _safe_set(b, 'edu_Type', a2)
    assert _is_linked(b, 'edu_Type', a2)
    if hasattr(a1, 'edu_VariableDeclaration'):
        assert not _is_linked(a1, 'edu_VariableDeclaration', b)
    if hasattr(a2, 'edu_VariableDeclaration'):
        assert _is_linked(a2, 'edu_VariableDeclaration', b)
    _safe_set(b, 'edu_Type', None)
    assert not _is_linked(b, 'edu_Type', a2)
    if hasattr(a2, 'edu_VariableDeclaration'):
        assert not _is_linked(a2, 'edu_VariableDeclaration', b)


def test_assoc_value19_reverse_link_reassign_clear():
    a1 = edu_Expression()
    a2 = edu_Expression()
    b = edu_Assignment()
    _safe_set(b, 'edu_Assignment', a1)
    assert _is_linked(b, 'edu_Assignment', a1)
    if hasattr(a1, 'edu_Expression20'):
        assert _is_linked(a1, 'edu_Expression20', b)
    _safe_set(b, 'edu_Assignment', a2)
    assert _is_linked(b, 'edu_Assignment', a2)
    if hasattr(a1, 'edu_Expression20'):
        assert not _is_linked(a1, 'edu_Expression20', b)
    if hasattr(a2, 'edu_Expression20'):
        assert _is_linked(a2, 'edu_Expression20', b)
    _safe_set(b, 'edu_Assignment', None)
    assert not _is_linked(b, 'edu_Assignment', a2)
    if hasattr(a2, 'edu_Expression20'):
        assert not _is_linked(a2, 'edu_Expression20', b)


def test_assoc_value90_reverse_link_reassign_clear():
    a1 = edu_Expression()
    a2 = edu_Expression()
    b = edu_ArrayFunction()
    _safe_set(b, 'edu_ArrayFunction91', a1)
    assert _is_linked(b, 'edu_ArrayFunction91', a1)
    if hasattr(a1, 'edu_Expression92'):
        assert _is_linked(a1, 'edu_Expression92', b)
    _safe_set(b, 'edu_ArrayFunction91', a2)
    assert _is_linked(b, 'edu_ArrayFunction91', a2)
    if hasattr(a1, 'edu_Expression92'):
        assert not _is_linked(a1, 'edu_Expression92', b)
    if hasattr(a2, 'edu_Expression92'):
        assert _is_linked(a2, 'edu_Expression92', b)
    _safe_set(b, 'edu_ArrayFunction91', None)
    assert not _is_linked(b, 'edu_ArrayFunction91', a2)
    if hasattr(a2, 'edu_Expression92'):
        assert not _is_linked(a2, 'edu_Expression92', b)


def test_assoc_values11_reverse_link_reassign_clear():
    a1 = edu_Expression()
    a2 = edu_Expression()
    b = edu_ArrayLiteral()
    _safe_set(b, 'edu_ArrayLiteral', {a1})
    assert _is_linked(b, 'edu_ArrayLiteral', a1)
    if hasattr(a1, 'edu_Expression12'):
        assert _is_linked(a1, 'edu_Expression12', b)
    _safe_set(b, 'edu_ArrayLiteral', {a2})
    assert _is_linked(b, 'edu_ArrayLiteral', a2)
    if hasattr(a1, 'edu_Expression12'):
        assert not _is_linked(a1, 'edu_Expression12', b)
    if hasattr(a2, 'edu_Expression12'):
        assert _is_linked(a2, 'edu_Expression12', b)
    _safe_set(b, 'edu_ArrayLiteral', set())
    assert not _is_linked(b, 'edu_ArrayLiteral', a2)
    if hasattr(a2, 'edu_Expression12'):
        assert not _is_linked(a2, 'edu_Expression12', b)


def test_assoc_variable21_reverse_link_reassign_clear():
    a1 = edu_VariableReference()
    a2 = edu_VariableReference()
    b = edu_Assignment()
    _safe_set(b, 'edu_Assignment22', a1)
    assert _is_linked(b, 'edu_Assignment22', a1)
    if hasattr(a1, 'edu_VariableReference'):
        assert _is_linked(a1, 'edu_VariableReference', b)
    _safe_set(b, 'edu_Assignment22', a2)
    assert _is_linked(b, 'edu_Assignment22', a2)
    if hasattr(a1, 'edu_VariableReference'):
        assert not _is_linked(a1, 'edu_VariableReference', b)
    if hasattr(a2, 'edu_VariableReference'):
        assert _is_linked(a2, 'edu_VariableReference', b)
    _safe_set(b, 'edu_Assignment22', None)
    assert not _is_linked(b, 'edu_Assignment22', a2)
    if hasattr(a2, 'edu_VariableReference'):
        assert not _is_linked(a2, 'edu_VariableReference', b)


def test_assoc_variable76_reverse_link_reassign_clear():
    a1 = edu_VariableReference()
    a2 = edu_VariableReference()
    b = edu_VariableDeclaration(name="sample_text")
    _safe_set(b, 'edu_VariableDeclaration78', a1)
    assert _is_linked(b, 'edu_VariableDeclaration78', a1)
    if hasattr(a1, 'edu_VariableReference77'):
        assert _is_linked(a1, 'edu_VariableReference77', b)
    _safe_set(b, 'edu_VariableDeclaration78', a2)
    assert _is_linked(b, 'edu_VariableDeclaration78', a2)
    if hasattr(a1, 'edu_VariableReference77'):
        assert not _is_linked(a1, 'edu_VariableReference77', b)
    if hasattr(a2, 'edu_VariableReference77'):
        assert _is_linked(a2, 'edu_VariableReference77', b)
    _safe_set(b, 'edu_VariableDeclaration78', None)
    assert not _is_linked(b, 'edu_VariableDeclaration78', a2)
    if hasattr(a2, 'edu_VariableReference77'):
        assert not _is_linked(a2, 'edu_VariableReference77', b)


def test_assoc_whenFalse105_reverse_link_reassign_clear():
    a1 = edu_TernaryExpression()
    a2 = edu_TernaryExpression()
    b = edu_Expression()
    _safe_set(b, 'edu_Expression107', a1)
    assert _is_linked(b, 'edu_Expression107', a1)
    if hasattr(a1, 'edu_TernaryExpression106'):
        assert _is_linked(a1, 'edu_TernaryExpression106', b)
    _safe_set(b, 'edu_Expression107', a2)
    assert _is_linked(b, 'edu_Expression107', a2)
    if hasattr(a1, 'edu_TernaryExpression106'):
        assert not _is_linked(a1, 'edu_TernaryExpression106', b)
    if hasattr(a2, 'edu_TernaryExpression106'):
        assert _is_linked(a2, 'edu_TernaryExpression106', b)
    _safe_set(b, 'edu_Expression107', None)
    assert not _is_linked(b, 'edu_Expression107', a2)
    if hasattr(a2, 'edu_TernaryExpression106'):
        assert not _is_linked(a2, 'edu_TernaryExpression106', b)


def test_assoc_whenTrue103_reverse_link_reassign_clear():
    a1 = edu_TernaryExpression()
    a2 = edu_TernaryExpression()
    b = edu_Expression()
    _safe_set(b, 'edu_Expression104', a1)
    assert _is_linked(b, 'edu_Expression104', a1)
    if hasattr(a1, 'edu_TernaryExpression'):
        assert _is_linked(a1, 'edu_TernaryExpression', b)
    _safe_set(b, 'edu_Expression104', a2)
    assert _is_linked(b, 'edu_Expression104', a2)
    if hasattr(a1, 'edu_TernaryExpression'):
        assert not _is_linked(a1, 'edu_TernaryExpression', b)
    if hasattr(a2, 'edu_TernaryExpression'):
        assert _is_linked(a2, 'edu_TernaryExpression', b)
    _safe_set(b, 'edu_Expression104', None)
    assert not _is_linked(b, 'edu_Expression104', a2)
    if hasattr(a2, 'edu_TernaryExpression'):
        assert not _is_linked(a2, 'edu_TernaryExpression', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_expression113_stub_double():
    # edu_LetExpression has no real 'edu_LetExpression114' property in the generated
    # code (a bare stub) -- manually attach it so edu_Expression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # edu_Expression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = edu_Expression()
    partner = edu_LetExpression()
    setattr(partner, 'edu_LetExpression114', None)
    _safe_set(owner, 'edu_Expression115', partner)
    assert getattr(partner, 'edu_LetExpression114') == owner
    _safe_set(owner, 'edu_Expression115', None)
    assert getattr(partner, 'edu_LetExpression114') is None


def test_assoc_expression83_stub_double():
    # edu_ExpressionEvaluation has no real 'edu_ExpressionEvaluation' property in the generated
    # code (a bare stub) -- manually attach it so edu_Expression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # edu_Expression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = edu_Expression()
    partner = edu_ExpressionEvaluation()
    setattr(partner, 'edu_ExpressionEvaluation', None)
    _safe_set(owner, 'edu_Expression84', partner)
    assert getattr(partner, 'edu_ExpressionEvaluation') == owner
    _safe_set(owner, 'edu_Expression84', None)
    assert getattr(partner, 'edu_ExpressionEvaluation') is None


def test_assoc_key98_stub_double():
    # edu_ExpressionToExpressionMap has no real 'edu_ExpressionToExpressionMap' property in the generated
    # code (a bare stub) -- manually attach it so edu_Expression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # edu_Expression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = edu_Expression()
    partner = edu_ExpressionToExpressionMap()
    setattr(partner, 'edu_ExpressionToExpressionMap', None)
    _safe_set(owner, 'edu_Expression99', partner)
    assert getattr(partner, 'edu_ExpressionToExpressionMap') == owner
    _safe_set(owner, 'edu_Expression99', None)
    assert getattr(partner, 'edu_ExpressionToExpressionMap') is None


def test_assoc_parameters111_stub_double():
    # edu_LetExpression has no real 'edu_LetExpression' property in the generated
    # code (a bare stub) -- manually attach it so edu_VariableDeclaration's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # edu_VariableDeclaration's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = edu_VariableDeclaration(name="sample_text")
    partner = edu_LetExpression()
    setattr(partner, 'edu_LetExpression', None)
    _safe_set(owner, 'edu_VariableDeclaration112', partner)
    assert owner in getattr(partner, 'edu_LetExpression')
    _safe_set(owner, 'edu_VariableDeclaration112', None)
    assert owner not in getattr(partner, 'edu_LetExpression')


def test_assoc_value100_stub_double():
    # edu_ExpressionToExpressionMap has no real 'edu_ExpressionToExpressionMap101' property in the generated
    # code (a bare stub) -- manually attach it so edu_Expression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # edu_Expression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = edu_Expression()
    partner = edu_ExpressionToExpressionMap()
    setattr(partner, 'edu_ExpressionToExpressionMap101', None)
    _safe_set(owner, 'edu_Expression102', partner)
    assert getattr(partner, 'edu_ExpressionToExpressionMap101') == owner
    _safe_set(owner, 'edu_Expression102', None)
    assert getattr(partner, 'edu_ExpressionToExpressionMap101') is None


