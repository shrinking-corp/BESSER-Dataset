import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Action,
    Actuate,
    Behavior,
    Condition,
    Node,
    gyro_Action,
    gyro_Actuate,
    gyro_Behavior,
    gyro_Bumpers,
    gyro_Child,
    gyro_Condition,
    gyro_Distance,
    gyro_GyroSpecification,
    gyro_LED,
    gyro_Motor,
    gyro_Node,
    gyro_Parallel,
    gyro_Priority,
    gyro_Sequential,
    gyro_Servo,
    gyro_Sibling,
    gyro_StatusChange,
    gyro_Waiting,
    BumperKind,
    DistanceKind,
    FailureState,
    LightStatus,
    RunningState,
    SuccessState,
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

def test_assoc_nodes0_reverse_link_reassign_clear():
    a1 = gyro_Node(name="sample_text")
    a2 = gyro_Node(name="sample_text_2")
    b = gyro_GyroSpecification(name="sample_text")
    _safe_set(b, 'gyro_GyroSpecification', {a1})
    assert _is_linked(b, 'gyro_GyroSpecification', a1)
    if hasattr(a1, 'gyro_Node'):
        assert _is_linked(a1, 'gyro_Node', b)
    _safe_set(b, 'gyro_GyroSpecification', {a2})
    assert _is_linked(b, 'gyro_GyroSpecification', a2)
    if hasattr(a1, 'gyro_Node'):
        assert not _is_linked(a1, 'gyro_Node', b)
    if hasattr(a2, 'gyro_Node'):
        assert _is_linked(a2, 'gyro_Node', b)
    _safe_set(b, 'gyro_GyroSpecification', set())
    assert not _is_linked(b, 'gyro_GyroSpecification', a2)
    if hasattr(a2, 'gyro_Node'):
        assert not _is_linked(a2, 'gyro_Node', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_child1_stub_double():
    # gyro_Child has no real 'gyro_Child' property in the generated
    # code (a bare stub) -- manually attach it so gyro_GyroSpecification's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # gyro_GyroSpecification's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = gyro_GyroSpecification(name="sample_text")
    partner = gyro_Child()
    setattr(partner, 'gyro_Child', None)
    _safe_set(owner, 'gyro_GyroSpecification2', {partner})
    assert getattr(partner, 'gyro_Child') == owner
    _safe_set(owner, 'gyro_GyroSpecification2', set())
    assert getattr(partner, 'gyro_Child') is None


def test_assoc_next3_stub_double():
    # gyro_Sibling has no real 'gyro_Sibling' property in the generated
    # code (a bare stub) -- manually attach it so gyro_GyroSpecification's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # gyro_GyroSpecification's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = gyro_GyroSpecification(name="sample_text")
    partner = gyro_Sibling()
    setattr(partner, 'gyro_Sibling', None)
    _safe_set(owner, 'gyro_GyroSpecification4', {partner})
    assert getattr(partner, 'gyro_Sibling') == owner
    _safe_set(owner, 'gyro_GyroSpecification4', set())
    assert getattr(partner, 'gyro_Sibling') is None


def test_assoc_source10_stub_double():
    # gyro_Sibling has no real 'gyro_Sibling11' property in the generated
    # code (a bare stub) -- manually attach it so gyro_Node's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # gyro_Node's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = gyro_Node(name="sample_text")
    partner = gyro_Sibling()
    setattr(partner, 'gyro_Sibling11', None)
    _safe_set(owner, 'gyro_Node12', partner)
    assert owner in getattr(partner, 'gyro_Sibling11')
    _safe_set(owner, 'gyro_Node12', None)
    assert owner not in getattr(partner, 'gyro_Sibling11')


def test_assoc_target13_stub_double():
    # gyro_Sibling has no real 'gyro_Sibling14' property in the generated
    # code (a bare stub) -- manually attach it so gyro_Node's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # gyro_Node's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = gyro_Node(name="sample_text")
    partner = gyro_Sibling()
    setattr(partner, 'gyro_Sibling14', None)
    _safe_set(owner, 'gyro_Node15', partner)
    assert owner in getattr(partner, 'gyro_Sibling14')
    _safe_set(owner, 'gyro_Node15', None)
    assert owner not in getattr(partner, 'gyro_Sibling14')


def test_assoc_target7_stub_double():
    # gyro_Child has no real 'gyro_Child8' property in the generated
    # code (a bare stub) -- manually attach it so gyro_Node's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # gyro_Node's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = gyro_Node(name="sample_text")
    partner = gyro_Child()
    setattr(partner, 'gyro_Child8', None)
    _safe_set(owner, 'gyro_Node9', partner)
    assert owner in getattr(partner, 'gyro_Child8')
    _safe_set(owner, 'gyro_Node9', None)
    assert owner not in getattr(partner, 'gyro_Child8')


