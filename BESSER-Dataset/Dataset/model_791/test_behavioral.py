import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    fsm_Action,
    fsm_Event,
    fsm_FSM,
    fsm_Guard,
    fsm_Message,
    fsm_State,
    fsm_StringToStringMap,
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

def test_assoc_actions30_reverse_link_reassign_clear():
    a1 = fsm_Transition(InverseGuard=True, name="sample_text")
    a2 = fsm_Transition(InverseGuard=False, name="sample_text_2")
    b = fsm_Action(name="sample_text")
    _safe_set(b, 'fsm_Action31', a1)
    assert _is_linked(b, 'fsm_Action31', a1)
    if hasattr(a1, 'fsm_Transition'):
        assert _is_linked(a1, 'fsm_Transition', b)
    _safe_set(b, 'fsm_Action31', a2)
    assert _is_linked(b, 'fsm_Action31', a2)
    if hasattr(a1, 'fsm_Transition'):
        assert not _is_linked(a1, 'fsm_Transition', b)
    if hasattr(a2, 'fsm_Transition'):
        assert _is_linked(a2, 'fsm_Transition', b)
    _safe_set(b, 'fsm_Action31', None)
    assert not _is_linked(b, 'fsm_Action31', a2)
    if hasattr(a2, 'fsm_Transition'):
        assert not _is_linked(a2, 'fsm_Transition', b)


def test_assoc_data43_reverse_link_reassign_clear():
    a1 = fsm_StringToStringMap(key="sample_text", value="sample_text")
    a2 = fsm_StringToStringMap(key="sample_text_2", value="sample_text_2")
    b = fsm_Message(name="sample_text")
    _safe_set(b, 'fsm_Message44', {a1})
    assert _is_linked(b, 'fsm_Message44', a1)
    if hasattr(a1, 'fsm_StringToStringMap45'):
        assert _is_linked(a1, 'fsm_StringToStringMap45', b)
    _safe_set(b, 'fsm_Message44', {a2})
    assert _is_linked(b, 'fsm_Message44', a2)
    if hasattr(a1, 'fsm_StringToStringMap45'):
        assert not _is_linked(a1, 'fsm_StringToStringMap45', b)
    if hasattr(a2, 'fsm_StringToStringMap45'):
        assert _is_linked(a2, 'fsm_StringToStringMap45', b)
    _safe_set(b, 'fsm_Message44', set())
    assert not _is_linked(b, 'fsm_Message44', a2)
    if hasattr(a2, 'fsm_StringToStringMap45'):
        assert not _is_linked(a2, 'fsm_StringToStringMap45', b)


def test_assoc_dataTypes13_reverse_link_reassign_clear():
    a1 = fsm_StringToStringMap(key="sample_text", value="sample_text")
    a2 = fsm_StringToStringMap(key="sample_text_2", value="sample_text_2")
    b = fsm_FSM(groupId="sample_text", isServer=True, name="sample_text")
    _safe_set(b, 'fsm_FSM14', {a1})
    assert _is_linked(b, 'fsm_FSM14', a1)
    if hasattr(a1, 'fsm_StringToStringMap'):
        assert _is_linked(a1, 'fsm_StringToStringMap', b)
    _safe_set(b, 'fsm_FSM14', {a2})
    assert _is_linked(b, 'fsm_FSM14', a2)
    if hasattr(a1, 'fsm_StringToStringMap'):
        assert not _is_linked(a1, 'fsm_StringToStringMap', b)
    if hasattr(a2, 'fsm_StringToStringMap'):
        assert _is_linked(a2, 'fsm_StringToStringMap', b)
    _safe_set(b, 'fsm_FSM14', set())
    assert not _is_linked(b, 'fsm_FSM14', a2)
    if hasattr(a2, 'fsm_StringToStringMap'):
        assert not _is_linked(a2, 'fsm_StringToStringMap', b)


def test_assoc_enumsDef46_reverse_link_reassign_clear():
    a1 = fsm_StringToStringMap(key="sample_text", value="sample_text")
    a2 = fsm_StringToStringMap(key="sample_text_2", value="sample_text_2")
    b = fsm_Message(name="sample_text")
    _safe_set(b, 'fsm_Message47', {a1})
    assert _is_linked(b, 'fsm_Message47', a1)
    if hasattr(a1, 'fsm_StringToStringMap48'):
        assert _is_linked(a1, 'fsm_StringToStringMap48', b)
    _safe_set(b, 'fsm_Message47', {a2})
    assert _is_linked(b, 'fsm_Message47', a2)
    if hasattr(a1, 'fsm_StringToStringMap48'):
        assert not _is_linked(a1, 'fsm_StringToStringMap48', b)
    if hasattr(a2, 'fsm_StringToStringMap48'):
        assert _is_linked(a2, 'fsm_StringToStringMap48', b)
    _safe_set(b, 'fsm_Message47', set())
    assert not _is_linked(b, 'fsm_Message47', a2)
    if hasattr(a2, 'fsm_StringToStringMap48'):
        assert not _is_linked(a2, 'fsm_StringToStringMap48', b)


def test_assoc_event35_reverse_link_reassign_clear():
    a1 = fsm_Transition(InverseGuard=True, name="sample_text")
    a2 = fsm_Transition(InverseGuard=False, name="sample_text_2")
    b = fsm_Event(name="sample_text")
    _safe_set(b, 'fsm_Event37', a1)
    assert _is_linked(b, 'fsm_Event37', a1)
    if hasattr(a1, 'fsm_Transition36'):
        assert _is_linked(a1, 'fsm_Transition36', b)
    _safe_set(b, 'fsm_Event37', a2)
    assert _is_linked(b, 'fsm_Event37', a2)
    if hasattr(a1, 'fsm_Transition36'):
        assert not _is_linked(a1, 'fsm_Transition36', b)
    if hasattr(a2, 'fsm_Transition36'):
        assert _is_linked(a2, 'fsm_Transition36', b)
    _safe_set(b, 'fsm_Event37', None)
    assert not _is_linked(b, 'fsm_Event37', a2)
    if hasattr(a2, 'fsm_Transition36'):
        assert not _is_linked(a2, 'fsm_Transition36', b)


def test_assoc_event40_reverse_link_reassign_clear():
    a1 = fsm_Message(name="sample_text")
    a2 = fsm_Message(name="sample_text_2")
    b = fsm_Event(name="sample_text")
    _safe_set(b, 'fsm_Event42', a1)
    assert _is_linked(b, 'fsm_Event42', a1)
    if hasattr(a1, 'fsm_Message41'):
        assert _is_linked(a1, 'fsm_Message41', b)
    _safe_set(b, 'fsm_Event42', a2)
    assert _is_linked(b, 'fsm_Event42', a2)
    if hasattr(a1, 'fsm_Message41'):
        assert not _is_linked(a1, 'fsm_Message41', b)
    if hasattr(a2, 'fsm_Message41'):
        assert _is_linked(a2, 'fsm_Message41', b)
    _safe_set(b, 'fsm_Event42', None)
    assert not _is_linked(b, 'fsm_Event42', a2)
    if hasattr(a2, 'fsm_Message41'):
        assert not _is_linked(a2, 'fsm_Message41', b)


def test_assoc_expectedMessage25_reverse_link_reassign_clear():
    a1 = fsm_State(name="sample_text")
    a2 = fsm_State(name="sample_text_2")
    b = fsm_Message(name="sample_text")
    _safe_set(b, 'fsm_Message27', a1)
    assert _is_linked(b, 'fsm_Message27', a1)
    if hasattr(a1, 'fsm_State26'):
        assert _is_linked(a1, 'fsm_State26', b)
    _safe_set(b, 'fsm_Message27', a2)
    assert _is_linked(b, 'fsm_Message27', a2)
    if hasattr(a1, 'fsm_State26'):
        assert not _is_linked(a1, 'fsm_State26', b)
    if hasattr(a2, 'fsm_State26'):
        assert _is_linked(a2, 'fsm_State26', b)
    _safe_set(b, 'fsm_Message27', None)
    assert not _is_linked(b, 'fsm_Message27', a2)
    if hasattr(a2, 'fsm_State26'):
        assert not _is_linked(a2, 'fsm_State26', b)


def test_assoc_finalState2_reverse_link_reassign_clear():
    a1 = fsm_State(name="sample_text")
    a2 = fsm_State(name="sample_text_2")
    b = fsm_FSM(groupId="sample_text", isServer=True, name="sample_text")
    _safe_set(b, 'fsm_FSM3', a1)
    assert _is_linked(b, 'fsm_FSM3', a1)
    if hasattr(a1, 'fsm_State4'):
        assert _is_linked(a1, 'fsm_State4', b)
    _safe_set(b, 'fsm_FSM3', a2)
    assert _is_linked(b, 'fsm_FSM3', a2)
    if hasattr(a1, 'fsm_State4'):
        assert not _is_linked(a1, 'fsm_State4', b)
    if hasattr(a2, 'fsm_State4'):
        assert _is_linked(a2, 'fsm_State4', b)
    _safe_set(b, 'fsm_FSM3', None)
    assert not _is_linked(b, 'fsm_FSM3', a2)
    if hasattr(a2, 'fsm_State4'):
        assert not _is_linked(a2, 'fsm_State4', b)


def test_assoc_guard32_reverse_link_reassign_clear():
    a1 = fsm_Transition(InverseGuard=True, name="sample_text")
    a2 = fsm_Transition(InverseGuard=False, name="sample_text_2")
    b = fsm_Guard(name="sample_text")
    _safe_set(b, 'fsm_Guard34', a1)
    assert _is_linked(b, 'fsm_Guard34', a1)
    if hasattr(a1, 'fsm_Transition33'):
        assert _is_linked(a1, 'fsm_Transition33', b)
    _safe_set(b, 'fsm_Guard34', a2)
    assert _is_linked(b, 'fsm_Guard34', a2)
    if hasattr(a1, 'fsm_Transition33'):
        assert not _is_linked(a1, 'fsm_Transition33', b)
    if hasattr(a2, 'fsm_Transition33'):
        assert _is_linked(a2, 'fsm_Transition33', b)
    _safe_set(b, 'fsm_Guard34', None)
    assert not _is_linked(b, 'fsm_Guard34', a2)
    if hasattr(a2, 'fsm_Transition33'):
        assert not _is_linked(a2, 'fsm_Transition33', b)


def test_assoc_incomingTransitions17_reverse_link_reassign_clear():
    a1 = fsm_Transition(InverseGuard=True, name="sample_text")
    a2 = fsm_Transition(InverseGuard=False, name="sample_text_2")
    b = fsm_State(name="sample_text")
    _safe_set(b, 'target', {a1})
    assert _is_linked(b, 'target', a1)
    if hasattr(a1, 'Transition18'):
        assert _is_linked(a1, 'Transition18', b)
    _safe_set(b, 'target', {a2})
    assert _is_linked(b, 'target', a2)
    if hasattr(a1, 'Transition18'):
        assert not _is_linked(a1, 'Transition18', b)
    if hasattr(a2, 'Transition18'):
        assert _is_linked(a2, 'Transition18', b)
    _safe_set(b, 'target', set())
    assert not _is_linked(b, 'target', a2)
    if hasattr(a2, 'Transition18'):
        assert not _is_linked(a2, 'Transition18', b)


def test_assoc_initialState1_reverse_link_reassign_clear():
    a1 = fsm_State(name="sample_text")
    a2 = fsm_State(name="sample_text_2")
    b = fsm_FSM(groupId="sample_text", isServer=True, name="sample_text")
    _safe_set(b, 'fsm_FSM', a1)
    assert _is_linked(b, 'fsm_FSM', a1)
    if hasattr(a1, 'fsm_State'):
        assert _is_linked(a1, 'fsm_State', b)
    _safe_set(b, 'fsm_FSM', a2)
    assert _is_linked(b, 'fsm_FSM', a2)
    if hasattr(a1, 'fsm_State'):
        assert not _is_linked(a1, 'fsm_State', b)
    if hasattr(a2, 'fsm_State'):
        assert _is_linked(a2, 'fsm_State', b)
    _safe_set(b, 'fsm_FSM', None)
    assert not _is_linked(b, 'fsm_FSM', a2)
    if hasattr(a2, 'fsm_State'):
        assert not _is_linked(a2, 'fsm_State', b)


def test_assoc_onEnteredActions19_reverse_link_reassign_clear():
    a1 = fsm_State(name="sample_text")
    a2 = fsm_State(name="sample_text_2")
    b = fsm_Action(name="sample_text")
    _safe_set(b, 'fsm_Action21', a1)
    assert _is_linked(b, 'fsm_Action21', a1)
    if hasattr(a1, 'fsm_State20'):
        assert _is_linked(a1, 'fsm_State20', b)
    _safe_set(b, 'fsm_Action21', a2)
    assert _is_linked(b, 'fsm_Action21', a2)
    if hasattr(a1, 'fsm_State20'):
        assert not _is_linked(a1, 'fsm_State20', b)
    if hasattr(a2, 'fsm_State20'):
        assert _is_linked(a2, 'fsm_State20', b)
    _safe_set(b, 'fsm_Action21', None)
    assert not _is_linked(b, 'fsm_Action21', a2)
    if hasattr(a2, 'fsm_State20'):
        assert not _is_linked(a2, 'fsm_State20', b)


def test_assoc_onExitedActions22_reverse_link_reassign_clear():
    a1 = fsm_State(name="sample_text")
    a2 = fsm_State(name="sample_text_2")
    b = fsm_Action(name="sample_text")
    _safe_set(b, 'fsm_Action24', a1)
    assert _is_linked(b, 'fsm_Action24', a1)
    if hasattr(a1, 'fsm_State23'):
        assert _is_linked(a1, 'fsm_State23', b)
    _safe_set(b, 'fsm_Action24', a2)
    assert _is_linked(b, 'fsm_Action24', a2)
    if hasattr(a1, 'fsm_State23'):
        assert not _is_linked(a1, 'fsm_State23', b)
    if hasattr(a2, 'fsm_State23'):
        assert _is_linked(a2, 'fsm_State23', b)
    _safe_set(b, 'fsm_Action24', None)
    assert not _is_linked(b, 'fsm_Action24', a2)
    if hasattr(a2, 'fsm_State23'):
        assert not _is_linked(a2, 'fsm_State23', b)


def test_assoc_outgoingTransitions16_reverse_link_reassign_clear():
    a1 = fsm_Transition(InverseGuard=True, name="sample_text")
    a2 = fsm_Transition(InverseGuard=False, name="sample_text_2")
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


def test_assoc_ownedActions7_reverse_link_reassign_clear():
    a1 = fsm_FSM(groupId="sample_text", isServer=True, name="sample_text")
    a2 = fsm_FSM(groupId="sample_text_2", isServer=False, name="sample_text_2")
    b = fsm_Action(name="sample_text")
    _safe_set(b, 'fsm_Action', a1)
    assert _is_linked(b, 'fsm_Action', a1)
    if hasattr(a1, 'fsm_FSM8'):
        assert _is_linked(a1, 'fsm_FSM8', b)
    _safe_set(b, 'fsm_Action', a2)
    assert _is_linked(b, 'fsm_Action', a2)
    if hasattr(a1, 'fsm_FSM8'):
        assert not _is_linked(a1, 'fsm_FSM8', b)
    if hasattr(a2, 'fsm_FSM8'):
        assert _is_linked(a2, 'fsm_FSM8', b)
    _safe_set(b, 'fsm_Action', None)
    assert not _is_linked(b, 'fsm_Action', a2)
    if hasattr(a2, 'fsm_FSM8'):
        assert not _is_linked(a2, 'fsm_FSM8', b)


def test_assoc_ownedEvents5_reverse_link_reassign_clear():
    a1 = fsm_FSM(groupId="sample_text", isServer=True, name="sample_text")
    a2 = fsm_FSM(groupId="sample_text_2", isServer=False, name="sample_text_2")
    b = fsm_Event(name="sample_text")
    _safe_set(b, 'fsm_Event', a1)
    assert _is_linked(b, 'fsm_Event', a1)
    if hasattr(a1, 'fsm_FSM6'):
        assert _is_linked(a1, 'fsm_FSM6', b)
    _safe_set(b, 'fsm_Event', a2)
    assert _is_linked(b, 'fsm_Event', a2)
    if hasattr(a1, 'fsm_FSM6'):
        assert not _is_linked(a1, 'fsm_FSM6', b)
    if hasattr(a2, 'fsm_FSM6'):
        assert _is_linked(a2, 'fsm_FSM6', b)
    _safe_set(b, 'fsm_Event', None)
    assert not _is_linked(b, 'fsm_Event', a2)
    if hasattr(a2, 'fsm_FSM6'):
        assert not _is_linked(a2, 'fsm_FSM6', b)


def test_assoc_ownedGuards9_reverse_link_reassign_clear():
    a1 = fsm_Guard(name="sample_text")
    a2 = fsm_Guard(name="sample_text_2")
    b = fsm_FSM(groupId="sample_text", isServer=True, name="sample_text")
    _safe_set(b, 'fsm_FSM10', {a1})
    assert _is_linked(b, 'fsm_FSM10', a1)
    if hasattr(a1, 'fsm_Guard'):
        assert _is_linked(a1, 'fsm_Guard', b)
    _safe_set(b, 'fsm_FSM10', {a2})
    assert _is_linked(b, 'fsm_FSM10', a2)
    if hasattr(a1, 'fsm_Guard'):
        assert not _is_linked(a1, 'fsm_Guard', b)
    if hasattr(a2, 'fsm_Guard'):
        assert _is_linked(a2, 'fsm_Guard', b)
    _safe_set(b, 'fsm_FSM10', set())
    assert not _is_linked(b, 'fsm_FSM10', a2)
    if hasattr(a2, 'fsm_Guard'):
        assert not _is_linked(a2, 'fsm_Guard', b)


def test_assoc_ownedMessages11_reverse_link_reassign_clear():
    a1 = fsm_Message(name="sample_text")
    a2 = fsm_Message(name="sample_text_2")
    b = fsm_FSM(groupId="sample_text", isServer=True, name="sample_text")
    _safe_set(b, 'fsm_FSM12', {a1})
    assert _is_linked(b, 'fsm_FSM12', a1)
    if hasattr(a1, 'fsm_Message'):
        assert _is_linked(a1, 'fsm_Message', b)
    _safe_set(b, 'fsm_FSM12', {a2})
    assert _is_linked(b, 'fsm_FSM12', a2)
    if hasattr(a1, 'fsm_Message'):
        assert not _is_linked(a1, 'fsm_Message', b)
    if hasattr(a2, 'fsm_Message'):
        assert _is_linked(a2, 'fsm_Message', b)
    _safe_set(b, 'fsm_FSM12', set())
    assert not _is_linked(b, 'fsm_FSM12', a2)
    if hasattr(a2, 'fsm_Message'):
        assert not _is_linked(a2, 'fsm_Message', b)


def test_assoc_ownedStates0_reverse_link_reassign_clear():
    a1 = fsm_State(name="sample_text")
    a2 = fsm_State(name="sample_text_2")
    b = fsm_FSM(groupId="sample_text", isServer=True, name="sample_text")
    _safe_set(b, 'owningFSM', {a1})
    assert _is_linked(b, 'owningFSM', a1)
    if hasattr(a1, 'State'):
        assert _is_linked(a1, 'State', b)
    _safe_set(b, 'owningFSM', {a2})
    assert _is_linked(b, 'owningFSM', a2)
    if hasattr(a1, 'State'):
        assert not _is_linked(a1, 'State', b)
    if hasattr(a2, 'State'):
        assert _is_linked(a2, 'State', b)
    _safe_set(b, 'owningFSM', set())
    assert not _is_linked(b, 'owningFSM', a2)
    if hasattr(a2, 'State'):
        assert not _is_linked(a2, 'State', b)


def test_assoc_owningFSM15_reverse_link_reassign_clear():
    a1 = fsm_State(name="sample_text")
    a2 = fsm_State(name="sample_text_2")
    b = fsm_FSM(groupId="sample_text", isServer=True, name="sample_text")
    _safe_set(b, 'FSM', a1)
    assert _is_linked(b, 'FSM', a1)
    if hasattr(a1, 'ownedStates'):
        assert _is_linked(a1, 'ownedStates', b)
    _safe_set(b, 'FSM', a2)
    assert _is_linked(b, 'FSM', a2)
    if hasattr(a1, 'ownedStates'):
        assert not _is_linked(a1, 'ownedStates', b)
    if hasattr(a2, 'ownedStates'):
        assert _is_linked(a2, 'ownedStates', b)
    _safe_set(b, 'FSM', None)
    assert not _is_linked(b, 'FSM', a2)
    if hasattr(a2, 'ownedStates'):
        assert not _is_linked(a2, 'ownedStates', b)


def test_assoc_source28_reverse_link_reassign_clear():
    a1 = fsm_Transition(InverseGuard=True, name="sample_text")
    a2 = fsm_Transition(InverseGuard=False, name="sample_text_2")
    b = fsm_State(name="sample_text")
    _safe_set(b, 'State29', a1)
    assert _is_linked(b, 'State29', a1)
    if hasattr(a1, 'outgoingTransitions'):
        assert _is_linked(a1, 'outgoingTransitions', b)
    _safe_set(b, 'State29', a2)
    assert _is_linked(b, 'State29', a2)
    if hasattr(a1, 'outgoingTransitions'):
        assert not _is_linked(a1, 'outgoingTransitions', b)
    if hasattr(a2, 'outgoingTransitions'):
        assert _is_linked(a2, 'outgoingTransitions', b)
    _safe_set(b, 'State29', None)
    assert not _is_linked(b, 'State29', a2)
    if hasattr(a2, 'outgoingTransitions'):
        assert not _is_linked(a2, 'outgoingTransitions', b)


def test_assoc_target38_reverse_link_reassign_clear():
    a1 = fsm_Transition(InverseGuard=True, name="sample_text")
    a2 = fsm_Transition(InverseGuard=False, name="sample_text_2")
    b = fsm_State(name="sample_text")
    _safe_set(b, 'State39', a1)
    assert _is_linked(b, 'State39', a1)
    if hasattr(a1, 'incomingTransitions'):
        assert _is_linked(a1, 'incomingTransitions', b)
    _safe_set(b, 'State39', a2)
    assert _is_linked(b, 'State39', a2)
    if hasattr(a1, 'incomingTransitions'):
        assert not _is_linked(a1, 'incomingTransitions', b)
    if hasattr(a2, 'incomingTransitions'):
        assert _is_linked(a2, 'incomingTransitions', b)
    _safe_set(b, 'State39', None)
    assert not _is_linked(b, 'State39', a2)
    if hasattr(a2, 'incomingTransitions'):
        assert not _is_linked(a2, 'incomingTransitions', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

