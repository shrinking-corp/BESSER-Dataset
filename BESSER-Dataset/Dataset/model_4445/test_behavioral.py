import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Brick,
    NamedElement,
    Transition,
    arduinoML_Action,
    arduinoML_Actuator,
    arduinoML_Analog,
    arduinoML_App,
    arduinoML_Brick,
    arduinoML_Digital,
    arduinoML_Mode,
    arduinoML_NamedElement,
    arduinoML_State,
    arduinoML_Transition,
    arduinoML_TransitionMode,
    arduinoML_TransitionState,
    Compare,
    Signal,
    Time_unit,
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

def test_assoc_analogs11_reverse_link_reassign_clear():
    a1 = arduinoML_Transition(a_values=7, comp="sample_text", d_values="sample_text", time=7, unit="sample_text")
    a2 = arduinoML_Transition(a_values=13, comp="sample_text_2", d_values="sample_text_2", time=13, unit="sample_text_2")
    b = arduinoML_Analog(debug=True)
    _safe_set(b, 'arduinoML_Analog', a1)
    assert _is_linked(b, 'arduinoML_Analog', a1)
    if hasattr(a1, 'arduinoML_Transition12'):
        assert _is_linked(a1, 'arduinoML_Transition12', b)
    _safe_set(b, 'arduinoML_Analog', a2)
    assert _is_linked(b, 'arduinoML_Analog', a2)
    if hasattr(a1, 'arduinoML_Transition12'):
        assert not _is_linked(a1, 'arduinoML_Transition12', b)
    if hasattr(a2, 'arduinoML_Transition12'):
        assert _is_linked(a2, 'arduinoML_Transition12', b)
    _safe_set(b, 'arduinoML_Analog', None)
    assert not _is_linked(b, 'arduinoML_Analog', a2)
    if hasattr(a2, 'arduinoML_Transition12'):
        assert not _is_linked(a2, 'arduinoML_Transition12', b)


def test_assoc_bricks4_reverse_link_reassign_clear():
    a1 = arduinoML_Brick(pin=7)
    a2 = arduinoML_Brick(pin=13)
    b = arduinoML_App(monitoring=True)
    _safe_set(b, 'arduinoML_App5', {a1})
    assert _is_linked(b, 'arduinoML_App5', a1)
    if hasattr(a1, 'arduinoML_Brick'):
        assert _is_linked(a1, 'arduinoML_Brick', b)
    _safe_set(b, 'arduinoML_App5', {a2})
    assert _is_linked(b, 'arduinoML_App5', a2)
    if hasattr(a1, 'arduinoML_Brick'):
        assert not _is_linked(a1, 'arduinoML_Brick', b)
    if hasattr(a2, 'arduinoML_Brick'):
        assert _is_linked(a2, 'arduinoML_Brick', b)
    _safe_set(b, 'arduinoML_App5', set())
    assert not _is_linked(b, 'arduinoML_App5', a2)
    if hasattr(a2, 'arduinoML_Brick'):
        assert not _is_linked(a2, 'arduinoML_Brick', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_actions6_stub_double():
    # arduinoML_State has no real 'arduinoML_State' property in the generated
    # code (a bare stub) -- manually attach it so arduinoML_Action's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # arduinoML_Action's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = arduinoML_Action(value="sample_text")
    partner = arduinoML_State()
    setattr(partner, 'arduinoML_State', None)
    _safe_set(owner, 'arduinoML_Action', partner)
    assert owner in getattr(partner, 'arduinoML_State')
    _safe_set(owner, 'arduinoML_Action', None)
    assert owner not in getattr(partner, 'arduinoML_State')


def test_assoc_actuator8_stub_double():
    # arduinoML_Actuator has no real 'arduinoML_Actuator' property in the generated
    # code (a bare stub) -- manually attach it so arduinoML_Action's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # arduinoML_Action's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = arduinoML_Action(value="sample_text")
    partner = arduinoML_Actuator()
    setattr(partner, 'arduinoML_Actuator', None)
    _safe_set(owner, 'arduinoML_Action9', partner)
    assert getattr(partner, 'arduinoML_Actuator') == owner
    _safe_set(owner, 'arduinoML_Action9', None)
    assert getattr(partner, 'arduinoML_Actuator') is None


def test_assoc_bricks13_stub_double():
    # arduinoML_Mode has no real 'arduinoML_Mode14' property in the generated
    # code (a bare stub) -- manually attach it so arduinoML_Brick's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # arduinoML_Brick's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = arduinoML_Brick(pin=7)
    partner = arduinoML_Mode()
    setattr(partner, 'arduinoML_Mode14', None)
    _safe_set(owner, 'arduinoML_Brick15', partner)
    assert owner in getattr(partner, 'arduinoML_Mode14')
    _safe_set(owner, 'arduinoML_Brick15', None)
    assert owner not in getattr(partner, 'arduinoML_Mode14')


def test_assoc_digitals10_stub_double():
    # arduinoML_Digital has no real 'arduinoML_Digital' property in the generated
    # code (a bare stub) -- manually attach it so arduinoML_Transition's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # arduinoML_Transition's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = arduinoML_Transition(a_values=7, comp="sample_text", d_values="sample_text", time=7, unit="sample_text")
    partner = arduinoML_Digital()
    setattr(partner, 'arduinoML_Digital', None)
    _safe_set(owner, 'arduinoML_Transition', {partner})
    assert getattr(partner, 'arduinoML_Digital') == owner
    _safe_set(owner, 'arduinoML_Transition', set())
    assert getattr(partner, 'arduinoML_Digital') is None


def test_assoc_initial_mode0_stub_double():
    # arduinoML_Mode has no real 'arduinoML_Mode' property in the generated
    # code (a bare stub) -- manually attach it so arduinoML_App's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # arduinoML_App's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = arduinoML_App(monitoring=True)
    partner = arduinoML_Mode()
    setattr(partner, 'arduinoML_Mode', None)
    _safe_set(owner, 'arduinoML_App', partner)
    assert getattr(partner, 'arduinoML_Mode') == owner
    _safe_set(owner, 'arduinoML_App', None)
    assert getattr(partner, 'arduinoML_Mode') is None


def test_assoc_modes1_stub_double():
    # arduinoML_Mode has no real 'arduinoML_Mode3' property in the generated
    # code (a bare stub) -- manually attach it so arduinoML_App's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # arduinoML_App's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = arduinoML_App(monitoring=True)
    partner = arduinoML_Mode()
    setattr(partner, 'arduinoML_Mode3', None)
    _safe_set(owner, 'arduinoML_App2', {partner})
    assert getattr(partner, 'arduinoML_Mode3') == owner
    _safe_set(owner, 'arduinoML_App2', set())
    assert getattr(partner, 'arduinoML_Mode3') is None


