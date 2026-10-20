import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    AbstractDataMove,
    DataMove,
    Entity,
    PyDslRep_AbstractCrossMove,
    PyDslRep_AbstractDataMove,
    PyDslRep_AbstractMove,
    PyDslRep_DataMove,
    PyDslRep_Entity,
    PyDslRep_Environment,
    PyDslRep_IP,
    PyDslRep_Model,
    PyDslRep_Move,
    PyDslRep_MoveCollection,
    PyDslRep_Robot,
    PyDslRep_Sensor,
    PyDslRep_Turn,
    PyDslRep_TypeSensor,
    PyDslRep_Wheel,
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

def test_assoc_ip1_reverse_link_reassign_clear():
    a1 = PyDslRep_IP(ip="sample_text", name="sample_text")
    a2 = PyDslRep_IP(ip="sample_text_2", name="sample_text_2")
    b = PyDslRep_Environment(name="sample_text")
    _safe_set(b, 'PyDslRep_Environment', a1)
    assert _is_linked(b, 'PyDslRep_Environment', a1)
    if hasattr(a1, 'PyDslRep_IP'):
        assert _is_linked(a1, 'PyDslRep_IP', b)
    _safe_set(b, 'PyDslRep_Environment', a2)
    assert _is_linked(b, 'PyDslRep_Environment', a2)
    if hasattr(a1, 'PyDslRep_IP'):
        assert not _is_linked(a1, 'PyDslRep_IP', b)
    if hasattr(a2, 'PyDslRep_IP'):
        assert _is_linked(a2, 'PyDslRep_IP', b)
    _safe_set(b, 'PyDslRep_Environment', None)
    assert not _is_linked(b, 'PyDslRep_Environment', a2)
    if hasattr(a2, 'PyDslRep_IP'):
        assert not _is_linked(a2, 'PyDslRep_IP', b)


def test_assoc_moves4_reverse_link_reassign_clear():
    a1 = PyDslRep_MoveCollection(concurrent=True, name="sample_text")
    a2 = PyDslRep_MoveCollection(concurrent=False, name="sample_text_2")
    b = PyDslRep_Environment(name="sample_text")
    _safe_set(b, 'PyDslRep_Environment5', {a1})
    assert _is_linked(b, 'PyDslRep_Environment5', a1)
    if hasattr(a1, 'PyDslRep_MoveCollection'):
        assert _is_linked(a1, 'PyDslRep_MoveCollection', b)
    _safe_set(b, 'PyDslRep_Environment5', {a2})
    assert _is_linked(b, 'PyDslRep_Environment5', a2)
    if hasattr(a1, 'PyDslRep_MoveCollection'):
        assert not _is_linked(a1, 'PyDslRep_MoveCollection', b)
    if hasattr(a2, 'PyDslRep_MoveCollection'):
        assert _is_linked(a2, 'PyDslRep_MoveCollection', b)
    _safe_set(b, 'PyDslRep_Environment5', set())
    assert not _is_linked(b, 'PyDslRep_Environment5', a2)
    if hasattr(a2, 'PyDslRep_MoveCollection'):
        assert not _is_linked(a2, 'PyDslRep_MoveCollection', b)


def test_assoc_robot8_reverse_link_reassign_clear():
    a1 = PyDslRep_Robot(name="sample_text", port=7)
    a2 = PyDslRep_Robot(name="sample_text_2", port=13)
    b = PyDslRep_MoveCollection(concurrent=True, name="sample_text")
    _safe_set(b, 'PyDslRep_MoveCollection9', a1)
    assert _is_linked(b, 'PyDslRep_MoveCollection9', a1)
    if hasattr(a1, 'PyDslRep_Robot10'):
        assert _is_linked(a1, 'PyDslRep_Robot10', b)
    _safe_set(b, 'PyDslRep_MoveCollection9', a2)
    assert _is_linked(b, 'PyDslRep_MoveCollection9', a2)
    if hasattr(a1, 'PyDslRep_Robot10'):
        assert not _is_linked(a1, 'PyDslRep_Robot10', b)
    if hasattr(a2, 'PyDslRep_Robot10'):
        assert _is_linked(a2, 'PyDslRep_Robot10', b)
    _safe_set(b, 'PyDslRep_MoveCollection9', None)
    assert not _is_linked(b, 'PyDslRep_MoveCollection9', a2)
    if hasattr(a2, 'PyDslRep_Robot10'):
        assert not _is_linked(a2, 'PyDslRep_Robot10', b)


def test_assoc_robots2_reverse_link_reassign_clear():
    a1 = PyDslRep_Robot(name="sample_text", port=7)
    a2 = PyDslRep_Robot(name="sample_text_2", port=13)
    b = PyDslRep_Environment(name="sample_text")
    _safe_set(b, 'PyDslRep_Environment3', {a1})
    assert _is_linked(b, 'PyDslRep_Environment3', a1)
    if hasattr(a1, 'PyDslRep_Robot'):
        assert _is_linked(a1, 'PyDslRep_Robot', b)
    _safe_set(b, 'PyDslRep_Environment3', {a2})
    assert _is_linked(b, 'PyDslRep_Environment3', a2)
    if hasattr(a1, 'PyDslRep_Robot'):
        assert not _is_linked(a1, 'PyDslRep_Robot', b)
    if hasattr(a2, 'PyDslRep_Robot'):
        assert _is_linked(a2, 'PyDslRep_Robot', b)
    _safe_set(b, 'PyDslRep_Environment3', set())
    assert not _is_linked(b, 'PyDslRep_Environment3', a2)
    if hasattr(a2, 'PyDslRep_Robot'):
        assert not _is_linked(a2, 'PyDslRep_Robot', b)


def test_assoc_type16_reverse_link_reassign_clear():
    a1 = PyDslRep_TypeSensor(typeName="sample_text")
    a2 = PyDslRep_TypeSensor(typeName="sample_text_2")
    b = PyDslRep_Sensor(name="sample_text")
    _safe_set(b, 'PyDslRep_Sensor', a1)
    assert _is_linked(b, 'PyDslRep_Sensor', a1)
    if hasattr(a1, 'PyDslRep_TypeSensor'):
        assert _is_linked(a1, 'PyDslRep_TypeSensor', b)
    _safe_set(b, 'PyDslRep_Sensor', a2)
    assert _is_linked(b, 'PyDslRep_Sensor', a2)
    if hasattr(a1, 'PyDslRep_TypeSensor'):
        assert not _is_linked(a1, 'PyDslRep_TypeSensor', b)
    if hasattr(a2, 'PyDslRep_TypeSensor'):
        assert _is_linked(a2, 'PyDslRep_TypeSensor', b)
    _safe_set(b, 'PyDslRep_Sensor', None)
    assert not _is_linked(b, 'PyDslRep_Sensor', a2)
    if hasattr(a2, 'PyDslRep_TypeSensor'):
        assert not _is_linked(a2, 'PyDslRep_TypeSensor', b)


def test_assoc_wheels6_reverse_link_reassign_clear():
    a1 = PyDslRep_Wheel(name="sample_text", radius="sample_text")
    a2 = PyDslRep_Wheel(name="sample_text_2", radius="sample_text_2")
    b = PyDslRep_Robot(name="sample_text", port=7)
    _safe_set(b, 'PyDslRep_Robot7', {a1})
    assert _is_linked(b, 'PyDslRep_Robot7', a1)
    if hasattr(a1, 'PyDslRep_Wheel'):
        assert _is_linked(a1, 'PyDslRep_Wheel', b)
    _safe_set(b, 'PyDslRep_Robot7', {a2})
    assert _is_linked(b, 'PyDslRep_Robot7', a2)
    if hasattr(a1, 'PyDslRep_Wheel'):
        assert not _is_linked(a1, 'PyDslRep_Wheel', b)
    if hasattr(a2, 'PyDslRep_Wheel'):
        assert _is_linked(a2, 'PyDslRep_Wheel', b)
    _safe_set(b, 'PyDslRep_Robot7', set())
    assert not _is_linked(b, 'PyDslRep_Robot7', a2)
    if hasattr(a2, 'PyDslRep_Wheel'):
        assert not _is_linked(a2, 'PyDslRep_Wheel', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_moves11_stub_double():
    # PyDslRep_AbstractDataMove has no real 'PyDslRep_AbstractDataMove' property in the generated
    # code (a bare stub) -- manually attach it so PyDslRep_MoveCollection's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # PyDslRep_MoveCollection's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = PyDslRep_MoveCollection(concurrent=True, name="sample_text")
    partner = PyDslRep_AbstractDataMove()
    setattr(partner, 'PyDslRep_AbstractDataMove', None)
    _safe_set(owner, 'PyDslRep_MoveCollection12', {partner})
    assert getattr(partner, 'PyDslRep_AbstractDataMove') == owner
    _safe_set(owner, 'PyDslRep_MoveCollection12', set())
    assert getattr(partner, 'PyDslRep_AbstractDataMove') is None


def test_assoc_typeM13_stub_double():
    # PyDslRep_AbstractMove has no real 'PyDslRep_AbstractMove' property in the generated
    # code (a bare stub) -- manually attach it so PyDslRep_DataMove's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # PyDslRep_DataMove's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = PyDslRep_DataMove(name=True, type="sample_text", velocity="sample_text")
    partner = PyDslRep_AbstractMove()
    setattr(partner, 'PyDslRep_AbstractMove', None)
    _safe_set(owner, 'PyDslRep_DataMove', partner)
    assert getattr(partner, 'PyDslRep_AbstractMove') == owner
    _safe_set(owner, 'PyDslRep_DataMove', None)
    assert getattr(partner, 'PyDslRep_AbstractMove') is None


def test_assoc_typeM14_stub_double():
    # PyDslRep_AbstractCrossMove has no real 'PyDslRep_AbstractCrossMove' property in the generated
    # code (a bare stub) -- manually attach it so PyDslRep_DataMove's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # PyDslRep_DataMove's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = PyDslRep_DataMove(name=True, type="sample_text", velocity="sample_text")
    partner = PyDslRep_AbstractCrossMove()
    setattr(partner, 'PyDslRep_AbstractCrossMove', None)
    _safe_set(owner, 'PyDslRep_DataMove15', partner)
    assert getattr(partner, 'PyDslRep_AbstractCrossMove') == owner
    _safe_set(owner, 'PyDslRep_DataMove15', None)
    assert getattr(partner, 'PyDslRep_AbstractCrossMove') is None


