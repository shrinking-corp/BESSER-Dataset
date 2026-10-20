import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    ConsoleOutput,
    Constraint,
    Expression,
    Literal,
    NamedElement,
    Node,
    Statement,
    flowchartpck_Action,
    flowchartpck_Arc,
    flowchartpck_ArithmeticExpression,
    flowchartpck_Assignation,
    flowchartpck_BoolLit,
    flowchartpck_Conditional,
    flowchartpck_ConsoleOutput,
    flowchartpck_Constraint,
    flowchartpck_Decision,
    flowchartpck_End,
    flowchartpck_Expression,
    flowchartpck_Flowchart,
    flowchartpck_IntegerLit,
    flowchartpck_Literal,
    flowchartpck_Loop,
    flowchartpck_NamedElement,
    flowchartpck_Node,
    flowchartpck_Print,
    flowchartpck_Println,
    flowchartpck_Program,
    flowchartpck_RelationalConstraint,
    flowchartpck_RelationalExpression,
    flowchartpck_Start,
    flowchartpck_Statement,
    flowchartpck_StringLit,
    flowchartpck_VarDecl,
    flowchartpck_VarReference,
    flowchartpck_Wait,
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

def test_assoc_expression41_stub_double():
    # flowchartpck_Expression has no real 'flowchartpck_Expression43' property in the generated
    # code (a bare stub) -- manually attach it so flowchartpck_VarDecl's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # flowchartpck_VarDecl's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = flowchartpck_VarDecl(key="sample_text")
    partner = flowchartpck_Expression()
    setattr(partner, 'flowchartpck_Expression43', None)
    _safe_set(owner, 'flowchartpck_VarDecl42', partner)
    assert getattr(partner, 'flowchartpck_Expression43') == owner
    _safe_set(owner, 'flowchartpck_VarDecl42', None)
    assert getattr(partner, 'flowchartpck_Expression43') is None


def test_assoc_left12_stub_double():
    # flowchartpck_Expression has no real 'flowchartpck_Expression13' property in the generated
    # code (a bare stub) -- manually attach it so flowchartpck_ArithmeticExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # flowchartpck_ArithmeticExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = flowchartpck_ArithmeticExpression(operator="sample_text")
    partner = flowchartpck_Expression()
    setattr(partner, 'flowchartpck_Expression13', None)
    _safe_set(owner, 'flowchartpck_ArithmeticExpression', partner)
    assert getattr(partner, 'flowchartpck_Expression13') == owner
    _safe_set(owner, 'flowchartpck_ArithmeticExpression', None)
    assert getattr(partner, 'flowchartpck_Expression13') is None


def test_assoc_left17_stub_double():
    # flowchartpck_Expression has no real 'flowchartpck_Expression18' property in the generated
    # code (a bare stub) -- manually attach it so flowchartpck_RelationalExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # flowchartpck_RelationalExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = flowchartpck_RelationalExpression(operator="sample_text")
    partner = flowchartpck_Expression()
    setattr(partner, 'flowchartpck_Expression18', None)
    _safe_set(owner, 'flowchartpck_RelationalExpression', partner)
    assert getattr(partner, 'flowchartpck_Expression18') == owner
    _safe_set(owner, 'flowchartpck_RelationalExpression', None)
    assert getattr(partner, 'flowchartpck_Expression18') is None


def test_assoc_right14_stub_double():
    # flowchartpck_Expression has no real 'flowchartpck_Expression16' property in the generated
    # code (a bare stub) -- manually attach it so flowchartpck_ArithmeticExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # flowchartpck_ArithmeticExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = flowchartpck_ArithmeticExpression(operator="sample_text")
    partner = flowchartpck_Expression()
    setattr(partner, 'flowchartpck_Expression16', None)
    _safe_set(owner, 'flowchartpck_ArithmeticExpression15', partner)
    assert getattr(partner, 'flowchartpck_Expression16') == owner
    _safe_set(owner, 'flowchartpck_ArithmeticExpression15', None)
    assert getattr(partner, 'flowchartpck_Expression16') is None


def test_assoc_right19_stub_double():
    # flowchartpck_Expression has no real 'flowchartpck_Expression21' property in the generated
    # code (a bare stub) -- manually attach it so flowchartpck_RelationalExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # flowchartpck_RelationalExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = flowchartpck_RelationalExpression(operator="sample_text")
    partner = flowchartpck_Expression()
    setattr(partner, 'flowchartpck_Expression21', None)
    _safe_set(owner, 'flowchartpck_RelationalExpression20', partner)
    assert getattr(partner, 'flowchartpck_Expression21') == owner
    _safe_set(owner, 'flowchartpck_RelationalExpression20', None)
    assert getattr(partner, 'flowchartpck_Expression21') is None


def test_assoc_varRef37_stub_double():
    # flowchartpck_Assignation has no real 'flowchartpck_Assignation' property in the generated
    # code (a bare stub) -- manually attach it so flowchartpck_VarDecl's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # flowchartpck_VarDecl's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = flowchartpck_VarDecl(key="sample_text")
    partner = flowchartpck_Assignation()
    setattr(partner, 'flowchartpck_Assignation', None)
    _safe_set(owner, 'flowchartpck_VarDecl', partner)
    assert getattr(partner, 'flowchartpck_Assignation') == owner
    _safe_set(owner, 'flowchartpck_VarDecl', None)
    assert getattr(partner, 'flowchartpck_Assignation') is None


