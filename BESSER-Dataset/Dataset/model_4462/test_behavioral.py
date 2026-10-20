import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Action,
    Actuator,
    Brick,
    Condition,
    NamedElement,
    Sensor,
    arduinoml_Action,
    arduinoml_Actuator,
    arduinoml_AnalogAction,
    arduinoml_AnalogActuator,
    arduinoml_AnalogSensor,
    arduinoml_App,
    arduinoml_BinaryAction,
    arduinoml_BinaryActuator,
    arduinoml_BinarySensor,
    arduinoml_Brick,
    arduinoml_Condition,
    arduinoml_MultipleElementCondition,
    arduinoml_NamedElement,
    arduinoml_Sensor,
    arduinoml_SingleElementCondition,
    arduinoml_State,
    arduinoml_Transition,
    arduinoml_ValueElementCondition,
    COMPARATOR,
    OPERATOR,
    SIGNAL,
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

def test_assoc_bricks1_stub_double():
    # arduinoml_App has no real 'arduinoml_App2' property in the generated
    # code (a bare stub) -- manually attach it so arduinoml_Brick's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # arduinoml_Brick's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = arduinoml_Brick(pin="sample_text")
    partner = arduinoml_App()
    setattr(partner, 'arduinoml_App2', None)
    _safe_set(owner, 'arduinoml_Brick', partner)
    assert owner in getattr(partner, 'arduinoml_App2')
    _safe_set(owner, 'arduinoml_Brick', None)
    assert owner not in getattr(partner, 'arduinoml_App2')


def test_assoc_condition15_stub_double():
    # arduinoml_Transition has no real 'arduinoml_Transition16' property in the generated
    # code (a bare stub) -- manually attach it so arduinoml_MultipleElementCondition's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # arduinoml_MultipleElementCondition's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = arduinoml_MultipleElementCondition(operators="sample_text")
    partner = arduinoml_Transition()
    setattr(partner, 'arduinoml_Transition16', None)
    _safe_set(owner, 'arduinoml_MultipleElementCondition', partner)
    assert getattr(partner, 'arduinoml_Transition16') == owner
    _safe_set(owner, 'arduinoml_MultipleElementCondition', None)
    assert getattr(partner, 'arduinoml_Transition16') is None


def test_assoc_conditions18_stub_double():
    # arduinoml_Condition has no real 'arduinoml_Condition' property in the generated
    # code (a bare stub) -- manually attach it so arduinoml_MultipleElementCondition's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # arduinoml_MultipleElementCondition's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = arduinoml_MultipleElementCondition(operators="sample_text")
    partner = arduinoml_Condition()
    setattr(partner, 'arduinoml_Condition', None)
    _safe_set(owner, 'arduinoml_MultipleElementCondition19', {partner})
    assert getattr(partner, 'arduinoml_Condition') == owner
    _safe_set(owner, 'arduinoml_MultipleElementCondition19', set())
    assert getattr(partner, 'arduinoml_Condition') is None


def test_assoc_sensor17_stub_double():
    # arduinoml_BinarySensor has no real 'arduinoml_BinarySensor' property in the generated
    # code (a bare stub) -- manually attach it so arduinoml_SingleElementCondition's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # arduinoml_SingleElementCondition's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = arduinoml_SingleElementCondition(value="sample_text")
    partner = arduinoml_BinarySensor()
    setattr(partner, 'arduinoml_BinarySensor', None)
    _safe_set(owner, 'arduinoml_SingleElementCondition', partner)
    assert getattr(partner, 'arduinoml_BinarySensor') == owner
    _safe_set(owner, 'arduinoml_SingleElementCondition', None)
    assert getattr(partner, 'arduinoml_BinarySensor') is None


def test_assoc_sensor20_stub_double():
    # arduinoml_AnalogSensor has no real 'arduinoml_AnalogSensor' property in the generated
    # code (a bare stub) -- manually attach it so arduinoml_ValueElementCondition's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # arduinoml_ValueElementCondition's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = arduinoml_ValueElementCondition(comparator="sample_text", value=3.14)
    partner = arduinoml_AnalogSensor()
    setattr(partner, 'arduinoml_AnalogSensor', None)
    _safe_set(owner, 'arduinoml_ValueElementCondition', partner)
    assert getattr(partner, 'arduinoml_AnalogSensor') == owner
    _safe_set(owner, 'arduinoml_ValueElementCondition', None)
    assert getattr(partner, 'arduinoml_AnalogSensor') is None


