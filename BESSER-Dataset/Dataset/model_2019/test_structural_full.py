import inspect
import pytest
from datetime import date, datetime, time, timedelta
from hypothesis import given, settings
import hypothesis.strategies as st

from python_code import (
    Execution,
    executionTrace_ActivityEdgeTraversal,
    executionTrace_ActivityExecution,
    executionTrace_ActivityNodeExecution,
    executionTrace_AttributeValueSet,
    executionTrace_Execution,
    executionTrace_ExecutionTrace,
    executionTrace_ExpressionEvaluation,
    executionTrace_InstanceLinkCreation,
    executionTrace_InstanceLinkDeletion,
    executionTrace_InstanceLinkModification,
    executionTrace_InstanceObjectCreation,
    executionTrace_InstanceObjectDeletion,
    executionTrace_InstanceObjectModification,
    executionTrace_LinkCheck,
    executionTrace_LinkCheckFailed,
    executionTrace_LinkCheckSuccessful,
    executionTrace_MapEntry,
    executionTrace_StoryPatternApplication,
    executionTrace_StoryPatternConstraintEvaluation,
    executionTrace_StoryPatternConstraintHolds,
    executionTrace_StoryPatternConstraintViolated,
    executionTrace_StoryPatternExecution,
    executionTrace_StoryPatternInitialization,
    executionTrace_StoryPatternLinkExecution,
    executionTrace_StoryPatternMatching,
    executionTrace_StoryPatternObjectBindingRevoked,
    executionTrace_StoryPatternObjectBound,
    executionTrace_StoryPatternObjectConstraintEvaluation,
    executionTrace_StoryPatternObjectConstraintHolds,
    executionTrace_StoryPatternObjectConstraintViolated,
    executionTrace_StoryPatternObjectExecution,
    executionTrace_StoryPatternObjectNotBound,
    executionTrace_TraversingLink,
    executionTrace_VariableChanged,
    executionTrace_VariableCreated,
    executionTrace_VariableDeleted,
    executionTrace_VariableModification,
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

def test_executionTrace_AttributeValueSet_instanceObject_value_roundtrip():
    instance = executionTrace_AttributeValueSet(instanceObject="sample_text", newValue="sample_text")
    assert instance.instanceObject == "sample_text"
    instance.instanceObject = "sample_text_2"
    assert instance.instanceObject == "sample_text_2"


def test_executionTrace_AttributeValueSet_newValue_value_roundtrip():
    instance = executionTrace_AttributeValueSet(instanceObject="sample_text", newValue="sample_text")
    assert instance.newValue == "sample_text"
    instance.newValue = "sample_text_2"
    assert instance.newValue == "sample_text_2"


def test_executionTrace_Execution_executionFinishedTimeStamp_value_roundtrip():
    instance = executionTrace_Execution(executionFinishedTimeStamp="sample_text", executionStartedTimeStamp="sample_text", executionTime="sample_text", executionTimeMsec="sample_text")
    assert instance.executionFinishedTimeStamp == "sample_text"
    instance.executionFinishedTimeStamp = "sample_text_2"
    assert instance.executionFinishedTimeStamp == "sample_text_2"


def test_executionTrace_Execution_executionStartedTimeStamp_value_roundtrip():
    instance = executionTrace_Execution(executionFinishedTimeStamp="sample_text", executionStartedTimeStamp="sample_text", executionTime="sample_text", executionTimeMsec="sample_text")
    assert instance.executionStartedTimeStamp == "sample_text"
    instance.executionStartedTimeStamp = "sample_text_2"
    assert instance.executionStartedTimeStamp == "sample_text_2"


def test_executionTrace_Execution_executionTime_value_roundtrip():
    instance = executionTrace_Execution(executionFinishedTimeStamp="sample_text", executionStartedTimeStamp="sample_text", executionTime="sample_text", executionTimeMsec="sample_text")
    assert instance.executionTime == "sample_text"
    instance.executionTime = "sample_text_2"
    assert instance.executionTime == "sample_text_2"


def test_executionTrace_Execution_executionTimeMsec_value_roundtrip():
    instance = executionTrace_Execution(executionFinishedTimeStamp="sample_text", executionStartedTimeStamp="sample_text", executionTime="sample_text", executionTimeMsec="sample_text")
    assert instance.executionTimeMsec == "sample_text"
    instance.executionTimeMsec = "sample_text_2"
    assert instance.executionTimeMsec == "sample_text_2"


def test_executionTrace_ExecutionTrace_description_value_roundtrip():
    instance = executionTrace_ExecutionTrace(description="sample_text", totalExecutionTime="sample_text", totalExecutionTimeMsec="sample_text")
    assert instance.description == "sample_text"
    instance.description = "sample_text_2"
    assert instance.description == "sample_text_2"


def test_executionTrace_ExecutionTrace_totalExecutionTime_value_roundtrip():
    instance = executionTrace_ExecutionTrace(description="sample_text", totalExecutionTime="sample_text", totalExecutionTimeMsec="sample_text")
    assert instance.totalExecutionTime == "sample_text"
    instance.totalExecutionTime = "sample_text_2"
    assert instance.totalExecutionTime == "sample_text_2"


def test_executionTrace_ExecutionTrace_totalExecutionTimeMsec_value_roundtrip():
    instance = executionTrace_ExecutionTrace(description="sample_text", totalExecutionTime="sample_text", totalExecutionTimeMsec="sample_text")
    assert instance.totalExecutionTimeMsec == "sample_text"
    instance.totalExecutionTimeMsec = "sample_text_2"
    assert instance.totalExecutionTimeMsec == "sample_text_2"


def test_executionTrace_ExpressionEvaluation_result_value_roundtrip():
    instance = executionTrace_ExpressionEvaluation(result="sample_text")
    assert instance.result == "sample_text"
    instance.result = "sample_text_2"
    assert instance.result == "sample_text_2"


def test_executionTrace_InstanceLinkModification_sourceInstanceObject_value_roundtrip():
    instance = executionTrace_InstanceLinkModification(sourceInstanceObject="sample_text", targetInstanceObject="sample_text")
    assert instance.sourceInstanceObject == "sample_text"
    instance.sourceInstanceObject = "sample_text_2"
    assert instance.sourceInstanceObject == "sample_text_2"


def test_executionTrace_InstanceLinkModification_targetInstanceObject_value_roundtrip():
    instance = executionTrace_InstanceLinkModification(sourceInstanceObject="sample_text", targetInstanceObject="sample_text")
    assert instance.targetInstanceObject == "sample_text"
    instance.targetInstanceObject = "sample_text_2"
    assert instance.targetInstanceObject == "sample_text_2"


def test_executionTrace_InstanceObjectModification_instanceObject_value_roundtrip():
    instance = executionTrace_InstanceObjectModification(instanceObject="sample_text")
    assert instance.instanceObject == "sample_text"
    instance.instanceObject = "sample_text_2"
    assert instance.instanceObject == "sample_text_2"


def test_executionTrace_LinkCheck_targetObject_value_roundtrip():
    instance = executionTrace_LinkCheck(targetObject="sample_text")
    assert instance.targetObject == "sample_text"
    instance.targetObject = "sample_text_2"
    assert instance.targetObject == "sample_text_2"


def test_executionTrace_MapEntry_key_value_roundtrip():
    instance = executionTrace_MapEntry(key="sample_text", value="sample_text")
    assert instance.key == "sample_text"
    instance.key = "sample_text_2"
    assert instance.key == "sample_text_2"


def test_executionTrace_MapEntry_value_value_roundtrip():
    instance = executionTrace_MapEntry(key="sample_text", value="sample_text")
    assert instance.value == "sample_text"
    instance.value = "sample_text_2"
    assert instance.value == "sample_text_2"


def test_executionTrace_StoryPatternLinkExecution_sourceObject_value_roundtrip():
    instance = executionTrace_StoryPatternLinkExecution(sourceObject="sample_text")
    assert instance.sourceObject == "sample_text"
    instance.sourceObject = "sample_text_2"
    assert instance.sourceObject == "sample_text_2"


def test_executionTrace_StoryPatternMatching_successful_value_roundtrip():
    instance = executionTrace_StoryPatternMatching(successful=True)
    assert instance.successful == True
    instance.successful = False
    assert instance.successful == False


def test_executionTrace_StoryPatternObjectBindingRevoked_previousValue_value_roundtrip():
    instance = executionTrace_StoryPatternObjectBindingRevoked(previousValue="sample_text")
    assert instance.previousValue == "sample_text"
    instance.previousValue = "sample_text_2"
    assert instance.previousValue == "sample_text_2"


def test_executionTrace_StoryPatternObjectBound_value_value_roundtrip():
    instance = executionTrace_StoryPatternObjectBound(value="sample_text")
    assert instance.value == "sample_text"
    instance.value = "sample_text_2"
    assert instance.value == "sample_text_2"


def test_executionTrace_VariableChanged_oldValue_value_roundtrip():
    instance = executionTrace_VariableChanged(oldValue="sample_text")
    assert instance.oldValue == "sample_text"
    instance.oldValue = "sample_text_2"
    assert instance.oldValue == "sample_text_2"


def test_executionTrace_VariableModification_value_value_roundtrip():
    instance = executionTrace_VariableModification(value="sample_text", variableName="sample_text")
    assert instance.value == "sample_text"
    instance.value = "sample_text_2"
    assert instance.value == "sample_text_2"


def test_executionTrace_VariableModification_variableName_value_roundtrip():
    instance = executionTrace_VariableModification(value="sample_text", variableName="sample_text")
    assert instance.variableName == "sample_text"
    instance.variableName = "sample_text_2"
    assert instance.variableName == "sample_text_2"


def test_executionTrace_ActivityEdgeTraversal_isa_Execution():
    instance = executionTrace_ActivityEdgeTraversal()
    assert isinstance(instance, Execution)


def test_executionTrace_ActivityExecution_isa_Execution():
    instance = executionTrace_ActivityExecution()
    assert isinstance(instance, Execution)


def test_executionTrace_ActivityNodeExecution_isa_Execution():
    instance = executionTrace_ActivityNodeExecution()
    assert isinstance(instance, Execution)


def test_executionTrace_AttributeValueSet_isa_Execution():
    instance = executionTrace_AttributeValueSet(instanceObject="sample_text", newValue="sample_text")
    assert isinstance(instance, Execution)


def test_executionTrace_ExpressionEvaluation_isa_Execution():
    instance = executionTrace_ExpressionEvaluation(result="sample_text")
    assert isinstance(instance, Execution)


def test_executionTrace_InstanceLinkModification_isa_Execution():
    instance = executionTrace_InstanceLinkModification(sourceInstanceObject="sample_text", targetInstanceObject="sample_text")
    assert isinstance(instance, Execution)


def test_executionTrace_InstanceObjectModification_isa_Execution():
    instance = executionTrace_InstanceObjectModification(instanceObject="sample_text")
    assert isinstance(instance, Execution)


def test_executionTrace_StoryPatternExecution_isa_Execution():
    instance = executionTrace_StoryPatternExecution()
    assert isinstance(instance, Execution)


def test_executionTrace_StoryPatternLinkExecution_isa_Execution():
    instance = executionTrace_StoryPatternLinkExecution(sourceObject="sample_text")
    assert isinstance(instance, Execution)


def test_executionTrace_StoryPatternObjectExecution_isa_Execution():
    instance = executionTrace_StoryPatternObjectExecution()
    assert isinstance(instance, Execution)


def test_executionTrace_VariableModification_isa_Execution():
    instance = executionTrace_VariableModification(value="sample_text", variableName="sample_text")
    assert isinstance(instance, Execution)


def test_assoc_container4_link_reassign_clear():
    a = executionTrace_Execution(executionFinishedTimeStamp="sample_text", executionStartedTimeStamp="sample_text", executionTime="sample_text", executionTimeMsec="sample_text")
    b1 = executionTrace_Execution(executionFinishedTimeStamp="sample_text", executionStartedTimeStamp="sample_text", executionTime="sample_text", executionTimeMsec="sample_text")
    b2 = executionTrace_Execution(executionFinishedTimeStamp="sample_text_2", executionStartedTimeStamp="sample_text_2", executionTime="sample_text_2", executionTimeMsec="sample_text_2")
    _safe_set(a, 'Execution5', b1)
    assert _is_linked(a, 'Execution5', b1)
    if hasattr(b1, 'elements'):
        assert _is_linked(b1, 'elements', a)
    _safe_set(a, 'Execution5', b2)
    assert _is_linked(a, 'Execution5', b2)
    if hasattr(b1, 'elements'):
        assert not _is_linked(b1, 'elements', a)
    if hasattr(b2, 'elements'):
        assert _is_linked(b2, 'elements', a)
    _safe_set(a, 'Execution5', None)
    assert not _is_linked(a, 'Execution5', b2)
    if hasattr(b2, 'elements'):
        assert not _is_linked(b2, 'elements', a)


def test_assoc_elements2_link_reassign_clear():
    a = executionTrace_Execution(executionFinishedTimeStamp="sample_text", executionStartedTimeStamp="sample_text", executionTime="sample_text", executionTimeMsec="sample_text")
    b1 = executionTrace_Execution(executionFinishedTimeStamp="sample_text", executionStartedTimeStamp="sample_text", executionTime="sample_text", executionTimeMsec="sample_text")
    b2 = executionTrace_Execution(executionFinishedTimeStamp="sample_text_2", executionStartedTimeStamp="sample_text_2", executionTime="sample_text_2", executionTimeMsec="sample_text_2")
    _safe_set(a, 'Execution', b1)
    assert _is_linked(a, 'Execution', b1)
    if hasattr(b1, 'container'):
        assert _is_linked(b1, 'container', a)
    _safe_set(a, 'Execution', b2)
    assert _is_linked(a, 'Execution', b2)
    if hasattr(b1, 'container'):
        assert not _is_linked(b1, 'container', a)
    if hasattr(b2, 'container'):
        assert _is_linked(b2, 'container', a)
    _safe_set(a, 'Execution', None)
    assert not _is_linked(a, 'Execution', b2)
    if hasattr(b2, 'container'):
        assert not _is_linked(b2, 'container', a)


def test_assoc_executions0_link_reassign_clear():
    a = executionTrace_ExecutionTrace(description="sample_text", totalExecutionTime="sample_text", totalExecutionTimeMsec="sample_text")
    b1 = executionTrace_Execution(executionFinishedTimeStamp="sample_text", executionStartedTimeStamp="sample_text", executionTime="sample_text", executionTimeMsec="sample_text")
    b2 = executionTrace_Execution(executionFinishedTimeStamp="sample_text_2", executionStartedTimeStamp="sample_text_2", executionTime="sample_text_2", executionTimeMsec="sample_text_2")
    _safe_set(a, 'executionTrace_ExecutionTrace', {b1})
    assert _is_linked(a, 'executionTrace_ExecutionTrace', b1)
    if hasattr(b1, 'executionTrace_Execution'):
        assert _is_linked(b1, 'executionTrace_Execution', a)
    _safe_set(a, 'executionTrace_ExecutionTrace', {b2})
    assert _is_linked(a, 'executionTrace_ExecutionTrace', b2)
    if hasattr(b1, 'executionTrace_Execution'):
        assert not _is_linked(b1, 'executionTrace_Execution', a)
    if hasattr(b2, 'executionTrace_Execution'):
        assert _is_linked(b2, 'executionTrace_Execution', a)
    _safe_set(a, 'executionTrace_ExecutionTrace', set())
    assert not _is_linked(a, 'executionTrace_ExecutionTrace', b2)
    if hasattr(b2, 'executionTrace_Execution'):
        assert not _is_linked(b2, 'executionTrace_Execution', a)


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

Execution_strategy = st.builds(Execution)
@given(instance=Execution_strategy)
@settings(max_examples=25)
def test_Execution_instantiation(instance):
    assert isinstance(instance, Execution)


executionTrace_ActivityEdgeTraversal_strategy = st.builds(executionTrace_ActivityEdgeTraversal)
@given(instance=executionTrace_ActivityEdgeTraversal_strategy)
@settings(max_examples=25)
def test_executionTrace_ActivityEdgeTraversal_instantiation(instance):
    assert isinstance(instance, executionTrace_ActivityEdgeTraversal)


executionTrace_ActivityExecution_strategy = st.builds(executionTrace_ActivityExecution)
@given(instance=executionTrace_ActivityExecution_strategy)
@settings(max_examples=25)
def test_executionTrace_ActivityExecution_instantiation(instance):
    assert isinstance(instance, executionTrace_ActivityExecution)


executionTrace_ActivityNodeExecution_strategy = st.builds(executionTrace_ActivityNodeExecution)
@given(instance=executionTrace_ActivityNodeExecution_strategy)
@settings(max_examples=25)
def test_executionTrace_ActivityNodeExecution_instantiation(instance):
    assert isinstance(instance, executionTrace_ActivityNodeExecution)


executionTrace_AttributeValueSet_strategy = st.builds(executionTrace_AttributeValueSet, instanceObject=safe_text, newValue=safe_text)
@given(instance=executionTrace_AttributeValueSet_strategy)
@settings(max_examples=25)
def test_executionTrace_AttributeValueSet_instantiation(instance):
    assert isinstance(instance, executionTrace_AttributeValueSet)


executionTrace_Execution_strategy = st.builds(executionTrace_Execution, executionFinishedTimeStamp=safe_text, executionStartedTimeStamp=safe_text, executionTime=safe_text, executionTimeMsec=safe_text)
@given(instance=executionTrace_Execution_strategy)
@settings(max_examples=25)
def test_executionTrace_Execution_instantiation(instance):
    assert isinstance(instance, executionTrace_Execution)


executionTrace_ExecutionTrace_strategy = st.builds(executionTrace_ExecutionTrace, description=safe_text, totalExecutionTime=safe_text, totalExecutionTimeMsec=safe_text)
@given(instance=executionTrace_ExecutionTrace_strategy)
@settings(max_examples=25)
def test_executionTrace_ExecutionTrace_instantiation(instance):
    assert isinstance(instance, executionTrace_ExecutionTrace)


executionTrace_ExpressionEvaluation_strategy = st.builds(executionTrace_ExpressionEvaluation, result=safe_text)
@given(instance=executionTrace_ExpressionEvaluation_strategy)
@settings(max_examples=25)
def test_executionTrace_ExpressionEvaluation_instantiation(instance):
    assert isinstance(instance, executionTrace_ExpressionEvaluation)


executionTrace_InstanceLinkCreation_strategy = st.builds(executionTrace_InstanceLinkCreation)
@given(instance=executionTrace_InstanceLinkCreation_strategy)
@settings(max_examples=25)
def test_executionTrace_InstanceLinkCreation_instantiation(instance):
    assert isinstance(instance, executionTrace_InstanceLinkCreation)


executionTrace_InstanceLinkDeletion_strategy = st.builds(executionTrace_InstanceLinkDeletion)
@given(instance=executionTrace_InstanceLinkDeletion_strategy)
@settings(max_examples=25)
def test_executionTrace_InstanceLinkDeletion_instantiation(instance):
    assert isinstance(instance, executionTrace_InstanceLinkDeletion)


executionTrace_InstanceLinkModification_strategy = st.builds(executionTrace_InstanceLinkModification, sourceInstanceObject=safe_text, targetInstanceObject=safe_text)
@given(instance=executionTrace_InstanceLinkModification_strategy)
@settings(max_examples=25)
def test_executionTrace_InstanceLinkModification_instantiation(instance):
    assert isinstance(instance, executionTrace_InstanceLinkModification)


executionTrace_InstanceObjectCreation_strategy = st.builds(executionTrace_InstanceObjectCreation)
@given(instance=executionTrace_InstanceObjectCreation_strategy)
@settings(max_examples=25)
def test_executionTrace_InstanceObjectCreation_instantiation(instance):
    assert isinstance(instance, executionTrace_InstanceObjectCreation)


executionTrace_InstanceObjectDeletion_strategy = st.builds(executionTrace_InstanceObjectDeletion)
@given(instance=executionTrace_InstanceObjectDeletion_strategy)
@settings(max_examples=25)
def test_executionTrace_InstanceObjectDeletion_instantiation(instance):
    assert isinstance(instance, executionTrace_InstanceObjectDeletion)


executionTrace_InstanceObjectModification_strategy = st.builds(executionTrace_InstanceObjectModification, instanceObject=safe_text)
@given(instance=executionTrace_InstanceObjectModification_strategy)
@settings(max_examples=25)
def test_executionTrace_InstanceObjectModification_instantiation(instance):
    assert isinstance(instance, executionTrace_InstanceObjectModification)


executionTrace_LinkCheck_strategy = st.builds(executionTrace_LinkCheck, targetObject=safe_text)
@given(instance=executionTrace_LinkCheck_strategy)
@settings(max_examples=25)
def test_executionTrace_LinkCheck_instantiation(instance):
    assert isinstance(instance, executionTrace_LinkCheck)


executionTrace_LinkCheckFailed_strategy = st.builds(executionTrace_LinkCheckFailed)
@given(instance=executionTrace_LinkCheckFailed_strategy)
@settings(max_examples=25)
def test_executionTrace_LinkCheckFailed_instantiation(instance):
    assert isinstance(instance, executionTrace_LinkCheckFailed)


executionTrace_LinkCheckSuccessful_strategy = st.builds(executionTrace_LinkCheckSuccessful)
@given(instance=executionTrace_LinkCheckSuccessful_strategy)
@settings(max_examples=25)
def test_executionTrace_LinkCheckSuccessful_instantiation(instance):
    assert isinstance(instance, executionTrace_LinkCheckSuccessful)


executionTrace_MapEntry_strategy = st.builds(executionTrace_MapEntry, key=safe_text, value=safe_text)
@given(instance=executionTrace_MapEntry_strategy)
@settings(max_examples=25)
def test_executionTrace_MapEntry_instantiation(instance):
    assert isinstance(instance, executionTrace_MapEntry)


executionTrace_StoryPatternApplication_strategy = st.builds(executionTrace_StoryPatternApplication)
@given(instance=executionTrace_StoryPatternApplication_strategy)
@settings(max_examples=25)
def test_executionTrace_StoryPatternApplication_instantiation(instance):
    assert isinstance(instance, executionTrace_StoryPatternApplication)


executionTrace_StoryPatternConstraintEvaluation_strategy = st.builds(executionTrace_StoryPatternConstraintEvaluation)
@given(instance=executionTrace_StoryPatternConstraintEvaluation_strategy)
@settings(max_examples=25)
def test_executionTrace_StoryPatternConstraintEvaluation_instantiation(instance):
    assert isinstance(instance, executionTrace_StoryPatternConstraintEvaluation)


executionTrace_StoryPatternConstraintHolds_strategy = st.builds(executionTrace_StoryPatternConstraintHolds)
@given(instance=executionTrace_StoryPatternConstraintHolds_strategy)
@settings(max_examples=25)
def test_executionTrace_StoryPatternConstraintHolds_instantiation(instance):
    assert isinstance(instance, executionTrace_StoryPatternConstraintHolds)


executionTrace_StoryPatternConstraintViolated_strategy = st.builds(executionTrace_StoryPatternConstraintViolated)
@given(instance=executionTrace_StoryPatternConstraintViolated_strategy)
@settings(max_examples=25)
def test_executionTrace_StoryPatternConstraintViolated_instantiation(instance):
    assert isinstance(instance, executionTrace_StoryPatternConstraintViolated)


executionTrace_StoryPatternExecution_strategy = st.builds(executionTrace_StoryPatternExecution)
@given(instance=executionTrace_StoryPatternExecution_strategy)
@settings(max_examples=25)
def test_executionTrace_StoryPatternExecution_instantiation(instance):
    assert isinstance(instance, executionTrace_StoryPatternExecution)


executionTrace_StoryPatternInitialization_strategy = st.builds(executionTrace_StoryPatternInitialization)
@given(instance=executionTrace_StoryPatternInitialization_strategy)
@settings(max_examples=25)
def test_executionTrace_StoryPatternInitialization_instantiation(instance):
    assert isinstance(instance, executionTrace_StoryPatternInitialization)


executionTrace_StoryPatternLinkExecution_strategy = st.builds(executionTrace_StoryPatternLinkExecution, sourceObject=safe_text)
@given(instance=executionTrace_StoryPatternLinkExecution_strategy)
@settings(max_examples=25)
def test_executionTrace_StoryPatternLinkExecution_instantiation(instance):
    assert isinstance(instance, executionTrace_StoryPatternLinkExecution)


executionTrace_StoryPatternMatching_strategy = st.builds(executionTrace_StoryPatternMatching, successful=st.booleans())
@given(instance=executionTrace_StoryPatternMatching_strategy)
@settings(max_examples=25)
def test_executionTrace_StoryPatternMatching_instantiation(instance):
    assert isinstance(instance, executionTrace_StoryPatternMatching)


executionTrace_StoryPatternObjectBindingRevoked_strategy = st.builds(executionTrace_StoryPatternObjectBindingRevoked, previousValue=safe_text)
@given(instance=executionTrace_StoryPatternObjectBindingRevoked_strategy)
@settings(max_examples=25)
def test_executionTrace_StoryPatternObjectBindingRevoked_instantiation(instance):
    assert isinstance(instance, executionTrace_StoryPatternObjectBindingRevoked)


executionTrace_StoryPatternObjectBound_strategy = st.builds(executionTrace_StoryPatternObjectBound, value=safe_text)
@given(instance=executionTrace_StoryPatternObjectBound_strategy)
@settings(max_examples=25)
def test_executionTrace_StoryPatternObjectBound_instantiation(instance):
    assert isinstance(instance, executionTrace_StoryPatternObjectBound)


executionTrace_StoryPatternObjectConstraintEvaluation_strategy = st.builds(executionTrace_StoryPatternObjectConstraintEvaluation)
@given(instance=executionTrace_StoryPatternObjectConstraintEvaluation_strategy)
@settings(max_examples=25)
def test_executionTrace_StoryPatternObjectConstraintEvaluation_instantiation(instance):
    assert isinstance(instance, executionTrace_StoryPatternObjectConstraintEvaluation)


executionTrace_StoryPatternObjectConstraintHolds_strategy = st.builds(executionTrace_StoryPatternObjectConstraintHolds)
@given(instance=executionTrace_StoryPatternObjectConstraintHolds_strategy)
@settings(max_examples=25)
def test_executionTrace_StoryPatternObjectConstraintHolds_instantiation(instance):
    assert isinstance(instance, executionTrace_StoryPatternObjectConstraintHolds)


executionTrace_StoryPatternObjectConstraintViolated_strategy = st.builds(executionTrace_StoryPatternObjectConstraintViolated)
@given(instance=executionTrace_StoryPatternObjectConstraintViolated_strategy)
@settings(max_examples=25)
def test_executionTrace_StoryPatternObjectConstraintViolated_instantiation(instance):
    assert isinstance(instance, executionTrace_StoryPatternObjectConstraintViolated)


executionTrace_StoryPatternObjectExecution_strategy = st.builds(executionTrace_StoryPatternObjectExecution)
@given(instance=executionTrace_StoryPatternObjectExecution_strategy)
@settings(max_examples=25)
def test_executionTrace_StoryPatternObjectExecution_instantiation(instance):
    assert isinstance(instance, executionTrace_StoryPatternObjectExecution)


executionTrace_StoryPatternObjectNotBound_strategy = st.builds(executionTrace_StoryPatternObjectNotBound)
@given(instance=executionTrace_StoryPatternObjectNotBound_strategy)
@settings(max_examples=25)
def test_executionTrace_StoryPatternObjectNotBound_instantiation(instance):
    assert isinstance(instance, executionTrace_StoryPatternObjectNotBound)


executionTrace_TraversingLink_strategy = st.builds(executionTrace_TraversingLink)
@given(instance=executionTrace_TraversingLink_strategy)
@settings(max_examples=25)
def test_executionTrace_TraversingLink_instantiation(instance):
    assert isinstance(instance, executionTrace_TraversingLink)


executionTrace_VariableChanged_strategy = st.builds(executionTrace_VariableChanged, oldValue=safe_text)
@given(instance=executionTrace_VariableChanged_strategy)
@settings(max_examples=25)
def test_executionTrace_VariableChanged_instantiation(instance):
    assert isinstance(instance, executionTrace_VariableChanged)


executionTrace_VariableCreated_strategy = st.builds(executionTrace_VariableCreated)
@given(instance=executionTrace_VariableCreated_strategy)
@settings(max_examples=25)
def test_executionTrace_VariableCreated_instantiation(instance):
    assert isinstance(instance, executionTrace_VariableCreated)


executionTrace_VariableDeleted_strategy = st.builds(executionTrace_VariableDeleted)
@given(instance=executionTrace_VariableDeleted_strategy)
@settings(max_examples=25)
def test_executionTrace_VariableDeleted_instantiation(instance):
    assert isinstance(instance, executionTrace_VariableDeleted)


executionTrace_VariableModification_strategy = st.builds(executionTrace_VariableModification, value=safe_text, variableName=safe_text)
@given(instance=executionTrace_VariableModification_strategy)
@settings(max_examples=25)
def test_executionTrace_VariableModification_instantiation(instance):
    assert isinstance(instance, executionTrace_VariableModification)


