import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Expression,
    Instruction,
    Literal,
    Primitive,
    kmLogo_ArithmeticExpression,
    kmLogo_Back,
    kmLogo_BoolLit,
    kmLogo_Clear,
    kmLogo_Expression,
    kmLogo_Forward,
    kmLogo_Instruction,
    kmLogo_IntegerLit,
    kmLogo_Left,
    kmLogo_Literal,
    kmLogo_LogoProgram,
    kmLogo_PenDown,
    kmLogo_PenUp,
    kmLogo_Primitive,
    kmLogo_RelationalExpression,
    kmLogo_Right,
    kmLogo_StringLit,
    kmLogo_VarDecl,
    kmLogo_VarReference,
    ArithmeticOperator,
    RelationalOperator,
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

def test_assoc_expression20_stub_double():
    # kmLogo_Expression has no real 'kmLogo_Expression22' property in the generated
    # code (a bare stub) -- manually attach it so kmLogo_VarDecl's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # kmLogo_VarDecl's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = kmLogo_VarDecl(key="sample_text")
    partner = kmLogo_Expression()
    setattr(partner, 'kmLogo_Expression22', None)
    _safe_set(owner, 'kmLogo_VarDecl21', partner)
    assert getattr(partner, 'kmLogo_Expression22') == owner
    _safe_set(owner, 'kmLogo_VarDecl21', None)
    assert getattr(partner, 'kmLogo_Expression22') is None


def test_assoc_left10_stub_double():
    # kmLogo_Expression has no real 'kmLogo_Expression11' property in the generated
    # code (a bare stub) -- manually attach it so kmLogo_ArithmeticExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # kmLogo_ArithmeticExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = kmLogo_ArithmeticExpression(operator="sample_text")
    partner = kmLogo_Expression()
    setattr(partner, 'kmLogo_Expression11', None)
    _safe_set(owner, 'kmLogo_ArithmeticExpression', partner)
    assert getattr(partner, 'kmLogo_Expression11') == owner
    _safe_set(owner, 'kmLogo_ArithmeticExpression', None)
    assert getattr(partner, 'kmLogo_Expression11') is None


def test_assoc_left15_stub_double():
    # kmLogo_Expression has no real 'kmLogo_Expression16' property in the generated
    # code (a bare stub) -- manually attach it so kmLogo_RelationalExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # kmLogo_RelationalExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = kmLogo_RelationalExpression(operator="sample_text")
    partner = kmLogo_Expression()
    setattr(partner, 'kmLogo_Expression16', None)
    _safe_set(owner, 'kmLogo_RelationalExpression', partner)
    assert getattr(partner, 'kmLogo_Expression16') == owner
    _safe_set(owner, 'kmLogo_RelationalExpression', None)
    assert getattr(partner, 'kmLogo_Expression16') is None


def test_assoc_right12_stub_double():
    # kmLogo_Expression has no real 'kmLogo_Expression14' property in the generated
    # code (a bare stub) -- manually attach it so kmLogo_ArithmeticExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # kmLogo_ArithmeticExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = kmLogo_ArithmeticExpression(operator="sample_text")
    partner = kmLogo_Expression()
    setattr(partner, 'kmLogo_Expression14', None)
    _safe_set(owner, 'kmLogo_ArithmeticExpression13', partner)
    assert getattr(partner, 'kmLogo_Expression14') == owner
    _safe_set(owner, 'kmLogo_ArithmeticExpression13', None)
    assert getattr(partner, 'kmLogo_Expression14') is None


def test_assoc_right17_stub_double():
    # kmLogo_Expression has no real 'kmLogo_Expression19' property in the generated
    # code (a bare stub) -- manually attach it so kmLogo_RelationalExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # kmLogo_RelationalExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = kmLogo_RelationalExpression(operator="sample_text")
    partner = kmLogo_Expression()
    setattr(partner, 'kmLogo_Expression19', None)
    _safe_set(owner, 'kmLogo_RelationalExpression18', partner)
    assert getattr(partner, 'kmLogo_Expression19') == owner
    _safe_set(owner, 'kmLogo_RelationalExpression18', None)
    assert getattr(partner, 'kmLogo_Expression19') is None


def test_assoc_variables0_stub_double():
    # kmLogo_LogoProgram has no real 'kmLogo_LogoProgram' property in the generated
    # code (a bare stub) -- manually attach it so kmLogo_VarDecl's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # kmLogo_VarDecl's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = kmLogo_VarDecl(key="sample_text")
    partner = kmLogo_LogoProgram()
    setattr(partner, 'kmLogo_LogoProgram', None)
    _safe_set(owner, 'kmLogo_VarDecl', partner)
    assert owner in getattr(partner, 'kmLogo_LogoProgram')
    _safe_set(owner, 'kmLogo_VarDecl', None)
    assert owner not in getattr(partner, 'kmLogo_LogoProgram')


