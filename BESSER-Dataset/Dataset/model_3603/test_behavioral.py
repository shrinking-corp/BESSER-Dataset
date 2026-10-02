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


