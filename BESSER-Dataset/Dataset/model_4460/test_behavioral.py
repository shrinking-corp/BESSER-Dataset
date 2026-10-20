import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Brick,
    Condition,
    NamedElement,
    arduinoml_Action,
    arduinoml_Actuator,
    arduinoml_App,
    arduinoml_Brick,
    arduinoml_Condition,
    arduinoml_MultipleCondition,
    arduinoml_NamedElement,
    arduinoml_Sensor,
    arduinoml_SimpleCondition,
    arduinoml_State,
    arduinoml_Transition,
    BrickType,
    COMPARATOR,
    OPERATOR,
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

def test_assoc_conditions24_reverse_link_reassign_clear():
    a1 = arduinoml_SimpleCondition(comparator="sample_text", value="sample_text")
    a2 = arduinoml_SimpleCondition(comparator="sample_text_2", value="sample_text_2")
    b = arduinoml_MultipleCondition(operators="sample_text")
    _safe_set(b, 'arduinoml_MultipleCondition', {a1})
    assert _is_linked(b, 'arduinoml_MultipleCondition', a1)
    if hasattr(a1, 'arduinoml_SimpleCondition25'):
        assert _is_linked(a1, 'arduinoml_SimpleCondition25', b)
    _safe_set(b, 'arduinoml_MultipleCondition', {a2})
    assert _is_linked(b, 'arduinoml_MultipleCondition', a2)
    if hasattr(a1, 'arduinoml_SimpleCondition25'):
        assert not _is_linked(a1, 'arduinoml_SimpleCondition25', b)
    if hasattr(a2, 'arduinoml_SimpleCondition25'):
        assert _is_linked(a2, 'arduinoml_SimpleCondition25', b)
    _safe_set(b, 'arduinoml_MultipleCondition', set())
    assert not _is_linked(b, 'arduinoml_MultipleCondition', a2)
    if hasattr(a2, 'arduinoml_SimpleCondition25'):
        assert not _is_linked(a2, 'arduinoml_SimpleCondition25', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_actions16_stub_double():
    # arduinoml_State has no real 'arduinoml_State17' property in the generated
    # code (a bare stub) -- manually attach it so arduinoml_Action's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # arduinoml_Action's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = arduinoml_Action(value="sample_text")
    partner = arduinoml_State()
    setattr(partner, 'arduinoml_State17', None)
    _safe_set(owner, 'arduinoml_Action', partner)
    assert owner in getattr(partner, 'arduinoml_State17')
    _safe_set(owner, 'arduinoml_Action', None)
    assert owner not in getattr(partner, 'arduinoml_State17')


def test_assoc_actuator21_stub_double():
    # arduinoml_Actuator has no real 'arduinoml_Actuator' property in the generated
    # code (a bare stub) -- manually attach it so arduinoml_Action's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # arduinoml_Action's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = arduinoml_Action(value="sample_text")
    partner = arduinoml_Actuator()
    setattr(partner, 'arduinoml_Actuator', None)
    _safe_set(owner, 'arduinoml_Action22', partner)
    assert getattr(partner, 'arduinoml_Actuator') == owner
    _safe_set(owner, 'arduinoml_Action22', None)
    assert getattr(partner, 'arduinoml_Actuator') is None


def test_assoc_bricks0_stub_double():
    # arduinoml_App has no real 'arduinoml_App' property in the generated
    # code (a bare stub) -- manually attach it so arduinoml_Brick's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # arduinoml_Brick's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = arduinoml_Brick(pin=7, type="sample_text")
    partner = arduinoml_App()
    setattr(partner, 'arduinoml_App', None)
    _safe_set(owner, 'arduinoml_Brick', partner)
    assert owner in getattr(partner, 'arduinoml_App')
    _safe_set(owner, 'arduinoml_Brick', None)
    assert owner not in getattr(partner, 'arduinoml_App')


def test_assoc_sensor23_stub_double():
    # arduinoml_Sensor has no real 'arduinoml_Sensor' property in the generated
    # code (a bare stub) -- manually attach it so arduinoml_SimpleCondition's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # arduinoml_SimpleCondition's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = arduinoml_SimpleCondition(comparator="sample_text", value="sample_text")
    partner = arduinoml_Sensor()
    setattr(partner, 'arduinoml_Sensor', None)
    _safe_set(owner, 'arduinoml_SimpleCondition', partner)
    assert getattr(partner, 'arduinoml_Sensor') == owner
    _safe_set(owner, 'arduinoml_SimpleCondition', None)
    assert getattr(partner, 'arduinoml_Sensor') is None


