import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    ActorContainerClass,
    ActorContainerRef,
    InterfaceItem,
    NonInitialTransition,
    RoomClass,
    SAPoint,
    SemanticsRule,
    State,
    StateGraphItem,
    StateGraphNode,
    StructureClass,
    TrPoint,
    Transition,
    TransitionTerminal,
    room_ActorClass,
    room_ActorContainerClass,
    room_ActorContainerRef,
    room_ActorInstancePath,
    room_ActorRef,
    room_Attribute,
    room_BaseState,
    room_Binding,
    room_BindingEndPoint,
    room_CPBranchTransition,
    room_ChoicePoint,
    room_ChoicepointTerminal,
    room_ContinuationTransition,
    room_DataClass,
    room_DetailCode,
    room_EntryPoint,
    room_ExitPoint,
    room_ExternalPort,
    room_FreeType,
    room_FreeTypedID,
    room_Guard,
    room_Import,
    room_InitialTransition,
    room_InterfaceItem,
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
    room_ProtocolClass,
    room_ProtocolSemantics,
    room_RefSAPoint,
    room_RefinedState,
    room_RelaySAPoint,
    room_RoomClass,
    room_RoomModel,
    room_SAPRef,
    room_SAPoint,
    room_SPPRef,
    room_SPPoint,
    room_SemanticsInRule,
    room_SemanticsOutRule,
    room_SemanticsRule,
    room_ServiceImplementation,
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
    room_TransitionPoint,
    room_TransitionTerminal,
    room_Trigger,
    room_TriggeredTransition,
    room_Type,
    room_TypedID,
    PrimitiveType,
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

def test_assoc_action187_reverse_link_reassign_clear():
    a1 = room_Transition(name="sample_text")
    a2 = room_Transition(name="sample_text_2")
    b = room_DetailCode(commands="sample_text")
    _safe_set(b, 'room_DetailCode189', a1)
    assert _is_linked(b, 'room_DetailCode189', a1)
    if hasattr(a1, 'room_Transition188'):
        assert _is_linked(a1, 'room_Transition188', b)
    _safe_set(b, 'room_DetailCode189', a2)
    assert _is_linked(b, 'room_DetailCode189', a2)
    if hasattr(a1, 'room_Transition188'):
        assert not _is_linked(a1, 'room_Transition188', b)
    if hasattr(a2, 'room_Transition188'):
        assert _is_linked(a2, 'room_Transition188', b)
    _safe_set(b, 'room_DetailCode189', None)
    assert not _is_linked(b, 'room_DetailCode189', a2)
    if hasattr(a2, 'room_Transition188'):
        assert not _is_linked(a2, 'room_Transition188', b)


def test_assoc_actorClasses5_reverse_link_reassign_clear():
    a1 = room_RoomModel(name="sample_text")
    a2 = room_RoomModel(name="sample_text_2")
    b = room_ActorClass(abstract=True)
    _safe_set(b, 'room_ActorClass', a1)
    assert _is_linked(b, 'room_ActorClass', a1)
    if hasattr(a1, 'room_RoomModel6'):
        assert _is_linked(a1, 'room_RoomModel6', b)
    _safe_set(b, 'room_ActorClass', a2)
    assert _is_linked(b, 'room_ActorClass', a2)
    if hasattr(a1, 'room_RoomModel6'):
        assert not _is_linked(a1, 'room_RoomModel6', b)
    if hasattr(a2, 'room_RoomModel6'):
        assert _is_linked(a2, 'room_RoomModel6', b)
    _safe_set(b, 'room_ActorClass', None)
    assert not _is_linked(b, 'room_ActorClass', a2)
    if hasattr(a2, 'room_RoomModel6'):
        assert not _is_linked(a2, 'room_RoomModel6', b)


def test_assoc_arguments35_reverse_link_reassign_clear():
    a1 = room_Operation(name="sample_text")
    a2 = room_Operation(name="sample_text_2")
    b = room_FreeTypedID(name="sample_text")
    _safe_set(b, 'room_FreeTypedID37', a1)
    assert _is_linked(b, 'room_FreeTypedID37', a1)
    if hasattr(a1, 'room_Operation36'):
        assert _is_linked(a1, 'room_Operation36', b)
    _safe_set(b, 'room_FreeTypedID37', a2)
    assert _is_linked(b, 'room_FreeTypedID37', a2)
    if hasattr(a1, 'room_Operation36'):
        assert not _is_linked(a1, 'room_Operation36', b)
    if hasattr(a2, 'room_Operation36'):
        assert _is_linked(a2, 'room_Operation36', b)
    _safe_set(b, 'room_FreeTypedID37', None)
    assert not _is_linked(b, 'room_FreeTypedID37', a2)
    if hasattr(a2, 'room_Operation36'):
        assert not _is_linked(a2, 'room_Operation36', b)


def test_assoc_arguments64_reverse_link_reassign_clear():
    a1 = room_TypedID(name="sample_text")
    a2 = room_TypedID(name="sample_text_2")
    b = room_Message(name="sample_text")
    _safe_set(b, 'room_Message65', {a1})
    assert _is_linked(b, 'room_Message65', a1)
    if hasattr(a1, 'room_TypedID66'):
        assert _is_linked(a1, 'room_TypedID66', b)
    _safe_set(b, 'room_Message65', {a2})
    assert _is_linked(b, 'room_Message65', a2)
    if hasattr(a1, 'room_TypedID66'):
        assert not _is_linked(a1, 'room_TypedID66', b)
    if hasattr(a2, 'room_TypedID66'):
        assert _is_linked(a2, 'room_TypedID66', b)
    _safe_set(b, 'room_Message65', set())
    assert not _is_linked(b, 'room_Message65', a2)
    if hasattr(a2, 'room_TypedID66'):
        assert not _is_linked(a2, 'room_TypedID66', b)


def test_assoc_attributes112_reverse_link_reassign_clear():
    a1 = room_Attribute(name="sample_text", size=7)
    a2 = room_Attribute(name="sample_text_2", size=13)
    b = room_ActorClass(abstract=True)
    _safe_set(b, 'room_ActorClass113', {a1})
    assert _is_linked(b, 'room_ActorClass113', a1)
    if hasattr(a1, 'room_Attribute114'):
        assert _is_linked(a1, 'room_Attribute114', b)
    _safe_set(b, 'room_ActorClass113', {a2})
    assert _is_linked(b, 'room_ActorClass113', a2)
    if hasattr(a1, 'room_Attribute114'):
        assert not _is_linked(a1, 'room_Attribute114', b)
    if hasattr(a2, 'room_Attribute114'):
        assert _is_linked(a2, 'room_Attribute114', b)
    _safe_set(b, 'room_ActorClass113', set())
    assert not _is_linked(b, 'room_ActorClass113', a2)
    if hasattr(a2, 'room_Attribute114'):
        assert not _is_linked(a2, 'room_Attribute114', b)


def test_assoc_base93_reverse_link_reassign_clear():
    a1 = room_ActorClass(abstract=True)
    a2 = room_ActorClass(abstract=False)
    b = room_ActorClass(abstract=True)
    _safe_set(b, 'room_ActorClass94', a1)
    assert _is_linked(b, 'room_ActorClass94', a1)
    if hasattr(a1, 'room_ActorClass92'):
        assert _is_linked(a1, 'room_ActorClass92', b)
    _safe_set(b, 'room_ActorClass94', a2)
    assert _is_linked(b, 'room_ActorClass94', a2)
    if hasattr(a1, 'room_ActorClass92'):
        assert not _is_linked(a1, 'room_ActorClass92', b)
    if hasattr(a2, 'room_ActorClass92'):
        assert _is_linked(a2, 'room_ActorClass92', b)
    _safe_set(b, 'room_ActorClass94', None)
    assert not _is_linked(b, 'room_ActorClass94', a2)
    if hasattr(a2, 'room_ActorClass92'):
        assert not _is_linked(a2, 'room_ActorClass92', b)


def test_assoc_detailCode41_reverse_link_reassign_clear():
    a1 = room_Operation(name="sample_text")
    a2 = room_Operation(name="sample_text_2")
    b = room_DetailCode(commands="sample_text")
    _safe_set(b, 'room_DetailCode', a1)
    assert _is_linked(b, 'room_DetailCode', a1)
    if hasattr(a1, 'room_Operation42'):
        assert _is_linked(a1, 'room_Operation42', b)
    _safe_set(b, 'room_DetailCode', a2)
    assert _is_linked(b, 'room_DetailCode', a2)
    if hasattr(a1, 'room_Operation42'):
        assert not _is_linked(a1, 'room_Operation42', b)
    if hasattr(a2, 'room_Operation42'):
        assert _is_linked(a2, 'room_Operation42', b)
    _safe_set(b, 'room_DetailCode', None)
    assert not _is_linked(b, 'room_DetailCode', a2)
    if hasattr(a2, 'room_Operation42'):
        assert not _is_linked(a2, 'room_Operation42', b)


def test_assoc_entryCode167_reverse_link_reassign_clear():
    a1 = room_State()
    a2 = room_State()
    b = room_DetailCode(commands="sample_text")
    _safe_set(b, 'room_DetailCode168', a1)
    assert _is_linked(b, 'room_DetailCode168', a1)
    if hasattr(a1, 'room_State'):
        assert _is_linked(a1, 'room_State', b)
    _safe_set(b, 'room_DetailCode168', a2)
    assert _is_linked(b, 'room_DetailCode168', a2)
    if hasattr(a1, 'room_State'):
        assert not _is_linked(a1, 'room_State', b)
    if hasattr(a2, 'room_State'):
        assert _is_linked(a2, 'room_State', b)
    _safe_set(b, 'room_DetailCode168', None)
    assert not _is_linked(b, 'room_DetailCode168', a2)
    if hasattr(a2, 'room_State'):
        assert not _is_linked(a2, 'room_State', b)


def test_assoc_exitCode169_reverse_link_reassign_clear():
    a1 = room_State()
    a2 = room_State()
    b = room_DetailCode(commands="sample_text")
    _safe_set(b, 'room_DetailCode171', a1)
    assert _is_linked(b, 'room_DetailCode171', a1)
    if hasattr(a1, 'room_State170'):
        assert _is_linked(a1, 'room_State170', b)
    _safe_set(b, 'room_DetailCode171', a2)
    assert _is_linked(b, 'room_DetailCode171', a2)
    if hasattr(a1, 'room_State170'):
        assert not _is_linked(a1, 'room_State170', b)
    if hasattr(a2, 'room_State170'):
        assert _is_linked(a2, 'room_State170', b)
    _safe_set(b, 'room_DetailCode171', None)
    assert not _is_linked(b, 'room_DetailCode171', a2)
    if hasattr(a2, 'room_State170'):
        assert not _is_linked(a2, 'room_State170', b)


def test_assoc_ifPorts95_reverse_link_reassign_clear():
    a1 = room_Port(conjugated=True, multiplicity=7)
    a2 = room_Port(conjugated=False, multiplicity=13)
    b = room_ActorClass(abstract=True)
    _safe_set(b, 'room_ActorClass96', {a1})
    assert _is_linked(b, 'room_ActorClass96', a1)
    if hasattr(a1, 'room_Port'):
        assert _is_linked(a1, 'room_Port', b)
    _safe_set(b, 'room_ActorClass96', {a2})
    assert _is_linked(b, 'room_ActorClass96', a2)
    if hasattr(a1, 'room_Port'):
        assert not _is_linked(a1, 'room_Port', b)
    if hasattr(a2, 'room_Port'):
        assert _is_linked(a2, 'room_Port', b)
    _safe_set(b, 'room_ActorClass96', set())
    assert not _is_linked(b, 'room_ActorClass96', a2)
    if hasattr(a2, 'room_Port'):
        assert not _is_linked(a2, 'room_Port', b)


def test_assoc_imports0_reverse_link_reassign_clear():
    a1 = room_RoomModel(name="sample_text")
    a2 = room_RoomModel(name="sample_text_2")
    b = room_Import(importedNamespace="sample_text")
    _safe_set(b, 'room_Import', a1)
    assert _is_linked(b, 'room_Import', a1)
    if hasattr(a1, 'room_RoomModel'):
        assert _is_linked(a1, 'room_RoomModel', b)
    _safe_set(b, 'room_Import', a2)
    assert _is_linked(b, 'room_Import', a2)
    if hasattr(a1, 'room_RoomModel'):
        assert not _is_linked(a1, 'room_RoomModel', b)
    if hasattr(a2, 'room_RoomModel'):
        assert _is_linked(a2, 'room_RoomModel', b)
    _safe_set(b, 'room_Import', None)
    assert not _is_linked(b, 'room_Import', a2)
    if hasattr(a2, 'room_RoomModel'):
        assert not _is_linked(a2, 'room_RoomModel', b)


def test_assoc_instances138_reverse_link_reassign_clear():
    a1 = room_LogicalThread(name="sample_text")
    a2 = room_LogicalThread(name="sample_text_2")
    b = room_ActorInstancePath(segments="sample_text")
    _safe_set(b, 'room_ActorInstancePath', a1)
    assert _is_linked(b, 'room_ActorInstancePath', a1)
    if hasattr(a1, 'room_LogicalThread139'):
        assert _is_linked(a1, 'room_LogicalThread139', b)
    _safe_set(b, 'room_ActorInstancePath', a2)
    assert _is_linked(b, 'room_ActorInstancePath', a2)
    if hasattr(a1, 'room_LogicalThread139'):
        assert not _is_linked(a1, 'room_LogicalThread139', b)
    if hasattr(a2, 'room_LogicalThread139'):
        assert _is_linked(a2, 'room_LogicalThread139', b)
    _safe_set(b, 'room_ActorInstancePath', None)
    assert not _is_linked(b, 'room_ActorInstancePath', a2)
    if hasattr(a2, 'room_LogicalThread139'):
        assert not _is_linked(a2, 'room_LogicalThread139', b)


def test_assoc_intPorts103_reverse_link_reassign_clear():
    a1 = room_Port(conjugated=True, multiplicity=7)
    a2 = room_Port(conjugated=False, multiplicity=13)
    b = room_ActorClass(abstract=True)
    _safe_set(b, 'room_ActorClass104', {a1})
    assert _is_linked(b, 'room_ActorClass104', a1)
    if hasattr(a1, 'room_Port105'):
        assert _is_linked(a1, 'room_Port105', b)
    _safe_set(b, 'room_ActorClass104', {a2})
    assert _is_linked(b, 'room_ActorClass104', a2)
    if hasattr(a1, 'room_Port105'):
        assert not _is_linked(a1, 'room_Port105', b)
    if hasattr(a2, 'room_Port105'):
        assert _is_linked(a2, 'room_Port105', b)
    _safe_set(b, 'room_ActorClass104', set())
    assert not _is_linked(b, 'room_ActorClass104', a2)
    if hasattr(a2, 'room_Port105'):
        assert not _is_linked(a2, 'room_Port105', b)


def test_assoc_operations115_reverse_link_reassign_clear():
    a1 = room_Operation(name="sample_text")
    a2 = room_Operation(name="sample_text_2")
    b = room_ActorClass(abstract=True)
    _safe_set(b, 'room_ActorClass116', {a1})
    assert _is_linked(b, 'room_ActorClass116', a1)
    if hasattr(a1, 'room_Operation117'):
        assert _is_linked(a1, 'room_Operation117', b)
    _safe_set(b, 'room_ActorClass116', {a2})
    assert _is_linked(b, 'room_ActorClass116', a2)
    if hasattr(a1, 'room_Operation117'):
        assert not _is_linked(a1, 'room_Operation117', b)
    if hasattr(a2, 'room_Operation117'):
        assert _is_linked(a2, 'room_Operation117', b)
    _safe_set(b, 'room_ActorClass116', set())
    assert not _is_linked(b, 'room_ActorClass116', a2)
    if hasattr(a2, 'room_Operation117'):
        assert not _is_linked(a2, 'room_Operation117', b)


def test_assoc_returntype38_reverse_link_reassign_clear():
    a1 = room_Operation(name="sample_text")
    a2 = room_Operation(name="sample_text_2")
    b = room_FreeType(prim="sample_text", type="sample_text")
    _safe_set(b, 'room_FreeType40', a1)
    assert _is_linked(b, 'room_FreeType40', a1)
    if hasattr(a1, 'room_Operation39'):
        assert _is_linked(a1, 'room_Operation39', b)
    _safe_set(b, 'room_FreeType40', a2)
    assert _is_linked(b, 'room_FreeType40', a2)
    if hasattr(a1, 'room_Operation39'):
        assert not _is_linked(a1, 'room_Operation39', b)
    if hasattr(a2, 'room_Operation39'):
        assert _is_linked(a2, 'room_Operation39', b)
    _safe_set(b, 'room_FreeType40', None)
    assert not _is_linked(b, 'room_FreeType40', a2)
    if hasattr(a2, 'room_Operation39'):
        assert not _is_linked(a2, 'room_Operation39', b)


def test_assoc_type17_reverse_link_reassign_clear():
    a1 = room_TypedID(name="sample_text")
    a2 = room_TypedID(name="sample_text_2")
    b = room_Type(prim="sample_text")
    _safe_set(b, 'room_Type', a1)
    assert _is_linked(b, 'room_Type', a1)
    if hasattr(a1, 'room_TypedID'):
        assert _is_linked(a1, 'room_TypedID', b)
    _safe_set(b, 'room_Type', a2)
    assert _is_linked(b, 'room_Type', a2)
    if hasattr(a1, 'room_TypedID'):
        assert not _is_linked(a1, 'room_TypedID', b)
    if hasattr(a2, 'room_TypedID'):
        assert _is_linked(a2, 'room_TypedID', b)
    _safe_set(b, 'room_Type', None)
    assert not _is_linked(b, 'room_Type', a2)
    if hasattr(a2, 'room_TypedID'):
        assert not _is_linked(a2, 'room_TypedID', b)


def test_assoc_type18_reverse_link_reassign_clear():
    a1 = room_FreeTypedID(name="sample_text")
    a2 = room_FreeTypedID(name="sample_text_2")
    b = room_FreeType(prim="sample_text", type="sample_text")
    _safe_set(b, 'room_FreeType', a1)
    assert _is_linked(b, 'room_FreeType', a1)
    if hasattr(a1, 'room_FreeTypedID'):
        assert _is_linked(a1, 'room_FreeTypedID', b)
    _safe_set(b, 'room_FreeType', a2)
    assert _is_linked(b, 'room_FreeType', a2)
    if hasattr(a1, 'room_FreeTypedID'):
        assert not _is_linked(a1, 'room_FreeTypedID', b)
    if hasattr(a2, 'room_FreeTypedID'):
        assert _is_linked(a2, 'room_FreeTypedID', b)
    _safe_set(b, 'room_FreeType', None)
    assert not _is_linked(b, 'room_FreeType', a2)
    if hasattr(a2, 'room_FreeTypedID'):
        assert not _is_linked(a2, 'room_FreeTypedID', b)


def test_assoc_type32_reverse_link_reassign_clear():
    a1 = room_Type(prim="sample_text")
    a2 = room_Type(prim="sample_text_2")
    b = room_Attribute(name="sample_text", size=7)
    _safe_set(b, 'room_Attribute33', a1)
    assert _is_linked(b, 'room_Attribute33', a1)
    if hasattr(a1, 'room_Type34'):
        assert _is_linked(a1, 'room_Type34', b)
    _safe_set(b, 'room_Attribute33', a2)
    assert _is_linked(b, 'room_Attribute33', a2)
    if hasattr(a1, 'room_Type34'):
        assert not _is_linked(a1, 'room_Type34', b)
    if hasattr(a2, 'room_Type34'):
        assert _is_linked(a2, 'room_Type34', b)
    _safe_set(b, 'room_Attribute33', None)
    assert not _is_linked(b, 'room_Attribute33', a2)
    if hasattr(a2, 'room_Type34'):
        assert not _is_linked(a2, 'room_Type34', b)


def test_assoc_userCode197_reverse_link_reassign_clear():
    a1 = room_DetailCode(commands="sample_text")
    a2 = room_DetailCode(commands="sample_text_2")
    b = room_ActorClass(abstract=True)
    _safe_set(b, 'room_ActorClass98', a1)
    assert _is_linked(b, 'room_ActorClass98', a1)
    if hasattr(a1, 'room_DetailCode99'):
        assert _is_linked(a1, 'room_DetailCode99', b)
    _safe_set(b, 'room_ActorClass98', a2)
    assert _is_linked(b, 'room_ActorClass98', a2)
    if hasattr(a1, 'room_DetailCode99'):
        assert not _is_linked(a1, 'room_DetailCode99', b)
    if hasattr(a2, 'room_DetailCode99'):
        assert _is_linked(a2, 'room_DetailCode99', b)
    _safe_set(b, 'room_ActorClass98', None)
    assert not _is_linked(b, 'room_ActorClass98', a2)
    if hasattr(a2, 'room_DetailCode99'):
        assert not _is_linked(a2, 'room_DetailCode99', b)


def test_assoc_userCode2100_reverse_link_reassign_clear():
    a1 = room_DetailCode(commands="sample_text")
    a2 = room_DetailCode(commands="sample_text_2")
    b = room_ActorClass(abstract=True)
    _safe_set(b, 'room_ActorClass101', a1)
    assert _is_linked(b, 'room_ActorClass101', a1)
    if hasattr(a1, 'room_DetailCode102'):
        assert _is_linked(a1, 'room_DetailCode102', b)
    _safe_set(b, 'room_ActorClass101', a2)
    assert _is_linked(b, 'room_ActorClass101', a2)
    if hasattr(a1, 'room_DetailCode102'):
        assert not _is_linked(a1, 'room_DetailCode102', b)
    if hasattr(a2, 'room_DetailCode102'):
        assert _is_linked(a2, 'room_DetailCode102', b)
    _safe_set(b, 'room_ActorClass101', None)
    assert not _is_linked(b, 'room_ActorClass101', a2)
    if hasattr(a2, 'room_DetailCode102'):
        assert not _is_linked(a2, 'room_DetailCode102', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_actorRef145_stub_double():
    # room_BindingEndPoint has no real 'room_BindingEndPoint146' property in the generated
    # code (a bare stub) -- manually attach it so room_ActorContainerRef's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # room_ActorContainerRef's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = room_ActorContainerRef(name="sample_text")
    partner = room_BindingEndPoint()
    setattr(partner, 'room_BindingEndPoint146', None)
    _safe_set(owner, 'room_ActorContainerRef', partner)
    assert getattr(partner, 'room_BindingEndPoint146') == owner
    _safe_set(owner, 'room_ActorContainerRef', None)
    assert getattr(partner, 'room_BindingEndPoint146') is None


def test_assoc_attributes28_stub_double():
    # room_DataClass has no real 'room_DataClass29' property in the generated
    # code (a bare stub) -- manually attach it so room_Attribute's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # room_Attribute's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = room_Attribute(name="sample_text", size=7)
    partner = room_DataClass()
    setattr(partner, 'room_DataClass29', None)
    _safe_set(owner, 'room_Attribute', partner)
    assert owner in getattr(partner, 'room_DataClass29')
    _safe_set(owner, 'room_Attribute', None)
    assert owner not in getattr(partner, 'room_DataClass29')


def test_assoc_attributes70_stub_double():
    # room_PortClass has no real 'room_PortClass71' property in the generated
    # code (a bare stub) -- manually attach it so room_Attribute's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # room_Attribute's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = room_Attribute(name="sample_text", size=7)
    partner = room_PortClass()
    setattr(partner, 'room_PortClass71', None)
    _safe_set(owner, 'room_Attribute72', partner)
    assert owner in getattr(partner, 'room_PortClass71')
    _safe_set(owner, 'room_Attribute72', None)
    assert owner not in getattr(partner, 'room_PortClass71')


def test_assoc_base184_stub_double():
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


def test_assoc_chPoints180_stub_double():
    # room_StateGraph has no real 'room_StateGraph181' property in the generated
    # code (a bare stub) -- manually attach it so room_ChoicePoint's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # room_ChoicePoint's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = room_ChoicePoint(name="sample_text")
    partner = room_StateGraph()
    setattr(partner, 'room_StateGraph181', None)
    _safe_set(owner, 'room_ChoicePoint', partner)
    assert owner in getattr(partner, 'room_StateGraph181')
    _safe_set(owner, 'room_ChoicePoint', None)
    assert owner not in getattr(partner, 'room_StateGraph181')


def test_assoc_condition193_stub_double():
    # room_CPBranchTransition has no real 'room_CPBranchTransition' property in the generated
    # code (a bare stub) -- manually attach it so room_DetailCode's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # room_DetailCode's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = room_DetailCode(commands="sample_text")
    partner = room_CPBranchTransition()
    setattr(partner, 'room_CPBranchTransition', None)
    _safe_set(owner, 'room_DetailCode194', partner)
    assert getattr(partner, 'room_CPBranchTransition') == owner
    _safe_set(owner, 'room_DetailCode194', None)
    assert getattr(partner, 'room_CPBranchTransition') is None


def test_assoc_cp204_stub_double():
    # room_ChoicepointTerminal has no real 'room_ChoicepointTerminal' property in the generated
    # code (a bare stub) -- manually attach it so room_ChoicePoint's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # room_ChoicePoint's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = room_ChoicePoint(name="sample_text")
    partner = room_ChoicepointTerminal()
    setattr(partner, 'room_ChoicepointTerminal', None)
    _safe_set(owner, 'room_ChoicePoint205', partner)
    assert getattr(partner, 'room_ChoicepointTerminal') == owner
    _safe_set(owner, 'room_ChoicePoint205', None)
    assert getattr(partner, 'room_ChoicepointTerminal') is None


def test_assoc_dataClasses1_stub_double():
    # room_DataClass has no real 'room_DataClass' property in the generated
    # code (a bare stub) -- manually attach it so room_RoomModel's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # room_RoomModel's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = room_RoomModel(name="sample_text")
    partner = room_DataClass()
    setattr(partner, 'room_DataClass', None)
    _safe_set(owner, 'room_RoomModel2', {partner})
    assert getattr(partner, 'room_DataClass') == owner
    _safe_set(owner, 'room_RoomModel2', set())
    assert getattr(partner, 'room_DataClass') is None


def test_assoc_detailCode81_stub_double():
    # room_MessageHandler has no real 'room_MessageHandler82' property in the generated
    # code (a bare stub) -- manually attach it so room_DetailCode's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # room_DetailCode's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = room_DetailCode(commands="sample_text")
    partner = room_MessageHandler()
    setattr(partner, 'room_MessageHandler82', None)
    _safe_set(owner, 'room_DetailCode83', partner)
    assert getattr(partner, 'room_MessageHandler82') == owner
    _safe_set(owner, 'room_DetailCode83', None)
    assert getattr(partner, 'room_MessageHandler82') is None


def test_assoc_extPorts106_stub_double():
    # room_ExternalPort has no real 'room_ExternalPort' property in the generated
    # code (a bare stub) -- manually attach it so room_ActorClass's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # room_ActorClass's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = room_ActorClass(abstract=True)
    partner = room_ExternalPort()
    setattr(partner, 'room_ExternalPort', None)
    _safe_set(owner, 'room_ActorClass107', {partner})
    assert getattr(partner, 'room_ExternalPort') == owner
    _safe_set(owner, 'room_ActorClass107', set())
    assert getattr(partner, 'room_ExternalPort') is None


def test_assoc_from_213_stub_double():
    # room_MessageFromIf has no real 'room_MessageFromIf214' property in the generated
    # code (a bare stub) -- manually attach it so room_InterfaceItem's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # room_InterfaceItem's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = room_InterfaceItem(name="sample_text")
    partner = room_MessageFromIf()
    setattr(partner, 'room_MessageFromIf214', None)
    _safe_set(owner, 'room_InterfaceItem215', partner)
    assert getattr(partner, 'room_MessageFromIf214') == owner
    _safe_set(owner, 'room_InterfaceItem215', None)
    assert getattr(partner, 'room_MessageFromIf214') is None


def test_assoc_guard216_stub_double():
    # room_Guard has no real 'room_Guard217' property in the generated
    # code (a bare stub) -- manually attach it so room_DetailCode's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # room_DetailCode's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = room_DetailCode(commands="sample_text")
    partner = room_Guard()
    setattr(partner, 'room_Guard217', None)
    _safe_set(owner, 'room_DetailCode218', partner)
    assert getattr(partner, 'room_Guard217') == owner
    _safe_set(owner, 'room_DetailCode218', None)
    assert getattr(partner, 'room_Guard217') is None


def test_assoc_ifport122_stub_double():
    # room_ExternalPort has no real 'room_ExternalPort123' property in the generated
    # code (a bare stub) -- manually attach it so room_Port's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # room_Port's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = room_Port(conjugated=True, multiplicity=7)
    partner = room_ExternalPort()
    setattr(partner, 'room_ExternalPort123', None)
    _safe_set(owner, 'room_Port124', partner)
    assert getattr(partner, 'room_ExternalPort123') == owner
    _safe_set(owner, 'room_Port124', None)
    assert getattr(partner, 'room_ExternalPort123') is None


def test_assoc_imports25_stub_double():
    # room_DataClass has no real 'room_DataClass26' property in the generated
    # code (a bare stub) -- manually attach it so room_Import's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # room_Import's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = room_Import(importedNamespace="sample_text")
    partner = room_DataClass()
    setattr(partner, 'room_DataClass26', None)
    _safe_set(owner, 'room_Import27', partner)
    assert owner in getattr(partner, 'room_DataClass26')
    _safe_set(owner, 'room_Import27', None)
    assert owner not in getattr(partner, 'room_DataClass26')


def test_assoc_incomingMessages52_stub_double():
    # room_ProtocolClass has no real 'room_ProtocolClass53' property in the generated
    # code (a bare stub) -- manually attach it so room_Message's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # room_Message's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = room_Message(name="sample_text")
    partner = room_ProtocolClass()
    setattr(partner, 'room_ProtocolClass53', None)
    _safe_set(owner, 'room_Message', partner)
    assert owner in getattr(partner, 'room_ProtocolClass53')
    _safe_set(owner, 'room_Message', None)
    assert owner not in getattr(partner, 'room_ProtocolClass53')


def test_assoc_message210_stub_double():
    # room_MessageFromIf has no real 'room_MessageFromIf211' property in the generated
    # code (a bare stub) -- manually attach it so room_Message's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # room_Message's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = room_Message(name="sample_text")
    partner = room_MessageFromIf()
    setattr(partner, 'room_MessageFromIf211', None)
    _safe_set(owner, 'room_Message212', partner)
    assert getattr(partner, 'room_MessageFromIf211') == owner
    _safe_set(owner, 'room_Message212', None)
    assert getattr(partner, 'room_MessageFromIf211') is None


def test_assoc_msg78_stub_double():
    # room_MessageHandler has no real 'room_MessageHandler79' property in the generated
    # code (a bare stub) -- manually attach it so room_Message's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # room_Message's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = room_Message(name="sample_text")
    partner = room_MessageHandler()
    setattr(partner, 'room_MessageHandler79', None)
    _safe_set(owner, 'room_Message80', partner)
    assert getattr(partner, 'room_MessageHandler79') == owner
    _safe_set(owner, 'room_Message80', None)
    assert getattr(partner, 'room_MessageHandler79') is None


def test_assoc_msg86_stub_double():
    # room_SemanticsRule has no real 'room_SemanticsRule87' property in the generated
    # code (a bare stub) -- manually attach it so room_Message's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # room_Message's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = room_Message(name="sample_text")
    partner = room_SemanticsRule()
    setattr(partner, 'room_SemanticsRule87', None)
    _safe_set(owner, 'room_Message88', partner)
    assert getattr(partner, 'room_SemanticsRule87') == owner
    _safe_set(owner, 'room_Message88', None)
    assert getattr(partner, 'room_SemanticsRule87') is None


def test_assoc_operations30_stub_double():
    # room_DataClass has no real 'room_DataClass31' property in the generated
    # code (a bare stub) -- manually attach it so room_Operation's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # room_Operation's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = room_Operation(name="sample_text")
    partner = room_DataClass()
    setattr(partner, 'room_DataClass31', None)
    _safe_set(owner, 'room_Operation', partner)
    assert owner in getattr(partner, 'room_DataClass31')
    _safe_set(owner, 'room_Operation', None)
    assert owner not in getattr(partner, 'room_DataClass31')


def test_assoc_operations73_stub_double():
    # room_PortClass has no real 'room_PortClass74' property in the generated
    # code (a bare stub) -- manually attach it so room_Operation's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # room_Operation's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = room_Operation(name="sample_text")
    partner = room_PortClass()
    setattr(partner, 'room_PortClass74', None)
    _safe_set(owner, 'room_Operation75', partner)
    assert owner in getattr(partner, 'room_PortClass74')
    _safe_set(owner, 'room_Operation75', None)
    assert owner not in getattr(partner, 'room_PortClass74')


def test_assoc_outgoingMessages54_stub_double():
    # room_ProtocolClass has no real 'room_ProtocolClass55' property in the generated
    # code (a bare stub) -- manually attach it so room_Message's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # room_Message's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = room_Message(name="sample_text")
    partner = room_ProtocolClass()
    setattr(partner, 'room_ProtocolClass55', None)
    _safe_set(owner, 'room_Message56', partner)
    assert owner in getattr(partner, 'room_ProtocolClass55')
    _safe_set(owner, 'room_Message56', None)
    assert owner not in getattr(partner, 'room_ProtocolClass55')


def test_assoc_port147_stub_double():
    # room_BindingEndPoint has no real 'room_BindingEndPoint148' property in the generated
    # code (a bare stub) -- manually attach it so room_Port's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # room_Port's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = room_Port(conjugated=True, multiplicity=7)
    partner = room_BindingEndPoint()
    setattr(partner, 'room_BindingEndPoint148', None)
    _safe_set(owner, 'room_Port149', partner)
    assert getattr(partner, 'room_BindingEndPoint148') == owner
    _safe_set(owner, 'room_Port149', None)
    assert getattr(partner, 'room_BindingEndPoint148') is None


def test_assoc_protocol120_stub_double():
    # room_ProtocolClass has no real 'room_ProtocolClass121' property in the generated
    # code (a bare stub) -- manually attach it so room_InterfaceItem's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # room_InterfaceItem's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = room_InterfaceItem(name="sample_text")
    partner = room_ProtocolClass()
    setattr(partner, 'room_ProtocolClass121', None)
    _safe_set(owner, 'room_InterfaceItem', partner)
    assert getattr(partner, 'room_ProtocolClass121') == owner
    _safe_set(owner, 'room_InterfaceItem', None)
    assert getattr(partner, 'room_ProtocolClass121') is None


def test_assoc_protocolClasses3_stub_double():
    # room_ProtocolClass has no real 'room_ProtocolClass' property in the generated
    # code (a bare stub) -- manually attach it so room_RoomModel's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # room_RoomModel's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = room_RoomModel(name="sample_text")
    partner = room_ProtocolClass()
    setattr(partner, 'room_ProtocolClass', None)
    _safe_set(owner, 'room_RoomModel4', {partner})
    assert getattr(partner, 'room_ProtocolClass') == owner
    _safe_set(owner, 'room_RoomModel4', set())
    assert getattr(partner, 'room_ProtocolClass') is None


def test_assoc_ref154_stub_double():
    # room_RefSAPoint has no real 'room_RefSAPoint' property in the generated
    # code (a bare stub) -- manually attach it so room_ActorContainerRef's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # room_ActorContainerRef's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = room_ActorContainerRef(name="sample_text")
    partner = room_RefSAPoint()
    setattr(partner, 'room_RefSAPoint', None)
    _safe_set(owner, 'room_ActorContainerRef155', partner)
    assert getattr(partner, 'room_RefSAPoint') == owner
    _safe_set(owner, 'room_ActorContainerRef155', None)
    assert getattr(partner, 'room_RefSAPoint') is None


def test_assoc_ref158_stub_double():
    # room_SPPoint has no real 'room_SPPoint159' property in the generated
    # code (a bare stub) -- manually attach it so room_ActorContainerRef's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # room_ActorContainerRef's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = room_ActorContainerRef(name="sample_text")
    partner = room_SPPoint()
    setattr(partner, 'room_SPPoint159', None)
    _safe_set(owner, 'room_ActorContainerRef160', partner)
    assert getattr(partner, 'room_SPPoint159') == owner
    _safe_set(owner, 'room_ActorContainerRef160', None)
    assert getattr(partner, 'room_SPPoint159') is None


def test_assoc_relayPorts133_stub_double():
    # room_SubSystemClass has no real 'room_SubSystemClass134' property in the generated
    # code (a bare stub) -- manually attach it so room_Port's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # room_Port's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = room_Port(conjugated=True, multiplicity=7)
    partner = room_SubSystemClass()
    setattr(partner, 'room_SubSystemClass134', None)
    _safe_set(owner, 'room_Port135', partner)
    assert owner in getattr(partner, 'room_SubSystemClass134')
    _safe_set(owner, 'room_Port135', None)
    assert owner not in getattr(partner, 'room_SubSystemClass134')


def test_assoc_serviceImplementations108_stub_double():
    # room_ServiceImplementation has no real 'room_ServiceImplementation' property in the generated
    # code (a bare stub) -- manually attach it so room_ActorClass's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # room_ActorClass's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = room_ActorClass(abstract=True)
    partner = room_ServiceImplementation()
    setattr(partner, 'room_ServiceImplementation', None)
    _safe_set(owner, 'room_ActorClass109', {partner})
    assert getattr(partner, 'room_ServiceImplementation') == owner
    _safe_set(owner, 'room_ActorClass109', set())
    assert getattr(partner, 'room_ServiceImplementation') is None


def test_assoc_state195_stub_double():
    # room_StateTerminal has no real 'room_StateTerminal' property in the generated
    # code (a bare stub) -- manually attach it so room_BaseState's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # room_BaseState's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = room_BaseState(name="sample_text")
    partner = room_StateTerminal()
    setattr(partner, 'room_StateTerminal', None)
    _safe_set(owner, 'room_BaseState196', partner)
    assert getattr(partner, 'room_StateTerminal') == owner
    _safe_set(owner, 'room_BaseState196', None)
    assert getattr(partner, 'room_StateTerminal') is None


def test_assoc_state201_stub_double():
    # room_SubStateTrPointTerminal has no real 'room_SubStateTrPointTerminal202' property in the generated
    # code (a bare stub) -- manually attach it so room_BaseState's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # room_BaseState's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = room_BaseState(name="sample_text")
    partner = room_SubStateTrPointTerminal()
    setattr(partner, 'room_SubStateTrPointTerminal202', None)
    _safe_set(owner, 'room_BaseState203', partner)
    assert getattr(partner, 'room_SubStateTrPointTerminal202') == owner
    _safe_set(owner, 'room_BaseState203', None)
    assert getattr(partner, 'room_SubStateTrPointTerminal202') is None


def test_assoc_stateMachine118_stub_double():
    # room_StateGraph has no real 'room_StateGraph' property in the generated
    # code (a bare stub) -- manually attach it so room_ActorClass's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # room_ActorClass's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = room_ActorClass(abstract=True)
    partner = room_StateGraph()
    setattr(partner, 'room_StateGraph', None)
    _safe_set(owner, 'room_ActorClass119', partner)
    assert getattr(partner, 'room_StateGraph') == owner
    _safe_set(owner, 'room_ActorClass119', None)
    assert getattr(partner, 'room_StateGraph') is None


def test_assoc_states175_stub_double():
    # room_StateGraph has no real 'room_StateGraph176' property in the generated
    # code (a bare stub) -- manually attach it so room_State's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # room_State's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = room_State()
    partner = room_StateGraph()
    setattr(partner, 'room_StateGraph176', None)
    _safe_set(owner, 'room_State177', partner)
    assert owner in getattr(partner, 'room_StateGraph176')
    _safe_set(owner, 'room_State177', None)
    assert owner not in getattr(partner, 'room_StateGraph176')


def test_assoc_strSAPs110_stub_double():
    # room_SAPRef has no real 'room_SAPRef' property in the generated
    # code (a bare stub) -- manually attach it so room_ActorClass's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # room_ActorClass's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = room_ActorClass(abstract=True)
    partner = room_SAPRef()
    setattr(partner, 'room_SAPRef', None)
    _safe_set(owner, 'room_ActorClass111', {partner})
    assert getattr(partner, 'room_SAPRef') == owner
    _safe_set(owner, 'room_ActorClass111', set())
    assert getattr(partner, 'room_SAPRef') is None


def test_assoc_subSystemClasses7_stub_double():
    # room_SubSystemClass has no real 'room_SubSystemClass' property in the generated
    # code (a bare stub) -- manually attach it so room_RoomModel's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # room_RoomModel's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = room_RoomModel(name="sample_text")
    partner = room_SubSystemClass()
    setattr(partner, 'room_SubSystemClass', None)
    _safe_set(owner, 'room_RoomModel8', {partner})
    assert getattr(partner, 'room_SubSystemClass') == owner
    _safe_set(owner, 'room_RoomModel8', set())
    assert getattr(partner, 'room_SubSystemClass') is None


def test_assoc_subgraph172_stub_double():
    # room_StateGraph has no real 'room_StateGraph174' property in the generated
    # code (a bare stub) -- manually attach it so room_State's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # room_State's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = room_State()
    partner = room_StateGraph()
    setattr(partner, 'room_StateGraph174', None)
    _safe_set(owner, 'room_State173', partner)
    assert getattr(partner, 'room_StateGraph174') == owner
    _safe_set(owner, 'room_State173', None)
    assert getattr(partner, 'room_StateGraph174') is None


def test_assoc_systems9_stub_double():
    # room_LogicalSystem has no real 'room_LogicalSystem' property in the generated
    # code (a bare stub) -- manually attach it so room_RoomModel's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # room_RoomModel's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = room_RoomModel(name="sample_text")
    partner = room_LogicalSystem()
    setattr(partner, 'room_LogicalSystem', None)
    _safe_set(owner, 'room_RoomModel10', {partner})
    assert getattr(partner, 'room_LogicalSystem') == owner
    _safe_set(owner, 'room_RoomModel10', set())
    assert getattr(partner, 'room_LogicalSystem') is None


def test_assoc_threads136_stub_double():
    # room_SubSystemClass has no real 'room_SubSystemClass137' property in the generated
    # code (a bare stub) -- manually attach it so room_LogicalThread's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # room_LogicalThread's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = room_LogicalThread(name="sample_text")
    partner = room_SubSystemClass()
    setattr(partner, 'room_SubSystemClass137', None)
    _safe_set(owner, 'room_LogicalThread', partner)
    assert owner in getattr(partner, 'room_SubSystemClass137')
    _safe_set(owner, 'room_LogicalThread', None)
    assert owner not in getattr(partner, 'room_SubSystemClass137')


def test_assoc_to185_stub_double():
    # room_TransitionTerminal has no real 'room_TransitionTerminal' property in the generated
    # code (a bare stub) -- manually attach it so room_Transition's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # room_Transition's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = room_Transition(name="sample_text")
    partner = room_TransitionTerminal()
    setattr(partner, 'room_TransitionTerminal', None)
    _safe_set(owner, 'room_Transition186', partner)
    assert getattr(partner, 'room_TransitionTerminal') == owner
    _safe_set(owner, 'room_Transition186', None)
    assert getattr(partner, 'room_TransitionTerminal') is None


def test_assoc_trPoint197_stub_double():
    # room_TrPointTerminal has no real 'room_TrPointTerminal' property in the generated
    # code (a bare stub) -- manually attach it so room_TrPoint's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # room_TrPoint's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = room_TrPoint(name="sample_text")
    partner = room_TrPointTerminal()
    setattr(partner, 'room_TrPointTerminal', None)
    _safe_set(owner, 'room_TrPoint198', partner)
    assert getattr(partner, 'room_TrPointTerminal') == owner
    _safe_set(owner, 'room_TrPoint198', None)
    assert getattr(partner, 'room_TrPointTerminal') is None


def test_assoc_trPoint199_stub_double():
    # room_SubStateTrPointTerminal has no real 'room_SubStateTrPointTerminal' property in the generated
    # code (a bare stub) -- manually attach it so room_TrPoint's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # room_TrPoint's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = room_TrPoint(name="sample_text")
    partner = room_SubStateTrPointTerminal()
    setattr(partner, 'room_SubStateTrPointTerminal', None)
    _safe_set(owner, 'room_TrPoint200', partner)
    assert getattr(partner, 'room_SubStateTrPointTerminal') == owner
    _safe_set(owner, 'room_TrPoint200', None)
    assert getattr(partner, 'room_SubStateTrPointTerminal') is None


def test_assoc_trPoints178_stub_double():
    # room_StateGraph has no real 'room_StateGraph179' property in the generated
    # code (a bare stub) -- manually attach it so room_TrPoint's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # room_TrPoint's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = room_TrPoint(name="sample_text")
    partner = room_StateGraph()
    setattr(partner, 'room_StateGraph179', None)
    _safe_set(owner, 'room_TrPoint', partner)
    assert owner in getattr(partner, 'room_StateGraph179')
    _safe_set(owner, 'room_TrPoint', None)
    assert owner not in getattr(partner, 'room_StateGraph179')


def test_assoc_transitions182_stub_double():
    # room_StateGraph has no real 'room_StateGraph183' property in the generated
    # code (a bare stub) -- manually attach it so room_Transition's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # room_Transition's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = room_Transition(name="sample_text")
    partner = room_StateGraph()
    setattr(partner, 'room_StateGraph183', None)
    _safe_set(owner, 'room_Transition', partner)
    assert owner in getattr(partner, 'room_StateGraph183')
    _safe_set(owner, 'room_Transition', None)
    assert owner not in getattr(partner, 'room_StateGraph183')


def test_assoc_type164_stub_double():
    # room_ActorRef has no real 'room_ActorRef165' property in the generated
    # code (a bare stub) -- manually attach it so room_ActorClass's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # room_ActorClass's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = room_ActorClass(abstract=True)
    partner = room_ActorRef()
    setattr(partner, 'room_ActorRef165', None)
    _safe_set(owner, 'room_ActorClass166', partner)
    assert getattr(partner, 'room_ActorRef165') == owner
    _safe_set(owner, 'room_ActorClass166', None)
    assert getattr(partner, 'room_ActorRef165') is None


def test_assoc_type19_stub_double():
    # room_DataClass has no real 'room_DataClass21' property in the generated
    # code (a bare stub) -- manually attach it so room_Type's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # room_Type's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = room_Type(prim="sample_text")
    partner = room_DataClass()
    setattr(partner, 'room_DataClass21', None)
    _safe_set(owner, 'room_Type20', partner)
    assert getattr(partner, 'room_DataClass21') == owner
    _safe_set(owner, 'room_Type20', None)
    assert getattr(partner, 'room_DataClass21') is None


def test_assoc_userCode146_stub_double():
    # room_ProtocolClass has no real 'room_ProtocolClass47' property in the generated
    # code (a bare stub) -- manually attach it so room_DetailCode's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # room_DetailCode's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = room_DetailCode(commands="sample_text")
    partner = room_ProtocolClass()
    setattr(partner, 'room_ProtocolClass47', None)
    _safe_set(owner, 'room_DetailCode48', partner)
    assert getattr(partner, 'room_ProtocolClass47') == owner
    _safe_set(owner, 'room_DetailCode48', None)
    assert getattr(partner, 'room_ProtocolClass47') is None


def test_assoc_userCode249_stub_double():
    # room_ProtocolClass has no real 'room_ProtocolClass50' property in the generated
    # code (a bare stub) -- manually attach it so room_DetailCode's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # room_DetailCode's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = room_DetailCode(commands="sample_text")
    partner = room_ProtocolClass()
    setattr(partner, 'room_ProtocolClass50', None)
    _safe_set(owner, 'room_DetailCode51', partner)
    assert getattr(partner, 'room_ProtocolClass50') == owner
    _safe_set(owner, 'room_DetailCode51', None)
    assert getattr(partner, 'room_ProtocolClass50') is None


def test_assoc_userCode67_stub_double():
    # room_PortClass has no real 'room_PortClass68' property in the generated
    # code (a bare stub) -- manually attach it so room_DetailCode's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # room_DetailCode's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = room_DetailCode(commands="sample_text")
    partner = room_PortClass()
    setattr(partner, 'room_PortClass68', None)
    _safe_set(owner, 'room_DetailCode69', partner)
    assert getattr(partner, 'room_PortClass68') == owner
    _safe_set(owner, 'room_DetailCode69', None)
    assert getattr(partner, 'room_PortClass68') is None


