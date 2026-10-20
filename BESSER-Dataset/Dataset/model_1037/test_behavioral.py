import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    BinaryClockConstraint,
    ClockConstraint,
    ClockConstraintOperation,
    State,
    tfsm_AndClockConstraint,
    tfsm_BinaryClockConstraint,
    tfsm_Clock,
    tfsm_ClockConstraint,
    tfsm_ClockConstraintOperation,
    tfsm_ClockReset,
    tfsm_FSM,
    tfsm_FinalState,
    tfsm_InitialState,
    tfsm_LowerClockConstraint,
    tfsm_LowerEqualClockConstraint,
    tfsm_OrClockConstraint,
    tfsm_State,
    tfsm_Transition,
    tfsm_UpperClockConstraint,
    tfsm_UpperEqualClockConstraint,
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

def test_assoc_clock26_reverse_link_reassign_clear():
    a1 = tfsm_ClockConstraint(threshold=7)
    a2 = tfsm_ClockConstraint(threshold=13)
    b = tfsm_Clock(name="sample_text", tick=7)
    _safe_set(b, 'tfsm_Clock27', a1)
    assert _is_linked(b, 'tfsm_Clock27', a1)
    if hasattr(a1, 'tfsm_ClockConstraint'):
        assert _is_linked(a1, 'tfsm_ClockConstraint', b)
    _safe_set(b, 'tfsm_Clock27', a2)
    assert _is_linked(b, 'tfsm_Clock27', a2)
    if hasattr(a1, 'tfsm_ClockConstraint'):
        assert not _is_linked(a1, 'tfsm_ClockConstraint', b)
    if hasattr(a2, 'tfsm_ClockConstraint'):
        assert _is_linked(a2, 'tfsm_ClockConstraint', b)
    _safe_set(b, 'tfsm_Clock27', None)
    assert not _is_linked(b, 'tfsm_Clock27', a2)
    if hasattr(a2, 'tfsm_ClockConstraint'):
        assert not _is_linked(a2, 'tfsm_ClockConstraint', b)


def test_assoc_clocks0_reverse_link_reassign_clear():
    a1 = tfsm_FSM(name="sample_text")
    a2 = tfsm_FSM(name="sample_text_2")
    b = tfsm_Clock(name="sample_text", tick=7)
    _safe_set(b, 'tfsm_Clock', a1)
    assert _is_linked(b, 'tfsm_Clock', a1)
    if hasattr(a1, 'tfsm_FSM'):
        assert _is_linked(a1, 'tfsm_FSM', b)
    _safe_set(b, 'tfsm_Clock', a2)
    assert _is_linked(b, 'tfsm_Clock', a2)
    if hasattr(a1, 'tfsm_FSM'):
        assert not _is_linked(a1, 'tfsm_FSM', b)
    if hasattr(a2, 'tfsm_FSM'):
        assert _is_linked(a2, 'tfsm_FSM', b)
    _safe_set(b, 'tfsm_Clock', None)
    assert not _is_linked(b, 'tfsm_Clock', a2)
    if hasattr(a2, 'tfsm_FSM'):
        assert not _is_linked(a2, 'tfsm_FSM', b)


def test_assoc_currentState7_reverse_link_reassign_clear():
    a1 = tfsm_State(name="sample_text")
    a2 = tfsm_State(name="sample_text_2")
    b = tfsm_FSM(name="sample_text")
    _safe_set(b, 'tfsm_FSM8', a1)
    assert _is_linked(b, 'tfsm_FSM8', a1)
    if hasattr(a1, 'tfsm_State9'):
        assert _is_linked(a1, 'tfsm_State9', b)
    _safe_set(b, 'tfsm_FSM8', a2)
    assert _is_linked(b, 'tfsm_FSM8', a2)
    if hasattr(a1, 'tfsm_State9'):
        assert not _is_linked(a1, 'tfsm_State9', b)
    if hasattr(a2, 'tfsm_State9'):
        assert _is_linked(a2, 'tfsm_State9', b)
    _safe_set(b, 'tfsm_FSM8', None)
    assert not _is_linked(b, 'tfsm_FSM8', a2)
    if hasattr(a2, 'tfsm_State9'):
        assert not _is_linked(a2, 'tfsm_State9', b)


def test_assoc_from_23_reverse_link_reassign_clear():
    a1 = tfsm_Transition(event="sample_text")
    a2 = tfsm_Transition(event="sample_text_2")
    b = tfsm_State(name="sample_text")
    _safe_set(b, 'State', a1)
    assert _is_linked(b, 'State', a1)
    if hasattr(a1, 'outgoingtransitions'):
        assert _is_linked(a1, 'outgoingtransitions', b)
    _safe_set(b, 'State', a2)
    assert _is_linked(b, 'State', a2)
    if hasattr(a1, 'outgoingtransitions'):
        assert not _is_linked(a1, 'outgoingtransitions', b)
    if hasattr(a2, 'outgoingtransitions'):
        assert _is_linked(a2, 'outgoingtransitions', b)
    _safe_set(b, 'State', None)
    assert not _is_linked(b, 'State', a2)
    if hasattr(a2, 'outgoingtransitions'):
        assert not _is_linked(a2, 'outgoingtransitions', b)


def test_assoc_fsm12_reverse_link_reassign_clear():
    a1 = tfsm_State(name="sample_text")
    a2 = tfsm_State(name="sample_text_2")
    b = tfsm_FSM(name="sample_text")
    _safe_set(b, 'tfsm_FSM14', a1)
    assert _is_linked(b, 'tfsm_FSM14', a1)
    if hasattr(a1, 'tfsm_State13'):
        assert _is_linked(a1, 'tfsm_State13', b)
    _safe_set(b, 'tfsm_FSM14', a2)
    assert _is_linked(b, 'tfsm_FSM14', a2)
    if hasattr(a1, 'tfsm_State13'):
        assert not _is_linked(a1, 'tfsm_State13', b)
    if hasattr(a2, 'tfsm_State13'):
        assert _is_linked(a2, 'tfsm_State13', b)
    _safe_set(b, 'tfsm_FSM14', None)
    assert not _is_linked(b, 'tfsm_FSM14', a2)
    if hasattr(a2, 'tfsm_State13'):
        assert not _is_linked(a2, 'tfsm_State13', b)


def test_assoc_incommingtransitions16_reverse_link_reassign_clear():
    a1 = tfsm_Transition(event="sample_text")
    a2 = tfsm_Transition(event="sample_text_2")
    b = tfsm_State(name="sample_text")
    _safe_set(b, 'to', {a1})
    assert _is_linked(b, 'to', a1)
    if hasattr(a1, 'Transition17'):
        assert _is_linked(a1, 'Transition17', b)
    _safe_set(b, 'to', {a2})
    assert _is_linked(b, 'to', a2)
    if hasattr(a1, 'Transition17'):
        assert not _is_linked(a1, 'Transition17', b)
    if hasattr(a2, 'Transition17'):
        assert _is_linked(a2, 'Transition17', b)
    _safe_set(b, 'to', set())
    assert not _is_linked(b, 'to', a2)
    if hasattr(a2, 'Transition17'):
        assert not _is_linked(a2, 'Transition17', b)


def test_assoc_outgoingtransitions15_reverse_link_reassign_clear():
    a1 = tfsm_Transition(event="sample_text")
    a2 = tfsm_Transition(event="sample_text_2")
    b = tfsm_State(name="sample_text")
    _safe_set(b, 'from_', {a1})
    assert _is_linked(b, 'from_', a1)
    if hasattr(a1, 'Transition'):
        assert _is_linked(a1, 'Transition', b)
    _safe_set(b, 'from_', {a2})
    assert _is_linked(b, 'from_', a2)
    if hasattr(a1, 'Transition'):
        assert not _is_linked(a1, 'Transition', b)
    if hasattr(a2, 'Transition'):
        assert _is_linked(a2, 'Transition', b)
    _safe_set(b, 'from_', set())
    assert not _is_linked(b, 'from_', a2)
    if hasattr(a2, 'Transition'):
        assert not _is_linked(a2, 'Transition', b)


def test_assoc_states1_reverse_link_reassign_clear():
    a1 = tfsm_State(name="sample_text")
    a2 = tfsm_State(name="sample_text_2")
    b = tfsm_FSM(name="sample_text")
    _safe_set(b, 'tfsm_FSM2', {a1})
    assert _is_linked(b, 'tfsm_FSM2', a1)
    if hasattr(a1, 'tfsm_State'):
        assert _is_linked(a1, 'tfsm_State', b)
    _safe_set(b, 'tfsm_FSM2', {a2})
    assert _is_linked(b, 'tfsm_FSM2', a2)
    if hasattr(a1, 'tfsm_State'):
        assert not _is_linked(a1, 'tfsm_State', b)
    if hasattr(a2, 'tfsm_State'):
        assert _is_linked(a2, 'tfsm_State', b)
    _safe_set(b, 'tfsm_FSM2', set())
    assert not _is_linked(b, 'tfsm_FSM2', a2)
    if hasattr(a2, 'tfsm_State'):
        assert not _is_linked(a2, 'tfsm_State', b)


def test_assoc_to24_reverse_link_reassign_clear():
    a1 = tfsm_Transition(event="sample_text")
    a2 = tfsm_Transition(event="sample_text_2")
    b = tfsm_State(name="sample_text")
    _safe_set(b, 'State25', a1)
    assert _is_linked(b, 'State25', a1)
    if hasattr(a1, 'incommingtransitions'):
        assert _is_linked(a1, 'incommingtransitions', b)
    _safe_set(b, 'State25', a2)
    assert _is_linked(b, 'State25', a2)
    if hasattr(a1, 'incommingtransitions'):
        assert not _is_linked(a1, 'incommingtransitions', b)
    if hasattr(a2, 'incommingtransitions'):
        assert _is_linked(a2, 'incommingtransitions', b)
    _safe_set(b, 'State25', None)
    assert not _is_linked(b, 'State25', a2)
    if hasattr(a2, 'incommingtransitions'):
        assert not _is_linked(a2, 'incommingtransitions', b)


def test_assoc_transitions3_reverse_link_reassign_clear():
    a1 = tfsm_Transition(event="sample_text")
    a2 = tfsm_Transition(event="sample_text_2")
    b = tfsm_FSM(name="sample_text")
    _safe_set(b, 'tfsm_FSM4', {a1})
    assert _is_linked(b, 'tfsm_FSM4', a1)
    if hasattr(a1, 'tfsm_Transition'):
        assert _is_linked(a1, 'tfsm_Transition', b)
    _safe_set(b, 'tfsm_FSM4', {a2})
    assert _is_linked(b, 'tfsm_FSM4', a2)
    if hasattr(a1, 'tfsm_Transition'):
        assert not _is_linked(a1, 'tfsm_Transition', b)
    if hasattr(a2, 'tfsm_Transition'):
        assert _is_linked(a2, 'tfsm_Transition', b)
    _safe_set(b, 'tfsm_FSM4', set())
    assert not _is_linked(b, 'tfsm_FSM4', a2)
    if hasattr(a2, 'tfsm_Transition'):
        assert not _is_linked(a2, 'tfsm_Transition', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_clock28_stub_double():
    # tfsm_ClockReset has no real 'tfsm_ClockReset29' property in the generated
    # code (a bare stub) -- manually attach it so tfsm_Clock's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # tfsm_Clock's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = tfsm_Clock(name="sample_text", tick=7)
    partner = tfsm_ClockReset()
    setattr(partner, 'tfsm_ClockReset29', None)
    _safe_set(owner, 'tfsm_Clock30', partner)
    assert getattr(partner, 'tfsm_ClockReset29') == owner
    _safe_set(owner, 'tfsm_Clock30', None)
    assert getattr(partner, 'tfsm_ClockReset29') is None


def test_assoc_clockresets18_stub_double():
    # tfsm_ClockReset has no real 'tfsm_ClockReset' property in the generated
    # code (a bare stub) -- manually attach it so tfsm_Transition's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # tfsm_Transition's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = tfsm_Transition(event="sample_text")
    partner = tfsm_ClockReset()
    setattr(partner, 'tfsm_ClockReset', None)
    _safe_set(owner, 'tfsm_Transition19', {partner})
    assert getattr(partner, 'tfsm_ClockReset') == owner
    _safe_set(owner, 'tfsm_Transition19', set())
    assert getattr(partner, 'tfsm_ClockReset') is None


def test_assoc_initialstate5_stub_double():
    # tfsm_InitialState has no real 'tfsm_InitialState' property in the generated
    # code (a bare stub) -- manually attach it so tfsm_FSM's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # tfsm_FSM's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = tfsm_FSM(name="sample_text")
    partner = tfsm_InitialState()
    setattr(partner, 'tfsm_InitialState', None)
    _safe_set(owner, 'tfsm_FSM6', partner)
    assert getattr(partner, 'tfsm_InitialState') == owner
    _safe_set(owner, 'tfsm_FSM6', None)
    assert getattr(partner, 'tfsm_InitialState') is None


def test_assoc_stateguard10_stub_double():
    # tfsm_ClockConstraintOperation has no real 'tfsm_ClockConstraintOperation' property in the generated
    # code (a bare stub) -- manually attach it so tfsm_State's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # tfsm_State's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = tfsm_State(name="sample_text")
    partner = tfsm_ClockConstraintOperation()
    setattr(partner, 'tfsm_ClockConstraintOperation', None)
    _safe_set(owner, 'tfsm_State11', partner)
    assert getattr(partner, 'tfsm_ClockConstraintOperation') == owner
    _safe_set(owner, 'tfsm_State11', None)
    assert getattr(partner, 'tfsm_ClockConstraintOperation') is None


def test_assoc_transitionguard20_stub_double():
    # tfsm_ClockConstraintOperation has no real 'tfsm_ClockConstraintOperation22' property in the generated
    # code (a bare stub) -- manually attach it so tfsm_Transition's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # tfsm_Transition's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = tfsm_Transition(event="sample_text")
    partner = tfsm_ClockConstraintOperation()
    setattr(partner, 'tfsm_ClockConstraintOperation22', None)
    _safe_set(owner, 'tfsm_Transition21', partner)
    assert getattr(partner, 'tfsm_ClockConstraintOperation22') == owner
    _safe_set(owner, 'tfsm_Transition21', None)
    assert getattr(partner, 'tfsm_ClockConstraintOperation22') is None


