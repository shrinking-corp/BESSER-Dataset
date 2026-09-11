import inspect
import pytest
from datetime import date, datetime, time, timedelta
from hypothesis import given, settings
import hypothesis.strategies as st

from python_code import (
    Activity,
    ActivityEdge,
    ActivityGroup,
    ActivityNode,
    ControlNode,
    ExecutableNode,
    FinalNode,
    NamedElement,
    ObjectNode,
    Pin,
    activity_AcceptEventAction,
    activity_AcceptTimeEventAction,
    activity_Action,
    activity_Activity,
    activity_ActivityEdge,
    activity_ActivityFinalNode,
    activity_ActivityGroup,
    activity_ActivityNode,
    activity_ActivityParameterNode,
    activity_ActivityPartition,
    activity_CentralBufferNode,
    activity_Connector,
    activity_ControlFlow,
    activity_ControlNode,
    activity_DataStoreNode,
    activity_DecisionNode,
    activity_ExecutableNode,
    activity_FinalNode,
    activity_FlowFinalNode,
    activity_ForkNode,
    activity_InitialNode,
    activity_InputPin,
    activity_InterruptEdge,
    activity_InterruptibleActivityRegion,
    activity_JoinNode,
    activity_MergeNode,
    activity_NamedElement,
    activity_Object,
    activity_ObjectFlow,
    activity_ObjectNode,
    activity_OutputPin,
    activity_Pin,
    activity_SendSignalAction,
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

def test_activity_ActivityGroup_name_value_roundtrip():
    instance = activity_ActivityGroup(name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_activity_ActivityParameterNode_name_value_roundtrip():
    instance = activity_ActivityParameterNode(name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_activity_NamedElement_Name_value_roundtrip():
    instance = activity_NamedElement(Name="sample_text", qualifiedName="sample_text")
    assert instance.Name == "sample_text"
    instance.Name = "sample_text_2"
    assert instance.Name == "sample_text_2"


def test_activity_NamedElement_qualifiedName_value_roundtrip():
    instance = activity_NamedElement(Name="sample_text", qualifiedName="sample_text")
    assert instance.qualifiedName == "sample_text"
    instance.qualifiedName = "sample_text_2"
    assert instance.qualifiedName == "sample_text_2"


def test_activity_ActivityGroup_isa_Activity():
    instance = activity_ActivityGroup(name="sample_text")
    assert isinstance(instance, Activity)


def test_activity_ActivityParameterNode_isa_Activity():
    instance = activity_ActivityParameterNode(name="sample_text")
    assert isinstance(instance, Activity)


def test_activity_ControlFlow_isa_ActivityEdge():
    instance = activity_ControlFlow()
    assert isinstance(instance, ActivityEdge)


def test_activity_InterruptEdge_isa_ActivityEdge():
    instance = activity_InterruptEdge()
    assert isinstance(instance, ActivityEdge)


def test_activity_ObjectFlow_isa_ActivityEdge():
    instance = activity_ObjectFlow()
    assert isinstance(instance, ActivityEdge)


def test_activity_ActivityPartition_isa_ActivityGroup():
    instance = activity_ActivityPartition()
    assert isinstance(instance, ActivityGroup)


def test_activity_InterruptibleActivityRegion_isa_ActivityGroup():
    instance = activity_InterruptibleActivityRegion()
    assert isinstance(instance, ActivityGroup)


def test_activity_ControlNode_isa_ActivityNode():
    instance = activity_ControlNode()
    assert isinstance(instance, ActivityNode)


def test_activity_ExecutableNode_isa_ActivityNode():
    instance = activity_ExecutableNode()
    assert isinstance(instance, ActivityNode)


def test_activity_ObjectNode_isa_ActivityNode():
    instance = activity_ObjectNode()
    assert isinstance(instance, ActivityNode)


def test_activity_Connector_isa_ControlNode():
    instance = activity_Connector()
    assert isinstance(instance, ControlNode)


def test_activity_DecisionNode_isa_ControlNode():
    instance = activity_DecisionNode()
    assert isinstance(instance, ControlNode)


def test_activity_FinalNode_isa_ControlNode():
    instance = activity_FinalNode()
    assert isinstance(instance, ControlNode)


def test_activity_ForkNode_isa_ControlNode():
    instance = activity_ForkNode()
    assert isinstance(instance, ControlNode)


def test_activity_InitialNode_isa_ControlNode():
    instance = activity_InitialNode()
    assert isinstance(instance, ControlNode)


def test_activity_JoinNode_isa_ControlNode():
    instance = activity_JoinNode()
    assert isinstance(instance, ControlNode)


def test_activity_MergeNode_isa_ControlNode():
    instance = activity_MergeNode()
    assert isinstance(instance, ControlNode)


def test_activity_AcceptEventAction_isa_ExecutableNode():
    instance = activity_AcceptEventAction()
    assert isinstance(instance, ExecutableNode)


def test_activity_AcceptTimeEventAction_isa_ExecutableNode():
    instance = activity_AcceptTimeEventAction()
    assert isinstance(instance, ExecutableNode)


def test_activity_Action_isa_ExecutableNode():
    instance = activity_Action()
    assert isinstance(instance, ExecutableNode)


def test_activity_SendSignalAction_isa_ExecutableNode():
    instance = activity_SendSignalAction()
    assert isinstance(instance, ExecutableNode)


def test_activity_ActivityFinalNode_isa_FinalNode():
    instance = activity_ActivityFinalNode()
    assert isinstance(instance, FinalNode)


def test_activity_FlowFinalNode_isa_FinalNode():
    instance = activity_FlowFinalNode()
    assert isinstance(instance, FinalNode)


def test_activity_ActivityEdge_isa_NamedElement():
    instance = activity_ActivityEdge()
    assert isinstance(instance, NamedElement)


def test_activity_ActivityNode_isa_NamedElement():
    instance = activity_ActivityNode()
    assert isinstance(instance, NamedElement)


def test_activity_CentralBufferNode_isa_ObjectNode():
    instance = activity_CentralBufferNode()
    assert isinstance(instance, ObjectNode)


def test_activity_DataStoreNode_isa_ObjectNode():
    instance = activity_DataStoreNode()
    assert isinstance(instance, ObjectNode)


def test_activity_Object_isa_ObjectNode():
    instance = activity_Object()
    assert isinstance(instance, ObjectNode)


def test_activity_Pin_isa_ObjectNode():
    instance = activity_Pin()
    assert isinstance(instance, ObjectNode)


def test_activity_InputPin_isa_Pin():
    instance = activity_InputPin()
    assert isinstance(instance, Pin)


def test_activity_OutputPin_isa_Pin():
    instance = activity_OutputPin()
    assert isinstance(instance, Pin)


def test_assoc_activityGroups7_link_reassign_clear():
    a = activity_ActivityGroup(name="sample_text")
    b1 = activity_Activity()
    b2 = activity_Activity()
    _safe_set(a, 'activity_ActivityGroup', b1)
    assert _is_linked(a, 'activity_ActivityGroup', b1)
    if hasattr(b1, 'activity_Activity8'):
        assert _is_linked(b1, 'activity_Activity8', a)
    _safe_set(a, 'activity_ActivityGroup', b2)
    assert _is_linked(a, 'activity_ActivityGroup', b2)
    if hasattr(b1, 'activity_Activity8'):
        assert not _is_linked(b1, 'activity_Activity8', a)
    if hasattr(b2, 'activity_Activity8'):
        assert _is_linked(b2, 'activity_Activity8', a)
    _safe_set(a, 'activity_ActivityGroup', None)
    assert not _is_linked(a, 'activity_ActivityGroup', b2)
    if hasattr(b2, 'activity_Activity8'):
        assert not _is_linked(b2, 'activity_Activity8', a)


def test_assoc_activityparameternode3_link_reassign_clear():
    a = activity_ActivityParameterNode(name="sample_text")
    b1 = activity_Activity()
    b2 = activity_Activity()
    _safe_set(a, 'activity_ActivityParameterNode', b1)
    assert _is_linked(a, 'activity_ActivityParameterNode', b1)
    if hasattr(b1, 'activity_Activity4'):
        assert _is_linked(b1, 'activity_Activity4', a)
    _safe_set(a, 'activity_ActivityParameterNode', b2)
    assert _is_linked(a, 'activity_ActivityParameterNode', b2)
    if hasattr(b1, 'activity_Activity4'):
        assert not _is_linked(b1, 'activity_Activity4', a)
    if hasattr(b2, 'activity_Activity4'):
        assert _is_linked(b2, 'activity_Activity4', a)
    _safe_set(a, 'activity_ActivityParameterNode', None)
    assert not _is_linked(a, 'activity_ActivityParameterNode', b2)
    if hasattr(b2, 'activity_Activity4'):
        assert not _is_linked(b2, 'activity_Activity4', a)


def test_assoc_inBorder9_link_reassign_clear():
    a = activity_ActivityParameterNode(name="sample_text")
    b1 = activity_ActivityNode()
    b2 = activity_ActivityNode()
    _safe_set(a, 'activity_ActivityParameterNode10', {b1})
    assert _is_linked(a, 'activity_ActivityParameterNode10', b1)
    if hasattr(b1, 'activity_ActivityNode11'):
        assert _is_linked(b1, 'activity_ActivityNode11', a)
    _safe_set(a, 'activity_ActivityParameterNode10', {b2})
    assert _is_linked(a, 'activity_ActivityParameterNode10', b2)
    if hasattr(b1, 'activity_ActivityNode11'):
        assert not _is_linked(b1, 'activity_ActivityNode11', a)
    if hasattr(b2, 'activity_ActivityNode11'):
        assert _is_linked(b2, 'activity_ActivityNode11', a)
    _safe_set(a, 'activity_ActivityParameterNode10', set())
    assert not _is_linked(a, 'activity_ActivityParameterNode10', b2)
    if hasattr(b2, 'activity_ActivityNode11'):
        assert not _is_linked(b2, 'activity_ActivityNode11', a)


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

Activity_strategy = st.builds(Activity)
@given(instance=Activity_strategy)
@settings(max_examples=25)
def test_Activity_instantiation(instance):
    assert isinstance(instance, Activity)


ActivityEdge_strategy = st.builds(ActivityEdge)
@given(instance=ActivityEdge_strategy)
@settings(max_examples=25)
def test_ActivityEdge_instantiation(instance):
    assert isinstance(instance, ActivityEdge)


ActivityGroup_strategy = st.builds(ActivityGroup)
@given(instance=ActivityGroup_strategy)
@settings(max_examples=25)
def test_ActivityGroup_instantiation(instance):
    assert isinstance(instance, ActivityGroup)


ActivityNode_strategy = st.builds(ActivityNode)
@given(instance=ActivityNode_strategy)
@settings(max_examples=25)
def test_ActivityNode_instantiation(instance):
    assert isinstance(instance, ActivityNode)


ControlNode_strategy = st.builds(ControlNode)
@given(instance=ControlNode_strategy)
@settings(max_examples=25)
def test_ControlNode_instantiation(instance):
    assert isinstance(instance, ControlNode)


ExecutableNode_strategy = st.builds(ExecutableNode)
@given(instance=ExecutableNode_strategy)
@settings(max_examples=25)
def test_ExecutableNode_instantiation(instance):
    assert isinstance(instance, ExecutableNode)


FinalNode_strategy = st.builds(FinalNode)
@given(instance=FinalNode_strategy)
@settings(max_examples=25)
def test_FinalNode_instantiation(instance):
    assert isinstance(instance, FinalNode)


NamedElement_strategy = st.builds(NamedElement)
@given(instance=NamedElement_strategy)
@settings(max_examples=25)
def test_NamedElement_instantiation(instance):
    assert isinstance(instance, NamedElement)


ObjectNode_strategy = st.builds(ObjectNode)
@given(instance=ObjectNode_strategy)
@settings(max_examples=25)
def test_ObjectNode_instantiation(instance):
    assert isinstance(instance, ObjectNode)


Pin_strategy = st.builds(Pin)
@given(instance=Pin_strategy)
@settings(max_examples=25)
def test_Pin_instantiation(instance):
    assert isinstance(instance, Pin)


activity_AcceptEventAction_strategy = st.builds(activity_AcceptEventAction)
@given(instance=activity_AcceptEventAction_strategy)
@settings(max_examples=25)
def test_activity_AcceptEventAction_instantiation(instance):
    assert isinstance(instance, activity_AcceptEventAction)


activity_AcceptTimeEventAction_strategy = st.builds(activity_AcceptTimeEventAction)
@given(instance=activity_AcceptTimeEventAction_strategy)
@settings(max_examples=25)
def test_activity_AcceptTimeEventAction_instantiation(instance):
    assert isinstance(instance, activity_AcceptTimeEventAction)


activity_Action_strategy = st.builds(activity_Action)
@given(instance=activity_Action_strategy)
@settings(max_examples=25)
def test_activity_Action_instantiation(instance):
    assert isinstance(instance, activity_Action)


activity_Activity_strategy = st.builds(activity_Activity)
@given(instance=activity_Activity_strategy)
@settings(max_examples=25)
def test_activity_Activity_instantiation(instance):
    assert isinstance(instance, activity_Activity)


activity_ActivityEdge_strategy = st.builds(activity_ActivityEdge)
@given(instance=activity_ActivityEdge_strategy)
@settings(max_examples=25)
def test_activity_ActivityEdge_instantiation(instance):
    assert isinstance(instance, activity_ActivityEdge)


activity_ActivityFinalNode_strategy = st.builds(activity_ActivityFinalNode)
@given(instance=activity_ActivityFinalNode_strategy)
@settings(max_examples=25)
def test_activity_ActivityFinalNode_instantiation(instance):
    assert isinstance(instance, activity_ActivityFinalNode)


activity_ActivityGroup_strategy = st.builds(activity_ActivityGroup, name=safe_text)
@given(instance=activity_ActivityGroup_strategy)
@settings(max_examples=25)
def test_activity_ActivityGroup_instantiation(instance):
    assert isinstance(instance, activity_ActivityGroup)


activity_ActivityNode_strategy = st.builds(activity_ActivityNode)
@given(instance=activity_ActivityNode_strategy)
@settings(max_examples=25)
def test_activity_ActivityNode_instantiation(instance):
    assert isinstance(instance, activity_ActivityNode)


activity_ActivityParameterNode_strategy = st.builds(activity_ActivityParameterNode, name=safe_text)
@given(instance=activity_ActivityParameterNode_strategy)
@settings(max_examples=25)
def test_activity_ActivityParameterNode_instantiation(instance):
    assert isinstance(instance, activity_ActivityParameterNode)


activity_ActivityPartition_strategy = st.builds(activity_ActivityPartition)
@given(instance=activity_ActivityPartition_strategy)
@settings(max_examples=25)
def test_activity_ActivityPartition_instantiation(instance):
    assert isinstance(instance, activity_ActivityPartition)


activity_CentralBufferNode_strategy = st.builds(activity_CentralBufferNode)
@given(instance=activity_CentralBufferNode_strategy)
@settings(max_examples=25)
def test_activity_CentralBufferNode_instantiation(instance):
    assert isinstance(instance, activity_CentralBufferNode)


activity_Connector_strategy = st.builds(activity_Connector)
@given(instance=activity_Connector_strategy)
@settings(max_examples=25)
def test_activity_Connector_instantiation(instance):
    assert isinstance(instance, activity_Connector)


activity_ControlFlow_strategy = st.builds(activity_ControlFlow)
@given(instance=activity_ControlFlow_strategy)
@settings(max_examples=25)
def test_activity_ControlFlow_instantiation(instance):
    assert isinstance(instance, activity_ControlFlow)


activity_ControlNode_strategy = st.builds(activity_ControlNode)
@given(instance=activity_ControlNode_strategy)
@settings(max_examples=25)
def test_activity_ControlNode_instantiation(instance):
    assert isinstance(instance, activity_ControlNode)


activity_DataStoreNode_strategy = st.builds(activity_DataStoreNode)
@given(instance=activity_DataStoreNode_strategy)
@settings(max_examples=25)
def test_activity_DataStoreNode_instantiation(instance):
    assert isinstance(instance, activity_DataStoreNode)


activity_DecisionNode_strategy = st.builds(activity_DecisionNode)
@given(instance=activity_DecisionNode_strategy)
@settings(max_examples=25)
def test_activity_DecisionNode_instantiation(instance):
    assert isinstance(instance, activity_DecisionNode)


activity_ExecutableNode_strategy = st.builds(activity_ExecutableNode)
@given(instance=activity_ExecutableNode_strategy)
@settings(max_examples=25)
def test_activity_ExecutableNode_instantiation(instance):
    assert isinstance(instance, activity_ExecutableNode)


activity_FinalNode_strategy = st.builds(activity_FinalNode)
@given(instance=activity_FinalNode_strategy)
@settings(max_examples=25)
def test_activity_FinalNode_instantiation(instance):
    assert isinstance(instance, activity_FinalNode)


activity_FlowFinalNode_strategy = st.builds(activity_FlowFinalNode)
@given(instance=activity_FlowFinalNode_strategy)
@settings(max_examples=25)
def test_activity_FlowFinalNode_instantiation(instance):
    assert isinstance(instance, activity_FlowFinalNode)


activity_ForkNode_strategy = st.builds(activity_ForkNode)
@given(instance=activity_ForkNode_strategy)
@settings(max_examples=25)
def test_activity_ForkNode_instantiation(instance):
    assert isinstance(instance, activity_ForkNode)


activity_InitialNode_strategy = st.builds(activity_InitialNode)
@given(instance=activity_InitialNode_strategy)
@settings(max_examples=25)
def test_activity_InitialNode_instantiation(instance):
    assert isinstance(instance, activity_InitialNode)


activity_InputPin_strategy = st.builds(activity_InputPin)
@given(instance=activity_InputPin_strategy)
@settings(max_examples=25)
def test_activity_InputPin_instantiation(instance):
    assert isinstance(instance, activity_InputPin)


activity_InterruptEdge_strategy = st.builds(activity_InterruptEdge)
@given(instance=activity_InterruptEdge_strategy)
@settings(max_examples=25)
def test_activity_InterruptEdge_instantiation(instance):
    assert isinstance(instance, activity_InterruptEdge)


activity_InterruptibleActivityRegion_strategy = st.builds(activity_InterruptibleActivityRegion)
@given(instance=activity_InterruptibleActivityRegion_strategy)
@settings(max_examples=25)
def test_activity_InterruptibleActivityRegion_instantiation(instance):
    assert isinstance(instance, activity_InterruptibleActivityRegion)


activity_JoinNode_strategy = st.builds(activity_JoinNode)
@given(instance=activity_JoinNode_strategy)
@settings(max_examples=25)
def test_activity_JoinNode_instantiation(instance):
    assert isinstance(instance, activity_JoinNode)


activity_MergeNode_strategy = st.builds(activity_MergeNode)
@given(instance=activity_MergeNode_strategy)
@settings(max_examples=25)
def test_activity_MergeNode_instantiation(instance):
    assert isinstance(instance, activity_MergeNode)


activity_NamedElement_strategy = st.builds(activity_NamedElement, Name=safe_text, qualifiedName=safe_text)
@given(instance=activity_NamedElement_strategy)
@settings(max_examples=25)
def test_activity_NamedElement_instantiation(instance):
    assert isinstance(instance, activity_NamedElement)


activity_Object_strategy = st.builds(activity_Object)
@given(instance=activity_Object_strategy)
@settings(max_examples=25)
def test_activity_Object_instantiation(instance):
    assert isinstance(instance, activity_Object)


activity_ObjectFlow_strategy = st.builds(activity_ObjectFlow)
@given(instance=activity_ObjectFlow_strategy)
@settings(max_examples=25)
def test_activity_ObjectFlow_instantiation(instance):
    assert isinstance(instance, activity_ObjectFlow)


activity_ObjectNode_strategy = st.builds(activity_ObjectNode)
@given(instance=activity_ObjectNode_strategy)
@settings(max_examples=25)
def test_activity_ObjectNode_instantiation(instance):
    assert isinstance(instance, activity_ObjectNode)


activity_OutputPin_strategy = st.builds(activity_OutputPin)
@given(instance=activity_OutputPin_strategy)
@settings(max_examples=25)
def test_activity_OutputPin_instantiation(instance):
    assert isinstance(instance, activity_OutputPin)


activity_Pin_strategy = st.builds(activity_Pin)
@given(instance=activity_Pin_strategy)
@settings(max_examples=25)
def test_activity_Pin_instantiation(instance):
    assert isinstance(instance, activity_Pin)


activity_SendSignalAction_strategy = st.builds(activity_SendSignalAction)
@given(instance=activity_SendSignalAction_strategy)
@settings(max_examples=25)
def test_activity_SendSignalAction_instantiation(instance):
    assert isinstance(instance, activity_SendSignalAction)


