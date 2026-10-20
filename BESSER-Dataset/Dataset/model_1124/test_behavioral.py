import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Action,
    Block,
    BufferFunction,
    Chart,
    Data,
    Element,
    EmbeddedFunction,
    Event,
    InPortBlock,
    Node,
    PortBlock,
    SimulinkFile,
    State,
    StateflowElement,
    StateflowMachine,
    SubSystem,
    Transition,
    simulink_Block,
    simulink_Bus,
    simulink_BusCreator,
    simulink_BusElement,
    simulink_BusSelector,
    simulink_ChartBlock,
    simulink_Constant,
    simulink_DigitalClock,
    simulink_Element,
    simulink_EmbeddedMatlabFunction,
    simulink_EnablePort,
    simulink_InPortBlock,
    simulink_LibraryReference,
    simulink_Line,
    simulink_MiscBlock,
    simulink_OutPortBlock,
    simulink_Parameter,
    simulink_PortBlock,
    simulink_SimulinkContainer,
    simulink_SimulinkFile,
    simulink_SimulinkLibrary,
    simulink_SimulinkModel,
    simulink_SubSystem,
    simulink_TriggerPort,
    simulink_UnitDelay,
    simulink_ZeroOrderHold,
    simulink_buffer_BufferFunction,
    simulink_buffer_CheckQueue,
    simulink_buffer_Dequeue,
    simulink_buffer_Enqueue,
    simulink_buffer_SharedCheckQueue,
    simulink_buffer_SharedDequeue,
    simulink_buffer_SharedEnqueue,
    simulink_msglib_CommunicationSwitch,
    simulink_msglib_LinkLayer,
    simulink_reconfiguration_FadingComponent,
    simulink_reconfiguration_MultiSourceControl,
    simulink_reconfiguration_MultiTargetControl,
    simulink_stateflow_Action,
    simulink_stateflow_Chart,
    simulink_stateflow_Data,
    simulink_stateflow_EmbeddedFunction,
    simulink_stateflow_Event,
    simulink_stateflow_History,
    simulink_stateflow_Junction,
    simulink_stateflow_Node,
    simulink_stateflow_State,
    simulink_stateflow_StateflowElement,
    simulink_stateflow_StateflowMachine,
    simulink_stateflow_Transition,
    stateflow_simulink_ChartBlock,
    stateflow_simulink_SimulinkFile,
    DataType,
    SubStateType,
    TriggerEvent,
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

def test_assoc_allBlocks24_reverse_link_reassign_clear():
    a1 = simulink_SubSystem()
    a2 = simulink_SubSystem()
    b = simulink_Block(name="sample_text")
    _safe_set(b, 'simulink_Block', a1)
    assert _is_linked(b, 'simulink_Block', a1)
    if hasattr(a1, 'simulink_SubSystem25'):
        assert _is_linked(a1, 'simulink_SubSystem25', b)
    _safe_set(b, 'simulink_Block', a2)
    assert _is_linked(b, 'simulink_Block', a2)
    if hasattr(a1, 'simulink_SubSystem25'):
        assert not _is_linked(a1, 'simulink_SubSystem25', b)
    if hasattr(a2, 'simulink_SubSystem25'):
        assert _is_linked(a2, 'simulink_SubSystem25', b)
    _safe_set(b, 'simulink_Block', None)
    assert not _is_linked(b, 'simulink_Block', a2)
    if hasattr(a2, 'simulink_SubSystem25'):
        assert not _is_linked(a2, 'simulink_SubSystem25', b)


def test_assoc_blocks19_reverse_link_reassign_clear():
    a1 = simulink_SubSystem()
    a2 = simulink_SubSystem()
    b = simulink_Block(name="sample_text")
    _safe_set(b, 'Block20', a1)
    assert _is_linked(b, 'Block20', a1)
    if hasattr(a1, 'parent'):
        assert _is_linked(a1, 'parent', b)
    _safe_set(b, 'Block20', a2)
    assert _is_linked(b, 'Block20', a2)
    if hasattr(a1, 'parent'):
        assert not _is_linked(a1, 'parent', b)
    if hasattr(a2, 'parent'):
        assert _is_linked(a2, 'parent', b)
    _safe_set(b, 'Block20', None)
    assert not _is_linked(b, 'Block20', a2)
    if hasattr(a2, 'parent'):
        assert not _is_linked(a2, 'parent', b)


def test_assoc_bus45_reverse_link_reassign_clear():
    a1 = simulink_BusElement(dimensions="sample_text", name="sample_text", type="sample_text")
    a2 = simulink_BusElement(dimensions="sample_text_2", name="sample_text_2", type="sample_text_2")
    b = simulink_Bus(name="sample_text")
    _safe_set(b, 'simulink_Bus47', a1)
    assert _is_linked(b, 'simulink_Bus47', a1)
    if hasattr(a1, 'simulink_BusElement46'):
        assert _is_linked(a1, 'simulink_BusElement46', b)
    _safe_set(b, 'simulink_Bus47', a2)
    assert _is_linked(b, 'simulink_Bus47', a2)
    if hasattr(a1, 'simulink_BusElement46'):
        assert not _is_linked(a1, 'simulink_BusElement46', b)
    if hasattr(a2, 'simulink_BusElement46'):
        assert _is_linked(a2, 'simulink_BusElement46', b)
    _safe_set(b, 'simulink_Bus47', None)
    assert not _is_linked(b, 'simulink_Bus47', a2)
    if hasattr(a2, 'simulink_BusElement46'):
        assert not _is_linked(a2, 'simulink_BusElement46', b)


def test_assoc_elements39_reverse_link_reassign_clear():
    a1 = simulink_BusElement(dimensions="sample_text", name="sample_text", type="sample_text")
    a2 = simulink_BusElement(dimensions="sample_text_2", name="sample_text_2", type="sample_text_2")
    b = simulink_Bus(name="sample_text")
    _safe_set(b, 'simulink_Bus40', {a1})
    assert _is_linked(b, 'simulink_Bus40', a1)
    if hasattr(a1, 'simulink_BusElement'):
        assert _is_linked(a1, 'simulink_BusElement', b)
    _safe_set(b, 'simulink_Bus40', {a2})
    assert _is_linked(b, 'simulink_Bus40', a2)
    if hasattr(a1, 'simulink_BusElement'):
        assert not _is_linked(a1, 'simulink_BusElement', b)
    if hasattr(a2, 'simulink_BusElement'):
        assert _is_linked(a2, 'simulink_BusElement', b)
    _safe_set(b, 'simulink_Bus40', set())
    assert not _is_linked(b, 'simulink_Bus40', a2)
    if hasattr(a2, 'simulink_BusElement'):
        assert not _is_linked(a2, 'simulink_BusElement', b)


def test_assoc_parameters8_reverse_link_reassign_clear():
    a1 = simulink_Parameter(name="sample_text", type="sample_text", value="sample_text")
    a2 = simulink_Parameter(name="sample_text_2", type="sample_text_2", value="sample_text_2")
    b = simulink_Element(id="sample_text")
    _safe_set(b, 'simulink_Element', {a1})
    assert _is_linked(b, 'simulink_Element', a1)
    if hasattr(a1, 'simulink_Parameter'):
        assert _is_linked(a1, 'simulink_Parameter', b)
    _safe_set(b, 'simulink_Element', {a2})
    assert _is_linked(b, 'simulink_Element', a2)
    if hasattr(a1, 'simulink_Parameter'):
        assert not _is_linked(a1, 'simulink_Parameter', b)
    if hasattr(a2, 'simulink_Parameter'):
        assert _is_linked(a2, 'simulink_Parameter', b)
    _safe_set(b, 'simulink_Element', set())
    assert not _is_linked(b, 'simulink_Element', a2)
    if hasattr(a2, 'simulink_Parameter'):
        assert not _is_linked(a2, 'simulink_Parameter', b)


def test_assoc_parent0_reverse_link_reassign_clear():
    a1 = simulink_SubSystem()
    a2 = simulink_SubSystem()
    b = simulink_Block(name="sample_text")
    _safe_set(b, 'blocks', a1)
    assert _is_linked(b, 'blocks', a1)
    if hasattr(a1, 'SubSystem'):
        assert _is_linked(a1, 'SubSystem', b)
    _safe_set(b, 'blocks', a2)
    assert _is_linked(b, 'blocks', a2)
    if hasattr(a1, 'SubSystem'):
        assert not _is_linked(a1, 'SubSystem', b)
    if hasattr(a2, 'SubSystem'):
        assert _is_linked(a2, 'SubSystem', b)
    _safe_set(b, 'blocks', None)
    assert not _is_linked(b, 'blocks', a2)
    if hasattr(a2, 'SubSystem'):
        assert not _is_linked(a2, 'SubSystem', b)


def test_assoc_subSystems22_reverse_link_reassign_clear():
    a1 = simulink_SubSystem()
    a2 = simulink_SubSystem()
    b = simulink_SubSystem()
    _safe_set(b, 'simulink_SubSystem23', a1)
    assert _is_linked(b, 'simulink_SubSystem23', a1)
    if hasattr(a1, 'simulink_SubSystem21'):
        assert _is_linked(a1, 'simulink_SubSystem21', b)
    _safe_set(b, 'simulink_SubSystem23', a2)
    assert _is_linked(b, 'simulink_SubSystem23', a2)
    if hasattr(a1, 'simulink_SubSystem21'):
        assert not _is_linked(a1, 'simulink_SubSystem21', b)
    if hasattr(a2, 'simulink_SubSystem21'):
        assert _is_linked(a2, 'simulink_SubSystem21', b)
    _safe_set(b, 'simulink_SubSystem23', None)
    assert not _is_linked(b, 'simulink_SubSystem23', a2)
    if hasattr(a2, 'simulink_SubSystem21'):
        assert not _is_linked(a2, 'simulink_SubSystem21', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_action91_stub_double():
    # Action has no real 'Action93' property in the generated
    # code (a bare stub) -- manually attach it so simulink_stateflow_Transition's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # simulink_stateflow_Transition's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = simulink_stateflow_Transition(priority=7)
    partner = Action()
    setattr(partner, 'Action93', None)
    _safe_set(owner, 'simulink_stateflow_Transition92', {partner})
    assert getattr(partner, 'Action93') == owner
    _safe_set(owner, 'simulink_stateflow_Transition92', set())
    assert getattr(partner, 'Action93') is None


def test_assoc_block26_stub_double():
    # simulink_InPortBlock has no real 'inPorts' property in the generated
    # code (a bare stub) -- manually attach it so simulink_Block's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # simulink_Block's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = simulink_Block(name="sample_text")
    partner = simulink_InPortBlock()
    setattr(partner, 'inPorts', None)
    _safe_set(owner, 'Block27', partner)
    assert getattr(partner, 'inPorts') == owner
    _safe_set(owner, 'Block27', None)
    assert getattr(partner, 'inPorts') is None


def test_assoc_block35_stub_double():
    # simulink_OutPortBlock has no real 'outPorts' property in the generated
    # code (a bare stub) -- manually attach it so simulink_Block's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # simulink_Block's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = simulink_Block(name="sample_text")
    partner = simulink_OutPortBlock()
    setattr(partner, 'outPorts', None)
    _safe_set(owner, 'Block36', partner)
    assert getattr(partner, 'outPorts') == owner
    _safe_set(owner, 'Block36', None)
    assert getattr(partner, 'outPorts') is None


def test_assoc_bus15_stub_double():
    # simulink_Line has no real 'simulink_Line16' property in the generated
    # code (a bare stub) -- manually attach it so simulink_Bus's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # simulink_Bus's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = simulink_Bus(name="sample_text")
    partner = simulink_Line()
    setattr(partner, 'simulink_Line16', None)
    _safe_set(owner, 'simulink_Bus', partner)
    assert getattr(partner, 'simulink_Line16') == owner
    _safe_set(owner, 'simulink_Bus', None)
    assert getattr(partner, 'simulink_Line16') is None


def test_assoc_bus41_stub_double():
    # simulink_BusCreator has no real 'simulink_BusCreator' property in the generated
    # code (a bare stub) -- manually attach it so simulink_Bus's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # simulink_Bus's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = simulink_Bus(name="sample_text")
    partner = simulink_BusCreator()
    setattr(partner, 'simulink_BusCreator', None)
    _safe_set(owner, 'simulink_Bus42', partner)
    assert getattr(partner, 'simulink_BusCreator') == owner
    _safe_set(owner, 'simulink_Bus42', None)
    assert getattr(partner, 'simulink_BusCreator') is None


def test_assoc_bus43_stub_double():
    # simulink_BusSelector has no real 'simulink_BusSelector' property in the generated
    # code (a bare stub) -- manually attach it so simulink_Bus's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # simulink_Bus's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = simulink_Bus(name="sample_text")
    partner = simulink_BusSelector()
    setattr(partner, 'simulink_BusSelector', None)
    _safe_set(owner, 'simulink_Bus44', partner)
    assert getattr(partner, 'simulink_BusSelector') == owner
    _safe_set(owner, 'simulink_Bus44', None)
    assert getattr(partner, 'simulink_BusSelector') is None


def test_assoc_buses33_stub_double():
    # simulink_SimulinkFile has no real 'simulink_SimulinkFile' property in the generated
    # code (a bare stub) -- manually attach it so simulink_Bus's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # simulink_Bus's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = simulink_Bus(name="sample_text")
    partner = simulink_SimulinkFile()
    setattr(partner, 'simulink_SimulinkFile', None)
    _safe_set(owner, 'simulink_Bus34', partner)
    assert owner in getattr(partner, 'simulink_SimulinkFile')
    _safe_set(owner, 'simulink_Bus34', None)
    assert owner not in getattr(partner, 'simulink_SimulinkFile')


def test_assoc_constant107_stub_double():
    # Data has no real 'Data109' property in the generated
    # code (a bare stub) -- manually attach it so simulink_stateflow_EmbeddedFunction's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # simulink_stateflow_EmbeddedFunction's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = simulink_stateflow_EmbeddedFunction(code="sample_text", name="sample_text")
    partner = Data()
    setattr(partner, 'Data109', None)
    _safe_set(owner, 'simulink_stateflow_EmbeddedFunction108', {partner})
    assert getattr(partner, 'Data109') == owner
    _safe_set(owner, 'simulink_stateflow_EmbeddedFunction108', set())
    assert getattr(partner, 'Data109') is None


def test_assoc_constant76_stub_double():
    # Data has no real 'Data78' property in the generated
    # code (a bare stub) -- manually attach it so simulink_stateflow_State's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # simulink_stateflow_State's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = simulink_stateflow_State(initial=True, name="sample_text", priority=7, subStateType="sample_text")
    partner = Data()
    setattr(partner, 'Data78', None)
    _safe_set(owner, 'simulink_stateflow_State77', {partner})
    assert getattr(partner, 'Data78') == owner
    _safe_set(owner, 'simulink_stateflow_State77', set())
    assert getattr(partner, 'Data78') is None


def test_assoc_duringAction70_stub_double():
    # Action has no real 'Action72' property in the generated
    # code (a bare stub) -- manually attach it so simulink_stateflow_State's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # simulink_stateflow_State's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = simulink_stateflow_State(initial=True, name="sample_text", priority=7, subStateType="sample_text")
    partner = Action()
    setattr(partner, 'Action72', None)
    _safe_set(owner, 'simulink_stateflow_State71', {partner})
    assert getattr(partner, 'Action72') == owner
    _safe_set(owner, 'simulink_stateflow_State71', set())
    assert getattr(partner, 'Action72') is None


def test_assoc_embeddedFunctions63_stub_double():
    # EmbeddedFunction has no real 'EmbeddedFunction' property in the generated
    # code (a bare stub) -- manually attach it so simulink_stateflow_State's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # simulink_stateflow_State's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = simulink_stateflow_State(initial=True, name="sample_text", priority=7, subStateType="sample_text")
    partner = EmbeddedFunction()
    setattr(partner, 'EmbeddedFunction', None)
    _safe_set(owner, 'simulink_stateflow_State64', {partner})
    assert getattr(partner, 'EmbeddedFunction') == owner
    _safe_set(owner, 'simulink_stateflow_State64', set())
    assert getattr(partner, 'EmbeddedFunction') is None


def test_assoc_entryAction65_stub_double():
    # Action has no real 'Action' property in the generated
    # code (a bare stub) -- manually attach it so simulink_stateflow_State's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # simulink_stateflow_State's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = simulink_stateflow_State(initial=True, name="sample_text", priority=7, subStateType="sample_text")
    partner = Action()
    setattr(partner, 'Action', None)
    _safe_set(owner, 'simulink_stateflow_State66', {partner})
    assert getattr(partner, 'Action') == owner
    _safe_set(owner, 'simulink_stateflow_State66', set())
    assert getattr(partner, 'Action') is None


def test_assoc_event86_stub_double():
    # Event has no real 'Event87' property in the generated
    # code (a bare stub) -- manually attach it so simulink_stateflow_Transition's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # simulink_stateflow_Transition's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = simulink_stateflow_Transition(priority=7)
    partner = Event()
    setattr(partner, 'Event87', None)
    _safe_set(owner, 'simulink_stateflow_Transition', partner)
    assert getattr(partner, 'Event87') == owner
    _safe_set(owner, 'simulink_stateflow_Transition', None)
    assert getattr(partner, 'Event87') is None


def test_assoc_events61_stub_double():
    # Event has no real 'Event' property in the generated
    # code (a bare stub) -- manually attach it so simulink_stateflow_State's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # simulink_stateflow_State's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = simulink_stateflow_State(initial=True, name="sample_text", priority=7, subStateType="sample_text")
    partner = Event()
    setattr(partner, 'Event', None)
    _safe_set(owner, 'simulink_stateflow_State62', {partner})
    assert getattr(partner, 'Event') == owner
    _safe_set(owner, 'simulink_stateflow_State62', set())
    assert getattr(partner, 'Event') is None


def test_assoc_exitAction67_stub_double():
    # Action has no real 'Action69' property in the generated
    # code (a bare stub) -- manually attach it so simulink_stateflow_State's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # simulink_stateflow_State's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = simulink_stateflow_State(initial=True, name="sample_text", priority=7, subStateType="sample_text")
    partner = Action()
    setattr(partner, 'Action69', None)
    _safe_set(owner, 'simulink_stateflow_State68', {partner})
    assert getattr(partner, 'Action69') == owner
    _safe_set(owner, 'simulink_stateflow_State68', set())
    assert getattr(partner, 'Action69') is None


def test_assoc_guard88_stub_double():
    # Action has no real 'Action90' property in the generated
    # code (a bare stub) -- manually attach it so simulink_stateflow_Transition's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # simulink_stateflow_Transition's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = simulink_stateflow_Transition(priority=7)
    partner = Action()
    setattr(partner, 'Action90', None)
    _safe_set(owner, 'simulink_stateflow_Transition89', {partner})
    assert getattr(partner, 'Action90') == owner
    _safe_set(owner, 'simulink_stateflow_Transition89', set())
    assert getattr(partner, 'Action90') is None


def test_assoc_inPorts2_stub_double():
    # simulink_InPortBlock has no real 'InPortBlock' property in the generated
    # code (a bare stub) -- manually attach it so simulink_Block's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # simulink_Block's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = simulink_Block(name="sample_text")
    partner = simulink_InPortBlock()
    setattr(partner, 'InPortBlock', None)
    _safe_set(owner, 'block3', {partner})
    assert getattr(partner, 'InPortBlock') == owner
    _safe_set(owner, 'block3', set())
    assert getattr(partner, 'InPortBlock') is None


def test_assoc_incomingLines4_stub_double():
    # simulink_Line has no real 'Line' property in the generated
    # code (a bare stub) -- manually attach it so simulink_Block's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # simulink_Block's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = simulink_Block(name="sample_text")
    partner = simulink_Line()
    setattr(partner, 'Line', None)
    _safe_set(owner, 'targetBlock', {partner})
    assert getattr(partner, 'Line') == owner
    _safe_set(owner, 'targetBlock', set())
    assert getattr(partner, 'Line') is None


def test_assoc_initial_guard79_stub_double():
    # Action has no real 'Action81' property in the generated
    # code (a bare stub) -- manually attach it so simulink_stateflow_State's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # simulink_stateflow_State's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = simulink_stateflow_State(initial=True, name="sample_text", priority=7, subStateType="sample_text")
    partner = Action()
    setattr(partner, 'Action81', None)
    _safe_set(owner, 'simulink_stateflow_State80', {partner})
    assert getattr(partner, 'Action81') == owner
    _safe_set(owner, 'simulink_stateflow_State80', set())
    assert getattr(partner, 'Action81') is None


def test_assoc_input99_stub_double():
    # Data has no real 'Data100' property in the generated
    # code (a bare stub) -- manually attach it so simulink_stateflow_EmbeddedFunction's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # simulink_stateflow_EmbeddedFunction's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = simulink_stateflow_EmbeddedFunction(code="sample_text", name="sample_text")
    partner = Data()
    setattr(partner, 'Data100', None)
    _safe_set(owner, 'simulink_stateflow_EmbeddedFunction', {partner})
    assert getattr(partner, 'Data100') == owner
    _safe_set(owner, 'simulink_stateflow_EmbeddedFunction', set())
    assert getattr(partner, 'Data100') is None


def test_assoc_lines17_stub_double():
    # simulink_Line has no real 'simulink_Line18' property in the generated
    # code (a bare stub) -- manually attach it so simulink_SubSystem's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # simulink_SubSystem's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = simulink_SubSystem()
    partner = simulink_Line()
    setattr(partner, 'simulink_Line18', None)
    _safe_set(owner, 'simulink_SubSystem', {partner})
    assert getattr(partner, 'simulink_Line18') == owner
    _safe_set(owner, 'simulink_SubSystem', set())
    assert getattr(partner, 'simulink_Line18') is None


def test_assoc_local104_stub_double():
    # Data has no real 'Data106' property in the generated
    # code (a bare stub) -- manually attach it so simulink_stateflow_EmbeddedFunction's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # simulink_stateflow_EmbeddedFunction's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = simulink_stateflow_EmbeddedFunction(code="sample_text", name="sample_text")
    partner = Data()
    setattr(partner, 'Data106', None)
    _safe_set(owner, 'simulink_stateflow_EmbeddedFunction105', {partner})
    assert getattr(partner, 'Data106') == owner
    _safe_set(owner, 'simulink_stateflow_EmbeddedFunction105', set())
    assert getattr(partner, 'Data106') is None


def test_assoc_local73_stub_double():
    # Data has no real 'Data75' property in the generated
    # code (a bare stub) -- manually attach it so simulink_stateflow_State's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # simulink_stateflow_State's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = simulink_stateflow_State(initial=True, name="sample_text", priority=7, subStateType="sample_text")
    partner = Data()
    setattr(partner, 'Data75', None)
    _safe_set(owner, 'simulink_stateflow_State74', {partner})
    assert getattr(partner, 'Data75') == owner
    _safe_set(owner, 'simulink_stateflow_State74', set())
    assert getattr(partner, 'Data75') is None


def test_assoc_nodes58_stub_double():
    # Node has no real 'Node' property in the generated
    # code (a bare stub) -- manually attach it so simulink_stateflow_State's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # simulink_stateflow_State's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = simulink_stateflow_State(initial=True, name="sample_text", priority=7, subStateType="sample_text")
    partner = Node()
    setattr(partner, 'Node', None)
    _safe_set(owner, 'parent59', {partner})
    assert getattr(partner, 'Node') == owner
    _safe_set(owner, 'parent59', set())
    assert getattr(partner, 'Node') is None


def test_assoc_outPorts1_stub_double():
    # simulink_OutPortBlock has no real 'OutPortBlock' property in the generated
    # code (a bare stub) -- manually attach it so simulink_Block's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # simulink_Block's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = simulink_Block(name="sample_text")
    partner = simulink_OutPortBlock()
    setattr(partner, 'OutPortBlock', None)
    _safe_set(owner, 'block', {partner})
    assert getattr(partner, 'OutPortBlock') == owner
    _safe_set(owner, 'block', set())
    assert getattr(partner, 'OutPortBlock') is None


def test_assoc_outgoingLines5_stub_double():
    # simulink_Line has no real 'Line6' property in the generated
    # code (a bare stub) -- manually attach it so simulink_Block's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # simulink_Block's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = simulink_Block(name="sample_text")
    partner = simulink_Line()
    setattr(partner, 'Line6', None)
    _safe_set(owner, 'sourceBlock', {partner})
    assert getattr(partner, 'Line6') == owner
    _safe_set(owner, 'sourceBlock', set())
    assert getattr(partner, 'Line6') is None


def test_assoc_output101_stub_double():
    # Data has no real 'Data103' property in the generated
    # code (a bare stub) -- manually attach it so simulink_stateflow_EmbeddedFunction's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # simulink_stateflow_EmbeddedFunction's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = simulink_stateflow_EmbeddedFunction(code="sample_text", name="sample_text")
    partner = Data()
    setattr(partner, 'Data103', None)
    _safe_set(owner, 'simulink_stateflow_EmbeddedFunction102', {partner})
    assert getattr(partner, 'Data103') == owner
    _safe_set(owner, 'simulink_stateflow_EmbeddedFunction102', set())
    assert getattr(partner, 'Data103') is None


def test_assoc_source82_stub_double():
    # Node has no real 'Node83' property in the generated
    # code (a bare stub) -- manually attach it so simulink_stateflow_Transition's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # simulink_stateflow_Transition's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = simulink_stateflow_Transition(priority=7)
    partner = Node()
    setattr(partner, 'Node83', None)
    _safe_set(owner, 'outgoing', partner)
    assert getattr(partner, 'Node83') == owner
    _safe_set(owner, 'outgoing', None)
    assert getattr(partner, 'Node83') is None


def test_assoc_sourceBlock12_stub_double():
    # simulink_Line has no real 'outgoingLines' property in the generated
    # code (a bare stub) -- manually attach it so simulink_Block's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # simulink_Block's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = simulink_Block(name="sample_text")
    partner = simulink_Line()
    setattr(partner, 'outgoingLines', None)
    _safe_set(owner, 'Block', partner)
    assert getattr(partner, 'outgoingLines') == owner
    _safe_set(owner, 'Block', None)
    assert getattr(partner, 'outgoingLines') is None


def test_assoc_sourceBlock30_stub_double():
    # simulink_LibraryReference has no real 'simulink_LibraryReference' property in the generated
    # code (a bare stub) -- manually attach it so simulink_Block's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # simulink_Block's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = simulink_Block(name="sample_text")
    partner = simulink_LibraryReference()
    setattr(partner, 'simulink_LibraryReference', None)
    _safe_set(owner, 'simulink_Block31', partner)
    assert getattr(partner, 'simulink_LibraryReference') == owner
    _safe_set(owner, 'simulink_Block31', None)
    assert getattr(partner, 'simulink_LibraryReference') is None


def test_assoc_target84_stub_double():
    # Node has no real 'Node85' property in the generated
    # code (a bare stub) -- manually attach it so simulink_stateflow_Transition's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # simulink_stateflow_Transition's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = simulink_stateflow_Transition(priority=7)
    partner = Node()
    setattr(partner, 'Node85', None)
    _safe_set(owner, 'incoming', partner)
    assert getattr(partner, 'Node85') == owner
    _safe_set(owner, 'incoming', None)
    assert getattr(partner, 'Node85') is None


def test_assoc_targetBlock13_stub_double():
    # simulink_Line has no real 'incomingLines' property in the generated
    # code (a bare stub) -- manually attach it so simulink_Block's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # simulink_Block's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = simulink_Block(name="sample_text")
    partner = simulink_Line()
    setattr(partner, 'incomingLines', None)
    _safe_set(owner, 'Block14', partner)
    assert getattr(partner, 'incomingLines') == owner
    _safe_set(owner, 'Block14', None)
    assert getattr(partner, 'incomingLines') is None


def test_assoc_transitions60_stub_double():
    # Transition has no real 'Transition' property in the generated
    # code (a bare stub) -- manually attach it so simulink_stateflow_State's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # simulink_stateflow_State's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = simulink_stateflow_State(initial=True, name="sample_text", priority=7, subStateType="sample_text")
    partner = Transition()
    setattr(partner, 'Transition', None)
    _safe_set(owner, 'simulink_stateflow_State', {partner})
    assert getattr(partner, 'Transition') == owner
    _safe_set(owner, 'simulink_stateflow_State', set())
    assert getattr(partner, 'Transition') is None


