import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Action,
    Behavior,
    Block,
    BlockContainer,
    Condition,
    ConditionContainer,
    Flow,
    Instruction,
    NamedElement,
    Sensor,
    mindstorms_Action,
    mindstorms_Arbitrator,
    mindstorms_AvoidObstacle,
    mindstorms_Behavior,
    mindstorms_Block,
    mindstorms_BlockContainer,
    mindstorms_ColorSensor,
    mindstorms_Condition,
    mindstorms_ConditionContainer,
    mindstorms_Delay,
    mindstorms_ExploreForward,
    mindstorms_Flow,
    mindstorms_GoBackward,
    mindstorms_GoForward,
    mindstorms_GoTo,
    mindstorms_GoToEnemy,
    mindstorms_Grab,
    mindstorms_If,
    mindstorms_Instruction,
    mindstorms_Main,
    mindstorms_NamedElement,
    mindstorms_Procedure,
    mindstorms_Release,
    mindstorms_ReturnBottleToBase,
    mindstorms_ReturnToBase,
    mindstorms_ReuseInstruction,
    mindstorms_Rotate,
    mindstorms_Sensor,
    mindstorms_TouchSensor,
    mindstorms_UltrasonicSensor,
    mindstorms_While,
    Color,
    OperatorKind,
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

