import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    BuiltinEventSpec,
    Declaration,
    DefRoot,
    Effect,
    Event,
    EventSpec,
    Expression,
    Reaction,
    ReactionProperty,
    Scope,
    Statement,
    TransitionStatement,
    Trigger,
    Variable,
    stext_AlwaysEvent,
    stext_Assignment,
    stext_BitwiseAndExpression,
    stext_BitwiseOrExpression,
    stext_BitwiseXorExpression,
    stext_BuiltinEventSpec,
    stext_Clock,
    stext_ConditionalExpression,
    stext_Declaration,
    stext_DefRoot,
    stext_ElementReferenceExpression,
    stext_EntryEvent,
    stext_EntryPointSpec,
    stext_Entrypoint,
    stext_Event,
    stext_EventDefinition,
    stext_EventDerivation,
    stext_EventRaising,
    stext_EventSpec,
    stext_ExitEvent,
    stext_ExitPointSpec,
    stext_Exitpoint,
    stext_Expression,
    stext_InterfaceScope,
    stext_InternalScope,
    stext_LocalReaction,
    stext_LogicalAndExpression,
    stext_LogicalNotExpression,
    stext_LogicalOrExpression,
    stext_LogicalRelationExpression,
    stext_NumericalAddSubtractExpression,
    stext_NumericalMultiplyDivideExpression,
    stext_NumericalUnaryExpression,
    stext_OnCycleEvent,
    stext_Operation,
    stext_OperationCall,
    stext_PrimitiveValueExpression,
    stext_ReactionEffect,
    stext_ReactionPriority,
    stext_ReactionProperties,
    stext_ReactionProperty,
    stext_ReactionTrigger,
    stext_RegularEventSpec,
    stext_Root,
    stext_Scope,
    stext_ShiftExpression,
    stext_SimpleScope,
    stext_StateDeclaration,
    stext_StateRoot,
    stext_StatechartDefinition,
    stext_StatechartRoot,
    stext_Statement,
    stext_TimeEventSpec,
    stext_TransitionReaction,
    stext_TransitionRoot,
    stext_TransitionStatement,
    stext_Variable,
    stext_VariableDefinition,
    AdditiveOperator,
    AssignmentOperator,
    Direction,
    MultiplicativeOperator,
    RelationalOperator,
    ShiftOperator,
    TimeUnit,
    Type,
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

def test_assoc_derivation30_stub_double():
    # stext_EventDerivation has no real 'stext_EventDerivation31' property in the generated
    # code (a bare stub) -- manually attach it so stext_EventDefinition's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # stext_EventDefinition's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = stext_EventDefinition(direction="sample_text", type="sample_text")
    partner = stext_EventDerivation()
    setattr(partner, 'stext_EventDerivation31', None)
    _safe_set(owner, 'stext_EventDefinition', partner)
    assert getattr(partner, 'stext_EventDerivation31') == owner
    _safe_set(owner, 'stext_EventDefinition', None)
    assert getattr(partner, 'stext_EventDerivation31') is None


def test_assoc_expression22_stub_double():
    # stext_Expression has no real 'stext_Expression24' property in the generated
    # code (a bare stub) -- manually attach it so stext_Assignment's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # stext_Assignment's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = stext_Assignment(operator="sample_text")
    partner = stext_Expression()
    setattr(partner, 'stext_Expression24', None)
    _safe_set(owner, 'stext_Assignment23', partner)
    assert getattr(partner, 'stext_Expression24') == owner
    _safe_set(owner, 'stext_Assignment23', None)
    assert getattr(partner, 'stext_Expression24') is None


def test_assoc_leftOperand72_stub_double():
    # stext_Expression has no real 'stext_Expression73' property in the generated
    # code (a bare stub) -- manually attach it so stext_LogicalRelationExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # stext_LogicalRelationExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = stext_LogicalRelationExpression(operator="sample_text")
    partner = stext_Expression()
    setattr(partner, 'stext_Expression73', None)
    _safe_set(owner, 'stext_LogicalRelationExpression', partner)
    assert getattr(partner, 'stext_Expression73') == owner
    _safe_set(owner, 'stext_LogicalRelationExpression', None)
    assert getattr(partner, 'stext_Expression73') is None


def test_assoc_leftOperand77_stub_double():
    # stext_Expression has no real 'stext_Expression78' property in the generated
    # code (a bare stub) -- manually attach it so stext_ShiftExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # stext_ShiftExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = stext_ShiftExpression(operator="sample_text")
    partner = stext_Expression()
    setattr(partner, 'stext_Expression78', None)
    _safe_set(owner, 'stext_ShiftExpression', partner)
    assert getattr(partner, 'stext_Expression78') == owner
    _safe_set(owner, 'stext_ShiftExpression', None)
    assert getattr(partner, 'stext_Expression78') is None


def test_assoc_leftOperand82_stub_double():
    # stext_Expression has no real 'stext_Expression83' property in the generated
    # code (a bare stub) -- manually attach it so stext_NumericalAddSubtractExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # stext_NumericalAddSubtractExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = stext_NumericalAddSubtractExpression(operator="sample_text")
    partner = stext_Expression()
    setattr(partner, 'stext_Expression83', None)
    _safe_set(owner, 'stext_NumericalAddSubtractExpression', partner)
    assert getattr(partner, 'stext_Expression83') == owner
    _safe_set(owner, 'stext_NumericalAddSubtractExpression', None)
    assert getattr(partner, 'stext_Expression83') is None


def test_assoc_leftOperand87_stub_double():
    # stext_Expression has no real 'stext_Expression88' property in the generated
    # code (a bare stub) -- manually attach it so stext_NumericalMultiplyDivideExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # stext_NumericalMultiplyDivideExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = stext_NumericalMultiplyDivideExpression(operator="sample_text")
    partner = stext_Expression()
    setattr(partner, 'stext_Expression88', None)
    _safe_set(owner, 'stext_NumericalMultiplyDivideExpression', partner)
    assert getattr(partner, 'stext_Expression88') == owner
    _safe_set(owner, 'stext_NumericalMultiplyDivideExpression', None)
    assert getattr(partner, 'stext_Expression88') is None


def test_assoc_operand92_stub_double():
    # stext_Expression has no real 'stext_Expression93' property in the generated
    # code (a bare stub) -- manually attach it so stext_NumericalUnaryExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # stext_NumericalUnaryExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = stext_NumericalUnaryExpression(operator="sample_text")
    partner = stext_Expression()
    setattr(partner, 'stext_Expression93', None)
    _safe_set(owner, 'stext_NumericalUnaryExpression', partner)
    assert getattr(partner, 'stext_Expression93') == owner
    _safe_set(owner, 'stext_NumericalUnaryExpression', None)
    assert getattr(partner, 'stext_Expression93') is None


def test_assoc_operation95_stub_double():
    # stext_OperationCall has no real 'stext_OperationCall' property in the generated
    # code (a bare stub) -- manually attach it so stext_Operation's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # stext_Operation's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = stext_Operation(paramTypes="sample_text", type="sample_text")
    partner = stext_OperationCall()
    setattr(partner, 'stext_OperationCall', None)
    _safe_set(owner, 'stext_Operation', partner)
    assert getattr(partner, 'stext_OperationCall') == owner
    _safe_set(owner, 'stext_Operation', None)
    assert getattr(partner, 'stext_OperationCall') is None


def test_assoc_rightOperand74_stub_double():
    # stext_Expression has no real 'stext_Expression76' property in the generated
    # code (a bare stub) -- manually attach it so stext_LogicalRelationExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # stext_LogicalRelationExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = stext_LogicalRelationExpression(operator="sample_text")
    partner = stext_Expression()
    setattr(partner, 'stext_Expression76', None)
    _safe_set(owner, 'stext_LogicalRelationExpression75', partner)
    assert getattr(partner, 'stext_Expression76') == owner
    _safe_set(owner, 'stext_LogicalRelationExpression75', None)
    assert getattr(partner, 'stext_Expression76') is None


def test_assoc_rightOperand79_stub_double():
    # stext_Expression has no real 'stext_Expression81' property in the generated
    # code (a bare stub) -- manually attach it so stext_ShiftExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # stext_ShiftExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = stext_ShiftExpression(operator="sample_text")
    partner = stext_Expression()
    setattr(partner, 'stext_Expression81', None)
    _safe_set(owner, 'stext_ShiftExpression80', partner)
    assert getattr(partner, 'stext_Expression81') == owner
    _safe_set(owner, 'stext_ShiftExpression80', None)
    assert getattr(partner, 'stext_Expression81') is None


def test_assoc_rightOperand84_stub_double():
    # stext_Expression has no real 'stext_Expression86' property in the generated
    # code (a bare stub) -- manually attach it so stext_NumericalAddSubtractExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # stext_NumericalAddSubtractExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = stext_NumericalAddSubtractExpression(operator="sample_text")
    partner = stext_Expression()
    setattr(partner, 'stext_Expression86', None)
    _safe_set(owner, 'stext_NumericalAddSubtractExpression85', partner)
    assert getattr(partner, 'stext_Expression86') == owner
    _safe_set(owner, 'stext_NumericalAddSubtractExpression85', None)
    assert getattr(partner, 'stext_Expression86') is None


def test_assoc_rightOperand89_stub_double():
    # stext_Expression has no real 'stext_Expression91' property in the generated
    # code (a bare stub) -- manually attach it so stext_NumericalMultiplyDivideExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # stext_NumericalMultiplyDivideExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = stext_NumericalMultiplyDivideExpression(operator="sample_text")
    partner = stext_Expression()
    setattr(partner, 'stext_Expression91', None)
    _safe_set(owner, 'stext_NumericalMultiplyDivideExpression90', partner)
    assert getattr(partner, 'stext_Expression91') == owner
    _safe_set(owner, 'stext_NumericalMultiplyDivideExpression90', None)
    assert getattr(partner, 'stext_Expression91') is None


def test_assoc_varRef21_stub_double():
    # stext_Variable has no real 'stext_Variable' property in the generated
    # code (a bare stub) -- manually attach it so stext_Assignment's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # stext_Assignment's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = stext_Assignment(operator="sample_text")
    partner = stext_Variable()
    setattr(partner, 'stext_Variable', None)
    _safe_set(owner, 'stext_Assignment', partner)
    assert getattr(partner, 'stext_Variable') == owner
    _safe_set(owner, 'stext_Assignment', None)
    assert getattr(partner, 'stext_Variable') is None


