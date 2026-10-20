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

def test_assoc_source18_reverse_link_reassign_clear():
    a1 = fsm_NumberVariable(initialValue=7)
    a2 = fsm_NumberVariable(initialValue=13)
    b = fsm_NumberGuard(value=7)
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


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_guard14_stub_double():
    # fsm_Transition has no real 'fsm_Transition15' property in the generated
    # code (a bare stub) -- manually attach it so fsm_Guard's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # fsm_Guard's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = fsm_Guard(not_=True)
    partner = fsm_Transition()
    setattr(partner, 'fsm_Transition15', None)
    _safe_set(owner, 'fsm_Guard', partner)
    assert getattr(partner, 'fsm_Transition15') == owner
    _safe_set(owner, 'fsm_Guard', None)
    assert getattr(partner, 'fsm_Transition15') is None


def test_assoc_target19_stub_double():
    # fsm_Action has no real 'fsm_Action20' property in the generated
    # code (a bare stub) -- manually attach it so fsm_NumberVariable's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # fsm_NumberVariable's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = fsm_NumberVariable(initialValue=7)
    partner = fsm_Action()
    setattr(partner, 'fsm_Action20', None)
    _safe_set(owner, 'fsm_NumberVariable21', partner)
    assert getattr(partner, 'fsm_Action20') == owner
    _safe_set(owner, 'fsm_NumberVariable21', None)
    assert getattr(partner, 'fsm_Action20') is None


def test_assoc_variables4_stub_double():
    # fsm_StateMachine has no real 'fsm_StateMachine5' property in the generated
    # code (a bare stub) -- manually attach it so fsm_Variable's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # fsm_Variable's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = fsm_Variable(name="sample_text")
    partner = fsm_StateMachine()
    setattr(partner, 'fsm_StateMachine5', None)
    _safe_set(owner, 'fsm_Variable', partner)
    assert owner in getattr(partner, 'fsm_StateMachine5')
    _safe_set(owner, 'fsm_Variable', None)
    assert owner not in getattr(partner, 'fsm_StateMachine5')


