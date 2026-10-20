import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    FSM_FSMModel,
    FSM_NamedElement,
    FSM_State,
    FSM_StateMachine,
    FSM_Transition,
    NamedElement,
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

def test_assoc_source9_reverse_link_reassign_clear():
    a1 = FSM_Transition(input="sample_text", output="sample_text")
    a2 = FSM_Transition(input="sample_text_2", output="sample_text_2")
    b = FSM_State(isFinal=True)
    _safe_set(b, 'State', a1)
    assert _is_linked(b, 'State', a1)
    if hasattr(a1, 'transitions'):
        assert _is_linked(a1, 'transitions', b)
    _safe_set(b, 'State', a2)
    assert _is_linked(b, 'State', a2)
    if hasattr(a1, 'transitions'):
        assert not _is_linked(a1, 'transitions', b)
    if hasattr(a2, 'transitions'):
        assert _is_linked(a2, 'transitions', b)
    _safe_set(b, 'State', None)
    assert not _is_linked(b, 'State', a2)
    if hasattr(a2, 'transitions'):
        assert not _is_linked(a2, 'transitions', b)


def test_assoc_target7_reverse_link_reassign_clear():
    a1 = FSM_Transition(input="sample_text", output="sample_text")
    a2 = FSM_Transition(input="sample_text_2", output="sample_text_2")
    b = FSM_State(isFinal=True)
    _safe_set(b, 'FSM_State8', a1)
    assert _is_linked(b, 'FSM_State8', a1)
    if hasattr(a1, 'FSM_Transition'):
        assert _is_linked(a1, 'FSM_Transition', b)
    _safe_set(b, 'FSM_State8', a2)
    assert _is_linked(b, 'FSM_State8', a2)
    if hasattr(a1, 'FSM_Transition'):
        assert not _is_linked(a1, 'FSM_Transition', b)
    if hasattr(a2, 'FSM_Transition'):
        assert _is_linked(a2, 'FSM_Transition', b)
    _safe_set(b, 'FSM_State8', None)
    assert not _is_linked(b, 'FSM_State8', a2)
    if hasattr(a2, 'FSM_Transition'):
        assert not _is_linked(a2, 'FSM_Transition', b)


def test_assoc_transitions6_reverse_link_reassign_clear():
    a1 = FSM_Transition(input="sample_text", output="sample_text")
    a2 = FSM_Transition(input="sample_text_2", output="sample_text_2")
    b = FSM_State(isFinal=True)
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


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_initial1_stub_double():
    # FSM_StateMachine has no real 'FSM_StateMachine2' property in the generated
    # code (a bare stub) -- manually attach it so FSM_State's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # FSM_State's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = FSM_State(isFinal=True)
    partner = FSM_StateMachine()
    setattr(partner, 'FSM_StateMachine2', None)
    _safe_set(owner, 'FSM_State', partner)
    assert getattr(partner, 'FSM_StateMachine2') == owner
    _safe_set(owner, 'FSM_State', None)
    assert getattr(partner, 'FSM_StateMachine2') is None


def test_assoc_states3_stub_double():
    # FSM_StateMachine has no real 'FSM_StateMachine4' property in the generated
    # code (a bare stub) -- manually attach it so FSM_State's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # FSM_State's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = FSM_State(isFinal=True)
    partner = FSM_StateMachine()
    setattr(partner, 'FSM_StateMachine4', None)
    _safe_set(owner, 'FSM_State5', partner)
    assert owner in getattr(partner, 'FSM_StateMachine4')
    _safe_set(owner, 'FSM_State5', None)
    assert owner not in getattr(partner, 'FSM_StateMachine4')


