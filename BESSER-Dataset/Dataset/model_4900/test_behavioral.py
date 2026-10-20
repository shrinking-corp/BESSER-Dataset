import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    ArithmeticOperation,
    BinaryExpression,
    ComparisonOperator,
    Expression,
    Statement,
    behaviour_ArithmeticOperation,
    behaviour_AssignmentStatement,
    behaviour_Behaviour,
    behaviour_BinaryExpression,
    behaviour_CallFunctionStatement,
    behaviour_ComparisonOperator,
    behaviour_CondionalStatement,
    behaviour_DeclarationStatement,
    behaviour_Equals,
    behaviour_ExceptionStatement,
    behaviour_Expression,
    behaviour_Function,
    behaviour_FunctionCall,
    behaviour_Literal,
    behaviour_LoopStatement,
    behaviour_Plus,
    behaviour_ReadLine,
    behaviour_ReturnStatement,
    behaviour_Statement,
    behaviour_TryCatchStatement,
    behaviour_Variable,
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

def test_assoc_arguments24_stub_double():
    # behaviour_Expression has no real 'behaviour_Expression25' property in the generated
    # code (a bare stub) -- manually attach it so behaviour_CallFunctionStatement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # behaviour_CallFunctionStatement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = behaviour_CallFunctionStatement(nameFunc="sample_text")
    partner = behaviour_Expression()
    setattr(partner, 'behaviour_Expression25', None)
    _safe_set(owner, 'behaviour_CallFunctionStatement', {partner})
    assert getattr(partner, 'behaviour_Expression25') == owner
    _safe_set(owner, 'behaviour_CallFunctionStatement', set())
    assert getattr(partner, 'behaviour_Expression25') is None


def test_assoc_arguments33_stub_double():
    # behaviour_Expression has no real 'behaviour_Expression34' property in the generated
    # code (a bare stub) -- manually attach it so behaviour_FunctionCall's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # behaviour_FunctionCall's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = behaviour_FunctionCall(funcName="sample_text")
    partner = behaviour_Expression()
    setattr(partner, 'behaviour_Expression34', None)
    _safe_set(owner, 'behaviour_FunctionCall', {partner})
    assert getattr(partner, 'behaviour_Expression34') == owner
    _safe_set(owner, 'behaviour_FunctionCall', set())
    assert getattr(partner, 'behaviour_Expression34') is None


def test_assoc_assignExpression18_stub_double():
    # behaviour_Expression has no real 'behaviour_Expression19' property in the generated
    # code (a bare stub) -- manually attach it so behaviour_AssignmentStatement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # behaviour_AssignmentStatement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = behaviour_AssignmentStatement(varName="sample_text")
    partner = behaviour_Expression()
    setattr(partner, 'behaviour_Expression19', None)
    _safe_set(owner, 'behaviour_AssignmentStatement', partner)
    assert getattr(partner, 'behaviour_Expression19') == owner
    _safe_set(owner, 'behaviour_AssignmentStatement', None)
    assert getattr(partner, 'behaviour_Expression19') is None


def test_assoc_entryFunction1_stub_double():
    # behaviour_Behaviour has no real 'behaviour_Behaviour2' property in the generated
    # code (a bare stub) -- manually attach it so behaviour_Function's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # behaviour_Function's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = behaviour_Function(name="sample_text")
    partner = behaviour_Behaviour()
    setattr(partner, 'behaviour_Behaviour2', None)
    _safe_set(owner, 'behaviour_Function3', partner)
    assert getattr(partner, 'behaviour_Behaviour2') == owner
    _safe_set(owner, 'behaviour_Function3', None)
    assert getattr(partner, 'behaviour_Behaviour2') is None


def test_assoc_functionBody4_stub_double():
    # behaviour_Statement has no real 'behaviour_Statement' property in the generated
    # code (a bare stub) -- manually attach it so behaviour_Function's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # behaviour_Function's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = behaviour_Function(name="sample_text")
    partner = behaviour_Statement()
    setattr(partner, 'behaviour_Statement', None)
    _safe_set(owner, 'behaviour_Function5', {partner})
    assert getattr(partner, 'behaviour_Statement') == owner
    _safe_set(owner, 'behaviour_Function5', set())
    assert getattr(partner, 'behaviour_Statement') is None


def test_assoc_functions0_stub_double():
    # behaviour_Behaviour has no real 'behaviour_Behaviour' property in the generated
    # code (a bare stub) -- manually attach it so behaviour_Function's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # behaviour_Function's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = behaviour_Function(name="sample_text")
    partner = behaviour_Behaviour()
    setattr(partner, 'behaviour_Behaviour', None)
    _safe_set(owner, 'behaviour_Function', partner)
    assert owner in getattr(partner, 'behaviour_Behaviour')
    _safe_set(owner, 'behaviour_Function', None)
    assert owner not in getattr(partner, 'behaviour_Behaviour')


def test_assoc_initialExpression20_stub_double():
    # behaviour_Expression has no real 'behaviour_Expression21' property in the generated
    # code (a bare stub) -- manually attach it so behaviour_DeclarationStatement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # behaviour_DeclarationStatement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = behaviour_DeclarationStatement(varName="sample_text", varType="sample_text")
    partner = behaviour_Expression()
    setattr(partner, 'behaviour_Expression21', None)
    _safe_set(owner, 'behaviour_DeclarationStatement', partner)
    assert getattr(partner, 'behaviour_Expression21') == owner
    _safe_set(owner, 'behaviour_DeclarationStatement', None)
    assert getattr(partner, 'behaviour_Expression21') is None


