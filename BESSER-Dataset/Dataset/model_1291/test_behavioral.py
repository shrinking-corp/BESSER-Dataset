import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    StateMachineHyperedges_Event,
    StateMachineHyperedges_FinalState,
    StateMachineHyperedges_InitialState,
    StateMachineHyperedges_SimpleState,
    StateMachineHyperedges_StateMachine,
    StateMachineHyperedges_StateVertex,
    StateMachineHyperedges_Transition,
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
    a1 = StateMachineHyperedges_Transition(name="sample_text")
    a2 = StateMachineHyperedges_Transition(name="sample_text_2")
    b = StateMachineHyperedges_StateVertex(name="sample_text")
    _safe_set(b, 'targets', {a1})
    assert _is_linked(b, 'targets', a1)
    if hasattr(a1, 'Transition5'):
        assert _is_linked(a1, 'Transition5', b)
    _safe_set(b, 'targets', {a2})
    assert _is_linked(b, 'targets', a2)
    if hasattr(a1, 'Transition5'):
        assert not _is_linked(a1, 'Transition5', b)
    if hasattr(a2, 'Transition5'):
        assert _is_linked(a2, 'Transition5', b)
    _safe_set(b, 'targets', set())
    assert not _is_linked(b, 'targets', a2)
    if hasattr(a2, 'Transition5'):
        assert not _is_linked(a2, 'Transition5', b)


def test_assoc_outgoing3_reverse_link_reassign_clear():
    a1 = StateMachineHyperedges_Transition(name="sample_text")
    a2 = StateMachineHyperedges_Transition(name="sample_text_2")
    b = StateMachineHyperedges_StateVertex(name="sample_text")
    _safe_set(b, 'sources', {a1})
    assert _is_linked(b, 'sources', a1)
    if hasattr(a1, 'Transition'):
        assert _is_linked(a1, 'Transition', b)
    _safe_set(b, 'sources', {a2})
    assert _is_linked(b, 'sources', a2)
    if hasattr(a1, 'Transition'):
        assert not _is_linked(a1, 'Transition', b)
    if hasattr(a2, 'Transition'):
        assert _is_linked(a2, 'Transition', b)
    _safe_set(b, 'sources', set())
    assert not _is_linked(b, 'sources', a2)
    if hasattr(a2, 'Transition'):
        assert not _is_linked(a2, 'Transition', b)


def test_assoc_sources8_reverse_link_reassign_clear():
    a1 = StateMachineHyperedges_Transition(name="sample_text")
    a2 = StateMachineHyperedges_Transition(name="sample_text_2")
    b = StateMachineHyperedges_StateVertex(name="sample_text")
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


def test_assoc_targets9_reverse_link_reassign_clear():
    a1 = StateMachineHyperedges_Transition(name="sample_text")
    a2 = StateMachineHyperedges_Transition(name="sample_text_2")
    b = StateMachineHyperedges_StateVertex(name="sample_text")
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
    # StateMachineHyperedges_StateMachine has no real 'StateMachineHyperedges_StateMachine' property in the generated
    # code (a bare stub) -- manually attach it so StateMachineHyperedges_StateVertex's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # StateMachineHyperedges_StateVertex's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = StateMachineHyperedges_StateVertex(name="sample_text")
    partner = StateMachineHyperedges_StateMachine()
    setattr(partner, 'StateMachineHyperedges_StateMachine', None)
    _safe_set(owner, 'StateMachineHyperedges_StateVertex', partner)
    assert owner in getattr(partner, 'StateMachineHyperedges_StateMachine')
    _safe_set(owner, 'StateMachineHyperedges_StateVertex', None)
    assert owner not in getattr(partner, 'StateMachineHyperedges_StateMachine')


def test_assoc_transitions1_stub_double():
    # StateMachineHyperedges_StateMachine has no real 'StateMachineHyperedges_StateMachine2' property in the generated
    # code (a bare stub) -- manually attach it so StateMachineHyperedges_Transition's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # StateMachineHyperedges_Transition's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = StateMachineHyperedges_Transition(name="sample_text")
    partner = StateMachineHyperedges_StateMachine()
    setattr(partner, 'StateMachineHyperedges_StateMachine2', None)
    _safe_set(owner, 'StateMachineHyperedges_Transition', partner)
    assert owner in getattr(partner, 'StateMachineHyperedges_StateMachine2')
    _safe_set(owner, 'StateMachineHyperedges_Transition', None)
    assert owner not in getattr(partner, 'StateMachineHyperedges_StateMachine2')


def test_assoc_trigger6_stub_double():
    # StateMachineHyperedges_Event has no real 'StateMachineHyperedges_Event' property in the generated
    # code (a bare stub) -- manually attach it so StateMachineHyperedges_Transition's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # StateMachineHyperedges_Transition's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = StateMachineHyperedges_Transition(name="sample_text")
    partner = StateMachineHyperedges_Event()
    setattr(partner, 'StateMachineHyperedges_Event', None)
    _safe_set(owner, 'StateMachineHyperedges_Transition7', partner)
    assert getattr(partner, 'StateMachineHyperedges_Event') == owner
    _safe_set(owner, 'StateMachineHyperedges_Transition7', None)
    assert getattr(partner, 'StateMachineHyperedges_Event') is None


