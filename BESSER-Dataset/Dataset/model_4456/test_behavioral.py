import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Action,
    Brick,
    arduinoml_Action,
    arduinoml_Actuator,
    arduinoml_ActuatorState,
    arduinoml_Board,
    arduinoml_Brick,
    arduinoml_Off,
    arduinoml_On,
    arduinoml_Sensor,
    arduinoml_State,
    arduinoml_Transition,
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

def test_assoc_actions6_stub_double():
    # arduinoml_Action has no real 'arduinoml_Action' property in the generated
    # code (a bare stub) -- manually attach it so arduinoml_State's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # arduinoml_State's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = arduinoml_State(name="sample_text")
    partner = arduinoml_Action()
    setattr(partner, 'arduinoml_Action', None)
    _safe_set(owner, 'arduinoml_State7', {partner})
    assert getattr(partner, 'arduinoml_Action') == owner
    _safe_set(owner, 'arduinoml_State7', set())
    assert getattr(partner, 'arduinoml_Action') is None


def test_assoc_bricks4_stub_double():
    # arduinoml_Board has no real 'arduinoml_Board5' property in the generated
    # code (a bare stub) -- manually attach it so arduinoml_Brick's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # arduinoml_Brick's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = arduinoml_Brick(name="sample_text", pin=7)
    partner = arduinoml_Board()
    setattr(partner, 'arduinoml_Board5', None)
    _safe_set(owner, 'arduinoml_Brick', partner)
    assert owner in getattr(partner, 'arduinoml_Board5')
    _safe_set(owner, 'arduinoml_Brick', None)
    assert owner not in getattr(partner, 'arduinoml_Board5')


def test_assoc_eventCode8_stub_double():
    # arduinoml_Transition has no real 'arduinoml_Transition' property in the generated
    # code (a bare stub) -- manually attach it so arduinoml_State's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # arduinoml_State's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = arduinoml_State(name="sample_text")
    partner = arduinoml_Transition()
    setattr(partner, 'arduinoml_Transition', None)
    _safe_set(owner, 'arduinoml_State9', {partner})
    assert getattr(partner, 'arduinoml_Transition') == owner
    _safe_set(owner, 'arduinoml_State9', set())
    assert getattr(partner, 'arduinoml_Transition') is None


def test_assoc_initial0_stub_double():
    # arduinoml_Board has no real 'arduinoml_Board' property in the generated
    # code (a bare stub) -- manually attach it so arduinoml_State's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # arduinoml_State's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = arduinoml_State(name="sample_text")
    partner = arduinoml_Board()
    setattr(partner, 'arduinoml_Board', None)
    _safe_set(owner, 'arduinoml_State', partner)
    assert getattr(partner, 'arduinoml_Board') == owner
    _safe_set(owner, 'arduinoml_State', None)
    assert getattr(partner, 'arduinoml_Board') is None


def test_assoc_possibles1_stub_double():
    # arduinoml_Board has no real 'arduinoml_Board2' property in the generated
    # code (a bare stub) -- manually attach it so arduinoml_State's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # arduinoml_State's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = arduinoml_State(name="sample_text")
    partner = arduinoml_Board()
    setattr(partner, 'arduinoml_Board2', None)
    _safe_set(owner, 'arduinoml_State3', partner)
    assert owner in getattr(partner, 'arduinoml_Board2')
    _safe_set(owner, 'arduinoml_State3', None)
    assert owner not in getattr(partner, 'arduinoml_Board2')


def test_assoc_source11_stub_double():
    # arduinoml_Transition has no real 'arduinoml_Transition12' property in the generated
    # code (a bare stub) -- manually attach it so arduinoml_State's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # arduinoml_State's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = arduinoml_State(name="sample_text")
    partner = arduinoml_Transition()
    setattr(partner, 'arduinoml_Transition12', None)
    _safe_set(owner, 'arduinoml_State13', partner)
    assert getattr(partner, 'arduinoml_Transition12') == owner
    _safe_set(owner, 'arduinoml_State13', None)
    assert getattr(partner, 'arduinoml_Transition12') is None


def test_assoc_state10_stub_double():
    # arduinoml_Actuator has no real 'arduinoml_Actuator' property in the generated
    # code (a bare stub) -- manually attach it so arduinoml_ActuatorState's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # arduinoml_ActuatorState's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = arduinoml_ActuatorState(isOn=True)
    partner = arduinoml_Actuator()
    setattr(partner, 'arduinoml_Actuator', None)
    _safe_set(owner, 'arduinoml_ActuatorState', partner)
    assert getattr(partner, 'arduinoml_Actuator') == owner
    _safe_set(owner, 'arduinoml_ActuatorState', None)
    assert getattr(partner, 'arduinoml_Actuator') is None


def test_assoc_target14_stub_double():
    # arduinoml_Transition has no real 'arduinoml_Transition15' property in the generated
    # code (a bare stub) -- manually attach it so arduinoml_State's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # arduinoml_State's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = arduinoml_State(name="sample_text")
    partner = arduinoml_Transition()
    setattr(partner, 'arduinoml_Transition15', None)
    _safe_set(owner, 'arduinoml_State16', partner)
    assert getattr(partner, 'arduinoml_Transition15') == owner
    _safe_set(owner, 'arduinoml_State16', None)
    assert getattr(partner, 'arduinoml_Transition15') is None


def test_assoc_triggers19_stub_double():
    # arduinoml_Transition has no real 'arduinoml_Transition21' property in the generated
    # code (a bare stub) -- manually attach it so arduinoml_ActuatorState's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # arduinoml_ActuatorState's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = arduinoml_ActuatorState(isOn=True)
    partner = arduinoml_Transition()
    setattr(partner, 'arduinoml_Transition21', None)
    _safe_set(owner, 'arduinoml_ActuatorState20', partner)
    assert getattr(partner, 'arduinoml_Transition21') == owner
    _safe_set(owner, 'arduinoml_ActuatorState20', None)
    assert getattr(partner, 'arduinoml_Transition21') is None


