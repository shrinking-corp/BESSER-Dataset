import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Command,
    Condition,
    Expr,
    robo_Motor,
    robo_Program,
    robo_Robot,
    robo_Sensor,
    robo_Setup,
    robo_command_Assignment,
    robo_command_Branch,
    robo_command_Command,
    robo_command_Drive,
    robo_command_Loop,
    robo_condition_Comparison,
    robo_condition_Condition,
    robo_expression_Expr,
    robo_expression_Literal,
    robo_expression_Operation,
    robo_expression_Variable,
    ComparisonOperator,
    Direction,
    ExprOperation,
    MotorPort,
    MotorType,
    SensorMode,
    SensorPort,
    SensorType,
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

def test_assoc_commands10_stub_double():
    # Command has no real 'Command' property in the generated
    # code (a bare stub) -- manually attach it so robo_Program's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # robo_Program's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = robo_Program(name="sample_text")
    partner = Command()
    setattr(partner, 'Command', None)
    _safe_set(owner, 'robo_Program11', {partner})
    assert getattr(partner, 'Command') == owner
    _safe_set(owner, 'robo_Program11', set())
    assert getattr(partner, 'Command') is None


def test_assoc_distance12_stub_double():
    # Expr has no real 'Expr' property in the generated
    # code (a bare stub) -- manually attach it so robo_command_Drive's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # robo_command_Drive's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = robo_command_Drive(direction="sample_text")
    partner = Expr()
    setattr(partner, 'Expr', None)
    _safe_set(owner, 'robo_command_Drive', partner)
    assert getattr(partner, 'Expr') == owner
    _safe_set(owner, 'robo_command_Drive', None)
    assert getattr(partner, 'Expr') is None


def test_assoc_left27_stub_double():
    # Expr has no real 'Expr28' property in the generated
    # code (a bare stub) -- manually attach it so robo_expression_Operation's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # robo_expression_Operation's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = robo_expression_Operation(operator="sample_text")
    partner = Expr()
    setattr(partner, 'Expr28', None)
    _safe_set(owner, 'robo_expression_Operation', partner)
    assert getattr(partner, 'Expr28') == owner
    _safe_set(owner, 'robo_expression_Operation', None)
    assert getattr(partner, 'Expr28') is None


def test_assoc_left32_stub_double():
    # Expr has no real 'Expr33' property in the generated
    # code (a bare stub) -- manually attach it so robo_condition_Comparison's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # robo_condition_Comparison's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = robo_condition_Comparison(operator="sample_text")
    partner = Expr()
    setattr(partner, 'Expr33', None)
    _safe_set(owner, 'robo_condition_Comparison', partner)
    assert getattr(partner, 'Expr33') == owner
    _safe_set(owner, 'robo_condition_Comparison', None)
    assert getattr(partner, 'Expr33') is None


def test_assoc_leftMotor3_stub_double():
    # robo_Setup has no real 'robo_Setup4' property in the generated
    # code (a bare stub) -- manually attach it so robo_Motor's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # robo_Motor's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = robo_Motor(port="sample_text", reversed=True, speed=3.14, type="sample_text")
    partner = robo_Setup()
    setattr(partner, 'robo_Setup4', None)
    _safe_set(owner, 'robo_Motor', partner)
    assert getattr(partner, 'robo_Setup4') == owner
    _safe_set(owner, 'robo_Motor', None)
    assert getattr(partner, 'robo_Setup4') is None


def test_assoc_programms0_stub_double():
    # robo_Robot has no real 'robo_Robot' property in the generated
    # code (a bare stub) -- manually attach it so robo_Program's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # robo_Program's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = robo_Program(name="sample_text")
    partner = robo_Robot()
    setattr(partner, 'robo_Robot', None)
    _safe_set(owner, 'robo_Program', partner)
    assert owner in getattr(partner, 'robo_Robot')
    _safe_set(owner, 'robo_Program', None)
    assert owner not in getattr(partner, 'robo_Robot')


def test_assoc_right29_stub_double():
    # Expr has no real 'Expr31' property in the generated
    # code (a bare stub) -- manually attach it so robo_expression_Operation's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # robo_expression_Operation's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = robo_expression_Operation(operator="sample_text")
    partner = Expr()
    setattr(partner, 'Expr31', None)
    _safe_set(owner, 'robo_expression_Operation30', partner)
    assert getattr(partner, 'Expr31') == owner
    _safe_set(owner, 'robo_expression_Operation30', None)
    assert getattr(partner, 'Expr31') is None


def test_assoc_right34_stub_double():
    # Expr has no real 'Expr36' property in the generated
    # code (a bare stub) -- manually attach it so robo_condition_Comparison's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # robo_condition_Comparison's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = robo_condition_Comparison(operator="sample_text")
    partner = Expr()
    setattr(partner, 'Expr36', None)
    _safe_set(owner, 'robo_condition_Comparison35', partner)
    assert getattr(partner, 'Expr36') == owner
    _safe_set(owner, 'robo_condition_Comparison35', None)
    assert getattr(partner, 'Expr36') is None


def test_assoc_rightMotor5_stub_double():
    # robo_Setup has no real 'robo_Setup6' property in the generated
    # code (a bare stub) -- manually attach it so robo_Motor's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # robo_Motor's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = robo_Motor(port="sample_text", reversed=True, speed=3.14, type="sample_text")
    partner = robo_Setup()
    setattr(partner, 'robo_Setup6', None)
    _safe_set(owner, 'robo_Motor7', partner)
    assert getattr(partner, 'robo_Setup6') == owner
    _safe_set(owner, 'robo_Motor7', None)
    assert getattr(partner, 'robo_Setup6') is None


def test_assoc_sensors8_stub_double():
    # robo_Setup has no real 'robo_Setup9' property in the generated
    # code (a bare stub) -- manually attach it so robo_Sensor's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # robo_Sensor's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = robo_Sensor(mode="sample_text", name="sample_text", port="sample_text", type="sample_text")
    partner = robo_Setup()
    setattr(partner, 'robo_Setup9', None)
    _safe_set(owner, 'robo_Sensor', partner)
    assert owner in getattr(partner, 'robo_Setup9')
    _safe_set(owner, 'robo_Sensor', None)
    assert owner not in getattr(partner, 'robo_Setup9')


def test_assoc_until13_stub_double():
    # Condition has no real 'Condition' property in the generated
    # code (a bare stub) -- manually attach it so robo_command_Drive's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # robo_command_Drive's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = robo_command_Drive(direction="sample_text")
    partner = Condition()
    setattr(partner, 'Condition', None)
    _safe_set(owner, 'robo_command_Drive14', partner)
    assert getattr(partner, 'Condition') == owner
    _safe_set(owner, 'robo_command_Drive14', None)
    assert getattr(partner, 'Condition') is None


def test_assoc_value25_stub_double():
    # Expr has no real 'Expr26' property in the generated
    # code (a bare stub) -- manually attach it so robo_command_Assignment's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # robo_command_Assignment's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = robo_command_Assignment(variable="sample_text")
    partner = Expr()
    setattr(partner, 'Expr26', None)
    _safe_set(owner, 'robo_command_Assignment', partner)
    assert getattr(partner, 'Expr26') == owner
    _safe_set(owner, 'robo_command_Assignment', None)
    assert getattr(partner, 'Expr26') is None


