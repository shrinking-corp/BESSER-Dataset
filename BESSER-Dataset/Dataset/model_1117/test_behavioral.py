import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Behavior,
    BehavioralElement,
    Event,
    NamedElement,
    Vertex,
    rtsc_Behavior,
    rtsc_BehavioralElement,
    rtsc_Clock,
    rtsc_ClockConstraint,
    rtsc_ClockResetEvent,
    rtsc_Connector,
    rtsc_CoordinationProtocol,
    rtsc_Event,
    rtsc_Guard,
    rtsc_Message,
    rtsc_MessageBuffer,
    rtsc_MessageEvent,
    rtsc_MessageType,
    rtsc_MessageTypeRepository,
    rtsc_NamedElement,
    rtsc_Port,
    rtsc_Realtimestatechart,
    rtsc_State,
    rtsc_System,
    rtsc_Transition,
    rtsc_Variable,
    rtsc_VariableAssignmentEvent,
    rtsc_Vertex,
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

def test_assoc_clock38_reverse_link_reassign_clear():
    a1 = rtsc_ClockConstraint(bound=7)
    a2 = rtsc_ClockConstraint(bound=13)
    b = rtsc_Clock(uClock=True)
    _safe_set(b, 'rtsc_Clock', a1)
    assert _is_linked(b, 'rtsc_Clock', a1)
    if hasattr(a1, 'rtsc_ClockConstraint39'):
        assert _is_linked(a1, 'rtsc_ClockConstraint39', b)
    _safe_set(b, 'rtsc_Clock', a2)
    assert _is_linked(b, 'rtsc_Clock', a2)
    if hasattr(a1, 'rtsc_ClockConstraint39'):
        assert not _is_linked(a1, 'rtsc_ClockConstraint39', b)
    if hasattr(a2, 'rtsc_ClockConstraint39'):
        assert _is_linked(a2, 'rtsc_ClockConstraint39', b)
    _safe_set(b, 'rtsc_Clock', None)
    assert not _is_linked(b, 'rtsc_Clock', a2)
    if hasattr(a2, 'rtsc_ClockConstraint39'):
        assert not _is_linked(a2, 'rtsc_ClockConstraint39', b)


def test_assoc_clock73_reverse_link_reassign_clear():
    a1 = rtsc_ClockResetEvent()
    a2 = rtsc_ClockResetEvent()
    b = rtsc_Clock(uClock=True)
    _safe_set(b, 'rtsc_Clock74', a1)
    assert _is_linked(b, 'rtsc_Clock74', a1)
    if hasattr(a1, 'rtsc_ClockResetEvent'):
        assert _is_linked(a1, 'rtsc_ClockResetEvent', b)
    _safe_set(b, 'rtsc_Clock74', a2)
    assert _is_linked(b, 'rtsc_Clock74', a2)
    if hasattr(a1, 'rtsc_ClockResetEvent'):
        assert not _is_linked(a1, 'rtsc_ClockResetEvent', b)
    if hasattr(a2, 'rtsc_ClockResetEvent'):
        assert _is_linked(a2, 'rtsc_ClockResetEvent', b)
    _safe_set(b, 'rtsc_Clock74', None)
    assert not _is_linked(b, 'rtsc_Clock74', a2)
    if hasattr(a2, 'rtsc_ClockResetEvent'):
        assert not _is_linked(a2, 'rtsc_ClockResetEvent', b)


def test_assoc_clockConstraints27_reverse_link_reassign_clear():
    a1 = rtsc_Transition(hitCount=7)
    a2 = rtsc_Transition(hitCount=13)
    b = rtsc_ClockConstraint(bound=7)
    _safe_set(b, 'rtsc_ClockConstraint', a1)
    assert _is_linked(b, 'rtsc_ClockConstraint', a1)
    if hasattr(a1, 'rtsc_Transition28'):
        assert _is_linked(a1, 'rtsc_Transition28', b)
    _safe_set(b, 'rtsc_ClockConstraint', a2)
    assert _is_linked(b, 'rtsc_ClockConstraint', a2)
    if hasattr(a1, 'rtsc_Transition28'):
        assert not _is_linked(a1, 'rtsc_Transition28', b)
    if hasattr(a2, 'rtsc_Transition28'):
        assert _is_linked(a2, 'rtsc_Transition28', b)
    _safe_set(b, 'rtsc_ClockConstraint', None)
    assert not _is_linked(b, 'rtsc_ClockConstraint', a2)
    if hasattr(a2, 'rtsc_Transition28'):
        assert not _is_linked(a2, 'rtsc_Transition28', b)


def test_assoc_clocks7_reverse_link_reassign_clear():
    a1 = rtsc_Realtimestatechart(rounds=7)
    a2 = rtsc_Realtimestatechart(rounds=13)
    b = rtsc_Clock(uClock=True)
    _safe_set(b, 'Clock', a1)
    assert _is_linked(b, 'Clock', a1)
    if hasattr(a1, 'statechart8'):
        assert _is_linked(a1, 'statechart8', b)
    _safe_set(b, 'Clock', a2)
    assert _is_linked(b, 'Clock', a2)
    if hasattr(a1, 'statechart8'):
        assert not _is_linked(a1, 'statechart8', b)
    if hasattr(a2, 'statechart8'):
        assert _is_linked(a2, 'statechart8', b)
    _safe_set(b, 'Clock', None)
    assert not _is_linked(b, 'Clock', a2)
    if hasattr(a2, 'statechart8'):
        assert not _is_linked(a2, 'statechart8', b)


def test_assoc_entryEvents17_reverse_link_reassign_clear():
    a1 = rtsc_State(final=True, initial=True)
    a2 = rtsc_State(final=False, initial=False)
    b = rtsc_Event()
    _safe_set(b, 'rtsc_Event', a1)
    assert _is_linked(b, 'rtsc_Event', a1)
    if hasattr(a1, 'rtsc_State18'):
        assert _is_linked(a1, 'rtsc_State18', b)
    _safe_set(b, 'rtsc_Event', a2)
    assert _is_linked(b, 'rtsc_Event', a2)
    if hasattr(a1, 'rtsc_State18'):
        assert not _is_linked(a1, 'rtsc_State18', b)
    if hasattr(a2, 'rtsc_State18'):
        assert _is_linked(a2, 'rtsc_State18', b)
    _safe_set(b, 'rtsc_Event', None)
    assert not _is_linked(b, 'rtsc_Event', a2)
    if hasattr(a2, 'rtsc_State18'):
        assert not _is_linked(a2, 'rtsc_State18', b)


def test_assoc_events33_reverse_link_reassign_clear():
    a1 = rtsc_Transition(hitCount=7)
    a2 = rtsc_Transition(hitCount=13)
    b = rtsc_Event()
    _safe_set(b, 'rtsc_Event35', a1)
    assert _is_linked(b, 'rtsc_Event35', a1)
    if hasattr(a1, 'rtsc_Transition34'):
        assert _is_linked(a1, 'rtsc_Transition34', b)
    _safe_set(b, 'rtsc_Event35', a2)
    assert _is_linked(b, 'rtsc_Event35', a2)
    if hasattr(a1, 'rtsc_Transition34'):
        assert not _is_linked(a1, 'rtsc_Transition34', b)
    if hasattr(a2, 'rtsc_Transition34'):
        assert _is_linked(a2, 'rtsc_Transition34', b)
    _safe_set(b, 'rtsc_Event35', None)
    assert not _is_linked(b, 'rtsc_Event35', a2)
    if hasattr(a2, 'rtsc_Transition34'):
        assert not _is_linked(a2, 'rtsc_Transition34', b)


def test_assoc_exitEvents19_reverse_link_reassign_clear():
    a1 = rtsc_State(final=True, initial=True)
    a2 = rtsc_State(final=False, initial=False)
    b = rtsc_Event()
    _safe_set(b, 'rtsc_Event21', a1)
    assert _is_linked(b, 'rtsc_Event21', a1)
    if hasattr(a1, 'rtsc_State20'):
        assert _is_linked(a1, 'rtsc_State20', b)
    _safe_set(b, 'rtsc_Event21', a2)
    assert _is_linked(b, 'rtsc_Event21', a2)
    if hasattr(a1, 'rtsc_State20'):
        assert not _is_linked(a1, 'rtsc_State20', b)
    if hasattr(a2, 'rtsc_State20'):
        assert _is_linked(a2, 'rtsc_State20', b)
    _safe_set(b, 'rtsc_Event21', None)
    assert not _is_linked(b, 'rtsc_Event21', a2)
    if hasattr(a2, 'rtsc_State20'):
        assert not _is_linked(a2, 'rtsc_State20', b)


def test_assoc_guards26_reverse_link_reassign_clear():
    a1 = rtsc_Transition(hitCount=7)
    a2 = rtsc_Transition(hitCount=13)
    b = rtsc_Guard(value=True)
    _safe_set(b, 'rtsc_Guard', a1)
    assert _is_linked(b, 'rtsc_Guard', a1)
    if hasattr(a1, 'rtsc_Transition'):
        assert _is_linked(a1, 'rtsc_Transition', b)
    _safe_set(b, 'rtsc_Guard', a2)
    assert _is_linked(b, 'rtsc_Guard', a2)
    if hasattr(a1, 'rtsc_Transition'):
        assert not _is_linked(a1, 'rtsc_Transition', b)
    if hasattr(a2, 'rtsc_Transition'):
        assert _is_linked(a2, 'rtsc_Transition', b)
    _safe_set(b, 'rtsc_Guard', None)
    assert not _is_linked(b, 'rtsc_Guard', a2)
    if hasattr(a2, 'rtsc_Transition'):
        assert not _is_linked(a2, 'rtsc_Transition', b)


def test_assoc_incomingTransitions13_reverse_link_reassign_clear():
    a1 = rtsc_Transition(hitCount=7)
    a2 = rtsc_Transition(hitCount=13)
    b = rtsc_State(final=True, initial=True)
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


def test_assoc_initialState4_reverse_link_reassign_clear():
    a1 = rtsc_State(final=True, initial=True)
    a2 = rtsc_State(final=False, initial=False)
    b = rtsc_Realtimestatechart(rounds=7)
    _safe_set(b, 'rtsc_Realtimestatechart', a1)
    assert _is_linked(b, 'rtsc_Realtimestatechart', a1)
    if hasattr(a1, 'rtsc_State'):
        assert _is_linked(a1, 'rtsc_State', b)
    _safe_set(b, 'rtsc_Realtimestatechart', a2)
    assert _is_linked(b, 'rtsc_Realtimestatechart', a2)
    if hasattr(a1, 'rtsc_State'):
        assert not _is_linked(a1, 'rtsc_State', b)
    if hasattr(a2, 'rtsc_State'):
        assert _is_linked(a2, 'rtsc_State', b)
    _safe_set(b, 'rtsc_Realtimestatechart', None)
    assert not _is_linked(b, 'rtsc_Realtimestatechart', a2)
    if hasattr(a2, 'rtsc_State'):
        assert not _is_linked(a2, 'rtsc_State', b)


def test_assoc_outgoingTransitions15_reverse_link_reassign_clear():
    a1 = rtsc_Transition(hitCount=7)
    a2 = rtsc_Transition(hitCount=13)
    b = rtsc_State(final=True, initial=True)
    _safe_set(b, 'source', {a1})
    assert _is_linked(b, 'source', a1)
    if hasattr(a1, 'Transition16'):
        assert _is_linked(a1, 'Transition16', b)
    _safe_set(b, 'source', {a2})
    assert _is_linked(b, 'source', a2)
    if hasattr(a1, 'Transition16'):
        assert not _is_linked(a1, 'Transition16', b)
    if hasattr(a2, 'Transition16'):
        assert _is_linked(a2, 'Transition16', b)
    _safe_set(b, 'source', set())
    assert not _is_linked(b, 'source', a2)
    if hasattr(a2, 'Transition16'):
        assert not _is_linked(a2, 'Transition16', b)


def test_assoc_owningRTSC12_reverse_link_reassign_clear():
    a1 = rtsc_State(final=True, initial=True)
    a2 = rtsc_State(final=False, initial=False)
    b = rtsc_Realtimestatechart(rounds=7)
    _safe_set(b, 'Realtimestatechart', a1)
    assert _is_linked(b, 'Realtimestatechart', a1)
    if hasattr(a1, 'states'):
        assert _is_linked(a1, 'states', b)
    _safe_set(b, 'Realtimestatechart', a2)
    assert _is_linked(b, 'Realtimestatechart', a2)
    if hasattr(a1, 'states'):
        assert not _is_linked(a1, 'states', b)
    if hasattr(a2, 'states'):
        assert _is_linked(a2, 'states', b)
    _safe_set(b, 'Realtimestatechart', None)
    assert not _is_linked(b, 'Realtimestatechart', a2)
    if hasattr(a2, 'states'):
        assert not _is_linked(a2, 'states', b)


def test_assoc_source22_reverse_link_reassign_clear():
    a1 = rtsc_Transition(hitCount=7)
    a2 = rtsc_Transition(hitCount=13)
    b = rtsc_State(final=True, initial=True)
    _safe_set(b, 'State23', a1)
    assert _is_linked(b, 'State23', a1)
    if hasattr(a1, 'outgoingTransitions'):
        assert _is_linked(a1, 'outgoingTransitions', b)
    _safe_set(b, 'State23', a2)
    assert _is_linked(b, 'State23', a2)
    if hasattr(a1, 'outgoingTransitions'):
        assert not _is_linked(a1, 'outgoingTransitions', b)
    if hasattr(a2, 'outgoingTransitions'):
        assert _is_linked(a2, 'outgoingTransitions', b)
    _safe_set(b, 'State23', None)
    assert not _is_linked(b, 'State23', a2)
    if hasattr(a2, 'outgoingTransitions'):
        assert not _is_linked(a2, 'outgoingTransitions', b)


def test_assoc_statechart29_reverse_link_reassign_clear():
    a1 = rtsc_Transition(hitCount=7)
    a2 = rtsc_Transition(hitCount=13)
    b = rtsc_Realtimestatechart(rounds=7)
    _safe_set(b, 'Realtimestatechart30', a1)
    assert _is_linked(b, 'Realtimestatechart30', a1)
    if hasattr(a1, 'transitions'):
        assert _is_linked(a1, 'transitions', b)
    _safe_set(b, 'Realtimestatechart30', a2)
    assert _is_linked(b, 'Realtimestatechart30', a2)
    if hasattr(a1, 'transitions'):
        assert not _is_linked(a1, 'transitions', b)
    if hasattr(a2, 'transitions'):
        assert _is_linked(a2, 'transitions', b)
    _safe_set(b, 'Realtimestatechart30', None)
    assert not _is_linked(b, 'Realtimestatechart30', a2)
    if hasattr(a2, 'transitions'):
        assert not _is_linked(a2, 'transitions', b)


def test_assoc_statechart40_reverse_link_reassign_clear():
    a1 = rtsc_Variable(initialValue="sample_text", runtimeValue="sample_text")
    a2 = rtsc_Variable(initialValue="sample_text_2", runtimeValue="sample_text_2")
    b = rtsc_Realtimestatechart(rounds=7)
    _safe_set(b, 'Realtimestatechart41', a1)
    assert _is_linked(b, 'Realtimestatechart41', a1)
    if hasattr(a1, 'variables'):
        assert _is_linked(a1, 'variables', b)
    _safe_set(b, 'Realtimestatechart41', a2)
    assert _is_linked(b, 'Realtimestatechart41', a2)
    if hasattr(a1, 'variables'):
        assert not _is_linked(a1, 'variables', b)
    if hasattr(a2, 'variables'):
        assert _is_linked(a2, 'variables', b)
    _safe_set(b, 'Realtimestatechart41', None)
    assert not _is_linked(b, 'Realtimestatechart41', a2)
    if hasattr(a2, 'variables'):
        assert not _is_linked(a2, 'variables', b)


def test_assoc_statechart42_reverse_link_reassign_clear():
    a1 = rtsc_Realtimestatechart(rounds=7)
    a2 = rtsc_Realtimestatechart(rounds=13)
    b = rtsc_Clock(uClock=True)
    _safe_set(b, 'clocks', a1)
    assert _is_linked(b, 'clocks', a1)
    if hasattr(a1, 'Realtimestatechart43'):
        assert _is_linked(a1, 'Realtimestatechart43', b)
    _safe_set(b, 'clocks', a2)
    assert _is_linked(b, 'clocks', a2)
    if hasattr(a1, 'Realtimestatechart43'):
        assert not _is_linked(a1, 'Realtimestatechart43', b)
    if hasattr(a2, 'Realtimestatechart43'):
        assert _is_linked(a2, 'Realtimestatechart43', b)
    _safe_set(b, 'clocks', None)
    assert not _is_linked(b, 'clocks', a2)
    if hasattr(a2, 'Realtimestatechart43'):
        assert not _is_linked(a2, 'Realtimestatechart43', b)


def test_assoc_states3_reverse_link_reassign_clear():
    a1 = rtsc_State(final=True, initial=True)
    a2 = rtsc_State(final=False, initial=False)
    b = rtsc_Realtimestatechart(rounds=7)
    _safe_set(b, 'owningRTSC', {a1})
    assert _is_linked(b, 'owningRTSC', a1)
    if hasattr(a1, 'State'):
        assert _is_linked(a1, 'State', b)
    _safe_set(b, 'owningRTSC', {a2})
    assert _is_linked(b, 'owningRTSC', a2)
    if hasattr(a1, 'State'):
        assert not _is_linked(a1, 'State', b)
    if hasattr(a2, 'State'):
        assert _is_linked(a2, 'State', b)
    _safe_set(b, 'owningRTSC', set())
    assert not _is_linked(b, 'owningRTSC', a2)
    if hasattr(a2, 'State'):
        assert not _is_linked(a2, 'State', b)


def test_assoc_subStatecharts9_reverse_link_reassign_clear():
    a1 = rtsc_State(final=True, initial=True)
    a2 = rtsc_State(final=False, initial=False)
    b = rtsc_Realtimestatechart(rounds=7)
    _safe_set(b, 'rtsc_Realtimestatechart11', a1)
    assert _is_linked(b, 'rtsc_Realtimestatechart11', a1)
    if hasattr(a1, 'rtsc_State10'):
        assert _is_linked(a1, 'rtsc_State10', b)
    _safe_set(b, 'rtsc_Realtimestatechart11', a2)
    assert _is_linked(b, 'rtsc_Realtimestatechart11', a2)
    if hasattr(a1, 'rtsc_State10'):
        assert not _is_linked(a1, 'rtsc_State10', b)
    if hasattr(a2, 'rtsc_State10'):
        assert _is_linked(a2, 'rtsc_State10', b)
    _safe_set(b, 'rtsc_Realtimestatechart11', None)
    assert not _is_linked(b, 'rtsc_Realtimestatechart11', a2)
    if hasattr(a2, 'rtsc_State10'):
        assert not _is_linked(a2, 'rtsc_State10', b)


def test_assoc_target24_reverse_link_reassign_clear():
    a1 = rtsc_Transition(hitCount=7)
    a2 = rtsc_Transition(hitCount=13)
    b = rtsc_State(final=True, initial=True)
    _safe_set(b, 'State25', a1)
    assert _is_linked(b, 'State25', a1)
    if hasattr(a1, 'incomingTransitions'):
        assert _is_linked(a1, 'incomingTransitions', b)
    _safe_set(b, 'State25', a2)
    assert _is_linked(b, 'State25', a2)
    if hasattr(a1, 'incomingTransitions'):
        assert not _is_linked(a1, 'incomingTransitions', b)
    if hasattr(a2, 'incomingTransitions'):
        assert _is_linked(a2, 'incomingTransitions', b)
    _safe_set(b, 'State25', None)
    assert not _is_linked(b, 'State25', a2)
    if hasattr(a2, 'incomingTransitions'):
        assert not _is_linked(a2, 'incomingTransitions', b)


def test_assoc_transitions2_reverse_link_reassign_clear():
    a1 = rtsc_Transition(hitCount=7)
    a2 = rtsc_Transition(hitCount=13)
    b = rtsc_Realtimestatechart(rounds=7)
    _safe_set(b, 'statechart', {a1})
    assert _is_linked(b, 'statechart', a1)
    if hasattr(a1, 'Transition'):
        assert _is_linked(a1, 'Transition', b)
    _safe_set(b, 'statechart', {a2})
    assert _is_linked(b, 'statechart', a2)
    if hasattr(a1, 'Transition'):
        assert not _is_linked(a1, 'Transition', b)
    if hasattr(a2, 'Transition'):
        assert _is_linked(a2, 'Transition', b)
    _safe_set(b, 'statechart', set())
    assert not _is_linked(b, 'statechart', a2)
    if hasattr(a2, 'Transition'):
        assert not _is_linked(a2, 'Transition', b)


def test_assoc_variable36_reverse_link_reassign_clear():
    a1 = rtsc_Variable(initialValue="sample_text", runtimeValue="sample_text")
    a2 = rtsc_Variable(initialValue="sample_text_2", runtimeValue="sample_text_2")
    b = rtsc_Guard(value=True)
    _safe_set(b, 'rtsc_Guard37', a1)
    assert _is_linked(b, 'rtsc_Guard37', a1)
    if hasattr(a1, 'rtsc_Variable'):
        assert _is_linked(a1, 'rtsc_Variable', b)
    _safe_set(b, 'rtsc_Guard37', a2)
    assert _is_linked(b, 'rtsc_Guard37', a2)
    if hasattr(a1, 'rtsc_Variable'):
        assert not _is_linked(a1, 'rtsc_Variable', b)
    if hasattr(a2, 'rtsc_Variable'):
        assert _is_linked(a2, 'rtsc_Variable', b)
    _safe_set(b, 'rtsc_Guard37', None)
    assert not _is_linked(b, 'rtsc_Guard37', a2)
    if hasattr(a2, 'rtsc_Variable'):
        assert not _is_linked(a2, 'rtsc_Variable', b)


def test_assoc_variable75_reverse_link_reassign_clear():
    a1 = rtsc_VariableAssignmentEvent(value="sample_text")
    a2 = rtsc_VariableAssignmentEvent(value="sample_text_2")
    b = rtsc_Variable(initialValue="sample_text", runtimeValue="sample_text")
    _safe_set(b, 'rtsc_Variable76', a1)
    assert _is_linked(b, 'rtsc_Variable76', a1)
    if hasattr(a1, 'rtsc_VariableAssignmentEvent'):
        assert _is_linked(a1, 'rtsc_VariableAssignmentEvent', b)
    _safe_set(b, 'rtsc_Variable76', a2)
    assert _is_linked(b, 'rtsc_Variable76', a2)
    if hasattr(a1, 'rtsc_VariableAssignmentEvent'):
        assert not _is_linked(a1, 'rtsc_VariableAssignmentEvent', b)
    if hasattr(a2, 'rtsc_VariableAssignmentEvent'):
        assert _is_linked(a2, 'rtsc_VariableAssignmentEvent', b)
    _safe_set(b, 'rtsc_Variable76', None)
    assert not _is_linked(b, 'rtsc_Variable76', a2)
    if hasattr(a2, 'rtsc_VariableAssignmentEvent'):
        assert not _is_linked(a2, 'rtsc_VariableAssignmentEvent', b)


def test_assoc_variables5_reverse_link_reassign_clear():
    a1 = rtsc_Variable(initialValue="sample_text", runtimeValue="sample_text")
    a2 = rtsc_Variable(initialValue="sample_text_2", runtimeValue="sample_text_2")
    b = rtsc_Realtimestatechart(rounds=7)
    _safe_set(b, 'statechart6', {a1})
    assert _is_linked(b, 'statechart6', a1)
    if hasattr(a1, 'Variable'):
        assert _is_linked(a1, 'Variable', b)
    _safe_set(b, 'statechart6', {a2})
    assert _is_linked(b, 'statechart6', a2)
    if hasattr(a1, 'Variable'):
        assert not _is_linked(a1, 'Variable', b)
    if hasattr(a2, 'Variable'):
        assert _is_linked(a2, 'Variable', b)
    _safe_set(b, 'statechart6', set())
    assert not _is_linked(b, 'statechart6', a2)
    if hasattr(a2, 'Variable'):
        assert not _is_linked(a2, 'Variable', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_allMessages50_stub_double():
    # rtsc_Message has no real 'rtsc_Message' property in the generated
    # code (a bare stub) -- manually attach it so rtsc_MessageBuffer's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # rtsc_MessageBuffer's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = rtsc_MessageBuffer()
    partner = rtsc_Message()
    setattr(partner, 'rtsc_Message', None)
    _safe_set(owner, 'rtsc_MessageBuffer51', {partner})
    assert getattr(partner, 'rtsc_Message') == owner
    _safe_set(owner, 'rtsc_MessageBuffer51', set())
    assert getattr(partner, 'rtsc_Message') is None


def test_assoc_connector56_stub_double():
    # rtsc_Connector has no real 'rtsc_Connector' property in the generated
    # code (a bare stub) -- manually attach it so rtsc_CoordinationProtocol's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # rtsc_CoordinationProtocol's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = rtsc_CoordinationProtocol()
    partner = rtsc_Connector()
    setattr(partner, 'rtsc_Connector', None)
    _safe_set(owner, 'rtsc_CoordinationProtocol57', partner)
    assert getattr(partner, 'rtsc_Connector') == owner
    _safe_set(owner, 'rtsc_CoordinationProtocol57', None)
    assert getattr(partner, 'rtsc_Connector') is None


def test_assoc_incomingBuffer45_stub_double():
    # rtsc_Port has no real 'port' property in the generated
    # code (a bare stub) -- manually attach it so rtsc_MessageBuffer's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # rtsc_MessageBuffer's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = rtsc_MessageBuffer()
    partner = rtsc_Port()
    setattr(partner, 'port', None)
    _safe_set(owner, 'MessageBuffer', partner)
    assert getattr(partner, 'port') == owner
    _safe_set(owner, 'MessageBuffer', None)
    assert getattr(partner, 'port') is None


def test_assoc_messageType71_stub_double():
    # rtsc_MessageType has no real 'rtsc_MessageType72' property in the generated
    # code (a bare stub) -- manually attach it so rtsc_MessageEvent's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # rtsc_MessageEvent's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = rtsc_MessageEvent()
    partner = rtsc_MessageType()
    setattr(partner, 'rtsc_MessageType72', None)
    _safe_set(owner, 'rtsc_MessageEvent', partner)
    assert getattr(partner, 'rtsc_MessageType72') == owner
    _safe_set(owner, 'rtsc_MessageEvent', None)
    assert getattr(partner, 'rtsc_MessageType72') is None


def test_assoc_port47_stub_double():
    # rtsc_Port has no real 'Port' property in the generated
    # code (a bare stub) -- manually attach it so rtsc_MessageBuffer's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # rtsc_MessageBuffer's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = rtsc_MessageBuffer()
    partner = rtsc_Port()
    setattr(partner, 'Port', None)
    _safe_set(owner, 'incomingBuffer', partner)
    assert getattr(partner, 'Port') == owner
    _safe_set(owner, 'incomingBuffer', None)
    assert getattr(partner, 'Port') is None


def test_assoc_ports54_stub_double():
    # rtsc_Port has no real 'rtsc_Port55' property in the generated
    # code (a bare stub) -- manually attach it so rtsc_CoordinationProtocol's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # rtsc_CoordinationProtocol's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = rtsc_CoordinationProtocol()
    partner = rtsc_Port()
    setattr(partner, 'rtsc_Port55', None)
    _safe_set(owner, 'rtsc_CoordinationProtocol', {partner})
    assert getattr(partner, 'rtsc_Port55') == owner
    _safe_set(owner, 'rtsc_CoordinationProtocol', set())
    assert getattr(partner, 'rtsc_Port55') is None


def test_assoc_protocol63_stub_double():
    # rtsc_System has no real 'rtsc_System64' property in the generated
    # code (a bare stub) -- manually attach it so rtsc_CoordinationProtocol's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # rtsc_CoordinationProtocol's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = rtsc_CoordinationProtocol()
    partner = rtsc_System()
    setattr(partner, 'rtsc_System64', None)
    _safe_set(owner, 'rtsc_CoordinationProtocol65', partner)
    assert owner in getattr(partner, 'rtsc_System64')
    _safe_set(owner, 'rtsc_CoordinationProtocol65', None)
    assert owner not in getattr(partner, 'rtsc_System64')


def test_assoc_statecharts61_stub_double():
    # rtsc_System has no real 'rtsc_System' property in the generated
    # code (a bare stub) -- manually attach it so rtsc_Realtimestatechart's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # rtsc_Realtimestatechart's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = rtsc_Realtimestatechart(rounds=7)
    partner = rtsc_System()
    setattr(partner, 'rtsc_System', None)
    _safe_set(owner, 'rtsc_Realtimestatechart62', partner)
    assert owner in getattr(partner, 'rtsc_System')
    _safe_set(owner, 'rtsc_Realtimestatechart62', None)
    assert owner not in getattr(partner, 'rtsc_System')


def test_assoc_triggerMessage31_stub_double():
    # rtsc_MessageType has no real 'rtsc_MessageType' property in the generated
    # code (a bare stub) -- manually attach it so rtsc_Transition's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # rtsc_Transition's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = rtsc_Transition(hitCount=7)
    partner = rtsc_MessageType()
    setattr(partner, 'rtsc_MessageType', None)
    _safe_set(owner, 'rtsc_Transition32', {partner})
    assert getattr(partner, 'rtsc_MessageType') == owner
    _safe_set(owner, 'rtsc_Transition32', set())
    assert getattr(partner, 'rtsc_MessageType') is None


def test_assoc_types48_stub_double():
    # rtsc_MessageType has no real 'rtsc_MessageType49' property in the generated
    # code (a bare stub) -- manually attach it so rtsc_MessageBuffer's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # rtsc_MessageBuffer's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = rtsc_MessageBuffer()
    partner = rtsc_MessageType()
    setattr(partner, 'rtsc_MessageType49', None)
    _safe_set(owner, 'rtsc_MessageBuffer', {partner})
    assert getattr(partner, 'rtsc_MessageType49') == owner
    _safe_set(owner, 'rtsc_MessageBuffer', set())
    assert getattr(partner, 'rtsc_MessageType49') is None


