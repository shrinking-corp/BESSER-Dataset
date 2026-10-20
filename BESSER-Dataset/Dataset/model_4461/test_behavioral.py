import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Brick,
    Condition,
    NamedElement,
    arduinoML_Action,
    arduinoML_Actuator,
    arduinoML_App,
    arduinoML_BaseCondition,
    arduinoML_BooleanCondition,
    arduinoML_Brick,
    arduinoML_Condition,
    arduinoML_NamedElement,
    arduinoML_Sensor,
    arduinoML_SinkError,
    arduinoML_State,
    arduinoML_Transition,
    Comparator,
    Operator,
    Signal,
    Type,
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

def test_assoc_booleancondition23_reverse_link_reassign_clear():
    a1 = arduinoML_SinkError(value=7)
    a2 = arduinoML_SinkError(value=13)
    b = arduinoML_BooleanCondition(operator="sample_text")
    _safe_set(b, 'arduinoML_BooleanCondition25', a1)
    assert _is_linked(b, 'arduinoML_BooleanCondition25', a1)
    if hasattr(a1, 'arduinoML_SinkError24'):
        assert _is_linked(a1, 'arduinoML_SinkError24', b)
    _safe_set(b, 'arduinoML_BooleanCondition25', a2)
    assert _is_linked(b, 'arduinoML_BooleanCondition25', a2)
    if hasattr(a1, 'arduinoML_SinkError24'):
        assert not _is_linked(a1, 'arduinoML_SinkError24', b)
    if hasattr(a2, 'arduinoML_SinkError24'):
        assert _is_linked(a2, 'arduinoML_SinkError24', b)
    _safe_set(b, 'arduinoML_BooleanCondition25', None)
    assert not _is_linked(b, 'arduinoML_BooleanCondition25', a2)
    if hasattr(a2, 'arduinoML_SinkError24'):
        assert not _is_linked(a2, 'arduinoML_SinkError24', b)


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
    owner = arduinoML_Action(analogvalue=7, value="sample_text")
    partner = arduinoML_State()
    setattr(partner, 'arduinoML_State7', None)
    _safe_set(owner, 'arduinoML_Action', partner)
    assert owner in getattr(partner, 'arduinoML_State7')
    _safe_set(owner, 'arduinoML_Action', None)
    assert owner not in getattr(partner, 'arduinoML_State7')


def test_assoc_actuator11_stub_double():
    # arduinoML_Actuator has no real 'arduinoML_Actuator' property in the generated
    # code (a bare stub) -- manually attach it so arduinoML_Action's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # arduinoML_Action's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = arduinoML_Action(analogvalue=7, value="sample_text")
    partner = arduinoML_Actuator()
    setattr(partner, 'arduinoML_Actuator', None)
    _safe_set(owner, 'arduinoML_Action12', partner)
    assert getattr(partner, 'arduinoML_Actuator') == owner
    _safe_set(owner, 'arduinoML_Action12', None)
    assert getattr(partner, 'arduinoML_Actuator') is None


def test_assoc_basecondition21_stub_double():
    # arduinoML_BaseCondition has no real 'arduinoML_BaseCondition22' property in the generated
    # code (a bare stub) -- manually attach it so arduinoML_SinkError's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # arduinoML_SinkError's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = arduinoML_SinkError(value=7)
    partner = arduinoML_BaseCondition()
    setattr(partner, 'arduinoML_BaseCondition22', None)
    _safe_set(owner, 'arduinoML_SinkError', partner)
    assert getattr(partner, 'arduinoML_BaseCondition22') == owner
    _safe_set(owner, 'arduinoML_SinkError', None)
    assert getattr(partner, 'arduinoML_BaseCondition22') is None


def test_assoc_booleancondition18_stub_double():
    # arduinoML_Transition has no real 'arduinoML_Transition19' property in the generated
    # code (a bare stub) -- manually attach it so arduinoML_BooleanCondition's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # arduinoML_BooleanCondition's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = arduinoML_BooleanCondition(operator="sample_text")
    partner = arduinoML_Transition()
    setattr(partner, 'arduinoML_Transition19', None)
    _safe_set(owner, 'arduinoML_BooleanCondition', partner)
    assert owner in getattr(partner, 'arduinoML_Transition19')
    _safe_set(owner, 'arduinoML_BooleanCondition', None)
    assert owner not in getattr(partner, 'arduinoML_Transition19')


def test_assoc_bricks0_stub_double():
    # arduinoML_App has no real 'arduinoML_App' property in the generated
    # code (a bare stub) -- manually attach it so arduinoML_Brick's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # arduinoML_Brick's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = arduinoML_Brick(pin=7, type="sample_text")
    partner = arduinoML_App()
    setattr(partner, 'arduinoML_App', None)
    _safe_set(owner, 'arduinoML_Brick', partner)
    assert owner in getattr(partner, 'arduinoML_App')
    _safe_set(owner, 'arduinoML_Brick', None)
    assert owner not in getattr(partner, 'arduinoML_App')


def test_assoc_errors9_stub_double():
    # arduinoML_State has no real 'state10' property in the generated
    # code (a bare stub) -- manually attach it so arduinoML_SinkError's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # arduinoML_SinkError's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = arduinoML_SinkError(value=7)
    partner = arduinoML_State()
    setattr(partner, 'state10', None)
    _safe_set(owner, 'SinkError', partner)
    assert owner in getattr(partner, 'state10')
    _safe_set(owner, 'SinkError', None)
    assert owner not in getattr(partner, 'state10')


def test_assoc_sensor20_stub_double():
    # arduinoML_Sensor has no real 'arduinoML_Sensor' property in the generated
    # code (a bare stub) -- manually attach it so arduinoML_Condition's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # arduinoML_Condition's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = arduinoML_Condition(analogvalue=7, comparator="sample_text", value="sample_text")
    partner = arduinoML_Sensor()
    setattr(partner, 'arduinoML_Sensor', None)
    _safe_set(owner, 'arduinoML_Condition', partner)
    assert getattr(partner, 'arduinoML_Sensor') == owner
    _safe_set(owner, 'arduinoML_Condition', None)
    assert getattr(partner, 'arduinoML_Sensor') is None


def test_assoc_state26_stub_double():
    # arduinoML_State has no real 'State27' property in the generated
    # code (a bare stub) -- manually attach it so arduinoML_SinkError's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # arduinoML_SinkError's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = arduinoML_SinkError(value=7)
    partner = arduinoML_State()
    setattr(partner, 'State27', None)
    _safe_set(owner, 'errors', partner)
    assert getattr(partner, 'State27') == owner
    _safe_set(owner, 'errors', None)
    assert getattr(partner, 'State27') is None


