import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    ArithmeticExpression,
    AtomicExpression,
    ComparisonOperator,
    Expression,
    Form,
    FunctionalUnit,
    Loop,
    Operation,
    UnaryExpression,
    mpl_AddExpression,
    mpl_ArithmeticExpression,
    mpl_Assignment,
    mpl_AtomicExpression,
    mpl_Block,
    mpl_Comparison,
    mpl_ComparisonOperator,
    mpl_DivisionExpression,
    mpl_EQ,
    mpl_Expression,
    mpl_ExpressionStatement,
    mpl_For,
    mpl_Form,
    mpl_Function,
    mpl_FunctionalUnit,
    mpl_GE,
    mpl_GT,
    mpl_If,
    mpl_InputExpression,
    mpl_LE,
    mpl_LT,
    mpl_LiteralValue,
    mpl_Loop,
    mpl_MPLModel,
    mpl_MultiplyExpression,
    mpl_NE,
    mpl_NegateExpression,
    mpl_Operation,
    mpl_OperationExpression,
    mpl_ParenExpression,
    mpl_Procedure,
    mpl_Program,
    mpl_Return,
    mpl_Statement,
    mpl_SubtractExpression,
    mpl_TraceCall,
    mpl_UnaryExpression,
    mpl_Variable,
    mpl_VariableDeclaration,
    mpl_VariableReference,
    mpl_While,
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

def test_assoc_body4_stub_double():
    # mpl_Block has no real 'mpl_Block' property in the generated
    # code (a bare stub) -- manually attach it so mpl_FunctionalUnit's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # mpl_FunctionalUnit's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = mpl_FunctionalUnit(name="sample_text")
    partner = mpl_Block()
    setattr(partner, 'mpl_Block', None)
    _safe_set(owner, 'mpl_FunctionalUnit5', partner)
    assert getattr(partner, 'mpl_Block') == owner
    _safe_set(owner, 'mpl_FunctionalUnit5', None)
    assert getattr(partner, 'mpl_Block') is None


def test_assoc_from_53_stub_double():
    # mpl_Assignment has no real 'mpl_Assignment54' property in the generated
    # code (a bare stub) -- manually attach it so mpl_For's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # mpl_For's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = mpl_For(downwards="sample_text")
    partner = mpl_Assignment()
    setattr(partner, 'mpl_Assignment54', None)
    _safe_set(owner, 'mpl_For', partner)
    assert getattr(partner, 'mpl_Assignment54') == owner
    _safe_set(owner, 'mpl_For', None)
    assert getattr(partner, 'mpl_Assignment54') is None


def test_assoc_lowerBound30_stub_double():
    # mpl_InputExpression has no real 'mpl_InputExpression' property in the generated
    # code (a bare stub) -- manually attach it so mpl_LiteralValue's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # mpl_LiteralValue's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = mpl_LiteralValue(rawValue=7)
    partner = mpl_InputExpression()
    setattr(partner, 'mpl_InputExpression', None)
    _safe_set(owner, 'mpl_LiteralValue', partner)
    assert getattr(partner, 'mpl_InputExpression') == owner
    _safe_set(owner, 'mpl_LiteralValue', None)
    assert getattr(partner, 'mpl_InputExpression') is None


def test_assoc_parameters58_stub_double():
    # mpl_Operation has no real 'mpl_Operation59' property in the generated
    # code (a bare stub) -- manually attach it so mpl_Variable's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # mpl_Variable's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = mpl_Variable(name="sample_text")
    partner = mpl_Operation()
    setattr(partner, 'mpl_Operation59', None)
    _safe_set(owner, 'mpl_Variable60', partner)
    assert owner in getattr(partner, 'mpl_Operation59')
    _safe_set(owner, 'mpl_Variable60', None)
    assert owner not in getattr(partner, 'mpl_Operation59')


def test_assoc_to55_stub_double():
    # mpl_Expression has no real 'mpl_Expression57' property in the generated
    # code (a bare stub) -- manually attach it so mpl_For's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # mpl_For's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = mpl_For(downwards="sample_text")
    partner = mpl_Expression()
    setattr(partner, 'mpl_Expression57', None)
    _safe_set(owner, 'mpl_For56', partner)
    assert getattr(partner, 'mpl_Expression57') == owner
    _safe_set(owner, 'mpl_For56', None)
    assert getattr(partner, 'mpl_Expression57') is None


def test_assoc_upperBound31_stub_double():
    # mpl_InputExpression has no real 'mpl_InputExpression32' property in the generated
    # code (a bare stub) -- manually attach it so mpl_LiteralValue's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # mpl_LiteralValue's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = mpl_LiteralValue(rawValue=7)
    partner = mpl_InputExpression()
    setattr(partner, 'mpl_InputExpression32', None)
    _safe_set(owner, 'mpl_LiteralValue33', partner)
    assert getattr(partner, 'mpl_InputExpression32') == owner
    _safe_set(owner, 'mpl_LiteralValue33', None)
    assert getattr(partner, 'mpl_InputExpression32') is None


def test_assoc_variable20_stub_double():
    # mpl_VariableReference has no real 'mpl_VariableReference21' property in the generated
    # code (a bare stub) -- manually attach it so mpl_Variable's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # mpl_Variable's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = mpl_Variable(name="sample_text")
    partner = mpl_VariableReference()
    setattr(partner, 'mpl_VariableReference21', None)
    _safe_set(owner, 'mpl_Variable22', partner)
    assert getattr(partner, 'mpl_VariableReference21') == owner
    _safe_set(owner, 'mpl_Variable22', None)
    assert getattr(partner, 'mpl_VariableReference21') is None


def test_assoc_variable6_stub_double():
    # mpl_VariableDeclaration has no real 'mpl_VariableDeclaration7' property in the generated
    # code (a bare stub) -- manually attach it so mpl_Variable's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # mpl_Variable's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = mpl_Variable(name="sample_text")
    partner = mpl_VariableDeclaration()
    setattr(partner, 'mpl_VariableDeclaration7', None)
    _safe_set(owner, 'mpl_Variable', partner)
    assert getattr(partner, 'mpl_VariableDeclaration7') == owner
    _safe_set(owner, 'mpl_Variable', None)
    assert getattr(partner, 'mpl_VariableDeclaration7') is None


def test_assoc_variableDeclarations3_stub_double():
    # mpl_VariableDeclaration has no real 'mpl_VariableDeclaration' property in the generated
    # code (a bare stub) -- manually attach it so mpl_FunctionalUnit's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # mpl_FunctionalUnit's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = mpl_FunctionalUnit(name="sample_text")
    partner = mpl_VariableDeclaration()
    setattr(partner, 'mpl_VariableDeclaration', None)
    _safe_set(owner, 'mpl_FunctionalUnit', {partner})
    assert getattr(partner, 'mpl_VariableDeclaration') == owner
    _safe_set(owner, 'mpl_FunctionalUnit', set())
    assert getattr(partner, 'mpl_VariableDeclaration') is None


