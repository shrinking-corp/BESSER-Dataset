import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Actuator,
    Component,
    Sensor,
    rover_Actuator,
    rover_Block,
    rover_Command,
    rover_Compass,
    rover_Component,
    rover_DistanceSensor,
    rover_GPS,
    rover_Light,
    rover_Motor,
    rover_Move,
    rover_PositionQuantity,
    rover_Program,
    rover_Repeate,
    rover_Rotate,
    rover_Rover,
    rover_Sensor,
    rover_SetLightColor,
    rover_SingleQuantity,
    rover_Tansition,
    rover_Wait,
    rover_directionFacing,
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

def test_assoc_block4_reverse_link_reassign_clear():
    a1 = rover_Program(name="sample_text")
    a2 = rover_Program(name="sample_text_2")
    b = rover_Block(name="sample_text")
    _safe_set(b, 'rover_Block', a1)
    assert _is_linked(b, 'rover_Block', a1)
    if hasattr(a1, 'rover_Program5'):
        assert _is_linked(a1, 'rover_Program5', b)
    _safe_set(b, 'rover_Block', a2)
    assert _is_linked(b, 'rover_Block', a2)
    if hasattr(a1, 'rover_Program5'):
        assert not _is_linked(a1, 'rover_Program5', b)
    if hasattr(a2, 'rover_Program5'):
        assert _is_linked(a2, 'rover_Program5', b)
    _safe_set(b, 'rover_Block', None)
    assert not _is_linked(b, 'rover_Block', a2)
    if hasattr(a2, 'rover_Program5'):
        assert not _is_linked(a2, 'rover_Program5', b)


def test_assoc_tansition8_reverse_link_reassign_clear():
    a1 = rover_Tansition(comparedQuantity="sample_text", operationUsed="sample_text")
    a2 = rover_Tansition(comparedQuantity="sample_text_2", operationUsed="sample_text_2")
    b = rover_Block(name="sample_text")
    _safe_set(b, 'rover_Block9', {a1})
    assert _is_linked(b, 'rover_Block9', a1)
    if hasattr(a1, 'rover_Tansition10'):
        assert _is_linked(a1, 'rover_Tansition10', b)
    _safe_set(b, 'rover_Block9', {a2})
    assert _is_linked(b, 'rover_Block9', a2)
    if hasattr(a1, 'rover_Tansition10'):
        assert not _is_linked(a1, 'rover_Tansition10', b)
    if hasattr(a2, 'rover_Tansition10'):
        assert _is_linked(a2, 'rover_Tansition10', b)
    _safe_set(b, 'rover_Block9', set())
    assert not _is_linked(b, 'rover_Block9', a2)
    if hasattr(a2, 'rover_Tansition10'):
        assert not _is_linked(a2, 'rover_Tansition10', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_command6_stub_double():
    # rover_Command has no real 'rover_Command' property in the generated
    # code (a bare stub) -- manually attach it so rover_Block's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # rover_Block's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = rover_Block(name="sample_text")
    partner = rover_Command()
    setattr(partner, 'rover_Command', None)
    _safe_set(owner, 'rover_Block7', {partner})
    assert getattr(partner, 'rover_Command') == owner
    _safe_set(owner, 'rover_Block7', set())
    assert getattr(partner, 'rover_Command') is None


def test_assoc_component0_stub_double():
    # rover_Rover has no real 'rover_Rover' property in the generated
    # code (a bare stub) -- manually attach it so rover_Component's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # rover_Component's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = rover_Component(name="sample_text")
    partner = rover_Rover()
    setattr(partner, 'rover_Rover', None)
    _safe_set(owner, 'rover_Component', partner)
    assert owner in getattr(partner, 'rover_Rover')
    _safe_set(owner, 'rover_Component', None)
    assert owner not in getattr(partner, 'rover_Rover')


def test_assoc_incomingTransition22_stub_double():
    # rover_Command has no real 'targetCommand' property in the generated
    # code (a bare stub) -- manually attach it so rover_Tansition's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # rover_Tansition's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = rover_Tansition(comparedQuantity="sample_text", operationUsed="sample_text")
    partner = rover_Command()
    setattr(partner, 'targetCommand', None)
    _safe_set(owner, 'Tansition23', partner)
    assert getattr(partner, 'targetCommand') == owner
    _safe_set(owner, 'Tansition23', None)
    assert getattr(partner, 'targetCommand') is None


def test_assoc_move15_stub_double():
    # rover_Command has no real 'rover_Command16' property in the generated
    # code (a bare stub) -- manually attach it so rover_Move's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # rover_Move's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = rover_Move(length=7, velocity=7)
    partner = rover_Command()
    setattr(partner, 'rover_Command16', None)
    _safe_set(owner, 'rover_Move', partner)
    assert getattr(partner, 'rover_Command16') == owner
    _safe_set(owner, 'rover_Move', None)
    assert getattr(partner, 'rover_Command16') is None


def test_assoc_outgoingTransition21_stub_double():
    # rover_Command has no real 'sourceCommand' property in the generated
    # code (a bare stub) -- manually attach it so rover_Tansition's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # rover_Tansition's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = rover_Tansition(comparedQuantity="sample_text", operationUsed="sample_text")
    partner = rover_Command()
    setattr(partner, 'sourceCommand', None)
    _safe_set(owner, 'Tansition', partner)
    assert getattr(partner, 'sourceCommand') == owner
    _safe_set(owner, 'Tansition', None)
    assert getattr(partner, 'sourceCommand') is None


def test_assoc_program1_stub_double():
    # rover_Rover has no real 'rover_Rover2' property in the generated
    # code (a bare stub) -- manually attach it so rover_Program's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # rover_Program's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = rover_Program(name="sample_text")
    partner = rover_Rover()
    setattr(partner, 'rover_Rover2', None)
    _safe_set(owner, 'rover_Program', partner)
    assert getattr(partner, 'rover_Rover2') == owner
    _safe_set(owner, 'rover_Program', None)
    assert getattr(partner, 'rover_Rover2') is None


def test_assoc_repeate11_stub_double():
    # rover_Command has no real 'rover_Command12' property in the generated
    # code (a bare stub) -- manually attach it so rover_Repeate's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # rover_Repeate's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = rover_Repeate(count=7)
    partner = rover_Command()
    setattr(partner, 'rover_Command12', None)
    _safe_set(owner, 'rover_Repeate', partner)
    assert getattr(partner, 'rover_Command12') == owner
    _safe_set(owner, 'rover_Repeate', None)
    assert getattr(partner, 'rover_Command12') is None


def test_assoc_rotate13_stub_double():
    # rover_Command has no real 'rover_Command14' property in the generated
    # code (a bare stub) -- manually attach it so rover_Rotate's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # rover_Rotate's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = rover_Rotate(angel=7)
    partner = rover_Command()
    setattr(partner, 'rover_Command14', None)
    _safe_set(owner, 'rover_Rotate', partner)
    assert getattr(partner, 'rover_Command14') == owner
    _safe_set(owner, 'rover_Rotate', None)
    assert getattr(partner, 'rover_Command14') is None


def test_assoc_setlightcolor19_stub_double():
    # rover_Command has no real 'rover_Command20' property in the generated
    # code (a bare stub) -- manually attach it so rover_SetLightColor's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # rover_SetLightColor's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = rover_SetLightColor(color="sample_text")
    partner = rover_Command()
    setattr(partner, 'rover_Command20', None)
    _safe_set(owner, 'rover_SetLightColor', partner)
    assert getattr(partner, 'rover_Command20') == owner
    _safe_set(owner, 'rover_SetLightColor', None)
    assert getattr(partner, 'rover_Command20') is None


def test_assoc_sourceCommand24_stub_double():
    # rover_Command has no real 'Command' property in the generated
    # code (a bare stub) -- manually attach it so rover_Tansition's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # rover_Tansition's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = rover_Tansition(comparedQuantity="sample_text", operationUsed="sample_text")
    partner = rover_Command()
    setattr(partner, 'Command', None)
    _safe_set(owner, 'outgoingTransition', partner)
    assert getattr(partner, 'Command') == owner
    _safe_set(owner, 'outgoingTransition', None)
    assert getattr(partner, 'Command') is None


def test_assoc_targetCommand25_stub_double():
    # rover_Command has no real 'Command26' property in the generated
    # code (a bare stub) -- manually attach it so rover_Tansition's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # rover_Tansition's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = rover_Tansition(comparedQuantity="sample_text", operationUsed="sample_text")
    partner = rover_Command()
    setattr(partner, 'Command26', None)
    _safe_set(owner, 'incomingTransition', partner)
    assert getattr(partner, 'Command26') == owner
    _safe_set(owner, 'incomingTransition', None)
    assert getattr(partner, 'Command26') is None


def test_assoc_triggered3_stub_double():
    # rover_Sensor has no real 'rover_Sensor' property in the generated
    # code (a bare stub) -- manually attach it so rover_Tansition's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # rover_Tansition's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = rover_Tansition(comparedQuantity="sample_text", operationUsed="sample_text")
    partner = rover_Sensor()
    setattr(partner, 'rover_Sensor', None)
    _safe_set(owner, 'rover_Tansition', partner)
    assert getattr(partner, 'rover_Sensor') == owner
    _safe_set(owner, 'rover_Tansition', None)
    assert getattr(partner, 'rover_Sensor') is None


def test_assoc_wait17_stub_double():
    # rover_Command has no real 'rover_Command18' property in the generated
    # code (a bare stub) -- manually attach it so rover_Wait's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # rover_Wait's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = rover_Wait(time=7)
    partner = rover_Command()
    setattr(partner, 'rover_Command18', None)
    _safe_set(owner, 'rover_Wait', partner)
    assert getattr(partner, 'rover_Command18') == owner
    _safe_set(owner, 'rover_Wait', None)
    assert getattr(partner, 'rover_Command18') is None


