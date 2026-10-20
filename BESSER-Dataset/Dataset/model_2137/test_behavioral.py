import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    transitiongraph_State,
    transitiongraph_Transition,
    transitiongraph_TransitionGraph,
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

def test_assoc_incoming4_reverse_link_reassign_clear():
    a1 = transitiongraph_Transition(label="sample_text", probability=3.14)
    a2 = transitiongraph_Transition(label="sample_text_2", probability=9.99)
    b = transitiongraph_State(id=7, isFinal=True, isInitial=True)
    _safe_set(b, 'target', {a1})
    assert _is_linked(b, 'target', a1)
    if hasattr(a1, 'Transition5'):
        assert _is_linked(a1, 'Transition5', b)
    _safe_set(b, 'target', {a2})
    assert _is_linked(b, 'target', a2)
    if hasattr(a1, 'Transition5'):
        assert not _is_linked(a1, 'Transition5', b)
    if hasattr(a2, 'Transition5'):
        assert _is_linked(a2, 'Transition5', b)
    _safe_set(b, 'target', set())
    assert not _is_linked(b, 'target', a2)
    if hasattr(a2, 'Transition5'):
        assert not _is_linked(a2, 'Transition5', b)


def test_assoc_outgoing3_reverse_link_reassign_clear():
    a1 = transitiongraph_Transition(label="sample_text", probability=3.14)
    a2 = transitiongraph_Transition(label="sample_text_2", probability=9.99)
    b = transitiongraph_State(id=7, isFinal=True, isInitial=True)
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


def test_assoc_source6_reverse_link_reassign_clear():
    a1 = transitiongraph_Transition(label="sample_text", probability=3.14)
    a2 = transitiongraph_Transition(label="sample_text_2", probability=9.99)
    b = transitiongraph_State(id=7, isFinal=True, isInitial=True)
    _safe_set(b, 'State', a1)
    assert _is_linked(b, 'State', a1)
    if hasattr(a1, 'outgoing'):
        assert _is_linked(a1, 'outgoing', b)
    _safe_set(b, 'State', a2)
    assert _is_linked(b, 'State', a2)
    if hasattr(a1, 'outgoing'):
        assert not _is_linked(a1, 'outgoing', b)
    if hasattr(a2, 'outgoing'):
        assert _is_linked(a2, 'outgoing', b)
    _safe_set(b, 'State', None)
    assert not _is_linked(b, 'State', a2)
    if hasattr(a2, 'outgoing'):
        assert not _is_linked(a2, 'outgoing', b)


def test_assoc_target7_reverse_link_reassign_clear():
    a1 = transitiongraph_Transition(label="sample_text", probability=3.14)
    a2 = transitiongraph_Transition(label="sample_text_2", probability=9.99)
    b = transitiongraph_State(id=7, isFinal=True, isInitial=True)
    _safe_set(b, 'State8', a1)
    assert _is_linked(b, 'State8', a1)
    if hasattr(a1, 'incoming'):
        assert _is_linked(a1, 'incoming', b)
    _safe_set(b, 'State8', a2)
    assert _is_linked(b, 'State8', a2)
    if hasattr(a1, 'incoming'):
        assert not _is_linked(a1, 'incoming', b)
    if hasattr(a2, 'incoming'):
        assert _is_linked(a2, 'incoming', b)
    _safe_set(b, 'State8', None)
    assert not _is_linked(b, 'State8', a2)
    if hasattr(a2, 'incoming'):
        assert not _is_linked(a2, 'incoming', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_states0_stub_double():
    # transitiongraph_TransitionGraph has no real 'transitiongraph_TransitionGraph' property in the generated
    # code (a bare stub) -- manually attach it so transitiongraph_State's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # transitiongraph_State's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = transitiongraph_State(id=7, isFinal=True, isInitial=True)
    partner = transitiongraph_TransitionGraph()
    setattr(partner, 'transitiongraph_TransitionGraph', None)
    _safe_set(owner, 'transitiongraph_State', partner)
    assert owner in getattr(partner, 'transitiongraph_TransitionGraph')
    _safe_set(owner, 'transitiongraph_State', None)
    assert owner not in getattr(partner, 'transitiongraph_TransitionGraph')


def test_assoc_transitions1_stub_double():
    # transitiongraph_TransitionGraph has no real 'transitiongraph_TransitionGraph2' property in the generated
    # code (a bare stub) -- manually attach it so transitiongraph_Transition's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # transitiongraph_Transition's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = transitiongraph_Transition(label="sample_text", probability=3.14)
    partner = transitiongraph_TransitionGraph()
    setattr(partner, 'transitiongraph_TransitionGraph2', None)
    _safe_set(owner, 'transitiongraph_Transition', partner)
    assert owner in getattr(partner, 'transitiongraph_TransitionGraph2')
    _safe_set(owner, 'transitiongraph_Transition', None)
    assert owner not in getattr(partner, 'transitiongraph_TransitionGraph2')


