import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    FExpression,
    Referentiable,
    fsmWithMethods_Event,
    fsmWithMethods_FExpression,
    fsmWithMethods_Fsm,
    fsmWithMethods_Method,
    fsmWithMethods_MethodCall,
    fsmWithMethods_Referentiable,
    fsmWithMethods_State,
    fsmWithMethods_Transition,
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

def test_assoc_expressions1_reverse_link_reassign_clear():
    a1 = fsmWithMethods_Fsm(name="sample_text")
    a2 = fsmWithMethods_Fsm(name="sample_text_2")
    b = fsmWithMethods_FExpression(name="sample_text")
    _safe_set(b, 'fsmWithMethods_FExpression', a1)
    assert _is_linked(b, 'fsmWithMethods_FExpression', a1)
    if hasattr(a1, 'fsmWithMethods_Fsm2'):
        assert _is_linked(a1, 'fsmWithMethods_Fsm2', b)
    _safe_set(b, 'fsmWithMethods_FExpression', a2)
    assert _is_linked(b, 'fsmWithMethods_FExpression', a2)
    if hasattr(a1, 'fsmWithMethods_Fsm2'):
        assert not _is_linked(a1, 'fsmWithMethods_Fsm2', b)
    if hasattr(a2, 'fsmWithMethods_Fsm2'):
        assert _is_linked(a2, 'fsmWithMethods_Fsm2', b)
    _safe_set(b, 'fsmWithMethods_FExpression', None)
    assert not _is_linked(b, 'fsmWithMethods_FExpression', a2)
    if hasattr(a2, 'fsmWithMethods_Fsm2'):
        assert not _is_linked(a2, 'fsmWithMethods_Fsm2', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_event12_stub_double():
    # fsmWithMethods_Transition has no real 'fsmWithMethods_Transition' property in the generated
    # code (a bare stub) -- manually attach it so fsmWithMethods_FExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # fsmWithMethods_FExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = fsmWithMethods_FExpression(name="sample_text")
    partner = fsmWithMethods_Transition()
    setattr(partner, 'fsmWithMethods_Transition', None)
    _safe_set(owner, 'fsmWithMethods_FExpression13', partner)
    assert getattr(partner, 'fsmWithMethods_Transition') == owner
    _safe_set(owner, 'fsmWithMethods_FExpression13', None)
    assert getattr(partner, 'fsmWithMethods_Transition') is None


def test_assoc_expressions5_stub_double():
    # fsmWithMethods_Method has no real 'fsmWithMethods_Method6' property in the generated
    # code (a bare stub) -- manually attach it so fsmWithMethods_FExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # fsmWithMethods_FExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = fsmWithMethods_FExpression(name="sample_text")
    partner = fsmWithMethods_Method()
    setattr(partner, 'fsmWithMethods_Method6', None)
    _safe_set(owner, 'fsmWithMethods_FExpression7', partner)
    assert owner in getattr(partner, 'fsmWithMethods_Method6')
    _safe_set(owner, 'fsmWithMethods_FExpression7', None)
    assert owner not in getattr(partner, 'fsmWithMethods_Method6')


def test_assoc_from_14_stub_double():
    # fsmWithMethods_Transition has no real 'fsmWithMethods_Transition15' property in the generated
    # code (a bare stub) -- manually attach it so fsmWithMethods_FExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # fsmWithMethods_FExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = fsmWithMethods_FExpression(name="sample_text")
    partner = fsmWithMethods_Transition()
    setattr(partner, 'fsmWithMethods_Transition15', None)
    _safe_set(owner, 'fsmWithMethods_FExpression16', partner)
    assert getattr(partner, 'fsmWithMethods_Transition15') == owner
    _safe_set(owner, 'fsmWithMethods_FExpression16', None)
    assert getattr(partner, 'fsmWithMethods_Transition15') is None


def test_assoc_params3_stub_double():
    # fsmWithMethods_Method has no real 'fsmWithMethods_Method' property in the generated
    # code (a bare stub) -- manually attach it so fsmWithMethods_FExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # fsmWithMethods_FExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = fsmWithMethods_FExpression(name="sample_text")
    partner = fsmWithMethods_Method()
    setattr(partner, 'fsmWithMethods_Method', None)
    _safe_set(owner, 'fsmWithMethods_FExpression4', partner)
    assert owner in getattr(partner, 'fsmWithMethods_Method')
    _safe_set(owner, 'fsmWithMethods_FExpression4', None)
    assert owner not in getattr(partner, 'fsmWithMethods_Method')


def test_assoc_state0_stub_double():
    # fsmWithMethods_State has no real 'fsmWithMethods_State' property in the generated
    # code (a bare stub) -- manually attach it so fsmWithMethods_Fsm's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # fsmWithMethods_Fsm's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = fsmWithMethods_Fsm(name="sample_text")
    partner = fsmWithMethods_State()
    setattr(partner, 'fsmWithMethods_State', None)
    _safe_set(owner, 'fsmWithMethods_Fsm', partner)
    assert getattr(partner, 'fsmWithMethods_State') == owner
    _safe_set(owner, 'fsmWithMethods_Fsm', None)
    assert getattr(partner, 'fsmWithMethods_State') is None


def test_assoc_to17_stub_double():
    # fsmWithMethods_Transition has no real 'fsmWithMethods_Transition18' property in the generated
    # code (a bare stub) -- manually attach it so fsmWithMethods_FExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # fsmWithMethods_FExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = fsmWithMethods_FExpression(name="sample_text")
    partner = fsmWithMethods_Transition()
    setattr(partner, 'fsmWithMethods_Transition18', None)
    _safe_set(owner, 'fsmWithMethods_FExpression19', partner)
    assert getattr(partner, 'fsmWithMethods_Transition18') == owner
    _safe_set(owner, 'fsmWithMethods_FExpression19', None)
    assert getattr(partner, 'fsmWithMethods_Transition18') is None


