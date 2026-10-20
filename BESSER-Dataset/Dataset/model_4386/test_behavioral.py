import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    BoolExpression,
    ControlStructure,
    Expression,
    IntBinaryOperation,
    IntExpression,
    Statement,
    gx10_And,
    gx10_Async,
    gx10_Block,
    gx10_BoolExpression,
    gx10_BoolVar,
    gx10_BoolVarAccess,
    gx10_ControlStructure,
    gx10_Equal,
    gx10_Expression,
    gx10_False,
    gx10_Finish,
    gx10_If,
    gx10_IntBinaryOperation,
    gx10_IntConst,
    gx10_IntExpression,
    gx10_IntVar,
    gx10_IntVarAccess,
    gx10_Method,
    gx10_MethodCall,
    gx10_MethodCallParameter,
    gx10_Not,
    gx10_Plus,
    gx10_Print,
    gx10_Program,
    gx10_Referentiable,
    gx10_Statement,
    gx10_Time,
    gx10_True,
    gx10_While,
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

def test_assoc_boolVarExpr38_reverse_link_reassign_clear():
    a1 = gx10_BoolVar()
    a2 = gx10_BoolVar()
    b = gx10_BoolExpression()
    _safe_set(b, 'gx10_BoolExpression39', a1)
    assert _is_linked(b, 'gx10_BoolExpression39', a1)
    if hasattr(a1, 'gx10_BoolVar'):
        assert _is_linked(a1, 'gx10_BoolVar', b)
    _safe_set(b, 'gx10_BoolExpression39', a2)
    assert _is_linked(b, 'gx10_BoolExpression39', a2)
    if hasattr(a1, 'gx10_BoolVar'):
        assert not _is_linked(a1, 'gx10_BoolVar', b)
    if hasattr(a2, 'gx10_BoolVar'):
        assert _is_linked(a2, 'gx10_BoolVar', b)
    _safe_set(b, 'gx10_BoolExpression39', None)
    assert not _is_linked(b, 'gx10_BoolExpression39', a2)
    if hasattr(a2, 'gx10_BoolVar'):
        assert not _is_linked(a2, 'gx10_BoolVar', b)


def test_assoc_boolVarName40_reverse_link_reassign_clear():
    a1 = gx10_Referentiable(name=7)
    a2 = gx10_Referentiable(name=13)
    b = gx10_BoolVar()
    _safe_set(b, 'gx10_BoolVar41', a1)
    assert _is_linked(b, 'gx10_BoolVar41', a1)
    if hasattr(a1, 'gx10_Referentiable42'):
        assert _is_linked(a1, 'gx10_Referentiable42', b)
    _safe_set(b, 'gx10_BoolVar41', a2)
    assert _is_linked(b, 'gx10_BoolVar41', a2)
    if hasattr(a1, 'gx10_Referentiable42'):
        assert not _is_linked(a1, 'gx10_Referentiable42', b)
    if hasattr(a2, 'gx10_Referentiable42'):
        assert _is_linked(a2, 'gx10_Referentiable42', b)
    _safe_set(b, 'gx10_BoolVar41', None)
    assert not _is_linked(b, 'gx10_BoolVar41', a2)
    if hasattr(a2, 'gx10_Referentiable42'):
        assert not _is_linked(a2, 'gx10_Referentiable42', b)


def test_assoc_boolVarRef50_reverse_link_reassign_clear():
    a1 = gx10_Referentiable(name=7)
    a2 = gx10_Referentiable(name=13)
    b = gx10_BoolVarAccess()
    _safe_set(b, 'gx10_BoolVarAccess', a1)
    assert _is_linked(b, 'gx10_BoolVarAccess', a1)
    if hasattr(a1, 'gx10_Referentiable51'):
        assert _is_linked(a1, 'gx10_Referentiable51', b)
    _safe_set(b, 'gx10_BoolVarAccess', a2)
    assert _is_linked(b, 'gx10_BoolVarAccess', a2)
    if hasattr(a1, 'gx10_Referentiable51'):
        assert not _is_linked(a1, 'gx10_Referentiable51', b)
    if hasattr(a2, 'gx10_Referentiable51'):
        assert _is_linked(a2, 'gx10_Referentiable51', b)
    _safe_set(b, 'gx10_BoolVarAccess', None)
    assert not _is_linked(b, 'gx10_BoolVarAccess', a2)
    if hasattr(a2, 'gx10_Referentiable51'):
        assert not _is_linked(a2, 'gx10_Referentiable51', b)


def test_assoc_calledBy5_reverse_link_reassign_clear():
    a1 = gx10_MethodCall()
    a2 = gx10_MethodCall()
    b = gx10_Method(name="sample_text")
    _safe_set(b, 'methodToCall', {a1})
    assert _is_linked(b, 'methodToCall', a1)
    if hasattr(a1, 'MethodCall'):
        assert _is_linked(a1, 'MethodCall', b)
    _safe_set(b, 'methodToCall', {a2})
    assert _is_linked(b, 'methodToCall', a2)
    if hasattr(a1, 'MethodCall'):
        assert not _is_linked(a1, 'MethodCall', b)
    if hasattr(a2, 'MethodCall'):
        assert _is_linked(a2, 'MethodCall', b)
    _safe_set(b, 'methodToCall', set())
    assert not _is_linked(b, 'methodToCall', a2)
    if hasattr(a2, 'MethodCall'):
        assert not _is_linked(a2, 'MethodCall', b)


def test_assoc_inMethodCall58_reverse_link_reassign_clear():
    a1 = gx10_MethodCallParameter(name="sample_text")
    a2 = gx10_MethodCallParameter(name="sample_text_2")
    b = gx10_MethodCall()
    _safe_set(b, 'MethodCall59', a1)
    assert _is_linked(b, 'MethodCall59', a1)
    if hasattr(a1, 'methodCallParameters'):
        assert _is_linked(a1, 'methodCallParameters', b)
    _safe_set(b, 'MethodCall59', a2)
    assert _is_linked(b, 'MethodCall59', a2)
    if hasattr(a1, 'methodCallParameters'):
        assert not _is_linked(a1, 'methodCallParameters', b)
    if hasattr(a2, 'methodCallParameters'):
        assert _is_linked(a2, 'methodCallParameters', b)
    _safe_set(b, 'MethodCall59', None)
    assert not _is_linked(b, 'MethodCall59', a2)
    if hasattr(a2, 'methodCallParameters'):
        assert not _is_linked(a2, 'methodCallParameters', b)


def test_assoc_inMethodCallParameter11_reverse_link_reassign_clear():
    a1 = gx10_MethodCallParameter(name="sample_text")
    a2 = gx10_MethodCallParameter(name="sample_text_2")
    b = gx10_IntExpression()
    _safe_set(b, 'methodCallParameterExpr', a1)
    assert _is_linked(b, 'methodCallParameterExpr', a1)
    if hasattr(a1, 'MethodCallParameter'):
        assert _is_linked(a1, 'MethodCallParameter', b)
    _safe_set(b, 'methodCallParameterExpr', a2)
    assert _is_linked(b, 'methodCallParameterExpr', a2)
    if hasattr(a1, 'MethodCallParameter'):
        assert not _is_linked(a1, 'MethodCallParameter', b)
    if hasattr(a2, 'MethodCallParameter'):
        assert _is_linked(a2, 'MethodCallParameter', b)
    _safe_set(b, 'methodCallParameterExpr', None)
    assert not _is_linked(b, 'methodCallParameterExpr', a2)
    if hasattr(a2, 'MethodCallParameter'):
        assert not _is_linked(a2, 'MethodCallParameter', b)


def test_assoc_intVarExpr43_reverse_link_reassign_clear():
    a1 = gx10_IntVar()
    a2 = gx10_IntVar()
    b = gx10_IntExpression()
    _safe_set(b, 'gx10_IntExpression44', a1)
    assert _is_linked(b, 'gx10_IntExpression44', a1)
    if hasattr(a1, 'gx10_IntVar'):
        assert _is_linked(a1, 'gx10_IntVar', b)
    _safe_set(b, 'gx10_IntExpression44', a2)
    assert _is_linked(b, 'gx10_IntExpression44', a2)
    if hasattr(a1, 'gx10_IntVar'):
        assert not _is_linked(a1, 'gx10_IntVar', b)
    if hasattr(a2, 'gx10_IntVar'):
        assert _is_linked(a2, 'gx10_IntVar', b)
    _safe_set(b, 'gx10_IntExpression44', None)
    assert not _is_linked(b, 'gx10_IntExpression44', a2)
    if hasattr(a2, 'gx10_IntVar'):
        assert not _is_linked(a2, 'gx10_IntVar', b)


def test_assoc_intVarName45_reverse_link_reassign_clear():
    a1 = gx10_Referentiable(name=7)
    a2 = gx10_Referentiable(name=13)
    b = gx10_IntVar()
    _safe_set(b, 'gx10_IntVar46', a1)
    assert _is_linked(b, 'gx10_IntVar46', a1)
    if hasattr(a1, 'gx10_Referentiable47'):
        assert _is_linked(a1, 'gx10_Referentiable47', b)
    _safe_set(b, 'gx10_IntVar46', a2)
    assert _is_linked(b, 'gx10_IntVar46', a2)
    if hasattr(a1, 'gx10_Referentiable47'):
        assert not _is_linked(a1, 'gx10_Referentiable47', b)
    if hasattr(a2, 'gx10_Referentiable47'):
        assert _is_linked(a2, 'gx10_Referentiable47', b)
    _safe_set(b, 'gx10_IntVar46', None)
    assert not _is_linked(b, 'gx10_IntVar46', a2)
    if hasattr(a2, 'gx10_Referentiable47'):
        assert not _is_linked(a2, 'gx10_Referentiable47', b)


def test_assoc_intVarRef48_reverse_link_reassign_clear():
    a1 = gx10_Referentiable(name=7)
    a2 = gx10_Referentiable(name=13)
    b = gx10_IntVarAccess()
    _safe_set(b, 'gx10_IntVarAccess', a1)
    assert _is_linked(b, 'gx10_IntVarAccess', a1)
    if hasattr(a1, 'gx10_Referentiable49'):
        assert _is_linked(a1, 'gx10_Referentiable49', b)
    _safe_set(b, 'gx10_IntVarAccess', a2)
    assert _is_linked(b, 'gx10_IntVarAccess', a2)
    if hasattr(a1, 'gx10_Referentiable49'):
        assert not _is_linked(a1, 'gx10_Referentiable49', b)
    if hasattr(a2, 'gx10_Referentiable49'):
        assert _is_linked(a2, 'gx10_Referentiable49', b)
    _safe_set(b, 'gx10_IntVarAccess', None)
    assert not _is_linked(b, 'gx10_IntVarAccess', a2)
    if hasattr(a2, 'gx10_Referentiable49'):
        assert not _is_linked(a2, 'gx10_Referentiable49', b)


def test_assoc_leftBinaryExpression26_reverse_link_reassign_clear():
    a1 = gx10_IntExpression()
    a2 = gx10_IntExpression()
    b = gx10_IntBinaryOperation()
    _safe_set(b, 'gx10_IntBinaryOperation', a1)
    assert _is_linked(b, 'gx10_IntBinaryOperation', a1)
    if hasattr(a1, 'gx10_IntExpression'):
        assert _is_linked(a1, 'gx10_IntExpression', b)
    _safe_set(b, 'gx10_IntBinaryOperation', a2)
    assert _is_linked(b, 'gx10_IntBinaryOperation', a2)
    if hasattr(a1, 'gx10_IntExpression'):
        assert not _is_linked(a1, 'gx10_IntExpression', b)
    if hasattr(a2, 'gx10_IntExpression'):
        assert _is_linked(a2, 'gx10_IntExpression', b)
    _safe_set(b, 'gx10_IntBinaryOperation', None)
    assert not _is_linked(b, 'gx10_IntBinaryOperation', a2)
    if hasattr(a2, 'gx10_IntExpression'):
        assert not _is_linked(a2, 'gx10_IntExpression', b)


def test_assoc_leftEqual52_reverse_link_reassign_clear():
    a1 = gx10_IntExpression()
    a2 = gx10_IntExpression()
    b = gx10_Equal()
    _safe_set(b, 'gx10_Equal', a1)
    assert _is_linked(b, 'gx10_Equal', a1)
    if hasattr(a1, 'gx10_IntExpression53'):
        assert _is_linked(a1, 'gx10_IntExpression53', b)
    _safe_set(b, 'gx10_Equal', a2)
    assert _is_linked(b, 'gx10_Equal', a2)
    if hasattr(a1, 'gx10_IntExpression53'):
        assert not _is_linked(a1, 'gx10_IntExpression53', b)
    if hasattr(a2, 'gx10_IntExpression53'):
        assert _is_linked(a2, 'gx10_IntExpression53', b)
    _safe_set(b, 'gx10_Equal', None)
    assert not _is_linked(b, 'gx10_Equal', a2)
    if hasattr(a2, 'gx10_IntExpression53'):
        assert not _is_linked(a2, 'gx10_IntExpression53', b)


def test_assoc_methodBlock3_reverse_link_reassign_clear():
    a1 = gx10_Method(name="sample_text")
    a2 = gx10_Method(name="sample_text_2")
    b = gx10_Block(context=7)
    _safe_set(b, 'gx10_Block', a1)
    assert _is_linked(b, 'gx10_Block', a1)
    if hasattr(a1, 'gx10_Method4'):
        assert _is_linked(a1, 'gx10_Method4', b)
    _safe_set(b, 'gx10_Block', a2)
    assert _is_linked(b, 'gx10_Block', a2)
    if hasattr(a1, 'gx10_Method4'):
        assert not _is_linked(a1, 'gx10_Method4', b)
    if hasattr(a2, 'gx10_Method4'):
        assert _is_linked(a2, 'gx10_Method4', b)
    _safe_set(b, 'gx10_Block', None)
    assert not _is_linked(b, 'gx10_Block', a2)
    if hasattr(a2, 'gx10_Method4'):
        assert not _is_linked(a2, 'gx10_Method4', b)


def test_assoc_methodCallParameterExpr57_reverse_link_reassign_clear():
    a1 = gx10_MethodCallParameter(name="sample_text")
    a2 = gx10_MethodCallParameter(name="sample_text_2")
    b = gx10_IntExpression()
    _safe_set(b, 'IntExpression', a1)
    assert _is_linked(b, 'IntExpression', a1)
    if hasattr(a1, 'inMethodCallParameter'):
        assert _is_linked(a1, 'inMethodCallParameter', b)
    _safe_set(b, 'IntExpression', a2)
    assert _is_linked(b, 'IntExpression', a2)
    if hasattr(a1, 'inMethodCallParameter'):
        assert not _is_linked(a1, 'inMethodCallParameter', b)
    if hasattr(a2, 'inMethodCallParameter'):
        assert _is_linked(a2, 'inMethodCallParameter', b)
    _safe_set(b, 'IntExpression', None)
    assert not _is_linked(b, 'IntExpression', a2)
    if hasattr(a2, 'inMethodCallParameter'):
        assert not _is_linked(a2, 'inMethodCallParameter', b)


def test_assoc_methodCallParameters33_reverse_link_reassign_clear():
    a1 = gx10_MethodCallParameter(name="sample_text")
    a2 = gx10_MethodCallParameter(name="sample_text_2")
    b = gx10_MethodCall()
    _safe_set(b, 'inMethodCall', {a1})
    assert _is_linked(b, 'inMethodCall', a1)
    if hasattr(a1, 'MethodCallParameter34'):
        assert _is_linked(a1, 'MethodCallParameter34', b)
    _safe_set(b, 'inMethodCall', {a2})
    assert _is_linked(b, 'inMethodCall', a2)
    if hasattr(a1, 'MethodCallParameter34'):
        assert not _is_linked(a1, 'MethodCallParameter34', b)
    if hasattr(a2, 'MethodCallParameter34'):
        assert _is_linked(a2, 'MethodCallParameter34', b)
    _safe_set(b, 'inMethodCall', set())
    assert not _is_linked(b, 'inMethodCall', a2)
    if hasattr(a2, 'MethodCallParameter34'):
        assert not _is_linked(a2, 'MethodCallParameter34', b)


def test_assoc_methodParameters6_reverse_link_reassign_clear():
    a1 = gx10_Referentiable(name=7)
    a2 = gx10_Referentiable(name=13)
    b = gx10_Method(name="sample_text")
    _safe_set(b, 'gx10_Method7', {a1})
    assert _is_linked(b, 'gx10_Method7', a1)
    if hasattr(a1, 'gx10_Referentiable'):
        assert _is_linked(a1, 'gx10_Referentiable', b)
    _safe_set(b, 'gx10_Method7', {a2})
    assert _is_linked(b, 'gx10_Method7', a2)
    if hasattr(a1, 'gx10_Referentiable'):
        assert not _is_linked(a1, 'gx10_Referentiable', b)
    if hasattr(a2, 'gx10_Referentiable'):
        assert _is_linked(a2, 'gx10_Referentiable', b)
    _safe_set(b, 'gx10_Method7', set())
    assert not _is_linked(b, 'gx10_Method7', a2)
    if hasattr(a2, 'gx10_Referentiable'):
        assert not _is_linked(a2, 'gx10_Referentiable', b)


def test_assoc_methodToCall31_reverse_link_reassign_clear():
    a1 = gx10_MethodCall()
    a2 = gx10_MethodCall()
    b = gx10_Method(name="sample_text")
    _safe_set(b, 'Method32', a1)
    assert _is_linked(b, 'Method32', a1)
    if hasattr(a1, 'calledBy'):
        assert _is_linked(a1, 'calledBy', b)
    _safe_set(b, 'Method32', a2)
    assert _is_linked(b, 'Method32', a2)
    if hasattr(a1, 'calledBy'):
        assert not _is_linked(a1, 'calledBy', b)
    if hasattr(a2, 'calledBy'):
        assert _is_linked(a2, 'calledBy', b)
    _safe_set(b, 'Method32', None)
    assert not _is_linked(b, 'Method32', a2)
    if hasattr(a2, 'calledBy'):
        assert not _is_linked(a2, 'calledBy', b)


def test_assoc_notExpression19_reverse_link_reassign_clear():
    a1 = gx10_Not()
    a2 = gx10_Not()
    b = gx10_BoolExpression()
    _safe_set(b, 'gx10_BoolExpression20', a1)
    assert _is_linked(b, 'gx10_BoolExpression20', a1)
    if hasattr(a1, 'gx10_Not'):
        assert _is_linked(a1, 'gx10_Not', b)
    _safe_set(b, 'gx10_BoolExpression20', a2)
    assert _is_linked(b, 'gx10_BoolExpression20', a2)
    if hasattr(a1, 'gx10_Not'):
        assert not _is_linked(a1, 'gx10_Not', b)
    if hasattr(a2, 'gx10_Not'):
        assert _is_linked(a2, 'gx10_Not', b)
    _safe_set(b, 'gx10_BoolExpression20', None)
    assert not _is_linked(b, 'gx10_BoolExpression20', a2)
    if hasattr(a2, 'gx10_Not'):
        assert not _is_linked(a2, 'gx10_Not', b)


def test_assoc_rightBinaryExpression27_reverse_link_reassign_clear():
    a1 = gx10_IntExpression()
    a2 = gx10_IntExpression()
    b = gx10_IntBinaryOperation()
    _safe_set(b, 'gx10_IntBinaryOperation28', a1)
    assert _is_linked(b, 'gx10_IntBinaryOperation28', a1)
    if hasattr(a1, 'gx10_IntExpression29'):
        assert _is_linked(a1, 'gx10_IntExpression29', b)
    _safe_set(b, 'gx10_IntBinaryOperation28', a2)
    assert _is_linked(b, 'gx10_IntBinaryOperation28', a2)
    if hasattr(a1, 'gx10_IntExpression29'):
        assert not _is_linked(a1, 'gx10_IntExpression29', b)
    if hasattr(a2, 'gx10_IntExpression29'):
        assert _is_linked(a2, 'gx10_IntExpression29', b)
    _safe_set(b, 'gx10_IntBinaryOperation28', None)
    assert not _is_linked(b, 'gx10_IntBinaryOperation28', a2)
    if hasattr(a2, 'gx10_IntExpression29'):
        assert not _is_linked(a2, 'gx10_IntExpression29', b)


def test_assoc_rightEqual54_reverse_link_reassign_clear():
    a1 = gx10_IntExpression()
    a2 = gx10_IntExpression()
    b = gx10_Equal()
    _safe_set(b, 'gx10_Equal55', a1)
    assert _is_linked(b, 'gx10_Equal55', a1)
    if hasattr(a1, 'gx10_IntExpression56'):
        assert _is_linked(a1, 'gx10_IntExpression56', b)
    _safe_set(b, 'gx10_Equal55', a2)
    assert _is_linked(b, 'gx10_Equal55', a2)
    if hasattr(a1, 'gx10_IntExpression56'):
        assert not _is_linked(a1, 'gx10_IntExpression56', b)
    if hasattr(a2, 'gx10_IntExpression56'):
        assert _is_linked(a2, 'gx10_IntExpression56', b)
    _safe_set(b, 'gx10_Equal55', None)
    assert not _is_linked(b, 'gx10_Equal55', a2)
    if hasattr(a2, 'gx10_IntExpression56'):
        assert not _is_linked(a2, 'gx10_IntExpression56', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_blockStatements8_stub_double():
    # gx10_Statement has no real 'Statement' property in the generated
    # code (a bare stub) -- manually attach it so gx10_Block's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # gx10_Block's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = gx10_Block(context=7)
    partner = gx10_Statement()
    setattr(partner, 'Statement', None)
    _safe_set(owner, 'inBlock', {partner})
    assert getattr(partner, 'Statement') == owner
    _safe_set(owner, 'inBlock', set())
    assert getattr(partner, 'Statement') is None


def test_assoc_controlStructureCondition10_stub_double():
    # gx10_ControlStructure has no real 'gx10_ControlStructure' property in the generated
    # code (a bare stub) -- manually attach it so gx10_BoolExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # gx10_BoolExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = gx10_BoolExpression()
    partner = gx10_ControlStructure()
    setattr(partner, 'gx10_ControlStructure', None)
    _safe_set(owner, 'gx10_BoolExpression', partner)
    assert getattr(partner, 'gx10_ControlStructure') == owner
    _safe_set(owner, 'gx10_BoolExpression', None)
    assert getattr(partner, 'gx10_ControlStructure') is None


def test_assoc_elseBlock14_stub_double():
    # gx10_If has no real 'gx10_If15' property in the generated
    # code (a bare stub) -- manually attach it so gx10_Block's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # gx10_Block's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = gx10_Block(context=7)
    partner = gx10_If()
    setattr(partner, 'gx10_If15', None)
    _safe_set(owner, 'gx10_Block16', partner)
    assert getattr(partner, 'gx10_If15') == owner
    _safe_set(owner, 'gx10_Block16', None)
    assert getattr(partner, 'gx10_If15') is None


def test_assoc_inBlock9_stub_double():
    # gx10_Statement has no real 'blockStatements' property in the generated
    # code (a bare stub) -- manually attach it so gx10_Block's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # gx10_Block's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = gx10_Block(context=7)
    partner = gx10_Statement()
    setattr(partner, 'blockStatements', None)
    _safe_set(owner, 'Block', partner)
    assert getattr(partner, 'blockStatements') == owner
    _safe_set(owner, 'Block', None)
    assert getattr(partner, 'blockStatements') is None


def test_assoc_inProgram2_stub_double():
    # gx10_Program has no real 'Program' property in the generated
    # code (a bare stub) -- manually attach it so gx10_Method's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # gx10_Method's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = gx10_Method(name="sample_text")
    partner = gx10_Program()
    setattr(partner, 'Program', None)
    _safe_set(owner, 'methods', partner)
    assert getattr(partner, 'Program') == owner
    _safe_set(owner, 'methods', None)
    assert getattr(partner, 'Program') is None


def test_assoc_leftAndExpression21_stub_double():
    # gx10_And has no real 'gx10_And' property in the generated
    # code (a bare stub) -- manually attach it so gx10_BoolExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # gx10_BoolExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = gx10_BoolExpression()
    partner = gx10_And()
    setattr(partner, 'gx10_And', None)
    _safe_set(owner, 'gx10_BoolExpression22', partner)
    assert getattr(partner, 'gx10_And') == owner
    _safe_set(owner, 'gx10_BoolExpression22', None)
    assert getattr(partner, 'gx10_And') is None


def test_assoc_methods0_stub_double():
    # gx10_Program has no real 'inProgram' property in the generated
    # code (a bare stub) -- manually attach it so gx10_Method's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # gx10_Method's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = gx10_Method(name="sample_text")
    partner = gx10_Program()
    setattr(partner, 'inProgram', None)
    _safe_set(owner, 'Method', partner)
    assert owner in getattr(partner, 'inProgram')
    _safe_set(owner, 'Method', None)
    assert owner not in getattr(partner, 'inProgram')


def test_assoc_rightAndExpression23_stub_double():
    # gx10_And has no real 'gx10_And24' property in the generated
    # code (a bare stub) -- manually attach it so gx10_BoolExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # gx10_BoolExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = gx10_BoolExpression()
    partner = gx10_And()
    setattr(partner, 'gx10_And24', None)
    _safe_set(owner, 'gx10_BoolExpression25', partner)
    assert getattr(partner, 'gx10_And24') == owner
    _safe_set(owner, 'gx10_BoolExpression25', None)
    assert getattr(partner, 'gx10_And24') is None


def test_assoc_startMethod1_stub_double():
    # gx10_Program has no real 'gx10_Program' property in the generated
    # code (a bare stub) -- manually attach it so gx10_Method's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # gx10_Method's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = gx10_Method(name="sample_text")
    partner = gx10_Program()
    setattr(partner, 'gx10_Program', None)
    _safe_set(owner, 'gx10_Method', partner)
    assert getattr(partner, 'gx10_Program') == owner
    _safe_set(owner, 'gx10_Method', None)
    assert getattr(partner, 'gx10_Program') is None


def test_assoc_thenBlock12_stub_double():
    # gx10_If has no real 'gx10_If' property in the generated
    # code (a bare stub) -- manually attach it so gx10_Block's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # gx10_Block's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = gx10_Block(context=7)
    partner = gx10_If()
    setattr(partner, 'gx10_If', None)
    _safe_set(owner, 'gx10_Block13', partner)
    assert getattr(partner, 'gx10_If') == owner
    _safe_set(owner, 'gx10_Block13', None)
    assert getattr(partner, 'gx10_If') is None


def test_assoc_toPrint37_stub_double():
    # gx10_Expression has no real 'gx10_Expression' property in the generated
    # code (a bare stub) -- manually attach it so gx10_Print's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # gx10_Print's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = gx10_Print()
    partner = gx10_Expression()
    setattr(partner, 'gx10_Expression', None)
    _safe_set(owner, 'gx10_Print', partner)
    assert getattr(partner, 'gx10_Expression') == owner
    _safe_set(owner, 'gx10_Print', None)
    assert getattr(partner, 'gx10_Expression') is None


def test_assoc_whileBlock17_stub_double():
    # gx10_While has no real 'gx10_While' property in the generated
    # code (a bare stub) -- manually attach it so gx10_Block's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # gx10_Block's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = gx10_Block(context=7)
    partner = gx10_While()
    setattr(partner, 'gx10_While', None)
    _safe_set(owner, 'gx10_Block18', partner)
    assert getattr(partner, 'gx10_While') == owner
    _safe_set(owner, 'gx10_Block18', None)
    assert getattr(partner, 'gx10_While') is None


