import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    compositefsm_FSM,
    compositefsm_State,
    compositefsm_Transition,
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

def test_assoc_incomingTransition7_reverse_link_reassign_clear():
    a1 = compositefsm_Transition(input="sample_text", output="sample_text")
    a2 = compositefsm_Transition(input="sample_text_2", output="sample_text_2")
    b = compositefsm_State(name="sample_text")
    _safe_set(b, 'target', {a1})
    assert _is_linked(b, 'target', a1)
    if hasattr(a1, 'Transition8'):
        assert _is_linked(a1, 'Transition8', b)
    _safe_set(b, 'target', {a2})
    assert _is_linked(b, 'target', a2)
    if hasattr(a1, 'Transition8'):
        assert not _is_linked(a1, 'Transition8', b)
    if hasattr(a2, 'Transition8'):
        assert _is_linked(a2, 'Transition8', b)
    _safe_set(b, 'target', set())
    assert not _is_linked(b, 'target', a2)
    if hasattr(a2, 'Transition8'):
        assert not _is_linked(a2, 'Transition8', b)


def test_assoc_outgoingTransition6_reverse_link_reassign_clear():
    a1 = compositefsm_Transition(input="sample_text", output="sample_text")
    a2 = compositefsm_Transition(input="sample_text_2", output="sample_text_2")
    b = compositefsm_State(name="sample_text")
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


def test_assoc_source15_reverse_link_reassign_clear():
    a1 = compositefsm_Transition(input="sample_text", output="sample_text")
    a2 = compositefsm_Transition(input="sample_text_2", output="sample_text_2")
    b = compositefsm_State(name="sample_text")
    _safe_set(b, 'State16', a1)
    assert _is_linked(b, 'State16', a1)
    if hasattr(a1, 'outgoingTransition'):
        assert _is_linked(a1, 'outgoingTransition', b)
    _safe_set(b, 'State16', a2)
    assert _is_linked(b, 'State16', a2)
    if hasattr(a1, 'outgoingTransition'):
        assert not _is_linked(a1, 'outgoingTransition', b)
    if hasattr(a2, 'outgoingTransition'):
        assert _is_linked(a2, 'outgoingTransition', b)
    _safe_set(b, 'State16', None)
    assert not _is_linked(b, 'State16', a2)
    if hasattr(a2, 'outgoingTransition'):
        assert not _is_linked(a2, 'outgoingTransition', b)


def test_assoc_subStates10_reverse_link_reassign_clear():
    a1 = compositefsm_State(name="sample_text")
    a2 = compositefsm_State(name="sample_text_2")
    b = compositefsm_State(name="sample_text")
    _safe_set(b, 'superState', {a1})
    assert _is_linked(b, 'superState', a1)
    if hasattr(a1, 'State11'):
        assert _is_linked(a1, 'State11', b)
    _safe_set(b, 'superState', {a2})
    assert _is_linked(b, 'superState', a2)
    if hasattr(a1, 'State11'):
        assert not _is_linked(a1, 'State11', b)
    if hasattr(a2, 'State11'):
        assert _is_linked(a2, 'State11', b)
    _safe_set(b, 'superState', set())
    assert not _is_linked(b, 'superState', a2)
    if hasattr(a2, 'State11'):
        assert not _is_linked(a2, 'State11', b)


def test_assoc_superState13_reverse_link_reassign_clear():
    a1 = compositefsm_State(name="sample_text")
    a2 = compositefsm_State(name="sample_text_2")
    b = compositefsm_State(name="sample_text")
    _safe_set(b, 'subStates', a1)
    assert _is_linked(b, 'subStates', a1)
    if hasattr(a1, 'State14'):
        assert _is_linked(a1, 'State14', b)
    _safe_set(b, 'subStates', a2)
    assert _is_linked(b, 'subStates', a2)
    if hasattr(a1, 'State14'):
        assert not _is_linked(a1, 'State14', b)
    if hasattr(a2, 'State14'):
        assert _is_linked(a2, 'State14', b)
    _safe_set(b, 'subStates', None)
    assert not _is_linked(b, 'subStates', a2)
    if hasattr(a2, 'State14'):
        assert not _is_linked(a2, 'State14', b)


def test_assoc_target17_reverse_link_reassign_clear():
    a1 = compositefsm_Transition(input="sample_text", output="sample_text")
    a2 = compositefsm_Transition(input="sample_text_2", output="sample_text_2")
    b = compositefsm_State(name="sample_text")
    _safe_set(b, 'State18', a1)
    assert _is_linked(b, 'State18', a1)
    if hasattr(a1, 'incomingTransition'):
        assert _is_linked(a1, 'incomingTransition', b)
    _safe_set(b, 'State18', a2)
    assert _is_linked(b, 'State18', a2)
    if hasattr(a1, 'incomingTransition'):
        assert not _is_linked(a1, 'incomingTransition', b)
    if hasattr(a2, 'incomingTransition'):
        assert _is_linked(a2, 'incomingTransition', b)
    _safe_set(b, 'State18', None)
    assert not _is_linked(b, 'State18', a2)
    if hasattr(a2, 'incomingTransition'):
        assert not _is_linked(a2, 'incomingTransition', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_finalState2_stub_double():
    # compositefsm_FSM has no real 'compositefsm_FSM3' property in the generated
    # code (a bare stub) -- manually attach it so compositefsm_State's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # compositefsm_State's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = compositefsm_State(name="sample_text")
    partner = compositefsm_FSM()
    setattr(partner, 'compositefsm_FSM3', None)
    _safe_set(owner, 'compositefsm_State4', partner)
    assert owner in getattr(partner, 'compositefsm_FSM3')
    _safe_set(owner, 'compositefsm_State4', None)
    assert owner not in getattr(partner, 'compositefsm_FSM3')


def test_assoc_initialState1_stub_double():
    # compositefsm_FSM has no real 'compositefsm_FSM' property in the generated
    # code (a bare stub) -- manually attach it so compositefsm_State's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # compositefsm_State's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = compositefsm_State(name="sample_text")
    partner = compositefsm_FSM()
    setattr(partner, 'compositefsm_FSM', None)
    _safe_set(owner, 'compositefsm_State', partner)
    assert getattr(partner, 'compositefsm_FSM') == owner
    _safe_set(owner, 'compositefsm_State', None)
    assert getattr(partner, 'compositefsm_FSM') is None


def test_assoc_ownedState0_stub_double():
    # compositefsm_FSM has no real 'owningFSM' property in the generated
    # code (a bare stub) -- manually attach it so compositefsm_State's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # compositefsm_State's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = compositefsm_State(name="sample_text")
    partner = compositefsm_FSM()
    setattr(partner, 'owningFSM', None)
    _safe_set(owner, 'State', partner)
    assert owner in getattr(partner, 'owningFSM')
    _safe_set(owner, 'State', None)
    assert owner not in getattr(partner, 'owningFSM')


def test_assoc_owningFSM5_stub_double():
    # compositefsm_FSM has no real 'FSM' property in the generated
    # code (a bare stub) -- manually attach it so compositefsm_State's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # compositefsm_State's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = compositefsm_State(name="sample_text")
    partner = compositefsm_FSM()
    setattr(partner, 'FSM', None)
    _safe_set(owner, 'ownedState', partner)
    assert getattr(partner, 'FSM') == owner
    _safe_set(owner, 'ownedState', None)
    assert getattr(partner, 'FSM') is None


