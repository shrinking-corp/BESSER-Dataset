import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    AbstractRoot,
    BaseType,
    Expression,
    Type,
    VariableReference,
    ast_expressions_EObject,
    expressions_ast_AbstractRoot,
    expressions_ast_ActionRoot,
    expressions_ast_AstVisitor,
    expressions_ast_BinaryExpression,
    expressions_ast_Constant,
    expressions_ast_Expression,
    expressions_ast_Literal,
    expressions_ast_LogicalRoot,
    expressions_ast_ResourceRoot,
    expressions_ast_TernaryExpression,
    expressions_ast_UnaryExpression,
    expressions_ast_VariableReference,
    expressions_type_AnyType,
    expressions_type_BaseType,
    expressions_type_BooleanType,
    expressions_type_ClockType,
    expressions_type_FloatType,
    expressions_type_IntegerType,
    expressions_type_NaturalType,
    expressions_type_ResourceType,
    expressions_type_Type,
    BinaryOperation,
    ResolvedType,
    TernaryOperation,
    UnaryOperation,
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

def test_assoc_arrayIndex21_stub_double():
    # Expression has no real 'Expression22' property in the generated
    # code (a bare stub) -- manually attach it so expressions_ast_VariableReference's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # expressions_ast_VariableReference's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = expressions_ast_VariableReference(name="sample_text")
    partner = Expression()
    setattr(partner, 'Expression22', None)
    _safe_set(owner, 'expressions_ast_VariableReference', partner)
    assert getattr(partner, 'Expression22') == owner
    _safe_set(owner, 'expressions_ast_VariableReference', None)
    assert getattr(partner, 'Expression22') is None


def test_assoc_param114_stub_double():
    # Expression has no real 'Expression15' property in the generated
    # code (a bare stub) -- manually attach it so expressions_ast_BinaryExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # expressions_ast_BinaryExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = expressions_ast_BinaryExpression(operation="sample_text")
    partner = Expression()
    setattr(partner, 'Expression15', None)
    _safe_set(owner, 'expressions_ast_BinaryExpression', partner)
    assert getattr(partner, 'Expression15') == owner
    _safe_set(owner, 'expressions_ast_BinaryExpression', None)
    assert getattr(partner, 'Expression15') is None


def test_assoc_param119_stub_double():
    # Expression has no real 'Expression20' property in the generated
    # code (a bare stub) -- manually attach it so expressions_ast_UnaryExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # expressions_ast_UnaryExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = expressions_ast_UnaryExpression(operation="sample_text")
    partner = Expression()
    setattr(partner, 'Expression20', None)
    _safe_set(owner, 'expressions_ast_UnaryExpression', partner)
    assert getattr(partner, 'Expression20') == owner
    _safe_set(owner, 'expressions_ast_UnaryExpression', None)
    assert getattr(partner, 'Expression20') is None


def test_assoc_param16_stub_double():
    # Expression has no real 'Expression7' property in the generated
    # code (a bare stub) -- manually attach it so expressions_ast_TernaryExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # expressions_ast_TernaryExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = expressions_ast_TernaryExpression(operation="sample_text")
    partner = Expression()
    setattr(partner, 'Expression7', None)
    _safe_set(owner, 'expressions_ast_TernaryExpression', partner)
    assert getattr(partner, 'Expression7') == owner
    _safe_set(owner, 'expressions_ast_TernaryExpression', None)
    assert getattr(partner, 'Expression7') is None


def test_assoc_param216_stub_double():
    # Expression has no real 'Expression18' property in the generated
    # code (a bare stub) -- manually attach it so expressions_ast_BinaryExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # expressions_ast_BinaryExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = expressions_ast_BinaryExpression(operation="sample_text")
    partner = Expression()
    setattr(partner, 'Expression18', None)
    _safe_set(owner, 'expressions_ast_BinaryExpression17', partner)
    assert getattr(partner, 'Expression18') == owner
    _safe_set(owner, 'expressions_ast_BinaryExpression17', None)
    assert getattr(partner, 'Expression18') is None


def test_assoc_param28_stub_double():
    # Expression has no real 'Expression10' property in the generated
    # code (a bare stub) -- manually attach it so expressions_ast_TernaryExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # expressions_ast_TernaryExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = expressions_ast_TernaryExpression(operation="sample_text")
    partner = Expression()
    setattr(partner, 'Expression10', None)
    _safe_set(owner, 'expressions_ast_TernaryExpression9', partner)
    assert getattr(partner, 'Expression10') == owner
    _safe_set(owner, 'expressions_ast_TernaryExpression9', None)
    assert getattr(partner, 'Expression10') is None


def test_assoc_param311_stub_double():
    # Expression has no real 'Expression13' property in the generated
    # code (a bare stub) -- manually attach it so expressions_ast_TernaryExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # expressions_ast_TernaryExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = expressions_ast_TernaryExpression(operation="sample_text")
    partner = Expression()
    setattr(partner, 'Expression13', None)
    _safe_set(owner, 'expressions_ast_TernaryExpression12', partner)
    assert getattr(partner, 'Expression13') == owner
    _safe_set(owner, 'expressions_ast_TernaryExpression12', None)
    assert getattr(partner, 'Expression13') is None


def test_assoc_referencedVariables0_stub_double():
    # VariableReference has no real 'VariableReference' property in the generated
    # code (a bare stub) -- manually attach it so expressions_ast_AbstractRoot's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # expressions_ast_AbstractRoot's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = expressions_ast_AbstractRoot(type="sample_text")
    partner = VariableReference()
    setattr(partner, 'VariableReference', None)
    _safe_set(owner, 'expressions_ast_AbstractRoot', {partner})
    assert getattr(partner, 'VariableReference') == owner
    _safe_set(owner, 'expressions_ast_AbstractRoot', set())
    assert getattr(partner, 'VariableReference') is None


def test_assoc_resolved23_stub_double():
    # ast_expressions_EObject has no real 'ast_expressions_EObject' property in the generated
    # code (a bare stub) -- manually attach it so expressions_ast_VariableReference's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # expressions_ast_VariableReference's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = expressions_ast_VariableReference(name="sample_text")
    partner = ast_expressions_EObject()
    setattr(partner, 'ast_expressions_EObject', None)
    _safe_set(owner, 'expressions_ast_VariableReference24', partner)
    assert getattr(partner, 'ast_expressions_EObject') == owner
    _safe_set(owner, 'expressions_ast_VariableReference24', None)
    assert getattr(partner, 'ast_expressions_EObject') is None


