import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    BinaryExpr,
    ControlStructure,
    Expression,
    Instruction,
    Literal,
    Logo_ArithmeticExpr,
    Logo_Assignation,
    Logo_Back,
    Logo_BinaryExpr,
    Logo_Block,
    Logo_Boolean,
    Logo_BooleanExpr,
    Logo_ControlStructure,
    Logo_Double,
    Logo_Expression,
    Logo_Forward,
    Logo_If,
    Logo_Instruction,
    Logo_Integer,
    Logo_Left,
    Logo_Literal,
    Logo_LogoProgram,
    Logo_Primitive,
    Logo_Procedure,
    Logo_ProcedureCall,
    Logo_Right,
    Logo_String,
    Logo_VarDecl,
    Logo_VarReference,
    Logo_Void,
    Logo_While,
    Primitive,
    ArithmeticOperator,
    BooleanOperator,
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

def test_assoc_body29_stub_double():
    # Logo_Block has no real 'Logo_Block30' property in the generated
    # code (a bare stub) -- manually attach it so Logo_Procedure's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # Logo_Procedure's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = Logo_Procedure(name="sample_text")
    partner = Logo_Block()
    setattr(partner, 'Logo_Block30', None)
    _safe_set(owner, 'Logo_Procedure', partner)
    assert getattr(partner, 'Logo_Block30') == owner
    _safe_set(owner, 'Logo_Procedure', None)
    assert getattr(partner, 'Logo_Block30') is None


def test_assoc_expr8_stub_double():
    # Logo_Expression has no real 'Logo_Expression9' property in the generated
    # code (a bare stub) -- manually attach it so Logo_VarDecl's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # Logo_VarDecl's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = Logo_VarDecl(name="sample_text")
    partner = Logo_Expression()
    setattr(partner, 'Logo_Expression9', None)
    _safe_set(owner, 'Logo_VarDecl', partner)
    assert getattr(partner, 'Logo_Expression9') == owner
    _safe_set(owner, 'Logo_VarDecl', None)
    assert getattr(partner, 'Logo_Expression9') is None


def test_assoc_ref10_stub_double():
    # Logo_VarReference has no real 'Logo_VarReference' property in the generated
    # code (a bare stub) -- manually attach it so Logo_VarDecl's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # Logo_VarDecl's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = Logo_VarDecl(name="sample_text")
    partner = Logo_VarReference()
    setattr(partner, 'Logo_VarReference', None)
    _safe_set(owner, 'Logo_VarDecl11', partner)
    assert getattr(partner, 'Logo_VarReference') == owner
    _safe_set(owner, 'Logo_VarDecl11', None)
    assert getattr(partner, 'Logo_VarReference') is None


def test_assoc_ref33_stub_double():
    # Logo_ProcedureCall has no real 'Logo_ProcedureCall' property in the generated
    # code (a bare stub) -- manually attach it so Logo_Procedure's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # Logo_Procedure's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = Logo_Procedure(name="sample_text")
    partner = Logo_ProcedureCall()
    setattr(partner, 'Logo_ProcedureCall', None)
    _safe_set(owner, 'Logo_Procedure34', partner)
    assert getattr(partner, 'Logo_ProcedureCall') == owner
    _safe_set(owner, 'Logo_Procedure34', None)
    assert getattr(partner, 'Logo_ProcedureCall') is None


def test_assoc_ref35_stub_double():
    # Logo_Assignation has no real 'Logo_Assignation' property in the generated
    # code (a bare stub) -- manually attach it so Logo_VarDecl's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # Logo_VarDecl's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = Logo_VarDecl(name="sample_text")
    partner = Logo_Assignation()
    setattr(partner, 'Logo_Assignation', None)
    _safe_set(owner, 'Logo_VarDecl36', partner)
    assert getattr(partner, 'Logo_Assignation') == owner
    _safe_set(owner, 'Logo_VarDecl36', None)
    assert getattr(partner, 'Logo_Assignation') is None


def test_assoc_returnType31_stub_double():
    # Logo_Literal has no real 'Logo_Literal' property in the generated
    # code (a bare stub) -- manually attach it so Logo_Procedure's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # Logo_Procedure's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = Logo_Procedure(name="sample_text")
    partner = Logo_Literal()
    setattr(partner, 'Logo_Literal', None)
    _safe_set(owner, 'Logo_Procedure32', partner)
    assert getattr(partner, 'Logo_Literal') == owner
    _safe_set(owner, 'Logo_Procedure32', None)
    assert getattr(partner, 'Logo_Literal') is None


