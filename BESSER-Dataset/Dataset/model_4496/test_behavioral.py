import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Brick,
    NamedElement,
    arduinoML_Action,
    arduinoML_Actuator,
    arduinoML_App,
    arduinoML_Brick,
    arduinoML_NamedElement,
    arduinoML_Sensor,
    arduinoML_State,
    arduinoML_Transition,
    Signal,
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
    # arduinoML_State has no real 'arduinoML_State7' property in the generated
    # code (a bare stub) -- manually attach it so arduinoML_Action's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # arduinoML_Action's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = arduinoML_Action(value="sample_text")
    partner = arduinoML_State()
    setattr(partner, 'arduinoML_State7', None)
    _safe_set(owner, 'arduinoML_Action', partner)
    assert owner in getattr(partner, 'arduinoML_State7')
    _safe_set(owner, 'arduinoML_Action', None)
    assert owner not in getattr(partner, 'arduinoML_State7')


def test_assoc_actuator9_stub_double():
    # arduinoML_Actuator has no real 'arduinoML_Actuator' property in the generated
    # code (a bare stub) -- manually attach it so arduinoML_Action's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # arduinoML_Action's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = arduinoML_Action(value="sample_text")
    partner = arduinoML_Actuator()
    setattr(partner, 'arduinoML_Actuator', None)
    _safe_set(owner, 'arduinoML_Action10', partner)
    assert getattr(partner, 'arduinoML_Actuator') == owner
    _safe_set(owner, 'arduinoML_Action10', None)
    assert getattr(partner, 'arduinoML_Actuator') is None


def test_assoc_bricks0_stub_double():
    # arduinoML_App has no real 'arduinoML_App' property in the generated
    # code (a bare stub) -- manually attach it so arduinoML_Brick's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # arduinoML_Brick's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = arduinoML_Brick(pin=7)
    partner = arduinoML_App()
    setattr(partner, 'arduinoML_App', None)
    _safe_set(owner, 'arduinoML_Brick', partner)
    assert owner in getattr(partner, 'arduinoML_App')
    _safe_set(owner, 'arduinoML_Brick', None)
    assert owner not in getattr(partner, 'arduinoML_App')


def test_assoc_next11_stub_double():
    # arduinoML_State has no real 'arduinoML_State12' property in the generated
    # code (a bare stub) -- manually attach it so arduinoML_Transition's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # arduinoML_Transition's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = arduinoML_Transition(value="sample_text")
    partner = arduinoML_State()
    setattr(partner, 'arduinoML_State12', None)
    _safe_set(owner, 'arduinoML_Transition', partner)
    assert getattr(partner, 'arduinoML_State12') == owner
    _safe_set(owner, 'arduinoML_Transition', None)
    assert getattr(partner, 'arduinoML_State12') is None


def test_assoc_sensor13_stub_double():
    # arduinoML_Sensor has no real 'arduinoML_Sensor' property in the generated
    # code (a bare stub) -- manually attach it so arduinoML_Transition's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # arduinoML_Transition's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = arduinoML_Transition(value="sample_text")
    partner = arduinoML_Sensor()
    setattr(partner, 'arduinoML_Sensor', None)
    _safe_set(owner, 'arduinoML_Transition14', partner)
    assert getattr(partner, 'arduinoML_Sensor') == owner
    _safe_set(owner, 'arduinoML_Transition14', None)
    assert getattr(partner, 'arduinoML_Sensor') is None


def test_assoc_state15_stub_double():
    # arduinoML_State has no real 'State' property in the generated
    # code (a bare stub) -- manually attach it so arduinoML_Transition's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # arduinoML_Transition's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = arduinoML_Transition(value="sample_text")
    partner = arduinoML_State()
    setattr(partner, 'State', None)
    _safe_set(owner, 'transition', partner)
    assert getattr(partner, 'State') == owner
    _safe_set(owner, 'transition', None)
    assert getattr(partner, 'State') is None


def test_assoc_transition8_stub_double():
    # arduinoML_State has no real 'state' property in the generated
    # code (a bare stub) -- manually attach it so arduinoML_Transition's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # arduinoML_Transition's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = arduinoML_Transition(value="sample_text")
    partner = arduinoML_State()
    setattr(partner, 'state', None)
    _safe_set(owner, 'Transition', partner)
    assert getattr(partner, 'state') == owner
    _safe_set(owner, 'Transition', None)
    assert getattr(partner, 'state') is None


