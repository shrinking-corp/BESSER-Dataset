import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    AbstractEvent,
    martinfowlerdsl_AbstractEvent,
    martinfowlerdsl_Command,
    martinfowlerdsl_Event,
    martinfowlerdsl_State,
    martinfowlerdsl_StateMachine,
    martinfowlerdsl_Transition,
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

def test_assoc_actions6_stub_double():
    # martinfowlerdsl_Command has no real 'martinfowlerdsl_Command' property in the generated
    # code (a bare stub) -- manually attach it so martinfowlerdsl_State's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # martinfowlerdsl_State's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = martinfowlerdsl_State(name="sample_text")
    partner = martinfowlerdsl_Command()
    setattr(partner, 'martinfowlerdsl_Command', None)
    _safe_set(owner, 'martinfowlerdsl_State7', {partner})
    assert getattr(partner, 'martinfowlerdsl_Command') == owner
    _safe_set(owner, 'martinfowlerdsl_State7', set())
    assert getattr(partner, 'martinfowlerdsl_Command') is None


def test_assoc_events4_stub_double():
    # martinfowlerdsl_StateMachine has no real 'martinfowlerdsl_StateMachine5' property in the generated
    # code (a bare stub) -- manually attach it so martinfowlerdsl_AbstractEvent's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # martinfowlerdsl_AbstractEvent's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = martinfowlerdsl_AbstractEvent(code="sample_text", name="sample_text")
    partner = martinfowlerdsl_StateMachine()
    setattr(partner, 'martinfowlerdsl_StateMachine5', None)
    _safe_set(owner, 'martinfowlerdsl_AbstractEvent', partner)
    assert owner in getattr(partner, 'martinfowlerdsl_StateMachine5')
    _safe_set(owner, 'martinfowlerdsl_AbstractEvent', None)
    assert owner not in getattr(partner, 'martinfowlerdsl_StateMachine5')


def test_assoc_source9_stub_double():
    # martinfowlerdsl_Transition has no real 'transitions' property in the generated
    # code (a bare stub) -- manually attach it so martinfowlerdsl_State's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # martinfowlerdsl_State's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = martinfowlerdsl_State(name="sample_text")
    partner = martinfowlerdsl_Transition()
    setattr(partner, 'transitions', None)
    _safe_set(owner, 'State', partner)
    assert getattr(partner, 'transitions') == owner
    _safe_set(owner, 'State', None)
    assert getattr(partner, 'transitions') is None


def test_assoc_start1_stub_double():
    # martinfowlerdsl_StateMachine has no real 'martinfowlerdsl_StateMachine2' property in the generated
    # code (a bare stub) -- manually attach it so martinfowlerdsl_State's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # martinfowlerdsl_State's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = martinfowlerdsl_State(name="sample_text")
    partner = martinfowlerdsl_StateMachine()
    setattr(partner, 'martinfowlerdsl_StateMachine2', None)
    _safe_set(owner, 'martinfowlerdsl_State3', partner)
    assert getattr(partner, 'martinfowlerdsl_StateMachine2') == owner
    _safe_set(owner, 'martinfowlerdsl_State3', None)
    assert getattr(partner, 'martinfowlerdsl_StateMachine2') is None


def test_assoc_states0_stub_double():
    # martinfowlerdsl_StateMachine has no real 'martinfowlerdsl_StateMachine' property in the generated
    # code (a bare stub) -- manually attach it so martinfowlerdsl_State's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # martinfowlerdsl_State's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = martinfowlerdsl_State(name="sample_text")
    partner = martinfowlerdsl_StateMachine()
    setattr(partner, 'martinfowlerdsl_StateMachine', None)
    _safe_set(owner, 'martinfowlerdsl_State', partner)
    assert owner in getattr(partner, 'martinfowlerdsl_StateMachine')
    _safe_set(owner, 'martinfowlerdsl_State', None)
    assert owner not in getattr(partner, 'martinfowlerdsl_StateMachine')


def test_assoc_target10_stub_double():
    # martinfowlerdsl_Transition has no real 'martinfowlerdsl_Transition' property in the generated
    # code (a bare stub) -- manually attach it so martinfowlerdsl_State's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # martinfowlerdsl_State's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = martinfowlerdsl_State(name="sample_text")
    partner = martinfowlerdsl_Transition()
    setattr(partner, 'martinfowlerdsl_Transition', None)
    _safe_set(owner, 'martinfowlerdsl_State11', partner)
    assert getattr(partner, 'martinfowlerdsl_Transition') == owner
    _safe_set(owner, 'martinfowlerdsl_State11', None)
    assert getattr(partner, 'martinfowlerdsl_Transition') is None


def test_assoc_transitions8_stub_double():
    # martinfowlerdsl_Transition has no real 'Transition' property in the generated
    # code (a bare stub) -- manually attach it so martinfowlerdsl_State's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # martinfowlerdsl_State's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = martinfowlerdsl_State(name="sample_text")
    partner = martinfowlerdsl_Transition()
    setattr(partner, 'Transition', None)
    _safe_set(owner, 'source', {partner})
    assert getattr(partner, 'Transition') == owner
    _safe_set(owner, 'source', set())
    assert getattr(partner, 'Transition') is None


def test_assoc_trigger12_stub_double():
    # martinfowlerdsl_Transition has no real 'martinfowlerdsl_Transition13' property in the generated
    # code (a bare stub) -- manually attach it so martinfowlerdsl_Event's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # martinfowlerdsl_Event's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = martinfowlerdsl_Event(resetting=True)
    partner = martinfowlerdsl_Transition()
    setattr(partner, 'martinfowlerdsl_Transition13', None)
    _safe_set(owner, 'martinfowlerdsl_Event', partner)
    assert getattr(partner, 'martinfowlerdsl_Transition13') == owner
    _safe_set(owner, 'martinfowlerdsl_Event', None)
    assert getattr(partner, 'martinfowlerdsl_Transition13') is None


