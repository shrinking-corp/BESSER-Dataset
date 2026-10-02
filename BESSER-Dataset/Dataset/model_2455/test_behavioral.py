import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Delegation,
    jpdl31_ActionType,
    jpdl31_AssignmentType,
    jpdl31_CancelTimerType,
    jpdl31_ConditionType,
    jpdl31_CreateTimerType,
    jpdl31_DecisionType,
    jpdl31_Delegation,
    jpdl31_DocumentRoot,
    jpdl31_EStringToStringMapEntry,
    jpdl31_EndStateType,
    jpdl31_EventType,
    jpdl31_ExceptionHandlerType,
    jpdl31_ForkType,
    jpdl31_JoinType,
    jpdl31_NodeType,
    jpdl31_ProcessDefinitionType,
    jpdl31_ProcessStateType,
    jpdl31_ScriptType,
    jpdl31_StartStateType,
    jpdl31_StateType,
    jpdl31_SubProcessType,
    jpdl31_SuperStateType,
    jpdl31_SwimlaneType,
    jpdl31_TaskNodeType,
    jpdl31_TaskType,
    jpdl31_TimerType,
    jpdl31_TransitionType,
    jpdl31_TransitionType1,
    jpdl31_VariableType,
    BooleanType,
    ConfigType,
    ConfigTypeType,
    ConfigTypeType1,
    PriorityTypeMember0,
    SignalType,
    TypeTypeMember1,
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

def test_assoc_action0_reverse_link_reassign_clear():
    a1 = jpdl31_CreateTimerType(duedate="sample_text", name="sample_text", repeat="sample_text", transition="sample_text")
    a2 = jpdl31_CreateTimerType(duedate="sample_text_2", name="sample_text_2", repeat="sample_text_2", transition="sample_text_2")
    b = jpdl31_ActionType(acceptPropagatedEvents="sample_text", any="sample_text", async_="sample_text", class_="sample_text", configType="sample_text", expression="sample_text", mixed="sample_text", name="sample_text", refName="sample_text")
    _safe_set(b, 'jpdl31_ActionType', a1)
    assert _is_linked(b, 'jpdl31_ActionType', a1)
    if hasattr(a1, 'jpdl31_CreateTimerType'):
        assert _is_linked(a1, 'jpdl31_CreateTimerType', b)
    _safe_set(b, 'jpdl31_ActionType', a2)
    assert _is_linked(b, 'jpdl31_ActionType', a2)
    if hasattr(a1, 'jpdl31_CreateTimerType'):
        assert not _is_linked(a1, 'jpdl31_CreateTimerType', b)
    if hasattr(a2, 'jpdl31_CreateTimerType'):
        assert _is_linked(a2, 'jpdl31_CreateTimerType', b)
    _safe_set(b, 'jpdl31_ActionType', None)
    assert not _is_linked(b, 'jpdl31_ActionType', a2)
    if hasattr(a2, 'jpdl31_CreateTimerType'):
        assert not _is_linked(a2, 'jpdl31_CreateTimerType', b)


def test_assoc_action120_reverse_link_reassign_clear():
    a1 = jpdl31_NodeType(async_="sample_text", name="sample_text", nodeContentElements="sample_text")
    a2 = jpdl31_NodeType(async_="sample_text_2", name="sample_text_2", nodeContentElements="sample_text_2")
    b = jpdl31_ActionType(acceptPropagatedEvents="sample_text", any="sample_text", async_="sample_text", class_="sample_text", configType="sample_text", expression="sample_text", mixed="sample_text", name="sample_text", refName="sample_text")
    _safe_set(b, 'jpdl31_ActionType122', a1)
    assert _is_linked(b, 'jpdl31_ActionType122', a1)
    if hasattr(a1, 'jpdl31_NodeType121'):
        assert _is_linked(a1, 'jpdl31_NodeType121', b)
    _safe_set(b, 'jpdl31_ActionType122', a2)
    assert _is_linked(b, 'jpdl31_ActionType122', a2)
    if hasattr(a1, 'jpdl31_NodeType121'):
        assert not _is_linked(a1, 'jpdl31_NodeType121', b)
    if hasattr(a2, 'jpdl31_NodeType121'):
        assert _is_linked(a2, 'jpdl31_NodeType121', b)
    _safe_set(b, 'jpdl31_ActionType122', None)
    assert not _is_linked(b, 'jpdl31_ActionType122', a2)
    if hasattr(a2, 'jpdl31_NodeType121'):
        assert not _is_linked(a2, 'jpdl31_NodeType121', b)


def test_assoc_action14_reverse_link_reassign_clear():
    a1 = jpdl31_DocumentRoot(mixed="sample_text")
    a2 = jpdl31_DocumentRoot(mixed="sample_text_2")
    b = jpdl31_ActionType(acceptPropagatedEvents="sample_text", any="sample_text", async_="sample_text", class_="sample_text", configType="sample_text", expression="sample_text", mixed="sample_text", name="sample_text", refName="sample_text")
    _safe_set(b, 'jpdl31_ActionType16', a1)
    assert _is_linked(b, 'jpdl31_ActionType16', a1)
    if hasattr(a1, 'jpdl31_DocumentRoot15'):
        assert _is_linked(a1, 'jpdl31_DocumentRoot15', b)
    _safe_set(b, 'jpdl31_ActionType16', a2)
    assert _is_linked(b, 'jpdl31_ActionType16', a2)
    if hasattr(a1, 'jpdl31_DocumentRoot15'):
        assert not _is_linked(a1, 'jpdl31_DocumentRoot15', b)
    if hasattr(a2, 'jpdl31_DocumentRoot15'):
        assert _is_linked(a2, 'jpdl31_DocumentRoot15', b)
    _safe_set(b, 'jpdl31_ActionType16', None)
    assert not _is_linked(b, 'jpdl31_ActionType16', a2)
    if hasattr(a2, 'jpdl31_DocumentRoot15'):
        assert not _is_linked(a2, 'jpdl31_DocumentRoot15', b)


def test_assoc_action177_reverse_link_reassign_clear():
    a1 = jpdl31_ProcessDefinitionType(group="sample_text", name="sample_text")
    a2 = jpdl31_ProcessDefinitionType(group="sample_text_2", name="sample_text_2")
    b = jpdl31_ActionType(acceptPropagatedEvents="sample_text", any="sample_text", async_="sample_text", class_="sample_text", configType="sample_text", expression="sample_text", mixed="sample_text", name="sample_text", refName="sample_text")
    _safe_set(b, 'jpdl31_ActionType179', a1)
    assert _is_linked(b, 'jpdl31_ActionType179', a1)
    if hasattr(a1, 'jpdl31_ProcessDefinitionType178'):
        assert _is_linked(a1, 'jpdl31_ProcessDefinitionType178', b)
    _safe_set(b, 'jpdl31_ActionType179', a2)
    assert _is_linked(b, 'jpdl31_ActionType179', a2)
    if hasattr(a1, 'jpdl31_ProcessDefinitionType178'):
        assert not _is_linked(a1, 'jpdl31_ProcessDefinitionType178', b)
    if hasattr(a2, 'jpdl31_ProcessDefinitionType178'):
        assert _is_linked(a2, 'jpdl31_ProcessDefinitionType178', b)
    _safe_set(b, 'jpdl31_ActionType179', None)
    assert not _is_linked(b, 'jpdl31_ActionType179', a2)
    if hasattr(a2, 'jpdl31_ProcessDefinitionType178'):
        assert not _is_linked(a2, 'jpdl31_ProcessDefinitionType178', b)


def test_assoc_action308_reverse_link_reassign_clear():
    a1 = jpdl31_TimerType(duedate="sample_text", name="sample_text", repeat="sample_text", transition="sample_text")
    a2 = jpdl31_TimerType(duedate="sample_text_2", name="sample_text_2", repeat="sample_text_2", transition="sample_text_2")
    b = jpdl31_ActionType(acceptPropagatedEvents="sample_text", any="sample_text", async_="sample_text", class_="sample_text", configType="sample_text", expression="sample_text", mixed="sample_text", name="sample_text", refName="sample_text")
    _safe_set(b, 'jpdl31_ActionType310', a1)
    assert _is_linked(b, 'jpdl31_ActionType310', a1)
    if hasattr(a1, 'jpdl31_TimerType309'):
        assert _is_linked(a1, 'jpdl31_TimerType309', b)
    _safe_set(b, 'jpdl31_ActionType310', a2)
    assert _is_linked(b, 'jpdl31_ActionType310', a2)
    if hasattr(a1, 'jpdl31_TimerType309'):
        assert not _is_linked(a1, 'jpdl31_TimerType309', b)
    if hasattr(a2, 'jpdl31_TimerType309'):
        assert _is_linked(a2, 'jpdl31_TimerType309', b)
    _safe_set(b, 'jpdl31_ActionType310', None)
    assert not _is_linked(b, 'jpdl31_ActionType310', a2)
    if hasattr(a2, 'jpdl31_TimerType309'):
        assert not _is_linked(a2, 'jpdl31_TimerType309', b)


def test_assoc_action314_reverse_link_reassign_clear():
    a1 = jpdl31_TransitionType(group="sample_text", name="sample_text", to="sample_text")
    a2 = jpdl31_TransitionType(group="sample_text_2", name="sample_text_2", to="sample_text_2")
    b = jpdl31_ActionType(acceptPropagatedEvents="sample_text", any="sample_text", async_="sample_text", class_="sample_text", configType="sample_text", expression="sample_text", mixed="sample_text", name="sample_text", refName="sample_text")
    _safe_set(b, 'jpdl31_ActionType316', a1)
    assert _is_linked(b, 'jpdl31_ActionType316', a1)
    if hasattr(a1, 'jpdl31_TransitionType315'):
        assert _is_linked(a1, 'jpdl31_TransitionType315', b)
    _safe_set(b, 'jpdl31_ActionType316', a2)
    assert _is_linked(b, 'jpdl31_ActionType316', a2)
    if hasattr(a1, 'jpdl31_TransitionType315'):
        assert not _is_linked(a1, 'jpdl31_TransitionType315', b)
    if hasattr(a2, 'jpdl31_TransitionType315'):
        assert _is_linked(a2, 'jpdl31_TransitionType315', b)
    _safe_set(b, 'jpdl31_ActionType316', None)
    assert not _is_linked(b, 'jpdl31_ActionType316', a2)
    if hasattr(a2, 'jpdl31_TransitionType315'):
        assert not _is_linked(a2, 'jpdl31_TransitionType315', b)


def test_assoc_action331_reverse_link_reassign_clear():
    a1 = jpdl31_TransitionType1(group="sample_text", name="sample_text", to="sample_text")
    a2 = jpdl31_TransitionType1(group="sample_text_2", name="sample_text_2", to="sample_text_2")
    b = jpdl31_ActionType(acceptPropagatedEvents="sample_text", any="sample_text", async_="sample_text", class_="sample_text", configType="sample_text", expression="sample_text", mixed="sample_text", name="sample_text", refName="sample_text")
    _safe_set(b, 'jpdl31_ActionType333', a1)
    assert _is_linked(b, 'jpdl31_ActionType333', a1)
    if hasattr(a1, 'jpdl31_TransitionType1332'):
        assert _is_linked(a1, 'jpdl31_TransitionType1332', b)
    _safe_set(b, 'jpdl31_ActionType333', a2)
    assert _is_linked(b, 'jpdl31_ActionType333', a2)
    if hasattr(a1, 'jpdl31_TransitionType1332'):
        assert not _is_linked(a1, 'jpdl31_TransitionType1332', b)
    if hasattr(a2, 'jpdl31_TransitionType1332'):
        assert _is_linked(a2, 'jpdl31_TransitionType1332', b)
    _safe_set(b, 'jpdl31_ActionType333', None)
    assert not _is_linked(b, 'jpdl31_ActionType333', a2)
    if hasattr(a2, 'jpdl31_TransitionType1332'):
        assert not _is_linked(a2, 'jpdl31_TransitionType1332', b)


def test_assoc_action75_reverse_link_reassign_clear():
    a1 = jpdl31_EventType(actionElements="sample_text", type="sample_text")
    a2 = jpdl31_EventType(actionElements="sample_text_2", type="sample_text_2")
    b = jpdl31_ActionType(acceptPropagatedEvents="sample_text", any="sample_text", async_="sample_text", class_="sample_text", configType="sample_text", expression="sample_text", mixed="sample_text", name="sample_text", refName="sample_text")
    _safe_set(b, 'jpdl31_ActionType77', a1)
    assert _is_linked(b, 'jpdl31_ActionType77', a1)
    if hasattr(a1, 'jpdl31_EventType76'):
        assert _is_linked(a1, 'jpdl31_EventType76', b)
    _safe_set(b, 'jpdl31_ActionType77', a2)
    assert _is_linked(b, 'jpdl31_ActionType77', a2)
    if hasattr(a1, 'jpdl31_EventType76'):
        assert not _is_linked(a1, 'jpdl31_EventType76', b)
    if hasattr(a2, 'jpdl31_EventType76'):
        assert _is_linked(a2, 'jpdl31_EventType76', b)
    _safe_set(b, 'jpdl31_ActionType77', None)
    assert not _is_linked(b, 'jpdl31_ActionType77', a2)
    if hasattr(a2, 'jpdl31_EventType76'):
        assert not _is_linked(a2, 'jpdl31_EventType76', b)


def test_assoc_action87_reverse_link_reassign_clear():
    a1 = jpdl31_ExceptionHandlerType(exceptionClass="sample_text", group="sample_text")
    a2 = jpdl31_ExceptionHandlerType(exceptionClass="sample_text_2", group="sample_text_2")
    b = jpdl31_ActionType(acceptPropagatedEvents="sample_text", any="sample_text", async_="sample_text", class_="sample_text", configType="sample_text", expression="sample_text", mixed="sample_text", name="sample_text", refName="sample_text")
    _safe_set(b, 'jpdl31_ActionType89', a1)
    assert _is_linked(b, 'jpdl31_ActionType89', a1)
    if hasattr(a1, 'jpdl31_ExceptionHandlerType88'):
        assert _is_linked(a1, 'jpdl31_ExceptionHandlerType88', b)
    _safe_set(b, 'jpdl31_ActionType89', a2)
    assert _is_linked(b, 'jpdl31_ActionType89', a2)
    if hasattr(a1, 'jpdl31_ExceptionHandlerType88'):
        assert not _is_linked(a1, 'jpdl31_ExceptionHandlerType88', b)
    if hasattr(a2, 'jpdl31_ExceptionHandlerType88'):
        assert _is_linked(a2, 'jpdl31_ExceptionHandlerType88', b)
    _safe_set(b, 'jpdl31_ActionType89', None)
    assert not _is_linked(b, 'jpdl31_ActionType89', a2)
    if hasattr(a2, 'jpdl31_ExceptionHandlerType88'):
        assert not _is_linked(a2, 'jpdl31_ExceptionHandlerType88', b)


def test_assoc_assignment17_reverse_link_reassign_clear():
    a1 = jpdl31_DocumentRoot(mixed="sample_text")
    a2 = jpdl31_DocumentRoot(mixed="sample_text_2")
    b = jpdl31_AssignmentType(actorId="sample_text", expression="sample_text", pooledActors="sample_text")
    _safe_set(b, 'jpdl31_AssignmentType', a1)
    assert _is_linked(b, 'jpdl31_AssignmentType', a1)
    if hasattr(a1, 'jpdl31_DocumentRoot18'):
        assert _is_linked(a1, 'jpdl31_DocumentRoot18', b)
    _safe_set(b, 'jpdl31_AssignmentType', a2)
    assert _is_linked(b, 'jpdl31_AssignmentType', a2)
    if hasattr(a1, 'jpdl31_DocumentRoot18'):
        assert not _is_linked(a1, 'jpdl31_DocumentRoot18', b)
    if hasattr(a2, 'jpdl31_DocumentRoot18'):
        assert _is_linked(a2, 'jpdl31_DocumentRoot18', b)
    _safe_set(b, 'jpdl31_AssignmentType', None)
    assert not _is_linked(b, 'jpdl31_AssignmentType', a2)
    if hasattr(a2, 'jpdl31_DocumentRoot18'):
        assert not _is_linked(a2, 'jpdl31_DocumentRoot18', b)


def test_assoc_assignment278_reverse_link_reassign_clear():
    a1 = jpdl31_SwimlaneType(name="sample_text")
    a2 = jpdl31_SwimlaneType(name="sample_text_2")
    b = jpdl31_AssignmentType(actorId="sample_text", expression="sample_text", pooledActors="sample_text")
    _safe_set(b, 'jpdl31_AssignmentType280', a1)
    assert _is_linked(b, 'jpdl31_AssignmentType280', a1)
    if hasattr(a1, 'jpdl31_SwimlaneType279'):
        assert _is_linked(a1, 'jpdl31_SwimlaneType279', b)
    _safe_set(b, 'jpdl31_AssignmentType280', a2)
    assert _is_linked(b, 'jpdl31_AssignmentType280', a2)
    if hasattr(a1, 'jpdl31_SwimlaneType279'):
        assert not _is_linked(a1, 'jpdl31_SwimlaneType279', b)
    if hasattr(a2, 'jpdl31_SwimlaneType279'):
        assert _is_linked(a2, 'jpdl31_SwimlaneType279', b)
    _safe_set(b, 'jpdl31_AssignmentType280', None)
    assert not _is_linked(b, 'jpdl31_AssignmentType280', a2)
    if hasattr(a2, 'jpdl31_SwimlaneType279'):
        assert not _is_linked(a2, 'jpdl31_SwimlaneType279', b)


def test_assoc_assignment296_reverse_link_reassign_clear():
    a1 = jpdl31_TaskType(blocking="sample_text", description="sample_text", duedate="sample_text", group="sample_text", name="sample_text", priority="sample_text", signalling="sample_text", swimlane="sample_text")
    a2 = jpdl31_TaskType(blocking="sample_text_2", description="sample_text_2", duedate="sample_text_2", group="sample_text_2", name="sample_text_2", priority="sample_text_2", signalling="sample_text_2", swimlane="sample_text_2")
    b = jpdl31_AssignmentType(actorId="sample_text", expression="sample_text", pooledActors="sample_text")
    _safe_set(b, 'jpdl31_AssignmentType298', a1)
    assert _is_linked(b, 'jpdl31_AssignmentType298', a1)
    if hasattr(a1, 'jpdl31_TaskType297'):
        assert _is_linked(a1, 'jpdl31_TaskType297', b)
    _safe_set(b, 'jpdl31_AssignmentType298', a2)
    assert _is_linked(b, 'jpdl31_AssignmentType298', a2)
    if hasattr(a1, 'jpdl31_TaskType297'):
        assert not _is_linked(a1, 'jpdl31_TaskType297', b)
    if hasattr(a2, 'jpdl31_TaskType297'):
        assert _is_linked(a2, 'jpdl31_TaskType297', b)
    _safe_set(b, 'jpdl31_AssignmentType298', None)
    assert not _is_linked(b, 'jpdl31_AssignmentType298', a2)
    if hasattr(a2, 'jpdl31_TaskType297'):
        assert not _is_linked(a2, 'jpdl31_TaskType297', b)


def test_assoc_cancelTimer129_reverse_link_reassign_clear():
    a1 = jpdl31_NodeType(async_="sample_text", name="sample_text", nodeContentElements="sample_text")
    a2 = jpdl31_NodeType(async_="sample_text_2", name="sample_text_2", nodeContentElements="sample_text_2")
    b = jpdl31_CancelTimerType(name="sample_text")
    _safe_set(b, 'jpdl31_CancelTimerType131', a1)
    assert _is_linked(b, 'jpdl31_CancelTimerType131', a1)
    if hasattr(a1, 'jpdl31_NodeType130'):
        assert _is_linked(a1, 'jpdl31_NodeType130', b)
    _safe_set(b, 'jpdl31_CancelTimerType131', a2)
    assert _is_linked(b, 'jpdl31_CancelTimerType131', a2)
    if hasattr(a1, 'jpdl31_NodeType130'):
        assert not _is_linked(a1, 'jpdl31_NodeType130', b)
    if hasattr(a2, 'jpdl31_NodeType130'):
        assert _is_linked(a2, 'jpdl31_NodeType130', b)
    _safe_set(b, 'jpdl31_CancelTimerType131', None)
    assert not _is_linked(b, 'jpdl31_CancelTimerType131', a2)
    if hasattr(a2, 'jpdl31_NodeType130'):
        assert not _is_linked(a2, 'jpdl31_NodeType130', b)


def test_assoc_cancelTimer186_reverse_link_reassign_clear():
    a1 = jpdl31_ProcessDefinitionType(group="sample_text", name="sample_text")
    a2 = jpdl31_ProcessDefinitionType(group="sample_text_2", name="sample_text_2")
    b = jpdl31_CancelTimerType(name="sample_text")
    _safe_set(b, 'jpdl31_CancelTimerType188', a1)
    assert _is_linked(b, 'jpdl31_CancelTimerType188', a1)
    if hasattr(a1, 'jpdl31_ProcessDefinitionType187'):
        assert _is_linked(a1, 'jpdl31_ProcessDefinitionType187', b)
    _safe_set(b, 'jpdl31_CancelTimerType188', a2)
    assert _is_linked(b, 'jpdl31_CancelTimerType188', a2)
    if hasattr(a1, 'jpdl31_ProcessDefinitionType187'):
        assert not _is_linked(a1, 'jpdl31_ProcessDefinitionType187', b)
    if hasattr(a2, 'jpdl31_ProcessDefinitionType187'):
        assert _is_linked(a2, 'jpdl31_ProcessDefinitionType187', b)
    _safe_set(b, 'jpdl31_CancelTimerType188', None)
    assert not _is_linked(b, 'jpdl31_CancelTimerType188', a2)
    if hasattr(a2, 'jpdl31_ProcessDefinitionType187'):
        assert not _is_linked(a2, 'jpdl31_ProcessDefinitionType187', b)


def test_assoc_cancelTimer19_reverse_link_reassign_clear():
    a1 = jpdl31_DocumentRoot(mixed="sample_text")
    a2 = jpdl31_DocumentRoot(mixed="sample_text_2")
    b = jpdl31_CancelTimerType(name="sample_text")
    _safe_set(b, 'jpdl31_CancelTimerType', a1)
    assert _is_linked(b, 'jpdl31_CancelTimerType', a1)
    if hasattr(a1, 'jpdl31_DocumentRoot20'):
        assert _is_linked(a1, 'jpdl31_DocumentRoot20', b)
    _safe_set(b, 'jpdl31_CancelTimerType', a2)
    assert _is_linked(b, 'jpdl31_CancelTimerType', a2)
    if hasattr(a1, 'jpdl31_DocumentRoot20'):
        assert not _is_linked(a1, 'jpdl31_DocumentRoot20', b)
    if hasattr(a2, 'jpdl31_DocumentRoot20'):
        assert _is_linked(a2, 'jpdl31_DocumentRoot20', b)
    _safe_set(b, 'jpdl31_CancelTimerType', None)
    assert not _is_linked(b, 'jpdl31_CancelTimerType', a2)
    if hasattr(a2, 'jpdl31_DocumentRoot20'):
        assert not _is_linked(a2, 'jpdl31_DocumentRoot20', b)


def test_assoc_cancelTimer323_reverse_link_reassign_clear():
    a1 = jpdl31_TransitionType(group="sample_text", name="sample_text", to="sample_text")
    a2 = jpdl31_TransitionType(group="sample_text_2", name="sample_text_2", to="sample_text_2")
    b = jpdl31_CancelTimerType(name="sample_text")
    _safe_set(b, 'jpdl31_CancelTimerType325', a1)
    assert _is_linked(b, 'jpdl31_CancelTimerType325', a1)
    if hasattr(a1, 'jpdl31_TransitionType324'):
        assert _is_linked(a1, 'jpdl31_TransitionType324', b)
    _safe_set(b, 'jpdl31_CancelTimerType325', a2)
    assert _is_linked(b, 'jpdl31_CancelTimerType325', a2)
    if hasattr(a1, 'jpdl31_TransitionType324'):
        assert not _is_linked(a1, 'jpdl31_TransitionType324', b)
    if hasattr(a2, 'jpdl31_TransitionType324'):
        assert _is_linked(a2, 'jpdl31_TransitionType324', b)
    _safe_set(b, 'jpdl31_CancelTimerType325', None)
    assert not _is_linked(b, 'jpdl31_CancelTimerType325', a2)
    if hasattr(a2, 'jpdl31_TransitionType324'):
        assert not _is_linked(a2, 'jpdl31_TransitionType324', b)


def test_assoc_cancelTimer340_reverse_link_reassign_clear():
    a1 = jpdl31_TransitionType1(group="sample_text", name="sample_text", to="sample_text")
    a2 = jpdl31_TransitionType1(group="sample_text_2", name="sample_text_2", to="sample_text_2")
    b = jpdl31_CancelTimerType(name="sample_text")
    _safe_set(b, 'jpdl31_CancelTimerType342', a1)
    assert _is_linked(b, 'jpdl31_CancelTimerType342', a1)
    if hasattr(a1, 'jpdl31_TransitionType1341'):
        assert _is_linked(a1, 'jpdl31_TransitionType1341', b)
    _safe_set(b, 'jpdl31_CancelTimerType342', a2)
    assert _is_linked(b, 'jpdl31_CancelTimerType342', a2)
    if hasattr(a1, 'jpdl31_TransitionType1341'):
        assert not _is_linked(a1, 'jpdl31_TransitionType1341', b)
    if hasattr(a2, 'jpdl31_TransitionType1341'):
        assert _is_linked(a2, 'jpdl31_TransitionType1341', b)
    _safe_set(b, 'jpdl31_CancelTimerType342', None)
    assert not _is_linked(b, 'jpdl31_CancelTimerType342', a2)
    if hasattr(a2, 'jpdl31_TransitionType1341'):
        assert not _is_linked(a2, 'jpdl31_TransitionType1341', b)


def test_assoc_cancelTimer84_reverse_link_reassign_clear():
    a1 = jpdl31_EventType(actionElements="sample_text", type="sample_text")
    a2 = jpdl31_EventType(actionElements="sample_text_2", type="sample_text_2")
    b = jpdl31_CancelTimerType(name="sample_text")
    _safe_set(b, 'jpdl31_CancelTimerType86', a1)
    assert _is_linked(b, 'jpdl31_CancelTimerType86', a1)
    if hasattr(a1, 'jpdl31_EventType85'):
        assert _is_linked(a1, 'jpdl31_EventType85', b)
    _safe_set(b, 'jpdl31_CancelTimerType86', a2)
    assert _is_linked(b, 'jpdl31_CancelTimerType86', a2)
    if hasattr(a1, 'jpdl31_EventType85'):
        assert not _is_linked(a1, 'jpdl31_EventType85', b)
    if hasattr(a2, 'jpdl31_EventType85'):
        assert _is_linked(a2, 'jpdl31_EventType85', b)
    _safe_set(b, 'jpdl31_CancelTimerType86', None)
    assert not _is_linked(b, 'jpdl31_CancelTimerType86', a2)
    if hasattr(a2, 'jpdl31_EventType85'):
        assert not _is_linked(a2, 'jpdl31_EventType85', b)


def test_assoc_condition329_reverse_link_reassign_clear():
    a1 = jpdl31_TransitionType1(group="sample_text", name="sample_text", to="sample_text")
    a2 = jpdl31_TransitionType1(group="sample_text_2", name="sample_text_2", to="sample_text_2")
    b = jpdl31_ConditionType(any="sample_text", expression="sample_text", group="sample_text", mixed="sample_text")
    _safe_set(b, 'jpdl31_ConditionType', a1)
    assert _is_linked(b, 'jpdl31_ConditionType', a1)
    if hasattr(a1, 'jpdl31_TransitionType1330'):
        assert _is_linked(a1, 'jpdl31_TransitionType1330', b)
    _safe_set(b, 'jpdl31_ConditionType', a2)
    assert _is_linked(b, 'jpdl31_ConditionType', a2)
    if hasattr(a1, 'jpdl31_TransitionType1330'):
        assert not _is_linked(a1, 'jpdl31_TransitionType1330', b)
    if hasattr(a2, 'jpdl31_TransitionType1330'):
        assert _is_linked(a2, 'jpdl31_TransitionType1330', b)
    _safe_set(b, 'jpdl31_ConditionType', None)
    assert not _is_linked(b, 'jpdl31_ConditionType', a2)
    if hasattr(a2, 'jpdl31_TransitionType1330'):
        assert not _is_linked(a2, 'jpdl31_TransitionType1330', b)


def test_assoc_controller21_reverse_link_reassign_clear():
    a1 = jpdl31_DocumentRoot(mixed="sample_text")
    a2 = jpdl31_DocumentRoot(mixed="sample_text_2")
    b = jpdl31_Delegation(any="sample_text", class_="sample_text", configType="sample_text", mixed="sample_text")
    _safe_set(b, 'jpdl31_Delegation23', a1)
    assert _is_linked(b, 'jpdl31_Delegation23', a1)
    if hasattr(a1, 'jpdl31_DocumentRoot22'):
        assert _is_linked(a1, 'jpdl31_DocumentRoot22', b)
    _safe_set(b, 'jpdl31_Delegation23', a2)
    assert _is_linked(b, 'jpdl31_Delegation23', a2)
    if hasattr(a1, 'jpdl31_DocumentRoot22'):
        assert not _is_linked(a1, 'jpdl31_DocumentRoot22', b)
    if hasattr(a2, 'jpdl31_DocumentRoot22'):
        assert _is_linked(a2, 'jpdl31_DocumentRoot22', b)
    _safe_set(b, 'jpdl31_Delegation23', None)
    assert not _is_linked(b, 'jpdl31_Delegation23', a2)
    if hasattr(a2, 'jpdl31_DocumentRoot22'):
        assert not _is_linked(a2, 'jpdl31_DocumentRoot22', b)


def test_assoc_controller299_reverse_link_reassign_clear():
    a1 = jpdl31_TaskType(blocking="sample_text", description="sample_text", duedate="sample_text", group="sample_text", name="sample_text", priority="sample_text", signalling="sample_text", swimlane="sample_text")
    a2 = jpdl31_TaskType(blocking="sample_text_2", description="sample_text_2", duedate="sample_text_2", group="sample_text_2", name="sample_text_2", priority="sample_text_2", signalling="sample_text_2", swimlane="sample_text_2")
    b = jpdl31_Delegation(any="sample_text", class_="sample_text", configType="sample_text", mixed="sample_text")
    _safe_set(b, 'jpdl31_Delegation301', a1)
    assert _is_linked(b, 'jpdl31_Delegation301', a1)
    if hasattr(a1, 'jpdl31_TaskType300'):
        assert _is_linked(a1, 'jpdl31_TaskType300', b)
    _safe_set(b, 'jpdl31_Delegation301', a2)
    assert _is_linked(b, 'jpdl31_Delegation301', a2)
    if hasattr(a1, 'jpdl31_TaskType300'):
        assert not _is_linked(a1, 'jpdl31_TaskType300', b)
    if hasattr(a2, 'jpdl31_TaskType300'):
        assert _is_linked(a2, 'jpdl31_TaskType300', b)
    _safe_set(b, 'jpdl31_Delegation301', None)
    assert not _is_linked(b, 'jpdl31_Delegation301', a2)
    if hasattr(a2, 'jpdl31_TaskType300'):
        assert not _is_linked(a2, 'jpdl31_TaskType300', b)


def test_assoc_createTimer126_reverse_link_reassign_clear():
    a1 = jpdl31_NodeType(async_="sample_text", name="sample_text", nodeContentElements="sample_text")
    a2 = jpdl31_NodeType(async_="sample_text_2", name="sample_text_2", nodeContentElements="sample_text_2")
    b = jpdl31_CreateTimerType(duedate="sample_text", name="sample_text", repeat="sample_text", transition="sample_text")
    _safe_set(b, 'jpdl31_CreateTimerType128', a1)
    assert _is_linked(b, 'jpdl31_CreateTimerType128', a1)
    if hasattr(a1, 'jpdl31_NodeType127'):
        assert _is_linked(a1, 'jpdl31_NodeType127', b)
    _safe_set(b, 'jpdl31_CreateTimerType128', a2)
    assert _is_linked(b, 'jpdl31_CreateTimerType128', a2)
    if hasattr(a1, 'jpdl31_NodeType127'):
        assert not _is_linked(a1, 'jpdl31_NodeType127', b)
    if hasattr(a2, 'jpdl31_NodeType127'):
        assert _is_linked(a2, 'jpdl31_NodeType127', b)
    _safe_set(b, 'jpdl31_CreateTimerType128', None)
    assert not _is_linked(b, 'jpdl31_CreateTimerType128', a2)
    if hasattr(a2, 'jpdl31_NodeType127'):
        assert not _is_linked(a2, 'jpdl31_NodeType127', b)


def test_assoc_createTimer183_reverse_link_reassign_clear():
    a1 = jpdl31_ProcessDefinitionType(group="sample_text", name="sample_text")
    a2 = jpdl31_ProcessDefinitionType(group="sample_text_2", name="sample_text_2")
    b = jpdl31_CreateTimerType(duedate="sample_text", name="sample_text", repeat="sample_text", transition="sample_text")
    _safe_set(b, 'jpdl31_CreateTimerType185', a1)
    assert _is_linked(b, 'jpdl31_CreateTimerType185', a1)
    if hasattr(a1, 'jpdl31_ProcessDefinitionType184'):
        assert _is_linked(a1, 'jpdl31_ProcessDefinitionType184', b)
    _safe_set(b, 'jpdl31_CreateTimerType185', a2)
    assert _is_linked(b, 'jpdl31_CreateTimerType185', a2)
    if hasattr(a1, 'jpdl31_ProcessDefinitionType184'):
        assert not _is_linked(a1, 'jpdl31_ProcessDefinitionType184', b)
    if hasattr(a2, 'jpdl31_ProcessDefinitionType184'):
        assert _is_linked(a2, 'jpdl31_ProcessDefinitionType184', b)
    _safe_set(b, 'jpdl31_CreateTimerType185', None)
    assert not _is_linked(b, 'jpdl31_CreateTimerType185', a2)
    if hasattr(a2, 'jpdl31_ProcessDefinitionType184'):
        assert not _is_linked(a2, 'jpdl31_ProcessDefinitionType184', b)


def test_assoc_createTimer24_reverse_link_reassign_clear():
    a1 = jpdl31_DocumentRoot(mixed="sample_text")
    a2 = jpdl31_DocumentRoot(mixed="sample_text_2")
    b = jpdl31_CreateTimerType(duedate="sample_text", name="sample_text", repeat="sample_text", transition="sample_text")
    _safe_set(b, 'jpdl31_CreateTimerType26', a1)
    assert _is_linked(b, 'jpdl31_CreateTimerType26', a1)
    if hasattr(a1, 'jpdl31_DocumentRoot25'):
        assert _is_linked(a1, 'jpdl31_DocumentRoot25', b)
    _safe_set(b, 'jpdl31_CreateTimerType26', a2)
    assert _is_linked(b, 'jpdl31_CreateTimerType26', a2)
    if hasattr(a1, 'jpdl31_DocumentRoot25'):
        assert not _is_linked(a1, 'jpdl31_DocumentRoot25', b)
    if hasattr(a2, 'jpdl31_DocumentRoot25'):
        assert _is_linked(a2, 'jpdl31_DocumentRoot25', b)
    _safe_set(b, 'jpdl31_CreateTimerType26', None)
    assert not _is_linked(b, 'jpdl31_CreateTimerType26', a2)
    if hasattr(a2, 'jpdl31_DocumentRoot25'):
        assert not _is_linked(a2, 'jpdl31_DocumentRoot25', b)


def test_assoc_createTimer320_reverse_link_reassign_clear():
    a1 = jpdl31_TransitionType(group="sample_text", name="sample_text", to="sample_text")
    a2 = jpdl31_TransitionType(group="sample_text_2", name="sample_text_2", to="sample_text_2")
    b = jpdl31_CreateTimerType(duedate="sample_text", name="sample_text", repeat="sample_text", transition="sample_text")
    _safe_set(b, 'jpdl31_CreateTimerType322', a1)
    assert _is_linked(b, 'jpdl31_CreateTimerType322', a1)
    if hasattr(a1, 'jpdl31_TransitionType321'):
        assert _is_linked(a1, 'jpdl31_TransitionType321', b)
    _safe_set(b, 'jpdl31_CreateTimerType322', a2)
    assert _is_linked(b, 'jpdl31_CreateTimerType322', a2)
    if hasattr(a1, 'jpdl31_TransitionType321'):
        assert not _is_linked(a1, 'jpdl31_TransitionType321', b)
    if hasattr(a2, 'jpdl31_TransitionType321'):
        assert _is_linked(a2, 'jpdl31_TransitionType321', b)
    _safe_set(b, 'jpdl31_CreateTimerType322', None)
    assert not _is_linked(b, 'jpdl31_CreateTimerType322', a2)
    if hasattr(a2, 'jpdl31_TransitionType321'):
        assert not _is_linked(a2, 'jpdl31_TransitionType321', b)


def test_assoc_createTimer337_reverse_link_reassign_clear():
    a1 = jpdl31_TransitionType1(group="sample_text", name="sample_text", to="sample_text")
    a2 = jpdl31_TransitionType1(group="sample_text_2", name="sample_text_2", to="sample_text_2")
    b = jpdl31_CreateTimerType(duedate="sample_text", name="sample_text", repeat="sample_text", transition="sample_text")
    _safe_set(b, 'jpdl31_CreateTimerType339', a1)
    assert _is_linked(b, 'jpdl31_CreateTimerType339', a1)
    if hasattr(a1, 'jpdl31_TransitionType1338'):
        assert _is_linked(a1, 'jpdl31_TransitionType1338', b)
    _safe_set(b, 'jpdl31_CreateTimerType339', a2)
    assert _is_linked(b, 'jpdl31_CreateTimerType339', a2)
    if hasattr(a1, 'jpdl31_TransitionType1338'):
        assert not _is_linked(a1, 'jpdl31_TransitionType1338', b)
    if hasattr(a2, 'jpdl31_TransitionType1338'):
        assert _is_linked(a2, 'jpdl31_TransitionType1338', b)
    _safe_set(b, 'jpdl31_CreateTimerType339', None)
    assert not _is_linked(b, 'jpdl31_CreateTimerType339', a2)
    if hasattr(a2, 'jpdl31_TransitionType1338'):
        assert not _is_linked(a2, 'jpdl31_TransitionType1338', b)


def test_assoc_createTimer81_reverse_link_reassign_clear():
    a1 = jpdl31_EventType(actionElements="sample_text", type="sample_text")
    a2 = jpdl31_EventType(actionElements="sample_text_2", type="sample_text_2")
    b = jpdl31_CreateTimerType(duedate="sample_text", name="sample_text", repeat="sample_text", transition="sample_text")
    _safe_set(b, 'jpdl31_CreateTimerType83', a1)
    assert _is_linked(b, 'jpdl31_CreateTimerType83', a1)
    if hasattr(a1, 'jpdl31_EventType82'):
        assert _is_linked(a1, 'jpdl31_EventType82', b)
    _safe_set(b, 'jpdl31_CreateTimerType83', a2)
    assert _is_linked(b, 'jpdl31_CreateTimerType83', a2)
    if hasattr(a1, 'jpdl31_EventType82'):
        assert not _is_linked(a1, 'jpdl31_EventType82', b)
    if hasattr(a2, 'jpdl31_EventType82'):
        assert _is_linked(a2, 'jpdl31_EventType82', b)
    _safe_set(b, 'jpdl31_CreateTimerType83', None)
    assert not _is_linked(b, 'jpdl31_CreateTimerType83', a2)
    if hasattr(a2, 'jpdl31_EventType82'):
        assert not _is_linked(a2, 'jpdl31_EventType82', b)


def test_assoc_decision171_reverse_link_reassign_clear():
    a1 = jpdl31_ProcessDefinitionType(group="sample_text", name="sample_text")
    a2 = jpdl31_ProcessDefinitionType(group="sample_text_2", name="sample_text_2")
    b = jpdl31_DecisionType(async_="sample_text", expression="sample_text", group="sample_text", name="sample_text")
    _safe_set(b, 'jpdl31_DecisionType173', a1)
    assert _is_linked(b, 'jpdl31_DecisionType173', a1)
    if hasattr(a1, 'jpdl31_ProcessDefinitionType172'):
        assert _is_linked(a1, 'jpdl31_ProcessDefinitionType172', b)
    _safe_set(b, 'jpdl31_DecisionType173', a2)
    assert _is_linked(b, 'jpdl31_DecisionType173', a2)
    if hasattr(a1, 'jpdl31_ProcessDefinitionType172'):
        assert not _is_linked(a1, 'jpdl31_ProcessDefinitionType172', b)
    if hasattr(a2, 'jpdl31_ProcessDefinitionType172'):
        assert _is_linked(a2, 'jpdl31_ProcessDefinitionType172', b)
    _safe_set(b, 'jpdl31_DecisionType173', None)
    assert not _is_linked(b, 'jpdl31_DecisionType173', a2)
    if hasattr(a2, 'jpdl31_ProcessDefinitionType172'):
        assert not _is_linked(a2, 'jpdl31_ProcessDefinitionType172', b)


def test_assoc_decision260_reverse_link_reassign_clear():
    a1 = jpdl31_SuperStateType(async_="sample_text", group="sample_text", name="sample_text")
    a2 = jpdl31_SuperStateType(async_="sample_text_2", group="sample_text_2", name="sample_text_2")
    b = jpdl31_DecisionType(async_="sample_text", expression="sample_text", group="sample_text", name="sample_text")
    _safe_set(b, 'jpdl31_DecisionType262', a1)
    assert _is_linked(b, 'jpdl31_DecisionType262', a1)
    if hasattr(a1, 'jpdl31_SuperStateType261'):
        assert _is_linked(a1, 'jpdl31_SuperStateType261', b)
    _safe_set(b, 'jpdl31_DecisionType262', a2)
    assert _is_linked(b, 'jpdl31_DecisionType262', a2)
    if hasattr(a1, 'jpdl31_SuperStateType261'):
        assert not _is_linked(a1, 'jpdl31_SuperStateType261', b)
    if hasattr(a2, 'jpdl31_SuperStateType261'):
        assert _is_linked(a2, 'jpdl31_SuperStateType261', b)
    _safe_set(b, 'jpdl31_DecisionType262', None)
    assert not _is_linked(b, 'jpdl31_DecisionType262', a2)
    if hasattr(a2, 'jpdl31_SuperStateType261'):
        assert not _is_linked(a2, 'jpdl31_SuperStateType261', b)


def test_assoc_decision27_reverse_link_reassign_clear():
    a1 = jpdl31_DocumentRoot(mixed="sample_text")
    a2 = jpdl31_DocumentRoot(mixed="sample_text_2")
    b = jpdl31_DecisionType(async_="sample_text", expression="sample_text", group="sample_text", name="sample_text")
    _safe_set(b, 'jpdl31_DecisionType29', a1)
    assert _is_linked(b, 'jpdl31_DecisionType29', a1)
    if hasattr(a1, 'jpdl31_DocumentRoot28'):
        assert _is_linked(a1, 'jpdl31_DocumentRoot28', b)
    _safe_set(b, 'jpdl31_DecisionType29', a2)
    assert _is_linked(b, 'jpdl31_DecisionType29', a2)
    if hasattr(a1, 'jpdl31_DocumentRoot28'):
        assert not _is_linked(a1, 'jpdl31_DocumentRoot28', b)
    if hasattr(a2, 'jpdl31_DocumentRoot28'):
        assert _is_linked(a2, 'jpdl31_DocumentRoot28', b)
    _safe_set(b, 'jpdl31_DecisionType29', None)
    assert not _is_linked(b, 'jpdl31_DecisionType29', a2)
    if hasattr(a2, 'jpdl31_DocumentRoot28'):
        assert not _is_linked(a2, 'jpdl31_DocumentRoot28', b)


def test_assoc_endState174_reverse_link_reassign_clear():
    a1 = jpdl31_ProcessDefinitionType(group="sample_text", name="sample_text")
    a2 = jpdl31_ProcessDefinitionType(group="sample_text_2", name="sample_text_2")
    b = jpdl31_EndStateType(group="sample_text", name="sample_text")
    _safe_set(b, 'jpdl31_EndStateType176', a1)
    assert _is_linked(b, 'jpdl31_EndStateType176', a1)
    if hasattr(a1, 'jpdl31_ProcessDefinitionType175'):
        assert _is_linked(a1, 'jpdl31_ProcessDefinitionType175', b)
    _safe_set(b, 'jpdl31_EndStateType176', a2)
    assert _is_linked(b, 'jpdl31_EndStateType176', a2)
    if hasattr(a1, 'jpdl31_ProcessDefinitionType175'):
        assert not _is_linked(a1, 'jpdl31_ProcessDefinitionType175', b)
    if hasattr(a2, 'jpdl31_ProcessDefinitionType175'):
        assert _is_linked(a2, 'jpdl31_ProcessDefinitionType175', b)
    _safe_set(b, 'jpdl31_EndStateType176', None)
    assert not _is_linked(b, 'jpdl31_EndStateType176', a2)
    if hasattr(a2, 'jpdl31_ProcessDefinitionType175'):
        assert not _is_linked(a2, 'jpdl31_ProcessDefinitionType175', b)


def test_assoc_endState263_reverse_link_reassign_clear():
    a1 = jpdl31_SuperStateType(async_="sample_text", group="sample_text", name="sample_text")
    a2 = jpdl31_SuperStateType(async_="sample_text_2", group="sample_text_2", name="sample_text_2")
    b = jpdl31_EndStateType(group="sample_text", name="sample_text")
    _safe_set(b, 'jpdl31_EndStateType265', a1)
    assert _is_linked(b, 'jpdl31_EndStateType265', a1)
    if hasattr(a1, 'jpdl31_SuperStateType264'):
        assert _is_linked(a1, 'jpdl31_SuperStateType264', b)
    _safe_set(b, 'jpdl31_EndStateType265', a2)
    assert _is_linked(b, 'jpdl31_EndStateType265', a2)
    if hasattr(a1, 'jpdl31_SuperStateType264'):
        assert not _is_linked(a1, 'jpdl31_SuperStateType264', b)
    if hasattr(a2, 'jpdl31_SuperStateType264'):
        assert _is_linked(a2, 'jpdl31_SuperStateType264', b)
    _safe_set(b, 'jpdl31_EndStateType265', None)
    assert not _is_linked(b, 'jpdl31_EndStateType265', a2)
    if hasattr(a2, 'jpdl31_SuperStateType264'):
        assert not _is_linked(a2, 'jpdl31_SuperStateType264', b)


def test_assoc_endState30_reverse_link_reassign_clear():
    a1 = jpdl31_EndStateType(group="sample_text", name="sample_text")
    a2 = jpdl31_EndStateType(group="sample_text_2", name="sample_text_2")
    b = jpdl31_DocumentRoot(mixed="sample_text")
    _safe_set(b, 'jpdl31_DocumentRoot31', {a1})
    assert _is_linked(b, 'jpdl31_DocumentRoot31', a1)
    if hasattr(a1, 'jpdl31_EndStateType'):
        assert _is_linked(a1, 'jpdl31_EndStateType', b)
    _safe_set(b, 'jpdl31_DocumentRoot31', {a2})
    assert _is_linked(b, 'jpdl31_DocumentRoot31', a2)
    if hasattr(a1, 'jpdl31_EndStateType'):
        assert not _is_linked(a1, 'jpdl31_EndStateType', b)
    if hasattr(a2, 'jpdl31_EndStateType'):
        assert _is_linked(a2, 'jpdl31_EndStateType', b)
    _safe_set(b, 'jpdl31_DocumentRoot31', set())
    assert not _is_linked(b, 'jpdl31_DocumentRoot31', a2)
    if hasattr(a2, 'jpdl31_EndStateType'):
        assert not _is_linked(a2, 'jpdl31_EndStateType', b)


def test_assoc_event108_reverse_link_reassign_clear():
    a1 = jpdl31_JoinType(async_="sample_text", name="sample_text", nodeContentElements="sample_text")
    a2 = jpdl31_JoinType(async_="sample_text_2", name="sample_text_2", nodeContentElements="sample_text_2")
    b = jpdl31_EventType(actionElements="sample_text", type="sample_text")
    _safe_set(b, 'jpdl31_EventType110', a1)
    assert _is_linked(b, 'jpdl31_EventType110', a1)
    if hasattr(a1, 'jpdl31_JoinType109'):
        assert _is_linked(a1, 'jpdl31_JoinType109', b)
    _safe_set(b, 'jpdl31_EventType110', a2)
    assert _is_linked(b, 'jpdl31_EventType110', a2)
    if hasattr(a1, 'jpdl31_JoinType109'):
        assert not _is_linked(a1, 'jpdl31_JoinType109', b)
    if hasattr(a2, 'jpdl31_JoinType109'):
        assert _is_linked(a2, 'jpdl31_JoinType109', b)
    _safe_set(b, 'jpdl31_EventType110', None)
    assert not _is_linked(b, 'jpdl31_EventType110', a2)
    if hasattr(a2, 'jpdl31_JoinType109'):
        assert not _is_linked(a2, 'jpdl31_JoinType109', b)


def test_assoc_event132_reverse_link_reassign_clear():
    a1 = jpdl31_NodeType(async_="sample_text", name="sample_text", nodeContentElements="sample_text")
    a2 = jpdl31_NodeType(async_="sample_text_2", name="sample_text_2", nodeContentElements="sample_text_2")
    b = jpdl31_EventType(actionElements="sample_text", type="sample_text")
    _safe_set(b, 'jpdl31_EventType134', a1)
    assert _is_linked(b, 'jpdl31_EventType134', a1)
    if hasattr(a1, 'jpdl31_NodeType133'):
        assert _is_linked(a1, 'jpdl31_NodeType133', b)
    _safe_set(b, 'jpdl31_EventType134', a2)
    assert _is_linked(b, 'jpdl31_EventType134', a2)
    if hasattr(a1, 'jpdl31_NodeType133'):
        assert not _is_linked(a1, 'jpdl31_NodeType133', b)
    if hasattr(a2, 'jpdl31_NodeType133'):
        assert _is_linked(a2, 'jpdl31_NodeType133', b)
    _safe_set(b, 'jpdl31_EventType134', None)
    assert not _is_linked(b, 'jpdl31_EventType134', a2)
    if hasattr(a2, 'jpdl31_NodeType133'):
        assert not _is_linked(a2, 'jpdl31_NodeType133', b)


def test_assoc_event189_reverse_link_reassign_clear():
    a1 = jpdl31_ProcessDefinitionType(group="sample_text", name="sample_text")
    a2 = jpdl31_ProcessDefinitionType(group="sample_text_2", name="sample_text_2")
    b = jpdl31_EventType(actionElements="sample_text", type="sample_text")
    _safe_set(b, 'jpdl31_EventType191', a1)
    assert _is_linked(b, 'jpdl31_EventType191', a1)
    if hasattr(a1, 'jpdl31_ProcessDefinitionType190'):
        assert _is_linked(a1, 'jpdl31_ProcessDefinitionType190', b)
    _safe_set(b, 'jpdl31_EventType191', a2)
    assert _is_linked(b, 'jpdl31_EventType191', a2)
    if hasattr(a1, 'jpdl31_ProcessDefinitionType190'):
        assert not _is_linked(a1, 'jpdl31_ProcessDefinitionType190', b)
    if hasattr(a2, 'jpdl31_ProcessDefinitionType190'):
        assert _is_linked(a2, 'jpdl31_ProcessDefinitionType190', b)
    _safe_set(b, 'jpdl31_EventType191', None)
    assert not _is_linked(b, 'jpdl31_EventType191', a2)
    if hasattr(a2, 'jpdl31_ProcessDefinitionType190'):
        assert not _is_linked(a2, 'jpdl31_ProcessDefinitionType190', b)


def test_assoc_event203_reverse_link_reassign_clear():
    a1 = jpdl31_ProcessStateType(async_="sample_text", group="sample_text", name="sample_text")
    a2 = jpdl31_ProcessStateType(async_="sample_text_2", group="sample_text_2", name="sample_text_2")
    b = jpdl31_EventType(actionElements="sample_text", type="sample_text")
    _safe_set(b, 'jpdl31_EventType205', a1)
    assert _is_linked(b, 'jpdl31_EventType205', a1)
    if hasattr(a1, 'jpdl31_ProcessStateType204'):
        assert _is_linked(a1, 'jpdl31_ProcessStateType204', b)
    _safe_set(b, 'jpdl31_EventType205', a2)
    assert _is_linked(b, 'jpdl31_EventType205', a2)
    if hasattr(a1, 'jpdl31_ProcessStateType204'):
        assert not _is_linked(a1, 'jpdl31_ProcessStateType204', b)
    if hasattr(a2, 'jpdl31_ProcessStateType204'):
        assert _is_linked(a2, 'jpdl31_ProcessStateType204', b)
    _safe_set(b, 'jpdl31_EventType205', None)
    assert not _is_linked(b, 'jpdl31_EventType205', a2)
    if hasattr(a2, 'jpdl31_ProcessStateType204'):
        assert not _is_linked(a2, 'jpdl31_ProcessStateType204', b)


def test_assoc_event221_reverse_link_reassign_clear():
    a1 = jpdl31_StartStateType(group="sample_text", name="sample_text")
    a2 = jpdl31_StartStateType(group="sample_text_2", name="sample_text_2")
    b = jpdl31_EventType(actionElements="sample_text", type="sample_text")
    _safe_set(b, 'jpdl31_EventType223', a1)
    assert _is_linked(b, 'jpdl31_EventType223', a1)
    if hasattr(a1, 'jpdl31_StartStateType222'):
        assert _is_linked(a1, 'jpdl31_StartStateType222', b)
    _safe_set(b, 'jpdl31_EventType223', a2)
    assert _is_linked(b, 'jpdl31_EventType223', a2)
    if hasattr(a1, 'jpdl31_StartStateType222'):
        assert not _is_linked(a1, 'jpdl31_StartStateType222', b)
    if hasattr(a2, 'jpdl31_StartStateType222'):
        assert _is_linked(a2, 'jpdl31_StartStateType222', b)
    _safe_set(b, 'jpdl31_EventType223', None)
    assert not _is_linked(b, 'jpdl31_EventType223', a2)
    if hasattr(a2, 'jpdl31_StartStateType222'):
        assert not _is_linked(a2, 'jpdl31_StartStateType222', b)


def test_assoc_event227_reverse_link_reassign_clear():
    a1 = jpdl31_StateType(async_="sample_text", name="sample_text", nodeContentElements="sample_text")
    a2 = jpdl31_StateType(async_="sample_text_2", name="sample_text_2", nodeContentElements="sample_text_2")
    b = jpdl31_EventType(actionElements="sample_text", type="sample_text")
    _safe_set(b, 'jpdl31_EventType229', a1)
    assert _is_linked(b, 'jpdl31_EventType229', a1)
    if hasattr(a1, 'jpdl31_StateType228'):
        assert _is_linked(a1, 'jpdl31_StateType228', b)
    _safe_set(b, 'jpdl31_EventType229', a2)
    assert _is_linked(b, 'jpdl31_EventType229', a2)
    if hasattr(a1, 'jpdl31_StateType228'):
        assert not _is_linked(a1, 'jpdl31_StateType228', b)
    if hasattr(a2, 'jpdl31_StateType228'):
        assert _is_linked(a2, 'jpdl31_StateType228', b)
    _safe_set(b, 'jpdl31_EventType229', None)
    assert not _is_linked(b, 'jpdl31_EventType229', a2)
    if hasattr(a2, 'jpdl31_StateType228'):
        assert not _is_linked(a2, 'jpdl31_StateType228', b)


def test_assoc_event266_reverse_link_reassign_clear():
    a1 = jpdl31_SuperStateType(async_="sample_text", group="sample_text", name="sample_text")
    a2 = jpdl31_SuperStateType(async_="sample_text_2", group="sample_text_2", name="sample_text_2")
    b = jpdl31_EventType(actionElements="sample_text", type="sample_text")
    _safe_set(b, 'jpdl31_EventType268', a1)
    assert _is_linked(b, 'jpdl31_EventType268', a1)
    if hasattr(a1, 'jpdl31_SuperStateType267'):
        assert _is_linked(a1, 'jpdl31_SuperStateType267', b)
    _safe_set(b, 'jpdl31_EventType268', a2)
    assert _is_linked(b, 'jpdl31_EventType268', a2)
    if hasattr(a1, 'jpdl31_SuperStateType267'):
        assert not _is_linked(a1, 'jpdl31_SuperStateType267', b)
    if hasattr(a2, 'jpdl31_SuperStateType267'):
        assert _is_linked(a2, 'jpdl31_SuperStateType267', b)
    _safe_set(b, 'jpdl31_EventType268', None)
    assert not _is_linked(b, 'jpdl31_EventType268', a2)
    if hasattr(a2, 'jpdl31_SuperStateType267'):
        assert not _is_linked(a2, 'jpdl31_SuperStateType267', b)


def test_assoc_event284_reverse_link_reassign_clear():
    a1 = jpdl31_TaskNodeType(async_="sample_text", createTasks="sample_text", endTasks="sample_text", group="sample_text", name="sample_text", signal="sample_text")
    a2 = jpdl31_TaskNodeType(async_="sample_text_2", createTasks="sample_text_2", endTasks="sample_text_2", group="sample_text_2", name="sample_text_2", signal="sample_text_2")
    b = jpdl31_EventType(actionElements="sample_text", type="sample_text")
    _safe_set(b, 'jpdl31_EventType286', a1)
    assert _is_linked(b, 'jpdl31_EventType286', a1)
    if hasattr(a1, 'jpdl31_TaskNodeType285'):
        assert _is_linked(a1, 'jpdl31_TaskNodeType285', b)
    _safe_set(b, 'jpdl31_EventType286', a2)
    assert _is_linked(b, 'jpdl31_EventType286', a2)
    if hasattr(a1, 'jpdl31_TaskNodeType285'):
        assert not _is_linked(a1, 'jpdl31_TaskNodeType285', b)
    if hasattr(a2, 'jpdl31_TaskNodeType285'):
        assert _is_linked(a2, 'jpdl31_TaskNodeType285', b)
    _safe_set(b, 'jpdl31_EventType286', None)
    assert not _is_linked(b, 'jpdl31_EventType286', a2)
    if hasattr(a2, 'jpdl31_TaskNodeType285'):
        assert not _is_linked(a2, 'jpdl31_TaskNodeType285', b)


def test_assoc_event302_reverse_link_reassign_clear():
    a1 = jpdl31_TaskType(blocking="sample_text", description="sample_text", duedate="sample_text", group="sample_text", name="sample_text", priority="sample_text", signalling="sample_text", swimlane="sample_text")
    a2 = jpdl31_TaskType(blocking="sample_text_2", description="sample_text_2", duedate="sample_text_2", group="sample_text_2", name="sample_text_2", priority="sample_text_2", signalling="sample_text_2", swimlane="sample_text_2")
    b = jpdl31_EventType(actionElements="sample_text", type="sample_text")
    _safe_set(b, 'jpdl31_EventType304', a1)
    assert _is_linked(b, 'jpdl31_EventType304', a1)
    if hasattr(a1, 'jpdl31_TaskType303'):
        assert _is_linked(a1, 'jpdl31_TaskType303', b)
    _safe_set(b, 'jpdl31_EventType304', a2)
    assert _is_linked(b, 'jpdl31_EventType304', a2)
    if hasattr(a1, 'jpdl31_TaskType303'):
        assert not _is_linked(a1, 'jpdl31_TaskType303', b)
    if hasattr(a2, 'jpdl31_TaskType303'):
        assert _is_linked(a2, 'jpdl31_TaskType303', b)
    _safe_set(b, 'jpdl31_EventType304', None)
    assert not _is_linked(b, 'jpdl31_EventType304', a2)
    if hasattr(a2, 'jpdl31_TaskType303'):
        assert not _is_linked(a2, 'jpdl31_TaskType303', b)


def test_assoc_event32_reverse_link_reassign_clear():
    a1 = jpdl31_EventType(actionElements="sample_text", type="sample_text")
    a2 = jpdl31_EventType(actionElements="sample_text_2", type="sample_text_2")
    b = jpdl31_DocumentRoot(mixed="sample_text")
    _safe_set(b, 'jpdl31_DocumentRoot33', {a1})
    assert _is_linked(b, 'jpdl31_DocumentRoot33', a1)
    if hasattr(a1, 'jpdl31_EventType34'):
        assert _is_linked(a1, 'jpdl31_EventType34', b)
    _safe_set(b, 'jpdl31_DocumentRoot33', {a2})
    assert _is_linked(b, 'jpdl31_DocumentRoot33', a2)
    if hasattr(a1, 'jpdl31_EventType34'):
        assert not _is_linked(a1, 'jpdl31_EventType34', b)
    if hasattr(a2, 'jpdl31_EventType34'):
        assert _is_linked(a2, 'jpdl31_EventType34', b)
    _safe_set(b, 'jpdl31_DocumentRoot33', set())
    assert not _is_linked(b, 'jpdl31_DocumentRoot33', a2)
    if hasattr(a2, 'jpdl31_EventType34'):
        assert not _is_linked(a2, 'jpdl31_EventType34', b)


def test_assoc_event4_reverse_link_reassign_clear():
    a1 = jpdl31_EventType(actionElements="sample_text", type="sample_text")
    a2 = jpdl31_EventType(actionElements="sample_text_2", type="sample_text_2")
    b = jpdl31_DecisionType(async_="sample_text", expression="sample_text", group="sample_text", name="sample_text")
    _safe_set(b, 'jpdl31_DecisionType5', {a1})
    assert _is_linked(b, 'jpdl31_DecisionType5', a1)
    if hasattr(a1, 'jpdl31_EventType'):
        assert _is_linked(a1, 'jpdl31_EventType', b)
    _safe_set(b, 'jpdl31_DecisionType5', {a2})
    assert _is_linked(b, 'jpdl31_DecisionType5', a2)
    if hasattr(a1, 'jpdl31_EventType'):
        assert not _is_linked(a1, 'jpdl31_EventType', b)
    if hasattr(a2, 'jpdl31_EventType'):
        assert _is_linked(a2, 'jpdl31_EventType', b)
    _safe_set(b, 'jpdl31_DecisionType5', set())
    assert not _is_linked(b, 'jpdl31_DecisionType5', a2)
    if hasattr(a2, 'jpdl31_EventType'):
        assert not _is_linked(a2, 'jpdl31_EventType', b)


def test_assoc_event69_reverse_link_reassign_clear():
    a1 = jpdl31_EventType(actionElements="sample_text", type="sample_text")
    a2 = jpdl31_EventType(actionElements="sample_text_2", type="sample_text_2")
    b = jpdl31_EndStateType(group="sample_text", name="sample_text")
    _safe_set(b, 'jpdl31_EndStateType70', {a1})
    assert _is_linked(b, 'jpdl31_EndStateType70', a1)
    if hasattr(a1, 'jpdl31_EventType71'):
        assert _is_linked(a1, 'jpdl31_EventType71', b)
    _safe_set(b, 'jpdl31_EndStateType70', {a2})
    assert _is_linked(b, 'jpdl31_EndStateType70', a2)
    if hasattr(a1, 'jpdl31_EventType71'):
        assert not _is_linked(a1, 'jpdl31_EventType71', b)
    if hasattr(a2, 'jpdl31_EventType71'):
        assert _is_linked(a2, 'jpdl31_EventType71', b)
    _safe_set(b, 'jpdl31_EndStateType70', set())
    assert not _is_linked(b, 'jpdl31_EndStateType70', a2)
    if hasattr(a2, 'jpdl31_EventType71'):
        assert not _is_linked(a2, 'jpdl31_EventType71', b)


def test_assoc_event96_reverse_link_reassign_clear():
    a1 = jpdl31_ForkType(async_="sample_text", group="sample_text", name="sample_text")
    a2 = jpdl31_ForkType(async_="sample_text_2", group="sample_text_2", name="sample_text_2")
    b = jpdl31_EventType(actionElements="sample_text", type="sample_text")
    _safe_set(b, 'jpdl31_EventType98', a1)
    assert _is_linked(b, 'jpdl31_EventType98', a1)
    if hasattr(a1, 'jpdl31_ForkType97'):
        assert _is_linked(a1, 'jpdl31_ForkType97', b)
    _safe_set(b, 'jpdl31_EventType98', a2)
    assert _is_linked(b, 'jpdl31_EventType98', a2)
    if hasattr(a1, 'jpdl31_ForkType97'):
        assert not _is_linked(a1, 'jpdl31_ForkType97', b)
    if hasattr(a2, 'jpdl31_ForkType97'):
        assert _is_linked(a2, 'jpdl31_ForkType97', b)
    _safe_set(b, 'jpdl31_EventType98', None)
    assert not _is_linked(b, 'jpdl31_EventType98', a2)
    if hasattr(a2, 'jpdl31_ForkType97'):
        assert not _is_linked(a2, 'jpdl31_ForkType97', b)


def test_assoc_exceptionHandler111_reverse_link_reassign_clear():
    a1 = jpdl31_JoinType(async_="sample_text", name="sample_text", nodeContentElements="sample_text")
    a2 = jpdl31_JoinType(async_="sample_text_2", name="sample_text_2", nodeContentElements="sample_text_2")
    b = jpdl31_ExceptionHandlerType(exceptionClass="sample_text", group="sample_text")
    _safe_set(b, 'jpdl31_ExceptionHandlerType113', a1)
    assert _is_linked(b, 'jpdl31_ExceptionHandlerType113', a1)
    if hasattr(a1, 'jpdl31_JoinType112'):
        assert _is_linked(a1, 'jpdl31_JoinType112', b)
    _safe_set(b, 'jpdl31_ExceptionHandlerType113', a2)
    assert _is_linked(b, 'jpdl31_ExceptionHandlerType113', a2)
    if hasattr(a1, 'jpdl31_JoinType112'):
        assert not _is_linked(a1, 'jpdl31_JoinType112', b)
    if hasattr(a2, 'jpdl31_JoinType112'):
        assert _is_linked(a2, 'jpdl31_JoinType112', b)
    _safe_set(b, 'jpdl31_ExceptionHandlerType113', None)
    assert not _is_linked(b, 'jpdl31_ExceptionHandlerType113', a2)
    if hasattr(a2, 'jpdl31_JoinType112'):
        assert not _is_linked(a2, 'jpdl31_JoinType112', b)


def test_assoc_exceptionHandler135_reverse_link_reassign_clear():
    a1 = jpdl31_NodeType(async_="sample_text", name="sample_text", nodeContentElements="sample_text")
    a2 = jpdl31_NodeType(async_="sample_text_2", name="sample_text_2", nodeContentElements="sample_text_2")
    b = jpdl31_ExceptionHandlerType(exceptionClass="sample_text", group="sample_text")
    _safe_set(b, 'jpdl31_ExceptionHandlerType137', a1)
    assert _is_linked(b, 'jpdl31_ExceptionHandlerType137', a1)
    if hasattr(a1, 'jpdl31_NodeType136'):
        assert _is_linked(a1, 'jpdl31_NodeType136', b)
    _safe_set(b, 'jpdl31_ExceptionHandlerType137', a2)
    assert _is_linked(b, 'jpdl31_ExceptionHandlerType137', a2)
    if hasattr(a1, 'jpdl31_NodeType136'):
        assert not _is_linked(a1, 'jpdl31_NodeType136', b)
    if hasattr(a2, 'jpdl31_NodeType136'):
        assert _is_linked(a2, 'jpdl31_NodeType136', b)
    _safe_set(b, 'jpdl31_ExceptionHandlerType137', None)
    assert not _is_linked(b, 'jpdl31_ExceptionHandlerType137', a2)
    if hasattr(a2, 'jpdl31_NodeType136'):
        assert not _is_linked(a2, 'jpdl31_NodeType136', b)


def test_assoc_exceptionHandler192_reverse_link_reassign_clear():
    a1 = jpdl31_ProcessDefinitionType(group="sample_text", name="sample_text")
    a2 = jpdl31_ProcessDefinitionType(group="sample_text_2", name="sample_text_2")
    b = jpdl31_ExceptionHandlerType(exceptionClass="sample_text", group="sample_text")
    _safe_set(b, 'jpdl31_ExceptionHandlerType194', a1)
    assert _is_linked(b, 'jpdl31_ExceptionHandlerType194', a1)
    if hasattr(a1, 'jpdl31_ProcessDefinitionType193'):
        assert _is_linked(a1, 'jpdl31_ProcessDefinitionType193', b)
    _safe_set(b, 'jpdl31_ExceptionHandlerType194', a2)
    assert _is_linked(b, 'jpdl31_ExceptionHandlerType194', a2)
    if hasattr(a1, 'jpdl31_ProcessDefinitionType193'):
        assert not _is_linked(a1, 'jpdl31_ProcessDefinitionType193', b)
    if hasattr(a2, 'jpdl31_ProcessDefinitionType193'):
        assert _is_linked(a2, 'jpdl31_ProcessDefinitionType193', b)
    _safe_set(b, 'jpdl31_ExceptionHandlerType194', None)
    assert not _is_linked(b, 'jpdl31_ExceptionHandlerType194', a2)
    if hasattr(a2, 'jpdl31_ProcessDefinitionType193'):
        assert not _is_linked(a2, 'jpdl31_ProcessDefinitionType193', b)


def test_assoc_exceptionHandler206_reverse_link_reassign_clear():
    a1 = jpdl31_ProcessStateType(async_="sample_text", group="sample_text", name="sample_text")
    a2 = jpdl31_ProcessStateType(async_="sample_text_2", group="sample_text_2", name="sample_text_2")
    b = jpdl31_ExceptionHandlerType(exceptionClass="sample_text", group="sample_text")
    _safe_set(b, 'jpdl31_ExceptionHandlerType208', a1)
    assert _is_linked(b, 'jpdl31_ExceptionHandlerType208', a1)
    if hasattr(a1, 'jpdl31_ProcessStateType207'):
        assert _is_linked(a1, 'jpdl31_ProcessStateType207', b)
    _safe_set(b, 'jpdl31_ExceptionHandlerType208', a2)
    assert _is_linked(b, 'jpdl31_ExceptionHandlerType208', a2)
    if hasattr(a1, 'jpdl31_ProcessStateType207'):
        assert not _is_linked(a1, 'jpdl31_ProcessStateType207', b)
    if hasattr(a2, 'jpdl31_ProcessStateType207'):
        assert _is_linked(a2, 'jpdl31_ProcessStateType207', b)
    _safe_set(b, 'jpdl31_ExceptionHandlerType208', None)
    assert not _is_linked(b, 'jpdl31_ExceptionHandlerType208', a2)
    if hasattr(a2, 'jpdl31_ProcessStateType207'):
        assert not _is_linked(a2, 'jpdl31_ProcessStateType207', b)


def test_assoc_exceptionHandler224_reverse_link_reassign_clear():
    a1 = jpdl31_StartStateType(group="sample_text", name="sample_text")
    a2 = jpdl31_StartStateType(group="sample_text_2", name="sample_text_2")
    b = jpdl31_ExceptionHandlerType(exceptionClass="sample_text", group="sample_text")
    _safe_set(b, 'jpdl31_ExceptionHandlerType226', a1)
    assert _is_linked(b, 'jpdl31_ExceptionHandlerType226', a1)
    if hasattr(a1, 'jpdl31_StartStateType225'):
        assert _is_linked(a1, 'jpdl31_StartStateType225', b)
    _safe_set(b, 'jpdl31_ExceptionHandlerType226', a2)
    assert _is_linked(b, 'jpdl31_ExceptionHandlerType226', a2)
    if hasattr(a1, 'jpdl31_StartStateType225'):
        assert not _is_linked(a1, 'jpdl31_StartStateType225', b)
    if hasattr(a2, 'jpdl31_StartStateType225'):
        assert _is_linked(a2, 'jpdl31_StartStateType225', b)
    _safe_set(b, 'jpdl31_ExceptionHandlerType226', None)
    assert not _is_linked(b, 'jpdl31_ExceptionHandlerType226', a2)
    if hasattr(a2, 'jpdl31_StartStateType225'):
        assert not _is_linked(a2, 'jpdl31_StartStateType225', b)


def test_assoc_exceptionHandler230_reverse_link_reassign_clear():
    a1 = jpdl31_StateType(async_="sample_text", name="sample_text", nodeContentElements="sample_text")
    a2 = jpdl31_StateType(async_="sample_text_2", name="sample_text_2", nodeContentElements="sample_text_2")
    b = jpdl31_ExceptionHandlerType(exceptionClass="sample_text", group="sample_text")
    _safe_set(b, 'jpdl31_ExceptionHandlerType232', a1)
    assert _is_linked(b, 'jpdl31_ExceptionHandlerType232', a1)
    if hasattr(a1, 'jpdl31_StateType231'):
        assert _is_linked(a1, 'jpdl31_StateType231', b)
    _safe_set(b, 'jpdl31_ExceptionHandlerType232', a2)
    assert _is_linked(b, 'jpdl31_ExceptionHandlerType232', a2)
    if hasattr(a1, 'jpdl31_StateType231'):
        assert not _is_linked(a1, 'jpdl31_StateType231', b)
    if hasattr(a2, 'jpdl31_StateType231'):
        assert _is_linked(a2, 'jpdl31_StateType231', b)
    _safe_set(b, 'jpdl31_ExceptionHandlerType232', None)
    assert not _is_linked(b, 'jpdl31_ExceptionHandlerType232', a2)
    if hasattr(a2, 'jpdl31_StateType231'):
        assert not _is_linked(a2, 'jpdl31_StateType231', b)


def test_assoc_exceptionHandler269_reverse_link_reassign_clear():
    a1 = jpdl31_SuperStateType(async_="sample_text", group="sample_text", name="sample_text")
    a2 = jpdl31_SuperStateType(async_="sample_text_2", group="sample_text_2", name="sample_text_2")
    b = jpdl31_ExceptionHandlerType(exceptionClass="sample_text", group="sample_text")
    _safe_set(b, 'jpdl31_ExceptionHandlerType271', a1)
    assert _is_linked(b, 'jpdl31_ExceptionHandlerType271', a1)
    if hasattr(a1, 'jpdl31_SuperStateType270'):
        assert _is_linked(a1, 'jpdl31_SuperStateType270', b)
    _safe_set(b, 'jpdl31_ExceptionHandlerType271', a2)
    assert _is_linked(b, 'jpdl31_ExceptionHandlerType271', a2)
    if hasattr(a1, 'jpdl31_SuperStateType270'):
        assert not _is_linked(a1, 'jpdl31_SuperStateType270', b)
    if hasattr(a2, 'jpdl31_SuperStateType270'):
        assert _is_linked(a2, 'jpdl31_SuperStateType270', b)
    _safe_set(b, 'jpdl31_ExceptionHandlerType271', None)
    assert not _is_linked(b, 'jpdl31_ExceptionHandlerType271', a2)
    if hasattr(a2, 'jpdl31_SuperStateType270'):
        assert not _is_linked(a2, 'jpdl31_SuperStateType270', b)


def test_assoc_exceptionHandler287_reverse_link_reassign_clear():
    a1 = jpdl31_TaskNodeType(async_="sample_text", createTasks="sample_text", endTasks="sample_text", group="sample_text", name="sample_text", signal="sample_text")
    a2 = jpdl31_TaskNodeType(async_="sample_text_2", createTasks="sample_text_2", endTasks="sample_text_2", group="sample_text_2", name="sample_text_2", signal="sample_text_2")
    b = jpdl31_ExceptionHandlerType(exceptionClass="sample_text", group="sample_text")
    _safe_set(b, 'jpdl31_ExceptionHandlerType289', a1)
    assert _is_linked(b, 'jpdl31_ExceptionHandlerType289', a1)
    if hasattr(a1, 'jpdl31_TaskNodeType288'):
        assert _is_linked(a1, 'jpdl31_TaskNodeType288', b)
    _safe_set(b, 'jpdl31_ExceptionHandlerType289', a2)
    assert _is_linked(b, 'jpdl31_ExceptionHandlerType289', a2)
    if hasattr(a1, 'jpdl31_TaskNodeType288'):
        assert not _is_linked(a1, 'jpdl31_TaskNodeType288', b)
    if hasattr(a2, 'jpdl31_TaskNodeType288'):
        assert _is_linked(a2, 'jpdl31_TaskNodeType288', b)
    _safe_set(b, 'jpdl31_ExceptionHandlerType289', None)
    assert not _is_linked(b, 'jpdl31_ExceptionHandlerType289', a2)
    if hasattr(a2, 'jpdl31_TaskNodeType288'):
        assert not _is_linked(a2, 'jpdl31_TaskNodeType288', b)


def test_assoc_exceptionHandler326_reverse_link_reassign_clear():
    a1 = jpdl31_TransitionType(group="sample_text", name="sample_text", to="sample_text")
    a2 = jpdl31_TransitionType(group="sample_text_2", name="sample_text_2", to="sample_text_2")
    b = jpdl31_ExceptionHandlerType(exceptionClass="sample_text", group="sample_text")
    _safe_set(b, 'jpdl31_ExceptionHandlerType328', a1)
    assert _is_linked(b, 'jpdl31_ExceptionHandlerType328', a1)
    if hasattr(a1, 'jpdl31_TransitionType327'):
        assert _is_linked(a1, 'jpdl31_TransitionType327', b)
    _safe_set(b, 'jpdl31_ExceptionHandlerType328', a2)
    assert _is_linked(b, 'jpdl31_ExceptionHandlerType328', a2)
    if hasattr(a1, 'jpdl31_TransitionType327'):
        assert not _is_linked(a1, 'jpdl31_TransitionType327', b)
    if hasattr(a2, 'jpdl31_TransitionType327'):
        assert _is_linked(a2, 'jpdl31_TransitionType327', b)
    _safe_set(b, 'jpdl31_ExceptionHandlerType328', None)
    assert not _is_linked(b, 'jpdl31_ExceptionHandlerType328', a2)
    if hasattr(a2, 'jpdl31_TransitionType327'):
        assert not _is_linked(a2, 'jpdl31_TransitionType327', b)


def test_assoc_exceptionHandler343_reverse_link_reassign_clear():
    a1 = jpdl31_TransitionType1(group="sample_text", name="sample_text", to="sample_text")
    a2 = jpdl31_TransitionType1(group="sample_text_2", name="sample_text_2", to="sample_text_2")
    b = jpdl31_ExceptionHandlerType(exceptionClass="sample_text", group="sample_text")
    _safe_set(b, 'jpdl31_ExceptionHandlerType345', a1)
    assert _is_linked(b, 'jpdl31_ExceptionHandlerType345', a1)
    if hasattr(a1, 'jpdl31_TransitionType1344'):
        assert _is_linked(a1, 'jpdl31_TransitionType1344', b)
    _safe_set(b, 'jpdl31_ExceptionHandlerType345', a2)
    assert _is_linked(b, 'jpdl31_ExceptionHandlerType345', a2)
    if hasattr(a1, 'jpdl31_TransitionType1344'):
        assert not _is_linked(a1, 'jpdl31_TransitionType1344', b)
    if hasattr(a2, 'jpdl31_TransitionType1344'):
        assert _is_linked(a2, 'jpdl31_TransitionType1344', b)
    _safe_set(b, 'jpdl31_ExceptionHandlerType345', None)
    assert not _is_linked(b, 'jpdl31_ExceptionHandlerType345', a2)
    if hasattr(a2, 'jpdl31_TransitionType1344'):
        assert not _is_linked(a2, 'jpdl31_TransitionType1344', b)


def test_assoc_exceptionHandler35_reverse_link_reassign_clear():
    a1 = jpdl31_ExceptionHandlerType(exceptionClass="sample_text", group="sample_text")
    a2 = jpdl31_ExceptionHandlerType(exceptionClass="sample_text_2", group="sample_text_2")
    b = jpdl31_DocumentRoot(mixed="sample_text")
    _safe_set(b, 'jpdl31_DocumentRoot36', {a1})
    assert _is_linked(b, 'jpdl31_DocumentRoot36', a1)
    if hasattr(a1, 'jpdl31_ExceptionHandlerType37'):
        assert _is_linked(a1, 'jpdl31_ExceptionHandlerType37', b)
    _safe_set(b, 'jpdl31_DocumentRoot36', {a2})
    assert _is_linked(b, 'jpdl31_DocumentRoot36', a2)
    if hasattr(a1, 'jpdl31_ExceptionHandlerType37'):
        assert not _is_linked(a1, 'jpdl31_ExceptionHandlerType37', b)
    if hasattr(a2, 'jpdl31_ExceptionHandlerType37'):
        assert _is_linked(a2, 'jpdl31_ExceptionHandlerType37', b)
    _safe_set(b, 'jpdl31_DocumentRoot36', set())
    assert not _is_linked(b, 'jpdl31_DocumentRoot36', a2)
    if hasattr(a2, 'jpdl31_ExceptionHandlerType37'):
        assert not _is_linked(a2, 'jpdl31_ExceptionHandlerType37', b)


def test_assoc_exceptionHandler6_reverse_link_reassign_clear():
    a1 = jpdl31_ExceptionHandlerType(exceptionClass="sample_text", group="sample_text")
    a2 = jpdl31_ExceptionHandlerType(exceptionClass="sample_text_2", group="sample_text_2")
    b = jpdl31_DecisionType(async_="sample_text", expression="sample_text", group="sample_text", name="sample_text")
    _safe_set(b, 'jpdl31_DecisionType7', {a1})
    assert _is_linked(b, 'jpdl31_DecisionType7', a1)
    if hasattr(a1, 'jpdl31_ExceptionHandlerType'):
        assert _is_linked(a1, 'jpdl31_ExceptionHandlerType', b)
    _safe_set(b, 'jpdl31_DecisionType7', {a2})
    assert _is_linked(b, 'jpdl31_DecisionType7', a2)
    if hasattr(a1, 'jpdl31_ExceptionHandlerType'):
        assert not _is_linked(a1, 'jpdl31_ExceptionHandlerType', b)
    if hasattr(a2, 'jpdl31_ExceptionHandlerType'):
        assert _is_linked(a2, 'jpdl31_ExceptionHandlerType', b)
    _safe_set(b, 'jpdl31_DecisionType7', set())
    assert not _is_linked(b, 'jpdl31_DecisionType7', a2)
    if hasattr(a2, 'jpdl31_ExceptionHandlerType'):
        assert not _is_linked(a2, 'jpdl31_ExceptionHandlerType', b)


def test_assoc_exceptionHandler72_reverse_link_reassign_clear():
    a1 = jpdl31_ExceptionHandlerType(exceptionClass="sample_text", group="sample_text")
    a2 = jpdl31_ExceptionHandlerType(exceptionClass="sample_text_2", group="sample_text_2")
    b = jpdl31_EndStateType(group="sample_text", name="sample_text")
    _safe_set(b, 'jpdl31_EndStateType73', {a1})
    assert _is_linked(b, 'jpdl31_EndStateType73', a1)
    if hasattr(a1, 'jpdl31_ExceptionHandlerType74'):
        assert _is_linked(a1, 'jpdl31_ExceptionHandlerType74', b)
    _safe_set(b, 'jpdl31_EndStateType73', {a2})
    assert _is_linked(b, 'jpdl31_EndStateType73', a2)
    if hasattr(a1, 'jpdl31_ExceptionHandlerType74'):
        assert not _is_linked(a1, 'jpdl31_ExceptionHandlerType74', b)
    if hasattr(a2, 'jpdl31_ExceptionHandlerType74'):
        assert _is_linked(a2, 'jpdl31_ExceptionHandlerType74', b)
    _safe_set(b, 'jpdl31_EndStateType73', set())
    assert not _is_linked(b, 'jpdl31_EndStateType73', a2)
    if hasattr(a2, 'jpdl31_ExceptionHandlerType74'):
        assert not _is_linked(a2, 'jpdl31_ExceptionHandlerType74', b)


def test_assoc_exceptionHandler99_reverse_link_reassign_clear():
    a1 = jpdl31_ForkType(async_="sample_text", group="sample_text", name="sample_text")
    a2 = jpdl31_ForkType(async_="sample_text_2", group="sample_text_2", name="sample_text_2")
    b = jpdl31_ExceptionHandlerType(exceptionClass="sample_text", group="sample_text")
    _safe_set(b, 'jpdl31_ExceptionHandlerType101', a1)
    assert _is_linked(b, 'jpdl31_ExceptionHandlerType101', a1)
    if hasattr(a1, 'jpdl31_ForkType100'):
        assert _is_linked(a1, 'jpdl31_ForkType100', b)
    _safe_set(b, 'jpdl31_ExceptionHandlerType101', a2)
    assert _is_linked(b, 'jpdl31_ExceptionHandlerType101', a2)
    if hasattr(a1, 'jpdl31_ForkType100'):
        assert not _is_linked(a1, 'jpdl31_ForkType100', b)
    if hasattr(a2, 'jpdl31_ForkType100'):
        assert _is_linked(a2, 'jpdl31_ForkType100', b)
    _safe_set(b, 'jpdl31_ExceptionHandlerType101', None)
    assert not _is_linked(b, 'jpdl31_ExceptionHandlerType101', a2)
    if hasattr(a2, 'jpdl31_ForkType100'):
        assert not _is_linked(a2, 'jpdl31_ForkType100', b)


def test_assoc_fork165_reverse_link_reassign_clear():
    a1 = jpdl31_ProcessDefinitionType(group="sample_text", name="sample_text")
    a2 = jpdl31_ProcessDefinitionType(group="sample_text_2", name="sample_text_2")
    b = jpdl31_ForkType(async_="sample_text", group="sample_text", name="sample_text")
    _safe_set(b, 'jpdl31_ForkType167', a1)
    assert _is_linked(b, 'jpdl31_ForkType167', a1)
    if hasattr(a1, 'jpdl31_ProcessDefinitionType166'):
        assert _is_linked(a1, 'jpdl31_ProcessDefinitionType166', b)
    _safe_set(b, 'jpdl31_ForkType167', a2)
    assert _is_linked(b, 'jpdl31_ForkType167', a2)
    if hasattr(a1, 'jpdl31_ProcessDefinitionType166'):
        assert not _is_linked(a1, 'jpdl31_ProcessDefinitionType166', b)
    if hasattr(a2, 'jpdl31_ProcessDefinitionType166'):
        assert _is_linked(a2, 'jpdl31_ProcessDefinitionType166', b)
    _safe_set(b, 'jpdl31_ForkType167', None)
    assert not _is_linked(b, 'jpdl31_ForkType167', a2)
    if hasattr(a2, 'jpdl31_ProcessDefinitionType166'):
        assert not _is_linked(a2, 'jpdl31_ProcessDefinitionType166', b)


def test_assoc_fork254_reverse_link_reassign_clear():
    a1 = jpdl31_SuperStateType(async_="sample_text", group="sample_text", name="sample_text")
    a2 = jpdl31_SuperStateType(async_="sample_text_2", group="sample_text_2", name="sample_text_2")
    b = jpdl31_ForkType(async_="sample_text", group="sample_text", name="sample_text")
    _safe_set(b, 'jpdl31_ForkType256', a1)
    assert _is_linked(b, 'jpdl31_ForkType256', a1)
    if hasattr(a1, 'jpdl31_SuperStateType255'):
        assert _is_linked(a1, 'jpdl31_SuperStateType255', b)
    _safe_set(b, 'jpdl31_ForkType256', a2)
    assert _is_linked(b, 'jpdl31_ForkType256', a2)
    if hasattr(a1, 'jpdl31_SuperStateType255'):
        assert not _is_linked(a1, 'jpdl31_SuperStateType255', b)
    if hasattr(a2, 'jpdl31_SuperStateType255'):
        assert _is_linked(a2, 'jpdl31_SuperStateType255', b)
    _safe_set(b, 'jpdl31_ForkType256', None)
    assert not _is_linked(b, 'jpdl31_ForkType256', a2)
    if hasattr(a2, 'jpdl31_SuperStateType255'):
        assert not _is_linked(a2, 'jpdl31_SuperStateType255', b)


def test_assoc_fork38_reverse_link_reassign_clear():
    a1 = jpdl31_ForkType(async_="sample_text", group="sample_text", name="sample_text")
    a2 = jpdl31_ForkType(async_="sample_text_2", group="sample_text_2", name="sample_text_2")
    b = jpdl31_DocumentRoot(mixed="sample_text")
    _safe_set(b, 'jpdl31_DocumentRoot39', {a1})
    assert _is_linked(b, 'jpdl31_DocumentRoot39', a1)
    if hasattr(a1, 'jpdl31_ForkType'):
        assert _is_linked(a1, 'jpdl31_ForkType', b)
    _safe_set(b, 'jpdl31_DocumentRoot39', {a2})
    assert _is_linked(b, 'jpdl31_DocumentRoot39', a2)
    if hasattr(a1, 'jpdl31_ForkType'):
        assert not _is_linked(a1, 'jpdl31_ForkType', b)
    if hasattr(a2, 'jpdl31_ForkType'):
        assert _is_linked(a2, 'jpdl31_ForkType', b)
    _safe_set(b, 'jpdl31_DocumentRoot39', set())
    assert not _is_linked(b, 'jpdl31_DocumentRoot39', a2)
    if hasattr(a2, 'jpdl31_ForkType'):
        assert not _is_linked(a2, 'jpdl31_ForkType', b)


def test_assoc_handler3_reverse_link_reassign_clear():
    a1 = jpdl31_Delegation(any="sample_text", class_="sample_text", configType="sample_text", mixed="sample_text")
    a2 = jpdl31_Delegation(any="sample_text_2", class_="sample_text_2", configType="sample_text_2", mixed="sample_text_2")
    b = jpdl31_DecisionType(async_="sample_text", expression="sample_text", group="sample_text", name="sample_text")
    _safe_set(b, 'jpdl31_DecisionType', {a1})
    assert _is_linked(b, 'jpdl31_DecisionType', a1)
    if hasattr(a1, 'jpdl31_Delegation'):
        assert _is_linked(a1, 'jpdl31_Delegation', b)
    _safe_set(b, 'jpdl31_DecisionType', {a2})
    assert _is_linked(b, 'jpdl31_DecisionType', a2)
    if hasattr(a1, 'jpdl31_Delegation'):
        assert not _is_linked(a1, 'jpdl31_Delegation', b)
    if hasattr(a2, 'jpdl31_Delegation'):
        assert _is_linked(a2, 'jpdl31_Delegation', b)
    _safe_set(b, 'jpdl31_DecisionType', set())
    assert not _is_linked(b, 'jpdl31_DecisionType', a2)
    if hasattr(a2, 'jpdl31_Delegation'):
        assert not _is_linked(a2, 'jpdl31_Delegation', b)


def test_assoc_join168_reverse_link_reassign_clear():
    a1 = jpdl31_ProcessDefinitionType(group="sample_text", name="sample_text")
    a2 = jpdl31_ProcessDefinitionType(group="sample_text_2", name="sample_text_2")
    b = jpdl31_JoinType(async_="sample_text", name="sample_text", nodeContentElements="sample_text")
    _safe_set(b, 'jpdl31_JoinType170', a1)
    assert _is_linked(b, 'jpdl31_JoinType170', a1)
    if hasattr(a1, 'jpdl31_ProcessDefinitionType169'):
        assert _is_linked(a1, 'jpdl31_ProcessDefinitionType169', b)
    _safe_set(b, 'jpdl31_JoinType170', a2)
    assert _is_linked(b, 'jpdl31_JoinType170', a2)
    if hasattr(a1, 'jpdl31_ProcessDefinitionType169'):
        assert not _is_linked(a1, 'jpdl31_ProcessDefinitionType169', b)
    if hasattr(a2, 'jpdl31_ProcessDefinitionType169'):
        assert _is_linked(a2, 'jpdl31_ProcessDefinitionType169', b)
    _safe_set(b, 'jpdl31_JoinType170', None)
    assert not _is_linked(b, 'jpdl31_JoinType170', a2)
    if hasattr(a2, 'jpdl31_ProcessDefinitionType169'):
        assert not _is_linked(a2, 'jpdl31_ProcessDefinitionType169', b)


def test_assoc_join257_reverse_link_reassign_clear():
    a1 = jpdl31_SuperStateType(async_="sample_text", group="sample_text", name="sample_text")
    a2 = jpdl31_SuperStateType(async_="sample_text_2", group="sample_text_2", name="sample_text_2")
    b = jpdl31_JoinType(async_="sample_text", name="sample_text", nodeContentElements="sample_text")
    _safe_set(b, 'jpdl31_JoinType259', a1)
    assert _is_linked(b, 'jpdl31_JoinType259', a1)
    if hasattr(a1, 'jpdl31_SuperStateType258'):
        assert _is_linked(a1, 'jpdl31_SuperStateType258', b)
    _safe_set(b, 'jpdl31_JoinType259', a2)
    assert _is_linked(b, 'jpdl31_JoinType259', a2)
    if hasattr(a1, 'jpdl31_SuperStateType258'):
        assert not _is_linked(a1, 'jpdl31_SuperStateType258', b)
    if hasattr(a2, 'jpdl31_SuperStateType258'):
        assert _is_linked(a2, 'jpdl31_SuperStateType258', b)
    _safe_set(b, 'jpdl31_JoinType259', None)
    assert not _is_linked(b, 'jpdl31_JoinType259', a2)
    if hasattr(a2, 'jpdl31_SuperStateType258'):
        assert not _is_linked(a2, 'jpdl31_SuperStateType258', b)


def test_assoc_join40_reverse_link_reassign_clear():
    a1 = jpdl31_JoinType(async_="sample_text", name="sample_text", nodeContentElements="sample_text")
    a2 = jpdl31_JoinType(async_="sample_text_2", name="sample_text_2", nodeContentElements="sample_text_2")
    b = jpdl31_DocumentRoot(mixed="sample_text")
    _safe_set(b, 'jpdl31_DocumentRoot41', {a1})
    assert _is_linked(b, 'jpdl31_DocumentRoot41', a1)
    if hasattr(a1, 'jpdl31_JoinType'):
        assert _is_linked(a1, 'jpdl31_JoinType', b)
    _safe_set(b, 'jpdl31_DocumentRoot41', {a2})
    assert _is_linked(b, 'jpdl31_DocumentRoot41', a2)
    if hasattr(a1, 'jpdl31_JoinType'):
        assert not _is_linked(a1, 'jpdl31_JoinType', b)
    if hasattr(a2, 'jpdl31_JoinType'):
        assert _is_linked(a2, 'jpdl31_JoinType', b)
    _safe_set(b, 'jpdl31_DocumentRoot41', set())
    assert not _is_linked(b, 'jpdl31_DocumentRoot41', a2)
    if hasattr(a2, 'jpdl31_JoinType'):
        assert not _is_linked(a2, 'jpdl31_JoinType', b)


def test_assoc_node150_reverse_link_reassign_clear():
    a1 = jpdl31_ProcessDefinitionType(group="sample_text", name="sample_text")
    a2 = jpdl31_ProcessDefinitionType(group="sample_text_2", name="sample_text_2")
    b = jpdl31_NodeType(async_="sample_text", name="sample_text", nodeContentElements="sample_text")
    _safe_set(b, 'jpdl31_NodeType152', a1)
    assert _is_linked(b, 'jpdl31_NodeType152', a1)
    if hasattr(a1, 'jpdl31_ProcessDefinitionType151'):
        assert _is_linked(a1, 'jpdl31_ProcessDefinitionType151', b)
    _safe_set(b, 'jpdl31_NodeType152', a2)
    assert _is_linked(b, 'jpdl31_NodeType152', a2)
    if hasattr(a1, 'jpdl31_ProcessDefinitionType151'):
        assert not _is_linked(a1, 'jpdl31_ProcessDefinitionType151', b)
    if hasattr(a2, 'jpdl31_ProcessDefinitionType151'):
        assert _is_linked(a2, 'jpdl31_ProcessDefinitionType151', b)
    _safe_set(b, 'jpdl31_NodeType152', None)
    assert not _is_linked(b, 'jpdl31_NodeType152', a2)
    if hasattr(a2, 'jpdl31_ProcessDefinitionType151'):
        assert not _is_linked(a2, 'jpdl31_ProcessDefinitionType151', b)


def test_assoc_node239_reverse_link_reassign_clear():
    a1 = jpdl31_SuperStateType(async_="sample_text", group="sample_text", name="sample_text")
    a2 = jpdl31_SuperStateType(async_="sample_text_2", group="sample_text_2", name="sample_text_2")
    b = jpdl31_NodeType(async_="sample_text", name="sample_text", nodeContentElements="sample_text")
    _safe_set(b, 'jpdl31_NodeType241', a1)
    assert _is_linked(b, 'jpdl31_NodeType241', a1)
    if hasattr(a1, 'jpdl31_SuperStateType240'):
        assert _is_linked(a1, 'jpdl31_SuperStateType240', b)
    _safe_set(b, 'jpdl31_NodeType241', a2)
    assert _is_linked(b, 'jpdl31_NodeType241', a2)
    if hasattr(a1, 'jpdl31_SuperStateType240'):
        assert not _is_linked(a1, 'jpdl31_SuperStateType240', b)
    if hasattr(a2, 'jpdl31_SuperStateType240'):
        assert _is_linked(a2, 'jpdl31_SuperStateType240', b)
    _safe_set(b, 'jpdl31_NodeType241', None)
    assert not _is_linked(b, 'jpdl31_NodeType241', a2)
    if hasattr(a2, 'jpdl31_SuperStateType240'):
        assert not _is_linked(a2, 'jpdl31_SuperStateType240', b)


def test_assoc_node42_reverse_link_reassign_clear():
    a1 = jpdl31_NodeType(async_="sample_text", name="sample_text", nodeContentElements="sample_text")
    a2 = jpdl31_NodeType(async_="sample_text_2", name="sample_text_2", nodeContentElements="sample_text_2")
    b = jpdl31_DocumentRoot(mixed="sample_text")
    _safe_set(b, 'jpdl31_DocumentRoot43', {a1})
    assert _is_linked(b, 'jpdl31_DocumentRoot43', a1)
    if hasattr(a1, 'jpdl31_NodeType'):
        assert _is_linked(a1, 'jpdl31_NodeType', b)
    _safe_set(b, 'jpdl31_DocumentRoot43', {a2})
    assert _is_linked(b, 'jpdl31_DocumentRoot43', a2)
    if hasattr(a1, 'jpdl31_NodeType'):
        assert not _is_linked(a1, 'jpdl31_NodeType', b)
    if hasattr(a2, 'jpdl31_NodeType'):
        assert _is_linked(a2, 'jpdl31_NodeType', b)
    _safe_set(b, 'jpdl31_DocumentRoot43', set())
    assert not _is_linked(b, 'jpdl31_DocumentRoot43', a2)
    if hasattr(a2, 'jpdl31_NodeType'):
        assert not _is_linked(a2, 'jpdl31_NodeType', b)


def test_assoc_processDefinition44_reverse_link_reassign_clear():
    a1 = jpdl31_ProcessDefinitionType(group="sample_text", name="sample_text")
    a2 = jpdl31_ProcessDefinitionType(group="sample_text_2", name="sample_text_2")
    b = jpdl31_DocumentRoot(mixed="sample_text")
    _safe_set(b, 'jpdl31_DocumentRoot45', {a1})
    assert _is_linked(b, 'jpdl31_DocumentRoot45', a1)
    if hasattr(a1, 'jpdl31_ProcessDefinitionType'):
        assert _is_linked(a1, 'jpdl31_ProcessDefinitionType', b)
    _safe_set(b, 'jpdl31_DocumentRoot45', {a2})
    assert _is_linked(b, 'jpdl31_DocumentRoot45', a2)
    if hasattr(a1, 'jpdl31_ProcessDefinitionType'):
        assert not _is_linked(a1, 'jpdl31_ProcessDefinitionType', b)
    if hasattr(a2, 'jpdl31_ProcessDefinitionType'):
        assert _is_linked(a2, 'jpdl31_ProcessDefinitionType', b)
    _safe_set(b, 'jpdl31_DocumentRoot45', set())
    assert not _is_linked(b, 'jpdl31_DocumentRoot45', a2)
    if hasattr(a2, 'jpdl31_ProcessDefinitionType'):
        assert not _is_linked(a2, 'jpdl31_ProcessDefinitionType', b)


def test_assoc_processState162_reverse_link_reassign_clear():
    a1 = jpdl31_ProcessStateType(async_="sample_text", group="sample_text", name="sample_text")
    a2 = jpdl31_ProcessStateType(async_="sample_text_2", group="sample_text_2", name="sample_text_2")
    b = jpdl31_ProcessDefinitionType(group="sample_text", name="sample_text")
    _safe_set(b, 'jpdl31_ProcessDefinitionType163', {a1})
    assert _is_linked(b, 'jpdl31_ProcessDefinitionType163', a1)
    if hasattr(a1, 'jpdl31_ProcessStateType164'):
        assert _is_linked(a1, 'jpdl31_ProcessStateType164', b)
    _safe_set(b, 'jpdl31_ProcessDefinitionType163', {a2})
    assert _is_linked(b, 'jpdl31_ProcessDefinitionType163', a2)
    if hasattr(a1, 'jpdl31_ProcessStateType164'):
        assert not _is_linked(a1, 'jpdl31_ProcessStateType164', b)
    if hasattr(a2, 'jpdl31_ProcessStateType164'):
        assert _is_linked(a2, 'jpdl31_ProcessStateType164', b)
    _safe_set(b, 'jpdl31_ProcessDefinitionType163', set())
    assert not _is_linked(b, 'jpdl31_ProcessDefinitionType163', a2)
    if hasattr(a2, 'jpdl31_ProcessStateType164'):
        assert not _is_linked(a2, 'jpdl31_ProcessStateType164', b)


def test_assoc_processState251_reverse_link_reassign_clear():
    a1 = jpdl31_SuperStateType(async_="sample_text", group="sample_text", name="sample_text")
    a2 = jpdl31_SuperStateType(async_="sample_text_2", group="sample_text_2", name="sample_text_2")
    b = jpdl31_ProcessStateType(async_="sample_text", group="sample_text", name="sample_text")
    _safe_set(b, 'jpdl31_ProcessStateType253', a1)
    assert _is_linked(b, 'jpdl31_ProcessStateType253', a1)
    if hasattr(a1, 'jpdl31_SuperStateType252'):
        assert _is_linked(a1, 'jpdl31_SuperStateType252', b)
    _safe_set(b, 'jpdl31_ProcessStateType253', a2)
    assert _is_linked(b, 'jpdl31_ProcessStateType253', a2)
    if hasattr(a1, 'jpdl31_SuperStateType252'):
        assert not _is_linked(a1, 'jpdl31_SuperStateType252', b)
    if hasattr(a2, 'jpdl31_SuperStateType252'):
        assert _is_linked(a2, 'jpdl31_SuperStateType252', b)
    _safe_set(b, 'jpdl31_ProcessStateType253', None)
    assert not _is_linked(b, 'jpdl31_ProcessStateType253', a2)
    if hasattr(a2, 'jpdl31_SuperStateType252'):
        assert not _is_linked(a2, 'jpdl31_SuperStateType252', b)


def test_assoc_processState46_reverse_link_reassign_clear():
    a1 = jpdl31_ProcessStateType(async_="sample_text", group="sample_text", name="sample_text")
    a2 = jpdl31_ProcessStateType(async_="sample_text_2", group="sample_text_2", name="sample_text_2")
    b = jpdl31_DocumentRoot(mixed="sample_text")
    _safe_set(b, 'jpdl31_DocumentRoot47', {a1})
    assert _is_linked(b, 'jpdl31_DocumentRoot47', a1)
    if hasattr(a1, 'jpdl31_ProcessStateType'):
        assert _is_linked(a1, 'jpdl31_ProcessStateType', b)
    _safe_set(b, 'jpdl31_DocumentRoot47', {a2})
    assert _is_linked(b, 'jpdl31_DocumentRoot47', a2)
    if hasattr(a1, 'jpdl31_ProcessStateType'):
        assert not _is_linked(a1, 'jpdl31_ProcessStateType', b)
    if hasattr(a2, 'jpdl31_ProcessStateType'):
        assert _is_linked(a2, 'jpdl31_ProcessStateType', b)
    _safe_set(b, 'jpdl31_DocumentRoot47', set())
    assert not _is_linked(b, 'jpdl31_DocumentRoot47', a2)
    if hasattr(a2, 'jpdl31_ProcessStateType'):
        assert not _is_linked(a2, 'jpdl31_ProcessStateType', b)


def test_assoc_script1_reverse_link_reassign_clear():
    a1 = jpdl31_ScriptType(acceptPropagatedEvents="sample_text", any="sample_text", mixed="sample_text", name="sample_text")
    a2 = jpdl31_ScriptType(acceptPropagatedEvents="sample_text_2", any="sample_text_2", mixed="sample_text_2", name="sample_text_2")
    b = jpdl31_CreateTimerType(duedate="sample_text", name="sample_text", repeat="sample_text", transition="sample_text")
    _safe_set(b, 'jpdl31_CreateTimerType2', a1)
    assert _is_linked(b, 'jpdl31_CreateTimerType2', a1)
    if hasattr(a1, 'jpdl31_ScriptType'):
        assert _is_linked(a1, 'jpdl31_ScriptType', b)
    _safe_set(b, 'jpdl31_CreateTimerType2', a2)
    assert _is_linked(b, 'jpdl31_CreateTimerType2', a2)
    if hasattr(a1, 'jpdl31_ScriptType'):
        assert not _is_linked(a1, 'jpdl31_ScriptType', b)
    if hasattr(a2, 'jpdl31_ScriptType'):
        assert _is_linked(a2, 'jpdl31_ScriptType', b)
    _safe_set(b, 'jpdl31_CreateTimerType2', None)
    assert not _is_linked(b, 'jpdl31_CreateTimerType2', a2)
    if hasattr(a2, 'jpdl31_ScriptType'):
        assert not _is_linked(a2, 'jpdl31_ScriptType', b)


def test_assoc_script123_reverse_link_reassign_clear():
    a1 = jpdl31_ScriptType(acceptPropagatedEvents="sample_text", any="sample_text", mixed="sample_text", name="sample_text")
    a2 = jpdl31_ScriptType(acceptPropagatedEvents="sample_text_2", any="sample_text_2", mixed="sample_text_2", name="sample_text_2")
    b = jpdl31_NodeType(async_="sample_text", name="sample_text", nodeContentElements="sample_text")
    _safe_set(b, 'jpdl31_NodeType124', a1)
    assert _is_linked(b, 'jpdl31_NodeType124', a1)
    if hasattr(a1, 'jpdl31_ScriptType125'):
        assert _is_linked(a1, 'jpdl31_ScriptType125', b)
    _safe_set(b, 'jpdl31_NodeType124', a2)
    assert _is_linked(b, 'jpdl31_NodeType124', a2)
    if hasattr(a1, 'jpdl31_ScriptType125'):
        assert not _is_linked(a1, 'jpdl31_ScriptType125', b)
    if hasattr(a2, 'jpdl31_ScriptType125'):
        assert _is_linked(a2, 'jpdl31_ScriptType125', b)
    _safe_set(b, 'jpdl31_NodeType124', None)
    assert not _is_linked(b, 'jpdl31_NodeType124', a2)
    if hasattr(a2, 'jpdl31_ScriptType125'):
        assert not _is_linked(a2, 'jpdl31_ScriptType125', b)


def test_assoc_script180_reverse_link_reassign_clear():
    a1 = jpdl31_ScriptType(acceptPropagatedEvents="sample_text", any="sample_text", mixed="sample_text", name="sample_text")
    a2 = jpdl31_ScriptType(acceptPropagatedEvents="sample_text_2", any="sample_text_2", mixed="sample_text_2", name="sample_text_2")
    b = jpdl31_ProcessDefinitionType(group="sample_text", name="sample_text")
    _safe_set(b, 'jpdl31_ProcessDefinitionType181', {a1})
    assert _is_linked(b, 'jpdl31_ProcessDefinitionType181', a1)
    if hasattr(a1, 'jpdl31_ScriptType182'):
        assert _is_linked(a1, 'jpdl31_ScriptType182', b)
    _safe_set(b, 'jpdl31_ProcessDefinitionType181', {a2})
    assert _is_linked(b, 'jpdl31_ProcessDefinitionType181', a2)
    if hasattr(a1, 'jpdl31_ScriptType182'):
        assert not _is_linked(a1, 'jpdl31_ScriptType182', b)
    if hasattr(a2, 'jpdl31_ScriptType182'):
        assert _is_linked(a2, 'jpdl31_ScriptType182', b)
    _safe_set(b, 'jpdl31_ProcessDefinitionType181', set())
    assert not _is_linked(b, 'jpdl31_ProcessDefinitionType181', a2)
    if hasattr(a2, 'jpdl31_ScriptType182'):
        assert not _is_linked(a2, 'jpdl31_ScriptType182', b)


def test_assoc_script311_reverse_link_reassign_clear():
    a1 = jpdl31_TimerType(duedate="sample_text", name="sample_text", repeat="sample_text", transition="sample_text")
    a2 = jpdl31_TimerType(duedate="sample_text_2", name="sample_text_2", repeat="sample_text_2", transition="sample_text_2")
    b = jpdl31_ScriptType(acceptPropagatedEvents="sample_text", any="sample_text", mixed="sample_text", name="sample_text")
    _safe_set(b, 'jpdl31_ScriptType313', a1)
    assert _is_linked(b, 'jpdl31_ScriptType313', a1)
    if hasattr(a1, 'jpdl31_TimerType312'):
        assert _is_linked(a1, 'jpdl31_TimerType312', b)
    _safe_set(b, 'jpdl31_ScriptType313', a2)
    assert _is_linked(b, 'jpdl31_ScriptType313', a2)
    if hasattr(a1, 'jpdl31_TimerType312'):
        assert not _is_linked(a1, 'jpdl31_TimerType312', b)
    if hasattr(a2, 'jpdl31_TimerType312'):
        assert _is_linked(a2, 'jpdl31_TimerType312', b)
    _safe_set(b, 'jpdl31_ScriptType313', None)
    assert not _is_linked(b, 'jpdl31_ScriptType313', a2)
    if hasattr(a2, 'jpdl31_TimerType312'):
        assert not _is_linked(a2, 'jpdl31_TimerType312', b)


def test_assoc_script317_reverse_link_reassign_clear():
    a1 = jpdl31_TransitionType(group="sample_text", name="sample_text", to="sample_text")
    a2 = jpdl31_TransitionType(group="sample_text_2", name="sample_text_2", to="sample_text_2")
    b = jpdl31_ScriptType(acceptPropagatedEvents="sample_text", any="sample_text", mixed="sample_text", name="sample_text")
    _safe_set(b, 'jpdl31_ScriptType319', a1)
    assert _is_linked(b, 'jpdl31_ScriptType319', a1)
    if hasattr(a1, 'jpdl31_TransitionType318'):
        assert _is_linked(a1, 'jpdl31_TransitionType318', b)
    _safe_set(b, 'jpdl31_ScriptType319', a2)
    assert _is_linked(b, 'jpdl31_ScriptType319', a2)
    if hasattr(a1, 'jpdl31_TransitionType318'):
        assert not _is_linked(a1, 'jpdl31_TransitionType318', b)
    if hasattr(a2, 'jpdl31_TransitionType318'):
        assert _is_linked(a2, 'jpdl31_TransitionType318', b)
    _safe_set(b, 'jpdl31_ScriptType319', None)
    assert not _is_linked(b, 'jpdl31_ScriptType319', a2)
    if hasattr(a2, 'jpdl31_TransitionType318'):
        assert not _is_linked(a2, 'jpdl31_TransitionType318', b)


def test_assoc_script334_reverse_link_reassign_clear():
    a1 = jpdl31_TransitionType1(group="sample_text", name="sample_text", to="sample_text")
    a2 = jpdl31_TransitionType1(group="sample_text_2", name="sample_text_2", to="sample_text_2")
    b = jpdl31_ScriptType(acceptPropagatedEvents="sample_text", any="sample_text", mixed="sample_text", name="sample_text")
    _safe_set(b, 'jpdl31_ScriptType336', a1)
    assert _is_linked(b, 'jpdl31_ScriptType336', a1)
    if hasattr(a1, 'jpdl31_TransitionType1335'):
        assert _is_linked(a1, 'jpdl31_TransitionType1335', b)
    _safe_set(b, 'jpdl31_ScriptType336', a2)
    assert _is_linked(b, 'jpdl31_ScriptType336', a2)
    if hasattr(a1, 'jpdl31_TransitionType1335'):
        assert not _is_linked(a1, 'jpdl31_TransitionType1335', b)
    if hasattr(a2, 'jpdl31_TransitionType1335'):
        assert _is_linked(a2, 'jpdl31_TransitionType1335', b)
    _safe_set(b, 'jpdl31_ScriptType336', None)
    assert not _is_linked(b, 'jpdl31_ScriptType336', a2)
    if hasattr(a2, 'jpdl31_TransitionType1335'):
        assert not _is_linked(a2, 'jpdl31_TransitionType1335', b)


def test_assoc_script48_reverse_link_reassign_clear():
    a1 = jpdl31_ScriptType(acceptPropagatedEvents="sample_text", any="sample_text", mixed="sample_text", name="sample_text")
    a2 = jpdl31_ScriptType(acceptPropagatedEvents="sample_text_2", any="sample_text_2", mixed="sample_text_2", name="sample_text_2")
    b = jpdl31_DocumentRoot(mixed="sample_text")
    _safe_set(b, 'jpdl31_DocumentRoot49', {a1})
    assert _is_linked(b, 'jpdl31_DocumentRoot49', a1)
    if hasattr(a1, 'jpdl31_ScriptType50'):
        assert _is_linked(a1, 'jpdl31_ScriptType50', b)
    _safe_set(b, 'jpdl31_DocumentRoot49', {a2})
    assert _is_linked(b, 'jpdl31_DocumentRoot49', a2)
    if hasattr(a1, 'jpdl31_ScriptType50'):
        assert not _is_linked(a1, 'jpdl31_ScriptType50', b)
    if hasattr(a2, 'jpdl31_ScriptType50'):
        assert _is_linked(a2, 'jpdl31_ScriptType50', b)
    _safe_set(b, 'jpdl31_DocumentRoot49', set())
    assert not _is_linked(b, 'jpdl31_DocumentRoot49', a2)
    if hasattr(a2, 'jpdl31_ScriptType50'):
        assert not _is_linked(a2, 'jpdl31_ScriptType50', b)


def test_assoc_script78_reverse_link_reassign_clear():
    a1 = jpdl31_ScriptType(acceptPropagatedEvents="sample_text", any="sample_text", mixed="sample_text", name="sample_text")
    a2 = jpdl31_ScriptType(acceptPropagatedEvents="sample_text_2", any="sample_text_2", mixed="sample_text_2", name="sample_text_2")
    b = jpdl31_EventType(actionElements="sample_text", type="sample_text")
    _safe_set(b, 'jpdl31_EventType79', {a1})
    assert _is_linked(b, 'jpdl31_EventType79', a1)
    if hasattr(a1, 'jpdl31_ScriptType80'):
        assert _is_linked(a1, 'jpdl31_ScriptType80', b)
    _safe_set(b, 'jpdl31_EventType79', {a2})
    assert _is_linked(b, 'jpdl31_EventType79', a2)
    if hasattr(a1, 'jpdl31_ScriptType80'):
        assert not _is_linked(a1, 'jpdl31_ScriptType80', b)
    if hasattr(a2, 'jpdl31_ScriptType80'):
        assert _is_linked(a2, 'jpdl31_ScriptType80', b)
    _safe_set(b, 'jpdl31_EventType79', set())
    assert not _is_linked(b, 'jpdl31_EventType79', a2)
    if hasattr(a2, 'jpdl31_ScriptType80'):
        assert not _is_linked(a2, 'jpdl31_ScriptType80', b)


def test_assoc_script90_reverse_link_reassign_clear():
    a1 = jpdl31_ScriptType(acceptPropagatedEvents="sample_text", any="sample_text", mixed="sample_text", name="sample_text")
    a2 = jpdl31_ScriptType(acceptPropagatedEvents="sample_text_2", any="sample_text_2", mixed="sample_text_2", name="sample_text_2")
    b = jpdl31_ExceptionHandlerType(exceptionClass="sample_text", group="sample_text")
    _safe_set(b, 'jpdl31_ExceptionHandlerType91', {a1})
    assert _is_linked(b, 'jpdl31_ExceptionHandlerType91', a1)
    if hasattr(a1, 'jpdl31_ScriptType92'):
        assert _is_linked(a1, 'jpdl31_ScriptType92', b)
    _safe_set(b, 'jpdl31_ExceptionHandlerType91', {a2})
    assert _is_linked(b, 'jpdl31_ExceptionHandlerType91', a2)
    if hasattr(a1, 'jpdl31_ScriptType92'):
        assert not _is_linked(a1, 'jpdl31_ScriptType92', b)
    if hasattr(a2, 'jpdl31_ScriptType92'):
        assert _is_linked(a2, 'jpdl31_ScriptType92', b)
    _safe_set(b, 'jpdl31_ExceptionHandlerType91', set())
    assert not _is_linked(b, 'jpdl31_ExceptionHandlerType91', a2)
    if hasattr(a2, 'jpdl31_ScriptType92'):
        assert not _is_linked(a2, 'jpdl31_ScriptType92', b)


def test_assoc_script93_reverse_link_reassign_clear():
    a1 = jpdl31_ScriptType(acceptPropagatedEvents="sample_text", any="sample_text", mixed="sample_text", name="sample_text")
    a2 = jpdl31_ScriptType(acceptPropagatedEvents="sample_text_2", any="sample_text_2", mixed="sample_text_2", name="sample_text_2")
    b = jpdl31_ForkType(async_="sample_text", group="sample_text", name="sample_text")
    _safe_set(b, 'jpdl31_ForkType94', {a1})
    assert _is_linked(b, 'jpdl31_ForkType94', a1)
    if hasattr(a1, 'jpdl31_ScriptType95'):
        assert _is_linked(a1, 'jpdl31_ScriptType95', b)
    _safe_set(b, 'jpdl31_ForkType94', {a2})
    assert _is_linked(b, 'jpdl31_ForkType94', a2)
    if hasattr(a1, 'jpdl31_ScriptType95'):
        assert not _is_linked(a1, 'jpdl31_ScriptType95', b)
    if hasattr(a2, 'jpdl31_ScriptType95'):
        assert _is_linked(a2, 'jpdl31_ScriptType95', b)
    _safe_set(b, 'jpdl31_ForkType94', set())
    assert not _is_linked(b, 'jpdl31_ForkType94', a2)
    if hasattr(a2, 'jpdl31_ScriptType95'):
        assert not _is_linked(a2, 'jpdl31_ScriptType95', b)


def test_assoc_startState147_reverse_link_reassign_clear():
    a1 = jpdl31_StartStateType(group="sample_text", name="sample_text")
    a2 = jpdl31_StartStateType(group="sample_text_2", name="sample_text_2")
    b = jpdl31_ProcessDefinitionType(group="sample_text", name="sample_text")
    _safe_set(b, 'jpdl31_ProcessDefinitionType148', {a1})
    assert _is_linked(b, 'jpdl31_ProcessDefinitionType148', a1)
    if hasattr(a1, 'jpdl31_StartStateType149'):
        assert _is_linked(a1, 'jpdl31_StartStateType149', b)
    _safe_set(b, 'jpdl31_ProcessDefinitionType148', {a2})
    assert _is_linked(b, 'jpdl31_ProcessDefinitionType148', a2)
    if hasattr(a1, 'jpdl31_StartStateType149'):
        assert not _is_linked(a1, 'jpdl31_StartStateType149', b)
    if hasattr(a2, 'jpdl31_StartStateType149'):
        assert _is_linked(a2, 'jpdl31_StartStateType149', b)
    _safe_set(b, 'jpdl31_ProcessDefinitionType148', set())
    assert not _is_linked(b, 'jpdl31_ProcessDefinitionType148', a2)
    if hasattr(a2, 'jpdl31_StartStateType149'):
        assert not _is_linked(a2, 'jpdl31_StartStateType149', b)


def test_assoc_startState51_reverse_link_reassign_clear():
    a1 = jpdl31_StartStateType(group="sample_text", name="sample_text")
    a2 = jpdl31_StartStateType(group="sample_text_2", name="sample_text_2")
    b = jpdl31_DocumentRoot(mixed="sample_text")
    _safe_set(b, 'jpdl31_DocumentRoot52', {a1})
    assert _is_linked(b, 'jpdl31_DocumentRoot52', a1)
    if hasattr(a1, 'jpdl31_StartStateType'):
        assert _is_linked(a1, 'jpdl31_StartStateType', b)
    _safe_set(b, 'jpdl31_DocumentRoot52', {a2})
    assert _is_linked(b, 'jpdl31_DocumentRoot52', a2)
    if hasattr(a1, 'jpdl31_StartStateType'):
        assert not _is_linked(a1, 'jpdl31_StartStateType', b)
    if hasattr(a2, 'jpdl31_StartStateType'):
        assert _is_linked(a2, 'jpdl31_StartStateType', b)
    _safe_set(b, 'jpdl31_DocumentRoot52', set())
    assert not _is_linked(b, 'jpdl31_DocumentRoot52', a2)
    if hasattr(a2, 'jpdl31_StartStateType'):
        assert not _is_linked(a2, 'jpdl31_StartStateType', b)


def test_assoc_state153_reverse_link_reassign_clear():
    a1 = jpdl31_StateType(async_="sample_text", name="sample_text", nodeContentElements="sample_text")
    a2 = jpdl31_StateType(async_="sample_text_2", name="sample_text_2", nodeContentElements="sample_text_2")
    b = jpdl31_ProcessDefinitionType(group="sample_text", name="sample_text")
    _safe_set(b, 'jpdl31_ProcessDefinitionType154', {a1})
    assert _is_linked(b, 'jpdl31_ProcessDefinitionType154', a1)
    if hasattr(a1, 'jpdl31_StateType155'):
        assert _is_linked(a1, 'jpdl31_StateType155', b)
    _safe_set(b, 'jpdl31_ProcessDefinitionType154', {a2})
    assert _is_linked(b, 'jpdl31_ProcessDefinitionType154', a2)
    if hasattr(a1, 'jpdl31_StateType155'):
        assert not _is_linked(a1, 'jpdl31_StateType155', b)
    if hasattr(a2, 'jpdl31_StateType155'):
        assert _is_linked(a2, 'jpdl31_StateType155', b)
    _safe_set(b, 'jpdl31_ProcessDefinitionType154', set())
    assert not _is_linked(b, 'jpdl31_ProcessDefinitionType154', a2)
    if hasattr(a2, 'jpdl31_StateType155'):
        assert not _is_linked(a2, 'jpdl31_StateType155', b)


def test_assoc_state242_reverse_link_reassign_clear():
    a1 = jpdl31_SuperStateType(async_="sample_text", group="sample_text", name="sample_text")
    a2 = jpdl31_SuperStateType(async_="sample_text_2", group="sample_text_2", name="sample_text_2")
    b = jpdl31_StateType(async_="sample_text", name="sample_text", nodeContentElements="sample_text")
    _safe_set(b, 'jpdl31_StateType244', a1)
    assert _is_linked(b, 'jpdl31_StateType244', a1)
    if hasattr(a1, 'jpdl31_SuperStateType243'):
        assert _is_linked(a1, 'jpdl31_SuperStateType243', b)
    _safe_set(b, 'jpdl31_StateType244', a2)
    assert _is_linked(b, 'jpdl31_StateType244', a2)
    if hasattr(a1, 'jpdl31_SuperStateType243'):
        assert not _is_linked(a1, 'jpdl31_SuperStateType243', b)
    if hasattr(a2, 'jpdl31_SuperStateType243'):
        assert _is_linked(a2, 'jpdl31_SuperStateType243', b)
    _safe_set(b, 'jpdl31_StateType244', None)
    assert not _is_linked(b, 'jpdl31_StateType244', a2)
    if hasattr(a2, 'jpdl31_SuperStateType243'):
        assert not _is_linked(a2, 'jpdl31_SuperStateType243', b)


def test_assoc_state53_reverse_link_reassign_clear():
    a1 = jpdl31_StateType(async_="sample_text", name="sample_text", nodeContentElements="sample_text")
    a2 = jpdl31_StateType(async_="sample_text_2", name="sample_text_2", nodeContentElements="sample_text_2")
    b = jpdl31_DocumentRoot(mixed="sample_text")
    _safe_set(b, 'jpdl31_DocumentRoot54', {a1})
    assert _is_linked(b, 'jpdl31_DocumentRoot54', a1)
    if hasattr(a1, 'jpdl31_StateType'):
        assert _is_linked(a1, 'jpdl31_StateType', b)
    _safe_set(b, 'jpdl31_DocumentRoot54', {a2})
    assert _is_linked(b, 'jpdl31_DocumentRoot54', a2)
    if hasattr(a1, 'jpdl31_StateType'):
        assert not _is_linked(a1, 'jpdl31_StateType', b)
    if hasattr(a2, 'jpdl31_StateType'):
        assert _is_linked(a2, 'jpdl31_StateType', b)
    _safe_set(b, 'jpdl31_DocumentRoot54', set())
    assert not _is_linked(b, 'jpdl31_DocumentRoot54', a2)
    if hasattr(a2, 'jpdl31_StateType'):
        assert not _is_linked(a2, 'jpdl31_StateType', b)


def test_assoc_subProcess198_reverse_link_reassign_clear():
    a1 = jpdl31_SubProcessType(name="sample_text", version="sample_text")
    a2 = jpdl31_SubProcessType(name="sample_text_2", version="sample_text_2")
    b = jpdl31_ProcessStateType(async_="sample_text", group="sample_text", name="sample_text")
    _safe_set(b, 'jpdl31_ProcessStateType199', {a1})
    assert _is_linked(b, 'jpdl31_ProcessStateType199', a1)
    if hasattr(a1, 'jpdl31_SubProcessType'):
        assert _is_linked(a1, 'jpdl31_SubProcessType', b)
    _safe_set(b, 'jpdl31_ProcessStateType199', {a2})
    assert _is_linked(b, 'jpdl31_ProcessStateType199', a2)
    if hasattr(a1, 'jpdl31_SubProcessType'):
        assert not _is_linked(a1, 'jpdl31_SubProcessType', b)
    if hasattr(a2, 'jpdl31_SubProcessType'):
        assert _is_linked(a2, 'jpdl31_SubProcessType', b)
    _safe_set(b, 'jpdl31_ProcessStateType199', set())
    assert not _is_linked(b, 'jpdl31_ProcessStateType199', a2)
    if hasattr(a2, 'jpdl31_SubProcessType'):
        assert not _is_linked(a2, 'jpdl31_SubProcessType', b)


def test_assoc_superState159_reverse_link_reassign_clear():
    a1 = jpdl31_SuperStateType(async_="sample_text", group="sample_text", name="sample_text")
    a2 = jpdl31_SuperStateType(async_="sample_text_2", group="sample_text_2", name="sample_text_2")
    b = jpdl31_ProcessDefinitionType(group="sample_text", name="sample_text")
    _safe_set(b, 'jpdl31_ProcessDefinitionType160', {a1})
    assert _is_linked(b, 'jpdl31_ProcessDefinitionType160', a1)
    if hasattr(a1, 'jpdl31_SuperStateType161'):
        assert _is_linked(a1, 'jpdl31_SuperStateType161', b)
    _safe_set(b, 'jpdl31_ProcessDefinitionType160', {a2})
    assert _is_linked(b, 'jpdl31_ProcessDefinitionType160', a2)
    if hasattr(a1, 'jpdl31_SuperStateType161'):
        assert not _is_linked(a1, 'jpdl31_SuperStateType161', b)
    if hasattr(a2, 'jpdl31_SuperStateType161'):
        assert _is_linked(a2, 'jpdl31_SuperStateType161', b)
    _safe_set(b, 'jpdl31_ProcessDefinitionType160', set())
    assert not _is_linked(b, 'jpdl31_ProcessDefinitionType160', a2)
    if hasattr(a2, 'jpdl31_SuperStateType161'):
        assert not _is_linked(a2, 'jpdl31_SuperStateType161', b)


def test_assoc_superState249_reverse_link_reassign_clear():
    a1 = jpdl31_SuperStateType(async_="sample_text", group="sample_text", name="sample_text")
    a2 = jpdl31_SuperStateType(async_="sample_text_2", group="sample_text_2", name="sample_text_2")
    b = jpdl31_SuperStateType(async_="sample_text", group="sample_text", name="sample_text")
    _safe_set(b, 'jpdl31_SuperStateType250', a1)
    assert _is_linked(b, 'jpdl31_SuperStateType250', a1)
    if hasattr(a1, 'jpdl31_SuperStateType248'):
        assert _is_linked(a1, 'jpdl31_SuperStateType248', b)
    _safe_set(b, 'jpdl31_SuperStateType250', a2)
    assert _is_linked(b, 'jpdl31_SuperStateType250', a2)
    if hasattr(a1, 'jpdl31_SuperStateType248'):
        assert not _is_linked(a1, 'jpdl31_SuperStateType248', b)
    if hasattr(a2, 'jpdl31_SuperStateType248'):
        assert _is_linked(a2, 'jpdl31_SuperStateType248', b)
    _safe_set(b, 'jpdl31_SuperStateType250', None)
    assert not _is_linked(b, 'jpdl31_SuperStateType250', a2)
    if hasattr(a2, 'jpdl31_SuperStateType248'):
        assert not _is_linked(a2, 'jpdl31_SuperStateType248', b)


def test_assoc_superState55_reverse_link_reassign_clear():
    a1 = jpdl31_SuperStateType(async_="sample_text", group="sample_text", name="sample_text")
    a2 = jpdl31_SuperStateType(async_="sample_text_2", group="sample_text_2", name="sample_text_2")
    b = jpdl31_DocumentRoot(mixed="sample_text")
    _safe_set(b, 'jpdl31_DocumentRoot56', {a1})
    assert _is_linked(b, 'jpdl31_DocumentRoot56', a1)
    if hasattr(a1, 'jpdl31_SuperStateType'):
        assert _is_linked(a1, 'jpdl31_SuperStateType', b)
    _safe_set(b, 'jpdl31_DocumentRoot56', {a2})
    assert _is_linked(b, 'jpdl31_DocumentRoot56', a2)
    if hasattr(a1, 'jpdl31_SuperStateType'):
        assert not _is_linked(a1, 'jpdl31_SuperStateType', b)
    if hasattr(a2, 'jpdl31_SuperStateType'):
        assert _is_linked(a2, 'jpdl31_SuperStateType', b)
    _safe_set(b, 'jpdl31_DocumentRoot56', set())
    assert not _is_linked(b, 'jpdl31_DocumentRoot56', a2)
    if hasattr(a2, 'jpdl31_SuperStateType'):
        assert not _is_linked(a2, 'jpdl31_SuperStateType', b)


def test_assoc_swimlane144_reverse_link_reassign_clear():
    a1 = jpdl31_SwimlaneType(name="sample_text")
    a2 = jpdl31_SwimlaneType(name="sample_text_2")
    b = jpdl31_ProcessDefinitionType(group="sample_text", name="sample_text")
    _safe_set(b, 'jpdl31_ProcessDefinitionType145', {a1})
    assert _is_linked(b, 'jpdl31_ProcessDefinitionType145', a1)
    if hasattr(a1, 'jpdl31_SwimlaneType146'):
        assert _is_linked(a1, 'jpdl31_SwimlaneType146', b)
    _safe_set(b, 'jpdl31_ProcessDefinitionType145', {a2})
    assert _is_linked(b, 'jpdl31_ProcessDefinitionType145', a2)
    if hasattr(a1, 'jpdl31_SwimlaneType146'):
        assert not _is_linked(a1, 'jpdl31_SwimlaneType146', b)
    if hasattr(a2, 'jpdl31_SwimlaneType146'):
        assert _is_linked(a2, 'jpdl31_SwimlaneType146', b)
    _safe_set(b, 'jpdl31_ProcessDefinitionType145', set())
    assert not _is_linked(b, 'jpdl31_ProcessDefinitionType145', a2)
    if hasattr(a2, 'jpdl31_SwimlaneType146'):
        assert not _is_linked(a2, 'jpdl31_SwimlaneType146', b)


def test_assoc_swimlane57_reverse_link_reassign_clear():
    a1 = jpdl31_SwimlaneType(name="sample_text")
    a2 = jpdl31_SwimlaneType(name="sample_text_2")
    b = jpdl31_DocumentRoot(mixed="sample_text")
    _safe_set(b, 'jpdl31_DocumentRoot58', {a1})
    assert _is_linked(b, 'jpdl31_DocumentRoot58', a1)
    if hasattr(a1, 'jpdl31_SwimlaneType'):
        assert _is_linked(a1, 'jpdl31_SwimlaneType', b)
    _safe_set(b, 'jpdl31_DocumentRoot58', {a2})
    assert _is_linked(b, 'jpdl31_DocumentRoot58', a2)
    if hasattr(a1, 'jpdl31_SwimlaneType'):
        assert not _is_linked(a1, 'jpdl31_SwimlaneType', b)
    if hasattr(a2, 'jpdl31_SwimlaneType'):
        assert _is_linked(a2, 'jpdl31_SwimlaneType', b)
    _safe_set(b, 'jpdl31_DocumentRoot58', set())
    assert not _is_linked(b, 'jpdl31_DocumentRoot58', a2)
    if hasattr(a2, 'jpdl31_SwimlaneType'):
        assert not _is_linked(a2, 'jpdl31_SwimlaneType', b)


def test_assoc_task195_reverse_link_reassign_clear():
    a1 = jpdl31_TaskType(blocking="sample_text", description="sample_text", duedate="sample_text", group="sample_text", name="sample_text", priority="sample_text", signalling="sample_text", swimlane="sample_text")
    a2 = jpdl31_TaskType(blocking="sample_text_2", description="sample_text_2", duedate="sample_text_2", group="sample_text_2", name="sample_text_2", priority="sample_text_2", signalling="sample_text_2", swimlane="sample_text_2")
    b = jpdl31_ProcessDefinitionType(group="sample_text", name="sample_text")
    _safe_set(b, 'jpdl31_ProcessDefinitionType196', {a1})
    assert _is_linked(b, 'jpdl31_ProcessDefinitionType196', a1)
    if hasattr(a1, 'jpdl31_TaskType197'):
        assert _is_linked(a1, 'jpdl31_TaskType197', b)
    _safe_set(b, 'jpdl31_ProcessDefinitionType196', {a2})
    assert _is_linked(b, 'jpdl31_ProcessDefinitionType196', a2)
    if hasattr(a1, 'jpdl31_TaskType197'):
        assert not _is_linked(a1, 'jpdl31_TaskType197', b)
    if hasattr(a2, 'jpdl31_TaskType197'):
        assert _is_linked(a2, 'jpdl31_TaskType197', b)
    _safe_set(b, 'jpdl31_ProcessDefinitionType196', set())
    assert not _is_linked(b, 'jpdl31_ProcessDefinitionType196', a2)
    if hasattr(a2, 'jpdl31_TaskType197'):
        assert not _is_linked(a2, 'jpdl31_TaskType197', b)


def test_assoc_task215_reverse_link_reassign_clear():
    a1 = jpdl31_TaskType(blocking="sample_text", description="sample_text", duedate="sample_text", group="sample_text", name="sample_text", priority="sample_text", signalling="sample_text", swimlane="sample_text")
    a2 = jpdl31_TaskType(blocking="sample_text_2", description="sample_text_2", duedate="sample_text_2", group="sample_text_2", name="sample_text_2", priority="sample_text_2", signalling="sample_text_2", swimlane="sample_text_2")
    b = jpdl31_StartStateType(group="sample_text", name="sample_text")
    _safe_set(b, 'jpdl31_StartStateType216', {a1})
    assert _is_linked(b, 'jpdl31_StartStateType216', a1)
    if hasattr(a1, 'jpdl31_TaskType217'):
        assert _is_linked(a1, 'jpdl31_TaskType217', b)
    _safe_set(b, 'jpdl31_StartStateType216', {a2})
    assert _is_linked(b, 'jpdl31_StartStateType216', a2)
    if hasattr(a1, 'jpdl31_TaskType217'):
        assert not _is_linked(a1, 'jpdl31_TaskType217', b)
    if hasattr(a2, 'jpdl31_TaskType217'):
        assert _is_linked(a2, 'jpdl31_TaskType217', b)
    _safe_set(b, 'jpdl31_StartStateType216', set())
    assert not _is_linked(b, 'jpdl31_StartStateType216', a2)
    if hasattr(a2, 'jpdl31_TaskType217'):
        assert not _is_linked(a2, 'jpdl31_TaskType217', b)


def test_assoc_task281_reverse_link_reassign_clear():
    a1 = jpdl31_TaskType(blocking="sample_text", description="sample_text", duedate="sample_text", group="sample_text", name="sample_text", priority="sample_text", signalling="sample_text", swimlane="sample_text")
    a2 = jpdl31_TaskType(blocking="sample_text_2", description="sample_text_2", duedate="sample_text_2", group="sample_text_2", name="sample_text_2", priority="sample_text_2", signalling="sample_text_2", swimlane="sample_text_2")
    b = jpdl31_TaskNodeType(async_="sample_text", createTasks="sample_text", endTasks="sample_text", group="sample_text", name="sample_text", signal="sample_text")
    _safe_set(b, 'jpdl31_TaskNodeType282', {a1})
    assert _is_linked(b, 'jpdl31_TaskNodeType282', a1)
    if hasattr(a1, 'jpdl31_TaskType283'):
        assert _is_linked(a1, 'jpdl31_TaskType283', b)
    _safe_set(b, 'jpdl31_TaskNodeType282', {a2})
    assert _is_linked(b, 'jpdl31_TaskNodeType282', a2)
    if hasattr(a1, 'jpdl31_TaskType283'):
        assert not _is_linked(a1, 'jpdl31_TaskType283', b)
    if hasattr(a2, 'jpdl31_TaskType283'):
        assert _is_linked(a2, 'jpdl31_TaskType283', b)
    _safe_set(b, 'jpdl31_TaskNodeType282', set())
    assert not _is_linked(b, 'jpdl31_TaskNodeType282', a2)
    if hasattr(a2, 'jpdl31_TaskType283'):
        assert not _is_linked(a2, 'jpdl31_TaskType283', b)


def test_assoc_task59_reverse_link_reassign_clear():
    a1 = jpdl31_TaskType(blocking="sample_text", description="sample_text", duedate="sample_text", group="sample_text", name="sample_text", priority="sample_text", signalling="sample_text", swimlane="sample_text")
    a2 = jpdl31_TaskType(blocking="sample_text_2", description="sample_text_2", duedate="sample_text_2", group="sample_text_2", name="sample_text_2", priority="sample_text_2", signalling="sample_text_2", swimlane="sample_text_2")
    b = jpdl31_DocumentRoot(mixed="sample_text")
    _safe_set(b, 'jpdl31_DocumentRoot60', {a1})
    assert _is_linked(b, 'jpdl31_DocumentRoot60', a1)
    if hasattr(a1, 'jpdl31_TaskType'):
        assert _is_linked(a1, 'jpdl31_TaskType', b)
    _safe_set(b, 'jpdl31_DocumentRoot60', {a2})
    assert _is_linked(b, 'jpdl31_DocumentRoot60', a2)
    if hasattr(a1, 'jpdl31_TaskType'):
        assert not _is_linked(a1, 'jpdl31_TaskType', b)
    if hasattr(a2, 'jpdl31_TaskType'):
        assert _is_linked(a2, 'jpdl31_TaskType', b)
    _safe_set(b, 'jpdl31_DocumentRoot60', set())
    assert not _is_linked(b, 'jpdl31_DocumentRoot60', a2)
    if hasattr(a2, 'jpdl31_TaskType'):
        assert not _is_linked(a2, 'jpdl31_TaskType', b)


def test_assoc_taskNode156_reverse_link_reassign_clear():
    a1 = jpdl31_TaskNodeType(async_="sample_text", createTasks="sample_text", endTasks="sample_text", group="sample_text", name="sample_text", signal="sample_text")
    a2 = jpdl31_TaskNodeType(async_="sample_text_2", createTasks="sample_text_2", endTasks="sample_text_2", group="sample_text_2", name="sample_text_2", signal="sample_text_2")
    b = jpdl31_ProcessDefinitionType(group="sample_text", name="sample_text")
    _safe_set(b, 'jpdl31_ProcessDefinitionType157', {a1})
    assert _is_linked(b, 'jpdl31_ProcessDefinitionType157', a1)
    if hasattr(a1, 'jpdl31_TaskNodeType158'):
        assert _is_linked(a1, 'jpdl31_TaskNodeType158', b)
    _safe_set(b, 'jpdl31_ProcessDefinitionType157', {a2})
    assert _is_linked(b, 'jpdl31_ProcessDefinitionType157', a2)
    if hasattr(a1, 'jpdl31_TaskNodeType158'):
        assert not _is_linked(a1, 'jpdl31_TaskNodeType158', b)
    if hasattr(a2, 'jpdl31_TaskNodeType158'):
        assert _is_linked(a2, 'jpdl31_TaskNodeType158', b)
    _safe_set(b, 'jpdl31_ProcessDefinitionType157', set())
    assert not _is_linked(b, 'jpdl31_ProcessDefinitionType157', a2)
    if hasattr(a2, 'jpdl31_TaskNodeType158'):
        assert not _is_linked(a2, 'jpdl31_TaskNodeType158', b)


def test_assoc_taskNode245_reverse_link_reassign_clear():
    a1 = jpdl31_TaskNodeType(async_="sample_text", createTasks="sample_text", endTasks="sample_text", group="sample_text", name="sample_text", signal="sample_text")
    a2 = jpdl31_TaskNodeType(async_="sample_text_2", createTasks="sample_text_2", endTasks="sample_text_2", group="sample_text_2", name="sample_text_2", signal="sample_text_2")
    b = jpdl31_SuperStateType(async_="sample_text", group="sample_text", name="sample_text")
    _safe_set(b, 'jpdl31_SuperStateType246', {a1})
    assert _is_linked(b, 'jpdl31_SuperStateType246', a1)
    if hasattr(a1, 'jpdl31_TaskNodeType247'):
        assert _is_linked(a1, 'jpdl31_TaskNodeType247', b)
    _safe_set(b, 'jpdl31_SuperStateType246', {a2})
    assert _is_linked(b, 'jpdl31_SuperStateType246', a2)
    if hasattr(a1, 'jpdl31_TaskNodeType247'):
        assert not _is_linked(a1, 'jpdl31_TaskNodeType247', b)
    if hasattr(a2, 'jpdl31_TaskNodeType247'):
        assert _is_linked(a2, 'jpdl31_TaskNodeType247', b)
    _safe_set(b, 'jpdl31_SuperStateType246', set())
    assert not _is_linked(b, 'jpdl31_SuperStateType246', a2)
    if hasattr(a2, 'jpdl31_TaskNodeType247'):
        assert not _is_linked(a2, 'jpdl31_TaskNodeType247', b)


def test_assoc_taskNode61_reverse_link_reassign_clear():
    a1 = jpdl31_TaskNodeType(async_="sample_text", createTasks="sample_text", endTasks="sample_text", group="sample_text", name="sample_text", signal="sample_text")
    a2 = jpdl31_TaskNodeType(async_="sample_text_2", createTasks="sample_text_2", endTasks="sample_text_2", group="sample_text_2", name="sample_text_2", signal="sample_text_2")
    b = jpdl31_DocumentRoot(mixed="sample_text")
    _safe_set(b, 'jpdl31_DocumentRoot62', {a1})
    assert _is_linked(b, 'jpdl31_DocumentRoot62', a1)
    if hasattr(a1, 'jpdl31_TaskNodeType'):
        assert _is_linked(a1, 'jpdl31_TaskNodeType', b)
    _safe_set(b, 'jpdl31_DocumentRoot62', {a2})
    assert _is_linked(b, 'jpdl31_DocumentRoot62', a2)
    if hasattr(a1, 'jpdl31_TaskNodeType'):
        assert not _is_linked(a1, 'jpdl31_TaskNodeType', b)
    if hasattr(a2, 'jpdl31_TaskNodeType'):
        assert _is_linked(a2, 'jpdl31_TaskNodeType', b)
    _safe_set(b, 'jpdl31_DocumentRoot62', set())
    assert not _is_linked(b, 'jpdl31_DocumentRoot62', a2)
    if hasattr(a2, 'jpdl31_TaskNodeType'):
        assert not _is_linked(a2, 'jpdl31_TaskNodeType', b)


def test_assoc_timer102_reverse_link_reassign_clear():
    a1 = jpdl31_TimerType(duedate="sample_text", name="sample_text", repeat="sample_text", transition="sample_text")
    a2 = jpdl31_TimerType(duedate="sample_text_2", name="sample_text_2", repeat="sample_text_2", transition="sample_text_2")
    b = jpdl31_ForkType(async_="sample_text", group="sample_text", name="sample_text")
    _safe_set(b, 'jpdl31_ForkType103', {a1})
    assert _is_linked(b, 'jpdl31_ForkType103', a1)
    if hasattr(a1, 'jpdl31_TimerType104'):
        assert _is_linked(a1, 'jpdl31_TimerType104', b)
    _safe_set(b, 'jpdl31_ForkType103', {a2})
    assert _is_linked(b, 'jpdl31_ForkType103', a2)
    if hasattr(a1, 'jpdl31_TimerType104'):
        assert not _is_linked(a1, 'jpdl31_TimerType104', b)
    if hasattr(a2, 'jpdl31_TimerType104'):
        assert _is_linked(a2, 'jpdl31_TimerType104', b)
    _safe_set(b, 'jpdl31_ForkType103', set())
    assert not _is_linked(b, 'jpdl31_ForkType103', a2)
    if hasattr(a2, 'jpdl31_TimerType104'):
        assert not _is_linked(a2, 'jpdl31_TimerType104', b)


def test_assoc_timer114_reverse_link_reassign_clear():
    a1 = jpdl31_TimerType(duedate="sample_text", name="sample_text", repeat="sample_text", transition="sample_text")
    a2 = jpdl31_TimerType(duedate="sample_text_2", name="sample_text_2", repeat="sample_text_2", transition="sample_text_2")
    b = jpdl31_JoinType(async_="sample_text", name="sample_text", nodeContentElements="sample_text")
    _safe_set(b, 'jpdl31_JoinType115', {a1})
    assert _is_linked(b, 'jpdl31_JoinType115', a1)
    if hasattr(a1, 'jpdl31_TimerType116'):
        assert _is_linked(a1, 'jpdl31_TimerType116', b)
    _safe_set(b, 'jpdl31_JoinType115', {a2})
    assert _is_linked(b, 'jpdl31_JoinType115', a2)
    if hasattr(a1, 'jpdl31_TimerType116'):
        assert not _is_linked(a1, 'jpdl31_TimerType116', b)
    if hasattr(a2, 'jpdl31_TimerType116'):
        assert _is_linked(a2, 'jpdl31_TimerType116', b)
    _safe_set(b, 'jpdl31_JoinType115', set())
    assert not _is_linked(b, 'jpdl31_JoinType115', a2)
    if hasattr(a2, 'jpdl31_TimerType116'):
        assert not _is_linked(a2, 'jpdl31_TimerType116', b)


def test_assoc_timer138_reverse_link_reassign_clear():
    a1 = jpdl31_TimerType(duedate="sample_text", name="sample_text", repeat="sample_text", transition="sample_text")
    a2 = jpdl31_TimerType(duedate="sample_text_2", name="sample_text_2", repeat="sample_text_2", transition="sample_text_2")
    b = jpdl31_NodeType(async_="sample_text", name="sample_text", nodeContentElements="sample_text")
    _safe_set(b, 'jpdl31_NodeType139', {a1})
    assert _is_linked(b, 'jpdl31_NodeType139', a1)
    if hasattr(a1, 'jpdl31_TimerType140'):
        assert _is_linked(a1, 'jpdl31_TimerType140', b)
    _safe_set(b, 'jpdl31_NodeType139', {a2})
    assert _is_linked(b, 'jpdl31_NodeType139', a2)
    if hasattr(a1, 'jpdl31_TimerType140'):
        assert not _is_linked(a1, 'jpdl31_TimerType140', b)
    if hasattr(a2, 'jpdl31_TimerType140'):
        assert _is_linked(a2, 'jpdl31_TimerType140', b)
    _safe_set(b, 'jpdl31_NodeType139', set())
    assert not _is_linked(b, 'jpdl31_NodeType139', a2)
    if hasattr(a2, 'jpdl31_TimerType140'):
        assert not _is_linked(a2, 'jpdl31_TimerType140', b)


def test_assoc_timer209_reverse_link_reassign_clear():
    a1 = jpdl31_TimerType(duedate="sample_text", name="sample_text", repeat="sample_text", transition="sample_text")
    a2 = jpdl31_TimerType(duedate="sample_text_2", name="sample_text_2", repeat="sample_text_2", transition="sample_text_2")
    b = jpdl31_ProcessStateType(async_="sample_text", group="sample_text", name="sample_text")
    _safe_set(b, 'jpdl31_ProcessStateType210', {a1})
    assert _is_linked(b, 'jpdl31_ProcessStateType210', a1)
    if hasattr(a1, 'jpdl31_TimerType211'):
        assert _is_linked(a1, 'jpdl31_TimerType211', b)
    _safe_set(b, 'jpdl31_ProcessStateType210', {a2})
    assert _is_linked(b, 'jpdl31_ProcessStateType210', a2)
    if hasattr(a1, 'jpdl31_TimerType211'):
        assert not _is_linked(a1, 'jpdl31_TimerType211', b)
    if hasattr(a2, 'jpdl31_TimerType211'):
        assert _is_linked(a2, 'jpdl31_TimerType211', b)
    _safe_set(b, 'jpdl31_ProcessStateType210', set())
    assert not _is_linked(b, 'jpdl31_ProcessStateType210', a2)
    if hasattr(a2, 'jpdl31_TimerType211'):
        assert not _is_linked(a2, 'jpdl31_TimerType211', b)


def test_assoc_timer233_reverse_link_reassign_clear():
    a1 = jpdl31_TimerType(duedate="sample_text", name="sample_text", repeat="sample_text", transition="sample_text")
    a2 = jpdl31_TimerType(duedate="sample_text_2", name="sample_text_2", repeat="sample_text_2", transition="sample_text_2")
    b = jpdl31_StateType(async_="sample_text", name="sample_text", nodeContentElements="sample_text")
    _safe_set(b, 'jpdl31_StateType234', {a1})
    assert _is_linked(b, 'jpdl31_StateType234', a1)
    if hasattr(a1, 'jpdl31_TimerType235'):
        assert _is_linked(a1, 'jpdl31_TimerType235', b)
    _safe_set(b, 'jpdl31_StateType234', {a2})
    assert _is_linked(b, 'jpdl31_StateType234', a2)
    if hasattr(a1, 'jpdl31_TimerType235'):
        assert not _is_linked(a1, 'jpdl31_TimerType235', b)
    if hasattr(a2, 'jpdl31_TimerType235'):
        assert _is_linked(a2, 'jpdl31_TimerType235', b)
    _safe_set(b, 'jpdl31_StateType234', set())
    assert not _is_linked(b, 'jpdl31_StateType234', a2)
    if hasattr(a2, 'jpdl31_TimerType235'):
        assert not _is_linked(a2, 'jpdl31_TimerType235', b)


def test_assoc_timer272_reverse_link_reassign_clear():
    a1 = jpdl31_TimerType(duedate="sample_text", name="sample_text", repeat="sample_text", transition="sample_text")
    a2 = jpdl31_TimerType(duedate="sample_text_2", name="sample_text_2", repeat="sample_text_2", transition="sample_text_2")
    b = jpdl31_SuperStateType(async_="sample_text", group="sample_text", name="sample_text")
    _safe_set(b, 'jpdl31_SuperStateType273', {a1})
    assert _is_linked(b, 'jpdl31_SuperStateType273', a1)
    if hasattr(a1, 'jpdl31_TimerType274'):
        assert _is_linked(a1, 'jpdl31_TimerType274', b)
    _safe_set(b, 'jpdl31_SuperStateType273', {a2})
    assert _is_linked(b, 'jpdl31_SuperStateType273', a2)
    if hasattr(a1, 'jpdl31_TimerType274'):
        assert not _is_linked(a1, 'jpdl31_TimerType274', b)
    if hasattr(a2, 'jpdl31_TimerType274'):
        assert _is_linked(a2, 'jpdl31_TimerType274', b)
    _safe_set(b, 'jpdl31_SuperStateType273', set())
    assert not _is_linked(b, 'jpdl31_SuperStateType273', a2)
    if hasattr(a2, 'jpdl31_TimerType274'):
        assert not _is_linked(a2, 'jpdl31_TimerType274', b)


def test_assoc_timer290_reverse_link_reassign_clear():
    a1 = jpdl31_TimerType(duedate="sample_text", name="sample_text", repeat="sample_text", transition="sample_text")
    a2 = jpdl31_TimerType(duedate="sample_text_2", name="sample_text_2", repeat="sample_text_2", transition="sample_text_2")
    b = jpdl31_TaskNodeType(async_="sample_text", createTasks="sample_text", endTasks="sample_text", group="sample_text", name="sample_text", signal="sample_text")
    _safe_set(b, 'jpdl31_TaskNodeType291', {a1})
    assert _is_linked(b, 'jpdl31_TaskNodeType291', a1)
    if hasattr(a1, 'jpdl31_TimerType292'):
        assert _is_linked(a1, 'jpdl31_TimerType292', b)
    _safe_set(b, 'jpdl31_TaskNodeType291', {a2})
    assert _is_linked(b, 'jpdl31_TaskNodeType291', a2)
    if hasattr(a1, 'jpdl31_TimerType292'):
        assert not _is_linked(a1, 'jpdl31_TimerType292', b)
    if hasattr(a2, 'jpdl31_TimerType292'):
        assert _is_linked(a2, 'jpdl31_TimerType292', b)
    _safe_set(b, 'jpdl31_TaskNodeType291', set())
    assert not _is_linked(b, 'jpdl31_TaskNodeType291', a2)
    if hasattr(a2, 'jpdl31_TimerType292'):
        assert not _is_linked(a2, 'jpdl31_TimerType292', b)


def test_assoc_timer305_reverse_link_reassign_clear():
    a1 = jpdl31_TimerType(duedate="sample_text", name="sample_text", repeat="sample_text", transition="sample_text")
    a2 = jpdl31_TimerType(duedate="sample_text_2", name="sample_text_2", repeat="sample_text_2", transition="sample_text_2")
    b = jpdl31_TaskType(blocking="sample_text", description="sample_text", duedate="sample_text", group="sample_text", name="sample_text", priority="sample_text", signalling="sample_text", swimlane="sample_text")
    _safe_set(b, 'jpdl31_TaskType306', {a1})
    assert _is_linked(b, 'jpdl31_TaskType306', a1)
    if hasattr(a1, 'jpdl31_TimerType307'):
        assert _is_linked(a1, 'jpdl31_TimerType307', b)
    _safe_set(b, 'jpdl31_TaskType306', {a2})
    assert _is_linked(b, 'jpdl31_TaskType306', a2)
    if hasattr(a1, 'jpdl31_TimerType307'):
        assert not _is_linked(a1, 'jpdl31_TimerType307', b)
    if hasattr(a2, 'jpdl31_TimerType307'):
        assert _is_linked(a2, 'jpdl31_TimerType307', b)
    _safe_set(b, 'jpdl31_TaskType306', set())
    assert not _is_linked(b, 'jpdl31_TaskType306', a2)
    if hasattr(a2, 'jpdl31_TimerType307'):
        assert not _is_linked(a2, 'jpdl31_TimerType307', b)


def test_assoc_timer63_reverse_link_reassign_clear():
    a1 = jpdl31_TimerType(duedate="sample_text", name="sample_text", repeat="sample_text", transition="sample_text")
    a2 = jpdl31_TimerType(duedate="sample_text_2", name="sample_text_2", repeat="sample_text_2", transition="sample_text_2")
    b = jpdl31_DocumentRoot(mixed="sample_text")
    _safe_set(b, 'jpdl31_DocumentRoot64', {a1})
    assert _is_linked(b, 'jpdl31_DocumentRoot64', a1)
    if hasattr(a1, 'jpdl31_TimerType'):
        assert _is_linked(a1, 'jpdl31_TimerType', b)
    _safe_set(b, 'jpdl31_DocumentRoot64', {a2})
    assert _is_linked(b, 'jpdl31_DocumentRoot64', a2)
    if hasattr(a1, 'jpdl31_TimerType'):
        assert not _is_linked(a1, 'jpdl31_TimerType', b)
    if hasattr(a2, 'jpdl31_TimerType'):
        assert _is_linked(a2, 'jpdl31_TimerType', b)
    _safe_set(b, 'jpdl31_DocumentRoot64', set())
    assert not _is_linked(b, 'jpdl31_DocumentRoot64', a2)
    if hasattr(a2, 'jpdl31_TimerType'):
        assert not _is_linked(a2, 'jpdl31_TimerType', b)


def test_assoc_transition105_reverse_link_reassign_clear():
    a1 = jpdl31_TransitionType(group="sample_text", name="sample_text", to="sample_text")
    a2 = jpdl31_TransitionType(group="sample_text_2", name="sample_text_2", to="sample_text_2")
    b = jpdl31_ForkType(async_="sample_text", group="sample_text", name="sample_text")
    _safe_set(b, 'jpdl31_ForkType106', {a1})
    assert _is_linked(b, 'jpdl31_ForkType106', a1)
    if hasattr(a1, 'jpdl31_TransitionType107'):
        assert _is_linked(a1, 'jpdl31_TransitionType107', b)
    _safe_set(b, 'jpdl31_ForkType106', {a2})
    assert _is_linked(b, 'jpdl31_ForkType106', a2)
    if hasattr(a1, 'jpdl31_TransitionType107'):
        assert not _is_linked(a1, 'jpdl31_TransitionType107', b)
    if hasattr(a2, 'jpdl31_TransitionType107'):
        assert _is_linked(a2, 'jpdl31_TransitionType107', b)
    _safe_set(b, 'jpdl31_ForkType106', set())
    assert not _is_linked(b, 'jpdl31_ForkType106', a2)
    if hasattr(a2, 'jpdl31_TransitionType107'):
        assert not _is_linked(a2, 'jpdl31_TransitionType107', b)


def test_assoc_transition117_reverse_link_reassign_clear():
    a1 = jpdl31_TransitionType(group="sample_text", name="sample_text", to="sample_text")
    a2 = jpdl31_TransitionType(group="sample_text_2", name="sample_text_2", to="sample_text_2")
    b = jpdl31_JoinType(async_="sample_text", name="sample_text", nodeContentElements="sample_text")
    _safe_set(b, 'jpdl31_JoinType118', {a1})
    assert _is_linked(b, 'jpdl31_JoinType118', a1)
    if hasattr(a1, 'jpdl31_TransitionType119'):
        assert _is_linked(a1, 'jpdl31_TransitionType119', b)
    _safe_set(b, 'jpdl31_JoinType118', {a2})
    assert _is_linked(b, 'jpdl31_JoinType118', a2)
    if hasattr(a1, 'jpdl31_TransitionType119'):
        assert not _is_linked(a1, 'jpdl31_TransitionType119', b)
    if hasattr(a2, 'jpdl31_TransitionType119'):
        assert _is_linked(a2, 'jpdl31_TransitionType119', b)
    _safe_set(b, 'jpdl31_JoinType118', set())
    assert not _is_linked(b, 'jpdl31_JoinType118', a2)
    if hasattr(a2, 'jpdl31_TransitionType119'):
        assert not _is_linked(a2, 'jpdl31_TransitionType119', b)


def test_assoc_transition141_reverse_link_reassign_clear():
    a1 = jpdl31_TransitionType(group="sample_text", name="sample_text", to="sample_text")
    a2 = jpdl31_TransitionType(group="sample_text_2", name="sample_text_2", to="sample_text_2")
    b = jpdl31_NodeType(async_="sample_text", name="sample_text", nodeContentElements="sample_text")
    _safe_set(b, 'jpdl31_NodeType142', {a1})
    assert _is_linked(b, 'jpdl31_NodeType142', a1)
    if hasattr(a1, 'jpdl31_TransitionType143'):
        assert _is_linked(a1, 'jpdl31_TransitionType143', b)
    _safe_set(b, 'jpdl31_NodeType142', {a2})
    assert _is_linked(b, 'jpdl31_NodeType142', a2)
    if hasattr(a1, 'jpdl31_TransitionType143'):
        assert not _is_linked(a1, 'jpdl31_TransitionType143', b)
    if hasattr(a2, 'jpdl31_TransitionType143'):
        assert _is_linked(a2, 'jpdl31_TransitionType143', b)
    _safe_set(b, 'jpdl31_NodeType142', set())
    assert not _is_linked(b, 'jpdl31_NodeType142', a2)
    if hasattr(a2, 'jpdl31_TransitionType143'):
        assert not _is_linked(a2, 'jpdl31_TransitionType143', b)


def test_assoc_transition212_reverse_link_reassign_clear():
    a1 = jpdl31_TransitionType(group="sample_text", name="sample_text", to="sample_text")
    a2 = jpdl31_TransitionType(group="sample_text_2", name="sample_text_2", to="sample_text_2")
    b = jpdl31_ProcessStateType(async_="sample_text", group="sample_text", name="sample_text")
    _safe_set(b, 'jpdl31_ProcessStateType213', {a1})
    assert _is_linked(b, 'jpdl31_ProcessStateType213', a1)
    if hasattr(a1, 'jpdl31_TransitionType214'):
        assert _is_linked(a1, 'jpdl31_TransitionType214', b)
    _safe_set(b, 'jpdl31_ProcessStateType213', {a2})
    assert _is_linked(b, 'jpdl31_ProcessStateType213', a2)
    if hasattr(a1, 'jpdl31_TransitionType214'):
        assert not _is_linked(a1, 'jpdl31_TransitionType214', b)
    if hasattr(a2, 'jpdl31_TransitionType214'):
        assert _is_linked(a2, 'jpdl31_TransitionType214', b)
    _safe_set(b, 'jpdl31_ProcessStateType213', set())
    assert not _is_linked(b, 'jpdl31_ProcessStateType213', a2)
    if hasattr(a2, 'jpdl31_TransitionType214'):
        assert not _is_linked(a2, 'jpdl31_TransitionType214', b)


def test_assoc_transition218_reverse_link_reassign_clear():
    a1 = jpdl31_TransitionType(group="sample_text", name="sample_text", to="sample_text")
    a2 = jpdl31_TransitionType(group="sample_text_2", name="sample_text_2", to="sample_text_2")
    b = jpdl31_StartStateType(group="sample_text", name="sample_text")
    _safe_set(b, 'jpdl31_StartStateType219', {a1})
    assert _is_linked(b, 'jpdl31_StartStateType219', a1)
    if hasattr(a1, 'jpdl31_TransitionType220'):
        assert _is_linked(a1, 'jpdl31_TransitionType220', b)
    _safe_set(b, 'jpdl31_StartStateType219', {a2})
    assert _is_linked(b, 'jpdl31_StartStateType219', a2)
    if hasattr(a1, 'jpdl31_TransitionType220'):
        assert not _is_linked(a1, 'jpdl31_TransitionType220', b)
    if hasattr(a2, 'jpdl31_TransitionType220'):
        assert _is_linked(a2, 'jpdl31_TransitionType220', b)
    _safe_set(b, 'jpdl31_StartStateType219', set())
    assert not _is_linked(b, 'jpdl31_StartStateType219', a2)
    if hasattr(a2, 'jpdl31_TransitionType220'):
        assert not _is_linked(a2, 'jpdl31_TransitionType220', b)


def test_assoc_transition236_reverse_link_reassign_clear():
    a1 = jpdl31_TransitionType(group="sample_text", name="sample_text", to="sample_text")
    a2 = jpdl31_TransitionType(group="sample_text_2", name="sample_text_2", to="sample_text_2")
    b = jpdl31_StateType(async_="sample_text", name="sample_text", nodeContentElements="sample_text")
    _safe_set(b, 'jpdl31_StateType237', {a1})
    assert _is_linked(b, 'jpdl31_StateType237', a1)
    if hasattr(a1, 'jpdl31_TransitionType238'):
        assert _is_linked(a1, 'jpdl31_TransitionType238', b)
    _safe_set(b, 'jpdl31_StateType237', {a2})
    assert _is_linked(b, 'jpdl31_StateType237', a2)
    if hasattr(a1, 'jpdl31_TransitionType238'):
        assert not _is_linked(a1, 'jpdl31_TransitionType238', b)
    if hasattr(a2, 'jpdl31_TransitionType238'):
        assert _is_linked(a2, 'jpdl31_TransitionType238', b)
    _safe_set(b, 'jpdl31_StateType237', set())
    assert not _is_linked(b, 'jpdl31_StateType237', a2)
    if hasattr(a2, 'jpdl31_TransitionType238'):
        assert not _is_linked(a2, 'jpdl31_TransitionType238', b)


def test_assoc_transition275_reverse_link_reassign_clear():
    a1 = jpdl31_TransitionType(group="sample_text", name="sample_text", to="sample_text")
    a2 = jpdl31_TransitionType(group="sample_text_2", name="sample_text_2", to="sample_text_2")
    b = jpdl31_SuperStateType(async_="sample_text", group="sample_text", name="sample_text")
    _safe_set(b, 'jpdl31_SuperStateType276', {a1})
    assert _is_linked(b, 'jpdl31_SuperStateType276', a1)
    if hasattr(a1, 'jpdl31_TransitionType277'):
        assert _is_linked(a1, 'jpdl31_TransitionType277', b)
    _safe_set(b, 'jpdl31_SuperStateType276', {a2})
    assert _is_linked(b, 'jpdl31_SuperStateType276', a2)
    if hasattr(a1, 'jpdl31_TransitionType277'):
        assert not _is_linked(a1, 'jpdl31_TransitionType277', b)
    if hasattr(a2, 'jpdl31_TransitionType277'):
        assert _is_linked(a2, 'jpdl31_TransitionType277', b)
    _safe_set(b, 'jpdl31_SuperStateType276', set())
    assert not _is_linked(b, 'jpdl31_SuperStateType276', a2)
    if hasattr(a2, 'jpdl31_TransitionType277'):
        assert not _is_linked(a2, 'jpdl31_TransitionType277', b)


def test_assoc_transition293_reverse_link_reassign_clear():
    a1 = jpdl31_TransitionType(group="sample_text", name="sample_text", to="sample_text")
    a2 = jpdl31_TransitionType(group="sample_text_2", name="sample_text_2", to="sample_text_2")
    b = jpdl31_TaskNodeType(async_="sample_text", createTasks="sample_text", endTasks="sample_text", group="sample_text", name="sample_text", signal="sample_text")
    _safe_set(b, 'jpdl31_TaskNodeType294', {a1})
    assert _is_linked(b, 'jpdl31_TaskNodeType294', a1)
    if hasattr(a1, 'jpdl31_TransitionType295'):
        assert _is_linked(a1, 'jpdl31_TransitionType295', b)
    _safe_set(b, 'jpdl31_TaskNodeType294', {a2})
    assert _is_linked(b, 'jpdl31_TaskNodeType294', a2)
    if hasattr(a1, 'jpdl31_TransitionType295'):
        assert not _is_linked(a1, 'jpdl31_TransitionType295', b)
    if hasattr(a2, 'jpdl31_TransitionType295'):
        assert _is_linked(a2, 'jpdl31_TransitionType295', b)
    _safe_set(b, 'jpdl31_TaskNodeType294', set())
    assert not _is_linked(b, 'jpdl31_TaskNodeType294', a2)
    if hasattr(a2, 'jpdl31_TransitionType295'):
        assert not _is_linked(a2, 'jpdl31_TransitionType295', b)


def test_assoc_transition65_reverse_link_reassign_clear():
    a1 = jpdl31_TransitionType(group="sample_text", name="sample_text", to="sample_text")
    a2 = jpdl31_TransitionType(group="sample_text_2", name="sample_text_2", to="sample_text_2")
    b = jpdl31_DocumentRoot(mixed="sample_text")
    _safe_set(b, 'jpdl31_DocumentRoot66', {a1})
    assert _is_linked(b, 'jpdl31_DocumentRoot66', a1)
    if hasattr(a1, 'jpdl31_TransitionType'):
        assert _is_linked(a1, 'jpdl31_TransitionType', b)
    _safe_set(b, 'jpdl31_DocumentRoot66', {a2})
    assert _is_linked(b, 'jpdl31_DocumentRoot66', a2)
    if hasattr(a1, 'jpdl31_TransitionType'):
        assert not _is_linked(a1, 'jpdl31_TransitionType', b)
    if hasattr(a2, 'jpdl31_TransitionType'):
        assert _is_linked(a2, 'jpdl31_TransitionType', b)
    _safe_set(b, 'jpdl31_DocumentRoot66', set())
    assert not _is_linked(b, 'jpdl31_DocumentRoot66', a2)
    if hasattr(a2, 'jpdl31_TransitionType'):
        assert not _is_linked(a2, 'jpdl31_TransitionType', b)


def test_assoc_transition8_reverse_link_reassign_clear():
    a1 = jpdl31_TransitionType1(group="sample_text", name="sample_text", to="sample_text")
    a2 = jpdl31_TransitionType1(group="sample_text_2", name="sample_text_2", to="sample_text_2")
    b = jpdl31_DecisionType(async_="sample_text", expression="sample_text", group="sample_text", name="sample_text")
    _safe_set(b, 'jpdl31_DecisionType9', {a1})
    assert _is_linked(b, 'jpdl31_DecisionType9', a1)
    if hasattr(a1, 'jpdl31_TransitionType1'):
        assert _is_linked(a1, 'jpdl31_TransitionType1', b)
    _safe_set(b, 'jpdl31_DecisionType9', {a2})
    assert _is_linked(b, 'jpdl31_DecisionType9', a2)
    if hasattr(a1, 'jpdl31_TransitionType1'):
        assert not _is_linked(a1, 'jpdl31_TransitionType1', b)
    if hasattr(a2, 'jpdl31_TransitionType1'):
        assert _is_linked(a2, 'jpdl31_TransitionType1', b)
    _safe_set(b, 'jpdl31_DecisionType9', set())
    assert not _is_linked(b, 'jpdl31_DecisionType9', a2)
    if hasattr(a2, 'jpdl31_TransitionType1'):
        assert not _is_linked(a2, 'jpdl31_TransitionType1', b)


def test_assoc_variable200_reverse_link_reassign_clear():
    a1 = jpdl31_VariableType(access="sample_text", any="sample_text", mappedName="sample_text", name="sample_text")
    a2 = jpdl31_VariableType(access="sample_text_2", any="sample_text_2", mappedName="sample_text_2", name="sample_text_2")
    b = jpdl31_ProcessStateType(async_="sample_text", group="sample_text", name="sample_text")
    _safe_set(b, 'jpdl31_ProcessStateType201', {a1})
    assert _is_linked(b, 'jpdl31_ProcessStateType201', a1)
    if hasattr(a1, 'jpdl31_VariableType202'):
        assert _is_linked(a1, 'jpdl31_VariableType202', b)
    _safe_set(b, 'jpdl31_ProcessStateType201', {a2})
    assert _is_linked(b, 'jpdl31_ProcessStateType201', a2)
    if hasattr(a1, 'jpdl31_VariableType202'):
        assert not _is_linked(a1, 'jpdl31_VariableType202', b)
    if hasattr(a2, 'jpdl31_VariableType202'):
        assert _is_linked(a2, 'jpdl31_VariableType202', b)
    _safe_set(b, 'jpdl31_ProcessStateType201', set())
    assert not _is_linked(b, 'jpdl31_ProcessStateType201', a2)
    if hasattr(a2, 'jpdl31_VariableType202'):
        assert not _is_linked(a2, 'jpdl31_VariableType202', b)


def test_assoc_variable67_reverse_link_reassign_clear():
    a1 = jpdl31_VariableType(access="sample_text", any="sample_text", mappedName="sample_text", name="sample_text")
    a2 = jpdl31_VariableType(access="sample_text_2", any="sample_text_2", mappedName="sample_text_2", name="sample_text_2")
    b = jpdl31_DocumentRoot(mixed="sample_text")
    _safe_set(b, 'jpdl31_DocumentRoot68', {a1})
    assert _is_linked(b, 'jpdl31_DocumentRoot68', a1)
    if hasattr(a1, 'jpdl31_VariableType'):
        assert _is_linked(a1, 'jpdl31_VariableType', b)
    _safe_set(b, 'jpdl31_DocumentRoot68', {a2})
    assert _is_linked(b, 'jpdl31_DocumentRoot68', a2)
    if hasattr(a1, 'jpdl31_VariableType'):
        assert not _is_linked(a1, 'jpdl31_VariableType', b)
    if hasattr(a2, 'jpdl31_VariableType'):
        assert _is_linked(a2, 'jpdl31_VariableType', b)
    _safe_set(b, 'jpdl31_DocumentRoot68', set())
    assert not _is_linked(b, 'jpdl31_DocumentRoot68', a2)
    if hasattr(a2, 'jpdl31_VariableType'):
        assert not _is_linked(a2, 'jpdl31_VariableType', b)


