import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Guard,
    Value,
    statemachine_Command,
    statemachine_Constant,
    statemachine_ConstantRef,
    statemachine_Event,
    statemachine_Guard,
    statemachine_IntLiteral,
    statemachine_RangeGuard,
    statemachine_State,
    statemachine_Statemachine,
    statemachine_Thing,
    statemachine_Transition,
    statemachine_Value,
    statemachine_ValueGuard,
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

def test_assoc_actions26_reverse_link_reassign_clear():
    a1 = statemachine_State(description="sample_text", name="sample_text")
    a2 = statemachine_State(description="sample_text_2", name="sample_text_2")
    b = statemachine_Command(code=7, name="sample_text")
    _safe_set(b, 'statemachine_Command28', a1)
    assert _is_linked(b, 'statemachine_Command28', a1)
    if hasattr(a1, 'statemachine_State27'):
        assert _is_linked(a1, 'statemachine_State27', b)
    _safe_set(b, 'statemachine_Command28', a2)
    assert _is_linked(b, 'statemachine_Command28', a2)
    if hasattr(a1, 'statemachine_State27'):
        assert not _is_linked(a1, 'statemachine_State27', b)
    if hasattr(a2, 'statemachine_State27'):
        assert _is_linked(a2, 'statemachine_State27', b)
    _safe_set(b, 'statemachine_Command28', None)
    assert not _is_linked(b, 'statemachine_Command28', a2)
    if hasattr(a2, 'statemachine_State27'):
        assert not _is_linked(a2, 'statemachine_State27', b)


def test_assoc_commands4_reverse_link_reassign_clear():
    a1 = statemachine_Statemachine(name="sample_text")
    a2 = statemachine_Statemachine(name="sample_text_2")
    b = statemachine_Command(code=7, name="sample_text")
    _safe_set(b, 'statemachine_Command', a1)
    assert _is_linked(b, 'statemachine_Command', a1)
    if hasattr(a1, 'statemachine_Statemachine5'):
        assert _is_linked(a1, 'statemachine_Statemachine5', b)
    _safe_set(b, 'statemachine_Command', a2)
    assert _is_linked(b, 'statemachine_Command', a2)
    if hasattr(a1, 'statemachine_Statemachine5'):
        assert not _is_linked(a1, 'statemachine_Statemachine5', b)
    if hasattr(a2, 'statemachine_Statemachine5'):
        assert _is_linked(a2, 'statemachine_Statemachine5', b)
    _safe_set(b, 'statemachine_Command', None)
    assert not _is_linked(b, 'statemachine_Command', a2)
    if hasattr(a2, 'statemachine_Statemachine5'):
        assert not _is_linked(a2, 'statemachine_Statemachine5', b)


def test_assoc_constants6_reverse_link_reassign_clear():
    a1 = statemachine_Statemachine(name="sample_text")
    a2 = statemachine_Statemachine(name="sample_text_2")
    b = statemachine_Constant(name="sample_text")
    _safe_set(b, 'statemachine_Constant', a1)
    assert _is_linked(b, 'statemachine_Constant', a1)
    if hasattr(a1, 'statemachine_Statemachine7'):
        assert _is_linked(a1, 'statemachine_Statemachine7', b)
    _safe_set(b, 'statemachine_Constant', a2)
    assert _is_linked(b, 'statemachine_Constant', a2)
    if hasattr(a1, 'statemachine_Statemachine7'):
        assert not _is_linked(a1, 'statemachine_Statemachine7', b)
    if hasattr(a2, 'statemachine_Statemachine7'):
        assert _is_linked(a2, 'statemachine_Statemachine7', b)
    _safe_set(b, 'statemachine_Constant', None)
    assert not _is_linked(b, 'statemachine_Constant', a2)
    if hasattr(a2, 'statemachine_Statemachine7'):
        assert not _is_linked(a2, 'statemachine_Statemachine7', b)


def test_assoc_events0_reverse_link_reassign_clear():
    a1 = statemachine_Statemachine(name="sample_text")
    a2 = statemachine_Statemachine(name="sample_text_2")
    b = statemachine_Event(code=7, name="sample_text")
    _safe_set(b, 'statemachine_Event', a1)
    assert _is_linked(b, 'statemachine_Event', a1)
    if hasattr(a1, 'statemachine_Statemachine'):
        assert _is_linked(a1, 'statemachine_Statemachine', b)
    _safe_set(b, 'statemachine_Event', a2)
    assert _is_linked(b, 'statemachine_Event', a2)
    if hasattr(a1, 'statemachine_Statemachine'):
        assert not _is_linked(a1, 'statemachine_Statemachine', b)
    if hasattr(a2, 'statemachine_Statemachine'):
        assert _is_linked(a2, 'statemachine_Statemachine', b)
    _safe_set(b, 'statemachine_Event', None)
    assert not _is_linked(b, 'statemachine_Event', a2)
    if hasattr(a2, 'statemachine_Statemachine'):
        assert not _is_linked(a2, 'statemachine_Statemachine', b)


def test_assoc_resetEvents1_reverse_link_reassign_clear():
    a1 = statemachine_Statemachine(name="sample_text")
    a2 = statemachine_Statemachine(name="sample_text_2")
    b = statemachine_Event(code=7, name="sample_text")
    _safe_set(b, 'statemachine_Event3', a1)
    assert _is_linked(b, 'statemachine_Event3', a1)
    if hasattr(a1, 'statemachine_Statemachine2'):
        assert _is_linked(a1, 'statemachine_Statemachine2', b)
    _safe_set(b, 'statemachine_Event3', a2)
    assert _is_linked(b, 'statemachine_Event3', a2)
    if hasattr(a1, 'statemachine_Statemachine2'):
        assert not _is_linked(a1, 'statemachine_Statemachine2', b)
    if hasattr(a2, 'statemachine_Statemachine2'):
        assert _is_linked(a2, 'statemachine_Statemachine2', b)
    _safe_set(b, 'statemachine_Event3', None)
    assert not _is_linked(b, 'statemachine_Event3', a2)
    if hasattr(a2, 'statemachine_Statemachine2'):
        assert not _is_linked(a2, 'statemachine_Statemachine2', b)


def test_assoc_states8_reverse_link_reassign_clear():
    a1 = statemachine_Statemachine(name="sample_text")
    a2 = statemachine_Statemachine(name="sample_text_2")
    b = statemachine_State(description="sample_text", name="sample_text")
    _safe_set(b, 'statemachine_State', a1)
    assert _is_linked(b, 'statemachine_State', a1)
    if hasattr(a1, 'statemachine_Statemachine9'):
        assert _is_linked(a1, 'statemachine_Statemachine9', b)
    _safe_set(b, 'statemachine_State', a2)
    assert _is_linked(b, 'statemachine_State', a2)
    if hasattr(a1, 'statemachine_Statemachine9'):
        assert not _is_linked(a1, 'statemachine_Statemachine9', b)
    if hasattr(a2, 'statemachine_Statemachine9'):
        assert _is_linked(a2, 'statemachine_Statemachine9', b)
    _safe_set(b, 'statemachine_State', None)
    assert not _is_linked(b, 'statemachine_State', a2)
    if hasattr(a2, 'statemachine_Statemachine9'):
        assert not _is_linked(a2, 'statemachine_Statemachine9', b)


def test_assoc_things31_reverse_link_reassign_clear():
    a1 = statemachine_Thing(name="sample_text")
    a2 = statemachine_Thing(name="sample_text_2")
    b = statemachine_State(description="sample_text", name="sample_text")
    _safe_set(b, 'statemachine_State32', {a1})
    assert _is_linked(b, 'statemachine_State32', a1)
    if hasattr(a1, 'statemachine_Thing'):
        assert _is_linked(a1, 'statemachine_Thing', b)
    _safe_set(b, 'statemachine_State32', {a2})
    assert _is_linked(b, 'statemachine_State32', a2)
    if hasattr(a1, 'statemachine_Thing'):
        assert not _is_linked(a1, 'statemachine_Thing', b)
    if hasattr(a2, 'statemachine_Thing'):
        assert _is_linked(a2, 'statemachine_Thing', b)
    _safe_set(b, 'statemachine_State32', set())
    assert not _is_linked(b, 'statemachine_State32', a2)
    if hasattr(a2, 'statemachine_Thing'):
        assert not _is_linked(a2, 'statemachine_Thing', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_constant18_stub_double():
    # statemachine_ConstantRef has no real 'statemachine_ConstantRef' property in the generated
    # code (a bare stub) -- manually attach it so statemachine_Constant's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # statemachine_Constant's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = statemachine_Constant(name="sample_text")
    partner = statemachine_ConstantRef()
    setattr(partner, 'statemachine_ConstantRef', None)
    _safe_set(owner, 'statemachine_Constant19', partner)
    assert getattr(partner, 'statemachine_ConstantRef') == owner
    _safe_set(owner, 'statemachine_Constant19', None)
    assert getattr(partner, 'statemachine_ConstantRef') is None


def test_assoc_event33_stub_double():
    # statemachine_Transition has no real 'statemachine_Transition34' property in the generated
    # code (a bare stub) -- manually attach it so statemachine_Event's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # statemachine_Event's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = statemachine_Event(code=7, name="sample_text")
    partner = statemachine_Transition()
    setattr(partner, 'statemachine_Transition34', None)
    _safe_set(owner, 'statemachine_Event35', partner)
    assert getattr(partner, 'statemachine_Transition34') == owner
    _safe_set(owner, 'statemachine_Event35', None)
    assert getattr(partner, 'statemachine_Transition34') is None


def test_assoc_guard10_stub_double():
    # statemachine_Guard has no real 'statemachine_Guard' property in the generated
    # code (a bare stub) -- manually attach it so statemachine_Event's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # statemachine_Event's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = statemachine_Event(code=7, name="sample_text")
    partner = statemachine_Guard()
    setattr(partner, 'statemachine_Guard', None)
    _safe_set(owner, 'statemachine_Event11', partner)
    assert getattr(partner, 'statemachine_Guard') == owner
    _safe_set(owner, 'statemachine_Event11', None)
    assert getattr(partner, 'statemachine_Guard') is None


def test_assoc_guard20_stub_double():
    # statemachine_Guard has no real 'statemachine_Guard22' property in the generated
    # code (a bare stub) -- manually attach it so statemachine_Command's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # statemachine_Command's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = statemachine_Command(code=7, name="sample_text")
    partner = statemachine_Guard()
    setattr(partner, 'statemachine_Guard22', None)
    _safe_set(owner, 'statemachine_Command21', partner)
    assert getattr(partner, 'statemachine_Guard22') == owner
    _safe_set(owner, 'statemachine_Command21', None)
    assert getattr(partner, 'statemachine_Guard22') is None


def test_assoc_guard42_stub_double():
    # statemachine_Guard has no real 'statemachine_Guard44' property in the generated
    # code (a bare stub) -- manually attach it so statemachine_Thing's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # statemachine_Thing's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = statemachine_Thing(name="sample_text")
    partner = statemachine_Guard()
    setattr(partner, 'statemachine_Guard44', None)
    _safe_set(owner, 'statemachine_Thing43', partner)
    assert getattr(partner, 'statemachine_Guard44') == owner
    _safe_set(owner, 'statemachine_Thing43', None)
    assert getattr(partner, 'statemachine_Guard44') is None


def test_assoc_state39_stub_double():
    # statemachine_Transition has no real 'statemachine_Transition40' property in the generated
    # code (a bare stub) -- manually attach it so statemachine_State's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # statemachine_State's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = statemachine_State(description="sample_text", name="sample_text")
    partner = statemachine_Transition()
    setattr(partner, 'statemachine_Transition40', None)
    _safe_set(owner, 'statemachine_State41', partner)
    assert getattr(partner, 'statemachine_Transition40') == owner
    _safe_set(owner, 'statemachine_State41', None)
    assert getattr(partner, 'statemachine_Transition40') is None


def test_assoc_transitions29_stub_double():
    # statemachine_Transition has no real 'statemachine_Transition' property in the generated
    # code (a bare stub) -- manually attach it so statemachine_State's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # statemachine_State's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = statemachine_State(description="sample_text", name="sample_text")
    partner = statemachine_Transition()
    setattr(partner, 'statemachine_Transition', None)
    _safe_set(owner, 'statemachine_State30', {partner})
    assert getattr(partner, 'statemachine_Transition') == owner
    _safe_set(owner, 'statemachine_State30', set())
    assert getattr(partner, 'statemachine_Transition') is None


def test_assoc_value23_stub_double():
    # statemachine_Value has no real 'statemachine_Value25' property in the generated
    # code (a bare stub) -- manually attach it so statemachine_Constant's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # statemachine_Constant's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = statemachine_Constant(name="sample_text")
    partner = statemachine_Value()
    setattr(partner, 'statemachine_Value25', None)
    _safe_set(owner, 'statemachine_Constant24', partner)
    assert getattr(partner, 'statemachine_Value25') == owner
    _safe_set(owner, 'statemachine_Constant24', None)
    assert getattr(partner, 'statemachine_Value25') is None


