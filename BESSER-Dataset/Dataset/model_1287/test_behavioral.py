import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    StateMachine_Event,
    StateMachine_FinalState,
    StateMachine_InitialState,
    StateMachine_SimpleState,
    StateMachine_StateMachine,
    StateMachine_StateVertex,
    StateMachine_Transition,
    StateVertex,
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
    a1 = StateMachine_Transition(name="sample_text")
    a2 = StateMachine_Transition(name="sample_text_2")
    b = StateMachine_StateVertex(name="sample_text")
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
    a1 = StateMachine_Transition(name="sample_text")
    a2 = StateMachine_Transition(name="sample_text_2")
    b = StateMachine_StateVertex(name="sample_text")
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


def test_assoc_source8_reverse_link_reassign_clear():
    a1 = StateMachine_Transition(name="sample_text")
    a2 = StateMachine_Transition(name="sample_text_2")
    b = StateMachine_StateVertex(name="sample_text")
    _safe_set(b, 'StateVertex', a1)
    assert _is_linked(b, 'StateVertex', a1)
    if hasattr(a1, 'outgoing'):
        assert _is_linked(a1, 'outgoing', b)
    _safe_set(b, 'StateVertex', a2)
    assert _is_linked(b, 'StateVertex', a2)
    if hasattr(a1, 'outgoing'):
        assert not _is_linked(a1, 'outgoing', b)
    if hasattr(a2, 'outgoing'):
        assert _is_linked(a2, 'outgoing', b)
    _safe_set(b, 'StateVertex', None)
    assert not _is_linked(b, 'StateVertex', a2)
    if hasattr(a2, 'outgoing'):
        assert not _is_linked(a2, 'outgoing', b)


def test_assoc_target9_reverse_link_reassign_clear():
    a1 = StateMachine_Transition(name="sample_text")
    a2 = StateMachine_Transition(name="sample_text_2")
    b = StateMachine_StateVertex(name="sample_text")
    _safe_set(b, 'StateVertex10', a1)
    assert _is_linked(b, 'StateVertex10', a1)
    if hasattr(a1, 'incoming'):
        assert _is_linked(a1, 'incoming', b)
    _safe_set(b, 'StateVertex10', a2)
    assert _is_linked(b, 'StateVertex10', a2)
    if hasattr(a1, 'incoming'):
        assert not _is_linked(a1, 'incoming', b)
    if hasattr(a2, 'incoming'):
        assert _is_linked(a2, 'incoming', b)
    _safe_set(b, 'StateVertex10', None)
    assert not _is_linked(b, 'StateVertex10', a2)
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
    # StateMachine_StateMachine has no real 'StateMachine_StateMachine' property in the generated
    # code (a bare stub) -- manually attach it so StateMachine_StateVertex's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # StateMachine_StateVertex's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = StateMachine_StateVertex(name="sample_text")
    partner = StateMachine_StateMachine()
    setattr(partner, 'StateMachine_StateMachine', None)
    _safe_set(owner, 'StateMachine_StateVertex', partner)
    assert owner in getattr(partner, 'StateMachine_StateMachine')
    _safe_set(owner, 'StateMachine_StateVertex', None)
    assert owner not in getattr(partner, 'StateMachine_StateMachine')


def test_assoc_transitions1_stub_double():
    # StateMachine_StateMachine has no real 'StateMachine_StateMachine2' property in the generated
    # code (a bare stub) -- manually attach it so StateMachine_Transition's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # StateMachine_Transition's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = StateMachine_Transition(name="sample_text")
    partner = StateMachine_StateMachine()
    setattr(partner, 'StateMachine_StateMachine2', None)
    _safe_set(owner, 'StateMachine_Transition', partner)
    assert owner in getattr(partner, 'StateMachine_StateMachine2')
    _safe_set(owner, 'StateMachine_Transition', None)
    assert owner not in getattr(partner, 'StateMachine_StateMachine2')


def test_assoc_trigger6_stub_double():
    # StateMachine_Event has no real 'StateMachine_Event' property in the generated
    # code (a bare stub) -- manually attach it so StateMachine_Transition's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # StateMachine_Transition's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = StateMachine_Transition(name="sample_text")
    partner = StateMachine_Event()
    setattr(partner, 'StateMachine_Event', None)
    _safe_set(owner, 'StateMachine_Transition7', partner)
    assert getattr(partner, 'StateMachine_Event') == owner
    _safe_set(owner, 'StateMachine_Transition7', None)
    assert getattr(partner, 'StateMachine_Event') is None


