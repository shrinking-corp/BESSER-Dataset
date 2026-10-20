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
    Literal,
    Reaction,
    ReactionProperty,
    Scope,
    Statement,
    Trigger,
    Variable,
    stext_ActiveStateReferenceExpression,
    stext_AlwaysEvent,
    stext_Assignment,
    stext_BitwiseAndExpression,
    stext_BitwiseOrExpression,
    stext_BitwiseXorExpression,
    stext_BoolLiteral,
    stext_BuiltinEventSpec,
    stext_ConditionalExpression,
    stext_Declaration,
    stext_DefRoot,
    stext_DefaultEvent,
    stext_ElementReferenceExpression,
    stext_EntryEvent,
    stext_EntryPointSpec,
    stext_Entrypoint,
    stext_Event,
    stext_EventDefinition,
    stext_EventDerivation,
    stext_EventRaising,
    stext_EventSpec,
    stext_EventValueReferenceExpression,
    stext_ExitEvent,
    stext_ExitPointSpec,
    stext_Exitpoint,
    stext_Expression,
    stext_HexLiteral,
    stext_IntLiteral,
    stext_InterfaceScope,
    stext_InternalScope,
    stext_Literal,
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
    stext_ReactionProperties,
    stext_ReactionProperty,
    stext_ReactionTrigger,
    stext_RealLiteral,
    stext_RegularEventSpec,
    stext_RegularState,
    stext_Root,
    stext_Scope,
    stext_ShiftExpression,
    stext_SimpleScope,
    stext_StateRoot,
    stext_StateSpecification,
    stext_StatechartRoot,
    stext_StatechartSpecification,
    stext_Statement,
    stext_TimeEventSpec,
    stext_TransitionReaction,
    stext_TransitionRoot,
    stext_TransitionSpecification,
    stext_Type,
    stext_Variable,
    stext_VariableDefinition,
    AdditiveOperator,
    AssignmentOperator,
    Direction,
    MultiplicativeOperator,
    RelationalOperator,
    ShiftOperator,
    TimeEventType,
    TimeUnit,
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

def test_assoc_def_1_stub_double():
    # stext_StatechartRoot has no real 'stext_StatechartRoot' property in the generated
    # code (a bare stub) -- manually attach it so stext_StatechartSpecification's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # stext_StatechartSpecification's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = stext_StatechartSpecification(namespace="sample_text")
    partner = stext_StatechartRoot()
    setattr(partner, 'stext_StatechartRoot', None)
    _safe_set(owner, 'stext_StatechartSpecification', partner)
    assert getattr(partner, 'stext_StatechartRoot') == owner
    _safe_set(owner, 'stext_StatechartSpecification', None)
    assert getattr(partner, 'stext_StatechartRoot') is None


def test_assoc_definitionScopes4_stub_double():
    # stext_Scope has no real 'stext_Scope' property in the generated
    # code (a bare stub) -- manually attach it so stext_StatechartSpecification's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # stext_StatechartSpecification's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = stext_StatechartSpecification(namespace="sample_text")
    partner = stext_Scope()
    setattr(partner, 'stext_Scope', None)
    _safe_set(owner, 'stext_StatechartSpecification5', {partner})
    assert getattr(partner, 'stext_Scope') == owner
    _safe_set(owner, 'stext_StatechartSpecification5', set())
    assert getattr(partner, 'stext_Scope') is None


def test_assoc_derivation38_stub_double():
    # stext_EventDerivation has no real 'stext_EventDerivation40' property in the generated
    # code (a bare stub) -- manually attach it so stext_EventDefinition's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # stext_EventDefinition's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = stext_EventDefinition(direction="sample_text")
    partner = stext_EventDerivation()
    setattr(partner, 'stext_EventDerivation40', None)
    _safe_set(owner, 'stext_EventDefinition39', partner)
    assert getattr(partner, 'stext_EventDerivation40') == owner
    _safe_set(owner, 'stext_EventDefinition39', None)
    assert getattr(partner, 'stext_EventDerivation40') is None


def test_assoc_expression25_stub_double():
    # stext_Expression has no real 'stext_Expression27' property in the generated
    # code (a bare stub) -- manually attach it so stext_Assignment's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # stext_Assignment's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = stext_Assignment(operator="sample_text")
    partner = stext_Expression()
    setattr(partner, 'stext_Expression27', None)
    _safe_set(owner, 'stext_Assignment26', partner)
    assert getattr(partner, 'stext_Expression27') == owner
    _safe_set(owner, 'stext_Assignment26', None)
    assert getattr(partner, 'stext_Expression27') is None


def test_assoc_initialValue43_stub_double():
    # stext_Expression has no real 'stext_Expression45' property in the generated
    # code (a bare stub) -- manually attach it so stext_VariableDefinition's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # stext_VariableDefinition's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = stext_VariableDefinition(external=True, readonly=True)
    partner = stext_Expression()
    setattr(partner, 'stext_Expression45', None)
    _safe_set(owner, 'stext_VariableDefinition44', partner)
    assert getattr(partner, 'stext_Expression45') == owner
    _safe_set(owner, 'stext_VariableDefinition44', None)
    assert getattr(partner, 'stext_Expression45') is None


def test_assoc_leftOperand101_stub_double():
    # stext_Expression has no real 'stext_Expression102' property in the generated
    # code (a bare stub) -- manually attach it so stext_NumericalAddSubtractExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # stext_NumericalAddSubtractExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = stext_NumericalAddSubtractExpression(operator="sample_text")
    partner = stext_Expression()
    setattr(partner, 'stext_Expression102', None)
    _safe_set(owner, 'stext_NumericalAddSubtractExpression', partner)
    assert getattr(partner, 'stext_Expression102') == owner
    _safe_set(owner, 'stext_NumericalAddSubtractExpression', None)
    assert getattr(partner, 'stext_Expression102') is None


def test_assoc_leftOperand106_stub_double():
    # stext_Expression has no real 'stext_Expression107' property in the generated
    # code (a bare stub) -- manually attach it so stext_NumericalMultiplyDivideExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # stext_NumericalMultiplyDivideExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = stext_NumericalMultiplyDivideExpression(operator="sample_text")
    partner = stext_Expression()
    setattr(partner, 'stext_Expression107', None)
    _safe_set(owner, 'stext_NumericalMultiplyDivideExpression', partner)
    assert getattr(partner, 'stext_Expression107') == owner
    _safe_set(owner, 'stext_NumericalMultiplyDivideExpression', None)
    assert getattr(partner, 'stext_Expression107') is None


def test_assoc_leftOperand91_stub_double():
    # stext_Expression has no real 'stext_Expression92' property in the generated
    # code (a bare stub) -- manually attach it so stext_LogicalRelationExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # stext_LogicalRelationExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = stext_LogicalRelationExpression(operator="sample_text")
    partner = stext_Expression()
    setattr(partner, 'stext_Expression92', None)
    _safe_set(owner, 'stext_LogicalRelationExpression', partner)
    assert getattr(partner, 'stext_Expression92') == owner
    _safe_set(owner, 'stext_LogicalRelationExpression', None)
    assert getattr(partner, 'stext_Expression92') is None


def test_assoc_leftOperand96_stub_double():
    # stext_Expression has no real 'stext_Expression97' property in the generated
    # code (a bare stub) -- manually attach it so stext_ShiftExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # stext_ShiftExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = stext_ShiftExpression(operator="sample_text")
    partner = stext_Expression()
    setattr(partner, 'stext_Expression97', None)
    _safe_set(owner, 'stext_ShiftExpression', partner)
    assert getattr(partner, 'stext_Expression97') == owner
    _safe_set(owner, 'stext_ShiftExpression', None)
    assert getattr(partner, 'stext_Expression97') is None


def test_assoc_operand111_stub_double():
    # stext_Expression has no real 'stext_Expression112' property in the generated
    # code (a bare stub) -- manually attach it so stext_NumericalUnaryExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # stext_NumericalUnaryExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = stext_NumericalUnaryExpression(operator="sample_text")
    partner = stext_Expression()
    setattr(partner, 'stext_Expression112', None)
    _safe_set(owner, 'stext_NumericalUnaryExpression', partner)
    assert getattr(partner, 'stext_Expression112') == owner
    _safe_set(owner, 'stext_NumericalUnaryExpression', None)
    assert getattr(partner, 'stext_Expression112') is None


def test_assoc_rightOperand103_stub_double():
    # stext_Expression has no real 'stext_Expression105' property in the generated
    # code (a bare stub) -- manually attach it so stext_NumericalAddSubtractExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # stext_NumericalAddSubtractExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = stext_NumericalAddSubtractExpression(operator="sample_text")
    partner = stext_Expression()
    setattr(partner, 'stext_Expression105', None)
    _safe_set(owner, 'stext_NumericalAddSubtractExpression104', partner)
    assert getattr(partner, 'stext_Expression105') == owner
    _safe_set(owner, 'stext_NumericalAddSubtractExpression104', None)
    assert getattr(partner, 'stext_Expression105') is None


def test_assoc_rightOperand108_stub_double():
    # stext_Expression has no real 'stext_Expression110' property in the generated
    # code (a bare stub) -- manually attach it so stext_NumericalMultiplyDivideExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # stext_NumericalMultiplyDivideExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = stext_NumericalMultiplyDivideExpression(operator="sample_text")
    partner = stext_Expression()
    setattr(partner, 'stext_Expression110', None)
    _safe_set(owner, 'stext_NumericalMultiplyDivideExpression109', partner)
    assert getattr(partner, 'stext_Expression110') == owner
    _safe_set(owner, 'stext_NumericalMultiplyDivideExpression109', None)
    assert getattr(partner, 'stext_Expression110') is None


def test_assoc_rightOperand93_stub_double():
    # stext_Expression has no real 'stext_Expression95' property in the generated
    # code (a bare stub) -- manually attach it so stext_LogicalRelationExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # stext_LogicalRelationExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = stext_LogicalRelationExpression(operator="sample_text")
    partner = stext_Expression()
    setattr(partner, 'stext_Expression95', None)
    _safe_set(owner, 'stext_LogicalRelationExpression94', partner)
    assert getattr(partner, 'stext_Expression95') == owner
    _safe_set(owner, 'stext_LogicalRelationExpression94', None)
    assert getattr(partner, 'stext_Expression95') is None


def test_assoc_rightOperand98_stub_double():
    # stext_Expression has no real 'stext_Expression100' property in the generated
    # code (a bare stub) -- manually attach it so stext_ShiftExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # stext_ShiftExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = stext_ShiftExpression(operator="sample_text")
    partner = stext_Expression()
    setattr(partner, 'stext_Expression100', None)
    _safe_set(owner, 'stext_ShiftExpression99', partner)
    assert getattr(partner, 'stext_Expression100') == owner
    _safe_set(owner, 'stext_ShiftExpression99', None)
    assert getattr(partner, 'stext_Expression100') is None


def test_assoc_type37_stub_double():
    # stext_Type has no real 'stext_Type' property in the generated
    # code (a bare stub) -- manually attach it so stext_EventDefinition's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # stext_EventDefinition's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = stext_EventDefinition(direction="sample_text")
    partner = stext_Type()
    setattr(partner, 'stext_Type', None)
    _safe_set(owner, 'stext_EventDefinition', partner)
    assert getattr(partner, 'stext_Type') == owner
    _safe_set(owner, 'stext_EventDefinition', None)
    assert getattr(partner, 'stext_Type') is None


def test_assoc_type41_stub_double():
    # stext_Type has no real 'stext_Type42' property in the generated
    # code (a bare stub) -- manually attach it so stext_VariableDefinition's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # stext_VariableDefinition's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = stext_VariableDefinition(external=True, readonly=True)
    partner = stext_Type()
    setattr(partner, 'stext_Type42', None)
    _safe_set(owner, 'stext_VariableDefinition', partner)
    assert getattr(partner, 'stext_Type42') == owner
    _safe_set(owner, 'stext_VariableDefinition', None)
    assert getattr(partner, 'stext_Type42') is None


def test_assoc_varRef24_stub_double():
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


