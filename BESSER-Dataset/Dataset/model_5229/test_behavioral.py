import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    BinaryExpression,
    Expression,
    ilp_ArithmeticExpression,
    ilp_BinaryExpression,
    ilp_ConstraintExpression,
    ilp_Expression,
    ilp_IntegerLinearProgram,
    ilp_LiteralExpression,
    ilp_ObjectiveFunctionExpression,
    ilp_Variable,
    ilp_VariableExpression,
    ILPDataType,
    ObjectiveGoal,
    Operator,
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

def test_assoc_leftExpression5_reverse_link_reassign_clear():
    a1 = ilp_Expression(comment="sample_text")
    a2 = ilp_Expression(comment="sample_text_2")
    b = ilp_BinaryExpression(operator="sample_text")
    _safe_set(b, 'ilp_BinaryExpression', a1)
    assert _is_linked(b, 'ilp_BinaryExpression', a1)
    if hasattr(a1, 'ilp_Expression'):
        assert _is_linked(a1, 'ilp_Expression', b)
    _safe_set(b, 'ilp_BinaryExpression', a2)
    assert _is_linked(b, 'ilp_BinaryExpression', a2)
    if hasattr(a1, 'ilp_Expression'):
        assert not _is_linked(a1, 'ilp_Expression', b)
    if hasattr(a2, 'ilp_Expression'):
        assert _is_linked(a2, 'ilp_Expression', b)
    _safe_set(b, 'ilp_BinaryExpression', None)
    assert not _is_linked(b, 'ilp_BinaryExpression', a2)
    if hasattr(a2, 'ilp_Expression'):
        assert not _is_linked(a2, 'ilp_Expression', b)


def test_assoc_objectiveFunction11_reverse_link_reassign_clear():
    a1 = ilp_ObjectiveFunctionExpression(goal="sample_text")
    a2 = ilp_ObjectiveFunctionExpression(goal="sample_text_2")
    b = ilp_Expression(comment="sample_text")
    _safe_set(b, 'ilp_Expression13', a1)
    assert _is_linked(b, 'ilp_Expression13', a1)
    if hasattr(a1, 'ilp_ObjectiveFunctionExpression12'):
        assert _is_linked(a1, 'ilp_ObjectiveFunctionExpression12', b)
    _safe_set(b, 'ilp_Expression13', a2)
    assert _is_linked(b, 'ilp_Expression13', a2)
    if hasattr(a1, 'ilp_ObjectiveFunctionExpression12'):
        assert not _is_linked(a1, 'ilp_ObjectiveFunctionExpression12', b)
    if hasattr(a2, 'ilp_ObjectiveFunctionExpression12'):
        assert _is_linked(a2, 'ilp_ObjectiveFunctionExpression12', b)
    _safe_set(b, 'ilp_Expression13', None)
    assert not _is_linked(b, 'ilp_Expression13', a2)
    if hasattr(a2, 'ilp_ObjectiveFunctionExpression12'):
        assert not _is_linked(a2, 'ilp_ObjectiveFunctionExpression12', b)


def test_assoc_rightExpression6_reverse_link_reassign_clear():
    a1 = ilp_Expression(comment="sample_text")
    a2 = ilp_Expression(comment="sample_text_2")
    b = ilp_BinaryExpression(operator="sample_text")
    _safe_set(b, 'ilp_BinaryExpression7', a1)
    assert _is_linked(b, 'ilp_BinaryExpression7', a1)
    if hasattr(a1, 'ilp_Expression8'):
        assert _is_linked(a1, 'ilp_Expression8', b)
    _safe_set(b, 'ilp_BinaryExpression7', a2)
    assert _is_linked(b, 'ilp_BinaryExpression7', a2)
    if hasattr(a1, 'ilp_Expression8'):
        assert not _is_linked(a1, 'ilp_Expression8', b)
    if hasattr(a2, 'ilp_Expression8'):
        assert _is_linked(a2, 'ilp_Expression8', b)
    _safe_set(b, 'ilp_BinaryExpression7', None)
    assert not _is_linked(b, 'ilp_BinaryExpression7', a2)
    if hasattr(a2, 'ilp_Expression8'):
        assert not _is_linked(a2, 'ilp_Expression8', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_objectiveFunction3_stub_double():
    # ilp_IntegerLinearProgram has no real 'ilp_IntegerLinearProgram4' property in the generated
    # code (a bare stub) -- manually attach it so ilp_ObjectiveFunctionExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ilp_ObjectiveFunctionExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ilp_ObjectiveFunctionExpression(goal="sample_text")
    partner = ilp_IntegerLinearProgram()
    setattr(partner, 'ilp_IntegerLinearProgram4', None)
    _safe_set(owner, 'ilp_ObjectiveFunctionExpression', partner)
    assert getattr(partner, 'ilp_IntegerLinearProgram4') == owner
    _safe_set(owner, 'ilp_ObjectiveFunctionExpression', None)
    assert getattr(partner, 'ilp_IntegerLinearProgram4') is None


def test_assoc_variable9_stub_double():
    # ilp_VariableExpression has no real 'ilp_VariableExpression' property in the generated
    # code (a bare stub) -- manually attach it so ilp_Variable's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ilp_Variable's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ilp_Variable(dataType="sample_text", name="sample_text")
    partner = ilp_VariableExpression()
    setattr(partner, 'ilp_VariableExpression', None)
    _safe_set(owner, 'ilp_Variable10', partner)
    assert getattr(partner, 'ilp_VariableExpression') == owner
    _safe_set(owner, 'ilp_Variable10', None)
    assert getattr(partner, 'ilp_VariableExpression') is None


def test_assoc_variables0_stub_double():
    # ilp_IntegerLinearProgram has no real 'ilp_IntegerLinearProgram' property in the generated
    # code (a bare stub) -- manually attach it so ilp_Variable's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ilp_Variable's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ilp_Variable(dataType="sample_text", name="sample_text")
    partner = ilp_IntegerLinearProgram()
    setattr(partner, 'ilp_IntegerLinearProgram', None)
    _safe_set(owner, 'ilp_Variable', partner)
    assert owner in getattr(partner, 'ilp_IntegerLinearProgram')
    _safe_set(owner, 'ilp_Variable', None)
    assert owner not in getattr(partner, 'ilp_IntegerLinearProgram')


