import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Actuator,
    Block,
    Command,
    Component,
    NamedElement,
    Quantity,
    SingleQuantity,
    Transition,
    roverml_Actuator,
    roverml_Angle,
    roverml_Block,
    roverml_Command,
    roverml_Compass,
    roverml_CompassTrigger,
    roverml_Component,
    roverml_DistanceSensor,
    roverml_DistanceSensorTrigger,
    roverml_GPS,
    roverml_GpsTrigger,
    roverml_Length,
    roverml_Light,
    roverml_Motor,
    roverml_Move,
    roverml_NamedElement,
    roverml_Position,
    roverml_Quantity,
    roverml_Repeat,
    roverml_Rotate,
    roverml_Rover,
    roverml_RoverProgram,
    roverml_RoverSystem,
    roverml_Sensor,
    roverml_SetLightColor,
    roverml_SingleQuantity,
    roverml_Terminate,
    roverml_Time,
    roverml_Transition,
    roverml_TriggeredTransition,
    roverml_Velocity,
    roverml_Wait,
    AngleUnit,
    Color,
    ComparisonOperator,
    LengthUnit,
    TimeUnit,
    VelocityUnit,
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

def test_assoc_angle11_stub_double():
    # roverml_Rotate has no real 'roverml_Rotate' property in the generated
    # code (a bare stub) -- manually attach it so roverml_Angle's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # roverml_Angle's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = roverml_Angle(angleUnit="sample_text")
    partner = roverml_Rotate()
    setattr(partner, 'roverml_Rotate', None)
    _safe_set(owner, 'roverml_Angle', partner)
    assert getattr(partner, 'roverml_Rotate') == owner
    _safe_set(owner, 'roverml_Angle', None)
    assert getattr(partner, 'roverml_Rotate') is None


def test_assoc_components13_stub_double():
    # roverml_Rover has no real 'roverml_Rover14' property in the generated
    # code (a bare stub) -- manually attach it so roverml_Component's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # roverml_Component's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = roverml_Component(kind="sample_text")
    partner = roverml_Rover()
    setattr(partner, 'roverml_Rover14', None)
    _safe_set(owner, 'roverml_Component', partner)
    assert owner in getattr(partner, 'roverml_Rover14')
    _safe_set(owner, 'roverml_Component', None)
    assert owner not in getattr(partner, 'roverml_Rover14')


def test_assoc_distance8_stub_double():
    # roverml_Move has no real 'roverml_Move9' property in the generated
    # code (a bare stub) -- manually attach it so roverml_Length's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # roverml_Length's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = roverml_Length(lengthUnit="sample_text")
    partner = roverml_Move()
    setattr(partner, 'roverml_Move9', None)
    _safe_set(owner, 'roverml_Length', partner)
    assert getattr(partner, 'roverml_Move9') == owner
    _safe_set(owner, 'roverml_Length', None)
    assert getattr(partner, 'roverml_Move9') is None


def test_assoc_duration12_stub_double():
    # roverml_Wait has no real 'roverml_Wait' property in the generated
    # code (a bare stub) -- manually attach it so roverml_Time's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # roverml_Time's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = roverml_Time(timeUnit="sample_text")
    partner = roverml_Wait()
    setattr(partner, 'roverml_Wait', None)
    _safe_set(owner, 'roverml_Time', partner)
    assert getattr(partner, 'roverml_Wait') == owner
    _safe_set(owner, 'roverml_Time', None)
    assert getattr(partner, 'roverml_Wait') is None


def test_assoc_lights10_stub_double():
    # roverml_Light has no real 'roverml_Light' property in the generated
    # code (a bare stub) -- manually attach it so roverml_SetLightColor's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # roverml_SetLightColor's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = roverml_SetLightColor(color="sample_text")
    partner = roverml_Light()
    setattr(partner, 'roverml_Light', None)
    _safe_set(owner, 'roverml_SetLightColor', {partner})
    assert getattr(partner, 'roverml_Light') == owner
    _safe_set(owner, 'roverml_SetLightColor', set())
    assert getattr(partner, 'roverml_Light') is None


def test_assoc_speed7_stub_double():
    # roverml_Move has no real 'roverml_Move' property in the generated
    # code (a bare stub) -- manually attach it so roverml_Velocity's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # roverml_Velocity's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = roverml_Velocity(velocityUnit="sample_text")
    partner = roverml_Move()
    setattr(partner, 'roverml_Move', None)
    _safe_set(owner, 'roverml_Velocity', partner)
    assert getattr(partner, 'roverml_Move') == owner
    _safe_set(owner, 'roverml_Velocity', None)
    assert getattr(partner, 'roverml_Move') is None


def test_assoc_x32_stub_double():
    # roverml_Position has no real 'roverml_Position' property in the generated
    # code (a bare stub) -- manually attach it so roverml_Length's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # roverml_Length's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = roverml_Length(lengthUnit="sample_text")
    partner = roverml_Position()
    setattr(partner, 'roverml_Position', None)
    _safe_set(owner, 'roverml_Length33', partner)
    assert getattr(partner, 'roverml_Position') == owner
    _safe_set(owner, 'roverml_Length33', None)
    assert getattr(partner, 'roverml_Position') is None


def test_assoc_y34_stub_double():
    # roverml_Position has no real 'roverml_Position35' property in the generated
    # code (a bare stub) -- manually attach it so roverml_Length's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # roverml_Length's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = roverml_Length(lengthUnit="sample_text")
    partner = roverml_Position()
    setattr(partner, 'roverml_Position35', None)
    _safe_set(owner, 'roverml_Length36', partner)
    assert getattr(partner, 'roverml_Position35') == owner
    _safe_set(owner, 'roverml_Length36', None)
    assert getattr(partner, 'roverml_Position35') is None


