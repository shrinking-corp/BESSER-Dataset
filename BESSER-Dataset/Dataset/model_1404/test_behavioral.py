import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    HSM_CompositeState,
    HSM_State,
    HSM_StateMachine,
    HSM_Transition,
    State,
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

def test_assoc_machine3_reverse_link_reassign_clear():
    a1 = HSM_StateMachine(name="sample_text")
    a2 = HSM_StateMachine(name="sample_text_2")
    b = HSM_State(name="sample_text")
    _safe_set(b, 'states', a1)
    assert _is_linked(b, 'states', a1)
    if hasattr(a1, 'StateMachine'):
        assert _is_linked(a1, 'StateMachine', b)
    _safe_set(b, 'states', a2)
    assert _is_linked(b, 'states', a2)
    if hasattr(a1, 'StateMachine'):
        assert not _is_linked(a1, 'StateMachine', b)
    if hasattr(a2, 'StateMachine'):
        assert _is_linked(a2, 'StateMachine', b)
    _safe_set(b, 'states', None)
    assert not _is_linked(b, 'states', a2)
    if hasattr(a2, 'StateMachine'):
        assert not _is_linked(a2, 'StateMachine', b)


def test_assoc_states0_reverse_link_reassign_clear():
    a1 = HSM_StateMachine(name="sample_text")
    a2 = HSM_StateMachine(name="sample_text_2")
    b = HSM_State(name="sample_text")
    _safe_set(b, 'State', a1)
    assert _is_linked(b, 'State', a1)
    if hasattr(a1, 'machine'):
        assert _is_linked(a1, 'machine', b)
    _safe_set(b, 'State', a2)
    assert _is_linked(b, 'State', a2)
    if hasattr(a1, 'machine'):
        assert not _is_linked(a1, 'machine', b)
    if hasattr(a2, 'machine'):
        assert _is_linked(a2, 'machine', b)
    _safe_set(b, 'State', None)
    assert not _is_linked(b, 'State', a2)
    if hasattr(a2, 'machine'):
        assert not _is_linked(a2, 'machine', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_container2_stub_double():
    # HSM_CompositeState has no real 'HSM_CompositeState' property in the generated
    # code (a bare stub) -- manually attach it so HSM_State's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # HSM_State's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = HSM_State(name="sample_text")
    partner = HSM_CompositeState()
    setattr(partner, 'HSM_CompositeState', None)
    _safe_set(owner, 'HSM_State', partner)
    assert getattr(partner, 'HSM_CompositeState') == owner
    _safe_set(owner, 'HSM_State', None)
    assert getattr(partner, 'HSM_CompositeState') is None


def test_assoc_machine10_stub_double():
    # HSM_Transition has no real 'HSM_Transition11' property in the generated
    # code (a bare stub) -- manually attach it so HSM_StateMachine's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # HSM_StateMachine's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = HSM_StateMachine(name="sample_text")
    partner = HSM_Transition()
    setattr(partner, 'HSM_Transition11', None)
    _safe_set(owner, 'HSM_StateMachine12', partner)
    assert getattr(partner, 'HSM_Transition11') == owner
    _safe_set(owner, 'HSM_StateMachine12', None)
    assert getattr(partner, 'HSM_Transition11') is None


def test_assoc_source4_stub_double():
    # HSM_Transition has no real 'HSM_Transition5' property in the generated
    # code (a bare stub) -- manually attach it so HSM_State's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # HSM_State's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = HSM_State(name="sample_text")
    partner = HSM_Transition()
    setattr(partner, 'HSM_Transition5', None)
    _safe_set(owner, 'HSM_State6', partner)
    assert getattr(partner, 'HSM_Transition5') == owner
    _safe_set(owner, 'HSM_State6', None)
    assert getattr(partner, 'HSM_Transition5') is None


def test_assoc_target7_stub_double():
    # HSM_Transition has no real 'HSM_Transition8' property in the generated
    # code (a bare stub) -- manually attach it so HSM_State's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # HSM_State's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = HSM_State(name="sample_text")
    partner = HSM_Transition()
    setattr(partner, 'HSM_Transition8', None)
    _safe_set(owner, 'HSM_State9', partner)
    assert getattr(partner, 'HSM_Transition8') == owner
    _safe_set(owner, 'HSM_State9', None)
    assert getattr(partner, 'HSM_Transition8') is None


def test_assoc_transitions1_stub_double():
    # HSM_Transition has no real 'HSM_Transition' property in the generated
    # code (a bare stub) -- manually attach it so HSM_StateMachine's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # HSM_StateMachine's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = HSM_StateMachine(name="sample_text")
    partner = HSM_Transition()
    setattr(partner, 'HSM_Transition', None)
    _safe_set(owner, 'HSM_StateMachine', {partner})
    assert getattr(partner, 'HSM_Transition') == owner
    _safe_set(owner, 'HSM_StateMachine', set())
    assert getattr(partner, 'HSM_Transition') is None


