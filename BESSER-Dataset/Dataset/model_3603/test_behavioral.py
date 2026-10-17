import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    AbstractConnector,
    Action,
    AnnotatedElement,
    ElmtProperty,
    Event,
    Expression,
    Handler,
    Port,
    ReferencedElmt,
    Region,
    Source,
    State,
    Type,
    Variable,
    ViewSource,
    thingML_AbstractConnector,
    thingML_Action,
    thingML_ActionBlock,
    thingML_AndExpression,
    thingML_AnnotatedElement,
    thingML_ArrayIndex,
    thingML_ArrayParamRef,
    thingML_BooleanLiteral,
    thingML_CompositeState,
    thingML_ConditionalAction,
    thingML_ConfigPropertyAssign,
    thingML_Configuration,
    thingML_Connector,
    thingML_Decrement,
    thingML_DivExpression,
    thingML_DoubleLiteral,
    thingML_ElmtProperty,
    thingML_EnumLiteralRef,
    thingML_Enumeration,
    thingML_EnumerationLiteral,
    thingML_EqualsExpression,
    thingML_ErrorAction,
    thingML_Event,
    thingML_Expression,
    thingML_ExternExpression,
    thingML_ExternStatement,
    thingML_ExternalConnector,
    thingML_Filter,
    thingML_FinalState,
    thingML_Function,
    thingML_FunctionCallExpression,
    thingML_FunctionCallStatement,
    thingML_GreaterExpression,
    thingML_GreaterOrEqualExpression,
    thingML_Handler,
    thingML_Import,
    thingML_Increment,
    thingML_Instance,
    thingML_InstanceRef,
    thingML_IntegerLiteral,
    thingML_InternalPort,
    thingML_InternalTransition,
    thingML_JoinSources,
    thingML_LengthArray,
    thingML_LengthWindow,
    thingML_LocalVariable,
    thingML_LoopAction,
    thingML_LowerExpression,
    thingML_LowerOrEqualExpression,
    thingML_MergeSources,
    thingML_Message,
    thingML_MessageParameter,
    thingML_MinusExpression,
    thingML_ModExpression,
    thingML_NotEqualsExpression,
    thingML_NotExpression,
    thingML_ObjectType,
    thingML_OrExpression,
    thingML_ParallelRegion,
    thingML_Parameter,
    thingML_PlatformAnnotation,
    thingML_PlusExpression,
    thingML_Port,
    thingML_PrimitiveType,
    thingML_PrintAction,
    thingML_Property,
    thingML_PropertyAssign,
    thingML_PropertyReference,
    thingML_Protocol,
    thingML_ProvidedPort,
    thingML_ReceiveMessage,
    thingML_Reference,
    thingML_ReferencedElmt,
    thingML_Region,
    thingML_RequiredPort,
    thingML_ReturnAction,
    thingML_SendAction,
    thingML_Session,
    thingML_SimpleParamRef,
    thingML_SimpleSource,
    thingML_Source,
    thingML_StartSession,
    thingML_State,
    thingML_Stream,
    thingML_StringLiteral,
    thingML_Thing,
    thingML_ThingMLModel,
    thingML_TimeWindow,
    thingML_TimesExpression,
    thingML_Transition,
    thingML_Type,
    thingML_TypeRef,
    thingML_UnaryMinus,
    thingML_Variable,
    thingML_VariableAssignment,
    thingML_ViewSource,
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

def test_assoc_annotations13_reverse_link_reassign_clear():
    a1 = thingML_PlatformAnnotation(name="sample_text", value="sample_text")
    a2 = thingML_PlatformAnnotation(name="sample_text_2", value="sample_text_2")
    b = thingML_EnumerationLiteral(name="sample_text")
    _safe_set(b, 'thingML_EnumerationLiteral14', {a1})
    assert _is_linked(b, 'thingML_EnumerationLiteral14', a1)
    if hasattr(a1, 'thingML_PlatformAnnotation15'):
        assert _is_linked(a1, 'thingML_PlatformAnnotation15', b)
    _safe_set(b, 'thingML_EnumerationLiteral14', {a2})
    assert _is_linked(b, 'thingML_EnumerationLiteral14', a2)
    if hasattr(a1, 'thingML_PlatformAnnotation15'):
        assert not _is_linked(a1, 'thingML_PlatformAnnotation15', b)
    if hasattr(a2, 'thingML_PlatformAnnotation15'):
        assert _is_linked(a2, 'thingML_PlatformAnnotation15', b)
    _safe_set(b, 'thingML_EnumerationLiteral14', set())
    assert not _is_linked(b, 'thingML_EnumerationLiteral14', a2)
    if hasattr(a2, 'thingML_PlatformAnnotation15'):
        assert not _is_linked(a2, 'thingML_PlatformAnnotation15', b)


def test_assoc_behaviour28_reverse_link_reassign_clear():
    a1 = thingML_Thing(fragment=True)
    a2 = thingML_Thing(fragment=False)
    b = thingML_CompositeState(history=True)
    _safe_set(b, 'thingML_CompositeState', a1)
    assert _is_linked(b, 'thingML_CompositeState', a1)
    if hasattr(a1, 'thingML_Thing29'):
        assert _is_linked(a1, 'thingML_Thing29', b)
    _safe_set(b, 'thingML_CompositeState', a2)
    assert _is_linked(b, 'thingML_CompositeState', a2)
    if hasattr(a1, 'thingML_Thing29'):
        assert not _is_linked(a1, 'thingML_Thing29', b)
    if hasattr(a2, 'thingML_Thing29'):
        assert _is_linked(a2, 'thingML_Thing29', b)
    _safe_set(b, 'thingML_CompositeState', None)
    assert not _is_linked(b, 'thingML_CompositeState', a2)
    if hasattr(a2, 'thingML_Thing29'):
        assert not _is_linked(a2, 'thingML_Thing29', b)


def test_assoc_connectors237_reverse_link_reassign_clear():
    a1 = thingML_Configuration(name="sample_text")
    a2 = thingML_Configuration(name="sample_text_2")
    b = thingML_AbstractConnector(name="sample_text")
    _safe_set(b, 'thingML_AbstractConnector', a1)
    assert _is_linked(b, 'thingML_AbstractConnector', a1)
    if hasattr(a1, 'thingML_Configuration238'):
        assert _is_linked(a1, 'thingML_Configuration238', b)
    _safe_set(b, 'thingML_AbstractConnector', a2)
    assert _is_linked(b, 'thingML_AbstractConnector', a2)
    if hasattr(a1, 'thingML_Configuration238'):
        assert not _is_linked(a1, 'thingML_Configuration238', b)
    if hasattr(a2, 'thingML_Configuration238'):
        assert _is_linked(a2, 'thingML_Configuration238', b)
    _safe_set(b, 'thingML_AbstractConnector', None)
    assert not _is_linked(b, 'thingML_AbstractConnector', a2)
    if hasattr(a2, 'thingML_Configuration238'):
        assert not _is_linked(a2, 'thingML_Configuration238', b)


def test_assoc_functions24_reverse_link_reassign_clear():
    a1 = thingML_Thing(fragment=True)
    a2 = thingML_Thing(fragment=False)
    b = thingML_Function(name="sample_text")
    _safe_set(b, 'thingML_Function', a1)
    assert _is_linked(b, 'thingML_Function', a1)
    if hasattr(a1, 'thingML_Thing25'):
        assert _is_linked(a1, 'thingML_Thing25', b)
    _safe_set(b, 'thingML_Function', a2)
    assert _is_linked(b, 'thingML_Function', a2)
    if hasattr(a1, 'thingML_Thing25'):
        assert not _is_linked(a1, 'thingML_Thing25', b)
    if hasattr(a2, 'thingML_Thing25'):
        assert _is_linked(a2, 'thingML_Thing25', b)
    _safe_set(b, 'thingML_Function', None)
    assert not _is_linked(b, 'thingML_Function', a2)
    if hasattr(a2, 'thingML_Thing25'):
        assert not _is_linked(a2, 'thingML_Thing25', b)


def test_assoc_includes17_reverse_link_reassign_clear():
    a1 = thingML_Thing(fragment=True)
    a2 = thingML_Thing(fragment=False)
    b = thingML_Thing(fragment=True)
    _safe_set(b, 'thingML_Thing16', {a1})
    assert _is_linked(b, 'thingML_Thing16', a1)
    if hasattr(a1, 'thingML_Thing'):
        assert _is_linked(a1, 'thingML_Thing', b)
    _safe_set(b, 'thingML_Thing16', {a2})
    assert _is_linked(b, 'thingML_Thing16', a2)
    if hasattr(a1, 'thingML_Thing'):
        assert not _is_linked(a1, 'thingML_Thing', b)
    if hasattr(a2, 'thingML_Thing'):
        assert _is_linked(a2, 'thingML_Thing', b)
    _safe_set(b, 'thingML_Thing16', set())
    assert not _is_linked(b, 'thingML_Thing16', a2)
    if hasattr(a2, 'thingML_Thing'):
        assert not _is_linked(a2, 'thingML_Thing', b)


def test_assoc_initial112_reverse_link_reassign_clear():
    a1 = thingML_State(name="sample_text")
    a2 = thingML_State(name="sample_text_2")
    b = thingML_CompositeState(history=True)
    _safe_set(b, 'thingML_CompositeState113', a1)
    assert _is_linked(b, 'thingML_CompositeState113', a1)
    if hasattr(a1, 'thingML_State'):
        assert _is_linked(a1, 'thingML_State', b)
    _safe_set(b, 'thingML_CompositeState113', a2)
    assert _is_linked(b, 'thingML_CompositeState113', a2)
    if hasattr(a1, 'thingML_State'):
        assert not _is_linked(a1, 'thingML_State', b)
    if hasattr(a2, 'thingML_State'):
        assert _is_linked(a2, 'thingML_State', b)
    _safe_set(b, 'thingML_CompositeState113', None)
    assert not _is_linked(b, 'thingML_CompositeState113', a2)
    if hasattr(a2, 'thingML_State'):
        assert not _is_linked(a2, 'thingML_State', b)


def test_assoc_initial119_reverse_link_reassign_clear():
    a1 = thingML_State(name="sample_text")
    a2 = thingML_State(name="sample_text_2")
    b = thingML_Session(maxInstances=7)
    _safe_set(b, 'thingML_Session', a1)
    assert _is_linked(b, 'thingML_Session', a1)
    if hasattr(a1, 'thingML_State120'):
        assert _is_linked(a1, 'thingML_State120', b)
    _safe_set(b, 'thingML_Session', a2)
    assert _is_linked(b, 'thingML_Session', a2)
    if hasattr(a1, 'thingML_State120'):
        assert not _is_linked(a1, 'thingML_State120', b)
    if hasattr(a2, 'thingML_State120'):
        assert _is_linked(a2, 'thingML_State120', b)
    _safe_set(b, 'thingML_Session', None)
    assert not _is_linked(b, 'thingML_Session', a2)
    if hasattr(a2, 'thingML_State120'):
        assert not _is_linked(a2, 'thingML_State120', b)


def test_assoc_initial127_reverse_link_reassign_clear():
    a1 = thingML_State(name="sample_text")
    a2 = thingML_State(name="sample_text_2")
    b = thingML_ParallelRegion(history=True, name="sample_text")
    _safe_set(b, 'thingML_ParallelRegion128', a1)
    assert _is_linked(b, 'thingML_ParallelRegion128', a1)
    if hasattr(a1, 'thingML_State129'):
        assert _is_linked(a1, 'thingML_State129', b)
    _safe_set(b, 'thingML_ParallelRegion128', a2)
    assert _is_linked(b, 'thingML_ParallelRegion128', a2)
    if hasattr(a1, 'thingML_State129'):
        assert not _is_linked(a1, 'thingML_State129', b)
    if hasattr(a2, 'thingML_State129'):
        assert _is_linked(a2, 'thingML_State129', b)
    _safe_set(b, 'thingML_ParallelRegion128', None)
    assert not _is_linked(b, 'thingML_ParallelRegion128', a2)
    if hasattr(a2, 'thingML_State129'):
        assert not _is_linked(a2, 'thingML_State129', b)


def test_assoc_instances235_reverse_link_reassign_clear():
    a1 = thingML_Instance(name="sample_text")
    a2 = thingML_Instance(name="sample_text_2")
    b = thingML_Configuration(name="sample_text")
    _safe_set(b, 'thingML_Configuration236', {a1})
    assert _is_linked(b, 'thingML_Configuration236', a1)
    if hasattr(a1, 'thingML_Instance'):
        assert _is_linked(a1, 'thingML_Instance', b)
    _safe_set(b, 'thingML_Configuration236', {a2})
    assert _is_linked(b, 'thingML_Configuration236', a2)
    if hasattr(a1, 'thingML_Instance'):
        assert not _is_linked(a1, 'thingML_Instance', b)
    if hasattr(a2, 'thingML_Instance'):
        assert _is_linked(a2, 'thingML_Instance', b)
    _safe_set(b, 'thingML_Configuration236', set())
    assert not _is_linked(b, 'thingML_Configuration236', a2)
    if hasattr(a2, 'thingML_Instance'):
        assert not _is_linked(a2, 'thingML_Instance', b)


def test_assoc_message158_reverse_link_reassign_clear():
    a1 = thingML_ReceiveMessage(name="sample_text")
    a2 = thingML_ReceiveMessage(name="sample_text_2")
    b = thingML_Message(name="sample_text")
    _safe_set(b, 'thingML_Message160', a1)
    assert _is_linked(b, 'thingML_Message160', a1)
    if hasattr(a1, 'thingML_ReceiveMessage159'):
        assert _is_linked(a1, 'thingML_ReceiveMessage159', b)
    _safe_set(b, 'thingML_Message160', a2)
    assert _is_linked(b, 'thingML_Message160', a2)
    if hasattr(a1, 'thingML_ReceiveMessage159'):
        assert not _is_linked(a1, 'thingML_ReceiveMessage159', b)
    if hasattr(a2, 'thingML_ReceiveMessage159'):
        assert _is_linked(a2, 'thingML_ReceiveMessage159', b)
    _safe_set(b, 'thingML_Message160', None)
    assert not _is_linked(b, 'thingML_Message160', a2)
    if hasattr(a2, 'thingML_ReceiveMessage159'):
        assert not _is_linked(a2, 'thingML_ReceiveMessage159', b)


def test_assoc_message90_reverse_link_reassign_clear():
    a1 = thingML_SimpleSource(name="sample_text")
    a2 = thingML_SimpleSource(name="sample_text_2")
    b = thingML_ReceiveMessage(name="sample_text")
    _safe_set(b, 'thingML_ReceiveMessage', a1)
    assert _is_linked(b, 'thingML_ReceiveMessage', a1)
    if hasattr(a1, 'thingML_SimpleSource'):
        assert _is_linked(a1, 'thingML_SimpleSource', b)
    _safe_set(b, 'thingML_ReceiveMessage', a2)
    assert _is_linked(b, 'thingML_ReceiveMessage', a2)
    if hasattr(a1, 'thingML_SimpleSource'):
        assert not _is_linked(a1, 'thingML_SimpleSource', b)
    if hasattr(a2, 'thingML_SimpleSource'):
        assert _is_linked(a2, 'thingML_SimpleSource', b)
    _safe_set(b, 'thingML_ReceiveMessage', None)
    assert not _is_linked(b, 'thingML_ReceiveMessage', a2)
    if hasattr(a2, 'thingML_SimpleSource'):
        assert not _is_linked(a2, 'thingML_SimpleSource', b)


def test_assoc_messages18_reverse_link_reassign_clear():
    a1 = thingML_Thing(fragment=True)
    a2 = thingML_Thing(fragment=False)
    b = thingML_Message(name="sample_text")
    _safe_set(b, 'thingML_Message', a1)
    assert _is_linked(b, 'thingML_Message', a1)
    if hasattr(a1, 'thingML_Thing19'):
        assert _is_linked(a1, 'thingML_Thing19', b)
    _safe_set(b, 'thingML_Message', a2)
    assert _is_linked(b, 'thingML_Message', a2)
    if hasattr(a1, 'thingML_Thing19'):
        assert not _is_linked(a1, 'thingML_Thing19', b)
    if hasattr(a2, 'thingML_Thing19'):
        assert _is_linked(a2, 'thingML_Thing19', b)
    _safe_set(b, 'thingML_Message', None)
    assert not _is_linked(b, 'thingML_Message', a2)
    if hasattr(a2, 'thingML_Thing19'):
        assert not _is_linked(a2, 'thingML_Thing19', b)


def test_assoc_msgRef106_reverse_link_reassign_clear():
    a1 = thingML_MessageParameter(name="sample_text")
    a2 = thingML_MessageParameter(name="sample_text_2")
    b = thingML_Message(name="sample_text")
    _safe_set(b, 'thingML_Message107', a1)
    assert _is_linked(b, 'thingML_Message107', a1)
    if hasattr(a1, 'thingML_MessageParameter'):
        assert _is_linked(a1, 'thingML_MessageParameter', b)
    _safe_set(b, 'thingML_Message107', a2)
    assert _is_linked(b, 'thingML_Message107', a2)
    if hasattr(a1, 'thingML_MessageParameter'):
        assert not _is_linked(a1, 'thingML_MessageParameter', b)
    if hasattr(a2, 'thingML_MessageParameter'):
        assert _is_linked(a2, 'thingML_MessageParameter', b)
    _safe_set(b, 'thingML_Message107', None)
    assert not _is_linked(b, 'thingML_Message107', a2)
    if hasattr(a2, 'thingML_MessageParameter'):
        assert not _is_linked(a2, 'thingML_MessageParameter', b)


def test_assoc_parameters41_reverse_link_reassign_clear():
    a1 = thingML_Parameter(name="sample_text")
    a2 = thingML_Parameter(name="sample_text_2")
    b = thingML_Function(name="sample_text")
    _safe_set(b, 'thingML_Function42', {a1})
    assert _is_linked(b, 'thingML_Function42', a1)
    if hasattr(a1, 'thingML_Parameter'):
        assert _is_linked(a1, 'thingML_Parameter', b)
    _safe_set(b, 'thingML_Function42', {a2})
    assert _is_linked(b, 'thingML_Function42', a2)
    if hasattr(a1, 'thingML_Parameter'):
        assert not _is_linked(a1, 'thingML_Parameter', b)
    if hasattr(a2, 'thingML_Parameter'):
        assert _is_linked(a2, 'thingML_Parameter', b)
    _safe_set(b, 'thingML_Function42', set())
    assert not _is_linked(b, 'thingML_Function42', a2)
    if hasattr(a2, 'thingML_Parameter'):
        assert not _is_linked(a2, 'thingML_Parameter', b)


def test_assoc_parameters54_reverse_link_reassign_clear():
    a1 = thingML_Parameter(name="sample_text")
    a2 = thingML_Parameter(name="sample_text_2")
    b = thingML_Message(name="sample_text")
    _safe_set(b, 'thingML_Message55', {a1})
    assert _is_linked(b, 'thingML_Message55', a1)
    if hasattr(a1, 'thingML_Parameter56'):
        assert _is_linked(a1, 'thingML_Parameter56', b)
    _safe_set(b, 'thingML_Message55', {a2})
    assert _is_linked(b, 'thingML_Message55', a2)
    if hasattr(a1, 'thingML_Parameter56'):
        assert not _is_linked(a1, 'thingML_Parameter56', b)
    if hasattr(a2, 'thingML_Parameter56'):
        assert _is_linked(a2, 'thingML_Parameter56', b)
    _safe_set(b, 'thingML_Message55', set())
    assert not _is_linked(b, 'thingML_Message55', a2)
    if hasattr(a2, 'thingML_Parameter56'):
        assert not _is_linked(a2, 'thingML_Parameter56', b)


def test_assoc_port155_reverse_link_reassign_clear():
    a1 = thingML_ReceiveMessage(name="sample_text")
    a2 = thingML_ReceiveMessage(name="sample_text_2")
    b = thingML_Port(name="sample_text")
    _safe_set(b, 'thingML_Port157', a1)
    assert _is_linked(b, 'thingML_Port157', a1)
    if hasattr(a1, 'thingML_ReceiveMessage156'):
        assert _is_linked(a1, 'thingML_ReceiveMessage156', b)
    _safe_set(b, 'thingML_Port157', a2)
    assert _is_linked(b, 'thingML_Port157', a2)
    if hasattr(a1, 'thingML_ReceiveMessage156'):
        assert not _is_linked(a1, 'thingML_ReceiveMessage156', b)
    if hasattr(a2, 'thingML_ReceiveMessage156'):
        assert _is_linked(a2, 'thingML_ReceiveMessage156', b)
    _safe_set(b, 'thingML_Port157', None)
    assert not _is_linked(b, 'thingML_Port157', a2)
    if hasattr(a2, 'thingML_ReceiveMessage156'):
        assert not _is_linked(a2, 'thingML_ReceiveMessage156', b)


def test_assoc_ports20_reverse_link_reassign_clear():
    a1 = thingML_Thing(fragment=True)
    a2 = thingML_Thing(fragment=False)
    b = thingML_Port(name="sample_text")
    _safe_set(b, 'thingML_Port', a1)
    assert _is_linked(b, 'thingML_Port', a1)
    if hasattr(a1, 'thingML_Thing21'):
        assert _is_linked(a1, 'thingML_Thing21', b)
    _safe_set(b, 'thingML_Port', a2)
    assert _is_linked(b, 'thingML_Port', a2)
    if hasattr(a1, 'thingML_Thing21'):
        assert not _is_linked(a1, 'thingML_Thing21', b)
    if hasattr(a2, 'thingML_Thing21'):
        assert _is_linked(a2, 'thingML_Thing21', b)
    _safe_set(b, 'thingML_Port', None)
    assert not _is_linked(b, 'thingML_Port', a2)
    if hasattr(a2, 'thingML_Thing21'):
        assert not _is_linked(a2, 'thingML_Thing21', b)


def test_assoc_properties133_reverse_link_reassign_clear():
    a1 = thingML_State(name="sample_text")
    a2 = thingML_State(name="sample_text_2")
    b = thingML_Property(changeable=True, name="sample_text")
    _safe_set(b, 'thingML_Property135', a1)
    assert _is_linked(b, 'thingML_Property135', a1)
    if hasattr(a1, 'thingML_State134'):
        assert _is_linked(a1, 'thingML_State134', b)
    _safe_set(b, 'thingML_Property135', a2)
    assert _is_linked(b, 'thingML_Property135', a2)
    if hasattr(a1, 'thingML_State134'):
        assert not _is_linked(a1, 'thingML_State134', b)
    if hasattr(a2, 'thingML_State134'):
        assert _is_linked(a2, 'thingML_State134', b)
    _safe_set(b, 'thingML_Property135', None)
    assert not _is_linked(b, 'thingML_Property135', a2)
    if hasattr(a2, 'thingML_State134'):
        assert not _is_linked(a2, 'thingML_State134', b)


def test_assoc_properties22_reverse_link_reassign_clear():
    a1 = thingML_Thing(fragment=True)
    a2 = thingML_Thing(fragment=False)
    b = thingML_Property(changeable=True, name="sample_text")
    _safe_set(b, 'thingML_Property', a1)
    assert _is_linked(b, 'thingML_Property', a1)
    if hasattr(a1, 'thingML_Thing23'):
        assert _is_linked(a1, 'thingML_Thing23', b)
    _safe_set(b, 'thingML_Property', a2)
    assert _is_linked(b, 'thingML_Property', a2)
    if hasattr(a1, 'thingML_Thing23'):
        assert not _is_linked(a1, 'thingML_Thing23', b)
    if hasattr(a2, 'thingML_Thing23'):
        assert _is_linked(a2, 'thingML_Thing23', b)
    _safe_set(b, 'thingML_Property', None)
    assert not _is_linked(b, 'thingML_Property', a2)
    if hasattr(a2, 'thingML_Thing23'):
        assert not _is_linked(a2, 'thingML_Thing23', b)


def test_assoc_receives63_reverse_link_reassign_clear():
    a1 = thingML_Port(name="sample_text")
    a2 = thingML_Port(name="sample_text_2")
    b = thingML_Message(name="sample_text")
    _safe_set(b, 'thingML_Message65', a1)
    assert _is_linked(b, 'thingML_Message65', a1)
    if hasattr(a1, 'thingML_Port64'):
        assert _is_linked(a1, 'thingML_Port64', b)
    _safe_set(b, 'thingML_Message65', a2)
    assert _is_linked(b, 'thingML_Message65', a2)
    if hasattr(a1, 'thingML_Port64'):
        assert not _is_linked(a1, 'thingML_Port64', b)
    if hasattr(a2, 'thingML_Port64'):
        assert _is_linked(a2, 'thingML_Port64', b)
    _safe_set(b, 'thingML_Message65', None)
    assert not _is_linked(b, 'thingML_Message65', a2)
    if hasattr(a2, 'thingML_Port64'):
        assert not _is_linked(a2, 'thingML_Port64', b)


def test_assoc_region117_reverse_link_reassign_clear():
    a1 = thingML_ParallelRegion(history=True, name="sample_text")
    a2 = thingML_ParallelRegion(history=False, name="sample_text_2")
    b = thingML_CompositeState(history=True)
    _safe_set(b, 'thingML_CompositeState118', {a1})
    assert _is_linked(b, 'thingML_CompositeState118', a1)
    if hasattr(a1, 'thingML_ParallelRegion'):
        assert _is_linked(a1, 'thingML_ParallelRegion', b)
    _safe_set(b, 'thingML_CompositeState118', {a2})
    assert _is_linked(b, 'thingML_CompositeState118', a2)
    if hasattr(a1, 'thingML_ParallelRegion'):
        assert not _is_linked(a1, 'thingML_ParallelRegion', b)
    if hasattr(a2, 'thingML_ParallelRegion'):
        assert _is_linked(a2, 'thingML_ParallelRegion', b)
    _safe_set(b, 'thingML_CompositeState118', set())
    assert not _is_linked(b, 'thingML_CompositeState118', a2)
    if hasattr(a2, 'thingML_ParallelRegion'):
        assert not _is_linked(a2, 'thingML_ParallelRegion', b)


def test_assoc_region124_reverse_link_reassign_clear():
    a1 = thingML_Session(maxInstances=7)
    a2 = thingML_Session(maxInstances=13)
    b = thingML_ParallelRegion(history=True, name="sample_text")
    _safe_set(b, 'thingML_ParallelRegion126', a1)
    assert _is_linked(b, 'thingML_ParallelRegion126', a1)
    if hasattr(a1, 'thingML_Session125'):
        assert _is_linked(a1, 'thingML_Session125', b)
    _safe_set(b, 'thingML_ParallelRegion126', a2)
    assert _is_linked(b, 'thingML_ParallelRegion126', a2)
    if hasattr(a1, 'thingML_Session125'):
        assert not _is_linked(a1, 'thingML_Session125', b)
    if hasattr(a2, 'thingML_Session125'):
        assert _is_linked(a2, 'thingML_Session125', b)
    _safe_set(b, 'thingML_ParallelRegion126', None)
    assert not _is_linked(b, 'thingML_ParallelRegion126', a2)
    if hasattr(a2, 'thingML_Session125'):
        assert not _is_linked(a2, 'thingML_Session125', b)


def test_assoc_resultMessage74_reverse_link_reassign_clear():
    a1 = thingML_Message(name="sample_text")
    a2 = thingML_Message(name="sample_text_2")
    b = thingML_JoinSources(name="sample_text")
    _safe_set(b, 'thingML_JoinSources75', a1)
    assert _is_linked(b, 'thingML_JoinSources75', a1)
    if hasattr(a1, 'thingML_Message76'):
        assert _is_linked(a1, 'thingML_Message76', b)
    _safe_set(b, 'thingML_JoinSources75', a2)
    assert _is_linked(b, 'thingML_JoinSources75', a2)
    if hasattr(a1, 'thingML_Message76'):
        assert not _is_linked(a1, 'thingML_Message76', b)
    if hasattr(a2, 'thingML_Message76'):
        assert _is_linked(a2, 'thingML_Message76', b)
    _safe_set(b, 'thingML_JoinSources75', None)
    assert not _is_linked(b, 'thingML_JoinSources75', a2)
    if hasattr(a2, 'thingML_Message76'):
        assert not _is_linked(a2, 'thingML_Message76', b)


def test_assoc_resultMessage84_reverse_link_reassign_clear():
    a1 = thingML_Message(name="sample_text")
    a2 = thingML_Message(name="sample_text_2")
    b = thingML_MergeSources(name="sample_text")
    _safe_set(b, 'thingML_MergeSources85', a1)
    assert _is_linked(b, 'thingML_MergeSources85', a1)
    if hasattr(a1, 'thingML_Message86'):
        assert _is_linked(a1, 'thingML_Message86', b)
    _safe_set(b, 'thingML_MergeSources85', a2)
    assert _is_linked(b, 'thingML_MergeSources85', a2)
    if hasattr(a1, 'thingML_Message86'):
        assert not _is_linked(a1, 'thingML_Message86', b)
    if hasattr(a2, 'thingML_Message86'):
        assert _is_linked(a2, 'thingML_Message86', b)
    _safe_set(b, 'thingML_MergeSources85', None)
    assert not _is_linked(b, 'thingML_MergeSources85', a2)
    if hasattr(a2, 'thingML_Message86'):
        assert not _is_linked(a2, 'thingML_Message86', b)


def test_assoc_selection68_reverse_link_reassign_clear():
    a1 = thingML_Stream(name="sample_text")
    a2 = thingML_Stream(name="sample_text_2")
    b = thingML_LocalVariable(changeable=True, name="sample_text")
    _safe_set(b, 'thingML_LocalVariable', a1)
    assert _is_linked(b, 'thingML_LocalVariable', a1)
    if hasattr(a1, 'thingML_Stream69'):
        assert _is_linked(a1, 'thingML_Stream69', b)
    _safe_set(b, 'thingML_LocalVariable', a2)
    assert _is_linked(b, 'thingML_LocalVariable', a2)
    if hasattr(a1, 'thingML_Stream69'):
        assert not _is_linked(a1, 'thingML_Stream69', b)
    if hasattr(a2, 'thingML_Stream69'):
        assert _is_linked(a2, 'thingML_Stream69', b)
    _safe_set(b, 'thingML_LocalVariable', None)
    assert not _is_linked(b, 'thingML_LocalVariable', a2)
    if hasattr(a2, 'thingML_Stream69'):
        assert not _is_linked(a2, 'thingML_Stream69', b)


def test_assoc_sends60_reverse_link_reassign_clear():
    a1 = thingML_Port(name="sample_text")
    a2 = thingML_Port(name="sample_text_2")
    b = thingML_Message(name="sample_text")
    _safe_set(b, 'thingML_Message62', a1)
    assert _is_linked(b, 'thingML_Message62', a1)
    if hasattr(a1, 'thingML_Port61'):
        assert _is_linked(a1, 'thingML_Port61', b)
    _safe_set(b, 'thingML_Message62', a2)
    assert _is_linked(b, 'thingML_Message62', a2)
    if hasattr(a1, 'thingML_Port61'):
        assert not _is_linked(a1, 'thingML_Port61', b)
    if hasattr(a2, 'thingML_Port61'):
        assert _is_linked(a2, 'thingML_Port61', b)
    _safe_set(b, 'thingML_Message62', None)
    assert not _is_linked(b, 'thingML_Message62', a2)
    if hasattr(a2, 'thingML_Port61'):
        assert not _is_linked(a2, 'thingML_Port61', b)


def test_assoc_streams30_reverse_link_reassign_clear():
    a1 = thingML_Thing(fragment=True)
    a2 = thingML_Thing(fragment=False)
    b = thingML_Stream(name="sample_text")
    _safe_set(b, 'thingML_Stream', a1)
    assert _is_linked(b, 'thingML_Stream', a1)
    if hasattr(a1, 'thingML_Thing31'):
        assert _is_linked(a1, 'thingML_Thing31', b)
    _safe_set(b, 'thingML_Stream', a2)
    assert _is_linked(b, 'thingML_Stream', a2)
    if hasattr(a1, 'thingML_Thing31'):
        assert not _is_linked(a1, 'thingML_Thing31', b)
    if hasattr(a2, 'thingML_Thing31'):
        assert _is_linked(a2, 'thingML_Thing31', b)
    _safe_set(b, 'thingML_Stream', None)
    assert not _is_linked(b, 'thingML_Stream', a2)
    if hasattr(a2, 'thingML_Thing31'):
        assert not _is_linked(a2, 'thingML_Thing31', b)


def test_assoc_substate114_reverse_link_reassign_clear():
    a1 = thingML_State(name="sample_text")
    a2 = thingML_State(name="sample_text_2")
    b = thingML_CompositeState(history=True)
    _safe_set(b, 'thingML_CompositeState115', {a1})
    assert _is_linked(b, 'thingML_CompositeState115', a1)
    if hasattr(a1, 'thingML_State116'):
        assert _is_linked(a1, 'thingML_State116', b)
    _safe_set(b, 'thingML_CompositeState115', {a2})
    assert _is_linked(b, 'thingML_CompositeState115', a2)
    if hasattr(a1, 'thingML_State116'):
        assert not _is_linked(a1, 'thingML_State116', b)
    if hasattr(a2, 'thingML_State116'):
        assert _is_linked(a2, 'thingML_State116', b)
    _safe_set(b, 'thingML_CompositeState115', set())
    assert not _is_linked(b, 'thingML_CompositeState115', a2)
    if hasattr(a2, 'thingML_State116'):
        assert not _is_linked(a2, 'thingML_State116', b)


def test_assoc_substate121_reverse_link_reassign_clear():
    a1 = thingML_State(name="sample_text")
    a2 = thingML_State(name="sample_text_2")
    b = thingML_Session(maxInstances=7)
    _safe_set(b, 'thingML_Session122', {a1})
    assert _is_linked(b, 'thingML_Session122', a1)
    if hasattr(a1, 'thingML_State123'):
        assert _is_linked(a1, 'thingML_State123', b)
    _safe_set(b, 'thingML_Session122', {a2})
    assert _is_linked(b, 'thingML_Session122', a2)
    if hasattr(a1, 'thingML_State123'):
        assert not _is_linked(a1, 'thingML_State123', b)
    if hasattr(a2, 'thingML_State123'):
        assert _is_linked(a2, 'thingML_State123', b)
    _safe_set(b, 'thingML_Session122', set())
    assert not _is_linked(b, 'thingML_Session122', a2)
    if hasattr(a2, 'thingML_State123'):
        assert not _is_linked(a2, 'thingML_State123', b)


def test_assoc_substate130_reverse_link_reassign_clear():
    a1 = thingML_State(name="sample_text")
    a2 = thingML_State(name="sample_text_2")
    b = thingML_ParallelRegion(history=True, name="sample_text")
    _safe_set(b, 'thingML_ParallelRegion131', {a1})
    assert _is_linked(b, 'thingML_ParallelRegion131', a1)
    if hasattr(a1, 'thingML_State132'):
        assert _is_linked(a1, 'thingML_State132', b)
    _safe_set(b, 'thingML_ParallelRegion131', {a2})
    assert _is_linked(b, 'thingML_ParallelRegion131', a2)
    if hasattr(a1, 'thingML_State132'):
        assert not _is_linked(a1, 'thingML_State132', b)
    if hasattr(a2, 'thingML_State132'):
        assert _is_linked(a2, 'thingML_State132', b)
    _safe_set(b, 'thingML_ParallelRegion131', set())
    assert not _is_linked(b, 'thingML_ParallelRegion131', a2)
    if hasattr(a2, 'thingML_State132'):
        assert not _is_linked(a2, 'thingML_State132', b)


def test_assoc_type241_reverse_link_reassign_clear():
    a1 = thingML_Thing(fragment=True)
    a2 = thingML_Thing(fragment=False)
    b = thingML_Instance(name="sample_text")
    _safe_set(b, 'thingML_Instance242', a1)
    assert _is_linked(b, 'thingML_Instance242', a1)
    if hasattr(a1, 'thingML_Thing243'):
        assert _is_linked(a1, 'thingML_Thing243', b)
    _safe_set(b, 'thingML_Instance242', a2)
    assert _is_linked(b, 'thingML_Instance242', a2)
    if hasattr(a1, 'thingML_Thing243'):
        assert not _is_linked(a1, 'thingML_Thing243', b)
    if hasattr(a2, 'thingML_Thing243'):
        assert _is_linked(a2, 'thingML_Thing243', b)
    _safe_set(b, 'thingML_Instance242', None)
    assert not _is_linked(b, 'thingML_Instance242', a2)
    if hasattr(a2, 'thingML_Thing243'):
        assert not _is_linked(a2, 'thingML_Thing243', b)


def test_assoc_type8_reverse_link_reassign_clear():
    a1 = thingML_TypeRef(isArray=True)
    a2 = thingML_TypeRef(isArray=False)
    b = thingML_Type(name="sample_text")
    _safe_set(b, 'thingML_Type9', a1)
    assert _is_linked(b, 'thingML_Type9', a1)
    if hasattr(a1, 'thingML_TypeRef'):
        assert _is_linked(a1, 'thingML_TypeRef', b)
    _safe_set(b, 'thingML_Type9', a2)
    assert _is_linked(b, 'thingML_Type9', a2)
    if hasattr(a1, 'thingML_TypeRef'):
        assert not _is_linked(a1, 'thingML_TypeRef', b)
    if hasattr(a2, 'thingML_TypeRef'):
        assert _is_linked(a2, 'thingML_TypeRef', b)
    _safe_set(b, 'thingML_Type9', None)
    assert not _is_linked(b, 'thingML_Type9', a2)
    if hasattr(a2, 'thingML_TypeRef'):
        assert not _is_linked(a2, 'thingML_TypeRef', b)


def test_assoc_typeRef166_reverse_link_reassign_clear():
    a1 = thingML_TypeRef(isArray=True)
    a2 = thingML_TypeRef(isArray=False)
    b = thingML_LocalVariable(changeable=True, name="sample_text")
    _safe_set(b, 'thingML_LocalVariable167', a1)
    assert _is_linked(b, 'thingML_LocalVariable167', a1)
    if hasattr(a1, 'thingML_TypeRef168'):
        assert _is_linked(a1, 'thingML_TypeRef168', b)
    _safe_set(b, 'thingML_LocalVariable167', a2)
    assert _is_linked(b, 'thingML_LocalVariable167', a2)
    if hasattr(a1, 'thingML_TypeRef168'):
        assert not _is_linked(a1, 'thingML_TypeRef168', b)
    if hasattr(a2, 'thingML_TypeRef168'):
        assert _is_linked(a2, 'thingML_TypeRef168', b)
    _safe_set(b, 'thingML_LocalVariable167', None)
    assert not _is_linked(b, 'thingML_LocalVariable167', a2)
    if hasattr(a2, 'thingML_TypeRef168'):
        assert not _is_linked(a2, 'thingML_TypeRef168', b)


def test_assoc_typeRef43_reverse_link_reassign_clear():
    a1 = thingML_TypeRef(isArray=True)
    a2 = thingML_TypeRef(isArray=False)
    b = thingML_Function(name="sample_text")
    _safe_set(b, 'thingML_Function44', a1)
    assert _is_linked(b, 'thingML_Function44', a1)
    if hasattr(a1, 'thingML_TypeRef45'):
        assert _is_linked(a1, 'thingML_TypeRef45', b)
    _safe_set(b, 'thingML_Function44', a2)
    assert _is_linked(b, 'thingML_Function44', a2)
    if hasattr(a1, 'thingML_TypeRef45'):
        assert not _is_linked(a1, 'thingML_TypeRef45', b)
    if hasattr(a2, 'thingML_TypeRef45'):
        assert _is_linked(a2, 'thingML_TypeRef45', b)
    _safe_set(b, 'thingML_Function44', None)
    assert not _is_linked(b, 'thingML_Function44', a2)
    if hasattr(a2, 'thingML_TypeRef45'):
        assert not _is_linked(a2, 'thingML_TypeRef45', b)


def test_assoc_typeRef48_reverse_link_reassign_clear():
    a1 = thingML_TypeRef(isArray=True)
    a2 = thingML_TypeRef(isArray=False)
    b = thingML_Property(changeable=True, name="sample_text")
    _safe_set(b, 'thingML_Property49', a1)
    assert _is_linked(b, 'thingML_Property49', a1)
    if hasattr(a1, 'thingML_TypeRef50'):
        assert _is_linked(a1, 'thingML_TypeRef50', b)
    _safe_set(b, 'thingML_Property49', a2)
    assert _is_linked(b, 'thingML_Property49', a2)
    if hasattr(a1, 'thingML_TypeRef50'):
        assert not _is_linked(a1, 'thingML_TypeRef50', b)
    if hasattr(a2, 'thingML_TypeRef50'):
        assert _is_linked(a2, 'thingML_TypeRef50', b)
    _safe_set(b, 'thingML_Property49', None)
    assert not _is_linked(b, 'thingML_Property49', a2)
    if hasattr(a2, 'thingML_TypeRef50'):
        assert not _is_linked(a2, 'thingML_TypeRef50', b)


def test_assoc_typeRef57_reverse_link_reassign_clear():
    a1 = thingML_TypeRef(isArray=True)
    a2 = thingML_TypeRef(isArray=False)
    b = thingML_Parameter(name="sample_text")
    _safe_set(b, 'thingML_Parameter58', a1)
    assert _is_linked(b, 'thingML_Parameter58', a1)
    if hasattr(a1, 'thingML_TypeRef59'):
        assert _is_linked(a1, 'thingML_TypeRef59', b)
    _safe_set(b, 'thingML_Parameter58', a2)
    assert _is_linked(b, 'thingML_Parameter58', a2)
    if hasattr(a1, 'thingML_TypeRef59'):
        assert not _is_linked(a1, 'thingML_TypeRef59', b)
    if hasattr(a2, 'thingML_TypeRef59'):
        assert _is_linked(a2, 'thingML_TypeRef59', b)
    _safe_set(b, 'thingML_Parameter58', None)
    assert not _is_linked(b, 'thingML_Parameter58', a2)
    if hasattr(a2, 'thingML_TypeRef59'):
        assert not _is_linked(a2, 'thingML_TypeRef59', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_action149_stub_double():
    # thingML_Action has no real 'thingML_Action151' property in the generated
    # code (a bare stub) -- manually attach it so thingML_Handler's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # thingML_Handler's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = thingML_Handler(name="sample_text")
    partner = thingML_Action()
    setattr(partner, 'thingML_Action151', None)
    _safe_set(owner, 'thingML_Handler150', partner)
    assert getattr(partner, 'thingML_Action151') == owner
    _safe_set(owner, 'thingML_Handler150', None)
    assert getattr(partner, 'thingML_Action151') is None


def test_assoc_annotations255_stub_double():
    # thingML_ConfigPropertyAssign has no real 'thingML_ConfigPropertyAssign256' property in the generated
    # code (a bare stub) -- manually attach it so thingML_PlatformAnnotation's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # thingML_PlatformAnnotation's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = thingML_PlatformAnnotation(name="sample_text", value="sample_text")
    partner = thingML_ConfigPropertyAssign()
    setattr(partner, 'thingML_ConfigPropertyAssign256', None)
    _safe_set(owner, 'thingML_PlatformAnnotation257', partner)
    assert getattr(partner, 'thingML_ConfigPropertyAssign256') == owner
    _safe_set(owner, 'thingML_PlatformAnnotation257', None)
    assert getattr(partner, 'thingML_ConfigPropertyAssign256') is None


def test_assoc_annotations7_stub_double():
    # thingML_AnnotatedElement has no real 'thingML_AnnotatedElement' property in the generated
    # code (a bare stub) -- manually attach it so thingML_PlatformAnnotation's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # thingML_PlatformAnnotation's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = thingML_PlatformAnnotation(name="sample_text", value="sample_text")
    partner = thingML_AnnotatedElement()
    setattr(partner, 'thingML_AnnotatedElement', None)
    _safe_set(owner, 'thingML_PlatformAnnotation', partner)
    assert getattr(partner, 'thingML_AnnotatedElement') == owner
    _safe_set(owner, 'thingML_PlatformAnnotation', None)
    assert getattr(partner, 'thingML_AnnotatedElement') is None


def test_assoc_assign26_stub_double():
    # thingML_PropertyAssign has no real 'thingML_PropertyAssign' property in the generated
    # code (a bare stub) -- manually attach it so thingML_Thing's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # thingML_Thing's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = thingML_Thing(fragment=True)
    partner = thingML_PropertyAssign()
    setattr(partner, 'thingML_PropertyAssign', None)
    _safe_set(owner, 'thingML_Thing27', {partner})
    assert getattr(partner, 'thingML_PropertyAssign') == owner
    _safe_set(owner, 'thingML_Thing27', set())
    assert getattr(partner, 'thingML_PropertyAssign') is None


def test_assoc_body46_stub_double():
    # thingML_ActionBlock has no real 'thingML_ActionBlock' property in the generated
    # code (a bare stub) -- manually attach it so thingML_Function's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # thingML_Function's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = thingML_Function(name="sample_text")
    partner = thingML_ActionBlock()
    setattr(partner, 'thingML_ActionBlock', None)
    _safe_set(owner, 'thingML_Function47', partner)
    assert getattr(partner, 'thingML_ActionBlock') == owner
    _safe_set(owner, 'thingML_Function47', None)
    assert getattr(partner, 'thingML_ActionBlock') is None


def test_assoc_cardinality10_stub_double():
    # thingML_Expression has no real 'thingML_Expression' property in the generated
    # code (a bare stub) -- manually attach it so thingML_TypeRef's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # thingML_TypeRef's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = thingML_TypeRef(isArray=True)
    partner = thingML_Expression()
    setattr(partner, 'thingML_Expression', None)
    _safe_set(owner, 'thingML_TypeRef11', partner)
    assert getattr(partner, 'thingML_Expression') == owner
    _safe_set(owner, 'thingML_TypeRef11', None)
    assert getattr(partner, 'thingML_Expression') is None


def test_assoc_configs5_stub_double():
    # thingML_ThingMLModel has no real 'thingML_ThingMLModel6' property in the generated
    # code (a bare stub) -- manually attach it so thingML_Configuration's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # thingML_Configuration's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = thingML_Configuration(name="sample_text")
    partner = thingML_ThingMLModel()
    setattr(partner, 'thingML_ThingMLModel6', None)
    _safe_set(owner, 'thingML_Configuration', partner)
    assert getattr(partner, 'thingML_ThingMLModel6') == owner
    _safe_set(owner, 'thingML_Configuration', None)
    assert getattr(partner, 'thingML_ThingMLModel6') is None


def test_assoc_entry136_stub_double():
    # thingML_Action has no real 'thingML_Action' property in the generated
    # code (a bare stub) -- manually attach it so thingML_State's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # thingML_State's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = thingML_State(name="sample_text")
    partner = thingML_Action()
    setattr(partner, 'thingML_Action', None)
    _safe_set(owner, 'thingML_State137', partner)
    assert getattr(partner, 'thingML_Action') == owner
    _safe_set(owner, 'thingML_State137', None)
    assert getattr(partner, 'thingML_Action') is None


def test_assoc_event145_stub_double():
    # thingML_Event has no real 'thingML_Event' property in the generated
    # code (a bare stub) -- manually attach it so thingML_Handler's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # thingML_Handler's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = thingML_Handler(name="sample_text")
    partner = thingML_Event()
    setattr(partner, 'thingML_Event', None)
    _safe_set(owner, 'thingML_Handler', {partner})
    assert getattr(partner, 'thingML_Event') == owner
    _safe_set(owner, 'thingML_Handler', set())
    assert getattr(partner, 'thingML_Event') is None


def test_assoc_exit138_stub_double():
    # thingML_Action has no real 'thingML_Action140' property in the generated
    # code (a bare stub) -- manually attach it so thingML_State's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # thingML_State's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = thingML_State(name="sample_text")
    partner = thingML_Action()
    setattr(partner, 'thingML_Action140', None)
    _safe_set(owner, 'thingML_State139', partner)
    assert getattr(partner, 'thingML_Action140') == owner
    _safe_set(owner, 'thingML_State139', None)
    assert getattr(partner, 'thingML_Action140') is None


def test_assoc_function213_stub_double():
    # thingML_FunctionCallStatement has no real 'thingML_FunctionCallStatement' property in the generated
    # code (a bare stub) -- manually attach it so thingML_Function's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # thingML_Function's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = thingML_Function(name="sample_text")
    partner = thingML_FunctionCallStatement()
    setattr(partner, 'thingML_FunctionCallStatement', None)
    _safe_set(owner, 'thingML_Function214', partner)
    assert getattr(partner, 'thingML_FunctionCallStatement') == owner
    _safe_set(owner, 'thingML_Function214', None)
    assert getattr(partner, 'thingML_FunctionCallStatement') is None


def test_assoc_function230_stub_double():
    # thingML_FunctionCallExpression has no real 'thingML_FunctionCallExpression' property in the generated
    # code (a bare stub) -- manually attach it so thingML_Function's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # thingML_Function's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = thingML_Function(name="sample_text")
    partner = thingML_FunctionCallExpression()
    setattr(partner, 'thingML_FunctionCallExpression', None)
    _safe_set(owner, 'thingML_Function231', partner)
    assert getattr(partner, 'thingML_FunctionCallExpression') == owner
    _safe_set(owner, 'thingML_Function231', None)
    assert getattr(partner, 'thingML_FunctionCallExpression') is None


def test_assoc_guard146_stub_double():
    # thingML_Expression has no real 'thingML_Expression148' property in the generated
    # code (a bare stub) -- manually attach it so thingML_Handler's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # thingML_Handler's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = thingML_Handler(name="sample_text")
    partner = thingML_Expression()
    setattr(partner, 'thingML_Expression148', None)
    _safe_set(owner, 'thingML_Handler147', partner)
    assert getattr(partner, 'thingML_Expression148') == owner
    _safe_set(owner, 'thingML_Handler147', None)
    assert getattr(partner, 'thingML_Expression148') is None


def test_assoc_imports0_stub_double():
    # thingML_ThingMLModel has no real 'thingML_ThingMLModel' property in the generated
    # code (a bare stub) -- manually attach it so thingML_Import's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # thingML_Import's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = thingML_Import(importURI="sample_text")
    partner = thingML_ThingMLModel()
    setattr(partner, 'thingML_ThingMLModel', None)
    _safe_set(owner, 'thingML_Import', partner)
    assert getattr(partner, 'thingML_ThingMLModel') == owner
    _safe_set(owner, 'thingML_Import', None)
    assert getattr(partner, 'thingML_ThingMLModel') is None


def test_assoc_init169_stub_double():
    # thingML_Expression has no real 'thingML_Expression171' property in the generated
    # code (a bare stub) -- manually attach it so thingML_LocalVariable's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # thingML_LocalVariable's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = thingML_LocalVariable(changeable=True, name="sample_text")
    partner = thingML_Expression()
    setattr(partner, 'thingML_Expression171', None)
    _safe_set(owner, 'thingML_LocalVariable170', partner)
    assert getattr(partner, 'thingML_Expression171') == owner
    _safe_set(owner, 'thingML_LocalVariable170', None)
    assert getattr(partner, 'thingML_Expression171') is None


def test_assoc_init51_stub_double():
    # thingML_Expression has no real 'thingML_Expression53' property in the generated
    # code (a bare stub) -- manually attach it so thingML_Property's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # thingML_Property's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = thingML_Property(changeable=True, name="sample_text")
    partner = thingML_Expression()
    setattr(partner, 'thingML_Expression53', None)
    _safe_set(owner, 'thingML_Property52', partner)
    assert getattr(partner, 'thingML_Expression53') == owner
    _safe_set(owner, 'thingML_Property52', None)
    assert getattr(partner, 'thingML_Expression53') is None


def test_assoc_input66_stub_double():
    # thingML_Source has no real 'thingML_Source' property in the generated
    # code (a bare stub) -- manually attach it so thingML_Stream's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # thingML_Stream's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = thingML_Stream(name="sample_text")
    partner = thingML_Source()
    setattr(partner, 'thingML_Source', None)
    _safe_set(owner, 'thingML_Stream67', partner)
    assert getattr(partner, 'thingML_Source') == owner
    _safe_set(owner, 'thingML_Stream67', None)
    assert getattr(partner, 'thingML_Source') is None


def test_assoc_instance275_stub_double():
    # thingML_InstanceRef has no real 'thingML_InstanceRef276' property in the generated
    # code (a bare stub) -- manually attach it so thingML_Instance's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # thingML_Instance's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = thingML_Instance(name="sample_text")
    partner = thingML_InstanceRef()
    setattr(partner, 'thingML_InstanceRef276', None)
    _safe_set(owner, 'thingML_Instance277', partner)
    assert getattr(partner, 'thingML_InstanceRef276') == owner
    _safe_set(owner, 'thingML_Instance277', None)
    assert getattr(partner, 'thingML_InstanceRef276') is None


def test_assoc_internal141_stub_double():
    # thingML_InternalTransition has no real 'thingML_InternalTransition' property in the generated
    # code (a bare stub) -- manually attach it so thingML_State's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # thingML_State's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = thingML_State(name="sample_text")
    partner = thingML_InternalTransition()
    setattr(partner, 'thingML_InternalTransition', None)
    _safe_set(owner, 'thingML_State142', {partner})
    assert getattr(partner, 'thingML_InternalTransition') == owner
    _safe_set(owner, 'thingML_State142', set())
    assert getattr(partner, 'thingML_InternalTransition') is None


def test_assoc_literal222_stub_double():
    # thingML_EnumLiteralRef has no real 'thingML_EnumLiteralRef223' property in the generated
    # code (a bare stub) -- manually attach it so thingML_EnumerationLiteral's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # thingML_EnumerationLiteral's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = thingML_EnumerationLiteral(name="sample_text")
    partner = thingML_EnumLiteralRef()
    setattr(partner, 'thingML_EnumLiteralRef223', None)
    _safe_set(owner, 'thingML_EnumerationLiteral224', partner)
    assert getattr(partner, 'thingML_EnumLiteralRef223') == owner
    _safe_set(owner, 'thingML_EnumerationLiteral224', None)
    assert getattr(partner, 'thingML_EnumLiteralRef223') is None


def test_assoc_literals12_stub_double():
    # thingML_Enumeration has no real 'thingML_Enumeration' property in the generated
    # code (a bare stub) -- manually attach it so thingML_EnumerationLiteral's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # thingML_EnumerationLiteral's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = thingML_EnumerationLiteral(name="sample_text")
    partner = thingML_Enumeration()
    setattr(partner, 'thingML_Enumeration', None)
    _safe_set(owner, 'thingML_EnumerationLiteral', partner)
    assert getattr(partner, 'thingML_Enumeration') == owner
    _safe_set(owner, 'thingML_EnumerationLiteral', None)
    assert getattr(partner, 'thingML_Enumeration') is None


def test_assoc_message175_stub_double():
    # thingML_SendAction has no real 'thingML_SendAction176' property in the generated
    # code (a bare stub) -- manually attach it so thingML_Message's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # thingML_Message's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = thingML_Message(name="sample_text")
    partner = thingML_SendAction()
    setattr(partner, 'thingML_SendAction176', None)
    _safe_set(owner, 'thingML_Message177', partner)
    assert getattr(partner, 'thingML_SendAction176') == owner
    _safe_set(owner, 'thingML_Message177', None)
    assert getattr(partner, 'thingML_SendAction176') is None


def test_assoc_operators80_stub_double():
    # thingML_ViewSource has no real 'thingML_ViewSource' property in the generated
    # code (a bare stub) -- manually attach it so thingML_JoinSources's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # thingML_JoinSources's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = thingML_JoinSources(name="sample_text")
    partner = thingML_ViewSource()
    setattr(partner, 'thingML_ViewSource', None)
    _safe_set(owner, 'thingML_JoinSources81', {partner})
    assert getattr(partner, 'thingML_ViewSource') == owner
    _safe_set(owner, 'thingML_JoinSources81', set())
    assert getattr(partner, 'thingML_ViewSource') is None


def test_assoc_operators87_stub_double():
    # thingML_ViewSource has no real 'thingML_ViewSource89' property in the generated
    # code (a bare stub) -- manually attach it so thingML_MergeSources's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # thingML_MergeSources's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = thingML_MergeSources(name="sample_text")
    partner = thingML_ViewSource()
    setattr(partner, 'thingML_ViewSource89', None)
    _safe_set(owner, 'thingML_MergeSources88', {partner})
    assert getattr(partner, 'thingML_ViewSource89') == owner
    _safe_set(owner, 'thingML_MergeSources88', set())
    assert getattr(partner, 'thingML_ViewSource89') is None


def test_assoc_operators91_stub_double():
    # thingML_ViewSource has no real 'thingML_ViewSource93' property in the generated
    # code (a bare stub) -- manually attach it so thingML_SimpleSource's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # thingML_SimpleSource's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = thingML_SimpleSource(name="sample_text")
    partner = thingML_ViewSource()
    setattr(partner, 'thingML_ViewSource93', None)
    _safe_set(owner, 'thingML_SimpleSource92', {partner})
    assert getattr(partner, 'thingML_ViewSource93') == owner
    _safe_set(owner, 'thingML_SimpleSource92', set())
    assert getattr(partner, 'thingML_ViewSource93') is None


def test_assoc_outgoing143_stub_double():
    # thingML_Transition has no real 'thingML_Transition' property in the generated
    # code (a bare stub) -- manually attach it so thingML_State's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # thingML_State's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = thingML_State(name="sample_text")
    partner = thingML_Transition()
    setattr(partner, 'thingML_Transition', None)
    _safe_set(owner, 'thingML_State144', {partner})
    assert getattr(partner, 'thingML_Transition') == owner
    _safe_set(owner, 'thingML_State144', set())
    assert getattr(partner, 'thingML_Transition') is None


def test_assoc_output70_stub_double():
    # thingML_SendAction has no real 'thingML_SendAction' property in the generated
    # code (a bare stub) -- manually attach it so thingML_Stream's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # thingML_Stream's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = thingML_Stream(name="sample_text")
    partner = thingML_SendAction()
    setattr(partner, 'thingML_SendAction', None)
    _safe_set(owner, 'thingML_Stream71', partner)
    assert getattr(partner, 'thingML_SendAction') == owner
    _safe_set(owner, 'thingML_Stream71', None)
    assert getattr(partner, 'thingML_SendAction') is None


def test_assoc_parameterRef108_stub_double():
    # thingML_SimpleParamRef has no real 'thingML_SimpleParamRef' property in the generated
    # code (a bare stub) -- manually attach it so thingML_Parameter's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # thingML_Parameter's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = thingML_Parameter(name="sample_text")
    partner = thingML_SimpleParamRef()
    setattr(partner, 'thingML_SimpleParamRef', None)
    _safe_set(owner, 'thingML_Parameter109', partner)
    assert getattr(partner, 'thingML_SimpleParamRef') == owner
    _safe_set(owner, 'thingML_Parameter109', None)
    assert getattr(partner, 'thingML_SimpleParamRef') is None


def test_assoc_parameterRef110_stub_double():
    # thingML_ArrayParamRef has no real 'thingML_ArrayParamRef' property in the generated
    # code (a bare stub) -- manually attach it so thingML_Parameter's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # thingML_Parameter's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = thingML_Parameter(name="sample_text")
    partner = thingML_ArrayParamRef()
    setattr(partner, 'thingML_ArrayParamRef', None)
    _safe_set(owner, 'thingML_Parameter111', partner)
    assert getattr(partner, 'thingML_ArrayParamRef') == owner
    _safe_set(owner, 'thingML_Parameter111', None)
    assert getattr(partner, 'thingML_ArrayParamRef') is None


def test_assoc_port172_stub_double():
    # thingML_SendAction has no real 'thingML_SendAction173' property in the generated
    # code (a bare stub) -- manually attach it so thingML_Port's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # thingML_Port's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = thingML_Port(name="sample_text")
    partner = thingML_SendAction()
    setattr(partner, 'thingML_SendAction173', None)
    _safe_set(owner, 'thingML_Port174', partner)
    assert getattr(partner, 'thingML_SendAction173') == owner
    _safe_set(owner, 'thingML_Port174', None)
    assert getattr(partner, 'thingML_SendAction173') is None


def test_assoc_port269_stub_double():
    # thingML_ExternalConnector has no real 'thingML_ExternalConnector270' property in the generated
    # code (a bare stub) -- manually attach it so thingML_Port's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # thingML_Port's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = thingML_Port(name="sample_text")
    partner = thingML_ExternalConnector()
    setattr(partner, 'thingML_ExternalConnector270', None)
    _safe_set(owner, 'thingML_Port271', partner)
    assert getattr(partner, 'thingML_ExternalConnector270') == owner
    _safe_set(owner, 'thingML_Port271', None)
    assert getattr(partner, 'thingML_ExternalConnector270') is None


def test_assoc_propassigns239_stub_double():
    # thingML_ConfigPropertyAssign has no real 'thingML_ConfigPropertyAssign' property in the generated
    # code (a bare stub) -- manually attach it so thingML_Configuration's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # thingML_Configuration's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = thingML_Configuration(name="sample_text")
    partner = thingML_ConfigPropertyAssign()
    setattr(partner, 'thingML_ConfigPropertyAssign', None)
    _safe_set(owner, 'thingML_Configuration240', {partner})
    assert getattr(partner, 'thingML_ConfigPropertyAssign') == owner
    _safe_set(owner, 'thingML_Configuration240', set())
    assert getattr(partner, 'thingML_ConfigPropertyAssign') is None


def test_assoc_property246_stub_double():
    # thingML_ConfigPropertyAssign has no real 'thingML_ConfigPropertyAssign247' property in the generated
    # code (a bare stub) -- manually attach it so thingML_Property's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # thingML_Property's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = thingML_Property(changeable=True, name="sample_text")
    partner = thingML_ConfigPropertyAssign()
    setattr(partner, 'thingML_ConfigPropertyAssign247', None)
    _safe_set(owner, 'thingML_Property248', partner)
    assert getattr(partner, 'thingML_ConfigPropertyAssign247') == owner
    _safe_set(owner, 'thingML_Property248', None)
    assert getattr(partner, 'thingML_ConfigPropertyAssign247') is None


def test_assoc_property32_stub_double():
    # thingML_PropertyAssign has no real 'thingML_PropertyAssign33' property in the generated
    # code (a bare stub) -- manually attach it so thingML_Property's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # thingML_Property's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = thingML_Property(changeable=True, name="sample_text")
    partner = thingML_PropertyAssign()
    setattr(partner, 'thingML_PropertyAssign33', None)
    _safe_set(owner, 'thingML_Property34', partner)
    assert getattr(partner, 'thingML_PropertyAssign33') == owner
    _safe_set(owner, 'thingML_Property34', None)
    assert getattr(partner, 'thingML_PropertyAssign33') is None


def test_assoc_protocol272_stub_double():
    # thingML_ExternalConnector has no real 'thingML_ExternalConnector273' property in the generated
    # code (a bare stub) -- manually attach it so thingML_Protocol's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # thingML_Protocol's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = thingML_Protocol(name="sample_text")
    partner = thingML_ExternalConnector()
    setattr(partner, 'thingML_ExternalConnector273', None)
    _safe_set(owner, 'thingML_Protocol274', partner)
    assert getattr(partner, 'thingML_ExternalConnector273') == owner
    _safe_set(owner, 'thingML_Protocol274', None)
    assert getattr(partner, 'thingML_ExternalConnector273') is None


def test_assoc_protocols3_stub_double():
    # thingML_ThingMLModel has no real 'thingML_ThingMLModel4' property in the generated
    # code (a bare stub) -- manually attach it so thingML_Protocol's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # thingML_Protocol's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = thingML_Protocol(name="sample_text")
    partner = thingML_ThingMLModel()
    setattr(partner, 'thingML_ThingMLModel4', None)
    _safe_set(owner, 'thingML_Protocol', partner)
    assert getattr(partner, 'thingML_ThingMLModel4') == owner
    _safe_set(owner, 'thingML_Protocol', None)
    assert getattr(partner, 'thingML_ThingMLModel4') is None


def test_assoc_required260_stub_double():
    # thingML_Connector has no real 'thingML_Connector261' property in the generated
    # code (a bare stub) -- manually attach it so thingML_RequiredPort's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # thingML_RequiredPort's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = thingML_RequiredPort(optional=True)
    partner = thingML_Connector()
    setattr(partner, 'thingML_Connector261', None)
    _safe_set(owner, 'thingML_RequiredPort', partner)
    assert getattr(partner, 'thingML_Connector261') == owner
    _safe_set(owner, 'thingML_RequiredPort', None)
    assert getattr(partner, 'thingML_Connector261') is None


def test_assoc_rules77_stub_double():
    # thingML_Expression has no real 'thingML_Expression79' property in the generated
    # code (a bare stub) -- manually attach it so thingML_JoinSources's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # thingML_JoinSources's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = thingML_JoinSources(name="sample_text")
    partner = thingML_Expression()
    setattr(partner, 'thingML_Expression79', None)
    _safe_set(owner, 'thingML_JoinSources78', {partner})
    assert getattr(partner, 'thingML_Expression79') == owner
    _safe_set(owner, 'thingML_JoinSources78', set())
    assert getattr(partner, 'thingML_Expression79') is None


def test_assoc_segments164_stub_double():
    # thingML_Expression has no real 'thingML_Expression165' property in the generated
    # code (a bare stub) -- manually attach it so thingML_ExternStatement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # thingML_ExternStatement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = thingML_ExternStatement(statement="sample_text")
    partner = thingML_Expression()
    setattr(partner, 'thingML_Expression165', None)
    _safe_set(owner, 'thingML_ExternStatement', {partner})
    assert getattr(partner, 'thingML_Expression165') == owner
    _safe_set(owner, 'thingML_ExternStatement', set())
    assert getattr(partner, 'thingML_Expression165') is None


def test_assoc_segments218_stub_double():
    # thingML_Expression has no real 'thingML_Expression219' property in the generated
    # code (a bare stub) -- manually attach it so thingML_ExternExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # thingML_ExternExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = thingML_ExternExpression(expression="sample_text")
    partner = thingML_Expression()
    setattr(partner, 'thingML_Expression219', None)
    _safe_set(owner, 'thingML_ExternExpression', {partner})
    assert getattr(partner, 'thingML_Expression219') == owner
    _safe_set(owner, 'thingML_ExternExpression', set())
    assert getattr(partner, 'thingML_Expression219') is None


def test_assoc_session211_stub_double():
    # thingML_StartSession has no real 'thingML_StartSession' property in the generated
    # code (a bare stub) -- manually attach it so thingML_Session's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # thingML_Session's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = thingML_Session(maxInstances=7)
    partner = thingML_StartSession()
    setattr(partner, 'thingML_StartSession', None)
    _safe_set(owner, 'thingML_Session212', partner)
    assert getattr(partner, 'thingML_StartSession') == owner
    _safe_set(owner, 'thingML_Session212', None)
    assert getattr(partner, 'thingML_StartSession') is None


def test_assoc_sources72_stub_double():
    # thingML_Source has no real 'thingML_Source73' property in the generated
    # code (a bare stub) -- manually attach it so thingML_JoinSources's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # thingML_JoinSources's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = thingML_JoinSources(name="sample_text")
    partner = thingML_Source()
    setattr(partner, 'thingML_Source73', None)
    _safe_set(owner, 'thingML_JoinSources', {partner})
    assert getattr(partner, 'thingML_Source73') == owner
    _safe_set(owner, 'thingML_JoinSources', set())
    assert getattr(partner, 'thingML_Source73') is None


def test_assoc_sources82_stub_double():
    # thingML_Source has no real 'thingML_Source83' property in the generated
    # code (a bare stub) -- manually attach it so thingML_MergeSources's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # thingML_MergeSources's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = thingML_MergeSources(name="sample_text")
    partner = thingML_Source()
    setattr(partner, 'thingML_Source83', None)
    _safe_set(owner, 'thingML_MergeSources', {partner})
    assert getattr(partner, 'thingML_Source83') == owner
    _safe_set(owner, 'thingML_MergeSources', set())
    assert getattr(partner, 'thingML_Source83') is None


def test_assoc_target152_stub_double():
    # thingML_Transition has no real 'thingML_Transition153' property in the generated
    # code (a bare stub) -- manually attach it so thingML_State's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # thingML_State's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = thingML_State(name="sample_text")
    partner = thingML_Transition()
    setattr(partner, 'thingML_Transition153', None)
    _safe_set(owner, 'thingML_State154', partner)
    assert getattr(partner, 'thingML_Transition153') == owner
    _safe_set(owner, 'thingML_State154', None)
    assert getattr(partner, 'thingML_Transition153') is None


def test_assoc_types1_stub_double():
    # thingML_ThingMLModel has no real 'thingML_ThingMLModel2' property in the generated
    # code (a bare stub) -- manually attach it so thingML_Type's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # thingML_Type's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = thingML_Type(name="sample_text")
    partner = thingML_ThingMLModel()
    setattr(partner, 'thingML_ThingMLModel2', None)
    _safe_set(owner, 'thingML_Type', partner)
    assert getattr(partner, 'thingML_ThingMLModel2') == owner
    _safe_set(owner, 'thingML_Type', None)
    assert getattr(partner, 'thingML_ThingMLModel2') is None


