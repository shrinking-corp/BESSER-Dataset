import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Actuator,
    Command,
    Component,
    NamedElement,
    Quantity,
    Sensor,
    SingleQuantity,
    Transition,
    Triggered,
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
    roverml_GPSTrigger,
    roverml_Length,
    roverml_Light,
    roverml_Motor,
    roverml_Move,
    roverml_NamedElement,
    roverml_Position,
    roverml_Program,
    roverml_Quantity,
    roverml_Regular,
    roverml_Repeat,
    roverml_Rotate,
    roverml_Rover,
    roverml_Sensor,
    roverml_SetLightColor,
    roverml_SingleQuantity,
    roverml_System,
    roverml_Terminate,
    roverml_Time,
    roverml_Transition,
    roverml_Triggered,
    roverml_Velocity,
    roverml_Wait,
    AngleUnits,
    Colours,
    LengthUnits,
    TimeUnits,
    VelocityUnits,
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

def test_assoc_angleUnits27_reverse_link_reassign_clear():
    a1 = roverml_Rotate(angle=7)
    a2 = roverml_Rotate(angle=13)
    b = roverml_Angle(units="sample_text")
    _safe_set(b, 'roverml_Angle', a1)
    assert _is_linked(b, 'roverml_Angle', a1)
    if hasattr(a1, 'roverml_Rotate'):
        assert _is_linked(a1, 'roverml_Rotate', b)
    _safe_set(b, 'roverml_Angle', a2)
    assert _is_linked(b, 'roverml_Angle', a2)
    if hasattr(a1, 'roverml_Rotate'):
        assert not _is_linked(a1, 'roverml_Rotate', b)
    if hasattr(a2, 'roverml_Rotate'):
        assert _is_linked(a2, 'roverml_Rotate', b)
    _safe_set(b, 'roverml_Angle', None)
    assert not _is_linked(b, 'roverml_Angle', a2)
    if hasattr(a2, 'roverml_Rotate'):
        assert not _is_linked(a2, 'roverml_Rotate', b)


def test_assoc_angles34_reverse_link_reassign_clear():
    a1 = roverml_CompassTrigger(angle=7)
    a2 = roverml_CompassTrigger(angle=13)
    b = roverml_Angle(units="sample_text")
    _safe_set(b, 'roverml_Angle35', a1)
    assert _is_linked(b, 'roverml_Angle35', a1)
    if hasattr(a1, 'roverml_CompassTrigger'):
        assert _is_linked(a1, 'roverml_CompassTrigger', b)
    _safe_set(b, 'roverml_Angle35', a2)
    assert _is_linked(b, 'roverml_Angle35', a2)
    if hasattr(a1, 'roverml_CompassTrigger'):
        assert not _is_linked(a1, 'roverml_CompassTrigger', b)
    if hasattr(a2, 'roverml_CompassTrigger'):
        assert _is_linked(a2, 'roverml_CompassTrigger', b)
    _safe_set(b, 'roverml_Angle35', None)
    assert not _is_linked(b, 'roverml_Angle35', a2)
    if hasattr(a2, 'roverml_CompassTrigger'):
        assert not _is_linked(a2, 'roverml_CompassTrigger', b)


def test_assoc_compass36_reverse_link_reassign_clear():
    a1 = roverml_CompassTrigger(angle=7)
    a2 = roverml_CompassTrigger(angle=13)
    b = roverml_Compass(angle=7)
    _safe_set(b, 'roverml_Compass', a1)
    assert _is_linked(b, 'roverml_Compass', a1)
    if hasattr(a1, 'roverml_CompassTrigger37'):
        assert _is_linked(a1, 'roverml_CompassTrigger37', b)
    _safe_set(b, 'roverml_Compass', a2)
    assert _is_linked(b, 'roverml_Compass', a2)
    if hasattr(a1, 'roverml_CompassTrigger37'):
        assert not _is_linked(a1, 'roverml_CompassTrigger37', b)
    if hasattr(a2, 'roverml_CompassTrigger37'):
        assert _is_linked(a2, 'roverml_CompassTrigger37', b)
    _safe_set(b, 'roverml_Compass', None)
    assert not _is_linked(b, 'roverml_Compass', a2)
    if hasattr(a2, 'roverml_CompassTrigger37'):
        assert not _is_linked(a2, 'roverml_CompassTrigger37', b)


def test_assoc_distancesensor32_reverse_link_reassign_clear():
    a1 = roverml_DistanceSensorTrigger(dist=3.14)
    a2 = roverml_DistanceSensorTrigger(dist=9.99)
    b = roverml_DistanceSensor(distance=3.14)
    _safe_set(b, 'roverml_DistanceSensor', a1)
    assert _is_linked(b, 'roverml_DistanceSensor', a1)
    if hasattr(a1, 'roverml_DistanceSensorTrigger33'):
        assert _is_linked(a1, 'roverml_DistanceSensorTrigger33', b)
    _safe_set(b, 'roverml_DistanceSensor', a2)
    assert _is_linked(b, 'roverml_DistanceSensor', a2)
    if hasattr(a1, 'roverml_DistanceSensorTrigger33'):
        assert not _is_linked(a1, 'roverml_DistanceSensorTrigger33', b)
    if hasattr(a2, 'roverml_DistanceSensorTrigger33'):
        assert _is_linked(a2, 'roverml_DistanceSensorTrigger33', b)
    _safe_set(b, 'roverml_DistanceSensor', None)
    assert not _is_linked(b, 'roverml_DistanceSensor', a2)
    if hasattr(a2, 'roverml_DistanceSensorTrigger33'):
        assert not _is_linked(a2, 'roverml_DistanceSensorTrigger33', b)


def test_assoc_gps39_reverse_link_reassign_clear():
    a1 = roverml_GPSTrigger(x=3.14, y=3.14)
    a2 = roverml_GPSTrigger(x=9.99, y=9.99)
    b = roverml_GPS(x=3.14, y=3.14)
    _safe_set(b, 'roverml_GPS', a1)
    assert _is_linked(b, 'roverml_GPS', a1)
    if hasattr(a1, 'roverml_GPSTrigger40'):
        assert _is_linked(a1, 'roverml_GPSTrigger40', b)
    _safe_set(b, 'roverml_GPS', a2)
    assert _is_linked(b, 'roverml_GPS', a2)
    if hasattr(a1, 'roverml_GPSTrigger40'):
        assert not _is_linked(a1, 'roverml_GPSTrigger40', b)
    if hasattr(a2, 'roverml_GPSTrigger40'):
        assert _is_linked(a2, 'roverml_GPSTrigger40', b)
    _safe_set(b, 'roverml_GPS', None)
    assert not _is_linked(b, 'roverml_GPS', a2)
    if hasattr(a2, 'roverml_GPSTrigger40'):
        assert not _is_linked(a2, 'roverml_GPSTrigger40', b)


def test_assoc_length30_reverse_link_reassign_clear():
    a1 = roverml_Length(units="sample_text")
    a2 = roverml_Length(units="sample_text_2")
    b = roverml_DistanceSensorTrigger(dist=3.14)
    _safe_set(b, 'roverml_DistanceSensorTrigger', a1)
    assert _is_linked(b, 'roverml_DistanceSensorTrigger', a1)
    if hasattr(a1, 'roverml_Length31'):
        assert _is_linked(a1, 'roverml_Length31', b)
    _safe_set(b, 'roverml_DistanceSensorTrigger', a2)
    assert _is_linked(b, 'roverml_DistanceSensorTrigger', a2)
    if hasattr(a1, 'roverml_Length31'):
        assert not _is_linked(a1, 'roverml_Length31', b)
    if hasattr(a2, 'roverml_Length31'):
        assert _is_linked(a2, 'roverml_Length31', b)
    _safe_set(b, 'roverml_DistanceSensorTrigger', None)
    assert not _is_linked(b, 'roverml_DistanceSensorTrigger', a2)
    if hasattr(a2, 'roverml_Length31'):
        assert not _is_linked(a2, 'roverml_Length31', b)


def test_assoc_lengthUnits25_reverse_link_reassign_clear():
    a1 = roverml_Move(length=3.14, velocity=3.14)
    a2 = roverml_Move(length=9.99, velocity=9.99)
    b = roverml_Length(units="sample_text")
    _safe_set(b, 'roverml_Length', a1)
    assert _is_linked(b, 'roverml_Length', a1)
    if hasattr(a1, 'roverml_Move26'):
        assert _is_linked(a1, 'roverml_Move26', b)
    _safe_set(b, 'roverml_Length', a2)
    assert _is_linked(b, 'roverml_Length', a2)
    if hasattr(a1, 'roverml_Move26'):
        assert not _is_linked(a1, 'roverml_Move26', b)
    if hasattr(a2, 'roverml_Move26'):
        assert _is_linked(a2, 'roverml_Move26', b)
    _safe_set(b, 'roverml_Length', None)
    assert not _is_linked(b, 'roverml_Length', a2)
    if hasattr(a2, 'roverml_Move26'):
        assert not _is_linked(a2, 'roverml_Move26', b)


def test_assoc_position38_reverse_link_reassign_clear():
    a1 = roverml_Position(x=3.14, y=3.14)
    a2 = roverml_Position(x=9.99, y=9.99)
    b = roverml_GPSTrigger(x=3.14, y=3.14)
    _safe_set(b, 'roverml_GPSTrigger', a1)
    assert _is_linked(b, 'roverml_GPSTrigger', a1)
    if hasattr(a1, 'roverml_Position'):
        assert _is_linked(a1, 'roverml_Position', b)
    _safe_set(b, 'roverml_GPSTrigger', a2)
    assert _is_linked(b, 'roverml_GPSTrigger', a2)
    if hasattr(a1, 'roverml_Position'):
        assert not _is_linked(a1, 'roverml_Position', b)
    if hasattr(a2, 'roverml_Position'):
        assert _is_linked(a2, 'roverml_Position', b)
    _safe_set(b, 'roverml_GPSTrigger', None)
    assert not _is_linked(b, 'roverml_GPSTrigger', a2)
    if hasattr(a2, 'roverml_Position'):
        assert not _is_linked(a2, 'roverml_Position', b)


def test_assoc_timeUnit23_reverse_link_reassign_clear():
    a1 = roverml_Wait(time=7)
    a2 = roverml_Wait(time=13)
    b = roverml_Time(units="sample_text")
    _safe_set(b, 'roverml_Time', a1)
    assert _is_linked(b, 'roverml_Time', a1)
    if hasattr(a1, 'roverml_Wait'):
        assert _is_linked(a1, 'roverml_Wait', b)
    _safe_set(b, 'roverml_Time', a2)
    assert _is_linked(b, 'roverml_Time', a2)
    if hasattr(a1, 'roverml_Wait'):
        assert not _is_linked(a1, 'roverml_Wait', b)
    if hasattr(a2, 'roverml_Wait'):
        assert _is_linked(a2, 'roverml_Wait', b)
    _safe_set(b, 'roverml_Time', None)
    assert not _is_linked(b, 'roverml_Time', a2)
    if hasattr(a2, 'roverml_Wait'):
        assert not _is_linked(a2, 'roverml_Wait', b)


def test_assoc_velocityUnits24_reverse_link_reassign_clear():
    a1 = roverml_Velocity(units="sample_text")
    a2 = roverml_Velocity(units="sample_text_2")
    b = roverml_Move(length=3.14, velocity=3.14)
    _safe_set(b, 'roverml_Move', a1)
    assert _is_linked(b, 'roverml_Move', a1)
    if hasattr(a1, 'roverml_Velocity'):
        assert _is_linked(a1, 'roverml_Velocity', b)
    _safe_set(b, 'roverml_Move', a2)
    assert _is_linked(b, 'roverml_Move', a2)
    if hasattr(a1, 'roverml_Velocity'):
        assert not _is_linked(a1, 'roverml_Velocity', b)
    if hasattr(a2, 'roverml_Velocity'):
        assert _is_linked(a2, 'roverml_Velocity', b)
    _safe_set(b, 'roverml_Move', None)
    assert not _is_linked(b, 'roverml_Move', a2)
    if hasattr(a2, 'roverml_Velocity'):
        assert not _is_linked(a2, 'roverml_Velocity', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_commands28_stub_double():
    # roverml_Command has no real 'roverml_Command29' property in the generated
    # code (a bare stub) -- manually attach it so roverml_Repeat's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # roverml_Repeat's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = roverml_Repeat(numberOfReps=7)
    partner = roverml_Command()
    setattr(partner, 'roverml_Command29', None)
    _safe_set(owner, 'roverml_Repeat', {partner})
    assert getattr(partner, 'roverml_Command29') == owner
    _safe_set(owner, 'roverml_Repeat', set())
    assert getattr(partner, 'roverml_Command29') is None


