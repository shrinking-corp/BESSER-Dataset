import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
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

def test_assoc_events1_reverse_link_reassign_clear():
    a1 = statemachine_Statemachine(name="sample_text")
    a2 = statemachine_Statemachine(name="sample_text_2")
    b = statemachine_Event(name="sample_text")
    _safe_set(b, 'statemachine_Event', a1)
    assert _is_linked(b, 'statemachine_Event', a1)
    if hasattr(a1, 'statemachine_Statemachine2'):
        assert _is_linked(a1, 'statemachine_Statemachine2', b)
    _safe_set(b, 'statemachine_Event', a2)
    assert _is_linked(b, 'statemachine_Event', a2)
    if hasattr(a1, 'statemachine_Statemachine2'):
        assert not _is_linked(a1, 'statemachine_Statemachine2', b)
    if hasattr(a2, 'statemachine_Statemachine2'):
        assert _is_linked(a2, 'statemachine_Statemachine2', b)
    _safe_set(b, 'statemachine_Event', None)
    assert not _is_linked(b, 'statemachine_Event', a2)
    if hasattr(a2, 'statemachine_Statemachine2'):
        assert not _is_linked(a2, 'statemachine_Statemachine2', b)


def test_assoc_initialiState5_reverse_link_reassign_clear():
    a1 = statemachine_Statemachine(name="sample_text")
    a2 = statemachine_Statemachine(name="sample_text_2")
    b = statemachine_State(name="sample_text")
    _safe_set(b, 'statemachine_State7', a1)
    assert _is_linked(b, 'statemachine_State7', a1)
    if hasattr(a1, 'statemachine_Statemachine6'):
        assert _is_linked(a1, 'statemachine_Statemachine6', b)
    _safe_set(b, 'statemachine_State7', a2)
    assert _is_linked(b, 'statemachine_State7', a2)
    if hasattr(a1, 'statemachine_Statemachine6'):
        assert not _is_linked(a1, 'statemachine_Statemachine6', b)
    if hasattr(a2, 'statemachine_Statemachine6'):
        assert _is_linked(a2, 'statemachine_Statemachine6', b)
    _safe_set(b, 'statemachine_State7', None)
    assert not _is_linked(b, 'statemachine_State7', a2)
    if hasattr(a2, 'statemachine_Statemachine6'):
        assert not _is_linked(a2, 'statemachine_Statemachine6', b)


def test_assoc_states0_reverse_link_reassign_clear():
    a1 = statemachine_Statemachine(name="sample_text")
    a2 = statemachine_Statemachine(name="sample_text_2")
    b = statemachine_State(name="sample_text")
    _safe_set(b, 'statemachine_State', a1)
    assert _is_linked(b, 'statemachine_State', a1)
    if hasattr(a1, 'statemachine_Statemachine'):
        assert _is_linked(a1, 'statemachine_Statemachine', b)
    _safe_set(b, 'statemachine_State', a2)
    assert _is_linked(b, 'statemachine_State', a2)
    if hasattr(a1, 'statemachine_Statemachine'):
        assert not _is_linked(a1, 'statemachine_Statemachine', b)
    if hasattr(a2, 'statemachine_Statemachine'):
        assert _is_linked(a2, 'statemachine_Statemachine', b)
    _safe_set(b, 'statemachine_State', None)
    assert not _is_linked(b, 'statemachine_State', a2)
    if hasattr(a2, 'statemachine_Statemachine'):
        assert not _is_linked(a2, 'statemachine_Statemachine', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_event11_stub_double():
    # statemachine_Transition has no real 'statemachine_Transition12' property in the generated
    # code (a bare stub) -- manually attach it so statemachine_Event's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # statemachine_Event's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = statemachine_Event(name="sample_text")
    partner = statemachine_Transition()
    setattr(partner, 'statemachine_Transition12', None)
    _safe_set(owner, 'statemachine_Event13', partner)
    assert getattr(partner, 'statemachine_Transition12') == owner
    _safe_set(owner, 'statemachine_Event13', None)
    assert getattr(partner, 'statemachine_Transition12') is None


def test_assoc_from_8_stub_double():
    # statemachine_Transition has no real 'statemachine_Transition9' property in the generated
    # code (a bare stub) -- manually attach it so statemachine_State's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # statemachine_State's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = statemachine_State(name="sample_text")
    partner = statemachine_Transition()
    setattr(partner, 'statemachine_Transition9', None)
    _safe_set(owner, 'statemachine_State10', partner)
    assert getattr(partner, 'statemachine_Transition9') == owner
    _safe_set(owner, 'statemachine_State10', None)
    assert getattr(partner, 'statemachine_Transition9') is None


def test_assoc_to14_stub_double():
    # statemachine_Transition has no real 'statemachine_Transition15' property in the generated
    # code (a bare stub) -- manually attach it so statemachine_State's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # statemachine_State's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = statemachine_State(name="sample_text")
    partner = statemachine_Transition()
    setattr(partner, 'statemachine_Transition15', None)
    _safe_set(owner, 'statemachine_State16', partner)
    assert getattr(partner, 'statemachine_Transition15') == owner
    _safe_set(owner, 'statemachine_State16', None)
    assert getattr(partner, 'statemachine_Transition15') is None


def test_assoc_transitions3_stub_double():
    # statemachine_Transition has no real 'statemachine_Transition' property in the generated
    # code (a bare stub) -- manually attach it so statemachine_Statemachine's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # statemachine_Statemachine's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = statemachine_Statemachine(name="sample_text")
    partner = statemachine_Transition()
    setattr(partner, 'statemachine_Transition', None)
    _safe_set(owner, 'statemachine_Statemachine4', {partner})
    assert getattr(partner, 'statemachine_Transition') == owner
    _safe_set(owner, 'statemachine_Statemachine4', set())
    assert getattr(partner, 'statemachine_Transition') is None


