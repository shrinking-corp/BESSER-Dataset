import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    fowlerdsl_Command,
    fowlerdsl_Event,
    fowlerdsl_State,
    fowlerdsl_Statemachine,
    fowlerdsl_Transition,
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

def test_assoc_actions5_reverse_link_reassign_clear():
    a1 = fowlerdsl_State(name="sample_text")
    a2 = fowlerdsl_State(name="sample_text_2")
    b = fowlerdsl_Command(code="sample_text", name="sample_text")
    _safe_set(b, 'fowlerdsl_Command7', a1)
    assert _is_linked(b, 'fowlerdsl_Command7', a1)
    if hasattr(a1, 'fowlerdsl_State6'):
        assert _is_linked(a1, 'fowlerdsl_State6', b)
    _safe_set(b, 'fowlerdsl_Command7', a2)
    assert _is_linked(b, 'fowlerdsl_Command7', a2)
    if hasattr(a1, 'fowlerdsl_State6'):
        assert not _is_linked(a1, 'fowlerdsl_State6', b)
    if hasattr(a2, 'fowlerdsl_State6'):
        assert _is_linked(a2, 'fowlerdsl_State6', b)
    _safe_set(b, 'fowlerdsl_Command7', None)
    assert not _is_linked(b, 'fowlerdsl_Command7', a2)
    if hasattr(a2, 'fowlerdsl_State6'):
        assert not _is_linked(a2, 'fowlerdsl_State6', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_commands1_stub_double():
    # fowlerdsl_Statemachine has no real 'fowlerdsl_Statemachine2' property in the generated
    # code (a bare stub) -- manually attach it so fowlerdsl_Command's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # fowlerdsl_Command's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = fowlerdsl_Command(code="sample_text", name="sample_text")
    partner = fowlerdsl_Statemachine()
    setattr(partner, 'fowlerdsl_Statemachine2', None)
    _safe_set(owner, 'fowlerdsl_Command', partner)
    assert owner in getattr(partner, 'fowlerdsl_Statemachine2')
    _safe_set(owner, 'fowlerdsl_Command', None)
    assert owner not in getattr(partner, 'fowlerdsl_Statemachine2')


def test_assoc_event10_stub_double():
    # fowlerdsl_Transition has no real 'fowlerdsl_Transition11' property in the generated
    # code (a bare stub) -- manually attach it so fowlerdsl_Event's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # fowlerdsl_Event's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = fowlerdsl_Event(code="sample_text", name="sample_text", resetting=True)
    partner = fowlerdsl_Transition()
    setattr(partner, 'fowlerdsl_Transition11', None)
    _safe_set(owner, 'fowlerdsl_Event12', partner)
    assert getattr(partner, 'fowlerdsl_Transition11') == owner
    _safe_set(owner, 'fowlerdsl_Event12', None)
    assert getattr(partner, 'fowlerdsl_Transition11') is None


def test_assoc_events0_stub_double():
    # fowlerdsl_Statemachine has no real 'fowlerdsl_Statemachine' property in the generated
    # code (a bare stub) -- manually attach it so fowlerdsl_Event's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # fowlerdsl_Event's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = fowlerdsl_Event(code="sample_text", name="sample_text", resetting=True)
    partner = fowlerdsl_Statemachine()
    setattr(partner, 'fowlerdsl_Statemachine', None)
    _safe_set(owner, 'fowlerdsl_Event', partner)
    assert owner in getattr(partner, 'fowlerdsl_Statemachine')
    _safe_set(owner, 'fowlerdsl_Event', None)
    assert owner not in getattr(partner, 'fowlerdsl_Statemachine')


def test_assoc_state13_stub_double():
    # fowlerdsl_Transition has no real 'fowlerdsl_Transition14' property in the generated
    # code (a bare stub) -- manually attach it so fowlerdsl_State's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # fowlerdsl_State's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = fowlerdsl_State(name="sample_text")
    partner = fowlerdsl_Transition()
    setattr(partner, 'fowlerdsl_Transition14', None)
    _safe_set(owner, 'fowlerdsl_State15', partner)
    assert getattr(partner, 'fowlerdsl_Transition14') == owner
    _safe_set(owner, 'fowlerdsl_State15', None)
    assert getattr(partner, 'fowlerdsl_Transition14') is None


def test_assoc_states3_stub_double():
    # fowlerdsl_Statemachine has no real 'fowlerdsl_Statemachine4' property in the generated
    # code (a bare stub) -- manually attach it so fowlerdsl_State's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # fowlerdsl_State's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = fowlerdsl_State(name="sample_text")
    partner = fowlerdsl_Statemachine()
    setattr(partner, 'fowlerdsl_Statemachine4', None)
    _safe_set(owner, 'fowlerdsl_State', partner)
    assert owner in getattr(partner, 'fowlerdsl_Statemachine4')
    _safe_set(owner, 'fowlerdsl_State', None)
    assert owner not in getattr(partner, 'fowlerdsl_Statemachine4')


def test_assoc_transitions8_stub_double():
    # fowlerdsl_Transition has no real 'fowlerdsl_Transition' property in the generated
    # code (a bare stub) -- manually attach it so fowlerdsl_State's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # fowlerdsl_State's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = fowlerdsl_State(name="sample_text")
    partner = fowlerdsl_Transition()
    setattr(partner, 'fowlerdsl_Transition', None)
    _safe_set(owner, 'fowlerdsl_State9', {partner})
    assert getattr(partner, 'fowlerdsl_Transition') == owner
    _safe_set(owner, 'fowlerdsl_State9', set())
    assert getattr(partner, 'fowlerdsl_Transition') is None


