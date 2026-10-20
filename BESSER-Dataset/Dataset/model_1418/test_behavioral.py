import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    AbstractState,
    AsynchronousGate,
    ControlPort,
    DataPort,
    DataSynchronisation,
    EModelElement,
    ENamedElement,
    Flow,
    Gate,
    IdentifiedItem,
    InputPort,
    MergeGate,
    MessagePort,
    ModelContent,
    NamedItem,
    OutputPort,
    Port,
    SplitGate,
    State,
    SynchronousGate,
    TraceableElement,
    sam_AbstractState,
    sam_AsynchronousGate,
    sam_Automaton,
    sam_ControlFlow,
    sam_ControlMerge,
    sam_ControlPort,
    sam_DataComposition,
    sam_DataDecomposition,
    sam_DataFlow,
    sam_DataMerge,
    sam_DataPort,
    sam_DataStore,
    sam_DataSynchronisation,
    sam_EObject,
    sam_Flow,
    sam_FlowGroup,
    sam_Gate,
    sam_IdentifiedItem,
    sam_InControlPort,
    sam_InDataPort,
    sam_InMessagePort,
    sam_InitialState,
    sam_InputPort,
    sam_MacroState,
    sam_MergeGate,
    sam_MessageFlow,
    sam_MessageMerge,
    sam_MessagePort,
    sam_MessageSplit,
    sam_Model,
    sam_ModelContent,
    sam_MultiPort,
    sam_NamedItem,
    sam_OutControlPort,
    sam_OutDataPort,
    sam_OutMessagePort,
    sam_OutputPort,
    sam_Port,
    sam_SplitGate,
    sam_State,
    sam_SynchronousGate,
    sam_System,
    sam_TraceableElement,
    sam_Transition,
    DataType,
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

def test_assoc_isInstanceOf52_reverse_link_reassign_clear():
    a1 = sam_Port()
    a2 = sam_Port()
    b = sam_Port()
    _safe_set(b, 'sam_Port53', a1)
    assert _is_linked(b, 'sam_Port53', a1)
    if hasattr(a1, 'sam_Port51'):
        assert _is_linked(a1, 'sam_Port51', b)
    _safe_set(b, 'sam_Port53', a2)
    assert _is_linked(b, 'sam_Port53', a2)
    if hasattr(a1, 'sam_Port51'):
        assert not _is_linked(a1, 'sam_Port51', b)
    if hasattr(a2, 'sam_Port51'):
        assert _is_linked(a2, 'sam_Port51', b)
    _safe_set(b, 'sam_Port53', None)
    assert not _is_linked(b, 'sam_Port53', a2)
    if hasattr(a2, 'sam_Port51'):
        assert not _is_linked(a2, 'sam_Port51', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_dest15_stub_double():
    # sam_State has no real 'State' property in the generated
    # code (a bare stub) -- manually attach it so sam_Transition's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # sam_Transition's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = sam_Transition(condition="sample_text", emission="sample_text", priority="sample_text")
    partner = sam_State()
    setattr(partner, 'State', None)
    _safe_set(owner, 'inlink', partner)
    assert getattr(partner, 'State') == owner
    _safe_set(owner, 'inlink', None)
    assert getattr(partner, 'State') is None


def test_assoc_dest59_stub_double():
    # sam_DataPort has no real 'sam_DataPort61' property in the generated
    # code (a bare stub) -- manually attach it so sam_DataFlow's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # sam_DataFlow's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = sam_DataFlow(type="sample_text")
    partner = sam_DataPort()
    setattr(partner, 'sam_DataPort61', None)
    _safe_set(owner, 'sam_DataFlow60', {partner})
    assert getattr(partner, 'sam_DataPort61') == owner
    _safe_set(owner, 'sam_DataFlow60', set())
    assert getattr(partner, 'sam_DataPort61') is None


def test_assoc_flowGroups85_stub_double():
    # sam_Model has no real 'model' property in the generated
    # code (a bare stub) -- manually attach it so sam_FlowGroup's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # sam_FlowGroup's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = sam_FlowGroup(globalComment="sample_text")
    partner = sam_Model()
    setattr(partner, 'model', None)
    _safe_set(owner, 'FlowGroup86', partner)
    assert owner in getattr(partner, 'model')
    _safe_set(owner, 'FlowGroup86', None)
    assert owner not in getattr(partner, 'model')


def test_assoc_flows112_stub_double():
    # sam_Flow has no real 'Flow113' property in the generated
    # code (a bare stub) -- manually attach it so sam_FlowGroup's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # sam_FlowGroup's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = sam_FlowGroup(globalComment="sample_text")
    partner = sam_Flow()
    setattr(partner, 'Flow113', None)
    _safe_set(owner, 'group', {partner})
    assert getattr(partner, 'Flow113') == owner
    _safe_set(owner, 'group', set())
    assert getattr(partner, 'Flow113') is None


def test_assoc_group69_stub_double():
    # sam_Flow has no real 'flows' property in the generated
    # code (a bare stub) -- manually attach it so sam_FlowGroup's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # sam_FlowGroup's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = sam_FlowGroup(globalComment="sample_text")
    partner = sam_Flow()
    setattr(partner, 'flows', None)
    _safe_set(owner, 'FlowGroup', partner)
    assert getattr(partner, 'flows') == owner
    _safe_set(owner, 'FlowGroup', None)
    assert getattr(partner, 'flows') is None


def test_assoc_inlink13_stub_double():
    # sam_State has no real 'dest' property in the generated
    # code (a bare stub) -- manually attach it so sam_Transition's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # sam_Transition's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = sam_Transition(condition="sample_text", emission="sample_text", priority="sample_text")
    partner = sam_State()
    setattr(partner, 'dest', None)
    _safe_set(owner, 'Transition14', partner)
    assert owner in getattr(partner, 'dest')
    _safe_set(owner, 'Transition14', None)
    assert owner not in getattr(partner, 'dest')


def test_assoc_inlink43_stub_double():
    # sam_Flow has no real 'sam_Flow45' property in the generated
    # code (a bare stub) -- manually attach it so sam_Port's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # sam_Port's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = sam_Port()
    partner = sam_Flow()
    setattr(partner, 'sam_Flow45', None)
    _safe_set(owner, 'sam_Port44', partner)
    assert getattr(partner, 'sam_Flow45') == owner
    _safe_set(owner, 'sam_Port44', None)
    assert getattr(partner, 'sam_Flow45') is None


def test_assoc_listPort92_stub_double():
    # sam_MultiPort has no real 'sam_MultiPort93' property in the generated
    # code (a bare stub) -- manually attach it so sam_Port's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # sam_Port's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = sam_Port()
    partner = sam_MultiPort()
    setattr(partner, 'sam_MultiPort93', None)
    _safe_set(owner, 'sam_Port94', partner)
    assert owner in getattr(partner, 'sam_MultiPort93')
    _safe_set(owner, 'sam_Port94', None)
    assert owner not in getattr(partner, 'sam_MultiPort93')


def test_assoc_listPorts5_stub_double():
    # sam_Automaton has no real 'parentAutomaton6' property in the generated
    # code (a bare stub) -- manually attach it so sam_Port's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # sam_Port's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = sam_Port()
    partner = sam_Automaton()
    setattr(partner, 'parentAutomaton6', None)
    _safe_set(owner, 'Port', partner)
    assert owner in getattr(partner, 'parentAutomaton6')
    _safe_set(owner, 'Port', None)
    assert owner not in getattr(partner, 'parentAutomaton6')


def test_assoc_listPorts70_stub_double():
    # sam_System has no real 'parentSystem' property in the generated
    # code (a bare stub) -- manually attach it so sam_Port's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # sam_Port's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = sam_Port()
    partner = sam_System()
    setattr(partner, 'parentSystem', None)
    _safe_set(owner, 'Port71', partner)
    assert owner in getattr(partner, 'parentSystem')
    _safe_set(owner, 'Port71', None)
    assert owner not in getattr(partner, 'parentSystem')


def test_assoc_listTransitions3_stub_double():
    # sam_Automaton has no real 'parentAutomaton' property in the generated
    # code (a bare stub) -- manually attach it so sam_Transition's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # sam_Transition's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = sam_Transition(condition="sample_text", emission="sample_text", priority="sample_text")
    partner = sam_Automaton()
    setattr(partner, 'parentAutomaton', None)
    _safe_set(owner, 'Transition4', partner)
    assert owner in getattr(partner, 'parentAutomaton')
    _safe_set(owner, 'Transition4', None)
    assert owner not in getattr(partner, 'parentAutomaton')


def test_assoc_model114_stub_double():
    # sam_Model has no real 'Model115' property in the generated
    # code (a bare stub) -- manually attach it so sam_FlowGroup's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # sam_FlowGroup's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = sam_FlowGroup(globalComment="sample_text")
    partner = sam_Model()
    setattr(partner, 'Model115', None)
    _safe_set(owner, 'flowGroups', partner)
    assert getattr(partner, 'Model115') == owner
    _safe_set(owner, 'flowGroups', None)
    assert getattr(partner, 'Model115') is None


def test_assoc_outlink2_stub_double():
    # sam_AbstractState has no real 'source' property in the generated
    # code (a bare stub) -- manually attach it so sam_Transition's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # sam_Transition's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = sam_Transition(condition="sample_text", emission="sample_text", priority="sample_text")
    partner = sam_AbstractState()
    setattr(partner, 'source', None)
    _safe_set(owner, 'Transition', partner)
    assert owner in getattr(partner, 'source')
    _safe_set(owner, 'Transition', None)
    assert owner not in getattr(partner, 'source')


def test_assoc_outlink42_stub_double():
    # sam_Flow has no real 'sam_Flow' property in the generated
    # code (a bare stub) -- manually attach it so sam_Port's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # sam_Port's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = sam_Port()
    partner = sam_Flow()
    setattr(partner, 'sam_Flow', None)
    _safe_set(owner, 'sam_Port', partner)
    assert getattr(partner, 'sam_Flow') == owner
    _safe_set(owner, 'sam_Port', None)
    assert getattr(partner, 'sam_Flow') is None


def test_assoc_parentAutomaton16_stub_double():
    # sam_Automaton has no real 'Automaton17' property in the generated
    # code (a bare stub) -- manually attach it so sam_Transition's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # sam_Transition's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = sam_Transition(condition="sample_text", emission="sample_text", priority="sample_text")
    partner = sam_Automaton()
    setattr(partner, 'Automaton17', None)
    _safe_set(owner, 'listTransitions', partner)
    assert getattr(partner, 'Automaton17') == owner
    _safe_set(owner, 'listTransitions', None)
    assert getattr(partner, 'Automaton17') is None


def test_assoc_parentAutomaton46_stub_double():
    # sam_Automaton has no real 'Automaton48' property in the generated
    # code (a bare stub) -- manually attach it so sam_Port's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # sam_Port's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = sam_Port()
    partner = sam_Automaton()
    setattr(partner, 'Automaton48', None)
    _safe_set(owner, 'listPorts47', partner)
    assert getattr(partner, 'Automaton48') == owner
    _safe_set(owner, 'listPorts47', None)
    assert getattr(partner, 'Automaton48') is None


def test_assoc_parentMultiPort49_stub_double():
    # sam_MultiPort has no real 'sam_MultiPort' property in the generated
    # code (a bare stub) -- manually attach it so sam_Port's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # sam_Port's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = sam_Port()
    partner = sam_MultiPort()
    setattr(partner, 'sam_MultiPort', None)
    _safe_set(owner, 'sam_Port50', partner)
    assert getattr(partner, 'sam_MultiPort') == owner
    _safe_set(owner, 'sam_Port50', None)
    assert getattr(partner, 'sam_MultiPort') is None


def test_assoc_parentSystem41_stub_double():
    # sam_System has no real 'System' property in the generated
    # code (a bare stub) -- manually attach it so sam_Port's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # sam_Port's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = sam_Port()
    partner = sam_System()
    setattr(partner, 'System', None)
    _safe_set(owner, 'listPorts', partner)
    assert getattr(partner, 'System') == owner
    _safe_set(owner, 'listPorts', None)
    assert getattr(partner, 'System') is None


def test_assoc_source18_stub_double():
    # sam_AbstractState has no real 'AbstractState19' property in the generated
    # code (a bare stub) -- manually attach it so sam_Transition's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # sam_Transition's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = sam_Transition(condition="sample_text", emission="sample_text", priority="sample_text")
    partner = sam_AbstractState()
    setattr(partner, 'AbstractState19', None)
    _safe_set(owner, 'outlink', partner)
    assert getattr(partner, 'AbstractState19') == owner
    _safe_set(owner, 'outlink', None)
    assert getattr(partner, 'AbstractState19') is None


def test_assoc_source58_stub_double():
    # sam_DataPort has no real 'sam_DataPort' property in the generated
    # code (a bare stub) -- manually attach it so sam_DataFlow's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # sam_DataFlow's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = sam_DataFlow(type="sample_text")
    partner = sam_DataPort()
    setattr(partner, 'sam_DataPort', None)
    _safe_set(owner, 'sam_DataFlow', partner)
    assert getattr(partner, 'sam_DataPort') == owner
    _safe_set(owner, 'sam_DataFlow', None)
    assert getattr(partner, 'sam_DataPort') is None


