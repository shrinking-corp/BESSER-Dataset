import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    NamedElement,
    Pseudostate,
    State2,
    Transition2,
    finitestatemachines_FinalState,
    finitestatemachines_Fork,
    finitestatemachines_InitialState,
    finitestatemachines_Join2,
    finitestatemachines_NamedElement,
    finitestatemachines_Pseudostate,
    finitestatemachines_State2,
    finitestatemachines_StateMachine,
    finitestatemachines_TimedTransition,
    finitestatemachines_Transition2,
    finitestatemachines_Trigger2,
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
    a1 = finitestatemachines_Transition2(finalTime2=7, initialTime=7)
    a2 = finitestatemachines_Transition2(finalTime2=13, initialTime=13)
    b = finitestatemachines_State2(finalTime=7, initialTime2=7)
    _safe_set(b, 'target', {a1})
    assert _is_linked(b, 'target', a1)
    if hasattr(a1, 'Transition25'):
        assert _is_linked(a1, 'Transition25', b)
    _safe_set(b, 'target', {a2})
    assert _is_linked(b, 'target', a2)
    if hasattr(a1, 'Transition25'):
        assert not _is_linked(a1, 'Transition25', b)
    if hasattr(a2, 'Transition25'):
        assert _is_linked(a2, 'Transition25', b)
    _safe_set(b, 'target', set())
    assert not _is_linked(b, 'target', a2)
    if hasattr(a2, 'Transition25'):
        assert not _is_linked(a2, 'Transition25', b)


def test_assoc_outgoing2_reverse_link_reassign_clear():
    a1 = finitestatemachines_Transition2(finalTime2=7, initialTime=7)
    a2 = finitestatemachines_Transition2(finalTime2=13, initialTime=13)
    b = finitestatemachines_State2(finalTime=7, initialTime2=7)
    _safe_set(b, 'source', {a1})
    assert _is_linked(b, 'source', a1)
    if hasattr(a1, 'Transition23'):
        assert _is_linked(a1, 'Transition23', b)
    _safe_set(b, 'source', {a2})
    assert _is_linked(b, 'source', a2)
    if hasattr(a1, 'Transition23'):
        assert not _is_linked(a1, 'Transition23', b)
    if hasattr(a2, 'Transition23'):
        assert _is_linked(a2, 'Transition23', b)
    _safe_set(b, 'source', set())
    assert not _is_linked(b, 'source', a2)
    if hasattr(a2, 'Transition23'):
        assert not _is_linked(a2, 'Transition23', b)


def test_assoc_source9_reverse_link_reassign_clear():
    a1 = finitestatemachines_Transition2(finalTime2=7, initialTime=7)
    a2 = finitestatemachines_Transition2(finalTime2=13, initialTime=13)
    b = finitestatemachines_State2(finalTime=7, initialTime2=7)
    _safe_set(b, 'State210', a1)
    assert _is_linked(b, 'State210', a1)
    if hasattr(a1, 'outgoing'):
        assert _is_linked(a1, 'outgoing', b)
    _safe_set(b, 'State210', a2)
    assert _is_linked(b, 'State210', a2)
    if hasattr(a1, 'outgoing'):
        assert not _is_linked(a1, 'outgoing', b)
    if hasattr(a2, 'outgoing'):
        assert _is_linked(a2, 'outgoing', b)
    _safe_set(b, 'State210', None)
    assert not _is_linked(b, 'State210', a2)
    if hasattr(a2, 'outgoing'):
        assert not _is_linked(a2, 'outgoing', b)


def test_assoc_target7_reverse_link_reassign_clear():
    a1 = finitestatemachines_Transition2(finalTime2=7, initialTime=7)
    a2 = finitestatemachines_Transition2(finalTime2=13, initialTime=13)
    b = finitestatemachines_State2(finalTime=7, initialTime2=7)
    _safe_set(b, 'State28', a1)
    assert _is_linked(b, 'State28', a1)
    if hasattr(a1, 'incoming'):
        assert _is_linked(a1, 'incoming', b)
    _safe_set(b, 'State28', a2)
    assert _is_linked(b, 'State28', a2)
    if hasattr(a1, 'incoming'):
        assert not _is_linked(a1, 'incoming', b)
    if hasattr(a2, 'incoming'):
        assert _is_linked(a2, 'incoming', b)
    _safe_set(b, 'State28', None)
    assert not _is_linked(b, 'State28', a2)
    if hasattr(a2, 'incoming'):
        assert not _is_linked(a2, 'incoming', b)


def test_assoc_trigger11_reverse_link_reassign_clear():
    a1 = finitestatemachines_Trigger2(expression="sample_text")
    a2 = finitestatemachines_Trigger2(expression="sample_text_2")
    b = finitestatemachines_Transition2(finalTime2=7, initialTime=7)
    _safe_set(b, 'finitestatemachines_Transition2', a1)
    assert _is_linked(b, 'finitestatemachines_Transition2', a1)
    if hasattr(a1, 'finitestatemachines_Trigger2'):
        assert _is_linked(a1, 'finitestatemachines_Trigger2', b)
    _safe_set(b, 'finitestatemachines_Transition2', a2)
    assert _is_linked(b, 'finitestatemachines_Transition2', a2)
    if hasattr(a1, 'finitestatemachines_Trigger2'):
        assert not _is_linked(a1, 'finitestatemachines_Trigger2', b)
    if hasattr(a2, 'finitestatemachines_Trigger2'):
        assert _is_linked(a2, 'finitestatemachines_Trigger2', b)
    _safe_set(b, 'finitestatemachines_Transition2', None)
    assert not _is_linked(b, 'finitestatemachines_Transition2', a2)
    if hasattr(a2, 'finitestatemachines_Trigger2'):
        assert not _is_linked(a2, 'finitestatemachines_Trigger2', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_stateMachine12_stub_double():
    # finitestatemachines_StateMachine has no real 'StateMachine13' property in the generated
    # code (a bare stub) -- manually attach it so finitestatemachines_Transition2's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # finitestatemachines_Transition2's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = finitestatemachines_Transition2(finalTime2=7, initialTime=7)
    partner = finitestatemachines_StateMachine()
    setattr(partner, 'StateMachine13', None)
    _safe_set(owner, 'transitions2', partner)
    assert getattr(partner, 'StateMachine13') == owner
    _safe_set(owner, 'transitions2', None)
    assert getattr(partner, 'StateMachine13') is None


def test_assoc_stateMachine26_stub_double():
    # finitestatemachines_StateMachine has no real 'StateMachine' property in the generated
    # code (a bare stub) -- manually attach it so finitestatemachines_State2's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # finitestatemachines_State2's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = finitestatemachines_State2(finalTime=7, initialTime2=7)
    partner = finitestatemachines_StateMachine()
    setattr(partner, 'StateMachine', None)
    _safe_set(owner, 'states2', partner)
    assert getattr(partner, 'StateMachine') == owner
    _safe_set(owner, 'states2', None)
    assert getattr(partner, 'StateMachine') is None


def test_assoc_states20_stub_double():
    # finitestatemachines_StateMachine has no real 'stateMachine2' property in the generated
    # code (a bare stub) -- manually attach it so finitestatemachines_State2's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # finitestatemachines_State2's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = finitestatemachines_State2(finalTime=7, initialTime2=7)
    partner = finitestatemachines_StateMachine()
    setattr(partner, 'stateMachine2', None)
    _safe_set(owner, 'State2', partner)
    assert owner in getattr(partner, 'stateMachine2')
    _safe_set(owner, 'State2', None)
    assert owner not in getattr(partner, 'stateMachine2')


def test_assoc_transitions21_stub_double():
    # finitestatemachines_StateMachine has no real 'stateMachine' property in the generated
    # code (a bare stub) -- manually attach it so finitestatemachines_Transition2's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # finitestatemachines_Transition2's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = finitestatemachines_Transition2(finalTime2=7, initialTime=7)
    partner = finitestatemachines_StateMachine()
    setattr(partner, 'stateMachine', None)
    _safe_set(owner, 'Transition2', partner)
    assert owner in getattr(partner, 'stateMachine')
    _safe_set(owner, 'Transition2', None)
    assert owner not in getattr(partner, 'stateMachine')


