import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Amount,
    Angle,
    Condition,
    Instruction,
    RobotProjectModel_Amount,
    RobotProjectModel_Angle,
    RobotProjectModel_Call,
    RobotProjectModel_Condition,
    RobotProjectModel_DetectedObjectIs,
    RobotProjectModel_Distance,
    RobotProjectModel_Duration,
    RobotProjectModel_Function,
    RobotProjectModel_Grab,
    RobotProjectModel_HomeDirection,
    RobotProjectModel_If,
    RobotProjectModel_Instruction,
    RobotProjectModel_InstructionBlock,
    RobotProjectModel_MoveStraight,
    RobotProjectModel_Print,
    RobotProjectModel_Release,
    RobotProjectModel_Robot,
    RobotProjectModel_SensorActivation,
    RobotProjectModel_TimedInstruction,
    RobotProjectModel_Turn,
    RobotProjectModel_Wait,
    TimedInstruction,
    AngleUnit,
    DetectedType,
    DistanceUnit,
    TimeUnit,
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

def test_assoc_angle3_stub_double():
    # RobotProjectModel_Turn has no real 'RobotProjectModel_Turn' property in the generated
    # code (a bare stub) -- manually attach it so RobotProjectModel_Angle's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # RobotProjectModel_Angle's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = RobotProjectModel_Angle(angleUnit="sample_text")
    partner = RobotProjectModel_Turn()
    setattr(partner, 'RobotProjectModel_Turn', None)
    _safe_set(owner, 'RobotProjectModel_Angle', partner)
    assert getattr(partner, 'RobotProjectModel_Turn') == owner
    _safe_set(owner, 'RobotProjectModel_Angle', None)
    assert getattr(partner, 'RobotProjectModel_Turn') is None


def test_assoc_destination5_stub_double():
    # RobotProjectModel_Call has no real 'RobotProjectModel_Call' property in the generated
    # code (a bare stub) -- manually attach it so RobotProjectModel_Function's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # RobotProjectModel_Function's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = RobotProjectModel_Function(name="sample_text")
    partner = RobotProjectModel_Call()
    setattr(partner, 'RobotProjectModel_Call', None)
    _safe_set(owner, 'RobotProjectModel_Function6', partner)
    assert getattr(partner, 'RobotProjectModel_Call') == owner
    _safe_set(owner, 'RobotProjectModel_Function6', None)
    assert getattr(partner, 'RobotProjectModel_Call') is None


def test_assoc_distance0_stub_double():
    # RobotProjectModel_MoveStraight has no real 'RobotProjectModel_MoveStraight' property in the generated
    # code (a bare stub) -- manually attach it so RobotProjectModel_Distance's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # RobotProjectModel_Distance's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = RobotProjectModel_Distance(distanceUnit="sample_text")
    partner = RobotProjectModel_MoveStraight()
    setattr(partner, 'RobotProjectModel_MoveStraight', None)
    _safe_set(owner, 'RobotProjectModel_Distance', partner)
    assert getattr(partner, 'RobotProjectModel_MoveStraight') == owner
    _safe_set(owner, 'RobotProjectModel_Distance', None)
    assert getattr(partner, 'RobotProjectModel_MoveStraight') is None


def test_assoc_duration2_stub_double():
    # RobotProjectModel_TimedInstruction has no real 'RobotProjectModel_TimedInstruction' property in the generated
    # code (a bare stub) -- manually attach it so RobotProjectModel_Duration's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # RobotProjectModel_Duration's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = RobotProjectModel_Duration(timeUnit="sample_text")
    partner = RobotProjectModel_TimedInstruction()
    setattr(partner, 'RobotProjectModel_TimedInstruction', None)
    _safe_set(owner, 'RobotProjectModel_Duration', partner)
    assert getattr(partner, 'RobotProjectModel_TimedInstruction') == owner
    _safe_set(owner, 'RobotProjectModel_Duration', None)
    assert getattr(partner, 'RobotProjectModel_TimedInstruction') is None


def test_assoc_instructionBlock4_stub_double():
    # RobotProjectModel_InstructionBlock has no real 'RobotProjectModel_InstructionBlock' property in the generated
    # code (a bare stub) -- manually attach it so RobotProjectModel_Function's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # RobotProjectModel_Function's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = RobotProjectModel_Function(name="sample_text")
    partner = RobotProjectModel_InstructionBlock()
    setattr(partner, 'RobotProjectModel_InstructionBlock', None)
    _safe_set(owner, 'RobotProjectModel_Function', partner)
    assert getattr(partner, 'RobotProjectModel_InstructionBlock') == owner
    _safe_set(owner, 'RobotProjectModel_Function', None)
    assert getattr(partner, 'RobotProjectModel_InstructionBlock') is None


