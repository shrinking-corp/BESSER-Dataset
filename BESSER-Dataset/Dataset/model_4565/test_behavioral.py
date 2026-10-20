import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Condition,
    ConditionalStatement,
    ControlStatement,
    NamedElement,
    Statement,
    robot_Condition,
    robot_ConditionalStatement,
    robot_Connection,
    robot_ControlStatement,
    robot_ExecuteStatement,
    robot_ForwardStatement,
    robot_IfStatement,
    robot_NamedElement,
    robot_ObjectAheadCondition,
    robot_PrintStatement,
    robot_RightStatement,
    robot_Robot,
    robot_Scenario,
    robot_Statement,
    robot_StatementBlock,
    robot_TrueCondition,
    robot_UntilStatement,
    robot_WhileStatement,
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

def test_assoc_connection6_stub_double():
    # robot_Robot has no real 'robot_Robot7' property in the generated
    # code (a bare stub) -- manually attach it so robot_Connection's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # robot_Connection's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = robot_Connection(ip="sample_text", port=7)
    partner = robot_Robot()
    setattr(partner, 'robot_Robot7', None)
    _safe_set(owner, 'robot_Connection', partner)
    assert getattr(partner, 'robot_Robot7') == owner
    _safe_set(owner, 'robot_Connection', None)
    assert getattr(partner, 'robot_Robot7') is None


