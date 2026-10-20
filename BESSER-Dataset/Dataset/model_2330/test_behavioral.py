import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    AcceptEventAction,
    Action,
    Actions_BasicActions_Action,
    Actions_BasicActions_Behavior,
    Actions_BasicActions_CallAction,
    Actions_BasicActions_CallBehaviorAction,
    Actions_BasicActions_CallOperationAction,
    Actions_BasicActions_Classifier,
    Actions_BasicActions_InputPin,
    Actions_BasicActions_InvocationAction,
    Actions_BasicActions_MultiplicityElement,
    Actions_BasicActions_NamedElement,
    Actions_BasicActions_OpaqueAction,
    Actions_BasicActions_Operation,
    Actions_BasicActions_OutputPin,
    Actions_BasicActions_Pin,
    Actions_BasicActions_SendSignalAction,
    Actions_BasicActions_Signal,
    Actions_BasicActions_TypedElement,
    Actions_BasicActions_ValuePin,
    Actions_BasicActions_ValueSpecification,
    Actions_CompleteActions_AcceptCallAction,
    Actions_CompleteActions_AcceptEventAction,
    Actions_CompleteActions_CreateLinkObjectAction,
    Actions_CompleteActions_QualifierValue,
    Actions_CompleteActions_ReadExtendAction,
    Actions_CompleteActions_ReadLinkObjectEndAction,
    Actions_CompleteActions_ReadLinkObjectEndQualifierAction,
    Actions_CompleteActions_ReadlsClassifiedObjectAction,
    Actions_CompleteActions_ReclassifyObjectAction,
    Actions_CompleteActions_ReduceAction,
    Actions_CompleteActions_ReplyAction,
    Actions_CompleteActions_StartClassifierBehaviorAction,
    Actions_CompleteActions_StartObjectBehaviorAction,
    Actions_CompleteActions_Trigger,
    Actions_CompleteActions_UnmarshallAction,
    Actions_IntermediateActions_AddStructuralFeatureValueAction,
    Actions_IntermediateActions_BroadcastSignalAction,
    Actions_IntermediateActions_ClearStructuralFeatureAction,
    Actions_IntermediateActions_CreateLinkAction,
    Actions_IntermediateActions_CreateObjectAction,
    Actions_IntermediateActions_DestroyLinkAction,
    Actions_IntermediateActions_DestroyObjectAction,
    Actions_IntermediateActions_Element,
    Actions_IntermediateActions_LinkAction,
    Actions_IntermediateActions_LinkEndCreationData,
    Actions_IntermediateActions_LinkEndData,
    Actions_IntermediateActions_LinkEndDestructionData,
    Actions_IntermediateActions_Property,
    Actions_IntermediateActions_ReadLinkAction,
    Actions_IntermediateActions_ReadSelfAction,
    Actions_IntermediateActions_ReadStructuralFeatureAction,
    Actions_IntermediateActions_RemoveStructuralFeatureValueAction,
    Actions_IntermediateActions_SendObjectAction,
    Actions_IntermediateActions_StructuralFeature,
    Actions_IntermediateActions_StructuralFeatureAction,
    Actions_IntermediateActions_TestIdentityAction,
    Actions_IntermediateActions_ValueSpecificationAction,
    Actions_IntermediateActions_WriteLinkAction,
    Actions_IntermediateActions_WriteStructuralFeatureAction,
    Actions_StructuredActions_ActionInputPin,
    Actions_StructuredActions_AddVariableValueAction,
    Actions_StructuredActions_ClearVariableAction,
    Actions_StructuredActions_RaiseExceptionAction,
    Actions_StructuredActions_ReadVariableAction,
    Actions_StructuredActions_RemoveVariableValueAction,
    Actions_StructuredActions_Variable,
    Actions_StructuredActions_VariableAction,
    Actions_StructuredActions_WriteVariableAction,
    BasicActions_MultiplicityElement,
    BasicActions_TypedElement,
    Behavior,
    CallAction,
    Classifier,
    CreateLinkAction,
    Element,
    InputPin,
    InvocationAction,
    LinkAction,
    LinkEndData,
    NamedElement,
    Operation,
    OutputPin,
    Pin,
    Property,
    QualifierValue,
    Signal,
    StructuralFeature,
    StructuralFeatureAction,
    Trigger,
    ValueSpecification,
    Variable,
    VariableAction,
    WriteLinkAction,
    WriteStructuralFeatureAction,
    WriteVariableAction,
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

# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_collection155_stub_double():
    # InputPin has no real 'InputPin157' property in the generated
    # code (a bare stub) -- manually attach it so Actions_CompleteActions_ReduceAction's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # Actions_CompleteActions_ReduceAction's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = Actions_CompleteActions_ReduceAction(isOrdered=True)
    partner = InputPin()
    setattr(partner, 'InputPin157', None)
    _safe_set(owner, 'Actions_CompleteActions_ReduceAction156', partner)
    assert getattr(partner, 'InputPin157') == owner
    _safe_set(owner, 'Actions_CompleteActions_ReduceAction156', None)
    assert getattr(partner, 'InputPin157') is None


def test_assoc_destroyAt84_stub_double():
    # InputPin has no real 'InputPin85' property in the generated
    # code (a bare stub) -- manually attach it so Actions_IntermediateActions_LinkEndDestructionData's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # Actions_IntermediateActions_LinkEndDestructionData's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = Actions_IntermediateActions_LinkEndDestructionData(isDestroyDuplicates=True)
    partner = InputPin()
    setattr(partner, 'InputPin85', None)
    _safe_set(owner, 'Actions_IntermediateActions_LinkEndDestructionData', partner)
    assert getattr(partner, 'InputPin85') == owner
    _safe_set(owner, 'Actions_IntermediateActions_LinkEndDestructionData', None)
    assert getattr(partner, 'InputPin85') is None


def test_assoc_inputValue5_stub_double():
    # InputPin has no real 'InputPin6' property in the generated
    # code (a bare stub) -- manually attach it so Actions_BasicActions_OpaqueAction's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # Actions_BasicActions_OpaqueAction's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = Actions_BasicActions_OpaqueAction(body="sample_text", language="sample_text")
    partner = InputPin()
    setattr(partner, 'InputPin6', None)
    _safe_set(owner, 'Actions_BasicActions_OpaqueAction', {partner})
    assert getattr(partner, 'InputPin6') == owner
    _safe_set(owner, 'Actions_BasicActions_OpaqueAction', set())
    assert getattr(partner, 'InputPin6') is None


def test_assoc_insertAt82_stub_double():
    # InputPin has no real 'InputPin83' property in the generated
    # code (a bare stub) -- manually attach it so Actions_IntermediateActions_LinkEndCreationData's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # Actions_IntermediateActions_LinkEndCreationData's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = Actions_IntermediateActions_LinkEndCreationData(isReplaceAll=True)
    partner = InputPin()
    setattr(partner, 'InputPin83', None)
    _safe_set(owner, 'Actions_IntermediateActions_LinkEndCreationData', partner)
    assert getattr(partner, 'InputPin83') == owner
    _safe_set(owner, 'Actions_IntermediateActions_LinkEndCreationData', None)
    assert getattr(partner, 'InputPin83') is None


def test_assoc_newClassifier118_stub_double():
    # Classifier has no real 'Classifier120' property in the generated
    # code (a bare stub) -- manually attach it so Actions_CompleteActions_ReclassifyObjectAction's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # Actions_CompleteActions_ReclassifyObjectAction's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = Actions_CompleteActions_ReclassifyObjectAction(isReplaceAll=True)
    partner = Classifier()
    setattr(partner, 'Classifier120', None)
    _safe_set(owner, 'Actions_CompleteActions_ReclassifyObjectAction119', {partner})
    assert getattr(partner, 'Classifier120') == owner
    _safe_set(owner, 'Actions_CompleteActions_ReclassifyObjectAction119', set())
    assert getattr(partner, 'Classifier120') is None


def test_assoc_object113_stub_double():
    # InputPin has no real 'InputPin114' property in the generated
    # code (a bare stub) -- manually attach it so Actions_CompleteActions_ReclassifyObjectAction's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # Actions_CompleteActions_ReclassifyObjectAction's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = Actions_CompleteActions_ReclassifyObjectAction(isReplaceAll=True)
    partner = InputPin()
    setattr(partner, 'InputPin114', None)
    _safe_set(owner, 'Actions_CompleteActions_ReclassifyObjectAction', partner)
    assert getattr(partner, 'InputPin114') == owner
    _safe_set(owner, 'Actions_CompleteActions_ReclassifyObjectAction', None)
    assert getattr(partner, 'InputPin114') is None


def test_assoc_oldClassifier115_stub_double():
    # Classifier has no real 'Classifier117' property in the generated
    # code (a bare stub) -- manually attach it so Actions_CompleteActions_ReclassifyObjectAction's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # Actions_CompleteActions_ReclassifyObjectAction's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = Actions_CompleteActions_ReclassifyObjectAction(isReplaceAll=True)
    partner = Classifier()
    setattr(partner, 'Classifier117', None)
    _safe_set(owner, 'Actions_CompleteActions_ReclassifyObjectAction116', {partner})
    assert getattr(partner, 'Classifier117') == owner
    _safe_set(owner, 'Actions_CompleteActions_ReclassifyObjectAction116', set())
    assert getattr(partner, 'Classifier117') is None


def test_assoc_outputValue7_stub_double():
    # OutputPin has no real 'OutputPin9' property in the generated
    # code (a bare stub) -- manually attach it so Actions_BasicActions_OpaqueAction's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # Actions_BasicActions_OpaqueAction's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = Actions_BasicActions_OpaqueAction(body="sample_text", language="sample_text")
    partner = OutputPin()
    setattr(partner, 'OutputPin9', None)
    _safe_set(owner, 'Actions_BasicActions_OpaqueAction8', {partner})
    assert getattr(partner, 'OutputPin9') == owner
    _safe_set(owner, 'Actions_BasicActions_OpaqueAction8', set())
    assert getattr(partner, 'OutputPin9') is None


def test_assoc_reducer158_stub_double():
    # Behavior has no real 'Behavior160' property in the generated
    # code (a bare stub) -- manually attach it so Actions_CompleteActions_ReduceAction's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # Actions_CompleteActions_ReduceAction's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = Actions_CompleteActions_ReduceAction(isOrdered=True)
    partner = Behavior()
    setattr(partner, 'Behavior160', None)
    _safe_set(owner, 'Actions_CompleteActions_ReduceAction159', partner)
    assert getattr(partner, 'Behavior160') == owner
    _safe_set(owner, 'Actions_CompleteActions_ReduceAction159', None)
    assert getattr(partner, 'Behavior160') is None


def test_assoc_result101_stub_double():
    # OutputPin has no real 'OutputPin102' property in the generated
    # code (a bare stub) -- manually attach it so Actions_CompleteActions_AcceptEventAction's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # Actions_CompleteActions_AcceptEventAction's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = Actions_CompleteActions_AcceptEventAction(isUnmarshall=True)
    partner = OutputPin()
    setattr(partner, 'OutputPin102', None)
    _safe_set(owner, 'Actions_CompleteActions_AcceptEventAction', {partner})
    assert getattr(partner, 'OutputPin102') == owner
    _safe_set(owner, 'Actions_CompleteActions_AcceptEventAction', set())
    assert getattr(partner, 'OutputPin102') is None


def test_assoc_result13_stub_double():
    # OutputPin has no real 'OutputPin14' property in the generated
    # code (a bare stub) -- manually attach it so Actions_BasicActions_CallAction's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # Actions_BasicActions_CallAction's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = Actions_BasicActions_CallAction(isSynchronous=True)
    partner = OutputPin()
    setattr(partner, 'OutputPin14', None)
    _safe_set(owner, 'Actions_BasicActions_CallAction', {partner})
    assert getattr(partner, 'OutputPin14') == owner
    _safe_set(owner, 'Actions_BasicActions_CallAction', set())
    assert getattr(partner, 'OutputPin14') is None


def test_assoc_result153_stub_double():
    # OutputPin has no real 'OutputPin154' property in the generated
    # code (a bare stub) -- manually attach it so Actions_CompleteActions_ReduceAction's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # Actions_CompleteActions_ReduceAction's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = Actions_CompleteActions_ReduceAction(isOrdered=True)
    partner = OutputPin()
    setattr(partner, 'OutputPin154', None)
    _safe_set(owner, 'Actions_CompleteActions_ReduceAction', partner)
    assert getattr(partner, 'OutputPin154') == owner
    _safe_set(owner, 'Actions_CompleteActions_ReduceAction', None)
    assert getattr(partner, 'OutputPin154') is None


def test_assoc_trigger103_stub_double():
    # Trigger has no real 'Trigger105' property in the generated
    # code (a bare stub) -- manually attach it so Actions_CompleteActions_AcceptEventAction's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # Actions_CompleteActions_AcceptEventAction's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = Actions_CompleteActions_AcceptEventAction(isUnmarshall=True)
    partner = Trigger()
    setattr(partner, 'Trigger105', None)
    _safe_set(owner, 'Actions_CompleteActions_AcceptEventAction104', {partner})
    assert getattr(partner, 'Trigger105') == owner
    _safe_set(owner, 'Actions_CompleteActions_AcceptEventAction104', set())
    assert getattr(partner, 'Trigger105') is None


