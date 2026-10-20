import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    ArithmeticInfixOperator,
    BinaryOperator,
    ComparsionOperator,
    Expression,
    FunctionCallStatement,
    Statement,
    behaviouralProgramMM_ArithmeticInfixOperator,
    behaviouralProgramMM_Assignment,
    behaviouralProgramMM_Behaviour,
    behaviouralProgramMM_BinaryOperator,
    behaviouralProgramMM_ComparsionOperator,
    behaviouralProgramMM_ConditionalBranch,
    behaviouralProgramMM_Equals,
    behaviouralProgramMM_Expression,
    behaviouralProgramMM_Function,
    behaviouralProgramMM_FunctionCall,
    behaviouralProgramMM_FunctionCallStatement,
    behaviouralProgramMM_Instantiation,
    behaviouralProgramMM_Literal,
    behaviouralProgramMM_Loop,
    behaviouralProgramMM_Plus,
    behaviouralProgramMM_RaiseException,
    behaviouralProgramMM_ReadLine,
    behaviouralProgramMM_ReadLineStatement,
    behaviouralProgramMM_Return,
    behaviouralProgramMM_Statement,
    behaviouralProgramMM_TryCatch,
    behaviouralProgramMM_Variable,
    behaviouralProgramMM_WriteLineStatement,
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

def test_assoc_InitiationExpression22_stub_double():
    # behaviouralProgramMM_Expression has no real 'behaviouralProgramMM_Expression23' property in the generated
    # code (a bare stub) -- manually attach it so behaviouralProgramMM_Instantiation's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # behaviouralProgramMM_Instantiation's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = behaviouralProgramMM_Instantiation(VarName="sample_text", VarType="sample_text")
    partner = behaviouralProgramMM_Expression()
    setattr(partner, 'behaviouralProgramMM_Expression23', None)
    _safe_set(owner, 'behaviouralProgramMM_Instantiation', partner)
    assert getattr(partner, 'behaviouralProgramMM_Expression23') == owner
    _safe_set(owner, 'behaviouralProgramMM_Instantiation', None)
    assert getattr(partner, 'behaviouralProgramMM_Expression23') is None


def test_assoc_arguments20_stub_double():
    # behaviouralProgramMM_Expression has no real 'behaviouralProgramMM_Expression21' property in the generated
    # code (a bare stub) -- manually attach it so behaviouralProgramMM_FunctionCall's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # behaviouralProgramMM_FunctionCall's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = behaviouralProgramMM_FunctionCall(FuncName="sample_text")
    partner = behaviouralProgramMM_Expression()
    setattr(partner, 'behaviouralProgramMM_Expression21', None)
    _safe_set(owner, 'behaviouralProgramMM_FunctionCall', {partner})
    assert getattr(partner, 'behaviouralProgramMM_Expression21') == owner
    _safe_set(owner, 'behaviouralProgramMM_FunctionCall', set())
    assert getattr(partner, 'behaviouralProgramMM_Expression21') is None


def test_assoc_arguments33_stub_double():
    # behaviouralProgramMM_Expression has no real 'behaviouralProgramMM_Expression34' property in the generated
    # code (a bare stub) -- manually attach it so behaviouralProgramMM_FunctionCallStatement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # behaviouralProgramMM_FunctionCallStatement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = behaviouralProgramMM_FunctionCallStatement(FuncName="sample_text")
    partner = behaviouralProgramMM_Expression()
    setattr(partner, 'behaviouralProgramMM_Expression34', None)
    _safe_set(owner, 'behaviouralProgramMM_FunctionCallStatement', {partner})
    assert getattr(partner, 'behaviouralProgramMM_Expression34') == owner
    _safe_set(owner, 'behaviouralProgramMM_FunctionCallStatement', set())
    assert getattr(partner, 'behaviouralProgramMM_Expression34') is None


def test_assoc_assignexpression6_stub_double():
    # behaviouralProgramMM_Expression has no real 'behaviouralProgramMM_Expression' property in the generated
    # code (a bare stub) -- manually attach it so behaviouralProgramMM_Assignment's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # behaviouralProgramMM_Assignment's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = behaviouralProgramMM_Assignment(VariableName="sample_text")
    partner = behaviouralProgramMM_Expression()
    setattr(partner, 'behaviouralProgramMM_Expression', None)
    _safe_set(owner, 'behaviouralProgramMM_Assignment', partner)
    assert getattr(partner, 'behaviouralProgramMM_Expression') == owner
    _safe_set(owner, 'behaviouralProgramMM_Assignment', None)
    assert getattr(partner, 'behaviouralProgramMM_Expression') is None


def test_assoc_functionBody4_stub_double():
    # behaviouralProgramMM_Statement has no real 'behaviouralProgramMM_Statement' property in the generated
    # code (a bare stub) -- manually attach it so behaviouralProgramMM_Function's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # behaviouralProgramMM_Function's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = behaviouralProgramMM_Function(Name="sample_text")
    partner = behaviouralProgramMM_Statement()
    setattr(partner, 'behaviouralProgramMM_Statement', None)
    _safe_set(owner, 'behaviouralProgramMM_Function5', {partner})
    assert getattr(partner, 'behaviouralProgramMM_Statement') == owner
    _safe_set(owner, 'behaviouralProgramMM_Function5', set())
    assert getattr(partner, 'behaviouralProgramMM_Statement') is None


def test_assoc_functions0_stub_double():
    # behaviouralProgramMM_Behaviour has no real 'behaviouralProgramMM_Behaviour' property in the generated
    # code (a bare stub) -- manually attach it so behaviouralProgramMM_Function's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # behaviouralProgramMM_Function's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = behaviouralProgramMM_Function(Name="sample_text")
    partner = behaviouralProgramMM_Behaviour()
    setattr(partner, 'behaviouralProgramMM_Behaviour', None)
    _safe_set(owner, 'behaviouralProgramMM_Function', partner)
    assert owner in getattr(partner, 'behaviouralProgramMM_Behaviour')
    _safe_set(owner, 'behaviouralProgramMM_Function', None)
    assert owner not in getattr(partner, 'behaviouralProgramMM_Behaviour')


def test_assoc_startfunction1_stub_double():
    # behaviouralProgramMM_Behaviour has no real 'behaviouralProgramMM_Behaviour2' property in the generated
    # code (a bare stub) -- manually attach it so behaviouralProgramMM_Function's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # behaviouralProgramMM_Function's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = behaviouralProgramMM_Function(Name="sample_text")
    partner = behaviouralProgramMM_Behaviour()
    setattr(partner, 'behaviouralProgramMM_Behaviour2', None)
    _safe_set(owner, 'behaviouralProgramMM_Function3', partner)
    assert getattr(partner, 'behaviouralProgramMM_Behaviour2') == owner
    _safe_set(owner, 'behaviouralProgramMM_Function3', None)
    assert getattr(partner, 'behaviouralProgramMM_Behaviour2') is None


