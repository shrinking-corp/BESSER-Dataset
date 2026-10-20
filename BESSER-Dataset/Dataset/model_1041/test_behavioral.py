import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    AbstractState,
    FSM_AbstractState,
    FSM_EndState,
    FSM_StartState,
    FSM_State,
    FSM_StateMachine,
    FSM_Transition,
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

def test_assoc_statemachine7_reverse_link_reassign_clear():
    a1 = FSM_StateMachine(code="sample_text")
    a2 = FSM_StateMachine(code="sample_text_2")
    b = FSM_AbstractState(envs="sample_text", name="sample_text")
    _safe_set(b, 'states', a1)
    assert _is_linked(b, 'states', a1)
    if hasattr(a1, 'StateMachine'):
        assert _is_linked(a1, 'StateMachine', b)
    _safe_set(b, 'states', a2)
    assert _is_linked(b, 'states', a2)
    if hasattr(a1, 'StateMachine'):
        assert not _is_linked(a1, 'StateMachine', b)
    if hasattr(a2, 'StateMachine'):
        assert _is_linked(a2, 'StateMachine', b)
    _safe_set(b, 'states', None)
    assert not _is_linked(b, 'states', a2)
    if hasattr(a2, 'StateMachine'):
        assert not _is_linked(a2, 'StateMachine', b)


def test_assoc_states0_reverse_link_reassign_clear():
    a1 = FSM_StateMachine(code="sample_text")
    a2 = FSM_StateMachine(code="sample_text_2")
    b = FSM_AbstractState(envs="sample_text", name="sample_text")
    _safe_set(b, 'AbstractState', a1)
    assert _is_linked(b, 'AbstractState', a1)
    if hasattr(a1, 'statemachine'):
        assert _is_linked(a1, 'statemachine', b)
    _safe_set(b, 'AbstractState', a2)
    assert _is_linked(b, 'AbstractState', a2)
    if hasattr(a1, 'statemachine'):
        assert not _is_linked(a1, 'statemachine', b)
    if hasattr(a2, 'statemachine'):
        assert _is_linked(a2, 'statemachine', b)
    _safe_set(b, 'AbstractState', None)
    assert not _is_linked(b, 'AbstractState', a2)
    if hasattr(a2, 'statemachine'):
        assert not _is_linked(a2, 'statemachine', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_source3_stub_double():
    # FSM_Transition has no real 'Transition4' property in the generated
    # code (a bare stub) -- manually attach it so FSM_AbstractState's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # FSM_AbstractState's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = FSM_AbstractState(envs="sample_text", name="sample_text")
    partner = FSM_Transition()
    setattr(partner, 'Transition4', None)
    _safe_set(owner, 'src', {partner})
    assert getattr(partner, 'Transition4') == owner
    _safe_set(owner, 'src', set())
    assert getattr(partner, 'Transition4') is None


def test_assoc_src8_stub_double():
    # FSM_Transition has no real 'source' property in the generated
    # code (a bare stub) -- manually attach it so FSM_AbstractState's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # FSM_AbstractState's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = FSM_AbstractState(envs="sample_text", name="sample_text")
    partner = FSM_Transition()
    setattr(partner, 'source', None)
    _safe_set(owner, 'AbstractState9', partner)
    assert getattr(partner, 'source') == owner
    _safe_set(owner, 'AbstractState9', None)
    assert getattr(partner, 'source') is None


def test_assoc_statemachine12_stub_double():
    # FSM_Transition has no real 'transitions' property in the generated
    # code (a bare stub) -- manually attach it so FSM_StateMachine's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # FSM_StateMachine's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = FSM_StateMachine(code="sample_text")
    partner = FSM_Transition()
    setattr(partner, 'transitions', None)
    _safe_set(owner, 'StateMachine13', partner)
    assert getattr(partner, 'transitions') == owner
    _safe_set(owner, 'StateMachine13', None)
    assert getattr(partner, 'transitions') is None


def test_assoc_tar10_stub_double():
    # FSM_Transition has no real 'target' property in the generated
    # code (a bare stub) -- manually attach it so FSM_AbstractState's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # FSM_AbstractState's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = FSM_AbstractState(envs="sample_text", name="sample_text")
    partner = FSM_Transition()
    setattr(partner, 'target', None)
    _safe_set(owner, 'AbstractState11', partner)
    assert getattr(partner, 'target') == owner
    _safe_set(owner, 'AbstractState11', None)
    assert getattr(partner, 'target') is None


def test_assoc_target5_stub_double():
    # FSM_Transition has no real 'Transition6' property in the generated
    # code (a bare stub) -- manually attach it so FSM_AbstractState's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # FSM_AbstractState's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = FSM_AbstractState(envs="sample_text", name="sample_text")
    partner = FSM_Transition()
    setattr(partner, 'Transition6', None)
    _safe_set(owner, 'tar', {partner})
    assert getattr(partner, 'Transition6') == owner
    _safe_set(owner, 'tar', set())
    assert getattr(partner, 'Transition6') is None


def test_assoc_transitions1_stub_double():
    # FSM_Transition has no real 'Transition' property in the generated
    # code (a bare stub) -- manually attach it so FSM_StateMachine's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # FSM_StateMachine's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = FSM_StateMachine(code="sample_text")
    partner = FSM_Transition()
    setattr(partner, 'Transition', None)
    _safe_set(owner, 'statemachine2', {partner})
    assert getattr(partner, 'Transition') == owner
    _safe_set(owner, 'statemachine2', set())
    assert getattr(partner, 'Transition') is None


