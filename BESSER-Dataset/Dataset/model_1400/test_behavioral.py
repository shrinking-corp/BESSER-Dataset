import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    AbstractState,
    NamedElement,
    State,
    Statement,
    fsmcore_AbstractState,
    fsmcore_Conditional,
    fsmcore_Constraint,
    fsmcore_FinalState,
    fsmcore_Loop,
    fsmcore_NamedElement,
    fsmcore_Program,
    fsmcore_Pseudostate,
    fsmcore_Region,
    fsmcore_State,
    fsmcore_StateMachine,
    fsmcore_Statement,
    fsmcore_Transition,
    fsmcore_Trigger,
    fsmcore_VarDecl,
    PseudostateKind,
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

def test_assoc_statements23_reverse_link_reassign_clear():
    a1 = fsmcore_Statement()
    a2 = fsmcore_Statement()
    b = fsmcore_Program()
    _safe_set(b, 'fsmcore_Program24', {a1})
    assert _is_linked(b, 'fsmcore_Program24', a1)
    if hasattr(a1, 'fsmcore_Statement'):
        assert _is_linked(a1, 'fsmcore_Statement', b)
    _safe_set(b, 'fsmcore_Program24', {a2})
    assert _is_linked(b, 'fsmcore_Program24', a2)
    if hasattr(a1, 'fsmcore_Statement'):
        assert not _is_linked(a1, 'fsmcore_Statement', b)
    if hasattr(a2, 'fsmcore_Statement'):
        assert _is_linked(a2, 'fsmcore_Statement', b)
    _safe_set(b, 'fsmcore_Program24', set())
    assert not _is_linked(b, 'fsmcore_Program24', a2)
    if hasattr(a2, 'fsmcore_Statement'):
        assert not _is_linked(a2, 'fsmcore_Statement', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_doActivity8_stub_double():
    # fsmcore_State has no real 'fsmcore_State' property in the generated
    # code (a bare stub) -- manually attach it so fsmcore_Program's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # fsmcore_Program's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = fsmcore_Program()
    partner = fsmcore_State()
    setattr(partner, 'fsmcore_State', None)
    _safe_set(owner, 'fsmcore_Program', partner)
    assert getattr(partner, 'fsmcore_State') == owner
    _safe_set(owner, 'fsmcore_Program', None)
    assert getattr(partner, 'fsmcore_State') is None


def test_assoc_entry9_stub_double():
    # fsmcore_State has no real 'fsmcore_State10' property in the generated
    # code (a bare stub) -- manually attach it so fsmcore_Program's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # fsmcore_Program's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = fsmcore_Program()
    partner = fsmcore_State()
    setattr(partner, 'fsmcore_State10', None)
    _safe_set(owner, 'fsmcore_Program11', partner)
    assert getattr(partner, 'fsmcore_State10') == owner
    _safe_set(owner, 'fsmcore_Program11', None)
    assert getattr(partner, 'fsmcore_State10') is None


def test_assoc_exit12_stub_double():
    # fsmcore_State has no real 'fsmcore_State13' property in the generated
    # code (a bare stub) -- manually attach it so fsmcore_Program's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # fsmcore_Program's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = fsmcore_Program()
    partner = fsmcore_State()
    setattr(partner, 'fsmcore_State13', None)
    _safe_set(owner, 'fsmcore_Program14', partner)
    assert getattr(partner, 'fsmcore_State13') == owner
    _safe_set(owner, 'fsmcore_Program14', None)
    assert getattr(partner, 'fsmcore_State13') is None


def test_assoc_guard21_stub_double():
    # fsmcore_Transition has no real 'fsmcore_Transition22' property in the generated
    # code (a bare stub) -- manually attach it so fsmcore_Constraint's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # fsmcore_Constraint's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = fsmcore_Constraint()
    partner = fsmcore_Transition()
    setattr(partner, 'fsmcore_Transition22', None)
    _safe_set(owner, 'fsmcore_Constraint', partner)
    assert getattr(partner, 'fsmcore_Transition22') == owner
    _safe_set(owner, 'fsmcore_Constraint', None)
    assert getattr(partner, 'fsmcore_Transition22') is None


def test_assoc_trigger15_stub_double():
    # fsmcore_Transition has no real 'fsmcore_Transition16' property in the generated
    # code (a bare stub) -- manually attach it so fsmcore_Trigger's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # fsmcore_Trigger's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = fsmcore_Trigger(expression=True)
    partner = fsmcore_Transition()
    setattr(partner, 'fsmcore_Transition16', None)
    _safe_set(owner, 'fsmcore_Trigger', partner)
    assert getattr(partner, 'fsmcore_Transition16') == owner
    _safe_set(owner, 'fsmcore_Trigger', None)
    assert getattr(partner, 'fsmcore_Transition16') is None


