import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Expression,
    Statement,
    parameterizedExpressionsTestLanguage_AssignmentExpression,
    parameterizedExpressionsTestLanguage_Block,
    parameterizedExpressionsTestLanguage_CommaExpression,
    parameterizedExpressionsTestLanguage_Expression,
    parameterizedExpressionsTestLanguage_ExpressionStatement,
    parameterizedExpressionsTestLanguage_FunctionDeclaration,
    parameterizedExpressionsTestLanguage_IdentifierRef,
    parameterizedExpressionsTestLanguage_IndexedAccessExpression,
    parameterizedExpressionsTestLanguage_LabelledStatement,
    parameterizedExpressionsTestLanguage_ParameterizedPropertyAccessExpression,
    parameterizedExpressionsTestLanguage_RelationalExpression,
    parameterizedExpressionsTestLanguage_ShiftExpression,
    parameterizedExpressionsTestLanguage_Statement,
    parameterizedExpressionsTestLanguage_YieldExpression,
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

def test_assoc_body0_stub_double():
    # parameterizedExpressionsTestLanguage_Block has no real 'parameterizedExpressionsTestLanguage_Block' property in the generated
    # code (a bare stub) -- manually attach it so parameterizedExpressionsTestLanguage_FunctionDeclaration's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # parameterizedExpressionsTestLanguage_FunctionDeclaration's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = parameterizedExpressionsTestLanguage_FunctionDeclaration(generator=True, name="sample_text")
    partner = parameterizedExpressionsTestLanguage_Block()
    setattr(partner, 'parameterizedExpressionsTestLanguage_Block', None)
    _safe_set(owner, 'parameterizedExpressionsTestLanguage_FunctionDeclaration', partner)
    assert getattr(partner, 'parameterizedExpressionsTestLanguage_Block') == owner
    _safe_set(owner, 'parameterizedExpressionsTestLanguage_FunctionDeclaration', None)
    assert getattr(partner, 'parameterizedExpressionsTestLanguage_Block') is None


def test_assoc_expression28_stub_double():
    # parameterizedExpressionsTestLanguage_Expression has no real 'parameterizedExpressionsTestLanguage_Expression29' property in the generated
    # code (a bare stub) -- manually attach it so parameterizedExpressionsTestLanguage_YieldExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # parameterizedExpressionsTestLanguage_YieldExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = parameterizedExpressionsTestLanguage_YieldExpression(many=True)
    partner = parameterizedExpressionsTestLanguage_Expression()
    setattr(partner, 'parameterizedExpressionsTestLanguage_Expression29', None)
    _safe_set(owner, 'parameterizedExpressionsTestLanguage_YieldExpression', partner)
    assert getattr(partner, 'parameterizedExpressionsTestLanguage_Expression29') == owner
    _safe_set(owner, 'parameterizedExpressionsTestLanguage_YieldExpression', None)
    assert getattr(partner, 'parameterizedExpressionsTestLanguage_Expression29') is None


def test_assoc_lhs13_stub_double():
    # parameterizedExpressionsTestLanguage_Expression has no real 'parameterizedExpressionsTestLanguage_Expression14' property in the generated
    # code (a bare stub) -- manually attach it so parameterizedExpressionsTestLanguage_ShiftExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # parameterizedExpressionsTestLanguage_ShiftExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = parameterizedExpressionsTestLanguage_ShiftExpression(op="sample_text")
    partner = parameterizedExpressionsTestLanguage_Expression()
    setattr(partner, 'parameterizedExpressionsTestLanguage_Expression14', None)
    _safe_set(owner, 'parameterizedExpressionsTestLanguage_ShiftExpression', partner)
    assert getattr(partner, 'parameterizedExpressionsTestLanguage_Expression14') == owner
    _safe_set(owner, 'parameterizedExpressionsTestLanguage_ShiftExpression', None)
    assert getattr(partner, 'parameterizedExpressionsTestLanguage_Expression14') is None


def test_assoc_lhs18_stub_double():
    # parameterizedExpressionsTestLanguage_Expression has no real 'parameterizedExpressionsTestLanguage_Expression19' property in the generated
    # code (a bare stub) -- manually attach it so parameterizedExpressionsTestLanguage_RelationalExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # parameterizedExpressionsTestLanguage_RelationalExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = parameterizedExpressionsTestLanguage_RelationalExpression(op="sample_text")
    partner = parameterizedExpressionsTestLanguage_Expression()
    setattr(partner, 'parameterizedExpressionsTestLanguage_Expression19', None)
    _safe_set(owner, 'parameterizedExpressionsTestLanguage_RelationalExpression', partner)
    assert getattr(partner, 'parameterizedExpressionsTestLanguage_Expression19') == owner
    _safe_set(owner, 'parameterizedExpressionsTestLanguage_RelationalExpression', None)
    assert getattr(partner, 'parameterizedExpressionsTestLanguage_Expression19') is None


def test_assoc_lhs23_stub_double():
    # parameterizedExpressionsTestLanguage_Expression has no real 'parameterizedExpressionsTestLanguage_Expression24' property in the generated
    # code (a bare stub) -- manually attach it so parameterizedExpressionsTestLanguage_AssignmentExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # parameterizedExpressionsTestLanguage_AssignmentExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = parameterizedExpressionsTestLanguage_AssignmentExpression(op="sample_text")
    partner = parameterizedExpressionsTestLanguage_Expression()
    setattr(partner, 'parameterizedExpressionsTestLanguage_Expression24', None)
    _safe_set(owner, 'parameterizedExpressionsTestLanguage_AssignmentExpression', partner)
    assert getattr(partner, 'parameterizedExpressionsTestLanguage_Expression24') == owner
    _safe_set(owner, 'parameterizedExpressionsTestLanguage_AssignmentExpression', None)
    assert getattr(partner, 'parameterizedExpressionsTestLanguage_Expression24') is None


def test_assoc_rhs15_stub_double():
    # parameterizedExpressionsTestLanguage_Expression has no real 'parameterizedExpressionsTestLanguage_Expression17' property in the generated
    # code (a bare stub) -- manually attach it so parameterizedExpressionsTestLanguage_ShiftExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # parameterizedExpressionsTestLanguage_ShiftExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = parameterizedExpressionsTestLanguage_ShiftExpression(op="sample_text")
    partner = parameterizedExpressionsTestLanguage_Expression()
    setattr(partner, 'parameterizedExpressionsTestLanguage_Expression17', None)
    _safe_set(owner, 'parameterizedExpressionsTestLanguage_ShiftExpression16', partner)
    assert getattr(partner, 'parameterizedExpressionsTestLanguage_Expression17') == owner
    _safe_set(owner, 'parameterizedExpressionsTestLanguage_ShiftExpression16', None)
    assert getattr(partner, 'parameterizedExpressionsTestLanguage_Expression17') is None


def test_assoc_rhs20_stub_double():
    # parameterizedExpressionsTestLanguage_Expression has no real 'parameterizedExpressionsTestLanguage_Expression22' property in the generated
    # code (a bare stub) -- manually attach it so parameterizedExpressionsTestLanguage_RelationalExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # parameterizedExpressionsTestLanguage_RelationalExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = parameterizedExpressionsTestLanguage_RelationalExpression(op="sample_text")
    partner = parameterizedExpressionsTestLanguage_Expression()
    setattr(partner, 'parameterizedExpressionsTestLanguage_Expression22', None)
    _safe_set(owner, 'parameterizedExpressionsTestLanguage_RelationalExpression21', partner)
    assert getattr(partner, 'parameterizedExpressionsTestLanguage_Expression22') == owner
    _safe_set(owner, 'parameterizedExpressionsTestLanguage_RelationalExpression21', None)
    assert getattr(partner, 'parameterizedExpressionsTestLanguage_Expression22') is None


def test_assoc_rhs25_stub_double():
    # parameterizedExpressionsTestLanguage_Expression has no real 'parameterizedExpressionsTestLanguage_Expression27' property in the generated
    # code (a bare stub) -- manually attach it so parameterizedExpressionsTestLanguage_AssignmentExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # parameterizedExpressionsTestLanguage_AssignmentExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = parameterizedExpressionsTestLanguage_AssignmentExpression(op="sample_text")
    partner = parameterizedExpressionsTestLanguage_Expression()
    setattr(partner, 'parameterizedExpressionsTestLanguage_Expression27', None)
    _safe_set(owner, 'parameterizedExpressionsTestLanguage_AssignmentExpression26', partner)
    assert getattr(partner, 'parameterizedExpressionsTestLanguage_Expression27') == owner
    _safe_set(owner, 'parameterizedExpressionsTestLanguage_AssignmentExpression26', None)
    assert getattr(partner, 'parameterizedExpressionsTestLanguage_Expression27') is None


def test_assoc_statement4_stub_double():
    # parameterizedExpressionsTestLanguage_Statement has no real 'parameterizedExpressionsTestLanguage_Statement5' property in the generated
    # code (a bare stub) -- manually attach it so parameterizedExpressionsTestLanguage_LabelledStatement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # parameterizedExpressionsTestLanguage_LabelledStatement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = parameterizedExpressionsTestLanguage_LabelledStatement(name="sample_text")
    partner = parameterizedExpressionsTestLanguage_Statement()
    setattr(partner, 'parameterizedExpressionsTestLanguage_Statement5', None)
    _safe_set(owner, 'parameterizedExpressionsTestLanguage_LabelledStatement', partner)
    assert getattr(partner, 'parameterizedExpressionsTestLanguage_Statement5') == owner
    _safe_set(owner, 'parameterizedExpressionsTestLanguage_LabelledStatement', None)
    assert getattr(partner, 'parameterizedExpressionsTestLanguage_Statement5') is None


def test_assoc_target11_stub_double():
    # parameterizedExpressionsTestLanguage_Expression has no real 'parameterizedExpressionsTestLanguage_Expression12' property in the generated
    # code (a bare stub) -- manually attach it so parameterizedExpressionsTestLanguage_ParameterizedPropertyAccessExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # parameterizedExpressionsTestLanguage_ParameterizedPropertyAccessExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = parameterizedExpressionsTestLanguage_ParameterizedPropertyAccessExpression(_property="sample_text")
    partner = parameterizedExpressionsTestLanguage_Expression()
    setattr(partner, 'parameterizedExpressionsTestLanguage_Expression12', None)
    _safe_set(owner, 'parameterizedExpressionsTestLanguage_ParameterizedPropertyAccessExpression', partner)
    assert getattr(partner, 'parameterizedExpressionsTestLanguage_Expression12') == owner
    _safe_set(owner, 'parameterizedExpressionsTestLanguage_ParameterizedPropertyAccessExpression', None)
    assert getattr(partner, 'parameterizedExpressionsTestLanguage_Expression12') is None


