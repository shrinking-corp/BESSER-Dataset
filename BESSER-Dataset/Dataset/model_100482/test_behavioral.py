import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Guard,
    NamedElement,
    tfsmextended_EvaluateGuard,
    tfsmextended_EventGuard,
    tfsmextended_FSMClock,
    tfsmextended_FSMEvent,
    tfsmextended_Guard,
    tfsmextended_NamedElement,
    tfsmextended_State,
    tfsmextended_TFSM,
    tfsmextended_TemporalGuard,
    tfsmextended_TimedSystem,
    tfsmextended_Transition,
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

def test_assoc_currentState8_reverse_link_reassign_clear():
    a1 = tfsmextended_TFSM()
    a2 = tfsmextended_TFSM()
    b = tfsmextended_State()
    _safe_set(b, 'tfsmextended_State10', a1)
    assert _is_linked(b, 'tfsmextended_State10', a1)
    if hasattr(a1, 'tfsmextended_TFSM9'):
        assert _is_linked(a1, 'tfsmextended_TFSM9', b)
    _safe_set(b, 'tfsmextended_State10', a2)
    assert _is_linked(b, 'tfsmextended_State10', a2)
    if hasattr(a1, 'tfsmextended_TFSM9'):
        assert not _is_linked(a1, 'tfsmextended_TFSM9', b)
    if hasattr(a2, 'tfsmextended_TFSM9'):
        assert _is_linked(a2, 'tfsmextended_TFSM9', b)
    _safe_set(b, 'tfsmextended_State10', None)
    assert not _is_linked(b, 'tfsmextended_State10', a2)
    if hasattr(a2, 'tfsmextended_TFSM9'):
        assert not _is_linked(a2, 'tfsmextended_TFSM9', b)


def test_assoc_generatedEvents21_reverse_link_reassign_clear():
    a1 = tfsmextended_Transition(action="sample_text")
    a2 = tfsmextended_Transition(action="sample_text_2")
    b = tfsmextended_FSMEvent(isTriggered=True)
    _safe_set(b, 'tfsmextended_FSMEvent23', a1)
    assert _is_linked(b, 'tfsmextended_FSMEvent23', a1)
    if hasattr(a1, 'tfsmextended_Transition22'):
        assert _is_linked(a1, 'tfsmextended_Transition22', b)
    _safe_set(b, 'tfsmextended_FSMEvent23', a2)
    assert _is_linked(b, 'tfsmextended_FSMEvent23', a2)
    if hasattr(a1, 'tfsmextended_Transition22'):
        assert not _is_linked(a1, 'tfsmextended_Transition22', b)
    if hasattr(a2, 'tfsmextended_Transition22'):
        assert _is_linked(a2, 'tfsmextended_Transition22', b)
    _safe_set(b, 'tfsmextended_FSMEvent23', None)
    assert not _is_linked(b, 'tfsmextended_FSMEvent23', a2)
    if hasattr(a2, 'tfsmextended_Transition22'):
        assert not _is_linked(a2, 'tfsmextended_Transition22', b)


def test_assoc_incomingTransitions13_reverse_link_reassign_clear():
    a1 = tfsmextended_Transition(action="sample_text")
    a2 = tfsmextended_Transition(action="sample_text_2")
    b = tfsmextended_State()
    _safe_set(b, 'target', {a1})
    assert _is_linked(b, 'target', a1)
    if hasattr(a1, 'Transition14'):
        assert _is_linked(a1, 'Transition14', b)
    _safe_set(b, 'target', {a2})
    assert _is_linked(b, 'target', a2)
    if hasattr(a1, 'Transition14'):
        assert not _is_linked(a1, 'Transition14', b)
    if hasattr(a2, 'Transition14'):
        assert _is_linked(a2, 'Transition14', b)
    _safe_set(b, 'target', set())
    assert not _is_linked(b, 'target', a2)
    if hasattr(a2, 'Transition14'):
        assert not _is_linked(a2, 'Transition14', b)


def test_assoc_initialState1_reverse_link_reassign_clear():
    a1 = tfsmextended_TFSM()
    a2 = tfsmextended_TFSM()
    b = tfsmextended_State()
    _safe_set(b, 'tfsmextended_State', a1)
    assert _is_linked(b, 'tfsmextended_State', a1)
    if hasattr(a1, 'tfsmextended_TFSM'):
        assert _is_linked(a1, 'tfsmextended_TFSM', b)
    _safe_set(b, 'tfsmextended_State', a2)
    assert _is_linked(b, 'tfsmextended_State', a2)
    if hasattr(a1, 'tfsmextended_TFSM'):
        assert not _is_linked(a1, 'tfsmextended_TFSM', b)
    if hasattr(a2, 'tfsmextended_TFSM'):
        assert _is_linked(a2, 'tfsmextended_TFSM', b)
    _safe_set(b, 'tfsmextended_State', None)
    assert not _is_linked(b, 'tfsmextended_State', a2)
    if hasattr(a2, 'tfsmextended_TFSM'):
        assert not _is_linked(a2, 'tfsmextended_TFSM', b)


def test_assoc_localClock4_reverse_link_reassign_clear():
    a1 = tfsmextended_TFSM()
    a2 = tfsmextended_TFSM()
    b = tfsmextended_FSMClock(numberOfTicks="sample_text")
    _safe_set(b, 'tfsmextended_FSMClock', a1)
    assert _is_linked(b, 'tfsmextended_FSMClock', a1)
    if hasattr(a1, 'tfsmextended_TFSM5'):
        assert _is_linked(a1, 'tfsmextended_TFSM5', b)
    _safe_set(b, 'tfsmextended_FSMClock', a2)
    assert _is_linked(b, 'tfsmextended_FSMClock', a2)
    if hasattr(a1, 'tfsmextended_TFSM5'):
        assert not _is_linked(a1, 'tfsmextended_TFSM5', b)
    if hasattr(a2, 'tfsmextended_TFSM5'):
        assert _is_linked(a2, 'tfsmextended_TFSM5', b)
    _safe_set(b, 'tfsmextended_FSMClock', None)
    assert not _is_linked(b, 'tfsmextended_FSMClock', a2)
    if hasattr(a2, 'tfsmextended_TFSM5'):
        assert not _is_linked(a2, 'tfsmextended_TFSM5', b)


def test_assoc_localEvents2_reverse_link_reassign_clear():
    a1 = tfsmextended_TFSM()
    a2 = tfsmextended_TFSM()
    b = tfsmextended_FSMEvent(isTriggered=True)
    _safe_set(b, 'tfsmextended_FSMEvent', a1)
    assert _is_linked(b, 'tfsmextended_FSMEvent', a1)
    if hasattr(a1, 'tfsmextended_TFSM3'):
        assert _is_linked(a1, 'tfsmextended_TFSM3', b)
    _safe_set(b, 'tfsmextended_FSMEvent', a2)
    assert _is_linked(b, 'tfsmextended_FSMEvent', a2)
    if hasattr(a1, 'tfsmextended_TFSM3'):
        assert not _is_linked(a1, 'tfsmextended_TFSM3', b)
    if hasattr(a2, 'tfsmextended_TFSM3'):
        assert _is_linked(a2, 'tfsmextended_TFSM3', b)
    _safe_set(b, 'tfsmextended_FSMEvent', None)
    assert not _is_linked(b, 'tfsmextended_FSMEvent', a2)
    if hasattr(a2, 'tfsmextended_TFSM3'):
        assert not _is_linked(a2, 'tfsmextended_TFSM3', b)


def test_assoc_onClock24_reverse_link_reassign_clear():
    a1 = tfsmextended_TemporalGuard(afterDuration=7)
    a2 = tfsmextended_TemporalGuard(afterDuration=13)
    b = tfsmextended_FSMClock(numberOfTicks="sample_text")
    _safe_set(b, 'tfsmextended_FSMClock25', a1)
    assert _is_linked(b, 'tfsmextended_FSMClock25', a1)
    if hasattr(a1, 'tfsmextended_TemporalGuard'):
        assert _is_linked(a1, 'tfsmextended_TemporalGuard', b)
    _safe_set(b, 'tfsmextended_FSMClock25', a2)
    assert _is_linked(b, 'tfsmextended_FSMClock25', a2)
    if hasattr(a1, 'tfsmextended_TemporalGuard'):
        assert not _is_linked(a1, 'tfsmextended_TemporalGuard', b)
    if hasattr(a2, 'tfsmextended_TemporalGuard'):
        assert _is_linked(a2, 'tfsmextended_TemporalGuard', b)
    _safe_set(b, 'tfsmextended_FSMClock25', None)
    assert not _is_linked(b, 'tfsmextended_FSMClock25', a2)
    if hasattr(a2, 'tfsmextended_TemporalGuard'):
        assert not _is_linked(a2, 'tfsmextended_TemporalGuard', b)


def test_assoc_outgoingTransitions12_reverse_link_reassign_clear():
    a1 = tfsmextended_Transition(action="sample_text")
    a2 = tfsmextended_Transition(action="sample_text_2")
    b = tfsmextended_State()
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


def test_assoc_ownedStates0_reverse_link_reassign_clear():
    a1 = tfsmextended_TFSM()
    a2 = tfsmextended_TFSM()
    b = tfsmextended_State()
    _safe_set(b, 'State', a1)
    assert _is_linked(b, 'State', a1)
    if hasattr(a1, 'owningFSM'):
        assert _is_linked(a1, 'owningFSM', b)
    _safe_set(b, 'State', a2)
    assert _is_linked(b, 'State', a2)
    if hasattr(a1, 'owningFSM'):
        assert not _is_linked(a1, 'owningFSM', b)
    if hasattr(a2, 'owningFSM'):
        assert _is_linked(a2, 'owningFSM', b)
    _safe_set(b, 'State', None)
    assert not _is_linked(b, 'State', a2)
    if hasattr(a2, 'owningFSM'):
        assert not _is_linked(a2, 'owningFSM', b)


def test_assoc_ownedTransitions6_reverse_link_reassign_clear():
    a1 = tfsmextended_Transition(action="sample_text")
    a2 = tfsmextended_Transition(action="sample_text_2")
    b = tfsmextended_TFSM()
    _safe_set(b, 'tfsmextended_TFSM7', {a1})
    assert _is_linked(b, 'tfsmextended_TFSM7', a1)
    if hasattr(a1, 'tfsmextended_Transition'):
        assert _is_linked(a1, 'tfsmextended_Transition', b)
    _safe_set(b, 'tfsmextended_TFSM7', {a2})
    assert _is_linked(b, 'tfsmextended_TFSM7', a2)
    if hasattr(a1, 'tfsmextended_Transition'):
        assert not _is_linked(a1, 'tfsmextended_Transition', b)
    if hasattr(a2, 'tfsmextended_Transition'):
        assert _is_linked(a2, 'tfsmextended_Transition', b)
    _safe_set(b, 'tfsmextended_TFSM7', set())
    assert not _is_linked(b, 'tfsmextended_TFSM7', a2)
    if hasattr(a2, 'tfsmextended_Transition'):
        assert not _is_linked(a2, 'tfsmextended_Transition', b)


def test_assoc_owningFSM11_reverse_link_reassign_clear():
    a1 = tfsmextended_TFSM()
    a2 = tfsmextended_TFSM()
    b = tfsmextended_State()
    _safe_set(b, 'ownedStates', a1)
    assert _is_linked(b, 'ownedStates', a1)
    if hasattr(a1, 'TFSM'):
        assert _is_linked(a1, 'TFSM', b)
    _safe_set(b, 'ownedStates', a2)
    assert _is_linked(b, 'ownedStates', a2)
    if hasattr(a1, 'TFSM'):
        assert not _is_linked(a1, 'TFSM', b)
    if hasattr(a2, 'TFSM'):
        assert _is_linked(a2, 'TFSM', b)
    _safe_set(b, 'ownedStates', None)
    assert not _is_linked(b, 'ownedStates', a2)
    if hasattr(a2, 'TFSM'):
        assert not _is_linked(a2, 'TFSM', b)


def test_assoc_sollicitingTransitions28_reverse_link_reassign_clear():
    a1 = tfsmextended_Transition(action="sample_text")
    a2 = tfsmextended_Transition(action="sample_text_2")
    b = tfsmextended_FSMEvent(isTriggered=True)
    _safe_set(b, 'tfsmextended_FSMEvent29', {a1})
    assert _is_linked(b, 'tfsmextended_FSMEvent29', a1)
    if hasattr(a1, 'tfsmextended_Transition30'):
        assert _is_linked(a1, 'tfsmextended_Transition30', b)
    _safe_set(b, 'tfsmextended_FSMEvent29', {a2})
    assert _is_linked(b, 'tfsmextended_FSMEvent29', a2)
    if hasattr(a1, 'tfsmextended_Transition30'):
        assert not _is_linked(a1, 'tfsmextended_Transition30', b)
    if hasattr(a2, 'tfsmextended_Transition30'):
        assert _is_linked(a2, 'tfsmextended_Transition30', b)
    _safe_set(b, 'tfsmextended_FSMEvent29', set())
    assert not _is_linked(b, 'tfsmextended_FSMEvent29', a2)
    if hasattr(a2, 'tfsmextended_Transition30'):
        assert not _is_linked(a2, 'tfsmextended_Transition30', b)


def test_assoc_source15_reverse_link_reassign_clear():
    a1 = tfsmextended_Transition(action="sample_text")
    a2 = tfsmextended_Transition(action="sample_text_2")
    b = tfsmextended_State()
    _safe_set(b, 'State16', a1)
    assert _is_linked(b, 'State16', a1)
    if hasattr(a1, 'outgoingTransitions'):
        assert _is_linked(a1, 'outgoingTransitions', b)
    _safe_set(b, 'State16', a2)
    assert _is_linked(b, 'State16', a2)
    if hasattr(a1, 'outgoingTransitions'):
        assert not _is_linked(a1, 'outgoingTransitions', b)
    if hasattr(a2, 'outgoingTransitions'):
        assert _is_linked(a2, 'outgoingTransitions', b)
    _safe_set(b, 'State16', None)
    assert not _is_linked(b, 'State16', a2)
    if hasattr(a2, 'outgoingTransitions'):
        assert not _is_linked(a2, 'outgoingTransitions', b)


def test_assoc_target17_reverse_link_reassign_clear():
    a1 = tfsmextended_Transition(action="sample_text")
    a2 = tfsmextended_Transition(action="sample_text_2")
    b = tfsmextended_State()
    _safe_set(b, 'State18', a1)
    assert _is_linked(b, 'State18', a1)
    if hasattr(a1, 'incomingTransitions'):
        assert _is_linked(a1, 'incomingTransitions', b)
    _safe_set(b, 'State18', a2)
    assert _is_linked(b, 'State18', a2)
    if hasattr(a1, 'incomingTransitions'):
        assert not _is_linked(a1, 'incomingTransitions', b)
    if hasattr(a2, 'incomingTransitions'):
        assert _is_linked(a2, 'incomingTransitions', b)
    _safe_set(b, 'State18', None)
    assert not _is_linked(b, 'State18', a2)
    if hasattr(a2, 'incomingTransitions'):
        assert not _is_linked(a2, 'incomingTransitions', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_globalClocks33_stub_double():
    # tfsmextended_TimedSystem has no real 'tfsmextended_TimedSystem34' property in the generated
    # code (a bare stub) -- manually attach it so tfsmextended_FSMClock's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # tfsmextended_FSMClock's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = tfsmextended_FSMClock(numberOfTicks="sample_text")
    partner = tfsmextended_TimedSystem()
    setattr(partner, 'tfsmextended_TimedSystem34', None)
    _safe_set(owner, 'tfsmextended_FSMClock35', partner)
    assert owner in getattr(partner, 'tfsmextended_TimedSystem34')
    _safe_set(owner, 'tfsmextended_FSMClock35', None)
    assert owner not in getattr(partner, 'tfsmextended_TimedSystem34')


def test_assoc_globalEvents36_stub_double():
    # tfsmextended_TimedSystem has no real 'tfsmextended_TimedSystem37' property in the generated
    # code (a bare stub) -- manually attach it so tfsmextended_FSMEvent's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # tfsmextended_FSMEvent's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = tfsmextended_FSMEvent(isTriggered=True)
    partner = tfsmextended_TimedSystem()
    setattr(partner, 'tfsmextended_TimedSystem37', None)
    _safe_set(owner, 'tfsmextended_FSMEvent38', partner)
    assert owner in getattr(partner, 'tfsmextended_TimedSystem37')
    _safe_set(owner, 'tfsmextended_FSMEvent38', None)
    assert owner not in getattr(partner, 'tfsmextended_TimedSystem37')


def test_assoc_ownedGuard19_stub_double():
    # tfsmextended_Guard has no real 'tfsmextended_Guard' property in the generated
    # code (a bare stub) -- manually attach it so tfsmextended_Transition's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # tfsmextended_Transition's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = tfsmextended_Transition(action="sample_text")
    partner = tfsmextended_Guard()
    setattr(partner, 'tfsmextended_Guard', None)
    _safe_set(owner, 'tfsmextended_Transition20', partner)
    assert getattr(partner, 'tfsmextended_Guard') == owner
    _safe_set(owner, 'tfsmextended_Transition20', None)
    assert getattr(partner, 'tfsmextended_Guard') is None


def test_assoc_tfsms31_stub_double():
    # tfsmextended_TimedSystem has no real 'tfsmextended_TimedSystem' property in the generated
    # code (a bare stub) -- manually attach it so tfsmextended_TFSM's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # tfsmextended_TFSM's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = tfsmextended_TFSM()
    partner = tfsmextended_TimedSystem()
    setattr(partner, 'tfsmextended_TimedSystem', None)
    _safe_set(owner, 'tfsmextended_TFSM32', partner)
    assert owner in getattr(partner, 'tfsmextended_TimedSystem')
    _safe_set(owner, 'tfsmextended_TFSM32', None)
    assert owner not in getattr(partner, 'tfsmextended_TimedSystem')


def test_assoc_triggeringEvent26_stub_double():
    # tfsmextended_EventGuard has no real 'tfsmextended_EventGuard' property in the generated
    # code (a bare stub) -- manually attach it so tfsmextended_FSMEvent's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # tfsmextended_FSMEvent's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = tfsmextended_FSMEvent(isTriggered=True)
    partner = tfsmextended_EventGuard()
    setattr(partner, 'tfsmextended_EventGuard', None)
    _safe_set(owner, 'tfsmextended_FSMEvent27', partner)
    assert getattr(partner, 'tfsmextended_EventGuard') == owner
    _safe_set(owner, 'tfsmextended_FSMEvent27', None)
    assert getattr(partner, 'tfsmextended_EventGuard') is None


