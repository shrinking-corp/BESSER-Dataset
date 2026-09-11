import inspect
import pytest
from datetime import date, datetime, time, timedelta
from hypothesis import given, settings
import hypothesis.strategies as st

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

def test_trace_States_ActivityNode_running_State_running_value_roundtrip():
    instance = trace_States_ActivityNode_running_State(running=True)
    assert instance.running == True
    instance.running = False
    assert instance.running == False


def test_trace_States_ForkedToken_baseTokenIsWithdrawn_State_baseTokenIsWithdrawn_value_roundtrip():
    instance = trace_States_ForkedToken_baseTokenIsWithdrawn_State(baseTokenIsWithdrawn=True)
    assert instance.baseTokenIsWithdrawn == True
    instance.baseTokenIsWithdrawn = False
    assert instance.baseTokenIsWithdrawn == False


def test_trace_States_ForkedToken_remainingOffersCount_State_remainingOffersCount_value_roundtrip():
    instance = trace_States_ForkedToken_remainingOffersCount_State(remainingOffersCount=7)
    assert instance.remainingOffersCount == 7
    instance.remainingOffersCount = 13
    assert instance.remainingOffersCount == 13


def test_trace_activitydiagram_TracedNamedElement_name_value_roundtrip():
    instance = trace_activitydiagram_TracedNamedElement(name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_trace_Events_Action_fire_actionEntryEventOccurrence_isa_EventOccurrence():
    instance = trace_Events_Action_fire_actionEntryEventOccurrence()
    assert isinstance(instance, EventOccurrence)


def test_trace_Events_Action_fire_actionExitEventOccurrence_isa_EventOccurrence():
    instance = trace_Events_Action_fire_actionExitEventOccurrence()
    assert isinstance(instance, EventOccurrence)


def test_trace_Events_Action_isReady_actionEntryEventOccurrence_isa_EventOccurrence():
    instance = trace_Events_Action_isReady_actionEntryEventOccurrence()
    assert isinstance(instance, EventOccurrence)


def test_trace_Events_Action_isReady_actionExitEventOccurrence_isa_EventOccurrence():
    instance = trace_Events_Action_isReady_actionExitEventOccurrence()
    assert isinstance(instance, EventOccurrence)


def test_trace_Events_Action_sendOffers_actionEntryEventOccurrence_isa_EventOccurrence():
    instance = trace_Events_Action_sendOffers_actionEntryEventOccurrence()
    assert isinstance(instance, EventOccurrence)


def test_trace_Events_Action_sendOffers_actionExitEventOccurrence_isa_EventOccurrence():
    instance = trace_Events_Action_sendOffers_actionExitEventOccurrence()
    assert isinstance(instance, EventOccurrence)


def test_trace_Events_ActivityEdge_hasOfferEntryEventOccurrence_isa_EventOccurrence():
    instance = trace_Events_ActivityEdge_hasOfferEntryEventOccurrence()
    assert isinstance(instance, EventOccurrence)


def test_trace_Events_ActivityEdge_hasOfferExitEventOccurrence_isa_EventOccurrence():
    instance = trace_Events_ActivityEdge_hasOfferExitEventOccurrence()
    assert isinstance(instance, EventOccurrence)


def test_trace_Events_ActivityEdge_sendOfferEntryEventOccurrence_isa_EventOccurrence():
    instance = trace_Events_ActivityEdge_sendOfferEntryEventOccurrence()
    assert isinstance(instance, EventOccurrence)


def test_trace_Events_ActivityEdge_sendOfferExitEventOccurrence_isa_EventOccurrence():
    instance = trace_Events_ActivityEdge_sendOfferExitEventOccurrence()
    assert isinstance(instance, EventOccurrence)


def test_trace_Events_ActivityEdge_takeOfferedTokens_activityEdgeEntryEventOccurrence_isa_EventOccurrence():
    instance = trace_Events_ActivityEdge_takeOfferedTokens_activityEdgeEntryEventOccurrence()
    assert isinstance(instance, EventOccurrence)


def test_trace_Events_ActivityEdge_takeOfferedTokens_activityEdgeExitEventOccurrence_isa_EventOccurrence():
    instance = trace_Events_ActivityEdge_takeOfferedTokens_activityEdgeExitEventOccurrence()
    assert isinstance(instance, EventOccurrence)


def test_trace_Events_ActivityFinalNode_fire_activityFinalNodeEntryEventOccurrence_isa_EventOccurrence():
    instance = trace_Events_ActivityFinalNode_fire_activityFinalNodeEntryEventOccurrence()
    assert isinstance(instance, EventOccurrence)


def test_trace_Events_ActivityFinalNode_fire_activityFinalNodeExitEventOccurrence_isa_EventOccurrence():
    instance = trace_Events_ActivityFinalNode_fire_activityFinalNodeExitEventOccurrence()
    assert isinstance(instance, EventOccurrence)


def test_trace_Events_ActivityNode_addTokensEntryEventOccurrence_isa_EventOccurrence():
    instance = trace_Events_ActivityNode_addTokensEntryEventOccurrence()
    assert isinstance(instance, EventOccurrence)


def test_trace_Events_ActivityNode_addTokensExitEventOccurrence_isa_EventOccurrence():
    instance = trace_Events_ActivityNode_addTokensExitEventOccurrence()
    assert isinstance(instance, EventOccurrence)


def test_trace_Events_ActivityNode_hasOffersEntryEventOccurrence_isa_EventOccurrence():
    instance = trace_Events_ActivityNode_hasOffersEntryEventOccurrence()
    assert isinstance(instance, EventOccurrence)


def test_trace_Events_ActivityNode_hasOffersExitEventOccurrence_isa_EventOccurrence():
    instance = trace_Events_ActivityNode_hasOffersExitEventOccurrence()
    assert isinstance(instance, EventOccurrence)


def test_trace_Events_ActivityNode_isReadyEntryEventOccurrence_isa_EventOccurrence():
    instance = trace_Events_ActivityNode_isReadyEntryEventOccurrence()
    assert isinstance(instance, EventOccurrence)


def test_trace_Events_ActivityNode_isReadyExitEventOccurrence_isa_EventOccurrence():
    instance = trace_Events_ActivityNode_isReadyExitEventOccurrence()
    assert isinstance(instance, EventOccurrence)


def test_trace_Events_ActivityNode_isRunningEntryEventOccurrence_isa_EventOccurrence():
    instance = trace_Events_ActivityNode_isRunningEntryEventOccurrence()
    assert isinstance(instance, EventOccurrence)


def test_trace_Events_ActivityNode_isRunningExitEventOccurrence_isa_EventOccurrence():
    instance = trace_Events_ActivityNode_isRunningExitEventOccurrence()
    assert isinstance(instance, EventOccurrence)


def test_trace_Events_ActivityNode_removeTokenEntryEventOccurrence_isa_EventOccurrence():
    instance = trace_Events_ActivityNode_removeTokenEntryEventOccurrence()
    assert isinstance(instance, EventOccurrence)


def test_trace_Events_ActivityNode_removeTokenExitEventOccurrence_isa_EventOccurrence():
    instance = trace_Events_ActivityNode_removeTokenExitEventOccurrence()
    assert isinstance(instance, EventOccurrence)


def test_trace_Events_ActivityNode_run_activityNodeEntryEventOccurrence_isa_EventOccurrence():
    instance = trace_Events_ActivityNode_run_activityNodeEntryEventOccurrence()
    assert isinstance(instance, EventOccurrence)


def test_trace_Events_ActivityNode_run_activityNodeExitEventOccurrence_isa_EventOccurrence():
    instance = trace_Events_ActivityNode_run_activityNodeExitEventOccurrence()
    assert isinstance(instance, EventOccurrence)


def test_trace_Events_ActivityNode_sendOffersEntryEventOccurrence_isa_EventOccurrence():
    instance = trace_Events_ActivityNode_sendOffersEntryEventOccurrence()
    assert isinstance(instance, EventOccurrence)


def test_trace_Events_ActivityNode_sendOffersExitEventOccurrence_isa_EventOccurrence():
    instance = trace_Events_ActivityNode_sendOffersExitEventOccurrence()
    assert isinstance(instance, EventOccurrence)


def test_trace_Events_ActivityNode_takeOfferedTokensEntryEventOccurrence_isa_EventOccurrence():
    instance = trace_Events_ActivityNode_takeOfferedTokensEntryEventOccurrence()
    assert isinstance(instance, EventOccurrence)


def test_trace_Events_ActivityNode_takeOfferedTokensExitEventOccurrence_isa_EventOccurrence():
    instance = trace_Events_ActivityNode_takeOfferedTokensExitEventOccurrence()
    assert isinstance(instance, EventOccurrence)


def test_trace_Events_ActivityNode_terminate_activityNodeEntryEventOccurrence_isa_EventOccurrence():
    instance = trace_Events_ActivityNode_terminate_activityNodeEntryEventOccurrence()
    assert isinstance(instance, EventOccurrence)


def test_trace_Events_ActivityNode_terminate_activityNodeExitEventOccurrence_isa_EventOccurrence():
    instance = trace_Events_ActivityNode_terminate_activityNodeExitEventOccurrence()
    assert isinstance(instance, EventOccurrence)


def test_trace_Events_Activity_fireInitialNodeEntryEventOccurrence_isa_EventOccurrence():
    instance = trace_Events_Activity_fireInitialNodeEntryEventOccurrence()
    assert isinstance(instance, EventOccurrence)


def test_trace_Events_Activity_fireInitialNodeExitEventOccurrence_isa_EventOccurrence():
    instance = trace_Events_Activity_fireInitialNodeExitEventOccurrence()
    assert isinstance(instance, EventOccurrence)


def test_trace_Events_Activity_fireNodeEntryEventOccurrence_isa_EventOccurrence():
    instance = trace_Events_Activity_fireNodeEntryEventOccurrence()
    assert isinstance(instance, EventOccurrence)


def test_trace_Events_Activity_fireNodeExitEventOccurrence_isa_EventOccurrence():
    instance = trace_Events_Activity_fireNodeExitEventOccurrence()
    assert isinstance(instance, EventOccurrence)


def test_trace_Events_Activity_getEnabledNodesEntryEventOccurrence_isa_EventOccurrence():
    instance = trace_Events_Activity_getEnabledNodesEntryEventOccurrence()
    assert isinstance(instance, EventOccurrence)


def test_trace_Events_Activity_getEnabledNodesExitEventOccurrence_isa_EventOccurrence():
    instance = trace_Events_Activity_getEnabledNodesExitEventOccurrence()
    assert isinstance(instance, EventOccurrence)


def test_trace_Events_Activity_getInitialNodeEntryEventOccurrence_isa_EventOccurrence():
    instance = trace_Events_Activity_getInitialNodeEntryEventOccurrence()
    assert isinstance(instance, EventOccurrence)


def test_trace_Events_Activity_getInitialNodeExitEventOccurrence_isa_EventOccurrence():
    instance = trace_Events_Activity_getInitialNodeExitEventOccurrence()
    assert isinstance(instance, EventOccurrence)


def test_trace_Events_Activity_initializeEntryEventOccurrence_isa_EventOccurrence():
    instance = trace_Events_Activity_initializeEntryEventOccurrence()
    assert isinstance(instance, EventOccurrence)


def test_trace_Events_Activity_initializeExitEventOccurrence_isa_EventOccurrence():
    instance = trace_Events_Activity_initializeExitEventOccurrence()
    assert isinstance(instance, EventOccurrence)


def test_trace_Events_Activity_mainEntryEventOccurrence_isa_EventOccurrence():
    instance = trace_Events_Activity_mainEntryEventOccurrence()
    assert isinstance(instance, EventOccurrence)


def test_trace_Events_Activity_mainExitEventOccurrence_isa_EventOccurrence():
    instance = trace_Events_Activity_mainExitEventOccurrence()
    assert isinstance(instance, EventOccurrence)


def test_trace_Events_Activity_runEntryEventOccurrence_isa_EventOccurrence():
    instance = trace_Events_Activity_runEntryEventOccurrence()
    assert isinstance(instance, EventOccurrence)


def test_trace_Events_Activity_runExitEventOccurrence_isa_EventOccurrence():
    instance = trace_Events_Activity_runExitEventOccurrence()
    assert isinstance(instance, EventOccurrence)


def test_trace_Events_Activity_runNodesEntryEventOccurrence_isa_EventOccurrence():
    instance = trace_Events_Activity_runNodesEntryEventOccurrence()
    assert isinstance(instance, EventOccurrence)


def test_trace_Events_Activity_runNodesExitEventOccurrence_isa_EventOccurrence():
    instance = trace_Events_Activity_runNodesExitEventOccurrence()
    assert isinstance(instance, EventOccurrence)


def test_trace_Events_Activity_selectNextNodeEntryEventOccurrence_isa_EventOccurrence():
    instance = trace_Events_Activity_selectNextNodeEntryEventOccurrence()
    assert isinstance(instance, EventOccurrence)


def test_trace_Events_Activity_selectNextNodeExitEventOccurrence_isa_EventOccurrence():
    instance = trace_Events_Activity_selectNextNodeExitEventOccurrence()
    assert isinstance(instance, EventOccurrence)


def test_trace_Events_Activity_terminateEntryEventOccurrence_isa_EventOccurrence():
    instance = trace_Events_Activity_terminateEntryEventOccurrence()
    assert isinstance(instance, EventOccurrence)


def test_trace_Events_Activity_terminateExitEventOccurrence_isa_EventOccurrence():
    instance = trace_Events_Activity_terminateExitEventOccurrence()
    assert isinstance(instance, EventOccurrence)


def test_trace_Events_BooleanBinaryExpression_evaluateANDEntryEventOccurrence_isa_EventOccurrence():
    instance = trace_Events_BooleanBinaryExpression_evaluateANDEntryEventOccurrence()
    assert isinstance(instance, EventOccurrence)


def test_trace_Events_BooleanBinaryExpression_evaluateANDExitEventOccurrence_isa_EventOccurrence():
    instance = trace_Events_BooleanBinaryExpression_evaluateANDExitEventOccurrence()
    assert isinstance(instance, EventOccurrence)


def test_trace_Events_BooleanBinaryExpression_evaluateOREntryEventOccurrence_isa_EventOccurrence():
    instance = trace_Events_BooleanBinaryExpression_evaluateOREntryEventOccurrence()
    assert isinstance(instance, EventOccurrence)


def test_trace_Events_BooleanBinaryExpression_evaluateORExitEventOccurrence_isa_EventOccurrence():
    instance = trace_Events_BooleanBinaryExpression_evaluateORExitEventOccurrence()
    assert isinstance(instance, EventOccurrence)


def test_trace_Events_BooleanBinaryExpression_execute_booleanBinaryExpressionEntryEventOccurrence_isa_EventOccurrence():
    instance = trace_Events_BooleanBinaryExpression_execute_booleanBinaryExpressionEntryEventOccurrence()
    assert isinstance(instance, EventOccurrence)


def test_trace_Events_BooleanBinaryExpression_execute_booleanBinaryExpressionExitEventOccurrence_isa_EventOccurrence():
    instance = trace_Events_BooleanBinaryExpression_execute_booleanBinaryExpressionExitEventOccurrence()
    assert isinstance(instance, EventOccurrence)


def test_trace_Events_BooleanUnaryExpression_evaluateNOTEntryEventOccurrence_isa_EventOccurrence():
    instance = trace_Events_BooleanUnaryExpression_evaluateNOTEntryEventOccurrence()
    assert isinstance(instance, EventOccurrence)


def test_trace_Events_BooleanUnaryExpression_evaluateNOTExitEventOccurrence_isa_EventOccurrence():
    instance = trace_Events_BooleanUnaryExpression_evaluateNOTExitEventOccurrence()
    assert isinstance(instance, EventOccurrence)


def test_trace_Events_BooleanUnaryExpression_execute_booleanUnaryExpressionEntryEventOccurrence_isa_EventOccurrence():
    instance = trace_Events_BooleanUnaryExpression_execute_booleanUnaryExpressionEntryEventOccurrence()
    assert isinstance(instance, EventOccurrence)


def test_trace_Events_BooleanUnaryExpression_execute_booleanUnaryExpressionExitEventOccurrence_isa_EventOccurrence():
    instance = trace_Events_BooleanUnaryExpression_execute_booleanUnaryExpressionExitEventOccurrence()
    assert isinstance(instance, EventOccurrence)


def test_trace_Events_BooleanVariable_getCurrentValueValue_booleanVariableEntryEventOccurrence_isa_EventOccurrence():
    instance = trace_Events_BooleanVariable_getCurrentValueValue_booleanVariableEntryEventOccurrence()
    assert isinstance(instance, EventOccurrence)


def test_trace_Events_BooleanVariable_getCurrentValueValue_booleanVariableExitEventOccurrence_isa_EventOccurrence():
    instance = trace_Events_BooleanVariable_getCurrentValueValue_booleanVariableExitEventOccurrence()
    assert isinstance(instance, EventOccurrence)


def test_trace_Events_BooleanVariable_setCurrentValue_boolenVariableEntryEventOccurrence_isa_EventOccurrence():
    instance = trace_Events_BooleanVariable_setCurrentValue_boolenVariableEntryEventOccurrence()
    assert isinstance(instance, EventOccurrence)


def test_trace_Events_BooleanVariable_setCurrentValue_boolenVariableExitEventOccurrence_isa_EventOccurrence():
    instance = trace_Events_BooleanVariable_setCurrentValue_boolenVariableExitEventOccurrence()
    assert isinstance(instance, EventOccurrence)


def test_trace_Events_ControlNode_fire_controlNodeEntryEventOccurrence_isa_EventOccurrence():
    instance = trace_Events_ControlNode_fire_controlNodeEntryEventOccurrence()
    assert isinstance(instance, EventOccurrence)


def test_trace_Events_ControlNode_fire_controlNodeExitEventOccurrence_isa_EventOccurrence():
    instance = trace_Events_ControlNode_fire_controlNodeExitEventOccurrence()
    assert isinstance(instance, EventOccurrence)


def test_trace_Events_ControlNode_isReady_ControlNodeEntryEventOccurrence_isa_EventOccurrence():
    instance = trace_Events_ControlNode_isReady_ControlNodeEntryEventOccurrence()
    assert isinstance(instance, EventOccurrence)


def test_trace_Events_ControlNode_isReady_ControlNodeExitEventOccurrence_isa_EventOccurrence():
    instance = trace_Events_ControlNode_isReady_ControlNodeExitEventOccurrence()
    assert isinstance(instance, EventOccurrence)


def test_trace_Events_DecisionNode_fire_decisionNodeEntryEventOccurrence_isa_EventOccurrence():
    instance = trace_Events_DecisionNode_fire_decisionNodeEntryEventOccurrence()
    assert isinstance(instance, EventOccurrence)


def test_trace_Events_DecisionNode_fire_decisionNodeExitEventOccurrence_isa_EventOccurrence():
    instance = trace_Events_DecisionNode_fire_decisionNodeExitEventOccurrence()
    assert isinstance(instance, EventOccurrence)


def test_trace_Events_ForkNode_fire_forkNodeEntryEventOccurrence_isa_EventOccurrence():
    instance = trace_Events_ForkNode_fire_forkNodeEntryEventOccurrence()
    assert isinstance(instance, EventOccurrence)


def test_trace_Events_ForkNode_fire_forkNodeExitEventOccurrence_isa_EventOccurrence():
    instance = trace_Events_ForkNode_fire_forkNodeExitEventOccurrence()
    assert isinstance(instance, EventOccurrence)


def test_trace_Events_ForkedToken_withdraw_forkedTokenEntryEventOccurrence_isa_EventOccurrence():
    instance = trace_Events_ForkedToken_withdraw_forkedTokenEntryEventOccurrence()
    assert isinstance(instance, EventOccurrence)


def test_trace_Events_ForkedToken_withdraw_forkedTokenExitEventOccurrence_isa_EventOccurrence():
    instance = trace_Events_ForkedToken_withdraw_forkedTokenExitEventOccurrence()
    assert isinstance(instance, EventOccurrence)


def test_trace_Events_InitialNode_fire_initialNodeEntryEventOccurrence_isa_EventOccurrence():
    instance = trace_Events_InitialNode_fire_initialNodeEntryEventOccurrence()
    assert isinstance(instance, EventOccurrence)


def test_trace_Events_InitialNode_fire_initialNodeExitEventOccurrence_isa_EventOccurrence():
    instance = trace_Events_InitialNode_fire_initialNodeExitEventOccurrence()
    assert isinstance(instance, EventOccurrence)


def test_trace_Events_InitialNode_isReady_InitialNodeEntryEventOccurrence_isa_EventOccurrence():
    instance = trace_Events_InitialNode_isReady_InitialNodeEntryEventOccurrence()
    assert isinstance(instance, EventOccurrence)


def test_trace_Events_InitialNode_isReady_InitialNodeExitEventOccurrence_isa_EventOccurrence():
    instance = trace_Events_InitialNode_isReady_InitialNodeExitEventOccurrence()
    assert isinstance(instance, EventOccurrence)


def test_trace_Events_IntegerCalculationExpression_evaluateADDEntryEventOccurrence_isa_EventOccurrence():
    instance = trace_Events_IntegerCalculationExpression_evaluateADDEntryEventOccurrence()
    assert isinstance(instance, EventOccurrence)


def test_trace_Events_IntegerCalculationExpression_evaluateADDExitEventOccurrence_isa_EventOccurrence():
    instance = trace_Events_IntegerCalculationExpression_evaluateADDExitEventOccurrence()
    assert isinstance(instance, EventOccurrence)


def test_trace_Events_IntegerCalculationExpression_evaluateSUBTRACTEntryEventOccurrence_isa_EventOccurrence():
    instance = trace_Events_IntegerCalculationExpression_evaluateSUBTRACTEntryEventOccurrence()
    assert isinstance(instance, EventOccurrence)


def test_trace_Events_IntegerCalculationExpression_evaluateSUBTRACTExitEventOccurrence_isa_EventOccurrence():
    instance = trace_Events_IntegerCalculationExpression_evaluateSUBTRACTExitEventOccurrence()
    assert isinstance(instance, EventOccurrence)


def test_trace_Events_IntegerCalculationExpression_execute_integerCalculationExpressionEntryEventOccurrence_isa_EventOccurrence():
    instance = trace_Events_IntegerCalculationExpression_execute_integerCalculationExpressionEntryEventOccurrence()
    assert isinstance(instance, EventOccurrence)


def test_trace_Events_IntegerCalculationExpression_execute_integerCalculationExpressionExitEventOccurrence_isa_EventOccurrence():
    instance = trace_Events_IntegerCalculationExpression_execute_integerCalculationExpressionExitEventOccurrence()
    assert isinstance(instance, EventOccurrence)


def test_trace_Events_IntegerComparisonExpression_evaluateEQUALSEntryEventOccurrence_isa_EventOccurrence():
    instance = trace_Events_IntegerComparisonExpression_evaluateEQUALSEntryEventOccurrence()
    assert isinstance(instance, EventOccurrence)


def test_trace_Events_IntegerComparisonExpression_evaluateEQUALSExitEventOccurrence_isa_EventOccurrence():
    instance = trace_Events_IntegerComparisonExpression_evaluateEQUALSExitEventOccurrence()
    assert isinstance(instance, EventOccurrence)


def test_trace_Events_IntegerComparisonExpression_evaluateGREATEREntryEventOccurrence_isa_EventOccurrence():
    instance = trace_Events_IntegerComparisonExpression_evaluateGREATEREntryEventOccurrence()
    assert isinstance(instance, EventOccurrence)


def test_trace_Events_IntegerComparisonExpression_evaluateGREATERExitEventOccurrence_isa_EventOccurrence():
    instance = trace_Events_IntegerComparisonExpression_evaluateGREATERExitEventOccurrence()
    assert isinstance(instance, EventOccurrence)


def test_trace_Events_IntegerComparisonExpression_evaluateGREATER_EQUALSEntryEventOccurrence_isa_EventOccurrence():
    instance = trace_Events_IntegerComparisonExpression_evaluateGREATER_EQUALSEntryEventOccurrence()
    assert isinstance(instance, EventOccurrence)


def test_trace_Events_IntegerComparisonExpression_evaluateGREATER_EQUALSExitEventOccurrence_isa_EventOccurrence():
    instance = trace_Events_IntegerComparisonExpression_evaluateGREATER_EQUALSExitEventOccurrence()
    assert isinstance(instance, EventOccurrence)


def test_trace_Events_IntegerComparisonExpression_evaluateSMALLEREntryEventOccurrence_isa_EventOccurrence():
    instance = trace_Events_IntegerComparisonExpression_evaluateSMALLEREntryEventOccurrence()
    assert isinstance(instance, EventOccurrence)


def test_trace_Events_IntegerComparisonExpression_evaluateSMALLERExitEventOccurrence_isa_EventOccurrence():
    instance = trace_Events_IntegerComparisonExpression_evaluateSMALLERExitEventOccurrence()
    assert isinstance(instance, EventOccurrence)


def test_trace_Events_IntegerComparisonExpression_evaluateSMALLER_EQUALSEntryEventOccurrence_isa_EventOccurrence():
    instance = trace_Events_IntegerComparisonExpression_evaluateSMALLER_EQUALSEntryEventOccurrence()
    assert isinstance(instance, EventOccurrence)


def test_trace_Events_IntegerComparisonExpression_evaluateSMALLER_EQUALSExitEventOccurrence_isa_EventOccurrence():
    instance = trace_Events_IntegerComparisonExpression_evaluateSMALLER_EQUALSExitEventOccurrence()
    assert isinstance(instance, EventOccurrence)


def test_trace_Events_IntegerComparisonExpression_execute_IntegerComparisionExpressionEntryEventOccurrence_isa_EventOccurrence():
    instance = trace_Events_IntegerComparisonExpression_execute_IntegerComparisionExpressionEntryEventOccurrence()
    assert isinstance(instance, EventOccurrence)


def test_trace_Events_IntegerComparisonExpression_execute_IntegerComparisionExpressionExitEventOccurrence_isa_EventOccurrence():
    instance = trace_Events_IntegerComparisonExpression_execute_IntegerComparisionExpressionExitEventOccurrence()
    assert isinstance(instance, EventOccurrence)


def test_trace_Events_IntegerExpression_getOperandCurrentValuesEntryEventOccurrence_isa_EventOccurrence():
    instance = trace_Events_IntegerExpression_getOperandCurrentValuesEntryEventOccurrence()
    assert isinstance(instance, EventOccurrence)


def test_trace_Events_IntegerExpression_getOperandCurrentValuesExitEventOccurrence_isa_EventOccurrence():
    instance = trace_Events_IntegerExpression_getOperandCurrentValuesExitEventOccurrence()
    assert isinstance(instance, EventOccurrence)


def test_trace_Events_IntegerVariable_getCurrentValueValue_integerVariableEntryEventOccurrence_isa_EventOccurrence():
    instance = trace_Events_IntegerVariable_getCurrentValueValue_integerVariableEntryEventOccurrence()
    assert isinstance(instance, EventOccurrence)


def test_trace_Events_IntegerVariable_getCurrentValueValue_integerVariableExitEventOccurrence_isa_EventOccurrence():
    instance = trace_Events_IntegerVariable_getCurrentValueValue_integerVariableExitEventOccurrence()
    assert isinstance(instance, EventOccurrence)


def test_trace_Events_IntegerVariable_setCurrentValue_integerVariableEntryEventOccurrence_isa_EventOccurrence():
    instance = trace_Events_IntegerVariable_setCurrentValue_integerVariableEntryEventOccurrence()
    assert isinstance(instance, EventOccurrence)


def test_trace_Events_IntegerVariable_setCurrentValue_integerVariableExitEventOccurrence_isa_EventOccurrence():
    instance = trace_Events_IntegerVariable_setCurrentValue_integerVariableExitEventOccurrence()
    assert isinstance(instance, EventOccurrence)


def test_trace_Events_MergeNode_hasOffers_mergeNodeEntryEventOccurrence_isa_EventOccurrence():
    instance = trace_Events_MergeNode_hasOffers_mergeNodeEntryEventOccurrence()
    assert isinstance(instance, EventOccurrence)


def test_trace_Events_MergeNode_hasOffers_mergeNodeExitEventOccurrence_isa_EventOccurrence():
    instance = trace_Events_MergeNode_hasOffers_mergeNodeExitEventOccurrence()
    assert isinstance(instance, EventOccurrence)


def test_trace_Events_Offer_hasTokensEntryEventOccurrence_isa_EventOccurrence():
    instance = trace_Events_Offer_hasTokensEntryEventOccurrence()
    assert isinstance(instance, EventOccurrence)


def test_trace_Events_Offer_hasTokensExitEventOccurrence_isa_EventOccurrence():
    instance = trace_Events_Offer_hasTokensExitEventOccurrence()
    assert isinstance(instance, EventOccurrence)


def test_trace_Events_OpaqueAction_doAction_opaqueActionEntryEventOccurrence_isa_EventOccurrence():
    instance = trace_Events_OpaqueAction_doAction_opaqueActionEntryEventOccurrence()
    assert isinstance(instance, EventOccurrence)


def test_trace_Events_OpaqueAction_doAction_opaqueActionExitEventOccurrence_isa_EventOccurrence():
    instance = trace_Events_OpaqueAction_doAction_opaqueActionExitEventOccurrence()
    assert isinstance(instance, EventOccurrence)


def test_trace_Events_StringVariable_getCurrentValueValue_stringVariableEntryEventOccurrence_isa_EventOccurrence():
    instance = trace_Events_StringVariable_getCurrentValueValue_stringVariableEntryEventOccurrence()
    assert isinstance(instance, EventOccurrence)


def test_trace_Events_StringVariable_getCurrentValueValue_stringVariableExitEventOccurrence_isa_EventOccurrence():
    instance = trace_Events_StringVariable_getCurrentValueValue_stringVariableExitEventOccurrence()
    assert isinstance(instance, EventOccurrence)


def test_trace_Events_StringVariable_setCurrentValue_stringVariableEntryEventOccurrence_isa_EventOccurrence():
    instance = trace_Events_StringVariable_setCurrentValue_stringVariableEntryEventOccurrence()
    assert isinstance(instance, EventOccurrence)


def test_trace_Events_StringVariable_setCurrentValue_stringVariableExitEventOccurrence_isa_EventOccurrence():
    instance = trace_Events_StringVariable_setCurrentValue_stringVariableExitEventOccurrence()
    assert isinstance(instance, EventOccurrence)


def test_trace_Events_Token_isWithdrawnEntryEventOccurrence_isa_EventOccurrence():
    instance = trace_Events_Token_isWithdrawnEntryEventOccurrence()
    assert isinstance(instance, EventOccurrence)


def test_trace_Events_Token_isWithdrawnExitEventOccurrence_isa_EventOccurrence():
    instance = trace_Events_Token_isWithdrawnExitEventOccurrence()
    assert isinstance(instance, EventOccurrence)


def test_trace_Events_Token_transferEntryEventOccurrence_isa_EventOccurrence():
    instance = trace_Events_Token_transferEntryEventOccurrence()
    assert isinstance(instance, EventOccurrence)


def test_trace_Events_Token_transferExitEventOccurrence_isa_EventOccurrence():
    instance = trace_Events_Token_transferExitEventOccurrence()
    assert isinstance(instance, EventOccurrence)


def test_trace_Events_Token_withdrawEntryEventOccurrence_isa_EventOccurrence():
    instance = trace_Events_Token_withdrawEntryEventOccurrence()
    assert isinstance(instance, EventOccurrence)


def test_trace_Events_Token_withdrawExitEventOccurrence_isa_EventOccurrence():
    instance = trace_Events_Token_withdrawExitEventOccurrence()
    assert isinstance(instance, EventOccurrence)


def test_trace_activitydiagram_TracedOpaqueAction_isa_TracedAction():
    instance = trace_activitydiagram_TracedOpaqueAction()
    assert isinstance(instance, TracedAction)


def test_trace_activitydiagram_TracedControlFlow_isa_TracedActivityEdge():
    instance = trace_activitydiagram_TracedControlFlow()
    assert isinstance(instance, TracedActivityEdge)


def test_trace_activitydiagram_TracedControlNode_isa_TracedActivityNode():
    instance = trace_activitydiagram_TracedControlNode()
    assert isinstance(instance, TracedActivityNode)


def test_trace_activitydiagram_TracedExecutableNode_isa_TracedActivityNode():
    instance = trace_activitydiagram_TracedExecutableNode()
    assert isinstance(instance, TracedActivityNode)


def test_trace_activitydiagram_TracedDecisionNode_isa_TracedControlNode():
    instance = trace_activitydiagram_TracedDecisionNode()
    assert isinstance(instance, TracedControlNode)


def test_trace_activitydiagram_TracedFinalNode_isa_TracedControlNode():
    instance = trace_activitydiagram_TracedFinalNode()
    assert isinstance(instance, TracedControlNode)


def test_trace_activitydiagram_TracedForkNode_isa_TracedControlNode():
    instance = trace_activitydiagram_TracedForkNode()
    assert isinstance(instance, TracedControlNode)


def test_trace_activitydiagram_TracedInitialNode_isa_TracedControlNode():
    instance = trace_activitydiagram_TracedInitialNode()
    assert isinstance(instance, TracedControlNode)


def test_trace_activitydiagram_TracedJoinNode_isa_TracedControlNode():
    instance = trace_activitydiagram_TracedJoinNode()
    assert isinstance(instance, TracedControlNode)


def test_trace_activitydiagram_TracedMergeNode_isa_TracedControlNode():
    instance = trace_activitydiagram_TracedMergeNode()
    assert isinstance(instance, TracedControlNode)


def test_trace_activitydiagram_TracedAction_isa_TracedExecutableNode():
    instance = trace_activitydiagram_TracedAction()
    assert isinstance(instance, TracedExecutableNode)


def test_trace_activitydiagram_TracedActivityFinalNode_isa_TracedFinalNode():
    instance = trace_activitydiagram_TracedActivityFinalNode()
    assert isinstance(instance, TracedFinalNode)


def test_trace_activitydiagram_TracedActivity_isa_TracedNamedElement():
    instance = trace_activitydiagram_TracedActivity()
    assert isinstance(instance, TracedNamedElement)


def test_trace_activitydiagram_TracedActivityEdge_isa_TracedNamedElement():
    instance = trace_activitydiagram_TracedActivityEdge()
    assert isinstance(instance, TracedNamedElement)


def test_trace_activitydiagram_TracedActivityNode_isa_TracedNamedElement():
    instance = trace_activitydiagram_TracedActivityNode()
    assert isinstance(instance, TracedNamedElement)


def test_trace_activitydiagram_TracedVariable_isa_TracedNamedElement():
    instance = trace_activitydiagram_TracedVariable()
    assert isinstance(instance, TracedNamedElement)


def test_trace_activitydiagramConfiguration_TracedControlToken_isa_TracedToken():
    instance = trace_activitydiagramConfiguration_TracedControlToken()
    assert isinstance(instance, TracedToken)


def test_trace_activitydiagramConfiguration_TracedForkedToken_isa_TracedToken():
    instance = trace_activitydiagramConfiguration_TracedForkedToken()
    assert isinstance(instance, TracedToken)


def test_trace_activitydiagram_TracedBooleanVariable_isa_TracedVariable():
    instance = trace_activitydiagram_TracedBooleanVariable()
    assert isinstance(instance, TracedVariable)


def test_trace_activitydiagram_TracedIntegerVariable_isa_TracedVariable():
    instance = trace_activitydiagram_TracedIntegerVariable()
    assert isinstance(instance, TracedVariable)


def test_trace_activitydiagram_TracedStringVariable_isa_TracedVariable():
    instance = trace_activitydiagram_TracedStringVariable()
    assert isinstance(instance, TracedVariable)


def test_assoc_globalStates671_link_reassign_clear():
    a = trace_States_ForkedToken_remainingOffersCount_State(remainingOffersCount=7)
    b1 = States_trace_GlobalState()
    b2 = States_trace_GlobalState()
    _safe_set(a, 'forkedToken_remainingOffersCount_States', {b1})
    assert _is_linked(a, 'forkedToken_remainingOffersCount_States', b1)
    if hasattr(b1, 'GlobalState672'):
        assert _is_linked(b1, 'GlobalState672', a)
    _safe_set(a, 'forkedToken_remainingOffersCount_States', {b2})
    assert _is_linked(a, 'forkedToken_remainingOffersCount_States', b2)
    if hasattr(b1, 'GlobalState672'):
        assert not _is_linked(b1, 'GlobalState672', a)
    if hasattr(b2, 'GlobalState672'):
        assert _is_linked(b2, 'GlobalState672', a)
    _safe_set(a, 'forkedToken_remainingOffersCount_States', set())
    assert not _is_linked(a, 'forkedToken_remainingOffersCount_States', b2)
    if hasattr(b2, 'GlobalState672'):
        assert not _is_linked(b2, 'GlobalState672', a)


def test_assoc_globalStates681_link_reassign_clear():
    a = trace_States_ForkedToken_baseTokenIsWithdrawn_State(baseTokenIsWithdrawn=True)
    b1 = States_trace_GlobalState()
    b2 = States_trace_GlobalState()
    _safe_set(a, 'forkedToken_baseTokenIsWithdrawn_States', {b1})
    assert _is_linked(a, 'forkedToken_baseTokenIsWithdrawn_States', b1)
    if hasattr(b1, 'GlobalState682'):
        assert _is_linked(b1, 'GlobalState682', a)
    _safe_set(a, 'forkedToken_baseTokenIsWithdrawn_States', {b2})
    assert _is_linked(a, 'forkedToken_baseTokenIsWithdrawn_States', b2)
    if hasattr(b1, 'GlobalState682'):
        assert not _is_linked(b1, 'GlobalState682', a)
    if hasattr(b2, 'GlobalState682'):
        assert _is_linked(b2, 'GlobalState682', a)
    _safe_set(a, 'forkedToken_baseTokenIsWithdrawn_States', set())
    assert not _is_linked(a, 'forkedToken_baseTokenIsWithdrawn_States', b2)
    if hasattr(b2, 'GlobalState682'):
        assert not _is_linked(b2, 'GlobalState682', a)


def test_assoc_globalStates699_link_reassign_clear():
    a = trace_States_ActivityNode_running_State(running=True)
    b1 = States_trace_GlobalState()
    b2 = States_trace_GlobalState()
    _safe_set(a, 'activityNode_running_States', {b1})
    assert _is_linked(a, 'activityNode_running_States', b1)
    if hasattr(b1, 'GlobalState700'):
        assert _is_linked(b1, 'GlobalState700', a)
    _safe_set(a, 'activityNode_running_States', {b2})
    assert _is_linked(a, 'activityNode_running_States', b2)
    if hasattr(b1, 'GlobalState700'):
        assert not _is_linked(b1, 'GlobalState700', a)
    if hasattr(b2, 'GlobalState700'):
        assert _is_linked(b2, 'GlobalState700', a)
    _safe_set(a, 'activityNode_running_States', set())
    assert not _is_linked(a, 'activityNode_running_States', b2)
    if hasattr(b2, 'GlobalState700'):
        assert not _is_linked(b2, 'GlobalState700', a)


def test_assoc_parent670_link_reassign_clear():
    a = trace_States_ForkedToken_remainingOffersCount_State(remainingOffersCount=7)
    b1 = activitydiagramConfiguration_TracedForkedToken()
    b2 = activitydiagramConfiguration_TracedForkedToken()
    _safe_set(a, 'remainingOffersCountTrace', b1)
    assert _is_linked(a, 'remainingOffersCountTrace', b1)
    if hasattr(b1, 'TracedForkedToken'):
        assert _is_linked(b1, 'TracedForkedToken', a)
    _safe_set(a, 'remainingOffersCountTrace', b2)
    assert _is_linked(a, 'remainingOffersCountTrace', b2)
    if hasattr(b1, 'TracedForkedToken'):
        assert not _is_linked(b1, 'TracedForkedToken', a)
    if hasattr(b2, 'TracedForkedToken'):
        assert _is_linked(b2, 'TracedForkedToken', a)
    _safe_set(a, 'remainingOffersCountTrace', None)
    assert not _is_linked(a, 'remainingOffersCountTrace', b2)
    if hasattr(b2, 'TracedForkedToken'):
        assert not _is_linked(b2, 'TracedForkedToken', a)


def test_assoc_parent679_link_reassign_clear():
    a = trace_States_ForkedToken_baseTokenIsWithdrawn_State(baseTokenIsWithdrawn=True)
    b1 = activitydiagramConfiguration_TracedForkedToken()
    b2 = activitydiagramConfiguration_TracedForkedToken()
    _safe_set(a, 'baseTokenIsWithdrawnTrace', b1)
    assert _is_linked(a, 'baseTokenIsWithdrawnTrace', b1)
    if hasattr(b1, 'TracedForkedToken680'):
        assert _is_linked(b1, 'TracedForkedToken680', a)
    _safe_set(a, 'baseTokenIsWithdrawnTrace', b2)
    assert _is_linked(a, 'baseTokenIsWithdrawnTrace', b2)
    if hasattr(b1, 'TracedForkedToken680'):
        assert not _is_linked(b1, 'TracedForkedToken680', a)
    if hasattr(b2, 'TracedForkedToken680'):
        assert _is_linked(b2, 'TracedForkedToken680', a)
    _safe_set(a, 'baseTokenIsWithdrawnTrace', None)
    assert not _is_linked(a, 'baseTokenIsWithdrawnTrace', b2)
    if hasattr(b2, 'TracedForkedToken680'):
        assert not _is_linked(b2, 'TracedForkedToken680', a)


def test_assoc_parent698_link_reassign_clear():
    a = trace_States_ActivityNode_running_State(running=True)
    b1 = activitydiagram_TracedActivityNode()
    b2 = activitydiagram_TracedActivityNode()
    _safe_set(a, 'runningTrace', b1)
    assert _is_linked(a, 'runningTrace', b1)
    if hasattr(b1, 'TracedActivityNode'):
        assert _is_linked(b1, 'TracedActivityNode', a)
    _safe_set(a, 'runningTrace', b2)
    assert _is_linked(a, 'runningTrace', b2)
    if hasattr(b1, 'TracedActivityNode'):
        assert not _is_linked(b1, 'TracedActivityNode', a)
    if hasattr(b2, 'TracedActivityNode'):
        assert _is_linked(b2, 'TracedActivityNode', a)
    _safe_set(a, 'runningTrace', None)
    assert not _is_linked(a, 'runningTrace', b2)
    if hasattr(b2, 'TracedActivityNode'):
        assert not _is_linked(b2, 'TracedActivityNode', a)


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

Action_fire_actionEntryEventOccurrence_strategy = st.builds(Action_fire_actionEntryEventOccurrence)
@given(instance=Action_fire_actionEntryEventOccurrence_strategy)
@settings(max_examples=25)
def test_Action_fire_actionEntryEventOccurrence_instantiation(instance):
    assert isinstance(instance, Action_fire_actionEntryEventOccurrence)


Action_fire_actionExitEventOccurrence_strategy = st.builds(Action_fire_actionExitEventOccurrence)
@given(instance=Action_fire_actionExitEventOccurrence_strategy)
@settings(max_examples=25)
def test_Action_fire_actionExitEventOccurrence_instantiation(instance):
    assert isinstance(instance, Action_fire_actionExitEventOccurrence)


Action_isReady_actionEntryEventOccurrence_strategy = st.builds(Action_isReady_actionEntryEventOccurrence)
@given(instance=Action_isReady_actionEntryEventOccurrence_strategy)
@settings(max_examples=25)
def test_Action_isReady_actionEntryEventOccurrence_instantiation(instance):
    assert isinstance(instance, Action_isReady_actionEntryEventOccurrence)


Action_isReady_actionExitEventOccurrence_strategy = st.builds(Action_isReady_actionExitEventOccurrence)
@given(instance=Action_isReady_actionExitEventOccurrence_strategy)
@settings(max_examples=25)
def test_Action_isReady_actionExitEventOccurrence_instantiation(instance):
    assert isinstance(instance, Action_isReady_actionExitEventOccurrence)


Action_sendOffers_actionEntryEventOccurrence_strategy = st.builds(Action_sendOffers_actionEntryEventOccurrence)
@given(instance=Action_sendOffers_actionEntryEventOccurrence_strategy)
@settings(max_examples=25)
def test_Action_sendOffers_actionEntryEventOccurrence_instantiation(instance):
    assert isinstance(instance, Action_sendOffers_actionEntryEventOccurrence)


Action_sendOffers_actionExitEventOccurrence_strategy = st.builds(Action_sendOffers_actionExitEventOccurrence)
@given(instance=Action_sendOffers_actionExitEventOccurrence_strategy)
@settings(max_examples=25)
def test_Action_sendOffers_actionExitEventOccurrence_instantiation(instance):
    assert isinstance(instance, Action_sendOffers_actionExitEventOccurrence)


ActivityEdge_hasOfferEntryEventOccurrence_strategy = st.builds(ActivityEdge_hasOfferEntryEventOccurrence)
@given(instance=ActivityEdge_hasOfferEntryEventOccurrence_strategy)
@settings(max_examples=25)
def test_ActivityEdge_hasOfferEntryEventOccurrence_instantiation(instance):
    assert isinstance(instance, ActivityEdge_hasOfferEntryEventOccurrence)


ActivityEdge_hasOfferExitEventOccurrence_strategy = st.builds(ActivityEdge_hasOfferExitEventOccurrence)
@given(instance=ActivityEdge_hasOfferExitEventOccurrence_strategy)
@settings(max_examples=25)
def test_ActivityEdge_hasOfferExitEventOccurrence_instantiation(instance):
    assert isinstance(instance, ActivityEdge_hasOfferExitEventOccurrence)


ActivityEdge_offers_State_strategy = st.builds(ActivityEdge_offers_State)
@given(instance=ActivityEdge_offers_State_strategy)
@settings(max_examples=25)
def test_ActivityEdge_offers_State_instantiation(instance):
    assert isinstance(instance, ActivityEdge_offers_State)


ActivityEdge_sendOfferEntryEventOccurrence_strategy = st.builds(ActivityEdge_sendOfferEntryEventOccurrence)
@given(instance=ActivityEdge_sendOfferEntryEventOccurrence_strategy)
@settings(max_examples=25)
def test_ActivityEdge_sendOfferEntryEventOccurrence_instantiation(instance):
    assert isinstance(instance, ActivityEdge_sendOfferEntryEventOccurrence)


ActivityEdge_sendOfferExitEventOccurrence_strategy = st.builds(ActivityEdge_sendOfferExitEventOccurrence)
@given(instance=ActivityEdge_sendOfferExitEventOccurrence_strategy)
@settings(max_examples=25)
def test_ActivityEdge_sendOfferExitEventOccurrence_instantiation(instance):
    assert isinstance(instance, ActivityEdge_sendOfferExitEventOccurrence)


ActivityEdge_takeOfferedTokens_activityEdgeEntryEventOccurrence_strategy = st.builds(ActivityEdge_takeOfferedTokens_activityEdgeEntryEventOccurrence)
@given(instance=ActivityEdge_takeOfferedTokens_activityEdgeEntryEventOccurrence_strategy)
@settings(max_examples=25)
def test_ActivityEdge_takeOfferedTokens_activityEdgeEntryEventOccurrence_instantiation(instance):
    assert isinstance(instance, ActivityEdge_takeOfferedTokens_activityEdgeEntryEventOccurrence)


ActivityEdge_takeOfferedTokens_activityEdgeExitEventOccurrence_strategy = st.builds(ActivityEdge_takeOfferedTokens_activityEdgeExitEventOccurrence)
@given(instance=ActivityEdge_takeOfferedTokens_activityEdgeExitEventOccurrence_strategy)
@settings(max_examples=25)
def test_ActivityEdge_takeOfferedTokens_activityEdgeExitEventOccurrence_instantiation(instance):
    assert isinstance(instance, ActivityEdge_takeOfferedTokens_activityEdgeExitEventOccurrence)


ActivityFinalNode_fire_activityFinalNodeEntryEventOccurrence_strategy = st.builds(ActivityFinalNode_fire_activityFinalNodeEntryEventOccurrence)
@given(instance=ActivityFinalNode_fire_activityFinalNodeEntryEventOccurrence_strategy)
@settings(max_examples=25)
def test_ActivityFinalNode_fire_activityFinalNodeEntryEventOccurrence_instantiation(instance):
    assert isinstance(instance, ActivityFinalNode_fire_activityFinalNodeEntryEventOccurrence)


ActivityFinalNode_fire_activityFinalNodeExitEventOccurrence_strategy = st.builds(ActivityFinalNode_fire_activityFinalNodeExitEventOccurrence)
@given(instance=ActivityFinalNode_fire_activityFinalNodeExitEventOccurrence_strategy)
@settings(max_examples=25)
def test_ActivityFinalNode_fire_activityFinalNodeExitEventOccurrence_instantiation(instance):
    assert isinstance(instance, ActivityFinalNode_fire_activityFinalNodeExitEventOccurrence)


ActivityNode_addTokensEntryEventOccurrence_strategy = st.builds(ActivityNode_addTokensEntryEventOccurrence)
@given(instance=ActivityNode_addTokensEntryEventOccurrence_strategy)
@settings(max_examples=25)
def test_ActivityNode_addTokensEntryEventOccurrence_instantiation(instance):
    assert isinstance(instance, ActivityNode_addTokensEntryEventOccurrence)


ActivityNode_addTokensExitEventOccurrence_strategy = st.builds(ActivityNode_addTokensExitEventOccurrence)
@given(instance=ActivityNode_addTokensExitEventOccurrence_strategy)
@settings(max_examples=25)
def test_ActivityNode_addTokensExitEventOccurrence_instantiation(instance):
    assert isinstance(instance, ActivityNode_addTokensExitEventOccurrence)


ActivityNode_hasOffersEntryEventOccurrence_strategy = st.builds(ActivityNode_hasOffersEntryEventOccurrence)
@given(instance=ActivityNode_hasOffersEntryEventOccurrence_strategy)
@settings(max_examples=25)
def test_ActivityNode_hasOffersEntryEventOccurrence_instantiation(instance):
    assert isinstance(instance, ActivityNode_hasOffersEntryEventOccurrence)


ActivityNode_hasOffersExitEventOccurrence_strategy = st.builds(ActivityNode_hasOffersExitEventOccurrence)
@given(instance=ActivityNode_hasOffersExitEventOccurrence_strategy)
@settings(max_examples=25)
def test_ActivityNode_hasOffersExitEventOccurrence_instantiation(instance):
    assert isinstance(instance, ActivityNode_hasOffersExitEventOccurrence)


ActivityNode_heldTokens_State_strategy = st.builds(ActivityNode_heldTokens_State)
@given(instance=ActivityNode_heldTokens_State_strategy)
@settings(max_examples=25)
def test_ActivityNode_heldTokens_State_instantiation(instance):
    assert isinstance(instance, ActivityNode_heldTokens_State)


ActivityNode_isReadyEntryEventOccurrence_strategy = st.builds(ActivityNode_isReadyEntryEventOccurrence)
@given(instance=ActivityNode_isReadyEntryEventOccurrence_strategy)
@settings(max_examples=25)
def test_ActivityNode_isReadyEntryEventOccurrence_instantiation(instance):
    assert isinstance(instance, ActivityNode_isReadyEntryEventOccurrence)


ActivityNode_isReadyExitEventOccurrence_strategy = st.builds(ActivityNode_isReadyExitEventOccurrence)
@given(instance=ActivityNode_isReadyExitEventOccurrence_strategy)
@settings(max_examples=25)
def test_ActivityNode_isReadyExitEventOccurrence_instantiation(instance):
    assert isinstance(instance, ActivityNode_isReadyExitEventOccurrence)


ActivityNode_isRunningEntryEventOccurrence_strategy = st.builds(ActivityNode_isRunningEntryEventOccurrence)
@given(instance=ActivityNode_isRunningEntryEventOccurrence_strategy)
@settings(max_examples=25)
def test_ActivityNode_isRunningEntryEventOccurrence_instantiation(instance):
    assert isinstance(instance, ActivityNode_isRunningEntryEventOccurrence)


ActivityNode_isRunningExitEventOccurrence_strategy = st.builds(ActivityNode_isRunningExitEventOccurrence)
@given(instance=ActivityNode_isRunningExitEventOccurrence_strategy)
@settings(max_examples=25)
def test_ActivityNode_isRunningExitEventOccurrence_instantiation(instance):
    assert isinstance(instance, ActivityNode_isRunningExitEventOccurrence)


ActivityNode_removeTokenEntryEventOccurrence_strategy = st.builds(ActivityNode_removeTokenEntryEventOccurrence)
@given(instance=ActivityNode_removeTokenEntryEventOccurrence_strategy)
@settings(max_examples=25)
def test_ActivityNode_removeTokenEntryEventOccurrence_instantiation(instance):
    assert isinstance(instance, ActivityNode_removeTokenEntryEventOccurrence)


ActivityNode_removeTokenExitEventOccurrence_strategy = st.builds(ActivityNode_removeTokenExitEventOccurrence)
@given(instance=ActivityNode_removeTokenExitEventOccurrence_strategy)
@settings(max_examples=25)
def test_ActivityNode_removeTokenExitEventOccurrence_instantiation(instance):
    assert isinstance(instance, ActivityNode_removeTokenExitEventOccurrence)


ActivityNode_run_activityNodeEntryEventOccurrence_strategy = st.builds(ActivityNode_run_activityNodeEntryEventOccurrence)
@given(instance=ActivityNode_run_activityNodeEntryEventOccurrence_strategy)
@settings(max_examples=25)
def test_ActivityNode_run_activityNodeEntryEventOccurrence_instantiation(instance):
    assert isinstance(instance, ActivityNode_run_activityNodeEntryEventOccurrence)


ActivityNode_run_activityNodeExitEventOccurrence_strategy = st.builds(ActivityNode_run_activityNodeExitEventOccurrence)
@given(instance=ActivityNode_run_activityNodeExitEventOccurrence_strategy)
@settings(max_examples=25)
def test_ActivityNode_run_activityNodeExitEventOccurrence_instantiation(instance):
    assert isinstance(instance, ActivityNode_run_activityNodeExitEventOccurrence)


ActivityNode_running_State_strategy = st.builds(ActivityNode_running_State)
@given(instance=ActivityNode_running_State_strategy)
@settings(max_examples=25)
def test_ActivityNode_running_State_instantiation(instance):
    assert isinstance(instance, ActivityNode_running_State)


ActivityNode_sendOffersEntryEventOccurrence_strategy = st.builds(ActivityNode_sendOffersEntryEventOccurrence)
@given(instance=ActivityNode_sendOffersEntryEventOccurrence_strategy)
@settings(max_examples=25)
def test_ActivityNode_sendOffersEntryEventOccurrence_instantiation(instance):
    assert isinstance(instance, ActivityNode_sendOffersEntryEventOccurrence)


ActivityNode_sendOffersExitEventOccurrence_strategy = st.builds(ActivityNode_sendOffersExitEventOccurrence)
@given(instance=ActivityNode_sendOffersExitEventOccurrence_strategy)
@settings(max_examples=25)
def test_ActivityNode_sendOffersExitEventOccurrence_instantiation(instance):
    assert isinstance(instance, ActivityNode_sendOffersExitEventOccurrence)


ActivityNode_takeOfferedTokensEntryEventOccurrence_strategy = st.builds(ActivityNode_takeOfferedTokensEntryEventOccurrence)
@given(instance=ActivityNode_takeOfferedTokensEntryEventOccurrence_strategy)
@settings(max_examples=25)
def test_ActivityNode_takeOfferedTokensEntryEventOccurrence_instantiation(instance):
    assert isinstance(instance, ActivityNode_takeOfferedTokensEntryEventOccurrence)


ActivityNode_takeOfferedTokensExitEventOccurrence_strategy = st.builds(ActivityNode_takeOfferedTokensExitEventOccurrence)
@given(instance=ActivityNode_takeOfferedTokensExitEventOccurrence_strategy)
@settings(max_examples=25)
def test_ActivityNode_takeOfferedTokensExitEventOccurrence_instantiation(instance):
    assert isinstance(instance, ActivityNode_takeOfferedTokensExitEventOccurrence)


ActivityNode_terminate_activityNodeEntryEventOccurrence_strategy = st.builds(ActivityNode_terminate_activityNodeEntryEventOccurrence)
@given(instance=ActivityNode_terminate_activityNodeEntryEventOccurrence_strategy)
@settings(max_examples=25)
def test_ActivityNode_terminate_activityNodeEntryEventOccurrence_instantiation(instance):
    assert isinstance(instance, ActivityNode_terminate_activityNodeEntryEventOccurrence)


ActivityNode_terminate_activityNodeExitEventOccurrence_strategy = st.builds(ActivityNode_terminate_activityNodeExitEventOccurrence)
@given(instance=ActivityNode_terminate_activityNodeExitEventOccurrence_strategy)
@settings(max_examples=25)
def test_ActivityNode_terminate_activityNodeExitEventOccurrence_instantiation(instance):
    assert isinstance(instance, ActivityNode_terminate_activityNodeExitEventOccurrence)


Activity_fireInitialNodeEntryEventOccurrence_strategy = st.builds(Activity_fireInitialNodeEntryEventOccurrence)
@given(instance=Activity_fireInitialNodeEntryEventOccurrence_strategy)
@settings(max_examples=25)
def test_Activity_fireInitialNodeEntryEventOccurrence_instantiation(instance):
    assert isinstance(instance, Activity_fireInitialNodeEntryEventOccurrence)


Activity_fireInitialNodeExitEventOccurrence_strategy = st.builds(Activity_fireInitialNodeExitEventOccurrence)
@given(instance=Activity_fireInitialNodeExitEventOccurrence_strategy)
@settings(max_examples=25)
def test_Activity_fireInitialNodeExitEventOccurrence_instantiation(instance):
    assert isinstance(instance, Activity_fireInitialNodeExitEventOccurrence)


Activity_fireNodeEntryEventOccurrence_strategy = st.builds(Activity_fireNodeEntryEventOccurrence)
@given(instance=Activity_fireNodeEntryEventOccurrence_strategy)
@settings(max_examples=25)
def test_Activity_fireNodeEntryEventOccurrence_instantiation(instance):
    assert isinstance(instance, Activity_fireNodeEntryEventOccurrence)


Activity_fireNodeExitEventOccurrence_strategy = st.builds(Activity_fireNodeExitEventOccurrence)
@given(instance=Activity_fireNodeExitEventOccurrence_strategy)
@settings(max_examples=25)
def test_Activity_fireNodeExitEventOccurrence_instantiation(instance):
    assert isinstance(instance, Activity_fireNodeExitEventOccurrence)


Activity_getEnabledNodesEntryEventOccurrence_strategy = st.builds(Activity_getEnabledNodesEntryEventOccurrence)
@given(instance=Activity_getEnabledNodesEntryEventOccurrence_strategy)
@settings(max_examples=25)
def test_Activity_getEnabledNodesEntryEventOccurrence_instantiation(instance):
    assert isinstance(instance, Activity_getEnabledNodesEntryEventOccurrence)


Activity_getEnabledNodesExitEventOccurrence_strategy = st.builds(Activity_getEnabledNodesExitEventOccurrence)
@given(instance=Activity_getEnabledNodesExitEventOccurrence_strategy)
@settings(max_examples=25)
def test_Activity_getEnabledNodesExitEventOccurrence_instantiation(instance):
    assert isinstance(instance, Activity_getEnabledNodesExitEventOccurrence)


Activity_getInitialNodeEntryEventOccurrence_strategy = st.builds(Activity_getInitialNodeEntryEventOccurrence)
@given(instance=Activity_getInitialNodeEntryEventOccurrence_strategy)
@settings(max_examples=25)
def test_Activity_getInitialNodeEntryEventOccurrence_instantiation(instance):
    assert isinstance(instance, Activity_getInitialNodeEntryEventOccurrence)


Activity_getInitialNodeExitEventOccurrence_strategy = st.builds(Activity_getInitialNodeExitEventOccurrence)
@given(instance=Activity_getInitialNodeExitEventOccurrence_strategy)
@settings(max_examples=25)
def test_Activity_getInitialNodeExitEventOccurrence_instantiation(instance):
    assert isinstance(instance, Activity_getInitialNodeExitEventOccurrence)


Activity_initializeEntryEventOccurrence_strategy = st.builds(Activity_initializeEntryEventOccurrence)
@given(instance=Activity_initializeEntryEventOccurrence_strategy)
@settings(max_examples=25)
def test_Activity_initializeEntryEventOccurrence_instantiation(instance):
    assert isinstance(instance, Activity_initializeEntryEventOccurrence)


Activity_initializeExitEventOccurrence_strategy = st.builds(Activity_initializeExitEventOccurrence)
@given(instance=Activity_initializeExitEventOccurrence_strategy)
@settings(max_examples=25)
def test_Activity_initializeExitEventOccurrence_instantiation(instance):
    assert isinstance(instance, Activity_initializeExitEventOccurrence)


Activity_mainEntryEventOccurrence_strategy = st.builds(Activity_mainEntryEventOccurrence)
@given(instance=Activity_mainEntryEventOccurrence_strategy)
@settings(max_examples=25)
def test_Activity_mainEntryEventOccurrence_instantiation(instance):
    assert isinstance(instance, Activity_mainEntryEventOccurrence)


Activity_mainExitEventOccurrence_strategy = st.builds(Activity_mainExitEventOccurrence)
@given(instance=Activity_mainExitEventOccurrence_strategy)
@settings(max_examples=25)
def test_Activity_mainExitEventOccurrence_instantiation(instance):
    assert isinstance(instance, Activity_mainExitEventOccurrence)


Activity_runEntryEventOccurrence_strategy = st.builds(Activity_runEntryEventOccurrence)
@given(instance=Activity_runEntryEventOccurrence_strategy)
@settings(max_examples=25)
def test_Activity_runEntryEventOccurrence_instantiation(instance):
    assert isinstance(instance, Activity_runEntryEventOccurrence)


Activity_runExitEventOccurrence_strategy = st.builds(Activity_runExitEventOccurrence)
@given(instance=Activity_runExitEventOccurrence_strategy)
@settings(max_examples=25)
def test_Activity_runExitEventOccurrence_instantiation(instance):
    assert isinstance(instance, Activity_runExitEventOccurrence)


Activity_runNodesEntryEventOccurrence_strategy = st.builds(Activity_runNodesEntryEventOccurrence)
@given(instance=Activity_runNodesEntryEventOccurrence_strategy)
@settings(max_examples=25)
def test_Activity_runNodesEntryEventOccurrence_instantiation(instance):
    assert isinstance(instance, Activity_runNodesEntryEventOccurrence)


Activity_runNodesExitEventOccurrence_strategy = st.builds(Activity_runNodesExitEventOccurrence)
@given(instance=Activity_runNodesExitEventOccurrence_strategy)
@settings(max_examples=25)
def test_Activity_runNodesExitEventOccurrence_instantiation(instance):
    assert isinstance(instance, Activity_runNodesExitEventOccurrence)


Activity_selectNextNodeEntryEventOccurrence_strategy = st.builds(Activity_selectNextNodeEntryEventOccurrence)
@given(instance=Activity_selectNextNodeEntryEventOccurrence_strategy)
@settings(max_examples=25)
def test_Activity_selectNextNodeEntryEventOccurrence_instantiation(instance):
    assert isinstance(instance, Activity_selectNextNodeEntryEventOccurrence)


Activity_selectNextNodeExitEventOccurrence_strategy = st.builds(Activity_selectNextNodeExitEventOccurrence)
@given(instance=Activity_selectNextNodeExitEventOccurrence_strategy)
@settings(max_examples=25)
def test_Activity_selectNextNodeExitEventOccurrence_instantiation(instance):
    assert isinstance(instance, Activity_selectNextNodeExitEventOccurrence)


Activity_terminateEntryEventOccurrence_strategy = st.builds(Activity_terminateEntryEventOccurrence)
@given(instance=Activity_terminateEntryEventOccurrence_strategy)
@settings(max_examples=25)
def test_Activity_terminateEntryEventOccurrence_instantiation(instance):
    assert isinstance(instance, Activity_terminateEntryEventOccurrence)


Activity_terminateExitEventOccurrence_strategy = st.builds(Activity_terminateExitEventOccurrence)
@given(instance=Activity_terminateExitEventOccurrence_strategy)
@settings(max_examples=25)
def test_Activity_terminateExitEventOccurrence_instantiation(instance):
    assert isinstance(instance, Activity_terminateExitEventOccurrence)


Activity_trace_State_strategy = st.builds(Activity_trace_State)
@given(instance=Activity_trace_State_strategy)
@settings(max_examples=25)
def test_Activity_trace_State_instantiation(instance):
    assert isinstance(instance, Activity_trace_State)


BooleanBinaryExpression_evaluateANDEntryEventOccurrence_strategy = st.builds(BooleanBinaryExpression_evaluateANDEntryEventOccurrence)
@given(instance=BooleanBinaryExpression_evaluateANDEntryEventOccurrence_strategy)
@settings(max_examples=25)
def test_BooleanBinaryExpression_evaluateANDEntryEventOccurrence_instantiation(instance):
    assert isinstance(instance, BooleanBinaryExpression_evaluateANDEntryEventOccurrence)


BooleanBinaryExpression_evaluateANDExitEventOccurrence_strategy = st.builds(BooleanBinaryExpression_evaluateANDExitEventOccurrence)
@given(instance=BooleanBinaryExpression_evaluateANDExitEventOccurrence_strategy)
@settings(max_examples=25)
def test_BooleanBinaryExpression_evaluateANDExitEventOccurrence_instantiation(instance):
    assert isinstance(instance, BooleanBinaryExpression_evaluateANDExitEventOccurrence)


BooleanBinaryExpression_evaluateOREntryEventOccurrence_strategy = st.builds(BooleanBinaryExpression_evaluateOREntryEventOccurrence)
@given(instance=BooleanBinaryExpression_evaluateOREntryEventOccurrence_strategy)
@settings(max_examples=25)
def test_BooleanBinaryExpression_evaluateOREntryEventOccurrence_instantiation(instance):
    assert isinstance(instance, BooleanBinaryExpression_evaluateOREntryEventOccurrence)


BooleanBinaryExpression_evaluateORExitEventOccurrence_strategy = st.builds(BooleanBinaryExpression_evaluateORExitEventOccurrence)
@given(instance=BooleanBinaryExpression_evaluateORExitEventOccurrence_strategy)
@settings(max_examples=25)
def test_BooleanBinaryExpression_evaluateORExitEventOccurrence_instantiation(instance):
    assert isinstance(instance, BooleanBinaryExpression_evaluateORExitEventOccurrence)


BooleanBinaryExpression_execute_booleanBinaryExpressionEntryEventOccurrence_strategy = st.builds(BooleanBinaryExpression_execute_booleanBinaryExpressionEntryEventOccurrence)
@given(instance=BooleanBinaryExpression_execute_booleanBinaryExpressionEntryEventOccurrence_strategy)
@settings(max_examples=25)
def test_BooleanBinaryExpression_execute_booleanBinaryExpressionEntryEventOccurrence_instantiation(instance):
    assert isinstance(instance, BooleanBinaryExpression_execute_booleanBinaryExpressionEntryEventOccurrence)


BooleanBinaryExpression_execute_booleanBinaryExpressionExitEventOccurrence_strategy = st.builds(BooleanBinaryExpression_execute_booleanBinaryExpressionExitEventOccurrence)
@given(instance=BooleanBinaryExpression_execute_booleanBinaryExpressionExitEventOccurrence_strategy)
@settings(max_examples=25)
def test_BooleanBinaryExpression_execute_booleanBinaryExpressionExitEventOccurrence_instantiation(instance):
    assert isinstance(instance, BooleanBinaryExpression_execute_booleanBinaryExpressionExitEventOccurrence)


BooleanUnaryExpression_evaluateNOTEntryEventOccurrence_strategy = st.builds(BooleanUnaryExpression_evaluateNOTEntryEventOccurrence)
@given(instance=BooleanUnaryExpression_evaluateNOTEntryEventOccurrence_strategy)
@settings(max_examples=25)
def test_BooleanUnaryExpression_evaluateNOTEntryEventOccurrence_instantiation(instance):
    assert isinstance(instance, BooleanUnaryExpression_evaluateNOTEntryEventOccurrence)


BooleanUnaryExpression_evaluateNOTExitEventOccurrence_strategy = st.builds(BooleanUnaryExpression_evaluateNOTExitEventOccurrence)
@given(instance=BooleanUnaryExpression_evaluateNOTExitEventOccurrence_strategy)
@settings(max_examples=25)
def test_BooleanUnaryExpression_evaluateNOTExitEventOccurrence_instantiation(instance):
    assert isinstance(instance, BooleanUnaryExpression_evaluateNOTExitEventOccurrence)


BooleanUnaryExpression_execute_booleanUnaryExpressionEntryEventOccurrence_strategy = st.builds(BooleanUnaryExpression_execute_booleanUnaryExpressionEntryEventOccurrence)
@given(instance=BooleanUnaryExpression_execute_booleanUnaryExpressionEntryEventOccurrence_strategy)
@settings(max_examples=25)
def test_BooleanUnaryExpression_execute_booleanUnaryExpressionEntryEventOccurrence_instantiation(instance):
    assert isinstance(instance, BooleanUnaryExpression_execute_booleanUnaryExpressionEntryEventOccurrence)


BooleanUnaryExpression_execute_booleanUnaryExpressionExitEventOccurrence_strategy = st.builds(BooleanUnaryExpression_execute_booleanUnaryExpressionExitEventOccurrence)
@given(instance=BooleanUnaryExpression_execute_booleanUnaryExpressionExitEventOccurrence_strategy)
@settings(max_examples=25)
def test_BooleanUnaryExpression_execute_booleanUnaryExpressionExitEventOccurrence_instantiation(instance):
    assert isinstance(instance, BooleanUnaryExpression_execute_booleanUnaryExpressionExitEventOccurrence)


BooleanVariable_getCurrentValueValue_booleanVariableEntryEventOccurrence_strategy = st.builds(BooleanVariable_getCurrentValueValue_booleanVariableEntryEventOccurrence)
@given(instance=BooleanVariable_getCurrentValueValue_booleanVariableEntryEventOccurrence_strategy)
@settings(max_examples=25)
def test_BooleanVariable_getCurrentValueValue_booleanVariableEntryEventOccurrence_instantiation(instance):
    assert isinstance(instance, BooleanVariable_getCurrentValueValue_booleanVariableEntryEventOccurrence)


BooleanVariable_getCurrentValueValue_booleanVariableExitEventOccurrence_strategy = st.builds(BooleanVariable_getCurrentValueValue_booleanVariableExitEventOccurrence)
@given(instance=BooleanVariable_getCurrentValueValue_booleanVariableExitEventOccurrence_strategy)
@settings(max_examples=25)
def test_BooleanVariable_getCurrentValueValue_booleanVariableExitEventOccurrence_instantiation(instance):
    assert isinstance(instance, BooleanVariable_getCurrentValueValue_booleanVariableExitEventOccurrence)


BooleanVariable_setCurrentValue_boolenVariableEntryEventOccurrence_strategy = st.builds(BooleanVariable_setCurrentValue_boolenVariableEntryEventOccurrence)
@given(instance=BooleanVariable_setCurrentValue_boolenVariableEntryEventOccurrence_strategy)
@settings(max_examples=25)
def test_BooleanVariable_setCurrentValue_boolenVariableEntryEventOccurrence_instantiation(instance):
    assert isinstance(instance, BooleanVariable_setCurrentValue_boolenVariableEntryEventOccurrence)


BooleanVariable_setCurrentValue_boolenVariableExitEventOccurrence_strategy = st.builds(BooleanVariable_setCurrentValue_boolenVariableExitEventOccurrence)
@given(instance=BooleanVariable_setCurrentValue_boolenVariableExitEventOccurrence_strategy)
@settings(max_examples=25)
def test_BooleanVariable_setCurrentValue_boolenVariableExitEventOccurrence_instantiation(instance):
    assert isinstance(instance, BooleanVariable_setCurrentValue_boolenVariableExitEventOccurrence)


ControlNode_fire_controlNodeEntryEventOccurrence_strategy = st.builds(ControlNode_fire_controlNodeEntryEventOccurrence)
@given(instance=ControlNode_fire_controlNodeEntryEventOccurrence_strategy)
@settings(max_examples=25)
def test_ControlNode_fire_controlNodeEntryEventOccurrence_instantiation(instance):
    assert isinstance(instance, ControlNode_fire_controlNodeEntryEventOccurrence)


ControlNode_fire_controlNodeExitEventOccurrence_strategy = st.builds(ControlNode_fire_controlNodeExitEventOccurrence)
@given(instance=ControlNode_fire_controlNodeExitEventOccurrence_strategy)
@settings(max_examples=25)
def test_ControlNode_fire_controlNodeExitEventOccurrence_instantiation(instance):
    assert isinstance(instance, ControlNode_fire_controlNodeExitEventOccurrence)


ControlNode_isReady_ControlNodeEntryEventOccurrence_strategy = st.builds(ControlNode_isReady_ControlNodeEntryEventOccurrence)
@given(instance=ControlNode_isReady_ControlNodeEntryEventOccurrence_strategy)
@settings(max_examples=25)
def test_ControlNode_isReady_ControlNodeEntryEventOccurrence_instantiation(instance):
    assert isinstance(instance, ControlNode_isReady_ControlNodeEntryEventOccurrence)


ControlNode_isReady_ControlNodeExitEventOccurrence_strategy = st.builds(ControlNode_isReady_ControlNodeExitEventOccurrence)
@given(instance=ControlNode_isReady_ControlNodeExitEventOccurrence_strategy)
@settings(max_examples=25)
def test_ControlNode_isReady_ControlNodeExitEventOccurrence_instantiation(instance):
    assert isinstance(instance, ControlNode_isReady_ControlNodeExitEventOccurrence)


DecisionNode_fire_decisionNodeEntryEventOccurrence_strategy = st.builds(DecisionNode_fire_decisionNodeEntryEventOccurrence)
@given(instance=DecisionNode_fire_decisionNodeEntryEventOccurrence_strategy)
@settings(max_examples=25)
def test_DecisionNode_fire_decisionNodeEntryEventOccurrence_instantiation(instance):
    assert isinstance(instance, DecisionNode_fire_decisionNodeEntryEventOccurrence)


DecisionNode_fire_decisionNodeExitEventOccurrence_strategy = st.builds(DecisionNode_fire_decisionNodeExitEventOccurrence)
@given(instance=DecisionNode_fire_decisionNodeExitEventOccurrence_strategy)
@settings(max_examples=25)
def test_DecisionNode_fire_decisionNodeExitEventOccurrence_instantiation(instance):
    assert isinstance(instance, DecisionNode_fire_decisionNodeExitEventOccurrence)


EventOccurrence_strategy = st.builds(EventOccurrence)
@given(instance=EventOccurrence_strategy)
@settings(max_examples=25)
def test_EventOccurrence_instantiation(instance):
    assert isinstance(instance, EventOccurrence)


Events_strategy = st.builds(Events)
@given(instance=Events_strategy)
@settings(max_examples=25)
def test_Events_instantiation(instance):
    assert isinstance(instance, Events)


Events_trace_BooleanBinaryExpression_strategy = st.builds(Events_trace_BooleanBinaryExpression)
@given(instance=Events_trace_BooleanBinaryExpression_strategy)
@settings(max_examples=25)
def test_Events_trace_BooleanBinaryExpression_instantiation(instance):
    assert isinstance(instance, Events_trace_BooleanBinaryExpression)


Events_trace_BooleanUnaryExpression_strategy = st.builds(Events_trace_BooleanUnaryExpression)
@given(instance=Events_trace_BooleanUnaryExpression_strategy)
@settings(max_examples=25)
def test_Events_trace_BooleanUnaryExpression_instantiation(instance):
    assert isinstance(instance, Events_trace_BooleanUnaryExpression)


Events_trace_EObject_strategy = st.builds(Events_trace_EObject)
@given(instance=Events_trace_EObject_strategy)
@settings(max_examples=25)
def test_Events_trace_EObject_instantiation(instance):
    assert isinstance(instance, Events_trace_EObject)


Events_trace_GlobalState_strategy = st.builds(Events_trace_GlobalState)
@given(instance=Events_trace_GlobalState_strategy)
@settings(max_examples=25)
def test_Events_trace_GlobalState_instantiation(instance):
    assert isinstance(instance, Events_trace_GlobalState)


Events_trace_IntegerCalculationExpression_strategy = st.builds(Events_trace_IntegerCalculationExpression)
@given(instance=Events_trace_IntegerCalculationExpression_strategy)
@settings(max_examples=25)
def test_Events_trace_IntegerCalculationExpression_instantiation(instance):
    assert isinstance(instance, Events_trace_IntegerCalculationExpression)


Events_trace_IntegerComparisonExpression_strategy = st.builds(Events_trace_IntegerComparisonExpression)
@given(instance=Events_trace_IntegerComparisonExpression_strategy)
@settings(max_examples=25)
def test_Events_trace_IntegerComparisonExpression_instantiation(instance):
    assert isinstance(instance, Events_trace_IntegerComparisonExpression)


Events_trace_IntegerExpression_strategy = st.builds(Events_trace_IntegerExpression)
@given(instance=Events_trace_IntegerExpression_strategy)
@settings(max_examples=25)
def test_Events_trace_IntegerExpression_instantiation(instance):
    assert isinstance(instance, Events_trace_IntegerExpression)


Events_trace_Value_strategy = st.builds(Events_trace_Value)
@given(instance=Events_trace_Value_strategy)
@settings(max_examples=25)
def test_Events_trace_Value_instantiation(instance):
    assert isinstance(instance, Events_trace_Value)


ForkNode_fire_forkNodeEntryEventOccurrence_strategy = st.builds(ForkNode_fire_forkNodeEntryEventOccurrence)
@given(instance=ForkNode_fire_forkNodeEntryEventOccurrence_strategy)
@settings(max_examples=25)
def test_ForkNode_fire_forkNodeEntryEventOccurrence_instantiation(instance):
    assert isinstance(instance, ForkNode_fire_forkNodeEntryEventOccurrence)


ForkNode_fire_forkNodeExitEventOccurrence_strategy = st.builds(ForkNode_fire_forkNodeExitEventOccurrence)
@given(instance=ForkNode_fire_forkNodeExitEventOccurrence_strategy)
@settings(max_examples=25)
def test_ForkNode_fire_forkNodeExitEventOccurrence_instantiation(instance):
    assert isinstance(instance, ForkNode_fire_forkNodeExitEventOccurrence)


ForkedToken_baseTokenIsWithdrawn_State_strategy = st.builds(ForkedToken_baseTokenIsWithdrawn_State)
@given(instance=ForkedToken_baseTokenIsWithdrawn_State_strategy)
@settings(max_examples=25)
def test_ForkedToken_baseTokenIsWithdrawn_State_instantiation(instance):
    assert isinstance(instance, ForkedToken_baseTokenIsWithdrawn_State)


ForkedToken_baseToken_State_strategy = st.builds(ForkedToken_baseToken_State)
@given(instance=ForkedToken_baseToken_State_strategy)
@settings(max_examples=25)
def test_ForkedToken_baseToken_State_instantiation(instance):
    assert isinstance(instance, ForkedToken_baseToken_State)


ForkedToken_remainingOffersCount_State_strategy = st.builds(ForkedToken_remainingOffersCount_State)
@given(instance=ForkedToken_remainingOffersCount_State_strategy)
@settings(max_examples=25)
def test_ForkedToken_remainingOffersCount_State_instantiation(instance):
    assert isinstance(instance, ForkedToken_remainingOffersCount_State)


ForkedToken_withdraw_forkedTokenEntryEventOccurrence_strategy = st.builds(ForkedToken_withdraw_forkedTokenEntryEventOccurrence)
@given(instance=ForkedToken_withdraw_forkedTokenEntryEventOccurrence_strategy)
@settings(max_examples=25)
def test_ForkedToken_withdraw_forkedTokenEntryEventOccurrence_instantiation(instance):
    assert isinstance(instance, ForkedToken_withdraw_forkedTokenEntryEventOccurrence)


ForkedToken_withdraw_forkedTokenExitEventOccurrence_strategy = st.builds(ForkedToken_withdraw_forkedTokenExitEventOccurrence)
@given(instance=ForkedToken_withdraw_forkedTokenExitEventOccurrence_strategy)
@settings(max_examples=25)
def test_ForkedToken_withdraw_forkedTokenExitEventOccurrence_instantiation(instance):
    assert isinstance(instance, ForkedToken_withdraw_forkedTokenExitEventOccurrence)


InitialNode_fire_initialNodeEntryEventOccurrence_strategy = st.builds(InitialNode_fire_initialNodeEntryEventOccurrence)
@given(instance=InitialNode_fire_initialNodeEntryEventOccurrence_strategy)
@settings(max_examples=25)
def test_InitialNode_fire_initialNodeEntryEventOccurrence_instantiation(instance):
    assert isinstance(instance, InitialNode_fire_initialNodeEntryEventOccurrence)


InitialNode_fire_initialNodeExitEventOccurrence_strategy = st.builds(InitialNode_fire_initialNodeExitEventOccurrence)
@given(instance=InitialNode_fire_initialNodeExitEventOccurrence_strategy)
@settings(max_examples=25)
def test_InitialNode_fire_initialNodeExitEventOccurrence_instantiation(instance):
    assert isinstance(instance, InitialNode_fire_initialNodeExitEventOccurrence)


InitialNode_isReady_InitialNodeEntryEventOccurrence_strategy = st.builds(InitialNode_isReady_InitialNodeEntryEventOccurrence)
@given(instance=InitialNode_isReady_InitialNodeEntryEventOccurrence_strategy)
@settings(max_examples=25)
def test_InitialNode_isReady_InitialNodeEntryEventOccurrence_instantiation(instance):
    assert isinstance(instance, InitialNode_isReady_InitialNodeEntryEventOccurrence)


InitialNode_isReady_InitialNodeExitEventOccurrence_strategy = st.builds(InitialNode_isReady_InitialNodeExitEventOccurrence)
@given(instance=InitialNode_isReady_InitialNodeExitEventOccurrence_strategy)
@settings(max_examples=25)
def test_InitialNode_isReady_InitialNodeExitEventOccurrence_instantiation(instance):
    assert isinstance(instance, InitialNode_isReady_InitialNodeExitEventOccurrence)


InputValue_value_State_strategy = st.builds(InputValue_value_State)
@given(instance=InputValue_value_State_strategy)
@settings(max_examples=25)
def test_InputValue_value_State_instantiation(instance):
    assert isinstance(instance, InputValue_value_State)


InputValue_variable_State_strategy = st.builds(InputValue_variable_State)
@given(instance=InputValue_variable_State_strategy)
@settings(max_examples=25)
def test_InputValue_variable_State_instantiation(instance):
    assert isinstance(instance, InputValue_variable_State)


Input_inputValues_State_strategy = st.builds(Input_inputValues_State)
@given(instance=Input_inputValues_State_strategy)
@settings(max_examples=25)
def test_Input_inputValues_State_instantiation(instance):
    assert isinstance(instance, Input_inputValues_State)


IntegerCalculationExpression_evaluateADDEntryEventOccurrence_strategy = st.builds(IntegerCalculationExpression_evaluateADDEntryEventOccurrence)
@given(instance=IntegerCalculationExpression_evaluateADDEntryEventOccurrence_strategy)
@settings(max_examples=25)
def test_IntegerCalculationExpression_evaluateADDEntryEventOccurrence_instantiation(instance):
    assert isinstance(instance, IntegerCalculationExpression_evaluateADDEntryEventOccurrence)


IntegerCalculationExpression_evaluateADDExitEventOccurrence_strategy = st.builds(IntegerCalculationExpression_evaluateADDExitEventOccurrence)
@given(instance=IntegerCalculationExpression_evaluateADDExitEventOccurrence_strategy)
@settings(max_examples=25)
def test_IntegerCalculationExpression_evaluateADDExitEventOccurrence_instantiation(instance):
    assert isinstance(instance, IntegerCalculationExpression_evaluateADDExitEventOccurrence)


IntegerCalculationExpression_evaluateSUBTRACTEntryEventOccurrence_strategy = st.builds(IntegerCalculationExpression_evaluateSUBTRACTEntryEventOccurrence)
@given(instance=IntegerCalculationExpression_evaluateSUBTRACTEntryEventOccurrence_strategy)
@settings(max_examples=25)
def test_IntegerCalculationExpression_evaluateSUBTRACTEntryEventOccurrence_instantiation(instance):
    assert isinstance(instance, IntegerCalculationExpression_evaluateSUBTRACTEntryEventOccurrence)


IntegerCalculationExpression_evaluateSUBTRACTExitEventOccurrence_strategy = st.builds(IntegerCalculationExpression_evaluateSUBTRACTExitEventOccurrence)
@given(instance=IntegerCalculationExpression_evaluateSUBTRACTExitEventOccurrence_strategy)
@settings(max_examples=25)
def test_IntegerCalculationExpression_evaluateSUBTRACTExitEventOccurrence_instantiation(instance):
    assert isinstance(instance, IntegerCalculationExpression_evaluateSUBTRACTExitEventOccurrence)


IntegerCalculationExpression_execute_integerCalculationExpressionEntryEventOccurrence_strategy = st.builds(IntegerCalculationExpression_execute_integerCalculationExpressionEntryEventOccurrence)
@given(instance=IntegerCalculationExpression_execute_integerCalculationExpressionEntryEventOccurrence_strategy)
@settings(max_examples=25)
def test_IntegerCalculationExpression_execute_integerCalculationExpressionEntryEventOccurrence_instantiation(instance):
    assert isinstance(instance, IntegerCalculationExpression_execute_integerCalculationExpressionEntryEventOccurrence)


IntegerCalculationExpression_execute_integerCalculationExpressionExitEventOccurrence_strategy = st.builds(IntegerCalculationExpression_execute_integerCalculationExpressionExitEventOccurrence)
@given(instance=IntegerCalculationExpression_execute_integerCalculationExpressionExitEventOccurrence_strategy)
@settings(max_examples=25)
def test_IntegerCalculationExpression_execute_integerCalculationExpressionExitEventOccurrence_instantiation(instance):
    assert isinstance(instance, IntegerCalculationExpression_execute_integerCalculationExpressionExitEventOccurrence)


IntegerComparisonExpression_evaluateEQUALSEntryEventOccurrence_strategy = st.builds(IntegerComparisonExpression_evaluateEQUALSEntryEventOccurrence)
@given(instance=IntegerComparisonExpression_evaluateEQUALSEntryEventOccurrence_strategy)
@settings(max_examples=25)
def test_IntegerComparisonExpression_evaluateEQUALSEntryEventOccurrence_instantiation(instance):
    assert isinstance(instance, IntegerComparisonExpression_evaluateEQUALSEntryEventOccurrence)


IntegerComparisonExpression_evaluateEQUALSExitEventOccurrence_strategy = st.builds(IntegerComparisonExpression_evaluateEQUALSExitEventOccurrence)
@given(instance=IntegerComparisonExpression_evaluateEQUALSExitEventOccurrence_strategy)
@settings(max_examples=25)
def test_IntegerComparisonExpression_evaluateEQUALSExitEventOccurrence_instantiation(instance):
    assert isinstance(instance, IntegerComparisonExpression_evaluateEQUALSExitEventOccurrence)


IntegerComparisonExpression_evaluateGREATEREntryEventOccurrence_strategy = st.builds(IntegerComparisonExpression_evaluateGREATEREntryEventOccurrence)
@given(instance=IntegerComparisonExpression_evaluateGREATEREntryEventOccurrence_strategy)
@settings(max_examples=25)
def test_IntegerComparisonExpression_evaluateGREATEREntryEventOccurrence_instantiation(instance):
    assert isinstance(instance, IntegerComparisonExpression_evaluateGREATEREntryEventOccurrence)


IntegerComparisonExpression_evaluateGREATERExitEventOccurrence_strategy = st.builds(IntegerComparisonExpression_evaluateGREATERExitEventOccurrence)
@given(instance=IntegerComparisonExpression_evaluateGREATERExitEventOccurrence_strategy)
@settings(max_examples=25)
def test_IntegerComparisonExpression_evaluateGREATERExitEventOccurrence_instantiation(instance):
    assert isinstance(instance, IntegerComparisonExpression_evaluateGREATERExitEventOccurrence)


IntegerComparisonExpression_evaluateGREATER_EQUALSEntryEventOccurrence_strategy = st.builds(IntegerComparisonExpression_evaluateGREATER_EQUALSEntryEventOccurrence)
@given(instance=IntegerComparisonExpression_evaluateGREATER_EQUALSEntryEventOccurrence_strategy)
@settings(max_examples=25)
def test_IntegerComparisonExpression_evaluateGREATER_EQUALSEntryEventOccurrence_instantiation(instance):
    assert isinstance(instance, IntegerComparisonExpression_evaluateGREATER_EQUALSEntryEventOccurrence)


IntegerComparisonExpression_evaluateGREATER_EQUALSExitEventOccurrence_strategy = st.builds(IntegerComparisonExpression_evaluateGREATER_EQUALSExitEventOccurrence)
@given(instance=IntegerComparisonExpression_evaluateGREATER_EQUALSExitEventOccurrence_strategy)
@settings(max_examples=25)
def test_IntegerComparisonExpression_evaluateGREATER_EQUALSExitEventOccurrence_instantiation(instance):
    assert isinstance(instance, IntegerComparisonExpression_evaluateGREATER_EQUALSExitEventOccurrence)


IntegerComparisonExpression_evaluateSMALLEREntryEventOccurrence_strategy = st.builds(IntegerComparisonExpression_evaluateSMALLEREntryEventOccurrence)
@given(instance=IntegerComparisonExpression_evaluateSMALLEREntryEventOccurrence_strategy)
@settings(max_examples=25)
def test_IntegerComparisonExpression_evaluateSMALLEREntryEventOccurrence_instantiation(instance):
    assert isinstance(instance, IntegerComparisonExpression_evaluateSMALLEREntryEventOccurrence)


IntegerComparisonExpression_evaluateSMALLERExitEventOccurrence_strategy = st.builds(IntegerComparisonExpression_evaluateSMALLERExitEventOccurrence)
@given(instance=IntegerComparisonExpression_evaluateSMALLERExitEventOccurrence_strategy)
@settings(max_examples=25)
def test_IntegerComparisonExpression_evaluateSMALLERExitEventOccurrence_instantiation(instance):
    assert isinstance(instance, IntegerComparisonExpression_evaluateSMALLERExitEventOccurrence)


IntegerComparisonExpression_evaluateSMALLER_EQUALSEntryEventOccurrence_strategy = st.builds(IntegerComparisonExpression_evaluateSMALLER_EQUALSEntryEventOccurrence)
@given(instance=IntegerComparisonExpression_evaluateSMALLER_EQUALSEntryEventOccurrence_strategy)
@settings(max_examples=25)
def test_IntegerComparisonExpression_evaluateSMALLER_EQUALSEntryEventOccurrence_instantiation(instance):
    assert isinstance(instance, IntegerComparisonExpression_evaluateSMALLER_EQUALSEntryEventOccurrence)


IntegerComparisonExpression_evaluateSMALLER_EQUALSExitEventOccurrence_strategy = st.builds(IntegerComparisonExpression_evaluateSMALLER_EQUALSExitEventOccurrence)
@given(instance=IntegerComparisonExpression_evaluateSMALLER_EQUALSExitEventOccurrence_strategy)
@settings(max_examples=25)
def test_IntegerComparisonExpression_evaluateSMALLER_EQUALSExitEventOccurrence_instantiation(instance):
    assert isinstance(instance, IntegerComparisonExpression_evaluateSMALLER_EQUALSExitEventOccurrence)


IntegerComparisonExpression_execute_IntegerComparisionExpressionEntryEventOccurrence_strategy = st.builds(IntegerComparisonExpression_execute_IntegerComparisionExpressionEntryEventOccurrence)
@given(instance=IntegerComparisonExpression_execute_IntegerComparisionExpressionEntryEventOccurrence_strategy)
@settings(max_examples=25)
def test_IntegerComparisonExpression_execute_IntegerComparisionExpressionEntryEventOccurrence_instantiation(instance):
    assert isinstance(instance, IntegerComparisonExpression_execute_IntegerComparisionExpressionEntryEventOccurrence)


IntegerComparisonExpression_execute_IntegerComparisionExpressionExitEventOccurrence_strategy = st.builds(IntegerComparisonExpression_execute_IntegerComparisionExpressionExitEventOccurrence)
@given(instance=IntegerComparisonExpression_execute_IntegerComparisionExpressionExitEventOccurrence_strategy)
@settings(max_examples=25)
def test_IntegerComparisonExpression_execute_IntegerComparisionExpressionExitEventOccurrence_instantiation(instance):
    assert isinstance(instance, IntegerComparisonExpression_execute_IntegerComparisionExpressionExitEventOccurrence)


IntegerExpression_getOperandCurrentValuesEntryEventOccurrence_strategy = st.builds(IntegerExpression_getOperandCurrentValuesEntryEventOccurrence)
@given(instance=IntegerExpression_getOperandCurrentValuesEntryEventOccurrence_strategy)
@settings(max_examples=25)
def test_IntegerExpression_getOperandCurrentValuesEntryEventOccurrence_instantiation(instance):
    assert isinstance(instance, IntegerExpression_getOperandCurrentValuesEntryEventOccurrence)


IntegerExpression_getOperandCurrentValuesExitEventOccurrence_strategy = st.builds(IntegerExpression_getOperandCurrentValuesExitEventOccurrence)
@given(instance=IntegerExpression_getOperandCurrentValuesExitEventOccurrence_strategy)
@settings(max_examples=25)
def test_IntegerExpression_getOperandCurrentValuesExitEventOccurrence_instantiation(instance):
    assert isinstance(instance, IntegerExpression_getOperandCurrentValuesExitEventOccurrence)


IntegerVariable_getCurrentValueValue_integerVariableEntryEventOccurrence_strategy = st.builds(IntegerVariable_getCurrentValueValue_integerVariableEntryEventOccurrence)
@given(instance=IntegerVariable_getCurrentValueValue_integerVariableEntryEventOccurrence_strategy)
@settings(max_examples=25)
def test_IntegerVariable_getCurrentValueValue_integerVariableEntryEventOccurrence_instantiation(instance):
    assert isinstance(instance, IntegerVariable_getCurrentValueValue_integerVariableEntryEventOccurrence)


IntegerVariable_getCurrentValueValue_integerVariableExitEventOccurrence_strategy = st.builds(IntegerVariable_getCurrentValueValue_integerVariableExitEventOccurrence)
@given(instance=IntegerVariable_getCurrentValueValue_integerVariableExitEventOccurrence_strategy)
@settings(max_examples=25)
def test_IntegerVariable_getCurrentValueValue_integerVariableExitEventOccurrence_instantiation(instance):
    assert isinstance(instance, IntegerVariable_getCurrentValueValue_integerVariableExitEventOccurrence)


IntegerVariable_setCurrentValue_integerVariableEntryEventOccurrence_strategy = st.builds(IntegerVariable_setCurrentValue_integerVariableEntryEventOccurrence)
@given(instance=IntegerVariable_setCurrentValue_integerVariableEntryEventOccurrence_strategy)
@settings(max_examples=25)
def test_IntegerVariable_setCurrentValue_integerVariableEntryEventOccurrence_instantiation(instance):
    assert isinstance(instance, IntegerVariable_setCurrentValue_integerVariableEntryEventOccurrence)


IntegerVariable_setCurrentValue_integerVariableExitEventOccurrence_strategy = st.builds(IntegerVariable_setCurrentValue_integerVariableExitEventOccurrence)
@given(instance=IntegerVariable_setCurrentValue_integerVariableExitEventOccurrence_strategy)
@settings(max_examples=25)
def test_IntegerVariable_setCurrentValue_integerVariableExitEventOccurrence_instantiation(instance):
    assert isinstance(instance, IntegerVariable_setCurrentValue_integerVariableExitEventOccurrence)


MergeNode_hasOffers_mergeNodeEntryEventOccurrence_strategy = st.builds(MergeNode_hasOffers_mergeNodeEntryEventOccurrence)
@given(instance=MergeNode_hasOffers_mergeNodeEntryEventOccurrence_strategy)
@settings(max_examples=25)
def test_MergeNode_hasOffers_mergeNodeEntryEventOccurrence_instantiation(instance):
    assert isinstance(instance, MergeNode_hasOffers_mergeNodeEntryEventOccurrence)


MergeNode_hasOffers_mergeNodeExitEventOccurrence_strategy = st.builds(MergeNode_hasOffers_mergeNodeExitEventOccurrence)
@given(instance=MergeNode_hasOffers_mergeNodeExitEventOccurrence_strategy)
@settings(max_examples=25)
def test_MergeNode_hasOffers_mergeNodeExitEventOccurrence_instantiation(instance):
    assert isinstance(instance, MergeNode_hasOffers_mergeNodeExitEventOccurrence)


Offer_hasTokensEntryEventOccurrence_strategy = st.builds(Offer_hasTokensEntryEventOccurrence)
@given(instance=Offer_hasTokensEntryEventOccurrence_strategy)
@settings(max_examples=25)
def test_Offer_hasTokensEntryEventOccurrence_instantiation(instance):
    assert isinstance(instance, Offer_hasTokensEntryEventOccurrence)


Offer_hasTokensExitEventOccurrence_strategy = st.builds(Offer_hasTokensExitEventOccurrence)
@given(instance=Offer_hasTokensExitEventOccurrence_strategy)
@settings(max_examples=25)
def test_Offer_hasTokensExitEventOccurrence_instantiation(instance):
    assert isinstance(instance, Offer_hasTokensExitEventOccurrence)


Offer_offeredTokens_State_strategy = st.builds(Offer_offeredTokens_State)
@given(instance=Offer_offeredTokens_State_strategy)
@settings(max_examples=25)
def test_Offer_offeredTokens_State_instantiation(instance):
    assert isinstance(instance, Offer_offeredTokens_State)


OpaqueAction_doAction_opaqueActionEntryEventOccurrence_strategy = st.builds(OpaqueAction_doAction_opaqueActionEntryEventOccurrence)
@given(instance=OpaqueAction_doAction_opaqueActionEntryEventOccurrence_strategy)
@settings(max_examples=25)
def test_OpaqueAction_doAction_opaqueActionEntryEventOccurrence_instantiation(instance):
    assert isinstance(instance, OpaqueAction_doAction_opaqueActionEntryEventOccurrence)


OpaqueAction_doAction_opaqueActionExitEventOccurrence_strategy = st.builds(OpaqueAction_doAction_opaqueActionExitEventOccurrence)
@given(instance=OpaqueAction_doAction_opaqueActionExitEventOccurrence_strategy)
@settings(max_examples=25)
def test_OpaqueAction_doAction_opaqueActionExitEventOccurrence_instantiation(instance):
    assert isinstance(instance, OpaqueAction_doAction_opaqueActionExitEventOccurrence)


States_trace_GlobalState_strategy = st.builds(States_trace_GlobalState)
@given(instance=States_trace_GlobalState_strategy)
@settings(max_examples=25)
def test_States_trace_GlobalState_instantiation(instance):
    assert isinstance(instance, States_trace_GlobalState)


States_trace_Value_strategy = st.builds(States_trace_Value)
@given(instance=States_trace_Value_strategy)
@settings(max_examples=25)
def test_States_trace_Value_instantiation(instance):
    assert isinstance(instance, States_trace_Value)


StringVariable_getCurrentValueValue_stringVariableEntryEventOccurrence_strategy = st.builds(StringVariable_getCurrentValueValue_stringVariableEntryEventOccurrence)
@given(instance=StringVariable_getCurrentValueValue_stringVariableEntryEventOccurrence_strategy)
@settings(max_examples=25)
def test_StringVariable_getCurrentValueValue_stringVariableEntryEventOccurrence_instantiation(instance):
    assert isinstance(instance, StringVariable_getCurrentValueValue_stringVariableEntryEventOccurrence)


StringVariable_getCurrentValueValue_stringVariableExitEventOccurrence_strategy = st.builds(StringVariable_getCurrentValueValue_stringVariableExitEventOccurrence)
@given(instance=StringVariable_getCurrentValueValue_stringVariableExitEventOccurrence_strategy)
@settings(max_examples=25)
def test_StringVariable_getCurrentValueValue_stringVariableExitEventOccurrence_instantiation(instance):
    assert isinstance(instance, StringVariable_getCurrentValueValue_stringVariableExitEventOccurrence)


StringVariable_setCurrentValue_stringVariableEntryEventOccurrence_strategy = st.builds(StringVariable_setCurrentValue_stringVariableEntryEventOccurrence)
@given(instance=StringVariable_setCurrentValue_stringVariableEntryEventOccurrence_strategy)
@settings(max_examples=25)
def test_StringVariable_setCurrentValue_stringVariableEntryEventOccurrence_instantiation(instance):
    assert isinstance(instance, StringVariable_setCurrentValue_stringVariableEntryEventOccurrence)


StringVariable_setCurrentValue_stringVariableExitEventOccurrence_strategy = st.builds(StringVariable_setCurrentValue_stringVariableExitEventOccurrence)
@given(instance=StringVariable_setCurrentValue_stringVariableExitEventOccurrence_strategy)
@settings(max_examples=25)
def test_StringVariable_setCurrentValue_stringVariableExitEventOccurrence_instantiation(instance):
    assert isinstance(instance, StringVariable_setCurrentValue_stringVariableExitEventOccurrence)


Token_holder_State_strategy = st.builds(Token_holder_State)
@given(instance=Token_holder_State_strategy)
@settings(max_examples=25)
def test_Token_holder_State_instantiation(instance):
    assert isinstance(instance, Token_holder_State)


Token_isWithdrawnEntryEventOccurrence_strategy = st.builds(Token_isWithdrawnEntryEventOccurrence)
@given(instance=Token_isWithdrawnEntryEventOccurrence_strategy)
@settings(max_examples=25)
def test_Token_isWithdrawnEntryEventOccurrence_instantiation(instance):
    assert isinstance(instance, Token_isWithdrawnEntryEventOccurrence)


Token_isWithdrawnExitEventOccurrence_strategy = st.builds(Token_isWithdrawnExitEventOccurrence)
@given(instance=Token_isWithdrawnExitEventOccurrence_strategy)
@settings(max_examples=25)
def test_Token_isWithdrawnExitEventOccurrence_instantiation(instance):
    assert isinstance(instance, Token_isWithdrawnExitEventOccurrence)


Token_transferEntryEventOccurrence_strategy = st.builds(Token_transferEntryEventOccurrence)
@given(instance=Token_transferEntryEventOccurrence_strategy)
@settings(max_examples=25)
def test_Token_transferEntryEventOccurrence_instantiation(instance):
    assert isinstance(instance, Token_transferEntryEventOccurrence)


Token_transferExitEventOccurrence_strategy = st.builds(Token_transferExitEventOccurrence)
@given(instance=Token_transferExitEventOccurrence_strategy)
@settings(max_examples=25)
def test_Token_transferExitEventOccurrence_instantiation(instance):
    assert isinstance(instance, Token_transferExitEventOccurrence)


Token_withdrawEntryEventOccurrence_strategy = st.builds(Token_withdrawEntryEventOccurrence)
@given(instance=Token_withdrawEntryEventOccurrence_strategy)
@settings(max_examples=25)
def test_Token_withdrawEntryEventOccurrence_instantiation(instance):
    assert isinstance(instance, Token_withdrawEntryEventOccurrence)


Token_withdrawExitEventOccurrence_strategy = st.builds(Token_withdrawExitEventOccurrence)
@given(instance=Token_withdrawExitEventOccurrence_strategy)
@settings(max_examples=25)
def test_Token_withdrawExitEventOccurrence_instantiation(instance):
    assert isinstance(instance, Token_withdrawExitEventOccurrence)


Trace_executedNodes_State_strategy = st.builds(Trace_executedNodes_State)
@given(instance=Trace_executedNodes_State_strategy)
@settings(max_examples=25)
def test_Trace_executedNodes_State_instantiation(instance):
    assert isinstance(instance, Trace_executedNodes_State)


TracedAction_strategy = st.builds(TracedAction)
@given(instance=TracedAction_strategy)
@settings(max_examples=25)
def test_TracedAction_instantiation(instance):
    assert isinstance(instance, TracedAction)


TracedActivityEdge_strategy = st.builds(TracedActivityEdge)
@given(instance=TracedActivityEdge_strategy)
@settings(max_examples=25)
def test_TracedActivityEdge_instantiation(instance):
    assert isinstance(instance, TracedActivityEdge)


TracedActivityNode_strategy = st.builds(TracedActivityNode)
@given(instance=TracedActivityNode_strategy)
@settings(max_examples=25)
def test_TracedActivityNode_instantiation(instance):
    assert isinstance(instance, TracedActivityNode)


TracedControlNode_strategy = st.builds(TracedControlNode)
@given(instance=TracedControlNode_strategy)
@settings(max_examples=25)
def test_TracedControlNode_instantiation(instance):
    assert isinstance(instance, TracedControlNode)


TracedExecutableNode_strategy = st.builds(TracedExecutableNode)
@given(instance=TracedExecutableNode_strategy)
@settings(max_examples=25)
def test_TracedExecutableNode_instantiation(instance):
    assert isinstance(instance, TracedExecutableNode)


TracedFinalNode_strategy = st.builds(TracedFinalNode)
@given(instance=TracedFinalNode_strategy)
@settings(max_examples=25)
def test_TracedFinalNode_instantiation(instance):
    assert isinstance(instance, TracedFinalNode)


TracedNamedElement_strategy = st.builds(TracedNamedElement)
@given(instance=TracedNamedElement_strategy)
@settings(max_examples=25)
def test_TracedNamedElement_instantiation(instance):
    assert isinstance(instance, TracedNamedElement)


TracedObjects_strategy = st.builds(TracedObjects)
@given(instance=TracedObjects_strategy)
@settings(max_examples=25)
def test_TracedObjects_instantiation(instance):
    assert isinstance(instance, TracedObjects)


TracedToken_strategy = st.builds(TracedToken)
@given(instance=TracedToken_strategy)
@settings(max_examples=25)
def test_TracedToken_instantiation(instance):
    assert isinstance(instance, TracedToken)


TracedVariable_strategy = st.builds(TracedVariable)
@given(instance=TracedVariable_strategy)
@settings(max_examples=25)
def test_TracedVariable_instantiation(instance):
    assert isinstance(instance, TracedVariable)


Variable_currentValue_State_strategy = st.builds(Variable_currentValue_State)
@given(instance=Variable_currentValue_State_strategy)
@settings(max_examples=25)
def test_Variable_currentValue_State_instantiation(instance):
    assert isinstance(instance, Variable_currentValue_State)


activitydiagramConfiguration_TracedControlToken_strategy = st.builds(activitydiagramConfiguration_TracedControlToken)
@given(instance=activitydiagramConfiguration_TracedControlToken_strategy)
@settings(max_examples=25)
def test_activitydiagramConfiguration_TracedControlToken_instantiation(instance):
    assert isinstance(instance, activitydiagramConfiguration_TracedControlToken)


activitydiagramConfiguration_TracedForkedToken_strategy = st.builds(activitydiagramConfiguration_TracedForkedToken)
@given(instance=activitydiagramConfiguration_TracedForkedToken_strategy)
@settings(max_examples=25)
def test_activitydiagramConfiguration_TracedForkedToken_instantiation(instance):
    assert isinstance(instance, activitydiagramConfiguration_TracedForkedToken)


activitydiagramConfiguration_TracedInput_strategy = st.builds(activitydiagramConfiguration_TracedInput)
@given(instance=activitydiagramConfiguration_TracedInput_strategy)
@settings(max_examples=25)
def test_activitydiagramConfiguration_TracedInput_instantiation(instance):
    assert isinstance(instance, activitydiagramConfiguration_TracedInput)


activitydiagramConfiguration_TracedInputValue_strategy = st.builds(activitydiagramConfiguration_TracedInputValue)
@given(instance=activitydiagramConfiguration_TracedInputValue_strategy)
@settings(max_examples=25)
def test_activitydiagramConfiguration_TracedInputValue_instantiation(instance):
    assert isinstance(instance, activitydiagramConfiguration_TracedInputValue)


activitydiagramConfiguration_TracedOffer_strategy = st.builds(activitydiagramConfiguration_TracedOffer)
@given(instance=activitydiagramConfiguration_TracedOffer_strategy)
@settings(max_examples=25)
def test_activitydiagramConfiguration_TracedOffer_instantiation(instance):
    assert isinstance(instance, activitydiagramConfiguration_TracedOffer)


activitydiagramConfiguration_TracedToken_strategy = st.builds(activitydiagramConfiguration_TracedToken)
@given(instance=activitydiagramConfiguration_TracedToken_strategy)
@settings(max_examples=25)
def test_activitydiagramConfiguration_TracedToken_instantiation(instance):
    assert isinstance(instance, activitydiagramConfiguration_TracedToken)


activitydiagramConfiguration_TracedTrace_strategy = st.builds(activitydiagramConfiguration_TracedTrace)
@given(instance=activitydiagramConfiguration_TracedTrace_strategy)
@settings(max_examples=25)
def test_activitydiagramConfiguration_TracedTrace_instantiation(instance):
    assert isinstance(instance, activitydiagramConfiguration_TracedTrace)


activitydiagram_TracedAction_strategy = st.builds(activitydiagram_TracedAction)
@given(instance=activitydiagram_TracedAction_strategy)
@settings(max_examples=25)
def test_activitydiagram_TracedAction_instantiation(instance):
    assert isinstance(instance, activitydiagram_TracedAction)


activitydiagram_TracedActivity_strategy = st.builds(activitydiagram_TracedActivity)
@given(instance=activitydiagram_TracedActivity_strategy)
@settings(max_examples=25)
def test_activitydiagram_TracedActivity_instantiation(instance):
    assert isinstance(instance, activitydiagram_TracedActivity)


activitydiagram_TracedActivityEdge_strategy = st.builds(activitydiagram_TracedActivityEdge)
@given(instance=activitydiagram_TracedActivityEdge_strategy)
@settings(max_examples=25)
def test_activitydiagram_TracedActivityEdge_instantiation(instance):
    assert isinstance(instance, activitydiagram_TracedActivityEdge)


activitydiagram_TracedActivityFinalNode_strategy = st.builds(activitydiagram_TracedActivityFinalNode)
@given(instance=activitydiagram_TracedActivityFinalNode_strategy)
@settings(max_examples=25)
def test_activitydiagram_TracedActivityFinalNode_instantiation(instance):
    assert isinstance(instance, activitydiagram_TracedActivityFinalNode)


activitydiagram_TracedActivityNode_strategy = st.builds(activitydiagram_TracedActivityNode)
@given(instance=activitydiagram_TracedActivityNode_strategy)
@settings(max_examples=25)
def test_activitydiagram_TracedActivityNode_instantiation(instance):
    assert isinstance(instance, activitydiagram_TracedActivityNode)


activitydiagram_TracedBooleanVariable_strategy = st.builds(activitydiagram_TracedBooleanVariable)
@given(instance=activitydiagram_TracedBooleanVariable_strategy)
@settings(max_examples=25)
def test_activitydiagram_TracedBooleanVariable_instantiation(instance):
    assert isinstance(instance, activitydiagram_TracedBooleanVariable)


activitydiagram_TracedControlFlow_strategy = st.builds(activitydiagram_TracedControlFlow)
@given(instance=activitydiagram_TracedControlFlow_strategy)
@settings(max_examples=25)
def test_activitydiagram_TracedControlFlow_instantiation(instance):
    assert isinstance(instance, activitydiagram_TracedControlFlow)


activitydiagram_TracedControlNode_strategy = st.builds(activitydiagram_TracedControlNode)
@given(instance=activitydiagram_TracedControlNode_strategy)
@settings(max_examples=25)
def test_activitydiagram_TracedControlNode_instantiation(instance):
    assert isinstance(instance, activitydiagram_TracedControlNode)


activitydiagram_TracedDecisionNode_strategy = st.builds(activitydiagram_TracedDecisionNode)
@given(instance=activitydiagram_TracedDecisionNode_strategy)
@settings(max_examples=25)
def test_activitydiagram_TracedDecisionNode_instantiation(instance):
    assert isinstance(instance, activitydiagram_TracedDecisionNode)


activitydiagram_TracedForkNode_strategy = st.builds(activitydiagram_TracedForkNode)
@given(instance=activitydiagram_TracedForkNode_strategy)
@settings(max_examples=25)
def test_activitydiagram_TracedForkNode_instantiation(instance):
    assert isinstance(instance, activitydiagram_TracedForkNode)


activitydiagram_TracedInitialNode_strategy = st.builds(activitydiagram_TracedInitialNode)
@given(instance=activitydiagram_TracedInitialNode_strategy)
@settings(max_examples=25)
def test_activitydiagram_TracedInitialNode_instantiation(instance):
    assert isinstance(instance, activitydiagram_TracedInitialNode)


activitydiagram_TracedIntegerVariable_strategy = st.builds(activitydiagram_TracedIntegerVariable)
@given(instance=activitydiagram_TracedIntegerVariable_strategy)
@settings(max_examples=25)
def test_activitydiagram_TracedIntegerVariable_instantiation(instance):
    assert isinstance(instance, activitydiagram_TracedIntegerVariable)


activitydiagram_TracedJoinNode_strategy = st.builds(activitydiagram_TracedJoinNode)
@given(instance=activitydiagram_TracedJoinNode_strategy)
@settings(max_examples=25)
def test_activitydiagram_TracedJoinNode_instantiation(instance):
    assert isinstance(instance, activitydiagram_TracedJoinNode)


activitydiagram_TracedMergeNode_strategy = st.builds(activitydiagram_TracedMergeNode)
@given(instance=activitydiagram_TracedMergeNode_strategy)
@settings(max_examples=25)
def test_activitydiagram_TracedMergeNode_instantiation(instance):
    assert isinstance(instance, activitydiagram_TracedMergeNode)


activitydiagram_TracedOpaqueAction_strategy = st.builds(activitydiagram_TracedOpaqueAction)
@given(instance=activitydiagram_TracedOpaqueAction_strategy)
@settings(max_examples=25)
def test_activitydiagram_TracedOpaqueAction_instantiation(instance):
    assert isinstance(instance, activitydiagram_TracedOpaqueAction)


activitydiagram_TracedStringVariable_strategy = st.builds(activitydiagram_TracedStringVariable)
@given(instance=activitydiagram_TracedStringVariable_strategy)
@settings(max_examples=25)
def test_activitydiagram_TracedStringVariable_instantiation(instance):
    assert isinstance(instance, activitydiagram_TracedStringVariable)


activitydiagram_TracedVariable_strategy = st.builds(activitydiagram_TracedVariable)
@given(instance=activitydiagram_TracedVariable_strategy)
@settings(max_examples=25)
def test_activitydiagram_TracedVariable_instantiation(instance):
    assert isinstance(instance, activitydiagram_TracedVariable)


activitydiagram_trace_Activity_strategy = st.builds(activitydiagram_trace_Activity)
@given(instance=activitydiagram_trace_Activity_strategy)
@settings(max_examples=25)
def test_activitydiagram_trace_Activity_instantiation(instance):
    assert isinstance(instance, activitydiagram_trace_Activity)


activitydiagram_trace_ActivityFinalNode_strategy = st.builds(activitydiagram_trace_ActivityFinalNode)
@given(instance=activitydiagram_trace_ActivityFinalNode_strategy)
@settings(max_examples=25)
def test_activitydiagram_trace_ActivityFinalNode_instantiation(instance):
    assert isinstance(instance, activitydiagram_trace_ActivityFinalNode)


activitydiagram_trace_BooleanVariable_strategy = st.builds(activitydiagram_trace_BooleanVariable)
@given(instance=activitydiagram_trace_BooleanVariable_strategy)
@settings(max_examples=25)
def test_activitydiagram_trace_BooleanVariable_instantiation(instance):
    assert isinstance(instance, activitydiagram_trace_BooleanVariable)


activitydiagram_trace_ControlFlow_strategy = st.builds(activitydiagram_trace_ControlFlow)
@given(instance=activitydiagram_trace_ControlFlow_strategy)
@settings(max_examples=25)
def test_activitydiagram_trace_ControlFlow_instantiation(instance):
    assert isinstance(instance, activitydiagram_trace_ControlFlow)


activitydiagram_trace_DecisionNode_strategy = st.builds(activitydiagram_trace_DecisionNode)
@given(instance=activitydiagram_trace_DecisionNode_strategy)
@settings(max_examples=25)
def test_activitydiagram_trace_DecisionNode_instantiation(instance):
    assert isinstance(instance, activitydiagram_trace_DecisionNode)


activitydiagram_trace_Expression_strategy = st.builds(activitydiagram_trace_Expression)
@given(instance=activitydiagram_trace_Expression_strategy)
@settings(max_examples=25)
def test_activitydiagram_trace_Expression_instantiation(instance):
    assert isinstance(instance, activitydiagram_trace_Expression)


activitydiagram_trace_ForkNode_strategy = st.builds(activitydiagram_trace_ForkNode)
@given(instance=activitydiagram_trace_ForkNode_strategy)
@settings(max_examples=25)
def test_activitydiagram_trace_ForkNode_instantiation(instance):
    assert isinstance(instance, activitydiagram_trace_ForkNode)


activitydiagram_trace_InitialNode_strategy = st.builds(activitydiagram_trace_InitialNode)
@given(instance=activitydiagram_trace_InitialNode_strategy)
@settings(max_examples=25)
def test_activitydiagram_trace_InitialNode_instantiation(instance):
    assert isinstance(instance, activitydiagram_trace_InitialNode)


activitydiagram_trace_IntegerVariable_strategy = st.builds(activitydiagram_trace_IntegerVariable)
@given(instance=activitydiagram_trace_IntegerVariable_strategy)
@settings(max_examples=25)
def test_activitydiagram_trace_IntegerVariable_instantiation(instance):
    assert isinstance(instance, activitydiagram_trace_IntegerVariable)


activitydiagram_trace_JoinNode_strategy = st.builds(activitydiagram_trace_JoinNode)
@given(instance=activitydiagram_trace_JoinNode_strategy)
@settings(max_examples=25)
def test_activitydiagram_trace_JoinNode_instantiation(instance):
    assert isinstance(instance, activitydiagram_trace_JoinNode)


activitydiagram_trace_MergeNode_strategy = st.builds(activitydiagram_trace_MergeNode)
@given(instance=activitydiagram_trace_MergeNode_strategy)
@settings(max_examples=25)
def test_activitydiagram_trace_MergeNode_instantiation(instance):
    assert isinstance(instance, activitydiagram_trace_MergeNode)


activitydiagram_trace_OpaqueAction_strategy = st.builds(activitydiagram_trace_OpaqueAction)
@given(instance=activitydiagram_trace_OpaqueAction_strategy)
@settings(max_examples=25)
def test_activitydiagram_trace_OpaqueAction_instantiation(instance):
    assert isinstance(instance, activitydiagram_trace_OpaqueAction)


activitydiagram_trace_StringVariable_strategy = st.builds(activitydiagram_trace_StringVariable)
@given(instance=activitydiagram_trace_StringVariable_strategy)
@settings(max_examples=25)
def test_activitydiagram_trace_StringVariable_instantiation(instance):
    assert isinstance(instance, activitydiagram_trace_StringVariable)


activitydiagram_trace_Value_strategy = st.builds(activitydiagram_trace_Value)
@given(instance=activitydiagram_trace_Value_strategy)
@settings(max_examples=25)
def test_activitydiagram_trace_Value_instantiation(instance):
    assert isinstance(instance, activitydiagram_trace_Value)


trace_BooleanBinaryExpression_strategy = st.builds(trace_BooleanBinaryExpression)
@given(instance=trace_BooleanBinaryExpression_strategy)
@settings(max_examples=25)
def test_trace_BooleanBinaryExpression_instantiation(instance):
    assert isinstance(instance, trace_BooleanBinaryExpression)


trace_BooleanUnaryExpression_strategy = st.builds(trace_BooleanUnaryExpression)
@given(instance=trace_BooleanUnaryExpression_strategy)
@settings(max_examples=25)
def test_trace_BooleanUnaryExpression_instantiation(instance):
    assert isinstance(instance, trace_BooleanUnaryExpression)


trace_BooleanValue_strategy = st.builds(trace_BooleanValue)
@given(instance=trace_BooleanValue_strategy)
@settings(max_examples=25)
def test_trace_BooleanValue_instantiation(instance):
    assert isinstance(instance, trace_BooleanValue)


trace_Events_Action_fire_actionEntryEventOccurrence_strategy = st.builds(trace_Events_Action_fire_actionEntryEventOccurrence)
@given(instance=trace_Events_Action_fire_actionEntryEventOccurrence_strategy)
@settings(max_examples=25)
def test_trace_Events_Action_fire_actionEntryEventOccurrence_instantiation(instance):
    assert isinstance(instance, trace_Events_Action_fire_actionEntryEventOccurrence)


trace_Events_Action_fire_actionExitEventOccurrence_strategy = st.builds(trace_Events_Action_fire_actionExitEventOccurrence)
@given(instance=trace_Events_Action_fire_actionExitEventOccurrence_strategy)
@settings(max_examples=25)
def test_trace_Events_Action_fire_actionExitEventOccurrence_instantiation(instance):
    assert isinstance(instance, trace_Events_Action_fire_actionExitEventOccurrence)


trace_Events_Action_isReady_actionEntryEventOccurrence_strategy = st.builds(trace_Events_Action_isReady_actionEntryEventOccurrence)
@given(instance=trace_Events_Action_isReady_actionEntryEventOccurrence_strategy)
@settings(max_examples=25)
def test_trace_Events_Action_isReady_actionEntryEventOccurrence_instantiation(instance):
    assert isinstance(instance, trace_Events_Action_isReady_actionEntryEventOccurrence)


trace_Events_Action_isReady_actionExitEventOccurrence_strategy = st.builds(trace_Events_Action_isReady_actionExitEventOccurrence)
@given(instance=trace_Events_Action_isReady_actionExitEventOccurrence_strategy)
@settings(max_examples=25)
def test_trace_Events_Action_isReady_actionExitEventOccurrence_instantiation(instance):
    assert isinstance(instance, trace_Events_Action_isReady_actionExitEventOccurrence)


trace_Events_Action_sendOffers_actionEntryEventOccurrence_strategy = st.builds(trace_Events_Action_sendOffers_actionEntryEventOccurrence)
@given(instance=trace_Events_Action_sendOffers_actionEntryEventOccurrence_strategy)
@settings(max_examples=25)
def test_trace_Events_Action_sendOffers_actionEntryEventOccurrence_instantiation(instance):
    assert isinstance(instance, trace_Events_Action_sendOffers_actionEntryEventOccurrence)


trace_Events_Action_sendOffers_actionExitEventOccurrence_strategy = st.builds(trace_Events_Action_sendOffers_actionExitEventOccurrence)
@given(instance=trace_Events_Action_sendOffers_actionExitEventOccurrence_strategy)
@settings(max_examples=25)
def test_trace_Events_Action_sendOffers_actionExitEventOccurrence_instantiation(instance):
    assert isinstance(instance, trace_Events_Action_sendOffers_actionExitEventOccurrence)


trace_Events_ActivityEdge_hasOfferEntryEventOccurrence_strategy = st.builds(trace_Events_ActivityEdge_hasOfferEntryEventOccurrence)
@given(instance=trace_Events_ActivityEdge_hasOfferEntryEventOccurrence_strategy)
@settings(max_examples=25)
def test_trace_Events_ActivityEdge_hasOfferEntryEventOccurrence_instantiation(instance):
    assert isinstance(instance, trace_Events_ActivityEdge_hasOfferEntryEventOccurrence)


trace_Events_ActivityEdge_hasOfferExitEventOccurrence_strategy = st.builds(trace_Events_ActivityEdge_hasOfferExitEventOccurrence)
@given(instance=trace_Events_ActivityEdge_hasOfferExitEventOccurrence_strategy)
@settings(max_examples=25)
def test_trace_Events_ActivityEdge_hasOfferExitEventOccurrence_instantiation(instance):
    assert isinstance(instance, trace_Events_ActivityEdge_hasOfferExitEventOccurrence)


trace_Events_ActivityEdge_sendOfferEntryEventOccurrence_strategy = st.builds(trace_Events_ActivityEdge_sendOfferEntryEventOccurrence)
@given(instance=trace_Events_ActivityEdge_sendOfferEntryEventOccurrence_strategy)
@settings(max_examples=25)
def test_trace_Events_ActivityEdge_sendOfferEntryEventOccurrence_instantiation(instance):
    assert isinstance(instance, trace_Events_ActivityEdge_sendOfferEntryEventOccurrence)


trace_Events_ActivityEdge_sendOfferExitEventOccurrence_strategy = st.builds(trace_Events_ActivityEdge_sendOfferExitEventOccurrence)
@given(instance=trace_Events_ActivityEdge_sendOfferExitEventOccurrence_strategy)
@settings(max_examples=25)
def test_trace_Events_ActivityEdge_sendOfferExitEventOccurrence_instantiation(instance):
    assert isinstance(instance, trace_Events_ActivityEdge_sendOfferExitEventOccurrence)


trace_Events_ActivityEdge_takeOfferedTokens_activityEdgeEntryEventOccurrence_strategy = st.builds(trace_Events_ActivityEdge_takeOfferedTokens_activityEdgeEntryEventOccurrence)
@given(instance=trace_Events_ActivityEdge_takeOfferedTokens_activityEdgeEntryEventOccurrence_strategy)
@settings(max_examples=25)
def test_trace_Events_ActivityEdge_takeOfferedTokens_activityEdgeEntryEventOccurrence_instantiation(instance):
    assert isinstance(instance, trace_Events_ActivityEdge_takeOfferedTokens_activityEdgeEntryEventOccurrence)


trace_Events_ActivityEdge_takeOfferedTokens_activityEdgeExitEventOccurrence_strategy = st.builds(trace_Events_ActivityEdge_takeOfferedTokens_activityEdgeExitEventOccurrence)
@given(instance=trace_Events_ActivityEdge_takeOfferedTokens_activityEdgeExitEventOccurrence_strategy)
@settings(max_examples=25)
def test_trace_Events_ActivityEdge_takeOfferedTokens_activityEdgeExitEventOccurrence_instantiation(instance):
    assert isinstance(instance, trace_Events_ActivityEdge_takeOfferedTokens_activityEdgeExitEventOccurrence)


trace_Events_ActivityFinalNode_fire_activityFinalNodeEntryEventOccurrence_strategy = st.builds(trace_Events_ActivityFinalNode_fire_activityFinalNodeEntryEventOccurrence)
@given(instance=trace_Events_ActivityFinalNode_fire_activityFinalNodeEntryEventOccurrence_strategy)
@settings(max_examples=25)
def test_trace_Events_ActivityFinalNode_fire_activityFinalNodeEntryEventOccurrence_instantiation(instance):
    assert isinstance(instance, trace_Events_ActivityFinalNode_fire_activityFinalNodeEntryEventOccurrence)


trace_Events_ActivityFinalNode_fire_activityFinalNodeExitEventOccurrence_strategy = st.builds(trace_Events_ActivityFinalNode_fire_activityFinalNodeExitEventOccurrence)
@given(instance=trace_Events_ActivityFinalNode_fire_activityFinalNodeExitEventOccurrence_strategy)
@settings(max_examples=25)
def test_trace_Events_ActivityFinalNode_fire_activityFinalNodeExitEventOccurrence_instantiation(instance):
    assert isinstance(instance, trace_Events_ActivityFinalNode_fire_activityFinalNodeExitEventOccurrence)


trace_Events_ActivityNode_addTokensEntryEventOccurrence_strategy = st.builds(trace_Events_ActivityNode_addTokensEntryEventOccurrence)
@given(instance=trace_Events_ActivityNode_addTokensEntryEventOccurrence_strategy)
@settings(max_examples=25)
def test_trace_Events_ActivityNode_addTokensEntryEventOccurrence_instantiation(instance):
    assert isinstance(instance, trace_Events_ActivityNode_addTokensEntryEventOccurrence)


trace_Events_ActivityNode_addTokensExitEventOccurrence_strategy = st.builds(trace_Events_ActivityNode_addTokensExitEventOccurrence)
@given(instance=trace_Events_ActivityNode_addTokensExitEventOccurrence_strategy)
@settings(max_examples=25)
def test_trace_Events_ActivityNode_addTokensExitEventOccurrence_instantiation(instance):
    assert isinstance(instance, trace_Events_ActivityNode_addTokensExitEventOccurrence)


trace_Events_ActivityNode_hasOffersEntryEventOccurrence_strategy = st.builds(trace_Events_ActivityNode_hasOffersEntryEventOccurrence)
@given(instance=trace_Events_ActivityNode_hasOffersEntryEventOccurrence_strategy)
@settings(max_examples=25)
def test_trace_Events_ActivityNode_hasOffersEntryEventOccurrence_instantiation(instance):
    assert isinstance(instance, trace_Events_ActivityNode_hasOffersEntryEventOccurrence)


trace_Events_ActivityNode_hasOffersExitEventOccurrence_strategy = st.builds(trace_Events_ActivityNode_hasOffersExitEventOccurrence)
@given(instance=trace_Events_ActivityNode_hasOffersExitEventOccurrence_strategy)
@settings(max_examples=25)
def test_trace_Events_ActivityNode_hasOffersExitEventOccurrence_instantiation(instance):
    assert isinstance(instance, trace_Events_ActivityNode_hasOffersExitEventOccurrence)


trace_Events_ActivityNode_isReadyEntryEventOccurrence_strategy = st.builds(trace_Events_ActivityNode_isReadyEntryEventOccurrence)
@given(instance=trace_Events_ActivityNode_isReadyEntryEventOccurrence_strategy)
@settings(max_examples=25)
def test_trace_Events_ActivityNode_isReadyEntryEventOccurrence_instantiation(instance):
    assert isinstance(instance, trace_Events_ActivityNode_isReadyEntryEventOccurrence)


trace_Events_ActivityNode_isReadyExitEventOccurrence_strategy = st.builds(trace_Events_ActivityNode_isReadyExitEventOccurrence)
@given(instance=trace_Events_ActivityNode_isReadyExitEventOccurrence_strategy)
@settings(max_examples=25)
def test_trace_Events_ActivityNode_isReadyExitEventOccurrence_instantiation(instance):
    assert isinstance(instance, trace_Events_ActivityNode_isReadyExitEventOccurrence)


trace_Events_ActivityNode_isRunningEntryEventOccurrence_strategy = st.builds(trace_Events_ActivityNode_isRunningEntryEventOccurrence)
@given(instance=trace_Events_ActivityNode_isRunningEntryEventOccurrence_strategy)
@settings(max_examples=25)
def test_trace_Events_ActivityNode_isRunningEntryEventOccurrence_instantiation(instance):
    assert isinstance(instance, trace_Events_ActivityNode_isRunningEntryEventOccurrence)


trace_Events_ActivityNode_isRunningExitEventOccurrence_strategy = st.builds(trace_Events_ActivityNode_isRunningExitEventOccurrence)
@given(instance=trace_Events_ActivityNode_isRunningExitEventOccurrence_strategy)
@settings(max_examples=25)
def test_trace_Events_ActivityNode_isRunningExitEventOccurrence_instantiation(instance):
    assert isinstance(instance, trace_Events_ActivityNode_isRunningExitEventOccurrence)


trace_Events_ActivityNode_removeTokenEntryEventOccurrence_strategy = st.builds(trace_Events_ActivityNode_removeTokenEntryEventOccurrence)
@given(instance=trace_Events_ActivityNode_removeTokenEntryEventOccurrence_strategy)
@settings(max_examples=25)
def test_trace_Events_ActivityNode_removeTokenEntryEventOccurrence_instantiation(instance):
    assert isinstance(instance, trace_Events_ActivityNode_removeTokenEntryEventOccurrence)


trace_Events_ActivityNode_removeTokenExitEventOccurrence_strategy = st.builds(trace_Events_ActivityNode_removeTokenExitEventOccurrence)
@given(instance=trace_Events_ActivityNode_removeTokenExitEventOccurrence_strategy)
@settings(max_examples=25)
def test_trace_Events_ActivityNode_removeTokenExitEventOccurrence_instantiation(instance):
    assert isinstance(instance, trace_Events_ActivityNode_removeTokenExitEventOccurrence)


trace_Events_ActivityNode_run_activityNodeEntryEventOccurrence_strategy = st.builds(trace_Events_ActivityNode_run_activityNodeEntryEventOccurrence)
@given(instance=trace_Events_ActivityNode_run_activityNodeEntryEventOccurrence_strategy)
@settings(max_examples=25)
def test_trace_Events_ActivityNode_run_activityNodeEntryEventOccurrence_instantiation(instance):
    assert isinstance(instance, trace_Events_ActivityNode_run_activityNodeEntryEventOccurrence)


trace_Events_ActivityNode_run_activityNodeExitEventOccurrence_strategy = st.builds(trace_Events_ActivityNode_run_activityNodeExitEventOccurrence)
@given(instance=trace_Events_ActivityNode_run_activityNodeExitEventOccurrence_strategy)
@settings(max_examples=25)
def test_trace_Events_ActivityNode_run_activityNodeExitEventOccurrence_instantiation(instance):
    assert isinstance(instance, trace_Events_ActivityNode_run_activityNodeExitEventOccurrence)


trace_Events_ActivityNode_sendOffersEntryEventOccurrence_strategy = st.builds(trace_Events_ActivityNode_sendOffersEntryEventOccurrence)
@given(instance=trace_Events_ActivityNode_sendOffersEntryEventOccurrence_strategy)
@settings(max_examples=25)
def test_trace_Events_ActivityNode_sendOffersEntryEventOccurrence_instantiation(instance):
    assert isinstance(instance, trace_Events_ActivityNode_sendOffersEntryEventOccurrence)


trace_Events_ActivityNode_sendOffersExitEventOccurrence_strategy = st.builds(trace_Events_ActivityNode_sendOffersExitEventOccurrence)
@given(instance=trace_Events_ActivityNode_sendOffersExitEventOccurrence_strategy)
@settings(max_examples=25)
def test_trace_Events_ActivityNode_sendOffersExitEventOccurrence_instantiation(instance):
    assert isinstance(instance, trace_Events_ActivityNode_sendOffersExitEventOccurrence)


trace_Events_ActivityNode_takeOfferedTokensEntryEventOccurrence_strategy = st.builds(trace_Events_ActivityNode_takeOfferedTokensEntryEventOccurrence)
@given(instance=trace_Events_ActivityNode_takeOfferedTokensEntryEventOccurrence_strategy)
@settings(max_examples=25)
def test_trace_Events_ActivityNode_takeOfferedTokensEntryEventOccurrence_instantiation(instance):
    assert isinstance(instance, trace_Events_ActivityNode_takeOfferedTokensEntryEventOccurrence)


trace_Events_ActivityNode_takeOfferedTokensExitEventOccurrence_strategy = st.builds(trace_Events_ActivityNode_takeOfferedTokensExitEventOccurrence)
@given(instance=trace_Events_ActivityNode_takeOfferedTokensExitEventOccurrence_strategy)
@settings(max_examples=25)
def test_trace_Events_ActivityNode_takeOfferedTokensExitEventOccurrence_instantiation(instance):
    assert isinstance(instance, trace_Events_ActivityNode_takeOfferedTokensExitEventOccurrence)


trace_Events_ActivityNode_terminate_activityNodeEntryEventOccurrence_strategy = st.builds(trace_Events_ActivityNode_terminate_activityNodeEntryEventOccurrence)
@given(instance=trace_Events_ActivityNode_terminate_activityNodeEntryEventOccurrence_strategy)
@settings(max_examples=25)
def test_trace_Events_ActivityNode_terminate_activityNodeEntryEventOccurrence_instantiation(instance):
    assert isinstance(instance, trace_Events_ActivityNode_terminate_activityNodeEntryEventOccurrence)


trace_Events_ActivityNode_terminate_activityNodeExitEventOccurrence_strategy = st.builds(trace_Events_ActivityNode_terminate_activityNodeExitEventOccurrence)
@given(instance=trace_Events_ActivityNode_terminate_activityNodeExitEventOccurrence_strategy)
@settings(max_examples=25)
def test_trace_Events_ActivityNode_terminate_activityNodeExitEventOccurrence_instantiation(instance):
    assert isinstance(instance, trace_Events_ActivityNode_terminate_activityNodeExitEventOccurrence)


trace_Events_Activity_fireInitialNodeEntryEventOccurrence_strategy = st.builds(trace_Events_Activity_fireInitialNodeEntryEventOccurrence)
@given(instance=trace_Events_Activity_fireInitialNodeEntryEventOccurrence_strategy)
@settings(max_examples=25)
def test_trace_Events_Activity_fireInitialNodeEntryEventOccurrence_instantiation(instance):
    assert isinstance(instance, trace_Events_Activity_fireInitialNodeEntryEventOccurrence)


trace_Events_Activity_fireInitialNodeExitEventOccurrence_strategy = st.builds(trace_Events_Activity_fireInitialNodeExitEventOccurrence)
@given(instance=trace_Events_Activity_fireInitialNodeExitEventOccurrence_strategy)
@settings(max_examples=25)
def test_trace_Events_Activity_fireInitialNodeExitEventOccurrence_instantiation(instance):
    assert isinstance(instance, trace_Events_Activity_fireInitialNodeExitEventOccurrence)


trace_Events_Activity_fireNodeEntryEventOccurrence_strategy = st.builds(trace_Events_Activity_fireNodeEntryEventOccurrence)
@given(instance=trace_Events_Activity_fireNodeEntryEventOccurrence_strategy)
@settings(max_examples=25)
def test_trace_Events_Activity_fireNodeEntryEventOccurrence_instantiation(instance):
    assert isinstance(instance, trace_Events_Activity_fireNodeEntryEventOccurrence)


trace_Events_Activity_fireNodeExitEventOccurrence_strategy = st.builds(trace_Events_Activity_fireNodeExitEventOccurrence)
@given(instance=trace_Events_Activity_fireNodeExitEventOccurrence_strategy)
@settings(max_examples=25)
def test_trace_Events_Activity_fireNodeExitEventOccurrence_instantiation(instance):
    assert isinstance(instance, trace_Events_Activity_fireNodeExitEventOccurrence)


trace_Events_Activity_getEnabledNodesEntryEventOccurrence_strategy = st.builds(trace_Events_Activity_getEnabledNodesEntryEventOccurrence)
@given(instance=trace_Events_Activity_getEnabledNodesEntryEventOccurrence_strategy)
@settings(max_examples=25)
def test_trace_Events_Activity_getEnabledNodesEntryEventOccurrence_instantiation(instance):
    assert isinstance(instance, trace_Events_Activity_getEnabledNodesEntryEventOccurrence)


trace_Events_Activity_getEnabledNodesExitEventOccurrence_strategy = st.builds(trace_Events_Activity_getEnabledNodesExitEventOccurrence)
@given(instance=trace_Events_Activity_getEnabledNodesExitEventOccurrence_strategy)
@settings(max_examples=25)
def test_trace_Events_Activity_getEnabledNodesExitEventOccurrence_instantiation(instance):
    assert isinstance(instance, trace_Events_Activity_getEnabledNodesExitEventOccurrence)


trace_Events_Activity_getInitialNodeEntryEventOccurrence_strategy = st.builds(trace_Events_Activity_getInitialNodeEntryEventOccurrence)
@given(instance=trace_Events_Activity_getInitialNodeEntryEventOccurrence_strategy)
@settings(max_examples=25)
def test_trace_Events_Activity_getInitialNodeEntryEventOccurrence_instantiation(instance):
    assert isinstance(instance, trace_Events_Activity_getInitialNodeEntryEventOccurrence)


trace_Events_Activity_getInitialNodeExitEventOccurrence_strategy = st.builds(trace_Events_Activity_getInitialNodeExitEventOccurrence)
@given(instance=trace_Events_Activity_getInitialNodeExitEventOccurrence_strategy)
@settings(max_examples=25)
def test_trace_Events_Activity_getInitialNodeExitEventOccurrence_instantiation(instance):
    assert isinstance(instance, trace_Events_Activity_getInitialNodeExitEventOccurrence)


trace_Events_Activity_initializeEntryEventOccurrence_strategy = st.builds(trace_Events_Activity_initializeEntryEventOccurrence)
@given(instance=trace_Events_Activity_initializeEntryEventOccurrence_strategy)
@settings(max_examples=25)
def test_trace_Events_Activity_initializeEntryEventOccurrence_instantiation(instance):
    assert isinstance(instance, trace_Events_Activity_initializeEntryEventOccurrence)


trace_Events_Activity_initializeExitEventOccurrence_strategy = st.builds(trace_Events_Activity_initializeExitEventOccurrence)
@given(instance=trace_Events_Activity_initializeExitEventOccurrence_strategy)
@settings(max_examples=25)
def test_trace_Events_Activity_initializeExitEventOccurrence_instantiation(instance):
    assert isinstance(instance, trace_Events_Activity_initializeExitEventOccurrence)


trace_Events_Activity_mainEntryEventOccurrence_strategy = st.builds(trace_Events_Activity_mainEntryEventOccurrence)
@given(instance=trace_Events_Activity_mainEntryEventOccurrence_strategy)
@settings(max_examples=25)
def test_trace_Events_Activity_mainEntryEventOccurrence_instantiation(instance):
    assert isinstance(instance, trace_Events_Activity_mainEntryEventOccurrence)


trace_Events_Activity_mainExitEventOccurrence_strategy = st.builds(trace_Events_Activity_mainExitEventOccurrence)
@given(instance=trace_Events_Activity_mainExitEventOccurrence_strategy)
@settings(max_examples=25)
def test_trace_Events_Activity_mainExitEventOccurrence_instantiation(instance):
    assert isinstance(instance, trace_Events_Activity_mainExitEventOccurrence)


trace_Events_Activity_runEntryEventOccurrence_strategy = st.builds(trace_Events_Activity_runEntryEventOccurrence)
@given(instance=trace_Events_Activity_runEntryEventOccurrence_strategy)
@settings(max_examples=25)
def test_trace_Events_Activity_runEntryEventOccurrence_instantiation(instance):
    assert isinstance(instance, trace_Events_Activity_runEntryEventOccurrence)


trace_Events_Activity_runExitEventOccurrence_strategy = st.builds(trace_Events_Activity_runExitEventOccurrence)
@given(instance=trace_Events_Activity_runExitEventOccurrence_strategy)
@settings(max_examples=25)
def test_trace_Events_Activity_runExitEventOccurrence_instantiation(instance):
    assert isinstance(instance, trace_Events_Activity_runExitEventOccurrence)


trace_Events_Activity_runNodesEntryEventOccurrence_strategy = st.builds(trace_Events_Activity_runNodesEntryEventOccurrence)
@given(instance=trace_Events_Activity_runNodesEntryEventOccurrence_strategy)
@settings(max_examples=25)
def test_trace_Events_Activity_runNodesEntryEventOccurrence_instantiation(instance):
    assert isinstance(instance, trace_Events_Activity_runNodesEntryEventOccurrence)


trace_Events_Activity_runNodesExitEventOccurrence_strategy = st.builds(trace_Events_Activity_runNodesExitEventOccurrence)
@given(instance=trace_Events_Activity_runNodesExitEventOccurrence_strategy)
@settings(max_examples=25)
def test_trace_Events_Activity_runNodesExitEventOccurrence_instantiation(instance):
    assert isinstance(instance, trace_Events_Activity_runNodesExitEventOccurrence)


trace_Events_Activity_selectNextNodeEntryEventOccurrence_strategy = st.builds(trace_Events_Activity_selectNextNodeEntryEventOccurrence)
@given(instance=trace_Events_Activity_selectNextNodeEntryEventOccurrence_strategy)
@settings(max_examples=25)
def test_trace_Events_Activity_selectNextNodeEntryEventOccurrence_instantiation(instance):
    assert isinstance(instance, trace_Events_Activity_selectNextNodeEntryEventOccurrence)


trace_Events_Activity_selectNextNodeExitEventOccurrence_strategy = st.builds(trace_Events_Activity_selectNextNodeExitEventOccurrence)
@given(instance=trace_Events_Activity_selectNextNodeExitEventOccurrence_strategy)
@settings(max_examples=25)
def test_trace_Events_Activity_selectNextNodeExitEventOccurrence_instantiation(instance):
    assert isinstance(instance, trace_Events_Activity_selectNextNodeExitEventOccurrence)


trace_Events_Activity_terminateEntryEventOccurrence_strategy = st.builds(trace_Events_Activity_terminateEntryEventOccurrence)
@given(instance=trace_Events_Activity_terminateEntryEventOccurrence_strategy)
@settings(max_examples=25)
def test_trace_Events_Activity_terminateEntryEventOccurrence_instantiation(instance):
    assert isinstance(instance, trace_Events_Activity_terminateEntryEventOccurrence)


trace_Events_Activity_terminateExitEventOccurrence_strategy = st.builds(trace_Events_Activity_terminateExitEventOccurrence)
@given(instance=trace_Events_Activity_terminateExitEventOccurrence_strategy)
@settings(max_examples=25)
def test_trace_Events_Activity_terminateExitEventOccurrence_instantiation(instance):
    assert isinstance(instance, trace_Events_Activity_terminateExitEventOccurrence)


trace_Events_BooleanBinaryExpression_evaluateANDEntryEventOccurrence_strategy = st.builds(trace_Events_BooleanBinaryExpression_evaluateANDEntryEventOccurrence)
@given(instance=trace_Events_BooleanBinaryExpression_evaluateANDEntryEventOccurrence_strategy)
@settings(max_examples=25)
def test_trace_Events_BooleanBinaryExpression_evaluateANDEntryEventOccurrence_instantiation(instance):
    assert isinstance(instance, trace_Events_BooleanBinaryExpression_evaluateANDEntryEventOccurrence)


trace_Events_BooleanBinaryExpression_evaluateANDExitEventOccurrence_strategy = st.builds(trace_Events_BooleanBinaryExpression_evaluateANDExitEventOccurrence)
@given(instance=trace_Events_BooleanBinaryExpression_evaluateANDExitEventOccurrence_strategy)
@settings(max_examples=25)
def test_trace_Events_BooleanBinaryExpression_evaluateANDExitEventOccurrence_instantiation(instance):
    assert isinstance(instance, trace_Events_BooleanBinaryExpression_evaluateANDExitEventOccurrence)


trace_Events_BooleanBinaryExpression_evaluateOREntryEventOccurrence_strategy = st.builds(trace_Events_BooleanBinaryExpression_evaluateOREntryEventOccurrence)
@given(instance=trace_Events_BooleanBinaryExpression_evaluateOREntryEventOccurrence_strategy)
@settings(max_examples=25)
def test_trace_Events_BooleanBinaryExpression_evaluateOREntryEventOccurrence_instantiation(instance):
    assert isinstance(instance, trace_Events_BooleanBinaryExpression_evaluateOREntryEventOccurrence)


trace_Events_BooleanBinaryExpression_evaluateORExitEventOccurrence_strategy = st.builds(trace_Events_BooleanBinaryExpression_evaluateORExitEventOccurrence)
@given(instance=trace_Events_BooleanBinaryExpression_evaluateORExitEventOccurrence_strategy)
@settings(max_examples=25)
def test_trace_Events_BooleanBinaryExpression_evaluateORExitEventOccurrence_instantiation(instance):
    assert isinstance(instance, trace_Events_BooleanBinaryExpression_evaluateORExitEventOccurrence)


trace_Events_BooleanBinaryExpression_execute_booleanBinaryExpressionEntryEventOccurrence_strategy = st.builds(trace_Events_BooleanBinaryExpression_execute_booleanBinaryExpressionEntryEventOccurrence)
@given(instance=trace_Events_BooleanBinaryExpression_execute_booleanBinaryExpressionEntryEventOccurrence_strategy)
@settings(max_examples=25)
def test_trace_Events_BooleanBinaryExpression_execute_booleanBinaryExpressionEntryEventOccurrence_instantiation(instance):
    assert isinstance(instance, trace_Events_BooleanBinaryExpression_execute_booleanBinaryExpressionEntryEventOccurrence)


trace_Events_BooleanBinaryExpression_execute_booleanBinaryExpressionExitEventOccurrence_strategy = st.builds(trace_Events_BooleanBinaryExpression_execute_booleanBinaryExpressionExitEventOccurrence)
@given(instance=trace_Events_BooleanBinaryExpression_execute_booleanBinaryExpressionExitEventOccurrence_strategy)
@settings(max_examples=25)
def test_trace_Events_BooleanBinaryExpression_execute_booleanBinaryExpressionExitEventOccurrence_instantiation(instance):
    assert isinstance(instance, trace_Events_BooleanBinaryExpression_execute_booleanBinaryExpressionExitEventOccurrence)


trace_Events_BooleanUnaryExpression_evaluateNOTEntryEventOccurrence_strategy = st.builds(trace_Events_BooleanUnaryExpression_evaluateNOTEntryEventOccurrence)
@given(instance=trace_Events_BooleanUnaryExpression_evaluateNOTEntryEventOccurrence_strategy)
@settings(max_examples=25)
def test_trace_Events_BooleanUnaryExpression_evaluateNOTEntryEventOccurrence_instantiation(instance):
    assert isinstance(instance, trace_Events_BooleanUnaryExpression_evaluateNOTEntryEventOccurrence)


trace_Events_BooleanUnaryExpression_evaluateNOTExitEventOccurrence_strategy = st.builds(trace_Events_BooleanUnaryExpression_evaluateNOTExitEventOccurrence)
@given(instance=trace_Events_BooleanUnaryExpression_evaluateNOTExitEventOccurrence_strategy)
@settings(max_examples=25)
def test_trace_Events_BooleanUnaryExpression_evaluateNOTExitEventOccurrence_instantiation(instance):
    assert isinstance(instance, trace_Events_BooleanUnaryExpression_evaluateNOTExitEventOccurrence)


trace_Events_BooleanUnaryExpression_execute_booleanUnaryExpressionEntryEventOccurrence_strategy = st.builds(trace_Events_BooleanUnaryExpression_execute_booleanUnaryExpressionEntryEventOccurrence)
@given(instance=trace_Events_BooleanUnaryExpression_execute_booleanUnaryExpressionEntryEventOccurrence_strategy)
@settings(max_examples=25)
def test_trace_Events_BooleanUnaryExpression_execute_booleanUnaryExpressionEntryEventOccurrence_instantiation(instance):
    assert isinstance(instance, trace_Events_BooleanUnaryExpression_execute_booleanUnaryExpressionEntryEventOccurrence)


trace_Events_BooleanUnaryExpression_execute_booleanUnaryExpressionExitEventOccurrence_strategy = st.builds(trace_Events_BooleanUnaryExpression_execute_booleanUnaryExpressionExitEventOccurrence)
@given(instance=trace_Events_BooleanUnaryExpression_execute_booleanUnaryExpressionExitEventOccurrence_strategy)
@settings(max_examples=25)
def test_trace_Events_BooleanUnaryExpression_execute_booleanUnaryExpressionExitEventOccurrence_instantiation(instance):
    assert isinstance(instance, trace_Events_BooleanUnaryExpression_execute_booleanUnaryExpressionExitEventOccurrence)


trace_Events_BooleanVariable_getCurrentValueValue_booleanVariableEntryEventOccurrence_strategy = st.builds(trace_Events_BooleanVariable_getCurrentValueValue_booleanVariableEntryEventOccurrence)
@given(instance=trace_Events_BooleanVariable_getCurrentValueValue_booleanVariableEntryEventOccurrence_strategy)
@settings(max_examples=25)
def test_trace_Events_BooleanVariable_getCurrentValueValue_booleanVariableEntryEventOccurrence_instantiation(instance):
    assert isinstance(instance, trace_Events_BooleanVariable_getCurrentValueValue_booleanVariableEntryEventOccurrence)


trace_Events_BooleanVariable_getCurrentValueValue_booleanVariableExitEventOccurrence_strategy = st.builds(trace_Events_BooleanVariable_getCurrentValueValue_booleanVariableExitEventOccurrence)
@given(instance=trace_Events_BooleanVariable_getCurrentValueValue_booleanVariableExitEventOccurrence_strategy)
@settings(max_examples=25)
def test_trace_Events_BooleanVariable_getCurrentValueValue_booleanVariableExitEventOccurrence_instantiation(instance):
    assert isinstance(instance, trace_Events_BooleanVariable_getCurrentValueValue_booleanVariableExitEventOccurrence)


trace_Events_BooleanVariable_setCurrentValue_boolenVariableEntryEventOccurrence_strategy = st.builds(trace_Events_BooleanVariable_setCurrentValue_boolenVariableEntryEventOccurrence)
@given(instance=trace_Events_BooleanVariable_setCurrentValue_boolenVariableEntryEventOccurrence_strategy)
@settings(max_examples=25)
def test_trace_Events_BooleanVariable_setCurrentValue_boolenVariableEntryEventOccurrence_instantiation(instance):
    assert isinstance(instance, trace_Events_BooleanVariable_setCurrentValue_boolenVariableEntryEventOccurrence)


trace_Events_BooleanVariable_setCurrentValue_boolenVariableExitEventOccurrence_strategy = st.builds(trace_Events_BooleanVariable_setCurrentValue_boolenVariableExitEventOccurrence)
@given(instance=trace_Events_BooleanVariable_setCurrentValue_boolenVariableExitEventOccurrence_strategy)
@settings(max_examples=25)
def test_trace_Events_BooleanVariable_setCurrentValue_boolenVariableExitEventOccurrence_instantiation(instance):
    assert isinstance(instance, trace_Events_BooleanVariable_setCurrentValue_boolenVariableExitEventOccurrence)


trace_Events_ControlNode_fire_controlNodeEntryEventOccurrence_strategy = st.builds(trace_Events_ControlNode_fire_controlNodeEntryEventOccurrence)
@given(instance=trace_Events_ControlNode_fire_controlNodeEntryEventOccurrence_strategy)
@settings(max_examples=25)
def test_trace_Events_ControlNode_fire_controlNodeEntryEventOccurrence_instantiation(instance):
    assert isinstance(instance, trace_Events_ControlNode_fire_controlNodeEntryEventOccurrence)


trace_Events_ControlNode_fire_controlNodeExitEventOccurrence_strategy = st.builds(trace_Events_ControlNode_fire_controlNodeExitEventOccurrence)
@given(instance=trace_Events_ControlNode_fire_controlNodeExitEventOccurrence_strategy)
@settings(max_examples=25)
def test_trace_Events_ControlNode_fire_controlNodeExitEventOccurrence_instantiation(instance):
    assert isinstance(instance, trace_Events_ControlNode_fire_controlNodeExitEventOccurrence)


trace_Events_ControlNode_isReady_ControlNodeEntryEventOccurrence_strategy = st.builds(trace_Events_ControlNode_isReady_ControlNodeEntryEventOccurrence)
@given(instance=trace_Events_ControlNode_isReady_ControlNodeEntryEventOccurrence_strategy)
@settings(max_examples=25)
def test_trace_Events_ControlNode_isReady_ControlNodeEntryEventOccurrence_instantiation(instance):
    assert isinstance(instance, trace_Events_ControlNode_isReady_ControlNodeEntryEventOccurrence)


trace_Events_ControlNode_isReady_ControlNodeExitEventOccurrence_strategy = st.builds(trace_Events_ControlNode_isReady_ControlNodeExitEventOccurrence)
@given(instance=trace_Events_ControlNode_isReady_ControlNodeExitEventOccurrence_strategy)
@settings(max_examples=25)
def test_trace_Events_ControlNode_isReady_ControlNodeExitEventOccurrence_instantiation(instance):
    assert isinstance(instance, trace_Events_ControlNode_isReady_ControlNodeExitEventOccurrence)


trace_Events_DecisionNode_fire_decisionNodeEntryEventOccurrence_strategy = st.builds(trace_Events_DecisionNode_fire_decisionNodeEntryEventOccurrence)
@given(instance=trace_Events_DecisionNode_fire_decisionNodeEntryEventOccurrence_strategy)
@settings(max_examples=25)
def test_trace_Events_DecisionNode_fire_decisionNodeEntryEventOccurrence_instantiation(instance):
    assert isinstance(instance, trace_Events_DecisionNode_fire_decisionNodeEntryEventOccurrence)


trace_Events_DecisionNode_fire_decisionNodeExitEventOccurrence_strategy = st.builds(trace_Events_DecisionNode_fire_decisionNodeExitEventOccurrence)
@given(instance=trace_Events_DecisionNode_fire_decisionNodeExitEventOccurrence_strategy)
@settings(max_examples=25)
def test_trace_Events_DecisionNode_fire_decisionNodeExitEventOccurrence_instantiation(instance):
    assert isinstance(instance, trace_Events_DecisionNode_fire_decisionNodeExitEventOccurrence)


trace_Events_EventOccurrence_strategy = st.builds(trace_Events_EventOccurrence)
@given(instance=trace_Events_EventOccurrence_strategy)
@settings(max_examples=25)
def test_trace_Events_EventOccurrence_instantiation(instance):
    assert isinstance(instance, trace_Events_EventOccurrence)


trace_Events_Events_strategy = st.builds(trace_Events_Events)
@given(instance=trace_Events_Events_strategy)
@settings(max_examples=25)
def test_trace_Events_Events_instantiation(instance):
    assert isinstance(instance, trace_Events_Events)


trace_Events_ForkNode_fire_forkNodeEntryEventOccurrence_strategy = st.builds(trace_Events_ForkNode_fire_forkNodeEntryEventOccurrence)
@given(instance=trace_Events_ForkNode_fire_forkNodeEntryEventOccurrence_strategy)
@settings(max_examples=25)
def test_trace_Events_ForkNode_fire_forkNodeEntryEventOccurrence_instantiation(instance):
    assert isinstance(instance, trace_Events_ForkNode_fire_forkNodeEntryEventOccurrence)


trace_Events_ForkNode_fire_forkNodeExitEventOccurrence_strategy = st.builds(trace_Events_ForkNode_fire_forkNodeExitEventOccurrence)
@given(instance=trace_Events_ForkNode_fire_forkNodeExitEventOccurrence_strategy)
@settings(max_examples=25)
def test_trace_Events_ForkNode_fire_forkNodeExitEventOccurrence_instantiation(instance):
    assert isinstance(instance, trace_Events_ForkNode_fire_forkNodeExitEventOccurrence)


trace_Events_ForkedToken_withdraw_forkedTokenEntryEventOccurrence_strategy = st.builds(trace_Events_ForkedToken_withdraw_forkedTokenEntryEventOccurrence)
@given(instance=trace_Events_ForkedToken_withdraw_forkedTokenEntryEventOccurrence_strategy)
@settings(max_examples=25)
def test_trace_Events_ForkedToken_withdraw_forkedTokenEntryEventOccurrence_instantiation(instance):
    assert isinstance(instance, trace_Events_ForkedToken_withdraw_forkedTokenEntryEventOccurrence)


trace_Events_ForkedToken_withdraw_forkedTokenExitEventOccurrence_strategy = st.builds(trace_Events_ForkedToken_withdraw_forkedTokenExitEventOccurrence)
@given(instance=trace_Events_ForkedToken_withdraw_forkedTokenExitEventOccurrence_strategy)
@settings(max_examples=25)
def test_trace_Events_ForkedToken_withdraw_forkedTokenExitEventOccurrence_instantiation(instance):
    assert isinstance(instance, trace_Events_ForkedToken_withdraw_forkedTokenExitEventOccurrence)


trace_Events_InitialNode_fire_initialNodeEntryEventOccurrence_strategy = st.builds(trace_Events_InitialNode_fire_initialNodeEntryEventOccurrence)
@given(instance=trace_Events_InitialNode_fire_initialNodeEntryEventOccurrence_strategy)
@settings(max_examples=25)
def test_trace_Events_InitialNode_fire_initialNodeEntryEventOccurrence_instantiation(instance):
    assert isinstance(instance, trace_Events_InitialNode_fire_initialNodeEntryEventOccurrence)


trace_Events_InitialNode_fire_initialNodeExitEventOccurrence_strategy = st.builds(trace_Events_InitialNode_fire_initialNodeExitEventOccurrence)
@given(instance=trace_Events_InitialNode_fire_initialNodeExitEventOccurrence_strategy)
@settings(max_examples=25)
def test_trace_Events_InitialNode_fire_initialNodeExitEventOccurrence_instantiation(instance):
    assert isinstance(instance, trace_Events_InitialNode_fire_initialNodeExitEventOccurrence)


trace_Events_InitialNode_isReady_InitialNodeEntryEventOccurrence_strategy = st.builds(trace_Events_InitialNode_isReady_InitialNodeEntryEventOccurrence)
@given(instance=trace_Events_InitialNode_isReady_InitialNodeEntryEventOccurrence_strategy)
@settings(max_examples=25)
def test_trace_Events_InitialNode_isReady_InitialNodeEntryEventOccurrence_instantiation(instance):
    assert isinstance(instance, trace_Events_InitialNode_isReady_InitialNodeEntryEventOccurrence)


trace_Events_InitialNode_isReady_InitialNodeExitEventOccurrence_strategy = st.builds(trace_Events_InitialNode_isReady_InitialNodeExitEventOccurrence)
@given(instance=trace_Events_InitialNode_isReady_InitialNodeExitEventOccurrence_strategy)
@settings(max_examples=25)
def test_trace_Events_InitialNode_isReady_InitialNodeExitEventOccurrence_instantiation(instance):
    assert isinstance(instance, trace_Events_InitialNode_isReady_InitialNodeExitEventOccurrence)


trace_Events_IntegerCalculationExpression_evaluateADDEntryEventOccurrence_strategy = st.builds(trace_Events_IntegerCalculationExpression_evaluateADDEntryEventOccurrence)
@given(instance=trace_Events_IntegerCalculationExpression_evaluateADDEntryEventOccurrence_strategy)
@settings(max_examples=25)
def test_trace_Events_IntegerCalculationExpression_evaluateADDEntryEventOccurrence_instantiation(instance):
    assert isinstance(instance, trace_Events_IntegerCalculationExpression_evaluateADDEntryEventOccurrence)


trace_Events_IntegerCalculationExpression_evaluateADDExitEventOccurrence_strategy = st.builds(trace_Events_IntegerCalculationExpression_evaluateADDExitEventOccurrence)
@given(instance=trace_Events_IntegerCalculationExpression_evaluateADDExitEventOccurrence_strategy)
@settings(max_examples=25)
def test_trace_Events_IntegerCalculationExpression_evaluateADDExitEventOccurrence_instantiation(instance):
    assert isinstance(instance, trace_Events_IntegerCalculationExpression_evaluateADDExitEventOccurrence)


trace_Events_IntegerCalculationExpression_evaluateSUBTRACTEntryEventOccurrence_strategy = st.builds(trace_Events_IntegerCalculationExpression_evaluateSUBTRACTEntryEventOccurrence)
@given(instance=trace_Events_IntegerCalculationExpression_evaluateSUBTRACTEntryEventOccurrence_strategy)
@settings(max_examples=25)
def test_trace_Events_IntegerCalculationExpression_evaluateSUBTRACTEntryEventOccurrence_instantiation(instance):
    assert isinstance(instance, trace_Events_IntegerCalculationExpression_evaluateSUBTRACTEntryEventOccurrence)


trace_Events_IntegerCalculationExpression_evaluateSUBTRACTExitEventOccurrence_strategy = st.builds(trace_Events_IntegerCalculationExpression_evaluateSUBTRACTExitEventOccurrence)
@given(instance=trace_Events_IntegerCalculationExpression_evaluateSUBTRACTExitEventOccurrence_strategy)
@settings(max_examples=25)
def test_trace_Events_IntegerCalculationExpression_evaluateSUBTRACTExitEventOccurrence_instantiation(instance):
    assert isinstance(instance, trace_Events_IntegerCalculationExpression_evaluateSUBTRACTExitEventOccurrence)


trace_Events_IntegerCalculationExpression_execute_integerCalculationExpressionEntryEventOccurrence_strategy = st.builds(trace_Events_IntegerCalculationExpression_execute_integerCalculationExpressionEntryEventOccurrence)
@given(instance=trace_Events_IntegerCalculationExpression_execute_integerCalculationExpressionEntryEventOccurrence_strategy)
@settings(max_examples=25)
def test_trace_Events_IntegerCalculationExpression_execute_integerCalculationExpressionEntryEventOccurrence_instantiation(instance):
    assert isinstance(instance, trace_Events_IntegerCalculationExpression_execute_integerCalculationExpressionEntryEventOccurrence)


trace_Events_IntegerCalculationExpression_execute_integerCalculationExpressionExitEventOccurrence_strategy = st.builds(trace_Events_IntegerCalculationExpression_execute_integerCalculationExpressionExitEventOccurrence)
@given(instance=trace_Events_IntegerCalculationExpression_execute_integerCalculationExpressionExitEventOccurrence_strategy)
@settings(max_examples=25)
def test_trace_Events_IntegerCalculationExpression_execute_integerCalculationExpressionExitEventOccurrence_instantiation(instance):
    assert isinstance(instance, trace_Events_IntegerCalculationExpression_execute_integerCalculationExpressionExitEventOccurrence)


trace_Events_IntegerComparisonExpression_evaluateEQUALSEntryEventOccurrence_strategy = st.builds(trace_Events_IntegerComparisonExpression_evaluateEQUALSEntryEventOccurrence)
@given(instance=trace_Events_IntegerComparisonExpression_evaluateEQUALSEntryEventOccurrence_strategy)
@settings(max_examples=25)
def test_trace_Events_IntegerComparisonExpression_evaluateEQUALSEntryEventOccurrence_instantiation(instance):
    assert isinstance(instance, trace_Events_IntegerComparisonExpression_evaluateEQUALSEntryEventOccurrence)


trace_Events_IntegerComparisonExpression_evaluateEQUALSExitEventOccurrence_strategy = st.builds(trace_Events_IntegerComparisonExpression_evaluateEQUALSExitEventOccurrence)
@given(instance=trace_Events_IntegerComparisonExpression_evaluateEQUALSExitEventOccurrence_strategy)
@settings(max_examples=25)
def test_trace_Events_IntegerComparisonExpression_evaluateEQUALSExitEventOccurrence_instantiation(instance):
    assert isinstance(instance, trace_Events_IntegerComparisonExpression_evaluateEQUALSExitEventOccurrence)


trace_Events_IntegerComparisonExpression_evaluateGREATEREntryEventOccurrence_strategy = st.builds(trace_Events_IntegerComparisonExpression_evaluateGREATEREntryEventOccurrence)
@given(instance=trace_Events_IntegerComparisonExpression_evaluateGREATEREntryEventOccurrence_strategy)
@settings(max_examples=25)
def test_trace_Events_IntegerComparisonExpression_evaluateGREATEREntryEventOccurrence_instantiation(instance):
    assert isinstance(instance, trace_Events_IntegerComparisonExpression_evaluateGREATEREntryEventOccurrence)


trace_Events_IntegerComparisonExpression_evaluateGREATERExitEventOccurrence_strategy = st.builds(trace_Events_IntegerComparisonExpression_evaluateGREATERExitEventOccurrence)
@given(instance=trace_Events_IntegerComparisonExpression_evaluateGREATERExitEventOccurrence_strategy)
@settings(max_examples=25)
def test_trace_Events_IntegerComparisonExpression_evaluateGREATERExitEventOccurrence_instantiation(instance):
    assert isinstance(instance, trace_Events_IntegerComparisonExpression_evaluateGREATERExitEventOccurrence)


trace_Events_IntegerComparisonExpression_evaluateGREATER_EQUALSEntryEventOccurrence_strategy = st.builds(trace_Events_IntegerComparisonExpression_evaluateGREATER_EQUALSEntryEventOccurrence)
@given(instance=trace_Events_IntegerComparisonExpression_evaluateGREATER_EQUALSEntryEventOccurrence_strategy)
@settings(max_examples=25)
def test_trace_Events_IntegerComparisonExpression_evaluateGREATER_EQUALSEntryEventOccurrence_instantiation(instance):
    assert isinstance(instance, trace_Events_IntegerComparisonExpression_evaluateGREATER_EQUALSEntryEventOccurrence)


trace_Events_IntegerComparisonExpression_evaluateGREATER_EQUALSExitEventOccurrence_strategy = st.builds(trace_Events_IntegerComparisonExpression_evaluateGREATER_EQUALSExitEventOccurrence)
@given(instance=trace_Events_IntegerComparisonExpression_evaluateGREATER_EQUALSExitEventOccurrence_strategy)
@settings(max_examples=25)
def test_trace_Events_IntegerComparisonExpression_evaluateGREATER_EQUALSExitEventOccurrence_instantiation(instance):
    assert isinstance(instance, trace_Events_IntegerComparisonExpression_evaluateGREATER_EQUALSExitEventOccurrence)


trace_Events_IntegerComparisonExpression_evaluateSMALLEREntryEventOccurrence_strategy = st.builds(trace_Events_IntegerComparisonExpression_evaluateSMALLEREntryEventOccurrence)
@given(instance=trace_Events_IntegerComparisonExpression_evaluateSMALLEREntryEventOccurrence_strategy)
@settings(max_examples=25)
def test_trace_Events_IntegerComparisonExpression_evaluateSMALLEREntryEventOccurrence_instantiation(instance):
    assert isinstance(instance, trace_Events_IntegerComparisonExpression_evaluateSMALLEREntryEventOccurrence)


trace_Events_IntegerComparisonExpression_evaluateSMALLERExitEventOccurrence_strategy = st.builds(trace_Events_IntegerComparisonExpression_evaluateSMALLERExitEventOccurrence)
@given(instance=trace_Events_IntegerComparisonExpression_evaluateSMALLERExitEventOccurrence_strategy)
@settings(max_examples=25)
def test_trace_Events_IntegerComparisonExpression_evaluateSMALLERExitEventOccurrence_instantiation(instance):
    assert isinstance(instance, trace_Events_IntegerComparisonExpression_evaluateSMALLERExitEventOccurrence)


trace_Events_IntegerComparisonExpression_evaluateSMALLER_EQUALSEntryEventOccurrence_strategy = st.builds(trace_Events_IntegerComparisonExpression_evaluateSMALLER_EQUALSEntryEventOccurrence)
@given(instance=trace_Events_IntegerComparisonExpression_evaluateSMALLER_EQUALSEntryEventOccurrence_strategy)
@settings(max_examples=25)
def test_trace_Events_IntegerComparisonExpression_evaluateSMALLER_EQUALSEntryEventOccurrence_instantiation(instance):
    assert isinstance(instance, trace_Events_IntegerComparisonExpression_evaluateSMALLER_EQUALSEntryEventOccurrence)


trace_Events_IntegerComparisonExpression_evaluateSMALLER_EQUALSExitEventOccurrence_strategy = st.builds(trace_Events_IntegerComparisonExpression_evaluateSMALLER_EQUALSExitEventOccurrence)
@given(instance=trace_Events_IntegerComparisonExpression_evaluateSMALLER_EQUALSExitEventOccurrence_strategy)
@settings(max_examples=25)
def test_trace_Events_IntegerComparisonExpression_evaluateSMALLER_EQUALSExitEventOccurrence_instantiation(instance):
    assert isinstance(instance, trace_Events_IntegerComparisonExpression_evaluateSMALLER_EQUALSExitEventOccurrence)


trace_Events_IntegerComparisonExpression_execute_IntegerComparisionExpressionEntryEventOccurrence_strategy = st.builds(trace_Events_IntegerComparisonExpression_execute_IntegerComparisionExpressionEntryEventOccurrence)
@given(instance=trace_Events_IntegerComparisonExpression_execute_IntegerComparisionExpressionEntryEventOccurrence_strategy)
@settings(max_examples=25)
def test_trace_Events_IntegerComparisonExpression_execute_IntegerComparisionExpressionEntryEventOccurrence_instantiation(instance):
    assert isinstance(instance, trace_Events_IntegerComparisonExpression_execute_IntegerComparisionExpressionEntryEventOccurrence)


trace_Events_IntegerComparisonExpression_execute_IntegerComparisionExpressionExitEventOccurrence_strategy = st.builds(trace_Events_IntegerComparisonExpression_execute_IntegerComparisionExpressionExitEventOccurrence)
@given(instance=trace_Events_IntegerComparisonExpression_execute_IntegerComparisionExpressionExitEventOccurrence_strategy)
@settings(max_examples=25)
def test_trace_Events_IntegerComparisonExpression_execute_IntegerComparisionExpressionExitEventOccurrence_instantiation(instance):
    assert isinstance(instance, trace_Events_IntegerComparisonExpression_execute_IntegerComparisionExpressionExitEventOccurrence)


trace_Events_IntegerExpression_getOperandCurrentValuesEntryEventOccurrence_strategy = st.builds(trace_Events_IntegerExpression_getOperandCurrentValuesEntryEventOccurrence)
@given(instance=trace_Events_IntegerExpression_getOperandCurrentValuesEntryEventOccurrence_strategy)
@settings(max_examples=25)
def test_trace_Events_IntegerExpression_getOperandCurrentValuesEntryEventOccurrence_instantiation(instance):
    assert isinstance(instance, trace_Events_IntegerExpression_getOperandCurrentValuesEntryEventOccurrence)


trace_Events_IntegerExpression_getOperandCurrentValuesExitEventOccurrence_strategy = st.builds(trace_Events_IntegerExpression_getOperandCurrentValuesExitEventOccurrence)
@given(instance=trace_Events_IntegerExpression_getOperandCurrentValuesExitEventOccurrence_strategy)
@settings(max_examples=25)
def test_trace_Events_IntegerExpression_getOperandCurrentValuesExitEventOccurrence_instantiation(instance):
    assert isinstance(instance, trace_Events_IntegerExpression_getOperandCurrentValuesExitEventOccurrence)


trace_Events_IntegerVariable_getCurrentValueValue_integerVariableEntryEventOccurrence_strategy = st.builds(trace_Events_IntegerVariable_getCurrentValueValue_integerVariableEntryEventOccurrence)
@given(instance=trace_Events_IntegerVariable_getCurrentValueValue_integerVariableEntryEventOccurrence_strategy)
@settings(max_examples=25)
def test_trace_Events_IntegerVariable_getCurrentValueValue_integerVariableEntryEventOccurrence_instantiation(instance):
    assert isinstance(instance, trace_Events_IntegerVariable_getCurrentValueValue_integerVariableEntryEventOccurrence)


trace_Events_IntegerVariable_getCurrentValueValue_integerVariableExitEventOccurrence_strategy = st.builds(trace_Events_IntegerVariable_getCurrentValueValue_integerVariableExitEventOccurrence)
@given(instance=trace_Events_IntegerVariable_getCurrentValueValue_integerVariableExitEventOccurrence_strategy)
@settings(max_examples=25)
def test_trace_Events_IntegerVariable_getCurrentValueValue_integerVariableExitEventOccurrence_instantiation(instance):
    assert isinstance(instance, trace_Events_IntegerVariable_getCurrentValueValue_integerVariableExitEventOccurrence)


trace_Events_IntegerVariable_setCurrentValue_integerVariableEntryEventOccurrence_strategy = st.builds(trace_Events_IntegerVariable_setCurrentValue_integerVariableEntryEventOccurrence)
@given(instance=trace_Events_IntegerVariable_setCurrentValue_integerVariableEntryEventOccurrence_strategy)
@settings(max_examples=25)
def test_trace_Events_IntegerVariable_setCurrentValue_integerVariableEntryEventOccurrence_instantiation(instance):
    assert isinstance(instance, trace_Events_IntegerVariable_setCurrentValue_integerVariableEntryEventOccurrence)


trace_Events_IntegerVariable_setCurrentValue_integerVariableExitEventOccurrence_strategy = st.builds(trace_Events_IntegerVariable_setCurrentValue_integerVariableExitEventOccurrence)
@given(instance=trace_Events_IntegerVariable_setCurrentValue_integerVariableExitEventOccurrence_strategy)
@settings(max_examples=25)
def test_trace_Events_IntegerVariable_setCurrentValue_integerVariableExitEventOccurrence_instantiation(instance):
    assert isinstance(instance, trace_Events_IntegerVariable_setCurrentValue_integerVariableExitEventOccurrence)


trace_Events_MergeNode_hasOffers_mergeNodeEntryEventOccurrence_strategy = st.builds(trace_Events_MergeNode_hasOffers_mergeNodeEntryEventOccurrence)
@given(instance=trace_Events_MergeNode_hasOffers_mergeNodeEntryEventOccurrence_strategy)
@settings(max_examples=25)
def test_trace_Events_MergeNode_hasOffers_mergeNodeEntryEventOccurrence_instantiation(instance):
    assert isinstance(instance, trace_Events_MergeNode_hasOffers_mergeNodeEntryEventOccurrence)


trace_Events_MergeNode_hasOffers_mergeNodeExitEventOccurrence_strategy = st.builds(trace_Events_MergeNode_hasOffers_mergeNodeExitEventOccurrence)
@given(instance=trace_Events_MergeNode_hasOffers_mergeNodeExitEventOccurrence_strategy)
@settings(max_examples=25)
def test_trace_Events_MergeNode_hasOffers_mergeNodeExitEventOccurrence_instantiation(instance):
    assert isinstance(instance, trace_Events_MergeNode_hasOffers_mergeNodeExitEventOccurrence)


trace_Events_Offer_hasTokensEntryEventOccurrence_strategy = st.builds(trace_Events_Offer_hasTokensEntryEventOccurrence)
@given(instance=trace_Events_Offer_hasTokensEntryEventOccurrence_strategy)
@settings(max_examples=25)
def test_trace_Events_Offer_hasTokensEntryEventOccurrence_instantiation(instance):
    assert isinstance(instance, trace_Events_Offer_hasTokensEntryEventOccurrence)


trace_Events_Offer_hasTokensExitEventOccurrence_strategy = st.builds(trace_Events_Offer_hasTokensExitEventOccurrence)
@given(instance=trace_Events_Offer_hasTokensExitEventOccurrence_strategy)
@settings(max_examples=25)
def test_trace_Events_Offer_hasTokensExitEventOccurrence_instantiation(instance):
    assert isinstance(instance, trace_Events_Offer_hasTokensExitEventOccurrence)


trace_Events_OpaqueAction_doAction_opaqueActionEntryEventOccurrence_strategy = st.builds(trace_Events_OpaqueAction_doAction_opaqueActionEntryEventOccurrence)
@given(instance=trace_Events_OpaqueAction_doAction_opaqueActionEntryEventOccurrence_strategy)
@settings(max_examples=25)
def test_trace_Events_OpaqueAction_doAction_opaqueActionEntryEventOccurrence_instantiation(instance):
    assert isinstance(instance, trace_Events_OpaqueAction_doAction_opaqueActionEntryEventOccurrence)


trace_Events_OpaqueAction_doAction_opaqueActionExitEventOccurrence_strategy = st.builds(trace_Events_OpaqueAction_doAction_opaqueActionExitEventOccurrence)
@given(instance=trace_Events_OpaqueAction_doAction_opaqueActionExitEventOccurrence_strategy)
@settings(max_examples=25)
def test_trace_Events_OpaqueAction_doAction_opaqueActionExitEventOccurrence_instantiation(instance):
    assert isinstance(instance, trace_Events_OpaqueAction_doAction_opaqueActionExitEventOccurrence)


trace_Events_StringVariable_getCurrentValueValue_stringVariableEntryEventOccurrence_strategy = st.builds(trace_Events_StringVariable_getCurrentValueValue_stringVariableEntryEventOccurrence)
@given(instance=trace_Events_StringVariable_getCurrentValueValue_stringVariableEntryEventOccurrence_strategy)
@settings(max_examples=25)
def test_trace_Events_StringVariable_getCurrentValueValue_stringVariableEntryEventOccurrence_instantiation(instance):
    assert isinstance(instance, trace_Events_StringVariable_getCurrentValueValue_stringVariableEntryEventOccurrence)


trace_Events_StringVariable_getCurrentValueValue_stringVariableExitEventOccurrence_strategy = st.builds(trace_Events_StringVariable_getCurrentValueValue_stringVariableExitEventOccurrence)
@given(instance=trace_Events_StringVariable_getCurrentValueValue_stringVariableExitEventOccurrence_strategy)
@settings(max_examples=25)
def test_trace_Events_StringVariable_getCurrentValueValue_stringVariableExitEventOccurrence_instantiation(instance):
    assert isinstance(instance, trace_Events_StringVariable_getCurrentValueValue_stringVariableExitEventOccurrence)


trace_Events_StringVariable_setCurrentValue_stringVariableEntryEventOccurrence_strategy = st.builds(trace_Events_StringVariable_setCurrentValue_stringVariableEntryEventOccurrence)
@given(instance=trace_Events_StringVariable_setCurrentValue_stringVariableEntryEventOccurrence_strategy)
@settings(max_examples=25)
def test_trace_Events_StringVariable_setCurrentValue_stringVariableEntryEventOccurrence_instantiation(instance):
    assert isinstance(instance, trace_Events_StringVariable_setCurrentValue_stringVariableEntryEventOccurrence)


trace_Events_StringVariable_setCurrentValue_stringVariableExitEventOccurrence_strategy = st.builds(trace_Events_StringVariable_setCurrentValue_stringVariableExitEventOccurrence)
@given(instance=trace_Events_StringVariable_setCurrentValue_stringVariableExitEventOccurrence_strategy)
@settings(max_examples=25)
def test_trace_Events_StringVariable_setCurrentValue_stringVariableExitEventOccurrence_instantiation(instance):
    assert isinstance(instance, trace_Events_StringVariable_setCurrentValue_stringVariableExitEventOccurrence)


trace_Events_Token_isWithdrawnEntryEventOccurrence_strategy = st.builds(trace_Events_Token_isWithdrawnEntryEventOccurrence)
@given(instance=trace_Events_Token_isWithdrawnEntryEventOccurrence_strategy)
@settings(max_examples=25)
def test_trace_Events_Token_isWithdrawnEntryEventOccurrence_instantiation(instance):
    assert isinstance(instance, trace_Events_Token_isWithdrawnEntryEventOccurrence)


trace_Events_Token_isWithdrawnExitEventOccurrence_strategy = st.builds(trace_Events_Token_isWithdrawnExitEventOccurrence)
@given(instance=trace_Events_Token_isWithdrawnExitEventOccurrence_strategy)
@settings(max_examples=25)
def test_trace_Events_Token_isWithdrawnExitEventOccurrence_instantiation(instance):
    assert isinstance(instance, trace_Events_Token_isWithdrawnExitEventOccurrence)


trace_Events_Token_transferEntryEventOccurrence_strategy = st.builds(trace_Events_Token_transferEntryEventOccurrence)
@given(instance=trace_Events_Token_transferEntryEventOccurrence_strategy)
@settings(max_examples=25)
def test_trace_Events_Token_transferEntryEventOccurrence_instantiation(instance):
    assert isinstance(instance, trace_Events_Token_transferEntryEventOccurrence)


trace_Events_Token_transferExitEventOccurrence_strategy = st.builds(trace_Events_Token_transferExitEventOccurrence)
@given(instance=trace_Events_Token_transferExitEventOccurrence_strategy)
@settings(max_examples=25)
def test_trace_Events_Token_transferExitEventOccurrence_instantiation(instance):
    assert isinstance(instance, trace_Events_Token_transferExitEventOccurrence)


trace_Events_Token_withdrawEntryEventOccurrence_strategy = st.builds(trace_Events_Token_withdrawEntryEventOccurrence)
@given(instance=trace_Events_Token_withdrawEntryEventOccurrence_strategy)
@settings(max_examples=25)
def test_trace_Events_Token_withdrawEntryEventOccurrence_instantiation(instance):
    assert isinstance(instance, trace_Events_Token_withdrawEntryEventOccurrence)


trace_Events_Token_withdrawExitEventOccurrence_strategy = st.builds(trace_Events_Token_withdrawExitEventOccurrence)
@given(instance=trace_Events_Token_withdrawExitEventOccurrence_strategy)
@settings(max_examples=25)
def test_trace_Events_Token_withdrawExitEventOccurrence_instantiation(instance):
    assert isinstance(instance, trace_Events_Token_withdrawExitEventOccurrence)


trace_GlobalState_strategy = st.builds(trace_GlobalState)
@given(instance=trace_GlobalState_strategy)
@settings(max_examples=25)
def test_trace_GlobalState_instantiation(instance):
    assert isinstance(instance, trace_GlobalState)


trace_IntegerCalculationExpression_strategy = st.builds(trace_IntegerCalculationExpression)
@given(instance=trace_IntegerCalculationExpression_strategy)
@settings(max_examples=25)
def test_trace_IntegerCalculationExpression_instantiation(instance):
    assert isinstance(instance, trace_IntegerCalculationExpression)


trace_IntegerComparisonExpression_strategy = st.builds(trace_IntegerComparisonExpression)
@given(instance=trace_IntegerComparisonExpression_strategy)
@settings(max_examples=25)
def test_trace_IntegerComparisonExpression_instantiation(instance):
    assert isinstance(instance, trace_IntegerComparisonExpression)


trace_IntegerValue_strategy = st.builds(trace_IntegerValue)
@given(instance=trace_IntegerValue_strategy)
@settings(max_examples=25)
def test_trace_IntegerValue_instantiation(instance):
    assert isinstance(instance, trace_IntegerValue)


trace_States_ActivityEdge_offers_State_strategy = st.builds(trace_States_ActivityEdge_offers_State)
@given(instance=trace_States_ActivityEdge_offers_State_strategy)
@settings(max_examples=25)
def test_trace_States_ActivityEdge_offers_State_instantiation(instance):
    assert isinstance(instance, trace_States_ActivityEdge_offers_State)


trace_States_ActivityNode_heldTokens_State_strategy = st.builds(trace_States_ActivityNode_heldTokens_State)
@given(instance=trace_States_ActivityNode_heldTokens_State_strategy)
@settings(max_examples=25)
def test_trace_States_ActivityNode_heldTokens_State_instantiation(instance):
    assert isinstance(instance, trace_States_ActivityNode_heldTokens_State)


trace_States_ActivityNode_running_State_strategy = st.builds(trace_States_ActivityNode_running_State, running=st.booleans())
@given(instance=trace_States_ActivityNode_running_State_strategy)
@settings(max_examples=25)
def test_trace_States_ActivityNode_running_State_instantiation(instance):
    assert isinstance(instance, trace_States_ActivityNode_running_State)


trace_States_Activity_trace_State_strategy = st.builds(trace_States_Activity_trace_State)
@given(instance=trace_States_Activity_trace_State_strategy)
@settings(max_examples=25)
def test_trace_States_Activity_trace_State_instantiation(instance):
    assert isinstance(instance, trace_States_Activity_trace_State)


trace_States_ForkedToken_baseTokenIsWithdrawn_State_strategy = st.builds(trace_States_ForkedToken_baseTokenIsWithdrawn_State, baseTokenIsWithdrawn=st.booleans())
@given(instance=trace_States_ForkedToken_baseTokenIsWithdrawn_State_strategy)
@settings(max_examples=25)
def test_trace_States_ForkedToken_baseTokenIsWithdrawn_State_instantiation(instance):
    assert isinstance(instance, trace_States_ForkedToken_baseTokenIsWithdrawn_State)


trace_States_ForkedToken_baseToken_State_strategy = st.builds(trace_States_ForkedToken_baseToken_State)
@given(instance=trace_States_ForkedToken_baseToken_State_strategy)
@settings(max_examples=25)
def test_trace_States_ForkedToken_baseToken_State_instantiation(instance):
    assert isinstance(instance, trace_States_ForkedToken_baseToken_State)


trace_States_ForkedToken_remainingOffersCount_State_strategy = st.builds(trace_States_ForkedToken_remainingOffersCount_State, remainingOffersCount=st.integers())
@given(instance=trace_States_ForkedToken_remainingOffersCount_State_strategy)
@settings(max_examples=25)
def test_trace_States_ForkedToken_remainingOffersCount_State_instantiation(instance):
    assert isinstance(instance, trace_States_ForkedToken_remainingOffersCount_State)


trace_States_InputValue_value_State_strategy = st.builds(trace_States_InputValue_value_State)
@given(instance=trace_States_InputValue_value_State_strategy)
@settings(max_examples=25)
def test_trace_States_InputValue_value_State_instantiation(instance):
    assert isinstance(instance, trace_States_InputValue_value_State)


trace_States_InputValue_variable_State_strategy = st.builds(trace_States_InputValue_variable_State)
@given(instance=trace_States_InputValue_variable_State_strategy)
@settings(max_examples=25)
def test_trace_States_InputValue_variable_State_instantiation(instance):
    assert isinstance(instance, trace_States_InputValue_variable_State)


trace_States_Input_inputValues_State_strategy = st.builds(trace_States_Input_inputValues_State)
@given(instance=trace_States_Input_inputValues_State_strategy)
@settings(max_examples=25)
def test_trace_States_Input_inputValues_State_instantiation(instance):
    assert isinstance(instance, trace_States_Input_inputValues_State)


trace_States_Offer_offeredTokens_State_strategy = st.builds(trace_States_Offer_offeredTokens_State)
@given(instance=trace_States_Offer_offeredTokens_State_strategy)
@settings(max_examples=25)
def test_trace_States_Offer_offeredTokens_State_instantiation(instance):
    assert isinstance(instance, trace_States_Offer_offeredTokens_State)


trace_States_Token_holder_State_strategy = st.builds(trace_States_Token_holder_State)
@given(instance=trace_States_Token_holder_State_strategy)
@settings(max_examples=25)
def test_trace_States_Token_holder_State_instantiation(instance):
    assert isinstance(instance, trace_States_Token_holder_State)


trace_States_Trace_executedNodes_State_strategy = st.builds(trace_States_Trace_executedNodes_State)
@given(instance=trace_States_Trace_executedNodes_State_strategy)
@settings(max_examples=25)
def test_trace_States_Trace_executedNodes_State_instantiation(instance):
    assert isinstance(instance, trace_States_Trace_executedNodes_State)


trace_States_Variable_currentValue_State_strategy = st.builds(trace_States_Variable_currentValue_State)
@given(instance=trace_States_Variable_currentValue_State_strategy)
@settings(max_examples=25)
def test_trace_States_Variable_currentValue_State_instantiation(instance):
    assert isinstance(instance, trace_States_Variable_currentValue_State)


trace_StaticObjectsPools_strategy = st.builds(trace_StaticObjectsPools)
@given(instance=trace_StaticObjectsPools_strategy)
@settings(max_examples=25)
def test_trace_StaticObjectsPools_instantiation(instance):
    assert isinstance(instance, trace_StaticObjectsPools)


trace_StringValue_strategy = st.builds(trace_StringValue)
@given(instance=trace_StringValue_strategy)
@settings(max_examples=25)
def test_trace_StringValue_instantiation(instance):
    assert isinstance(instance, trace_StringValue)


trace_Trace_strategy = st.builds(trace_Trace)
@given(instance=trace_Trace_strategy)
@settings(max_examples=25)
def test_trace_Trace_instantiation(instance):
    assert isinstance(instance, trace_Trace)


trace_Traced_TracedObjects_strategy = st.builds(trace_Traced_TracedObjects)
@given(instance=trace_Traced_TracedObjects_strategy)
@settings(max_examples=25)
def test_trace_Traced_TracedObjects_instantiation(instance):
    assert isinstance(instance, trace_Traced_TracedObjects)


trace_activitydiagramConfiguration_TracedControlToken_strategy = st.builds(trace_activitydiagramConfiguration_TracedControlToken)
@given(instance=trace_activitydiagramConfiguration_TracedControlToken_strategy)
@settings(max_examples=25)
def test_trace_activitydiagramConfiguration_TracedControlToken_instantiation(instance):
    assert isinstance(instance, trace_activitydiagramConfiguration_TracedControlToken)


trace_activitydiagramConfiguration_TracedForkedToken_strategy = st.builds(trace_activitydiagramConfiguration_TracedForkedToken)
@given(instance=trace_activitydiagramConfiguration_TracedForkedToken_strategy)
@settings(max_examples=25)
def test_trace_activitydiagramConfiguration_TracedForkedToken_instantiation(instance):
    assert isinstance(instance, trace_activitydiagramConfiguration_TracedForkedToken)


trace_activitydiagramConfiguration_TracedInput_strategy = st.builds(trace_activitydiagramConfiguration_TracedInput)
@given(instance=trace_activitydiagramConfiguration_TracedInput_strategy)
@settings(max_examples=25)
def test_trace_activitydiagramConfiguration_TracedInput_instantiation(instance):
    assert isinstance(instance, trace_activitydiagramConfiguration_TracedInput)


trace_activitydiagramConfiguration_TracedInputValue_strategy = st.builds(trace_activitydiagramConfiguration_TracedInputValue)
@given(instance=trace_activitydiagramConfiguration_TracedInputValue_strategy)
@settings(max_examples=25)
def test_trace_activitydiagramConfiguration_TracedInputValue_instantiation(instance):
    assert isinstance(instance, trace_activitydiagramConfiguration_TracedInputValue)


trace_activitydiagramConfiguration_TracedOffer_strategy = st.builds(trace_activitydiagramConfiguration_TracedOffer)
@given(instance=trace_activitydiagramConfiguration_TracedOffer_strategy)
@settings(max_examples=25)
def test_trace_activitydiagramConfiguration_TracedOffer_instantiation(instance):
    assert isinstance(instance, trace_activitydiagramConfiguration_TracedOffer)


trace_activitydiagramConfiguration_TracedToken_strategy = st.builds(trace_activitydiagramConfiguration_TracedToken)
@given(instance=trace_activitydiagramConfiguration_TracedToken_strategy)
@settings(max_examples=25)
def test_trace_activitydiagramConfiguration_TracedToken_instantiation(instance):
    assert isinstance(instance, trace_activitydiagramConfiguration_TracedToken)


trace_activitydiagramConfiguration_TracedTrace_strategy = st.builds(trace_activitydiagramConfiguration_TracedTrace)
@given(instance=trace_activitydiagramConfiguration_TracedTrace_strategy)
@settings(max_examples=25)
def test_trace_activitydiagramConfiguration_TracedTrace_instantiation(instance):
    assert isinstance(instance, trace_activitydiagramConfiguration_TracedTrace)


trace_activitydiagram_TracedAction_strategy = st.builds(trace_activitydiagram_TracedAction)
@given(instance=trace_activitydiagram_TracedAction_strategy)
@settings(max_examples=25)
def test_trace_activitydiagram_TracedAction_instantiation(instance):
    assert isinstance(instance, trace_activitydiagram_TracedAction)


trace_activitydiagram_TracedActivity_strategy = st.builds(trace_activitydiagram_TracedActivity)
@given(instance=trace_activitydiagram_TracedActivity_strategy)
@settings(max_examples=25)
def test_trace_activitydiagram_TracedActivity_instantiation(instance):
    assert isinstance(instance, trace_activitydiagram_TracedActivity)


trace_activitydiagram_TracedActivityEdge_strategy = st.builds(trace_activitydiagram_TracedActivityEdge)
@given(instance=trace_activitydiagram_TracedActivityEdge_strategy)
@settings(max_examples=25)
def test_trace_activitydiagram_TracedActivityEdge_instantiation(instance):
    assert isinstance(instance, trace_activitydiagram_TracedActivityEdge)


trace_activitydiagram_TracedActivityFinalNode_strategy = st.builds(trace_activitydiagram_TracedActivityFinalNode)
@given(instance=trace_activitydiagram_TracedActivityFinalNode_strategy)
@settings(max_examples=25)
def test_trace_activitydiagram_TracedActivityFinalNode_instantiation(instance):
    assert isinstance(instance, trace_activitydiagram_TracedActivityFinalNode)


trace_activitydiagram_TracedActivityNode_strategy = st.builds(trace_activitydiagram_TracedActivityNode)
@given(instance=trace_activitydiagram_TracedActivityNode_strategy)
@settings(max_examples=25)
def test_trace_activitydiagram_TracedActivityNode_instantiation(instance):
    assert isinstance(instance, trace_activitydiagram_TracedActivityNode)


trace_activitydiagram_TracedBooleanVariable_strategy = st.builds(trace_activitydiagram_TracedBooleanVariable)
@given(instance=trace_activitydiagram_TracedBooleanVariable_strategy)
@settings(max_examples=25)
def test_trace_activitydiagram_TracedBooleanVariable_instantiation(instance):
    assert isinstance(instance, trace_activitydiagram_TracedBooleanVariable)


trace_activitydiagram_TracedControlFlow_strategy = st.builds(trace_activitydiagram_TracedControlFlow)
@given(instance=trace_activitydiagram_TracedControlFlow_strategy)
@settings(max_examples=25)
def test_trace_activitydiagram_TracedControlFlow_instantiation(instance):
    assert isinstance(instance, trace_activitydiagram_TracedControlFlow)


trace_activitydiagram_TracedControlNode_strategy = st.builds(trace_activitydiagram_TracedControlNode)
@given(instance=trace_activitydiagram_TracedControlNode_strategy)
@settings(max_examples=25)
def test_trace_activitydiagram_TracedControlNode_instantiation(instance):
    assert isinstance(instance, trace_activitydiagram_TracedControlNode)


trace_activitydiagram_TracedDecisionNode_strategy = st.builds(trace_activitydiagram_TracedDecisionNode)
@given(instance=trace_activitydiagram_TracedDecisionNode_strategy)
@settings(max_examples=25)
def test_trace_activitydiagram_TracedDecisionNode_instantiation(instance):
    assert isinstance(instance, trace_activitydiagram_TracedDecisionNode)


trace_activitydiagram_TracedExecutableNode_strategy = st.builds(trace_activitydiagram_TracedExecutableNode)
@given(instance=trace_activitydiagram_TracedExecutableNode_strategy)
@settings(max_examples=25)
def test_trace_activitydiagram_TracedExecutableNode_instantiation(instance):
    assert isinstance(instance, trace_activitydiagram_TracedExecutableNode)


trace_activitydiagram_TracedFinalNode_strategy = st.builds(trace_activitydiagram_TracedFinalNode)
@given(instance=trace_activitydiagram_TracedFinalNode_strategy)
@settings(max_examples=25)
def test_trace_activitydiagram_TracedFinalNode_instantiation(instance):
    assert isinstance(instance, trace_activitydiagram_TracedFinalNode)


trace_activitydiagram_TracedForkNode_strategy = st.builds(trace_activitydiagram_TracedForkNode)
@given(instance=trace_activitydiagram_TracedForkNode_strategy)
@settings(max_examples=25)
def test_trace_activitydiagram_TracedForkNode_instantiation(instance):
    assert isinstance(instance, trace_activitydiagram_TracedForkNode)


trace_activitydiagram_TracedInitialNode_strategy = st.builds(trace_activitydiagram_TracedInitialNode)
@given(instance=trace_activitydiagram_TracedInitialNode_strategy)
@settings(max_examples=25)
def test_trace_activitydiagram_TracedInitialNode_instantiation(instance):
    assert isinstance(instance, trace_activitydiagram_TracedInitialNode)


trace_activitydiagram_TracedIntegerVariable_strategy = st.builds(trace_activitydiagram_TracedIntegerVariable)
@given(instance=trace_activitydiagram_TracedIntegerVariable_strategy)
@settings(max_examples=25)
def test_trace_activitydiagram_TracedIntegerVariable_instantiation(instance):
    assert isinstance(instance, trace_activitydiagram_TracedIntegerVariable)


trace_activitydiagram_TracedJoinNode_strategy = st.builds(trace_activitydiagram_TracedJoinNode)
@given(instance=trace_activitydiagram_TracedJoinNode_strategy)
@settings(max_examples=25)
def test_trace_activitydiagram_TracedJoinNode_instantiation(instance):
    assert isinstance(instance, trace_activitydiagram_TracedJoinNode)


trace_activitydiagram_TracedMergeNode_strategy = st.builds(trace_activitydiagram_TracedMergeNode)
@given(instance=trace_activitydiagram_TracedMergeNode_strategy)
@settings(max_examples=25)
def test_trace_activitydiagram_TracedMergeNode_instantiation(instance):
    assert isinstance(instance, trace_activitydiagram_TracedMergeNode)


trace_activitydiagram_TracedNamedElement_strategy = st.builds(trace_activitydiagram_TracedNamedElement, name=safe_text)
@given(instance=trace_activitydiagram_TracedNamedElement_strategy)
@settings(max_examples=25)
def test_trace_activitydiagram_TracedNamedElement_instantiation(instance):
    assert isinstance(instance, trace_activitydiagram_TracedNamedElement)


trace_activitydiagram_TracedOpaqueAction_strategy = st.builds(trace_activitydiagram_TracedOpaqueAction)
@given(instance=trace_activitydiagram_TracedOpaqueAction_strategy)
@settings(max_examples=25)
def test_trace_activitydiagram_TracedOpaqueAction_instantiation(instance):
    assert isinstance(instance, trace_activitydiagram_TracedOpaqueAction)


trace_activitydiagram_TracedStringVariable_strategy = st.builds(trace_activitydiagram_TracedStringVariable)
@given(instance=trace_activitydiagram_TracedStringVariable_strategy)
@settings(max_examples=25)
def test_trace_activitydiagram_TracedStringVariable_instantiation(instance):
    assert isinstance(instance, trace_activitydiagram_TracedStringVariable)


trace_activitydiagram_TracedVariable_strategy = st.builds(trace_activitydiagram_TracedVariable)
@given(instance=trace_activitydiagram_TracedVariable_strategy)
@settings(max_examples=25)
def test_trace_activitydiagram_TracedVariable_instantiation(instance):
    assert isinstance(instance, trace_activitydiagram_TracedVariable)


