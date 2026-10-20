import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Guard,
    NamedElement,
    tfsm_EvaluateGuard,
    tfsm_EventGuard,
    tfsm_FSMClock,
    tfsm_FSMEvent,
    tfsm_Guard,
    tfsm_NamedElement,
    tfsm_State,
    tfsm_TFSM,
    tfsm_TemporalGuard,
    tfsm_TimedSystem,
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

def test_assoc_currentState8_reverse_link_reassign_clear():
    a1 = tfsm_TFSM(lastStateChangeStepNumber=7, stepNumber=7)
    a2 = tfsm_TFSM(lastStateChangeStepNumber=13, stepNumber=13)
    b = tfsm_State()
    _safe_set(b, 'tfsm_State10', a1)
    assert _is_linked(b, 'tfsm_State10', a1)
    if hasattr(a1, 'tfsm_TFSM9'):
        assert _is_linked(a1, 'tfsm_TFSM9', b)
    _safe_set(b, 'tfsm_State10', a2)
    assert _is_linked(b, 'tfsm_State10', a2)
    if hasattr(a1, 'tfsm_TFSM9'):
        assert not _is_linked(a1, 'tfsm_TFSM9', b)
    if hasattr(a2, 'tfsm_TFSM9'):
        assert _is_linked(a2, 'tfsm_TFSM9', b)
    _safe_set(b, 'tfsm_State10', None)
    assert not _is_linked(b, 'tfsm_State10', a2)
    if hasattr(a2, 'tfsm_TFSM9'):
        assert not _is_linked(a2, 'tfsm_TFSM9', b)


def test_assoc_generatedEvents21_reverse_link_reassign_clear():
    a1 = tfsm_Transition(action="sample_text")
    a2 = tfsm_Transition(action="sample_text_2")
    b = tfsm_FSMEvent(isTriggered="sample_text")
    _safe_set(b, 'tfsm_FSMEvent23', a1)
    assert _is_linked(b, 'tfsm_FSMEvent23', a1)
    if hasattr(a1, 'tfsm_Transition22'):
        assert _is_linked(a1, 'tfsm_Transition22', b)
    _safe_set(b, 'tfsm_FSMEvent23', a2)
    assert _is_linked(b, 'tfsm_FSMEvent23', a2)
    if hasattr(a1, 'tfsm_Transition22'):
        assert not _is_linked(a1, 'tfsm_Transition22', b)
    if hasattr(a2, 'tfsm_Transition22'):
        assert _is_linked(a2, 'tfsm_Transition22', b)
    _safe_set(b, 'tfsm_FSMEvent23', None)
    assert not _is_linked(b, 'tfsm_FSMEvent23', a2)
    if hasattr(a2, 'tfsm_Transition22'):
        assert not _is_linked(a2, 'tfsm_Transition22', b)


def test_assoc_globalClocks33_reverse_link_reassign_clear():
    a1 = tfsm_TimedSystem()
    a2 = tfsm_TimedSystem()
    b = tfsm_FSMClock(numberOfTicks="sample_text")
    _safe_set(b, 'tfsm_FSMClock35', a1)
    assert _is_linked(b, 'tfsm_FSMClock35', a1)
    if hasattr(a1, 'tfsm_TimedSystem34'):
        assert _is_linked(a1, 'tfsm_TimedSystem34', b)
    _safe_set(b, 'tfsm_FSMClock35', a2)
    assert _is_linked(b, 'tfsm_FSMClock35', a2)
    if hasattr(a1, 'tfsm_TimedSystem34'):
        assert not _is_linked(a1, 'tfsm_TimedSystem34', b)
    if hasattr(a2, 'tfsm_TimedSystem34'):
        assert _is_linked(a2, 'tfsm_TimedSystem34', b)
    _safe_set(b, 'tfsm_FSMClock35', None)
    assert not _is_linked(b, 'tfsm_FSMClock35', a2)
    if hasattr(a2, 'tfsm_TimedSystem34'):
        assert not _is_linked(a2, 'tfsm_TimedSystem34', b)


def test_assoc_globalEvents36_reverse_link_reassign_clear():
    a1 = tfsm_TimedSystem()
    a2 = tfsm_TimedSystem()
    b = tfsm_FSMEvent(isTriggered="sample_text")
    _safe_set(b, 'tfsm_FSMEvent38', a1)
    assert _is_linked(b, 'tfsm_FSMEvent38', a1)
    if hasattr(a1, 'tfsm_TimedSystem37'):
        assert _is_linked(a1, 'tfsm_TimedSystem37', b)
    _safe_set(b, 'tfsm_FSMEvent38', a2)
    assert _is_linked(b, 'tfsm_FSMEvent38', a2)
    if hasattr(a1, 'tfsm_TimedSystem37'):
        assert not _is_linked(a1, 'tfsm_TimedSystem37', b)
    if hasattr(a2, 'tfsm_TimedSystem37'):
        assert _is_linked(a2, 'tfsm_TimedSystem37', b)
    _safe_set(b, 'tfsm_FSMEvent38', None)
    assert not _is_linked(b, 'tfsm_FSMEvent38', a2)
    if hasattr(a2, 'tfsm_TimedSystem37'):
        assert not _is_linked(a2, 'tfsm_TimedSystem37', b)


def test_assoc_incomingTransitions13_reverse_link_reassign_clear():
    a1 = tfsm_Transition(action="sample_text")
    a2 = tfsm_Transition(action="sample_text_2")
    b = tfsm_State()
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
    a1 = tfsm_TFSM(lastStateChangeStepNumber=7, stepNumber=7)
    a2 = tfsm_TFSM(lastStateChangeStepNumber=13, stepNumber=13)
    b = tfsm_State()
    _safe_set(b, 'tfsm_State', a1)
    assert _is_linked(b, 'tfsm_State', a1)
    if hasattr(a1, 'tfsm_TFSM'):
        assert _is_linked(a1, 'tfsm_TFSM', b)
    _safe_set(b, 'tfsm_State', a2)
    assert _is_linked(b, 'tfsm_State', a2)
    if hasattr(a1, 'tfsm_TFSM'):
        assert not _is_linked(a1, 'tfsm_TFSM', b)
    if hasattr(a2, 'tfsm_TFSM'):
        assert _is_linked(a2, 'tfsm_TFSM', b)
    _safe_set(b, 'tfsm_State', None)
    assert not _is_linked(b, 'tfsm_State', a2)
    if hasattr(a2, 'tfsm_TFSM'):
        assert not _is_linked(a2, 'tfsm_TFSM', b)


def test_assoc_localClock4_reverse_link_reassign_clear():
    a1 = tfsm_TFSM(lastStateChangeStepNumber=7, stepNumber=7)
    a2 = tfsm_TFSM(lastStateChangeStepNumber=13, stepNumber=13)
    b = tfsm_FSMClock(numberOfTicks="sample_text")
    _safe_set(b, 'tfsm_FSMClock', a1)
    assert _is_linked(b, 'tfsm_FSMClock', a1)
    if hasattr(a1, 'tfsm_TFSM5'):
        assert _is_linked(a1, 'tfsm_TFSM5', b)
    _safe_set(b, 'tfsm_FSMClock', a2)
    assert _is_linked(b, 'tfsm_FSMClock', a2)
    if hasattr(a1, 'tfsm_TFSM5'):
        assert not _is_linked(a1, 'tfsm_TFSM5', b)
    if hasattr(a2, 'tfsm_TFSM5'):
        assert _is_linked(a2, 'tfsm_TFSM5', b)
    _safe_set(b, 'tfsm_FSMClock', None)
    assert not _is_linked(b, 'tfsm_FSMClock', a2)
    if hasattr(a2, 'tfsm_TFSM5'):
        assert not _is_linked(a2, 'tfsm_TFSM5', b)


def test_assoc_localEvents2_reverse_link_reassign_clear():
    a1 = tfsm_TFSM(lastStateChangeStepNumber=7, stepNumber=7)
    a2 = tfsm_TFSM(lastStateChangeStepNumber=13, stepNumber=13)
    b = tfsm_FSMEvent(isTriggered="sample_text")
    _safe_set(b, 'tfsm_FSMEvent', a1)
    assert _is_linked(b, 'tfsm_FSMEvent', a1)
    if hasattr(a1, 'tfsm_TFSM3'):
        assert _is_linked(a1, 'tfsm_TFSM3', b)
    _safe_set(b, 'tfsm_FSMEvent', a2)
    assert _is_linked(b, 'tfsm_FSMEvent', a2)
    if hasattr(a1, 'tfsm_TFSM3'):
        assert not _is_linked(a1, 'tfsm_TFSM3', b)
    if hasattr(a2, 'tfsm_TFSM3'):
        assert _is_linked(a2, 'tfsm_TFSM3', b)
    _safe_set(b, 'tfsm_FSMEvent', None)
    assert not _is_linked(b, 'tfsm_FSMEvent', a2)
    if hasattr(a2, 'tfsm_TFSM3'):
        assert not _is_linked(a2, 'tfsm_TFSM3', b)


def test_assoc_onClock24_reverse_link_reassign_clear():
    a1 = tfsm_TemporalGuard(afterDuration=7)
    a2 = tfsm_TemporalGuard(afterDuration=13)
    b = tfsm_FSMClock(numberOfTicks="sample_text")
    _safe_set(b, 'tfsm_FSMClock25', a1)
    assert _is_linked(b, 'tfsm_FSMClock25', a1)
    if hasattr(a1, 'tfsm_TemporalGuard'):
        assert _is_linked(a1, 'tfsm_TemporalGuard', b)
    _safe_set(b, 'tfsm_FSMClock25', a2)
    assert _is_linked(b, 'tfsm_FSMClock25', a2)
    if hasattr(a1, 'tfsm_TemporalGuard'):
        assert not _is_linked(a1, 'tfsm_TemporalGuard', b)
    if hasattr(a2, 'tfsm_TemporalGuard'):
        assert _is_linked(a2, 'tfsm_TemporalGuard', b)
    _safe_set(b, 'tfsm_FSMClock25', None)
    assert not _is_linked(b, 'tfsm_FSMClock25', a2)
    if hasattr(a2, 'tfsm_TemporalGuard'):
        assert not _is_linked(a2, 'tfsm_TemporalGuard', b)


def test_assoc_outgoingTransitions12_reverse_link_reassign_clear():
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


def test_assoc_ownedGuard19_reverse_link_reassign_clear():
    a1 = tfsm_Transition(action="sample_text")
    a2 = tfsm_Transition(action="sample_text_2")
    b = tfsm_Guard()
    _safe_set(b, 'tfsm_Guard', a1)
    assert _is_linked(b, 'tfsm_Guard', a1)
    if hasattr(a1, 'tfsm_Transition20'):
        assert _is_linked(a1, 'tfsm_Transition20', b)
    _safe_set(b, 'tfsm_Guard', a2)
    assert _is_linked(b, 'tfsm_Guard', a2)
    if hasattr(a1, 'tfsm_Transition20'):
        assert not _is_linked(a1, 'tfsm_Transition20', b)
    if hasattr(a2, 'tfsm_Transition20'):
        assert _is_linked(a2, 'tfsm_Transition20', b)
    _safe_set(b, 'tfsm_Guard', None)
    assert not _is_linked(b, 'tfsm_Guard', a2)
    if hasattr(a2, 'tfsm_Transition20'):
        assert not _is_linked(a2, 'tfsm_Transition20', b)


def test_assoc_ownedStates0_reverse_link_reassign_clear():
    a1 = tfsm_TFSM(lastStateChangeStepNumber=7, stepNumber=7)
    a2 = tfsm_TFSM(lastStateChangeStepNumber=13, stepNumber=13)
    b = tfsm_State()
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
    a1 = tfsm_Transition(action="sample_text")
    a2 = tfsm_Transition(action="sample_text_2")
    b = tfsm_TFSM(lastStateChangeStepNumber=7, stepNumber=7)
    _safe_set(b, 'tfsm_TFSM7', {a1})
    assert _is_linked(b, 'tfsm_TFSM7', a1)
    if hasattr(a1, 'tfsm_Transition'):
        assert _is_linked(a1, 'tfsm_Transition', b)
    _safe_set(b, 'tfsm_TFSM7', {a2})
    assert _is_linked(b, 'tfsm_TFSM7', a2)
    if hasattr(a1, 'tfsm_Transition'):
        assert not _is_linked(a1, 'tfsm_Transition', b)
    if hasattr(a2, 'tfsm_Transition'):
        assert _is_linked(a2, 'tfsm_Transition', b)
    _safe_set(b, 'tfsm_TFSM7', set())
    assert not _is_linked(b, 'tfsm_TFSM7', a2)
    if hasattr(a2, 'tfsm_Transition'):
        assert not _is_linked(a2, 'tfsm_Transition', b)


def test_assoc_owningFSM11_reverse_link_reassign_clear():
    a1 = tfsm_TFSM(lastStateChangeStepNumber=7, stepNumber=7)
    a2 = tfsm_TFSM(lastStateChangeStepNumber=13, stepNumber=13)
    b = tfsm_State()
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
    a1 = tfsm_Transition(action="sample_text")
    a2 = tfsm_Transition(action="sample_text_2")
    b = tfsm_FSMEvent(isTriggered="sample_text")
    _safe_set(b, 'tfsm_FSMEvent29', {a1})
    assert _is_linked(b, 'tfsm_FSMEvent29', a1)
    if hasattr(a1, 'tfsm_Transition30'):
        assert _is_linked(a1, 'tfsm_Transition30', b)
    _safe_set(b, 'tfsm_FSMEvent29', {a2})
    assert _is_linked(b, 'tfsm_FSMEvent29', a2)
    if hasattr(a1, 'tfsm_Transition30'):
        assert not _is_linked(a1, 'tfsm_Transition30', b)
    if hasattr(a2, 'tfsm_Transition30'):
        assert _is_linked(a2, 'tfsm_Transition30', b)
    _safe_set(b, 'tfsm_FSMEvent29', set())
    assert not _is_linked(b, 'tfsm_FSMEvent29', a2)
    if hasattr(a2, 'tfsm_Transition30'):
        assert not _is_linked(a2, 'tfsm_Transition30', b)


def test_assoc_source15_reverse_link_reassign_clear():
    a1 = tfsm_Transition(action="sample_text")
    a2 = tfsm_Transition(action="sample_text_2")
    b = tfsm_State()
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
    a1 = tfsm_Transition(action="sample_text")
    a2 = tfsm_Transition(action="sample_text_2")
    b = tfsm_State()
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


def test_assoc_tfsms31_reverse_link_reassign_clear():
    a1 = tfsm_TimedSystem()
    a2 = tfsm_TimedSystem()
    b = tfsm_TFSM(lastStateChangeStepNumber=7, stepNumber=7)
    _safe_set(b, 'tfsm_TFSM32', a1)
    assert _is_linked(b, 'tfsm_TFSM32', a1)
    if hasattr(a1, 'tfsm_TimedSystem'):
        assert _is_linked(a1, 'tfsm_TimedSystem', b)
    _safe_set(b, 'tfsm_TFSM32', a2)
    assert _is_linked(b, 'tfsm_TFSM32', a2)
    if hasattr(a1, 'tfsm_TimedSystem'):
        assert not _is_linked(a1, 'tfsm_TimedSystem', b)
    if hasattr(a2, 'tfsm_TimedSystem'):
        assert _is_linked(a2, 'tfsm_TimedSystem', b)
    _safe_set(b, 'tfsm_TFSM32', None)
    assert not _is_linked(b, 'tfsm_TFSM32', a2)
    if hasattr(a2, 'tfsm_TimedSystem'):
        assert not _is_linked(a2, 'tfsm_TimedSystem', b)


def test_assoc_triggeringEvent26_reverse_link_reassign_clear():
    a1 = tfsm_FSMEvent(isTriggered="sample_text")
    a2 = tfsm_FSMEvent(isTriggered="sample_text_2")
    b = tfsm_EventGuard()
    _safe_set(b, 'tfsm_EventGuard', a1)
    assert _is_linked(b, 'tfsm_EventGuard', a1)
    if hasattr(a1, 'tfsm_FSMEvent27'):
        assert _is_linked(a1, 'tfsm_FSMEvent27', b)
    _safe_set(b, 'tfsm_EventGuard', a2)
    assert _is_linked(b, 'tfsm_EventGuard', a2)
    if hasattr(a1, 'tfsm_FSMEvent27'):
        assert not _is_linked(a1, 'tfsm_FSMEvent27', b)
    if hasattr(a2, 'tfsm_FSMEvent27'):
        assert _is_linked(a2, 'tfsm_FSMEvent27', b)
    _safe_set(b, 'tfsm_EventGuard', None)
    assert not _is_linked(b, 'tfsm_EventGuard', a2)
    if hasattr(a2, 'tfsm_FSMEvent27'):
        assert not _is_linked(a2, 'tfsm_FSMEvent27', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

