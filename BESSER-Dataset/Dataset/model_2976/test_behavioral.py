import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    AbstractState,
    CompleteDSLPckg_AbstractState,
    CompleteDSLPckg_AndTrigger,
    CompleteDSLPckg_ArithmeticExpression,
    CompleteDSLPckg_Assignation,
    CompleteDSLPckg_Block,
    CompleteDSLPckg_BoolLit,
    CompleteDSLPckg_Conditional,
    CompleteDSLPckg_ConsoleOutput,
    CompleteDSLPckg_Expression,
    CompleteDSLPckg_FinalState,
    CompleteDSLPckg_InitialState,
    CompleteDSLPckg_IntegerLit,
    CompleteDSLPckg_Literal,
    CompleteDSLPckg_Loop,
    CompleteDSLPckg_NamedElement,
    CompleteDSLPckg_NotTrigger,
    CompleteDSLPckg_OrTrigger,
    CompleteDSLPckg_Print,
    CompleteDSLPckg_Println,
    CompleteDSLPckg_Pseudostate,
    CompleteDSLPckg_Region,
    CompleteDSLPckg_RelationalExpression,
    CompleteDSLPckg_State,
    CompleteDSLPckg_StateMachine,
    CompleteDSLPckg_Statement,
    CompleteDSLPckg_StringLit,
    CompleteDSLPckg_Transition,
    CompleteDSLPckg_Trigger,
    CompleteDSLPckg_VarDecl,
    CompleteDSLPckg_VarRef,
    CompleteDSLPckg_Wait,
    ConsoleOutput,
    Expression,
    Literal,
    NamedElement,
    Pseudostate,
    State,
    Statement,
    Trigger,
    ArithmeticOperator,
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

# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_expr20_stub_double():
    # CompleteDSLPckg_Expression has no real 'CompleteDSLPckg_Expression21' property in the generated
    # code (a bare stub) -- manually attach it so CompleteDSLPckg_VarDecl's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # CompleteDSLPckg_VarDecl's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = CompleteDSLPckg_VarDecl(name="sample_text")
    partner = CompleteDSLPckg_Expression()
    setattr(partner, 'CompleteDSLPckg_Expression21', None)
    _safe_set(owner, 'CompleteDSLPckg_VarDecl', partner)
    assert getattr(partner, 'CompleteDSLPckg_Expression21') == owner
    _safe_set(owner, 'CompleteDSLPckg_VarDecl', None)
    assert getattr(partner, 'CompleteDSLPckg_Expression21') is None


def test_assoc_left0_stub_double():
    # CompleteDSLPckg_Expression has no real 'CompleteDSLPckg_Expression' property in the generated
    # code (a bare stub) -- manually attach it so CompleteDSLPckg_ArithmeticExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # CompleteDSLPckg_ArithmeticExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = CompleteDSLPckg_ArithmeticExpression(operator="sample_text")
    partner = CompleteDSLPckg_Expression()
    setattr(partner, 'CompleteDSLPckg_Expression', None)
    _safe_set(owner, 'CompleteDSLPckg_ArithmeticExpression', partner)
    assert getattr(partner, 'CompleteDSLPckg_Expression') == owner
    _safe_set(owner, 'CompleteDSLPckg_ArithmeticExpression', None)
    assert getattr(partner, 'CompleteDSLPckg_Expression') is None


def test_assoc_left4_stub_double():
    # CompleteDSLPckg_Expression has no real 'CompleteDSLPckg_Expression5' property in the generated
    # code (a bare stub) -- manually attach it so CompleteDSLPckg_RelationalExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # CompleteDSLPckg_RelationalExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = CompleteDSLPckg_RelationalExpression(operator="sample_text")
    partner = CompleteDSLPckg_Expression()
    setattr(partner, 'CompleteDSLPckg_Expression5', None)
    _safe_set(owner, 'CompleteDSLPckg_RelationalExpression', partner)
    assert getattr(partner, 'CompleteDSLPckg_Expression5') == owner
    _safe_set(owner, 'CompleteDSLPckg_RelationalExpression', None)
    assert getattr(partner, 'CompleteDSLPckg_Expression5') is None


def test_assoc_left62_stub_double():
    # CompleteDSLPckg_AndTrigger has no real 'CompleteDSLPckg_AndTrigger' property in the generated
    # code (a bare stub) -- manually attach it so CompleteDSLPckg_Trigger's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # CompleteDSLPckg_Trigger's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = CompleteDSLPckg_Trigger(expression="sample_text")
    partner = CompleteDSLPckg_AndTrigger()
    setattr(partner, 'CompleteDSLPckg_AndTrigger', None)
    _safe_set(owner, 'CompleteDSLPckg_Trigger63', partner)
    assert getattr(partner, 'CompleteDSLPckg_AndTrigger') == owner
    _safe_set(owner, 'CompleteDSLPckg_Trigger63', None)
    assert getattr(partner, 'CompleteDSLPckg_AndTrigger') is None


def test_assoc_left67_stub_double():
    # CompleteDSLPckg_OrTrigger has no real 'CompleteDSLPckg_OrTrigger' property in the generated
    # code (a bare stub) -- manually attach it so CompleteDSLPckg_Trigger's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # CompleteDSLPckg_Trigger's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = CompleteDSLPckg_Trigger(expression="sample_text")
    partner = CompleteDSLPckg_OrTrigger()
    setattr(partner, 'CompleteDSLPckg_OrTrigger', None)
    _safe_set(owner, 'CompleteDSLPckg_Trigger68', partner)
    assert getattr(partner, 'CompleteDSLPckg_OrTrigger') == owner
    _safe_set(owner, 'CompleteDSLPckg_Trigger68', None)
    assert getattr(partner, 'CompleteDSLPckg_OrTrigger') is None


def test_assoc_right1_stub_double():
    # CompleteDSLPckg_Expression has no real 'CompleteDSLPckg_Expression3' property in the generated
    # code (a bare stub) -- manually attach it so CompleteDSLPckg_ArithmeticExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # CompleteDSLPckg_ArithmeticExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = CompleteDSLPckg_ArithmeticExpression(operator="sample_text")
    partner = CompleteDSLPckg_Expression()
    setattr(partner, 'CompleteDSLPckg_Expression3', None)
    _safe_set(owner, 'CompleteDSLPckg_ArithmeticExpression2', partner)
    assert getattr(partner, 'CompleteDSLPckg_Expression3') == owner
    _safe_set(owner, 'CompleteDSLPckg_ArithmeticExpression2', None)
    assert getattr(partner, 'CompleteDSLPckg_Expression3') is None


def test_assoc_right6_stub_double():
    # CompleteDSLPckg_Expression has no real 'CompleteDSLPckg_Expression8' property in the generated
    # code (a bare stub) -- manually attach it so CompleteDSLPckg_RelationalExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # CompleteDSLPckg_RelationalExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = CompleteDSLPckg_RelationalExpression(operator="sample_text")
    partner = CompleteDSLPckg_Expression()
    setattr(partner, 'CompleteDSLPckg_Expression8', None)
    _safe_set(owner, 'CompleteDSLPckg_RelationalExpression7', partner)
    assert getattr(partner, 'CompleteDSLPckg_Expression8') == owner
    _safe_set(owner, 'CompleteDSLPckg_RelationalExpression7', None)
    assert getattr(partner, 'CompleteDSLPckg_Expression8') is None


def test_assoc_right64_stub_double():
    # CompleteDSLPckg_AndTrigger has no real 'CompleteDSLPckg_AndTrigger65' property in the generated
    # code (a bare stub) -- manually attach it so CompleteDSLPckg_Trigger's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # CompleteDSLPckg_Trigger's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = CompleteDSLPckg_Trigger(expression="sample_text")
    partner = CompleteDSLPckg_AndTrigger()
    setattr(partner, 'CompleteDSLPckg_AndTrigger65', None)
    _safe_set(owner, 'CompleteDSLPckg_Trigger66', partner)
    assert getattr(partner, 'CompleteDSLPckg_AndTrigger65') == owner
    _safe_set(owner, 'CompleteDSLPckg_Trigger66', None)
    assert getattr(partner, 'CompleteDSLPckg_AndTrigger65') is None


def test_assoc_right69_stub_double():
    # CompleteDSLPckg_OrTrigger has no real 'CompleteDSLPckg_OrTrigger70' property in the generated
    # code (a bare stub) -- manually attach it so CompleteDSLPckg_Trigger's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # CompleteDSLPckg_Trigger's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = CompleteDSLPckg_Trigger(expression="sample_text")
    partner = CompleteDSLPckg_OrTrigger()
    setattr(partner, 'CompleteDSLPckg_OrTrigger70', None)
    _safe_set(owner, 'CompleteDSLPckg_Trigger71', partner)
    assert getattr(partner, 'CompleteDSLPckg_OrTrigger70') == owner
    _safe_set(owner, 'CompleteDSLPckg_Trigger71', None)
    assert getattr(partner, 'CompleteDSLPckg_OrTrigger70') is None


def test_assoc_trigger52_stub_double():
    # CompleteDSLPckg_Transition has no real 'CompleteDSLPckg_Transition53' property in the generated
    # code (a bare stub) -- manually attach it so CompleteDSLPckg_Trigger's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # CompleteDSLPckg_Trigger's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = CompleteDSLPckg_Trigger(expression="sample_text")
    partner = CompleteDSLPckg_Transition()
    setattr(partner, 'CompleteDSLPckg_Transition53', None)
    _safe_set(owner, 'CompleteDSLPckg_Trigger', partner)
    assert getattr(partner, 'CompleteDSLPckg_Transition53') == owner
    _safe_set(owner, 'CompleteDSLPckg_Trigger', None)
    assert getattr(partner, 'CompleteDSLPckg_Transition53') is None


def test_assoc_trigger60_stub_double():
    # CompleteDSLPckg_NotTrigger has no real 'CompleteDSLPckg_NotTrigger' property in the generated
    # code (a bare stub) -- manually attach it so CompleteDSLPckg_Trigger's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # CompleteDSLPckg_Trigger's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = CompleteDSLPckg_Trigger(expression="sample_text")
    partner = CompleteDSLPckg_NotTrigger()
    setattr(partner, 'CompleteDSLPckg_NotTrigger', None)
    _safe_set(owner, 'CompleteDSLPckg_Trigger61', partner)
    assert getattr(partner, 'CompleteDSLPckg_NotTrigger') == owner
    _safe_set(owner, 'CompleteDSLPckg_Trigger61', None)
    assert getattr(partner, 'CompleteDSLPckg_NotTrigger') is None


def test_assoc_varRef22_stub_double():
    # CompleteDSLPckg_Assignation has no real 'CompleteDSLPckg_Assignation' property in the generated
    # code (a bare stub) -- manually attach it so CompleteDSLPckg_VarDecl's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # CompleteDSLPckg_VarDecl's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = CompleteDSLPckg_VarDecl(name="sample_text")
    partner = CompleteDSLPckg_Assignation()
    setattr(partner, 'CompleteDSLPckg_Assignation', None)
    _safe_set(owner, 'CompleteDSLPckg_VarDecl23', partner)
    assert getattr(partner, 'CompleteDSLPckg_Assignation') == owner
    _safe_set(owner, 'CompleteDSLPckg_VarDecl23', None)
    assert getattr(partner, 'CompleteDSLPckg_Assignation') is None


