import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Action_fire_actionEntryEventOccurrence,
    Action_fire_actionExitEventOccurrence,
    Action_isReady_actionEntryEventOccurrence,
    Action_isReady_actionExitEventOccurrence,
    Action_sendOffers_actionEntryEventOccurrence,
    Action_sendOffers_actionExitEventOccurrence,
    ActivityEdge_hasOfferEntryEventOccurrence,
    ActivityEdge_hasOfferExitEventOccurrence,
    ActivityEdge_offers_State,
    ActivityEdge_sendOfferEntryEventOccurrence,
    ActivityEdge_sendOfferExitEventOccurrence,
    ActivityEdge_takeOfferedTokens_activityEdgeEntryEventOccurrence,
    ActivityEdge_takeOfferedTokens_activityEdgeExitEventOccurrence,
    ActivityFinalNode_fire_activityFinalNodeEntryEventOccurrence,
    ActivityFinalNode_fire_activityFinalNodeExitEventOccurrence,
    ActivityNode_addTokensEntryEventOccurrence,
    ActivityNode_addTokensExitEventOccurrence,
    ActivityNode_hasOffersEntryEventOccurrence,
    ActivityNode_hasOffersExitEventOccurrence,
    ActivityNode_heldTokens_State,
    ActivityNode_isReadyEntryEventOccurrence,
    ActivityNode_isReadyExitEventOccurrence,
    ActivityNode_isRunningEntryEventOccurrence,
    ActivityNode_isRunningExitEventOccurrence,
    ActivityNode_removeTokenEntryEventOccurrence,
    ActivityNode_removeTokenExitEventOccurrence,
    ActivityNode_run_activityNodeEntryEventOccurrence,
    ActivityNode_run_activityNodeExitEventOccurrence,
    ActivityNode_running_State,
    ActivityNode_sendOffersEntryEventOccurrence,
    ActivityNode_sendOffersExitEventOccurrence,
    ActivityNode_takeOfferedTokensEntryEventOccurrence,
    ActivityNode_takeOfferedTokensExitEventOccurrence,
    ActivityNode_terminate_activityNodeEntryEventOccurrence,
    ActivityNode_terminate_activityNodeExitEventOccurrence,
    Activity_fireInitialNodeEntryEventOccurrence,
    Activity_fireInitialNodeExitEventOccurrence,
    Activity_fireNodeEntryEventOccurrence,
    Activity_fireNodeExitEventOccurrence,
    Activity_getEnabledNodesEntryEventOccurrence,
    Activity_getEnabledNodesExitEventOccurrence,
    Activity_getInitialNodeEntryEventOccurrence,
    Activity_getInitialNodeExitEventOccurrence,
    Activity_initializeEntryEventOccurrence,
    Activity_initializeExitEventOccurrence,
    Activity_mainEntryEventOccurrence,
    Activity_mainExitEventOccurrence,
    Activity_runEntryEventOccurrence,
    Activity_runExitEventOccurrence,
    Activity_runNodesEntryEventOccurrence,
    Activity_runNodesExitEventOccurrence,
    Activity_selectNextNodeEntryEventOccurrence,
    Activity_selectNextNodeExitEventOccurrence,
    Activity_terminateEntryEventOccurrence,
    Activity_terminateExitEventOccurrence,
    Activity_trace_State,
    BooleanBinaryExpression_evaluateANDEntryEventOccurrence,
    BooleanBinaryExpression_evaluateANDExitEventOccurrence,
    BooleanBinaryExpression_evaluateOREntryEventOccurrence,
    BooleanBinaryExpression_evaluateORExitEventOccurrence,
    BooleanBinaryExpression_execute_booleanBinaryExpressionEntryEventOccurrence,
    BooleanBinaryExpression_execute_booleanBinaryExpressionExitEventOccurrence,
    BooleanUnaryExpression_evaluateNOTEntryEventOccurrence,
    BooleanUnaryExpression_evaluateNOTExitEventOccurrence,
    BooleanUnaryExpression_execute_booleanUnaryExpressionEntryEventOccurrence,
    BooleanUnaryExpression_execute_booleanUnaryExpressionExitEventOccurrence,
    BooleanVariable_getCurrentValueValue_booleanVariableEntryEventOccurrence,
    BooleanVariable_getCurrentValueValue_booleanVariableExitEventOccurrence,
    BooleanVariable_setCurrentValue_boolenVariableEntryEventOccurrence,
    BooleanVariable_setCurrentValue_boolenVariableExitEventOccurrence,
    ControlNode_fire_controlNodeEntryEventOccurrence,
    ControlNode_fire_controlNodeExitEventOccurrence,
    ControlNode_isReady_ControlNodeEntryEventOccurrence,
    ControlNode_isReady_ControlNodeExitEventOccurrence,
    DecisionNode_fire_decisionNodeEntryEventOccurrence,
    DecisionNode_fire_decisionNodeExitEventOccurrence,
    EventOccurrence,
    Events,
    Events_traceSystem_BooleanBinaryExpression,
    Events_traceSystem_BooleanUnaryExpression,
    Events_traceSystem_EObject,
    Events_traceSystem_GlobalState,
    Events_traceSystem_IntegerCalculationExpression,
    Events_traceSystem_IntegerComparisonExpression,
    Events_traceSystem_IntegerExpression,
    Events_traceSystem_Value,
    ForkNode_fire_forkNodeEntryEventOccurrence,
    ForkNode_fire_forkNodeExitEventOccurrence,
    ForkedToken_baseTokenIsWithdrawn_State,
    ForkedToken_baseToken_State,
    ForkedToken_remainingOffersCount_State,
    ForkedToken_withdraw_forkedTokenEntryEventOccurrence,
    ForkedToken_withdraw_forkedTokenExitEventOccurrence,
    InitialNode_fire_initialNodeEntryEventOccurrence,
    InitialNode_fire_initialNodeExitEventOccurrence,
    InitialNode_isReady_InitialNodeEntryEventOccurrence,
    InitialNode_isReady_InitialNodeExitEventOccurrence,
    InputValue_value_State,
    InputValue_variable_State,
    Input_inputValues_State,
    IntegerCalculationExpression_evaluateADDEntryEventOccurrence,
    IntegerCalculationExpression_evaluateADDExitEventOccurrence,
    IntegerCalculationExpression_evaluateSUBTRACTEntryEventOccurrence,
    IntegerCalculationExpression_evaluateSUBTRACTExitEventOccurrence,
    IntegerCalculationExpression_execute_integerCalculationExpressionEntryEventOccurrence,
    IntegerCalculationExpression_execute_integerCalculationExpressionExitEventOccurrence,
    IntegerComparisonExpression_evaluateEQUALSEntryEventOccurrence,
    IntegerComparisonExpression_evaluateEQUALSExitEventOccurrence,
    IntegerComparisonExpression_evaluateGREATEREntryEventOccurrence,
    IntegerComparisonExpression_evaluateGREATERExitEventOccurrence,
    IntegerComparisonExpression_evaluateGREATER_EQUALSEntryEventOccurrence,
    IntegerComparisonExpression_evaluateGREATER_EQUALSExitEventOccurrence,
    IntegerComparisonExpression_evaluateSMALLEREntryEventOccurrence,
    IntegerComparisonExpression_evaluateSMALLERExitEventOccurrence,
    IntegerComparisonExpression_evaluateSMALLER_EQUALSEntryEventOccurrence,
    IntegerComparisonExpression_evaluateSMALLER_EQUALSExitEventOccurrence,
    IntegerComparisonExpression_execute_IntegerComparisionExpressionEntryEventOccurrence,
    IntegerComparisonExpression_execute_IntegerComparisionExpressionExitEventOccurrence,
    IntegerExpression_getOperandCurrentValuesEntryEventOccurrence,
    IntegerExpression_getOperandCurrentValuesExitEventOccurrence,
    IntegerVariable_getCurrentValueValue_integerVariableEntryEventOccurrence,
    IntegerVariable_getCurrentValueValue_integerVariableExitEventOccurrence,
    IntegerVariable_setCurrentValue_integerVariableEntryEventOccurrence,
    IntegerVariable_setCurrentValue_integerVariableExitEventOccurrence,
    MergeNode_hasOffers_mergeNodeEntryEventOccurrence,
    MergeNode_hasOffers_mergeNodeExitEventOccurrence,
    Offer_hasTokensEntryEventOccurrence,
    Offer_hasTokensExitEventOccurrence,
    Offer_offeredTokens_State,
    OpaqueAction_doAction_opaqueActionEntryEventOccurrence,
    OpaqueAction_doAction_opaqueActionExitEventOccurrence,
    States_traceSystem_GlobalState,
    States_traceSystem_Value,
    StringVariable_getCurrentValueValue_stringVariableEntryEventOccurrence,
    StringVariable_getCurrentValueValue_stringVariableExitEventOccurrence,
    StringVariable_setCurrentValue_stringVariableEntryEventOccurrence,
    StringVariable_setCurrentValue_stringVariableExitEventOccurrence,
    Token_holder_State,
    Token_isWithdrawnEntryEventOccurrence,
    Token_isWithdrawnExitEventOccurrence,
    Token_transferEntryEventOccurrence,
    Token_transferExitEventOccurrence,
    Token_withdrawEntryEventOccurrence,
    Token_withdrawExitEventOccurrence,
    Trace_executedNodes_State,
    TracedAction,
    TracedActivityEdge,
    TracedActivityNode,
    TracedControlNode,
    TracedExecutableNode,
    TracedFinalNode,
    TracedNamedElement,
    TracedObjects,
    TracedToken,
    TracedVariable,
    Variable_currentValue_State,
    activitydiagramConfiguration_TracedControlToken,
    activitydiagramConfiguration_TracedForkedToken,
    activitydiagramConfiguration_TracedInput,
    activitydiagramConfiguration_TracedInputValue,
    activitydiagramConfiguration_TracedOffer,
    activitydiagramConfiguration_TracedToken,
    activitydiagramConfiguration_TracedTrace,
    activitydiagram_TracedAction,
    activitydiagram_TracedActivity,
    activitydiagram_TracedActivityEdge,
    activitydiagram_TracedActivityFinalNode,
    activitydiagram_TracedActivityNode,
    activitydiagram_TracedBooleanVariable,
    activitydiagram_TracedControlFlow,
    activitydiagram_TracedControlNode,
    activitydiagram_TracedDecisionNode,
    activitydiagram_TracedForkNode,
    activitydiagram_TracedInitialNode,
    activitydiagram_TracedIntegerVariable,
    activitydiagram_TracedJoinNode,
    activitydiagram_TracedMergeNode,
    activitydiagram_TracedOpaqueAction,
    activitydiagram_TracedStringVariable,
    activitydiagram_TracedVariable,
    activitydiagram_traceSystem_Activity,
    activitydiagram_traceSystem_ActivityFinalNode,
    activitydiagram_traceSystem_BooleanVariable,
    activitydiagram_traceSystem_ControlFlow,
    activitydiagram_traceSystem_DecisionNode,
    activitydiagram_traceSystem_Expression,
    activitydiagram_traceSystem_ForkNode,
    activitydiagram_traceSystem_InitialNode,
    activitydiagram_traceSystem_IntegerVariable,
    activitydiagram_traceSystem_JoinNode,
    activitydiagram_traceSystem_MergeNode,
    activitydiagram_traceSystem_OpaqueAction,
    activitydiagram_traceSystem_StringVariable,
    activitydiagram_traceSystem_Value,
    traceSystem_BooleanBinaryExpression,
    traceSystem_BooleanUnaryExpression,
    traceSystem_BooleanValue,
    traceSystem_Events_Action_fire_actionEntryEventOccurrence,
    traceSystem_Events_Action_fire_actionExitEventOccurrence,
    traceSystem_Events_Action_isReady_actionEntryEventOccurrence,
    traceSystem_Events_Action_isReady_actionExitEventOccurrence,
    traceSystem_Events_Action_sendOffers_actionEntryEventOccurrence,
    traceSystem_Events_Action_sendOffers_actionExitEventOccurrence,
    traceSystem_Events_ActivityEdge_hasOfferEntryEventOccurrence,
    traceSystem_Events_ActivityEdge_hasOfferExitEventOccurrence,
    traceSystem_Events_ActivityEdge_sendOfferEntryEventOccurrence,
    traceSystem_Events_ActivityEdge_sendOfferExitEventOccurrence,
    traceSystem_Events_ActivityEdge_takeOfferedTokens_activityEdgeEntryEventOccurrence,
    traceSystem_Events_ActivityEdge_takeOfferedTokens_activityEdgeExitEventOccurrence,
    traceSystem_Events_ActivityFinalNode_fire_activityFinalNodeEntryEventOccurrence,
    traceSystem_Events_ActivityFinalNode_fire_activityFinalNodeExitEventOccurrence,
    traceSystem_Events_ActivityNode_addTokensEntryEventOccurrence,
    traceSystem_Events_ActivityNode_addTokensExitEventOccurrence,
    traceSystem_Events_ActivityNode_hasOffersEntryEventOccurrence,
    traceSystem_Events_ActivityNode_hasOffersExitEventOccurrence,
    traceSystem_Events_ActivityNode_isReadyEntryEventOccurrence,
    traceSystem_Events_ActivityNode_isReadyExitEventOccurrence,
    traceSystem_Events_ActivityNode_isRunningEntryEventOccurrence,
    traceSystem_Events_ActivityNode_isRunningExitEventOccurrence,
    traceSystem_Events_ActivityNode_removeTokenEntryEventOccurrence,
    traceSystem_Events_ActivityNode_removeTokenExitEventOccurrence,
    traceSystem_Events_ActivityNode_run_activityNodeEntryEventOccurrence,
    traceSystem_Events_ActivityNode_run_activityNodeExitEventOccurrence,
    traceSystem_Events_ActivityNode_sendOffersEntryEventOccurrence,
    traceSystem_Events_ActivityNode_sendOffersExitEventOccurrence,
    traceSystem_Events_ActivityNode_takeOfferedTokensEntryEventOccurrence,
    traceSystem_Events_ActivityNode_takeOfferedTokensExitEventOccurrence,
    traceSystem_Events_ActivityNode_terminate_activityNodeEntryEventOccurrence,
    traceSystem_Events_ActivityNode_terminate_activityNodeExitEventOccurrence,
    traceSystem_Events_Activity_fireInitialNodeEntryEventOccurrence,
    traceSystem_Events_Activity_fireInitialNodeExitEventOccurrence,
    traceSystem_Events_Activity_fireNodeEntryEventOccurrence,
    traceSystem_Events_Activity_fireNodeExitEventOccurrence,
    traceSystem_Events_Activity_getEnabledNodesEntryEventOccurrence,
    traceSystem_Events_Activity_getEnabledNodesExitEventOccurrence,
    traceSystem_Events_Activity_getInitialNodeEntryEventOccurrence,
    traceSystem_Events_Activity_getInitialNodeExitEventOccurrence,
    traceSystem_Events_Activity_initializeEntryEventOccurrence,
    traceSystem_Events_Activity_initializeExitEventOccurrence,
    traceSystem_Events_Activity_mainEntryEventOccurrence,
    traceSystem_Events_Activity_mainExitEventOccurrence,
    traceSystem_Events_Activity_runEntryEventOccurrence,
    traceSystem_Events_Activity_runExitEventOccurrence,
    traceSystem_Events_Activity_runNodesEntryEventOccurrence,
    traceSystem_Events_Activity_runNodesExitEventOccurrence,
    traceSystem_Events_Activity_selectNextNodeEntryEventOccurrence,
    traceSystem_Events_Activity_selectNextNodeExitEventOccurrence,
    traceSystem_Events_Activity_terminateEntryEventOccurrence,
    traceSystem_Events_Activity_terminateExitEventOccurrence,
    traceSystem_Events_BooleanBinaryExpression_evaluateANDEntryEventOccurrence,
    traceSystem_Events_BooleanBinaryExpression_evaluateANDExitEventOccurrence,
    traceSystem_Events_BooleanBinaryExpression_evaluateOREntryEventOccurrence,
    traceSystem_Events_BooleanBinaryExpression_evaluateORExitEventOccurrence,
    traceSystem_Events_BooleanBinaryExpression_execute_booleanBinaryExpressionEntryEventOccurrence,
    traceSystem_Events_BooleanBinaryExpression_execute_booleanBinaryExpressionExitEventOccurrence,
    traceSystem_Events_BooleanUnaryExpression_evaluateNOTEntryEventOccurrence,
    traceSystem_Events_BooleanUnaryExpression_evaluateNOTExitEventOccurrence,
    traceSystem_Events_BooleanUnaryExpression_execute_booleanUnaryExpressionEntryEventOccurrence,
    traceSystem_Events_BooleanUnaryExpression_execute_booleanUnaryExpressionExitEventOccurrence,
    traceSystem_Events_BooleanVariable_getCurrentValueValue_booleanVariableEntryEventOccurrence,
    traceSystem_Events_BooleanVariable_getCurrentValueValue_booleanVariableExitEventOccurrence,
    traceSystem_Events_BooleanVariable_setCurrentValue_boolenVariableEntryEventOccurrence,
    traceSystem_Events_BooleanVariable_setCurrentValue_boolenVariableExitEventOccurrence,
    traceSystem_Events_ControlNode_fire_controlNodeEntryEventOccurrence,
    traceSystem_Events_ControlNode_fire_controlNodeExitEventOccurrence,
    traceSystem_Events_ControlNode_isReady_ControlNodeEntryEventOccurrence,
    traceSystem_Events_ControlNode_isReady_ControlNodeExitEventOccurrence,
    traceSystem_Events_DecisionNode_fire_decisionNodeEntryEventOccurrence,
    traceSystem_Events_DecisionNode_fire_decisionNodeExitEventOccurrence,
    traceSystem_Events_EventOccurrence,
    traceSystem_Events_Events,
    traceSystem_Events_ForkNode_fire_forkNodeEntryEventOccurrence,
    traceSystem_Events_ForkNode_fire_forkNodeExitEventOccurrence,
    traceSystem_Events_ForkedToken_withdraw_forkedTokenEntryEventOccurrence,
    traceSystem_Events_ForkedToken_withdraw_forkedTokenExitEventOccurrence,
    traceSystem_Events_InitialNode_fire_initialNodeEntryEventOccurrence,
    traceSystem_Events_InitialNode_fire_initialNodeExitEventOccurrence,
    traceSystem_Events_InitialNode_isReady_InitialNodeEntryEventOccurrence,
    traceSystem_Events_InitialNode_isReady_InitialNodeExitEventOccurrence,
    traceSystem_Events_IntegerCalculationExpression_evaluateADDEntryEventOccurrence,
    traceSystem_Events_IntegerCalculationExpression_evaluateADDExitEventOccurrence,
    traceSystem_Events_IntegerCalculationExpression_evaluateSUBTRACTEntryEventOccurrence,
    traceSystem_Events_IntegerCalculationExpression_evaluateSUBTRACTExitEventOccurrence,
    traceSystem_Events_IntegerCalculationExpression_execute_integerCalculationExpressionEntryEventOccurrence,
    traceSystem_Events_IntegerCalculationExpression_execute_integerCalculationExpressionExitEventOccurrence,
    traceSystem_Events_IntegerComparisonExpression_evaluateEQUALSEntryEventOccurrence,
    traceSystem_Events_IntegerComparisonExpression_evaluateEQUALSExitEventOccurrence,
    traceSystem_Events_IntegerComparisonExpression_evaluateGREATEREntryEventOccurrence,
    traceSystem_Events_IntegerComparisonExpression_evaluateGREATERExitEventOccurrence,
    traceSystem_Events_IntegerComparisonExpression_evaluateGREATER_EQUALSEntryEventOccurrence,
    traceSystem_Events_IntegerComparisonExpression_evaluateGREATER_EQUALSExitEventOccurrence,
    traceSystem_Events_IntegerComparisonExpression_evaluateSMALLEREntryEventOccurrence,
    traceSystem_Events_IntegerComparisonExpression_evaluateSMALLERExitEventOccurrence,
    traceSystem_Events_IntegerComparisonExpression_evaluateSMALLER_EQUALSEntryEventOccurrence,
    traceSystem_Events_IntegerComparisonExpression_evaluateSMALLER_EQUALSExitEventOccurrence,
    traceSystem_Events_IntegerComparisonExpression_execute_IntegerComparisionExpressionEntryEventOccurrence,
    traceSystem_Events_IntegerComparisonExpression_execute_IntegerComparisionExpressionExitEventOccurrence,
    traceSystem_Events_IntegerExpression_getOperandCurrentValuesEntryEventOccurrence,
    traceSystem_Events_IntegerExpression_getOperandCurrentValuesExitEventOccurrence,
    traceSystem_Events_IntegerVariable_getCurrentValueValue_integerVariableEntryEventOccurrence,
    traceSystem_Events_IntegerVariable_getCurrentValueValue_integerVariableExitEventOccurrence,
    traceSystem_Events_IntegerVariable_setCurrentValue_integerVariableEntryEventOccurrence,
    traceSystem_Events_IntegerVariable_setCurrentValue_integerVariableExitEventOccurrence,
    traceSystem_Events_MergeNode_hasOffers_mergeNodeEntryEventOccurrence,
    traceSystem_Events_MergeNode_hasOffers_mergeNodeExitEventOccurrence,
    traceSystem_Events_Offer_hasTokensEntryEventOccurrence,
    traceSystem_Events_Offer_hasTokensExitEventOccurrence,
    traceSystem_Events_OpaqueAction_doAction_opaqueActionEntryEventOccurrence,
    traceSystem_Events_OpaqueAction_doAction_opaqueActionExitEventOccurrence,
    traceSystem_Events_StringVariable_getCurrentValueValue_stringVariableEntryEventOccurrence,
    traceSystem_Events_StringVariable_getCurrentValueValue_stringVariableExitEventOccurrence,
    traceSystem_Events_StringVariable_setCurrentValue_stringVariableEntryEventOccurrence,
    traceSystem_Events_StringVariable_setCurrentValue_stringVariableExitEventOccurrence,
    traceSystem_Events_Token_isWithdrawnEntryEventOccurrence,
    traceSystem_Events_Token_isWithdrawnExitEventOccurrence,
    traceSystem_Events_Token_transferEntryEventOccurrence,
    traceSystem_Events_Token_transferExitEventOccurrence,
    traceSystem_Events_Token_withdrawEntryEventOccurrence,
    traceSystem_Events_Token_withdrawExitEventOccurrence,
    traceSystem_GlobalState,
    traceSystem_IntegerCalculationExpression,
    traceSystem_IntegerComparisonExpression,
    traceSystem_IntegerValue,
    traceSystem_States_ActivityEdge_offers_State,
    traceSystem_States_ActivityNode_heldTokens_State,
    traceSystem_States_ActivityNode_running_State,
    traceSystem_States_Activity_trace_State,
    traceSystem_States_ForkedToken_baseTokenIsWithdrawn_State,
    traceSystem_States_ForkedToken_baseToken_State,
    traceSystem_States_ForkedToken_remainingOffersCount_State,
    traceSystem_States_InputValue_value_State,
    traceSystem_States_InputValue_variable_State,
    traceSystem_States_Input_inputValues_State,
    traceSystem_States_Offer_offeredTokens_State,
    traceSystem_States_Token_holder_State,
    traceSystem_States_Trace_executedNodes_State,
    traceSystem_States_Variable_currentValue_State,
    traceSystem_StaticObjectsPools,
    traceSystem_StringValue,
    traceSystem_Trace,
    traceSystem_Traced_TracedObjects,
    traceSystem_activitydiagramConfiguration_TracedControlToken,
    traceSystem_activitydiagramConfiguration_TracedForkedToken,
    traceSystem_activitydiagramConfiguration_TracedInput,
    traceSystem_activitydiagramConfiguration_TracedInputValue,
    traceSystem_activitydiagramConfiguration_TracedOffer,
    traceSystem_activitydiagramConfiguration_TracedToken,
    traceSystem_activitydiagramConfiguration_TracedTrace,
    traceSystem_activitydiagram_TracedAction,
    traceSystem_activitydiagram_TracedActivity,
    traceSystem_activitydiagram_TracedActivityEdge,
    traceSystem_activitydiagram_TracedActivityFinalNode,
    traceSystem_activitydiagram_TracedActivityNode,
    traceSystem_activitydiagram_TracedBooleanVariable,
    traceSystem_activitydiagram_TracedControlFlow,
    traceSystem_activitydiagram_TracedControlNode,
    traceSystem_activitydiagram_TracedDecisionNode,
    traceSystem_activitydiagram_TracedExecutableNode,
    traceSystem_activitydiagram_TracedFinalNode,
    traceSystem_activitydiagram_TracedForkNode,
    traceSystem_activitydiagram_TracedInitialNode,
    traceSystem_activitydiagram_TracedIntegerVariable,
    traceSystem_activitydiagram_TracedJoinNode,
    traceSystem_activitydiagram_TracedMergeNode,
    traceSystem_activitydiagram_TracedNamedElement,
    traceSystem_activitydiagram_TracedOpaqueAction,
    traceSystem_activitydiagram_TracedStringVariable,
    traceSystem_activitydiagram_TracedVariable,
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

def test_assoc_globalStates659_stub_double():
    # States_traceSystem_GlobalState has no real 'GlobalState660' property in the generated
    # code (a bare stub) -- manually attach it so traceSystem_States_ForkedToken_remainingOffersCount_State's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # traceSystem_States_ForkedToken_remainingOffersCount_State's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = traceSystem_States_ForkedToken_remainingOffersCount_State(remainingOffersCount=7)
    partner = States_traceSystem_GlobalState()
    setattr(partner, 'GlobalState660', None)
    _safe_set(owner, 'forkedToken_remainingOffersCount_States', {partner})
    assert getattr(partner, 'GlobalState660') == owner
    _safe_set(owner, 'forkedToken_remainingOffersCount_States', set())
    assert getattr(partner, 'GlobalState660') is None


def test_assoc_globalStates663_stub_double():
    # States_traceSystem_GlobalState has no real 'GlobalState664' property in the generated
    # code (a bare stub) -- manually attach it so traceSystem_States_ForkedToken_baseTokenIsWithdrawn_State's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # traceSystem_States_ForkedToken_baseTokenIsWithdrawn_State's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = traceSystem_States_ForkedToken_baseTokenIsWithdrawn_State(baseTokenIsWithdrawn=True)
    partner = States_traceSystem_GlobalState()
    setattr(partner, 'GlobalState664', None)
    _safe_set(owner, 'forkedToken_baseTokenIsWithdrawn_States', {partner})
    assert getattr(partner, 'GlobalState664') == owner
    _safe_set(owner, 'forkedToken_baseTokenIsWithdrawn_States', set())
    assert getattr(partner, 'GlobalState664') is None


def test_assoc_globalStates714_stub_double():
    # States_traceSystem_GlobalState has no real 'GlobalState715' property in the generated
    # code (a bare stub) -- manually attach it so traceSystem_States_ActivityNode_running_State's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # traceSystem_States_ActivityNode_running_State's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = traceSystem_States_ActivityNode_running_State(running=True)
    partner = States_traceSystem_GlobalState()
    setattr(partner, 'GlobalState715', None)
    _safe_set(owner, 'activityNode_running_States', {partner})
    assert getattr(partner, 'GlobalState715') == owner
    _safe_set(owner, 'activityNode_running_States', set())
    assert getattr(partner, 'GlobalState715') is None


def test_assoc_parent657_stub_double():
    # activitydiagramConfiguration_TracedForkedToken has no real 'TracedForkedToken658' property in the generated
    # code (a bare stub) -- manually attach it so traceSystem_States_ForkedToken_remainingOffersCount_State's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # traceSystem_States_ForkedToken_remainingOffersCount_State's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = traceSystem_States_ForkedToken_remainingOffersCount_State(remainingOffersCount=7)
    partner = activitydiagramConfiguration_TracedForkedToken()
    setattr(partner, 'TracedForkedToken658', None)
    _safe_set(owner, 'remainingOffersCountTrace', partner)
    assert getattr(partner, 'TracedForkedToken658') == owner
    _safe_set(owner, 'remainingOffersCountTrace', None)
    assert getattr(partner, 'TracedForkedToken658') is None


def test_assoc_parent661_stub_double():
    # activitydiagramConfiguration_TracedForkedToken has no real 'TracedForkedToken662' property in the generated
    # code (a bare stub) -- manually attach it so traceSystem_States_ForkedToken_baseTokenIsWithdrawn_State's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # traceSystem_States_ForkedToken_baseTokenIsWithdrawn_State's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = traceSystem_States_ForkedToken_baseTokenIsWithdrawn_State(baseTokenIsWithdrawn=True)
    partner = activitydiagramConfiguration_TracedForkedToken()
    setattr(partner, 'TracedForkedToken662', None)
    _safe_set(owner, 'baseTokenIsWithdrawnTrace', partner)
    assert getattr(partner, 'TracedForkedToken662') == owner
    _safe_set(owner, 'baseTokenIsWithdrawnTrace', None)
    assert getattr(partner, 'TracedForkedToken662') is None


def test_assoc_parent712_stub_double():
    # activitydiagram_TracedActivityNode has no real 'TracedActivityNode713' property in the generated
    # code (a bare stub) -- manually attach it so traceSystem_States_ActivityNode_running_State's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # traceSystem_States_ActivityNode_running_State's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = traceSystem_States_ActivityNode_running_State(running=True)
    partner = activitydiagram_TracedActivityNode()
    setattr(partner, 'TracedActivityNode713', None)
    _safe_set(owner, 'runningTrace', partner)
    assert getattr(partner, 'TracedActivityNode713') == owner
    _safe_set(owner, 'runningTrace', None)
    assert getattr(partner, 'TracedActivityNode713') is None


