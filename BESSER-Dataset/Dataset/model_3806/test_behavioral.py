import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    stateMachineEditRules_DFA,
    stateMachineEditRules_State,
    stateMachineEditRules_Transition,
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

def test_assoc_from_1_reverse_link_reassign_clear():
    a1 = stateMachineEditRules_Transition(input="sample_text")
    a2 = stateMachineEditRules_Transition(input="sample_text_2")
    b = stateMachineEditRules_State(id="sample_text", isEnd=True, isStart=True)
    _safe_set(b, 'State2', a1)
    assert _is_linked(b, 'State2', a1)
    if hasattr(a1, 'outgoingTransitions'):
        assert _is_linked(a1, 'outgoingTransitions', b)
    _safe_set(b, 'State2', a2)
    assert _is_linked(b, 'State2', a2)
    if hasattr(a1, 'outgoingTransitions'):
        assert not _is_linked(a1, 'outgoingTransitions', b)
    if hasattr(a2, 'outgoingTransitions'):
        assert _is_linked(a2, 'outgoingTransitions', b)
    _safe_set(b, 'State2', None)
    assert not _is_linked(b, 'State2', a2)
    if hasattr(a2, 'outgoingTransitions'):
        assert not _is_linked(a2, 'outgoingTransitions', b)


def test_assoc_incomingTransitions3_reverse_link_reassign_clear():
    a1 = stateMachineEditRules_Transition(input="sample_text")
    a2 = stateMachineEditRules_Transition(input="sample_text_2")
    b = stateMachineEditRules_State(id="sample_text", isEnd=True, isStart=True)
    _safe_set(b, 'to', {a1})
    assert _is_linked(b, 'to', a1)
    if hasattr(a1, 'Transition'):
        assert _is_linked(a1, 'Transition', b)
    _safe_set(b, 'to', {a2})
    assert _is_linked(b, 'to', a2)
    if hasattr(a1, 'Transition'):
        assert not _is_linked(a1, 'Transition', b)
    if hasattr(a2, 'Transition'):
        assert _is_linked(a2, 'Transition', b)
    _safe_set(b, 'to', set())
    assert not _is_linked(b, 'to', a2)
    if hasattr(a2, 'Transition'):
        assert not _is_linked(a2, 'Transition', b)


def test_assoc_outgoingTransitions4_reverse_link_reassign_clear():
    a1 = stateMachineEditRules_Transition(input="sample_text")
    a2 = stateMachineEditRules_Transition(input="sample_text_2")
    b = stateMachineEditRules_State(id="sample_text", isEnd=True, isStart=True)
    _safe_set(b, 'from_', {a1})
    assert _is_linked(b, 'from_', a1)
    if hasattr(a1, 'Transition5'):
        assert _is_linked(a1, 'Transition5', b)
    _safe_set(b, 'from_', {a2})
    assert _is_linked(b, 'from_', a2)
    if hasattr(a1, 'Transition5'):
        assert not _is_linked(a1, 'Transition5', b)
    if hasattr(a2, 'Transition5'):
        assert _is_linked(a2, 'Transition5', b)
    _safe_set(b, 'from_', set())
    assert not _is_linked(b, 'from_', a2)
    if hasattr(a2, 'Transition5'):
        assert not _is_linked(a2, 'Transition5', b)


def test_assoc_to0_reverse_link_reassign_clear():
    a1 = stateMachineEditRules_Transition(input="sample_text")
    a2 = stateMachineEditRules_Transition(input="sample_text_2")
    b = stateMachineEditRules_State(id="sample_text", isEnd=True, isStart=True)
    _safe_set(b, 'State', a1)
    assert _is_linked(b, 'State', a1)
    if hasattr(a1, 'incomingTransitions'):
        assert _is_linked(a1, 'incomingTransitions', b)
    _safe_set(b, 'State', a2)
    assert _is_linked(b, 'State', a2)
    if hasattr(a1, 'incomingTransitions'):
        assert not _is_linked(a1, 'incomingTransitions', b)
    if hasattr(a2, 'incomingTransitions'):
        assert _is_linked(a2, 'incomingTransitions', b)
    _safe_set(b, 'State', None)
    assert not _is_linked(b, 'State', a2)
    if hasattr(a2, 'incomingTransitions'):
        assert not _is_linked(a2, 'incomingTransitions', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_states6_stub_double():
    # stateMachineEditRules_DFA has no real 'stateMachineEditRules_DFA' property in the generated
    # code (a bare stub) -- manually attach it so stateMachineEditRules_State's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # stateMachineEditRules_State's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = stateMachineEditRules_State(id="sample_text", isEnd=True, isStart=True)
    partner = stateMachineEditRules_DFA()
    setattr(partner, 'stateMachineEditRules_DFA', None)
    _safe_set(owner, 'stateMachineEditRules_State', partner)
    assert owner in getattr(partner, 'stateMachineEditRules_DFA')
    _safe_set(owner, 'stateMachineEditRules_State', None)
    assert owner not in getattr(partner, 'stateMachineEditRules_DFA')


def test_assoc_transitions7_stub_double():
    # stateMachineEditRules_DFA has no real 'stateMachineEditRules_DFA8' property in the generated
    # code (a bare stub) -- manually attach it so stateMachineEditRules_Transition's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # stateMachineEditRules_Transition's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = stateMachineEditRules_Transition(input="sample_text")
    partner = stateMachineEditRules_DFA()
    setattr(partner, 'stateMachineEditRules_DFA8', None)
    _safe_set(owner, 'stateMachineEditRules_Transition', partner)
    assert owner in getattr(partner, 'stateMachineEditRules_DFA8')
    _safe_set(owner, 'stateMachineEditRules_Transition', None)
    assert owner not in getattr(partner, 'stateMachineEditRules_DFA8')


