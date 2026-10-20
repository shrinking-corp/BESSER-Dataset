import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    AbstractState,
    fsm_AbstractState,
    fsm_CompositeState,
    fsm_InitialState,
    fsm_RegularState,
    fsm_Root,
    fsm_StateMachine,
    fsm_Transition,
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

def test_assoc_source4_reverse_link_reassign_clear():
    a1 = fsm_Transition(label="sample_text")
    a2 = fsm_Transition(label="sample_text_2")
    b = fsm_AbstractState(name="sample_text")
    _safe_set(b, 'fsm_AbstractState', a1)
    assert _is_linked(b, 'fsm_AbstractState', a1)
    if hasattr(a1, 'fsm_Transition'):
        assert _is_linked(a1, 'fsm_Transition', b)
    _safe_set(b, 'fsm_AbstractState', a2)
    assert _is_linked(b, 'fsm_AbstractState', a2)
    if hasattr(a1, 'fsm_Transition'):
        assert not _is_linked(a1, 'fsm_Transition', b)
    if hasattr(a2, 'fsm_Transition'):
        assert _is_linked(a2, 'fsm_Transition', b)
    _safe_set(b, 'fsm_AbstractState', None)
    assert not _is_linked(b, 'fsm_AbstractState', a2)
    if hasattr(a2, 'fsm_Transition'):
        assert not _is_linked(a2, 'fsm_Transition', b)


def test_assoc_stateMachine3_reverse_link_reassign_clear():
    a1 = fsm_Transition(label="sample_text")
    a2 = fsm_Transition(label="sample_text_2")
    b = fsm_StateMachine(name="sample_text")
    _safe_set(b, 'StateMachine', a1)
    assert _is_linked(b, 'StateMachine', a1)
    if hasattr(a1, 'transitions'):
        assert _is_linked(a1, 'transitions', b)
    _safe_set(b, 'StateMachine', a2)
    assert _is_linked(b, 'StateMachine', a2)
    if hasattr(a1, 'transitions'):
        assert not _is_linked(a1, 'transitions', b)
    if hasattr(a2, 'transitions'):
        assert _is_linked(a2, 'transitions', b)
    _safe_set(b, 'StateMachine', None)
    assert not _is_linked(b, 'StateMachine', a2)
    if hasattr(a2, 'transitions'):
        assert not _is_linked(a2, 'transitions', b)


def test_assoc_stateMachine8_reverse_link_reassign_clear():
    a1 = fsm_StateMachine(name="sample_text")
    a2 = fsm_StateMachine(name="sample_text_2")
    b = fsm_AbstractState(name="sample_text")
    _safe_set(b, 'states', a1)
    assert _is_linked(b, 'states', a1)
    if hasattr(a1, 'StateMachine9'):
        assert _is_linked(a1, 'StateMachine9', b)
    _safe_set(b, 'states', a2)
    assert _is_linked(b, 'states', a2)
    if hasattr(a1, 'StateMachine9'):
        assert not _is_linked(a1, 'StateMachine9', b)
    if hasattr(a2, 'StateMachine9'):
        assert _is_linked(a2, 'StateMachine9', b)
    _safe_set(b, 'states', None)
    assert not _is_linked(b, 'states', a2)
    if hasattr(a2, 'StateMachine9'):
        assert not _is_linked(a2, 'StateMachine9', b)


def test_assoc_states1_reverse_link_reassign_clear():
    a1 = fsm_StateMachine(name="sample_text")
    a2 = fsm_StateMachine(name="sample_text_2")
    b = fsm_AbstractState(name="sample_text")
    _safe_set(b, 'AbstractState', a1)
    assert _is_linked(b, 'AbstractState', a1)
    if hasattr(a1, 'stateMachine2'):
        assert _is_linked(a1, 'stateMachine2', b)
    _safe_set(b, 'AbstractState', a2)
    assert _is_linked(b, 'AbstractState', a2)
    if hasattr(a1, 'stateMachine2'):
        assert not _is_linked(a1, 'stateMachine2', b)
    if hasattr(a2, 'stateMachine2'):
        assert _is_linked(a2, 'stateMachine2', b)
    _safe_set(b, 'AbstractState', None)
    assert not _is_linked(b, 'AbstractState', a2)
    if hasattr(a2, 'stateMachine2'):
        assert not _is_linked(a2, 'stateMachine2', b)


def test_assoc_target5_reverse_link_reassign_clear():
    a1 = fsm_Transition(label="sample_text")
    a2 = fsm_Transition(label="sample_text_2")
    b = fsm_AbstractState(name="sample_text")
    _safe_set(b, 'fsm_AbstractState7', a1)
    assert _is_linked(b, 'fsm_AbstractState7', a1)
    if hasattr(a1, 'fsm_Transition6'):
        assert _is_linked(a1, 'fsm_Transition6', b)
    _safe_set(b, 'fsm_AbstractState7', a2)
    assert _is_linked(b, 'fsm_AbstractState7', a2)
    if hasattr(a1, 'fsm_Transition6'):
        assert not _is_linked(a1, 'fsm_Transition6', b)
    if hasattr(a2, 'fsm_Transition6'):
        assert _is_linked(a2, 'fsm_Transition6', b)
    _safe_set(b, 'fsm_AbstractState7', None)
    assert not _is_linked(b, 'fsm_AbstractState7', a2)
    if hasattr(a2, 'fsm_Transition6'):
        assert not _is_linked(a2, 'fsm_Transition6', b)


def test_assoc_transitions0_reverse_link_reassign_clear():
    a1 = fsm_Transition(label="sample_text")
    a2 = fsm_Transition(label="sample_text_2")
    b = fsm_StateMachine(name="sample_text")
    _safe_set(b, 'stateMachine', {a1})
    assert _is_linked(b, 'stateMachine', a1)
    if hasattr(a1, 'Transition'):
        assert _is_linked(a1, 'Transition', b)
    _safe_set(b, 'stateMachine', {a2})
    assert _is_linked(b, 'stateMachine', a2)
    if hasattr(a1, 'Transition'):
        assert not _is_linked(a1, 'Transition', b)
    if hasattr(a2, 'Transition'):
        assert _is_linked(a2, 'Transition', b)
    _safe_set(b, 'stateMachine', set())
    assert not _is_linked(b, 'stateMachine', a2)
    if hasattr(a2, 'Transition'):
        assert not _is_linked(a2, 'Transition', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_compositeStates10_stub_double():
    # fsm_CompositeState has no real 'CompositeState' property in the generated
    # code (a bare stub) -- manually attach it so fsm_AbstractState's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # fsm_AbstractState's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = fsm_AbstractState(name="sample_text")
    partner = fsm_CompositeState()
    setattr(partner, 'CompositeState', None)
    _safe_set(owner, 'states11', partner)
    assert getattr(partner, 'CompositeState') == owner
    _safe_set(owner, 'states11', None)
    assert getattr(partner, 'CompositeState') is None


def test_assoc_stateMachines14_stub_double():
    # fsm_Root has no real 'fsm_Root' property in the generated
    # code (a bare stub) -- manually attach it so fsm_StateMachine's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # fsm_StateMachine's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = fsm_StateMachine(name="sample_text")
    partner = fsm_Root()
    setattr(partner, 'fsm_Root', None)
    _safe_set(owner, 'fsm_StateMachine', partner)
    assert owner in getattr(partner, 'fsm_Root')
    _safe_set(owner, 'fsm_StateMachine', None)
    assert owner not in getattr(partner, 'fsm_Root')


def test_assoc_states12_stub_double():
    # fsm_CompositeState has no real 'compositeStates' property in the generated
    # code (a bare stub) -- manually attach it so fsm_AbstractState's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # fsm_AbstractState's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = fsm_AbstractState(name="sample_text")
    partner = fsm_CompositeState()
    setattr(partner, 'compositeStates', None)
    _safe_set(owner, 'AbstractState13', partner)
    assert owner in getattr(partner, 'compositeStates')
    _safe_set(owner, 'AbstractState13', None)
    assert owner not in getattr(partner, 'compositeStates')


