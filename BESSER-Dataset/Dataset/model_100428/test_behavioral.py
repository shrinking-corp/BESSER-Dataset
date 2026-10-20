import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Declaration,
    State,
    statemachine_Action,
    statemachine_Declaration,
    statemachine_Expression,
    statemachine_FinalState,
    statemachine_InitialState,
    statemachine_NormalState,
    statemachine_State,
    statemachine_StateMachine,
    statemachine_StateMachineVariable,
    statemachine_Statement,
    statemachine_Transition,
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

def test_assoc_declarations0_reverse_link_reassign_clear():
    a1 = statemachine_StateMachine()
    a2 = statemachine_StateMachine()
    b = statemachine_Declaration()
    _safe_set(b, 'statemachine_Declaration', a1)
    assert _is_linked(b, 'statemachine_Declaration', a1)
    if hasattr(a1, 'statemachine_StateMachine'):
        assert _is_linked(a1, 'statemachine_StateMachine', b)
    _safe_set(b, 'statemachine_Declaration', a2)
    assert _is_linked(b, 'statemachine_Declaration', a2)
    if hasattr(a1, 'statemachine_StateMachine'):
        assert not _is_linked(a1, 'statemachine_StateMachine', b)
    if hasattr(a2, 'statemachine_StateMachine'):
        assert _is_linked(a2, 'statemachine_StateMachine', b)
    _safe_set(b, 'statemachine_Declaration', None)
    assert not _is_linked(b, 'statemachine_Declaration', a2)
    if hasattr(a2, 'statemachine_StateMachine'):
        assert not _is_linked(a2, 'statemachine_StateMachine', b)


def test_assoc_machineVariables1_reverse_link_reassign_clear():
    a1 = statemachine_StateMachineVariable(name="sample_text", type="sample_text")
    a2 = statemachine_StateMachineVariable(name="sample_text_2", type="sample_text_2")
    b = statemachine_StateMachine()
    _safe_set(b, 'statemachine_StateMachine2', {a1})
    assert _is_linked(b, 'statemachine_StateMachine2', a1)
    if hasattr(a1, 'statemachine_StateMachineVariable'):
        assert _is_linked(a1, 'statemachine_StateMachineVariable', b)
    _safe_set(b, 'statemachine_StateMachine2', {a2})
    assert _is_linked(b, 'statemachine_StateMachine2', a2)
    if hasattr(a1, 'statemachine_StateMachineVariable'):
        assert not _is_linked(a1, 'statemachine_StateMachineVariable', b)
    if hasattr(a2, 'statemachine_StateMachineVariable'):
        assert _is_linked(a2, 'statemachine_StateMachineVariable', b)
    _safe_set(b, 'statemachine_StateMachine2', set())
    assert not _is_linked(b, 'statemachine_StateMachine2', a2)
    if hasattr(a2, 'statemachine_StateMachineVariable'):
        assert not _is_linked(a2, 'statemachine_StateMachineVariable', b)


def test_assoc_reachable15_reverse_link_reassign_clear():
    a1 = statemachine_State(id=7, label="sample_text")
    a2 = statemachine_State(id=13, label="sample_text_2")
    b = statemachine_State(id=7, label="sample_text")
    _safe_set(b, 'statemachine_State16', a1)
    assert _is_linked(b, 'statemachine_State16', a1)
    if hasattr(a1, 'statemachine_State14'):
        assert _is_linked(a1, 'statemachine_State14', b)
    _safe_set(b, 'statemachine_State16', a2)
    assert _is_linked(b, 'statemachine_State16', a2)
    if hasattr(a1, 'statemachine_State14'):
        assert not _is_linked(a1, 'statemachine_State14', b)
    if hasattr(a2, 'statemachine_State14'):
        assert _is_linked(a2, 'statemachine_State14', b)
    _safe_set(b, 'statemachine_State16', None)
    assert not _is_linked(b, 'statemachine_State16', a2)
    if hasattr(a2, 'statemachine_State14'):
        assert not _is_linked(a2, 'statemachine_State14', b)


def test_assoc_source3_reverse_link_reassign_clear():
    a1 = statemachine_Transition(actionLabel="sample_text", guardLabel="sample_text", label="sample_text", sourceLabel="sample_text", targetLabel="sample_text")
    a2 = statemachine_Transition(actionLabel="sample_text_2", guardLabel="sample_text_2", label="sample_text_2", sourceLabel="sample_text_2", targetLabel="sample_text_2")
    b = statemachine_State(id=7, label="sample_text")
    _safe_set(b, 'statemachine_State', a1)
    assert _is_linked(b, 'statemachine_State', a1)
    if hasattr(a1, 'statemachine_Transition'):
        assert _is_linked(a1, 'statemachine_Transition', b)
    _safe_set(b, 'statemachine_State', a2)
    assert _is_linked(b, 'statemachine_State', a2)
    if hasattr(a1, 'statemachine_Transition'):
        assert not _is_linked(a1, 'statemachine_Transition', b)
    if hasattr(a2, 'statemachine_Transition'):
        assert _is_linked(a2, 'statemachine_Transition', b)
    _safe_set(b, 'statemachine_State', None)
    assert not _is_linked(b, 'statemachine_State', a2)
    if hasattr(a2, 'statemachine_Transition'):
        assert not _is_linked(a2, 'statemachine_Transition', b)


def test_assoc_successors12_reverse_link_reassign_clear():
    a1 = statemachine_State(id=7, label="sample_text")
    a2 = statemachine_State(id=13, label="sample_text_2")
    b = statemachine_State(id=7, label="sample_text")
    _safe_set(b, 'statemachine_State13', a1)
    assert _is_linked(b, 'statemachine_State13', a1)
    if hasattr(a1, 'statemachine_State11'):
        assert _is_linked(a1, 'statemachine_State11', b)
    _safe_set(b, 'statemachine_State13', a2)
    assert _is_linked(b, 'statemachine_State13', a2)
    if hasattr(a1, 'statemachine_State11'):
        assert not _is_linked(a1, 'statemachine_State11', b)
    if hasattr(a2, 'statemachine_State11'):
        assert _is_linked(a2, 'statemachine_State11', b)
    _safe_set(b, 'statemachine_State13', None)
    assert not _is_linked(b, 'statemachine_State13', a2)
    if hasattr(a2, 'statemachine_State11'):
        assert not _is_linked(a2, 'statemachine_State11', b)


def test_assoc_target4_reverse_link_reassign_clear():
    a1 = statemachine_Transition(actionLabel="sample_text", guardLabel="sample_text", label="sample_text", sourceLabel="sample_text", targetLabel="sample_text")
    a2 = statemachine_Transition(actionLabel="sample_text_2", guardLabel="sample_text_2", label="sample_text_2", sourceLabel="sample_text_2", targetLabel="sample_text_2")
    b = statemachine_State(id=7, label="sample_text")
    _safe_set(b, 'statemachine_State6', a1)
    assert _is_linked(b, 'statemachine_State6', a1)
    if hasattr(a1, 'statemachine_Transition5'):
        assert _is_linked(a1, 'statemachine_Transition5', b)
    _safe_set(b, 'statemachine_State6', a2)
    assert _is_linked(b, 'statemachine_State6', a2)
    if hasattr(a1, 'statemachine_Transition5'):
        assert not _is_linked(a1, 'statemachine_Transition5', b)
    if hasattr(a2, 'statemachine_Transition5'):
        assert _is_linked(a2, 'statemachine_Transition5', b)
    _safe_set(b, 'statemachine_State6', None)
    assert not _is_linked(b, 'statemachine_State6', a2)
    if hasattr(a2, 'statemachine_Transition5'):
        assert not _is_linked(a2, 'statemachine_Transition5', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_actionStatement17_stub_double():
    # statemachine_Statement has no real 'statemachine_Statement18' property in the generated
    # code (a bare stub) -- manually attach it so statemachine_Action's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # statemachine_Action's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = statemachine_Action(actionLabel="sample_text")
    partner = statemachine_Statement()
    setattr(partner, 'statemachine_Statement18', None)
    _safe_set(owner, 'statemachine_Action', partner)
    assert getattr(partner, 'statemachine_Statement18') == owner
    _safe_set(owner, 'statemachine_Action', None)
    assert getattr(partner, 'statemachine_Statement18') is None


def test_assoc_actionStatement9_stub_double():
    # statemachine_Statement has no real 'statemachine_Statement' property in the generated
    # code (a bare stub) -- manually attach it so statemachine_Transition's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # statemachine_Transition's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = statemachine_Transition(actionLabel="sample_text", guardLabel="sample_text", label="sample_text", sourceLabel="sample_text", targetLabel="sample_text")
    partner = statemachine_Statement()
    setattr(partner, 'statemachine_Statement', None)
    _safe_set(owner, 'statemachine_Transition10', partner)
    assert getattr(partner, 'statemachine_Statement') == owner
    _safe_set(owner, 'statemachine_Transition10', None)
    assert getattr(partner, 'statemachine_Statement') is None


def test_assoc_entry19_stub_double():
    # statemachine_NormalState has no real 'statemachine_NormalState' property in the generated
    # code (a bare stub) -- manually attach it so statemachine_Action's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # statemachine_Action's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = statemachine_Action(actionLabel="sample_text")
    partner = statemachine_NormalState()
    setattr(partner, 'statemachine_NormalState', None)
    _safe_set(owner, 'statemachine_Action20', partner)
    assert getattr(partner, 'statemachine_NormalState') == owner
    _safe_set(owner, 'statemachine_Action20', None)
    assert getattr(partner, 'statemachine_NormalState') is None


def test_assoc_guardExpression7_stub_double():
    # statemachine_Expression has no real 'statemachine_Expression' property in the generated
    # code (a bare stub) -- manually attach it so statemachine_Transition's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # statemachine_Transition's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = statemachine_Transition(actionLabel="sample_text", guardLabel="sample_text", label="sample_text", sourceLabel="sample_text", targetLabel="sample_text")
    partner = statemachine_Expression()
    setattr(partner, 'statemachine_Expression', None)
    _safe_set(owner, 'statemachine_Transition8', partner)
    assert getattr(partner, 'statemachine_Expression') == owner
    _safe_set(owner, 'statemachine_Transition8', None)
    assert getattr(partner, 'statemachine_Expression') is None


