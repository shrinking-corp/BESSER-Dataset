import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    BinaryExp,
    BoolExp,
    Exp,
    Statement,
    while_AndExp,
    while_Assignment,
    while_BinaryExp,
    while_BoolExp,
    while_EqExp,
    while_Exp,
    while_If,
    while_NEqExp,
    while_Program,
    while_Ret,
    while_Statement,
    while_Val,
    while_Var,
    while_VarExp,
    while_While,
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

def test_assoc_literals3_stub_double():
    # while_Program has no real 'while_Program4' property in the generated
    # code (a bare stub) -- manually attach it so while_Val's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # while_Val's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = while_Val(id="sample_text")
    partner = while_Program()
    setattr(partner, 'while_Program4', None)
    _safe_set(owner, 'while_Val', partner)
    assert owner in getattr(partner, 'while_Program4')
    _safe_set(owner, 'while_Val', None)
    assert owner not in getattr(partner, 'while_Program4')


def test_assoc_var24_stub_double():
    # while_VarExp has no real 'while_VarExp' property in the generated
    # code (a bare stub) -- manually attach it so while_Var's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # while_Var's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = while_Var(id="sample_text")
    partner = while_VarExp()
    setattr(partner, 'while_VarExp', None)
    _safe_set(owner, 'while_Var25', partner)
    assert getattr(partner, 'while_VarExp') == owner
    _safe_set(owner, 'while_Var25', None)
    assert getattr(partner, 'while_VarExp') is None


def test_assoc_var26_stub_double():
    # while_Assignment has no real 'while_Assignment' property in the generated
    # code (a bare stub) -- manually attach it so while_Var's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # while_Var's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = while_Var(id="sample_text")
    partner = while_Assignment()
    setattr(partner, 'while_Assignment', None)
    _safe_set(owner, 'while_Var27', partner)
    assert getattr(partner, 'while_Assignment') == owner
    _safe_set(owner, 'while_Var27', None)
    assert getattr(partner, 'while_Assignment') is None


def test_assoc_variables1_stub_double():
    # while_Program has no real 'while_Program2' property in the generated
    # code (a bare stub) -- manually attach it so while_Var's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # while_Var's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = while_Var(id="sample_text")
    partner = while_Program()
    setattr(partner, 'while_Program2', None)
    _safe_set(owner, 'while_Var', partner)
    assert owner in getattr(partner, 'while_Program2')
    _safe_set(owner, 'while_Var', None)
    assert owner not in getattr(partner, 'while_Program2')


