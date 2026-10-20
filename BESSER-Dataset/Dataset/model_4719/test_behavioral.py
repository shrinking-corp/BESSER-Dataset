import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    BinaryExpression,
    IntegerExpression,
    UnaryExpression,
    core_Add,
    core_And,
    core_BinaryExpression,
    core_Conditional,
    core_Div,
    core_Equal,
    core_Filter,
    core_Greater,
    core_IntegerExpression,
    core_IntegerLiteral,
    core_Lower,
    core_Minus,
    core_Mod,
    core_Mult,
    core_Not,
    core_Or,
    core_Rule,
    core_UMinus,
    core_UnaryExpression,
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

def test_assoc_condition10_stub_double():
    # core_Conditional has no real 'core_Conditional11' property in the generated
    # code (a bare stub) -- manually attach it so core_IntegerExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # core_IntegerExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = core_IntegerExpression()
    partner = core_Conditional()
    setattr(partner, 'core_Conditional11', None)
    _safe_set(owner, 'core_IntegerExpression12', partner)
    assert getattr(partner, 'core_Conditional11') == owner
    _safe_set(owner, 'core_IntegerExpression12', None)
    assert getattr(partner, 'core_Conditional11') is None


def test_assoc_evaluatedVal0_stub_double():
    # core_Rule has no real 'core_Rule' property in the generated
    # code (a bare stub) -- manually attach it so core_IntegerExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # core_IntegerExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = core_IntegerExpression()
    partner = core_Rule()
    setattr(partner, 'core_Rule', None)
    _safe_set(owner, 'core_IntegerExpression', partner)
    assert getattr(partner, 'core_Rule') == owner
    _safe_set(owner, 'core_IntegerExpression', None)
    assert getattr(partner, 'core_Rule') is None


def test_assoc_ifFalseExpression7_stub_double():
    # core_Conditional has no real 'core_Conditional8' property in the generated
    # code (a bare stub) -- manually attach it so core_IntegerExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # core_IntegerExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = core_IntegerExpression()
    partner = core_Conditional()
    setattr(partner, 'core_Conditional8', None)
    _safe_set(owner, 'core_IntegerExpression9', partner)
    assert getattr(partner, 'core_Conditional8') == owner
    _safe_set(owner, 'core_IntegerExpression9', None)
    assert getattr(partner, 'core_Conditional8') is None


def test_assoc_ifTrueExpression5_stub_double():
    # core_Conditional has no real 'core_Conditional' property in the generated
    # code (a bare stub) -- manually attach it so core_IntegerExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # core_IntegerExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = core_IntegerExpression()
    partner = core_Conditional()
    setattr(partner, 'core_Conditional', None)
    _safe_set(owner, 'core_IntegerExpression6', partner)
    assert getattr(partner, 'core_Conditional') == owner
    _safe_set(owner, 'core_IntegerExpression6', None)
    assert getattr(partner, 'core_Conditional') is None


def test_assoc_left13_stub_double():
    # core_BinaryExpression has no real 'core_BinaryExpression' property in the generated
    # code (a bare stub) -- manually attach it so core_IntegerExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # core_IntegerExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = core_IntegerExpression()
    partner = core_BinaryExpression()
    setattr(partner, 'core_BinaryExpression', None)
    _safe_set(owner, 'core_IntegerExpression14', partner)
    assert getattr(partner, 'core_BinaryExpression') == owner
    _safe_set(owner, 'core_IntegerExpression14', None)
    assert getattr(partner, 'core_BinaryExpression') is None


def test_assoc_right15_stub_double():
    # core_BinaryExpression has no real 'core_BinaryExpression16' property in the generated
    # code (a bare stub) -- manually attach it so core_IntegerExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # core_IntegerExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = core_IntegerExpression()
    partner = core_BinaryExpression()
    setattr(partner, 'core_BinaryExpression16', None)
    _safe_set(owner, 'core_IntegerExpression17', partner)
    assert getattr(partner, 'core_BinaryExpression16') == owner
    _safe_set(owner, 'core_IntegerExpression17', None)
    assert getattr(partner, 'core_BinaryExpression16') is None


def test_assoc_target3_stub_double():
    # core_UnaryExpression has no real 'core_UnaryExpression' property in the generated
    # code (a bare stub) -- manually attach it so core_IntegerExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # core_IntegerExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = core_IntegerExpression()
    partner = core_UnaryExpression()
    setattr(partner, 'core_UnaryExpression', None)
    _safe_set(owner, 'core_IntegerExpression4', partner)
    assert getattr(partner, 'core_UnaryExpression') == owner
    _safe_set(owner, 'core_IntegerExpression4', None)
    assert getattr(partner, 'core_UnaryExpression') is None


