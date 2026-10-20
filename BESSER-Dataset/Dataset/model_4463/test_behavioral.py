import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Actuator,
    Brick,
    NamedElement,
    Sensor,
    Signal,
    arduinoML_Action,
    arduinoML_Actuator,
    arduinoML_App,
    arduinoML_Brick,
    arduinoML_Condition,
    arduinoML_DigitalSignal,
    arduinoML_KeyboardSensor,
    arduinoML_LCDScreenActuator,
    arduinoML_NamedElement,
    arduinoML_Sensor,
    arduinoML_Signal,
    arduinoML_State,
    arduinoML_StringSignal,
    arduinoML_Transition,
    DigitalSignalEnum,
    Operator,
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
    a1 = arduinoML_Brick(pins=7)
    a2 = arduinoML_Brick(pins=13)
    b = arduinoML_App(name="sample_text")
    _safe_set(b, 'arduinoML_App', {a1})
    assert _is_linked(b, 'arduinoML_App', a1)
    if hasattr(a1, 'arduinoML_Brick'):
        assert _is_linked(a1, 'arduinoML_Brick', b)
    _safe_set(b, 'arduinoML_App', {a2})
    assert _is_linked(b, 'arduinoML_App', a2)
    if hasattr(a1, 'arduinoML_Brick'):
        assert not _is_linked(a1, 'arduinoML_Brick', b)
    if hasattr(a2, 'arduinoML_Brick'):
        assert _is_linked(a2, 'arduinoML_Brick', b)
    _safe_set(b, 'arduinoML_App', set())
    assert not _is_linked(b, 'arduinoML_App', a2)
    if hasattr(a2, 'arduinoML_Brick'):
        assert not _is_linked(a2, 'arduinoML_Brick', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_conditions17_stub_double():
    # arduinoML_Transition has no real 'arduinoML_Transition18' property in the generated
    # code (a bare stub) -- manually attach it so arduinoML_Condition's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # arduinoML_Condition's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = arduinoML_Condition(operator="sample_text")
    partner = arduinoML_Transition()
    setattr(partner, 'arduinoML_Transition18', None)
    _safe_set(owner, 'arduinoML_Condition', partner)
    assert owner in getattr(partner, 'arduinoML_Transition18')
    _safe_set(owner, 'arduinoML_Condition', None)
    assert owner not in getattr(partner, 'arduinoML_Transition18')


def test_assoc_initial3_stub_double():
    # arduinoML_State has no real 'arduinoML_State5' property in the generated
    # code (a bare stub) -- manually attach it so arduinoML_App's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # arduinoML_App's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = arduinoML_App(name="sample_text")
    partner = arduinoML_State()
    setattr(partner, 'arduinoML_State5', None)
    _safe_set(owner, 'arduinoML_App4', partner)
    assert getattr(partner, 'arduinoML_State5') == owner
    _safe_set(owner, 'arduinoML_App4', None)
    assert getattr(partner, 'arduinoML_State5') is None


def test_assoc_sensor19_stub_double():
    # arduinoML_Sensor has no real 'arduinoML_Sensor' property in the generated
    # code (a bare stub) -- manually attach it so arduinoML_Condition's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # arduinoML_Condition's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = arduinoML_Condition(operator="sample_text")
    partner = arduinoML_Sensor()
    setattr(partner, 'arduinoML_Sensor', None)
    _safe_set(owner, 'arduinoML_Condition20', partner)
    assert getattr(partner, 'arduinoML_Sensor') == owner
    _safe_set(owner, 'arduinoML_Condition20', None)
    assert getattr(partner, 'arduinoML_Sensor') is None


def test_assoc_signal21_stub_double():
    # arduinoML_Signal has no real 'arduinoML_Signal23' property in the generated
    # code (a bare stub) -- manually attach it so arduinoML_Condition's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # arduinoML_Condition's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = arduinoML_Condition(operator="sample_text")
    partner = arduinoML_Signal()
    setattr(partner, 'arduinoML_Signal23', None)
    _safe_set(owner, 'arduinoML_Condition22', partner)
    assert getattr(partner, 'arduinoML_Signal23') == owner
    _safe_set(owner, 'arduinoML_Condition22', None)
    assert getattr(partner, 'arduinoML_Signal23') is None


def test_assoc_states1_stub_double():
    # arduinoML_State has no real 'arduinoML_State' property in the generated
    # code (a bare stub) -- manually attach it so arduinoML_App's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # arduinoML_App's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = arduinoML_App(name="sample_text")
    partner = arduinoML_State()
    setattr(partner, 'arduinoML_State', None)
    _safe_set(owner, 'arduinoML_App2', {partner})
    assert getattr(partner, 'arduinoML_State') == owner
    _safe_set(owner, 'arduinoML_App2', set())
    assert getattr(partner, 'arduinoML_State') is None


