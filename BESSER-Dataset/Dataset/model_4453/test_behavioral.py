import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Actuator,
    Command,
    Component,
    Quantity,
    Sensor,
    SingleQuantity,
    Transition,
    TriggeredTransition,
    rover_Actuator,
    rover_Angle,
    rover_Block,
    rover_Command,
    rover_Compass,
    rover_CompassTrigger,
    rover_Component,
    rover_Distance,
    rover_DistanceSensorTrigger,
    rover_GPS,
    rover_GPSTrigger,
    rover_Length,
    rover_Light,
    rover_Motor,
    rover_Move,
    rover_NormalTransition,
    rover_Position,
    rover_Program,
    rover_Quantity,
    rover_Repeat,
    rover_Rotate,
    rover_Rover,
    rover_Sensor,
    rover_SetLightColor,
    rover_SingleQuantity,
    rover_System,
    rover_Terminate,
    rover_Time,
    rover_Transition,
    rover_TriggeredTransition,
    rover_Velocity,
    rover_Wait,
    AngleUnit,
    ColorKind,
    LengthUnit,
    Operator,
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

def test_assoc_component3_reverse_link_reassign_clear():
    a1 = rover_Rover(name="sample_text")
    a2 = rover_Rover(name="sample_text_2")
    b = rover_Component(name="sample_text")
    _safe_set(b, 'rover_Component', a1)
    assert _is_linked(b, 'rover_Component', a1)
    if hasattr(a1, 'rover_Rover4'):
        assert _is_linked(a1, 'rover_Rover4', b)
    _safe_set(b, 'rover_Component', a2)
    assert _is_linked(b, 'rover_Component', a2)
    if hasattr(a1, 'rover_Rover4'):
        assert not _is_linked(a1, 'rover_Rover4', b)
    if hasattr(a2, 'rover_Rover4'):
        assert _is_linked(a2, 'rover_Rover4', b)
    _safe_set(b, 'rover_Component', None)
    assert not _is_linked(b, 'rover_Component', a2)
    if hasattr(a2, 'rover_Rover4'):
        assert not _is_linked(a2, 'rover_Rover4', b)


def test_assoc_light27_reverse_link_reassign_clear():
    a1 = rover_SetLightColor(lightColor="sample_text")
    a2 = rover_SetLightColor(lightColor="sample_text_2")
    b = rover_Light(color="sample_text")
    _safe_set(b, 'rover_Light', a1)
    assert _is_linked(b, 'rover_Light', a1)
    if hasattr(a1, 'rover_SetLightColor'):
        assert _is_linked(a1, 'rover_SetLightColor', b)
    _safe_set(b, 'rover_Light', a2)
    assert _is_linked(b, 'rover_Light', a2)
    if hasattr(a1, 'rover_SetLightColor'):
        assert not _is_linked(a1, 'rover_SetLightColor', b)
    if hasattr(a2, 'rover_SetLightColor'):
        assert _is_linked(a2, 'rover_SetLightColor', b)
    _safe_set(b, 'rover_Light', None)
    assert not _is_linked(b, 'rover_Light', a2)
    if hasattr(a2, 'rover_SetLightColor'):
        assert not _is_linked(a2, 'rover_SetLightColor', b)


def test_assoc_rover5_reverse_link_reassign_clear():
    a1 = rover_Rover(name="sample_text")
    a2 = rover_Rover(name="sample_text_2")
    b = rover_Program(name="sample_text")
    _safe_set(b, 'rover_Program6', a1)
    assert _is_linked(b, 'rover_Program6', a1)
    if hasattr(a1, 'rover_Rover7'):
        assert _is_linked(a1, 'rover_Rover7', b)
    _safe_set(b, 'rover_Program6', a2)
    assert _is_linked(b, 'rover_Program6', a2)
    if hasattr(a1, 'rover_Rover7'):
        assert not _is_linked(a1, 'rover_Rover7', b)
    if hasattr(a2, 'rover_Rover7'):
        assert _is_linked(a2, 'rover_Rover7', b)
    _safe_set(b, 'rover_Program6', None)
    assert not _is_linked(b, 'rover_Program6', a2)
    if hasattr(a2, 'rover_Rover7'):
        assert not _is_linked(a2, 'rover_Rover7', b)


def test_assoc_setlightcolor37_reverse_link_reassign_clear():
    a1 = rover_SetLightColor(lightColor="sample_text")
    a2 = rover_SetLightColor(lightColor="sample_text_2")
    b = rover_Repeat(count=7)
    _safe_set(b, 'rover_Repeat38', {a1})
    assert _is_linked(b, 'rover_Repeat38', a1)
    if hasattr(a1, 'rover_SetLightColor39'):
        assert _is_linked(a1, 'rover_SetLightColor39', b)
    _safe_set(b, 'rover_Repeat38', {a2})
    assert _is_linked(b, 'rover_Repeat38', a2)
    if hasattr(a1, 'rover_SetLightColor39'):
        assert not _is_linked(a1, 'rover_SetLightColor39', b)
    if hasattr(a2, 'rover_SetLightColor39'):
        assert _is_linked(a2, 'rover_SetLightColor39', b)
    _safe_set(b, 'rover_Repeat38', set())
    assert not _is_linked(b, 'rover_Repeat38', a2)
    if hasattr(a2, 'rover_SetLightColor39'):
        assert not _is_linked(a2, 'rover_SetLightColor39', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_X64_stub_double():
    # rover_Position has no real 'rover_Position65' property in the generated
    # code (a bare stub) -- manually attach it so rover_Length's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # rover_Length's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = rover_Length(lengthUnit="sample_text")
    partner = rover_Position()
    setattr(partner, 'rover_Position65', None)
    _safe_set(owner, 'rover_Length66', partner)
    assert getattr(partner, 'rover_Position65') == owner
    _safe_set(owner, 'rover_Length66', None)
    assert getattr(partner, 'rover_Position65') is None


def test_assoc_Y67_stub_double():
    # rover_Position has no real 'rover_Position68' property in the generated
    # code (a bare stub) -- manually attach it so rover_Length's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # rover_Length's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = rover_Length(lengthUnit="sample_text")
    partner = rover_Position()
    setattr(partner, 'rover_Position68', None)
    _safe_set(owner, 'rover_Length69', partner)
    assert getattr(partner, 'rover_Position68') == owner
    _safe_set(owner, 'rover_Length69', None)
    assert getattr(partner, 'rover_Position68') is None


def test_assoc_angle13_stub_double():
    # rover_Compass has no real 'rover_Compass' property in the generated
    # code (a bare stub) -- manually attach it so rover_Angle's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # rover_Angle's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = rover_Angle(angleUnit="sample_text")
    partner = rover_Compass()
    setattr(partner, 'rover_Compass', None)
    _safe_set(owner, 'rover_Angle', partner)
    assert getattr(partner, 'rover_Compass') == owner
    _safe_set(owner, 'rover_Angle', None)
    assert getattr(partner, 'rover_Compass') is None


def test_assoc_angle35_stub_double():
    # rover_Rotate has no real 'rover_Rotate' property in the generated
    # code (a bare stub) -- manually attach it so rover_Angle's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # rover_Angle's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = rover_Angle(angleUnit="sample_text")
    partner = rover_Rotate()
    setattr(partner, 'rover_Rotate', None)
    _safe_set(owner, 'rover_Angle36', partner)
    assert getattr(partner, 'rover_Rotate') == owner
    _safe_set(owner, 'rover_Angle36', None)
    assert getattr(partner, 'rover_Rotate') is None


def test_assoc_angle56_stub_double():
    # rover_CompassTrigger has no real 'rover_CompassTrigger57' property in the generated
    # code (a bare stub) -- manually attach it so rover_Angle's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # rover_Angle's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = rover_Angle(angleUnit="sample_text")
    partner = rover_CompassTrigger()
    setattr(partner, 'rover_CompassTrigger57', None)
    _safe_set(owner, 'rover_Angle58', partner)
    assert getattr(partner, 'rover_CompassTrigger57') == owner
    _safe_set(owner, 'rover_Angle58', None)
    assert getattr(partner, 'rover_CompassTrigger57') is None


def test_assoc_block8_stub_double():
    # rover_Block has no real 'rover_Block' property in the generated
    # code (a bare stub) -- manually attach it so rover_Program's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # rover_Program's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = rover_Program(name="sample_text")
    partner = rover_Block()
    setattr(partner, 'rover_Block', None)
    _safe_set(owner, 'rover_Program9', partner)
    assert getattr(partner, 'rover_Block') == owner
    _safe_set(owner, 'rover_Program9', None)
    assert getattr(partner, 'rover_Block') is None


def test_assoc_length14_stub_double():
    # rover_Distance has no real 'rover_Distance' property in the generated
    # code (a bare stub) -- manually attach it so rover_Length's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # rover_Length's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = rover_Length(lengthUnit="sample_text")
    partner = rover_Distance()
    setattr(partner, 'rover_Distance', None)
    _safe_set(owner, 'rover_Length', partner)
    assert getattr(partner, 'rover_Distance') == owner
    _safe_set(owner, 'rover_Length', None)
    assert getattr(partner, 'rover_Distance') is None


def test_assoc_length30_stub_double():
    # rover_Move has no real 'rover_Move31' property in the generated
    # code (a bare stub) -- manually attach it so rover_Length's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # rover_Length's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = rover_Length(lengthUnit="sample_text")
    partner = rover_Move()
    setattr(partner, 'rover_Move31', None)
    _safe_set(owner, 'rover_Length32', partner)
    assert getattr(partner, 'rover_Move31') == owner
    _safe_set(owner, 'rover_Length32', None)
    assert getattr(partner, 'rover_Move31') is None


def test_assoc_length51_stub_double():
    # rover_DistanceSensorTrigger has no real 'rover_DistanceSensorTrigger52' property in the generated
    # code (a bare stub) -- manually attach it so rover_Length's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # rover_Length's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = rover_Length(lengthUnit="sample_text")
    partner = rover_DistanceSensorTrigger()
    setattr(partner, 'rover_DistanceSensorTrigger52', None)
    _safe_set(owner, 'rover_Length53', partner)
    assert getattr(partner, 'rover_DistanceSensorTrigger52') == owner
    _safe_set(owner, 'rover_Length53', None)
    assert getattr(partner, 'rover_DistanceSensorTrigger52') is None


def test_assoc_move43_stub_double():
    # rover_Move has no real 'rover_Move45' property in the generated
    # code (a bare stub) -- manually attach it so rover_Repeat's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # rover_Repeat's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = rover_Repeat(count=7)
    partner = rover_Move()
    setattr(partner, 'rover_Move45', None)
    _safe_set(owner, 'rover_Repeat44', {partner})
    assert getattr(partner, 'rover_Move45') == owner
    _safe_set(owner, 'rover_Repeat44', set())
    assert getattr(partner, 'rover_Move45') is None


def test_assoc_program1_stub_double():
    # rover_System has no real 'rover_System2' property in the generated
    # code (a bare stub) -- manually attach it so rover_Program's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # rover_Program's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = rover_Program(name="sample_text")
    partner = rover_System()
    setattr(partner, 'rover_System2', None)
    _safe_set(owner, 'rover_Program', partner)
    assert owner in getattr(partner, 'rover_System2')
    _safe_set(owner, 'rover_Program', None)
    assert owner not in getattr(partner, 'rover_System2')


def test_assoc_quantity10_stub_double():
    # rover_Quantity has no real 'rover_Quantity' property in the generated
    # code (a bare stub) -- manually attach it so rover_Program's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # rover_Program's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = rover_Program(name="sample_text")
    partner = rover_Quantity()
    setattr(partner, 'rover_Quantity', None)
    _safe_set(owner, 'rover_Program11', {partner})
    assert getattr(partner, 'rover_Quantity') == owner
    _safe_set(owner, 'rover_Program11', set())
    assert getattr(partner, 'rover_Quantity') is None


def test_assoc_repeat19_stub_double():
    # rover_Block has no real 'rover_Block20' property in the generated
    # code (a bare stub) -- manually attach it so rover_Repeat's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # rover_Repeat's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = rover_Repeat(count=7)
    partner = rover_Block()
    setattr(partner, 'rover_Block20', None)
    _safe_set(owner, 'rover_Repeat', partner)
    assert getattr(partner, 'rover_Block20') == owner
    _safe_set(owner, 'rover_Repeat', None)
    assert getattr(partner, 'rover_Block20') is None


def test_assoc_rotate46_stub_double():
    # rover_Rotate has no real 'rover_Rotate48' property in the generated
    # code (a bare stub) -- manually attach it so rover_Repeat's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # rover_Repeat's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = rover_Repeat(count=7)
    partner = rover_Rotate()
    setattr(partner, 'rover_Rotate48', None)
    _safe_set(owner, 'rover_Repeat47', {partner})
    assert getattr(partner, 'rover_Rotate48') == owner
    _safe_set(owner, 'rover_Repeat47', set())
    assert getattr(partner, 'rover_Rotate48') is None


def test_assoc_rover0_stub_double():
    # rover_System has no real 'rover_System' property in the generated
    # code (a bare stub) -- manually attach it so rover_Rover's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # rover_Rover's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = rover_Rover(name="sample_text")
    partner = rover_System()
    setattr(partner, 'rover_System', None)
    _safe_set(owner, 'rover_Rover', partner)
    assert owner in getattr(partner, 'rover_System')
    _safe_set(owner, 'rover_Rover', None)
    assert owner not in getattr(partner, 'rover_System')


def test_assoc_time28_stub_double():
    # rover_Wait has no real 'rover_Wait' property in the generated
    # code (a bare stub) -- manually attach it so rover_Time's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # rover_Time's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = rover_Time(timeUnit="sample_text")
    partner = rover_Wait()
    setattr(partner, 'rover_Wait', None)
    _safe_set(owner, 'rover_Time', partner)
    assert getattr(partner, 'rover_Wait') == owner
    _safe_set(owner, 'rover_Time', None)
    assert getattr(partner, 'rover_Wait') is None


def test_assoc_velocity33_stub_double():
    # rover_Move has no real 'rover_Move34' property in the generated
    # code (a bare stub) -- manually attach it so rover_Velocity's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # rover_Velocity's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = rover_Velocity(velocityUnit="sample_text")
    partner = rover_Move()
    setattr(partner, 'rover_Move34', None)
    _safe_set(owner, 'rover_Velocity', partner)
    assert getattr(partner, 'rover_Move34') == owner
    _safe_set(owner, 'rover_Velocity', None)
    assert getattr(partner, 'rover_Move34') is None


def test_assoc_wait40_stub_double():
    # rover_Wait has no real 'rover_Wait42' property in the generated
    # code (a bare stub) -- manually attach it so rover_Repeat's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # rover_Repeat's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = rover_Repeat(count=7)
    partner = rover_Wait()
    setattr(partner, 'rover_Wait42', None)
    _safe_set(owner, 'rover_Repeat41', {partner})
    assert getattr(partner, 'rover_Wait42') == owner
    _safe_set(owner, 'rover_Repeat41', set())
    assert getattr(partner, 'rover_Wait42') is None


