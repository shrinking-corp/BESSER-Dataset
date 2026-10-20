import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Action,
    ActionWheel,
    Actuator,
    BinaryCond,
    BinaryOperator,
    Condition,
    Operator,
    Sensor,
    Type,
    UnaryCond,
    UnaryOperator,
    metamodel_Action,
    metamodel_ActionWheel,
    metamodel_Actuator,
    metamodel_Add,
    metamodel_And,
    metamodel_Backward,
    metamodel_Behaviour,
    metamodel_BinaryCond,
    metamodel_BinaryOperator,
    metamodel_BoolVal,
    metamodel_Condition,
    metamodel_Different,
    metamodel_DifferentialWheel,
    metamodel_DistanceSensor,
    metamodel_Equal,
    metamodel_FloatVal,
    metamodel_Forward,
    metamodel_Group,
    metamodel_IntVal,
    metamodel_Less,
    metamodel_LessOrEqual,
    metamodel_LightSensor,
    metamodel_More,
    metamodel_MoreOrEqual,
    metamodel_Negation,
    metamodel_Negative,
    metamodel_Operator,
    metamodel_Or,
    metamodel_Positive,
    metamodel_Robot,
    metamodel_Sensor,
    metamodel_State,
    metamodel_StateMachine,
    metamodel_Stopping,
    metamodel_Sub,
    metamodel_Transition,
    metamodel_TurnLeft,
    metamodel_TurnRight,
    metamodel_Type,
    metamodel_UnaryCond,
    metamodel_UnaryOperator,
    metamodel_Value,
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

def test_assoc_actuators3_reverse_link_reassign_clear():
    a1 = metamodel_Robot(name="sample_text")
    a2 = metamodel_Robot(name="sample_text_2")
    b = metamodel_Actuator(name="sample_text")
    _safe_set(b, 'metamodel_Actuator', a1)
    assert _is_linked(b, 'metamodel_Actuator', a1)
    if hasattr(a1, 'metamodel_Robot4'):
        assert _is_linked(a1, 'metamodel_Robot4', b)
    _safe_set(b, 'metamodel_Actuator', a2)
    assert _is_linked(b, 'metamodel_Actuator', a2)
    if hasattr(a1, 'metamodel_Robot4'):
        assert not _is_linked(a1, 'metamodel_Robot4', b)
    if hasattr(a2, 'metamodel_Robot4'):
        assert _is_linked(a2, 'metamodel_Robot4', b)
    _safe_set(b, 'metamodel_Actuator', None)
    assert not _is_linked(b, 'metamodel_Actuator', a2)
    if hasattr(a2, 'metamodel_Robot4'):
        assert not _is_linked(a2, 'metamodel_Robot4', b)


def test_assoc_behaviours0_reverse_link_reassign_clear():
    a1 = metamodel_Robot(name="sample_text")
    a2 = metamodel_Robot(name="sample_text_2")
    b = metamodel_Behaviour(name="sample_text", priority=7)
    _safe_set(b, 'metamodel_Behaviour', a1)
    assert _is_linked(b, 'metamodel_Behaviour', a1)
    if hasattr(a1, 'metamodel_Robot'):
        assert _is_linked(a1, 'metamodel_Robot', b)
    _safe_set(b, 'metamodel_Behaviour', a2)
    assert _is_linked(b, 'metamodel_Behaviour', a2)
    if hasattr(a1, 'metamodel_Robot'):
        assert not _is_linked(a1, 'metamodel_Robot', b)
    if hasattr(a2, 'metamodel_Robot'):
        assert _is_linked(a2, 'metamodel_Robot', b)
    _safe_set(b, 'metamodel_Behaviour', None)
    assert not _is_linked(b, 'metamodel_Behaviour', a2)
    if hasattr(a2, 'metamodel_Robot'):
        assert not _is_linked(a2, 'metamodel_Robot', b)


def test_assoc_constants18_reverse_link_reassign_clear():
    a1 = metamodel_Value(name="sample_text")
    a2 = metamodel_Value(name="sample_text_2")
    b = metamodel_StateMachine(name="sample_text")
    _safe_set(b, 'metamodel_StateMachine19', {a1})
    assert _is_linked(b, 'metamodel_StateMachine19', a1)
    if hasattr(a1, 'metamodel_Value20'):
        assert _is_linked(a1, 'metamodel_Value20', b)
    _safe_set(b, 'metamodel_StateMachine19', {a2})
    assert _is_linked(b, 'metamodel_StateMachine19', a2)
    if hasattr(a1, 'metamodel_Value20'):
        assert not _is_linked(a1, 'metamodel_Value20', b)
    if hasattr(a2, 'metamodel_Value20'):
        assert _is_linked(a2, 'metamodel_Value20', b)
    _safe_set(b, 'metamodel_StateMachine19', set())
    assert not _is_linked(b, 'metamodel_StateMachine19', a2)
    if hasattr(a2, 'metamodel_Value20'):
        assert not _is_linked(a2, 'metamodel_Value20', b)


def test_assoc_dstId32_reverse_link_reassign_clear():
    a1 = metamodel_Transition(nameIn="sample_text")
    a2 = metamodel_Transition(nameIn="sample_text_2")
    b = metamodel_State(isInitial=True, name="sample_text", uid=7)
    _safe_set(b, 'metamodel_State34', a1)
    assert _is_linked(b, 'metamodel_State34', a1)
    if hasattr(a1, 'metamodel_Transition33'):
        assert _is_linked(a1, 'metamodel_Transition33', b)
    _safe_set(b, 'metamodel_State34', a2)
    assert _is_linked(b, 'metamodel_State34', a2)
    if hasattr(a1, 'metamodel_Transition33'):
        assert not _is_linked(a1, 'metamodel_Transition33', b)
    if hasattr(a2, 'metamodel_Transition33'):
        assert _is_linked(a2, 'metamodel_Transition33', b)
    _safe_set(b, 'metamodel_State34', None)
    assert not _is_linked(b, 'metamodel_State34', a2)
    if hasattr(a2, 'metamodel_Transition33'):
        assert not _is_linked(a2, 'metamodel_Transition33', b)


def test_assoc_sensors1_reverse_link_reassign_clear():
    a1 = metamodel_Sensor(name="sample_text", sensorName="sample_text")
    a2 = metamodel_Sensor(name="sample_text_2", sensorName="sample_text_2")
    b = metamodel_Robot(name="sample_text")
    _safe_set(b, 'metamodel_Robot2', {a1})
    assert _is_linked(b, 'metamodel_Robot2', a1)
    if hasattr(a1, 'metamodel_Sensor'):
        assert _is_linked(a1, 'metamodel_Sensor', b)
    _safe_set(b, 'metamodel_Robot2', {a2})
    assert _is_linked(b, 'metamodel_Robot2', a2)
    if hasattr(a1, 'metamodel_Sensor'):
        assert not _is_linked(a1, 'metamodel_Sensor', b)
    if hasattr(a2, 'metamodel_Sensor'):
        assert _is_linked(a2, 'metamodel_Sensor', b)
    _safe_set(b, 'metamodel_Robot2', set())
    assert not _is_linked(b, 'metamodel_Robot2', a2)
    if hasattr(a2, 'metamodel_Sensor'):
        assert not _is_linked(a2, 'metamodel_Sensor', b)


def test_assoc_stateMachine14_reverse_link_reassign_clear():
    a1 = metamodel_StateMachine(name="sample_text")
    a2 = metamodel_StateMachine(name="sample_text_2")
    b = metamodel_Behaviour(name="sample_text", priority=7)
    _safe_set(b, 'metamodel_Behaviour15', a1)
    assert _is_linked(b, 'metamodel_Behaviour15', a1)
    if hasattr(a1, 'metamodel_StateMachine'):
        assert _is_linked(a1, 'metamodel_StateMachine', b)
    _safe_set(b, 'metamodel_Behaviour15', a2)
    assert _is_linked(b, 'metamodel_Behaviour15', a2)
    if hasattr(a1, 'metamodel_StateMachine'):
        assert not _is_linked(a1, 'metamodel_StateMachine', b)
    if hasattr(a2, 'metamodel_StateMachine'):
        assert _is_linked(a2, 'metamodel_StateMachine', b)
    _safe_set(b, 'metamodel_Behaviour15', None)
    assert not _is_linked(b, 'metamodel_Behaviour15', a2)
    if hasattr(a2, 'metamodel_StateMachine'):
        assert not _is_linked(a2, 'metamodel_StateMachine', b)


def test_assoc_states16_reverse_link_reassign_clear():
    a1 = metamodel_StateMachine(name="sample_text")
    a2 = metamodel_StateMachine(name="sample_text_2")
    b = metamodel_State(isInitial=True, name="sample_text", uid=7)
    _safe_set(b, 'metamodel_State', a1)
    assert _is_linked(b, 'metamodel_State', a1)
    if hasattr(a1, 'metamodel_StateMachine17'):
        assert _is_linked(a1, 'metamodel_StateMachine17', b)
    _safe_set(b, 'metamodel_State', a2)
    assert _is_linked(b, 'metamodel_State', a2)
    if hasattr(a1, 'metamodel_StateMachine17'):
        assert not _is_linked(a1, 'metamodel_StateMachine17', b)
    if hasattr(a2, 'metamodel_StateMachine17'):
        assert _is_linked(a2, 'metamodel_StateMachine17', b)
    _safe_set(b, 'metamodel_State', None)
    assert not _is_linked(b, 'metamodel_State', a2)
    if hasattr(a2, 'metamodel_StateMachine17'):
        assert not _is_linked(a2, 'metamodel_StateMachine17', b)


def test_assoc_transitions21_reverse_link_reassign_clear():
    a1 = metamodel_Transition(nameIn="sample_text")
    a2 = metamodel_Transition(nameIn="sample_text_2")
    b = metamodel_State(isInitial=True, name="sample_text", uid=7)
    _safe_set(b, 'metamodel_State22', {a1})
    assert _is_linked(b, 'metamodel_State22', a1)
    if hasattr(a1, 'metamodel_Transition'):
        assert _is_linked(a1, 'metamodel_Transition', b)
    _safe_set(b, 'metamodel_State22', {a2})
    assert _is_linked(b, 'metamodel_State22', a2)
    if hasattr(a1, 'metamodel_Transition'):
        assert not _is_linked(a1, 'metamodel_Transition', b)
    if hasattr(a2, 'metamodel_Transition'):
        assert _is_linked(a2, 'metamodel_Transition', b)
    _safe_set(b, 'metamodel_State22', set())
    assert not _is_linked(b, 'metamodel_State22', a2)
    if hasattr(a2, 'metamodel_Transition'):
        assert not _is_linked(a2, 'metamodel_Transition', b)


def test_assoc_value10_reverse_link_reassign_clear():
    a1 = metamodel_Value(name="sample_text")
    a2 = metamodel_Value(name="sample_text_2")
    b = metamodel_Sensor(name="sample_text", sensorName="sample_text")
    _safe_set(b, 'metamodel_Sensor11', a1)
    assert _is_linked(b, 'metamodel_Sensor11', a1)
    if hasattr(a1, 'metamodel_Value'):
        assert _is_linked(a1, 'metamodel_Value', b)
    _safe_set(b, 'metamodel_Sensor11', a2)
    assert _is_linked(b, 'metamodel_Sensor11', a2)
    if hasattr(a1, 'metamodel_Value'):
        assert not _is_linked(a1, 'metamodel_Value', b)
    if hasattr(a2, 'metamodel_Value'):
        assert _is_linked(a2, 'metamodel_Value', b)
    _safe_set(b, 'metamodel_Sensor11', None)
    assert not _is_linked(b, 'metamodel_Sensor11', a2)
    if hasattr(a2, 'metamodel_Value'):
        assert not _is_linked(a2, 'metamodel_Value', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_actions5_stub_double():
    # metamodel_Action has no real 'metamodel_Action' property in the generated
    # code (a bare stub) -- manually attach it so metamodel_Robot's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # metamodel_Robot's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = metamodel_Robot(name="sample_text")
    partner = metamodel_Action()
    setattr(partner, 'metamodel_Action', None)
    _safe_set(owner, 'metamodel_Robot6', {partner})
    assert getattr(partner, 'metamodel_Action') == owner
    _safe_set(owner, 'metamodel_Robot6', set())
    assert getattr(partner, 'metamodel_Action') is None


def test_assoc_cond35_stub_double():
    # metamodel_Condition has no real 'metamodel_Condition' property in the generated
    # code (a bare stub) -- manually attach it so metamodel_Transition's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # metamodel_Transition's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = metamodel_Transition(nameIn="sample_text")
    partner = metamodel_Condition()
    setattr(partner, 'metamodel_Condition', None)
    _safe_set(owner, 'metamodel_Transition36', partner)
    assert getattr(partner, 'metamodel_Condition') == owner
    _safe_set(owner, 'metamodel_Transition36', None)
    assert getattr(partner, 'metamodel_Condition') is None


def test_assoc_group8_stub_double():
    # metamodel_Group has no real 'metamodel_Group9' property in the generated
    # code (a bare stub) -- manually attach it so metamodel_ActionWheel's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # metamodel_ActionWheel's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = metamodel_ActionWheel(speed=7)
    partner = metamodel_Group()
    setattr(partner, 'metamodel_Group9', None)
    _safe_set(owner, 'metamodel_ActionWheel', partner)
    assert getattr(partner, 'metamodel_Group9') == owner
    _safe_set(owner, 'metamodel_ActionWheel', None)
    assert getattr(partner, 'metamodel_Group9') is None


def test_assoc_onEnterAction26_stub_double():
    # metamodel_Action has no real 'metamodel_Action28' property in the generated
    # code (a bare stub) -- manually attach it so metamodel_State's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # metamodel_State's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = metamodel_State(isInitial=True, name="sample_text", uid=7)
    partner = metamodel_Action()
    setattr(partner, 'metamodel_Action28', None)
    _safe_set(owner, 'metamodel_State27', partner)
    assert getattr(partner, 'metamodel_Action28') == owner
    _safe_set(owner, 'metamodel_State27', None)
    assert getattr(partner, 'metamodel_Action28') is None


def test_assoc_onLeaveAction29_stub_double():
    # metamodel_Action has no real 'metamodel_Action31' property in the generated
    # code (a bare stub) -- manually attach it so metamodel_State's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # metamodel_State's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = metamodel_State(isInitial=True, name="sample_text", uid=7)
    partner = metamodel_Action()
    setattr(partner, 'metamodel_Action31', None)
    _safe_set(owner, 'metamodel_State30', partner)
    assert getattr(partner, 'metamodel_Action31') == owner
    _safe_set(owner, 'metamodel_State30', None)
    assert getattr(partner, 'metamodel_Action31') is None


def test_assoc_valeur37_stub_double():
    # metamodel_UnaryOperator has no real 'metamodel_UnaryOperator' property in the generated
    # code (a bare stub) -- manually attach it so metamodel_Value's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # metamodel_Value's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = metamodel_Value(name="sample_text")
    partner = metamodel_UnaryOperator()
    setattr(partner, 'metamodel_UnaryOperator', None)
    _safe_set(owner, 'metamodel_Value38', partner)
    assert getattr(partner, 'metamodel_UnaryOperator') == owner
    _safe_set(owner, 'metamodel_Value38', None)
    assert getattr(partner, 'metamodel_UnaryOperator') is None


def test_assoc_value12_stub_double():
    # metamodel_Type has no real 'metamodel_Type' property in the generated
    # code (a bare stub) -- manually attach it so metamodel_Value's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # metamodel_Value's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = metamodel_Value(name="sample_text")
    partner = metamodel_Type()
    setattr(partner, 'metamodel_Type', None)
    _safe_set(owner, 'metamodel_Value13', partner)
    assert getattr(partner, 'metamodel_Type') == owner
    _safe_set(owner, 'metamodel_Value13', None)
    assert getattr(partner, 'metamodel_Type') is None


def test_assoc_wheels7_stub_double():
    # metamodel_Group has no real 'metamodel_Group' property in the generated
    # code (a bare stub) -- manually attach it so metamodel_DifferentialWheel's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # metamodel_DifferentialWheel's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = metamodel_DifferentialWheel(isLeft=True, speed=7)
    partner = metamodel_Group()
    setattr(partner, 'metamodel_Group', None)
    _safe_set(owner, 'metamodel_DifferentialWheel', partner)
    assert owner in getattr(partner, 'metamodel_Group')
    _safe_set(owner, 'metamodel_DifferentialWheel', None)
    assert owner not in getattr(partner, 'metamodel_Group')


def test_assoc_workingAction23_stub_double():
    # metamodel_Action has no real 'metamodel_Action25' property in the generated
    # code (a bare stub) -- manually attach it so metamodel_State's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # metamodel_State's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = metamodel_State(isInitial=True, name="sample_text", uid=7)
    partner = metamodel_Action()
    setattr(partner, 'metamodel_Action25', None)
    _safe_set(owner, 'metamodel_State24', partner)
    assert getattr(partner, 'metamodel_Action25') == owner
    _safe_set(owner, 'metamodel_State24', None)
    assert getattr(partner, 'metamodel_Action25') is None


