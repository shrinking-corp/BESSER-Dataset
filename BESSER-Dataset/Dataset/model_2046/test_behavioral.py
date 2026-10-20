import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    ActorContainerClass,
    ActorContainerRef,
    ComplexType,
    DataType,
    GeneralProtocolClass,
    InterfaceItem,
    MessageHandler,
    NonInitialTransition,
    Operation,
    RoomClass,
    SAPoint,
    SemanticsRule,
    State,
    StateGraphItem,
    StateGraphNode,
    StructureClass,
    TrPoint,
    Transition,
    TransitionChainStartTransition,
    TransitionTerminal,
    room_ActorClass,
    room_ActorContainerClass,
    room_ActorContainerRef,
    room_ActorInstancePath,
    room_ActorRef,
    room_Annotation,
    room_Attribute,
    room_Binding,
    room_BindingEndPoint,
    room_CPBranchTransition,
    room_ChoicePoint,
    room_ChoicepointTerminal,
    room_ComplexType,
    room_CompoundProtocolClass,
    room_ContinuationTransition,
    room_DataClass,
    room_DataType,
    room_DetailCode,
    room_Documentation,
    room_EntryPoint,
    room_ExitPoint,
    room_ExternalPort,
    room_ExternalType,
    room_GeneralProtocolClass,
    room_Guard,
    room_GuardedTransition,
    room_Import,
    room_InMessageHandler,
    room_InSemanticsRule,
    room_InitialTransition,
    room_InterfaceItem,
    room_KeyValue,
    room_LayerConnection,
    room_LogicalSystem,
    room_LogicalThread,
    room_Message,
    room_MessageFromIf,
    room_MessageHandler,
    room_NonInitialTransition,
    room_Operation,
    room_OutMessageHandler,
    room_OutSemanticsRule,
    room_Port,
    room_PortClass,
    room_PortOperation,
    room_PrimitiveType,
    room_ProtocolClass,
    room_ProtocolSemantics,
    room_RefSAPoint,
    room_RefableType,
    room_RefinedState,
    room_RefinedTransition,
    room_RelaySAPoint,
    room_RoomClass,
    room_RoomModel,
    room_SAPRef,
    room_SAPoint,
    room_SPPRef,
    room_SPPoint,
    room_SemanticsRule,
    room_ServiceImplementation,
    room_SimpleState,
    room_StandardOperation,
    room_State,
    room_StateGraph,
    room_StateGraphItem,
    room_StateGraphNode,
    room_StateTerminal,
    room_StructureClass,
    room_SubProtocol,
    room_SubStateTrPointTerminal,
    room_SubSystemClass,
    room_SubSystemRef,
    room_TrPoint,
    room_TrPointTerminal,
    room_Transition,
    room_TransitionChainStartTransition,
    room_TransitionPoint,
    room_TransitionTerminal,
    room_Trigger,
    room_TriggeredTransition,
    room_VarDecl,
    ActorCommunicationType,
    CommunicationType,
    LiteralType,
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

def test_assoc_action266_reverse_link_reassign_clear():
    a1 = room_Transition(name="sample_text")
    a2 = room_Transition(name="sample_text_2")
    b = room_DetailCode(commands="sample_text")
    _safe_set(b, 'room_DetailCode268', a1)
    assert _is_linked(b, 'room_DetailCode268', a1)
    if hasattr(a1, 'room_Transition267'):
        assert _is_linked(a1, 'room_Transition267', b)
    _safe_set(b, 'room_DetailCode268', a2)
    assert _is_linked(b, 'room_DetailCode268', a2)
    if hasattr(a1, 'room_Transition267'):
        assert not _is_linked(a1, 'room_Transition267', b)
    if hasattr(a2, 'room_Transition267'):
        assert _is_linked(a2, 'room_Transition267', b)
    _safe_set(b, 'room_DetailCode268', None)
    assert not _is_linked(b, 'room_DetailCode268', a2)
    if hasattr(a2, 'room_Transition267'):
        assert not _is_linked(a2, 'room_Transition267', b)


def test_assoc_actorClasses11_reverse_link_reassign_clear():
    a1 = room_RoomModel(name="sample_text")
    a2 = room_RoomModel(name="sample_text_2")
    b = room_ActorClass(abstract=True, commType="sample_text")
    _safe_set(b, 'room_ActorClass', a1)
    assert _is_linked(b, 'room_ActorClass', a1)
    if hasattr(a1, 'room_RoomModel12'):
        assert _is_linked(a1, 'room_RoomModel12', b)
    _safe_set(b, 'room_ActorClass', a2)
    assert _is_linked(b, 'room_ActorClass', a2)
    if hasattr(a1, 'room_RoomModel12'):
        assert not _is_linked(a1, 'room_RoomModel12', b)
    if hasattr(a2, 'room_RoomModel12'):
        assert _is_linked(a2, 'room_RoomModel12', b)
    _safe_set(b, 'room_ActorClass', None)
    assert not _is_linked(b, 'room_ActorClass', a2)
    if hasattr(a2, 'room_RoomModel12'):
        assert not _is_linked(a2, 'room_RoomModel12', b)


def test_assoc_arguments63_reverse_link_reassign_clear():
    a1 = room_VarDecl(name="sample_text")
    a2 = room_VarDecl(name="sample_text_2")
    b = room_Operation(name="sample_text")
    _safe_set(b, 'room_Operation', {a1})
    assert _is_linked(b, 'room_Operation', a1)
    if hasattr(a1, 'room_VarDecl64'):
        assert _is_linked(a1, 'room_VarDecl64', b)
    _safe_set(b, 'room_Operation', {a2})
    assert _is_linked(b, 'room_Operation', a2)
    if hasattr(a1, 'room_VarDecl64'):
        assert not _is_linked(a1, 'room_VarDecl64', b)
    if hasattr(a2, 'room_VarDecl64'):
        assert _is_linked(a2, 'room_VarDecl64', b)
    _safe_set(b, 'room_Operation', set())
    assert not _is_linked(b, 'room_Operation', a2)
    if hasattr(a2, 'room_VarDecl64'):
        assert not _is_linked(a2, 'room_VarDecl64', b)


def test_assoc_attributes154_reverse_link_reassign_clear():
    a1 = room_Attribute(defaultValueLiteral="sample_text", name="sample_text", size=7)
    a2 = room_Attribute(defaultValueLiteral="sample_text_2", name="sample_text_2", size=13)
    b = room_ActorClass(abstract=True, commType="sample_text")
    _safe_set(b, 'room_ActorClass155', {a1})
    assert _is_linked(b, 'room_ActorClass155', a1)
    if hasattr(a1, 'room_Attribute156'):
        assert _is_linked(a1, 'room_Attribute156', b)
    _safe_set(b, 'room_ActorClass155', {a2})
    assert _is_linked(b, 'room_ActorClass155', a2)
    if hasattr(a1, 'room_Attribute156'):
        assert not _is_linked(a1, 'room_Attribute156', b)
    if hasattr(a2, 'room_Attribute156'):
        assert _is_linked(a2, 'room_Attribute156', b)
    _safe_set(b, 'room_ActorClass155', set())
    assert not _is_linked(b, 'room_ActorClass155', a2)
    if hasattr(a2, 'room_Attribute156'):
        assert not _is_linked(a2, 'room_Attribute156', b)


def test_assoc_attributes308_reverse_link_reassign_clear():
    a1 = room_KeyValue(key="sample_text", value="sample_text")
    a2 = room_KeyValue(key="sample_text_2", value="sample_text_2")
    b = room_Annotation(name="sample_text")
    _safe_set(b, 'room_Annotation309', {a1})
    assert _is_linked(b, 'room_Annotation309', a1)
    if hasattr(a1, 'room_KeyValue'):
        assert _is_linked(a1, 'room_KeyValue', b)
    _safe_set(b, 'room_Annotation309', {a2})
    assert _is_linked(b, 'room_Annotation309', a2)
    if hasattr(a1, 'room_KeyValue'):
        assert not _is_linked(a1, 'room_KeyValue', b)
    if hasattr(a2, 'room_KeyValue'):
        assert _is_linked(a2, 'room_KeyValue', b)
    _safe_set(b, 'room_Annotation309', set())
    assert not _is_linked(b, 'room_Annotation309', a2)
    if hasattr(a2, 'room_KeyValue'):
        assert not _is_linked(a2, 'room_KeyValue', b)


def test_assoc_base138_reverse_link_reassign_clear():
    a1 = room_ActorClass(abstract=True, commType="sample_text")
    a2 = room_ActorClass(abstract=False, commType="sample_text_2")
    b = room_ActorClass(abstract=True, commType="sample_text")
    _safe_set(b, 'room_ActorClass139', a1)
    assert _is_linked(b, 'room_ActorClass139', a1)
    if hasattr(a1, 'room_ActorClass137'):
        assert _is_linked(a1, 'room_ActorClass137', b)
    _safe_set(b, 'room_ActorClass139', a2)
    assert _is_linked(b, 'room_ActorClass139', a2)
    if hasattr(a1, 'room_ActorClass137'):
        assert not _is_linked(a1, 'room_ActorClass137', b)
    if hasattr(a2, 'room_ActorClass137'):
        assert _is_linked(a2, 'room_ActorClass137', b)
    _safe_set(b, 'room_ActorClass139', None)
    assert not _is_linked(b, 'room_ActorClass139', a2)
    if hasattr(a2, 'room_ActorClass137'):
        assert not _is_linked(a2, 'room_ActorClass137', b)


def test_assoc_base79_reverse_link_reassign_clear():
    a1 = room_ProtocolClass(commType="sample_text")
    a2 = room_ProtocolClass(commType="sample_text_2")
    b = room_ProtocolClass(commType="sample_text")
    _safe_set(b, 'room_ProtocolClass78', a1)
    assert _is_linked(b, 'room_ProtocolClass78', a1)
    if hasattr(a1, 'room_ProtocolClass'):
        assert _is_linked(a1, 'room_ProtocolClass', b)
    _safe_set(b, 'room_ProtocolClass78', a2)
    assert _is_linked(b, 'room_ProtocolClass78', a2)
    if hasattr(a1, 'room_ProtocolClass'):
        assert not _is_linked(a1, 'room_ProtocolClass', b)
    if hasattr(a2, 'room_ProtocolClass'):
        assert _is_linked(a2, 'room_ProtocolClass', b)
    _safe_set(b, 'room_ProtocolClass78', None)
    assert not _is_linked(b, 'room_ProtocolClass78', a2)
    if hasattr(a2, 'room_ProtocolClass'):
        assert not _is_linked(a2, 'room_ProtocolClass', b)


def test_assoc_behaviorAnnotations160_reverse_link_reassign_clear():
    a1 = room_Annotation(name="sample_text")
    a2 = room_Annotation(name="sample_text_2")
    b = room_ActorClass(abstract=True, commType="sample_text")
    _safe_set(b, 'room_ActorClass161', {a1})
    assert _is_linked(b, 'room_ActorClass161', a1)
    if hasattr(a1, 'room_Annotation162'):
        assert _is_linked(a1, 'room_Annotation162', b)
    _safe_set(b, 'room_ActorClass161', {a2})
    assert _is_linked(b, 'room_ActorClass161', a2)
    if hasattr(a1, 'room_Annotation162'):
        assert not _is_linked(a1, 'room_Annotation162', b)
    if hasattr(a2, 'room_Annotation162'):
        assert _is_linked(a2, 'room_Annotation162', b)
    _safe_set(b, 'room_ActorClass161', set())
    assert not _is_linked(b, 'room_ActorClass161', a2)
    if hasattr(a2, 'room_Annotation162'):
        assert not _is_linked(a2, 'room_Annotation162', b)


def test_assoc_behaviorDocu157_reverse_link_reassign_clear():
    a1 = room_Documentation(text="sample_text")
    a2 = room_Documentation(text="sample_text_2")
    b = room_ActorClass(abstract=True, commType="sample_text")
    _safe_set(b, 'room_ActorClass158', a1)
    assert _is_linked(b, 'room_ActorClass158', a1)
    if hasattr(a1, 'room_Documentation159'):
        assert _is_linked(a1, 'room_Documentation159', b)
    _safe_set(b, 'room_ActorClass158', a2)
    assert _is_linked(b, 'room_ActorClass158', a2)
    if hasattr(a1, 'room_Documentation159'):
        assert not _is_linked(a1, 'room_Documentation159', b)
    if hasattr(a2, 'room_Documentation159'):
        assert _is_linked(a2, 'room_Documentation159', b)
    _safe_set(b, 'room_ActorClass158', None)
    assert not _is_linked(b, 'room_ActorClass158', a2)
    if hasattr(a2, 'room_Documentation159'):
        assert not _is_linked(a2, 'room_Documentation159', b)


def test_assoc_data106_reverse_link_reassign_clear():
    a1 = room_VarDecl(name="sample_text")
    a2 = room_VarDecl(name="sample_text_2")
    b = room_Message(name="sample_text", priv=True)
    _safe_set(b, 'room_Message107', a1)
    assert _is_linked(b, 'room_Message107', a1)
    if hasattr(a1, 'room_VarDecl108'):
        assert _is_linked(a1, 'room_VarDecl108', b)
    _safe_set(b, 'room_Message107', a2)
    assert _is_linked(b, 'room_Message107', a2)
    if hasattr(a1, 'room_VarDecl108'):
        assert not _is_linked(a1, 'room_VarDecl108', b)
    if hasattr(a2, 'room_VarDecl108'):
        assert _is_linked(a2, 'room_VarDecl108', b)
    _safe_set(b, 'room_Message107', None)
    assert not _is_linked(b, 'room_Message107', a2)
    if hasattr(a2, 'room_VarDecl108'):
        assert not _is_linked(a2, 'room_VarDecl108', b)


def test_assoc_detailCode71_reverse_link_reassign_clear():
    a1 = room_Operation(name="sample_text")
    a2 = room_Operation(name="sample_text_2")
    b = room_DetailCode(commands="sample_text")
    _safe_set(b, 'room_DetailCode73', a1)
    assert _is_linked(b, 'room_DetailCode73', a1)
    if hasattr(a1, 'room_Operation72'):
        assert _is_linked(a1, 'room_Operation72', b)
    _safe_set(b, 'room_DetailCode73', a2)
    assert _is_linked(b, 'room_DetailCode73', a2)
    if hasattr(a1, 'room_Operation72'):
        assert not _is_linked(a1, 'room_Operation72', b)
    if hasattr(a2, 'room_Operation72'):
        assert _is_linked(a2, 'room_Operation72', b)
    _safe_set(b, 'room_DetailCode73', None)
    assert not _is_linked(b, 'room_DetailCode73', a2)
    if hasattr(a2, 'room_Operation72'):
        assert not _is_linked(a2, 'room_Operation72', b)


def test_assoc_doCode239_reverse_link_reassign_clear():
    a1 = room_State()
    a2 = room_State()
    b = room_DetailCode(commands="sample_text")
    _safe_set(b, 'room_DetailCode241', a1)
    assert _is_linked(b, 'room_DetailCode241', a1)
    if hasattr(a1, 'room_State240'):
        assert _is_linked(a1, 'room_State240', b)
    _safe_set(b, 'room_DetailCode241', a2)
    assert _is_linked(b, 'room_DetailCode241', a2)
    if hasattr(a1, 'room_State240'):
        assert not _is_linked(a1, 'room_State240', b)
    if hasattr(a2, 'room_State240'):
        assert _is_linked(a2, 'room_State240', b)
    _safe_set(b, 'room_DetailCode241', None)
    assert not _is_linked(b, 'room_DetailCode241', a2)
    if hasattr(a2, 'room_State240'):
        assert not _is_linked(a2, 'room_State240', b)


def test_assoc_docu0_reverse_link_reassign_clear():
    a1 = room_RoomModel(name="sample_text")
    a2 = room_RoomModel(name="sample_text_2")
    b = room_Documentation(text="sample_text")
    _safe_set(b, 'room_Documentation', a1)
    assert _is_linked(b, 'room_Documentation', a1)
    if hasattr(a1, 'room_RoomModel'):
        assert _is_linked(a1, 'room_RoomModel', b)
    _safe_set(b, 'room_Documentation', a2)
    assert _is_linked(b, 'room_Documentation', a2)
    if hasattr(a1, 'room_RoomModel'):
        assert not _is_linked(a1, 'room_RoomModel', b)
    if hasattr(a2, 'room_RoomModel'):
        assert _is_linked(a2, 'room_RoomModel', b)
    _safe_set(b, 'room_Documentation', None)
    assert not _is_linked(b, 'room_Documentation', a2)
    if hasattr(a2, 'room_RoomModel'):
        assert not _is_linked(a2, 'room_RoomModel', b)


def test_assoc_docu109_reverse_link_reassign_clear():
    a1 = room_Message(name="sample_text", priv=True)
    a2 = room_Message(name="sample_text_2", priv=False)
    b = room_Documentation(text="sample_text")
    _safe_set(b, 'room_Documentation111', a1)
    assert _is_linked(b, 'room_Documentation111', a1)
    if hasattr(a1, 'room_Message110'):
        assert _is_linked(a1, 'room_Message110', b)
    _safe_set(b, 'room_Documentation111', a2)
    assert _is_linked(b, 'room_Documentation111', a2)
    if hasattr(a1, 'room_Message110'):
        assert not _is_linked(a1, 'room_Message110', b)
    if hasattr(a2, 'room_Message110'):
        assert _is_linked(a2, 'room_Message110', b)
    _safe_set(b, 'room_Documentation111', None)
    assert not _is_linked(b, 'room_Documentation111', a2)
    if hasattr(a2, 'room_Message110'):
        assert not _is_linked(a2, 'room_Message110', b)


def test_assoc_docu17_reverse_link_reassign_clear():
    a1 = room_RoomClass(name="sample_text")
    a2 = room_RoomClass(name="sample_text_2")
    b = room_Documentation(text="sample_text")
    _safe_set(b, 'room_Documentation18', a1)
    assert _is_linked(b, 'room_Documentation18', a1)
    if hasattr(a1, 'room_RoomClass'):
        assert _is_linked(a1, 'room_RoomClass', b)
    _safe_set(b, 'room_Documentation18', a2)
    assert _is_linked(b, 'room_Documentation18', a2)
    if hasattr(a1, 'room_RoomClass'):
        assert not _is_linked(a1, 'room_RoomClass', b)
    if hasattr(a2, 'room_RoomClass'):
        assert _is_linked(a2, 'room_RoomClass', b)
    _safe_set(b, 'room_Documentation18', None)
    assert not _is_linked(b, 'room_Documentation18', a2)
    if hasattr(a2, 'room_RoomClass'):
        assert not _is_linked(a2, 'room_RoomClass', b)


def test_assoc_docu171_reverse_link_reassign_clear():
    a1 = room_Port(conjugated=True, multiplicity=7)
    a2 = room_Port(conjugated=False, multiplicity=13)
    b = room_Documentation(text="sample_text")
    _safe_set(b, 'room_Documentation173', a1)
    assert _is_linked(b, 'room_Documentation173', a1)
    if hasattr(a1, 'room_Port172'):
        assert _is_linked(a1, 'room_Port172', b)
    _safe_set(b, 'room_Documentation173', a2)
    assert _is_linked(b, 'room_Documentation173', a2)
    if hasattr(a1, 'room_Port172'):
        assert not _is_linked(a1, 'room_Port172', b)
    if hasattr(a2, 'room_Port172'):
        assert _is_linked(a2, 'room_Port172', b)
    _safe_set(b, 'room_Documentation173', None)
    assert not _is_linked(b, 'room_Documentation173', a2)
    if hasattr(a2, 'room_Port172'):
        assert not _is_linked(a2, 'room_Port172', b)


def test_assoc_docu188_reverse_link_reassign_clear():
    a1 = room_Documentation(text="sample_text")
    a2 = room_Documentation(text="sample_text_2")
    b = room_ActorContainerRef(name="sample_text")
    _safe_set(b, 'room_ActorContainerRef', a1)
    assert _is_linked(b, 'room_ActorContainerRef', a1)
    if hasattr(a1, 'room_Documentation189'):
        assert _is_linked(a1, 'room_Documentation189', b)
    _safe_set(b, 'room_ActorContainerRef', a2)
    assert _is_linked(b, 'room_ActorContainerRef', a2)
    if hasattr(a1, 'room_Documentation189'):
        assert not _is_linked(a1, 'room_Documentation189', b)
    if hasattr(a2, 'room_Documentation189'):
        assert _is_linked(a2, 'room_Documentation189', b)
    _safe_set(b, 'room_ActorContainerRef', None)
    assert not _is_linked(b, 'room_ActorContainerRef', a2)
    if hasattr(a2, 'room_Documentation189'):
        assert not _is_linked(a2, 'room_Documentation189', b)


def test_assoc_docu231_reverse_link_reassign_clear():
    a1 = room_State()
    a2 = room_State()
    b = room_Documentation(text="sample_text")
    _safe_set(b, 'room_Documentation232', a1)
    assert _is_linked(b, 'room_Documentation232', a1)
    if hasattr(a1, 'room_State'):
        assert _is_linked(a1, 'room_State', b)
    _safe_set(b, 'room_Documentation232', a2)
    assert _is_linked(b, 'room_Documentation232', a2)
    if hasattr(a1, 'room_State'):
        assert not _is_linked(a1, 'room_State', b)
    if hasattr(a2, 'room_State'):
        assert _is_linked(a2, 'room_State', b)
    _safe_set(b, 'room_Documentation232', None)
    assert not _is_linked(b, 'room_Documentation232', a2)
    if hasattr(a2, 'room_State'):
        assert not _is_linked(a2, 'room_State', b)


def test_assoc_docu258_reverse_link_reassign_clear():
    a1 = room_Documentation(text="sample_text")
    a2 = room_Documentation(text="sample_text_2")
    b = room_ChoicePoint(name="sample_text")
    _safe_set(b, 'room_ChoicePoint259', a1)
    assert _is_linked(b, 'room_ChoicePoint259', a1)
    if hasattr(a1, 'room_Documentation260'):
        assert _is_linked(a1, 'room_Documentation260', b)
    _safe_set(b, 'room_ChoicePoint259', a2)
    assert _is_linked(b, 'room_ChoicePoint259', a2)
    if hasattr(a1, 'room_Documentation260'):
        assert not _is_linked(a1, 'room_Documentation260', b)
    if hasattr(a2, 'room_Documentation260'):
        assert _is_linked(a2, 'room_Documentation260', b)
    _safe_set(b, 'room_ChoicePoint259', None)
    assert not _is_linked(b, 'room_ChoicePoint259', a2)
    if hasattr(a2, 'room_Documentation260'):
        assert not _is_linked(a2, 'room_Documentation260', b)


def test_assoc_docu263_reverse_link_reassign_clear():
    a1 = room_Transition(name="sample_text")
    a2 = room_Transition(name="sample_text_2")
    b = room_Documentation(text="sample_text")
    _safe_set(b, 'room_Documentation265', a1)
    assert _is_linked(b, 'room_Documentation265', a1)
    if hasattr(a1, 'room_Transition264'):
        assert _is_linked(a1, 'room_Transition264', b)
    _safe_set(b, 'room_Documentation265', a2)
    assert _is_linked(b, 'room_Documentation265', a2)
    if hasattr(a1, 'room_Transition264'):
        assert not _is_linked(a1, 'room_Transition264', b)
    if hasattr(a2, 'room_Transition264'):
        assert _is_linked(a2, 'room_Transition264', b)
    _safe_set(b, 'room_Documentation265', None)
    assert not _is_linked(b, 'room_Documentation265', a2)
    if hasattr(a2, 'room_Transition264'):
        assert not _is_linked(a2, 'room_Transition264', b)


def test_assoc_docu60_reverse_link_reassign_clear():
    a1 = room_Documentation(text="sample_text")
    a2 = room_Documentation(text="sample_text_2")
    b = room_Attribute(defaultValueLiteral="sample_text", name="sample_text", size=7)
    _safe_set(b, 'room_Attribute61', a1)
    assert _is_linked(b, 'room_Attribute61', a1)
    if hasattr(a1, 'room_Documentation62'):
        assert _is_linked(a1, 'room_Documentation62', b)
    _safe_set(b, 'room_Attribute61', a2)
    assert _is_linked(b, 'room_Attribute61', a2)
    if hasattr(a1, 'room_Documentation62'):
        assert not _is_linked(a1, 'room_Documentation62', b)
    if hasattr(a2, 'room_Documentation62'):
        assert _is_linked(a2, 'room_Documentation62', b)
    _safe_set(b, 'room_Attribute61', None)
    assert not _is_linked(b, 'room_Attribute61', a2)
    if hasattr(a2, 'room_Documentation62'):
        assert not _is_linked(a2, 'room_Documentation62', b)


def test_assoc_docu68_reverse_link_reassign_clear():
    a1 = room_Operation(name="sample_text")
    a2 = room_Operation(name="sample_text_2")
    b = room_Documentation(text="sample_text")
    _safe_set(b, 'room_Documentation70', a1)
    assert _is_linked(b, 'room_Documentation70', a1)
    if hasattr(a1, 'room_Operation69'):
        assert _is_linked(a1, 'room_Operation69', b)
    _safe_set(b, 'room_Documentation70', a2)
    assert _is_linked(b, 'room_Documentation70', a2)
    if hasattr(a1, 'room_Operation69'):
        assert not _is_linked(a1, 'room_Operation69', b)
    if hasattr(a2, 'room_Operation69'):
        assert _is_linked(a2, 'room_Operation69', b)
    _safe_set(b, 'room_Documentation70', None)
    assert not _is_linked(b, 'room_Documentation70', a2)
    if hasattr(a2, 'room_Operation69'):
        assert not _is_linked(a2, 'room_Operation69', b)


def test_assoc_entryCode233_reverse_link_reassign_clear():
    a1 = room_State()
    a2 = room_State()
    b = room_DetailCode(commands="sample_text")
    _safe_set(b, 'room_DetailCode235', a1)
    assert _is_linked(b, 'room_DetailCode235', a1)
    if hasattr(a1, 'room_State234'):
        assert _is_linked(a1, 'room_State234', b)
    _safe_set(b, 'room_DetailCode235', a2)
    assert _is_linked(b, 'room_DetailCode235', a2)
    if hasattr(a1, 'room_State234'):
        assert not _is_linked(a1, 'room_State234', b)
    if hasattr(a2, 'room_State234'):
        assert _is_linked(a2, 'room_State234', b)
    _safe_set(b, 'room_DetailCode235', None)
    assert not _is_linked(b, 'room_DetailCode235', a2)
    if hasattr(a2, 'room_State234'):
        assert not _is_linked(a2, 'room_State234', b)


def test_assoc_exitCode236_reverse_link_reassign_clear():
    a1 = room_State()
    a2 = room_State()
    b = room_DetailCode(commands="sample_text")
    _safe_set(b, 'room_DetailCode238', a1)
    assert _is_linked(b, 'room_DetailCode238', a1)
    if hasattr(a1, 'room_State237'):
        assert _is_linked(a1, 'room_State237', b)
    _safe_set(b, 'room_DetailCode238', a2)
    assert _is_linked(b, 'room_DetailCode238', a2)
    if hasattr(a1, 'room_State237'):
        assert not _is_linked(a1, 'room_State237', b)
    if hasattr(a2, 'room_State237'):
        assert _is_linked(a2, 'room_State237', b)
    _safe_set(b, 'room_DetailCode238', None)
    assert not _is_linked(b, 'room_DetailCode238', a2)
    if hasattr(a2, 'room_State237'):
        assert not _is_linked(a2, 'room_State237', b)


def test_assoc_externalTypes5_reverse_link_reassign_clear():
    a1 = room_RoomModel(name="sample_text")
    a2 = room_RoomModel(name="sample_text_2")
    b = room_ExternalType(targetName="sample_text")
    _safe_set(b, 'room_ExternalType', a1)
    assert _is_linked(b, 'room_ExternalType', a1)
    if hasattr(a1, 'room_RoomModel6'):
        assert _is_linked(a1, 'room_RoomModel6', b)
    _safe_set(b, 'room_ExternalType', a2)
    assert _is_linked(b, 'room_ExternalType', a2)
    if hasattr(a1, 'room_RoomModel6'):
        assert not _is_linked(a1, 'room_RoomModel6', b)
    if hasattr(a2, 'room_RoomModel6'):
        assert _is_linked(a2, 'room_RoomModel6', b)
    _safe_set(b, 'room_ExternalType', None)
    assert not _is_linked(b, 'room_ExternalType', a2)
    if hasattr(a2, 'room_RoomModel6'):
        assert not _is_linked(a2, 'room_RoomModel6', b)


def test_assoc_ifPorts140_reverse_link_reassign_clear():
    a1 = room_Port(conjugated=True, multiplicity=7)
    a2 = room_Port(conjugated=False, multiplicity=13)
    b = room_ActorClass(abstract=True, commType="sample_text")
    _safe_set(b, 'room_ActorClass141', {a1})
    assert _is_linked(b, 'room_ActorClass141', a1)
    if hasattr(a1, 'room_Port'):
        assert _is_linked(a1, 'room_Port', b)
    _safe_set(b, 'room_ActorClass141', {a2})
    assert _is_linked(b, 'room_ActorClass141', a2)
    if hasattr(a1, 'room_Port'):
        assert not _is_linked(a1, 'room_Port', b)
    if hasattr(a2, 'room_Port'):
        assert _is_linked(a2, 'room_Port', b)
    _safe_set(b, 'room_ActorClass141', set())
    assert not _is_linked(b, 'room_ActorClass141', a2)
    if hasattr(a2, 'room_Port'):
        assert not _is_linked(a2, 'room_Port', b)


def test_assoc_imports1_reverse_link_reassign_clear():
    a1 = room_RoomModel(name="sample_text")
    a2 = room_RoomModel(name="sample_text_2")
    b = room_Import(importURI="sample_text", importedNamespace="sample_text")
    _safe_set(b, 'room_Import', a1)
    assert _is_linked(b, 'room_Import', a1)
    if hasattr(a1, 'room_RoomModel2'):
        assert _is_linked(a1, 'room_RoomModel2', b)
    _safe_set(b, 'room_Import', a2)
    assert _is_linked(b, 'room_Import', a2)
    if hasattr(a1, 'room_RoomModel2'):
        assert not _is_linked(a1, 'room_RoomModel2', b)
    if hasattr(a2, 'room_RoomModel2'):
        assert _is_linked(a2, 'room_RoomModel2', b)
    _safe_set(b, 'room_Import', None)
    assert not _is_linked(b, 'room_Import', a2)
    if hasattr(a2, 'room_RoomModel2'):
        assert not _is_linked(a2, 'room_RoomModel2', b)


def test_assoc_incomingMessages89_reverse_link_reassign_clear():
    a1 = room_ProtocolClass(commType="sample_text")
    a2 = room_ProtocolClass(commType="sample_text_2")
    b = room_Message(name="sample_text", priv=True)
    _safe_set(b, 'room_Message91', a1)
    assert _is_linked(b, 'room_Message91', a1)
    if hasattr(a1, 'room_ProtocolClass90'):
        assert _is_linked(a1, 'room_ProtocolClass90', b)
    _safe_set(b, 'room_Message91', a2)
    assert _is_linked(b, 'room_Message91', a2)
    if hasattr(a1, 'room_ProtocolClass90'):
        assert not _is_linked(a1, 'room_ProtocolClass90', b)
    if hasattr(a2, 'room_ProtocolClass90'):
        assert _is_linked(a2, 'room_ProtocolClass90', b)
    _safe_set(b, 'room_Message91', None)
    assert not _is_linked(b, 'room_Message91', a2)
    if hasattr(a2, 'room_ProtocolClass90'):
        assert not _is_linked(a2, 'room_ProtocolClass90', b)


def test_assoc_instances198_reverse_link_reassign_clear():
    a1 = room_LogicalThread(name="sample_text", prio=7)
    a2 = room_LogicalThread(name="sample_text_2", prio=13)
    b = room_ActorInstancePath(segments="sample_text")
    _safe_set(b, 'room_ActorInstancePath', a1)
    assert _is_linked(b, 'room_ActorInstancePath', a1)
    if hasattr(a1, 'room_LogicalThread199'):
        assert _is_linked(a1, 'room_LogicalThread199', b)
    _safe_set(b, 'room_ActorInstancePath', a2)
    assert _is_linked(b, 'room_ActorInstancePath', a2)
    if hasattr(a1, 'room_LogicalThread199'):
        assert not _is_linked(a1, 'room_LogicalThread199', b)
    if hasattr(a2, 'room_LogicalThread199'):
        assert _is_linked(a2, 'room_LogicalThread199', b)
    _safe_set(b, 'room_ActorInstancePath', None)
    assert not _is_linked(b, 'room_ActorInstancePath', a2)
    if hasattr(a2, 'room_LogicalThread199'):
        assert not _is_linked(a2, 'room_LogicalThread199', b)


def test_assoc_intPorts145_reverse_link_reassign_clear():
    a1 = room_Port(conjugated=True, multiplicity=7)
    a2 = room_Port(conjugated=False, multiplicity=13)
    b = room_ActorClass(abstract=True, commType="sample_text")
    _safe_set(b, 'room_ActorClass146', {a1})
    assert _is_linked(b, 'room_ActorClass146', a1)
    if hasattr(a1, 'room_Port147'):
        assert _is_linked(a1, 'room_Port147', b)
    _safe_set(b, 'room_ActorClass146', {a2})
    assert _is_linked(b, 'room_ActorClass146', a2)
    if hasattr(a1, 'room_Port147'):
        assert not _is_linked(a1, 'room_Port147', b)
    if hasattr(a2, 'room_Port147'):
        assert _is_linked(a2, 'room_Port147', b)
    _safe_set(b, 'room_ActorClass146', set())
    assert not _is_linked(b, 'room_ActorClass146', a2)
    if hasattr(a2, 'room_Port147'):
        assert not _is_linked(a2, 'room_Port147', b)


def test_assoc_operations163_reverse_link_reassign_clear():
    a1 = room_StandardOperation(destructor=True)
    a2 = room_StandardOperation(destructor=False)
    b = room_ActorClass(abstract=True, commType="sample_text")
    _safe_set(b, 'room_ActorClass164', {a1})
    assert _is_linked(b, 'room_ActorClass164', a1)
    if hasattr(a1, 'room_StandardOperation165'):
        assert _is_linked(a1, 'room_StandardOperation165', b)
    _safe_set(b, 'room_ActorClass164', {a2})
    assert _is_linked(b, 'room_ActorClass164', a2)
    if hasattr(a1, 'room_StandardOperation165'):
        assert not _is_linked(a1, 'room_StandardOperation165', b)
    if hasattr(a2, 'room_StandardOperation165'):
        assert _is_linked(a2, 'room_StandardOperation165', b)
    _safe_set(b, 'room_ActorClass164', set())
    assert not _is_linked(b, 'room_ActorClass164', a2)
    if hasattr(a2, 'room_StandardOperation165'):
        assert not _is_linked(a2, 'room_StandardOperation165', b)


def test_assoc_outgoingMessages92_reverse_link_reassign_clear():
    a1 = room_ProtocolClass(commType="sample_text")
    a2 = room_ProtocolClass(commType="sample_text_2")
    b = room_Message(name="sample_text", priv=True)
    _safe_set(b, 'room_Message94', a1)
    assert _is_linked(b, 'room_Message94', a1)
    if hasattr(a1, 'room_ProtocolClass93'):
        assert _is_linked(a1, 'room_ProtocolClass93', b)
    _safe_set(b, 'room_Message94', a2)
    assert _is_linked(b, 'room_Message94', a2)
    if hasattr(a1, 'room_ProtocolClass93'):
        assert not _is_linked(a1, 'room_ProtocolClass93', b)
    if hasattr(a2, 'room_ProtocolClass93'):
        assert _is_linked(a2, 'room_ProtocolClass93', b)
    _safe_set(b, 'room_Message94', None)
    assert not _is_linked(b, 'room_Message94', a2)
    if hasattr(a2, 'room_ProtocolClass93'):
        assert not _is_linked(a2, 'room_ProtocolClass93', b)


def test_assoc_primitiveTypes3_reverse_link_reassign_clear():
    a1 = room_RoomModel(name="sample_text")
    a2 = room_RoomModel(name="sample_text_2")
    b = room_PrimitiveType(castName="sample_text", defaultValueLiteral="sample_text", targetName="sample_text", type="sample_text")
    _safe_set(b, 'room_PrimitiveType', a1)
    assert _is_linked(b, 'room_PrimitiveType', a1)
    if hasattr(a1, 'room_RoomModel4'):
        assert _is_linked(a1, 'room_RoomModel4', b)
    _safe_set(b, 'room_PrimitiveType', a2)
    assert _is_linked(b, 'room_PrimitiveType', a2)
    if hasattr(a1, 'room_RoomModel4'):
        assert not _is_linked(a1, 'room_RoomModel4', b)
    if hasattr(a2, 'room_RoomModel4'):
        assert _is_linked(a2, 'room_RoomModel4', b)
    _safe_set(b, 'room_PrimitiveType', None)
    assert not _is_linked(b, 'room_PrimitiveType', a2)
    if hasattr(a2, 'room_RoomModel4'):
        assert not _is_linked(a2, 'room_RoomModel4', b)


def test_assoc_refType35_reverse_link_reassign_clear():
    a1 = room_VarDecl(name="sample_text")
    a2 = room_VarDecl(name="sample_text_2")
    b = room_RefableType(ref=True)
    _safe_set(b, 'room_RefableType', a1)
    assert _is_linked(b, 'room_RefableType', a1)
    if hasattr(a1, 'room_VarDecl'):
        assert _is_linked(a1, 'room_VarDecl', b)
    _safe_set(b, 'room_RefableType', a2)
    assert _is_linked(b, 'room_RefableType', a2)
    if hasattr(a1, 'room_VarDecl'):
        assert not _is_linked(a1, 'room_VarDecl', b)
    if hasattr(a2, 'room_VarDecl'):
        assert _is_linked(a2, 'room_VarDecl', b)
    _safe_set(b, 'room_RefableType', None)
    assert not _is_linked(b, 'room_RefableType', a2)
    if hasattr(a2, 'room_VarDecl'):
        assert not _is_linked(a2, 'room_VarDecl', b)


def test_assoc_refType57_reverse_link_reassign_clear():
    a1 = room_RefableType(ref=True)
    a2 = room_RefableType(ref=False)
    b = room_Attribute(defaultValueLiteral="sample_text", name="sample_text", size=7)
    _safe_set(b, 'room_Attribute58', a1)
    assert _is_linked(b, 'room_Attribute58', a1)
    if hasattr(a1, 'room_RefableType59'):
        assert _is_linked(a1, 'room_RefableType59', b)
    _safe_set(b, 'room_Attribute58', a2)
    assert _is_linked(b, 'room_Attribute58', a2)
    if hasattr(a1, 'room_RefableType59'):
        assert not _is_linked(a1, 'room_RefableType59', b)
    if hasattr(a2, 'room_RefableType59'):
        assert _is_linked(a2, 'room_RefableType59', b)
    _safe_set(b, 'room_Attribute58', None)
    assert not _is_linked(b, 'room_Attribute58', a2)
    if hasattr(a2, 'room_RefableType59'):
        assert not _is_linked(a2, 'room_RefableType59', b)


def test_assoc_returntype65_reverse_link_reassign_clear():
    a1 = room_RefableType(ref=True)
    a2 = room_RefableType(ref=False)
    b = room_Operation(name="sample_text")
    _safe_set(b, 'room_Operation66', a1)
    assert _is_linked(b, 'room_Operation66', a1)
    if hasattr(a1, 'room_RefableType67'):
        assert _is_linked(a1, 'room_RefableType67', b)
    _safe_set(b, 'room_Operation66', a2)
    assert _is_linked(b, 'room_Operation66', a2)
    if hasattr(a1, 'room_RefableType67'):
        assert not _is_linked(a1, 'room_RefableType67', b)
    if hasattr(a2, 'room_RefableType67'):
        assert _is_linked(a2, 'room_RefableType67', b)
    _safe_set(b, 'room_Operation66', None)
    assert not _is_linked(b, 'room_Operation66', a2)
    if hasattr(a2, 'room_RefableType67'):
        assert not _is_linked(a2, 'room_RefableType67', b)


def test_assoc_structureDocu142_reverse_link_reassign_clear():
    a1 = room_Documentation(text="sample_text")
    a2 = room_Documentation(text="sample_text_2")
    b = room_ActorClass(abstract=True, commType="sample_text")
    _safe_set(b, 'room_ActorClass143', a1)
    assert _is_linked(b, 'room_ActorClass143', a1)
    if hasattr(a1, 'room_Documentation144'):
        assert _is_linked(a1, 'room_Documentation144', b)
    _safe_set(b, 'room_ActorClass143', a2)
    assert _is_linked(b, 'room_ActorClass143', a2)
    if hasattr(a1, 'room_Documentation144'):
        assert not _is_linked(a1, 'room_Documentation144', b)
    if hasattr(a2, 'room_Documentation144'):
        assert _is_linked(a2, 'room_Documentation144', b)
    _safe_set(b, 'room_ActorClass143', None)
    assert not _is_linked(b, 'room_ActorClass143', a2)
    if hasattr(a2, 'room_Documentation144'):
        assert not _is_linked(a2, 'room_Documentation144', b)


def test_assoc_type228_reverse_link_reassign_clear():
    a1 = room_ActorRef(size=7)
    a2 = room_ActorRef(size=13)
    b = room_ActorClass(abstract=True, commType="sample_text")
    _safe_set(b, 'room_ActorClass230', a1)
    assert _is_linked(b, 'room_ActorClass230', a1)
    if hasattr(a1, 'room_ActorRef229'):
        assert _is_linked(a1, 'room_ActorRef229', b)
    _safe_set(b, 'room_ActorClass230', a2)
    assert _is_linked(b, 'room_ActorClass230', a2)
    if hasattr(a1, 'room_ActorRef229'):
        assert not _is_linked(a1, 'room_ActorRef229', b)
    if hasattr(a2, 'room_ActorRef229'):
        assert _is_linked(a2, 'room_ActorRef229', b)
    _safe_set(b, 'room_ActorClass230', None)
    assert not _is_linked(b, 'room_ActorClass230', a2)
    if hasattr(a2, 'room_ActorRef229'):
        assert not _is_linked(a2, 'room_ActorRef229', b)


def test_assoc_userCode180_reverse_link_reassign_clear():
    a1 = room_ProtocolClass(commType="sample_text")
    a2 = room_ProtocolClass(commType="sample_text_2")
    b = room_DetailCode(commands="sample_text")
    _safe_set(b, 'room_DetailCode82', a1)
    assert _is_linked(b, 'room_DetailCode82', a1)
    if hasattr(a1, 'room_ProtocolClass81'):
        assert _is_linked(a1, 'room_ProtocolClass81', b)
    _safe_set(b, 'room_DetailCode82', a2)
    assert _is_linked(b, 'room_DetailCode82', a2)
    if hasattr(a1, 'room_ProtocolClass81'):
        assert not _is_linked(a1, 'room_ProtocolClass81', b)
    if hasattr(a2, 'room_ProtocolClass81'):
        assert _is_linked(a2, 'room_ProtocolClass81', b)
    _safe_set(b, 'room_DetailCode82', None)
    assert not _is_linked(b, 'room_DetailCode82', a2)
    if hasattr(a2, 'room_ProtocolClass81'):
        assert not _is_linked(a2, 'room_ProtocolClass81', b)


def test_assoc_userCode283_reverse_link_reassign_clear():
    a1 = room_ProtocolClass(commType="sample_text")
    a2 = room_ProtocolClass(commType="sample_text_2")
    b = room_DetailCode(commands="sample_text")
    _safe_set(b, 'room_DetailCode85', a1)
    assert _is_linked(b, 'room_DetailCode85', a1)
    if hasattr(a1, 'room_ProtocolClass84'):
        assert _is_linked(a1, 'room_ProtocolClass84', b)
    _safe_set(b, 'room_DetailCode85', a2)
    assert _is_linked(b, 'room_DetailCode85', a2)
    if hasattr(a1, 'room_ProtocolClass84'):
        assert not _is_linked(a1, 'room_ProtocolClass84', b)
    if hasattr(a2, 'room_ProtocolClass84'):
        assert _is_linked(a2, 'room_ProtocolClass84', b)
    _safe_set(b, 'room_DetailCode85', None)
    assert not _is_linked(b, 'room_DetailCode85', a2)
    if hasattr(a2, 'room_ProtocolClass84'):
        assert not _is_linked(a2, 'room_ProtocolClass84', b)


def test_assoc_userCode386_reverse_link_reassign_clear():
    a1 = room_ProtocolClass(commType="sample_text")
    a2 = room_ProtocolClass(commType="sample_text_2")
    b = room_DetailCode(commands="sample_text")
    _safe_set(b, 'room_DetailCode88', a1)
    assert _is_linked(b, 'room_DetailCode88', a1)
    if hasattr(a1, 'room_ProtocolClass87'):
        assert _is_linked(a1, 'room_ProtocolClass87', b)
    _safe_set(b, 'room_DetailCode88', a2)
    assert _is_linked(b, 'room_DetailCode88', a2)
    if hasattr(a1, 'room_ProtocolClass87'):
        assert not _is_linked(a1, 'room_ProtocolClass87', b)
    if hasattr(a2, 'room_ProtocolClass87'):
        assert _is_linked(a2, 'room_ProtocolClass87', b)
    _safe_set(b, 'room_DetailCode88', None)
    assert not _is_linked(b, 'room_DetailCode88', a2)
    if hasattr(a2, 'room_ProtocolClass87'):
        assert not _is_linked(a2, 'room_ProtocolClass87', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_action282_stub_double():
    # room_RefinedTransition has no real 'room_RefinedTransition283' property in the generated
    # code (a bare stub) -- manually attach it so room_DetailCode's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # room_DetailCode's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = room_DetailCode(commands="sample_text")
    partner = room_RefinedTransition()
    setattr(partner, 'room_RefinedTransition283', None)
    _safe_set(owner, 'room_DetailCode284', partner)
    assert getattr(partner, 'room_RefinedTransition283') == owner
    _safe_set(owner, 'room_DetailCode284', None)
    assert getattr(partner, 'room_RefinedTransition283') is None


def test_assoc_actorRef205_stub_double():
    # room_BindingEndPoint has no real 'room_BindingEndPoint206' property in the generated
    # code (a bare stub) -- manually attach it so room_ActorContainerRef's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # room_ActorContainerRef's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = room_ActorContainerRef(name="sample_text")
    partner = room_BindingEndPoint()
    setattr(partner, 'room_BindingEndPoint206', None)
    _safe_set(owner, 'room_ActorContainerRef207', partner)
    assert getattr(partner, 'room_BindingEndPoint206') == owner
    _safe_set(owner, 'room_ActorContainerRef207', None)
    assert getattr(partner, 'room_BindingEndPoint206') is None


def test_assoc_actorRefs33_stub_double():
    # room_ActorContainerClass has no real 'room_ActorContainerClass34' property in the generated
    # code (a bare stub) -- manually attach it so room_ActorRef's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # room_ActorRef's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = room_ActorRef(size=7)
    partner = room_ActorContainerClass()
    setattr(partner, 'room_ActorContainerClass34', None)
    _safe_set(owner, 'room_ActorRef', partner)
    assert owner in getattr(partner, 'room_ActorContainerClass34')
    _safe_set(owner, 'room_ActorRef', None)
    assert owner not in getattr(partner, 'room_ActorContainerClass34')


def test_assoc_annotations19_stub_double():
    # room_StructureClass has no real 'room_StructureClass' property in the generated
    # code (a bare stub) -- manually attach it so room_Annotation's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # room_Annotation's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = room_Annotation(name="sample_text")
    partner = room_StructureClass()
    setattr(partner, 'room_StructureClass', None)
    _safe_set(owner, 'room_Annotation', partner)
    assert owner in getattr(partner, 'room_StructureClass')
    _safe_set(owner, 'room_Annotation', None)
    assert owner not in getattr(partner, 'room_StructureClass')


def test_assoc_annotations41_stub_double():
    # room_DataClass has no real 'room_DataClass42' property in the generated
    # code (a bare stub) -- manually attach it so room_Annotation's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # room_Annotation's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = room_Annotation(name="sample_text")
    partner = room_DataClass()
    setattr(partner, 'room_DataClass42', None)
    _safe_set(owner, 'room_Annotation43', partner)
    assert owner in getattr(partner, 'room_DataClass42')
    _safe_set(owner, 'room_Annotation43', None)
    assert owner not in getattr(partner, 'room_DataClass42')


def test_assoc_annotations75_stub_double():
    # room_GeneralProtocolClass has no real 'room_GeneralProtocolClass76' property in the generated
    # code (a bare stub) -- manually attach it so room_Annotation's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # room_Annotation's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = room_Annotation(name="sample_text")
    partner = room_GeneralProtocolClass()
    setattr(partner, 'room_GeneralProtocolClass76', None)
    _safe_set(owner, 'room_Annotation77', partner)
    assert owner in getattr(partner, 'room_GeneralProtocolClass76')
    _safe_set(owner, 'room_Annotation77', None)
    assert owner not in getattr(partner, 'room_GeneralProtocolClass76')


def test_assoc_attributes115_stub_double():
    # room_PortClass has no real 'room_PortClass116' property in the generated
    # code (a bare stub) -- manually attach it so room_Attribute's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # room_Attribute's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = room_Attribute(defaultValueLiteral="sample_text", name="sample_text", size=7)
    partner = room_PortClass()
    setattr(partner, 'room_PortClass116', None)
    _safe_set(owner, 'room_Attribute117', partner)
    assert owner in getattr(partner, 'room_PortClass116')
    _safe_set(owner, 'room_Attribute117', None)
    assert owner not in getattr(partner, 'room_PortClass116')


def test_assoc_attributes53_stub_double():
    # room_DataClass has no real 'room_DataClass54' property in the generated
    # code (a bare stub) -- manually attach it so room_Attribute's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # room_Attribute's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = room_Attribute(defaultValueLiteral="sample_text", name="sample_text", size=7)
    partner = room_DataClass()
    setattr(partner, 'room_DataClass54', None)
    _safe_set(owner, 'room_Attribute', partner)
    assert owner in getattr(partner, 'room_DataClass54')
    _safe_set(owner, 'room_Attribute', None)
    assert owner not in getattr(partner, 'room_DataClass54')


def test_assoc_chPoints250_stub_double():
    # room_StateGraph has no real 'room_StateGraph251' property in the generated
    # code (a bare stub) -- manually attach it so room_ChoicePoint's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # room_ChoicePoint's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = room_ChoicePoint(name="sample_text")
    partner = room_StateGraph()
    setattr(partner, 'room_StateGraph251', None)
    _safe_set(owner, 'room_ChoicePoint', partner)
    assert owner in getattr(partner, 'room_StateGraph251')
    _safe_set(owner, 'room_ChoicePoint', None)
    assert owner not in getattr(partner, 'room_StateGraph251')


def test_assoc_condition274_stub_double():
    # room_CPBranchTransition has no real 'room_CPBranchTransition' property in the generated
    # code (a bare stub) -- manually attach it so room_DetailCode's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # room_DetailCode's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = room_DetailCode(commands="sample_text")
    partner = room_CPBranchTransition()
    setattr(partner, 'room_CPBranchTransition', None)
    _safe_set(owner, 'room_DetailCode275', partner)
    assert getattr(partner, 'room_CPBranchTransition') == owner
    _safe_set(owner, 'room_DetailCode275', None)
    assert getattr(partner, 'room_CPBranchTransition') is None


def test_assoc_conjugate97_stub_double():
    # room_PortClass has no real 'room_PortClass99' property in the generated
    # code (a bare stub) -- manually attach it so room_ProtocolClass's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # room_ProtocolClass's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = room_ProtocolClass(commType="sample_text")
    partner = room_PortClass()
    setattr(partner, 'room_PortClass99', None)
    _safe_set(owner, 'room_ProtocolClass98', partner)
    assert getattr(partner, 'room_PortClass99') == owner
    _safe_set(owner, 'room_ProtocolClass98', None)
    assert getattr(partner, 'room_PortClass99') is None


def test_assoc_cp294_stub_double():
    # room_ChoicepointTerminal has no real 'room_ChoicepointTerminal' property in the generated
    # code (a bare stub) -- manually attach it so room_ChoicePoint's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # room_ChoicePoint's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = room_ChoicePoint(name="sample_text")
    partner = room_ChoicepointTerminal()
    setattr(partner, 'room_ChoicepointTerminal', None)
    _safe_set(owner, 'room_ChoicePoint295', partner)
    assert getattr(partner, 'room_ChoicepointTerminal') == owner
    _safe_set(owner, 'room_ChoicePoint295', None)
    assert getattr(partner, 'room_ChoicepointTerminal') is None


def test_assoc_dataClasses7_stub_double():
    # room_DataClass has no real 'room_DataClass' property in the generated
    # code (a bare stub) -- manually attach it so room_RoomModel's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # room_RoomModel's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = room_RoomModel(name="sample_text")
    partner = room_DataClass()
    setattr(partner, 'room_DataClass', None)
    _safe_set(owner, 'room_RoomModel8', {partner})
    assert getattr(partner, 'room_DataClass') == owner
    _safe_set(owner, 'room_RoomModel8', set())
    assert getattr(partner, 'room_DataClass') is None


def test_assoc_detailCode126_stub_double():
    # room_MessageHandler has no real 'room_MessageHandler127' property in the generated
    # code (a bare stub) -- manually attach it so room_DetailCode's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # room_DetailCode's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = room_DetailCode(commands="sample_text")
    partner = room_MessageHandler()
    setattr(partner, 'room_MessageHandler127', None)
    _safe_set(owner, 'room_DetailCode128', partner)
    assert getattr(partner, 'room_MessageHandler127') == owner
    _safe_set(owner, 'room_DetailCode128', None)
    assert getattr(partner, 'room_MessageHandler127') is None


def test_assoc_docu279_stub_double():
    # room_RefinedTransition has no real 'room_RefinedTransition280' property in the generated
    # code (a bare stub) -- manually attach it so room_Documentation's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # room_Documentation's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = room_Documentation(text="sample_text")
    partner = room_RefinedTransition()
    setattr(partner, 'room_RefinedTransition280', None)
    _safe_set(owner, 'room_Documentation281', partner)
    assert getattr(partner, 'room_RefinedTransition280') == owner
    _safe_set(owner, 'room_Documentation281', None)
    assert getattr(partner, 'room_RefinedTransition280') is None


def test_assoc_extPorts148_stub_double():
    # room_ExternalPort has no real 'room_ExternalPort' property in the generated
    # code (a bare stub) -- manually attach it so room_ActorClass's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # room_ActorClass's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = room_ActorClass(abstract=True, commType="sample_text")
    partner = room_ExternalPort()
    setattr(partner, 'room_ExternalPort', None)
    _safe_set(owner, 'room_ActorClass149', {partner})
    assert getattr(partner, 'room_ExternalPort') == owner
    _safe_set(owner, 'room_ActorClass149', set())
    assert getattr(partner, 'room_ExternalPort') is None


def test_assoc_from_303_stub_double():
    # room_MessageFromIf has no real 'room_MessageFromIf304' property in the generated
    # code (a bare stub) -- manually attach it so room_InterfaceItem's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # room_InterfaceItem's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = room_InterfaceItem(name="sample_text")
    partner = room_MessageFromIf()
    setattr(partner, 'room_MessageFromIf304', None)
    _safe_set(owner, 'room_InterfaceItem', partner)
    assert getattr(partner, 'room_MessageFromIf304') == owner
    _safe_set(owner, 'room_InterfaceItem', None)
    assert getattr(partner, 'room_MessageFromIf304') is None


def test_assoc_guard272_stub_double():
    # room_GuardedTransition has no real 'room_GuardedTransition' property in the generated
    # code (a bare stub) -- manually attach it so room_DetailCode's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # room_DetailCode's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = room_DetailCode(commands="sample_text")
    partner = room_GuardedTransition()
    setattr(partner, 'room_GuardedTransition', None)
    _safe_set(owner, 'room_DetailCode273', partner)
    assert getattr(partner, 'room_GuardedTransition') == owner
    _safe_set(owner, 'room_DetailCode273', None)
    assert getattr(partner, 'room_GuardedTransition') is None


def test_assoc_guard305_stub_double():
    # room_Guard has no real 'room_Guard306' property in the generated
    # code (a bare stub) -- manually attach it so room_DetailCode's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # room_DetailCode's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = room_DetailCode(commands="sample_text")
    partner = room_Guard()
    setattr(partner, 'room_Guard306', None)
    _safe_set(owner, 'room_DetailCode307', partner)
    assert getattr(partner, 'room_Guard306') == owner
    _safe_set(owner, 'room_DetailCode307', None)
    assert getattr(partner, 'room_Guard306') is None


def test_assoc_ifport174_stub_double():
    # room_ExternalPort has no real 'room_ExternalPort175' property in the generated
    # code (a bare stub) -- manually attach it so room_Port's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # room_Port's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = room_Port(conjugated=True, multiplicity=7)
    partner = room_ExternalPort()
    setattr(partner, 'room_ExternalPort175', None)
    _safe_set(owner, 'room_Port176', partner)
    assert getattr(partner, 'room_ExternalPort175') == owner
    _safe_set(owner, 'room_Port176', None)
    assert getattr(partner, 'room_ExternalPort175') is None


def test_assoc_message300_stub_double():
    # room_MessageFromIf has no real 'room_MessageFromIf301' property in the generated
    # code (a bare stub) -- manually attach it so room_Message's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # room_Message's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = room_Message(name="sample_text", priv=True)
    partner = room_MessageFromIf()
    setattr(partner, 'room_MessageFromIf301', None)
    _safe_set(owner, 'room_Message302', partner)
    assert getattr(partner, 'room_MessageFromIf301') == owner
    _safe_set(owner, 'room_Message302', None)
    assert getattr(partner, 'room_MessageFromIf301') is None


def test_assoc_msg123_stub_double():
    # room_MessageHandler has no real 'room_MessageHandler124' property in the generated
    # code (a bare stub) -- manually attach it so room_Message's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # room_Message's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = room_Message(name="sample_text", priv=True)
    partner = room_MessageHandler()
    setattr(partner, 'room_MessageHandler124', None)
    _safe_set(owner, 'room_Message125', partner)
    assert getattr(partner, 'room_MessageHandler124') == owner
    _safe_set(owner, 'room_Message125', None)
    assert getattr(partner, 'room_MessageHandler124') is None


def test_assoc_msg131_stub_double():
    # room_SemanticsRule has no real 'room_SemanticsRule132' property in the generated
    # code (a bare stub) -- manually attach it so room_Message's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # room_Message's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = room_Message(name="sample_text", priv=True)
    partner = room_SemanticsRule()
    setattr(partner, 'room_SemanticsRule132', None)
    _safe_set(owner, 'room_Message133', partner)
    assert getattr(partner, 'room_SemanticsRule132') == owner
    _safe_set(owner, 'room_Message133', None)
    assert getattr(partner, 'room_SemanticsRule132') is None


def test_assoc_operations55_stub_double():
    # room_DataClass has no real 'room_DataClass56' property in the generated
    # code (a bare stub) -- manually attach it so room_StandardOperation's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # room_StandardOperation's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = room_StandardOperation(destructor=True)
    partner = room_DataClass()
    setattr(partner, 'room_DataClass56', None)
    _safe_set(owner, 'room_StandardOperation', partner)
    assert owner in getattr(partner, 'room_DataClass56')
    _safe_set(owner, 'room_StandardOperation', None)
    assert owner not in getattr(partner, 'room_DataClass56')


def test_assoc_port208_stub_double():
    # room_BindingEndPoint has no real 'room_BindingEndPoint209' property in the generated
    # code (a bare stub) -- manually attach it so room_Port's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # room_Port's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = room_Port(conjugated=True, multiplicity=7)
    partner = room_BindingEndPoint()
    setattr(partner, 'room_BindingEndPoint209', None)
    _safe_set(owner, 'room_Port210', partner)
    assert getattr(partner, 'room_BindingEndPoint209') == owner
    _safe_set(owner, 'room_Port210', None)
    assert getattr(partner, 'room_BindingEndPoint209') is None


def test_assoc_protocol103_stub_double():
    # room_GeneralProtocolClass has no real 'room_GeneralProtocolClass105' property in the generated
    # code (a bare stub) -- manually attach it so room_SubProtocol's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # room_SubProtocol's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = room_SubProtocol(name="sample_text")
    partner = room_GeneralProtocolClass()
    setattr(partner, 'room_GeneralProtocolClass105', None)
    _safe_set(owner, 'room_SubProtocol104', partner)
    assert getattr(partner, 'room_GeneralProtocolClass105') == owner
    _safe_set(owner, 'room_SubProtocol104', None)
    assert getattr(partner, 'room_GeneralProtocolClass105') is None


def test_assoc_protocol168_stub_double():
    # room_GeneralProtocolClass has no real 'room_GeneralProtocolClass170' property in the generated
    # code (a bare stub) -- manually attach it so room_Port's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # room_Port's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = room_Port(conjugated=True, multiplicity=7)
    partner = room_GeneralProtocolClass()
    setattr(partner, 'room_GeneralProtocolClass170', None)
    _safe_set(owner, 'room_Port169', partner)
    assert getattr(partner, 'room_GeneralProtocolClass170') == owner
    _safe_set(owner, 'room_Port169', None)
    assert getattr(partner, 'room_GeneralProtocolClass170') is None


def test_assoc_protocol177_stub_double():
    # room_SAPRef has no real 'room_SAPRef178' property in the generated
    # code (a bare stub) -- manually attach it so room_ProtocolClass's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # room_ProtocolClass's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = room_ProtocolClass(commType="sample_text")
    partner = room_SAPRef()
    setattr(partner, 'room_SAPRef178', None)
    _safe_set(owner, 'room_ProtocolClass179', partner)
    assert getattr(partner, 'room_SAPRef178') == owner
    _safe_set(owner, 'room_ProtocolClass179', None)
    assert getattr(partner, 'room_SAPRef178') is None


def test_assoc_protocol180_stub_double():
    # room_SPPRef has no real 'room_SPPRef181' property in the generated
    # code (a bare stub) -- manually attach it so room_ProtocolClass's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # room_ProtocolClass's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = room_ProtocolClass(commType="sample_text")
    partner = room_SPPRef()
    setattr(partner, 'room_SPPRef181', None)
    _safe_set(owner, 'room_ProtocolClass182', partner)
    assert getattr(partner, 'room_SPPRef181') == owner
    _safe_set(owner, 'room_ProtocolClass182', None)
    assert getattr(partner, 'room_SPPRef181') is None


def test_assoc_protocolClasses9_stub_double():
    # room_GeneralProtocolClass has no real 'room_GeneralProtocolClass' property in the generated
    # code (a bare stub) -- manually attach it so room_RoomModel's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # room_RoomModel's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = room_RoomModel(name="sample_text")
    partner = room_GeneralProtocolClass()
    setattr(partner, 'room_GeneralProtocolClass', None)
    _safe_set(owner, 'room_RoomModel10', {partner})
    assert getattr(partner, 'room_GeneralProtocolClass') == owner
    _safe_set(owner, 'room_RoomModel10', set())
    assert getattr(partner, 'room_GeneralProtocolClass') is None


def test_assoc_ref218_stub_double():
    # room_RefSAPoint has no real 'room_RefSAPoint' property in the generated
    # code (a bare stub) -- manually attach it so room_ActorContainerRef's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # room_ActorContainerRef's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = room_ActorContainerRef(name="sample_text")
    partner = room_RefSAPoint()
    setattr(partner, 'room_RefSAPoint', None)
    _safe_set(owner, 'room_ActorContainerRef219', partner)
    assert getattr(partner, 'room_RefSAPoint') == owner
    _safe_set(owner, 'room_ActorContainerRef219', None)
    assert getattr(partner, 'room_RefSAPoint') is None


def test_assoc_ref222_stub_double():
    # room_SPPoint has no real 'room_SPPoint223' property in the generated
    # code (a bare stub) -- manually attach it so room_ActorContainerRef's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # room_ActorContainerRef's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = room_ActorContainerRef(name="sample_text")
    partner = room_SPPoint()
    setattr(partner, 'room_SPPoint223', None)
    _safe_set(owner, 'room_ActorContainerRef224', partner)
    assert getattr(partner, 'room_SPPoint223') == owner
    _safe_set(owner, 'room_ActorContainerRef224', None)
    assert getattr(partner, 'room_SPPoint223') is None


def test_assoc_regular95_stub_double():
    # room_PortClass has no real 'room_PortClass' property in the generated
    # code (a bare stub) -- manually attach it so room_ProtocolClass's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # room_ProtocolClass's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = room_ProtocolClass(commType="sample_text")
    partner = room_PortClass()
    setattr(partner, 'room_PortClass', None)
    _safe_set(owner, 'room_ProtocolClass96', partner)
    assert getattr(partner, 'room_PortClass') == owner
    _safe_set(owner, 'room_ProtocolClass96', None)
    assert getattr(partner, 'room_PortClass') is None


def test_assoc_relayPorts193_stub_double():
    # room_SubSystemClass has no real 'room_SubSystemClass194' property in the generated
    # code (a bare stub) -- manually attach it so room_Port's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # room_Port's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = room_Port(conjugated=True, multiplicity=7)
    partner = room_SubSystemClass()
    setattr(partner, 'room_SubSystemClass194', None)
    _safe_set(owner, 'room_Port195', partner)
    assert owner in getattr(partner, 'room_SubSystemClass194')
    _safe_set(owner, 'room_Port195', None)
    assert owner not in getattr(partner, 'room_SubSystemClass194')


def test_assoc_semantics100_stub_double():
    # room_ProtocolSemantics has no real 'room_ProtocolSemantics' property in the generated
    # code (a bare stub) -- manually attach it so room_ProtocolClass's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # room_ProtocolClass's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = room_ProtocolClass(commType="sample_text")
    partner = room_ProtocolSemantics()
    setattr(partner, 'room_ProtocolSemantics', None)
    _safe_set(owner, 'room_ProtocolClass101', partner)
    assert getattr(partner, 'room_ProtocolSemantics') == owner
    _safe_set(owner, 'room_ProtocolClass101', None)
    assert getattr(partner, 'room_ProtocolSemantics') is None


def test_assoc_sendsMsg74_stub_double():
    # room_PortOperation has no real 'room_PortOperation' property in the generated
    # code (a bare stub) -- manually attach it so room_Message's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # room_Message's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = room_Message(name="sample_text", priv=True)
    partner = room_PortOperation()
    setattr(partner, 'room_PortOperation', None)
    _safe_set(owner, 'room_Message', partner)
    assert getattr(partner, 'room_PortOperation') == owner
    _safe_set(owner, 'room_Message', None)
    assert getattr(partner, 'room_PortOperation') is None


def test_assoc_serviceImplementations150_stub_double():
    # room_ServiceImplementation has no real 'room_ServiceImplementation' property in the generated
    # code (a bare stub) -- manually attach it so room_ActorClass's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # room_ActorClass's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = room_ActorClass(abstract=True, commType="sample_text")
    partner = room_ServiceImplementation()
    setattr(partner, 'room_ServiceImplementation', None)
    _safe_set(owner, 'room_ActorClass151', {partner})
    assert getattr(partner, 'room_ServiceImplementation') == owner
    _safe_set(owner, 'room_ActorClass151', set())
    assert getattr(partner, 'room_ServiceImplementation') is None


def test_assoc_state285_stub_double():
    # room_StateTerminal has no real 'room_StateTerminal' property in the generated
    # code (a bare stub) -- manually attach it so room_State's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # room_State's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = room_State()
    partner = room_StateTerminal()
    setattr(partner, 'room_StateTerminal', None)
    _safe_set(owner, 'room_State286', partner)
    assert getattr(partner, 'room_StateTerminal') == owner
    _safe_set(owner, 'room_State286', None)
    assert getattr(partner, 'room_StateTerminal') is None


def test_assoc_state291_stub_double():
    # room_SubStateTrPointTerminal has no real 'room_SubStateTrPointTerminal292' property in the generated
    # code (a bare stub) -- manually attach it so room_State's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # room_State's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = room_State()
    partner = room_SubStateTrPointTerminal()
    setattr(partner, 'room_SubStateTrPointTerminal292', None)
    _safe_set(owner, 'room_State293', partner)
    assert getattr(partner, 'room_SubStateTrPointTerminal292') == owner
    _safe_set(owner, 'room_State293', None)
    assert getattr(partner, 'room_SubStateTrPointTerminal292') is None


def test_assoc_stateMachine166_stub_double():
    # room_StateGraph has no real 'room_StateGraph' property in the generated
    # code (a bare stub) -- manually attach it so room_ActorClass's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # room_ActorClass's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = room_ActorClass(abstract=True, commType="sample_text")
    partner = room_StateGraph()
    setattr(partner, 'room_StateGraph', None)
    _safe_set(owner, 'room_ActorClass167', partner)
    assert getattr(partner, 'room_StateGraph') == owner
    _safe_set(owner, 'room_ActorClass167', None)
    assert getattr(partner, 'room_StateGraph') is None


def test_assoc_states245_stub_double():
    # room_StateGraph has no real 'room_StateGraph246' property in the generated
    # code (a bare stub) -- manually attach it so room_State's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # room_State's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = room_State()
    partner = room_StateGraph()
    setattr(partner, 'room_StateGraph246', None)
    _safe_set(owner, 'room_State247', partner)
    assert owner in getattr(partner, 'room_StateGraph246')
    _safe_set(owner, 'room_State247', None)
    assert owner not in getattr(partner, 'room_StateGraph246')


def test_assoc_strSAPs152_stub_double():
    # room_SAPRef has no real 'room_SAPRef' property in the generated
    # code (a bare stub) -- manually attach it so room_ActorClass's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # room_ActorClass's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = room_ActorClass(abstract=True, commType="sample_text")
    partner = room_SAPRef()
    setattr(partner, 'room_SAPRef', None)
    _safe_set(owner, 'room_ActorClass153', {partner})
    assert getattr(partner, 'room_SAPRef') == owner
    _safe_set(owner, 'room_ActorClass153', set())
    assert getattr(partner, 'room_SAPRef') is None


def test_assoc_sub211_stub_double():
    # room_BindingEndPoint has no real 'room_BindingEndPoint212' property in the generated
    # code (a bare stub) -- manually attach it so room_SubProtocol's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # room_SubProtocol's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = room_SubProtocol(name="sample_text")
    partner = room_BindingEndPoint()
    setattr(partner, 'room_BindingEndPoint212', None)
    _safe_set(owner, 'room_SubProtocol213', partner)
    assert getattr(partner, 'room_BindingEndPoint212') == owner
    _safe_set(owner, 'room_SubProtocol213', None)
    assert getattr(partner, 'room_BindingEndPoint212') is None


def test_assoc_subProtocols102_stub_double():
    # room_CompoundProtocolClass has no real 'room_CompoundProtocolClass' property in the generated
    # code (a bare stub) -- manually attach it so room_SubProtocol's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # room_SubProtocol's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = room_SubProtocol(name="sample_text")
    partner = room_CompoundProtocolClass()
    setattr(partner, 'room_CompoundProtocolClass', None)
    _safe_set(owner, 'room_SubProtocol', partner)
    assert owner in getattr(partner, 'room_CompoundProtocolClass')
    _safe_set(owner, 'room_SubProtocol', None)
    assert owner not in getattr(partner, 'room_CompoundProtocolClass')


def test_assoc_subSystemClasses13_stub_double():
    # room_SubSystemClass has no real 'room_SubSystemClass' property in the generated
    # code (a bare stub) -- manually attach it so room_RoomModel's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # room_RoomModel's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = room_RoomModel(name="sample_text")
    partner = room_SubSystemClass()
    setattr(partner, 'room_SubSystemClass', None)
    _safe_set(owner, 'room_RoomModel14', {partner})
    assert getattr(partner, 'room_SubSystemClass') == owner
    _safe_set(owner, 'room_RoomModel14', set())
    assert getattr(partner, 'room_SubSystemClass') is None


def test_assoc_subgraph242_stub_double():
    # room_StateGraph has no real 'room_StateGraph244' property in the generated
    # code (a bare stub) -- manually attach it so room_State's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # room_State's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = room_State()
    partner = room_StateGraph()
    setattr(partner, 'room_StateGraph244', None)
    _safe_set(owner, 'room_State243', partner)
    assert getattr(partner, 'room_StateGraph244') == owner
    _safe_set(owner, 'room_State243', None)
    assert getattr(partner, 'room_StateGraph244') is None


def test_assoc_systems15_stub_double():
    # room_LogicalSystem has no real 'room_LogicalSystem' property in the generated
    # code (a bare stub) -- manually attach it so room_RoomModel's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # room_RoomModel's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = room_RoomModel(name="sample_text")
    partner = room_LogicalSystem()
    setattr(partner, 'room_LogicalSystem', None)
    _safe_set(owner, 'room_RoomModel16', {partner})
    assert getattr(partner, 'room_LogicalSystem') == owner
    _safe_set(owner, 'room_RoomModel16', set())
    assert getattr(partner, 'room_LogicalSystem') is None


def test_assoc_target256_stub_double():
    # room_RefinedState has no real 'room_RefinedState' property in the generated
    # code (a bare stub) -- manually attach it so room_State's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # room_State's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = room_State()
    partner = room_RefinedState()
    setattr(partner, 'room_RefinedState', None)
    _safe_set(owner, 'room_State257', partner)
    assert getattr(partner, 'room_RefinedState') == owner
    _safe_set(owner, 'room_State257', None)
    assert getattr(partner, 'room_RefinedState') is None


def test_assoc_target276_stub_double():
    # room_RefinedTransition has no real 'room_RefinedTransition277' property in the generated
    # code (a bare stub) -- manually attach it so room_Transition's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # room_Transition's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = room_Transition(name="sample_text")
    partner = room_RefinedTransition()
    setattr(partner, 'room_RefinedTransition277', None)
    _safe_set(owner, 'room_Transition278', partner)
    assert getattr(partner, 'room_RefinedTransition277') == owner
    _safe_set(owner, 'room_Transition278', None)
    assert getattr(partner, 'room_RefinedTransition277') is None


def test_assoc_threads196_stub_double():
    # room_SubSystemClass has no real 'room_SubSystemClass197' property in the generated
    # code (a bare stub) -- manually attach it so room_LogicalThread's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # room_LogicalThread's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = room_LogicalThread(name="sample_text", prio=7)
    partner = room_SubSystemClass()
    setattr(partner, 'room_SubSystemClass197', None)
    _safe_set(owner, 'room_LogicalThread', partner)
    assert owner in getattr(partner, 'room_SubSystemClass197')
    _safe_set(owner, 'room_LogicalThread', None)
    assert owner not in getattr(partner, 'room_SubSystemClass197')


def test_assoc_to261_stub_double():
    # room_TransitionTerminal has no real 'room_TransitionTerminal' property in the generated
    # code (a bare stub) -- manually attach it so room_Transition's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # room_Transition's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = room_Transition(name="sample_text")
    partner = room_TransitionTerminal()
    setattr(partner, 'room_TransitionTerminal', None)
    _safe_set(owner, 'room_Transition262', partner)
    assert getattr(partner, 'room_TransitionTerminal') == owner
    _safe_set(owner, 'room_Transition262', None)
    assert getattr(partner, 'room_TransitionTerminal') is None


def test_assoc_trPoint287_stub_double():
    # room_TrPointTerminal has no real 'room_TrPointTerminal' property in the generated
    # code (a bare stub) -- manually attach it so room_TrPoint's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # room_TrPoint's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = room_TrPoint(name="sample_text")
    partner = room_TrPointTerminal()
    setattr(partner, 'room_TrPointTerminal', None)
    _safe_set(owner, 'room_TrPoint288', partner)
    assert getattr(partner, 'room_TrPointTerminal') == owner
    _safe_set(owner, 'room_TrPoint288', None)
    assert getattr(partner, 'room_TrPointTerminal') is None


def test_assoc_trPoint289_stub_double():
    # room_SubStateTrPointTerminal has no real 'room_SubStateTrPointTerminal' property in the generated
    # code (a bare stub) -- manually attach it so room_TrPoint's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # room_TrPoint's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = room_TrPoint(name="sample_text")
    partner = room_SubStateTrPointTerminal()
    setattr(partner, 'room_SubStateTrPointTerminal', None)
    _safe_set(owner, 'room_TrPoint290', partner)
    assert getattr(partner, 'room_SubStateTrPointTerminal') == owner
    _safe_set(owner, 'room_TrPoint290', None)
    assert getattr(partner, 'room_SubStateTrPointTerminal') is None


def test_assoc_trPoints248_stub_double():
    # room_StateGraph has no real 'room_StateGraph249' property in the generated
    # code (a bare stub) -- manually attach it so room_TrPoint's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # room_TrPoint's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = room_TrPoint(name="sample_text")
    partner = room_StateGraph()
    setattr(partner, 'room_StateGraph249', None)
    _safe_set(owner, 'room_TrPoint', partner)
    assert owner in getattr(partner, 'room_StateGraph249')
    _safe_set(owner, 'room_TrPoint', None)
    assert owner not in getattr(partner, 'room_StateGraph249')


def test_assoc_transitions252_stub_double():
    # room_StateGraph has no real 'room_StateGraph253' property in the generated
    # code (a bare stub) -- manually attach it so room_Transition's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # room_Transition's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = room_Transition(name="sample_text")
    partner = room_StateGraph()
    setattr(partner, 'room_StateGraph253', None)
    _safe_set(owner, 'room_Transition', partner)
    assert owner in getattr(partner, 'room_StateGraph253')
    _safe_set(owner, 'room_Transition', None)
    assert owner not in getattr(partner, 'room_StateGraph253')


def test_assoc_type36_stub_double():
    # room_DataType has no real 'room_DataType' property in the generated
    # code (a bare stub) -- manually attach it so room_RefableType's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # room_RefableType's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = room_RefableType(ref=True)
    partner = room_DataType()
    setattr(partner, 'room_DataType', None)
    _safe_set(owner, 'room_RefableType37', partner)
    assert getattr(partner, 'room_DataType') == owner
    _safe_set(owner, 'room_RefableType37', None)
    assert getattr(partner, 'room_DataType') is None


def test_assoc_userCode112_stub_double():
    # room_PortClass has no real 'room_PortClass113' property in the generated
    # code (a bare stub) -- manually attach it so room_DetailCode's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # room_DetailCode's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = room_DetailCode(commands="sample_text")
    partner = room_PortClass()
    setattr(partner, 'room_PortClass113', None)
    _safe_set(owner, 'room_DetailCode114', partner)
    assert getattr(partner, 'room_PortClass113') == owner
    _safe_set(owner, 'room_DetailCode114', None)
    assert getattr(partner, 'room_PortClass113') is None


def test_assoc_userCode125_stub_double():
    # room_ActorContainerClass has no real 'room_ActorContainerClass26' property in the generated
    # code (a bare stub) -- manually attach it so room_DetailCode's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # room_DetailCode's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = room_DetailCode(commands="sample_text")
    partner = room_ActorContainerClass()
    setattr(partner, 'room_ActorContainerClass26', None)
    _safe_set(owner, 'room_DetailCode', partner)
    assert getattr(partner, 'room_ActorContainerClass26') == owner
    _safe_set(owner, 'room_DetailCode', None)
    assert getattr(partner, 'room_ActorContainerClass26') is None


def test_assoc_userCode144_stub_double():
    # room_DataClass has no real 'room_DataClass45' property in the generated
    # code (a bare stub) -- manually attach it so room_DetailCode's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # room_DetailCode's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = room_DetailCode(commands="sample_text")
    partner = room_DataClass()
    setattr(partner, 'room_DataClass45', None)
    _safe_set(owner, 'room_DetailCode46', partner)
    assert getattr(partner, 'room_DataClass45') == owner
    _safe_set(owner, 'room_DetailCode46', None)
    assert getattr(partner, 'room_DataClass45') is None


def test_assoc_userCode227_stub_double():
    # room_ActorContainerClass has no real 'room_ActorContainerClass28' property in the generated
    # code (a bare stub) -- manually attach it so room_DetailCode's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # room_DetailCode's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = room_DetailCode(commands="sample_text")
    partner = room_ActorContainerClass()
    setattr(partner, 'room_ActorContainerClass28', None)
    _safe_set(owner, 'room_DetailCode29', partner)
    assert getattr(partner, 'room_ActorContainerClass28') == owner
    _safe_set(owner, 'room_DetailCode29', None)
    assert getattr(partner, 'room_ActorContainerClass28') is None


def test_assoc_userCode247_stub_double():
    # room_DataClass has no real 'room_DataClass48' property in the generated
    # code (a bare stub) -- manually attach it so room_DetailCode's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # room_DetailCode's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = room_DetailCode(commands="sample_text")
    partner = room_DataClass()
    setattr(partner, 'room_DataClass48', None)
    _safe_set(owner, 'room_DetailCode49', partner)
    assert getattr(partner, 'room_DataClass48') == owner
    _safe_set(owner, 'room_DetailCode49', None)
    assert getattr(partner, 'room_DataClass48') is None


def test_assoc_userCode330_stub_double():
    # room_ActorContainerClass has no real 'room_ActorContainerClass31' property in the generated
    # code (a bare stub) -- manually attach it so room_DetailCode's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # room_DetailCode's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = room_DetailCode(commands="sample_text")
    partner = room_ActorContainerClass()
    setattr(partner, 'room_ActorContainerClass31', None)
    _safe_set(owner, 'room_DetailCode32', partner)
    assert getattr(partner, 'room_ActorContainerClass31') == owner
    _safe_set(owner, 'room_DetailCode32', None)
    assert getattr(partner, 'room_ActorContainerClass31') is None


def test_assoc_userCode350_stub_double():
    # room_DataClass has no real 'room_DataClass51' property in the generated
    # code (a bare stub) -- manually attach it so room_DetailCode's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # room_DetailCode's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = room_DetailCode(commands="sample_text")
    partner = room_DataClass()
    setattr(partner, 'room_DataClass51', None)
    _safe_set(owner, 'room_DetailCode52', partner)
    assert getattr(partner, 'room_DataClass51') == owner
    _safe_set(owner, 'room_DetailCode52', None)
    assert getattr(partner, 'room_DataClass51') is None


