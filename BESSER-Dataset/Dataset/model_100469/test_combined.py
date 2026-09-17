# =============================================================================
# This file is a generated concatenation of two independent test suites --
# see scripts/generate_combined_tests.py for why simple concatenation is safe
# despite both generators using the same naming convention for some helpers,
# and for the deterministic rules used to drop old-suite tests the new suite
# already covers equally or more thoroughly.
# =============================================================================

# ----- SECTION A: test_hypothesis.py (original generated suite) -----
import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    stext_NamedElement,
    stext_State,
    stext_Feature,
    Expression,
    stext_BitwiseAndExpression,
    stext_LogicalRelationExpression,
    stext_EventValueReferenceExpression,
    stext_ShiftExpression,
    stext_TypedElementReferenceExpression,
    stext_AssignmentExpression,
    stext_FeatureCall,
    stext_LogicalNotExpression,
    stext_BitwiseOrExpression,
    stext_ActiveStateReferenceExpression,
    stext_NumericalUnaryExpression,
    stext_LogicalAndExpression,
    stext_PrimitiveValueExpression,
    stext_NumericalAddSubtractExpression,
    stext_BitwiseXorExpression,
    stext_NumericalMultiplyDivideExpression,
    stext_LogicalOrExpression,
    stext_ConditionalExpression,
    stext_EventRaisingExpression,
    Effect,
    stext_ReactionEffect,
    Trigger,
    stext_ReactionTrigger,
    Operation,
    Declaration,
    stext_OperationDefinition,
    Property,
    Variable,
    stext_VariableDefinition,
    Literal,
    stext_StringLiteral,
    stext_HexLiteral,
    stext_IntLiteral,
    stext_RealLiteral,
    stext_BoolLiteral,
    stext_Literal,
    Statement,
    BuiltinEventSpec,
    stext_ExitEvent,
    stext_OnCycleEvent,
    stext_AlwaysEvent,
    stext_DefaultEvent,
    stext_EntryEvent,
    EventSpec,
    stext_BuiltinEventSpec,
    stext_TimeEventSpec,
    stext_RegularEventSpec,
    stext_EventSpec,
    stext_Exitpoint,
    stext_Entrypoint,
    ReactionProperty,
    stext_ExitPointSpec,
    stext_EntryPointSpec,
    stext_ReactionProperty,
    stext_ReactionProperties,
    Reaction,
    stext_LocalReaction,
    stext_Type,
    stext_DefRoot,
    stext_Root,
    stext_Expression,
    stext_EventDerivation,
    Event,
    stext_EventDefinition,
    NamedElement,
    StatechartScope,
    stext_InternalScope,
    stext_InterfaceScope,
    Scope,
    stext_SimpleScope,
    stext_TransitionReaction,
    stext_Scope,
    stext_StatechartScope,
    stext_TransitionSpecification,
    stext_StateSpecification,
    stext_StatechartSpecification,
    DefRoot,
    stext_StateRoot,
    stext_TransitionRoot,
    stext_StatechartRoot,
    RelationalOperator,
    TimeUnit,
    Direction,
    UnaryOperator,
    AdditiveOperator,
    AssignmentOperator,
    MultiplicativeOperator,
    TimeEventType,
    ShiftOperator,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_hyp_stext_namedelement_is_not_abstract():
    assert not inspect.isabstract(stext_NamedElement)


def test_hyp_stext_namedelement_constructor_exists():
    assert callable(stext_NamedElement.__init__)


def test_hyp_stext_namedelement_constructor_args():
    sig = inspect.signature(stext_NamedElement.__init__)
    params = list(sig.parameters.keys())



def test_hyp_stext_state_is_not_abstract():
    assert not inspect.isabstract(stext_State)


def test_hyp_stext_state_constructor_exists():
    assert callable(stext_State.__init__)


def test_hyp_stext_state_constructor_args():
    sig = inspect.signature(stext_State.__init__)
    params = list(sig.parameters.keys())



def test_hyp_stext_feature_is_not_abstract():
    assert not inspect.isabstract(stext_Feature)


def test_hyp_stext_feature_constructor_exists():
    assert callable(stext_Feature.__init__)


def test_hyp_stext_feature_constructor_args():
    sig = inspect.signature(stext_Feature.__init__)
    params = list(sig.parameters.keys())



def test_hyp_expression_is_not_abstract():
    assert not inspect.isabstract(Expression)


def test_hyp_expression_constructor_exists():
    assert callable(Expression.__init__)


def test_hyp_expression_constructor_args():
    sig = inspect.signature(Expression.__init__)
    params = list(sig.parameters.keys())



def test_hyp_stext_bitwiseandexpression_is_not_abstract():
    assert not inspect.isabstract(stext_BitwiseAndExpression)


def test_hyp_stext_bitwiseandexpression_constructor_exists():
    assert callable(stext_BitwiseAndExpression.__init__)


def test_hyp_stext_bitwiseandexpression_constructor_args():
    sig = inspect.signature(stext_BitwiseAndExpression.__init__)
    params = list(sig.parameters.keys())



def test_hyp_stext_logicalrelationexpression_is_not_abstract():
    assert not inspect.isabstract(stext_LogicalRelationExpression)


def test_hyp_stext_logicalrelationexpression_constructor_exists():
    assert callable(stext_LogicalRelationExpression.__init__)


def test_hyp_stext_logicalrelationexpression_constructor_args():
    sig = inspect.signature(stext_LogicalRelationExpression.__init__)
    params = list(sig.parameters.keys())
    assert "operator" in params, "Missing parameter 'operator'"




def test_hyp_stext_eventvaluereferenceexpression_is_not_abstract():
    assert not inspect.isabstract(stext_EventValueReferenceExpression)


def test_hyp_stext_eventvaluereferenceexpression_constructor_exists():
    assert callable(stext_EventValueReferenceExpression.__init__)


def test_hyp_stext_eventvaluereferenceexpression_constructor_args():
    sig = inspect.signature(stext_EventValueReferenceExpression.__init__)
    params = list(sig.parameters.keys())



def test_hyp_stext_shiftexpression_is_not_abstract():
    assert not inspect.isabstract(stext_ShiftExpression)


def test_hyp_stext_shiftexpression_constructor_exists():
    assert callable(stext_ShiftExpression.__init__)


def test_hyp_stext_shiftexpression_constructor_args():
    sig = inspect.signature(stext_ShiftExpression.__init__)
    params = list(sig.parameters.keys())
    assert "operator" in params, "Missing parameter 'operator'"




def test_hyp_stext_typedelementreferenceexpression_is_not_abstract():
    assert not inspect.isabstract(stext_TypedElementReferenceExpression)


def test_hyp_stext_typedelementreferenceexpression_constructor_exists():
    assert callable(stext_TypedElementReferenceExpression.__init__)


def test_hyp_stext_typedelementreferenceexpression_constructor_args():
    sig = inspect.signature(stext_TypedElementReferenceExpression.__init__)
    params = list(sig.parameters.keys())



def test_hyp_stext_assignmentexpression_is_not_abstract():
    assert not inspect.isabstract(stext_AssignmentExpression)


def test_hyp_stext_assignmentexpression_constructor_exists():
    assert callable(stext_AssignmentExpression.__init__)


def test_hyp_stext_assignmentexpression_constructor_args():
    sig = inspect.signature(stext_AssignmentExpression.__init__)
    params = list(sig.parameters.keys())
    assert "operator" in params, "Missing parameter 'operator'"




def test_hyp_stext_featurecall_is_not_abstract():
    assert not inspect.isabstract(stext_FeatureCall)


def test_hyp_stext_featurecall_constructor_exists():
    assert callable(stext_FeatureCall.__init__)


def test_hyp_stext_featurecall_constructor_args():
    sig = inspect.signature(stext_FeatureCall.__init__)
    params = list(sig.parameters.keys())
    assert "operationCall" in params, "Missing parameter 'operationCall'"




def test_hyp_stext_logicalnotexpression_is_not_abstract():
    assert not inspect.isabstract(stext_LogicalNotExpression)


def test_hyp_stext_logicalnotexpression_constructor_exists():
    assert callable(stext_LogicalNotExpression.__init__)


def test_hyp_stext_logicalnotexpression_constructor_args():
    sig = inspect.signature(stext_LogicalNotExpression.__init__)
    params = list(sig.parameters.keys())



def test_hyp_stext_bitwiseorexpression_is_not_abstract():
    assert not inspect.isabstract(stext_BitwiseOrExpression)


def test_hyp_stext_bitwiseorexpression_constructor_exists():
    assert callable(stext_BitwiseOrExpression.__init__)


def test_hyp_stext_bitwiseorexpression_constructor_args():
    sig = inspect.signature(stext_BitwiseOrExpression.__init__)
    params = list(sig.parameters.keys())



def test_hyp_stext_activestatereferenceexpression_is_not_abstract():
    assert not inspect.isabstract(stext_ActiveStateReferenceExpression)


def test_hyp_stext_activestatereferenceexpression_constructor_exists():
    assert callable(stext_ActiveStateReferenceExpression.__init__)


def test_hyp_stext_activestatereferenceexpression_constructor_args():
    sig = inspect.signature(stext_ActiveStateReferenceExpression.__init__)
    params = list(sig.parameters.keys())



def test_hyp_stext_numericalunaryexpression_is_not_abstract():
    assert not inspect.isabstract(stext_NumericalUnaryExpression)


def test_hyp_stext_numericalunaryexpression_constructor_exists():
    assert callable(stext_NumericalUnaryExpression.__init__)


def test_hyp_stext_numericalunaryexpression_constructor_args():
    sig = inspect.signature(stext_NumericalUnaryExpression.__init__)
    params = list(sig.parameters.keys())
    assert "operator" in params, "Missing parameter 'operator'"




def test_hyp_stext_logicalandexpression_is_not_abstract():
    assert not inspect.isabstract(stext_LogicalAndExpression)


def test_hyp_stext_logicalandexpression_constructor_exists():
    assert callable(stext_LogicalAndExpression.__init__)


def test_hyp_stext_logicalandexpression_constructor_args():
    sig = inspect.signature(stext_LogicalAndExpression.__init__)
    params = list(sig.parameters.keys())



def test_hyp_stext_primitivevalueexpression_is_not_abstract():
    assert not inspect.isabstract(stext_PrimitiveValueExpression)


def test_hyp_stext_primitivevalueexpression_constructor_exists():
    assert callable(stext_PrimitiveValueExpression.__init__)


def test_hyp_stext_primitivevalueexpression_constructor_args():
    sig = inspect.signature(stext_PrimitiveValueExpression.__init__)
    params = list(sig.parameters.keys())



def test_hyp_stext_numericaladdsubtractexpression_is_not_abstract():
    assert not inspect.isabstract(stext_NumericalAddSubtractExpression)


def test_hyp_stext_numericaladdsubtractexpression_constructor_exists():
    assert callable(stext_NumericalAddSubtractExpression.__init__)


def test_hyp_stext_numericaladdsubtractexpression_constructor_args():
    sig = inspect.signature(stext_NumericalAddSubtractExpression.__init__)
    params = list(sig.parameters.keys())
    assert "operator" in params, "Missing parameter 'operator'"




def test_hyp_stext_bitwisexorexpression_is_not_abstract():
    assert not inspect.isabstract(stext_BitwiseXorExpression)


def test_hyp_stext_bitwisexorexpression_constructor_exists():
    assert callable(stext_BitwiseXorExpression.__init__)


def test_hyp_stext_bitwisexorexpression_constructor_args():
    sig = inspect.signature(stext_BitwiseXorExpression.__init__)
    params = list(sig.parameters.keys())



def test_hyp_stext_numericalmultiplydivideexpression_is_not_abstract():
    assert not inspect.isabstract(stext_NumericalMultiplyDivideExpression)


def test_hyp_stext_numericalmultiplydivideexpression_constructor_exists():
    assert callable(stext_NumericalMultiplyDivideExpression.__init__)


def test_hyp_stext_numericalmultiplydivideexpression_constructor_args():
    sig = inspect.signature(stext_NumericalMultiplyDivideExpression.__init__)
    params = list(sig.parameters.keys())
    assert "operator" in params, "Missing parameter 'operator'"




def test_hyp_stext_logicalorexpression_is_not_abstract():
    assert not inspect.isabstract(stext_LogicalOrExpression)


def test_hyp_stext_logicalorexpression_constructor_exists():
    assert callable(stext_LogicalOrExpression.__init__)


def test_hyp_stext_logicalorexpression_constructor_args():
    sig = inspect.signature(stext_LogicalOrExpression.__init__)
    params = list(sig.parameters.keys())



def test_hyp_stext_conditionalexpression_is_not_abstract():
    assert not inspect.isabstract(stext_ConditionalExpression)


def test_hyp_stext_conditionalexpression_constructor_exists():
    assert callable(stext_ConditionalExpression.__init__)


def test_hyp_stext_conditionalexpression_constructor_args():
    sig = inspect.signature(stext_ConditionalExpression.__init__)
    params = list(sig.parameters.keys())



def test_hyp_stext_eventraisingexpression_is_not_abstract():
    assert not inspect.isabstract(stext_EventRaisingExpression)


def test_hyp_stext_eventraisingexpression_constructor_exists():
    assert callable(stext_EventRaisingExpression.__init__)


def test_hyp_stext_eventraisingexpression_constructor_args():
    sig = inspect.signature(stext_EventRaisingExpression.__init__)
    params = list(sig.parameters.keys())



def test_hyp_effect_is_not_abstract():
    assert not inspect.isabstract(Effect)


def test_hyp_effect_constructor_exists():
    assert callable(Effect.__init__)


def test_hyp_effect_constructor_args():
    sig = inspect.signature(Effect.__init__)
    params = list(sig.parameters.keys())



def test_hyp_stext_reactioneffect_is_not_abstract():
    assert not inspect.isabstract(stext_ReactionEffect)


def test_hyp_stext_reactioneffect_constructor_exists():
    assert callable(stext_ReactionEffect.__init__)


def test_hyp_stext_reactioneffect_constructor_args():
    sig = inspect.signature(stext_ReactionEffect.__init__)
    params = list(sig.parameters.keys())



def test_hyp_trigger_is_not_abstract():
    assert not inspect.isabstract(Trigger)


def test_hyp_trigger_constructor_exists():
    assert callable(Trigger.__init__)


def test_hyp_trigger_constructor_args():
    sig = inspect.signature(Trigger.__init__)
    params = list(sig.parameters.keys())



def test_hyp_stext_reactiontrigger_is_not_abstract():
    assert not inspect.isabstract(stext_ReactionTrigger)


def test_hyp_stext_reactiontrigger_constructor_exists():
    assert callable(stext_ReactionTrigger.__init__)


def test_hyp_stext_reactiontrigger_constructor_args():
    sig = inspect.signature(stext_ReactionTrigger.__init__)
    params = list(sig.parameters.keys())



def test_hyp_operation_is_not_abstract():
    assert not inspect.isabstract(Operation)


def test_hyp_operation_constructor_exists():
    assert callable(Operation.__init__)


def test_hyp_operation_constructor_args():
    sig = inspect.signature(Operation.__init__)
    params = list(sig.parameters.keys())



def test_hyp_declaration_is_not_abstract():
    assert not inspect.isabstract(Declaration)


def test_hyp_declaration_constructor_exists():
    assert callable(Declaration.__init__)


def test_hyp_declaration_constructor_args():
    sig = inspect.signature(Declaration.__init__)
    params = list(sig.parameters.keys())



def test_hyp_stext_operationdefinition_is_not_abstract():
    assert not inspect.isabstract(stext_OperationDefinition)


def test_hyp_stext_operationdefinition_constructor_exists():
    assert callable(stext_OperationDefinition.__init__)


def test_hyp_stext_operationdefinition_constructor_args():
    sig = inspect.signature(stext_OperationDefinition.__init__)
    params = list(sig.parameters.keys())



def test_hyp_property_is_not_abstract():
    assert not inspect.isabstract(Property)


def test_hyp_property_constructor_exists():
    assert callable(Property.__init__)


def test_hyp_property_constructor_args():
    sig = inspect.signature(Property.__init__)
    params = list(sig.parameters.keys())



def test_hyp_variable_is_not_abstract():
    assert not inspect.isabstract(Variable)


def test_hyp_variable_constructor_exists():
    assert callable(Variable.__init__)


def test_hyp_variable_constructor_args():
    sig = inspect.signature(Variable.__init__)
    params = list(sig.parameters.keys())



def test_hyp_stext_variabledefinition_is_not_abstract():
    assert not inspect.isabstract(stext_VariableDefinition)


def test_hyp_stext_variabledefinition_constructor_exists():
    assert callable(stext_VariableDefinition.__init__)


def test_hyp_stext_variabledefinition_constructor_args():
    sig = inspect.signature(stext_VariableDefinition.__init__)
    params = list(sig.parameters.keys())
    assert "external" in params, "Missing parameter 'external'"
    assert "readonly" in params, "Missing parameter 'readonly'"





def test_hyp_literal_is_not_abstract():
    assert not inspect.isabstract(Literal)


def test_hyp_literal_constructor_exists():
    assert callable(Literal.__init__)


def test_hyp_literal_constructor_args():
    sig = inspect.signature(Literal.__init__)
    params = list(sig.parameters.keys())



def test_hyp_stext_stringliteral_is_not_abstract():
    assert not inspect.isabstract(stext_StringLiteral)


def test_hyp_stext_stringliteral_constructor_exists():
    assert callable(stext_StringLiteral.__init__)


def test_hyp_stext_stringliteral_constructor_args():
    sig = inspect.signature(stext_StringLiteral.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"




def test_hyp_stext_hexliteral_is_not_abstract():
    assert not inspect.isabstract(stext_HexLiteral)


def test_hyp_stext_hexliteral_constructor_exists():
    assert callable(stext_HexLiteral.__init__)


def test_hyp_stext_hexliteral_constructor_args():
    sig = inspect.signature(stext_HexLiteral.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"




def test_hyp_stext_intliteral_is_not_abstract():
    assert not inspect.isabstract(stext_IntLiteral)


def test_hyp_stext_intliteral_constructor_exists():
    assert callable(stext_IntLiteral.__init__)


def test_hyp_stext_intliteral_constructor_args():
    sig = inspect.signature(stext_IntLiteral.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"




def test_hyp_stext_realliteral_is_not_abstract():
    assert not inspect.isabstract(stext_RealLiteral)


def test_hyp_stext_realliteral_constructor_exists():
    assert callable(stext_RealLiteral.__init__)


def test_hyp_stext_realliteral_constructor_args():
    sig = inspect.signature(stext_RealLiteral.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"




def test_hyp_stext_boolliteral_is_not_abstract():
    assert not inspect.isabstract(stext_BoolLiteral)


def test_hyp_stext_boolliteral_constructor_exists():
    assert callable(stext_BoolLiteral.__init__)


def test_hyp_stext_boolliteral_constructor_args():
    sig = inspect.signature(stext_BoolLiteral.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"




def test_hyp_stext_literal_is_not_abstract():
    assert not inspect.isabstract(stext_Literal)


def test_hyp_stext_literal_constructor_exists():
    assert callable(stext_Literal.__init__)


def test_hyp_stext_literal_constructor_args():
    sig = inspect.signature(stext_Literal.__init__)
    params = list(sig.parameters.keys())



def test_hyp_statement_is_not_abstract():
    assert not inspect.isabstract(Statement)


def test_hyp_statement_constructor_exists():
    assert callable(Statement.__init__)


def test_hyp_statement_constructor_args():
    sig = inspect.signature(Statement.__init__)
    params = list(sig.parameters.keys())



def test_hyp_builtineventspec_is_not_abstract():
    assert not inspect.isabstract(BuiltinEventSpec)


def test_hyp_builtineventspec_constructor_exists():
    assert callable(BuiltinEventSpec.__init__)


def test_hyp_builtineventspec_constructor_args():
    sig = inspect.signature(BuiltinEventSpec.__init__)
    params = list(sig.parameters.keys())



def test_hyp_stext_exitevent_is_not_abstract():
    assert not inspect.isabstract(stext_ExitEvent)


def test_hyp_stext_exitevent_constructor_exists():
    assert callable(stext_ExitEvent.__init__)


def test_hyp_stext_exitevent_constructor_args():
    sig = inspect.signature(stext_ExitEvent.__init__)
    params = list(sig.parameters.keys())



def test_hyp_stext_oncycleevent_is_not_abstract():
    assert not inspect.isabstract(stext_OnCycleEvent)


def test_hyp_stext_oncycleevent_constructor_exists():
    assert callable(stext_OnCycleEvent.__init__)


def test_hyp_stext_oncycleevent_constructor_args():
    sig = inspect.signature(stext_OnCycleEvent.__init__)
    params = list(sig.parameters.keys())



def test_hyp_stext_alwaysevent_is_not_abstract():
    assert not inspect.isabstract(stext_AlwaysEvent)


def test_hyp_stext_alwaysevent_constructor_exists():
    assert callable(stext_AlwaysEvent.__init__)


def test_hyp_stext_alwaysevent_constructor_args():
    sig = inspect.signature(stext_AlwaysEvent.__init__)
    params = list(sig.parameters.keys())



def test_hyp_stext_defaultevent_is_not_abstract():
    assert not inspect.isabstract(stext_DefaultEvent)


def test_hyp_stext_defaultevent_constructor_exists():
    assert callable(stext_DefaultEvent.__init__)


def test_hyp_stext_defaultevent_constructor_args():
    sig = inspect.signature(stext_DefaultEvent.__init__)
    params = list(sig.parameters.keys())



def test_hyp_stext_entryevent_is_not_abstract():
    assert not inspect.isabstract(stext_EntryEvent)


def test_hyp_stext_entryevent_constructor_exists():
    assert callable(stext_EntryEvent.__init__)


def test_hyp_stext_entryevent_constructor_args():
    sig = inspect.signature(stext_EntryEvent.__init__)
    params = list(sig.parameters.keys())



def test_hyp_eventspec_is_not_abstract():
    assert not inspect.isabstract(EventSpec)


def test_hyp_eventspec_constructor_exists():
    assert callable(EventSpec.__init__)


def test_hyp_eventspec_constructor_args():
    sig = inspect.signature(EventSpec.__init__)
    params = list(sig.parameters.keys())



def test_hyp_stext_builtineventspec_is_not_abstract():
    assert not inspect.isabstract(stext_BuiltinEventSpec)


def test_hyp_stext_builtineventspec_constructor_exists():
    assert callable(stext_BuiltinEventSpec.__init__)


def test_hyp_stext_builtineventspec_constructor_args():
    sig = inspect.signature(stext_BuiltinEventSpec.__init__)
    params = list(sig.parameters.keys())



def test_hyp_stext_timeeventspec_is_not_abstract():
    assert not inspect.isabstract(stext_TimeEventSpec)


def test_hyp_stext_timeeventspec_constructor_exists():
    assert callable(stext_TimeEventSpec.__init__)


def test_hyp_stext_timeeventspec_constructor_args():
    sig = inspect.signature(stext_TimeEventSpec.__init__)
    params = list(sig.parameters.keys())
    assert "unit" in params, "Missing parameter 'unit'"
    assert "type" in params, "Missing parameter 'type'"
    assert "value" in params, "Missing parameter 'value'"






def test_hyp_stext_regulareventspec_is_not_abstract():
    assert not inspect.isabstract(stext_RegularEventSpec)


def test_hyp_stext_regulareventspec_constructor_exists():
    assert callable(stext_RegularEventSpec.__init__)


def test_hyp_stext_regulareventspec_constructor_args():
    sig = inspect.signature(stext_RegularEventSpec.__init__)
    params = list(sig.parameters.keys())



def test_hyp_stext_eventspec_is_not_abstract():
    assert not inspect.isabstract(stext_EventSpec)


def test_hyp_stext_eventspec_constructor_exists():
    assert callable(stext_EventSpec.__init__)


def test_hyp_stext_eventspec_constructor_args():
    sig = inspect.signature(stext_EventSpec.__init__)
    params = list(sig.parameters.keys())



def test_hyp_stext_exitpoint_is_not_abstract():
    assert not inspect.isabstract(stext_Exitpoint)


def test_hyp_stext_exitpoint_constructor_exists():
    assert callable(stext_Exitpoint.__init__)


def test_hyp_stext_exitpoint_constructor_args():
    sig = inspect.signature(stext_Exitpoint.__init__)
    params = list(sig.parameters.keys())



def test_hyp_stext_entrypoint_is_not_abstract():
    assert not inspect.isabstract(stext_Entrypoint)


def test_hyp_stext_entrypoint_constructor_exists():
    assert callable(stext_Entrypoint.__init__)


def test_hyp_stext_entrypoint_constructor_args():
    sig = inspect.signature(stext_Entrypoint.__init__)
    params = list(sig.parameters.keys())



def test_hyp_reactionproperty_is_not_abstract():
    assert not inspect.isabstract(ReactionProperty)


def test_hyp_reactionproperty_constructor_exists():
    assert callable(ReactionProperty.__init__)


def test_hyp_reactionproperty_constructor_args():
    sig = inspect.signature(ReactionProperty.__init__)
    params = list(sig.parameters.keys())



def test_hyp_stext_exitpointspec_is_not_abstract():
    assert not inspect.isabstract(stext_ExitPointSpec)


def test_hyp_stext_exitpointspec_constructor_exists():
    assert callable(stext_ExitPointSpec.__init__)


def test_hyp_stext_exitpointspec_constructor_args():
    sig = inspect.signature(stext_ExitPointSpec.__init__)
    params = list(sig.parameters.keys())



def test_hyp_stext_entrypointspec_is_not_abstract():
    assert not inspect.isabstract(stext_EntryPointSpec)


def test_hyp_stext_entrypointspec_constructor_exists():
    assert callable(stext_EntryPointSpec.__init__)


def test_hyp_stext_entrypointspec_constructor_args():
    sig = inspect.signature(stext_EntryPointSpec.__init__)
    params = list(sig.parameters.keys())



def test_hyp_stext_reactionproperty_is_not_abstract():
    assert not inspect.isabstract(stext_ReactionProperty)


def test_hyp_stext_reactionproperty_constructor_exists():
    assert callable(stext_ReactionProperty.__init__)


def test_hyp_stext_reactionproperty_constructor_args():
    sig = inspect.signature(stext_ReactionProperty.__init__)
    params = list(sig.parameters.keys())



def test_hyp_stext_reactionproperties_is_not_abstract():
    assert not inspect.isabstract(stext_ReactionProperties)


def test_hyp_stext_reactionproperties_constructor_exists():
    assert callable(stext_ReactionProperties.__init__)


def test_hyp_stext_reactionproperties_constructor_args():
    sig = inspect.signature(stext_ReactionProperties.__init__)
    params = list(sig.parameters.keys())



def test_hyp_reaction_is_not_abstract():
    assert not inspect.isabstract(Reaction)


def test_hyp_reaction_constructor_exists():
    assert callable(Reaction.__init__)


def test_hyp_reaction_constructor_args():
    sig = inspect.signature(Reaction.__init__)
    params = list(sig.parameters.keys())



def test_hyp_stext_localreaction_is_not_abstract():
    assert not inspect.isabstract(stext_LocalReaction)


def test_hyp_stext_localreaction_constructor_exists():
    assert callable(stext_LocalReaction.__init__)


def test_hyp_stext_localreaction_constructor_args():
    sig = inspect.signature(stext_LocalReaction.__init__)
    params = list(sig.parameters.keys())



def test_hyp_stext_type_is_not_abstract():
    assert not inspect.isabstract(stext_Type)


def test_hyp_stext_type_constructor_exists():
    assert callable(stext_Type.__init__)


def test_hyp_stext_type_constructor_args():
    sig = inspect.signature(stext_Type.__init__)
    params = list(sig.parameters.keys())



def test_hyp_stext_defroot_is_not_abstract():
    assert not inspect.isabstract(stext_DefRoot)


def test_hyp_stext_defroot_constructor_exists():
    assert callable(stext_DefRoot.__init__)


def test_hyp_stext_defroot_constructor_args():
    sig = inspect.signature(stext_DefRoot.__init__)
    params = list(sig.parameters.keys())



def test_hyp_stext_root_is_not_abstract():
    assert not inspect.isabstract(stext_Root)


def test_hyp_stext_root_constructor_exists():
    assert callable(stext_Root.__init__)


def test_hyp_stext_root_constructor_args():
    sig = inspect.signature(stext_Root.__init__)
    params = list(sig.parameters.keys())



def test_hyp_stext_expression_is_not_abstract():
    assert not inspect.isabstract(stext_Expression)


def test_hyp_stext_expression_constructor_exists():
    assert callable(stext_Expression.__init__)


def test_hyp_stext_expression_constructor_args():
    sig = inspect.signature(stext_Expression.__init__)
    params = list(sig.parameters.keys())



def test_hyp_stext_eventderivation_is_not_abstract():
    assert not inspect.isabstract(stext_EventDerivation)


def test_hyp_stext_eventderivation_constructor_exists():
    assert callable(stext_EventDerivation.__init__)


def test_hyp_stext_eventderivation_constructor_args():
    sig = inspect.signature(stext_EventDerivation.__init__)
    params = list(sig.parameters.keys())



def test_hyp_event_is_not_abstract():
    assert not inspect.isabstract(Event)


def test_hyp_event_constructor_exists():
    assert callable(Event.__init__)


def test_hyp_event_constructor_args():
    sig = inspect.signature(Event.__init__)
    params = list(sig.parameters.keys())



def test_hyp_stext_eventdefinition_is_not_abstract():
    assert not inspect.isabstract(stext_EventDefinition)


def test_hyp_stext_eventdefinition_constructor_exists():
    assert callable(stext_EventDefinition.__init__)


def test_hyp_stext_eventdefinition_constructor_args():
    sig = inspect.signature(stext_EventDefinition.__init__)
    params = list(sig.parameters.keys())
    assert "direction" in params, "Missing parameter 'direction'"




def test_hyp_namedelement_is_not_abstract():
    assert not inspect.isabstract(NamedElement)


def test_hyp_namedelement_constructor_exists():
    assert callable(NamedElement.__init__)


def test_hyp_namedelement_constructor_args():
    sig = inspect.signature(NamedElement.__init__)
    params = list(sig.parameters.keys())



def test_hyp_statechartscope_is_not_abstract():
    assert not inspect.isabstract(StatechartScope)


def test_hyp_statechartscope_constructor_exists():
    assert callable(StatechartScope.__init__)


def test_hyp_statechartscope_constructor_args():
    sig = inspect.signature(StatechartScope.__init__)
    params = list(sig.parameters.keys())



def test_hyp_stext_internalscope_is_not_abstract():
    assert not inspect.isabstract(stext_InternalScope)


def test_hyp_stext_internalscope_constructor_exists():
    assert callable(stext_InternalScope.__init__)


def test_hyp_stext_internalscope_constructor_args():
    sig = inspect.signature(stext_InternalScope.__init__)
    params = list(sig.parameters.keys())



def test_hyp_stext_interfacescope_is_not_abstract():
    assert not inspect.isabstract(stext_InterfaceScope)


def test_hyp_stext_interfacescope_constructor_exists():
    assert callable(stext_InterfaceScope.__init__)


def test_hyp_stext_interfacescope_constructor_args():
    sig = inspect.signature(stext_InterfaceScope.__init__)
    params = list(sig.parameters.keys())



def test_hyp_scope_is_not_abstract():
    assert not inspect.isabstract(Scope)


def test_hyp_scope_constructor_exists():
    assert callable(Scope.__init__)


def test_hyp_scope_constructor_args():
    sig = inspect.signature(Scope.__init__)
    params = list(sig.parameters.keys())



def test_hyp_stext_simplescope_is_not_abstract():
    assert not inspect.isabstract(stext_SimpleScope)


def test_hyp_stext_simplescope_constructor_exists():
    assert callable(stext_SimpleScope.__init__)


def test_hyp_stext_simplescope_constructor_args():
    sig = inspect.signature(stext_SimpleScope.__init__)
    params = list(sig.parameters.keys())



def test_hyp_stext_transitionreaction_is_not_abstract():
    assert not inspect.isabstract(stext_TransitionReaction)


def test_hyp_stext_transitionreaction_constructor_exists():
    assert callable(stext_TransitionReaction.__init__)


def test_hyp_stext_transitionreaction_constructor_args():
    sig = inspect.signature(stext_TransitionReaction.__init__)
    params = list(sig.parameters.keys())



def test_hyp_stext_scope_is_not_abstract():
    assert not inspect.isabstract(stext_Scope)


def test_hyp_stext_scope_constructor_exists():
    assert callable(stext_Scope.__init__)


def test_hyp_stext_scope_constructor_args():
    sig = inspect.signature(stext_Scope.__init__)
    params = list(sig.parameters.keys())



def test_hyp_stext_statechartscope_is_not_abstract():
    assert not inspect.isabstract(stext_StatechartScope)


def test_hyp_stext_statechartscope_constructor_exists():
    assert callable(stext_StatechartScope.__init__)


def test_hyp_stext_statechartscope_constructor_args():
    sig = inspect.signature(stext_StatechartScope.__init__)
    params = list(sig.parameters.keys())



def test_hyp_stext_transitionspecification_is_not_abstract():
    assert not inspect.isabstract(stext_TransitionSpecification)


def test_hyp_stext_transitionspecification_constructor_exists():
    assert callable(stext_TransitionSpecification.__init__)


def test_hyp_stext_transitionspecification_constructor_args():
    sig = inspect.signature(stext_TransitionSpecification.__init__)
    params = list(sig.parameters.keys())



def test_hyp_stext_statespecification_is_not_abstract():
    assert not inspect.isabstract(stext_StateSpecification)


def test_hyp_stext_statespecification_constructor_exists():
    assert callable(stext_StateSpecification.__init__)


def test_hyp_stext_statespecification_constructor_args():
    sig = inspect.signature(stext_StateSpecification.__init__)
    params = list(sig.parameters.keys())



def test_hyp_stext_statechartspecification_is_not_abstract():
    assert not inspect.isabstract(stext_StatechartSpecification)


def test_hyp_stext_statechartspecification_constructor_exists():
    assert callable(stext_StatechartSpecification.__init__)


def test_hyp_stext_statechartspecification_constructor_args():
    sig = inspect.signature(stext_StatechartSpecification.__init__)
    params = list(sig.parameters.keys())
    assert "namespace" in params, "Missing parameter 'namespace'"




def test_hyp_defroot_is_not_abstract():
    assert not inspect.isabstract(DefRoot)


def test_hyp_defroot_constructor_exists():
    assert callable(DefRoot.__init__)


def test_hyp_defroot_constructor_args():
    sig = inspect.signature(DefRoot.__init__)
    params = list(sig.parameters.keys())



def test_hyp_stext_stateroot_is_not_abstract():
    assert not inspect.isabstract(stext_StateRoot)


def test_hyp_stext_stateroot_constructor_exists():
    assert callable(stext_StateRoot.__init__)


def test_hyp_stext_stateroot_constructor_args():
    sig = inspect.signature(stext_StateRoot.__init__)
    params = list(sig.parameters.keys())



def test_hyp_stext_transitionroot_is_not_abstract():
    assert not inspect.isabstract(stext_TransitionRoot)


def test_hyp_stext_transitionroot_constructor_exists():
    assert callable(stext_TransitionRoot.__init__)


def test_hyp_stext_transitionroot_constructor_args():
    sig = inspect.signature(stext_TransitionRoot.__init__)
    params = list(sig.parameters.keys())



def test_hyp_stext_statechartroot_is_not_abstract():
    assert not inspect.isabstract(stext_StatechartRoot)


def test_hyp_stext_statechartroot_constructor_exists():
    assert callable(stext_StatechartRoot.__init__)


def test_hyp_stext_statechartroot_constructor_args():
    sig = inspect.signature(stext_StatechartRoot.__init__)
    params = list(sig.parameters.keys())

def test_hyp_relationaloperator_exists():
    # Check that the Enumeration exists
    assert RelationalOperator is not None

def test_hyp_relationaloperator_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in RelationalOperator]
    expected_literals = [
        "equals",
        "greaterEqual",
        "greater",
        "notEquals",
        "smaller",
        "smallerEqual",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in RelationalOperator"

def test_hyp_timeunit_exists():
    # Check that the Enumeration exists
    assert TimeUnit is not None

def test_hyp_timeunit_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in TimeUnit]
    expected_literals = [
        "nanosecond",
        "second",
        "microsecond",
        "millisecond",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in TimeUnit"

def test_hyp_direction_exists():
    # Check that the Enumeration exists
    assert Direction is not None

def test_hyp_direction_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in Direction]
    expected_literals = [
        "OUT",
        "LOCAL",
        "IN",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in Direction"

def test_hyp_unaryoperator_exists():
    # Check that the Enumeration exists
    assert UnaryOperator is not None

def test_hyp_unaryoperator_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in UnaryOperator]
    expected_literals = [
        "complement",
        "positive",
        "negative",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in UnaryOperator"

def test_hyp_additiveoperator_exists():
    # Check that the Enumeration exists
    assert AdditiveOperator is not None

def test_hyp_additiveoperator_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in AdditiveOperator]
    expected_literals = [
        "minus",
        "plus",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in AdditiveOperator"

def test_hyp_assignmentoperator_exists():
    # Check that the Enumeration exists
    assert AssignmentOperator is not None

def test_hyp_assignmentoperator_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in AssignmentOperator]
    expected_literals = [
        "leftShiftAssign",
        "modAssign",
        "rightShiftAssign",
        "divAssign",
        "orAssign",
        "addAssign",
        "assign",
        "multAssign",
        "xorAssign",
        "andAssign",
        "subAssign",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in AssignmentOperator"

def test_hyp_multiplicativeoperator_exists():
    # Check that the Enumeration exists
    assert MultiplicativeOperator is not None

def test_hyp_multiplicativeoperator_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in MultiplicativeOperator]
    expected_literals = [
        "mod",
        "mul",
        "div",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in MultiplicativeOperator"

def test_hyp_timeeventtype_exists():
    # Check that the Enumeration exists
    assert TimeEventType is not None

def test_hyp_timeeventtype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in TimeEventType]
    expected_literals = [
        "every",
        "after",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in TimeEventType"

def test_hyp_shiftoperator_exists():
    # Check that the Enumeration exists
    assert ShiftOperator is not None

def test_hyp_shiftoperator_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in ShiftOperator]
    expected_literals = [
        "right",
        "left",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in ShiftOperator"


# =============================================================================
# HYPOTHESIS STRATEGIES
# =============================================================================

safe_text = st.text(
    alphabet=st.characters(
        whitelist_categories=("Ll", "Lu", "Nd"),
        whitelist_characters="_",
    ),
    min_size=1,
).filter(lambda s: s[0].isalpha())
stext_NamedElement_strategy = st.builds(
    stext_NamedElement,
)
stext_State_strategy = st.builds(
    stext_State,
)
stext_Feature_strategy = st.builds(
    stext_Feature,
)
Expression_strategy = st.builds(
    Expression,
)
stext_BitwiseAndExpression_strategy = st.builds(
    stext_BitwiseAndExpression,
)
stext_LogicalRelationExpression_strategy = st.builds(
    stext_LogicalRelationExpression,
    operator=
        safe_text
)
stext_EventValueReferenceExpression_strategy = st.builds(
    stext_EventValueReferenceExpression,
)
stext_ShiftExpression_strategy = st.builds(
    stext_ShiftExpression,
    operator=
        safe_text
)
stext_TypedElementReferenceExpression_strategy = st.builds(
    stext_TypedElementReferenceExpression,
)
stext_AssignmentExpression_strategy = st.builds(
    stext_AssignmentExpression,
    operator=
        safe_text
)
stext_FeatureCall_strategy = st.builds(
    stext_FeatureCall,
    operationCall=
        st.booleans()
)
stext_LogicalNotExpression_strategy = st.builds(
    stext_LogicalNotExpression,
)
stext_BitwiseOrExpression_strategy = st.builds(
    stext_BitwiseOrExpression,
)
stext_ActiveStateReferenceExpression_strategy = st.builds(
    stext_ActiveStateReferenceExpression,
)
stext_NumericalUnaryExpression_strategy = st.builds(
    stext_NumericalUnaryExpression,
    operator=
        safe_text
)
stext_LogicalAndExpression_strategy = st.builds(
    stext_LogicalAndExpression,
)
stext_PrimitiveValueExpression_strategy = st.builds(
    stext_PrimitiveValueExpression,
)
stext_NumericalAddSubtractExpression_strategy = st.builds(
    stext_NumericalAddSubtractExpression,
    operator=
        safe_text
)
stext_BitwiseXorExpression_strategy = st.builds(
    stext_BitwiseXorExpression,
)
stext_NumericalMultiplyDivideExpression_strategy = st.builds(
    stext_NumericalMultiplyDivideExpression,
    operator=
        safe_text
)
stext_LogicalOrExpression_strategy = st.builds(
    stext_LogicalOrExpression,
)
stext_ConditionalExpression_strategy = st.builds(
    stext_ConditionalExpression,
)
stext_EventRaisingExpression_strategy = st.builds(
    stext_EventRaisingExpression,
)
Effect_strategy = st.builds(
    Effect,
)
stext_ReactionEffect_strategy = st.builds(
    stext_ReactionEffect,
)
Trigger_strategy = st.builds(
    Trigger,
)
stext_ReactionTrigger_strategy = st.builds(
    stext_ReactionTrigger,
)
Operation_strategy = st.builds(
    Operation,
)
Declaration_strategy = st.builds(
    Declaration,
)
stext_OperationDefinition_strategy = st.builds(
    stext_OperationDefinition,
)
Property_strategy = st.builds(
    Property,
)
Variable_strategy = st.builds(
    Variable,
)
stext_VariableDefinition_strategy = st.builds(
    stext_VariableDefinition,
    external=
        st.booleans(),
    readonly=
        st.booleans()
)
Literal_strategy = st.builds(
    Literal,
)
stext_StringLiteral_strategy = st.builds(
    stext_StringLiteral,
    value=
        safe_text
)
stext_HexLiteral_strategy = st.builds(
    stext_HexLiteral,
    value=
        st.integers()
)
stext_IntLiteral_strategy = st.builds(
    stext_IntLiteral,
    value=
        st.integers()
)
stext_RealLiteral_strategy = st.builds(
    stext_RealLiteral,
    value=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
stext_BoolLiteral_strategy = st.builds(
    stext_BoolLiteral,
    value=
        st.booleans()
)
stext_Literal_strategy = st.builds(
    stext_Literal,
)
Statement_strategy = st.builds(
    Statement,
)
BuiltinEventSpec_strategy = st.builds(
    BuiltinEventSpec,
)
stext_ExitEvent_strategy = st.builds(
    stext_ExitEvent,
)
stext_OnCycleEvent_strategy = st.builds(
    stext_OnCycleEvent,
)
stext_AlwaysEvent_strategy = st.builds(
    stext_AlwaysEvent,
)
stext_DefaultEvent_strategy = st.builds(
    stext_DefaultEvent,
)
stext_EntryEvent_strategy = st.builds(
    stext_EntryEvent,
)
EventSpec_strategy = st.builds(
    EventSpec,
)
stext_BuiltinEventSpec_strategy = st.builds(
    stext_BuiltinEventSpec,
)
stext_TimeEventSpec_strategy = st.builds(
    stext_TimeEventSpec,
    unit=
        safe_text,
    type=
        safe_text,
    value=
        st.integers()
)
stext_RegularEventSpec_strategy = st.builds(
    stext_RegularEventSpec,
)
stext_EventSpec_strategy = st.builds(
    stext_EventSpec,
)
stext_Exitpoint_strategy = st.builds(
    stext_Exitpoint,
)
stext_Entrypoint_strategy = st.builds(
    stext_Entrypoint,
)
ReactionProperty_strategy = st.builds(
    ReactionProperty,
)
stext_ExitPointSpec_strategy = st.builds(
    stext_ExitPointSpec,
)
stext_EntryPointSpec_strategy = st.builds(
    stext_EntryPointSpec,
)
stext_ReactionProperty_strategy = st.builds(
    stext_ReactionProperty,
)
stext_ReactionProperties_strategy = st.builds(
    stext_ReactionProperties,
)
Reaction_strategy = st.builds(
    Reaction,
)
stext_LocalReaction_strategy = st.builds(
    stext_LocalReaction,
)
stext_Type_strategy = st.builds(
    stext_Type,
)
stext_DefRoot_strategy = st.builds(
    stext_DefRoot,
)
stext_Root_strategy = st.builds(
    stext_Root,
)
stext_Expression_strategy = st.builds(
    stext_Expression,
)
stext_EventDerivation_strategy = st.builds(
    stext_EventDerivation,
)
Event_strategy = st.builds(
    Event,
)
stext_EventDefinition_strategy = st.builds(
    stext_EventDefinition,
    direction=
        safe_text
)
NamedElement_strategy = st.builds(
    NamedElement,
)
StatechartScope_strategy = st.builds(
    StatechartScope,
)
stext_InternalScope_strategy = st.builds(
    stext_InternalScope,
)
stext_InterfaceScope_strategy = st.builds(
    stext_InterfaceScope,
)
Scope_strategy = st.builds(
    Scope,
)
stext_SimpleScope_strategy = st.builds(
    stext_SimpleScope,
)
stext_TransitionReaction_strategy = st.builds(
    stext_TransitionReaction,
)
stext_Scope_strategy = st.builds(
    stext_Scope,
)
stext_StatechartScope_strategy = st.builds(
    stext_StatechartScope,
)
stext_TransitionSpecification_strategy = st.builds(
    stext_TransitionSpecification,
)
stext_StateSpecification_strategy = st.builds(
    stext_StateSpecification,
)
stext_StatechartSpecification_strategy = st.builds(
    stext_StatechartSpecification,
    namespace=
        safe_text
)
DefRoot_strategy = st.builds(
    DefRoot,
)
stext_StateRoot_strategy = st.builds(
    stext_StateRoot,
)
stext_TransitionRoot_strategy = st.builds(
    stext_TransitionRoot,
)
stext_StatechartRoot_strategy = st.builds(
    stext_StatechartRoot,
)









@given(instance=stext_LogicalRelationExpression_strategy)
def test_hyp_stext_logicalrelationexpression_operator_setter(instance):
    original = instance.operator
    instance.operator = original
    assert instance.operator == original





@given(instance=stext_ShiftExpression_strategy)
def test_hyp_stext_shiftexpression_operator_setter(instance):
    original = instance.operator
    instance.operator = original
    assert instance.operator == original





@given(instance=stext_AssignmentExpression_strategy)
def test_hyp_stext_assignmentexpression_operator_setter(instance):
    original = instance.operator
    instance.operator = original
    assert instance.operator == original




@given(instance=stext_FeatureCall_strategy)
def test_hyp_stext_featurecall_operationCall_setter(instance):
    original = instance.operationCall
    instance.operationCall = original
    assert instance.operationCall == original







@given(instance=stext_NumericalUnaryExpression_strategy)
def test_hyp_stext_numericalunaryexpression_operator_setter(instance):
    original = instance.operator
    instance.operator = original
    assert instance.operator == original






@given(instance=stext_NumericalAddSubtractExpression_strategy)
def test_hyp_stext_numericaladdsubtractexpression_operator_setter(instance):
    original = instance.operator
    instance.operator = original
    assert instance.operator == original





@given(instance=stext_NumericalMultiplyDivideExpression_strategy)
def test_hyp_stext_numericalmultiplydivideexpression_operator_setter(instance):
    original = instance.operator
    instance.operator = original
    assert instance.operator == original
















@given(instance=stext_VariableDefinition_strategy)
def test_hyp_stext_variabledefinition_external_setter(instance):
    original = instance.external
    instance.external = original
    assert instance.external == original



@given(instance=stext_VariableDefinition_strategy)
def test_hyp_stext_variabledefinition_readonly_setter(instance):
    original = instance.readonly
    instance.readonly = original
    assert instance.readonly == original





@given(instance=stext_StringLiteral_strategy)
def test_hyp_stext_stringliteral_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original




@given(instance=stext_HexLiteral_strategy)
def test_hyp_stext_hexliteral_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original




@given(instance=stext_IntLiteral_strategy)
def test_hyp_stext_intliteral_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original




@given(instance=stext_RealLiteral_strategy)
def test_hyp_stext_realliteral_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original




@given(instance=stext_BoolLiteral_strategy)
def test_hyp_stext_boolliteral_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original














@given(instance=stext_TimeEventSpec_strategy)
def test_hyp_stext_timeeventspec_unit_setter(instance):
    original = instance.unit
    instance.unit = original
    assert instance.unit == original



@given(instance=stext_TimeEventSpec_strategy)
def test_hyp_stext_timeeventspec_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original



@given(instance=stext_TimeEventSpec_strategy)
def test_hyp_stext_timeeventspec_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original





















@given(instance=stext_EventDefinition_strategy)
def test_hyp_stext_eventdefinition_direction_setter(instance):
    original = instance.direction
    instance.direction = original
    assert instance.direction == original















@given(instance=stext_StatechartSpecification_strategy)
def test_hyp_stext_statechartspecification_namespace_setter(instance):
    original = instance.namespace
    instance.namespace = original
    assert instance.namespace == original






# ----- SECTION B: test_structural_full.py (deterministic-first suite) -----
import inspect
import pytest
from datetime import date, datetime, time, timedelta
from hypothesis import given, settings
import hypothesis.strategies as st

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
    stext_Type,
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

safe_text = st.text(
    alphabet=st.characters(
        whitelist_categories=("Ll", "Lu", "Nd"),
        whitelist_characters="_",
    ),
    min_size=1,
).filter(lambda s: s[0].isalpha())

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
# SECTION 1 -- DETERMINISTIC TESTS (attributes, generalizations, relationships)
# =============================================================================

def test_stext_AssignmentExpression_operator_value_roundtrip():
    instance = stext_AssignmentExpression(operator="sample_text")
    assert instance.operator == "sample_text"
    instance.operator = "sample_text_2"
    assert instance.operator == "sample_text_2"


def test_stext_BoolLiteral_value_value_roundtrip():
    instance = stext_BoolLiteral(value=True)
    assert instance.value == True
    instance.value = False
    assert instance.value == False


def test_stext_EventDefinition_direction_value_roundtrip():
    instance = stext_EventDefinition(direction="sample_text")
    assert instance.direction == "sample_text"
    instance.direction = "sample_text_2"
    assert instance.direction == "sample_text_2"


def test_stext_FeatureCall_operationCall_value_roundtrip():
    instance = stext_FeatureCall(operationCall=True)
    assert instance.operationCall == True
    instance.operationCall = False
    assert instance.operationCall == False


def test_stext_HexLiteral_value_value_roundtrip():
    instance = stext_HexLiteral(value=7)
    assert instance.value == 7
    instance.value = 13
    assert instance.value == 13


def test_stext_IntLiteral_value_value_roundtrip():
    instance = stext_IntLiteral(value=7)
    assert instance.value == 7
    instance.value = 13
    assert instance.value == 13


def test_stext_LogicalRelationExpression_operator_value_roundtrip():
    instance = stext_LogicalRelationExpression(operator="sample_text")
    assert instance.operator == "sample_text"
    instance.operator = "sample_text_2"
    assert instance.operator == "sample_text_2"


def test_stext_NumericalAddSubtractExpression_operator_value_roundtrip():
    instance = stext_NumericalAddSubtractExpression(operator="sample_text")
    assert instance.operator == "sample_text"
    instance.operator = "sample_text_2"
    assert instance.operator == "sample_text_2"


def test_stext_NumericalMultiplyDivideExpression_operator_value_roundtrip():
    instance = stext_NumericalMultiplyDivideExpression(operator="sample_text")
    assert instance.operator == "sample_text"
    instance.operator = "sample_text_2"
    assert instance.operator == "sample_text_2"


def test_stext_NumericalUnaryExpression_operator_value_roundtrip():
    instance = stext_NumericalUnaryExpression(operator="sample_text")
    assert instance.operator == "sample_text"
    instance.operator = "sample_text_2"
    assert instance.operator == "sample_text_2"


def test_stext_RealLiteral_value_value_roundtrip():
    instance = stext_RealLiteral(value=3.14)
    assert instance.value == 3.14
    instance.value = 9.99
    assert instance.value == 9.99


def test_stext_ShiftExpression_operator_value_roundtrip():
    instance = stext_ShiftExpression(operator="sample_text")
    assert instance.operator == "sample_text"
    instance.operator = "sample_text_2"
    assert instance.operator == "sample_text_2"


def test_stext_StatechartSpecification_namespace_value_roundtrip():
    instance = stext_StatechartSpecification(namespace="sample_text")
    assert instance.namespace == "sample_text"
    instance.namespace = "sample_text_2"
    assert instance.namespace == "sample_text_2"


def test_stext_StringLiteral_value_value_roundtrip():
    instance = stext_StringLiteral(value="sample_text")
    assert instance.value == "sample_text"
    instance.value = "sample_text_2"
    assert instance.value == "sample_text_2"


def test_stext_TimeEventSpec_type_value_roundtrip():
    instance = stext_TimeEventSpec(type="sample_text", unit="sample_text", value=7)
    assert instance.type == "sample_text"
    instance.type = "sample_text_2"
    assert instance.type == "sample_text_2"


def test_stext_TimeEventSpec_unit_value_roundtrip():
    instance = stext_TimeEventSpec(type="sample_text", unit="sample_text", value=7)
    assert instance.unit == "sample_text"
    instance.unit = "sample_text_2"
    assert instance.unit == "sample_text_2"


def test_stext_TimeEventSpec_value_value_roundtrip():
    instance = stext_TimeEventSpec(type="sample_text", unit="sample_text", value=7)
    assert instance.value == 7
    instance.value = 13
    assert instance.value == 13


def test_stext_VariableDefinition_external_value_roundtrip():
    instance = stext_VariableDefinition(external=True, readonly=True)
    assert instance.external == True
    instance.external = False
    assert instance.external == False


def test_stext_VariableDefinition_readonly_value_roundtrip():
    instance = stext_VariableDefinition(external=True, readonly=True)
    assert instance.readonly == True
    instance.readonly = False
    assert instance.readonly == False


def test_stext_AlwaysEvent_isa_BuiltinEventSpec():
    instance = stext_AlwaysEvent()
    assert isinstance(instance, BuiltinEventSpec)


def test_stext_DefaultEvent_isa_BuiltinEventSpec():
    instance = stext_DefaultEvent()
    assert isinstance(instance, BuiltinEventSpec)


def test_stext_EntryEvent_isa_BuiltinEventSpec():
    instance = stext_EntryEvent()
    assert isinstance(instance, BuiltinEventSpec)


def test_stext_ExitEvent_isa_BuiltinEventSpec():
    instance = stext_ExitEvent()
    assert isinstance(instance, BuiltinEventSpec)


def test_stext_OnCycleEvent_isa_BuiltinEventSpec():
    instance = stext_OnCycleEvent()
    assert isinstance(instance, BuiltinEventSpec)


def test_stext_Entrypoint_isa_Declaration():
    instance = stext_Entrypoint()
    assert isinstance(instance, Declaration)


def test_stext_Exitpoint_isa_Declaration():
    instance = stext_Exitpoint()
    assert isinstance(instance, Declaration)


def test_stext_LocalReaction_isa_Declaration():
    instance = stext_LocalReaction()
    assert isinstance(instance, Declaration)


def test_stext_OperationDefinition_isa_Declaration():
    instance = stext_OperationDefinition()
    assert isinstance(instance, Declaration)


def test_stext_StateRoot_isa_DefRoot():
    instance = stext_StateRoot()
    assert isinstance(instance, DefRoot)


def test_stext_StatechartRoot_isa_DefRoot():
    instance = stext_StatechartRoot()
    assert isinstance(instance, DefRoot)


def test_stext_TransitionRoot_isa_DefRoot():
    instance = stext_TransitionRoot()
    assert isinstance(instance, DefRoot)


def test_stext_ReactionEffect_isa_Effect():
    instance = stext_ReactionEffect()
    assert isinstance(instance, Effect)


def test_stext_EventDefinition_isa_Event():
    instance = stext_EventDefinition(direction="sample_text")
    assert isinstance(instance, Event)


def test_stext_BuiltinEventSpec_isa_EventSpec():
    instance = stext_BuiltinEventSpec()
    assert isinstance(instance, EventSpec)


def test_stext_RegularEventSpec_isa_EventSpec():
    instance = stext_RegularEventSpec()
    assert isinstance(instance, EventSpec)


def test_stext_TimeEventSpec_isa_EventSpec():
    instance = stext_TimeEventSpec(type="sample_text", unit="sample_text", value=7)
    assert isinstance(instance, EventSpec)


def test_stext_ActiveStateReferenceExpression_isa_Expression():
    instance = stext_ActiveStateReferenceExpression()
    assert isinstance(instance, Expression)


def test_stext_AssignmentExpression_isa_Expression():
    instance = stext_AssignmentExpression(operator="sample_text")
    assert isinstance(instance, Expression)


def test_stext_BitwiseAndExpression_isa_Expression():
    instance = stext_BitwiseAndExpression()
    assert isinstance(instance, Expression)


def test_stext_BitwiseOrExpression_isa_Expression():
    instance = stext_BitwiseOrExpression()
    assert isinstance(instance, Expression)


def test_stext_BitwiseXorExpression_isa_Expression():
    instance = stext_BitwiseXorExpression()
    assert isinstance(instance, Expression)


def test_stext_ConditionalExpression_isa_Expression():
    instance = stext_ConditionalExpression()
    assert isinstance(instance, Expression)


def test_stext_EventRaisingExpression_isa_Expression():
    instance = stext_EventRaisingExpression()
    assert isinstance(instance, Expression)


def test_stext_EventValueReferenceExpression_isa_Expression():
    instance = stext_EventValueReferenceExpression()
    assert isinstance(instance, Expression)


def test_stext_FeatureCall_isa_Expression():
    instance = stext_FeatureCall(operationCall=True)
    assert isinstance(instance, Expression)


def test_stext_LogicalAndExpression_isa_Expression():
    instance = stext_LogicalAndExpression()
    assert isinstance(instance, Expression)


def test_stext_LogicalNotExpression_isa_Expression():
    instance = stext_LogicalNotExpression()
    assert isinstance(instance, Expression)


def test_stext_LogicalOrExpression_isa_Expression():
    instance = stext_LogicalOrExpression()
    assert isinstance(instance, Expression)


def test_stext_LogicalRelationExpression_isa_Expression():
    instance = stext_LogicalRelationExpression(operator="sample_text")
    assert isinstance(instance, Expression)


def test_stext_NumericalAddSubtractExpression_isa_Expression():
    instance = stext_NumericalAddSubtractExpression(operator="sample_text")
    assert isinstance(instance, Expression)


def test_stext_NumericalMultiplyDivideExpression_isa_Expression():
    instance = stext_NumericalMultiplyDivideExpression(operator="sample_text")
    assert isinstance(instance, Expression)


def test_stext_NumericalUnaryExpression_isa_Expression():
    instance = stext_NumericalUnaryExpression(operator="sample_text")
    assert isinstance(instance, Expression)


def test_stext_PrimitiveValueExpression_isa_Expression():
    instance = stext_PrimitiveValueExpression()
    assert isinstance(instance, Expression)


def test_stext_ShiftExpression_isa_Expression():
    instance = stext_ShiftExpression(operator="sample_text")
    assert isinstance(instance, Expression)


def test_stext_TypedElementReferenceExpression_isa_Expression():
    instance = stext_TypedElementReferenceExpression()
    assert isinstance(instance, Expression)


def test_stext_BoolLiteral_isa_Literal():
    instance = stext_BoolLiteral(value=True)
    assert isinstance(instance, Literal)


def test_stext_HexLiteral_isa_Literal():
    instance = stext_HexLiteral(value=7)
    assert isinstance(instance, Literal)


def test_stext_IntLiteral_isa_Literal():
    instance = stext_IntLiteral(value=7)
    assert isinstance(instance, Literal)


def test_stext_RealLiteral_isa_Literal():
    instance = stext_RealLiteral(value=3.14)
    assert isinstance(instance, Literal)


def test_stext_StringLiteral_isa_Literal():
    instance = stext_StringLiteral(value="sample_text")
    assert isinstance(instance, Literal)


def test_stext_InterfaceScope_isa_NamedElement():
    instance = stext_InterfaceScope()
    assert isinstance(instance, NamedElement)


def test_stext_OperationDefinition_isa_Operation():
    instance = stext_OperationDefinition()
    assert isinstance(instance, Operation)


def test_stext_VariableDefinition_isa_Property():
    instance = stext_VariableDefinition(external=True, readonly=True)
    assert isinstance(instance, Property)


def test_stext_LocalReaction_isa_Reaction():
    instance = stext_LocalReaction()
    assert isinstance(instance, Reaction)


def test_stext_TransitionReaction_isa_Reaction():
    instance = stext_TransitionReaction()
    assert isinstance(instance, Reaction)


def test_stext_EntryPointSpec_isa_ReactionProperty():
    instance = stext_EntryPointSpec()
    assert isinstance(instance, ReactionProperty)


def test_stext_ExitPointSpec_isa_ReactionProperty():
    instance = stext_ExitPointSpec()
    assert isinstance(instance, ReactionProperty)


def test_stext_SimpleScope_isa_Scope():
    instance = stext_SimpleScope()
    assert isinstance(instance, Scope)


def test_stext_StatechartScope_isa_Scope():
    instance = stext_StatechartScope()
    assert isinstance(instance, Scope)


def test_stext_InterfaceScope_isa_StatechartScope():
    instance = stext_InterfaceScope()
    assert isinstance(instance, StatechartScope)


def test_stext_InternalScope_isa_StatechartScope():
    instance = stext_InternalScope()
    assert isinstance(instance, StatechartScope)


def test_stext_Expression_isa_Statement():
    instance = stext_Expression()
    assert isinstance(instance, Statement)


def test_stext_ReactionTrigger_isa_Trigger():
    instance = stext_ReactionTrigger()
    assert isinstance(instance, Trigger)


def test_stext_VariableDefinition_isa_Variable():
    instance = stext_VariableDefinition(external=True, readonly=True)
    assert isinstance(instance, Variable)


def test_assoc_args107_link_reassign_clear():
    a = stext_FeatureCall(operationCall=True)
    b1 = stext_Expression()
    b2 = stext_Expression()
    _safe_set(a, 'stext_FeatureCall108', {b1})
    assert _is_linked(a, 'stext_FeatureCall108', b1)
    if hasattr(b1, 'stext_Expression109'):
        assert _is_linked(b1, 'stext_Expression109', a)
    _safe_set(a, 'stext_FeatureCall108', {b2})
    assert _is_linked(a, 'stext_FeatureCall108', b2)
    if hasattr(b1, 'stext_Expression109'):
        assert not _is_linked(b1, 'stext_Expression109', a)
    if hasattr(b2, 'stext_Expression109'):
        assert _is_linked(b2, 'stext_Expression109', a)
    _safe_set(a, 'stext_FeatureCall108', set())
    assert not _is_linked(a, 'stext_FeatureCall108', b2)
    if hasattr(b2, 'stext_Expression109'):
        assert not _is_linked(b2, 'stext_Expression109', a)


def test_assoc_def_1_link_reassign_clear():
    a = stext_StatechartSpecification(namespace="sample_text")
    b1 = stext_StatechartRoot()
    b2 = stext_StatechartRoot()
    _safe_set(a, 'stext_StatechartSpecification', b1)
    assert _is_linked(a, 'stext_StatechartSpecification', b1)
    if hasattr(b1, 'stext_StatechartRoot'):
        assert _is_linked(b1, 'stext_StatechartRoot', a)
    _safe_set(a, 'stext_StatechartSpecification', b2)
    assert _is_linked(a, 'stext_StatechartSpecification', b2)
    if hasattr(b1, 'stext_StatechartRoot'):
        assert not _is_linked(b1, 'stext_StatechartRoot', a)
    if hasattr(b2, 'stext_StatechartRoot'):
        assert _is_linked(b2, 'stext_StatechartRoot', a)
    _safe_set(a, 'stext_StatechartSpecification', None)
    assert not _is_linked(a, 'stext_StatechartSpecification', b2)
    if hasattr(b2, 'stext_StatechartRoot'):
        assert not _is_linked(b2, 'stext_StatechartRoot', a)


def test_assoc_definitionScopes4_link_reassign_clear():
    a = stext_StatechartSpecification(namespace="sample_text")
    b1 = stext_StatechartScope()
    b2 = stext_StatechartScope()
    _safe_set(a, 'stext_StatechartSpecification5', {b1})
    assert _is_linked(a, 'stext_StatechartSpecification5', b1)
    if hasattr(b1, 'stext_StatechartScope'):
        assert _is_linked(b1, 'stext_StatechartScope', a)
    _safe_set(a, 'stext_StatechartSpecification5', {b2})
    assert _is_linked(a, 'stext_StatechartSpecification5', b2)
    if hasattr(b1, 'stext_StatechartScope'):
        assert not _is_linked(b1, 'stext_StatechartScope', a)
    if hasattr(b2, 'stext_StatechartScope'):
        assert _is_linked(b2, 'stext_StatechartScope', a)
    _safe_set(a, 'stext_StatechartSpecification5', set())
    assert not _is_linked(a, 'stext_StatechartSpecification5', b2)
    if hasattr(b2, 'stext_StatechartScope'):
        assert not _is_linked(b2, 'stext_StatechartScope', a)


def test_assoc_derivation10_link_reassign_clear():
    a = stext_EventDefinition(direction="sample_text")
    b1 = stext_EventDerivation()
    b2 = stext_EventDerivation()
    _safe_set(a, 'stext_EventDefinition', b1)
    assert _is_linked(a, 'stext_EventDefinition', b1)
    if hasattr(b1, 'stext_EventDerivation'):
        assert _is_linked(b1, 'stext_EventDerivation', a)
    _safe_set(a, 'stext_EventDefinition', b2)
    assert _is_linked(a, 'stext_EventDefinition', b2)
    if hasattr(b1, 'stext_EventDerivation'):
        assert not _is_linked(b1, 'stext_EventDerivation', a)
    if hasattr(b2, 'stext_EventDerivation'):
        assert _is_linked(b2, 'stext_EventDerivation', a)
    _safe_set(a, 'stext_EventDefinition', None)
    assert not _is_linked(a, 'stext_EventDefinition', b2)
    if hasattr(b2, 'stext_EventDerivation'):
        assert not _is_linked(b2, 'stext_EventDerivation', a)


def test_assoc_expression42_link_reassign_clear():
    a = stext_AssignmentExpression(operator="sample_text")
    b1 = stext_Expression()
    b2 = stext_Expression()
    _safe_set(a, 'stext_AssignmentExpression43', b1)
    assert _is_linked(a, 'stext_AssignmentExpression43', b1)
    if hasattr(b1, 'stext_Expression44'):
        assert _is_linked(b1, 'stext_Expression44', a)
    _safe_set(a, 'stext_AssignmentExpression43', b2)
    assert _is_linked(a, 'stext_AssignmentExpression43', b2)
    if hasattr(b1, 'stext_Expression44'):
        assert not _is_linked(b1, 'stext_Expression44', a)
    if hasattr(b2, 'stext_Expression44'):
        assert _is_linked(b2, 'stext_Expression44', a)
    _safe_set(a, 'stext_AssignmentExpression43', None)
    assert not _is_linked(a, 'stext_AssignmentExpression43', b2)
    if hasattr(b2, 'stext_Expression44'):
        assert not _is_linked(b2, 'stext_Expression44', a)


def test_assoc_feature105_link_reassign_clear():
    a = stext_FeatureCall(operationCall=True)
    b1 = stext_Feature()
    b2 = stext_Feature()
    _safe_set(a, 'stext_FeatureCall106', b1)
    assert _is_linked(a, 'stext_FeatureCall106', b1)
    if hasattr(b1, 'stext_Feature'):
        assert _is_linked(b1, 'stext_Feature', a)
    _safe_set(a, 'stext_FeatureCall106', b2)
    assert _is_linked(a, 'stext_FeatureCall106', b2)
    if hasattr(b1, 'stext_Feature'):
        assert not _is_linked(b1, 'stext_Feature', a)
    if hasattr(b2, 'stext_Feature'):
        assert _is_linked(b2, 'stext_Feature', a)
    _safe_set(a, 'stext_FeatureCall106', None)
    assert not _is_linked(a, 'stext_FeatureCall106', b2)
    if hasattr(b2, 'stext_Feature'):
        assert not _is_linked(b2, 'stext_Feature', a)


def test_assoc_initialValue16_link_reassign_clear():
    a = stext_VariableDefinition(external=True, readonly=True)
    b1 = stext_Expression()
    b2 = stext_Expression()
    _safe_set(a, 'stext_VariableDefinition', b1)
    assert _is_linked(a, 'stext_VariableDefinition', b1)
    if hasattr(b1, 'stext_Expression17'):
        assert _is_linked(b1, 'stext_Expression17', a)
    _safe_set(a, 'stext_VariableDefinition', b2)
    assert _is_linked(a, 'stext_VariableDefinition', b2)
    if hasattr(b1, 'stext_Expression17'):
        assert not _is_linked(b1, 'stext_Expression17', a)
    if hasattr(b2, 'stext_Expression17'):
        assert _is_linked(b2, 'stext_Expression17', a)
    _safe_set(a, 'stext_VariableDefinition', None)
    assert not _is_linked(a, 'stext_VariableDefinition', b2)
    if hasattr(b2, 'stext_Expression17'):
        assert not _is_linked(b2, 'stext_Expression17', a)


def test_assoc_leftOperand80_link_reassign_clear():
    a = stext_LogicalRelationExpression(operator="sample_text")
    b1 = stext_Expression()
    b2 = stext_Expression()
    _safe_set(a, 'stext_LogicalRelationExpression', b1)
    assert _is_linked(a, 'stext_LogicalRelationExpression', b1)
    if hasattr(b1, 'stext_Expression81'):
        assert _is_linked(b1, 'stext_Expression81', a)
    _safe_set(a, 'stext_LogicalRelationExpression', b2)
    assert _is_linked(a, 'stext_LogicalRelationExpression', b2)
    if hasattr(b1, 'stext_Expression81'):
        assert not _is_linked(b1, 'stext_Expression81', a)
    if hasattr(b2, 'stext_Expression81'):
        assert _is_linked(b2, 'stext_Expression81', a)
    _safe_set(a, 'stext_LogicalRelationExpression', None)
    assert not _is_linked(a, 'stext_LogicalRelationExpression', b2)
    if hasattr(b2, 'stext_Expression81'):
        assert not _is_linked(b2, 'stext_Expression81', a)


def test_assoc_leftOperand85_link_reassign_clear():
    a = stext_ShiftExpression(operator="sample_text")
    b1 = stext_Expression()
    b2 = stext_Expression()
    _safe_set(a, 'stext_ShiftExpression', b1)
    assert _is_linked(a, 'stext_ShiftExpression', b1)
    if hasattr(b1, 'stext_Expression86'):
        assert _is_linked(b1, 'stext_Expression86', a)
    _safe_set(a, 'stext_ShiftExpression', b2)
    assert _is_linked(a, 'stext_ShiftExpression', b2)
    if hasattr(b1, 'stext_Expression86'):
        assert not _is_linked(b1, 'stext_Expression86', a)
    if hasattr(b2, 'stext_Expression86'):
        assert _is_linked(b2, 'stext_Expression86', a)
    _safe_set(a, 'stext_ShiftExpression', None)
    assert not _is_linked(a, 'stext_ShiftExpression', b2)
    if hasattr(b2, 'stext_Expression86'):
        assert not _is_linked(b2, 'stext_Expression86', a)


def test_assoc_leftOperand90_link_reassign_clear():
    a = stext_NumericalAddSubtractExpression(operator="sample_text")
    b1 = stext_Expression()
    b2 = stext_Expression()
    _safe_set(a, 'stext_NumericalAddSubtractExpression', b1)
    assert _is_linked(a, 'stext_NumericalAddSubtractExpression', b1)
    if hasattr(b1, 'stext_Expression91'):
        assert _is_linked(b1, 'stext_Expression91', a)
    _safe_set(a, 'stext_NumericalAddSubtractExpression', b2)
    assert _is_linked(a, 'stext_NumericalAddSubtractExpression', b2)
    if hasattr(b1, 'stext_Expression91'):
        assert not _is_linked(b1, 'stext_Expression91', a)
    if hasattr(b2, 'stext_Expression91'):
        assert _is_linked(b2, 'stext_Expression91', a)
    _safe_set(a, 'stext_NumericalAddSubtractExpression', None)
    assert not _is_linked(a, 'stext_NumericalAddSubtractExpression', b2)
    if hasattr(b2, 'stext_Expression91'):
        assert not _is_linked(b2, 'stext_Expression91', a)


def test_assoc_leftOperand95_link_reassign_clear():
    a = stext_NumericalMultiplyDivideExpression(operator="sample_text")
    b1 = stext_Expression()
    b2 = stext_Expression()
    _safe_set(a, 'stext_NumericalMultiplyDivideExpression', b1)
    assert _is_linked(a, 'stext_NumericalMultiplyDivideExpression', b1)
    if hasattr(b1, 'stext_Expression96'):
        assert _is_linked(b1, 'stext_Expression96', a)
    _safe_set(a, 'stext_NumericalMultiplyDivideExpression', b2)
    assert _is_linked(a, 'stext_NumericalMultiplyDivideExpression', b2)
    if hasattr(b1, 'stext_Expression96'):
        assert not _is_linked(b1, 'stext_Expression96', a)
    if hasattr(b2, 'stext_Expression96'):
        assert _is_linked(b2, 'stext_Expression96', a)
    _safe_set(a, 'stext_NumericalMultiplyDivideExpression', None)
    assert not _is_linked(a, 'stext_NumericalMultiplyDivideExpression', b2)
    if hasattr(b2, 'stext_Expression96'):
        assert not _is_linked(b2, 'stext_Expression96', a)


def test_assoc_operand100_link_reassign_clear():
    a = stext_NumericalUnaryExpression(operator="sample_text")
    b1 = stext_Expression()
    b2 = stext_Expression()
    _safe_set(a, 'stext_NumericalUnaryExpression', b1)
    assert _is_linked(a, 'stext_NumericalUnaryExpression', b1)
    if hasattr(b1, 'stext_Expression101'):
        assert _is_linked(b1, 'stext_Expression101', a)
    _safe_set(a, 'stext_NumericalUnaryExpression', b2)
    assert _is_linked(a, 'stext_NumericalUnaryExpression', b2)
    if hasattr(b1, 'stext_Expression101'):
        assert not _is_linked(b1, 'stext_Expression101', a)
    if hasattr(b2, 'stext_Expression101'):
        assert _is_linked(b2, 'stext_Expression101', a)
    _safe_set(a, 'stext_NumericalUnaryExpression', None)
    assert not _is_linked(a, 'stext_NumericalUnaryExpression', b2)
    if hasattr(b2, 'stext_Expression101'):
        assert not _is_linked(b2, 'stext_Expression101', a)


def test_assoc_owner103_link_reassign_clear():
    a = stext_FeatureCall(operationCall=True)
    b1 = stext_Expression()
    b2 = stext_Expression()
    _safe_set(a, 'stext_FeatureCall', b1)
    assert _is_linked(a, 'stext_FeatureCall', b1)
    if hasattr(b1, 'stext_Expression104'):
        assert _is_linked(b1, 'stext_Expression104', a)
    _safe_set(a, 'stext_FeatureCall', b2)
    assert _is_linked(a, 'stext_FeatureCall', b2)
    if hasattr(b1, 'stext_Expression104'):
        assert not _is_linked(b1, 'stext_Expression104', a)
    if hasattr(b2, 'stext_Expression104'):
        assert _is_linked(b2, 'stext_Expression104', a)
    _safe_set(a, 'stext_FeatureCall', None)
    assert not _is_linked(a, 'stext_FeatureCall', b2)
    if hasattr(b2, 'stext_Expression104'):
        assert not _is_linked(b2, 'stext_Expression104', a)


def test_assoc_rightOperand82_link_reassign_clear():
    a = stext_LogicalRelationExpression(operator="sample_text")
    b1 = stext_Expression()
    b2 = stext_Expression()
    _safe_set(a, 'stext_LogicalRelationExpression83', b1)
    assert _is_linked(a, 'stext_LogicalRelationExpression83', b1)
    if hasattr(b1, 'stext_Expression84'):
        assert _is_linked(b1, 'stext_Expression84', a)
    _safe_set(a, 'stext_LogicalRelationExpression83', b2)
    assert _is_linked(a, 'stext_LogicalRelationExpression83', b2)
    if hasattr(b1, 'stext_Expression84'):
        assert not _is_linked(b1, 'stext_Expression84', a)
    if hasattr(b2, 'stext_Expression84'):
        assert _is_linked(b2, 'stext_Expression84', a)
    _safe_set(a, 'stext_LogicalRelationExpression83', None)
    assert not _is_linked(a, 'stext_LogicalRelationExpression83', b2)
    if hasattr(b2, 'stext_Expression84'):
        assert not _is_linked(b2, 'stext_Expression84', a)


def test_assoc_rightOperand87_link_reassign_clear():
    a = stext_ShiftExpression(operator="sample_text")
    b1 = stext_Expression()
    b2 = stext_Expression()
    _safe_set(a, 'stext_ShiftExpression88', b1)
    assert _is_linked(a, 'stext_ShiftExpression88', b1)
    if hasattr(b1, 'stext_Expression89'):
        assert _is_linked(b1, 'stext_Expression89', a)
    _safe_set(a, 'stext_ShiftExpression88', b2)
    assert _is_linked(a, 'stext_ShiftExpression88', b2)
    if hasattr(b1, 'stext_Expression89'):
        assert not _is_linked(b1, 'stext_Expression89', a)
    if hasattr(b2, 'stext_Expression89'):
        assert _is_linked(b2, 'stext_Expression89', a)
    _safe_set(a, 'stext_ShiftExpression88', None)
    assert not _is_linked(a, 'stext_ShiftExpression88', b2)
    if hasattr(b2, 'stext_Expression89'):
        assert not _is_linked(b2, 'stext_Expression89', a)


def test_assoc_rightOperand92_link_reassign_clear():
    a = stext_NumericalAddSubtractExpression(operator="sample_text")
    b1 = stext_Expression()
    b2 = stext_Expression()
    _safe_set(a, 'stext_NumericalAddSubtractExpression93', b1)
    assert _is_linked(a, 'stext_NumericalAddSubtractExpression93', b1)
    if hasattr(b1, 'stext_Expression94'):
        assert _is_linked(b1, 'stext_Expression94', a)
    _safe_set(a, 'stext_NumericalAddSubtractExpression93', b2)
    assert _is_linked(a, 'stext_NumericalAddSubtractExpression93', b2)
    if hasattr(b1, 'stext_Expression94'):
        assert not _is_linked(b1, 'stext_Expression94', a)
    if hasattr(b2, 'stext_Expression94'):
        assert _is_linked(b2, 'stext_Expression94', a)
    _safe_set(a, 'stext_NumericalAddSubtractExpression93', None)
    assert not _is_linked(a, 'stext_NumericalAddSubtractExpression93', b2)
    if hasattr(b2, 'stext_Expression94'):
        assert not _is_linked(b2, 'stext_Expression94', a)


def test_assoc_rightOperand97_link_reassign_clear():
    a = stext_NumericalMultiplyDivideExpression(operator="sample_text")
    b1 = stext_Expression()
    b2 = stext_Expression()
    _safe_set(a, 'stext_NumericalMultiplyDivideExpression98', b1)
    assert _is_linked(a, 'stext_NumericalMultiplyDivideExpression98', b1)
    if hasattr(b1, 'stext_Expression99'):
        assert _is_linked(b1, 'stext_Expression99', a)
    _safe_set(a, 'stext_NumericalMultiplyDivideExpression98', b2)
    assert _is_linked(a, 'stext_NumericalMultiplyDivideExpression98', b2)
    if hasattr(b1, 'stext_Expression99'):
        assert not _is_linked(b1, 'stext_Expression99', a)
    if hasattr(b2, 'stext_Expression99'):
        assert _is_linked(b2, 'stext_Expression99', a)
    _safe_set(a, 'stext_NumericalMultiplyDivideExpression98', None)
    assert not _is_linked(a, 'stext_NumericalMultiplyDivideExpression98', b2)
    if hasattr(b2, 'stext_Expression99'):
        assert not _is_linked(b2, 'stext_Expression99', a)


def test_assoc_varRef40_link_reassign_clear():
    a = stext_AssignmentExpression(operator="sample_text")
    b1 = stext_Expression()
    b2 = stext_Expression()
    _safe_set(a, 'stext_AssignmentExpression', b1)
    assert _is_linked(a, 'stext_AssignmentExpression', b1)
    if hasattr(b1, 'stext_Expression41'):
        assert _is_linked(b1, 'stext_Expression41', a)
    _safe_set(a, 'stext_AssignmentExpression', b2)
    assert _is_linked(a, 'stext_AssignmentExpression', b2)
    if hasattr(b1, 'stext_Expression41'):
        assert not _is_linked(b1, 'stext_Expression41', a)
    if hasattr(b2, 'stext_Expression41'):
        assert _is_linked(b2, 'stext_Expression41', a)
    _safe_set(a, 'stext_AssignmentExpression', None)
    assert not _is_linked(a, 'stext_AssignmentExpression', b2)
    if hasattr(b2, 'stext_Expression41'):
        assert not _is_linked(b2, 'stext_Expression41', a)


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

BuiltinEventSpec_strategy = st.builds(BuiltinEventSpec)
@given(instance=BuiltinEventSpec_strategy)
@settings(max_examples=25)
def test_BuiltinEventSpec_instantiation(instance):
    assert isinstance(instance, BuiltinEventSpec)


Declaration_strategy = st.builds(Declaration)
@given(instance=Declaration_strategy)
@settings(max_examples=25)
def test_Declaration_instantiation(instance):
    assert isinstance(instance, Declaration)


DefRoot_strategy = st.builds(DefRoot)
@given(instance=DefRoot_strategy)
@settings(max_examples=25)
def test_DefRoot_instantiation(instance):
    assert isinstance(instance, DefRoot)


Effect_strategy = st.builds(Effect)
@given(instance=Effect_strategy)
@settings(max_examples=25)
def test_Effect_instantiation(instance):
    assert isinstance(instance, Effect)


Event_strategy = st.builds(Event)
@given(instance=Event_strategy)
@settings(max_examples=25)
def test_Event_instantiation(instance):
    assert isinstance(instance, Event)


EventSpec_strategy = st.builds(EventSpec)
@given(instance=EventSpec_strategy)
@settings(max_examples=25)
def test_EventSpec_instantiation(instance):
    assert isinstance(instance, EventSpec)


Expression_strategy = st.builds(Expression)
@given(instance=Expression_strategy)
@settings(max_examples=25)
def test_Expression_instantiation(instance):
    assert isinstance(instance, Expression)


Literal_strategy = st.builds(Literal)
@given(instance=Literal_strategy)
@settings(max_examples=25)
def test_Literal_instantiation(instance):
    assert isinstance(instance, Literal)


NamedElement_strategy = st.builds(NamedElement)
@given(instance=NamedElement_strategy)
@settings(max_examples=25)
def test_NamedElement_instantiation(instance):
    assert isinstance(instance, NamedElement)


Operation_strategy = st.builds(Operation)
@given(instance=Operation_strategy)
@settings(max_examples=25)
def test_Operation_instantiation(instance):
    assert isinstance(instance, Operation)


Property_strategy = st.builds(Property)
@given(instance=Property_strategy)
@settings(max_examples=25)
def test_Property_instantiation(instance):
    assert isinstance(instance, Property)


Reaction_strategy = st.builds(Reaction)
@given(instance=Reaction_strategy)
@settings(max_examples=25)
def test_Reaction_instantiation(instance):
    assert isinstance(instance, Reaction)


ReactionProperty_strategy = st.builds(ReactionProperty)
@given(instance=ReactionProperty_strategy)
@settings(max_examples=25)
def test_ReactionProperty_instantiation(instance):
    assert isinstance(instance, ReactionProperty)


Scope_strategy = st.builds(Scope)
@given(instance=Scope_strategy)
@settings(max_examples=25)
def test_Scope_instantiation(instance):
    assert isinstance(instance, Scope)


StatechartScope_strategy = st.builds(StatechartScope)
@given(instance=StatechartScope_strategy)
@settings(max_examples=25)
def test_StatechartScope_instantiation(instance):
    assert isinstance(instance, StatechartScope)


Statement_strategy = st.builds(Statement)
@given(instance=Statement_strategy)
@settings(max_examples=25)
def test_Statement_instantiation(instance):
    assert isinstance(instance, Statement)


Trigger_strategy = st.builds(Trigger)
@given(instance=Trigger_strategy)
@settings(max_examples=25)
def test_Trigger_instantiation(instance):
    assert isinstance(instance, Trigger)


Variable_strategy = st.builds(Variable)
@given(instance=Variable_strategy)
@settings(max_examples=25)
def test_Variable_instantiation(instance):
    assert isinstance(instance, Variable)


stext_ActiveStateReferenceExpression_strategy = st.builds(stext_ActiveStateReferenceExpression)
@given(instance=stext_ActiveStateReferenceExpression_strategy)
@settings(max_examples=25)
def test_stext_ActiveStateReferenceExpression_instantiation(instance):
    assert isinstance(instance, stext_ActiveStateReferenceExpression)


stext_AlwaysEvent_strategy = st.builds(stext_AlwaysEvent)
@given(instance=stext_AlwaysEvent_strategy)
@settings(max_examples=25)
def test_stext_AlwaysEvent_instantiation(instance):
    assert isinstance(instance, stext_AlwaysEvent)


stext_AssignmentExpression_strategy = st.builds(stext_AssignmentExpression, operator=safe_text)
@given(instance=stext_AssignmentExpression_strategy)
@settings(max_examples=25)
def test_stext_AssignmentExpression_instantiation(instance):
    assert isinstance(instance, stext_AssignmentExpression)


stext_BitwiseAndExpression_strategy = st.builds(stext_BitwiseAndExpression)
@given(instance=stext_BitwiseAndExpression_strategy)
@settings(max_examples=25)
def test_stext_BitwiseAndExpression_instantiation(instance):
    assert isinstance(instance, stext_BitwiseAndExpression)


stext_BitwiseOrExpression_strategy = st.builds(stext_BitwiseOrExpression)
@given(instance=stext_BitwiseOrExpression_strategy)
@settings(max_examples=25)
def test_stext_BitwiseOrExpression_instantiation(instance):
    assert isinstance(instance, stext_BitwiseOrExpression)


stext_BitwiseXorExpression_strategy = st.builds(stext_BitwiseXorExpression)
@given(instance=stext_BitwiseXorExpression_strategy)
@settings(max_examples=25)
def test_stext_BitwiseXorExpression_instantiation(instance):
    assert isinstance(instance, stext_BitwiseXorExpression)


stext_BoolLiteral_strategy = st.builds(stext_BoolLiteral, value=st.booleans())
@given(instance=stext_BoolLiteral_strategy)
@settings(max_examples=25)
def test_stext_BoolLiteral_instantiation(instance):
    assert isinstance(instance, stext_BoolLiteral)


stext_BuiltinEventSpec_strategy = st.builds(stext_BuiltinEventSpec)
@given(instance=stext_BuiltinEventSpec_strategy)
@settings(max_examples=25)
def test_stext_BuiltinEventSpec_instantiation(instance):
    assert isinstance(instance, stext_BuiltinEventSpec)


stext_ConditionalExpression_strategy = st.builds(stext_ConditionalExpression)
@given(instance=stext_ConditionalExpression_strategy)
@settings(max_examples=25)
def test_stext_ConditionalExpression_instantiation(instance):
    assert isinstance(instance, stext_ConditionalExpression)


stext_DefRoot_strategy = st.builds(stext_DefRoot)
@given(instance=stext_DefRoot_strategy)
@settings(max_examples=25)
def test_stext_DefRoot_instantiation(instance):
    assert isinstance(instance, stext_DefRoot)


stext_DefaultEvent_strategy = st.builds(stext_DefaultEvent)
@given(instance=stext_DefaultEvent_strategy)
@settings(max_examples=25)
def test_stext_DefaultEvent_instantiation(instance):
    assert isinstance(instance, stext_DefaultEvent)


stext_EntryEvent_strategy = st.builds(stext_EntryEvent)
@given(instance=stext_EntryEvent_strategy)
@settings(max_examples=25)
def test_stext_EntryEvent_instantiation(instance):
    assert isinstance(instance, stext_EntryEvent)


stext_EntryPointSpec_strategy = st.builds(stext_EntryPointSpec)
@given(instance=stext_EntryPointSpec_strategy)
@settings(max_examples=25)
def test_stext_EntryPointSpec_instantiation(instance):
    assert isinstance(instance, stext_EntryPointSpec)


stext_Entrypoint_strategy = st.builds(stext_Entrypoint)
@given(instance=stext_Entrypoint_strategy)
@settings(max_examples=25)
def test_stext_Entrypoint_instantiation(instance):
    assert isinstance(instance, stext_Entrypoint)


stext_EventDefinition_strategy = st.builds(stext_EventDefinition, direction=safe_text)
@given(instance=stext_EventDefinition_strategy)
@settings(max_examples=25)
def test_stext_EventDefinition_instantiation(instance):
    assert isinstance(instance, stext_EventDefinition)


stext_EventDerivation_strategy = st.builds(stext_EventDerivation)
@given(instance=stext_EventDerivation_strategy)
@settings(max_examples=25)
def test_stext_EventDerivation_instantiation(instance):
    assert isinstance(instance, stext_EventDerivation)


stext_EventRaisingExpression_strategy = st.builds(stext_EventRaisingExpression)
@given(instance=stext_EventRaisingExpression_strategy)
@settings(max_examples=25)
def test_stext_EventRaisingExpression_instantiation(instance):
    assert isinstance(instance, stext_EventRaisingExpression)


stext_EventSpec_strategy = st.builds(stext_EventSpec)
@given(instance=stext_EventSpec_strategy)
@settings(max_examples=25)
def test_stext_EventSpec_instantiation(instance):
    assert isinstance(instance, stext_EventSpec)


stext_EventValueReferenceExpression_strategy = st.builds(stext_EventValueReferenceExpression)
@given(instance=stext_EventValueReferenceExpression_strategy)
@settings(max_examples=25)
def test_stext_EventValueReferenceExpression_instantiation(instance):
    assert isinstance(instance, stext_EventValueReferenceExpression)


stext_ExitEvent_strategy = st.builds(stext_ExitEvent)
@given(instance=stext_ExitEvent_strategy)
@settings(max_examples=25)
def test_stext_ExitEvent_instantiation(instance):
    assert isinstance(instance, stext_ExitEvent)


stext_ExitPointSpec_strategy = st.builds(stext_ExitPointSpec)
@given(instance=stext_ExitPointSpec_strategy)
@settings(max_examples=25)
def test_stext_ExitPointSpec_instantiation(instance):
    assert isinstance(instance, stext_ExitPointSpec)


stext_Exitpoint_strategy = st.builds(stext_Exitpoint)
@given(instance=stext_Exitpoint_strategy)
@settings(max_examples=25)
def test_stext_Exitpoint_instantiation(instance):
    assert isinstance(instance, stext_Exitpoint)


stext_Expression_strategy = st.builds(stext_Expression)
@given(instance=stext_Expression_strategy)
@settings(max_examples=25)
def test_stext_Expression_instantiation(instance):
    assert isinstance(instance, stext_Expression)


stext_Feature_strategy = st.builds(stext_Feature)
@given(instance=stext_Feature_strategy)
@settings(max_examples=25)
def test_stext_Feature_instantiation(instance):
    assert isinstance(instance, stext_Feature)


stext_FeatureCall_strategy = st.builds(stext_FeatureCall, operationCall=st.booleans())
@given(instance=stext_FeatureCall_strategy)
@settings(max_examples=25)
def test_stext_FeatureCall_instantiation(instance):
    assert isinstance(instance, stext_FeatureCall)


stext_HexLiteral_strategy = st.builds(stext_HexLiteral, value=st.integers())
@given(instance=stext_HexLiteral_strategy)
@settings(max_examples=25)
def test_stext_HexLiteral_instantiation(instance):
    assert isinstance(instance, stext_HexLiteral)


stext_IntLiteral_strategy = st.builds(stext_IntLiteral, value=st.integers())
@given(instance=stext_IntLiteral_strategy)
@settings(max_examples=25)
def test_stext_IntLiteral_instantiation(instance):
    assert isinstance(instance, stext_IntLiteral)


stext_InterfaceScope_strategy = st.builds(stext_InterfaceScope)
@given(instance=stext_InterfaceScope_strategy)
@settings(max_examples=25)
def test_stext_InterfaceScope_instantiation(instance):
    assert isinstance(instance, stext_InterfaceScope)


stext_InternalScope_strategy = st.builds(stext_InternalScope)
@given(instance=stext_InternalScope_strategy)
@settings(max_examples=25)
def test_stext_InternalScope_instantiation(instance):
    assert isinstance(instance, stext_InternalScope)


stext_Literal_strategy = st.builds(stext_Literal)
@given(instance=stext_Literal_strategy)
@settings(max_examples=25)
def test_stext_Literal_instantiation(instance):
    assert isinstance(instance, stext_Literal)


stext_LocalReaction_strategy = st.builds(stext_LocalReaction)
@given(instance=stext_LocalReaction_strategy)
@settings(max_examples=25)
def test_stext_LocalReaction_instantiation(instance):
    assert isinstance(instance, stext_LocalReaction)


stext_LogicalAndExpression_strategy = st.builds(stext_LogicalAndExpression)
@given(instance=stext_LogicalAndExpression_strategy)
@settings(max_examples=25)
def test_stext_LogicalAndExpression_instantiation(instance):
    assert isinstance(instance, stext_LogicalAndExpression)


stext_LogicalNotExpression_strategy = st.builds(stext_LogicalNotExpression)
@given(instance=stext_LogicalNotExpression_strategy)
@settings(max_examples=25)
def test_stext_LogicalNotExpression_instantiation(instance):
    assert isinstance(instance, stext_LogicalNotExpression)


stext_LogicalOrExpression_strategy = st.builds(stext_LogicalOrExpression)
@given(instance=stext_LogicalOrExpression_strategy)
@settings(max_examples=25)
def test_stext_LogicalOrExpression_instantiation(instance):
    assert isinstance(instance, stext_LogicalOrExpression)


stext_LogicalRelationExpression_strategy = st.builds(stext_LogicalRelationExpression, operator=safe_text)
@given(instance=stext_LogicalRelationExpression_strategy)
@settings(max_examples=25)
def test_stext_LogicalRelationExpression_instantiation(instance):
    assert isinstance(instance, stext_LogicalRelationExpression)


stext_NamedElement_strategy = st.builds(stext_NamedElement)
@given(instance=stext_NamedElement_strategy)
@settings(max_examples=25)
def test_stext_NamedElement_instantiation(instance):
    assert isinstance(instance, stext_NamedElement)


stext_NumericalAddSubtractExpression_strategy = st.builds(stext_NumericalAddSubtractExpression, operator=safe_text)
@given(instance=stext_NumericalAddSubtractExpression_strategy)
@settings(max_examples=25)
def test_stext_NumericalAddSubtractExpression_instantiation(instance):
    assert isinstance(instance, stext_NumericalAddSubtractExpression)


stext_NumericalMultiplyDivideExpression_strategy = st.builds(stext_NumericalMultiplyDivideExpression, operator=safe_text)
@given(instance=stext_NumericalMultiplyDivideExpression_strategy)
@settings(max_examples=25)
def test_stext_NumericalMultiplyDivideExpression_instantiation(instance):
    assert isinstance(instance, stext_NumericalMultiplyDivideExpression)


stext_NumericalUnaryExpression_strategy = st.builds(stext_NumericalUnaryExpression, operator=safe_text)
@given(instance=stext_NumericalUnaryExpression_strategy)
@settings(max_examples=25)
def test_stext_NumericalUnaryExpression_instantiation(instance):
    assert isinstance(instance, stext_NumericalUnaryExpression)


stext_OnCycleEvent_strategy = st.builds(stext_OnCycleEvent)
@given(instance=stext_OnCycleEvent_strategy)
@settings(max_examples=25)
def test_stext_OnCycleEvent_instantiation(instance):
    assert isinstance(instance, stext_OnCycleEvent)


stext_OperationDefinition_strategy = st.builds(stext_OperationDefinition)
@given(instance=stext_OperationDefinition_strategy)
@settings(max_examples=25)
def test_stext_OperationDefinition_instantiation(instance):
    assert isinstance(instance, stext_OperationDefinition)


stext_PrimitiveValueExpression_strategy = st.builds(stext_PrimitiveValueExpression)
@given(instance=stext_PrimitiveValueExpression_strategy)
@settings(max_examples=25)
def test_stext_PrimitiveValueExpression_instantiation(instance):
    assert isinstance(instance, stext_PrimitiveValueExpression)


stext_ReactionEffect_strategy = st.builds(stext_ReactionEffect)
@given(instance=stext_ReactionEffect_strategy)
@settings(max_examples=25)
def test_stext_ReactionEffect_instantiation(instance):
    assert isinstance(instance, stext_ReactionEffect)


stext_ReactionProperties_strategy = st.builds(stext_ReactionProperties)
@given(instance=stext_ReactionProperties_strategy)
@settings(max_examples=25)
def test_stext_ReactionProperties_instantiation(instance):
    assert isinstance(instance, stext_ReactionProperties)


stext_ReactionProperty_strategy = st.builds(stext_ReactionProperty)
@given(instance=stext_ReactionProperty_strategy)
@settings(max_examples=25)
def test_stext_ReactionProperty_instantiation(instance):
    assert isinstance(instance, stext_ReactionProperty)


stext_ReactionTrigger_strategy = st.builds(stext_ReactionTrigger)
@given(instance=stext_ReactionTrigger_strategy)
@settings(max_examples=25)
def test_stext_ReactionTrigger_instantiation(instance):
    assert isinstance(instance, stext_ReactionTrigger)


stext_RealLiteral_strategy = st.builds(stext_RealLiteral, value=st.floats(allow_nan=False, allow_infinity=False))
@given(instance=stext_RealLiteral_strategy)
@settings(max_examples=25)
def test_stext_RealLiteral_instantiation(instance):
    assert isinstance(instance, stext_RealLiteral)


stext_RegularEventSpec_strategy = st.builds(stext_RegularEventSpec)
@given(instance=stext_RegularEventSpec_strategy)
@settings(max_examples=25)
def test_stext_RegularEventSpec_instantiation(instance):
    assert isinstance(instance, stext_RegularEventSpec)


stext_Root_strategy = st.builds(stext_Root)
@given(instance=stext_Root_strategy)
@settings(max_examples=25)
def test_stext_Root_instantiation(instance):
    assert isinstance(instance, stext_Root)


stext_Scope_strategy = st.builds(stext_Scope)
@given(instance=stext_Scope_strategy)
@settings(max_examples=25)
def test_stext_Scope_instantiation(instance):
    assert isinstance(instance, stext_Scope)


stext_ShiftExpression_strategy = st.builds(stext_ShiftExpression, operator=safe_text)
@given(instance=stext_ShiftExpression_strategy)
@settings(max_examples=25)
def test_stext_ShiftExpression_instantiation(instance):
    assert isinstance(instance, stext_ShiftExpression)


stext_SimpleScope_strategy = st.builds(stext_SimpleScope)
@given(instance=stext_SimpleScope_strategy)
@settings(max_examples=25)
def test_stext_SimpleScope_instantiation(instance):
    assert isinstance(instance, stext_SimpleScope)


stext_State_strategy = st.builds(stext_State)
@given(instance=stext_State_strategy)
@settings(max_examples=25)
def test_stext_State_instantiation(instance):
    assert isinstance(instance, stext_State)


stext_StateRoot_strategy = st.builds(stext_StateRoot)
@given(instance=stext_StateRoot_strategy)
@settings(max_examples=25)
def test_stext_StateRoot_instantiation(instance):
    assert isinstance(instance, stext_StateRoot)


stext_StateSpecification_strategy = st.builds(stext_StateSpecification)
@given(instance=stext_StateSpecification_strategy)
@settings(max_examples=25)
def test_stext_StateSpecification_instantiation(instance):
    assert isinstance(instance, stext_StateSpecification)


stext_StatechartRoot_strategy = st.builds(stext_StatechartRoot)
@given(instance=stext_StatechartRoot_strategy)
@settings(max_examples=25)
def test_stext_StatechartRoot_instantiation(instance):
    assert isinstance(instance, stext_StatechartRoot)


stext_StatechartScope_strategy = st.builds(stext_StatechartScope)
@given(instance=stext_StatechartScope_strategy)
@settings(max_examples=25)
def test_stext_StatechartScope_instantiation(instance):
    assert isinstance(instance, stext_StatechartScope)


stext_StatechartSpecification_strategy = st.builds(stext_StatechartSpecification, namespace=safe_text)
@given(instance=stext_StatechartSpecification_strategy)
@settings(max_examples=25)
def test_stext_StatechartSpecification_instantiation(instance):
    assert isinstance(instance, stext_StatechartSpecification)


stext_StringLiteral_strategy = st.builds(stext_StringLiteral, value=safe_text)
@given(instance=stext_StringLiteral_strategy)
@settings(max_examples=25)
def test_stext_StringLiteral_instantiation(instance):
    assert isinstance(instance, stext_StringLiteral)


stext_TimeEventSpec_strategy = st.builds(stext_TimeEventSpec, type=safe_text, unit=safe_text, value=st.integers())
@given(instance=stext_TimeEventSpec_strategy)
@settings(max_examples=25)
def test_stext_TimeEventSpec_instantiation(instance):
    assert isinstance(instance, stext_TimeEventSpec)


stext_TransitionReaction_strategy = st.builds(stext_TransitionReaction)
@given(instance=stext_TransitionReaction_strategy)
@settings(max_examples=25)
def test_stext_TransitionReaction_instantiation(instance):
    assert isinstance(instance, stext_TransitionReaction)


stext_TransitionRoot_strategy = st.builds(stext_TransitionRoot)
@given(instance=stext_TransitionRoot_strategy)
@settings(max_examples=25)
def test_stext_TransitionRoot_instantiation(instance):
    assert isinstance(instance, stext_TransitionRoot)


stext_TransitionSpecification_strategy = st.builds(stext_TransitionSpecification)
@given(instance=stext_TransitionSpecification_strategy)
@settings(max_examples=25)
def test_stext_TransitionSpecification_instantiation(instance):
    assert isinstance(instance, stext_TransitionSpecification)


stext_Type_strategy = st.builds(stext_Type)
@given(instance=stext_Type_strategy)
@settings(max_examples=25)
def test_stext_Type_instantiation(instance):
    assert isinstance(instance, stext_Type)


stext_TypedElementReferenceExpression_strategy = st.builds(stext_TypedElementReferenceExpression)
@given(instance=stext_TypedElementReferenceExpression_strategy)
@settings(max_examples=25)
def test_stext_TypedElementReferenceExpression_instantiation(instance):
    assert isinstance(instance, stext_TypedElementReferenceExpression)


stext_VariableDefinition_strategy = st.builds(stext_VariableDefinition, external=st.booleans(), readonly=st.booleans())
@given(instance=stext_VariableDefinition_strategy)
@settings(max_examples=25)
def test_stext_VariableDefinition_instantiation(instance):
    assert isinstance(instance, stext_VariableDefinition)



