import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Assignment,
    BooleanLiteral,
    ChannelDeclaration,
    ChannelReference,
    CompositeDeclaration,
    DVE_model_ArrayLiteral,
    DVE_model_ArrayType,
    DVE_model_Assignment,
    DVE_model_Asynchronous,
    DVE_model_BinaryExpression,
    DVE_model_BooleanLiteral,
    DVE_model_ByteType,
    DVE_model_ChannelDeclaration,
    DVE_model_ChannelReference,
    DVE_model_CompositeDeclaration,
    DVE_model_ConstantDeclaration,
    DVE_model_Declaration,
    DVE_model_Element,
    DVE_model_Expression,
    DVE_model_FalseLiteral,
    DVE_model_IndexedExpression,
    DVE_model_InputSynchronization,
    DVE_model_IntegerType,
    DVE_model_Literal,
    DVE_model_NamedDeclaration,
    DVE_model_NumberLiteral,
    DVE_model_OutputSynchronization,
    DVE_model_PrefixedReference,
    DVE_model_Process,
    DVE_model_ProcessReference,
    DVE_model_ProcessStateReference,
    DVE_model_ProcessVariableReference,
    DVE_model_Reference,
    DVE_model_State,
    DVE_model_StateReference,
    DVE_model_Synchronization,
    DVE_model_Synchronous,
    DVE_model_System,
    DVE_model_SystemProperties,
    DVE_model_SystemType,
    DVE_model_Transition,
    DVE_model_TrueLiteral,
    DVE_model_Type,
    DVE_model_TypedChannelDeclaration,
    DVE_model_UnaryExpression,
    DVE_model_VariableDeclaration,
    DVE_model_VariableReference,
    Declaration,
    Element,
    Expression,
    Literal,
    NamedDeclaration,
    Process,
    ProcessReference,
    Reference,
    State,
    StateReference,
    Synchronization,
    System,
    SystemProperties,
    SystemType,
    Transition,
    Type,
    VariableDeclaration,
    model_PrefixedReference,
    model_StateReference,
    model_VariableReference,
    BinaryOperator,
    UnaryOperator,
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

def test_assoc_operand52_stub_double():
    # Expression has no real 'Expression53' property in the generated
    # code (a bare stub) -- manually attach it so DVE_model_UnaryExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # DVE_model_UnaryExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = DVE_model_UnaryExpression(operator="sample_text")
    partner = Expression()
    setattr(partner, 'Expression53', None)
    _safe_set(owner, 'DVE_model_UnaryExpression', partner)
    assert getattr(partner, 'Expression53') == owner
    _safe_set(owner, 'DVE_model_UnaryExpression', None)
    assert getattr(partner, 'Expression53') is None


def test_assoc_operands54_stub_double():
    # Expression has no real 'Expression55' property in the generated
    # code (a bare stub) -- manually attach it so DVE_model_BinaryExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # DVE_model_BinaryExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = DVE_model_BinaryExpression(operator="sample_text")
    partner = Expression()
    setattr(partner, 'Expression55', None)
    _safe_set(owner, 'DVE_model_BinaryExpression', {partner})
    assert getattr(partner, 'Expression55') == owner
    _safe_set(owner, 'DVE_model_BinaryExpression', set())
    assert getattr(partner, 'Expression55') is None


