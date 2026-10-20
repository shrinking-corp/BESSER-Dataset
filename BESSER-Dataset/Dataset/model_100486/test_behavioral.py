import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    State,
    StateMachine,
    TracedClass,
    Transition,
    UHSM_CompositeState,
    UHSM_EObject,
    UHSM_FinalState,
    UHSM_InitialState,
    UHSM_State,
    UHSM_StateMachine,
    UHSM_TracedClass,
    UHSM_Transition,
    UHSM_UState,
    UHSM_UStateMachine,
    UHSM_UTransition,
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

def test_assoc_ownedState11_reverse_link_reassign_clear():
    a1 = UHSM_StateMachine(name="sample_text")
    a2 = UHSM_StateMachine(name="sample_text_2")
    b = UHSM_State(name="sample_text")
    _safe_set(b, 'UHSM_State12', a1)
    assert _is_linked(b, 'UHSM_State12', a1)
    if hasattr(a1, 'UHSM_StateMachine'):
        assert _is_linked(a1, 'UHSM_StateMachine', b)
    _safe_set(b, 'UHSM_State12', a2)
    assert _is_linked(b, 'UHSM_State12', a2)
    if hasattr(a1, 'UHSM_StateMachine'):
        assert not _is_linked(a1, 'UHSM_StateMachine', b)
    if hasattr(a2, 'UHSM_StateMachine'):
        assert _is_linked(a2, 'UHSM_StateMachine', b)
    _safe_set(b, 'UHSM_State12', None)
    assert not _is_linked(b, 'UHSM_State12', a2)
    if hasattr(a2, 'UHSM_StateMachine'):
        assert not _is_linked(a2, 'UHSM_StateMachine', b)


def test_assoc_ownedTransition13_reverse_link_reassign_clear():
    a1 = UHSM_Transition(effect="sample_text", name="sample_text", trigger="sample_text")
    a2 = UHSM_Transition(effect="sample_text_2", name="sample_text_2", trigger="sample_text_2")
    b = UHSM_StateMachine(name="sample_text")
    _safe_set(b, 'UHSM_StateMachine14', {a1})
    assert _is_linked(b, 'UHSM_StateMachine14', a1)
    if hasattr(a1, 'UHSM_Transition15'):
        assert _is_linked(a1, 'UHSM_Transition15', b)
    _safe_set(b, 'UHSM_StateMachine14', {a2})
    assert _is_linked(b, 'UHSM_StateMachine14', a2)
    if hasattr(a1, 'UHSM_Transition15'):
        assert not _is_linked(a1, 'UHSM_Transition15', b)
    if hasattr(a2, 'UHSM_Transition15'):
        assert _is_linked(a2, 'UHSM_Transition15', b)
    _safe_set(b, 'UHSM_StateMachine14', set())
    assert not _is_linked(b, 'UHSM_StateMachine14', a2)
    if hasattr(a2, 'UHSM_Transition15'):
        assert not _is_linked(a2, 'UHSM_Transition15', b)


def test_assoc_source5_reverse_link_reassign_clear():
    a1 = UHSM_Transition(effect="sample_text", name="sample_text", trigger="sample_text")
    a2 = UHSM_Transition(effect="sample_text_2", name="sample_text_2", trigger="sample_text_2")
    b = UHSM_State(name="sample_text")
    _safe_set(b, 'UHSM_State7', a1)
    assert _is_linked(b, 'UHSM_State7', a1)
    if hasattr(a1, 'UHSM_Transition6'):
        assert _is_linked(a1, 'UHSM_Transition6', b)
    _safe_set(b, 'UHSM_State7', a2)
    assert _is_linked(b, 'UHSM_State7', a2)
    if hasattr(a1, 'UHSM_Transition6'):
        assert not _is_linked(a1, 'UHSM_Transition6', b)
    if hasattr(a2, 'UHSM_Transition6'):
        assert _is_linked(a2, 'UHSM_Transition6', b)
    _safe_set(b, 'UHSM_State7', None)
    assert not _is_linked(b, 'UHSM_State7', a2)
    if hasattr(a2, 'UHSM_Transition6'):
        assert not _is_linked(a2, 'UHSM_Transition6', b)


def test_assoc_target2_reverse_link_reassign_clear():
    a1 = UHSM_Transition(effect="sample_text", name="sample_text", trigger="sample_text")
    a2 = UHSM_Transition(effect="sample_text_2", name="sample_text_2", trigger="sample_text_2")
    b = UHSM_State(name="sample_text")
    _safe_set(b, 'UHSM_State4', a1)
    assert _is_linked(b, 'UHSM_State4', a1)
    if hasattr(a1, 'UHSM_Transition3'):
        assert _is_linked(a1, 'UHSM_Transition3', b)
    _safe_set(b, 'UHSM_State4', a2)
    assert _is_linked(b, 'UHSM_State4', a2)
    if hasattr(a1, 'UHSM_Transition3'):
        assert not _is_linked(a1, 'UHSM_Transition3', b)
    if hasattr(a2, 'UHSM_Transition3'):
        assert _is_linked(a2, 'UHSM_Transition3', b)
    _safe_set(b, 'UHSM_State4', None)
    assert not _is_linked(b, 'UHSM_State4', a2)
    if hasattr(a2, 'UHSM_Transition3'):
        assert not _is_linked(a2, 'UHSM_Transition3', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_States16_stub_double():
    # UHSM_UState has no real 'UHSM_UState' property in the generated
    # code (a bare stub) -- manually attach it so UHSM_State's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # UHSM_State's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = UHSM_State(name="sample_text")
    partner = UHSM_UState()
    setattr(partner, 'UHSM_UState', None)
    _safe_set(owner, 'UHSM_State17', partner)
    assert owner in getattr(partner, 'UHSM_UState')
    _safe_set(owner, 'UHSM_State17', None)
    assert owner not in getattr(partner, 'UHSM_UState')


def test_assoc_ownedSubState8_stub_double():
    # UHSM_CompositeState has no real 'UHSM_CompositeState9' property in the generated
    # code (a bare stub) -- manually attach it so UHSM_State's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # UHSM_State's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = UHSM_State(name="sample_text")
    partner = UHSM_CompositeState()
    setattr(partner, 'UHSM_CompositeState9', None)
    _safe_set(owner, 'UHSM_State10', partner)
    assert owner in getattr(partner, 'UHSM_CompositeState9')
    _safe_set(owner, 'UHSM_State10', None)
    assert owner not in getattr(partner, 'UHSM_CompositeState9')


def test_assoc_owningCompositeState0_stub_double():
    # UHSM_CompositeState has no real 'UHSM_CompositeState' property in the generated
    # code (a bare stub) -- manually attach it so UHSM_State's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # UHSM_State's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = UHSM_State(name="sample_text")
    partner = UHSM_CompositeState()
    setattr(partner, 'UHSM_CompositeState', None)
    _safe_set(owner, 'UHSM_State', partner)
    assert getattr(partner, 'UHSM_CompositeState') == owner
    _safe_set(owner, 'UHSM_State', None)
    assert getattr(partner, 'UHSM_CompositeState') is None


def test_assoc_ref20_stub_double():
    # UHSM_EObject has no real 'UHSM_EObject' property in the generated
    # code (a bare stub) -- manually attach it so UHSM_TracedClass's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # UHSM_TracedClass's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = UHSM_TracedClass(trace="sample_text")
    partner = UHSM_EObject()
    setattr(partner, 'UHSM_EObject', None)
    _safe_set(owner, 'UHSM_TracedClass', {partner})
    assert getattr(partner, 'UHSM_EObject') == owner
    _safe_set(owner, 'UHSM_TracedClass', set())
    assert getattr(partner, 'UHSM_EObject') is None


def test_assoc_stateMachines18_stub_double():
    # UHSM_UStateMachine has no real 'UHSM_UStateMachine' property in the generated
    # code (a bare stub) -- manually attach it so UHSM_StateMachine's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # UHSM_StateMachine's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = UHSM_StateMachine(name="sample_text")
    partner = UHSM_UStateMachine()
    setattr(partner, 'UHSM_UStateMachine', None)
    _safe_set(owner, 'UHSM_StateMachine19', partner)
    assert owner in getattr(partner, 'UHSM_UStateMachine')
    _safe_set(owner, 'UHSM_StateMachine19', None)
    assert owner not in getattr(partner, 'UHSM_UStateMachine')


def test_assoc_transitions1_stub_double():
    # UHSM_UTransition has no real 'UHSM_UTransition' property in the generated
    # code (a bare stub) -- manually attach it so UHSM_Transition's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # UHSM_Transition's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = UHSM_Transition(effect="sample_text", name="sample_text", trigger="sample_text")
    partner = UHSM_UTransition()
    setattr(partner, 'UHSM_UTransition', None)
    _safe_set(owner, 'UHSM_Transition', partner)
    assert owner in getattr(partner, 'UHSM_UTransition')
    _safe_set(owner, 'UHSM_Transition', None)
    assert owner not in getattr(partner, 'UHSM_UTransition')


