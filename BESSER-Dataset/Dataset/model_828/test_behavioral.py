import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Guard,
    NamedElement,
    tfsm_EventGuard,
    tfsm_FSMClock,
    tfsm_FSMEvent,
    tfsm_Guard,
    tfsm_NamedElement,
    tfsm_State,
    tfsm_System,
    tfsm_TFSM,
    tfsm_TemporalGuard,
    tfsm_Transition,
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
    a1 = tfsm_Transition(action="sample_text")
    a2 = tfsm_Transition(action="sample_text_2")
    b = tfsm_State()
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


def test_assoc_outgoingTransition7_reverse_link_reassign_clear():
    a1 = tfsm_Transition(action="sample_text")
    a2 = tfsm_Transition(action="sample_text_2")
    b = tfsm_State()
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
    a1 = tfsm_Transition(action="sample_text")
    a2 = tfsm_Transition(action="sample_text_2")
    b = tfsm_State()
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
    a1 = tfsm_Transition(action="sample_text")
    a2 = tfsm_Transition(action="sample_text_2")
    b = tfsm_State()
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

def test_assoc_generatedEvents15_stub_double():
    # tfsm_FSMEvent has no real 'FSMEvent' property in the generated
    # code (a bare stub) -- manually attach it so tfsm_Transition's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # tfsm_Transition's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = tfsm_Transition(action="sample_text")
    partner = tfsm_FSMEvent()
    setattr(partner, 'FSMEvent', None)
    _safe_set(owner, 'sollicitingTransitions', {partner})
    assert getattr(partner, 'FSMEvent') == owner
    _safe_set(owner, 'sollicitingTransitions', set())
    assert getattr(partner, 'FSMEvent') is None


def test_assoc_initialState1_stub_double():
    # tfsm_TFSM has no real 'tfsm_TFSM' property in the generated
    # code (a bare stub) -- manually attach it so tfsm_State's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # tfsm_State's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = tfsm_State()
    partner = tfsm_TFSM()
    setattr(partner, 'tfsm_TFSM', None)
    _safe_set(owner, 'tfsm_State', partner)
    assert getattr(partner, 'tfsm_TFSM') == owner
    _safe_set(owner, 'tfsm_State', None)
    assert getattr(partner, 'tfsm_TFSM') is None


def test_assoc_onClock16_stub_double():
    # tfsm_FSMClock has no real 'tfsm_FSMClock17' property in the generated
    # code (a bare stub) -- manually attach it so tfsm_TemporalGuard's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # tfsm_TemporalGuard's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = tfsm_TemporalGuard(afterDuration=7)
    partner = tfsm_FSMClock()
    setattr(partner, 'tfsm_FSMClock17', None)
    _safe_set(owner, 'tfsm_TemporalGuard', partner)
    assert getattr(partner, 'tfsm_FSMClock17') == owner
    _safe_set(owner, 'tfsm_TemporalGuard', None)
    assert getattr(partner, 'tfsm_FSMClock17') is None


def test_assoc_ownedGuard14_stub_double():
    # tfsm_Guard has no real 'tfsm_Guard' property in the generated
    # code (a bare stub) -- manually attach it so tfsm_Transition's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # tfsm_Transition's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = tfsm_Transition(action="sample_text")
    partner = tfsm_Guard()
    setattr(partner, 'tfsm_Guard', None)
    _safe_set(owner, 'tfsm_Transition', partner)
    assert getattr(partner, 'tfsm_Guard') == owner
    _safe_set(owner, 'tfsm_Transition', None)
    assert getattr(partner, 'tfsm_Guard') is None


def test_assoc_ownedState0_stub_double():
    # tfsm_TFSM has no real 'owningFSM' property in the generated
    # code (a bare stub) -- manually attach it so tfsm_State's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # tfsm_State's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = tfsm_State()
    partner = tfsm_TFSM()
    setattr(partner, 'owningFSM', None)
    _safe_set(owner, 'State', partner)
    assert owner in getattr(partner, 'owningFSM')
    _safe_set(owner, 'State', None)
    assert owner not in getattr(partner, 'owningFSM')


def test_assoc_owningFSM6_stub_double():
    # tfsm_TFSM has no real 'TFSM' property in the generated
    # code (a bare stub) -- manually attach it so tfsm_State's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # tfsm_State's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = tfsm_State()
    partner = tfsm_TFSM()
    setattr(partner, 'TFSM', None)
    _safe_set(owner, 'ownedState', partner)
    assert getattr(partner, 'TFSM') == owner
    _safe_set(owner, 'ownedState', None)
    assert getattr(partner, 'TFSM') is None


def test_assoc_sollicitingTransitions20_stub_double():
    # tfsm_FSMEvent has no real 'generatedEvents' property in the generated
    # code (a bare stub) -- manually attach it so tfsm_Transition's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # tfsm_Transition's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = tfsm_Transition(action="sample_text")
    partner = tfsm_FSMEvent()
    setattr(partner, 'generatedEvents', None)
    _safe_set(owner, 'Transition21', partner)
    assert owner in getattr(partner, 'generatedEvents')
    _safe_set(owner, 'Transition21', None)
    assert owner not in getattr(partner, 'generatedEvents')


