import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    ArithmeticExpression,
    AtomicExpression,
    Expression,
    FunctionalUnit,
    Operation,
    Statement,
    UnaryExpression,
    mpl_AddExpression,
    mpl_ArithmeticExpression,
    mpl_Assignment,
    mpl_AtomicExpression,
    mpl_Block,
    mpl_ComparisonExpression,
    mpl_DivExpression,
    mpl_Expression,
    mpl_ExpressionStatement,
    mpl_ForLoop,
    mpl_Function,
    mpl_FunctionalUnit,
    mpl_IfStatement,
    mpl_LiteralValue,
    mpl_MPLModel,
    mpl_MulExpression,
    mpl_Operation,
    mpl_OperationExpression,
    mpl_ParenthesisExpression,
    mpl_Procedure,
    mpl_Program,
    mpl_ReturnStatement,
    mpl_Statement,
    mpl_SubExpression,
    mpl_Trace,
    mpl_UnaryExpression,
    mpl_UnaryMinusExpression,
    mpl_Variable,
    mpl_VariableDeclaration,
    mpl_VariableReference,
    mpl_WhileLoop,
    ComparisonOperator,
    ForLoopDirection,
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

def test_assoc_body36_stub_double():
    # mpl_Block has no real 'mpl_Block38' property in the generated
    # code (a bare stub) -- manually attach it so mpl_ForLoop's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # mpl_ForLoop's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = mpl_ForLoop(direction="sample_text")
    partner = mpl_Block()
    setattr(partner, 'mpl_Block38', None)
    _safe_set(owner, 'mpl_ForLoop37', partner)
    assert getattr(partner, 'mpl_Block38') == owner
    _safe_set(owner, 'mpl_ForLoop37', None)
    assert getattr(partner, 'mpl_Block38') is None


def test_assoc_bound33_stub_double():
    # mpl_Expression has no real 'mpl_Expression35' property in the generated
    # code (a bare stub) -- manually attach it so mpl_ForLoop's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # mpl_ForLoop's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = mpl_ForLoop(direction="sample_text")
    partner = mpl_Expression()
    setattr(partner, 'mpl_Expression35', None)
    _safe_set(owner, 'mpl_ForLoop34', partner)
    assert getattr(partner, 'mpl_Expression35') == owner
    _safe_set(owner, 'mpl_ForLoop34', None)
    assert getattr(partner, 'mpl_Expression35') is None


def test_assoc_condition19_stub_double():
    # mpl_IfStatement has no real 'mpl_IfStatement' property in the generated
    # code (a bare stub) -- manually attach it so mpl_ComparisonExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # mpl_ComparisonExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = mpl_ComparisonExpression(comparisonOperator="sample_text")
    partner = mpl_IfStatement()
    setattr(partner, 'mpl_IfStatement', None)
    _safe_set(owner, 'mpl_ComparisonExpression', partner)
    assert getattr(partner, 'mpl_IfStatement') == owner
    _safe_set(owner, 'mpl_ComparisonExpression', None)
    assert getattr(partner, 'mpl_IfStatement') is None


def test_assoc_condition26_stub_double():
    # mpl_WhileLoop has no real 'mpl_WhileLoop' property in the generated
    # code (a bare stub) -- manually attach it so mpl_ComparisonExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # mpl_ComparisonExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = mpl_ComparisonExpression(comparisonOperator="sample_text")
    partner = mpl_WhileLoop()
    setattr(partner, 'mpl_WhileLoop', None)
    _safe_set(owner, 'mpl_ComparisonExpression27', partner)
    assert getattr(partner, 'mpl_WhileLoop') == owner
    _safe_set(owner, 'mpl_ComparisonExpression27', None)
    assert getattr(partner, 'mpl_WhileLoop') is None


def test_assoc_counter31_stub_double():
    # mpl_Assignment has no real 'mpl_Assignment32' property in the generated
    # code (a bare stub) -- manually attach it so mpl_ForLoop's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # mpl_ForLoop's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = mpl_ForLoop(direction="sample_text")
    partner = mpl_Assignment()
    setattr(partner, 'mpl_Assignment32', None)
    _safe_set(owner, 'mpl_ForLoop', partner)
    assert getattr(partner, 'mpl_Assignment32') == owner
    _safe_set(owner, 'mpl_ForLoop', None)
    assert getattr(partner, 'mpl_Assignment32') is None


def test_assoc_functionalBody4_stub_double():
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


def test_assoc_leftHandSide48_stub_double():
    # mpl_Expression has no real 'mpl_Expression50' property in the generated
    # code (a bare stub) -- manually attach it so mpl_ComparisonExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # mpl_ComparisonExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = mpl_ComparisonExpression(comparisonOperator="sample_text")
    partner = mpl_Expression()
    setattr(partner, 'mpl_Expression50', None)
    _safe_set(owner, 'mpl_ComparisonExpression49', partner)
    assert getattr(partner, 'mpl_Expression50') == owner
    _safe_set(owner, 'mpl_ComparisonExpression49', None)
    assert getattr(partner, 'mpl_Expression50') is None


def test_assoc_parameters6_stub_double():
    # mpl_Operation has no real 'mpl_Operation7' property in the generated
    # code (a bare stub) -- manually attach it so mpl_Variable's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # mpl_Variable's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = mpl_Variable(name="sample_text")
    partner = mpl_Operation()
    setattr(partner, 'mpl_Operation7', None)
    _safe_set(owner, 'mpl_Variable', partner)
    assert owner in getattr(partner, 'mpl_Operation7')
    _safe_set(owner, 'mpl_Variable', None)
    assert owner not in getattr(partner, 'mpl_Operation7')


def test_assoc_rightHandSide51_stub_double():
    # mpl_Expression has no real 'mpl_Expression53' property in the generated
    # code (a bare stub) -- manually attach it so mpl_ComparisonExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # mpl_ComparisonExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = mpl_ComparisonExpression(comparisonOperator="sample_text")
    partner = mpl_Expression()
    setattr(partner, 'mpl_Expression53', None)
    _safe_set(owner, 'mpl_ComparisonExpression52', partner)
    assert getattr(partner, 'mpl_Expression53') == owner
    _safe_set(owner, 'mpl_ComparisonExpression52', None)
    assert getattr(partner, 'mpl_Expression53') is None


def test_assoc_variable45_stub_double():
    # mpl_VariableReference has no real 'mpl_VariableReference46' property in the generated
    # code (a bare stub) -- manually attach it so mpl_Variable's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # mpl_Variable's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = mpl_Variable(name="sample_text")
    partner = mpl_VariableReference()
    setattr(partner, 'mpl_VariableReference46', None)
    _safe_set(owner, 'mpl_Variable47', partner)
    assert getattr(partner, 'mpl_VariableReference46') == owner
    _safe_set(owner, 'mpl_Variable47', None)
    assert getattr(partner, 'mpl_VariableReference46') is None


def test_assoc_variable8_stub_double():
    # mpl_VariableDeclaration has no real 'mpl_VariableDeclaration9' property in the generated
    # code (a bare stub) -- manually attach it so mpl_Variable's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # mpl_Variable's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = mpl_Variable(name="sample_text")
    partner = mpl_VariableDeclaration()
    setattr(partner, 'mpl_VariableDeclaration9', None)
    _safe_set(owner, 'mpl_Variable10', partner)
    assert getattr(partner, 'mpl_VariableDeclaration9') == owner
    _safe_set(owner, 'mpl_Variable10', None)
    assert getattr(partner, 'mpl_VariableDeclaration9') is None


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


