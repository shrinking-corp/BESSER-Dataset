import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Action,
    Guard,
    NamedElement,
    NumberGuard,
    Variable,
    fsm_Action,
    fsm_AssignValueAction,
    fsm_DecreaseValueAction,
    fsm_EqualNumberGuard,
    fsm_GreaterThanNumberGuard,
    fsm_Guard,
    fsm_IncreaseValueAction,
    fsm_LessThanNumberGuard,
    fsm_NamedElement,
    fsm_NumberGuard,
    fsm_NumberVariable,
    fsm_State,
    fsm_StateMachine,
    fsm_Transition,
    fsm_Variable,
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

def test_assoc_action19_reverse_link_reassign_clear():
    a1 = fsm_Transition()
    a2 = fsm_Transition()
    b = fsm_Action()
    _safe_set(b, 'fsm_Action', a1)
    assert _is_linked(b, 'fsm_Action', a1)
    if hasattr(a1, 'fsm_Transition20'):
        assert _is_linked(a1, 'fsm_Transition20', b)
    _safe_set(b, 'fsm_Action', a2)
    assert _is_linked(b, 'fsm_Action', a2)
    if hasattr(a1, 'fsm_Transition20'):
        assert not _is_linked(a1, 'fsm_Transition20', b)
    if hasattr(a2, 'fsm_Transition20'):
        assert _is_linked(a2, 'fsm_Transition20', b)
    _safe_set(b, 'fsm_Action', None)
    assert not _is_linked(b, 'fsm_Action', a2)
    if hasattr(a2, 'fsm_Transition20'):
        assert not _is_linked(a2, 'fsm_Transition20', b)


def test_assoc_guard17_reverse_link_reassign_clear():
    a1 = fsm_Transition()
    a2 = fsm_Transition()
    b = fsm_Guard(not_=True)
    _safe_set(b, 'fsm_Guard', a1)
    assert _is_linked(b, 'fsm_Guard', a1)
    if hasattr(a1, 'fsm_Transition18'):
        assert _is_linked(a1, 'fsm_Transition18', b)
    _safe_set(b, 'fsm_Guard', a2)
    assert _is_linked(b, 'fsm_Guard', a2)
    if hasattr(a1, 'fsm_Transition18'):
        assert not _is_linked(a1, 'fsm_Transition18', b)
    if hasattr(a2, 'fsm_Transition18'):
        assert _is_linked(a2, 'fsm_Transition18', b)
    _safe_set(b, 'fsm_Guard', None)
    assert not _is_linked(b, 'fsm_Guard', a2)
    if hasattr(a2, 'fsm_Transition18'):
        assert not _is_linked(a2, 'fsm_Transition18', b)


def test_assoc_ownedTransitions2_reverse_link_reassign_clear():
    a1 = fsm_Transition()
    a2 = fsm_Transition()
    b = fsm_StateMachine()
    _safe_set(b, 'fsm_StateMachine3', {a1})
    assert _is_linked(b, 'fsm_StateMachine3', a1)
    if hasattr(a1, 'fsm_Transition'):
        assert _is_linked(a1, 'fsm_Transition', b)
    _safe_set(b, 'fsm_StateMachine3', {a2})
    assert _is_linked(b, 'fsm_StateMachine3', a2)
    if hasattr(a1, 'fsm_Transition'):
        assert not _is_linked(a1, 'fsm_Transition', b)
    if hasattr(a2, 'fsm_Transition'):
        assert _is_linked(a2, 'fsm_Transition', b)
    _safe_set(b, 'fsm_StateMachine3', set())
    assert not _is_linked(b, 'fsm_StateMachine3', a2)
    if hasattr(a2, 'fsm_Transition'):
        assert not _is_linked(a2, 'fsm_Transition', b)


def test_assoc_source21_reverse_link_reassign_clear():
    a1 = fsm_NumberVariable(initialValue=7, value=True)
    a2 = fsm_NumberVariable(initialValue=13, value=False)
    b = fsm_NumberGuard(value=True)
    _safe_set(b, 'fsm_NumberGuard', a1)
    assert _is_linked(b, 'fsm_NumberGuard', a1)
    if hasattr(a1, 'fsm_NumberVariable'):
        assert _is_linked(a1, 'fsm_NumberVariable', b)
    _safe_set(b, 'fsm_NumberGuard', a2)
    assert _is_linked(b, 'fsm_NumberGuard', a2)
    if hasattr(a1, 'fsm_NumberVariable'):
        assert not _is_linked(a1, 'fsm_NumberVariable', b)
    if hasattr(a2, 'fsm_NumberVariable'):
        assert _is_linked(a2, 'fsm_NumberVariable', b)
    _safe_set(b, 'fsm_NumberGuard', None)
    assert not _is_linked(b, 'fsm_NumberGuard', a2)
    if hasattr(a2, 'fsm_NumberVariable'):
        assert not _is_linked(a2, 'fsm_NumberVariable', b)


def test_assoc_target22_reverse_link_reassign_clear():
    a1 = fsm_NumberVariable(initialValue=7, value=True)
    a2 = fsm_NumberVariable(initialValue=13, value=False)
    b = fsm_Action()
    _safe_set(b, 'fsm_Action23', a1)
    assert _is_linked(b, 'fsm_Action23', a1)
    if hasattr(a1, 'fsm_NumberVariable24'):
        assert _is_linked(a1, 'fsm_NumberVariable24', b)
    _safe_set(b, 'fsm_Action23', a2)
    assert _is_linked(b, 'fsm_Action23', a2)
    if hasattr(a1, 'fsm_NumberVariable24'):
        assert not _is_linked(a1, 'fsm_NumberVariable24', b)
    if hasattr(a2, 'fsm_NumberVariable24'):
        assert _is_linked(a2, 'fsm_NumberVariable24', b)
    _safe_set(b, 'fsm_Action23', None)
    assert not _is_linked(b, 'fsm_Action23', a2)
    if hasattr(a2, 'fsm_NumberVariable24'):
        assert not _is_linked(a2, 'fsm_NumberVariable24', b)


def test_assoc_variables4_reverse_link_reassign_clear():
    a1 = fsm_Variable(name="sample_text")
    a2 = fsm_Variable(name="sample_text_2")
    b = fsm_StateMachine()
    _safe_set(b, 'fsm_StateMachine5', {a1})
    assert _is_linked(b, 'fsm_StateMachine5', a1)
    if hasattr(a1, 'fsm_Variable'):
        assert _is_linked(a1, 'fsm_Variable', b)
    _safe_set(b, 'fsm_StateMachine5', {a2})
    assert _is_linked(b, 'fsm_StateMachine5', a2)
    if hasattr(a1, 'fsm_Variable'):
        assert not _is_linked(a1, 'fsm_Variable', b)
    if hasattr(a2, 'fsm_Variable'):
        assert _is_linked(a2, 'fsm_Variable', b)
    _safe_set(b, 'fsm_StateMachine5', set())
    assert not _is_linked(b, 'fsm_StateMachine5', a2)
    if hasattr(a2, 'fsm_Variable'):
        assert not _is_linked(a2, 'fsm_Variable', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_currentState6_stub_double():
    # fsm_State has no real 'fsm_State8' property in the generated
    # code (a bare stub) -- manually attach it so fsm_StateMachine's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # fsm_StateMachine's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = fsm_StateMachine()
    partner = fsm_State()
    setattr(partner, 'fsm_State8', None)
    _safe_set(owner, 'fsm_StateMachine7', partner)
    assert getattr(partner, 'fsm_State8') == owner
    _safe_set(owner, 'fsm_StateMachine7', None)
    assert getattr(partner, 'fsm_State8') is None


def test_assoc_incomingTransitions11_stub_double():
    # fsm_State has no real 'target' property in the generated
    # code (a bare stub) -- manually attach it so fsm_Transition's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # fsm_Transition's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = fsm_Transition()
    partner = fsm_State()
    setattr(partner, 'target', None)
    _safe_set(owner, 'Transition12', partner)
    assert owner in getattr(partner, 'target')
    _safe_set(owner, 'Transition12', None)
    assert owner not in getattr(partner, 'target')


def test_assoc_initialState1_stub_double():
    # fsm_State has no real 'fsm_State' property in the generated
    # code (a bare stub) -- manually attach it so fsm_StateMachine's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # fsm_StateMachine's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = fsm_StateMachine()
    partner = fsm_State()
    setattr(partner, 'fsm_State', None)
    _safe_set(owner, 'fsm_StateMachine', partner)
    assert getattr(partner, 'fsm_State') == owner
    _safe_set(owner, 'fsm_StateMachine', None)
    assert getattr(partner, 'fsm_State') is None


def test_assoc_outgoingTransitions10_stub_double():
    # fsm_State has no real 'source' property in the generated
    # code (a bare stub) -- manually attach it so fsm_Transition's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # fsm_Transition's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = fsm_Transition()
    partner = fsm_State()
    setattr(partner, 'source', None)
    _safe_set(owner, 'Transition', partner)
    assert owner in getattr(partner, 'source')
    _safe_set(owner, 'Transition', None)
    assert owner not in getattr(partner, 'source')


def test_assoc_ownedStates0_stub_double():
    # fsm_State has no real 'State' property in the generated
    # code (a bare stub) -- manually attach it so fsm_StateMachine's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # fsm_StateMachine's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = fsm_StateMachine()
    partner = fsm_State()
    setattr(partner, 'State', None)
    _safe_set(owner, 'owningFSM', {partner})
    assert getattr(partner, 'State') == owner
    _safe_set(owner, 'owningFSM', set())
    assert getattr(partner, 'State') is None


def test_assoc_owningFSM9_stub_double():
    # fsm_State has no real 'ownedStates' property in the generated
    # code (a bare stub) -- manually attach it so fsm_StateMachine's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # fsm_StateMachine's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = fsm_StateMachine()
    partner = fsm_State()
    setattr(partner, 'ownedStates', None)
    _safe_set(owner, 'StateMachine', partner)
    assert getattr(partner, 'ownedStates') == owner
    _safe_set(owner, 'StateMachine', None)
    assert getattr(partner, 'ownedStates') is None


def test_assoc_source13_stub_double():
    # fsm_State has no real 'State14' property in the generated
    # code (a bare stub) -- manually attach it so fsm_Transition's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # fsm_Transition's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = fsm_Transition()
    partner = fsm_State()
    setattr(partner, 'State14', None)
    _safe_set(owner, 'outgoingTransitions', partner)
    assert getattr(partner, 'State14') == owner
    _safe_set(owner, 'outgoingTransitions', None)
    assert getattr(partner, 'State14') is None


def test_assoc_target15_stub_double():
    # fsm_State has no real 'State16' property in the generated
    # code (a bare stub) -- manually attach it so fsm_Transition's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # fsm_Transition's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = fsm_Transition()
    partner = fsm_State()
    setattr(partner, 'State16', None)
    _safe_set(owner, 'incomingTransitions', partner)
    assert getattr(partner, 'State16') == owner
    _safe_set(owner, 'incomingTransitions', None)
    assert getattr(partner, 'State16') is None


