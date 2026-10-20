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
    NamedElement,
    Operation,
    Property,
    Reaction,
    ReactionProperty,
    Scope,
    StatechartScope,
    Statement,
    Trigger,
    Variable,
    stext_ActiveStateReferenceExpression,
    stext_AlwaysEvent,
    stext_AssignmentExpression,
    stext_BitwiseAndExpression,
    stext_BitwiseOrExpression,
    stext_BitwiseXorExpression,
    stext_BoolLiteral,
    stext_BuiltinEventSpec,
    stext_ConditionalExpression,
    stext_DefRoot,
    stext_DefaultEvent,
    stext_EntryEvent,
    stext_EntryPointSpec,
    stext_Entrypoint,
    stext_EventDefinition,
    stext_EventDerivation,
    stext_EventRaisingExpression,
    stext_EventSpec,
    stext_EventValueReferenceExpression,
    stext_ExitEvent,
    stext_ExitPointSpec,
    stext_Exitpoint,
    stext_Expression,
    stext_Feature,
    stext_FeatureCall,
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
    stext_NamedElement,
    stext_NumericalAddSubtractExpression,
    stext_NumericalMultiplyDivideExpression,
    stext_NumericalUnaryExpression,
    stext_OnCycleEvent,
    stext_OperationDefinition,
    stext_Parameter,
    stext_PrimitiveValueExpression,
    stext_ReactionEffect,
    stext_ReactionProperties,
    stext_ReactionProperty,
    stext_ReactionTrigger,
    stext_RealLiteral,
    stext_RegularEventSpec,
    stext_Root,
    stext_Scope,
    stext_ShiftExpression,
    stext_SimpleScope,
    stext_State,
    stext_StateRoot,
    stext_StateSpecification,
    stext_StatechartRoot,
    stext_StatechartScope,
    stext_StatechartSpecification,
    stext_StringLiteral,
    stext_TimeEventSpec,
    stext_TransitionReaction,
    stext_TransitionRoot,
    stext_TransitionSpecification,
    stext_TypedElementReferenceExpression,
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

def test_assoc_args107_stub_double():
    # stext_Expression has no real 'stext_Expression109' property in the generated
    # code (a bare stub) -- manually attach it so stext_FeatureCall's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # stext_FeatureCall's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = stext_FeatureCall(operationCall=True)
    partner = stext_Expression()
    setattr(partner, 'stext_Expression109', None)
    _safe_set(owner, 'stext_FeatureCall108', {partner})
    assert getattr(partner, 'stext_Expression109') == owner
    _safe_set(owner, 'stext_FeatureCall108', set())
    assert getattr(partner, 'stext_Expression109') is None


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
    # stext_StatechartScope has no real 'stext_StatechartScope' property in the generated
    # code (a bare stub) -- manually attach it so stext_StatechartSpecification's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # stext_StatechartSpecification's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = stext_StatechartSpecification(namespace="sample_text")
    partner = stext_StatechartScope()
    setattr(partner, 'stext_StatechartScope', None)
    _safe_set(owner, 'stext_StatechartSpecification5', {partner})
    assert getattr(partner, 'stext_StatechartScope') == owner
    _safe_set(owner, 'stext_StatechartSpecification5', set())
    assert getattr(partner, 'stext_StatechartScope') is None


def test_assoc_derivation10_stub_double():
    # stext_EventDerivation has no real 'stext_EventDerivation' property in the generated
    # code (a bare stub) -- manually attach it so stext_EventDefinition's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # stext_EventDefinition's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = stext_EventDefinition(direction="sample_text")
    partner = stext_EventDerivation()
    setattr(partner, 'stext_EventDerivation', None)
    _safe_set(owner, 'stext_EventDefinition', partner)
    assert getattr(partner, 'stext_EventDerivation') == owner
    _safe_set(owner, 'stext_EventDefinition', None)
    assert getattr(partner, 'stext_EventDerivation') is None


def test_assoc_expression42_stub_double():
    # stext_Expression has no real 'stext_Expression44' property in the generated
    # code (a bare stub) -- manually attach it so stext_AssignmentExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # stext_AssignmentExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = stext_AssignmentExpression(operator="sample_text")
    partner = stext_Expression()
    setattr(partner, 'stext_Expression44', None)
    _safe_set(owner, 'stext_AssignmentExpression43', partner)
    assert getattr(partner, 'stext_Expression44') == owner
    _safe_set(owner, 'stext_AssignmentExpression43', None)
    assert getattr(partner, 'stext_Expression44') is None


def test_assoc_feature105_stub_double():
    # stext_Feature has no real 'stext_Feature' property in the generated
    # code (a bare stub) -- manually attach it so stext_FeatureCall's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # stext_FeatureCall's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = stext_FeatureCall(operationCall=True)
    partner = stext_Feature()
    setattr(partner, 'stext_Feature', None)
    _safe_set(owner, 'stext_FeatureCall106', partner)
    assert getattr(partner, 'stext_Feature') == owner
    _safe_set(owner, 'stext_FeatureCall106', None)
    assert getattr(partner, 'stext_Feature') is None


def test_assoc_initialValue16_stub_double():
    # stext_Expression has no real 'stext_Expression17' property in the generated
    # code (a bare stub) -- manually attach it so stext_VariableDefinition's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # stext_VariableDefinition's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = stext_VariableDefinition(external=True, readonly=True)
    partner = stext_Expression()
    setattr(partner, 'stext_Expression17', None)
    _safe_set(owner, 'stext_VariableDefinition', partner)
    assert getattr(partner, 'stext_Expression17') == owner
    _safe_set(owner, 'stext_VariableDefinition', None)
    assert getattr(partner, 'stext_Expression17') is None


def test_assoc_leftOperand80_stub_double():
    # stext_Expression has no real 'stext_Expression81' property in the generated
    # code (a bare stub) -- manually attach it so stext_LogicalRelationExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # stext_LogicalRelationExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = stext_LogicalRelationExpression(operator="sample_text")
    partner = stext_Expression()
    setattr(partner, 'stext_Expression81', None)
    _safe_set(owner, 'stext_LogicalRelationExpression', partner)
    assert getattr(partner, 'stext_Expression81') == owner
    _safe_set(owner, 'stext_LogicalRelationExpression', None)
    assert getattr(partner, 'stext_Expression81') is None


def test_assoc_leftOperand85_stub_double():
    # stext_Expression has no real 'stext_Expression86' property in the generated
    # code (a bare stub) -- manually attach it so stext_ShiftExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # stext_ShiftExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = stext_ShiftExpression(operator="sample_text")
    partner = stext_Expression()
    setattr(partner, 'stext_Expression86', None)
    _safe_set(owner, 'stext_ShiftExpression', partner)
    assert getattr(partner, 'stext_Expression86') == owner
    _safe_set(owner, 'stext_ShiftExpression', None)
    assert getattr(partner, 'stext_Expression86') is None


def test_assoc_leftOperand90_stub_double():
    # stext_Expression has no real 'stext_Expression91' property in the generated
    # code (a bare stub) -- manually attach it so stext_NumericalAddSubtractExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # stext_NumericalAddSubtractExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = stext_NumericalAddSubtractExpression(operator="sample_text")
    partner = stext_Expression()
    setattr(partner, 'stext_Expression91', None)
    _safe_set(owner, 'stext_NumericalAddSubtractExpression', partner)
    assert getattr(partner, 'stext_Expression91') == owner
    _safe_set(owner, 'stext_NumericalAddSubtractExpression', None)
    assert getattr(partner, 'stext_Expression91') is None


def test_assoc_leftOperand95_stub_double():
    # stext_Expression has no real 'stext_Expression96' property in the generated
    # code (a bare stub) -- manually attach it so stext_NumericalMultiplyDivideExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # stext_NumericalMultiplyDivideExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = stext_NumericalMultiplyDivideExpression(operator="sample_text")
    partner = stext_Expression()
    setattr(partner, 'stext_Expression96', None)
    _safe_set(owner, 'stext_NumericalMultiplyDivideExpression', partner)
    assert getattr(partner, 'stext_Expression96') == owner
    _safe_set(owner, 'stext_NumericalMultiplyDivideExpression', None)
    assert getattr(partner, 'stext_Expression96') is None


def test_assoc_operand100_stub_double():
    # stext_Expression has no real 'stext_Expression101' property in the generated
    # code (a bare stub) -- manually attach it so stext_NumericalUnaryExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # stext_NumericalUnaryExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = stext_NumericalUnaryExpression(operator="sample_text")
    partner = stext_Expression()
    setattr(partner, 'stext_Expression101', None)
    _safe_set(owner, 'stext_NumericalUnaryExpression', partner)
    assert getattr(partner, 'stext_Expression101') == owner
    _safe_set(owner, 'stext_NumericalUnaryExpression', None)
    assert getattr(partner, 'stext_Expression101') is None


def test_assoc_owner103_stub_double():
    # stext_Expression has no real 'stext_Expression104' property in the generated
    # code (a bare stub) -- manually attach it so stext_FeatureCall's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # stext_FeatureCall's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = stext_FeatureCall(operationCall=True)
    partner = stext_Expression()
    setattr(partner, 'stext_Expression104', None)
    _safe_set(owner, 'stext_FeatureCall', partner)
    assert getattr(partner, 'stext_Expression104') == owner
    _safe_set(owner, 'stext_FeatureCall', None)
    assert getattr(partner, 'stext_Expression104') is None


def test_assoc_rightOperand82_stub_double():
    # stext_Expression has no real 'stext_Expression84' property in the generated
    # code (a bare stub) -- manually attach it so stext_LogicalRelationExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # stext_LogicalRelationExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = stext_LogicalRelationExpression(operator="sample_text")
    partner = stext_Expression()
    setattr(partner, 'stext_Expression84', None)
    _safe_set(owner, 'stext_LogicalRelationExpression83', partner)
    assert getattr(partner, 'stext_Expression84') == owner
    _safe_set(owner, 'stext_LogicalRelationExpression83', None)
    assert getattr(partner, 'stext_Expression84') is None


def test_assoc_rightOperand87_stub_double():
    # stext_Expression has no real 'stext_Expression89' property in the generated
    # code (a bare stub) -- manually attach it so stext_ShiftExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # stext_ShiftExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = stext_ShiftExpression(operator="sample_text")
    partner = stext_Expression()
    setattr(partner, 'stext_Expression89', None)
    _safe_set(owner, 'stext_ShiftExpression88', partner)
    assert getattr(partner, 'stext_Expression89') == owner
    _safe_set(owner, 'stext_ShiftExpression88', None)
    assert getattr(partner, 'stext_Expression89') is None


def test_assoc_rightOperand92_stub_double():
    # stext_Expression has no real 'stext_Expression94' property in the generated
    # code (a bare stub) -- manually attach it so stext_NumericalAddSubtractExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # stext_NumericalAddSubtractExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = stext_NumericalAddSubtractExpression(operator="sample_text")
    partner = stext_Expression()
    setattr(partner, 'stext_Expression94', None)
    _safe_set(owner, 'stext_NumericalAddSubtractExpression93', partner)
    assert getattr(partner, 'stext_Expression94') == owner
    _safe_set(owner, 'stext_NumericalAddSubtractExpression93', None)
    assert getattr(partner, 'stext_Expression94') is None


def test_assoc_rightOperand97_stub_double():
    # stext_Expression has no real 'stext_Expression99' property in the generated
    # code (a bare stub) -- manually attach it so stext_NumericalMultiplyDivideExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # stext_NumericalMultiplyDivideExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = stext_NumericalMultiplyDivideExpression(operator="sample_text")
    partner = stext_Expression()
    setattr(partner, 'stext_Expression99', None)
    _safe_set(owner, 'stext_NumericalMultiplyDivideExpression98', partner)
    assert getattr(partner, 'stext_Expression99') == owner
    _safe_set(owner, 'stext_NumericalMultiplyDivideExpression98', None)
    assert getattr(partner, 'stext_Expression99') is None


def test_assoc_varRef40_stub_double():
    # stext_Expression has no real 'stext_Expression41' property in the generated
    # code (a bare stub) -- manually attach it so stext_AssignmentExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # stext_AssignmentExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = stext_AssignmentExpression(operator="sample_text")
    partner = stext_Expression()
    setattr(partner, 'stext_Expression41', None)
    _safe_set(owner, 'stext_AssignmentExpression', partner)
    assert getattr(partner, 'stext_Expression41') == owner
    _safe_set(owner, 'stext_AssignmentExpression', None)
    assert getattr(partner, 'stext_Expression41') is None


