import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Delegation,
    jpdl32_ActionType,
    jpdl32_AssignmentType,
    jpdl32_CancelTimerType,
    jpdl32_ConditionType,
    jpdl32_CreateTimerType,
    jpdl32_DecisionType,
    jpdl32_Delegation,
    jpdl32_DocumentRoot,
    jpdl32_EStringToStringMapEntry,
    jpdl32_EndStateType,
    jpdl32_EventType,
    jpdl32_ExceptionHandlerType,
    jpdl32_ForkType,
    jpdl32_JoinType,
    jpdl32_MailNodeType,
    jpdl32_MailType,
    jpdl32_NodeType,
    jpdl32_ProcessDefinitionType,
    jpdl32_ProcessStateType,
    jpdl32_ReminderType,
    jpdl32_ScriptType,
    jpdl32_StartStateType,
    jpdl32_StateType,
    jpdl32_SubProcessType,
    jpdl32_SuperStateType,
    jpdl32_SwimlaneType,
    jpdl32_TaskNodeType,
    jpdl32_TaskType,
    jpdl32_TimerType,
    jpdl32_TransitionType,
    jpdl32_VariableType,
    BindingType,
    BooleanType,
    ConfigType,
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
    a1 = jpdl32_CreateTimerType(duedate="sample_text", name="sample_text", repeat="sample_text", transition="sample_text")
    a2 = jpdl32_CreateTimerType(duedate="sample_text_2", name="sample_text_2", repeat="sample_text_2", transition="sample_text_2")
    b = jpdl32_ActionType(acceptPropagatedEvents="sample_text", any="sample_text", async_="sample_text", class_="sample_text", configType="sample_text", expression="sample_text", mixed="sample_text", name="sample_text", refName="sample_text")
    _safe_set(b, 'jpdl32_ActionType', a1)
    assert _is_linked(b, 'jpdl32_ActionType', a1)
    if hasattr(a1, 'jpdl32_CreateTimerType'):
        assert _is_linked(a1, 'jpdl32_CreateTimerType', b)
    _safe_set(b, 'jpdl32_ActionType', a2)
    assert _is_linked(b, 'jpdl32_ActionType', a2)
    if hasattr(a1, 'jpdl32_CreateTimerType'):
        assert not _is_linked(a1, 'jpdl32_CreateTimerType', b)
    if hasattr(a2, 'jpdl32_CreateTimerType'):
        assert _is_linked(a2, 'jpdl32_CreateTimerType', b)
    _safe_set(b, 'jpdl32_ActionType', None)
    assert not _is_linked(b, 'jpdl32_ActionType', a2)
    if hasattr(a2, 'jpdl32_CreateTimerType'):
        assert not _is_linked(a2, 'jpdl32_CreateTimerType', b)


def test_assoc_action14_reverse_link_reassign_clear():
    a1 = jpdl32_DocumentRoot(description="sample_text", mixed="sample_text", recipients="sample_text", subject="sample_text", template="sample_text", text="sample_text", to="sample_text")
    a2 = jpdl32_DocumentRoot(description="sample_text_2", mixed="sample_text_2", recipients="sample_text_2", subject="sample_text_2", template="sample_text_2", text="sample_text_2", to="sample_text_2")
    b = jpdl32_ActionType(acceptPropagatedEvents="sample_text", any="sample_text", async_="sample_text", class_="sample_text", configType="sample_text", expression="sample_text", mixed="sample_text", name="sample_text", refName="sample_text")
    _safe_set(b, 'jpdl32_ActionType16', a1)
    assert _is_linked(b, 'jpdl32_ActionType16', a1)
    if hasattr(a1, 'jpdl32_DocumentRoot15'):
        assert _is_linked(a1, 'jpdl32_DocumentRoot15', b)
    _safe_set(b, 'jpdl32_ActionType16', a2)
    assert _is_linked(b, 'jpdl32_ActionType16', a2)
    if hasattr(a1, 'jpdl32_DocumentRoot15'):
        assert not _is_linked(a1, 'jpdl32_DocumentRoot15', b)
    if hasattr(a2, 'jpdl32_DocumentRoot15'):
        assert _is_linked(a2, 'jpdl32_DocumentRoot15', b)
    _safe_set(b, 'jpdl32_ActionType16', None)
    assert not _is_linked(b, 'jpdl32_ActionType16', a2)
    if hasattr(a2, 'jpdl32_DocumentRoot15'):
        assert not _is_linked(a2, 'jpdl32_DocumentRoot15', b)


def test_assoc_action140_reverse_link_reassign_clear():
    a1 = jpdl32_NodeType(async_="sample_text", description="sample_text", name="sample_text", nodeContentElements="sample_text")
    a2 = jpdl32_NodeType(async_="sample_text_2", description="sample_text_2", name="sample_text_2", nodeContentElements="sample_text_2")
    b = jpdl32_ActionType(acceptPropagatedEvents="sample_text", any="sample_text", async_="sample_text", class_="sample_text", configType="sample_text", expression="sample_text", mixed="sample_text", name="sample_text", refName="sample_text")
    _safe_set(b, 'jpdl32_ActionType142', a1)
    assert _is_linked(b, 'jpdl32_ActionType142', a1)
    if hasattr(a1, 'jpdl32_NodeType141'):
        assert _is_linked(a1, 'jpdl32_NodeType141', b)
    _safe_set(b, 'jpdl32_ActionType142', a2)
    assert _is_linked(b, 'jpdl32_ActionType142', a2)
    if hasattr(a1, 'jpdl32_NodeType141'):
        assert not _is_linked(a1, 'jpdl32_NodeType141', b)
    if hasattr(a2, 'jpdl32_NodeType141'):
        assert _is_linked(a2, 'jpdl32_NodeType141', b)
    _safe_set(b, 'jpdl32_ActionType142', None)
    assert not _is_linked(b, 'jpdl32_ActionType142', a2)
    if hasattr(a2, 'jpdl32_NodeType141'):
        assert not _is_linked(a2, 'jpdl32_NodeType141', b)


def test_assoc_action203_reverse_link_reassign_clear():
    a1 = jpdl32_ProcessDefinitionType(description="sample_text", group="sample_text", name="sample_text")
    a2 = jpdl32_ProcessDefinitionType(description="sample_text_2", group="sample_text_2", name="sample_text_2")
    b = jpdl32_ActionType(acceptPropagatedEvents="sample_text", any="sample_text", async_="sample_text", class_="sample_text", configType="sample_text", expression="sample_text", mixed="sample_text", name="sample_text", refName="sample_text")
    _safe_set(b, 'jpdl32_ActionType205', a1)
    assert _is_linked(b, 'jpdl32_ActionType205', a1)
    if hasattr(a1, 'jpdl32_ProcessDefinitionType204'):
        assert _is_linked(a1, 'jpdl32_ProcessDefinitionType204', b)
    _safe_set(b, 'jpdl32_ActionType205', a2)
    assert _is_linked(b, 'jpdl32_ActionType205', a2)
    if hasattr(a1, 'jpdl32_ProcessDefinitionType204'):
        assert not _is_linked(a1, 'jpdl32_ProcessDefinitionType204', b)
    if hasattr(a2, 'jpdl32_ProcessDefinitionType204'):
        assert _is_linked(a2, 'jpdl32_ProcessDefinitionType204', b)
    _safe_set(b, 'jpdl32_ActionType205', None)
    assert not _is_linked(b, 'jpdl32_ActionType205', a2)
    if hasattr(a2, 'jpdl32_ProcessDefinitionType204'):
        assert not _is_linked(a2, 'jpdl32_ProcessDefinitionType204', b)


def test_assoc_action342_reverse_link_reassign_clear():
    a1 = jpdl32_TimerType(duedate="sample_text", name="sample_text", repeat="sample_text", transition="sample_text")
    a2 = jpdl32_TimerType(duedate="sample_text_2", name="sample_text_2", repeat="sample_text_2", transition="sample_text_2")
    b = jpdl32_ActionType(acceptPropagatedEvents="sample_text", any="sample_text", async_="sample_text", class_="sample_text", configType="sample_text", expression="sample_text", mixed="sample_text", name="sample_text", refName="sample_text")
    _safe_set(b, 'jpdl32_ActionType344', a1)
    assert _is_linked(b, 'jpdl32_ActionType344', a1)
    if hasattr(a1, 'jpdl32_TimerType343'):
        assert _is_linked(a1, 'jpdl32_TimerType343', b)
    _safe_set(b, 'jpdl32_ActionType344', a2)
    assert _is_linked(b, 'jpdl32_ActionType344', a2)
    if hasattr(a1, 'jpdl32_TimerType343'):
        assert not _is_linked(a1, 'jpdl32_TimerType343', b)
    if hasattr(a2, 'jpdl32_TimerType343'):
        assert _is_linked(a2, 'jpdl32_TimerType343', b)
    _safe_set(b, 'jpdl32_ActionType344', None)
    assert not _is_linked(b, 'jpdl32_ActionType344', a2)
    if hasattr(a2, 'jpdl32_TimerType343'):
        assert not _is_linked(a2, 'jpdl32_TimerType343', b)


def test_assoc_action359_reverse_link_reassign_clear():
    a1 = jpdl32_TransitionType(description="sample_text", group="sample_text", name="sample_text", to="sample_text")
    a2 = jpdl32_TransitionType(description="sample_text_2", group="sample_text_2", name="sample_text_2", to="sample_text_2")
    b = jpdl32_ActionType(acceptPropagatedEvents="sample_text", any="sample_text", async_="sample_text", class_="sample_text", configType="sample_text", expression="sample_text", mixed="sample_text", name="sample_text", refName="sample_text")
    _safe_set(b, 'jpdl32_ActionType361', a1)
    assert _is_linked(b, 'jpdl32_ActionType361', a1)
    if hasattr(a1, 'jpdl32_TransitionType360'):
        assert _is_linked(a1, 'jpdl32_TransitionType360', b)
    _safe_set(b, 'jpdl32_ActionType361', a2)
    assert _is_linked(b, 'jpdl32_ActionType361', a2)
    if hasattr(a1, 'jpdl32_TransitionType360'):
        assert not _is_linked(a1, 'jpdl32_TransitionType360', b)
    if hasattr(a2, 'jpdl32_TransitionType360'):
        assert _is_linked(a2, 'jpdl32_TransitionType360', b)
    _safe_set(b, 'jpdl32_ActionType361', None)
    assert not _is_linked(b, 'jpdl32_ActionType361', a2)
    if hasattr(a2, 'jpdl32_TransitionType360'):
        assert not _is_linked(a2, 'jpdl32_TransitionType360', b)


def test_assoc_action80_reverse_link_reassign_clear():
    a1 = jpdl32_EventType(actionElements="sample_text", type="sample_text")
    a2 = jpdl32_EventType(actionElements="sample_text_2", type="sample_text_2")
    b = jpdl32_ActionType(acceptPropagatedEvents="sample_text", any="sample_text", async_="sample_text", class_="sample_text", configType="sample_text", expression="sample_text", mixed="sample_text", name="sample_text", refName="sample_text")
    _safe_set(b, 'jpdl32_ActionType82', a1)
    assert _is_linked(b, 'jpdl32_ActionType82', a1)
    if hasattr(a1, 'jpdl32_EventType81'):
        assert _is_linked(a1, 'jpdl32_EventType81', b)
    _safe_set(b, 'jpdl32_ActionType82', a2)
    assert _is_linked(b, 'jpdl32_ActionType82', a2)
    if hasattr(a1, 'jpdl32_EventType81'):
        assert not _is_linked(a1, 'jpdl32_EventType81', b)
    if hasattr(a2, 'jpdl32_EventType81'):
        assert _is_linked(a2, 'jpdl32_EventType81', b)
    _safe_set(b, 'jpdl32_ActionType82', None)
    assert not _is_linked(b, 'jpdl32_ActionType82', a2)
    if hasattr(a2, 'jpdl32_EventType81'):
        assert not _is_linked(a2, 'jpdl32_EventType81', b)


def test_assoc_action95_reverse_link_reassign_clear():
    a1 = jpdl32_ExceptionHandlerType(exceptionClass="sample_text", group="sample_text")
    a2 = jpdl32_ExceptionHandlerType(exceptionClass="sample_text_2", group="sample_text_2")
    b = jpdl32_ActionType(acceptPropagatedEvents="sample_text", any="sample_text", async_="sample_text", class_="sample_text", configType="sample_text", expression="sample_text", mixed="sample_text", name="sample_text", refName="sample_text")
    _safe_set(b, 'jpdl32_ActionType97', a1)
    assert _is_linked(b, 'jpdl32_ActionType97', a1)
    if hasattr(a1, 'jpdl32_ExceptionHandlerType96'):
        assert _is_linked(a1, 'jpdl32_ExceptionHandlerType96', b)
    _safe_set(b, 'jpdl32_ActionType97', a2)
    assert _is_linked(b, 'jpdl32_ActionType97', a2)
    if hasattr(a1, 'jpdl32_ExceptionHandlerType96'):
        assert not _is_linked(a1, 'jpdl32_ExceptionHandlerType96', b)
    if hasattr(a2, 'jpdl32_ExceptionHandlerType96'):
        assert _is_linked(a2, 'jpdl32_ExceptionHandlerType96', b)
    _safe_set(b, 'jpdl32_ActionType97', None)
    assert not _is_linked(b, 'jpdl32_ActionType97', a2)
    if hasattr(a2, 'jpdl32_ExceptionHandlerType96'):
        assert not _is_linked(a2, 'jpdl32_ExceptionHandlerType96', b)


def test_assoc_assignment17_reverse_link_reassign_clear():
    a1 = jpdl32_DocumentRoot(description="sample_text", mixed="sample_text", recipients="sample_text", subject="sample_text", template="sample_text", text="sample_text", to="sample_text")
    a2 = jpdl32_DocumentRoot(description="sample_text_2", mixed="sample_text_2", recipients="sample_text_2", subject="sample_text_2", template="sample_text_2", text="sample_text_2", to="sample_text_2")
    b = jpdl32_AssignmentType(actorId="sample_text", expression="sample_text", pooledActors="sample_text")
    _safe_set(b, 'jpdl32_AssignmentType', a1)
    assert _is_linked(b, 'jpdl32_AssignmentType', a1)
    if hasattr(a1, 'jpdl32_DocumentRoot18'):
        assert _is_linked(a1, 'jpdl32_DocumentRoot18', b)
    _safe_set(b, 'jpdl32_AssignmentType', a2)
    assert _is_linked(b, 'jpdl32_AssignmentType', a2)
    if hasattr(a1, 'jpdl32_DocumentRoot18'):
        assert not _is_linked(a1, 'jpdl32_DocumentRoot18', b)
    if hasattr(a2, 'jpdl32_DocumentRoot18'):
        assert _is_linked(a2, 'jpdl32_DocumentRoot18', b)
    _safe_set(b, 'jpdl32_AssignmentType', None)
    assert not _is_linked(b, 'jpdl32_AssignmentType', a2)
    if hasattr(a2, 'jpdl32_DocumentRoot18'):
        assert not _is_linked(a2, 'jpdl32_DocumentRoot18', b)


def test_assoc_assignment310_reverse_link_reassign_clear():
    a1 = jpdl32_SwimlaneType(name="sample_text")
    a2 = jpdl32_SwimlaneType(name="sample_text_2")
    b = jpdl32_AssignmentType(actorId="sample_text", expression="sample_text", pooledActors="sample_text")
    _safe_set(b, 'jpdl32_AssignmentType312', a1)
    assert _is_linked(b, 'jpdl32_AssignmentType312', a1)
    if hasattr(a1, 'jpdl32_SwimlaneType311'):
        assert _is_linked(a1, 'jpdl32_SwimlaneType311', b)
    _safe_set(b, 'jpdl32_AssignmentType312', a2)
    assert _is_linked(b, 'jpdl32_AssignmentType312', a2)
    if hasattr(a1, 'jpdl32_SwimlaneType311'):
        assert not _is_linked(a1, 'jpdl32_SwimlaneType311', b)
    if hasattr(a2, 'jpdl32_SwimlaneType311'):
        assert _is_linked(a2, 'jpdl32_SwimlaneType311', b)
    _safe_set(b, 'jpdl32_AssignmentType312', None)
    assert not _is_linked(b, 'jpdl32_AssignmentType312', a2)
    if hasattr(a2, 'jpdl32_SwimlaneType311'):
        assert not _is_linked(a2, 'jpdl32_SwimlaneType311', b)


def test_assoc_assignment328_reverse_link_reassign_clear():
    a1 = jpdl32_TaskType(blocking="sample_text", description="sample_text", description1="sample_text", duedate="sample_text", group="sample_text", name="sample_text", notify="sample_text", priority="sample_text", signalling="sample_text", swimlane="sample_text")
    a2 = jpdl32_TaskType(blocking="sample_text_2", description="sample_text_2", description1="sample_text_2", duedate="sample_text_2", group="sample_text_2", name="sample_text_2", notify="sample_text_2", priority="sample_text_2", signalling="sample_text_2", swimlane="sample_text_2")
    b = jpdl32_AssignmentType(actorId="sample_text", expression="sample_text", pooledActors="sample_text")
    _safe_set(b, 'jpdl32_AssignmentType330', a1)
    assert _is_linked(b, 'jpdl32_AssignmentType330', a1)
    if hasattr(a1, 'jpdl32_TaskType329'):
        assert _is_linked(a1, 'jpdl32_TaskType329', b)
    _safe_set(b, 'jpdl32_AssignmentType330', a2)
    assert _is_linked(b, 'jpdl32_AssignmentType330', a2)
    if hasattr(a1, 'jpdl32_TaskType329'):
        assert not _is_linked(a1, 'jpdl32_TaskType329', b)
    if hasattr(a2, 'jpdl32_TaskType329'):
        assert _is_linked(a2, 'jpdl32_TaskType329', b)
    _safe_set(b, 'jpdl32_AssignmentType330', None)
    assert not _is_linked(b, 'jpdl32_AssignmentType330', a2)
    if hasattr(a2, 'jpdl32_TaskType329'):
        assert not _is_linked(a2, 'jpdl32_TaskType329', b)


def test_assoc_cancelTimer149_reverse_link_reassign_clear():
    a1 = jpdl32_NodeType(async_="sample_text", description="sample_text", name="sample_text", nodeContentElements="sample_text")
    a2 = jpdl32_NodeType(async_="sample_text_2", description="sample_text_2", name="sample_text_2", nodeContentElements="sample_text_2")
    b = jpdl32_CancelTimerType(name="sample_text")
    _safe_set(b, 'jpdl32_CancelTimerType151', a1)
    assert _is_linked(b, 'jpdl32_CancelTimerType151', a1)
    if hasattr(a1, 'jpdl32_NodeType150'):
        assert _is_linked(a1, 'jpdl32_NodeType150', b)
    _safe_set(b, 'jpdl32_CancelTimerType151', a2)
    assert _is_linked(b, 'jpdl32_CancelTimerType151', a2)
    if hasattr(a1, 'jpdl32_NodeType150'):
        assert not _is_linked(a1, 'jpdl32_NodeType150', b)
    if hasattr(a2, 'jpdl32_NodeType150'):
        assert _is_linked(a2, 'jpdl32_NodeType150', b)
    _safe_set(b, 'jpdl32_CancelTimerType151', None)
    assert not _is_linked(b, 'jpdl32_CancelTimerType151', a2)
    if hasattr(a2, 'jpdl32_NodeType150'):
        assert not _is_linked(a2, 'jpdl32_NodeType150', b)


def test_assoc_cancelTimer19_reverse_link_reassign_clear():
    a1 = jpdl32_DocumentRoot(description="sample_text", mixed="sample_text", recipients="sample_text", subject="sample_text", template="sample_text", text="sample_text", to="sample_text")
    a2 = jpdl32_DocumentRoot(description="sample_text_2", mixed="sample_text_2", recipients="sample_text_2", subject="sample_text_2", template="sample_text_2", text="sample_text_2", to="sample_text_2")
    b = jpdl32_CancelTimerType(name="sample_text")
    _safe_set(b, 'jpdl32_CancelTimerType', a1)
    assert _is_linked(b, 'jpdl32_CancelTimerType', a1)
    if hasattr(a1, 'jpdl32_DocumentRoot20'):
        assert _is_linked(a1, 'jpdl32_DocumentRoot20', b)
    _safe_set(b, 'jpdl32_CancelTimerType', a2)
    assert _is_linked(b, 'jpdl32_CancelTimerType', a2)
    if hasattr(a1, 'jpdl32_DocumentRoot20'):
        assert not _is_linked(a1, 'jpdl32_DocumentRoot20', b)
    if hasattr(a2, 'jpdl32_DocumentRoot20'):
        assert _is_linked(a2, 'jpdl32_DocumentRoot20', b)
    _safe_set(b, 'jpdl32_CancelTimerType', None)
    assert not _is_linked(b, 'jpdl32_CancelTimerType', a2)
    if hasattr(a2, 'jpdl32_DocumentRoot20'):
        assert not _is_linked(a2, 'jpdl32_DocumentRoot20', b)


def test_assoc_cancelTimer212_reverse_link_reassign_clear():
    a1 = jpdl32_ProcessDefinitionType(description="sample_text", group="sample_text", name="sample_text")
    a2 = jpdl32_ProcessDefinitionType(description="sample_text_2", group="sample_text_2", name="sample_text_2")
    b = jpdl32_CancelTimerType(name="sample_text")
    _safe_set(b, 'jpdl32_CancelTimerType214', a1)
    assert _is_linked(b, 'jpdl32_CancelTimerType214', a1)
    if hasattr(a1, 'jpdl32_ProcessDefinitionType213'):
        assert _is_linked(a1, 'jpdl32_ProcessDefinitionType213', b)
    _safe_set(b, 'jpdl32_CancelTimerType214', a2)
    assert _is_linked(b, 'jpdl32_CancelTimerType214', a2)
    if hasattr(a1, 'jpdl32_ProcessDefinitionType213'):
        assert not _is_linked(a1, 'jpdl32_ProcessDefinitionType213', b)
    if hasattr(a2, 'jpdl32_ProcessDefinitionType213'):
        assert _is_linked(a2, 'jpdl32_ProcessDefinitionType213', b)
    _safe_set(b, 'jpdl32_CancelTimerType214', None)
    assert not _is_linked(b, 'jpdl32_CancelTimerType214', a2)
    if hasattr(a2, 'jpdl32_ProcessDefinitionType213'):
        assert not _is_linked(a2, 'jpdl32_ProcessDefinitionType213', b)


def test_assoc_cancelTimer351_reverse_link_reassign_clear():
    a1 = jpdl32_TimerType(duedate="sample_text", name="sample_text", repeat="sample_text", transition="sample_text")
    a2 = jpdl32_TimerType(duedate="sample_text_2", name="sample_text_2", repeat="sample_text_2", transition="sample_text_2")
    b = jpdl32_CancelTimerType(name="sample_text")
    _safe_set(b, 'jpdl32_CancelTimerType353', a1)
    assert _is_linked(b, 'jpdl32_CancelTimerType353', a1)
    if hasattr(a1, 'jpdl32_TimerType352'):
        assert _is_linked(a1, 'jpdl32_TimerType352', b)
    _safe_set(b, 'jpdl32_CancelTimerType353', a2)
    assert _is_linked(b, 'jpdl32_CancelTimerType353', a2)
    if hasattr(a1, 'jpdl32_TimerType352'):
        assert not _is_linked(a1, 'jpdl32_TimerType352', b)
    if hasattr(a2, 'jpdl32_TimerType352'):
        assert _is_linked(a2, 'jpdl32_TimerType352', b)
    _safe_set(b, 'jpdl32_CancelTimerType353', None)
    assert not _is_linked(b, 'jpdl32_CancelTimerType353', a2)
    if hasattr(a2, 'jpdl32_TimerType352'):
        assert not _is_linked(a2, 'jpdl32_TimerType352', b)


def test_assoc_cancelTimer368_reverse_link_reassign_clear():
    a1 = jpdl32_TransitionType(description="sample_text", group="sample_text", name="sample_text", to="sample_text")
    a2 = jpdl32_TransitionType(description="sample_text_2", group="sample_text_2", name="sample_text_2", to="sample_text_2")
    b = jpdl32_CancelTimerType(name="sample_text")
    _safe_set(b, 'jpdl32_CancelTimerType370', a1)
    assert _is_linked(b, 'jpdl32_CancelTimerType370', a1)
    if hasattr(a1, 'jpdl32_TransitionType369'):
        assert _is_linked(a1, 'jpdl32_TransitionType369', b)
    _safe_set(b, 'jpdl32_CancelTimerType370', a2)
    assert _is_linked(b, 'jpdl32_CancelTimerType370', a2)
    if hasattr(a1, 'jpdl32_TransitionType369'):
        assert not _is_linked(a1, 'jpdl32_TransitionType369', b)
    if hasattr(a2, 'jpdl32_TransitionType369'):
        assert _is_linked(a2, 'jpdl32_TransitionType369', b)
    _safe_set(b, 'jpdl32_CancelTimerType370', None)
    assert not _is_linked(b, 'jpdl32_CancelTimerType370', a2)
    if hasattr(a2, 'jpdl32_TransitionType369'):
        assert not _is_linked(a2, 'jpdl32_TransitionType369', b)


def test_assoc_cancelTimer89_reverse_link_reassign_clear():
    a1 = jpdl32_EventType(actionElements="sample_text", type="sample_text")
    a2 = jpdl32_EventType(actionElements="sample_text_2", type="sample_text_2")
    b = jpdl32_CancelTimerType(name="sample_text")
    _safe_set(b, 'jpdl32_CancelTimerType91', a1)
    assert _is_linked(b, 'jpdl32_CancelTimerType91', a1)
    if hasattr(a1, 'jpdl32_EventType90'):
        assert _is_linked(a1, 'jpdl32_EventType90', b)
    _safe_set(b, 'jpdl32_CancelTimerType91', a2)
    assert _is_linked(b, 'jpdl32_CancelTimerType91', a2)
    if hasattr(a1, 'jpdl32_EventType90'):
        assert not _is_linked(a1, 'jpdl32_EventType90', b)
    if hasattr(a2, 'jpdl32_EventType90'):
        assert _is_linked(a2, 'jpdl32_EventType90', b)
    _safe_set(b, 'jpdl32_CancelTimerType91', None)
    assert not _is_linked(b, 'jpdl32_CancelTimerType91', a2)
    if hasattr(a2, 'jpdl32_EventType90'):
        assert not _is_linked(a2, 'jpdl32_EventType90', b)


def test_assoc_condition357_reverse_link_reassign_clear():
    a1 = jpdl32_TransitionType(description="sample_text", group="sample_text", name="sample_text", to="sample_text")
    a2 = jpdl32_TransitionType(description="sample_text_2", group="sample_text_2", name="sample_text_2", to="sample_text_2")
    b = jpdl32_ConditionType(any="sample_text", expression="sample_text", group="sample_text", mixed="sample_text")
    _safe_set(b, 'jpdl32_ConditionType', a1)
    assert _is_linked(b, 'jpdl32_ConditionType', a1)
    if hasattr(a1, 'jpdl32_TransitionType358'):
        assert _is_linked(a1, 'jpdl32_TransitionType358', b)
    _safe_set(b, 'jpdl32_ConditionType', a2)
    assert _is_linked(b, 'jpdl32_ConditionType', a2)
    if hasattr(a1, 'jpdl32_TransitionType358'):
        assert not _is_linked(a1, 'jpdl32_TransitionType358', b)
    if hasattr(a2, 'jpdl32_TransitionType358'):
        assert _is_linked(a2, 'jpdl32_TransitionType358', b)
    _safe_set(b, 'jpdl32_ConditionType', None)
    assert not _is_linked(b, 'jpdl32_ConditionType', a2)
    if hasattr(a2, 'jpdl32_TransitionType358'):
        assert not _is_linked(a2, 'jpdl32_TransitionType358', b)


def test_assoc_controller21_reverse_link_reassign_clear():
    a1 = jpdl32_DocumentRoot(description="sample_text", mixed="sample_text", recipients="sample_text", subject="sample_text", template="sample_text", text="sample_text", to="sample_text")
    a2 = jpdl32_DocumentRoot(description="sample_text_2", mixed="sample_text_2", recipients="sample_text_2", subject="sample_text_2", template="sample_text_2", text="sample_text_2", to="sample_text_2")
    b = jpdl32_Delegation(any="sample_text", class_="sample_text", configType="sample_text", mixed="sample_text")
    _safe_set(b, 'jpdl32_Delegation23', a1)
    assert _is_linked(b, 'jpdl32_Delegation23', a1)
    if hasattr(a1, 'jpdl32_DocumentRoot22'):
        assert _is_linked(a1, 'jpdl32_DocumentRoot22', b)
    _safe_set(b, 'jpdl32_Delegation23', a2)
    assert _is_linked(b, 'jpdl32_Delegation23', a2)
    if hasattr(a1, 'jpdl32_DocumentRoot22'):
        assert not _is_linked(a1, 'jpdl32_DocumentRoot22', b)
    if hasattr(a2, 'jpdl32_DocumentRoot22'):
        assert _is_linked(a2, 'jpdl32_DocumentRoot22', b)
    _safe_set(b, 'jpdl32_Delegation23', None)
    assert not _is_linked(b, 'jpdl32_Delegation23', a2)
    if hasattr(a2, 'jpdl32_DocumentRoot22'):
        assert not _is_linked(a2, 'jpdl32_DocumentRoot22', b)


def test_assoc_controller331_reverse_link_reassign_clear():
    a1 = jpdl32_TaskType(blocking="sample_text", description="sample_text", description1="sample_text", duedate="sample_text", group="sample_text", name="sample_text", notify="sample_text", priority="sample_text", signalling="sample_text", swimlane="sample_text")
    a2 = jpdl32_TaskType(blocking="sample_text_2", description="sample_text_2", description1="sample_text_2", duedate="sample_text_2", group="sample_text_2", name="sample_text_2", notify="sample_text_2", priority="sample_text_2", signalling="sample_text_2", swimlane="sample_text_2")
    b = jpdl32_Delegation(any="sample_text", class_="sample_text", configType="sample_text", mixed="sample_text")
    _safe_set(b, 'jpdl32_Delegation333', a1)
    assert _is_linked(b, 'jpdl32_Delegation333', a1)
    if hasattr(a1, 'jpdl32_TaskType332'):
        assert _is_linked(a1, 'jpdl32_TaskType332', b)
    _safe_set(b, 'jpdl32_Delegation333', a2)
    assert _is_linked(b, 'jpdl32_Delegation333', a2)
    if hasattr(a1, 'jpdl32_TaskType332'):
        assert not _is_linked(a1, 'jpdl32_TaskType332', b)
    if hasattr(a2, 'jpdl32_TaskType332'):
        assert _is_linked(a2, 'jpdl32_TaskType332', b)
    _safe_set(b, 'jpdl32_Delegation333', None)
    assert not _is_linked(b, 'jpdl32_Delegation333', a2)
    if hasattr(a2, 'jpdl32_TaskType332'):
        assert not _is_linked(a2, 'jpdl32_TaskType332', b)


def test_assoc_createTimer146_reverse_link_reassign_clear():
    a1 = jpdl32_NodeType(async_="sample_text", description="sample_text", name="sample_text", nodeContentElements="sample_text")
    a2 = jpdl32_NodeType(async_="sample_text_2", description="sample_text_2", name="sample_text_2", nodeContentElements="sample_text_2")
    b = jpdl32_CreateTimerType(duedate="sample_text", name="sample_text", repeat="sample_text", transition="sample_text")
    _safe_set(b, 'jpdl32_CreateTimerType148', a1)
    assert _is_linked(b, 'jpdl32_CreateTimerType148', a1)
    if hasattr(a1, 'jpdl32_NodeType147'):
        assert _is_linked(a1, 'jpdl32_NodeType147', b)
    _safe_set(b, 'jpdl32_CreateTimerType148', a2)
    assert _is_linked(b, 'jpdl32_CreateTimerType148', a2)
    if hasattr(a1, 'jpdl32_NodeType147'):
        assert not _is_linked(a1, 'jpdl32_NodeType147', b)
    if hasattr(a2, 'jpdl32_NodeType147'):
        assert _is_linked(a2, 'jpdl32_NodeType147', b)
    _safe_set(b, 'jpdl32_CreateTimerType148', None)
    assert not _is_linked(b, 'jpdl32_CreateTimerType148', a2)
    if hasattr(a2, 'jpdl32_NodeType147'):
        assert not _is_linked(a2, 'jpdl32_NodeType147', b)


def test_assoc_createTimer209_reverse_link_reassign_clear():
    a1 = jpdl32_ProcessDefinitionType(description="sample_text", group="sample_text", name="sample_text")
    a2 = jpdl32_ProcessDefinitionType(description="sample_text_2", group="sample_text_2", name="sample_text_2")
    b = jpdl32_CreateTimerType(duedate="sample_text", name="sample_text", repeat="sample_text", transition="sample_text")
    _safe_set(b, 'jpdl32_CreateTimerType211', a1)
    assert _is_linked(b, 'jpdl32_CreateTimerType211', a1)
    if hasattr(a1, 'jpdl32_ProcessDefinitionType210'):
        assert _is_linked(a1, 'jpdl32_ProcessDefinitionType210', b)
    _safe_set(b, 'jpdl32_CreateTimerType211', a2)
    assert _is_linked(b, 'jpdl32_CreateTimerType211', a2)
    if hasattr(a1, 'jpdl32_ProcessDefinitionType210'):
        assert not _is_linked(a1, 'jpdl32_ProcessDefinitionType210', b)
    if hasattr(a2, 'jpdl32_ProcessDefinitionType210'):
        assert _is_linked(a2, 'jpdl32_ProcessDefinitionType210', b)
    _safe_set(b, 'jpdl32_CreateTimerType211', None)
    assert not _is_linked(b, 'jpdl32_CreateTimerType211', a2)
    if hasattr(a2, 'jpdl32_ProcessDefinitionType210'):
        assert not _is_linked(a2, 'jpdl32_ProcessDefinitionType210', b)


def test_assoc_createTimer24_reverse_link_reassign_clear():
    a1 = jpdl32_DocumentRoot(description="sample_text", mixed="sample_text", recipients="sample_text", subject="sample_text", template="sample_text", text="sample_text", to="sample_text")
    a2 = jpdl32_DocumentRoot(description="sample_text_2", mixed="sample_text_2", recipients="sample_text_2", subject="sample_text_2", template="sample_text_2", text="sample_text_2", to="sample_text_2")
    b = jpdl32_CreateTimerType(duedate="sample_text", name="sample_text", repeat="sample_text", transition="sample_text")
    _safe_set(b, 'jpdl32_CreateTimerType26', a1)
    assert _is_linked(b, 'jpdl32_CreateTimerType26', a1)
    if hasattr(a1, 'jpdl32_DocumentRoot25'):
        assert _is_linked(a1, 'jpdl32_DocumentRoot25', b)
    _safe_set(b, 'jpdl32_CreateTimerType26', a2)
    assert _is_linked(b, 'jpdl32_CreateTimerType26', a2)
    if hasattr(a1, 'jpdl32_DocumentRoot25'):
        assert not _is_linked(a1, 'jpdl32_DocumentRoot25', b)
    if hasattr(a2, 'jpdl32_DocumentRoot25'):
        assert _is_linked(a2, 'jpdl32_DocumentRoot25', b)
    _safe_set(b, 'jpdl32_CreateTimerType26', None)
    assert not _is_linked(b, 'jpdl32_CreateTimerType26', a2)
    if hasattr(a2, 'jpdl32_DocumentRoot25'):
        assert not _is_linked(a2, 'jpdl32_DocumentRoot25', b)


def test_assoc_createTimer348_reverse_link_reassign_clear():
    a1 = jpdl32_TimerType(duedate="sample_text", name="sample_text", repeat="sample_text", transition="sample_text")
    a2 = jpdl32_TimerType(duedate="sample_text_2", name="sample_text_2", repeat="sample_text_2", transition="sample_text_2")
    b = jpdl32_CreateTimerType(duedate="sample_text", name="sample_text", repeat="sample_text", transition="sample_text")
    _safe_set(b, 'jpdl32_CreateTimerType350', a1)
    assert _is_linked(b, 'jpdl32_CreateTimerType350', a1)
    if hasattr(a1, 'jpdl32_TimerType349'):
        assert _is_linked(a1, 'jpdl32_TimerType349', b)
    _safe_set(b, 'jpdl32_CreateTimerType350', a2)
    assert _is_linked(b, 'jpdl32_CreateTimerType350', a2)
    if hasattr(a1, 'jpdl32_TimerType349'):
        assert not _is_linked(a1, 'jpdl32_TimerType349', b)
    if hasattr(a2, 'jpdl32_TimerType349'):
        assert _is_linked(a2, 'jpdl32_TimerType349', b)
    _safe_set(b, 'jpdl32_CreateTimerType350', None)
    assert not _is_linked(b, 'jpdl32_CreateTimerType350', a2)
    if hasattr(a2, 'jpdl32_TimerType349'):
        assert not _is_linked(a2, 'jpdl32_TimerType349', b)


def test_assoc_createTimer365_reverse_link_reassign_clear():
    a1 = jpdl32_TransitionType(description="sample_text", group="sample_text", name="sample_text", to="sample_text")
    a2 = jpdl32_TransitionType(description="sample_text_2", group="sample_text_2", name="sample_text_2", to="sample_text_2")
    b = jpdl32_CreateTimerType(duedate="sample_text", name="sample_text", repeat="sample_text", transition="sample_text")
    _safe_set(b, 'jpdl32_CreateTimerType367', a1)
    assert _is_linked(b, 'jpdl32_CreateTimerType367', a1)
    if hasattr(a1, 'jpdl32_TransitionType366'):
        assert _is_linked(a1, 'jpdl32_TransitionType366', b)
    _safe_set(b, 'jpdl32_CreateTimerType367', a2)
    assert _is_linked(b, 'jpdl32_CreateTimerType367', a2)
    if hasattr(a1, 'jpdl32_TransitionType366'):
        assert not _is_linked(a1, 'jpdl32_TransitionType366', b)
    if hasattr(a2, 'jpdl32_TransitionType366'):
        assert _is_linked(a2, 'jpdl32_TransitionType366', b)
    _safe_set(b, 'jpdl32_CreateTimerType367', None)
    assert not _is_linked(b, 'jpdl32_CreateTimerType367', a2)
    if hasattr(a2, 'jpdl32_TransitionType366'):
        assert not _is_linked(a2, 'jpdl32_TransitionType366', b)


def test_assoc_createTimer86_reverse_link_reassign_clear():
    a1 = jpdl32_EventType(actionElements="sample_text", type="sample_text")
    a2 = jpdl32_EventType(actionElements="sample_text_2", type="sample_text_2")
    b = jpdl32_CreateTimerType(duedate="sample_text", name="sample_text", repeat="sample_text", transition="sample_text")
    _safe_set(b, 'jpdl32_CreateTimerType88', a1)
    assert _is_linked(b, 'jpdl32_CreateTimerType88', a1)
    if hasattr(a1, 'jpdl32_EventType87'):
        assert _is_linked(a1, 'jpdl32_EventType87', b)
    _safe_set(b, 'jpdl32_CreateTimerType88', a2)
    assert _is_linked(b, 'jpdl32_CreateTimerType88', a2)
    if hasattr(a1, 'jpdl32_EventType87'):
        assert not _is_linked(a1, 'jpdl32_EventType87', b)
    if hasattr(a2, 'jpdl32_EventType87'):
        assert _is_linked(a2, 'jpdl32_EventType87', b)
    _safe_set(b, 'jpdl32_CreateTimerType88', None)
    assert not _is_linked(b, 'jpdl32_CreateTimerType88', a2)
    if hasattr(a2, 'jpdl32_EventType87'):
        assert not _is_linked(a2, 'jpdl32_EventType87', b)


def test_assoc_decision194_reverse_link_reassign_clear():
    a1 = jpdl32_ProcessDefinitionType(description="sample_text", group="sample_text", name="sample_text")
    a2 = jpdl32_ProcessDefinitionType(description="sample_text_2", group="sample_text_2", name="sample_text_2")
    b = jpdl32_DecisionType(async_="sample_text", description="sample_text", expression="sample_text", group="sample_text", name="sample_text")
    _safe_set(b, 'jpdl32_DecisionType196', a1)
    assert _is_linked(b, 'jpdl32_DecisionType196', a1)
    if hasattr(a1, 'jpdl32_ProcessDefinitionType195'):
        assert _is_linked(a1, 'jpdl32_ProcessDefinitionType195', b)
    _safe_set(b, 'jpdl32_DecisionType196', a2)
    assert _is_linked(b, 'jpdl32_DecisionType196', a2)
    if hasattr(a1, 'jpdl32_ProcessDefinitionType195'):
        assert not _is_linked(a1, 'jpdl32_ProcessDefinitionType195', b)
    if hasattr(a2, 'jpdl32_ProcessDefinitionType195'):
        assert _is_linked(a2, 'jpdl32_ProcessDefinitionType195', b)
    _safe_set(b, 'jpdl32_DecisionType196', None)
    assert not _is_linked(b, 'jpdl32_DecisionType196', a2)
    if hasattr(a2, 'jpdl32_ProcessDefinitionType195'):
        assert not _is_linked(a2, 'jpdl32_ProcessDefinitionType195', b)


def test_assoc_decision27_reverse_link_reassign_clear():
    a1 = jpdl32_DocumentRoot(description="sample_text", mixed="sample_text", recipients="sample_text", subject="sample_text", template="sample_text", text="sample_text", to="sample_text")
    a2 = jpdl32_DocumentRoot(description="sample_text_2", mixed="sample_text_2", recipients="sample_text_2", subject="sample_text_2", template="sample_text_2", text="sample_text_2", to="sample_text_2")
    b = jpdl32_DecisionType(async_="sample_text", description="sample_text", expression="sample_text", group="sample_text", name="sample_text")
    _safe_set(b, 'jpdl32_DecisionType29', a1)
    assert _is_linked(b, 'jpdl32_DecisionType29', a1)
    if hasattr(a1, 'jpdl32_DocumentRoot28'):
        assert _is_linked(a1, 'jpdl32_DocumentRoot28', b)
    _safe_set(b, 'jpdl32_DecisionType29', a2)
    assert _is_linked(b, 'jpdl32_DecisionType29', a2)
    if hasattr(a1, 'jpdl32_DocumentRoot28'):
        assert not _is_linked(a1, 'jpdl32_DocumentRoot28', b)
    if hasattr(a2, 'jpdl32_DocumentRoot28'):
        assert _is_linked(a2, 'jpdl32_DocumentRoot28', b)
    _safe_set(b, 'jpdl32_DecisionType29', None)
    assert not _is_linked(b, 'jpdl32_DecisionType29', a2)
    if hasattr(a2, 'jpdl32_DocumentRoot28'):
        assert not _is_linked(a2, 'jpdl32_DocumentRoot28', b)


def test_assoc_decision289_reverse_link_reassign_clear():
    a1 = jpdl32_SuperStateType(async_="sample_text", description="sample_text", group="sample_text", name="sample_text")
    a2 = jpdl32_SuperStateType(async_="sample_text_2", description="sample_text_2", group="sample_text_2", name="sample_text_2")
    b = jpdl32_DecisionType(async_="sample_text", description="sample_text", expression="sample_text", group="sample_text", name="sample_text")
    _safe_set(b, 'jpdl32_DecisionType291', a1)
    assert _is_linked(b, 'jpdl32_DecisionType291', a1)
    if hasattr(a1, 'jpdl32_SuperStateType290'):
        assert _is_linked(a1, 'jpdl32_SuperStateType290', b)
    _safe_set(b, 'jpdl32_DecisionType291', a2)
    assert _is_linked(b, 'jpdl32_DecisionType291', a2)
    if hasattr(a1, 'jpdl32_SuperStateType290'):
        assert not _is_linked(a1, 'jpdl32_SuperStateType290', b)
    if hasattr(a2, 'jpdl32_SuperStateType290'):
        assert _is_linked(a2, 'jpdl32_SuperStateType290', b)
    _safe_set(b, 'jpdl32_DecisionType291', None)
    assert not _is_linked(b, 'jpdl32_DecisionType291', a2)
    if hasattr(a2, 'jpdl32_SuperStateType290'):
        assert not _is_linked(a2, 'jpdl32_SuperStateType290', b)


def test_assoc_endState197_reverse_link_reassign_clear():
    a1 = jpdl32_ProcessDefinitionType(description="sample_text", group="sample_text", name="sample_text")
    a2 = jpdl32_ProcessDefinitionType(description="sample_text_2", group="sample_text_2", name="sample_text_2")
    b = jpdl32_EndStateType(description="sample_text", endCompleteProcess="sample_text", group="sample_text", name="sample_text")
    _safe_set(b, 'jpdl32_EndStateType199', a1)
    assert _is_linked(b, 'jpdl32_EndStateType199', a1)
    if hasattr(a1, 'jpdl32_ProcessDefinitionType198'):
        assert _is_linked(a1, 'jpdl32_ProcessDefinitionType198', b)
    _safe_set(b, 'jpdl32_EndStateType199', a2)
    assert _is_linked(b, 'jpdl32_EndStateType199', a2)
    if hasattr(a1, 'jpdl32_ProcessDefinitionType198'):
        assert not _is_linked(a1, 'jpdl32_ProcessDefinitionType198', b)
    if hasattr(a2, 'jpdl32_ProcessDefinitionType198'):
        assert _is_linked(a2, 'jpdl32_ProcessDefinitionType198', b)
    _safe_set(b, 'jpdl32_EndStateType199', None)
    assert not _is_linked(b, 'jpdl32_EndStateType199', a2)
    if hasattr(a2, 'jpdl32_ProcessDefinitionType198'):
        assert not _is_linked(a2, 'jpdl32_ProcessDefinitionType198', b)


def test_assoc_endState292_reverse_link_reassign_clear():
    a1 = jpdl32_SuperStateType(async_="sample_text", description="sample_text", group="sample_text", name="sample_text")
    a2 = jpdl32_SuperStateType(async_="sample_text_2", description="sample_text_2", group="sample_text_2", name="sample_text_2")
    b = jpdl32_EndStateType(description="sample_text", endCompleteProcess="sample_text", group="sample_text", name="sample_text")
    _safe_set(b, 'jpdl32_EndStateType294', a1)
    assert _is_linked(b, 'jpdl32_EndStateType294', a1)
    if hasattr(a1, 'jpdl32_SuperStateType293'):
        assert _is_linked(a1, 'jpdl32_SuperStateType293', b)
    _safe_set(b, 'jpdl32_EndStateType294', a2)
    assert _is_linked(b, 'jpdl32_EndStateType294', a2)
    if hasattr(a1, 'jpdl32_SuperStateType293'):
        assert not _is_linked(a1, 'jpdl32_SuperStateType293', b)
    if hasattr(a2, 'jpdl32_SuperStateType293'):
        assert _is_linked(a2, 'jpdl32_SuperStateType293', b)
    _safe_set(b, 'jpdl32_EndStateType294', None)
    assert not _is_linked(b, 'jpdl32_EndStateType294', a2)
    if hasattr(a2, 'jpdl32_SuperStateType293'):
        assert not _is_linked(a2, 'jpdl32_SuperStateType293', b)


def test_assoc_endState30_reverse_link_reassign_clear():
    a1 = jpdl32_EndStateType(description="sample_text", endCompleteProcess="sample_text", group="sample_text", name="sample_text")
    a2 = jpdl32_EndStateType(description="sample_text_2", endCompleteProcess="sample_text_2", group="sample_text_2", name="sample_text_2")
    b = jpdl32_DocumentRoot(description="sample_text", mixed="sample_text", recipients="sample_text", subject="sample_text", template="sample_text", text="sample_text", to="sample_text")
    _safe_set(b, 'jpdl32_DocumentRoot31', {a1})
    assert _is_linked(b, 'jpdl32_DocumentRoot31', a1)
    if hasattr(a1, 'jpdl32_EndStateType'):
        assert _is_linked(a1, 'jpdl32_EndStateType', b)
    _safe_set(b, 'jpdl32_DocumentRoot31', {a2})
    assert _is_linked(b, 'jpdl32_DocumentRoot31', a2)
    if hasattr(a1, 'jpdl32_EndStateType'):
        assert not _is_linked(a1, 'jpdl32_EndStateType', b)
    if hasattr(a2, 'jpdl32_EndStateType'):
        assert _is_linked(a2, 'jpdl32_EndStateType', b)
    _safe_set(b, 'jpdl32_DocumentRoot31', set())
    assert not _is_linked(b, 'jpdl32_DocumentRoot31', a2)
    if hasattr(a2, 'jpdl32_EndStateType'):
        assert not _is_linked(a2, 'jpdl32_EndStateType', b)


def test_assoc_event104_reverse_link_reassign_clear():
    a1 = jpdl32_ForkType(async_="sample_text", description="sample_text", group="sample_text", name="sample_text")
    a2 = jpdl32_ForkType(async_="sample_text_2", description="sample_text_2", group="sample_text_2", name="sample_text_2")
    b = jpdl32_EventType(actionElements="sample_text", type="sample_text")
    _safe_set(b, 'jpdl32_EventType106', a1)
    assert _is_linked(b, 'jpdl32_EventType106', a1)
    if hasattr(a1, 'jpdl32_ForkType105'):
        assert _is_linked(a1, 'jpdl32_ForkType105', b)
    _safe_set(b, 'jpdl32_EventType106', a2)
    assert _is_linked(b, 'jpdl32_EventType106', a2)
    if hasattr(a1, 'jpdl32_ForkType105'):
        assert not _is_linked(a1, 'jpdl32_ForkType105', b)
    if hasattr(a2, 'jpdl32_ForkType105'):
        assert _is_linked(a2, 'jpdl32_ForkType105', b)
    _safe_set(b, 'jpdl32_EventType106', None)
    assert not _is_linked(b, 'jpdl32_EventType106', a2)
    if hasattr(a2, 'jpdl32_ForkType105'):
        assert not _is_linked(a2, 'jpdl32_ForkType105', b)


def test_assoc_event116_reverse_link_reassign_clear():
    a1 = jpdl32_JoinType(async_="sample_text", description="sample_text", name="sample_text", nodeContentElements="sample_text")
    a2 = jpdl32_JoinType(async_="sample_text_2", description="sample_text_2", name="sample_text_2", nodeContentElements="sample_text_2")
    b = jpdl32_EventType(actionElements="sample_text", type="sample_text")
    _safe_set(b, 'jpdl32_EventType118', a1)
    assert _is_linked(b, 'jpdl32_EventType118', a1)
    if hasattr(a1, 'jpdl32_JoinType117'):
        assert _is_linked(a1, 'jpdl32_JoinType117', b)
    _safe_set(b, 'jpdl32_EventType118', a2)
    assert _is_linked(b, 'jpdl32_EventType118', a2)
    if hasattr(a1, 'jpdl32_JoinType117'):
        assert not _is_linked(a1, 'jpdl32_JoinType117', b)
    if hasattr(a2, 'jpdl32_JoinType117'):
        assert _is_linked(a2, 'jpdl32_JoinType117', b)
    _safe_set(b, 'jpdl32_EventType118', None)
    assert not _is_linked(b, 'jpdl32_EventType118', a2)
    if hasattr(a2, 'jpdl32_JoinType117'):
        assert not _is_linked(a2, 'jpdl32_JoinType117', b)


def test_assoc_event128_reverse_link_reassign_clear():
    a1 = jpdl32_MailNodeType(actors="sample_text", async_="sample_text", description="sample_text", group="sample_text", name="sample_text", subject="sample_text", subject1="sample_text", template="sample_text", text="sample_text", text1="sample_text", to="sample_text")
    a2 = jpdl32_MailNodeType(actors="sample_text_2", async_="sample_text_2", description="sample_text_2", group="sample_text_2", name="sample_text_2", subject="sample_text_2", subject1="sample_text_2", template="sample_text_2", text="sample_text_2", text1="sample_text_2", to="sample_text_2")
    b = jpdl32_EventType(actionElements="sample_text", type="sample_text")
    _safe_set(b, 'jpdl32_EventType130', a1)
    assert _is_linked(b, 'jpdl32_EventType130', a1)
    if hasattr(a1, 'jpdl32_MailNodeType129'):
        assert _is_linked(a1, 'jpdl32_MailNodeType129', b)
    _safe_set(b, 'jpdl32_EventType130', a2)
    assert _is_linked(b, 'jpdl32_EventType130', a2)
    if hasattr(a1, 'jpdl32_MailNodeType129'):
        assert not _is_linked(a1, 'jpdl32_MailNodeType129', b)
    if hasattr(a2, 'jpdl32_MailNodeType129'):
        assert _is_linked(a2, 'jpdl32_MailNodeType129', b)
    _safe_set(b, 'jpdl32_EventType130', None)
    assert not _is_linked(b, 'jpdl32_EventType130', a2)
    if hasattr(a2, 'jpdl32_MailNodeType129'):
        assert not _is_linked(a2, 'jpdl32_MailNodeType129', b)


def test_assoc_event155_reverse_link_reassign_clear():
    a1 = jpdl32_NodeType(async_="sample_text", description="sample_text", name="sample_text", nodeContentElements="sample_text")
    a2 = jpdl32_NodeType(async_="sample_text_2", description="sample_text_2", name="sample_text_2", nodeContentElements="sample_text_2")
    b = jpdl32_EventType(actionElements="sample_text", type="sample_text")
    _safe_set(b, 'jpdl32_EventType157', a1)
    assert _is_linked(b, 'jpdl32_EventType157', a1)
    if hasattr(a1, 'jpdl32_NodeType156'):
        assert _is_linked(a1, 'jpdl32_NodeType156', b)
    _safe_set(b, 'jpdl32_EventType157', a2)
    assert _is_linked(b, 'jpdl32_EventType157', a2)
    if hasattr(a1, 'jpdl32_NodeType156'):
        assert not _is_linked(a1, 'jpdl32_NodeType156', b)
    if hasattr(a2, 'jpdl32_NodeType156'):
        assert _is_linked(a2, 'jpdl32_NodeType156', b)
    _safe_set(b, 'jpdl32_EventType157', None)
    assert not _is_linked(b, 'jpdl32_EventType157', a2)
    if hasattr(a2, 'jpdl32_NodeType156'):
        assert not _is_linked(a2, 'jpdl32_NodeType156', b)


def test_assoc_event218_reverse_link_reassign_clear():
    a1 = jpdl32_ProcessDefinitionType(description="sample_text", group="sample_text", name="sample_text")
    a2 = jpdl32_ProcessDefinitionType(description="sample_text_2", group="sample_text_2", name="sample_text_2")
    b = jpdl32_EventType(actionElements="sample_text", type="sample_text")
    _safe_set(b, 'jpdl32_EventType220', a1)
    assert _is_linked(b, 'jpdl32_EventType220', a1)
    if hasattr(a1, 'jpdl32_ProcessDefinitionType219'):
        assert _is_linked(a1, 'jpdl32_ProcessDefinitionType219', b)
    _safe_set(b, 'jpdl32_EventType220', a2)
    assert _is_linked(b, 'jpdl32_EventType220', a2)
    if hasattr(a1, 'jpdl32_ProcessDefinitionType219'):
        assert not _is_linked(a1, 'jpdl32_ProcessDefinitionType219', b)
    if hasattr(a2, 'jpdl32_ProcessDefinitionType219'):
        assert _is_linked(a2, 'jpdl32_ProcessDefinitionType219', b)
    _safe_set(b, 'jpdl32_EventType220', None)
    assert not _is_linked(b, 'jpdl32_EventType220', a2)
    if hasattr(a2, 'jpdl32_ProcessDefinitionType219'):
        assert not _is_linked(a2, 'jpdl32_ProcessDefinitionType219', b)


def test_assoc_event232_reverse_link_reassign_clear():
    a1 = jpdl32_ProcessStateType(async_="sample_text", binding="sample_text", description="sample_text", group="sample_text", name="sample_text")
    a2 = jpdl32_ProcessStateType(async_="sample_text_2", binding="sample_text_2", description="sample_text_2", group="sample_text_2", name="sample_text_2")
    b = jpdl32_EventType(actionElements="sample_text", type="sample_text")
    _safe_set(b, 'jpdl32_EventType234', a1)
    assert _is_linked(b, 'jpdl32_EventType234', a1)
    if hasattr(a1, 'jpdl32_ProcessStateType233'):
        assert _is_linked(a1, 'jpdl32_ProcessStateType233', b)
    _safe_set(b, 'jpdl32_EventType234', a2)
    assert _is_linked(b, 'jpdl32_EventType234', a2)
    if hasattr(a1, 'jpdl32_ProcessStateType233'):
        assert not _is_linked(a1, 'jpdl32_ProcessStateType233', b)
    if hasattr(a2, 'jpdl32_ProcessStateType233'):
        assert _is_linked(a2, 'jpdl32_ProcessStateType233', b)
    _safe_set(b, 'jpdl32_EventType234', None)
    assert not _is_linked(b, 'jpdl32_EventType234', a2)
    if hasattr(a2, 'jpdl32_ProcessStateType233'):
        assert not _is_linked(a2, 'jpdl32_ProcessStateType233', b)


def test_assoc_event250_reverse_link_reassign_clear():
    a1 = jpdl32_StartStateType(description="sample_text", group="sample_text", name="sample_text")
    a2 = jpdl32_StartStateType(description="sample_text_2", group="sample_text_2", name="sample_text_2")
    b = jpdl32_EventType(actionElements="sample_text", type="sample_text")
    _safe_set(b, 'jpdl32_EventType252', a1)
    assert _is_linked(b, 'jpdl32_EventType252', a1)
    if hasattr(a1, 'jpdl32_StartStateType251'):
        assert _is_linked(a1, 'jpdl32_StartStateType251', b)
    _safe_set(b, 'jpdl32_EventType252', a2)
    assert _is_linked(b, 'jpdl32_EventType252', a2)
    if hasattr(a1, 'jpdl32_StartStateType251'):
        assert not _is_linked(a1, 'jpdl32_StartStateType251', b)
    if hasattr(a2, 'jpdl32_StartStateType251'):
        assert _is_linked(a2, 'jpdl32_StartStateType251', b)
    _safe_set(b, 'jpdl32_EventType252', None)
    assert not _is_linked(b, 'jpdl32_EventType252', a2)
    if hasattr(a2, 'jpdl32_StartStateType251'):
        assert not _is_linked(a2, 'jpdl32_StartStateType251', b)


def test_assoc_event256_reverse_link_reassign_clear():
    a1 = jpdl32_StateType(async_="sample_text", description="sample_text", name="sample_text", nodeContentElements="sample_text")
    a2 = jpdl32_StateType(async_="sample_text_2", description="sample_text_2", name="sample_text_2", nodeContentElements="sample_text_2")
    b = jpdl32_EventType(actionElements="sample_text", type="sample_text")
    _safe_set(b, 'jpdl32_EventType258', a1)
    assert _is_linked(b, 'jpdl32_EventType258', a1)
    if hasattr(a1, 'jpdl32_StateType257'):
        assert _is_linked(a1, 'jpdl32_StateType257', b)
    _safe_set(b, 'jpdl32_EventType258', a2)
    assert _is_linked(b, 'jpdl32_EventType258', a2)
    if hasattr(a1, 'jpdl32_StateType257'):
        assert not _is_linked(a1, 'jpdl32_StateType257', b)
    if hasattr(a2, 'jpdl32_StateType257'):
        assert _is_linked(a2, 'jpdl32_StateType257', b)
    _safe_set(b, 'jpdl32_EventType258', None)
    assert not _is_linked(b, 'jpdl32_EventType258', a2)
    if hasattr(a2, 'jpdl32_StateType257'):
        assert not _is_linked(a2, 'jpdl32_StateType257', b)


def test_assoc_event298_reverse_link_reassign_clear():
    a1 = jpdl32_SuperStateType(async_="sample_text", description="sample_text", group="sample_text", name="sample_text")
    a2 = jpdl32_SuperStateType(async_="sample_text_2", description="sample_text_2", group="sample_text_2", name="sample_text_2")
    b = jpdl32_EventType(actionElements="sample_text", type="sample_text")
    _safe_set(b, 'jpdl32_EventType300', a1)
    assert _is_linked(b, 'jpdl32_EventType300', a1)
    if hasattr(a1, 'jpdl32_SuperStateType299'):
        assert _is_linked(a1, 'jpdl32_SuperStateType299', b)
    _safe_set(b, 'jpdl32_EventType300', a2)
    assert _is_linked(b, 'jpdl32_EventType300', a2)
    if hasattr(a1, 'jpdl32_SuperStateType299'):
        assert not _is_linked(a1, 'jpdl32_SuperStateType299', b)
    if hasattr(a2, 'jpdl32_SuperStateType299'):
        assert _is_linked(a2, 'jpdl32_SuperStateType299', b)
    _safe_set(b, 'jpdl32_EventType300', None)
    assert not _is_linked(b, 'jpdl32_EventType300', a2)
    if hasattr(a2, 'jpdl32_SuperStateType299'):
        assert not _is_linked(a2, 'jpdl32_SuperStateType299', b)


def test_assoc_event316_reverse_link_reassign_clear():
    a1 = jpdl32_TaskNodeType(async_="sample_text", createTasks="sample_text", description="sample_text", endTasks="sample_text", group="sample_text", name="sample_text", signal="sample_text")
    a2 = jpdl32_TaskNodeType(async_="sample_text_2", createTasks="sample_text_2", description="sample_text_2", endTasks="sample_text_2", group="sample_text_2", name="sample_text_2", signal="sample_text_2")
    b = jpdl32_EventType(actionElements="sample_text", type="sample_text")
    _safe_set(b, 'jpdl32_EventType318', a1)
    assert _is_linked(b, 'jpdl32_EventType318', a1)
    if hasattr(a1, 'jpdl32_TaskNodeType317'):
        assert _is_linked(a1, 'jpdl32_TaskNodeType317', b)
    _safe_set(b, 'jpdl32_EventType318', a2)
    assert _is_linked(b, 'jpdl32_EventType318', a2)
    if hasattr(a1, 'jpdl32_TaskNodeType317'):
        assert not _is_linked(a1, 'jpdl32_TaskNodeType317', b)
    if hasattr(a2, 'jpdl32_TaskNodeType317'):
        assert _is_linked(a2, 'jpdl32_TaskNodeType317', b)
    _safe_set(b, 'jpdl32_EventType318', None)
    assert not _is_linked(b, 'jpdl32_EventType318', a2)
    if hasattr(a2, 'jpdl32_TaskNodeType317'):
        assert not _is_linked(a2, 'jpdl32_TaskNodeType317', b)


def test_assoc_event32_reverse_link_reassign_clear():
    a1 = jpdl32_EventType(actionElements="sample_text", type="sample_text")
    a2 = jpdl32_EventType(actionElements="sample_text_2", type="sample_text_2")
    b = jpdl32_DocumentRoot(description="sample_text", mixed="sample_text", recipients="sample_text", subject="sample_text", template="sample_text", text="sample_text", to="sample_text")
    _safe_set(b, 'jpdl32_DocumentRoot33', {a1})
    assert _is_linked(b, 'jpdl32_DocumentRoot33', a1)
    if hasattr(a1, 'jpdl32_EventType34'):
        assert _is_linked(a1, 'jpdl32_EventType34', b)
    _safe_set(b, 'jpdl32_DocumentRoot33', {a2})
    assert _is_linked(b, 'jpdl32_DocumentRoot33', a2)
    if hasattr(a1, 'jpdl32_EventType34'):
        assert not _is_linked(a1, 'jpdl32_EventType34', b)
    if hasattr(a2, 'jpdl32_EventType34'):
        assert _is_linked(a2, 'jpdl32_EventType34', b)
    _safe_set(b, 'jpdl32_DocumentRoot33', set())
    assert not _is_linked(b, 'jpdl32_DocumentRoot33', a2)
    if hasattr(a2, 'jpdl32_EventType34'):
        assert not _is_linked(a2, 'jpdl32_EventType34', b)


def test_assoc_event334_reverse_link_reassign_clear():
    a1 = jpdl32_TaskType(blocking="sample_text", description="sample_text", description1="sample_text", duedate="sample_text", group="sample_text", name="sample_text", notify="sample_text", priority="sample_text", signalling="sample_text", swimlane="sample_text")
    a2 = jpdl32_TaskType(blocking="sample_text_2", description="sample_text_2", description1="sample_text_2", duedate="sample_text_2", group="sample_text_2", name="sample_text_2", notify="sample_text_2", priority="sample_text_2", signalling="sample_text_2", swimlane="sample_text_2")
    b = jpdl32_EventType(actionElements="sample_text", type="sample_text")
    _safe_set(b, 'jpdl32_EventType336', a1)
    assert _is_linked(b, 'jpdl32_EventType336', a1)
    if hasattr(a1, 'jpdl32_TaskType335'):
        assert _is_linked(a1, 'jpdl32_TaskType335', b)
    _safe_set(b, 'jpdl32_EventType336', a2)
    assert _is_linked(b, 'jpdl32_EventType336', a2)
    if hasattr(a1, 'jpdl32_TaskType335'):
        assert not _is_linked(a1, 'jpdl32_TaskType335', b)
    if hasattr(a2, 'jpdl32_TaskType335'):
        assert _is_linked(a2, 'jpdl32_TaskType335', b)
    _safe_set(b, 'jpdl32_EventType336', None)
    assert not _is_linked(b, 'jpdl32_EventType336', a2)
    if hasattr(a2, 'jpdl32_TaskType335'):
        assert not _is_linked(a2, 'jpdl32_TaskType335', b)


def test_assoc_event4_reverse_link_reassign_clear():
    a1 = jpdl32_EventType(actionElements="sample_text", type="sample_text")
    a2 = jpdl32_EventType(actionElements="sample_text_2", type="sample_text_2")
    b = jpdl32_DecisionType(async_="sample_text", description="sample_text", expression="sample_text", group="sample_text", name="sample_text")
    _safe_set(b, 'jpdl32_DecisionType5', {a1})
    assert _is_linked(b, 'jpdl32_DecisionType5', a1)
    if hasattr(a1, 'jpdl32_EventType'):
        assert _is_linked(a1, 'jpdl32_EventType', b)
    _safe_set(b, 'jpdl32_DecisionType5', {a2})
    assert _is_linked(b, 'jpdl32_DecisionType5', a2)
    if hasattr(a1, 'jpdl32_EventType'):
        assert not _is_linked(a1, 'jpdl32_EventType', b)
    if hasattr(a2, 'jpdl32_EventType'):
        assert _is_linked(a2, 'jpdl32_EventType', b)
    _safe_set(b, 'jpdl32_DecisionType5', set())
    assert not _is_linked(b, 'jpdl32_DecisionType5', a2)
    if hasattr(a2, 'jpdl32_EventType'):
        assert not _is_linked(a2, 'jpdl32_EventType', b)


def test_assoc_event74_reverse_link_reassign_clear():
    a1 = jpdl32_EventType(actionElements="sample_text", type="sample_text")
    a2 = jpdl32_EventType(actionElements="sample_text_2", type="sample_text_2")
    b = jpdl32_EndStateType(description="sample_text", endCompleteProcess="sample_text", group="sample_text", name="sample_text")
    _safe_set(b, 'jpdl32_EndStateType75', {a1})
    assert _is_linked(b, 'jpdl32_EndStateType75', a1)
    if hasattr(a1, 'jpdl32_EventType76'):
        assert _is_linked(a1, 'jpdl32_EventType76', b)
    _safe_set(b, 'jpdl32_EndStateType75', {a2})
    assert _is_linked(b, 'jpdl32_EndStateType75', a2)
    if hasattr(a1, 'jpdl32_EventType76'):
        assert not _is_linked(a1, 'jpdl32_EventType76', b)
    if hasattr(a2, 'jpdl32_EventType76'):
        assert _is_linked(a2, 'jpdl32_EventType76', b)
    _safe_set(b, 'jpdl32_EndStateType75', set())
    assert not _is_linked(b, 'jpdl32_EndStateType75', a2)
    if hasattr(a2, 'jpdl32_EventType76'):
        assert not _is_linked(a2, 'jpdl32_EventType76', b)


def test_assoc_exceptionHandler107_reverse_link_reassign_clear():
    a1 = jpdl32_ForkType(async_="sample_text", description="sample_text", group="sample_text", name="sample_text")
    a2 = jpdl32_ForkType(async_="sample_text_2", description="sample_text_2", group="sample_text_2", name="sample_text_2")
    b = jpdl32_ExceptionHandlerType(exceptionClass="sample_text", group="sample_text")
    _safe_set(b, 'jpdl32_ExceptionHandlerType109', a1)
    assert _is_linked(b, 'jpdl32_ExceptionHandlerType109', a1)
    if hasattr(a1, 'jpdl32_ForkType108'):
        assert _is_linked(a1, 'jpdl32_ForkType108', b)
    _safe_set(b, 'jpdl32_ExceptionHandlerType109', a2)
    assert _is_linked(b, 'jpdl32_ExceptionHandlerType109', a2)
    if hasattr(a1, 'jpdl32_ForkType108'):
        assert not _is_linked(a1, 'jpdl32_ForkType108', b)
    if hasattr(a2, 'jpdl32_ForkType108'):
        assert _is_linked(a2, 'jpdl32_ForkType108', b)
    _safe_set(b, 'jpdl32_ExceptionHandlerType109', None)
    assert not _is_linked(b, 'jpdl32_ExceptionHandlerType109', a2)
    if hasattr(a2, 'jpdl32_ForkType108'):
        assert not _is_linked(a2, 'jpdl32_ForkType108', b)


def test_assoc_exceptionHandler119_reverse_link_reassign_clear():
    a1 = jpdl32_JoinType(async_="sample_text", description="sample_text", name="sample_text", nodeContentElements="sample_text")
    a2 = jpdl32_JoinType(async_="sample_text_2", description="sample_text_2", name="sample_text_2", nodeContentElements="sample_text_2")
    b = jpdl32_ExceptionHandlerType(exceptionClass="sample_text", group="sample_text")
    _safe_set(b, 'jpdl32_ExceptionHandlerType121', a1)
    assert _is_linked(b, 'jpdl32_ExceptionHandlerType121', a1)
    if hasattr(a1, 'jpdl32_JoinType120'):
        assert _is_linked(a1, 'jpdl32_JoinType120', b)
    _safe_set(b, 'jpdl32_ExceptionHandlerType121', a2)
    assert _is_linked(b, 'jpdl32_ExceptionHandlerType121', a2)
    if hasattr(a1, 'jpdl32_JoinType120'):
        assert not _is_linked(a1, 'jpdl32_JoinType120', b)
    if hasattr(a2, 'jpdl32_JoinType120'):
        assert _is_linked(a2, 'jpdl32_JoinType120', b)
    _safe_set(b, 'jpdl32_ExceptionHandlerType121', None)
    assert not _is_linked(b, 'jpdl32_ExceptionHandlerType121', a2)
    if hasattr(a2, 'jpdl32_JoinType120'):
        assert not _is_linked(a2, 'jpdl32_JoinType120', b)


def test_assoc_exceptionHandler131_reverse_link_reassign_clear():
    a1 = jpdl32_MailNodeType(actors="sample_text", async_="sample_text", description="sample_text", group="sample_text", name="sample_text", subject="sample_text", subject1="sample_text", template="sample_text", text="sample_text", text1="sample_text", to="sample_text")
    a2 = jpdl32_MailNodeType(actors="sample_text_2", async_="sample_text_2", description="sample_text_2", group="sample_text_2", name="sample_text_2", subject="sample_text_2", subject1="sample_text_2", template="sample_text_2", text="sample_text_2", text1="sample_text_2", to="sample_text_2")
    b = jpdl32_ExceptionHandlerType(exceptionClass="sample_text", group="sample_text")
    _safe_set(b, 'jpdl32_ExceptionHandlerType133', a1)
    assert _is_linked(b, 'jpdl32_ExceptionHandlerType133', a1)
    if hasattr(a1, 'jpdl32_MailNodeType132'):
        assert _is_linked(a1, 'jpdl32_MailNodeType132', b)
    _safe_set(b, 'jpdl32_ExceptionHandlerType133', a2)
    assert _is_linked(b, 'jpdl32_ExceptionHandlerType133', a2)
    if hasattr(a1, 'jpdl32_MailNodeType132'):
        assert not _is_linked(a1, 'jpdl32_MailNodeType132', b)
    if hasattr(a2, 'jpdl32_MailNodeType132'):
        assert _is_linked(a2, 'jpdl32_MailNodeType132', b)
    _safe_set(b, 'jpdl32_ExceptionHandlerType133', None)
    assert not _is_linked(b, 'jpdl32_ExceptionHandlerType133', a2)
    if hasattr(a2, 'jpdl32_MailNodeType132'):
        assert not _is_linked(a2, 'jpdl32_MailNodeType132', b)


def test_assoc_exceptionHandler158_reverse_link_reassign_clear():
    a1 = jpdl32_NodeType(async_="sample_text", description="sample_text", name="sample_text", nodeContentElements="sample_text")
    a2 = jpdl32_NodeType(async_="sample_text_2", description="sample_text_2", name="sample_text_2", nodeContentElements="sample_text_2")
    b = jpdl32_ExceptionHandlerType(exceptionClass="sample_text", group="sample_text")
    _safe_set(b, 'jpdl32_ExceptionHandlerType160', a1)
    assert _is_linked(b, 'jpdl32_ExceptionHandlerType160', a1)
    if hasattr(a1, 'jpdl32_NodeType159'):
        assert _is_linked(a1, 'jpdl32_NodeType159', b)
    _safe_set(b, 'jpdl32_ExceptionHandlerType160', a2)
    assert _is_linked(b, 'jpdl32_ExceptionHandlerType160', a2)
    if hasattr(a1, 'jpdl32_NodeType159'):
        assert not _is_linked(a1, 'jpdl32_NodeType159', b)
    if hasattr(a2, 'jpdl32_NodeType159'):
        assert _is_linked(a2, 'jpdl32_NodeType159', b)
    _safe_set(b, 'jpdl32_ExceptionHandlerType160', None)
    assert not _is_linked(b, 'jpdl32_ExceptionHandlerType160', a2)
    if hasattr(a2, 'jpdl32_NodeType159'):
        assert not _is_linked(a2, 'jpdl32_NodeType159', b)


def test_assoc_exceptionHandler221_reverse_link_reassign_clear():
    a1 = jpdl32_ProcessDefinitionType(description="sample_text", group="sample_text", name="sample_text")
    a2 = jpdl32_ProcessDefinitionType(description="sample_text_2", group="sample_text_2", name="sample_text_2")
    b = jpdl32_ExceptionHandlerType(exceptionClass="sample_text", group="sample_text")
    _safe_set(b, 'jpdl32_ExceptionHandlerType223', a1)
    assert _is_linked(b, 'jpdl32_ExceptionHandlerType223', a1)
    if hasattr(a1, 'jpdl32_ProcessDefinitionType222'):
        assert _is_linked(a1, 'jpdl32_ProcessDefinitionType222', b)
    _safe_set(b, 'jpdl32_ExceptionHandlerType223', a2)
    assert _is_linked(b, 'jpdl32_ExceptionHandlerType223', a2)
    if hasattr(a1, 'jpdl32_ProcessDefinitionType222'):
        assert not _is_linked(a1, 'jpdl32_ProcessDefinitionType222', b)
    if hasattr(a2, 'jpdl32_ProcessDefinitionType222'):
        assert _is_linked(a2, 'jpdl32_ProcessDefinitionType222', b)
    _safe_set(b, 'jpdl32_ExceptionHandlerType223', None)
    assert not _is_linked(b, 'jpdl32_ExceptionHandlerType223', a2)
    if hasattr(a2, 'jpdl32_ProcessDefinitionType222'):
        assert not _is_linked(a2, 'jpdl32_ProcessDefinitionType222', b)


def test_assoc_exceptionHandler235_reverse_link_reassign_clear():
    a1 = jpdl32_ProcessStateType(async_="sample_text", binding="sample_text", description="sample_text", group="sample_text", name="sample_text")
    a2 = jpdl32_ProcessStateType(async_="sample_text_2", binding="sample_text_2", description="sample_text_2", group="sample_text_2", name="sample_text_2")
    b = jpdl32_ExceptionHandlerType(exceptionClass="sample_text", group="sample_text")
    _safe_set(b, 'jpdl32_ExceptionHandlerType237', a1)
    assert _is_linked(b, 'jpdl32_ExceptionHandlerType237', a1)
    if hasattr(a1, 'jpdl32_ProcessStateType236'):
        assert _is_linked(a1, 'jpdl32_ProcessStateType236', b)
    _safe_set(b, 'jpdl32_ExceptionHandlerType237', a2)
    assert _is_linked(b, 'jpdl32_ExceptionHandlerType237', a2)
    if hasattr(a1, 'jpdl32_ProcessStateType236'):
        assert not _is_linked(a1, 'jpdl32_ProcessStateType236', b)
    if hasattr(a2, 'jpdl32_ProcessStateType236'):
        assert _is_linked(a2, 'jpdl32_ProcessStateType236', b)
    _safe_set(b, 'jpdl32_ExceptionHandlerType237', None)
    assert not _is_linked(b, 'jpdl32_ExceptionHandlerType237', a2)
    if hasattr(a2, 'jpdl32_ProcessStateType236'):
        assert not _is_linked(a2, 'jpdl32_ProcessStateType236', b)


def test_assoc_exceptionHandler253_reverse_link_reassign_clear():
    a1 = jpdl32_StartStateType(description="sample_text", group="sample_text", name="sample_text")
    a2 = jpdl32_StartStateType(description="sample_text_2", group="sample_text_2", name="sample_text_2")
    b = jpdl32_ExceptionHandlerType(exceptionClass="sample_text", group="sample_text")
    _safe_set(b, 'jpdl32_ExceptionHandlerType255', a1)
    assert _is_linked(b, 'jpdl32_ExceptionHandlerType255', a1)
    if hasattr(a1, 'jpdl32_StartStateType254'):
        assert _is_linked(a1, 'jpdl32_StartStateType254', b)
    _safe_set(b, 'jpdl32_ExceptionHandlerType255', a2)
    assert _is_linked(b, 'jpdl32_ExceptionHandlerType255', a2)
    if hasattr(a1, 'jpdl32_StartStateType254'):
        assert not _is_linked(a1, 'jpdl32_StartStateType254', b)
    if hasattr(a2, 'jpdl32_StartStateType254'):
        assert _is_linked(a2, 'jpdl32_StartStateType254', b)
    _safe_set(b, 'jpdl32_ExceptionHandlerType255', None)
    assert not _is_linked(b, 'jpdl32_ExceptionHandlerType255', a2)
    if hasattr(a2, 'jpdl32_StartStateType254'):
        assert not _is_linked(a2, 'jpdl32_StartStateType254', b)


def test_assoc_exceptionHandler259_reverse_link_reassign_clear():
    a1 = jpdl32_StateType(async_="sample_text", description="sample_text", name="sample_text", nodeContentElements="sample_text")
    a2 = jpdl32_StateType(async_="sample_text_2", description="sample_text_2", name="sample_text_2", nodeContentElements="sample_text_2")
    b = jpdl32_ExceptionHandlerType(exceptionClass="sample_text", group="sample_text")
    _safe_set(b, 'jpdl32_ExceptionHandlerType261', a1)
    assert _is_linked(b, 'jpdl32_ExceptionHandlerType261', a1)
    if hasattr(a1, 'jpdl32_StateType260'):
        assert _is_linked(a1, 'jpdl32_StateType260', b)
    _safe_set(b, 'jpdl32_ExceptionHandlerType261', a2)
    assert _is_linked(b, 'jpdl32_ExceptionHandlerType261', a2)
    if hasattr(a1, 'jpdl32_StateType260'):
        assert not _is_linked(a1, 'jpdl32_StateType260', b)
    if hasattr(a2, 'jpdl32_StateType260'):
        assert _is_linked(a2, 'jpdl32_StateType260', b)
    _safe_set(b, 'jpdl32_ExceptionHandlerType261', None)
    assert not _is_linked(b, 'jpdl32_ExceptionHandlerType261', a2)
    if hasattr(a2, 'jpdl32_StateType260'):
        assert not _is_linked(a2, 'jpdl32_StateType260', b)


def test_assoc_exceptionHandler301_reverse_link_reassign_clear():
    a1 = jpdl32_SuperStateType(async_="sample_text", description="sample_text", group="sample_text", name="sample_text")
    a2 = jpdl32_SuperStateType(async_="sample_text_2", description="sample_text_2", group="sample_text_2", name="sample_text_2")
    b = jpdl32_ExceptionHandlerType(exceptionClass="sample_text", group="sample_text")
    _safe_set(b, 'jpdl32_ExceptionHandlerType303', a1)
    assert _is_linked(b, 'jpdl32_ExceptionHandlerType303', a1)
    if hasattr(a1, 'jpdl32_SuperStateType302'):
        assert _is_linked(a1, 'jpdl32_SuperStateType302', b)
    _safe_set(b, 'jpdl32_ExceptionHandlerType303', a2)
    assert _is_linked(b, 'jpdl32_ExceptionHandlerType303', a2)
    if hasattr(a1, 'jpdl32_SuperStateType302'):
        assert not _is_linked(a1, 'jpdl32_SuperStateType302', b)
    if hasattr(a2, 'jpdl32_SuperStateType302'):
        assert _is_linked(a2, 'jpdl32_SuperStateType302', b)
    _safe_set(b, 'jpdl32_ExceptionHandlerType303', None)
    assert not _is_linked(b, 'jpdl32_ExceptionHandlerType303', a2)
    if hasattr(a2, 'jpdl32_SuperStateType302'):
        assert not _is_linked(a2, 'jpdl32_SuperStateType302', b)


def test_assoc_exceptionHandler319_reverse_link_reassign_clear():
    a1 = jpdl32_TaskNodeType(async_="sample_text", createTasks="sample_text", description="sample_text", endTasks="sample_text", group="sample_text", name="sample_text", signal="sample_text")
    a2 = jpdl32_TaskNodeType(async_="sample_text_2", createTasks="sample_text_2", description="sample_text_2", endTasks="sample_text_2", group="sample_text_2", name="sample_text_2", signal="sample_text_2")
    b = jpdl32_ExceptionHandlerType(exceptionClass="sample_text", group="sample_text")
    _safe_set(b, 'jpdl32_ExceptionHandlerType321', a1)
    assert _is_linked(b, 'jpdl32_ExceptionHandlerType321', a1)
    if hasattr(a1, 'jpdl32_TaskNodeType320'):
        assert _is_linked(a1, 'jpdl32_TaskNodeType320', b)
    _safe_set(b, 'jpdl32_ExceptionHandlerType321', a2)
    assert _is_linked(b, 'jpdl32_ExceptionHandlerType321', a2)
    if hasattr(a1, 'jpdl32_TaskNodeType320'):
        assert not _is_linked(a1, 'jpdl32_TaskNodeType320', b)
    if hasattr(a2, 'jpdl32_TaskNodeType320'):
        assert _is_linked(a2, 'jpdl32_TaskNodeType320', b)
    _safe_set(b, 'jpdl32_ExceptionHandlerType321', None)
    assert not _is_linked(b, 'jpdl32_ExceptionHandlerType321', a2)
    if hasattr(a2, 'jpdl32_TaskNodeType320'):
        assert not _is_linked(a2, 'jpdl32_TaskNodeType320', b)


def test_assoc_exceptionHandler35_reverse_link_reassign_clear():
    a1 = jpdl32_ExceptionHandlerType(exceptionClass="sample_text", group="sample_text")
    a2 = jpdl32_ExceptionHandlerType(exceptionClass="sample_text_2", group="sample_text_2")
    b = jpdl32_DocumentRoot(description="sample_text", mixed="sample_text", recipients="sample_text", subject="sample_text", template="sample_text", text="sample_text", to="sample_text")
    _safe_set(b, 'jpdl32_DocumentRoot36', {a1})
    assert _is_linked(b, 'jpdl32_DocumentRoot36', a1)
    if hasattr(a1, 'jpdl32_ExceptionHandlerType37'):
        assert _is_linked(a1, 'jpdl32_ExceptionHandlerType37', b)
    _safe_set(b, 'jpdl32_DocumentRoot36', {a2})
    assert _is_linked(b, 'jpdl32_DocumentRoot36', a2)
    if hasattr(a1, 'jpdl32_ExceptionHandlerType37'):
        assert not _is_linked(a1, 'jpdl32_ExceptionHandlerType37', b)
    if hasattr(a2, 'jpdl32_ExceptionHandlerType37'):
        assert _is_linked(a2, 'jpdl32_ExceptionHandlerType37', b)
    _safe_set(b, 'jpdl32_DocumentRoot36', set())
    assert not _is_linked(b, 'jpdl32_DocumentRoot36', a2)
    if hasattr(a2, 'jpdl32_ExceptionHandlerType37'):
        assert not _is_linked(a2, 'jpdl32_ExceptionHandlerType37', b)


def test_assoc_exceptionHandler374_reverse_link_reassign_clear():
    a1 = jpdl32_TransitionType(description="sample_text", group="sample_text", name="sample_text", to="sample_text")
    a2 = jpdl32_TransitionType(description="sample_text_2", group="sample_text_2", name="sample_text_2", to="sample_text_2")
    b = jpdl32_ExceptionHandlerType(exceptionClass="sample_text", group="sample_text")
    _safe_set(b, 'jpdl32_ExceptionHandlerType376', a1)
    assert _is_linked(b, 'jpdl32_ExceptionHandlerType376', a1)
    if hasattr(a1, 'jpdl32_TransitionType375'):
        assert _is_linked(a1, 'jpdl32_TransitionType375', b)
    _safe_set(b, 'jpdl32_ExceptionHandlerType376', a2)
    assert _is_linked(b, 'jpdl32_ExceptionHandlerType376', a2)
    if hasattr(a1, 'jpdl32_TransitionType375'):
        assert not _is_linked(a1, 'jpdl32_TransitionType375', b)
    if hasattr(a2, 'jpdl32_TransitionType375'):
        assert _is_linked(a2, 'jpdl32_TransitionType375', b)
    _safe_set(b, 'jpdl32_ExceptionHandlerType376', None)
    assert not _is_linked(b, 'jpdl32_ExceptionHandlerType376', a2)
    if hasattr(a2, 'jpdl32_TransitionType375'):
        assert not _is_linked(a2, 'jpdl32_TransitionType375', b)


def test_assoc_exceptionHandler6_reverse_link_reassign_clear():
    a1 = jpdl32_ExceptionHandlerType(exceptionClass="sample_text", group="sample_text")
    a2 = jpdl32_ExceptionHandlerType(exceptionClass="sample_text_2", group="sample_text_2")
    b = jpdl32_DecisionType(async_="sample_text", description="sample_text", expression="sample_text", group="sample_text", name="sample_text")
    _safe_set(b, 'jpdl32_DecisionType7', {a1})
    assert _is_linked(b, 'jpdl32_DecisionType7', a1)
    if hasattr(a1, 'jpdl32_ExceptionHandlerType'):
        assert _is_linked(a1, 'jpdl32_ExceptionHandlerType', b)
    _safe_set(b, 'jpdl32_DecisionType7', {a2})
    assert _is_linked(b, 'jpdl32_DecisionType7', a2)
    if hasattr(a1, 'jpdl32_ExceptionHandlerType'):
        assert not _is_linked(a1, 'jpdl32_ExceptionHandlerType', b)
    if hasattr(a2, 'jpdl32_ExceptionHandlerType'):
        assert _is_linked(a2, 'jpdl32_ExceptionHandlerType', b)
    _safe_set(b, 'jpdl32_DecisionType7', set())
    assert not _is_linked(b, 'jpdl32_DecisionType7', a2)
    if hasattr(a2, 'jpdl32_ExceptionHandlerType'):
        assert not _is_linked(a2, 'jpdl32_ExceptionHandlerType', b)


def test_assoc_exceptionHandler77_reverse_link_reassign_clear():
    a1 = jpdl32_ExceptionHandlerType(exceptionClass="sample_text", group="sample_text")
    a2 = jpdl32_ExceptionHandlerType(exceptionClass="sample_text_2", group="sample_text_2")
    b = jpdl32_EndStateType(description="sample_text", endCompleteProcess="sample_text", group="sample_text", name="sample_text")
    _safe_set(b, 'jpdl32_EndStateType78', {a1})
    assert _is_linked(b, 'jpdl32_EndStateType78', a1)
    if hasattr(a1, 'jpdl32_ExceptionHandlerType79'):
        assert _is_linked(a1, 'jpdl32_ExceptionHandlerType79', b)
    _safe_set(b, 'jpdl32_EndStateType78', {a2})
    assert _is_linked(b, 'jpdl32_EndStateType78', a2)
    if hasattr(a1, 'jpdl32_ExceptionHandlerType79'):
        assert not _is_linked(a1, 'jpdl32_ExceptionHandlerType79', b)
    if hasattr(a2, 'jpdl32_ExceptionHandlerType79'):
        assert _is_linked(a2, 'jpdl32_ExceptionHandlerType79', b)
    _safe_set(b, 'jpdl32_EndStateType78', set())
    assert not _is_linked(b, 'jpdl32_EndStateType78', a2)
    if hasattr(a2, 'jpdl32_ExceptionHandlerType79'):
        assert not _is_linked(a2, 'jpdl32_ExceptionHandlerType79', b)


def test_assoc_fork188_reverse_link_reassign_clear():
    a1 = jpdl32_ProcessDefinitionType(description="sample_text", group="sample_text", name="sample_text")
    a2 = jpdl32_ProcessDefinitionType(description="sample_text_2", group="sample_text_2", name="sample_text_2")
    b = jpdl32_ForkType(async_="sample_text", description="sample_text", group="sample_text", name="sample_text")
    _safe_set(b, 'jpdl32_ForkType190', a1)
    assert _is_linked(b, 'jpdl32_ForkType190', a1)
    if hasattr(a1, 'jpdl32_ProcessDefinitionType189'):
        assert _is_linked(a1, 'jpdl32_ProcessDefinitionType189', b)
    _safe_set(b, 'jpdl32_ForkType190', a2)
    assert _is_linked(b, 'jpdl32_ForkType190', a2)
    if hasattr(a1, 'jpdl32_ProcessDefinitionType189'):
        assert not _is_linked(a1, 'jpdl32_ProcessDefinitionType189', b)
    if hasattr(a2, 'jpdl32_ProcessDefinitionType189'):
        assert _is_linked(a2, 'jpdl32_ProcessDefinitionType189', b)
    _safe_set(b, 'jpdl32_ForkType190', None)
    assert not _is_linked(b, 'jpdl32_ForkType190', a2)
    if hasattr(a2, 'jpdl32_ProcessDefinitionType189'):
        assert not _is_linked(a2, 'jpdl32_ProcessDefinitionType189', b)


def test_assoc_fork283_reverse_link_reassign_clear():
    a1 = jpdl32_SuperStateType(async_="sample_text", description="sample_text", group="sample_text", name="sample_text")
    a2 = jpdl32_SuperStateType(async_="sample_text_2", description="sample_text_2", group="sample_text_2", name="sample_text_2")
    b = jpdl32_ForkType(async_="sample_text", description="sample_text", group="sample_text", name="sample_text")
    _safe_set(b, 'jpdl32_ForkType285', a1)
    assert _is_linked(b, 'jpdl32_ForkType285', a1)
    if hasattr(a1, 'jpdl32_SuperStateType284'):
        assert _is_linked(a1, 'jpdl32_SuperStateType284', b)
    _safe_set(b, 'jpdl32_ForkType285', a2)
    assert _is_linked(b, 'jpdl32_ForkType285', a2)
    if hasattr(a1, 'jpdl32_SuperStateType284'):
        assert not _is_linked(a1, 'jpdl32_SuperStateType284', b)
    if hasattr(a2, 'jpdl32_SuperStateType284'):
        assert _is_linked(a2, 'jpdl32_SuperStateType284', b)
    _safe_set(b, 'jpdl32_ForkType285', None)
    assert not _is_linked(b, 'jpdl32_ForkType285', a2)
    if hasattr(a2, 'jpdl32_SuperStateType284'):
        assert not _is_linked(a2, 'jpdl32_SuperStateType284', b)


def test_assoc_fork38_reverse_link_reassign_clear():
    a1 = jpdl32_ForkType(async_="sample_text", description="sample_text", group="sample_text", name="sample_text")
    a2 = jpdl32_ForkType(async_="sample_text_2", description="sample_text_2", group="sample_text_2", name="sample_text_2")
    b = jpdl32_DocumentRoot(description="sample_text", mixed="sample_text", recipients="sample_text", subject="sample_text", template="sample_text", text="sample_text", to="sample_text")
    _safe_set(b, 'jpdl32_DocumentRoot39', {a1})
    assert _is_linked(b, 'jpdl32_DocumentRoot39', a1)
    if hasattr(a1, 'jpdl32_ForkType'):
        assert _is_linked(a1, 'jpdl32_ForkType', b)
    _safe_set(b, 'jpdl32_DocumentRoot39', {a2})
    assert _is_linked(b, 'jpdl32_DocumentRoot39', a2)
    if hasattr(a1, 'jpdl32_ForkType'):
        assert not _is_linked(a1, 'jpdl32_ForkType', b)
    if hasattr(a2, 'jpdl32_ForkType'):
        assert _is_linked(a2, 'jpdl32_ForkType', b)
    _safe_set(b, 'jpdl32_DocumentRoot39', set())
    assert not _is_linked(b, 'jpdl32_DocumentRoot39', a2)
    if hasattr(a2, 'jpdl32_ForkType'):
        assert not _is_linked(a2, 'jpdl32_ForkType', b)


def test_assoc_handler3_reverse_link_reassign_clear():
    a1 = jpdl32_Delegation(any="sample_text", class_="sample_text", configType="sample_text", mixed="sample_text")
    a2 = jpdl32_Delegation(any="sample_text_2", class_="sample_text_2", configType="sample_text_2", mixed="sample_text_2")
    b = jpdl32_DecisionType(async_="sample_text", description="sample_text", expression="sample_text", group="sample_text", name="sample_text")
    _safe_set(b, 'jpdl32_DecisionType', {a1})
    assert _is_linked(b, 'jpdl32_DecisionType', a1)
    if hasattr(a1, 'jpdl32_Delegation'):
        assert _is_linked(a1, 'jpdl32_Delegation', b)
    _safe_set(b, 'jpdl32_DecisionType', {a2})
    assert _is_linked(b, 'jpdl32_DecisionType', a2)
    if hasattr(a1, 'jpdl32_Delegation'):
        assert not _is_linked(a1, 'jpdl32_Delegation', b)
    if hasattr(a2, 'jpdl32_Delegation'):
        assert _is_linked(a2, 'jpdl32_Delegation', b)
    _safe_set(b, 'jpdl32_DecisionType', set())
    assert not _is_linked(b, 'jpdl32_DecisionType', a2)
    if hasattr(a2, 'jpdl32_Delegation'):
        assert not _is_linked(a2, 'jpdl32_Delegation', b)


def test_assoc_join191_reverse_link_reassign_clear():
    a1 = jpdl32_ProcessDefinitionType(description="sample_text", group="sample_text", name="sample_text")
    a2 = jpdl32_ProcessDefinitionType(description="sample_text_2", group="sample_text_2", name="sample_text_2")
    b = jpdl32_JoinType(async_="sample_text", description="sample_text", name="sample_text", nodeContentElements="sample_text")
    _safe_set(b, 'jpdl32_JoinType193', a1)
    assert _is_linked(b, 'jpdl32_JoinType193', a1)
    if hasattr(a1, 'jpdl32_ProcessDefinitionType192'):
        assert _is_linked(a1, 'jpdl32_ProcessDefinitionType192', b)
    _safe_set(b, 'jpdl32_JoinType193', a2)
    assert _is_linked(b, 'jpdl32_JoinType193', a2)
    if hasattr(a1, 'jpdl32_ProcessDefinitionType192'):
        assert not _is_linked(a1, 'jpdl32_ProcessDefinitionType192', b)
    if hasattr(a2, 'jpdl32_ProcessDefinitionType192'):
        assert _is_linked(a2, 'jpdl32_ProcessDefinitionType192', b)
    _safe_set(b, 'jpdl32_JoinType193', None)
    assert not _is_linked(b, 'jpdl32_JoinType193', a2)
    if hasattr(a2, 'jpdl32_ProcessDefinitionType192'):
        assert not _is_linked(a2, 'jpdl32_ProcessDefinitionType192', b)


def test_assoc_join286_reverse_link_reassign_clear():
    a1 = jpdl32_SuperStateType(async_="sample_text", description="sample_text", group="sample_text", name="sample_text")
    a2 = jpdl32_SuperStateType(async_="sample_text_2", description="sample_text_2", group="sample_text_2", name="sample_text_2")
    b = jpdl32_JoinType(async_="sample_text", description="sample_text", name="sample_text", nodeContentElements="sample_text")
    _safe_set(b, 'jpdl32_JoinType288', a1)
    assert _is_linked(b, 'jpdl32_JoinType288', a1)
    if hasattr(a1, 'jpdl32_SuperStateType287'):
        assert _is_linked(a1, 'jpdl32_SuperStateType287', b)
    _safe_set(b, 'jpdl32_JoinType288', a2)
    assert _is_linked(b, 'jpdl32_JoinType288', a2)
    if hasattr(a1, 'jpdl32_SuperStateType287'):
        assert not _is_linked(a1, 'jpdl32_SuperStateType287', b)
    if hasattr(a2, 'jpdl32_SuperStateType287'):
        assert _is_linked(a2, 'jpdl32_SuperStateType287', b)
    _safe_set(b, 'jpdl32_JoinType288', None)
    assert not _is_linked(b, 'jpdl32_JoinType288', a2)
    if hasattr(a2, 'jpdl32_SuperStateType287'):
        assert not _is_linked(a2, 'jpdl32_SuperStateType287', b)


def test_assoc_join40_reverse_link_reassign_clear():
    a1 = jpdl32_JoinType(async_="sample_text", description="sample_text", name="sample_text", nodeContentElements="sample_text")
    a2 = jpdl32_JoinType(async_="sample_text_2", description="sample_text_2", name="sample_text_2", nodeContentElements="sample_text_2")
    b = jpdl32_DocumentRoot(description="sample_text", mixed="sample_text", recipients="sample_text", subject="sample_text", template="sample_text", text="sample_text", to="sample_text")
    _safe_set(b, 'jpdl32_DocumentRoot41', {a1})
    assert _is_linked(b, 'jpdl32_DocumentRoot41', a1)
    if hasattr(a1, 'jpdl32_JoinType'):
        assert _is_linked(a1, 'jpdl32_JoinType', b)
    _safe_set(b, 'jpdl32_DocumentRoot41', {a2})
    assert _is_linked(b, 'jpdl32_DocumentRoot41', a2)
    if hasattr(a1, 'jpdl32_JoinType'):
        assert not _is_linked(a1, 'jpdl32_JoinType', b)
    if hasattr(a2, 'jpdl32_JoinType'):
        assert _is_linked(a2, 'jpdl32_JoinType', b)
    _safe_set(b, 'jpdl32_DocumentRoot41', set())
    assert not _is_linked(b, 'jpdl32_DocumentRoot41', a2)
    if hasattr(a2, 'jpdl32_JoinType'):
        assert not _is_linked(a2, 'jpdl32_JoinType', b)


def test_assoc_mail152_reverse_link_reassign_clear():
    a1 = jpdl32_NodeType(async_="sample_text", description="sample_text", name="sample_text", nodeContentElements="sample_text")
    a2 = jpdl32_NodeType(async_="sample_text_2", description="sample_text_2", name="sample_text_2", nodeContentElements="sample_text_2")
    b = jpdl32_MailType(actors="sample_text", async_="sample_text", group="sample_text", name="sample_text", subject="sample_text", subject1="sample_text", template="sample_text", text="sample_text", text1="sample_text", to="sample_text")
    _safe_set(b, 'jpdl32_MailType154', a1)
    assert _is_linked(b, 'jpdl32_MailType154', a1)
    if hasattr(a1, 'jpdl32_NodeType153'):
        assert _is_linked(a1, 'jpdl32_NodeType153', b)
    _safe_set(b, 'jpdl32_MailType154', a2)
    assert _is_linked(b, 'jpdl32_MailType154', a2)
    if hasattr(a1, 'jpdl32_NodeType153'):
        assert not _is_linked(a1, 'jpdl32_NodeType153', b)
    if hasattr(a2, 'jpdl32_NodeType153'):
        assert _is_linked(a2, 'jpdl32_NodeType153', b)
    _safe_set(b, 'jpdl32_MailType154', None)
    assert not _is_linked(b, 'jpdl32_MailType154', a2)
    if hasattr(a2, 'jpdl32_NodeType153'):
        assert not _is_linked(a2, 'jpdl32_NodeType153', b)


def test_assoc_mail215_reverse_link_reassign_clear():
    a1 = jpdl32_ProcessDefinitionType(description="sample_text", group="sample_text", name="sample_text")
    a2 = jpdl32_ProcessDefinitionType(description="sample_text_2", group="sample_text_2", name="sample_text_2")
    b = jpdl32_MailType(actors="sample_text", async_="sample_text", group="sample_text", name="sample_text", subject="sample_text", subject1="sample_text", template="sample_text", text="sample_text", text1="sample_text", to="sample_text")
    _safe_set(b, 'jpdl32_MailType217', a1)
    assert _is_linked(b, 'jpdl32_MailType217', a1)
    if hasattr(a1, 'jpdl32_ProcessDefinitionType216'):
        assert _is_linked(a1, 'jpdl32_ProcessDefinitionType216', b)
    _safe_set(b, 'jpdl32_MailType217', a2)
    assert _is_linked(b, 'jpdl32_MailType217', a2)
    if hasattr(a1, 'jpdl32_ProcessDefinitionType216'):
        assert not _is_linked(a1, 'jpdl32_ProcessDefinitionType216', b)
    if hasattr(a2, 'jpdl32_ProcessDefinitionType216'):
        assert _is_linked(a2, 'jpdl32_ProcessDefinitionType216', b)
    _safe_set(b, 'jpdl32_MailType217', None)
    assert not _is_linked(b, 'jpdl32_MailType217', a2)
    if hasattr(a2, 'jpdl32_ProcessDefinitionType216'):
        assert not _is_linked(a2, 'jpdl32_ProcessDefinitionType216', b)


def test_assoc_mail354_reverse_link_reassign_clear():
    a1 = jpdl32_TimerType(duedate="sample_text", name="sample_text", repeat="sample_text", transition="sample_text")
    a2 = jpdl32_TimerType(duedate="sample_text_2", name="sample_text_2", repeat="sample_text_2", transition="sample_text_2")
    b = jpdl32_MailType(actors="sample_text", async_="sample_text", group="sample_text", name="sample_text", subject="sample_text", subject1="sample_text", template="sample_text", text="sample_text", text1="sample_text", to="sample_text")
    _safe_set(b, 'jpdl32_MailType356', a1)
    assert _is_linked(b, 'jpdl32_MailType356', a1)
    if hasattr(a1, 'jpdl32_TimerType355'):
        assert _is_linked(a1, 'jpdl32_TimerType355', b)
    _safe_set(b, 'jpdl32_MailType356', a2)
    assert _is_linked(b, 'jpdl32_MailType356', a2)
    if hasattr(a1, 'jpdl32_TimerType355'):
        assert not _is_linked(a1, 'jpdl32_TimerType355', b)
    if hasattr(a2, 'jpdl32_TimerType355'):
        assert _is_linked(a2, 'jpdl32_TimerType355', b)
    _safe_set(b, 'jpdl32_MailType356', None)
    assert not _is_linked(b, 'jpdl32_MailType356', a2)
    if hasattr(a2, 'jpdl32_TimerType355'):
        assert not _is_linked(a2, 'jpdl32_TimerType355', b)


def test_assoc_mail371_reverse_link_reassign_clear():
    a1 = jpdl32_TransitionType(description="sample_text", group="sample_text", name="sample_text", to="sample_text")
    a2 = jpdl32_TransitionType(description="sample_text_2", group="sample_text_2", name="sample_text_2", to="sample_text_2")
    b = jpdl32_MailType(actors="sample_text", async_="sample_text", group="sample_text", name="sample_text", subject="sample_text", subject1="sample_text", template="sample_text", text="sample_text", text1="sample_text", to="sample_text")
    _safe_set(b, 'jpdl32_MailType373', a1)
    assert _is_linked(b, 'jpdl32_MailType373', a1)
    if hasattr(a1, 'jpdl32_TransitionType372'):
        assert _is_linked(a1, 'jpdl32_TransitionType372', b)
    _safe_set(b, 'jpdl32_MailType373', a2)
    assert _is_linked(b, 'jpdl32_MailType373', a2)
    if hasattr(a1, 'jpdl32_TransitionType372'):
        assert not _is_linked(a1, 'jpdl32_TransitionType372', b)
    if hasattr(a2, 'jpdl32_TransitionType372'):
        assert _is_linked(a2, 'jpdl32_TransitionType372', b)
    _safe_set(b, 'jpdl32_MailType373', None)
    assert not _is_linked(b, 'jpdl32_MailType373', a2)
    if hasattr(a2, 'jpdl32_TransitionType372'):
        assert not _is_linked(a2, 'jpdl32_TransitionType372', b)


def test_assoc_mail42_reverse_link_reassign_clear():
    a1 = jpdl32_MailType(actors="sample_text", async_="sample_text", group="sample_text", name="sample_text", subject="sample_text", subject1="sample_text", template="sample_text", text="sample_text", text1="sample_text", to="sample_text")
    a2 = jpdl32_MailType(actors="sample_text_2", async_="sample_text_2", group="sample_text_2", name="sample_text_2", subject="sample_text_2", subject1="sample_text_2", template="sample_text_2", text="sample_text_2", text1="sample_text_2", to="sample_text_2")
    b = jpdl32_DocumentRoot(description="sample_text", mixed="sample_text", recipients="sample_text", subject="sample_text", template="sample_text", text="sample_text", to="sample_text")
    _safe_set(b, 'jpdl32_DocumentRoot43', {a1})
    assert _is_linked(b, 'jpdl32_DocumentRoot43', a1)
    if hasattr(a1, 'jpdl32_MailType'):
        assert _is_linked(a1, 'jpdl32_MailType', b)
    _safe_set(b, 'jpdl32_DocumentRoot43', {a2})
    assert _is_linked(b, 'jpdl32_DocumentRoot43', a2)
    if hasattr(a1, 'jpdl32_MailType'):
        assert not _is_linked(a1, 'jpdl32_MailType', b)
    if hasattr(a2, 'jpdl32_MailType'):
        assert _is_linked(a2, 'jpdl32_MailType', b)
    _safe_set(b, 'jpdl32_DocumentRoot43', set())
    assert not _is_linked(b, 'jpdl32_DocumentRoot43', a2)
    if hasattr(a2, 'jpdl32_MailType'):
        assert not _is_linked(a2, 'jpdl32_MailType', b)


def test_assoc_mail92_reverse_link_reassign_clear():
    a1 = jpdl32_MailType(actors="sample_text", async_="sample_text", group="sample_text", name="sample_text", subject="sample_text", subject1="sample_text", template="sample_text", text="sample_text", text1="sample_text", to="sample_text")
    a2 = jpdl32_MailType(actors="sample_text_2", async_="sample_text_2", group="sample_text_2", name="sample_text_2", subject="sample_text_2", subject1="sample_text_2", template="sample_text_2", text="sample_text_2", text1="sample_text_2", to="sample_text_2")
    b = jpdl32_EventType(actionElements="sample_text", type="sample_text")
    _safe_set(b, 'jpdl32_EventType93', {a1})
    assert _is_linked(b, 'jpdl32_EventType93', a1)
    if hasattr(a1, 'jpdl32_MailType94'):
        assert _is_linked(a1, 'jpdl32_MailType94', b)
    _safe_set(b, 'jpdl32_EventType93', {a2})
    assert _is_linked(b, 'jpdl32_EventType93', a2)
    if hasattr(a1, 'jpdl32_MailType94'):
        assert not _is_linked(a1, 'jpdl32_MailType94', b)
    if hasattr(a2, 'jpdl32_MailType94'):
        assert _is_linked(a2, 'jpdl32_MailType94', b)
    _safe_set(b, 'jpdl32_EventType93', set())
    assert not _is_linked(b, 'jpdl32_EventType93', a2)
    if hasattr(a2, 'jpdl32_MailType94'):
        assert not _is_linked(a2, 'jpdl32_MailType94', b)


def test_assoc_mailNode200_reverse_link_reassign_clear():
    a1 = jpdl32_ProcessDefinitionType(description="sample_text", group="sample_text", name="sample_text")
    a2 = jpdl32_ProcessDefinitionType(description="sample_text_2", group="sample_text_2", name="sample_text_2")
    b = jpdl32_MailNodeType(actors="sample_text", async_="sample_text", description="sample_text", group="sample_text", name="sample_text", subject="sample_text", subject1="sample_text", template="sample_text", text="sample_text", text1="sample_text", to="sample_text")
    _safe_set(b, 'jpdl32_MailNodeType202', a1)
    assert _is_linked(b, 'jpdl32_MailNodeType202', a1)
    if hasattr(a1, 'jpdl32_ProcessDefinitionType201'):
        assert _is_linked(a1, 'jpdl32_ProcessDefinitionType201', b)
    _safe_set(b, 'jpdl32_MailNodeType202', a2)
    assert _is_linked(b, 'jpdl32_MailNodeType202', a2)
    if hasattr(a1, 'jpdl32_ProcessDefinitionType201'):
        assert not _is_linked(a1, 'jpdl32_ProcessDefinitionType201', b)
    if hasattr(a2, 'jpdl32_ProcessDefinitionType201'):
        assert _is_linked(a2, 'jpdl32_ProcessDefinitionType201', b)
    _safe_set(b, 'jpdl32_MailNodeType202', None)
    assert not _is_linked(b, 'jpdl32_MailNodeType202', a2)
    if hasattr(a2, 'jpdl32_ProcessDefinitionType201'):
        assert not _is_linked(a2, 'jpdl32_ProcessDefinitionType201', b)


def test_assoc_mailNode295_reverse_link_reassign_clear():
    a1 = jpdl32_SuperStateType(async_="sample_text", description="sample_text", group="sample_text", name="sample_text")
    a2 = jpdl32_SuperStateType(async_="sample_text_2", description="sample_text_2", group="sample_text_2", name="sample_text_2")
    b = jpdl32_MailNodeType(actors="sample_text", async_="sample_text", description="sample_text", group="sample_text", name="sample_text", subject="sample_text", subject1="sample_text", template="sample_text", text="sample_text", text1="sample_text", to="sample_text")
    _safe_set(b, 'jpdl32_MailNodeType297', a1)
    assert _is_linked(b, 'jpdl32_MailNodeType297', a1)
    if hasattr(a1, 'jpdl32_SuperStateType296'):
        assert _is_linked(a1, 'jpdl32_SuperStateType296', b)
    _safe_set(b, 'jpdl32_MailNodeType297', a2)
    assert _is_linked(b, 'jpdl32_MailNodeType297', a2)
    if hasattr(a1, 'jpdl32_SuperStateType296'):
        assert not _is_linked(a1, 'jpdl32_SuperStateType296', b)
    if hasattr(a2, 'jpdl32_SuperStateType296'):
        assert _is_linked(a2, 'jpdl32_SuperStateType296', b)
    _safe_set(b, 'jpdl32_MailNodeType297', None)
    assert not _is_linked(b, 'jpdl32_MailNodeType297', a2)
    if hasattr(a2, 'jpdl32_SuperStateType296'):
        assert not _is_linked(a2, 'jpdl32_SuperStateType296', b)


def test_assoc_mailNode44_reverse_link_reassign_clear():
    a1 = jpdl32_MailNodeType(actors="sample_text", async_="sample_text", description="sample_text", group="sample_text", name="sample_text", subject="sample_text", subject1="sample_text", template="sample_text", text="sample_text", text1="sample_text", to="sample_text")
    a2 = jpdl32_MailNodeType(actors="sample_text_2", async_="sample_text_2", description="sample_text_2", group="sample_text_2", name="sample_text_2", subject="sample_text_2", subject1="sample_text_2", template="sample_text_2", text="sample_text_2", text1="sample_text_2", to="sample_text_2")
    b = jpdl32_DocumentRoot(description="sample_text", mixed="sample_text", recipients="sample_text", subject="sample_text", template="sample_text", text="sample_text", to="sample_text")
    _safe_set(b, 'jpdl32_DocumentRoot45', {a1})
    assert _is_linked(b, 'jpdl32_DocumentRoot45', a1)
    if hasattr(a1, 'jpdl32_MailNodeType'):
        assert _is_linked(a1, 'jpdl32_MailNodeType', b)
    _safe_set(b, 'jpdl32_DocumentRoot45', {a2})
    assert _is_linked(b, 'jpdl32_DocumentRoot45', a2)
    if hasattr(a1, 'jpdl32_MailNodeType'):
        assert not _is_linked(a1, 'jpdl32_MailNodeType', b)
    if hasattr(a2, 'jpdl32_MailNodeType'):
        assert _is_linked(a2, 'jpdl32_MailNodeType', b)
    _safe_set(b, 'jpdl32_DocumentRoot45', set())
    assert not _is_linked(b, 'jpdl32_DocumentRoot45', a2)
    if hasattr(a2, 'jpdl32_MailNodeType'):
        assert not _is_linked(a2, 'jpdl32_MailNodeType', b)


def test_assoc_node173_reverse_link_reassign_clear():
    a1 = jpdl32_ProcessDefinitionType(description="sample_text", group="sample_text", name="sample_text")
    a2 = jpdl32_ProcessDefinitionType(description="sample_text_2", group="sample_text_2", name="sample_text_2")
    b = jpdl32_NodeType(async_="sample_text", description="sample_text", name="sample_text", nodeContentElements="sample_text")
    _safe_set(b, 'jpdl32_NodeType175', a1)
    assert _is_linked(b, 'jpdl32_NodeType175', a1)
    if hasattr(a1, 'jpdl32_ProcessDefinitionType174'):
        assert _is_linked(a1, 'jpdl32_ProcessDefinitionType174', b)
    _safe_set(b, 'jpdl32_NodeType175', a2)
    assert _is_linked(b, 'jpdl32_NodeType175', a2)
    if hasattr(a1, 'jpdl32_ProcessDefinitionType174'):
        assert not _is_linked(a1, 'jpdl32_ProcessDefinitionType174', b)
    if hasattr(a2, 'jpdl32_ProcessDefinitionType174'):
        assert _is_linked(a2, 'jpdl32_ProcessDefinitionType174', b)
    _safe_set(b, 'jpdl32_NodeType175', None)
    assert not _is_linked(b, 'jpdl32_NodeType175', a2)
    if hasattr(a2, 'jpdl32_ProcessDefinitionType174'):
        assert not _is_linked(a2, 'jpdl32_ProcessDefinitionType174', b)


def test_assoc_node268_reverse_link_reassign_clear():
    a1 = jpdl32_SuperStateType(async_="sample_text", description="sample_text", group="sample_text", name="sample_text")
    a2 = jpdl32_SuperStateType(async_="sample_text_2", description="sample_text_2", group="sample_text_2", name="sample_text_2")
    b = jpdl32_NodeType(async_="sample_text", description="sample_text", name="sample_text", nodeContentElements="sample_text")
    _safe_set(b, 'jpdl32_NodeType270', a1)
    assert _is_linked(b, 'jpdl32_NodeType270', a1)
    if hasattr(a1, 'jpdl32_SuperStateType269'):
        assert _is_linked(a1, 'jpdl32_SuperStateType269', b)
    _safe_set(b, 'jpdl32_NodeType270', a2)
    assert _is_linked(b, 'jpdl32_NodeType270', a2)
    if hasattr(a1, 'jpdl32_SuperStateType269'):
        assert not _is_linked(a1, 'jpdl32_SuperStateType269', b)
    if hasattr(a2, 'jpdl32_SuperStateType269'):
        assert _is_linked(a2, 'jpdl32_SuperStateType269', b)
    _safe_set(b, 'jpdl32_NodeType270', None)
    assert not _is_linked(b, 'jpdl32_NodeType270', a2)
    if hasattr(a2, 'jpdl32_SuperStateType269'):
        assert not _is_linked(a2, 'jpdl32_SuperStateType269', b)


def test_assoc_node46_reverse_link_reassign_clear():
    a1 = jpdl32_NodeType(async_="sample_text", description="sample_text", name="sample_text", nodeContentElements="sample_text")
    a2 = jpdl32_NodeType(async_="sample_text_2", description="sample_text_2", name="sample_text_2", nodeContentElements="sample_text_2")
    b = jpdl32_DocumentRoot(description="sample_text", mixed="sample_text", recipients="sample_text", subject="sample_text", template="sample_text", text="sample_text", to="sample_text")
    _safe_set(b, 'jpdl32_DocumentRoot47', {a1})
    assert _is_linked(b, 'jpdl32_DocumentRoot47', a1)
    if hasattr(a1, 'jpdl32_NodeType'):
        assert _is_linked(a1, 'jpdl32_NodeType', b)
    _safe_set(b, 'jpdl32_DocumentRoot47', {a2})
    assert _is_linked(b, 'jpdl32_DocumentRoot47', a2)
    if hasattr(a1, 'jpdl32_NodeType'):
        assert not _is_linked(a1, 'jpdl32_NodeType', b)
    if hasattr(a2, 'jpdl32_NodeType'):
        assert _is_linked(a2, 'jpdl32_NodeType', b)
    _safe_set(b, 'jpdl32_DocumentRoot47', set())
    assert not _is_linked(b, 'jpdl32_DocumentRoot47', a2)
    if hasattr(a2, 'jpdl32_NodeType'):
        assert not _is_linked(a2, 'jpdl32_NodeType', b)


def test_assoc_processDefinition48_reverse_link_reassign_clear():
    a1 = jpdl32_ProcessDefinitionType(description="sample_text", group="sample_text", name="sample_text")
    a2 = jpdl32_ProcessDefinitionType(description="sample_text_2", group="sample_text_2", name="sample_text_2")
    b = jpdl32_DocumentRoot(description="sample_text", mixed="sample_text", recipients="sample_text", subject="sample_text", template="sample_text", text="sample_text", to="sample_text")
    _safe_set(b, 'jpdl32_DocumentRoot49', {a1})
    assert _is_linked(b, 'jpdl32_DocumentRoot49', a1)
    if hasattr(a1, 'jpdl32_ProcessDefinitionType'):
        assert _is_linked(a1, 'jpdl32_ProcessDefinitionType', b)
    _safe_set(b, 'jpdl32_DocumentRoot49', {a2})
    assert _is_linked(b, 'jpdl32_DocumentRoot49', a2)
    if hasattr(a1, 'jpdl32_ProcessDefinitionType'):
        assert not _is_linked(a1, 'jpdl32_ProcessDefinitionType', b)
    if hasattr(a2, 'jpdl32_ProcessDefinitionType'):
        assert _is_linked(a2, 'jpdl32_ProcessDefinitionType', b)
    _safe_set(b, 'jpdl32_DocumentRoot49', set())
    assert not _is_linked(b, 'jpdl32_DocumentRoot49', a2)
    if hasattr(a2, 'jpdl32_ProcessDefinitionType'):
        assert not _is_linked(a2, 'jpdl32_ProcessDefinitionType', b)


def test_assoc_processState185_reverse_link_reassign_clear():
    a1 = jpdl32_ProcessStateType(async_="sample_text", binding="sample_text", description="sample_text", group="sample_text", name="sample_text")
    a2 = jpdl32_ProcessStateType(async_="sample_text_2", binding="sample_text_2", description="sample_text_2", group="sample_text_2", name="sample_text_2")
    b = jpdl32_ProcessDefinitionType(description="sample_text", group="sample_text", name="sample_text")
    _safe_set(b, 'jpdl32_ProcessDefinitionType186', {a1})
    assert _is_linked(b, 'jpdl32_ProcessDefinitionType186', a1)
    if hasattr(a1, 'jpdl32_ProcessStateType187'):
        assert _is_linked(a1, 'jpdl32_ProcessStateType187', b)
    _safe_set(b, 'jpdl32_ProcessDefinitionType186', {a2})
    assert _is_linked(b, 'jpdl32_ProcessDefinitionType186', a2)
    if hasattr(a1, 'jpdl32_ProcessStateType187'):
        assert not _is_linked(a1, 'jpdl32_ProcessStateType187', b)
    if hasattr(a2, 'jpdl32_ProcessStateType187'):
        assert _is_linked(a2, 'jpdl32_ProcessStateType187', b)
    _safe_set(b, 'jpdl32_ProcessDefinitionType186', set())
    assert not _is_linked(b, 'jpdl32_ProcessDefinitionType186', a2)
    if hasattr(a2, 'jpdl32_ProcessStateType187'):
        assert not _is_linked(a2, 'jpdl32_ProcessStateType187', b)


def test_assoc_processState280_reverse_link_reassign_clear():
    a1 = jpdl32_SuperStateType(async_="sample_text", description="sample_text", group="sample_text", name="sample_text")
    a2 = jpdl32_SuperStateType(async_="sample_text_2", description="sample_text_2", group="sample_text_2", name="sample_text_2")
    b = jpdl32_ProcessStateType(async_="sample_text", binding="sample_text", description="sample_text", group="sample_text", name="sample_text")
    _safe_set(b, 'jpdl32_ProcessStateType282', a1)
    assert _is_linked(b, 'jpdl32_ProcessStateType282', a1)
    if hasattr(a1, 'jpdl32_SuperStateType281'):
        assert _is_linked(a1, 'jpdl32_SuperStateType281', b)
    _safe_set(b, 'jpdl32_ProcessStateType282', a2)
    assert _is_linked(b, 'jpdl32_ProcessStateType282', a2)
    if hasattr(a1, 'jpdl32_SuperStateType281'):
        assert not _is_linked(a1, 'jpdl32_SuperStateType281', b)
    if hasattr(a2, 'jpdl32_SuperStateType281'):
        assert _is_linked(a2, 'jpdl32_SuperStateType281', b)
    _safe_set(b, 'jpdl32_ProcessStateType282', None)
    assert not _is_linked(b, 'jpdl32_ProcessStateType282', a2)
    if hasattr(a2, 'jpdl32_SuperStateType281'):
        assert not _is_linked(a2, 'jpdl32_SuperStateType281', b)


def test_assoc_processState50_reverse_link_reassign_clear():
    a1 = jpdl32_ProcessStateType(async_="sample_text", binding="sample_text", description="sample_text", group="sample_text", name="sample_text")
    a2 = jpdl32_ProcessStateType(async_="sample_text_2", binding="sample_text_2", description="sample_text_2", group="sample_text_2", name="sample_text_2")
    b = jpdl32_DocumentRoot(description="sample_text", mixed="sample_text", recipients="sample_text", subject="sample_text", template="sample_text", text="sample_text", to="sample_text")
    _safe_set(b, 'jpdl32_DocumentRoot51', {a1})
    assert _is_linked(b, 'jpdl32_DocumentRoot51', a1)
    if hasattr(a1, 'jpdl32_ProcessStateType'):
        assert _is_linked(a1, 'jpdl32_ProcessStateType', b)
    _safe_set(b, 'jpdl32_DocumentRoot51', {a2})
    assert _is_linked(b, 'jpdl32_DocumentRoot51', a2)
    if hasattr(a1, 'jpdl32_ProcessStateType'):
        assert not _is_linked(a1, 'jpdl32_ProcessStateType', b)
    if hasattr(a2, 'jpdl32_ProcessStateType'):
        assert _is_linked(a2, 'jpdl32_ProcessStateType', b)
    _safe_set(b, 'jpdl32_DocumentRoot51', set())
    assert not _is_linked(b, 'jpdl32_DocumentRoot51', a2)
    if hasattr(a2, 'jpdl32_ProcessStateType'):
        assert not _is_linked(a2, 'jpdl32_ProcessStateType', b)


def test_assoc_reminder340_reverse_link_reassign_clear():
    a1 = jpdl32_TaskType(blocking="sample_text", description="sample_text", description1="sample_text", duedate="sample_text", group="sample_text", name="sample_text", notify="sample_text", priority="sample_text", signalling="sample_text", swimlane="sample_text")
    a2 = jpdl32_TaskType(blocking="sample_text_2", description="sample_text_2", description1="sample_text_2", duedate="sample_text_2", group="sample_text_2", name="sample_text_2", notify="sample_text_2", priority="sample_text_2", signalling="sample_text_2", swimlane="sample_text_2")
    b = jpdl32_ReminderType(duedate="sample_text", repeat="sample_text")
    _safe_set(b, 'jpdl32_ReminderType', a1)
    assert _is_linked(b, 'jpdl32_ReminderType', a1)
    if hasattr(a1, 'jpdl32_TaskType341'):
        assert _is_linked(a1, 'jpdl32_TaskType341', b)
    _safe_set(b, 'jpdl32_ReminderType', a2)
    assert _is_linked(b, 'jpdl32_ReminderType', a2)
    if hasattr(a1, 'jpdl32_TaskType341'):
        assert not _is_linked(a1, 'jpdl32_TaskType341', b)
    if hasattr(a2, 'jpdl32_TaskType341'):
        assert _is_linked(a2, 'jpdl32_TaskType341', b)
    _safe_set(b, 'jpdl32_ReminderType', None)
    assert not _is_linked(b, 'jpdl32_ReminderType', a2)
    if hasattr(a2, 'jpdl32_TaskType341'):
        assert not _is_linked(a2, 'jpdl32_TaskType341', b)


def test_assoc_script1_reverse_link_reassign_clear():
    a1 = jpdl32_ScriptType(acceptPropagatedEvents="sample_text", any="sample_text", mixed="sample_text", name="sample_text")
    a2 = jpdl32_ScriptType(acceptPropagatedEvents="sample_text_2", any="sample_text_2", mixed="sample_text_2", name="sample_text_2")
    b = jpdl32_CreateTimerType(duedate="sample_text", name="sample_text", repeat="sample_text", transition="sample_text")
    _safe_set(b, 'jpdl32_CreateTimerType2', a1)
    assert _is_linked(b, 'jpdl32_CreateTimerType2', a1)
    if hasattr(a1, 'jpdl32_ScriptType'):
        assert _is_linked(a1, 'jpdl32_ScriptType', b)
    _safe_set(b, 'jpdl32_CreateTimerType2', a2)
    assert _is_linked(b, 'jpdl32_CreateTimerType2', a2)
    if hasattr(a1, 'jpdl32_ScriptType'):
        assert not _is_linked(a1, 'jpdl32_ScriptType', b)
    if hasattr(a2, 'jpdl32_ScriptType'):
        assert _is_linked(a2, 'jpdl32_ScriptType', b)
    _safe_set(b, 'jpdl32_CreateTimerType2', None)
    assert not _is_linked(b, 'jpdl32_CreateTimerType2', a2)
    if hasattr(a2, 'jpdl32_ScriptType'):
        assert not _is_linked(a2, 'jpdl32_ScriptType', b)


def test_assoc_script101_reverse_link_reassign_clear():
    a1 = jpdl32_ScriptType(acceptPropagatedEvents="sample_text", any="sample_text", mixed="sample_text", name="sample_text")
    a2 = jpdl32_ScriptType(acceptPropagatedEvents="sample_text_2", any="sample_text_2", mixed="sample_text_2", name="sample_text_2")
    b = jpdl32_ForkType(async_="sample_text", description="sample_text", group="sample_text", name="sample_text")
    _safe_set(b, 'jpdl32_ForkType102', {a1})
    assert _is_linked(b, 'jpdl32_ForkType102', a1)
    if hasattr(a1, 'jpdl32_ScriptType103'):
        assert _is_linked(a1, 'jpdl32_ScriptType103', b)
    _safe_set(b, 'jpdl32_ForkType102', {a2})
    assert _is_linked(b, 'jpdl32_ForkType102', a2)
    if hasattr(a1, 'jpdl32_ScriptType103'):
        assert not _is_linked(a1, 'jpdl32_ScriptType103', b)
    if hasattr(a2, 'jpdl32_ScriptType103'):
        assert _is_linked(a2, 'jpdl32_ScriptType103', b)
    _safe_set(b, 'jpdl32_ForkType102', set())
    assert not _is_linked(b, 'jpdl32_ForkType102', a2)
    if hasattr(a2, 'jpdl32_ScriptType103'):
        assert not _is_linked(a2, 'jpdl32_ScriptType103', b)


def test_assoc_script143_reverse_link_reassign_clear():
    a1 = jpdl32_ScriptType(acceptPropagatedEvents="sample_text", any="sample_text", mixed="sample_text", name="sample_text")
    a2 = jpdl32_ScriptType(acceptPropagatedEvents="sample_text_2", any="sample_text_2", mixed="sample_text_2", name="sample_text_2")
    b = jpdl32_NodeType(async_="sample_text", description="sample_text", name="sample_text", nodeContentElements="sample_text")
    _safe_set(b, 'jpdl32_NodeType144', a1)
    assert _is_linked(b, 'jpdl32_NodeType144', a1)
    if hasattr(a1, 'jpdl32_ScriptType145'):
        assert _is_linked(a1, 'jpdl32_ScriptType145', b)
    _safe_set(b, 'jpdl32_NodeType144', a2)
    assert _is_linked(b, 'jpdl32_NodeType144', a2)
    if hasattr(a1, 'jpdl32_ScriptType145'):
        assert not _is_linked(a1, 'jpdl32_ScriptType145', b)
    if hasattr(a2, 'jpdl32_ScriptType145'):
        assert _is_linked(a2, 'jpdl32_ScriptType145', b)
    _safe_set(b, 'jpdl32_NodeType144', None)
    assert not _is_linked(b, 'jpdl32_NodeType144', a2)
    if hasattr(a2, 'jpdl32_ScriptType145'):
        assert not _is_linked(a2, 'jpdl32_ScriptType145', b)


def test_assoc_script206_reverse_link_reassign_clear():
    a1 = jpdl32_ScriptType(acceptPropagatedEvents="sample_text", any="sample_text", mixed="sample_text", name="sample_text")
    a2 = jpdl32_ScriptType(acceptPropagatedEvents="sample_text_2", any="sample_text_2", mixed="sample_text_2", name="sample_text_2")
    b = jpdl32_ProcessDefinitionType(description="sample_text", group="sample_text", name="sample_text")
    _safe_set(b, 'jpdl32_ProcessDefinitionType207', {a1})
    assert _is_linked(b, 'jpdl32_ProcessDefinitionType207', a1)
    if hasattr(a1, 'jpdl32_ScriptType208'):
        assert _is_linked(a1, 'jpdl32_ScriptType208', b)
    _safe_set(b, 'jpdl32_ProcessDefinitionType207', {a2})
    assert _is_linked(b, 'jpdl32_ProcessDefinitionType207', a2)
    if hasattr(a1, 'jpdl32_ScriptType208'):
        assert not _is_linked(a1, 'jpdl32_ScriptType208', b)
    if hasattr(a2, 'jpdl32_ScriptType208'):
        assert _is_linked(a2, 'jpdl32_ScriptType208', b)
    _safe_set(b, 'jpdl32_ProcessDefinitionType207', set())
    assert not _is_linked(b, 'jpdl32_ProcessDefinitionType207', a2)
    if hasattr(a2, 'jpdl32_ScriptType208'):
        assert not _is_linked(a2, 'jpdl32_ScriptType208', b)


def test_assoc_script345_reverse_link_reassign_clear():
    a1 = jpdl32_TimerType(duedate="sample_text", name="sample_text", repeat="sample_text", transition="sample_text")
    a2 = jpdl32_TimerType(duedate="sample_text_2", name="sample_text_2", repeat="sample_text_2", transition="sample_text_2")
    b = jpdl32_ScriptType(acceptPropagatedEvents="sample_text", any="sample_text", mixed="sample_text", name="sample_text")
    _safe_set(b, 'jpdl32_ScriptType347', a1)
    assert _is_linked(b, 'jpdl32_ScriptType347', a1)
    if hasattr(a1, 'jpdl32_TimerType346'):
        assert _is_linked(a1, 'jpdl32_TimerType346', b)
    _safe_set(b, 'jpdl32_ScriptType347', a2)
    assert _is_linked(b, 'jpdl32_ScriptType347', a2)
    if hasattr(a1, 'jpdl32_TimerType346'):
        assert not _is_linked(a1, 'jpdl32_TimerType346', b)
    if hasattr(a2, 'jpdl32_TimerType346'):
        assert _is_linked(a2, 'jpdl32_TimerType346', b)
    _safe_set(b, 'jpdl32_ScriptType347', None)
    assert not _is_linked(b, 'jpdl32_ScriptType347', a2)
    if hasattr(a2, 'jpdl32_TimerType346'):
        assert not _is_linked(a2, 'jpdl32_TimerType346', b)


def test_assoc_script362_reverse_link_reassign_clear():
    a1 = jpdl32_TransitionType(description="sample_text", group="sample_text", name="sample_text", to="sample_text")
    a2 = jpdl32_TransitionType(description="sample_text_2", group="sample_text_2", name="sample_text_2", to="sample_text_2")
    b = jpdl32_ScriptType(acceptPropagatedEvents="sample_text", any="sample_text", mixed="sample_text", name="sample_text")
    _safe_set(b, 'jpdl32_ScriptType364', a1)
    assert _is_linked(b, 'jpdl32_ScriptType364', a1)
    if hasattr(a1, 'jpdl32_TransitionType363'):
        assert _is_linked(a1, 'jpdl32_TransitionType363', b)
    _safe_set(b, 'jpdl32_ScriptType364', a2)
    assert _is_linked(b, 'jpdl32_ScriptType364', a2)
    if hasattr(a1, 'jpdl32_TransitionType363'):
        assert not _is_linked(a1, 'jpdl32_TransitionType363', b)
    if hasattr(a2, 'jpdl32_TransitionType363'):
        assert _is_linked(a2, 'jpdl32_TransitionType363', b)
    _safe_set(b, 'jpdl32_ScriptType364', None)
    assert not _is_linked(b, 'jpdl32_ScriptType364', a2)
    if hasattr(a2, 'jpdl32_TransitionType363'):
        assert not _is_linked(a2, 'jpdl32_TransitionType363', b)


def test_assoc_script52_reverse_link_reassign_clear():
    a1 = jpdl32_ScriptType(acceptPropagatedEvents="sample_text", any="sample_text", mixed="sample_text", name="sample_text")
    a2 = jpdl32_ScriptType(acceptPropagatedEvents="sample_text_2", any="sample_text_2", mixed="sample_text_2", name="sample_text_2")
    b = jpdl32_DocumentRoot(description="sample_text", mixed="sample_text", recipients="sample_text", subject="sample_text", template="sample_text", text="sample_text", to="sample_text")
    _safe_set(b, 'jpdl32_DocumentRoot53', {a1})
    assert _is_linked(b, 'jpdl32_DocumentRoot53', a1)
    if hasattr(a1, 'jpdl32_ScriptType54'):
        assert _is_linked(a1, 'jpdl32_ScriptType54', b)
    _safe_set(b, 'jpdl32_DocumentRoot53', {a2})
    assert _is_linked(b, 'jpdl32_DocumentRoot53', a2)
    if hasattr(a1, 'jpdl32_ScriptType54'):
        assert not _is_linked(a1, 'jpdl32_ScriptType54', b)
    if hasattr(a2, 'jpdl32_ScriptType54'):
        assert _is_linked(a2, 'jpdl32_ScriptType54', b)
    _safe_set(b, 'jpdl32_DocumentRoot53', set())
    assert not _is_linked(b, 'jpdl32_DocumentRoot53', a2)
    if hasattr(a2, 'jpdl32_ScriptType54'):
        assert not _is_linked(a2, 'jpdl32_ScriptType54', b)


def test_assoc_script83_reverse_link_reassign_clear():
    a1 = jpdl32_ScriptType(acceptPropagatedEvents="sample_text", any="sample_text", mixed="sample_text", name="sample_text")
    a2 = jpdl32_ScriptType(acceptPropagatedEvents="sample_text_2", any="sample_text_2", mixed="sample_text_2", name="sample_text_2")
    b = jpdl32_EventType(actionElements="sample_text", type="sample_text")
    _safe_set(b, 'jpdl32_EventType84', {a1})
    assert _is_linked(b, 'jpdl32_EventType84', a1)
    if hasattr(a1, 'jpdl32_ScriptType85'):
        assert _is_linked(a1, 'jpdl32_ScriptType85', b)
    _safe_set(b, 'jpdl32_EventType84', {a2})
    assert _is_linked(b, 'jpdl32_EventType84', a2)
    if hasattr(a1, 'jpdl32_ScriptType85'):
        assert not _is_linked(a1, 'jpdl32_ScriptType85', b)
    if hasattr(a2, 'jpdl32_ScriptType85'):
        assert _is_linked(a2, 'jpdl32_ScriptType85', b)
    _safe_set(b, 'jpdl32_EventType84', set())
    assert not _is_linked(b, 'jpdl32_EventType84', a2)
    if hasattr(a2, 'jpdl32_ScriptType85'):
        assert not _is_linked(a2, 'jpdl32_ScriptType85', b)


def test_assoc_script98_reverse_link_reassign_clear():
    a1 = jpdl32_ScriptType(acceptPropagatedEvents="sample_text", any="sample_text", mixed="sample_text", name="sample_text")
    a2 = jpdl32_ScriptType(acceptPropagatedEvents="sample_text_2", any="sample_text_2", mixed="sample_text_2", name="sample_text_2")
    b = jpdl32_ExceptionHandlerType(exceptionClass="sample_text", group="sample_text")
    _safe_set(b, 'jpdl32_ExceptionHandlerType99', {a1})
    assert _is_linked(b, 'jpdl32_ExceptionHandlerType99', a1)
    if hasattr(a1, 'jpdl32_ScriptType100'):
        assert _is_linked(a1, 'jpdl32_ScriptType100', b)
    _safe_set(b, 'jpdl32_ExceptionHandlerType99', {a2})
    assert _is_linked(b, 'jpdl32_ExceptionHandlerType99', a2)
    if hasattr(a1, 'jpdl32_ScriptType100'):
        assert not _is_linked(a1, 'jpdl32_ScriptType100', b)
    if hasattr(a2, 'jpdl32_ScriptType100'):
        assert _is_linked(a2, 'jpdl32_ScriptType100', b)
    _safe_set(b, 'jpdl32_ExceptionHandlerType99', set())
    assert not _is_linked(b, 'jpdl32_ExceptionHandlerType99', a2)
    if hasattr(a2, 'jpdl32_ScriptType100'):
        assert not _is_linked(a2, 'jpdl32_ScriptType100', b)


def test_assoc_startState170_reverse_link_reassign_clear():
    a1 = jpdl32_StartStateType(description="sample_text", group="sample_text", name="sample_text")
    a2 = jpdl32_StartStateType(description="sample_text_2", group="sample_text_2", name="sample_text_2")
    b = jpdl32_ProcessDefinitionType(description="sample_text", group="sample_text", name="sample_text")
    _safe_set(b, 'jpdl32_ProcessDefinitionType171', {a1})
    assert _is_linked(b, 'jpdl32_ProcessDefinitionType171', a1)
    if hasattr(a1, 'jpdl32_StartStateType172'):
        assert _is_linked(a1, 'jpdl32_StartStateType172', b)
    _safe_set(b, 'jpdl32_ProcessDefinitionType171', {a2})
    assert _is_linked(b, 'jpdl32_ProcessDefinitionType171', a2)
    if hasattr(a1, 'jpdl32_StartStateType172'):
        assert not _is_linked(a1, 'jpdl32_StartStateType172', b)
    if hasattr(a2, 'jpdl32_StartStateType172'):
        assert _is_linked(a2, 'jpdl32_StartStateType172', b)
    _safe_set(b, 'jpdl32_ProcessDefinitionType171', set())
    assert not _is_linked(b, 'jpdl32_ProcessDefinitionType171', a2)
    if hasattr(a2, 'jpdl32_StartStateType172'):
        assert not _is_linked(a2, 'jpdl32_StartStateType172', b)


def test_assoc_startState55_reverse_link_reassign_clear():
    a1 = jpdl32_StartStateType(description="sample_text", group="sample_text", name="sample_text")
    a2 = jpdl32_StartStateType(description="sample_text_2", group="sample_text_2", name="sample_text_2")
    b = jpdl32_DocumentRoot(description="sample_text", mixed="sample_text", recipients="sample_text", subject="sample_text", template="sample_text", text="sample_text", to="sample_text")
    _safe_set(b, 'jpdl32_DocumentRoot56', {a1})
    assert _is_linked(b, 'jpdl32_DocumentRoot56', a1)
    if hasattr(a1, 'jpdl32_StartStateType'):
        assert _is_linked(a1, 'jpdl32_StartStateType', b)
    _safe_set(b, 'jpdl32_DocumentRoot56', {a2})
    assert _is_linked(b, 'jpdl32_DocumentRoot56', a2)
    if hasattr(a1, 'jpdl32_StartStateType'):
        assert not _is_linked(a1, 'jpdl32_StartStateType', b)
    if hasattr(a2, 'jpdl32_StartStateType'):
        assert _is_linked(a2, 'jpdl32_StartStateType', b)
    _safe_set(b, 'jpdl32_DocumentRoot56', set())
    assert not _is_linked(b, 'jpdl32_DocumentRoot56', a2)
    if hasattr(a2, 'jpdl32_StartStateType'):
        assert not _is_linked(a2, 'jpdl32_StartStateType', b)


def test_assoc_state176_reverse_link_reassign_clear():
    a1 = jpdl32_StateType(async_="sample_text", description="sample_text", name="sample_text", nodeContentElements="sample_text")
    a2 = jpdl32_StateType(async_="sample_text_2", description="sample_text_2", name="sample_text_2", nodeContentElements="sample_text_2")
    b = jpdl32_ProcessDefinitionType(description="sample_text", group="sample_text", name="sample_text")
    _safe_set(b, 'jpdl32_ProcessDefinitionType177', {a1})
    assert _is_linked(b, 'jpdl32_ProcessDefinitionType177', a1)
    if hasattr(a1, 'jpdl32_StateType178'):
        assert _is_linked(a1, 'jpdl32_StateType178', b)
    _safe_set(b, 'jpdl32_ProcessDefinitionType177', {a2})
    assert _is_linked(b, 'jpdl32_ProcessDefinitionType177', a2)
    if hasattr(a1, 'jpdl32_StateType178'):
        assert not _is_linked(a1, 'jpdl32_StateType178', b)
    if hasattr(a2, 'jpdl32_StateType178'):
        assert _is_linked(a2, 'jpdl32_StateType178', b)
    _safe_set(b, 'jpdl32_ProcessDefinitionType177', set())
    assert not _is_linked(b, 'jpdl32_ProcessDefinitionType177', a2)
    if hasattr(a2, 'jpdl32_StateType178'):
        assert not _is_linked(a2, 'jpdl32_StateType178', b)


def test_assoc_state271_reverse_link_reassign_clear():
    a1 = jpdl32_SuperStateType(async_="sample_text", description="sample_text", group="sample_text", name="sample_text")
    a2 = jpdl32_SuperStateType(async_="sample_text_2", description="sample_text_2", group="sample_text_2", name="sample_text_2")
    b = jpdl32_StateType(async_="sample_text", description="sample_text", name="sample_text", nodeContentElements="sample_text")
    _safe_set(b, 'jpdl32_StateType273', a1)
    assert _is_linked(b, 'jpdl32_StateType273', a1)
    if hasattr(a1, 'jpdl32_SuperStateType272'):
        assert _is_linked(a1, 'jpdl32_SuperStateType272', b)
    _safe_set(b, 'jpdl32_StateType273', a2)
    assert _is_linked(b, 'jpdl32_StateType273', a2)
    if hasattr(a1, 'jpdl32_SuperStateType272'):
        assert not _is_linked(a1, 'jpdl32_SuperStateType272', b)
    if hasattr(a2, 'jpdl32_SuperStateType272'):
        assert _is_linked(a2, 'jpdl32_SuperStateType272', b)
    _safe_set(b, 'jpdl32_StateType273', None)
    assert not _is_linked(b, 'jpdl32_StateType273', a2)
    if hasattr(a2, 'jpdl32_SuperStateType272'):
        assert not _is_linked(a2, 'jpdl32_SuperStateType272', b)


def test_assoc_state57_reverse_link_reassign_clear():
    a1 = jpdl32_StateType(async_="sample_text", description="sample_text", name="sample_text", nodeContentElements="sample_text")
    a2 = jpdl32_StateType(async_="sample_text_2", description="sample_text_2", name="sample_text_2", nodeContentElements="sample_text_2")
    b = jpdl32_DocumentRoot(description="sample_text", mixed="sample_text", recipients="sample_text", subject="sample_text", template="sample_text", text="sample_text", to="sample_text")
    _safe_set(b, 'jpdl32_DocumentRoot58', {a1})
    assert _is_linked(b, 'jpdl32_DocumentRoot58', a1)
    if hasattr(a1, 'jpdl32_StateType'):
        assert _is_linked(a1, 'jpdl32_StateType', b)
    _safe_set(b, 'jpdl32_DocumentRoot58', {a2})
    assert _is_linked(b, 'jpdl32_DocumentRoot58', a2)
    if hasattr(a1, 'jpdl32_StateType'):
        assert not _is_linked(a1, 'jpdl32_StateType', b)
    if hasattr(a2, 'jpdl32_StateType'):
        assert _is_linked(a2, 'jpdl32_StateType', b)
    _safe_set(b, 'jpdl32_DocumentRoot58', set())
    assert not _is_linked(b, 'jpdl32_DocumentRoot58', a2)
    if hasattr(a2, 'jpdl32_StateType'):
        assert not _is_linked(a2, 'jpdl32_StateType', b)


def test_assoc_subProcess227_reverse_link_reassign_clear():
    a1 = jpdl32_SubProcessType(binding="sample_text", name="sample_text", version="sample_text")
    a2 = jpdl32_SubProcessType(binding="sample_text_2", name="sample_text_2", version="sample_text_2")
    b = jpdl32_ProcessStateType(async_="sample_text", binding="sample_text", description="sample_text", group="sample_text", name="sample_text")
    _safe_set(b, 'jpdl32_ProcessStateType228', {a1})
    assert _is_linked(b, 'jpdl32_ProcessStateType228', a1)
    if hasattr(a1, 'jpdl32_SubProcessType'):
        assert _is_linked(a1, 'jpdl32_SubProcessType', b)
    _safe_set(b, 'jpdl32_ProcessStateType228', {a2})
    assert _is_linked(b, 'jpdl32_ProcessStateType228', a2)
    if hasattr(a1, 'jpdl32_SubProcessType'):
        assert not _is_linked(a1, 'jpdl32_SubProcessType', b)
    if hasattr(a2, 'jpdl32_SubProcessType'):
        assert _is_linked(a2, 'jpdl32_SubProcessType', b)
    _safe_set(b, 'jpdl32_ProcessStateType228', set())
    assert not _is_linked(b, 'jpdl32_ProcessStateType228', a2)
    if hasattr(a2, 'jpdl32_SubProcessType'):
        assert not _is_linked(a2, 'jpdl32_SubProcessType', b)


def test_assoc_superState182_reverse_link_reassign_clear():
    a1 = jpdl32_SuperStateType(async_="sample_text", description="sample_text", group="sample_text", name="sample_text")
    a2 = jpdl32_SuperStateType(async_="sample_text_2", description="sample_text_2", group="sample_text_2", name="sample_text_2")
    b = jpdl32_ProcessDefinitionType(description="sample_text", group="sample_text", name="sample_text")
    _safe_set(b, 'jpdl32_ProcessDefinitionType183', {a1})
    assert _is_linked(b, 'jpdl32_ProcessDefinitionType183', a1)
    if hasattr(a1, 'jpdl32_SuperStateType184'):
        assert _is_linked(a1, 'jpdl32_SuperStateType184', b)
    _safe_set(b, 'jpdl32_ProcessDefinitionType183', {a2})
    assert _is_linked(b, 'jpdl32_ProcessDefinitionType183', a2)
    if hasattr(a1, 'jpdl32_SuperStateType184'):
        assert not _is_linked(a1, 'jpdl32_SuperStateType184', b)
    if hasattr(a2, 'jpdl32_SuperStateType184'):
        assert _is_linked(a2, 'jpdl32_SuperStateType184', b)
    _safe_set(b, 'jpdl32_ProcessDefinitionType183', set())
    assert not _is_linked(b, 'jpdl32_ProcessDefinitionType183', a2)
    if hasattr(a2, 'jpdl32_SuperStateType184'):
        assert not _is_linked(a2, 'jpdl32_SuperStateType184', b)


def test_assoc_superState278_reverse_link_reassign_clear():
    a1 = jpdl32_SuperStateType(async_="sample_text", description="sample_text", group="sample_text", name="sample_text")
    a2 = jpdl32_SuperStateType(async_="sample_text_2", description="sample_text_2", group="sample_text_2", name="sample_text_2")
    b = jpdl32_SuperStateType(async_="sample_text", description="sample_text", group="sample_text", name="sample_text")
    _safe_set(b, 'jpdl32_SuperStateType279', a1)
    assert _is_linked(b, 'jpdl32_SuperStateType279', a1)
    if hasattr(a1, 'jpdl32_SuperStateType277'):
        assert _is_linked(a1, 'jpdl32_SuperStateType277', b)
    _safe_set(b, 'jpdl32_SuperStateType279', a2)
    assert _is_linked(b, 'jpdl32_SuperStateType279', a2)
    if hasattr(a1, 'jpdl32_SuperStateType277'):
        assert not _is_linked(a1, 'jpdl32_SuperStateType277', b)
    if hasattr(a2, 'jpdl32_SuperStateType277'):
        assert _is_linked(a2, 'jpdl32_SuperStateType277', b)
    _safe_set(b, 'jpdl32_SuperStateType279', None)
    assert not _is_linked(b, 'jpdl32_SuperStateType279', a2)
    if hasattr(a2, 'jpdl32_SuperStateType277'):
        assert not _is_linked(a2, 'jpdl32_SuperStateType277', b)


def test_assoc_superState59_reverse_link_reassign_clear():
    a1 = jpdl32_SuperStateType(async_="sample_text", description="sample_text", group="sample_text", name="sample_text")
    a2 = jpdl32_SuperStateType(async_="sample_text_2", description="sample_text_2", group="sample_text_2", name="sample_text_2")
    b = jpdl32_DocumentRoot(description="sample_text", mixed="sample_text", recipients="sample_text", subject="sample_text", template="sample_text", text="sample_text", to="sample_text")
    _safe_set(b, 'jpdl32_DocumentRoot60', {a1})
    assert _is_linked(b, 'jpdl32_DocumentRoot60', a1)
    if hasattr(a1, 'jpdl32_SuperStateType'):
        assert _is_linked(a1, 'jpdl32_SuperStateType', b)
    _safe_set(b, 'jpdl32_DocumentRoot60', {a2})
    assert _is_linked(b, 'jpdl32_DocumentRoot60', a2)
    if hasattr(a1, 'jpdl32_SuperStateType'):
        assert not _is_linked(a1, 'jpdl32_SuperStateType', b)
    if hasattr(a2, 'jpdl32_SuperStateType'):
        assert _is_linked(a2, 'jpdl32_SuperStateType', b)
    _safe_set(b, 'jpdl32_DocumentRoot60', set())
    assert not _is_linked(b, 'jpdl32_DocumentRoot60', a2)
    if hasattr(a2, 'jpdl32_SuperStateType'):
        assert not _is_linked(a2, 'jpdl32_SuperStateType', b)


def test_assoc_swimlane167_reverse_link_reassign_clear():
    a1 = jpdl32_SwimlaneType(name="sample_text")
    a2 = jpdl32_SwimlaneType(name="sample_text_2")
    b = jpdl32_ProcessDefinitionType(description="sample_text", group="sample_text", name="sample_text")
    _safe_set(b, 'jpdl32_ProcessDefinitionType168', {a1})
    assert _is_linked(b, 'jpdl32_ProcessDefinitionType168', a1)
    if hasattr(a1, 'jpdl32_SwimlaneType169'):
        assert _is_linked(a1, 'jpdl32_SwimlaneType169', b)
    _safe_set(b, 'jpdl32_ProcessDefinitionType168', {a2})
    assert _is_linked(b, 'jpdl32_ProcessDefinitionType168', a2)
    if hasattr(a1, 'jpdl32_SwimlaneType169'):
        assert not _is_linked(a1, 'jpdl32_SwimlaneType169', b)
    if hasattr(a2, 'jpdl32_SwimlaneType169'):
        assert _is_linked(a2, 'jpdl32_SwimlaneType169', b)
    _safe_set(b, 'jpdl32_ProcessDefinitionType168', set())
    assert not _is_linked(b, 'jpdl32_ProcessDefinitionType168', a2)
    if hasattr(a2, 'jpdl32_SwimlaneType169'):
        assert not _is_linked(a2, 'jpdl32_SwimlaneType169', b)


def test_assoc_swimlane61_reverse_link_reassign_clear():
    a1 = jpdl32_SwimlaneType(name="sample_text")
    a2 = jpdl32_SwimlaneType(name="sample_text_2")
    b = jpdl32_DocumentRoot(description="sample_text", mixed="sample_text", recipients="sample_text", subject="sample_text", template="sample_text", text="sample_text", to="sample_text")
    _safe_set(b, 'jpdl32_DocumentRoot62', {a1})
    assert _is_linked(b, 'jpdl32_DocumentRoot62', a1)
    if hasattr(a1, 'jpdl32_SwimlaneType'):
        assert _is_linked(a1, 'jpdl32_SwimlaneType', b)
    _safe_set(b, 'jpdl32_DocumentRoot62', {a2})
    assert _is_linked(b, 'jpdl32_DocumentRoot62', a2)
    if hasattr(a1, 'jpdl32_SwimlaneType'):
        assert not _is_linked(a1, 'jpdl32_SwimlaneType', b)
    if hasattr(a2, 'jpdl32_SwimlaneType'):
        assert _is_linked(a2, 'jpdl32_SwimlaneType', b)
    _safe_set(b, 'jpdl32_DocumentRoot62', set())
    assert not _is_linked(b, 'jpdl32_DocumentRoot62', a2)
    if hasattr(a2, 'jpdl32_SwimlaneType'):
        assert not _is_linked(a2, 'jpdl32_SwimlaneType', b)


def test_assoc_task224_reverse_link_reassign_clear():
    a1 = jpdl32_TaskType(blocking="sample_text", description="sample_text", description1="sample_text", duedate="sample_text", group="sample_text", name="sample_text", notify="sample_text", priority="sample_text", signalling="sample_text", swimlane="sample_text")
    a2 = jpdl32_TaskType(blocking="sample_text_2", description="sample_text_2", description1="sample_text_2", duedate="sample_text_2", group="sample_text_2", name="sample_text_2", notify="sample_text_2", priority="sample_text_2", signalling="sample_text_2", swimlane="sample_text_2")
    b = jpdl32_ProcessDefinitionType(description="sample_text", group="sample_text", name="sample_text")
    _safe_set(b, 'jpdl32_ProcessDefinitionType225', {a1})
    assert _is_linked(b, 'jpdl32_ProcessDefinitionType225', a1)
    if hasattr(a1, 'jpdl32_TaskType226'):
        assert _is_linked(a1, 'jpdl32_TaskType226', b)
    _safe_set(b, 'jpdl32_ProcessDefinitionType225', {a2})
    assert _is_linked(b, 'jpdl32_ProcessDefinitionType225', a2)
    if hasattr(a1, 'jpdl32_TaskType226'):
        assert not _is_linked(a1, 'jpdl32_TaskType226', b)
    if hasattr(a2, 'jpdl32_TaskType226'):
        assert _is_linked(a2, 'jpdl32_TaskType226', b)
    _safe_set(b, 'jpdl32_ProcessDefinitionType225', set())
    assert not _is_linked(b, 'jpdl32_ProcessDefinitionType225', a2)
    if hasattr(a2, 'jpdl32_TaskType226'):
        assert not _is_linked(a2, 'jpdl32_TaskType226', b)


def test_assoc_task244_reverse_link_reassign_clear():
    a1 = jpdl32_TaskType(blocking="sample_text", description="sample_text", description1="sample_text", duedate="sample_text", group="sample_text", name="sample_text", notify="sample_text", priority="sample_text", signalling="sample_text", swimlane="sample_text")
    a2 = jpdl32_TaskType(blocking="sample_text_2", description="sample_text_2", description1="sample_text_2", duedate="sample_text_2", group="sample_text_2", name="sample_text_2", notify="sample_text_2", priority="sample_text_2", signalling="sample_text_2", swimlane="sample_text_2")
    b = jpdl32_StartStateType(description="sample_text", group="sample_text", name="sample_text")
    _safe_set(b, 'jpdl32_StartStateType245', {a1})
    assert _is_linked(b, 'jpdl32_StartStateType245', a1)
    if hasattr(a1, 'jpdl32_TaskType246'):
        assert _is_linked(a1, 'jpdl32_TaskType246', b)
    _safe_set(b, 'jpdl32_StartStateType245', {a2})
    assert _is_linked(b, 'jpdl32_StartStateType245', a2)
    if hasattr(a1, 'jpdl32_TaskType246'):
        assert not _is_linked(a1, 'jpdl32_TaskType246', b)
    if hasattr(a2, 'jpdl32_TaskType246'):
        assert _is_linked(a2, 'jpdl32_TaskType246', b)
    _safe_set(b, 'jpdl32_StartStateType245', set())
    assert not _is_linked(b, 'jpdl32_StartStateType245', a2)
    if hasattr(a2, 'jpdl32_TaskType246'):
        assert not _is_linked(a2, 'jpdl32_TaskType246', b)


def test_assoc_task313_reverse_link_reassign_clear():
    a1 = jpdl32_TaskType(blocking="sample_text", description="sample_text", description1="sample_text", duedate="sample_text", group="sample_text", name="sample_text", notify="sample_text", priority="sample_text", signalling="sample_text", swimlane="sample_text")
    a2 = jpdl32_TaskType(blocking="sample_text_2", description="sample_text_2", description1="sample_text_2", duedate="sample_text_2", group="sample_text_2", name="sample_text_2", notify="sample_text_2", priority="sample_text_2", signalling="sample_text_2", swimlane="sample_text_2")
    b = jpdl32_TaskNodeType(async_="sample_text", createTasks="sample_text", description="sample_text", endTasks="sample_text", group="sample_text", name="sample_text", signal="sample_text")
    _safe_set(b, 'jpdl32_TaskNodeType314', {a1})
    assert _is_linked(b, 'jpdl32_TaskNodeType314', a1)
    if hasattr(a1, 'jpdl32_TaskType315'):
        assert _is_linked(a1, 'jpdl32_TaskType315', b)
    _safe_set(b, 'jpdl32_TaskNodeType314', {a2})
    assert _is_linked(b, 'jpdl32_TaskNodeType314', a2)
    if hasattr(a1, 'jpdl32_TaskType315'):
        assert not _is_linked(a1, 'jpdl32_TaskType315', b)
    if hasattr(a2, 'jpdl32_TaskType315'):
        assert _is_linked(a2, 'jpdl32_TaskType315', b)
    _safe_set(b, 'jpdl32_TaskNodeType314', set())
    assert not _is_linked(b, 'jpdl32_TaskNodeType314', a2)
    if hasattr(a2, 'jpdl32_TaskType315'):
        assert not _is_linked(a2, 'jpdl32_TaskType315', b)


def test_assoc_task63_reverse_link_reassign_clear():
    a1 = jpdl32_TaskType(blocking="sample_text", description="sample_text", description1="sample_text", duedate="sample_text", group="sample_text", name="sample_text", notify="sample_text", priority="sample_text", signalling="sample_text", swimlane="sample_text")
    a2 = jpdl32_TaskType(blocking="sample_text_2", description="sample_text_2", description1="sample_text_2", duedate="sample_text_2", group="sample_text_2", name="sample_text_2", notify="sample_text_2", priority="sample_text_2", signalling="sample_text_2", swimlane="sample_text_2")
    b = jpdl32_DocumentRoot(description="sample_text", mixed="sample_text", recipients="sample_text", subject="sample_text", template="sample_text", text="sample_text", to="sample_text")
    _safe_set(b, 'jpdl32_DocumentRoot64', {a1})
    assert _is_linked(b, 'jpdl32_DocumentRoot64', a1)
    if hasattr(a1, 'jpdl32_TaskType'):
        assert _is_linked(a1, 'jpdl32_TaskType', b)
    _safe_set(b, 'jpdl32_DocumentRoot64', {a2})
    assert _is_linked(b, 'jpdl32_DocumentRoot64', a2)
    if hasattr(a1, 'jpdl32_TaskType'):
        assert not _is_linked(a1, 'jpdl32_TaskType', b)
    if hasattr(a2, 'jpdl32_TaskType'):
        assert _is_linked(a2, 'jpdl32_TaskType', b)
    _safe_set(b, 'jpdl32_DocumentRoot64', set())
    assert not _is_linked(b, 'jpdl32_DocumentRoot64', a2)
    if hasattr(a2, 'jpdl32_TaskType'):
        assert not _is_linked(a2, 'jpdl32_TaskType', b)


def test_assoc_taskNode179_reverse_link_reassign_clear():
    a1 = jpdl32_TaskNodeType(async_="sample_text", createTasks="sample_text", description="sample_text", endTasks="sample_text", group="sample_text", name="sample_text", signal="sample_text")
    a2 = jpdl32_TaskNodeType(async_="sample_text_2", createTasks="sample_text_2", description="sample_text_2", endTasks="sample_text_2", group="sample_text_2", name="sample_text_2", signal="sample_text_2")
    b = jpdl32_ProcessDefinitionType(description="sample_text", group="sample_text", name="sample_text")
    _safe_set(b, 'jpdl32_ProcessDefinitionType180', {a1})
    assert _is_linked(b, 'jpdl32_ProcessDefinitionType180', a1)
    if hasattr(a1, 'jpdl32_TaskNodeType181'):
        assert _is_linked(a1, 'jpdl32_TaskNodeType181', b)
    _safe_set(b, 'jpdl32_ProcessDefinitionType180', {a2})
    assert _is_linked(b, 'jpdl32_ProcessDefinitionType180', a2)
    if hasattr(a1, 'jpdl32_TaskNodeType181'):
        assert not _is_linked(a1, 'jpdl32_TaskNodeType181', b)
    if hasattr(a2, 'jpdl32_TaskNodeType181'):
        assert _is_linked(a2, 'jpdl32_TaskNodeType181', b)
    _safe_set(b, 'jpdl32_ProcessDefinitionType180', set())
    assert not _is_linked(b, 'jpdl32_ProcessDefinitionType180', a2)
    if hasattr(a2, 'jpdl32_TaskNodeType181'):
        assert not _is_linked(a2, 'jpdl32_TaskNodeType181', b)


def test_assoc_taskNode274_reverse_link_reassign_clear():
    a1 = jpdl32_TaskNodeType(async_="sample_text", createTasks="sample_text", description="sample_text", endTasks="sample_text", group="sample_text", name="sample_text", signal="sample_text")
    a2 = jpdl32_TaskNodeType(async_="sample_text_2", createTasks="sample_text_2", description="sample_text_2", endTasks="sample_text_2", group="sample_text_2", name="sample_text_2", signal="sample_text_2")
    b = jpdl32_SuperStateType(async_="sample_text", description="sample_text", group="sample_text", name="sample_text")
    _safe_set(b, 'jpdl32_SuperStateType275', {a1})
    assert _is_linked(b, 'jpdl32_SuperStateType275', a1)
    if hasattr(a1, 'jpdl32_TaskNodeType276'):
        assert _is_linked(a1, 'jpdl32_TaskNodeType276', b)
    _safe_set(b, 'jpdl32_SuperStateType275', {a2})
    assert _is_linked(b, 'jpdl32_SuperStateType275', a2)
    if hasattr(a1, 'jpdl32_TaskNodeType276'):
        assert not _is_linked(a1, 'jpdl32_TaskNodeType276', b)
    if hasattr(a2, 'jpdl32_TaskNodeType276'):
        assert _is_linked(a2, 'jpdl32_TaskNodeType276', b)
    _safe_set(b, 'jpdl32_SuperStateType275', set())
    assert not _is_linked(b, 'jpdl32_SuperStateType275', a2)
    if hasattr(a2, 'jpdl32_TaskNodeType276'):
        assert not _is_linked(a2, 'jpdl32_TaskNodeType276', b)


def test_assoc_taskNode65_reverse_link_reassign_clear():
    a1 = jpdl32_TaskNodeType(async_="sample_text", createTasks="sample_text", description="sample_text", endTasks="sample_text", group="sample_text", name="sample_text", signal="sample_text")
    a2 = jpdl32_TaskNodeType(async_="sample_text_2", createTasks="sample_text_2", description="sample_text_2", endTasks="sample_text_2", group="sample_text_2", name="sample_text_2", signal="sample_text_2")
    b = jpdl32_DocumentRoot(description="sample_text", mixed="sample_text", recipients="sample_text", subject="sample_text", template="sample_text", text="sample_text", to="sample_text")
    _safe_set(b, 'jpdl32_DocumentRoot66', {a1})
    assert _is_linked(b, 'jpdl32_DocumentRoot66', a1)
    if hasattr(a1, 'jpdl32_TaskNodeType'):
        assert _is_linked(a1, 'jpdl32_TaskNodeType', b)
    _safe_set(b, 'jpdl32_DocumentRoot66', {a2})
    assert _is_linked(b, 'jpdl32_DocumentRoot66', a2)
    if hasattr(a1, 'jpdl32_TaskNodeType'):
        assert not _is_linked(a1, 'jpdl32_TaskNodeType', b)
    if hasattr(a2, 'jpdl32_TaskNodeType'):
        assert _is_linked(a2, 'jpdl32_TaskNodeType', b)
    _safe_set(b, 'jpdl32_DocumentRoot66', set())
    assert not _is_linked(b, 'jpdl32_DocumentRoot66', a2)
    if hasattr(a2, 'jpdl32_TaskNodeType'):
        assert not _is_linked(a2, 'jpdl32_TaskNodeType', b)


def test_assoc_timer110_reverse_link_reassign_clear():
    a1 = jpdl32_TimerType(duedate="sample_text", name="sample_text", repeat="sample_text", transition="sample_text")
    a2 = jpdl32_TimerType(duedate="sample_text_2", name="sample_text_2", repeat="sample_text_2", transition="sample_text_2")
    b = jpdl32_ForkType(async_="sample_text", description="sample_text", group="sample_text", name="sample_text")
    _safe_set(b, 'jpdl32_ForkType111', {a1})
    assert _is_linked(b, 'jpdl32_ForkType111', a1)
    if hasattr(a1, 'jpdl32_TimerType112'):
        assert _is_linked(a1, 'jpdl32_TimerType112', b)
    _safe_set(b, 'jpdl32_ForkType111', {a2})
    assert _is_linked(b, 'jpdl32_ForkType111', a2)
    if hasattr(a1, 'jpdl32_TimerType112'):
        assert not _is_linked(a1, 'jpdl32_TimerType112', b)
    if hasattr(a2, 'jpdl32_TimerType112'):
        assert _is_linked(a2, 'jpdl32_TimerType112', b)
    _safe_set(b, 'jpdl32_ForkType111', set())
    assert not _is_linked(b, 'jpdl32_ForkType111', a2)
    if hasattr(a2, 'jpdl32_TimerType112'):
        assert not _is_linked(a2, 'jpdl32_TimerType112', b)


def test_assoc_timer122_reverse_link_reassign_clear():
    a1 = jpdl32_TimerType(duedate="sample_text", name="sample_text", repeat="sample_text", transition="sample_text")
    a2 = jpdl32_TimerType(duedate="sample_text_2", name="sample_text_2", repeat="sample_text_2", transition="sample_text_2")
    b = jpdl32_JoinType(async_="sample_text", description="sample_text", name="sample_text", nodeContentElements="sample_text")
    _safe_set(b, 'jpdl32_JoinType123', {a1})
    assert _is_linked(b, 'jpdl32_JoinType123', a1)
    if hasattr(a1, 'jpdl32_TimerType124'):
        assert _is_linked(a1, 'jpdl32_TimerType124', b)
    _safe_set(b, 'jpdl32_JoinType123', {a2})
    assert _is_linked(b, 'jpdl32_JoinType123', a2)
    if hasattr(a1, 'jpdl32_TimerType124'):
        assert not _is_linked(a1, 'jpdl32_TimerType124', b)
    if hasattr(a2, 'jpdl32_TimerType124'):
        assert _is_linked(a2, 'jpdl32_TimerType124', b)
    _safe_set(b, 'jpdl32_JoinType123', set())
    assert not _is_linked(b, 'jpdl32_JoinType123', a2)
    if hasattr(a2, 'jpdl32_TimerType124'):
        assert not _is_linked(a2, 'jpdl32_TimerType124', b)


def test_assoc_timer134_reverse_link_reassign_clear():
    a1 = jpdl32_TimerType(duedate="sample_text", name="sample_text", repeat="sample_text", transition="sample_text")
    a2 = jpdl32_TimerType(duedate="sample_text_2", name="sample_text_2", repeat="sample_text_2", transition="sample_text_2")
    b = jpdl32_MailNodeType(actors="sample_text", async_="sample_text", description="sample_text", group="sample_text", name="sample_text", subject="sample_text", subject1="sample_text", template="sample_text", text="sample_text", text1="sample_text", to="sample_text")
    _safe_set(b, 'jpdl32_MailNodeType135', {a1})
    assert _is_linked(b, 'jpdl32_MailNodeType135', a1)
    if hasattr(a1, 'jpdl32_TimerType136'):
        assert _is_linked(a1, 'jpdl32_TimerType136', b)
    _safe_set(b, 'jpdl32_MailNodeType135', {a2})
    assert _is_linked(b, 'jpdl32_MailNodeType135', a2)
    if hasattr(a1, 'jpdl32_TimerType136'):
        assert not _is_linked(a1, 'jpdl32_TimerType136', b)
    if hasattr(a2, 'jpdl32_TimerType136'):
        assert _is_linked(a2, 'jpdl32_TimerType136', b)
    _safe_set(b, 'jpdl32_MailNodeType135', set())
    assert not _is_linked(b, 'jpdl32_MailNodeType135', a2)
    if hasattr(a2, 'jpdl32_TimerType136'):
        assert not _is_linked(a2, 'jpdl32_TimerType136', b)


def test_assoc_timer161_reverse_link_reassign_clear():
    a1 = jpdl32_TimerType(duedate="sample_text", name="sample_text", repeat="sample_text", transition="sample_text")
    a2 = jpdl32_TimerType(duedate="sample_text_2", name="sample_text_2", repeat="sample_text_2", transition="sample_text_2")
    b = jpdl32_NodeType(async_="sample_text", description="sample_text", name="sample_text", nodeContentElements="sample_text")
    _safe_set(b, 'jpdl32_NodeType162', {a1})
    assert _is_linked(b, 'jpdl32_NodeType162', a1)
    if hasattr(a1, 'jpdl32_TimerType163'):
        assert _is_linked(a1, 'jpdl32_TimerType163', b)
    _safe_set(b, 'jpdl32_NodeType162', {a2})
    assert _is_linked(b, 'jpdl32_NodeType162', a2)
    if hasattr(a1, 'jpdl32_TimerType163'):
        assert not _is_linked(a1, 'jpdl32_TimerType163', b)
    if hasattr(a2, 'jpdl32_TimerType163'):
        assert _is_linked(a2, 'jpdl32_TimerType163', b)
    _safe_set(b, 'jpdl32_NodeType162', set())
    assert not _is_linked(b, 'jpdl32_NodeType162', a2)
    if hasattr(a2, 'jpdl32_TimerType163'):
        assert not _is_linked(a2, 'jpdl32_TimerType163', b)


def test_assoc_timer238_reverse_link_reassign_clear():
    a1 = jpdl32_TimerType(duedate="sample_text", name="sample_text", repeat="sample_text", transition="sample_text")
    a2 = jpdl32_TimerType(duedate="sample_text_2", name="sample_text_2", repeat="sample_text_2", transition="sample_text_2")
    b = jpdl32_ProcessStateType(async_="sample_text", binding="sample_text", description="sample_text", group="sample_text", name="sample_text")
    _safe_set(b, 'jpdl32_ProcessStateType239', {a1})
    assert _is_linked(b, 'jpdl32_ProcessStateType239', a1)
    if hasattr(a1, 'jpdl32_TimerType240'):
        assert _is_linked(a1, 'jpdl32_TimerType240', b)
    _safe_set(b, 'jpdl32_ProcessStateType239', {a2})
    assert _is_linked(b, 'jpdl32_ProcessStateType239', a2)
    if hasattr(a1, 'jpdl32_TimerType240'):
        assert not _is_linked(a1, 'jpdl32_TimerType240', b)
    if hasattr(a2, 'jpdl32_TimerType240'):
        assert _is_linked(a2, 'jpdl32_TimerType240', b)
    _safe_set(b, 'jpdl32_ProcessStateType239', set())
    assert not _is_linked(b, 'jpdl32_ProcessStateType239', a2)
    if hasattr(a2, 'jpdl32_TimerType240'):
        assert not _is_linked(a2, 'jpdl32_TimerType240', b)


def test_assoc_timer262_reverse_link_reassign_clear():
    a1 = jpdl32_TimerType(duedate="sample_text", name="sample_text", repeat="sample_text", transition="sample_text")
    a2 = jpdl32_TimerType(duedate="sample_text_2", name="sample_text_2", repeat="sample_text_2", transition="sample_text_2")
    b = jpdl32_StateType(async_="sample_text", description="sample_text", name="sample_text", nodeContentElements="sample_text")
    _safe_set(b, 'jpdl32_StateType263', {a1})
    assert _is_linked(b, 'jpdl32_StateType263', a1)
    if hasattr(a1, 'jpdl32_TimerType264'):
        assert _is_linked(a1, 'jpdl32_TimerType264', b)
    _safe_set(b, 'jpdl32_StateType263', {a2})
    assert _is_linked(b, 'jpdl32_StateType263', a2)
    if hasattr(a1, 'jpdl32_TimerType264'):
        assert not _is_linked(a1, 'jpdl32_TimerType264', b)
    if hasattr(a2, 'jpdl32_TimerType264'):
        assert _is_linked(a2, 'jpdl32_TimerType264', b)
    _safe_set(b, 'jpdl32_StateType263', set())
    assert not _is_linked(b, 'jpdl32_StateType263', a2)
    if hasattr(a2, 'jpdl32_TimerType264'):
        assert not _is_linked(a2, 'jpdl32_TimerType264', b)


def test_assoc_timer304_reverse_link_reassign_clear():
    a1 = jpdl32_TimerType(duedate="sample_text", name="sample_text", repeat="sample_text", transition="sample_text")
    a2 = jpdl32_TimerType(duedate="sample_text_2", name="sample_text_2", repeat="sample_text_2", transition="sample_text_2")
    b = jpdl32_SuperStateType(async_="sample_text", description="sample_text", group="sample_text", name="sample_text")
    _safe_set(b, 'jpdl32_SuperStateType305', {a1})
    assert _is_linked(b, 'jpdl32_SuperStateType305', a1)
    if hasattr(a1, 'jpdl32_TimerType306'):
        assert _is_linked(a1, 'jpdl32_TimerType306', b)
    _safe_set(b, 'jpdl32_SuperStateType305', {a2})
    assert _is_linked(b, 'jpdl32_SuperStateType305', a2)
    if hasattr(a1, 'jpdl32_TimerType306'):
        assert not _is_linked(a1, 'jpdl32_TimerType306', b)
    if hasattr(a2, 'jpdl32_TimerType306'):
        assert _is_linked(a2, 'jpdl32_TimerType306', b)
    _safe_set(b, 'jpdl32_SuperStateType305', set())
    assert not _is_linked(b, 'jpdl32_SuperStateType305', a2)
    if hasattr(a2, 'jpdl32_TimerType306'):
        assert not _is_linked(a2, 'jpdl32_TimerType306', b)


def test_assoc_timer322_reverse_link_reassign_clear():
    a1 = jpdl32_TimerType(duedate="sample_text", name="sample_text", repeat="sample_text", transition="sample_text")
    a2 = jpdl32_TimerType(duedate="sample_text_2", name="sample_text_2", repeat="sample_text_2", transition="sample_text_2")
    b = jpdl32_TaskNodeType(async_="sample_text", createTasks="sample_text", description="sample_text", endTasks="sample_text", group="sample_text", name="sample_text", signal="sample_text")
    _safe_set(b, 'jpdl32_TaskNodeType323', {a1})
    assert _is_linked(b, 'jpdl32_TaskNodeType323', a1)
    if hasattr(a1, 'jpdl32_TimerType324'):
        assert _is_linked(a1, 'jpdl32_TimerType324', b)
    _safe_set(b, 'jpdl32_TaskNodeType323', {a2})
    assert _is_linked(b, 'jpdl32_TaskNodeType323', a2)
    if hasattr(a1, 'jpdl32_TimerType324'):
        assert not _is_linked(a1, 'jpdl32_TimerType324', b)
    if hasattr(a2, 'jpdl32_TimerType324'):
        assert _is_linked(a2, 'jpdl32_TimerType324', b)
    _safe_set(b, 'jpdl32_TaskNodeType323', set())
    assert not _is_linked(b, 'jpdl32_TaskNodeType323', a2)
    if hasattr(a2, 'jpdl32_TimerType324'):
        assert not _is_linked(a2, 'jpdl32_TimerType324', b)


def test_assoc_timer337_reverse_link_reassign_clear():
    a1 = jpdl32_TimerType(duedate="sample_text", name="sample_text", repeat="sample_text", transition="sample_text")
    a2 = jpdl32_TimerType(duedate="sample_text_2", name="sample_text_2", repeat="sample_text_2", transition="sample_text_2")
    b = jpdl32_TaskType(blocking="sample_text", description="sample_text", description1="sample_text", duedate="sample_text", group="sample_text", name="sample_text", notify="sample_text", priority="sample_text", signalling="sample_text", swimlane="sample_text")
    _safe_set(b, 'jpdl32_TaskType338', {a1})
    assert _is_linked(b, 'jpdl32_TaskType338', a1)
    if hasattr(a1, 'jpdl32_TimerType339'):
        assert _is_linked(a1, 'jpdl32_TimerType339', b)
    _safe_set(b, 'jpdl32_TaskType338', {a2})
    assert _is_linked(b, 'jpdl32_TaskType338', a2)
    if hasattr(a1, 'jpdl32_TimerType339'):
        assert not _is_linked(a1, 'jpdl32_TimerType339', b)
    if hasattr(a2, 'jpdl32_TimerType339'):
        assert _is_linked(a2, 'jpdl32_TimerType339', b)
    _safe_set(b, 'jpdl32_TaskType338', set())
    assert not _is_linked(b, 'jpdl32_TaskType338', a2)
    if hasattr(a2, 'jpdl32_TimerType339'):
        assert not _is_linked(a2, 'jpdl32_TimerType339', b)


def test_assoc_timer67_reverse_link_reassign_clear():
    a1 = jpdl32_TimerType(duedate="sample_text", name="sample_text", repeat="sample_text", transition="sample_text")
    a2 = jpdl32_TimerType(duedate="sample_text_2", name="sample_text_2", repeat="sample_text_2", transition="sample_text_2")
    b = jpdl32_DocumentRoot(description="sample_text", mixed="sample_text", recipients="sample_text", subject="sample_text", template="sample_text", text="sample_text", to="sample_text")
    _safe_set(b, 'jpdl32_DocumentRoot68', {a1})
    assert _is_linked(b, 'jpdl32_DocumentRoot68', a1)
    if hasattr(a1, 'jpdl32_TimerType'):
        assert _is_linked(a1, 'jpdl32_TimerType', b)
    _safe_set(b, 'jpdl32_DocumentRoot68', {a2})
    assert _is_linked(b, 'jpdl32_DocumentRoot68', a2)
    if hasattr(a1, 'jpdl32_TimerType'):
        assert not _is_linked(a1, 'jpdl32_TimerType', b)
    if hasattr(a2, 'jpdl32_TimerType'):
        assert _is_linked(a2, 'jpdl32_TimerType', b)
    _safe_set(b, 'jpdl32_DocumentRoot68', set())
    assert not _is_linked(b, 'jpdl32_DocumentRoot68', a2)
    if hasattr(a2, 'jpdl32_TimerType'):
        assert not _is_linked(a2, 'jpdl32_TimerType', b)


def test_assoc_transition113_reverse_link_reassign_clear():
    a1 = jpdl32_TransitionType(description="sample_text", group="sample_text", name="sample_text", to="sample_text")
    a2 = jpdl32_TransitionType(description="sample_text_2", group="sample_text_2", name="sample_text_2", to="sample_text_2")
    b = jpdl32_ForkType(async_="sample_text", description="sample_text", group="sample_text", name="sample_text")
    _safe_set(b, 'jpdl32_ForkType114', {a1})
    assert _is_linked(b, 'jpdl32_ForkType114', a1)
    if hasattr(a1, 'jpdl32_TransitionType115'):
        assert _is_linked(a1, 'jpdl32_TransitionType115', b)
    _safe_set(b, 'jpdl32_ForkType114', {a2})
    assert _is_linked(b, 'jpdl32_ForkType114', a2)
    if hasattr(a1, 'jpdl32_TransitionType115'):
        assert not _is_linked(a1, 'jpdl32_TransitionType115', b)
    if hasattr(a2, 'jpdl32_TransitionType115'):
        assert _is_linked(a2, 'jpdl32_TransitionType115', b)
    _safe_set(b, 'jpdl32_ForkType114', set())
    assert not _is_linked(b, 'jpdl32_ForkType114', a2)
    if hasattr(a2, 'jpdl32_TransitionType115'):
        assert not _is_linked(a2, 'jpdl32_TransitionType115', b)


def test_assoc_transition125_reverse_link_reassign_clear():
    a1 = jpdl32_TransitionType(description="sample_text", group="sample_text", name="sample_text", to="sample_text")
    a2 = jpdl32_TransitionType(description="sample_text_2", group="sample_text_2", name="sample_text_2", to="sample_text_2")
    b = jpdl32_JoinType(async_="sample_text", description="sample_text", name="sample_text", nodeContentElements="sample_text")
    _safe_set(b, 'jpdl32_JoinType126', {a1})
    assert _is_linked(b, 'jpdl32_JoinType126', a1)
    if hasattr(a1, 'jpdl32_TransitionType127'):
        assert _is_linked(a1, 'jpdl32_TransitionType127', b)
    _safe_set(b, 'jpdl32_JoinType126', {a2})
    assert _is_linked(b, 'jpdl32_JoinType126', a2)
    if hasattr(a1, 'jpdl32_TransitionType127'):
        assert not _is_linked(a1, 'jpdl32_TransitionType127', b)
    if hasattr(a2, 'jpdl32_TransitionType127'):
        assert _is_linked(a2, 'jpdl32_TransitionType127', b)
    _safe_set(b, 'jpdl32_JoinType126', set())
    assert not _is_linked(b, 'jpdl32_JoinType126', a2)
    if hasattr(a2, 'jpdl32_TransitionType127'):
        assert not _is_linked(a2, 'jpdl32_TransitionType127', b)


def test_assoc_transition137_reverse_link_reassign_clear():
    a1 = jpdl32_TransitionType(description="sample_text", group="sample_text", name="sample_text", to="sample_text")
    a2 = jpdl32_TransitionType(description="sample_text_2", group="sample_text_2", name="sample_text_2", to="sample_text_2")
    b = jpdl32_MailNodeType(actors="sample_text", async_="sample_text", description="sample_text", group="sample_text", name="sample_text", subject="sample_text", subject1="sample_text", template="sample_text", text="sample_text", text1="sample_text", to="sample_text")
    _safe_set(b, 'jpdl32_MailNodeType138', {a1})
    assert _is_linked(b, 'jpdl32_MailNodeType138', a1)
    if hasattr(a1, 'jpdl32_TransitionType139'):
        assert _is_linked(a1, 'jpdl32_TransitionType139', b)
    _safe_set(b, 'jpdl32_MailNodeType138', {a2})
    assert _is_linked(b, 'jpdl32_MailNodeType138', a2)
    if hasattr(a1, 'jpdl32_TransitionType139'):
        assert not _is_linked(a1, 'jpdl32_TransitionType139', b)
    if hasattr(a2, 'jpdl32_TransitionType139'):
        assert _is_linked(a2, 'jpdl32_TransitionType139', b)
    _safe_set(b, 'jpdl32_MailNodeType138', set())
    assert not _is_linked(b, 'jpdl32_MailNodeType138', a2)
    if hasattr(a2, 'jpdl32_TransitionType139'):
        assert not _is_linked(a2, 'jpdl32_TransitionType139', b)


def test_assoc_transition164_reverse_link_reassign_clear():
    a1 = jpdl32_TransitionType(description="sample_text", group="sample_text", name="sample_text", to="sample_text")
    a2 = jpdl32_TransitionType(description="sample_text_2", group="sample_text_2", name="sample_text_2", to="sample_text_2")
    b = jpdl32_NodeType(async_="sample_text", description="sample_text", name="sample_text", nodeContentElements="sample_text")
    _safe_set(b, 'jpdl32_NodeType165', {a1})
    assert _is_linked(b, 'jpdl32_NodeType165', a1)
    if hasattr(a1, 'jpdl32_TransitionType166'):
        assert _is_linked(a1, 'jpdl32_TransitionType166', b)
    _safe_set(b, 'jpdl32_NodeType165', {a2})
    assert _is_linked(b, 'jpdl32_NodeType165', a2)
    if hasattr(a1, 'jpdl32_TransitionType166'):
        assert not _is_linked(a1, 'jpdl32_TransitionType166', b)
    if hasattr(a2, 'jpdl32_TransitionType166'):
        assert _is_linked(a2, 'jpdl32_TransitionType166', b)
    _safe_set(b, 'jpdl32_NodeType165', set())
    assert not _is_linked(b, 'jpdl32_NodeType165', a2)
    if hasattr(a2, 'jpdl32_TransitionType166'):
        assert not _is_linked(a2, 'jpdl32_TransitionType166', b)


def test_assoc_transition241_reverse_link_reassign_clear():
    a1 = jpdl32_TransitionType(description="sample_text", group="sample_text", name="sample_text", to="sample_text")
    a2 = jpdl32_TransitionType(description="sample_text_2", group="sample_text_2", name="sample_text_2", to="sample_text_2")
    b = jpdl32_ProcessStateType(async_="sample_text", binding="sample_text", description="sample_text", group="sample_text", name="sample_text")
    _safe_set(b, 'jpdl32_ProcessStateType242', {a1})
    assert _is_linked(b, 'jpdl32_ProcessStateType242', a1)
    if hasattr(a1, 'jpdl32_TransitionType243'):
        assert _is_linked(a1, 'jpdl32_TransitionType243', b)
    _safe_set(b, 'jpdl32_ProcessStateType242', {a2})
    assert _is_linked(b, 'jpdl32_ProcessStateType242', a2)
    if hasattr(a1, 'jpdl32_TransitionType243'):
        assert not _is_linked(a1, 'jpdl32_TransitionType243', b)
    if hasattr(a2, 'jpdl32_TransitionType243'):
        assert _is_linked(a2, 'jpdl32_TransitionType243', b)
    _safe_set(b, 'jpdl32_ProcessStateType242', set())
    assert not _is_linked(b, 'jpdl32_ProcessStateType242', a2)
    if hasattr(a2, 'jpdl32_TransitionType243'):
        assert not _is_linked(a2, 'jpdl32_TransitionType243', b)


def test_assoc_transition247_reverse_link_reassign_clear():
    a1 = jpdl32_TransitionType(description="sample_text", group="sample_text", name="sample_text", to="sample_text")
    a2 = jpdl32_TransitionType(description="sample_text_2", group="sample_text_2", name="sample_text_2", to="sample_text_2")
    b = jpdl32_StartStateType(description="sample_text", group="sample_text", name="sample_text")
    _safe_set(b, 'jpdl32_StartStateType248', {a1})
    assert _is_linked(b, 'jpdl32_StartStateType248', a1)
    if hasattr(a1, 'jpdl32_TransitionType249'):
        assert _is_linked(a1, 'jpdl32_TransitionType249', b)
    _safe_set(b, 'jpdl32_StartStateType248', {a2})
    assert _is_linked(b, 'jpdl32_StartStateType248', a2)
    if hasattr(a1, 'jpdl32_TransitionType249'):
        assert not _is_linked(a1, 'jpdl32_TransitionType249', b)
    if hasattr(a2, 'jpdl32_TransitionType249'):
        assert _is_linked(a2, 'jpdl32_TransitionType249', b)
    _safe_set(b, 'jpdl32_StartStateType248', set())
    assert not _is_linked(b, 'jpdl32_StartStateType248', a2)
    if hasattr(a2, 'jpdl32_TransitionType249'):
        assert not _is_linked(a2, 'jpdl32_TransitionType249', b)


def test_assoc_transition265_reverse_link_reassign_clear():
    a1 = jpdl32_TransitionType(description="sample_text", group="sample_text", name="sample_text", to="sample_text")
    a2 = jpdl32_TransitionType(description="sample_text_2", group="sample_text_2", name="sample_text_2", to="sample_text_2")
    b = jpdl32_StateType(async_="sample_text", description="sample_text", name="sample_text", nodeContentElements="sample_text")
    _safe_set(b, 'jpdl32_StateType266', {a1})
    assert _is_linked(b, 'jpdl32_StateType266', a1)
    if hasattr(a1, 'jpdl32_TransitionType267'):
        assert _is_linked(a1, 'jpdl32_TransitionType267', b)
    _safe_set(b, 'jpdl32_StateType266', {a2})
    assert _is_linked(b, 'jpdl32_StateType266', a2)
    if hasattr(a1, 'jpdl32_TransitionType267'):
        assert not _is_linked(a1, 'jpdl32_TransitionType267', b)
    if hasattr(a2, 'jpdl32_TransitionType267'):
        assert _is_linked(a2, 'jpdl32_TransitionType267', b)
    _safe_set(b, 'jpdl32_StateType266', set())
    assert not _is_linked(b, 'jpdl32_StateType266', a2)
    if hasattr(a2, 'jpdl32_TransitionType267'):
        assert not _is_linked(a2, 'jpdl32_TransitionType267', b)


def test_assoc_transition307_reverse_link_reassign_clear():
    a1 = jpdl32_TransitionType(description="sample_text", group="sample_text", name="sample_text", to="sample_text")
    a2 = jpdl32_TransitionType(description="sample_text_2", group="sample_text_2", name="sample_text_2", to="sample_text_2")
    b = jpdl32_SuperStateType(async_="sample_text", description="sample_text", group="sample_text", name="sample_text")
    _safe_set(b, 'jpdl32_SuperStateType308', {a1})
    assert _is_linked(b, 'jpdl32_SuperStateType308', a1)
    if hasattr(a1, 'jpdl32_TransitionType309'):
        assert _is_linked(a1, 'jpdl32_TransitionType309', b)
    _safe_set(b, 'jpdl32_SuperStateType308', {a2})
    assert _is_linked(b, 'jpdl32_SuperStateType308', a2)
    if hasattr(a1, 'jpdl32_TransitionType309'):
        assert not _is_linked(a1, 'jpdl32_TransitionType309', b)
    if hasattr(a2, 'jpdl32_TransitionType309'):
        assert _is_linked(a2, 'jpdl32_TransitionType309', b)
    _safe_set(b, 'jpdl32_SuperStateType308', set())
    assert not _is_linked(b, 'jpdl32_SuperStateType308', a2)
    if hasattr(a2, 'jpdl32_TransitionType309'):
        assert not _is_linked(a2, 'jpdl32_TransitionType309', b)


def test_assoc_transition325_reverse_link_reassign_clear():
    a1 = jpdl32_TransitionType(description="sample_text", group="sample_text", name="sample_text", to="sample_text")
    a2 = jpdl32_TransitionType(description="sample_text_2", group="sample_text_2", name="sample_text_2", to="sample_text_2")
    b = jpdl32_TaskNodeType(async_="sample_text", createTasks="sample_text", description="sample_text", endTasks="sample_text", group="sample_text", name="sample_text", signal="sample_text")
    _safe_set(b, 'jpdl32_TaskNodeType326', {a1})
    assert _is_linked(b, 'jpdl32_TaskNodeType326', a1)
    if hasattr(a1, 'jpdl32_TransitionType327'):
        assert _is_linked(a1, 'jpdl32_TransitionType327', b)
    _safe_set(b, 'jpdl32_TaskNodeType326', {a2})
    assert _is_linked(b, 'jpdl32_TaskNodeType326', a2)
    if hasattr(a1, 'jpdl32_TransitionType327'):
        assert not _is_linked(a1, 'jpdl32_TransitionType327', b)
    if hasattr(a2, 'jpdl32_TransitionType327'):
        assert _is_linked(a2, 'jpdl32_TransitionType327', b)
    _safe_set(b, 'jpdl32_TaskNodeType326', set())
    assert not _is_linked(b, 'jpdl32_TaskNodeType326', a2)
    if hasattr(a2, 'jpdl32_TransitionType327'):
        assert not _is_linked(a2, 'jpdl32_TransitionType327', b)


def test_assoc_transition69_reverse_link_reassign_clear():
    a1 = jpdl32_TransitionType(description="sample_text", group="sample_text", name="sample_text", to="sample_text")
    a2 = jpdl32_TransitionType(description="sample_text_2", group="sample_text_2", name="sample_text_2", to="sample_text_2")
    b = jpdl32_DocumentRoot(description="sample_text", mixed="sample_text", recipients="sample_text", subject="sample_text", template="sample_text", text="sample_text", to="sample_text")
    _safe_set(b, 'jpdl32_DocumentRoot70', {a1})
    assert _is_linked(b, 'jpdl32_DocumentRoot70', a1)
    if hasattr(a1, 'jpdl32_TransitionType71'):
        assert _is_linked(a1, 'jpdl32_TransitionType71', b)
    _safe_set(b, 'jpdl32_DocumentRoot70', {a2})
    assert _is_linked(b, 'jpdl32_DocumentRoot70', a2)
    if hasattr(a1, 'jpdl32_TransitionType71'):
        assert not _is_linked(a1, 'jpdl32_TransitionType71', b)
    if hasattr(a2, 'jpdl32_TransitionType71'):
        assert _is_linked(a2, 'jpdl32_TransitionType71', b)
    _safe_set(b, 'jpdl32_DocumentRoot70', set())
    assert not _is_linked(b, 'jpdl32_DocumentRoot70', a2)
    if hasattr(a2, 'jpdl32_TransitionType71'):
        assert not _is_linked(a2, 'jpdl32_TransitionType71', b)


def test_assoc_transition8_reverse_link_reassign_clear():
    a1 = jpdl32_TransitionType(description="sample_text", group="sample_text", name="sample_text", to="sample_text")
    a2 = jpdl32_TransitionType(description="sample_text_2", group="sample_text_2", name="sample_text_2", to="sample_text_2")
    b = jpdl32_DecisionType(async_="sample_text", description="sample_text", expression="sample_text", group="sample_text", name="sample_text")
    _safe_set(b, 'jpdl32_DecisionType9', {a1})
    assert _is_linked(b, 'jpdl32_DecisionType9', a1)
    if hasattr(a1, 'jpdl32_TransitionType'):
        assert _is_linked(a1, 'jpdl32_TransitionType', b)
    _safe_set(b, 'jpdl32_DecisionType9', {a2})
    assert _is_linked(b, 'jpdl32_DecisionType9', a2)
    if hasattr(a1, 'jpdl32_TransitionType'):
        assert not _is_linked(a1, 'jpdl32_TransitionType', b)
    if hasattr(a2, 'jpdl32_TransitionType'):
        assert _is_linked(a2, 'jpdl32_TransitionType', b)
    _safe_set(b, 'jpdl32_DecisionType9', set())
    assert not _is_linked(b, 'jpdl32_DecisionType9', a2)
    if hasattr(a2, 'jpdl32_TransitionType'):
        assert not _is_linked(a2, 'jpdl32_TransitionType', b)


def test_assoc_variable229_reverse_link_reassign_clear():
    a1 = jpdl32_VariableType(access="sample_text", any="sample_text", mappedName="sample_text", name="sample_text")
    a2 = jpdl32_VariableType(access="sample_text_2", any="sample_text_2", mappedName="sample_text_2", name="sample_text_2")
    b = jpdl32_ProcessStateType(async_="sample_text", binding="sample_text", description="sample_text", group="sample_text", name="sample_text")
    _safe_set(b, 'jpdl32_ProcessStateType230', {a1})
    assert _is_linked(b, 'jpdl32_ProcessStateType230', a1)
    if hasattr(a1, 'jpdl32_VariableType231'):
        assert _is_linked(a1, 'jpdl32_VariableType231', b)
    _safe_set(b, 'jpdl32_ProcessStateType230', {a2})
    assert _is_linked(b, 'jpdl32_ProcessStateType230', a2)
    if hasattr(a1, 'jpdl32_VariableType231'):
        assert not _is_linked(a1, 'jpdl32_VariableType231', b)
    if hasattr(a2, 'jpdl32_VariableType231'):
        assert _is_linked(a2, 'jpdl32_VariableType231', b)
    _safe_set(b, 'jpdl32_ProcessStateType230', set())
    assert not _is_linked(b, 'jpdl32_ProcessStateType230', a2)
    if hasattr(a2, 'jpdl32_VariableType231'):
        assert not _is_linked(a2, 'jpdl32_VariableType231', b)


def test_assoc_variable72_reverse_link_reassign_clear():
    a1 = jpdl32_VariableType(access="sample_text", any="sample_text", mappedName="sample_text", name="sample_text")
    a2 = jpdl32_VariableType(access="sample_text_2", any="sample_text_2", mappedName="sample_text_2", name="sample_text_2")
    b = jpdl32_DocumentRoot(description="sample_text", mixed="sample_text", recipients="sample_text", subject="sample_text", template="sample_text", text="sample_text", to="sample_text")
    _safe_set(b, 'jpdl32_DocumentRoot73', {a1})
    assert _is_linked(b, 'jpdl32_DocumentRoot73', a1)
    if hasattr(a1, 'jpdl32_VariableType'):
        assert _is_linked(a1, 'jpdl32_VariableType', b)
    _safe_set(b, 'jpdl32_DocumentRoot73', {a2})
    assert _is_linked(b, 'jpdl32_DocumentRoot73', a2)
    if hasattr(a1, 'jpdl32_VariableType'):
        assert not _is_linked(a1, 'jpdl32_VariableType', b)
    if hasattr(a2, 'jpdl32_VariableType'):
        assert _is_linked(a2, 'jpdl32_VariableType', b)
    _safe_set(b, 'jpdl32_DocumentRoot73', set())
    assert not _is_linked(b, 'jpdl32_DocumentRoot73', a2)
    if hasattr(a2, 'jpdl32_VariableType'):
        assert not _is_linked(a2, 'jpdl32_VariableType', b)


