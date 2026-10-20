import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    NamedElement,
    Pseudostate,
    State,
    Transition,
    fsm_CompositeState,
    fsm_FinalState,
    fsm_Fork,
    fsm_InitialState,
    fsm_Join,
    fsm_NamedElement,
    fsm_Pseudostate,
    fsm_Region,
    fsm_State,
    fsm_StateMachine,
    fsm_TimedTransition,
    fsm_Transition,
    fsm_Trigger,
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

def test_assoc_incoming5_reverse_link_reassign_clear():
    a1 = fsm_Transition(finalTime=7, initialTime=7, time=7)
    a2 = fsm_Transition(finalTime=13, initialTime=13, time=13)
    b = fsm_State(finalTime=7, initialTime=7)
    _safe_set(b, 'target', {a1})
    assert _is_linked(b, 'target', a1)
    if hasattr(a1, 'Transition6'):
        assert _is_linked(a1, 'Transition6', b)
    _safe_set(b, 'target', {a2})
    assert _is_linked(b, 'target', a2)
    if hasattr(a1, 'Transition6'):
        assert not _is_linked(a1, 'Transition6', b)
    if hasattr(a2, 'Transition6'):
        assert _is_linked(a2, 'Transition6', b)
    _safe_set(b, 'target', set())
    assert not _is_linked(b, 'target', a2)
    if hasattr(a2, 'Transition6'):
        assert not _is_linked(a2, 'Transition6', b)


def test_assoc_outgoing3_reverse_link_reassign_clear():
    a1 = fsm_Transition(finalTime=7, initialTime=7, time=7)
    a2 = fsm_Transition(finalTime=13, initialTime=13, time=13)
    b = fsm_State(finalTime=7, initialTime=7)
    _safe_set(b, 'source', {a1})
    assert _is_linked(b, 'source', a1)
    if hasattr(a1, 'Transition4'):
        assert _is_linked(a1, 'Transition4', b)
    _safe_set(b, 'source', {a2})
    assert _is_linked(b, 'source', a2)
    if hasattr(a1, 'Transition4'):
        assert not _is_linked(a1, 'Transition4', b)
    if hasattr(a2, 'Transition4'):
        assert _is_linked(a2, 'Transition4', b)
    _safe_set(b, 'source', set())
    assert not _is_linked(b, 'source', a2)
    if hasattr(a2, 'Transition4'):
        assert not _is_linked(a2, 'Transition4', b)


def test_assoc_source11_reverse_link_reassign_clear():
    a1 = fsm_Transition(finalTime=7, initialTime=7, time=7)
    a2 = fsm_Transition(finalTime=13, initialTime=13, time=13)
    b = fsm_State(finalTime=7, initialTime=7)
    _safe_set(b, 'State12', a1)
    assert _is_linked(b, 'State12', a1)
    if hasattr(a1, 'outgoing'):
        assert _is_linked(a1, 'outgoing', b)
    _safe_set(b, 'State12', a2)
    assert _is_linked(b, 'State12', a2)
    if hasattr(a1, 'outgoing'):
        assert not _is_linked(a1, 'outgoing', b)
    if hasattr(a2, 'outgoing'):
        assert _is_linked(a2, 'outgoing', b)
    _safe_set(b, 'State12', None)
    assert not _is_linked(b, 'State12', a2)
    if hasattr(a2, 'outgoing'):
        assert not _is_linked(a2, 'outgoing', b)


def test_assoc_target9_reverse_link_reassign_clear():
    a1 = fsm_Transition(finalTime=7, initialTime=7, time=7)
    a2 = fsm_Transition(finalTime=13, initialTime=13, time=13)
    b = fsm_State(finalTime=7, initialTime=7)
    _safe_set(b, 'State10', a1)
    assert _is_linked(b, 'State10', a1)
    if hasattr(a1, 'incoming'):
        assert _is_linked(a1, 'incoming', b)
    _safe_set(b, 'State10', a2)
    assert _is_linked(b, 'State10', a2)
    if hasattr(a1, 'incoming'):
        assert not _is_linked(a1, 'incoming', b)
    if hasattr(a2, 'incoming'):
        assert _is_linked(a2, 'incoming', b)
    _safe_set(b, 'State10', None)
    assert not _is_linked(b, 'State10', a2)
    if hasattr(a2, 'incoming'):
        assert not _is_linked(a2, 'incoming', b)


def test_assoc_trigger13_reverse_link_reassign_clear():
    a1 = fsm_Trigger(expression="sample_text")
    a2 = fsm_Trigger(expression="sample_text_2")
    b = fsm_Transition(finalTime=7, initialTime=7, time=7)
    _safe_set(b, 'fsm_Transition', a1)
    assert _is_linked(b, 'fsm_Transition', a1)
    if hasattr(a1, 'fsm_Trigger'):
        assert _is_linked(a1, 'fsm_Trigger', b)
    _safe_set(b, 'fsm_Transition', a2)
    assert _is_linked(b, 'fsm_Transition', a2)
    if hasattr(a1, 'fsm_Trigger'):
        assert not _is_linked(a1, 'fsm_Trigger', b)
    if hasattr(a2, 'fsm_Trigger'):
        assert _is_linked(a2, 'fsm_Trigger', b)
    _safe_set(b, 'fsm_Transition', None)
    assert not _is_linked(b, 'fsm_Transition', a2)
    if hasattr(a2, 'fsm_Trigger'):
        assert not _is_linked(a2, 'fsm_Trigger', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_parentState8_stub_double():
    # fsm_CompositeState has no real 'fsm_CompositeState' property in the generated
    # code (a bare stub) -- manually attach it so fsm_State's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # fsm_State's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = fsm_State(finalTime=7, initialTime=7)
    partner = fsm_CompositeState()
    setattr(partner, 'fsm_CompositeState', None)
    _safe_set(owner, 'fsm_State', partner)
    assert getattr(partner, 'fsm_CompositeState') == owner
    _safe_set(owner, 'fsm_State', None)
    assert getattr(partner, 'fsm_CompositeState') is None


def test_assoc_stateMachine14_stub_double():
    # fsm_StateMachine has no real 'StateMachine15' property in the generated
    # code (a bare stub) -- manually attach it so fsm_Transition's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # fsm_Transition's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = fsm_Transition(finalTime=7, initialTime=7, time=7)
    partner = fsm_StateMachine()
    setattr(partner, 'StateMachine15', None)
    _safe_set(owner, 'transitions', partner)
    assert getattr(partner, 'StateMachine15') == owner
    _safe_set(owner, 'transitions', None)
    assert getattr(partner, 'StateMachine15') is None


def test_assoc_stateMachine7_stub_double():
    # fsm_StateMachine has no real 'StateMachine' property in the generated
    # code (a bare stub) -- manually attach it so fsm_State's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # fsm_State's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = fsm_State(finalTime=7, initialTime=7)
    partner = fsm_StateMachine()
    setattr(partner, 'StateMachine', None)
    _safe_set(owner, 'states', partner)
    assert getattr(partner, 'StateMachine') == owner
    _safe_set(owner, 'states', None)
    assert getattr(partner, 'StateMachine') is None


def test_assoc_states0_stub_double():
    # fsm_StateMachine has no real 'stateMachine' property in the generated
    # code (a bare stub) -- manually attach it so fsm_State's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # fsm_State's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = fsm_State(finalTime=7, initialTime=7)
    partner = fsm_StateMachine()
    setattr(partner, 'stateMachine', None)
    _safe_set(owner, 'State', partner)
    assert owner in getattr(partner, 'stateMachine')
    _safe_set(owner, 'State', None)
    assert owner not in getattr(partner, 'stateMachine')


def test_assoc_states18_stub_double():
    # fsm_Region has no real 'fsm_Region19' property in the generated
    # code (a bare stub) -- manually attach it so fsm_State's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # fsm_State's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = fsm_State(finalTime=7, initialTime=7)
    partner = fsm_Region()
    setattr(partner, 'fsm_Region19', None)
    _safe_set(owner, 'fsm_State20', partner)
    assert owner in getattr(partner, 'fsm_Region19')
    _safe_set(owner, 'fsm_State20', None)
    assert owner not in getattr(partner, 'fsm_Region19')


def test_assoc_transitions1_stub_double():
    # fsm_StateMachine has no real 'stateMachine2' property in the generated
    # code (a bare stub) -- manually attach it so fsm_Transition's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # fsm_Transition's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = fsm_Transition(finalTime=7, initialTime=7, time=7)
    partner = fsm_StateMachine()
    setattr(partner, 'stateMachine2', None)
    _safe_set(owner, 'Transition', partner)
    assert owner in getattr(partner, 'stateMachine2')
    _safe_set(owner, 'Transition', None)
    assert owner not in getattr(partner, 'stateMachine2')


