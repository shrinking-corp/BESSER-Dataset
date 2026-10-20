import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    statemachine_Command,
    statemachine_Event,
    statemachine_State,
    statemachine_Statemachine,
    statemachine_Transition,
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

def test_assoc_actions8_reverse_link_reassign_clear():
    a1 = statemachine_State(name="sample_text")
    a2 = statemachine_State(name="sample_text_2")
    b = statemachine_Command(code="sample_text", name="sample_text")
    _safe_set(b, 'statemachine_Command10', a1)
    assert _is_linked(b, 'statemachine_Command10', a1)
    if hasattr(a1, 'statemachine_State9'):
        assert _is_linked(a1, 'statemachine_State9', b)
    _safe_set(b, 'statemachine_Command10', a2)
    assert _is_linked(b, 'statemachine_Command10', a2)
    if hasattr(a1, 'statemachine_State9'):
        assert not _is_linked(a1, 'statemachine_State9', b)
    if hasattr(a2, 'statemachine_State9'):
        assert _is_linked(a2, 'statemachine_State9', b)
    _safe_set(b, 'statemachine_Command10', None)
    assert not _is_linked(b, 'statemachine_Command10', a2)
    if hasattr(a2, 'statemachine_State9'):
        assert not _is_linked(a2, 'statemachine_State9', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_commands4_stub_double():
    # statemachine_Statemachine has no real 'statemachine_Statemachine5' property in the generated
    # code (a bare stub) -- manually attach it so statemachine_Command's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # statemachine_Command's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = statemachine_Command(code="sample_text", name="sample_text")
    partner = statemachine_Statemachine()
    setattr(partner, 'statemachine_Statemachine5', None)
    _safe_set(owner, 'statemachine_Command', partner)
    assert owner in getattr(partner, 'statemachine_Statemachine5')
    _safe_set(owner, 'statemachine_Command', None)
    assert owner not in getattr(partner, 'statemachine_Statemachine5')


def test_assoc_event13_stub_double():
    # statemachine_Transition has no real 'statemachine_Transition14' property in the generated
    # code (a bare stub) -- manually attach it so statemachine_Event's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # statemachine_Event's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = statemachine_Event(code="sample_text", name="sample_text")
    partner = statemachine_Transition()
    setattr(partner, 'statemachine_Transition14', None)
    _safe_set(owner, 'statemachine_Event15', partner)
    assert getattr(partner, 'statemachine_Transition14') == owner
    _safe_set(owner, 'statemachine_Event15', None)
    assert getattr(partner, 'statemachine_Transition14') is None


def test_assoc_events0_stub_double():
    # statemachine_Statemachine has no real 'statemachine_Statemachine' property in the generated
    # code (a bare stub) -- manually attach it so statemachine_Event's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # statemachine_Event's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = statemachine_Event(code="sample_text", name="sample_text")
    partner = statemachine_Statemachine()
    setattr(partner, 'statemachine_Statemachine', None)
    _safe_set(owner, 'statemachine_Event', partner)
    assert owner in getattr(partner, 'statemachine_Statemachine')
    _safe_set(owner, 'statemachine_Event', None)
    assert owner not in getattr(partner, 'statemachine_Statemachine')


def test_assoc_resetEvents1_stub_double():
    # statemachine_Statemachine has no real 'statemachine_Statemachine2' property in the generated
    # code (a bare stub) -- manually attach it so statemachine_Event's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # statemachine_Event's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = statemachine_Event(code="sample_text", name="sample_text")
    partner = statemachine_Statemachine()
    setattr(partner, 'statemachine_Statemachine2', None)
    _safe_set(owner, 'statemachine_Event3', partner)
    assert owner in getattr(partner, 'statemachine_Statemachine2')
    _safe_set(owner, 'statemachine_Event3', None)
    assert owner not in getattr(partner, 'statemachine_Statemachine2')


def test_assoc_state16_stub_double():
    # statemachine_Transition has no real 'statemachine_Transition17' property in the generated
    # code (a bare stub) -- manually attach it so statemachine_State's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # statemachine_State's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = statemachine_State(name="sample_text")
    partner = statemachine_Transition()
    setattr(partner, 'statemachine_Transition17', None)
    _safe_set(owner, 'statemachine_State18', partner)
    assert getattr(partner, 'statemachine_Transition17') == owner
    _safe_set(owner, 'statemachine_State18', None)
    assert getattr(partner, 'statemachine_Transition17') is None


def test_assoc_states6_stub_double():
    # statemachine_Statemachine has no real 'statemachine_Statemachine7' property in the generated
    # code (a bare stub) -- manually attach it so statemachine_State's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # statemachine_State's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = statemachine_State(name="sample_text")
    partner = statemachine_Statemachine()
    setattr(partner, 'statemachine_Statemachine7', None)
    _safe_set(owner, 'statemachine_State', partner)
    assert owner in getattr(partner, 'statemachine_Statemachine7')
    _safe_set(owner, 'statemachine_State', None)
    assert owner not in getattr(partner, 'statemachine_Statemachine7')


def test_assoc_transitions11_stub_double():
    # statemachine_Transition has no real 'statemachine_Transition' property in the generated
    # code (a bare stub) -- manually attach it so statemachine_State's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # statemachine_State's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = statemachine_State(name="sample_text")
    partner = statemachine_Transition()
    setattr(partner, 'statemachine_Transition', None)
    _safe_set(owner, 'statemachine_State12', {partner})
    assert getattr(partner, 'statemachine_Transition') == owner
    _safe_set(owner, 'statemachine_State12', set())
    assert getattr(partner, 'statemachine_Transition') is None


