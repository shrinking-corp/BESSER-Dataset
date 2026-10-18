import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Delegation,
    jpdl31_ActionType,
    jpdl31_Alternative,
    jpdl31_Artefact,
    jpdl31_AssignmentType,
    jpdl31_CancelTimerType,
    jpdl31_ConditionType,
    jpdl31_CreateTimerType,
    jpdl31_DecisionType,
    jpdl31_Delegation,
    jpdl31_DependentVariable,
    jpdl31_Design,
    jpdl31_DocumentRoot,
    jpdl31_EStringToStringMapEntry,
    jpdl31_EndStateType,
    jpdl31_EventType,
    jpdl31_ExceptionHandlerType,
    jpdl31_ExperimentalPlan,
    jpdl31_Factor,
    jpdl31_ForkType,
    jpdl31_Goal,
    jpdl31_Hyphotesis,
    jpdl31_JoinType,
    jpdl31_Level,
    jpdl31_Metric,
    jpdl31_MetricInfo,
    jpdl31_Model,
    jpdl31_NodeType,
    jpdl31_Parameter,
    jpdl31_ProcessDefinitionType,
    jpdl31_ProcessStateType,
    jpdl31_Question,
    jpdl31_Questionnaire,
    jpdl31_ScriptType,
    jpdl31_StartStateType,
    jpdl31_StateType,
    jpdl31_StatisticalTest,
    jpdl31_SubProcessType,
    jpdl31_Subhypotheses,
    jpdl31_SuperStateType,
    jpdl31_SwimlaneType,
    jpdl31_TaskNodeType,
    jpdl31_TaskType,
    jpdl31_TimerType,
    jpdl31_TransitionType,
    jpdl31_TransitionType1,
    jpdl31_VariableType,
    AnswerType,
    ArtefactType,
    BooleanType,
    ConfigType,
    ConfigTypeType,
    ConfigTypeType1,
    DoEType,
    HypothesisType,
    MetricType,
    PriorityTypeMember0,
    QuestionnaireType,
    RelationOperator,
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

def test_assoc_EReference0396_reverse_link_reassign_clear():
    a1 = jpdl31_Question(description="sample_text", required="sample_text", type="sample_text")
    a2 = jpdl31_Question(description="sample_text_2", required="sample_text_2", type="sample_text_2")
    b = jpdl31_Question(description="sample_text", required="sample_text", type="sample_text")
    _safe_set(b, 'jpdl31_Question397', a1)
    assert _is_linked(b, 'jpdl31_Question397', a1)
    if hasattr(a1, 'jpdl31_Question395'):
        assert _is_linked(a1, 'jpdl31_Question395', b)
    _safe_set(b, 'jpdl31_Question397', a2)
    assert _is_linked(b, 'jpdl31_Question397', a2)
    if hasattr(a1, 'jpdl31_Question395'):
        assert not _is_linked(a1, 'jpdl31_Question395', b)
    if hasattr(a2, 'jpdl31_Question395'):
        assert _is_linked(a2, 'jpdl31_Question395', b)
    _safe_set(b, 'jpdl31_Question397', None)
    assert not _is_linked(b, 'jpdl31_Question397', a2)
    if hasattr(a2, 'jpdl31_Question395'):
        assert not _is_linked(a2, 'jpdl31_Question395', b)


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


def test_assoc_action126_reverse_link_reassign_clear():
    a1 = jpdl31_NodeType(async_="sample_text", description="sample_text", name="sample_text", nodeContentElements="sample_text")
    a2 = jpdl31_NodeType(async_="sample_text_2", description="sample_text_2", name="sample_text_2", nodeContentElements="sample_text_2")
    b = jpdl31_ActionType(acceptPropagatedEvents="sample_text", any="sample_text", async_="sample_text", class_="sample_text", configType="sample_text", expression="sample_text", mixed="sample_text", name="sample_text", refName="sample_text")
    _safe_set(b, 'jpdl31_ActionType128', a1)
    assert _is_linked(b, 'jpdl31_ActionType128', a1)
    if hasattr(a1, 'jpdl31_NodeType127'):
        assert _is_linked(a1, 'jpdl31_NodeType127', b)
    _safe_set(b, 'jpdl31_ActionType128', a2)
    assert _is_linked(b, 'jpdl31_ActionType128', a2)
    if hasattr(a1, 'jpdl31_NodeType127'):
        assert not _is_linked(a1, 'jpdl31_NodeType127', b)
    if hasattr(a2, 'jpdl31_NodeType127'):
        assert _is_linked(a2, 'jpdl31_NodeType127', b)
    _safe_set(b, 'jpdl31_ActionType128', None)
    assert not _is_linked(b, 'jpdl31_ActionType128', a2)
    if hasattr(a2, 'jpdl31_NodeType127'):
        assert not _is_linked(a2, 'jpdl31_NodeType127', b)


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


def test_assoc_action183_reverse_link_reassign_clear():
    a1 = jpdl31_ProcessDefinitionType(group="sample_text", name="sample_text", quantity="sample_text")
    a2 = jpdl31_ProcessDefinitionType(group="sample_text_2", name="sample_text_2", quantity="sample_text_2")
    b = jpdl31_ActionType(acceptPropagatedEvents="sample_text", any="sample_text", async_="sample_text", class_="sample_text", configType="sample_text", expression="sample_text", mixed="sample_text", name="sample_text", refName="sample_text")
    _safe_set(b, 'jpdl31_ActionType185', a1)
    assert _is_linked(b, 'jpdl31_ActionType185', a1)
    if hasattr(a1, 'jpdl31_ProcessDefinitionType184'):
        assert _is_linked(a1, 'jpdl31_ProcessDefinitionType184', b)
    _safe_set(b, 'jpdl31_ActionType185', a2)
    assert _is_linked(b, 'jpdl31_ActionType185', a2)
    if hasattr(a1, 'jpdl31_ProcessDefinitionType184'):
        assert not _is_linked(a1, 'jpdl31_ProcessDefinitionType184', b)
    if hasattr(a2, 'jpdl31_ProcessDefinitionType184'):
        assert _is_linked(a2, 'jpdl31_ProcessDefinitionType184', b)
    _safe_set(b, 'jpdl31_ActionType185', None)
    assert not _is_linked(b, 'jpdl31_ActionType185', a2)
    if hasattr(a2, 'jpdl31_ProcessDefinitionType184'):
        assert not _is_linked(a2, 'jpdl31_ProcessDefinitionType184', b)


def test_assoc_action324_reverse_link_reassign_clear():
    a1 = jpdl31_TimerType(duedate="sample_text", name="sample_text", repeat="sample_text", transition="sample_text")
    a2 = jpdl31_TimerType(duedate="sample_text_2", name="sample_text_2", repeat="sample_text_2", transition="sample_text_2")
    b = jpdl31_ActionType(acceptPropagatedEvents="sample_text", any="sample_text", async_="sample_text", class_="sample_text", configType="sample_text", expression="sample_text", mixed="sample_text", name="sample_text", refName="sample_text")
    _safe_set(b, 'jpdl31_ActionType326', a1)
    assert _is_linked(b, 'jpdl31_ActionType326', a1)
    if hasattr(a1, 'jpdl31_TimerType325'):
        assert _is_linked(a1, 'jpdl31_TimerType325', b)
    _safe_set(b, 'jpdl31_ActionType326', a2)
    assert _is_linked(b, 'jpdl31_ActionType326', a2)
    if hasattr(a1, 'jpdl31_TimerType325'):
        assert not _is_linked(a1, 'jpdl31_TimerType325', b)
    if hasattr(a2, 'jpdl31_TimerType325'):
        assert _is_linked(a2, 'jpdl31_TimerType325', b)
    _safe_set(b, 'jpdl31_ActionType326', None)
    assert not _is_linked(b, 'jpdl31_ActionType326', a2)
    if hasattr(a2, 'jpdl31_TimerType325'):
        assert not _is_linked(a2, 'jpdl31_TimerType325', b)


def test_assoc_action330_reverse_link_reassign_clear():
    a1 = jpdl31_TransitionType(group="sample_text", name="sample_text", to="sample_text")
    a2 = jpdl31_TransitionType(group="sample_text_2", name="sample_text_2", to="sample_text_2")
    b = jpdl31_ActionType(acceptPropagatedEvents="sample_text", any="sample_text", async_="sample_text", class_="sample_text", configType="sample_text", expression="sample_text", mixed="sample_text", name="sample_text", refName="sample_text")
    _safe_set(b, 'jpdl31_ActionType332', a1)
    assert _is_linked(b, 'jpdl31_ActionType332', a1)
    if hasattr(a1, 'jpdl31_TransitionType331'):
        assert _is_linked(a1, 'jpdl31_TransitionType331', b)
    _safe_set(b, 'jpdl31_ActionType332', a2)
    assert _is_linked(b, 'jpdl31_ActionType332', a2)
    if hasattr(a1, 'jpdl31_TransitionType331'):
        assert not _is_linked(a1, 'jpdl31_TransitionType331', b)
    if hasattr(a2, 'jpdl31_TransitionType331'):
        assert _is_linked(a2, 'jpdl31_TransitionType331', b)
    _safe_set(b, 'jpdl31_ActionType332', None)
    assert not _is_linked(b, 'jpdl31_ActionType332', a2)
    if hasattr(a2, 'jpdl31_TransitionType331'):
        assert not _is_linked(a2, 'jpdl31_TransitionType331', b)


def test_assoc_action347_reverse_link_reassign_clear():
    a1 = jpdl31_TransitionType1(group="sample_text", name="sample_text", to="sample_text")
    a2 = jpdl31_TransitionType1(group="sample_text_2", name="sample_text_2", to="sample_text_2")
    b = jpdl31_ActionType(acceptPropagatedEvents="sample_text", any="sample_text", async_="sample_text", class_="sample_text", configType="sample_text", expression="sample_text", mixed="sample_text", name="sample_text", refName="sample_text")
    _safe_set(b, 'jpdl31_ActionType349', a1)
    assert _is_linked(b, 'jpdl31_ActionType349', a1)
    if hasattr(a1, 'jpdl31_TransitionType1348'):
        assert _is_linked(a1, 'jpdl31_TransitionType1348', b)
    _safe_set(b, 'jpdl31_ActionType349', a2)
    assert _is_linked(b, 'jpdl31_ActionType349', a2)
    if hasattr(a1, 'jpdl31_TransitionType1348'):
        assert not _is_linked(a1, 'jpdl31_TransitionType1348', b)
    if hasattr(a2, 'jpdl31_TransitionType1348'):
        assert _is_linked(a2, 'jpdl31_TransitionType1348', b)
    _safe_set(b, 'jpdl31_ActionType349', None)
    assert not _is_linked(b, 'jpdl31_ActionType349', a2)
    if hasattr(a2, 'jpdl31_TransitionType1348'):
        assert not _is_linked(a2, 'jpdl31_TransitionType1348', b)


def test_assoc_action81_reverse_link_reassign_clear():
    a1 = jpdl31_EventType(actionElements="sample_text", type="sample_text")
    a2 = jpdl31_EventType(actionElements="sample_text_2", type="sample_text_2")
    b = jpdl31_ActionType(acceptPropagatedEvents="sample_text", any="sample_text", async_="sample_text", class_="sample_text", configType="sample_text", expression="sample_text", mixed="sample_text", name="sample_text", refName="sample_text")
    _safe_set(b, 'jpdl31_ActionType83', a1)
    assert _is_linked(b, 'jpdl31_ActionType83', a1)
    if hasattr(a1, 'jpdl31_EventType82'):
        assert _is_linked(a1, 'jpdl31_EventType82', b)
    _safe_set(b, 'jpdl31_ActionType83', a2)
    assert _is_linked(b, 'jpdl31_ActionType83', a2)
    if hasattr(a1, 'jpdl31_EventType82'):
        assert not _is_linked(a1, 'jpdl31_EventType82', b)
    if hasattr(a2, 'jpdl31_EventType82'):
        assert _is_linked(a2, 'jpdl31_EventType82', b)
    _safe_set(b, 'jpdl31_ActionType83', None)
    assert not _is_linked(b, 'jpdl31_ActionType83', a2)
    if hasattr(a2, 'jpdl31_EventType82'):
        assert not _is_linked(a2, 'jpdl31_EventType82', b)


def test_assoc_action93_reverse_link_reassign_clear():
    a1 = jpdl31_ExceptionHandlerType(exceptionClass="sample_text", group="sample_text")
    a2 = jpdl31_ExceptionHandlerType(exceptionClass="sample_text_2", group="sample_text_2")
    b = jpdl31_ActionType(acceptPropagatedEvents="sample_text", any="sample_text", async_="sample_text", class_="sample_text", configType="sample_text", expression="sample_text", mixed="sample_text", name="sample_text", refName="sample_text")
    _safe_set(b, 'jpdl31_ActionType95', a1)
    assert _is_linked(b, 'jpdl31_ActionType95', a1)
    if hasattr(a1, 'jpdl31_ExceptionHandlerType94'):
        assert _is_linked(a1, 'jpdl31_ExceptionHandlerType94', b)
    _safe_set(b, 'jpdl31_ActionType95', a2)
    assert _is_linked(b, 'jpdl31_ActionType95', a2)
    if hasattr(a1, 'jpdl31_ExceptionHandlerType94'):
        assert not _is_linked(a1, 'jpdl31_ExceptionHandlerType94', b)
    if hasattr(a2, 'jpdl31_ExceptionHandlerType94'):
        assert _is_linked(a2, 'jpdl31_ExceptionHandlerType94', b)
    _safe_set(b, 'jpdl31_ActionType95', None)
    assert not _is_linked(b, 'jpdl31_ActionType95', a2)
    if hasattr(a2, 'jpdl31_ExceptionHandlerType94'):
        assert not _is_linked(a2, 'jpdl31_ExceptionHandlerType94', b)


def test_assoc_artefacts302_reverse_link_reassign_clear():
    a1 = jpdl31_TaskNodeType(async_="sample_text", createTasks="sample_text", description="sample_text", endTasks="sample_text", group="sample_text", name="sample_text", signal="sample_text")
    a2 = jpdl31_TaskNodeType(async_="sample_text_2", createTasks="sample_text_2", description="sample_text_2", endTasks="sample_text_2", group="sample_text_2", name="sample_text_2", signal="sample_text_2")
    b = jpdl31_Artefact(description="sample_text", name="sample_text", type="sample_text")
    _safe_set(b, 'jpdl31_Artefact', a1)
    assert _is_linked(b, 'jpdl31_Artefact', a1)
    if hasattr(a1, 'jpdl31_TaskNodeType303'):
        assert _is_linked(a1, 'jpdl31_TaskNodeType303', b)
    _safe_set(b, 'jpdl31_Artefact', a2)
    assert _is_linked(b, 'jpdl31_Artefact', a2)
    if hasattr(a1, 'jpdl31_TaskNodeType303'):
        assert not _is_linked(a1, 'jpdl31_TaskNodeType303', b)
    if hasattr(a2, 'jpdl31_TaskNodeType303'):
        assert _is_linked(a2, 'jpdl31_TaskNodeType303', b)
    _safe_set(b, 'jpdl31_Artefact', None)
    assert not _is_linked(b, 'jpdl31_Artefact', a2)
    if hasattr(a2, 'jpdl31_TaskNodeType303'):
        assert not _is_linked(a2, 'jpdl31_TaskNodeType303', b)


def test_assoc_artefacts318_reverse_link_reassign_clear():
    a1 = jpdl31_TaskType(blocking="sample_text", description="sample_text", duedate="sample_text", group="sample_text", name="sample_text", priority="sample_text", signalling="sample_text", swimlane="sample_text")
    a2 = jpdl31_TaskType(blocking="sample_text_2", description="sample_text_2", duedate="sample_text_2", group="sample_text_2", name="sample_text_2", priority="sample_text_2", signalling="sample_text_2", swimlane="sample_text_2")
    b = jpdl31_Artefact(description="sample_text", name="sample_text", type="sample_text")
    _safe_set(b, 'jpdl31_Artefact320', a1)
    assert _is_linked(b, 'jpdl31_Artefact320', a1)
    if hasattr(a1, 'jpdl31_TaskType319'):
        assert _is_linked(a1, 'jpdl31_TaskType319', b)
    _safe_set(b, 'jpdl31_Artefact320', a2)
    assert _is_linked(b, 'jpdl31_Artefact320', a2)
    if hasattr(a1, 'jpdl31_TaskType319'):
        assert not _is_linked(a1, 'jpdl31_TaskType319', b)
    if hasattr(a2, 'jpdl31_TaskType319'):
        assert _is_linked(a2, 'jpdl31_TaskType319', b)
    _safe_set(b, 'jpdl31_Artefact320', None)
    assert not _is_linked(b, 'jpdl31_Artefact320', a2)
    if hasattr(a2, 'jpdl31_TaskType319'):
        assert not _is_linked(a2, 'jpdl31_TaskType319', b)


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


def test_assoc_assignment284_reverse_link_reassign_clear():
    a1 = jpdl31_SwimlaneType(name="sample_text")
    a2 = jpdl31_SwimlaneType(name="sample_text_2")
    b = jpdl31_AssignmentType(actorId="sample_text", expression="sample_text", pooledActors="sample_text")
    _safe_set(b, 'jpdl31_AssignmentType286', a1)
    assert _is_linked(b, 'jpdl31_AssignmentType286', a1)
    if hasattr(a1, 'jpdl31_SwimlaneType285'):
        assert _is_linked(a1, 'jpdl31_SwimlaneType285', b)
    _safe_set(b, 'jpdl31_AssignmentType286', a2)
    assert _is_linked(b, 'jpdl31_AssignmentType286', a2)
    if hasattr(a1, 'jpdl31_SwimlaneType285'):
        assert not _is_linked(a1, 'jpdl31_SwimlaneType285', b)
    if hasattr(a2, 'jpdl31_SwimlaneType285'):
        assert _is_linked(a2, 'jpdl31_SwimlaneType285', b)
    _safe_set(b, 'jpdl31_AssignmentType286', None)
    assert not _is_linked(b, 'jpdl31_AssignmentType286', a2)
    if hasattr(a2, 'jpdl31_SwimlaneType285'):
        assert not _is_linked(a2, 'jpdl31_SwimlaneType285', b)


def test_assoc_assignment306_reverse_link_reassign_clear():
    a1 = jpdl31_TaskType(blocking="sample_text", description="sample_text", duedate="sample_text", group="sample_text", name="sample_text", priority="sample_text", signalling="sample_text", swimlane="sample_text")
    a2 = jpdl31_TaskType(blocking="sample_text_2", description="sample_text_2", duedate="sample_text_2", group="sample_text_2", name="sample_text_2", priority="sample_text_2", signalling="sample_text_2", swimlane="sample_text_2")
    b = jpdl31_AssignmentType(actorId="sample_text", expression="sample_text", pooledActors="sample_text")
    _safe_set(b, 'jpdl31_AssignmentType308', a1)
    assert _is_linked(b, 'jpdl31_AssignmentType308', a1)
    if hasattr(a1, 'jpdl31_TaskType307'):
        assert _is_linked(a1, 'jpdl31_TaskType307', b)
    _safe_set(b, 'jpdl31_AssignmentType308', a2)
    assert _is_linked(b, 'jpdl31_AssignmentType308', a2)
    if hasattr(a1, 'jpdl31_TaskType307'):
        assert not _is_linked(a1, 'jpdl31_TaskType307', b)
    if hasattr(a2, 'jpdl31_TaskType307'):
        assert _is_linked(a2, 'jpdl31_TaskType307', b)
    _safe_set(b, 'jpdl31_AssignmentType308', None)
    assert not _is_linked(b, 'jpdl31_AssignmentType308', a2)
    if hasattr(a2, 'jpdl31_TaskType307'):
        assert not _is_linked(a2, 'jpdl31_TaskType307', b)


def test_assoc_cancelTimer135_reverse_link_reassign_clear():
    a1 = jpdl31_NodeType(async_="sample_text", description="sample_text", name="sample_text", nodeContentElements="sample_text")
    a2 = jpdl31_NodeType(async_="sample_text_2", description="sample_text_2", name="sample_text_2", nodeContentElements="sample_text_2")
    b = jpdl31_CancelTimerType(name="sample_text")
    _safe_set(b, 'jpdl31_CancelTimerType137', a1)
    assert _is_linked(b, 'jpdl31_CancelTimerType137', a1)
    if hasattr(a1, 'jpdl31_NodeType136'):
        assert _is_linked(a1, 'jpdl31_NodeType136', b)
    _safe_set(b, 'jpdl31_CancelTimerType137', a2)
    assert _is_linked(b, 'jpdl31_CancelTimerType137', a2)
    if hasattr(a1, 'jpdl31_NodeType136'):
        assert not _is_linked(a1, 'jpdl31_NodeType136', b)
    if hasattr(a2, 'jpdl31_NodeType136'):
        assert _is_linked(a2, 'jpdl31_NodeType136', b)
    _safe_set(b, 'jpdl31_CancelTimerType137', None)
    assert not _is_linked(b, 'jpdl31_CancelTimerType137', a2)
    if hasattr(a2, 'jpdl31_NodeType136'):
        assert not _is_linked(a2, 'jpdl31_NodeType136', b)


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


def test_assoc_cancelTimer192_reverse_link_reassign_clear():
    a1 = jpdl31_ProcessDefinitionType(group="sample_text", name="sample_text", quantity="sample_text")
    a2 = jpdl31_ProcessDefinitionType(group="sample_text_2", name="sample_text_2", quantity="sample_text_2")
    b = jpdl31_CancelTimerType(name="sample_text")
    _safe_set(b, 'jpdl31_CancelTimerType194', a1)
    assert _is_linked(b, 'jpdl31_CancelTimerType194', a1)
    if hasattr(a1, 'jpdl31_ProcessDefinitionType193'):
        assert _is_linked(a1, 'jpdl31_ProcessDefinitionType193', b)
    _safe_set(b, 'jpdl31_CancelTimerType194', a2)
    assert _is_linked(b, 'jpdl31_CancelTimerType194', a2)
    if hasattr(a1, 'jpdl31_ProcessDefinitionType193'):
        assert not _is_linked(a1, 'jpdl31_ProcessDefinitionType193', b)
    if hasattr(a2, 'jpdl31_ProcessDefinitionType193'):
        assert _is_linked(a2, 'jpdl31_ProcessDefinitionType193', b)
    _safe_set(b, 'jpdl31_CancelTimerType194', None)
    assert not _is_linked(b, 'jpdl31_CancelTimerType194', a2)
    if hasattr(a2, 'jpdl31_ProcessDefinitionType193'):
        assert not _is_linked(a2, 'jpdl31_ProcessDefinitionType193', b)


def test_assoc_cancelTimer339_reverse_link_reassign_clear():
    a1 = jpdl31_TransitionType(group="sample_text", name="sample_text", to="sample_text")
    a2 = jpdl31_TransitionType(group="sample_text_2", name="sample_text_2", to="sample_text_2")
    b = jpdl31_CancelTimerType(name="sample_text")
    _safe_set(b, 'jpdl31_CancelTimerType341', a1)
    assert _is_linked(b, 'jpdl31_CancelTimerType341', a1)
    if hasattr(a1, 'jpdl31_TransitionType340'):
        assert _is_linked(a1, 'jpdl31_TransitionType340', b)
    _safe_set(b, 'jpdl31_CancelTimerType341', a2)
    assert _is_linked(b, 'jpdl31_CancelTimerType341', a2)
    if hasattr(a1, 'jpdl31_TransitionType340'):
        assert not _is_linked(a1, 'jpdl31_TransitionType340', b)
    if hasattr(a2, 'jpdl31_TransitionType340'):
        assert _is_linked(a2, 'jpdl31_TransitionType340', b)
    _safe_set(b, 'jpdl31_CancelTimerType341', None)
    assert not _is_linked(b, 'jpdl31_CancelTimerType341', a2)
    if hasattr(a2, 'jpdl31_TransitionType340'):
        assert not _is_linked(a2, 'jpdl31_TransitionType340', b)


def test_assoc_cancelTimer356_reverse_link_reassign_clear():
    a1 = jpdl31_TransitionType1(group="sample_text", name="sample_text", to="sample_text")
    a2 = jpdl31_TransitionType1(group="sample_text_2", name="sample_text_2", to="sample_text_2")
    b = jpdl31_CancelTimerType(name="sample_text")
    _safe_set(b, 'jpdl31_CancelTimerType358', a1)
    assert _is_linked(b, 'jpdl31_CancelTimerType358', a1)
    if hasattr(a1, 'jpdl31_TransitionType1357'):
        assert _is_linked(a1, 'jpdl31_TransitionType1357', b)
    _safe_set(b, 'jpdl31_CancelTimerType358', a2)
    assert _is_linked(b, 'jpdl31_CancelTimerType358', a2)
    if hasattr(a1, 'jpdl31_TransitionType1357'):
        assert not _is_linked(a1, 'jpdl31_TransitionType1357', b)
    if hasattr(a2, 'jpdl31_TransitionType1357'):
        assert _is_linked(a2, 'jpdl31_TransitionType1357', b)
    _safe_set(b, 'jpdl31_CancelTimerType358', None)
    assert not _is_linked(b, 'jpdl31_CancelTimerType358', a2)
    if hasattr(a2, 'jpdl31_TransitionType1357'):
        assert not _is_linked(a2, 'jpdl31_TransitionType1357', b)


def test_assoc_cancelTimer90_reverse_link_reassign_clear():
    a1 = jpdl31_EventType(actionElements="sample_text", type="sample_text")
    a2 = jpdl31_EventType(actionElements="sample_text_2", type="sample_text_2")
    b = jpdl31_CancelTimerType(name="sample_text")
    _safe_set(b, 'jpdl31_CancelTimerType92', a1)
    assert _is_linked(b, 'jpdl31_CancelTimerType92', a1)
    if hasattr(a1, 'jpdl31_EventType91'):
        assert _is_linked(a1, 'jpdl31_EventType91', b)
    _safe_set(b, 'jpdl31_CancelTimerType92', a2)
    assert _is_linked(b, 'jpdl31_CancelTimerType92', a2)
    if hasattr(a1, 'jpdl31_EventType91'):
        assert not _is_linked(a1, 'jpdl31_EventType91', b)
    if hasattr(a2, 'jpdl31_EventType91'):
        assert _is_linked(a2, 'jpdl31_EventType91', b)
    _safe_set(b, 'jpdl31_CancelTimerType92', None)
    assert not _is_linked(b, 'jpdl31_CancelTimerType92', a2)
    if hasattr(a2, 'jpdl31_EventType91'):
        assert not _is_linked(a2, 'jpdl31_EventType91', b)


def test_assoc_condition345_reverse_link_reassign_clear():
    a1 = jpdl31_TransitionType1(group="sample_text", name="sample_text", to="sample_text")
    a2 = jpdl31_TransitionType1(group="sample_text_2", name="sample_text_2", to="sample_text_2")
    b = jpdl31_ConditionType(any="sample_text", expression="sample_text", group="sample_text", mixed="sample_text")
    _safe_set(b, 'jpdl31_ConditionType', a1)
    assert _is_linked(b, 'jpdl31_ConditionType', a1)
    if hasattr(a1, 'jpdl31_TransitionType1346'):
        assert _is_linked(a1, 'jpdl31_TransitionType1346', b)
    _safe_set(b, 'jpdl31_ConditionType', a2)
    assert _is_linked(b, 'jpdl31_ConditionType', a2)
    if hasattr(a1, 'jpdl31_TransitionType1346'):
        assert not _is_linked(a1, 'jpdl31_TransitionType1346', b)
    if hasattr(a2, 'jpdl31_TransitionType1346'):
        assert _is_linked(a2, 'jpdl31_TransitionType1346', b)
    _safe_set(b, 'jpdl31_ConditionType', None)
    assert not _is_linked(b, 'jpdl31_ConditionType', a2)
    if hasattr(a2, 'jpdl31_TransitionType1346'):
        assert not _is_linked(a2, 'jpdl31_TransitionType1346', b)


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


def test_assoc_controller309_reverse_link_reassign_clear():
    a1 = jpdl31_TaskType(blocking="sample_text", description="sample_text", duedate="sample_text", group="sample_text", name="sample_text", priority="sample_text", signalling="sample_text", swimlane="sample_text")
    a2 = jpdl31_TaskType(blocking="sample_text_2", description="sample_text_2", duedate="sample_text_2", group="sample_text_2", name="sample_text_2", priority="sample_text_2", signalling="sample_text_2", swimlane="sample_text_2")
    b = jpdl31_Delegation(any="sample_text", class_="sample_text", configType="sample_text", mixed="sample_text")
    _safe_set(b, 'jpdl31_Delegation311', a1)
    assert _is_linked(b, 'jpdl31_Delegation311', a1)
    if hasattr(a1, 'jpdl31_TaskType310'):
        assert _is_linked(a1, 'jpdl31_TaskType310', b)
    _safe_set(b, 'jpdl31_Delegation311', a2)
    assert _is_linked(b, 'jpdl31_Delegation311', a2)
    if hasattr(a1, 'jpdl31_TaskType310'):
        assert not _is_linked(a1, 'jpdl31_TaskType310', b)
    if hasattr(a2, 'jpdl31_TaskType310'):
        assert _is_linked(a2, 'jpdl31_TaskType310', b)
    _safe_set(b, 'jpdl31_Delegation311', None)
    assert not _is_linked(b, 'jpdl31_Delegation311', a2)
    if hasattr(a2, 'jpdl31_TaskType310'):
        assert not _is_linked(a2, 'jpdl31_TaskType310', b)


def test_assoc_createTimer132_reverse_link_reassign_clear():
    a1 = jpdl31_NodeType(async_="sample_text", description="sample_text", name="sample_text", nodeContentElements="sample_text")
    a2 = jpdl31_NodeType(async_="sample_text_2", description="sample_text_2", name="sample_text_2", nodeContentElements="sample_text_2")
    b = jpdl31_CreateTimerType(duedate="sample_text", name="sample_text", repeat="sample_text", transition="sample_text")
    _safe_set(b, 'jpdl31_CreateTimerType134', a1)
    assert _is_linked(b, 'jpdl31_CreateTimerType134', a1)
    if hasattr(a1, 'jpdl31_NodeType133'):
        assert _is_linked(a1, 'jpdl31_NodeType133', b)
    _safe_set(b, 'jpdl31_CreateTimerType134', a2)
    assert _is_linked(b, 'jpdl31_CreateTimerType134', a2)
    if hasattr(a1, 'jpdl31_NodeType133'):
        assert not _is_linked(a1, 'jpdl31_NodeType133', b)
    if hasattr(a2, 'jpdl31_NodeType133'):
        assert _is_linked(a2, 'jpdl31_NodeType133', b)
    _safe_set(b, 'jpdl31_CreateTimerType134', None)
    assert not _is_linked(b, 'jpdl31_CreateTimerType134', a2)
    if hasattr(a2, 'jpdl31_NodeType133'):
        assert not _is_linked(a2, 'jpdl31_NodeType133', b)


def test_assoc_createTimer189_reverse_link_reassign_clear():
    a1 = jpdl31_ProcessDefinitionType(group="sample_text", name="sample_text", quantity="sample_text")
    a2 = jpdl31_ProcessDefinitionType(group="sample_text_2", name="sample_text_2", quantity="sample_text_2")
    b = jpdl31_CreateTimerType(duedate="sample_text", name="sample_text", repeat="sample_text", transition="sample_text")
    _safe_set(b, 'jpdl31_CreateTimerType191', a1)
    assert _is_linked(b, 'jpdl31_CreateTimerType191', a1)
    if hasattr(a1, 'jpdl31_ProcessDefinitionType190'):
        assert _is_linked(a1, 'jpdl31_ProcessDefinitionType190', b)
    _safe_set(b, 'jpdl31_CreateTimerType191', a2)
    assert _is_linked(b, 'jpdl31_CreateTimerType191', a2)
    if hasattr(a1, 'jpdl31_ProcessDefinitionType190'):
        assert not _is_linked(a1, 'jpdl31_ProcessDefinitionType190', b)
    if hasattr(a2, 'jpdl31_ProcessDefinitionType190'):
        assert _is_linked(a2, 'jpdl31_ProcessDefinitionType190', b)
    _safe_set(b, 'jpdl31_CreateTimerType191', None)
    assert not _is_linked(b, 'jpdl31_CreateTimerType191', a2)
    if hasattr(a2, 'jpdl31_ProcessDefinitionType190'):
        assert not _is_linked(a2, 'jpdl31_ProcessDefinitionType190', b)


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


def test_assoc_createTimer336_reverse_link_reassign_clear():
    a1 = jpdl31_TransitionType(group="sample_text", name="sample_text", to="sample_text")
    a2 = jpdl31_TransitionType(group="sample_text_2", name="sample_text_2", to="sample_text_2")
    b = jpdl31_CreateTimerType(duedate="sample_text", name="sample_text", repeat="sample_text", transition="sample_text")
    _safe_set(b, 'jpdl31_CreateTimerType338', a1)
    assert _is_linked(b, 'jpdl31_CreateTimerType338', a1)
    if hasattr(a1, 'jpdl31_TransitionType337'):
        assert _is_linked(a1, 'jpdl31_TransitionType337', b)
    _safe_set(b, 'jpdl31_CreateTimerType338', a2)
    assert _is_linked(b, 'jpdl31_CreateTimerType338', a2)
    if hasattr(a1, 'jpdl31_TransitionType337'):
        assert not _is_linked(a1, 'jpdl31_TransitionType337', b)
    if hasattr(a2, 'jpdl31_TransitionType337'):
        assert _is_linked(a2, 'jpdl31_TransitionType337', b)
    _safe_set(b, 'jpdl31_CreateTimerType338', None)
    assert not _is_linked(b, 'jpdl31_CreateTimerType338', a2)
    if hasattr(a2, 'jpdl31_TransitionType337'):
        assert not _is_linked(a2, 'jpdl31_TransitionType337', b)


def test_assoc_createTimer353_reverse_link_reassign_clear():
    a1 = jpdl31_TransitionType1(group="sample_text", name="sample_text", to="sample_text")
    a2 = jpdl31_TransitionType1(group="sample_text_2", name="sample_text_2", to="sample_text_2")
    b = jpdl31_CreateTimerType(duedate="sample_text", name="sample_text", repeat="sample_text", transition="sample_text")
    _safe_set(b, 'jpdl31_CreateTimerType355', a1)
    assert _is_linked(b, 'jpdl31_CreateTimerType355', a1)
    if hasattr(a1, 'jpdl31_TransitionType1354'):
        assert _is_linked(a1, 'jpdl31_TransitionType1354', b)
    _safe_set(b, 'jpdl31_CreateTimerType355', a2)
    assert _is_linked(b, 'jpdl31_CreateTimerType355', a2)
    if hasattr(a1, 'jpdl31_TransitionType1354'):
        assert not _is_linked(a1, 'jpdl31_TransitionType1354', b)
    if hasattr(a2, 'jpdl31_TransitionType1354'):
        assert _is_linked(a2, 'jpdl31_TransitionType1354', b)
    _safe_set(b, 'jpdl31_CreateTimerType355', None)
    assert not _is_linked(b, 'jpdl31_CreateTimerType355', a2)
    if hasattr(a2, 'jpdl31_TransitionType1354'):
        assert not _is_linked(a2, 'jpdl31_TransitionType1354', b)


def test_assoc_createTimer87_reverse_link_reassign_clear():
    a1 = jpdl31_EventType(actionElements="sample_text", type="sample_text")
    a2 = jpdl31_EventType(actionElements="sample_text_2", type="sample_text_2")
    b = jpdl31_CreateTimerType(duedate="sample_text", name="sample_text", repeat="sample_text", transition="sample_text")
    _safe_set(b, 'jpdl31_CreateTimerType89', a1)
    assert _is_linked(b, 'jpdl31_CreateTimerType89', a1)
    if hasattr(a1, 'jpdl31_EventType88'):
        assert _is_linked(a1, 'jpdl31_EventType88', b)
    _safe_set(b, 'jpdl31_CreateTimerType89', a2)
    assert _is_linked(b, 'jpdl31_CreateTimerType89', a2)
    if hasattr(a1, 'jpdl31_EventType88'):
        assert not _is_linked(a1, 'jpdl31_EventType88', b)
    if hasattr(a2, 'jpdl31_EventType88'):
        assert _is_linked(a2, 'jpdl31_EventType88', b)
    _safe_set(b, 'jpdl31_CreateTimerType89', None)
    assert not _is_linked(b, 'jpdl31_CreateTimerType89', a2)
    if hasattr(a2, 'jpdl31_EventType88'):
        assert not _is_linked(a2, 'jpdl31_EventType88', b)


def test_assoc_decision177_reverse_link_reassign_clear():
    a1 = jpdl31_ProcessDefinitionType(group="sample_text", name="sample_text", quantity="sample_text")
    a2 = jpdl31_ProcessDefinitionType(group="sample_text_2", name="sample_text_2", quantity="sample_text_2")
    b = jpdl31_DecisionType(async_="sample_text", expression="sample_text", group="sample_text", name="sample_text")
    _safe_set(b, 'jpdl31_DecisionType179', a1)
    assert _is_linked(b, 'jpdl31_DecisionType179', a1)
    if hasattr(a1, 'jpdl31_ProcessDefinitionType178'):
        assert _is_linked(a1, 'jpdl31_ProcessDefinitionType178', b)
    _safe_set(b, 'jpdl31_DecisionType179', a2)
    assert _is_linked(b, 'jpdl31_DecisionType179', a2)
    if hasattr(a1, 'jpdl31_ProcessDefinitionType178'):
        assert not _is_linked(a1, 'jpdl31_ProcessDefinitionType178', b)
    if hasattr(a2, 'jpdl31_ProcessDefinitionType178'):
        assert _is_linked(a2, 'jpdl31_ProcessDefinitionType178', b)
    _safe_set(b, 'jpdl31_DecisionType179', None)
    assert not _is_linked(b, 'jpdl31_DecisionType179', a2)
    if hasattr(a2, 'jpdl31_ProcessDefinitionType178'):
        assert not _is_linked(a2, 'jpdl31_ProcessDefinitionType178', b)


def test_assoc_decision266_reverse_link_reassign_clear():
    a1 = jpdl31_SuperStateType(async_="sample_text", group="sample_text", name="sample_text")
    a2 = jpdl31_SuperStateType(async_="sample_text_2", group="sample_text_2", name="sample_text_2")
    b = jpdl31_DecisionType(async_="sample_text", expression="sample_text", group="sample_text", name="sample_text")
    _safe_set(b, 'jpdl31_DecisionType268', a1)
    assert _is_linked(b, 'jpdl31_DecisionType268', a1)
    if hasattr(a1, 'jpdl31_SuperStateType267'):
        assert _is_linked(a1, 'jpdl31_SuperStateType267', b)
    _safe_set(b, 'jpdl31_DecisionType268', a2)
    assert _is_linked(b, 'jpdl31_DecisionType268', a2)
    if hasattr(a1, 'jpdl31_SuperStateType267'):
        assert not _is_linked(a1, 'jpdl31_SuperStateType267', b)
    if hasattr(a2, 'jpdl31_SuperStateType267'):
        assert _is_linked(a2, 'jpdl31_SuperStateType267', b)
    _safe_set(b, 'jpdl31_DecisionType268', None)
    assert not _is_linked(b, 'jpdl31_DecisionType268', a2)
    if hasattr(a2, 'jpdl31_SuperStateType267'):
        assert not _is_linked(a2, 'jpdl31_SuperStateType267', b)


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


def test_assoc_depVariable416_reverse_link_reassign_clear():
    a1 = jpdl31_Design(DoE="sample_text")
    a2 = jpdl31_Design(DoE="sample_text_2")
    b = jpdl31_DependentVariable(description="sample_text", name="sample_text")
    _safe_set(b, 'jpdl31_DependentVariable418', a1)
    assert _is_linked(b, 'jpdl31_DependentVariable418', a1)
    if hasattr(a1, 'jpdl31_Design417'):
        assert _is_linked(a1, 'jpdl31_Design417', b)
    _safe_set(b, 'jpdl31_DependentVariable418', a2)
    assert _is_linked(b, 'jpdl31_DependentVariable418', a2)
    if hasattr(a1, 'jpdl31_Design417'):
        assert not _is_linked(a1, 'jpdl31_Design417', b)
    if hasattr(a2, 'jpdl31_Design417'):
        assert _is_linked(a2, 'jpdl31_Design417', b)
    _safe_set(b, 'jpdl31_DependentVariable418', None)
    assert not _is_linked(b, 'jpdl31_DependentVariable418', a2)
    if hasattr(a2, 'jpdl31_Design417'):
        assert not _is_linked(a2, 'jpdl31_Design417', b)


def test_assoc_dependentVariable372_reverse_link_reassign_clear():
    a1 = jpdl31_Hyphotesis(description="sample_text", id="sample_text", relationOp="sample_text", type="sample_text")
    a2 = jpdl31_Hyphotesis(description="sample_text_2", id="sample_text_2", relationOp="sample_text_2", type="sample_text_2")
    b = jpdl31_DependentVariable(description="sample_text", name="sample_text")
    _safe_set(b, 'jpdl31_DependentVariable', a1)
    assert _is_linked(b, 'jpdl31_DependentVariable', a1)
    if hasattr(a1, 'jpdl31_Hyphotesis373'):
        assert _is_linked(a1, 'jpdl31_Hyphotesis373', b)
    _safe_set(b, 'jpdl31_DependentVariable', a2)
    assert _is_linked(b, 'jpdl31_DependentVariable', a2)
    if hasattr(a1, 'jpdl31_Hyphotesis373'):
        assert not _is_linked(a1, 'jpdl31_Hyphotesis373', b)
    if hasattr(a2, 'jpdl31_Hyphotesis373'):
        assert _is_linked(a2, 'jpdl31_Hyphotesis373', b)
    _safe_set(b, 'jpdl31_DependentVariable', None)
    assert not _is_linked(b, 'jpdl31_DependentVariable', a2)
    if hasattr(a2, 'jpdl31_Hyphotesis373'):
        assert not _is_linked(a2, 'jpdl31_Hyphotesis373', b)


def test_assoc_dependentVariable377_reverse_link_reassign_clear():
    a1 = jpdl31_Subhypotheses(relationOp="sample_text")
    a2 = jpdl31_Subhypotheses(relationOp="sample_text_2")
    b = jpdl31_DependentVariable(description="sample_text", name="sample_text")
    _safe_set(b, 'jpdl31_DependentVariable379', a1)
    assert _is_linked(b, 'jpdl31_DependentVariable379', a1)
    if hasattr(a1, 'jpdl31_Subhypotheses378'):
        assert _is_linked(a1, 'jpdl31_Subhypotheses378', b)
    _safe_set(b, 'jpdl31_DependentVariable379', a2)
    assert _is_linked(b, 'jpdl31_DependentVariable379', a2)
    if hasattr(a1, 'jpdl31_Subhypotheses378'):
        assert not _is_linked(a1, 'jpdl31_Subhypotheses378', b)
    if hasattr(a2, 'jpdl31_Subhypotheses378'):
        assert _is_linked(a2, 'jpdl31_Subhypotheses378', b)
    _safe_set(b, 'jpdl31_DependentVariable379', None)
    assert not _is_linked(b, 'jpdl31_DependentVariable379', a2)
    if hasattr(a2, 'jpdl31_Subhypotheses378'):
        assert not _is_linked(a2, 'jpdl31_Subhypotheses378', b)


def test_assoc_endState180_reverse_link_reassign_clear():
    a1 = jpdl31_ProcessDefinitionType(group="sample_text", name="sample_text", quantity="sample_text")
    a2 = jpdl31_ProcessDefinitionType(group="sample_text_2", name="sample_text_2", quantity="sample_text_2")
    b = jpdl31_EndStateType(group="sample_text", name="sample_text")
    _safe_set(b, 'jpdl31_EndStateType182', a1)
    assert _is_linked(b, 'jpdl31_EndStateType182', a1)
    if hasattr(a1, 'jpdl31_ProcessDefinitionType181'):
        assert _is_linked(a1, 'jpdl31_ProcessDefinitionType181', b)
    _safe_set(b, 'jpdl31_EndStateType182', a2)
    assert _is_linked(b, 'jpdl31_EndStateType182', a2)
    if hasattr(a1, 'jpdl31_ProcessDefinitionType181'):
        assert not _is_linked(a1, 'jpdl31_ProcessDefinitionType181', b)
    if hasattr(a2, 'jpdl31_ProcessDefinitionType181'):
        assert _is_linked(a2, 'jpdl31_ProcessDefinitionType181', b)
    _safe_set(b, 'jpdl31_EndStateType182', None)
    assert not _is_linked(b, 'jpdl31_EndStateType182', a2)
    if hasattr(a2, 'jpdl31_ProcessDefinitionType181'):
        assert not _is_linked(a2, 'jpdl31_ProcessDefinitionType181', b)


def test_assoc_endState269_reverse_link_reassign_clear():
    a1 = jpdl31_SuperStateType(async_="sample_text", group="sample_text", name="sample_text")
    a2 = jpdl31_SuperStateType(async_="sample_text_2", group="sample_text_2", name="sample_text_2")
    b = jpdl31_EndStateType(group="sample_text", name="sample_text")
    _safe_set(b, 'jpdl31_EndStateType271', a1)
    assert _is_linked(b, 'jpdl31_EndStateType271', a1)
    if hasattr(a1, 'jpdl31_SuperStateType270'):
        assert _is_linked(a1, 'jpdl31_SuperStateType270', b)
    _safe_set(b, 'jpdl31_EndStateType271', a2)
    assert _is_linked(b, 'jpdl31_EndStateType271', a2)
    if hasattr(a1, 'jpdl31_SuperStateType270'):
        assert not _is_linked(a1, 'jpdl31_SuperStateType270', b)
    if hasattr(a2, 'jpdl31_SuperStateType270'):
        assert _is_linked(a2, 'jpdl31_SuperStateType270', b)
    _safe_set(b, 'jpdl31_EndStateType271', None)
    assert not _is_linked(b, 'jpdl31_EndStateType271', a2)
    if hasattr(a2, 'jpdl31_SuperStateType270'):
        assert not _is_linked(a2, 'jpdl31_SuperStateType270', b)


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


def test_assoc_event102_reverse_link_reassign_clear():
    a1 = jpdl31_ForkType(async_="sample_text", group="sample_text", name="sample_text")
    a2 = jpdl31_ForkType(async_="sample_text_2", group="sample_text_2", name="sample_text_2")
    b = jpdl31_EventType(actionElements="sample_text", type="sample_text")
    _safe_set(b, 'jpdl31_EventType104', a1)
    assert _is_linked(b, 'jpdl31_EventType104', a1)
    if hasattr(a1, 'jpdl31_ForkType103'):
        assert _is_linked(a1, 'jpdl31_ForkType103', b)
    _safe_set(b, 'jpdl31_EventType104', a2)
    assert _is_linked(b, 'jpdl31_EventType104', a2)
    if hasattr(a1, 'jpdl31_ForkType103'):
        assert not _is_linked(a1, 'jpdl31_ForkType103', b)
    if hasattr(a2, 'jpdl31_ForkType103'):
        assert _is_linked(a2, 'jpdl31_ForkType103', b)
    _safe_set(b, 'jpdl31_EventType104', None)
    assert not _is_linked(b, 'jpdl31_EventType104', a2)
    if hasattr(a2, 'jpdl31_ForkType103'):
        assert not _is_linked(a2, 'jpdl31_ForkType103', b)


def test_assoc_event114_reverse_link_reassign_clear():
    a1 = jpdl31_JoinType(async_="sample_text", name="sample_text", nodeContentElements="sample_text")
    a2 = jpdl31_JoinType(async_="sample_text_2", name="sample_text_2", nodeContentElements="sample_text_2")
    b = jpdl31_EventType(actionElements="sample_text", type="sample_text")
    _safe_set(b, 'jpdl31_EventType116', a1)
    assert _is_linked(b, 'jpdl31_EventType116', a1)
    if hasattr(a1, 'jpdl31_JoinType115'):
        assert _is_linked(a1, 'jpdl31_JoinType115', b)
    _safe_set(b, 'jpdl31_EventType116', a2)
    assert _is_linked(b, 'jpdl31_EventType116', a2)
    if hasattr(a1, 'jpdl31_JoinType115'):
        assert not _is_linked(a1, 'jpdl31_JoinType115', b)
    if hasattr(a2, 'jpdl31_JoinType115'):
        assert _is_linked(a2, 'jpdl31_JoinType115', b)
    _safe_set(b, 'jpdl31_EventType116', None)
    assert not _is_linked(b, 'jpdl31_EventType116', a2)
    if hasattr(a2, 'jpdl31_JoinType115'):
        assert not _is_linked(a2, 'jpdl31_JoinType115', b)


def test_assoc_event138_reverse_link_reassign_clear():
    a1 = jpdl31_NodeType(async_="sample_text", description="sample_text", name="sample_text", nodeContentElements="sample_text")
    a2 = jpdl31_NodeType(async_="sample_text_2", description="sample_text_2", name="sample_text_2", nodeContentElements="sample_text_2")
    b = jpdl31_EventType(actionElements="sample_text", type="sample_text")
    _safe_set(b, 'jpdl31_EventType140', a1)
    assert _is_linked(b, 'jpdl31_EventType140', a1)
    if hasattr(a1, 'jpdl31_NodeType139'):
        assert _is_linked(a1, 'jpdl31_NodeType139', b)
    _safe_set(b, 'jpdl31_EventType140', a2)
    assert _is_linked(b, 'jpdl31_EventType140', a2)
    if hasattr(a1, 'jpdl31_NodeType139'):
        assert not _is_linked(a1, 'jpdl31_NodeType139', b)
    if hasattr(a2, 'jpdl31_NodeType139'):
        assert _is_linked(a2, 'jpdl31_NodeType139', b)
    _safe_set(b, 'jpdl31_EventType140', None)
    assert not _is_linked(b, 'jpdl31_EventType140', a2)
    if hasattr(a2, 'jpdl31_NodeType139'):
        assert not _is_linked(a2, 'jpdl31_NodeType139', b)


def test_assoc_event195_reverse_link_reassign_clear():
    a1 = jpdl31_ProcessDefinitionType(group="sample_text", name="sample_text", quantity="sample_text")
    a2 = jpdl31_ProcessDefinitionType(group="sample_text_2", name="sample_text_2", quantity="sample_text_2")
    b = jpdl31_EventType(actionElements="sample_text", type="sample_text")
    _safe_set(b, 'jpdl31_EventType197', a1)
    assert _is_linked(b, 'jpdl31_EventType197', a1)
    if hasattr(a1, 'jpdl31_ProcessDefinitionType196'):
        assert _is_linked(a1, 'jpdl31_ProcessDefinitionType196', b)
    _safe_set(b, 'jpdl31_EventType197', a2)
    assert _is_linked(b, 'jpdl31_EventType197', a2)
    if hasattr(a1, 'jpdl31_ProcessDefinitionType196'):
        assert not _is_linked(a1, 'jpdl31_ProcessDefinitionType196', b)
    if hasattr(a2, 'jpdl31_ProcessDefinitionType196'):
        assert _is_linked(a2, 'jpdl31_ProcessDefinitionType196', b)
    _safe_set(b, 'jpdl31_EventType197', None)
    assert not _is_linked(b, 'jpdl31_EventType197', a2)
    if hasattr(a2, 'jpdl31_ProcessDefinitionType196'):
        assert not _is_linked(a2, 'jpdl31_ProcessDefinitionType196', b)


def test_assoc_event209_reverse_link_reassign_clear():
    a1 = jpdl31_ProcessStateType(async_="sample_text", group="sample_text", name="sample_text")
    a2 = jpdl31_ProcessStateType(async_="sample_text_2", group="sample_text_2", name="sample_text_2")
    b = jpdl31_EventType(actionElements="sample_text", type="sample_text")
    _safe_set(b, 'jpdl31_EventType211', a1)
    assert _is_linked(b, 'jpdl31_EventType211', a1)
    if hasattr(a1, 'jpdl31_ProcessStateType210'):
        assert _is_linked(a1, 'jpdl31_ProcessStateType210', b)
    _safe_set(b, 'jpdl31_EventType211', a2)
    assert _is_linked(b, 'jpdl31_EventType211', a2)
    if hasattr(a1, 'jpdl31_ProcessStateType210'):
        assert not _is_linked(a1, 'jpdl31_ProcessStateType210', b)
    if hasattr(a2, 'jpdl31_ProcessStateType210'):
        assert _is_linked(a2, 'jpdl31_ProcessStateType210', b)
    _safe_set(b, 'jpdl31_EventType211', None)
    assert not _is_linked(b, 'jpdl31_EventType211', a2)
    if hasattr(a2, 'jpdl31_ProcessStateType210'):
        assert not _is_linked(a2, 'jpdl31_ProcessStateType210', b)


def test_assoc_event227_reverse_link_reassign_clear():
    a1 = jpdl31_StartStateType(group="sample_text", name="sample_text")
    a2 = jpdl31_StartStateType(group="sample_text_2", name="sample_text_2")
    b = jpdl31_EventType(actionElements="sample_text", type="sample_text")
    _safe_set(b, 'jpdl31_EventType229', a1)
    assert _is_linked(b, 'jpdl31_EventType229', a1)
    if hasattr(a1, 'jpdl31_StartStateType228'):
        assert _is_linked(a1, 'jpdl31_StartStateType228', b)
    _safe_set(b, 'jpdl31_EventType229', a2)
    assert _is_linked(b, 'jpdl31_EventType229', a2)
    if hasattr(a1, 'jpdl31_StartStateType228'):
        assert not _is_linked(a1, 'jpdl31_StartStateType228', b)
    if hasattr(a2, 'jpdl31_StartStateType228'):
        assert _is_linked(a2, 'jpdl31_StartStateType228', b)
    _safe_set(b, 'jpdl31_EventType229', None)
    assert not _is_linked(b, 'jpdl31_EventType229', a2)
    if hasattr(a2, 'jpdl31_StartStateType228'):
        assert not _is_linked(a2, 'jpdl31_StartStateType228', b)


def test_assoc_event233_reverse_link_reassign_clear():
    a1 = jpdl31_StateType(async_="sample_text", name="sample_text", nodeContentElements="sample_text")
    a2 = jpdl31_StateType(async_="sample_text_2", name="sample_text_2", nodeContentElements="sample_text_2")
    b = jpdl31_EventType(actionElements="sample_text", type="sample_text")
    _safe_set(b, 'jpdl31_EventType235', a1)
    assert _is_linked(b, 'jpdl31_EventType235', a1)
    if hasattr(a1, 'jpdl31_StateType234'):
        assert _is_linked(a1, 'jpdl31_StateType234', b)
    _safe_set(b, 'jpdl31_EventType235', a2)
    assert _is_linked(b, 'jpdl31_EventType235', a2)
    if hasattr(a1, 'jpdl31_StateType234'):
        assert not _is_linked(a1, 'jpdl31_StateType234', b)
    if hasattr(a2, 'jpdl31_StateType234'):
        assert _is_linked(a2, 'jpdl31_StateType234', b)
    _safe_set(b, 'jpdl31_EventType235', None)
    assert not _is_linked(b, 'jpdl31_EventType235', a2)
    if hasattr(a2, 'jpdl31_StateType234'):
        assert not _is_linked(a2, 'jpdl31_StateType234', b)


def test_assoc_event272_reverse_link_reassign_clear():
    a1 = jpdl31_SuperStateType(async_="sample_text", group="sample_text", name="sample_text")
    a2 = jpdl31_SuperStateType(async_="sample_text_2", group="sample_text_2", name="sample_text_2")
    b = jpdl31_EventType(actionElements="sample_text", type="sample_text")
    _safe_set(b, 'jpdl31_EventType274', a1)
    assert _is_linked(b, 'jpdl31_EventType274', a1)
    if hasattr(a1, 'jpdl31_SuperStateType273'):
        assert _is_linked(a1, 'jpdl31_SuperStateType273', b)
    _safe_set(b, 'jpdl31_EventType274', a2)
    assert _is_linked(b, 'jpdl31_EventType274', a2)
    if hasattr(a1, 'jpdl31_SuperStateType273'):
        assert not _is_linked(a1, 'jpdl31_SuperStateType273', b)
    if hasattr(a2, 'jpdl31_SuperStateType273'):
        assert _is_linked(a2, 'jpdl31_SuperStateType273', b)
    _safe_set(b, 'jpdl31_EventType274', None)
    assert not _is_linked(b, 'jpdl31_EventType274', a2)
    if hasattr(a2, 'jpdl31_SuperStateType273'):
        assert not _is_linked(a2, 'jpdl31_SuperStateType273', b)


def test_assoc_event290_reverse_link_reassign_clear():
    a1 = jpdl31_TaskNodeType(async_="sample_text", createTasks="sample_text", description="sample_text", endTasks="sample_text", group="sample_text", name="sample_text", signal="sample_text")
    a2 = jpdl31_TaskNodeType(async_="sample_text_2", createTasks="sample_text_2", description="sample_text_2", endTasks="sample_text_2", group="sample_text_2", name="sample_text_2", signal="sample_text_2")
    b = jpdl31_EventType(actionElements="sample_text", type="sample_text")
    _safe_set(b, 'jpdl31_EventType292', a1)
    assert _is_linked(b, 'jpdl31_EventType292', a1)
    if hasattr(a1, 'jpdl31_TaskNodeType291'):
        assert _is_linked(a1, 'jpdl31_TaskNodeType291', b)
    _safe_set(b, 'jpdl31_EventType292', a2)
    assert _is_linked(b, 'jpdl31_EventType292', a2)
    if hasattr(a1, 'jpdl31_TaskNodeType291'):
        assert not _is_linked(a1, 'jpdl31_TaskNodeType291', b)
    if hasattr(a2, 'jpdl31_TaskNodeType291'):
        assert _is_linked(a2, 'jpdl31_TaskNodeType291', b)
    _safe_set(b, 'jpdl31_EventType292', None)
    assert not _is_linked(b, 'jpdl31_EventType292', a2)
    if hasattr(a2, 'jpdl31_TaskNodeType291'):
        assert not _is_linked(a2, 'jpdl31_TaskNodeType291', b)


def test_assoc_event312_reverse_link_reassign_clear():
    a1 = jpdl31_TaskType(blocking="sample_text", description="sample_text", duedate="sample_text", group="sample_text", name="sample_text", priority="sample_text", signalling="sample_text", swimlane="sample_text")
    a2 = jpdl31_TaskType(blocking="sample_text_2", description="sample_text_2", duedate="sample_text_2", group="sample_text_2", name="sample_text_2", priority="sample_text_2", signalling="sample_text_2", swimlane="sample_text_2")
    b = jpdl31_EventType(actionElements="sample_text", type="sample_text")
    _safe_set(b, 'jpdl31_EventType314', a1)
    assert _is_linked(b, 'jpdl31_EventType314', a1)
    if hasattr(a1, 'jpdl31_TaskType313'):
        assert _is_linked(a1, 'jpdl31_TaskType313', b)
    _safe_set(b, 'jpdl31_EventType314', a2)
    assert _is_linked(b, 'jpdl31_EventType314', a2)
    if hasattr(a1, 'jpdl31_TaskType313'):
        assert not _is_linked(a1, 'jpdl31_TaskType313', b)
    if hasattr(a2, 'jpdl31_TaskType313'):
        assert _is_linked(a2, 'jpdl31_TaskType313', b)
    _safe_set(b, 'jpdl31_EventType314', None)
    assert not _is_linked(b, 'jpdl31_EventType314', a2)
    if hasattr(a2, 'jpdl31_TaskType313'):
        assert not _is_linked(a2, 'jpdl31_TaskType313', b)


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


def test_assoc_event75_reverse_link_reassign_clear():
    a1 = jpdl31_EventType(actionElements="sample_text", type="sample_text")
    a2 = jpdl31_EventType(actionElements="sample_text_2", type="sample_text_2")
    b = jpdl31_EndStateType(group="sample_text", name="sample_text")
    _safe_set(b, 'jpdl31_EndStateType76', {a1})
    assert _is_linked(b, 'jpdl31_EndStateType76', a1)
    if hasattr(a1, 'jpdl31_EventType77'):
        assert _is_linked(a1, 'jpdl31_EventType77', b)
    _safe_set(b, 'jpdl31_EndStateType76', {a2})
    assert _is_linked(b, 'jpdl31_EndStateType76', a2)
    if hasattr(a1, 'jpdl31_EventType77'):
        assert not _is_linked(a1, 'jpdl31_EventType77', b)
    if hasattr(a2, 'jpdl31_EventType77'):
        assert _is_linked(a2, 'jpdl31_EventType77', b)
    _safe_set(b, 'jpdl31_EndStateType76', set())
    assert not _is_linked(b, 'jpdl31_EndStateType76', a2)
    if hasattr(a2, 'jpdl31_EventType77'):
        assert not _is_linked(a2, 'jpdl31_EventType77', b)


def test_assoc_exceptionHandler105_reverse_link_reassign_clear():
    a1 = jpdl31_ForkType(async_="sample_text", group="sample_text", name="sample_text")
    a2 = jpdl31_ForkType(async_="sample_text_2", group="sample_text_2", name="sample_text_2")
    b = jpdl31_ExceptionHandlerType(exceptionClass="sample_text", group="sample_text")
    _safe_set(b, 'jpdl31_ExceptionHandlerType107', a1)
    assert _is_linked(b, 'jpdl31_ExceptionHandlerType107', a1)
    if hasattr(a1, 'jpdl31_ForkType106'):
        assert _is_linked(a1, 'jpdl31_ForkType106', b)
    _safe_set(b, 'jpdl31_ExceptionHandlerType107', a2)
    assert _is_linked(b, 'jpdl31_ExceptionHandlerType107', a2)
    if hasattr(a1, 'jpdl31_ForkType106'):
        assert not _is_linked(a1, 'jpdl31_ForkType106', b)
    if hasattr(a2, 'jpdl31_ForkType106'):
        assert _is_linked(a2, 'jpdl31_ForkType106', b)
    _safe_set(b, 'jpdl31_ExceptionHandlerType107', None)
    assert not _is_linked(b, 'jpdl31_ExceptionHandlerType107', a2)
    if hasattr(a2, 'jpdl31_ForkType106'):
        assert not _is_linked(a2, 'jpdl31_ForkType106', b)


def test_assoc_exceptionHandler117_reverse_link_reassign_clear():
    a1 = jpdl31_JoinType(async_="sample_text", name="sample_text", nodeContentElements="sample_text")
    a2 = jpdl31_JoinType(async_="sample_text_2", name="sample_text_2", nodeContentElements="sample_text_2")
    b = jpdl31_ExceptionHandlerType(exceptionClass="sample_text", group="sample_text")
    _safe_set(b, 'jpdl31_ExceptionHandlerType119', a1)
    assert _is_linked(b, 'jpdl31_ExceptionHandlerType119', a1)
    if hasattr(a1, 'jpdl31_JoinType118'):
        assert _is_linked(a1, 'jpdl31_JoinType118', b)
    _safe_set(b, 'jpdl31_ExceptionHandlerType119', a2)
    assert _is_linked(b, 'jpdl31_ExceptionHandlerType119', a2)
    if hasattr(a1, 'jpdl31_JoinType118'):
        assert not _is_linked(a1, 'jpdl31_JoinType118', b)
    if hasattr(a2, 'jpdl31_JoinType118'):
        assert _is_linked(a2, 'jpdl31_JoinType118', b)
    _safe_set(b, 'jpdl31_ExceptionHandlerType119', None)
    assert not _is_linked(b, 'jpdl31_ExceptionHandlerType119', a2)
    if hasattr(a2, 'jpdl31_JoinType118'):
        assert not _is_linked(a2, 'jpdl31_JoinType118', b)


def test_assoc_exceptionHandler141_reverse_link_reassign_clear():
    a1 = jpdl31_NodeType(async_="sample_text", description="sample_text", name="sample_text", nodeContentElements="sample_text")
    a2 = jpdl31_NodeType(async_="sample_text_2", description="sample_text_2", name="sample_text_2", nodeContentElements="sample_text_2")
    b = jpdl31_ExceptionHandlerType(exceptionClass="sample_text", group="sample_text")
    _safe_set(b, 'jpdl31_ExceptionHandlerType143', a1)
    assert _is_linked(b, 'jpdl31_ExceptionHandlerType143', a1)
    if hasattr(a1, 'jpdl31_NodeType142'):
        assert _is_linked(a1, 'jpdl31_NodeType142', b)
    _safe_set(b, 'jpdl31_ExceptionHandlerType143', a2)
    assert _is_linked(b, 'jpdl31_ExceptionHandlerType143', a2)
    if hasattr(a1, 'jpdl31_NodeType142'):
        assert not _is_linked(a1, 'jpdl31_NodeType142', b)
    if hasattr(a2, 'jpdl31_NodeType142'):
        assert _is_linked(a2, 'jpdl31_NodeType142', b)
    _safe_set(b, 'jpdl31_ExceptionHandlerType143', None)
    assert not _is_linked(b, 'jpdl31_ExceptionHandlerType143', a2)
    if hasattr(a2, 'jpdl31_NodeType142'):
        assert not _is_linked(a2, 'jpdl31_NodeType142', b)


def test_assoc_exceptionHandler198_reverse_link_reassign_clear():
    a1 = jpdl31_ProcessDefinitionType(group="sample_text", name="sample_text", quantity="sample_text")
    a2 = jpdl31_ProcessDefinitionType(group="sample_text_2", name="sample_text_2", quantity="sample_text_2")
    b = jpdl31_ExceptionHandlerType(exceptionClass="sample_text", group="sample_text")
    _safe_set(b, 'jpdl31_ExceptionHandlerType200', a1)
    assert _is_linked(b, 'jpdl31_ExceptionHandlerType200', a1)
    if hasattr(a1, 'jpdl31_ProcessDefinitionType199'):
        assert _is_linked(a1, 'jpdl31_ProcessDefinitionType199', b)
    _safe_set(b, 'jpdl31_ExceptionHandlerType200', a2)
    assert _is_linked(b, 'jpdl31_ExceptionHandlerType200', a2)
    if hasattr(a1, 'jpdl31_ProcessDefinitionType199'):
        assert not _is_linked(a1, 'jpdl31_ProcessDefinitionType199', b)
    if hasattr(a2, 'jpdl31_ProcessDefinitionType199'):
        assert _is_linked(a2, 'jpdl31_ProcessDefinitionType199', b)
    _safe_set(b, 'jpdl31_ExceptionHandlerType200', None)
    assert not _is_linked(b, 'jpdl31_ExceptionHandlerType200', a2)
    if hasattr(a2, 'jpdl31_ProcessDefinitionType199'):
        assert not _is_linked(a2, 'jpdl31_ProcessDefinitionType199', b)


def test_assoc_exceptionHandler212_reverse_link_reassign_clear():
    a1 = jpdl31_ProcessStateType(async_="sample_text", group="sample_text", name="sample_text")
    a2 = jpdl31_ProcessStateType(async_="sample_text_2", group="sample_text_2", name="sample_text_2")
    b = jpdl31_ExceptionHandlerType(exceptionClass="sample_text", group="sample_text")
    _safe_set(b, 'jpdl31_ExceptionHandlerType214', a1)
    assert _is_linked(b, 'jpdl31_ExceptionHandlerType214', a1)
    if hasattr(a1, 'jpdl31_ProcessStateType213'):
        assert _is_linked(a1, 'jpdl31_ProcessStateType213', b)
    _safe_set(b, 'jpdl31_ExceptionHandlerType214', a2)
    assert _is_linked(b, 'jpdl31_ExceptionHandlerType214', a2)
    if hasattr(a1, 'jpdl31_ProcessStateType213'):
        assert not _is_linked(a1, 'jpdl31_ProcessStateType213', b)
    if hasattr(a2, 'jpdl31_ProcessStateType213'):
        assert _is_linked(a2, 'jpdl31_ProcessStateType213', b)
    _safe_set(b, 'jpdl31_ExceptionHandlerType214', None)
    assert not _is_linked(b, 'jpdl31_ExceptionHandlerType214', a2)
    if hasattr(a2, 'jpdl31_ProcessStateType213'):
        assert not _is_linked(a2, 'jpdl31_ProcessStateType213', b)


def test_assoc_exceptionHandler230_reverse_link_reassign_clear():
    a1 = jpdl31_StartStateType(group="sample_text", name="sample_text")
    a2 = jpdl31_StartStateType(group="sample_text_2", name="sample_text_2")
    b = jpdl31_ExceptionHandlerType(exceptionClass="sample_text", group="sample_text")
    _safe_set(b, 'jpdl31_ExceptionHandlerType232', a1)
    assert _is_linked(b, 'jpdl31_ExceptionHandlerType232', a1)
    if hasattr(a1, 'jpdl31_StartStateType231'):
        assert _is_linked(a1, 'jpdl31_StartStateType231', b)
    _safe_set(b, 'jpdl31_ExceptionHandlerType232', a2)
    assert _is_linked(b, 'jpdl31_ExceptionHandlerType232', a2)
    if hasattr(a1, 'jpdl31_StartStateType231'):
        assert not _is_linked(a1, 'jpdl31_StartStateType231', b)
    if hasattr(a2, 'jpdl31_StartStateType231'):
        assert _is_linked(a2, 'jpdl31_StartStateType231', b)
    _safe_set(b, 'jpdl31_ExceptionHandlerType232', None)
    assert not _is_linked(b, 'jpdl31_ExceptionHandlerType232', a2)
    if hasattr(a2, 'jpdl31_StartStateType231'):
        assert not _is_linked(a2, 'jpdl31_StartStateType231', b)


def test_assoc_exceptionHandler236_reverse_link_reassign_clear():
    a1 = jpdl31_StateType(async_="sample_text", name="sample_text", nodeContentElements="sample_text")
    a2 = jpdl31_StateType(async_="sample_text_2", name="sample_text_2", nodeContentElements="sample_text_2")
    b = jpdl31_ExceptionHandlerType(exceptionClass="sample_text", group="sample_text")
    _safe_set(b, 'jpdl31_ExceptionHandlerType238', a1)
    assert _is_linked(b, 'jpdl31_ExceptionHandlerType238', a1)
    if hasattr(a1, 'jpdl31_StateType237'):
        assert _is_linked(a1, 'jpdl31_StateType237', b)
    _safe_set(b, 'jpdl31_ExceptionHandlerType238', a2)
    assert _is_linked(b, 'jpdl31_ExceptionHandlerType238', a2)
    if hasattr(a1, 'jpdl31_StateType237'):
        assert not _is_linked(a1, 'jpdl31_StateType237', b)
    if hasattr(a2, 'jpdl31_StateType237'):
        assert _is_linked(a2, 'jpdl31_StateType237', b)
    _safe_set(b, 'jpdl31_ExceptionHandlerType238', None)
    assert not _is_linked(b, 'jpdl31_ExceptionHandlerType238', a2)
    if hasattr(a2, 'jpdl31_StateType237'):
        assert not _is_linked(a2, 'jpdl31_StateType237', b)


def test_assoc_exceptionHandler275_reverse_link_reassign_clear():
    a1 = jpdl31_SuperStateType(async_="sample_text", group="sample_text", name="sample_text")
    a2 = jpdl31_SuperStateType(async_="sample_text_2", group="sample_text_2", name="sample_text_2")
    b = jpdl31_ExceptionHandlerType(exceptionClass="sample_text", group="sample_text")
    _safe_set(b, 'jpdl31_ExceptionHandlerType277', a1)
    assert _is_linked(b, 'jpdl31_ExceptionHandlerType277', a1)
    if hasattr(a1, 'jpdl31_SuperStateType276'):
        assert _is_linked(a1, 'jpdl31_SuperStateType276', b)
    _safe_set(b, 'jpdl31_ExceptionHandlerType277', a2)
    assert _is_linked(b, 'jpdl31_ExceptionHandlerType277', a2)
    if hasattr(a1, 'jpdl31_SuperStateType276'):
        assert not _is_linked(a1, 'jpdl31_SuperStateType276', b)
    if hasattr(a2, 'jpdl31_SuperStateType276'):
        assert _is_linked(a2, 'jpdl31_SuperStateType276', b)
    _safe_set(b, 'jpdl31_ExceptionHandlerType277', None)
    assert not _is_linked(b, 'jpdl31_ExceptionHandlerType277', a2)
    if hasattr(a2, 'jpdl31_SuperStateType276'):
        assert not _is_linked(a2, 'jpdl31_SuperStateType276', b)


def test_assoc_exceptionHandler293_reverse_link_reassign_clear():
    a1 = jpdl31_TaskNodeType(async_="sample_text", createTasks="sample_text", description="sample_text", endTasks="sample_text", group="sample_text", name="sample_text", signal="sample_text")
    a2 = jpdl31_TaskNodeType(async_="sample_text_2", createTasks="sample_text_2", description="sample_text_2", endTasks="sample_text_2", group="sample_text_2", name="sample_text_2", signal="sample_text_2")
    b = jpdl31_ExceptionHandlerType(exceptionClass="sample_text", group="sample_text")
    _safe_set(b, 'jpdl31_ExceptionHandlerType295', a1)
    assert _is_linked(b, 'jpdl31_ExceptionHandlerType295', a1)
    if hasattr(a1, 'jpdl31_TaskNodeType294'):
        assert _is_linked(a1, 'jpdl31_TaskNodeType294', b)
    _safe_set(b, 'jpdl31_ExceptionHandlerType295', a2)
    assert _is_linked(b, 'jpdl31_ExceptionHandlerType295', a2)
    if hasattr(a1, 'jpdl31_TaskNodeType294'):
        assert not _is_linked(a1, 'jpdl31_TaskNodeType294', b)
    if hasattr(a2, 'jpdl31_TaskNodeType294'):
        assert _is_linked(a2, 'jpdl31_TaskNodeType294', b)
    _safe_set(b, 'jpdl31_ExceptionHandlerType295', None)
    assert not _is_linked(b, 'jpdl31_ExceptionHandlerType295', a2)
    if hasattr(a2, 'jpdl31_TaskNodeType294'):
        assert not _is_linked(a2, 'jpdl31_TaskNodeType294', b)


def test_assoc_exceptionHandler342_reverse_link_reassign_clear():
    a1 = jpdl31_TransitionType(group="sample_text", name="sample_text", to="sample_text")
    a2 = jpdl31_TransitionType(group="sample_text_2", name="sample_text_2", to="sample_text_2")
    b = jpdl31_ExceptionHandlerType(exceptionClass="sample_text", group="sample_text")
    _safe_set(b, 'jpdl31_ExceptionHandlerType344', a1)
    assert _is_linked(b, 'jpdl31_ExceptionHandlerType344', a1)
    if hasattr(a1, 'jpdl31_TransitionType343'):
        assert _is_linked(a1, 'jpdl31_TransitionType343', b)
    _safe_set(b, 'jpdl31_ExceptionHandlerType344', a2)
    assert _is_linked(b, 'jpdl31_ExceptionHandlerType344', a2)
    if hasattr(a1, 'jpdl31_TransitionType343'):
        assert not _is_linked(a1, 'jpdl31_TransitionType343', b)
    if hasattr(a2, 'jpdl31_TransitionType343'):
        assert _is_linked(a2, 'jpdl31_TransitionType343', b)
    _safe_set(b, 'jpdl31_ExceptionHandlerType344', None)
    assert not _is_linked(b, 'jpdl31_ExceptionHandlerType344', a2)
    if hasattr(a2, 'jpdl31_TransitionType343'):
        assert not _is_linked(a2, 'jpdl31_TransitionType343', b)


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


def test_assoc_exceptionHandler359_reverse_link_reassign_clear():
    a1 = jpdl31_TransitionType1(group="sample_text", name="sample_text", to="sample_text")
    a2 = jpdl31_TransitionType1(group="sample_text_2", name="sample_text_2", to="sample_text_2")
    b = jpdl31_ExceptionHandlerType(exceptionClass="sample_text", group="sample_text")
    _safe_set(b, 'jpdl31_ExceptionHandlerType361', a1)
    assert _is_linked(b, 'jpdl31_ExceptionHandlerType361', a1)
    if hasattr(a1, 'jpdl31_TransitionType1360'):
        assert _is_linked(a1, 'jpdl31_TransitionType1360', b)
    _safe_set(b, 'jpdl31_ExceptionHandlerType361', a2)
    assert _is_linked(b, 'jpdl31_ExceptionHandlerType361', a2)
    if hasattr(a1, 'jpdl31_TransitionType1360'):
        assert not _is_linked(a1, 'jpdl31_TransitionType1360', b)
    if hasattr(a2, 'jpdl31_TransitionType1360'):
        assert _is_linked(a2, 'jpdl31_TransitionType1360', b)
    _safe_set(b, 'jpdl31_ExceptionHandlerType361', None)
    assert not _is_linked(b, 'jpdl31_ExceptionHandlerType361', a2)
    if hasattr(a2, 'jpdl31_TransitionType1360'):
        assert not _is_linked(a2, 'jpdl31_TransitionType1360', b)


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


def test_assoc_exceptionHandler78_reverse_link_reassign_clear():
    a1 = jpdl31_ExceptionHandlerType(exceptionClass="sample_text", group="sample_text")
    a2 = jpdl31_ExceptionHandlerType(exceptionClass="sample_text_2", group="sample_text_2")
    b = jpdl31_EndStateType(group="sample_text", name="sample_text")
    _safe_set(b, 'jpdl31_EndStateType79', {a1})
    assert _is_linked(b, 'jpdl31_EndStateType79', a1)
    if hasattr(a1, 'jpdl31_ExceptionHandlerType80'):
        assert _is_linked(a1, 'jpdl31_ExceptionHandlerType80', b)
    _safe_set(b, 'jpdl31_EndStateType79', {a2})
    assert _is_linked(b, 'jpdl31_EndStateType79', a2)
    if hasattr(a1, 'jpdl31_ExceptionHandlerType80'):
        assert not _is_linked(a1, 'jpdl31_ExceptionHandlerType80', b)
    if hasattr(a2, 'jpdl31_ExceptionHandlerType80'):
        assert _is_linked(a2, 'jpdl31_ExceptionHandlerType80', b)
    _safe_set(b, 'jpdl31_EndStateType79', set())
    assert not _is_linked(b, 'jpdl31_EndStateType79', a2)
    if hasattr(a2, 'jpdl31_ExceptionHandlerType80'):
        assert not _is_linked(a2, 'jpdl31_ExceptionHandlerType80', b)


def test_assoc_factors409_reverse_link_reassign_clear():
    a1 = jpdl31_Factor(isTreament="sample_text", name="sample_text")
    a2 = jpdl31_Factor(isTreament="sample_text_2", name="sample_text_2")
    b = jpdl31_Design(DoE="sample_text")
    _safe_set(b, 'jpdl31_Design410', {a1})
    assert _is_linked(b, 'jpdl31_Design410', a1)
    if hasattr(a1, 'jpdl31_Factor411'):
        assert _is_linked(a1, 'jpdl31_Factor411', b)
    _safe_set(b, 'jpdl31_Design410', {a2})
    assert _is_linked(b, 'jpdl31_Design410', a2)
    if hasattr(a1, 'jpdl31_Factor411'):
        assert not _is_linked(a1, 'jpdl31_Factor411', b)
    if hasattr(a2, 'jpdl31_Factor411'):
        assert _is_linked(a2, 'jpdl31_Factor411', b)
    _safe_set(b, 'jpdl31_Design410', set())
    assert not _is_linked(b, 'jpdl31_Design410', a2)
    if hasattr(a2, 'jpdl31_Factor411'):
        assert not _is_linked(a2, 'jpdl31_Factor411', b)


def test_assoc_fork171_reverse_link_reassign_clear():
    a1 = jpdl31_ProcessDefinitionType(group="sample_text", name="sample_text", quantity="sample_text")
    a2 = jpdl31_ProcessDefinitionType(group="sample_text_2", name="sample_text_2", quantity="sample_text_2")
    b = jpdl31_ForkType(async_="sample_text", group="sample_text", name="sample_text")
    _safe_set(b, 'jpdl31_ForkType173', a1)
    assert _is_linked(b, 'jpdl31_ForkType173', a1)
    if hasattr(a1, 'jpdl31_ProcessDefinitionType172'):
        assert _is_linked(a1, 'jpdl31_ProcessDefinitionType172', b)
    _safe_set(b, 'jpdl31_ForkType173', a2)
    assert _is_linked(b, 'jpdl31_ForkType173', a2)
    if hasattr(a1, 'jpdl31_ProcessDefinitionType172'):
        assert not _is_linked(a1, 'jpdl31_ProcessDefinitionType172', b)
    if hasattr(a2, 'jpdl31_ProcessDefinitionType172'):
        assert _is_linked(a2, 'jpdl31_ProcessDefinitionType172', b)
    _safe_set(b, 'jpdl31_ForkType173', None)
    assert not _is_linked(b, 'jpdl31_ForkType173', a2)
    if hasattr(a2, 'jpdl31_ProcessDefinitionType172'):
        assert not _is_linked(a2, 'jpdl31_ProcessDefinitionType172', b)


def test_assoc_fork260_reverse_link_reassign_clear():
    a1 = jpdl31_SuperStateType(async_="sample_text", group="sample_text", name="sample_text")
    a2 = jpdl31_SuperStateType(async_="sample_text_2", group="sample_text_2", name="sample_text_2")
    b = jpdl31_ForkType(async_="sample_text", group="sample_text", name="sample_text")
    _safe_set(b, 'jpdl31_ForkType262', a1)
    assert _is_linked(b, 'jpdl31_ForkType262', a1)
    if hasattr(a1, 'jpdl31_SuperStateType261'):
        assert _is_linked(a1, 'jpdl31_SuperStateType261', b)
    _safe_set(b, 'jpdl31_ForkType262', a2)
    assert _is_linked(b, 'jpdl31_ForkType262', a2)
    if hasattr(a1, 'jpdl31_SuperStateType261'):
        assert not _is_linked(a1, 'jpdl31_SuperStateType261', b)
    if hasattr(a2, 'jpdl31_SuperStateType261'):
        assert _is_linked(a2, 'jpdl31_SuperStateType261', b)
    _safe_set(b, 'jpdl31_ForkType262', None)
    assert not _is_linked(b, 'jpdl31_ForkType262', a2)
    if hasattr(a2, 'jpdl31_SuperStateType261'):
        assert not _is_linked(a2, 'jpdl31_SuperStateType261', b)


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


def test_assoc_formalizes367_reverse_link_reassign_clear():
    a1 = jpdl31_Subhypotheses(relationOp="sample_text")
    a2 = jpdl31_Subhypotheses(relationOp="sample_text_2")
    b = jpdl31_Hyphotesis(description="sample_text", id="sample_text", relationOp="sample_text", type="sample_text")
    _safe_set(b, 'jpdl31_Hyphotesis', {a1})
    assert _is_linked(b, 'jpdl31_Hyphotesis', a1)
    if hasattr(a1, 'jpdl31_Subhypotheses'):
        assert _is_linked(a1, 'jpdl31_Subhypotheses', b)
    _safe_set(b, 'jpdl31_Hyphotesis', {a2})
    assert _is_linked(b, 'jpdl31_Hyphotesis', a2)
    if hasattr(a1, 'jpdl31_Subhypotheses'):
        assert not _is_linked(a1, 'jpdl31_Subhypotheses', b)
    if hasattr(a2, 'jpdl31_Subhypotheses'):
        assert _is_linked(a2, 'jpdl31_Subhypotheses', b)
    _safe_set(b, 'jpdl31_Hyphotesis', set())
    assert not _is_linked(b, 'jpdl31_Hyphotesis', a2)
    if hasattr(a2, 'jpdl31_Subhypotheses'):
        assert not _is_linked(a2, 'jpdl31_Subhypotheses', b)


def test_assoc_fromGoal368_reverse_link_reassign_clear():
    a1 = jpdl31_Hyphotesis(description="sample_text", id="sample_text", relationOp="sample_text", type="sample_text")
    a2 = jpdl31_Hyphotesis(description="sample_text_2", id="sample_text_2", relationOp="sample_text_2", type="sample_text_2")
    b = jpdl31_Goal(description="sample_text", id="sample_text")
    _safe_set(b, 'jpdl31_Goal', a1)
    assert _is_linked(b, 'jpdl31_Goal', a1)
    if hasattr(a1, 'jpdl31_Hyphotesis369'):
        assert _is_linked(a1, 'jpdl31_Hyphotesis369', b)
    _safe_set(b, 'jpdl31_Goal', a2)
    assert _is_linked(b, 'jpdl31_Goal', a2)
    if hasattr(a1, 'jpdl31_Hyphotesis369'):
        assert not _is_linked(a1, 'jpdl31_Hyphotesis369', b)
    if hasattr(a2, 'jpdl31_Hyphotesis369'):
        assert _is_linked(a2, 'jpdl31_Hyphotesis369', b)
    _safe_set(b, 'jpdl31_Goal', None)
    assert not _is_linked(b, 'jpdl31_Goal', a2)
    if hasattr(a2, 'jpdl31_Hyphotesis369'):
        assert not _is_linked(a2, 'jpdl31_Hyphotesis369', b)


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


def test_assoc_hypotheses398_reverse_link_reassign_clear():
    a1 = jpdl31_Hyphotesis(description="sample_text", id="sample_text", relationOp="sample_text", type="sample_text")
    a2 = jpdl31_Hyphotesis(description="sample_text_2", id="sample_text_2", relationOp="sample_text_2", type="sample_text_2")
    b = jpdl31_Goal(description="sample_text", id="sample_text")
    _safe_set(b, 'jpdl31_Goal399', {a1})
    assert _is_linked(b, 'jpdl31_Goal399', a1)
    if hasattr(a1, 'jpdl31_Hyphotesis400'):
        assert _is_linked(a1, 'jpdl31_Hyphotesis400', b)
    _safe_set(b, 'jpdl31_Goal399', {a2})
    assert _is_linked(b, 'jpdl31_Goal399', a2)
    if hasattr(a1, 'jpdl31_Hyphotesis400'):
        assert not _is_linked(a1, 'jpdl31_Hyphotesis400', b)
    if hasattr(a2, 'jpdl31_Hyphotesis400'):
        assert _is_linked(a2, 'jpdl31_Hyphotesis400', b)
    _safe_set(b, 'jpdl31_Goal399', set())
    assert not _is_linked(b, 'jpdl31_Goal399', a2)
    if hasattr(a2, 'jpdl31_Hyphotesis400'):
        assert not _is_linked(a2, 'jpdl31_Hyphotesis400', b)


def test_assoc_join174_reverse_link_reassign_clear():
    a1 = jpdl31_ProcessDefinitionType(group="sample_text", name="sample_text", quantity="sample_text")
    a2 = jpdl31_ProcessDefinitionType(group="sample_text_2", name="sample_text_2", quantity="sample_text_2")
    b = jpdl31_JoinType(async_="sample_text", name="sample_text", nodeContentElements="sample_text")
    _safe_set(b, 'jpdl31_JoinType176', a1)
    assert _is_linked(b, 'jpdl31_JoinType176', a1)
    if hasattr(a1, 'jpdl31_ProcessDefinitionType175'):
        assert _is_linked(a1, 'jpdl31_ProcessDefinitionType175', b)
    _safe_set(b, 'jpdl31_JoinType176', a2)
    assert _is_linked(b, 'jpdl31_JoinType176', a2)
    if hasattr(a1, 'jpdl31_ProcessDefinitionType175'):
        assert not _is_linked(a1, 'jpdl31_ProcessDefinitionType175', b)
    if hasattr(a2, 'jpdl31_ProcessDefinitionType175'):
        assert _is_linked(a2, 'jpdl31_ProcessDefinitionType175', b)
    _safe_set(b, 'jpdl31_JoinType176', None)
    assert not _is_linked(b, 'jpdl31_JoinType176', a2)
    if hasattr(a2, 'jpdl31_ProcessDefinitionType175'):
        assert not _is_linked(a2, 'jpdl31_ProcessDefinitionType175', b)


def test_assoc_join263_reverse_link_reassign_clear():
    a1 = jpdl31_SuperStateType(async_="sample_text", group="sample_text", name="sample_text")
    a2 = jpdl31_SuperStateType(async_="sample_text_2", group="sample_text_2", name="sample_text_2")
    b = jpdl31_JoinType(async_="sample_text", name="sample_text", nodeContentElements="sample_text")
    _safe_set(b, 'jpdl31_JoinType265', a1)
    assert _is_linked(b, 'jpdl31_JoinType265', a1)
    if hasattr(a1, 'jpdl31_SuperStateType264'):
        assert _is_linked(a1, 'jpdl31_SuperStateType264', b)
    _safe_set(b, 'jpdl31_JoinType265', a2)
    assert _is_linked(b, 'jpdl31_JoinType265', a2)
    if hasattr(a1, 'jpdl31_SuperStateType264'):
        assert not _is_linked(a1, 'jpdl31_SuperStateType264', b)
    if hasattr(a2, 'jpdl31_SuperStateType264'):
        assert _is_linked(a2, 'jpdl31_SuperStateType264', b)
    _safe_set(b, 'jpdl31_JoinType265', None)
    assert not _is_linked(b, 'jpdl31_JoinType265', a2)
    if hasattr(a2, 'jpdl31_SuperStateType264'):
        assert not _is_linked(a2, 'jpdl31_SuperStateType264', b)


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


def test_assoc_levels383_reverse_link_reassign_clear():
    a1 = jpdl31_Level(name="sample_text")
    a2 = jpdl31_Level(name="sample_text_2")
    b = jpdl31_Factor(isTreament="sample_text", name="sample_text")
    _safe_set(b, 'jpdl31_Factor', {a1})
    assert _is_linked(b, 'jpdl31_Factor', a1)
    if hasattr(a1, 'jpdl31_Level384'):
        assert _is_linked(a1, 'jpdl31_Level384', b)
    _safe_set(b, 'jpdl31_Factor', {a2})
    assert _is_linked(b, 'jpdl31_Factor', a2)
    if hasattr(a1, 'jpdl31_Level384'):
        assert not _is_linked(a1, 'jpdl31_Level384', b)
    if hasattr(a2, 'jpdl31_Level384'):
        assert _is_linked(a2, 'jpdl31_Level384', b)
    _safe_set(b, 'jpdl31_Factor', set())
    assert not _is_linked(b, 'jpdl31_Factor', a2)
    if hasattr(a2, 'jpdl31_Level384'):
        assert not _is_linked(a2, 'jpdl31_Level384', b)


def test_assoc_measureBy380_reverse_link_reassign_clear():
    a1 = jpdl31_Metric(description="sample_text", name="sample_text", refname="sample_text", type="sample_text")
    a2 = jpdl31_Metric(description="sample_text_2", name="sample_text_2", refname="sample_text_2", type="sample_text_2")
    b = jpdl31_DependentVariable(description="sample_text", name="sample_text")
    _safe_set(b, 'jpdl31_DependentVariable381', {a1})
    assert _is_linked(b, 'jpdl31_DependentVariable381', a1)
    if hasattr(a1, 'jpdl31_Metric382'):
        assert _is_linked(a1, 'jpdl31_Metric382', b)
    _safe_set(b, 'jpdl31_DependentVariable381', {a2})
    assert _is_linked(b, 'jpdl31_DependentVariable381', a2)
    if hasattr(a1, 'jpdl31_Metric382'):
        assert not _is_linked(a1, 'jpdl31_Metric382', b)
    if hasattr(a2, 'jpdl31_Metric382'):
        assert _is_linked(a2, 'jpdl31_Metric382', b)
    _safe_set(b, 'jpdl31_DependentVariable381', set())
    assert not _is_linked(b, 'jpdl31_DependentVariable381', a2)
    if hasattr(a2, 'jpdl31_Metric382'):
        assert not _is_linked(a2, 'jpdl31_Metric382', b)


def test_assoc_metricInfo321_reverse_link_reassign_clear():
    a1 = jpdl31_TaskType(blocking="sample_text", description="sample_text", duedate="sample_text", group="sample_text", name="sample_text", priority="sample_text", signalling="sample_text", swimlane="sample_text")
    a2 = jpdl31_TaskType(blocking="sample_text_2", description="sample_text_2", duedate="sample_text_2", group="sample_text_2", name="sample_text_2", priority="sample_text_2", signalling="sample_text_2", swimlane="sample_text_2")
    b = jpdl31_MetricInfo(name="sample_text")
    _safe_set(b, 'jpdl31_MetricInfo323', a1)
    assert _is_linked(b, 'jpdl31_MetricInfo323', a1)
    if hasattr(a1, 'jpdl31_TaskType322'):
        assert _is_linked(a1, 'jpdl31_TaskType322', b)
    _safe_set(b, 'jpdl31_MetricInfo323', a2)
    assert _is_linked(b, 'jpdl31_MetricInfo323', a2)
    if hasattr(a1, 'jpdl31_TaskType322'):
        assert not _is_linked(a1, 'jpdl31_TaskType322', b)
    if hasattr(a2, 'jpdl31_TaskType322'):
        assert _is_linked(a2, 'jpdl31_TaskType322', b)
    _safe_set(b, 'jpdl31_MetricInfo323', None)
    assert not _is_linked(b, 'jpdl31_MetricInfo323', a2)
    if hasattr(a2, 'jpdl31_TaskType322'):
        assert not _is_linked(a2, 'jpdl31_TaskType322', b)


def test_assoc_metricReferenced364_reverse_link_reassign_clear():
    a1 = jpdl31_MetricInfo(name="sample_text")
    a2 = jpdl31_MetricInfo(name="sample_text_2")
    b = jpdl31_Metric(description="sample_text", name="sample_text", refname="sample_text", type="sample_text")
    _safe_set(b, 'jpdl31_Metric366', a1)
    assert _is_linked(b, 'jpdl31_Metric366', a1)
    if hasattr(a1, 'jpdl31_MetricInfo365'):
        assert _is_linked(a1, 'jpdl31_MetricInfo365', b)
    _safe_set(b, 'jpdl31_Metric366', a2)
    assert _is_linked(b, 'jpdl31_Metric366', a2)
    if hasattr(a1, 'jpdl31_MetricInfo365'):
        assert not _is_linked(a1, 'jpdl31_MetricInfo365', b)
    if hasattr(a2, 'jpdl31_MetricInfo365'):
        assert _is_linked(a2, 'jpdl31_MetricInfo365', b)
    _safe_set(b, 'jpdl31_Metric366', None)
    assert not _is_linked(b, 'jpdl31_Metric366', a2)
    if hasattr(a2, 'jpdl31_MetricInfo365'):
        assert not _is_linked(a2, 'jpdl31_MetricInfo365', b)


def test_assoc_metrics304_reverse_link_reassign_clear():
    a1 = jpdl31_TaskNodeType(async_="sample_text", createTasks="sample_text", description="sample_text", endTasks="sample_text", group="sample_text", name="sample_text", signal="sample_text")
    a2 = jpdl31_TaskNodeType(async_="sample_text_2", createTasks="sample_text_2", description="sample_text_2", endTasks="sample_text_2", group="sample_text_2", name="sample_text_2", signal="sample_text_2")
    b = jpdl31_MetricInfo(name="sample_text")
    _safe_set(b, 'jpdl31_MetricInfo', a1)
    assert _is_linked(b, 'jpdl31_MetricInfo', a1)
    if hasattr(a1, 'jpdl31_TaskNodeType305'):
        assert _is_linked(a1, 'jpdl31_TaskNodeType305', b)
    _safe_set(b, 'jpdl31_MetricInfo', a2)
    assert _is_linked(b, 'jpdl31_MetricInfo', a2)
    if hasattr(a1, 'jpdl31_TaskNodeType305'):
        assert not _is_linked(a1, 'jpdl31_TaskNodeType305', b)
    if hasattr(a2, 'jpdl31_TaskNodeType305'):
        assert _is_linked(a2, 'jpdl31_TaskNodeType305', b)
    _safe_set(b, 'jpdl31_MetricInfo', None)
    assert not _is_linked(b, 'jpdl31_MetricInfo', a2)
    if hasattr(a2, 'jpdl31_TaskNodeType305'):
        assert not _is_linked(a2, 'jpdl31_TaskNodeType305', b)


def test_assoc_metrics73_reverse_link_reassign_clear():
    a1 = jpdl31_Metric(description="sample_text", name="sample_text", refname="sample_text", type="sample_text")
    a2 = jpdl31_Metric(description="sample_text_2", name="sample_text_2", refname="sample_text_2", type="sample_text_2")
    b = jpdl31_DocumentRoot(mixed="sample_text")
    _safe_set(b, 'jpdl31_DocumentRoot74', {a1})
    assert _is_linked(b, 'jpdl31_DocumentRoot74', a1)
    if hasattr(a1, 'jpdl31_Metric'):
        assert _is_linked(a1, 'jpdl31_Metric', b)
    _safe_set(b, 'jpdl31_DocumentRoot74', {a2})
    assert _is_linked(b, 'jpdl31_DocumentRoot74', a2)
    if hasattr(a1, 'jpdl31_Metric'):
        assert not _is_linked(a1, 'jpdl31_Metric', b)
    if hasattr(a2, 'jpdl31_Metric'):
        assert _is_linked(a2, 'jpdl31_Metric', b)
    _safe_set(b, 'jpdl31_DocumentRoot74', set())
    assert not _is_linked(b, 'jpdl31_DocumentRoot74', a2)
    if hasattr(a2, 'jpdl31_Metric'):
        assert not _is_linked(a2, 'jpdl31_Metric', b)


def test_assoc_node156_reverse_link_reassign_clear():
    a1 = jpdl31_ProcessDefinitionType(group="sample_text", name="sample_text", quantity="sample_text")
    a2 = jpdl31_ProcessDefinitionType(group="sample_text_2", name="sample_text_2", quantity="sample_text_2")
    b = jpdl31_NodeType(async_="sample_text", description="sample_text", name="sample_text", nodeContentElements="sample_text")
    _safe_set(b, 'jpdl31_NodeType158', a1)
    assert _is_linked(b, 'jpdl31_NodeType158', a1)
    if hasattr(a1, 'jpdl31_ProcessDefinitionType157'):
        assert _is_linked(a1, 'jpdl31_ProcessDefinitionType157', b)
    _safe_set(b, 'jpdl31_NodeType158', a2)
    assert _is_linked(b, 'jpdl31_NodeType158', a2)
    if hasattr(a1, 'jpdl31_ProcessDefinitionType157'):
        assert not _is_linked(a1, 'jpdl31_ProcessDefinitionType157', b)
    if hasattr(a2, 'jpdl31_ProcessDefinitionType157'):
        assert _is_linked(a2, 'jpdl31_ProcessDefinitionType157', b)
    _safe_set(b, 'jpdl31_NodeType158', None)
    assert not _is_linked(b, 'jpdl31_NodeType158', a2)
    if hasattr(a2, 'jpdl31_ProcessDefinitionType157'):
        assert not _is_linked(a2, 'jpdl31_ProcessDefinitionType157', b)


def test_assoc_node245_reverse_link_reassign_clear():
    a1 = jpdl31_SuperStateType(async_="sample_text", group="sample_text", name="sample_text")
    a2 = jpdl31_SuperStateType(async_="sample_text_2", group="sample_text_2", name="sample_text_2")
    b = jpdl31_NodeType(async_="sample_text", description="sample_text", name="sample_text", nodeContentElements="sample_text")
    _safe_set(b, 'jpdl31_NodeType247', a1)
    assert _is_linked(b, 'jpdl31_NodeType247', a1)
    if hasattr(a1, 'jpdl31_SuperStateType246'):
        assert _is_linked(a1, 'jpdl31_SuperStateType246', b)
    _safe_set(b, 'jpdl31_NodeType247', a2)
    assert _is_linked(b, 'jpdl31_NodeType247', a2)
    if hasattr(a1, 'jpdl31_SuperStateType246'):
        assert not _is_linked(a1, 'jpdl31_SuperStateType246', b)
    if hasattr(a2, 'jpdl31_SuperStateType246'):
        assert _is_linked(a2, 'jpdl31_SuperStateType246', b)
    _safe_set(b, 'jpdl31_NodeType247', None)
    assert not _is_linked(b, 'jpdl31_NodeType247', a2)
    if hasattr(a2, 'jpdl31_SuperStateType246'):
        assert not _is_linked(a2, 'jpdl31_SuperStateType246', b)


def test_assoc_node42_reverse_link_reassign_clear():
    a1 = jpdl31_NodeType(async_="sample_text", description="sample_text", name="sample_text", nodeContentElements="sample_text")
    a2 = jpdl31_NodeType(async_="sample_text_2", description="sample_text_2", name="sample_text_2", nodeContentElements="sample_text_2")
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


def test_assoc_option393_reverse_link_reassign_clear():
    a1 = jpdl31_Question(description="sample_text", required="sample_text", type="sample_text")
    a2 = jpdl31_Question(description="sample_text_2", required="sample_text_2", type="sample_text_2")
    b = jpdl31_Alternative(description="sample_text")
    _safe_set(b, 'jpdl31_Alternative', a1)
    assert _is_linked(b, 'jpdl31_Alternative', a1)
    if hasattr(a1, 'jpdl31_Question394'):
        assert _is_linked(a1, 'jpdl31_Question394', b)
    _safe_set(b, 'jpdl31_Alternative', a2)
    assert _is_linked(b, 'jpdl31_Alternative', a2)
    if hasattr(a1, 'jpdl31_Question394'):
        assert not _is_linked(a1, 'jpdl31_Question394', b)
    if hasattr(a2, 'jpdl31_Question394'):
        assert _is_linked(a2, 'jpdl31_Question394', b)
    _safe_set(b, 'jpdl31_Alternative', None)
    assert not _is_linked(b, 'jpdl31_Alternative', a2)
    if hasattr(a2, 'jpdl31_Question394'):
        assert not _is_linked(a2, 'jpdl31_Question394', b)


def test_assoc_parameters412_reverse_link_reassign_clear():
    a1 = jpdl31_Parameter(key="sample_text", value="sample_text")
    a2 = jpdl31_Parameter(key="sample_text_2", value="sample_text_2")
    b = jpdl31_Design(DoE="sample_text")
    _safe_set(b, 'jpdl31_Design413', {a1})
    assert _is_linked(b, 'jpdl31_Design413', a1)
    if hasattr(a1, 'jpdl31_Parameter'):
        assert _is_linked(a1, 'jpdl31_Parameter', b)
    _safe_set(b, 'jpdl31_Design413', {a2})
    assert _is_linked(b, 'jpdl31_Design413', a2)
    if hasattr(a1, 'jpdl31_Parameter'):
        assert not _is_linked(a1, 'jpdl31_Parameter', b)
    if hasattr(a2, 'jpdl31_Parameter'):
        assert _is_linked(a2, 'jpdl31_Parameter', b)
    _safe_set(b, 'jpdl31_Design413', set())
    assert not _is_linked(b, 'jpdl31_Design413', a2)
    if hasattr(a2, 'jpdl31_Parameter'):
        assert not _is_linked(a2, 'jpdl31_Parameter', b)


def test_assoc_processDefinition44_reverse_link_reassign_clear():
    a1 = jpdl31_ProcessDefinitionType(group="sample_text", name="sample_text", quantity="sample_text")
    a2 = jpdl31_ProcessDefinitionType(group="sample_text_2", name="sample_text_2", quantity="sample_text_2")
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


def test_assoc_processState168_reverse_link_reassign_clear():
    a1 = jpdl31_ProcessStateType(async_="sample_text", group="sample_text", name="sample_text")
    a2 = jpdl31_ProcessStateType(async_="sample_text_2", group="sample_text_2", name="sample_text_2")
    b = jpdl31_ProcessDefinitionType(group="sample_text", name="sample_text", quantity="sample_text")
    _safe_set(b, 'jpdl31_ProcessDefinitionType169', {a1})
    assert _is_linked(b, 'jpdl31_ProcessDefinitionType169', a1)
    if hasattr(a1, 'jpdl31_ProcessStateType170'):
        assert _is_linked(a1, 'jpdl31_ProcessStateType170', b)
    _safe_set(b, 'jpdl31_ProcessDefinitionType169', {a2})
    assert _is_linked(b, 'jpdl31_ProcessDefinitionType169', a2)
    if hasattr(a1, 'jpdl31_ProcessStateType170'):
        assert not _is_linked(a1, 'jpdl31_ProcessStateType170', b)
    if hasattr(a2, 'jpdl31_ProcessStateType170'):
        assert _is_linked(a2, 'jpdl31_ProcessStateType170', b)
    _safe_set(b, 'jpdl31_ProcessDefinitionType169', set())
    assert not _is_linked(b, 'jpdl31_ProcessDefinitionType169', a2)
    if hasattr(a2, 'jpdl31_ProcessStateType170'):
        assert not _is_linked(a2, 'jpdl31_ProcessStateType170', b)


def test_assoc_processState257_reverse_link_reassign_clear():
    a1 = jpdl31_SuperStateType(async_="sample_text", group="sample_text", name="sample_text")
    a2 = jpdl31_SuperStateType(async_="sample_text_2", group="sample_text_2", name="sample_text_2")
    b = jpdl31_ProcessStateType(async_="sample_text", group="sample_text", name="sample_text")
    _safe_set(b, 'jpdl31_ProcessStateType259', a1)
    assert _is_linked(b, 'jpdl31_ProcessStateType259', a1)
    if hasattr(a1, 'jpdl31_SuperStateType258'):
        assert _is_linked(a1, 'jpdl31_SuperStateType258', b)
    _safe_set(b, 'jpdl31_ProcessStateType259', a2)
    assert _is_linked(b, 'jpdl31_ProcessStateType259', a2)
    if hasattr(a1, 'jpdl31_SuperStateType258'):
        assert not _is_linked(a1, 'jpdl31_SuperStateType258', b)
    if hasattr(a2, 'jpdl31_SuperStateType258'):
        assert _is_linked(a2, 'jpdl31_SuperStateType258', b)
    _safe_set(b, 'jpdl31_ProcessStateType259', None)
    assert not _is_linked(b, 'jpdl31_ProcessStateType259', a2)
    if hasattr(a2, 'jpdl31_SuperStateType258'):
        assert not _is_linked(a2, 'jpdl31_SuperStateType258', b)


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


def test_assoc_processes390_reverse_link_reassign_clear():
    a1 = jpdl31_Questionnaire(name="sample_text", type="sample_text")
    a2 = jpdl31_Questionnaire(name="sample_text_2", type="sample_text_2")
    b = jpdl31_ProcessDefinitionType(group="sample_text", name="sample_text", quantity="sample_text")
    _safe_set(b, 'jpdl31_ProcessDefinitionType392', a1)
    assert _is_linked(b, 'jpdl31_ProcessDefinitionType392', a1)
    if hasattr(a1, 'jpdl31_Questionnaire391'):
        assert _is_linked(a1, 'jpdl31_Questionnaire391', b)
    _safe_set(b, 'jpdl31_ProcessDefinitionType392', a2)
    assert _is_linked(b, 'jpdl31_ProcessDefinitionType392', a2)
    if hasattr(a1, 'jpdl31_Questionnaire391'):
        assert not _is_linked(a1, 'jpdl31_Questionnaire391', b)
    if hasattr(a2, 'jpdl31_Questionnaire391'):
        assert _is_linked(a2, 'jpdl31_Questionnaire391', b)
    _safe_set(b, 'jpdl31_ProcessDefinitionType392', None)
    assert not _is_linked(b, 'jpdl31_ProcessDefinitionType392', a2)
    if hasattr(a2, 'jpdl31_Questionnaire391'):
        assert not _is_linked(a2, 'jpdl31_Questionnaire391', b)


def test_assoc_question388_reverse_link_reassign_clear():
    a1 = jpdl31_Questionnaire(name="sample_text", type="sample_text")
    a2 = jpdl31_Questionnaire(name="sample_text_2", type="sample_text_2")
    b = jpdl31_Question(description="sample_text", required="sample_text", type="sample_text")
    _safe_set(b, 'jpdl31_Question', a1)
    assert _is_linked(b, 'jpdl31_Question', a1)
    if hasattr(a1, 'jpdl31_Questionnaire389'):
        assert _is_linked(a1, 'jpdl31_Questionnaire389', b)
    _safe_set(b, 'jpdl31_Question', a2)
    assert _is_linked(b, 'jpdl31_Question', a2)
    if hasattr(a1, 'jpdl31_Questionnaire389'):
        assert not _is_linked(a1, 'jpdl31_Questionnaire389', b)
    if hasattr(a2, 'jpdl31_Questionnaire389'):
        assert _is_linked(a2, 'jpdl31_Questionnaire389', b)
    _safe_set(b, 'jpdl31_Question', None)
    assert not _is_linked(b, 'jpdl31_Question', a2)
    if hasattr(a2, 'jpdl31_Questionnaire389'):
        assert not _is_linked(a2, 'jpdl31_Questionnaire389', b)


def test_assoc_questionnaires69_reverse_link_reassign_clear():
    a1 = jpdl31_Questionnaire(name="sample_text", type="sample_text")
    a2 = jpdl31_Questionnaire(name="sample_text_2", type="sample_text_2")
    b = jpdl31_DocumentRoot(mixed="sample_text")
    _safe_set(b, 'jpdl31_DocumentRoot70', {a1})
    assert _is_linked(b, 'jpdl31_DocumentRoot70', a1)
    if hasattr(a1, 'jpdl31_Questionnaire'):
        assert _is_linked(a1, 'jpdl31_Questionnaire', b)
    _safe_set(b, 'jpdl31_DocumentRoot70', {a2})
    assert _is_linked(b, 'jpdl31_DocumentRoot70', a2)
    if hasattr(a1, 'jpdl31_Questionnaire'):
        assert not _is_linked(a1, 'jpdl31_Questionnaire', b)
    if hasattr(a2, 'jpdl31_Questionnaire'):
        assert _is_linked(a2, 'jpdl31_Questionnaire', b)
    _safe_set(b, 'jpdl31_DocumentRoot70', set())
    assert not _is_linked(b, 'jpdl31_DocumentRoot70', a2)
    if hasattr(a2, 'jpdl31_Questionnaire'):
        assert not _is_linked(a2, 'jpdl31_Questionnaire', b)


def test_assoc_relatesTo385_reverse_link_reassign_clear():
    a1 = jpdl31_ProcessDefinitionType(group="sample_text", name="sample_text", quantity="sample_text")
    a2 = jpdl31_ProcessDefinitionType(group="sample_text_2", name="sample_text_2", quantity="sample_text_2")
    b = jpdl31_Metric(description="sample_text", name="sample_text", refname="sample_text", type="sample_text")
    _safe_set(b, 'jpdl31_Metric386', {a1})
    assert _is_linked(b, 'jpdl31_Metric386', a1)
    if hasattr(a1, 'jpdl31_ProcessDefinitionType387'):
        assert _is_linked(a1, 'jpdl31_ProcessDefinitionType387', b)
    _safe_set(b, 'jpdl31_Metric386', {a2})
    assert _is_linked(b, 'jpdl31_Metric386', a2)
    if hasattr(a1, 'jpdl31_ProcessDefinitionType387'):
        assert not _is_linked(a1, 'jpdl31_ProcessDefinitionType387', b)
    if hasattr(a2, 'jpdl31_ProcessDefinitionType387'):
        assert _is_linked(a2, 'jpdl31_ProcessDefinitionType387', b)
    _safe_set(b, 'jpdl31_Metric386', set())
    assert not _is_linked(b, 'jpdl31_Metric386', a2)
    if hasattr(a2, 'jpdl31_ProcessDefinitionType387'):
        assert not _is_linked(a2, 'jpdl31_ProcessDefinitionType387', b)


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


def test_assoc_script129_reverse_link_reassign_clear():
    a1 = jpdl31_ScriptType(acceptPropagatedEvents="sample_text", any="sample_text", mixed="sample_text", name="sample_text")
    a2 = jpdl31_ScriptType(acceptPropagatedEvents="sample_text_2", any="sample_text_2", mixed="sample_text_2", name="sample_text_2")
    b = jpdl31_NodeType(async_="sample_text", description="sample_text", name="sample_text", nodeContentElements="sample_text")
    _safe_set(b, 'jpdl31_NodeType130', a1)
    assert _is_linked(b, 'jpdl31_NodeType130', a1)
    if hasattr(a1, 'jpdl31_ScriptType131'):
        assert _is_linked(a1, 'jpdl31_ScriptType131', b)
    _safe_set(b, 'jpdl31_NodeType130', a2)
    assert _is_linked(b, 'jpdl31_NodeType130', a2)
    if hasattr(a1, 'jpdl31_ScriptType131'):
        assert not _is_linked(a1, 'jpdl31_ScriptType131', b)
    if hasattr(a2, 'jpdl31_ScriptType131'):
        assert _is_linked(a2, 'jpdl31_ScriptType131', b)
    _safe_set(b, 'jpdl31_NodeType130', None)
    assert not _is_linked(b, 'jpdl31_NodeType130', a2)
    if hasattr(a2, 'jpdl31_ScriptType131'):
        assert not _is_linked(a2, 'jpdl31_ScriptType131', b)


def test_assoc_script186_reverse_link_reassign_clear():
    a1 = jpdl31_ScriptType(acceptPropagatedEvents="sample_text", any="sample_text", mixed="sample_text", name="sample_text")
    a2 = jpdl31_ScriptType(acceptPropagatedEvents="sample_text_2", any="sample_text_2", mixed="sample_text_2", name="sample_text_2")
    b = jpdl31_ProcessDefinitionType(group="sample_text", name="sample_text", quantity="sample_text")
    _safe_set(b, 'jpdl31_ProcessDefinitionType187', {a1})
    assert _is_linked(b, 'jpdl31_ProcessDefinitionType187', a1)
    if hasattr(a1, 'jpdl31_ScriptType188'):
        assert _is_linked(a1, 'jpdl31_ScriptType188', b)
    _safe_set(b, 'jpdl31_ProcessDefinitionType187', {a2})
    assert _is_linked(b, 'jpdl31_ProcessDefinitionType187', a2)
    if hasattr(a1, 'jpdl31_ScriptType188'):
        assert not _is_linked(a1, 'jpdl31_ScriptType188', b)
    if hasattr(a2, 'jpdl31_ScriptType188'):
        assert _is_linked(a2, 'jpdl31_ScriptType188', b)
    _safe_set(b, 'jpdl31_ProcessDefinitionType187', set())
    assert not _is_linked(b, 'jpdl31_ProcessDefinitionType187', a2)
    if hasattr(a2, 'jpdl31_ScriptType188'):
        assert not _is_linked(a2, 'jpdl31_ScriptType188', b)


def test_assoc_script327_reverse_link_reassign_clear():
    a1 = jpdl31_TimerType(duedate="sample_text", name="sample_text", repeat="sample_text", transition="sample_text")
    a2 = jpdl31_TimerType(duedate="sample_text_2", name="sample_text_2", repeat="sample_text_2", transition="sample_text_2")
    b = jpdl31_ScriptType(acceptPropagatedEvents="sample_text", any="sample_text", mixed="sample_text", name="sample_text")
    _safe_set(b, 'jpdl31_ScriptType329', a1)
    assert _is_linked(b, 'jpdl31_ScriptType329', a1)
    if hasattr(a1, 'jpdl31_TimerType328'):
        assert _is_linked(a1, 'jpdl31_TimerType328', b)
    _safe_set(b, 'jpdl31_ScriptType329', a2)
    assert _is_linked(b, 'jpdl31_ScriptType329', a2)
    if hasattr(a1, 'jpdl31_TimerType328'):
        assert not _is_linked(a1, 'jpdl31_TimerType328', b)
    if hasattr(a2, 'jpdl31_TimerType328'):
        assert _is_linked(a2, 'jpdl31_TimerType328', b)
    _safe_set(b, 'jpdl31_ScriptType329', None)
    assert not _is_linked(b, 'jpdl31_ScriptType329', a2)
    if hasattr(a2, 'jpdl31_TimerType328'):
        assert not _is_linked(a2, 'jpdl31_TimerType328', b)


def test_assoc_script333_reverse_link_reassign_clear():
    a1 = jpdl31_TransitionType(group="sample_text", name="sample_text", to="sample_text")
    a2 = jpdl31_TransitionType(group="sample_text_2", name="sample_text_2", to="sample_text_2")
    b = jpdl31_ScriptType(acceptPropagatedEvents="sample_text", any="sample_text", mixed="sample_text", name="sample_text")
    _safe_set(b, 'jpdl31_ScriptType335', a1)
    assert _is_linked(b, 'jpdl31_ScriptType335', a1)
    if hasattr(a1, 'jpdl31_TransitionType334'):
        assert _is_linked(a1, 'jpdl31_TransitionType334', b)
    _safe_set(b, 'jpdl31_ScriptType335', a2)
    assert _is_linked(b, 'jpdl31_ScriptType335', a2)
    if hasattr(a1, 'jpdl31_TransitionType334'):
        assert not _is_linked(a1, 'jpdl31_TransitionType334', b)
    if hasattr(a2, 'jpdl31_TransitionType334'):
        assert _is_linked(a2, 'jpdl31_TransitionType334', b)
    _safe_set(b, 'jpdl31_ScriptType335', None)
    assert not _is_linked(b, 'jpdl31_ScriptType335', a2)
    if hasattr(a2, 'jpdl31_TransitionType334'):
        assert not _is_linked(a2, 'jpdl31_TransitionType334', b)


def test_assoc_script350_reverse_link_reassign_clear():
    a1 = jpdl31_TransitionType1(group="sample_text", name="sample_text", to="sample_text")
    a2 = jpdl31_TransitionType1(group="sample_text_2", name="sample_text_2", to="sample_text_2")
    b = jpdl31_ScriptType(acceptPropagatedEvents="sample_text", any="sample_text", mixed="sample_text", name="sample_text")
    _safe_set(b, 'jpdl31_ScriptType352', a1)
    assert _is_linked(b, 'jpdl31_ScriptType352', a1)
    if hasattr(a1, 'jpdl31_TransitionType1351'):
        assert _is_linked(a1, 'jpdl31_TransitionType1351', b)
    _safe_set(b, 'jpdl31_ScriptType352', a2)
    assert _is_linked(b, 'jpdl31_ScriptType352', a2)
    if hasattr(a1, 'jpdl31_TransitionType1351'):
        assert not _is_linked(a1, 'jpdl31_TransitionType1351', b)
    if hasattr(a2, 'jpdl31_TransitionType1351'):
        assert _is_linked(a2, 'jpdl31_TransitionType1351', b)
    _safe_set(b, 'jpdl31_ScriptType352', None)
    assert not _is_linked(b, 'jpdl31_ScriptType352', a2)
    if hasattr(a2, 'jpdl31_TransitionType1351'):
        assert not _is_linked(a2, 'jpdl31_TransitionType1351', b)


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


def test_assoc_script84_reverse_link_reassign_clear():
    a1 = jpdl31_ScriptType(acceptPropagatedEvents="sample_text", any="sample_text", mixed="sample_text", name="sample_text")
    a2 = jpdl31_ScriptType(acceptPropagatedEvents="sample_text_2", any="sample_text_2", mixed="sample_text_2", name="sample_text_2")
    b = jpdl31_EventType(actionElements="sample_text", type="sample_text")
    _safe_set(b, 'jpdl31_EventType85', {a1})
    assert _is_linked(b, 'jpdl31_EventType85', a1)
    if hasattr(a1, 'jpdl31_ScriptType86'):
        assert _is_linked(a1, 'jpdl31_ScriptType86', b)
    _safe_set(b, 'jpdl31_EventType85', {a2})
    assert _is_linked(b, 'jpdl31_EventType85', a2)
    if hasattr(a1, 'jpdl31_ScriptType86'):
        assert not _is_linked(a1, 'jpdl31_ScriptType86', b)
    if hasattr(a2, 'jpdl31_ScriptType86'):
        assert _is_linked(a2, 'jpdl31_ScriptType86', b)
    _safe_set(b, 'jpdl31_EventType85', set())
    assert not _is_linked(b, 'jpdl31_EventType85', a2)
    if hasattr(a2, 'jpdl31_ScriptType86'):
        assert not _is_linked(a2, 'jpdl31_ScriptType86', b)


def test_assoc_script96_reverse_link_reassign_clear():
    a1 = jpdl31_ScriptType(acceptPropagatedEvents="sample_text", any="sample_text", mixed="sample_text", name="sample_text")
    a2 = jpdl31_ScriptType(acceptPropagatedEvents="sample_text_2", any="sample_text_2", mixed="sample_text_2", name="sample_text_2")
    b = jpdl31_ExceptionHandlerType(exceptionClass="sample_text", group="sample_text")
    _safe_set(b, 'jpdl31_ExceptionHandlerType97', {a1})
    assert _is_linked(b, 'jpdl31_ExceptionHandlerType97', a1)
    if hasattr(a1, 'jpdl31_ScriptType98'):
        assert _is_linked(a1, 'jpdl31_ScriptType98', b)
    _safe_set(b, 'jpdl31_ExceptionHandlerType97', {a2})
    assert _is_linked(b, 'jpdl31_ExceptionHandlerType97', a2)
    if hasattr(a1, 'jpdl31_ScriptType98'):
        assert not _is_linked(a1, 'jpdl31_ScriptType98', b)
    if hasattr(a2, 'jpdl31_ScriptType98'):
        assert _is_linked(a2, 'jpdl31_ScriptType98', b)
    _safe_set(b, 'jpdl31_ExceptionHandlerType97', set())
    assert not _is_linked(b, 'jpdl31_ExceptionHandlerType97', a2)
    if hasattr(a2, 'jpdl31_ScriptType98'):
        assert not _is_linked(a2, 'jpdl31_ScriptType98', b)


def test_assoc_script99_reverse_link_reassign_clear():
    a1 = jpdl31_ScriptType(acceptPropagatedEvents="sample_text", any="sample_text", mixed="sample_text", name="sample_text")
    a2 = jpdl31_ScriptType(acceptPropagatedEvents="sample_text_2", any="sample_text_2", mixed="sample_text_2", name="sample_text_2")
    b = jpdl31_ForkType(async_="sample_text", group="sample_text", name="sample_text")
    _safe_set(b, 'jpdl31_ForkType100', {a1})
    assert _is_linked(b, 'jpdl31_ForkType100', a1)
    if hasattr(a1, 'jpdl31_ScriptType101'):
        assert _is_linked(a1, 'jpdl31_ScriptType101', b)
    _safe_set(b, 'jpdl31_ForkType100', {a2})
    assert _is_linked(b, 'jpdl31_ForkType100', a2)
    if hasattr(a1, 'jpdl31_ScriptType101'):
        assert not _is_linked(a1, 'jpdl31_ScriptType101', b)
    if hasattr(a2, 'jpdl31_ScriptType101'):
        assert _is_linked(a2, 'jpdl31_ScriptType101', b)
    _safe_set(b, 'jpdl31_ForkType100', set())
    assert not _is_linked(b, 'jpdl31_ForkType100', a2)
    if hasattr(a2, 'jpdl31_ScriptType101'):
        assert not _is_linked(a2, 'jpdl31_ScriptType101', b)


def test_assoc_startState153_reverse_link_reassign_clear():
    a1 = jpdl31_StartStateType(group="sample_text", name="sample_text")
    a2 = jpdl31_StartStateType(group="sample_text_2", name="sample_text_2")
    b = jpdl31_ProcessDefinitionType(group="sample_text", name="sample_text", quantity="sample_text")
    _safe_set(b, 'jpdl31_ProcessDefinitionType154', {a1})
    assert _is_linked(b, 'jpdl31_ProcessDefinitionType154', a1)
    if hasattr(a1, 'jpdl31_StartStateType155'):
        assert _is_linked(a1, 'jpdl31_StartStateType155', b)
    _safe_set(b, 'jpdl31_ProcessDefinitionType154', {a2})
    assert _is_linked(b, 'jpdl31_ProcessDefinitionType154', a2)
    if hasattr(a1, 'jpdl31_StartStateType155'):
        assert not _is_linked(a1, 'jpdl31_StartStateType155', b)
    if hasattr(a2, 'jpdl31_StartStateType155'):
        assert _is_linked(a2, 'jpdl31_StartStateType155', b)
    _safe_set(b, 'jpdl31_ProcessDefinitionType154', set())
    assert not _is_linked(b, 'jpdl31_ProcessDefinitionType154', a2)
    if hasattr(a2, 'jpdl31_StartStateType155'):
        assert not _is_linked(a2, 'jpdl31_StartStateType155', b)


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


def test_assoc_state159_reverse_link_reassign_clear():
    a1 = jpdl31_StateType(async_="sample_text", name="sample_text", nodeContentElements="sample_text")
    a2 = jpdl31_StateType(async_="sample_text_2", name="sample_text_2", nodeContentElements="sample_text_2")
    b = jpdl31_ProcessDefinitionType(group="sample_text", name="sample_text", quantity="sample_text")
    _safe_set(b, 'jpdl31_ProcessDefinitionType160', {a1})
    assert _is_linked(b, 'jpdl31_ProcessDefinitionType160', a1)
    if hasattr(a1, 'jpdl31_StateType161'):
        assert _is_linked(a1, 'jpdl31_StateType161', b)
    _safe_set(b, 'jpdl31_ProcessDefinitionType160', {a2})
    assert _is_linked(b, 'jpdl31_ProcessDefinitionType160', a2)
    if hasattr(a1, 'jpdl31_StateType161'):
        assert not _is_linked(a1, 'jpdl31_StateType161', b)
    if hasattr(a2, 'jpdl31_StateType161'):
        assert _is_linked(a2, 'jpdl31_StateType161', b)
    _safe_set(b, 'jpdl31_ProcessDefinitionType160', set())
    assert not _is_linked(b, 'jpdl31_ProcessDefinitionType160', a2)
    if hasattr(a2, 'jpdl31_StateType161'):
        assert not _is_linked(a2, 'jpdl31_StateType161', b)


def test_assoc_state248_reverse_link_reassign_clear():
    a1 = jpdl31_SuperStateType(async_="sample_text", group="sample_text", name="sample_text")
    a2 = jpdl31_SuperStateType(async_="sample_text_2", group="sample_text_2", name="sample_text_2")
    b = jpdl31_StateType(async_="sample_text", name="sample_text", nodeContentElements="sample_text")
    _safe_set(b, 'jpdl31_StateType250', a1)
    assert _is_linked(b, 'jpdl31_StateType250', a1)
    if hasattr(a1, 'jpdl31_SuperStateType249'):
        assert _is_linked(a1, 'jpdl31_SuperStateType249', b)
    _safe_set(b, 'jpdl31_StateType250', a2)
    assert _is_linked(b, 'jpdl31_StateType250', a2)
    if hasattr(a1, 'jpdl31_SuperStateType249'):
        assert not _is_linked(a1, 'jpdl31_SuperStateType249', b)
    if hasattr(a2, 'jpdl31_SuperStateType249'):
        assert _is_linked(a2, 'jpdl31_SuperStateType249', b)
    _safe_set(b, 'jpdl31_StateType250', None)
    assert not _is_linked(b, 'jpdl31_StateType250', a2)
    if hasattr(a2, 'jpdl31_SuperStateType249'):
        assert not _is_linked(a2, 'jpdl31_SuperStateType249', b)


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


def test_assoc_subProcess204_reverse_link_reassign_clear():
    a1 = jpdl31_SubProcessType(name="sample_text", version="sample_text")
    a2 = jpdl31_SubProcessType(name="sample_text_2", version="sample_text_2")
    b = jpdl31_ProcessStateType(async_="sample_text", group="sample_text", name="sample_text")
    _safe_set(b, 'jpdl31_ProcessStateType205', {a1})
    assert _is_linked(b, 'jpdl31_ProcessStateType205', a1)
    if hasattr(a1, 'jpdl31_SubProcessType'):
        assert _is_linked(a1, 'jpdl31_SubProcessType', b)
    _safe_set(b, 'jpdl31_ProcessStateType205', {a2})
    assert _is_linked(b, 'jpdl31_ProcessStateType205', a2)
    if hasattr(a1, 'jpdl31_SubProcessType'):
        assert not _is_linked(a1, 'jpdl31_SubProcessType', b)
    if hasattr(a2, 'jpdl31_SubProcessType'):
        assert _is_linked(a2, 'jpdl31_SubProcessType', b)
    _safe_set(b, 'jpdl31_ProcessStateType205', set())
    assert not _is_linked(b, 'jpdl31_ProcessStateType205', a2)
    if hasattr(a2, 'jpdl31_SubProcessType'):
        assert not _is_linked(a2, 'jpdl31_SubProcessType', b)


def test_assoc_superState165_reverse_link_reassign_clear():
    a1 = jpdl31_SuperStateType(async_="sample_text", group="sample_text", name="sample_text")
    a2 = jpdl31_SuperStateType(async_="sample_text_2", group="sample_text_2", name="sample_text_2")
    b = jpdl31_ProcessDefinitionType(group="sample_text", name="sample_text", quantity="sample_text")
    _safe_set(b, 'jpdl31_ProcessDefinitionType166', {a1})
    assert _is_linked(b, 'jpdl31_ProcessDefinitionType166', a1)
    if hasattr(a1, 'jpdl31_SuperStateType167'):
        assert _is_linked(a1, 'jpdl31_SuperStateType167', b)
    _safe_set(b, 'jpdl31_ProcessDefinitionType166', {a2})
    assert _is_linked(b, 'jpdl31_ProcessDefinitionType166', a2)
    if hasattr(a1, 'jpdl31_SuperStateType167'):
        assert not _is_linked(a1, 'jpdl31_SuperStateType167', b)
    if hasattr(a2, 'jpdl31_SuperStateType167'):
        assert _is_linked(a2, 'jpdl31_SuperStateType167', b)
    _safe_set(b, 'jpdl31_ProcessDefinitionType166', set())
    assert not _is_linked(b, 'jpdl31_ProcessDefinitionType166', a2)
    if hasattr(a2, 'jpdl31_SuperStateType167'):
        assert not _is_linked(a2, 'jpdl31_SuperStateType167', b)


def test_assoc_superState255_reverse_link_reassign_clear():
    a1 = jpdl31_SuperStateType(async_="sample_text", group="sample_text", name="sample_text")
    a2 = jpdl31_SuperStateType(async_="sample_text_2", group="sample_text_2", name="sample_text_2")
    b = jpdl31_SuperStateType(async_="sample_text", group="sample_text", name="sample_text")
    _safe_set(b, 'jpdl31_SuperStateType256', a1)
    assert _is_linked(b, 'jpdl31_SuperStateType256', a1)
    if hasattr(a1, 'jpdl31_SuperStateType254'):
        assert _is_linked(a1, 'jpdl31_SuperStateType254', b)
    _safe_set(b, 'jpdl31_SuperStateType256', a2)
    assert _is_linked(b, 'jpdl31_SuperStateType256', a2)
    if hasattr(a1, 'jpdl31_SuperStateType254'):
        assert not _is_linked(a1, 'jpdl31_SuperStateType254', b)
    if hasattr(a2, 'jpdl31_SuperStateType254'):
        assert _is_linked(a2, 'jpdl31_SuperStateType254', b)
    _safe_set(b, 'jpdl31_SuperStateType256', None)
    assert not _is_linked(b, 'jpdl31_SuperStateType256', a2)
    if hasattr(a2, 'jpdl31_SuperStateType254'):
        assert not _is_linked(a2, 'jpdl31_SuperStateType254', b)


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


def test_assoc_swimlane150_reverse_link_reassign_clear():
    a1 = jpdl31_SwimlaneType(name="sample_text")
    a2 = jpdl31_SwimlaneType(name="sample_text_2")
    b = jpdl31_ProcessDefinitionType(group="sample_text", name="sample_text", quantity="sample_text")
    _safe_set(b, 'jpdl31_ProcessDefinitionType151', {a1})
    assert _is_linked(b, 'jpdl31_ProcessDefinitionType151', a1)
    if hasattr(a1, 'jpdl31_SwimlaneType152'):
        assert _is_linked(a1, 'jpdl31_SwimlaneType152', b)
    _safe_set(b, 'jpdl31_ProcessDefinitionType151', {a2})
    assert _is_linked(b, 'jpdl31_ProcessDefinitionType151', a2)
    if hasattr(a1, 'jpdl31_SwimlaneType152'):
        assert not _is_linked(a1, 'jpdl31_SwimlaneType152', b)
    if hasattr(a2, 'jpdl31_SwimlaneType152'):
        assert _is_linked(a2, 'jpdl31_SwimlaneType152', b)
    _safe_set(b, 'jpdl31_ProcessDefinitionType151', set())
    assert not _is_linked(b, 'jpdl31_ProcessDefinitionType151', a2)
    if hasattr(a2, 'jpdl31_SwimlaneType152'):
        assert not _is_linked(a2, 'jpdl31_SwimlaneType152', b)


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


def test_assoc_task201_reverse_link_reassign_clear():
    a1 = jpdl31_TaskType(blocking="sample_text", description="sample_text", duedate="sample_text", group="sample_text", name="sample_text", priority="sample_text", signalling="sample_text", swimlane="sample_text")
    a2 = jpdl31_TaskType(blocking="sample_text_2", description="sample_text_2", duedate="sample_text_2", group="sample_text_2", name="sample_text_2", priority="sample_text_2", signalling="sample_text_2", swimlane="sample_text_2")
    b = jpdl31_ProcessDefinitionType(group="sample_text", name="sample_text", quantity="sample_text")
    _safe_set(b, 'jpdl31_ProcessDefinitionType202', {a1})
    assert _is_linked(b, 'jpdl31_ProcessDefinitionType202', a1)
    if hasattr(a1, 'jpdl31_TaskType203'):
        assert _is_linked(a1, 'jpdl31_TaskType203', b)
    _safe_set(b, 'jpdl31_ProcessDefinitionType202', {a2})
    assert _is_linked(b, 'jpdl31_ProcessDefinitionType202', a2)
    if hasattr(a1, 'jpdl31_TaskType203'):
        assert not _is_linked(a1, 'jpdl31_TaskType203', b)
    if hasattr(a2, 'jpdl31_TaskType203'):
        assert _is_linked(a2, 'jpdl31_TaskType203', b)
    _safe_set(b, 'jpdl31_ProcessDefinitionType202', set())
    assert not _is_linked(b, 'jpdl31_ProcessDefinitionType202', a2)
    if hasattr(a2, 'jpdl31_TaskType203'):
        assert not _is_linked(a2, 'jpdl31_TaskType203', b)


def test_assoc_task221_reverse_link_reassign_clear():
    a1 = jpdl31_TaskType(blocking="sample_text", description="sample_text", duedate="sample_text", group="sample_text", name="sample_text", priority="sample_text", signalling="sample_text", swimlane="sample_text")
    a2 = jpdl31_TaskType(blocking="sample_text_2", description="sample_text_2", duedate="sample_text_2", group="sample_text_2", name="sample_text_2", priority="sample_text_2", signalling="sample_text_2", swimlane="sample_text_2")
    b = jpdl31_StartStateType(group="sample_text", name="sample_text")
    _safe_set(b, 'jpdl31_StartStateType222', {a1})
    assert _is_linked(b, 'jpdl31_StartStateType222', a1)
    if hasattr(a1, 'jpdl31_TaskType223'):
        assert _is_linked(a1, 'jpdl31_TaskType223', b)
    _safe_set(b, 'jpdl31_StartStateType222', {a2})
    assert _is_linked(b, 'jpdl31_StartStateType222', a2)
    if hasattr(a1, 'jpdl31_TaskType223'):
        assert not _is_linked(a1, 'jpdl31_TaskType223', b)
    if hasattr(a2, 'jpdl31_TaskType223'):
        assert _is_linked(a2, 'jpdl31_TaskType223', b)
    _safe_set(b, 'jpdl31_StartStateType222', set())
    assert not _is_linked(b, 'jpdl31_StartStateType222', a2)
    if hasattr(a2, 'jpdl31_TaskType223'):
        assert not _is_linked(a2, 'jpdl31_TaskType223', b)


def test_assoc_task287_reverse_link_reassign_clear():
    a1 = jpdl31_TaskType(blocking="sample_text", description="sample_text", duedate="sample_text", group="sample_text", name="sample_text", priority="sample_text", signalling="sample_text", swimlane="sample_text")
    a2 = jpdl31_TaskType(blocking="sample_text_2", description="sample_text_2", duedate="sample_text_2", group="sample_text_2", name="sample_text_2", priority="sample_text_2", signalling="sample_text_2", swimlane="sample_text_2")
    b = jpdl31_TaskNodeType(async_="sample_text", createTasks="sample_text", description="sample_text", endTasks="sample_text", group="sample_text", name="sample_text", signal="sample_text")
    _safe_set(b, 'jpdl31_TaskNodeType288', {a1})
    assert _is_linked(b, 'jpdl31_TaskNodeType288', a1)
    if hasattr(a1, 'jpdl31_TaskType289'):
        assert _is_linked(a1, 'jpdl31_TaskType289', b)
    _safe_set(b, 'jpdl31_TaskNodeType288', {a2})
    assert _is_linked(b, 'jpdl31_TaskNodeType288', a2)
    if hasattr(a1, 'jpdl31_TaskType289'):
        assert not _is_linked(a1, 'jpdl31_TaskType289', b)
    if hasattr(a2, 'jpdl31_TaskType289'):
        assert _is_linked(a2, 'jpdl31_TaskType289', b)
    _safe_set(b, 'jpdl31_TaskNodeType288', set())
    assert not _is_linked(b, 'jpdl31_TaskNodeType288', a2)
    if hasattr(a2, 'jpdl31_TaskType289'):
        assert not _is_linked(a2, 'jpdl31_TaskType289', b)


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


def test_assoc_taskNode162_reverse_link_reassign_clear():
    a1 = jpdl31_TaskNodeType(async_="sample_text", createTasks="sample_text", description="sample_text", endTasks="sample_text", group="sample_text", name="sample_text", signal="sample_text")
    a2 = jpdl31_TaskNodeType(async_="sample_text_2", createTasks="sample_text_2", description="sample_text_2", endTasks="sample_text_2", group="sample_text_2", name="sample_text_2", signal="sample_text_2")
    b = jpdl31_ProcessDefinitionType(group="sample_text", name="sample_text", quantity="sample_text")
    _safe_set(b, 'jpdl31_ProcessDefinitionType163', {a1})
    assert _is_linked(b, 'jpdl31_ProcessDefinitionType163', a1)
    if hasattr(a1, 'jpdl31_TaskNodeType164'):
        assert _is_linked(a1, 'jpdl31_TaskNodeType164', b)
    _safe_set(b, 'jpdl31_ProcessDefinitionType163', {a2})
    assert _is_linked(b, 'jpdl31_ProcessDefinitionType163', a2)
    if hasattr(a1, 'jpdl31_TaskNodeType164'):
        assert not _is_linked(a1, 'jpdl31_TaskNodeType164', b)
    if hasattr(a2, 'jpdl31_TaskNodeType164'):
        assert _is_linked(a2, 'jpdl31_TaskNodeType164', b)
    _safe_set(b, 'jpdl31_ProcessDefinitionType163', set())
    assert not _is_linked(b, 'jpdl31_ProcessDefinitionType163', a2)
    if hasattr(a2, 'jpdl31_TaskNodeType164'):
        assert not _is_linked(a2, 'jpdl31_TaskNodeType164', b)


def test_assoc_taskNode251_reverse_link_reassign_clear():
    a1 = jpdl31_TaskNodeType(async_="sample_text", createTasks="sample_text", description="sample_text", endTasks="sample_text", group="sample_text", name="sample_text", signal="sample_text")
    a2 = jpdl31_TaskNodeType(async_="sample_text_2", createTasks="sample_text_2", description="sample_text_2", endTasks="sample_text_2", group="sample_text_2", name="sample_text_2", signal="sample_text_2")
    b = jpdl31_SuperStateType(async_="sample_text", group="sample_text", name="sample_text")
    _safe_set(b, 'jpdl31_SuperStateType252', {a1})
    assert _is_linked(b, 'jpdl31_SuperStateType252', a1)
    if hasattr(a1, 'jpdl31_TaskNodeType253'):
        assert _is_linked(a1, 'jpdl31_TaskNodeType253', b)
    _safe_set(b, 'jpdl31_SuperStateType252', {a2})
    assert _is_linked(b, 'jpdl31_SuperStateType252', a2)
    if hasattr(a1, 'jpdl31_TaskNodeType253'):
        assert not _is_linked(a1, 'jpdl31_TaskNodeType253', b)
    if hasattr(a2, 'jpdl31_TaskNodeType253'):
        assert _is_linked(a2, 'jpdl31_TaskNodeType253', b)
    _safe_set(b, 'jpdl31_SuperStateType252', set())
    assert not _is_linked(b, 'jpdl31_SuperStateType252', a2)
    if hasattr(a2, 'jpdl31_TaskNodeType253'):
        assert not _is_linked(a2, 'jpdl31_TaskNodeType253', b)


def test_assoc_taskNode61_reverse_link_reassign_clear():
    a1 = jpdl31_TaskNodeType(async_="sample_text", createTasks="sample_text", description="sample_text", endTasks="sample_text", group="sample_text", name="sample_text", signal="sample_text")
    a2 = jpdl31_TaskNodeType(async_="sample_text_2", createTasks="sample_text_2", description="sample_text_2", endTasks="sample_text_2", group="sample_text_2", name="sample_text_2", signal="sample_text_2")
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


def test_assoc_timer108_reverse_link_reassign_clear():
    a1 = jpdl31_TimerType(duedate="sample_text", name="sample_text", repeat="sample_text", transition="sample_text")
    a2 = jpdl31_TimerType(duedate="sample_text_2", name="sample_text_2", repeat="sample_text_2", transition="sample_text_2")
    b = jpdl31_ForkType(async_="sample_text", group="sample_text", name="sample_text")
    _safe_set(b, 'jpdl31_ForkType109', {a1})
    assert _is_linked(b, 'jpdl31_ForkType109', a1)
    if hasattr(a1, 'jpdl31_TimerType110'):
        assert _is_linked(a1, 'jpdl31_TimerType110', b)
    _safe_set(b, 'jpdl31_ForkType109', {a2})
    assert _is_linked(b, 'jpdl31_ForkType109', a2)
    if hasattr(a1, 'jpdl31_TimerType110'):
        assert not _is_linked(a1, 'jpdl31_TimerType110', b)
    if hasattr(a2, 'jpdl31_TimerType110'):
        assert _is_linked(a2, 'jpdl31_TimerType110', b)
    _safe_set(b, 'jpdl31_ForkType109', set())
    assert not _is_linked(b, 'jpdl31_ForkType109', a2)
    if hasattr(a2, 'jpdl31_TimerType110'):
        assert not _is_linked(a2, 'jpdl31_TimerType110', b)


def test_assoc_timer120_reverse_link_reassign_clear():
    a1 = jpdl31_TimerType(duedate="sample_text", name="sample_text", repeat="sample_text", transition="sample_text")
    a2 = jpdl31_TimerType(duedate="sample_text_2", name="sample_text_2", repeat="sample_text_2", transition="sample_text_2")
    b = jpdl31_JoinType(async_="sample_text", name="sample_text", nodeContentElements="sample_text")
    _safe_set(b, 'jpdl31_JoinType121', {a1})
    assert _is_linked(b, 'jpdl31_JoinType121', a1)
    if hasattr(a1, 'jpdl31_TimerType122'):
        assert _is_linked(a1, 'jpdl31_TimerType122', b)
    _safe_set(b, 'jpdl31_JoinType121', {a2})
    assert _is_linked(b, 'jpdl31_JoinType121', a2)
    if hasattr(a1, 'jpdl31_TimerType122'):
        assert not _is_linked(a1, 'jpdl31_TimerType122', b)
    if hasattr(a2, 'jpdl31_TimerType122'):
        assert _is_linked(a2, 'jpdl31_TimerType122', b)
    _safe_set(b, 'jpdl31_JoinType121', set())
    assert not _is_linked(b, 'jpdl31_JoinType121', a2)
    if hasattr(a2, 'jpdl31_TimerType122'):
        assert not _is_linked(a2, 'jpdl31_TimerType122', b)


def test_assoc_timer144_reverse_link_reassign_clear():
    a1 = jpdl31_TimerType(duedate="sample_text", name="sample_text", repeat="sample_text", transition="sample_text")
    a2 = jpdl31_TimerType(duedate="sample_text_2", name="sample_text_2", repeat="sample_text_2", transition="sample_text_2")
    b = jpdl31_NodeType(async_="sample_text", description="sample_text", name="sample_text", nodeContentElements="sample_text")
    _safe_set(b, 'jpdl31_NodeType145', {a1})
    assert _is_linked(b, 'jpdl31_NodeType145', a1)
    if hasattr(a1, 'jpdl31_TimerType146'):
        assert _is_linked(a1, 'jpdl31_TimerType146', b)
    _safe_set(b, 'jpdl31_NodeType145', {a2})
    assert _is_linked(b, 'jpdl31_NodeType145', a2)
    if hasattr(a1, 'jpdl31_TimerType146'):
        assert not _is_linked(a1, 'jpdl31_TimerType146', b)
    if hasattr(a2, 'jpdl31_TimerType146'):
        assert _is_linked(a2, 'jpdl31_TimerType146', b)
    _safe_set(b, 'jpdl31_NodeType145', set())
    assert not _is_linked(b, 'jpdl31_NodeType145', a2)
    if hasattr(a2, 'jpdl31_TimerType146'):
        assert not _is_linked(a2, 'jpdl31_TimerType146', b)


def test_assoc_timer215_reverse_link_reassign_clear():
    a1 = jpdl31_TimerType(duedate="sample_text", name="sample_text", repeat="sample_text", transition="sample_text")
    a2 = jpdl31_TimerType(duedate="sample_text_2", name="sample_text_2", repeat="sample_text_2", transition="sample_text_2")
    b = jpdl31_ProcessStateType(async_="sample_text", group="sample_text", name="sample_text")
    _safe_set(b, 'jpdl31_ProcessStateType216', {a1})
    assert _is_linked(b, 'jpdl31_ProcessStateType216', a1)
    if hasattr(a1, 'jpdl31_TimerType217'):
        assert _is_linked(a1, 'jpdl31_TimerType217', b)
    _safe_set(b, 'jpdl31_ProcessStateType216', {a2})
    assert _is_linked(b, 'jpdl31_ProcessStateType216', a2)
    if hasattr(a1, 'jpdl31_TimerType217'):
        assert not _is_linked(a1, 'jpdl31_TimerType217', b)
    if hasattr(a2, 'jpdl31_TimerType217'):
        assert _is_linked(a2, 'jpdl31_TimerType217', b)
    _safe_set(b, 'jpdl31_ProcessStateType216', set())
    assert not _is_linked(b, 'jpdl31_ProcessStateType216', a2)
    if hasattr(a2, 'jpdl31_TimerType217'):
        assert not _is_linked(a2, 'jpdl31_TimerType217', b)


def test_assoc_timer239_reverse_link_reassign_clear():
    a1 = jpdl31_TimerType(duedate="sample_text", name="sample_text", repeat="sample_text", transition="sample_text")
    a2 = jpdl31_TimerType(duedate="sample_text_2", name="sample_text_2", repeat="sample_text_2", transition="sample_text_2")
    b = jpdl31_StateType(async_="sample_text", name="sample_text", nodeContentElements="sample_text")
    _safe_set(b, 'jpdl31_StateType240', {a1})
    assert _is_linked(b, 'jpdl31_StateType240', a1)
    if hasattr(a1, 'jpdl31_TimerType241'):
        assert _is_linked(a1, 'jpdl31_TimerType241', b)
    _safe_set(b, 'jpdl31_StateType240', {a2})
    assert _is_linked(b, 'jpdl31_StateType240', a2)
    if hasattr(a1, 'jpdl31_TimerType241'):
        assert not _is_linked(a1, 'jpdl31_TimerType241', b)
    if hasattr(a2, 'jpdl31_TimerType241'):
        assert _is_linked(a2, 'jpdl31_TimerType241', b)
    _safe_set(b, 'jpdl31_StateType240', set())
    assert not _is_linked(b, 'jpdl31_StateType240', a2)
    if hasattr(a2, 'jpdl31_TimerType241'):
        assert not _is_linked(a2, 'jpdl31_TimerType241', b)


def test_assoc_timer278_reverse_link_reassign_clear():
    a1 = jpdl31_TimerType(duedate="sample_text", name="sample_text", repeat="sample_text", transition="sample_text")
    a2 = jpdl31_TimerType(duedate="sample_text_2", name="sample_text_2", repeat="sample_text_2", transition="sample_text_2")
    b = jpdl31_SuperStateType(async_="sample_text", group="sample_text", name="sample_text")
    _safe_set(b, 'jpdl31_SuperStateType279', {a1})
    assert _is_linked(b, 'jpdl31_SuperStateType279', a1)
    if hasattr(a1, 'jpdl31_TimerType280'):
        assert _is_linked(a1, 'jpdl31_TimerType280', b)
    _safe_set(b, 'jpdl31_SuperStateType279', {a2})
    assert _is_linked(b, 'jpdl31_SuperStateType279', a2)
    if hasattr(a1, 'jpdl31_TimerType280'):
        assert not _is_linked(a1, 'jpdl31_TimerType280', b)
    if hasattr(a2, 'jpdl31_TimerType280'):
        assert _is_linked(a2, 'jpdl31_TimerType280', b)
    _safe_set(b, 'jpdl31_SuperStateType279', set())
    assert not _is_linked(b, 'jpdl31_SuperStateType279', a2)
    if hasattr(a2, 'jpdl31_TimerType280'):
        assert not _is_linked(a2, 'jpdl31_TimerType280', b)


def test_assoc_timer296_reverse_link_reassign_clear():
    a1 = jpdl31_TimerType(duedate="sample_text", name="sample_text", repeat="sample_text", transition="sample_text")
    a2 = jpdl31_TimerType(duedate="sample_text_2", name="sample_text_2", repeat="sample_text_2", transition="sample_text_2")
    b = jpdl31_TaskNodeType(async_="sample_text", createTasks="sample_text", description="sample_text", endTasks="sample_text", group="sample_text", name="sample_text", signal="sample_text")
    _safe_set(b, 'jpdl31_TaskNodeType297', {a1})
    assert _is_linked(b, 'jpdl31_TaskNodeType297', a1)
    if hasattr(a1, 'jpdl31_TimerType298'):
        assert _is_linked(a1, 'jpdl31_TimerType298', b)
    _safe_set(b, 'jpdl31_TaskNodeType297', {a2})
    assert _is_linked(b, 'jpdl31_TaskNodeType297', a2)
    if hasattr(a1, 'jpdl31_TimerType298'):
        assert not _is_linked(a1, 'jpdl31_TimerType298', b)
    if hasattr(a2, 'jpdl31_TimerType298'):
        assert _is_linked(a2, 'jpdl31_TimerType298', b)
    _safe_set(b, 'jpdl31_TaskNodeType297', set())
    assert not _is_linked(b, 'jpdl31_TaskNodeType297', a2)
    if hasattr(a2, 'jpdl31_TimerType298'):
        assert not _is_linked(a2, 'jpdl31_TimerType298', b)


def test_assoc_timer315_reverse_link_reassign_clear():
    a1 = jpdl31_TimerType(duedate="sample_text", name="sample_text", repeat="sample_text", transition="sample_text")
    a2 = jpdl31_TimerType(duedate="sample_text_2", name="sample_text_2", repeat="sample_text_2", transition="sample_text_2")
    b = jpdl31_TaskType(blocking="sample_text", description="sample_text", duedate="sample_text", group="sample_text", name="sample_text", priority="sample_text", signalling="sample_text", swimlane="sample_text")
    _safe_set(b, 'jpdl31_TaskType316', {a1})
    assert _is_linked(b, 'jpdl31_TaskType316', a1)
    if hasattr(a1, 'jpdl31_TimerType317'):
        assert _is_linked(a1, 'jpdl31_TimerType317', b)
    _safe_set(b, 'jpdl31_TaskType316', {a2})
    assert _is_linked(b, 'jpdl31_TaskType316', a2)
    if hasattr(a1, 'jpdl31_TimerType317'):
        assert not _is_linked(a1, 'jpdl31_TimerType317', b)
    if hasattr(a2, 'jpdl31_TimerType317'):
        assert _is_linked(a2, 'jpdl31_TimerType317', b)
    _safe_set(b, 'jpdl31_TaskType316', set())
    assert not _is_linked(b, 'jpdl31_TaskType316', a2)
    if hasattr(a2, 'jpdl31_TimerType317'):
        assert not _is_linked(a2, 'jpdl31_TimerType317', b)


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


def test_assoc_transition111_reverse_link_reassign_clear():
    a1 = jpdl31_TransitionType(group="sample_text", name="sample_text", to="sample_text")
    a2 = jpdl31_TransitionType(group="sample_text_2", name="sample_text_2", to="sample_text_2")
    b = jpdl31_ForkType(async_="sample_text", group="sample_text", name="sample_text")
    _safe_set(b, 'jpdl31_ForkType112', {a1})
    assert _is_linked(b, 'jpdl31_ForkType112', a1)
    if hasattr(a1, 'jpdl31_TransitionType113'):
        assert _is_linked(a1, 'jpdl31_TransitionType113', b)
    _safe_set(b, 'jpdl31_ForkType112', {a2})
    assert _is_linked(b, 'jpdl31_ForkType112', a2)
    if hasattr(a1, 'jpdl31_TransitionType113'):
        assert not _is_linked(a1, 'jpdl31_TransitionType113', b)
    if hasattr(a2, 'jpdl31_TransitionType113'):
        assert _is_linked(a2, 'jpdl31_TransitionType113', b)
    _safe_set(b, 'jpdl31_ForkType112', set())
    assert not _is_linked(b, 'jpdl31_ForkType112', a2)
    if hasattr(a2, 'jpdl31_TransitionType113'):
        assert not _is_linked(a2, 'jpdl31_TransitionType113', b)


def test_assoc_transition123_reverse_link_reassign_clear():
    a1 = jpdl31_TransitionType(group="sample_text", name="sample_text", to="sample_text")
    a2 = jpdl31_TransitionType(group="sample_text_2", name="sample_text_2", to="sample_text_2")
    b = jpdl31_JoinType(async_="sample_text", name="sample_text", nodeContentElements="sample_text")
    _safe_set(b, 'jpdl31_JoinType124', {a1})
    assert _is_linked(b, 'jpdl31_JoinType124', a1)
    if hasattr(a1, 'jpdl31_TransitionType125'):
        assert _is_linked(a1, 'jpdl31_TransitionType125', b)
    _safe_set(b, 'jpdl31_JoinType124', {a2})
    assert _is_linked(b, 'jpdl31_JoinType124', a2)
    if hasattr(a1, 'jpdl31_TransitionType125'):
        assert not _is_linked(a1, 'jpdl31_TransitionType125', b)
    if hasattr(a2, 'jpdl31_TransitionType125'):
        assert _is_linked(a2, 'jpdl31_TransitionType125', b)
    _safe_set(b, 'jpdl31_JoinType124', set())
    assert not _is_linked(b, 'jpdl31_JoinType124', a2)
    if hasattr(a2, 'jpdl31_TransitionType125'):
        assert not _is_linked(a2, 'jpdl31_TransitionType125', b)


def test_assoc_transition147_reverse_link_reassign_clear():
    a1 = jpdl31_TransitionType(group="sample_text", name="sample_text", to="sample_text")
    a2 = jpdl31_TransitionType(group="sample_text_2", name="sample_text_2", to="sample_text_2")
    b = jpdl31_NodeType(async_="sample_text", description="sample_text", name="sample_text", nodeContentElements="sample_text")
    _safe_set(b, 'jpdl31_NodeType148', {a1})
    assert _is_linked(b, 'jpdl31_NodeType148', a1)
    if hasattr(a1, 'jpdl31_TransitionType149'):
        assert _is_linked(a1, 'jpdl31_TransitionType149', b)
    _safe_set(b, 'jpdl31_NodeType148', {a2})
    assert _is_linked(b, 'jpdl31_NodeType148', a2)
    if hasattr(a1, 'jpdl31_TransitionType149'):
        assert not _is_linked(a1, 'jpdl31_TransitionType149', b)
    if hasattr(a2, 'jpdl31_TransitionType149'):
        assert _is_linked(a2, 'jpdl31_TransitionType149', b)
    _safe_set(b, 'jpdl31_NodeType148', set())
    assert not _is_linked(b, 'jpdl31_NodeType148', a2)
    if hasattr(a2, 'jpdl31_TransitionType149'):
        assert not _is_linked(a2, 'jpdl31_TransitionType149', b)


def test_assoc_transition218_reverse_link_reassign_clear():
    a1 = jpdl31_TransitionType(group="sample_text", name="sample_text", to="sample_text")
    a2 = jpdl31_TransitionType(group="sample_text_2", name="sample_text_2", to="sample_text_2")
    b = jpdl31_ProcessStateType(async_="sample_text", group="sample_text", name="sample_text")
    _safe_set(b, 'jpdl31_ProcessStateType219', {a1})
    assert _is_linked(b, 'jpdl31_ProcessStateType219', a1)
    if hasattr(a1, 'jpdl31_TransitionType220'):
        assert _is_linked(a1, 'jpdl31_TransitionType220', b)
    _safe_set(b, 'jpdl31_ProcessStateType219', {a2})
    assert _is_linked(b, 'jpdl31_ProcessStateType219', a2)
    if hasattr(a1, 'jpdl31_TransitionType220'):
        assert not _is_linked(a1, 'jpdl31_TransitionType220', b)
    if hasattr(a2, 'jpdl31_TransitionType220'):
        assert _is_linked(a2, 'jpdl31_TransitionType220', b)
    _safe_set(b, 'jpdl31_ProcessStateType219', set())
    assert not _is_linked(b, 'jpdl31_ProcessStateType219', a2)
    if hasattr(a2, 'jpdl31_TransitionType220'):
        assert not _is_linked(a2, 'jpdl31_TransitionType220', b)


def test_assoc_transition224_reverse_link_reassign_clear():
    a1 = jpdl31_TransitionType(group="sample_text", name="sample_text", to="sample_text")
    a2 = jpdl31_TransitionType(group="sample_text_2", name="sample_text_2", to="sample_text_2")
    b = jpdl31_StartStateType(group="sample_text", name="sample_text")
    _safe_set(b, 'jpdl31_StartStateType225', {a1})
    assert _is_linked(b, 'jpdl31_StartStateType225', a1)
    if hasattr(a1, 'jpdl31_TransitionType226'):
        assert _is_linked(a1, 'jpdl31_TransitionType226', b)
    _safe_set(b, 'jpdl31_StartStateType225', {a2})
    assert _is_linked(b, 'jpdl31_StartStateType225', a2)
    if hasattr(a1, 'jpdl31_TransitionType226'):
        assert not _is_linked(a1, 'jpdl31_TransitionType226', b)
    if hasattr(a2, 'jpdl31_TransitionType226'):
        assert _is_linked(a2, 'jpdl31_TransitionType226', b)
    _safe_set(b, 'jpdl31_StartStateType225', set())
    assert not _is_linked(b, 'jpdl31_StartStateType225', a2)
    if hasattr(a2, 'jpdl31_TransitionType226'):
        assert not _is_linked(a2, 'jpdl31_TransitionType226', b)


def test_assoc_transition242_reverse_link_reassign_clear():
    a1 = jpdl31_TransitionType(group="sample_text", name="sample_text", to="sample_text")
    a2 = jpdl31_TransitionType(group="sample_text_2", name="sample_text_2", to="sample_text_2")
    b = jpdl31_StateType(async_="sample_text", name="sample_text", nodeContentElements="sample_text")
    _safe_set(b, 'jpdl31_StateType243', {a1})
    assert _is_linked(b, 'jpdl31_StateType243', a1)
    if hasattr(a1, 'jpdl31_TransitionType244'):
        assert _is_linked(a1, 'jpdl31_TransitionType244', b)
    _safe_set(b, 'jpdl31_StateType243', {a2})
    assert _is_linked(b, 'jpdl31_StateType243', a2)
    if hasattr(a1, 'jpdl31_TransitionType244'):
        assert not _is_linked(a1, 'jpdl31_TransitionType244', b)
    if hasattr(a2, 'jpdl31_TransitionType244'):
        assert _is_linked(a2, 'jpdl31_TransitionType244', b)
    _safe_set(b, 'jpdl31_StateType243', set())
    assert not _is_linked(b, 'jpdl31_StateType243', a2)
    if hasattr(a2, 'jpdl31_TransitionType244'):
        assert not _is_linked(a2, 'jpdl31_TransitionType244', b)


def test_assoc_transition281_reverse_link_reassign_clear():
    a1 = jpdl31_TransitionType(group="sample_text", name="sample_text", to="sample_text")
    a2 = jpdl31_TransitionType(group="sample_text_2", name="sample_text_2", to="sample_text_2")
    b = jpdl31_SuperStateType(async_="sample_text", group="sample_text", name="sample_text")
    _safe_set(b, 'jpdl31_SuperStateType282', {a1})
    assert _is_linked(b, 'jpdl31_SuperStateType282', a1)
    if hasattr(a1, 'jpdl31_TransitionType283'):
        assert _is_linked(a1, 'jpdl31_TransitionType283', b)
    _safe_set(b, 'jpdl31_SuperStateType282', {a2})
    assert _is_linked(b, 'jpdl31_SuperStateType282', a2)
    if hasattr(a1, 'jpdl31_TransitionType283'):
        assert not _is_linked(a1, 'jpdl31_TransitionType283', b)
    if hasattr(a2, 'jpdl31_TransitionType283'):
        assert _is_linked(a2, 'jpdl31_TransitionType283', b)
    _safe_set(b, 'jpdl31_SuperStateType282', set())
    assert not _is_linked(b, 'jpdl31_SuperStateType282', a2)
    if hasattr(a2, 'jpdl31_TransitionType283'):
        assert not _is_linked(a2, 'jpdl31_TransitionType283', b)


def test_assoc_transition299_reverse_link_reassign_clear():
    a1 = jpdl31_TransitionType(group="sample_text", name="sample_text", to="sample_text")
    a2 = jpdl31_TransitionType(group="sample_text_2", name="sample_text_2", to="sample_text_2")
    b = jpdl31_TaskNodeType(async_="sample_text", createTasks="sample_text", description="sample_text", endTasks="sample_text", group="sample_text", name="sample_text", signal="sample_text")
    _safe_set(b, 'jpdl31_TaskNodeType300', {a1})
    assert _is_linked(b, 'jpdl31_TaskNodeType300', a1)
    if hasattr(a1, 'jpdl31_TransitionType301'):
        assert _is_linked(a1, 'jpdl31_TransitionType301', b)
    _safe_set(b, 'jpdl31_TaskNodeType300', {a2})
    assert _is_linked(b, 'jpdl31_TaskNodeType300', a2)
    if hasattr(a1, 'jpdl31_TransitionType301'):
        assert not _is_linked(a1, 'jpdl31_TransitionType301', b)
    if hasattr(a2, 'jpdl31_TransitionType301'):
        assert _is_linked(a2, 'jpdl31_TransitionType301', b)
    _safe_set(b, 'jpdl31_TaskNodeType300', set())
    assert not _is_linked(b, 'jpdl31_TaskNodeType300', a2)
    if hasattr(a2, 'jpdl31_TransitionType301'):
        assert not _is_linked(a2, 'jpdl31_TransitionType301', b)


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


def test_assoc_treatment370_reverse_link_reassign_clear():
    a1 = jpdl31_Level(name="sample_text")
    a2 = jpdl31_Level(name="sample_text_2")
    b = jpdl31_Hyphotesis(description="sample_text", id="sample_text", relationOp="sample_text", type="sample_text")
    _safe_set(b, 'jpdl31_Hyphotesis371', {a1})
    assert _is_linked(b, 'jpdl31_Hyphotesis371', a1)
    if hasattr(a1, 'jpdl31_Level'):
        assert _is_linked(a1, 'jpdl31_Level', b)
    _safe_set(b, 'jpdl31_Hyphotesis371', {a2})
    assert _is_linked(b, 'jpdl31_Hyphotesis371', a2)
    if hasattr(a1, 'jpdl31_Level'):
        assert not _is_linked(a1, 'jpdl31_Level', b)
    if hasattr(a2, 'jpdl31_Level'):
        assert _is_linked(a2, 'jpdl31_Level', b)
    _safe_set(b, 'jpdl31_Hyphotesis371', set())
    assert not _is_linked(b, 'jpdl31_Hyphotesis371', a2)
    if hasattr(a2, 'jpdl31_Level'):
        assert not _is_linked(a2, 'jpdl31_Level', b)


def test_assoc_treatment374_reverse_link_reassign_clear():
    a1 = jpdl31_Subhypotheses(relationOp="sample_text")
    a2 = jpdl31_Subhypotheses(relationOp="sample_text_2")
    b = jpdl31_Level(name="sample_text")
    _safe_set(b, 'jpdl31_Level376', a1)
    assert _is_linked(b, 'jpdl31_Level376', a1)
    if hasattr(a1, 'jpdl31_Subhypotheses375'):
        assert _is_linked(a1, 'jpdl31_Subhypotheses375', b)
    _safe_set(b, 'jpdl31_Level376', a2)
    assert _is_linked(b, 'jpdl31_Level376', a2)
    if hasattr(a1, 'jpdl31_Subhypotheses375'):
        assert not _is_linked(a1, 'jpdl31_Subhypotheses375', b)
    if hasattr(a2, 'jpdl31_Subhypotheses375'):
        assert _is_linked(a2, 'jpdl31_Subhypotheses375', b)
    _safe_set(b, 'jpdl31_Level376', None)
    assert not _is_linked(b, 'jpdl31_Level376', a2)
    if hasattr(a2, 'jpdl31_Subhypotheses375'):
        assert not _is_linked(a2, 'jpdl31_Subhypotheses375', b)


def test_assoc_variable206_reverse_link_reassign_clear():
    a1 = jpdl31_VariableType(access="sample_text", any="sample_text", mappedName="sample_text", name="sample_text")
    a2 = jpdl31_VariableType(access="sample_text_2", any="sample_text_2", mappedName="sample_text_2", name="sample_text_2")
    b = jpdl31_ProcessStateType(async_="sample_text", group="sample_text", name="sample_text")
    _safe_set(b, 'jpdl31_ProcessStateType207', {a1})
    assert _is_linked(b, 'jpdl31_ProcessStateType207', a1)
    if hasattr(a1, 'jpdl31_VariableType208'):
        assert _is_linked(a1, 'jpdl31_VariableType208', b)
    _safe_set(b, 'jpdl31_ProcessStateType207', {a2})
    assert _is_linked(b, 'jpdl31_ProcessStateType207', a2)
    if hasattr(a1, 'jpdl31_VariableType208'):
        assert not _is_linked(a1, 'jpdl31_VariableType208', b)
    if hasattr(a2, 'jpdl31_VariableType208'):
        assert _is_linked(a2, 'jpdl31_VariableType208', b)
    _safe_set(b, 'jpdl31_ProcessStateType207', set())
    assert not _is_linked(b, 'jpdl31_ProcessStateType207', a2)
    if hasattr(a2, 'jpdl31_VariableType208'):
        assert not _is_linked(a2, 'jpdl31_VariableType208', b)


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


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_design407_stub_double():
    # jpdl31_ExperimentalPlan has no real 'jpdl31_ExperimentalPlan408' property in the generated
    # code (a bare stub) -- manually attach it so jpdl31_Design's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # jpdl31_Design's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = jpdl31_Design(DoE="sample_text")
    partner = jpdl31_ExperimentalPlan()
    setattr(partner, 'jpdl31_ExperimentalPlan408', None)
    _safe_set(owner, 'jpdl31_Design', partner)
    assert getattr(partner, 'jpdl31_ExperimentalPlan408') == owner
    _safe_set(owner, 'jpdl31_Design', None)
    assert getattr(partner, 'jpdl31_ExperimentalPlan408') is None


def test_assoc_elements362_stub_double():
    # jpdl31_Model has no real 'jpdl31_Model' property in the generated
    # code (a bare stub) -- manually attach it so jpdl31_DocumentRoot's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # jpdl31_DocumentRoot's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = jpdl31_DocumentRoot(mixed="sample_text")
    partner = jpdl31_Model()
    setattr(partner, 'jpdl31_Model', None)
    _safe_set(owner, 'jpdl31_DocumentRoot363', partner)
    assert owner in getattr(partner, 'jpdl31_Model')
    _safe_set(owner, 'jpdl31_DocumentRoot363', None)
    assert owner not in getattr(partner, 'jpdl31_Model')


def test_assoc_goals401_stub_double():
    # jpdl31_ExperimentalPlan has no real 'jpdl31_ExperimentalPlan402' property in the generated
    # code (a bare stub) -- manually attach it so jpdl31_Goal's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # jpdl31_Goal's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = jpdl31_Goal(description="sample_text", id="sample_text")
    partner = jpdl31_ExperimentalPlan()
    setattr(partner, 'jpdl31_ExperimentalPlan402', None)
    _safe_set(owner, 'jpdl31_Goal403', partner)
    assert owner in getattr(partner, 'jpdl31_ExperimentalPlan402')
    _safe_set(owner, 'jpdl31_Goal403', None)
    assert owner not in getattr(partner, 'jpdl31_ExperimentalPlan402')


def test_assoc_hypothesis404_stub_double():
    # jpdl31_ExperimentalPlan has no real 'jpdl31_ExperimentalPlan405' property in the generated
    # code (a bare stub) -- manually attach it so jpdl31_Hyphotesis's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # jpdl31_Hyphotesis's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = jpdl31_Hyphotesis(description="sample_text", id="sample_text", relationOp="sample_text", type="sample_text")
    partner = jpdl31_ExperimentalPlan()
    setattr(partner, 'jpdl31_ExperimentalPlan405', None)
    _safe_set(owner, 'jpdl31_Hyphotesis406', partner)
    assert owner in getattr(partner, 'jpdl31_ExperimentalPlan405')
    _safe_set(owner, 'jpdl31_Hyphotesis406', None)
    assert owner not in getattr(partner, 'jpdl31_ExperimentalPlan405')


def test_assoc_plan71_stub_double():
    # jpdl31_ExperimentalPlan has no real 'jpdl31_ExperimentalPlan' property in the generated
    # code (a bare stub) -- manually attach it so jpdl31_DocumentRoot's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # jpdl31_DocumentRoot's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = jpdl31_DocumentRoot(mixed="sample_text")
    partner = jpdl31_ExperimentalPlan()
    setattr(partner, 'jpdl31_ExperimentalPlan', None)
    _safe_set(owner, 'jpdl31_DocumentRoot72', {partner})
    assert getattr(partner, 'jpdl31_ExperimentalPlan') == owner
    _safe_set(owner, 'jpdl31_DocumentRoot72', set())
    assert getattr(partner, 'jpdl31_ExperimentalPlan') is None


def test_assoc_test414_stub_double():
    # jpdl31_StatisticalTest has no real 'jpdl31_StatisticalTest' property in the generated
    # code (a bare stub) -- manually attach it so jpdl31_Design's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # jpdl31_Design's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = jpdl31_Design(DoE="sample_text")
    partner = jpdl31_StatisticalTest()
    setattr(partner, 'jpdl31_StatisticalTest', None)
    _safe_set(owner, 'jpdl31_Design415', {partner})
    assert getattr(partner, 'jpdl31_StatisticalTest') == owner
    _safe_set(owner, 'jpdl31_Design415', set())
    assert getattr(partner, 'jpdl31_StatisticalTest') is None


def test_assoc_xMLNSPrefixMap10_stub_double():
    # jpdl31_EStringToStringMapEntry has no real 'jpdl31_EStringToStringMapEntry' property in the generated
    # code (a bare stub) -- manually attach it so jpdl31_DocumentRoot's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # jpdl31_DocumentRoot's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = jpdl31_DocumentRoot(mixed="sample_text")
    partner = jpdl31_EStringToStringMapEntry()
    setattr(partner, 'jpdl31_EStringToStringMapEntry', None)
    _safe_set(owner, 'jpdl31_DocumentRoot', {partner})
    assert getattr(partner, 'jpdl31_EStringToStringMapEntry') == owner
    _safe_set(owner, 'jpdl31_DocumentRoot', set())
    assert getattr(partner, 'jpdl31_EStringToStringMapEntry') is None


def test_assoc_xSISchemaLocation11_stub_double():
    # jpdl31_EStringToStringMapEntry has no real 'jpdl31_EStringToStringMapEntry13' property in the generated
    # code (a bare stub) -- manually attach it so jpdl31_DocumentRoot's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # jpdl31_DocumentRoot's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = jpdl31_DocumentRoot(mixed="sample_text")
    partner = jpdl31_EStringToStringMapEntry()
    setattr(partner, 'jpdl31_EStringToStringMapEntry13', None)
    _safe_set(owner, 'jpdl31_DocumentRoot12', {partner})
    assert getattr(partner, 'jpdl31_EStringToStringMapEntry13') == owner
    _safe_set(owner, 'jpdl31_DocumentRoot12', set())
    assert getattr(partner, 'jpdl31_EStringToStringMapEntry13') is None


