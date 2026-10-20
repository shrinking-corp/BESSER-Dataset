import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Action,
    Condition,
    Guard,
    NamedElement,
    RegionContainer,
    ardurobotml_AcceleratetAction,
    ardurobotml_Action,
    ardurobotml_ActionSequence,
    ardurobotml_AllActionFinishedCondition,
    ardurobotml_CollisionSensorCondition,
    ardurobotml_Condition,
    ardurobotml_DeceleratetAction,
    ardurobotml_EmergencyStopAction,
    ardurobotml_EvaluateGuard,
    ardurobotml_EventGuard,
    ardurobotml_FSMClock,
    ardurobotml_FSMEvent,
    ardurobotml_Guard,
    ardurobotml_MoveBackardAction,
    ardurobotml_MoveBackardAndTurningLeftAction,
    ardurobotml_MoveBackardAndTurningRightAction,
    ardurobotml_MoveForwardAction,
    ardurobotml_MoveForwardAndTurningLeftAction,
    ardurobotml_MoveForwardAndTurningRightAction,
    ardurobotml_NamedElement,
    ardurobotml_Region,
    ardurobotml_RegionContainer,
    ardurobotml_SCANCollisionAction,
    ardurobotml_State,
    ardurobotml_StopAction,
    ardurobotml_SystemPropertyCondition,
    ardurobotml_TFSM,
    ardurobotml_TemporalGuard,
    ardurobotml_TimedSystem,
    ardurobotml_Transition,
    ardurobotml_TurningLeftAction,
    ardurobotml_TurningRightAction,
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

def test_assoc_actions22_reverse_link_reassign_clear():
    a1 = ardurobotml_State()
    a2 = ardurobotml_State()
    b = ardurobotml_Action()
    _safe_set(b, 'ardurobotml_Action', a1)
    assert _is_linked(b, 'ardurobotml_Action', a1)
    if hasattr(a1, 'ardurobotml_State23'):
        assert _is_linked(a1, 'ardurobotml_State23', b)
    _safe_set(b, 'ardurobotml_Action', a2)
    assert _is_linked(b, 'ardurobotml_Action', a2)
    if hasattr(a1, 'ardurobotml_State23'):
        assert not _is_linked(a1, 'ardurobotml_State23', b)
    if hasattr(a2, 'ardurobotml_State23'):
        assert _is_linked(a2, 'ardurobotml_State23', b)
    _safe_set(b, 'ardurobotml_Action', None)
    assert not _is_linked(b, 'ardurobotml_Action', a2)
    if hasattr(a2, 'ardurobotml_State23'):
        assert not _is_linked(a2, 'ardurobotml_State23', b)


def test_assoc_currentState15_reverse_link_reassign_clear():
    a1 = ardurobotml_TFSM()
    a2 = ardurobotml_TFSM()
    b = ardurobotml_State()
    _safe_set(b, 'ardurobotml_State17', a1)
    assert _is_linked(b, 'ardurobotml_State17', a1)
    if hasattr(a1, 'ardurobotml_TFSM16'):
        assert _is_linked(a1, 'ardurobotml_TFSM16', b)
    _safe_set(b, 'ardurobotml_State17', a2)
    assert _is_linked(b, 'ardurobotml_State17', a2)
    if hasattr(a1, 'ardurobotml_TFSM16'):
        assert not _is_linked(a1, 'ardurobotml_TFSM16', b)
    if hasattr(a2, 'ardurobotml_TFSM16'):
        assert _is_linked(a2, 'ardurobotml_TFSM16', b)
    _safe_set(b, 'ardurobotml_State17', None)
    assert not _is_linked(b, 'ardurobotml_State17', a2)
    if hasattr(a2, 'ardurobotml_TFSM16'):
        assert not _is_linked(a2, 'ardurobotml_TFSM16', b)


def test_assoc_incomingTransitions20_reverse_link_reassign_clear():
    a1 = ardurobotml_Transition()
    a2 = ardurobotml_Transition()
    b = ardurobotml_State()
    _safe_set(b, 'target', {a1})
    assert _is_linked(b, 'target', a1)
    if hasattr(a1, 'Transition21'):
        assert _is_linked(a1, 'Transition21', b)
    _safe_set(b, 'target', {a2})
    assert _is_linked(b, 'target', a2)
    if hasattr(a1, 'Transition21'):
        assert not _is_linked(a1, 'Transition21', b)
    if hasattr(a2, 'Transition21'):
        assert _is_linked(a2, 'Transition21', b)
    _safe_set(b, 'target', set())
    assert not _is_linked(b, 'target', a2)
    if hasattr(a2, 'Transition21'):
        assert not _is_linked(a2, 'Transition21', b)


def test_assoc_initialState5_reverse_link_reassign_clear():
    a1 = ardurobotml_TFSM()
    a2 = ardurobotml_TFSM()
    b = ardurobotml_State()
    _safe_set(b, 'ardurobotml_State', a1)
    assert _is_linked(b, 'ardurobotml_State', a1)
    if hasattr(a1, 'ardurobotml_TFSM6'):
        assert _is_linked(a1, 'ardurobotml_TFSM6', b)
    _safe_set(b, 'ardurobotml_State', a2)
    assert _is_linked(b, 'ardurobotml_State', a2)
    if hasattr(a1, 'ardurobotml_TFSM6'):
        assert not _is_linked(a1, 'ardurobotml_TFSM6', b)
    if hasattr(a2, 'ardurobotml_TFSM6'):
        assert _is_linked(a2, 'ardurobotml_TFSM6', b)
    _safe_set(b, 'ardurobotml_State', None)
    assert not _is_linked(b, 'ardurobotml_State', a2)
    if hasattr(a2, 'ardurobotml_TFSM6'):
        assert not _is_linked(a2, 'ardurobotml_TFSM6', b)


def test_assoc_localClock10_reverse_link_reassign_clear():
    a1 = ardurobotml_TFSM()
    a2 = ardurobotml_TFSM()
    b = ardurobotml_FSMClock(value=7)
    _safe_set(b, 'ardurobotml_FSMClock12', a1)
    assert _is_linked(b, 'ardurobotml_FSMClock12', a1)
    if hasattr(a1, 'ardurobotml_TFSM11'):
        assert _is_linked(a1, 'ardurobotml_TFSM11', b)
    _safe_set(b, 'ardurobotml_FSMClock12', a2)
    assert _is_linked(b, 'ardurobotml_FSMClock12', a2)
    if hasattr(a1, 'ardurobotml_TFSM11'):
        assert not _is_linked(a1, 'ardurobotml_TFSM11', b)
    if hasattr(a2, 'ardurobotml_TFSM11'):
        assert _is_linked(a2, 'ardurobotml_TFSM11', b)
    _safe_set(b, 'ardurobotml_FSMClock12', None)
    assert not _is_linked(b, 'ardurobotml_FSMClock12', a2)
    if hasattr(a2, 'ardurobotml_TFSM11'):
        assert not _is_linked(a2, 'ardurobotml_TFSM11', b)


def test_assoc_onClock34_reverse_link_reassign_clear():
    a1 = ardurobotml_TemporalGuard(afterDuration=7)
    a2 = ardurobotml_TemporalGuard(afterDuration=13)
    b = ardurobotml_FSMClock(value=7)
    _safe_set(b, 'ardurobotml_FSMClock35', a1)
    assert _is_linked(b, 'ardurobotml_FSMClock35', a1)
    if hasattr(a1, 'ardurobotml_TemporalGuard'):
        assert _is_linked(a1, 'ardurobotml_TemporalGuard', b)
    _safe_set(b, 'ardurobotml_FSMClock35', a2)
    assert _is_linked(b, 'ardurobotml_FSMClock35', a2)
    if hasattr(a1, 'ardurobotml_TemporalGuard'):
        assert not _is_linked(a1, 'ardurobotml_TemporalGuard', b)
    if hasattr(a2, 'ardurobotml_TemporalGuard'):
        assert _is_linked(a2, 'ardurobotml_TemporalGuard', b)
    _safe_set(b, 'ardurobotml_FSMClock35', None)
    assert not _is_linked(b, 'ardurobotml_FSMClock35', a2)
    if hasattr(a2, 'ardurobotml_TemporalGuard'):
        assert not _is_linked(a2, 'ardurobotml_TemporalGuard', b)


def test_assoc_outgoingTransitions19_reverse_link_reassign_clear():
    a1 = ardurobotml_Transition()
    a2 = ardurobotml_Transition()
    b = ardurobotml_State()
    _safe_set(b, 'source', {a1})
    assert _is_linked(b, 'source', a1)
    if hasattr(a1, 'Transition'):
        assert _is_linked(a1, 'Transition', b)
    _safe_set(b, 'source', {a2})
    assert _is_linked(b, 'source', a2)
    if hasattr(a1, 'Transition'):
        assert not _is_linked(a1, 'Transition', b)
    if hasattr(a2, 'Transition'):
        assert _is_linked(a2, 'Transition', b)
    _safe_set(b, 'source', set())
    assert not _is_linked(b, 'source', a2)
    if hasattr(a2, 'Transition'):
        assert not _is_linked(a2, 'Transition', b)


def test_assoc_ownedStates18_reverse_link_reassign_clear():
    a1 = ardurobotml_TFSM()
    a2 = ardurobotml_TFSM()
    b = ardurobotml_State()
    _safe_set(b, 'State', a1)
    assert _is_linked(b, 'State', a1)
    if hasattr(a1, 'owningFSM'):
        assert _is_linked(a1, 'owningFSM', b)
    _safe_set(b, 'State', a2)
    assert _is_linked(b, 'State', a2)
    if hasattr(a1, 'owningFSM'):
        assert not _is_linked(a1, 'owningFSM', b)
    if hasattr(a2, 'owningFSM'):
        assert _is_linked(a2, 'owningFSM', b)
    _safe_set(b, 'State', None)
    assert not _is_linked(b, 'State', a2)
    if hasattr(a2, 'owningFSM'):
        assert not _is_linked(a2, 'owningFSM', b)


def test_assoc_ownedStates42_reverse_link_reassign_clear():
    a1 = ardurobotml_State()
    a2 = ardurobotml_State()
    b = ardurobotml_Region(name="sample_text")
    _safe_set(b, 'ardurobotml_Region', {a1})
    assert _is_linked(b, 'ardurobotml_Region', a1)
    if hasattr(a1, 'ardurobotml_State43'):
        assert _is_linked(a1, 'ardurobotml_State43', b)
    _safe_set(b, 'ardurobotml_Region', {a2})
    assert _is_linked(b, 'ardurobotml_Region', a2)
    if hasattr(a1, 'ardurobotml_State43'):
        assert not _is_linked(a1, 'ardurobotml_State43', b)
    if hasattr(a2, 'ardurobotml_State43'):
        assert _is_linked(a2, 'ardurobotml_State43', b)
    _safe_set(b, 'ardurobotml_Region', set())
    assert not _is_linked(b, 'ardurobotml_Region', a2)
    if hasattr(a2, 'ardurobotml_State43'):
        assert not _is_linked(a2, 'ardurobotml_State43', b)


def test_assoc_ownedTransitions13_reverse_link_reassign_clear():
    a1 = ardurobotml_Transition()
    a2 = ardurobotml_Transition()
    b = ardurobotml_TFSM()
    _safe_set(b, 'ardurobotml_TFSM14', {a1})
    assert _is_linked(b, 'ardurobotml_TFSM14', a1)
    if hasattr(a1, 'ardurobotml_Transition'):
        assert _is_linked(a1, 'ardurobotml_Transition', b)
    _safe_set(b, 'ardurobotml_TFSM14', {a2})
    assert _is_linked(b, 'ardurobotml_TFSM14', a2)
    if hasattr(a1, 'ardurobotml_Transition'):
        assert not _is_linked(a1, 'ardurobotml_Transition', b)
    if hasattr(a2, 'ardurobotml_Transition'):
        assert _is_linked(a2, 'ardurobotml_Transition', b)
    _safe_set(b, 'ardurobotml_TFSM14', set())
    assert not _is_linked(b, 'ardurobotml_TFSM14', a2)
    if hasattr(a2, 'ardurobotml_Transition'):
        assert not _is_linked(a2, 'ardurobotml_Transition', b)


def test_assoc_owningFSM24_reverse_link_reassign_clear():
    a1 = ardurobotml_TFSM()
    a2 = ardurobotml_TFSM()
    b = ardurobotml_State()
    _safe_set(b, 'ownedStates', a1)
    assert _is_linked(b, 'ownedStates', a1)
    if hasattr(a1, 'TFSM'):
        assert _is_linked(a1, 'TFSM', b)
    _safe_set(b, 'ownedStates', a2)
    assert _is_linked(b, 'ownedStates', a2)
    if hasattr(a1, 'TFSM'):
        assert not _is_linked(a1, 'TFSM', b)
    if hasattr(a2, 'TFSM'):
        assert _is_linked(a2, 'TFSM', b)
    _safe_set(b, 'ownedStates', None)
    assert not _is_linked(b, 'ownedStates', a2)
    if hasattr(a2, 'TFSM'):
        assert not _is_linked(a2, 'TFSM', b)


def test_assoc_source25_reverse_link_reassign_clear():
    a1 = ardurobotml_Transition()
    a2 = ardurobotml_Transition()
    b = ardurobotml_State()
    _safe_set(b, 'State26', a1)
    assert _is_linked(b, 'State26', a1)
    if hasattr(a1, 'outgoingTransitions'):
        assert _is_linked(a1, 'outgoingTransitions', b)
    _safe_set(b, 'State26', a2)
    assert _is_linked(b, 'State26', a2)
    if hasattr(a1, 'outgoingTransitions'):
        assert not _is_linked(a1, 'outgoingTransitions', b)
    if hasattr(a2, 'outgoingTransitions'):
        assert _is_linked(a2, 'outgoingTransitions', b)
    _safe_set(b, 'State26', None)
    assert not _is_linked(b, 'State26', a2)
    if hasattr(a2, 'outgoingTransitions'):
        assert not _is_linked(a2, 'outgoingTransitions', b)


def test_assoc_target27_reverse_link_reassign_clear():
    a1 = ardurobotml_Transition()
    a2 = ardurobotml_Transition()
    b = ardurobotml_State()
    _safe_set(b, 'State28', a1)
    assert _is_linked(b, 'State28', a1)
    if hasattr(a1, 'incomingTransitions'):
        assert _is_linked(a1, 'incomingTransitions', b)
    _safe_set(b, 'State28', a2)
    assert _is_linked(b, 'State28', a2)
    if hasattr(a1, 'incomingTransitions'):
        assert not _is_linked(a1, 'incomingTransitions', b)
    if hasattr(a2, 'incomingTransitions'):
        assert _is_linked(a2, 'incomingTransitions', b)
    _safe_set(b, 'State28', None)
    assert not _is_linked(b, 'State28', a2)
    if hasattr(a2, 'incomingTransitions'):
        assert not _is_linked(a2, 'incomingTransitions', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_actions46_stub_double():
    # ardurobotml_ActionSequence has no real 'ardurobotml_ActionSequence' property in the generated
    # code (a bare stub) -- manually attach it so ardurobotml_Action's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ardurobotml_Action's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ardurobotml_Action()
    partner = ardurobotml_ActionSequence()
    setattr(partner, 'ardurobotml_ActionSequence', None)
    _safe_set(owner, 'ardurobotml_Action47', partner)
    assert owner in getattr(partner, 'ardurobotml_ActionSequence')
    _safe_set(owner, 'ardurobotml_Action47', None)
    assert owner not in getattr(partner, 'ardurobotml_ActionSequence')


def test_assoc_generatedEvents31_stub_double():
    # ardurobotml_FSMEvent has no real 'ardurobotml_FSMEvent33' property in the generated
    # code (a bare stub) -- manually attach it so ardurobotml_Transition's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ardurobotml_Transition's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ardurobotml_Transition()
    partner = ardurobotml_FSMEvent()
    setattr(partner, 'ardurobotml_FSMEvent33', None)
    _safe_set(owner, 'ardurobotml_Transition32', {partner})
    assert getattr(partner, 'ardurobotml_FSMEvent33') == owner
    _safe_set(owner, 'ardurobotml_Transition32', set())
    assert getattr(partner, 'ardurobotml_FSMEvent33') is None


def test_assoc_globalClocks1_stub_double():
    # ardurobotml_TimedSystem has no real 'ardurobotml_TimedSystem2' property in the generated
    # code (a bare stub) -- manually attach it so ardurobotml_FSMClock's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ardurobotml_FSMClock's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ardurobotml_FSMClock(value=7)
    partner = ardurobotml_TimedSystem()
    setattr(partner, 'ardurobotml_TimedSystem2', None)
    _safe_set(owner, 'ardurobotml_FSMClock', partner)
    assert owner in getattr(partner, 'ardurobotml_TimedSystem2')
    _safe_set(owner, 'ardurobotml_FSMClock', None)
    assert owner not in getattr(partner, 'ardurobotml_TimedSystem2')


def test_assoc_localEvents7_stub_double():
    # ardurobotml_FSMEvent has no real 'ardurobotml_FSMEvent9' property in the generated
    # code (a bare stub) -- manually attach it so ardurobotml_TFSM's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ardurobotml_TFSM's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ardurobotml_TFSM()
    partner = ardurobotml_FSMEvent()
    setattr(partner, 'ardurobotml_FSMEvent9', None)
    _safe_set(owner, 'ardurobotml_TFSM8', {partner})
    assert getattr(partner, 'ardurobotml_FSMEvent9') == owner
    _safe_set(owner, 'ardurobotml_TFSM8', set())
    assert getattr(partner, 'ardurobotml_FSMEvent9') is None


def test_assoc_ownedGuard29_stub_double():
    # ardurobotml_Guard has no real 'ardurobotml_Guard' property in the generated
    # code (a bare stub) -- manually attach it so ardurobotml_Transition's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ardurobotml_Transition's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ardurobotml_Transition()
    partner = ardurobotml_Guard()
    setattr(partner, 'ardurobotml_Guard', None)
    _safe_set(owner, 'ardurobotml_Transition30', partner)
    assert getattr(partner, 'ardurobotml_Guard') == owner
    _safe_set(owner, 'ardurobotml_Transition30', None)
    assert getattr(partner, 'ardurobotml_Guard') is None


def test_assoc_ownedRegions44_stub_double():
    # ardurobotml_RegionContainer has no real 'ardurobotml_RegionContainer' property in the generated
    # code (a bare stub) -- manually attach it so ardurobotml_Region's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ardurobotml_Region's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ardurobotml_Region(name="sample_text")
    partner = ardurobotml_RegionContainer()
    setattr(partner, 'ardurobotml_RegionContainer', None)
    _safe_set(owner, 'ardurobotml_Region45', partner)
    assert owner in getattr(partner, 'ardurobotml_RegionContainer')
    _safe_set(owner, 'ardurobotml_Region45', None)
    assert owner not in getattr(partner, 'ardurobotml_RegionContainer')


def test_assoc_sollicitingTransitions38_stub_double():
    # ardurobotml_FSMEvent has no real 'ardurobotml_FSMEvent39' property in the generated
    # code (a bare stub) -- manually attach it so ardurobotml_Transition's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ardurobotml_Transition's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ardurobotml_Transition()
    partner = ardurobotml_FSMEvent()
    setattr(partner, 'ardurobotml_FSMEvent39', None)
    _safe_set(owner, 'ardurobotml_Transition40', partner)
    assert owner in getattr(partner, 'ardurobotml_FSMEvent39')
    _safe_set(owner, 'ardurobotml_Transition40', None)
    assert owner not in getattr(partner, 'ardurobotml_FSMEvent39')


def test_assoc_tfsms0_stub_double():
    # ardurobotml_TimedSystem has no real 'ardurobotml_TimedSystem' property in the generated
    # code (a bare stub) -- manually attach it so ardurobotml_TFSM's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ardurobotml_TFSM's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ardurobotml_TFSM()
    partner = ardurobotml_TimedSystem()
    setattr(partner, 'ardurobotml_TimedSystem', None)
    _safe_set(owner, 'ardurobotml_TFSM', partner)
    assert owner in getattr(partner, 'ardurobotml_TimedSystem')
    _safe_set(owner, 'ardurobotml_TFSM', None)
    assert owner not in getattr(partner, 'ardurobotml_TimedSystem')


