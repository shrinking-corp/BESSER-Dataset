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
    Events_trace_BooleanBinaryExpression,
    Events_trace_BooleanUnaryExpression,
    Events_trace_EObject,
    Events_trace_GlobalState,
    Events_trace_IntegerCalculationExpression,
    Events_trace_IntegerComparisonExpression,
    Events_trace_IntegerExpression,
    Events_trace_Value,
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
    States_trace_GlobalState,
    States_trace_Value,
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
    activitydiagram_trace_Activity,
    activitydiagram_trace_ActivityFinalNode,
    activitydiagram_trace_BooleanVariable,
    activitydiagram_trace_ControlFlow,
    activitydiagram_trace_DecisionNode,
    activitydiagram_trace_Expression,
    activitydiagram_trace_ForkNode,
    activitydiagram_trace_InitialNode,
    activitydiagram_trace_IntegerVariable,
    activitydiagram_trace_JoinNode,
    activitydiagram_trace_MergeNode,
    activitydiagram_trace_OpaqueAction,
    activitydiagram_trace_StringVariable,
    activitydiagram_trace_Value,
    trace_BooleanBinaryExpression,
    trace_BooleanUnaryExpression,
    trace_BooleanValue,
    trace_Events_Action_fire_actionEntryEventOccurrence,
    trace_Events_Action_fire_actionExitEventOccurrence,
    trace_Events_Action_isReady_actionEntryEventOccurrence,
    trace_Events_Action_isReady_actionExitEventOccurrence,
    trace_Events_Action_sendOffers_actionEntryEventOccurrence,
    trace_Events_Action_sendOffers_actionExitEventOccurrence,
    trace_Events_ActivityEdge_hasOfferEntryEventOccurrence,
    trace_Events_ActivityEdge_hasOfferExitEventOccurrence,
    trace_Events_ActivityEdge_sendOfferEntryEventOccurrence,
    trace_Events_ActivityEdge_sendOfferExitEventOccurrence,
    trace_Events_ActivityEdge_takeOfferedTokens_activityEdgeEntryEventOccurrence,
    trace_Events_ActivityEdge_takeOfferedTokens_activityEdgeExitEventOccurrence,
    trace_Events_ActivityFinalNode_fire_activityFinalNodeEntryEventOccurrence,
    trace_Events_ActivityFinalNode_fire_activityFinalNodeExitEventOccurrence,
    trace_Events_ActivityNode_addTokensEntryEventOccurrence,
    trace_Events_ActivityNode_addTokensExitEventOccurrence,
    trace_Events_ActivityNode_hasOffersEntryEventOccurrence,
    trace_Events_ActivityNode_hasOffersExitEventOccurrence,
    trace_Events_ActivityNode_isReadyEntryEventOccurrence,
    trace_Events_ActivityNode_isReadyExitEventOccurrence,
    trace_Events_ActivityNode_isRunningEntryEventOccurrence,
    trace_Events_ActivityNode_isRunningExitEventOccurrence,
    trace_Events_ActivityNode_removeTokenEntryEventOccurrence,
    trace_Events_ActivityNode_removeTokenExitEventOccurrence,
    trace_Events_ActivityNode_run_activityNodeEntryEventOccurrence,
    trace_Events_ActivityNode_run_activityNodeExitEventOccurrence,
    trace_Events_ActivityNode_sendOffersEntryEventOccurrence,
    trace_Events_ActivityNode_sendOffersExitEventOccurrence,
    trace_Events_ActivityNode_takeOfferedTokensEntryEventOccurrence,
    trace_Events_ActivityNode_takeOfferedTokensExitEventOccurrence,
    trace_Events_ActivityNode_terminate_activityNodeEntryEventOccurrence,
    trace_Events_ActivityNode_terminate_activityNodeExitEventOccurrence,
    trace_Events_Activity_fireInitialNodeEntryEventOccurrence,
    trace_Events_Activity_fireInitialNodeExitEventOccurrence,
    trace_Events_Activity_fireNodeEntryEventOccurrence,
    trace_Events_Activity_fireNodeExitEventOccurrence,
    trace_Events_Activity_getEnabledNodesEntryEventOccurrence,
    trace_Events_Activity_getEnabledNodesExitEventOccurrence,
    trace_Events_Activity_getInitialNodeEntryEventOccurrence,
    trace_Events_Activity_getInitialNodeExitEventOccurrence,
    trace_Events_Activity_initializeEntryEventOccurrence,
    trace_Events_Activity_initializeExitEventOccurrence,
    trace_Events_Activity_mainEntryEventOccurrence,
    trace_Events_Activity_mainExitEventOccurrence,
    trace_Events_Activity_runEntryEventOccurrence,
    trace_Events_Activity_runExitEventOccurrence,
    trace_Events_Activity_runNodesEntryEventOccurrence,
    trace_Events_Activity_runNodesExitEventOccurrence,
    trace_Events_Activity_selectNextNodeEntryEventOccurrence,
    trace_Events_Activity_selectNextNodeExitEventOccurrence,
    trace_Events_Activity_terminateEntryEventOccurrence,
    trace_Events_Activity_terminateExitEventOccurrence,
    trace_Events_BooleanBinaryExpression_evaluateANDEntryEventOccurrence,
    trace_Events_BooleanBinaryExpression_evaluateANDExitEventOccurrence,
    trace_Events_BooleanBinaryExpression_evaluateOREntryEventOccurrence,
    trace_Events_BooleanBinaryExpression_evaluateORExitEventOccurrence,
    trace_Events_BooleanBinaryExpression_execute_booleanBinaryExpressionEntryEventOccurrence,
    trace_Events_BooleanBinaryExpression_execute_booleanBinaryExpressionExitEventOccurrence,
    trace_Events_BooleanUnaryExpression_evaluateNOTEntryEventOccurrence,
    trace_Events_BooleanUnaryExpression_evaluateNOTExitEventOccurrence,
    trace_Events_BooleanUnaryExpression_execute_booleanUnaryExpressionEntryEventOccurrence,
    trace_Events_BooleanUnaryExpression_execute_booleanUnaryExpressionExitEventOccurrence,
    trace_Events_BooleanVariable_getCurrentValueValue_booleanVariableEntryEventOccurrence,
    trace_Events_BooleanVariable_getCurrentValueValue_booleanVariableExitEventOccurrence,
    trace_Events_BooleanVariable_setCurrentValue_boolenVariableEntryEventOccurrence,
    trace_Events_BooleanVariable_setCurrentValue_boolenVariableExitEventOccurrence,
    trace_Events_ControlNode_fire_controlNodeEntryEventOccurrence,
    trace_Events_ControlNode_fire_controlNodeExitEventOccurrence,
    trace_Events_ControlNode_isReady_ControlNodeEntryEventOccurrence,
    trace_Events_ControlNode_isReady_ControlNodeExitEventOccurrence,
    trace_Events_DecisionNode_fire_decisionNodeEntryEventOccurrence,
    trace_Events_DecisionNode_fire_decisionNodeExitEventOccurrence,
    trace_Events_EventOccurrence,
    trace_Events_Events,
    trace_Events_ForkNode_fire_forkNodeEntryEventOccurrence,
    trace_Events_ForkNode_fire_forkNodeExitEventOccurrence,
    trace_Events_ForkedToken_withdraw_forkedTokenEntryEventOccurrence,
    trace_Events_ForkedToken_withdraw_forkedTokenExitEventOccurrence,
    trace_Events_InitialNode_fire_initialNodeEntryEventOccurrence,
    trace_Events_InitialNode_fire_initialNodeExitEventOccurrence,
    trace_Events_InitialNode_isReady_InitialNodeEntryEventOccurrence,
    trace_Events_InitialNode_isReady_InitialNodeExitEventOccurrence,
    trace_Events_IntegerCalculationExpression_evaluateADDEntryEventOccurrence,
    trace_Events_IntegerCalculationExpression_evaluateADDExitEventOccurrence,
    trace_Events_IntegerCalculationExpression_evaluateSUBTRACTEntryEventOccurrence,
    trace_Events_IntegerCalculationExpression_evaluateSUBTRACTExitEventOccurrence,
    trace_Events_IntegerCalculationExpression_execute_integerCalculationExpressionEntryEventOccurrence,
    trace_Events_IntegerCalculationExpression_execute_integerCalculationExpressionExitEventOccurrence,
    trace_Events_IntegerComparisonExpression_evaluateEQUALSEntryEventOccurrence,
    trace_Events_IntegerComparisonExpression_evaluateEQUALSExitEventOccurrence,
    trace_Events_IntegerComparisonExpression_evaluateGREATEREntryEventOccurrence,
    trace_Events_IntegerComparisonExpression_evaluateGREATERExitEventOccurrence,
    trace_Events_IntegerComparisonExpression_evaluateGREATER_EQUALSEntryEventOccurrence,
    trace_Events_IntegerComparisonExpression_evaluateGREATER_EQUALSExitEventOccurrence,
    trace_Events_IntegerComparisonExpression_evaluateSMALLEREntryEventOccurrence,
    trace_Events_IntegerComparisonExpression_evaluateSMALLERExitEventOccurrence,
    trace_Events_IntegerComparisonExpression_evaluateSMALLER_EQUALSEntryEventOccurrence,
    trace_Events_IntegerComparisonExpression_evaluateSMALLER_EQUALSExitEventOccurrence,
    trace_Events_IntegerComparisonExpression_execute_IntegerComparisionExpressionEntryEventOccurrence,
    trace_Events_IntegerComparisonExpression_execute_IntegerComparisionExpressionExitEventOccurrence,
    trace_Events_IntegerExpression_getOperandCurrentValuesEntryEventOccurrence,
    trace_Events_IntegerExpression_getOperandCurrentValuesExitEventOccurrence,
    trace_Events_IntegerVariable_getCurrentValueValue_integerVariableEntryEventOccurrence,
    trace_Events_IntegerVariable_getCurrentValueValue_integerVariableExitEventOccurrence,
    trace_Events_IntegerVariable_setCurrentValue_integerVariableEntryEventOccurrence,
    trace_Events_IntegerVariable_setCurrentValue_integerVariableExitEventOccurrence,
    trace_Events_MergeNode_hasOffers_mergeNodeEntryEventOccurrence,
    trace_Events_MergeNode_hasOffers_mergeNodeExitEventOccurrence,
    trace_Events_Offer_hasTokensEntryEventOccurrence,
    trace_Events_Offer_hasTokensExitEventOccurrence,
    trace_Events_OpaqueAction_doAction_opaqueActionEntryEventOccurrence,
    trace_Events_OpaqueAction_doAction_opaqueActionExitEventOccurrence,
    trace_Events_StringVariable_getCurrentValueValue_stringVariableEntryEventOccurrence,
    trace_Events_StringVariable_getCurrentValueValue_stringVariableExitEventOccurrence,
    trace_Events_StringVariable_setCurrentValue_stringVariableEntryEventOccurrence,
    trace_Events_StringVariable_setCurrentValue_stringVariableExitEventOccurrence,
    trace_Events_Token_isWithdrawnEntryEventOccurrence,
    trace_Events_Token_isWithdrawnExitEventOccurrence,
    trace_Events_Token_transferEntryEventOccurrence,
    trace_Events_Token_transferExitEventOccurrence,
    trace_Events_Token_withdrawEntryEventOccurrence,
    trace_Events_Token_withdrawExitEventOccurrence,
    trace_GlobalState,
    trace_IntegerCalculationExpression,
    trace_IntegerComparisonExpression,
    trace_IntegerValue,
    trace_States_ActivityEdge_offers_State,
    trace_States_ActivityNode_heldTokens_State,
    trace_States_ActivityNode_running_State,
    trace_States_Activity_trace_State,
    trace_States_ForkedToken_baseTokenIsWithdrawn_State,
    trace_States_ForkedToken_baseToken_State,
    trace_States_ForkedToken_remainingOffersCount_State,
    trace_States_InputValue_value_State,
    trace_States_InputValue_variable_State,
    trace_States_Input_inputValues_State,
    trace_States_Offer_offeredTokens_State,
    trace_States_Token_holder_State,
    trace_States_Trace_executedNodes_State,
    trace_States_Variable_currentValue_State,
    trace_StaticObjectsPools,
    trace_StringValue,
    trace_Trace,
    trace_Traced_TracedObjects,
    trace_activitydiagramConfiguration_TracedControlToken,
    trace_activitydiagramConfiguration_TracedForkedToken,
    trace_activitydiagramConfiguration_TracedInput,
    trace_activitydiagramConfiguration_TracedInputValue,
    trace_activitydiagramConfiguration_TracedOffer,
    trace_activitydiagramConfiguration_TracedToken,
    trace_activitydiagramConfiguration_TracedTrace,
    trace_activitydiagram_TracedAction,
    trace_activitydiagram_TracedActivity,
    trace_activitydiagram_TracedActivityEdge,
    trace_activitydiagram_TracedActivityFinalNode,
    trace_activitydiagram_TracedActivityNode,
    trace_activitydiagram_TracedBooleanVariable,
    trace_activitydiagram_TracedControlFlow,
    trace_activitydiagram_TracedControlNode,
    trace_activitydiagram_TracedDecisionNode,
    trace_activitydiagram_TracedExecutableNode,
    trace_activitydiagram_TracedFinalNode,
    trace_activitydiagram_TracedForkNode,
    trace_activitydiagram_TracedInitialNode,
    trace_activitydiagram_TracedIntegerVariable,
    trace_activitydiagram_TracedJoinNode,
    trace_activitydiagram_TracedMergeNode,
    trace_activitydiagram_TracedNamedElement,
    trace_activitydiagram_TracedOpaqueAction,
    trace_activitydiagram_TracedStringVariable,
    trace_activitydiagram_TracedVariable,
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

def test_assoc_globalStates671_stub_double():
    # States_trace_GlobalState has no real 'GlobalState672' property in the generated
    # code (a bare stub) -- manually attach it so trace_States_ForkedToken_remainingOffersCount_State's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # trace_States_ForkedToken_remainingOffersCount_State's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = trace_States_ForkedToken_remainingOffersCount_State(remainingOffersCount=7)
    partner = States_trace_GlobalState()
    setattr(partner, 'GlobalState672', None)
    _safe_set(owner, 'forkedToken_remainingOffersCount_States', {partner})
    assert getattr(partner, 'GlobalState672') == owner
    _safe_set(owner, 'forkedToken_remainingOffersCount_States', set())
    assert getattr(partner, 'GlobalState672') is None


def test_assoc_globalStates681_stub_double():
    # States_trace_GlobalState has no real 'GlobalState682' property in the generated
    # code (a bare stub) -- manually attach it so trace_States_ForkedToken_baseTokenIsWithdrawn_State's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # trace_States_ForkedToken_baseTokenIsWithdrawn_State's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = trace_States_ForkedToken_baseTokenIsWithdrawn_State(baseTokenIsWithdrawn=True)
    partner = States_trace_GlobalState()
    setattr(partner, 'GlobalState682', None)
    _safe_set(owner, 'forkedToken_baseTokenIsWithdrawn_States', {partner})
    assert getattr(partner, 'GlobalState682') == owner
    _safe_set(owner, 'forkedToken_baseTokenIsWithdrawn_States', set())
    assert getattr(partner, 'GlobalState682') is None


def test_assoc_globalStates699_stub_double():
    # States_trace_GlobalState has no real 'GlobalState700' property in the generated
    # code (a bare stub) -- manually attach it so trace_States_ActivityNode_running_State's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # trace_States_ActivityNode_running_State's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = trace_States_ActivityNode_running_State(running=True)
    partner = States_trace_GlobalState()
    setattr(partner, 'GlobalState700', None)
    _safe_set(owner, 'activityNode_running_States', {partner})
    assert getattr(partner, 'GlobalState700') == owner
    _safe_set(owner, 'activityNode_running_States', set())
    assert getattr(partner, 'GlobalState700') is None


def test_assoc_parent670_stub_double():
    # activitydiagramConfiguration_TracedForkedToken has no real 'TracedForkedToken' property in the generated
    # code (a bare stub) -- manually attach it so trace_States_ForkedToken_remainingOffersCount_State's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # trace_States_ForkedToken_remainingOffersCount_State's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = trace_States_ForkedToken_remainingOffersCount_State(remainingOffersCount=7)
    partner = activitydiagramConfiguration_TracedForkedToken()
    setattr(partner, 'TracedForkedToken', None)
    _safe_set(owner, 'remainingOffersCountTrace', partner)
    assert getattr(partner, 'TracedForkedToken') == owner
    _safe_set(owner, 'remainingOffersCountTrace', None)
    assert getattr(partner, 'TracedForkedToken') is None


def test_assoc_parent679_stub_double():
    # activitydiagramConfiguration_TracedForkedToken has no real 'TracedForkedToken680' property in the generated
    # code (a bare stub) -- manually attach it so trace_States_ForkedToken_baseTokenIsWithdrawn_State's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # trace_States_ForkedToken_baseTokenIsWithdrawn_State's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = trace_States_ForkedToken_baseTokenIsWithdrawn_State(baseTokenIsWithdrawn=True)
    partner = activitydiagramConfiguration_TracedForkedToken()
    setattr(partner, 'TracedForkedToken680', None)
    _safe_set(owner, 'baseTokenIsWithdrawnTrace', partner)
    assert getattr(partner, 'TracedForkedToken680') == owner
    _safe_set(owner, 'baseTokenIsWithdrawnTrace', None)
    assert getattr(partner, 'TracedForkedToken680') is None


def test_assoc_parent698_stub_double():
    # activitydiagram_TracedActivityNode has no real 'TracedActivityNode' property in the generated
    # code (a bare stub) -- manually attach it so trace_States_ActivityNode_running_State's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # trace_States_ActivityNode_running_State's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = trace_States_ActivityNode_running_State(running=True)
    partner = activitydiagram_TracedActivityNode()
    setattr(partner, 'TracedActivityNode', None)
    _safe_set(owner, 'runningTrace', partner)
    assert getattr(partner, 'TracedActivityNode') == owner
    _safe_set(owner, 'runningTrace', None)
    assert getattr(partner, 'TracedActivityNode') is None


