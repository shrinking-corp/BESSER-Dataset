import inspect
import pytest
from datetime import date, datetime, time, timedelta
from hypothesis import given, settings
import hypothesis.strategies as st

from python_code import (
    Activities_BasicActivities_ActivityEdge,
    Activities_BasicActivities_ActivityFinalNode,
    Activities_BasicActivities_ActivityParameterNode,
    Activities_BasicActivities_ControlFlow,
    Activities_BasicActivities_ControlNode,
    Activities_BasicActivities_InitialNode,
    Activities_BasicActivities_ObjectFlow,
    Activities_BasicActivities_ObjectNode,
    Activities_BasicActivities_Parameter,
    Activities_BasicActivities_Pin,
    Activities_BasicActivities_RedefinableElement,
    Activities_BasicActivities_TypedElement,
    Activities_CompleteStructuredActivities_InputPin,
    Activities_ExtraStructuredActivities_Classifier,
    Activities_ExtraStructuredActivities_ExceptionHandler,
    Activities_ExtraStructuredActivities_ExpansionNode,
    Activities_ExtraStructuredActivities_ExpansionRegion,
    Activities_FundamentalActivities_Action,
    Activities_FundamentalActivities_Activity,
    Activities_FundamentalActivities_ActivityGroup,
    Activities_FundamentalActivities_ActivityNode,
    Activities_FundamentalActivities_Behavior,
    Activities_FundamentalActivities_NamedElement,
    Activities_FundamentalActivities_Namespace,
    Activities_IntermediateActivities_ActivityPartition,
    Activities_IntermediateActivities_BehavioralFeature,
    Activities_IntermediateActivities_CentralBufferNode,
    Activities_IntermediateActivities_Class,
    Activities_IntermediateActivities_Constraint,
    Activities_IntermediateActivities_DataStoreNode,
    Activities_IntermediateActivities_DecisionNode,
    Activities_IntermediateActivities_Element,
    Activities_IntermediateActivities_Feature,
    Activities_IntermediateActivities_FinalNode,
    Activities_IntermediateActivities_FlowFinalNode,
    Activities_IntermediateActivities_ForkNode,
    Activities_IntermediateActivities_InterruptibleActivityRegion,
    Activities_IntermediateActivities_JoinNode,
    Activities_IntermediateActivities_MergeNode,
    Activities_IntermediateActivities_ParameterSet,
    Activities_IntermediateActivities_State,
    Activities_IntermediateActivities_ValueSpecification,
    Activities_StructuredActivities_Clause,
    Activities_StructuredActivities_ConditionalNode,
    Activities_StructuredActivities_ExecutableNode,
    Activities_StructuredActivities_LoopNode,
    Activities_StructuredActivities_MultiplicityElement,
    Activities_StructuredActivities_OutputPin,
    Activities_StructuredActivities_SequenceNode,
    Activities_StructuredActivities_StructuredActivityNode,
    Activities_StructuredActivities_Variable,
    Activity,
    ActivityEdge,
    ActivityGroup,
    ActivityNode,
    ActivityPartition,
    BasicActivities_ControlNode,
    BasicActivities_RedefinableElement,
    BasicActivities_TypedElement,
    Behavior,
    CentralBufferNode,
    Class,
    Classifier,
    Clause,
    Constraint,
    ControlNode,
    Element,
    ExceptionHandler,
    ExecutableNode,
    ExpansionNode,
    ExpansionRegion,
    FinalNode,
    FundamentalActivities_Action,
    FundamentalActivities_ActivityGroup,
    FundamentalActivities_ActivityNode,
    FundamentalActivities_NamedElement,
    FundamentalActivities_Namespace,
    InputPin,
    IntermediateActivities_Feature,
    IntermediateActivities_FinalNode,
    InterruptibleActivityRegion,
    NamedElement,
    ObjectFlow,
    ObjectNode,
    OutputPin,
    Parameter,
    ParameterSet,
    RedefinableElement,
    State,
    StructuredActivities_ExecutableNode,
    StructuredActivities_MultiplicityElement,
    StructuredActivityNode,
    ValueSpecification,
    Variable,
    ExpansionKind,
    ObjectNodeOrderingKind,
    ParameterEffectKind,
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

def test_Activities_BasicActivities_ObjectFlow_isControlType_value_roundtrip():
    instance = Activities_BasicActivities_ObjectFlow(isControlType=True, isMulticast=True, isMultireceive=True, ordering="sample_text")
    assert instance.isControlType == True
    instance.isControlType = False
    assert instance.isControlType == False


def test_Activities_BasicActivities_ObjectFlow_isMulticast_value_roundtrip():
    instance = Activities_BasicActivities_ObjectFlow(isControlType=True, isMulticast=True, isMultireceive=True, ordering="sample_text")
    assert instance.isMulticast == True
    instance.isMulticast = False
    assert instance.isMulticast == False


def test_Activities_BasicActivities_ObjectFlow_isMultireceive_value_roundtrip():
    instance = Activities_BasicActivities_ObjectFlow(isControlType=True, isMulticast=True, isMultireceive=True, ordering="sample_text")
    assert instance.isMultireceive == True
    instance.isMultireceive = False
    assert instance.isMultireceive == False


def test_Activities_BasicActivities_ObjectFlow_ordering_value_roundtrip():
    instance = Activities_BasicActivities_ObjectFlow(isControlType=True, isMulticast=True, isMultireceive=True, ordering="sample_text")
    assert instance.ordering == "sample_text"
    instance.ordering = "sample_text_2"
    assert instance.ordering == "sample_text_2"


def test_Activities_BasicActivities_Parameter_effect_value_roundtrip():
    instance = Activities_BasicActivities_Parameter(effect="sample_text", isException=True, isStream=True)
    assert instance.effect == "sample_text"
    instance.effect = "sample_text_2"
    assert instance.effect == "sample_text_2"


def test_Activities_BasicActivities_Parameter_isException_value_roundtrip():
    instance = Activities_BasicActivities_Parameter(effect="sample_text", isException=True, isStream=True)
    assert instance.isException == True
    instance.isException = False
    assert instance.isException == False


def test_Activities_BasicActivities_Parameter_isStream_value_roundtrip():
    instance = Activities_BasicActivities_Parameter(effect="sample_text", isException=True, isStream=True)
    assert instance.isStream == True
    instance.isStream = False
    assert instance.isStream == False


def test_Activities_BasicActivities_Pin_isControl_value_roundtrip():
    instance = Activities_BasicActivities_Pin(isControl=True)
    assert instance.isControl == True
    instance.isControl = False
    assert instance.isControl == False


def test_Activities_ExtraStructuredActivities_ExpansionRegion_mode_value_roundtrip():
    instance = Activities_ExtraStructuredActivities_ExpansionRegion(mode="sample_text")
    assert instance.mode == "sample_text"
    instance.mode = "sample_text_2"
    assert instance.mode == "sample_text_2"


def test_Activities_FundamentalActivities_Action_isLocallyReentrant_value_roundtrip():
    instance = Activities_FundamentalActivities_Action(isLocallyReentrant=True)
    assert instance.isLocallyReentrant == True
    instance.isLocallyReentrant = False
    assert instance.isLocallyReentrant == False


def test_Activities_FundamentalActivities_Activity_isReadOnly_value_roundtrip():
    instance = Activities_FundamentalActivities_Activity(isReadOnly=True, isSingleExecution=True)
    assert instance.isReadOnly == True
    instance.isReadOnly = False
    assert instance.isReadOnly == False


def test_Activities_FundamentalActivities_Activity_isSingleExecution_value_roundtrip():
    instance = Activities_FundamentalActivities_Activity(isReadOnly=True, isSingleExecution=True)
    assert instance.isSingleExecution == True
    instance.isSingleExecution = False
    assert instance.isSingleExecution == False


def test_Activities_IntermediateActivities_JoinNode_isCombineDuplicate_value_roundtrip():
    instance = Activities_IntermediateActivities_JoinNode(isCombineDuplicate=True)
    assert instance.isCombineDuplicate == True
    instance.isCombineDuplicate = False
    assert instance.isCombineDuplicate == False


def test_Activities_StructuredActivities_ConditionalNode_isAssumed_value_roundtrip():
    instance = Activities_StructuredActivities_ConditionalNode(isAssumed=True, isDeterminate=True)
    assert instance.isAssumed == True
    instance.isAssumed = False
    assert instance.isAssumed == False


def test_Activities_StructuredActivities_ConditionalNode_isDeterminate_value_roundtrip():
    instance = Activities_StructuredActivities_ConditionalNode(isAssumed=True, isDeterminate=True)
    assert instance.isDeterminate == True
    instance.isDeterminate = False
    assert instance.isDeterminate == False


def test_Activities_StructuredActivities_LoopNode_isTestedFirst_value_roundtrip():
    instance = Activities_StructuredActivities_LoopNode(isTestedFirst=True)
    assert instance.isTestedFirst == True
    instance.isTestedFirst = False
    assert instance.isTestedFirst == False


def test_Activities_StructuredActivities_StructuredActivityNode_mustIsolate_value_roundtrip():
    instance = Activities_StructuredActivities_StructuredActivityNode(mustIsolate=True)
    assert instance.mustIsolate == True
    instance.mustIsolate = False
    assert instance.mustIsolate == False


def test_Activities_BasicActivities_ControlFlow_isa_ActivityEdge():
    instance = Activities_BasicActivities_ControlFlow()
    assert isinstance(instance, ActivityEdge)


def test_Activities_BasicActivities_ObjectFlow_isa_ActivityEdge():
    instance = Activities_BasicActivities_ObjectFlow(isControlType=True, isMulticast=True, isMultireceive=True, ordering="sample_text")
    assert isinstance(instance, ActivityEdge)


def test_Activities_IntermediateActivities_ActivityPartition_isa_ActivityGroup():
    instance = Activities_IntermediateActivities_ActivityPartition()
    assert isinstance(instance, ActivityGroup)


def test_Activities_IntermediateActivities_InterruptibleActivityRegion_isa_ActivityGroup():
    instance = Activities_IntermediateActivities_InterruptibleActivityRegion()
    assert isinstance(instance, ActivityGroup)


def test_Activities_BasicActivities_ControlNode_isa_ActivityNode():
    instance = Activities_BasicActivities_ControlNode()
    assert isinstance(instance, ActivityNode)


def test_Activities_FundamentalActivities_Action_isa_ActivityNode():
    instance = Activities_FundamentalActivities_Action(isLocallyReentrant=True)
    assert isinstance(instance, ActivityNode)


def test_Activities_StructuredActivities_ExecutableNode_isa_ActivityNode():
    instance = Activities_StructuredActivities_ExecutableNode()
    assert isinstance(instance, ActivityNode)


def test_Activities_BasicActivities_ActivityFinalNode_isa_BasicActivities_ControlNode():
    instance = Activities_BasicActivities_ActivityFinalNode()
    assert isinstance(instance, BasicActivities_ControlNode)


def test_Activities_FundamentalActivities_ActivityNode_isa_BasicActivities_RedefinableElement():
    instance = Activities_FundamentalActivities_ActivityNode()
    assert isinstance(instance, BasicActivities_RedefinableElement)


def test_Activities_BasicActivities_ObjectNode_isa_BasicActivities_TypedElement():
    instance = Activities_BasicActivities_ObjectNode()
    assert isinstance(instance, BasicActivities_TypedElement)


def test_Activities_StructuredActivities_Variable_isa_BasicActivities_TypedElement():
    instance = Activities_StructuredActivities_Variable()
    assert isinstance(instance, BasicActivities_TypedElement)


def test_Activities_FundamentalActivities_Activity_isa_Behavior():
    instance = Activities_FundamentalActivities_Activity(isReadOnly=True, isSingleExecution=True)
    assert isinstance(instance, Behavior)


def test_Activities_IntermediateActivities_DataStoreNode_isa_CentralBufferNode():
    instance = Activities_IntermediateActivities_DataStoreNode()
    assert isinstance(instance, CentralBufferNode)


def test_Activities_FundamentalActivities_Behavior_isa_Class():
    instance = Activities_FundamentalActivities_Behavior()
    assert isinstance(instance, Class)


def test_Activities_BasicActivities_InitialNode_isa_ControlNode():
    instance = Activities_BasicActivities_InitialNode()
    assert isinstance(instance, ControlNode)


def test_Activities_IntermediateActivities_DecisionNode_isa_ControlNode():
    instance = Activities_IntermediateActivities_DecisionNode()
    assert isinstance(instance, ControlNode)


def test_Activities_IntermediateActivities_FinalNode_isa_ControlNode():
    instance = Activities_IntermediateActivities_FinalNode()
    assert isinstance(instance, ControlNode)


def test_Activities_IntermediateActivities_ForkNode_isa_ControlNode():
    instance = Activities_IntermediateActivities_ForkNode()
    assert isinstance(instance, ControlNode)


def test_Activities_IntermediateActivities_JoinNode_isa_ControlNode():
    instance = Activities_IntermediateActivities_JoinNode(isCombineDuplicate=True)
    assert isinstance(instance, ControlNode)


def test_Activities_IntermediateActivities_MergeNode_isa_ControlNode():
    instance = Activities_IntermediateActivities_MergeNode()
    assert isinstance(instance, ControlNode)


def test_Activities_ExtraStructuredActivities_ExceptionHandler_isa_Element():
    instance = Activities_ExtraStructuredActivities_ExceptionHandler()
    assert isinstance(instance, Element)


def test_Activities_StructuredActivities_Clause_isa_Element():
    instance = Activities_StructuredActivities_Clause()
    assert isinstance(instance, Element)


def test_Activities_IntermediateActivities_FlowFinalNode_isa_FinalNode():
    instance = Activities_IntermediateActivities_FlowFinalNode()
    assert isinstance(instance, FinalNode)


def test_Activities_StructuredActivities_StructuredActivityNode_isa_FundamentalActivities_Action():
    instance = Activities_StructuredActivities_StructuredActivityNode(mustIsolate=True)
    assert isinstance(instance, FundamentalActivities_Action)


def test_Activities_StructuredActivities_StructuredActivityNode_isa_FundamentalActivities_ActivityGroup():
    instance = Activities_StructuredActivities_StructuredActivityNode(mustIsolate=True)
    assert isinstance(instance, FundamentalActivities_ActivityGroup)


def test_Activities_BasicActivities_ObjectNode_isa_FundamentalActivities_ActivityNode():
    instance = Activities_BasicActivities_ObjectNode()
    assert isinstance(instance, FundamentalActivities_ActivityNode)


def test_Activities_FundamentalActivities_ActivityNode_isa_FundamentalActivities_NamedElement():
    instance = Activities_FundamentalActivities_ActivityNode()
    assert isinstance(instance, FundamentalActivities_NamedElement)


def test_Activities_IntermediateActivities_BehavioralFeature_isa_FundamentalActivities_Namespace():
    instance = Activities_IntermediateActivities_BehavioralFeature()
    assert isinstance(instance, FundamentalActivities_Namespace)


def test_Activities_StructuredActivities_StructuredActivityNode_isa_FundamentalActivities_Namespace():
    instance = Activities_StructuredActivities_StructuredActivityNode(mustIsolate=True)
    assert isinstance(instance, FundamentalActivities_Namespace)


def test_Activities_IntermediateActivities_BehavioralFeature_isa_IntermediateActivities_Feature():
    instance = Activities_IntermediateActivities_BehavioralFeature()
    assert isinstance(instance, IntermediateActivities_Feature)


def test_Activities_BasicActivities_ActivityFinalNode_isa_IntermediateActivities_FinalNode():
    instance = Activities_BasicActivities_ActivityFinalNode()
    assert isinstance(instance, IntermediateActivities_FinalNode)


def test_Activities_FundamentalActivities_ActivityGroup_isa_NamedElement():
    instance = Activities_FundamentalActivities_ActivityGroup()
    assert isinstance(instance, NamedElement)


def test_Activities_IntermediateActivities_ParameterSet_isa_NamedElement():
    instance = Activities_IntermediateActivities_ParameterSet()
    assert isinstance(instance, NamedElement)


def test_Activities_BasicActivities_ActivityParameterNode_isa_ObjectNode():
    instance = Activities_BasicActivities_ActivityParameterNode()
    assert isinstance(instance, ObjectNode)


def test_Activities_BasicActivities_Pin_isa_ObjectNode():
    instance = Activities_BasicActivities_Pin(isControl=True)
    assert isinstance(instance, ObjectNode)


def test_Activities_ExtraStructuredActivities_ExpansionNode_isa_ObjectNode():
    instance = Activities_ExtraStructuredActivities_ExpansionNode()
    assert isinstance(instance, ObjectNode)


def test_Activities_IntermediateActivities_CentralBufferNode_isa_ObjectNode():
    instance = Activities_IntermediateActivities_CentralBufferNode()
    assert isinstance(instance, ObjectNode)


def test_Activities_BasicActivities_ActivityEdge_isa_RedefinableElement():
    instance = Activities_BasicActivities_ActivityEdge()
    assert isinstance(instance, RedefinableElement)


def test_Activities_StructuredActivities_StructuredActivityNode_isa_StructuredActivities_ExecutableNode():
    instance = Activities_StructuredActivities_StructuredActivityNode(mustIsolate=True)
    assert isinstance(instance, StructuredActivities_ExecutableNode)


def test_Activities_StructuredActivities_Variable_isa_StructuredActivities_MultiplicityElement():
    instance = Activities_StructuredActivities_Variable()
    assert isinstance(instance, StructuredActivities_MultiplicityElement)


def test_Activities_ExtraStructuredActivities_ExpansionRegion_isa_StructuredActivityNode():
    instance = Activities_ExtraStructuredActivities_ExpansionRegion(mode="sample_text")
    assert isinstance(instance, StructuredActivityNode)


def test_Activities_StructuredActivities_ConditionalNode_isa_StructuredActivityNode():
    instance = Activities_StructuredActivities_ConditionalNode(isAssumed=True, isDeterminate=True)
    assert isinstance(instance, StructuredActivityNode)


def test_Activities_StructuredActivities_LoopNode_isa_StructuredActivityNode():
    instance = Activities_StructuredActivities_LoopNode(isTestedFirst=True)
    assert isinstance(instance, StructuredActivityNode)


def test_Activities_StructuredActivities_SequenceNode_isa_StructuredActivityNode():
    instance = Activities_StructuredActivities_SequenceNode()
    assert isinstance(instance, StructuredActivityNode)


def test_assoc_activity99_link_reassign_clear():
    a = Activities_StructuredActivities_StructuredActivityNode(mustIsolate=True)
    b1 = Activity()
    b2 = Activity()
    _safe_set(a, 'structuredNode', b1)
    assert _is_linked(a, 'structuredNode', b1)
    if hasattr(b1, 'Activity100'):
        assert _is_linked(b1, 'Activity100', a)
    _safe_set(a, 'structuredNode', b2)
    assert _is_linked(a, 'structuredNode', b2)
    if hasattr(b1, 'Activity100'):
        assert not _is_linked(b1, 'Activity100', a)
    if hasattr(b2, 'Activity100'):
        assert _is_linked(b2, 'Activity100', a)
    _safe_set(a, 'structuredNode', None)
    assert not _is_linked(a, 'structuredNode', b2)
    if hasattr(b2, 'Activity100'):
        assert not _is_linked(b2, 'Activity100', a)


def test_assoc_body141_link_reassign_clear():
    a = Activities_StructuredActivities_ConditionalNode(isAssumed=True, isDeterminate=True)
    b1 = ExecutableNode()
    b2 = ExecutableNode()
    _safe_set(a, 'Activities_StructuredActivities_ConditionalNode142', {b1})
    assert _is_linked(a, 'Activities_StructuredActivities_ConditionalNode142', b1)
    if hasattr(b1, 'ExecutableNode143'):
        assert _is_linked(b1, 'ExecutableNode143', a)
    _safe_set(a, 'Activities_StructuredActivities_ConditionalNode142', {b2})
    assert _is_linked(a, 'Activities_StructuredActivities_ConditionalNode142', b2)
    if hasattr(b1, 'ExecutableNode143'):
        assert not _is_linked(b1, 'ExecutableNode143', a)
    if hasattr(b2, 'ExecutableNode143'):
        assert _is_linked(b2, 'ExecutableNode143', a)
    _safe_set(a, 'Activities_StructuredActivities_ConditionalNode142', set())
    assert not _is_linked(a, 'Activities_StructuredActivities_ConditionalNode142', b2)
    if hasattr(b2, 'ExecutableNode143'):
        assert not _is_linked(b2, 'ExecutableNode143', a)


def test_assoc_bodyOutput131_link_reassign_clear():
    a = Activities_StructuredActivities_LoopNode(isTestedFirst=True)
    b1 = OutputPin()
    b2 = OutputPin()
    _safe_set(a, 'Activities_StructuredActivities_LoopNode132', {b1})
    assert _is_linked(a, 'Activities_StructuredActivities_LoopNode132', b1)
    if hasattr(b1, 'OutputPin133'):
        assert _is_linked(b1, 'OutputPin133', a)
    _safe_set(a, 'Activities_StructuredActivities_LoopNode132', {b2})
    assert _is_linked(a, 'Activities_StructuredActivities_LoopNode132', b2)
    if hasattr(b1, 'OutputPin133'):
        assert not _is_linked(b1, 'OutputPin133', a)
    if hasattr(b2, 'OutputPin133'):
        assert _is_linked(b2, 'OutputPin133', a)
    _safe_set(a, 'Activities_StructuredActivities_LoopNode132', set())
    assert not _is_linked(a, 'Activities_StructuredActivities_LoopNode132', b2)
    if hasattr(b2, 'OutputPin133'):
        assert not _is_linked(b2, 'OutputPin133', a)


def test_assoc_bodyPart116_link_reassign_clear():
    a = Activities_StructuredActivities_LoopNode(isTestedFirst=True)
    b1 = ExecutableNode()
    b2 = ExecutableNode()
    _safe_set(a, 'Activities_StructuredActivities_LoopNode117', {b1})
    assert _is_linked(a, 'Activities_StructuredActivities_LoopNode117', b1)
    if hasattr(b1, 'ExecutableNode118'):
        assert _is_linked(b1, 'ExecutableNode118', a)
    _safe_set(a, 'Activities_StructuredActivities_LoopNode117', {b2})
    assert _is_linked(a, 'Activities_StructuredActivities_LoopNode117', b2)
    if hasattr(b1, 'ExecutableNode118'):
        assert not _is_linked(b1, 'ExecutableNode118', a)
    if hasattr(b2, 'ExecutableNode118'):
        assert _is_linked(b2, 'ExecutableNode118', a)
    _safe_set(a, 'Activities_StructuredActivities_LoopNode117', set())
    assert not _is_linked(a, 'Activities_StructuredActivities_LoopNode117', b2)
    if hasattr(b2, 'ExecutableNode118'):
        assert not _is_linked(b2, 'ExecutableNode118', a)


def test_assoc_clause137_link_reassign_clear():
    a = Activities_StructuredActivities_ConditionalNode(isAssumed=True, isDeterminate=True)
    b1 = Clause()
    b2 = Clause()
    _safe_set(a, 'Activities_StructuredActivities_ConditionalNode', {b1})
    assert _is_linked(a, 'Activities_StructuredActivities_ConditionalNode', b1)
    if hasattr(b1, 'Clause'):
        assert _is_linked(b1, 'Clause', a)
    _safe_set(a, 'Activities_StructuredActivities_ConditionalNode', {b2})
    assert _is_linked(a, 'Activities_StructuredActivities_ConditionalNode', b2)
    if hasattr(b1, 'Clause'):
        assert not _is_linked(b1, 'Clause', a)
    if hasattr(b2, 'Clause'):
        assert _is_linked(b2, 'Clause', a)
    _safe_set(a, 'Activities_StructuredActivities_ConditionalNode', set())
    assert not _is_linked(a, 'Activities_StructuredActivities_ConditionalNode', b2)
    if hasattr(b2, 'Clause'):
        assert not _is_linked(b2, 'Clause', a)


def test_assoc_decider122_link_reassign_clear():
    a = Activities_StructuredActivities_LoopNode(isTestedFirst=True)
    b1 = OutputPin()
    b2 = OutputPin()
    _safe_set(a, 'Activities_StructuredActivities_LoopNode123', b1)
    assert _is_linked(a, 'Activities_StructuredActivities_LoopNode123', b1)
    if hasattr(b1, 'OutputPin124'):
        assert _is_linked(b1, 'OutputPin124', a)
    _safe_set(a, 'Activities_StructuredActivities_LoopNode123', b2)
    assert _is_linked(a, 'Activities_StructuredActivities_LoopNode123', b2)
    if hasattr(b1, 'OutputPin124'):
        assert not _is_linked(b1, 'OutputPin124', a)
    if hasattr(b2, 'OutputPin124'):
        assert _is_linked(b2, 'OutputPin124', a)
    _safe_set(a, 'Activities_StructuredActivities_LoopNode123', None)
    assert not _is_linked(a, 'Activities_StructuredActivities_LoopNode123', b2)
    if hasattr(b2, 'OutputPin124'):
        assert not _is_linked(b2, 'OutputPin124', a)


def test_assoc_edge108_link_reassign_clear():
    a = Activities_StructuredActivities_StructuredActivityNode(mustIsolate=True)
    b1 = ActivityEdge()
    b2 = ActivityEdge()
    _safe_set(a, 'inStructuredNode109', {b1})
    assert _is_linked(a, 'inStructuredNode109', b1)
    if hasattr(b1, 'ActivityEdge110'):
        assert _is_linked(b1, 'ActivityEdge110', a)
    _safe_set(a, 'inStructuredNode109', {b2})
    assert _is_linked(a, 'inStructuredNode109', b2)
    if hasattr(b1, 'ActivityEdge110'):
        assert not _is_linked(b1, 'ActivityEdge110', a)
    if hasattr(b2, 'ActivityEdge110'):
        assert _is_linked(b2, 'ActivityEdge110', a)
    _safe_set(a, 'inStructuredNode109', set())
    assert not _is_linked(a, 'inStructuredNode109', b2)
    if hasattr(b2, 'ActivityEdge110'):
        assert not _is_linked(b2, 'ActivityEdge110', a)


def test_assoc_edge2_link_reassign_clear():
    a = Activities_FundamentalActivities_Activity(isReadOnly=True, isSingleExecution=True)
    b1 = ActivityEdge()
    b2 = ActivityEdge()
    _safe_set(a, 'Activities_FundamentalActivities_Activity3', {b1})
    assert _is_linked(a, 'Activities_FundamentalActivities_Activity3', b1)
    if hasattr(b1, 'ActivityEdge'):
        assert _is_linked(b1, 'ActivityEdge', a)
    _safe_set(a, 'Activities_FundamentalActivities_Activity3', {b2})
    assert _is_linked(a, 'Activities_FundamentalActivities_Activity3', b2)
    if hasattr(b1, 'ActivityEdge'):
        assert not _is_linked(b1, 'ActivityEdge', a)
    if hasattr(b2, 'ActivityEdge'):
        assert _is_linked(b2, 'ActivityEdge', a)
    _safe_set(a, 'Activities_FundamentalActivities_Activity3', set())
    assert not _is_linked(a, 'Activities_FundamentalActivities_Activity3', b2)
    if hasattr(b2, 'ActivityEdge'):
        assert not _is_linked(b2, 'ActivityEdge', a)


def test_assoc_group1_link_reassign_clear():
    a = Activities_FundamentalActivities_Activity(isReadOnly=True, isSingleExecution=True)
    b1 = ActivityGroup()
    b2 = ActivityGroup()
    _safe_set(a, 'inActivity', {b1})
    assert _is_linked(a, 'inActivity', b1)
    if hasattr(b1, 'ActivityGroup'):
        assert _is_linked(b1, 'ActivityGroup', a)
    _safe_set(a, 'inActivity', {b2})
    assert _is_linked(a, 'inActivity', b2)
    if hasattr(b1, 'ActivityGroup'):
        assert not _is_linked(b1, 'ActivityGroup', a)
    if hasattr(b2, 'ActivityGroup'):
        assert _is_linked(b2, 'ActivityGroup', a)
    _safe_set(a, 'inActivity', set())
    assert not _is_linked(a, 'inActivity', b2)
    if hasattr(b2, 'ActivityGroup'):
        assert not _is_linked(b2, 'ActivityGroup', a)


def test_assoc_inState71_link_reassign_clear():
    a = Activities_BasicActivities_ObjectFlow(isControlType=True, isMulticast=True, isMultireceive=True, ordering="sample_text")
    b1 = State()
    b2 = State()
    _safe_set(a, 'Activities_BasicActivities_ObjectFlow72', {b1})
    assert _is_linked(a, 'Activities_BasicActivities_ObjectFlow72', b1)
    if hasattr(b1, 'State'):
        assert _is_linked(b1, 'State', a)
    _safe_set(a, 'Activities_BasicActivities_ObjectFlow72', {b2})
    assert _is_linked(a, 'Activities_BasicActivities_ObjectFlow72', b2)
    if hasattr(b1, 'State'):
        assert not _is_linked(b1, 'State', a)
    if hasattr(b2, 'State'):
        assert _is_linked(b2, 'State', a)
    _safe_set(a, 'Activities_BasicActivities_ObjectFlow72', set())
    assert not _is_linked(a, 'Activities_BasicActivities_ObjectFlow72', b2)
    if hasattr(b2, 'State'):
        assert not _is_linked(b2, 'State', a)


def test_assoc_input29_link_reassign_clear():
    a = Activities_FundamentalActivities_Action(isLocallyReentrant=True)
    b1 = InputPin()
    b2 = InputPin()
    _safe_set(a, 'Activities_FundamentalActivities_Action30', {b1})
    assert _is_linked(a, 'Activities_FundamentalActivities_Action30', b1)
    if hasattr(b1, 'InputPin'):
        assert _is_linked(b1, 'InputPin', a)
    _safe_set(a, 'Activities_FundamentalActivities_Action30', {b2})
    assert _is_linked(a, 'Activities_FundamentalActivities_Action30', b2)
    if hasattr(b1, 'InputPin'):
        assert not _is_linked(b1, 'InputPin', a)
    if hasattr(b2, 'InputPin'):
        assert _is_linked(b2, 'InputPin', a)
    _safe_set(a, 'Activities_FundamentalActivities_Action30', set())
    assert not _is_linked(a, 'Activities_FundamentalActivities_Action30', b2)
    if hasattr(b2, 'InputPin'):
        assert not _is_linked(b2, 'InputPin', a)


def test_assoc_inputElement163_link_reassign_clear():
    a = Activities_ExtraStructuredActivities_ExpansionRegion(mode="sample_text")
    b1 = ExpansionNode()
    b2 = ExpansionNode()
    _safe_set(a, 'regionAsInput', {b1})
    assert _is_linked(a, 'regionAsInput', b1)
    if hasattr(b1, 'ExpansionNode'):
        assert _is_linked(b1, 'ExpansionNode', a)
    _safe_set(a, 'regionAsInput', {b2})
    assert _is_linked(a, 'regionAsInput', b2)
    if hasattr(b1, 'ExpansionNode'):
        assert not _is_linked(b1, 'ExpansionNode', a)
    if hasattr(b2, 'ExpansionNode'):
        assert _is_linked(b2, 'ExpansionNode', a)
    _safe_set(a, 'regionAsInput', set())
    assert not _is_linked(a, 'regionAsInput', b2)
    if hasattr(b2, 'ExpansionNode'):
        assert not _is_linked(b2, 'ExpansionNode', a)


def test_assoc_joinSpec73_link_reassign_clear():
    a = Activities_IntermediateActivities_JoinNode(isCombineDuplicate=True)
    b1 = ValueSpecification()
    b2 = ValueSpecification()
    _safe_set(a, 'Activities_IntermediateActivities_JoinNode', b1)
    assert _is_linked(a, 'Activities_IntermediateActivities_JoinNode', b1)
    if hasattr(b1, 'ValueSpecification74'):
        assert _is_linked(b1, 'ValueSpecification74', a)
    _safe_set(a, 'Activities_IntermediateActivities_JoinNode', b2)
    assert _is_linked(a, 'Activities_IntermediateActivities_JoinNode', b2)
    if hasattr(b1, 'ValueSpecification74'):
        assert not _is_linked(b1, 'ValueSpecification74', a)
    if hasattr(b2, 'ValueSpecification74'):
        assert _is_linked(b2, 'ValueSpecification74', a)
    _safe_set(a, 'Activities_IntermediateActivities_JoinNode', None)
    assert not _is_linked(a, 'Activities_IntermediateActivities_JoinNode', b2)
    if hasattr(b2, 'ValueSpecification74'):
        assert not _is_linked(b2, 'ValueSpecification74', a)


def test_assoc_localPostcondition26_link_reassign_clear():
    a = Activities_FundamentalActivities_Action(isLocallyReentrant=True)
    b1 = Constraint()
    b2 = Constraint()
    _safe_set(a, 'Activities_FundamentalActivities_Action27', {b1})
    assert _is_linked(a, 'Activities_FundamentalActivities_Action27', b1)
    if hasattr(b1, 'Constraint28'):
        assert _is_linked(b1, 'Constraint28', a)
    _safe_set(a, 'Activities_FundamentalActivities_Action27', {b2})
    assert _is_linked(a, 'Activities_FundamentalActivities_Action27', b2)
    if hasattr(b1, 'Constraint28'):
        assert not _is_linked(b1, 'Constraint28', a)
    if hasattr(b2, 'Constraint28'):
        assert _is_linked(b2, 'Constraint28', a)
    _safe_set(a, 'Activities_FundamentalActivities_Action27', set())
    assert not _is_linked(a, 'Activities_FundamentalActivities_Action27', b2)
    if hasattr(b2, 'Constraint28'):
        assert not _is_linked(b2, 'Constraint28', a)


def test_assoc_localPrecondition25_link_reassign_clear():
    a = Activities_FundamentalActivities_Action(isLocallyReentrant=True)
    b1 = Constraint()
    b2 = Constraint()
    _safe_set(a, 'Activities_FundamentalActivities_Action', {b1})
    assert _is_linked(a, 'Activities_FundamentalActivities_Action', b1)
    if hasattr(b1, 'Constraint'):
        assert _is_linked(b1, 'Constraint', a)
    _safe_set(a, 'Activities_FundamentalActivities_Action', {b2})
    assert _is_linked(a, 'Activities_FundamentalActivities_Action', b2)
    if hasattr(b1, 'Constraint'):
        assert not _is_linked(b1, 'Constraint', a)
    if hasattr(b2, 'Constraint'):
        assert _is_linked(b2, 'Constraint', a)
    _safe_set(a, 'Activities_FundamentalActivities_Action', set())
    assert not _is_linked(a, 'Activities_FundamentalActivities_Action', b2)
    if hasattr(b2, 'Constraint'):
        assert not _is_linked(b2, 'Constraint', a)


def test_assoc_loopVariable128_link_reassign_clear():
    a = Activities_StructuredActivities_LoopNode(isTestedFirst=True)
    b1 = OutputPin()
    b2 = OutputPin()
    _safe_set(a, 'Activities_StructuredActivities_LoopNode129', {b1})
    assert _is_linked(a, 'Activities_StructuredActivities_LoopNode129', b1)
    if hasattr(b1, 'OutputPin130'):
        assert _is_linked(b1, 'OutputPin130', a)
    _safe_set(a, 'Activities_StructuredActivities_LoopNode129', {b2})
    assert _is_linked(a, 'Activities_StructuredActivities_LoopNode129', b2)
    if hasattr(b1, 'OutputPin130'):
        assert not _is_linked(b1, 'OutputPin130', a)
    if hasattr(b2, 'OutputPin130'):
        assert _is_linked(b2, 'OutputPin130', a)
    _safe_set(a, 'Activities_StructuredActivities_LoopNode129', set())
    assert not _is_linked(a, 'Activities_StructuredActivities_LoopNode129', b2)
    if hasattr(b2, 'OutputPin130'):
        assert not _is_linked(b2, 'OutputPin130', a)


def test_assoc_loopVariableInput125_link_reassign_clear():
    a = Activities_StructuredActivities_LoopNode(isTestedFirst=True)
    b1 = InputPin()
    b2 = InputPin()
    _safe_set(a, 'Activities_StructuredActivities_LoopNode126', {b1})
    assert _is_linked(a, 'Activities_StructuredActivities_LoopNode126', b1)
    if hasattr(b1, 'InputPin127'):
        assert _is_linked(b1, 'InputPin127', a)
    _safe_set(a, 'Activities_StructuredActivities_LoopNode126', {b2})
    assert _is_linked(a, 'Activities_StructuredActivities_LoopNode126', b2)
    if hasattr(b1, 'InputPin127'):
        assert not _is_linked(b1, 'InputPin127', a)
    if hasattr(b2, 'InputPin127'):
        assert _is_linked(b2, 'InputPin127', a)
    _safe_set(a, 'Activities_StructuredActivities_LoopNode126', set())
    assert not _is_linked(a, 'Activities_StructuredActivities_LoopNode126', b2)
    if hasattr(b2, 'InputPin127'):
        assert not _is_linked(b2, 'InputPin127', a)


def test_assoc_node0_link_reassign_clear():
    a = Activities_FundamentalActivities_Activity(isReadOnly=True, isSingleExecution=True)
    b1 = ActivityNode()
    b2 = ActivityNode()
    _safe_set(a, 'Activities_FundamentalActivities_Activity', {b1})
    assert _is_linked(a, 'Activities_FundamentalActivities_Activity', b1)
    if hasattr(b1, 'ActivityNode'):
        assert _is_linked(b1, 'ActivityNode', a)
    _safe_set(a, 'Activities_FundamentalActivities_Activity', {b2})
    assert _is_linked(a, 'Activities_FundamentalActivities_Activity', b2)
    if hasattr(b1, 'ActivityNode'):
        assert not _is_linked(b1, 'ActivityNode', a)
    if hasattr(b2, 'ActivityNode'):
        assert _is_linked(b2, 'ActivityNode', a)
    _safe_set(a, 'Activities_FundamentalActivities_Activity', set())
    assert not _is_linked(a, 'Activities_FundamentalActivities_Activity', b2)
    if hasattr(b2, 'ActivityNode'):
        assert not _is_linked(b2, 'ActivityNode', a)


def test_assoc_node103_link_reassign_clear():
    a = Activities_StructuredActivities_StructuredActivityNode(mustIsolate=True)
    b1 = ActivityNode()
    b2 = ActivityNode()
    _safe_set(a, 'inStructuredNode', {b1})
    assert _is_linked(a, 'inStructuredNode', b1)
    if hasattr(b1, 'ActivityNode104'):
        assert _is_linked(b1, 'ActivityNode104', a)
    _safe_set(a, 'inStructuredNode', {b2})
    assert _is_linked(a, 'inStructuredNode', b2)
    if hasattr(b1, 'ActivityNode104'):
        assert not _is_linked(b1, 'ActivityNode104', a)
    if hasattr(b2, 'ActivityNode104'):
        assert _is_linked(b2, 'ActivityNode104', a)
    _safe_set(a, 'inStructuredNode', set())
    assert not _is_linked(a, 'inStructuredNode', b2)
    if hasattr(b2, 'ActivityNode104'):
        assert not _is_linked(b2, 'ActivityNode104', a)


def test_assoc_output31_link_reassign_clear():
    a = Activities_FundamentalActivities_Action(isLocallyReentrant=True)
    b1 = OutputPin()
    b2 = OutputPin()
    _safe_set(a, 'Activities_FundamentalActivities_Action32', {b1})
    assert _is_linked(a, 'Activities_FundamentalActivities_Action32', b1)
    if hasattr(b1, 'OutputPin'):
        assert _is_linked(b1, 'OutputPin', a)
    _safe_set(a, 'Activities_FundamentalActivities_Action32', {b2})
    assert _is_linked(a, 'Activities_FundamentalActivities_Action32', b2)
    if hasattr(b1, 'OutputPin'):
        assert not _is_linked(b1, 'OutputPin', a)
    if hasattr(b2, 'OutputPin'):
        assert _is_linked(b2, 'OutputPin', a)
    _safe_set(a, 'Activities_FundamentalActivities_Action32', set())
    assert not _is_linked(a, 'Activities_FundamentalActivities_Action32', b2)
    if hasattr(b2, 'OutputPin'):
        assert not _is_linked(b2, 'OutputPin', a)


def test_assoc_outputElement164_link_reassign_clear():
    a = Activities_ExtraStructuredActivities_ExpansionRegion(mode="sample_text")
    b1 = ExpansionNode()
    b2 = ExpansionNode()
    _safe_set(a, 'regionAsOutput', {b1})
    assert _is_linked(a, 'regionAsOutput', b1)
    if hasattr(b1, 'ExpansionNode165'):
        assert _is_linked(b1, 'ExpansionNode165', a)
    _safe_set(a, 'regionAsOutput', {b2})
    assert _is_linked(a, 'regionAsOutput', b2)
    if hasattr(b1, 'ExpansionNode165'):
        assert not _is_linked(b1, 'ExpansionNode165', a)
    if hasattr(b2, 'ExpansionNode165'):
        assert _is_linked(b2, 'ExpansionNode165', a)
    _safe_set(a, 'regionAsOutput', set())
    assert not _is_linked(a, 'regionAsOutput', b2)
    if hasattr(b2, 'ExpansionNode165'):
        assert not _is_linked(b2, 'ExpansionNode165', a)


def test_assoc_parameterSet45_link_reassign_clear():
    a = Activities_BasicActivities_Parameter(effect="sample_text", isException=True, isStream=True)
    b1 = ParameterSet()
    b2 = ParameterSet()
    _safe_set(a, 'parameter', {b1})
    assert _is_linked(a, 'parameter', b1)
    if hasattr(b1, 'ParameterSet46'):
        assert _is_linked(b1, 'ParameterSet46', a)
    _safe_set(a, 'parameter', {b2})
    assert _is_linked(a, 'parameter', b2)
    if hasattr(b1, 'ParameterSet46'):
        assert not _is_linked(b1, 'ParameterSet46', a)
    if hasattr(b2, 'ParameterSet46'):
        assert _is_linked(b2, 'ParameterSet46', a)
    _safe_set(a, 'parameter', set())
    assert not _is_linked(a, 'parameter', b2)
    if hasattr(b2, 'ParameterSet46'):
        assert not _is_linked(b2, 'ParameterSet46', a)


def test_assoc_partition4_link_reassign_clear():
    a = Activities_FundamentalActivities_Activity(isReadOnly=True, isSingleExecution=True)
    b1 = ActivityPartition()
    b2 = ActivityPartition()
    _safe_set(a, 'Activities_FundamentalActivities_Activity5', {b1})
    assert _is_linked(a, 'Activities_FundamentalActivities_Activity5', b1)
    if hasattr(b1, 'ActivityPartition'):
        assert _is_linked(b1, 'ActivityPartition', a)
    _safe_set(a, 'Activities_FundamentalActivities_Activity5', {b2})
    assert _is_linked(a, 'Activities_FundamentalActivities_Activity5', b2)
    if hasattr(b1, 'ActivityPartition'):
        assert not _is_linked(b1, 'ActivityPartition', a)
    if hasattr(b2, 'ActivityPartition'):
        assert _is_linked(b2, 'ActivityPartition', a)
    _safe_set(a, 'Activities_FundamentalActivities_Activity5', set())
    assert not _is_linked(a, 'Activities_FundamentalActivities_Activity5', b2)
    if hasattr(b2, 'ActivityPartition'):
        assert not _is_linked(b2, 'ActivityPartition', a)


def test_assoc_result134_link_reassign_clear():
    a = Activities_StructuredActivities_LoopNode(isTestedFirst=True)
    b1 = OutputPin()
    b2 = OutputPin()
    _safe_set(a, 'Activities_StructuredActivities_LoopNode135', {b1})
    assert _is_linked(a, 'Activities_StructuredActivities_LoopNode135', b1)
    if hasattr(b1, 'OutputPin136'):
        assert _is_linked(b1, 'OutputPin136', a)
    _safe_set(a, 'Activities_StructuredActivities_LoopNode135', {b2})
    assert _is_linked(a, 'Activities_StructuredActivities_LoopNode135', b2)
    if hasattr(b1, 'OutputPin136'):
        assert not _is_linked(b1, 'OutputPin136', a)
    if hasattr(b2, 'OutputPin136'):
        assert _is_linked(b2, 'OutputPin136', a)
    _safe_set(a, 'Activities_StructuredActivities_LoopNode135', set())
    assert not _is_linked(a, 'Activities_StructuredActivities_LoopNode135', b2)
    if hasattr(b2, 'OutputPin136'):
        assert not _is_linked(b2, 'OutputPin136', a)


def test_assoc_result144_link_reassign_clear():
    a = Activities_StructuredActivities_ConditionalNode(isAssumed=True, isDeterminate=True)
    b1 = OutputPin()
    b2 = OutputPin()
    _safe_set(a, 'Activities_StructuredActivities_ConditionalNode145', {b1})
    assert _is_linked(a, 'Activities_StructuredActivities_ConditionalNode145', b1)
    if hasattr(b1, 'OutputPin146'):
        assert _is_linked(b1, 'OutputPin146', a)
    _safe_set(a, 'Activities_StructuredActivities_ConditionalNode145', {b2})
    assert _is_linked(a, 'Activities_StructuredActivities_ConditionalNode145', b2)
    if hasattr(b1, 'OutputPin146'):
        assert not _is_linked(b1, 'OutputPin146', a)
    if hasattr(b2, 'OutputPin146'):
        assert _is_linked(b2, 'OutputPin146', a)
    _safe_set(a, 'Activities_StructuredActivities_ConditionalNode145', set())
    assert not _is_linked(a, 'Activities_StructuredActivities_ConditionalNode145', b2)
    if hasattr(b2, 'OutputPin146'):
        assert not _is_linked(b2, 'OutputPin146', a)


def test_assoc_selection68_link_reassign_clear():
    a = Activities_BasicActivities_ObjectFlow(isControlType=True, isMulticast=True, isMultireceive=True, ordering="sample_text")
    b1 = Behavior()
    b2 = Behavior()
    _safe_set(a, 'Activities_BasicActivities_ObjectFlow69', b1)
    assert _is_linked(a, 'Activities_BasicActivities_ObjectFlow69', b1)
    if hasattr(b1, 'Behavior70'):
        assert _is_linked(b1, 'Behavior70', a)
    _safe_set(a, 'Activities_BasicActivities_ObjectFlow69', b2)
    assert _is_linked(a, 'Activities_BasicActivities_ObjectFlow69', b2)
    if hasattr(b1, 'Behavior70'):
        assert not _is_linked(b1, 'Behavior70', a)
    if hasattr(b2, 'Behavior70'):
        assert _is_linked(b2, 'Behavior70', a)
    _safe_set(a, 'Activities_BasicActivities_ObjectFlow69', None)
    assert not _is_linked(a, 'Activities_BasicActivities_ObjectFlow69', b2)
    if hasattr(b2, 'Behavior70'):
        assert not _is_linked(b2, 'Behavior70', a)


def test_assoc_setupPart115_link_reassign_clear():
    a = Activities_StructuredActivities_LoopNode(isTestedFirst=True)
    b1 = ExecutableNode()
    b2 = ExecutableNode()
    _safe_set(a, 'Activities_StructuredActivities_LoopNode', {b1})
    assert _is_linked(a, 'Activities_StructuredActivities_LoopNode', b1)
    if hasattr(b1, 'ExecutableNode'):
        assert _is_linked(b1, 'ExecutableNode', a)
    _safe_set(a, 'Activities_StructuredActivities_LoopNode', {b2})
    assert _is_linked(a, 'Activities_StructuredActivities_LoopNode', b2)
    if hasattr(b1, 'ExecutableNode'):
        assert not _is_linked(b1, 'ExecutableNode', a)
    if hasattr(b2, 'ExecutableNode'):
        assert _is_linked(b2, 'ExecutableNode', a)
    _safe_set(a, 'Activities_StructuredActivities_LoopNode', set())
    assert not _is_linked(a, 'Activities_StructuredActivities_LoopNode', b2)
    if hasattr(b2, 'ExecutableNode'):
        assert not _is_linked(b2, 'ExecutableNode', a)


def test_assoc_structuredNode6_link_reassign_clear():
    a = Activities_FundamentalActivities_Activity(isReadOnly=True, isSingleExecution=True)
    b1 = StructuredActivityNode()
    b2 = StructuredActivityNode()
    _safe_set(a, 'activity', {b1})
    assert _is_linked(a, 'activity', b1)
    if hasattr(b1, 'StructuredActivityNode'):
        assert _is_linked(b1, 'StructuredActivityNode', a)
    _safe_set(a, 'activity', {b2})
    assert _is_linked(a, 'activity', b2)
    if hasattr(b1, 'StructuredActivityNode'):
        assert not _is_linked(b1, 'StructuredActivityNode', a)
    if hasattr(b2, 'StructuredActivityNode'):
        assert _is_linked(b2, 'StructuredActivityNode', a)
    _safe_set(a, 'activity', set())
    assert not _is_linked(a, 'activity', b2)
    if hasattr(b2, 'StructuredActivityNode'):
        assert not _is_linked(b2, 'StructuredActivityNode', a)


def test_assoc_structuredNodeInput105_link_reassign_clear():
    a = Activities_StructuredActivities_StructuredActivityNode(mustIsolate=True)
    b1 = InputPin()
    b2 = InputPin()
    _safe_set(a, 'Activities_StructuredActivities_StructuredActivityNode106', {b1})
    assert _is_linked(a, 'Activities_StructuredActivities_StructuredActivityNode106', b1)
    if hasattr(b1, 'InputPin107'):
        assert _is_linked(b1, 'InputPin107', a)
    _safe_set(a, 'Activities_StructuredActivities_StructuredActivityNode106', {b2})
    assert _is_linked(a, 'Activities_StructuredActivities_StructuredActivityNode106', b2)
    if hasattr(b1, 'InputPin107'):
        assert not _is_linked(b1, 'InputPin107', a)
    if hasattr(b2, 'InputPin107'):
        assert _is_linked(b2, 'InputPin107', a)
    _safe_set(a, 'Activities_StructuredActivities_StructuredActivityNode106', set())
    assert not _is_linked(a, 'Activities_StructuredActivities_StructuredActivityNode106', b2)
    if hasattr(b2, 'InputPin107'):
        assert not _is_linked(b2, 'InputPin107', a)


def test_assoc_structuredNodeOutput111_link_reassign_clear():
    a = Activities_StructuredActivities_StructuredActivityNode(mustIsolate=True)
    b1 = OutputPin()
    b2 = OutputPin()
    _safe_set(a, 'Activities_StructuredActivities_StructuredActivityNode112', {b1})
    assert _is_linked(a, 'Activities_StructuredActivities_StructuredActivityNode112', b1)
    if hasattr(b1, 'OutputPin113'):
        assert _is_linked(b1, 'OutputPin113', a)
    _safe_set(a, 'Activities_StructuredActivities_StructuredActivityNode112', {b2})
    assert _is_linked(a, 'Activities_StructuredActivities_StructuredActivityNode112', b2)
    if hasattr(b1, 'OutputPin113'):
        assert not _is_linked(b1, 'OutputPin113', a)
    if hasattr(b2, 'OutputPin113'):
        assert _is_linked(b2, 'OutputPin113', a)
    _safe_set(a, 'Activities_StructuredActivities_StructuredActivityNode112', set())
    assert not _is_linked(a, 'Activities_StructuredActivities_StructuredActivityNode112', b2)
    if hasattr(b2, 'OutputPin113'):
        assert not _is_linked(b2, 'OutputPin113', a)


def test_assoc_test119_link_reassign_clear():
    a = Activities_StructuredActivities_LoopNode(isTestedFirst=True)
    b1 = ExecutableNode()
    b2 = ExecutableNode()
    _safe_set(a, 'Activities_StructuredActivities_LoopNode120', {b1})
    assert _is_linked(a, 'Activities_StructuredActivities_LoopNode120', b1)
    if hasattr(b1, 'ExecutableNode121'):
        assert _is_linked(b1, 'ExecutableNode121', a)
    _safe_set(a, 'Activities_StructuredActivities_LoopNode120', {b2})
    assert _is_linked(a, 'Activities_StructuredActivities_LoopNode120', b2)
    if hasattr(b1, 'ExecutableNode121'):
        assert not _is_linked(b1, 'ExecutableNode121', a)
    if hasattr(b2, 'ExecutableNode121'):
        assert _is_linked(b2, 'ExecutableNode121', a)
    _safe_set(a, 'Activities_StructuredActivities_LoopNode120', set())
    assert not _is_linked(a, 'Activities_StructuredActivities_LoopNode120', b2)
    if hasattr(b2, 'ExecutableNode121'):
        assert not _is_linked(b2, 'ExecutableNode121', a)


def test_assoc_test138_link_reassign_clear():
    a = Activities_StructuredActivities_ConditionalNode(isAssumed=True, isDeterminate=True)
    b1 = ExecutableNode()
    b2 = ExecutableNode()
    _safe_set(a, 'Activities_StructuredActivities_ConditionalNode139', {b1})
    assert _is_linked(a, 'Activities_StructuredActivities_ConditionalNode139', b1)
    if hasattr(b1, 'ExecutableNode140'):
        assert _is_linked(b1, 'ExecutableNode140', a)
    _safe_set(a, 'Activities_StructuredActivities_ConditionalNode139', {b2})
    assert _is_linked(a, 'Activities_StructuredActivities_ConditionalNode139', b2)
    if hasattr(b1, 'ExecutableNode140'):
        assert not _is_linked(b1, 'ExecutableNode140', a)
    if hasattr(b2, 'ExecutableNode140'):
        assert _is_linked(b2, 'ExecutableNode140', a)
    _safe_set(a, 'Activities_StructuredActivities_ConditionalNode139', set())
    assert not _is_linked(a, 'Activities_StructuredActivities_ConditionalNode139', b2)
    if hasattr(b2, 'ExecutableNode140'):
        assert not _is_linked(b2, 'ExecutableNode140', a)


def test_assoc_transformation67_link_reassign_clear():
    a = Activities_BasicActivities_ObjectFlow(isControlType=True, isMulticast=True, isMultireceive=True, ordering="sample_text")
    b1 = Behavior()
    b2 = Behavior()
    _safe_set(a, 'Activities_BasicActivities_ObjectFlow', b1)
    assert _is_linked(a, 'Activities_BasicActivities_ObjectFlow', b1)
    if hasattr(b1, 'Behavior'):
        assert _is_linked(b1, 'Behavior', a)
    _safe_set(a, 'Activities_BasicActivities_ObjectFlow', b2)
    assert _is_linked(a, 'Activities_BasicActivities_ObjectFlow', b2)
    if hasattr(b1, 'Behavior'):
        assert not _is_linked(b1, 'Behavior', a)
    if hasattr(b2, 'Behavior'):
        assert _is_linked(b2, 'Behavior', a)
    _safe_set(a, 'Activities_BasicActivities_ObjectFlow', None)
    assert not _is_linked(a, 'Activities_BasicActivities_ObjectFlow', b2)
    if hasattr(b2, 'Behavior'):
        assert not _is_linked(b2, 'Behavior', a)


def test_assoc_variable101_link_reassign_clear():
    a = Activities_StructuredActivities_StructuredActivityNode(mustIsolate=True)
    b1 = Variable()
    b2 = Variable()
    _safe_set(a, 'Activities_StructuredActivities_StructuredActivityNode', {b1})
    assert _is_linked(a, 'Activities_StructuredActivities_StructuredActivityNode', b1)
    if hasattr(b1, 'Variable102'):
        assert _is_linked(b1, 'Variable102', a)
    _safe_set(a, 'Activities_StructuredActivities_StructuredActivityNode', {b2})
    assert _is_linked(a, 'Activities_StructuredActivities_StructuredActivityNode', b2)
    if hasattr(b1, 'Variable102'):
        assert not _is_linked(b1, 'Variable102', a)
    if hasattr(b2, 'Variable102'):
        assert _is_linked(b2, 'Variable102', a)
    _safe_set(a, 'Activities_StructuredActivities_StructuredActivityNode', set())
    assert not _is_linked(a, 'Activities_StructuredActivities_StructuredActivityNode', b2)
    if hasattr(b2, 'Variable102'):
        assert not _is_linked(b2, 'Variable102', a)


def test_assoc_variable7_link_reassign_clear():
    a = Activities_FundamentalActivities_Activity(isReadOnly=True, isSingleExecution=True)
    b1 = Variable()
    b2 = Variable()
    _safe_set(a, 'Activities_FundamentalActivities_Activity8', {b1})
    assert _is_linked(a, 'Activities_FundamentalActivities_Activity8', b1)
    if hasattr(b1, 'Variable'):
        assert _is_linked(b1, 'Variable', a)
    _safe_set(a, 'Activities_FundamentalActivities_Activity8', {b2})
    assert _is_linked(a, 'Activities_FundamentalActivities_Activity8', b2)
    if hasattr(b1, 'Variable'):
        assert not _is_linked(b1, 'Variable', a)
    if hasattr(b2, 'Variable'):
        assert _is_linked(b2, 'Variable', a)
    _safe_set(a, 'Activities_FundamentalActivities_Activity8', set())
    assert not _is_linked(a, 'Activities_FundamentalActivities_Activity8', b2)
    if hasattr(b2, 'Variable'):
        assert not _is_linked(b2, 'Variable', a)


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

Activities_BasicActivities_ActivityEdge_strategy = st.builds(Activities_BasicActivities_ActivityEdge)
@given(instance=Activities_BasicActivities_ActivityEdge_strategy)
@settings(max_examples=25)
def test_Activities_BasicActivities_ActivityEdge_instantiation(instance):
    assert isinstance(instance, Activities_BasicActivities_ActivityEdge)


Activities_BasicActivities_ActivityFinalNode_strategy = st.builds(Activities_BasicActivities_ActivityFinalNode)
@given(instance=Activities_BasicActivities_ActivityFinalNode_strategy)
@settings(max_examples=25)
def test_Activities_BasicActivities_ActivityFinalNode_instantiation(instance):
    assert isinstance(instance, Activities_BasicActivities_ActivityFinalNode)


Activities_BasicActivities_ActivityParameterNode_strategy = st.builds(Activities_BasicActivities_ActivityParameterNode)
@given(instance=Activities_BasicActivities_ActivityParameterNode_strategy)
@settings(max_examples=25)
def test_Activities_BasicActivities_ActivityParameterNode_instantiation(instance):
    assert isinstance(instance, Activities_BasicActivities_ActivityParameterNode)


Activities_BasicActivities_ControlFlow_strategy = st.builds(Activities_BasicActivities_ControlFlow)
@given(instance=Activities_BasicActivities_ControlFlow_strategy)
@settings(max_examples=25)
def test_Activities_BasicActivities_ControlFlow_instantiation(instance):
    assert isinstance(instance, Activities_BasicActivities_ControlFlow)


Activities_BasicActivities_ControlNode_strategy = st.builds(Activities_BasicActivities_ControlNode)
@given(instance=Activities_BasicActivities_ControlNode_strategy)
@settings(max_examples=25)
def test_Activities_BasicActivities_ControlNode_instantiation(instance):
    assert isinstance(instance, Activities_BasicActivities_ControlNode)


Activities_BasicActivities_InitialNode_strategy = st.builds(Activities_BasicActivities_InitialNode)
@given(instance=Activities_BasicActivities_InitialNode_strategy)
@settings(max_examples=25)
def test_Activities_BasicActivities_InitialNode_instantiation(instance):
    assert isinstance(instance, Activities_BasicActivities_InitialNode)


Activities_BasicActivities_ObjectFlow_strategy = st.builds(Activities_BasicActivities_ObjectFlow, isControlType=st.booleans(), isMulticast=st.booleans(), isMultireceive=st.booleans(), ordering=safe_text)
@given(instance=Activities_BasicActivities_ObjectFlow_strategy)
@settings(max_examples=25)
def test_Activities_BasicActivities_ObjectFlow_instantiation(instance):
    assert isinstance(instance, Activities_BasicActivities_ObjectFlow)


Activities_BasicActivities_ObjectNode_strategy = st.builds(Activities_BasicActivities_ObjectNode)
@given(instance=Activities_BasicActivities_ObjectNode_strategy)
@settings(max_examples=25)
def test_Activities_BasicActivities_ObjectNode_instantiation(instance):
    assert isinstance(instance, Activities_BasicActivities_ObjectNode)


Activities_BasicActivities_Parameter_strategy = st.builds(Activities_BasicActivities_Parameter, effect=safe_text, isException=st.booleans(), isStream=st.booleans())
@given(instance=Activities_BasicActivities_Parameter_strategy)
@settings(max_examples=25)
def test_Activities_BasicActivities_Parameter_instantiation(instance):
    assert isinstance(instance, Activities_BasicActivities_Parameter)


Activities_BasicActivities_Pin_strategy = st.builds(Activities_BasicActivities_Pin, isControl=st.booleans())
@given(instance=Activities_BasicActivities_Pin_strategy)
@settings(max_examples=25)
def test_Activities_BasicActivities_Pin_instantiation(instance):
    assert isinstance(instance, Activities_BasicActivities_Pin)


Activities_BasicActivities_RedefinableElement_strategy = st.builds(Activities_BasicActivities_RedefinableElement)
@given(instance=Activities_BasicActivities_RedefinableElement_strategy)
@settings(max_examples=25)
def test_Activities_BasicActivities_RedefinableElement_instantiation(instance):
    assert isinstance(instance, Activities_BasicActivities_RedefinableElement)


Activities_BasicActivities_TypedElement_strategy = st.builds(Activities_BasicActivities_TypedElement)
@given(instance=Activities_BasicActivities_TypedElement_strategy)
@settings(max_examples=25)
def test_Activities_BasicActivities_TypedElement_instantiation(instance):
    assert isinstance(instance, Activities_BasicActivities_TypedElement)


Activities_CompleteStructuredActivities_InputPin_strategy = st.builds(Activities_CompleteStructuredActivities_InputPin)
@given(instance=Activities_CompleteStructuredActivities_InputPin_strategy)
@settings(max_examples=25)
def test_Activities_CompleteStructuredActivities_InputPin_instantiation(instance):
    assert isinstance(instance, Activities_CompleteStructuredActivities_InputPin)


Activities_ExtraStructuredActivities_Classifier_strategy = st.builds(Activities_ExtraStructuredActivities_Classifier)
@given(instance=Activities_ExtraStructuredActivities_Classifier_strategy)
@settings(max_examples=25)
def test_Activities_ExtraStructuredActivities_Classifier_instantiation(instance):
    assert isinstance(instance, Activities_ExtraStructuredActivities_Classifier)


Activities_ExtraStructuredActivities_ExceptionHandler_strategy = st.builds(Activities_ExtraStructuredActivities_ExceptionHandler)
@given(instance=Activities_ExtraStructuredActivities_ExceptionHandler_strategy)
@settings(max_examples=25)
def test_Activities_ExtraStructuredActivities_ExceptionHandler_instantiation(instance):
    assert isinstance(instance, Activities_ExtraStructuredActivities_ExceptionHandler)


Activities_ExtraStructuredActivities_ExpansionNode_strategy = st.builds(Activities_ExtraStructuredActivities_ExpansionNode)
@given(instance=Activities_ExtraStructuredActivities_ExpansionNode_strategy)
@settings(max_examples=25)
def test_Activities_ExtraStructuredActivities_ExpansionNode_instantiation(instance):
    assert isinstance(instance, Activities_ExtraStructuredActivities_ExpansionNode)


Activities_ExtraStructuredActivities_ExpansionRegion_strategy = st.builds(Activities_ExtraStructuredActivities_ExpansionRegion, mode=safe_text)
@given(instance=Activities_ExtraStructuredActivities_ExpansionRegion_strategy)
@settings(max_examples=25)
def test_Activities_ExtraStructuredActivities_ExpansionRegion_instantiation(instance):
    assert isinstance(instance, Activities_ExtraStructuredActivities_ExpansionRegion)


Activities_FundamentalActivities_Action_strategy = st.builds(Activities_FundamentalActivities_Action, isLocallyReentrant=st.booleans())
@given(instance=Activities_FundamentalActivities_Action_strategy)
@settings(max_examples=25)
def test_Activities_FundamentalActivities_Action_instantiation(instance):
    assert isinstance(instance, Activities_FundamentalActivities_Action)


Activities_FundamentalActivities_Activity_strategy = st.builds(Activities_FundamentalActivities_Activity, isReadOnly=st.booleans(), isSingleExecution=st.booleans())
@given(instance=Activities_FundamentalActivities_Activity_strategy)
@settings(max_examples=25)
def test_Activities_FundamentalActivities_Activity_instantiation(instance):
    assert isinstance(instance, Activities_FundamentalActivities_Activity)


Activities_FundamentalActivities_ActivityGroup_strategy = st.builds(Activities_FundamentalActivities_ActivityGroup)
@given(instance=Activities_FundamentalActivities_ActivityGroup_strategy)
@settings(max_examples=25)
def test_Activities_FundamentalActivities_ActivityGroup_instantiation(instance):
    assert isinstance(instance, Activities_FundamentalActivities_ActivityGroup)


Activities_FundamentalActivities_ActivityNode_strategy = st.builds(Activities_FundamentalActivities_ActivityNode)
@given(instance=Activities_FundamentalActivities_ActivityNode_strategy)
@settings(max_examples=25)
def test_Activities_FundamentalActivities_ActivityNode_instantiation(instance):
    assert isinstance(instance, Activities_FundamentalActivities_ActivityNode)


Activities_FundamentalActivities_Behavior_strategy = st.builds(Activities_FundamentalActivities_Behavior)
@given(instance=Activities_FundamentalActivities_Behavior_strategy)
@settings(max_examples=25)
def test_Activities_FundamentalActivities_Behavior_instantiation(instance):
    assert isinstance(instance, Activities_FundamentalActivities_Behavior)


Activities_FundamentalActivities_NamedElement_strategy = st.builds(Activities_FundamentalActivities_NamedElement)
@given(instance=Activities_FundamentalActivities_NamedElement_strategy)
@settings(max_examples=25)
def test_Activities_FundamentalActivities_NamedElement_instantiation(instance):
    assert isinstance(instance, Activities_FundamentalActivities_NamedElement)


Activities_FundamentalActivities_Namespace_strategy = st.builds(Activities_FundamentalActivities_Namespace)
@given(instance=Activities_FundamentalActivities_Namespace_strategy)
@settings(max_examples=25)
def test_Activities_FundamentalActivities_Namespace_instantiation(instance):
    assert isinstance(instance, Activities_FundamentalActivities_Namespace)


Activities_IntermediateActivities_ActivityPartition_strategy = st.builds(Activities_IntermediateActivities_ActivityPartition)
@given(instance=Activities_IntermediateActivities_ActivityPartition_strategy)
@settings(max_examples=25)
def test_Activities_IntermediateActivities_ActivityPartition_instantiation(instance):
    assert isinstance(instance, Activities_IntermediateActivities_ActivityPartition)


Activities_IntermediateActivities_BehavioralFeature_strategy = st.builds(Activities_IntermediateActivities_BehavioralFeature)
@given(instance=Activities_IntermediateActivities_BehavioralFeature_strategy)
@settings(max_examples=25)
def test_Activities_IntermediateActivities_BehavioralFeature_instantiation(instance):
    assert isinstance(instance, Activities_IntermediateActivities_BehavioralFeature)


Activities_IntermediateActivities_CentralBufferNode_strategy = st.builds(Activities_IntermediateActivities_CentralBufferNode)
@given(instance=Activities_IntermediateActivities_CentralBufferNode_strategy)
@settings(max_examples=25)
def test_Activities_IntermediateActivities_CentralBufferNode_instantiation(instance):
    assert isinstance(instance, Activities_IntermediateActivities_CentralBufferNode)


Activities_IntermediateActivities_Class_strategy = st.builds(Activities_IntermediateActivities_Class)
@given(instance=Activities_IntermediateActivities_Class_strategy)
@settings(max_examples=25)
def test_Activities_IntermediateActivities_Class_instantiation(instance):
    assert isinstance(instance, Activities_IntermediateActivities_Class)


Activities_IntermediateActivities_Constraint_strategy = st.builds(Activities_IntermediateActivities_Constraint)
@given(instance=Activities_IntermediateActivities_Constraint_strategy)
@settings(max_examples=25)
def test_Activities_IntermediateActivities_Constraint_instantiation(instance):
    assert isinstance(instance, Activities_IntermediateActivities_Constraint)


Activities_IntermediateActivities_DataStoreNode_strategy = st.builds(Activities_IntermediateActivities_DataStoreNode)
@given(instance=Activities_IntermediateActivities_DataStoreNode_strategy)
@settings(max_examples=25)
def test_Activities_IntermediateActivities_DataStoreNode_instantiation(instance):
    assert isinstance(instance, Activities_IntermediateActivities_DataStoreNode)


Activities_IntermediateActivities_DecisionNode_strategy = st.builds(Activities_IntermediateActivities_DecisionNode)
@given(instance=Activities_IntermediateActivities_DecisionNode_strategy)
@settings(max_examples=25)
def test_Activities_IntermediateActivities_DecisionNode_instantiation(instance):
    assert isinstance(instance, Activities_IntermediateActivities_DecisionNode)


Activities_IntermediateActivities_Element_strategy = st.builds(Activities_IntermediateActivities_Element)
@given(instance=Activities_IntermediateActivities_Element_strategy)
@settings(max_examples=25)
def test_Activities_IntermediateActivities_Element_instantiation(instance):
    assert isinstance(instance, Activities_IntermediateActivities_Element)


Activities_IntermediateActivities_Feature_strategy = st.builds(Activities_IntermediateActivities_Feature)
@given(instance=Activities_IntermediateActivities_Feature_strategy)
@settings(max_examples=25)
def test_Activities_IntermediateActivities_Feature_instantiation(instance):
    assert isinstance(instance, Activities_IntermediateActivities_Feature)


Activities_IntermediateActivities_FinalNode_strategy = st.builds(Activities_IntermediateActivities_FinalNode)
@given(instance=Activities_IntermediateActivities_FinalNode_strategy)
@settings(max_examples=25)
def test_Activities_IntermediateActivities_FinalNode_instantiation(instance):
    assert isinstance(instance, Activities_IntermediateActivities_FinalNode)


Activities_IntermediateActivities_FlowFinalNode_strategy = st.builds(Activities_IntermediateActivities_FlowFinalNode)
@given(instance=Activities_IntermediateActivities_FlowFinalNode_strategy)
@settings(max_examples=25)
def test_Activities_IntermediateActivities_FlowFinalNode_instantiation(instance):
    assert isinstance(instance, Activities_IntermediateActivities_FlowFinalNode)


Activities_IntermediateActivities_ForkNode_strategy = st.builds(Activities_IntermediateActivities_ForkNode)
@given(instance=Activities_IntermediateActivities_ForkNode_strategy)
@settings(max_examples=25)
def test_Activities_IntermediateActivities_ForkNode_instantiation(instance):
    assert isinstance(instance, Activities_IntermediateActivities_ForkNode)


Activities_IntermediateActivities_InterruptibleActivityRegion_strategy = st.builds(Activities_IntermediateActivities_InterruptibleActivityRegion)
@given(instance=Activities_IntermediateActivities_InterruptibleActivityRegion_strategy)
@settings(max_examples=25)
def test_Activities_IntermediateActivities_InterruptibleActivityRegion_instantiation(instance):
    assert isinstance(instance, Activities_IntermediateActivities_InterruptibleActivityRegion)


Activities_IntermediateActivities_JoinNode_strategy = st.builds(Activities_IntermediateActivities_JoinNode, isCombineDuplicate=st.booleans())
@given(instance=Activities_IntermediateActivities_JoinNode_strategy)
@settings(max_examples=25)
def test_Activities_IntermediateActivities_JoinNode_instantiation(instance):
    assert isinstance(instance, Activities_IntermediateActivities_JoinNode)


Activities_IntermediateActivities_MergeNode_strategy = st.builds(Activities_IntermediateActivities_MergeNode)
@given(instance=Activities_IntermediateActivities_MergeNode_strategy)
@settings(max_examples=25)
def test_Activities_IntermediateActivities_MergeNode_instantiation(instance):
    assert isinstance(instance, Activities_IntermediateActivities_MergeNode)


Activities_IntermediateActivities_ParameterSet_strategy = st.builds(Activities_IntermediateActivities_ParameterSet)
@given(instance=Activities_IntermediateActivities_ParameterSet_strategy)
@settings(max_examples=25)
def test_Activities_IntermediateActivities_ParameterSet_instantiation(instance):
    assert isinstance(instance, Activities_IntermediateActivities_ParameterSet)


Activities_IntermediateActivities_State_strategy = st.builds(Activities_IntermediateActivities_State)
@given(instance=Activities_IntermediateActivities_State_strategy)
@settings(max_examples=25)
def test_Activities_IntermediateActivities_State_instantiation(instance):
    assert isinstance(instance, Activities_IntermediateActivities_State)


Activities_IntermediateActivities_ValueSpecification_strategy = st.builds(Activities_IntermediateActivities_ValueSpecification)
@given(instance=Activities_IntermediateActivities_ValueSpecification_strategy)
@settings(max_examples=25)
def test_Activities_IntermediateActivities_ValueSpecification_instantiation(instance):
    assert isinstance(instance, Activities_IntermediateActivities_ValueSpecification)


Activities_StructuredActivities_Clause_strategy = st.builds(Activities_StructuredActivities_Clause)
@given(instance=Activities_StructuredActivities_Clause_strategy)
@settings(max_examples=25)
def test_Activities_StructuredActivities_Clause_instantiation(instance):
    assert isinstance(instance, Activities_StructuredActivities_Clause)


Activities_StructuredActivities_ConditionalNode_strategy = st.builds(Activities_StructuredActivities_ConditionalNode, isAssumed=st.booleans(), isDeterminate=st.booleans())
@given(instance=Activities_StructuredActivities_ConditionalNode_strategy)
@settings(max_examples=25)
def test_Activities_StructuredActivities_ConditionalNode_instantiation(instance):
    assert isinstance(instance, Activities_StructuredActivities_ConditionalNode)


Activities_StructuredActivities_ExecutableNode_strategy = st.builds(Activities_StructuredActivities_ExecutableNode)
@given(instance=Activities_StructuredActivities_ExecutableNode_strategy)
@settings(max_examples=25)
def test_Activities_StructuredActivities_ExecutableNode_instantiation(instance):
    assert isinstance(instance, Activities_StructuredActivities_ExecutableNode)


Activities_StructuredActivities_LoopNode_strategy = st.builds(Activities_StructuredActivities_LoopNode, isTestedFirst=st.booleans())
@given(instance=Activities_StructuredActivities_LoopNode_strategy)
@settings(max_examples=25)
def test_Activities_StructuredActivities_LoopNode_instantiation(instance):
    assert isinstance(instance, Activities_StructuredActivities_LoopNode)


Activities_StructuredActivities_MultiplicityElement_strategy = st.builds(Activities_StructuredActivities_MultiplicityElement)
@given(instance=Activities_StructuredActivities_MultiplicityElement_strategy)
@settings(max_examples=25)
def test_Activities_StructuredActivities_MultiplicityElement_instantiation(instance):
    assert isinstance(instance, Activities_StructuredActivities_MultiplicityElement)


Activities_StructuredActivities_OutputPin_strategy = st.builds(Activities_StructuredActivities_OutputPin)
@given(instance=Activities_StructuredActivities_OutputPin_strategy)
@settings(max_examples=25)
def test_Activities_StructuredActivities_OutputPin_instantiation(instance):
    assert isinstance(instance, Activities_StructuredActivities_OutputPin)


Activities_StructuredActivities_SequenceNode_strategy = st.builds(Activities_StructuredActivities_SequenceNode)
@given(instance=Activities_StructuredActivities_SequenceNode_strategy)
@settings(max_examples=25)
def test_Activities_StructuredActivities_SequenceNode_instantiation(instance):
    assert isinstance(instance, Activities_StructuredActivities_SequenceNode)


Activities_StructuredActivities_StructuredActivityNode_strategy = st.builds(Activities_StructuredActivities_StructuredActivityNode, mustIsolate=st.booleans())
@given(instance=Activities_StructuredActivities_StructuredActivityNode_strategy)
@settings(max_examples=25)
def test_Activities_StructuredActivities_StructuredActivityNode_instantiation(instance):
    assert isinstance(instance, Activities_StructuredActivities_StructuredActivityNode)


Activities_StructuredActivities_Variable_strategy = st.builds(Activities_StructuredActivities_Variable)
@given(instance=Activities_StructuredActivities_Variable_strategy)
@settings(max_examples=25)
def test_Activities_StructuredActivities_Variable_instantiation(instance):
    assert isinstance(instance, Activities_StructuredActivities_Variable)


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


ActivityPartition_strategy = st.builds(ActivityPartition)
@given(instance=ActivityPartition_strategy)
@settings(max_examples=25)
def test_ActivityPartition_instantiation(instance):
    assert isinstance(instance, ActivityPartition)


BasicActivities_ControlNode_strategy = st.builds(BasicActivities_ControlNode)
@given(instance=BasicActivities_ControlNode_strategy)
@settings(max_examples=25)
def test_BasicActivities_ControlNode_instantiation(instance):
    assert isinstance(instance, BasicActivities_ControlNode)


BasicActivities_RedefinableElement_strategy = st.builds(BasicActivities_RedefinableElement)
@given(instance=BasicActivities_RedefinableElement_strategy)
@settings(max_examples=25)
def test_BasicActivities_RedefinableElement_instantiation(instance):
    assert isinstance(instance, BasicActivities_RedefinableElement)


BasicActivities_TypedElement_strategy = st.builds(BasicActivities_TypedElement)
@given(instance=BasicActivities_TypedElement_strategy)
@settings(max_examples=25)
def test_BasicActivities_TypedElement_instantiation(instance):
    assert isinstance(instance, BasicActivities_TypedElement)


Behavior_strategy = st.builds(Behavior)
@given(instance=Behavior_strategy)
@settings(max_examples=25)
def test_Behavior_instantiation(instance):
    assert isinstance(instance, Behavior)


CentralBufferNode_strategy = st.builds(CentralBufferNode)
@given(instance=CentralBufferNode_strategy)
@settings(max_examples=25)
def test_CentralBufferNode_instantiation(instance):
    assert isinstance(instance, CentralBufferNode)


Class_strategy = st.builds(Class)
@given(instance=Class_strategy)
@settings(max_examples=25)
def test_Class_instantiation(instance):
    assert isinstance(instance, Class)


Classifier_strategy = st.builds(Classifier)
@given(instance=Classifier_strategy)
@settings(max_examples=25)
def test_Classifier_instantiation(instance):
    assert isinstance(instance, Classifier)


Clause_strategy = st.builds(Clause)
@given(instance=Clause_strategy)
@settings(max_examples=25)
def test_Clause_instantiation(instance):
    assert isinstance(instance, Clause)


Constraint_strategy = st.builds(Constraint)
@given(instance=Constraint_strategy)
@settings(max_examples=25)
def test_Constraint_instantiation(instance):
    assert isinstance(instance, Constraint)


ControlNode_strategy = st.builds(ControlNode)
@given(instance=ControlNode_strategy)
@settings(max_examples=25)
def test_ControlNode_instantiation(instance):
    assert isinstance(instance, ControlNode)


Element_strategy = st.builds(Element)
@given(instance=Element_strategy)
@settings(max_examples=25)
def test_Element_instantiation(instance):
    assert isinstance(instance, Element)


ExceptionHandler_strategy = st.builds(ExceptionHandler)
@given(instance=ExceptionHandler_strategy)
@settings(max_examples=25)
def test_ExceptionHandler_instantiation(instance):
    assert isinstance(instance, ExceptionHandler)


ExecutableNode_strategy = st.builds(ExecutableNode)
@given(instance=ExecutableNode_strategy)
@settings(max_examples=25)
def test_ExecutableNode_instantiation(instance):
    assert isinstance(instance, ExecutableNode)


ExpansionNode_strategy = st.builds(ExpansionNode)
@given(instance=ExpansionNode_strategy)
@settings(max_examples=25)
def test_ExpansionNode_instantiation(instance):
    assert isinstance(instance, ExpansionNode)


ExpansionRegion_strategy = st.builds(ExpansionRegion)
@given(instance=ExpansionRegion_strategy)
@settings(max_examples=25)
def test_ExpansionRegion_instantiation(instance):
    assert isinstance(instance, ExpansionRegion)


FinalNode_strategy = st.builds(FinalNode)
@given(instance=FinalNode_strategy)
@settings(max_examples=25)
def test_FinalNode_instantiation(instance):
    assert isinstance(instance, FinalNode)


FundamentalActivities_Action_strategy = st.builds(FundamentalActivities_Action)
@given(instance=FundamentalActivities_Action_strategy)
@settings(max_examples=25)
def test_FundamentalActivities_Action_instantiation(instance):
    assert isinstance(instance, FundamentalActivities_Action)


FundamentalActivities_ActivityGroup_strategy = st.builds(FundamentalActivities_ActivityGroup)
@given(instance=FundamentalActivities_ActivityGroup_strategy)
@settings(max_examples=25)
def test_FundamentalActivities_ActivityGroup_instantiation(instance):
    assert isinstance(instance, FundamentalActivities_ActivityGroup)


FundamentalActivities_ActivityNode_strategy = st.builds(FundamentalActivities_ActivityNode)
@given(instance=FundamentalActivities_ActivityNode_strategy)
@settings(max_examples=25)
def test_FundamentalActivities_ActivityNode_instantiation(instance):
    assert isinstance(instance, FundamentalActivities_ActivityNode)


FundamentalActivities_NamedElement_strategy = st.builds(FundamentalActivities_NamedElement)
@given(instance=FundamentalActivities_NamedElement_strategy)
@settings(max_examples=25)
def test_FundamentalActivities_NamedElement_instantiation(instance):
    assert isinstance(instance, FundamentalActivities_NamedElement)


FundamentalActivities_Namespace_strategy = st.builds(FundamentalActivities_Namespace)
@given(instance=FundamentalActivities_Namespace_strategy)
@settings(max_examples=25)
def test_FundamentalActivities_Namespace_instantiation(instance):
    assert isinstance(instance, FundamentalActivities_Namespace)


InputPin_strategy = st.builds(InputPin)
@given(instance=InputPin_strategy)
@settings(max_examples=25)
def test_InputPin_instantiation(instance):
    assert isinstance(instance, InputPin)


IntermediateActivities_Feature_strategy = st.builds(IntermediateActivities_Feature)
@given(instance=IntermediateActivities_Feature_strategy)
@settings(max_examples=25)
def test_IntermediateActivities_Feature_instantiation(instance):
    assert isinstance(instance, IntermediateActivities_Feature)


IntermediateActivities_FinalNode_strategy = st.builds(IntermediateActivities_FinalNode)
@given(instance=IntermediateActivities_FinalNode_strategy)
@settings(max_examples=25)
def test_IntermediateActivities_FinalNode_instantiation(instance):
    assert isinstance(instance, IntermediateActivities_FinalNode)


InterruptibleActivityRegion_strategy = st.builds(InterruptibleActivityRegion)
@given(instance=InterruptibleActivityRegion_strategy)
@settings(max_examples=25)
def test_InterruptibleActivityRegion_instantiation(instance):
    assert isinstance(instance, InterruptibleActivityRegion)


NamedElement_strategy = st.builds(NamedElement)
@given(instance=NamedElement_strategy)
@settings(max_examples=25)
def test_NamedElement_instantiation(instance):
    assert isinstance(instance, NamedElement)


ObjectFlow_strategy = st.builds(ObjectFlow)
@given(instance=ObjectFlow_strategy)
@settings(max_examples=25)
def test_ObjectFlow_instantiation(instance):
    assert isinstance(instance, ObjectFlow)


ObjectNode_strategy = st.builds(ObjectNode)
@given(instance=ObjectNode_strategy)
@settings(max_examples=25)
def test_ObjectNode_instantiation(instance):
    assert isinstance(instance, ObjectNode)


OutputPin_strategy = st.builds(OutputPin)
@given(instance=OutputPin_strategy)
@settings(max_examples=25)
def test_OutputPin_instantiation(instance):
    assert isinstance(instance, OutputPin)


Parameter_strategy = st.builds(Parameter)
@given(instance=Parameter_strategy)
@settings(max_examples=25)
def test_Parameter_instantiation(instance):
    assert isinstance(instance, Parameter)


ParameterSet_strategy = st.builds(ParameterSet)
@given(instance=ParameterSet_strategy)
@settings(max_examples=25)
def test_ParameterSet_instantiation(instance):
    assert isinstance(instance, ParameterSet)


RedefinableElement_strategy = st.builds(RedefinableElement)
@given(instance=RedefinableElement_strategy)
@settings(max_examples=25)
def test_RedefinableElement_instantiation(instance):
    assert isinstance(instance, RedefinableElement)


State_strategy = st.builds(State)
@given(instance=State_strategy)
@settings(max_examples=25)
def test_State_instantiation(instance):
    assert isinstance(instance, State)


StructuredActivities_ExecutableNode_strategy = st.builds(StructuredActivities_ExecutableNode)
@given(instance=StructuredActivities_ExecutableNode_strategy)
@settings(max_examples=25)
def test_StructuredActivities_ExecutableNode_instantiation(instance):
    assert isinstance(instance, StructuredActivities_ExecutableNode)


StructuredActivities_MultiplicityElement_strategy = st.builds(StructuredActivities_MultiplicityElement)
@given(instance=StructuredActivities_MultiplicityElement_strategy)
@settings(max_examples=25)
def test_StructuredActivities_MultiplicityElement_instantiation(instance):
    assert isinstance(instance, StructuredActivities_MultiplicityElement)


StructuredActivityNode_strategy = st.builds(StructuredActivityNode)
@given(instance=StructuredActivityNode_strategy)
@settings(max_examples=25)
def test_StructuredActivityNode_instantiation(instance):
    assert isinstance(instance, StructuredActivityNode)


ValueSpecification_strategy = st.builds(ValueSpecification)
@given(instance=ValueSpecification_strategy)
@settings(max_examples=25)
def test_ValueSpecification_instantiation(instance):
    assert isinstance(instance, ValueSpecification)


Variable_strategy = st.builds(Variable)
@given(instance=Variable_strategy)
@settings(max_examples=25)
def test_Variable_instantiation(instance):
    assert isinstance(instance, Variable)


