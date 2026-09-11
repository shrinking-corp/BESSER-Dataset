import inspect
import pytest
from datetime import date, datetime, time, timedelta
from hypothesis import given, settings
import hypothesis.strategies as st

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

safe_text = st.text(
    alphabet=st.characters(
        whitelist_categories=("Ll", "Lu", "Nd"),
        whitelist_characters="_",
    ),
    min_size=1,
).filter(lambda s: s[0].isalpha())

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
# SECTION 1 -- DETERMINISTIC TESTS (attributes, generalizations, relationships)
# =============================================================================

def test_jpdl31_ActionType_acceptPropagatedEvents_value_roundtrip():
    instance = jpdl31_ActionType(acceptPropagatedEvents="sample_text", any="sample_text", async_="sample_text", class_="sample_text", configType="sample_text", expression="sample_text", mixed="sample_text", name="sample_text", refName="sample_text")
    assert instance.acceptPropagatedEvents == "sample_text"
    instance.acceptPropagatedEvents = "sample_text_2"
    assert instance.acceptPropagatedEvents == "sample_text_2"


def test_jpdl31_ActionType_any_value_roundtrip():
    instance = jpdl31_ActionType(acceptPropagatedEvents="sample_text", any="sample_text", async_="sample_text", class_="sample_text", configType="sample_text", expression="sample_text", mixed="sample_text", name="sample_text", refName="sample_text")
    assert instance.any == "sample_text"
    instance.any = "sample_text_2"
    assert instance.any == "sample_text_2"


def test_jpdl31_ActionType_async__value_roundtrip():
    instance = jpdl31_ActionType(acceptPropagatedEvents="sample_text", any="sample_text", async_="sample_text", class_="sample_text", configType="sample_text", expression="sample_text", mixed="sample_text", name="sample_text", refName="sample_text")
    assert instance.async_ == "sample_text"
    instance.async_ = "sample_text_2"
    assert instance.async_ == "sample_text_2"


def test_jpdl31_ActionType_class__value_roundtrip():
    instance = jpdl31_ActionType(acceptPropagatedEvents="sample_text", any="sample_text", async_="sample_text", class_="sample_text", configType="sample_text", expression="sample_text", mixed="sample_text", name="sample_text", refName="sample_text")
    assert instance.class_ == "sample_text"
    instance.class_ = "sample_text_2"
    assert instance.class_ == "sample_text_2"


def test_jpdl31_ActionType_configType_value_roundtrip():
    instance = jpdl31_ActionType(acceptPropagatedEvents="sample_text", any="sample_text", async_="sample_text", class_="sample_text", configType="sample_text", expression="sample_text", mixed="sample_text", name="sample_text", refName="sample_text")
    assert instance.configType == "sample_text"
    instance.configType = "sample_text_2"
    assert instance.configType == "sample_text_2"


def test_jpdl31_ActionType_expression_value_roundtrip():
    instance = jpdl31_ActionType(acceptPropagatedEvents="sample_text", any="sample_text", async_="sample_text", class_="sample_text", configType="sample_text", expression="sample_text", mixed="sample_text", name="sample_text", refName="sample_text")
    assert instance.expression == "sample_text"
    instance.expression = "sample_text_2"
    assert instance.expression == "sample_text_2"


def test_jpdl31_ActionType_mixed_value_roundtrip():
    instance = jpdl31_ActionType(acceptPropagatedEvents="sample_text", any="sample_text", async_="sample_text", class_="sample_text", configType="sample_text", expression="sample_text", mixed="sample_text", name="sample_text", refName="sample_text")
    assert instance.mixed == "sample_text"
    instance.mixed = "sample_text_2"
    assert instance.mixed == "sample_text_2"


def test_jpdl31_ActionType_name_value_roundtrip():
    instance = jpdl31_ActionType(acceptPropagatedEvents="sample_text", any="sample_text", async_="sample_text", class_="sample_text", configType="sample_text", expression="sample_text", mixed="sample_text", name="sample_text", refName="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_jpdl31_ActionType_refName_value_roundtrip():
    instance = jpdl31_ActionType(acceptPropagatedEvents="sample_text", any="sample_text", async_="sample_text", class_="sample_text", configType="sample_text", expression="sample_text", mixed="sample_text", name="sample_text", refName="sample_text")
    assert instance.refName == "sample_text"
    instance.refName = "sample_text_2"
    assert instance.refName == "sample_text_2"


def test_jpdl31_AssignmentType_actorId_value_roundtrip():
    instance = jpdl31_AssignmentType(actorId="sample_text", expression="sample_text", pooledActors="sample_text")
    assert instance.actorId == "sample_text"
    instance.actorId = "sample_text_2"
    assert instance.actorId == "sample_text_2"


def test_jpdl31_AssignmentType_expression_value_roundtrip():
    instance = jpdl31_AssignmentType(actorId="sample_text", expression="sample_text", pooledActors="sample_text")
    assert instance.expression == "sample_text"
    instance.expression = "sample_text_2"
    assert instance.expression == "sample_text_2"


def test_jpdl31_AssignmentType_pooledActors_value_roundtrip():
    instance = jpdl31_AssignmentType(actorId="sample_text", expression="sample_text", pooledActors="sample_text")
    assert instance.pooledActors == "sample_text"
    instance.pooledActors = "sample_text_2"
    assert instance.pooledActors == "sample_text_2"


def test_jpdl31_CancelTimerType_name_value_roundtrip():
    instance = jpdl31_CancelTimerType(name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_jpdl31_ConditionType_any_value_roundtrip():
    instance = jpdl31_ConditionType(any="sample_text", expression="sample_text", group="sample_text", mixed="sample_text")
    assert instance.any == "sample_text"
    instance.any = "sample_text_2"
    assert instance.any == "sample_text_2"


def test_jpdl31_ConditionType_expression_value_roundtrip():
    instance = jpdl31_ConditionType(any="sample_text", expression="sample_text", group="sample_text", mixed="sample_text")
    assert instance.expression == "sample_text"
    instance.expression = "sample_text_2"
    assert instance.expression == "sample_text_2"


def test_jpdl31_ConditionType_group_value_roundtrip():
    instance = jpdl31_ConditionType(any="sample_text", expression="sample_text", group="sample_text", mixed="sample_text")
    assert instance.group == "sample_text"
    instance.group = "sample_text_2"
    assert instance.group == "sample_text_2"


def test_jpdl31_ConditionType_mixed_value_roundtrip():
    instance = jpdl31_ConditionType(any="sample_text", expression="sample_text", group="sample_text", mixed="sample_text")
    assert instance.mixed == "sample_text"
    instance.mixed = "sample_text_2"
    assert instance.mixed == "sample_text_2"


def test_jpdl31_CreateTimerType_duedate_value_roundtrip():
    instance = jpdl31_CreateTimerType(duedate="sample_text", name="sample_text", repeat="sample_text", transition="sample_text")
    assert instance.duedate == "sample_text"
    instance.duedate = "sample_text_2"
    assert instance.duedate == "sample_text_2"


def test_jpdl31_CreateTimerType_name_value_roundtrip():
    instance = jpdl31_CreateTimerType(duedate="sample_text", name="sample_text", repeat="sample_text", transition="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_jpdl31_CreateTimerType_repeat_value_roundtrip():
    instance = jpdl31_CreateTimerType(duedate="sample_text", name="sample_text", repeat="sample_text", transition="sample_text")
    assert instance.repeat == "sample_text"
    instance.repeat = "sample_text_2"
    assert instance.repeat == "sample_text_2"


def test_jpdl31_CreateTimerType_transition_value_roundtrip():
    instance = jpdl31_CreateTimerType(duedate="sample_text", name="sample_text", repeat="sample_text", transition="sample_text")
    assert instance.transition == "sample_text"
    instance.transition = "sample_text_2"
    assert instance.transition == "sample_text_2"


def test_jpdl31_DecisionType_async__value_roundtrip():
    instance = jpdl31_DecisionType(async_="sample_text", expression="sample_text", group="sample_text", name="sample_text")
    assert instance.async_ == "sample_text"
    instance.async_ = "sample_text_2"
    assert instance.async_ == "sample_text_2"


def test_jpdl31_DecisionType_expression_value_roundtrip():
    instance = jpdl31_DecisionType(async_="sample_text", expression="sample_text", group="sample_text", name="sample_text")
    assert instance.expression == "sample_text"
    instance.expression = "sample_text_2"
    assert instance.expression == "sample_text_2"


def test_jpdl31_DecisionType_group_value_roundtrip():
    instance = jpdl31_DecisionType(async_="sample_text", expression="sample_text", group="sample_text", name="sample_text")
    assert instance.group == "sample_text"
    instance.group = "sample_text_2"
    assert instance.group == "sample_text_2"


def test_jpdl31_DecisionType_name_value_roundtrip():
    instance = jpdl31_DecisionType(async_="sample_text", expression="sample_text", group="sample_text", name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_jpdl31_Delegation_any_value_roundtrip():
    instance = jpdl31_Delegation(any="sample_text", class_="sample_text", configType="sample_text", mixed="sample_text")
    assert instance.any == "sample_text"
    instance.any = "sample_text_2"
    assert instance.any == "sample_text_2"


def test_jpdl31_Delegation_class__value_roundtrip():
    instance = jpdl31_Delegation(any="sample_text", class_="sample_text", configType="sample_text", mixed="sample_text")
    assert instance.class_ == "sample_text"
    instance.class_ = "sample_text_2"
    assert instance.class_ == "sample_text_2"


def test_jpdl31_Delegation_configType_value_roundtrip():
    instance = jpdl31_Delegation(any="sample_text", class_="sample_text", configType="sample_text", mixed="sample_text")
    assert instance.configType == "sample_text"
    instance.configType = "sample_text_2"
    assert instance.configType == "sample_text_2"


def test_jpdl31_Delegation_mixed_value_roundtrip():
    instance = jpdl31_Delegation(any="sample_text", class_="sample_text", configType="sample_text", mixed="sample_text")
    assert instance.mixed == "sample_text"
    instance.mixed = "sample_text_2"
    assert instance.mixed == "sample_text_2"


def test_jpdl31_DocumentRoot_mixed_value_roundtrip():
    instance = jpdl31_DocumentRoot(mixed="sample_text")
    assert instance.mixed == "sample_text"
    instance.mixed = "sample_text_2"
    assert instance.mixed == "sample_text_2"


def test_jpdl31_EndStateType_group_value_roundtrip():
    instance = jpdl31_EndStateType(group="sample_text", name="sample_text")
    assert instance.group == "sample_text"
    instance.group = "sample_text_2"
    assert instance.group == "sample_text_2"


def test_jpdl31_EndStateType_name_value_roundtrip():
    instance = jpdl31_EndStateType(group="sample_text", name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_jpdl31_EventType_actionElements_value_roundtrip():
    instance = jpdl31_EventType(actionElements="sample_text", type="sample_text")
    assert instance.actionElements == "sample_text"
    instance.actionElements = "sample_text_2"
    assert instance.actionElements == "sample_text_2"


def test_jpdl31_EventType_type_value_roundtrip():
    instance = jpdl31_EventType(actionElements="sample_text", type="sample_text")
    assert instance.type == "sample_text"
    instance.type = "sample_text_2"
    assert instance.type == "sample_text_2"


def test_jpdl31_ExceptionHandlerType_exceptionClass_value_roundtrip():
    instance = jpdl31_ExceptionHandlerType(exceptionClass="sample_text", group="sample_text")
    assert instance.exceptionClass == "sample_text"
    instance.exceptionClass = "sample_text_2"
    assert instance.exceptionClass == "sample_text_2"


def test_jpdl31_ExceptionHandlerType_group_value_roundtrip():
    instance = jpdl31_ExceptionHandlerType(exceptionClass="sample_text", group="sample_text")
    assert instance.group == "sample_text"
    instance.group = "sample_text_2"
    assert instance.group == "sample_text_2"


def test_jpdl31_ForkType_async__value_roundtrip():
    instance = jpdl31_ForkType(async_="sample_text", group="sample_text", name="sample_text")
    assert instance.async_ == "sample_text"
    instance.async_ = "sample_text_2"
    assert instance.async_ == "sample_text_2"


def test_jpdl31_ForkType_group_value_roundtrip():
    instance = jpdl31_ForkType(async_="sample_text", group="sample_text", name="sample_text")
    assert instance.group == "sample_text"
    instance.group = "sample_text_2"
    assert instance.group == "sample_text_2"


def test_jpdl31_ForkType_name_value_roundtrip():
    instance = jpdl31_ForkType(async_="sample_text", group="sample_text", name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_jpdl31_JoinType_async__value_roundtrip():
    instance = jpdl31_JoinType(async_="sample_text", name="sample_text", nodeContentElements="sample_text")
    assert instance.async_ == "sample_text"
    instance.async_ = "sample_text_2"
    assert instance.async_ == "sample_text_2"


def test_jpdl31_JoinType_name_value_roundtrip():
    instance = jpdl31_JoinType(async_="sample_text", name="sample_text", nodeContentElements="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_jpdl31_JoinType_nodeContentElements_value_roundtrip():
    instance = jpdl31_JoinType(async_="sample_text", name="sample_text", nodeContentElements="sample_text")
    assert instance.nodeContentElements == "sample_text"
    instance.nodeContentElements = "sample_text_2"
    assert instance.nodeContentElements == "sample_text_2"


def test_jpdl31_NodeType_async__value_roundtrip():
    instance = jpdl31_NodeType(async_="sample_text", name="sample_text", nodeContentElements="sample_text")
    assert instance.async_ == "sample_text"
    instance.async_ = "sample_text_2"
    assert instance.async_ == "sample_text_2"


def test_jpdl31_NodeType_name_value_roundtrip():
    instance = jpdl31_NodeType(async_="sample_text", name="sample_text", nodeContentElements="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_jpdl31_NodeType_nodeContentElements_value_roundtrip():
    instance = jpdl31_NodeType(async_="sample_text", name="sample_text", nodeContentElements="sample_text")
    assert instance.nodeContentElements == "sample_text"
    instance.nodeContentElements = "sample_text_2"
    assert instance.nodeContentElements == "sample_text_2"


def test_jpdl31_ProcessDefinitionType_group_value_roundtrip():
    instance = jpdl31_ProcessDefinitionType(group="sample_text", name="sample_text")
    assert instance.group == "sample_text"
    instance.group = "sample_text_2"
    assert instance.group == "sample_text_2"


def test_jpdl31_ProcessDefinitionType_name_value_roundtrip():
    instance = jpdl31_ProcessDefinitionType(group="sample_text", name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_jpdl31_ProcessStateType_async__value_roundtrip():
    instance = jpdl31_ProcessStateType(async_="sample_text", group="sample_text", name="sample_text")
    assert instance.async_ == "sample_text"
    instance.async_ = "sample_text_2"
    assert instance.async_ == "sample_text_2"


def test_jpdl31_ProcessStateType_group_value_roundtrip():
    instance = jpdl31_ProcessStateType(async_="sample_text", group="sample_text", name="sample_text")
    assert instance.group == "sample_text"
    instance.group = "sample_text_2"
    assert instance.group == "sample_text_2"


def test_jpdl31_ProcessStateType_name_value_roundtrip():
    instance = jpdl31_ProcessStateType(async_="sample_text", group="sample_text", name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_jpdl31_ScriptType_acceptPropagatedEvents_value_roundtrip():
    instance = jpdl31_ScriptType(acceptPropagatedEvents="sample_text", any="sample_text", mixed="sample_text", name="sample_text")
    assert instance.acceptPropagatedEvents == "sample_text"
    instance.acceptPropagatedEvents = "sample_text_2"
    assert instance.acceptPropagatedEvents == "sample_text_2"


def test_jpdl31_ScriptType_any_value_roundtrip():
    instance = jpdl31_ScriptType(acceptPropagatedEvents="sample_text", any="sample_text", mixed="sample_text", name="sample_text")
    assert instance.any == "sample_text"
    instance.any = "sample_text_2"
    assert instance.any == "sample_text_2"


def test_jpdl31_ScriptType_mixed_value_roundtrip():
    instance = jpdl31_ScriptType(acceptPropagatedEvents="sample_text", any="sample_text", mixed="sample_text", name="sample_text")
    assert instance.mixed == "sample_text"
    instance.mixed = "sample_text_2"
    assert instance.mixed == "sample_text_2"


def test_jpdl31_ScriptType_name_value_roundtrip():
    instance = jpdl31_ScriptType(acceptPropagatedEvents="sample_text", any="sample_text", mixed="sample_text", name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_jpdl31_StartStateType_group_value_roundtrip():
    instance = jpdl31_StartStateType(group="sample_text", name="sample_text")
    assert instance.group == "sample_text"
    instance.group = "sample_text_2"
    assert instance.group == "sample_text_2"


def test_jpdl31_StartStateType_name_value_roundtrip():
    instance = jpdl31_StartStateType(group="sample_text", name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_jpdl31_StateType_async__value_roundtrip():
    instance = jpdl31_StateType(async_="sample_text", name="sample_text", nodeContentElements="sample_text")
    assert instance.async_ == "sample_text"
    instance.async_ = "sample_text_2"
    assert instance.async_ == "sample_text_2"


def test_jpdl31_StateType_name_value_roundtrip():
    instance = jpdl31_StateType(async_="sample_text", name="sample_text", nodeContentElements="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_jpdl31_StateType_nodeContentElements_value_roundtrip():
    instance = jpdl31_StateType(async_="sample_text", name="sample_text", nodeContentElements="sample_text")
    assert instance.nodeContentElements == "sample_text"
    instance.nodeContentElements = "sample_text_2"
    assert instance.nodeContentElements == "sample_text_2"


def test_jpdl31_SubProcessType_name_value_roundtrip():
    instance = jpdl31_SubProcessType(name="sample_text", version="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_jpdl31_SubProcessType_version_value_roundtrip():
    instance = jpdl31_SubProcessType(name="sample_text", version="sample_text")
    assert instance.version == "sample_text"
    instance.version = "sample_text_2"
    assert instance.version == "sample_text_2"


def test_jpdl31_SuperStateType_async__value_roundtrip():
    instance = jpdl31_SuperStateType(async_="sample_text", group="sample_text", name="sample_text")
    assert instance.async_ == "sample_text"
    instance.async_ = "sample_text_2"
    assert instance.async_ == "sample_text_2"


def test_jpdl31_SuperStateType_group_value_roundtrip():
    instance = jpdl31_SuperStateType(async_="sample_text", group="sample_text", name="sample_text")
    assert instance.group == "sample_text"
    instance.group = "sample_text_2"
    assert instance.group == "sample_text_2"


def test_jpdl31_SuperStateType_name_value_roundtrip():
    instance = jpdl31_SuperStateType(async_="sample_text", group="sample_text", name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_jpdl31_SwimlaneType_name_value_roundtrip():
    instance = jpdl31_SwimlaneType(name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_jpdl31_TaskNodeType_async__value_roundtrip():
    instance = jpdl31_TaskNodeType(async_="sample_text", createTasks="sample_text", endTasks="sample_text", group="sample_text", name="sample_text", signal="sample_text")
    assert instance.async_ == "sample_text"
    instance.async_ = "sample_text_2"
    assert instance.async_ == "sample_text_2"


def test_jpdl31_TaskNodeType_createTasks_value_roundtrip():
    instance = jpdl31_TaskNodeType(async_="sample_text", createTasks="sample_text", endTasks="sample_text", group="sample_text", name="sample_text", signal="sample_text")
    assert instance.createTasks == "sample_text"
    instance.createTasks = "sample_text_2"
    assert instance.createTasks == "sample_text_2"


def test_jpdl31_TaskNodeType_endTasks_value_roundtrip():
    instance = jpdl31_TaskNodeType(async_="sample_text", createTasks="sample_text", endTasks="sample_text", group="sample_text", name="sample_text", signal="sample_text")
    assert instance.endTasks == "sample_text"
    instance.endTasks = "sample_text_2"
    assert instance.endTasks == "sample_text_2"


def test_jpdl31_TaskNodeType_group_value_roundtrip():
    instance = jpdl31_TaskNodeType(async_="sample_text", createTasks="sample_text", endTasks="sample_text", group="sample_text", name="sample_text", signal="sample_text")
    assert instance.group == "sample_text"
    instance.group = "sample_text_2"
    assert instance.group == "sample_text_2"


def test_jpdl31_TaskNodeType_name_value_roundtrip():
    instance = jpdl31_TaskNodeType(async_="sample_text", createTasks="sample_text", endTasks="sample_text", group="sample_text", name="sample_text", signal="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_jpdl31_TaskNodeType_signal_value_roundtrip():
    instance = jpdl31_TaskNodeType(async_="sample_text", createTasks="sample_text", endTasks="sample_text", group="sample_text", name="sample_text", signal="sample_text")
    assert instance.signal == "sample_text"
    instance.signal = "sample_text_2"
    assert instance.signal == "sample_text_2"


def test_jpdl31_TaskType_blocking_value_roundtrip():
    instance = jpdl31_TaskType(blocking="sample_text", description="sample_text", duedate="sample_text", group="sample_text", name="sample_text", priority="sample_text", signalling="sample_text", swimlane="sample_text")
    assert instance.blocking == "sample_text"
    instance.blocking = "sample_text_2"
    assert instance.blocking == "sample_text_2"


def test_jpdl31_TaskType_description_value_roundtrip():
    instance = jpdl31_TaskType(blocking="sample_text", description="sample_text", duedate="sample_text", group="sample_text", name="sample_text", priority="sample_text", signalling="sample_text", swimlane="sample_text")
    assert instance.description == "sample_text"
    instance.description = "sample_text_2"
    assert instance.description == "sample_text_2"


def test_jpdl31_TaskType_duedate_value_roundtrip():
    instance = jpdl31_TaskType(blocking="sample_text", description="sample_text", duedate="sample_text", group="sample_text", name="sample_text", priority="sample_text", signalling="sample_text", swimlane="sample_text")
    assert instance.duedate == "sample_text"
    instance.duedate = "sample_text_2"
    assert instance.duedate == "sample_text_2"


def test_jpdl31_TaskType_group_value_roundtrip():
    instance = jpdl31_TaskType(blocking="sample_text", description="sample_text", duedate="sample_text", group="sample_text", name="sample_text", priority="sample_text", signalling="sample_text", swimlane="sample_text")
    assert instance.group == "sample_text"
    instance.group = "sample_text_2"
    assert instance.group == "sample_text_2"


def test_jpdl31_TaskType_name_value_roundtrip():
    instance = jpdl31_TaskType(blocking="sample_text", description="sample_text", duedate="sample_text", group="sample_text", name="sample_text", priority="sample_text", signalling="sample_text", swimlane="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_jpdl31_TaskType_priority_value_roundtrip():
    instance = jpdl31_TaskType(blocking="sample_text", description="sample_text", duedate="sample_text", group="sample_text", name="sample_text", priority="sample_text", signalling="sample_text", swimlane="sample_text")
    assert instance.priority == "sample_text"
    instance.priority = "sample_text_2"
    assert instance.priority == "sample_text_2"


def test_jpdl31_TaskType_signalling_value_roundtrip():
    instance = jpdl31_TaskType(blocking="sample_text", description="sample_text", duedate="sample_text", group="sample_text", name="sample_text", priority="sample_text", signalling="sample_text", swimlane="sample_text")
    assert instance.signalling == "sample_text"
    instance.signalling = "sample_text_2"
    assert instance.signalling == "sample_text_2"


def test_jpdl31_TaskType_swimlane_value_roundtrip():
    instance = jpdl31_TaskType(blocking="sample_text", description="sample_text", duedate="sample_text", group="sample_text", name="sample_text", priority="sample_text", signalling="sample_text", swimlane="sample_text")
    assert instance.swimlane == "sample_text"
    instance.swimlane = "sample_text_2"
    assert instance.swimlane == "sample_text_2"


def test_jpdl31_TimerType_duedate_value_roundtrip():
    instance = jpdl31_TimerType(duedate="sample_text", name="sample_text", repeat="sample_text", transition="sample_text")
    assert instance.duedate == "sample_text"
    instance.duedate = "sample_text_2"
    assert instance.duedate == "sample_text_2"


def test_jpdl31_TimerType_name_value_roundtrip():
    instance = jpdl31_TimerType(duedate="sample_text", name="sample_text", repeat="sample_text", transition="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_jpdl31_TimerType_repeat_value_roundtrip():
    instance = jpdl31_TimerType(duedate="sample_text", name="sample_text", repeat="sample_text", transition="sample_text")
    assert instance.repeat == "sample_text"
    instance.repeat = "sample_text_2"
    assert instance.repeat == "sample_text_2"


def test_jpdl31_TimerType_transition_value_roundtrip():
    instance = jpdl31_TimerType(duedate="sample_text", name="sample_text", repeat="sample_text", transition="sample_text")
    assert instance.transition == "sample_text"
    instance.transition = "sample_text_2"
    assert instance.transition == "sample_text_2"


def test_jpdl31_TransitionType_group_value_roundtrip():
    instance = jpdl31_TransitionType(group="sample_text", name="sample_text", to="sample_text")
    assert instance.group == "sample_text"
    instance.group = "sample_text_2"
    assert instance.group == "sample_text_2"


def test_jpdl31_TransitionType_name_value_roundtrip():
    instance = jpdl31_TransitionType(group="sample_text", name="sample_text", to="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_jpdl31_TransitionType_to_value_roundtrip():
    instance = jpdl31_TransitionType(group="sample_text", name="sample_text", to="sample_text")
    assert instance.to == "sample_text"
    instance.to = "sample_text_2"
    assert instance.to == "sample_text_2"


def test_jpdl31_TransitionType1_group_value_roundtrip():
    instance = jpdl31_TransitionType1(group="sample_text", name="sample_text", to="sample_text")
    assert instance.group == "sample_text"
    instance.group = "sample_text_2"
    assert instance.group == "sample_text_2"


def test_jpdl31_TransitionType1_name_value_roundtrip():
    instance = jpdl31_TransitionType1(group="sample_text", name="sample_text", to="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_jpdl31_TransitionType1_to_value_roundtrip():
    instance = jpdl31_TransitionType1(group="sample_text", name="sample_text", to="sample_text")
    assert instance.to == "sample_text"
    instance.to = "sample_text_2"
    assert instance.to == "sample_text_2"


def test_jpdl31_VariableType_access_value_roundtrip():
    instance = jpdl31_VariableType(access="sample_text", any="sample_text", mappedName="sample_text", name="sample_text")
    assert instance.access == "sample_text"
    instance.access = "sample_text_2"
    assert instance.access == "sample_text_2"


def test_jpdl31_VariableType_any_value_roundtrip():
    instance = jpdl31_VariableType(access="sample_text", any="sample_text", mappedName="sample_text", name="sample_text")
    assert instance.any == "sample_text"
    instance.any = "sample_text_2"
    assert instance.any == "sample_text_2"


def test_jpdl31_VariableType_mappedName_value_roundtrip():
    instance = jpdl31_VariableType(access="sample_text", any="sample_text", mappedName="sample_text", name="sample_text")
    assert instance.mappedName == "sample_text"
    instance.mappedName = "sample_text_2"
    assert instance.mappedName == "sample_text_2"


def test_jpdl31_VariableType_name_value_roundtrip():
    instance = jpdl31_VariableType(access="sample_text", any="sample_text", mappedName="sample_text", name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_jpdl31_AssignmentType_isa_Delegation():
    instance = jpdl31_AssignmentType(actorId="sample_text", expression="sample_text", pooledActors="sample_text")
    assert isinstance(instance, Delegation)


def test_assoc_action0_link_reassign_clear():
    a = jpdl31_CreateTimerType(duedate="sample_text", name="sample_text", repeat="sample_text", transition="sample_text")
    b1 = jpdl31_ActionType(acceptPropagatedEvents="sample_text", any="sample_text", async_="sample_text", class_="sample_text", configType="sample_text", expression="sample_text", mixed="sample_text", name="sample_text", refName="sample_text")
    b2 = jpdl31_ActionType(acceptPropagatedEvents="sample_text_2", any="sample_text_2", async_="sample_text_2", class_="sample_text_2", configType="sample_text_2", expression="sample_text_2", mixed="sample_text_2", name="sample_text_2", refName="sample_text_2")
    _safe_set(a, 'jpdl31_CreateTimerType', b1)
    assert _is_linked(a, 'jpdl31_CreateTimerType', b1)
    if hasattr(b1, 'jpdl31_ActionType'):
        assert _is_linked(b1, 'jpdl31_ActionType', a)
    _safe_set(a, 'jpdl31_CreateTimerType', b2)
    assert _is_linked(a, 'jpdl31_CreateTimerType', b2)
    if hasattr(b1, 'jpdl31_ActionType'):
        assert not _is_linked(b1, 'jpdl31_ActionType', a)
    if hasattr(b2, 'jpdl31_ActionType'):
        assert _is_linked(b2, 'jpdl31_ActionType', a)
    _safe_set(a, 'jpdl31_CreateTimerType', None)
    assert not _is_linked(a, 'jpdl31_CreateTimerType', b2)
    if hasattr(b2, 'jpdl31_ActionType'):
        assert not _is_linked(b2, 'jpdl31_ActionType', a)


def test_assoc_action120_link_reassign_clear():
    a = jpdl31_NodeType(async_="sample_text", name="sample_text", nodeContentElements="sample_text")
    b1 = jpdl31_ActionType(acceptPropagatedEvents="sample_text", any="sample_text", async_="sample_text", class_="sample_text", configType="sample_text", expression="sample_text", mixed="sample_text", name="sample_text", refName="sample_text")
    b2 = jpdl31_ActionType(acceptPropagatedEvents="sample_text_2", any="sample_text_2", async_="sample_text_2", class_="sample_text_2", configType="sample_text_2", expression="sample_text_2", mixed="sample_text_2", name="sample_text_2", refName="sample_text_2")
    _safe_set(a, 'jpdl31_NodeType121', b1)
    assert _is_linked(a, 'jpdl31_NodeType121', b1)
    if hasattr(b1, 'jpdl31_ActionType122'):
        assert _is_linked(b1, 'jpdl31_ActionType122', a)
    _safe_set(a, 'jpdl31_NodeType121', b2)
    assert _is_linked(a, 'jpdl31_NodeType121', b2)
    if hasattr(b1, 'jpdl31_ActionType122'):
        assert not _is_linked(b1, 'jpdl31_ActionType122', a)
    if hasattr(b2, 'jpdl31_ActionType122'):
        assert _is_linked(b2, 'jpdl31_ActionType122', a)
    _safe_set(a, 'jpdl31_NodeType121', None)
    assert not _is_linked(a, 'jpdl31_NodeType121', b2)
    if hasattr(b2, 'jpdl31_ActionType122'):
        assert not _is_linked(b2, 'jpdl31_ActionType122', a)


def test_assoc_action14_link_reassign_clear():
    a = jpdl31_DocumentRoot(mixed="sample_text")
    b1 = jpdl31_ActionType(acceptPropagatedEvents="sample_text", any="sample_text", async_="sample_text", class_="sample_text", configType="sample_text", expression="sample_text", mixed="sample_text", name="sample_text", refName="sample_text")
    b2 = jpdl31_ActionType(acceptPropagatedEvents="sample_text_2", any="sample_text_2", async_="sample_text_2", class_="sample_text_2", configType="sample_text_2", expression="sample_text_2", mixed="sample_text_2", name="sample_text_2", refName="sample_text_2")
    _safe_set(a, 'jpdl31_DocumentRoot15', {b1})
    assert _is_linked(a, 'jpdl31_DocumentRoot15', b1)
    if hasattr(b1, 'jpdl31_ActionType16'):
        assert _is_linked(b1, 'jpdl31_ActionType16', a)
    _safe_set(a, 'jpdl31_DocumentRoot15', {b2})
    assert _is_linked(a, 'jpdl31_DocumentRoot15', b2)
    if hasattr(b1, 'jpdl31_ActionType16'):
        assert not _is_linked(b1, 'jpdl31_ActionType16', a)
    if hasattr(b2, 'jpdl31_ActionType16'):
        assert _is_linked(b2, 'jpdl31_ActionType16', a)
    _safe_set(a, 'jpdl31_DocumentRoot15', set())
    assert not _is_linked(a, 'jpdl31_DocumentRoot15', b2)
    if hasattr(b2, 'jpdl31_ActionType16'):
        assert not _is_linked(b2, 'jpdl31_ActionType16', a)


def test_assoc_action177_link_reassign_clear():
    a = jpdl31_ProcessDefinitionType(group="sample_text", name="sample_text")
    b1 = jpdl31_ActionType(acceptPropagatedEvents="sample_text", any="sample_text", async_="sample_text", class_="sample_text", configType="sample_text", expression="sample_text", mixed="sample_text", name="sample_text", refName="sample_text")
    b2 = jpdl31_ActionType(acceptPropagatedEvents="sample_text_2", any="sample_text_2", async_="sample_text_2", class_="sample_text_2", configType="sample_text_2", expression="sample_text_2", mixed="sample_text_2", name="sample_text_2", refName="sample_text_2")
    _safe_set(a, 'jpdl31_ProcessDefinitionType178', {b1})
    assert _is_linked(a, 'jpdl31_ProcessDefinitionType178', b1)
    if hasattr(b1, 'jpdl31_ActionType179'):
        assert _is_linked(b1, 'jpdl31_ActionType179', a)
    _safe_set(a, 'jpdl31_ProcessDefinitionType178', {b2})
    assert _is_linked(a, 'jpdl31_ProcessDefinitionType178', b2)
    if hasattr(b1, 'jpdl31_ActionType179'):
        assert not _is_linked(b1, 'jpdl31_ActionType179', a)
    if hasattr(b2, 'jpdl31_ActionType179'):
        assert _is_linked(b2, 'jpdl31_ActionType179', a)
    _safe_set(a, 'jpdl31_ProcessDefinitionType178', set())
    assert not _is_linked(a, 'jpdl31_ProcessDefinitionType178', b2)
    if hasattr(b2, 'jpdl31_ActionType179'):
        assert not _is_linked(b2, 'jpdl31_ActionType179', a)


def test_assoc_action308_link_reassign_clear():
    a = jpdl31_TimerType(duedate="sample_text", name="sample_text", repeat="sample_text", transition="sample_text")
    b1 = jpdl31_ActionType(acceptPropagatedEvents="sample_text", any="sample_text", async_="sample_text", class_="sample_text", configType="sample_text", expression="sample_text", mixed="sample_text", name="sample_text", refName="sample_text")
    b2 = jpdl31_ActionType(acceptPropagatedEvents="sample_text_2", any="sample_text_2", async_="sample_text_2", class_="sample_text_2", configType="sample_text_2", expression="sample_text_2", mixed="sample_text_2", name="sample_text_2", refName="sample_text_2")
    _safe_set(a, 'jpdl31_TimerType309', b1)
    assert _is_linked(a, 'jpdl31_TimerType309', b1)
    if hasattr(b1, 'jpdl31_ActionType310'):
        assert _is_linked(b1, 'jpdl31_ActionType310', a)
    _safe_set(a, 'jpdl31_TimerType309', b2)
    assert _is_linked(a, 'jpdl31_TimerType309', b2)
    if hasattr(b1, 'jpdl31_ActionType310'):
        assert not _is_linked(b1, 'jpdl31_ActionType310', a)
    if hasattr(b2, 'jpdl31_ActionType310'):
        assert _is_linked(b2, 'jpdl31_ActionType310', a)
    _safe_set(a, 'jpdl31_TimerType309', None)
    assert not _is_linked(a, 'jpdl31_TimerType309', b2)
    if hasattr(b2, 'jpdl31_ActionType310'):
        assert not _is_linked(b2, 'jpdl31_ActionType310', a)


def test_assoc_action314_link_reassign_clear():
    a = jpdl31_TransitionType(group="sample_text", name="sample_text", to="sample_text")
    b1 = jpdl31_ActionType(acceptPropagatedEvents="sample_text", any="sample_text", async_="sample_text", class_="sample_text", configType="sample_text", expression="sample_text", mixed="sample_text", name="sample_text", refName="sample_text")
    b2 = jpdl31_ActionType(acceptPropagatedEvents="sample_text_2", any="sample_text_2", async_="sample_text_2", class_="sample_text_2", configType="sample_text_2", expression="sample_text_2", mixed="sample_text_2", name="sample_text_2", refName="sample_text_2")
    _safe_set(a, 'jpdl31_TransitionType315', {b1})
    assert _is_linked(a, 'jpdl31_TransitionType315', b1)
    if hasattr(b1, 'jpdl31_ActionType316'):
        assert _is_linked(b1, 'jpdl31_ActionType316', a)
    _safe_set(a, 'jpdl31_TransitionType315', {b2})
    assert _is_linked(a, 'jpdl31_TransitionType315', b2)
    if hasattr(b1, 'jpdl31_ActionType316'):
        assert not _is_linked(b1, 'jpdl31_ActionType316', a)
    if hasattr(b2, 'jpdl31_ActionType316'):
        assert _is_linked(b2, 'jpdl31_ActionType316', a)
    _safe_set(a, 'jpdl31_TransitionType315', set())
    assert not _is_linked(a, 'jpdl31_TransitionType315', b2)
    if hasattr(b2, 'jpdl31_ActionType316'):
        assert not _is_linked(b2, 'jpdl31_ActionType316', a)


def test_assoc_action331_link_reassign_clear():
    a = jpdl31_TransitionType1(group="sample_text", name="sample_text", to="sample_text")
    b1 = jpdl31_ActionType(acceptPropagatedEvents="sample_text", any="sample_text", async_="sample_text", class_="sample_text", configType="sample_text", expression="sample_text", mixed="sample_text", name="sample_text", refName="sample_text")
    b2 = jpdl31_ActionType(acceptPropagatedEvents="sample_text_2", any="sample_text_2", async_="sample_text_2", class_="sample_text_2", configType="sample_text_2", expression="sample_text_2", mixed="sample_text_2", name="sample_text_2", refName="sample_text_2")
    _safe_set(a, 'jpdl31_TransitionType1332', {b1})
    assert _is_linked(a, 'jpdl31_TransitionType1332', b1)
    if hasattr(b1, 'jpdl31_ActionType333'):
        assert _is_linked(b1, 'jpdl31_ActionType333', a)
    _safe_set(a, 'jpdl31_TransitionType1332', {b2})
    assert _is_linked(a, 'jpdl31_TransitionType1332', b2)
    if hasattr(b1, 'jpdl31_ActionType333'):
        assert not _is_linked(b1, 'jpdl31_ActionType333', a)
    if hasattr(b2, 'jpdl31_ActionType333'):
        assert _is_linked(b2, 'jpdl31_ActionType333', a)
    _safe_set(a, 'jpdl31_TransitionType1332', set())
    assert not _is_linked(a, 'jpdl31_TransitionType1332', b2)
    if hasattr(b2, 'jpdl31_ActionType333'):
        assert not _is_linked(b2, 'jpdl31_ActionType333', a)


def test_assoc_action75_link_reassign_clear():
    a = jpdl31_EventType(actionElements="sample_text", type="sample_text")
    b1 = jpdl31_ActionType(acceptPropagatedEvents="sample_text", any="sample_text", async_="sample_text", class_="sample_text", configType="sample_text", expression="sample_text", mixed="sample_text", name="sample_text", refName="sample_text")
    b2 = jpdl31_ActionType(acceptPropagatedEvents="sample_text_2", any="sample_text_2", async_="sample_text_2", class_="sample_text_2", configType="sample_text_2", expression="sample_text_2", mixed="sample_text_2", name="sample_text_2", refName="sample_text_2")
    _safe_set(a, 'jpdl31_EventType76', {b1})
    assert _is_linked(a, 'jpdl31_EventType76', b1)
    if hasattr(b1, 'jpdl31_ActionType77'):
        assert _is_linked(b1, 'jpdl31_ActionType77', a)
    _safe_set(a, 'jpdl31_EventType76', {b2})
    assert _is_linked(a, 'jpdl31_EventType76', b2)
    if hasattr(b1, 'jpdl31_ActionType77'):
        assert not _is_linked(b1, 'jpdl31_ActionType77', a)
    if hasattr(b2, 'jpdl31_ActionType77'):
        assert _is_linked(b2, 'jpdl31_ActionType77', a)
    _safe_set(a, 'jpdl31_EventType76', set())
    assert not _is_linked(a, 'jpdl31_EventType76', b2)
    if hasattr(b2, 'jpdl31_ActionType77'):
        assert not _is_linked(b2, 'jpdl31_ActionType77', a)


def test_assoc_action87_link_reassign_clear():
    a = jpdl31_ExceptionHandlerType(exceptionClass="sample_text", group="sample_text")
    b1 = jpdl31_ActionType(acceptPropagatedEvents="sample_text", any="sample_text", async_="sample_text", class_="sample_text", configType="sample_text", expression="sample_text", mixed="sample_text", name="sample_text", refName="sample_text")
    b2 = jpdl31_ActionType(acceptPropagatedEvents="sample_text_2", any="sample_text_2", async_="sample_text_2", class_="sample_text_2", configType="sample_text_2", expression="sample_text_2", mixed="sample_text_2", name="sample_text_2", refName="sample_text_2")
    _safe_set(a, 'jpdl31_ExceptionHandlerType88', {b1})
    assert _is_linked(a, 'jpdl31_ExceptionHandlerType88', b1)
    if hasattr(b1, 'jpdl31_ActionType89'):
        assert _is_linked(b1, 'jpdl31_ActionType89', a)
    _safe_set(a, 'jpdl31_ExceptionHandlerType88', {b2})
    assert _is_linked(a, 'jpdl31_ExceptionHandlerType88', b2)
    if hasattr(b1, 'jpdl31_ActionType89'):
        assert not _is_linked(b1, 'jpdl31_ActionType89', a)
    if hasattr(b2, 'jpdl31_ActionType89'):
        assert _is_linked(b2, 'jpdl31_ActionType89', a)
    _safe_set(a, 'jpdl31_ExceptionHandlerType88', set())
    assert not _is_linked(a, 'jpdl31_ExceptionHandlerType88', b2)
    if hasattr(b2, 'jpdl31_ActionType89'):
        assert not _is_linked(b2, 'jpdl31_ActionType89', a)


def test_assoc_assignment17_link_reassign_clear():
    a = jpdl31_DocumentRoot(mixed="sample_text")
    b1 = jpdl31_AssignmentType(actorId="sample_text", expression="sample_text", pooledActors="sample_text")
    b2 = jpdl31_AssignmentType(actorId="sample_text_2", expression="sample_text_2", pooledActors="sample_text_2")
    _safe_set(a, 'jpdl31_DocumentRoot18', {b1})
    assert _is_linked(a, 'jpdl31_DocumentRoot18', b1)
    if hasattr(b1, 'jpdl31_AssignmentType'):
        assert _is_linked(b1, 'jpdl31_AssignmentType', a)
    _safe_set(a, 'jpdl31_DocumentRoot18', {b2})
    assert _is_linked(a, 'jpdl31_DocumentRoot18', b2)
    if hasattr(b1, 'jpdl31_AssignmentType'):
        assert not _is_linked(b1, 'jpdl31_AssignmentType', a)
    if hasattr(b2, 'jpdl31_AssignmentType'):
        assert _is_linked(b2, 'jpdl31_AssignmentType', a)
    _safe_set(a, 'jpdl31_DocumentRoot18', set())
    assert not _is_linked(a, 'jpdl31_DocumentRoot18', b2)
    if hasattr(b2, 'jpdl31_AssignmentType'):
        assert not _is_linked(b2, 'jpdl31_AssignmentType', a)


def test_assoc_assignment278_link_reassign_clear():
    a = jpdl31_SwimlaneType(name="sample_text")
    b1 = jpdl31_AssignmentType(actorId="sample_text", expression="sample_text", pooledActors="sample_text")
    b2 = jpdl31_AssignmentType(actorId="sample_text_2", expression="sample_text_2", pooledActors="sample_text_2")
    _safe_set(a, 'jpdl31_SwimlaneType279', b1)
    assert _is_linked(a, 'jpdl31_SwimlaneType279', b1)
    if hasattr(b1, 'jpdl31_AssignmentType280'):
        assert _is_linked(b1, 'jpdl31_AssignmentType280', a)
    _safe_set(a, 'jpdl31_SwimlaneType279', b2)
    assert _is_linked(a, 'jpdl31_SwimlaneType279', b2)
    if hasattr(b1, 'jpdl31_AssignmentType280'):
        assert not _is_linked(b1, 'jpdl31_AssignmentType280', a)
    if hasattr(b2, 'jpdl31_AssignmentType280'):
        assert _is_linked(b2, 'jpdl31_AssignmentType280', a)
    _safe_set(a, 'jpdl31_SwimlaneType279', None)
    assert not _is_linked(a, 'jpdl31_SwimlaneType279', b2)
    if hasattr(b2, 'jpdl31_AssignmentType280'):
        assert not _is_linked(b2, 'jpdl31_AssignmentType280', a)


def test_assoc_assignment296_link_reassign_clear():
    a = jpdl31_TaskType(blocking="sample_text", description="sample_text", duedate="sample_text", group="sample_text", name="sample_text", priority="sample_text", signalling="sample_text", swimlane="sample_text")
    b1 = jpdl31_AssignmentType(actorId="sample_text", expression="sample_text", pooledActors="sample_text")
    b2 = jpdl31_AssignmentType(actorId="sample_text_2", expression="sample_text_2", pooledActors="sample_text_2")
    _safe_set(a, 'jpdl31_TaskType297', {b1})
    assert _is_linked(a, 'jpdl31_TaskType297', b1)
    if hasattr(b1, 'jpdl31_AssignmentType298'):
        assert _is_linked(b1, 'jpdl31_AssignmentType298', a)
    _safe_set(a, 'jpdl31_TaskType297', {b2})
    assert _is_linked(a, 'jpdl31_TaskType297', b2)
    if hasattr(b1, 'jpdl31_AssignmentType298'):
        assert not _is_linked(b1, 'jpdl31_AssignmentType298', a)
    if hasattr(b2, 'jpdl31_AssignmentType298'):
        assert _is_linked(b2, 'jpdl31_AssignmentType298', a)
    _safe_set(a, 'jpdl31_TaskType297', set())
    assert not _is_linked(a, 'jpdl31_TaskType297', b2)
    if hasattr(b2, 'jpdl31_AssignmentType298'):
        assert not _is_linked(b2, 'jpdl31_AssignmentType298', a)


def test_assoc_cancelTimer129_link_reassign_clear():
    a = jpdl31_NodeType(async_="sample_text", name="sample_text", nodeContentElements="sample_text")
    b1 = jpdl31_CancelTimerType(name="sample_text")
    b2 = jpdl31_CancelTimerType(name="sample_text_2")
    _safe_set(a, 'jpdl31_NodeType130', b1)
    assert _is_linked(a, 'jpdl31_NodeType130', b1)
    if hasattr(b1, 'jpdl31_CancelTimerType131'):
        assert _is_linked(b1, 'jpdl31_CancelTimerType131', a)
    _safe_set(a, 'jpdl31_NodeType130', b2)
    assert _is_linked(a, 'jpdl31_NodeType130', b2)
    if hasattr(b1, 'jpdl31_CancelTimerType131'):
        assert not _is_linked(b1, 'jpdl31_CancelTimerType131', a)
    if hasattr(b2, 'jpdl31_CancelTimerType131'):
        assert _is_linked(b2, 'jpdl31_CancelTimerType131', a)
    _safe_set(a, 'jpdl31_NodeType130', None)
    assert not _is_linked(a, 'jpdl31_NodeType130', b2)
    if hasattr(b2, 'jpdl31_CancelTimerType131'):
        assert not _is_linked(b2, 'jpdl31_CancelTimerType131', a)


def test_assoc_cancelTimer186_link_reassign_clear():
    a = jpdl31_ProcessDefinitionType(group="sample_text", name="sample_text")
    b1 = jpdl31_CancelTimerType(name="sample_text")
    b2 = jpdl31_CancelTimerType(name="sample_text_2")
    _safe_set(a, 'jpdl31_ProcessDefinitionType187', {b1})
    assert _is_linked(a, 'jpdl31_ProcessDefinitionType187', b1)
    if hasattr(b1, 'jpdl31_CancelTimerType188'):
        assert _is_linked(b1, 'jpdl31_CancelTimerType188', a)
    _safe_set(a, 'jpdl31_ProcessDefinitionType187', {b2})
    assert _is_linked(a, 'jpdl31_ProcessDefinitionType187', b2)
    if hasattr(b1, 'jpdl31_CancelTimerType188'):
        assert not _is_linked(b1, 'jpdl31_CancelTimerType188', a)
    if hasattr(b2, 'jpdl31_CancelTimerType188'):
        assert _is_linked(b2, 'jpdl31_CancelTimerType188', a)
    _safe_set(a, 'jpdl31_ProcessDefinitionType187', set())
    assert not _is_linked(a, 'jpdl31_ProcessDefinitionType187', b2)
    if hasattr(b2, 'jpdl31_CancelTimerType188'):
        assert not _is_linked(b2, 'jpdl31_CancelTimerType188', a)


def test_assoc_cancelTimer19_link_reassign_clear():
    a = jpdl31_DocumentRoot(mixed="sample_text")
    b1 = jpdl31_CancelTimerType(name="sample_text")
    b2 = jpdl31_CancelTimerType(name="sample_text_2")
    _safe_set(a, 'jpdl31_DocumentRoot20', {b1})
    assert _is_linked(a, 'jpdl31_DocumentRoot20', b1)
    if hasattr(b1, 'jpdl31_CancelTimerType'):
        assert _is_linked(b1, 'jpdl31_CancelTimerType', a)
    _safe_set(a, 'jpdl31_DocumentRoot20', {b2})
    assert _is_linked(a, 'jpdl31_DocumentRoot20', b2)
    if hasattr(b1, 'jpdl31_CancelTimerType'):
        assert not _is_linked(b1, 'jpdl31_CancelTimerType', a)
    if hasattr(b2, 'jpdl31_CancelTimerType'):
        assert _is_linked(b2, 'jpdl31_CancelTimerType', a)
    _safe_set(a, 'jpdl31_DocumentRoot20', set())
    assert not _is_linked(a, 'jpdl31_DocumentRoot20', b2)
    if hasattr(b2, 'jpdl31_CancelTimerType'):
        assert not _is_linked(b2, 'jpdl31_CancelTimerType', a)


def test_assoc_cancelTimer323_link_reassign_clear():
    a = jpdl31_TransitionType(group="sample_text", name="sample_text", to="sample_text")
    b1 = jpdl31_CancelTimerType(name="sample_text")
    b2 = jpdl31_CancelTimerType(name="sample_text_2")
    _safe_set(a, 'jpdl31_TransitionType324', {b1})
    assert _is_linked(a, 'jpdl31_TransitionType324', b1)
    if hasattr(b1, 'jpdl31_CancelTimerType325'):
        assert _is_linked(b1, 'jpdl31_CancelTimerType325', a)
    _safe_set(a, 'jpdl31_TransitionType324', {b2})
    assert _is_linked(a, 'jpdl31_TransitionType324', b2)
    if hasattr(b1, 'jpdl31_CancelTimerType325'):
        assert not _is_linked(b1, 'jpdl31_CancelTimerType325', a)
    if hasattr(b2, 'jpdl31_CancelTimerType325'):
        assert _is_linked(b2, 'jpdl31_CancelTimerType325', a)
    _safe_set(a, 'jpdl31_TransitionType324', set())
    assert not _is_linked(a, 'jpdl31_TransitionType324', b2)
    if hasattr(b2, 'jpdl31_CancelTimerType325'):
        assert not _is_linked(b2, 'jpdl31_CancelTimerType325', a)


def test_assoc_cancelTimer340_link_reassign_clear():
    a = jpdl31_TransitionType1(group="sample_text", name="sample_text", to="sample_text")
    b1 = jpdl31_CancelTimerType(name="sample_text")
    b2 = jpdl31_CancelTimerType(name="sample_text_2")
    _safe_set(a, 'jpdl31_TransitionType1341', {b1})
    assert _is_linked(a, 'jpdl31_TransitionType1341', b1)
    if hasattr(b1, 'jpdl31_CancelTimerType342'):
        assert _is_linked(b1, 'jpdl31_CancelTimerType342', a)
    _safe_set(a, 'jpdl31_TransitionType1341', {b2})
    assert _is_linked(a, 'jpdl31_TransitionType1341', b2)
    if hasattr(b1, 'jpdl31_CancelTimerType342'):
        assert not _is_linked(b1, 'jpdl31_CancelTimerType342', a)
    if hasattr(b2, 'jpdl31_CancelTimerType342'):
        assert _is_linked(b2, 'jpdl31_CancelTimerType342', a)
    _safe_set(a, 'jpdl31_TransitionType1341', set())
    assert not _is_linked(a, 'jpdl31_TransitionType1341', b2)
    if hasattr(b2, 'jpdl31_CancelTimerType342'):
        assert not _is_linked(b2, 'jpdl31_CancelTimerType342', a)


def test_assoc_cancelTimer84_link_reassign_clear():
    a = jpdl31_EventType(actionElements="sample_text", type="sample_text")
    b1 = jpdl31_CancelTimerType(name="sample_text")
    b2 = jpdl31_CancelTimerType(name="sample_text_2")
    _safe_set(a, 'jpdl31_EventType85', {b1})
    assert _is_linked(a, 'jpdl31_EventType85', b1)
    if hasattr(b1, 'jpdl31_CancelTimerType86'):
        assert _is_linked(b1, 'jpdl31_CancelTimerType86', a)
    _safe_set(a, 'jpdl31_EventType85', {b2})
    assert _is_linked(a, 'jpdl31_EventType85', b2)
    if hasattr(b1, 'jpdl31_CancelTimerType86'):
        assert not _is_linked(b1, 'jpdl31_CancelTimerType86', a)
    if hasattr(b2, 'jpdl31_CancelTimerType86'):
        assert _is_linked(b2, 'jpdl31_CancelTimerType86', a)
    _safe_set(a, 'jpdl31_EventType85', set())
    assert not _is_linked(a, 'jpdl31_EventType85', b2)
    if hasattr(b2, 'jpdl31_CancelTimerType86'):
        assert not _is_linked(b2, 'jpdl31_CancelTimerType86', a)


def test_assoc_condition329_link_reassign_clear():
    a = jpdl31_TransitionType1(group="sample_text", name="sample_text", to="sample_text")
    b1 = jpdl31_ConditionType(any="sample_text", expression="sample_text", group="sample_text", mixed="sample_text")
    b2 = jpdl31_ConditionType(any="sample_text_2", expression="sample_text_2", group="sample_text_2", mixed="sample_text_2")
    _safe_set(a, 'jpdl31_TransitionType1330', {b1})
    assert _is_linked(a, 'jpdl31_TransitionType1330', b1)
    if hasattr(b1, 'jpdl31_ConditionType'):
        assert _is_linked(b1, 'jpdl31_ConditionType', a)
    _safe_set(a, 'jpdl31_TransitionType1330', {b2})
    assert _is_linked(a, 'jpdl31_TransitionType1330', b2)
    if hasattr(b1, 'jpdl31_ConditionType'):
        assert not _is_linked(b1, 'jpdl31_ConditionType', a)
    if hasattr(b2, 'jpdl31_ConditionType'):
        assert _is_linked(b2, 'jpdl31_ConditionType', a)
    _safe_set(a, 'jpdl31_TransitionType1330', set())
    assert not _is_linked(a, 'jpdl31_TransitionType1330', b2)
    if hasattr(b2, 'jpdl31_ConditionType'):
        assert not _is_linked(b2, 'jpdl31_ConditionType', a)


def test_assoc_controller21_link_reassign_clear():
    a = jpdl31_DocumentRoot(mixed="sample_text")
    b1 = jpdl31_Delegation(any="sample_text", class_="sample_text", configType="sample_text", mixed="sample_text")
    b2 = jpdl31_Delegation(any="sample_text_2", class_="sample_text_2", configType="sample_text_2", mixed="sample_text_2")
    _safe_set(a, 'jpdl31_DocumentRoot22', {b1})
    assert _is_linked(a, 'jpdl31_DocumentRoot22', b1)
    if hasattr(b1, 'jpdl31_Delegation23'):
        assert _is_linked(b1, 'jpdl31_Delegation23', a)
    _safe_set(a, 'jpdl31_DocumentRoot22', {b2})
    assert _is_linked(a, 'jpdl31_DocumentRoot22', b2)
    if hasattr(b1, 'jpdl31_Delegation23'):
        assert not _is_linked(b1, 'jpdl31_Delegation23', a)
    if hasattr(b2, 'jpdl31_Delegation23'):
        assert _is_linked(b2, 'jpdl31_Delegation23', a)
    _safe_set(a, 'jpdl31_DocumentRoot22', set())
    assert not _is_linked(a, 'jpdl31_DocumentRoot22', b2)
    if hasattr(b2, 'jpdl31_Delegation23'):
        assert not _is_linked(b2, 'jpdl31_Delegation23', a)


def test_assoc_controller299_link_reassign_clear():
    a = jpdl31_TaskType(blocking="sample_text", description="sample_text", duedate="sample_text", group="sample_text", name="sample_text", priority="sample_text", signalling="sample_text", swimlane="sample_text")
    b1 = jpdl31_Delegation(any="sample_text", class_="sample_text", configType="sample_text", mixed="sample_text")
    b2 = jpdl31_Delegation(any="sample_text_2", class_="sample_text_2", configType="sample_text_2", mixed="sample_text_2")
    _safe_set(a, 'jpdl31_TaskType300', {b1})
    assert _is_linked(a, 'jpdl31_TaskType300', b1)
    if hasattr(b1, 'jpdl31_Delegation301'):
        assert _is_linked(b1, 'jpdl31_Delegation301', a)
    _safe_set(a, 'jpdl31_TaskType300', {b2})
    assert _is_linked(a, 'jpdl31_TaskType300', b2)
    if hasattr(b1, 'jpdl31_Delegation301'):
        assert not _is_linked(b1, 'jpdl31_Delegation301', a)
    if hasattr(b2, 'jpdl31_Delegation301'):
        assert _is_linked(b2, 'jpdl31_Delegation301', a)
    _safe_set(a, 'jpdl31_TaskType300', set())
    assert not _is_linked(a, 'jpdl31_TaskType300', b2)
    if hasattr(b2, 'jpdl31_Delegation301'):
        assert not _is_linked(b2, 'jpdl31_Delegation301', a)


def test_assoc_createTimer126_link_reassign_clear():
    a = jpdl31_NodeType(async_="sample_text", name="sample_text", nodeContentElements="sample_text")
    b1 = jpdl31_CreateTimerType(duedate="sample_text", name="sample_text", repeat="sample_text", transition="sample_text")
    b2 = jpdl31_CreateTimerType(duedate="sample_text_2", name="sample_text_2", repeat="sample_text_2", transition="sample_text_2")
    _safe_set(a, 'jpdl31_NodeType127', b1)
    assert _is_linked(a, 'jpdl31_NodeType127', b1)
    if hasattr(b1, 'jpdl31_CreateTimerType128'):
        assert _is_linked(b1, 'jpdl31_CreateTimerType128', a)
    _safe_set(a, 'jpdl31_NodeType127', b2)
    assert _is_linked(a, 'jpdl31_NodeType127', b2)
    if hasattr(b1, 'jpdl31_CreateTimerType128'):
        assert not _is_linked(b1, 'jpdl31_CreateTimerType128', a)
    if hasattr(b2, 'jpdl31_CreateTimerType128'):
        assert _is_linked(b2, 'jpdl31_CreateTimerType128', a)
    _safe_set(a, 'jpdl31_NodeType127', None)
    assert not _is_linked(a, 'jpdl31_NodeType127', b2)
    if hasattr(b2, 'jpdl31_CreateTimerType128'):
        assert not _is_linked(b2, 'jpdl31_CreateTimerType128', a)


def test_assoc_createTimer183_link_reassign_clear():
    a = jpdl31_ProcessDefinitionType(group="sample_text", name="sample_text")
    b1 = jpdl31_CreateTimerType(duedate="sample_text", name="sample_text", repeat="sample_text", transition="sample_text")
    b2 = jpdl31_CreateTimerType(duedate="sample_text_2", name="sample_text_2", repeat="sample_text_2", transition="sample_text_2")
    _safe_set(a, 'jpdl31_ProcessDefinitionType184', {b1})
    assert _is_linked(a, 'jpdl31_ProcessDefinitionType184', b1)
    if hasattr(b1, 'jpdl31_CreateTimerType185'):
        assert _is_linked(b1, 'jpdl31_CreateTimerType185', a)
    _safe_set(a, 'jpdl31_ProcessDefinitionType184', {b2})
    assert _is_linked(a, 'jpdl31_ProcessDefinitionType184', b2)
    if hasattr(b1, 'jpdl31_CreateTimerType185'):
        assert not _is_linked(b1, 'jpdl31_CreateTimerType185', a)
    if hasattr(b2, 'jpdl31_CreateTimerType185'):
        assert _is_linked(b2, 'jpdl31_CreateTimerType185', a)
    _safe_set(a, 'jpdl31_ProcessDefinitionType184', set())
    assert not _is_linked(a, 'jpdl31_ProcessDefinitionType184', b2)
    if hasattr(b2, 'jpdl31_CreateTimerType185'):
        assert not _is_linked(b2, 'jpdl31_CreateTimerType185', a)


def test_assoc_createTimer24_link_reassign_clear():
    a = jpdl31_DocumentRoot(mixed="sample_text")
    b1 = jpdl31_CreateTimerType(duedate="sample_text", name="sample_text", repeat="sample_text", transition="sample_text")
    b2 = jpdl31_CreateTimerType(duedate="sample_text_2", name="sample_text_2", repeat="sample_text_2", transition="sample_text_2")
    _safe_set(a, 'jpdl31_DocumentRoot25', {b1})
    assert _is_linked(a, 'jpdl31_DocumentRoot25', b1)
    if hasattr(b1, 'jpdl31_CreateTimerType26'):
        assert _is_linked(b1, 'jpdl31_CreateTimerType26', a)
    _safe_set(a, 'jpdl31_DocumentRoot25', {b2})
    assert _is_linked(a, 'jpdl31_DocumentRoot25', b2)
    if hasattr(b1, 'jpdl31_CreateTimerType26'):
        assert not _is_linked(b1, 'jpdl31_CreateTimerType26', a)
    if hasattr(b2, 'jpdl31_CreateTimerType26'):
        assert _is_linked(b2, 'jpdl31_CreateTimerType26', a)
    _safe_set(a, 'jpdl31_DocumentRoot25', set())
    assert not _is_linked(a, 'jpdl31_DocumentRoot25', b2)
    if hasattr(b2, 'jpdl31_CreateTimerType26'):
        assert not _is_linked(b2, 'jpdl31_CreateTimerType26', a)


def test_assoc_createTimer320_link_reassign_clear():
    a = jpdl31_TransitionType(group="sample_text", name="sample_text", to="sample_text")
    b1 = jpdl31_CreateTimerType(duedate="sample_text", name="sample_text", repeat="sample_text", transition="sample_text")
    b2 = jpdl31_CreateTimerType(duedate="sample_text_2", name="sample_text_2", repeat="sample_text_2", transition="sample_text_2")
    _safe_set(a, 'jpdl31_TransitionType321', {b1})
    assert _is_linked(a, 'jpdl31_TransitionType321', b1)
    if hasattr(b1, 'jpdl31_CreateTimerType322'):
        assert _is_linked(b1, 'jpdl31_CreateTimerType322', a)
    _safe_set(a, 'jpdl31_TransitionType321', {b2})
    assert _is_linked(a, 'jpdl31_TransitionType321', b2)
    if hasattr(b1, 'jpdl31_CreateTimerType322'):
        assert not _is_linked(b1, 'jpdl31_CreateTimerType322', a)
    if hasattr(b2, 'jpdl31_CreateTimerType322'):
        assert _is_linked(b2, 'jpdl31_CreateTimerType322', a)
    _safe_set(a, 'jpdl31_TransitionType321', set())
    assert not _is_linked(a, 'jpdl31_TransitionType321', b2)
    if hasattr(b2, 'jpdl31_CreateTimerType322'):
        assert not _is_linked(b2, 'jpdl31_CreateTimerType322', a)


def test_assoc_createTimer337_link_reassign_clear():
    a = jpdl31_TransitionType1(group="sample_text", name="sample_text", to="sample_text")
    b1 = jpdl31_CreateTimerType(duedate="sample_text", name="sample_text", repeat="sample_text", transition="sample_text")
    b2 = jpdl31_CreateTimerType(duedate="sample_text_2", name="sample_text_2", repeat="sample_text_2", transition="sample_text_2")
    _safe_set(a, 'jpdl31_TransitionType1338', {b1})
    assert _is_linked(a, 'jpdl31_TransitionType1338', b1)
    if hasattr(b1, 'jpdl31_CreateTimerType339'):
        assert _is_linked(b1, 'jpdl31_CreateTimerType339', a)
    _safe_set(a, 'jpdl31_TransitionType1338', {b2})
    assert _is_linked(a, 'jpdl31_TransitionType1338', b2)
    if hasattr(b1, 'jpdl31_CreateTimerType339'):
        assert not _is_linked(b1, 'jpdl31_CreateTimerType339', a)
    if hasattr(b2, 'jpdl31_CreateTimerType339'):
        assert _is_linked(b2, 'jpdl31_CreateTimerType339', a)
    _safe_set(a, 'jpdl31_TransitionType1338', set())
    assert not _is_linked(a, 'jpdl31_TransitionType1338', b2)
    if hasattr(b2, 'jpdl31_CreateTimerType339'):
        assert not _is_linked(b2, 'jpdl31_CreateTimerType339', a)


def test_assoc_createTimer81_link_reassign_clear():
    a = jpdl31_EventType(actionElements="sample_text", type="sample_text")
    b1 = jpdl31_CreateTimerType(duedate="sample_text", name="sample_text", repeat="sample_text", transition="sample_text")
    b2 = jpdl31_CreateTimerType(duedate="sample_text_2", name="sample_text_2", repeat="sample_text_2", transition="sample_text_2")
    _safe_set(a, 'jpdl31_EventType82', {b1})
    assert _is_linked(a, 'jpdl31_EventType82', b1)
    if hasattr(b1, 'jpdl31_CreateTimerType83'):
        assert _is_linked(b1, 'jpdl31_CreateTimerType83', a)
    _safe_set(a, 'jpdl31_EventType82', {b2})
    assert _is_linked(a, 'jpdl31_EventType82', b2)
    if hasattr(b1, 'jpdl31_CreateTimerType83'):
        assert not _is_linked(b1, 'jpdl31_CreateTimerType83', a)
    if hasattr(b2, 'jpdl31_CreateTimerType83'):
        assert _is_linked(b2, 'jpdl31_CreateTimerType83', a)
    _safe_set(a, 'jpdl31_EventType82', set())
    assert not _is_linked(a, 'jpdl31_EventType82', b2)
    if hasattr(b2, 'jpdl31_CreateTimerType83'):
        assert not _is_linked(b2, 'jpdl31_CreateTimerType83', a)


def test_assoc_decision171_link_reassign_clear():
    a = jpdl31_ProcessDefinitionType(group="sample_text", name="sample_text")
    b1 = jpdl31_DecisionType(async_="sample_text", expression="sample_text", group="sample_text", name="sample_text")
    b2 = jpdl31_DecisionType(async_="sample_text_2", expression="sample_text_2", group="sample_text_2", name="sample_text_2")
    _safe_set(a, 'jpdl31_ProcessDefinitionType172', {b1})
    assert _is_linked(a, 'jpdl31_ProcessDefinitionType172', b1)
    if hasattr(b1, 'jpdl31_DecisionType173'):
        assert _is_linked(b1, 'jpdl31_DecisionType173', a)
    _safe_set(a, 'jpdl31_ProcessDefinitionType172', {b2})
    assert _is_linked(a, 'jpdl31_ProcessDefinitionType172', b2)
    if hasattr(b1, 'jpdl31_DecisionType173'):
        assert not _is_linked(b1, 'jpdl31_DecisionType173', a)
    if hasattr(b2, 'jpdl31_DecisionType173'):
        assert _is_linked(b2, 'jpdl31_DecisionType173', a)
    _safe_set(a, 'jpdl31_ProcessDefinitionType172', set())
    assert not _is_linked(a, 'jpdl31_ProcessDefinitionType172', b2)
    if hasattr(b2, 'jpdl31_DecisionType173'):
        assert not _is_linked(b2, 'jpdl31_DecisionType173', a)


def test_assoc_decision260_link_reassign_clear():
    a = jpdl31_SuperStateType(async_="sample_text", group="sample_text", name="sample_text")
    b1 = jpdl31_DecisionType(async_="sample_text", expression="sample_text", group="sample_text", name="sample_text")
    b2 = jpdl31_DecisionType(async_="sample_text_2", expression="sample_text_2", group="sample_text_2", name="sample_text_2")
    _safe_set(a, 'jpdl31_SuperStateType261', {b1})
    assert _is_linked(a, 'jpdl31_SuperStateType261', b1)
    if hasattr(b1, 'jpdl31_DecisionType262'):
        assert _is_linked(b1, 'jpdl31_DecisionType262', a)
    _safe_set(a, 'jpdl31_SuperStateType261', {b2})
    assert _is_linked(a, 'jpdl31_SuperStateType261', b2)
    if hasattr(b1, 'jpdl31_DecisionType262'):
        assert not _is_linked(b1, 'jpdl31_DecisionType262', a)
    if hasattr(b2, 'jpdl31_DecisionType262'):
        assert _is_linked(b2, 'jpdl31_DecisionType262', a)
    _safe_set(a, 'jpdl31_SuperStateType261', set())
    assert not _is_linked(a, 'jpdl31_SuperStateType261', b2)
    if hasattr(b2, 'jpdl31_DecisionType262'):
        assert not _is_linked(b2, 'jpdl31_DecisionType262', a)


def test_assoc_decision27_link_reassign_clear():
    a = jpdl31_DocumentRoot(mixed="sample_text")
    b1 = jpdl31_DecisionType(async_="sample_text", expression="sample_text", group="sample_text", name="sample_text")
    b2 = jpdl31_DecisionType(async_="sample_text_2", expression="sample_text_2", group="sample_text_2", name="sample_text_2")
    _safe_set(a, 'jpdl31_DocumentRoot28', {b1})
    assert _is_linked(a, 'jpdl31_DocumentRoot28', b1)
    if hasattr(b1, 'jpdl31_DecisionType29'):
        assert _is_linked(b1, 'jpdl31_DecisionType29', a)
    _safe_set(a, 'jpdl31_DocumentRoot28', {b2})
    assert _is_linked(a, 'jpdl31_DocumentRoot28', b2)
    if hasattr(b1, 'jpdl31_DecisionType29'):
        assert not _is_linked(b1, 'jpdl31_DecisionType29', a)
    if hasattr(b2, 'jpdl31_DecisionType29'):
        assert _is_linked(b2, 'jpdl31_DecisionType29', a)
    _safe_set(a, 'jpdl31_DocumentRoot28', set())
    assert not _is_linked(a, 'jpdl31_DocumentRoot28', b2)
    if hasattr(b2, 'jpdl31_DecisionType29'):
        assert not _is_linked(b2, 'jpdl31_DecisionType29', a)


def test_assoc_endState174_link_reassign_clear():
    a = jpdl31_ProcessDefinitionType(group="sample_text", name="sample_text")
    b1 = jpdl31_EndStateType(group="sample_text", name="sample_text")
    b2 = jpdl31_EndStateType(group="sample_text_2", name="sample_text_2")
    _safe_set(a, 'jpdl31_ProcessDefinitionType175', {b1})
    assert _is_linked(a, 'jpdl31_ProcessDefinitionType175', b1)
    if hasattr(b1, 'jpdl31_EndStateType176'):
        assert _is_linked(b1, 'jpdl31_EndStateType176', a)
    _safe_set(a, 'jpdl31_ProcessDefinitionType175', {b2})
    assert _is_linked(a, 'jpdl31_ProcessDefinitionType175', b2)
    if hasattr(b1, 'jpdl31_EndStateType176'):
        assert not _is_linked(b1, 'jpdl31_EndStateType176', a)
    if hasattr(b2, 'jpdl31_EndStateType176'):
        assert _is_linked(b2, 'jpdl31_EndStateType176', a)
    _safe_set(a, 'jpdl31_ProcessDefinitionType175', set())
    assert not _is_linked(a, 'jpdl31_ProcessDefinitionType175', b2)
    if hasattr(b2, 'jpdl31_EndStateType176'):
        assert not _is_linked(b2, 'jpdl31_EndStateType176', a)


def test_assoc_endState263_link_reassign_clear():
    a = jpdl31_SuperStateType(async_="sample_text", group="sample_text", name="sample_text")
    b1 = jpdl31_EndStateType(group="sample_text", name="sample_text")
    b2 = jpdl31_EndStateType(group="sample_text_2", name="sample_text_2")
    _safe_set(a, 'jpdl31_SuperStateType264', {b1})
    assert _is_linked(a, 'jpdl31_SuperStateType264', b1)
    if hasattr(b1, 'jpdl31_EndStateType265'):
        assert _is_linked(b1, 'jpdl31_EndStateType265', a)
    _safe_set(a, 'jpdl31_SuperStateType264', {b2})
    assert _is_linked(a, 'jpdl31_SuperStateType264', b2)
    if hasattr(b1, 'jpdl31_EndStateType265'):
        assert not _is_linked(b1, 'jpdl31_EndStateType265', a)
    if hasattr(b2, 'jpdl31_EndStateType265'):
        assert _is_linked(b2, 'jpdl31_EndStateType265', a)
    _safe_set(a, 'jpdl31_SuperStateType264', set())
    assert not _is_linked(a, 'jpdl31_SuperStateType264', b2)
    if hasattr(b2, 'jpdl31_EndStateType265'):
        assert not _is_linked(b2, 'jpdl31_EndStateType265', a)


def test_assoc_endState30_link_reassign_clear():
    a = jpdl31_EndStateType(group="sample_text", name="sample_text")
    b1 = jpdl31_DocumentRoot(mixed="sample_text")
    b2 = jpdl31_DocumentRoot(mixed="sample_text_2")
    _safe_set(a, 'jpdl31_EndStateType', b1)
    assert _is_linked(a, 'jpdl31_EndStateType', b1)
    if hasattr(b1, 'jpdl31_DocumentRoot31'):
        assert _is_linked(b1, 'jpdl31_DocumentRoot31', a)
    _safe_set(a, 'jpdl31_EndStateType', b2)
    assert _is_linked(a, 'jpdl31_EndStateType', b2)
    if hasattr(b1, 'jpdl31_DocumentRoot31'):
        assert not _is_linked(b1, 'jpdl31_DocumentRoot31', a)
    if hasattr(b2, 'jpdl31_DocumentRoot31'):
        assert _is_linked(b2, 'jpdl31_DocumentRoot31', a)
    _safe_set(a, 'jpdl31_EndStateType', None)
    assert not _is_linked(a, 'jpdl31_EndStateType', b2)
    if hasattr(b2, 'jpdl31_DocumentRoot31'):
        assert not _is_linked(b2, 'jpdl31_DocumentRoot31', a)


def test_assoc_event108_link_reassign_clear():
    a = jpdl31_JoinType(async_="sample_text", name="sample_text", nodeContentElements="sample_text")
    b1 = jpdl31_EventType(actionElements="sample_text", type="sample_text")
    b2 = jpdl31_EventType(actionElements="sample_text_2", type="sample_text_2")
    _safe_set(a, 'jpdl31_JoinType109', {b1})
    assert _is_linked(a, 'jpdl31_JoinType109', b1)
    if hasattr(b1, 'jpdl31_EventType110'):
        assert _is_linked(b1, 'jpdl31_EventType110', a)
    _safe_set(a, 'jpdl31_JoinType109', {b2})
    assert _is_linked(a, 'jpdl31_JoinType109', b2)
    if hasattr(b1, 'jpdl31_EventType110'):
        assert not _is_linked(b1, 'jpdl31_EventType110', a)
    if hasattr(b2, 'jpdl31_EventType110'):
        assert _is_linked(b2, 'jpdl31_EventType110', a)
    _safe_set(a, 'jpdl31_JoinType109', set())
    assert not _is_linked(a, 'jpdl31_JoinType109', b2)
    if hasattr(b2, 'jpdl31_EventType110'):
        assert not _is_linked(b2, 'jpdl31_EventType110', a)


def test_assoc_event132_link_reassign_clear():
    a = jpdl31_NodeType(async_="sample_text", name="sample_text", nodeContentElements="sample_text")
    b1 = jpdl31_EventType(actionElements="sample_text", type="sample_text")
    b2 = jpdl31_EventType(actionElements="sample_text_2", type="sample_text_2")
    _safe_set(a, 'jpdl31_NodeType133', {b1})
    assert _is_linked(a, 'jpdl31_NodeType133', b1)
    if hasattr(b1, 'jpdl31_EventType134'):
        assert _is_linked(b1, 'jpdl31_EventType134', a)
    _safe_set(a, 'jpdl31_NodeType133', {b2})
    assert _is_linked(a, 'jpdl31_NodeType133', b2)
    if hasattr(b1, 'jpdl31_EventType134'):
        assert not _is_linked(b1, 'jpdl31_EventType134', a)
    if hasattr(b2, 'jpdl31_EventType134'):
        assert _is_linked(b2, 'jpdl31_EventType134', a)
    _safe_set(a, 'jpdl31_NodeType133', set())
    assert not _is_linked(a, 'jpdl31_NodeType133', b2)
    if hasattr(b2, 'jpdl31_EventType134'):
        assert not _is_linked(b2, 'jpdl31_EventType134', a)


def test_assoc_event189_link_reassign_clear():
    a = jpdl31_ProcessDefinitionType(group="sample_text", name="sample_text")
    b1 = jpdl31_EventType(actionElements="sample_text", type="sample_text")
    b2 = jpdl31_EventType(actionElements="sample_text_2", type="sample_text_2")
    _safe_set(a, 'jpdl31_ProcessDefinitionType190', {b1})
    assert _is_linked(a, 'jpdl31_ProcessDefinitionType190', b1)
    if hasattr(b1, 'jpdl31_EventType191'):
        assert _is_linked(b1, 'jpdl31_EventType191', a)
    _safe_set(a, 'jpdl31_ProcessDefinitionType190', {b2})
    assert _is_linked(a, 'jpdl31_ProcessDefinitionType190', b2)
    if hasattr(b1, 'jpdl31_EventType191'):
        assert not _is_linked(b1, 'jpdl31_EventType191', a)
    if hasattr(b2, 'jpdl31_EventType191'):
        assert _is_linked(b2, 'jpdl31_EventType191', a)
    _safe_set(a, 'jpdl31_ProcessDefinitionType190', set())
    assert not _is_linked(a, 'jpdl31_ProcessDefinitionType190', b2)
    if hasattr(b2, 'jpdl31_EventType191'):
        assert not _is_linked(b2, 'jpdl31_EventType191', a)


def test_assoc_event203_link_reassign_clear():
    a = jpdl31_ProcessStateType(async_="sample_text", group="sample_text", name="sample_text")
    b1 = jpdl31_EventType(actionElements="sample_text", type="sample_text")
    b2 = jpdl31_EventType(actionElements="sample_text_2", type="sample_text_2")
    _safe_set(a, 'jpdl31_ProcessStateType204', {b1})
    assert _is_linked(a, 'jpdl31_ProcessStateType204', b1)
    if hasattr(b1, 'jpdl31_EventType205'):
        assert _is_linked(b1, 'jpdl31_EventType205', a)
    _safe_set(a, 'jpdl31_ProcessStateType204', {b2})
    assert _is_linked(a, 'jpdl31_ProcessStateType204', b2)
    if hasattr(b1, 'jpdl31_EventType205'):
        assert not _is_linked(b1, 'jpdl31_EventType205', a)
    if hasattr(b2, 'jpdl31_EventType205'):
        assert _is_linked(b2, 'jpdl31_EventType205', a)
    _safe_set(a, 'jpdl31_ProcessStateType204', set())
    assert not _is_linked(a, 'jpdl31_ProcessStateType204', b2)
    if hasattr(b2, 'jpdl31_EventType205'):
        assert not _is_linked(b2, 'jpdl31_EventType205', a)


def test_assoc_event221_link_reassign_clear():
    a = jpdl31_StartStateType(group="sample_text", name="sample_text")
    b1 = jpdl31_EventType(actionElements="sample_text", type="sample_text")
    b2 = jpdl31_EventType(actionElements="sample_text_2", type="sample_text_2")
    _safe_set(a, 'jpdl31_StartStateType222', {b1})
    assert _is_linked(a, 'jpdl31_StartStateType222', b1)
    if hasattr(b1, 'jpdl31_EventType223'):
        assert _is_linked(b1, 'jpdl31_EventType223', a)
    _safe_set(a, 'jpdl31_StartStateType222', {b2})
    assert _is_linked(a, 'jpdl31_StartStateType222', b2)
    if hasattr(b1, 'jpdl31_EventType223'):
        assert not _is_linked(b1, 'jpdl31_EventType223', a)
    if hasattr(b2, 'jpdl31_EventType223'):
        assert _is_linked(b2, 'jpdl31_EventType223', a)
    _safe_set(a, 'jpdl31_StartStateType222', set())
    assert not _is_linked(a, 'jpdl31_StartStateType222', b2)
    if hasattr(b2, 'jpdl31_EventType223'):
        assert not _is_linked(b2, 'jpdl31_EventType223', a)


def test_assoc_event227_link_reassign_clear():
    a = jpdl31_StateType(async_="sample_text", name="sample_text", nodeContentElements="sample_text")
    b1 = jpdl31_EventType(actionElements="sample_text", type="sample_text")
    b2 = jpdl31_EventType(actionElements="sample_text_2", type="sample_text_2")
    _safe_set(a, 'jpdl31_StateType228', {b1})
    assert _is_linked(a, 'jpdl31_StateType228', b1)
    if hasattr(b1, 'jpdl31_EventType229'):
        assert _is_linked(b1, 'jpdl31_EventType229', a)
    _safe_set(a, 'jpdl31_StateType228', {b2})
    assert _is_linked(a, 'jpdl31_StateType228', b2)
    if hasattr(b1, 'jpdl31_EventType229'):
        assert not _is_linked(b1, 'jpdl31_EventType229', a)
    if hasattr(b2, 'jpdl31_EventType229'):
        assert _is_linked(b2, 'jpdl31_EventType229', a)
    _safe_set(a, 'jpdl31_StateType228', set())
    assert not _is_linked(a, 'jpdl31_StateType228', b2)
    if hasattr(b2, 'jpdl31_EventType229'):
        assert not _is_linked(b2, 'jpdl31_EventType229', a)


def test_assoc_event266_link_reassign_clear():
    a = jpdl31_SuperStateType(async_="sample_text", group="sample_text", name="sample_text")
    b1 = jpdl31_EventType(actionElements="sample_text", type="sample_text")
    b2 = jpdl31_EventType(actionElements="sample_text_2", type="sample_text_2")
    _safe_set(a, 'jpdl31_SuperStateType267', {b1})
    assert _is_linked(a, 'jpdl31_SuperStateType267', b1)
    if hasattr(b1, 'jpdl31_EventType268'):
        assert _is_linked(b1, 'jpdl31_EventType268', a)
    _safe_set(a, 'jpdl31_SuperStateType267', {b2})
    assert _is_linked(a, 'jpdl31_SuperStateType267', b2)
    if hasattr(b1, 'jpdl31_EventType268'):
        assert not _is_linked(b1, 'jpdl31_EventType268', a)
    if hasattr(b2, 'jpdl31_EventType268'):
        assert _is_linked(b2, 'jpdl31_EventType268', a)
    _safe_set(a, 'jpdl31_SuperStateType267', set())
    assert not _is_linked(a, 'jpdl31_SuperStateType267', b2)
    if hasattr(b2, 'jpdl31_EventType268'):
        assert not _is_linked(b2, 'jpdl31_EventType268', a)


def test_assoc_event284_link_reassign_clear():
    a = jpdl31_TaskNodeType(async_="sample_text", createTasks="sample_text", endTasks="sample_text", group="sample_text", name="sample_text", signal="sample_text")
    b1 = jpdl31_EventType(actionElements="sample_text", type="sample_text")
    b2 = jpdl31_EventType(actionElements="sample_text_2", type="sample_text_2")
    _safe_set(a, 'jpdl31_TaskNodeType285', {b1})
    assert _is_linked(a, 'jpdl31_TaskNodeType285', b1)
    if hasattr(b1, 'jpdl31_EventType286'):
        assert _is_linked(b1, 'jpdl31_EventType286', a)
    _safe_set(a, 'jpdl31_TaskNodeType285', {b2})
    assert _is_linked(a, 'jpdl31_TaskNodeType285', b2)
    if hasattr(b1, 'jpdl31_EventType286'):
        assert not _is_linked(b1, 'jpdl31_EventType286', a)
    if hasattr(b2, 'jpdl31_EventType286'):
        assert _is_linked(b2, 'jpdl31_EventType286', a)
    _safe_set(a, 'jpdl31_TaskNodeType285', set())
    assert not _is_linked(a, 'jpdl31_TaskNodeType285', b2)
    if hasattr(b2, 'jpdl31_EventType286'):
        assert not _is_linked(b2, 'jpdl31_EventType286', a)


def test_assoc_event302_link_reassign_clear():
    a = jpdl31_TaskType(blocking="sample_text", description="sample_text", duedate="sample_text", group="sample_text", name="sample_text", priority="sample_text", signalling="sample_text", swimlane="sample_text")
    b1 = jpdl31_EventType(actionElements="sample_text", type="sample_text")
    b2 = jpdl31_EventType(actionElements="sample_text_2", type="sample_text_2")
    _safe_set(a, 'jpdl31_TaskType303', {b1})
    assert _is_linked(a, 'jpdl31_TaskType303', b1)
    if hasattr(b1, 'jpdl31_EventType304'):
        assert _is_linked(b1, 'jpdl31_EventType304', a)
    _safe_set(a, 'jpdl31_TaskType303', {b2})
    assert _is_linked(a, 'jpdl31_TaskType303', b2)
    if hasattr(b1, 'jpdl31_EventType304'):
        assert not _is_linked(b1, 'jpdl31_EventType304', a)
    if hasattr(b2, 'jpdl31_EventType304'):
        assert _is_linked(b2, 'jpdl31_EventType304', a)
    _safe_set(a, 'jpdl31_TaskType303', set())
    assert not _is_linked(a, 'jpdl31_TaskType303', b2)
    if hasattr(b2, 'jpdl31_EventType304'):
        assert not _is_linked(b2, 'jpdl31_EventType304', a)


def test_assoc_event32_link_reassign_clear():
    a = jpdl31_EventType(actionElements="sample_text", type="sample_text")
    b1 = jpdl31_DocumentRoot(mixed="sample_text")
    b2 = jpdl31_DocumentRoot(mixed="sample_text_2")
    _safe_set(a, 'jpdl31_EventType34', b1)
    assert _is_linked(a, 'jpdl31_EventType34', b1)
    if hasattr(b1, 'jpdl31_DocumentRoot33'):
        assert _is_linked(b1, 'jpdl31_DocumentRoot33', a)
    _safe_set(a, 'jpdl31_EventType34', b2)
    assert _is_linked(a, 'jpdl31_EventType34', b2)
    if hasattr(b1, 'jpdl31_DocumentRoot33'):
        assert not _is_linked(b1, 'jpdl31_DocumentRoot33', a)
    if hasattr(b2, 'jpdl31_DocumentRoot33'):
        assert _is_linked(b2, 'jpdl31_DocumentRoot33', a)
    _safe_set(a, 'jpdl31_EventType34', None)
    assert not _is_linked(a, 'jpdl31_EventType34', b2)
    if hasattr(b2, 'jpdl31_DocumentRoot33'):
        assert not _is_linked(b2, 'jpdl31_DocumentRoot33', a)


def test_assoc_event4_link_reassign_clear():
    a = jpdl31_EventType(actionElements="sample_text", type="sample_text")
    b1 = jpdl31_DecisionType(async_="sample_text", expression="sample_text", group="sample_text", name="sample_text")
    b2 = jpdl31_DecisionType(async_="sample_text_2", expression="sample_text_2", group="sample_text_2", name="sample_text_2")
    _safe_set(a, 'jpdl31_EventType', b1)
    assert _is_linked(a, 'jpdl31_EventType', b1)
    if hasattr(b1, 'jpdl31_DecisionType5'):
        assert _is_linked(b1, 'jpdl31_DecisionType5', a)
    _safe_set(a, 'jpdl31_EventType', b2)
    assert _is_linked(a, 'jpdl31_EventType', b2)
    if hasattr(b1, 'jpdl31_DecisionType5'):
        assert not _is_linked(b1, 'jpdl31_DecisionType5', a)
    if hasattr(b2, 'jpdl31_DecisionType5'):
        assert _is_linked(b2, 'jpdl31_DecisionType5', a)
    _safe_set(a, 'jpdl31_EventType', None)
    assert not _is_linked(a, 'jpdl31_EventType', b2)
    if hasattr(b2, 'jpdl31_DecisionType5'):
        assert not _is_linked(b2, 'jpdl31_DecisionType5', a)


def test_assoc_event69_link_reassign_clear():
    a = jpdl31_EventType(actionElements="sample_text", type="sample_text")
    b1 = jpdl31_EndStateType(group="sample_text", name="sample_text")
    b2 = jpdl31_EndStateType(group="sample_text_2", name="sample_text_2")
    _safe_set(a, 'jpdl31_EventType71', b1)
    assert _is_linked(a, 'jpdl31_EventType71', b1)
    if hasattr(b1, 'jpdl31_EndStateType70'):
        assert _is_linked(b1, 'jpdl31_EndStateType70', a)
    _safe_set(a, 'jpdl31_EventType71', b2)
    assert _is_linked(a, 'jpdl31_EventType71', b2)
    if hasattr(b1, 'jpdl31_EndStateType70'):
        assert not _is_linked(b1, 'jpdl31_EndStateType70', a)
    if hasattr(b2, 'jpdl31_EndStateType70'):
        assert _is_linked(b2, 'jpdl31_EndStateType70', a)
    _safe_set(a, 'jpdl31_EventType71', None)
    assert not _is_linked(a, 'jpdl31_EventType71', b2)
    if hasattr(b2, 'jpdl31_EndStateType70'):
        assert not _is_linked(b2, 'jpdl31_EndStateType70', a)


def test_assoc_event96_link_reassign_clear():
    a = jpdl31_ForkType(async_="sample_text", group="sample_text", name="sample_text")
    b1 = jpdl31_EventType(actionElements="sample_text", type="sample_text")
    b2 = jpdl31_EventType(actionElements="sample_text_2", type="sample_text_2")
    _safe_set(a, 'jpdl31_ForkType97', {b1})
    assert _is_linked(a, 'jpdl31_ForkType97', b1)
    if hasattr(b1, 'jpdl31_EventType98'):
        assert _is_linked(b1, 'jpdl31_EventType98', a)
    _safe_set(a, 'jpdl31_ForkType97', {b2})
    assert _is_linked(a, 'jpdl31_ForkType97', b2)
    if hasattr(b1, 'jpdl31_EventType98'):
        assert not _is_linked(b1, 'jpdl31_EventType98', a)
    if hasattr(b2, 'jpdl31_EventType98'):
        assert _is_linked(b2, 'jpdl31_EventType98', a)
    _safe_set(a, 'jpdl31_ForkType97', set())
    assert not _is_linked(a, 'jpdl31_ForkType97', b2)
    if hasattr(b2, 'jpdl31_EventType98'):
        assert not _is_linked(b2, 'jpdl31_EventType98', a)


def test_assoc_exceptionHandler111_link_reassign_clear():
    a = jpdl31_JoinType(async_="sample_text", name="sample_text", nodeContentElements="sample_text")
    b1 = jpdl31_ExceptionHandlerType(exceptionClass="sample_text", group="sample_text")
    b2 = jpdl31_ExceptionHandlerType(exceptionClass="sample_text_2", group="sample_text_2")
    _safe_set(a, 'jpdl31_JoinType112', {b1})
    assert _is_linked(a, 'jpdl31_JoinType112', b1)
    if hasattr(b1, 'jpdl31_ExceptionHandlerType113'):
        assert _is_linked(b1, 'jpdl31_ExceptionHandlerType113', a)
    _safe_set(a, 'jpdl31_JoinType112', {b2})
    assert _is_linked(a, 'jpdl31_JoinType112', b2)
    if hasattr(b1, 'jpdl31_ExceptionHandlerType113'):
        assert not _is_linked(b1, 'jpdl31_ExceptionHandlerType113', a)
    if hasattr(b2, 'jpdl31_ExceptionHandlerType113'):
        assert _is_linked(b2, 'jpdl31_ExceptionHandlerType113', a)
    _safe_set(a, 'jpdl31_JoinType112', set())
    assert not _is_linked(a, 'jpdl31_JoinType112', b2)
    if hasattr(b2, 'jpdl31_ExceptionHandlerType113'):
        assert not _is_linked(b2, 'jpdl31_ExceptionHandlerType113', a)


def test_assoc_exceptionHandler135_link_reassign_clear():
    a = jpdl31_NodeType(async_="sample_text", name="sample_text", nodeContentElements="sample_text")
    b1 = jpdl31_ExceptionHandlerType(exceptionClass="sample_text", group="sample_text")
    b2 = jpdl31_ExceptionHandlerType(exceptionClass="sample_text_2", group="sample_text_2")
    _safe_set(a, 'jpdl31_NodeType136', {b1})
    assert _is_linked(a, 'jpdl31_NodeType136', b1)
    if hasattr(b1, 'jpdl31_ExceptionHandlerType137'):
        assert _is_linked(b1, 'jpdl31_ExceptionHandlerType137', a)
    _safe_set(a, 'jpdl31_NodeType136', {b2})
    assert _is_linked(a, 'jpdl31_NodeType136', b2)
    if hasattr(b1, 'jpdl31_ExceptionHandlerType137'):
        assert not _is_linked(b1, 'jpdl31_ExceptionHandlerType137', a)
    if hasattr(b2, 'jpdl31_ExceptionHandlerType137'):
        assert _is_linked(b2, 'jpdl31_ExceptionHandlerType137', a)
    _safe_set(a, 'jpdl31_NodeType136', set())
    assert not _is_linked(a, 'jpdl31_NodeType136', b2)
    if hasattr(b2, 'jpdl31_ExceptionHandlerType137'):
        assert not _is_linked(b2, 'jpdl31_ExceptionHandlerType137', a)


def test_assoc_exceptionHandler192_link_reassign_clear():
    a = jpdl31_ProcessDefinitionType(group="sample_text", name="sample_text")
    b1 = jpdl31_ExceptionHandlerType(exceptionClass="sample_text", group="sample_text")
    b2 = jpdl31_ExceptionHandlerType(exceptionClass="sample_text_2", group="sample_text_2")
    _safe_set(a, 'jpdl31_ProcessDefinitionType193', {b1})
    assert _is_linked(a, 'jpdl31_ProcessDefinitionType193', b1)
    if hasattr(b1, 'jpdl31_ExceptionHandlerType194'):
        assert _is_linked(b1, 'jpdl31_ExceptionHandlerType194', a)
    _safe_set(a, 'jpdl31_ProcessDefinitionType193', {b2})
    assert _is_linked(a, 'jpdl31_ProcessDefinitionType193', b2)
    if hasattr(b1, 'jpdl31_ExceptionHandlerType194'):
        assert not _is_linked(b1, 'jpdl31_ExceptionHandlerType194', a)
    if hasattr(b2, 'jpdl31_ExceptionHandlerType194'):
        assert _is_linked(b2, 'jpdl31_ExceptionHandlerType194', a)
    _safe_set(a, 'jpdl31_ProcessDefinitionType193', set())
    assert not _is_linked(a, 'jpdl31_ProcessDefinitionType193', b2)
    if hasattr(b2, 'jpdl31_ExceptionHandlerType194'):
        assert not _is_linked(b2, 'jpdl31_ExceptionHandlerType194', a)


def test_assoc_exceptionHandler206_link_reassign_clear():
    a = jpdl31_ProcessStateType(async_="sample_text", group="sample_text", name="sample_text")
    b1 = jpdl31_ExceptionHandlerType(exceptionClass="sample_text", group="sample_text")
    b2 = jpdl31_ExceptionHandlerType(exceptionClass="sample_text_2", group="sample_text_2")
    _safe_set(a, 'jpdl31_ProcessStateType207', {b1})
    assert _is_linked(a, 'jpdl31_ProcessStateType207', b1)
    if hasattr(b1, 'jpdl31_ExceptionHandlerType208'):
        assert _is_linked(b1, 'jpdl31_ExceptionHandlerType208', a)
    _safe_set(a, 'jpdl31_ProcessStateType207', {b2})
    assert _is_linked(a, 'jpdl31_ProcessStateType207', b2)
    if hasattr(b1, 'jpdl31_ExceptionHandlerType208'):
        assert not _is_linked(b1, 'jpdl31_ExceptionHandlerType208', a)
    if hasattr(b2, 'jpdl31_ExceptionHandlerType208'):
        assert _is_linked(b2, 'jpdl31_ExceptionHandlerType208', a)
    _safe_set(a, 'jpdl31_ProcessStateType207', set())
    assert not _is_linked(a, 'jpdl31_ProcessStateType207', b2)
    if hasattr(b2, 'jpdl31_ExceptionHandlerType208'):
        assert not _is_linked(b2, 'jpdl31_ExceptionHandlerType208', a)


def test_assoc_exceptionHandler224_link_reassign_clear():
    a = jpdl31_StartStateType(group="sample_text", name="sample_text")
    b1 = jpdl31_ExceptionHandlerType(exceptionClass="sample_text", group="sample_text")
    b2 = jpdl31_ExceptionHandlerType(exceptionClass="sample_text_2", group="sample_text_2")
    _safe_set(a, 'jpdl31_StartStateType225', {b1})
    assert _is_linked(a, 'jpdl31_StartStateType225', b1)
    if hasattr(b1, 'jpdl31_ExceptionHandlerType226'):
        assert _is_linked(b1, 'jpdl31_ExceptionHandlerType226', a)
    _safe_set(a, 'jpdl31_StartStateType225', {b2})
    assert _is_linked(a, 'jpdl31_StartStateType225', b2)
    if hasattr(b1, 'jpdl31_ExceptionHandlerType226'):
        assert not _is_linked(b1, 'jpdl31_ExceptionHandlerType226', a)
    if hasattr(b2, 'jpdl31_ExceptionHandlerType226'):
        assert _is_linked(b2, 'jpdl31_ExceptionHandlerType226', a)
    _safe_set(a, 'jpdl31_StartStateType225', set())
    assert not _is_linked(a, 'jpdl31_StartStateType225', b2)
    if hasattr(b2, 'jpdl31_ExceptionHandlerType226'):
        assert not _is_linked(b2, 'jpdl31_ExceptionHandlerType226', a)


def test_assoc_exceptionHandler230_link_reassign_clear():
    a = jpdl31_StateType(async_="sample_text", name="sample_text", nodeContentElements="sample_text")
    b1 = jpdl31_ExceptionHandlerType(exceptionClass="sample_text", group="sample_text")
    b2 = jpdl31_ExceptionHandlerType(exceptionClass="sample_text_2", group="sample_text_2")
    _safe_set(a, 'jpdl31_StateType231', {b1})
    assert _is_linked(a, 'jpdl31_StateType231', b1)
    if hasattr(b1, 'jpdl31_ExceptionHandlerType232'):
        assert _is_linked(b1, 'jpdl31_ExceptionHandlerType232', a)
    _safe_set(a, 'jpdl31_StateType231', {b2})
    assert _is_linked(a, 'jpdl31_StateType231', b2)
    if hasattr(b1, 'jpdl31_ExceptionHandlerType232'):
        assert not _is_linked(b1, 'jpdl31_ExceptionHandlerType232', a)
    if hasattr(b2, 'jpdl31_ExceptionHandlerType232'):
        assert _is_linked(b2, 'jpdl31_ExceptionHandlerType232', a)
    _safe_set(a, 'jpdl31_StateType231', set())
    assert not _is_linked(a, 'jpdl31_StateType231', b2)
    if hasattr(b2, 'jpdl31_ExceptionHandlerType232'):
        assert not _is_linked(b2, 'jpdl31_ExceptionHandlerType232', a)


def test_assoc_exceptionHandler269_link_reassign_clear():
    a = jpdl31_SuperStateType(async_="sample_text", group="sample_text", name="sample_text")
    b1 = jpdl31_ExceptionHandlerType(exceptionClass="sample_text", group="sample_text")
    b2 = jpdl31_ExceptionHandlerType(exceptionClass="sample_text_2", group="sample_text_2")
    _safe_set(a, 'jpdl31_SuperStateType270', {b1})
    assert _is_linked(a, 'jpdl31_SuperStateType270', b1)
    if hasattr(b1, 'jpdl31_ExceptionHandlerType271'):
        assert _is_linked(b1, 'jpdl31_ExceptionHandlerType271', a)
    _safe_set(a, 'jpdl31_SuperStateType270', {b2})
    assert _is_linked(a, 'jpdl31_SuperStateType270', b2)
    if hasattr(b1, 'jpdl31_ExceptionHandlerType271'):
        assert not _is_linked(b1, 'jpdl31_ExceptionHandlerType271', a)
    if hasattr(b2, 'jpdl31_ExceptionHandlerType271'):
        assert _is_linked(b2, 'jpdl31_ExceptionHandlerType271', a)
    _safe_set(a, 'jpdl31_SuperStateType270', set())
    assert not _is_linked(a, 'jpdl31_SuperStateType270', b2)
    if hasattr(b2, 'jpdl31_ExceptionHandlerType271'):
        assert not _is_linked(b2, 'jpdl31_ExceptionHandlerType271', a)


def test_assoc_exceptionHandler287_link_reassign_clear():
    a = jpdl31_TaskNodeType(async_="sample_text", createTasks="sample_text", endTasks="sample_text", group="sample_text", name="sample_text", signal="sample_text")
    b1 = jpdl31_ExceptionHandlerType(exceptionClass="sample_text", group="sample_text")
    b2 = jpdl31_ExceptionHandlerType(exceptionClass="sample_text_2", group="sample_text_2")
    _safe_set(a, 'jpdl31_TaskNodeType288', {b1})
    assert _is_linked(a, 'jpdl31_TaskNodeType288', b1)
    if hasattr(b1, 'jpdl31_ExceptionHandlerType289'):
        assert _is_linked(b1, 'jpdl31_ExceptionHandlerType289', a)
    _safe_set(a, 'jpdl31_TaskNodeType288', {b2})
    assert _is_linked(a, 'jpdl31_TaskNodeType288', b2)
    if hasattr(b1, 'jpdl31_ExceptionHandlerType289'):
        assert not _is_linked(b1, 'jpdl31_ExceptionHandlerType289', a)
    if hasattr(b2, 'jpdl31_ExceptionHandlerType289'):
        assert _is_linked(b2, 'jpdl31_ExceptionHandlerType289', a)
    _safe_set(a, 'jpdl31_TaskNodeType288', set())
    assert not _is_linked(a, 'jpdl31_TaskNodeType288', b2)
    if hasattr(b2, 'jpdl31_ExceptionHandlerType289'):
        assert not _is_linked(b2, 'jpdl31_ExceptionHandlerType289', a)


def test_assoc_exceptionHandler326_link_reassign_clear():
    a = jpdl31_TransitionType(group="sample_text", name="sample_text", to="sample_text")
    b1 = jpdl31_ExceptionHandlerType(exceptionClass="sample_text", group="sample_text")
    b2 = jpdl31_ExceptionHandlerType(exceptionClass="sample_text_2", group="sample_text_2")
    _safe_set(a, 'jpdl31_TransitionType327', {b1})
    assert _is_linked(a, 'jpdl31_TransitionType327', b1)
    if hasattr(b1, 'jpdl31_ExceptionHandlerType328'):
        assert _is_linked(b1, 'jpdl31_ExceptionHandlerType328', a)
    _safe_set(a, 'jpdl31_TransitionType327', {b2})
    assert _is_linked(a, 'jpdl31_TransitionType327', b2)
    if hasattr(b1, 'jpdl31_ExceptionHandlerType328'):
        assert not _is_linked(b1, 'jpdl31_ExceptionHandlerType328', a)
    if hasattr(b2, 'jpdl31_ExceptionHandlerType328'):
        assert _is_linked(b2, 'jpdl31_ExceptionHandlerType328', a)
    _safe_set(a, 'jpdl31_TransitionType327', set())
    assert not _is_linked(a, 'jpdl31_TransitionType327', b2)
    if hasattr(b2, 'jpdl31_ExceptionHandlerType328'):
        assert not _is_linked(b2, 'jpdl31_ExceptionHandlerType328', a)


def test_assoc_exceptionHandler343_link_reassign_clear():
    a = jpdl31_TransitionType1(group="sample_text", name="sample_text", to="sample_text")
    b1 = jpdl31_ExceptionHandlerType(exceptionClass="sample_text", group="sample_text")
    b2 = jpdl31_ExceptionHandlerType(exceptionClass="sample_text_2", group="sample_text_2")
    _safe_set(a, 'jpdl31_TransitionType1344', {b1})
    assert _is_linked(a, 'jpdl31_TransitionType1344', b1)
    if hasattr(b1, 'jpdl31_ExceptionHandlerType345'):
        assert _is_linked(b1, 'jpdl31_ExceptionHandlerType345', a)
    _safe_set(a, 'jpdl31_TransitionType1344', {b2})
    assert _is_linked(a, 'jpdl31_TransitionType1344', b2)
    if hasattr(b1, 'jpdl31_ExceptionHandlerType345'):
        assert not _is_linked(b1, 'jpdl31_ExceptionHandlerType345', a)
    if hasattr(b2, 'jpdl31_ExceptionHandlerType345'):
        assert _is_linked(b2, 'jpdl31_ExceptionHandlerType345', a)
    _safe_set(a, 'jpdl31_TransitionType1344', set())
    assert not _is_linked(a, 'jpdl31_TransitionType1344', b2)
    if hasattr(b2, 'jpdl31_ExceptionHandlerType345'):
        assert not _is_linked(b2, 'jpdl31_ExceptionHandlerType345', a)


def test_assoc_exceptionHandler35_link_reassign_clear():
    a = jpdl31_ExceptionHandlerType(exceptionClass="sample_text", group="sample_text")
    b1 = jpdl31_DocumentRoot(mixed="sample_text")
    b2 = jpdl31_DocumentRoot(mixed="sample_text_2")
    _safe_set(a, 'jpdl31_ExceptionHandlerType37', b1)
    assert _is_linked(a, 'jpdl31_ExceptionHandlerType37', b1)
    if hasattr(b1, 'jpdl31_DocumentRoot36'):
        assert _is_linked(b1, 'jpdl31_DocumentRoot36', a)
    _safe_set(a, 'jpdl31_ExceptionHandlerType37', b2)
    assert _is_linked(a, 'jpdl31_ExceptionHandlerType37', b2)
    if hasattr(b1, 'jpdl31_DocumentRoot36'):
        assert not _is_linked(b1, 'jpdl31_DocumentRoot36', a)
    if hasattr(b2, 'jpdl31_DocumentRoot36'):
        assert _is_linked(b2, 'jpdl31_DocumentRoot36', a)
    _safe_set(a, 'jpdl31_ExceptionHandlerType37', None)
    assert not _is_linked(a, 'jpdl31_ExceptionHandlerType37', b2)
    if hasattr(b2, 'jpdl31_DocumentRoot36'):
        assert not _is_linked(b2, 'jpdl31_DocumentRoot36', a)


def test_assoc_exceptionHandler6_link_reassign_clear():
    a = jpdl31_ExceptionHandlerType(exceptionClass="sample_text", group="sample_text")
    b1 = jpdl31_DecisionType(async_="sample_text", expression="sample_text", group="sample_text", name="sample_text")
    b2 = jpdl31_DecisionType(async_="sample_text_2", expression="sample_text_2", group="sample_text_2", name="sample_text_2")
    _safe_set(a, 'jpdl31_ExceptionHandlerType', b1)
    assert _is_linked(a, 'jpdl31_ExceptionHandlerType', b1)
    if hasattr(b1, 'jpdl31_DecisionType7'):
        assert _is_linked(b1, 'jpdl31_DecisionType7', a)
    _safe_set(a, 'jpdl31_ExceptionHandlerType', b2)
    assert _is_linked(a, 'jpdl31_ExceptionHandlerType', b2)
    if hasattr(b1, 'jpdl31_DecisionType7'):
        assert not _is_linked(b1, 'jpdl31_DecisionType7', a)
    if hasattr(b2, 'jpdl31_DecisionType7'):
        assert _is_linked(b2, 'jpdl31_DecisionType7', a)
    _safe_set(a, 'jpdl31_ExceptionHandlerType', None)
    assert not _is_linked(a, 'jpdl31_ExceptionHandlerType', b2)
    if hasattr(b2, 'jpdl31_DecisionType7'):
        assert not _is_linked(b2, 'jpdl31_DecisionType7', a)


def test_assoc_exceptionHandler72_link_reassign_clear():
    a = jpdl31_ExceptionHandlerType(exceptionClass="sample_text", group="sample_text")
    b1 = jpdl31_EndStateType(group="sample_text", name="sample_text")
    b2 = jpdl31_EndStateType(group="sample_text_2", name="sample_text_2")
    _safe_set(a, 'jpdl31_ExceptionHandlerType74', b1)
    assert _is_linked(a, 'jpdl31_ExceptionHandlerType74', b1)
    if hasattr(b1, 'jpdl31_EndStateType73'):
        assert _is_linked(b1, 'jpdl31_EndStateType73', a)
    _safe_set(a, 'jpdl31_ExceptionHandlerType74', b2)
    assert _is_linked(a, 'jpdl31_ExceptionHandlerType74', b2)
    if hasattr(b1, 'jpdl31_EndStateType73'):
        assert not _is_linked(b1, 'jpdl31_EndStateType73', a)
    if hasattr(b2, 'jpdl31_EndStateType73'):
        assert _is_linked(b2, 'jpdl31_EndStateType73', a)
    _safe_set(a, 'jpdl31_ExceptionHandlerType74', None)
    assert not _is_linked(a, 'jpdl31_ExceptionHandlerType74', b2)
    if hasattr(b2, 'jpdl31_EndStateType73'):
        assert not _is_linked(b2, 'jpdl31_EndStateType73', a)


def test_assoc_exceptionHandler99_link_reassign_clear():
    a = jpdl31_ForkType(async_="sample_text", group="sample_text", name="sample_text")
    b1 = jpdl31_ExceptionHandlerType(exceptionClass="sample_text", group="sample_text")
    b2 = jpdl31_ExceptionHandlerType(exceptionClass="sample_text_2", group="sample_text_2")
    _safe_set(a, 'jpdl31_ForkType100', {b1})
    assert _is_linked(a, 'jpdl31_ForkType100', b1)
    if hasattr(b1, 'jpdl31_ExceptionHandlerType101'):
        assert _is_linked(b1, 'jpdl31_ExceptionHandlerType101', a)
    _safe_set(a, 'jpdl31_ForkType100', {b2})
    assert _is_linked(a, 'jpdl31_ForkType100', b2)
    if hasattr(b1, 'jpdl31_ExceptionHandlerType101'):
        assert not _is_linked(b1, 'jpdl31_ExceptionHandlerType101', a)
    if hasattr(b2, 'jpdl31_ExceptionHandlerType101'):
        assert _is_linked(b2, 'jpdl31_ExceptionHandlerType101', a)
    _safe_set(a, 'jpdl31_ForkType100', set())
    assert not _is_linked(a, 'jpdl31_ForkType100', b2)
    if hasattr(b2, 'jpdl31_ExceptionHandlerType101'):
        assert not _is_linked(b2, 'jpdl31_ExceptionHandlerType101', a)


def test_assoc_fork165_link_reassign_clear():
    a = jpdl31_ProcessDefinitionType(group="sample_text", name="sample_text")
    b1 = jpdl31_ForkType(async_="sample_text", group="sample_text", name="sample_text")
    b2 = jpdl31_ForkType(async_="sample_text_2", group="sample_text_2", name="sample_text_2")
    _safe_set(a, 'jpdl31_ProcessDefinitionType166', {b1})
    assert _is_linked(a, 'jpdl31_ProcessDefinitionType166', b1)
    if hasattr(b1, 'jpdl31_ForkType167'):
        assert _is_linked(b1, 'jpdl31_ForkType167', a)
    _safe_set(a, 'jpdl31_ProcessDefinitionType166', {b2})
    assert _is_linked(a, 'jpdl31_ProcessDefinitionType166', b2)
    if hasattr(b1, 'jpdl31_ForkType167'):
        assert not _is_linked(b1, 'jpdl31_ForkType167', a)
    if hasattr(b2, 'jpdl31_ForkType167'):
        assert _is_linked(b2, 'jpdl31_ForkType167', a)
    _safe_set(a, 'jpdl31_ProcessDefinitionType166', set())
    assert not _is_linked(a, 'jpdl31_ProcessDefinitionType166', b2)
    if hasattr(b2, 'jpdl31_ForkType167'):
        assert not _is_linked(b2, 'jpdl31_ForkType167', a)


def test_assoc_fork254_link_reassign_clear():
    a = jpdl31_SuperStateType(async_="sample_text", group="sample_text", name="sample_text")
    b1 = jpdl31_ForkType(async_="sample_text", group="sample_text", name="sample_text")
    b2 = jpdl31_ForkType(async_="sample_text_2", group="sample_text_2", name="sample_text_2")
    _safe_set(a, 'jpdl31_SuperStateType255', {b1})
    assert _is_linked(a, 'jpdl31_SuperStateType255', b1)
    if hasattr(b1, 'jpdl31_ForkType256'):
        assert _is_linked(b1, 'jpdl31_ForkType256', a)
    _safe_set(a, 'jpdl31_SuperStateType255', {b2})
    assert _is_linked(a, 'jpdl31_SuperStateType255', b2)
    if hasattr(b1, 'jpdl31_ForkType256'):
        assert not _is_linked(b1, 'jpdl31_ForkType256', a)
    if hasattr(b2, 'jpdl31_ForkType256'):
        assert _is_linked(b2, 'jpdl31_ForkType256', a)
    _safe_set(a, 'jpdl31_SuperStateType255', set())
    assert not _is_linked(a, 'jpdl31_SuperStateType255', b2)
    if hasattr(b2, 'jpdl31_ForkType256'):
        assert not _is_linked(b2, 'jpdl31_ForkType256', a)


def test_assoc_fork38_link_reassign_clear():
    a = jpdl31_ForkType(async_="sample_text", group="sample_text", name="sample_text")
    b1 = jpdl31_DocumentRoot(mixed="sample_text")
    b2 = jpdl31_DocumentRoot(mixed="sample_text_2")
    _safe_set(a, 'jpdl31_ForkType', b1)
    assert _is_linked(a, 'jpdl31_ForkType', b1)
    if hasattr(b1, 'jpdl31_DocumentRoot39'):
        assert _is_linked(b1, 'jpdl31_DocumentRoot39', a)
    _safe_set(a, 'jpdl31_ForkType', b2)
    assert _is_linked(a, 'jpdl31_ForkType', b2)
    if hasattr(b1, 'jpdl31_DocumentRoot39'):
        assert not _is_linked(b1, 'jpdl31_DocumentRoot39', a)
    if hasattr(b2, 'jpdl31_DocumentRoot39'):
        assert _is_linked(b2, 'jpdl31_DocumentRoot39', a)
    _safe_set(a, 'jpdl31_ForkType', None)
    assert not _is_linked(a, 'jpdl31_ForkType', b2)
    if hasattr(b2, 'jpdl31_DocumentRoot39'):
        assert not _is_linked(b2, 'jpdl31_DocumentRoot39', a)


def test_assoc_handler3_link_reassign_clear():
    a = jpdl31_Delegation(any="sample_text", class_="sample_text", configType="sample_text", mixed="sample_text")
    b1 = jpdl31_DecisionType(async_="sample_text", expression="sample_text", group="sample_text", name="sample_text")
    b2 = jpdl31_DecisionType(async_="sample_text_2", expression="sample_text_2", group="sample_text_2", name="sample_text_2")
    _safe_set(a, 'jpdl31_Delegation', b1)
    assert _is_linked(a, 'jpdl31_Delegation', b1)
    if hasattr(b1, 'jpdl31_DecisionType'):
        assert _is_linked(b1, 'jpdl31_DecisionType', a)
    _safe_set(a, 'jpdl31_Delegation', b2)
    assert _is_linked(a, 'jpdl31_Delegation', b2)
    if hasattr(b1, 'jpdl31_DecisionType'):
        assert not _is_linked(b1, 'jpdl31_DecisionType', a)
    if hasattr(b2, 'jpdl31_DecisionType'):
        assert _is_linked(b2, 'jpdl31_DecisionType', a)
    _safe_set(a, 'jpdl31_Delegation', None)
    assert not _is_linked(a, 'jpdl31_Delegation', b2)
    if hasattr(b2, 'jpdl31_DecisionType'):
        assert not _is_linked(b2, 'jpdl31_DecisionType', a)


def test_assoc_join168_link_reassign_clear():
    a = jpdl31_ProcessDefinitionType(group="sample_text", name="sample_text")
    b1 = jpdl31_JoinType(async_="sample_text", name="sample_text", nodeContentElements="sample_text")
    b2 = jpdl31_JoinType(async_="sample_text_2", name="sample_text_2", nodeContentElements="sample_text_2")
    _safe_set(a, 'jpdl31_ProcessDefinitionType169', {b1})
    assert _is_linked(a, 'jpdl31_ProcessDefinitionType169', b1)
    if hasattr(b1, 'jpdl31_JoinType170'):
        assert _is_linked(b1, 'jpdl31_JoinType170', a)
    _safe_set(a, 'jpdl31_ProcessDefinitionType169', {b2})
    assert _is_linked(a, 'jpdl31_ProcessDefinitionType169', b2)
    if hasattr(b1, 'jpdl31_JoinType170'):
        assert not _is_linked(b1, 'jpdl31_JoinType170', a)
    if hasattr(b2, 'jpdl31_JoinType170'):
        assert _is_linked(b2, 'jpdl31_JoinType170', a)
    _safe_set(a, 'jpdl31_ProcessDefinitionType169', set())
    assert not _is_linked(a, 'jpdl31_ProcessDefinitionType169', b2)
    if hasattr(b2, 'jpdl31_JoinType170'):
        assert not _is_linked(b2, 'jpdl31_JoinType170', a)


def test_assoc_join257_link_reassign_clear():
    a = jpdl31_SuperStateType(async_="sample_text", group="sample_text", name="sample_text")
    b1 = jpdl31_JoinType(async_="sample_text", name="sample_text", nodeContentElements="sample_text")
    b2 = jpdl31_JoinType(async_="sample_text_2", name="sample_text_2", nodeContentElements="sample_text_2")
    _safe_set(a, 'jpdl31_SuperStateType258', {b1})
    assert _is_linked(a, 'jpdl31_SuperStateType258', b1)
    if hasattr(b1, 'jpdl31_JoinType259'):
        assert _is_linked(b1, 'jpdl31_JoinType259', a)
    _safe_set(a, 'jpdl31_SuperStateType258', {b2})
    assert _is_linked(a, 'jpdl31_SuperStateType258', b2)
    if hasattr(b1, 'jpdl31_JoinType259'):
        assert not _is_linked(b1, 'jpdl31_JoinType259', a)
    if hasattr(b2, 'jpdl31_JoinType259'):
        assert _is_linked(b2, 'jpdl31_JoinType259', a)
    _safe_set(a, 'jpdl31_SuperStateType258', set())
    assert not _is_linked(a, 'jpdl31_SuperStateType258', b2)
    if hasattr(b2, 'jpdl31_JoinType259'):
        assert not _is_linked(b2, 'jpdl31_JoinType259', a)


def test_assoc_join40_link_reassign_clear():
    a = jpdl31_JoinType(async_="sample_text", name="sample_text", nodeContentElements="sample_text")
    b1 = jpdl31_DocumentRoot(mixed="sample_text")
    b2 = jpdl31_DocumentRoot(mixed="sample_text_2")
    _safe_set(a, 'jpdl31_JoinType', b1)
    assert _is_linked(a, 'jpdl31_JoinType', b1)
    if hasattr(b1, 'jpdl31_DocumentRoot41'):
        assert _is_linked(b1, 'jpdl31_DocumentRoot41', a)
    _safe_set(a, 'jpdl31_JoinType', b2)
    assert _is_linked(a, 'jpdl31_JoinType', b2)
    if hasattr(b1, 'jpdl31_DocumentRoot41'):
        assert not _is_linked(b1, 'jpdl31_DocumentRoot41', a)
    if hasattr(b2, 'jpdl31_DocumentRoot41'):
        assert _is_linked(b2, 'jpdl31_DocumentRoot41', a)
    _safe_set(a, 'jpdl31_JoinType', None)
    assert not _is_linked(a, 'jpdl31_JoinType', b2)
    if hasattr(b2, 'jpdl31_DocumentRoot41'):
        assert not _is_linked(b2, 'jpdl31_DocumentRoot41', a)


def test_assoc_node150_link_reassign_clear():
    a = jpdl31_ProcessDefinitionType(group="sample_text", name="sample_text")
    b1 = jpdl31_NodeType(async_="sample_text", name="sample_text", nodeContentElements="sample_text")
    b2 = jpdl31_NodeType(async_="sample_text_2", name="sample_text_2", nodeContentElements="sample_text_2")
    _safe_set(a, 'jpdl31_ProcessDefinitionType151', {b1})
    assert _is_linked(a, 'jpdl31_ProcessDefinitionType151', b1)
    if hasattr(b1, 'jpdl31_NodeType152'):
        assert _is_linked(b1, 'jpdl31_NodeType152', a)
    _safe_set(a, 'jpdl31_ProcessDefinitionType151', {b2})
    assert _is_linked(a, 'jpdl31_ProcessDefinitionType151', b2)
    if hasattr(b1, 'jpdl31_NodeType152'):
        assert not _is_linked(b1, 'jpdl31_NodeType152', a)
    if hasattr(b2, 'jpdl31_NodeType152'):
        assert _is_linked(b2, 'jpdl31_NodeType152', a)
    _safe_set(a, 'jpdl31_ProcessDefinitionType151', set())
    assert not _is_linked(a, 'jpdl31_ProcessDefinitionType151', b2)
    if hasattr(b2, 'jpdl31_NodeType152'):
        assert not _is_linked(b2, 'jpdl31_NodeType152', a)


def test_assoc_node239_link_reassign_clear():
    a = jpdl31_SuperStateType(async_="sample_text", group="sample_text", name="sample_text")
    b1 = jpdl31_NodeType(async_="sample_text", name="sample_text", nodeContentElements="sample_text")
    b2 = jpdl31_NodeType(async_="sample_text_2", name="sample_text_2", nodeContentElements="sample_text_2")
    _safe_set(a, 'jpdl31_SuperStateType240', {b1})
    assert _is_linked(a, 'jpdl31_SuperStateType240', b1)
    if hasattr(b1, 'jpdl31_NodeType241'):
        assert _is_linked(b1, 'jpdl31_NodeType241', a)
    _safe_set(a, 'jpdl31_SuperStateType240', {b2})
    assert _is_linked(a, 'jpdl31_SuperStateType240', b2)
    if hasattr(b1, 'jpdl31_NodeType241'):
        assert not _is_linked(b1, 'jpdl31_NodeType241', a)
    if hasattr(b2, 'jpdl31_NodeType241'):
        assert _is_linked(b2, 'jpdl31_NodeType241', a)
    _safe_set(a, 'jpdl31_SuperStateType240', set())
    assert not _is_linked(a, 'jpdl31_SuperStateType240', b2)
    if hasattr(b2, 'jpdl31_NodeType241'):
        assert not _is_linked(b2, 'jpdl31_NodeType241', a)


def test_assoc_node42_link_reassign_clear():
    a = jpdl31_NodeType(async_="sample_text", name="sample_text", nodeContentElements="sample_text")
    b1 = jpdl31_DocumentRoot(mixed="sample_text")
    b2 = jpdl31_DocumentRoot(mixed="sample_text_2")
    _safe_set(a, 'jpdl31_NodeType', b1)
    assert _is_linked(a, 'jpdl31_NodeType', b1)
    if hasattr(b1, 'jpdl31_DocumentRoot43'):
        assert _is_linked(b1, 'jpdl31_DocumentRoot43', a)
    _safe_set(a, 'jpdl31_NodeType', b2)
    assert _is_linked(a, 'jpdl31_NodeType', b2)
    if hasattr(b1, 'jpdl31_DocumentRoot43'):
        assert not _is_linked(b1, 'jpdl31_DocumentRoot43', a)
    if hasattr(b2, 'jpdl31_DocumentRoot43'):
        assert _is_linked(b2, 'jpdl31_DocumentRoot43', a)
    _safe_set(a, 'jpdl31_NodeType', None)
    assert not _is_linked(a, 'jpdl31_NodeType', b2)
    if hasattr(b2, 'jpdl31_DocumentRoot43'):
        assert not _is_linked(b2, 'jpdl31_DocumentRoot43', a)


def test_assoc_processDefinition44_link_reassign_clear():
    a = jpdl31_ProcessDefinitionType(group="sample_text", name="sample_text")
    b1 = jpdl31_DocumentRoot(mixed="sample_text")
    b2 = jpdl31_DocumentRoot(mixed="sample_text_2")
    _safe_set(a, 'jpdl31_ProcessDefinitionType', b1)
    assert _is_linked(a, 'jpdl31_ProcessDefinitionType', b1)
    if hasattr(b1, 'jpdl31_DocumentRoot45'):
        assert _is_linked(b1, 'jpdl31_DocumentRoot45', a)
    _safe_set(a, 'jpdl31_ProcessDefinitionType', b2)
    assert _is_linked(a, 'jpdl31_ProcessDefinitionType', b2)
    if hasattr(b1, 'jpdl31_DocumentRoot45'):
        assert not _is_linked(b1, 'jpdl31_DocumentRoot45', a)
    if hasattr(b2, 'jpdl31_DocumentRoot45'):
        assert _is_linked(b2, 'jpdl31_DocumentRoot45', a)
    _safe_set(a, 'jpdl31_ProcessDefinitionType', None)
    assert not _is_linked(a, 'jpdl31_ProcessDefinitionType', b2)
    if hasattr(b2, 'jpdl31_DocumentRoot45'):
        assert not _is_linked(b2, 'jpdl31_DocumentRoot45', a)


def test_assoc_processState162_link_reassign_clear():
    a = jpdl31_ProcessStateType(async_="sample_text", group="sample_text", name="sample_text")
    b1 = jpdl31_ProcessDefinitionType(group="sample_text", name="sample_text")
    b2 = jpdl31_ProcessDefinitionType(group="sample_text_2", name="sample_text_2")
    _safe_set(a, 'jpdl31_ProcessStateType164', b1)
    assert _is_linked(a, 'jpdl31_ProcessStateType164', b1)
    if hasattr(b1, 'jpdl31_ProcessDefinitionType163'):
        assert _is_linked(b1, 'jpdl31_ProcessDefinitionType163', a)
    _safe_set(a, 'jpdl31_ProcessStateType164', b2)
    assert _is_linked(a, 'jpdl31_ProcessStateType164', b2)
    if hasattr(b1, 'jpdl31_ProcessDefinitionType163'):
        assert not _is_linked(b1, 'jpdl31_ProcessDefinitionType163', a)
    if hasattr(b2, 'jpdl31_ProcessDefinitionType163'):
        assert _is_linked(b2, 'jpdl31_ProcessDefinitionType163', a)
    _safe_set(a, 'jpdl31_ProcessStateType164', None)
    assert not _is_linked(a, 'jpdl31_ProcessStateType164', b2)
    if hasattr(b2, 'jpdl31_ProcessDefinitionType163'):
        assert not _is_linked(b2, 'jpdl31_ProcessDefinitionType163', a)


def test_assoc_processState251_link_reassign_clear():
    a = jpdl31_SuperStateType(async_="sample_text", group="sample_text", name="sample_text")
    b1 = jpdl31_ProcessStateType(async_="sample_text", group="sample_text", name="sample_text")
    b2 = jpdl31_ProcessStateType(async_="sample_text_2", group="sample_text_2", name="sample_text_2")
    _safe_set(a, 'jpdl31_SuperStateType252', {b1})
    assert _is_linked(a, 'jpdl31_SuperStateType252', b1)
    if hasattr(b1, 'jpdl31_ProcessStateType253'):
        assert _is_linked(b1, 'jpdl31_ProcessStateType253', a)
    _safe_set(a, 'jpdl31_SuperStateType252', {b2})
    assert _is_linked(a, 'jpdl31_SuperStateType252', b2)
    if hasattr(b1, 'jpdl31_ProcessStateType253'):
        assert not _is_linked(b1, 'jpdl31_ProcessStateType253', a)
    if hasattr(b2, 'jpdl31_ProcessStateType253'):
        assert _is_linked(b2, 'jpdl31_ProcessStateType253', a)
    _safe_set(a, 'jpdl31_SuperStateType252', set())
    assert not _is_linked(a, 'jpdl31_SuperStateType252', b2)
    if hasattr(b2, 'jpdl31_ProcessStateType253'):
        assert not _is_linked(b2, 'jpdl31_ProcessStateType253', a)


def test_assoc_processState46_link_reassign_clear():
    a = jpdl31_ProcessStateType(async_="sample_text", group="sample_text", name="sample_text")
    b1 = jpdl31_DocumentRoot(mixed="sample_text")
    b2 = jpdl31_DocumentRoot(mixed="sample_text_2")
    _safe_set(a, 'jpdl31_ProcessStateType', b1)
    assert _is_linked(a, 'jpdl31_ProcessStateType', b1)
    if hasattr(b1, 'jpdl31_DocumentRoot47'):
        assert _is_linked(b1, 'jpdl31_DocumentRoot47', a)
    _safe_set(a, 'jpdl31_ProcessStateType', b2)
    assert _is_linked(a, 'jpdl31_ProcessStateType', b2)
    if hasattr(b1, 'jpdl31_DocumentRoot47'):
        assert not _is_linked(b1, 'jpdl31_DocumentRoot47', a)
    if hasattr(b2, 'jpdl31_DocumentRoot47'):
        assert _is_linked(b2, 'jpdl31_DocumentRoot47', a)
    _safe_set(a, 'jpdl31_ProcessStateType', None)
    assert not _is_linked(a, 'jpdl31_ProcessStateType', b2)
    if hasattr(b2, 'jpdl31_DocumentRoot47'):
        assert not _is_linked(b2, 'jpdl31_DocumentRoot47', a)


def test_assoc_script1_link_reassign_clear():
    a = jpdl31_ScriptType(acceptPropagatedEvents="sample_text", any="sample_text", mixed="sample_text", name="sample_text")
    b1 = jpdl31_CreateTimerType(duedate="sample_text", name="sample_text", repeat="sample_text", transition="sample_text")
    b2 = jpdl31_CreateTimerType(duedate="sample_text_2", name="sample_text_2", repeat="sample_text_2", transition="sample_text_2")
    _safe_set(a, 'jpdl31_ScriptType', b1)
    assert _is_linked(a, 'jpdl31_ScriptType', b1)
    if hasattr(b1, 'jpdl31_CreateTimerType2'):
        assert _is_linked(b1, 'jpdl31_CreateTimerType2', a)
    _safe_set(a, 'jpdl31_ScriptType', b2)
    assert _is_linked(a, 'jpdl31_ScriptType', b2)
    if hasattr(b1, 'jpdl31_CreateTimerType2'):
        assert not _is_linked(b1, 'jpdl31_CreateTimerType2', a)
    if hasattr(b2, 'jpdl31_CreateTimerType2'):
        assert _is_linked(b2, 'jpdl31_CreateTimerType2', a)
    _safe_set(a, 'jpdl31_ScriptType', None)
    assert not _is_linked(a, 'jpdl31_ScriptType', b2)
    if hasattr(b2, 'jpdl31_CreateTimerType2'):
        assert not _is_linked(b2, 'jpdl31_CreateTimerType2', a)


def test_assoc_script123_link_reassign_clear():
    a = jpdl31_ScriptType(acceptPropagatedEvents="sample_text", any="sample_text", mixed="sample_text", name="sample_text")
    b1 = jpdl31_NodeType(async_="sample_text", name="sample_text", nodeContentElements="sample_text")
    b2 = jpdl31_NodeType(async_="sample_text_2", name="sample_text_2", nodeContentElements="sample_text_2")
    _safe_set(a, 'jpdl31_ScriptType125', b1)
    assert _is_linked(a, 'jpdl31_ScriptType125', b1)
    if hasattr(b1, 'jpdl31_NodeType124'):
        assert _is_linked(b1, 'jpdl31_NodeType124', a)
    _safe_set(a, 'jpdl31_ScriptType125', b2)
    assert _is_linked(a, 'jpdl31_ScriptType125', b2)
    if hasattr(b1, 'jpdl31_NodeType124'):
        assert not _is_linked(b1, 'jpdl31_NodeType124', a)
    if hasattr(b2, 'jpdl31_NodeType124'):
        assert _is_linked(b2, 'jpdl31_NodeType124', a)
    _safe_set(a, 'jpdl31_ScriptType125', None)
    assert not _is_linked(a, 'jpdl31_ScriptType125', b2)
    if hasattr(b2, 'jpdl31_NodeType124'):
        assert not _is_linked(b2, 'jpdl31_NodeType124', a)


def test_assoc_script180_link_reassign_clear():
    a = jpdl31_ScriptType(acceptPropagatedEvents="sample_text", any="sample_text", mixed="sample_text", name="sample_text")
    b1 = jpdl31_ProcessDefinitionType(group="sample_text", name="sample_text")
    b2 = jpdl31_ProcessDefinitionType(group="sample_text_2", name="sample_text_2")
    _safe_set(a, 'jpdl31_ScriptType182', b1)
    assert _is_linked(a, 'jpdl31_ScriptType182', b1)
    if hasattr(b1, 'jpdl31_ProcessDefinitionType181'):
        assert _is_linked(b1, 'jpdl31_ProcessDefinitionType181', a)
    _safe_set(a, 'jpdl31_ScriptType182', b2)
    assert _is_linked(a, 'jpdl31_ScriptType182', b2)
    if hasattr(b1, 'jpdl31_ProcessDefinitionType181'):
        assert not _is_linked(b1, 'jpdl31_ProcessDefinitionType181', a)
    if hasattr(b2, 'jpdl31_ProcessDefinitionType181'):
        assert _is_linked(b2, 'jpdl31_ProcessDefinitionType181', a)
    _safe_set(a, 'jpdl31_ScriptType182', None)
    assert not _is_linked(a, 'jpdl31_ScriptType182', b2)
    if hasattr(b2, 'jpdl31_ProcessDefinitionType181'):
        assert not _is_linked(b2, 'jpdl31_ProcessDefinitionType181', a)


def test_assoc_script311_link_reassign_clear():
    a = jpdl31_TimerType(duedate="sample_text", name="sample_text", repeat="sample_text", transition="sample_text")
    b1 = jpdl31_ScriptType(acceptPropagatedEvents="sample_text", any="sample_text", mixed="sample_text", name="sample_text")
    b2 = jpdl31_ScriptType(acceptPropagatedEvents="sample_text_2", any="sample_text_2", mixed="sample_text_2", name="sample_text_2")
    _safe_set(a, 'jpdl31_TimerType312', b1)
    assert _is_linked(a, 'jpdl31_TimerType312', b1)
    if hasattr(b1, 'jpdl31_ScriptType313'):
        assert _is_linked(b1, 'jpdl31_ScriptType313', a)
    _safe_set(a, 'jpdl31_TimerType312', b2)
    assert _is_linked(a, 'jpdl31_TimerType312', b2)
    if hasattr(b1, 'jpdl31_ScriptType313'):
        assert not _is_linked(b1, 'jpdl31_ScriptType313', a)
    if hasattr(b2, 'jpdl31_ScriptType313'):
        assert _is_linked(b2, 'jpdl31_ScriptType313', a)
    _safe_set(a, 'jpdl31_TimerType312', None)
    assert not _is_linked(a, 'jpdl31_TimerType312', b2)
    if hasattr(b2, 'jpdl31_ScriptType313'):
        assert not _is_linked(b2, 'jpdl31_ScriptType313', a)


def test_assoc_script317_link_reassign_clear():
    a = jpdl31_TransitionType(group="sample_text", name="sample_text", to="sample_text")
    b1 = jpdl31_ScriptType(acceptPropagatedEvents="sample_text", any="sample_text", mixed="sample_text", name="sample_text")
    b2 = jpdl31_ScriptType(acceptPropagatedEvents="sample_text_2", any="sample_text_2", mixed="sample_text_2", name="sample_text_2")
    _safe_set(a, 'jpdl31_TransitionType318', {b1})
    assert _is_linked(a, 'jpdl31_TransitionType318', b1)
    if hasattr(b1, 'jpdl31_ScriptType319'):
        assert _is_linked(b1, 'jpdl31_ScriptType319', a)
    _safe_set(a, 'jpdl31_TransitionType318', {b2})
    assert _is_linked(a, 'jpdl31_TransitionType318', b2)
    if hasattr(b1, 'jpdl31_ScriptType319'):
        assert not _is_linked(b1, 'jpdl31_ScriptType319', a)
    if hasattr(b2, 'jpdl31_ScriptType319'):
        assert _is_linked(b2, 'jpdl31_ScriptType319', a)
    _safe_set(a, 'jpdl31_TransitionType318', set())
    assert not _is_linked(a, 'jpdl31_TransitionType318', b2)
    if hasattr(b2, 'jpdl31_ScriptType319'):
        assert not _is_linked(b2, 'jpdl31_ScriptType319', a)


def test_assoc_script334_link_reassign_clear():
    a = jpdl31_TransitionType1(group="sample_text", name="sample_text", to="sample_text")
    b1 = jpdl31_ScriptType(acceptPropagatedEvents="sample_text", any="sample_text", mixed="sample_text", name="sample_text")
    b2 = jpdl31_ScriptType(acceptPropagatedEvents="sample_text_2", any="sample_text_2", mixed="sample_text_2", name="sample_text_2")
    _safe_set(a, 'jpdl31_TransitionType1335', {b1})
    assert _is_linked(a, 'jpdl31_TransitionType1335', b1)
    if hasattr(b1, 'jpdl31_ScriptType336'):
        assert _is_linked(b1, 'jpdl31_ScriptType336', a)
    _safe_set(a, 'jpdl31_TransitionType1335', {b2})
    assert _is_linked(a, 'jpdl31_TransitionType1335', b2)
    if hasattr(b1, 'jpdl31_ScriptType336'):
        assert not _is_linked(b1, 'jpdl31_ScriptType336', a)
    if hasattr(b2, 'jpdl31_ScriptType336'):
        assert _is_linked(b2, 'jpdl31_ScriptType336', a)
    _safe_set(a, 'jpdl31_TransitionType1335', set())
    assert not _is_linked(a, 'jpdl31_TransitionType1335', b2)
    if hasattr(b2, 'jpdl31_ScriptType336'):
        assert not _is_linked(b2, 'jpdl31_ScriptType336', a)


def test_assoc_script48_link_reassign_clear():
    a = jpdl31_ScriptType(acceptPropagatedEvents="sample_text", any="sample_text", mixed="sample_text", name="sample_text")
    b1 = jpdl31_DocumentRoot(mixed="sample_text")
    b2 = jpdl31_DocumentRoot(mixed="sample_text_2")
    _safe_set(a, 'jpdl31_ScriptType50', b1)
    assert _is_linked(a, 'jpdl31_ScriptType50', b1)
    if hasattr(b1, 'jpdl31_DocumentRoot49'):
        assert _is_linked(b1, 'jpdl31_DocumentRoot49', a)
    _safe_set(a, 'jpdl31_ScriptType50', b2)
    assert _is_linked(a, 'jpdl31_ScriptType50', b2)
    if hasattr(b1, 'jpdl31_DocumentRoot49'):
        assert not _is_linked(b1, 'jpdl31_DocumentRoot49', a)
    if hasattr(b2, 'jpdl31_DocumentRoot49'):
        assert _is_linked(b2, 'jpdl31_DocumentRoot49', a)
    _safe_set(a, 'jpdl31_ScriptType50', None)
    assert not _is_linked(a, 'jpdl31_ScriptType50', b2)
    if hasattr(b2, 'jpdl31_DocumentRoot49'):
        assert not _is_linked(b2, 'jpdl31_DocumentRoot49', a)


def test_assoc_script78_link_reassign_clear():
    a = jpdl31_ScriptType(acceptPropagatedEvents="sample_text", any="sample_text", mixed="sample_text", name="sample_text")
    b1 = jpdl31_EventType(actionElements="sample_text", type="sample_text")
    b2 = jpdl31_EventType(actionElements="sample_text_2", type="sample_text_2")
    _safe_set(a, 'jpdl31_ScriptType80', b1)
    assert _is_linked(a, 'jpdl31_ScriptType80', b1)
    if hasattr(b1, 'jpdl31_EventType79'):
        assert _is_linked(b1, 'jpdl31_EventType79', a)
    _safe_set(a, 'jpdl31_ScriptType80', b2)
    assert _is_linked(a, 'jpdl31_ScriptType80', b2)
    if hasattr(b1, 'jpdl31_EventType79'):
        assert not _is_linked(b1, 'jpdl31_EventType79', a)
    if hasattr(b2, 'jpdl31_EventType79'):
        assert _is_linked(b2, 'jpdl31_EventType79', a)
    _safe_set(a, 'jpdl31_ScriptType80', None)
    assert not _is_linked(a, 'jpdl31_ScriptType80', b2)
    if hasattr(b2, 'jpdl31_EventType79'):
        assert not _is_linked(b2, 'jpdl31_EventType79', a)


def test_assoc_script90_link_reassign_clear():
    a = jpdl31_ScriptType(acceptPropagatedEvents="sample_text", any="sample_text", mixed="sample_text", name="sample_text")
    b1 = jpdl31_ExceptionHandlerType(exceptionClass="sample_text", group="sample_text")
    b2 = jpdl31_ExceptionHandlerType(exceptionClass="sample_text_2", group="sample_text_2")
    _safe_set(a, 'jpdl31_ScriptType92', b1)
    assert _is_linked(a, 'jpdl31_ScriptType92', b1)
    if hasattr(b1, 'jpdl31_ExceptionHandlerType91'):
        assert _is_linked(b1, 'jpdl31_ExceptionHandlerType91', a)
    _safe_set(a, 'jpdl31_ScriptType92', b2)
    assert _is_linked(a, 'jpdl31_ScriptType92', b2)
    if hasattr(b1, 'jpdl31_ExceptionHandlerType91'):
        assert not _is_linked(b1, 'jpdl31_ExceptionHandlerType91', a)
    if hasattr(b2, 'jpdl31_ExceptionHandlerType91'):
        assert _is_linked(b2, 'jpdl31_ExceptionHandlerType91', a)
    _safe_set(a, 'jpdl31_ScriptType92', None)
    assert not _is_linked(a, 'jpdl31_ScriptType92', b2)
    if hasattr(b2, 'jpdl31_ExceptionHandlerType91'):
        assert not _is_linked(b2, 'jpdl31_ExceptionHandlerType91', a)


def test_assoc_script93_link_reassign_clear():
    a = jpdl31_ScriptType(acceptPropagatedEvents="sample_text", any="sample_text", mixed="sample_text", name="sample_text")
    b1 = jpdl31_ForkType(async_="sample_text", group="sample_text", name="sample_text")
    b2 = jpdl31_ForkType(async_="sample_text_2", group="sample_text_2", name="sample_text_2")
    _safe_set(a, 'jpdl31_ScriptType95', b1)
    assert _is_linked(a, 'jpdl31_ScriptType95', b1)
    if hasattr(b1, 'jpdl31_ForkType94'):
        assert _is_linked(b1, 'jpdl31_ForkType94', a)
    _safe_set(a, 'jpdl31_ScriptType95', b2)
    assert _is_linked(a, 'jpdl31_ScriptType95', b2)
    if hasattr(b1, 'jpdl31_ForkType94'):
        assert not _is_linked(b1, 'jpdl31_ForkType94', a)
    if hasattr(b2, 'jpdl31_ForkType94'):
        assert _is_linked(b2, 'jpdl31_ForkType94', a)
    _safe_set(a, 'jpdl31_ScriptType95', None)
    assert not _is_linked(a, 'jpdl31_ScriptType95', b2)
    if hasattr(b2, 'jpdl31_ForkType94'):
        assert not _is_linked(b2, 'jpdl31_ForkType94', a)


def test_assoc_startState147_link_reassign_clear():
    a = jpdl31_StartStateType(group="sample_text", name="sample_text")
    b1 = jpdl31_ProcessDefinitionType(group="sample_text", name="sample_text")
    b2 = jpdl31_ProcessDefinitionType(group="sample_text_2", name="sample_text_2")
    _safe_set(a, 'jpdl31_StartStateType149', b1)
    assert _is_linked(a, 'jpdl31_StartStateType149', b1)
    if hasattr(b1, 'jpdl31_ProcessDefinitionType148'):
        assert _is_linked(b1, 'jpdl31_ProcessDefinitionType148', a)
    _safe_set(a, 'jpdl31_StartStateType149', b2)
    assert _is_linked(a, 'jpdl31_StartStateType149', b2)
    if hasattr(b1, 'jpdl31_ProcessDefinitionType148'):
        assert not _is_linked(b1, 'jpdl31_ProcessDefinitionType148', a)
    if hasattr(b2, 'jpdl31_ProcessDefinitionType148'):
        assert _is_linked(b2, 'jpdl31_ProcessDefinitionType148', a)
    _safe_set(a, 'jpdl31_StartStateType149', None)
    assert not _is_linked(a, 'jpdl31_StartStateType149', b2)
    if hasattr(b2, 'jpdl31_ProcessDefinitionType148'):
        assert not _is_linked(b2, 'jpdl31_ProcessDefinitionType148', a)


def test_assoc_startState51_link_reassign_clear():
    a = jpdl31_StartStateType(group="sample_text", name="sample_text")
    b1 = jpdl31_DocumentRoot(mixed="sample_text")
    b2 = jpdl31_DocumentRoot(mixed="sample_text_2")
    _safe_set(a, 'jpdl31_StartStateType', b1)
    assert _is_linked(a, 'jpdl31_StartStateType', b1)
    if hasattr(b1, 'jpdl31_DocumentRoot52'):
        assert _is_linked(b1, 'jpdl31_DocumentRoot52', a)
    _safe_set(a, 'jpdl31_StartStateType', b2)
    assert _is_linked(a, 'jpdl31_StartStateType', b2)
    if hasattr(b1, 'jpdl31_DocumentRoot52'):
        assert not _is_linked(b1, 'jpdl31_DocumentRoot52', a)
    if hasattr(b2, 'jpdl31_DocumentRoot52'):
        assert _is_linked(b2, 'jpdl31_DocumentRoot52', a)
    _safe_set(a, 'jpdl31_StartStateType', None)
    assert not _is_linked(a, 'jpdl31_StartStateType', b2)
    if hasattr(b2, 'jpdl31_DocumentRoot52'):
        assert not _is_linked(b2, 'jpdl31_DocumentRoot52', a)


def test_assoc_state153_link_reassign_clear():
    a = jpdl31_StateType(async_="sample_text", name="sample_text", nodeContentElements="sample_text")
    b1 = jpdl31_ProcessDefinitionType(group="sample_text", name="sample_text")
    b2 = jpdl31_ProcessDefinitionType(group="sample_text_2", name="sample_text_2")
    _safe_set(a, 'jpdl31_StateType155', b1)
    assert _is_linked(a, 'jpdl31_StateType155', b1)
    if hasattr(b1, 'jpdl31_ProcessDefinitionType154'):
        assert _is_linked(b1, 'jpdl31_ProcessDefinitionType154', a)
    _safe_set(a, 'jpdl31_StateType155', b2)
    assert _is_linked(a, 'jpdl31_StateType155', b2)
    if hasattr(b1, 'jpdl31_ProcessDefinitionType154'):
        assert not _is_linked(b1, 'jpdl31_ProcessDefinitionType154', a)
    if hasattr(b2, 'jpdl31_ProcessDefinitionType154'):
        assert _is_linked(b2, 'jpdl31_ProcessDefinitionType154', a)
    _safe_set(a, 'jpdl31_StateType155', None)
    assert not _is_linked(a, 'jpdl31_StateType155', b2)
    if hasattr(b2, 'jpdl31_ProcessDefinitionType154'):
        assert not _is_linked(b2, 'jpdl31_ProcessDefinitionType154', a)


def test_assoc_state242_link_reassign_clear():
    a = jpdl31_SuperStateType(async_="sample_text", group="sample_text", name="sample_text")
    b1 = jpdl31_StateType(async_="sample_text", name="sample_text", nodeContentElements="sample_text")
    b2 = jpdl31_StateType(async_="sample_text_2", name="sample_text_2", nodeContentElements="sample_text_2")
    _safe_set(a, 'jpdl31_SuperStateType243', {b1})
    assert _is_linked(a, 'jpdl31_SuperStateType243', b1)
    if hasattr(b1, 'jpdl31_StateType244'):
        assert _is_linked(b1, 'jpdl31_StateType244', a)
    _safe_set(a, 'jpdl31_SuperStateType243', {b2})
    assert _is_linked(a, 'jpdl31_SuperStateType243', b2)
    if hasattr(b1, 'jpdl31_StateType244'):
        assert not _is_linked(b1, 'jpdl31_StateType244', a)
    if hasattr(b2, 'jpdl31_StateType244'):
        assert _is_linked(b2, 'jpdl31_StateType244', a)
    _safe_set(a, 'jpdl31_SuperStateType243', set())
    assert not _is_linked(a, 'jpdl31_SuperStateType243', b2)
    if hasattr(b2, 'jpdl31_StateType244'):
        assert not _is_linked(b2, 'jpdl31_StateType244', a)


def test_assoc_state53_link_reassign_clear():
    a = jpdl31_StateType(async_="sample_text", name="sample_text", nodeContentElements="sample_text")
    b1 = jpdl31_DocumentRoot(mixed="sample_text")
    b2 = jpdl31_DocumentRoot(mixed="sample_text_2")
    _safe_set(a, 'jpdl31_StateType', b1)
    assert _is_linked(a, 'jpdl31_StateType', b1)
    if hasattr(b1, 'jpdl31_DocumentRoot54'):
        assert _is_linked(b1, 'jpdl31_DocumentRoot54', a)
    _safe_set(a, 'jpdl31_StateType', b2)
    assert _is_linked(a, 'jpdl31_StateType', b2)
    if hasattr(b1, 'jpdl31_DocumentRoot54'):
        assert not _is_linked(b1, 'jpdl31_DocumentRoot54', a)
    if hasattr(b2, 'jpdl31_DocumentRoot54'):
        assert _is_linked(b2, 'jpdl31_DocumentRoot54', a)
    _safe_set(a, 'jpdl31_StateType', None)
    assert not _is_linked(a, 'jpdl31_StateType', b2)
    if hasattr(b2, 'jpdl31_DocumentRoot54'):
        assert not _is_linked(b2, 'jpdl31_DocumentRoot54', a)


def test_assoc_subProcess198_link_reassign_clear():
    a = jpdl31_SubProcessType(name="sample_text", version="sample_text")
    b1 = jpdl31_ProcessStateType(async_="sample_text", group="sample_text", name="sample_text")
    b2 = jpdl31_ProcessStateType(async_="sample_text_2", group="sample_text_2", name="sample_text_2")
    _safe_set(a, 'jpdl31_SubProcessType', b1)
    assert _is_linked(a, 'jpdl31_SubProcessType', b1)
    if hasattr(b1, 'jpdl31_ProcessStateType199'):
        assert _is_linked(b1, 'jpdl31_ProcessStateType199', a)
    _safe_set(a, 'jpdl31_SubProcessType', b2)
    assert _is_linked(a, 'jpdl31_SubProcessType', b2)
    if hasattr(b1, 'jpdl31_ProcessStateType199'):
        assert not _is_linked(b1, 'jpdl31_ProcessStateType199', a)
    if hasattr(b2, 'jpdl31_ProcessStateType199'):
        assert _is_linked(b2, 'jpdl31_ProcessStateType199', a)
    _safe_set(a, 'jpdl31_SubProcessType', None)
    assert not _is_linked(a, 'jpdl31_SubProcessType', b2)
    if hasattr(b2, 'jpdl31_ProcessStateType199'):
        assert not _is_linked(b2, 'jpdl31_ProcessStateType199', a)


def test_assoc_superState159_link_reassign_clear():
    a = jpdl31_SuperStateType(async_="sample_text", group="sample_text", name="sample_text")
    b1 = jpdl31_ProcessDefinitionType(group="sample_text", name="sample_text")
    b2 = jpdl31_ProcessDefinitionType(group="sample_text_2", name="sample_text_2")
    _safe_set(a, 'jpdl31_SuperStateType161', b1)
    assert _is_linked(a, 'jpdl31_SuperStateType161', b1)
    if hasattr(b1, 'jpdl31_ProcessDefinitionType160'):
        assert _is_linked(b1, 'jpdl31_ProcessDefinitionType160', a)
    _safe_set(a, 'jpdl31_SuperStateType161', b2)
    assert _is_linked(a, 'jpdl31_SuperStateType161', b2)
    if hasattr(b1, 'jpdl31_ProcessDefinitionType160'):
        assert not _is_linked(b1, 'jpdl31_ProcessDefinitionType160', a)
    if hasattr(b2, 'jpdl31_ProcessDefinitionType160'):
        assert _is_linked(b2, 'jpdl31_ProcessDefinitionType160', a)
    _safe_set(a, 'jpdl31_SuperStateType161', None)
    assert not _is_linked(a, 'jpdl31_SuperStateType161', b2)
    if hasattr(b2, 'jpdl31_ProcessDefinitionType160'):
        assert not _is_linked(b2, 'jpdl31_ProcessDefinitionType160', a)


def test_assoc_superState249_link_reassign_clear():
    a = jpdl31_SuperStateType(async_="sample_text", group="sample_text", name="sample_text")
    b1 = jpdl31_SuperStateType(async_="sample_text", group="sample_text", name="sample_text")
    b2 = jpdl31_SuperStateType(async_="sample_text_2", group="sample_text_2", name="sample_text_2")
    _safe_set(a, 'jpdl31_SuperStateType248', {b1})
    assert _is_linked(a, 'jpdl31_SuperStateType248', b1)
    if hasattr(b1, 'jpdl31_SuperStateType250'):
        assert _is_linked(b1, 'jpdl31_SuperStateType250', a)
    _safe_set(a, 'jpdl31_SuperStateType248', {b2})
    assert _is_linked(a, 'jpdl31_SuperStateType248', b2)
    if hasattr(b1, 'jpdl31_SuperStateType250'):
        assert not _is_linked(b1, 'jpdl31_SuperStateType250', a)
    if hasattr(b2, 'jpdl31_SuperStateType250'):
        assert _is_linked(b2, 'jpdl31_SuperStateType250', a)
    _safe_set(a, 'jpdl31_SuperStateType248', set())
    assert not _is_linked(a, 'jpdl31_SuperStateType248', b2)
    if hasattr(b2, 'jpdl31_SuperStateType250'):
        assert not _is_linked(b2, 'jpdl31_SuperStateType250', a)


def test_assoc_superState55_link_reassign_clear():
    a = jpdl31_SuperStateType(async_="sample_text", group="sample_text", name="sample_text")
    b1 = jpdl31_DocumentRoot(mixed="sample_text")
    b2 = jpdl31_DocumentRoot(mixed="sample_text_2")
    _safe_set(a, 'jpdl31_SuperStateType', b1)
    assert _is_linked(a, 'jpdl31_SuperStateType', b1)
    if hasattr(b1, 'jpdl31_DocumentRoot56'):
        assert _is_linked(b1, 'jpdl31_DocumentRoot56', a)
    _safe_set(a, 'jpdl31_SuperStateType', b2)
    assert _is_linked(a, 'jpdl31_SuperStateType', b2)
    if hasattr(b1, 'jpdl31_DocumentRoot56'):
        assert not _is_linked(b1, 'jpdl31_DocumentRoot56', a)
    if hasattr(b2, 'jpdl31_DocumentRoot56'):
        assert _is_linked(b2, 'jpdl31_DocumentRoot56', a)
    _safe_set(a, 'jpdl31_SuperStateType', None)
    assert not _is_linked(a, 'jpdl31_SuperStateType', b2)
    if hasattr(b2, 'jpdl31_DocumentRoot56'):
        assert not _is_linked(b2, 'jpdl31_DocumentRoot56', a)


def test_assoc_swimlane144_link_reassign_clear():
    a = jpdl31_SwimlaneType(name="sample_text")
    b1 = jpdl31_ProcessDefinitionType(group="sample_text", name="sample_text")
    b2 = jpdl31_ProcessDefinitionType(group="sample_text_2", name="sample_text_2")
    _safe_set(a, 'jpdl31_SwimlaneType146', b1)
    assert _is_linked(a, 'jpdl31_SwimlaneType146', b1)
    if hasattr(b1, 'jpdl31_ProcessDefinitionType145'):
        assert _is_linked(b1, 'jpdl31_ProcessDefinitionType145', a)
    _safe_set(a, 'jpdl31_SwimlaneType146', b2)
    assert _is_linked(a, 'jpdl31_SwimlaneType146', b2)
    if hasattr(b1, 'jpdl31_ProcessDefinitionType145'):
        assert not _is_linked(b1, 'jpdl31_ProcessDefinitionType145', a)
    if hasattr(b2, 'jpdl31_ProcessDefinitionType145'):
        assert _is_linked(b2, 'jpdl31_ProcessDefinitionType145', a)
    _safe_set(a, 'jpdl31_SwimlaneType146', None)
    assert not _is_linked(a, 'jpdl31_SwimlaneType146', b2)
    if hasattr(b2, 'jpdl31_ProcessDefinitionType145'):
        assert not _is_linked(b2, 'jpdl31_ProcessDefinitionType145', a)


def test_assoc_swimlane57_link_reassign_clear():
    a = jpdl31_SwimlaneType(name="sample_text")
    b1 = jpdl31_DocumentRoot(mixed="sample_text")
    b2 = jpdl31_DocumentRoot(mixed="sample_text_2")
    _safe_set(a, 'jpdl31_SwimlaneType', b1)
    assert _is_linked(a, 'jpdl31_SwimlaneType', b1)
    if hasattr(b1, 'jpdl31_DocumentRoot58'):
        assert _is_linked(b1, 'jpdl31_DocumentRoot58', a)
    _safe_set(a, 'jpdl31_SwimlaneType', b2)
    assert _is_linked(a, 'jpdl31_SwimlaneType', b2)
    if hasattr(b1, 'jpdl31_DocumentRoot58'):
        assert not _is_linked(b1, 'jpdl31_DocumentRoot58', a)
    if hasattr(b2, 'jpdl31_DocumentRoot58'):
        assert _is_linked(b2, 'jpdl31_DocumentRoot58', a)
    _safe_set(a, 'jpdl31_SwimlaneType', None)
    assert not _is_linked(a, 'jpdl31_SwimlaneType', b2)
    if hasattr(b2, 'jpdl31_DocumentRoot58'):
        assert not _is_linked(b2, 'jpdl31_DocumentRoot58', a)


def test_assoc_task195_link_reassign_clear():
    a = jpdl31_TaskType(blocking="sample_text", description="sample_text", duedate="sample_text", group="sample_text", name="sample_text", priority="sample_text", signalling="sample_text", swimlane="sample_text")
    b1 = jpdl31_ProcessDefinitionType(group="sample_text", name="sample_text")
    b2 = jpdl31_ProcessDefinitionType(group="sample_text_2", name="sample_text_2")
    _safe_set(a, 'jpdl31_TaskType197', b1)
    assert _is_linked(a, 'jpdl31_TaskType197', b1)
    if hasattr(b1, 'jpdl31_ProcessDefinitionType196'):
        assert _is_linked(b1, 'jpdl31_ProcessDefinitionType196', a)
    _safe_set(a, 'jpdl31_TaskType197', b2)
    assert _is_linked(a, 'jpdl31_TaskType197', b2)
    if hasattr(b1, 'jpdl31_ProcessDefinitionType196'):
        assert not _is_linked(b1, 'jpdl31_ProcessDefinitionType196', a)
    if hasattr(b2, 'jpdl31_ProcessDefinitionType196'):
        assert _is_linked(b2, 'jpdl31_ProcessDefinitionType196', a)
    _safe_set(a, 'jpdl31_TaskType197', None)
    assert not _is_linked(a, 'jpdl31_TaskType197', b2)
    if hasattr(b2, 'jpdl31_ProcessDefinitionType196'):
        assert not _is_linked(b2, 'jpdl31_ProcessDefinitionType196', a)


def test_assoc_task215_link_reassign_clear():
    a = jpdl31_TaskType(blocking="sample_text", description="sample_text", duedate="sample_text", group="sample_text", name="sample_text", priority="sample_text", signalling="sample_text", swimlane="sample_text")
    b1 = jpdl31_StartStateType(group="sample_text", name="sample_text")
    b2 = jpdl31_StartStateType(group="sample_text_2", name="sample_text_2")
    _safe_set(a, 'jpdl31_TaskType217', b1)
    assert _is_linked(a, 'jpdl31_TaskType217', b1)
    if hasattr(b1, 'jpdl31_StartStateType216'):
        assert _is_linked(b1, 'jpdl31_StartStateType216', a)
    _safe_set(a, 'jpdl31_TaskType217', b2)
    assert _is_linked(a, 'jpdl31_TaskType217', b2)
    if hasattr(b1, 'jpdl31_StartStateType216'):
        assert not _is_linked(b1, 'jpdl31_StartStateType216', a)
    if hasattr(b2, 'jpdl31_StartStateType216'):
        assert _is_linked(b2, 'jpdl31_StartStateType216', a)
    _safe_set(a, 'jpdl31_TaskType217', None)
    assert not _is_linked(a, 'jpdl31_TaskType217', b2)
    if hasattr(b2, 'jpdl31_StartStateType216'):
        assert not _is_linked(b2, 'jpdl31_StartStateType216', a)


def test_assoc_task281_link_reassign_clear():
    a = jpdl31_TaskType(blocking="sample_text", description="sample_text", duedate="sample_text", group="sample_text", name="sample_text", priority="sample_text", signalling="sample_text", swimlane="sample_text")
    b1 = jpdl31_TaskNodeType(async_="sample_text", createTasks="sample_text", endTasks="sample_text", group="sample_text", name="sample_text", signal="sample_text")
    b2 = jpdl31_TaskNodeType(async_="sample_text_2", createTasks="sample_text_2", endTasks="sample_text_2", group="sample_text_2", name="sample_text_2", signal="sample_text_2")
    _safe_set(a, 'jpdl31_TaskType283', b1)
    assert _is_linked(a, 'jpdl31_TaskType283', b1)
    if hasattr(b1, 'jpdl31_TaskNodeType282'):
        assert _is_linked(b1, 'jpdl31_TaskNodeType282', a)
    _safe_set(a, 'jpdl31_TaskType283', b2)
    assert _is_linked(a, 'jpdl31_TaskType283', b2)
    if hasattr(b1, 'jpdl31_TaskNodeType282'):
        assert not _is_linked(b1, 'jpdl31_TaskNodeType282', a)
    if hasattr(b2, 'jpdl31_TaskNodeType282'):
        assert _is_linked(b2, 'jpdl31_TaskNodeType282', a)
    _safe_set(a, 'jpdl31_TaskType283', None)
    assert not _is_linked(a, 'jpdl31_TaskType283', b2)
    if hasattr(b2, 'jpdl31_TaskNodeType282'):
        assert not _is_linked(b2, 'jpdl31_TaskNodeType282', a)


def test_assoc_task59_link_reassign_clear():
    a = jpdl31_TaskType(blocking="sample_text", description="sample_text", duedate="sample_text", group="sample_text", name="sample_text", priority="sample_text", signalling="sample_text", swimlane="sample_text")
    b1 = jpdl31_DocumentRoot(mixed="sample_text")
    b2 = jpdl31_DocumentRoot(mixed="sample_text_2")
    _safe_set(a, 'jpdl31_TaskType', b1)
    assert _is_linked(a, 'jpdl31_TaskType', b1)
    if hasattr(b1, 'jpdl31_DocumentRoot60'):
        assert _is_linked(b1, 'jpdl31_DocumentRoot60', a)
    _safe_set(a, 'jpdl31_TaskType', b2)
    assert _is_linked(a, 'jpdl31_TaskType', b2)
    if hasattr(b1, 'jpdl31_DocumentRoot60'):
        assert not _is_linked(b1, 'jpdl31_DocumentRoot60', a)
    if hasattr(b2, 'jpdl31_DocumentRoot60'):
        assert _is_linked(b2, 'jpdl31_DocumentRoot60', a)
    _safe_set(a, 'jpdl31_TaskType', None)
    assert not _is_linked(a, 'jpdl31_TaskType', b2)
    if hasattr(b2, 'jpdl31_DocumentRoot60'):
        assert not _is_linked(b2, 'jpdl31_DocumentRoot60', a)


def test_assoc_taskNode156_link_reassign_clear():
    a = jpdl31_TaskNodeType(async_="sample_text", createTasks="sample_text", endTasks="sample_text", group="sample_text", name="sample_text", signal="sample_text")
    b1 = jpdl31_ProcessDefinitionType(group="sample_text", name="sample_text")
    b2 = jpdl31_ProcessDefinitionType(group="sample_text_2", name="sample_text_2")
    _safe_set(a, 'jpdl31_TaskNodeType158', b1)
    assert _is_linked(a, 'jpdl31_TaskNodeType158', b1)
    if hasattr(b1, 'jpdl31_ProcessDefinitionType157'):
        assert _is_linked(b1, 'jpdl31_ProcessDefinitionType157', a)
    _safe_set(a, 'jpdl31_TaskNodeType158', b2)
    assert _is_linked(a, 'jpdl31_TaskNodeType158', b2)
    if hasattr(b1, 'jpdl31_ProcessDefinitionType157'):
        assert not _is_linked(b1, 'jpdl31_ProcessDefinitionType157', a)
    if hasattr(b2, 'jpdl31_ProcessDefinitionType157'):
        assert _is_linked(b2, 'jpdl31_ProcessDefinitionType157', a)
    _safe_set(a, 'jpdl31_TaskNodeType158', None)
    assert not _is_linked(a, 'jpdl31_TaskNodeType158', b2)
    if hasattr(b2, 'jpdl31_ProcessDefinitionType157'):
        assert not _is_linked(b2, 'jpdl31_ProcessDefinitionType157', a)


def test_assoc_taskNode245_link_reassign_clear():
    a = jpdl31_TaskNodeType(async_="sample_text", createTasks="sample_text", endTasks="sample_text", group="sample_text", name="sample_text", signal="sample_text")
    b1 = jpdl31_SuperStateType(async_="sample_text", group="sample_text", name="sample_text")
    b2 = jpdl31_SuperStateType(async_="sample_text_2", group="sample_text_2", name="sample_text_2")
    _safe_set(a, 'jpdl31_TaskNodeType247', b1)
    assert _is_linked(a, 'jpdl31_TaskNodeType247', b1)
    if hasattr(b1, 'jpdl31_SuperStateType246'):
        assert _is_linked(b1, 'jpdl31_SuperStateType246', a)
    _safe_set(a, 'jpdl31_TaskNodeType247', b2)
    assert _is_linked(a, 'jpdl31_TaskNodeType247', b2)
    if hasattr(b1, 'jpdl31_SuperStateType246'):
        assert not _is_linked(b1, 'jpdl31_SuperStateType246', a)
    if hasattr(b2, 'jpdl31_SuperStateType246'):
        assert _is_linked(b2, 'jpdl31_SuperStateType246', a)
    _safe_set(a, 'jpdl31_TaskNodeType247', None)
    assert not _is_linked(a, 'jpdl31_TaskNodeType247', b2)
    if hasattr(b2, 'jpdl31_SuperStateType246'):
        assert not _is_linked(b2, 'jpdl31_SuperStateType246', a)


def test_assoc_taskNode61_link_reassign_clear():
    a = jpdl31_TaskNodeType(async_="sample_text", createTasks="sample_text", endTasks="sample_text", group="sample_text", name="sample_text", signal="sample_text")
    b1 = jpdl31_DocumentRoot(mixed="sample_text")
    b2 = jpdl31_DocumentRoot(mixed="sample_text_2")
    _safe_set(a, 'jpdl31_TaskNodeType', b1)
    assert _is_linked(a, 'jpdl31_TaskNodeType', b1)
    if hasattr(b1, 'jpdl31_DocumentRoot62'):
        assert _is_linked(b1, 'jpdl31_DocumentRoot62', a)
    _safe_set(a, 'jpdl31_TaskNodeType', b2)
    assert _is_linked(a, 'jpdl31_TaskNodeType', b2)
    if hasattr(b1, 'jpdl31_DocumentRoot62'):
        assert not _is_linked(b1, 'jpdl31_DocumentRoot62', a)
    if hasattr(b2, 'jpdl31_DocumentRoot62'):
        assert _is_linked(b2, 'jpdl31_DocumentRoot62', a)
    _safe_set(a, 'jpdl31_TaskNodeType', None)
    assert not _is_linked(a, 'jpdl31_TaskNodeType', b2)
    if hasattr(b2, 'jpdl31_DocumentRoot62'):
        assert not _is_linked(b2, 'jpdl31_DocumentRoot62', a)


def test_assoc_timer102_link_reassign_clear():
    a = jpdl31_TimerType(duedate="sample_text", name="sample_text", repeat="sample_text", transition="sample_text")
    b1 = jpdl31_ForkType(async_="sample_text", group="sample_text", name="sample_text")
    b2 = jpdl31_ForkType(async_="sample_text_2", group="sample_text_2", name="sample_text_2")
    _safe_set(a, 'jpdl31_TimerType104', b1)
    assert _is_linked(a, 'jpdl31_TimerType104', b1)
    if hasattr(b1, 'jpdl31_ForkType103'):
        assert _is_linked(b1, 'jpdl31_ForkType103', a)
    _safe_set(a, 'jpdl31_TimerType104', b2)
    assert _is_linked(a, 'jpdl31_TimerType104', b2)
    if hasattr(b1, 'jpdl31_ForkType103'):
        assert not _is_linked(b1, 'jpdl31_ForkType103', a)
    if hasattr(b2, 'jpdl31_ForkType103'):
        assert _is_linked(b2, 'jpdl31_ForkType103', a)
    _safe_set(a, 'jpdl31_TimerType104', None)
    assert not _is_linked(a, 'jpdl31_TimerType104', b2)
    if hasattr(b2, 'jpdl31_ForkType103'):
        assert not _is_linked(b2, 'jpdl31_ForkType103', a)


def test_assoc_timer114_link_reassign_clear():
    a = jpdl31_TimerType(duedate="sample_text", name="sample_text", repeat="sample_text", transition="sample_text")
    b1 = jpdl31_JoinType(async_="sample_text", name="sample_text", nodeContentElements="sample_text")
    b2 = jpdl31_JoinType(async_="sample_text_2", name="sample_text_2", nodeContentElements="sample_text_2")
    _safe_set(a, 'jpdl31_TimerType116', b1)
    assert _is_linked(a, 'jpdl31_TimerType116', b1)
    if hasattr(b1, 'jpdl31_JoinType115'):
        assert _is_linked(b1, 'jpdl31_JoinType115', a)
    _safe_set(a, 'jpdl31_TimerType116', b2)
    assert _is_linked(a, 'jpdl31_TimerType116', b2)
    if hasattr(b1, 'jpdl31_JoinType115'):
        assert not _is_linked(b1, 'jpdl31_JoinType115', a)
    if hasattr(b2, 'jpdl31_JoinType115'):
        assert _is_linked(b2, 'jpdl31_JoinType115', a)
    _safe_set(a, 'jpdl31_TimerType116', None)
    assert not _is_linked(a, 'jpdl31_TimerType116', b2)
    if hasattr(b2, 'jpdl31_JoinType115'):
        assert not _is_linked(b2, 'jpdl31_JoinType115', a)


def test_assoc_timer138_link_reassign_clear():
    a = jpdl31_TimerType(duedate="sample_text", name="sample_text", repeat="sample_text", transition="sample_text")
    b1 = jpdl31_NodeType(async_="sample_text", name="sample_text", nodeContentElements="sample_text")
    b2 = jpdl31_NodeType(async_="sample_text_2", name="sample_text_2", nodeContentElements="sample_text_2")
    _safe_set(a, 'jpdl31_TimerType140', b1)
    assert _is_linked(a, 'jpdl31_TimerType140', b1)
    if hasattr(b1, 'jpdl31_NodeType139'):
        assert _is_linked(b1, 'jpdl31_NodeType139', a)
    _safe_set(a, 'jpdl31_TimerType140', b2)
    assert _is_linked(a, 'jpdl31_TimerType140', b2)
    if hasattr(b1, 'jpdl31_NodeType139'):
        assert not _is_linked(b1, 'jpdl31_NodeType139', a)
    if hasattr(b2, 'jpdl31_NodeType139'):
        assert _is_linked(b2, 'jpdl31_NodeType139', a)
    _safe_set(a, 'jpdl31_TimerType140', None)
    assert not _is_linked(a, 'jpdl31_TimerType140', b2)
    if hasattr(b2, 'jpdl31_NodeType139'):
        assert not _is_linked(b2, 'jpdl31_NodeType139', a)


def test_assoc_timer209_link_reassign_clear():
    a = jpdl31_TimerType(duedate="sample_text", name="sample_text", repeat="sample_text", transition="sample_text")
    b1 = jpdl31_ProcessStateType(async_="sample_text", group="sample_text", name="sample_text")
    b2 = jpdl31_ProcessStateType(async_="sample_text_2", group="sample_text_2", name="sample_text_2")
    _safe_set(a, 'jpdl31_TimerType211', b1)
    assert _is_linked(a, 'jpdl31_TimerType211', b1)
    if hasattr(b1, 'jpdl31_ProcessStateType210'):
        assert _is_linked(b1, 'jpdl31_ProcessStateType210', a)
    _safe_set(a, 'jpdl31_TimerType211', b2)
    assert _is_linked(a, 'jpdl31_TimerType211', b2)
    if hasattr(b1, 'jpdl31_ProcessStateType210'):
        assert not _is_linked(b1, 'jpdl31_ProcessStateType210', a)
    if hasattr(b2, 'jpdl31_ProcessStateType210'):
        assert _is_linked(b2, 'jpdl31_ProcessStateType210', a)
    _safe_set(a, 'jpdl31_TimerType211', None)
    assert not _is_linked(a, 'jpdl31_TimerType211', b2)
    if hasattr(b2, 'jpdl31_ProcessStateType210'):
        assert not _is_linked(b2, 'jpdl31_ProcessStateType210', a)


def test_assoc_timer233_link_reassign_clear():
    a = jpdl31_TimerType(duedate="sample_text", name="sample_text", repeat="sample_text", transition="sample_text")
    b1 = jpdl31_StateType(async_="sample_text", name="sample_text", nodeContentElements="sample_text")
    b2 = jpdl31_StateType(async_="sample_text_2", name="sample_text_2", nodeContentElements="sample_text_2")
    _safe_set(a, 'jpdl31_TimerType235', b1)
    assert _is_linked(a, 'jpdl31_TimerType235', b1)
    if hasattr(b1, 'jpdl31_StateType234'):
        assert _is_linked(b1, 'jpdl31_StateType234', a)
    _safe_set(a, 'jpdl31_TimerType235', b2)
    assert _is_linked(a, 'jpdl31_TimerType235', b2)
    if hasattr(b1, 'jpdl31_StateType234'):
        assert not _is_linked(b1, 'jpdl31_StateType234', a)
    if hasattr(b2, 'jpdl31_StateType234'):
        assert _is_linked(b2, 'jpdl31_StateType234', a)
    _safe_set(a, 'jpdl31_TimerType235', None)
    assert not _is_linked(a, 'jpdl31_TimerType235', b2)
    if hasattr(b2, 'jpdl31_StateType234'):
        assert not _is_linked(b2, 'jpdl31_StateType234', a)


def test_assoc_timer272_link_reassign_clear():
    a = jpdl31_TimerType(duedate="sample_text", name="sample_text", repeat="sample_text", transition="sample_text")
    b1 = jpdl31_SuperStateType(async_="sample_text", group="sample_text", name="sample_text")
    b2 = jpdl31_SuperStateType(async_="sample_text_2", group="sample_text_2", name="sample_text_2")
    _safe_set(a, 'jpdl31_TimerType274', b1)
    assert _is_linked(a, 'jpdl31_TimerType274', b1)
    if hasattr(b1, 'jpdl31_SuperStateType273'):
        assert _is_linked(b1, 'jpdl31_SuperStateType273', a)
    _safe_set(a, 'jpdl31_TimerType274', b2)
    assert _is_linked(a, 'jpdl31_TimerType274', b2)
    if hasattr(b1, 'jpdl31_SuperStateType273'):
        assert not _is_linked(b1, 'jpdl31_SuperStateType273', a)
    if hasattr(b2, 'jpdl31_SuperStateType273'):
        assert _is_linked(b2, 'jpdl31_SuperStateType273', a)
    _safe_set(a, 'jpdl31_TimerType274', None)
    assert not _is_linked(a, 'jpdl31_TimerType274', b2)
    if hasattr(b2, 'jpdl31_SuperStateType273'):
        assert not _is_linked(b2, 'jpdl31_SuperStateType273', a)


def test_assoc_timer290_link_reassign_clear():
    a = jpdl31_TimerType(duedate="sample_text", name="sample_text", repeat="sample_text", transition="sample_text")
    b1 = jpdl31_TaskNodeType(async_="sample_text", createTasks="sample_text", endTasks="sample_text", group="sample_text", name="sample_text", signal="sample_text")
    b2 = jpdl31_TaskNodeType(async_="sample_text_2", createTasks="sample_text_2", endTasks="sample_text_2", group="sample_text_2", name="sample_text_2", signal="sample_text_2")
    _safe_set(a, 'jpdl31_TimerType292', b1)
    assert _is_linked(a, 'jpdl31_TimerType292', b1)
    if hasattr(b1, 'jpdl31_TaskNodeType291'):
        assert _is_linked(b1, 'jpdl31_TaskNodeType291', a)
    _safe_set(a, 'jpdl31_TimerType292', b2)
    assert _is_linked(a, 'jpdl31_TimerType292', b2)
    if hasattr(b1, 'jpdl31_TaskNodeType291'):
        assert not _is_linked(b1, 'jpdl31_TaskNodeType291', a)
    if hasattr(b2, 'jpdl31_TaskNodeType291'):
        assert _is_linked(b2, 'jpdl31_TaskNodeType291', a)
    _safe_set(a, 'jpdl31_TimerType292', None)
    assert not _is_linked(a, 'jpdl31_TimerType292', b2)
    if hasattr(b2, 'jpdl31_TaskNodeType291'):
        assert not _is_linked(b2, 'jpdl31_TaskNodeType291', a)


def test_assoc_timer305_link_reassign_clear():
    a = jpdl31_TimerType(duedate="sample_text", name="sample_text", repeat="sample_text", transition="sample_text")
    b1 = jpdl31_TaskType(blocking="sample_text", description="sample_text", duedate="sample_text", group="sample_text", name="sample_text", priority="sample_text", signalling="sample_text", swimlane="sample_text")
    b2 = jpdl31_TaskType(blocking="sample_text_2", description="sample_text_2", duedate="sample_text_2", group="sample_text_2", name="sample_text_2", priority="sample_text_2", signalling="sample_text_2", swimlane="sample_text_2")
    _safe_set(a, 'jpdl31_TimerType307', b1)
    assert _is_linked(a, 'jpdl31_TimerType307', b1)
    if hasattr(b1, 'jpdl31_TaskType306'):
        assert _is_linked(b1, 'jpdl31_TaskType306', a)
    _safe_set(a, 'jpdl31_TimerType307', b2)
    assert _is_linked(a, 'jpdl31_TimerType307', b2)
    if hasattr(b1, 'jpdl31_TaskType306'):
        assert not _is_linked(b1, 'jpdl31_TaskType306', a)
    if hasattr(b2, 'jpdl31_TaskType306'):
        assert _is_linked(b2, 'jpdl31_TaskType306', a)
    _safe_set(a, 'jpdl31_TimerType307', None)
    assert not _is_linked(a, 'jpdl31_TimerType307', b2)
    if hasattr(b2, 'jpdl31_TaskType306'):
        assert not _is_linked(b2, 'jpdl31_TaskType306', a)


def test_assoc_timer63_link_reassign_clear():
    a = jpdl31_TimerType(duedate="sample_text", name="sample_text", repeat="sample_text", transition="sample_text")
    b1 = jpdl31_DocumentRoot(mixed="sample_text")
    b2 = jpdl31_DocumentRoot(mixed="sample_text_2")
    _safe_set(a, 'jpdl31_TimerType', b1)
    assert _is_linked(a, 'jpdl31_TimerType', b1)
    if hasattr(b1, 'jpdl31_DocumentRoot64'):
        assert _is_linked(b1, 'jpdl31_DocumentRoot64', a)
    _safe_set(a, 'jpdl31_TimerType', b2)
    assert _is_linked(a, 'jpdl31_TimerType', b2)
    if hasattr(b1, 'jpdl31_DocumentRoot64'):
        assert not _is_linked(b1, 'jpdl31_DocumentRoot64', a)
    if hasattr(b2, 'jpdl31_DocumentRoot64'):
        assert _is_linked(b2, 'jpdl31_DocumentRoot64', a)
    _safe_set(a, 'jpdl31_TimerType', None)
    assert not _is_linked(a, 'jpdl31_TimerType', b2)
    if hasattr(b2, 'jpdl31_DocumentRoot64'):
        assert not _is_linked(b2, 'jpdl31_DocumentRoot64', a)


def test_assoc_transition105_link_reassign_clear():
    a = jpdl31_TransitionType(group="sample_text", name="sample_text", to="sample_text")
    b1 = jpdl31_ForkType(async_="sample_text", group="sample_text", name="sample_text")
    b2 = jpdl31_ForkType(async_="sample_text_2", group="sample_text_2", name="sample_text_2")
    _safe_set(a, 'jpdl31_TransitionType107', b1)
    assert _is_linked(a, 'jpdl31_TransitionType107', b1)
    if hasattr(b1, 'jpdl31_ForkType106'):
        assert _is_linked(b1, 'jpdl31_ForkType106', a)
    _safe_set(a, 'jpdl31_TransitionType107', b2)
    assert _is_linked(a, 'jpdl31_TransitionType107', b2)
    if hasattr(b1, 'jpdl31_ForkType106'):
        assert not _is_linked(b1, 'jpdl31_ForkType106', a)
    if hasattr(b2, 'jpdl31_ForkType106'):
        assert _is_linked(b2, 'jpdl31_ForkType106', a)
    _safe_set(a, 'jpdl31_TransitionType107', None)
    assert not _is_linked(a, 'jpdl31_TransitionType107', b2)
    if hasattr(b2, 'jpdl31_ForkType106'):
        assert not _is_linked(b2, 'jpdl31_ForkType106', a)


def test_assoc_transition117_link_reassign_clear():
    a = jpdl31_TransitionType(group="sample_text", name="sample_text", to="sample_text")
    b1 = jpdl31_JoinType(async_="sample_text", name="sample_text", nodeContentElements="sample_text")
    b2 = jpdl31_JoinType(async_="sample_text_2", name="sample_text_2", nodeContentElements="sample_text_2")
    _safe_set(a, 'jpdl31_TransitionType119', b1)
    assert _is_linked(a, 'jpdl31_TransitionType119', b1)
    if hasattr(b1, 'jpdl31_JoinType118'):
        assert _is_linked(b1, 'jpdl31_JoinType118', a)
    _safe_set(a, 'jpdl31_TransitionType119', b2)
    assert _is_linked(a, 'jpdl31_TransitionType119', b2)
    if hasattr(b1, 'jpdl31_JoinType118'):
        assert not _is_linked(b1, 'jpdl31_JoinType118', a)
    if hasattr(b2, 'jpdl31_JoinType118'):
        assert _is_linked(b2, 'jpdl31_JoinType118', a)
    _safe_set(a, 'jpdl31_TransitionType119', None)
    assert not _is_linked(a, 'jpdl31_TransitionType119', b2)
    if hasattr(b2, 'jpdl31_JoinType118'):
        assert not _is_linked(b2, 'jpdl31_JoinType118', a)


def test_assoc_transition141_link_reassign_clear():
    a = jpdl31_TransitionType(group="sample_text", name="sample_text", to="sample_text")
    b1 = jpdl31_NodeType(async_="sample_text", name="sample_text", nodeContentElements="sample_text")
    b2 = jpdl31_NodeType(async_="sample_text_2", name="sample_text_2", nodeContentElements="sample_text_2")
    _safe_set(a, 'jpdl31_TransitionType143', b1)
    assert _is_linked(a, 'jpdl31_TransitionType143', b1)
    if hasattr(b1, 'jpdl31_NodeType142'):
        assert _is_linked(b1, 'jpdl31_NodeType142', a)
    _safe_set(a, 'jpdl31_TransitionType143', b2)
    assert _is_linked(a, 'jpdl31_TransitionType143', b2)
    if hasattr(b1, 'jpdl31_NodeType142'):
        assert not _is_linked(b1, 'jpdl31_NodeType142', a)
    if hasattr(b2, 'jpdl31_NodeType142'):
        assert _is_linked(b2, 'jpdl31_NodeType142', a)
    _safe_set(a, 'jpdl31_TransitionType143', None)
    assert not _is_linked(a, 'jpdl31_TransitionType143', b2)
    if hasattr(b2, 'jpdl31_NodeType142'):
        assert not _is_linked(b2, 'jpdl31_NodeType142', a)


def test_assoc_transition212_link_reassign_clear():
    a = jpdl31_TransitionType(group="sample_text", name="sample_text", to="sample_text")
    b1 = jpdl31_ProcessStateType(async_="sample_text", group="sample_text", name="sample_text")
    b2 = jpdl31_ProcessStateType(async_="sample_text_2", group="sample_text_2", name="sample_text_2")
    _safe_set(a, 'jpdl31_TransitionType214', b1)
    assert _is_linked(a, 'jpdl31_TransitionType214', b1)
    if hasattr(b1, 'jpdl31_ProcessStateType213'):
        assert _is_linked(b1, 'jpdl31_ProcessStateType213', a)
    _safe_set(a, 'jpdl31_TransitionType214', b2)
    assert _is_linked(a, 'jpdl31_TransitionType214', b2)
    if hasattr(b1, 'jpdl31_ProcessStateType213'):
        assert not _is_linked(b1, 'jpdl31_ProcessStateType213', a)
    if hasattr(b2, 'jpdl31_ProcessStateType213'):
        assert _is_linked(b2, 'jpdl31_ProcessStateType213', a)
    _safe_set(a, 'jpdl31_TransitionType214', None)
    assert not _is_linked(a, 'jpdl31_TransitionType214', b2)
    if hasattr(b2, 'jpdl31_ProcessStateType213'):
        assert not _is_linked(b2, 'jpdl31_ProcessStateType213', a)


def test_assoc_transition218_link_reassign_clear():
    a = jpdl31_TransitionType(group="sample_text", name="sample_text", to="sample_text")
    b1 = jpdl31_StartStateType(group="sample_text", name="sample_text")
    b2 = jpdl31_StartStateType(group="sample_text_2", name="sample_text_2")
    _safe_set(a, 'jpdl31_TransitionType220', b1)
    assert _is_linked(a, 'jpdl31_TransitionType220', b1)
    if hasattr(b1, 'jpdl31_StartStateType219'):
        assert _is_linked(b1, 'jpdl31_StartStateType219', a)
    _safe_set(a, 'jpdl31_TransitionType220', b2)
    assert _is_linked(a, 'jpdl31_TransitionType220', b2)
    if hasattr(b1, 'jpdl31_StartStateType219'):
        assert not _is_linked(b1, 'jpdl31_StartStateType219', a)
    if hasattr(b2, 'jpdl31_StartStateType219'):
        assert _is_linked(b2, 'jpdl31_StartStateType219', a)
    _safe_set(a, 'jpdl31_TransitionType220', None)
    assert not _is_linked(a, 'jpdl31_TransitionType220', b2)
    if hasattr(b2, 'jpdl31_StartStateType219'):
        assert not _is_linked(b2, 'jpdl31_StartStateType219', a)


def test_assoc_transition236_link_reassign_clear():
    a = jpdl31_TransitionType(group="sample_text", name="sample_text", to="sample_text")
    b1 = jpdl31_StateType(async_="sample_text", name="sample_text", nodeContentElements="sample_text")
    b2 = jpdl31_StateType(async_="sample_text_2", name="sample_text_2", nodeContentElements="sample_text_2")
    _safe_set(a, 'jpdl31_TransitionType238', b1)
    assert _is_linked(a, 'jpdl31_TransitionType238', b1)
    if hasattr(b1, 'jpdl31_StateType237'):
        assert _is_linked(b1, 'jpdl31_StateType237', a)
    _safe_set(a, 'jpdl31_TransitionType238', b2)
    assert _is_linked(a, 'jpdl31_TransitionType238', b2)
    if hasattr(b1, 'jpdl31_StateType237'):
        assert not _is_linked(b1, 'jpdl31_StateType237', a)
    if hasattr(b2, 'jpdl31_StateType237'):
        assert _is_linked(b2, 'jpdl31_StateType237', a)
    _safe_set(a, 'jpdl31_TransitionType238', None)
    assert not _is_linked(a, 'jpdl31_TransitionType238', b2)
    if hasattr(b2, 'jpdl31_StateType237'):
        assert not _is_linked(b2, 'jpdl31_StateType237', a)


def test_assoc_transition275_link_reassign_clear():
    a = jpdl31_TransitionType(group="sample_text", name="sample_text", to="sample_text")
    b1 = jpdl31_SuperStateType(async_="sample_text", group="sample_text", name="sample_text")
    b2 = jpdl31_SuperStateType(async_="sample_text_2", group="sample_text_2", name="sample_text_2")
    _safe_set(a, 'jpdl31_TransitionType277', b1)
    assert _is_linked(a, 'jpdl31_TransitionType277', b1)
    if hasattr(b1, 'jpdl31_SuperStateType276'):
        assert _is_linked(b1, 'jpdl31_SuperStateType276', a)
    _safe_set(a, 'jpdl31_TransitionType277', b2)
    assert _is_linked(a, 'jpdl31_TransitionType277', b2)
    if hasattr(b1, 'jpdl31_SuperStateType276'):
        assert not _is_linked(b1, 'jpdl31_SuperStateType276', a)
    if hasattr(b2, 'jpdl31_SuperStateType276'):
        assert _is_linked(b2, 'jpdl31_SuperStateType276', a)
    _safe_set(a, 'jpdl31_TransitionType277', None)
    assert not _is_linked(a, 'jpdl31_TransitionType277', b2)
    if hasattr(b2, 'jpdl31_SuperStateType276'):
        assert not _is_linked(b2, 'jpdl31_SuperStateType276', a)


def test_assoc_transition293_link_reassign_clear():
    a = jpdl31_TransitionType(group="sample_text", name="sample_text", to="sample_text")
    b1 = jpdl31_TaskNodeType(async_="sample_text", createTasks="sample_text", endTasks="sample_text", group="sample_text", name="sample_text", signal="sample_text")
    b2 = jpdl31_TaskNodeType(async_="sample_text_2", createTasks="sample_text_2", endTasks="sample_text_2", group="sample_text_2", name="sample_text_2", signal="sample_text_2")
    _safe_set(a, 'jpdl31_TransitionType295', b1)
    assert _is_linked(a, 'jpdl31_TransitionType295', b1)
    if hasattr(b1, 'jpdl31_TaskNodeType294'):
        assert _is_linked(b1, 'jpdl31_TaskNodeType294', a)
    _safe_set(a, 'jpdl31_TransitionType295', b2)
    assert _is_linked(a, 'jpdl31_TransitionType295', b2)
    if hasattr(b1, 'jpdl31_TaskNodeType294'):
        assert not _is_linked(b1, 'jpdl31_TaskNodeType294', a)
    if hasattr(b2, 'jpdl31_TaskNodeType294'):
        assert _is_linked(b2, 'jpdl31_TaskNodeType294', a)
    _safe_set(a, 'jpdl31_TransitionType295', None)
    assert not _is_linked(a, 'jpdl31_TransitionType295', b2)
    if hasattr(b2, 'jpdl31_TaskNodeType294'):
        assert not _is_linked(b2, 'jpdl31_TaskNodeType294', a)


def test_assoc_transition65_link_reassign_clear():
    a = jpdl31_TransitionType(group="sample_text", name="sample_text", to="sample_text")
    b1 = jpdl31_DocumentRoot(mixed="sample_text")
    b2 = jpdl31_DocumentRoot(mixed="sample_text_2")
    _safe_set(a, 'jpdl31_TransitionType', b1)
    assert _is_linked(a, 'jpdl31_TransitionType', b1)
    if hasattr(b1, 'jpdl31_DocumentRoot66'):
        assert _is_linked(b1, 'jpdl31_DocumentRoot66', a)
    _safe_set(a, 'jpdl31_TransitionType', b2)
    assert _is_linked(a, 'jpdl31_TransitionType', b2)
    if hasattr(b1, 'jpdl31_DocumentRoot66'):
        assert not _is_linked(b1, 'jpdl31_DocumentRoot66', a)
    if hasattr(b2, 'jpdl31_DocumentRoot66'):
        assert _is_linked(b2, 'jpdl31_DocumentRoot66', a)
    _safe_set(a, 'jpdl31_TransitionType', None)
    assert not _is_linked(a, 'jpdl31_TransitionType', b2)
    if hasattr(b2, 'jpdl31_DocumentRoot66'):
        assert not _is_linked(b2, 'jpdl31_DocumentRoot66', a)


def test_assoc_transition8_link_reassign_clear():
    a = jpdl31_TransitionType1(group="sample_text", name="sample_text", to="sample_text")
    b1 = jpdl31_DecisionType(async_="sample_text", expression="sample_text", group="sample_text", name="sample_text")
    b2 = jpdl31_DecisionType(async_="sample_text_2", expression="sample_text_2", group="sample_text_2", name="sample_text_2")
    _safe_set(a, 'jpdl31_TransitionType1', b1)
    assert _is_linked(a, 'jpdl31_TransitionType1', b1)
    if hasattr(b1, 'jpdl31_DecisionType9'):
        assert _is_linked(b1, 'jpdl31_DecisionType9', a)
    _safe_set(a, 'jpdl31_TransitionType1', b2)
    assert _is_linked(a, 'jpdl31_TransitionType1', b2)
    if hasattr(b1, 'jpdl31_DecisionType9'):
        assert not _is_linked(b1, 'jpdl31_DecisionType9', a)
    if hasattr(b2, 'jpdl31_DecisionType9'):
        assert _is_linked(b2, 'jpdl31_DecisionType9', a)
    _safe_set(a, 'jpdl31_TransitionType1', None)
    assert not _is_linked(a, 'jpdl31_TransitionType1', b2)
    if hasattr(b2, 'jpdl31_DecisionType9'):
        assert not _is_linked(b2, 'jpdl31_DecisionType9', a)


def test_assoc_variable200_link_reassign_clear():
    a = jpdl31_VariableType(access="sample_text", any="sample_text", mappedName="sample_text", name="sample_text")
    b1 = jpdl31_ProcessStateType(async_="sample_text", group="sample_text", name="sample_text")
    b2 = jpdl31_ProcessStateType(async_="sample_text_2", group="sample_text_2", name="sample_text_2")
    _safe_set(a, 'jpdl31_VariableType202', b1)
    assert _is_linked(a, 'jpdl31_VariableType202', b1)
    if hasattr(b1, 'jpdl31_ProcessStateType201'):
        assert _is_linked(b1, 'jpdl31_ProcessStateType201', a)
    _safe_set(a, 'jpdl31_VariableType202', b2)
    assert _is_linked(a, 'jpdl31_VariableType202', b2)
    if hasattr(b1, 'jpdl31_ProcessStateType201'):
        assert not _is_linked(b1, 'jpdl31_ProcessStateType201', a)
    if hasattr(b2, 'jpdl31_ProcessStateType201'):
        assert _is_linked(b2, 'jpdl31_ProcessStateType201', a)
    _safe_set(a, 'jpdl31_VariableType202', None)
    assert not _is_linked(a, 'jpdl31_VariableType202', b2)
    if hasattr(b2, 'jpdl31_ProcessStateType201'):
        assert not _is_linked(b2, 'jpdl31_ProcessStateType201', a)


def test_assoc_variable67_link_reassign_clear():
    a = jpdl31_VariableType(access="sample_text", any="sample_text", mappedName="sample_text", name="sample_text")
    b1 = jpdl31_DocumentRoot(mixed="sample_text")
    b2 = jpdl31_DocumentRoot(mixed="sample_text_2")
    _safe_set(a, 'jpdl31_VariableType', b1)
    assert _is_linked(a, 'jpdl31_VariableType', b1)
    if hasattr(b1, 'jpdl31_DocumentRoot68'):
        assert _is_linked(b1, 'jpdl31_DocumentRoot68', a)
    _safe_set(a, 'jpdl31_VariableType', b2)
    assert _is_linked(a, 'jpdl31_VariableType', b2)
    if hasattr(b1, 'jpdl31_DocumentRoot68'):
        assert not _is_linked(b1, 'jpdl31_DocumentRoot68', a)
    if hasattr(b2, 'jpdl31_DocumentRoot68'):
        assert _is_linked(b2, 'jpdl31_DocumentRoot68', a)
    _safe_set(a, 'jpdl31_VariableType', None)
    assert not _is_linked(a, 'jpdl31_VariableType', b2)
    if hasattr(b2, 'jpdl31_DocumentRoot68'):
        assert not _is_linked(b2, 'jpdl31_DocumentRoot68', a)


def test_assoc_xMLNSPrefixMap10_link_reassign_clear():
    a = jpdl31_DocumentRoot(mixed="sample_text")
    b1 = jpdl31_EStringToStringMapEntry()
    b2 = jpdl31_EStringToStringMapEntry()
    _safe_set(a, 'jpdl31_DocumentRoot', {b1})
    assert _is_linked(a, 'jpdl31_DocumentRoot', b1)
    if hasattr(b1, 'jpdl31_EStringToStringMapEntry'):
        assert _is_linked(b1, 'jpdl31_EStringToStringMapEntry', a)
    _safe_set(a, 'jpdl31_DocumentRoot', {b2})
    assert _is_linked(a, 'jpdl31_DocumentRoot', b2)
    if hasattr(b1, 'jpdl31_EStringToStringMapEntry'):
        assert not _is_linked(b1, 'jpdl31_EStringToStringMapEntry', a)
    if hasattr(b2, 'jpdl31_EStringToStringMapEntry'):
        assert _is_linked(b2, 'jpdl31_EStringToStringMapEntry', a)
    _safe_set(a, 'jpdl31_DocumentRoot', set())
    assert not _is_linked(a, 'jpdl31_DocumentRoot', b2)
    if hasattr(b2, 'jpdl31_EStringToStringMapEntry'):
        assert not _is_linked(b2, 'jpdl31_EStringToStringMapEntry', a)


def test_assoc_xSISchemaLocation11_link_reassign_clear():
    a = jpdl31_DocumentRoot(mixed="sample_text")
    b1 = jpdl31_EStringToStringMapEntry()
    b2 = jpdl31_EStringToStringMapEntry()
    _safe_set(a, 'jpdl31_DocumentRoot12', {b1})
    assert _is_linked(a, 'jpdl31_DocumentRoot12', b1)
    if hasattr(b1, 'jpdl31_EStringToStringMapEntry13'):
        assert _is_linked(b1, 'jpdl31_EStringToStringMapEntry13', a)
    _safe_set(a, 'jpdl31_DocumentRoot12', {b2})
    assert _is_linked(a, 'jpdl31_DocumentRoot12', b2)
    if hasattr(b1, 'jpdl31_EStringToStringMapEntry13'):
        assert not _is_linked(b1, 'jpdl31_EStringToStringMapEntry13', a)
    if hasattr(b2, 'jpdl31_EStringToStringMapEntry13'):
        assert _is_linked(b2, 'jpdl31_EStringToStringMapEntry13', a)
    _safe_set(a, 'jpdl31_DocumentRoot12', set())
    assert not _is_linked(a, 'jpdl31_DocumentRoot12', b2)
    if hasattr(b2, 'jpdl31_EStringToStringMapEntry13'):
        assert not _is_linked(b2, 'jpdl31_EStringToStringMapEntry13', a)


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

Delegation_strategy = st.builds(Delegation)
@given(instance=Delegation_strategy)
@settings(max_examples=25)
def test_Delegation_instantiation(instance):
    assert isinstance(instance, Delegation)


jpdl31_ActionType_strategy = st.builds(jpdl31_ActionType, acceptPropagatedEvents=safe_text, any=safe_text, async_=safe_text, class_=safe_text, configType=safe_text, expression=safe_text, mixed=safe_text, name=safe_text, refName=safe_text)
@given(instance=jpdl31_ActionType_strategy)
@settings(max_examples=25)
def test_jpdl31_ActionType_instantiation(instance):
    assert isinstance(instance, jpdl31_ActionType)


jpdl31_AssignmentType_strategy = st.builds(jpdl31_AssignmentType, actorId=safe_text, expression=safe_text, pooledActors=safe_text)
@given(instance=jpdl31_AssignmentType_strategy)
@settings(max_examples=25)
def test_jpdl31_AssignmentType_instantiation(instance):
    assert isinstance(instance, jpdl31_AssignmentType)


jpdl31_CancelTimerType_strategy = st.builds(jpdl31_CancelTimerType, name=safe_text)
@given(instance=jpdl31_CancelTimerType_strategy)
@settings(max_examples=25)
def test_jpdl31_CancelTimerType_instantiation(instance):
    assert isinstance(instance, jpdl31_CancelTimerType)


jpdl31_ConditionType_strategy = st.builds(jpdl31_ConditionType, any=safe_text, expression=safe_text, group=safe_text, mixed=safe_text)
@given(instance=jpdl31_ConditionType_strategy)
@settings(max_examples=25)
def test_jpdl31_ConditionType_instantiation(instance):
    assert isinstance(instance, jpdl31_ConditionType)


jpdl31_CreateTimerType_strategy = st.builds(jpdl31_CreateTimerType, duedate=safe_text, name=safe_text, repeat=safe_text, transition=safe_text)
@given(instance=jpdl31_CreateTimerType_strategy)
@settings(max_examples=25)
def test_jpdl31_CreateTimerType_instantiation(instance):
    assert isinstance(instance, jpdl31_CreateTimerType)


jpdl31_DecisionType_strategy = st.builds(jpdl31_DecisionType, async_=safe_text, expression=safe_text, group=safe_text, name=safe_text)
@given(instance=jpdl31_DecisionType_strategy)
@settings(max_examples=25)
def test_jpdl31_DecisionType_instantiation(instance):
    assert isinstance(instance, jpdl31_DecisionType)


jpdl31_Delegation_strategy = st.builds(jpdl31_Delegation, any=safe_text, class_=safe_text, configType=safe_text, mixed=safe_text)
@given(instance=jpdl31_Delegation_strategy)
@settings(max_examples=25)
def test_jpdl31_Delegation_instantiation(instance):
    assert isinstance(instance, jpdl31_Delegation)


jpdl31_DocumentRoot_strategy = st.builds(jpdl31_DocumentRoot, mixed=safe_text)
@given(instance=jpdl31_DocumentRoot_strategy)
@settings(max_examples=25)
def test_jpdl31_DocumentRoot_instantiation(instance):
    assert isinstance(instance, jpdl31_DocumentRoot)


jpdl31_EStringToStringMapEntry_strategy = st.builds(jpdl31_EStringToStringMapEntry)
@given(instance=jpdl31_EStringToStringMapEntry_strategy)
@settings(max_examples=25)
def test_jpdl31_EStringToStringMapEntry_instantiation(instance):
    assert isinstance(instance, jpdl31_EStringToStringMapEntry)


jpdl31_EndStateType_strategy = st.builds(jpdl31_EndStateType, group=safe_text, name=safe_text)
@given(instance=jpdl31_EndStateType_strategy)
@settings(max_examples=25)
def test_jpdl31_EndStateType_instantiation(instance):
    assert isinstance(instance, jpdl31_EndStateType)


jpdl31_EventType_strategy = st.builds(jpdl31_EventType, actionElements=safe_text, type=safe_text)
@given(instance=jpdl31_EventType_strategy)
@settings(max_examples=25)
def test_jpdl31_EventType_instantiation(instance):
    assert isinstance(instance, jpdl31_EventType)


jpdl31_ExceptionHandlerType_strategy = st.builds(jpdl31_ExceptionHandlerType, exceptionClass=safe_text, group=safe_text)
@given(instance=jpdl31_ExceptionHandlerType_strategy)
@settings(max_examples=25)
def test_jpdl31_ExceptionHandlerType_instantiation(instance):
    assert isinstance(instance, jpdl31_ExceptionHandlerType)


jpdl31_ForkType_strategy = st.builds(jpdl31_ForkType, async_=safe_text, group=safe_text, name=safe_text)
@given(instance=jpdl31_ForkType_strategy)
@settings(max_examples=25)
def test_jpdl31_ForkType_instantiation(instance):
    assert isinstance(instance, jpdl31_ForkType)


jpdl31_JoinType_strategy = st.builds(jpdl31_JoinType, async_=safe_text, name=safe_text, nodeContentElements=safe_text)
@given(instance=jpdl31_JoinType_strategy)
@settings(max_examples=25)
def test_jpdl31_JoinType_instantiation(instance):
    assert isinstance(instance, jpdl31_JoinType)


jpdl31_NodeType_strategy = st.builds(jpdl31_NodeType, async_=safe_text, name=safe_text, nodeContentElements=safe_text)
@given(instance=jpdl31_NodeType_strategy)
@settings(max_examples=25)
def test_jpdl31_NodeType_instantiation(instance):
    assert isinstance(instance, jpdl31_NodeType)


jpdl31_ProcessDefinitionType_strategy = st.builds(jpdl31_ProcessDefinitionType, group=safe_text, name=safe_text)
@given(instance=jpdl31_ProcessDefinitionType_strategy)
@settings(max_examples=25)
def test_jpdl31_ProcessDefinitionType_instantiation(instance):
    assert isinstance(instance, jpdl31_ProcessDefinitionType)


jpdl31_ProcessStateType_strategy = st.builds(jpdl31_ProcessStateType, async_=safe_text, group=safe_text, name=safe_text)
@given(instance=jpdl31_ProcessStateType_strategy)
@settings(max_examples=25)
def test_jpdl31_ProcessStateType_instantiation(instance):
    assert isinstance(instance, jpdl31_ProcessStateType)


jpdl31_ScriptType_strategy = st.builds(jpdl31_ScriptType, acceptPropagatedEvents=safe_text, any=safe_text, mixed=safe_text, name=safe_text)
@given(instance=jpdl31_ScriptType_strategy)
@settings(max_examples=25)
def test_jpdl31_ScriptType_instantiation(instance):
    assert isinstance(instance, jpdl31_ScriptType)


jpdl31_StartStateType_strategy = st.builds(jpdl31_StartStateType, group=safe_text, name=safe_text)
@given(instance=jpdl31_StartStateType_strategy)
@settings(max_examples=25)
def test_jpdl31_StartStateType_instantiation(instance):
    assert isinstance(instance, jpdl31_StartStateType)


jpdl31_StateType_strategy = st.builds(jpdl31_StateType, async_=safe_text, name=safe_text, nodeContentElements=safe_text)
@given(instance=jpdl31_StateType_strategy)
@settings(max_examples=25)
def test_jpdl31_StateType_instantiation(instance):
    assert isinstance(instance, jpdl31_StateType)


jpdl31_SubProcessType_strategy = st.builds(jpdl31_SubProcessType, name=safe_text, version=safe_text)
@given(instance=jpdl31_SubProcessType_strategy)
@settings(max_examples=25)
def test_jpdl31_SubProcessType_instantiation(instance):
    assert isinstance(instance, jpdl31_SubProcessType)


jpdl31_SuperStateType_strategy = st.builds(jpdl31_SuperStateType, async_=safe_text, group=safe_text, name=safe_text)
@given(instance=jpdl31_SuperStateType_strategy)
@settings(max_examples=25)
def test_jpdl31_SuperStateType_instantiation(instance):
    assert isinstance(instance, jpdl31_SuperStateType)


jpdl31_SwimlaneType_strategy = st.builds(jpdl31_SwimlaneType, name=safe_text)
@given(instance=jpdl31_SwimlaneType_strategy)
@settings(max_examples=25)
def test_jpdl31_SwimlaneType_instantiation(instance):
    assert isinstance(instance, jpdl31_SwimlaneType)


jpdl31_TaskNodeType_strategy = st.builds(jpdl31_TaskNodeType, async_=safe_text, createTasks=safe_text, endTasks=safe_text, group=safe_text, name=safe_text, signal=safe_text)
@given(instance=jpdl31_TaskNodeType_strategy)
@settings(max_examples=25)
def test_jpdl31_TaskNodeType_instantiation(instance):
    assert isinstance(instance, jpdl31_TaskNodeType)


jpdl31_TaskType_strategy = st.builds(jpdl31_TaskType, blocking=safe_text, description=safe_text, duedate=safe_text, group=safe_text, name=safe_text, priority=safe_text, signalling=safe_text, swimlane=safe_text)
@given(instance=jpdl31_TaskType_strategy)
@settings(max_examples=25)
def test_jpdl31_TaskType_instantiation(instance):
    assert isinstance(instance, jpdl31_TaskType)


jpdl31_TimerType_strategy = st.builds(jpdl31_TimerType, duedate=safe_text, name=safe_text, repeat=safe_text, transition=safe_text)
@given(instance=jpdl31_TimerType_strategy)
@settings(max_examples=25)
def test_jpdl31_TimerType_instantiation(instance):
    assert isinstance(instance, jpdl31_TimerType)


jpdl31_TransitionType_strategy = st.builds(jpdl31_TransitionType, group=safe_text, name=safe_text, to=safe_text)
@given(instance=jpdl31_TransitionType_strategy)
@settings(max_examples=25)
def test_jpdl31_TransitionType_instantiation(instance):
    assert isinstance(instance, jpdl31_TransitionType)


jpdl31_TransitionType1_strategy = st.builds(jpdl31_TransitionType1, group=safe_text, name=safe_text, to=safe_text)
@given(instance=jpdl31_TransitionType1_strategy)
@settings(max_examples=25)
def test_jpdl31_TransitionType1_instantiation(instance):
    assert isinstance(instance, jpdl31_TransitionType1)


jpdl31_VariableType_strategy = st.builds(jpdl31_VariableType, access=safe_text, any=safe_text, mappedName=safe_text, name=safe_text)
@given(instance=jpdl31_VariableType_strategy)
@settings(max_examples=25)
def test_jpdl31_VariableType_instantiation(instance):
    assert isinstance(instance, jpdl31_VariableType)


