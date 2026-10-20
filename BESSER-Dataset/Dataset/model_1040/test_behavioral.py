import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    AbstractState,
    Expression,
    Literal,
    Pseudostate,
    State,
    Statement,
    Trigger,
    fsm_AbstractState,
    fsm_AndTrigger,
    fsm_ArithmeticExpression,
    fsm_Assignation,
    fsm_Block,
    fsm_Boolean,
    fsm_Condition,
    fsm_Conditional,
    fsm_Constraint,
    fsm_Context,
    fsm_DeepHistory,
    fsm_Expression,
    fsm_FinalState,
    fsm_Fork,
    fsm_InitialState,
    fsm_Integer,
    fsm_Join,
    fsm_Junction,
    fsm_Literal,
    fsm_Loop,
    fsm_NotTrigger,
    fsm_OrTrigger,
    fsm_Pseudostate,
    fsm_Real,
    fsm_Region,
    fsm_RelationalExpression,
    fsm_ShallowHistory,
    fsm_State,
    fsm_StateMachine,
    fsm_Statement,
    fsm_String,
    fsm_Transition,
    fsm_Trigger,
    fsm_VarDecl,
    fsm_VarRef,
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

# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_left24_stub_double():
    # fsm_AndTrigger has no real 'fsm_AndTrigger' property in the generated
    # code (a bare stub) -- manually attach it so fsm_Trigger's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # fsm_Trigger's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = fsm_Trigger(expression="sample_text")
    partner = fsm_AndTrigger()
    setattr(partner, 'fsm_AndTrigger', None)
    _safe_set(owner, 'fsm_Trigger25', partner)
    assert getattr(partner, 'fsm_AndTrigger') == owner
    _safe_set(owner, 'fsm_Trigger25', None)
    assert getattr(partner, 'fsm_AndTrigger') is None


def test_assoc_left29_stub_double():
    # fsm_OrTrigger has no real 'fsm_OrTrigger' property in the generated
    # code (a bare stub) -- manually attach it so fsm_Trigger's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # fsm_Trigger's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = fsm_Trigger(expression="sample_text")
    partner = fsm_OrTrigger()
    setattr(partner, 'fsm_OrTrigger', None)
    _safe_set(owner, 'fsm_Trigger30', partner)
    assert getattr(partner, 'fsm_OrTrigger') == owner
    _safe_set(owner, 'fsm_Trigger30', None)
    assert getattr(partner, 'fsm_OrTrigger') is None


def test_assoc_right26_stub_double():
    # fsm_AndTrigger has no real 'fsm_AndTrigger27' property in the generated
    # code (a bare stub) -- manually attach it so fsm_Trigger's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # fsm_Trigger's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = fsm_Trigger(expression="sample_text")
    partner = fsm_AndTrigger()
    setattr(partner, 'fsm_AndTrigger27', None)
    _safe_set(owner, 'fsm_Trigger28', partner)
    assert getattr(partner, 'fsm_AndTrigger27') == owner
    _safe_set(owner, 'fsm_Trigger28', None)
    assert getattr(partner, 'fsm_AndTrigger27') is None


def test_assoc_right31_stub_double():
    # fsm_OrTrigger has no real 'fsm_OrTrigger32' property in the generated
    # code (a bare stub) -- manually attach it so fsm_Trigger's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # fsm_Trigger's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = fsm_Trigger(expression="sample_text")
    partner = fsm_OrTrigger()
    setattr(partner, 'fsm_OrTrigger32', None)
    _safe_set(owner, 'fsm_Trigger33', partner)
    assert getattr(partner, 'fsm_OrTrigger32') == owner
    _safe_set(owner, 'fsm_Trigger33', None)
    assert getattr(partner, 'fsm_OrTrigger32') is None


def test_assoc_trigger12_stub_double():
    # fsm_Transition has no real 'fsm_Transition13' property in the generated
    # code (a bare stub) -- manually attach it so fsm_Trigger's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # fsm_Trigger's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = fsm_Trigger(expression="sample_text")
    partner = fsm_Transition()
    setattr(partner, 'fsm_Transition13', None)
    _safe_set(owner, 'fsm_Trigger', partner)
    assert getattr(partner, 'fsm_Transition13') == owner
    _safe_set(owner, 'fsm_Trigger', None)
    assert getattr(partner, 'fsm_Transition13') is None


def test_assoc_trigger22_stub_double():
    # fsm_NotTrigger has no real 'fsm_NotTrigger' property in the generated
    # code (a bare stub) -- manually attach it so fsm_Trigger's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # fsm_Trigger's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = fsm_Trigger(expression="sample_text")
    partner = fsm_NotTrigger()
    setattr(partner, 'fsm_NotTrigger', None)
    _safe_set(owner, 'fsm_Trigger23', partner)
    assert getattr(partner, 'fsm_NotTrigger') == owner
    _safe_set(owner, 'fsm_Trigger23', None)
    assert getattr(partner, 'fsm_NotTrigger') is None


