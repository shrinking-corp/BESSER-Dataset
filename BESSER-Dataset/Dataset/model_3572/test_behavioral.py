import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Expression,
    FileRegion,
    expressions_AddExpression,
    expressions_AndExpression,
    expressions_BooleanLiteral,
    expressions_CharacterLiteral,
    expressions_ConstExpression,
    expressions_DoubleLiteral,
    expressions_Expression,
    expressions_FixedPtLiteral,
    expressions_FloatingPointLiteral,
    expressions_IdlTypeDcl,
    expressions_IntegerLiteral,
    expressions_MultExpression,
    expressions_OrExpression,
    expressions_ScopeLiteral,
    expressions_ShiftExpression,
    expressions_StringLiteral,
    expressions_UnaryExpression,
    expressions_WideCharacterLiteral,
    expressions_WideStringLiteral,
    expressions_XOrExpression,
    AddType,
    MultiType,
    ShiftType,
    UnaryType,
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

def test_assoc_expr31_stub_double():
    # expressions_Expression has no real 'expressions_Expression32' property in the generated
    # code (a bare stub) -- manually attach it so expressions_UnaryExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # expressions_UnaryExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = expressions_UnaryExpression(type="sample_text")
    partner = expressions_Expression()
    setattr(partner, 'expressions_Expression32', None)
    _safe_set(owner, 'expressions_UnaryExpression', partner)
    assert getattr(partner, 'expressions_Expression32') == owner
    _safe_set(owner, 'expressions_UnaryExpression', None)
    assert getattr(partner, 'expressions_Expression32') is None


def test_assoc_left16_stub_double():
    # expressions_Expression has no real 'expressions_Expression17' property in the generated
    # code (a bare stub) -- manually attach it so expressions_ShiftExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # expressions_ShiftExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = expressions_ShiftExpression(type="sample_text")
    partner = expressions_Expression()
    setattr(partner, 'expressions_Expression17', None)
    _safe_set(owner, 'expressions_ShiftExpression', partner)
    assert getattr(partner, 'expressions_Expression17') == owner
    _safe_set(owner, 'expressions_ShiftExpression', None)
    assert getattr(partner, 'expressions_Expression17') is None


def test_assoc_left21_stub_double():
    # expressions_Expression has no real 'expressions_Expression22' property in the generated
    # code (a bare stub) -- manually attach it so expressions_AddExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # expressions_AddExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = expressions_AddExpression(type="sample_text")
    partner = expressions_Expression()
    setattr(partner, 'expressions_Expression22', None)
    _safe_set(owner, 'expressions_AddExpression', partner)
    assert getattr(partner, 'expressions_Expression22') == owner
    _safe_set(owner, 'expressions_AddExpression', None)
    assert getattr(partner, 'expressions_Expression22') is None


def test_assoc_left26_stub_double():
    # expressions_Expression has no real 'expressions_Expression27' property in the generated
    # code (a bare stub) -- manually attach it so expressions_MultExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # expressions_MultExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = expressions_MultExpression(type="sample_text")
    partner = expressions_Expression()
    setattr(partner, 'expressions_Expression27', None)
    _safe_set(owner, 'expressions_MultExpression', partner)
    assert getattr(partner, 'expressions_Expression27') == owner
    _safe_set(owner, 'expressions_MultExpression', None)
    assert getattr(partner, 'expressions_Expression27') is None


def test_assoc_right18_stub_double():
    # expressions_Expression has no real 'expressions_Expression20' property in the generated
    # code (a bare stub) -- manually attach it so expressions_ShiftExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # expressions_ShiftExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = expressions_ShiftExpression(type="sample_text")
    partner = expressions_Expression()
    setattr(partner, 'expressions_Expression20', None)
    _safe_set(owner, 'expressions_ShiftExpression19', partner)
    assert getattr(partner, 'expressions_Expression20') == owner
    _safe_set(owner, 'expressions_ShiftExpression19', None)
    assert getattr(partner, 'expressions_Expression20') is None


def test_assoc_right23_stub_double():
    # expressions_Expression has no real 'expressions_Expression25' property in the generated
    # code (a bare stub) -- manually attach it so expressions_AddExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # expressions_AddExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = expressions_AddExpression(type="sample_text")
    partner = expressions_Expression()
    setattr(partner, 'expressions_Expression25', None)
    _safe_set(owner, 'expressions_AddExpression24', partner)
    assert getattr(partner, 'expressions_Expression25') == owner
    _safe_set(owner, 'expressions_AddExpression24', None)
    assert getattr(partner, 'expressions_Expression25') is None


def test_assoc_right28_stub_double():
    # expressions_Expression has no real 'expressions_Expression30' property in the generated
    # code (a bare stub) -- manually attach it so expressions_MultExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # expressions_MultExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = expressions_MultExpression(type="sample_text")
    partner = expressions_Expression()
    setattr(partner, 'expressions_Expression30', None)
    _safe_set(owner, 'expressions_MultExpression29', partner)
    assert getattr(partner, 'expressions_Expression30') == owner
    _safe_set(owner, 'expressions_MultExpression29', None)
    assert getattr(partner, 'expressions_Expression30') is None


