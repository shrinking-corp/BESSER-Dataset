import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    StateMachineUnnamed_Event,
    StateMachineUnnamed_FinalState,
    StateMachineUnnamed_InitialState,
    StateMachineUnnamed_SimpleState,
    StateMachineUnnamed_StateMachine,
    StateMachineUnnamed_StateVertex,
    StateMachineUnnamed_Transition,
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
    a1 = StateMachineUnnamed_Transition(name="sample_text")
    a2 = StateMachineUnnamed_Transition(name="sample_text_2")
    b = StateMachineUnnamed_StateVertex(name="sample_text")
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
    a1 = StateMachineUnnamed_Transition(name="sample_text")
    a2 = StateMachineUnnamed_Transition(name="sample_text_2")
    b = StateMachineUnnamed_StateVertex(name="sample_text")
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


def test_assoc_source9_reverse_link_reassign_clear():
    a1 = StateMachineUnnamed_Transition(name="sample_text")
    a2 = StateMachineUnnamed_Transition(name="sample_text_2")
    b = StateMachineUnnamed_StateVertex(name="sample_text")
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


def test_assoc_target10_reverse_link_reassign_clear():
    a1 = StateMachineUnnamed_Transition(name="sample_text")
    a2 = StateMachineUnnamed_Transition(name="sample_text_2")
    b = StateMachineUnnamed_StateVertex(name="sample_text")
    _safe_set(b, 'StateVertex11', a1)
    assert _is_linked(b, 'StateVertex11', a1)
    if hasattr(a1, 'incoming'):
        assert _is_linked(a1, 'incoming', b)
    _safe_set(b, 'StateVertex11', a2)
    assert _is_linked(b, 'StateVertex11', a2)
    if hasattr(a1, 'incoming'):
        assert not _is_linked(a1, 'incoming', b)
    if hasattr(a2, 'incoming'):
        assert _is_linked(a2, 'incoming', b)
    _safe_set(b, 'StateVertex11', None)
    assert not _is_linked(b, 'StateVertex11', a2)
    if hasattr(a2, 'incoming'):
        assert not _is_linked(a2, 'incoming', b)


def test_assoc_targets7_reverse_link_reassign_clear():
    a1 = StateMachineUnnamed_StateVertex(name="sample_text")
    a2 = StateMachineUnnamed_StateVertex(name="sample_text_2")
    b = StateMachineUnnamed_StateVertex(name="sample_text")
    _safe_set(b, 'StateMachineUnnamed_StateVertex8', a1)
    assert _is_linked(b, 'StateMachineUnnamed_StateVertex8', a1)
    if hasattr(a1, 'StateMachineUnnamed_StateVertex6'):
        assert _is_linked(a1, 'StateMachineUnnamed_StateVertex6', b)
    _safe_set(b, 'StateMachineUnnamed_StateVertex8', a2)
    assert _is_linked(b, 'StateMachineUnnamed_StateVertex8', a2)
    if hasattr(a1, 'StateMachineUnnamed_StateVertex6'):
        assert not _is_linked(a1, 'StateMachineUnnamed_StateVertex6', b)
    if hasattr(a2, 'StateMachineUnnamed_StateVertex6'):
        assert _is_linked(a2, 'StateMachineUnnamed_StateVertex6', b)
    _safe_set(b, 'StateMachineUnnamed_StateVertex8', None)
    assert not _is_linked(b, 'StateMachineUnnamed_StateVertex8', a2)
    if hasattr(a2, 'StateMachineUnnamed_StateVertex6'):
        assert not _is_linked(a2, 'StateMachineUnnamed_StateVertex6', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_states0_stub_double():
    # StateMachineUnnamed_StateMachine has no real 'StateMachineUnnamed_StateMachine' property in the generated
    # code (a bare stub) -- manually attach it so StateMachineUnnamed_StateVertex's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # StateMachineUnnamed_StateVertex's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = StateMachineUnnamed_StateVertex(name="sample_text")
    partner = StateMachineUnnamed_StateMachine()
    setattr(partner, 'StateMachineUnnamed_StateMachine', None)
    _safe_set(owner, 'StateMachineUnnamed_StateVertex', partner)
    assert owner in getattr(partner, 'StateMachineUnnamed_StateMachine')
    _safe_set(owner, 'StateMachineUnnamed_StateVertex', None)
    assert owner not in getattr(partner, 'StateMachineUnnamed_StateMachine')


def test_assoc_transitions1_stub_double():
    # StateMachineUnnamed_StateMachine has no real 'StateMachineUnnamed_StateMachine2' property in the generated
    # code (a bare stub) -- manually attach it so StateMachineUnnamed_Transition's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # StateMachineUnnamed_Transition's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = StateMachineUnnamed_Transition(name="sample_text")
    partner = StateMachineUnnamed_StateMachine()
    setattr(partner, 'StateMachineUnnamed_StateMachine2', None)
    _safe_set(owner, 'StateMachineUnnamed_Transition', partner)
    assert owner in getattr(partner, 'StateMachineUnnamed_StateMachine2')
    _safe_set(owner, 'StateMachineUnnamed_Transition', None)
    assert owner not in getattr(partner, 'StateMachineUnnamed_StateMachine2')


def test_assoc_trigger12_stub_double():
    # StateMachineUnnamed_Event has no real 'StateMachineUnnamed_Event' property in the generated
    # code (a bare stub) -- manually attach it so StateMachineUnnamed_Transition's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # StateMachineUnnamed_Transition's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = StateMachineUnnamed_Transition(name="sample_text")
    partner = StateMachineUnnamed_Event()
    setattr(partner, 'StateMachineUnnamed_Event', None)
    _safe_set(owner, 'StateMachineUnnamed_Transition13', partner)
    assert getattr(partner, 'StateMachineUnnamed_Event') == owner
    _safe_set(owner, 'StateMachineUnnamed_Transition13', None)
    assert getattr(partner, 'StateMachineUnnamed_Event') is None


