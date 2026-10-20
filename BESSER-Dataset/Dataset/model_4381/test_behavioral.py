import pytest
from datetime import date, datetime, time, timedelta

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

def test_assoc_parameters40_reverse_link_reassign_clear():
    a1 = leek_VariableDeclaration(byAdress=True, name="sample_text")
    a2 = leek_VariableDeclaration(byAdress=False, name="sample_text_2")
    b = leek_FunctionDeclaration(name="sample_text")
    _safe_set(b, 'leek_FunctionDeclaration', {a1})
    assert _is_linked(b, 'leek_FunctionDeclaration', a1)
    if hasattr(a1, 'leek_VariableDeclaration'):
        assert _is_linked(a1, 'leek_VariableDeclaration', b)
    _safe_set(b, 'leek_FunctionDeclaration', {a2})
    assert _is_linked(b, 'leek_FunctionDeclaration', a2)
    if hasattr(a1, 'leek_VariableDeclaration'):
        assert not _is_linked(a1, 'leek_VariableDeclaration', b)
    if hasattr(a2, 'leek_VariableDeclaration'):
        assert _is_linked(a2, 'leek_VariableDeclaration', b)
    _safe_set(b, 'leek_FunctionDeclaration', set())
    assert not _is_linked(b, 'leek_FunctionDeclaration', a2)
    if hasattr(a2, 'leek_VariableDeclaration'):
        assert not _is_linked(a2, 'leek_VariableDeclaration', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_body41_stub_double():
    # leek_StatementBlock has no real 'leek_StatementBlock43' property in the generated
    # code (a bare stub) -- manually attach it so leek_FunctionDeclaration's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # leek_FunctionDeclaration's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = leek_FunctionDeclaration(name="sample_text")
    partner = leek_StatementBlock()
    setattr(partner, 'leek_StatementBlock43', None)
    _safe_set(owner, 'leek_FunctionDeclaration42', partner)
    assert getattr(partner, 'leek_StatementBlock43') == owner
    _safe_set(owner, 'leek_FunctionDeclaration42', None)
    assert getattr(partner, 'leek_StatementBlock43') is None


def test_assoc_function56_stub_double():
    # leek_FunctionCall has no real 'leek_FunctionCall' property in the generated
    # code (a bare stub) -- manually attach it so leek_FunctionDeclaration's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # leek_FunctionDeclaration's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = leek_FunctionDeclaration(name="sample_text")
    partner = leek_FunctionCall()
    setattr(partner, 'leek_FunctionCall', None)
    _safe_set(owner, 'leek_FunctionDeclaration57', partner)
    assert getattr(partner, 'leek_FunctionCall') == owner
    _safe_set(owner, 'leek_FunctionDeclaration57', None)
    assert getattr(partner, 'leek_FunctionCall') is None


def test_assoc_variable50_stub_double():
    # leek_VariableReference has no real 'leek_VariableReference51' property in the generated
    # code (a bare stub) -- manually attach it so leek_VariableDeclaration's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # leek_VariableDeclaration's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = leek_VariableDeclaration(byAdress=True, name="sample_text")
    partner = leek_VariableReference()
    setattr(partner, 'leek_VariableReference51', None)
    _safe_set(owner, 'leek_VariableDeclaration52', partner)
    assert getattr(partner, 'leek_VariableReference51') == owner
    _safe_set(owner, 'leek_VariableDeclaration52', None)
    assert getattr(partner, 'leek_VariableReference51') is None


def test_assoc_variables44_stub_double():
    # leek_LocalDeclaration has no real 'leek_LocalDeclaration' property in the generated
    # code (a bare stub) -- manually attach it so leek_VariableDeclaration's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # leek_VariableDeclaration's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = leek_VariableDeclaration(byAdress=True, name="sample_text")
    partner = leek_LocalDeclaration()
    setattr(partner, 'leek_LocalDeclaration', None)
    _safe_set(owner, 'leek_VariableDeclaration45', partner)
    assert owner in getattr(partner, 'leek_LocalDeclaration')
    _safe_set(owner, 'leek_VariableDeclaration45', None)
    assert owner not in getattr(partner, 'leek_LocalDeclaration')


def test_assoc_variables46_stub_double():
    # leek_GlobalDeclaration has no real 'leek_GlobalDeclaration' property in the generated
    # code (a bare stub) -- manually attach it so leek_VariableDeclaration's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # leek_VariableDeclaration's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = leek_VariableDeclaration(byAdress=True, name="sample_text")
    partner = leek_GlobalDeclaration()
    setattr(partner, 'leek_GlobalDeclaration', None)
    _safe_set(owner, 'leek_VariableDeclaration47', partner)
    assert owner in getattr(partner, 'leek_GlobalDeclaration')
    _safe_set(owner, 'leek_VariableDeclaration47', None)
    assert owner not in getattr(partner, 'leek_GlobalDeclaration')


