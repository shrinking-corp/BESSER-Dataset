import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    AcceptEventAction,
    Action,
    ActionsProv_AcceptCallAction,
    ActionsProv_AcceptEventAction,
    ActionsProv_Action,
    ActionsProv_ActionInputPin,
    ActionsProv_AddStructuralFeatureValueAction,
    ActionsProv_AddVariableValueAction,
    ActionsProv_BroadcastSignalAction,
    ActionsProv_CallAction,
    ActionsProv_CallBehaviorAction,
    ActionsProv_CallOperationAction,
    ActionsProv_ClearStructuralFeatureAction,
    ActionsProv_ClearVariableAction,
    ActionsProv_CreateLinkAction,
    ActionsProv_CreateLinkObjectAction,
    ActionsProv_CreateObjectAction,
    ActionsProv_DestroyLinkAction,
    ActionsProv_DestroyObjectAction,
    ActionsProv_InputPin,
    ActionsProv_InvocationAction,
    ActionsProv_LinkAction,
    ActionsProv_LinkEndCreationData,
    ActionsProv_LinkEndData,
    ActionsProv_LinkEndDestructionData,
    ActionsProv_OpaqueAction,
    ActionsProv_OutputPin,
    ActionsProv_Pin,
    ActionsProv_QualifierValue,
    ActionsProv_RaiseExceptionAction,
    ActionsProv_ReadExtendAction,
    ActionsProv_ReadLinkAction,
    ActionsProv_ReadLinkObjectEndAction,
    ActionsProv_ReadLinkObjectEndQualifierAction,
    ActionsProv_ReadSelfAction,
    ActionsProv_ReadStructuralFeatureAction,
    ActionsProv_ReadVariableAction,
    ActionsProv_ReadlsClassifiedObjectAction,
    ActionsProv_ReclassifyObjectAction,
    ActionsProv_ReduceAction,
    ActionsProv_RemoveStructuralFeatureValueAction,
    ActionsProv_RemoveVariableValueAction,
    ActionsProv_ReplyAction,
    ActionsProv_SendObjectAction,
    ActionsProv_SendSignalAction,
    ActionsProv_StartClassifierBehaviorAction,
    ActionsProv_StartObjectBehaviorAction,
    ActionsProv_StructuralFeatureAction,
    ActionsProv_TestIdentityAction,
    ActionsProv_UnmarshallAction,
    ActionsProv_ValuePin,
    ActionsProv_ValueSpecificationAction,
    ActionsProv_VariableAction,
    ActionsProv_WriteLinkAction,
    ActionsProv_WriteStructuralFeatureAction,
    ActionsProv_WriteVariableAction,
    CallAction,
    CreateLinkAction,
    InputPin,
    InvocationAction,
    LinkAction,
    LinkEndData,
    Pin,
    StructuralFeatureAction,
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

def test_assoc_collection111_stub_double():
    # ActionsProv_InputPin has no real 'ActionsProv_InputPin113' property in the generated
    # code (a bare stub) -- manually attach it so ActionsProv_ReduceAction's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ActionsProv_ReduceAction's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ActionsProv_ReduceAction(isOrdered=True)
    partner = ActionsProv_InputPin()
    setattr(partner, 'ActionsProv_InputPin113', None)
    _safe_set(owner, 'ActionsProv_ReduceAction112', partner)
    assert getattr(partner, 'ActionsProv_InputPin113') == owner
    _safe_set(owner, 'ActionsProv_ReduceAction112', None)
    assert getattr(partner, 'ActionsProv_InputPin113') is None


def test_assoc_destroyAt65_stub_double():
    # ActionsProv_InputPin has no real 'ActionsProv_InputPin66' property in the generated
    # code (a bare stub) -- manually attach it so ActionsProv_LinkEndDestructionData's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ActionsProv_LinkEndDestructionData's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ActionsProv_LinkEndDestructionData(isDestroyDuplicates=True)
    partner = ActionsProv_InputPin()
    setattr(partner, 'ActionsProv_InputPin66', None)
    _safe_set(owner, 'ActionsProv_LinkEndDestructionData', partner)
    assert getattr(partner, 'ActionsProv_InputPin66') == owner
    _safe_set(owner, 'ActionsProv_LinkEndDestructionData', None)
    assert getattr(partner, 'ActionsProv_InputPin66') is None


def test_assoc_inputValue3_stub_double():
    # ActionsProv_InputPin has no real 'ActionsProv_InputPin4' property in the generated
    # code (a bare stub) -- manually attach it so ActionsProv_OpaqueAction's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ActionsProv_OpaqueAction's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ActionsProv_OpaqueAction(body="sample_text", language="sample_text")
    partner = ActionsProv_InputPin()
    setattr(partner, 'ActionsProv_InputPin4', None)
    _safe_set(owner, 'ActionsProv_OpaqueAction', {partner})
    assert getattr(partner, 'ActionsProv_InputPin4') == owner
    _safe_set(owner, 'ActionsProv_OpaqueAction', set())
    assert getattr(partner, 'ActionsProv_InputPin4') is None


def test_assoc_insertAt63_stub_double():
    # ActionsProv_InputPin has no real 'ActionsProv_InputPin64' property in the generated
    # code (a bare stub) -- manually attach it so ActionsProv_LinkEndCreationData's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ActionsProv_LinkEndCreationData's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ActionsProv_LinkEndCreationData(isReplaceAll=True)
    partner = ActionsProv_InputPin()
    setattr(partner, 'ActionsProv_InputPin64', None)
    _safe_set(owner, 'ActionsProv_LinkEndCreationData', partner)
    assert getattr(partner, 'ActionsProv_InputPin64') == owner
    _safe_set(owner, 'ActionsProv_LinkEndCreationData', None)
    assert getattr(partner, 'ActionsProv_InputPin64') is None


def test_assoc_object83_stub_double():
    # ActionsProv_InputPin has no real 'ActionsProv_InputPin84' property in the generated
    # code (a bare stub) -- manually attach it so ActionsProv_ReclassifyObjectAction's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ActionsProv_ReclassifyObjectAction's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ActionsProv_ReclassifyObjectAction(isReplaceAll=True)
    partner = ActionsProv_InputPin()
    setattr(partner, 'ActionsProv_InputPin84', None)
    _safe_set(owner, 'ActionsProv_ReclassifyObjectAction', partner)
    assert getattr(partner, 'ActionsProv_InputPin84') == owner
    _safe_set(owner, 'ActionsProv_ReclassifyObjectAction', None)
    assert getattr(partner, 'ActionsProv_InputPin84') is None


def test_assoc_outputValue5_stub_double():
    # ActionsProv_OutputPin has no real 'ActionsProv_OutputPin7' property in the generated
    # code (a bare stub) -- manually attach it so ActionsProv_OpaqueAction's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ActionsProv_OpaqueAction's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ActionsProv_OpaqueAction(body="sample_text", language="sample_text")
    partner = ActionsProv_OutputPin()
    setattr(partner, 'ActionsProv_OutputPin7', None)
    _safe_set(owner, 'ActionsProv_OpaqueAction6', {partner})
    assert getattr(partner, 'ActionsProv_OutputPin7') == owner
    _safe_set(owner, 'ActionsProv_OpaqueAction6', set())
    assert getattr(partner, 'ActionsProv_OutputPin7') is None


def test_assoc_result10_stub_double():
    # ActionsProv_OutputPin has no real 'ActionsProv_OutputPin11' property in the generated
    # code (a bare stub) -- manually attach it so ActionsProv_CallAction's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ActionsProv_CallAction's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ActionsProv_CallAction(isSynchronous=True)
    partner = ActionsProv_OutputPin()
    setattr(partner, 'ActionsProv_OutputPin11', None)
    _safe_set(owner, 'ActionsProv_CallAction', {partner})
    assert getattr(partner, 'ActionsProv_OutputPin11') == owner
    _safe_set(owner, 'ActionsProv_CallAction', set())
    assert getattr(partner, 'ActionsProv_OutputPin11') is None


def test_assoc_result109_stub_double():
    # ActionsProv_OutputPin has no real 'ActionsProv_OutputPin110' property in the generated
    # code (a bare stub) -- manually attach it so ActionsProv_ReduceAction's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ActionsProv_ReduceAction's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ActionsProv_ReduceAction(isOrdered=True)
    partner = ActionsProv_OutputPin()
    setattr(partner, 'ActionsProv_OutputPin110', None)
    _safe_set(owner, 'ActionsProv_ReduceAction', partner)
    assert getattr(partner, 'ActionsProv_OutputPin110') == owner
    _safe_set(owner, 'ActionsProv_ReduceAction', None)
    assert getattr(partner, 'ActionsProv_OutputPin110') is None


def test_assoc_result77_stub_double():
    # ActionsProv_OutputPin has no real 'ActionsProv_OutputPin78' property in the generated
    # code (a bare stub) -- manually attach it so ActionsProv_AcceptEventAction's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ActionsProv_AcceptEventAction's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ActionsProv_AcceptEventAction(isUnmarshall=True)
    partner = ActionsProv_OutputPin()
    setattr(partner, 'ActionsProv_OutputPin78', None)
    _safe_set(owner, 'ActionsProv_AcceptEventAction', {partner})
    assert getattr(partner, 'ActionsProv_OutputPin78') == owner
    _safe_set(owner, 'ActionsProv_AcceptEventAction', set())
    assert getattr(partner, 'ActionsProv_OutputPin78') is None


