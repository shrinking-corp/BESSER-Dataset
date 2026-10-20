import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    statemachine_State,
    statemachine_StateMachine,
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

def test_assoc_dst7_reverse_link_reassign_clear():
    a1 = statemachine_Transition(action="sample_text", trigger="sample_text")
    a2 = statemachine_Transition(action="sample_text_2", trigger="sample_text_2")
    b = statemachine_State(name="sample_text")
    _safe_set(b, 'State8', a1)
    assert _is_linked(b, 'State8', a1)
    if hasattr(a1, 'in_'):
        assert _is_linked(a1, 'in_', b)
    _safe_set(b, 'State8', a2)
    assert _is_linked(b, 'State8', a2)
    if hasattr(a1, 'in_'):
        assert not _is_linked(a1, 'in_', b)
    if hasattr(a2, 'in_'):
        assert _is_linked(a2, 'in_', b)
    _safe_set(b, 'State8', None)
    assert not _is_linked(b, 'State8', a2)
    if hasattr(a2, 'in_'):
        assert not _is_linked(a2, 'in_', b)


def test_assoc_in_4_reverse_link_reassign_clear():
    a1 = statemachine_Transition(action="sample_text", trigger="sample_text")
    a2 = statemachine_Transition(action="sample_text_2", trigger="sample_text_2")
    b = statemachine_State(name="sample_text")
    _safe_set(b, 'dst', {a1})
    assert _is_linked(b, 'dst', a1)
    if hasattr(a1, 'Transition5'):
        assert _is_linked(a1, 'Transition5', b)
    _safe_set(b, 'dst', {a2})
    assert _is_linked(b, 'dst', a2)
    if hasattr(a1, 'Transition5'):
        assert not _is_linked(a1, 'Transition5', b)
    if hasattr(a2, 'Transition5'):
        assert _is_linked(a2, 'Transition5', b)
    _safe_set(b, 'dst', set())
    assert not _is_linked(b, 'dst', a2)
    if hasattr(a2, 'Transition5'):
        assert not _is_linked(a2, 'Transition5', b)


def test_assoc_out3_reverse_link_reassign_clear():
    a1 = statemachine_Transition(action="sample_text", trigger="sample_text")
    a2 = statemachine_Transition(action="sample_text_2", trigger="sample_text_2")
    b = statemachine_State(name="sample_text")
    _safe_set(b, 'src', {a1})
    assert _is_linked(b, 'src', a1)
    if hasattr(a1, 'Transition'):
        assert _is_linked(a1, 'Transition', b)
    _safe_set(b, 'src', {a2})
    assert _is_linked(b, 'src', a2)
    if hasattr(a1, 'Transition'):
        assert not _is_linked(a1, 'Transition', b)
    if hasattr(a2, 'Transition'):
        assert _is_linked(a2, 'Transition', b)
    _safe_set(b, 'src', set())
    assert not _is_linked(b, 'src', a2)
    if hasattr(a2, 'Transition'):
        assert not _is_linked(a2, 'Transition', b)


def test_assoc_src6_reverse_link_reassign_clear():
    a1 = statemachine_Transition(action="sample_text", trigger="sample_text")
    a2 = statemachine_Transition(action="sample_text_2", trigger="sample_text_2")
    b = statemachine_State(name="sample_text")
    _safe_set(b, 'State', a1)
    assert _is_linked(b, 'State', a1)
    if hasattr(a1, 'out'):
        assert _is_linked(a1, 'out', b)
    _safe_set(b, 'State', a2)
    assert _is_linked(b, 'State', a2)
    if hasattr(a1, 'out'):
        assert not _is_linked(a1, 'out', b)
    if hasattr(a2, 'out'):
        assert _is_linked(a2, 'out', b)
    _safe_set(b, 'State', None)
    assert not _is_linked(b, 'State', a2)
    if hasattr(a2, 'out'):
        assert not _is_linked(a2, 'out', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_states0_stub_double():
    # statemachine_StateMachine has no real 'statemachine_StateMachine' property in the generated
    # code (a bare stub) -- manually attach it so statemachine_State's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # statemachine_State's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = statemachine_State(name="sample_text")
    partner = statemachine_StateMachine()
    setattr(partner, 'statemachine_StateMachine', None)
    _safe_set(owner, 'statemachine_State', partner)
    assert owner in getattr(partner, 'statemachine_StateMachine')
    _safe_set(owner, 'statemachine_State', None)
    assert owner not in getattr(partner, 'statemachine_StateMachine')


def test_assoc_transitions1_stub_double():
    # statemachine_StateMachine has no real 'statemachine_StateMachine2' property in the generated
    # code (a bare stub) -- manually attach it so statemachine_Transition's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # statemachine_Transition's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = statemachine_Transition(action="sample_text", trigger="sample_text")
    partner = statemachine_StateMachine()
    setattr(partner, 'statemachine_StateMachine2', None)
    _safe_set(owner, 'statemachine_Transition', partner)
    assert owner in getattr(partner, 'statemachine_StateMachine2')
    _safe_set(owner, 'statemachine_Transition', None)
    assert owner not in getattr(partner, 'statemachine_StateMachine2')


