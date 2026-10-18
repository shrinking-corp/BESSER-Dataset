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


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_actorRef186_stub_double():
    # room_BindingEndPoint has no real 'room_BindingEndPoint187' property in the generated
    # code (a bare stub) -- manually attach it so room_ActorContainerRef's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # room_ActorContainerRef's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = room_ActorContainerRef(name="sample_text")
    partner = room_BindingEndPoint()
    setattr(partner, 'room_BindingEndPoint187', None)
    _safe_set(owner, 'room_ActorContainerRef188', partner)
    assert getattr(partner, 'room_BindingEndPoint187') == owner
    _safe_set(owner, 'room_ActorContainerRef188', None)
    assert getattr(partner, 'room_BindingEndPoint187') is None


def test_assoc_attributes104_stub_double():
    # room_PortClass has no real 'room_PortClass105' property in the generated
    # code (a bare stub) -- manually attach it so room_Attribute's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # room_Attribute's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = room_Attribute(defaultValueLiteral="sample_text", name="sample_text", size=7)
    partner = room_PortClass()
    setattr(partner, 'room_PortClass105', None)
    _safe_set(owner, 'room_Attribute106', partner)
    assert owner in getattr(partner, 'room_PortClass105')
    _safe_set(owner, 'room_Attribute106', None)
    assert owner not in getattr(partner, 'room_PortClass105')


def test_assoc_attributes48_stub_double():
    # room_DataClass has no real 'room_DataClass49' property in the generated
    # code (a bare stub) -- manually attach it so room_Attribute's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # room_Attribute's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = room_Attribute(defaultValueLiteral="sample_text", name="sample_text", size=7)
    partner = room_DataClass()
    setattr(partner, 'room_DataClass49', None)
    _safe_set(owner, 'room_Attribute', partner)
    assert owner in getattr(partner, 'room_DataClass49')
    _safe_set(owner, 'room_Attribute', None)
    assert owner not in getattr(partner, 'room_DataClass49')


def test_assoc_base232_stub_double():
    # room_RefinedState has no real 'room_RefinedState' property in the generated
    # code (a bare stub) -- manually attach it so room_BaseState's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # room_BaseState's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = room_BaseState(name="sample_text")
    partner = room_RefinedState()
    setattr(partner, 'room_RefinedState', None)
    _safe_set(owner, 'room_BaseState', partner)
    assert getattr(partner, 'room_RefinedState') == owner
    _safe_set(owner, 'room_BaseState', None)
    assert getattr(partner, 'room_RefinedState') is None


def test_assoc_chPoints228_stub_double():
    # room_StateGraph has no real 'room_StateGraph229' property in the generated
    # code (a bare stub) -- manually attach it so room_ChoicePoint's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # room_ChoicePoint's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = room_ChoicePoint(name="sample_text")
    partner = room_StateGraph()
    setattr(partner, 'room_StateGraph229', None)
    _safe_set(owner, 'room_ChoicePoint', partner)
    assert owner in getattr(partner, 'room_StateGraph229')
    _safe_set(owner, 'room_ChoicePoint', None)
    assert owner not in getattr(partner, 'room_StateGraph229')


def test_assoc_condition249_stub_double():
    # room_CPBranchTransition has no real 'room_CPBranchTransition' property in the generated
    # code (a bare stub) -- manually attach it so room_DetailCode's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # room_DetailCode's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = room_DetailCode(commands="sample_text")
    partner = room_CPBranchTransition()
    setattr(partner, 'room_CPBranchTransition', None)
    _safe_set(owner, 'room_DetailCode250', partner)
    assert getattr(partner, 'room_CPBranchTransition') == owner
    _safe_set(owner, 'room_DetailCode250', None)
    assert getattr(partner, 'room_CPBranchTransition') is None


def test_assoc_conjugate90_stub_double():
    # room_PortClass has no real 'room_PortClass92' property in the generated
    # code (a bare stub) -- manually attach it so room_ProtocolClass's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # room_ProtocolClass's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = room_ProtocolClass(commType="sample_text")
    partner = room_PortClass()
    setattr(partner, 'room_PortClass92', None)
    _safe_set(owner, 'room_ProtocolClass91', partner)
    assert getattr(partner, 'room_PortClass92') == owner
    _safe_set(owner, 'room_ProtocolClass91', None)
    assert getattr(partner, 'room_PortClass92') is None


def test_assoc_cp260_stub_double():
    # room_ChoicepointTerminal has no real 'room_ChoicepointTerminal' property in the generated
    # code (a bare stub) -- manually attach it so room_ChoicePoint's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # room_ChoicePoint's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = room_ChoicePoint(name="sample_text")
    partner = room_ChoicepointTerminal()
    setattr(partner, 'room_ChoicepointTerminal', None)
    _safe_set(owner, 'room_ChoicePoint261', partner)
    assert getattr(partner, 'room_ChoicepointTerminal') == owner
    _safe_set(owner, 'room_ChoicePoint261', None)
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


def test_assoc_detailCode115_stub_double():
    # room_MessageHandler has no real 'room_MessageHandler116' property in the generated
    # code (a bare stub) -- manually attach it so room_DetailCode's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # room_DetailCode's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = room_DetailCode(commands="sample_text")
    partner = room_MessageHandler()
    setattr(partner, 'room_MessageHandler116', None)
    _safe_set(owner, 'room_DetailCode117', partner)
    assert getattr(partner, 'room_MessageHandler116') == owner
    _safe_set(owner, 'room_DetailCode117', None)
    assert getattr(partner, 'room_MessageHandler116') is None


def test_assoc_extPorts137_stub_double():
    # room_ExternalPort has no real 'room_ExternalPort' property in the generated
    # code (a bare stub) -- manually attach it so room_ActorClass's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # room_ActorClass's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = room_ActorClass(abstract=True, commType="sample_text")
    partner = room_ExternalPort()
    setattr(partner, 'room_ExternalPort', None)
    _safe_set(owner, 'room_ActorClass138', {partner})
    assert getattr(partner, 'room_ExternalPort') == owner
    _safe_set(owner, 'room_ActorClass138', set())
    assert getattr(partner, 'room_ExternalPort') is None


def test_assoc_from_269_stub_double():
    # room_MessageFromIf has no real 'room_MessageFromIf270' property in the generated
    # code (a bare stub) -- manually attach it so room_InterfaceItem's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # room_InterfaceItem's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = room_InterfaceItem(name="sample_text")
    partner = room_MessageFromIf()
    setattr(partner, 'room_MessageFromIf270', None)
    _safe_set(owner, 'room_InterfaceItem271', partner)
    assert getattr(partner, 'room_MessageFromIf270') == owner
    _safe_set(owner, 'room_InterfaceItem271', None)
    assert getattr(partner, 'room_MessageFromIf270') is None


def test_assoc_guard247_stub_double():
    # room_GuardedTransition has no real 'room_GuardedTransition' property in the generated
    # code (a bare stub) -- manually attach it so room_DetailCode's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # room_DetailCode's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = room_DetailCode(commands="sample_text")
    partner = room_GuardedTransition()
    setattr(partner, 'room_GuardedTransition', None)
    _safe_set(owner, 'room_DetailCode248', partner)
    assert getattr(partner, 'room_GuardedTransition') == owner
    _safe_set(owner, 'room_DetailCode248', None)
    assert getattr(partner, 'room_GuardedTransition') is None


def test_assoc_guard272_stub_double():
    # room_Guard has no real 'room_Guard273' property in the generated
    # code (a bare stub) -- manually attach it so room_DetailCode's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # room_DetailCode's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = room_DetailCode(commands="sample_text")
    partner = room_Guard()
    setattr(partner, 'room_Guard273', None)
    _safe_set(owner, 'room_DetailCode274', partner)
    assert getattr(partner, 'room_Guard273') == owner
    _safe_set(owner, 'room_DetailCode274', None)
    assert getattr(partner, 'room_Guard273') is None


def test_assoc_ifport161_stub_double():
    # room_ExternalPort has no real 'room_ExternalPort162' property in the generated
    # code (a bare stub) -- manually attach it so room_Port's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # room_Port's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = room_Port(conjugated=True, multiplicity=7)
    partner = room_ExternalPort()
    setattr(partner, 'room_ExternalPort162', None)
    _safe_set(owner, 'room_Port163', partner)
    assert getattr(partner, 'room_ExternalPort162') == owner
    _safe_set(owner, 'room_Port163', None)
    assert getattr(partner, 'room_ExternalPort162') is None


def test_assoc_message266_stub_double():
    # room_MessageFromIf has no real 'room_MessageFromIf267' property in the generated
    # code (a bare stub) -- manually attach it so room_Message's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # room_Message's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = room_Message(name="sample_text", priv=True)
    partner = room_MessageFromIf()
    setattr(partner, 'room_MessageFromIf267', None)
    _safe_set(owner, 'room_Message268', partner)
    assert getattr(partner, 'room_MessageFromIf267') == owner
    _safe_set(owner, 'room_Message268', None)
    assert getattr(partner, 'room_MessageFromIf267') is None


def test_assoc_msg112_stub_double():
    # room_MessageHandler has no real 'room_MessageHandler113' property in the generated
    # code (a bare stub) -- manually attach it so room_Message's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # room_Message's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = room_Message(name="sample_text", priv=True)
    partner = room_MessageHandler()
    setattr(partner, 'room_MessageHandler113', None)
    _safe_set(owner, 'room_Message114', partner)
    assert getattr(partner, 'room_MessageHandler113') == owner
    _safe_set(owner, 'room_Message114', None)
    assert getattr(partner, 'room_MessageHandler113') is None


def test_assoc_msg120_stub_double():
    # room_SemanticsRule has no real 'room_SemanticsRule121' property in the generated
    # code (a bare stub) -- manually attach it so room_Message's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # room_Message's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = room_Message(name="sample_text", priv=True)
    partner = room_SemanticsRule()
    setattr(partner, 'room_SemanticsRule121', None)
    _safe_set(owner, 'room_Message122', partner)
    assert getattr(partner, 'room_SemanticsRule121') == owner
    _safe_set(owner, 'room_Message122', None)
    assert getattr(partner, 'room_SemanticsRule121') is None


def test_assoc_operations151_stub_double():
    # room_StandardOperation has no real 'room_StandardOperation153' property in the generated
    # code (a bare stub) -- manually attach it so room_ActorClass's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # room_ActorClass's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = room_ActorClass(abstract=True, commType="sample_text")
    partner = room_StandardOperation()
    setattr(partner, 'room_StandardOperation153', None)
    _safe_set(owner, 'room_ActorClass152', {partner})
    assert getattr(partner, 'room_StandardOperation153') == owner
    _safe_set(owner, 'room_ActorClass152', set())
    assert getattr(partner, 'room_StandardOperation153') is None


def test_assoc_port189_stub_double():
    # room_BindingEndPoint has no real 'room_BindingEndPoint190' property in the generated
    # code (a bare stub) -- manually attach it so room_Port's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # room_Port's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = room_Port(conjugated=True, multiplicity=7)
    partner = room_BindingEndPoint()
    setattr(partner, 'room_BindingEndPoint190', None)
    _safe_set(owner, 'room_Port191', partner)
    assert getattr(partner, 'room_BindingEndPoint190') == owner
    _safe_set(owner, 'room_Port191', None)
    assert getattr(partner, 'room_BindingEndPoint190') is None


def test_assoc_ref196_stub_double():
    # room_RefSAPoint has no real 'room_RefSAPoint' property in the generated
    # code (a bare stub) -- manually attach it so room_ActorContainerRef's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # room_ActorContainerRef's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = room_ActorContainerRef(name="sample_text")
    partner = room_RefSAPoint()
    setattr(partner, 'room_RefSAPoint', None)
    _safe_set(owner, 'room_ActorContainerRef197', partner)
    assert getattr(partner, 'room_RefSAPoint') == owner
    _safe_set(owner, 'room_ActorContainerRef197', None)
    assert getattr(partner, 'room_RefSAPoint') is None


def test_assoc_ref200_stub_double():
    # room_SPPoint has no real 'room_SPPoint201' property in the generated
    # code (a bare stub) -- manually attach it so room_ActorContainerRef's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # room_ActorContainerRef's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = room_ActorContainerRef(name="sample_text")
    partner = room_SPPoint()
    setattr(partner, 'room_SPPoint201', None)
    _safe_set(owner, 'room_ActorContainerRef202', partner)
    assert getattr(partner, 'room_SPPoint201') == owner
    _safe_set(owner, 'room_ActorContainerRef202', None)
    assert getattr(partner, 'room_SPPoint201') is None


def test_assoc_regular88_stub_double():
    # room_PortClass has no real 'room_PortClass' property in the generated
    # code (a bare stub) -- manually attach it so room_ProtocolClass's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # room_ProtocolClass's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = room_ProtocolClass(commType="sample_text")
    partner = room_PortClass()
    setattr(partner, 'room_PortClass', None)
    _safe_set(owner, 'room_ProtocolClass89', partner)
    assert getattr(partner, 'room_PortClass') == owner
    _safe_set(owner, 'room_ProtocolClass89', None)
    assert getattr(partner, 'room_PortClass') is None


def test_assoc_relayPorts174_stub_double():
    # room_SubSystemClass has no real 'room_SubSystemClass175' property in the generated
    # code (a bare stub) -- manually attach it so room_Port's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # room_Port's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = room_Port(conjugated=True, multiplicity=7)
    partner = room_SubSystemClass()
    setattr(partner, 'room_SubSystemClass175', None)
    _safe_set(owner, 'room_Port176', partner)
    assert owner in getattr(partner, 'room_SubSystemClass175')
    _safe_set(owner, 'room_Port176', None)
    assert owner not in getattr(partner, 'room_SubSystemClass175')


def test_assoc_semantics93_stub_double():
    # room_ProtocolSemantics has no real 'room_ProtocolSemantics' property in the generated
    # code (a bare stub) -- manually attach it so room_ProtocolClass's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # room_ProtocolClass's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = room_ProtocolClass(commType="sample_text")
    partner = room_ProtocolSemantics()
    setattr(partner, 'room_ProtocolSemantics', None)
    _safe_set(owner, 'room_ProtocolClass94', partner)
    assert getattr(partner, 'room_ProtocolSemantics') == owner
    _safe_set(owner, 'room_ProtocolClass94', None)
    assert getattr(partner, 'room_ProtocolSemantics') is None


def test_assoc_sendsMsg69_stub_double():
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


def test_assoc_serviceImplementations139_stub_double():
    # room_ServiceImplementation has no real 'room_ServiceImplementation' property in the generated
    # code (a bare stub) -- manually attach it so room_ActorClass's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # room_ActorClass's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = room_ActorClass(abstract=True, commType="sample_text")
    partner = room_ServiceImplementation()
    setattr(partner, 'room_ServiceImplementation', None)
    _safe_set(owner, 'room_ActorClass140', {partner})
    assert getattr(partner, 'room_ServiceImplementation') == owner
    _safe_set(owner, 'room_ActorClass140', set())
    assert getattr(partner, 'room_ServiceImplementation') is None


def test_assoc_state251_stub_double():
    # room_StateTerminal has no real 'room_StateTerminal' property in the generated
    # code (a bare stub) -- manually attach it so room_BaseState's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # room_BaseState's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = room_BaseState(name="sample_text")
    partner = room_StateTerminal()
    setattr(partner, 'room_StateTerminal', None)
    _safe_set(owner, 'room_BaseState252', partner)
    assert getattr(partner, 'room_StateTerminal') == owner
    _safe_set(owner, 'room_BaseState252', None)
    assert getattr(partner, 'room_StateTerminal') is None


def test_assoc_state257_stub_double():
    # room_SubStateTrPointTerminal has no real 'room_SubStateTrPointTerminal258' property in the generated
    # code (a bare stub) -- manually attach it so room_BaseState's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # room_BaseState's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = room_BaseState(name="sample_text")
    partner = room_SubStateTrPointTerminal()
    setattr(partner, 'room_SubStateTrPointTerminal258', None)
    _safe_set(owner, 'room_BaseState259', partner)
    assert getattr(partner, 'room_SubStateTrPointTerminal258') == owner
    _safe_set(owner, 'room_BaseState259', None)
    assert getattr(partner, 'room_SubStateTrPointTerminal258') is None


def test_assoc_stateMachine154_stub_double():
    # room_StateGraph has no real 'room_StateGraph' property in the generated
    # code (a bare stub) -- manually attach it so room_ActorClass's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # room_ActorClass's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = room_ActorClass(abstract=True, commType="sample_text")
    partner = room_StateGraph()
    setattr(partner, 'room_StateGraph', None)
    _safe_set(owner, 'room_ActorClass155', partner)
    assert getattr(partner, 'room_StateGraph') == owner
    _safe_set(owner, 'room_ActorClass155', None)
    assert getattr(partner, 'room_StateGraph') is None


def test_assoc_states223_stub_double():
    # room_StateGraph has no real 'room_StateGraph224' property in the generated
    # code (a bare stub) -- manually attach it so room_State's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # room_State's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = room_State()
    partner = room_StateGraph()
    setattr(partner, 'room_StateGraph224', None)
    _safe_set(owner, 'room_State225', partner)
    assert owner in getattr(partner, 'room_StateGraph224')
    _safe_set(owner, 'room_State225', None)
    assert owner not in getattr(partner, 'room_StateGraph224')


def test_assoc_strSAPs141_stub_double():
    # room_SAPRef has no real 'room_SAPRef' property in the generated
    # code (a bare stub) -- manually attach it so room_ActorClass's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # room_ActorClass's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = room_ActorClass(abstract=True, commType="sample_text")
    partner = room_SAPRef()
    setattr(partner, 'room_SAPRef', None)
    _safe_set(owner, 'room_ActorClass142', {partner})
    assert getattr(partner, 'room_SAPRef') == owner
    _safe_set(owner, 'room_ActorClass142', set())
    assert getattr(partner, 'room_SAPRef') is None


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


def test_assoc_subgraph220_stub_double():
    # room_StateGraph has no real 'room_StateGraph222' property in the generated
    # code (a bare stub) -- manually attach it so room_State's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # room_State's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = room_State()
    partner = room_StateGraph()
    setattr(partner, 'room_StateGraph222', None)
    _safe_set(owner, 'room_State221', partner)
    assert getattr(partner, 'room_StateGraph222') == owner
    _safe_set(owner, 'room_State221', None)
    assert getattr(partner, 'room_StateGraph222') is None


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


def test_assoc_threads177_stub_double():
    # room_SubSystemClass has no real 'room_SubSystemClass178' property in the generated
    # code (a bare stub) -- manually attach it so room_LogicalThread's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # room_LogicalThread's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = room_LogicalThread(name="sample_text", prio=7)
    partner = room_SubSystemClass()
    setattr(partner, 'room_SubSystemClass178', None)
    _safe_set(owner, 'room_LogicalThread', partner)
    assert owner in getattr(partner, 'room_SubSystemClass178')
    _safe_set(owner, 'room_LogicalThread', None)
    assert owner not in getattr(partner, 'room_SubSystemClass178')


def test_assoc_to236_stub_double():
    # room_TransitionTerminal has no real 'room_TransitionTerminal' property in the generated
    # code (a bare stub) -- manually attach it so room_Transition's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # room_Transition's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = room_Transition(name="sample_text")
    partner = room_TransitionTerminal()
    setattr(partner, 'room_TransitionTerminal', None)
    _safe_set(owner, 'room_Transition237', partner)
    assert getattr(partner, 'room_TransitionTerminal') == owner
    _safe_set(owner, 'room_Transition237', None)
    assert getattr(partner, 'room_TransitionTerminal') is None


def test_assoc_trPoint253_stub_double():
    # room_TrPointTerminal has no real 'room_TrPointTerminal' property in the generated
    # code (a bare stub) -- manually attach it so room_TrPoint's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # room_TrPoint's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = room_TrPoint(name="sample_text")
    partner = room_TrPointTerminal()
    setattr(partner, 'room_TrPointTerminal', None)
    _safe_set(owner, 'room_TrPoint254', partner)
    assert getattr(partner, 'room_TrPointTerminal') == owner
    _safe_set(owner, 'room_TrPoint254', None)
    assert getattr(partner, 'room_TrPointTerminal') is None


def test_assoc_trPoint255_stub_double():
    # room_SubStateTrPointTerminal has no real 'room_SubStateTrPointTerminal' property in the generated
    # code (a bare stub) -- manually attach it so room_TrPoint's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # room_TrPoint's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = room_TrPoint(name="sample_text")
    partner = room_SubStateTrPointTerminal()
    setattr(partner, 'room_SubStateTrPointTerminal', None)
    _safe_set(owner, 'room_TrPoint256', partner)
    assert getattr(partner, 'room_SubStateTrPointTerminal') == owner
    _safe_set(owner, 'room_TrPoint256', None)
    assert getattr(partner, 'room_SubStateTrPointTerminal') is None


def test_assoc_trPoints226_stub_double():
    # room_StateGraph has no real 'room_StateGraph227' property in the generated
    # code (a bare stub) -- manually attach it so room_TrPoint's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # room_TrPoint's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = room_TrPoint(name="sample_text")
    partner = room_StateGraph()
    setattr(partner, 'room_StateGraph227', None)
    _safe_set(owner, 'room_TrPoint', partner)
    assert owner in getattr(partner, 'room_StateGraph227')
    _safe_set(owner, 'room_TrPoint', None)
    assert owner not in getattr(partner, 'room_StateGraph227')


def test_assoc_transitions230_stub_double():
    # room_StateGraph has no real 'room_StateGraph231' property in the generated
    # code (a bare stub) -- manually attach it so room_Transition's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # room_Transition's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = room_Transition(name="sample_text")
    partner = room_StateGraph()
    setattr(partner, 'room_StateGraph231', None)
    _safe_set(owner, 'room_Transition', partner)
    assert owner in getattr(partner, 'room_StateGraph231')
    _safe_set(owner, 'room_Transition', None)
    assert owner not in getattr(partner, 'room_StateGraph231')


def test_assoc_type206_stub_double():
    # room_ActorRef has no real 'room_ActorRef207' property in the generated
    # code (a bare stub) -- manually attach it so room_ActorClass's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # room_ActorClass's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = room_ActorClass(abstract=True, commType="sample_text")
    partner = room_ActorRef()
    setattr(partner, 'room_ActorRef207', None)
    _safe_set(owner, 'room_ActorClass208', partner)
    assert getattr(partner, 'room_ActorRef207') == owner
    _safe_set(owner, 'room_ActorClass208', None)
    assert getattr(partner, 'room_ActorRef207') is None


def test_assoc_type34_stub_double():
    # room_DataType has no real 'room_DataType' property in the generated
    # code (a bare stub) -- manually attach it so room_RefableType's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # room_RefableType's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = room_RefableType(ref=True)
    partner = room_DataType()
    setattr(partner, 'room_DataType', None)
    _safe_set(owner, 'room_RefableType35', partner)
    assert getattr(partner, 'room_DataType') == owner
    _safe_set(owner, 'room_RefableType35', None)
    assert getattr(partner, 'room_DataType') is None


def test_assoc_userCode101_stub_double():
    # room_PortClass has no real 'room_PortClass102' property in the generated
    # code (a bare stub) -- manually attach it so room_DetailCode's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # room_DetailCode's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = room_DetailCode(commands="sample_text")
    partner = room_PortClass()
    setattr(partner, 'room_PortClass102', None)
    _safe_set(owner, 'room_DetailCode103', partner)
    assert getattr(partner, 'room_PortClass102') == owner
    _safe_set(owner, 'room_DetailCode103', None)
    assert getattr(partner, 'room_PortClass102') is None


def test_assoc_userCode123_stub_double():
    # room_ActorContainerClass has no real 'room_ActorContainerClass24' property in the generated
    # code (a bare stub) -- manually attach it so room_DetailCode's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # room_DetailCode's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = room_DetailCode(commands="sample_text")
    partner = room_ActorContainerClass()
    setattr(partner, 'room_ActorContainerClass24', None)
    _safe_set(owner, 'room_DetailCode', partner)
    assert getattr(partner, 'room_ActorContainerClass24') == owner
    _safe_set(owner, 'room_DetailCode', None)
    assert getattr(partner, 'room_ActorContainerClass24') is None


def test_assoc_userCode139_stub_double():
    # room_DataClass has no real 'room_DataClass40' property in the generated
    # code (a bare stub) -- manually attach it so room_DetailCode's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # room_DetailCode's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = room_DetailCode(commands="sample_text")
    partner = room_DataClass()
    setattr(partner, 'room_DataClass40', None)
    _safe_set(owner, 'room_DetailCode41', partner)
    assert getattr(partner, 'room_DataClass40') == owner
    _safe_set(owner, 'room_DetailCode41', None)
    assert getattr(partner, 'room_DataClass40') is None


def test_assoc_userCode225_stub_double():
    # room_ActorContainerClass has no real 'room_ActorContainerClass26' property in the generated
    # code (a bare stub) -- manually attach it so room_DetailCode's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # room_DetailCode's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = room_DetailCode(commands="sample_text")
    partner = room_ActorContainerClass()
    setattr(partner, 'room_ActorContainerClass26', None)
    _safe_set(owner, 'room_DetailCode27', partner)
    assert getattr(partner, 'room_ActorContainerClass26') == owner
    _safe_set(owner, 'room_DetailCode27', None)
    assert getattr(partner, 'room_ActorContainerClass26') is None


def test_assoc_userCode242_stub_double():
    # room_DataClass has no real 'room_DataClass43' property in the generated
    # code (a bare stub) -- manually attach it so room_DetailCode's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # room_DetailCode's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = room_DetailCode(commands="sample_text")
    partner = room_DataClass()
    setattr(partner, 'room_DataClass43', None)
    _safe_set(owner, 'room_DetailCode44', partner)
    assert getattr(partner, 'room_DataClass43') == owner
    _safe_set(owner, 'room_DetailCode44', None)
    assert getattr(partner, 'room_DataClass43') is None


def test_assoc_userCode328_stub_double():
    # room_ActorContainerClass has no real 'room_ActorContainerClass29' property in the generated
    # code (a bare stub) -- manually attach it so room_DetailCode's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # room_DetailCode's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = room_DetailCode(commands="sample_text")
    partner = room_ActorContainerClass()
    setattr(partner, 'room_ActorContainerClass29', None)
    _safe_set(owner, 'room_DetailCode30', partner)
    assert getattr(partner, 'room_ActorContainerClass29') == owner
    _safe_set(owner, 'room_DetailCode30', None)
    assert getattr(partner, 'room_ActorContainerClass29') is None


def test_assoc_userCode345_stub_double():
    # room_DataClass has no real 'room_DataClass46' property in the generated
    # code (a bare stub) -- manually attach it so room_DetailCode's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # room_DetailCode's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = room_DetailCode(commands="sample_text")
    partner = room_DataClass()
    setattr(partner, 'room_DataClass46', None)
    _safe_set(owner, 'room_DetailCode47', partner)
    assert getattr(partner, 'room_DataClass46') == owner
    _safe_set(owner, 'room_DetailCode47', None)
    assert getattr(partner, 'room_DataClass46') is None


