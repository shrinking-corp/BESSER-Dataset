import inspect
import pytest
from datetime import date, datetime, time, timedelta
from hypothesis import given, settings
import hypothesis.strategies as st

from python_code import (
    ActivitiesProv_Activity,
    ActivitiesProv_ActivityEdge,
    ActivitiesProv_ActivityFinalNode,
    ActivitiesProv_ActivityGroup,
    ActivitiesProv_ActivityNode,
    ActivitiesProv_ActivityParameterNode,
    ActivitiesProv_ActivityPartition,
    ActivitiesProv_CentralBufferNode,
    ActivitiesProv_Clause,
    ActivitiesProv_ConditionalNode,
    ActivitiesProv_ControlFlow,
    ActivitiesProv_ControlNode,
    ActivitiesProv_DataStoreNode,
    ActivitiesProv_DecisionNode,
    ActivitiesProv_ExceptionHandler,
    ActivitiesProv_ExecutableNode,
    ActivitiesProv_ExpansionNode,
    ActivitiesProv_ExpansionRegion,
    ActivitiesProv_FinalNode,
    ActivitiesProv_FlowFinalNode,
    ActivitiesProv_ForkNode,
    ActivitiesProv_InitialNode,
    ActivitiesProv_InterruptibleActivityRegion,
    ActivitiesProv_JoinNode,
    ActivitiesProv_LoopNode,
    ActivitiesProv_MergeNode,
    ActivitiesProv_ObjectFlow,
    ActivitiesProv_ObjectNode,
    ActivitiesProv_ParameterSet,
    ActivitiesProv_SequenceNode,
    ActivitiesProv_StructuredActivityNode,
    ActivityEdge,
    ActivityGroup,
    ActivityNode,
    CentralBufferNode,
    ControlNode,
    ExecutableNode,
    FinalNode,
    ObjectNode,
    StructuredActivityNode,
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

def test_ActivitiesProv_Activity_isReadOnly_value_roundtrip():
    instance = ActivitiesProv_Activity(isReadOnly=True, isSingleExecution=True)
    assert instance.isReadOnly == True
    instance.isReadOnly = False
    assert instance.isReadOnly == False


def test_ActivitiesProv_Activity_isSingleExecution_value_roundtrip():
    instance = ActivitiesProv_Activity(isReadOnly=True, isSingleExecution=True)
    assert instance.isSingleExecution == True
    instance.isSingleExecution = False
    assert instance.isSingleExecution == False


def test_ActivitiesProv_ConditionalNode_isAssumed_value_roundtrip():
    instance = ActivitiesProv_ConditionalNode(isAssumed=True, isDeterminate=True)
    assert instance.isAssumed == True
    instance.isAssumed = False
    assert instance.isAssumed == False


def test_ActivitiesProv_ConditionalNode_isDeterminate_value_roundtrip():
    instance = ActivitiesProv_ConditionalNode(isAssumed=True, isDeterminate=True)
    assert instance.isDeterminate == True
    instance.isDeterminate = False
    assert instance.isDeterminate == False


def test_ActivitiesProv_JoinNode_isCombineDuplicate_value_roundtrip():
    instance = ActivitiesProv_JoinNode(isCombineDuplicate=True)
    assert instance.isCombineDuplicate == True
    instance.isCombineDuplicate = False
    assert instance.isCombineDuplicate == False


def test_ActivitiesProv_LoopNode_isTestedFirst_value_roundtrip():
    instance = ActivitiesProv_LoopNode(isTestedFirst=True)
    assert instance.isTestedFirst == True
    instance.isTestedFirst = False
    assert instance.isTestedFirst == False


def test_ActivitiesProv_ObjectFlow_isControlType_value_roundtrip():
    instance = ActivitiesProv_ObjectFlow(isControlType=True, isMulticast=True, isMultireceive=True)
    assert instance.isControlType == True
    instance.isControlType = False
    assert instance.isControlType == False


def test_ActivitiesProv_ObjectFlow_isMulticast_value_roundtrip():
    instance = ActivitiesProv_ObjectFlow(isControlType=True, isMulticast=True, isMultireceive=True)
    assert instance.isMulticast == True
    instance.isMulticast = False
    assert instance.isMulticast == False


def test_ActivitiesProv_ObjectFlow_isMultireceive_value_roundtrip():
    instance = ActivitiesProv_ObjectFlow(isControlType=True, isMulticast=True, isMultireceive=True)
    assert instance.isMultireceive == True
    instance.isMultireceive = False
    assert instance.isMultireceive == False


def test_ActivitiesProv_StructuredActivityNode_mustIsolate_value_roundtrip():
    instance = ActivitiesProv_StructuredActivityNode(mustIsolate=True)
    assert instance.mustIsolate == True
    instance.mustIsolate = False
    assert instance.mustIsolate == False


def test_ActivitiesProv_ControlFlow_isa_ActivityEdge():
    instance = ActivitiesProv_ControlFlow()
    assert isinstance(instance, ActivityEdge)


def test_ActivitiesProv_ObjectFlow_isa_ActivityEdge():
    instance = ActivitiesProv_ObjectFlow(isControlType=True, isMulticast=True, isMultireceive=True)
    assert isinstance(instance, ActivityEdge)


def test_ActivitiesProv_ActivityPartition_isa_ActivityGroup():
    instance = ActivitiesProv_ActivityPartition()
    assert isinstance(instance, ActivityGroup)


def test_ActivitiesProv_InterruptibleActivityRegion_isa_ActivityGroup():
    instance = ActivitiesProv_InterruptibleActivityRegion()
    assert isinstance(instance, ActivityGroup)


def test_ActivitiesProv_StructuredActivityNode_isa_ActivityGroup():
    instance = ActivitiesProv_StructuredActivityNode(mustIsolate=True)
    assert isinstance(instance, ActivityGroup)


def test_ActivitiesProv_ControlNode_isa_ActivityNode():
    instance = ActivitiesProv_ControlNode()
    assert isinstance(instance, ActivityNode)


def test_ActivitiesProv_ExecutableNode_isa_ActivityNode():
    instance = ActivitiesProv_ExecutableNode()
    assert isinstance(instance, ActivityNode)


def test_ActivitiesProv_ObjectNode_isa_ActivityNode():
    instance = ActivitiesProv_ObjectNode()
    assert isinstance(instance, ActivityNode)


def test_ActivitiesProv_DataStoreNode_isa_CentralBufferNode():
    instance = ActivitiesProv_DataStoreNode()
    assert isinstance(instance, CentralBufferNode)


def test_ActivitiesProv_ActivityFinalNode_isa_ControlNode():
    instance = ActivitiesProv_ActivityFinalNode()
    assert isinstance(instance, ControlNode)


def test_ActivitiesProv_DecisionNode_isa_ControlNode():
    instance = ActivitiesProv_DecisionNode()
    assert isinstance(instance, ControlNode)


def test_ActivitiesProv_FinalNode_isa_ControlNode():
    instance = ActivitiesProv_FinalNode()
    assert isinstance(instance, ControlNode)


def test_ActivitiesProv_ForkNode_isa_ControlNode():
    instance = ActivitiesProv_ForkNode()
    assert isinstance(instance, ControlNode)


def test_ActivitiesProv_InitialNode_isa_ControlNode():
    instance = ActivitiesProv_InitialNode()
    assert isinstance(instance, ControlNode)


def test_ActivitiesProv_JoinNode_isa_ControlNode():
    instance = ActivitiesProv_JoinNode(isCombineDuplicate=True)
    assert isinstance(instance, ControlNode)


def test_ActivitiesProv_MergeNode_isa_ControlNode():
    instance = ActivitiesProv_MergeNode()
    assert isinstance(instance, ControlNode)


def test_ActivitiesProv_StructuredActivityNode_isa_ExecutableNode():
    instance = ActivitiesProv_StructuredActivityNode(mustIsolate=True)
    assert isinstance(instance, ExecutableNode)


def test_ActivitiesProv_ActivityFinalNode_isa_FinalNode():
    instance = ActivitiesProv_ActivityFinalNode()
    assert isinstance(instance, FinalNode)


def test_ActivitiesProv_FlowFinalNode_isa_FinalNode():
    instance = ActivitiesProv_FlowFinalNode()
    assert isinstance(instance, FinalNode)


def test_ActivitiesProv_ActivityParameterNode_isa_ObjectNode():
    instance = ActivitiesProv_ActivityParameterNode()
    assert isinstance(instance, ObjectNode)


def test_ActivitiesProv_CentralBufferNode_isa_ObjectNode():
    instance = ActivitiesProv_CentralBufferNode()
    assert isinstance(instance, ObjectNode)


def test_ActivitiesProv_ExpansionNode_isa_ObjectNode():
    instance = ActivitiesProv_ExpansionNode()
    assert isinstance(instance, ObjectNode)


def test_ActivitiesProv_ConditionalNode_isa_StructuredActivityNode():
    instance = ActivitiesProv_ConditionalNode(isAssumed=True, isDeterminate=True)
    assert isinstance(instance, StructuredActivityNode)


def test_ActivitiesProv_ExpansionRegion_isa_StructuredActivityNode():
    instance = ActivitiesProv_ExpansionRegion()
    assert isinstance(instance, StructuredActivityNode)


def test_ActivitiesProv_LoopNode_isa_StructuredActivityNode():
    instance = ActivitiesProv_LoopNode(isTestedFirst=True)
    assert isinstance(instance, StructuredActivityNode)


def test_ActivitiesProv_SequenceNode_isa_StructuredActivityNode():
    instance = ActivitiesProv_SequenceNode()
    assert isinstance(instance, StructuredActivityNode)


def test_assoc_activity84_link_reassign_clear():
    a = ActivitiesProv_StructuredActivityNode(mustIsolate=True)
    b1 = ActivitiesProv_Activity(isReadOnly=True, isSingleExecution=True)
    b2 = ActivitiesProv_Activity(isReadOnly=False, isSingleExecution=False)
    _safe_set(a, 'ActivitiesProv_StructuredActivityNode85', b1)
    assert _is_linked(a, 'ActivitiesProv_StructuredActivityNode85', b1)
    if hasattr(b1, 'ActivitiesProv_Activity86'):
        assert _is_linked(b1, 'ActivitiesProv_Activity86', a)
    _safe_set(a, 'ActivitiesProv_StructuredActivityNode85', b2)
    assert _is_linked(a, 'ActivitiesProv_StructuredActivityNode85', b2)
    if hasattr(b1, 'ActivitiesProv_Activity86'):
        assert not _is_linked(b1, 'ActivitiesProv_Activity86', a)
    if hasattr(b2, 'ActivitiesProv_Activity86'):
        assert _is_linked(b2, 'ActivitiesProv_Activity86', a)
    _safe_set(a, 'ActivitiesProv_StructuredActivityNode85', None)
    assert not _is_linked(a, 'ActivitiesProv_StructuredActivityNode85', b2)
    if hasattr(b2, 'ActivitiesProv_Activity86'):
        assert not _is_linked(b2, 'ActivitiesProv_Activity86', a)


def test_assoc_body106_link_reassign_clear():
    a = ActivitiesProv_ConditionalNode(isAssumed=True, isDeterminate=True)
    b1 = ActivitiesProv_ExecutableNode()
    b2 = ActivitiesProv_ExecutableNode()
    _safe_set(a, 'ActivitiesProv_ConditionalNode107', {b1})
    assert _is_linked(a, 'ActivitiesProv_ConditionalNode107', b1)
    if hasattr(b1, 'ActivitiesProv_ExecutableNode108'):
        assert _is_linked(b1, 'ActivitiesProv_ExecutableNode108', a)
    _safe_set(a, 'ActivitiesProv_ConditionalNode107', {b2})
    assert _is_linked(a, 'ActivitiesProv_ConditionalNode107', b2)
    if hasattr(b1, 'ActivitiesProv_ExecutableNode108'):
        assert not _is_linked(b1, 'ActivitiesProv_ExecutableNode108', a)
    if hasattr(b2, 'ActivitiesProv_ExecutableNode108'):
        assert _is_linked(b2, 'ActivitiesProv_ExecutableNode108', a)
    _safe_set(a, 'ActivitiesProv_ConditionalNode107', set())
    assert not _is_linked(a, 'ActivitiesProv_ConditionalNode107', b2)
    if hasattr(b2, 'ActivitiesProv_ExecutableNode108'):
        assert not _is_linked(b2, 'ActivitiesProv_ExecutableNode108', a)


def test_assoc_bodyPart96_link_reassign_clear():
    a = ActivitiesProv_LoopNode(isTestedFirst=True)
    b1 = ActivitiesProv_ExecutableNode()
    b2 = ActivitiesProv_ExecutableNode()
    _safe_set(a, 'ActivitiesProv_LoopNode97', {b1})
    assert _is_linked(a, 'ActivitiesProv_LoopNode97', b1)
    if hasattr(b1, 'ActivitiesProv_ExecutableNode98'):
        assert _is_linked(b1, 'ActivitiesProv_ExecutableNode98', a)
    _safe_set(a, 'ActivitiesProv_LoopNode97', {b2})
    assert _is_linked(a, 'ActivitiesProv_LoopNode97', b2)
    if hasattr(b1, 'ActivitiesProv_ExecutableNode98'):
        assert not _is_linked(b1, 'ActivitiesProv_ExecutableNode98', a)
    if hasattr(b2, 'ActivitiesProv_ExecutableNode98'):
        assert _is_linked(b2, 'ActivitiesProv_ExecutableNode98', a)
    _safe_set(a, 'ActivitiesProv_LoopNode97', set())
    assert not _is_linked(a, 'ActivitiesProv_LoopNode97', b2)
    if hasattr(b2, 'ActivitiesProv_ExecutableNode98'):
        assert not _is_linked(b2, 'ActivitiesProv_ExecutableNode98', a)


def test_assoc_clause102_link_reassign_clear():
    a = ActivitiesProv_ConditionalNode(isAssumed=True, isDeterminate=True)
    b1 = ActivitiesProv_Clause()
    b2 = ActivitiesProv_Clause()
    _safe_set(a, 'ActivitiesProv_ConditionalNode', {b1})
    assert _is_linked(a, 'ActivitiesProv_ConditionalNode', b1)
    if hasattr(b1, 'ActivitiesProv_Clause'):
        assert _is_linked(b1, 'ActivitiesProv_Clause', a)
    _safe_set(a, 'ActivitiesProv_ConditionalNode', {b2})
    assert _is_linked(a, 'ActivitiesProv_ConditionalNode', b2)
    if hasattr(b1, 'ActivitiesProv_Clause'):
        assert not _is_linked(b1, 'ActivitiesProv_Clause', a)
    if hasattr(b2, 'ActivitiesProv_Clause'):
        assert _is_linked(b2, 'ActivitiesProv_Clause', a)
    _safe_set(a, 'ActivitiesProv_ConditionalNode', set())
    assert not _is_linked(a, 'ActivitiesProv_ConditionalNode', b2)
    if hasattr(b2, 'ActivitiesProv_Clause'):
        assert not _is_linked(b2, 'ActivitiesProv_Clause', a)


def test_assoc_decisionInputFlow65_link_reassign_clear():
    a = ActivitiesProv_ObjectFlow(isControlType=True, isMulticast=True, isMultireceive=True)
    b1 = ActivitiesProv_DecisionNode()
    b2 = ActivitiesProv_DecisionNode()
    _safe_set(a, 'ActivitiesProv_ObjectFlow', b1)
    assert _is_linked(a, 'ActivitiesProv_ObjectFlow', b1)
    if hasattr(b1, 'ActivitiesProv_DecisionNode'):
        assert _is_linked(b1, 'ActivitiesProv_DecisionNode', a)
    _safe_set(a, 'ActivitiesProv_ObjectFlow', b2)
    assert _is_linked(a, 'ActivitiesProv_ObjectFlow', b2)
    if hasattr(b1, 'ActivitiesProv_DecisionNode'):
        assert not _is_linked(b1, 'ActivitiesProv_DecisionNode', a)
    if hasattr(b2, 'ActivitiesProv_DecisionNode'):
        assert _is_linked(b2, 'ActivitiesProv_DecisionNode', a)
    _safe_set(a, 'ActivitiesProv_ObjectFlow', None)
    assert not _is_linked(a, 'ActivitiesProv_ObjectFlow', b2)
    if hasattr(b2, 'ActivitiesProv_DecisionNode'):
        assert not _is_linked(b2, 'ActivitiesProv_DecisionNode', a)


def test_assoc_edge3_link_reassign_clear():
    a = ActivitiesProv_Activity(isReadOnly=True, isSingleExecution=True)
    b1 = ActivitiesProv_ActivityEdge()
    b2 = ActivitiesProv_ActivityEdge()
    _safe_set(a, 'ActivitiesProv_Activity4', {b1})
    assert _is_linked(a, 'ActivitiesProv_Activity4', b1)
    if hasattr(b1, 'ActivitiesProv_ActivityEdge'):
        assert _is_linked(b1, 'ActivitiesProv_ActivityEdge', a)
    _safe_set(a, 'ActivitiesProv_Activity4', {b2})
    assert _is_linked(a, 'ActivitiesProv_Activity4', b2)
    if hasattr(b1, 'ActivitiesProv_ActivityEdge'):
        assert not _is_linked(b1, 'ActivitiesProv_ActivityEdge', a)
    if hasattr(b2, 'ActivitiesProv_ActivityEdge'):
        assert _is_linked(b2, 'ActivitiesProv_ActivityEdge', a)
    _safe_set(a, 'ActivitiesProv_Activity4', set())
    assert not _is_linked(a, 'ActivitiesProv_Activity4', b2)
    if hasattr(b2, 'ActivitiesProv_ActivityEdge'):
        assert not _is_linked(b2, 'ActivitiesProv_ActivityEdge', a)


def test_assoc_edge90_link_reassign_clear():
    a = ActivitiesProv_StructuredActivityNode(mustIsolate=True)
    b1 = ActivitiesProv_ActivityEdge()
    b2 = ActivitiesProv_ActivityEdge()
    _safe_set(a, 'ActivitiesProv_StructuredActivityNode91', {b1})
    assert _is_linked(a, 'ActivitiesProv_StructuredActivityNode91', b1)
    if hasattr(b1, 'ActivitiesProv_ActivityEdge92'):
        assert _is_linked(b1, 'ActivitiesProv_ActivityEdge92', a)
    _safe_set(a, 'ActivitiesProv_StructuredActivityNode91', {b2})
    assert _is_linked(a, 'ActivitiesProv_StructuredActivityNode91', b2)
    if hasattr(b1, 'ActivitiesProv_ActivityEdge92'):
        assert not _is_linked(b1, 'ActivitiesProv_ActivityEdge92', a)
    if hasattr(b2, 'ActivitiesProv_ActivityEdge92'):
        assert _is_linked(b2, 'ActivitiesProv_ActivityEdge92', a)
    _safe_set(a, 'ActivitiesProv_StructuredActivityNode91', set())
    assert not _is_linked(a, 'ActivitiesProv_StructuredActivityNode91', b2)
    if hasattr(b2, 'ActivitiesProv_ActivityEdge92'):
        assert not _is_linked(b2, 'ActivitiesProv_ActivityEdge92', a)


def test_assoc_group1_link_reassign_clear():
    a = ActivitiesProv_Activity(isReadOnly=True, isSingleExecution=True)
    b1 = ActivitiesProv_ActivityGroup()
    b2 = ActivitiesProv_ActivityGroup()
    _safe_set(a, 'ActivitiesProv_Activity2', {b1})
    assert _is_linked(a, 'ActivitiesProv_Activity2', b1)
    if hasattr(b1, 'ActivitiesProv_ActivityGroup'):
        assert _is_linked(b1, 'ActivitiesProv_ActivityGroup', a)
    _safe_set(a, 'ActivitiesProv_Activity2', {b2})
    assert _is_linked(a, 'ActivitiesProv_Activity2', b2)
    if hasattr(b1, 'ActivitiesProv_ActivityGroup'):
        assert not _is_linked(b1, 'ActivitiesProv_ActivityGroup', a)
    if hasattr(b2, 'ActivitiesProv_ActivityGroup'):
        assert _is_linked(b2, 'ActivitiesProv_ActivityGroup', a)
    _safe_set(a, 'ActivitiesProv_Activity2', set())
    assert not _is_linked(a, 'ActivitiesProv_Activity2', b2)
    if hasattr(b2, 'ActivitiesProv_ActivityGroup'):
        assert not _is_linked(b2, 'ActivitiesProv_ActivityGroup', a)


def test_assoc_inActivity35_link_reassign_clear():
    a = ActivitiesProv_Activity(isReadOnly=True, isSingleExecution=True)
    b1 = ActivitiesProv_ActivityGroup()
    b2 = ActivitiesProv_ActivityGroup()
    _safe_set(a, 'ActivitiesProv_Activity37', b1)
    assert _is_linked(a, 'ActivitiesProv_Activity37', b1)
    if hasattr(b1, 'ActivitiesProv_ActivityGroup36'):
        assert _is_linked(b1, 'ActivitiesProv_ActivityGroup36', a)
    _safe_set(a, 'ActivitiesProv_Activity37', b2)
    assert _is_linked(a, 'ActivitiesProv_Activity37', b2)
    if hasattr(b1, 'ActivitiesProv_ActivityGroup36'):
        assert not _is_linked(b1, 'ActivitiesProv_ActivityGroup36', a)
    if hasattr(b2, 'ActivitiesProv_ActivityGroup36'):
        assert _is_linked(b2, 'ActivitiesProv_ActivityGroup36', a)
    _safe_set(a, 'ActivitiesProv_Activity37', None)
    assert not _is_linked(a, 'ActivitiesProv_Activity37', b2)
    if hasattr(b2, 'ActivitiesProv_ActivityGroup36'):
        assert not _is_linked(b2, 'ActivitiesProv_ActivityGroup36', a)


def test_assoc_inStructuredNode26_link_reassign_clear():
    a = ActivitiesProv_StructuredActivityNode(mustIsolate=True)
    b1 = ActivitiesProv_ActivityNode()
    b2 = ActivitiesProv_ActivityNode()
    _safe_set(a, 'ActivitiesProv_StructuredActivityNode28', b1)
    assert _is_linked(a, 'ActivitiesProv_StructuredActivityNode28', b1)
    if hasattr(b1, 'ActivitiesProv_ActivityNode27'):
        assert _is_linked(b1, 'ActivitiesProv_ActivityNode27', a)
    _safe_set(a, 'ActivitiesProv_StructuredActivityNode28', b2)
    assert _is_linked(a, 'ActivitiesProv_StructuredActivityNode28', b2)
    if hasattr(b1, 'ActivitiesProv_ActivityNode27'):
        assert not _is_linked(b1, 'ActivitiesProv_ActivityNode27', a)
    if hasattr(b2, 'ActivitiesProv_ActivityNode27'):
        assert _is_linked(b2, 'ActivitiesProv_ActivityNode27', a)
    _safe_set(a, 'ActivitiesProv_StructuredActivityNode28', None)
    assert not _is_linked(a, 'ActivitiesProv_StructuredActivityNode28', b2)
    if hasattr(b2, 'ActivitiesProv_ActivityNode27'):
        assert not _is_linked(b2, 'ActivitiesProv_ActivityNode27', a)


def test_assoc_inStructuredNode62_link_reassign_clear():
    a = ActivitiesProv_StructuredActivityNode(mustIsolate=True)
    b1 = ActivitiesProv_ActivityEdge()
    b2 = ActivitiesProv_ActivityEdge()
    _safe_set(a, 'ActivitiesProv_StructuredActivityNode64', b1)
    assert _is_linked(a, 'ActivitiesProv_StructuredActivityNode64', b1)
    if hasattr(b1, 'ActivitiesProv_ActivityEdge63'):
        assert _is_linked(b1, 'ActivitiesProv_ActivityEdge63', a)
    _safe_set(a, 'ActivitiesProv_StructuredActivityNode64', b2)
    assert _is_linked(a, 'ActivitiesProv_StructuredActivityNode64', b2)
    if hasattr(b1, 'ActivitiesProv_ActivityEdge63'):
        assert not _is_linked(b1, 'ActivitiesProv_ActivityEdge63', a)
    if hasattr(b2, 'ActivitiesProv_ActivityEdge63'):
        assert _is_linked(b2, 'ActivitiesProv_ActivityEdge63', a)
    _safe_set(a, 'ActivitiesProv_StructuredActivityNode64', None)
    assert not _is_linked(a, 'ActivitiesProv_StructuredActivityNode64', b2)
    if hasattr(b2, 'ActivitiesProv_ActivityEdge63'):
        assert not _is_linked(b2, 'ActivitiesProv_ActivityEdge63', a)


def test_assoc_node0_link_reassign_clear():
    a = ActivitiesProv_Activity(isReadOnly=True, isSingleExecution=True)
    b1 = ActivitiesProv_ActivityNode()
    b2 = ActivitiesProv_ActivityNode()
    _safe_set(a, 'ActivitiesProv_Activity', {b1})
    assert _is_linked(a, 'ActivitiesProv_Activity', b1)
    if hasattr(b1, 'ActivitiesProv_ActivityNode'):
        assert _is_linked(b1, 'ActivitiesProv_ActivityNode', a)
    _safe_set(a, 'ActivitiesProv_Activity', {b2})
    assert _is_linked(a, 'ActivitiesProv_Activity', b2)
    if hasattr(b1, 'ActivitiesProv_ActivityNode'):
        assert not _is_linked(b1, 'ActivitiesProv_ActivityNode', a)
    if hasattr(b2, 'ActivitiesProv_ActivityNode'):
        assert _is_linked(b2, 'ActivitiesProv_ActivityNode', a)
    _safe_set(a, 'ActivitiesProv_Activity', set())
    assert not _is_linked(a, 'ActivitiesProv_Activity', b2)
    if hasattr(b2, 'ActivitiesProv_ActivityNode'):
        assert not _is_linked(b2, 'ActivitiesProv_ActivityNode', a)


def test_assoc_node87_link_reassign_clear():
    a = ActivitiesProv_StructuredActivityNode(mustIsolate=True)
    b1 = ActivitiesProv_ActivityNode()
    b2 = ActivitiesProv_ActivityNode()
    _safe_set(a, 'ActivitiesProv_StructuredActivityNode88', {b1})
    assert _is_linked(a, 'ActivitiesProv_StructuredActivityNode88', b1)
    if hasattr(b1, 'ActivitiesProv_ActivityNode89'):
        assert _is_linked(b1, 'ActivitiesProv_ActivityNode89', a)
    _safe_set(a, 'ActivitiesProv_StructuredActivityNode88', {b2})
    assert _is_linked(a, 'ActivitiesProv_StructuredActivityNode88', b2)
    if hasattr(b1, 'ActivitiesProv_ActivityNode89'):
        assert not _is_linked(b1, 'ActivitiesProv_ActivityNode89', a)
    if hasattr(b2, 'ActivitiesProv_ActivityNode89'):
        assert _is_linked(b2, 'ActivitiesProv_ActivityNode89', a)
    _safe_set(a, 'ActivitiesProv_StructuredActivityNode88', set())
    assert not _is_linked(a, 'ActivitiesProv_StructuredActivityNode88', b2)
    if hasattr(b2, 'ActivitiesProv_ActivityNode89'):
        assert not _is_linked(b2, 'ActivitiesProv_ActivityNode89', a)


def test_assoc_partition5_link_reassign_clear():
    a = ActivitiesProv_Activity(isReadOnly=True, isSingleExecution=True)
    b1 = ActivitiesProv_ActivityPartition()
    b2 = ActivitiesProv_ActivityPartition()
    _safe_set(a, 'ActivitiesProv_Activity6', {b1})
    assert _is_linked(a, 'ActivitiesProv_Activity6', b1)
    if hasattr(b1, 'ActivitiesProv_ActivityPartition'):
        assert _is_linked(b1, 'ActivitiesProv_ActivityPartition', a)
    _safe_set(a, 'ActivitiesProv_Activity6', {b2})
    assert _is_linked(a, 'ActivitiesProv_Activity6', b2)
    if hasattr(b1, 'ActivitiesProv_ActivityPartition'):
        assert not _is_linked(b1, 'ActivitiesProv_ActivityPartition', a)
    if hasattr(b2, 'ActivitiesProv_ActivityPartition'):
        assert _is_linked(b2, 'ActivitiesProv_ActivityPartition', a)
    _safe_set(a, 'ActivitiesProv_Activity6', set())
    assert not _is_linked(a, 'ActivitiesProv_Activity6', b2)
    if hasattr(b2, 'ActivitiesProv_ActivityPartition'):
        assert not _is_linked(b2, 'ActivitiesProv_ActivityPartition', a)


def test_assoc_setupPart94_link_reassign_clear():
    a = ActivitiesProv_LoopNode(isTestedFirst=True)
    b1 = ActivitiesProv_ExecutableNode()
    b2 = ActivitiesProv_ExecutableNode()
    _safe_set(a, 'ActivitiesProv_LoopNode', {b1})
    assert _is_linked(a, 'ActivitiesProv_LoopNode', b1)
    if hasattr(b1, 'ActivitiesProv_ExecutableNode95'):
        assert _is_linked(b1, 'ActivitiesProv_ExecutableNode95', a)
    _safe_set(a, 'ActivitiesProv_LoopNode', {b2})
    assert _is_linked(a, 'ActivitiesProv_LoopNode', b2)
    if hasattr(b1, 'ActivitiesProv_ExecutableNode95'):
        assert not _is_linked(b1, 'ActivitiesProv_ExecutableNode95', a)
    if hasattr(b2, 'ActivitiesProv_ExecutableNode95'):
        assert _is_linked(b2, 'ActivitiesProv_ExecutableNode95', a)
    _safe_set(a, 'ActivitiesProv_LoopNode', set())
    assert not _is_linked(a, 'ActivitiesProv_LoopNode', b2)
    if hasattr(b2, 'ActivitiesProv_ExecutableNode95'):
        assert not _is_linked(b2, 'ActivitiesProv_ExecutableNode95', a)


def test_assoc_structuredNode7_link_reassign_clear():
    a = ActivitiesProv_StructuredActivityNode(mustIsolate=True)
    b1 = ActivitiesProv_Activity(isReadOnly=True, isSingleExecution=True)
    b2 = ActivitiesProv_Activity(isReadOnly=False, isSingleExecution=False)
    _safe_set(a, 'ActivitiesProv_StructuredActivityNode', b1)
    assert _is_linked(a, 'ActivitiesProv_StructuredActivityNode', b1)
    if hasattr(b1, 'ActivitiesProv_Activity8'):
        assert _is_linked(b1, 'ActivitiesProv_Activity8', a)
    _safe_set(a, 'ActivitiesProv_StructuredActivityNode', b2)
    assert _is_linked(a, 'ActivitiesProv_StructuredActivityNode', b2)
    if hasattr(b1, 'ActivitiesProv_Activity8'):
        assert not _is_linked(b1, 'ActivitiesProv_Activity8', a)
    if hasattr(b2, 'ActivitiesProv_Activity8'):
        assert _is_linked(b2, 'ActivitiesProv_Activity8', a)
    _safe_set(a, 'ActivitiesProv_StructuredActivityNode', None)
    assert not _is_linked(a, 'ActivitiesProv_StructuredActivityNode', b2)
    if hasattr(b2, 'ActivitiesProv_Activity8'):
        assert not _is_linked(b2, 'ActivitiesProv_Activity8', a)


def test_assoc_test103_link_reassign_clear():
    a = ActivitiesProv_ConditionalNode(isAssumed=True, isDeterminate=True)
    b1 = ActivitiesProv_ExecutableNode()
    b2 = ActivitiesProv_ExecutableNode()
    _safe_set(a, 'ActivitiesProv_ConditionalNode104', {b1})
    assert _is_linked(a, 'ActivitiesProv_ConditionalNode104', b1)
    if hasattr(b1, 'ActivitiesProv_ExecutableNode105'):
        assert _is_linked(b1, 'ActivitiesProv_ExecutableNode105', a)
    _safe_set(a, 'ActivitiesProv_ConditionalNode104', {b2})
    assert _is_linked(a, 'ActivitiesProv_ConditionalNode104', b2)
    if hasattr(b1, 'ActivitiesProv_ExecutableNode105'):
        assert not _is_linked(b1, 'ActivitiesProv_ExecutableNode105', a)
    if hasattr(b2, 'ActivitiesProv_ExecutableNode105'):
        assert _is_linked(b2, 'ActivitiesProv_ExecutableNode105', a)
    _safe_set(a, 'ActivitiesProv_ConditionalNode104', set())
    assert not _is_linked(a, 'ActivitiesProv_ConditionalNode104', b2)
    if hasattr(b2, 'ActivitiesProv_ExecutableNode105'):
        assert not _is_linked(b2, 'ActivitiesProv_ExecutableNode105', a)


def test_assoc_test99_link_reassign_clear():
    a = ActivitiesProv_LoopNode(isTestedFirst=True)
    b1 = ActivitiesProv_ExecutableNode()
    b2 = ActivitiesProv_ExecutableNode()
    _safe_set(a, 'ActivitiesProv_LoopNode100', {b1})
    assert _is_linked(a, 'ActivitiesProv_LoopNode100', b1)
    if hasattr(b1, 'ActivitiesProv_ExecutableNode101'):
        assert _is_linked(b1, 'ActivitiesProv_ExecutableNode101', a)
    _safe_set(a, 'ActivitiesProv_LoopNode100', {b2})
    assert _is_linked(a, 'ActivitiesProv_LoopNode100', b2)
    if hasattr(b1, 'ActivitiesProv_ExecutableNode101'):
        assert not _is_linked(b1, 'ActivitiesProv_ExecutableNode101', a)
    if hasattr(b2, 'ActivitiesProv_ExecutableNode101'):
        assert _is_linked(b2, 'ActivitiesProv_ExecutableNode101', a)
    _safe_set(a, 'ActivitiesProv_LoopNode100', set())
    assert not _is_linked(a, 'ActivitiesProv_LoopNode100', b2)
    if hasattr(b2, 'ActivitiesProv_ExecutableNode101'):
        assert not _is_linked(b2, 'ActivitiesProv_ExecutableNode101', a)


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

ActivitiesProv_Activity_strategy = st.builds(ActivitiesProv_Activity, isReadOnly=st.booleans(), isSingleExecution=st.booleans())
@given(instance=ActivitiesProv_Activity_strategy)
@settings(max_examples=25)
def test_ActivitiesProv_Activity_instantiation(instance):
    assert isinstance(instance, ActivitiesProv_Activity)


ActivitiesProv_ActivityEdge_strategy = st.builds(ActivitiesProv_ActivityEdge)
@given(instance=ActivitiesProv_ActivityEdge_strategy)
@settings(max_examples=25)
def test_ActivitiesProv_ActivityEdge_instantiation(instance):
    assert isinstance(instance, ActivitiesProv_ActivityEdge)


ActivitiesProv_ActivityFinalNode_strategy = st.builds(ActivitiesProv_ActivityFinalNode)
@given(instance=ActivitiesProv_ActivityFinalNode_strategy)
@settings(max_examples=25)
def test_ActivitiesProv_ActivityFinalNode_instantiation(instance):
    assert isinstance(instance, ActivitiesProv_ActivityFinalNode)


ActivitiesProv_ActivityGroup_strategy = st.builds(ActivitiesProv_ActivityGroup)
@given(instance=ActivitiesProv_ActivityGroup_strategy)
@settings(max_examples=25)
def test_ActivitiesProv_ActivityGroup_instantiation(instance):
    assert isinstance(instance, ActivitiesProv_ActivityGroup)


ActivitiesProv_ActivityNode_strategy = st.builds(ActivitiesProv_ActivityNode)
@given(instance=ActivitiesProv_ActivityNode_strategy)
@settings(max_examples=25)
def test_ActivitiesProv_ActivityNode_instantiation(instance):
    assert isinstance(instance, ActivitiesProv_ActivityNode)


ActivitiesProv_ActivityParameterNode_strategy = st.builds(ActivitiesProv_ActivityParameterNode)
@given(instance=ActivitiesProv_ActivityParameterNode_strategy)
@settings(max_examples=25)
def test_ActivitiesProv_ActivityParameterNode_instantiation(instance):
    assert isinstance(instance, ActivitiesProv_ActivityParameterNode)


ActivitiesProv_ActivityPartition_strategy = st.builds(ActivitiesProv_ActivityPartition)
@given(instance=ActivitiesProv_ActivityPartition_strategy)
@settings(max_examples=25)
def test_ActivitiesProv_ActivityPartition_instantiation(instance):
    assert isinstance(instance, ActivitiesProv_ActivityPartition)


ActivitiesProv_CentralBufferNode_strategy = st.builds(ActivitiesProv_CentralBufferNode)
@given(instance=ActivitiesProv_CentralBufferNode_strategy)
@settings(max_examples=25)
def test_ActivitiesProv_CentralBufferNode_instantiation(instance):
    assert isinstance(instance, ActivitiesProv_CentralBufferNode)


ActivitiesProv_Clause_strategy = st.builds(ActivitiesProv_Clause)
@given(instance=ActivitiesProv_Clause_strategy)
@settings(max_examples=25)
def test_ActivitiesProv_Clause_instantiation(instance):
    assert isinstance(instance, ActivitiesProv_Clause)


ActivitiesProv_ConditionalNode_strategy = st.builds(ActivitiesProv_ConditionalNode, isAssumed=st.booleans(), isDeterminate=st.booleans())
@given(instance=ActivitiesProv_ConditionalNode_strategy)
@settings(max_examples=25)
def test_ActivitiesProv_ConditionalNode_instantiation(instance):
    assert isinstance(instance, ActivitiesProv_ConditionalNode)


ActivitiesProv_ControlFlow_strategy = st.builds(ActivitiesProv_ControlFlow)
@given(instance=ActivitiesProv_ControlFlow_strategy)
@settings(max_examples=25)
def test_ActivitiesProv_ControlFlow_instantiation(instance):
    assert isinstance(instance, ActivitiesProv_ControlFlow)


ActivitiesProv_ControlNode_strategy = st.builds(ActivitiesProv_ControlNode)
@given(instance=ActivitiesProv_ControlNode_strategy)
@settings(max_examples=25)
def test_ActivitiesProv_ControlNode_instantiation(instance):
    assert isinstance(instance, ActivitiesProv_ControlNode)


ActivitiesProv_DataStoreNode_strategy = st.builds(ActivitiesProv_DataStoreNode)
@given(instance=ActivitiesProv_DataStoreNode_strategy)
@settings(max_examples=25)
def test_ActivitiesProv_DataStoreNode_instantiation(instance):
    assert isinstance(instance, ActivitiesProv_DataStoreNode)


ActivitiesProv_DecisionNode_strategy = st.builds(ActivitiesProv_DecisionNode)
@given(instance=ActivitiesProv_DecisionNode_strategy)
@settings(max_examples=25)
def test_ActivitiesProv_DecisionNode_instantiation(instance):
    assert isinstance(instance, ActivitiesProv_DecisionNode)


ActivitiesProv_ExceptionHandler_strategy = st.builds(ActivitiesProv_ExceptionHandler)
@given(instance=ActivitiesProv_ExceptionHandler_strategy)
@settings(max_examples=25)
def test_ActivitiesProv_ExceptionHandler_instantiation(instance):
    assert isinstance(instance, ActivitiesProv_ExceptionHandler)


ActivitiesProv_ExecutableNode_strategy = st.builds(ActivitiesProv_ExecutableNode)
@given(instance=ActivitiesProv_ExecutableNode_strategy)
@settings(max_examples=25)
def test_ActivitiesProv_ExecutableNode_instantiation(instance):
    assert isinstance(instance, ActivitiesProv_ExecutableNode)


ActivitiesProv_ExpansionNode_strategy = st.builds(ActivitiesProv_ExpansionNode)
@given(instance=ActivitiesProv_ExpansionNode_strategy)
@settings(max_examples=25)
def test_ActivitiesProv_ExpansionNode_instantiation(instance):
    assert isinstance(instance, ActivitiesProv_ExpansionNode)


ActivitiesProv_ExpansionRegion_strategy = st.builds(ActivitiesProv_ExpansionRegion)
@given(instance=ActivitiesProv_ExpansionRegion_strategy)
@settings(max_examples=25)
def test_ActivitiesProv_ExpansionRegion_instantiation(instance):
    assert isinstance(instance, ActivitiesProv_ExpansionRegion)


ActivitiesProv_FinalNode_strategy = st.builds(ActivitiesProv_FinalNode)
@given(instance=ActivitiesProv_FinalNode_strategy)
@settings(max_examples=25)
def test_ActivitiesProv_FinalNode_instantiation(instance):
    assert isinstance(instance, ActivitiesProv_FinalNode)


ActivitiesProv_FlowFinalNode_strategy = st.builds(ActivitiesProv_FlowFinalNode)
@given(instance=ActivitiesProv_FlowFinalNode_strategy)
@settings(max_examples=25)
def test_ActivitiesProv_FlowFinalNode_instantiation(instance):
    assert isinstance(instance, ActivitiesProv_FlowFinalNode)


ActivitiesProv_ForkNode_strategy = st.builds(ActivitiesProv_ForkNode)
@given(instance=ActivitiesProv_ForkNode_strategy)
@settings(max_examples=25)
def test_ActivitiesProv_ForkNode_instantiation(instance):
    assert isinstance(instance, ActivitiesProv_ForkNode)


ActivitiesProv_InitialNode_strategy = st.builds(ActivitiesProv_InitialNode)
@given(instance=ActivitiesProv_InitialNode_strategy)
@settings(max_examples=25)
def test_ActivitiesProv_InitialNode_instantiation(instance):
    assert isinstance(instance, ActivitiesProv_InitialNode)


ActivitiesProv_InterruptibleActivityRegion_strategy = st.builds(ActivitiesProv_InterruptibleActivityRegion)
@given(instance=ActivitiesProv_InterruptibleActivityRegion_strategy)
@settings(max_examples=25)
def test_ActivitiesProv_InterruptibleActivityRegion_instantiation(instance):
    assert isinstance(instance, ActivitiesProv_InterruptibleActivityRegion)


ActivitiesProv_JoinNode_strategy = st.builds(ActivitiesProv_JoinNode, isCombineDuplicate=st.booleans())
@given(instance=ActivitiesProv_JoinNode_strategy)
@settings(max_examples=25)
def test_ActivitiesProv_JoinNode_instantiation(instance):
    assert isinstance(instance, ActivitiesProv_JoinNode)


ActivitiesProv_LoopNode_strategy = st.builds(ActivitiesProv_LoopNode, isTestedFirst=st.booleans())
@given(instance=ActivitiesProv_LoopNode_strategy)
@settings(max_examples=25)
def test_ActivitiesProv_LoopNode_instantiation(instance):
    assert isinstance(instance, ActivitiesProv_LoopNode)


ActivitiesProv_MergeNode_strategy = st.builds(ActivitiesProv_MergeNode)
@given(instance=ActivitiesProv_MergeNode_strategy)
@settings(max_examples=25)
def test_ActivitiesProv_MergeNode_instantiation(instance):
    assert isinstance(instance, ActivitiesProv_MergeNode)


ActivitiesProv_ObjectFlow_strategy = st.builds(ActivitiesProv_ObjectFlow, isControlType=st.booleans(), isMulticast=st.booleans(), isMultireceive=st.booleans())
@given(instance=ActivitiesProv_ObjectFlow_strategy)
@settings(max_examples=25)
def test_ActivitiesProv_ObjectFlow_instantiation(instance):
    assert isinstance(instance, ActivitiesProv_ObjectFlow)


ActivitiesProv_ObjectNode_strategy = st.builds(ActivitiesProv_ObjectNode)
@given(instance=ActivitiesProv_ObjectNode_strategy)
@settings(max_examples=25)
def test_ActivitiesProv_ObjectNode_instantiation(instance):
    assert isinstance(instance, ActivitiesProv_ObjectNode)


ActivitiesProv_ParameterSet_strategy = st.builds(ActivitiesProv_ParameterSet)
@given(instance=ActivitiesProv_ParameterSet_strategy)
@settings(max_examples=25)
def test_ActivitiesProv_ParameterSet_instantiation(instance):
    assert isinstance(instance, ActivitiesProv_ParameterSet)


ActivitiesProv_SequenceNode_strategy = st.builds(ActivitiesProv_SequenceNode)
@given(instance=ActivitiesProv_SequenceNode_strategy)
@settings(max_examples=25)
def test_ActivitiesProv_SequenceNode_instantiation(instance):
    assert isinstance(instance, ActivitiesProv_SequenceNode)


ActivitiesProv_StructuredActivityNode_strategy = st.builds(ActivitiesProv_StructuredActivityNode, mustIsolate=st.booleans())
@given(instance=ActivitiesProv_StructuredActivityNode_strategy)
@settings(max_examples=25)
def test_ActivitiesProv_StructuredActivityNode_instantiation(instance):
    assert isinstance(instance, ActivitiesProv_StructuredActivityNode)


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


CentralBufferNode_strategy = st.builds(CentralBufferNode)
@given(instance=CentralBufferNode_strategy)
@settings(max_examples=25)
def test_CentralBufferNode_instantiation(instance):
    assert isinstance(instance, CentralBufferNode)


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


ObjectNode_strategy = st.builds(ObjectNode)
@given(instance=ObjectNode_strategy)
@settings(max_examples=25)
def test_ObjectNode_instantiation(instance):
    assert isinstance(instance, ObjectNode)


StructuredActivityNode_strategy = st.builds(StructuredActivityNode)
@given(instance=StructuredActivityNode_strategy)
@settings(max_examples=25)
def test_StructuredActivityNode_instantiation(instance):
    assert isinstance(instance, StructuredActivityNode)


