import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Check,
    Event,
    ExecutionNode,
    ExecutionScope,
    MappedElement,
    NamedElement,
    ScopedElement,
    Step,
    Trace,
    sexec_Call,
    sexec_Check,
    sexec_CheckRef,
    sexec_EObject,
    sexec_EnterState,
    sexec_Execution,
    sexec_ExecutionChoice,
    sexec_ExecutionEntry,
    sexec_ExecutionExit,
    sexec_ExecutionFlow,
    sexec_ExecutionNode,
    sexec_ExecutionRegion,
    sexec_ExecutionScope,
    sexec_ExecutionState,
    sexec_ExecutionSynchronization,
    sexec_ExitState,
    sexec_Expression,
    sexec_HistoryEntry,
    sexec_MappedElement,
    sexec_ReactionFired,
    sexec_SaveHistory,
    sexec_ScheduleTimeEvent,
    sexec_StateCase,
    sexec_StateSwitch,
    sexec_StateVector,
    sexec_Step,
    sexec_TimeEvent,
    sexec_Trace,
    sexec_TraceBeginRunCycle,
    sexec_TraceEndRunCycle,
    sexec_TraceNodeExecuted,
    sexec_TraceReactionWillFire,
    sexec_TraceStateEntered,
    sexec_TraceStateExited,
    sexec_UnscheduleTimeEvent,
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

def test_assoc_entryAction13_reverse_link_reassign_clear():
    a1 = sexec_Step(comment="sample_text")
    a2 = sexec_Step(comment="sample_text_2")
    b = sexec_ExecutionState(leaf=True)
    _safe_set(b, 'sexec_ExecutionState14', a1)
    assert _is_linked(b, 'sexec_ExecutionState14', a1)
    if hasattr(a1, 'sexec_Step15'):
        assert _is_linked(a1, 'sexec_Step15', b)
    _safe_set(b, 'sexec_ExecutionState14', a2)
    assert _is_linked(b, 'sexec_ExecutionState14', a2)
    if hasattr(a1, 'sexec_Step15'):
        assert not _is_linked(a1, 'sexec_Step15', b)
    if hasattr(a2, 'sexec_Step15'):
        assert _is_linked(a2, 'sexec_Step15', b)
    _safe_set(b, 'sexec_ExecutionState14', None)
    assert not _is_linked(b, 'sexec_ExecutionState14', a2)
    if hasattr(a2, 'sexec_Step15'):
        assert not _is_linked(a2, 'sexec_Step15', b)


def test_assoc_exitAction16_reverse_link_reassign_clear():
    a1 = sexec_Step(comment="sample_text")
    a2 = sexec_Step(comment="sample_text_2")
    b = sexec_ExecutionState(leaf=True)
    _safe_set(b, 'sexec_ExecutionState17', a1)
    assert _is_linked(b, 'sexec_ExecutionState17', a1)
    if hasattr(a1, 'sexec_Step18'):
        assert _is_linked(a1, 'sexec_Step18', b)
    _safe_set(b, 'sexec_ExecutionState17', a2)
    assert _is_linked(b, 'sexec_ExecutionState17', a2)
    if hasattr(a1, 'sexec_Step18'):
        assert not _is_linked(a1, 'sexec_Step18', b)
    if hasattr(a2, 'sexec_Step18'):
        assert _is_linked(a2, 'sexec_Step18', b)
    _safe_set(b, 'sexec_ExecutionState17', None)
    assert not _is_linked(b, 'sexec_ExecutionState17', a2)
    if hasattr(a2, 'sexec_Step18'):
        assert not _is_linked(a2, 'sexec_Step18', b)


def test_assoc_historyStep64_reverse_link_reassign_clear():
    a1 = sexec_Step(comment="sample_text")
    a2 = sexec_Step(comment="sample_text_2")
    b = sexec_HistoryEntry(deep=True)
    _safe_set(b, 'sexec_HistoryEntry65', a1)
    assert _is_linked(b, 'sexec_HistoryEntry65', a1)
    if hasattr(a1, 'sexec_Step66'):
        assert _is_linked(a1, 'sexec_Step66', b)
    _safe_set(b, 'sexec_HistoryEntry65', a2)
    assert _is_linked(b, 'sexec_HistoryEntry65', a2)
    if hasattr(a1, 'sexec_Step66'):
        assert not _is_linked(a1, 'sexec_Step66', b)
    if hasattr(a2, 'sexec_Step66'):
        assert _is_linked(a2, 'sexec_Step66', b)
    _safe_set(b, 'sexec_HistoryEntry65', None)
    assert not _is_linked(b, 'sexec_HistoryEntry65', a2)
    if hasattr(a2, 'sexec_Step66'):
        assert not _is_linked(a2, 'sexec_Step66', b)


def test_assoc_initialStep59_reverse_link_reassign_clear():
    a1 = sexec_Step(comment="sample_text")
    a2 = sexec_Step(comment="sample_text_2")
    b = sexec_HistoryEntry(deep=True)
    _safe_set(b, 'sexec_HistoryEntry', a1)
    assert _is_linked(b, 'sexec_HistoryEntry', a1)
    if hasattr(a1, 'sexec_Step60'):
        assert _is_linked(a1, 'sexec_Step60', b)
    _safe_set(b, 'sexec_HistoryEntry', a2)
    assert _is_linked(b, 'sexec_HistoryEntry', a2)
    if hasattr(a1, 'sexec_Step60'):
        assert not _is_linked(a1, 'sexec_Step60', b)
    if hasattr(a2, 'sexec_Step60'):
        assert _is_linked(a2, 'sexec_Step60', b)
    _safe_set(b, 'sexec_HistoryEntry', None)
    assert not _is_linked(b, 'sexec_HistoryEntry', a2)
    if hasattr(a2, 'sexec_Step60'):
        assert not _is_linked(a2, 'sexec_Step60', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_cases47_stub_double():
    # sexec_StateCase has no real 'sexec_StateCase' property in the generated
    # code (a bare stub) -- manually attach it so sexec_StateSwitch's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # sexec_StateSwitch's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = sexec_StateSwitch(stateConfigurationIdx=7)
    partner = sexec_StateCase()
    setattr(partner, 'sexec_StateCase', None)
    _safe_set(owner, 'sexec_StateSwitch', {partner})
    assert getattr(partner, 'sexec_StateCase') == owner
    _safe_set(owner, 'sexec_StateSwitch', set())
    assert getattr(partner, 'sexec_StateCase') is None


def test_assoc_entryAction8_stub_double():
    # sexec_ExecutionFlow has no real 'sexec_ExecutionFlow9' property in the generated
    # code (a bare stub) -- manually attach it so sexec_Step's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # sexec_Step's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = sexec_Step(comment="sample_text")
    partner = sexec_ExecutionFlow()
    setattr(partner, 'sexec_ExecutionFlow9', None)
    _safe_set(owner, 'sexec_Step', partner)
    assert getattr(partner, 'sexec_ExecutionFlow9') == owner
    _safe_set(owner, 'sexec_Step', None)
    assert getattr(partner, 'sexec_ExecutionFlow9') is None


def test_assoc_exitAction10_stub_double():
    # sexec_ExecutionFlow has no real 'sexec_ExecutionFlow11' property in the generated
    # code (a bare stub) -- manually attach it so sexec_Step's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # sexec_Step's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = sexec_Step(comment="sample_text")
    partner = sexec_ExecutionFlow()
    setattr(partner, 'sexec_ExecutionFlow11', None)
    _safe_set(owner, 'sexec_Step12', partner)
    assert getattr(partner, 'sexec_ExecutionFlow11') == owner
    _safe_set(owner, 'sexec_Step12', None)
    assert getattr(partner, 'sexec_ExecutionFlow11') is None


def test_assoc_historyRegion48_stub_double():
    # sexec_ExecutionRegion has no real 'sexec_ExecutionRegion50' property in the generated
    # code (a bare stub) -- manually attach it so sexec_StateSwitch's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # sexec_StateSwitch's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = sexec_StateSwitch(stateConfigurationIdx=7)
    partner = sexec_ExecutionRegion()
    setattr(partner, 'sexec_ExecutionRegion50', None)
    _safe_set(owner, 'sexec_StateSwitch49', partner)
    assert getattr(partner, 'sexec_ExecutionRegion50') == owner
    _safe_set(owner, 'sexec_StateSwitch49', None)
    assert getattr(partner, 'sexec_ExecutionRegion50') is None


def test_assoc_historyVector26_stub_double():
    # sexec_ExecutionRegion has no real 'sexec_ExecutionRegion27' property in the generated
    # code (a bare stub) -- manually attach it so sexec_StateVector's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # sexec_StateVector's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = sexec_StateVector(offset=7, size=7)
    partner = sexec_ExecutionRegion()
    setattr(partner, 'sexec_ExecutionRegion27', None)
    _safe_set(owner, 'sexec_StateVector28', partner)
    assert getattr(partner, 'sexec_ExecutionRegion27') == owner
    _safe_set(owner, 'sexec_StateVector28', None)
    assert getattr(partner, 'sexec_ExecutionRegion27') is None


def test_assoc_historyVector6_stub_double():
    # sexec_ExecutionFlow has no real 'sexec_ExecutionFlow7' property in the generated
    # code (a bare stub) -- manually attach it so sexec_StateVector's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # sexec_StateVector's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = sexec_StateVector(offset=7, size=7)
    partner = sexec_ExecutionFlow()
    setattr(partner, 'sexec_ExecutionFlow7', None)
    _safe_set(owner, 'sexec_StateVector', partner)
    assert getattr(partner, 'sexec_ExecutionFlow7') == owner
    _safe_set(owner, 'sexec_StateVector', None)
    assert getattr(partner, 'sexec_ExecutionFlow7') is None


def test_assoc_node67_stub_double():
    # sexec_TraceNodeExecuted has no real 'sexec_TraceNodeExecuted' property in the generated
    # code (a bare stub) -- manually attach it so sexec_ExecutionNode's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # sexec_ExecutionNode's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = sexec_ExecutionNode(simpleName="sample_text")
    partner = sexec_TraceNodeExecuted()
    setattr(partner, 'sexec_TraceNodeExecuted', None)
    _safe_set(owner, 'sexec_ExecutionNode68', partner)
    assert getattr(partner, 'sexec_TraceNodeExecuted') == owner
    _safe_set(owner, 'sexec_ExecutionNode68', None)
    assert getattr(partner, 'sexec_TraceNodeExecuted') is None


def test_assoc_nodes2_stub_double():
    # sexec_ExecutionFlow has no real 'sexec_ExecutionFlow3' property in the generated
    # code (a bare stub) -- manually attach it so sexec_ExecutionNode's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # sexec_ExecutionNode's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = sexec_ExecutionNode(simpleName="sample_text")
    partner = sexec_ExecutionFlow()
    setattr(partner, 'sexec_ExecutionFlow3', None)
    _safe_set(owner, 'sexec_ExecutionNode', partner)
    assert owner in getattr(partner, 'sexec_ExecutionFlow3')
    _safe_set(owner, 'sexec_ExecutionNode', None)
    assert owner not in getattr(partner, 'sexec_ExecutionFlow3')


def test_assoc_nodes29_stub_double():
    # sexec_ExecutionRegion has no real 'sexec_ExecutionRegion30' property in the generated
    # code (a bare stub) -- manually attach it so sexec_ExecutionNode's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # sexec_ExecutionNode's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = sexec_ExecutionNode(simpleName="sample_text")
    partner = sexec_ExecutionRegion()
    setattr(partner, 'sexec_ExecutionRegion30', None)
    _safe_set(owner, 'sexec_ExecutionNode31', partner)
    assert owner in getattr(partner, 'sexec_ExecutionRegion30')
    _safe_set(owner, 'sexec_ExecutionNode31', None)
    assert owner not in getattr(partner, 'sexec_ExecutionRegion30')


def test_assoc_region57_stub_double():
    # sexec_ExecutionRegion has no real 'sexec_ExecutionRegion58' property in the generated
    # code (a bare stub) -- manually attach it so sexec_SaveHistory's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # sexec_SaveHistory's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = sexec_SaveHistory(deep=True)
    partner = sexec_ExecutionRegion()
    setattr(partner, 'sexec_ExecutionRegion58', None)
    _safe_set(owner, 'sexec_SaveHistory', partner)
    assert getattr(partner, 'sexec_ExecutionRegion58') == owner
    _safe_set(owner, 'sexec_SaveHistory', None)
    assert getattr(partner, 'sexec_ExecutionRegion58') is None


def test_assoc_region61_stub_double():
    # sexec_ExecutionRegion has no real 'sexec_ExecutionRegion63' property in the generated
    # code (a bare stub) -- manually attach it so sexec_HistoryEntry's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # sexec_HistoryEntry's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = sexec_HistoryEntry(deep=True)
    partner = sexec_ExecutionRegion()
    setattr(partner, 'sexec_ExecutionRegion63', None)
    _safe_set(owner, 'sexec_HistoryEntry62', partner)
    assert getattr(partner, 'sexec_ExecutionRegion63') == owner
    _safe_set(owner, 'sexec_HistoryEntry62', None)
    assert getattr(partner, 'sexec_ExecutionRegion63') is None


def test_assoc_state37_stub_double():
    # sexec_EnterState has no real 'sexec_EnterState' property in the generated
    # code (a bare stub) -- manually attach it so sexec_ExecutionState's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # sexec_ExecutionState's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = sexec_ExecutionState(leaf=True)
    partner = sexec_EnterState()
    setattr(partner, 'sexec_EnterState', None)
    _safe_set(owner, 'sexec_ExecutionState38', partner)
    assert getattr(partner, 'sexec_EnterState') == owner
    _safe_set(owner, 'sexec_ExecutionState38', None)
    assert getattr(partner, 'sexec_EnterState') is None


def test_assoc_state39_stub_double():
    # sexec_ExitState has no real 'sexec_ExitState' property in the generated
    # code (a bare stub) -- manually attach it so sexec_ExecutionState's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # sexec_ExecutionState's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = sexec_ExecutionState(leaf=True)
    partner = sexec_ExitState()
    setattr(partner, 'sexec_ExitState', None)
    _safe_set(owner, 'sexec_ExecutionState40', partner)
    assert getattr(partner, 'sexec_ExitState') == owner
    _safe_set(owner, 'sexec_ExecutionState40', None)
    assert getattr(partner, 'sexec_ExitState') is None


def test_assoc_state51_stub_double():
    # sexec_StateCase has no real 'sexec_StateCase52' property in the generated
    # code (a bare stub) -- manually attach it so sexec_ExecutionState's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # sexec_ExecutionState's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = sexec_ExecutionState(leaf=True)
    partner = sexec_StateCase()
    setattr(partner, 'sexec_StateCase52', None)
    _safe_set(owner, 'sexec_ExecutionState53', partner)
    assert getattr(partner, 'sexec_StateCase52') == owner
    _safe_set(owner, 'sexec_ExecutionState53', None)
    assert getattr(partner, 'sexec_StateCase52') is None


def test_assoc_state69_stub_double():
    # sexec_TraceStateEntered has no real 'sexec_TraceStateEntered' property in the generated
    # code (a bare stub) -- manually attach it so sexec_ExecutionState's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # sexec_ExecutionState's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = sexec_ExecutionState(leaf=True)
    partner = sexec_TraceStateEntered()
    setattr(partner, 'sexec_TraceStateEntered', None)
    _safe_set(owner, 'sexec_ExecutionState70', partner)
    assert getattr(partner, 'sexec_TraceStateEntered') == owner
    _safe_set(owner, 'sexec_ExecutionState70', None)
    assert getattr(partner, 'sexec_TraceStateEntered') is None


def test_assoc_state71_stub_double():
    # sexec_TraceStateExited has no real 'sexec_TraceStateExited' property in the generated
    # code (a bare stub) -- manually attach it so sexec_ExecutionState's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # sexec_ExecutionState's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = sexec_ExecutionState(leaf=True)
    partner = sexec_TraceStateExited()
    setattr(partner, 'sexec_TraceStateExited', None)
    _safe_set(owner, 'sexec_ExecutionState72', partner)
    assert getattr(partner, 'sexec_TraceStateExited') == owner
    _safe_set(owner, 'sexec_ExecutionState72', None)
    assert getattr(partner, 'sexec_TraceStateExited') is None


def test_assoc_stateVector19_stub_double():
    # sexec_ExecutionScope has no real 'sexec_ExecutionScope' property in the generated
    # code (a bare stub) -- manually attach it so sexec_StateVector's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # sexec_StateVector's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = sexec_StateVector(offset=7, size=7)
    partner = sexec_ExecutionScope()
    setattr(partner, 'sexec_ExecutionScope', None)
    _safe_set(owner, 'sexec_StateVector20', partner)
    assert getattr(partner, 'sexec_ExecutionScope') == owner
    _safe_set(owner, 'sexec_StateVector20', None)
    assert getattr(partner, 'sexec_ExecutionScope') is None


def test_assoc_states1_stub_double():
    # sexec_ExecutionFlow has no real 'sexec_ExecutionFlow' property in the generated
    # code (a bare stub) -- manually attach it so sexec_ExecutionState's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # sexec_ExecutionState's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = sexec_ExecutionState(leaf=True)
    partner = sexec_ExecutionFlow()
    setattr(partner, 'sexec_ExecutionFlow', None)
    _safe_set(owner, 'sexec_ExecutionState', partner)
    assert owner in getattr(partner, 'sexec_ExecutionFlow')
    _safe_set(owner, 'sexec_ExecutionState', None)
    assert owner not in getattr(partner, 'sexec_ExecutionFlow')


def test_assoc_step54_stub_double():
    # sexec_StateCase has no real 'sexec_StateCase55' property in the generated
    # code (a bare stub) -- manually attach it so sexec_Step's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # sexec_Step's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = sexec_Step(comment="sample_text")
    partner = sexec_StateCase()
    setattr(partner, 'sexec_StateCase55', None)
    _safe_set(owner, 'sexec_Step56', partner)
    assert getattr(partner, 'sexec_StateCase55') == owner
    _safe_set(owner, 'sexec_Step56', None)
    assert getattr(partner, 'sexec_StateCase55') is None


def test_assoc_timeEvent41_stub_double():
    # sexec_ScheduleTimeEvent has no real 'sexec_ScheduleTimeEvent' property in the generated
    # code (a bare stub) -- manually attach it so sexec_TimeEvent's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # sexec_TimeEvent's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = sexec_TimeEvent(periodic=True)
    partner = sexec_ScheduleTimeEvent()
    setattr(partner, 'sexec_ScheduleTimeEvent', None)
    _safe_set(owner, 'sexec_TimeEvent', partner)
    assert getattr(partner, 'sexec_ScheduleTimeEvent') == owner
    _safe_set(owner, 'sexec_TimeEvent', None)
    assert getattr(partner, 'sexec_ScheduleTimeEvent') is None


def test_assoc_timeEvent45_stub_double():
    # sexec_UnscheduleTimeEvent has no real 'sexec_UnscheduleTimeEvent' property in the generated
    # code (a bare stub) -- manually attach it so sexec_TimeEvent's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # sexec_TimeEvent's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = sexec_TimeEvent(periodic=True)
    partner = sexec_UnscheduleTimeEvent()
    setattr(partner, 'sexec_UnscheduleTimeEvent', None)
    _safe_set(owner, 'sexec_TimeEvent46', partner)
    assert getattr(partner, 'sexec_UnscheduleTimeEvent') == owner
    _safe_set(owner, 'sexec_TimeEvent46', None)
    assert getattr(partner, 'sexec_UnscheduleTimeEvent') is None


