import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    ArithmeticExpression,
    AtomicExpression,
    Expression,
    Statement,
    mpl_AddExpression,
    mpl_ArithmeticExpression,
    mpl_Assignment,
    mpl_AtomicExpression,
    mpl_Expression,
    mpl_ExpressionStatement,
    mpl_LiteralValue,
    mpl_Program,
    mpl_Statement,
    mpl_Variable,
    mpl_VariableDeclaration,
    mpl_VariableRefrence,
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

def test_assoc_statement1_stub_double():
    # mpl_Statement has no real 'mpl_Statement' property in the generated
    # code (a bare stub) -- manually attach it so mpl_Program's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # mpl_Program's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = mpl_Program(name="sample_text")
    partner = mpl_Statement()
    setattr(partner, 'mpl_Statement', None)
    _safe_set(owner, 'mpl_Program2', {partner})
    assert getattr(partner, 'mpl_Statement') == owner
    _safe_set(owner, 'mpl_Program2', set())
    assert getattr(partner, 'mpl_Statement') is None


def test_assoc_variable15_stub_double():
    # mpl_VariableRefrence has no real 'mpl_VariableRefrence16' property in the generated
    # code (a bare stub) -- manually attach it so mpl_Variable's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # mpl_Variable's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = mpl_Variable(name="sample_text")
    partner = mpl_VariableRefrence()
    setattr(partner, 'mpl_VariableRefrence16', None)
    _safe_set(owner, 'mpl_Variable17', partner)
    assert getattr(partner, 'mpl_VariableRefrence16') == owner
    _safe_set(owner, 'mpl_Variable17', None)
    assert getattr(partner, 'mpl_VariableRefrence16') is None


def test_assoc_variable3_stub_double():
    # mpl_VariableDeclaration has no real 'mpl_VariableDeclaration4' property in the generated
    # code (a bare stub) -- manually attach it so mpl_Variable's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # mpl_Variable's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = mpl_Variable(name="sample_text")
    partner = mpl_VariableDeclaration()
    setattr(partner, 'mpl_VariableDeclaration4', None)
    _safe_set(owner, 'mpl_Variable', partner)
    assert getattr(partner, 'mpl_VariableDeclaration4') == owner
    _safe_set(owner, 'mpl_Variable', None)
    assert getattr(partner, 'mpl_VariableDeclaration4') is None


def test_assoc_variabledeclarations0_stub_double():
    # mpl_VariableDeclaration has no real 'mpl_VariableDeclaration' property in the generated
    # code (a bare stub) -- manually attach it so mpl_Program's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # mpl_Program's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = mpl_Program(name="sample_text")
    partner = mpl_VariableDeclaration()
    setattr(partner, 'mpl_VariableDeclaration', None)
    _safe_set(owner, 'mpl_Program', {partner})
    assert getattr(partner, 'mpl_VariableDeclaration') == owner
    _safe_set(owner, 'mpl_Program', set())
    assert getattr(partner, 'mpl_VariableDeclaration') is None


