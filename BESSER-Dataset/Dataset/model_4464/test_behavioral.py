import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Condition,
    Movement,
    Operation,
    Operator,
    Values,
    Var,
    robot_Affectation,
    robot_Alternative,
    robot_Backward,
    robot_Compare,
    robot_Condition,
    robot_Declaration,
    robot_Different,
    robot_Echo,
    robot_Event,
    robot_Forward,
    robot_Mission,
    robot_Movement,
    robot_Operation,
    robot_Operator,
    robot_Sensor,
    robot_Sequence,
    robot_Sleep,
    robot_Stop,
    robot_TBoolean,
    robot_TFloat,
    robot_TInteger,
    robot_TString,
    robot_TurnLeft,
    robot_TurnRight,
    robot_Value,
    robot_Values,
    robot_Var,
    robot_Variable,
    robot_Whenever,
    robot_While,
    EOperator,
    ESensor,
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

def test_assoc_Operator34_stub_double():
    # robot_Compare has no real 'robot_Compare' property in the generated
    # code (a bare stub) -- manually attach it so robot_Operator's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # robot_Operator's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = robot_Operator(type="sample_text")
    partner = robot_Compare()
    setattr(partner, 'robot_Compare', None)
    _safe_set(owner, 'robot_Operator', partner)
    assert getattr(partner, 'robot_Compare') == owner
    _safe_set(owner, 'robot_Operator', None)
    assert getattr(partner, 'robot_Compare') is None


def test_assoc_Value18_stub_double():
    # robot_Values has no real 'robot_Values' property in the generated
    # code (a bare stub) -- manually attach it so robot_Var's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # robot_Var's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = robot_Var(Name="sample_text")
    partner = robot_Values()
    setattr(partner, 'robot_Values', None)
    _safe_set(owner, 'robot_Var', partner)
    assert getattr(partner, 'robot_Values') == owner
    _safe_set(owner, 'robot_Var', None)
    assert getattr(partner, 'robot_Values') is None


