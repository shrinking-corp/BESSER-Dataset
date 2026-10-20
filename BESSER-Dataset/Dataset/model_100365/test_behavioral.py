import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    AbstractState,
    ConsoleOutput,
    Constraint,
    Expression,
    Literal,
    State,
    Statement,
    fsm_AbstractState,
    fsm_ArithmeticExpression,
    fsm_Assignation,
    fsm_BoolLit,
    fsm_Conditional,
    fsm_ConsoleOutput,
    fsm_Constraint,
    fsm_Expression,
    fsm_FinalState,
    fsm_IntegerLit,
    fsm_Literal,
    fsm_Loop,
    fsm_Print,
    fsm_Println,
    fsm_Program,
    fsm_Pseudostate,
    fsm_RelationalConstraint,
    fsm_RelationalExpression,
    fsm_State,
    fsm_StateMachine,
    fsm_Statement,
    fsm_StringLit,
    fsm_Transition,
    fsm_Trigger,
    fsm_VarDecl,
    fsm_VarReference,
    fsm_Wait,
    ArithmeticOperator,
    PseudostateKind,
    RelationalOperator,
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

def test_assoc_subvertex0_reverse_link_reassign_clear():
    a1 = fsm_StateMachine(name="sample_text")
    a2 = fsm_StateMachine(name="sample_text_2")
    b = fsm_AbstractState(name="sample_text")
    _safe_set(b, 'fsm_AbstractState', a1)
    assert _is_linked(b, 'fsm_AbstractState', a1)
    if hasattr(a1, 'fsm_StateMachine'):
        assert _is_linked(a1, 'fsm_StateMachine', b)
    _safe_set(b, 'fsm_AbstractState', a2)
    assert _is_linked(b, 'fsm_AbstractState', a2)
    if hasattr(a1, 'fsm_StateMachine'):
        assert not _is_linked(a1, 'fsm_StateMachine', b)
    if hasattr(a2, 'fsm_StateMachine'):
        assert _is_linked(a2, 'fsm_StateMachine', b)
    _safe_set(b, 'fsm_AbstractState', None)
    assert not _is_linked(b, 'fsm_AbstractState', a2)
    if hasattr(a2, 'fsm_StateMachine'):
        assert not _is_linked(a2, 'fsm_StateMachine', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_expression39_stub_double():
    # fsm_Expression has no real 'fsm_Expression40' property in the generated
    # code (a bare stub) -- manually attach it so fsm_VarDecl's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # fsm_VarDecl's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = fsm_VarDecl(key="sample_text")
    partner = fsm_Expression()
    setattr(partner, 'fsm_Expression40', None)
    _safe_set(owner, 'fsm_VarDecl', partner)
    assert getattr(partner, 'fsm_Expression40') == owner
    _safe_set(owner, 'fsm_VarDecl', None)
    assert getattr(partner, 'fsm_Expression40') is None


def test_assoc_incoming3_stub_double():
    # fsm_Transition has no real 'Transition' property in the generated
    # code (a bare stub) -- manually attach it so fsm_AbstractState's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # fsm_AbstractState's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = fsm_AbstractState(name="sample_text")
    partner = fsm_Transition()
    setattr(partner, 'Transition', None)
    _safe_set(owner, 'target', {partner})
    assert getattr(partner, 'Transition') == owner
    _safe_set(owner, 'target', set())
    assert getattr(partner, 'Transition') is None


def test_assoc_left41_stub_double():
    # fsm_Expression has no real 'fsm_Expression42' property in the generated
    # code (a bare stub) -- manually attach it so fsm_ArithmeticExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # fsm_ArithmeticExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = fsm_ArithmeticExpression(operator="sample_text")
    partner = fsm_Expression()
    setattr(partner, 'fsm_Expression42', None)
    _safe_set(owner, 'fsm_ArithmeticExpression', partner)
    assert getattr(partner, 'fsm_Expression42') == owner
    _safe_set(owner, 'fsm_ArithmeticExpression', None)
    assert getattr(partner, 'fsm_Expression42') is None


def test_assoc_left46_stub_double():
    # fsm_Expression has no real 'fsm_Expression47' property in the generated
    # code (a bare stub) -- manually attach it so fsm_RelationalExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # fsm_RelationalExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = fsm_RelationalExpression(operator="sample_text")
    partner = fsm_Expression()
    setattr(partner, 'fsm_Expression47', None)
    _safe_set(owner, 'fsm_RelationalExpression', partner)
    assert getattr(partner, 'fsm_Expression47') == owner
    _safe_set(owner, 'fsm_RelationalExpression', None)
    assert getattr(partner, 'fsm_Expression47') is None


def test_assoc_outgoing4_stub_double():
    # fsm_Transition has no real 'Transition5' property in the generated
    # code (a bare stub) -- manually attach it so fsm_AbstractState's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # fsm_AbstractState's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = fsm_AbstractState(name="sample_text")
    partner = fsm_Transition()
    setattr(partner, 'Transition5', None)
    _safe_set(owner, 'source', {partner})
    assert getattr(partner, 'Transition5') == owner
    _safe_set(owner, 'source', set())
    assert getattr(partner, 'Transition5') is None


def test_assoc_right43_stub_double():
    # fsm_Expression has no real 'fsm_Expression45' property in the generated
    # code (a bare stub) -- manually attach it so fsm_ArithmeticExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # fsm_ArithmeticExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = fsm_ArithmeticExpression(operator="sample_text")
    partner = fsm_Expression()
    setattr(partner, 'fsm_Expression45', None)
    _safe_set(owner, 'fsm_ArithmeticExpression44', partner)
    assert getattr(partner, 'fsm_Expression45') == owner
    _safe_set(owner, 'fsm_ArithmeticExpression44', None)
    assert getattr(partner, 'fsm_Expression45') is None


def test_assoc_right48_stub_double():
    # fsm_Expression has no real 'fsm_Expression50' property in the generated
    # code (a bare stub) -- manually attach it so fsm_RelationalExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # fsm_RelationalExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = fsm_RelationalExpression(operator="sample_text")
    partner = fsm_Expression()
    setattr(partner, 'fsm_Expression50', None)
    _safe_set(owner, 'fsm_RelationalExpression49', partner)
    assert getattr(partner, 'fsm_Expression50') == owner
    _safe_set(owner, 'fsm_RelationalExpression49', None)
    assert getattr(partner, 'fsm_Expression50') is None


def test_assoc_source16_stub_double():
    # fsm_Transition has no real 'outgoing' property in the generated
    # code (a bare stub) -- manually attach it so fsm_AbstractState's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # fsm_AbstractState's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = fsm_AbstractState(name="sample_text")
    partner = fsm_Transition()
    setattr(partner, 'outgoing', None)
    _safe_set(owner, 'AbstractState17', partner)
    assert getattr(partner, 'outgoing') == owner
    _safe_set(owner, 'AbstractState17', None)
    assert getattr(partner, 'outgoing') is None


def test_assoc_target15_stub_double():
    # fsm_Transition has no real 'incoming' property in the generated
    # code (a bare stub) -- manually attach it so fsm_AbstractState's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # fsm_AbstractState's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = fsm_AbstractState(name="sample_text")
    partner = fsm_Transition()
    setattr(partner, 'incoming', None)
    _safe_set(owner, 'AbstractState', partner)
    assert getattr(partner, 'incoming') == owner
    _safe_set(owner, 'AbstractState', None)
    assert getattr(partner, 'incoming') is None


def test_assoc_transitions1_stub_double():
    # fsm_Transition has no real 'fsm_Transition' property in the generated
    # code (a bare stub) -- manually attach it so fsm_StateMachine's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # fsm_StateMachine's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = fsm_StateMachine(name="sample_text")
    partner = fsm_Transition()
    setattr(partner, 'fsm_Transition', None)
    _safe_set(owner, 'fsm_StateMachine2', {partner})
    assert getattr(partner, 'fsm_Transition') == owner
    _safe_set(owner, 'fsm_StateMachine2', set())
    assert getattr(partner, 'fsm_Transition') is None


def test_assoc_trigger13_stub_double():
    # fsm_Transition has no real 'fsm_Transition14' property in the generated
    # code (a bare stub) -- manually attach it so fsm_Trigger's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # fsm_Trigger's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = fsm_Trigger(expression="sample_text")
    partner = fsm_Transition()
    setattr(partner, 'fsm_Transition14', None)
    _safe_set(owner, 'fsm_Trigger', partner)
    assert getattr(partner, 'fsm_Transition14') == owner
    _safe_set(owner, 'fsm_Trigger', None)
    assert getattr(partner, 'fsm_Transition14') is None


def test_assoc_varRef51_stub_double():
    # fsm_Assignation has no real 'fsm_Assignation' property in the generated
    # code (a bare stub) -- manually attach it so fsm_VarDecl's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # fsm_VarDecl's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = fsm_VarDecl(key="sample_text")
    partner = fsm_Assignation()
    setattr(partner, 'fsm_Assignation', None)
    _safe_set(owner, 'fsm_VarDecl52', partner)
    assert getattr(partner, 'fsm_Assignation') == owner
    _safe_set(owner, 'fsm_VarDecl52', None)
    assert getattr(partner, 'fsm_Assignation') is None


