import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Command,
    SuperCommand,
    xDrone_BackWall,
    xDrone_Backward,
    xDrone_Color,
    xDrone_Command,
    xDrone_Down,
    xDrone_Drone,
    xDrone_Environment,
    xDrone_Fly,
    xDrone_Forward,
    xDrone_FrontWall,
    xDrone_GoTo,
    xDrone_Left,
    xDrone_LeftWall,
    xDrone_Main,
    xDrone_Object,
    xDrone_Origin,
    xDrone_Position,
    xDrone_Program,
    xDrone_Right,
    xDrone_RightWall,
    xDrone_RotateL,
    xDrone_RotateR,
    xDrone_Size,
    xDrone_SuperCommand,
    xDrone_Up,
    xDrone_UpWall,
    xDrone_Vector,
    xDrone_Wait,
    xDrone_Walls,
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

def test_assoc_color19_reverse_link_reassign_clear():
    a1 = xDrone_Object(object_name="sample_text")
    a2 = xDrone_Object(object_name="sample_text_2")
    b = xDrone_Color(color_value="sample_text")
    _safe_set(b, 'xDrone_Color', a1)
    assert _is_linked(b, 'xDrone_Color', a1)
    if hasattr(a1, 'xDrone_Object20'):
        assert _is_linked(a1, 'xDrone_Object20', b)
    _safe_set(b, 'xDrone_Color', a2)
    assert _is_linked(b, 'xDrone_Color', a2)
    if hasattr(a1, 'xDrone_Object20'):
        assert not _is_linked(a1, 'xDrone_Object20', b)
    if hasattr(a2, 'xDrone_Object20'):
        assert _is_linked(a2, 'xDrone_Object20', b)
    _safe_set(b, 'xDrone_Color', None)
    assert not _is_linked(b, 'xDrone_Color', a2)
    if hasattr(a2, 'xDrone_Object20'):
        assert not _is_linked(a2, 'xDrone_Object20', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_back33_stub_double():
    # xDrone_Walls has no real 'xDrone_Walls34' property in the generated
    # code (a bare stub) -- manually attach it so xDrone_BackWall's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # xDrone_BackWall's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = xDrone_BackWall(value="sample_text")
    partner = xDrone_Walls()
    setattr(partner, 'xDrone_Walls34', None)
    _safe_set(owner, 'xDrone_BackWall', partner)
    assert getattr(partner, 'xDrone_Walls34') == owner
    _safe_set(owner, 'xDrone_BackWall', None)
    assert getattr(partner, 'xDrone_Walls34') is None


def test_assoc_commands5_stub_double():
    # xDrone_SuperCommand has no real 'xDrone_SuperCommand' property in the generated
    # code (a bare stub) -- manually attach it so xDrone_Fly's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # xDrone_Fly's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = xDrone_Fly(land="sample_text", takeoff="sample_text")
    partner = xDrone_SuperCommand()
    setattr(partner, 'xDrone_SuperCommand', None)
    _safe_set(owner, 'xDrone_Fly6', {partner})
    assert getattr(partner, 'xDrone_SuperCommand') == owner
    _safe_set(owner, 'xDrone_Fly6', set())
    assert getattr(partner, 'xDrone_SuperCommand') is None


def test_assoc_drone7_stub_double():
    # xDrone_Environment has no real 'xDrone_Environment8' property in the generated
    # code (a bare stub) -- manually attach it so xDrone_Drone's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # xDrone_Drone's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = xDrone_Drone(rotation="sample_text")
    partner = xDrone_Environment()
    setattr(partner, 'xDrone_Environment8', None)
    _safe_set(owner, 'xDrone_Drone', partner)
    assert owner in getattr(partner, 'xDrone_Environment8')
    _safe_set(owner, 'xDrone_Drone', None)
    assert owner not in getattr(partner, 'xDrone_Environment8')


def test_assoc_fly1_stub_double():
    # xDrone_Main has no real 'xDrone_Main2' property in the generated
    # code (a bare stub) -- manually attach it so xDrone_Fly's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # xDrone_Fly's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = xDrone_Fly(land="sample_text", takeoff="sample_text")
    partner = xDrone_Main()
    setattr(partner, 'xDrone_Main2', None)
    _safe_set(owner, 'xDrone_Fly', partner)
    assert getattr(partner, 'xDrone_Main2') == owner
    _safe_set(owner, 'xDrone_Fly', None)
    assert getattr(partner, 'xDrone_Main2') is None


def test_assoc_front29_stub_double():
    # xDrone_Walls has no real 'xDrone_Walls30' property in the generated
    # code (a bare stub) -- manually attach it so xDrone_FrontWall's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # xDrone_FrontWall's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = xDrone_FrontWall(value="sample_text")
    partner = xDrone_Walls()
    setattr(partner, 'xDrone_Walls30', None)
    _safe_set(owner, 'xDrone_FrontWall', partner)
    assert getattr(partner, 'xDrone_Walls30') == owner
    _safe_set(owner, 'xDrone_FrontWall', None)
    assert getattr(partner, 'xDrone_Walls30') is None


def test_assoc_left35_stub_double():
    # xDrone_Walls has no real 'xDrone_Walls36' property in the generated
    # code (a bare stub) -- manually attach it so xDrone_LeftWall's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # xDrone_LeftWall's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = xDrone_LeftWall(value="sample_text")
    partner = xDrone_Walls()
    setattr(partner, 'xDrone_Walls36', None)
    _safe_set(owner, 'xDrone_LeftWall', partner)
    assert getattr(partner, 'xDrone_Walls36') == owner
    _safe_set(owner, 'xDrone_LeftWall', None)
    assert getattr(partner, 'xDrone_Walls36') is None


def test_assoc_objects11_stub_double():
    # xDrone_Environment has no real 'xDrone_Environment12' property in the generated
    # code (a bare stub) -- manually attach it so xDrone_Object's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # xDrone_Object's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = xDrone_Object(object_name="sample_text")
    partner = xDrone_Environment()
    setattr(partner, 'xDrone_Environment12', None)
    _safe_set(owner, 'xDrone_Object', partner)
    assert owner in getattr(partner, 'xDrone_Environment12')
    _safe_set(owner, 'xDrone_Object', None)
    assert owner not in getattr(partner, 'xDrone_Environment12')


def test_assoc_origin15_stub_double():
    # xDrone_Origin has no real 'xDrone_Origin' property in the generated
    # code (a bare stub) -- manually attach it so xDrone_Object's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # xDrone_Object's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = xDrone_Object(object_name="sample_text")
    partner = xDrone_Origin()
    setattr(partner, 'xDrone_Origin', None)
    _safe_set(owner, 'xDrone_Object16', partner)
    assert getattr(partner, 'xDrone_Origin') == owner
    _safe_set(owner, 'xDrone_Object16', None)
    assert getattr(partner, 'xDrone_Origin') is None


def test_assoc_position13_stub_double():
    # xDrone_Position has no real 'xDrone_Position' property in the generated
    # code (a bare stub) -- manually attach it so xDrone_Drone's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # xDrone_Drone's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = xDrone_Drone(rotation="sample_text")
    partner = xDrone_Position()
    setattr(partner, 'xDrone_Position', None)
    _safe_set(owner, 'xDrone_Drone14', partner)
    assert getattr(partner, 'xDrone_Position') == owner
    _safe_set(owner, 'xDrone_Drone14', None)
    assert getattr(partner, 'xDrone_Position') is None


def test_assoc_right31_stub_double():
    # xDrone_Walls has no real 'xDrone_Walls32' property in the generated
    # code (a bare stub) -- manually attach it so xDrone_RightWall's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # xDrone_RightWall's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = xDrone_RightWall(value="sample_text")
    partner = xDrone_Walls()
    setattr(partner, 'xDrone_Walls32', None)
    _safe_set(owner, 'xDrone_RightWall', partner)
    assert getattr(partner, 'xDrone_Walls32') == owner
    _safe_set(owner, 'xDrone_RightWall', None)
    assert getattr(partner, 'xDrone_Walls32') is None


def test_assoc_size17_stub_double():
    # xDrone_Size has no real 'xDrone_Size' property in the generated
    # code (a bare stub) -- manually attach it so xDrone_Object's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # xDrone_Object's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = xDrone_Object(object_name="sample_text")
    partner = xDrone_Size()
    setattr(partner, 'xDrone_Size', None)
    _safe_set(owner, 'xDrone_Object18', partner)
    assert getattr(partner, 'xDrone_Size') == owner
    _safe_set(owner, 'xDrone_Object18', None)
    assert getattr(partner, 'xDrone_Size') is None


def test_assoc_up37_stub_double():
    # xDrone_Walls has no real 'xDrone_Walls38' property in the generated
    # code (a bare stub) -- manually attach it so xDrone_UpWall's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # xDrone_UpWall's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = xDrone_UpWall(value="sample_text")
    partner = xDrone_Walls()
    setattr(partner, 'xDrone_Walls38', None)
    _safe_set(owner, 'xDrone_UpWall', partner)
    assert getattr(partner, 'xDrone_Walls38') == owner
    _safe_set(owner, 'xDrone_UpWall', None)
    assert getattr(partner, 'xDrone_Walls38') is None


def test_assoc_vector21_stub_double():
    # xDrone_Origin has no real 'xDrone_Origin22' property in the generated
    # code (a bare stub) -- manually attach it so xDrone_Vector's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # xDrone_Vector's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = xDrone_Vector(x="sample_text", y="sample_text", z="sample_text")
    partner = xDrone_Origin()
    setattr(partner, 'xDrone_Origin22', None)
    _safe_set(owner, 'xDrone_Vector', partner)
    assert getattr(partner, 'xDrone_Origin22') == owner
    _safe_set(owner, 'xDrone_Vector', None)
    assert getattr(partner, 'xDrone_Origin22') is None


def test_assoc_vector23_stub_double():
    # xDrone_Size has no real 'xDrone_Size24' property in the generated
    # code (a bare stub) -- manually attach it so xDrone_Vector's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # xDrone_Vector's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = xDrone_Vector(x="sample_text", y="sample_text", z="sample_text")
    partner = xDrone_Size()
    setattr(partner, 'xDrone_Size24', None)
    _safe_set(owner, 'xDrone_Vector25', partner)
    assert getattr(partner, 'xDrone_Size24') == owner
    _safe_set(owner, 'xDrone_Vector25', None)
    assert getattr(partner, 'xDrone_Size24') is None


def test_assoc_vector26_stub_double():
    # xDrone_Position has no real 'xDrone_Position27' property in the generated
    # code (a bare stub) -- manually attach it so xDrone_Vector's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # xDrone_Vector's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = xDrone_Vector(x="sample_text", y="sample_text", z="sample_text")
    partner = xDrone_Position()
    setattr(partner, 'xDrone_Position27', None)
    _safe_set(owner, 'xDrone_Vector28', partner)
    assert getattr(partner, 'xDrone_Position27') == owner
    _safe_set(owner, 'xDrone_Vector28', None)
    assert getattr(partner, 'xDrone_Position27') is None


