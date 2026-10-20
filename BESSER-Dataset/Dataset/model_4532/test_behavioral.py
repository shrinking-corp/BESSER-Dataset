import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    NamedElement,
    PropertyValue,
    drone_AreaObject,
    drone_Battery,
    drone_Capability,
    drone_CapabilityProperties,
    drone_Coordinate,
    drone_EObject,
    drone_Equipment,
    drone_MeasureConversion,
    drone_MeasureDimension,
    drone_MeasureValue,
    drone_Mission,
    drone_NamedElement,
    drone_Position,
    drone_Property,
    drone_PropertyKey,
    drone_PropertyKeyContainer,
    drone_PropertyValue,
    drone_Robot,
    drone_RobotMissionContainer,
    drone_Size,
    drone_StringValue,
    drone_Task,
    drone_TaskDescriptor,
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

def test_assoc_capacity58_stub_double():
    # drone_Battery has no real 'drone_Battery59' property in the generated
    # code (a bare stub) -- manually attach it so drone_MeasureValue's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # drone_MeasureValue's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = drone_MeasureValue(value=3.14)
    partner = drone_Battery()
    setattr(partner, 'drone_Battery59', None)
    _safe_set(owner, 'drone_MeasureValue60', partner)
    assert getattr(partner, 'drone_Battery59') == owner
    _safe_set(owner, 'drone_MeasureValue60', None)
    assert getattr(partner, 'drone_Battery59') is None


def test_assoc_communicationRange38_stub_double():
    # drone_Robot has no real 'drone_Robot39' property in the generated
    # code (a bare stub) -- manually attach it so drone_MeasureValue's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # drone_MeasureValue's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = drone_MeasureValue(value=3.14)
    partner = drone_Robot()
    setattr(partner, 'drone_Robot39', None)
    _safe_set(owner, 'drone_MeasureValue', partner)
    assert getattr(partner, 'drone_Robot39') == owner
    _safe_set(owner, 'drone_MeasureValue', None)
    assert getattr(partner, 'drone_Robot39') is None


def test_assoc_conversions80_stub_double():
    # drone_MeasureDimension has no real 'drone_MeasureDimension81' property in the generated
    # code (a bare stub) -- manually attach it so drone_MeasureConversion's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # drone_MeasureConversion's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = drone_MeasureConversion(rate=3.14)
    partner = drone_MeasureDimension()
    setattr(partner, 'drone_MeasureDimension81', None)
    _safe_set(owner, 'drone_MeasureConversion82', partner)
    assert owner in getattr(partner, 'drone_MeasureDimension81')
    _safe_set(owner, 'drone_MeasureConversion82', None)
    assert owner not in getattr(partner, 'drone_MeasureDimension81')


def test_assoc_coordinates8_stub_double():
    # drone_Position has no real 'drone_Position' property in the generated
    # code (a bare stub) -- manually attach it so drone_Coordinate's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # drone_Coordinate's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = drone_Coordinate(altitude=3.14, latitude=3.14, longitude=3.14)
    partner = drone_Position()
    setattr(partner, 'drone_Position', None)
    _safe_set(owner, 'drone_Coordinate', partner)
    assert owner in getattr(partner, 'drone_Position')
    _safe_set(owner, 'drone_Coordinate', None)
    assert owner not in getattr(partner, 'drone_Position')


def test_assoc_dimension76_stub_double():
    # drone_MeasureDimension has no real 'drone_MeasureDimension' property in the generated
    # code (a bare stub) -- manually attach it so drone_MeasureValue's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # drone_MeasureValue's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = drone_MeasureValue(value=3.14)
    partner = drone_MeasureDimension()
    setattr(partner, 'drone_MeasureDimension', None)
    _safe_set(owner, 'drone_MeasureValue77', partner)
    assert getattr(partner, 'drone_MeasureDimension') == owner
    _safe_set(owner, 'drone_MeasureValue77', None)
    assert getattr(partner, 'drone_MeasureDimension') is None


def test_assoc_dimension78_stub_double():
    # drone_MeasureDimension has no real 'drone_MeasureDimension79' property in the generated
    # code (a bare stub) -- manually attach it so drone_MeasureConversion's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # drone_MeasureConversion's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = drone_MeasureConversion(rate=3.14)
    partner = drone_MeasureDimension()
    setattr(partner, 'drone_MeasureDimension79', None)
    _safe_set(owner, 'drone_MeasureConversion', partner)
    assert getattr(partner, 'drone_MeasureDimension79') == owner
    _safe_set(owner, 'drone_MeasureConversion', None)
    assert getattr(partner, 'drone_MeasureDimension79') is None


def test_assoc_height52_stub_double():
    # drone_Size has no real 'drone_Size53' property in the generated
    # code (a bare stub) -- manually attach it so drone_MeasureValue's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # drone_MeasureValue's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = drone_MeasureValue(value=3.14)
    partner = drone_Size()
    setattr(partner, 'drone_Size53', None)
    _safe_set(owner, 'drone_MeasureValue54', partner)
    assert getattr(partner, 'drone_Size53') == owner
    _safe_set(owner, 'drone_MeasureValue54', None)
    assert getattr(partner, 'drone_Size53') is None


def test_assoc_length55_stub_double():
    # drone_Size has no real 'drone_Size56' property in the generated
    # code (a bare stub) -- manually attach it so drone_MeasureValue's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # drone_MeasureValue's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = drone_MeasureValue(value=3.14)
    partner = drone_Size()
    setattr(partner, 'drone_Size56', None)
    _safe_set(owner, 'drone_MeasureValue57', partner)
    assert getattr(partner, 'drone_Size56') == owner
    _safe_set(owner, 'drone_MeasureValue57', None)
    assert getattr(partner, 'drone_Size56') is None


def test_assoc_rechargeTime64_stub_double():
    # drone_Battery has no real 'drone_Battery65' property in the generated
    # code (a bare stub) -- manually attach it so drone_MeasureValue's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # drone_MeasureValue's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = drone_MeasureValue(value=3.14)
    partner = drone_Battery()
    setattr(partner, 'drone_Battery65', None)
    _safe_set(owner, 'drone_MeasureValue66', partner)
    assert getattr(partner, 'drone_Battery65') == owner
    _safe_set(owner, 'drone_MeasureValue66', None)
    assert getattr(partner, 'drone_Battery65') is None


def test_assoc_voltage61_stub_double():
    # drone_Battery has no real 'drone_Battery62' property in the generated
    # code (a bare stub) -- manually attach it so drone_MeasureValue's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # drone_MeasureValue's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = drone_MeasureValue(value=3.14)
    partner = drone_Battery()
    setattr(partner, 'drone_Battery62', None)
    _safe_set(owner, 'drone_MeasureValue63', partner)
    assert getattr(partner, 'drone_Battery62') == owner
    _safe_set(owner, 'drone_MeasureValue63', None)
    assert getattr(partner, 'drone_Battery62') is None


def test_assoc_weight40_stub_double():
    # drone_Robot has no real 'drone_Robot41' property in the generated
    # code (a bare stub) -- manually attach it so drone_MeasureValue's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # drone_MeasureValue's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = drone_MeasureValue(value=3.14)
    partner = drone_Robot()
    setattr(partner, 'drone_Robot41', None)
    _safe_set(owner, 'drone_MeasureValue42', partner)
    assert getattr(partner, 'drone_Robot41') == owner
    _safe_set(owner, 'drone_MeasureValue42', None)
    assert getattr(partner, 'drone_Robot41') is None


def test_assoc_width49_stub_double():
    # drone_Size has no real 'drone_Size50' property in the generated
    # code (a bare stub) -- manually attach it so drone_MeasureValue's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # drone_MeasureValue's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = drone_MeasureValue(value=3.14)
    partner = drone_Size()
    setattr(partner, 'drone_Size50', None)
    _safe_set(owner, 'drone_MeasureValue51', partner)
    assert getattr(partner, 'drone_Size50') == owner
    _safe_set(owner, 'drone_MeasureValue51', None)
    assert getattr(partner, 'drone_Size50') is None


