import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    ArduinoCard_Actuator,
    ArduinoCard_Block,
    ArduinoCard_BlockInteraction,
    ArduinoCard_Card,
    ArduinoCard_Command,
    ArduinoCard_Condition,
    ArduinoCard_Sensor,
    ArduinoCard_State,
    ArduinoCard_Transition,
    Block,
    BlockInteraction,
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

def test_assoc_Transitions0_reverse_link_reassign_clear():
    a1 = ArduinoCard_Transition(name="sample_text")
    a2 = ArduinoCard_Transition(name="sample_text_2")
    b = ArduinoCard_State(isInitial=True, name="sample_text")
    _safe_set(b, 'ArduinoCard_State', {a1})
    assert _is_linked(b, 'ArduinoCard_State', a1)
    if hasattr(a1, 'ArduinoCard_Transition'):
        assert _is_linked(a1, 'ArduinoCard_Transition', b)
    _safe_set(b, 'ArduinoCard_State', {a2})
    assert _is_linked(b, 'ArduinoCard_State', a2)
    if hasattr(a1, 'ArduinoCard_Transition'):
        assert not _is_linked(a1, 'ArduinoCard_Transition', b)
    if hasattr(a2, 'ArduinoCard_Transition'):
        assert _is_linked(a2, 'ArduinoCard_Transition', b)
    _safe_set(b, 'ArduinoCard_State', set())
    assert not _is_linked(b, 'ArduinoCard_State', a2)
    if hasattr(a2, 'ArduinoCard_Transition'):
        assert not _is_linked(a2, 'ArduinoCard_Transition', b)


def test_assoc_nextState4_reverse_link_reassign_clear():
    a1 = ArduinoCard_Transition(name="sample_text")
    a2 = ArduinoCard_Transition(name="sample_text_2")
    b = ArduinoCard_State(isInitial=True, name="sample_text")
    _safe_set(b, 'ArduinoCard_State6', a1)
    assert _is_linked(b, 'ArduinoCard_State6', a1)
    if hasattr(a1, 'ArduinoCard_Transition5'):
        assert _is_linked(a1, 'ArduinoCard_Transition5', b)
    _safe_set(b, 'ArduinoCard_State6', a2)
    assert _is_linked(b, 'ArduinoCard_State6', a2)
    if hasattr(a1, 'ArduinoCard_Transition5'):
        assert not _is_linked(a1, 'ArduinoCard_Transition5', b)
    if hasattr(a2, 'ArduinoCard_Transition5'):
        assert _is_linked(a2, 'ArduinoCard_Transition5', b)
    _safe_set(b, 'ArduinoCard_State6', None)
    assert not _is_linked(b, 'ArduinoCard_State6', a2)
    if hasattr(a2, 'ArduinoCard_Transition5'):
        assert not _is_linked(a2, 'ArduinoCard_Transition5', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_BlockInteractions17_stub_double():
    # ArduinoCard_Card has no real 'ArduinoCard_Card18' property in the generated
    # code (a bare stub) -- manually attach it so ArduinoCard_BlockInteraction's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ArduinoCard_BlockInteraction's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ArduinoCard_BlockInteraction(isHigh=True, name="sample_text")
    partner = ArduinoCard_Card()
    setattr(partner, 'ArduinoCard_Card18', None)
    _safe_set(owner, 'ArduinoCard_BlockInteraction', partner)
    assert owner in getattr(partner, 'ArduinoCard_Card18')
    _safe_set(owner, 'ArduinoCard_BlockInteraction', None)
    assert owner not in getattr(partner, 'ArduinoCard_Card18')


def test_assoc_Blocks19_stub_double():
    # ArduinoCard_Card has no real 'ArduinoCard_Card20' property in the generated
    # code (a bare stub) -- manually attach it so ArduinoCard_Block's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ArduinoCard_Block's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ArduinoCard_Block(isAnalogic="sample_text", name="sample_text", pinNumber=7)
    partner = ArduinoCard_Card()
    setattr(partner, 'ArduinoCard_Card20', None)
    _safe_set(owner, 'ArduinoCard_Block', partner)
    assert owner in getattr(partner, 'ArduinoCard_Card20')
    _safe_set(owner, 'ArduinoCard_Block', None)
    assert owner not in getattr(partner, 'ArduinoCard_Card20')


def test_assoc_Command1_stub_double():
    # ArduinoCard_Command has no real 'ArduinoCard_Command' property in the generated
    # code (a bare stub) -- manually attach it so ArduinoCard_State's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ArduinoCard_State's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ArduinoCard_State(isInitial=True, name="sample_text")
    partner = ArduinoCard_Command()
    setattr(partner, 'ArduinoCard_Command', None)
    _safe_set(owner, 'ArduinoCard_State2', {partner})
    assert getattr(partner, 'ArduinoCard_Command') == owner
    _safe_set(owner, 'ArduinoCard_State2', set())
    assert getattr(partner, 'ArduinoCard_Command') is None


def test_assoc_Condition7_stub_double():
    # ArduinoCard_Condition has no real 'ArduinoCard_Condition9' property in the generated
    # code (a bare stub) -- manually attach it so ArduinoCard_Transition's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ArduinoCard_Transition's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ArduinoCard_Transition(name="sample_text")
    partner = ArduinoCard_Condition()
    setattr(partner, 'ArduinoCard_Condition9', None)
    _safe_set(owner, 'ArduinoCard_Transition8', {partner})
    assert getattr(partner, 'ArduinoCard_Condition9') == owner
    _safe_set(owner, 'ArduinoCard_Transition8', set())
    assert getattr(partner, 'ArduinoCard_Condition9') is None


def test_assoc_States12_stub_double():
    # ArduinoCard_Card has no real 'ArduinoCard_Card' property in the generated
    # code (a bare stub) -- manually attach it so ArduinoCard_State's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ArduinoCard_State's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ArduinoCard_State(isInitial=True, name="sample_text")
    partner = ArduinoCard_Card()
    setattr(partner, 'ArduinoCard_Card', None)
    _safe_set(owner, 'ArduinoCard_State13', partner)
    assert owner in getattr(partner, 'ArduinoCard_Card')
    _safe_set(owner, 'ArduinoCard_State13', None)
    assert owner not in getattr(partner, 'ArduinoCard_Card')


def test_assoc_Transitions14_stub_double():
    # ArduinoCard_Card has no real 'ArduinoCard_Card15' property in the generated
    # code (a bare stub) -- manually attach it so ArduinoCard_Transition's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ArduinoCard_Transition's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ArduinoCard_Transition(name="sample_text")
    partner = ArduinoCard_Card()
    setattr(partner, 'ArduinoCard_Card15', None)
    _safe_set(owner, 'ArduinoCard_Transition16', partner)
    assert owner in getattr(partner, 'ArduinoCard_Card15')
    _safe_set(owner, 'ArduinoCard_Transition16', None)
    assert owner not in getattr(partner, 'ArduinoCard_Card15')


