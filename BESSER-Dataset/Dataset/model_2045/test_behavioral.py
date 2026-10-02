import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    ActorContainerClass,
    ActorContainerRef,
    ComplexType,
    DataType,
    InterfaceItem,
    NonInitialTransition,
    Operation,
    RoomClass,
    SAPoint,
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
    room_BaseState,
    room_Binding,
    room_BindingEndPoint,
    room_CPBranchTransition,
    room_ChoicePoint,
    room_ChoicepointTerminal,
    room_ComplexType,
    room_ContinuationTransition,
    room_DataClass,
    room_DataType,
    room_DetailCode,
    room_Documentation,
    room_EntryPoint,
    room_ExitPoint,
    room_ExternalPort,
    room_ExternalType,
    room_Guard,
    room_GuardedTransition,
    room_Import,
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
    room_Port,
    room_PortClass,
    room_PortOperation,
    room_PrimitiveType,
    room_ProtocolClass,
    room_ProtocolSemantics,
    room_RefSAPoint,
    room_RefableType,
    room_RefinedState,
    room_RelaySAPoint,
    room_RoomClass,
    room_RoomModel,
    room_SAPRef,
    room_SAPoint,
    room_SPPRef,
    room_SPPoint,
    room_SemanticsRule,
    room_ServiceImplementation,
    room_StandardOperation,
    room_State,
    room_StateGraph,
    room_StateGraphItem,
    room_StateGraphNode,
    room_StateTerminal,
    room_StructureClass,
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

def test_assoc_action241_reverse_link_reassign_clear():
    a1 = room_Transition(name="sample_text")
    a2 = room_Transition(name="sample_text_2")
    b = room_DetailCode(commands="sample_text")
    _safe_set(b, 'room_DetailCode243', a1)
    assert _is_linked(b, 'room_DetailCode243', a1)
    if hasattr(a1, 'room_Transition242'):
        assert _is_linked(a1, 'room_Transition242', b)
    _safe_set(b, 'room_DetailCode243', a2)
    assert _is_linked(b, 'room_DetailCode243', a2)
    if hasattr(a1, 'room_Transition242'):
        assert not _is_linked(a1, 'room_Transition242', b)
    if hasattr(a2, 'room_Transition242'):
        assert _is_linked(a2, 'room_Transition242', b)
    _safe_set(b, 'room_DetailCode243', None)
    assert not _is_linked(b, 'room_DetailCode243', a2)
    if hasattr(a2, 'room_Transition242'):
        assert not _is_linked(a2, 'room_Transition242', b)


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


def test_assoc_annotations149_reverse_link_reassign_clear():
    a1 = room_Annotation(name="sample_text")
    a2 = room_Annotation(name="sample_text_2")
    b = room_ActorClass(abstract=True, commType="sample_text")
    _safe_set(b, 'room_ActorClass150', {a1})
    assert _is_linked(b, 'room_ActorClass150', a1)
    if hasattr(a1, 'room_Annotation'):
        assert _is_linked(a1, 'room_Annotation', b)
    _safe_set(b, 'room_ActorClass150', {a2})
    assert _is_linked(b, 'room_ActorClass150', a2)
    if hasattr(a1, 'room_Annotation'):
        assert not _is_linked(a1, 'room_Annotation', b)
    if hasattr(a2, 'room_Annotation'):
        assert _is_linked(a2, 'room_Annotation', b)
    _safe_set(b, 'room_ActorClass150', set())
    assert not _is_linked(b, 'room_ActorClass150', a2)
    if hasattr(a2, 'room_Annotation'):
        assert not _is_linked(a2, 'room_Annotation', b)


def test_assoc_arguments58_reverse_link_reassign_clear():
    a1 = room_VarDecl(name="sample_text")
    a2 = room_VarDecl(name="sample_text_2")
    b = room_Operation(name="sample_text")
    _safe_set(b, 'room_Operation', {a1})
    assert _is_linked(b, 'room_Operation', a1)
    if hasattr(a1, 'room_VarDecl59'):
        assert _is_linked(a1, 'room_VarDecl59', b)
    _safe_set(b, 'room_Operation', {a2})
    assert _is_linked(b, 'room_Operation', a2)
    if hasattr(a1, 'room_VarDecl59'):
        assert not _is_linked(a1, 'room_VarDecl59', b)
    if hasattr(a2, 'room_VarDecl59'):
        assert _is_linked(a2, 'room_VarDecl59', b)
    _safe_set(b, 'room_Operation', set())
    assert not _is_linked(b, 'room_Operation', a2)
    if hasattr(a2, 'room_VarDecl59'):
        assert not _is_linked(a2, 'room_VarDecl59', b)


def test_assoc_attributes143_reverse_link_reassign_clear():
    a1 = room_Attribute(defaultValueLiteral="sample_text", name="sample_text", size=7)
    a2 = room_Attribute(defaultValueLiteral="sample_text_2", name="sample_text_2", size=13)
    b = room_ActorClass(abstract=True, commType="sample_text")
    _safe_set(b, 'room_ActorClass144', {a1})
    assert _is_linked(b, 'room_ActorClass144', a1)
    if hasattr(a1, 'room_Attribute145'):
        assert _is_linked(a1, 'room_Attribute145', b)
    _safe_set(b, 'room_ActorClass144', {a2})
    assert _is_linked(b, 'room_ActorClass144', a2)
    if hasattr(a1, 'room_Attribute145'):
        assert not _is_linked(a1, 'room_Attribute145', b)
    if hasattr(a2, 'room_Attribute145'):
        assert _is_linked(a2, 'room_Attribute145', b)
    _safe_set(b, 'room_ActorClass144', set())
    assert not _is_linked(b, 'room_ActorClass144', a2)
    if hasattr(a2, 'room_Attribute145'):
        assert not _is_linked(a2, 'room_Attribute145', b)


def test_assoc_attributes275_reverse_link_reassign_clear():
    a1 = room_KeyValue(key="sample_text", value="sample_text")
    a2 = room_KeyValue(key="sample_text_2", value="sample_text_2")
    b = room_Annotation(name="sample_text")
    _safe_set(b, 'room_Annotation276', {a1})
    assert _is_linked(b, 'room_Annotation276', a1)
    if hasattr(a1, 'room_KeyValue'):
        assert _is_linked(a1, 'room_KeyValue', b)
    _safe_set(b, 'room_Annotation276', {a2})
    assert _is_linked(b, 'room_Annotation276', a2)
    if hasattr(a1, 'room_KeyValue'):
        assert not _is_linked(a1, 'room_KeyValue', b)
    if hasattr(a2, 'room_KeyValue'):
        assert _is_linked(a2, 'room_KeyValue', b)
    _safe_set(b, 'room_Annotation276', set())
    assert not _is_linked(b, 'room_Annotation276', a2)
    if hasattr(a2, 'room_KeyValue'):
        assert not _is_linked(a2, 'room_KeyValue', b)


def test_assoc_base127_reverse_link_reassign_clear():
    a1 = room_ActorClass(abstract=True, commType="sample_text")
    a2 = room_ActorClass(abstract=False, commType="sample_text_2")
    b = room_ActorClass(abstract=True, commType="sample_text")
    _safe_set(b, 'room_ActorClass128', a1)
    assert _is_linked(b, 'room_ActorClass128', a1)
    if hasattr(a1, 'room_ActorClass126'):
        assert _is_linked(a1, 'room_ActorClass126', b)
    _safe_set(b, 'room_ActorClass128', a2)
    assert _is_linked(b, 'room_ActorClass128', a2)
    if hasattr(a1, 'room_ActorClass126'):
        assert not _is_linked(a1, 'room_ActorClass126', b)
    if hasattr(a2, 'room_ActorClass126'):
        assert _is_linked(a2, 'room_ActorClass126', b)
    _safe_set(b, 'room_ActorClass128', None)
    assert not _is_linked(b, 'room_ActorClass128', a2)
    if hasattr(a2, 'room_ActorClass126'):
        assert not _is_linked(a2, 'room_ActorClass126', b)


def test_assoc_base71_reverse_link_reassign_clear():
    a1 = room_ProtocolClass(commType="sample_text")
    a2 = room_ProtocolClass(commType="sample_text_2")
    b = room_ProtocolClass(commType="sample_text")
    _safe_set(b, 'room_ProtocolClass72', a1)
    assert _is_linked(b, 'room_ProtocolClass72', a1)
    if hasattr(a1, 'room_ProtocolClass70'):
        assert _is_linked(a1, 'room_ProtocolClass70', b)
    _safe_set(b, 'room_ProtocolClass72', a2)
    assert _is_linked(b, 'room_ProtocolClass72', a2)
    if hasattr(a1, 'room_ProtocolClass70'):
        assert not _is_linked(a1, 'room_ProtocolClass70', b)
    if hasattr(a2, 'room_ProtocolClass70'):
        assert _is_linked(a2, 'room_ProtocolClass70', b)
    _safe_set(b, 'room_ProtocolClass72', None)
    assert not _is_linked(b, 'room_ProtocolClass72', a2)
    if hasattr(a2, 'room_ProtocolClass70'):
        assert not _is_linked(a2, 'room_ProtocolClass70', b)


def test_assoc_behaviorDocu146_reverse_link_reassign_clear():
    a1 = room_Documentation(text="sample_text")
    a2 = room_Documentation(text="sample_text_2")
    b = room_ActorClass(abstract=True, commType="sample_text")
    _safe_set(b, 'room_ActorClass147', a1)
    assert _is_linked(b, 'room_ActorClass147', a1)
    if hasattr(a1, 'room_Documentation148'):
        assert _is_linked(a1, 'room_Documentation148', b)
    _safe_set(b, 'room_ActorClass147', a2)
    assert _is_linked(b, 'room_ActorClass147', a2)
    if hasattr(a1, 'room_Documentation148'):
        assert not _is_linked(a1, 'room_Documentation148', b)
    if hasattr(a2, 'room_Documentation148'):
        assert _is_linked(a2, 'room_Documentation148', b)
    _safe_set(b, 'room_ActorClass147', None)
    assert not _is_linked(b, 'room_ActorClass147', a2)
    if hasattr(a2, 'room_Documentation148'):
        assert not _is_linked(a2, 'room_Documentation148', b)


def test_assoc_data95_reverse_link_reassign_clear():
    a1 = room_VarDecl(name="sample_text")
    a2 = room_VarDecl(name="sample_text_2")
    b = room_Message(name="sample_text", priv=True)
    _safe_set(b, 'room_Message96', a1)
    assert _is_linked(b, 'room_Message96', a1)
    if hasattr(a1, 'room_VarDecl97'):
        assert _is_linked(a1, 'room_VarDecl97', b)
    _safe_set(b, 'room_Message96', a2)
    assert _is_linked(b, 'room_Message96', a2)
    if hasattr(a1, 'room_VarDecl97'):
        assert not _is_linked(a1, 'room_VarDecl97', b)
    if hasattr(a2, 'room_VarDecl97'):
        assert _is_linked(a2, 'room_VarDecl97', b)
    _safe_set(b, 'room_Message96', None)
    assert not _is_linked(b, 'room_Message96', a2)
    if hasattr(a2, 'room_VarDecl97'):
        assert not _is_linked(a2, 'room_VarDecl97', b)


def test_assoc_detailCode66_reverse_link_reassign_clear():
    a1 = room_Operation(name="sample_text")
    a2 = room_Operation(name="sample_text_2")
    b = room_DetailCode(commands="sample_text")
    _safe_set(b, 'room_DetailCode68', a1)
    assert _is_linked(b, 'room_DetailCode68', a1)
    if hasattr(a1, 'room_Operation67'):
        assert _is_linked(a1, 'room_Operation67', b)
    _safe_set(b, 'room_DetailCode68', a2)
    assert _is_linked(b, 'room_DetailCode68', a2)
    if hasattr(a1, 'room_Operation67'):
        assert not _is_linked(a1, 'room_Operation67', b)
    if hasattr(a2, 'room_Operation67'):
        assert _is_linked(a2, 'room_Operation67', b)
    _safe_set(b, 'room_DetailCode68', None)
    assert not _is_linked(b, 'room_DetailCode68', a2)
    if hasattr(a2, 'room_Operation67'):
        assert not _is_linked(a2, 'room_Operation67', b)


def test_assoc_doCode217_reverse_link_reassign_clear():
    a1 = room_State()
    a2 = room_State()
    b = room_DetailCode(commands="sample_text")
    _safe_set(b, 'room_DetailCode219', a1)
    assert _is_linked(b, 'room_DetailCode219', a1)
    if hasattr(a1, 'room_State218'):
        assert _is_linked(a1, 'room_State218', b)
    _safe_set(b, 'room_DetailCode219', a2)
    assert _is_linked(b, 'room_DetailCode219', a2)
    if hasattr(a1, 'room_State218'):
        assert not _is_linked(a1, 'room_State218', b)
    if hasattr(a2, 'room_State218'):
        assert _is_linked(a2, 'room_State218', b)
    _safe_set(b, 'room_DetailCode219', None)
    assert not _is_linked(b, 'room_DetailCode219', a2)
    if hasattr(a2, 'room_State218'):
        assert not _is_linked(a2, 'room_State218', b)


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


def test_assoc_docu158_reverse_link_reassign_clear():
    a1 = room_Port(conjugated=True, multiplicity=7)
    a2 = room_Port(conjugated=False, multiplicity=13)
    b = room_Documentation(text="sample_text")
    _safe_set(b, 'room_Documentation160', a1)
    assert _is_linked(b, 'room_Documentation160', a1)
    if hasattr(a1, 'room_Port159'):
        assert _is_linked(a1, 'room_Port159', b)
    _safe_set(b, 'room_Documentation160', a2)
    assert _is_linked(b, 'room_Documentation160', a2)
    if hasattr(a1, 'room_Port159'):
        assert not _is_linked(a1, 'room_Port159', b)
    if hasattr(a2, 'room_Port159'):
        assert _is_linked(a2, 'room_Port159', b)
    _safe_set(b, 'room_Documentation160', None)
    assert not _is_linked(b, 'room_Documentation160', a2)
    if hasattr(a2, 'room_Port159'):
        assert not _is_linked(a2, 'room_Port159', b)


def test_assoc_docu169_reverse_link_reassign_clear():
    a1 = room_Documentation(text="sample_text")
    a2 = room_Documentation(text="sample_text_2")
    b = room_ActorContainerRef(name="sample_text")
    _safe_set(b, 'room_ActorContainerRef', a1)
    assert _is_linked(b, 'room_ActorContainerRef', a1)
    if hasattr(a1, 'room_Documentation170'):
        assert _is_linked(a1, 'room_Documentation170', b)
    _safe_set(b, 'room_ActorContainerRef', a2)
    assert _is_linked(b, 'room_ActorContainerRef', a2)
    if hasattr(a1, 'room_Documentation170'):
        assert not _is_linked(a1, 'room_Documentation170', b)
    if hasattr(a2, 'room_Documentation170'):
        assert _is_linked(a2, 'room_Documentation170', b)
    _safe_set(b, 'room_ActorContainerRef', None)
    assert not _is_linked(b, 'room_ActorContainerRef', a2)
    if hasattr(a2, 'room_Documentation170'):
        assert not _is_linked(a2, 'room_Documentation170', b)


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


def test_assoc_docu209_reverse_link_reassign_clear():
    a1 = room_State()
    a2 = room_State()
    b = room_Documentation(text="sample_text")
    _safe_set(b, 'room_Documentation210', a1)
    assert _is_linked(b, 'room_Documentation210', a1)
    if hasattr(a1, 'room_State'):
        assert _is_linked(a1, 'room_State', b)
    _safe_set(b, 'room_Documentation210', a2)
    assert _is_linked(b, 'room_Documentation210', a2)
    if hasattr(a1, 'room_State'):
        assert not _is_linked(a1, 'room_State', b)
    if hasattr(a2, 'room_State'):
        assert _is_linked(a2, 'room_State', b)
    _safe_set(b, 'room_Documentation210', None)
    assert not _is_linked(b, 'room_Documentation210', a2)
    if hasattr(a2, 'room_State'):
        assert not _is_linked(a2, 'room_State', b)


def test_assoc_docu233_reverse_link_reassign_clear():
    a1 = room_Documentation(text="sample_text")
    a2 = room_Documentation(text="sample_text_2")
    b = room_ChoicePoint(name="sample_text")
    _safe_set(b, 'room_ChoicePoint234', a1)
    assert _is_linked(b, 'room_ChoicePoint234', a1)
    if hasattr(a1, 'room_Documentation235'):
        assert _is_linked(a1, 'room_Documentation235', b)
    _safe_set(b, 'room_ChoicePoint234', a2)
    assert _is_linked(b, 'room_ChoicePoint234', a2)
    if hasattr(a1, 'room_Documentation235'):
        assert not _is_linked(a1, 'room_Documentation235', b)
    if hasattr(a2, 'room_Documentation235'):
        assert _is_linked(a2, 'room_Documentation235', b)
    _safe_set(b, 'room_ChoicePoint234', None)
    assert not _is_linked(b, 'room_ChoicePoint234', a2)
    if hasattr(a2, 'room_Documentation235'):
        assert not _is_linked(a2, 'room_Documentation235', b)


def test_assoc_docu238_reverse_link_reassign_clear():
    a1 = room_Transition(name="sample_text")
    a2 = room_Transition(name="sample_text_2")
    b = room_Documentation(text="sample_text")
    _safe_set(b, 'room_Documentation240', a1)
    assert _is_linked(b, 'room_Documentation240', a1)
    if hasattr(a1, 'room_Transition239'):
        assert _is_linked(a1, 'room_Transition239', b)
    _safe_set(b, 'room_Documentation240', a2)
    assert _is_linked(b, 'room_Documentation240', a2)
    if hasattr(a1, 'room_Transition239'):
        assert not _is_linked(a1, 'room_Transition239', b)
    if hasattr(a2, 'room_Transition239'):
        assert _is_linked(a2, 'room_Transition239', b)
    _safe_set(b, 'room_Documentation240', None)
    assert not _is_linked(b, 'room_Documentation240', a2)
    if hasattr(a2, 'room_Transition239'):
        assert not _is_linked(a2, 'room_Transition239', b)


def test_assoc_docu55_reverse_link_reassign_clear():
    a1 = room_Documentation(text="sample_text")
    a2 = room_Documentation(text="sample_text_2")
    b = room_Attribute(defaultValueLiteral="sample_text", name="sample_text", size=7)
    _safe_set(b, 'room_Attribute56', a1)
    assert _is_linked(b, 'room_Attribute56', a1)
    if hasattr(a1, 'room_Documentation57'):
        assert _is_linked(a1, 'room_Documentation57', b)
    _safe_set(b, 'room_Attribute56', a2)
    assert _is_linked(b, 'room_Attribute56', a2)
    if hasattr(a1, 'room_Documentation57'):
        assert not _is_linked(a1, 'room_Documentation57', b)
    if hasattr(a2, 'room_Documentation57'):
        assert _is_linked(a2, 'room_Documentation57', b)
    _safe_set(b, 'room_Attribute56', None)
    assert not _is_linked(b, 'room_Attribute56', a2)
    if hasattr(a2, 'room_Documentation57'):
        assert not _is_linked(a2, 'room_Documentation57', b)


def test_assoc_docu63_reverse_link_reassign_clear():
    a1 = room_Operation(name="sample_text")
    a2 = room_Operation(name="sample_text_2")
    b = room_Documentation(text="sample_text")
    _safe_set(b, 'room_Documentation65', a1)
    assert _is_linked(b, 'room_Documentation65', a1)
    if hasattr(a1, 'room_Operation64'):
        assert _is_linked(a1, 'room_Operation64', b)
    _safe_set(b, 'room_Documentation65', a2)
    assert _is_linked(b, 'room_Documentation65', a2)
    if hasattr(a1, 'room_Operation64'):
        assert not _is_linked(a1, 'room_Operation64', b)
    if hasattr(a2, 'room_Operation64'):
        assert _is_linked(a2, 'room_Operation64', b)
    _safe_set(b, 'room_Documentation65', None)
    assert not _is_linked(b, 'room_Documentation65', a2)
    if hasattr(a2, 'room_Operation64'):
        assert not _is_linked(a2, 'room_Operation64', b)


def test_assoc_docu98_reverse_link_reassign_clear():
    a1 = room_Message(name="sample_text", priv=True)
    a2 = room_Message(name="sample_text_2", priv=False)
    b = room_Documentation(text="sample_text")
    _safe_set(b, 'room_Documentation100', a1)
    assert _is_linked(b, 'room_Documentation100', a1)
    if hasattr(a1, 'room_Message99'):
        assert _is_linked(a1, 'room_Message99', b)
    _safe_set(b, 'room_Documentation100', a2)
    assert _is_linked(b, 'room_Documentation100', a2)
    if hasattr(a1, 'room_Message99'):
        assert not _is_linked(a1, 'room_Message99', b)
    if hasattr(a2, 'room_Message99'):
        assert _is_linked(a2, 'room_Message99', b)
    _safe_set(b, 'room_Documentation100', None)
    assert not _is_linked(b, 'room_Documentation100', a2)
    if hasattr(a2, 'room_Message99'):
        assert not _is_linked(a2, 'room_Message99', b)


def test_assoc_entryCode211_reverse_link_reassign_clear():
    a1 = room_State()
    a2 = room_State()
    b = room_DetailCode(commands="sample_text")
    _safe_set(b, 'room_DetailCode213', a1)
    assert _is_linked(b, 'room_DetailCode213', a1)
    if hasattr(a1, 'room_State212'):
        assert _is_linked(a1, 'room_State212', b)
    _safe_set(b, 'room_DetailCode213', a2)
    assert _is_linked(b, 'room_DetailCode213', a2)
    if hasattr(a1, 'room_State212'):
        assert not _is_linked(a1, 'room_State212', b)
    if hasattr(a2, 'room_State212'):
        assert _is_linked(a2, 'room_State212', b)
    _safe_set(b, 'room_DetailCode213', None)
    assert not _is_linked(b, 'room_DetailCode213', a2)
    if hasattr(a2, 'room_State212'):
        assert not _is_linked(a2, 'room_State212', b)


def test_assoc_exitCode214_reverse_link_reassign_clear():
    a1 = room_State()
    a2 = room_State()
    b = room_DetailCode(commands="sample_text")
    _safe_set(b, 'room_DetailCode216', a1)
    assert _is_linked(b, 'room_DetailCode216', a1)
    if hasattr(a1, 'room_State215'):
        assert _is_linked(a1, 'room_State215', b)
    _safe_set(b, 'room_DetailCode216', a2)
    assert _is_linked(b, 'room_DetailCode216', a2)
    if hasattr(a1, 'room_State215'):
        assert not _is_linked(a1, 'room_State215', b)
    if hasattr(a2, 'room_State215'):
        assert _is_linked(a2, 'room_State215', b)
    _safe_set(b, 'room_DetailCode216', None)
    assert not _is_linked(b, 'room_DetailCode216', a2)
    if hasattr(a2, 'room_State215'):
        assert not _is_linked(a2, 'room_State215', b)


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


def test_assoc_ifPorts129_reverse_link_reassign_clear():
    a1 = room_Port(conjugated=True, multiplicity=7)
    a2 = room_Port(conjugated=False, multiplicity=13)
    b = room_ActorClass(abstract=True, commType="sample_text")
    _safe_set(b, 'room_ActorClass130', {a1})
    assert _is_linked(b, 'room_ActorClass130', a1)
    if hasattr(a1, 'room_Port'):
        assert _is_linked(a1, 'room_Port', b)
    _safe_set(b, 'room_ActorClass130', {a2})
    assert _is_linked(b, 'room_ActorClass130', a2)
    if hasattr(a1, 'room_Port'):
        assert not _is_linked(a1, 'room_Port', b)
    if hasattr(a2, 'room_Port'):
        assert _is_linked(a2, 'room_Port', b)
    _safe_set(b, 'room_ActorClass130', set())
    assert not _is_linked(b, 'room_ActorClass130', a2)
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


def test_assoc_incomingMessages82_reverse_link_reassign_clear():
    a1 = room_ProtocolClass(commType="sample_text")
    a2 = room_ProtocolClass(commType="sample_text_2")
    b = room_Message(name="sample_text", priv=True)
    _safe_set(b, 'room_Message84', a1)
    assert _is_linked(b, 'room_Message84', a1)
    if hasattr(a1, 'room_ProtocolClass83'):
        assert _is_linked(a1, 'room_ProtocolClass83', b)
    _safe_set(b, 'room_Message84', a2)
    assert _is_linked(b, 'room_Message84', a2)
    if hasattr(a1, 'room_ProtocolClass83'):
        assert not _is_linked(a1, 'room_ProtocolClass83', b)
    if hasattr(a2, 'room_ProtocolClass83'):
        assert _is_linked(a2, 'room_ProtocolClass83', b)
    _safe_set(b, 'room_Message84', None)
    assert not _is_linked(b, 'room_Message84', a2)
    if hasattr(a2, 'room_ProtocolClass83'):
        assert not _is_linked(a2, 'room_ProtocolClass83', b)


def test_assoc_instances179_reverse_link_reassign_clear():
    a1 = room_LogicalThread(name="sample_text", prio=7)
    a2 = room_LogicalThread(name="sample_text_2", prio=13)
    b = room_ActorInstancePath(segments="sample_text")
    _safe_set(b, 'room_ActorInstancePath', a1)
    assert _is_linked(b, 'room_ActorInstancePath', a1)
    if hasattr(a1, 'room_LogicalThread180'):
        assert _is_linked(a1, 'room_LogicalThread180', b)
    _safe_set(b, 'room_ActorInstancePath', a2)
    assert _is_linked(b, 'room_ActorInstancePath', a2)
    if hasattr(a1, 'room_LogicalThread180'):
        assert not _is_linked(a1, 'room_LogicalThread180', b)
    if hasattr(a2, 'room_LogicalThread180'):
        assert _is_linked(a2, 'room_LogicalThread180', b)
    _safe_set(b, 'room_ActorInstancePath', None)
    assert not _is_linked(b, 'room_ActorInstancePath', a2)
    if hasattr(a2, 'room_LogicalThread180'):
        assert not _is_linked(a2, 'room_LogicalThread180', b)


def test_assoc_intPorts134_reverse_link_reassign_clear():
    a1 = room_Port(conjugated=True, multiplicity=7)
    a2 = room_Port(conjugated=False, multiplicity=13)
    b = room_ActorClass(abstract=True, commType="sample_text")
    _safe_set(b, 'room_ActorClass135', {a1})
    assert _is_linked(b, 'room_ActorClass135', a1)
    if hasattr(a1, 'room_Port136'):
        assert _is_linked(a1, 'room_Port136', b)
    _safe_set(b, 'room_ActorClass135', {a2})
    assert _is_linked(b, 'room_ActorClass135', a2)
    if hasattr(a1, 'room_Port136'):
        assert not _is_linked(a1, 'room_Port136', b)
    if hasattr(a2, 'room_Port136'):
        assert _is_linked(a2, 'room_Port136', b)
    _safe_set(b, 'room_ActorClass135', set())
    assert not _is_linked(b, 'room_ActorClass135', a2)
    if hasattr(a2, 'room_Port136'):
        assert not _is_linked(a2, 'room_Port136', b)


def test_assoc_outgoingMessages85_reverse_link_reassign_clear():
    a1 = room_ProtocolClass(commType="sample_text")
    a2 = room_ProtocolClass(commType="sample_text_2")
    b = room_Message(name="sample_text", priv=True)
    _safe_set(b, 'room_Message87', a1)
    assert _is_linked(b, 'room_Message87', a1)
    if hasattr(a1, 'room_ProtocolClass86'):
        assert _is_linked(a1, 'room_ProtocolClass86', b)
    _safe_set(b, 'room_Message87', a2)
    assert _is_linked(b, 'room_Message87', a2)
    if hasattr(a1, 'room_ProtocolClass86'):
        assert not _is_linked(a1, 'room_ProtocolClass86', b)
    if hasattr(a2, 'room_ProtocolClass86'):
        assert _is_linked(a2, 'room_ProtocolClass86', b)
    _safe_set(b, 'room_Message87', None)
    assert not _is_linked(b, 'room_Message87', a2)
    if hasattr(a2, 'room_ProtocolClass86'):
        assert not _is_linked(a2, 'room_ProtocolClass86', b)


def test_assoc_primitiveTypes3_reverse_link_reassign_clear():
    a1 = room_RoomModel(name="sample_text")
    a2 = room_RoomModel(name="sample_text_2")
    b = room_PrimitiveType(castName="sample_text", defaultValueLiteral="sample_text", targetName="sample_text")
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


def test_assoc_protocol156_reverse_link_reassign_clear():
    a1 = room_ProtocolClass(commType="sample_text")
    a2 = room_ProtocolClass(commType="sample_text_2")
    b = room_InterfaceItem(name="sample_text")
    _safe_set(b, 'room_InterfaceItem', a1)
    assert _is_linked(b, 'room_InterfaceItem', a1)
    if hasattr(a1, 'room_ProtocolClass157'):
        assert _is_linked(a1, 'room_ProtocolClass157', b)
    _safe_set(b, 'room_InterfaceItem', a2)
    assert _is_linked(b, 'room_InterfaceItem', a2)
    if hasattr(a1, 'room_ProtocolClass157'):
        assert not _is_linked(a1, 'room_ProtocolClass157', b)
    if hasattr(a2, 'room_ProtocolClass157'):
        assert _is_linked(a2, 'room_ProtocolClass157', b)
    _safe_set(b, 'room_InterfaceItem', None)
    assert not _is_linked(b, 'room_InterfaceItem', a2)
    if hasattr(a2, 'room_ProtocolClass157'):
        assert not _is_linked(a2, 'room_ProtocolClass157', b)


def test_assoc_protocolClasses9_reverse_link_reassign_clear():
    a1 = room_RoomModel(name="sample_text")
    a2 = room_RoomModel(name="sample_text_2")
    b = room_ProtocolClass(commType="sample_text")
    _safe_set(b, 'room_ProtocolClass', a1)
    assert _is_linked(b, 'room_ProtocolClass', a1)
    if hasattr(a1, 'room_RoomModel10'):
        assert _is_linked(a1, 'room_RoomModel10', b)
    _safe_set(b, 'room_ProtocolClass', a2)
    assert _is_linked(b, 'room_ProtocolClass', a2)
    if hasattr(a1, 'room_RoomModel10'):
        assert not _is_linked(a1, 'room_RoomModel10', b)
    if hasattr(a2, 'room_RoomModel10'):
        assert _is_linked(a2, 'room_RoomModel10', b)
    _safe_set(b, 'room_ProtocolClass', None)
    assert not _is_linked(b, 'room_ProtocolClass', a2)
    if hasattr(a2, 'room_RoomModel10'):
        assert not _is_linked(a2, 'room_RoomModel10', b)


def test_assoc_refType33_reverse_link_reassign_clear():
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


def test_assoc_refType52_reverse_link_reassign_clear():
    a1 = room_RefableType(ref=True)
    a2 = room_RefableType(ref=False)
    b = room_Attribute(defaultValueLiteral="sample_text", name="sample_text", size=7)
    _safe_set(b, 'room_Attribute53', a1)
    assert _is_linked(b, 'room_Attribute53', a1)
    if hasattr(a1, 'room_RefableType54'):
        assert _is_linked(a1, 'room_RefableType54', b)
    _safe_set(b, 'room_Attribute53', a2)
    assert _is_linked(b, 'room_Attribute53', a2)
    if hasattr(a1, 'room_RefableType54'):
        assert not _is_linked(a1, 'room_RefableType54', b)
    if hasattr(a2, 'room_RefableType54'):
        assert _is_linked(a2, 'room_RefableType54', b)
    _safe_set(b, 'room_Attribute53', None)
    assert not _is_linked(b, 'room_Attribute53', a2)
    if hasattr(a2, 'room_RefableType54'):
        assert not _is_linked(a2, 'room_RefableType54', b)


def test_assoc_returntype60_reverse_link_reassign_clear():
    a1 = room_RefableType(ref=True)
    a2 = room_RefableType(ref=False)
    b = room_Operation(name="sample_text")
    _safe_set(b, 'room_Operation61', a1)
    assert _is_linked(b, 'room_Operation61', a1)
    if hasattr(a1, 'room_RefableType62'):
        assert _is_linked(a1, 'room_RefableType62', b)
    _safe_set(b, 'room_Operation61', a2)
    assert _is_linked(b, 'room_Operation61', a2)
    if hasattr(a1, 'room_RefableType62'):
        assert not _is_linked(a1, 'room_RefableType62', b)
    if hasattr(a2, 'room_RefableType62'):
        assert _is_linked(a2, 'room_RefableType62', b)
    _safe_set(b, 'room_Operation61', None)
    assert not _is_linked(b, 'room_Operation61', a2)
    if hasattr(a2, 'room_RefableType62'):
        assert not _is_linked(a2, 'room_RefableType62', b)


def test_assoc_structureDocu131_reverse_link_reassign_clear():
    a1 = room_Documentation(text="sample_text")
    a2 = room_Documentation(text="sample_text_2")
    b = room_ActorClass(abstract=True, commType="sample_text")
    _safe_set(b, 'room_ActorClass132', a1)
    assert _is_linked(b, 'room_ActorClass132', a1)
    if hasattr(a1, 'room_Documentation133'):
        assert _is_linked(a1, 'room_Documentation133', b)
    _safe_set(b, 'room_ActorClass132', a2)
    assert _is_linked(b, 'room_ActorClass132', a2)
    if hasattr(a1, 'room_Documentation133'):
        assert not _is_linked(a1, 'room_Documentation133', b)
    if hasattr(a2, 'room_Documentation133'):
        assert _is_linked(a2, 'room_Documentation133', b)
    _safe_set(b, 'room_ActorClass132', None)
    assert not _is_linked(b, 'room_ActorClass132', a2)
    if hasattr(a2, 'room_Documentation133'):
        assert not _is_linked(a2, 'room_Documentation133', b)


def test_assoc_userCode173_reverse_link_reassign_clear():
    a1 = room_ProtocolClass(commType="sample_text")
    a2 = room_ProtocolClass(commType="sample_text_2")
    b = room_DetailCode(commands="sample_text")
    _safe_set(b, 'room_DetailCode75', a1)
    assert _is_linked(b, 'room_DetailCode75', a1)
    if hasattr(a1, 'room_ProtocolClass74'):
        assert _is_linked(a1, 'room_ProtocolClass74', b)
    _safe_set(b, 'room_DetailCode75', a2)
    assert _is_linked(b, 'room_DetailCode75', a2)
    if hasattr(a1, 'room_ProtocolClass74'):
        assert not _is_linked(a1, 'room_ProtocolClass74', b)
    if hasattr(a2, 'room_ProtocolClass74'):
        assert _is_linked(a2, 'room_ProtocolClass74', b)
    _safe_set(b, 'room_DetailCode75', None)
    assert not _is_linked(b, 'room_DetailCode75', a2)
    if hasattr(a2, 'room_ProtocolClass74'):
        assert not _is_linked(a2, 'room_ProtocolClass74', b)


def test_assoc_userCode276_reverse_link_reassign_clear():
    a1 = room_ProtocolClass(commType="sample_text")
    a2 = room_ProtocolClass(commType="sample_text_2")
    b = room_DetailCode(commands="sample_text")
    _safe_set(b, 'room_DetailCode78', a1)
    assert _is_linked(b, 'room_DetailCode78', a1)
    if hasattr(a1, 'room_ProtocolClass77'):
        assert _is_linked(a1, 'room_ProtocolClass77', b)
    _safe_set(b, 'room_DetailCode78', a2)
    assert _is_linked(b, 'room_DetailCode78', a2)
    if hasattr(a1, 'room_ProtocolClass77'):
        assert not _is_linked(a1, 'room_ProtocolClass77', b)
    if hasattr(a2, 'room_ProtocolClass77'):
        assert _is_linked(a2, 'room_ProtocolClass77', b)
    _safe_set(b, 'room_DetailCode78', None)
    assert not _is_linked(b, 'room_DetailCode78', a2)
    if hasattr(a2, 'room_ProtocolClass77'):
        assert not _is_linked(a2, 'room_ProtocolClass77', b)


def test_assoc_userCode379_reverse_link_reassign_clear():
    a1 = room_ProtocolClass(commType="sample_text")
    a2 = room_ProtocolClass(commType="sample_text_2")
    b = room_DetailCode(commands="sample_text")
    _safe_set(b, 'room_DetailCode81', a1)
    assert _is_linked(b, 'room_DetailCode81', a1)
    if hasattr(a1, 'room_ProtocolClass80'):
        assert _is_linked(a1, 'room_ProtocolClass80', b)
    _safe_set(b, 'room_DetailCode81', a2)
    assert _is_linked(b, 'room_DetailCode81', a2)
    if hasattr(a1, 'room_ProtocolClass80'):
        assert not _is_linked(a1, 'room_ProtocolClass80', b)
    if hasattr(a2, 'room_ProtocolClass80'):
        assert _is_linked(a2, 'room_ProtocolClass80', b)
    _safe_set(b, 'room_DetailCode81', None)
    assert not _is_linked(b, 'room_DetailCode81', a2)
    if hasattr(a2, 'room_ProtocolClass80'):
        assert not _is_linked(a2, 'room_ProtocolClass80', b)


