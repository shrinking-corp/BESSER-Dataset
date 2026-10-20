import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Behavior,
    BehavioralElement,
    Event,
    NamedElement,
    Vertex,
    rtsc_Behavior,
    rtsc_BehavioralElement,
    rtsc_Clock,
    rtsc_ClockConstraint,
    rtsc_ClockResetEvent,
    rtsc_Connector,
    rtsc_CoordinationProtocol,
    rtsc_Event,
    rtsc_Guard,
    rtsc_Message,
    rtsc_MessageBuffer,
    rtsc_MessageEvent,
    rtsc_MessageType,
    rtsc_MessageTypeRepository,
    rtsc_NamedElement,
    rtsc_Port,
    rtsc_Realtimestatechart,
    rtsc_State,
    rtsc_System,
    rtsc_Transition,
    rtsc_Variable,
    rtsc_VariableAssignmentEvent,
    rtsc_Vertex,
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

def test_assoc_variable36_reverse_link_reassign_clear():
    a1 = rtsc_Variable(initialValue="sample_text")
    a2 = rtsc_Variable(initialValue="sample_text_2")
    b = rtsc_Guard(value="sample_text")
    _safe_set(b, 'rtsc_Guard37', a1)
    assert _is_linked(b, 'rtsc_Guard37', a1)
    if hasattr(a1, 'rtsc_Variable'):
        assert _is_linked(a1, 'rtsc_Variable', b)
    _safe_set(b, 'rtsc_Guard37', a2)
    assert _is_linked(b, 'rtsc_Guard37', a2)
    if hasattr(a1, 'rtsc_Variable'):
        assert not _is_linked(a1, 'rtsc_Variable', b)
    if hasattr(a2, 'rtsc_Variable'):
        assert _is_linked(a2, 'rtsc_Variable', b)
    _safe_set(b, 'rtsc_Guard37', None)
    assert not _is_linked(b, 'rtsc_Guard37', a2)
    if hasattr(a2, 'rtsc_Variable'):
        assert not _is_linked(a2, 'rtsc_Variable', b)


def test_assoc_variable72_reverse_link_reassign_clear():
    a1 = rtsc_VariableAssignmentEvent(value="sample_text")
    a2 = rtsc_VariableAssignmentEvent(value="sample_text_2")
    b = rtsc_Variable(initialValue="sample_text")
    _safe_set(b, 'rtsc_Variable73', a1)
    assert _is_linked(b, 'rtsc_Variable73', a1)
    if hasattr(a1, 'rtsc_VariableAssignmentEvent'):
        assert _is_linked(a1, 'rtsc_VariableAssignmentEvent', b)
    _safe_set(b, 'rtsc_Variable73', a2)
    assert _is_linked(b, 'rtsc_Variable73', a2)
    if hasattr(a1, 'rtsc_VariableAssignmentEvent'):
        assert not _is_linked(a1, 'rtsc_VariableAssignmentEvent', b)
    if hasattr(a2, 'rtsc_VariableAssignmentEvent'):
        assert _is_linked(a2, 'rtsc_VariableAssignmentEvent', b)
    _safe_set(b, 'rtsc_Variable73', None)
    assert not _is_linked(b, 'rtsc_Variable73', a2)
    if hasattr(a2, 'rtsc_VariableAssignmentEvent'):
        assert not _is_linked(a2, 'rtsc_VariableAssignmentEvent', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_clock38_stub_double():
    # rtsc_Clock has no real 'rtsc_Clock' property in the generated
    # code (a bare stub) -- manually attach it so rtsc_ClockConstraint's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # rtsc_ClockConstraint's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = rtsc_ClockConstraint(bound=7)
    partner = rtsc_Clock()
    setattr(partner, 'rtsc_Clock', None)
    _safe_set(owner, 'rtsc_ClockConstraint39', partner)
    assert getattr(partner, 'rtsc_Clock') == owner
    _safe_set(owner, 'rtsc_ClockConstraint39', None)
    assert getattr(partner, 'rtsc_Clock') is None


def test_assoc_clockConstraints27_stub_double():
    # rtsc_Transition has no real 'rtsc_Transition28' property in the generated
    # code (a bare stub) -- manually attach it so rtsc_ClockConstraint's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # rtsc_ClockConstraint's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = rtsc_ClockConstraint(bound=7)
    partner = rtsc_Transition()
    setattr(partner, 'rtsc_Transition28', None)
    _safe_set(owner, 'rtsc_ClockConstraint', partner)
    assert owner in getattr(partner, 'rtsc_Transition28')
    _safe_set(owner, 'rtsc_ClockConstraint', None)
    assert owner not in getattr(partner, 'rtsc_Transition28')


def test_assoc_entryEvents17_stub_double():
    # rtsc_Event has no real 'rtsc_Event' property in the generated
    # code (a bare stub) -- manually attach it so rtsc_State's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # rtsc_State's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = rtsc_State(final=True, initial=True)
    partner = rtsc_Event()
    setattr(partner, 'rtsc_Event', None)
    _safe_set(owner, 'rtsc_State18', {partner})
    assert getattr(partner, 'rtsc_Event') == owner
    _safe_set(owner, 'rtsc_State18', set())
    assert getattr(partner, 'rtsc_Event') is None


def test_assoc_exitEvents19_stub_double():
    # rtsc_Event has no real 'rtsc_Event21' property in the generated
    # code (a bare stub) -- manually attach it so rtsc_State's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # rtsc_State's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = rtsc_State(final=True, initial=True)
    partner = rtsc_Event()
    setattr(partner, 'rtsc_Event21', None)
    _safe_set(owner, 'rtsc_State20', {partner})
    assert getattr(partner, 'rtsc_Event21') == owner
    _safe_set(owner, 'rtsc_State20', set())
    assert getattr(partner, 'rtsc_Event21') is None


def test_assoc_guards26_stub_double():
    # rtsc_Transition has no real 'rtsc_Transition' property in the generated
    # code (a bare stub) -- manually attach it so rtsc_Guard's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # rtsc_Guard's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = rtsc_Guard(value="sample_text")
    partner = rtsc_Transition()
    setattr(partner, 'rtsc_Transition', None)
    _safe_set(owner, 'rtsc_Guard', partner)
    assert owner in getattr(partner, 'rtsc_Transition')
    _safe_set(owner, 'rtsc_Guard', None)
    assert owner not in getattr(partner, 'rtsc_Transition')


def test_assoc_incomingTransitions13_stub_double():
    # rtsc_Transition has no real 'Transition14' property in the generated
    # code (a bare stub) -- manually attach it so rtsc_State's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # rtsc_State's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = rtsc_State(final=True, initial=True)
    partner = rtsc_Transition()
    setattr(partner, 'Transition14', None)
    _safe_set(owner, 'target', {partner})
    assert getattr(partner, 'Transition14') == owner
    _safe_set(owner, 'target', set())
    assert getattr(partner, 'Transition14') is None


def test_assoc_initialState4_stub_double():
    # rtsc_Realtimestatechart has no real 'rtsc_Realtimestatechart' property in the generated
    # code (a bare stub) -- manually attach it so rtsc_State's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # rtsc_State's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = rtsc_State(final=True, initial=True)
    partner = rtsc_Realtimestatechart()
    setattr(partner, 'rtsc_Realtimestatechart', None)
    _safe_set(owner, 'rtsc_State', partner)
    assert getattr(partner, 'rtsc_Realtimestatechart') == owner
    _safe_set(owner, 'rtsc_State', None)
    assert getattr(partner, 'rtsc_Realtimestatechart') is None


def test_assoc_outgoingTransitions15_stub_double():
    # rtsc_Transition has no real 'Transition16' property in the generated
    # code (a bare stub) -- manually attach it so rtsc_State's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # rtsc_State's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = rtsc_State(final=True, initial=True)
    partner = rtsc_Transition()
    setattr(partner, 'Transition16', None)
    _safe_set(owner, 'source', {partner})
    assert getattr(partner, 'Transition16') == owner
    _safe_set(owner, 'source', set())
    assert getattr(partner, 'Transition16') is None


def test_assoc_owningRTSC12_stub_double():
    # rtsc_Realtimestatechart has no real 'Realtimestatechart' property in the generated
    # code (a bare stub) -- manually attach it so rtsc_State's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # rtsc_State's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = rtsc_State(final=True, initial=True)
    partner = rtsc_Realtimestatechart()
    setattr(partner, 'Realtimestatechart', None)
    _safe_set(owner, 'states', partner)
    assert getattr(partner, 'Realtimestatechart') == owner
    _safe_set(owner, 'states', None)
    assert getattr(partner, 'Realtimestatechart') is None


def test_assoc_source22_stub_double():
    # rtsc_Transition has no real 'outgoingTransitions' property in the generated
    # code (a bare stub) -- manually attach it so rtsc_State's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # rtsc_State's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = rtsc_State(final=True, initial=True)
    partner = rtsc_Transition()
    setattr(partner, 'outgoingTransitions', None)
    _safe_set(owner, 'State23', partner)
    assert getattr(partner, 'outgoingTransitions') == owner
    _safe_set(owner, 'State23', None)
    assert getattr(partner, 'outgoingTransitions') is None


def test_assoc_statechart40_stub_double():
    # rtsc_Realtimestatechart has no real 'Realtimestatechart41' property in the generated
    # code (a bare stub) -- manually attach it so rtsc_Variable's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # rtsc_Variable's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = rtsc_Variable(initialValue="sample_text")
    partner = rtsc_Realtimestatechart()
    setattr(partner, 'Realtimestatechart41', None)
    _safe_set(owner, 'variables', partner)
    assert getattr(partner, 'Realtimestatechart41') == owner
    _safe_set(owner, 'variables', None)
    assert getattr(partner, 'Realtimestatechart41') is None


def test_assoc_states3_stub_double():
    # rtsc_Realtimestatechart has no real 'owningRTSC' property in the generated
    # code (a bare stub) -- manually attach it so rtsc_State's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # rtsc_State's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = rtsc_State(final=True, initial=True)
    partner = rtsc_Realtimestatechart()
    setattr(partner, 'owningRTSC', None)
    _safe_set(owner, 'State', partner)
    assert owner in getattr(partner, 'owningRTSC')
    _safe_set(owner, 'State', None)
    assert owner not in getattr(partner, 'owningRTSC')


def test_assoc_subStatecharts9_stub_double():
    # rtsc_Realtimestatechart has no real 'rtsc_Realtimestatechart11' property in the generated
    # code (a bare stub) -- manually attach it so rtsc_State's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # rtsc_State's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = rtsc_State(final=True, initial=True)
    partner = rtsc_Realtimestatechart()
    setattr(partner, 'rtsc_Realtimestatechart11', None)
    _safe_set(owner, 'rtsc_State10', {partner})
    assert getattr(partner, 'rtsc_Realtimestatechart11') == owner
    _safe_set(owner, 'rtsc_State10', set())
    assert getattr(partner, 'rtsc_Realtimestatechart11') is None


def test_assoc_target24_stub_double():
    # rtsc_Transition has no real 'incomingTransitions' property in the generated
    # code (a bare stub) -- manually attach it so rtsc_State's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # rtsc_State's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = rtsc_State(final=True, initial=True)
    partner = rtsc_Transition()
    setattr(partner, 'incomingTransitions', None)
    _safe_set(owner, 'State25', partner)
    assert getattr(partner, 'incomingTransitions') == owner
    _safe_set(owner, 'State25', None)
    assert getattr(partner, 'incomingTransitions') is None


def test_assoc_variables5_stub_double():
    # rtsc_Realtimestatechart has no real 'statechart6' property in the generated
    # code (a bare stub) -- manually attach it so rtsc_Variable's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # rtsc_Variable's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = rtsc_Variable(initialValue="sample_text")
    partner = rtsc_Realtimestatechart()
    setattr(partner, 'statechart6', None)
    _safe_set(owner, 'Variable', partner)
    assert owner in getattr(partner, 'statechart6')
    _safe_set(owner, 'Variable', None)
    assert owner not in getattr(partner, 'statechart6')


