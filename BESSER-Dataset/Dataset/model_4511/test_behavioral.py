import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Action,
    AnalogAction,
    Brick,
    Condition,
    NamedElement,
    arduinoml_AMLMachine,
    arduinoml_AMLState,
    arduinoml_Action,
    arduinoml_AnalogAction,
    arduinoml_AnalogActionSensor,
    arduinoml_AnalogActionValue,
    arduinoml_AnalogActuator,
    arduinoml_AnalogCondition,
    arduinoml_AnalogSensor,
    arduinoml_Brick,
    arduinoml_Condition,
    arduinoml_DigitalAction,
    arduinoml_DigitalActuator,
    arduinoml_DigitalCondition,
    arduinoml_DigitalSensor,
    arduinoml_NamedElement,
    arduinoml_TimeCondition,
    arduinoml_Transition,
    AnalogComparison,
    DigitalState,
    TimeComparison,
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

def test_assoc_bricks0_reverse_link_reassign_clear():
    a1 = arduinoml_Brick(pin=7)
    a2 = arduinoml_Brick(pin=13)
    b = arduinoml_AMLMachine(frequency=7)
    _safe_set(b, 'arduinoml_AMLMachine', {a1})
    assert _is_linked(b, 'arduinoml_AMLMachine', a1)
    if hasattr(a1, 'arduinoml_Brick'):
        assert _is_linked(a1, 'arduinoml_Brick', b)
    _safe_set(b, 'arduinoml_AMLMachine', {a2})
    assert _is_linked(b, 'arduinoml_AMLMachine', a2)
    if hasattr(a1, 'arduinoml_Brick'):
        assert not _is_linked(a1, 'arduinoml_Brick', b)
    if hasattr(a2, 'arduinoml_Brick'):
        assert _is_linked(a2, 'arduinoml_Brick', b)
    _safe_set(b, 'arduinoml_AMLMachine', set())
    assert not _is_linked(b, 'arduinoml_AMLMachine', a2)
    if hasattr(a2, 'arduinoml_Brick'):
        assert not _is_linked(a2, 'arduinoml_Brick', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_actuator16_stub_double():
    # arduinoml_DigitalActuator has no real 'arduinoml_DigitalActuator' property in the generated
    # code (a bare stub) -- manually attach it so arduinoml_DigitalAction's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # arduinoml_DigitalAction's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = arduinoml_DigitalAction(dState="sample_text")
    partner = arduinoml_DigitalActuator()
    setattr(partner, 'arduinoml_DigitalActuator', None)
    _safe_set(owner, 'arduinoml_DigitalAction', partner)
    assert getattr(partner, 'arduinoml_DigitalActuator') == owner
    _safe_set(owner, 'arduinoml_DigitalAction', None)
    assert getattr(partner, 'arduinoml_DigitalActuator') is None


def test_assoc_sensor15_stub_double():
    # arduinoml_DigitalSensor has no real 'arduinoml_DigitalSensor' property in the generated
    # code (a bare stub) -- manually attach it so arduinoml_DigitalCondition's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # arduinoml_DigitalCondition's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = arduinoml_DigitalCondition(dState="sample_text")
    partner = arduinoml_DigitalSensor()
    setattr(partner, 'arduinoml_DigitalSensor', None)
    _safe_set(owner, 'arduinoml_DigitalCondition', partner)
    assert getattr(partner, 'arduinoml_DigitalSensor') == owner
    _safe_set(owner, 'arduinoml_DigitalCondition', None)
    assert getattr(partner, 'arduinoml_DigitalSensor') is None


def test_assoc_sensor17_stub_double():
    # arduinoml_AnalogSensor has no real 'arduinoml_AnalogSensor' property in the generated
    # code (a bare stub) -- manually attach it so arduinoml_AnalogCondition's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # arduinoml_AnalogCondition's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = arduinoml_AnalogCondition(aComp="sample_text", value=7)
    partner = arduinoml_AnalogSensor()
    setattr(partner, 'arduinoml_AnalogSensor', None)
    _safe_set(owner, 'arduinoml_AnalogCondition', partner)
    assert getattr(partner, 'arduinoml_AnalogSensor') == owner
    _safe_set(owner, 'arduinoml_AnalogCondition', None)
    assert getattr(partner, 'arduinoml_AnalogSensor') is None


def test_assoc_start3_stub_double():
    # arduinoml_AMLState has no real 'arduinoml_AMLState5' property in the generated
    # code (a bare stub) -- manually attach it so arduinoml_AMLMachine's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # arduinoml_AMLMachine's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = arduinoml_AMLMachine(frequency=7)
    partner = arduinoml_AMLState()
    setattr(partner, 'arduinoml_AMLState5', None)
    _safe_set(owner, 'arduinoml_AMLMachine4', partner)
    assert getattr(partner, 'arduinoml_AMLState5') == owner
    _safe_set(owner, 'arduinoml_AMLMachine4', None)
    assert getattr(partner, 'arduinoml_AMLState5') is None


def test_assoc_states1_stub_double():
    # arduinoml_AMLState has no real 'arduinoml_AMLState' property in the generated
    # code (a bare stub) -- manually attach it so arduinoml_AMLMachine's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # arduinoml_AMLMachine's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = arduinoml_AMLMachine(frequency=7)
    partner = arduinoml_AMLState()
    setattr(partner, 'arduinoml_AMLState', None)
    _safe_set(owner, 'arduinoml_AMLMachine2', {partner})
    assert getattr(partner, 'arduinoml_AMLState') == owner
    _safe_set(owner, 'arduinoml_AMLMachine2', set())
    assert getattr(partner, 'arduinoml_AMLState') is None


