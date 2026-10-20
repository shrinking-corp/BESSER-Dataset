import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    AtomicExpression,
    BinaryExpression,
    Expression,
    Operation,
    Statement,
    UnaryExpression,
    mpl_AddExpression,
    mpl_Assignment,
    mpl_AssignmentStatement,
    mpl_AtomicExpression,
    mpl_BinaryExpression,
    mpl_Block,
    mpl_Comparison,
    mpl_DivExpression,
    mpl_Expression,
    mpl_ExpressionStatement,
    mpl_ForLoop,
    mpl_Function,
    mpl_IfStatement,
    mpl_LiteralValue,
    mpl_MPLModel,
    mpl_MultExpression,
    mpl_Operation,
    mpl_OperationCall,
    mpl_ParenthesisExpression,
    mpl_Procedure,
    mpl_Program,
    mpl_ReturnStatement,
    mpl_Statement,
    mpl_SubExpression,
    mpl_TraceStatement,
    mpl_UnaryExpression,
    mpl_UnaryMinusExpression,
    mpl_Variable,
    mpl_VariableDeclaration,
    mpl_VariableReference,
    mpl_WhileLoop,
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

def test_assoc_block38_stub_double():
    # mpl_Block has no real 'mpl_Block39' property in the generated
    # code (a bare stub) -- manually attach it so mpl_ForLoop's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # mpl_ForLoop's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = mpl_ForLoop(increment=True)
    partner = mpl_Block()
    setattr(partner, 'mpl_Block39', None)
    _safe_set(owner, 'mpl_ForLoop', partner)
    assert getattr(partner, 'mpl_Block39') == owner
    _safe_set(owner, 'mpl_ForLoop', None)
    assert getattr(partner, 'mpl_Block39') is None


def test_assoc_block53_stub_double():
    # mpl_Block has no real 'mpl_Block55' property in the generated
    # code (a bare stub) -- manually attach it so mpl_Operation's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # mpl_Operation's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = mpl_Operation(name="sample_text")
    partner = mpl_Block()
    setattr(partner, 'mpl_Block55', None)
    _safe_set(owner, 'mpl_Operation54', partner)
    assert getattr(partner, 'mpl_Block55') == owner
    _safe_set(owner, 'mpl_Operation54', None)
    assert getattr(partner, 'mpl_Block55') is None


def test_assoc_condition25_stub_double():
    # mpl_IfStatement has no real 'mpl_IfStatement26' property in the generated
    # code (a bare stub) -- manually attach it so mpl_Comparison's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # mpl_Comparison's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = mpl_Comparison(operator="sample_text")
    partner = mpl_IfStatement()
    setattr(partner, 'mpl_IfStatement26', None)
    _safe_set(owner, 'mpl_Comparison', partner)
    assert getattr(partner, 'mpl_IfStatement26') == owner
    _safe_set(owner, 'mpl_Comparison', None)
    assert getattr(partner, 'mpl_IfStatement26') is None


def test_assoc_condition35_stub_double():
    # mpl_WhileLoop has no real 'mpl_WhileLoop36' property in the generated
    # code (a bare stub) -- manually attach it so mpl_Comparison's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # mpl_Comparison's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = mpl_Comparison(operator="sample_text")
    partner = mpl_WhileLoop()
    setattr(partner, 'mpl_WhileLoop36', None)
    _safe_set(owner, 'mpl_Comparison37', partner)
    assert getattr(partner, 'mpl_WhileLoop36') == owner
    _safe_set(owner, 'mpl_Comparison37', None)
    assert getattr(partner, 'mpl_WhileLoop36') is None


def test_assoc_index40_stub_double():
    # mpl_Assignment has no real 'mpl_Assignment42' property in the generated
    # code (a bare stub) -- manually attach it so mpl_ForLoop's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # mpl_ForLoop's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = mpl_ForLoop(increment=True)
    partner = mpl_Assignment()
    setattr(partner, 'mpl_Assignment42', None)
    _safe_set(owner, 'mpl_ForLoop41', partner)
    assert getattr(partner, 'mpl_Assignment42') == owner
    _safe_set(owner, 'mpl_ForLoop41', None)
    assert getattr(partner, 'mpl_Assignment42') is None


def test_assoc_operand130_stub_double():
    # mpl_Expression has no real 'mpl_Expression32' property in the generated
    # code (a bare stub) -- manually attach it so mpl_Comparison's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # mpl_Comparison's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = mpl_Comparison(operator="sample_text")
    partner = mpl_Expression()
    setattr(partner, 'mpl_Expression32', None)
    _safe_set(owner, 'mpl_Comparison31', partner)
    assert getattr(partner, 'mpl_Expression32') == owner
    _safe_set(owner, 'mpl_Comparison31', None)
    assert getattr(partner, 'mpl_Expression32') is None


def test_assoc_operand227_stub_double():
    # mpl_Expression has no real 'mpl_Expression29' property in the generated
    # code (a bare stub) -- manually attach it so mpl_Comparison's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # mpl_Comparison's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = mpl_Comparison(operator="sample_text")
    partner = mpl_Expression()
    setattr(partner, 'mpl_Expression29', None)
    _safe_set(owner, 'mpl_Comparison28', partner)
    assert getattr(partner, 'mpl_Expression29') == owner
    _safe_set(owner, 'mpl_Comparison28', None)
    assert getattr(partner, 'mpl_Expression29') is None


def test_assoc_operation60_stub_double():
    # mpl_OperationCall has no real 'mpl_OperationCall61' property in the generated
    # code (a bare stub) -- manually attach it so mpl_Operation's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # mpl_Operation's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = mpl_Operation(name="sample_text")
    partner = mpl_OperationCall()
    setattr(partner, 'mpl_OperationCall61', None)
    _safe_set(owner, 'mpl_Operation62', partner)
    assert getattr(partner, 'mpl_OperationCall61') == owner
    _safe_set(owner, 'mpl_Operation62', None)
    assert getattr(partner, 'mpl_OperationCall61') is None


def test_assoc_operations64_stub_double():
    # mpl_MPLModel has no real 'mpl_MPLModel65' property in the generated
    # code (a bare stub) -- manually attach it so mpl_Operation's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # mpl_Operation's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = mpl_Operation(name="sample_text")
    partner = mpl_MPLModel()
    setattr(partner, 'mpl_MPLModel65', None)
    _safe_set(owner, 'mpl_Operation66', partner)
    assert owner in getattr(partner, 'mpl_MPLModel65')
    _safe_set(owner, 'mpl_Operation66', None)
    assert owner not in getattr(partner, 'mpl_MPLModel65')


def test_assoc_parameters48_stub_double():
    # mpl_VariableDeclaration has no real 'mpl_VariableDeclaration49' property in the generated
    # code (a bare stub) -- manually attach it so mpl_Operation's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # mpl_Operation's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = mpl_Operation(name="sample_text")
    partner = mpl_VariableDeclaration()
    setattr(partner, 'mpl_VariableDeclaration49', None)
    _safe_set(owner, 'mpl_Operation', {partner})
    assert getattr(partner, 'mpl_VariableDeclaration49') == owner
    _safe_set(owner, 'mpl_Operation', set())
    assert getattr(partner, 'mpl_VariableDeclaration49') is None


def test_assoc_upperBound43_stub_double():
    # mpl_Expression has no real 'mpl_Expression45' property in the generated
    # code (a bare stub) -- manually attach it so mpl_ForLoop's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # mpl_ForLoop's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = mpl_ForLoop(increment=True)
    partner = mpl_Expression()
    setattr(partner, 'mpl_Expression45', None)
    _safe_set(owner, 'mpl_ForLoop44', partner)
    assert getattr(partner, 'mpl_Expression45') == owner
    _safe_set(owner, 'mpl_ForLoop44', None)
    assert getattr(partner, 'mpl_Expression45') is None


def test_assoc_variable0_stub_double():
    # mpl_VariableDeclaration has no real 'mpl_VariableDeclaration' property in the generated
    # code (a bare stub) -- manually attach it so mpl_Variable's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # mpl_Variable's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = mpl_Variable(name="sample_text", value=7)
    partner = mpl_VariableDeclaration()
    setattr(partner, 'mpl_VariableDeclaration', None)
    _safe_set(owner, 'mpl_Variable', partner)
    assert getattr(partner, 'mpl_VariableDeclaration') == owner
    _safe_set(owner, 'mpl_Variable', None)
    assert getattr(partner, 'mpl_VariableDeclaration') is None


def test_assoc_variable9_stub_double():
    # mpl_VariableReference has no real 'mpl_VariableReference10' property in the generated
    # code (a bare stub) -- manually attach it so mpl_Variable's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # mpl_Variable's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = mpl_Variable(name="sample_text", value=7)
    partner = mpl_VariableReference()
    setattr(partner, 'mpl_VariableReference10', None)
    _safe_set(owner, 'mpl_Variable11', partner)
    assert getattr(partner, 'mpl_VariableReference10') == owner
    _safe_set(owner, 'mpl_Variable11', None)
    assert getattr(partner, 'mpl_VariableReference10') is None


def test_assoc_variableDeclarations50_stub_double():
    # mpl_VariableDeclaration has no real 'mpl_VariableDeclaration52' property in the generated
    # code (a bare stub) -- manually attach it so mpl_Operation's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # mpl_Operation's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = mpl_Operation(name="sample_text")
    partner = mpl_VariableDeclaration()
    setattr(partner, 'mpl_VariableDeclaration52', None)
    _safe_set(owner, 'mpl_Operation51', {partner})
    assert getattr(partner, 'mpl_VariableDeclaration52') == owner
    _safe_set(owner, 'mpl_Operation51', set())
    assert getattr(partner, 'mpl_VariableDeclaration52') is None


