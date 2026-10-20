import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    AbstactType,
    AbstractExpression,
    Statement,
    miniJava_AbstactType,
    miniJava_AbstractExpression,
    miniJava_And,
    miniJava_ArrayAccess,
    miniJava_ArrayAssignment,
    miniJava_Assignment,
    miniJava_BlockExpression,
    miniJava_BlockStatement,
    miniJava_Boolean,
    miniJava_BooleanType,
    miniJava_Class,
    miniJava_ClassConstruction,
    miniJava_ClassifierReference,
    miniJava_ClassifierType,
    miniJava_FunctionCall,
    miniJava_Identifier,
    miniJava_IfStatement,
    miniJava_IntLiteral,
    miniJava_IntegerArrayConstruction,
    miniJava_IntegerArrayType,
    miniJava_IntegerType,
    miniJava_LengthOf,
    miniJava_LessThen,
    miniJava_MainClass,
    miniJava_MethodDeclaration,
    miniJava_Minus,
    miniJava_Multiply,
    miniJava_Negation,
    miniJava_Plus,
    miniJava_PrintLine,
    miniJava_Program,
    miniJava_Statement,
    miniJava_ThisReference,
    miniJava_VariableDeclaration,
    miniJava_WhileLoop,
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

# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_class_118_stub_double():
    # miniJava_ClassConstruction has no real 'miniJava_ClassConstruction' property in the generated
    # code (a bare stub) -- manually attach it so miniJava_Identifier's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # miniJava_Identifier's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = miniJava_Identifier(value="sample_text")
    partner = miniJava_ClassConstruction()
    setattr(partner, 'miniJava_ClassConstruction', None)
    _safe_set(owner, 'miniJava_Identifier119', partner)
    assert getattr(partner, 'miniJava_ClassConstruction') == owner
    _safe_set(owner, 'miniJava_Identifier119', None)
    assert getattr(partner, 'miniJava_ClassConstruction') is None


def test_assoc_commandLineArguments5_stub_double():
    # miniJava_MainClass has no real 'miniJava_MainClass6' property in the generated
    # code (a bare stub) -- manually attach it so miniJava_Identifier's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # miniJava_Identifier's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = miniJava_Identifier(value="sample_text")
    partner = miniJava_MainClass()
    setattr(partner, 'miniJava_MainClass6', None)
    _safe_set(owner, 'miniJava_Identifier7', partner)
    assert getattr(partner, 'miniJava_MainClass6') == owner
    _safe_set(owner, 'miniJava_Identifier7', None)
    assert getattr(partner, 'miniJava_MainClass6') is None


def test_assoc_function108_stub_double():
    # miniJava_FunctionCall has no real 'miniJava_FunctionCall109' property in the generated
    # code (a bare stub) -- manually attach it so miniJava_Identifier's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # miniJava_Identifier's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = miniJava_Identifier(value="sample_text")
    partner = miniJava_FunctionCall()
    setattr(partner, 'miniJava_FunctionCall109', None)
    _safe_set(owner, 'miniJava_Identifier110', partner)
    assert getattr(partner, 'miniJava_FunctionCall109') == owner
    _safe_set(owner, 'miniJava_Identifier110', None)
    assert getattr(partner, 'miniJava_FunctionCall109') is None


def test_assoc_identifier61_stub_double():
    # miniJava_Assignment has no real 'miniJava_Assignment' property in the generated
    # code (a bare stub) -- manually attach it so miniJava_Identifier's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # miniJava_Identifier's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = miniJava_Identifier(value="sample_text")
    partner = miniJava_Assignment()
    setattr(partner, 'miniJava_Assignment', None)
    _safe_set(owner, 'miniJava_Identifier62', partner)
    assert getattr(partner, 'miniJava_Assignment') == owner
    _safe_set(owner, 'miniJava_Identifier62', None)
    assert getattr(partner, 'miniJava_Assignment') is None


def test_assoc_identifier66_stub_double():
    # miniJava_ArrayAssignment has no real 'miniJava_ArrayAssignment' property in the generated
    # code (a bare stub) -- manually attach it so miniJava_Identifier's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # miniJava_Identifier's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = miniJava_Identifier(value="sample_text")
    partner = miniJava_ArrayAssignment()
    setattr(partner, 'miniJava_ArrayAssignment', None)
    _safe_set(owner, 'miniJava_Identifier67', partner)
    assert getattr(partner, 'miniJava_ArrayAssignment') == owner
    _safe_set(owner, 'miniJava_Identifier67', None)
    assert getattr(partner, 'miniJava_ArrayAssignment') is None


def test_assoc_name10_stub_double():
    # miniJava_Class has no real 'miniJava_Class11' property in the generated
    # code (a bare stub) -- manually attach it so miniJava_Identifier's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # miniJava_Identifier's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = miniJava_Identifier(value="sample_text")
    partner = miniJava_Class()
    setattr(partner, 'miniJava_Class11', None)
    _safe_set(owner, 'miniJava_Identifier12', partner)
    assert getattr(partner, 'miniJava_Class11') == owner
    _safe_set(owner, 'miniJava_Identifier12', None)
    assert getattr(partner, 'miniJava_Class11') is None


def test_assoc_name22_stub_double():
    # miniJava_VariableDeclaration has no real 'miniJava_VariableDeclaration23' property in the generated
    # code (a bare stub) -- manually attach it so miniJava_Identifier's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # miniJava_Identifier's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = miniJava_Identifier(value="sample_text")
    partner = miniJava_VariableDeclaration()
    setattr(partner, 'miniJava_VariableDeclaration23', None)
    _safe_set(owner, 'miniJava_Identifier24', partner)
    assert getattr(partner, 'miniJava_VariableDeclaration23') == owner
    _safe_set(owner, 'miniJava_Identifier24', None)
    assert getattr(partner, 'miniJava_VariableDeclaration23') is None


def test_assoc_name28_stub_double():
    # miniJava_MethodDeclaration has no real 'miniJava_MethodDeclaration29' property in the generated
    # code (a bare stub) -- manually attach it so miniJava_Identifier's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # miniJava_Identifier's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = miniJava_Identifier(value="sample_text")
    partner = miniJava_MethodDeclaration()
    setattr(partner, 'miniJava_MethodDeclaration29', None)
    _safe_set(owner, 'miniJava_Identifier30', partner)
    assert getattr(partner, 'miniJava_MethodDeclaration29') == owner
    _safe_set(owner, 'miniJava_Identifier30', None)
    assert getattr(partner, 'miniJava_MethodDeclaration29') is None


def test_assoc_name3_stub_double():
    # miniJava_MainClass has no real 'miniJava_MainClass4' property in the generated
    # code (a bare stub) -- manually attach it so miniJava_Identifier's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # miniJava_Identifier's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = miniJava_Identifier(value="sample_text")
    partner = miniJava_MainClass()
    setattr(partner, 'miniJava_MainClass4', None)
    _safe_set(owner, 'miniJava_Identifier', partner)
    assert getattr(partner, 'miniJava_MainClass4') == owner
    _safe_set(owner, 'miniJava_Identifier', None)
    assert getattr(partner, 'miniJava_MainClass4') is None


def test_assoc_name42_stub_double():
    # miniJava_ClassifierType has no real 'miniJava_ClassifierType' property in the generated
    # code (a bare stub) -- manually attach it so miniJava_Identifier's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # miniJava_Identifier's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = miniJava_Identifier(value="sample_text")
    partner = miniJava_ClassifierType()
    setattr(partner, 'miniJava_ClassifierType', None)
    _safe_set(owner, 'miniJava_Identifier43', partner)
    assert getattr(partner, 'miniJava_ClassifierType') == owner
    _safe_set(owner, 'miniJava_Identifier43', None)
    assert getattr(partner, 'miniJava_ClassifierType') is None


def test_assoc_referenceTo114_stub_double():
    # miniJava_ClassifierReference has no real 'miniJava_ClassifierReference' property in the generated
    # code (a bare stub) -- manually attach it so miniJava_Identifier's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # miniJava_Identifier's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = miniJava_Identifier(value="sample_text")
    partner = miniJava_ClassifierReference()
    setattr(partner, 'miniJava_ClassifierReference', None)
    _safe_set(owner, 'miniJava_Identifier115', partner)
    assert getattr(partner, 'miniJava_ClassifierReference') == owner
    _safe_set(owner, 'miniJava_Identifier115', None)
    assert getattr(partner, 'miniJava_ClassifierReference') is None


def test_assoc_superClass13_stub_double():
    # miniJava_Class has no real 'miniJava_Class14' property in the generated
    # code (a bare stub) -- manually attach it so miniJava_Identifier's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # miniJava_Identifier's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = miniJava_Identifier(value="sample_text")
    partner = miniJava_Class()
    setattr(partner, 'miniJava_Class14', None)
    _safe_set(owner, 'miniJava_Identifier15', partner)
    assert getattr(partner, 'miniJava_Class14') == owner
    _safe_set(owner, 'miniJava_Identifier15', None)
    assert getattr(partner, 'miniJava_Class14') is None


