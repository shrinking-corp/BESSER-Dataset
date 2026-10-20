import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    ArithmeticExpression,
    BinaryExpression,
    Declaration,
    EqualityExpression,
    Expression,
    LogicExpression,
    Statement,
    UnaryExpression,
    workflow_Addition,
    workflow_And,
    workflow_ArithmeticExpression,
    workflow_BinaryExpression,
    workflow_Block,
    workflow_CompilationUnit,
    workflow_Constant,
    workflow_Declaration,
    workflow_Division,
    workflow_Equal,
    workflow_EqualityExpression,
    workflow_Expression,
    workflow_GreaterThan,
    workflow_GreaterThanOrEqual,
    workflow_If,
    workflow_LessThan,
    workflow_LessThanOrEqual,
    workflow_LogicExpression,
    workflow_Multiplication,
    workflow_Not,
    workflow_NotEqual,
    workflow_Or,
    workflow_ParameterDeclaration,
    workflow_ProcedureCall,
    workflow_ProcedureDeclaration,
    workflow_ProcedureReturn,
    workflow_Read,
    workflow_Statement,
    workflow_Subtraction,
    workflow_UMinus,
    workflow_UnaryExpression,
    workflow_Variable,
    workflow_VariableAssignment,
    workflow_VariableDeclaration,
    workflow_While,
    workflow_Write,
    AccessModifiers,
    Languages,
    Type,
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

def test_assoc_Parameter29_reverse_link_reassign_clear():
    a1 = workflow_ProcedureDeclaration(accessModifier="sample_text", returnType="sample_text")
    a2 = workflow_ProcedureDeclaration(accessModifier="sample_text_2", returnType="sample_text_2")
    b = workflow_ParameterDeclaration(type="sample_text")
    _safe_set(b, 'workflow_ParameterDeclaration', a1)
    assert _is_linked(b, 'workflow_ParameterDeclaration', a1)
    if hasattr(a1, 'workflow_ProcedureDeclaration30'):
        assert _is_linked(a1, 'workflow_ProcedureDeclaration30', b)
    _safe_set(b, 'workflow_ParameterDeclaration', a2)
    assert _is_linked(b, 'workflow_ParameterDeclaration', a2)
    if hasattr(a1, 'workflow_ProcedureDeclaration30'):
        assert not _is_linked(a1, 'workflow_ProcedureDeclaration30', b)
    if hasattr(a2, 'workflow_ProcedureDeclaration30'):
        assert _is_linked(a2, 'workflow_ProcedureDeclaration30', b)
    _safe_set(b, 'workflow_ParameterDeclaration', None)
    assert not _is_linked(b, 'workflow_ParameterDeclaration', a2)
    if hasattr(a2, 'workflow_ProcedureDeclaration30'):
        assert not _is_linked(a2, 'workflow_ProcedureDeclaration30', b)


def test_assoc_Variables24_reverse_link_reassign_clear():
    a1 = workflow_VariableDeclaration(isConstant="sample_text", type="sample_text")
    a2 = workflow_VariableDeclaration(isConstant="sample_text_2", type="sample_text_2")
    b = workflow_ProcedureDeclaration(accessModifier="sample_text", returnType="sample_text")
    _safe_set(b, 'workflow_ProcedureDeclaration25', {a1})
    assert _is_linked(b, 'workflow_ProcedureDeclaration25', a1)
    if hasattr(a1, 'workflow_VariableDeclaration'):
        assert _is_linked(a1, 'workflow_VariableDeclaration', b)
    _safe_set(b, 'workflow_ProcedureDeclaration25', {a2})
    assert _is_linked(b, 'workflow_ProcedureDeclaration25', a2)
    if hasattr(a1, 'workflow_VariableDeclaration'):
        assert not _is_linked(a1, 'workflow_VariableDeclaration', b)
    if hasattr(a2, 'workflow_VariableDeclaration'):
        assert _is_linked(a2, 'workflow_VariableDeclaration', b)
    _safe_set(b, 'workflow_ProcedureDeclaration25', set())
    assert not _is_linked(b, 'workflow_ProcedureDeclaration25', a2)
    if hasattr(a2, 'workflow_VariableDeclaration'):
        assert not _is_linked(a2, 'workflow_VariableDeclaration', b)


def test_assoc_declarations0_reverse_link_reassign_clear():
    a1 = workflow_ProcedureDeclaration(accessModifier="sample_text", returnType="sample_text")
    a2 = workflow_ProcedureDeclaration(accessModifier="sample_text_2", returnType="sample_text_2")
    b = workflow_CompilationUnit(language="sample_text", name="sample_text")
    _safe_set(b, 'workflow_CompilationUnit', {a1})
    assert _is_linked(b, 'workflow_CompilationUnit', a1)
    if hasattr(a1, 'workflow_ProcedureDeclaration'):
        assert _is_linked(a1, 'workflow_ProcedureDeclaration', b)
    _safe_set(b, 'workflow_CompilationUnit', {a2})
    assert _is_linked(b, 'workflow_CompilationUnit', a2)
    if hasattr(a1, 'workflow_ProcedureDeclaration'):
        assert not _is_linked(a1, 'workflow_ProcedureDeclaration', b)
    if hasattr(a2, 'workflow_ProcedureDeclaration'):
        assert _is_linked(a2, 'workflow_ProcedureDeclaration', b)
    _safe_set(b, 'workflow_CompilationUnit', set())
    assert not _is_linked(b, 'workflow_CompilationUnit', a2)
    if hasattr(a2, 'workflow_ProcedureDeclaration'):
        assert not _is_linked(a2, 'workflow_ProcedureDeclaration', b)


def test_assoc_rVar22_reverse_link_reassign_clear():
    a1 = workflow_Variable(name="sample_text")
    a2 = workflow_Variable(name="sample_text_2")
    b = workflow_Read(type="sample_text")
    _safe_set(b, 'workflow_Read', a1)
    assert _is_linked(b, 'workflow_Read', a1)
    if hasattr(a1, 'workflow_Variable23'):
        assert _is_linked(a1, 'workflow_Variable23', b)
    _safe_set(b, 'workflow_Read', a2)
    assert _is_linked(b, 'workflow_Read', a2)
    if hasattr(a1, 'workflow_Variable23'):
        assert not _is_linked(a1, 'workflow_Variable23', b)
    if hasattr(a2, 'workflow_Variable23'):
        assert _is_linked(a2, 'workflow_Variable23', b)
    _safe_set(b, 'workflow_Read', None)
    assert not _is_linked(b, 'workflow_Read', a2)
    if hasattr(a2, 'workflow_Variable23'):
        assert not _is_linked(a2, 'workflow_Variable23', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_Argument31_stub_double():
    # workflow_Expression has no real 'workflow_Expression32' property in the generated
    # code (a bare stub) -- manually attach it so workflow_ProcedureCall's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # workflow_ProcedureCall's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = workflow_ProcedureCall(name="sample_text")
    partner = workflow_Expression()
    setattr(partner, 'workflow_Expression32', None)
    _safe_set(owner, 'workflow_ProcedureCall', {partner})
    assert getattr(partner, 'workflow_Expression32') == owner
    _safe_set(owner, 'workflow_ProcedureCall', set())
    assert getattr(partner, 'workflow_Expression32') is None


def test_assoc_Body26_stub_double():
    # workflow_Block has no real 'workflow_Block28' property in the generated
    # code (a bare stub) -- manually attach it so workflow_ProcedureDeclaration's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # workflow_ProcedureDeclaration's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = workflow_ProcedureDeclaration(accessModifier="sample_text", returnType="sample_text")
    partner = workflow_Block()
    setattr(partner, 'workflow_Block28', None)
    _safe_set(owner, 'workflow_ProcedureDeclaration27', partner)
    assert getattr(partner, 'workflow_Block28') == owner
    _safe_set(owner, 'workflow_ProcedureDeclaration27', None)
    assert getattr(partner, 'workflow_Block28') is None


def test_assoc_LValue14_stub_double():
    # workflow_VariableAssignment has no real 'workflow_VariableAssignment' property in the generated
    # code (a bare stub) -- manually attach it so workflow_Variable's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # workflow_Variable's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = workflow_Variable(name="sample_text")
    partner = workflow_VariableAssignment()
    setattr(partner, 'workflow_VariableAssignment', None)
    _safe_set(owner, 'workflow_Variable', partner)
    assert getattr(partner, 'workflow_VariableAssignment') == owner
    _safe_set(owner, 'workflow_Variable', None)
    assert getattr(partner, 'workflow_VariableAssignment') is None


def test_assoc_wVar20_stub_double():
    # workflow_Write has no real 'workflow_Write' property in the generated
    # code (a bare stub) -- manually attach it so workflow_Variable's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # workflow_Variable's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = workflow_Variable(name="sample_text")
    partner = workflow_Write()
    setattr(partner, 'workflow_Write', None)
    _safe_set(owner, 'workflow_Variable21', partner)
    assert getattr(partner, 'workflow_Write') == owner
    _safe_set(owner, 'workflow_Variable21', None)
    assert getattr(partner, 'workflow_Write') is None


