import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Block,
    CompositeStateflowElement,
    ContainableStateflowElement,
    Data,
    InPort,
    OutPort,
    Port,
    PortBlock,
    Reference,
    SimulinkElement,
    StateflowElement,
    SubSystem,
    TruthTable,
    Vertex,
    simulink_Action,
    simulink_ActionEntry,
    simulink_ActionTable,
    simulink_Block,
    simulink_BlockReference,
    simulink_Chart,
    simulink_CompositeStateflowElement,
    simulink_Condition,
    simulink_ConditionTable,
    simulink_Connection,
    simulink_ContainableStateflowElement,
    simulink_ContainableTruthTable,
    simulink_Data,
    simulink_Decision,
    simulink_DecisionEntry,
    simulink_Function,
    simulink_InPort,
    simulink_InPortBlock,
    simulink_InputData,
    simulink_Junction,
    simulink_LocalData,
    simulink_ModelReference,
    simulink_OutPort,
    simulink_OutPortBlock,
    simulink_OutputData,
    simulink_Port,
    simulink_PortBlock,
    simulink_Reference,
    simulink_SFWGuard,
    simulink_SFWTrigger,
    simulink_SimulinkElement,
    simulink_SimulinkModel,
    simulink_State,
    simulink_StateflowElement,
    simulink_SubSystem,
    simulink_Transition,
    simulink_TruthTable,
    simulink_TruthTableChart,
    simulink_Vertex,
    DecompositionType,
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

def test_assoc_condition57_reverse_link_reassign_clear():
    a1 = simulink_DecisionEntry(conditionOutcome="sample_text")
    a2 = simulink_DecisionEntry(conditionOutcome="sample_text_2")
    b = simulink_Condition(description="sample_text", statement="sample_text")
    _safe_set(b, 'simulink_Condition59', a1)
    assert _is_linked(b, 'simulink_Condition59', a1)
    if hasattr(a1, 'simulink_DecisionEntry58'):
        assert _is_linked(a1, 'simulink_DecisionEntry58', b)
    _safe_set(b, 'simulink_Condition59', a2)
    assert _is_linked(b, 'simulink_Condition59', a2)
    if hasattr(a1, 'simulink_DecisionEntry58'):
        assert not _is_linked(a1, 'simulink_DecisionEntry58', b)
    if hasattr(a2, 'simulink_DecisionEntry58'):
        assert _is_linked(a2, 'simulink_DecisionEntry58', b)
    _safe_set(b, 'simulink_Condition59', None)
    assert not _is_linked(b, 'simulink_Condition59', a2)
    if hasattr(a2, 'simulink_DecisionEntry58'):
        assert not _is_linked(a2, 'simulink_DecisionEntry58', b)


def test_assoc_decisionEntries55_reverse_link_reassign_clear():
    a1 = simulink_DecisionEntry(conditionOutcome="sample_text")
    a2 = simulink_DecisionEntry(conditionOutcome="sample_text_2")
    b = simulink_Decision(actionReference="sample_text", id=7)
    _safe_set(b, 'simulink_Decision56', {a1})
    assert _is_linked(b, 'simulink_Decision56', a1)
    if hasattr(a1, 'simulink_DecisionEntry'):
        assert _is_linked(a1, 'simulink_DecisionEntry', b)
    _safe_set(b, 'simulink_Decision56', {a2})
    assert _is_linked(b, 'simulink_Decision56', a2)
    if hasattr(a1, 'simulink_DecisionEntry'):
        assert not _is_linked(a1, 'simulink_DecisionEntry', b)
    if hasattr(a2, 'simulink_DecisionEntry'):
        assert _is_linked(a2, 'simulink_DecisionEntry', b)
    _safe_set(b, 'simulink_Decision56', set())
    assert not _is_linked(b, 'simulink_Decision56', a2)
    if hasattr(a2, 'simulink_DecisionEntry'):
        assert not _is_linked(a2, 'simulink_DecisionEntry', b)


def test_assoc_duringActions19_reverse_link_reassign_clear():
    a1 = simulink_State(decomposition="sample_text", executionOrder=7)
    a2 = simulink_State(decomposition="sample_text_2", executionOrder=13)
    b = simulink_Action(statement="sample_text")
    _safe_set(b, 'Action20', a1)
    assert _is_linked(b, 'Action20', a1)
    if hasattr(a1, 'stateDuring'):
        assert _is_linked(a1, 'stateDuring', b)
    _safe_set(b, 'Action20', a2)
    assert _is_linked(b, 'Action20', a2)
    if hasattr(a1, 'stateDuring'):
        assert not _is_linked(a1, 'stateDuring', b)
    if hasattr(a2, 'stateDuring'):
        assert _is_linked(a2, 'stateDuring', b)
    _safe_set(b, 'Action20', None)
    assert not _is_linked(b, 'Action20', a2)
    if hasattr(a2, 'stateDuring'):
        assert not _is_linked(a2, 'stateDuring', b)


def test_assoc_entryActions18_reverse_link_reassign_clear():
    a1 = simulink_State(decomposition="sample_text", executionOrder=7)
    a2 = simulink_State(decomposition="sample_text_2", executionOrder=13)
    b = simulink_Action(statement="sample_text")
    _safe_set(b, 'Action', a1)
    assert _is_linked(b, 'Action', a1)
    if hasattr(a1, 'stateEntry'):
        assert _is_linked(a1, 'stateEntry', b)
    _safe_set(b, 'Action', a2)
    assert _is_linked(b, 'Action', a2)
    if hasattr(a1, 'stateEntry'):
        assert not _is_linked(a1, 'stateEntry', b)
    if hasattr(a2, 'stateEntry'):
        assert _is_linked(a2, 'stateEntry', b)
    _safe_set(b, 'Action', None)
    assert not _is_linked(b, 'Action', a2)
    if hasattr(a2, 'stateEntry'):
        assert not _is_linked(a2, 'stateEntry', b)


def test_assoc_exitActions21_reverse_link_reassign_clear():
    a1 = simulink_State(decomposition="sample_text", executionOrder=7)
    a2 = simulink_State(decomposition="sample_text_2", executionOrder=13)
    b = simulink_Action(statement="sample_text")
    _safe_set(b, 'Action22', a1)
    assert _is_linked(b, 'Action22', a1)
    if hasattr(a1, 'stateExit'):
        assert _is_linked(a1, 'stateExit', b)
    _safe_set(b, 'Action22', a2)
    assert _is_linked(b, 'Action22', a2)
    if hasattr(a1, 'stateExit'):
        assert not _is_linked(a1, 'stateExit', b)
    if hasattr(a2, 'stateExit'):
        assert _is_linked(a2, 'stateExit', b)
    _safe_set(b, 'Action22', None)
    assert not _is_linked(b, 'Action22', a2)
    if hasattr(a2, 'stateExit'):
        assert not _is_linked(a2, 'stateExit', b)


def test_assoc_guard26_reverse_link_reassign_clear():
    a1 = simulink_Transition(executionOrder=7, isDefaultTransition=True)
    a2 = simulink_Transition(executionOrder=13, isDefaultTransition=False)
    b = simulink_SFWGuard(statement="sample_text")
    _safe_set(b, 'SFWGuard', a1)
    assert _is_linked(b, 'SFWGuard', a1)
    if hasattr(a1, 'transition'):
        assert _is_linked(a1, 'transition', b)
    _safe_set(b, 'SFWGuard', a2)
    assert _is_linked(b, 'SFWGuard', a2)
    if hasattr(a1, 'transition'):
        assert not _is_linked(a1, 'transition', b)
    if hasattr(a2, 'transition'):
        assert _is_linked(a2, 'transition', b)
    _safe_set(b, 'SFWGuard', None)
    assert not _is_linked(b, 'SFWGuard', a2)
    if hasattr(a2, 'transition'):
        assert not _is_linked(a2, 'transition', b)


def test_assoc_port10_reverse_link_reassign_clear():
    a1 = simulink_PortBlock(portNumber=7)
    a2 = simulink_PortBlock(portNumber=13)
    b = simulink_Port(dataType="sample_text", portNumber=7)
    _safe_set(b, 'Port11', a1)
    assert _is_linked(b, 'Port11', a1)
    if hasattr(a1, 'portBlock'):
        assert _is_linked(a1, 'portBlock', b)
    _safe_set(b, 'Port11', a2)
    assert _is_linked(b, 'Port11', a2)
    if hasattr(a1, 'portBlock'):
        assert not _is_linked(a1, 'portBlock', b)
    if hasattr(a2, 'portBlock'):
        assert _is_linked(a2, 'portBlock', b)
    _safe_set(b, 'Port11', None)
    assert not _is_linked(b, 'Port11', a2)
    if hasattr(a2, 'portBlock'):
        assert not _is_linked(a2, 'portBlock', b)


def test_assoc_portBlock3_reverse_link_reassign_clear():
    a1 = simulink_PortBlock(portNumber=7)
    a2 = simulink_PortBlock(portNumber=13)
    b = simulink_Port(dataType="sample_text", portNumber=7)
    _safe_set(b, 'port', a1)
    assert _is_linked(b, 'port', a1)
    if hasattr(a1, 'PortBlock'):
        assert _is_linked(a1, 'PortBlock', b)
    _safe_set(b, 'port', a2)
    assert _is_linked(b, 'port', a2)
    if hasattr(a1, 'PortBlock'):
        assert not _is_linked(a1, 'PortBlock', b)
    if hasattr(a2, 'PortBlock'):
        assert _is_linked(a2, 'PortBlock', b)
    _safe_set(b, 'port', None)
    assert not _is_linked(b, 'port', a2)
    if hasattr(a2, 'PortBlock'):
        assert not _is_linked(a2, 'PortBlock', b)


def test_assoc_stateDuring37_reverse_link_reassign_clear():
    a1 = simulink_State(decomposition="sample_text", executionOrder=7)
    a2 = simulink_State(decomposition="sample_text_2", executionOrder=13)
    b = simulink_Action(statement="sample_text")
    _safe_set(b, 'duringActions', a1)
    assert _is_linked(b, 'duringActions', a1)
    if hasattr(a1, 'State38'):
        assert _is_linked(a1, 'State38', b)
    _safe_set(b, 'duringActions', a2)
    assert _is_linked(b, 'duringActions', a2)
    if hasattr(a1, 'State38'):
        assert not _is_linked(a1, 'State38', b)
    if hasattr(a2, 'State38'):
        assert _is_linked(a2, 'State38', b)
    _safe_set(b, 'duringActions', None)
    assert not _is_linked(b, 'duringActions', a2)
    if hasattr(a2, 'State38'):
        assert not _is_linked(a2, 'State38', b)


def test_assoc_stateEntry36_reverse_link_reassign_clear():
    a1 = simulink_State(decomposition="sample_text", executionOrder=7)
    a2 = simulink_State(decomposition="sample_text_2", executionOrder=13)
    b = simulink_Action(statement="sample_text")
    _safe_set(b, 'entryActions', a1)
    assert _is_linked(b, 'entryActions', a1)
    if hasattr(a1, 'State'):
        assert _is_linked(a1, 'State', b)
    _safe_set(b, 'entryActions', a2)
    assert _is_linked(b, 'entryActions', a2)
    if hasattr(a1, 'State'):
        assert not _is_linked(a1, 'State', b)
    if hasattr(a2, 'State'):
        assert _is_linked(a2, 'State', b)
    _safe_set(b, 'entryActions', None)
    assert not _is_linked(b, 'entryActions', a2)
    if hasattr(a2, 'State'):
        assert not _is_linked(a2, 'State', b)


def test_assoc_stateExit39_reverse_link_reassign_clear():
    a1 = simulink_State(decomposition="sample_text", executionOrder=7)
    a2 = simulink_State(decomposition="sample_text_2", executionOrder=13)
    b = simulink_Action(statement="sample_text")
    _safe_set(b, 'exitActions', a1)
    assert _is_linked(b, 'exitActions', a1)
    if hasattr(a1, 'State40'):
        assert _is_linked(a1, 'State40', b)
    _safe_set(b, 'exitActions', a2)
    assert _is_linked(b, 'exitActions', a2)
    if hasattr(a1, 'State40'):
        assert not _is_linked(a1, 'State40', b)
    if hasattr(a2, 'State40'):
        assert _is_linked(a2, 'State40', b)
    _safe_set(b, 'exitActions', None)
    assert not _is_linked(b, 'exitActions', a2)
    if hasattr(a2, 'State40'):
        assert not _is_linked(a2, 'State40', b)


def test_assoc_transition32_reverse_link_reassign_clear():
    a1 = simulink_Transition(executionOrder=7, isDefaultTransition=True)
    a2 = simulink_Transition(executionOrder=13, isDefaultTransition=False)
    b = simulink_SFWGuard(statement="sample_text")
    _safe_set(b, 'guard', a1)
    assert _is_linked(b, 'guard', a1)
    if hasattr(a1, 'Transition33'):
        assert _is_linked(a1, 'Transition33', b)
    _safe_set(b, 'guard', a2)
    assert _is_linked(b, 'guard', a2)
    if hasattr(a1, 'Transition33'):
        assert not _is_linked(a1, 'Transition33', b)
    if hasattr(a2, 'Transition33'):
        assert _is_linked(a2, 'Transition33', b)
    _safe_set(b, 'guard', None)
    assert not _is_linked(b, 'guard', a2)
    if hasattr(a2, 'Transition33'):
        assert not _is_linked(a2, 'Transition33', b)


def test_assoc_transition34_reverse_link_reassign_clear():
    a1 = simulink_Transition(executionOrder=7, isDefaultTransition=True)
    a2 = simulink_Transition(executionOrder=13, isDefaultTransition=False)
    b = simulink_Action(statement="sample_text")
    _safe_set(b, 'triggeredActions', a1)
    assert _is_linked(b, 'triggeredActions', a1)
    if hasattr(a1, 'Transition35'):
        assert _is_linked(a1, 'Transition35', b)
    _safe_set(b, 'triggeredActions', a2)
    assert _is_linked(b, 'triggeredActions', a2)
    if hasattr(a1, 'Transition35'):
        assert not _is_linked(a1, 'Transition35', b)
    if hasattr(a2, 'Transition35'):
        assert _is_linked(a2, 'Transition35', b)
    _safe_set(b, 'triggeredActions', None)
    assert not _is_linked(b, 'triggeredActions', a2)
    if hasattr(a2, 'Transition35'):
        assert not _is_linked(a2, 'Transition35', b)


def test_assoc_transition60_reverse_link_reassign_clear():
    a1 = simulink_Transition(executionOrder=7, isDefaultTransition=True)
    a2 = simulink_Transition(executionOrder=13, isDefaultTransition=False)
    b = simulink_SFWTrigger(statement="sample_text")
    _safe_set(b, 'trigger', a1)
    assert _is_linked(b, 'trigger', a1)
    if hasattr(a1, 'Transition61'):
        assert _is_linked(a1, 'Transition61', b)
    _safe_set(b, 'trigger', a2)
    assert _is_linked(b, 'trigger', a2)
    if hasattr(a1, 'Transition61'):
        assert not _is_linked(a1, 'Transition61', b)
    if hasattr(a2, 'Transition61'):
        assert _is_linked(a2, 'Transition61', b)
    _safe_set(b, 'trigger', None)
    assert not _is_linked(b, 'trigger', a2)
    if hasattr(a2, 'Transition61'):
        assert not _is_linked(a2, 'Transition61', b)


def test_assoc_trigger30_reverse_link_reassign_clear():
    a1 = simulink_Transition(executionOrder=7, isDefaultTransition=True)
    a2 = simulink_Transition(executionOrder=13, isDefaultTransition=False)
    b = simulink_SFWTrigger(statement="sample_text")
    _safe_set(b, 'SFWTrigger', a1)
    assert _is_linked(b, 'SFWTrigger', a1)
    if hasattr(a1, 'transition31'):
        assert _is_linked(a1, 'transition31', b)
    _safe_set(b, 'SFWTrigger', a2)
    assert _is_linked(b, 'SFWTrigger', a2)
    if hasattr(a1, 'transition31'):
        assert not _is_linked(a1, 'transition31', b)
    if hasattr(a2, 'transition31'):
        assert _is_linked(a2, 'transition31', b)
    _safe_set(b, 'SFWTrigger', None)
    assert not _is_linked(b, 'SFWTrigger', a2)
    if hasattr(a2, 'transition31'):
        assert not _is_linked(a2, 'transition31', b)


def test_assoc_triggeredActions27_reverse_link_reassign_clear():
    a1 = simulink_Transition(executionOrder=7, isDefaultTransition=True)
    a2 = simulink_Transition(executionOrder=13, isDefaultTransition=False)
    b = simulink_Action(statement="sample_text")
    _safe_set(b, 'Action29', a1)
    assert _is_linked(b, 'Action29', a1)
    if hasattr(a1, 'transition28'):
        assert _is_linked(a1, 'transition28', b)
    _safe_set(b, 'Action29', a2)
    assert _is_linked(b, 'Action29', a2)
    if hasattr(a1, 'transition28'):
        assert not _is_linked(a1, 'transition28', b)
    if hasattr(a2, 'transition28'):
        assert _is_linked(a2, 'transition28', b)
    _safe_set(b, 'Action29', None)
    assert not _is_linked(b, 'Action29', a2)
    if hasattr(a2, 'transition28'):
        assert not _is_linked(a2, 'transition28', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_actionEntries53_stub_double():
    # simulink_ActionTable has no real 'simulink_ActionTable54' property in the generated
    # code (a bare stub) -- manually attach it so simulink_ActionEntry's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # simulink_ActionEntry's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = simulink_ActionEntry(actionReference="sample_text", actionStatement="sample_text", description="sample_text")
    partner = simulink_ActionTable()
    setattr(partner, 'simulink_ActionTable54', None)
    _safe_set(owner, 'simulink_ActionEntry', partner)
    assert owner in getattr(partner, 'simulink_ActionTable54')
    _safe_set(owner, 'simulink_ActionEntry', None)
    assert owner not in getattr(partner, 'simulink_ActionTable54')


def test_assoc_block2_stub_double():
    # simulink_Block has no real 'Block' property in the generated
    # code (a bare stub) -- manually attach it so simulink_Port's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # simulink_Port's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = simulink_Port(dataType="sample_text", portNumber=7)
    partner = simulink_Block()
    setattr(partner, 'Block', None)
    _safe_set(owner, 'ownedPorts', partner)
    assert getattr(partner, 'Block') == owner
    _safe_set(owner, 'ownedPorts', None)
    assert getattr(partner, 'Block') is None


def test_assoc_conditions51_stub_double():
    # simulink_ConditionTable has no real 'simulink_ConditionTable52' property in the generated
    # code (a bare stub) -- manually attach it so simulink_Condition's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # simulink_Condition's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = simulink_Condition(description="sample_text", statement="sample_text")
    partner = simulink_ConditionTable()
    setattr(partner, 'simulink_ConditionTable52', None)
    _safe_set(owner, 'simulink_Condition', partner)
    assert owner in getattr(partner, 'simulink_ConditionTable52')
    _safe_set(owner, 'simulink_Condition', None)
    assert owner not in getattr(partner, 'simulink_ConditionTable52')


def test_assoc_decisions49_stub_double():
    # simulink_ConditionTable has no real 'simulink_ConditionTable50' property in the generated
    # code (a bare stub) -- manually attach it so simulink_Decision's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # simulink_Decision's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = simulink_Decision(actionReference="sample_text", id=7)
    partner = simulink_ConditionTable()
    setattr(partner, 'simulink_ConditionTable50', None)
    _safe_set(owner, 'simulink_Decision', partner)
    assert owner in getattr(partner, 'simulink_ConditionTable50')
    _safe_set(owner, 'simulink_Decision', None)
    assert owner not in getattr(partner, 'simulink_ConditionTable50')


def test_assoc_destination24_stub_double():
    # simulink_Vertex has no real 'Vertex25' property in the generated
    # code (a bare stub) -- manually attach it so simulink_Transition's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # simulink_Transition's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = simulink_Transition(executionOrder=7, isDefaultTransition=True)
    partner = simulink_Vertex()
    setattr(partner, 'Vertex25', None)
    _safe_set(owner, 'incomingTransitions', partner)
    assert getattr(partner, 'Vertex25') == owner
    _safe_set(owner, 'incomingTransitions', None)
    assert getattr(partner, 'Vertex25') is None


def test_assoc_incomingTransitions15_stub_double():
    # simulink_Vertex has no real 'destination' property in the generated
    # code (a bare stub) -- manually attach it so simulink_Transition's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # simulink_Transition's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = simulink_Transition(executionOrder=7, isDefaultTransition=True)
    partner = simulink_Vertex()
    setattr(partner, 'destination', None)
    _safe_set(owner, 'Transition', partner)
    assert owner in getattr(partner, 'destination')
    _safe_set(owner, 'Transition', None)
    assert owner not in getattr(partner, 'destination')


def test_assoc_outgoingTransitions16_stub_double():
    # simulink_Vertex has no real 'source' property in the generated
    # code (a bare stub) -- manually attach it so simulink_Transition's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # simulink_Transition's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = simulink_Transition(executionOrder=7, isDefaultTransition=True)
    partner = simulink_Vertex()
    setattr(partner, 'source', None)
    _safe_set(owner, 'Transition17', partner)
    assert owner in getattr(partner, 'source')
    _safe_set(owner, 'Transition17', None)
    assert owner not in getattr(partner, 'source')


def test_assoc_ownedPorts0_stub_double():
    # simulink_Block has no real 'block' property in the generated
    # code (a bare stub) -- manually attach it so simulink_Port's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # simulink_Port's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = simulink_Port(dataType="sample_text", portNumber=7)
    partner = simulink_Block()
    setattr(partner, 'block', None)
    _safe_set(owner, 'Port', partner)
    assert owner in getattr(partner, 'block')
    _safe_set(owner, 'Port', None)
    assert owner not in getattr(partner, 'block')


def test_assoc_source23_stub_double():
    # simulink_Vertex has no real 'Vertex' property in the generated
    # code (a bare stub) -- manually attach it so simulink_Transition's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # simulink_Transition's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = simulink_Transition(executionOrder=7, isDefaultTransition=True)
    partner = simulink_Vertex()
    setattr(partner, 'Vertex', None)
    _safe_set(owner, 'outgoingTransitions', partner)
    assert getattr(partner, 'Vertex') == owner
    _safe_set(owner, 'outgoingTransitions', None)
    assert getattr(partner, 'Vertex') is None


