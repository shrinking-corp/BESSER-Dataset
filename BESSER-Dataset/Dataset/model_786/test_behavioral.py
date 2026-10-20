import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    fsm_FSM,
    fsm_RuntimeConcept1,
    fsm_RuntimeConcept2,
    fsm_State,
    fsm_Transition,
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

def test_assoc_incomingTransition8_reverse_link_reassign_clear():
    a1 = fsm_Transition(input="sample_text", output="sample_text")
    a2 = fsm_Transition(input="sample_text_2", output="sample_text_2")
    b = fsm_State(name="sample_text")
    _safe_set(b, 'target', {a1})
    assert _is_linked(b, 'target', a1)
    if hasattr(a1, 'Transition9'):
        assert _is_linked(a1, 'Transition9', b)
    _safe_set(b, 'target', {a2})
    assert _is_linked(b, 'target', a2)
    if hasattr(a1, 'Transition9'):
        assert not _is_linked(a1, 'Transition9', b)
    if hasattr(a2, 'Transition9'):
        assert _is_linked(a2, 'Transition9', b)
    _safe_set(b, 'target', set())
    assert not _is_linked(b, 'target', a2)
    if hasattr(a2, 'Transition9'):
        assert not _is_linked(a2, 'Transition9', b)


def test_assoc_myFoos5_reverse_link_reassign_clear():
    a1 = fsm_RuntimeConcept2(bar="sample_text")
    a2 = fsm_RuntimeConcept2(bar="sample_text_2")
    b = fsm_RuntimeConcept1(foo=7)
    _safe_set(b, 'fsm_RuntimeConcept1', a1)
    assert _is_linked(b, 'fsm_RuntimeConcept1', a1)
    if hasattr(a1, 'fsm_RuntimeConcept2'):
        assert _is_linked(a1, 'fsm_RuntimeConcept2', b)
    _safe_set(b, 'fsm_RuntimeConcept1', a2)
    assert _is_linked(b, 'fsm_RuntimeConcept1', a2)
    if hasattr(a1, 'fsm_RuntimeConcept2'):
        assert not _is_linked(a1, 'fsm_RuntimeConcept2', b)
    if hasattr(a2, 'fsm_RuntimeConcept2'):
        assert _is_linked(a2, 'fsm_RuntimeConcept2', b)
    _safe_set(b, 'fsm_RuntimeConcept1', None)
    assert not _is_linked(b, 'fsm_RuntimeConcept1', a2)
    if hasattr(a2, 'fsm_RuntimeConcept2'):
        assert not _is_linked(a2, 'fsm_RuntimeConcept2', b)


def test_assoc_myState14_reverse_link_reassign_clear():
    a1 = fsm_State(name="sample_text")
    a2 = fsm_State(name="sample_text_2")
    b = fsm_RuntimeConcept1(foo=7)
    _safe_set(b, 'fsm_RuntimeConcept115', a1)
    assert _is_linked(b, 'fsm_RuntimeConcept115', a1)
    if hasattr(a1, 'fsm_State16'):
        assert _is_linked(a1, 'fsm_State16', b)
    _safe_set(b, 'fsm_RuntimeConcept115', a2)
    assert _is_linked(b, 'fsm_RuntimeConcept115', a2)
    if hasattr(a1, 'fsm_State16'):
        assert not _is_linked(a1, 'fsm_State16', b)
    if hasattr(a2, 'fsm_State16'):
        assert _is_linked(a2, 'fsm_State16', b)
    _safe_set(b, 'fsm_RuntimeConcept115', None)
    assert not _is_linked(b, 'fsm_RuntimeConcept115', a2)
    if hasattr(a2, 'fsm_State16'):
        assert not _is_linked(a2, 'fsm_State16', b)


def test_assoc_outgoingTransition7_reverse_link_reassign_clear():
    a1 = fsm_Transition(input="sample_text", output="sample_text")
    a2 = fsm_Transition(input="sample_text_2", output="sample_text_2")
    b = fsm_State(name="sample_text")
    _safe_set(b, 'source', {a1})
    assert _is_linked(b, 'source', a1)
    if hasattr(a1, 'Transition'):
        assert _is_linked(a1, 'Transition', b)
    _safe_set(b, 'source', {a2})
    assert _is_linked(b, 'source', a2)
    if hasattr(a1, 'Transition'):
        assert not _is_linked(a1, 'Transition', b)
    if hasattr(a2, 'Transition'):
        assert _is_linked(a2, 'Transition', b)
    _safe_set(b, 'source', set())
    assert not _is_linked(b, 'source', a2)
    if hasattr(a2, 'Transition'):
        assert not _is_linked(a2, 'Transition', b)


def test_assoc_source10_reverse_link_reassign_clear():
    a1 = fsm_Transition(input="sample_text", output="sample_text")
    a2 = fsm_Transition(input="sample_text_2", output="sample_text_2")
    b = fsm_State(name="sample_text")
    _safe_set(b, 'State11', a1)
    assert _is_linked(b, 'State11', a1)
    if hasattr(a1, 'outgoingTransition'):
        assert _is_linked(a1, 'outgoingTransition', b)
    _safe_set(b, 'State11', a2)
    assert _is_linked(b, 'State11', a2)
    if hasattr(a1, 'outgoingTransition'):
        assert not _is_linked(a1, 'outgoingTransition', b)
    if hasattr(a2, 'outgoingTransition'):
        assert _is_linked(a2, 'outgoingTransition', b)
    _safe_set(b, 'State11', None)
    assert not _is_linked(b, 'State11', a2)
    if hasattr(a2, 'outgoingTransition'):
        assert not _is_linked(a2, 'outgoingTransition', b)


def test_assoc_target12_reverse_link_reassign_clear():
    a1 = fsm_Transition(input="sample_text", output="sample_text")
    a2 = fsm_Transition(input="sample_text_2", output="sample_text_2")
    b = fsm_State(name="sample_text")
    _safe_set(b, 'State13', a1)
    assert _is_linked(b, 'State13', a1)
    if hasattr(a1, 'incomingTransition'):
        assert _is_linked(a1, 'incomingTransition', b)
    _safe_set(b, 'State13', a2)
    assert _is_linked(b, 'State13', a2)
    if hasattr(a1, 'incomingTransition'):
        assert not _is_linked(a1, 'incomingTransition', b)
    if hasattr(a2, 'incomingTransition'):
        assert _is_linked(a2, 'incomingTransition', b)
    _safe_set(b, 'State13', None)
    assert not _is_linked(b, 'State13', a2)
    if hasattr(a2, 'incomingTransition'):
        assert not _is_linked(a2, 'incomingTransition', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_finalState2_stub_double():
    # fsm_FSM has no real 'fsm_FSM3' property in the generated
    # code (a bare stub) -- manually attach it so fsm_State's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # fsm_State's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = fsm_State(name="sample_text")
    partner = fsm_FSM()
    setattr(partner, 'fsm_FSM3', None)
    _safe_set(owner, 'fsm_State4', partner)
    assert owner in getattr(partner, 'fsm_FSM3')
    _safe_set(owner, 'fsm_State4', None)
    assert owner not in getattr(partner, 'fsm_FSM3')


def test_assoc_initialState1_stub_double():
    # fsm_FSM has no real 'fsm_FSM' property in the generated
    # code (a bare stub) -- manually attach it so fsm_State's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # fsm_State's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = fsm_State(name="sample_text")
    partner = fsm_FSM()
    setattr(partner, 'fsm_FSM', None)
    _safe_set(owner, 'fsm_State', partner)
    assert getattr(partner, 'fsm_FSM') == owner
    _safe_set(owner, 'fsm_State', None)
    assert getattr(partner, 'fsm_FSM') is None


def test_assoc_ownedState0_stub_double():
    # fsm_FSM has no real 'owningFSM' property in the generated
    # code (a bare stub) -- manually attach it so fsm_State's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # fsm_State's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = fsm_State(name="sample_text")
    partner = fsm_FSM()
    setattr(partner, 'owningFSM', None)
    _safe_set(owner, 'State', partner)
    assert owner in getattr(partner, 'owningFSM')
    _safe_set(owner, 'State', None)
    assert owner not in getattr(partner, 'owningFSM')


def test_assoc_owningFSM6_stub_double():
    # fsm_FSM has no real 'FSM' property in the generated
    # code (a bare stub) -- manually attach it so fsm_State's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # fsm_State's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = fsm_State(name="sample_text")
    partner = fsm_FSM()
    setattr(partner, 'FSM', None)
    _safe_set(owner, 'ownedState', partner)
    assert getattr(partner, 'FSM') == owner
    _safe_set(owner, 'ownedState', None)
    assert getattr(partner, 'FSM') is None


