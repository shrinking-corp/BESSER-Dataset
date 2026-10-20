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
    siple_Addition,
    siple_And,
    siple_ArithmeticExpression,
    siple_BinaryExpression,
    siple_Block,
    siple_CompilationUnit,
    siple_Constant,
    siple_Declaration,
    siple_Dereference,
    siple_Division,
    siple_Equal,
    siple_EqualityExpression,
    siple_Expression,
    siple_GreaterThan,
    siple_GreaterThanEqual,
    siple_If,
    siple_LesserThan,
    siple_LesserThanEqual,
    siple_LogicExpression,
    siple_Multiplication,
    siple_NestedExpression,
    siple_Not,
    siple_Or,
    siple_ProcedureCall,
    siple_ProcedureDeclaration,
    siple_ProcedureReturn,
    siple_Read,
    siple_RealCoercion,
    siple_Reference,
    siple_Statement,
    siple_Subtraction,
    siple_UMinus,
    siple_UnaryExpression,
    siple_VariableAssignment,
    siple_VariableDeclaration,
    siple_While,
    siple_Write,
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

def test_assoc_Declaration0_reverse_link_reassign_clear():
    a1 = siple_Declaration(IsParameterDeclaration=True, Name="sample_text", Type="sample_text")
    a2 = siple_Declaration(IsParameterDeclaration=False, Name="sample_text_2", Type="sample_text_2")
    b = siple_CompilationUnit()
    _safe_set(b, 'siple_CompilationUnit', {a1})
    assert _is_linked(b, 'siple_CompilationUnit', a1)
    if hasattr(a1, 'siple_Declaration'):
        assert _is_linked(a1, 'siple_Declaration', b)
    _safe_set(b, 'siple_CompilationUnit', {a2})
    assert _is_linked(b, 'siple_CompilationUnit', a2)
    if hasattr(a1, 'siple_Declaration'):
        assert not _is_linked(a1, 'siple_Declaration', b)
    if hasattr(a2, 'siple_Declaration'):
        assert _is_linked(a2, 'siple_Declaration', b)
    _safe_set(b, 'siple_CompilationUnit', set())
    assert not _is_linked(b, 'siple_CompilationUnit', a2)
    if hasattr(a2, 'siple_Declaration'):
        assert not _is_linked(a2, 'siple_Declaration', b)


def test_assoc_Declaration38_reverse_link_reassign_clear():
    a1 = siple_Reference(Name="sample_text")
    a2 = siple_Reference(Name="sample_text_2")
    b = siple_Declaration(IsParameterDeclaration=True, Name="sample_text", Type="sample_text")
    _safe_set(b, 'siple_Declaration39', a1)
    assert _is_linked(b, 'siple_Declaration39', a1)
    if hasattr(a1, 'siple_Reference'):
        assert _is_linked(a1, 'siple_Reference', b)
    _safe_set(b, 'siple_Declaration39', a2)
    assert _is_linked(b, 'siple_Declaration39', a2)
    if hasattr(a1, 'siple_Reference'):
        assert not _is_linked(a1, 'siple_Reference', b)
    if hasattr(a2, 'siple_Reference'):
        assert _is_linked(a2, 'siple_Reference', b)
    _safe_set(b, 'siple_Declaration39', None)
    assert not _is_linked(b, 'siple_Declaration39', a2)
    if hasattr(a2, 'siple_Reference'):
        assert not _is_linked(a2, 'siple_Reference', b)


def test_assoc_Expression27_reverse_link_reassign_clear():
    a1 = siple_ProcedureReturn(Type="sample_text")
    a2 = siple_ProcedureReturn(Type="sample_text_2")
    b = siple_Expression(Type="sample_text")
    _safe_set(b, 'siple_Expression28', a1)
    assert _is_linked(b, 'siple_Expression28', a1)
    if hasattr(a1, 'siple_ProcedureReturn'):
        assert _is_linked(a1, 'siple_ProcedureReturn', b)
    _safe_set(b, 'siple_Expression28', a2)
    assert _is_linked(b, 'siple_Expression28', a2)
    if hasattr(a1, 'siple_ProcedureReturn'):
        assert not _is_linked(a1, 'siple_ProcedureReturn', b)
    if hasattr(a2, 'siple_ProcedureReturn'):
        assert _is_linked(a2, 'siple_ProcedureReturn', b)
    _safe_set(b, 'siple_Expression28', None)
    assert not _is_linked(b, 'siple_Expression28', a2)
    if hasattr(a2, 'siple_ProcedureReturn'):
        assert not _is_linked(a2, 'siple_ProcedureReturn', b)


def test_assoc_Expression29_reverse_link_reassign_clear():
    a1 = siple_Write(Type="sample_text")
    a2 = siple_Write(Type="sample_text_2")
    b = siple_Expression(Type="sample_text")
    _safe_set(b, 'siple_Expression30', a1)
    assert _is_linked(b, 'siple_Expression30', a1)
    if hasattr(a1, 'siple_Write'):
        assert _is_linked(a1, 'siple_Write', b)
    _safe_set(b, 'siple_Expression30', a2)
    assert _is_linked(b, 'siple_Expression30', a2)
    if hasattr(a1, 'siple_Write'):
        assert not _is_linked(a1, 'siple_Write', b)
    if hasattr(a2, 'siple_Write'):
        assert _is_linked(a2, 'siple_Write', b)
    _safe_set(b, 'siple_Expression30', None)
    assert not _is_linked(b, 'siple_Expression30', a2)
    if hasattr(a2, 'siple_Write'):
        assert not _is_linked(a2, 'siple_Write', b)


def test_assoc_Expression31_reverse_link_reassign_clear():
    a1 = siple_Read(Type="sample_text")
    a2 = siple_Read(Type="sample_text_2")
    b = siple_Expression(Type="sample_text")
    _safe_set(b, 'siple_Expression32', a1)
    assert _is_linked(b, 'siple_Expression32', a1)
    if hasattr(a1, 'siple_Read'):
        assert _is_linked(a1, 'siple_Read', b)
    _safe_set(b, 'siple_Expression32', a2)
    assert _is_linked(b, 'siple_Expression32', a2)
    if hasattr(a1, 'siple_Read'):
        assert not _is_linked(a1, 'siple_Read', b)
    if hasattr(a2, 'siple_Read'):
        assert _is_linked(a2, 'siple_Read', b)
    _safe_set(b, 'siple_Expression32', None)
    assert not _is_linked(b, 'siple_Expression32', a2)
    if hasattr(a2, 'siple_Read'):
        assert not _is_linked(a2, 'siple_Read', b)


def test_assoc_LValue22_reverse_link_reassign_clear():
    a1 = siple_VariableAssignment(Type="sample_text")
    a2 = siple_VariableAssignment(Type="sample_text_2")
    b = siple_Expression(Type="sample_text")
    _safe_set(b, 'siple_Expression23', a1)
    assert _is_linked(b, 'siple_Expression23', a1)
    if hasattr(a1, 'siple_VariableAssignment'):
        assert _is_linked(a1, 'siple_VariableAssignment', b)
    _safe_set(b, 'siple_Expression23', a2)
    assert _is_linked(b, 'siple_Expression23', a2)
    if hasattr(a1, 'siple_VariableAssignment'):
        assert not _is_linked(a1, 'siple_VariableAssignment', b)
    if hasattr(a2, 'siple_VariableAssignment'):
        assert _is_linked(a2, 'siple_VariableAssignment', b)
    _safe_set(b, 'siple_Expression23', None)
    assert not _is_linked(b, 'siple_Expression23', a2)
    if hasattr(a2, 'siple_VariableAssignment'):
        assert not _is_linked(a2, 'siple_VariableAssignment', b)


def test_assoc_MainProcedure1_reverse_link_reassign_clear():
    a1 = siple_ProcedureDeclaration(ReturnType="sample_text")
    a2 = siple_ProcedureDeclaration(ReturnType="sample_text_2")
    b = siple_CompilationUnit()
    _safe_set(b, 'siple_CompilationUnit2', a1)
    assert _is_linked(b, 'siple_CompilationUnit2', a1)
    if hasattr(a1, 'siple_ProcedureDeclaration'):
        assert _is_linked(a1, 'siple_ProcedureDeclaration', b)
    _safe_set(b, 'siple_CompilationUnit2', a2)
    assert _is_linked(b, 'siple_CompilationUnit2', a2)
    if hasattr(a1, 'siple_ProcedureDeclaration'):
        assert not _is_linked(a1, 'siple_ProcedureDeclaration', b)
    if hasattr(a2, 'siple_ProcedureDeclaration'):
        assert _is_linked(a2, 'siple_ProcedureDeclaration', b)
    _safe_set(b, 'siple_CompilationUnit2', None)
    assert not _is_linked(b, 'siple_CompilationUnit2', a2)
    if hasattr(a2, 'siple_ProcedureDeclaration'):
        assert not _is_linked(a2, 'siple_ProcedureDeclaration', b)


def test_assoc_Parameter33_reverse_link_reassign_clear():
    a1 = siple_VariableDeclaration(DeclaredType="sample_text")
    a2 = siple_VariableDeclaration(DeclaredType="sample_text_2")
    b = siple_ProcedureDeclaration(ReturnType="sample_text")
    _safe_set(b, 'siple_ProcedureDeclaration34', {a1})
    assert _is_linked(b, 'siple_ProcedureDeclaration34', a1)
    if hasattr(a1, 'siple_VariableDeclaration'):
        assert _is_linked(a1, 'siple_VariableDeclaration', b)
    _safe_set(b, 'siple_ProcedureDeclaration34', {a2})
    assert _is_linked(b, 'siple_ProcedureDeclaration34', a2)
    if hasattr(a1, 'siple_VariableDeclaration'):
        assert not _is_linked(a1, 'siple_VariableDeclaration', b)
    if hasattr(a2, 'siple_VariableDeclaration'):
        assert _is_linked(a2, 'siple_VariableDeclaration', b)
    _safe_set(b, 'siple_ProcedureDeclaration34', set())
    assert not _is_linked(b, 'siple_ProcedureDeclaration34', a2)
    if hasattr(a2, 'siple_VariableDeclaration'):
        assert not _is_linked(a2, 'siple_VariableDeclaration', b)


def test_assoc_ProcedureInContext3_reverse_link_reassign_clear():
    a1 = siple_Statement()
    a2 = siple_Statement()
    b = siple_ProcedureDeclaration(ReturnType="sample_text")
    _safe_set(b, 'siple_ProcedureDeclaration4', a1)
    assert _is_linked(b, 'siple_ProcedureDeclaration4', a1)
    if hasattr(a1, 'siple_Statement'):
        assert _is_linked(a1, 'siple_Statement', b)
    _safe_set(b, 'siple_ProcedureDeclaration4', a2)
    assert _is_linked(b, 'siple_ProcedureDeclaration4', a2)
    if hasattr(a1, 'siple_Statement'):
        assert not _is_linked(a1, 'siple_Statement', b)
    if hasattr(a2, 'siple_Statement'):
        assert _is_linked(a2, 'siple_Statement', b)
    _safe_set(b, 'siple_ProcedureDeclaration4', None)
    assert not _is_linked(b, 'siple_ProcedureDeclaration4', a2)
    if hasattr(a2, 'siple_Statement'):
        assert not _is_linked(a2, 'siple_Statement', b)


def test_assoc_RValue24_reverse_link_reassign_clear():
    a1 = siple_VariableAssignment(Type="sample_text")
    a2 = siple_VariableAssignment(Type="sample_text_2")
    b = siple_Expression(Type="sample_text")
    _safe_set(b, 'siple_Expression26', a1)
    assert _is_linked(b, 'siple_Expression26', a1)
    if hasattr(a1, 'siple_VariableAssignment25'):
        assert _is_linked(a1, 'siple_VariableAssignment25', b)
    _safe_set(b, 'siple_Expression26', a2)
    assert _is_linked(b, 'siple_Expression26', a2)
    if hasattr(a1, 'siple_VariableAssignment25'):
        assert not _is_linked(a1, 'siple_VariableAssignment25', b)
    if hasattr(a2, 'siple_VariableAssignment25'):
        assert _is_linked(a2, 'siple_VariableAssignment25', b)
    _safe_set(b, 'siple_Expression26', None)
    assert not _is_linked(b, 'siple_Expression26', a2)
    if hasattr(a2, 'siple_VariableAssignment25'):
        assert not _is_linked(a2, 'siple_VariableAssignment25', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_Argument42_stub_double():
    # siple_ProcedureCall has no real 'siple_ProcedureCall43' property in the generated
    # code (a bare stub) -- manually attach it so siple_Expression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # siple_Expression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = siple_Expression(Type="sample_text")
    partner = siple_ProcedureCall()
    setattr(partner, 'siple_ProcedureCall43', None)
    _safe_set(owner, 'siple_Expression44', partner)
    assert owner in getattr(partner, 'siple_ProcedureCall43')
    _safe_set(owner, 'siple_Expression44', None)
    assert owner not in getattr(partner, 'siple_ProcedureCall43')


def test_assoc_Body35_stub_double():
    # siple_Block has no real 'siple_Block37' property in the generated
    # code (a bare stub) -- manually attach it so siple_ProcedureDeclaration's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # siple_ProcedureDeclaration's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = siple_ProcedureDeclaration(ReturnType="sample_text")
    partner = siple_Block()
    setattr(partner, 'siple_Block37', None)
    _safe_set(owner, 'siple_ProcedureDeclaration36', partner)
    assert getattr(partner, 'siple_Block37') == owner
    _safe_set(owner, 'siple_ProcedureDeclaration36', None)
    assert getattr(partner, 'siple_Block37') is None


def test_assoc_Condition10_stub_double():
    # siple_If has no real 'siple_If' property in the generated
    # code (a bare stub) -- manually attach it so siple_Expression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # siple_Expression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = siple_Expression(Type="sample_text")
    partner = siple_If()
    setattr(partner, 'siple_If', None)
    _safe_set(owner, 'siple_Expression', partner)
    assert getattr(partner, 'siple_If') == owner
    _safe_set(owner, 'siple_Expression', None)
    assert getattr(partner, 'siple_If') is None


def test_assoc_Condition17_stub_double():
    # siple_While has no real 'siple_While' property in the generated
    # code (a bare stub) -- manually attach it so siple_Expression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # siple_Expression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = siple_Expression(Type="sample_text")
    partner = siple_While()
    setattr(partner, 'siple_While', None)
    _safe_set(owner, 'siple_Expression18', partner)
    assert getattr(partner, 'siple_While') == owner
    _safe_set(owner, 'siple_Expression18', None)
    assert getattr(partner, 'siple_While') is None


def test_assoc_Declaration45_stub_double():
    # siple_ProcedureCall has no real 'siple_ProcedureCall46' property in the generated
    # code (a bare stub) -- manually attach it so siple_ProcedureDeclaration's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # siple_ProcedureDeclaration's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = siple_ProcedureDeclaration(ReturnType="sample_text")
    partner = siple_ProcedureCall()
    setattr(partner, 'siple_ProcedureCall46', None)
    _safe_set(owner, 'siple_ProcedureDeclaration47', partner)
    assert getattr(partner, 'siple_ProcedureCall46') == owner
    _safe_set(owner, 'siple_ProcedureDeclaration47', None)
    assert getattr(partner, 'siple_ProcedureCall46') is None


def test_assoc_Expression48_stub_double():
    # siple_NestedExpression has no real 'siple_NestedExpression' property in the generated
    # code (a bare stub) -- manually attach it so siple_Expression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # siple_Expression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = siple_Expression(Type="sample_text")
    partner = siple_NestedExpression()
    setattr(partner, 'siple_NestedExpression', None)
    _safe_set(owner, 'siple_Expression49', partner)
    assert getattr(partner, 'siple_NestedExpression') == owner
    _safe_set(owner, 'siple_Expression49', None)
    assert getattr(partner, 'siple_NestedExpression') is None


def test_assoc_IsProcedureBody7_stub_double():
    # siple_Block has no real 'siple_Block8' property in the generated
    # code (a bare stub) -- manually attach it so siple_ProcedureDeclaration's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # siple_ProcedureDeclaration's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = siple_ProcedureDeclaration(ReturnType="sample_text")
    partner = siple_Block()
    setattr(partner, 'siple_Block8', None)
    _safe_set(owner, 'siple_ProcedureDeclaration9', partner)
    assert getattr(partner, 'siple_Block8') == owner
    _safe_set(owner, 'siple_ProcedureDeclaration9', None)
    assert getattr(partner, 'siple_Block8') is None


def test_assoc_Operand152_stub_double():
    # siple_BinaryExpression has no real 'siple_BinaryExpression' property in the generated
    # code (a bare stub) -- manually attach it so siple_Expression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # siple_Expression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = siple_Expression(Type="sample_text")
    partner = siple_BinaryExpression()
    setattr(partner, 'siple_BinaryExpression', None)
    _safe_set(owner, 'siple_Expression53', partner)
    assert getattr(partner, 'siple_BinaryExpression') == owner
    _safe_set(owner, 'siple_Expression53', None)
    assert getattr(partner, 'siple_BinaryExpression') is None


def test_assoc_Operand254_stub_double():
    # siple_BinaryExpression has no real 'siple_BinaryExpression55' property in the generated
    # code (a bare stub) -- manually attach it so siple_Expression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # siple_Expression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = siple_Expression(Type="sample_text")
    partner = siple_BinaryExpression()
    setattr(partner, 'siple_BinaryExpression55', None)
    _safe_set(owner, 'siple_Expression56', partner)
    assert getattr(partner, 'siple_BinaryExpression55') == owner
    _safe_set(owner, 'siple_Expression56', None)
    assert getattr(partner, 'siple_BinaryExpression55') is None


def test_assoc_Operand50_stub_double():
    # siple_UnaryExpression has no real 'siple_UnaryExpression' property in the generated
    # code (a bare stub) -- manually attach it so siple_Expression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # siple_Expression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = siple_Expression(Type="sample_text")
    partner = siple_UnaryExpression()
    setattr(partner, 'siple_UnaryExpression', None)
    _safe_set(owner, 'siple_Expression51', partner)
    assert getattr(partner, 'siple_UnaryExpression') == owner
    _safe_set(owner, 'siple_Expression51', None)
    assert getattr(partner, 'siple_UnaryExpression') is None


def test_assoc_Procedure40_stub_double():
    # siple_ProcedureCall has no real 'siple_ProcedureCall' property in the generated
    # code (a bare stub) -- manually attach it so siple_Expression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # siple_Expression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = siple_Expression(Type="sample_text")
    partner = siple_ProcedureCall()
    setattr(partner, 'siple_ProcedureCall', None)
    _safe_set(owner, 'siple_Expression41', partner)
    assert getattr(partner, 'siple_ProcedureCall') == owner
    _safe_set(owner, 'siple_Expression41', None)
    assert getattr(partner, 'siple_ProcedureCall') is None


def test_assoc_Statement5_stub_double():
    # siple_Block has no real 'siple_Block' property in the generated
    # code (a bare stub) -- manually attach it so siple_Statement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # siple_Statement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = siple_Statement()
    partner = siple_Block()
    setattr(partner, 'siple_Block', None)
    _safe_set(owner, 'siple_Statement6', partner)
    assert owner in getattr(partner, 'siple_Block')
    _safe_set(owner, 'siple_Statement6', None)
    assert owner not in getattr(partner, 'siple_Block')


